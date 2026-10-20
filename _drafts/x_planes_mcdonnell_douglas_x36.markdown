---
layout: post
mathjax: true
comments: true
title: "X-Planes: McDonnell Douglas X-36"
date: 2025-11-11 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 37
---
<!-- A333 -->
<script>console.log("A333");</script>

The [McDonnell Douglas X-36][ref_x36] had no vertical tail and no horizontal tail, and every account of it
begins there. **The more interesting number is 28 percent.** The aircraft was a
[subscale model][ref_museum], which the
[National Aeronautics and Space Administration's programme account][ref_nasa_x36] and its
[inventory of American X-vehicles][ref_american_x_vehicles] both describe as a 28 percent scale
representation of a fighter. It flew with nobody aboard, from a [ground station][ref_nasa_x36] whose pilot watched through a
camera in its nose. Its [published specification][ref_x36] gives a maximum weight of 1,270 pounds and a
height of 0.946 metres. This is the thirty-seventh article
in the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1],
the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the
[X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the
[X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the
[X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the
[X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the
[X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], the
[X-14][related_post_a311_bell_x14], the [X-15][related_post_a312_north_american_x15], the
[X-16][related_post_a313_bell_x16], the [X-17][related_post_a314_lockheed_x17], the
[X-18][related_post_a315_hiller_x18], the [X-19][related_post_a316_curtiss_wright_x19], the
[X-20][related_post_a317_boeing_x20], the [X-21][related_post_a318_northrop_x21], the
[X-22][related_post_a319_bell_x22], the [X-23][related_post_a320_martin_marietta_x23], the
[X-24][related_post_a321_martin_marietta_x24], the [X-25][related_post_a322_bensen_x25], the
[X-26][related_post_a323_schweizer_x26], the [X-27][related_post_a324_lockheed_x27], the
[X-28][related_post_a325_osprey_x28], the [X-29][related_post_a326_grumman_x29], the
[X-30][related_post_a327_rockwell_x30], the [X-31][related_post_a328_rockwell_mbb_x31], the
[X-32][related_post_a329_boeing_x32], the [X-33][related_post_a330_lockheed_martin_x33], the
[X-34][related_post_a331_orbital_sciences_x34], and the [X-35][related_post_a332_lockheed_martin_x35].

**A scale factor is not a detail of the hardware. It decides what the experiment is able to measure**,
and here the decision has a sharp edge, because the choice that makes the aeroplane's motions
representative is the same choice that makes it harder to fly than the aircraft it represents.

## The Research Question

### The Question Everybody Asks

Can a fighter fly without a vertical tail? The tail costs weight, drag and radar return, and removing it
would buy all three back.
**Nobody had done it because the vertical tail keeps the aeroplane pointing where it is going**,
the property known as [directional stability][ref_directional]. A fuselage in sideslip generates a yawing moment that
turns it further into the sideslip, and the fin exists to overcome that. Take the fin away and the aircraft
is directionally unstable, which means that a disturbance grows instead of decaying.

By 1996 that question had an obvious answer in principle.
**A digital flight control system can stabilise an unstable aeroplane**, as the
[X-29][related_post_a326_grumman_x29] had already shown for a different instability, and the effectors to do
it in yaw were available in the form of split ailerons and a vectoring nozzle.
**So the question was not whether it could be done. It was whether it could be done well enough to be worth doing, at the angles of attack where a fighter earns its living.**

### The Question This Article Asks Instead

**The X-36 answered that question at 28 percent scale, and a 28 percent aeroplane is not a small aeroplane. It is a different aeroplane**,
obeying different combinations of the dimensionless groups that govern flight.

**So this article asks what the scale factor bought and what it cost.** Three quantities matter, they cannot
all be matched at once, and the choice among them defines the experiment. The answer turns
out to have an edge that the programme's own accounts do not mention.

**A preview.** Matching the right quantity makes the model's motions faithful and simultaneously makes them
**1.89 times faster in real time** than the full-scale aircraft's. The delay in a video link and the
reaction time of a human being do not get faster to match.
**The demonstration was therefore harder than the thing it demonstrated, by a factor this article computes**,
and that makes the result stronger and not weaker.

**The previous article found the opposite.** The [X-35's][related_post_a332_lockheed_martin_x35] most famous
sortie was flown in the easiest available ordering, at a weight the production aircraft would never see.
**This one was flown against a handicap the full-scale aircraft would never carry.** Two consecutive
demonstrators, opposite directions, and both differences are arithmetic, not opinion.

## Programme Origin

### Who Wanted the Answer

The programme was a partnership between McDonnell Douglas, whose [Phantom Works][ref_phantom_works] built
the aircraft, and the [National Aeronautics and Space Administration][ref_nasa], which
[supplied the flight research infrastructure][ref_nasa_x36] at [Dryden][ref_dryden].
**The cost of the tail explains why the question was asked and why it was asked then.** A vertical
tail is a large flat surface standing proud of the fuselage, which makes it the worst thing to have on
an aircraft designed to be difficult to see on radar, and [Walker 1997][research_walkerlaurencea_1997], the programme's test
pilot, wrote that stealth had recently become an important design consideration.

Two aircraft were built, and the [programme account][ref_nasa_x36] records that their fabrication began in 1994.

Research on who wanted the answer, and why, is gathered in The Contemporary Literature in the cluster on the X-36, X-29 and X-31 demonstrators and the cluster on radar signature and low observability.

### Why a Model Rather Than an Aeroplane

**The alternative to a subscale demonstrator was a piloted one, and the arithmetic of that comparison favoured an X-36 over an X-36-sized fighter.**
A piloted aircraft needs a cockpit, an escape system, a life support system, redundant everything, and a
structure certified to carry a person.
**None of that is cheap and none of it is relevant to the question being asked**, which is whether a control
law can hold a tailless configuration pointing straight. [Walker 1997][research_walkerlaurencea_1997] records that cost was the
major driver of the subscale decision, because cost correlates strongly with size.

The trade is that a model cannot answer every question, and the rest of this article is about which ones it
cannot.

For the research on this question, see the clusters on similitude, dynamic scaling and subscale flight testing and on unmanned aircraft, ground stations and remote piloting, under The Contemporary Literature.

## Sizing From First Principles

### Three Dimensionless Numbers and Only One Can Be Matched

**The design of the experiment follows from three lines of algebra.** An aeroplane's behaviour is
governed by the ratio of inertia to gravity, the [Froude number][ref_froude], by the ratio of
inertia to viscosity, the [Reynolds number][ref_reynolds], and by the ratio of speed to the speed
of sound. The general requirement that a model reproduce its original is [similitude][ref_similitude].
Writing $V$ for speed, $L$ for a length, $g$ for gravity, $\nu$ for kinematic viscosity and $a$ for the
speed of sound,

$$\mathrm{Fr} = \frac{V^{2}}{gL} \qquad \mathrm{Re} = \frac{VL}{\nu} \qquad \mathrm{M} = \frac{V}{a}$$

**A model in the same air as the full-scale aircraft has only one free variable, its speed**, so it
can match one of the three and must accept whatever the other two become. Writing $\lambda$ for the length
ratio and $r_V$ for the velocity ratio,

$$\frac{\mathrm{Fr}_m}{\mathrm{Fr}_f} = \frac{r_V^{2}}{\lambda} \qquad \frac{\mathrm{Re}_m}{\mathrm{Re}_f} = r_V \lambda \qquad \frac{\mathrm{M}_m}{\mathrm{M}_f} = r_V$$

At $\lambda = 0.28$ the three choices are these.

| Matched | Velocity ratio | Froude ratio | Mach ratio | Reynolds ratio |
|---|---|---|---|---|
| **Froude** | **0.5292** | **1.000** | 0.5292 | 0.1482 |
| Mach | 1.000 | 3.571 | 1.000 | 0.2800 |
| Reynolds | 3.571 | 45.55 | 3.571 | 1.000 |

**Read the last row first, because it disposes of an option people reach for.** Matching Reynolds number
would require the model to fly at 3.571 times the full-scale aircraft's speed, and its Froude number would
then be wrong by a factor of 45.55. A model flown that way does not fall the way an aeroplane falls.
**It is useless for flight dynamics and the row exists only to be dismissed.**

Matching Mach number, as a wind tunnel usually does, leaves the Froude number wrong by 3.571.
**Such a model is fine for measuring pressures and useless for measuring motion**, because the model's weight and
its aerodynamic forces are then in the wrong proportion.

**So a free-flight model that is meant to move like an aeroplane must match Froude, and every other ratio follows from that decision.**

The Contemporary Literature takes this subject up mainly in its cluster on similitude, dynamic scaling and subscale flight testing.

### What Froude Matching Does to Everything Else

Setting the Froude ratio to one gives $r_V = \sqrt{\lambda}$, and the rest follows by dimensions alone.

$$r_V = r_t = \sqrt{\lambda} = \sqrt{0.28} = 0.5292$$

$$r_\omega = \frac{1}{\sqrt{\lambda}} = 1.8898 \qquad r_{\dot\omega} = \frac{1}{\lambda} = 3.571$$

$$r_m = \lambda^{3} \qquad r_I = \lambda^{5} = 0.001721 \qquad r_{\mathrm{Re}} = \lambda^{3/2} = 0.1482$$

**Deriving the mass and inertia exponents is better than quoting them.** Holding density common makes mass
go as volume, the cube of length. A moment is a force times a length and a force at matched Froude number
goes as mass, so

$$r_F = \lambda^{3} \qquad r_M = r_F \lambda = \lambda^{4} \qquad r_I = r_m \lambda^{2} = \lambda^{5}$$

and the angular acceleration ratio is the moment ratio over the inertia ratio,

$$r_{\dot\omega} = \frac{\lambda^{4}}{\lambda^{5}} = \frac{1}{\lambda} = 3.571$$

**Each of those is an identity in the scale factor and holds at every value of it, not at 0.28 alone**,
because each exponent follows from dimensions and not from the particular aircraft.

**Three of them deserve reading slowly.**

**Time runs at 0.5292 of full scale**, which is to say every motion of the model happens 1.8898 times faster
in real seconds than the corresponding motion of the aeroplane it represents.

**Angular accelerations are 3.571 times larger.** Not the angles and not the rates, but the accelerations,
because moments scale as the fourth power of length and inertias as the fifth.

**Reynolds number is 0.1482 of full scale, a penalty of 6.749.** The penalty is the price of the choice, and it
falls on the separated flow at high angle of attack that the experiment exists to study.
**How much it costs is a separate question from how large the ratio is**, and the comparison
section below computes both Reynolds numbers so that the factor does not have to speak for itself.

### The Check That Costs Nothing

**If the aeroplane is a Froude-scaled model then its weight fixes the aeroplane it stands for**,
because mass scales as the cube of length. Inverting,

$$W_f = \frac{W_m}{\lambda^{3}} = \frac{1{,}270}{0.28^{3}} = 57{,}853 \ \text{lb}$$

and its empty weight likewise gives 49,654 pounds, while its dimensions give a full-scale length of 19.82
metres and a span of 11.34 metres.

**Those numbers describe a real class of aeroplane.** Sixty-five feet long, thirty-seven feet in span and
fifty-eight thousand pounds is the size of a heavy twin-engined fighter, a plausible class for the theoretical
advanced fighter that the [programme account][ref_nasa_x36] says the aircraft represented.
**The consistency is not a proof, because the designers chose the model's weight and could have chosen it to be consistent. It is a check that would have failed loudly had the aircraft not been dynamically scaled at all**,
and it did not fail.

The speeds convert the same way. The [published specification][ref_x36] gives a 243 knot maximum speed
limit and a 110 knot approach speed, and dividing each by the velocity ratio gives the full-scale equivalent,

$$V_f = \frac{V_m}{\sqrt{\lambda}} = \frac{243}{0.5292} = 459.2 \ \text{kt} \qquad V_f = \frac{110}{0.5292} = 207.9 \ \text{kt}$$

for model speed $V_m$ and full-scale speed $V_f$.
**A 208 knot approach is fast for a fighter.**

The same cluster on similitude, dynamic scaling and subscale flight testing holds the research records behind this check.

### The Handicap the Accounts Do Not Mention

**Here is the edge on the scale factor, and it follows from the time ratio in one step.**

The model's motions run 1.8898 times faster than the full-scale aircraft's.
**A delay in the command and video path does not run faster.** It is a fixed number of milliseconds imposed
by cameras, encoders, radio links and displays, the same whatever the
aeroplane is doing. So its significance, measured against the dynamics it is trying to control, is
multiplied by

$$\frac{1}{\sqrt{\lambda}} = 1.8898$$

| Delay in the link | Worth this much at full scale |
|---|---|
| 100 ms | 189.0 ms |
| 150 ms | 283.5 ms |
| 200 ms | 378.0 ms |
| 250 ms | 472.5 ms |

**And the pilot is subject to the same multiplication.** A human [visual reaction time][ref_reaction] of roughly 200
milliseconds, set by the human and not by the aeroplane, counts for **378.0 milliseconds** of
full-scale response.

**No latency figure for this aircraft's link has been published, so the article does not claim one.** What
it claims is the structure.
**Whatever the delay was, it was worth 1.8898 times as much as the same delay in a piloted full-scale aircraft**,
and the ground pilot was flying an aeroplane whose divergences developed nearly twice as quickly as the ones
the programme was trying to learn about.

**This is why the result is stronger than it looks.** A demonstration flown under a handicap that the
operational article would not carry proves more than a demonstration flown without it, and the previous
article in this series is the case where that ran the other way.

The clusters on time delay, latency and delay compensation and on handling qualities, pilot-induced oscillation and the pilot model, in The Contemporary Literature, gather the research on this handicap.

### What the Missing Fin Costs

**A fuselage in sideslip is destabilising and the reason is older than aeronautics.** A slender body at an
angle to the flow carries a moment that turns it further from alignment, and a fin behind the centre of
gravity produces an opposing moment that grows with the same sideslip. The sum is the directional stability
derivative. Writing $N$ for yawing moment, $q$ for dynamic pressure, $S$ for wing area, $b$ for span and
$\beta$ for sideslip,

$$N = q S b \, C_{n\beta} \, \beta$$

**With a fin, $C_{n\beta}$ is positive and the aircraft weathercocks. Without one it is negative and the aircraft diverges.**
The rest of this section follows from that sign change.

**The magnitude can be derived, not assumed, and it should be.** Slender-body theory gives the
destabilising moment of a body from its **volume alone**, through the apparent-mass difference $k_2 - k_1$,
which for a fineness ratio above about eight is near 0.9.
**The result is older than aeronautical stability and control as a discipline**, having been set out by Max
Munk in 1924 in [a study of the aerodynamic forces on airship hulls][research_munkmaxm_1924], and the
correction that makes it usable at real angles of attack, where the potential result must be supplemented by
cross-flow drag, was published in
[Allen and Perkins 1951][research_allenhjulian_perkinsedwardw_1951].
**Both are the primary sources for the relation this article displays.** The derivative per radian is

$$C_{n\beta}^{\text{body}} = -\left(k_2 - k_1\right) \frac{2 \, \mathrm{Vol}}{S b}$$

**The fuselage volume is not published either, so it is bracketed.**

| Fuselage volume | $C_{n\beta}$ per radian | Per degree |
|---|---|---|
| 0.60 m³ | 0.1041 | 0.001816 |
| 0.80 m³ | 0.1388 | 0.002422 |
| 1.00 m³ | 0.1734 | 0.003027 |

**The derived value at the middle of the bracket is 0.002422 per degree, which is 2.018 times the assumed value of 0.0012, a figure typical of a tailless configuration.**
That matters, and in a welcome direction. **The assumed figure is the optimistic one**, so the
aircraft was more unstable than the rows computed from it suggest, and
**every conclusion that survives the optimistic case survives the derived one more comfortably.** Both are
carried through the tables that follow, and neither replaces the other.

**The wing area is not published, so it is inverted from what is.** The approach speed of 110 knots and a
landing weight of about 1,153 pounds, taken as the empty weight with 35 percent of the fuel remaining, fix the product of area and lift coefficient, and at an approach
coefficient of 0.8 that gives

$$S = \frac{W}{q C_L} = \frac{5{,}129}{1{,}961 \times 0.8} = 3.269 \ \text{m}^{2}$$

and the geometry follows from it,

$$\mathrm{AR} = \frac{b^{2}}{S} = \frac{3.175^{2}}{3.269} = 3.084 \qquad \bar{c} = \frac{S}{b} = 1.029 \ \text{m}$$

$$\frac{W}{S} = \frac{1{,}270 \times 0.4536 \times 9.807}{3.269} = 1{,}728 \ \text{N/m}^{2}$$

**The wing loading is therefore 1,728 newtons per square metre at maximum weight**, which at 28 percent scale
corresponds to 6,171 at full size, since wing loading scales as the length ratio.

An aspect ratio near three is right for this planform class, and that agreement checks that the inversion is not
nonsense. Across coefficients from 0.7 to 1.0 the aspect ratio runs from 2.699 to 3.855, so the conclusion
does not depend on the choice.

### How Fast the Divergence Grows

Neglecting damping, the yaw equation for a directionally unstable aircraft is

$$I_{zz} \ddot{\beta} = \lvert C_{n\beta} \rvert q S b \, \beta \qquad \Rightarrow \qquad \ddot{\beta} = \sigma^{2} \beta$$

which grows instead of oscillating. The yaw inertia is unpublished, so it is estimated from a radius of
gyration taken as a fraction of length and reported across a bracket.

**There are two answers to how long a doubling takes and they differ by a factor that is constant.**
The flight dynamics convention measures the growing eigen-solution,

$$t_{2} = \frac{\ln 2}{\sigma}$$

while a disturbance **released from rest** follows a hyperbolic cosine rather than an exponential,
because it starts with no yaw rate at all, and needs

$$t_{2}^{\text{rest}} = \frac{\operatorname{arccosh} 2}{\sigma} = 1.900 \, t_{2}$$

**The ratio is arccosh 2 over ln 2, it is 1.900, and it depends on nothing.** The growth rate cancels from
it, so it holds at every growth rate, and integrating the equation of motion under each of the two initial
conditions reproduces both times without evaluating an exponent.

| Radius of gyration | Modal, 110 kt | From rest, 110 kt | Modal, 243 kt | From rest, 243 kt |
|---|---|---|---|---|
| 0.30 of length | 0.740 s | 1.407 s | 0.335 s | 0.637 s |
| 0.35 of length | 0.864 s | 1.641 s | 0.391 s | 0.743 s |
| 0.40 of length | 0.987 s | 1.876 s | 0.447 s | 0.849 s |

**Those use the assumed derivative. The derived one makes them shorter.** At a radius of gyration of 0.35
the growth rate rises from 0.802 to 1.140 per second at approach and from 1.773 to 2.518 at maximum speed,
so the modal doubling times fall to **0.608 seconds and 0.275 seconds**,

$$t_{2} = \frac{\ln 2}{1.140} = 0.608 \ \text{s} \qquad t_{2} = \frac{\ln 2}{2.518} = 0.275 \ \text{s}$$

by the modal relation above.

**Every entry is under two seconds and most are under one.** That is the number the control system had to
beat and the number the ground pilot's link delay had to be small against.

**The scaling makes the comparison worse in the obvious direction.** The full-scale aircraft's doubling
times would be 1.8898 times longer than these, so the model diverged nearly twice as fast as the aeroplane
it stood for, while the delay in reacting to it stayed the same.
**Both halves of the handicap point the same way.**

Work on the divergence is listed in The Contemporary Literature in the cluster on slender bodies, fuselages and apparent mass, the cluster on directional stability and lateral-directional dynamics and the cluster on flight dynamics, stability derivatives and unstable modes.

### The Delay Budget in Milliseconds

**A fixed delay is amplified by 1.8898. Control theory turns that amplification into a budget, and the budget is small enough to force a conclusion about the architecture.**

A loop that stabilises an unstable pole must cross over above it, because below the pole the loop gain is
not yet doing anything. Writing $\omega_c$ for the crossover frequency and taking a multiple $\kappa$ of the
growth rate,

$$\omega_c = \kappa \sigma$$

**A pure delay contributes phase lag in direct proportion to frequency**, and that proportionality makes delay
dangerous and not merely annoying,

$$\Delta\phi = \omega \tau$$

so at crossover the delay consumes $\omega_c \tau$ of phase. Setting that equal to the phase margin a
designer insists on gives the entire delay budget of the loop,

$$\tau_{\max} = \frac{\phi_m}{\omega_c} = \frac{\phi_m}{\kappa \sigma}$$

**And $\sigma$ scales as one over the square root of the scale factor, so the budget scales as its square root.**
The amplification of 1.8898 reappears here in the units a control engineer would use.

At a phase margin of 45 degrees and a crossover three times the growth rate,

| Condition | Growth rate | Crossover | Budget, model | Budget, full scale |
|---|---|---|---|---|
| 110 kt, assumed derivative | 0.802 /s | 2.41 rad/s | **326.3 ms** | 616.6 ms |
| 243 kt, assumed derivative | 1.773 /s | 5.32 rad/s | **147.7 ms** | 279.1 ms |
| 243 kt, derived derivative | 2.518 /s | 7.55 rad/s | **104.0 ms** | 196.5 ms |

**Read the fourth column, the model budget, against what a video link and a human cost.** A camera, an encoder, a radio path and
a display are not free, and a human [visual reaction time][ref_reaction] alone is around 200 milliseconds.
**The entire budget at maximum speed is between 104 and 148 milliseconds.**

**So the ground pilot cannot have been inside the stabilisation loop, and the architecture follows from the arithmetic rather than from a preference.**
The inner loop that held this aeroplane pointing straight had to be onboard, closing around sensors and
effectors with no radio in the path, while the pilot on the ground flew the aircraft through that loop.
**The aircraft was built that way**, with a digital fly-by-wire system stabilising it in the
[programme account][ref_nasa_x36] and the pilot flying every takeoff, test manoeuvre and landing in
[Walker 1997][research_walkerlaurencea_1997], and this article did not have to be told.

**The budget also explains why the full-scale comparison matters.** The same aeroplane at full size would
have had between 196 and 279 milliseconds, which is roughly a human reaction time.
**A full-scale tailless aircraft could conceivably be flown by a pilot whose hands were in the loop. The 28 percent model could not**,
and that difference is an artefact of the scale alone. The configuration plays no part in it.

Research behind the delay budget sits in the clusters on stability margins and robust control and on time delay, latency and delay compensation.

### Why a Nozzle Complements a Fin

**This is the cleanest result in the article and it comes from noticing which terms carry dynamic pressure.**
A fin's yawing moment is $q S b$ times a coefficient. The destabilising fuselage moment is $q S b$ times
another coefficient. **Both carry $q$, so their ratio does not change with speed**, which is why a fin sized
for one flight condition is sized for all of them.

**A vectored nozzle carries no $q$ at all.** Its moment is thrust times the sine of a deflection times a
moment arm,

$$N_{\text{vec}} = T \ell \sin\delta = 3{,}114 \times 2.220 \times \sin 20^{\circ} = 2{,}364 \ \text{N m}$$

so the ratio of what the nozzle can do to what the aerodynamics demand goes as one over dynamic pressure.
**The nozzle is strongest exactly where the fin is weakest.**

| Speed | Aerodynamic moment at 10 degrees of sideslip | Nozzle authority ratio |
|---|---|---|
| 60 kt | 72.7 N·m | 32.53 |
| 110 kt | 244.3 N·m | 9.679 |
| 160 kt | 516.8 N·m | 4.575 |
| 243 kt | 1,192 N·m | 1.983 |

**Inverting for the speed at which the nozzle alone can no longer hold ten degrees of sideslip gives 342.2 knots**,
because the nozzle authority ratio $R$ falls as the square of speed from its value $R_{243}$ at 243 knots,

$$R(V) = R_{243} \left(\frac{243}{V}\right)^{2} = 1 \qquad \Rightarrow \qquad V_{\text{vec}} = 243 \sqrt{R_{243}} = 243 \sqrt{1.983} = 342.2 \ \text{kt}$$

which is above anything this aircraft ever flew, and well above the
[206 knots it reached][ref_nasa_x36].
**So across its entire envelope the nozzle alone was sufficient.**

### The Unsettled Contribution of the Split Ailerons

A split aileron opens above and below to add drag on one wing, and the yawing moment is that drag increment
acting at its spanwise centroid,

$$N_{\text{dr}} = q \, S_p \, \Delta C_D \, y$$

where $S_p$ is the panel area and $y$ the arm, here 1.111 metres at 35 percent of span.

**The drag increment decides the answer, and it is not published**, so it is bracketed across the range a
split surface can produce, from lightly cracked to fully opened.

| Drag increment | Moment at 243 kt as a share of the nozzle | Speed at which it equals the nozzle |
|---|---|---|
| 0.10 | 22.1 percent | 517.4 kt |
| 0.30 | 66.2 percent | 298.7 kt |
| 0.60 | 132.4 percent | 211.2 kt |

**This limits what can honestly be said.**
At the bottom of the bracket the nozzle dominates everywhere and the split ailerons are margin.
**At the top they overtake the nozzle inside the cleared envelope, at 211.2 knots, and become the primary yaw effector at high speed.**
The drag rudder's moment rises as the square of speed while the nozzle's is constant, so a split-aileron
moment that is a share $s$ of the nozzle's at 243 knots equals it at

$$V_{\times} = \frac{243}{\sqrt{s}} = \frac{243}{\sqrt{1.324}} = 211.2 \ \text{kt}$$

which lies inside the 243 knot limit and a little above the 206 knots the aircraft is [recorded][ref_nasa_x36] as reaching.

**The bracket spans a factor of six and the conclusion flips inside it, so the correct statement is that it is not determined by public information.**
What survives is the structural claim, which does not depend on the increment at all.
**The nozzle's authority is flat with speed and the drag rudder's rises as the square of it**, so whatever
the crossover speed is, the nozzle owns the low-speed end and the split ailerons own the high-speed end.
**The configuration was built around this complementarity, which holds everywhere in the bracket.**

**The complementarity is the general lesson and it survives the particular numbers.** A tailless aircraft
needs an effector whose authority does not vanish with dynamic pressure, because the condition it
most fears is high angle of attack at low speed, where every aerodynamic surface is working in separated
flow and a fin would have stalled even if it were there.

The Contemporary Literature covers yaw effectors in its cluster on thrust vectoring, drag rudders and yaw effectors.

## The Vehicle

[Two aircraft were built][ref_museum]. The configuration is a wing
with a canard ahead of it, no vertical surface of any kind, [split ailerons][ref_american_x_vehicles] on the wing trailing edge that
open into upper and lower halves to make drag on one side, and a [thrust-vectoring][ref_tv] nozzle.
**The figures below are those of the [published specification][ref_x36]**, except the fuel fraction and the
thrust to weight ratio, which are the fuel load and the thrust each divided by the maximum weight,

$$\frac{180}{1{,}270} = 0.1417 \qquad \frac{700}{1{,}270} = 0.5512$$

The [programme account][ref_nasa_x36] gives rounder figures, about 1,250 pounds fully fuelled, 19 feet long
and three feet high, with about 700 pounds of thrust.

| Quantity | Value |
|---|---|
| Length | 18 ft 2.5 in, 5.550 m, including the pitot boom |
| Span | 10 ft 5 in, 3.175 m |
| Height | 3 ft 1.25 in, 0.946 m |
| Empty weight | 1,090 lb |
| Maximum weight | 1,270 lb |
| Fuel | 180 lb, a fraction of 0.1417 |
| Engine | [Williams F112 turbofan][ref_f112], 700 lbf |
| Thrust to weight | 0.5512 |
| Approach speed | 110 kt |
| Maximum speed | 160 kt initially, 243 kt later |
| Ceiling | 20,500 ft |
| Load factor | 5 g |

**The fuel fraction of 0.1417 is the specification that most constrains the programme**, because it is what
limits a sortie to well under an hour, 35 to 45 minutes for a typical research flight in the
[programme account][ref_nasa_x36], and therefore what makes the flight count the resource rather than the
flight hours.

Records on the engine fall in the cluster on turbofan performance, thrust and fuel consumption.

## Dependent Systems

### The Effectors

[Walker 1997][research_walkerlaurencea_1997] lists the control effectors as canards, split ailerons, leading and trailing edge flaps
and thrust vectoring, and the ailerons move [asymmetrically for roll][ref_american_x_vehicles].
**Yaw comes from [two places][ref_nasa_x36] and neither of them is a rudder.** The split ailerons open
asymmetrically to put drag on one wing, producing a yawing moment that grows with dynamic pressure like a
fin's, and the nozzle vectors to produce one that does not.

**An aircraft with more effectors than axes has to decide how to share a demand among them**, the
[control allocation][ref_allocation] problem. That problem is why this configuration needs a digital flight
control system and does not merely benefit from one.

For the research on the effectors, see the cluster on control allocation and redundant effectors and the cluster on thrust vectoring, drag rudders and yaw effectors in The Contemporary Literature.

### The Ground Station

The pilot sat in a ground-based cockpit with a conventional fighter head-up display and a moving map, as the
[programme account][ref_nasa_x36] describes the ground station, looking through a camera that the account
places in the aircraft's nose and that [Walker 1997][research_walkerlaurencea_1997] places on its canopy.
**The arrangement keeps the latency argument above from being academic.** Every element of that chain,
the camera, the encoding, the radio link, the display and the human, contributes delay, and the aircraft's
dynamics were running at nearly twice full-scale speed while it did.

The cluster on unmanned aircraft, ground stations and remote piloting and the cluster on time delay, latency and delay compensation hold the research on this arrangement.

## The Flight Test Record

### Flights and Hours

| Item | Value |
|---|---|
| First flight | 17 May 1997 |
| Final flight of the first programme | 12 November 1997 |
| Research flights | 31 |
| Flight time | 15 hours 38 minutes, which is 938 minutes |
| Mean sortie | 30.26 minutes |
| Campaign length | 25 weeks |

**Thirty-one flights in twenty-five weeks is one flight every 5.6 days**, which for a research aeroplane
with no pilot aboard and a mean sortie of half an hour is a brisk rate and not a leisurely one.

**The fuel load and the mean sortie together imply a fuel flow, useful as a check on the engine class but not as a datum.**
A mean sortie of 1,815 seconds burning 180 pounds gives

$$\dot{w}_f = \frac{180}{1815/3600} = 356.9 \ \text{lb/h} \qquad \Rightarrow \qquad \frac{\dot{w}_f}{T} = 0.510$$

**A mean thrust specific fuel consumption of 0.510 pounds per pound force per hour, referred to maximum thrust, sits below the 0.683 of the [Williams F107][ref_f112] from which the F112 was developed**,
as it should, because the engine did not run at maximum thrust for a whole sortie. **It is a weak check and it passes**,
and the result is reported here as weak without dressing it up. The mean sortie sits below the 35 to 45 minutes the
programme account gives for a typical research flight, so the mean includes shorter flights and the full fuel load
was not burned on every one. Taking a typical 40 minute flight on the same 180 pounds instead gives

$$\dot{w}_f = \frac{180}{40/60} = 270 \ \text{lb/h} \qquad \Rightarrow \qquad \frac{\dot{w}_f}{T} = 0.386$$

which is lower again, so the check gives a lower bound on the consumption rather than measuring it.

Research on the X-36 and its two closest relatives is collected in the cluster on the X-36, X-29 and X-31 demonstrators.

### The Often Omitted Second Programme

The aircraft flew twice more in [December 1998][ref_nasa_x36], carrying the Air Force Research Laboratory's
**Reconfigurable Control for Tailless Fighter Aircraft** software, a neural-network scheme intended to adapt
the control law in flight to damage or to an effector failure.

**That was a different experiment from the first, and the more ambitious of the two.** The 1997
campaign asked whether a fixed control law could fly a tailless aircraft. The 1998 flights asked whether a
control law could work out for itself how to fly one whose effectors had changed underneath it.

For the later work on reconfigurable control, see the cluster on adaptive, neural and reconfigurable flight control, and for the aircraft itself the cluster on the X-36, X-29 and X-31 demonstrators.

## Comparison With Ground Prediction

### What the Model Could Check and What It Could Not

**This section sorts the questions by the dimensionless group that governs each.**

| Question | Governed by | Could the model answer it? |
|---|---|---|
| Does the control law stabilise the divergence? | Froude, matched | **Yes**, and this is the experiment |
| Are the handling qualities acceptable? | Froude, matched | **Yes**, with the latency caveat |
| Does control allocation work with redundant effectors? | Froude, matched | **Yes** |
| Where does the flow separate at high angle of attack? | Reynolds, wrong by 6.749 | **Partly, and cautiously** |
| When does a leading-edge vortex burst? | Reynolds, wrong by 6.749 | **Partly** |
| What happens transonically? | Mach, wrong by 1.8898 | **No** |
| What is the radar cross section? | Neither, wavelength governs | **No** |

**The middle rows are the honest difficulty and they deserve more than a shrug.** The Reynolds penalty is a
factor of 6.749, which sounds fatal until both numbers are computed. The Reynolds number needs the
viscosity, which here comes from Sutherland's law,

$$\mu = \mu_0 \left(\frac{T}{T_0}\right)^{3/2} \frac{T_0 + 110.4}{T + 110.4} = 1.7894 \times 10^{-5} \ \text{Pa s}$$

$$\mathrm{Re} = \frac{\rho V \bar{c}}{\mu} = \frac{1.225 \times 125.0 \times 1.029}{1.7894 \times 10^{-5}} = 8.81 \times 10^{6}$$

so the model runs at **8.81 million** on the mean chord at maximum speed and **3.988 million** on approach,
while the full-scale aircraft at the corresponding condition would run at

$$\mathrm{Re}_f = \frac{\mathrm{Re}_m}{\lambda^{3/2}} = \frac{8.81 \times 10^{6}}{0.1482} = 59.46 \times 10^{6}$$

**Both of those are deep in the fully turbulent regime.** The penalty does not move the model into a
different flow regime for attached flow, and that counts as a genuine and slightly surprising mitigation.
**It does still matter where it matters most**, because separation onset and vortex burst position are
Reynolds sensitive well beyond transition, and those are the phenomena a high angle of attack
experiment is about.
**So the correct statement is neither that the penalty is fatal nor that it is negligible, but that it is confined to the questions the article has just listed.**

The Mach number tells the same story more simply. The model's maximum speed limit is about **Mach 0.367**
at sea level. Nothing compressible happens there, and nothing compressible could be learned.

The Contemporary Literature collects the work on this check mainly in two clusters, one on Reynolds number effects and low Reynolds number aerodynamics and one on the viscosity of air and Sutherland's law.

### Turn Rate as a Second Witness

**The published load factor limit is enough to compute the aircraft's turn performance, and doing so produces the scaling result a second time from an entirely different quantity.**
A level turn at load factor $n$ has

$$\dot\psi = \frac{g\sqrt{n^{2} - 1}}{V} \qquad R = \frac{V^{2}}{g\sqrt{n^{2} - 1}}$$

| Speed | Turn rate | Radius | Rate expressed at full scale |
|---|---|---|---|
| 110 kt | 48.64 deg/s | 67 m | 25.74 deg/s |
| 160 kt | 33.44 deg/s | 141 m | 17.70 deg/s |
| 243 kt | 22.02 deg/s | 325 m | 11.65 deg/s |

**The last column is the point.** Turn rate goes as one over speed, speed scales as the square root of the
scale factor, so **turn rate scales as one over that square root, which is 1.8898 again.** The model turns
visibly faster than the aeroplane it represents, in exactly the ratio that its divergences develop faster
and its delay budget shrinks.
**Three different quantities, one factor, and the article did not have to assume it for any of them.**

The corner speed, where the load factor limit meets the lift limit, follows from the same figures,

$$V^{*} = \sqrt{\frac{2 n W}{\rho S C_{L\max}}} = 210.8 \ \text{kt}$$

**which sits below the 243 knot maximum**, so the aircraft could reach the most demanding point of its
manoeuvre envelope.

Turn performance is surveyed in the cluster on turn performance, agility and manoeuvre.

### The Envelope That Was Opened Rather Than Reached

The [published specification][ref_x36] records the maximum speed limit moving from 160 knots to 243 during
the programme, which is the ordinary signature of envelope expansion. **The conditions actually reached were
lower in speed and high in angle of attack.** The [programme account][ref_nasa_x36] gives a speed envelope
reaching 206 knots, an altitude of 20,200 feet and a maximum angle of attack of 40 degrees, and the
[inventory of American X-vehicles][ref_american_x_vehicles] records 360 degree rolls at angles of attack up
to 15 degrees and rapid turning and rolling manoeuvres at up to 35 degrees.
**The two accounts disagree on the size of the programme.** The inventory lists 25 flights ending on 24
September 1997, a fastest flight of 204 miles per hour and a highest flight of 20,500 feet, while the
programme account gives 31 flights ending on 12 November 1997 with a flight-time total, and this article
follows the programme account as the more detailed of the two.
**What the published record gives at those angles of attack is thin.** [Walker 1997][research_walkerlaurencea_1997] reports Level 1
handling qualities for the phase that opened the envelope to 35 degrees and a normalised roll-time plot
reaching a little above 30 degrees, but no time history is public, and since that is what the
tailless argument turns on, the article notes the gap rather than filling it.

## What the Data Changed

### What the Programme Settled

**It established that a tailless configuration of this class [can be flown][ref_nasa_x36], and it did so under a handicap.**
The control law held an aeroplane whose divergence doubled in well under a second, through a command and
video path with a delay whose effective size was nearly twice what the same delay would have been on a
full-scale aircraft.

**It established that the effector set works**, meaning that split ailerons and a vectoring nozzle between
them can replace a fin across the flight conditions tested, and [Walker 1997][research_walkerlaurencea_1997] reports agility
demonstrations flown with thrust vectoring both on and off.

**And the 1998 flights established that a neural-network reconfigurable control law can compensate in flight for a failed effector**,
which at the time was a much less comfortable proposition than it now sounds, and the
[programme account][ref_nasa_x36] reports it compensating for each simulated control-surface failure.

### What It Fed Into

**The configuration did not become an aeroplane and the control ideas did.** No [X-36 derivative][ref_x36] was built.
[Tailless][ref_tailless] flying-wing planforms did reach production in the unmanned world, as in the
[RQ-170 Sentinel][ref_rq170], and control
allocation among redundant effectors, which this aircraft needed because it had no rudder, became a general
subject in flight control instead of a speciality.

### What It Failed to Influence

**No manned tailless fighter followed it into service**, although crewed tailless prototypes such as the
[Chengdu J-36][ref_j36] were flying by the end of 2024. The X-36 did not fail. The
question it answered was not the binding one. A production fighter's tail is a compromise among signature,
control, weight and the cost of certifying an aircraft that cannot be flown without its computers.
**The X-36 addressed exactly one of those four.**

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Adaptive, neural and reconfigurable flight control | 433 |
| Handling qualities, pilot-induced oscillation and the pilot model | 355 |
| Unmanned aircraft, ground stations and remote piloting | 306 |
| Flight test method, instrumentation and system identification | 250 |
| High angle of attack, vortex flow and departure | 227 |
| Tailless aircraft and flying wings | 214 |
| Flight control law design and fly-by-wire systems | 204 |
| Reynolds number effects and low Reynolds number aerodynamics | 202 |
| Similitude, dynamic scaling and subscale flight testing | 155 |
| Wing and configuration aerodynamics | 155 |
| Slender bodies, fuselages and apparent mass | 144 |
| Thrust vectoring, drag rudders and yaw effectors | 140 |
| Directional stability and lateral-directional dynamics | 137 |
| Time delay, latency and delay compensation | 135 |
| Stability margins and robust control | 105 |
| Control allocation and redundant effectors | 90 |
| Flight dynamics, stability derivatives and unstable modes | 83 |
| Turbofan performance, thrust and fuel consumption | 80 |
| Computational aerodynamics, surrogate models and uncertainty | 77 |
| Radar signature and low observability | 66 |
| Turn performance, agility and manoeuvre | 51 |
| Flight simulation and simulators | 29 |
| Mass properties and moments of inertia | 23 |
| The X-36, X-29 and X-31 demonstrators | 21 |
| The viscosity of air and Sutherland's law | 18 |
| Fighter and technology demonstrator programmes | 12 |
| **Total** | **3,712** |

This section surveys the current literature on the subjects the aircraft touched as well as on the aircraft
itself. **This subject is unusual in that its centre of gravity moved instead of growing.** Tailless
fighters remained a research topic. **Subscale dynamically scaled flight testing became a routine method.**
The cluster table above gives the shape of the survey, the review subsections that follow read the
literature against the aircraft, and the clusters themselves close the section.

### The Method Outlived the Aeroplane

**In 1997 a 28 percent remotely piloted research aeroplane was an expensive and unusual thing to build**, at
about 21 million dollars for two aircraft and their flight testing in the [programme account][ref_nasa_x36]. It
is now ordinary. Cheap airframes, cheap autopilots and cheap radio links turned the dynamically scaled
free-flight model from a specialist technique into a routine one, and much of the modern literature applies
the scaling relations set out above. [Sobron et al 2021][research_sobron_lundstrom_2021] review the current
practice of subscale flight testing and its practical difficulties,
[Raju Kulkarni et al 2019][research_rajukulkarni_larocca_2019] estimate how closely a subscale aircraft
reproduces its original, [Wang et al 2020][research_wang_zhang_2020] set out an analytical scaling method and
its scale effects, and [Hakim and Choukri 2023][research_hakim_choukri_2023] and
[Ananda et al 2017][research_ananda_vahora_2017] design small aircraft to Froude similarity from the start.

**The Froude choice is still the right one and for the same reason**, so the modern work inherits the same
Reynolds penalty and the same time compression the X-36 carried.
**What has changed is that the latency is now measured and compensated rather than assumed**, because the
people building these vehicles are also building their links, as in the real-time latency compensation of
[Ostermann et al 2024][research_ostermann_laubner_2024] for the remote control of an unmanned aircraft and
the study of latency in drone control by [Singh 2025][research_singh_2025].

The research records on this subject are gathered below in the cluster on similitude, dynamic scaling and subscale flight testing and the cluster on unmanned aircraft, ground stations and remote piloting.

### The Reynolds Penalty Has a Modern Name and a Large Literature

**The article's Reynolds penalty was a caveat in 1997 and is a field now.** What the period called scale
effects the present calls **low Reynolds number aerodynamics**, and the small unmanned aircraft is now one of
its principal applications, as in [Aditya and Srinivas 2019][research_aditya_srinivas_2019] on low Reynolds
number flyers, [Somashekar and Immanuel Selwyn Raj 2018][research_somashekar_immanuelselwynraj_2018] on an
aerofoil for a micro aerial vehicle and [Feng et al 2017][research_feng_peng_2017] on a solar unmanned
aircraft.

**That literature is directly about the middle rows of this article's comparison table.** Laminar separation
bubbles, transition location and their sensitivity to Reynolds number decide whether a
subscale model's separation onset resembles its original's, and they are reviewed in
[Benny Thompson and Gunasekaran 2021][research_bennythompson_gunasekaran_2021] and modelled in
[Catalano et al 2024][research_catalano_derosa_2024].

**The X-36 sits at the top of that regime rather than inside it.** At 8.81 million on the mean chord it is
far above the millions-and-below range where the low Reynolds literature concentrates, and the placement helps,
**because it means the penalty this article computes is real but the model is not in the difficult part of the curve.**

The cluster below on Reynolds number effects and low Reynolds number aerodynamics contains these records.

### Tailless Control Became an Unmanned Subject

**The configuration this aircraft tested became a subject of unmanned aircraft design.** The tailless and
flying-wing planform recurs throughout the literature on low-observable unmanned combat aircraft, as in
[Sepulveda Palacios and Smith 2019][research_sepulvedapalacios_smith_2019] on the effect of mission
requirements on low-observable configurations, [Cummings et al 2018][research_cummings_liersch_2018] on the
aerodynamics of an unmanned combat aircraft configuration and [Li et al 2017][research_li_yong_2017] on the
distribution of effectors on a flying wing optimised for low observability. **The control problem the X-36
explored is the control problem those vehicles have**, and yaw control without a fin is studied directly in
[Shearwood et al 2020][research_shearwood_nabawy_2020].

Below, the cluster on tailless aircraft and flying wings and the cluster on radar signature and low observability collect the records on this subject.

### Control Allocation Became General

**An aircraft with more effectors than axes was a speciality in 1997 and is now a standard problem.** The
literature moved from ad hoc mixing and daisy chaining to constrained optimisation, set out in
[Enns 1998][research_enns_1998], [Durham 1999][research_durham_1999] and [Bodson 2000][research_bodson_2000],
with the tailless case in [Buffington and Buffington 1997][research_buffington_buffington_1997] and
[Matamoros and de Visser 2018][research_matamoros_devisser_2018]. Multirotor and tilt-rotor vehicles, which
have nothing but redundant effectors, now carry much of the subject, as in
[Vepa 2021][research_vepa_2021].

The records for this subsection are in the cluster on control allocation and redundant effectors.

### The Reynolds Penalty Is Now Quantified

**The contemporary work does something the period could not. It computes what the penalty costs.**
High-fidelity simulation can run the same configuration at different Reynolds numbers and compare, as
[Yamazaki et al 2018][research_yamazaki_yamagishi_2018] do for the indirect Reynolds number effect and
[Wang et al 2021][research_wang_liu_2021] do for a transport aircraft, with the high angle of attack case in
[Rist 1996][research_rist_1996] and a double-delta wing measured in
[Verhaagen 1999][research_verhaagen_1999]. That turns the argument in this article's comparison section
from a caveat into a measurement.

The research records on this subject are gathered below in the cluster on Reynolds number effects and low Reynolds number aerodynamics and the cluster on computational aerodynamics, surrogate models and uncertainty.

### Latency Spread to Every Remote Vehicle

**The delay argument in this article was a niche concern for one aircraft and is now a general one.** Every
remotely operated vehicle has it. The aircraft-side evidence is older, in
[Smith and Sarrafian 1986][research_smith_sarrafian_1986] on time delay and flying qualities and
[King 1993][research_davidwking_1993] on display latency. The teleoperation literature has grown
around it since, with predictive displays in [Brudnak 2016][research_brudnak_2016], explicit delay
compensation in [Abidi et al 2016][research_abidi_yildiz_2016], and the measured effect of communication
latency on operators in [Storms and Tilbury 2015][research_storms_tilbury_2015] and
[Black et al 2024][research_black_andjelic_2024].

Records on latency appear below in the cluster on time delay, latency and delay compensation and the cluster on handling qualities, pilot-induced oscillation and the pilot model.

### Adaptive, neural and reconfigurable flight control

Adaptive, neural, fault-tolerant and reconfigurable flight control, including dynamic inversion and its incremental form, and the reinforcement learning controllers that now extend them.

**433 records.** \[[122 Neural networks applied to optimal flight control 1993][research_122_neural_1993]\] \[[Abouheaf et al 2020][research_abouheaf_gueaieb_2020]\] \[[Accommodation of failures in the F-16 aircraft using adaptive control 1991][research_accommodation_of_1991]\] \[[Acquatella et al 2017][research_acquatellab_vanekeren_2017]\] \[[Adams and Banda 1993][research_adams_banda_1993]\] \[[Adams and Banda 1993][research_adams_banda_1993_b]\] \[[Agarwal et al 2021][research_agarwal_ng_2021]\] \[[Agarwal 1988][research_agarwalak_1988]\] \[[Ahmadi Dastgerdi et al 2022][research_ahmadidastgerdi_asadi_2022]\] \[[Ahmed-Zaid et al 1990][research_ahmedzaid_ioannou_1990]\] \[[Alag and Kaufman 1974][research_alag_kaufman_1974]\] \[[Andrianantara et al 2025][research_andrianantara_ghazi_2025]\] \[[Andropov et al 2017][research_andropov_guirik_2017]\] \[[Annaswamy 2005][research_annaswamy_2005]\] \[[Applications of Fuzzy Logic and Neural Network Technology to Flight Control System Design: an Overview 2004][research_applications_of_2004]\] \[[Atmaca and Van Kampen 2025][research_atmaca_vankampen_2025]\] \[[Atmaca et al 2025][research_atmaca_stroosma_2025]\] \[[Bacon and Ostroff 2000][research_bacon_ostroff_2000]\] \[[Bajodah et al 2018][research_bajodah_mibar_2018]\] \[[Balakrishnan 1972][research_balakrishnan_1972]\] \[[Balas et al 1992][research_balas_garrard_1992]\] \[[Banerjee 2019][research_banerjee_2019]\] \[[Bao et al 2025][research_bao_li_2025]\] \[[Berens and Biezad 1988][research_berens_biezad_1988]\] \[[Berra et al 2017][research_berra_campbell_2017]\] \[[Beyer et al 2018][research_beyer_kuzolap_2018]\] \[[Binz and Moormann 2020][research_binz_moormann_2020]\] \[[Binz et al 2019][research_binz_islam_2019]\] \[[Bodson and Groszkiewicz 1997][research_bodson_groszkiewicz_1997]\] \[[Bodson and Pohlchuck 1996][research_bodson_pohlchuck_1996]\] \[[Bodson and Pohlchuck 1998][research_bodson_pohlchuck_1998]\] \[[Bodson et al 1997][research_bodson_pohlchuck_1997]\] \[[Bodur et al 2025][research_bodur_hancioglu_2025]\] \[[Bomben et al 2006][research_bombencraigr_smolkajamesw_2006]\] \[[Boskovic and Mehra 1999][research_boskovic_mehra_1999]\] \[[Boskovic and Mehra 2000][research_boskovic_mehra_2000]\] \[[Boskovic and Mehra 2001][research_boskovic_mehra_2001]\] \[[Boskovic and Mehra 2002][research_boskovic_mehra_2002]\] \[[Bosworth 2008][research_bosworthjohnt_2008]\] \[[Bosworth 2010][research_bosworthjohnt_2010]\] \[[Bouaiss et al 2023][research_bouaiss_mechgoug_2023]\] \[[Bradshaw and Huber 1982][research_bradshaw_huber_1982]\] \[[Brandin 1990][research_brandin_1990]\] \[[Braun et al 2025][research_braun_holzapfel_2025]\] \[[Brinker and Wise 1996][research_brinker_wise_1996]\] \[[Buffington and Sparks 1998][research_buffington_sparks_1998_b]\] \[[Buffington et al 1998][research_buffington_sparks_1998]\] \[[Bukov 1989][research_bukov_1989]\] \[[Burken et al 1999][research_burken_lu_1999]\] \[[Burken 2005][research_burkenjohnj_2005]\] \[[Burken and Larson 2009][research_burkenjohnj_larsonrichardr_2009]\] \[[Burken et al 2006][research_burkenjohnj_williamshayespeggy_2006]\] \[[Burken et al 2010][research_burkenjohnj_nguyennhant_2010]\] \[[Buschbacher and Bosworth 2006][research_buschbachermark_bosworthjohn_2006]\] \[[Cakiroglu et al 2018][research_cakiroglu_vankampen_2018]\] \[[Calise 2001][research_calise_2001]\] \[[Calise et al 1997][research_calise_rysdyk_1997]\] \[[Calise et al 1998][research_calise_lee_1998]\] \[[Calise et al 2000][research_calise_lee_2000]\] \[[Cao and Lu 2024][research_cao_lu_2024]\] \[[Cao et al 2026][research_cao_chen_2026]\] \[[Caverly et al 2016][research_caverly_girard_2016]\] \[[Chaikalis et al 2020][research_chaikalis_khorrami_2020]\] \[[Chakravarty and Mahanta 2015][research_chakravarty_mahanta_2015]\] \[[Chang et al 2022][research_chang_guo_2022]\] \[[Chao and Yingmin 2015][research_chao_yingmin_2015]\] \[[Chen et al 2017][research_chen_wang_2017]\] \[[Chen et al 2020][research_chen_liu_2020]\] \[[Chen et al 2024][research_chen_tang_2024]\] \[[Cheng et al 2019][research_cheng_cai_2019]\] \[[Cheng et al 2020][research_cheng_zhang_2020]\] \[[Cho and Cho 1995][research_cho_cho_1995]\] \[[Chowdhury and Keshmiri 2024][research_chowdhury_keshmiri_2024]\] \[[Chu et al 2001][research_chu_dacosta_2001]\] \[[Chun-Liang Lin et al 2004][research_chunlianglin_thongshinghwang_2004]\] \[[Clarke and Hwang 2020][research_clarke_hwang_2020]\] \[[Cotting and Burken 2001][research_cotting_burken_2001]\] \[[Crespo et al 2010][research_crespoluisg_matsutanimegumi_2010]\] \[[Cunningham et al 2011][research_cunningham_cox_2011]\] \[[d'Apolito and Sulzbachner 2021][research_dapolito_sulzbachner_2021]\] \[[Dally and Van Kampen 2022][research_dally_vankampen_2022]\] \[[Daskiran et al 2017][research_daskiran_huff_2017]\] \[[Deng et al 2024][research_deng_xu_2024]\] \[[Dethomas and Goel 1982][research_dethomas_goel_1982]\] \[[Di Francesco and Mattei 2016][research_difrancesco_mattei_2016]\] \[[Diget et al 2022][research_diget_hasan_2022]\] \[[Digirolamo 1992][research_digirolamo_1992]\] \[[Dillon and Speyer 1996][research_dillon_speyer_1996]\] \[[Dillon and Speyer 2000][research_dillon_speyer_2000]\] \[[Dong xinmin et al 2003][research_dongxinmin_xiongzhiguo_2003]\] \[[Duggan and Bhandari 2021][research_duggan_bhandari_2021]\] \[[Eberhardt and Ward 1999][research_eberhardt_ward_1999_b]\] \[[Ehlers and Smyth 1968][research_ehlers_smyth_1968]\] \[[Emami et al 2022][research_emami_castaldi_2022]\] \[[Enns and Si 2002][research_enns_si_2002]\] \[[Enns et al 1994][research_enns_bugajski_1994]\] \[[Ermeydan and Kiyak 2017][research_ermeydan_kiyak_2017]\] \[[Eva Wu et al 2000][research_evawu_zhang_2000]\] \[[Fan et al 2026][research_fan_jiang_2026]\] \[[Fault Tolerant Control for Aircraft Flaperon Faults Using Nonlinear Dynamic Inversion 2025][research_fault_tolerant_2025]\] \[[Fei et al 2023][research_fei_li_2023]\] \[[Feng et al 2022][research_feng_wang_2022]\] \[[Fernandes and Cardoso-Ribeiro 2025][research_fernandes_cardosoribeiro_2025]\] \[[Ferrari and Stengel 2004][research_ferrari_stengel_2004]\] \[[Gadient and Weltz 2004][research_gadient_weltz_2004]\] \[[Gaither et al 1989][research_gaithersa_agarwalak_1989]\] \[[Gavra and van Kampen 2024][research_gavra_vankampen_2024]\] \[[Gavra and Van Kampen 2024][research_gavra_vankampen_2024_b]\] \[[Ghiglino et al 2015][research_ghiglino_forshaw_2015]\] \[[Ghorawat et al 2015][research_ghorawat_lee_2015]\] \[[Goman and Kolesnikov 1998][research_goman_kolesnikov_1998]\] \[[Gong et al 2019][research_gong_wang_2019]\] \[[Gou et al 2023][research_gou_liu_2023]\] \[[Gregory 1998][research_gregory_1998]\] \[[Gregory 2001][research_gregory_2001]\] \[[Grondman et al 2018][research_grondman_looye_2018]\] \[[Guan and Shi 2019][research_guan_shi_2019]\] \[[Guo et al 2026][research_guo_liu_2026]\] \[[Guoqiang and Jinkun 2015][research_guoqiang_jinkun_2015]\] \[[Gursoy and Yavrucuk 2015][research_gursoy_yavrucuk_2015]\] \[[Gäßler and Robens 2025][research_gassler_robens_2025]\] \[[Gümüşboğa and İftar 2021][research_gumusboga_iftar_2021]\] \[[Ha 1990][research_ha_1990]\] \[[Hageman et al 2003][research_hageman_smith_2003]\] \[[Hajiyevt and Caliskan 2001][research_hajiyevt_caliskan_2001]\] \[[Hamza and Samir 2020][research_hamza_samir_2020]\] \[[Han and Zhang 2019][research_han_zhang_2019]\] \[[Han et al 2023][research_han_cheng_2023]\] \[[Han et al 2024][research_han_yang_2024]\] \[[Harris et al 2019][research_harris_elliott_2019]\] \[[He et al 2020][research_he_tan_2020]\] \[[He Mingyi et al 1998][research_hemingyi_jianghailin_1998]\] \[[Henkenjohann et al 2023][research_henkenjohann_nolte_2023]\] \[[Henkenjohann et al 2024][research_henkenjohann_nolte_2024]\] \[[Hess and Wells 2002][research_hess_wells_2002]\] \[[Hess and Wells 2003][research_hess_wells_2003]\] \[[Hess and McLean 2000][research_hessronalda_mcleanc_2000]\] \[[Heyer et al 2020][research_heyer_kroezen_2020]\] \[[Ho and Zhou 2023][research_ho_zhou_2023]\] \[[Hofsäβ and Holzapfel 2024][research_hofsa_holzapfel_2024]\] \[[Homola et al 2025][research_homola_li_2025]\] \[[Horowitz 1964][research_horowitz_1964]\] \[[Horowitz 1965][research_horowitz_1965]\] \[[Huang et al 1992][research_huang_tylock_1992]\] \[[Huang et al 1999][research_huang_celi_1999]\] \[[Huzmezan 1998][research_huzmezan_1998]\] \[[Huzmezan and Maciejowski 1999][research_huzmezan_maciejowski_1999]\] \[[Ignatyev 2018][research_ignatyev_2018]\] \[[Imran et al 2021][research_imran_stolkin_2021]\] \[[Inanc et al 2025][research_inanc_habboush_2025]\] \[[Jafari et al 2017][research_jafari_fehr_2017]\] \[[Jayaraman and Ghosh 2021][research_jayaraman_ghosh_2021]\] \[[Jayaraman et al 2021][research_jayaraman_giri_2021]\] \[[Jeong et al 2024][research_jeong_jeong_2024]\] \[[Ji et al 2021][research_ji_kim_2021]\] \[[Ji et al 2022][research_ji_chen_2022]\] \[[Jianmin Wang et al 2016][research_jianminwang_jinbowang_2016]\] \[[Johnson 1986][research_johnson_1986]\] \[[Juliana et al 2004][research_juliana_chu_2004]\] \[[Kamel et al 2015][research_kamel_ghamry_2015]\] \[[Kamel et al 2016][research_kamel_ghamry_2016]\] \[[Kanai et al 1990][research_kanai_nikiforuk_1990]\] \[[Kaneba et al 2022][research_kaneba_mu_2022]\] \[[Kaufman and Berry 1976][research_kaufman_berry_1976]\] \[[Kim 1995][research_kim_1995]\] \[[Kim et al 2003][research_kim_lee_2003]\] \[[Kiyak and Ermeydan 2018][research_kiyak_ermeydan_2018]\] \[[Klein et al 2016][research_klein_kashawlic_2016]\] \[[Ko et al 2019][research_ko_kang_2019]\] \[[Kocurek et al 1997][research_kocurek_durham_1997]\] \[[Konatala et al 2021][research_konatala_vankampen_2021]\] \[[Konatala et al 2024][research_konatala_milz_2024]\] \[[Koopman and Zammit-Mangion 2024][research_koopman_zammitmangion_2024]\] \[[Kumar et al 2018][research_kumar_srivastava_2018]\] \[[Kumtepe et al 2022][research_kumtepe_pollack_2022]\] \[[L'Afflitto et al 2018][research_lafflitto_anderson_2018]\] \[[Lamperski 2022][research_lamperski_2022]\] \[[Lang et al 2024][research_lang_li_2024]\] \[[Larson et al 2009][research_larsonrichardr_burkenjohnj_2009]\] \[[Lee and Kim 2001][research_lee_kim_2001]\] \[[Lee and Van Kampen 2021][research_lee_vankampen_2021]\] \[[Lee et al 2020][research_lee_kim_2020]\] \[[Lee et al 2021][research_lee_benedict_2021]\] \[[Lee et al 2021][research_lee_saj_2021]\] \[[Leonard and Arnett 1980][research_leonardrg_arnettem_1980]\] \[[Li and van Kampen 2024][research_li_vankampen_2024]\] \[[Li and Wang 2017][research_li_wang_2017]\] \[[Li et al 1994][research_li_ge_1994]\] \[[Li et al 2018][research_li_zhang_2018]\] \[[Li et al 2021][research_li_liu_2021]\] \[[Li Yan et al 2000][research_liyan_sundarajan_2000]\] \[[Linear and neural network feedback for flight control decoupling 1996][research_linear_and_1996]\] \[[Littleboy et al 1997][research_littleboy_smith_1997]\] \[[Liu and Jiang 2024][research_liu_jiang_2024]\] \[[Liu and Zhu 2021][research_liu_zhu_2021]\] \[[Liu et al 2016][research_liu_yuan_2016]\] \[[Liu et al 2018][research_liu_sun_2018]\] \[[Liu et al 2019][research_liu_dong_2019]\] \[[Liu et al 2022][research_liu_wang_2022]\] \[[Liu et al 2022][research_liu_zhang_2022]\] \[[Liu et al 2024][research_liu_an_2024]\] \[[Lu et al 2016][research_lu_vankampen_2016]\] \[[Lu et al 2024][research_lu_wu_2024]\] \[[Lubing et al 2017][research_lubing_yang_2017]\] \[[Lungu and Lungu 2016][research_lungu_lungu_2016]\] \[[Luo et al 2019][research_luo_du_2019]\] \[[Luo et al 2022][research_luo_zhang_2022]\] \[[Ly and Ho 1986][research_lyul_hojk_1986]\] \[[Ma and Peng 2021][research_ma_peng_2021]\] \[[Ma et al 2019][research_ma_dong_2019]\] \[[Ma et al 2023][research_ma_hui_2023]\] \[[Ma et al 2025][research_ma_yao_2025]\] \[[Mahulkar 2010][research_mahulkar_2010]\] \[[Mallavalli and Fekih 2018][research_mallavalli_fekih_2018]\] \[[Mallavalli and Fekih 2019][research_mallavalli_fekih_2019]\] \[[Mallery and Neebe 1965][research_mallery_neebe_1965]\] \[[Malloy and Chang 1998][research_malloy_chang_1998]\] \[[Mansur and Lanteigne 2020][research_mansur_lanteigne_2020]\] \[[Matthews and Yi 2019][research_matthews_yi_2019]\] \[[Matthews and Yi 2021][research_matthews_yi_2021]\] \[[Maybeck and Stevens 1990][research_maybeck_stevens_1990]\] \[[Maybeck and Stevens 1991][research_maybeck_stevens_1991]\] \[[Mayhew and Gleason 1988][research_mayhew_gleason_1988]\] \[[McFarland and D'Souza 1994][research_mcfarland_dsouza_1994]\] \[[McLean 1994][research_mclean_1994]\] \[[McLean and Aslam-Mir 1992][research_mclean_aslammir_1992]\] \[[McLean and Aslam-Mir 1994][research_mclean_aslammir_1994]\] \[[McLean and Aslam-Mir 1994][research_mclean_aslammir_1994_b]\] \[[Miller 2011][research_millerchristopherj_2011]\] \[[Miller 2011][research_millerchristopherj_2011_b]\] \[[Model Following Reconfigurable Flight Control System Design Using Direct Adaptive Scheme 2003][research_model_following_2003]\] \[[Moerder et al 1989][research_moerderdanield_halyonesim_1989]\] \[[Mohammadi et al 2025][research_mohammadi_ebrahimi_2025]\] \[[Mokhtar and El-Badawy 2023][research_mokhtar_elbadawy_2023]\] \[[Monaco et al 1997][research_monaco_ward_1997]\] \[[Montgomery and Caglayan 1976][research_montgomery_caglayan_1976]\] \[[Montgomery and Price 1976][research_montgomery_price_1976]\] \[[Morse and Ossman 1989][research_morse_ossman_1989]\] \[[Morse and Ossman 1990][research_morse_ossman_1990]\] \[[Morton et al 1996][research_morton_enns_1996]\] \[[Moses et al 1965][research_moses_pferschjr_1965]\] \[[Mueller et al 2026][research_mueller_theodoulis_2026]\] \[[Mulgund and Stengel 1993][research_mulgund_stengel_1993]\] \[[Mulgund and Stengel 1995][research_mulgund_stengel_1995]\] \[[Nadell et al 2023][research_nadell_berger_2023]\] \[[Napolitano et al 1997][research_napolitano_casanova_1997]\] \[[Napolitano et al 2001][research_napolitano_song_2001]\] \[[Niewoehner and Carter 2001][research_niewoehnerkevinr_carterjohn_2001]\] \[[Nihtilä 1989][research_nihtila_1989]\] \[[Nikiforuk and Gupta 1977][research_nikiforuk_gupta_1977]\] \[[Nikiforuk et al 1979][research_nikiforuk_ohta_1979]\] \[[Nivison and Khargonekar 2017][research_nivison_khargonekar_2017]\] \[[Nivison and Khargonekar 2017][research_nivison_khargonekar_2017_b]\] \[[Nivison and Khargonekar 2018][research_nivison_khargonekar_2018]\] \[[Nonlinear adaptive flight control using neural networks 1998][research_nonlinear_adaptive_1998]\] \[[Nonlinear Discrete-Time Reconfigurable Flight Control Systems Using Neural Networks 2004][research_nonlinear_discrete_time_2004]\] \[[Oktay and Kose 2021][research_oktay_kose_2021]\] \[[Oliva 2001][research_oliva_2001]\] \[[Oppenheimer and Doman 2004][research_oppenheimer_doman_2004]\] \[[Optimum neural network control 1993][research_optimum_neural_1993]\] \[[Orozco et al 2026][research_orozco_walsh_2026]\] \[[Ortiz-Torres et al 2018][research_ortiztorres_castillo_2018]\] \[[Ostroff and Bacon 2002][research_ostroff_bacon_2002]\] \[[Ouyang and Lin 2017][research_ouyang_lin_2017]\] \[[Ouyang et al 2022][research_ouyang_zhou_2022]\] \[[Padhi and Balakrishnan 2003][research_padhi_balakrishnan_2003]\] \[[Palkin and Zenchenko 2025][research_palkin_zenchenko_2025]\] \[[Pan et al 2016][research_pan_liu_2016]\] \[[Pan et al 2017][research_pan_sun_2017]\] \[[Panish et al 2023][research_panish_nicholls_2023]\] \[[Papageorgiou and Glover 2002][research_papageorgiou_glover_2002]\] \[[Park et al 2024][research_park_ramirezserrano_2024]\] \[[Park et al 2025][research_park_ramirezserrano_2025]\] \[[Park et al 2025][research_park_ramirezserrano_2025_b]\] \[[Patel and Smith 1998][research_patel_smith_1998]\] \[[Pfeifle and Fichter 2022][research_pfeifle_fichter_2022]\] \[[PI control of a tailless fighter aircraft with dynamic inversion and neural networks 1999][research_pi_control_1999]\] \[[Pollack et al 2026][research_pollack_theodoulis_2026]\] \[[Qian et al 2022][research_qian_yang_2022]\] \[[Qian et al 2024][research_qian_ma_2024]\] \[[Ransquin and Chatelain 2021][research_ransquin_chatelain_2021]\] \[[Reconfigurable Flight Control Law Using Adaptive Neural Networks and Backstepping Technique 2003][research_reconfigurable_flight_2003]\] \[[Reiner et al 1994][research_reiner_balas_1994]\] \[[Reiner et al 1995][research_reiner_balas_1995]\] \[[Reiner et al 1996][research_reiner_balas_1996]\] \[[Ren and Wang 2026][research_ren_wang_2026]\] \[[Richter et al 2024][research_richter_calix_2024]\] \[[Ronfle-Nadaud 2009][research_ronflenadaud_2009]\] \[[Rubertus 1983][research_rubertusdp_1983]\] \[[Rysdyk and Calise 1998][research_rysdyk_calise_1998]\] \[[Rysdyk and Calise 1999][research_rysdyk_calise_1999]\] \[[Sabra et al 2025][research_sabra_hafez_2025]\] \[[Sadeghi 1984][research_sadeghi_1984]\] \[[Safwat et al 2018][research_safwat_zhang_2018]\] \[[Saini et al 2024][research_saini_kumar_2024]\] \[[Salahudden et al 2024][research_salahudden_agrawal_2024]\] \[[Sancı and Öke Günel 2024][research_sanci_okegunel_2024]\] \[[Saraf et al 1998][research_saraf_deodhare_1998]\] \[[Sayyed et al 2025][research_sayyed_konar_2025]\] \[[Schaff and Prazenica 2025][research_schaff_prazenica_2025]\] \[[Schierman et al 2015][research_schierman_devore_2015]\] \[[Schnetter et al 2015][research_schnetter_kaste_2015]\] \[[Schuck 1959][research_schuck_1959]\] \[[Schuck 1960][research_schuck_1960]\] \[[Schumacher 1999][research_schumacher_1999]\] \[[Semmelhack and Hoppe 1967][research_semmelhack_hoppe_1967]\] \[[Seo and Kim 2019][research_seo_kim_2019]\] \[[Seres et al 2023][research_seres_liu_2023]\] \[[Sever et al 2025][research_sever_demir_2025]\] \[[Shankar et al 2004][research_shankar_yedavalli_2004]\] \[[Shao et al 2019][research_shao_chen_2019]\] \[[Shen and Xu 2021][research_shen_xu_2021]\] \[[Shen et al 2023][research_shen_wang_2023]\] \[[Shin and Kim 2004][research_shin_kim_2004]\] \[[Shin et al 2003][research_shin_johnson_2003]\] \[[Shore and Bodson 2004][research_shore_bodson_2004]\] \[[Shtessel et al 1999][research_shtessel_buffington_1999_b]\] \[[Shukla et al 2025][research_shukla_benyamen_2025]\] \[[Singh and Steinberg 1996][research_singh_steinberg_1996]\] \[[Singh et al 1999][research_singh_steinberg_1999]\] \[[Siwakosit and Hess 2001][research_siwakosit_hess_2001]\] \[[Siwakosit et al 2000][research_siwakosit_snell_2000]\] \[[Smit and Craig 1998][research_smit_craig_1998]\] \[[Smit et al 2022][research_smit_pollack_2022]\] \[[Smith 1994][research_smith_1994]\] \[[Smith 1998][research_smith_1998]\] \[[Smith and Berry 2000][research_smith_berry_2000]\] \[[Smith and Patel 1995][research_smith_patel_1995]\] \[[Smith et al 1998][research_smith_ward_1998]\] \[[Snell 1992][research_snell_1992]\] \[[Snell and Stout 1994][research_snell_stout_1994]\] \[[Snell and Stout 1998][research_snell_stout_1998]\] \[[Snell et al 1998][research_snell_hess_1998]\] \[[Soloway and Haley 2000][research_soloway_haley_2000]\] \[[Song 2008][research_song_2008]\] \[[Song and Huang 2026][research_song_huang_2026]\] \[[Stable multiple model adaptive flight control for accommodation of a large class of control effector failures 1999][research_stable_multiple_1999]\] \[[Stein et al 1975][research_stein_hartmann_1975]\] \[[Stein et al 1977][research_stein_hartmann_1977]\] \[[Steinberg 1999][research_steinberg_1999]\] \[[Steinberg 2001][research_steinberg_2001]\] \[[Steinberg and DiGirolamo 1991][research_steinberg_digirolamo_1991]\] \[[Steinberg and Page 1998][research_steinberg_page_1998]\] \[[Steinberg and Page 1999][research_steinberg_page_1999]\] \[[Steinleitner et al 2022][research_steinleitner_frenzel_2022]\] \[[Stewart and Shuck 1990][research_stewartjamesf_shuckthomasl_1990]\] \[[Stolarik 2007][research_stolarik_2007]\] \[[Stougie et al 2024][research_stougie_pollack_2024]\] \[[Sun and van Kampen 2021][research_sun_vankampen_2021]\] \[[Sun et al 2020][research_sun_wang_2020]\] \[[Taherinezhad and Ramirez-Serrano 2023][research_taherinezhad_ramirezserrano_2023]\] \[[Tamaskani et al 2026][research_tamaskani_alfi_2026]\] \[[Tang and Lai 2020][research_tang_lai_2020]\] \[[Tang et al 2024][research_tang_zhao_2024]\] \[[Tantrairatn and Veres 2015][research_tantrairatn_veres_2015]\] \[[Terrell and Zein-Sabatto 2017][research_terrell_zeinsabatto_2017]\] \[[Tian and Zhou 2021][research_tian_zhou_2021]\] \[[Toloei and Ghaderi 2026][research_toloei_ghaderi_2026]\] \[[Torres et al 2022][research_torres_xu_2022]\] \[[Totah and Totah 1997][research_totah_totah_1997]\] \[[Tranchero and Latorre 2001][research_tranchero_latorre_2001]\] \[[Unal 2021][research_unal_2021]\] \[[Urnes et al 2001][research_urnes_davidson_2001]\] \[[Urnes et al 1990][research_urnesjamesm_stewartjames_1990]\] \[[Urnes et al 1993][research_urnesjamesm_hoystephene_1993]\] \[[van Overeem et al 2023][research_vanovereem_wang_2023]\] \[[Vankadari et al 2018][research_vankadari_das_2018]\] \[[Vieira dos Santos and Van Kampen 2025][research_vieiradossantos_vankampen_2025]\] \[[Wang and Wang 2020][research_wang_wang_2020]\] \[[Wang and Zhang 2021][research_wang_zhang_2021]\] \[[Wang et al 2016][research_wang_wang_2016]\] \[[Wang et al 2016][research_wang_zhang_2016]\] \[[Wang et al 2017][research_wang_mu_2017]\] \[[Wang et al 2018][research_wang_li_2018]\] \[[Wang et al 2018][research_wang_vankampen_2018]\] \[[Wang et al 2018][research_wang_vankampen_2018_b]\] \[[Wang et al 2018][research_wang_xiang_2018]\] \[[Wang et al 2019][research_wang_vankampen_2019]\] \[[Wang et al 2020][research_wang_xu_2020]\] \[[Wang et al 2026][research_wang_yi_2026]\] \[[Ward et al 1998][research_ward_monaco_1998]\] \[[Weinstein et al 1986][research_weinstein_posingies_1986]\] \[[Wells 2002][research_wellsscottr_2002]\] \[[Wen and Tian 2020][research_wen_tian_2020]\] \[[Werbos 2001][research_werbos_2001]\] \[[Williams 2004][research_williams_2004]\] \[[Wilson and Riccardi 2022][research_wilson_riccardi_2022]\] \[[Wise 1992][research_wise_1992]\] \[[Wise and Sedwick 1998][research_wise_sedwick_1998]\] \[[Wu and Zhu 2024][research_wu_zhu_2024]\] \[[Xia and Zhang 2019][research_xia_zhang_2019]\] \[[Xiao et al 2018][research_xiao_zhang_2018]\] \[[Xiao et al 2025][research_xiao_fan_2025]\] \[[Xie et al 2022][research_xie_cabecinhas_2022]\] \[[Xu et al 2017][research_xu_jiang_2017]\] \[[Xu et al 2024][research_xu_tian_2024]\] \[[Yan et al 2019][research_yan_li_2019]\] \[[Yan et al 2025][research_yan_sun_2025]\] \[[Yang and Xiong 2023][research_yang_xiong_2023]\] \[[Yang et al 2023][research_yang_tan_2023]\] \[[Yang et al 2026][research_yang_wang_2026]\] \[[Yoo et al 2021][research_yoo_jang_2021]\] \[[Yu and Wang 2024][research_yu_wang_2024]\] \[[Yu et al 2017][research_yu_fu_2017]\] \[[Yu et al 2017][research_yu_zhang_2017]\] \[[Yu et al 2019][research_yu_xiaoxiong_2019]\] \[[Yu et al 2019][research_yu_zhang_2019]\] \[[Yu et al 2024][research_yu_bi_2024]\] \[[Yuan and Zhou 2024][research_yuan_zhou_2024]\] \[[Yuksek and Inalhan 2020][research_yuksek_inalhan_2020]\] \[[Zha and Li 2025][research_zha_li_2025]\] \[[Zhang 2026][research_zhang_2026]\] \[[Zhang and Ran 2023][research_zhang_ran_2023]\] \[[Zhang et al 2016][research_zhang_pang_2016]\] \[[Zhang et al 2017][research_zhang_devisser_2017]\] \[[Zhang et al 2018][research_zhang_chen_2018]\] \[[Zhang et al 2019][research_zhang_wang_2019]\] \[[Zhang et al 2020][research_zhang_han_2020]\] \[[Zhang et al 2021][research_zhang_du_2021]\] \[[Zhang et al 2023][research_zhang_chen_2023]\] \[[Zhang et al 2023][research_zhang_zhang_2023]\] \[[Zhang et al 2026][research_zhang_wang_2026_b]\] \[[Zhao and Zhu 2016][research_zhao_zhu_2016]\] \[[Zhao et al 2024][research_zhao_xu_2024]\] \[[Zhen and Hao 2020][research_zhen_hao_2020]\] \[[Zheng and Horn 2015][research_zheng_horn_2015]\] \[[Zheng and Li 2019][research_zheng_li_2019]\] \[[Zhou et al 2019][research_zhou_liu_2019]\] \[[Zhou et al 2021][research_zhou_ho_2021]\] \[[Zhou et al 2022][research_zhou_yang_2022]\] \[[Zou et al 2026][research_zou_xie_2026]\] \[[Zuhri 2025][research_zuhri_2025]\] \[[Żugaj 2017][research_zugaj_2017]\]

### Handling qualities, pilot-induced oscillation and the pilot model

Handling and flying qualities criteria, pilot-induced oscillation and the models of the human pilot, for fixed-wing aircraft, rotorcraft and unmanned aircraft.

**355 records.** \[[Abdel-Malek and Marmarelis 1988][research_abdelmalek_marmarelis_1988]\] \[[Abdulrahim et al 2019][research_abdulrahim_bates_2019]\] \[[Abu-Elola et al 2024][research_abuelola_alqaisia_2024]\] \[[Adams 1972][research_adams_1972]\] \[[Adams and Hatch 1971][research_adams_hatch_1971]\] \[[Adams and Hatch 1970][research_adams_hatchjr_1970]\] \[[Air Force Test Pilot School Edwards Afb Ca 1969][research_airforcetestpilotschooledwardsafbca_1969]\] \[[Air Force Test Pilot School Edwards Afb Ca 1981][research_airforcetestpilotschooledwardsafbca_1981]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_d]\] \[[Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991_c]\] \[[Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]\] \[[Alexander 2025][research_alexander_2025]\] \[[Alstrom and Paul 2023][research_alstrom_paul_2023]\] \[[Anderson 1970][research_anderson_1970]\] \[[Antonakis 2025][research_antonakis_2025]\] \[[Ashkenas 1965][research_ashkenas_1965]\] \[[Ashkenas 1965][research_ashkenas_1965_b]\] \[[Ashkenas 1965][research_ashkenas_1965_c]\] \[[Ashkenas 1982][research_ashkenas_1982]\] \[[Ashkenas 1984][research_ashkenas_1984]\] \[[Bachelder and Aponso 2020][research_bachelder_aponso_2020]\] \[[Bachelder and Aponso 2020][research_bachelder_aponso_2020_b]\] \[[Bachelder and Aponso 2023][research_bachelder_aponso_2023]\] \[[Bachelder et al 2023][research_bachelder_aponso_2023_b]\] \[[Bahr et al 2020][research_bahr_gandhi_2020]\] \[[Bailes et al 1975][research_bailes_mittag_1975]\] \[[Bar-Gill and Stengel 1986][research_bargill_stengel_1986]\] \[[Barbini et al 1970][research_barbini_balfe_1970]\] \[[Barnes 1971][research_barnes_1971]\] \[[Baughman and Longeauay 2015][research_baughman_longeauay_2015]\] \[[Bechelder et al 2025][research_bechelder_bjorkman_2025]\] \[[Berger et al 2016][research_berger_miller_2016]\] \[[Berger et al 2019][research_berger_horn_2019]\] \[[Berger et al 2025][research_berger_christensen_2025]\] \[[Berry and Powers 1970][research_berry_powers_1970]\] \[[Bidinotto et al 2021][research_bidinotto_moura_2021]\] \[[Biezad and Schmidt 1984][research_biezad_schmidt_1984]\] \[[Biezad and Schmidt 1985][research_biezad_schmidt_1985]\] \[[Bihrle 1969][research_bihrlejr_1969]\] \[[Bischoff 1983][research_bischoff_1983]\] \[[Black and Moorhouse 1979][research_black_moorhouse_1979]\] \[[Boeing Vertol Co Philadelphia Pa 1983][research_boeingvertolcophiladelphiapa_1983]\] \[[Boothe 1971][research_boothe_1971]\] \[[Boothe et al 1974][research_boothe_chen_1974]\] \[[Booz 1988][research_booz_1988]\] \[[Bowes and Miller 1976][research_bowes_miller_1976]\] \[[Brandon et al 1987][research_brandonjaym_brownphilipw_1987]\] \[[Brauser 1982][research_brauser_1982]\] \[[Breneman and Lower 1992][research_breneman_lower_1992]\] \[[Breul 1963][research_breul_1963]\] \[[Brown 1970][research_brownjr_1970]\] \[[Byers et al 1988][research_byers_bittner_1988]\] \[[Callaghan and Kunz 2019][research_callaghan_kunz_2019]\] \[[Callaghan and Kunz 2021][research_callaghan_kunz_2021]\] \[[Cameron et al 2003][research_cameron_thomson_2003]\] \[[Cameron et al 2021][research_cameron_memon_2021]\] \[[Cao and Qi 2018][research_cao_qi_2018]\] \[[Carlson 1958][research_carlson_1958]\] \[[Carlson et al 1965][research_carlson_mabli_1965]\] \[[Cavalcanti et al 2026][research_cavalcanti_uehara_2026]\] \[[Chalk 1964][research_chalk_1964]\] \[[Chalk et al 1969][research_chalk_neal_1969]\] \[[Chance Vought Corp Dallas Tx 1979][research_chancevoughtcorpdallastx_1979]\] \[[Chen and Ji 2017][research_chen_ji_2017]\] \[[Chetty and Lakshmi 1991][research_chetty_lakshmi_1991]\] \[[Chetty and Raol 1992][research_chetty_raol_1992]\] \[[Chevalier and Burke 1972][research_chevalier_burke_1972]\] \[[Chowhan et al 2019][research_chowhan_arya_2019]\] \[[Blanken and Whalley 1993][research_christopherlblanken_matthewswhalley_1993]\] \[[Breuhaus 1979][research_breuhaus_1979]\] \[[Clark 1964][research_clark_1964]\] \[[Clark 1982][research_clark_1982]\] \[[Corliss 1982][research_corliss_1982]\] \[[Cosenza and Vos 2017][research_cosenza_vos_2017]\] \[[Cox and Marshall 2000][research_coxtimothyh_marshallalisa_2000]\] \[[Craig and Heffley 1972][research_craig_heffley_1972]\] \[[Craig and Heffley 1973][research_craig_heffley_1973]\] \[[Crombie and Moorhouse 1980][research_crombie_moorhouse_1980]\] \[[Crother et al 1973][research_crother_gabelman_1973]\] \[[Curry et al 1965][research_curry_matthews_1965]\] \[[Curry and Batterson 2000][research_currytimothyj_battersonjamesg_2000]\] \[[Daughaday and Duwaldt 1955][research_daughaday_duwaldt_1955]\] \[[Difranco 1969][research_difranco_1969]\] \[[Difranco 1970][research_difranco_1970]\] \[[DiFranco 1971][research_difranco_1971]\] \[[Doko and Sasongko 2026][research_doko_sasongko_2026]\] \[[Doman 1995][research_doman_1995]\] \[[Dotson et al 2020][research_dotson_lee_2020]\] \[[Drewiacki et al 2016][research_drewiacki_silvestre_2016]\] \[[Drewiacki et al 2025][research_drewiacki_moreira_2025]\] \[[Dussart et al 2018][research_dussart_yusuf_2018]\] \[[Edwards et al 1997][research_edwards_fittante_1997]\] \[[Efremov et al 1998][research_efremov_ogloblin_1998]\] \[[Efremov et al 2019][research_efremov_efremov_2019]\] \[[Efremov et al 2019][research_efremov_tiaglik_2019]\] \[[Efremov et al 2020][research_efremov_efremov_2020]\] \[[Efremov et al 2022][research_efremov_shcherbakov_2022]\] \[[Efremov et al 2023][research_efremov_efremov_2023]\] \[[Eichler 1970][research_eichler_1970]\] \[[Ellis 1972][research_ellis_1972]\] \[[Ema et al 1997][research_ema_mizukura_1997]\] \[[Eney 1967][research_eney_1967]\] \[[Eney 1968][research_eney_1968]\] \[[Feather and Joshi 1981][research_featherjb_joshids_1981]\] \[[Fegely et al 2017][research_fegely_carl_2017]\] \[[Fegely et al 2017][research_fegely_xin_2017]\] \[[Fell et al 2015][research_fell_owen_2015]\] \[[Ferguson et al 2017][research_ferguson_thomson_2017]\] \[[Fielding and Southworth 2001][research_fielding_southworth_2001]\] \[[Ford 1989][research_ford_1989]\] \[[Franklin 1970][research_franklin_1970]\] \[[Franklin 1971][research_franklin_1971]\] \[[Franklin and Miller 1967][research_franklin_miller_1967]\] \[[Gallagher 1971][research_gallagher_1971]\] \[[Garkushenko and Vinogradov 2016][research_garkushenko_vinogradov_2016]\] \[[Gerken 1979][research_gerken_1979]\] \[[Gerosa et al 2018][research_gerosa_zanoni_2018]\] \[[Gertsen and Shomber 1965][research_gertsen_shomber_1965]\] \[[Gibson 1990][research_gibson_1990]\] \[[Gilbreath and Markofski 2001][research_gilbreath_markofski_2001]\] \[[Glenn 1988][research_glenn_1988]\] \[[Goetzendorf-Grabowski and Antoniewski 2016][research_goetzendorfgrabowski_antoniewski_2016]\] \[[Goldstein 1982][research_goldstein_1982]\] \[[Granata et al 2026][research_granata_mancini_2026]\] \[[Grant et al 2015][research_grant_stol_2015]\] \[[Grantham et al 1976][research_granthamwd_nguyenlt_1976]\] \[[Gray 1964][research_grayjr_1964]\] \[[Green 1988][research_green_1988]\] \[[Greene and Kunz 2015][research_greene_kunz_2015]\] \[[Griffin and Bellaire 1968][research_griffin_bellaire_1968]\] \[[Guo 2021][research_guo_2021_b]\] \[[Haffley 1982][research_haffley_1982]\] \[[Hall 1971][research_hall_1971]\] \[[Hall et al 1974][research_hall_weingarten_1974]\] \[[Hamidani and Kunz 2018][research_hamidani_kunz_2018]\] \[[Hanson 2012][research_hansoncurtise_2012]\] \[[Harper and Cooper 1986][research_harper_cooper_1986]\] \[[Harper and Robert P. 1955][research_harper_robertp_1955]\] \[[Harper and Sardanowsky 1969][research_harper_sardanowsky_1969]\] \[[Harper and Cooper 1984][research_harperjr_cooper_1984]\] \[[Harris 2000][research_harris_2000]\] \[[Harris et al 2000][research_harris_gautrey_2000]\] \[[Hebbar and Pashilkar 2016][research_hebbar_pashilkar_2016]\] \[[Herrington et al 2023][research_herrington_zahed_2023]\] \[[Hess 1980][research_hess_1980]\] \[[Hess 1981][research_hess_1981]\] \[[Hess 1984][research_hess_1984]\] \[[Hess 1987][research_hess_1987]\] \[[Hess 1995][research_hess_1995]\] \[[Hess 1997][research_hess_1997]\] \[[Hess 1998][research_hess_1998]\] \[[Hess 2016][research_hess_2016]\] \[[Hess and Hess 1997][research_hess_hess_1997]\] \[[Hess and Hess 1997][research_hess_hess_1997_b]\] \[[Higgins and Shomber 1964][research_higgins_shomber_1964]\] \[[Higgins and Shomber 1965][research_higgins_shomber_1965]\] \[[Hodgkinson 2003][research_hodgkinson_2003]\] \[[Hodgkinson and Lamanna 1977][research_hodgkinson_lamanna_1977]\] \[[Hodgkinson et al 1990][research_hodgkinson_potsdam_1990]\] \[[Hoh 1982][research_hoh_1982]\] \[[Hoh 1988][research_hoh_1988]\] \[[Hoh and Mitchell 1983][research_hoh_mitchell_1983]\] \[[Horn et al 2017][research_horn_thorsen_2017]\] \[[Hosseini et al 2025][research_hosseini_bridges_2025]\] \[[Howard 1975][research_howard_1975]\] \[[Howard 1976][research_howard_1976]\] \[[Huff 1949][research_huff_ww_1949]\] \[[Humphreys-Jennings et al 2020][research_humphreysjennings_lappas_2020]\] \[[Huntoon et al 1979][research_huntoon_schohan_1979]\] \[[Idan and Merhav 1990][research_idan_merhav_1990]\] \[[Iloputaife and Ma 1987][research_iloputaife_ma_1987]\] \[[Innocenti and Thukral 1991][research_innocenti_thukral_1991]\] \[[Innocenti et al 1998][research_innocenti_petretti_1998]\] \[[Ioannis and Ioannis 2026][research_ioannis_ioannis_2026]\] \[[Ivler and Geyer 2024][research_ivler_geyer_2024]\] \[[Jacobson and Joshi 1977][research_jacobson_joshi_1977]\] \[[Jacobson and Joshi 1978][research_jacobson_joshi_1978]\] \[[Jansen and Van Kampen 2025][research_jansen_vankampen_2025]\] \[[Jewell et al 1979][research_jewell_heffley_1979]\] \[[Jewell 1982][research_jewellwf_1982]\] \[[Ji et al 2022][research_ji_lu_2022]\] \[[jingwei and jiaming 2020][research_jingwei_jiaming_2020]\] \[[Johnston et al 1965][research_johnston_culver_1965]\] \[[Johnston et al 1974][research_johnston_ashkenas_1974]\] \[[Jones and Hunter 1993][research_jones_hunter_1993]\] \[[Joosten et al 2023][research_joosten_stroosma_2023]\] \[[Joshi and Rickard 1981][research_joshi_rickard_1981]\] \[[Junfeng et al 2017][research_junfeng_wuzhou_2017]\] \[[Junfeng et al 2020][research_junfeng_wuzhou_2020]\] \[[Jusko et al 2022][research_jusko_jones_2022]\] \[[Katayanagi 2004][research_katayanagi_2004]\] \[[Kemper and Cotting 2016][research_kemper_cotting_2016]\] \[[Key 1971][research_key_1971]\] \[[Key 1982][research_key_1982]\] \[[Khan 2019][research_khan_2019]\] \[[Kidd and Bull 1963][research_kidd_bull_1963]\] \[[Kim and Kunz 2016][research_kim_kunz_2016]\] \[[Kim and Kunz 2017][research_kim_kunz_2017]\] \[[Kish et al 1996][research_kish_leggett_1996]\] \[[Kish et al 1997][research_kish_mosle_1997]\] \[[Kish et al 1997][research_kish_mosleiii_1997]\] \[[Klein et al 2017][research_klein_krainski_2017]\] \[[Klyde et al 1995][research_klyde_aponso_1995]\] \[[Klyde et al 2001][research_klyde_brenner_2001]\] \[[Klyde et al 2018][research_klyde_schulze_2018]\] \[[Klyde et al 2020][research_klyde_mitchell_2020]\] \[[Klyde et al 2021][research_klyde_lampton_2021]\] \[[Kriechbaum and Stineman 1972][research_kriechbaum_stineman_1972]\] \[[Lampton et al 2024][research_lampton_klyde_2024]\] \[[Lampton et al 2024][research_lampton_klyde_2024_b]\] \[[Lawrence et al 2018][research_lawrence_theodore_2018]\] \[[Lee and Vining 2018][research_lee_vining_2018]\] \[[Lee et al 2003][research_lee_rodchenko_2003]\] \[[Lee et al 2026][research_lee_horn_2026]\] \[[Levi and Nelson 1963][research_levi_nelson_1963]\] \[[Levison 1982][research_levison_1982]\] \[[Li et al 2024][research_li_zhang_2024]\] \[[Loranchet et al 2025][research_loranchet_tiako_2025]\] \[[Luo and Wang 2017][research_luo_wang_2017]\] \[[Luria 2017][research_luria_2017]\] \[[Lusardi 2023][research_lusardi_2023]\] \[[Malaek and Sajjadi Kia 2004][research_malaek_sajjadikia_2004]\] \[[Malcom 1969][research_malcom_1969]\] \[[Malpica and Lusardi 2013][research_malpica_lusardi_2013]\] \[[Malpica et al 2023][research_malpica_suh_2023]\] \[[Mandal and Gu 2016][research_mandal_gu_2016_b]\] \[[Mansor et al 2015][research_mansor_nogoud_2015]\] \[[Markofski and Bailey 1999][research_markofski_bailey_1999]\] \[[Mavris et al 1998][research_mavris_delaurentis_1998]\] \[[McCormick 1969][research_mccormick_1969]\] \[[McGREGOR and Smith 1966][research_mcgregor_smith_1966]\] \[[Menner et al 2025][research_menner_lawless_2025]\] \[[Merhav 1989][research_merhav_1989]\] \[[Meyer 1983][research_meyer_1983]\] \[[Miller 1970][research_miller_1970]\] \[[Miller and Clark 1965][research_miller_clark_1965]\] \[[Miller and Franklin 1968][research_miller_franklin_1968]\] \[[Mitchell and Hoh 1983][research_mitchell_hoh_1983]\] \[[Mitchell and Hoh 1984][research_mitchell_hoh_1984]\] \[[Mitchell et al 2003][research_mitchell_doman_2003]\] \[[Mitchell et al 1992][research_mitchelldavidg_aponsobimall_1992]\] \[[Molloy et al 2026][research_molloy_shekar_2026]\] \[[Mooij and van Gool 1978][research_mooij_vangool_1978]\] \[[Mouritsen 1994][research_mouritsen_1994]\] \[[Mullins et al 1996][research_mullinsjr_tipton_1996]\] \[[Musso et al 2026][research_musso_vo_2026]\] \[[Nagata et al 1973][research_nagata_skinner_1973]\] \[[Nagy and Kirsten 1976][research_nagy_kirsten_1976]\] \[[Nettleton 1965][research_nettleton_1965]\] \[[Newton and Kroo 2023][research_newton_kroo_2023]\] \[[Newton and Kroo 2024][research_newton_kroo_2024]\] \[[Newton and Kroo 2025][research_newton_kroo_2025]\] \[[Nguyen and Cord 1999][research_nguyen_cord_1999]\] \[[Nguyen et al 1997][research_nguyen_cord_1997]\] \[[Nguyen et al 2021][research_nguyen_lowenberg_2021]\] \[[Nguyen et al 2021][research_nguyen_lowenberg_2021_b]\] \[[Niemiec et al 2020][research_niemiec_j_2020]\] \[[Perhinschi 1998][research_perhinschi_1998]\] \[[Perhinschi and Prasad 1995][research_perhinschi_prasad_1995]\] \[[Peristy et al 2020][research_peristy_perez_2020]\] \[[Place et al 1974][research_place_altmann_1974]\] \[[Portapas and Cooke 2020][research_portapas_cooke_2020]\] \[[Portapas et al 2017][research_portapas_yusuf_2017]\] \[[Postlethwaite et al 1999][research_postlethwaite_konstantopoulos_1999]\] \[[Postlethwaite et al 2000][research_postlethwaite_konstantopoulos_2000]\] \[[Pritchard et al 2016][research_pritchard_wallace_2016]\] \[[Raffel et al 2019][research_raffel_wienke_2019]\] \[[Raffel et al 2021][research_raffel_dillmann_2021]\] \[[Raffel et al 2021][research_raffel_wienke_2021]\] \[[Reeder 1958][research_reeder_1958]\] \[[Repperger et al 1997][research_repperger_koivo_1997]\] \[[Rhoads 1967][research_rhoads_1967]\] \[[Riboldi et al 2026][research_riboldi_alessi_2026]\] \[[Riccardi et al 2025][research_riccardi_mamino_2025]\] \[[Rodchenko et al 2002][research_rodchenko_zaichik_2002]\] \[[Rodchenko et al 2003][research_rodchenko_zaichik_2003]\] \[[Rosa et al 1974][research_rosa_sanneman_1974]\] \[[Ruflin and Grantham 1984][research_ruflin_grantham_1984]\] \[[Saetti and Rogers 2020][research_saetti_rogers_2020]\] \[[Saetti and Rogers 2024][research_saetti_rogers_2024]\] \[[Sahasrabudhe and Celi 1997][research_sahasrabudhe_celi_1997]\] \[[Saporito et al 2021][research_saporito_daronch_2021]\] \[[Sarathy and Murthy 1993][research_sarathy_murthy_1993_b]\] \[[Schmidt 1983][research_schmidt_1983]\] \[[Schroeder et al 1998][research_schroeder_chung_1998]\] \[[Schwartz and Shearer 1964][research_schwartz_shearer_1964]\] \[[Schwithal et al 2025][research_schwithal_wallace_2025]\] \[[Shafer et al 1983][research_shafer_smith_1983]\] \[[Shams et al 2023][research_shams_khouli_2023]\] \[[Shomber and Gertsen 1967][research_shomber_gertsen_1967]\] \[[Shubert and Jones 2025][research_shubert_jones_2025]\] \[[Slongo et al 2020][research_slongo_moraes_2020]\] \[[Smith 1977][research_smith_1977_b]\] \[[Smith 2023][research_smith_2023]\] \[[Smith and Geddes 1979][research_smith_geddes_1979]\] \[[Smith and Edwards 1980][research_smithjw_edwardsjw_1980]\] \[[Solies 1995][research_solies_1995]\] \[[Srinathkumar 2015][research_srinathkumar_2015]\] \[[Starke 1983][research_starke_1983]\] \[[Stifel 1979][research_stifel_1979]\] \[[Sudderth et al 1975][research_sudderthrw_bohnjg_1975]\] \[[Sun et al 2020][research_sun_shi_2020]\] \[[Swaim 1978][research_swaim_1978]\] \[[Swaim and Yen 1979][research_swaim_yen_1979]\] \[[Teofilatto 2001][research_teofilatto_2001]\] \[[Teper and Stapleford 1965][research_teper_stapleford_1965]\] \[[Teper and Stapleford 1966][research_teper_stapleford_1966]\] \[[Thorsen and Horn 2017][research_thorsen_horn_2017]\] \[[Tischler and Hoh 1982][research_tischler_hoh_1982]\] \[[Tischler et al 1991][research_tischlermarkb_fletcherjayw_1991]\] \[[Tohidi et al 2018][research_tohidi_yildiz_2018]\] \[[Tomczyk 2001][research_tomczyk_2001]\] \[[Tomczyk 2002][research_tomczyk_2002]\] \[[Tran et al 2017][research_tran_sakamoto_2017]\] \[[Turner et al 2002][research_turner_padfield_2002]\] \[[Umm-e-Aymon et al 2016][research_ummeaymon_shah_2016]\] \[[Uybarreta et al 2025][research_uybarreta_grant_2025]\] \[[Van Dam et al 1980][research_vandam_holmes_1980]\] \[[van Dam et al 1981][research_vandam_holmes_1981]\] \[[van Gool 1982][research_vangool_1982]\] \[[Van Orden 2001][research_vanorden_2001]\] \[[van Overeem et al 2022][research_vanovereem_wang_2022]\] \[[Viavattene and Mooij 2019][research_viavattene_mooij_2019]\] \[[Vinje and Miller 1973][research_vinje_miller_1973]\] \[[Von Hor and Guess 2017][research_vonhor_guess_2017]\] \[[Walter et al 2019][research_walter_ivler_2019]\] \[[Wang et al 2017][research_wang_guo_2017]\] \[[Wang et al 2021][research_wang_yang_2021]\] \[[Wang et al 2023][research_wang_lu_2023]\] \[[Wang et al 2023][research_wang_wang_2023]\] \[[Wang et al 2024][research_wang_guo_2024]\] \[[Wang et al 2025][research_wang_fang_2025]\] \[[Wasicko 1966][research_wasickorj_1966]\] \[[Wei 2020][research_wei_2020]\] \[[Westbrook 1964][research_westbrook_1964]\] \[[Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]\] \[[Wickens and Dixon 2002][research_wickens_dixon_2002]\] \[[Willebeek-LeMair and Rhinehart 2023][research_willebeeklemair_rhinehart_2023]\] \[[Withrow-Maser et al 2021][research_withrowmaser_malpica_2021]\] \[[Witte et al 2003][research_witte_monson_2003]\] \[[Wu 2025][research_wu_2025]\] \[[Wu and Perng 2004][research_wu_perng_2004]\] \[[Xu and Zhang 2024][research_xu_zhang_2024]\] \[[Xu et al 2019][research_xu_tan_2019]\] \[[Yin and Wang 2017][research_yin_wang_2017]\] \[[Yin et al 2019][research_yin_wang_2019]\] \[[Yuan et al 2021][research_yuan_anderson_2021]\] \[[Zanoni et al 2022][research_zanoni_gerosa_2022]\] \[[Zaytseva et al 2021][research_zaytseva_kuznetsov_2021]\] \[[Zeyada et al 1998][research_zeyada_hess_1998]\] \[[Zeyada et al 1999][research_zeyada_hess_1999]\]

### Unmanned aircraft, ground stations and remote piloting

Unmanned aircraft and remotely piloted vehicles as flying machines, their design, flight control, ground control stations, operators and the programmes that flew them.

**306 records.** \[[Abdullahi et al 2026][research_abdullahi_maimako_2026]\] \[[Advanced Control Techniques for Unmanned Aerial Vehicle (UAV) Navigation and Flight Control 2023][research_advanced_control_2023]\] \[[Aghazadeh Ardebili et al 2025][research_aghazadehardebili_martella_2025]\] \[[Al-Mashhadani 2019][research_almashhadani_2019]\] \[[Al-Zubaidi and Stol 2022][research_alzubaidi_stol_2022]\] \[[Alam and Mamun 2021][research_alam_mamun_2021]\] \[[Alexander 1979][research_alexander_1979]\] \[[Alexander 1979][research_alexander_1979_b]\] \[[An Overview On Unmanned Aerial Vehicle 2017][research_an_overview_2017]\] \[[Analysis of the relationship between mass, speed and cost of an unmanned aircraft 2024][research_analysis_of_2024]\] \[[Analytical synthesis of the control laws at short-period longitudinal motion of the unmanned aerial vehicle 2024][research_analytical_synthesis_2024]\] \[[Andre and Morris 1981][research_andre_morris_1981]\] \[[Arif and Sasongko 2021][research_arif_sasongko_2021]\] \[[Army Scientific Advisory Panel Washington Dc 1977][research_armyscientificadvisorypanelwashingtondc_1977]\] \[[Arogeti and Ailon 2023][research_arogeti_ailon_2023]\] \[[Athayde et al 2024][research_athayde_moutinho_2024]\] \[[Azimov and Allen 2017][research_azimov_allen_2017]\] \[[Deepak and Singh 2016][research_bbvl_singh_2016]\] \[[Bachtiar et al 2019][research_bachtiar_ardilla_2019]\] \[[Badole et al 2022][research_badole_choudhary_2022]\] \[[Baldini et al 2019][research_baldini_felicetti_2019]\] \[[Banfield et al 2016][research_banfield_kidd_2016]\] \[[Barela and Jackson 1988][research_barela_jackson_1988]\] \[[Battiston et al 2017][research_battiston_sharf_2017]\] \[[Baxter 2013][research_baxter_2013]\] \[[Bellman and Kier 1974][research_bellmandr_kierda_1974]\] \[[Bernstein 2000][research_bernstein_2000]\] \[[Bhandari et al 2026][research_bhandari_bhandari_2026]\] \[[Bhujel et al 2026][research_bhujel_pang_2026]\] \[[Bianchi et al 2024][research_bianchi_epicoco_2024]\] \[[Bramesfeld and Prinster 2015][research_bramesfeld_prinster_2015]\] \[[Bréda et al 2024][research_breda_andoga_2024]\] \[[Burke 2015][research_burke_2015]\] \[[Burnashev and Zbrutsky 2019][research_burnashev_zbrutsky_2019]\] \[[Cantarelo et al 2016][research_cantarelo_rolland_2016]\] \[[Carr et al 2003][research_carr_lambrecht_2003]\] \[[Carter et al 2024][research_carter_keeter_2024]\] \[[Castillo Zúñiga et al 2020][research_castillozuniga_souza_2020]\] \[[Chamitoff 1994][research_chamitoff_1994]\] \[[Chen 2021][research_chen_2021_b]\] \[[Chen 2024][research_chen_2024]\] \[[Chen et al 2017][research_chen_zhang_2017]\] \[[Cheng and Pei 2020][research_cheng_pei_2020]\] \[[Cheng and Pei 2021][research_cheng_pei_2021]\] \[[Chernenko and Burnashev 2022][research_chernenko_burnashev_2022]\] \[[Chhetri et al 2026][research_chhetri_jetawatthana_2026]\] \[[Chodnicki et al 2018][research_chodnicki_bartnik_2018]\] \[[Choi et al 2023][research_choi_kim_2023]\] \[[Cieślak 2021][research_cieslak_2021]\] \[[Clark 1983][research_clark_1983]\] \[[Coopmans et al 2015][research_coopmans_podhradsky_2015]\] \[[Coopmans et al 2016][research_coopmans_podhradsky_2016]\] \[[Coopmans et al 2022][research_coopmans_slack_2022]\] \[[Corraro et al 2003][research_corraro_delellis_2003]\] \[[Cote 2015][research_cote_2015]\] \[[Dahleh and Tsitsiklis 2002][research_dahleh_tsitsiklis_2002]\] \[[Dantsker et al 2018][research_dantsker_theile_2018_b]\] \[[Dantsker et al 2020][research_dantsker_theile_2020]\] \[[Daryanto et al 2018][research_daryanto_purwono_2018]\] \[[Davoudi and Duraisamy 2019][research_davoudi_duraisamy_2019]\] \[[de Bruin and Jones 2016][research_debruin_jones_2016]\] \[[De Wagter and Meulenbeld 2019][research_dewagter_meulenbeld_2019]\] \[[Deets and Edwards 1974][research_deetsda_edwardsjw_1974]\] \[[Deets and Purifoy 1998][research_deetsdwaina_purifoydana_1998]\] \[[del Arco et al 2015][research_delarco_alejo_2015]\] \[[Deng and Li 2015][research_deng_li_2015]\] \[[Deshpande and Zhang 2021][research_deshpande_zhang_2021]\] \[[Design and Development Autonomous Unmanned Aerial Vehicle Software 2020][research_design_and_2020]\] \[[Design and Fluid Flow Analysis of Unmanned Aerial Vehicle (UAV) 2015][research_design_and_2015]\] \[[Design and Implementation of Hybrid Wing Unmanned Aerial Vehicle (UAV) 2020][research_design_and_2020_b]\] \[[Determination of External Power Factors Acting on an Unmanned Aerial Vehicle in Critical Flight Modes 2019][research_determination_of_2019]\] \[[Dianovský et al 2023][research_dianovsky_pecho_2023]\] \[[Din et al 2023][research_din_mir_2023]\] \[[Diogo and Fernandes 2024][research_diogo_fernandes_2024]\] \[[Do et al 2023][research_do_dang_2023]\] \[[Dodge 2015][research_dodge_2015]\] \[[Dong 2021][research_dong_2021]\] \[[Dou and Duan 2016][research_dou_duan_2016]\] \[[Dunn 1980][research_dunn_1980]\] \[[Edi 2026][research_edi_2026]\] \[[Edwards 1972][research_edwards_1972]\] \[[Edwards and Deets 1975][research_edwardsjw_deetsda_1975]\] \[[Elario et al 1991][research_elario_guillmette_1991]\] \[[Erkol 2017][research_erkol_2017]\] \[[Fang et al 2026][research_fang_cao_2026]\] \[[Finigian et al 2024][research_finigian_kavounas_2024]\] \[[Flight Test Data Analysis of Hybrid Vertical Take-off and Landing Unmanned Aerial Vehicle 2016][research_flight_test_2016]\] \[[Fogel et al 1974][research_fogel_englund_1974]\] \[[Ford 1977][research_ford_1977]\] \[[Franco et al 2019][research_franco_correia_2019]\] \[[Fu et al 2021][research_fu_yu_2021]\] \[[Fukui et al 2020][research_fukui_harada_2020]\] \[[Fukushima and Tsubone 2019][research_fukushima_tsubone_2019]\] \[[Fulkerson et al 1980][research_fulkerson_hershberger_1980]\] \[[Gacy 2011][research_gacy_2011]\] \[[Garbarino et al 2023][research_garbarino_genito_2023]\] \[[Ghofur et al 2020][research_ghofurm_darmawan_2020]\] \[[Glīzde 2017][research_glizde_2017]\] \[[Gold and Walchli 1974][research_gold_walchli_1974]\] \[[Gorin and Gubankov 2025][research_gorin_gubankov_2025]\] \[[Gossett 1981][research_gossett_1981]\] \[[Gu et al 2017][research_gu_lyu_2017]\] \[[Gu et al 2019][research_gu_valavanis_2019]\] \[[Guerrero et al 2015][research_guerrero_martinez_2015]\] \[[Haber and Chung 2016][research_haber_chung_2016]\] \[[Hafez and Kamel 2016][research_hafez_kamel_2016]\] \[[Hajiyev 2016][research_hajiyev_2016]\] \[[Han et al 2019][research_han_hu_2019]\] \[[Hardy and Sturgeon 1979][research_hardy_sturgeon_1979]\] \[[Harmats and Weihs 1999][research_harmats_weihs_1999]\] \[[Hartley and Pulliam 1988][research_hartley_pulliam_1988]\] \[[Hartley et al 1984][research_hartley_cwynar_1984]\] \[[Hartmann et al 2016][research_hartmann_meyer_2016]\] \[[Hartmann et al 2017][research_hartmann_meyer_2017]\] \[[Hegde 2020][research_hegde_2020]\] \[[Herrmann and Schmidt 2018][research_herrmann_schmidt_2018]\] \[[Hossny et al 2020][research_hossny_elbadawy_2020]\] \[[How 2008][research_how_2008]\] \[[Hoyt et al 1980][research_hoyt_kempel_1980]\] \[[Hsiao et al 1997][research_hsiao_ho_1997]\] \[[Hu and Huang 2017][research_hu_huang_2017]\] \[[Hu-Sheng Wu et al 2015][research_hushengwu_weizonglu_2015]\] \[[Huo et al 2021][research_huo_duan_2021]\] \[[Ibraheem 2019][research_ibraheem_2019]\] \[[Identification, Modelling And Lateral Parameters Control Of Unmanned Aerial Vehicle 2015][research_identification_modelling_2015]\] \[[Iglesis et al 2021][research_iglesis_horri_2021]\] \[[Islam et al 2015][research_islam_faraz_2015]\] \[[Ito et al 2016][research_ito_endo_2016]\] \[[Ivler et al 2022][research_ivler_truong_2022]\] \[[Maddalon et al 2021][research_jeffreymmaddalon_kurtaswieringa_2021]\] \[[Jenkins 2008][research_jenkins_2008]\] \[[Jiang and Parimi 2021][research_jiang_parimi_2021]\] \[[Jimenez et al 2016][research_jimenez_faerevaag_2016]\] \[[Johnsen et al 2022][research_johnsen_runnels_2022]\] \[[Johnston et al 1983][research_johnston_myers_1983]\] \[[Jothiraj et al 2019][research_jothiraj_miles_2019]\] \[[Jun 2024][research_jun_2024]\] \[[Kamine and Bendrick 2008][research_kaminetovyhaber_bendrickgregga_2008]\] \[[Kan et al 2023][research_kan_yao_2023]\] \[[Kang et al 2016][research_kang_park_2016]\] \[[Karabetsky 2018][research_karabetsky_2018]\] \[[Khan and Nahon 2015][research_khan_nahon_2015]\] \[[Kharchenko et al 2017][research_kharchenko_kuzmenko_2017]\] \[[Kharchenko et al 2017][research_kharchenko_matiychyk_2017]\] \[[Kikkawa and Uchiyama 2017][research_kikkawa_uchiyama_2017_b]\] \[[Kim and Oh 2017][research_kim_oh_2017]\] \[[Kim et al 2015][research_kim_jung_2015]\] \[[Kimathi and Lantos 2024][research_kimathi_lantos_2024]\] \[[Kochersberger et al 2017][research_kochersberger_ohanian_2017]\] \[[Kopecki 2016][research_kopecki_2016]\] \[[Kotikalpudi et al 2015][research_kotikalpudi_pfifer_2015]\] \[[Krohn 1988][research_krohn_1988]\] \[[Kuchar 2018][research_kuchar_2018]\] \[[Kumar and Kothari 2024][research_kumar_kothari_2024]\] \[[Kumar et al 2024][research_kumar_shankar_2024]\] \[[Kumar et al 2026][research_kumar_mittal_2026]\] \[[Kumari and Raghunath 2016][research_kumari_raghunath_2016]\] \[[Kuwamura and Hara 2017][research_kuwamura_hara_2017]\] \[[Lanteigne and O'Reilly 2020][research_lanteigne_oreilly_2020]\] \[[Larsson et al 2020][research_larsson_sobron_2020]\] \[[Lavretsky and Misovec 2002][research_lavretsky_misovec_2002]\] \[[Lestari et al 2025][research_lestari_ridwan_2025]\] \[[Li 2024][research_li_2024]\] \[[Li et al 2015][research_li_liu_2015]\] \[[Li et al 2016][research_li_guo_2016]\] \[[Li et al 2016][research_li_yu_2016]\] \[[Linehan 1996][research_linehan_1996]\] \[[Liu 2024][research_liu_2024_b]\] \[[Liu and Chen 2016][research_liu_chen_2016]\] \[[Lu 2017][research_lu_2017]\] \[[Lynch 2012][research_lynch_2012]\] \[[Makarenko et al 2017][research_makarenko_makarov_2017]\] \[[Maldonado et al 2017][research_maldonado_sarker_2017]\] \[[Manoilo 2025][research_manoilo_2025]\] \[[Mathur and Atkins 2023][research_mathur_atkins_2023]\] \[[Maughmer and Somers 1987][research_maughmer_somers_1987]\] \[[Maurya et al 2025][research_maurya_patel_2025]\] \[[McDaniel 2017][research_mcdaniel_2017]\] \[[McMinn and Jackson 2002][research_mcminn_jackson_2002]\] \[[Mei et al 2023][research_mei_zhou_2023]\] \[[Merhav and Grunwald 1978][research_merhav_grunwald_1978]\] \[[Metodiev 2022][research_metodiev_2022]\] \[[Metzger 2012][research_metzger_2012]\] \[[Mikami and Uchiyama 2015][research_mikami_uchiyama_2015]\] \[[Mirchandani 2020][research_mirchandani_2020]\] \[[Morris 1981][research_morris_1981]\] \[[Morris 1983][research_morrisjr_1983]\] \[[Mrusek 2021][research_mrusek_2021]\] \[[Multi-Rotors A Revolution In 2015][research_multi_rotors_a_2015]\] \[[Myschik et al 2022][research_myschik_kinast_2022]\] \[[Müller and Moormann 2023][research_muller_moormann_2023]\] \[[Nadda and Swarup 2017][research_nadda_swarup_2017]\] \[[Neitzke 2025][research_neitzke_2025]\] \[[Nelms and Axelson 1974][research_nelms_axelson_1974]\] \[[Nelms and Bailey 1974][research_nelms_bailey_1974]\] \[[Ni et al 2021][research_ni_wu_2021]\] \[[O-THREE A high altitude 1990][research_o_three_a_1990]\] \[[P.S. and J.V. 2021][research_ps_jv_2021]\] \[[P5 et al 2026][research_p5_ramasubramanian1_2026]\] \[[Patterson and Arena 2015][research_patterson_arena_2015]\] \[[Paulson et al 1977][research_paulson_price_1977]\] \[[Pedersini et al 2015][research_pedersini_toscano_2015]\] \[[Pei et al 2025][research_pei_huang_2025]\] \[[Petnga 2018][research_petnga_2018]\] \[[Phelps 1979][research_phelps_1979]\] \[[Platanitis and Shkarayev 2005][research_platanitisgeorge_shkarayevsergey_2005]\] \[[Putra et al 2022][research_putra_mobedbachtiar_2022]\] \[[Krithiga 2024][research_rs_2024]\] \[[Ramirez and Nahon 2021][research_ramirez_nahon_2021]\] \[[Reghunath and Ramaiah 2022][research_reghunath_ramaiah_2022]\] \[[Reichstein et al 2022][research_reichstein_schopferer_2022]\] \[[Rezek 1985][research_rezek_1985]\] \[[Rinauto et al 2017][research_rinauto_gupta_2017]\] \[[Rithirun et al 2021][research_rithirun_charean_2021]\] \[[Rodríguez de Cos and Acosta 2020][research_rodriguezdecos_acosta_2020]\] \[[Rosales and Gross 2017][research_rosales_gross_2017]\] \[[Ross et al 2019][research_ross_jacob_2019]\] \[[Rutkay and Laliberté 2016][research_rutkay_laliberte_2016]\] \[[Sadraey 2017][research_sadraey_2017]\] \[[Safie and Yunus 2024][research_safie_yunus_2024]\] \[[Sanchez-Rivera et al 2019][research_sanchezrivera_lozano_2019]\] \[[Sanchez-Rivera et al 2020][research_sanchezrivera_lozano_2020]\] \[[Sato and Muraoka 2015][research_sato_muraoka_2015]\] \[[Sato et al 2017][research_sato_muraoka_2017]\] \[[Saxena and Faruque 2016][research_saxena_faruque_2016]\] \[[Schalk 2017][research_schalk_2017]\] \[[Schmidt et al 2019][research_schmidt_danowsky_2019]\] \[[Scott 2021][research_scott_2021]\] \[[Seaberg et al 1972][research_seaberg_etter_1972]\] \[[Sedláčková et al 2020][research_sedlackova_kurdel_2020]\] \[[Seiferth et al 2018][research_seiferth_kugler_2018]\] \[[Setiawarman and Sasongko 2026][research_setiawarman_sasongko_2026]\] \[[Sharif 2019][research_sharif_2019]\] \[[Sharif 2022][research_sharif_2022]\] \[[Shen and Chen 2025][research_shen_chen_2025]\] \[[Shenoy and Manjunatha 2023][research_shenoy_manjunatha_2023]\] \[[Shishkin 2025][research_shishkin_2025]\] \[[Sing Kang et al 2024][research_singkang_singh_2024]\] \[[Singhal et al 2019][research_singhal_thorpe_2019]\] \[[Skarka and Mateja 2024][research_skarka_mateja_2024]\] \[[Slaby et al 1985][research_slaby_hartley_1985]\] \[[Srinivasa et al 2016][research_srinivasa_sridhara_2016]\] \[[Stewart et al 2026][research_stewart_dooher_2026]\] \[[Strelkov and Bozhko 2026][research_strelkov_bozhko_2026]\] \[[Study of determining methods and preventing emergency conditions for the flight of an pilotless vehicle in case of failure of onboard equipment 2023][research_study_of_2023]\] \[[Subbarao et al 2015][research_subbarao_tule_2015]\] \[[Sun et al 2026][research_sun_carmody_2026]\] \[[Szabolcsi 2018][research_szabolcsi_2018]\] \[[Szabolcsi 2018][research_szabolcsi_2018_b]\] \[[Szabolcsi 2018][research_szabolcsi_2018_c]\] \[[Tachinina et al 2024][research_tachinina_lysenko_2024]\] \[[Takita and Kashitani 2016][research_takita_kashitani_2016]\] \[[Tan et al 2018][research_tan_ma_2018]\] \[[Thamann et al 2015][research_thamann_smith_2015]\] \[[Thato Elijah and Rui Vasconcellos 2026][research_thatoelijah_ruivasconcellos_2026]\] \[[The Design of Flight Surveillance and Control System Software for Unmanned Rotorcraft’s Ground Control Station 2015][research_the_design_of_2015]\] \[[Theys et al 2016][research_theys_devos_2016]\] \[[Tomlins 1983][research_tomlins_1983]\] \[[Torres et al 2017][research_torres_candelas_2017]\] \[[Tsench and Kurbanov 2023][research_tsench_kurbanov_2023]\] \[[Tsench et al 2024][research_tsench_kurbanov_2024]\] \[[Tvaryanas 2006][research_tvaryanas_2006]\] \[[Tvaryanas and Maupin 2013][research_tvaryanas_maupin_2013]\] \[[Tvaryanas et al 2012][research_tvaryanas_singer_2012]\] \[[Ungermann 1988][research_ungermann_1988]\] \[[Valavanis 2017][research_valavanis_2017]\] \[[Vandersteen 1987][research_vandersteen_1987]\] \[[Vengate et al 2016][research_vengate_erturk_2016]\] \[[Vinkler and Wood 1978][research_vinkler_wood_1978]\] \[[Vinkler et al 1979][research_vinkler_wood_1979]\] \[[Vinkler et al 1980][research_vinkler_wood_1980]\] \[[Vlasceanu et al 2018][research_vlasceanu_popescu_2018]\] \[[Vránics 2020][research_vranics_2020]\] \[[Wang and Sutton 2004][research_wang_sutton_2004]\] \[[Wang and Zhou 2022][research_wang_zhou_2022]\] \[[Wang et al 2018][research_wang_liu_2018]\] \[[Wang et al 2020][research_wang_gong_2020]\] \[[Wauters et al 2019][research_wauters_browaeys_2019]\] \[[Weibel et al 2015][research_weibel_lawrence_2015]\] \[[Welp et al 1975][research_welp_chace_1975]\] \[[Widiyanti et al 2024][research_widiyanti_asmoro_2024]\] \[[Winslow et al 2018][research_winslow_hrishikeshavan_2018]\] \[[Wolf et al 2016][research_wolf_shelley_2016]\] \[[Wood et al 2019][research_wood_araujoestrada_2019]\] \[[Woolley 1978][research_woolley_1978]\] \[[Wu et al 2017][research_wu_xiao_2017]\] \[[Xie and Low 2017][research_xie_low_2017]\] \[[Xinghua 2018][research_xinghua_2018]\] \[[Xu et al 2019][research_xu_petrunin_2019]\] \[[Yao and Wu 2019][research_yao_wu_2019]\] \[[Younes et al 2019][research_younes_noura_2019]\] \[[Yuksek and Inalhan 2022][research_yuksek_inalhan_2022]\] \[[Yuma Test Center Yuma Proving Ground Az 2008][research_yumatestcenteryumaprovinggroundaz_2008]\] \[[Yunerovna and Valerievich 2015][research_yunerovna_valerievich_2015]\] \[[Zeitler et al 2018][research_zeitler_schwierz_2018]\] \[[Zhang et al 2017][research_zhang_wang_2017]\] \[[Zhang et al 2021][research_zhang_su_2021]\] \[[Zhang et al 2025][research_zhang_sun_2025]\] \[[Zhao et al 2021][research_zhao_duan_2021]\] \[[Zhou and Ma 2025][research_zhou_ma_2025]\] \[[Zhu and Duan 2015][research_zhu_duan_2015]\] \[[Zolanvari et al 2018][research_zolanvari_teixeira_2018]\] \[[Zolotas 2023][research_zolotas_2023]\] \[[Zou et al 2017][research_zou_yin_2017]\] \[[Çoban 2020][research_coban_2020]\] \[[Çoban and Oktay 2018][research_coban_oktay_2018]\]

### Flight test method, instrumentation and system identification

Flight test method, parameter estimation and system identification from flight and wind tunnel data, and the correlation of the tunnel with flight.

**250 records.** \[[Advisory Group for Aerospace Research and Development 1999][research_advisorygroupforaerospaceresearchanddevelopment_1999]\] \[[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]\] \[[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_c]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_d]\] \[[Aircraft performance monitoring from flight data 2015][research_aircraft_performance_2015]\] \[[Aksteter et al 1994][research_aksteter_parks_1994]\] \[[AlAbsi and Fields 2017][research_alabsi_fields_2017]\] \[[Alexander 1991][research_alexander_1991]\] \[[Alford and Knarr 1999][research_alford_knarr_1999]\] \[[AlShabi et al 2024][research_alshabi_saleh_2024]\] \[[American Institute of Aeronautics and Astronautics 1992][research_americaninstituteofaeronauticsandastronautics_1992]\] \[[An et al 2025][research_an_wang_2025]\] \[[Anderson and Vincent 1985][research_anderson_vincent_1985]\] \[[Araujo-Estrada and Windsor 2019][research_araujoestrada_windsor_2019]\] \[[Armstrong 1977][research_armstrong_1977]\] \[[Asher and Hyland 1965][research_asher_hyland_1965]\] \[[Bach and McNally 1988][research_bach_mcnally_1988]\] \[[Badwan and Tutunji 2018][research_badwan_tutunji_2018]\] \[[Balatti et al 2021][research_balatti_haddadkhodaparast_2021]\] \[[Bayoğlu et al 2016][research_bayoglu_nalci_2016]\] \[[Simmons 2023][research_benjaminmsimmons_2023]\] \[[Bennett 1984][research_bennett_1984]\] \[[Benyamen and Keshmiri 2022][research_benyamen_keshmiri_2022]\] \[[Benyamen et al 2024][research_benyamen_chowdhury_2024]\] \[[Bergmann et al 2021][research_bergmann_denzel_2021]\] \[[Beyers 1986][research_beyers_1986]\] \[[Beyers and Ericsson 2002][research_beyers_ericsson_2002]\] \[[Billingsley 1976][research_billingsley_1976]\] \[[Bliss 1980][research_bliss_1980]\] \[[Bousson and Paglione 2001][research_bousson_paglione_2001]\] \[[Brandon and Morelli 2016][research_brandon_morelli_2016]\] \[[Bronz and Hattenberger 2016][research_bronz_hattenberger_2016]\] \[[Buffington et al 1999][research_buffington_chandler_1999]\] \[[Burner et al 2000][research_burner_liu_2000]\] \[[Burton and Bischoff 1976][research_burton_bischoff_1976]\] \[[Butler 1976][research_butler_1976]\] \[[Che et al 2021][research_che_lian_2021]\] \[[Chen and Xiao 2015][research_chen_xiao_2015]\] \[[Chen et al 2019][research_chen_kopsaftopoulos_2019]\] \[[Cheney 1988][research_cheney_1988]\] \[[Clarke and Roskam 1982][research_clarke_roskam_1982]\] \[[Cosentino 2007][research_cosentinogaryb_2007]\] \[[Cosentino 2008][research_cosentinogaryb_2008]\] \[[Danowsky et al 2017][research_danowsky_schmidt_2017]\] \[[Dantsker et al 2019][research_dantsker_yu_2019]\] \[[Dantsker et al 2020][research_dantsker_caccamo_2020]\] \[[Dantsker et al 2023][research_dantsker_caccamo_2023]\] \[[de Visser and Pool 2023][research_devisser_pool_2023]\] \[[Denton et al 2025][research_denton_benedict_2025]\] \[[Dias 2023][research_dias_2023]\] \[[Dogan Kuzey and Yıldırım Dalkıran 2026][research_dogankuzey_yildirimdalkiran_2026]\] \[[Domino et al 2023][research_domino_czyz_2023]\] \[[Donovan and Allison 2017][research_donovan_allison_2017]\] \[[Dwyer 1994][research_dwyer_1994]\] \[[Estlow and Kovacevic 1990][research_estlow_kovacevic_1990]\] \[[Eulrich and Rynaski 1980][research_eulrich_rynaski_1980]\] \[[Eulrich et al 1978][research_eulrich_govindaraj_1978]\] \[[Farhadi 2017][research_farhadi_2017]\] \[[Fegely et al 2016][research_fegely_tischler_2016]\] \[[Flight Test Programme 1970][research_flight_test_1970]\] \[[Flight-test evaluation of engine power effects on lift and drag 1985][research_flight_test_evaluation_1985]\] \[[Friehmelt 1997][research_friehmelt_1997]\] \[[Fry and Sage 1974][research_fry_sage_1974]\] \[[Fry and Sage 1974][research_frycm_sageap_1974]\] \[[Fukami et al 2004][research_fukami_higashino_2004]\] \[[Gandhi et al 2019][research_gandhi_whitcher_2019]\] \[[Gao et al 2021][research_gao_wang_2021]\] \[[Ge and Zhan 2024][research_ge_zhan_2024]\] \[[Gebert et al 2000][research_gebert_kelly_2000]\] \[[Geng and Li 2023][research_geng_li_2023]\] \[[Ghazi 1993][research_ghazi_1993]\] \[[Ghosh and Raisinghani 2000][research_ghosh_raisinghani_2000]\] \[[Ghosh and Raisinghani 2002][research_ghosh_raisinghani_2002]\] \[[Ghosh Roy and Peyada 2016][research_ghoshroy_peyada_2016]\] \[[Ghosh Roy and Peyada 2017][research_ghoshroy_peyada_2017]\] \[[Grauer 2015][research_grauer_2015]\] \[[Grauer 2016][research_grauer_2016]\] \[[Grauer 2020][research_grauer_2020]\] \[[Grauer 2021][research_grauer_2021]\] \[[Grauer and Boucher 2018][research_grauer_boucher_2018]\] \[[Grauer and Morelli 2015][research_grauer_morelli_2015]\] \[[Gres et al 2025][research_gres_stoura_2025]\] \[[Gresham et al 2023][research_gresham_simmons_2023]\] \[[Guenther et al 2026][research_guenther_eichner_2026]\] \[[Göttlicher et al 2016][research_gottlicher_gnoth_2016]\] \[[Hale et al 2015][research_hale_patil_2015]\] \[[Hale et al 2017][research_hale_patil_2017]\] \[[Halefom et al 2022][research_halefom_gresham_2022]\] \[[Hamel and Jategaonkar 1996][research_hamel_jategaonkar_1996]\] \[[Han et al 2025][research_han_wang_2025]\] \[[Harris et al 2016][research_harris_arthurs_2016]\] \[[Herrlinger 1991][research_herrlinger_1991]\] \[[Hoffer et al 2015][research_hoffer_coopmans_2015]\] \[[Hofmann et al 2025][research_hofmann_hosseini_2025]\] \[[Hosseini et al 2025][research_hosseini_hofmann_2025]\] \[[Hull and Roger 1975][research_hull_roger_1975]\] \[[Hutt and East 1985][research_hutt_east_1985]\] \[[Ibuka and Ishiguro 2023][research_ibuka_ishiguro_2023]\] \[[Iliff 1987][research_iliff_1987]\] \[[Iliff and Maine 1983][research_iliff_maine_1983]\] \[[Irwanto and Artono 2018][research_irwanto_artono_2018]\] \[[Ishola et al 2024][research_ishola_whidborne_2024]\] \[[Jaganraj and Velu 2019][research_jaganraj_velu_2019]\] \[[Jain et al 2025][research_jain_singla_2025]\] \[[Jategaonkar et al 1997][research_jategaonkar_monnich_1997]\] \[[Jones 1995][research_jones_1995]\] \[[Jordan 1974][research_jordan_1974]\] \[[Juhasz et al 2020][research_juhasz_xin_2020]\] \[[Klein 1978][research_klein_1978]\] \[[Klein 1989][research_klein_1989]\] \[[Klein and Murphy 2001][research_klein_murphy_2001]\] \[[Knighton 1992][research_knightondonnal_1992]\] \[[Kohlman 1977][research_kohlman_1977]\] \[[Kohlman 1979][research_kohlman_1979]\] \[[Kokolios 1994][research_kokolios_1994]\] \[[Korsun and Moung Htang 2023][research_korsun_mounghtang_2023]\] \[[Korsun et al 2018][research_korsun_stulovskii_2018]\] \[[Kraft 2018][research_kraft_2018]\] \[[Kumar and Ghosh 2017][research_kumar_ghosh_2017]\] \[[Kumar and Ghosh 2018][research_kumar_ghosh_2018]\] \[[Kumar and Ghosh 2018][research_kumar_ghosh_2018_b]\] \[[Kumar and Ghosh 2018][research_kumar_ghosh_2018_c]\] \[[Kumar and Ghosh 2023][research_kumar_ghosh_2023]\] \[[Kumar and Rao 2004][research_kumar_rao_2004]\] \[[Kumar et al 2015][research_kumar_steck_2015]\] \[[Lawrence and Mills 2002][research_lawrence_mills_2002]\] \[[Lebacqz 1974][research_lebacqzjv_1974]\] \[[Legowo et al 2019][research_legowo_sulaeman_2019]\] \[[Lerro et al 2020][research_lerro_brandl_2020]\] \[[Leshikar et al 2021][research_leshikar_eves_2021]\] \[[Leung et al 2019][research_leung_moszczynski_2019]\] \[[Li and Gao 2025][research_li_gao_2025]\] \[[Li et al 2026][research_li_sheng_2026]\] \[[Lichota 2016][research_lichota_2016]\] \[[Lichota 2023][research_lichota_2023]\] \[[Lichota et al 2016][research_lichota_ohme_2016]\] \[[Liu et al 2018][research_liu_zhou_2018]\] \[[Lu and Van Kampen 2015][research_lu_vankampen_2015]\] \[[Mamou and Broughton 2023][research_mamou_broughton_2023]\] \[[Margason and Hoad 1980][research_margason_hoad_1980]\] \[[Matt et al 2025][research_matt_chao_2025]\] \[[Maunder 1979][research_maunder_1979]\] \[[McCrink and Gregory 2017][research_mccrink_gregory_2017]\] \[[Mehra and Eupta 1975][research_mehrark_euptank_1975]\] \[[Mehra and Tyler 1973][research_mehrark_tylerjs_1973]\] \[[Metodiev 2024][research_metodiev_2024]\] \[[Miller 1973][research_millerjr_1973]\] \[[Moes and Iliff 2002][research_moestimothyr_iliffkenneth_2002]\] \[[Moes et al 2003][research_moestimothyr_smithmarks_2003]\] \[[Mohamed et al 2019][research_mohamed_madhavan_2019]\] \[[Molusis 1973][research_molusis_1973]\] \[[Molusis 1973][research_molusisja_1973]\] \[[Molusis and Briczinski 1974][research_molusisjh_briczinskis_1974]\] \[[Morelli 2021][research_morelli_2021]\] \[[Morelli and Cooper 2015][research_morelli_cooper_2015]\] \[[Morelli and Klein 1995][research_morelli_klein_1995]\] \[[Morelli and DeLoach 2003][research_morellieugenea_deloachrichard_2003]\] \[[Morris 1964][research_morris_1964]\] \[[Morris 1966][research_morris_1966]\] \[[Moszczynski and Grant 2017][research_moszczynski_grant_2017]\] \[[Moszczynski et al 2019][research_moszczynski_leung_2019]\] \[[Moua et al 2007][research_mouacheng_mcwhertershaunh_2007]\] \[[Moua et al 2012][research_mouachengm_mcwhertershaunc_2012]\] \[[Mulder 1985][research_mulder_1985]\] \[[Murphy et al 2004][research_murphy_klein_2004]\] \[[Neves et al 2020][research_neves_lawson_2020]\] \[[Neville and Stephens 1993][research_neville_stephens_1993]\] \[[Nicola et al 2025][research_nicola_dicapua_2025]\] \[[Nicolosi et al 2015][research_nicolosi_demarco_2015]\] \[[Niewald and Parker 2000][research_niewald_parker_2000]\] \[[O'Donnell and Mohseni 2018][research_odonnell_mohseni_2018]\] \[[Ovcharenko and Poplavsky 2021][research_ovcharenko_poplavsky_2021]\] \[[Parameter estimation techniques and 1974][research_parameter_estimation_1974]\] \[[Park 1977][research_park_1977]\] \[[Pfifer and Danowsky 2016][research_pfifer_danowsky_2016]\] \[[Plaetschke et al 1982][research_plaetschke_mulder_1982]\] \[[Pounds and Walker 1980][research_pounds_walker_1980]\] \[[Dhayalan et al 2018][research_r_saderla_2018]\] \[[Raisinghani and Adak 1983][research_raisinghani_adak_1983]\] \[[Ratcliff et al 2016][research_ratcliff_bodkin_2016]\] \[[Rhew and Parker 2017][research_rhew_parker_2017]\] \[[Rodzewicz 2024][research_rodzewicz_2024]\] \[[Saderla et al 2016][research_saderla_r_2016]\] \[[Saderla et al 2017][research_saderla_rajaram_2017]\] \[[Saraswathi 2000][research_saraswathi_2000]\] \[[Schaff and Prazenica 2024][research_schaff_prazenica_2024]\] \[[Schumacher 1952][research_schumacher_1952]\] \[[Schwanz and Grimes 1980][research_schwanz_grimes_1980]\] \[[Sharpe and Hansman 2024][research_sharpe_hansman_2024]\] \[[Shi et al 2023][research_shi_wang_2023]\] \[[Simmons 2022][research_simmons_2022]\] \[[Simmons 2023][research_simmons_2023]\] \[[Simmons and Murphy 2021][research_simmons_murphy_2021]\] \[[Simmons et al 2019][research_simmons_mcclelland_2019]\] \[[Simmons et al 2023][research_simmons_gresham_2023]\] \[[Simmons et al 2023][research_simmons_gresham_2023_b]\] \[[Simpson 1972][research_simpson_1972]\] \[[Simpson 1979][research_simpson_1979]\] \[[Smetana et al 1972][research_smetanafo_summerydc_1972]\] \[[Smith et al 2003][research_smithmarks_moestimothyr_2003]\] \[[Sokolov et al 2017][research_sokolov_beklemichev_2017]\] \[[Soltmann and Hall 2017][research_soltmann_hall_2017]\] \[[Song et al 2002][research_song_song_2002]\] \[[Song et al 2022][research_song_sanchezcuevas_2022]\] \[[Souza et al 2019][research_souza_castillozuniga_2019]\] \[[Speyer and Crues 1985][research_speyer_crues_1985]\] \[[Speyer and Crues 1987][research_speyer_crues_1987]\] \[[Srinathkumar et al 1995][research_srinathkumar_parameswaran_1995]\] \[[Steinmetz et al 1972][research_steinmetzgg_parrishrv_1972]\] \[[Stouder 1981][research_stouder_1981]\] \[[Strader et al 2016][research_strader_harper_2016]\] \[[Sun et al 2019][research_sun_devisser_2019]\] \[[Szymanski et al 2025][research_szymanski_ghazi_2025]\] \[[Tavoularis 1999][research_tavoularis_1999]\] \[[Taylor et al 1992][research_taylor_bennett_1992]\] \[[Thompson et al 2017][research_thompson_xu_2017]\] \[[Tomaine et al 1978][research_tomainerl_bryantwh_1978]\] \[[Travassos and Kaufman 1979][research_travassos_kaufman_1979]\] \[[Traven and Whitley 1995][research_traven_whitley_1995]\] \[[Venkataraman and Seiler 2019][research_venkataraman_seiler_2019]\] \[[Verhaegen 1988][research_verhaegen_1988]\] \[[Verma and Peyada 2018][research_verma_peyada_2018]\] \[[Wang and Iliff 2004][research_wang_iliff_2004]\] \[[Wang et al 1986][research_wang_demiroz_1986]\] \[[Wang et al 2015][research_wang_chen_2015]\] \[[Wang et al 2021][research_wang_qi_2021_b]\] \[[Wang et al 2022][research_wang_tai_2022]\] \[[Wang et al 2023][research_wang_shen_2023]\] \[[Ward 1968][research_ward_1968]\] \[[Wei and Renliang 2015][research_wei_renliang_2015]\] \[[Weinstein et al 2018][research_weinstein_hubbard_2018]\] \[[Weiss and Thielecke 2000][research_weiss_thielecke_2000]\] \[[Wells et al 1979][research_wells_banda_1979]\] \[[Wells et al 1982][research_wells_banda_1982]\] \[[Whitefield et al 1981][research_whitefield_griffith_1981]\] \[[Wingrove 1978][research_wingroverc_1978]\] \[[Wisbacher et al 2025][research_wisbacher_ossmann_2025]\] \[[Woodbury et al 2015][research_woodbury_valasek_2015]\] \[[Woodruff 2009][research_woodruffstephenl_2009]\] \[[Yasue 2020][research_yasue_2020]\] \[[Yavuztürk and Topbas 2020][research_yavuzturk_topbas_2020]\] \[[Yavuztürk et al 2017][research_yavuzturk_topbas_2017]\] \[[Yeager 1997][research_yeagerjessiec_1997]\] \[[Yechout 1988][research_yechout_1988]\] \[[Yechout and Schweikhard 1984][research_yechout_schweikhard_1984]\] \[[Yeo et al 2015][research_yeo_atkins_2015]\] \[[Yu et al 2017][research_yu_wang_2017]\] \[[Zhou and Wang 2026][research_zhou_wang_2026]\] \[[Zhou et al 2023][research_zhou_liu_2023]\]

### High angle of attack, vortex flow and departure

High angle of attack aerodynamics and control, vortex flow and vortex breakdown, departure and spin.

**227 records.** \[[Adams 1993][research_adamsrichardj_1993]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]\] \[[Alferov et al 1982][research_alferov_vernikova_1982]\] \[[Anderson 1984][research_anderson_1984]\] \[[Anderson 1985][research_anderson_1985]\] \[[Arena and Nelson 1989][research_arenaasjr_nelsonrc_1989]\] \[[Axelson 1975][research_axelson_1975]\] \[[Ayoub and McLachlan 1988][research_ayoub_mclachlan_1988]\] \[[Ayoub and McLachlan 1987][research_ayouba_mclachlanbg_1987]\] \[[Bagherzadeh et al 2025][research_bagherzadeh_mohammadkarimi_2025]\] \[[Banks 1988][research_banksdanielw_1988]\] \[[Bay and Kara 2026][research_bay_kara_2026]\] \[[Bennett et al 2017][research_bennett_lawson_2017]\] \[[Bigler 1986][research_bigler_1986]\] \[[Bihrle and Barnhart 1982][research_bihrle_barnhart_1982]\] \[[Bihrle and Billy 1980][research_bihrle_jr_1980]\] \[[Bihrle 1970][research_bihrlejr_1970]\] \[[Bihrle and Bowman 1980][research_bihrlewjr_bowmanjsjr_1980]\] \[[Boyden 1970][research_boyden_1970]\] \[[Boyden 1971][research_boyden_1971]\] \[[Brody and Fagley 2024][research_brody_fagley_2024]\] \[[Bruns and Smith 1992][research_brunsjamese_smithcf_1992]\] \[[Bui 2016][research_bui_2016]\] \[[Canin 2019][research_canin_2019]\] \[[Carine Viola Dsouza and Dr. Basawaraj 2015][research_carinevioladsouza_drbasawaraj_2015]\] \[[Cornelius and Lucius 1993][research_cornelius_lucius_1993_b]\] \[[Cornelius and Lucius 1994][research_cornelius_lucius_1994]\] \[[Cunis et al 2018][research_cunis_leth_2018]\] \[[Debry et al 1992][research_debry_komerath_1992]\] \[[Dias 2015][research_dias_2015]\] \[[Durston and Schreiner 1983][research_durston_schreiner_1983]\] \[[Ekaterinaris and Schiff 1990][research_ekaterinaris_schiff_1990]\] \[[Elmiligui et al 2015][research_elmiligui_abdolhamid_2015]\] \[[Elmiligui et al 2017][research_elmiligui_abdolhamid_2017]\] \[[Erickson and Brandon 1987][research_erickson_brandon_1987]\] \[[Erickson 1991][research_ericksongarye_1991]\] \[[Ericsson 1996][research_ericsson_1996]\] \[[Ericsson 1996][research_ericsson_1996_b]\] \[[Ericsson 1997][research_ericsson_1997]\] \[[Ericsson and Hanff 1994][research_ericsson_hanff_1994]\] \[[Farcy et al 2020][research_farcy_khrabrov_2020]\] \[[Faure and Leogrande 2020][research_faure_leogrande_2020]\] \[[Feng et al 2024][research_feng_wang_2024]\] \[[Fischenberg 1995][research_fischenberg_1995]\] \[[François et al 2021][research_francois_probst_2021]\] \[[Gee et al 1992][research_geeken_rizkyehiam_1992]\] \[[Go and Maqsood 2015][research_go_maqsood_2015]\] \[[Gordnier 1995][research_gordnier_1995]\] \[[Grafton et al 1982][research_graftonsb_gilberwp_1982]\] \[[Greenwell 2003][research_greenwell_2003]\] \[[Gursul and Yang 1994][research_gursul_yang_1994]\] \[[Gursul and Yang 1995][research_gursul_yang_1995]\] \[[Gursul et al 1995][research_gursul_srinivas_1995]\] \[[Hadidoolabi and Ansarian 2017][research_hadidoolabi_ansarian_2017]\] \[[Hadidoolabi and Ansarian 2018][research_hadidoolabi_ansarian_2018]\] \[[Hall et al 1998][research_hallrobertm_ericksongarye_1998]\] \[[Heald and Brassell 1976][research_heald_brassell_1976]\] \[[Hebbar et al 1991][research_hebbar_platzer_1991]\] \[[Hitzel 1988][research_hitzel_1988]\] \[[Hitzel 2017][research_hitzel_2017]\] \[[Hollingsworth and Cohen 1971][research_hollingsworth_cohen_1971]\] \[[Hreha and Lutze 1983][research_hreha_lutze_1983]\] \[[Hreha and Lutze 1984][research_hreha_lutze_1984]\] \[[Huang et al 2026][research_huang_li_2026]\] \[[Innocenti 1989][research_innocenti_1989]\] \[[Ishibashi and Miyaji 2015][research_ishibashi_miyaji_2015]\] \[[Jarrah 1989][research_jarrah_1989]\] \[[Johnson et al 1980][research_johnsonjljr_newsomwa_1980]\] \[[Johnston and Hogge 1974][research_johnston_hogge_1974]\] \[[Johnston and Hogge 1976][research_johnston_hogge_1976]\] \[[Kapuscinski et al 2020][research_kapuscinski_szczerba_2020]\] \[[Kofman and Becus 1996][research_kofman_becus_1996]\] \[[Kramer and Smith 1994][research_kramerbrian_smithbrooke_1994]\] \[[Kurade et al 2021][research_kurade_venkatakrishnan_2021]\] \[[Lackey and Hadfield 1992][research_lackey_hadfield_1992]\] \[[Landa et al 2018][research_landa_klug_2018]\] \[[Lanser and Meyn 1992][research_lanserwendyr_meynlarrya_1992]\] \[[Lee and Han 2019][research_lee_han_2019]\] \[[Lee and Ko 2017][research_lee_ko_2017]\] \[[Lee and Marnineau-Mes 1996][research_lee_marnineaumes_1996]\] \[[Lee and Libbey 1961][research_leehenrya_libbeycharlese_1961]\] \[[Li and Yang 2017][research_li_yang_2017]\] \[[Liberatori et al 2023][research_liberatori_valorani_2023]\] \[[Lin and Rockwell 1995][research_lin_rockwell_1995]\] \[[Liu et al 2016][research_liu_luo_2016]\] \[[Liu et al 2018][research_liu_luo_2018]\] \[[Lofthouse and Cummings 2015][research_lofthouse_cummings_2015]\] \[[Lofthouse and Cummings 2017][research_lofthouse_cummings_2017]\] \[[Lowson and Riley 1994][research_lowson_riley_1994]\] \[[Lowson and Riley 1995][research_lowson_riley_1995]\] \[[Nguyen et al 1980][research_luattnguyen_williampgilbert_1980]\] \[[Luckring et al 2022][research_luckring_taylor_2022]\] \[[Ma et al 2020][research_ma_shi_2020]\] \[[Malik et al 2020][research_malik_masud_2020]\] \[[Malik et al 2021][research_malik_masud_2021]\] \[[Marchman 1981][research_marchmaniii_1981]\] \[[Mayya et al 2022][research_mayya_karnick_2022]\] \[[McKeehen and Cord 1997][research_mckeehen_cord_1997]\] \[[Mello and Agnew 1979][research_mello_agnew_1979]\] \[[Menke and Gursul 1999][research_menke_gursul_1999]\] \[[Meyer et al 1989][research_meyerhf_yiplp_1989]\] \[[Milillo 1972][research_milillo_1972]\] \[[Mitchell et al 1980][research_mitchell_myers_1980]\] \[[Mitrut et al 2021][research_mitrut_bucur_2021]\] \[[Moore et al 1980][research_moore_skow_1980]\] \[[Morton 2003][research_morton_2003]\] \[[Morton et al 2002][research_morton_mitchell_2002]\] \[[Murri et al 1983][research_murri_croom_1983]\] \[[Naigle et al 2022][research_naigle_hiltner_2022]\] \[[Nelson 1985][research_nelson_1985]\] \[[Nelson and Mouch 1978][research_nelson_mouch_1978]\] \[[Nguyen 1979][research_nguyen_1979]\] \[[Numerical Analysis of the Flow Pattern and Vortex Breakdown over a Pitching Delta wing at Supersonic Speeds 2017][research_numerical_analysis_2017]\] \[[Ogburn et al 1993][research_ogburn_foster_1993]\] \[[Osipov 2019][research_osipov_2019]\] \[[Ostroff 1998][research_ostroffaaronj_1998]\] \[[Ozgören et al 2002][research_ozgoren_sahin_2002]\] \[[Patel and Smith 1996][research_patel_smith_1996]\] \[[Patel et al 2002][research_patel_prince_2002]\] \[[Patten 1988][research_patten_1988]\] \[[Pedreiro et al 1998][research_pedreiro_rock_1998]\] \[[Pelikan 1974][research_pelikan_1974]\] \[[Pelletier and Nelson 2000][research_pelletier_nelson_2000]\] \[[Pfnür and Breitsamter 2019][research_pfnur_breitsamter_2019]\] \[[Pitts et al 1974][research_pittsfl_holmesdce_1974]\] \[[Planeaux and Barth 1988][research_planeaux_barth_1988]\] \[[Prediction of vortex breakdown effects on a rolling delta wing 1994][research_prediction_of_1994]\] \[[Probst et al 2019][research_probst_knopp_2019]\] \[[Qi and Zhongke 2015][research_qi_zhongke_2015]\] \[[Rainbird et al 2015][research_rainbird_peiro_2015]\] \[[Ransom 1983][research_ransom_1983]\] \[[Rao 1989][research_rao_1989]\] \[[Rao and Murri 1986][research_rao_murri_1986]\] \[[Rao et al 1987][research_rao_moskovitz_1987]\] \[[Rao et al 1986][research_raodm_moskovitzc_1986]\] \[[Rhodeside 1986][research_rhodeside_1986]\] \[[Biedron and Whitaker 1994][research_roberttbiedron_davidlwhitaker_1994]\] \[[Li and Yang 2017][research_li_yang_2017_b]\] \[[Rohith and Sinha 2017][research_rohith_sinha_2017]\] \[[Rom et al 1987][research_rom_almosnino_1987]\] \[[Roos 1996][research_roos_1996]\] \[[Roos 2001][research_roos_2001]\] \[[Roy et al 2023][research_roy_biswas_2023]\] \[[Russell et al 2022][research_russell_werner_2022]\] \[[Saderla et al 2016][research_saderla_dhayalan_2016]\] \[[Sahin et al 2026][research_sahin_yayla_2026]\] \[[Salahudden 2024][research_salahudden_2024]\] \[[Salahudden 2025][research_salahudden_2025]\] \[[Salahudden and Ghosh 2021][research_salahudden_ghosh_2021]\] \[[Salahudden et al 2020][research_salahudden_giri_2020]\] \[[Salahudden et al 2022][research_salahudden_das_2022]\] \[[Salahudden et al 2024][research_salahudden_singh_2024]\] \[[Salahudden et al 2025][research_salahudden_kumar_2025]\] \[[Salehian et al 2022][research_salehian_khan_2022]\] \[[Salehian et al 2024][research_salehian_khan_2024]\] \[[Salehian et al 2025][research_salehian_khan_2025]\] \[[Schaeffler and Rediniotis 1995][research_schaeffler_rediniotis_1995]\] \[[Schmidt et al 2025][research_schmidt_hartl_2025]\] \[[Schrader et al 1988][research_schrader_reynolds_1988]\] \[[Sedlacek et al 2022][research_sedlacek_breitsamter_2022]\] \[[Sellers et al 1988][research_sellerswilliamliii_meyersjamesf_1988]\] \[[Sellers et al 2004][research_sellerswilliamliii_meyersjamesf_2004]\] \[[Seraj and Martins 2022][research_seraj_martins_2022]\] \[[Shah 1991][research_shahgautamh_1991]\] \[[Shivam and Verma 2019][research_shivam_verma_2019]\] \[[Shojae et al 2025][research_shojae_salehi_2025]\] \[[Silva and Wolf 2024][research_silva_wolf_2024]\] \[[Silva and Wolf 2026][research_silva_wolf_2026]\] \[[Singh and Jategaonkar 1996][research_singh_jategaonkar_1996_b]\] \[[Skow et al 1982][research_skow_moore_1982]\] \[[Skow and Peake 1983][research_skowam_peakedj_1983]\] \[[Son et al 2015][research_son_sa_2015]\] \[[Son et al 2015][research_son_sa_2015_b]\] \[[Stoll and Koenig 1983][research_stollf_koenigdg_1983]\] \[[Strickland et al 1996][research_stricklandmarke_bundickwthomas_1996]\] \[[Suarez et al 1992][research_suarezcarlosj_kramerbrianr_1992]\] \[[Suarez et al 1992][research_suarezcarlosj_malcolmgeraldn_1992]\] \[[Suarez et al 1993][research_suarezcarlosj_smithbrookec_1993]\] \[[Symposium on Advanced Flow 2003][research_symposium_on_2003]\] \[[Taylor and Skow 1988][research_taylor_skow_1988]\] \[[Tinger 1987][research_tinger_1987]\] \[[Tinoco 2020][research_tinoco_2020]\] \[[Towfighi and Rockwell 1993][research_towfighi_rockwell_1993]\] \[[Uhlig and Selig 2017][research_uhlig_selig_2017]\] \[[Valasek and Walchli 1998][research_valasek_walchli_1998]\] \[[Van Dommelen 1995][research_vandommelen_1995]\] \[[Vauchel and Caro 2026][research_vauchel_caro_2026]\] \[[Venkateswara Rao and Go 2019][research_venkateswararao_go_2019]\] \[[Visbal 1993][research_visbal_1993]\] \[[Visbal 1993][research_visbal_1993_b]\] \[[Visbal 1994][research_visbal_1994]\] \[[Visbal 1995][research_visbal_1995]\] \[[Visbal 1997][research_visbal_1997]\] \[[Visonneau et al 2022][research_visonneau_guilmineau_2022]\] \[[Vlahostergios et al 2018][research_vlahostergios_komnos_2018]\] \[[Vorobieff and Rockwell 1996][research_vorobieff_rockwell_1996]\] \[[Walchli et al 1992][research_walchli_guyton_1992]\] \[[Waldmann 2015][research_waldmann_2015]\] \[[Wan et al 2023][research_wan_ghoreyshi_2023]\] \[[Wang et al 2016][research_wang_gao_2016]\] \[[Wang et al 2017][research_wang_ye_2017]\] \[[Wang et al 2021][research_wang_ma_2021]\] \[[Wang et al 2023][research_wang_zhao_2023]\] \[[Wang et al 2025][research_wang_luo_2025_b]\] \[[Webster and Shang 1989][research_webster_shang_1989]\] \[[Wei et al 2017][research_wei_chen_2017]\] \[[Weissman 1972][research_weissman_1972]\] \[[Weissman 1973][research_weissman_1973]\] \[[Weissman 1974][research_weissman_1974]\] \[[Weissman 1975][research_weissman_1975]\] \[[Wendel et al 1991][research_wendel_boland_1991]\] \[[Werner et al 2022][research_werner_schutte_2022]\] \[[Werner et al 2024][research_werner_schutte_2024]\] \[[Witkowski et al 2022][research_witkowski_williams_2022]\] \[[Wu et al 2017][research_wu_yang_2017]\] \[[Xiong and Nguyen 2023][research_xiong_nguyen_2023]\] \[[Xiong et al 2026][research_xiong_nguyen_2026]\] \[[Xu et al 2016][research_xu_jiang_2016]\] \[[Yang et al 2015][research_yang_chen_2015]\] \[[Yoo 2018][research_yoo_2018]\] \[[York and Anderson 1994][research_york_anderson_1994]\] \[[Zhang and Samtaney 2016][research_zhang_samtaney_2016]\] \[[Zhang et al 2017][research_zhang_zhang_2017]\] \[[Zhou et al 2019][research_zhou_diskin_2019]\] \[[Zhu et al 2019][research_zhu_liu_2019]\] \[[Zohar and Er-El 1988][research_zohar_erel_1988]\] \[[Zwerger et al 2015][research_zwerger_hickel_2015]\]

### Tailless aircraft and flying wings

Tailless aircraft and flying wings, their stability, control and design, from the wartime tailless gliders to the unmanned combat aircraft.

**214 records.** \[[Addington and Myatt 2000][research_addington_myatt_2000]\] \[[Ahmed et al 2024][research_ahmed_zakaria_2024]\] \[[Aleisa et al 2023][research_aleisa_kontis_2023_b]\] \[[Asaro and Vos 2025][research_asaro_vos_2025]\] \[[Asaro and Vos 2026][research_asaro_vos_2026]\] \[[Ashkenas and Klyde 1989][research_ashkenasirvingl_klydedavidh_1989]\] \[[Atmaca et al 2026][research_atmaca_stroosma_2026]\] \[[Balasubramanian et al 2024][research_balasubramanian_ahuja_2024]\] \[[Banerjee 1988][research_banerjee_1988_b]\] \[[Barker and Balas 1999][research_barker_balas_1999]\] \[[Bishop 1961][research_bishop_1961]\] \[[Bliamis et al 2021][research_bliamis_zacharakis_2021]\] \[[Boskovic et al][research_boskovic_saimingli]\] \[[Bowlus et al 1997][research_bowlus_multhopp_1997]\] \[[Brewer 1946][research_brewergeraldw_1946]\] \[[Brinker and Wise 1998][research_brinker_wise_1998]\] \[[Brinker and Wise 1999][research_brinker_wise_1999]\] \[[Buffington 1999][research_buffington_1999]\] \[[Buffington 1999][research_buffington_1999_b]\] \[[Calise et al 2001][research_calise_lee_2001]\] \[[Campos and Marques 2021][research_campos_marques_2021]\] \[[Chaudhuri et al 2018][research_chaudhuri_jasa_2018]\] \[[Colgren and Loschke 2008][research_colgren_loschke_2008]\] \[[Cong et al 2023][research_cong_hu_2023_b]\] \[[Cook and Hauser 2018][research_cook_hauser_2018]\] \[[Coppin et al 2018][research_coppin_birch_2018]\] \[[Cosentino 2007][research_cosentinogaryb_2007_b]\] \[[Cox et al 1949][research_cox_siddall_1949]\] \[[Cusher and Gopalarathnam 2006][research_cusher_gopalarathnam_2006]\] \[[Cusher and Gopalarathnam 2012][research_cusher_gopalarathnam_2012]\] \[[de Becdelievre and Kroo 2021][research_debecdelievre_kroo_2021]\] \[[DeLaurier 2022][research_delaurier_2022]\] \[[Deslich et al 2021][research_deslich_flick_2021]\] \[[Development of Neo-Ptero Tailless Micro Aircraft 2018][research_development_of_2018]\] \[[Eberhardt and Ward 1999][research_eberhardt_ward_1999]\] \[[Ericsson and Beyers 2002][research_ericsson_beyers_2002]\] \[[Esfandabadi and Djavareshkian 2026][research_esfandabadi_djavareshkian_2026]\] \[[Experimental investigation of synthetic jet control of wing rock for a flying wing aircraft 2023][research_experimental_investigation_2023]\] \[[Flanagan et al 2020][research_flanagan_chao_2020]\] \[[Flow Control and High-Lift Performance for Flying-Wing Unmanned Combat Air Vehicle Configurations by inserting slots 2016][research_flow_control_2016]\] \[[Friehmelt 1996][research_friehmelt_1996]\] \[[Gamble and Inman 2016][research_gamble_inman_2016]\] \[[Gan and Zha 2015][research_gan_zha_2015]\] \[[Gillard 1998][research_gillard_1998]\] \[[Gillard et al 1997][research_gillard_dorsett_1997]\] \[[Grismer et al 1997][research_grismer_myatt_1997]\] \[[Guiler][research_guiler]\] \[[Guiler and Huebsch 2005][research_guiler_huebsch_2005]\] \[[Hall et al 2006][research_hall_lawrence_2006]\] \[[Hauser 1999][research_hauser_1999]\] \[[He et al 2022][research_he_hu_2022]\] \[[He et al 2022][research_he_hu_2022_b]\] \[[Hoffler et al 1988][research_hoffler_rao_1988]\] \[[Hong and Ma 2016][research_hong_ma_2016]\] \[[Hu et al 2024][research_hu_song_2024]\] \[[Hu et al 2025][research_hu_zhao_2025]\] \[[Huang and Zhang 2020][research_huang_zhang_2020]\] \[[Huber 2022][research_huber_2022]\] \[[Jentzsch et al 2017][research_jentzsch_taubert_2017]\] \[[Jentzsch et al 2019][research_jentzsch_taubert_2019]\] \[[Jiang et al 2019][research_jiang_zhang_2019]\] \[[Jiang et al 2025][research_jiang_li_2025]\] \[[Jiguang Li et al 2016][research_jiguangli_xinchen_2016]\] \[[Jo et al 2015][research_jo_park_2015]\] \[[Jo et al 2016][research_jo_park_2016]\] \[[Kalyankar et al 2024][research_kalyankar_pompe_2024]\] \[[Karimi Kelayeh and Djavareshkian 2024][research_karimikelayeh_djavareshkian_2024]\] \[[Keidel et al 2019][research_keidel_fasel_2019]\] \[[Keidel et al 2020][research_keidel_fasel_2020]\] \[[Kim et al 2025][research_kim_koh_2025]\] \[[Kwiek 2019][research_kwiek_2019]\] \[[Lee 1946][research_lee_1946]\] \[[Lee 1947][research_lee_1947]\] \[[Leishman 2026][research_leishman_2026]\] \[[Lesalli and Cahyono 2020][research_lesalli_cahyono_2020]\] \[[Li and Cai 2026][research_li_cai_2026]\] \[[Li et al 2017][research_li_yong_2017]\] \[[Li et al 2018][research_li_shi_2018]\] \[[Li et al 2022][research_li_sun_2022]\] \[[Lim et al 2025][research_lim_hur_2025]\] \[[Liu and Hu 2014][research_liu_hu_2014]\] \[[Liu and Jiao 2017][research_liu_jiao_2017]\] \[[Liu and Zhang 2022][research_liu_zhang_2022_b]\] \[[Liu et al 2021][research_liu_luo_2021]\] \[[Liu et al 2025][research_liu_zheng_2025]\] \[[Loechert et al 2018][research_loechert_huber_2018]\] \[[Lyu et al 2023][research_lyu_zhang_2023]\] \[[Ma et al 2008][research_ma_li_2008]\] \[[Ma et al 2019][research_ma_zhu_2019]\] \[[Marques 2013][research_marques_2013]\] \[[McKeehen 1998][research_mckeehen_1998]\] \[[Meckstroth and Blake 2015][research_meckstroth_blake_2015]\] \[[Meckstroth and Ordóñez 2020][research_meckstroth_ordonez_2020]\] \[[Meckstroth and Ordóñez 2020][research_meckstroth_ordonez_2020_b]\] \[[Metin et al 2023][research_metin_uzuner_2023]\] \[[Mirosław et al 2022][research_miroslaw_dominik_2022]\] \[[Mohammadi Farhadi et al 2018][research_mohammadifarhadi_kortunov_2018]\] \[[Mohan and Kumar 2025][research_mohan_kumar_2025]\] \[[Molinari et al 2015][research_molinari_arrieta_2015]\] \[[Molinari et al 2018][research_molinari_arrieta_2018]\] \[[Morris 1992][research_morris_1992]\] \[[Morris et al 2014][research_morris_allison_2014]\] \[[Myatt et al 1998][research_myatt_schumacher_1998]\] \[[Nae 2026][research_nae_2026]\] \[[Nedilko et al 2026][research_nedilko_kolisnichenko_2026]\] \[[Ngo et al 1996][research_ngo_reigelsperger_1996]\] \[[Nie et al 2021][research_nie_liu_2021]\] \[[Niestroy 2025][research_niestroy_2025]\] \[[Niestroy et al 2017][research_niestroy_dorsett_2017]\] \[[Niestroy et al 2019][research_niestroy_williams_2019]\] \[[Nieto-Wire and Sobel 2007][research_nietowire_sobel_2007]\] \[[Nieto-Wire and Sobel 2009][research_nietowire_sobel_2009]\] \[[Nieto-Wire and Sobel 2011][research_nietowire_sobel_2011]\] \[[Nieto-Wire and Sobel 2013][research_nietowire_sobel_2013]\] \[[Nieto-Wire and Sobel 2014][research_nietowire_sobel_2014]\] \[[Oosterom and Vos 2022][research_oosterom_vos_2022]\] \[[Orhan and Subbarao 2021][research_orhan_subbarao_2021]\] \[[Owashi et al 2017][research_owashi_tanaka_2017]\] \[[Pan and Huang 2018][research_pan_huang_2018]\] \[[Pan and Huang 2019][research_pan_huang_2019]\] \[[Pan and Huang 2019][research_pan_huang_2019_b]\] \[[Paranjape and Chung 2010][research_paranjape_chung_2010]\] \[[Paranjape et al 2011][research_paranjape_chung_2011]\] \[[Park et al 2015][research_park_ocheltree_2015]\] \[[Park et al 2016][research_park_choi_2016]\] \[[Park et al 2016][research_park_jo_2016]\] \[[Park et al 2017][research_park_choi_2017]\] \[[Park et al 2017][research_park_jo_2017]\] \[[Paul et al 1997][research_paul_garrard_1997]\] \[[Pena and Voulgaris 2001][research_pena_voulgaris_2001]\] \[[Pepelea et al 2016][research_pepelea_cojocaru_2016]\] \[[Petrenko and Gašparovič 2025][research_petrenko_gasparovic_2025]\] \[[Phillips et al 2019][research_phillips_jentzsch_2019]\] \[[Protz and Sparks 1998][research_protz_sparks_1998]\] \[[Qu et al 2011][research_qu_li_2011]\] \[[Rajput et al 2015][research_rajput_zhangweiguo_2015]\] \[[Reist and Zingg 2015][research_reist_zingg_2015]\] \[[Reist and Zingg 2016][research_reist_zingg_2016]\] \[[Riethausen 2026][research_riethausen_2026]\] \[[Rojas Carvajal and Amitay 2023][research_rojascarvajal_amitay_2023]\] \[[Rossetti and Beblo 2022][research_rossetti_beblo_2022]\] \[[Sudhakar et al 2025][research_s_c_2025]\] \[[Saeed and Graham 2015][research_saeed_graham_2015]\] \[[Saephan and van Dam 2006][research_saephan_vandam_2006_b]\] \[[Saephan and van Dam 2006][research_saephan_vandam_2006]\] \[[Seacord and Campbell 1945][research_seacordcharlesl_campbelljohnp_1945]\] \[[Shayan and Van Kampen 2021][research_shayan_vankampen_2021]\] \[[Shearwood et al 2019][research_shearwood_nabawy_2019]\] \[[Shi and Wu 2022][research_shi_wu_2022]\] \[[Shtessel et al 1999][research_shtessel_buffington_1999]\] \[[Shtessel et al 2002][research_shtessel_buffington_2002]\] \[[Shuang et al 2016][research_shuang_zhang_2016]\] \[[Simon et al 1993][research_simon_blake_1993]\] \[[Song et al 2016][research_song_yang_2016]\] \[[Sparks][research_sparks]\] \[[Sparks and Sparks 1997][research_sparks_sparks_1997]\] \[[Stenfelt and Ringertz 2009][research_stenfelt_ringertz_2009]\] \[[Stenfelt and Ringertz 2010][research_stenfelt_ringertz_2010]\] \[[Stenfelt and Ringertz 2013][research_stenfelt_ringertz_2013]\] \[[Tal and Karaman 2021][research_tal_karaman_2021]\] \[[Tal and Karaman 2022][research_tal_karaman_2022]\] \[[Teel 1999][research_teel_1999]\] \[[Teel 1999][research_teel_1999_b]\] \[[Tipton and Smith 1995][research_tipton_smith_1995]\] \[[Tipton et al 1996][research_tipton_smith_1996]\] \[[Tournes and Johnson 1999][research_tournes_johnson_1999]\] \[[Tournes et al 1997][research_tournes_shtessel_1997]\] \[[Traas et al 2026][research_traas_atmaca_2026]\] \[[Vale J 2013][research_valej_2013]\] \[[van den Aarssen et al 2019][research_vandenaarssen_visser_2019]\] \[[Veismann et al 2023][research_veismann_gharib_2023]\] \[[Vicroy et al 2018][research_vicroy_huber_2018]\] \[[Vos et al 2002][research_vos_brown_2002]\] \[[Wang and Qi 2021][research_wang_qi_2021]\] \[[Wang et al 2020][research_wang_tang_2020]\] \[[Wang et al 2023][research_wang_hu_2023]\] \[[Wang et al 2025][research_wang_luo_2025]\] \[[Weil 1981][research_weilj_1981]\] \[[Wells and Hess 2002][research_wells_hess_2002]\] \[[Wells and Hess 2003][research_wells_hess_2003]\] \[[Weyl 1944][research_weyl_1944]\] \[[Weyl 1945][research_weyl_1945]\] \[[Weyl 1945][research_weyl_1945_b]\] \[[Weyl 1945][research_weyl_1945_c]\] \[[Weyl 1945][research_weyl_1945_e]\] \[[Weyl 1945][research_weyl_1945_d]\] \[[White and Innis 1959][research_whitemauriced_innisrobertc_1959]\] \[[Williams et al 2025][research_williams_niestroy_2025]\] \[[Wise et al 1999][research_wise_brinker_1999]\] \[[Xi and Zhao 2017][research_xi_zhao_2017]\] \[[Xie et al 2011][research_xie_yang_2011]\] \[[Xin et al 2024][research_xin_chen_2024]\] \[[Xu and Feng 2025][research_xu_feng_2025]\] \[[Xu and Yu 2025][research_xu_yu_2025]\] \[[Xu and Zhou 2015][research_xu_zhou_2015]\] \[[Yazdi et al 2026][research_yazdi_gray_2026]\] \[[Yazdi et al 2026][research_yazdi_reist_2026]\] \[[Yu et al 2022][research_yu_li_2022]\] \[[Yu et al 2023][research_yu_li_2023]\] \[[Yu et al 2023][research_yu_li_2023_b]\] \[[Yu et al 2023][research_yu_li_2023_c]\] \[[Yue et al 2009][research_yue_wang_2009]\] \[[Yue et al 2013][research_yue_wang_2013]\] \[[Yuzawa and Ogami 2002][research_yuzawa_ogami_2002]\] \[[Zhang and He 2026][research_zhang_he_2026]\] \[[Zhang and He 2026][research_zhang_he_2026_b]\] \[[Zhang and Meng 2019][research_zhang_meng_2019]\] \[[Zhang et al 2018][research_zhang_shuang_2018]\] \[[Zhang et al 2023][research_zhang_huang_2023]\] \[[Zhang et al 2024][research_zhang_liu_2024]\] \[[Zhao et al 2023][research_zhao_luo_2023]\] \[[Zhu et al 2016][research_zhu_gao_2016]\] \[[Zhu et al 2022][research_zhu_shi_2022]\] \[[Zou et al 2026][research_zou_zhen_2026]\]

**Of the 214 records, 11 date from 1950 or earlier and 130 from 2015 or later.**

### Flight control law design and fly-by-wire systems

Flight control law design and fly-by-wire flight control systems, their redundancy, actuation and robustness.

**204 records.** \[[213 Development of a robust flight control law for a VSTOL aircraft 1994][research_213_development_1994]\] \[[A multi microprocessor flight control system design principles 1979][research_a_multi_1979]\] \[[A Novel Sliding Mode Controller for Underactuated Vertical Takeoff and Landing Aircraft 2020][research_a_novel_2020]\] \[[Ackerman et al 2019][research_ackerman_gregory_2019]\] \[[Akbari and Greeff 2024][research_akbari_greeff_2024]\] \[[Akmeliawati and Mareels 1999][research_akmeliawati_mareels_1999]\] \[[Aldosari and Feron 2025][research_aldosari_feron_2025]\] \[[Allen et al 2002][research_allenmichaelj_ryanjack_2002]\] \[[Amato et al 2022][research_amato_cortigiani_2022]\] \[[Automatic Landing 1964][research_automatic_landing_1964]\] \[[Barret and Barret 1997][research_barret_barret_1997]\] \[[Beasley 1984][research_beasleygp_1984]\] \[[Belmont 1983][research_belmont_1983]\] \[[Berg 1991][research_berg_1991]\] \[[Bodur and Ucun 2023][research_bodur_ucun_2023]\] \[[Bolting et al 2017][research_bolting_stolle_2017]\] \[[Bosch and Kuehl 1976][research_bosch_kuehl_1976]\] \[[Bosch and Kuehl 1977][research_bosch_kuehl_1977]\] \[[Bouzid et al 2018][research_bouzid_bestaoui_2018]\] \[[Burris 1969][research_burris_1969]\] \[[Burris and Bender 1969][research_burris_bender_1969]\] \[[Burton and Kneeland 1981][research_burton_kneelandjr_1981]\] \[[Carino et al 2015][research_carino_abaunza_2015]\] \[[Carpenter and Jenny 1964][research_carpenter_jenny_1964]\] \[[Caverly and Forbes 2018][research_caverly_forbes_2018]\] \[[Chakravarty 1987][research_chakravarty_1987]\] \[[Chen and Zhao 2017][research_chen_zhao_2017]\] \[[Cheng and Xin 2019][research_cheng_xin_2019]\] \[[Chu and Bryson 1987][research_chu_brysonjr_1987]\] \[[Chunrong and Yunhong 2025][research_chunrong_yunhong_2025]\] \[[Cliff and Lutze 1972][research_cliff_lutze_1972]\] \[[Colgren and Martin 2000][research_colgren_martin_2000]\] \[[Combined flight control/utility system 1974][research_combined_flight_1974]\] \[[Comer et al 2026][research_comer_chakraborty_2026]\] \[[Cotton 1974][research_cotton_1974]\] \[[Cox and Cotting 2005][research_coxtimothyh_cottingmchristopher_2005]\] \[[Craig 1965][research_craig_1965]\] \[[Czyba and Blachuta 2001][research_czyba_blachuta_2001]\] \[[Czyba and Blachuta 2003][research_czyba_blachuta_2003]\] \[[Czyba and Stajer 2019][research_czyba_stajer_2019]\] \[[de Oca and Flores 2020][research_deoca_flores_2020]\] \[[Demarchi and Haning 1978][research_demarchi_haning_1978]\] \[[Digital model-reference flight control of aircraft with unstable sampling zeros 1994][research_digital_model_reference_1994]\] \[[Dobos-Bubno and Hartsook 1977][research_dobosbubno_hartsook_1977]\] \[[Du 2024][research_du_2024]\] \[[Dukes 1970][research_dukes_1970]\] \[[Duran 2026][research_duran_2026]\] \[[Duran et al 2019][research_duran_whidborne_2019]\] \[[Ebner and Mark 1977][research_ebner_mark_1977]\] \[[Enns 2003][research_enns_2003]\] \[[Forkun et al 2020][research_forkun_medzatyi_2020]\] \[[Fosdick 1970][research_fosdick_1970]\] \[[Franklin et al 1985][research_franklin_hynes_1985]\] \[[Friedland 1982][research_friedland_1982]\] \[[Fujimori and Nikiforuk 1999][research_fujimori_nikiforuk_1999]\] \[[Fujimori et al 1997][research_fujimori_wu_1997]\] \[[Fujimori et al 1998][research_fujimori_wu_1998]\] \[[Funk 1975][research_funk_1975]\] \[[Gain Scheduled Fuzzy Control on Aircraft Flight Control 2004][research_gain_scheduled_2004]\] \[[Gainer 1963][research_gainer_1963]\] \[[Gaudet and Furfaro 2023][research_gaudet_furfaro_2023]\] \[[Gaylor 1984][research_gaylor_1984]\] \[[Goldberger 1966][research_goldberger_1966]\] \[[Govindaraj et al 1979][research_govindaraj_rynaski_1979]\] \[[Gregory et al 1994][research_gregoryirenem_chowdhryrajivs_1994]\] \[[Grossman 1957][research_grossman_1957]\] \[[Guerrero-Bonilla et al 2017][research_guerrerobonilla_mohta_2017]\] \[[Guo 2021][research_guo_2021]\] \[[Guy 1976][research_guy_1976]\] \[[Harris and Rickard 1979][research_harris_rickard_1979]\] \[[Hart 1956][research_hart_1956]\] \[[Hart 1968][research_hart_1968]\] \[[Henn and Boronow 1959][research_henn_boronow_1959]\] \[[Herrmann and Ben-Asher 2016][research_herrmann_benasher_2016]\] \[[Hess and Peng 2018][research_hess_peng_2018]\] \[[Hill 1987][research_hill_1987]\] \[[Hogan and Rinde 1978][research_hogan_rinde_1978]\] \[[Hongyan and Xiaoyong 2026][research_hongyan_xiaoyong_2026]\] \[[Hueschen 1984][research_hueschenrm_1984]\] \[[Hübener and Luckner 2026][research_hubener_luckner_2026]\] \[[Inertially augmented approach and landing systems 1971][research_inertially_augmented_1971]\] \[[Stewart 1992][research_jamesfstewart_1992]\] \[[Stewart et al 1992][research_jamesfstewart_frankwburchamjr_1992]\] \[[Jeffrie and Rolston 1972][research_jeffrie_rolston_1972]\] \[[Jenney 1979][research_jenney_1979]\] \[[Jenney 1980][research_jenney_1980]\] \[[Jenney et al 1982][research_jenney_schreadley_1982]\] \[[Jianhong and Yanxiang 2026][research_jianhong_yanxiang_2026]\] \[[Jianliang Wang and Sundararajan 1994][research_jianliangwang_sundararajan_1994]\] \[[Kanai and Nikiforuk 1982][research_kanai_nikiforuk_1982]\] \[[Kazarin et al 2016][research_kazarin_golubev_2016]\] \[[Khamvilai et al 2024][research_khamvilai_huang_2024]\] \[[Kisslinger and Wendl 1971][research_kisslinger_wendl_1971]\] \[[Kistyarev and Wang 2025][research_kistyarev_wang_2025]\] \[[Kohlman and Brainerd 1974][research_kohlman_brainerd_1974]\] \[[Kohnhorst and Magnacca 1980][research_kohnhorst_magnacca_1980]\] \[[Konar et al 1974][research_konar_mahesh_1974]\] \[[Kouvaritakis et al 1979][research_kouvaritakis_murray_1979]\] \[[Kuchar and Looye 2018][research_kuchar_looye_2018]\] \[[Kus and Ergazi 2025][research_kus_ergazi_2025]\] \[[Larson 1986][research_larson_1986]\] \[[Lateral Control of a Hypersonic Aircraft 2025][research_lateral_control_2025]\] \[[Lavretsky 2019][research_lavretsky_2019]\] \[[Lee and Hedrick 1994][research_lee_hedrick_1994]\] \[[Lee et al 2001][research_lee_shin_2001]\] \[[Liang 2025][research_liang_2025]\] \[[Liu et al 2018][research_liu_nakata_2018]\] \[[Liu et al 2023][research_liu_hao_2023]\] \[[Liu et al 2024][research_liu_hao_2024]\] \[[Lorenzetti et al 1969][research_lorenzetti_nelsen_1969]\] \[[Lu and Martos 2021][research_lu_martos_2021]\] \[[Ma 2019][research_ma_2019]\] \[[Mao et al 2022][research_mao_gong_2022]\] \[[Martorella et al 1981][research_martorella_kelly_1981]\] \[[Masaoka and Hashimoto 2024][research_masaoka_hashimoto_2024]\] \[[Masubuchi et al 2004][research_masubuchi_kato_2004]\] \[[Mattern et al 1989][research_matternduane_gargsanjay_1989]\] \[[McDonald and Farris 1964][research_mcdonald_farris_1964]\] \[[McGough et al 1974][research_mcgough_moses_1974]\] \[[McKenzie 1973][research_mckenzie_1973]\] \[[McMaster and Schenk 1974][research_mcmaster_schenk_1974]\] \[[Melekhin and Khachumov 2021][research_melekhin_khachumov_2021]\] \[[Mineck 1976][research_mineck_1976]\] \[[Mohamed 2024][research_mohamed_2024]\] \[[Mueller 1965][research_mueller_1965]\] \[[Muir 1993][research_muir_1993]\] \[[Muir and Bradshaw 1996][research_muir_bradshaw_1996]\] \[[Muller 1967][research_muller_1967]\] \[[Muravyev 2022][research_muravyev_2022]\] \[[Napolitano et al 1998][research_napolitano_windon_1998]\] \[[Nardi 1970][research_nardi_1970]\] \[[Neal and Smith 1970][research_neal_smith_1970]\] \[[Negre 1975][research_negre_1975]\] \[[Nguyen and Tran 2021][research_nguyen_tran_2021]\] \[[Nield 1981][research_nield_iv_1981]\] \[[Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]\] \[[Ogren et al 1974][research_ogren_sotanski_1974]\] \[[Onken and Stuckenberg 1978][research_onken_stuckenberg_1978]\] \[[Oosterom et al 2000][research_oosterom_schram_2000]\] \[[Oosterom et al 2002][research_oosterom_bergsten_2002]\] \[[Ossmann et al 2019][research_ossmann_luspay_2019]\] \[[Ostheimer and Giguere 1963][research_ostheimer_giguere_1963]\] \[[Patience and Nahon 2020][research_patience_nahon_2020]\] \[[Payne 1968][research_payne_1968]\] \[[Peng et al 2018][research_peng_lin_2018]\] \[[Petrie 1968][research_petrie_1968]\] \[[Porter and Swaim 1975][research_portermbjr_swaimrl_1975]\] \[[Posingies 1979][research_posingies_1979]\] \[[Qian et al 2025][research_qian_xinhui_2025]\] \[[Rabenberg and Palarz 1983][research_rabenberg_palarz_1983]\] \[[Research and Design of Automatic Flight Control System Test System 2022][research_research_and_2022_b]\] \[[Rickard 1978][research_rickard_1978]\] \[[Robinson 1968][research_robinson_1968]\] \[[Robinson 1969][research_robinson_1969]\] \[[Rogalski 2018][research_rogalski_2018]\] \[[Rogalski et al 2020][research_rogalski_rzucidlo_2020]\] \[[Rogalski et al 2021][research_rogalski_rzucidlo_2021]\] \[[Rosa and Belo 2021][research_rosa_belo_2021]\] \[[Rynaski 1994][research_rynaski_1994]\] \[[Schierman and Schmidt 1991][research_schiermanjohnd_schmidtdavidk_1991]\] \[[Schreadley 1977][research_schreadley_1977]\] \[[Scott 1977][research_scott_1977]\] \[[Sedlmair et al 2022][research_sedlmair_theis_2022]\] \[[Servo-control device for aircraft flight control 1984][research_servo_control_device_1984]\] \[[Sklaroff et al 1973][research_sklaroff_kilmer_1973]\] \[[Smith 1991][research_smith_1991]\] \[[Smith and Meyer 1984][research_smith_meyer_1984]\] \[[Smith and Meyer 1987][research_smith_meyer_1987]\] \[[Smith et al 1991][research_smithrh_chisholmjd_1991]\] \[[Snell et al 1990][research_snell_garrardjr_1990]\] \[[Snell et al 1992][research_snell_enns_1992]\] \[[Sobel and Shapiro 1984][research_sobel_shapiro_1984]\] \[[Sparks 2003][research_sparks_2003]\] \[[Stephan et al 2023][research_stephan_stumpf_2023]\] \[[Sugino et al 2019][research_sugino_harada_2019]\] \[[Thompson 1965][research_thompson_1965]\] \[[Thompson and Chiang 1990][research_thompson_chiang_1990]\] \[[Tribuno et al 1976][research_tribuno_klein_1976]\] \[[Venkataraman et al 2017][research_venkataraman_seiler_2017]\] \[[Verma and Junkins 1999][research_verma_junkins_1999]\] \[[Vieten 1992][research_vieten_1992]\] \[[Voting software for fault-tolerant aircraft flight control systems 1993][research_voting_software_1993]\] \[[Wagdi 1984][research_wagdi_1984]\] \[[Walker 1960][research_walker_1960]\] \[[Walker 1961][research_walker_1961]\] \[[Wang et al 2020][research_wang_wu_2020]\] \[[Wang et al 2022][research_wang_zheng_2022]\] \[[Warren 1989][research_warren_1989]\] \[[Watson and Komechak 1977][research_watson_komechak_1977]\] \[[Weiser et al 2020][research_weiser_ossmann_2020]\] \[[Weiser et al 2024][research_weiser_looye_2024]\] \[[Wise et al 1999][research_wise_sedwick_1999]\] \[[Wolf 1978][research_wolf_1978]\] \[[Wu et al 2015][research_wu_li_2015]\] \[[Xiao et al 2018][research_xiao_belt_2018]\] \[[Yang et al 2025][research_yang_zhen_2025]\] \[[Yijie et al 2023][research_yijie_deshuang_2023]\] \[[Yonke et al 1985][research_yonke_terrell_1985]\] \[[Yue et al 2017][research_yue_wang_2017]\] \[[Zhang et al 2017][research_zhang_duan_2017]\] \[[Zhishuai and Lingling 2022][research_zhishuai_lingling_2022]\] \[[Zhou and Deng 2024][research_zhou_deng_2024]\] \[[Zhu and Qin 2023][research_zhu_qin_2023]\] \[[Zipperer et al 1975][research_zipperer_jenney_1975]\]

### Reynolds number effects and low Reynolds number aerodynamics

Reynolds number effects, laminar separation bubbles and the aerodynamics of wings and aerofoils at low Reynolds number.

**202 records.** \[[Adak et al 2024][research_adak_mandal_2024]\] \[[Adeyi et al 2024][research_adeyi_alabi_2024]\] \[[Aditya and Srinivas 2019][research_aditya_srinivas_2019]\] \[[Ahmad and Li 2022][research_ahmad_li_2022]\] \[[Albrecht et al 2019][research_albrecht_naguib_2019]\] \[[Albrecht et al 2022][research_albrecht_olson_2022]\] \[[Alford and Altman 2004][research_alford_altman_2004]\] \[[Algozino et al 2015][research_algozino_maranondileo_2015]\] \[[Anyoji 2019][research_anyoji_2019]\] \[[Aono et al 2018][research_aono_anyoji_2018]\] \[[Arshad et al 2022][research_arshad_nawanjana_2022]\] \[[Ashish Kumar Gupta et al 2023][research_ashishkumargupta_paaswathanarayana_2023]\] \[[Aulehia 1987][research_aulehia_1987]\] \[[Avirovic et al 2023][research_avirovic_brunelli_2023]\] \[[Avirovic et al 2024][research_avirovic_brunelli_2024]\] \[[Badrya and Baeder 2019][research_badrya_baeder_2019]\] \[[Badrya et al 2018][research_badrya_govindarajan_2018]\] \[[Bagade et al 2015][research_bagade_krishnan_2015]\] \[[Balaji et al 2025][research_balaji_mahesh_2025]\] \[[Bansal and Lavoie 2025][research_bansal_lavoie_2025]\] \[[Benny Thompson and Gunasekaran 2021][research_bennythompson_gunasekaran_2021]\] \[[Bernal and Yu 2015][research_bernal_yu_2015]\] \[[Bernardos et al 2019][research_bernardos_richez_2019]\] \[[Boschetti et al 2004][research_boschetti_cardenas_2004]\] \[[Brunelli et al 2026][research_brunelli_avirovic_2026]\] \[[Bucci et al 1997][research_bucci_sullivan_1997]\] \[[Catalano and D'Aniello 2025][research_catalano_daniello_2025]\] \[[Catalano et al 2024][research_catalano_derosa_2024]\] \[[Chandan et al 2023][research_chandan_nagaraja_2023]\] \[[Chandra 2020][research_chandra_2020]\] \[[Chen and Yang 2022][research_chen_yang_2022]\] \[[Chitsaz et al 2021][research_chitsaz_siddiqui_2021]\] \[[Cho et al 2018][research_cho_kim_2018]\] \[[Ciobaca and Dandois 2017][research_ciobaca_dandois_2017]\] \[[Collison et al 2017][research_collison_harley_2017]\] \[[De Almeida and Dias 2024][research_dealmeida_dias_2024]\] \[[de Paula et al 2017][research_depaula_kleine_2017]\] \[[de Rosa et al 2024][research_derosa_catalano_2024]\] \[[Dellacasagrande et al 2020][research_dellacasagrande_barsi_2020]\] \[[Dias Pires de Souza et al 2017][research_diaspiresdesouza_rodriguez_2017]\] \[[Drela 1991][research_drela_1991]\] \[[Drela and Giles 1986][research_drela_giles_1986]\] \[[Durgesh et al 2019][research_durgesh_padilla_2019]\] \[[Dwivedi et al 2022][research_dwivedi_pavithra_2022]\] \[[Désert et al 2019][research_desert_jardin_2019]\] \[[Eftekhari and Al-Obaidi 2019][research_eftekhari_alobaidi_2019]\] \[[Esmaeili et al 2018][research_esmaeili_delgado_2018]\] \[[Evangelista et al 1987][research_evangelista_pfenninger_1987]\] \[[Evans 1964][research_evans_1964]\] \[[Fayaz et al 2022][research_fayaz_fathima_2022]\] \[[Feng et al 2017][research_feng_peng_2017]\] \[[Ferrand et al 2026][research_ferrand_gowree_2026]\] \[[Fujita et al 2019][research_fujita_uechi_2019]\] \[[Geng et al 2018][research_geng_kalkman_2018]\] \[[Genç et al 2022][research_genc_koca_2022]\] \[[Giacomini and Westerberg 2025][research_giacomini_westerberg_2025]\] \[[Gnatowska and Gajewska 2024][research_gnatowska_gajewska_2024]\] \[[Gopalarathnam et al 2001][research_gopalarathnam_broughton_2001]\] \[[Gopalarothnam and McGowan 2008][research_gopalarothnam_mcgowan_2008]\] \[[Greer et al 1999][research_greer_hamory_1999]\] \[[Gungordu and Tayfuner 2026][research_gungordu_tayfuner_2026]\] \[[Gupta et al 2025][research_gupta_aswathanarayana_2025]\] \[[Güler et al 2021][research_guler_durhasan_2021]\] \[[Hall and Kern 1996][research_hall_kern_1996]\] \[[Hammer and Shumway 2026][research_hammer_shumway_2026]\] \[[Hammer and Shumway 2026][research_hammer_shumway_2026_b]\] \[[Hart et al 2016][research_hart_sytsma_2016]\] \[[Herbst et al 2018][research_herbst_kahler_2018]\] \[[Hoxey et al 1997][research_hoxey_robertson_1997]\] \[[Hsiao 1988][research_hsiao_1988]\] \[[Hsiao et al 2004][research_hsiao_wang_2004]\] \[[Ikeda et al 2015][research_ikeda_atobe_2015]\] \[[Inoue et al 2019][research_inoue_yasuda_2019]\] \[[Itsariyapinyo and Sharma 2016][research_itsariyapinyo_sharma_2016]\] \[[Jabbari et al 2021][research_jabbari_esmaeili_2021]\] \[[Jacob et al 2026][research_jacob_stewart_2026]\] \[[Jain et al 2015][research_jain_sitaram_2015]\] \[[Jones et al 2017][research_jones_milholen_2017]\] \[[Joy et al 2016][research_joy_ibrahim_2016]\] \[[Karthikeyan et al 2024][research_karthikeyan_ajay_2024]\] \[[Kase et al 2021][research_kase_fujita_2021]\] \[[Kase et al 2023][research_kase_mizoguchi_2023]\] \[[Khan 2023][research_khan_2023]\] \[[Khan et al 2022][research_khan_iqbal_2022]\] \[[Klose et al 2018][research_klose_jacobs_2018]\] \[[Korkischko and Konrath 2017][research_korkischko_konrath_2017]\] \[[Kouser et al 2024][research_kouser_aliyu_2024]\] \[[Kouser et al 2024][research_kouser_kurtulus_2024]\] \[[Kuester et al 2016][research_kuester_borgoltz_2016]\] \[[Kumar et al 2015][research_kumar_tomar_2015]\] \[[Kumar and Mukherjee 2024][research_kumarg_mukherjee_2024]\] \[[Kumar Gupta et al 2018][research_kumargupta_aaswathanaray_2018]\] \[[Kurtulus 2019][research_kurtulus_2019]\] \[[Kurtulus 2021][research_kurtulus_2021]\] \[[Lee et al 2015][research_lee_kawai_2015]\] \[[Lee et al 2015][research_lee_kawai_2015_b]\] \[[Lee et al 2015][research_lee_nonomura_2015]\] \[[Lee et al 2015][research_lee_nonomura_2015_b]\] \[[Lei et al 2017][research_lei_liu_2017]\] \[[Leung and Redonnet 2022][research_leung_redonnet_2022]\] \[[Li and Liu 2016][research_li_liu_2016]\] \[[Li et al 2022][research_li_gu_2022]\] \[[Li et al 2023][research_li_nagata_2023]\] \[[Liang et al 2022][research_liang_yang_2022]\] \[[Lim et al 2026][research_lim_kurahashi_2026]\] \[[Lin et al 1992][research_lin_robinson_1992]\] \[[Linehan and Mohseni 2016][research_linehan_mohseni_2016]\] \[[Liu and Luo 2022][research_liu_luo_2022]\] \[[Liu and Xiao 2020][research_liu_xiao_2020]\] \[[Liu and Yang 2024][research_liu_yang_2024]\] \[[Liu et al 2021][research_liu_li_2021]\] \[[Liu et al 2024][research_liu_di_2024]\] \[[Mahns and Amitay 2025][research_mahns_amitay_2025]\] \[[Maji et al 2024][research_maji_pandi_2024]\] \[[Malik et al 2018][research_malik_asrar_2018]\] \[[Manar et al 2016][research_manar_cassell_2016]\] \[[Marchman 1987][research_marchman_1987]\] \[[Matías-García et al 2025][research_matiasgarcia_bardera_2025]\] \[[Maughmer and Somers 1987][research_maughmer_somers_1987_b]\] \[[Maughmer et al 2021][research_maughmer_axten_2021]\] \[[Maughmer et al 2023][research_maughmer_axten_2023]\] \[[Meng et al 2015][research_meng_yan_2015]\] \[[Meng et al 2026][research_meng_wang_2026]\] \[[Metkowski et al 2022][research_metkowski_axten_2022]\] \[[Michelsen and Mueller 1987][research_michelsen_mueller_1987]\] \[[Michna and Rogowski 2022][research_michna_rogowski_2022]\] \[[Michna et al 2025][research_michna_sledziewski_2025]\] \[[Mohamed et al 2021][research_mohamed_wood_2021]\] \[[Mohamed Ibren et al 2021][research_mohamedibren_ameldadianneandan_2021]\] \[[Moreschi and Guardone 2024][research_moreschi_guardone_2024]\] \[[Mueller and Torres 2001][research_mueller_torres_2001]\] \[[Muhammed and Virk 2024][research_muhammed_virk_2024]\] \[[Mukohara and Anyoji 2021][research_mukohara_anyoji_2021]\] \[[Munday et al 2015][research_munday_taira_2015]\] \[[Varsha et al 2023][research_nvarsha_deshpande_2023]\] \[[Neuwerth et al 1998][research_neuwerth_peiter_1998]\] \[[Nik Mohd 2017][research_nikmohd_2017]\] \[[Nudson et al 2025][research_nudson_stanfieldbrown_2025]\] \[[Oh and Choi 2018][research_oh_choi_2018]\] \[[Ol 2007][research_ol_2007]\] \[[Pandi and Mittal 2025][research_pandi_mittal_2025]\] \[[Park et al 2019][research_park_shim_2019]\] \[[Parra et al 2026][research_parra_uraldeguinea_2026]\] \[[Passive Flow Control over an Airfoil by Control Rod at Low Reynolds Number 2020][research_passive_flow_2020]\] \[[Pelletier and Mueller 1999][research_pelletier_mueller_1999]\] \[[Peng et al 2016][research_peng_li_2016]\] \[[Peristy et al 2016][research_peristy_perez_2016]\] \[[Perry and Mueller 1986][research_perry_mueller_1986]\] \[[Petrović et al 2016][research_petrovic_sajn_2016]\] \[[Pfenninger and Vemuru 1988][research_pfenninger_vemuru_1988]\] \[[Potter and Whitfield 1957][research_potter_whitfield_1957]\] \[[Poudel et al 2021][research_poudel_yu_2021]\] \[[Priyanka and Sivapragasam 2021][research_priyanka_sivapragasam_2021]\] \[[Rahal and Dutta 2024][research_rahal_dutta_2024]\] \[[Reaser et al 1983][research_reaser_hallissy_1983]\] \[[Reed 1990][research_reed_1990]\] \[[Ren and Zha 2025][research_ren_zha_2025]\] \[[Ren et al 2026][research_ren_ghopa_2026]\] \[[Rist 1996][research_rist_1996]\] \[[Robinson and Wissler 1988][research_robinson_wissler_1988]\] \[[Rocha Ribeiro and Wolf 2025][research_rocharibeiro_wolf_2025]\] \[[Rolston 2001][research_rolston_2001]\] \[[Roy and Mukherjee 2021][research_roy_mukherjee_2021]\] \[[Ruifeng 2015][research_ruifeng_2015]\] \[[Saunders 1996][research_saunders_1996]\] \[[Shah 2017][research_shah_2017]\] \[[Shams et al 2018][research_shams_alishah_2018]\] \[[Somashekar and Immanuel Selwyn Raj 2018][research_somashekar_immanuelselwynraj_2018]\] \[[Sreejith and Sathyabhama 2020][research_sreejith_sathyabhama_2020]\] \[[Steinhoff 2002][research_steinhoff_2002]\] \[[Stremel 1994][research_stremel_1994]\] \[[Sun and Boyd 2004][research_sun_boyd_2004]\] \[[Tamura and Oyama 2019][research_tamura_oyama_2019]\] \[[Tokugawa et al 2026][research_tokugawa_ishida_2026]\] \[[Toppings and Yarusevych 2021][research_toppings_yarusevych_2021]\] \[[Tran 2025][research_tran_2025]\] \[[Traub 2021][research_traub_2021]\] \[[Traub 2024][research_traub_2024_b]\] \[[Traub and Coffman 2019][research_traub_coffman_2019]\] \[[Traub et al 1998][research_traub_moeller_1998]\] \[[Traub et al 2015][research_traub_botero_2015]\] \[[Uthra and Antony 2020][research_uthra_antony_2020]\] \[[Somashekar and Immanuel Selwynraj 2022][research_v_a_2022]\] \[[Verhaagen 1999][research_verhaagen_1999]\] \[[Waldmann et al 2023][research_waldmann_ehrle_2023]\] \[[Wang et al 2021][research_wang_liu_2021]\] \[[White et al 2025][research_white_narsipur_2025]\] \[[Wrist and Hubner 2017][research_wrist_hubner_2017]\] \[[Xi et al 2025][research_xi_dai_2025]\] \[[Xiao et al 2016][research_xiao_li_2016]\] \[[Yamazaki et al 2017][research_yamazaki_yamagishi_2017]\] \[[Yamazaki et al 2018][research_yamazaki_yamagishi_2018]\] \[[Yang and Agarwal 2019][research_yang_agarwal_2019]\] \[[Yang et al 2016][research_yang_meng_2016]\] \[[You et al 2013][research_you_bromby_2013]\] \[[Yu et al 2024][research_yu_hrynuk_2024]\] \[[Zhang et al 2017][research_zhang_liu_2017]\] \[[Zhao et al 2024][research_zhao_wang_2024]\] \[[Zhou et al 2021][research_zhou_zhong_2021]\] \[[Zhu and Guo 2019][research_zhu_guo_2019]\] \[[Zilli et al 2017][research_zilli_sutton_2017]\] \[[Zilstra and Johnson 2026][research_zilstra_johnson_2026]\]

**Of the 202 records, 164 date from 2015 or later**, which is the shape of a literature that grew with the small unmanned aircraft.

### Similitude, dynamic scaling and subscale flight testing

Similitude, dynamic scaling and the subscale and free-flight model testing of aircraft, from the free-spinning tunnel to the radio-controlled research aircraft.

**155 records.** \[[Akaryildiz et al 2024][research_akaryildiz_demirkiran_2024]\] \[[Ananda et al 2017][research_ananda_vahora_2017]\] \[[Anderson et al 1954][research_anderson_flickinger_1954]\] \[[Axelson and Emerson 1949][research_axelsonjohna_emersonhoracef_1949]\] \[[Bantscheff and Breitsamter 2023][research_bantscheff_breitsamter_2023]\] \[[Baumann and Gal-Or 1992][research_baumann_galor_1992]\] \[[Baylen et al 1967][research_baylen_walton_1967]\] \[[Beeman 1972][research_beemanrr_1972]\] \[[Berman 1947][research_bermantheodore_1947]\] \[[Berman 1949][research_bermantheodore_1949]\] \[[Berman and Pumphrey 1950][research_bermantheodore_pumphreynormane_1950]\] \[[Bertrand-Noël et al 2022][research_bertrandnoel_bignaletcazalet_2022]\] \[[Betin 2026][research_betin_2026]\] \[[Bowman 1957][research_bowmanjamessjr_1957]\] \[[Brown and Duhon 1965][research_brown_duhon_1965]\] \[[Bunge et al 2015][research_bunge_munerasavino_2015]\] \[[Burk and Wilson 1975][research_burksmjr_wilsoncfjr_1975]\] \[[Byrdsong and Brooks 1980][research_byrdsong_brooks_1980]\] \[[Byrdsong and Brooks 1983][research_byrdsong_brooks_1983]\] \[[Byrdsong and Hallissy 1979][research_byrdsong_hallissy_1979]\] \[[Chedrik et al 2004][research_chedrik_ishmuratov_2004]\] \[[Comer et al 2024][research_comer_bhandari_2024]\] \[[Comer et al 2026][research_comer_atkinson_2026]\] \[[Comer et al 2026][research_comer_chakraborty_2026_b]\] \[[Courtin et al 2020][research_courtin_hansman_2020]\] \[[Cox et al 2012][research_coxdavide_cunninghamkevin_2012]\] \[[Crites et al 1992][research_crites_rueger_1992]\] \[[Croom et al 2000][research_croom_kenney_2000]\] \[[Cumming and Kramer 1966][research_cumming_kramer_1966]\] \[[Dantsker 2024][research_dantsker_2024]\] \[[Dantsker and Mancuso 2019][research_dantsker_mancuso_2019]\] \[[Dantsker and Selig 2015][research_dantsker_selig_2015]\] \[[Dantsker et al 2022][research_dantsker_haviland_2022]\] \[[Dantsker et al 2023][research_dantsker_haviland_2023]\] \[[DeBoer et al 2026][research_deboer_kimball_2026]\] \[[Deets and Brown 1986][research_deets_brown_1986]\] \[[Degenne et al 1973][research_degenne_verges_1973]\] \[[Denham and Owens 2016][research_denham_owens_2016]\] \[[Doll et al 2024][research_doll_hoogreef_2024]\] \[[Eilertson 1975][research_eilertson_1975]\] \[[Ericsson 1985][research_ericsson_1985]\] \[[Ericsson 1985][research_ericsson_1985_b]\] \[[Fitzgerald and Gingras 1996][research_fitzgerald_gingras_1996]\] \[[Foster et al 2020][research_foster_miller_2020]\] \[[Fratello and Shearin 1975][research_fratello_shearin_1975]\] \[[Fremaux 1995][research_fremaux_1995]\] \[[Gee 1978][research_geesw_1978]\] \[[Genito et al 2024][research_genito_garbarino_2024]\] \[[Geuther et al 2024][research_geuther_ackerman_2024]\] \[[Ghanchi and Gururajan 2026][research_ghanchi_gururajan_2026]\] \[[Gingrich et al 1977][research_gingrich_child_1977]\] \[[Grafton et al 1974][research_graftonsb_chambersjr_1974]\] \[[Gray 1964][research_gray_1964]\] \[[Guo et al 2017][research_guo_zhu_2017]\] \[[Hakim and Choukri 2023][research_hakim_choukri_2023]\] \[[Hammer et al 2026][research_hammer_degraaf_2026]\] \[[Hastedt et al 2022][research_hastedt_theis_2022]\] \[[Head 1962][research_head_1962]\] \[[Healy 1958][research_healyfrederickm_1958]\] \[[Hitzel and Zimper 2018][research_hitzel_zimper_2018]\] \[[Hoe et al 2012][research_hoegarrison_owensdonaldb_2012]\] \[[Holmes and Woehr 1971][research_holmes_woehr_1971]\] \[[Howard and Bray 1992][research_howard_bray_1992]\] \[[Hwang et al 2024][research_hwang_yoo_2024]\] \[[Hyde and Massie 1993][research_hydecharlesr_massiejeffreyj_1993]\] \[[Harasani 2015][research_iharasani_2015]\] \[[Iliff 1980][research_iliff_1980]\] \[[Jaffe 1972][research_jaffe_1972]\] \[[Jayaraman et al 2022][research_jayaraman_gaurav_2022]\] \[[Johnson 1949][research_johnsonjosephl_1949]\] \[[Jordan et al 2004][research_jordanthomas_langfordwilliam_2004]\] \[[Jordan et al 2005][research_jordanthomasl_langfordwilliamm_2005]\] \[[Chambers 1988][research_josephrchambers_1988]\] \[[Keller et al 2026][research_keller_mckillipjr_2026]\] \[[Klinar and Healy 1955][research_klinarwalterj_healyfrederickm_1955]\] \[[Kotsabasis 1981][research_kotsabasis_1981]\] \[[Krause et al 2024][research_krause_funke_2024]\] \[[Kunwar and Chakraborty 2025][research_kunwar_chakraborty_2025]\] \[[Kunwar et al 2026][research_kunwar_putra_2026]\] \[[Laiosa 1985][research_laiosa_1985]\] \[[Lallemand 2000][research_lallemand_2000]\] \[[Larsen 1975][research_larsen_1975]\] \[[Larsson 2025][research_larsson_2025]\] \[[Laughter 2012][research_laughterseana_2012]\] \[[Layton 1974][research_laytongp_1974]\] \[[Lee 1952][research_leehenrya_1952]\] \[[Lee 1963][research_leehenrya_1963]\] \[[Lockenour and Layton 1976][research_lockenour_layton_1976]\] \[[Long 1968][research_long_1968]\] \[[Lorincz 1980][research_lorincz_1980]\] \[[Lovell 1954][research_lovellpowellmjr_1954]\] \[[Lu et al 2015][research_lu_zhang_2015]\] \[[Lu et al 2016][research_lu_zhang_2016]\] \[[Lu et al 2019][research_lu_zhang_2019]\] \[[MacAllister 1955][research_macallister_1955]\] \[[Mandal and Gu 2016][research_mandal_gu_2016]\] \[[McClinton et al 1998][research_mcclinton_voland_1998]\] \[[Mineck et al 1976][research_mineckre_freemancr_1976]\] \[[Motter and High 2009][research_mottermarka_highjamesw_2009]\] \[[Murri et al 1984][research_murridg_nguyenlt_1984]\] \[[Nagel and Thomas 1965][research_nagel_thomas_1965]\] \[[Napolitano 2002][research_napolitano_2002]\] \[[Nepomuceno and Annes Da Silva 2021][research_nepomuceno_annesdasilva_2021]\] \[[Nepomuceno et al 2022][research_nepomuceno_fischer_2022]\] \[[Obermark 2004][research_obermark_2004]\] \[[Oblique Wing Remotely Piloted 1974][research_oblique_wing_1974]\] \[[Olejnik et al 2019][research_olejnik_kachel_2019]\] \[[Olejnik et al 2022][research_olejnik_rogolski_2022]\] \[[Owens et al 2006][research_owensdonaldb_coxdavide_2006]\] \[[Pallister et al 1992][research_pallister_parker_1992]\] \[[Pan et al 2025][research_pan_ma_2025]\] \[[Pan et al 2026][research_pan_mao_2026]\] \[[Park et al 2025][research_park_yang_2025]\] \[[Petersen 1976][research_petersen_1976]\] \[[Petersen 1976][research_petersen_1976_b]\] \[[Peterson et al 2016][research_peterson_sarigulklijn_2016]\] \[[Pieper et al 2018][research_pieper_perry_2018]\] \[[Platou 1968][research_platou_1968]\] \[[Pusztai et al 2024][research_pusztai_lowenberg_2024]\] \[[Raju Kulkarni et al 2019][research_rajukulkarni_larocca_2019]\] \[[Rayleigh 1915][research_rayleigh_1915]\] \[[Reed 1974][research_reed_1974]\] \[[Richardson 1976][research_richardson_1976]\] \[[Ruan and Aagren 2025][research_ruan_aagren_2025]\] \[[Sadovnitchii et al 1997][research_sadovnitchii_ryabkov_1997]\] \[[Sadovnychiy et al 1998][research_sadovnychiy_betin_1998]\] \[[Sakata 2002][research_sakata_2002]\] \[[Burk and Libbey 1961][research_sangermburkjr_charleselibbey_1961]\] \[[Sarker et al 2026][research_sarker_pudasaini_2026]\] \[[Silvers et al 1958][research_silvershnorman_fournierrogerh_1958]\] \[[Simmons and Ackerman 2026][research_simmons_ackerman_2026]\] \[[Simon et al 2023][research_simon_williams_2023]\] \[[Simon et al 2024][research_simon_williams_2024]\] \[[Sobron et al 2021][research_sobron_lundstrom_2021]\] \[[Solies 1994][research_solies_1994]\] \[[Spurlin and Lueck 1984][research_spurlin_lueck_1984]\] \[[Stephens 1931][research_stephens_1931]\] \[[Tai et al 2026][research_tai_wang_2026]\] \[[Tenhave et al 2026][research_tenhave_joiner_2026]\] \[[Traub 2024][research_traub_2024]\] \[[Tsushima et al 2024][research_tsushima_saitoh_2024]\] \[[Uppoor et al 2026][research_uppoor_chopra_2026]\] \[[Vigh 1977][research_vigh_1977]\] \[[Wang et al 2019][research_wang_zuo_2019]\] \[[Wang et al 2020][research_wang_zhang_2020]\] \[[Ward et al 2025][research_ward_ho_2025]\] \[[Ward et al 2026][research_ward_collins_2026]\] \[[Weiland 2021][research_weiland_2021]\] \[[Winchenbach et al 1982][research_winchenbach_chelekis_1982]\] \[[Winchenbach et al 1984][research_winchenbach_uselton_1984]\] \[[Wolowicz et al 1979][research_wolowiczch_brownjsjr_1979]\] \[[Yarlett et al 2000][research_yarlett_adrezin_2000]\] \[[Yip et al 1990][research_yip_fratello_1990]\] \[[Yip et al 1990][research_yip_fratello_1990_b]\] \[[Yip et al 1991][research_yip_fratello_1991]\]

**Of the 155 records, 73 date from 1997 or earlier**, the free-spinning and free-flight model tradition the X-36 descends from, and 66 from 2015 or later.

### Wing and configuration aerodynamics

The aerodynamics of wings, fuselages and complete configurations, and the estimation of aerodynamic coefficients for design.

**155 records.** \[[Abu Salem et al 2023][research_abusalem_palaia_2023]\] \[[Addoms 1977][research_addoms_1977]\] \[[Adiwidodo and Wijaya 2022][research_adiwidodo_wijaya_2022]\] \[[AERODYNAMIC ANALYSIS OF EAGLE WINGLETS ON AIRCRAFT 2017][research_aerodynamic_analysis_2017]\] \[[Aerodynamic Performance of Swayasa Aircraft Wing Model against the Effect of Airfoil Flap Angle Configuration 2025][research_aerodynamic_performance_2025]\] \[[Aircraft design optimization with multidisciplinary performance criteria 1989][research_aircraft_design_1989]\] \[[Akgumus Gok 2024][research_akgumusgok_2024]\] \[[Aleisa et al 2023][research_aleisa_kontis_2023]\] \[[Ali et al 2024][research_ali_rasani_2024]\] \[[Allen 2017][research_allen_2017]\] \[[Aprovitola et al 2021][research_aprovitola_dinuzzo_2021]\] \[[Aryasomayajula et al 2001][research_aryasomayajula_wang_2001]\] \[[Asztalos et al 2025][research_asztalos_salucci_2025]\] \[[Ban et al 2018][research_ban_yamazaki_2018]\] \[[Bissonnette and Bramesfeld 2015][research_bissonnette_bramesfeld_2015]\] \[[Black 1968][research_black_1968_b]\] \[[Boschetti et al 2020][research_boschetti_cardenas_2020]\] \[[Boschetti et al 2022][research_boschetti_neves_2022]\] \[[Bosnyakov et al 2024][research_bosnyakov_wolkov_2024]\] \[[Bui 2018][research_bui_2018]\] \[[Bushnell 1990][research_bushnell_1990]\] \[[Caap and Elemeland 1986][research_caap_elemeland_1986]\] \[[Casadei et al 2019][research_casadei_konozsy_2019]\] \[[Cavallo and Dash 2000][research_cavallo_dash_2000]\] \[[Chau and Zingg 2017][research_chau_zingg_2017]\] \[[Chau and Zingg 2022][research_chau_zingg_2022]\] \[[Chau et al 2026][research_chau_piotrowski_2026]\] \[[Chen et al 2025][research_chen_li_2025]\] \[[Coder and Ortiz-Melendez 2018][research_coder_ortizmelendez_2018]\] \[[Cui et al 2019][research_cui_feng_2019]\] \[[Cummings et al 2018][research_cummings_liersch_2018]\] \[[Czyz and Karpinski 2020][research_czyz_karpinski_2020]\] \[[de Vries and Vos 2023][research_devries_vos_2023]\] \[[Deere et al 2017][research_deere_viken_2017]\] \[[Della Corte et al 2021][research_dellacorte_vansluis_2021]\] \[[Della Corte et al 2022][research_dellacorte_vansluis_2022]\] \[[Deng et al 2017][research_deng_qu_2017]\] \[[Dickinson 1953][research_dickinson_1953]\] \[[Dizdarevic and Dizdarevic 2022][research_dizdarevic_dizdarevic_2022]\] \[[Dovi and Wrenn 1989][research_dovi_wrenn_1989]\] \[[Duong Nguyen et al 2022][research_duongnguyen_kashitani_2022]\] \[[Durston and Stonum 1987][research_durston_stonum_1987]\] \[[Erhard et al 2021][research_erhard_clarke_2021]\] \[[Evans et al 1949][research_evans_galow_1949]\] \[[Filippoli et al 2026][research_filippoli_perri_2026_b]\] \[[Gagnon and Zingg 2016][research_gagnon_zingg_2016]\] \[[Gallay and Laurendeau 2016][research_gallay_laurendeau_2016]\] \[[Gardner and Downey 1950][research_gardner_downey_1950]\] \[[Gerhardt and Chen 1978][research_gerhardtha_chenws_1978]\] \[[Ghasemzadeh and Banazadeh 2025][research_ghasemzadeh_banazadeh_2025]\] \[[Goerttler 2025][research_goerttler_2025]\] \[[Gopalarathnam and McAvoy 2002][research_gopalarathnam_mcavoy_2002]\] \[[Goparaju et al 2015][research_goparaju_gaitonde_2015]\] \[[Grauer and Morelli 2015][research_grauer_morelli_2015_b]\] \[[Xuan and Cheng 2016][research_h_s_2016]\] \[[Hall et al 1999][research_halljr_perkins_1999]\] \[[Hantla and Wang 2025][research_hantla_wang_2025]\] \[[Harry and Trobaugh 1966][research_harry_trobaugh_1966]\] \[[Hassan et al 1997][research_hassan_janakiram_1997]\] \[[Huntley et al 2019][research_huntley_woods_2019]\] \[[Ishikawa and Yamazaki 2021][research_ishikawa_yamazaki_2021]\] \[[Ito et al 2017][research_ito_murayama_2017]\] \[[Jaffrezic et al 2015][research_jaffrezic_ruetten_2015]\] \[[Jentys and Breitsamter 2023][research_jentys_breitsamter_2023]\] \[[Jesudasan et al 2026][research_jesudasan_doherty_2026]\] \[[Jin et al 2020][research_jin_liao_2020]\] \[[Jones 1979][research_jonesrt_1979]\] \[[Kamiyama and Yamazaki 2020][research_kamiyama_yamazaki_2020]\] \[[Katz 2017][research_katz_2017]\] \[[Kaygan and Ulusoy 2018][research_kaygan_ulusoy_2018]\] \[[Keshmiri et al 2017][research_keshmiri_lan_2017]\] \[[Kim et al 2022][research_kim_sohn_2022]\] \[[Konishi et al 2023][research_konishi_kojima_2023]\] \[[Kästner et al 2021][research_kastner_epple_2021]\] \[[Lam and Stollenwerk 1966][research_lam_stollenwerk_1966]\] \[[Lee 2016][research_lee_2016]\] \[[Lee and Ko 2018][research_lee_ko_2018]\] \[[Lee et al 2024][research_lee_tai_2024]\] \[[Li et al 2019][research_li_zhang_2019]\] \[[Li et al 2022][research_li_bai_2022]\] \[[Li et al 2024][research_li_zheng_2024]\] \[[Liu et al 2020][research_liu_shan_2020]\] \[[Liu et al 2024][research_liu_lu_2024]\] \[[Lucas 1978][research_lucas_1978]\] \[[Luckring et al 1989][research_luckringjamesm_foxcharleshjr_1989]\] \[[Ma 2025][research_ma_2025]\] \[[Mahesh et al 2023][research_mahesh_shah_2023]\] \[[Mahgoub and Cortelezzi 2020][research_mahgoub_cortelezzi_2020]\] \[[Makgantai et al 2021][research_makgantai_subaschandar_2021]\] \[[Mason 1991][research_mason_1991]\] \[[Matos and Marta 2025][research_matos_marta_2025]\] \[[McInville and Moore 1994][research_mcinville_moore_1994]\] \[[Mestriner et al 2018][research_mestriner_desouza_2018]\] \[[Morra and Nicolosi 2025][research_morra_nicolosi_2025]\] \[[Moëns 2022][research_moens_2022]\] \[[Murugappa and Kazerani 2025][research_murugappa_kazerani_2025]\] \[[Nasuhbeyoglu and Akça 2024][research_nasuhbeyoglu_akca_2024]\] \[[Navaratna and Pontillo 2022][research_navaratna_pontillo_2022]\] \[[Neuwerth et al 1999][research_neuwerth_peiter_1999]\] \[[Nguyen et al 2016][research_nguyen_reynolds_2016]\] \[[Nguyen et al 2018][research_nguyen_reynolds_2018]\] \[[Odendaal et al 2024][research_odendaal_smith_2024]\] \[[Okolo et al 2015][research_okolo_dogan_2015]\] \[[Olson and Selberg 1976][research_olson_selberg_1976]\] \[[Parlange 1968][research_parlange_1968]\] \[[Paulson et al 1979][research_paulsonjwjr_thomasjl_1979]\] \[[Peng et al 2019][research_peng_chen_2019]\] \[[Ptitsin 2017][research_ptitsin_2017]\] \[[Rakshith et al 2015][research_rakshith_deshpande_2015]\] \[[Reel and Baltadjiev 2018][research_reel_baltadjiev_2018]\] \[[Reinbold et al 2026][research_reinbold_breitsamter_2026]\] \[[Reist and Zingg 2017][research_reist_zingg_2017]\] \[[Reist et al 2022][research_reist_koo_2022]\] \[[Ren et al 2022][research_ren_su_2022]\] \[[Reuther and Jameson 1995][research_reuther_jameson_1995]\] \[[Ribeiro and Resende 1993][research_ribeiro_deresende_1993]\] \[[Rios and Tamayo 2017][research_rios_tamayo_2017]\] \[[Rivers et al 2001][research_rivers_wahls_2001]\] \[[Rohani and Jahangirian 2022][research_rohani_jahangirian_2022]\] \[[Rong 2026][research_rong_2026]\] \[[Rs et al 2018][research_rs_a_2018]\] \[[Sabo and Bugaj 2021][research_sabo_bugaj_2021]\] \[[Samoylovitch and Strelets 2000][research_samoylovitch_strelets_2000]\] \[[Shahjahan et al 2026][research_shahjahan_enriquez_2026]\] \[[Simon et al 2025][research_simon_zekry_2025]\] \[[Sinha 2004][research_sinha_2004]\] \[[Sirbaugh 1983][research_sirbaugh_1983]\] \[[Sluis et al 2023][research_sluis_dellacorte_2023]\] \[[Smith et al 1992][research_smith_garland_1992]\] \[[Soinne 1999][research_soinne_1999]\] \[[Stoldt et al 2020][research_stoldt_johansen_2020]\] \[[Sundaram and Wu 1983][research_sundaram_wu_1983]\] \[[Takarics et al 2020][research_takarics_mocsanyi_2020]\] \[[Terry 1964][research_terry_1964]\] \[[Tu 1992][research_tu_1992]\] \[[Uribe et al 2017][research_uribe_marty_2017]\] \[[Utsumi 2025][research_utsumi_2025]\] \[[van Rooij and Cummings 2018][research_vanrooij_cummings_2018]\] \[[van Sluis et al 2026][research_vansluis_sinnige_2026]\] \[[Veresnikov and Goncharenko 2025][research_veresnikov_goncharenko_2025]\] \[[Wang et al 2018][research_wang_song_2018]\] \[[Weisshaar 1977][research_weisshaar_1977]\] \[[Wendorff et al 2016][research_wendorff_alonso_2016]\] \[[Whoric 1974][research_whoric_1974]\] \[[Wood 2003][research_wood_2003]\] \[[Wu 1981][research_wu_1981]\] \[[Wu and Sankar 1980][research_wu_sankar_1980]\] \[[Yang 2024][research_yang_2024_b]\] \[[Yoo and Duensing 2019][research_yoo_duensing_2019]\] \[[Yu 2021][research_yu_2021]\] \[[Yuan 2026][research_yuan_2026]\] \[[Zannetti and Onofri 1984][research_zannetti_onofri_1984]\] \[[Zastawny 2016][research_zastawny_2016]\] \[[Zhu 2024][research_zhu_2024]\] \[[Zimper and Hummel 2018][research_zimper_hummel_2018]\]

### Slender bodies, fuselages and apparent mass

Slender bodies and bodies of revolution, fuselage aerodynamics, apparent mass and the cross-flow on inclined bodies, which carry the article's fuselage instability.

**144 records.** \[[Abdelhamid 1985][research_abdelhamid_1985]\] \[[Adams and John C. 1968][research_adams_johnc_1968]\] \[[Aerodynamic Characteristics of Bodies 1951][research_aerodynamic_characteristics_1951]\] \[[Aerodynamics of arbitrary wing body combinations with vortex latticeand slender body theory 1976][research_aerodynamics_of_1976]\] \[[Allee 1973][research_allee_eg_1973]\] \[[Allen and Perkins 1951][research_allenhjulian_perkinsedwardw_1951]\] \[[Almosnino 1983][research_almosnino_1983]\] \[[Almosnino 1985][research_almosnino_1985]\] \[[AlQadi and Eljack 2016][research_alqadi_eljack_2016]\] \[[Atli 1988][research_atli_1988]\] \[[Atta and Nayfeh 1978][research_atta_nayfeh_1978]\] \[[Bai et al 2025][research_bai_deng_2025]\] \[[Baker 1978][research_bakerjr_1978]\] \[[Beall 1986][research_beall_1986]\] \[[Benedikt 1953][research_benedikt_1953]\] \[[Bond and Packard 1961][research_bondreuben_packardbarbarab_1961]\] \[[Borisova and Silantiev 2022][research_borisova_silantiev_2022]\] \[[Calarese 1981][research_calarese_1981]\] \[[Campbell 1959][research_campbell_1959]\] \[[Catani et al 1982][research_catani_deamicis_1982]\] \[[Cebeci et al 1983][research_cebeci_stewartson_1983]\] \[[Champigny 1984][research_champigny_1984]\] \[[Chaudhuri and Praharaj 1971][research_chaudhuri_praharaj_1971]\] \[[Cleary 1969][research_cleary_1969]\] \[[Clevenson et al 1953][research_clevensonsa_wildmayerejr_1953]\] \[[Cohen 1951][research_cohenrobertj_1951]\] \[[Cox 1957][research_cox_1957]\] \[[Deffenbaugh and Jacoby 1980][research_deffenbaugh_jacoby_1980]\] \[[DeJarnette and Jones 1978][research_dejarnette_jones_1978]\] \[[Desai and Pant 2026][research_desai_pant_2026]\] \[[Devan 1989][research_devan_1989]\] \[[Dexter and Hunt 1981][research_dexter_hunt_1981]\] \[[Doyle and Rosema 2015][research_doyle_rosema_2015]\] \[[Dress 1988][research_dress_1988]\] \[[Dress 1989][research_dress_1989]\] \[[Ehret et al 1950][research_ehretdorrism_rossowvernonj_1950]\] \[[Ericsson 1989][research_ericsson_1989]\] \[[Ericsson and Reding 1985][research_ericsson_reding_1985]\] \[[Est and Nelson 1992][research_est_nelson_1992]\] \[[Fediaevsky 1935][research_fediaevsky_1935]\] \[[Fleeman and Nelson 1974][research_fleeman_nelson_1974]\] \[[Froning 1981][research_froning_1981]\] \[[Gorski 1998][research_gorski_1998]\] \[[Grimminger et al 1950][research_grimminger_williams_1950]\] \[[Hall 1987][research_hall_1987]\] \[[Han and Patel 1977][research_han_patel_1977]\] \[[Heller and Clemente 1973][research_heller_clemente_1973]\] \[[Hemsch 1985][research_hemsch_1985]\] \[[Hemsch 1987][research_hemsch_1987]\] \[[Hemsch 1988][research_hemsch_1988]\] \[[Hemsch 1989][research_hemsch_1989]\] \[[Hsieh and Wang 1976][research_hsieh_wang_1976]\] \[[Hung 1979][research_hung_1979]\] \[[Hung 1980][research_hung_1980]\] \[[Influence of interference of the wing and fuselage on aerodynamic characteristics 2018][research_influence_of_interference_2018]\] \[[Jack 1951][research_jackjohnr_1951]\] \[[Jorgensen 1977][research_jorgensenlh_1977]\] \[[Jorgensen 1979][research_jorgensenlh_1979]\] \[[Kao 1975][research_kao_1975]\] \[[Karn et al 2021][research_karn_kumar_2021]\] \[[Keldysh 1958][research_keldysh_1958]\] \[[Kellock and Miller 1971][research_kellock_miller_1971]\] \[[Kerney and White 1975][research_kerney_white_1975]\] \[[Kirk 1961][research_kirkdonnb_1961]\] \[[Klimas and Kilikevičius 2024][research_klimas_kilikevicius_2024]\] \[[Koh 1968][research_koh_1968]\] \[[Lai and Kamaruddin 2018][research_lai_kamaruddin_2018]\] \[[Laitone 1947][research_laitone_1947]\] \[[Lee et al 2021][research_lee_huang_2021]\] \[[Lee et al 2021][research_lee_huang_2021_b]\] \[[Levy 2003][research_levy_2003]\] \[[Levy and Tobak 1970][research_levyjr_tobak_1970]\] \[[Li et al 2026][research_li_li_2026]\] \[[Lijewski 1986][research_lijewski_1986]\] \[[Loposer and Rumsey 1954][research_loposerjdan_rumseycharlesb_1954]\] \[[Luckert 1973][research_luckert_1973]\] \[[Malmuth et al 1983][research_malmuth_wu_1983]\] \[[Martin et al 1976][research_martin_saunders_1976]\] \[[Mateescu 1986][research_mateescu_1986]\] \[[Mateescu 1987][research_mateescu_1987]\] \[[Matveev and Wheeler 2022][research_matveev_wheeler_2022]\] \[[Miles 1952][research_miles_1952]\] \[[Miles 1953][research_miles_1953]\] \[[Moretti 1965][research_moretti_1965]\] \[[Munk 1979][research_munkmm_1979]\] \[[Munk 1924][research_munkmaxm_1924]\] \[[Murphy 1966][research_murphy_1966]\] \[[Murphy and Schmidt 1953][research_murphy_schmidt_1953]\] \[[Newman 1965][research_newman_1965]\] \[[Nicolosi et al 2015][research_nicolosi_dellavecchia_2015]\] \[[Nicolosi et al 2016][research_nicolosi_dellavecchia_2016]\] \[[Nielsen 1985][research_nielsen_1985]\] \[[Obeid et al 2019][research_obeid_alqadi_2019]\] \[[Osawa and Hewitt 1986][research_osawa_hewitt_1986]\] \[[Owen and Johnson 1978][research_owen_johnson_1978]\] \[[Paranjape et al 1966][research_paranjapesv_thomastj_1966]\] \[[Patel and Ramaprian 1978][research_patel_ramaprian_1978]\] \[[Peterson 1968][research_peterson_1968]\] \[[Pinebrook and Dalton 1983][research_pinebrook_dalton_1983]\] \[[Pinebrook and Dalton 1983][research_pinebrook_dalton_1983_b]\] \[[Platzer and Hoffman 1966][research_platzer_hoffman_1966]\] \[[Plyashechnik et al 1999][research_plyashechnik_ivanov_1999]\] \[[Prizirembel and Wen 1978][research_prizirembel_wen_1978]\] \[[Rajagopal et al 1988][research_rajagopal_lick_1988]\] \[[Rakich and Cleary 1970][research_rakich_cleary_1970]\] \[[Rakich and Cleary 2003][research_rakich_cleary_2003]\] \[[Reklis 1980][research_reklis_1980]\] \[[Rodden et al 1962][research_rodden_farkas_1962]\] \[[Rodgers 1963][research_rodgers_1963]\] \[[Rubin and Mummolo 1973][research_rubin_mummolo_1973]\] \[[Sacks 1954][research_sacksalvinh_1954]\] \[[Schoombie et al 2017][research_schoombie_tuling_2017]\] \[[Schuman 1981][research_schuman_1981]\] \[[Seiff and Sandahl 1951][research_seiffalvin_sandahlcarla_1951]\] \[[Sharma et al 1998][research_sharma_sekaran_1998]\] \[[Shekarriz et al 1991][research_shekarriz_fu_1991]\] \[[Sheridan 1968][research_sheridan_jr_1968]\] \[[Smith 1960][research_smithfm_1960]\] \[[Spreiter and Stahara 1970][research_spreiter_stahara_1970]\] \[[Stanek and Visbal 1991][research_stanek_visbal_1991]\] \[[Starr and Varner 1976][research_starr_varner_1976]\] \[[Thomas 1991][research_thomas_1991]\] \[[Transonic theory for flow past slender fuselages and afterbodies 1970][research_transonic_theory_1970]\] \[[Tsien 1938][research_tsien_1938]\] \[[Tsutsui et al 2021][research_tsutsui_takagi_2021]\] \[[Tuckerman 1923][research_tuckermanlb_1923]\] \[[Van Tuyl 1988][research_vantuyl_1988]\] \[[Vendemia 1965][research_vendemia_rj_1965]\] \[[Venkatachari et al 2015][research_venkatachari_mullane_2015]\] \[[Wang 1971][research_wang_1971]\] \[[Wang 1972][research_wang_1972]\] \[[Ward and Katz 1987][research_ward_katz_1987]\] \[[Ward and Katz 1987][research_ward_katz_1987_b]\] \[[Ward and Katz 1989][research_ward_katz_1989]\] \[[Ward and Katz 1989][research_ward_katz_1989_b]\] \[[Wardlaw et al 1975][research_wardlaw_andrewb_1975]\] \[[Wei 1964][research_wei_1964]\] \[[White 1977][research_white_1977]\] \[[White 1977][research_white_1977_b]\] \[[White 1995][research_white_1995]\] \[[Wolfe and Oberkampf 1982][research_wolfe_oberkampf_1982]\] \[[Wood and Murphy 1955][research_wood_murphy_1955]\] \[[Yamaoka 1963][research_yamaoka_1963]\] \[[Zilliac et al 1990][research_zilliac_degani_1990]\]

### Thrust vectoring, drag rudders and yaw effectors

Thrust vectoring, drag rudders, spoilers and other yaw effectors that replace or supplement a fin.

**140 records.** \[[Ahmed et al 2025][research_ahmed_elbanna_2025]\] \[[Alexander 1993][research_alexander_1993]\] \[[Anna and Kidman 1994][research_annapauld_kidmandavids_1994]\] \[[APPLICATION OF FLUIDIC THRUST VECTORING IN V/STOL AIRCRAFT 2024][research_application_of_2024_b]\] \[[Bacon et al 1996][research_baconbartonj_carzoosusanw_1996]\] \[[Baldini et al 2026][research_baldini_felicetti_2026]\] \[[Barnhouse et al 2025][research_barnhouse_hamid_2025]\] \[[Bazuhair 2018][research_bazuhair_2018]\] \[[Beard and Foley 1983][research_beardbb_foleywh_1983]\] \[[Behm 1973][research_behm_1973]\] \[[Berens 2019][research_berens_2019]\] \[[Bergman 1979][research_bergman_1979]\] \[[Brandt et al 2019][research_brandt_mclaughlin_2019]\] \[[Buffington et al 1993][research_buffington_sparks_1993]\] \[[Buffington et al 1994][research_buffington_sparks_1994]\] \[[Capello et al 2019][research_capello_ferrero_2019]\] \[[Capone 1979][research_capone_1979]\] \[[Capone and Mason 1986][research_capone_mason_1986]\] \[[Chawla and Van Dalsem 1992][research_chawla_vandalsem_1992]\] \[[Cheatham et al 1991][research_cheatham_gridley_1991]\] \[[Chudoba and Cook 2003][research_chudoba_cook_2003]\] \[[Cohn et al 1985][research_cohn_dusa_1985]\] \[[Collins et al 2004][research_collins_zhao_2004]\] \[[Collins Jr 2005][research_collinsjr_2005]\] \[[Cornelius and Lucius 1993][research_cornelius_lucius_1993]\] \[[Cornelius and Lucius 1995][research_cornelius_lucius_1995]\] \[[Crowther and Wood 1993][research_crowther_wood_1993]\] \[[Das et al 2024][research_das_mankodi_2024]\] \[[Davis and Hines 1976][research_davis_hines_1976]\] \[[Erwin et al 1964][research_erwin_clark_1964]\] \[[Esker and McArdle 1993][research_esker_mcardle_1993]\] \[[Esker and Sedrick 1972][research_esker_sedrick_1972]\] \[[Ferlauto and Marsilio 2016][research_ferlauto_marsilio_2016]\] \[[Friend 1964][research_friend_1964]\] \[[Gal-Or 1994][research_galor_1994]\] \[[Gal-Or 2001][research_galor_2001]\] \[[Gal-Or et al 1995][research_galor_sherbaum_1995]\] \[[Gill 1974][research_gill_1974]\] \[[Glezer and Leonard 2012][research_glezer_leonard_2012]\] \[[Goetz et al 1976][research_goetz_young_1976]\] \[[Granasy 1995][research_granasy_1995]\] \[[Ha et al 2025][research_ha_kim_2025]\] \[[Hall 1965][research_hall_1965]\] \[[Helicopter Yaw Control 1990][research_helicopter_yaw_1990]\] \[[Herrick 1992][research_herrick_1992]\] \[[Hienz and Vedova 1984][research_hienz_vedova_1984]\] \[[Hirano et al 2019][research_hirano_uchiyama_2019]\] \[[Hoholis et al 2016][research_hoholis_steijl_2016]\] \[[Hollmeier et al 1999][research_hollmeier_kopp_1999]\] \[[Hu et al 2025][research_hu_wen_2025]\] \[[Hunter et al 2001][research_huntercraiga_vikensallya_2001]\] \[[Isaac et al 2024][research_isaac_pena_2024]\] \[[Jeong et al 2015][research_jeong_lee_2015]\] \[[Jeong et al 2024][research_jeong_kim_2024]\] \[[Jiméneze and Icaza 2000][research_jimeneze_icaza_2000]\] \[[Jyothy and John Wessley 2023][research_jyothy_johnwessley_2023]\] \[[Kazarin et al 2017][research_kazarin_mackunis_2017]\] \[[Kentfield 1975][research_kentfield_1975]\] \[[Kentfield 1975][research_kentfield_1975_b]\] \[[Kigotho et al 2022][research_kigotho_bodylski_2022]\] \[[Kikkawa and Uchiyama 2017][research_kikkawa_uchiyama_2017]\] \[[Kou et al 2021][research_kou_wang_2021]\] \[[Kowal 2002][research_kowal_2002]\] \[[Kuang and Zhu 2015][research_kuang_zhu_2015]\] \[[Kumar et al 2020][research_kumar_bhargavapuri_2020]\] \[[Lampard 1978][research_lampard_1978]\] \[[Lee et al 2018][research_lee_song_2018]\] \[[Li and Ma 2014][research_li_ma_2014]\] \[[Li et al 2018][research_li_dong_2018]\] \[[Li et al 2022][research_li_xu_2022]\] \[[Liu et al 2022][research_liu_gao_2022]\] \[[Liu et al 2024][research_liu_gao_2024]\] \[[Luo et al 2025][research_luo_cui_2025]\] \[[Lyu et al 2023][research_lyu_yin_2023]\] \[[Mace et al 1989][research_mace_smereczniak_1989]\] \[[Malcolm and Ng 1990][research_malcolmgn_ngtt_1990]\] \[[Margetts et al 2015][research_margetts_bingham_2015]\] \[[Mason and Crowther 2004][research_mason_crowther_2004]\] \[[Maughmer et al 1990][research_maughmermarkd_ozoroskil_1990]\] \[[Miller 1983][research_miller_1983]\] \[[Miller 1986][research_miller_1986]\] \[[Miwa 2021][research_miwa_2021]\] \[[Miwa and Maruhashi 2016][research_miwa_maruhashi_2016]\] \[[Murri and Rao 1987][research_murri_rao_1987]\] \[[Murri et al 1994][research_murridanielg_shahgautamh_1994]\] \[[Natarajan et al 2004][research_natarajan_kapania_2004]\] \[[Nguyen et al 2025][research_nguyen_han_2025]\] \[[O'Rourke 1995][research_orourke_1995]\] \[[O'Rourke and Sedor 1995][research_orourke_sedor_1995]\] \[[Oosedo et al 2022][research_oosedo_wada_2022]\] \[[Pahle et al 1996][research_pahlejosephw_bundickwthomas_1996]\] \[[Pedreiro 1997][research_pedreironelson_1997]\] \[[Pulk and Stolarik 1977][research_pulk_stolarik_1977]\] \[[Raney et al 2000][research_raneydavidl_montgomeryraymondc_2000]\] \[[Resta et al 2021][research_resta_marsilio_2021]\] \[[Rolls and Aoyagi 1977][research_rolls_aoyagi_1977]\] \[[Roseberg 1982][research_rosebergew_1982]\] \[[Ruetten 2018][research_ruetten_2018]\] \[[Salagame et al 2025][research_salagame_pandya_2025]\] \[[Schirmer and Capone 1989][research_schirmer_capone_1989]\] \[[Shearwood et al 2021][research_shearwood_nabawy_2021_b]\] \[[Shendge 2021][research_shendge_2021]\] \[[Sherbaum and Lichtsinder 1998][research_sherbaum_lichtsinder_1998]\] \[[Shi et al 2024][research_shi_hui_2024]\] \[[Shmilovich and Princen 2026][research_shmilovich_princen_2026]\] \[[Shukla et al 2026][research_shukla_mitra_2026]\] \[[Silva et al 2018][research_silva_dewagter_2018]\] \[[Snow 1990][research_snow_1990]\] \[[Soundararajan 2022][research_soundararajan_btn_2022]\] \[[Soundararajan and Sridhar 2024][research_soundararajan_sridhar_2024]\] \[[Steer 2000][research_steer_2000]\] \[[Steer 2000][research_steer_2000_b]\] \[[Syed et al 1990][research_syed_erhart_1990]\] \[[Syed et al 1992][research_syed_erhart_1992]\] \[[Tanveer and Ahmad 2023][research_tanveer_ahmad_2023]\] \[[Tanveer and Ahmad 2023][research_tanveer_ahmad_2023_b]\] \[[Tavella et al 1986][research_tavella_lee_1986]\] \[[Tavella et al 1987][research_tavella_lee_1987]\] \[[Taylor 1988][research_taylor_1988]\] \[[Thomas et al 1977][research_thomas_paulsonjr_1977]\] \[[Ulizar 1997][research_ulizar_1997]\] \[[Vechtel and Buch 2022][research_vechtel_buch_2022]\] \[[Vieira and Maughmer 2017][research_vieira_maughmer_2017]\] \[[Visser 1999][research_visser_1999]\] \[[Wang et al 2020][research_wang_zhu_2020_b]\] \[[Wang et al 2025][research_wang_zhang_2025]\] \[[Warsop and Crowther 2019][research_warsop_crowther_2019_b]\] \[[Warsop et al 2019][research_warsop_crowther_2019]\] \[[Whitaker and Gowadia 1994][research_whitaker_gowadia_1994]\] \[[Wilcox 1913][research_wilcox_1913]\] \[[Wood and Bauer 1999][research_woodrichardm_bauerstevenxs_1999]\] \[[Wornom 1960][research_wornomde_1960]\] \[[Xu and Zhang 2025][research_xu_zhang_2025]\] \[[Xue et al 2021][research_xue_yunsong_2021]\] \[[Yi et al 1979][research_yi_heimbold_1979]\] \[[Yong et al 2020][research_yong_wu_2020]\] \[[Yu and Kim 2024][research_yu_kim_2024]\] \[[Yu et al 2023][research_yu_zhang_2023]\] \[[Zhou et al 2022][research_zhou_wang_2022]\] \[[Zwerneman and Eller 1994][research_zwerneman_eller_1994]\]

### Directional stability and lateral-directional dynamics

Directional and lateral-directional stability and dynamics, the subject a missing fin makes primary.

**137 records.** \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_e]\] \[[Alaian et al 2016][research_alaian_basuno_2016]\] \[[Albostan and Gökaşan 2018][research_albostan_gokasan_2018]\] \[[Alston 1936][research_alston_1936]\] \[[Ananthkrishnan and Sinha 2023][research_ananthkrishnan_sinha_2023]\] \[[Anderson et al 2004][research_anderson_phillips_2004]\] \[[Ashraf and Van Kampen 2020][research_ashraf_vankampen_2020]\] \[[Atzhorn and Stengel 1981][research_atzhorn_stengel_1981]\] \[[Bachmaier and Anderson 2021][research_bachmaier_anderson_2021]\] \[[Balas et al 1996][research_balas_packard_1996]\] \[[Balas et al 1997][research_balas_fialho_1997]\] \[[Balas et al 1998][research_balas_packard_1998]\] \[[Banerjee et al 2017][research_banerjee_boyce_2017]\] \[[Bielat and Wiley 1959][research_bielatralphp_wileyharlethg_1959]\] \[[Bischoff and Palmer 1982][research_bischoff_palmer_1982]\] \[[Bischoff and Palmer 1983][research_bischoff_palmer_1983]\] \[[Bischoff et al 1974][research_bischoff_duffy_1974]\] \[[Bloy and Lea 1995][research_bloy_lea_1995]\] \[[Brandeau 1978][research_brandeau_1978]\] \[[Bryson 1954][research_bryson_1954]\] \[[Campbell and Abramovitz 1975][research_campbell_abramovitz_1975]\] \[[Cavanaugh 2003][research_cavanaugh_2003]\] \[[Chambers and Hall 2004][research_chambers_hall_2004]\] \[[Chavez and Vogel 2003][research_chavez_vogel_2003]\] \[[Chen and Xie 2024][research_chen_xie_2024]\] \[[Chen et al 2026][research_chen_gray_2026]\] \[[Chowdhury et al 2021][research_chowdhury_keshmiri_2021]\] \[[Chuan et al 2016][research_chuan_feng_2016]\] \[[Ciliberti and Nicolosi 2025][research_ciliberti_nicolosi_2025]\] \[[Coe et al 1975][research_coepljr_grahamab_1975]\] \[[Connors and Swaim 1968][research_connors_swaim_1968]\] \[[Corona-Sanchez and Rodriguez-Cortes 2015][research_coronasanchez_rodriguezcortes_2015]\] \[[Costigan and Calico 1989][research_costigan_calico_1989]\] \[[Davidson et al 1998][research_davidsonjohnb_murphypatrickc_1998]\] \[[De et al 2015][research_de_salvatore_2015]\] \[[de Paula et al 2017][research_depaula_porto_2017]\] \[[Della Vecchia et al 2015][research_dellavecchia_nicolosi_2015]\] \[[Dolan 1964][research_dolan_1964]\] \[[El Mobaraky et al 2026][research_elmobaraky_benjelloun_2026]\] \[[Enns 1990][research_enns_1990]\] \[[Fahmi and Woolsey 2018][research_fahmi_woolsey_2018]\] \[[Fialho et al 1997][research_fialho_balas_1997]\] \[[Foster et al 1993][research_foster_ross_1993]\] \[[Frazier 1991][research_frazier_1991]\] \[[Garrard 1998][research_garrard_1998]\] \[[Ghosh et al 1998][research_ghosh_raisinghani_1998]\] \[[Gilyard et al 1972][research_gilyard_berry_1972]\] \[[Goodwin and Kaattari 1958][research_goodwinfrederickk_kaattarigeorgee_1958]\] \[[Goud and Dwivedi 2022][research_goud_dwivedi_2022]\] \[[Hall and Boothe 1972][research_hall_boothe_1972]\] \[[Hart and Picha 1979][research_hart_picha_1979]\] \[[Hegde et al 2019][research_hegde_george_2019]\] \[[Hougui et al 1995][research_hougui_balas_1995]\] \[[Huang 2016][research_huang_2016]\] \[[Johnson 1940][research_johnson_1940]\] \[[Kanneganti et al 2022][research_kanneganti_charan_2022]\] \[[Kojima et al 2024][research_kojima_hidaka_2024]\] \[[Kostić et al 2024][research_kostic_simonovic_2024]\] \[[Kuhn 1981][research_kuhn_1981]\] \[[Kumar and Prakash 2022][research_kumar_prakash_2022]\] \[[Liang et al 2026][research_liang_kou_2026]\] \[[Lin et al 1998][research_lin_ge_1998]\] \[[Liu 2024][research_liu_2024]\] \[[Livneh 1995][research_livneh_1995]\] \[[Livneh 1995][research_livneh_1995_b]\] \[[Long Lu and Turkoglu 2015][research_longlu_turkoglu_2015]\] \[[Lu and Turkoglu 2016][research_lu_turkoglu_2016]\] \[[Lu and Turkoglu 2018][research_lu_turkoglu_2018]\] \[[Lungu and Lungu 2015][research_lungu_lungu_2015]\] \[[Lungu and Lungu 2016][research_lungu_lungu_2016_b]\] \[[Luu and Ochi 2023][research_luu_ochi_2023]\] \[[Lyu et al 2022][research_lyu_gong_2022]\] \[[Lyu et al 2023][research_lyu_ye_2023]\] \[[Ma et al 2019][research_ma_zhu_2019_b]\] \[[Mann et al 1987][research_mannmichaelj_huffmanjarrettk_1987]\] \[[Marino and Mastrocola 1952][research_marinoalfreda_mastrocolan_1952]\] \[[Martínez-Ramírez and Rodríguez-Cortés 2022][research_martinezramirez_rodriguezcortes_2022]\] \[[Mason and Ravi 1994][research_mason_ravi_1994]\] \[[Mengali 2003][research_mengali_2003]\] \[[Mineck 1977][research_mineckre_1977]\] \[[Mohamed and Joy 2021][research_mohamed_joy_2021]\] \[[Mohan and Kumar 2024][research_mohan_kumar_2024]\] \[[Napolitano and Kincheloe 1996][research_napolitano_kincheloe_1996]\] \[[Nicolosi et al 2020][research_nicolosi_ciliberti_2020]\] \[[Nie et al 2020][research_nie_liu_2020]\] \[[Park et al 2001][research_park_lee_2001]\] \[[Peristy et al 2019][research_peristy_perez_2019]\] \[[Peterson 2024][research_peterson_2024]\] \[[Peterson 2025][research_peterson_2025]\] \[[Peterson 1961][research_petersonvictorl_1961]\] \[[Phillips 2000][research_phillips_2000]\] \[[Phillips 2000][research_phillips_2000_b]\] \[[Poojari 2022][research_poojari_2022]\] \[[Price 1943][research_price_1943]\] \[[Putman 1969][research_putman_1969]\] \[[Raul Azinheira et al 2001][research_raulazinheira_carneirodepaiva_2001]\] \[[Ravi and Mason 1994][research_ravi_mason_1994]\] \[[Reigelsperger et al 1995][research_reigelsperger_hammett_1995]\] \[[Robinson 1958][research_robinsonrb_1958]\] \[[Sachan et al 2025][research_sachan_r_2025]\] \[[Sanfilippo 1970][research_sanfilippo_1970]\] \[[Seaver et al 2023][research_seaver_bennett_2023]\] \[[Shah and Granda 1998][research_shah_granda_1998]\] \[[Shankar and Yathisha 2023][research_shankar_l_2023]\] \[[Silva et al 2022][research_silva_nunes_2022]\] \[[Singh and Jategaonkar 1996][research_singh_jategaonkar_1996]\] \[[Singh and Raol 2000][research_singh_raol_2000]\] \[[Sinha and Ananthkrishnan 2002][research_sinha_ananthkrishnan_2002]\] \[[Sivan 1971][research_sivan_1971]\] \[[Snell 1993][research_snell_1993]\] \[[Snell et al 1991][research_snell_garrardjr_1991]\] \[[Sparks et al 1994][research_sparks_buffington_1994]\] \[[Stalford 1979][research_stalford_1979]\] \[[Stengel 1975][research_stengel_1975]\] \[[Stengel 1980][research_stengel_1980]\] \[[Stengel and Miller 1978][research_stengel_miller_1978]\] \[[Swaim and Connor 1968][research_swaim_connor_1968]\] \[[Swarnkar and Kothari 2016][research_swarnkar_kothari_2016]\] \[[Sánchez et al 2024][research_sanchez_cajas_2024]\] \[[Tai et al 2023][research_tai_wang_2023]\] \[[Thacker and Lan 1993][research_thacker_lan_1993]\] \[[Thompson and Gilruth 1940][research_thompsonfl_gilruthrr_1940]\] \[[Tournes and Landrum 2003][research_tournes_landrum_2003]\] \[[van Rooyen and Eshelby 1981][research_vanrooyen_eshelby_1981]\] \[[Wandini et al 2016][research_wandini_mulyanto_2016]\] \[[Wang et al 1999][research_wang_lan_1999]\] \[[Wang et al 2016][research_wang_liu_2016]\] \[[Wang et al 2022][research_wang_zhao_2022]\] \[[Wu et al 2018][research_wu_lv_2018]\] \[[Xiuming Liu et al 2016][research_xiumingliu_yingwang_2016]\] \[[Yanagihara et al 1991][research_yanagihara_suzuki_1991]\] \[[Yang et al 2026][research_yang_xu_2026]\] \[[Zanette and Almeida 2015][research_zanette_almeida_2015]\] \[[Zhang et al 2017][research_zhang_wang_2017_b]\] \[[Zhao et al 2022][research_zhao_li_2022]\] \[[Öznurlu et al 2023][research_oznurlu_bayri_2023]\]

### Time delay, latency and delay compensation

Time delay and its compensation in control systems and teleoperation, the stability of delayed systems, and the effect of delay on the pilot.

**135 records.** \[[Abidi et al 2016][research_abidi_yildiz_2016]\] \[[Alsolami et al 2025][research_alsolami_bhattacharjee_2025]\] \[[Alvarez-Munoz et al 2019][research_alvarezmunoz_castillozamora_2019]\] \[[Azarmi and Tavakoli-Kakhki 2020][research_azarmi_tavakolikakhki_2020]\] \[[Baker and Batavia 2016][research_baker_batavia_2016]\] \[[Bellamri et al 2024][research_bellamri_benineneto_2024]\] \[[Bing et al 2015][research_bing_feng_2015]\] \[[Black et al 2024][research_black_andjelic_2024]\] \[[Blanken and Pausder 1994][research_blanken_pausder_1994]\] \[[Bordei and Halanay 2025][research_bordei_halanay_2025]\] \[[Breitung 2001][research_breitung_2001]\] \[[Brudnak 2016][research_brudnak_2016]\] \[[Brudnak 2020][research_brudnak_2020]\] \[[Brueckner et al 2023][research_brueckner_patinostudencki_2023]\] \[[Caradima and Wang 2000][research_caradima_wang_2000]\] \[[Carter 1976][research_carter_1976]\] \[[Chao et al 2017][research_chao_ying_2017]\] \[[Chen and Liu 2021][research_chen_liu_2021]\] \[[Chen et al 2022][research_chen_ma_2022]\] \[[Crane 1983][research_cranedf_1983]\] \[[King 1993][research_davidwking_1993]\] \[[Delay-dependent stability criteria for discrete-time delay systems 1999][research_delay_dependent_stability_1999]\] \[[Ding and Eskandarian 2024][research_ding_eskandarian_2024]\] \[[Du 2019][research_du_2019]\] \[[Ellis and Christofides 2015][research_ellis_christofides_2015]\] \[[Gamal et al 2016][research_gamal_sadek_2016]\] \[[González et al 2017][research_gonzalez_aranda_2017]\] \[[Gu and Lee 1988][research_gu_lee_1988]\] \[[Han et al 2026][research_han_kim_2026]\] \[[Hashemipour et al 2017][research_hashemipour_vasegh_2017]\] \[[Hashemzadeh et al 2016][research_hashemzadeh_sharifi_2016]\] \[[He et al 2021][research_he_zhang_2021]\] \[[Herrera et al 2018][research_herrera_njeh_2018]\] \[[Heryana et al 2022][research_heryana_krisnandi_2022]\] \[[Hirai and Satoh 1980][research_hirai_satoh_1980]\] \[[Huang et al 2022][research_huang_zhang_2022]\] \[[Ionita 1996][research_ionita_1996]\] \[[Jafari and Spong 2017][research_jafari_spong_2017]\] \[[Ji et al 2025][research_ji_avedisov_2025]\] \[[Armah 2018][research_karmah_2018]\] \[[Katsanikakis and Bekiaris-Liberis 2025][research_katsanikakis_bekiarisliberis_2025]\] \[[Katsuyama et al 2023][research_katsuyama_sato_2023]\] \[[Kharitonov 1999][research_kharitonov_1999]\] \[[Kharrat 2024][research_kharrat_2024]\] \[[Kumar 2015][research_kumar_2015]\] \[[Kumar and Hote 2022][research_kumar_hote_2022]\] \[[Kumar et al 2018][research_kumar_bombuwela_2018]\] \[[Kumar et al 2022][research_kumar_kumar_2022]\] \[[Kuzu et al 2015][research_kuzu_bogosyan_2015]\] \[[Lane et al 2001][research_lane_carignan_2001]\] \[[Lee and Chang 1998][research_lee_chang_1998]\] \[[Levison and Papazian 1987][research_levison_papazian_1987]\] \[[Li et al 2017][research_li_qin_2017]\] \[[Li et al 2026][research_li_han_2026]\] \[[Liu 2023][research_liu_2023]\] \[[Liu and Brandel 2004][research_liu_brandel_2004]\] \[[Liu et al 2026][research_liu_li_2026_b]\] \[[Lloyds Raja and Ali 2017][research_lloydsraja_ali_2017]\] \[[Loo 1969][research_loo_1969]\] \[[Luz et al 2023][research_luz_silva_2023]\] \[[Ma et al 2015][research_ma_du_2015]\] \[[Ma et al 2024][research_ma_yu_2024]\] \[[Mazenc and Malisoff 2020][research_mazenc_malisoff_2020]\] \[[Mirzal 2017][research_mirzal_2017]\] \[[Mitchell et al 1991][research_mitchell_hoh_1991]\] \[[Moniruzzaman et al 2021][research_moniruzzaman_rassau_2021]\] \[[Moniruzzaman et al 2022][research_moniruzzaman_rassau_2022]\] \[[N-Nagy and Al-Tikriti 1970][research_nnagy_altikriti_1970]\] \[[Nasiri et al 2021][research_nasiri_montazerigh_2021]\] \[[Nenadic et al 1997][research_nenadic_debeljkovic_1997]\] \[[Optimized PI-PD Control for Varying Time Delay Systems Based on Modified Smith Predictor 2024][research_optimized_pi_pd_2024]\] \[[Orlosky et al 2018][research_orlosky_theofilis_2018]\] \[[Ostermann et al 2024][research_ostermann_laubner_2024]\] \[[Ozturk 1986][research_ozturk_1986]\] \[[Ozturk 1991][research_ozturk_1991]\] \[[Pacheco-Gutierrez et al 2021][research_pachecogutierrez_niu_2021]\] \[[Pakzad 2021][research_pakzad_2021]\] \[[Piccinelli and Muradore 2021][research_piccinelli_muradore_2021]\] \[[Popescu et al 2003][research_popescu_rasvan_2003]\] \[[Prakash et al 2019][research_prakash_vignati_2019]\] \[[Provost et al 2026][research_provost_hawlader_2026]\] \[[Provost et al 2026][research_provost_hawlader_2026_b]\] \[[Pryor et al 2020][research_pryor_vagvolgyi_2020]\] \[[Qi et al 2016][research_qi_gao_2016]\] \[[Rajarajan et al 2024][research_rajarajan_mudhangulla_2024]\] \[[Rakita et al 2020][research_rakita_mutlu_2020]\] \[[Ramírez et al 2021][research_ramirez_breda_2021]\] \[[Rao and Srinath 1965][research_rao_srinath_1965]\] \[[Roy et al 2017][research_roy_sengupta_2017]\] \[[Salinas et al 2015][research_salinas_slawinski_2015]\] \[[Sato et al 2021][research_sato_kashihara_2021]\] \[[Scholcover and Gillan 2017][research_scholcover_gillan_2017]\] \[[Sharma and Rajamani 2024][research_sharma_rajamani_2024]\] \[[Shen et al 2025][research_shen_lv_2025]\] \[[Shinoda et al 1998][research_shinoda_niwa_1998]\] \[[Shinoda et al 1999][research_shinoda_niwa_1999]\] \[[Singh 2025][research_singh_2025]\] \[[Smith and Sarrafian 1986][research_smith_sarrafian_1986]\] \[[SS networked control and teleoperation 2017][research_ss_networked_2017]\] \[[Stojanovic and Debeljkovic 2004][research_stojanovic_ljdebeljkovic_2004]\] \[[Stojanovic and Debeljkovic 2004][research_stojanovic_ljdebeljkovic_2004_b]\] \[[Storms and Tilbury 2015][research_storms_tilbury_2015]\] \[[Su et al 1993][research_su_shyr_1993]\] \[[Sun et al 2025][research_sun_liu_2025]\] \[[Tavakoli 2024][research_tavakoli_2024]\] \[[Thompson 1970][research_thompson_1970]\] \[[Tian 2021][research_tian_2021]\] \[[Tian et al 2015][research_tian_li_2015]\] \[[Ting et al 2016][research_ting_shun_2016]\] \[[Tissir and Hmamed 1994][research_tissir_hmamed_1994]\] \[[Tokutake et al 1999][research_tokutake_ohta_1999]\] \[[Tumerdem and Yilmaz 2021][research_tumerdem_yilmaz_2021]\] \[[Uddin and Ryu 2016][research_uddin_ryu_2016]\] \[[Vite and Mondie 2022][research_vite_mondie_2022]\] \[[Webb et al 2016][research_webb_li_2016]\] \[[Wu et al 2018][research_wu_chen_2018]\] \[[Xing and Zhang 2017][research_xing_zhang_2017]\] \[[Yang et al 2019][research_yang_liu_2019]\] \[[Yeg̃in and Özbay 2023][research_yegin_ozbay_2023]\] \[[Yongming and Yuanqing 2015][research_yongming_yuanqing_2015]\] \[[Youcef-Toumi and Bobbett 1991][research_youceftoumi_bobbett_1991]\] \[[Youcef-Toumi and Wu 1992][research_youceftoumi_wu_1992]\] \[[Yue et al 2003][research_yue_won_2003]\] \[[Zahedi and Haeri 2017][research_zahedi_haeri_2017]\] \[[Zennir et al 2017][research_zennir_larabi_2017]\] \[[Zennir et al 2017][research_zennir_larabi_2017_b]\] \[[Zhang 2023][research_zhang_2023]\] \[[Zhang and Bradley 2022][research_zhang_bradley_2022]\] \[[Zhang et al 1992][research_zhang_saeki_1992]\] \[[Zhang et al 2015][research_zhang_tomizuka_2015]\] \[[Zhang et al 2019][research_zhang_zhou_2019]\] \[[Zhao et al 2024][research_zhao_zhang_2024]\] \[[Zhong et al 2023][research_zhong_pu_2023]\] \[[Zhou 2023][research_zhou_2023]\] \[[Zhu and Zhang 2018][research_zhu_zhang_2018]\]

### Stability margins and robust control

Gain, phase and delay margins, robustness analysis and the fundamental limitations of feedback, which fix the article's delay budget.

**105 records.** \[[088 Stability margin of a feedback system with structured and unstructured uncertainties 1994][research_088_stability_1994]\] \[[A simple link between pole shifting and phase margin 1994][research_a_simple_1994]\] \[[Ahmadi and Haeri 2017][research_ahmadi_haeri_2017]\] \[[Ahmadi and Haeri 2018][research_ahmadi_haeri_2018]\] \[[Amato et al 1996][research_amato_ambrosino_1996]\] \[[Amaya et al 2026][research_amaya_xiang_2026]\] \[[Analytic constraints in feedback control of linear time-varying systems: Bode's sensitivity integral 1999][research_analytic_constraints_1999]\] \[[Balcan et al 2026][research_balcan_kucuker_2026]\] \[[Bar-On and Jonckheere 1991][research_baron_jonckheere_1991]\] \[[Begum et al 2020][research_begum_rao_2020]\] \[[Bennett and Baras 1985][research_bennett_baras_1985]\] \[[Bercovici et al 1990][research_bercovici_foias_1990]\] \[[Bhusal and Subbarao 2022][research_bhusal_subbarao_2022]\] \[[Bosworth and Stachowiak 2005][research_bosworthjohnt_stachowiaksusanj_2005]\] \[[Brimelow 1970][research_brimelow_1970]\] \[[Cao et al 2017][research_cao_tang_2017]\] \[[Chand and Chiu 1991][research_chand_chiu_1991]\] \[[Chandra et al 2025][research_chandra_gandhi_2025]\] \[[Chen 1992][research_chen_1992]\] \[[Chen 1993][research_chen_1993]\] \[[Clements 2016][research_clementskeith_2016]\] \[[Clements 2017][research_clementskeith_2017]\] \[[Czarkowski 2004][research_czarkowski_2004]\] \[[Dorato et al 1999][research_dorato_famularo_1999]\] \[[Elia 2004][research_elia_2004]\] \[[Emirler 2018][research_emirler_2018]\] \[[Famularo et al 1999][research_famularo_dorato_1999]\] \[[Freudenberg and Looze 1985][research_freudenberg_looze_1985]\] \[[Galeani et al 2004][research_galeani_grasselli_2004]\] \[[Glad 1982][research_glad_1982]\] \[[Glad 1984][research_glad_1984]\] \[[Ho et al 1993][research_ho_hang_1993]\] \[[Ho et al 1995][research_ho_hang_1995]\] \[[Ho et al 1998][research_ho_lim_1998]\] \[[Huang and Wang 2001][research_huang_wang_2001]\] \[[Jie Chen 1995][research_jiechen_1995]\] \[[Jie Chen 1998][research_jiechen_1998]\] \[[Jin et al 2018][research_jin_song_2018]\] \[[Jugo 2001][research_jugo_2001]\] \[[Junnarkar et al 2026][research_junnarkar_seiler_2026]\] \[[Kammer 2025][research_kammer_2025]\] \[[Katayanagi 2001][research_katayanagi_2001]\] \[[Kellett 1996][research_kellett_1996]\] \[[Kellett et al 1996][research_kellett_baguley_1996]\] \[[Khouloud and Ali 2023][research_khouloud_ali_2023]\] \[[Kiefer et al 2016][research_kieferjm_johnsonmd_2016]\] \[[Kim 2023][research_kim_2023]\] \[[Koduri et al 2016][research_koduri_rodriguezayerbe_2016]\] \[[Koduri et al 2016][research_koduri_rodriguezayerbe_2016_b]\] \[[Kubo 1999][research_kubo_1999]\] \[[Le Yi Wang and Ji-Feng Zhang 2001][research_leyiwang_jifengzhang_2001]\] \[[Lei et al 2025][research_lei_dong_2025]\] \[[Liang et al 2025][research_liang_wang_2025]\] \[[Lin and Han 1986][research_lin_han_1986]\] \[[Lindberg and Pates 2023][research_lindberg_pates_2023]\] \[[Lucarini et al 2025][research_lucarini_dirito_2025]\] \[[Luhanga and Mwandosya 1986][research_luhanga_mwandosya_1986]\] \[[Ly 2002][research_ly_2002]\] \[[Maeda and Vidyasagar 1985][research_maeda_vidyasagar_1985]\] \[[Mao and Chen 2026][research_mao_chen_2026]\] \[[Mazenc and Malisoff 2022][research_mazenc_malisoff_2022]\] \[[Molander and Willems 1980][research_molander_willems_1980]\] \[[Mori 1988][research_mori_1988]\] \[[Nataraj and Sardar 1999][research_nataraj_sardar_1999]\] \[[Nogami et al 1986][research_nogami_maeda_1986]\] \[[Noury and Yang 2020][research_noury_yang_2020]\] \[[Palframan et al 2019][research_palframan_fry_2019]\] \[[Patel et al 2002][research_patel_deodhare_2002]\] \[[Perng et al 2004][research_perng_wu_2004]\] \[[Pfifer and Seiler 2015][research_pfifer_seiler_2015]\] \[[Power 1969][research_power_1969]\] \[[Prabhakar et al 2019][research_prabhakar_prazenica_2019]\] \[[Quenzer et al 2018][research_quenzer_barzgaran_2018]\] \[[Ren and Quan 2016][research_ren_quan_2016]\] \[[Robertson 1997][research_robertson_1997]\] \[[Rossi and Miller 1999][research_rossi_miller_1999]\] \[[Roy and Bhasin 2019][research_roy_bhasin_2019]\] \[[Ryan 1990][research_ryanlaurae_1990]\] \[[Safonov and Athans 1976][research_safonov_athans_1976]\] \[[Safonov and Athans 1977][research_safonov_athans_1977]\] \[[Sariyildiz et al 2018][research_sariyildiz_mutlu_2018]\] \[[Satoh and Sugimoto 2002][research_satoh_sugimoto_2002]\] \[[Schmidt and Newman 1990][research_schmidtdavidk_newmanbrett_1990]\] \[[Sezer and Siljak 1980][research_sezer_siljak_1980]\] \[[Sezer and Siljak 1981][research_sezer_siljak_1981]\] \[[Shi et al 2021][research_shi_liu_2021]\] \[[Shin and Belcastro 2008][research_shinjongyeob_belcastrochristine_2008]\] \[[Singh and Padhy 2017][research_singh_padhy_2017]\] \[[Sobel et al 1983][research_sobel_chung_1983]\] \[[Sobhani and Jayasuriya 1994][research_sobhani_jayasuriya_1994]\] \[[Srazhidinov et al 2023][research_srazhidinov_liang_2023]\] \[[Surmann et al 2024][research_surmann_myschik_2024]\] \[[Tan 2004][research_tan_2004]\] \[[Tsu-Tian Lee and Shiow-Harn Lee 1988][research_tsutianlee_shiowharnlee_1988]\] \[[Uchida et al 1986][research_uchida_shimemura_1986]\] \[[Viola and Angel 2015][research_viola_angel_2015]\] \[[Wang et al 2017][research_wang_huang_2017]\] \[[Woolcock and Schmid 2026][research_woolcock_schmid_2026]\] \[[Yamaguchi et al 2000][research_yamaguchi_ohno_2000]\] \[[Yamaguchi et al 2001][research_yamaguchi_ohara_2001]\] \[[Yang and Kabamba 1991][research_yang_kabamba_1991]\] \[[Yaniv 1992][research_yaniv_1992]\] \[[Yue Zhao et al 2016][research_yuezhao_letianlin_2016]\] \[[Zhang et al 2024][research_zhang_zhou_2024]\] \[[Zhong and Huang 2023][research_zhong_huang_2023]\]

### Control allocation and redundant effectors

Control allocation among redundant effectors, for aircraft and for the multirotor and tilt-rotor vehicles that have only redundant effectors.

**90 records.** \[[Akram et al 2020][research_akram_tedesco_2020]\] \[[Antonakis and Biannic 2024][research_antonakis_biannic_2024]\] \[[Asghari and Tayefi 2026][research_asghari_tayefi_2026]\] \[[Atay et al 2021][research_atay_bryant_2021]\] \[[Baggi et al 2020][research_baggi_franco_2020]\] \[[Baggi et al 2022][research_baggi_serrani_2022]\] \[[Battipede et al 2004][research_battipede_gili_2004]\] \[[Bernhard and Adamy 2017][research_bernhard_adamy_2017]\] \[[Bezerra and Santos 2022][research_bezerra_santos_2022]\] \[[Bodson 2000][research_bodson_2000]\] \[[Bolling et al 1997][research_bolling_durham_1997]\] \[[Buffington and Buffington 1997][research_buffington_buffington_1997]\] \[[Bugliari Armenio et al 2024][research_bugliariarmenio_cortigiani_2024]\] \[[Burken et al 2001][research_burken_lu_2001]\] \[[Cao et al 2022][research_cao_zhang_2022]\] \[[Chen et al 2026][research_chen_li_2026]\] \[[Cong et al 2023][research_cong_hu_2023]\] \[[Cui et al 2021][research_cui_zuo_2021]\] \[[de Castro and Brembeck 2019][research_decastro_brembeck_2019]\] \[[de Vries and Van Kampen 2019][research_devries_vankampen_2019]\] \[[Derrouaoui et al 2023][research_derrouaoui_bouzid_2023]\] \[[Doman and Sparks 2002][research_doman_sparks_2002]\] \[[Dong et al 2016][research_dong_lu_2016]\] \[[Dong et al 2025][research_dong_zhou_2025]\] \[[Duan and Okwudire 2018][research_duan_okwudire_2018]\] \[[Durham 1999][research_durham_1999]\] \[[Durham and Nelson 2001][research_durhamwayne_nelsonmark_2001]\] \[[Enenakpogbe et al 2025][research_enenakpogbe_whidborne_2025]\] \[[Enns 1998][research_enns_1998]\] \[[Fan et al 2006][research_fan_zhu_2006]\] \[[Frost et al 2009][research_frostsusana_bodsonmarc_2009]\] \[[Goodrich and Sliwa 1987][research_goodrich_sliwa_1987]\] \[[Grogan et al 1994][research_grogan_durham_1994]\] \[[Harkegard 2003][research_harkegard_2003]\] \[[Jafari et al 2022][research_jafari_khakisedigh_2022]\] \[[Jothiraj et al 2020][research_jothiraj_sharf_2020]\] \[[Kamath et al 2025][research_kamath_sivakumar_2025]\] \[[Krimphove et al 2023][research_krimphove_schutt_2023]\] \[[Li et al 2023][research_li_sun_2023]\] \[[Li et al 2025][research_li_lian_2025]\] \[[Libório et al 2025][research_liborio_pimentel_2025]\] \[[Lin et al 2019][research_lin_zhang_2019]\] \[[Liu et al 2015][research_liu_jiang_2015]\] \[[Liu et al 2018][research_liu_gao_2018]\] \[[Maadani et al 2023][research_maadani_lopezmuro_2023]\] \[[Martin 2025][research_martin_2025]\] \[[Matamoros and de Visser 2018][research_matamoros_devisser_2018]\] \[[Miles and Broughton 2017][research_miles_broughton_2017]\] \[[Montgomery and Hunsaker 2022][research_montgomery_hunsaker_2022]\] \[[Nelson and Durham 2002][research_nelson_durham_2002]\] \[[Page and Steinberg 1999][research_page_steinberg_1999]\] \[[Park et al 2019][research_park_shin_2019]\] \[[Pfeifle and Fichter 2023][research_pfeifle_fichter_2023]\] \[[Pose et al 2017][research_pose_giribet_2017]\] \[[Prochazka and Stomberg 2020][research_prochazka_stomberg_2020]\] \[[Prochazka et al 2018][research_prochazka_eduardo_2018]\] \[[Raza and Silverthorn 1985][research_raza_silverthorn_1985]\] \[[Sagan et al 2021][research_sagan_krishnamurthy_2021]\] \[[Santos et al 2022][research_santos_honorio_2022]\] \[[Scordamaglia et al 2025][research_scordamaglia_mattei_2025]\] \[[Shearwood et al 2020][research_shearwood_nabawy_2020]\] \[[Shearwood et al 2020][research_shearwood_nabawy_2020_b]\] \[[Shearwood et al 2021][research_shearwood_nabawy_2021]\] \[[Shuo et al 2025][research_shuo_tuan_2025]\] \[[Singh et al 2024][research_singh_lambeth_2024]\] \[[Sisson and Dogan 2025][research_sisson_dogan_2025]\] \[[Sisson et al 2024][research_sisson_sarioglu_2024]\] \[[Spaans et al 2024][research_spaans_gilbert_2024]\] \[[Stam and de Visser 2025][research_stam_devisser_2025]\] \[[Su et al 2022][research_su_chu_2022]\] \[[Theilliol et al 2015][research_theilliol_weber_2015]\] \[[Tohidi et al 2017][research_tohidi_yildiz_2017]\] \[[Tohidi et al 2021][research_tohidi_yildiz_2021]\] \[[Tsagkaris et al 2026][research_tsagkaris_holzapfel_2026]\] \[[Venkataraman and Doman 2001][research_venkataraman_doman_2001]\] \[[Vepa 2021][research_vepa_2021]\] \[[Vernyi et al 2026][research_vernyi_stanko_2026]\] \[[Vile et al 2020][research_vile_alwi_2020]\] \[[Virnig and Bodden 1994][research_virnig_bodden_1994]\] \[[Wahler et al 2023][research_wahler_varriale_2023]\] \[[Wang and Zhang 2022][research_wang_zhang_2022]\] \[[Wang et al 2020][research_wang_zhu_2020]\] \[[Wang Fawei 2016][research_wangfawei_2016]\] \[[Wu et al 2026][research_wu_lian_2026]\] \[[Yan and Shi 2024][research_yan_shi_2024]\] \[[Yiming et al 2019][research_yiming_mei_2019]\] \[[Yin et al 2019][research_yin_chu_2019]\] \[[Yılmaz and German 2024][research_yilmaz_german_2024]\] \[[Zhou et al 2015][research_zhou_canova_2015]\] \[[Zhou et al 2016][research_zhou_canova_2016]\]

**Of the 90 records, 6 date from 1997 or earlier and 71 from 2015 or later.** Among their titles, 18 name a multirotor, tilt-rotor or vertical take-off vehicle and 9 name a tailless aircraft or flying wing.

### Flight dynamics, stability derivatives and unstable modes

Flight dynamics, stability derivatives and the modes of motion, including the unstable and inertia-coupled ones.

**83 records.** \[[Addington 2000][research_addington_2000]\] \[[Ajaj 2021][research_ajaj_2021]\] \[[Ananthkrishnan and Sudhakar 1994][research_ananthkrishnan_sudhakar_1994]\] \[[Ananthkrishnan and Sudhakar 1995][research_ananthkrishnan_sudhakar_1995]\] \[[Beaufrere 1986][research_beaufrere_1986]\] \[[Been et al 2018][research_been_kang_2018]\] \[[Biber 2015][research_biber_2015]\] \[[Bird 1970][research_bird_1970]\] \[[Campos 1989][research_campos_1989]\] \[[Coulter and Marquart 1982][research_coulter_marquart_1982]\] \[[Curtiss and Zhao 1988][research_curtisshc_zhaoxin_1988]\] \[[Czaykowski 1958][research_czaykowski_1958]\] \[[Dat et al 2018][research_dat_son_2018]\] \[[Dhiman et al 2022][research_dhiman_abhishek_2022]\] \[[Dr. Olivia Davis 2021][research_droliviadavis_2021]\] \[[Elliott et al 2025][research_elliott_saj_2025]\] \[[Ericsson 1980][research_ericsson_1980]\] \[[Ferguson and Thomson 2015][research_ferguson_thomson_2015]\] \[[Foster and Hartman 2017][research_foster_hartman_2017]\] \[[Gan et al 2021][research_gan_botre_2021]\] \[[Gao et al 2020][research_gao_liu_2020]\] \[[Gao et al 2022][research_gao_shi_2022]\] \[[Goetzendorf-Grabowski and Kwiek 2023][research_goetzendorfgrabowski_kwiek_2023]\] \[[Hacker 1977][research_hacker_1977]\] \[[Horst et al 2017][research_horst_sommerwerk_2017]\] \[[Humphreys and Watkinson 1972][research_humphreys_watkinson_1972]\] \[[Hyde et al 2014][research_hydedavidc_shweykkamalm_2014]\] \[[Foster and Hartman 2017][research_johnvfoster_davidchartman_2017]\] \[[Juhasz et al 2022][research_juhasz_celi_2022]\] \[[Junior Kuitche et al 2024][research_juniorkuitche_yanezbadillo_2024]\] \[[Klauck and Keßler 2025][research_klauck_kessler_2025]\] \[[Klein 1977][research_klein_1977]\] \[[Klein et al 1982][research_kleinrw_lapinsm_1982]\] \[[Kogler and Quam 1983][research_kogler_quam_1983]\] \[[Koryanov and Kukharenko 2023][research_koryanov_kukharenko_2023]\] \[[Krishnamurthy and Luckner 2017][research_krishnamurthy_luckner_2017]\] \[[Laitone and Lin 1972][research_laitone_lin_1972]\] \[[Laitone and Lin 1973][research_laitone_lin_1973]\] \[[Lapins et al 1982][research_lapinsm_kleinrw_1982]\] \[[Laudeman 1972][research_laudeman_1972]\] \[[Lee et al 2021][research_lee_kim_2021]\] \[[Lessing and Butler 1959][research_lessinghenryc_butlerjamesk_1959]\] \[[Leylek and Costello 2015][research_leylek_costello_2015]\] \[[Liu et al 2026][research_liu_li_2026]\] \[[Lueckhof and Stumpf 2018][research_lueckhof_stumpf_2018]\] \[[Lytovchenko 2026][research_lytovchenko_2026]\] \[[Masak 1965][research_masak_1965]\] \[[Montalvo and Costello 2015][research_montalvo_costello_2015]\] \[[Mukai and Hunter 1996][research_mukai_hunter_1996]\] \[[Mukherjee and Sinha 2016][research_mukherjee_sinha_2016]\] \[[Munk 1922][research_munkmaxm_1922]\] \[[Pagliuca and Timme 2016][research_pagliuca_timme_2016]\] \[[Perry 1976][research_perrybiii_1976]\] \[[Phillips and Santana 2002][research_phillips_santana_2002]\] \[[Potvin and Grant 2026][research_potvin_grant_2026]\] \[[Qiu and Gourishankar 1984][research_qiu_gourishankar_1984]\] \[[Quitter et al 2021][research_quitter_marino_2021]\] \[[Rampy 1966][research_rampy_1966]\] \[[Rising et al 1984][research_risingjj_daviswj_1984]\] \[[Roberts et al 1977][research_robertspa_swaimrl_1977]\] \[[Rodden and Giesing 1970][research_rodden_giesing_1970]\] \[[Rooney et al 1982][research_rooneyrh_chungjc_1982]\] \[[Rosario-Gabriel and Cortes 2018][research_rosariogabriel_cortes_2018]\] \[[Schiff 1971][research_schiff_1971]\] \[[Schwanz 1972][research_schwanz_1972]\] \[[Shayak et al 2024][research_shayak_girdhar_2024]\] \[[Shi and Wan 2015][research_shi_wan_2015]\] \[[Shrivastava and Stengel 1989][research_shrivastava_stengel_1989]\] \[[Sizlo et al 1979][research_sizlotr_bergra_1979]\] \[[Sliwa 1980][research_sliwasm_1980]\] \[[Sparavalo 2021][research_sparavalo_2021]\] \[[Spearman 1979][research_spearmanml_1979]\] \[[Suryakumar et al 2016][research_suryakumar_babbar_2016]\] \[[Swaim 1977][research_swaim_1977]\] \[[Theodore and Celi 2002][research_theodore_celi_2002]\] \[[Tran and Sawan 1983][research_tran_sawan_1983]\] \[[Tzafestas 1975][research_tzafestas_1975]\] \[[Uribe Quintero et al 2024][research_uribequintero_takahashi_2024]\] \[[Wang et al 2019][research_wang_yuan_2019]\] \[[Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]\] \[[Wu et al 2016][research_wu_chen_2016]\] \[[Yedavalli 2024][research_yedavalli_2024]\] \[[Yuan et al 2020][research_yuan_thomson_2020]\]

### Turbofan performance, thrust and fuel consumption

Turbofan and small gas turbine performance, thrust and fuel consumption, and engine control.

**80 records.** \[[Akagi et al 1997][research_akagi_shinomiya_1997]\] \[[Andersen and Bagby 1965][research_andersen_bagby_1965]\] \[[Bartlett and Turner 1975][research_bartlett_turner_1975]\] \[[Bennett et al 2024][research_bennett_chapman_2024]\] \[[Burnell et al 1973][research_burnell_morrison_1973]\] \[[Campbell 1973][research_campbell_1973]\] \[[Campbell 1974][research_campbell_1974]\] \[[Chamberlain 1968][research_chamberlain_1968]\] \[[Chamberlin and Miller 1979][research_chamberlin_miller_1979]\] \[[Coalson 1968][research_coalson_1968]\] \[[Coalson 1982][research_coalson_1982]\] \[[Coalson and Csavina 1975][research_coalson_csavina_1975]\] \[[Collins 1982][research_collins_1982]\] \[[Connolly et al 2017][research_connolly_csank_2017]\] \[[Connolly et al 2016][research_connollyjosephw_csankjeffreyt_2016]\] \[[Csavina 1976][research_csavina_1976]\] \[[Cui et al 2024][research_cui_bai_2024]\] \[[Dean 1978][research_dean_1978]\] \[[Dik et al 2017][research_dik_biten_2017]\] \[[Drell 1965][research_drell_1965]\] \[[Effects of Reynolds number and other parameters on the throttle-dependent, nozzle/afterbody drag of an 0.11 scale single-engine aircraft model 1979][research_effects_of_1979]\] \[[Evans and Chamblee 1966][research_evans_chamblee_1966]\] \[[Evans 1991][research_evansalisonb_1991]\] \[[Filinov and Ostapyuk 2019][research_filinov_ostapyuk_2019]\] \[[Filinov et al 2020][research_filinov_tkachenko_2020]\] \[[Gagg 1937][research_gagg_1937]\] \[[Guo et al 2024][research_guo_zhang_2024]\] \[[Hines and Gaffin 1976][research_hines_gaffin_1976]\] \[[Hunt and Gowadia 1981][research_hunt_gowadia_1981]\] \[[Identification method of temperature corrections to aircraft engine thrust in flight tests 2023][research_identification_method_2023]\] \[[Jameson 2009][research_jameson_2009]\] \[[Kadosh and Cukurel 2016][research_kadosh_cukurel_2016]\] \[[Kashikawa et al 1995][research_kashikawa_akagi_1995]\] \[[Kauser and Burcham 2001][research_kauser_burcham_2001]\] \[[Kc et al 2019][research_kc_ngo_2019]\] \[[Khalid 2016][research_khalid_2016]\] \[[Khalid 2017][research_khalid_2017]\] \[[Kingcombe and Dunning 1980][research_kingcombe_dunning_1980]\] \[[Lacaille and Loro 2016][research_lacaille_loro_2016]\] \[[Lecuyer 1970][research_lecuyer_1970]\] \[[Liew et al 2005][research_liewkh_uripe_2005]\] \[[Liew et al 2005][research_liewkh_uripe_2005_b]\] \[[Liew et al 2005][research_liewkh_uripe_2005_c]\] \[[Lin and Yeh 1999][research_lin_yeh_1999]\] \[[Lind and Protopapas 1977][research_lind_protopapas_1977]\] \[[Ling 1983][research_ling_1983]\] \[[Liu and Sirignano 2000][research_liu_sirignano_2000]\] \[[Loro and Lacaille 2017][research_loro_lacaille_2017]\] \[[Magrini et al 2021][research_magrini_buosi_2021]\] \[[Mattingly 1998][research_mattingly_1998]\] \[[McGuigan 1970][research_mcguigan_1970]\] \[[Mehalic and Ziemianski 1980][research_mehaliccm_ziemianskija_1980]\] \[[Miao et al 2020][research_miao_wang_2020]\] \[[Tong 2020][research_michaelttong_2020]\] \[[Miller and Hackney 1976][research_miller_hackney_1976]\] \[[Motycka and Skowronek 1968][research_motycka_skowronek_1968]\] \[[Neal and Sengupta 1989][research_nealbradford_senguptaupal_1989]\] \[[Olsson 1982][research_olsson_1982]\] \[[Palacios et al 1998][research_palacios_owens_1998]\] \[[Price and Glidewell 1981][research_pricejr_glidewell_1981]\] \[[Ramdin et al 2023][research_ramdin_visser_2023]\] \[[Roth and Mavris 2001][research_roth_mavris_2001]\] \[[Schmidt 1985][research_schmidt_1985]\] \[[Sens 1978][research_sens_1978]\] \[[Shmelоv et al 2019][research_shmelv_vladov_2019]\] \[[Shufan et al 2017][research_shufan_heng_2017]\] \[[Singh 1986][research_singhb_1986]\] \[[Sowers and Tabakoff 1983][research_sowers_tabakoff_1983]\] \[[Srivastava and Duraisamy 2018][research_srivastava_duraisamy_2018]\] \[[Subagyo 2019][research_subagyo_2019]\] \[[Tate and Gillard 1975][research_tate_gillard_1975]\] \[[Tich et al 1987][research_tich_shaw_1987]\] \[[Van Der Hoeven 1981][research_vanderhoeven_1981]\] \[[Wills and Wise 1976][research_wills_wise_1976]\] \[[Xu 2025][research_xu_2025]\] \[[Zagranski et al 1974][research_zagranski_lamart_1974]\] \[[Zeller et al 1982][research_zellerj_lehtinenb_1982]\] \[[Zhai et al 2025][research_zhai_li_2025]\] \[[Ziemianski 1981][research_ziemianskija_1981]\] \[[Zimbelman and Rouser 2025][research_zimbelman_rouser_2025]\]

### Computational aerodynamics, surrogate models and uncertainty

Computational aerodynamics, surrogate models, machine learning of aerodynamic data and uncertainty quantification.

**77 records.** \[[Abe 1993][research_abe_1993]\] \[[Abras et al 2023][research_abras_tuckey_2023]\] \[[Alhazmi et al 2021][research_alhazmi_ghazi_2021]\] \[[Ashton 2017][research_ashton_2017]\] \[[Asouti et al 2023][research_asouti_kontou_2023]\] \[[Asztalos et al 2026][research_asztalos_salucci_2026]\] \[[Atmaja et al 2023][research_atmaja_fajar_2023]\] \[[Bidar et al 2024][research_bidar_he_2024]\] \[[Bobrowski et al 2016][research_bobrowski_barnewitz_2016]\] \[[Brown 2025][research_brown_2025]\] \[[Burchett 2023][research_burchett_2023]\] \[[Burchett and Bryson 2025][research_burchett_bryson_2025]\] \[[Burrows and Allaire 2019][research_burrows_allaire_2019]\] \[[Cai et al 2026][research_cai_fan_2026]\] \[[Cakici and Yörük 2022][research_cakici_yoruk_2022]\] \[[Campbell et al 2026][research_campbell_mulani_2026]\] \[[Chen 2026][research_chen_2026]\] \[[Chen et al 2026][research_chen_huang_2026]\] \[[Dupuis et al 2018][research_dupuis_jouhaud_2018]\] \[[Eldredge and Mousavi 2026][research_eldredge_mousavi_2026]\] \[[Eriş et al 2026][research_eris_ozgoren_2026]\] \[[Feldwisch 2026][research_feldwisch_2026]\] \[[Gao et al 2015][research_gao_wang_2015]\] \[[Hasan et al 2025][research_hasan_redonnet_2025]\] \[[Iyengar and Mavris 2025][research_iyengar_mavris_2025]\] \[[Jo et al 2018][research_jo_choi_2018]\] \[[Jung and Baeder 2023][research_jung_baeder_2023]\] \[[Karali et al 2020][research_karali_demirezen_2020]\] \[[Kiely and Agarwal 2023][research_kiely_agarwal_2023]\] \[[Kikuchi et al 2016][research_kikuchi_misaka_2016]\] \[[Kirsch et al 2025][research_kirsch_fathi_2025]\] \[[Lakkur et al 2025][research_lakkur_schmidt_2025]\] \[[Liem et al 2015][research_liem_mader_2015]\] \[[Lin 2025][research_lin_2025]\] \[[Liu et al 2017][research_liu_litvinenko_2017]\] \[[Liu et al 2023][research_liu_zhang_2023]\] \[[Liu et al 2025][research_liu_zhang_2025]\] \[[Liu et al 2026][research_liu_wang_2026]\] \[[Long 2016][research_long_2016]\] \[[Long 2016][research_long_2016_b]\] \[[Lyu et al 2024][research_lyu_sun_2024]\] \[[Mar Aye et al 2020][research_maraye_pholdee_2020]\] \[[Michal 1998][research_michaltoddr_1998]\] \[[Ni et al 2024][research_ni_chen_2024]\] \[[Nieto-Centenero et al 2024][research_nietocentenero_martinezcava_2024]\] \[[Nikolaou et al 2025][research_nikolaou_kilimtzidis_2025]\] \[[Ong and Chan 2016][research_ong_chan_2016]\] \[[Othman and Kanazaki 2015][research_othman_kanazaki_2015]\] \[[Othman and Kanazaki 2015][research_othman_kanazaki_2015_b]\] \[[Pagliuca and Timme 2017][research_pagliuca_timme_2017]\] \[[Papoutsis-Kiachagias et al 2021][research_papoutsiskiachagias_asouti_2021]\] \[[Qin 2026][research_qin_2026]\] \[[Renard and Deck 2015][research_renard_deck_2015]\] \[[Rosić and Diekmann 2015][research_rosic_diekmann_2015]\] \[[Schaefer et al 2019][research_schaefer_cary_2019]\] \[[Schaefer et al 2024][research_schaefer_bekemeyer_2024]\] \[[Schnell 2023][research_schnell_2023]\] \[[Sharma and Hosder 2021][research_sharma_hosder_2021]\] \[[Song et al 2016][research_song_han_2016]\] \[[Stoldt et al 2021][research_stoldt_korobenko_2021]\] \[[Stradtner and Bekemeyer 2025][research_stradtner_bekemeyer_2025]\] \[[Suga and Yamazaki 2015][research_suga_yamazaki_2015]\] \[[Sun et al 2022][research_sun_sengupta_2022]\] \[[Sung et al 2025][research_sung_spreizer_2025]\] \[[Taylor 2015][research_taylor_2015]\] \[[Valasek and Chakravorty 2015][research_valasek_chakravorty_2015]\] \[[Wang 2025][research_wang_2025]\] \[[Wang 2025][research_wang_2025_b]\] \[[Wang et al 2024][research_wang_xu_2024]\] \[[Way et al 2026][research_way_sescu_2026]\] \[[West and Phillips 2020][research_west_phillips_2020]\] \[[West et al 2017][research_west_reuter_2017]\] \[[Yan and Shi 2025][research_yan_shi_2025]\] \[[Yang and Yee 2022][research_yang_yee_2022]\] \[[Yondo et al 2018][research_yondo_andres_2018]\] \[[Zhang et al 2024][research_zhang_xu_2024]\] \[[Zimmnau et al 2025][research_zimmnau_cremer_2025]\]

### Radar signature and low observability

Radar cross section and low observability of aircraft and unmanned aircraft, the consideration that made the vertical tail a liability.

**66 records.** \[[Abdullah and Miao 2026][research_abdullah_miao_2026]\] \[[Abdullah et al 2025][research_abdullah_kashif_2025]\] \[[Altman 2008][research_altman_2008]\] \[[Aronstein 1996][research_aronstein_1996]\] \[[Ashraf et al 2018][research_ashraf_tabassum_2018]\] \[[Brown 1993][research_brown_1993]\] \[[Chen et al 2015][research_chen_yue_2015]\] \[[Chung and Tuan 2021][research_chung_tuan_2021]\] \[[Correa et al 1981][research_correa_sengupta_1981]\] \[[Dybdal 1987][research_dybdal_1987]\] \[[Edefur and Tormalm 2018][research_edefur_tormalm_2018]\] \[[Fry 2008][research_fry_2008]\] \[[Garretson 1986][research_garretsoniii_1986]\] \[[Guay et al 2017][research_guay_drolet_2017]\] \[[Guo et al 2018][research_guo_lin_2018]\] \[[Jeong et al 2018][research_jeong_park_2018]\] \[[Kao and Anderson 1981][research_kao_anderson_1981]\] \[[Kurbanismailov et al 2021][research_kurbanismailov_tarlanov_2021]\] \[[Lee 2024][research_lee_2024]\] \[[Liu et al 2017][research_liu_huang_2017]\] \[[Lowry et al 1978][research_lowry_rich_1978]\] \[[Mahulikar et al 2022][research_mahulikar_rastogi_2022]\] \[[Mammadova et al 2025][research_mammadova_slavov_2025]\] \[[Marvasti and Boutayeb 2024][research_marvasti_boutayeb_2024]\] \[[Nam 2026][research_nam_2026]\] \[[Norsell 2003][research_norsell_2003]\] \[[Ozdemir et al 2024][research_ozdemir_kucuk_2024]\] \[[Papageorgiou et al 2018][research_papageorgiou_tarkian_2018]\] \[[Persson 2017][research_persson_2017]\] \[[Persson and Bull 2016][research_persson_bull_2016]\] \[[Piccirillo 1996][research_piccirillo_1996]\] \[[Queen 1976][research_queen_1976]\] \[[Radar cross section fundamentals for the aircraft designer 1979][research_radar_cross_1979]\] \[[Sai Teja et al 2017][research_saiteja_vaghela_2017]\] \[[Sepulveda Palacios and Smith 2019][research_sepulvedapalacios_smith_2019]\] \[[Siegel 1961][research_siegel_1961]\] \[[Sijabat and Indriyanto 2021][research_sijabat_indriyanto_2021]\] \[[Silva et al 2026][research_silva_souza_2026]\] \[[Steinberg et al 1989][research_steinberg_carlson_1989]\] \[[Taj et al 2023][research_taj_bilal_2023]\] \[[Tarlanov and Kurbanismailov 2021][research_tarlanov_kurbanismailov_2021]\] \[[Trueman et al 1993][research_trueman_kubina_1993]\] \[[Tsai et al 2016][research_tsai_chiang_2016]\] \[[Tusa et al 2015][research_tusa_nicolaescu_2015]\] \[[van Schalkwyk and Smit 2017][research_vanschalkwyk_smit_2017]\] \[[Vogel 2016][research_vogel_2016]\] \[[Vogel and Junqueira 2017][research_vogel_junqueira_2017]\] \[[Wang et al 2022][research_wang_ye_2022]\] \[[Wang et al 2025][research_wang_pei_2025]\] \[[Wang et al 2025][research_wang_yang_2025_b]\] \[[Wang et al 2026][research_wang_huang_2026]\] \[[Woods et al 1996][research_woods_sillence_1996]\] \[[Wright 1975][research_wright_1975]\] \[[Xiaofeng Ai et al 2016][research_xiaofengai_fengzhao_2016]\] \[[Xu et al 2020][research_xu_ge_2020]\] \[[Yang 2024][research_yang_2024]\] \[[Zhang et al 2023][research_zhang_jiang_2023]\] \[[Zhang et al 2026][research_zhang_yang_2026]\] \[[Zhou and Huang 2021][research_zhou_huang_2021]\] \[[Zhou and Huang 2021][research_zhou_huang_2021_c]\] \[[Zhou and Huang 2022][research_zhou_huang_2022_b]\] \[[Zhou and Huang 2022][research_zhou_huang_2022_c]\] \[[Zhou and Huang 2023][research_zhou_huang_2023]\] \[[Zhou and Huang 2023][research_zhou_huang_2023_b]\] \[[Zhou et al 2021][research_zhou_huang_2021_b]\] \[[Özdemi̇r 2020][research_ozdemir_2020]\]

### Turn performance, agility and manoeuvre

Turn performance, agility, energy manoeuvrability and the manoeuvre performance that thrust vectoring changes.

**51 records.** \[[Altunkaya and Özkol 2025][research_altunkaya_ozkol_2025]\] \[[Beck and Cord 1995][research_beck_cord_1995]\] \[[Boppe and Martorella 1992][research_boppe_martorella_1992]\] \[[Bryson et al 1969][research_bryson_desai_1969]\] \[[Bryson and Desai 1968][research_brysonjr_desai_1968]\] \[[Caddy and Arnold 1988][research_caddy_arnold_1988]\] \[[Denham et al 2022][research_caseyldenham_mayureshpatil_2022]\] \[[Cecen 2021][research_cecen_2021]\] \[[Chakraborty and Mishra 2021][research_chakraborty_mishra_2021]\] \[[Costes 1988][research_costes_1988]\] \[[Cramer 1995][research_cramer_1995]\] \[[Dwyer and Lutze 1993][research_dwyer_lutze_1993]\] \[[Foss 1944][research_foss_1944]\] \[[Gal-Or 1992][research_galor_1992]\] \[[Gal-Or and Baumann 1993][research_galor_baumann_1993]\] \[[Gomes and Suleman 2004][research_gomes_suleman_2004]\] \[[Hoffman and Stalford 1991][research_hoffman_stalford_1991]\] \[[Incorporating agility flight test metrics concurrently into the aircraft preliminary design process 1994][research_incorporating_agility_1994]\] \[[Johnson 1972][research_johnson_1972]\] \[[Kimberlin 2001][research_kimberlin_2001]\] \[[Kutschera and Render 1999][research_kutschera_render_1999]\] \[[Landgraf 1964][research_landgraf_1964]\] \[[Landgraf 1965][research_landgraf_1965]\] \[[Langan and Samuels 1995][research_langan_samuels_1995]\] \[[Lee and Lan 1992][research_lee_lan_1992]\] \[[Loh and Lusty 1974][research_loh_lustyjr_1974]\] \[[Manolescu 1994][research_manolescu_1994]\] \[[Mazza 1992][research_mazza_1992]\] \[[Montgomery et al 1998][research_montgomeryraymondc_scottmichaela_1998]\] \[[Moroney et al 1979][research_moroney_pruitt_1979]\] \[[Morris and Kroo 1990][research_morris_kroo_1990]\] \[[Papadales and Basil S. 1979][research_papadales_basils_1979]\] \[[Paranjape and Ananthkrishnan 2023][research_paranjape_ananthkrishnan_2023]\] \[[Rajeswari and Prabhu 1987][research_rajeswari_prabhu_1987]\] \[[Rutowski 1954][research_rutowski_1954]\] \[[Ryan and Downing 1993][research_ryangeorgewiii_downingdavidr_1993]\] \[[Sanders 1997][research_sanders_1997]\] \[[Schairer 1964][research_schairer_1964]\] \[[Schrage 1990][research_schrage_1990]\] \[[Schultz and Zagalsky 1972][research_schultz_zagalsky_1972]\] \[[Stalford and Hoffman 1989][research_stalford_hoffman_1989]\] \[[Stanley 1980][research_stanley_1980]\] \[[Tamboli 1956][research_tamboli_1956]\] \[[Tamrat 1988][research_tamrat_1988]\] \[[Tomczyk 1998][research_tomczyk_1998]\] \[[Valasek and Downing 1993][research_valasekjohn_downingdavidr_1993]\] \[[Wang et al 2020][research_wang_wang_2020_b]\] \[[Warren 1990][research_warren_1990]\] \[[Wilson et al 1993][research_wilson_riley_1993]\] \[[Wittenberg 2001][research_wittenberg_2001]\] \[[Yajnik 1977][research_yajnik_1977]\]

### Flight simulation and simulators

Flight simulation and simulators, ground-based and in flight, including the visual and motion cues a ground pilot receives.

**29 records.** \[[Aume et al 1976][research_aume_mills_1976]\] \[[Benyamen et al 2023][research_benyamen_mays_2023]\] \[[Bezdek 1995][research_bezdek_1995]\] \[[Carter 1988][research_carter_1988]\] \[[Chetty and Henschel 1987][research_chetty_henschel_1987]\] \[[Cooksey et al 1964][research_cooksey_dillenschneider_1964]\] \[[Ebeling 1969][research_ebeling_1969]\] \[[Fuad et al 2024][research_fuad_matute_2024]\] \[[Gu 2025][research_gu_2025]\] \[[Gundry 1977][research_gundry_1977]\] \[[Huang et al 2017][research_huang_pool_2017]\] \[[Huguenin 1981][research_huguenin_1981]\] \[[Ivan 1985][research_ivan_1985]\] \[[Jansen 1980][research_jansen_1980]\] \[[Litt et al 2012][research_littjonathans_sowerst_2012]\] \[[Liu et al 2015][research_liu_wang_2015]\] \[[Morlang and Strassburger 2025][research_morlang_strassburger_2025]\] \[[Motyka 1975][research_motyka_1975]\] \[[Motyka and Reynolds 1971][research_motyka_reynolds_1971]\] \[[Nonlinear model following control application to a flight simulator control loader 1989][research_nonlinear_model_1989]\] \[[Research and Analysis on Development and Flight Test of Military Aircraft Flight Simulator 2022][research_research_and_2022]\] \[[Roganov et al 2017][research_roganov_roganova_2017]\] \[[Sarathy and Murthy 1993][research_sarathy_murthy_1993]\] \[[Sarrafian 1984][research_sarrafian_1984]\] \[[Sarrafian 1986][research_sarrafian_1986]\] \[[Shlien 1991][research_shlien_1991]\] \[[Stortz and ODonoghue 1995][research_stortzmichaelw_odonoghuedennisp_1995]\] \[[Wortman et al 1975][research_wortman_duket_1975]\] \[[Yifei et al 2015][research_yifei_zongxia_2015]\]

### Mass properties and moments of inertia

Mass properties and the measurement and estimation of moments of inertia of aircraft, missiles and test articles.

**23 records.** \[[Aircraft moments of inertia 1996][research_aircraft_moments_1996]\] \[[Alyshev et al 2016][research_alyshev_melnikov_2016]\] \[[Chai et al 1995][research_chai_crisafulli_1995]\] \[[Chin et al 2015][research_chinalexanderw_herreraclaudiay_2015]\] \[[Chin et al 2015][research_chinalexanderw_herreraclaudiay_2015_b]\] \[[Dantsker et al 2018][research_dantsker_vahora_2018]\] \[[Green 1958][research_green_1958]\] \[[Hou et al 2011][research_hou_xue_2011]\] \[[Jardin and Mueller 2009][research_jardin_mueller_2009]\] \[[Malaek and Soltan-Mohammed 2001][research_malaek_soltanmohammed_2001]\] \[[Martin and Lind 2025][research_martin_lind_2025]\] \[[Morelli 2021][research_morelli_2021_b]\] \[[Morelli 2022][research_morelli_2022]\] \[[Napolitano et al 2024][research_napolitano_kerrian_2024]\] \[[Pal and Gaberson 1973][research_pal_gaberson_1973]\] \[[Patera 1981][research_patera_1981]\] \[[Peterson 2004][research_petersonwaynel_2004]\] \[[Schwartz et al 1957][research_schwartz_malick_1957]\] \[[Setati et al 2022][research_setati_botha_2022]\] \[[Simmons et al 2023][research_simmons_gresham_2023_c]\] \[[Simmons et al 2023][research_simmons_gresham_2023_d]\] \[[Swank 2012][research_swankaaronj_2012]\] \[[Wickman 1953][research_wickman_1953]\]

### The X-36, X-29 and X-31 demonstrators

The aircraft's own record, and that of the X-29 and X-31, the two flight-control demonstrators this article sets beside it.

**21 records.** \[[Bosworth and Cox 1989][research_bosworth_cox_1989]\] \[[Bosworth and Stoliker 1996][research_bosworthjohnt_stolikerpc_1996]\] \[[Brinker and Wise 2000][research_brinker_wise_2000]\] \[[Brinker and Wise 2001][research_brinker_wise_2001]\] \[[Calise 2000][research_calise_2000]\] \[[Fratello et al 1987][research_fratellodavidj_croommarka_1987]\] \[[Harris and Harris 1997][research_harris_harris_1997]\] \[[Hicks and Matheny 1989][research_hicksjohnw_mathenyneilw_1989]\] \[[Huber 1995][research_huber_1995]\] \[[Huber and Schellenger 1994][research_huberpeter_schellengerharveyg_1994]\] \[[Ishmael and Wierzbanowski 1985][research_ishmaelsd_wierzbanowskit_1985]\] \[[Kaletka and Fu 1993][research_kaletka_fu_1993]\] \[[Klafin 1988][research_klafin_1988]\] \[[Putnam et al 1986][research_putnamtw_petersenkl_1986]\] \[[Smith and Schroeder 1986][research_smithrogerse_schroederkurtc_1986]\] \[[Tamrat 2004][research_tamrat_2004]\] \[[Trippensee 1991][research_trippenseegary_1991]\] \[[Voracek and Clarke 1994][research_voracek_clarke_1994]\] \[[Walker 1997][research_walkerlaurencea_1997]\] \[[Whiting 1996][research_whitingmatthewrobert_1996]\] \[[X-29 Research Aircraft 1991][research_x_29_research_1991]\]

**Of the 21 records, 5 titles name the X-36, published from 1997 to 2001, and one of them is a report primary.**

### The viscosity of air and Sutherland's law

The viscosity of air and other gases and its variation with temperature, which Sutherland's law expresses and the Reynolds number computation uses.

**18 records.** \[[Bond 1936][research_bond_1936]\] \[[Edwards and Rankine 1927][research_edwards_rankine_1927]\] \[[Gupta et al 1991][research_guptaroopn_leekampui_1991]\] \[[Hansen 1959][research_hansencfrederick_1959]\] \[[Harrington 1939][research_harrington_1939]\] \[[Holman 1876][research_holman_1876]\] \[[Holman 1885][research_holman_1885]\] \[[Houston 1937][research_houston_1937]\] \[[Kellström 1936][research_kellstrom_1936]\] \[[Keyes 1927][research_keyes_1927]\] \[[McInally 1963][research_mcinally_1963]\] \[[Nadi and Zeid 1955][research_nadi_zeid_1955]\] \[[Palmer and Wright 2002][research_palmer_wright_2002]\] \[[Rigden 1938][research_rigden_1938]\] \[[Sutherland and Maass 1932][research_sutherland_maass_1932]\] \[[Viegas and Howe 1962][research_viegasjohnr_howejohnt_1962]\] \[[Williams 1926][research_williams_1926]\] \[[Williamson 1951][research_williamson_1951]\]

**None of the 18 records is later than 2002**, which is the shape a settled subject takes.

### Fighter and technology demonstrator programmes

Fighter and technology demonstrator programmes, their conduct, flight testing and lessons.

**12 records.** \[[Andrews et al 1980][research_andrewswh_simag_1980]\] \[[Aulehla and Kissel 1981][research_aulehla_kissel_1981]\] \[[Aulehla and Kissel 1982][research_aulehla_kissel_1982]\] \[[Bailey et al 2020][research_bailey_williams_2020]\] \[[Borer et al 2019][research_borer_cox_2019]\] \[[Borer et al 2024][research_borer_reynolds_2024]\] \[[Brown et al 2026][research_brown_hoover_2026]\] \[[Filippoli et al 2026][research_filippoli_perri_2026]\] \[[Kramer et al 2018][research_kramer_williams_2018]\] \[[Lorell 1989][research_lorell_1989]\] \[[Nicholson 1985][research_nicholson_1985]\] \[[Veletas 2026][research_veletas_2026]\]

## Where the Framing Breaks Down

### The Article Leans Hard on Idealised Similitude

**The scaling argument in this article assumes idealised similitude, and real models depart from it.**
Matching the mass ratio exactly requires matching the inertia ratio too, which means placing the mass
correctly in three axes and not merely getting the total right. Whether the X-36 did so is not in the public
record.
**If its inertias were not scaled, the doubling times computed above are wrong by whatever factor the inertia is wrong by**,
and the article's bracket across radius of gyration is an admission of that rather than a resolution of
it.

### The Latency Argument Has No Measurement Behind It

**The structure of the latency argument is sound and its magnitude is unknown.** The amplification factor of
1.8898 is exact and follows from the scale factor alone. **The thing being amplified is not published.** If
the link delay was very small then the handicap was small, and the article's claim reduces to a statement
about a multiplier rather than about a difficulty.

**The claim is therefore made in that weaker form**, and no assertion is made that the pilot found
the delay hard, because the published ratings do not isolate it. [Walker 1997][research_walkerlaurencea_1997] reports Cooper-Harper
ratings of 4 for pitch attitude capture and 3 for bank angle capture in the first phase, Level 1 handling
qualities in all axes in the second, and that considerable pilot attention was required.

### The Instability May Have Been Milder Than Assumed

The directional derivative used above is assumed rather than measured, at a value typical of a tailless
configuration. **A less unstable aircraft would double more slowly and the whole argument would soften.**
The bracket across radius of gyration does not cover this, because a different derivative scales the growth
rate rather than the inertia, and the article flags it as the assumption its sharpest number is most exposed
to.

### The Comparison With the Previous Article Is Neat and Should Be Distrusted for It

**Two consecutive demonstrators, one flown easier than the real thing and one flown harder, is a pleasing symmetry.**
It is also the kind of pattern that appears when one goes looking for it.
**The X-35 comparison rests on weights and an ordering, which are published. The X-36 comparison rests on a scaling law, which is exact, applied to a latency that is not published.**
Those are not equally solid, and they are not presented here as though they were.

## The Source Base

**The aircraft's own record is thin and the record of its methods is deep.** The vehicle facts come from the
[programme account][ref_nasa_x36], the [published specification][ref_x36] and the
[inventory of American X-vehicles][ref_american_x_vehicles], which disagree on the size of the programme and
are reported side by side where they do. The flight-control literature of the programme, the papers on the
reconfigurable control law flown in 1998, and the subsystems and test-pilot papers of 1997 are surveyed in
the cluster on the X-36, X-29 and X-31 demonstrators.

**No latency figure for the command and video link is public**, which is the quantity the article's sharpest
argument would most like to have. **Only envelope maxima of angle of attack are public**, 40 degrees in the
programme account and 35 degrees for turning and rolling manoeuvres in the inventory of American X-vehicles,
and what is public from high angles of attack is pilot ratings and a normalised roll-time plot reaching a little
above 30 degrees in [Walker 1997][research_walkerlaurencea_1997], with no time history, though that is what the tailless argument turns on.
**No moment of inertia, no stability derivative and no wing area is public**, so three of the numbers in the
sizing section are inversions or brackets rather than readings, and each says so where it stands.
**The fuselage volume the slender-body derivation needs is not public either**, and neither is the drag
increment of the split ailerons, which is why the conclusion about them flips inside its own bracket.

The following books and monographs supplied the standing theory, and almost none of them concerns this
aircraft, covering stability and control, flight dynamics, similitude, flight test method and the control
literature the adaptive work drew on.

- [Aerodynamics of the airplane][book_clarkbmillikan_1941]
- [Aerodynamics for model aircraft][book_avrumzier_1942]
- [Some properties and control problems of tailless aircraft][book_jmevans_1948]
- [Aerodynamics of the airplane][book_cbmillikan_1949]
- [Airplane performance stability and control][book_courtlanddperkins_1949]
- [Airplane Performance Stability and Control][book_robertehageperkinscourtlandd_1960]
- [Self-adaptive control systems][book_georgejthaler_1960]
- [Adaptive control systems][book_elimishkin_1961]
- [Aircraft stability and control][book_awbabister_1961]
- [Optimal adaptive control systems][book_davidsworder_1966]
- [Aircraft stability and control forpilots and engineers][book_dickinsonbrian_1968]
- [Aircraft stability and control data][book_garylteper_1969]
- [Model Aircraft Aerodynamics][book_martinsimons_1978]
- [Aerodynamics of the airplane][book_hermannschlichting_1979]
- [Aircraft flight test data processing][book_ljsmith_1980]
- [Flight Testing the Fixed Wing Configuration of the Rotor...][book_gwhall_pmmorris_1985]
- [Flight testing the fixed-wing configuration of the rotor...][book_gwarrenhall_1985]
- [Model aircraft aerodynamics][book_martinsimons_1985]
- [Application of parameter estimation to aircraft stability and...][book_richardemaine_1986]
- [Flight test report of the NASA icing research airplane][book_jerryljordan_1986]
- [Full-envelope aerodynamic modeling of the Harrier aircraft][book_bdavidmcnally_1986]
- [Adaptive control systems][book_vvchalam_1987]
- [Model Aircraft Aerodynamics][book_msimons_martinsimons_1987]
- [Aircraft flight test trajectory control][book_pkamenon_1988]
- [Introduction to aircraft flight test engineering][book_hubertsmith_hubertcsmith_1988]
- [Tailless aircraft performance improvements][book_irvinglouisashkenas_1989]
- [Basic helicopter aerodynamics][book_jseddon_simonnewman_1990]
- [Neural networks for control][book_richardssutton_pauljwerbos_1990]
- [Airplane Design Part VII Determination of Stability Control...][book_janroskam_1991]
- [Adaptive control systems][book_rolfisermann_1992]
- [Flight testing homebuilt aircraft][book_vaughanaskue_1992]
- [Fuzzy logic and neural networks for control systems][book_hamidrberenji_1992]
- [Neural networks for control and systems][book_kwarwick_kjhunt_1992]
- [Tailless aircraft--an extensive bibliography for subsonic...][book_sergekrauss_1992]
- [Modeling of aircraft unsteady aerodynamic characteristics][book_vladislavklein_1994]
- [Tailless Aircraft][book_karlnickel_1994]
- [Tailless aircraft in theory and practice][book_karllenickel_1994]
- [Advances in Neural Networks for Control Systems Advances in...][book_kjhunt_georgeirwin_1995]
- [Neural Networks for Control][book_richardssutton_pauljwerbos_1995]
- [Northrop Flying Wings][book_garryrpape_johnmcampbell_1995]
- [Flight dynamics principles][book_mvcook_1997]
- [Performance, stability, dynamics, and control of airplanes][book_bandunpamadi_1998]
- [Airplane Design Determination of Stability, Control and...][book_janroskam_2002]
- [Flight Testing of Fixed-Wing Aircraft Aiaa Education Series][book_ralphdkimberlin_2003]
- [Principles of helicopter flight dynamics][book_caoyihuaprof_2009]
- [Flying wings and tailless aircraft][book_billrose_2010]
- [Unmanned aircraft systems][book_regaustin_2010]
- [Flight Dynamics Principles][book_michaelvcook_2011]
- [Designing unmanned aircraft systems][book_jaygundlach_2012]
- [Introduction to unmanned aircraft systems][book_richardkbarnhart_2012]
- [Flight dynamics principles][book_mvcook_2013]
- [Introduction to Unmanned Aircraft Systems][book_richardbarnhart_stephenbhottman_2013]
- [Parameter Estimation Techniques and Applications in Aircraft...][book_flightcenter_2014]
- [Unmanned aircraft systems][book_jjayaraman_2014]
- [Luftwaffe X-Planes][book_manfredgriehl_2015]
- [Aircraft Control Allocation][book_waynedurham_kennethabordignon_2016]
- [Applied Artificial Higher Order Neural Networks for Control...][book_mingzhang_2016]
- [Adaptive Control Systems][book_chalam_2017]
- [Small Unmanned Aircraft Systems Guide][book_brentterwilliger_davidcison_2017]
- [Aerodynamics of the airplane][book_clarkblanchardmillikan_2018]
- [Applications of Small Unmanned Aircraft Systems][book_jbsharma_2019]
- [Self-Adaptive Control Systems][book_georgejthaler_2021]
- [Unmanned Aircraft Systems Traffic Management][book_michaelsbaum_2021]
- [Model Aircraft Aerodynamics, 5th Edition][book_martinsimons_2025]

**The research survey holds 3,712 research records drawn from the National Aeronautics and Space Administration's Technical Reports Server, the Defense Technical Information Center and the journal literature indexed by Crossref**, of which 520 are report primaries, being 14.0 percent, by the identifier rule set out under The Definition of Primary. **The median publication year is 2015.** Of the 3,709 dated records, 1,517 were published in 2001 or earlier, the period of the aircraft's design, flight programmes and reports, being 40.9 percent, and 1,973 were published in 2015 or later, being 53.2 percent. **The count and the fraction are reported together**, because adding sources on one side lowers the other's share without removing anything.

### The Definition of Primary

Primary means the reports and papers written during the programme and the technology base it drew on, which
for this subject reaches back to the free-flight model work of the 1950s and to the flying-wing stability
literature that is older still. **Primacy is a property of the document, and this survey derives it from the identifier.** A record is a report primary when its address is on the NASA Technical Reports Server or it carries a digital object identifier under the 10.21236 prefix, which Crossref registers for Defense Technical Information Center reports. **Of the five titles that name the X-36, one is a report primary**, so most of the aircraft's own record is journal and conference literature under this rule. **The rule does not reach the journal papers among the foundational sources**, such as the slender-body papers of the period and the viscosity measurements, so 14.0 percent is a lower bound on how much of the survey is first-hand.

### Thin Subjects

**Five research records carry this aircraft's designation in their titles.** The X-33, X-34 and X-35 show the same
shape for different reasons. The X-33 and X-34 were cancelled and stopped generating literature under their
own names. The X-35 won and never had a documentary trace at all, because contractor demonstrators flown for
a source selection do not produce reports.

**The X-36 is a fourth case and its reason is different again.** The programme was neither cancelled nor a
competition. It ran to completion, met its objectives, and produced a technique rather than a vehicle.
**What it contributed is in the literature under the names of its methods rather than under its own**, which
is why the scaling, control allocation and adaptive control clusters are large while the vehicle's own record
is not. **Four vehicles, four different reasons for the same thin record**, and the pattern is a finding
about the series of aircraft rather than about any one of them.

**Six subjects that this article's derivations depend on have thin literatures.** Each count below is the number of research records in this survey whose title carries at least one of the listed terms, with a hyphen read as a space. Where a row joins two groups of terms with the word together, a title must carry a term from each group.

| Subject | Title terms counted | Records |
|---|---|---|
| the drag increment of a split aileron or drag rudder | split aileron, split ailerons, drag rudder, drag rudders, deceleron, decelerons, clamshell | 1 |
| the time to double of an unstable mode | time to double, doubling time, doubling times, time to half | 0 |
| the link delay of a remotely piloted aircraft | latency, time delay, time delays, transport delay, video delay together with remotely piloted, unmanned aircraft, unmanned aerial, UAV, UAVs, RPV, drone, drones | 6 |
| the moments of inertia of an aircraft | moment of inertia, moments of inertia, radius of gyration, radii of gyration, inertia measurement together with aircraft, airplane, aeroplane, UAV, unmanned, hexacopter, quadcopter | 7 |
| turn rate and corner speed | turn rate, turn performance, corner speed, corner velocity, sustained turn, instantaneous turn | 3 |
| the Froude number of a free-flight model | Froude | 2 |

**The drag increment of a split surface is the quantity the yaw argument most needs and the least studied.** One title names a split aileron, a drag rudder, a deceleron or a clamshell surface, and the bracket on the increment stands on the relation derived above rather than on a measured value for this aircraft.

**The time to double is a textbook quantity rather than a research subject.** No title names the time to double or a doubling time, so the distinction drawn above between the modal time and the time from rest is the article's own.

**The delay of a remotely piloted aircraft's link is studied far less than delay in general.** Six titles name a delay together with a remotely piloted or unmanned aircraft, against 135 records in the cluster on time delay, latency and delay compensation, of which 23 titles name an aircraft, a pilot, flight or an unmanned aircraft and the rest concern teleoperated robots and ground vehicles or the theory of delayed systems. The delay that the article's amplification multiplies is therefore not available from this literature either.

**The inertia of a whole aircraft is rarely the subject of a title.** Seven titles name the moments of inertia of an aircraft or an unmanned aircraft, so the bracket across radius of gyration above cannot be narrowed from the literature.

**Turn rate and corner speed are named in three titles**, while the manoeuvre literature itself sits under agility and energy manoeuvrability in the cluster on turn performance, agility and manoeuvre.

**Froude scaling is used far more than it is named.** Two titles carry the word Froude, while the cluster on similitude, dynamic scaling and subscale flight testing holds 155 records on the scaling and testing of models.

### What the Survey Admits

**A record is admitted only when a person reading its title finds it on this article's subject**, which is the flight dynamics, control, aerodynamics, scaling, testing and remote operation of a tailless subscale research aircraft, together with the theory its derivations use. Many words this subject depends on also name something else, and a record that shares only such a word is excluded. Restore names a military laundry, a cancer gene and an operation in Somalia as well as a control law. Departure names a flight leaving its gate, so airport scheduling and departure noise are excluded. Similitude and dynamic scaling also belong to soils, beams, crash testing and mooring cables, and dynamic scaling is a term of control theory. Moment of inertia also names a property of servo drives, classroom pendulums, internal-friction apparatus and spacecraft. Viscosity also names liquids, aerosols and the artificial viscosity of numerical methods, and apparent mass also belongs to bodies in water and gas-particle flows. Control allocation also serves underwater vehicles, ships, electric cars, robots and satellites, rudder also names the rudders of ships and sailboats, and thrust vectoring also steers rockets and missiles. Reynolds number effects also govern turbine and compressor cascades, circular cylinders and buildings, and teleoperation also names the control of robotic manipulators with no delay in the loop. Records whose only link to the article is a distant application of the same aircraft class are excluded as well, among them drones used for mapping, surveying, wildfire watch and radio measurement, aircraft noise, icing, landing gear and tyres, crash survival, flutter and structures, rotorcraft rotors, launch vehicles, re-entry vehicles, projectiles and missiles, and electric propulsion and batteries. Correction notices, conference reports and announcements, trade news and supplementary-material records are excluded, because a survey counts research works and those are notices attached to works or parts of works. A signed comment on a paper and the authors' reply to it argue about a result and are research works, as are a signed discussion and a signed letter, so each is admitted when its subject is this article's, while an unsigned item of these kinds and a referee's report on a manuscript are not. Reviews of books, reference entries of two pages or fewer, and the abstracts of papers and patents reprinted in the abstract sections of other journals are excluded on the same ground, while a signed encyclopedia article and a textbook chapter are research works and stay. Where the same paper is deposited twice, as a digest and as the paper, one record is kept, while a conference paper and the journal article that followed it are kept as two documents.

**Some records of doubtful relevance are kept.** Teleoperation of ground vehicles and robots through a delayed link, the general theory of time-delay systems and of stability margins, control allocation for multirotor vehicles, the slender-body aerodynamics of missiles, rotorcraft handling qualities, and the correspondence of William Froude on ship models each share the delay, the margin, the redundant effectors, the fuselage or the scaling law with this subject, so each is kept and a reader may weigh it accordingly. **No residual cluster is needed**, because every admitted record falls within one of the named clusters.

**Every research title has been read for relevance, so the off-topic share that remains is a matter of reading judgement.** A reading of titles cannot show that a work is relevant in substance, so this is a statement about titles only.

## Epistemic State

### Historical Fact

The X-36 was a 28 percent scale, remotely piloted, tailless research aircraft built by McDonnell Douglas in
partnership with the National Aeronautics and Space Administration. Two were built. It was 18 feet 2.5
inches long with a span of 10 feet 5 inches, weighed 1,090 pounds empty and 1,270 pounds at maximum, carried
180 pounds of fuel, and was powered by a Williams F112 turbofan of 700 pounds force. Its approach speed was
110 knots, its maximum speed limit was raised from 160 to 243 knots during the programme, its ceiling was
20,500 feet and its load factor limit was 5 g. These dimensions, weights and speeds are those of one published
specification, and [Walker 1997][research_walkerlaurencea_1997], the test pilot's report, gives a takeoff gross weight of 1,245
pounds, an operating empty weight of 1,083 pounds, 162 pounds of usable fuel and an approach speed of 112
knots. It reached 206 knots, 20,200 feet and an angle of attack of
40 degrees. It first flew on 17 May 1997 and completed 31 research flights and 15 hours 38 minutes of
flight time by 12 November 1997, a period of 25 weeks. One inventory of American X-vehicles gives 25
flights ending on 24 September 1997 instead. In December 1998 it flew twice more carrying the Air Force Research Laboratory's Reconfigurable Control for Tailless Fighter Aircraft
software. It had no vertical or horizontal tail and used a canard, split ailerons and a thrust-vectoring
nozzle, commanded by a digital flight control system, with the pilot in a ground station viewing through a
camera on the forward fuselage.

### Engineering Analysis

Every scaling ratio follows from the scale factor alone once Froude matching is chosen, and each is an
identity that holds at every scale factor. The velocity and time ratios are
0.5292, the frequency ratio 1.8898, the angular acceleration ratio 3.571, the inertia ratio 0.001721 and the
Reynolds ratio 0.1482, a penalty of 6.749. The implied full-scale weight of 57,853 pounds, length of 19.82
metres and span of 11.34 metres follow from cube scaling. The wing area of 3.269 square metres and aspect
ratio of 3.084 are inverted from the published approach speed. The model Reynolds number of 8.81 million and
Mach number of 0.367 at maximum speed follow from the standard atmosphere and Sutherland's law. The yaw
moment from thrust vectoring of 2,364 newton metres and the authority crossover at 342.2 knots follow from
the moment balance.
**The identity that a disturbance released from rest doubles in 1.900 times the modal time is exact and depends on nothing.**
**Every figure in this section can be reproduced from the published specification and the stated assumptions
with the relations the article displays**, and the doubling times can also be reproduced by integrating the
yaw equation under its two initial conditions.

### Inference

That the scale factor is the interesting quantity, and not the missing tail, is a judgement about what is
worth explaining and not a fact. That the demonstration was harder than the thing it demonstrated is an
inference with an exact multiplier and an unmeasured multiplicand, and the article states it in that form.
**Whether the split ailerons were margin or necessity is not determined by public information**, since the
drag increment that decides it is unpublished and across its plausible range the split surfaces run from
22.1 to 132.4 percent of the nozzle's moment, so the answer flips inside the bracket. What is settled is the
structural claim, that the nozzle's authority is flat with speed while the drag rudder's rises as its
square, and that needs no increment at all. That the vehicle cluster is thin for a fourth distinct reason is
an inference from four cases and is offered as a pattern rather than a law.

### What the Record Does Not Settle

**Whether the aircraft's inertias were correctly scaled is not settled**, and if they were not then the
doubling times are wrong by that factor.

**The size of the link delay is unpublished**, so the amplification factor is exact and what it amplified
is unknown.

**The aircraft's behaviour at its highest angles of attack remains open**, since the public record gives
the maximum of 40 degrees but no time history there, only pilot ratings and a normalised roll-time plot from
lower angles, which limits what can be said about the question the
programme existed to answer.

**Whether a tailless manned fighter is practical is not settled by this aeroplane and was never going to be**,
because the binding constraints on that question are certification and signature rather than control.

## Out of Scope

The radar cross section of tailless configurations is outside this article, which has no access to the
measurements and no way to compute them. The production unmanned aircraft that adopted the planform are
outside it. The detailed architecture of the neural-network control law flown in 1998 is touched on only as
a programme fact. The X-31 and X-29, which are the series' other flight-control demonstrators, are covered
in their own articles, which this one cites without re-examining.

## Conclusion

**The X-36 asked whether a fighter can fly without a tail, and answered yes at 28 percent scale.** The
substance lies in that qualification.

Matching the Froude number is the only choice that makes a free-flight model move like an aeroplane, and it
fixes everything else.
**The model's motions run 1.8898 times faster than the full-scale aircraft's, its angular accelerations are 3.571 times larger, and its Reynolds number is lower by a factor of 6.749.**
The first of those is a handicap on the demonstration, because a delay in a video link and the reaction time
of a human being do not compress to match. The third is a limit on what the demonstration can measure, and
it falls precisely on the separated flow at high angle of attack that the experiment was about.

**The aircraft's own weight confirms the choice.** At 1,270 pounds and 28 percent it stands for a
fifty-eight thousand pound fighter, sixty-five feet long, which matches a real class of aeroplane.

**And the missing fin turns out to be the least interesting part of the story**, because the arithmetic says
the vectoring nozzle alone could hold ten degrees of sideslip at every speed the aircraft ever flew.
**Public information cannot say whether the split ailerons were carrying most of the yaw at high speed or almost none of it**,
and the article says so where it computes them.
**A nozzle can replace a fin because a fin's authority and the instability it opposes both scale with dynamic pressure, so their ratio never improves, while a nozzle's authority does not scale with anything.**
The nozzle is strongest where the fin is weakest, in the condition a tailless aircraft most
fears.

**The previous article found a demonstration flown easier than the thing it stood for. This one was flown harder.**
The X-36's divergence doubled in well under a second, nearly twice as fast as its full-scale equivalent
would have, and a pilot on the ground held it there through a delay that counted for nearly twice its
length in clock time.
**That is a better result than the programme claimed for itself, and nobody said so because the factor is hidden inside the scale.**
## References

### Books

- [A. W. Babister 1961, Aircraft stability and control][book_awbabister_1961]
- [Avrum Zier 1942, Aerodynamics for model aircraft][book_avrumzier_1942]
- [B. David McNally 1986, Full-envelope aerodynamic modeling of the...][book_bdavidmcnally_1986]
- [Bandu N. Pamadi 1998, Performance, stability, dynamics, and control of...][book_bandunpamadi_1998]
- [Bill Rose 2010, Flying wings and tailless aircraft][book_billrose_2010]
- [Brent Terwilliger 2017, Small Unmanned Aircraft Systems Guide][book_brentterwilliger_davidcison_2017]
- [C. B. Millikan 1949, Aerodynamics of the airplane][book_cbmillikan_1949]
- [Cao, Yihua Prof. 2009, Principles of helicopter flight dynamics][book_caoyihuaprof_2009]
- [Chalam 2017, Adaptive Control Systems][book_chalam_2017]
- [Clark B. Millikan 1941, Aerodynamics of the airplane][book_clarkbmillikan_1941]
- [Clark Blanchard Millikan 2018, Aerodynamics of the airplane][book_clarkblanchardmillikan_2018]
- [Courtland D. Perkins 1949, Airplane performance stability and control][book_courtlanddperkins_1949]
- [David Sworder 1966, Optimal adaptive control systems][book_davidsworder_1966]
- [Dickinson, Brian 1968, Aircraft stability and control forpilots and...][book_dickinsonbrian_1968]
- [Eli Mishkin 1961, Adaptive control systems][book_elimishkin_1961]
- [Flight Center 2014, Parameter Estimation Techniques and Applications in...][book_flightcenter_2014]
- [G. W. Hall 1985, Flight Testing the Fixed Wing Configuration of the...][book_gwhall_pmmorris_1985]
- [G. Warren Hall 1985, Flight testing the fixed-wing configuration of the...][book_gwarrenhall_1985]
- [Garry R. Pape 1995, Northrop Flying Wings][book_garryrpape_johnmcampbell_1995]
- [Gary L. Teper 1969, Aircraft stability and control data][book_garylteper_1969]
- [George J. Thaler 1960, Self-adaptive control systems][book_georgejthaler_1960]
- [George J. Thaler 2021, Self-Adaptive Control Systems][book_georgejthaler_2021]
- [Hamid R. Berenji 1992, Fuzzy logic and neural networks for control...][book_hamidrberenji_1992]
- [Hermann Schlichting 1979, Aerodynamics of the airplane][book_hermannschlichting_1979]
- [Hubert Smith 1988, Introduction to aircraft flight test engineering][book_hubertsmith_hubertcsmith_1988]
- [Irving Louis Ashkenas 1989, Tailless aircraft performance improvements][book_irvinglouisashkenas_1989]
- [J. B. Sharma 2019, Applications of Small Unmanned Aircraft Systems][book_jbsharma_2019]
- [J. Jayaraman 2014, Unmanned aircraft systems][book_jjayaraman_2014]
- [J. M. Evans 1948, Some properties and control problems of tailless...][book_jmevans_1948]
- [J. Seddon 1990, Basic helicopter aerodynamics][book_jseddon_simonnewman_1990]
- [Jan Roskam 1991, Airplane Design Part VII Determination of Stability...][book_janroskam_1991]
- [Jan Roskam 2002, Airplane Design Determination of Stability, Control...][book_janroskam_2002]
- [Jay Gundlach 2012, Designing unmanned aircraft systems][book_jaygundlach_2012]
- [Jerry L Jordan 1986, Flight test report of the NASA icing research...][book_jerryljordan_1986]
- [K. J. Hunt 1995, Advances in Neural Networks for Control Systems...][book_kjhunt_georgeirwin_1995]
- [K. Warwick 1992, Neural networks for control and systems][book_kwarwick_kjhunt_1992]
- [Karl L. E. Nickel 1994, Tailless aircraft in theory and practice][book_karllenickel_1994]
- [Karl Nickel 1994, Tailless Aircraft][book_karlnickel_1994]
- [L. J. Smith 1980, Aircraft flight test data processing][book_ljsmith_1980]
- [M. Simons 1987, Model Aircraft Aerodynamics][book_msimons_martinsimons_1987]
- [M. V. Cook 1997, Flight dynamics principles][book_mvcook_1997]
- [M. V. Cook 2013, Flight dynamics principles][book_mvcook_2013]
- [Manfred Griehl 2015, Luftwaffe X-Planes][book_manfredgriehl_2015]
- [Martin Simons 1978, Model Aircraft Aerodynamics][book_martinsimons_1978]
- [Martin Simons 1985, Model aircraft aerodynamics][book_martinsimons_1985]
- [Martin Simons 2025, Model Aircraft Aerodynamics, 5th Edition][book_martinsimons_2025]
- [Michael S. Baum 2021, Unmanned Aircraft Systems Traffic Management][book_michaelsbaum_2021]
- [Michael V. Cook 2011, Flight Dynamics Principles][book_michaelvcook_2011]
- [Ming Zhang 2016, Applied Artificial Higher Order Neural Networks for...][book_mingzhang_2016]
- [P. K. A. Menon 1988, Aircraft flight test trajectory control][book_pkamenon_1988]
- [Ralph D. Kimberlin 2003, Flight Testing of Fixed-Wing Aircraft Aiaa...][book_ralphdkimberlin_2003]
- [Reg Austin 2010, Unmanned aircraft systems][book_regaustin_2010]
- [Richard Barnhart 2013, Introduction to Unmanned Aircraft Systems][book_richardbarnhart_stephenbhottman_2013]
- [Richard E. Maine 1986, Application of parameter estimation to aircraft...][book_richardemaine_1986]
- [Richard K. Barnhart 2012, Introduction to unmanned aircraft systems][book_richardkbarnhart_2012]
- [Richard S. Sutton 1990, Neural networks for control][book_richardssutton_pauljwerbos_1990]
- [Richard S. Sutton 1995, Neural Networks for Control][book_richardssutton_pauljwerbos_1995]
- [Robert E. Hage Perkins Courtland D. 1960, Airplane Performance...][book_robertehageperkinscourtlandd_1960]
- [Rolf Isermann 1992, Adaptive control systems][book_rolfisermann_1992]
- [Serge Krauss 1992, Tailless aircraft--an extensive bibliography for...][book_sergekrauss_1992]
- [V. V. Chalam 1987, Adaptive control systems][book_vvchalam_1987]
- [Vaughan Askue 1992, Flight testing homebuilt aircraft][book_vaughanaskue_1992]
- [Vladislav Klein 1994, Modeling of aircraft unsteady aerodynamic...][book_vladislavklein_1994]
- [Wayne Durham 2016, Aircraft Control Allocation][book_waynedurham_kennethabordignon_2016]

[book_avrumzier_1942]: https://openlibrary.org/works/OL7663818W
[book_awbabister_1961]: https://openlibrary.org/works/OL6573117W
[book_bandunpamadi_1998]: https://openlibrary.org/works/OL1941667W
[book_bdavidmcnally_1986]: https://openlibrary.org/works/OL11147182W
[book_billrose_2010]: https://openlibrary.org/works/OL16997612W
[book_brentterwilliger_davidcison_2017]: https://openlibrary.org/works/OL21140975W
[book_caoyihuaprof_2009]: https://openlibrary.org/works/OL18570685W
[book_cbmillikan_1949]: https://openlibrary.org/works/OL13247458W
[book_chalam_2017]: https://openlibrary.org/works/OL28620740W
[book_clarkblanchardmillikan_2018]: https://openlibrary.org/works/OL19751827W
[book_clarkbmillikan_1941]: https://openlibrary.org/works/OL10544164W
[book_courtlanddperkins_1949]: https://openlibrary.org/works/OL7426871W
[book_davidsworder_1966]: https://openlibrary.org/works/OL7391577W
[book_dickinsonbrian_1968]: https://openlibrary.org/works/OL7073058W
[book_elimishkin_1961]: https://openlibrary.org/works/OL7344481W
[book_flightcenter_2014]: https://openlibrary.org/works/OL41017538W
[book_garryrpape_johnmcampbell_1995]: https://openlibrary.org/works/OL27791413W
[book_garylteper_1969]: https://openlibrary.org/works/OL13397523W
[book_georgejthaler_1960]: https://openlibrary.org/works/OL16848669W
[book_georgejthaler_2021]: https://openlibrary.org/works/OL32498853W
[book_gwarrenhall_1985]: https://openlibrary.org/works/OL8753398W
[book_gwhall_pmmorris_1985]: https://openlibrary.org/books/OL13259301M
[book_hamidrberenji_1992]: https://openlibrary.org/works/OL11166912W
[book_hermannschlichting_1979]: https://openlibrary.org/works/OL16930590W
[book_hubertsmith_hubertcsmith_1988]: https://openlibrary.org/works/OL4105982W
[book_irvinglouisashkenas_1989]: https://openlibrary.org/works/OL11564046W
[book_janroskam_1991]: https://openlibrary.org/works/OL6612011W
[book_janroskam_2002]: https://openlibrary.org/works/OL6612002W
[book_jaygundlach_2012]: https://openlibrary.org/works/OL16152092W
[book_jbsharma_2019]: https://openlibrary.org/works/OL25223450W
[book_jerryljordan_1986]: https://openlibrary.org/works/OL11329847W
[book_jjayaraman_2014]: https://openlibrary.org/works/OL23285881W
[book_jmevans_1948]: https://openlibrary.org/works/OL10551518W
[book_jseddon_simonnewman_1990]: https://openlibrary.org/works/OL4784768W
[book_karllenickel_1994]: https://openlibrary.org/works/OL13553727W
[book_karlnickel_1994]: https://openlibrary.org/works/OL3499225W
[book_kjhunt_georgeirwin_1995]: https://openlibrary.org/books/OL10152648M
[book_kwarwick_kjhunt_1992]: https://openlibrary.org/works/OL23480925W
[book_ljsmith_1980]: https://openlibrary.org/works/OL4444200W
[book_manfredgriehl_2015]: https://openlibrary.org/works/OL21652852W
[book_martinsimons_1978]: https://openlibrary.org/works/OL6632399W
[book_martinsimons_1985]: https://openlibrary.org/works/OL12605860W
[book_martinsimons_2025]: https://openlibrary.org/works/OL42549468W
[book_michaelsbaum_2021]: https://openlibrary.org/works/OL25273971W
[book_michaelvcook_2011]: https://openlibrary.org/works/OL25644852W
[book_mingzhang_2016]: https://openlibrary.org/works/OL41159108W
[book_msimons_martinsimons_1987]: https://openlibrary.org/works/OL35731100W
[book_mvcook_1997]: https://openlibrary.org/works/OL2047176W
[book_mvcook_2013]: https://openlibrary.org/works/OL16726305W
[book_pkamenon_1988]: https://openlibrary.org/works/OL11169852W
[book_ralphdkimberlin_2003]: https://openlibrary.org/works/OL8874080W
[book_regaustin_2010]: https://openlibrary.org/works/OL15537286W
[book_richardbarnhart_stephenbhottman_2013]: https://openlibrary.org/works/OL25156646W
[book_richardemaine_1986]: https://openlibrary.org/works/OL4930233W
[book_richardkbarnhart_2012]: https://openlibrary.org/works/OL16184054W
[book_richardssutton_pauljwerbos_1990]: https://openlibrary.org/works/OL19499640W
[book_richardssutton_pauljwerbos_1995]: https://openlibrary.org/works/OL39110551W
[book_robertehageperkinscourtlandd_1960]: https://openlibrary.org/works/OL36764926W
[book_rolfisermann_1992]: https://openlibrary.org/works/OL4105150W
[book_sergekrauss_1992]: https://openlibrary.org/works/OL3996721W
[book_vaughanaskue_1992]: https://openlibrary.org/works/OL4102187W
[book_vladislavklein_1994]: https://openlibrary.org/works/OL8874113W
[book_vvchalam_1987]: https://openlibrary.org/works/OL4960130W
[book_waynedurham_kennethabordignon_2016]: https://openlibrary.org/works/OL20225610W

### Reference

- [American X-Vehicles, An Inventory X-1 to X-50, SP-2003-4531][ref_american_x_vehicles]
- [Armstrong Flight Research Center][ref_dryden]
- [Chengdu J-36][ref_j36]
- [Control allocation for over-actuated aircraft][ref_allocation]
- [Directional stability][ref_directional]
- [Froude number][ref_froude]
- [Lockheed Martin RQ-170 Sentinel][ref_rq170]
- [McDonnell Douglas X-36][ref_x36]
- [Mental chronometry][ref_reaction]
- [NASA account of the X-36 tailless fighter agility research aircraft][ref_nasa_x36]
- [National Aeronautics and Space Administration][ref_nasa]
- [Phantom Works][ref_phantom_works]
- [Reynolds number][ref_reynolds]
- [Similitude in model testing][ref_similitude]
- [Tailless aircraft][ref_tailless]
- [The X-36 in the National Museum of the United States Air Force][ref_museum]
- [Thrust vectoring][ref_tv]
- [Williams F112 turbofan][ref_f112]

[ref_allocation]: https://en.wikipedia.org/wiki/Control_reconfiguration
[ref_american_x_vehicles]: https://www.nasa.gov/wp-content/uploads/2023/04/sp-4531.pdf
[ref_directional]: https://en.wikipedia.org/wiki/Directional_stability
[ref_dryden]: https://en.wikipedia.org/wiki/Armstrong_Flight_Research_Center
[ref_f112]: https://en.wikipedia.org/wiki/Williams_F107
[ref_froude]: https://en.wikipedia.org/wiki/Froude_number
[ref_j36]: https://en.wikipedia.org/wiki/Chengdu_J-36
[ref_museum]: https://www.nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Display/Article/195764/nasaboeing-x-36/
[ref_nasa]: https://en.wikipedia.org/wiki/NASA
[ref_nasa_x36]: https://www.nasa.gov/aeronautics/x-36-tailless-fighter/
[ref_phantom_works]: https://en.wikipedia.org/wiki/Phantom_Works
[ref_reaction]: https://en.wikipedia.org/wiki/Mental_chronometry
[ref_reynolds]: https://en.wikipedia.org/wiki/Reynolds_number
[ref_rq170]: https://en.wikipedia.org/wiki/Lockheed_Martin_RQ-170_Sentinel
[ref_similitude]: https://en.wikipedia.org/wiki/Similitude
[ref_tailless]: https://en.wikipedia.org/wiki/Tailless_aircraft
[ref_tv]: https://en.wikipedia.org/wiki/Thrust_vectoring
[ref_x36]: https://en.wikipedia.org/wiki/McDonnell_Douglas_X-36

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
- [X-Planes: Convair X-11][related_post_a308_convair_x11]
- [X-Planes: Convair X-12][related_post_a309_convair_x12]
- [X-Planes: Convair X-6][related_post_a303_convair_x6]
- [X-Planes: Curtiss-Wright X-19][related_post_a316_curtiss_wright_x19]
- [X-Planes: Douglas X-3 Stiletto][related_post_a300_douglas_x3]
- [X-Planes: Framing and the Research Aircraft Model][related_post_a297_xplanes_framing]
- [X-Planes: Grumman X-29][related_post_a326_grumman_x29]
- [X-Planes: Hiller X-18][related_post_a315_hiller_x18]
- [X-Planes: Lockheed Martin X-33][related_post_a330_lockheed_martin_x33]
- [X-Planes: Lockheed Martin X-35][related_post_a332_lockheed_martin_x35]
- [X-Planes: Lockheed X-17][related_post_a314_lockheed_x17]
- [X-Planes: Lockheed X-27][related_post_a324_lockheed_x27]
- [X-Planes: Lockheed X-7][related_post_a304_lockheed_x7]
- [X-Planes: Martin Marietta X-23 PRIME][related_post_a320_martin_marietta_x23]
- [X-Planes: Martin Marietta X-24][related_post_a321_martin_marietta_x24]
- [X-Planes: North American X-10][related_post_a307_north_american_x10]
- [X-Planes: North American X-15][related_post_a312_north_american_x15]
- [X-Planes: Northrop X-21][related_post_a318_northrop_x21]
- [X-Planes: Northrop X-4 Bantam][related_post_a301_northrop_x4]
- [X-Planes: Orbital Sciences X-34][related_post_a331_orbital_sciences_x34]
- [X-Planes: Osprey X-28 Sea Skimmer][related_post_a325_osprey_x28]
- [X-Planes: Rockwell X-30 and the National Aero-Space Plane][related_post_a327_rockwell_x30]
- [X-Planes: Rockwell-MBB X-31][related_post_a328_rockwell_mbb_x31]
- [X-Planes: Ryan X-13 Vertijet][related_post_a310_ryan_x13]
- [X-Planes: Schweizer X-26 Frigate][related_post_a323_schweizer_x26]

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

### Research

- [088 Stability margin of a feedback system with structured and unstructured uncertainties 1994][research_088_stability_1994]
- [122 Neural networks applied to optimal flight control 1993][research_122_neural_1993]
- [213 Development of a robust flight control law for a VSTOL aircraft 1994][research_213_development_1994]
- [A multi microprocessor flight control system design principles 1979][research_a_multi_1979]
- [A Novel Sliding Mode Controller for Underactuated Vertical Takeoff and Landing Aircraft 2020][research_a_novel_2020]
- [A simple link between pole shifting and phase margin 1994][research_a_simple_1994]
- [Abdel-Malek and Marmarelis 1988][research_abdelmalek_marmarelis_1988]
- [Abdelhamid 1985][research_abdelhamid_1985]
- [Abdullah and Miao 2026][research_abdullah_miao_2026]
- [Abdullah et al 2025][research_abdullah_kashif_2025]
- [Abdullahi et al 2026][research_abdullahi_maimako_2026]
- [Abdulrahim et al 2019][research_abdulrahim_bates_2019]
- [Abe 1993][research_abe_1993]
- [Abidi et al 2016][research_abidi_yildiz_2016]
- [Abouheaf et al 2020][research_abouheaf_gueaieb_2020]
- [Abras et al 2023][research_abras_tuckey_2023]
- [Abu Salem et al 2023][research_abusalem_palaia_2023]
- [Abu-Elola et al 2024][research_abuelola_alqaisia_2024]
- [Accommodation of failures in the F-16 aircraft using adaptive control 1991][research_accommodation_of_1991]
- [Ackerman et al 2019][research_ackerman_gregory_2019]
- [Acquatella et al 2017][research_acquatellab_vanekeren_2017]
- [Adak et al 2024][research_adak_mandal_2024]
- [Adams 1972][research_adams_1972]
- [Adams 1993][research_adamsrichardj_1993]
- [Adams and Banda 1993][research_adams_banda_1993]
- [Adams and Banda 1993][research_adams_banda_1993_b]
- [Adams and Hatch 1970][research_adams_hatchjr_1970]
- [Adams and Hatch 1971][research_adams_hatch_1971]
- [Adams and John C. 1968][research_adams_johnc_1968]
- [Addington 2000][research_addington_2000]
- [Addington and Myatt 2000][research_addington_myatt_2000]
- [Addoms 1977][research_addoms_1977]
- [Adeyi et al 2024][research_adeyi_alabi_2024]
- [Aditya and Srinivas 2019][research_aditya_srinivas_2019]
- [Adiwidodo and Wijaya 2022][research_adiwidodo_wijaya_2022]
- [Advanced Control Techniques for Unmanned Aerial Vehicle (UAV) Navigation and Flight Control 2023][research_advanced_control_2023]
- [Advisory Group for Aerospace Research and Development 1999][research_advisorygroupforaerospaceresearchanddevelopment_1999]
- [AERODYNAMIC ANALYSIS OF EAGLE WINGLETS ON AIRCRAFT 2017][research_aerodynamic_analysis_2017]
- [Aerodynamic Characteristics of Bodies 1951][research_aerodynamic_characteristics_1951]
- [Aerodynamic Performance of Swayasa Aircraft Wing Model against the Effect of Airfoil Flap Angle Configuration 2025][research_aerodynamic_performance_2025]
- [Aerodynamics of arbitrary wing body combinations with vortex latticeand slender body theory 1976][research_aerodynamics_of_1976]
- [Agarwal 1988][research_agarwalak_1988]
- [Agarwal et al 2021][research_agarwal_ng_2021]
- [Aghazadeh Ardebili et al 2025][research_aghazadehardebili_martella_2025]
- [Ahmad and Li 2022][research_ahmad_li_2022]
- [Ahmadi and Haeri 2017][research_ahmadi_haeri_2017]
- [Ahmadi and Haeri 2018][research_ahmadi_haeri_2018]
- [Ahmadi Dastgerdi et al 2022][research_ahmadidastgerdi_asadi_2022]
- [Ahmed et al 2024][research_ahmed_zakaria_2024]
- [Ahmed et al 2025][research_ahmed_elbanna_2025]
- [Ahmed-Zaid et al 1990][research_ahmedzaid_ioannou_1990]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]
- [Air Force Test Pilot School Edwards Afb Ca 1969][research_airforcetestpilotschooledwardsafbca_1969]
- [Air Force Test Pilot School Edwards Afb Ca 1981][research_airforcetestpilotschooledwardsafbca_1981]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_b]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_d]
- [Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_c]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_d]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_e]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991_c]
- [Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]
- [Aircraft design optimization with multidisciplinary performance criteria 1989][research_aircraft_design_1989]
- [Aircraft moments of inertia 1996][research_aircraft_moments_1996]
- [Aircraft performance monitoring from flight data 2015][research_aircraft_performance_2015]
- [Ajaj 2021][research_ajaj_2021]
- [Akagi et al 1997][research_akagi_shinomiya_1997]
- [Akaryildiz et al 2024][research_akaryildiz_demirkiran_2024]
- [Akbari and Greeff 2024][research_akbari_greeff_2024]
- [Akgumus Gok 2024][research_akgumusgok_2024]
- [Akmeliawati and Mareels 1999][research_akmeliawati_mareels_1999]
- [Akram et al 2020][research_akram_tedesco_2020]
- [Aksteter et al 1994][research_aksteter_parks_1994]
- [Al-Mashhadani 2019][research_almashhadani_2019]
- [Al-Zubaidi and Stol 2022][research_alzubaidi_stol_2022]
- [AlAbsi and Fields 2017][research_alabsi_fields_2017]
- [Alag and Kaufman 1974][research_alag_kaufman_1974]
- [Alaian et al 2016][research_alaian_basuno_2016]
- [Alam and Mamun 2021][research_alam_mamun_2021]
- [Albostan and Gökaşan 2018][research_albostan_gokasan_2018]
- [Albrecht et al 2019][research_albrecht_naguib_2019]
- [Albrecht et al 2022][research_albrecht_olson_2022]
- [Aldosari and Feron 2025][research_aldosari_feron_2025]
- [Aleisa et al 2023][research_aleisa_kontis_2023]
- [Aleisa et al 2023][research_aleisa_kontis_2023_b]
- [Alexander 1979][research_alexander_1979]
- [Alexander 1979][research_alexander_1979_b]
- [Alexander 1991][research_alexander_1991]
- [Alexander 1993][research_alexander_1993]
- [Alexander 2025][research_alexander_2025]
- [Alferov et al 1982][research_alferov_vernikova_1982]
- [Alford and Altman 2004][research_alford_altman_2004]
- [Alford and Knarr 1999][research_alford_knarr_1999]
- [Algozino et al 2015][research_algozino_maranondileo_2015]
- [Alhazmi et al 2021][research_alhazmi_ghazi_2021]
- [Ali et al 2024][research_ali_rasani_2024]
- [Allee 1973][research_allee_eg_1973]
- [Allen 2017][research_allen_2017]
- [Allen and Perkins 1951][research_allenhjulian_perkinsedwardw_1951]
- [Allen et al 2002][research_allenmichaelj_ryanjack_2002]
- [Almosnino 1983][research_almosnino_1983]
- [Almosnino 1985][research_almosnino_1985]
- [AlQadi and Eljack 2016][research_alqadi_eljack_2016]
- [AlShabi et al 2024][research_alshabi_saleh_2024]
- [Alsolami et al 2025][research_alsolami_bhattacharjee_2025]
- [Alston 1936][research_alston_1936]
- [Alstrom and Paul 2023][research_alstrom_paul_2023]
- [Altman 2008][research_altman_2008]
- [Altunkaya and Özkol 2025][research_altunkaya_ozkol_2025]
- [Alvarez-Munoz et al 2019][research_alvarezmunoz_castillozamora_2019]
- [Alyshev et al 2016][research_alyshev_melnikov_2016]
- [Amato et al 1996][research_amato_ambrosino_1996]
- [Amato et al 2022][research_amato_cortigiani_2022]
- [Amaya et al 2026][research_amaya_xiang_2026]
- [American Institute of Aeronautics and Astronautics 1992][research_americaninstituteofaeronauticsandastronautics_1992]
- [An et al 2025][research_an_wang_2025]
- [An Overview On Unmanned Aerial Vehicle 2017][research_an_overview_2017]
- [Analysis of the relationship between mass, speed and cost of an unmanned aircraft 2024][research_analysis_of_2024]
- [Analytic constraints in feedback control of linear time-varying systems: Bode's sensitivity integral 1999][research_analytic_constraints_1999]
- [Analytical synthesis of the control laws at short-period longitudinal motion of the unmanned aerial vehicle 2024][research_analytical_synthesis_2024]
- [Ananda et al 2017][research_ananda_vahora_2017]
- [Ananthkrishnan and Sinha 2023][research_ananthkrishnan_sinha_2023]
- [Ananthkrishnan and Sudhakar 1994][research_ananthkrishnan_sudhakar_1994]
- [Ananthkrishnan and Sudhakar 1995][research_ananthkrishnan_sudhakar_1995]
- [Andersen and Bagby 1965][research_andersen_bagby_1965]
- [Anderson 1970][research_anderson_1970]
- [Anderson 1984][research_anderson_1984]
- [Anderson 1985][research_anderson_1985]
- [Anderson and Vincent 1985][research_anderson_vincent_1985]
- [Anderson et al 1954][research_anderson_flickinger_1954]
- [Anderson et al 2004][research_anderson_phillips_2004]
- [Andre and Morris 1981][research_andre_morris_1981]
- [Andrews et al 1980][research_andrewswh_simag_1980]
- [Andrianantara et al 2025][research_andrianantara_ghazi_2025]
- [Andropov et al 2017][research_andropov_guirik_2017]
- [Anna and Kidman 1994][research_annapauld_kidmandavids_1994]
- [Annaswamy 2005][research_annaswamy_2005]
- [Antonakis 2025][research_antonakis_2025]
- [Antonakis and Biannic 2024][research_antonakis_biannic_2024]
- [Anyoji 2019][research_anyoji_2019]
- [Aono et al 2018][research_aono_anyoji_2018]
- [APPLICATION OF FLUIDIC THRUST VECTORING IN V/STOL AIRCRAFT 2024][research_application_of_2024_b]
- [Applications of Fuzzy Logic and Neural Network Technology to Flight Control System Design: an Overview 2004][research_applications_of_2004]
- [Aprovitola et al 2021][research_aprovitola_dinuzzo_2021]
- [Araujo-Estrada and Windsor 2019][research_araujoestrada_windsor_2019]
- [Arena and Nelson 1989][research_arenaasjr_nelsonrc_1989]
- [Arif and Sasongko 2021][research_arif_sasongko_2021]
- [Armah 2018][research_karmah_2018]
- [Armstrong 1977][research_armstrong_1977]
- [Army Scientific Advisory Panel Washington Dc 1977][research_armyscientificadvisorypanelwashingtondc_1977]
- [Arogeti and Ailon 2023][research_arogeti_ailon_2023]
- [Aronstein 1996][research_aronstein_1996]
- [Arshad et al 2022][research_arshad_nawanjana_2022]
- [Aryasomayajula et al 2001][research_aryasomayajula_wang_2001]
- [Asaro and Vos 2025][research_asaro_vos_2025]
- [Asaro and Vos 2026][research_asaro_vos_2026]
- [Asghari and Tayefi 2026][research_asghari_tayefi_2026]
- [Asher and Hyland 1965][research_asher_hyland_1965]
- [Ashish Kumar Gupta et al 2023][research_ashishkumargupta_paaswathanarayana_2023]
- [Ashkenas 1965][research_ashkenas_1965]
- [Ashkenas 1965][research_ashkenas_1965_b]
- [Ashkenas 1965][research_ashkenas_1965_c]
- [Ashkenas 1982][research_ashkenas_1982]
- [Ashkenas 1984][research_ashkenas_1984]
- [Ashkenas and Klyde 1989][research_ashkenasirvingl_klydedavidh_1989]
- [Ashraf and Van Kampen 2020][research_ashraf_vankampen_2020]
- [Ashraf et al 2018][research_ashraf_tabassum_2018]
- [Ashton 2017][research_ashton_2017]
- [Asouti et al 2023][research_asouti_kontou_2023]
- [Asztalos et al 2025][research_asztalos_salucci_2025]
- [Asztalos et al 2026][research_asztalos_salucci_2026]
- [Atay et al 2021][research_atay_bryant_2021]
- [Athayde et al 2024][research_athayde_moutinho_2024]
- [Atli 1988][research_atli_1988]
- [Atmaca and Van Kampen 2025][research_atmaca_vankampen_2025]
- [Atmaca et al 2025][research_atmaca_stroosma_2025]
- [Atmaca et al 2026][research_atmaca_stroosma_2026]
- [Atmaja et al 2023][research_atmaja_fajar_2023]
- [Atta and Nayfeh 1978][research_atta_nayfeh_1978]
- [Atzhorn and Stengel 1981][research_atzhorn_stengel_1981]
- [Aulehia 1987][research_aulehia_1987]
- [Aulehla and Kissel 1981][research_aulehla_kissel_1981]
- [Aulehla and Kissel 1982][research_aulehla_kissel_1982]
- [Aume et al 1976][research_aume_mills_1976]
- [Automatic Landing 1964][research_automatic_landing_1964]
- [Avirovic et al 2023][research_avirovic_brunelli_2023]
- [Avirovic et al 2024][research_avirovic_brunelli_2024]
- [Axelson 1975][research_axelson_1975]
- [Axelson and Emerson 1949][research_axelsonjohna_emersonhoracef_1949]
- [Ayoub and McLachlan 1987][research_ayouba_mclachlanbg_1987]
- [Ayoub and McLachlan 1988][research_ayoub_mclachlan_1988]
- [Azarmi and Tavakoli-Kakhki 2020][research_azarmi_tavakolikakhki_2020]
- [Azimov and Allen 2017][research_azimov_allen_2017]
- [Bach and McNally 1988][research_bach_mcnally_1988]
- [Bachelder and Aponso 2020][research_bachelder_aponso_2020]
- [Bachelder and Aponso 2020][research_bachelder_aponso_2020_b]
- [Bachelder and Aponso 2023][research_bachelder_aponso_2023]
- [Bachelder et al 2023][research_bachelder_aponso_2023_b]
- [Bachmaier and Anderson 2021][research_bachmaier_anderson_2021]
- [Bachtiar et al 2019][research_bachtiar_ardilla_2019]
- [Bacon and Ostroff 2000][research_bacon_ostroff_2000]
- [Bacon et al 1996][research_baconbartonj_carzoosusanw_1996]
- [Badole et al 2022][research_badole_choudhary_2022]
- [Badrya and Baeder 2019][research_badrya_baeder_2019]
- [Badrya et al 2018][research_badrya_govindarajan_2018]
- [Badwan and Tutunji 2018][research_badwan_tutunji_2018]
- [Bagade et al 2015][research_bagade_krishnan_2015]
- [Baggi et al 2020][research_baggi_franco_2020]
- [Baggi et al 2022][research_baggi_serrani_2022]
- [Bagherzadeh et al 2025][research_bagherzadeh_mohammadkarimi_2025]
- [Bahr et al 2020][research_bahr_gandhi_2020]
- [Bai et al 2025][research_bai_deng_2025]
- [Bailes et al 1975][research_bailes_mittag_1975]
- [Bailey et al 2020][research_bailey_williams_2020]
- [Bajodah et al 2018][research_bajodah_mibar_2018]
- [Baker 1978][research_bakerjr_1978]
- [Baker and Batavia 2016][research_baker_batavia_2016]
- [Balaji et al 2025][research_balaji_mahesh_2025]
- [Balakrishnan 1972][research_balakrishnan_1972]
- [Balas et al 1992][research_balas_garrard_1992]
- [Balas et al 1996][research_balas_packard_1996]
- [Balas et al 1997][research_balas_fialho_1997]
- [Balas et al 1998][research_balas_packard_1998]
- [Balasubramanian et al 2024][research_balasubramanian_ahuja_2024]
- [Balatti et al 2021][research_balatti_haddadkhodaparast_2021]
- [Balcan et al 2026][research_balcan_kucuker_2026]
- [Baldini et al 2019][research_baldini_felicetti_2019]
- [Baldini et al 2026][research_baldini_felicetti_2026]
- [Ban et al 2018][research_ban_yamazaki_2018]
- [Banerjee 1988][research_banerjee_1988_b]
- [Banerjee 2019][research_banerjee_2019]
- [Banerjee et al 2017][research_banerjee_boyce_2017]
- [Banfield et al 2016][research_banfield_kidd_2016]
- [Banks 1988][research_banksdanielw_1988]
- [Bansal and Lavoie 2025][research_bansal_lavoie_2025]
- [Bantscheff and Breitsamter 2023][research_bantscheff_breitsamter_2023]
- [Bao et al 2025][research_bao_li_2025]
- [Bar-Gill and Stengel 1986][research_bargill_stengel_1986]
- [Bar-On and Jonckheere 1991][research_baron_jonckheere_1991]
- [Barbini et al 1970][research_barbini_balfe_1970]
- [Barela and Jackson 1988][research_barela_jackson_1988]
- [Barker and Balas 1999][research_barker_balas_1999]
- [Barnes 1971][research_barnes_1971]
- [Barnhouse et al 2025][research_barnhouse_hamid_2025]
- [Barret and Barret 1997][research_barret_barret_1997]
- [Bartlett and Turner 1975][research_bartlett_turner_1975]
- [Battipede et al 2004][research_battipede_gili_2004]
- [Battiston et al 2017][research_battiston_sharf_2017]
- [Baughman and Longeauay 2015][research_baughman_longeauay_2015]
- [Baumann and Gal-Or 1992][research_baumann_galor_1992]
- [Baxter 2013][research_baxter_2013]
- [Bay and Kara 2026][research_bay_kara_2026]
- [Baylen et al 1967][research_baylen_walton_1967]
- [Bayoğlu et al 2016][research_bayoglu_nalci_2016]
- [Bazuhair 2018][research_bazuhair_2018]
- [Beall 1986][research_beall_1986]
- [Beard and Foley 1983][research_beardbb_foleywh_1983]
- [Beasley 1984][research_beasleygp_1984]
- [Beaufrere 1986][research_beaufrere_1986]
- [Bechelder et al 2025][research_bechelder_bjorkman_2025]
- [Beck and Cord 1995][research_beck_cord_1995]
- [Beeman 1972][research_beemanrr_1972]
- [Been et al 2018][research_been_kang_2018]
- [Begum et al 2020][research_begum_rao_2020]
- [Behm 1973][research_behm_1973]
- [Bellamri et al 2024][research_bellamri_benineneto_2024]
- [Bellman and Kier 1974][research_bellmandr_kierda_1974]
- [Belmont 1983][research_belmont_1983]
- [Benedikt 1953][research_benedikt_1953]
- [Bennett 1984][research_bennett_1984]
- [Bennett and Baras 1985][research_bennett_baras_1985]
- [Bennett et al 2017][research_bennett_lawson_2017]
- [Bennett et al 2024][research_bennett_chapman_2024]
- [Benny Thompson and Gunasekaran 2021][research_bennythompson_gunasekaran_2021]
- [Benyamen and Keshmiri 2022][research_benyamen_keshmiri_2022]
- [Benyamen et al 2023][research_benyamen_mays_2023]
- [Benyamen et al 2024][research_benyamen_chowdhury_2024]
- [Bercovici et al 1990][research_bercovici_foias_1990]
- [Berens 2019][research_berens_2019]
- [Berens and Biezad 1988][research_berens_biezad_1988]
- [Berg 1991][research_berg_1991]
- [Berger et al 2016][research_berger_miller_2016]
- [Berger et al 2019][research_berger_horn_2019]
- [Berger et al 2025][research_berger_christensen_2025]
- [Bergman 1979][research_bergman_1979]
- [Bergmann et al 2021][research_bergmann_denzel_2021]
- [Berman 1947][research_bermantheodore_1947]
- [Berman 1949][research_bermantheodore_1949]
- [Berman and Pumphrey 1950][research_bermantheodore_pumphreynormane_1950]
- [Bernal and Yu 2015][research_bernal_yu_2015]
- [Bernardos et al 2019][research_bernardos_richez_2019]
- [Bernhard and Adamy 2017][research_bernhard_adamy_2017]
- [Bernstein 2000][research_bernstein_2000]
- [Berra et al 2017][research_berra_campbell_2017]
- [Berry and Powers 1970][research_berry_powers_1970]
- [Bertrand-Noël et al 2022][research_bertrandnoel_bignaletcazalet_2022]
- [Betin 2026][research_betin_2026]
- [Beyer et al 2018][research_beyer_kuzolap_2018]
- [Beyers 1986][research_beyers_1986]
- [Beyers and Ericsson 2002][research_beyers_ericsson_2002]
- [Bezdek 1995][research_bezdek_1995]
- [Bezerra and Santos 2022][research_bezerra_santos_2022]
- [Bhandari et al 2026][research_bhandari_bhandari_2026]
- [Bhujel et al 2026][research_bhujel_pang_2026]
- [Bhusal and Subbarao 2022][research_bhusal_subbarao_2022]
- [Bianchi et al 2024][research_bianchi_epicoco_2024]
- [Biber 2015][research_biber_2015]
- [Bidar et al 2024][research_bidar_he_2024]
- [Bidinotto et al 2021][research_bidinotto_moura_2021]
- [Biedron and Whitaker 1994][research_roberttbiedron_davidlwhitaker_1994]
- [Bielat and Wiley 1959][research_bielatralphp_wileyharlethg_1959]
- [Biezad and Schmidt 1984][research_biezad_schmidt_1984]
- [Biezad and Schmidt 1985][research_biezad_schmidt_1985]
- [Bigler 1986][research_bigler_1986]
- [Bihrle 1969][research_bihrlejr_1969]
- [Bihrle 1970][research_bihrlejr_1970]
- [Bihrle and Barnhart 1982][research_bihrle_barnhart_1982]
- [Bihrle and Billy 1980][research_bihrle_jr_1980]
- [Bihrle and Bowman 1980][research_bihrlewjr_bowmanjsjr_1980]
- [Billingsley 1976][research_billingsley_1976]
- [Bing et al 2015][research_bing_feng_2015]
- [Binz and Moormann 2020][research_binz_moormann_2020]
- [Binz et al 2019][research_binz_islam_2019]
- [Bird 1970][research_bird_1970]
- [Bischoff 1983][research_bischoff_1983]
- [Bischoff and Palmer 1982][research_bischoff_palmer_1982]
- [Bischoff and Palmer 1983][research_bischoff_palmer_1983]
- [Bischoff et al 1974][research_bischoff_duffy_1974]
- [Bishop 1961][research_bishop_1961]
- [Bissonnette and Bramesfeld 2015][research_bissonnette_bramesfeld_2015]
- [Black 1968][research_black_1968_b]
- [Black and Moorhouse 1979][research_black_moorhouse_1979]
- [Black et al 2024][research_black_andjelic_2024]
- [Blanken and Pausder 1994][research_blanken_pausder_1994]
- [Blanken and Whalley 1993][research_christopherlblanken_matthewswhalley_1993]
- [Bliamis et al 2021][research_bliamis_zacharakis_2021]
- [Bliss 1980][research_bliss_1980]
- [Bloy and Lea 1995][research_bloy_lea_1995]
- [Bobrowski et al 2016][research_bobrowski_barnewitz_2016]
- [Bodson 2000][research_bodson_2000]
- [Bodson and Groszkiewicz 1997][research_bodson_groszkiewicz_1997]
- [Bodson and Pohlchuck 1996][research_bodson_pohlchuck_1996]
- [Bodson and Pohlchuck 1998][research_bodson_pohlchuck_1998]
- [Bodson et al 1997][research_bodson_pohlchuck_1997]
- [Bodur and Ucun 2023][research_bodur_ucun_2023]
- [Bodur et al 2025][research_bodur_hancioglu_2025]
- [Boeing Vertol Co Philadelphia Pa 1983][research_boeingvertolcophiladelphiapa_1983]
- [Bolling et al 1997][research_bolling_durham_1997]
- [Bolting et al 2017][research_bolting_stolle_2017]
- [Bomben et al 2006][research_bombencraigr_smolkajamesw_2006]
- [Bond 1936][research_bond_1936]
- [Bond and Packard 1961][research_bondreuben_packardbarbarab_1961]
- [Boothe 1971][research_boothe_1971]
- [Boothe et al 1974][research_boothe_chen_1974]
- [Booz 1988][research_booz_1988]
- [Boppe and Martorella 1992][research_boppe_martorella_1992]
- [Bordei and Halanay 2025][research_bordei_halanay_2025]
- [Borer et al 2019][research_borer_cox_2019]
- [Borer et al 2024][research_borer_reynolds_2024]
- [Borisova and Silantiev 2022][research_borisova_silantiev_2022]
- [Bosch and Kuehl 1976][research_bosch_kuehl_1976]
- [Bosch and Kuehl 1977][research_bosch_kuehl_1977]
- [Boschetti et al 2004][research_boschetti_cardenas_2004]
- [Boschetti et al 2020][research_boschetti_cardenas_2020]
- [Boschetti et al 2022][research_boschetti_neves_2022]
- [Boskovic and Mehra 1999][research_boskovic_mehra_1999]
- [Boskovic and Mehra 2000][research_boskovic_mehra_2000]
- [Boskovic and Mehra 2001][research_boskovic_mehra_2001]
- [Boskovic and Mehra 2002][research_boskovic_mehra_2002]
- [Boskovic et al][research_boskovic_saimingli]
- [Bosnyakov et al 2024][research_bosnyakov_wolkov_2024]
- [Bosworth 2008][research_bosworthjohnt_2008]
- [Bosworth 2010][research_bosworthjohnt_2010]
- [Bosworth and Cox 1989][research_bosworth_cox_1989]
- [Bosworth and Stachowiak 2005][research_bosworthjohnt_stachowiaksusanj_2005]
- [Bosworth and Stoliker 1996][research_bosworthjohnt_stolikerpc_1996]
- [Bouaiss et al 2023][research_bouaiss_mechgoug_2023]
- [Bousson and Paglione 2001][research_bousson_paglione_2001]
- [Bouzid et al 2018][research_bouzid_bestaoui_2018]
- [Bowes and Miller 1976][research_bowes_miller_1976]
- [Bowlus et al 1997][research_bowlus_multhopp_1997]
- [Bowman 1957][research_bowmanjamessjr_1957]
- [Boyden 1970][research_boyden_1970]
- [Boyden 1971][research_boyden_1971]
- [Bradshaw and Huber 1982][research_bradshaw_huber_1982]
- [Bramesfeld and Prinster 2015][research_bramesfeld_prinster_2015]
- [Brandeau 1978][research_brandeau_1978]
- [Brandin 1990][research_brandin_1990]
- [Brandon and Morelli 2016][research_brandon_morelli_2016]
- [Brandon et al 1987][research_brandonjaym_brownphilipw_1987]
- [Brandt et al 2019][research_brandt_mclaughlin_2019]
- [Braun et al 2025][research_braun_holzapfel_2025]
- [Brauser 1982][research_brauser_1982]
- [Breitung 2001][research_breitung_2001]
- [Breneman and Lower 1992][research_breneman_lower_1992]
- [Breuhaus 1979][research_breuhaus_1979]
- [Breul 1963][research_breul_1963]
- [Brewer 1946][research_brewergeraldw_1946]
- [Brimelow 1970][research_brimelow_1970]
- [Brinker and Wise 1996][research_brinker_wise_1996]
- [Brinker and Wise 1998][research_brinker_wise_1998]
- [Brinker and Wise 1999][research_brinker_wise_1999]
- [Brinker and Wise 2000][research_brinker_wise_2000]
- [Brinker and Wise 2001][research_brinker_wise_2001]
- [Brody and Fagley 2024][research_brody_fagley_2024]
- [Bronz and Hattenberger 2016][research_bronz_hattenberger_2016]
- [Brown 1970][research_brownjr_1970]
- [Brown 1993][research_brown_1993]
- [Brown 2025][research_brown_2025]
- [Brown and Duhon 1965][research_brown_duhon_1965]
- [Brown et al 2026][research_brown_hoover_2026]
- [Brudnak 2016][research_brudnak_2016]
- [Brudnak 2020][research_brudnak_2020]
- [Brueckner et al 2023][research_brueckner_patinostudencki_2023]
- [Brunelli et al 2026][research_brunelli_avirovic_2026]
- [Bruns and Smith 1992][research_brunsjamese_smithcf_1992]
- [Bryson 1954][research_bryson_1954]
- [Bryson and Desai 1968][research_brysonjr_desai_1968]
- [Bryson et al 1969][research_bryson_desai_1969]
- [Bréda et al 2024][research_breda_andoga_2024]
- [Bucci et al 1997][research_bucci_sullivan_1997]
- [Buffington 1999][research_buffington_1999]
- [Buffington 1999][research_buffington_1999_b]
- [Buffington and Buffington 1997][research_buffington_buffington_1997]
- [Buffington and Sparks 1998][research_buffington_sparks_1998_b]
- [Buffington et al 1993][research_buffington_sparks_1993]
- [Buffington et al 1994][research_buffington_sparks_1994]
- [Buffington et al 1998][research_buffington_sparks_1998]
- [Buffington et al 1999][research_buffington_chandler_1999]
- [Bugliari Armenio et al 2024][research_bugliariarmenio_cortigiani_2024]
- [Bui 2016][research_bui_2016]
- [Bui 2018][research_bui_2018]
- [Bukov 1989][research_bukov_1989]
- [Bunge et al 2015][research_bunge_munerasavino_2015]
- [Burchett 2023][research_burchett_2023]
- [Burchett and Bryson 2025][research_burchett_bryson_2025]
- [Burk and Libbey 1961][research_sangermburkjr_charleselibbey_1961]
- [Burk and Wilson 1975][research_burksmjr_wilsoncfjr_1975]
- [Burke 2015][research_burke_2015]
- [Burken 2005][research_burkenjohnj_2005]
- [Burken and Larson 2009][research_burkenjohnj_larsonrichardr_2009]
- [Burken et al 1999][research_burken_lu_1999]
- [Burken et al 2001][research_burken_lu_2001]
- [Burken et al 2006][research_burkenjohnj_williamshayespeggy_2006]
- [Burken et al 2010][research_burkenjohnj_nguyennhant_2010]
- [Burnashev and Zbrutsky 2019][research_burnashev_zbrutsky_2019]
- [Burnell et al 1973][research_burnell_morrison_1973]
- [Burner et al 2000][research_burner_liu_2000]
- [Burris 1969][research_burris_1969]
- [Burris and Bender 1969][research_burris_bender_1969]
- [Burrows and Allaire 2019][research_burrows_allaire_2019]
- [Burton and Bischoff 1976][research_burton_bischoff_1976]
- [Burton and Kneeland 1981][research_burton_kneelandjr_1981]
- [Buschbacher and Bosworth 2006][research_buschbachermark_bosworthjohn_2006]
- [Bushnell 1990][research_bushnell_1990]
- [Butler 1976][research_butler_1976]
- [Byers et al 1988][research_byers_bittner_1988]
- [Byrdsong and Brooks 1980][research_byrdsong_brooks_1980]
- [Byrdsong and Brooks 1983][research_byrdsong_brooks_1983]
- [Byrdsong and Hallissy 1979][research_byrdsong_hallissy_1979]
- [Caap and Elemeland 1986][research_caap_elemeland_1986]
- [Caddy and Arnold 1988][research_caddy_arnold_1988]
- [Cai et al 2026][research_cai_fan_2026]
- [Cakici and Yörük 2022][research_cakici_yoruk_2022]
- [Cakiroglu et al 2018][research_cakiroglu_vankampen_2018]
- [Calarese 1981][research_calarese_1981]
- [Calise 2000][research_calise_2000]
- [Calise 2001][research_calise_2001]
- [Calise et al 1997][research_calise_rysdyk_1997]
- [Calise et al 1998][research_calise_lee_1998]
- [Calise et al 2000][research_calise_lee_2000]
- [Calise et al 2001][research_calise_lee_2001]
- [Callaghan and Kunz 2019][research_callaghan_kunz_2019]
- [Callaghan and Kunz 2021][research_callaghan_kunz_2021]
- [Cameron et al 2003][research_cameron_thomson_2003]
- [Cameron et al 2021][research_cameron_memon_2021]
- [Campbell 1959][research_campbell_1959]
- [Campbell 1973][research_campbell_1973]
- [Campbell 1974][research_campbell_1974]
- [Campbell and Abramovitz 1975][research_campbell_abramovitz_1975]
- [Campbell et al 2026][research_campbell_mulani_2026]
- [Campos 1989][research_campos_1989]
- [Campos and Marques 2021][research_campos_marques_2021]
- [Canin 2019][research_canin_2019]
- [Cantarelo et al 2016][research_cantarelo_rolland_2016]
- [Cao and Lu 2024][research_cao_lu_2024]
- [Cao and Qi 2018][research_cao_qi_2018]
- [Cao et al 2017][research_cao_tang_2017]
- [Cao et al 2022][research_cao_zhang_2022]
- [Cao et al 2026][research_cao_chen_2026]
- [Capello et al 2019][research_capello_ferrero_2019]
- [Capone 1979][research_capone_1979]
- [Capone and Mason 1986][research_capone_mason_1986]
- [Caradima and Wang 2000][research_caradima_wang_2000]
- [Carine Viola Dsouza and Dr. Basawaraj 2015][research_carinevioladsouza_drbasawaraj_2015]
- [Carino et al 2015][research_carino_abaunza_2015]
- [Carlson 1958][research_carlson_1958]
- [Carlson et al 1965][research_carlson_mabli_1965]
- [Carpenter and Jenny 1964][research_carpenter_jenny_1964]
- [Carr et al 2003][research_carr_lambrecht_2003]
- [Carter 1976][research_carter_1976]
- [Carter 1988][research_carter_1988]
- [Carter et al 2024][research_carter_keeter_2024]
- [Casadei et al 2019][research_casadei_konozsy_2019]
- [Castillo Zúñiga et al 2020][research_castillozuniga_souza_2020]
- [Catalano and D'Aniello 2025][research_catalano_daniello_2025]
- [Catalano et al 2024][research_catalano_derosa_2024]
- [Catani et al 1982][research_catani_deamicis_1982]
- [Cavalcanti et al 2026][research_cavalcanti_uehara_2026]
- [Cavallo and Dash 2000][research_cavallo_dash_2000]
- [Cavanaugh 2003][research_cavanaugh_2003]
- [Caverly and Forbes 2018][research_caverly_forbes_2018]
- [Caverly et al 2016][research_caverly_girard_2016]
- [Cebeci et al 1983][research_cebeci_stewartson_1983]
- [Cecen 2021][research_cecen_2021]
- [Chai et al 1995][research_chai_crisafulli_1995]
- [Chaikalis et al 2020][research_chaikalis_khorrami_2020]
- [Chakraborty and Mishra 2021][research_chakraborty_mishra_2021]
- [Chakravarty 1987][research_chakravarty_1987]
- [Chakravarty and Mahanta 2015][research_chakravarty_mahanta_2015]
- [Chalk 1964][research_chalk_1964]
- [Chalk et al 1969][research_chalk_neal_1969]
- [Chamberlain 1968][research_chamberlain_1968]
- [Chamberlin and Miller 1979][research_chamberlin_miller_1979]
- [Chambers 1988][research_josephrchambers_1988]
- [Chambers and Hall 2004][research_chambers_hall_2004]
- [Chamitoff 1994][research_chamitoff_1994]
- [Champigny 1984][research_champigny_1984]
- [Chance Vought Corp Dallas Tx 1979][research_chancevoughtcorpdallastx_1979]
- [Chand and Chiu 1991][research_chand_chiu_1991]
- [Chandan et al 2023][research_chandan_nagaraja_2023]
- [Chandra 2020][research_chandra_2020]
- [Chandra et al 2025][research_chandra_gandhi_2025]
- [Chang et al 2022][research_chang_guo_2022]
- [Chao and Yingmin 2015][research_chao_yingmin_2015]
- [Chao et al 2017][research_chao_ying_2017]
- [Chau and Zingg 2017][research_chau_zingg_2017]
- [Chau and Zingg 2022][research_chau_zingg_2022]
- [Chau et al 2026][research_chau_piotrowski_2026]
- [Chaudhuri and Praharaj 1971][research_chaudhuri_praharaj_1971]
- [Chaudhuri et al 2018][research_chaudhuri_jasa_2018]
- [Chavez and Vogel 2003][research_chavez_vogel_2003]
- [Chawla and Van Dalsem 1992][research_chawla_vandalsem_1992]
- [Che et al 2021][research_che_lian_2021]
- [Cheatham et al 1991][research_cheatham_gridley_1991]
- [Chedrik et al 2004][research_chedrik_ishmuratov_2004]
- [Chen 1992][research_chen_1992]
- [Chen 1993][research_chen_1993]
- [Chen 2021][research_chen_2021_b]
- [Chen 2024][research_chen_2024]
- [Chen 2026][research_chen_2026]
- [Chen and Ji 2017][research_chen_ji_2017]
- [Chen and Liu 2021][research_chen_liu_2021]
- [Chen and Xiao 2015][research_chen_xiao_2015]
- [Chen and Xie 2024][research_chen_xie_2024]
- [Chen and Yang 2022][research_chen_yang_2022]
- [Chen and Zhao 2017][research_chen_zhao_2017]
- [Chen et al 2015][research_chen_yue_2015]
- [Chen et al 2017][research_chen_wang_2017]
- [Chen et al 2017][research_chen_zhang_2017]
- [Chen et al 2019][research_chen_kopsaftopoulos_2019]
- [Chen et al 2020][research_chen_liu_2020]
- [Chen et al 2022][research_chen_ma_2022]
- [Chen et al 2024][research_chen_tang_2024]
- [Chen et al 2025][research_chen_li_2025]
- [Chen et al 2026][research_chen_gray_2026]
- [Chen et al 2026][research_chen_huang_2026]
- [Chen et al 2026][research_chen_li_2026]
- [Cheney 1988][research_cheney_1988]
- [Cheng and Pei 2020][research_cheng_pei_2020]
- [Cheng and Pei 2021][research_cheng_pei_2021]
- [Cheng and Xin 2019][research_cheng_xin_2019]
- [Cheng et al 2019][research_cheng_cai_2019]
- [Cheng et al 2020][research_cheng_zhang_2020]
- [Chernenko and Burnashev 2022][research_chernenko_burnashev_2022]
- [Chetty and Henschel 1987][research_chetty_henschel_1987]
- [Chetty and Lakshmi 1991][research_chetty_lakshmi_1991]
- [Chetty and Raol 1992][research_chetty_raol_1992]
- [Chevalier and Burke 1972][research_chevalier_burke_1972]
- [Chhetri et al 2026][research_chhetri_jetawatthana_2026]
- [Chin et al 2015][research_chinalexanderw_herreraclaudiay_2015]
- [Chin et al 2015][research_chinalexanderw_herreraclaudiay_2015_b]
- [Chitsaz et al 2021][research_chitsaz_siddiqui_2021]
- [Cho and Cho 1995][research_cho_cho_1995]
- [Cho et al 2018][research_cho_kim_2018]
- [Chodnicki et al 2018][research_chodnicki_bartnik_2018]
- [Choi et al 2023][research_choi_kim_2023]
- [Chowdhury and Keshmiri 2024][research_chowdhury_keshmiri_2024]
- [Chowdhury et al 2021][research_chowdhury_keshmiri_2021]
- [Chowhan et al 2019][research_chowhan_arya_2019]
- [Chu and Bryson 1987][research_chu_brysonjr_1987]
- [Chu et al 2001][research_chu_dacosta_2001]
- [Chuan et al 2016][research_chuan_feng_2016]
- [Chudoba and Cook 2003][research_chudoba_cook_2003]
- [Chun-Liang Lin et al 2004][research_chunlianglin_thongshinghwang_2004]
- [Chung and Tuan 2021][research_chung_tuan_2021]
- [Chunrong and Yunhong 2025][research_chunrong_yunhong_2025]
- [Cieślak 2021][research_cieslak_2021]
- [Ciliberti and Nicolosi 2025][research_ciliberti_nicolosi_2025]
- [Ciobaca and Dandois 2017][research_ciobaca_dandois_2017]
- [Clark 1964][research_clark_1964]
- [Clark 1982][research_clark_1982]
- [Clark 1983][research_clark_1983]
- [Clarke and Hwang 2020][research_clarke_hwang_2020]
- [Clarke and Roskam 1982][research_clarke_roskam_1982]
- [Cleary 1969][research_cleary_1969]
- [Clements 2016][research_clementskeith_2016]
- [Clements 2017][research_clementskeith_2017]
- [Clevenson et al 1953][research_clevensonsa_wildmayerejr_1953]
- [Cliff and Lutze 1972][research_cliff_lutze_1972]
- [Coalson 1968][research_coalson_1968]
- [Coalson 1982][research_coalson_1982]
- [Coalson and Csavina 1975][research_coalson_csavina_1975]
- [Coder and Ortiz-Melendez 2018][research_coder_ortizmelendez_2018]
- [Coe et al 1975][research_coepljr_grahamab_1975]
- [Cohen 1951][research_cohenrobertj_1951]
- [Cohn et al 1985][research_cohn_dusa_1985]
- [Colgren and Loschke 2008][research_colgren_loschke_2008]
- [Colgren and Martin 2000][research_colgren_martin_2000]
- [Collins 1982][research_collins_1982]
- [Collins et al 2004][research_collins_zhao_2004]
- [Collins Jr 2005][research_collinsjr_2005]
- [Collison et al 2017][research_collison_harley_2017]
- [Combined flight control/utility system 1974][research_combined_flight_1974]
- [Comer et al 2024][research_comer_bhandari_2024]
- [Comer et al 2026][research_comer_atkinson_2026]
- [Comer et al 2026][research_comer_chakraborty_2026]
- [Comer et al 2026][research_comer_chakraborty_2026_b]
- [Cong et al 2023][research_cong_hu_2023]
- [Cong et al 2023][research_cong_hu_2023_b]
- [Connolly et al 2016][research_connollyjosephw_csankjeffreyt_2016]
- [Connolly et al 2017][research_connolly_csank_2017]
- [Connors and Swaim 1968][research_connors_swaim_1968]
- [Cook and Hauser 2018][research_cook_hauser_2018]
- [Cooksey et al 1964][research_cooksey_dillenschneider_1964]
- [Coopmans et al 2015][research_coopmans_podhradsky_2015]
- [Coopmans et al 2016][research_coopmans_podhradsky_2016]
- [Coopmans et al 2022][research_coopmans_slack_2022]
- [Coppin et al 2018][research_coppin_birch_2018]
- [Corliss 1982][research_corliss_1982]
- [Cornelius and Lucius 1993][research_cornelius_lucius_1993]
- [Cornelius and Lucius 1993][research_cornelius_lucius_1993_b]
- [Cornelius and Lucius 1994][research_cornelius_lucius_1994]
- [Cornelius and Lucius 1995][research_cornelius_lucius_1995]
- [Corona-Sanchez and Rodriguez-Cortes 2015][research_coronasanchez_rodriguezcortes_2015]
- [Corraro et al 2003][research_corraro_delellis_2003]
- [Correa et al 1981][research_correa_sengupta_1981]
- [Cosentino 2007][research_cosentinogaryb_2007]
- [Cosentino 2007][research_cosentinogaryb_2007_b]
- [Cosentino 2008][research_cosentinogaryb_2008]
- [Cosenza and Vos 2017][research_cosenza_vos_2017]
- [Costes 1988][research_costes_1988]
- [Costigan and Calico 1989][research_costigan_calico_1989]
- [Cote 2015][research_cote_2015]
- [Cotting and Burken 2001][research_cotting_burken_2001]
- [Cotton 1974][research_cotton_1974]
- [Coulter and Marquart 1982][research_coulter_marquart_1982]
- [Courtin et al 2020][research_courtin_hansman_2020]
- [Cox 1957][research_cox_1957]
- [Cox and Cotting 2005][research_coxtimothyh_cottingmchristopher_2005]
- [Cox and Marshall 2000][research_coxtimothyh_marshallalisa_2000]
- [Cox et al 1949][research_cox_siddall_1949]
- [Cox et al 2012][research_coxdavide_cunninghamkevin_2012]
- [Craig 1965][research_craig_1965]
- [Craig and Heffley 1972][research_craig_heffley_1972]
- [Craig and Heffley 1973][research_craig_heffley_1973]
- [Cramer 1995][research_cramer_1995]
- [Crane 1983][research_cranedf_1983]
- [Crespo et al 2010][research_crespoluisg_matsutanimegumi_2010]
- [Crites et al 1992][research_crites_rueger_1992]
- [Crombie and Moorhouse 1980][research_crombie_moorhouse_1980]
- [Croom et al 2000][research_croom_kenney_2000]
- [Crother et al 1973][research_crother_gabelman_1973]
- [Crowther and Wood 1993][research_crowther_wood_1993]
- [Csavina 1976][research_csavina_1976]
- [Cui et al 2019][research_cui_feng_2019]
- [Cui et al 2021][research_cui_zuo_2021]
- [Cui et al 2024][research_cui_bai_2024]
- [Cumming and Kramer 1966][research_cumming_kramer_1966]
- [Cummings et al 2018][research_cummings_liersch_2018]
- [Cunis et al 2018][research_cunis_leth_2018]
- [Cunningham et al 2011][research_cunningham_cox_2011]
- [Curry and Batterson 2000][research_currytimothyj_battersonjamesg_2000]
- [Curry et al 1965][research_curry_matthews_1965]
- [Curtiss and Zhao 1988][research_curtisshc_zhaoxin_1988]
- [Cusher and Gopalarathnam 2006][research_cusher_gopalarathnam_2006]
- [Cusher and Gopalarathnam 2012][research_cusher_gopalarathnam_2012]
- [Czarkowski 2004][research_czarkowski_2004]
- [Czaykowski 1958][research_czaykowski_1958]
- [Czyba and Blachuta 2001][research_czyba_blachuta_2001]
- [Czyba and Blachuta 2003][research_czyba_blachuta_2003]
- [Czyba and Stajer 2019][research_czyba_stajer_2019]
- [Czyz and Karpinski 2020][research_czyz_karpinski_2020]
- [d'Apolito and Sulzbachner 2021][research_dapolito_sulzbachner_2021]
- [Dahleh and Tsitsiklis 2002][research_dahleh_tsitsiklis_2002]
- [Dally and Van Kampen 2022][research_dally_vankampen_2022]
- [Danowsky et al 2017][research_danowsky_schmidt_2017]
- [Dantsker 2024][research_dantsker_2024]
- [Dantsker and Mancuso 2019][research_dantsker_mancuso_2019]
- [Dantsker and Selig 2015][research_dantsker_selig_2015]
- [Dantsker et al 2018][research_dantsker_theile_2018_b]
- [Dantsker et al 2018][research_dantsker_vahora_2018]
- [Dantsker et al 2019][research_dantsker_yu_2019]
- [Dantsker et al 2020][research_dantsker_caccamo_2020]
- [Dantsker et al 2020][research_dantsker_theile_2020]
- [Dantsker et al 2022][research_dantsker_haviland_2022]
- [Dantsker et al 2023][research_dantsker_caccamo_2023]
- [Dantsker et al 2023][research_dantsker_haviland_2023]
- [Daryanto et al 2018][research_daryanto_purwono_2018]
- [Das et al 2024][research_das_mankodi_2024]
- [Daskiran et al 2017][research_daskiran_huff_2017]
- [Dat et al 2018][research_dat_son_2018]
- [Daughaday and Duwaldt 1955][research_daughaday_duwaldt_1955]
- [Davidson et al 1998][research_davidsonjohnb_murphypatrickc_1998]
- [Davis and Hines 1976][research_davis_hines_1976]
- [Davoudi and Duraisamy 2019][research_davoudi_duraisamy_2019]
- [De Almeida and Dias 2024][research_dealmeida_dias_2024]
- [de Becdelievre and Kroo 2021][research_debecdelievre_kroo_2021]
- [de Bruin and Jones 2016][research_debruin_jones_2016]
- [de Castro and Brembeck 2019][research_decastro_brembeck_2019]
- [De et al 2015][research_de_salvatore_2015]
- [de Oca and Flores 2020][research_deoca_flores_2020]
- [de Paula et al 2017][research_depaula_kleine_2017]
- [de Paula et al 2017][research_depaula_porto_2017]
- [de Rosa et al 2024][research_derosa_catalano_2024]
- [de Visser and Pool 2023][research_devisser_pool_2023]
- [de Vries and Van Kampen 2019][research_devries_vankampen_2019]
- [de Vries and Vos 2023][research_devries_vos_2023]
- [De Wagter and Meulenbeld 2019][research_dewagter_meulenbeld_2019]
- [Dean 1978][research_dean_1978]
- [DeBoer et al 2026][research_deboer_kimball_2026]
- [Debry et al 1992][research_debry_komerath_1992]
- [Deepak and Singh 2016][research_bbvl_singh_2016]
- [Deere et al 2017][research_deere_viken_2017]
- [Deets and Brown 1986][research_deets_brown_1986]
- [Deets and Edwards 1974][research_deetsda_edwardsjw_1974]
- [Deets and Purifoy 1998][research_deetsdwaina_purifoydana_1998]
- [Deffenbaugh and Jacoby 1980][research_deffenbaugh_jacoby_1980]
- [Degenne et al 1973][research_degenne_verges_1973]
- [DeJarnette and Jones 1978][research_dejarnette_jones_1978]
- [del Arco et al 2015][research_delarco_alejo_2015]
- [DeLaurier 2022][research_delaurier_2022]
- [Delay-dependent stability criteria for discrete-time delay systems 1999][research_delay_dependent_stability_1999]
- [Della Corte et al 2021][research_dellacorte_vansluis_2021]
- [Della Corte et al 2022][research_dellacorte_vansluis_2022]
- [Della Vecchia et al 2015][research_dellavecchia_nicolosi_2015]
- [Dellacasagrande et al 2020][research_dellacasagrande_barsi_2020]
- [Demarchi and Haning 1978][research_demarchi_haning_1978]
- [Deng and Li 2015][research_deng_li_2015]
- [Deng et al 2017][research_deng_qu_2017]
- [Deng et al 2024][research_deng_xu_2024]
- [Denham and Owens 2016][research_denham_owens_2016]
- [Denham et al 2022][research_caseyldenham_mayureshpatil_2022]
- [Denton et al 2025][research_denton_benedict_2025]
- [Derrouaoui et al 2023][research_derrouaoui_bouzid_2023]
- [Desai and Pant 2026][research_desai_pant_2026]
- [Deshpande and Zhang 2021][research_deshpande_zhang_2021]
- [Design and Development Autonomous Unmanned Aerial Vehicle Software 2020][research_design_and_2020]
- [Design and Fluid Flow Analysis of Unmanned Aerial Vehicle (UAV) 2015][research_design_and_2015]
- [Design and Implementation of Hybrid Wing Unmanned Aerial Vehicle (UAV) 2020][research_design_and_2020_b]
- [Deslich et al 2021][research_deslich_flick_2021]
- [Determination of External Power Factors Acting on an Unmanned Aerial Vehicle in Critical Flight Modes 2019][research_determination_of_2019]
- [Dethomas and Goel 1982][research_dethomas_goel_1982]
- [Devan 1989][research_devan_1989]
- [Development of Neo-Ptero Tailless Micro Aircraft 2018][research_development_of_2018]
- [Dexter and Hunt 1981][research_dexter_hunt_1981]
- [Dhayalan et al 2018][research_r_saderla_2018]
- [Dhiman et al 2022][research_dhiman_abhishek_2022]
- [Di Francesco and Mattei 2016][research_difrancesco_mattei_2016]
- [Dianovský et al 2023][research_dianovsky_pecho_2023]
- [Dias 2015][research_dias_2015]
- [Dias 2023][research_dias_2023]
- [Dias Pires de Souza et al 2017][research_diaspiresdesouza_rodriguez_2017]
- [Dickinson 1953][research_dickinson_1953]
- [Difranco 1969][research_difranco_1969]
- [Difranco 1970][research_difranco_1970]
- [DiFranco 1971][research_difranco_1971]
- [Diget et al 2022][research_diget_hasan_2022]
- [Digirolamo 1992][research_digirolamo_1992]
- [Digital model-reference flight control of aircraft with unstable sampling zeros 1994][research_digital_model_reference_1994]
- [Dik et al 2017][research_dik_biten_2017]
- [Dillon and Speyer 1996][research_dillon_speyer_1996]
- [Dillon and Speyer 2000][research_dillon_speyer_2000]
- [Din et al 2023][research_din_mir_2023]
- [Ding and Eskandarian 2024][research_ding_eskandarian_2024]
- [Diogo and Fernandes 2024][research_diogo_fernandes_2024]
- [Dizdarevic and Dizdarevic 2022][research_dizdarevic_dizdarevic_2022]
- [Do et al 2023][research_do_dang_2023]
- [Dobos-Bubno and Hartsook 1977][research_dobosbubno_hartsook_1977]
- [Dodge 2015][research_dodge_2015]
- [Dogan Kuzey and Yıldırım Dalkıran 2026][research_dogankuzey_yildirimdalkiran_2026]
- [Doko and Sasongko 2026][research_doko_sasongko_2026]
- [Dolan 1964][research_dolan_1964]
- [Doll et al 2024][research_doll_hoogreef_2024]
- [Doman 1995][research_doman_1995]
- [Doman and Sparks 2002][research_doman_sparks_2002]
- [Domino et al 2023][research_domino_czyz_2023]
- [Dong 2021][research_dong_2021]
- [Dong et al 2016][research_dong_lu_2016]
- [Dong et al 2025][research_dong_zhou_2025]
- [Dong xinmin et al 2003][research_dongxinmin_xiongzhiguo_2003]
- [Donovan and Allison 2017][research_donovan_allison_2017]
- [Dorato et al 1999][research_dorato_famularo_1999]
- [Dotson et al 2020][research_dotson_lee_2020]
- [Dou and Duan 2016][research_dou_duan_2016]
- [Dovi and Wrenn 1989][research_dovi_wrenn_1989]
- [Doyle and Rosema 2015][research_doyle_rosema_2015]
- [Dr. Olivia Davis 2021][research_droliviadavis_2021]
- [Drela 1991][research_drela_1991]
- [Drela and Giles 1986][research_drela_giles_1986]
- [Drell 1965][research_drell_1965]
- [Dress 1988][research_dress_1988]
- [Dress 1989][research_dress_1989]
- [Drewiacki et al 2016][research_drewiacki_silvestre_2016]
- [Drewiacki et al 2025][research_drewiacki_moreira_2025]
- [Du 2019][research_du_2019]
- [Du 2024][research_du_2024]
- [Duan and Okwudire 2018][research_duan_okwudire_2018]
- [Duggan and Bhandari 2021][research_duggan_bhandari_2021]
- [Dukes 1970][research_dukes_1970]
- [Dunn 1980][research_dunn_1980]
- [Duong Nguyen et al 2022][research_duongnguyen_kashitani_2022]
- [Dupuis et al 2018][research_dupuis_jouhaud_2018]
- [Duran 2026][research_duran_2026]
- [Duran et al 2019][research_duran_whidborne_2019]
- [Durgesh et al 2019][research_durgesh_padilla_2019]
- [Durham 1999][research_durham_1999]
- [Durham and Nelson 2001][research_durhamwayne_nelsonmark_2001]
- [Durston and Schreiner 1983][research_durston_schreiner_1983]
- [Durston and Stonum 1987][research_durston_stonum_1987]
- [Dussart et al 2018][research_dussart_yusuf_2018]
- [Dwivedi et al 2022][research_dwivedi_pavithra_2022]
- [Dwyer 1994][research_dwyer_1994]
- [Dwyer and Lutze 1993][research_dwyer_lutze_1993]
- [Dybdal 1987][research_dybdal_1987]
- [Désert et al 2019][research_desert_jardin_2019]
- [Ebeling 1969][research_ebeling_1969]
- [Eberhardt and Ward 1999][research_eberhardt_ward_1999]
- [Eberhardt and Ward 1999][research_eberhardt_ward_1999_b]
- [Ebner and Mark 1977][research_ebner_mark_1977]
- [Edefur and Tormalm 2018][research_edefur_tormalm_2018]
- [Edi 2026][research_edi_2026]
- [Edwards 1972][research_edwards_1972]
- [Edwards and Deets 1975][research_edwardsjw_deetsda_1975]
- [Edwards and Rankine 1927][research_edwards_rankine_1927]
- [Edwards et al 1997][research_edwards_fittante_1997]
- [Effects of Reynolds number and other parameters on the throttle-dependent, nozzle/afterbody drag of an 0.11 scale single-engine aircraft model 1979][research_effects_of_1979]
- [Efremov et al 1998][research_efremov_ogloblin_1998]
- [Efremov et al 2019][research_efremov_efremov_2019]
- [Efremov et al 2019][research_efremov_tiaglik_2019]
- [Efremov et al 2020][research_efremov_efremov_2020]
- [Efremov et al 2022][research_efremov_shcherbakov_2022]
- [Efremov et al 2023][research_efremov_efremov_2023]
- [Eftekhari and Al-Obaidi 2019][research_eftekhari_alobaidi_2019]
- [Ehlers and Smyth 1968][research_ehlers_smyth_1968]
- [Ehret et al 1950][research_ehretdorrism_rossowvernonj_1950]
- [Eichler 1970][research_eichler_1970]
- [Eilertson 1975][research_eilertson_1975]
- [Ekaterinaris and Schiff 1990][research_ekaterinaris_schiff_1990]
- [El Mobaraky et al 2026][research_elmobaraky_benjelloun_2026]
- [Elario et al 1991][research_elario_guillmette_1991]
- [Eldredge and Mousavi 2026][research_eldredge_mousavi_2026]
- [Elia 2004][research_elia_2004]
- [Elliott et al 2025][research_elliott_saj_2025]
- [Ellis 1972][research_ellis_1972]
- [Ellis and Christofides 2015][research_ellis_christofides_2015]
- [Elmiligui et al 2015][research_elmiligui_abdolhamid_2015]
- [Elmiligui et al 2017][research_elmiligui_abdolhamid_2017]
- [Ema et al 1997][research_ema_mizukura_1997]
- [Emami et al 2022][research_emami_castaldi_2022]
- [Emirler 2018][research_emirler_2018]
- [Enenakpogbe et al 2025][research_enenakpogbe_whidborne_2025]
- [Eney 1967][research_eney_1967]
- [Eney 1968][research_eney_1968]
- [Enns 1990][research_enns_1990]
- [Enns 1998][research_enns_1998]
- [Enns 2003][research_enns_2003]
- [Enns and Si 2002][research_enns_si_2002]
- [Enns et al 1994][research_enns_bugajski_1994]
- [Erhard et al 2021][research_erhard_clarke_2021]
- [Erickson 1991][research_ericksongarye_1991]
- [Erickson and Brandon 1987][research_erickson_brandon_1987]
- [Ericsson 1980][research_ericsson_1980]
- [Ericsson 1985][research_ericsson_1985]
- [Ericsson 1985][research_ericsson_1985_b]
- [Ericsson 1989][research_ericsson_1989]
- [Ericsson 1996][research_ericsson_1996]
- [Ericsson 1996][research_ericsson_1996_b]
- [Ericsson 1997][research_ericsson_1997]
- [Ericsson and Beyers 2002][research_ericsson_beyers_2002]
- [Ericsson and Hanff 1994][research_ericsson_hanff_1994]
- [Ericsson and Reding 1985][research_ericsson_reding_1985]
- [Eriş et al 2026][research_eris_ozgoren_2026]
- [Erkol 2017][research_erkol_2017]
- [Ermeydan and Kiyak 2017][research_ermeydan_kiyak_2017]
- [Erwin et al 1964][research_erwin_clark_1964]
- [Esfandabadi and Djavareshkian 2026][research_esfandabadi_djavareshkian_2026]
- [Esker and McArdle 1993][research_esker_mcardle_1993]
- [Esker and Sedrick 1972][research_esker_sedrick_1972]
- [Esmaeili et al 2018][research_esmaeili_delgado_2018]
- [Est and Nelson 1992][research_est_nelson_1992]
- [Estlow and Kovacevic 1990][research_estlow_kovacevic_1990]
- [Eulrich and Rynaski 1980][research_eulrich_rynaski_1980]
- [Eulrich et al 1978][research_eulrich_govindaraj_1978]
- [Eva Wu et al 2000][research_evawu_zhang_2000]
- [Evangelista et al 1987][research_evangelista_pfenninger_1987]
- [Evans 1964][research_evans_1964]
- [Evans 1991][research_evansalisonb_1991]
- [Evans and Chamblee 1966][research_evans_chamblee_1966]
- [Evans et al 1949][research_evans_galow_1949]
- [Experimental investigation of synthetic jet control of wing rock for a flying wing aircraft 2023][research_experimental_investigation_2023]
- [Fahmi and Woolsey 2018][research_fahmi_woolsey_2018]
- [Famularo et al 1999][research_famularo_dorato_1999]
- [Fan et al 2006][research_fan_zhu_2006]
- [Fan et al 2026][research_fan_jiang_2026]
- [Fang et al 2026][research_fang_cao_2026]
- [Farcy et al 2020][research_farcy_khrabrov_2020]
- [Farhadi 2017][research_farhadi_2017]
- [Fault Tolerant Control for Aircraft Flaperon Faults Using Nonlinear Dynamic Inversion 2025][research_fault_tolerant_2025]
- [Faure and Leogrande 2020][research_faure_leogrande_2020]
- [Fayaz et al 2022][research_fayaz_fathima_2022]
- [Feather and Joshi 1981][research_featherjb_joshids_1981]
- [Fediaevsky 1935][research_fediaevsky_1935]
- [Fegely et al 2016][research_fegely_tischler_2016]
- [Fegely et al 2017][research_fegely_carl_2017]
- [Fegely et al 2017][research_fegely_xin_2017]
- [Fei et al 2023][research_fei_li_2023]
- [Feldwisch 2026][research_feldwisch_2026]
- [Fell et al 2015][research_fell_owen_2015]
- [Feng et al 2017][research_feng_peng_2017]
- [Feng et al 2022][research_feng_wang_2022]
- [Feng et al 2024][research_feng_wang_2024]
- [Ferguson and Thomson 2015][research_ferguson_thomson_2015]
- [Ferguson et al 2017][research_ferguson_thomson_2017]
- [Ferlauto and Marsilio 2016][research_ferlauto_marsilio_2016]
- [Fernandes and Cardoso-Ribeiro 2025][research_fernandes_cardosoribeiro_2025]
- [Ferrand et al 2026][research_ferrand_gowree_2026]
- [Ferrari and Stengel 2004][research_ferrari_stengel_2004]
- [Fialho et al 1997][research_fialho_balas_1997]
- [Fielding and Southworth 2001][research_fielding_southworth_2001]
- [Filinov and Ostapyuk 2019][research_filinov_ostapyuk_2019]
- [Filinov et al 2020][research_filinov_tkachenko_2020]
- [Filippoli et al 2026][research_filippoli_perri_2026]
- [Filippoli et al 2026][research_filippoli_perri_2026_b]
- [Finigian et al 2024][research_finigian_kavounas_2024]
- [Fischenberg 1995][research_fischenberg_1995]
- [Fitzgerald and Gingras 1996][research_fitzgerald_gingras_1996]
- [Flanagan et al 2020][research_flanagan_chao_2020]
- [Fleeman and Nelson 1974][research_fleeman_nelson_1974]
- [Flight Test Data Analysis of Hybrid Vertical Take-off and Landing Unmanned Aerial Vehicle 2016][research_flight_test_2016]
- [Flight Test Programme 1970][research_flight_test_1970]
- [Flight-test evaluation of engine power effects on lift and drag 1985][research_flight_test_evaluation_1985]
- [Flow Control and High-Lift Performance for Flying-Wing Unmanned Combat Air Vehicle Configurations by inserting slots 2016][research_flow_control_2016]
- [Fogel et al 1974][research_fogel_englund_1974]
- [Ford 1977][research_ford_1977]
- [Ford 1989][research_ford_1989]
- [Forkun et al 2020][research_forkun_medzatyi_2020]
- [Fosdick 1970][research_fosdick_1970]
- [Foss 1944][research_foss_1944]
- [Foster and Hartman 2017][research_foster_hartman_2017]
- [Foster and Hartman 2017][research_johnvfoster_davidchartman_2017]
- [Foster et al 1993][research_foster_ross_1993]
- [Foster et al 2020][research_foster_miller_2020]
- [Franco et al 2019][research_franco_correia_2019]
- [Franklin 1970][research_franklin_1970]
- [Franklin 1971][research_franklin_1971]
- [Franklin and Miller 1967][research_franklin_miller_1967]
- [Franklin et al 1985][research_franklin_hynes_1985]
- [François et al 2021][research_francois_probst_2021]
- [Fratello and Shearin 1975][research_fratello_shearin_1975]
- [Fratello et al 1987][research_fratellodavidj_croommarka_1987]
- [Frazier 1991][research_frazier_1991]
- [Fremaux 1995][research_fremaux_1995]
- [Freudenberg and Looze 1985][research_freudenberg_looze_1985]
- [Friedland 1982][research_friedland_1982]
- [Friehmelt 1996][research_friehmelt_1996]
- [Friehmelt 1997][research_friehmelt_1997]
- [Friend 1964][research_friend_1964]
- [Froning 1981][research_froning_1981]
- [Frost et al 2009][research_frostsusana_bodsonmarc_2009]
- [Fry 2008][research_fry_2008]
- [Fry and Sage 1974][research_fry_sage_1974]
- [Fry and Sage 1974][research_frycm_sageap_1974]
- [Fu et al 2021][research_fu_yu_2021]
- [Fuad et al 2024][research_fuad_matute_2024]
- [Fujimori and Nikiforuk 1999][research_fujimori_nikiforuk_1999]
- [Fujimori et al 1997][research_fujimori_wu_1997]
- [Fujimori et al 1998][research_fujimori_wu_1998]
- [Fujita et al 2019][research_fujita_uechi_2019]
- [Fukami et al 2004][research_fukami_higashino_2004]
- [Fukui et al 2020][research_fukui_harada_2020]
- [Fukushima and Tsubone 2019][research_fukushima_tsubone_2019]
- [Fulkerson et al 1980][research_fulkerson_hershberger_1980]
- [Funk 1975][research_funk_1975]
- [Gacy 2011][research_gacy_2011]
- [Gadient and Weltz 2004][research_gadient_weltz_2004]
- [Gagg 1937][research_gagg_1937]
- [Gagnon and Zingg 2016][research_gagnon_zingg_2016]
- [Gain Scheduled Fuzzy Control on Aircraft Flight Control 2004][research_gain_scheduled_2004]
- [Gainer 1963][research_gainer_1963]
- [Gaither et al 1989][research_gaithersa_agarwalak_1989]
- [Gal-Or 1992][research_galor_1992]
- [Gal-Or 1994][research_galor_1994]
- [Gal-Or 2001][research_galor_2001]
- [Gal-Or and Baumann 1993][research_galor_baumann_1993]
- [Gal-Or et al 1995][research_galor_sherbaum_1995]
- [Galeani et al 2004][research_galeani_grasselli_2004]
- [Gallagher 1971][research_gallagher_1971]
- [Gallay and Laurendeau 2016][research_gallay_laurendeau_2016]
- [Gamal et al 2016][research_gamal_sadek_2016]
- [Gamble and Inman 2016][research_gamble_inman_2016]
- [Gan and Zha 2015][research_gan_zha_2015]
- [Gan et al 2021][research_gan_botre_2021]
- [Gandhi et al 2019][research_gandhi_whitcher_2019]
- [Gao et al 2015][research_gao_wang_2015]
- [Gao et al 2020][research_gao_liu_2020]
- [Gao et al 2021][research_gao_wang_2021]
- [Gao et al 2022][research_gao_shi_2022]
- [Garbarino et al 2023][research_garbarino_genito_2023]
- [Gardner and Downey 1950][research_gardner_downey_1950]
- [Garkushenko and Vinogradov 2016][research_garkushenko_vinogradov_2016]
- [Garrard 1998][research_garrard_1998]
- [Garretson 1986][research_garretsoniii_1986]
- [Gaudet and Furfaro 2023][research_gaudet_furfaro_2023]
- [Gavra and van Kampen 2024][research_gavra_vankampen_2024]
- [Gavra and Van Kampen 2024][research_gavra_vankampen_2024_b]
- [Gaylor 1984][research_gaylor_1984]
- [Ge and Zhan 2024][research_ge_zhan_2024]
- [Gebert et al 2000][research_gebert_kelly_2000]
- [Gee 1978][research_geesw_1978]
- [Gee et al 1992][research_geeken_rizkyehiam_1992]
- [Geng and Li 2023][research_geng_li_2023]
- [Geng et al 2018][research_geng_kalkman_2018]
- [Genito et al 2024][research_genito_garbarino_2024]
- [Genç et al 2022][research_genc_koca_2022]
- [Gerhardt and Chen 1978][research_gerhardtha_chenws_1978]
- [Gerken 1979][research_gerken_1979]
- [Gerosa et al 2018][research_gerosa_zanoni_2018]
- [Gertsen and Shomber 1965][research_gertsen_shomber_1965]
- [Geuther et al 2024][research_geuther_ackerman_2024]
- [Ghanchi and Gururajan 2026][research_ghanchi_gururajan_2026]
- [Ghasemzadeh and Banazadeh 2025][research_ghasemzadeh_banazadeh_2025]
- [Ghazi 1993][research_ghazi_1993]
- [Ghiglino et al 2015][research_ghiglino_forshaw_2015]
- [Ghofur et al 2020][research_ghofurm_darmawan_2020]
- [Ghorawat et al 2015][research_ghorawat_lee_2015]
- [Ghosh and Raisinghani 2000][research_ghosh_raisinghani_2000]
- [Ghosh and Raisinghani 2002][research_ghosh_raisinghani_2002]
- [Ghosh et al 1998][research_ghosh_raisinghani_1998]
- [Ghosh Roy and Peyada 2016][research_ghoshroy_peyada_2016]
- [Ghosh Roy and Peyada 2017][research_ghoshroy_peyada_2017]
- [Giacomini and Westerberg 2025][research_giacomini_westerberg_2025]
- [Gibson 1990][research_gibson_1990]
- [Gilbreath and Markofski 2001][research_gilbreath_markofski_2001]
- [Gill 1974][research_gill_1974]
- [Gillard 1998][research_gillard_1998]
- [Gillard et al 1997][research_gillard_dorsett_1997]
- [Gilyard et al 1972][research_gilyard_berry_1972]
- [Gingrich et al 1977][research_gingrich_child_1977]
- [Glad 1982][research_glad_1982]
- [Glad 1984][research_glad_1984]
- [Glenn 1988][research_glenn_1988]
- [Glezer and Leonard 2012][research_glezer_leonard_2012]
- [Glīzde 2017][research_glizde_2017]
- [Gnatowska and Gajewska 2024][research_gnatowska_gajewska_2024]
- [Go and Maqsood 2015][research_go_maqsood_2015]
- [Goerttler 2025][research_goerttler_2025]
- [Goetz et al 1976][research_goetz_young_1976]
- [Goetzendorf-Grabowski and Antoniewski 2016][research_goetzendorfgrabowski_antoniewski_2016]
- [Goetzendorf-Grabowski and Kwiek 2023][research_goetzendorfgrabowski_kwiek_2023]
- [Gold and Walchli 1974][research_gold_walchli_1974]
- [Goldberger 1966][research_goldberger_1966]
- [Goldstein 1982][research_goldstein_1982]
- [Goman and Kolesnikov 1998][research_goman_kolesnikov_1998]
- [Gomes and Suleman 2004][research_gomes_suleman_2004]
- [Gong et al 2019][research_gong_wang_2019]
- [González et al 2017][research_gonzalez_aranda_2017]
- [Goodrich and Sliwa 1987][research_goodrich_sliwa_1987]
- [Goodwin and Kaattari 1958][research_goodwinfrederickk_kaattarigeorgee_1958]
- [Gopalarathnam and McAvoy 2002][research_gopalarathnam_mcavoy_2002]
- [Gopalarathnam et al 2001][research_gopalarathnam_broughton_2001]
- [Gopalarothnam and McGowan 2008][research_gopalarothnam_mcgowan_2008]
- [Goparaju et al 2015][research_goparaju_gaitonde_2015]
- [Gordnier 1995][research_gordnier_1995]
- [Gorin and Gubankov 2025][research_gorin_gubankov_2025]
- [Gorski 1998][research_gorski_1998]
- [Gossett 1981][research_gossett_1981]
- [Gou et al 2023][research_gou_liu_2023]
- [Goud and Dwivedi 2022][research_goud_dwivedi_2022]
- [Govindaraj et al 1979][research_govindaraj_rynaski_1979]
- [Grafton et al 1974][research_graftonsb_chambersjr_1974]
- [Grafton et al 1982][research_graftonsb_gilberwp_1982]
- [Granasy 1995][research_granasy_1995]
- [Granata et al 2026][research_granata_mancini_2026]
- [Grant et al 2015][research_grant_stol_2015]
- [Grantham et al 1976][research_granthamwd_nguyenlt_1976]
- [Grauer 2015][research_grauer_2015]
- [Grauer 2016][research_grauer_2016]
- [Grauer 2020][research_grauer_2020]
- [Grauer 2021][research_grauer_2021]
- [Grauer and Boucher 2018][research_grauer_boucher_2018]
- [Grauer and Morelli 2015][research_grauer_morelli_2015]
- [Grauer and Morelli 2015][research_grauer_morelli_2015_b]
- [Gray 1964][research_gray_1964]
- [Gray 1964][research_grayjr_1964]
- [Green 1958][research_green_1958]
- [Green 1988][research_green_1988]
- [Greene and Kunz 2015][research_greene_kunz_2015]
- [Greenwell 2003][research_greenwell_2003]
- [Greer et al 1999][research_greer_hamory_1999]
- [Gregory 1998][research_gregory_1998]
- [Gregory 2001][research_gregory_2001]
- [Gregory et al 1994][research_gregoryirenem_chowdhryrajivs_1994]
- [Gres et al 2025][research_gres_stoura_2025]
- [Gresham et al 2023][research_gresham_simmons_2023]
- [Griffin and Bellaire 1968][research_griffin_bellaire_1968]
- [Grimminger et al 1950][research_grimminger_williams_1950]
- [Grismer et al 1997][research_grismer_myatt_1997]
- [Grogan et al 1994][research_grogan_durham_1994]
- [Grondman et al 2018][research_grondman_looye_2018]
- [Grossman 1957][research_grossman_1957]
- [Gu 2025][research_gu_2025]
- [Gu and Lee 1988][research_gu_lee_1988]
- [Gu et al 2017][research_gu_lyu_2017]
- [Gu et al 2019][research_gu_valavanis_2019]
- [Guan and Shi 2019][research_guan_shi_2019]
- [Guay et al 2017][research_guay_drolet_2017]
- [Guenther et al 2026][research_guenther_eichner_2026]
- [Guerrero et al 2015][research_guerrero_martinez_2015]
- [Guerrero-Bonilla et al 2017][research_guerrerobonilla_mohta_2017]
- [Guiler][research_guiler]
- [Guiler and Huebsch 2005][research_guiler_huebsch_2005]
- [Gundry 1977][research_gundry_1977]
- [Gungordu and Tayfuner 2026][research_gungordu_tayfuner_2026]
- [Guo 2021][research_guo_2021]
- [Guo 2021][research_guo_2021_b]
- [Guo et al 2017][research_guo_zhu_2017]
- [Guo et al 2018][research_guo_lin_2018]
- [Guo et al 2024][research_guo_zhang_2024]
- [Guo et al 2026][research_guo_liu_2026]
- [Guoqiang and Jinkun 2015][research_guoqiang_jinkun_2015]
- [Gupta et al 1991][research_guptaroopn_leekampui_1991]
- [Gupta et al 2025][research_gupta_aswathanarayana_2025]
- [Gursoy and Yavrucuk 2015][research_gursoy_yavrucuk_2015]
- [Gursul and Yang 1994][research_gursul_yang_1994]
- [Gursul and Yang 1995][research_gursul_yang_1995]
- [Gursul et al 1995][research_gursul_srinivas_1995]
- [Guy 1976][research_guy_1976]
- [Gäßler and Robens 2025][research_gassler_robens_2025]
- [Göttlicher et al 2016][research_gottlicher_gnoth_2016]
- [Güler et al 2021][research_guler_durhasan_2021]
- [Gümüşboğa and İftar 2021][research_gumusboga_iftar_2021]
- [Ha 1990][research_ha_1990]
- [Ha et al 2025][research_ha_kim_2025]
- [Haber and Chung 2016][research_haber_chung_2016]
- [Hacker 1977][research_hacker_1977]
- [Hadidoolabi and Ansarian 2017][research_hadidoolabi_ansarian_2017]
- [Hadidoolabi and Ansarian 2018][research_hadidoolabi_ansarian_2018]
- [Hafez and Kamel 2016][research_hafez_kamel_2016]
- [Haffley 1982][research_haffley_1982]
- [Hageman et al 2003][research_hageman_smith_2003]
- [Hajiyev 2016][research_hajiyev_2016]
- [Hajiyevt and Caliskan 2001][research_hajiyevt_caliskan_2001]
- [Hakim and Choukri 2023][research_hakim_choukri_2023]
- [Hale et al 2015][research_hale_patil_2015]
- [Hale et al 2017][research_hale_patil_2017]
- [Halefom et al 2022][research_halefom_gresham_2022]
- [Hall 1965][research_hall_1965]
- [Hall 1971][research_hall_1971]
- [Hall 1987][research_hall_1987]
- [Hall and Boothe 1972][research_hall_boothe_1972]
- [Hall and Kern 1996][research_hall_kern_1996]
- [Hall et al 1974][research_hall_weingarten_1974]
- [Hall et al 1998][research_hallrobertm_ericksongarye_1998]
- [Hall et al 1999][research_halljr_perkins_1999]
- [Hall et al 2006][research_hall_lawrence_2006]
- [Hamel and Jategaonkar 1996][research_hamel_jategaonkar_1996]
- [Hamidani and Kunz 2018][research_hamidani_kunz_2018]
- [Hammer and Shumway 2026][research_hammer_shumway_2026]
- [Hammer and Shumway 2026][research_hammer_shumway_2026_b]
- [Hammer et al 2026][research_hammer_degraaf_2026]
- [Hamza and Samir 2020][research_hamza_samir_2020]
- [Han and Patel 1977][research_han_patel_1977]
- [Han and Zhang 2019][research_han_zhang_2019]
- [Han et al 2019][research_han_hu_2019]
- [Han et al 2023][research_han_cheng_2023]
- [Han et al 2024][research_han_yang_2024]
- [Han et al 2025][research_han_wang_2025]
- [Han et al 2026][research_han_kim_2026]
- [Hansen 1959][research_hansencfrederick_1959]
- [Hanson 2012][research_hansoncurtise_2012]
- [Hantla and Wang 2025][research_hantla_wang_2025]
- [Harasani 2015][research_iharasani_2015]
- [Hardy and Sturgeon 1979][research_hardy_sturgeon_1979]
- [Harkegard 2003][research_harkegard_2003]
- [Harmats and Weihs 1999][research_harmats_weihs_1999]
- [Harper and Cooper 1984][research_harperjr_cooper_1984]
- [Harper and Cooper 1986][research_harper_cooper_1986]
- [Harper and Robert P. 1955][research_harper_robertp_1955]
- [Harper and Sardanowsky 1969][research_harper_sardanowsky_1969]
- [Harrington 1939][research_harrington_1939]
- [Harris 2000][research_harris_2000]
- [Harris and Harris 1997][research_harris_harris_1997]
- [Harris and Rickard 1979][research_harris_rickard_1979]
- [Harris et al 2000][research_harris_gautrey_2000]
- [Harris et al 2016][research_harris_arthurs_2016]
- [Harris et al 2019][research_harris_elliott_2019]
- [Harry and Trobaugh 1966][research_harry_trobaugh_1966]
- [Hart 1956][research_hart_1956]
- [Hart 1968][research_hart_1968]
- [Hart and Picha 1979][research_hart_picha_1979]
- [Hart et al 2016][research_hart_sytsma_2016]
- [Hartley and Pulliam 1988][research_hartley_pulliam_1988]
- [Hartley et al 1984][research_hartley_cwynar_1984]
- [Hartmann et al 2016][research_hartmann_meyer_2016]
- [Hartmann et al 2017][research_hartmann_meyer_2017]
- [Hasan et al 2025][research_hasan_redonnet_2025]
- [Hashemipour et al 2017][research_hashemipour_vasegh_2017]
- [Hashemzadeh et al 2016][research_hashemzadeh_sharifi_2016]
- [Hassan et al 1997][research_hassan_janakiram_1997]
- [Hastedt et al 2022][research_hastedt_theis_2022]
- [Hauser 1999][research_hauser_1999]
- [He et al 2020][research_he_tan_2020]
- [He et al 2021][research_he_zhang_2021]
- [He et al 2022][research_he_hu_2022]
- [He et al 2022][research_he_hu_2022_b]
- [He Mingyi et al 1998][research_hemingyi_jianghailin_1998]
- [Head 1962][research_head_1962]
- [Heald and Brassell 1976][research_heald_brassell_1976]
- [Healy 1958][research_healyfrederickm_1958]
- [Hebbar and Pashilkar 2016][research_hebbar_pashilkar_2016]
- [Hebbar et al 1991][research_hebbar_platzer_1991]
- [Hegde 2020][research_hegde_2020]
- [Hegde et al 2019][research_hegde_george_2019]
- [Helicopter Yaw Control 1990][research_helicopter_yaw_1990]
- [Heller and Clemente 1973][research_heller_clemente_1973]
- [Hemsch 1985][research_hemsch_1985]
- [Hemsch 1987][research_hemsch_1987]
- [Hemsch 1988][research_hemsch_1988]
- [Hemsch 1989][research_hemsch_1989]
- [Henkenjohann et al 2023][research_henkenjohann_nolte_2023]
- [Henkenjohann et al 2024][research_henkenjohann_nolte_2024]
- [Henn and Boronow 1959][research_henn_boronow_1959]
- [Herbst et al 2018][research_herbst_kahler_2018]
- [Herrera et al 2018][research_herrera_njeh_2018]
- [Herrick 1992][research_herrick_1992]
- [Herrington et al 2023][research_herrington_zahed_2023]
- [Herrlinger 1991][research_herrlinger_1991]
- [Herrmann and Ben-Asher 2016][research_herrmann_benasher_2016]
- [Herrmann and Schmidt 2018][research_herrmann_schmidt_2018]
- [Heryana et al 2022][research_heryana_krisnandi_2022]
- [Hess 1980][research_hess_1980]
- [Hess 1981][research_hess_1981]
- [Hess 1984][research_hess_1984]
- [Hess 1987][research_hess_1987]
- [Hess 1995][research_hess_1995]
- [Hess 1997][research_hess_1997]
- [Hess 1998][research_hess_1998]
- [Hess 2016][research_hess_2016]
- [Hess and Hess 1997][research_hess_hess_1997]
- [Hess and Hess 1997][research_hess_hess_1997_b]
- [Hess and McLean 2000][research_hessronalda_mcleanc_2000]
- [Hess and Peng 2018][research_hess_peng_2018]
- [Hess and Wells 2002][research_hess_wells_2002]
- [Hess and Wells 2003][research_hess_wells_2003]
- [Heyer et al 2020][research_heyer_kroezen_2020]
- [Hicks and Matheny 1989][research_hicksjohnw_mathenyneilw_1989]
- [Hienz and Vedova 1984][research_hienz_vedova_1984]
- [Higgins and Shomber 1964][research_higgins_shomber_1964]
- [Higgins and Shomber 1965][research_higgins_shomber_1965]
- [Hill 1987][research_hill_1987]
- [Hines and Gaffin 1976][research_hines_gaffin_1976]
- [Hirai and Satoh 1980][research_hirai_satoh_1980]
- [Hirano et al 2019][research_hirano_uchiyama_2019]
- [Hitzel 1988][research_hitzel_1988]
- [Hitzel 2017][research_hitzel_2017]
- [Hitzel and Zimper 2018][research_hitzel_zimper_2018]
- [Ho and Zhou 2023][research_ho_zhou_2023]
- [Ho et al 1993][research_ho_hang_1993]
- [Ho et al 1995][research_ho_hang_1995]
- [Ho et al 1998][research_ho_lim_1998]
- [Hodgkinson 2003][research_hodgkinson_2003]
- [Hodgkinson and Lamanna 1977][research_hodgkinson_lamanna_1977]
- [Hodgkinson et al 1990][research_hodgkinson_potsdam_1990]
- [Hoe et al 2012][research_hoegarrison_owensdonaldb_2012]
- [Hoffer et al 2015][research_hoffer_coopmans_2015]
- [Hoffler et al 1988][research_hoffler_rao_1988]
- [Hoffman and Stalford 1991][research_hoffman_stalford_1991]
- [Hofmann et al 2025][research_hofmann_hosseini_2025]
- [Hofsäβ and Holzapfel 2024][research_hofsa_holzapfel_2024]
- [Hogan and Rinde 1978][research_hogan_rinde_1978]
- [Hoh 1982][research_hoh_1982]
- [Hoh 1988][research_hoh_1988]
- [Hoh and Mitchell 1983][research_hoh_mitchell_1983]
- [Hoholis et al 2016][research_hoholis_steijl_2016]
- [Hollingsworth and Cohen 1971][research_hollingsworth_cohen_1971]
- [Hollmeier et al 1999][research_hollmeier_kopp_1999]
- [Holman 1876][research_holman_1876]
- [Holman 1885][research_holman_1885]
- [Holmes and Woehr 1971][research_holmes_woehr_1971]
- [Homola et al 2025][research_homola_li_2025]
- [Hong and Ma 2016][research_hong_ma_2016]
- [Hongyan and Xiaoyong 2026][research_hongyan_xiaoyong_2026]
- [Horn et al 2017][research_horn_thorsen_2017]
- [Horowitz 1964][research_horowitz_1964]
- [Horowitz 1965][research_horowitz_1965]
- [Horst et al 2017][research_horst_sommerwerk_2017]
- [Hosseini et al 2025][research_hosseini_bridges_2025]
- [Hosseini et al 2025][research_hosseini_hofmann_2025]
- [Hossny et al 2020][research_hossny_elbadawy_2020]
- [Hou et al 2011][research_hou_xue_2011]
- [Hougui et al 1995][research_hougui_balas_1995]
- [Houston 1937][research_houston_1937]
- [How 2008][research_how_2008]
- [Howard 1975][research_howard_1975]
- [Howard 1976][research_howard_1976]
- [Howard and Bray 1992][research_howard_bray_1992]
- [Hoxey et al 1997][research_hoxey_robertson_1997]
- [Hoyt et al 1980][research_hoyt_kempel_1980]
- [Hreha and Lutze 1983][research_hreha_lutze_1983]
- [Hreha and Lutze 1984][research_hreha_lutze_1984]
- [Hsiao 1988][research_hsiao_1988]
- [Hsiao et al 1997][research_hsiao_ho_1997]
- [Hsiao et al 2004][research_hsiao_wang_2004]
- [Hsieh and Wang 1976][research_hsieh_wang_1976]
- [Hu and Huang 2017][research_hu_huang_2017]
- [Hu et al 2024][research_hu_song_2024]
- [Hu et al 2025][research_hu_wen_2025]
- [Hu et al 2025][research_hu_zhao_2025]
- [Hu-Sheng Wu et al 2015][research_hushengwu_weizonglu_2015]
- [Huang 2016][research_huang_2016]
- [Huang and Wang 2001][research_huang_wang_2001]
- [Huang and Zhang 2020][research_huang_zhang_2020]
- [Huang et al 1992][research_huang_tylock_1992]
- [Huang et al 1999][research_huang_celi_1999]
- [Huang et al 2017][research_huang_pool_2017]
- [Huang et al 2022][research_huang_zhang_2022]
- [Huang et al 2026][research_huang_li_2026]
- [Huber 1995][research_huber_1995]
- [Huber 2022][research_huber_2022]
- [Huber and Schellenger 1994][research_huberpeter_schellengerharveyg_1994]
- [Hueschen 1984][research_hueschenrm_1984]
- [Huff 1949][research_huff_ww_1949]
- [Huguenin 1981][research_huguenin_1981]
- [Hull and Roger 1975][research_hull_roger_1975]
- [Humphreys and Watkinson 1972][research_humphreys_watkinson_1972]
- [Humphreys-Jennings et al 2020][research_humphreysjennings_lappas_2020]
- [Hung 1979][research_hung_1979]
- [Hung 1980][research_hung_1980]
- [Hunt and Gowadia 1981][research_hunt_gowadia_1981]
- [Hunter et al 2001][research_huntercraiga_vikensallya_2001]
- [Huntley et al 2019][research_huntley_woods_2019]
- [Huntoon et al 1979][research_huntoon_schohan_1979]
- [Huo et al 2021][research_huo_duan_2021]
- [Hutt and East 1985][research_hutt_east_1985]
- [Huzmezan 1998][research_huzmezan_1998]
- [Huzmezan and Maciejowski 1999][research_huzmezan_maciejowski_1999]
- [Hwang et al 2024][research_hwang_yoo_2024]
- [Hyde and Massie 1993][research_hydecharlesr_massiejeffreyj_1993]
- [Hyde et al 2014][research_hydedavidc_shweykkamalm_2014]
- [Hübener and Luckner 2026][research_hubener_luckner_2026]
- [Ibraheem 2019][research_ibraheem_2019]
- [Ibuka and Ishiguro 2023][research_ibuka_ishiguro_2023]
- [Idan and Merhav 1990][research_idan_merhav_1990]
- [Identification method of temperature corrections to aircraft engine thrust in flight tests 2023][research_identification_method_2023]
- [Identification, Modelling And Lateral Parameters Control Of Unmanned Aerial Vehicle 2015][research_identification_modelling_2015]
- [Iglesis et al 2021][research_iglesis_horri_2021]
- [Ignatyev 2018][research_ignatyev_2018]
- [Ikeda et al 2015][research_ikeda_atobe_2015]
- [Iliff 1980][research_iliff_1980]
- [Iliff 1987][research_iliff_1987]
- [Iliff and Maine 1983][research_iliff_maine_1983]
- [Iloputaife and Ma 1987][research_iloputaife_ma_1987]
- [Imran et al 2021][research_imran_stolkin_2021]
- [Inanc et al 2025][research_inanc_habboush_2025]
- [Incorporating agility flight test metrics concurrently into the aircraft preliminary design process 1994][research_incorporating_agility_1994]
- [Inertially augmented approach and landing systems 1971][research_inertially_augmented_1971]
- [Influence of interference of the wing and fuselage on aerodynamic characteristics 2018][research_influence_of_interference_2018]
- [Innocenti 1989][research_innocenti_1989]
- [Innocenti and Thukral 1991][research_innocenti_thukral_1991]
- [Innocenti et al 1998][research_innocenti_petretti_1998]
- [Inoue et al 2019][research_inoue_yasuda_2019]
- [Ioannis and Ioannis 2026][research_ioannis_ioannis_2026]
- [Ionita 1996][research_ionita_1996]
- [Irwanto and Artono 2018][research_irwanto_artono_2018]
- [Isaac et al 2024][research_isaac_pena_2024]
- [Ishibashi and Miyaji 2015][research_ishibashi_miyaji_2015]
- [Ishikawa and Yamazaki 2021][research_ishikawa_yamazaki_2021]
- [Ishmael and Wierzbanowski 1985][research_ishmaelsd_wierzbanowskit_1985]
- [Ishola et al 2024][research_ishola_whidborne_2024]
- [Islam et al 2015][research_islam_faraz_2015]
- [Ito et al 2016][research_ito_endo_2016]
- [Ito et al 2017][research_ito_murayama_2017]
- [Itsariyapinyo and Sharma 2016][research_itsariyapinyo_sharma_2016]
- [Ivan 1985][research_ivan_1985]
- [Ivler and Geyer 2024][research_ivler_geyer_2024]
- [Ivler et al 2022][research_ivler_truong_2022]
- [Iyengar and Mavris 2025][research_iyengar_mavris_2025]
- [Jabbari et al 2021][research_jabbari_esmaeili_2021]
- [Jack 1951][research_jackjohnr_1951]
- [Jacob et al 2026][research_jacob_stewart_2026]
- [Jacobson and Joshi 1977][research_jacobson_joshi_1977]
- [Jacobson and Joshi 1978][research_jacobson_joshi_1978]
- [Jafari and Spong 2017][research_jafari_spong_2017]
- [Jafari et al 2017][research_jafari_fehr_2017]
- [Jafari et al 2022][research_jafari_khakisedigh_2022]
- [Jaffe 1972][research_jaffe_1972]
- [Jaffrezic et al 2015][research_jaffrezic_ruetten_2015]
- [Jaganraj and Velu 2019][research_jaganraj_velu_2019]
- [Jain et al 2015][research_jain_sitaram_2015]
- [Jain et al 2025][research_jain_singla_2025]
- [Jameson 2009][research_jameson_2009]
- [Jansen 1980][research_jansen_1980]
- [Jansen and Van Kampen 2025][research_jansen_vankampen_2025]
- [Jardin and Mueller 2009][research_jardin_mueller_2009]
- [Jarrah 1989][research_jarrah_1989]
- [Jategaonkar et al 1997][research_jategaonkar_monnich_1997]
- [Jayaraman and Ghosh 2021][research_jayaraman_ghosh_2021]
- [Jayaraman et al 2021][research_jayaraman_giri_2021]
- [Jayaraman et al 2022][research_jayaraman_gaurav_2022]
- [Jeffrie and Rolston 1972][research_jeffrie_rolston_1972]
- [Jenkins 2008][research_jenkins_2008]
- [Jenney 1979][research_jenney_1979]
- [Jenney 1980][research_jenney_1980]
- [Jenney et al 1982][research_jenney_schreadley_1982]
- [Jentys and Breitsamter 2023][research_jentys_breitsamter_2023]
- [Jentzsch et al 2017][research_jentzsch_taubert_2017]
- [Jentzsch et al 2019][research_jentzsch_taubert_2019]
- [Jeong et al 2015][research_jeong_lee_2015]
- [Jeong et al 2018][research_jeong_park_2018]
- [Jeong et al 2024][research_jeong_jeong_2024]
- [Jeong et al 2024][research_jeong_kim_2024]
- [Jesudasan et al 2026][research_jesudasan_doherty_2026]
- [Jewell 1982][research_jewellwf_1982]
- [Jewell et al 1979][research_jewell_heffley_1979]
- [Ji et al 2021][research_ji_kim_2021]
- [Ji et al 2022][research_ji_chen_2022]
- [Ji et al 2022][research_ji_lu_2022]
- [Ji et al 2025][research_ji_avedisov_2025]
- [Jiang and Parimi 2021][research_jiang_parimi_2021]
- [Jiang et al 2019][research_jiang_zhang_2019]
- [Jiang et al 2025][research_jiang_li_2025]
- [Jianhong and Yanxiang 2026][research_jianhong_yanxiang_2026]
- [Jianliang Wang and Sundararajan 1994][research_jianliangwang_sundararajan_1994]
- [Jianmin Wang et al 2016][research_jianminwang_jinbowang_2016]
- [Jie Chen 1995][research_jiechen_1995]
- [Jie Chen 1998][research_jiechen_1998]
- [Jiguang Li et al 2016][research_jiguangli_xinchen_2016]
- [Jimenez et al 2016][research_jimenez_faerevaag_2016]
- [Jiméneze and Icaza 2000][research_jimeneze_icaza_2000]
- [Jin et al 2018][research_jin_song_2018]
- [Jin et al 2020][research_jin_liao_2020]
- [jingwei and jiaming 2020][research_jingwei_jiaming_2020]
- [Jo et al 2015][research_jo_park_2015]
- [Jo et al 2016][research_jo_park_2016]
- [Jo et al 2018][research_jo_choi_2018]
- [Johnsen et al 2022][research_johnsen_runnels_2022]
- [Johnson 1940][research_johnson_1940]
- [Johnson 1949][research_johnsonjosephl_1949]
- [Johnson 1972][research_johnson_1972]
- [Johnson 1986][research_johnson_1986]
- [Johnson et al 1980][research_johnsonjljr_newsomwa_1980]
- [Johnston and Hogge 1974][research_johnston_hogge_1974]
- [Johnston and Hogge 1976][research_johnston_hogge_1976]
- [Johnston et al 1965][research_johnston_culver_1965]
- [Johnston et al 1974][research_johnston_ashkenas_1974]
- [Johnston et al 1983][research_johnston_myers_1983]
- [Jones 1979][research_jonesrt_1979]
- [Jones 1995][research_jones_1995]
- [Jones and Hunter 1993][research_jones_hunter_1993]
- [Jones et al 2017][research_jones_milholen_2017]
- [Joosten et al 2023][research_joosten_stroosma_2023]
- [Jordan 1974][research_jordan_1974]
- [Jordan et al 2004][research_jordanthomas_langfordwilliam_2004]
- [Jordan et al 2005][research_jordanthomasl_langfordwilliamm_2005]
- [Jorgensen 1977][research_jorgensenlh_1977]
- [Jorgensen 1979][research_jorgensenlh_1979]
- [Joshi and Rickard 1981][research_joshi_rickard_1981]
- [Jothiraj et al 2019][research_jothiraj_miles_2019]
- [Jothiraj et al 2020][research_jothiraj_sharf_2020]
- [Joy et al 2016][research_joy_ibrahim_2016]
- [Jugo 2001][research_jugo_2001]
- [Juhasz et al 2020][research_juhasz_xin_2020]
- [Juhasz et al 2022][research_juhasz_celi_2022]
- [Juliana et al 2004][research_juliana_chu_2004]
- [Jun 2024][research_jun_2024]
- [Junfeng et al 2017][research_junfeng_wuzhou_2017]
- [Junfeng et al 2020][research_junfeng_wuzhou_2020]
- [Jung and Baeder 2023][research_jung_baeder_2023]
- [Junior Kuitche et al 2024][research_juniorkuitche_yanezbadillo_2024]
- [Junnarkar et al 2026][research_junnarkar_seiler_2026]
- [Jusko et al 2022][research_jusko_jones_2022]
- [Jyothy and John Wessley 2023][research_jyothy_johnwessley_2023]
- [Kadosh and Cukurel 2016][research_kadosh_cukurel_2016]
- [Kaletka and Fu 1993][research_kaletka_fu_1993]
- [Kalyankar et al 2024][research_kalyankar_pompe_2024]
- [Kamath et al 2025][research_kamath_sivakumar_2025]
- [Kamel et al 2015][research_kamel_ghamry_2015]
- [Kamel et al 2016][research_kamel_ghamry_2016]
- [Kamine and Bendrick 2008][research_kaminetovyhaber_bendrickgregga_2008]
- [Kamiyama and Yamazaki 2020][research_kamiyama_yamazaki_2020]
- [Kammer 2025][research_kammer_2025]
- [Kan et al 2023][research_kan_yao_2023]
- [Kanai and Nikiforuk 1982][research_kanai_nikiforuk_1982]
- [Kanai et al 1990][research_kanai_nikiforuk_1990]
- [Kaneba et al 2022][research_kaneba_mu_2022]
- [Kang et al 2016][research_kang_park_2016]
- [Kanneganti et al 2022][research_kanneganti_charan_2022]
- [Kao 1975][research_kao_1975]
- [Kao and Anderson 1981][research_kao_anderson_1981]
- [Kapuscinski et al 2020][research_kapuscinski_szczerba_2020]
- [Karabetsky 2018][research_karabetsky_2018]
- [Karali et al 2020][research_karali_demirezen_2020]
- [Karimi Kelayeh and Djavareshkian 2024][research_karimikelayeh_djavareshkian_2024]
- [Karn et al 2021][research_karn_kumar_2021]
- [Karthikeyan et al 2024][research_karthikeyan_ajay_2024]
- [Kase et al 2021][research_kase_fujita_2021]
- [Kase et al 2023][research_kase_mizoguchi_2023]
- [Kashikawa et al 1995][research_kashikawa_akagi_1995]
- [Katayanagi 2001][research_katayanagi_2001]
- [Katayanagi 2004][research_katayanagi_2004]
- [Katsanikakis and Bekiaris-Liberis 2025][research_katsanikakis_bekiarisliberis_2025]
- [Katsuyama et al 2023][research_katsuyama_sato_2023]
- [Katz 2017][research_katz_2017]
- [Kaufman and Berry 1976][research_kaufman_berry_1976]
- [Kauser and Burcham 2001][research_kauser_burcham_2001]
- [Kaygan and Ulusoy 2018][research_kaygan_ulusoy_2018]
- [Kazarin et al 2016][research_kazarin_golubev_2016]
- [Kazarin et al 2017][research_kazarin_mackunis_2017]
- [Kc et al 2019][research_kc_ngo_2019]
- [Keidel et al 2019][research_keidel_fasel_2019]
- [Keidel et al 2020][research_keidel_fasel_2020]
- [Keldysh 1958][research_keldysh_1958]
- [Keller et al 2026][research_keller_mckillipjr_2026]
- [Kellett 1996][research_kellett_1996]
- [Kellett et al 1996][research_kellett_baguley_1996]
- [Kellock and Miller 1971][research_kellock_miller_1971]
- [Kellström 1936][research_kellstrom_1936]
- [Kemper and Cotting 2016][research_kemper_cotting_2016]
- [Kentfield 1975][research_kentfield_1975]
- [Kentfield 1975][research_kentfield_1975_b]
- [Kerney and White 1975][research_kerney_white_1975]
- [Keshmiri et al 2017][research_keshmiri_lan_2017]
- [Key 1971][research_key_1971]
- [Key 1982][research_key_1982]
- [Keyes 1927][research_keyes_1927]
- [Khalid 2016][research_khalid_2016]
- [Khalid 2017][research_khalid_2017]
- [Khamvilai et al 2024][research_khamvilai_huang_2024]
- [Khan 2019][research_khan_2019]
- [Khan 2023][research_khan_2023]
- [Khan and Nahon 2015][research_khan_nahon_2015]
- [Khan et al 2022][research_khan_iqbal_2022]
- [Kharchenko et al 2017][research_kharchenko_kuzmenko_2017]
- [Kharchenko et al 2017][research_kharchenko_matiychyk_2017]
- [Kharitonov 1999][research_kharitonov_1999]
- [Kharrat 2024][research_kharrat_2024]
- [Khouloud and Ali 2023][research_khouloud_ali_2023]
- [Kidd and Bull 1963][research_kidd_bull_1963]
- [Kiefer et al 2016][research_kieferjm_johnsonmd_2016]
- [Kiely and Agarwal 2023][research_kiely_agarwal_2023]
- [Kigotho et al 2022][research_kigotho_bodylski_2022]
- [Kikkawa and Uchiyama 2017][research_kikkawa_uchiyama_2017]
- [Kikkawa and Uchiyama 2017][research_kikkawa_uchiyama_2017_b]
- [Kikuchi et al 2016][research_kikuchi_misaka_2016]
- [Kim 1995][research_kim_1995]
- [Kim 2023][research_kim_2023]
- [Kim and Kunz 2016][research_kim_kunz_2016]
- [Kim and Kunz 2017][research_kim_kunz_2017]
- [Kim and Oh 2017][research_kim_oh_2017]
- [Kim et al 2003][research_kim_lee_2003]
- [Kim et al 2015][research_kim_jung_2015]
- [Kim et al 2022][research_kim_sohn_2022]
- [Kim et al 2025][research_kim_koh_2025]
- [Kimathi and Lantos 2024][research_kimathi_lantos_2024]
- [Kimberlin 2001][research_kimberlin_2001]
- [King 1993][research_davidwking_1993]
- [Kingcombe and Dunning 1980][research_kingcombe_dunning_1980]
- [Kirk 1961][research_kirkdonnb_1961]
- [Kirsch et al 2025][research_kirsch_fathi_2025]
- [Kish et al 1996][research_kish_leggett_1996]
- [Kish et al 1997][research_kish_mosle_1997]
- [Kish et al 1997][research_kish_mosleiii_1997]
- [Kisslinger and Wendl 1971][research_kisslinger_wendl_1971]
- [Kistyarev and Wang 2025][research_kistyarev_wang_2025]
- [Kiyak and Ermeydan 2018][research_kiyak_ermeydan_2018]
- [Klafin 1988][research_klafin_1988]
- [Klauck and Keßler 2025][research_klauck_kessler_2025]
- [Klein 1977][research_klein_1977]
- [Klein 1978][research_klein_1978]
- [Klein 1989][research_klein_1989]
- [Klein and Murphy 2001][research_klein_murphy_2001]
- [Klein et al 1982][research_kleinrw_lapinsm_1982]
- [Klein et al 2016][research_klein_kashawlic_2016]
- [Klein et al 2017][research_klein_krainski_2017]
- [Klimas and Kilikevičius 2024][research_klimas_kilikevicius_2024]
- [Klinar and Healy 1955][research_klinarwalterj_healyfrederickm_1955]
- [Klose et al 2018][research_klose_jacobs_2018]
- [Klyde et al 1995][research_klyde_aponso_1995]
- [Klyde et al 2001][research_klyde_brenner_2001]
- [Klyde et al 2018][research_klyde_schulze_2018]
- [Klyde et al 2020][research_klyde_mitchell_2020]
- [Klyde et al 2021][research_klyde_lampton_2021]
- [Knighton 1992][research_knightondonnal_1992]
- [Ko et al 2019][research_ko_kang_2019]
- [Kochersberger et al 2017][research_kochersberger_ohanian_2017]
- [Kocurek et al 1997][research_kocurek_durham_1997]
- [Koduri et al 2016][research_koduri_rodriguezayerbe_2016]
- [Koduri et al 2016][research_koduri_rodriguezayerbe_2016_b]
- [Kofman and Becus 1996][research_kofman_becus_1996]
- [Kogler and Quam 1983][research_kogler_quam_1983]
- [Koh 1968][research_koh_1968]
- [Kohlman 1977][research_kohlman_1977]
- [Kohlman 1979][research_kohlman_1979]
- [Kohlman and Brainerd 1974][research_kohlman_brainerd_1974]
- [Kohnhorst and Magnacca 1980][research_kohnhorst_magnacca_1980]
- [Kojima et al 2024][research_kojima_hidaka_2024]
- [Kokolios 1994][research_kokolios_1994]
- [Konar et al 1974][research_konar_mahesh_1974]
- [Konatala et al 2021][research_konatala_vankampen_2021]
- [Konatala et al 2024][research_konatala_milz_2024]
- [Konishi et al 2023][research_konishi_kojima_2023]
- [Koopman and Zammit-Mangion 2024][research_koopman_zammitmangion_2024]
- [Kopecki 2016][research_kopecki_2016]
- [Korkischko and Konrath 2017][research_korkischko_konrath_2017]
- [Korsun and Moung Htang 2023][research_korsun_mounghtang_2023]
- [Korsun et al 2018][research_korsun_stulovskii_2018]
- [Koryanov and Kukharenko 2023][research_koryanov_kukharenko_2023]
- [Kostić et al 2024][research_kostic_simonovic_2024]
- [Kotikalpudi et al 2015][research_kotikalpudi_pfifer_2015]
- [Kotsabasis 1981][research_kotsabasis_1981]
- [Kou et al 2021][research_kou_wang_2021]
- [Kouser et al 2024][research_kouser_aliyu_2024]
- [Kouser et al 2024][research_kouser_kurtulus_2024]
- [Kouvaritakis et al 1979][research_kouvaritakis_murray_1979]
- [Kowal 2002][research_kowal_2002]
- [Kraft 2018][research_kraft_2018]
- [Kramer and Smith 1994][research_kramerbrian_smithbrooke_1994]
- [Kramer et al 2018][research_kramer_williams_2018]
- [Krause et al 2024][research_krause_funke_2024]
- [Kriechbaum and Stineman 1972][research_kriechbaum_stineman_1972]
- [Krimphove et al 2023][research_krimphove_schutt_2023]
- [Krishnamurthy and Luckner 2017][research_krishnamurthy_luckner_2017]
- [Krithiga 2024][research_rs_2024]
- [Krohn 1988][research_krohn_1988]
- [Kuang and Zhu 2015][research_kuang_zhu_2015]
- [Kubo 1999][research_kubo_1999]
- [Kuchar 2018][research_kuchar_2018]
- [Kuchar and Looye 2018][research_kuchar_looye_2018]
- [Kuester et al 2016][research_kuester_borgoltz_2016]
- [Kuhn 1981][research_kuhn_1981]
- [Kumar 2015][research_kumar_2015]
- [Kumar and Ghosh 2017][research_kumar_ghosh_2017]
- [Kumar and Ghosh 2018][research_kumar_ghosh_2018]
- [Kumar and Ghosh 2018][research_kumar_ghosh_2018_b]
- [Kumar and Ghosh 2018][research_kumar_ghosh_2018_c]
- [Kumar and Ghosh 2023][research_kumar_ghosh_2023]
- [Kumar and Hote 2022][research_kumar_hote_2022]
- [Kumar and Kothari 2024][research_kumar_kothari_2024]
- [Kumar and Mukherjee 2024][research_kumarg_mukherjee_2024]
- [Kumar and Prakash 2022][research_kumar_prakash_2022]
- [Kumar and Rao 2004][research_kumar_rao_2004]
- [Kumar et al 2015][research_kumar_steck_2015]
- [Kumar et al 2015][research_kumar_tomar_2015]
- [Kumar et al 2018][research_kumar_bombuwela_2018]
- [Kumar et al 2018][research_kumar_srivastava_2018]
- [Kumar et al 2020][research_kumar_bhargavapuri_2020]
- [Kumar et al 2022][research_kumar_kumar_2022]
- [Kumar et al 2024][research_kumar_shankar_2024]
- [Kumar et al 2026][research_kumar_mittal_2026]
- [Kumar Gupta et al 2018][research_kumargupta_aaswathanaray_2018]
- [Kumari and Raghunath 2016][research_kumari_raghunath_2016]
- [Kumtepe et al 2022][research_kumtepe_pollack_2022]
- [Kunwar and Chakraborty 2025][research_kunwar_chakraborty_2025]
- [Kunwar et al 2026][research_kunwar_putra_2026]
- [Kurade et al 2021][research_kurade_venkatakrishnan_2021]
- [Kurbanismailov et al 2021][research_kurbanismailov_tarlanov_2021]
- [Kurtulus 2019][research_kurtulus_2019]
- [Kurtulus 2021][research_kurtulus_2021]
- [Kus and Ergazi 2025][research_kus_ergazi_2025]
- [Kutschera and Render 1999][research_kutschera_render_1999]
- [Kuwamura and Hara 2017][research_kuwamura_hara_2017]
- [Kuzu et al 2015][research_kuzu_bogosyan_2015]
- [Kwiek 2019][research_kwiek_2019]
- [Kästner et al 2021][research_kastner_epple_2021]
- [L'Afflitto et al 2018][research_lafflitto_anderson_2018]
- [Lacaille and Loro 2016][research_lacaille_loro_2016]
- [Lackey and Hadfield 1992][research_lackey_hadfield_1992]
- [Lai and Kamaruddin 2018][research_lai_kamaruddin_2018]
- [Laiosa 1985][research_laiosa_1985]
- [Laitone 1947][research_laitone_1947]
- [Laitone and Lin 1972][research_laitone_lin_1972]
- [Laitone and Lin 1973][research_laitone_lin_1973]
- [Lakkur et al 2025][research_lakkur_schmidt_2025]
- [Lallemand 2000][research_lallemand_2000]
- [Lam and Stollenwerk 1966][research_lam_stollenwerk_1966]
- [Lampard 1978][research_lampard_1978]
- [Lamperski 2022][research_lamperski_2022]
- [Lampton et al 2024][research_lampton_klyde_2024]
- [Lampton et al 2024][research_lampton_klyde_2024_b]
- [Landa et al 2018][research_landa_klug_2018]
- [Landgraf 1964][research_landgraf_1964]
- [Landgraf 1965][research_landgraf_1965]
- [Lane et al 2001][research_lane_carignan_2001]
- [Lang et al 2024][research_lang_li_2024]
- [Langan and Samuels 1995][research_langan_samuels_1995]
- [Lanser and Meyn 1992][research_lanserwendyr_meynlarrya_1992]
- [Lanteigne and O'Reilly 2020][research_lanteigne_oreilly_2020]
- [Lapins et al 1982][research_lapinsm_kleinrw_1982]
- [Larsen 1975][research_larsen_1975]
- [Larson 1986][research_larson_1986]
- [Larson et al 2009][research_larsonrichardr_burkenjohnj_2009]
- [Larsson 2025][research_larsson_2025]
- [Larsson et al 2020][research_larsson_sobron_2020]
- [Lateral Control of a Hypersonic Aircraft 2025][research_lateral_control_2025]
- [Laudeman 1972][research_laudeman_1972]
- [Laughter 2012][research_laughterseana_2012]
- [Lavretsky 2019][research_lavretsky_2019]
- [Lavretsky and Misovec 2002][research_lavretsky_misovec_2002]
- [Lawrence and Mills 2002][research_lawrence_mills_2002]
- [Lawrence et al 2018][research_lawrence_theodore_2018]
- [Layton 1974][research_laytongp_1974]
- [Le Yi Wang and Ji-Feng Zhang 2001][research_leyiwang_jifengzhang_2001]
- [Lebacqz 1974][research_lebacqzjv_1974]
- [Lecuyer 1970][research_lecuyer_1970]
- [Lee 1946][research_lee_1946]
- [Lee 1947][research_lee_1947]
- [Lee 1952][research_leehenrya_1952]
- [Lee 1963][research_leehenrya_1963]
- [Lee 2016][research_lee_2016]
- [Lee 2024][research_lee_2024]
- [Lee and Chang 1998][research_lee_chang_1998]
- [Lee and Han 2019][research_lee_han_2019]
- [Lee and Hedrick 1994][research_lee_hedrick_1994]
- [Lee and Kim 2001][research_lee_kim_2001]
- [Lee and Ko 2017][research_lee_ko_2017]
- [Lee and Ko 2018][research_lee_ko_2018]
- [Lee and Lan 1992][research_lee_lan_1992]
- [Lee and Libbey 1961][research_leehenrya_libbeycharlese_1961]
- [Lee and Marnineau-Mes 1996][research_lee_marnineaumes_1996]
- [Lee and Van Kampen 2021][research_lee_vankampen_2021]
- [Lee and Vining 2018][research_lee_vining_2018]
- [Lee et al 2001][research_lee_shin_2001]
- [Lee et al 2003][research_lee_rodchenko_2003]
- [Lee et al 2015][research_lee_kawai_2015]
- [Lee et al 2015][research_lee_kawai_2015_b]
- [Lee et al 2015][research_lee_nonomura_2015]
- [Lee et al 2015][research_lee_nonomura_2015_b]
- [Lee et al 2018][research_lee_song_2018]
- [Lee et al 2020][research_lee_kim_2020]
- [Lee et al 2021][research_lee_benedict_2021]
- [Lee et al 2021][research_lee_huang_2021]
- [Lee et al 2021][research_lee_huang_2021_b]
- [Lee et al 2021][research_lee_kim_2021]
- [Lee et al 2021][research_lee_saj_2021]
- [Lee et al 2024][research_lee_tai_2024]
- [Lee et al 2026][research_lee_horn_2026]
- [Legowo et al 2019][research_legowo_sulaeman_2019]
- [Lei et al 2017][research_lei_liu_2017]
- [Lei et al 2025][research_lei_dong_2025]
- [Leishman 2026][research_leishman_2026]
- [Leonard and Arnett 1980][research_leonardrg_arnettem_1980]
- [Lerro et al 2020][research_lerro_brandl_2020]
- [Lesalli and Cahyono 2020][research_lesalli_cahyono_2020]
- [Leshikar et al 2021][research_leshikar_eves_2021]
- [Lessing and Butler 1959][research_lessinghenryc_butlerjamesk_1959]
- [Lestari et al 2025][research_lestari_ridwan_2025]
- [Leung and Redonnet 2022][research_leung_redonnet_2022]
- [Leung et al 2019][research_leung_moszczynski_2019]
- [Levi and Nelson 1963][research_levi_nelson_1963]
- [Levison 1982][research_levison_1982]
- [Levison and Papazian 1987][research_levison_papazian_1987]
- [Levy 2003][research_levy_2003]
- [Levy and Tobak 1970][research_levyjr_tobak_1970]
- [Leylek and Costello 2015][research_leylek_costello_2015]
- [Li 2024][research_li_2024]
- [Li and Cai 2026][research_li_cai_2026]
- [Li and Gao 2025][research_li_gao_2025]
- [Li and Liu 2016][research_li_liu_2016]
- [Li and Ma 2014][research_li_ma_2014]
- [Li and van Kampen 2024][research_li_vankampen_2024]
- [Li and Wang 2017][research_li_wang_2017]
- [Li and Yang 2017][research_li_yang_2017]
- [Li and Yang 2017][research_li_yang_2017_b]
- [Li et al 1994][research_li_ge_1994]
- [Li et al 2015][research_li_liu_2015]
- [Li et al 2016][research_li_guo_2016]
- [Li et al 2016][research_li_yu_2016]
- [Li et al 2017][research_li_qin_2017]
- [Li et al 2017][research_li_yong_2017]
- [Li et al 2018][research_li_dong_2018]
- [Li et al 2018][research_li_shi_2018]
- [Li et al 2018][research_li_zhang_2018]
- [Li et al 2019][research_li_zhang_2019]
- [Li et al 2021][research_li_liu_2021]
- [Li et al 2022][research_li_bai_2022]
- [Li et al 2022][research_li_gu_2022]
- [Li et al 2022][research_li_sun_2022]
- [Li et al 2022][research_li_xu_2022]
- [Li et al 2023][research_li_nagata_2023]
- [Li et al 2023][research_li_sun_2023]
- [Li et al 2024][research_li_zhang_2024]
- [Li et al 2024][research_li_zheng_2024]
- [Li et al 2025][research_li_lian_2025]
- [Li et al 2026][research_li_han_2026]
- [Li et al 2026][research_li_li_2026]
- [Li et al 2026][research_li_sheng_2026]
- [Li Yan et al 2000][research_liyan_sundarajan_2000]
- [Liang 2025][research_liang_2025]
- [Liang et al 2022][research_liang_yang_2022]
- [Liang et al 2025][research_liang_wang_2025]
- [Liang et al 2026][research_liang_kou_2026]
- [Liberatori et al 2023][research_liberatori_valorani_2023]
- [Libório et al 2025][research_liborio_pimentel_2025]
- [Lichota 2016][research_lichota_2016]
- [Lichota 2023][research_lichota_2023]
- [Lichota et al 2016][research_lichota_ohme_2016]
- [Liem et al 2015][research_liem_mader_2015]
- [Liew et al 2005][research_liewkh_uripe_2005]
- [Liew et al 2005][research_liewkh_uripe_2005_b]
- [Liew et al 2005][research_liewkh_uripe_2005_c]
- [Lijewski 1986][research_lijewski_1986]
- [Lim et al 2025][research_lim_hur_2025]
- [Lim et al 2026][research_lim_kurahashi_2026]
- [Lin 2025][research_lin_2025]
- [Lin and Han 1986][research_lin_han_1986]
- [Lin and Rockwell 1995][research_lin_rockwell_1995]
- [Lin and Yeh 1999][research_lin_yeh_1999]
- [Lin et al 1992][research_lin_robinson_1992]
- [Lin et al 1998][research_lin_ge_1998]
- [Lin et al 2019][research_lin_zhang_2019]
- [Lind and Protopapas 1977][research_lind_protopapas_1977]
- [Lindberg and Pates 2023][research_lindberg_pates_2023]
- [Linear and neural network feedback for flight control decoupling 1996][research_linear_and_1996]
- [Linehan 1996][research_linehan_1996]
- [Linehan and Mohseni 2016][research_linehan_mohseni_2016]
- [Ling 1983][research_ling_1983]
- [Litt et al 2012][research_littjonathans_sowerst_2012]
- [Littleboy et al 1997][research_littleboy_smith_1997]
- [Liu 2023][research_liu_2023]
- [Liu 2024][research_liu_2024]
- [Liu 2024][research_liu_2024_b]
- [Liu and Brandel 2004][research_liu_brandel_2004]
- [Liu and Chen 2016][research_liu_chen_2016]
- [Liu and Hu 2014][research_liu_hu_2014]
- [Liu and Jiang 2024][research_liu_jiang_2024]
- [Liu and Jiao 2017][research_liu_jiao_2017]
- [Liu and Luo 2022][research_liu_luo_2022]
- [Liu and Sirignano 2000][research_liu_sirignano_2000]
- [Liu and Xiao 2020][research_liu_xiao_2020]
- [Liu and Yang 2024][research_liu_yang_2024]
- [Liu and Zhang 2022][research_liu_zhang_2022_b]
- [Liu and Zhu 2021][research_liu_zhu_2021]
- [Liu et al 2015][research_liu_jiang_2015]
- [Liu et al 2015][research_liu_wang_2015]
- [Liu et al 2016][research_liu_luo_2016]
- [Liu et al 2016][research_liu_yuan_2016]
- [Liu et al 2017][research_liu_huang_2017]
- [Liu et al 2017][research_liu_litvinenko_2017]
- [Liu et al 2018][research_liu_gao_2018]
- [Liu et al 2018][research_liu_luo_2018]
- [Liu et al 2018][research_liu_nakata_2018]
- [Liu et al 2018][research_liu_sun_2018]
- [Liu et al 2018][research_liu_zhou_2018]
- [Liu et al 2019][research_liu_dong_2019]
- [Liu et al 2020][research_liu_shan_2020]
- [Liu et al 2021][research_liu_li_2021]
- [Liu et al 2021][research_liu_luo_2021]
- [Liu et al 2022][research_liu_gao_2022]
- [Liu et al 2022][research_liu_wang_2022]
- [Liu et al 2022][research_liu_zhang_2022]
- [Liu et al 2023][research_liu_hao_2023]
- [Liu et al 2023][research_liu_zhang_2023]
- [Liu et al 2024][research_liu_an_2024]
- [Liu et al 2024][research_liu_di_2024]
- [Liu et al 2024][research_liu_gao_2024]
- [Liu et al 2024][research_liu_hao_2024]
- [Liu et al 2024][research_liu_lu_2024]
- [Liu et al 2025][research_liu_zhang_2025]
- [Liu et al 2025][research_liu_zheng_2025]
- [Liu et al 2026][research_liu_li_2026]
- [Liu et al 2026][research_liu_li_2026_b]
- [Liu et al 2026][research_liu_wang_2026]
- [Livneh 1995][research_livneh_1995]
- [Livneh 1995][research_livneh_1995_b]
- [Lloyds Raja and Ali 2017][research_lloydsraja_ali_2017]
- [Lockenour and Layton 1976][research_lockenour_layton_1976]
- [Loechert et al 2018][research_loechert_huber_2018]
- [Lofthouse and Cummings 2015][research_lofthouse_cummings_2015]
- [Lofthouse and Cummings 2017][research_lofthouse_cummings_2017]
- [Loh and Lusty 1974][research_loh_lustyjr_1974]
- [Long 1968][research_long_1968]
- [Long 2016][research_long_2016]
- [Long 2016][research_long_2016_b]
- [Long Lu and Turkoglu 2015][research_longlu_turkoglu_2015]
- [Loo 1969][research_loo_1969]
- [Loposer and Rumsey 1954][research_loposerjdan_rumseycharlesb_1954]
- [Loranchet et al 2025][research_loranchet_tiako_2025]
- [Lorell 1989][research_lorell_1989]
- [Lorenzetti et al 1969][research_lorenzetti_nelsen_1969]
- [Lorincz 1980][research_lorincz_1980]
- [Loro and Lacaille 2017][research_loro_lacaille_2017]
- [Lovell 1954][research_lovellpowellmjr_1954]
- [Lowry et al 1978][research_lowry_rich_1978]
- [Lowson and Riley 1994][research_lowson_riley_1994]
- [Lowson and Riley 1995][research_lowson_riley_1995]
- [Lu 2017][research_lu_2017]
- [Lu and Martos 2021][research_lu_martos_2021]
- [Lu and Turkoglu 2016][research_lu_turkoglu_2016]
- [Lu and Turkoglu 2018][research_lu_turkoglu_2018]
- [Lu and Van Kampen 2015][research_lu_vankampen_2015]
- [Lu et al 2015][research_lu_zhang_2015]
- [Lu et al 2016][research_lu_vankampen_2016]
- [Lu et al 2016][research_lu_zhang_2016]
- [Lu et al 2019][research_lu_zhang_2019]
- [Lu et al 2024][research_lu_wu_2024]
- [Lubing et al 2017][research_lubing_yang_2017]
- [Lucarini et al 2025][research_lucarini_dirito_2025]
- [Lucas 1978][research_lucas_1978]
- [Luckert 1973][research_luckert_1973]
- [Luckring et al 1989][research_luckringjamesm_foxcharleshjr_1989]
- [Luckring et al 2022][research_luckring_taylor_2022]
- [Lueckhof and Stumpf 2018][research_lueckhof_stumpf_2018]
- [Luhanga and Mwandosya 1986][research_luhanga_mwandosya_1986]
- [Lungu and Lungu 2015][research_lungu_lungu_2015]
- [Lungu and Lungu 2016][research_lungu_lungu_2016]
- [Lungu and Lungu 2016][research_lungu_lungu_2016_b]
- [Luo and Wang 2017][research_luo_wang_2017]
- [Luo et al 2019][research_luo_du_2019]
- [Luo et al 2022][research_luo_zhang_2022]
- [Luo et al 2025][research_luo_cui_2025]
- [Luria 2017][research_luria_2017]
- [Lusardi 2023][research_lusardi_2023]
- [Luu and Ochi 2023][research_luu_ochi_2023]
- [Luz et al 2023][research_luz_silva_2023]
- [Ly 2002][research_ly_2002]
- [Ly and Ho 1986][research_lyul_hojk_1986]
- [Lynch 2012][research_lynch_2012]
- [Lytovchenko 2026][research_lytovchenko_2026]
- [Lyu et al 2022][research_lyu_gong_2022]
- [Lyu et al 2023][research_lyu_ye_2023]
- [Lyu et al 2023][research_lyu_yin_2023]
- [Lyu et al 2023][research_lyu_zhang_2023]
- [Lyu et al 2024][research_lyu_sun_2024]
- [Ma 2019][research_ma_2019]
- [Ma 2025][research_ma_2025]
- [Ma and Peng 2021][research_ma_peng_2021]
- [Ma et al 2008][research_ma_li_2008]
- [Ma et al 2015][research_ma_du_2015]
- [Ma et al 2019][research_ma_dong_2019]
- [Ma et al 2019][research_ma_zhu_2019]
- [Ma et al 2019][research_ma_zhu_2019_b]
- [Ma et al 2020][research_ma_shi_2020]
- [Ma et al 2023][research_ma_hui_2023]
- [Ma et al 2024][research_ma_yu_2024]
- [Ma et al 2025][research_ma_yao_2025]
- [Maadani et al 2023][research_maadani_lopezmuro_2023]
- [MacAllister 1955][research_macallister_1955]
- [Mace et al 1989][research_mace_smereczniak_1989]
- [Maddalon et al 2021][research_jeffreymmaddalon_kurtaswieringa_2021]
- [Maeda and Vidyasagar 1985][research_maeda_vidyasagar_1985]
- [Magrini et al 2021][research_magrini_buosi_2021]
- [Mahesh et al 2023][research_mahesh_shah_2023]
- [Mahgoub and Cortelezzi 2020][research_mahgoub_cortelezzi_2020]
- [Mahns and Amitay 2025][research_mahns_amitay_2025]
- [Mahulikar et al 2022][research_mahulikar_rastogi_2022]
- [Mahulkar 2010][research_mahulkar_2010]
- [Maji et al 2024][research_maji_pandi_2024]
- [Makarenko et al 2017][research_makarenko_makarov_2017]
- [Makgantai et al 2021][research_makgantai_subaschandar_2021]
- [Malaek and Sajjadi Kia 2004][research_malaek_sajjadikia_2004]
- [Malaek and Soltan-Mohammed 2001][research_malaek_soltanmohammed_2001]
- [Malcolm and Ng 1990][research_malcolmgn_ngtt_1990]
- [Malcom 1969][research_malcom_1969]
- [Maldonado et al 2017][research_maldonado_sarker_2017]
- [Malik et al 2018][research_malik_asrar_2018]
- [Malik et al 2020][research_malik_masud_2020]
- [Malik et al 2021][research_malik_masud_2021]
- [Mallavalli and Fekih 2018][research_mallavalli_fekih_2018]
- [Mallavalli and Fekih 2019][research_mallavalli_fekih_2019]
- [Mallery and Neebe 1965][research_mallery_neebe_1965]
- [Malloy and Chang 1998][research_malloy_chang_1998]
- [Malmuth et al 1983][research_malmuth_wu_1983]
- [Malpica and Lusardi 2013][research_malpica_lusardi_2013]
- [Malpica et al 2023][research_malpica_suh_2023]
- [Mammadova et al 2025][research_mammadova_slavov_2025]
- [Mamou and Broughton 2023][research_mamou_broughton_2023]
- [Manar et al 2016][research_manar_cassell_2016]
- [Mandal and Gu 2016][research_mandal_gu_2016]
- [Mandal and Gu 2016][research_mandal_gu_2016_b]
- [Mann et al 1987][research_mannmichaelj_huffmanjarrettk_1987]
- [Manoilo 2025][research_manoilo_2025]
- [Manolescu 1994][research_manolescu_1994]
- [Mansor et al 2015][research_mansor_nogoud_2015]
- [Mansur and Lanteigne 2020][research_mansur_lanteigne_2020]
- [Mao and Chen 2026][research_mao_chen_2026]
- [Mao et al 2022][research_mao_gong_2022]
- [Mar Aye et al 2020][research_maraye_pholdee_2020]
- [Marchman 1981][research_marchmaniii_1981]
- [Marchman 1987][research_marchman_1987]
- [Margason and Hoad 1980][research_margason_hoad_1980]
- [Margetts et al 2015][research_margetts_bingham_2015]
- [Marino and Mastrocola 1952][research_marinoalfreda_mastrocolan_1952]
- [Markofski and Bailey 1999][research_markofski_bailey_1999]
- [Marques 2013][research_marques_2013]
- [Martin 2025][research_martin_2025]
- [Martin and Lind 2025][research_martin_lind_2025]
- [Martin et al 1976][research_martin_saunders_1976]
- [Martorella et al 1981][research_martorella_kelly_1981]
- [Martínez-Ramírez and Rodríguez-Cortés 2022][research_martinezramirez_rodriguezcortes_2022]
- [Marvasti and Boutayeb 2024][research_marvasti_boutayeb_2024]
- [Masak 1965][research_masak_1965]
- [Masaoka and Hashimoto 2024][research_masaoka_hashimoto_2024]
- [Mason 1991][research_mason_1991]
- [Mason and Crowther 2004][research_mason_crowther_2004]
- [Mason and Ravi 1994][research_mason_ravi_1994]
- [Masubuchi et al 2004][research_masubuchi_kato_2004]
- [Matamoros and de Visser 2018][research_matamoros_devisser_2018]
- [Mateescu 1986][research_mateescu_1986]
- [Mateescu 1987][research_mateescu_1987]
- [Mathur and Atkins 2023][research_mathur_atkins_2023]
- [Matos and Marta 2025][research_matos_marta_2025]
- [Matt et al 2025][research_matt_chao_2025]
- [Mattern et al 1989][research_matternduane_gargsanjay_1989]
- [Matthews and Yi 2019][research_matthews_yi_2019]
- [Matthews and Yi 2021][research_matthews_yi_2021]
- [Mattingly 1998][research_mattingly_1998]
- [Matveev and Wheeler 2022][research_matveev_wheeler_2022]
- [Matías-García et al 2025][research_matiasgarcia_bardera_2025]
- [Maughmer and Somers 1987][research_maughmer_somers_1987]
- [Maughmer and Somers 1987][research_maughmer_somers_1987_b]
- [Maughmer et al 1990][research_maughmermarkd_ozoroskil_1990]
- [Maughmer et al 2021][research_maughmer_axten_2021]
- [Maughmer et al 2023][research_maughmer_axten_2023]
- [Maunder 1979][research_maunder_1979]
- [Maurya et al 2025][research_maurya_patel_2025]
- [Mavris et al 1998][research_mavris_delaurentis_1998]
- [Maybeck and Stevens 1990][research_maybeck_stevens_1990]
- [Maybeck and Stevens 1991][research_maybeck_stevens_1991]
- [Mayhew and Gleason 1988][research_mayhew_gleason_1988]
- [Mayya et al 2022][research_mayya_karnick_2022]
- [Mazenc and Malisoff 2020][research_mazenc_malisoff_2020]
- [Mazenc and Malisoff 2022][research_mazenc_malisoff_2022]
- [Mazza 1992][research_mazza_1992]
- [McClinton et al 1998][research_mcclinton_voland_1998]
- [McCormick 1969][research_mccormick_1969]
- [McCrink and Gregory 2017][research_mccrink_gregory_2017]
- [McDaniel 2017][research_mcdaniel_2017]
- [McDonald and Farris 1964][research_mcdonald_farris_1964]
- [McFarland and D'Souza 1994][research_mcfarland_dsouza_1994]
- [McGough et al 1974][research_mcgough_moses_1974]
- [McGREGOR and Smith 1966][research_mcgregor_smith_1966]
- [McGuigan 1970][research_mcguigan_1970]
- [McInally 1963][research_mcinally_1963]
- [McInville and Moore 1994][research_mcinville_moore_1994]
- [McKeehen 1998][research_mckeehen_1998]
- [McKeehen and Cord 1997][research_mckeehen_cord_1997]
- [McKenzie 1973][research_mckenzie_1973]
- [McLean 1994][research_mclean_1994]
- [McLean and Aslam-Mir 1992][research_mclean_aslammir_1992]
- [McLean and Aslam-Mir 1994][research_mclean_aslammir_1994]
- [McLean and Aslam-Mir 1994][research_mclean_aslammir_1994_b]
- [McMaster and Schenk 1974][research_mcmaster_schenk_1974]
- [McMinn and Jackson 2002][research_mcminn_jackson_2002]
- [Meckstroth and Blake 2015][research_meckstroth_blake_2015]
- [Meckstroth and Ordóñez 2020][research_meckstroth_ordonez_2020]
- [Meckstroth and Ordóñez 2020][research_meckstroth_ordonez_2020_b]
- [Mehalic and Ziemianski 1980][research_mehaliccm_ziemianskija_1980]
- [Mehra and Eupta 1975][research_mehrark_euptank_1975]
- [Mehra and Tyler 1973][research_mehrark_tylerjs_1973]
- [Mei et al 2023][research_mei_zhou_2023]
- [Melekhin and Khachumov 2021][research_melekhin_khachumov_2021]
- [Mello and Agnew 1979][research_mello_agnew_1979]
- [Meng et al 2015][research_meng_yan_2015]
- [Meng et al 2026][research_meng_wang_2026]
- [Mengali 2003][research_mengali_2003]
- [Menke and Gursul 1999][research_menke_gursul_1999]
- [Menner et al 2025][research_menner_lawless_2025]
- [Merhav 1989][research_merhav_1989]
- [Merhav and Grunwald 1978][research_merhav_grunwald_1978]
- [Mestriner et al 2018][research_mestriner_desouza_2018]
- [Metin et al 2023][research_metin_uzuner_2023]
- [Metkowski et al 2022][research_metkowski_axten_2022]
- [Metodiev 2022][research_metodiev_2022]
- [Metodiev 2024][research_metodiev_2024]
- [Metzger 2012][research_metzger_2012]
- [Meyer 1983][research_meyer_1983]
- [Meyer et al 1989][research_meyerhf_yiplp_1989]
- [Miao et al 2020][research_miao_wang_2020]
- [Michal 1998][research_michaltoddr_1998]
- [Michelsen and Mueller 1987][research_michelsen_mueller_1987]
- [Michna and Rogowski 2022][research_michna_rogowski_2022]
- [Michna et al 2025][research_michna_sledziewski_2025]
- [Mikami and Uchiyama 2015][research_mikami_uchiyama_2015]
- [Miles 1952][research_miles_1952]
- [Miles 1953][research_miles_1953]
- [Miles and Broughton 2017][research_miles_broughton_2017]
- [Milillo 1972][research_milillo_1972]
- [Miller 1970][research_miller_1970]
- [Miller 1973][research_millerjr_1973]
- [Miller 1983][research_miller_1983]
- [Miller 1986][research_miller_1986]
- [Miller 2011][research_millerchristopherj_2011]
- [Miller 2011][research_millerchristopherj_2011_b]
- [Miller and Clark 1965][research_miller_clark_1965]
- [Miller and Franklin 1968][research_miller_franklin_1968]
- [Miller and Hackney 1976][research_miller_hackney_1976]
- [Mineck 1976][research_mineck_1976]
- [Mineck 1977][research_mineckre_1977]
- [Mineck et al 1976][research_mineckre_freemancr_1976]
- [Mirchandani 2020][research_mirchandani_2020]
- [Mirosław et al 2022][research_miroslaw_dominik_2022]
- [Mirzal 2017][research_mirzal_2017]
- [Mitchell and Hoh 1983][research_mitchell_hoh_1983]
- [Mitchell and Hoh 1984][research_mitchell_hoh_1984]
- [Mitchell et al 1980][research_mitchell_myers_1980]
- [Mitchell et al 1991][research_mitchell_hoh_1991]
- [Mitchell et al 1992][research_mitchelldavidg_aponsobimall_1992]
- [Mitchell et al 2003][research_mitchell_doman_2003]
- [Mitrut et al 2021][research_mitrut_bucur_2021]
- [Miwa 2021][research_miwa_2021]
- [Miwa and Maruhashi 2016][research_miwa_maruhashi_2016]
- [Model Following Reconfigurable Flight Control System Design Using Direct Adaptive Scheme 2003][research_model_following_2003]
- [Moerder et al 1989][research_moerderdanield_halyonesim_1989]
- [Moes and Iliff 2002][research_moestimothyr_iliffkenneth_2002]
- [Moes et al 2003][research_moestimothyr_smithmarks_2003]
- [Mohamed 2024][research_mohamed_2024]
- [Mohamed and Joy 2021][research_mohamed_joy_2021]
- [Mohamed et al 2019][research_mohamed_madhavan_2019]
- [Mohamed et al 2021][research_mohamed_wood_2021]
- [Mohamed Ibren et al 2021][research_mohamedibren_ameldadianneandan_2021]
- [Mohammadi et al 2025][research_mohammadi_ebrahimi_2025]
- [Mohammadi Farhadi et al 2018][research_mohammadifarhadi_kortunov_2018]
- [Mohan and Kumar 2024][research_mohan_kumar_2024]
- [Mohan and Kumar 2025][research_mohan_kumar_2025]
- [Mokhtar and El-Badawy 2023][research_mokhtar_elbadawy_2023]
- [Molander and Willems 1980][research_molander_willems_1980]
- [Molinari et al 2015][research_molinari_arrieta_2015]
- [Molinari et al 2018][research_molinari_arrieta_2018]
- [Molloy et al 2026][research_molloy_shekar_2026]
- [Molusis 1973][research_molusis_1973]
- [Molusis 1973][research_molusisja_1973]
- [Molusis and Briczinski 1974][research_molusisjh_briczinskis_1974]
- [Monaco et al 1997][research_monaco_ward_1997]
- [Moniruzzaman et al 2021][research_moniruzzaman_rassau_2021]
- [Moniruzzaman et al 2022][research_moniruzzaman_rassau_2022]
- [Montalvo and Costello 2015][research_montalvo_costello_2015]
- [Montgomery and Caglayan 1976][research_montgomery_caglayan_1976]
- [Montgomery and Hunsaker 2022][research_montgomery_hunsaker_2022]
- [Montgomery and Price 1976][research_montgomery_price_1976]
- [Montgomery et al 1998][research_montgomeryraymondc_scottmichaela_1998]
- [Mooij and van Gool 1978][research_mooij_vangool_1978]
- [Moore et al 1980][research_moore_skow_1980]
- [Morelli 2021][research_morelli_2021]
- [Morelli 2021][research_morelli_2021_b]
- [Morelli 2022][research_morelli_2022]
- [Morelli and Cooper 2015][research_morelli_cooper_2015]
- [Morelli and DeLoach 2003][research_morellieugenea_deloachrichard_2003]
- [Morelli and Klein 1995][research_morelli_klein_1995]
- [Moreschi and Guardone 2024][research_moreschi_guardone_2024]
- [Moretti 1965][research_moretti_1965]
- [Mori 1988][research_mori_1988]
- [Morlang and Strassburger 2025][research_morlang_strassburger_2025]
- [Moroney et al 1979][research_moroney_pruitt_1979]
- [Morra and Nicolosi 2025][research_morra_nicolosi_2025]
- [Morris 1964][research_morris_1964]
- [Morris 1966][research_morris_1966]
- [Morris 1981][research_morris_1981]
- [Morris 1983][research_morrisjr_1983]
- [Morris 1992][research_morris_1992]
- [Morris and Kroo 1990][research_morris_kroo_1990]
- [Morris et al 2014][research_morris_allison_2014]
- [Morse and Ossman 1989][research_morse_ossman_1989]
- [Morse and Ossman 1990][research_morse_ossman_1990]
- [Morton 2003][research_morton_2003]
- [Morton et al 1996][research_morton_enns_1996]
- [Morton et al 2002][research_morton_mitchell_2002]
- [Moses et al 1965][research_moses_pferschjr_1965]
- [Moszczynski and Grant 2017][research_moszczynski_grant_2017]
- [Moszczynski et al 2019][research_moszczynski_leung_2019]
- [Motter and High 2009][research_mottermarka_highjamesw_2009]
- [Motycka and Skowronek 1968][research_motycka_skowronek_1968]
- [Motyka 1975][research_motyka_1975]
- [Motyka and Reynolds 1971][research_motyka_reynolds_1971]
- [Moua et al 2007][research_mouacheng_mcwhertershaunh_2007]
- [Moua et al 2012][research_mouachengm_mcwhertershaunc_2012]
- [Mouritsen 1994][research_mouritsen_1994]
- [Moëns 2022][research_moens_2022]
- [Mrusek 2021][research_mrusek_2021]
- [Mueller 1965][research_mueller_1965]
- [Mueller and Torres 2001][research_mueller_torres_2001]
- [Mueller et al 2026][research_mueller_theodoulis_2026]
- [Muhammed and Virk 2024][research_muhammed_virk_2024]
- [Muir 1993][research_muir_1993]
- [Muir and Bradshaw 1996][research_muir_bradshaw_1996]
- [Mukai and Hunter 1996][research_mukai_hunter_1996]
- [Mukherjee and Sinha 2016][research_mukherjee_sinha_2016]
- [Mukohara and Anyoji 2021][research_mukohara_anyoji_2021]
- [Mulder 1985][research_mulder_1985]
- [Mulgund and Stengel 1993][research_mulgund_stengel_1993]
- [Mulgund and Stengel 1995][research_mulgund_stengel_1995]
- [Muller 1967][research_muller_1967]
- [Mullins et al 1996][research_mullinsjr_tipton_1996]
- [Multi-Rotors A Revolution In 2015][research_multi_rotors_a_2015]
- [Munday et al 2015][research_munday_taira_2015]
- [Munk 1922][research_munkmaxm_1922]
- [Munk 1924][research_munkmaxm_1924]
- [Munk 1979][research_munkmm_1979]
- [Muravyev 2022][research_muravyev_2022]
- [Murphy 1966][research_murphy_1966]
- [Murphy and Schmidt 1953][research_murphy_schmidt_1953]
- [Murphy et al 2004][research_murphy_klein_2004]
- [Murri and Rao 1987][research_murri_rao_1987]
- [Murri et al 1983][research_murri_croom_1983]
- [Murri et al 1984][research_murridg_nguyenlt_1984]
- [Murri et al 1994][research_murridanielg_shahgautamh_1994]
- [Murugappa and Kazerani 2025][research_murugappa_kazerani_2025]
- [Musso et al 2026][research_musso_vo_2026]
- [Myatt et al 1998][research_myatt_schumacher_1998]
- [Myschik et al 2022][research_myschik_kinast_2022]
- [Müller and Moormann 2023][research_muller_moormann_2023]
- [N-Nagy and Al-Tikriti 1970][research_nnagy_altikriti_1970]
- [Nadda and Swarup 2017][research_nadda_swarup_2017]
- [Nadell et al 2023][research_nadell_berger_2023]
- [Nadi and Zeid 1955][research_nadi_zeid_1955]
- [Nae 2026][research_nae_2026]
- [Nagata et al 1973][research_nagata_skinner_1973]
- [Nagel and Thomas 1965][research_nagel_thomas_1965]
- [Nagy and Kirsten 1976][research_nagy_kirsten_1976]
- [Naigle et al 2022][research_naigle_hiltner_2022]
- [Nam 2026][research_nam_2026]
- [Napolitano 2002][research_napolitano_2002]
- [Napolitano and Kincheloe 1996][research_napolitano_kincheloe_1996]
- [Napolitano et al 1997][research_napolitano_casanova_1997]
- [Napolitano et al 1998][research_napolitano_windon_1998]
- [Napolitano et al 2001][research_napolitano_song_2001]
- [Napolitano et al 2024][research_napolitano_kerrian_2024]
- [Nardi 1970][research_nardi_1970]
- [Nasiri et al 2021][research_nasiri_montazerigh_2021]
- [Nasuhbeyoglu and Akça 2024][research_nasuhbeyoglu_akca_2024]
- [Nataraj and Sardar 1999][research_nataraj_sardar_1999]
- [Natarajan et al 2004][research_natarajan_kapania_2004]
- [Navaratna and Pontillo 2022][research_navaratna_pontillo_2022]
- [Neal and Sengupta 1989][research_nealbradford_senguptaupal_1989]
- [Neal and Smith 1970][research_neal_smith_1970]
- [Nedilko et al 2026][research_nedilko_kolisnichenko_2026]
- [Negre 1975][research_negre_1975]
- [Neitzke 2025][research_neitzke_2025]
- [Nelms and Axelson 1974][research_nelms_axelson_1974]
- [Nelms and Bailey 1974][research_nelms_bailey_1974]
- [Nelson 1985][research_nelson_1985]
- [Nelson and Durham 2002][research_nelson_durham_2002]
- [Nelson and Mouch 1978][research_nelson_mouch_1978]
- [Nenadic et al 1997][research_nenadic_debeljkovic_1997]
- [Nepomuceno and Annes Da Silva 2021][research_nepomuceno_annesdasilva_2021]
- [Nepomuceno et al 2022][research_nepomuceno_fischer_2022]
- [Nettleton 1965][research_nettleton_1965]
- [Neuwerth et al 1998][research_neuwerth_peiter_1998]
- [Neuwerth et al 1999][research_neuwerth_peiter_1999]
- [Neves et al 2020][research_neves_lawson_2020]
- [Neville and Stephens 1993][research_neville_stephens_1993]
- [Newman 1965][research_newman_1965]
- [Newton and Kroo 2023][research_newton_kroo_2023]
- [Newton and Kroo 2024][research_newton_kroo_2024]
- [Newton and Kroo 2025][research_newton_kroo_2025]
- [Ngo et al 1996][research_ngo_reigelsperger_1996]
- [Nguyen 1979][research_nguyen_1979]
- [Nguyen and Cord 1999][research_nguyen_cord_1999]
- [Nguyen and Tran 2021][research_nguyen_tran_2021]
- [Nguyen et al 1980][research_luattnguyen_williampgilbert_1980]
- [Nguyen et al 1997][research_nguyen_cord_1997]
- [Nguyen et al 2016][research_nguyen_reynolds_2016]
- [Nguyen et al 2018][research_nguyen_reynolds_2018]
- [Nguyen et al 2021][research_nguyen_lowenberg_2021]
- [Nguyen et al 2021][research_nguyen_lowenberg_2021_b]
- [Nguyen et al 2025][research_nguyen_han_2025]
- [Ni et al 2021][research_ni_wu_2021]
- [Ni et al 2024][research_ni_chen_2024]
- [Nicholson 1985][research_nicholson_1985]
- [Nicola et al 2025][research_nicola_dicapua_2025]
- [Nicolosi et al 2015][research_nicolosi_dellavecchia_2015]
- [Nicolosi et al 2015][research_nicolosi_demarco_2015]
- [Nicolosi et al 2016][research_nicolosi_dellavecchia_2016]
- [Nicolosi et al 2020][research_nicolosi_ciliberti_2020]
- [Nie et al 2020][research_nie_liu_2020]
- [Nie et al 2021][research_nie_liu_2021]
- [Nield 1981][research_nield_iv_1981]
- [Nielsen 1985][research_nielsen_1985]
- [Niemiec et al 2020][research_niemiec_j_2020]
- [Niestroy 2025][research_niestroy_2025]
- [Niestroy et al 2017][research_niestroy_dorsett_2017]
- [Niestroy et al 2019][research_niestroy_williams_2019]
- [Nieto-Centenero et al 2024][research_nietocentenero_martinezcava_2024]
- [Nieto-Wire and Sobel 2007][research_nietowire_sobel_2007]
- [Nieto-Wire and Sobel 2009][research_nietowire_sobel_2009]
- [Nieto-Wire and Sobel 2011][research_nietowire_sobel_2011]
- [Nieto-Wire and Sobel 2013][research_nietowire_sobel_2013]
- [Nieto-Wire and Sobel 2014][research_nietowire_sobel_2014]
- [Niewald and Parker 2000][research_niewald_parker_2000]
- [Niewoehner and Carter 2001][research_niewoehnerkevinr_carterjohn_2001]
- [Nihtilä 1989][research_nihtila_1989]
- [Nik Mohd 2017][research_nikmohd_2017]
- [Nikiforuk and Gupta 1977][research_nikiforuk_gupta_1977]
- [Nikiforuk et al 1979][research_nikiforuk_ohta_1979]
- [Nikolaou et al 2025][research_nikolaou_kilimtzidis_2025]
- [Nivison and Khargonekar 2017][research_nivison_khargonekar_2017]
- [Nivison and Khargonekar 2017][research_nivison_khargonekar_2017_b]
- [Nivison and Khargonekar 2018][research_nivison_khargonekar_2018]
- [Nogami et al 1986][research_nogami_maeda_1986]
- [Nonlinear adaptive flight control using neural networks 1998][research_nonlinear_adaptive_1998]
- [Nonlinear Discrete-Time Reconfigurable Flight Control Systems Using Neural Networks 2004][research_nonlinear_discrete_time_2004]
- [Nonlinear model following control application to a flight simulator control loader 1989][research_nonlinear_model_1989]
- [Norsell 2003][research_norsell_2003]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]
- [Noury and Yang 2020][research_noury_yang_2020]
- [Nudson et al 2025][research_nudson_stanfieldbrown_2025]
- [Numerical Analysis of the Flow Pattern and Vortex Breakdown over a Pitching Delta wing at Supersonic Speeds 2017][research_numerical_analysis_2017]
- [O'Donnell and Mohseni 2018][research_odonnell_mohseni_2018]
- [O'Rourke 1995][research_orourke_1995]
- [O'Rourke and Sedor 1995][research_orourke_sedor_1995]
- [O-THREE A high altitude 1990][research_o_three_a_1990]
- [Obeid et al 2019][research_obeid_alqadi_2019]
- [Obermark 2004][research_obermark_2004]
- [Oblique Wing Remotely Piloted 1974][research_oblique_wing_1974]
- [Odendaal et al 2024][research_odendaal_smith_2024]
- [Ogburn et al 1993][research_ogburn_foster_1993]
- [Ogren et al 1974][research_ogren_sotanski_1974]
- [Oh and Choi 2018][research_oh_choi_2018]
- [Okolo et al 2015][research_okolo_dogan_2015]
- [Oktay and Kose 2021][research_oktay_kose_2021]
- [Ol 2007][research_ol_2007]
- [Olejnik et al 2019][research_olejnik_kachel_2019]
- [Olejnik et al 2022][research_olejnik_rogolski_2022]
- [Oliva 2001][research_oliva_2001]
- [Olson and Selberg 1976][research_olson_selberg_1976]
- [Olsson 1982][research_olsson_1982]
- [Ong and Chan 2016][research_ong_chan_2016]
- [Onken and Stuckenberg 1978][research_onken_stuckenberg_1978]
- [Oosedo et al 2022][research_oosedo_wada_2022]
- [Oosterom and Vos 2022][research_oosterom_vos_2022]
- [Oosterom et al 2000][research_oosterom_schram_2000]
- [Oosterom et al 2002][research_oosterom_bergsten_2002]
- [Oppenheimer and Doman 2004][research_oppenheimer_doman_2004]
- [Optimized PI-PD Control for Varying Time Delay Systems Based on Modified Smith Predictor 2024][research_optimized_pi_pd_2024]
- [Optimum neural network control 1993][research_optimum_neural_1993]
- [Orhan and Subbarao 2021][research_orhan_subbarao_2021]
- [Orlosky et al 2018][research_orlosky_theofilis_2018]
- [Orozco et al 2026][research_orozco_walsh_2026]
- [Ortiz-Torres et al 2018][research_ortiztorres_castillo_2018]
- [Osawa and Hewitt 1986][research_osawa_hewitt_1986]
- [Osipov 2019][research_osipov_2019]
- [Ossmann et al 2019][research_ossmann_luspay_2019]
- [Ostermann et al 2024][research_ostermann_laubner_2024]
- [Ostheimer and Giguere 1963][research_ostheimer_giguere_1963]
- [Ostroff 1998][research_ostroffaaronj_1998]
- [Ostroff and Bacon 2002][research_ostroff_bacon_2002]
- [Othman and Kanazaki 2015][research_othman_kanazaki_2015]
- [Othman and Kanazaki 2015][research_othman_kanazaki_2015_b]
- [Ouyang and Lin 2017][research_ouyang_lin_2017]
- [Ouyang et al 2022][research_ouyang_zhou_2022]
- [Ovcharenko and Poplavsky 2021][research_ovcharenko_poplavsky_2021]
- [Owashi et al 2017][research_owashi_tanaka_2017]
- [Owen and Johnson 1978][research_owen_johnson_1978]
- [Owens et al 2006][research_owensdonaldb_coxdavide_2006]
- [Ozdemir et al 2024][research_ozdemir_kucuk_2024]
- [Ozgören et al 2002][research_ozgoren_sahin_2002]
- [Ozturk 1986][research_ozturk_1986]
- [Ozturk 1991][research_ozturk_1991]
- [P.S. and J.V. 2021][research_ps_jv_2021]
- [P5 et al 2026][research_p5_ramasubramanian1_2026]
- [Pacheco-Gutierrez et al 2021][research_pachecogutierrez_niu_2021]
- [Padhi and Balakrishnan 2003][research_padhi_balakrishnan_2003]
- [Page and Steinberg 1999][research_page_steinberg_1999]
- [Pagliuca and Timme 2016][research_pagliuca_timme_2016]
- [Pagliuca and Timme 2017][research_pagliuca_timme_2017]
- [Pahle et al 1996][research_pahlejosephw_bundickwthomas_1996]
- [Pakzad 2021][research_pakzad_2021]
- [Pal and Gaberson 1973][research_pal_gaberson_1973]
- [Palacios et al 1998][research_palacios_owens_1998]
- [Palframan et al 2019][research_palframan_fry_2019]
- [Palkin and Zenchenko 2025][research_palkin_zenchenko_2025]
- [Pallister et al 1992][research_pallister_parker_1992]
- [Palmer and Wright 2002][research_palmer_wright_2002]
- [Pan and Huang 2018][research_pan_huang_2018]
- [Pan and Huang 2019][research_pan_huang_2019]
- [Pan and Huang 2019][research_pan_huang_2019_b]
- [Pan et al 2016][research_pan_liu_2016]
- [Pan et al 2017][research_pan_sun_2017]
- [Pan et al 2025][research_pan_ma_2025]
- [Pan et al 2026][research_pan_mao_2026]
- [Pandi and Mittal 2025][research_pandi_mittal_2025]
- [Panish et al 2023][research_panish_nicholls_2023]
- [Papadales and Basil S. 1979][research_papadales_basils_1979]
- [Papageorgiou and Glover 2002][research_papageorgiou_glover_2002]
- [Papageorgiou et al 2018][research_papageorgiou_tarkian_2018]
- [Papoutsis-Kiachagias et al 2021][research_papoutsiskiachagias_asouti_2021]
- [Parameter estimation techniques and 1974][research_parameter_estimation_1974]
- [Paranjape and Ananthkrishnan 2023][research_paranjape_ananthkrishnan_2023]
- [Paranjape and Chung 2010][research_paranjape_chung_2010]
- [Paranjape et al 1966][research_paranjapesv_thomastj_1966]
- [Paranjape et al 2011][research_paranjape_chung_2011]
- [Park 1977][research_park_1977]
- [Park et al 2001][research_park_lee_2001]
- [Park et al 2015][research_park_ocheltree_2015]
- [Park et al 2016][research_park_choi_2016]
- [Park et al 2016][research_park_jo_2016]
- [Park et al 2017][research_park_choi_2017]
- [Park et al 2017][research_park_jo_2017]
- [Park et al 2019][research_park_shim_2019]
- [Park et al 2019][research_park_shin_2019]
- [Park et al 2024][research_park_ramirezserrano_2024]
- [Park et al 2025][research_park_ramirezserrano_2025]
- [Park et al 2025][research_park_ramirezserrano_2025_b]
- [Park et al 2025][research_park_yang_2025]
- [Parlange 1968][research_parlange_1968]
- [Parra et al 2026][research_parra_uraldeguinea_2026]
- [Passive Flow Control over an Airfoil by Control Rod at Low Reynolds Number 2020][research_passive_flow_2020]
- [Patel and Ramaprian 1978][research_patel_ramaprian_1978]
- [Patel and Smith 1996][research_patel_smith_1996]
- [Patel and Smith 1998][research_patel_smith_1998]
- [Patel et al 2002][research_patel_deodhare_2002]
- [Patel et al 2002][research_patel_prince_2002]
- [Patera 1981][research_patera_1981]
- [Patience and Nahon 2020][research_patience_nahon_2020]
- [Patten 1988][research_patten_1988]
- [Patterson and Arena 2015][research_patterson_arena_2015]
- [Paul et al 1997][research_paul_garrard_1997]
- [Paulson et al 1977][research_paulson_price_1977]
- [Paulson et al 1979][research_paulsonjwjr_thomasjl_1979]
- [Payne 1968][research_payne_1968]
- [Pedersini et al 2015][research_pedersini_toscano_2015]
- [Pedreiro 1997][research_pedreironelson_1997]
- [Pedreiro et al 1998][research_pedreiro_rock_1998]
- [Pei et al 2025][research_pei_huang_2025]
- [Pelikan 1974][research_pelikan_1974]
- [Pelletier and Mueller 1999][research_pelletier_mueller_1999]
- [Pelletier and Nelson 2000][research_pelletier_nelson_2000]
- [Pena and Voulgaris 2001][research_pena_voulgaris_2001]
- [Peng et al 2016][research_peng_li_2016]
- [Peng et al 2018][research_peng_lin_2018]
- [Peng et al 2019][research_peng_chen_2019]
- [Pepelea et al 2016][research_pepelea_cojocaru_2016]
- [Perhinschi 1998][research_perhinschi_1998]
- [Perhinschi and Prasad 1995][research_perhinschi_prasad_1995]
- [Peristy et al 2016][research_peristy_perez_2016]
- [Peristy et al 2019][research_peristy_perez_2019]
- [Peristy et al 2020][research_peristy_perez_2020]
- [Perng et al 2004][research_perng_wu_2004]
- [Perry 1976][research_perrybiii_1976]
- [Perry and Mueller 1986][research_perry_mueller_1986]
- [Persson 2017][research_persson_2017]
- [Persson and Bull 2016][research_persson_bull_2016]
- [Petersen 1976][research_petersen_1976]
- [Petersen 1976][research_petersen_1976_b]
- [Peterson 1961][research_petersonvictorl_1961]
- [Peterson 1968][research_peterson_1968]
- [Peterson 2004][research_petersonwaynel_2004]
- [Peterson 2024][research_peterson_2024]
- [Peterson 2025][research_peterson_2025]
- [Peterson et al 2016][research_peterson_sarigulklijn_2016]
- [Petnga 2018][research_petnga_2018]
- [Petrenko and Gašparovič 2025][research_petrenko_gasparovic_2025]
- [Petrie 1968][research_petrie_1968]
- [Petrović et al 2016][research_petrovic_sajn_2016]
- [Pfeifle and Fichter 2022][research_pfeifle_fichter_2022]
- [Pfeifle and Fichter 2023][research_pfeifle_fichter_2023]
- [Pfenninger and Vemuru 1988][research_pfenninger_vemuru_1988]
- [Pfifer and Danowsky 2016][research_pfifer_danowsky_2016]
- [Pfifer and Seiler 2015][research_pfifer_seiler_2015]
- [Pfnür and Breitsamter 2019][research_pfnur_breitsamter_2019]
- [Phelps 1979][research_phelps_1979]
- [Phillips 2000][research_phillips_2000]
- [Phillips 2000][research_phillips_2000_b]
- [Phillips and Santana 2002][research_phillips_santana_2002]
- [Phillips et al 2019][research_phillips_jentzsch_2019]
- [PI control of a tailless fighter aircraft with dynamic inversion and neural networks 1999][research_pi_control_1999]
- [Piccinelli and Muradore 2021][research_piccinelli_muradore_2021]
- [Piccirillo 1996][research_piccirillo_1996]
- [Pieper et al 2018][research_pieper_perry_2018]
- [Pinebrook and Dalton 1983][research_pinebrook_dalton_1983]
- [Pinebrook and Dalton 1983][research_pinebrook_dalton_1983_b]
- [Pitts et al 1974][research_pittsfl_holmesdce_1974]
- [Place et al 1974][research_place_altmann_1974]
- [Plaetschke et al 1982][research_plaetschke_mulder_1982]
- [Planeaux and Barth 1988][research_planeaux_barth_1988]
- [Platanitis and Shkarayev 2005][research_platanitisgeorge_shkarayevsergey_2005]
- [Platou 1968][research_platou_1968]
- [Platzer and Hoffman 1966][research_platzer_hoffman_1966]
- [Plyashechnik et al 1999][research_plyashechnik_ivanov_1999]
- [Pollack et al 2026][research_pollack_theodoulis_2026]
- [Poojari 2022][research_poojari_2022]
- [Popescu et al 2003][research_popescu_rasvan_2003]
- [Portapas and Cooke 2020][research_portapas_cooke_2020]
- [Portapas et al 2017][research_portapas_yusuf_2017]
- [Porter and Swaim 1975][research_portermbjr_swaimrl_1975]
- [Pose et al 2017][research_pose_giribet_2017]
- [Posingies 1979][research_posingies_1979]
- [Postlethwaite et al 1999][research_postlethwaite_konstantopoulos_1999]
- [Postlethwaite et al 2000][research_postlethwaite_konstantopoulos_2000]
- [Potter and Whitfield 1957][research_potter_whitfield_1957]
- [Potvin and Grant 2026][research_potvin_grant_2026]
- [Poudel et al 2021][research_poudel_yu_2021]
- [Pounds and Walker 1980][research_pounds_walker_1980]
- [Power 1969][research_power_1969]
- [Prabhakar et al 2019][research_prabhakar_prazenica_2019]
- [Prakash et al 2019][research_prakash_vignati_2019]
- [Prediction of vortex breakdown effects on a rolling delta wing 1994][research_prediction_of_1994]
- [Price 1943][research_price_1943]
- [Price and Glidewell 1981][research_pricejr_glidewell_1981]
- [Pritchard et al 2016][research_pritchard_wallace_2016]
- [Priyanka and Sivapragasam 2021][research_priyanka_sivapragasam_2021]
- [Prizirembel and Wen 1978][research_prizirembel_wen_1978]
- [Probst et al 2019][research_probst_knopp_2019]
- [Prochazka and Stomberg 2020][research_prochazka_stomberg_2020]
- [Prochazka et al 2018][research_prochazka_eduardo_2018]
- [Protz and Sparks 1998][research_protz_sparks_1998]
- [Provost et al 2026][research_provost_hawlader_2026]
- [Provost et al 2026][research_provost_hawlader_2026_b]
- [Pryor et al 2020][research_pryor_vagvolgyi_2020]
- [Ptitsin 2017][research_ptitsin_2017]
- [Pulk and Stolarik 1977][research_pulk_stolarik_1977]
- [Pusztai et al 2024][research_pusztai_lowenberg_2024]
- [Putman 1969][research_putman_1969]
- [Putnam et al 1986][research_putnamtw_petersenkl_1986]
- [Putra et al 2022][research_putra_mobedbachtiar_2022]
- [Qi and Zhongke 2015][research_qi_zhongke_2015]
- [Qi et al 2016][research_qi_gao_2016]
- [Qian et al 2022][research_qian_yang_2022]
- [Qian et al 2024][research_qian_ma_2024]
- [Qian et al 2025][research_qian_xinhui_2025]
- [Qin 2026][research_qin_2026]
- [Qiu and Gourishankar 1984][research_qiu_gourishankar_1984]
- [Qu et al 2011][research_qu_li_2011]
- [Queen 1976][research_queen_1976]
- [Quenzer et al 2018][research_quenzer_barzgaran_2018]
- [Quitter et al 2021][research_quitter_marino_2021]
- [Rabenberg and Palarz 1983][research_rabenberg_palarz_1983]
- [Radar cross section fundamentals for the aircraft designer 1979][research_radar_cross_1979]
- [Raffel et al 2019][research_raffel_wienke_2019]
- [Raffel et al 2021][research_raffel_dillmann_2021]
- [Raffel et al 2021][research_raffel_wienke_2021]
- [Rahal and Dutta 2024][research_rahal_dutta_2024]
- [Rainbird et al 2015][research_rainbird_peiro_2015]
- [Raisinghani and Adak 1983][research_raisinghani_adak_1983]
- [Rajagopal et al 1988][research_rajagopal_lick_1988]
- [Rajarajan et al 2024][research_rajarajan_mudhangulla_2024]
- [Rajeswari and Prabhu 1987][research_rajeswari_prabhu_1987]
- [Rajput et al 2015][research_rajput_zhangweiguo_2015]
- [Raju Kulkarni et al 2019][research_rajukulkarni_larocca_2019]
- [Rakich and Cleary 1970][research_rakich_cleary_1970]
- [Rakich and Cleary 2003][research_rakich_cleary_2003]
- [Rakita et al 2020][research_rakita_mutlu_2020]
- [Rakshith et al 2015][research_rakshith_deshpande_2015]
- [Ramdin et al 2023][research_ramdin_visser_2023]
- [Ramirez and Nahon 2021][research_ramirez_nahon_2021]
- [Rampy 1966][research_rampy_1966]
- [Ramírez et al 2021][research_ramirez_breda_2021]
- [Raney et al 2000][research_raneydavidl_montgomeryraymondc_2000]
- [Ransom 1983][research_ransom_1983]
- [Ransquin and Chatelain 2021][research_ransquin_chatelain_2021]
- [Rao 1989][research_rao_1989]
- [Rao and Murri 1986][research_rao_murri_1986]
- [Rao and Srinath 1965][research_rao_srinath_1965]
- [Rao et al 1986][research_raodm_moskovitzc_1986]
- [Rao et al 1987][research_rao_moskovitz_1987]
- [Ratcliff et al 2016][research_ratcliff_bodkin_2016]
- [Raul Azinheira et al 2001][research_raulazinheira_carneirodepaiva_2001]
- [Ravi and Mason 1994][research_ravi_mason_1994]
- [Rayleigh 1915][research_rayleigh_1915]
- [Raza and Silverthorn 1985][research_raza_silverthorn_1985]
- [Reaser et al 1983][research_reaser_hallissy_1983]
- [Reconfigurable Flight Control Law Using Adaptive Neural Networks and Backstepping Technique 2003][research_reconfigurable_flight_2003]
- [Reed 1974][research_reed_1974]
- [Reed 1990][research_reed_1990]
- [Reeder 1958][research_reeder_1958]
- [Reel and Baltadjiev 2018][research_reel_baltadjiev_2018]
- [Reghunath and Ramaiah 2022][research_reghunath_ramaiah_2022]
- [Reichstein et al 2022][research_reichstein_schopferer_2022]
- [Reigelsperger et al 1995][research_reigelsperger_hammett_1995]
- [Reinbold et al 2026][research_reinbold_breitsamter_2026]
- [Reiner et al 1994][research_reiner_balas_1994]
- [Reiner et al 1995][research_reiner_balas_1995]
- [Reiner et al 1996][research_reiner_balas_1996]
- [Reist and Zingg 2015][research_reist_zingg_2015]
- [Reist and Zingg 2016][research_reist_zingg_2016]
- [Reist and Zingg 2017][research_reist_zingg_2017]
- [Reist et al 2022][research_reist_koo_2022]
- [Reklis 1980][research_reklis_1980]
- [Ren and Quan 2016][research_ren_quan_2016]
- [Ren and Wang 2026][research_ren_wang_2026]
- [Ren and Zha 2025][research_ren_zha_2025]
- [Ren et al 2022][research_ren_su_2022]
- [Ren et al 2026][research_ren_ghopa_2026]
- [Renard and Deck 2015][research_renard_deck_2015]
- [Repperger et al 1997][research_repperger_koivo_1997]
- [Research and Analysis on Development and Flight Test of Military Aircraft Flight Simulator 2022][research_research_and_2022]
- [Research and Design of Automatic Flight Control System Test System 2022][research_research_and_2022_b]
- [Resta et al 2021][research_resta_marsilio_2021]
- [Reuther and Jameson 1995][research_reuther_jameson_1995]
- [Rezek 1985][research_rezek_1985]
- [Rhew and Parker 2017][research_rhew_parker_2017]
- [Rhoads 1967][research_rhoads_1967]
- [Rhodeside 1986][research_rhodeside_1986]
- [Ribeiro and Resende 1993][research_ribeiro_deresende_1993]
- [Riboldi et al 2026][research_riboldi_alessi_2026]
- [Riccardi et al 2025][research_riccardi_mamino_2025]
- [Richardson 1976][research_richardson_1976]
- [Richter et al 2024][research_richter_calix_2024]
- [Rickard 1978][research_rickard_1978]
- [Riethausen 2026][research_riethausen_2026]
- [Rigden 1938][research_rigden_1938]
- [Rinauto et al 2017][research_rinauto_gupta_2017]
- [Rios and Tamayo 2017][research_rios_tamayo_2017]
- [Rising et al 1984][research_risingjj_daviswj_1984]
- [Rist 1996][research_rist_1996]
- [Rithirun et al 2021][research_rithirun_charean_2021]
- [Rivers et al 2001][research_rivers_wahls_2001]
- [Roberts et al 1977][research_robertspa_swaimrl_1977]
- [Robertson 1997][research_robertson_1997]
- [Robinson 1958][research_robinsonrb_1958]
- [Robinson 1968][research_robinson_1968]
- [Robinson 1969][research_robinson_1969]
- [Robinson and Wissler 1988][research_robinson_wissler_1988]
- [Rocha Ribeiro and Wolf 2025][research_rocharibeiro_wolf_2025]
- [Rodchenko et al 2002][research_rodchenko_zaichik_2002]
- [Rodchenko et al 2003][research_rodchenko_zaichik_2003]
- [Rodden and Giesing 1970][research_rodden_giesing_1970]
- [Rodden et al 1962][research_rodden_farkas_1962]
- [Rodgers 1963][research_rodgers_1963]
- [Rodríguez de Cos and Acosta 2020][research_rodriguezdecos_acosta_2020]
- [Rodzewicz 2024][research_rodzewicz_2024]
- [Rogalski 2018][research_rogalski_2018]
- [Rogalski et al 2020][research_rogalski_rzucidlo_2020]
- [Rogalski et al 2021][research_rogalski_rzucidlo_2021]
- [Roganov et al 2017][research_roganov_roganova_2017]
- [Rohani and Jahangirian 2022][research_rohani_jahangirian_2022]
- [Rohith and Sinha 2017][research_rohith_sinha_2017]
- [Rojas Carvajal and Amitay 2023][research_rojascarvajal_amitay_2023]
- [Rolls and Aoyagi 1977][research_rolls_aoyagi_1977]
- [Rolston 2001][research_rolston_2001]
- [Rom et al 1987][research_rom_almosnino_1987]
- [Ronfle-Nadaud 2009][research_ronflenadaud_2009]
- [Rong 2026][research_rong_2026]
- [Rooney et al 1982][research_rooneyrh_chungjc_1982]
- [Roos 1996][research_roos_1996]
- [Roos 2001][research_roos_2001]
- [Rosa and Belo 2021][research_rosa_belo_2021]
- [Rosa et al 1974][research_rosa_sanneman_1974]
- [Rosales and Gross 2017][research_rosales_gross_2017]
- [Rosario-Gabriel and Cortes 2018][research_rosariogabriel_cortes_2018]
- [Roseberg 1982][research_rosebergew_1982]
- [Rosić and Diekmann 2015][research_rosic_diekmann_2015]
- [Ross et al 2019][research_ross_jacob_2019]
- [Rossetti and Beblo 2022][research_rossetti_beblo_2022]
- [Rossi and Miller 1999][research_rossi_miller_1999]
- [Roth and Mavris 2001][research_roth_mavris_2001]
- [Roy and Bhasin 2019][research_roy_bhasin_2019]
- [Roy and Mukherjee 2021][research_roy_mukherjee_2021]
- [Roy et al 2017][research_roy_sengupta_2017]
- [Roy et al 2023][research_roy_biswas_2023]
- [Rs et al 2018][research_rs_a_2018]
- [Ruan and Aagren 2025][research_ruan_aagren_2025]
- [Rubertus 1983][research_rubertusdp_1983]
- [Rubin and Mummolo 1973][research_rubin_mummolo_1973]
- [Ruetten 2018][research_ruetten_2018]
- [Ruflin and Grantham 1984][research_ruflin_grantham_1984]
- [Ruifeng 2015][research_ruifeng_2015]
- [Russell et al 2022][research_russell_werner_2022]
- [Rutkay and Laliberté 2016][research_rutkay_laliberte_2016]
- [Rutowski 1954][research_rutowski_1954]
- [Ryan 1990][research_ryanlaurae_1990]
- [Ryan and Downing 1993][research_ryangeorgewiii_downingdavidr_1993]
- [Rynaski 1994][research_rynaski_1994]
- [Rysdyk and Calise 1998][research_rysdyk_calise_1998]
- [Rysdyk and Calise 1999][research_rysdyk_calise_1999]
- [Sabo and Bugaj 2021][research_sabo_bugaj_2021]
- [Sabra et al 2025][research_sabra_hafez_2025]
- [Sachan et al 2025][research_sachan_r_2025]
- [Sacks 1954][research_sacksalvinh_1954]
- [Sadeghi 1984][research_sadeghi_1984]
- [Saderla et al 2016][research_saderla_dhayalan_2016]
- [Saderla et al 2016][research_saderla_r_2016]
- [Saderla et al 2017][research_saderla_rajaram_2017]
- [Sadovnitchii et al 1997][research_sadovnitchii_ryabkov_1997]
- [Sadovnychiy et al 1998][research_sadovnychiy_betin_1998]
- [Sadraey 2017][research_sadraey_2017]
- [Saeed and Graham 2015][research_saeed_graham_2015]
- [Saephan and van Dam 2006][research_saephan_vandam_2006]
- [Saephan and van Dam 2006][research_saephan_vandam_2006_b]
- [Saetti and Rogers 2020][research_saetti_rogers_2020]
- [Saetti and Rogers 2024][research_saetti_rogers_2024]
- [Safie and Yunus 2024][research_safie_yunus_2024]
- [Safonov and Athans 1976][research_safonov_athans_1976]
- [Safonov and Athans 1977][research_safonov_athans_1977]
- [Safwat et al 2018][research_safwat_zhang_2018]
- [Sagan et al 2021][research_sagan_krishnamurthy_2021]
- [Sahasrabudhe and Celi 1997][research_sahasrabudhe_celi_1997]
- [Sahin et al 2026][research_sahin_yayla_2026]
- [Sai Teja et al 2017][research_saiteja_vaghela_2017]
- [Saini et al 2024][research_saini_kumar_2024]
- [Sakata 2002][research_sakata_2002]
- [Salagame et al 2025][research_salagame_pandya_2025]
- [Salahudden 2024][research_salahudden_2024]
- [Salahudden 2025][research_salahudden_2025]
- [Salahudden and Ghosh 2021][research_salahudden_ghosh_2021]
- [Salahudden et al 2020][research_salahudden_giri_2020]
- [Salahudden et al 2022][research_salahudden_das_2022]
- [Salahudden et al 2024][research_salahudden_agrawal_2024]
- [Salahudden et al 2024][research_salahudden_singh_2024]
- [Salahudden et al 2025][research_salahudden_kumar_2025]
- [Salehian et al 2022][research_salehian_khan_2022]
- [Salehian et al 2024][research_salehian_khan_2024]
- [Salehian et al 2025][research_salehian_khan_2025]
- [Salinas et al 2015][research_salinas_slawinski_2015]
- [Samoylovitch and Strelets 2000][research_samoylovitch_strelets_2000]
- [Sanchez-Rivera et al 2019][research_sanchezrivera_lozano_2019]
- [Sanchez-Rivera et al 2020][research_sanchezrivera_lozano_2020]
- [Sancı and Öke Günel 2024][research_sanci_okegunel_2024]
- [Sanders 1997][research_sanders_1997]
- [Sanfilippo 1970][research_sanfilippo_1970]
- [Santos et al 2022][research_santos_honorio_2022]
- [Saporito et al 2021][research_saporito_daronch_2021]
- [Saraf et al 1998][research_saraf_deodhare_1998]
- [Saraswathi 2000][research_saraswathi_2000]
- [Sarathy and Murthy 1993][research_sarathy_murthy_1993]
- [Sarathy and Murthy 1993][research_sarathy_murthy_1993_b]
- [Sariyildiz et al 2018][research_sariyildiz_mutlu_2018]
- [Sarker et al 2026][research_sarker_pudasaini_2026]
- [Sarrafian 1984][research_sarrafian_1984]
- [Sarrafian 1986][research_sarrafian_1986]
- [Sato and Muraoka 2015][research_sato_muraoka_2015]
- [Sato et al 2017][research_sato_muraoka_2017]
- [Sato et al 2021][research_sato_kashihara_2021]
- [Satoh and Sugimoto 2002][research_satoh_sugimoto_2002]
- [Saunders 1996][research_saunders_1996]
- [Saxena and Faruque 2016][research_saxena_faruque_2016]
- [Sayyed et al 2025][research_sayyed_konar_2025]
- [Schaefer et al 2019][research_schaefer_cary_2019]
- [Schaefer et al 2024][research_schaefer_bekemeyer_2024]
- [Schaeffler and Rediniotis 1995][research_schaeffler_rediniotis_1995]
- [Schaff and Prazenica 2024][research_schaff_prazenica_2024]
- [Schaff and Prazenica 2025][research_schaff_prazenica_2025]
- [Schairer 1964][research_schairer_1964]
- [Schalk 2017][research_schalk_2017]
- [Schierman and Schmidt 1991][research_schiermanjohnd_schmidtdavidk_1991]
- [Schierman et al 2015][research_schierman_devore_2015]
- [Schiff 1971][research_schiff_1971]
- [Schirmer and Capone 1989][research_schirmer_capone_1989]
- [Schmidt 1983][research_schmidt_1983]
- [Schmidt 1985][research_schmidt_1985]
- [Schmidt and Newman 1990][research_schmidtdavidk_newmanbrett_1990]
- [Schmidt et al 2019][research_schmidt_danowsky_2019]
- [Schmidt et al 2025][research_schmidt_hartl_2025]
- [Schnell 2023][research_schnell_2023]
- [Schnetter et al 2015][research_schnetter_kaste_2015]
- [Scholcover and Gillan 2017][research_scholcover_gillan_2017]
- [Schoombie et al 2017][research_schoombie_tuling_2017]
- [Schrader et al 1988][research_schrader_reynolds_1988]
- [Schrage 1990][research_schrage_1990]
- [Schreadley 1977][research_schreadley_1977]
- [Schroeder et al 1998][research_schroeder_chung_1998]
- [Schuck 1959][research_schuck_1959]
- [Schuck 1960][research_schuck_1960]
- [Schultz and Zagalsky 1972][research_schultz_zagalsky_1972]
- [Schumacher 1952][research_schumacher_1952]
- [Schumacher 1999][research_schumacher_1999]
- [Schuman 1981][research_schuman_1981]
- [Schwanz 1972][research_schwanz_1972]
- [Schwanz and Grimes 1980][research_schwanz_grimes_1980]
- [Schwartz and Shearer 1964][research_schwartz_shearer_1964]
- [Schwartz et al 1957][research_schwartz_malick_1957]
- [Schwithal et al 2025][research_schwithal_wallace_2025]
- [Scordamaglia et al 2025][research_scordamaglia_mattei_2025]
- [Scott 1977][research_scott_1977]
- [Scott 2021][research_scott_2021]
- [Seaberg et al 1972][research_seaberg_etter_1972]
- [Seacord and Campbell 1945][research_seacordcharlesl_campbelljohnp_1945]
- [Seaver et al 2023][research_seaver_bennett_2023]
- [Sedlacek et al 2022][research_sedlacek_breitsamter_2022]
- [Sedlmair et al 2022][research_sedlmair_theis_2022]
- [Sedláčková et al 2020][research_sedlackova_kurdel_2020]
- [Seiferth et al 2018][research_seiferth_kugler_2018]
- [Seiff and Sandahl 1951][research_seiffalvin_sandahlcarla_1951]
- [Sellers et al 1988][research_sellerswilliamliii_meyersjamesf_1988]
- [Sellers et al 2004][research_sellerswilliamliii_meyersjamesf_2004]
- [Semmelhack and Hoppe 1967][research_semmelhack_hoppe_1967]
- [Sens 1978][research_sens_1978]
- [Seo and Kim 2019][research_seo_kim_2019]
- [Sepulveda Palacios and Smith 2019][research_sepulvedapalacios_smith_2019]
- [Seraj and Martins 2022][research_seraj_martins_2022]
- [Seres et al 2023][research_seres_liu_2023]
- [Servo-control device for aircraft flight control 1984][research_servo_control_device_1984]
- [Setati et al 2022][research_setati_botha_2022]
- [Setiawarman and Sasongko 2026][research_setiawarman_sasongko_2026]
- [Sever et al 2025][research_sever_demir_2025]
- [Sezer and Siljak 1980][research_sezer_siljak_1980]
- [Sezer and Siljak 1981][research_sezer_siljak_1981]
- [Shafer et al 1983][research_shafer_smith_1983]
- [Shah 1991][research_shahgautamh_1991]
- [Shah 2017][research_shah_2017]
- [Shah and Granda 1998][research_shah_granda_1998]
- [Shahjahan et al 2026][research_shahjahan_enriquez_2026]
- [Shams et al 2018][research_shams_alishah_2018]
- [Shams et al 2023][research_shams_khouli_2023]
- [Shankar and Yathisha 2023][research_shankar_l_2023]
- [Shankar et al 2004][research_shankar_yedavalli_2004]
- [Shao et al 2019][research_shao_chen_2019]
- [Sharif 2019][research_sharif_2019]
- [Sharif 2022][research_sharif_2022]
- [Sharma and Hosder 2021][research_sharma_hosder_2021]
- [Sharma and Rajamani 2024][research_sharma_rajamani_2024]
- [Sharma et al 1998][research_sharma_sekaran_1998]
- [Sharpe and Hansman 2024][research_sharpe_hansman_2024]
- [Shayak et al 2024][research_shayak_girdhar_2024]
- [Shayan and Van Kampen 2021][research_shayan_vankampen_2021]
- [Shearwood et al 2019][research_shearwood_nabawy_2019]
- [Shearwood et al 2020][research_shearwood_nabawy_2020]
- [Shearwood et al 2020][research_shearwood_nabawy_2020_b]
- [Shearwood et al 2021][research_shearwood_nabawy_2021]
- [Shearwood et al 2021][research_shearwood_nabawy_2021_b]
- [Shekarriz et al 1991][research_shekarriz_fu_1991]
- [Shen and Chen 2025][research_shen_chen_2025]
- [Shen and Xu 2021][research_shen_xu_2021]
- [Shen et al 2023][research_shen_wang_2023]
- [Shen et al 2025][research_shen_lv_2025]
- [Shendge 2021][research_shendge_2021]
- [Shenoy and Manjunatha 2023][research_shenoy_manjunatha_2023]
- [Sherbaum and Lichtsinder 1998][research_sherbaum_lichtsinder_1998]
- [Sheridan 1968][research_sheridan_jr_1968]
- [Shi and Wan 2015][research_shi_wan_2015]
- [Shi and Wu 2022][research_shi_wu_2022]
- [Shi et al 2021][research_shi_liu_2021]
- [Shi et al 2023][research_shi_wang_2023]
- [Shi et al 2024][research_shi_hui_2024]
- [Shin and Belcastro 2008][research_shinjongyeob_belcastrochristine_2008]
- [Shin and Kim 2004][research_shin_kim_2004]
- [Shin et al 2003][research_shin_johnson_2003]
- [Shinoda et al 1998][research_shinoda_niwa_1998]
- [Shinoda et al 1999][research_shinoda_niwa_1999]
- [Shishkin 2025][research_shishkin_2025]
- [Shivam and Verma 2019][research_shivam_verma_2019]
- [Shlien 1991][research_shlien_1991]
- [Shmelоv et al 2019][research_shmelv_vladov_2019]
- [Shmilovich and Princen 2026][research_shmilovich_princen_2026]
- [Shojae et al 2025][research_shojae_salehi_2025]
- [Shomber and Gertsen 1967][research_shomber_gertsen_1967]
- [Shore and Bodson 2004][research_shore_bodson_2004]
- [Shrivastava and Stengel 1989][research_shrivastava_stengel_1989]
- [Shtessel et al 1999][research_shtessel_buffington_1999]
- [Shtessel et al 1999][research_shtessel_buffington_1999_b]
- [Shtessel et al 2002][research_shtessel_buffington_2002]
- [Shuang et al 2016][research_shuang_zhang_2016]
- [Shubert and Jones 2025][research_shubert_jones_2025]
- [Shufan et al 2017][research_shufan_heng_2017]
- [Shukla et al 2025][research_shukla_benyamen_2025]
- [Shukla et al 2026][research_shukla_mitra_2026]
- [Shuo et al 2025][research_shuo_tuan_2025]
- [Siegel 1961][research_siegel_1961]
- [Sijabat and Indriyanto 2021][research_sijabat_indriyanto_2021]
- [Silva and Wolf 2024][research_silva_wolf_2024]
- [Silva and Wolf 2026][research_silva_wolf_2026]
- [Silva et al 2018][research_silva_dewagter_2018]
- [Silva et al 2022][research_silva_nunes_2022]
- [Silva et al 2026][research_silva_souza_2026]
- [Silvers et al 1958][research_silvershnorman_fournierrogerh_1958]
- [Simmons 2022][research_simmons_2022]
- [Simmons 2023][research_benjaminmsimmons_2023]
- [Simmons 2023][research_simmons_2023]
- [Simmons and Ackerman 2026][research_simmons_ackerman_2026]
- [Simmons and Murphy 2021][research_simmons_murphy_2021]
- [Simmons et al 2019][research_simmons_mcclelland_2019]
- [Simmons et al 2023][research_simmons_gresham_2023]
- [Simmons et al 2023][research_simmons_gresham_2023_b]
- [Simmons et al 2023][research_simmons_gresham_2023_c]
- [Simmons et al 2023][research_simmons_gresham_2023_d]
- [Simon et al 1993][research_simon_blake_1993]
- [Simon et al 2023][research_simon_williams_2023]
- [Simon et al 2024][research_simon_williams_2024]
- [Simon et al 2025][research_simon_zekry_2025]
- [Simpson 1972][research_simpson_1972]
- [Simpson 1979][research_simpson_1979]
- [Sing Kang et al 2024][research_singkang_singh_2024]
- [Singh 1986][research_singhb_1986]
- [Singh 2025][research_singh_2025]
- [Singh and Jategaonkar 1996][research_singh_jategaonkar_1996]
- [Singh and Jategaonkar 1996][research_singh_jategaonkar_1996_b]
- [Singh and Padhy 2017][research_singh_padhy_2017]
- [Singh and Raol 2000][research_singh_raol_2000]
- [Singh and Steinberg 1996][research_singh_steinberg_1996]
- [Singh et al 1999][research_singh_steinberg_1999]
- [Singh et al 2024][research_singh_lambeth_2024]
- [Singhal et al 2019][research_singhal_thorpe_2019]
- [Sinha 2004][research_sinha_2004]
- [Sinha and Ananthkrishnan 2002][research_sinha_ananthkrishnan_2002]
- [Sirbaugh 1983][research_sirbaugh_1983]
- [Sisson and Dogan 2025][research_sisson_dogan_2025]
- [Sisson et al 2024][research_sisson_sarioglu_2024]
- [Sivan 1971][research_sivan_1971]
- [Siwakosit and Hess 2001][research_siwakosit_hess_2001]
- [Siwakosit et al 2000][research_siwakosit_snell_2000]
- [Sizlo et al 1979][research_sizlotr_bergra_1979]
- [Skarka and Mateja 2024][research_skarka_mateja_2024]
- [Sklaroff et al 1973][research_sklaroff_kilmer_1973]
- [Skow and Peake 1983][research_skowam_peakedj_1983]
- [Skow et al 1982][research_skow_moore_1982]
- [Slaby et al 1985][research_slaby_hartley_1985]
- [Sliwa 1980][research_sliwasm_1980]
- [Slongo et al 2020][research_slongo_moraes_2020]
- [Sluis et al 2023][research_sluis_dellacorte_2023]
- [Smetana et al 1972][research_smetanafo_summerydc_1972]
- [Smit and Craig 1998][research_smit_craig_1998]
- [Smit et al 2022][research_smit_pollack_2022]
- [Smith 1960][research_smithfm_1960]
- [Smith 1977][research_smith_1977_b]
- [Smith 1991][research_smith_1991]
- [Smith 1994][research_smith_1994]
- [Smith 1998][research_smith_1998]
- [Smith 2023][research_smith_2023]
- [Smith and Berry 2000][research_smith_berry_2000]
- [Smith and Edwards 1980][research_smithjw_edwardsjw_1980]
- [Smith and Geddes 1979][research_smith_geddes_1979]
- [Smith and Meyer 1984][research_smith_meyer_1984]
- [Smith and Meyer 1987][research_smith_meyer_1987]
- [Smith and Patel 1995][research_smith_patel_1995]
- [Smith and Sarrafian 1986][research_smith_sarrafian_1986]
- [Smith and Schroeder 1986][research_smithrogerse_schroederkurtc_1986]
- [Smith et al 1991][research_smithrh_chisholmjd_1991]
- [Smith et al 1992][research_smith_garland_1992]
- [Smith et al 1998][research_smith_ward_1998]
- [Smith et al 2003][research_smithmarks_moestimothyr_2003]
- [Snell 1992][research_snell_1992]
- [Snell 1993][research_snell_1993]
- [Snell and Stout 1994][research_snell_stout_1994]
- [Snell and Stout 1998][research_snell_stout_1998]
- [Snell et al 1990][research_snell_garrardjr_1990]
- [Snell et al 1991][research_snell_garrardjr_1991]
- [Snell et al 1992][research_snell_enns_1992]
- [Snell et al 1998][research_snell_hess_1998]
- [Snow 1990][research_snow_1990]
- [Sobel and Shapiro 1984][research_sobel_shapiro_1984]
- [Sobel et al 1983][research_sobel_chung_1983]
- [Sobhani and Jayasuriya 1994][research_sobhani_jayasuriya_1994]
- [Sobron et al 2021][research_sobron_lundstrom_2021]
- [Soinne 1999][research_soinne_1999]
- [Sokolov et al 2017][research_sokolov_beklemichev_2017]
- [Solies 1994][research_solies_1994]
- [Solies 1995][research_solies_1995]
- [Soloway and Haley 2000][research_soloway_haley_2000]
- [Soltmann and Hall 2017][research_soltmann_hall_2017]
- [Somashekar and Immanuel Selwyn Raj 2018][research_somashekar_immanuelselwynraj_2018]
- [Somashekar and Immanuel Selwynraj 2022][research_v_a_2022]
- [Son et al 2015][research_son_sa_2015]
- [Son et al 2015][research_son_sa_2015_b]
- [Song 2008][research_song_2008]
- [Song and Huang 2026][research_song_huang_2026]
- [Song et al 2002][research_song_song_2002]
- [Song et al 2016][research_song_han_2016]
- [Song et al 2016][research_song_yang_2016]
- [Song et al 2022][research_song_sanchezcuevas_2022]
- [Soundararajan 2022][research_soundararajan_btn_2022]
- [Soundararajan and Sridhar 2024][research_soundararajan_sridhar_2024]
- [Souza et al 2019][research_souza_castillozuniga_2019]
- [Sowers and Tabakoff 1983][research_sowers_tabakoff_1983]
- [Spaans et al 2024][research_spaans_gilbert_2024]
- [Sparavalo 2021][research_sparavalo_2021]
- [Sparks][research_sparks]
- [Sparks 2003][research_sparks_2003]
- [Sparks and Sparks 1997][research_sparks_sparks_1997]
- [Sparks et al 1994][research_sparks_buffington_1994]
- [Spearman 1979][research_spearmanml_1979]
- [Speyer and Crues 1985][research_speyer_crues_1985]
- [Speyer and Crues 1987][research_speyer_crues_1987]
- [Spreiter and Stahara 1970][research_spreiter_stahara_1970]
- [Spurlin and Lueck 1984][research_spurlin_lueck_1984]
- [Srazhidinov et al 2023][research_srazhidinov_liang_2023]
- [Sreejith and Sathyabhama 2020][research_sreejith_sathyabhama_2020]
- [Srinathkumar 2015][research_srinathkumar_2015]
- [Srinathkumar et al 1995][research_srinathkumar_parameswaran_1995]
- [Srinivasa et al 2016][research_srinivasa_sridhara_2016]
- [Srivastava and Duraisamy 2018][research_srivastava_duraisamy_2018]
- [SS networked control and teleoperation 2017][research_ss_networked_2017]
- [Stable multiple model adaptive flight control for accommodation of a large class of control effector failures 1999][research_stable_multiple_1999]
- [Stalford 1979][research_stalford_1979]
- [Stalford and Hoffman 1989][research_stalford_hoffman_1989]
- [Stam and de Visser 2025][research_stam_devisser_2025]
- [Stanek and Visbal 1991][research_stanek_visbal_1991]
- [Stanley 1980][research_stanley_1980]
- [Starke 1983][research_starke_1983]
- [Starr and Varner 1976][research_starr_varner_1976]
- [Steer 2000][research_steer_2000]
- [Steer 2000][research_steer_2000_b]
- [Stein et al 1975][research_stein_hartmann_1975]
- [Stein et al 1977][research_stein_hartmann_1977]
- [Steinberg 1999][research_steinberg_1999]
- [Steinberg 2001][research_steinberg_2001]
- [Steinberg and DiGirolamo 1991][research_steinberg_digirolamo_1991]
- [Steinberg and Page 1998][research_steinberg_page_1998]
- [Steinberg and Page 1999][research_steinberg_page_1999]
- [Steinberg et al 1989][research_steinberg_carlson_1989]
- [Steinhoff 2002][research_steinhoff_2002]
- [Steinleitner et al 2022][research_steinleitner_frenzel_2022]
- [Steinmetz et al 1972][research_steinmetzgg_parrishrv_1972]
- [Stenfelt and Ringertz 2009][research_stenfelt_ringertz_2009]
- [Stenfelt and Ringertz 2010][research_stenfelt_ringertz_2010]
- [Stenfelt and Ringertz 2013][research_stenfelt_ringertz_2013]
- [Stengel 1975][research_stengel_1975]
- [Stengel 1980][research_stengel_1980]
- [Stengel and Miller 1978][research_stengel_miller_1978]
- [Stephan et al 2023][research_stephan_stumpf_2023]
- [Stephens 1931][research_stephens_1931]
- [Stewart 1992][research_jamesfstewart_1992]
- [Stewart and Shuck 1990][research_stewartjamesf_shuckthomasl_1990]
- [Stewart et al 1992][research_jamesfstewart_frankwburchamjr_1992]
- [Stewart et al 2026][research_stewart_dooher_2026]
- [Stifel 1979][research_stifel_1979]
- [Stojanovic and Debeljkovic 2004][research_stojanovic_ljdebeljkovic_2004]
- [Stojanovic and Debeljkovic 2004][research_stojanovic_ljdebeljkovic_2004_b]
- [Stolarik 2007][research_stolarik_2007]
- [Stoldt et al 2020][research_stoldt_johansen_2020]
- [Stoldt et al 2021][research_stoldt_korobenko_2021]
- [Stoll and Koenig 1983][research_stollf_koenigdg_1983]
- [Storms and Tilbury 2015][research_storms_tilbury_2015]
- [Stortz and ODonoghue 1995][research_stortzmichaelw_odonoghuedennisp_1995]
- [Stouder 1981][research_stouder_1981]
- [Stougie et al 2024][research_stougie_pollack_2024]
- [Strader et al 2016][research_strader_harper_2016]
- [Stradtner and Bekemeyer 2025][research_stradtner_bekemeyer_2025]
- [Strelkov and Bozhko 2026][research_strelkov_bozhko_2026]
- [Stremel 1994][research_stremel_1994]
- [Strickland et al 1996][research_stricklandmarke_bundickwthomas_1996]
- [Study of determining methods and preventing emergency conditions for the flight of an pilotless vehicle in case of failure of onboard equipment 2023][research_study_of_2023]
- [Su et al 1993][research_su_shyr_1993]
- [Su et al 2022][research_su_chu_2022]
- [Suarez et al 1992][research_suarezcarlosj_kramerbrianr_1992]
- [Suarez et al 1992][research_suarezcarlosj_malcolmgeraldn_1992]
- [Suarez et al 1993][research_suarezcarlosj_smithbrookec_1993]
- [Subagyo 2019][research_subagyo_2019]
- [Subbarao et al 2015][research_subbarao_tule_2015]
- [Sudderth et al 1975][research_sudderthrw_bohnjg_1975]
- [Sudhakar et al 2025][research_s_c_2025]
- [Suga and Yamazaki 2015][research_suga_yamazaki_2015]
- [Sugino et al 2019][research_sugino_harada_2019]
- [Sun and Boyd 2004][research_sun_boyd_2004]
- [Sun and van Kampen 2021][research_sun_vankampen_2021]
- [Sun et al 2019][research_sun_devisser_2019]
- [Sun et al 2020][research_sun_shi_2020]
- [Sun et al 2020][research_sun_wang_2020]
- [Sun et al 2022][research_sun_sengupta_2022]
- [Sun et al 2025][research_sun_liu_2025]
- [Sun et al 2026][research_sun_carmody_2026]
- [Sundaram and Wu 1983][research_sundaram_wu_1983]
- [Sung et al 2025][research_sung_spreizer_2025]
- [Surmann et al 2024][research_surmann_myschik_2024]
- [Suryakumar et al 2016][research_suryakumar_babbar_2016]
- [Sutherland and Maass 1932][research_sutherland_maass_1932]
- [Swaim 1977][research_swaim_1977]
- [Swaim 1978][research_swaim_1978]
- [Swaim and Connor 1968][research_swaim_connor_1968]
- [Swaim and Yen 1979][research_swaim_yen_1979]
- [Swank 2012][research_swankaaronj_2012]
- [Swarnkar and Kothari 2016][research_swarnkar_kothari_2016]
- [Syed et al 1990][research_syed_erhart_1990]
- [Syed et al 1992][research_syed_erhart_1992]
- [Symposium on Advanced Flow 2003][research_symposium_on_2003]
- [Szabolcsi 2018][research_szabolcsi_2018]
- [Szabolcsi 2018][research_szabolcsi_2018_b]
- [Szabolcsi 2018][research_szabolcsi_2018_c]
- [Szymanski et al 2025][research_szymanski_ghazi_2025]
- [Sánchez et al 2024][research_sanchez_cajas_2024]
- [Tachinina et al 2024][research_tachinina_lysenko_2024]
- [Taherinezhad and Ramirez-Serrano 2023][research_taherinezhad_ramirezserrano_2023]
- [Tai et al 2023][research_tai_wang_2023]
- [Tai et al 2026][research_tai_wang_2026]
- [Taj et al 2023][research_taj_bilal_2023]
- [Takarics et al 2020][research_takarics_mocsanyi_2020]
- [Takita and Kashitani 2016][research_takita_kashitani_2016]
- [Tal and Karaman 2021][research_tal_karaman_2021]
- [Tal and Karaman 2022][research_tal_karaman_2022]
- [Tamaskani et al 2026][research_tamaskani_alfi_2026]
- [Tamboli 1956][research_tamboli_1956]
- [Tamrat 1988][research_tamrat_1988]
- [Tamrat 2004][research_tamrat_2004]
- [Tamura and Oyama 2019][research_tamura_oyama_2019]
- [Tan 2004][research_tan_2004]
- [Tan et al 2018][research_tan_ma_2018]
- [Tang and Lai 2020][research_tang_lai_2020]
- [Tang et al 2024][research_tang_zhao_2024]
- [Tantrairatn and Veres 2015][research_tantrairatn_veres_2015]
- [Tanveer and Ahmad 2023][research_tanveer_ahmad_2023]
- [Tanveer and Ahmad 2023][research_tanveer_ahmad_2023_b]
- [Tarlanov and Kurbanismailov 2021][research_tarlanov_kurbanismailov_2021]
- [Tate and Gillard 1975][research_tate_gillard_1975]
- [Tavakoli 2024][research_tavakoli_2024]
- [Tavella et al 1986][research_tavella_lee_1986]
- [Tavella et al 1987][research_tavella_lee_1987]
- [Tavoularis 1999][research_tavoularis_1999]
- [Taylor 1988][research_taylor_1988]
- [Taylor 2015][research_taylor_2015]
- [Taylor and Skow 1988][research_taylor_skow_1988]
- [Taylor et al 1992][research_taylor_bennett_1992]
- [Teel 1999][research_teel_1999]
- [Teel 1999][research_teel_1999_b]
- [Tenhave et al 2026][research_tenhave_joiner_2026]
- [Teofilatto 2001][research_teofilatto_2001]
- [Teper and Stapleford 1965][research_teper_stapleford_1965]
- [Teper and Stapleford 1966][research_teper_stapleford_1966]
- [Terrell and Zein-Sabatto 2017][research_terrell_zeinsabatto_2017]
- [Terry 1964][research_terry_1964]
- [Thacker and Lan 1993][research_thacker_lan_1993]
- [Thamann et al 2015][research_thamann_smith_2015]
- [Thato Elijah and Rui Vasconcellos 2026][research_thatoelijah_ruivasconcellos_2026]
- [The Design of Flight Surveillance and Control System Software for Unmanned Rotorcraft’s Ground Control Station 2015][research_the_design_of_2015]
- [Theilliol et al 2015][research_theilliol_weber_2015]
- [Theodore and Celi 2002][research_theodore_celi_2002]
- [Theys et al 2016][research_theys_devos_2016]
- [Thomas 1991][research_thomas_1991]
- [Thomas et al 1977][research_thomas_paulsonjr_1977]
- [Thompson 1965][research_thompson_1965]
- [Thompson 1970][research_thompson_1970]
- [Thompson and Chiang 1990][research_thompson_chiang_1990]
- [Thompson and Gilruth 1940][research_thompsonfl_gilruthrr_1940]
- [Thompson et al 2017][research_thompson_xu_2017]
- [Thorsen and Horn 2017][research_thorsen_horn_2017]
- [Tian 2021][research_tian_2021]
- [Tian and Zhou 2021][research_tian_zhou_2021]
- [Tian et al 2015][research_tian_li_2015]
- [Tich et al 1987][research_tich_shaw_1987]
- [Ting et al 2016][research_ting_shun_2016]
- [Tinger 1987][research_tinger_1987]
- [Tinoco 2020][research_tinoco_2020]
- [Tipton and Smith 1995][research_tipton_smith_1995]
- [Tipton et al 1996][research_tipton_smith_1996]
- [Tischler and Hoh 1982][research_tischler_hoh_1982]
- [Tischler et al 1991][research_tischlermarkb_fletcherjayw_1991]
- [Tissir and Hmamed 1994][research_tissir_hmamed_1994]
- [Tohidi et al 2017][research_tohidi_yildiz_2017]
- [Tohidi et al 2018][research_tohidi_yildiz_2018]
- [Tohidi et al 2021][research_tohidi_yildiz_2021]
- [Tokugawa et al 2026][research_tokugawa_ishida_2026]
- [Tokutake et al 1999][research_tokutake_ohta_1999]
- [Toloei and Ghaderi 2026][research_toloei_ghaderi_2026]
- [Tomaine et al 1978][research_tomainerl_bryantwh_1978]
- [Tomczyk 1998][research_tomczyk_1998]
- [Tomczyk 2001][research_tomczyk_2001]
- [Tomczyk 2002][research_tomczyk_2002]
- [Tomlins 1983][research_tomlins_1983]
- [Tong 2020][research_michaelttong_2020]
- [Toppings and Yarusevych 2021][research_toppings_yarusevych_2021]
- [Torres et al 2017][research_torres_candelas_2017]
- [Torres et al 2022][research_torres_xu_2022]
- [Totah and Totah 1997][research_totah_totah_1997]
- [Tournes and Johnson 1999][research_tournes_johnson_1999]
- [Tournes and Landrum 2003][research_tournes_landrum_2003]
- [Tournes et al 1997][research_tournes_shtessel_1997]
- [Towfighi and Rockwell 1993][research_towfighi_rockwell_1993]
- [Traas et al 2026][research_traas_atmaca_2026]
- [Tran 2025][research_tran_2025]
- [Tran and Sawan 1983][research_tran_sawan_1983]
- [Tran et al 2017][research_tran_sakamoto_2017]
- [Tranchero and Latorre 2001][research_tranchero_latorre_2001]
- [Transonic theory for flow past slender fuselages and afterbodies 1970][research_transonic_theory_1970]
- [Traub 2021][research_traub_2021]
- [Traub 2024][research_traub_2024]
- [Traub 2024][research_traub_2024_b]
- [Traub and Coffman 2019][research_traub_coffman_2019]
- [Traub et al 1998][research_traub_moeller_1998]
- [Traub et al 2015][research_traub_botero_2015]
- [Travassos and Kaufman 1979][research_travassos_kaufman_1979]
- [Traven and Whitley 1995][research_traven_whitley_1995]
- [Tribuno et al 1976][research_tribuno_klein_1976]
- [Trippensee 1991][research_trippenseegary_1991]
- [Trueman et al 1993][research_trueman_kubina_1993]
- [Tsagkaris et al 2026][research_tsagkaris_holzapfel_2026]
- [Tsai et al 2016][research_tsai_chiang_2016]
- [Tsench and Kurbanov 2023][research_tsench_kurbanov_2023]
- [Tsench et al 2024][research_tsench_kurbanov_2024]
- [Tsien 1938][research_tsien_1938]
- [Tsu-Tian Lee and Shiow-Harn Lee 1988][research_tsutianlee_shiowharnlee_1988]
- [Tsushima et al 2024][research_tsushima_saitoh_2024]
- [Tsutsui et al 2021][research_tsutsui_takagi_2021]
- [Tu 1992][research_tu_1992]
- [Tuckerman 1923][research_tuckermanlb_1923]
- [Tumerdem and Yilmaz 2021][research_tumerdem_yilmaz_2021]
- [Turner et al 2002][research_turner_padfield_2002]
- [Tusa et al 2015][research_tusa_nicolaescu_2015]
- [Tvaryanas 2006][research_tvaryanas_2006]
- [Tvaryanas and Maupin 2013][research_tvaryanas_maupin_2013]
- [Tvaryanas et al 2012][research_tvaryanas_singer_2012]
- [Tzafestas 1975][research_tzafestas_1975]
- [Uchida et al 1986][research_uchida_shimemura_1986]
- [Uddin and Ryu 2016][research_uddin_ryu_2016]
- [Uhlig and Selig 2017][research_uhlig_selig_2017]
- [Ulizar 1997][research_ulizar_1997]
- [Umm-e-Aymon et al 2016][research_ummeaymon_shah_2016]
- [Unal 2021][research_unal_2021]
- [Ungermann 1988][research_ungermann_1988]
- [Uppoor et al 2026][research_uppoor_chopra_2026]
- [Uribe et al 2017][research_uribe_marty_2017]
- [Uribe Quintero et al 2024][research_uribequintero_takahashi_2024]
- [Urnes et al 1990][research_urnesjamesm_stewartjames_1990]
- [Urnes et al 1993][research_urnesjamesm_hoystephene_1993]
- [Urnes et al 2001][research_urnes_davidson_2001]
- [Uthra and Antony 2020][research_uthra_antony_2020]
- [Utsumi 2025][research_utsumi_2025]
- [Uybarreta et al 2025][research_uybarreta_grant_2025]
- [Valasek and Chakravorty 2015][research_valasek_chakravorty_2015]
- [Valasek and Downing 1993][research_valasekjohn_downingdavidr_1993]
- [Valasek and Walchli 1998][research_valasek_walchli_1998]
- [Valavanis 2017][research_valavanis_2017]
- [Vale J 2013][research_valej_2013]
- [Van Dam et al 1980][research_vandam_holmes_1980]
- [van Dam et al 1981][research_vandam_holmes_1981]
- [van den Aarssen et al 2019][research_vandenaarssen_visser_2019]
- [Van Der Hoeven 1981][research_vanderhoeven_1981]
- [Van Dommelen 1995][research_vandommelen_1995]
- [van Gool 1982][research_vangool_1982]
- [Van Orden 2001][research_vanorden_2001]
- [van Overeem et al 2022][research_vanovereem_wang_2022]
- [van Overeem et al 2023][research_vanovereem_wang_2023]
- [van Rooij and Cummings 2018][research_vanrooij_cummings_2018]
- [van Rooyen and Eshelby 1981][research_vanrooyen_eshelby_1981]
- [van Schalkwyk and Smit 2017][research_vanschalkwyk_smit_2017]
- [van Sluis et al 2026][research_vansluis_sinnige_2026]
- [Van Tuyl 1988][research_vantuyl_1988]
- [Vandersteen 1987][research_vandersteen_1987]
- [Vankadari et al 2018][research_vankadari_das_2018]
- [Varsha et al 2023][research_nvarsha_deshpande_2023]
- [Vauchel and Caro 2026][research_vauchel_caro_2026]
- [Vechtel and Buch 2022][research_vechtel_buch_2022]
- [Veismann et al 2023][research_veismann_gharib_2023]
- [Veletas 2026][research_veletas_2026]
- [Vendemia 1965][research_vendemia_rj_1965]
- [Vengate et al 2016][research_vengate_erturk_2016]
- [Venkatachari et al 2015][research_venkatachari_mullane_2015]
- [Venkataraman and Doman 2001][research_venkataraman_doman_2001]
- [Venkataraman and Seiler 2019][research_venkataraman_seiler_2019]
- [Venkataraman et al 2017][research_venkataraman_seiler_2017]
- [Venkateswara Rao and Go 2019][research_venkateswararao_go_2019]
- [Vepa 2021][research_vepa_2021]
- [Veresnikov and Goncharenko 2025][research_veresnikov_goncharenko_2025]
- [Verhaagen 1999][research_verhaagen_1999]
- [Verhaegen 1988][research_verhaegen_1988]
- [Verma and Junkins 1999][research_verma_junkins_1999]
- [Verma and Peyada 2018][research_verma_peyada_2018]
- [Vernyi et al 2026][research_vernyi_stanko_2026]
- [Viavattene and Mooij 2019][research_viavattene_mooij_2019]
- [Vicroy et al 2018][research_vicroy_huber_2018]
- [Viegas and Howe 1962][research_viegasjohnr_howejohnt_1962]
- [Vieira and Maughmer 2017][research_vieira_maughmer_2017]
- [Vieira dos Santos and Van Kampen 2025][research_vieiradossantos_vankampen_2025]
- [Vieten 1992][research_vieten_1992]
- [Vigh 1977][research_vigh_1977]
- [Vile et al 2020][research_vile_alwi_2020]
- [Vinje and Miller 1973][research_vinje_miller_1973]
- [Vinkler and Wood 1978][research_vinkler_wood_1978]
- [Vinkler et al 1979][research_vinkler_wood_1979]
- [Vinkler et al 1980][research_vinkler_wood_1980]
- [Viola and Angel 2015][research_viola_angel_2015]
- [Virnig and Bodden 1994][research_virnig_bodden_1994]
- [Visbal 1993][research_visbal_1993]
- [Visbal 1993][research_visbal_1993_b]
- [Visbal 1994][research_visbal_1994]
- [Visbal 1995][research_visbal_1995]
- [Visbal 1997][research_visbal_1997]
- [Visonneau et al 2022][research_visonneau_guilmineau_2022]
- [Visser 1999][research_visser_1999]
- [Vite and Mondie 2022][research_vite_mondie_2022]
- [Vlahostergios et al 2018][research_vlahostergios_komnos_2018]
- [Vlasceanu et al 2018][research_vlasceanu_popescu_2018]
- [Vogel 2016][research_vogel_2016]
- [Vogel and Junqueira 2017][research_vogel_junqueira_2017]
- [Von Hor and Guess 2017][research_vonhor_guess_2017]
- [Voracek and Clarke 1994][research_voracek_clarke_1994]
- [Vorobieff and Rockwell 1996][research_vorobieff_rockwell_1996]
- [Vos et al 2002][research_vos_brown_2002]
- [Voting software for fault-tolerant aircraft flight control systems 1993][research_voting_software_1993]
- [Vránics 2020][research_vranics_2020]
- [Wagdi 1984][research_wagdi_1984]
- [Wahler et al 2023][research_wahler_varriale_2023]
- [Walchli et al 1992][research_walchli_guyton_1992]
- [Waldmann 2015][research_waldmann_2015]
- [Waldmann et al 2023][research_waldmann_ehrle_2023]
- [Walker 1960][research_walker_1960]
- [Walker 1961][research_walker_1961]
- [Walker 1997][research_walkerlaurencea_1997]
- [Walter et al 2019][research_walter_ivler_2019]
- [Wan et al 2023][research_wan_ghoreyshi_2023]
- [Wandini et al 2016][research_wandini_mulyanto_2016]
- [Wang 1971][research_wang_1971]
- [Wang 1972][research_wang_1972]
- [Wang 2025][research_wang_2025]
- [Wang 2025][research_wang_2025_b]
- [Wang and Iliff 2004][research_wang_iliff_2004]
- [Wang and Qi 2021][research_wang_qi_2021]
- [Wang and Sutton 2004][research_wang_sutton_2004]
- [Wang and Wang 2020][research_wang_wang_2020]
- [Wang and Zhang 2021][research_wang_zhang_2021]
- [Wang and Zhang 2022][research_wang_zhang_2022]
- [Wang and Zhou 2022][research_wang_zhou_2022]
- [Wang et al 1986][research_wang_demiroz_1986]
- [Wang et al 1999][research_wang_lan_1999]
- [Wang et al 2015][research_wang_chen_2015]
- [Wang et al 2016][research_wang_gao_2016]
- [Wang et al 2016][research_wang_liu_2016]
- [Wang et al 2016][research_wang_wang_2016]
- [Wang et al 2016][research_wang_zhang_2016]
- [Wang et al 2017][research_wang_guo_2017]
- [Wang et al 2017][research_wang_huang_2017]
- [Wang et al 2017][research_wang_mu_2017]
- [Wang et al 2017][research_wang_ye_2017]
- [Wang et al 2018][research_wang_li_2018]
- [Wang et al 2018][research_wang_liu_2018]
- [Wang et al 2018][research_wang_song_2018]
- [Wang et al 2018][research_wang_vankampen_2018]
- [Wang et al 2018][research_wang_vankampen_2018_b]
- [Wang et al 2018][research_wang_xiang_2018]
- [Wang et al 2019][research_wang_vankampen_2019]
- [Wang et al 2019][research_wang_yuan_2019]
- [Wang et al 2019][research_wang_zuo_2019]
- [Wang et al 2020][research_wang_gong_2020]
- [Wang et al 2020][research_wang_tang_2020]
- [Wang et al 2020][research_wang_wang_2020_b]
- [Wang et al 2020][research_wang_wu_2020]
- [Wang et al 2020][research_wang_xu_2020]
- [Wang et al 2020][research_wang_zhang_2020]
- [Wang et al 2020][research_wang_zhu_2020]
- [Wang et al 2020][research_wang_zhu_2020_b]
- [Wang et al 2021][research_wang_liu_2021]
- [Wang et al 2021][research_wang_ma_2021]
- [Wang et al 2021][research_wang_qi_2021_b]
- [Wang et al 2021][research_wang_yang_2021]
- [Wang et al 2022][research_wang_tai_2022]
- [Wang et al 2022][research_wang_ye_2022]
- [Wang et al 2022][research_wang_zhao_2022]
- [Wang et al 2022][research_wang_zheng_2022]
- [Wang et al 2023][research_wang_hu_2023]
- [Wang et al 2023][research_wang_lu_2023]
- [Wang et al 2023][research_wang_shen_2023]
- [Wang et al 2023][research_wang_wang_2023]
- [Wang et al 2023][research_wang_zhao_2023]
- [Wang et al 2024][research_wang_guo_2024]
- [Wang et al 2024][research_wang_xu_2024]
- [Wang et al 2025][research_wang_fang_2025]
- [Wang et al 2025][research_wang_luo_2025]
- [Wang et al 2025][research_wang_luo_2025_b]
- [Wang et al 2025][research_wang_pei_2025]
- [Wang et al 2025][research_wang_yang_2025_b]
- [Wang et al 2025][research_wang_zhang_2025]
- [Wang et al 2026][research_wang_huang_2026]
- [Wang et al 2026][research_wang_yi_2026]
- [Wang Fawei 2016][research_wangfawei_2016]
- [Ward 1968][research_ward_1968]
- [Ward and Katz 1987][research_ward_katz_1987]
- [Ward and Katz 1987][research_ward_katz_1987_b]
- [Ward and Katz 1989][research_ward_katz_1989]
- [Ward and Katz 1989][research_ward_katz_1989_b]
- [Ward et al 1998][research_ward_monaco_1998]
- [Ward et al 2025][research_ward_ho_2025]
- [Ward et al 2026][research_ward_collins_2026]
- [Wardlaw et al 1975][research_wardlaw_andrewb_1975]
- [Warren 1989][research_warren_1989]
- [Warren 1990][research_warren_1990]
- [Warsop and Crowther 2019][research_warsop_crowther_2019_b]
- [Warsop et al 2019][research_warsop_crowther_2019]
- [Wasicko 1966][research_wasickorj_1966]
- [Watson and Komechak 1977][research_watson_komechak_1977]
- [Wauters et al 2019][research_wauters_browaeys_2019]
- [Way et al 2026][research_way_sescu_2026]
- [Webb et al 2016][research_webb_li_2016]
- [Webster and Shang 1989][research_webster_shang_1989]
- [Wei 1964][research_wei_1964]
- [Wei 2020][research_wei_2020]
- [Wei and Renliang 2015][research_wei_renliang_2015]
- [Wei et al 2017][research_wei_chen_2017]
- [Weibel et al 2015][research_weibel_lawrence_2015]
- [Weil 1981][research_weilj_1981]
- [Weiland 2021][research_weiland_2021]
- [Weinstein et al 1986][research_weinstein_posingies_1986]
- [Weinstein et al 2018][research_weinstein_hubbard_2018]
- [Weiser et al 2020][research_weiser_ossmann_2020]
- [Weiser et al 2024][research_weiser_looye_2024]
- [Weiss and Thielecke 2000][research_weiss_thielecke_2000]
- [Weisshaar 1977][research_weisshaar_1977]
- [Weissman 1972][research_weissman_1972]
- [Weissman 1973][research_weissman_1973]
- [Weissman 1974][research_weissman_1974]
- [Weissman 1975][research_weissman_1975]
- [Wells 2002][research_wellsscottr_2002]
- [Wells and Hess 2002][research_wells_hess_2002]
- [Wells and Hess 2003][research_wells_hess_2003]
- [Wells et al 1979][research_wells_banda_1979]
- [Wells et al 1982][research_wells_banda_1982]
- [Welp et al 1975][research_welp_chace_1975]
- [Wen and Tian 2020][research_wen_tian_2020]
- [Wendel et al 1991][research_wendel_boland_1991]
- [Wendorff et al 2016][research_wendorff_alonso_2016]
- [Werbos 2001][research_werbos_2001]
- [Werner et al 2022][research_werner_schutte_2022]
- [Werner et al 2024][research_werner_schutte_2024]
- [West and Phillips 2020][research_west_phillips_2020]
- [West et al 2017][research_west_reuter_2017]
- [Westbrook 1964][research_westbrook_1964]
- [Weyl 1944][research_weyl_1944]
- [Weyl 1945][research_weyl_1945]
- [Weyl 1945][research_weyl_1945_b]
- [Weyl 1945][research_weyl_1945_c]
- [Weyl 1945][research_weyl_1945_d]
- [Weyl 1945][research_weyl_1945_e]
- [Whitaker and Gowadia 1994][research_whitaker_gowadia_1994]
- [Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]
- [White 1977][research_white_1977]
- [White 1977][research_white_1977_b]
- [White 1995][research_white_1995]
- [White and Innis 1959][research_whitemauriced_innisrobertc_1959]
- [White et al 2025][research_white_narsipur_2025]
- [Whitefield et al 1981][research_whitefield_griffith_1981]
- [Whiting 1996][research_whitingmatthewrobert_1996]
- [Whoric 1974][research_whoric_1974]
- [Wickens and Dixon 2002][research_wickens_dixon_2002]
- [Wickman 1953][research_wickman_1953]
- [Widiyanti et al 2024][research_widiyanti_asmoro_2024]
- [Wilcox 1913][research_wilcox_1913]
- [Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]
- [Willebeek-LeMair and Rhinehart 2023][research_willebeeklemair_rhinehart_2023]
- [Williams 1926][research_williams_1926]
- [Williams 2004][research_williams_2004]
- [Williams et al 2025][research_williams_niestroy_2025]
- [Williamson 1951][research_williamson_1951]
- [Wills and Wise 1976][research_wills_wise_1976]
- [Wilson and Riccardi 2022][research_wilson_riccardi_2022]
- [Wilson et al 1993][research_wilson_riley_1993]
- [Winchenbach et al 1982][research_winchenbach_chelekis_1982]
- [Winchenbach et al 1984][research_winchenbach_uselton_1984]
- [Wingrove 1978][research_wingroverc_1978]
- [Winslow et al 2018][research_winslow_hrishikeshavan_2018]
- [Wisbacher et al 2025][research_wisbacher_ossmann_2025]
- [Wise 1992][research_wise_1992]
- [Wise and Sedwick 1998][research_wise_sedwick_1998]
- [Wise et al 1999][research_wise_brinker_1999]
- [Wise et al 1999][research_wise_sedwick_1999]
- [Withrow-Maser et al 2021][research_withrowmaser_malpica_2021]
- [Witkowski et al 2022][research_witkowski_williams_2022]
- [Witte et al 2003][research_witte_monson_2003]
- [Wittenberg 2001][research_wittenberg_2001]
- [Wolf 1978][research_wolf_1978]
- [Wolf et al 2016][research_wolf_shelley_2016]
- [Wolfe and Oberkampf 1982][research_wolfe_oberkampf_1982]
- [Wolowicz et al 1979][research_wolowiczch_brownjsjr_1979]
- [Wood 2003][research_wood_2003]
- [Wood and Bauer 1999][research_woodrichardm_bauerstevenxs_1999]
- [Wood and Murphy 1955][research_wood_murphy_1955]
- [Wood et al 2019][research_wood_araujoestrada_2019]
- [Woodbury et al 2015][research_woodbury_valasek_2015]
- [Woodruff 2009][research_woodruffstephenl_2009]
- [Woods et al 1996][research_woods_sillence_1996]
- [Woolcock and Schmid 2026][research_woolcock_schmid_2026]
- [Woolley 1978][research_woolley_1978]
- [Wornom 1960][research_wornomde_1960]
- [Wortman et al 1975][research_wortman_duket_1975]
- [Wright 1975][research_wright_1975]
- [Wrist and Hubner 2017][research_wrist_hubner_2017]
- [Wu 1981][research_wu_1981]
- [Wu 2025][research_wu_2025]
- [Wu and Perng 2004][research_wu_perng_2004]
- [Wu and Sankar 1980][research_wu_sankar_1980]
- [Wu and Zhu 2024][research_wu_zhu_2024]
- [Wu et al 2015][research_wu_li_2015]
- [Wu et al 2016][research_wu_chen_2016]
- [Wu et al 2017][research_wu_xiao_2017]
- [Wu et al 2017][research_wu_yang_2017]
- [Wu et al 2018][research_wu_chen_2018]
- [Wu et al 2018][research_wu_lv_2018]
- [Wu et al 2026][research_wu_lian_2026]
- [X-29 Research Aircraft 1991][research_x_29_research_1991]
- [Xi and Zhao 2017][research_xi_zhao_2017]
- [Xi et al 2025][research_xi_dai_2025]
- [Xia and Zhang 2019][research_xia_zhang_2019]
- [Xiao et al 2016][research_xiao_li_2016]
- [Xiao et al 2018][research_xiao_belt_2018]
- [Xiao et al 2018][research_xiao_zhang_2018]
- [Xiao et al 2025][research_xiao_fan_2025]
- [Xiaofeng Ai et al 2016][research_xiaofengai_fengzhao_2016]
- [Xie and Low 2017][research_xie_low_2017]
- [Xie et al 2011][research_xie_yang_2011]
- [Xie et al 2022][research_xie_cabecinhas_2022]
- [Xin et al 2024][research_xin_chen_2024]
- [Xing and Zhang 2017][research_xing_zhang_2017]
- [Xinghua 2018][research_xinghua_2018]
- [Xiong and Nguyen 2023][research_xiong_nguyen_2023]
- [Xiong et al 2026][research_xiong_nguyen_2026]
- [Xiuming Liu et al 2016][research_xiumingliu_yingwang_2016]
- [Xu 2025][research_xu_2025]
- [Xu and Feng 2025][research_xu_feng_2025]
- [Xu and Yu 2025][research_xu_yu_2025]
- [Xu and Zhang 2024][research_xu_zhang_2024]
- [Xu and Zhang 2025][research_xu_zhang_2025]
- [Xu and Zhou 2015][research_xu_zhou_2015]
- [Xu et al 2016][research_xu_jiang_2016]
- [Xu et al 2017][research_xu_jiang_2017]
- [Xu et al 2019][research_xu_petrunin_2019]
- [Xu et al 2019][research_xu_tan_2019]
- [Xu et al 2020][research_xu_ge_2020]
- [Xu et al 2024][research_xu_tian_2024]
- [Xuan and Cheng 2016][research_h_s_2016]
- [Xue et al 2021][research_xue_yunsong_2021]
- [Yajnik 1977][research_yajnik_1977]
- [Yamaguchi et al 2000][research_yamaguchi_ohno_2000]
- [Yamaguchi et al 2001][research_yamaguchi_ohara_2001]
- [Yamaoka 1963][research_yamaoka_1963]
- [Yamazaki et al 2017][research_yamazaki_yamagishi_2017]
- [Yamazaki et al 2018][research_yamazaki_yamagishi_2018]
- [Yan and Shi 2024][research_yan_shi_2024]
- [Yan and Shi 2025][research_yan_shi_2025]
- [Yan et al 2019][research_yan_li_2019]
- [Yan et al 2025][research_yan_sun_2025]
- [Yanagihara et al 1991][research_yanagihara_suzuki_1991]
- [Yang 2024][research_yang_2024]
- [Yang 2024][research_yang_2024_b]
- [Yang and Agarwal 2019][research_yang_agarwal_2019]
- [Yang and Kabamba 1991][research_yang_kabamba_1991]
- [Yang and Xiong 2023][research_yang_xiong_2023]
- [Yang and Yee 2022][research_yang_yee_2022]
- [Yang et al 2015][research_yang_chen_2015]
- [Yang et al 2016][research_yang_meng_2016]
- [Yang et al 2019][research_yang_liu_2019]
- [Yang et al 2023][research_yang_tan_2023]
- [Yang et al 2025][research_yang_zhen_2025]
- [Yang et al 2026][research_yang_wang_2026]
- [Yang et al 2026][research_yang_xu_2026]
- [Yaniv 1992][research_yaniv_1992]
- [Yao and Wu 2019][research_yao_wu_2019]
- [Yarlett et al 2000][research_yarlett_adrezin_2000]
- [Yasue 2020][research_yasue_2020]
- [Yavuztürk and Topbas 2020][research_yavuzturk_topbas_2020]
- [Yavuztürk et al 2017][research_yavuzturk_topbas_2017]
- [Yazdi et al 2026][research_yazdi_gray_2026]
- [Yazdi et al 2026][research_yazdi_reist_2026]
- [Yeager 1997][research_yeagerjessiec_1997]
- [Yechout 1988][research_yechout_1988]
- [Yechout and Schweikhard 1984][research_yechout_schweikhard_1984]
- [Yedavalli 2024][research_yedavalli_2024]
- [Yeg̃in and Özbay 2023][research_yegin_ozbay_2023]
- [Yeo et al 2015][research_yeo_atkins_2015]
- [Yi et al 1979][research_yi_heimbold_1979]
- [Yifei et al 2015][research_yifei_zongxia_2015]
- [Yijie et al 2023][research_yijie_deshuang_2023]
- [Yiming et al 2019][research_yiming_mei_2019]
- [Yin and Wang 2017][research_yin_wang_2017]
- [Yin et al 2019][research_yin_chu_2019]
- [Yin et al 2019][research_yin_wang_2019]
- [Yip et al 1990][research_yip_fratello_1990]
- [Yip et al 1990][research_yip_fratello_1990_b]
- [Yip et al 1991][research_yip_fratello_1991]
- [Yondo et al 2018][research_yondo_andres_2018]
- [Yong et al 2020][research_yong_wu_2020]
- [Yongming and Yuanqing 2015][research_yongming_yuanqing_2015]
- [Yonke et al 1985][research_yonke_terrell_1985]
- [Yoo 2018][research_yoo_2018]
- [Yoo and Duensing 2019][research_yoo_duensing_2019]
- [Yoo et al 2021][research_yoo_jang_2021]
- [York and Anderson 1994][research_york_anderson_1994]
- [You et al 2013][research_you_bromby_2013]
- [Youcef-Toumi and Bobbett 1991][research_youceftoumi_bobbett_1991]
- [Youcef-Toumi and Wu 1992][research_youceftoumi_wu_1992]
- [Younes et al 2019][research_younes_noura_2019]
- [Yu 2021][research_yu_2021]
- [Yu and Kim 2024][research_yu_kim_2024]
- [Yu and Wang 2024][research_yu_wang_2024]
- [Yu et al 2017][research_yu_fu_2017]
- [Yu et al 2017][research_yu_wang_2017]
- [Yu et al 2017][research_yu_zhang_2017]
- [Yu et al 2019][research_yu_xiaoxiong_2019]
- [Yu et al 2019][research_yu_zhang_2019]
- [Yu et al 2022][research_yu_li_2022]
- [Yu et al 2023][research_yu_li_2023]
- [Yu et al 2023][research_yu_li_2023_b]
- [Yu et al 2023][research_yu_li_2023_c]
- [Yu et al 2023][research_yu_zhang_2023]
- [Yu et al 2024][research_yu_bi_2024]
- [Yu et al 2024][research_yu_hrynuk_2024]
- [Yuan 2026][research_yuan_2026]
- [Yuan and Zhou 2024][research_yuan_zhou_2024]
- [Yuan et al 2020][research_yuan_thomson_2020]
- [Yuan et al 2021][research_yuan_anderson_2021]
- [Yue et al 2003][research_yue_won_2003]
- [Yue et al 2009][research_yue_wang_2009]
- [Yue et al 2013][research_yue_wang_2013]
- [Yue et al 2017][research_yue_wang_2017]
- [Yue Zhao et al 2016][research_yuezhao_letianlin_2016]
- [Yuksek and Inalhan 2020][research_yuksek_inalhan_2020]
- [Yuksek and Inalhan 2022][research_yuksek_inalhan_2022]
- [Yuma Test Center Yuma Proving Ground Az 2008][research_yumatestcenteryumaprovinggroundaz_2008]
- [Yunerovna and Valerievich 2015][research_yunerovna_valerievich_2015]
- [Yuzawa and Ogami 2002][research_yuzawa_ogami_2002]
- [Yılmaz and German 2024][research_yilmaz_german_2024]
- [Zagranski et al 1974][research_zagranski_lamart_1974]
- [Zahedi and Haeri 2017][research_zahedi_haeri_2017]
- [Zanette and Almeida 2015][research_zanette_almeida_2015]
- [Zannetti and Onofri 1984][research_zannetti_onofri_1984]
- [Zanoni et al 2022][research_zanoni_gerosa_2022]
- [Zastawny 2016][research_zastawny_2016]
- [Zaytseva et al 2021][research_zaytseva_kuznetsov_2021]
- [Zeitler et al 2018][research_zeitler_schwierz_2018]
- [Zeller et al 1982][research_zellerj_lehtinenb_1982]
- [Zennir et al 2017][research_zennir_larabi_2017]
- [Zennir et al 2017][research_zennir_larabi_2017_b]
- [Zeyada et al 1998][research_zeyada_hess_1998]
- [Zeyada et al 1999][research_zeyada_hess_1999]
- [Zha and Li 2025][research_zha_li_2025]
- [Zhai et al 2025][research_zhai_li_2025]
- [Zhang 2023][research_zhang_2023]
- [Zhang 2026][research_zhang_2026]
- [Zhang and Bradley 2022][research_zhang_bradley_2022]
- [Zhang and He 2026][research_zhang_he_2026]
- [Zhang and He 2026][research_zhang_he_2026_b]
- [Zhang and Meng 2019][research_zhang_meng_2019]
- [Zhang and Ran 2023][research_zhang_ran_2023]
- [Zhang and Samtaney 2016][research_zhang_samtaney_2016]
- [Zhang et al 1992][research_zhang_saeki_1992]
- [Zhang et al 2015][research_zhang_tomizuka_2015]
- [Zhang et al 2016][research_zhang_pang_2016]
- [Zhang et al 2017][research_zhang_devisser_2017]
- [Zhang et al 2017][research_zhang_duan_2017]
- [Zhang et al 2017][research_zhang_liu_2017]
- [Zhang et al 2017][research_zhang_wang_2017]
- [Zhang et al 2017][research_zhang_wang_2017_b]
- [Zhang et al 2017][research_zhang_zhang_2017]
- [Zhang et al 2018][research_zhang_chen_2018]
- [Zhang et al 2018][research_zhang_shuang_2018]
- [Zhang et al 2019][research_zhang_wang_2019]
- [Zhang et al 2019][research_zhang_zhou_2019]
- [Zhang et al 2020][research_zhang_han_2020]
- [Zhang et al 2021][research_zhang_du_2021]
- [Zhang et al 2021][research_zhang_su_2021]
- [Zhang et al 2023][research_zhang_chen_2023]
- [Zhang et al 2023][research_zhang_huang_2023]
- [Zhang et al 2023][research_zhang_jiang_2023]
- [Zhang et al 2023][research_zhang_zhang_2023]
- [Zhang et al 2024][research_zhang_liu_2024]
- [Zhang et al 2024][research_zhang_xu_2024]
- [Zhang et al 2024][research_zhang_zhou_2024]
- [Zhang et al 2025][research_zhang_sun_2025]
- [Zhang et al 2026][research_zhang_wang_2026_b]
- [Zhang et al 2026][research_zhang_yang_2026]
- [Zhao and Zhu 2016][research_zhao_zhu_2016]
- [Zhao et al 2021][research_zhao_duan_2021]
- [Zhao et al 2022][research_zhao_li_2022]
- [Zhao et al 2023][research_zhao_luo_2023]
- [Zhao et al 2024][research_zhao_wang_2024]
- [Zhao et al 2024][research_zhao_xu_2024]
- [Zhao et al 2024][research_zhao_zhang_2024]
- [Zhen and Hao 2020][research_zhen_hao_2020]
- [Zheng and Horn 2015][research_zheng_horn_2015]
- [Zheng and Li 2019][research_zheng_li_2019]
- [Zhishuai and Lingling 2022][research_zhishuai_lingling_2022]
- [Zhong and Huang 2023][research_zhong_huang_2023]
- [Zhong et al 2023][research_zhong_pu_2023]
- [Zhou 2023][research_zhou_2023]
- [Zhou and Deng 2024][research_zhou_deng_2024]
- [Zhou and Huang 2021][research_zhou_huang_2021]
- [Zhou and Huang 2021][research_zhou_huang_2021_c]
- [Zhou and Huang 2022][research_zhou_huang_2022_b]
- [Zhou and Huang 2022][research_zhou_huang_2022_c]
- [Zhou and Huang 2023][research_zhou_huang_2023]
- [Zhou and Huang 2023][research_zhou_huang_2023_b]
- [Zhou and Ma 2025][research_zhou_ma_2025]
- [Zhou and Wang 2026][research_zhou_wang_2026]
- [Zhou et al 2015][research_zhou_canova_2015]
- [Zhou et al 2016][research_zhou_canova_2016]
- [Zhou et al 2019][research_zhou_diskin_2019]
- [Zhou et al 2019][research_zhou_liu_2019]
- [Zhou et al 2021][research_zhou_ho_2021]
- [Zhou et al 2021][research_zhou_huang_2021_b]
- [Zhou et al 2021][research_zhou_zhong_2021]
- [Zhou et al 2022][research_zhou_wang_2022]
- [Zhou et al 2022][research_zhou_yang_2022]
- [Zhou et al 2023][research_zhou_liu_2023]
- [Zhu 2024][research_zhu_2024]
- [Zhu and Duan 2015][research_zhu_duan_2015]
- [Zhu and Guo 2019][research_zhu_guo_2019]
- [Zhu and Qin 2023][research_zhu_qin_2023]
- [Zhu and Zhang 2018][research_zhu_zhang_2018]
- [Zhu et al 2016][research_zhu_gao_2016]
- [Zhu et al 2019][research_zhu_liu_2019]
- [Zhu et al 2022][research_zhu_shi_2022]
- [Ziemianski 1981][research_ziemianskija_1981]
- [Zilli et al 2017][research_zilli_sutton_2017]
- [Zilliac et al 1990][research_zilliac_degani_1990]
- [Zilstra and Johnson 2026][research_zilstra_johnson_2026]
- [Zimbelman and Rouser 2025][research_zimbelman_rouser_2025]
- [Zimmnau et al 2025][research_zimmnau_cremer_2025]
- [Zimper and Hummel 2018][research_zimper_hummel_2018]
- [Zipperer et al 1975][research_zipperer_jenney_1975]
- [Zohar and Er-El 1988][research_zohar_erel_1988]
- [Zolanvari et al 2018][research_zolanvari_teixeira_2018]
- [Zolotas 2023][research_zolotas_2023]
- [Zou et al 2017][research_zou_yin_2017]
- [Zou et al 2026][research_zou_xie_2026]
- [Zou et al 2026][research_zou_zhen_2026]
- [Zuhri 2025][research_zuhri_2025]
- [Zwerger et al 2015][research_zwerger_hickel_2015]
- [Zwerneman and Eller 1994][research_zwerneman_eller_1994]
- [Çoban 2020][research_coban_2020]
- [Çoban and Oktay 2018][research_coban_oktay_2018]
- [Özdemi̇r 2020][research_ozdemir_2020]
- [Öznurlu et al 2023][research_oznurlu_bayri_2023]
- [Żugaj 2017][research_zugaj_2017]

[research_088_stability_1994]: https://doi.org/10.1016/0967-0661(94)90103-1
[research_122_neural_1993]: https://doi.org/10.1016/0967-0661(93)90141-d
[research_213_development_1994]: https://doi.org/10.1016/0967-0661(94)91002-2
[research_a_multi_1979]: https://doi.org/10.2514/6.1979-1700
[research_a_novel_2020]: https://doi.org/10.46300/9106.2020.14.6
[research_a_simple_1994]: https://doi.org/10.1016/0967-0661(94)90222-4
[research_abdelhamid_1985]: https://doi.org/10.21608/asat.1985.26464
[research_abdelmalek_marmarelis_1988]: https://doi.org/10.1109/21.87065
[research_abdullah_kashif_2025]: https://doi.org/10.1109/icet64964.2025.11102913
[research_abdullah_miao_2026]: https://doi.org/10.37256/jeee.5120269903
[research_abdullahi_maimako_2026]: https://doi.org/10.2514/6.2026-4207
[research_abdulrahim_bates_2019]: https://doi.org/10.2514/6.2019-0825
[research_abe_1993]: https://doi.org/10.1016/0167-6105(93)90163-i
[research_abidi_yildiz_2016]: https://doi.org/10.1002/rnc.3513
[research_abouheaf_gueaieb_2020]: https://doi.org/10.1049/iet-cta.2018.6163
[research_abras_tuckey_2023]: https://doi.org/10.2514/6.2023-0232
[research_abuelola_alqaisia_2024]: https://doi.org/10.1109/rem63063.2024.10735705
[research_abusalem_palaia_2023]: https://doi.org/10.3390/aerospace10100874
[research_accommodation_of_1991]: https://doi.org/10.1109/37.103360
[research_ackerman_gregory_2019]: https://doi.org/10.1109/icuas.2019.8797739
[research_acquatellab_vanekeren_2017]: https://doi.org/10.1016/j.ifacol.2017.08.1265
[research_adak_mandal_2024]: https://doi.org/10.1063/5.0237871
[research_adams_1972]: https://doi.org/10.2514/6.1972-962
[research_adams_banda_1993]: https://doi.org/10.1109/87.238401
[research_adams_banda_1993_b]: https://doi.org/10.23919/acc.1993.4793098
[research_adams_hatch_1971]: https://doi.org/10.2514/3.59103
[research_adams_hatchjr_1970]: https://doi.org/10.2514/6.1970-568
[research_adams_johnc_1968]: https://doi.org/10.21236/ad0667523
[research_adamsrichardj_1993]: https://ntrs.nasa.gov/citations/19940020626
[research_addington_2000]: https://doi.org/10.21236/ada383535
[research_addington_myatt_2000]: https://doi.org/10.21236/ada383536
[research_addoms_1977]: https://doi.org/10.2514/3.58764
[research_adeyi_alabi_2024]: https://doi.org/10.47852/bonviewaaes42023485
[research_aditya_srinivas_2019]: https://doi.org/10.1088/1742-6596/1172/1/012034
[research_adiwidodo_wijaya_2022]: https://doi.org/10.51278/ajse.v1i1.396
[research_advanced_control_2023]: https://doi.org/10.48047/nq.2022.20.10.nq551258
[research_advisorygroupforaerospaceresearchanddevelopment_1999]: https://ntrs.nasa.gov/citations/19990032449
[research_aerodynamic_analysis_2017]: https://doi.org/10.21884/ijmter.2017.4171.1xs3v
[research_aerodynamic_characteristics_1951]: https://ntrs.nasa.gov/citations/20030067330
[research_aerodynamic_performance_2025]: https://doi.org/10.18178/ijmerr.14.1.48-58
[research_aerodynamics_of_1976]: https://doi.org/10.2514/6.1976-198
[research_agarwal_ng_2021]: https://doi.org/10.1109/icuas51884.2021.9476830
[research_agarwalak_1988]: https://ntrs.nasa.gov/citations/19880016737
[research_aghazadehardebili_martella_2025]: https://doi.org/10.11591/ijai.v14.i1.pp240-251
[research_ahmad_li_2022]: https://doi.org/10.1109/icuas54217.2022.9836229
[research_ahmadi_haeri_2017]: https://doi.org/10.1115/1.4036069
[research_ahmadi_haeri_2018]: https://doi.org/10.1115/1.4039086
[research_ahmadidastgerdi_asadi_2022]: https://doi.org/10.55212/ijaa.1033224
[research_ahmed_elbanna_2025]: https://doi.org/10.1142/s2301385026500366
[research_ahmed_zakaria_2024]: https://doi.org/10.1142/s230138502550027x
[research_ahmedzaid_ioannou_1990]: https://doi.org/10.23919/acc.1990.4790835
[research_aircraft_design_1989]: https://doi.org/10.2514/6.1989-1265
[research_aircraft_moments_1996]: https://doi.org/10.1016/b978-034063170-6/50016-5
[research_aircraft_performance_2015]: https://doi.org/10.17559/tv-20131220145918
[research_airforceflighttestcenteredwardsafbca_1974]: https://doi.org/10.21236/ada011561
[research_airforceflighttestcenteredwardsafbca_1974_b]: https://doi.org/10.21236/ada011562
[research_airforcetestpilotschooledwardsafbca_1969]: https://doi.org/10.21236/ada319985
[research_airforcetestpilotschooledwardsafbca_1981]: https://doi.org/10.21236/ada320347
[research_airforcetestpilotschooledwardsafbca_1988]: https://doi.org/10.21236/ada319984
[research_airforcetestpilotschooledwardsafbca_1988_b]: https://doi.org/10.21236/ada319979
[research_airforcetestpilotschooledwardsafbca_1988_d]: https://doi.org/10.21236/ada319975
[research_airforcetestpilotschooledwardsafbca_1989]: https://doi.org/10.21236/ada319980
[research_airforcetestpilotschooledwardsafbca_1990]: https://doi.org/10.21236/ada319978
[research_airforcetestpilotschooledwardsafbca_1990_b]: https://doi.org/10.21236/ada319977
[research_airforcetestpilotschooledwardsafbca_1990_c]: https://doi.org/10.21236/ada320062
[research_airforcetestpilotschooledwardsafbca_1990_d]: https://doi.org/10.21236/ada320058
[research_airforcetestpilotschooledwardsafbca_1990_e]: https://doi.org/10.21236/ada319976
[research_airforcetestpilotschooledwardsafbca_1991]: https://doi.org/10.21236/ada319981
[research_airforcetestpilotschooledwardsafbca_1991_c]: https://doi.org/10.21236/ada319972
[research_airforcetestpilotschooledwardsafbca_1992]: https://doi.org/10.21236/ada319982
[research_ajaj_2021]: https://doi.org/10.2514/1.c035940
[research_akagi_shinomiya_1997]: https://doi.org/10.1115/97-gt-289
[research_akaryildiz_demirkiran_2024]: https://doi.org/10.2514/6.2024-2876
[research_akbari_greeff_2024]: https://doi.org/10.1109/icuas60882.2024.10557089
[research_akgumusgok_2024]: https://doi.org/10.14744/thermal.0000892
[research_akmeliawati_mareels_1999]: https://doi.org/10.1016/s1474-6670(17)57359-0
[research_akram_tedesco_2020]: https://doi.org/10.5220/0009894800810088
[research_aksteter_parks_1994]: https://doi.org/10.2514/6.1994-2147
[research_alabsi_fields_2017]: https://doi.org/10.2514/6.2017-0697
[research_alag_kaufman_1974]: https://doi.org/10.2514/6.1974-886
[research_alaian_basuno_2016]: https://doi.org/10.3923/itj.2017.44.50
[research_alam_mamun_2021]: https://doi.org/10.1063/5.0037494
[research_albostan_gokasan_2018]: https://doi.org/10.1016/j.ast.2018.04.011
[research_albrecht_naguib_2019]: https://doi.org/10.2514/6.2019-2157
[research_albrecht_olson_2022]: https://doi.org/10.2514/6.2022-1055
[research_aldosari_feron_2025]: https://doi.org/10.1007/s12217-025-10182-8
[research_aleisa_kontis_2023]: https://doi.org/10.2514/1.c037258
[research_aleisa_kontis_2023_b]: https://doi.org/10.2514/1.c037257
[research_alexander_1979]: https://doi.org/10.21236/ada068345
[research_alexander_1979_b]: https://doi.org/10.21236/ada068346
[research_alexander_1991]: https://doi.org/10.21236/ada240263
[research_alexander_1993]: https://doi.org/10.2514/6.1993-3627
[research_alexander_2025]: https://doi.org/10.4050/sm_handling_2025-5295
[research_alferov_vernikova_1982]: https://doi.org/10.1007/bf01090706
[research_alford_altman_2004]: https://doi.org/10.2514/6.2004-4973
[research_alford_knarr_1999]: https://doi.org/10.21236/ada371942
[research_algozino_maranondileo_2015]: https://doi.org/10.2514/6.2015-3168
[research_alhazmi_ghazi_2021]: https://doi.org/10.2514/6.2021-0893
[research_ali_rasani_2024]: https://doi.org/10.37934/cfdl.17.6.4556
[research_allee_eg_1973]: https://doi.org/10.21236/ad0758817
[research_allen_2017]: https://doi.org/10.2514/6.2017-3888
[research_allenhjulian_perkinsedwardw_1951]: https://ntrs.nasa.gov/citations/19930090962
[research_allenmichaelj_ryanjack_2002]: https://ntrs.nasa.gov/citations/20030004787
[research_almashhadani_2019]: https://doi.org/10.1177/0020294019866860
[research_almosnino_1983]: https://doi.org/10.2514/6.1983-35
[research_almosnino_1985]: https://doi.org/10.2514/3.9057
[research_alqadi_eljack_2016]: https://doi.org/10.2514/6.2016-2083
[research_alshabi_saleh_2024]: https://doi.org/10.1117/12.3013949
[research_alsolami_bhattacharjee_2025]: https://doi.org/10.1145/3769102.3774640
[research_alston_1936]: https://doi.org/10.1108/eb030012
[research_alstrom_paul_2023]: https://doi.org/10.4050/sm_2023_hq-1193
[research_altman_2008]: https://doi.org/10.21236/ada494088
[research_altunkaya_ozkol_2025]: https://doi.org/10.2514/1.g008752
[research_alvarezmunoz_castillozamora_2019]: https://doi.org/10.1109/icuas.2019.8798094
[research_alyshev_melnikov_2016]: https://doi.org/10.17586/2226-1494-2016-16-5-928-935
[research_alzubaidi_stol_2022]: https://doi.org/10.1109/icuas54217.2022.9836158
[research_amato_ambrosino_1996]: https://doi.org/10.2514/3.21636
[research_amato_cortigiani_2022]: https://doi.org/10.4050/sm_2022_cs-1154
[research_amaya_xiang_2026]: https://doi.org/10.2514/6.2026-4681
[research_americaninstituteofaeronauticsandastronautics_1992]: https://ntrs.nasa.gov/citations/19930027254
[research_an_overview_2017]: https://doi.org/10.21884/ijmter.2017.4120.y54mr
[research_an_wang_2025]: https://doi.org/10.1061/jaeeez.aseng-6056
[research_analysis_of_2024]: https://doi.org/10.36652/0869-4931-2024-78-7-329-331
[research_analytic_constraints_1999]: https://doi.org/10.1109/acc.1999.786218
[research_analytical_synthesis_2024]: https://doi.org/10.36652/0869-4931-2024-78-9-404-410
[research_ananda_vahora_2017]: https://doi.org/10.2514/6.2017-4077
[research_ananthkrishnan_sinha_2023]: https://doi.org/10.61653/joast.v65i4.2013.877
[research_ananthkrishnan_sudhakar_1994]: https://doi.org/10.2514/3.46591
[research_ananthkrishnan_sudhakar_1995]: https://doi.org/10.2514/3.46807
[research_andersen_bagby_1965]: https://doi.org/10.2514/6.1965-796
[research_anderson_1970]: https://doi.org/10.21236/ad0710590
[research_anderson_1984]: https://doi.org/10.2514/6.1984-2093
[research_anderson_1985]: https://doi.org/10.2514/3.45218
[research_anderson_flickinger_1954]: https://doi.org/10.21236/ad0046351
[research_anderson_phillips_2004]: https://doi.org/10.2514/6.2004-12
[research_anderson_vincent_1985]: https://doi.org/10.1109/cdc.1985.268918
[research_andre_morris_1981]: https://ntrs.nasa.gov/citations/19820002894
[research_andrewswh_simag_1980]: https://ntrs.nasa.gov/citations/19810049789
[research_andrianantara_ghazi_2025]: https://doi.org/10.2514/6.2025-1826
[research_andropov_guirik_2017]: https://doi.org/10.1109/icumt.2017.8255145
[research_annapauld_kidmandavids_1994]: https://ntrs.nasa.gov/citations/19950007831
[research_annaswamy_2005]: https://doi.org/10.21236/ada441542
[research_antonakis_2025]: https://doi.org/10.1007/s13272-025-00815-4
[research_antonakis_biannic_2024]: https://doi.org/10.2514/1.c037707
[research_anyoji_2019]: https://doi.org/10.15406/fmrij.2019.03.00055
[research_aono_anyoji_2018]: https://doi.org/10.2514/6.2018-1085
[research_application_of_2024_b]: https://doi.org/10.56726/irjmets49706
[research_applications_of_2004]: https://doi.org/10.5302/j.icros.2004.10.2.103
[research_aprovitola_dinuzzo_2021]: https://doi.org/10.3390/en14206615
[research_araujoestrada_windsor_2019]: https://doi.org/10.2514/6.2019-1934
[research_arenaasjr_nelsonrc_1989]: https://ntrs.nasa.gov/citations/19890061682
[research_arif_sasongko_2021]: https://doi.org/10.47355/avia.v3i1.39
[research_armstrong_1977]: https://doi.org/10.21236/adb029224
[research_armyscientificadvisorypanelwashingtondc_1977]: https://doi.org/10.21236/ada046087
[research_arogeti_ailon_2023]: https://doi.org/10.1109/icuas57906.2023.10155926
[research_aronstein_1996]: https://doi.org/10.4271/965539
[research_arshad_nawanjana_2022]: https://doi.org/10.1109/icmae56000.2022.9852511
[research_aryasomayajula_wang_2001]: https://doi.org/10.2514/2.2817
[research_asaro_vos_2025]: https://doi.org/10.2514/6.2025-0852
[research_asaro_vos_2026]: https://doi.org/10.2514/1.c038513
[research_asghari_tayefi_2026]: https://doi.org/10.1109/access.2026.3679992
[research_asher_hyland_1965]: https://doi.org/10.2514/6.1965-1141
[research_ashishkumargupta_paaswathanarayana_2023]: https://doi.org/10.61653/joast.v70i3.2018.402
[research_ashkenas_1965]: https://doi.org/10.2514/6.1965-314
[research_ashkenas_1965_b]: https://doi.org/10.21236/ad0627989
[research_ashkenas_1965_c]: https://doi.org/10.21236/ad0627659
[research_ashkenas_1982]: https://doi.org/10.2514/6.1982-1353
[research_ashkenas_1984]: https://doi.org/10.2514/3.44963
[research_ashkenasirvingl_klydedavidh_1989]: https://ntrs.nasa.gov/citations/19890011628
[research_ashraf_tabassum_2018]: https://doi.org/10.1109/i2ct.2018.8529563
[research_ashraf_vankampen_2020]: https://doi.org/10.2514/6.2020-1845
[research_ashton_2017]: https://doi.org/10.2514/6.2017-4281
[research_asouti_kontou_2023]: https://doi.org/10.3390/fluids8110292
[research_asztalos_salucci_2025]: https://doi.org/10.2514/6.2025-1673
[research_asztalos_salucci_2026]: https://doi.org/10.2514/6.2026-0477
[research_atay_bryant_2021]: https://doi.org/10.1115/1.4050998
[research_athayde_moutinho_2024]: https://doi.org/10.3390/act13060225
[research_atli_1988]: https://doi.org/10.2514/3.9905
[research_atmaca_stroosma_2025]: https://doi.org/10.2514/6.2025-0973
[research_atmaca_stroosma_2026]: https://doi.org/10.2514/6.2026-0550
[research_atmaca_vankampen_2025]: https://doi.org/10.2514/6.2025-0081
[research_atmaja_fajar_2023]: https://doi.org/10.1063/5.0181453
[research_atta_nayfeh_1978]: https://doi.org/10.2514/6.1978-1206
[research_atzhorn_stengel_1981]: https://doi.org/10.2514/6.1981-2331
[research_aulehia_1987]: https://doi.org/10.2514/6.1987-2612
[research_aulehla_kissel_1981]: https://doi.org/10.2514/6.1981-2614
[research_aulehla_kissel_1982]: https://doi.org/10.1108/eb035801
[research_aume_mills_1976]: https://doi.org/10.21236/ada028877
[research_automatic_landing_1964]: https://doi.org/10.1108/eb033884
[research_avirovic_brunelli_2023]: https://doi.org/10.2514/6.2023-3674
[research_avirovic_brunelli_2024]: https://doi.org/10.2514/6.2024-3998
[research_axelson_1975]: https://doi.org/10.2514/6.1975-996
[research_axelsonjohna_emersonhoracef_1949]: https://ntrs.nasa.gov/citations/20090022152
[research_ayoub_mclachlan_1988]: https://doi.org/10.1063/1.4738826
[research_ayouba_mclachlanbg_1987]: https://ntrs.nasa.gov/citations/19870055053
[research_azarmi_tavakolikakhki_2020]: https://doi.org/10.1109/iccc49264.2020.9257235
[research_azimov_allen_2017]: https://doi.org/10.1109/icuas.2017.7991515
[research_bach_mcnally_1988]: https://doi.org/10.1016/s1474-6670(17)54915-0
[research_bachelder_aponso_2020]: https://doi.org/10.4050/sm_2020_hq-915
[research_bachelder_aponso_2020_b]: https://doi.org/10.4050/sm_2020_hq-914
[research_bachelder_aponso_2023]: https://doi.org/10.4050/sm_2023_hq-1185
[research_bachelder_aponso_2023_b]: https://doi.org/10.4050/sm_2023_hq-1194
[research_bachmaier_anderson_2021]: https://doi.org/10.2514/6.2021-3215
[research_bachtiar_ardilla_2019]: https://doi.org/10.1109/elecsym.2019.8901596
[research_bacon_ostroff_2000]: https://doi.org/10.2514/6.2000-4565
[research_baconbartonj_carzoosusanw_1996]: https://ntrs.nasa.gov/citations/19960044512
[research_badole_choudhary_2022]: https://doi.org/10.1109/icetet-sip-2254415.2022.9791727
[research_badrya_baeder_2019]: https://doi.org/10.2514/6.2019-0638
[research_badrya_govindarajan_2018]: https://doi.org/10.2514/6.2018-2061
[research_badwan_tutunji_2018]: https://doi.org/10.1109/rem.2018.8421797
[research_bagade_krishnan_2015]: https://doi.org/10.12783/fae.2015.0401.03
[research_baggi_franco_2020]: https://doi.org/10.2514/6.2020-0841
[research_baggi_serrani_2022]: https://doi.org/10.1109/ccta49430.2022.9966141
[research_bagherzadeh_mohammadkarimi_2025]: https://doi.org/10.3390/mca30020041
[research_bahr_gandhi_2020]: https://doi.org/10.4050/f-0076-2020-16479
[research_bai_deng_2025]: https://doi.org/10.1109/aero63441.2025.11068451
[research_bailes_mittag_1975]: https://doi.org/10.21236/ada033827
[research_bailey_williams_2020]: https://doi.org/10.2514/6.2020-3087
[research_bajodah_mibar_2018]: https://doi.org/10.1109/med.2018.8442505
[research_baker_batavia_2016]: https://doi.org/10.4271/2024-01-3620
[research_bakerjr_1978]: https://doi.org/10.2514/6.1978-60
[research_balaji_mahesh_2025]: https://doi.org/10.1063/5.0241922
[research_balakrishnan_1972]: https://doi.org/10.1007/bf00932590
[research_balas_fialho_1997]: https://doi.org/10.1109/acc.1997.611768
[research_balas_garrard_1992]: https://doi.org/10.2514/6.1992-4329
[research_balas_packard_1996]: https://doi.org/10.2514/6.1996-3781
[research_balas_packard_1998]: https://doi.org/10.2514/2.4323
[research_balasubramanian_ahuja_2024]: https://doi.org/10.2514/6.2024-4144
[research_balatti_haddadkhodaparast_2021]: https://doi.org/10.1016/j.ast.2021.106805
[research_balcan_kucuker_2026]: https://doi.org/10.2514/6.2026-4236
[research_baldini_felicetti_2019]: https://doi.org/10.1109/systol.2019.8864785
[research_baldini_felicetti_2026]: https://doi.org/10.1109/icuas69441.2026.11598634
[research_ban_yamazaki_2018]: https://doi.org/10.2514/1.c034171
[research_banerjee_1988_b]: https://doi.org/10.2514/6.1988-2212
[research_banerjee_2019]: https://doi.org/10.2514/1.c034888
[research_banerjee_boyce_2017]: https://doi.org/10.2514/1.c033313
[research_banfield_kidd_2016]: https://doi.org/10.2514/6.2016-2029
[research_banksdanielw_1988]: https://ntrs.nasa.gov/citations/19890063987
[research_bansal_lavoie_2025]: https://doi.org/10.1007/s12650-024-01039-0
[research_bantscheff_breitsamter_2023]: https://doi.org/10.3390/aerospace10070581
[research_bao_li_2025]: https://doi.org/10.3390/machines13060525
[research_barbini_balfe_1970]: https://doi.org/10.21236/ad0869906
[research_barela_jackson_1988]: https://doi.org/10.21236/ada202151
[research_bargill_stengel_1986]: https://doi.org/10.2514/3.45276
[research_barker_balas_1999]: https://doi.org/10.2514/6.1999-4133
[research_barnes_1971]: https://doi.org/10.2514/3.59122
[research_barnhouse_hamid_2025]: https://doi.org/10.2514/6.2025-3253
[research_baron_jonckheere_1991]: https://doi.org/10.1080/00207179108934164
[research_barret_barret_1997]: https://doi.org/10.2514/6.1997-425
[research_bartlett_turner_1975]: https://doi.org/10.2514/6.1975-1206
[research_battipede_gili_2004]: https://doi.org/10.2514/6.2004-4823
[research_battiston_sharf_2017]: https://doi.org/10.1109/icuas.2017.7991468
[research_baughman_longeauay_2015]: https://doi.org/10.21236/ada616887
[research_baumann_galor_1992]: https://doi.org/10.4271/921015
[research_baxter_2013]: https://doi.org/10.21236/ada613350
[research_bay_kara_2026]: https://doi.org/10.17798/bitlisfen.1847172
[research_baylen_walton_1967]: https://doi.org/10.2307/3816996
[research_bayoglu_nalci_2016]: https://doi.org/10.2514/6.2016-3856
[research_bazuhair_2018]: https://doi.org/10.3103/s106879981802006x
[research_bbvl_singh_2016]: https://doi.org/10.1108/ijius-10-2015-0012
[research_beall_1986]: https://doi.org/10.2514/6.1986-488
[research_beardbb_foleywh_1983]: https://ntrs.nasa.gov/citations/19830066784
[research_beasleygp_1984]: https://ntrs.nasa.gov/citations/19840012499
[research_beaufrere_1986]: https://doi.org/10.2514/6.1986-2203
[research_bechelder_bjorkman_2025]: https://doi.org/10.4050/sm_handling_2025-5299
[research_beck_cord_1995]: https://doi.org/10.2514/6.1995-3448
[research_beemanrr_1972]: https://ntrs.nasa.gov/citations/19760006024
[research_been_kang_2018]: https://doi.org/10.1007/s42405-018-0097-0
[research_begum_rao_2020]: https://doi.org/10.1504/ijaac.2020.108274
[research_behm_1973]: https://doi.org/10.2514/6.1973-888
[research_bellamri_benineneto_2024]: https://doi.org/10.1109/med61351.2024.10566121
[research_bellmandr_kierda_1974]: https://ntrs.nasa.gov/citations/19750032849
[research_belmont_1983]: https://doi.org/10.21236/ada133274
[research_benedikt_1953]: https://doi.org/10.2514/8.2809
[research_benjaminmsimmons_2023]: https://ntrs.nasa.gov/citations/20230004001
[research_bennett_1984]: https://doi.org/10.2514/6.1984-2500
[research_bennett_baras_1985]: https://doi.org/10.1109/cdc.1985.268496
[research_bennett_chapman_2024]: https://doi.org/10.2514/6.2024-1372
[research_bennett_lawson_2017]: https://doi.org/10.2514/6.2017-3652
[research_bennythompson_gunasekaran_2021]: https://doi.org/10.1088/1742-6596/2054/1/012005
[research_benyamen_chowdhury_2024]: https://doi.org/10.1115/1.4065804
[research_benyamen_keshmiri_2022]: https://doi.org/10.1109/icuas54217.2022.9836206
[research_benyamen_mays_2023]: https://doi.org/10.1109/icuas57906.2023.10156586
[research_bercovici_foias_1990]: https://doi.org/10.23919/acc.1990.4791154
[research_berens_2019]: https://doi.org/10.2514/6.2019-1685
[research_berens_biezad_1988]: https://doi.org/10.23919/acc.1988.4790100
[research_berg_1991]: https://doi.org/10.2514/6.1991-2630
[research_berger_christensen_2025]: https://doi.org/10.4050/sm_handling_2025-5294
[research_berger_horn_2019]: https://doi.org/10.4050/f-0075-2019-14595
[research_berger_miller_2016]: https://doi.org/10.4050/f-0072-2016-11452
[research_bergman_1979]: https://doi.org/10.2514/6.1979-1812
[research_bergmann_denzel_2021]: https://doi.org/10.3390/aerospace8020043
[research_bermantheodore_1947]: https://ntrs.nasa.gov/citations/20050019357
[research_bermantheodore_1949]: https://ntrs.nasa.gov/citations/20090026525
[research_bermantheodore_pumphreynormane_1950]: https://ntrs.nasa.gov/citations/20050080688
[research_bernal_yu_2015]: https://doi.org/10.2514/6.2015-0038
[research_bernardos_richez_2019]: https://doi.org/10.2514/6.2019-2922
[research_bernhard_adamy_2017]: https://doi.org/10.23919/acc.2017.7963091
[research_bernstein_2000]: https://doi.org/10.21236/ada382981
[research_berra_campbell_2017]: https://doi.org/10.2514/6.2017-3649
[research_berry_powers_1970]: https://doi.org/10.2514/6.1970-566
[research_bertrandnoel_bignaletcazalet_2022]: https://doi.org/10.1016/j.jsse.2021.12.002
[research_betin_2026]: https://doi.org/10.3849/aimt.02050
[research_beyer_kuzolap_2018]: https://doi.org/10.2514/6.2018-3257
[research_beyers_1986]: https://doi.org/10.2514/3.45286
[research_beyers_ericsson_2002]: https://doi.org/10.2514/2.2989
[research_bezdek_1995]: https://doi.org/10.2514/6.1995-3421
[research_bezerra_santos_2022]: https://doi.org/10.1109/lcsys.2021.3110490
[research_bhandari_bhandari_2026]: https://doi.org/10.2514/1.c038411
[research_bhujel_pang_2026]: https://doi.org/10.2514/6.2026-4760
[research_bhusal_subbarao_2022]: https://doi.org/10.2514/1.g006257
[research_bianchi_epicoco_2024]: https://doi.org/10.3390/drones8120716
[research_biber_2015]: https://doi.org/10.2514/6.2015-0031
[research_bidar_he_2024]: https://doi.org/10.2514/6.2024-1231
[research_bidinotto_moura_2021]: https://doi.org/10.1017/aer.2021.82
[research_bielatralphp_wileyharlethg_1959]: https://ntrs.nasa.gov/citations/19980227088
[research_biezad_schmidt_1984]: https://doi.org/10.2514/6.1984-1899
[research_biezad_schmidt_1985]: https://doi.org/10.2514/3.20053
[research_bigler_1986]: https://doi.org/10.2514/6.1986-9729
[research_bihrle_barnhart_1982]: https://doi.org/10.2514/3.44789
[research_bihrle_jr_1980]: https://doi.org/10.21236/ada082335
[research_bihrlejr_1969]: https://doi.org/10.2514/6.1969-894
[research_bihrlejr_1970]: https://doi.org/10.2514/6.1970-946
[research_bihrlewjr_bowmanjsjr_1980]: https://ntrs.nasa.gov/citations/19800042785
[research_billingsley_1976]: https://doi.org/10.21236/ada024445
[research_bing_feng_2015]: https://doi.org/10.1109/chicc.2015.7260672
[research_binz_islam_2019]: https://doi.org/10.1177/1756829319861370
[research_binz_moormann_2020]: https://doi.org/10.1177/1756829320961925
[research_bird_1970]: https://doi.org/10.21236/ad0706919
[research_bischoff_1983]: https://doi.org/10.2514/3.44899
[research_bischoff_duffy_1974]: https://doi.org/10.2514/3.60378
[research_bischoff_palmer_1982]: https://doi.org/10.2514/6.1982-1610
[research_bischoff_palmer_1983]: https://doi.org/10.21236/ada327418
[research_bishop_1961]: https://doi.org/10.1017/s0368393100075957
[research_bissonnette_bramesfeld_2015]: https://doi.org/10.2514/6.2015-1031
[research_black_1968_b]: https://doi.org/10.2514/6.1968-361
[research_black_andjelic_2024]: https://doi.org/10.1109/tmrb.2024.3349612
[research_black_moorhouse_1979]: https://doi.org/10.21236/ada085085
[research_blanken_pausder_1994]: https://doi.org/10.4050/jahs.39.3.24
[research_bliamis_zacharakis_2021]: https://doi.org/10.1088/1757-899x/1024/1/012039
[research_bliss_1980]: https://doi.org/10.21236/ada093301
[research_bloy_lea_1995]: https://doi.org/10.2514/3.46741
[research_bobrowski_barnewitz_2016]: https://doi.org/10.2514/6.2016-3831
[research_bodson_2000]: https://doi.org/10.21236/ada381657
[research_bodson_groszkiewicz_1997]: https://doi.org/10.1109/87.556026
[research_bodson_pohlchuck_1996]: https://doi.org/10.2514/6.1996-3772
[research_bodson_pohlchuck_1997]: https://doi.org/10.2514/6.1997-3604
[research_bodson_pohlchuck_1998]: https://doi.org/10.2514/2.4283
[research_bodur_hancioglu_2025]: https://doi.org/10.1109/codit66093.2025.11321820
[research_bodur_ucun_2023]: https://doi.org/10.1109/rast57548.2023.10197950
[research_boeingvertolcophiladelphiapa_1983]: https://doi.org/10.21236/ada134323
[research_bolling_durham_1997]: https://doi.org/10.2514/6.1997-3775
[research_bolting_stolle_2017]: https://doi.org/10.1016/j.ifacol.2017.08.1471
[research_bombencraigr_smolkajamesw_2006]: https://ntrs.nasa.gov/citations/20060049153
[research_bond_1936]: https://doi.org/10.1038/1371031b0
[research_bondreuben_packardbarbarab_1961]: https://ntrs.nasa.gov/citations/20040006386
[research_boothe_1971]: https://doi.org/10.2514/6.1971-771
[research_boothe_chen_1974]: https://doi.org/10.21236/ad0782218
[research_booz_1988]: https://doi.org/10.2514/6.1988-4363
[research_boppe_martorella_1992]: https://doi.org/10.1115/92-gt-362
[research_bordei_halanay_2025]: https://doi.org/10.3390/axioms14070519
[research_borer_cox_2019]: https://doi.org/10.2514/6.2019-2855
[research_borer_reynolds_2024]: https://doi.org/10.2514/6.2024-4133
[research_borisova_silantiev_2022]: https://doi.org/10.53954/9785604788967_30
[research_bosch_kuehl_1976]: https://doi.org/10.2514/6.1976-1932
[research_bosch_kuehl_1977]: https://doi.org/10.2514/3.58880
[research_boschetti_cardenas_2004]: https://doi.org/10.2514/6.2004-4969
[research_boschetti_cardenas_2020]: https://doi.org/10.2514/1.c035853
[research_boschetti_neves_2022]: https://doi.org/10.2514/1.c036721
[research_boskovic_mehra_1999]: https://doi.org/10.2514/6.1999-4041
[research_boskovic_mehra_2000]: https://doi.org/10.2514/2.4617
[research_boskovic_mehra_2001]: https://doi.org/10.1109/acc.2001.945871
[research_boskovic_mehra_2002]: https://doi.org/10.2514/2.4938
[research_boskovic_saimingli]: https://doi.org/10.1109/plans.2000.838323
[research_bosnyakov_wolkov_2024]: https://doi.org/10.53954/9785604990148_41
[research_bosworth_cox_1989]: https://doi.org/10.2514/6.1989-3428
[research_bosworthjohnt_2008]: https://ntrs.nasa.gov/citations/20080034509
[research_bosworthjohnt_2010]: https://ntrs.nasa.gov/citations/20110008197
[research_bosworthjohnt_stachowiaksusanj_2005]: https://ntrs.nasa.gov/citations/20050060997
[research_bosworthjohnt_stolikerpc_1996]: https://ntrs.nasa.gov/citations/19960029101
[research_bouaiss_mechgoug_2023]: https://doi.org/10.1002/acs.3659
[research_bousson_paglione_2001]: https://doi.org/10.4271/2001-01-2982
[research_bouzid_bestaoui_2018]: https://doi.org/10.1109/icuas.2018.8453367
[research_bowes_miller_1976]: https://doi.org/10.21236/ada026963
[research_bowlus_multhopp_1997]: https://doi.org/10.2514/6.1997-3830
[research_bowmanjamessjr_1957]: https://ntrs.nasa.gov/citations/20050028487
[research_boyden_1970]: https://doi.org/10.2514/6.1970-540
[research_boyden_1971]: https://doi.org/10.2514/3.59135
[research_bradshaw_huber_1982]: https://doi.org/10.2514/6.1982-1351
[research_bramesfeld_prinster_2015]: https://doi.org/10.1139/juvs-2014-0018
[research_brandeau_1978]: https://doi.org/10.2514/6.1978-1460
[research_brandin_1990]: https://doi.org/10.1016/s1474-6670(17)52742-1
[research_brandon_morelli_2016]: https://doi.org/10.2514/1.c033133
[research_brandonjaym_brownphilipw_1987]: https://ntrs.nasa.gov/citations/19870017489
[research_brandt_mclaughlin_2019]: https://doi.org/10.2514/6.2019-0283
[research_braun_holzapfel_2025]: https://doi.org/10.2514/6.2025-2809
[research_brauser_1982]: https://doi.org/10.1016/s1474-6670(17)62884-2
[research_breda_andoga_2024]: https://doi.org/10.23919/ntca60572.2024.10517831
[research_breitung_2001]: https://doi.org/10.1002/stc.4300080209
[research_breneman_lower_1992]: https://doi.org/10.2514/6.1992-4083
[research_breuhaus_1979]: https://doi.org/10.2514/3.58581
[research_breul_1963]: https://doi.org/10.2514/6.1963-1015
[research_brewergeraldw_1946]: https://ntrs.nasa.gov/citations/20050031173
[research_brimelow_1970]: https://doi.org/10.21236/ad0874880
[research_brinker_wise_1996]: https://doi.org/10.2514/3.21782
[research_brinker_wise_1998]: https://doi.org/10.2514/6.1998-4107
[research_brinker_wise_1999]: https://doi.org/10.2514/6.1999-4040
[research_brinker_wise_2000]: https://doi.org/10.2514/6.2000-3941
[research_brinker_wise_2001]: https://doi.org/10.2514/2.4826
[research_brody_fagley_2024]: https://doi.org/10.2514/6.2024-85438
[research_bronz_hattenberger_2016]: https://doi.org/10.2514/6.2016-3979
[research_brown_1993]: https://doi.org/10.2514/3.46331
[research_brown_2025]: https://doi.org/10.65391/r3083
[research_brown_duhon_1965]: https://doi.org/10.2514/6.1965-209
[research_brown_hoover_2026]: https://doi.org/10.1109/aero66936.2026.11520150
[research_brownjr_1970]: https://doi.org/10.2514/6.1970-947
[research_brudnak_2016]: https://doi.org/10.4271/2024-01-3607
[research_brudnak_2020]: https://doi.org/10.4271/2024-01-3842
[research_brueckner_patinostudencki_2023]: https://doi.org/10.1109/itsc57777.2023.10422699
[research_brunelli_avirovic_2026]: https://doi.org/10.1007/s10494-025-00727-7
[research_brunsjamese_smithcf_1992]: https://ntrs.nasa.gov/citations/19920071388
[research_bryson_1954]: https://doi.org/10.2514/8.3135
[research_bryson_desai_1969]: https://doi.org/10.2514/3.44093
[research_brysonjr_desai_1968]: https://doi.org/10.2514/6.1968-877
[research_bucci_sullivan_1997]: https://doi.org/10.2514/6.1997-2297
[research_buffington_1999]: https://doi.org/10.21236/ada375713
[research_buffington_1999_b]: https://doi.org/10.21236/ada374954
[research_buffington_buffington_1997]: https://doi.org/10.2514/6.1997-3605
[research_buffington_chandler_1999]: https://doi.org/10.1002/(sici)1099-1239(19991215)9:14<1033::aid-rnc451>3.0.co;2-#
[research_buffington_sparks_1993]: https://doi.org/10.23919/acc.1993.4792886
[research_buffington_sparks_1994]: https://doi.org/10.1016/0005-1098(94)90093-0
[research_buffington_sparks_1998]: https://doi.org/10.2514/6.1998-4248
[research_buffington_sparks_1998_b]: https://doi.org/10.1109/acc.1998.703591
[research_bugliariarmenio_cortigiani_2024]: https://doi.org/10.4050/f-0080-2024-1064
[research_bui_2016]: https://doi.org/10.2514/6.2016-3720
[research_bui_2018]: https://doi.org/10.2514/6.2018-3808
[research_bukov_1989]: https://doi.org/10.1016/s1474-6670(17)53011-6
[research_bunge_munerasavino_2015]: https://doi.org/10.2514/6.2015-3225
[research_burchett_2023]: https://doi.org/10.21236/ad1214017
[research_burchett_bryson_2025]: https://doi.org/10.2514/6.2025-1262
[research_burke_2015]: https://doi.org/10.21236/ad1019501
[research_burken_lu_1999]: https://doi.org/10.2514/6.1999-4134
[research_burken_lu_2001]: https://doi.org/10.2514/2.4769
[research_burkenjohnj_2005]: https://ntrs.nasa.gov/citations/20090008513
[research_burkenjohnj_larsonrichardr_2009]: https://ntrs.nasa.gov/citations/20090015898
[research_burkenjohnj_nguyennhant_2010]: https://ntrs.nasa.gov/citations/20100017255
[research_burkenjohnj_williamshayespeggy_2006]: https://ntrs.nasa.gov/citations/20060023991
[research_burksmjr_wilsoncfjr_1975]: https://ntrs.nasa.gov/citations/19790022002
[research_burnashev_zbrutsky_2019]: https://doi.org/10.1109/apuavd47061.2019.8943872
[research_burnell_morrison_1973]: https://doi.org/10.21236/ad0771030
[research_burner_liu_2000]: https://doi.org/10.2514/6.2000-2386
[research_burris_1969]: https://doi.org/10.2514/6.1969-767
[research_burris_bender_1969]: https://doi.org/10.21236/ad0865310
[research_burrows_allaire_2019]: https://doi.org/10.2514/6.2019-3663
[research_burton_bischoff_1976]: https://doi.org/10.2514/6.1976-894
[research_burton_kneelandjr_1981]: https://doi.org/10.2514/6.1981-2465
[research_buschbachermark_bosworthjohn_2006]: https://ntrs.nasa.gov/citations/20060056077
[research_bushnell_1990]: https://doi.org/10.2514/6.1990-1596
[research_butler_1976]: https://doi.org/10.21236/ada023690
[research_byers_bittner_1988]: https://doi.org/10.1177/154193128803201704
[research_byrdsong_brooks_1980]: https://ntrs.nasa.gov/citations/19830002872
[research_byrdsong_brooks_1983]: https://ntrs.nasa.gov/citations/19830020905
[research_byrdsong_hallissy_1979]: https://ntrs.nasa.gov/citations/19820007202
[research_caap_elemeland_1986]: https://doi.org/10.2514/6.1986-1771
[research_caddy_arnold_1988]: https://doi.org/10.1115/88-gt-303
[research_cai_fan_2026]: https://doi.org/10.2514/1.c038462
[research_cakici_yoruk_2022]: https://doi.org/10.5162/ettc2022/9.3
[research_cakiroglu_vankampen_2018]: https://doi.org/10.2514/6.2018-1128
[research_calarese_1981]: https://doi.org/10.2514/6.1981-359
[research_calise_2000]: https://doi.org/10.2514/6.2000-3940
[research_calise_2001]: https://doi.org/10.21236/ada389515
[research_calise_lee_1998]: https://doi.org/10.2514/6.1998-4108
[research_calise_lee_2000]: https://doi.org/10.2514/6.2000-4551
[research_calise_lee_2001]: https://doi.org/10.2514/2.4825
[research_calise_rysdyk_1997]: https://doi.org/10.2514/6.1997-3758
[research_callaghan_kunz_2019]: https://doi.org/10.2514/6.2019-3548
[research_callaghan_kunz_2021]: https://doi.org/10.2514/1.g004748
[research_cameron_memon_2021]: https://doi.org/10.2514/6.2021-0592
[research_cameron_thomson_2003]: https://doi.org/10.1017/s0001924000134013
[research_campbell_1959]: https://doi.org/10.1108/eb033068
[research_campbell_1973]: https://doi.org/10.2514/6.1973-821
[research_campbell_1974]: https://doi.org/10.2514/3.60402
[research_campbell_abramovitz_1975]: https://doi.org/10.2514/6.1975-1028
[research_campbell_mulani_2026]: https://doi.org/10.2514/6.2026-0770
[research_campos_1989]: https://doi.org/10.2514/6.1989-2041
[research_campos_marques_2021]: https://doi.org/10.3390/aerospace8030077
[research_canin_2019]: https://doi.org/10.2514/6.2019-3227
[research_cantarelo_rolland_2016]: https://doi.org/10.1109/smc.2016.7844857
[research_cao_chen_2026]: https://doi.org/10.1016/j.neucom.2025.132460
[research_cao_lu_2024]: https://doi.org/10.3390/biomimetics9050263
[research_cao_qi_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000803
[research_cao_tang_2017]: https://doi.org/10.1631/fitee.1601363
[research_cao_zhang_2022]: https://doi.org/10.1109/tim.2022.3173612
[research_capello_ferrero_2019]: https://doi.org/10.2514/6.2019-4311
[research_capone_1979]: https://doi.org/10.2514/6.1979-1810
[research_capone_mason_1986]: https://doi.org/10.2514/6.1986-1779
[research_caradima_wang_2000]: https://doi.org/10.1115/imece2000-2432
[research_carinevioladsouza_drbasawaraj_2015]: https://doi.org/10.17577/ijertv4is060764
[research_carino_abaunza_2015]: https://doi.org/10.1109/icuas.2015.7152367
[research_carlson_1958]: https://doi.org/10.4050/jahs.3.11
[research_carlson_mabli_1965]: https://doi.org/10.2514/6.1965-740
[research_carpenter_jenny_1964]: https://doi.org/10.2514/6.1964-286
[research_carr_lambrecht_2003]: https://doi.org/10.21236/ada424895
[research_carter_1976]: https://doi.org/10.21236/ada025408
[research_carter_1988]: https://doi.org/10.2514/6.1988-2045
[research_carter_keeter_2024]: https://doi.org/10.2514/6.2024-0570
[research_casadei_konozsy_2019]: https://doi.org/10.1016/j.ast.2019.05.034
[research_caseyldenham_mayureshpatil_2022]: https://ntrs.nasa.gov/citations/20220013129
[research_castillozuniga_souza_2020]: https://doi.org/10.1016/j.ymssp.2020.106900
[research_catalano_daniello_2025]: https://doi.org/10.2514/1.c038170
[research_catalano_derosa_2024]: https://doi.org/10.2514/6.2024-1347
[research_catani_deamicis_1982]: https://doi.org/10.2514/6.1982-319
[research_cavalcanti_uehara_2026]: https://doi.org/10.2514/1.c038528
[research_cavallo_dash_2000]: https://doi.org/10.2514/6.2000-4407
[research_cavanaugh_2003]: https://doi.org/10.2514/6.2003-5613
[research_caverly_forbes_2018]: https://doi.org/10.2514/6.2018-0601
[research_caverly_girard_2016]: https://doi.org/10.1016/j.ifacol.2016.09.058
[research_cebeci_stewartson_1983]: https://doi.org/10.21236/ada136257
[research_cecen_2021]: https://doi.org/10.1504/ijsa.2021.117241
[research_chai_crisafulli_1995]: https://doi.org/10.2514/6.1995-3882
[research_chaikalis_khorrami_2020]: https://doi.org/10.1109/icuas48674.2020.9213920
[research_chakraborty_mishra_2021]: https://doi.org/10.2514/1.c036101
[research_chakravarty_1987]: https://doi.org/10.2514/6.1987-2257
[research_chakravarty_mahanta_2015]: https://doi.org/10.1002/rnc.3392
[research_chalk_1964]: https://doi.org/10.2514/3.43604
[research_chalk_neal_1969]: https://doi.org/10.21236/ad0860856
[research_chamberlain_1968]: https://doi.org/10.2514/6.1968-395
[research_chamberlin_miller_1979]: https://doi.org/10.2514/6.1979-1861
[research_chambers_hall_2004]: https://doi.org/10.2514/1.4470
[research_chamitoff_1994]: https://doi.org/10.1016/s1474-6670(17)45823-x
[research_champigny_1984]: https://doi.org/10.2514/6.1984-2176
[research_chancevoughtcorpdallastx_1979]: https://doi.org/10.21236/ada358711
[research_chand_chiu_1991]: https://doi.org/10.2514/6.1991-2799
[research_chandan_nagaraja_2023]: https://doi.org/10.1109/icaect57570.2023.10118222
[research_chandra_2020]: https://doi.org/10.1007/s42405-019-00247-5
[research_chandra_gandhi_2025]: https://doi.org/10.23919/ecc65951.2025.11187289
[research_chang_guo_2022]: https://doi.org/10.1016/j.ifacol.2022.07.214
[research_chao_ying_2017]: https://doi.org/10.23919/chicc.2017.8028075
[research_chao_yingmin_2015]: https://doi.org/10.1109/chicc.2015.7260126
[research_chau_piotrowski_2026]: https://doi.org/10.2514/1.c038646
[research_chau_zingg_2017]: https://doi.org/10.2514/6.2017-3258
[research_chau_zingg_2022]: https://doi.org/10.2514/1.c036389
[research_chaudhuri_jasa_2018]: https://doi.org/10.2514/6.2018-1658
[research_chaudhuri_praharaj_1971]: https://doi.org/10.2514/6.1971-626
[research_chavez_vogel_2003]: https://doi.org/10.1115/imece2003-42864
[research_chawla_vandalsem_1992]: https://doi.org/10.2514/6.1992-4254
[research_che_lian_2021]: https://doi.org/10.1049/icp.2021.0285
[research_cheatham_gridley_1991]: https://doi.org/10.1115/91-gt-160
[research_chedrik_ishmuratov_2004]: https://doi.org/10.2514/6.2004-4642
[research_chen_1992]: https://doi.org/10.23919/acc.1992.4792723
[research_chen_1993]: https://doi.org/10.23919/acc.1993.4793489
[research_chen_2021_b]: https://doi.org/10.1117/12.2611407
[research_chen_2024]: https://doi.org/10.1016/j.iot.2024.101319
[research_chen_2026]: https://doi.org/10.54097/q4hfj028
[research_chen_gray_2026]: https://doi.org/10.2514/6.2026-1489
[research_chen_huang_2026]: https://doi.org/10.2514/6.2026-0297
[research_chen_ji_2017]: https://doi.org/10.4050/sm_2017_hq-2997
[research_chen_kopsaftopoulos_2019]: https://doi.org/10.3390/s19020275
[research_chen_li_2025]: https://doi.org/10.1109/icacrs67045.2025.11324281
[research_chen_li_2026]: https://doi.org/10.3390/aerospace13030221
[research_chen_liu_2020]: https://doi.org/10.1109/access.2020.3015857
[research_chen_liu_2021]: https://doi.org/10.2514/1.g005714
[research_chen_ma_2022]: https://doi.org/10.1109/tac.2021.3059155
[research_chen_tang_2024]: https://doi.org/10.1002/acs.3827
[research_chen_wang_2017]: https://doi.org/10.23919/chicc.2017.8028514
[research_chen_xiao_2015]: https://doi.org/10.1109/cyber.2015.7288158
[research_chen_xie_2024]: https://doi.org/10.1088/1742-6596/2882/1/012003
[research_chen_yang_2022]: https://doi.org/10.3390/app12084092
[research_chen_yue_2015]: https://doi.org/10.5028/jatm.v7i2.416
[research_chen_zhang_2017]: https://doi.org/10.1177/1729881416678141
[research_chen_zhao_2017]: https://doi.org/10.1109/ccdc.2017.7979409
[research_cheney_1988]: https://doi.org/10.2514/6.1988-2125
[research_cheng_cai_2019]: https://doi.org/10.1016/j.ifacol.2019.12.380
[research_cheng_pei_2020]: https://doi.org/10.1109/icuas48674.2020.9214014
[research_cheng_pei_2021]: https://doi.org/10.1109/icuas51884.2021.9476758
[research_cheng_xin_2019]: https://doi.org/10.1109/icus48101.2019.8995929
[research_cheng_zhang_2020]: https://doi.org/10.1109/ccdc49329.2020.9164681
[research_chernenko_burnashev_2022]: https://doi.org/10.20535/0203-3771422021268461
[research_chetty_henschel_1987]: https://doi.org/10.2514/6.1987-2451
[research_chetty_lakshmi_1991]: https://doi.org/10.1016/s1474-6670(17)54311-6
[research_chetty_raol_1992]: https://doi.org/10.2514/6.1992-4423
[research_chevalier_burke_1972]: https://doi.org/10.2514/6.1972-125
[research_chhetri_jetawatthana_2026]: https://doi.org/10.1142/s230138502830003x
[research_chinalexanderw_herreraclaudiay_2015]: https://ntrs.nasa.gov/citations/20150002077
[research_chinalexanderw_herreraclaudiay_2015_b]: https://ntrs.nasa.gov/citations/20150000840
[research_chitsaz_siddiqui_2021]: https://doi.org/10.1016/j.expthermflusci.2020.110286
[research_cho_cho_1995]: https://doi.org/10.1007/bf02953616
[research_cho_kim_2018]: https://doi.org/10.1103/physrevfluids.3.113901
[research_chodnicki_bartnik_2018]: https://doi.org/10.1108/aeat-01-2018-0039
[research_choi_kim_2023]: https://doi.org/10.3390/drones7070418
[research_chowdhury_keshmiri_2021]: https://doi.org/10.1109/icuas51884.2021.9476811
[research_chowdhury_keshmiri_2024]: https://doi.org/10.1109/icuas60882.2024.10556883
[research_chowhan_arya_2019]: https://doi.org/10.1002/j.2334-5837.2019.00697.x
[research_christopherlblanken_matthewswhalley_1993]: https://ntrs.nasa.gov/citations/19940008821
[research_chu_brysonjr_1987]: https://doi.org/10.2514/6.1987-632
[research_chu_dacosta_2001]: https://doi.org/10.2514/6.2001-4219
[research_chuan_feng_2016]: https://doi.org/10.2514/6.2016-0513
[research_chudoba_cook_2003]: https://doi.org/10.2514/6.2003-5386
[research_chung_tuan_2021]: https://doi.org/10.1109/piers53385.2021.9694999
[research_chunlianglin_thongshinghwang_2004]: https://doi.org/10.1109/isie.2004.1571788
[research_chunrong_yunhong_2025]: https://doi.org/10.1007/s40435-025-01869-2
[research_cieslak_2021]: https://doi.org/10.37105/sd.110
[research_ciliberti_nicolosi_2025]: https://doi.org/10.1186/s42774-024-00189-x
[research_ciobaca_dandois_2017]: https://doi.org/10.2514/6.2017-3245
[research_clark_1964]: https://doi.org/10.2514/6.1964-618
[research_clark_1982]: https://doi.org/10.2514/3.57365
[research_clark_1983]: https://doi.org/10.1117/12.933974
[research_clarke_hwang_2020]: https://doi.org/10.2514/6.2020-0136
[research_clarke_roskam_1982]: https://doi.org/10.2514/6.1982-1312
[research_cleary_1969]: https://doi.org/10.2514/6.1969-187
[research_clementskeith_2016]: https://ntrs.nasa.gov/citations/20160013364
[research_clementskeith_2017]: https://ntrs.nasa.gov/citations/20170001826
[research_clevensonsa_wildmayerejr_1953]: https://ntrs.nasa.gov/citations/20090014039
[research_cliff_lutze_1972]: https://doi.org/10.2514/3.44339
[research_coalson_1968]: https://doi.org/10.21236/ad0833750
[research_coalson_1982]: https://doi.org/10.1115/82-gt-183
[research_coalson_csavina_1975]: https://doi.org/10.2514/6.1975-1175
[research_coban_2020]: https://doi.org/10.1108/aeat-08-2019-0171
[research_coban_oktay_2018]: https://doi.org/10.30518/jav.461365
[research_coder_ortizmelendez_2018]: https://doi.org/10.2514/6.2018-2846
[research_coepljr_grahamab_1975]: https://ntrs.nasa.gov/citations/19750022117
[research_cohenrobertj_1951]: https://ntrs.nasa.gov/citations/19930086608
[research_cohn_dusa_1985]: https://doi.org/10.2514/6.1985-1466
[research_colgren_loschke_2008]: https://doi.org/10.2514/1.32083
[research_colgren_martin_2000]: https://doi.org/10.2514/6.2000-4447
[research_collins_1982]: https://doi.org/10.2514/3.44799
[research_collins_zhao_2004]: https://doi.org/10.23919/acc.2004.1384479
[research_collinsjr_2005]: https://doi.org/10.21236/ada438337
[research_collison_harley_2017]: https://doi.org/10.1115/gt2017-63294
[research_combined_flight_1974]: https://doi.org/10.1108/eb035139
[research_comer_atkinson_2026]: https://doi.org/10.2514/6.2026-2063
[research_comer_bhandari_2024]: https://doi.org/10.2514/6.2024-2644
[research_comer_chakraborty_2026]: https://doi.org/10.4050/f-0082-2026-0189
[research_comer_chakraborty_2026_b]: https://doi.org/10.2514/1.g009060
[research_cong_hu_2023]: https://doi.org/10.3390/aerospace10030241
[research_cong_hu_2023_b]: https://doi.org/10.2139/ssrn.4677641
[research_connolly_csank_2017]: https://doi.org/10.2514/6.2017-4787
[research_connollyjosephw_csankjeffreyt_2016]: https://ntrs.nasa.gov/citations/20170000940
[research_connors_swaim_1968]: https://doi.org/10.2514/6.1968-59
[research_cook_hauser_2018]: https://doi.org/10.23919/acc.2018.8431242
[research_cooksey_dillenschneider_1964]: https://doi.org/10.2514/6.1964-1108
[research_coopmans_podhradsky_2015]: https://doi.org/10.1109/red-uas.2015.7440998
[research_coopmans_podhradsky_2016]: https://doi.org/10.1109/icuas.2016.7502607
[research_coopmans_slack_2022]: https://doi.org/10.1109/icuas54217.2022.9836128
[research_coppin_birch_2018]: https://doi.org/10.2514/1.c033988
[research_corliss_1982]: https://doi.org/10.4050/sm_handling_1982-1262
[research_cornelius_lucius_1993]: https://doi.org/10.2514/6.1993-3261
[research_cornelius_lucius_1993_b]: https://doi.org/10.2514/6.1993-2959
[research_cornelius_lucius_1994]: https://doi.org/10.2514/3.46566
[research_cornelius_lucius_1995]: https://doi.org/10.2514/3.23861
[research_coronasanchez_rodriguezcortes_2015]: https://doi.org/10.1109/icuas.2015.7152381
[research_corraro_delellis_2003]: https://doi.org/10.23919/ecc.2003.7085137
[research_correa_sengupta_1981]: https://doi.org/10.2514/3.44704
[research_cosentinogaryb_2007]: https://ntrs.nasa.gov/citations/20080007530
[research_cosentinogaryb_2007_b]: https://ntrs.nasa.gov/citations/20080020277
[research_cosentinogaryb_2008]: https://ntrs.nasa.gov/citations/20080022273
[research_cosenza_vos_2017]: https://doi.org/10.2514/6.2017-3763
[research_costes_1988]: https://doi.org/10.2514/6.1988-4160
[research_costigan_calico_1989]: https://doi.org/10.2514/6.1989-17
[research_cote_2015]: https://doi.org/10.21236/ad1019500
[research_cotting_burken_2001]: https://doi.org/10.2514/6.2001-4379
[research_cotton_1974]: https://doi.org/10.21236/ada000894
[research_coulter_marquart_1982]: https://doi.org/10.2514/6.1982-596
[research_courtin_hansman_2020]: https://doi.org/10.2514/6.2020-0977
[research_cox_1957]: https://doi.org/10.1017/s0022112057000245
[research_cox_siddall_1949]: https://doi.org/10.1108/eb031772
[research_coxdavide_cunninghamkevin_2012]: https://ntrs.nasa.gov/citations/20120014564
[research_coxtimothyh_cottingmchristopher_2005]: https://ntrs.nasa.gov/citations/20050166903
[research_coxtimothyh_marshallalisa_2000]: https://ntrs.nasa.gov/citations/20000052206
[research_craig_1965]: https://doi.org/10.21236/ad0628087
[research_craig_heffley_1972]: https://doi.org/10.2514/6.1972-987
[research_craig_heffley_1973]: https://doi.org/10.2514/3.60252
[research_cramer_1995]: https://doi.org/10.2514/6.1995-3879
[research_cranedf_1983]: https://ntrs.nasa.gov/citations/19830055004
[research_crespoluisg_matsutanimegumi_2010]: https://ntrs.nasa.gov/citations/20100031112
[research_crites_rueger_1992]: https://doi.org/10.2514/6.1992-3983
[research_crombie_moorhouse_1980]: https://doi.org/10.21236/ada088629
[research_croom_kenney_2000]: https://doi.org/10.2514/6.2000-3913
[research_crother_gabelman_1973]: https://doi.org/10.21236/ada004416
[research_crowther_wood_1993]: https://doi.org/10.2514/6.1993-3406
[research_csavina_1976]: https://doi.org/10.2514/6.1976-649
[research_cui_bai_2024]: https://doi.org/10.1109/ifeea64237.2024.10878638
[research_cui_feng_2019]: https://doi.org/10.2514/1.c035047
[research_cui_zuo_2021]: https://doi.org/10.1109/tsmc.2019.2924357
[research_cumming_kramer_1966]: https://doi.org/10.2514/6.1966-776
[research_cummings_liersch_2018]: https://doi.org/10.2514/1.c033808
[research_cunis_leth_2018]: https://doi.org/10.1109/icuas.2018.8453340
[research_cunningham_cox_2011]: https://ntrs.nasa.gov/citations/20110014794
[research_curry_matthews_1965]: https://doi.org/10.21236/ad0617748
[research_currytimothyj_battersonjamesg_2000]: https://ntrs.nasa.gov/citations/20000103558
[research_curtisshc_zhaoxin_1988]: https://ntrs.nasa.gov/citations/19880064556
[research_cusher_gopalarathnam_2006]: https://doi.org/10.2514/6.2006-3320
[research_cusher_gopalarathnam_2012]: https://doi.org/10.2514/1.c031454
[research_czarkowski_2004]: https://doi.org/10.1049/cp:20040572
[research_czaykowski_1958]: https://doi.org/10.1108/eb033001
[research_czyba_blachuta_2001]: https://doi.org/10.2514/6.2001-4087
[research_czyba_blachuta_2003]: https://doi.org/10.2514/6.2003-5554
[research_czyba_stajer_2019]: https://doi.org/10.24425/acs.2019.127525
[research_czyz_karpinski_2020]: https://doi.org/10.2507/ijsimm19-4-534
[research_dahleh_tsitsiklis_2002]: https://doi.org/10.21236/ada417306
[research_dally_vankampen_2022]: https://doi.org/10.2514/6.2022-2078
[research_danowsky_schmidt_2017]: https://doi.org/10.2514/6.2017-1394
[research_dantsker_2024]: https://doi.org/10.2514/6.2024-4395
[research_dantsker_caccamo_2020]: https://doi.org/10.2514/6.2020-0780
[research_dantsker_caccamo_2023]: https://doi.org/10.2514/6.2023-2105
[research_dantsker_haviland_2022]: https://doi.org/10.2514/6.2022-3638
[research_dantsker_haviland_2023]: https://doi.org/10.2514/6.2023-3780
[research_dantsker_mancuso_2019]: https://doi.org/10.2514/6.2019-1616
[research_dantsker_selig_2015]: https://doi.org/10.2514/6.2015-2568
[research_dantsker_theile_2018_b]: https://doi.org/10.2514/6.2018-4217
[research_dantsker_theile_2020]: https://doi.org/10.2514/6.2020-0781
[research_dantsker_vahora_2018]: https://doi.org/10.2514/6.2018-4219
[research_dantsker_yu_2019]: https://doi.org/10.2514/6.2019-3230
[research_dapolito_sulzbachner_2021]: https://doi.org/10.1016/j.ifacol.2021.10.454
[research_daryanto_purwono_2018]: https://doi.org/10.1088/1742-6596/1005/1/012032
[research_das_mankodi_2024]: https://doi.org/10.1115/gt2024-128990
[research_daskiran_huff_2017]: https://doi.org/10.2514/6.2017-0934
[research_dat_son_2018]: https://doi.org/10.1145/3177457.3177470
[research_daughaday_duwaldt_1955]: https://doi.org/10.21236/ad0103817
[research_davidsonjohnb_murphypatrickc_1998]: https://ntrs.nasa.gov/citations/19990008184
[research_davidwking_1993]: https://ntrs.nasa.gov/citations/19940008843
[research_davis_hines_1976]: https://doi.org/10.21236/ada027367
[research_davoudi_duraisamy_2019]: https://doi.org/10.2514/6.2019-2823
[research_de_salvatore_2015]: https://doi.org/10.15224/978-1-63248-045-3-44
[research_dealmeida_dias_2024]: https://doi.org/10.5433/1679-0375.2024.v45.51520
[research_dean_1978]: https://doi.org/10.1115/78-gt-42
[research_debecdelievre_kroo_2021]: https://doi.org/10.2514/6.2021-3063
[research_deboer_kimball_2026]: https://doi.org/10.3390/act15050272
[research_debruin_jones_2016]: https://doi.org/10.1016/j.ifacol.2016.09.030
[research_debry_komerath_1992]: https://doi.org/10.2514/6.1992-2729
[research_decastro_brembeck_2019]: https://doi.org/10.23919/acc.2019.8814326
[research_deere_viken_2017]: https://doi.org/10.2514/6.2017-3921
[research_deets_brown_1986]: https://doi.org/10.2514/6.1986-2754
[research_deetsda_edwardsjw_1974]: https://ntrs.nasa.gov/citations/19750002864
[research_deetsdwaina_purifoydana_1998]: https://ntrs.nasa.gov/citations/19980039330
[research_deffenbaugh_jacoby_1980]: https://doi.org/10.21236/ada089496
[research_degenne_verges_1973]: https://doi.org/10.2307/3320247
[research_dejarnette_jones_1978]: https://doi.org/10.21236/ada055846
[research_delarco_alejo_2015]: https://doi.org/10.1109/med.2015.7158726
[research_delaurier_2022]: https://doi.org/10.1201/9781315228167-4
[research_delay_dependent_stability_1999]: https://doi.org/10.1109/acc.1999.782792
[research_dellacasagrande_barsi_2020]: https://doi.org/10.1007/s00348-020-02958-y
[research_dellacorte_vansluis_2021]: https://doi.org/10.2514/6.2021-2467
[research_dellacorte_vansluis_2022]: https://doi.org/10.2514/1.c036596
[research_dellavecchia_nicolosi_2015]: https://doi.org/10.2514/6.2015-2255
[research_demarchi_haning_1978]: https://doi.org/10.21236/ada060326
[research_deng_li_2015]: https://doi.org/10.4028/www.scientific.net/amm.719-720.1244
[research_deng_qu_2017]: https://doi.org/10.2514/6.2017-4234
[research_deng_xu_2024]: https://doi.org/10.3390/drones8100560
[research_denham_owens_2016]: https://doi.org/10.2514/6.2016-3105
[research_denton_benedict_2025]: https://doi.org/10.1177/17568293251361078
[research_deoca_flores_2020]: https://doi.org/10.1109/icuas48674.2020.9213878
[research_depaula_kleine_2017]: https://doi.org/10.2514/6.2017-1422
[research_depaula_porto_2017]: https://doi.org/10.2514/6.2017-1759
[research_derosa_catalano_2024]: https://doi.org/10.2514/6.2024-1357
[research_derrouaoui_bouzid_2023]: https://doi.org/10.1109/icuas57906.2023.10155908
[research_desai_pant_2026]: https://doi.org/10.2514/6.2026-4044
[research_desert_jardin_2019]: https://doi.org/10.1016/j.ast.2019.05.064
[research_deshpande_zhang_2021]: https://doi.org/10.1142/s2737480721400069
[research_design_and_2015]: https://doi.org/10.21275/v4i11.nov151216
[research_design_and_2020]: https://doi.org/10.35940/ijeat.d9147.049420
[research_design_and_2020_b]: https://doi.org/10.38007/proceedings.0000897
[research_deslich_flick_2021]: https://doi.org/10.2514/6.2021-0607
[research_determination_of_2019]: https://doi.org/10.26731/1813-9108.2019.4(64).125-131
[research_dethomas_goel_1982]: https://doi.org/10.2514/6.1982-1597
[research_devan_1989]: https://doi.org/10.2514/6.1989-2195
[research_development_of_2018]: https://doi.org/10.26666/rmp.jesr.2018.6.1
[research_devisser_pool_2023]: https://doi.org/10.2514/1.c037283
[research_devries_vankampen_2019]: https://doi.org/10.2514/6.2019-0144
[research_devries_vos_2023]: https://doi.org/10.2514/1.c036909
[research_dewagter_meulenbeld_2019]: https://doi.org/10.1177/1756829319880302
[research_dexter_hunt_1981]: https://doi.org/10.2514/6.1981-358
[research_dhiman_abhishek_2022]: https://doi.org/10.2514/1.c036390
[research_dianovsky_pecho_2023]: https://doi.org/10.46585/pc.2023.1.2454
[research_dias_2015]: https://doi.org/10.2514/6.2015-1477
[research_dias_2023]: https://doi.org/10.2514/1.c037252
[research_diaspiresdesouza_rodriguez_2017]: https://doi.org/10.26678/abcm.cobem2017.cob17-0208
[research_dickinson_1953]: https://doi.org/10.21236/ada953109
[research_difrancesco_mattei_2016]: https://doi.org/10.2514/1.c033183
[research_difranco_1969]: https://doi.org/10.2514/6.1969-768
[research_difranco_1970]: https://doi.org/10.2514/3.44199
[research_difranco_1971]: https://doi.org/10.21236/ad0742246
[research_diget_hasan_2022]: https://doi.org/10.1109/icuas54217.2022.9836179
[research_digirolamo_1992]: https://doi.org/10.2514/6.1992-4390
[research_digital_model_reference_1994]: https://doi.org/10.1016/0967-0661(94)90529-0
[research_dik_biten_2017]: https://doi.org/10.1016/j.egypro.2017.12.556
[research_dillon_speyer_1996]: https://doi.org/10.2514/6.1996-3830
[research_dillon_speyer_2000]: https://doi.org/10.2514/2.4526
[research_din_mir_2023]: https://doi.org/10.2514/6.2023-1071
[research_ding_eskandarian_2024]: https://doi.org/10.1016/j.ifacol.2024.07.335
[research_diogo_fernandes_2024]: https://doi.org/10.3390/drones8080396
[research_dizdarevic_dizdarevic_2022]: https://doi.org/10.2514/6.2022-3517
[research_do_dang_2023]: https://doi.org/10.15625/vap.2023.0131
[research_dobosbubno_hartsook_1977]: https://doi.org/10.21236/ada062008
[research_dodge_2015]: https://doi.org/10.21236/ad1019503
[research_dogankuzey_yildirimdalkiran_2026]: https://doi.org/10.1108/aeat-08-2025-0283
[research_doko_sasongko_2026]: https://doi.org/10.11648/j.ajae.20261201.11
[research_dolan_1964]: https://doi.org/10.2514/6.1964-806
[research_doll_hoogreef_2024]: https://doi.org/10.2514/6.2024-1304
[research_doman_1995]: https://doi.org/10.21236/ada305053
[research_doman_sparks_2002]: https://doi.org/10.1109/acc.2002.1024507
[research_domino_czyz_2023]: https://doi.org/10.1109/metroaerospace57412.2023.10189976
[research_dong_2021]: https://doi.org/10.1109/ccdc52312.2021.9601532
[research_dong_lu_2016]: https://doi.org/10.1155/2016/5037678
[research_dong_zhou_2025]: https://doi.org/10.1016/j.ast.2025.110199
[research_dongxinmin_xiongzhiguo_2003]: https://doi.org/10.1109/icnnsp.2003.1279270
[research_donovan_allison_2017]: https://doi.org/10.2514/6.2017-3662
[research_dorato_famularo_1999]: https://doi.org/10.1109/9.793731
[research_dotson_lee_2020]: https://doi.org/10.2514/6.2020-3092
[research_dou_duan_2016]: https://doi.org/10.1108/aeat-05-2014-0073
[research_dovi_wrenn_1989]: https://doi.org/10.2514/6.1989-2078
[research_doyle_rosema_2015]: https://doi.org/10.2514/6.2015-2587
[research_drela_1991]: https://doi.org/10.2514/6.1991-3337
[research_drela_giles_1986]: https://doi.org/10.2514/6.1986-1786
[research_drell_1965]: https://doi.org/10.4271/650150
[research_dress_1988]: https://doi.org/10.2514/6.1988-2010
[research_dress_1989]: https://doi.org/10.2514/3.10224
[research_drewiacki_moreira_2025]: https://doi.org/10.2514/6.2025-1440
[research_drewiacki_silvestre_2016]: https://doi.org/10.2514/6.2016-3539
[research_droliviadavis_2021]: https://doi.org/10.71465/ajaae269
[research_du_2019]: https://doi.org/10.5220/0007931607600766
[research_du_2024]: https://doi.org/10.54254/2755-2721/103/20241042
[research_duan_okwudire_2018]: https://doi.org/10.1109/tmech.2018.2796500
[research_duggan_bhandari_2021]: https://doi.org/10.1109/icuas51884.2021.9476857
[research_dukes_1970]: https://doi.org/10.21236/ad0871424
[research_dunn_1980]: https://ntrs.nasa.gov/citations/19800016546
[research_duongnguyen_kashitani_2022]: https://doi.org/10.2514/1.c036154
[research_dupuis_jouhaud_2018]: https://doi.org/10.2514/6.2018-1905
[research_duran_2026]: https://doi.org/10.2514/6.2026-2637
[research_duran_whidborne_2019]: https://doi.org/10.1177/0306419019852688
[research_durgesh_padilla_2019]: https://doi.org/10.2514/6.2019-0847
[research_durham_1999]: https://doi.org/10.2514/6.1999-4214
[research_durhamwayne_nelsonmark_2001]: https://ntrs.nasa.gov/citations/20010029666
[research_durston_schreiner_1983]: https://doi.org/10.2514/6.1983-2510
[research_durston_stonum_1987]: https://doi.org/10.4271/872311
[research_dussart_yusuf_2018]: https://doi.org/10.2514/6.2018-1015
[research_dwivedi_pavithra_2022]: https://doi.org/10.47893/gret.2022.1082
[research_dwyer_1994]: https://doi.org/10.2514/6.1994-2158
[research_dwyer_lutze_1993]: https://doi.org/10.2514/6.1993-3778
[research_dybdal_1987]: https://doi.org/10.1109/proc.1987.13757
[research_ebeling_1969]: https://doi.org/10.1117/12.946816
[research_eberhardt_ward_1999]: https://doi.org/10.2514/6.1999-4042
[research_eberhardt_ward_1999_b]: https://doi.org/10.1002/(sici)1099-1239(19991215)9:14<1013::aid-rnc450>3.0.co;2-4
[research_ebner_mark_1977]: https://doi.org/10.2514/6.1977-1109
[research_edefur_tormalm_2018]: https://doi.org/10.2514/6.2018-3162
[research_edi_2026]: https://doi.org/10.37394/232030.2026.5.2
[research_edwards_1972]: https://doi.org/10.2514/6.1972-883
[research_edwards_fittante_1997]: https://doi.org/10.21236/ada325252
[research_edwards_rankine_1927]: https://doi.org/10.1098/rspa.1927.0178
[research_edwardsjw_deetsda_1975]: https://ntrs.nasa.gov/citations/19750012221
[research_effects_of_1979]: https://doi.org/10.2514/6.1979-1167
[research_efremov_efremov_2019]: https://doi.org/10.1088/1757-899x/476/1/012010
[research_efremov_efremov_2020]: https://doi.org/10.2514/1.g004409
[research_efremov_efremov_2023]: https://doi.org/10.3103/s1068799823010051
[research_efremov_ogloblin_1998]: https://doi.org/10.2514/6.1998-4145
[research_efremov_shcherbakov_2022]: https://doi.org/10.34759/vst-2022-1-201-210
[research_efremov_tiaglik_2019]: https://doi.org/10.2514/6.2019-0564
[research_eftekhari_alobaidi_2019]: https://doi.org/10.5028/jatm.v11.1023
[research_ehlers_smyth_1968]: https://doi.org/10.2514/6.1968-970
[research_ehretdorrism_rossowvernonj_1950]: https://ntrs.nasa.gov/citations/19930082890
[research_eichler_1970]: https://doi.org/10.2514/3.44170
[research_eilertson_1975]: https://doi.org/10.4271/751103
[research_ekaterinaris_schiff_1990]: https://doi.org/10.2514/6.1990-3000
[research_elario_guillmette_1991]: https://ntrs.nasa.gov/citations/19920011423
[research_eldredge_mousavi_2026]: https://doi.org/10.2514/1.j066257
[research_elia_2004]: https://doi.org/10.1109/tac.2004.834119
[research_elliott_saj_2025]: https://doi.org/10.3390/aerospace12090754
[research_ellis_1972]: https://doi.org/10.4271/720317
[research_ellis_christofides_2015]: https://doi.org/10.1002/aic.14964
[research_elmiligui_abdolhamid_2015]: https://doi.org/10.2514/6.2015-1496
[research_elmiligui_abdolhamid_2017]: https://doi.org/10.2514/1.c033242
[research_elmobaraky_benjelloun_2026]: https://doi.org/10.1016/j.rineng.2026.110403
[research_ema_mizukura_1997]: https://doi.org/10.5100/jje.33.supplement_136
[research_emami_castaldi_2022]: https://doi.org/10.1016/j.arcontrol.2022.04.006
[research_emirler_2018]: https://doi.org/10.1049/el.2018.6630
[research_enenakpogbe_whidborne_2025]: https://doi.org/10.1016/j.ast.2025.110145
[research_eney_1967]: https://doi.org/10.2514/6.1967-576
[research_eney_1968]: https://doi.org/10.2514/3.43938
[research_enns_1990]: https://doi.org/10.2514/6.1990-3338
[research_enns_1998]: https://doi.org/10.2514/6.1998-4109
[research_enns_2003]: https://doi.org/10.21236/ada411755
[research_enns_bugajski_1994]: https://doi.org/10.1080/00207179408923070
[research_enns_si_2002]: https://doi.org/10.2514/6.2002-4837
[research_erhard_clarke_2021]: https://doi.org/10.2514/6.2021-1200
[research_erickson_brandon_1987]: https://doi.org/10.2514/6.1987-2617
[research_ericksongarye_1991]: https://ntrs.nasa.gov/citations/19920003776
[research_ericsson_1980]: https://doi.org/10.2514/6.1980-1801
[research_ericsson_1985]: https://doi.org/10.2514/3.45224
[research_ericsson_1985_b]: https://doi.org/10.2514/6.1985-378
[research_ericsson_1989]: https://doi.org/10.2514/6.1989-2223
[research_ericsson_1996]: https://doi.org/10.2514/3.46998
[research_ericsson_1996_b]: https://doi.org/10.2514/3.46969
[research_ericsson_1997]: https://doi.org/10.2514/2.2165
[research_ericsson_beyers_2002]: https://doi.org/10.2514/6.2002-94
[research_ericsson_hanff_1994]: https://doi.org/10.2514/3.46524
[research_ericsson_reding_1985]: https://doi.org/10.2514/6.1985-1797
[research_eris_ozgoren_2026]: https://doi.org/10.2514/1.c038914
[research_erkol_2017]: https://doi.org/10.1177/1756829317734835
[research_ermeydan_kiyak_2017]: https://doi.org/10.1108/aeat-04-2015-0096
[research_erwin_clark_1964]: https://doi.org/10.21236/ad0609059
[research_esfandabadi_djavareshkian_2026]: https://doi.org/10.1155/ijae/8522389
[research_esker_mcardle_1993]: https://doi.org/10.4271/931412
[research_esker_sedrick_1972]: https://doi.org/10.2514/6.1972-1029
[research_esmaeili_delgado_2018]: https://doi.org/10.2514/1.c034591
[research_est_nelson_1992]: https://doi.org/10.2514/3.46209
[research_estlow_kovacevic_1990]: https://doi.org/10.2514/6.1990-1395
[research_eulrich_govindaraj_1978]: https://doi.org/10.2514/6.1978-1326
[research_eulrich_rynaski_1980]: https://doi.org/10.2514/6.1980-1633
[research_evangelista_pfenninger_1987]: https://doi.org/10.2514/6.1987-2349
[research_evans_1964]: https://doi.org/10.2514/6.1964-1106
[research_evans_chamblee_1966]: https://doi.org/10.21236/ad0628775
[research_evans_galow_1949]: https://doi.org/10.21236/adb803042
[research_evansalisonb_1991]: https://ntrs.nasa.gov/citations/19910010772
[research_evawu_zhang_2000]: https://doi.org/10.1002/1099-1115(200011)14:7<775::aid-acs621>3.3.co;2-w
[research_experimental_investigation_2023]: https://doi.org/10.1063/5.0147213
[research_fahmi_woolsey_2018]: https://doi.org/10.2514/6.2018-3620
[research_famularo_dorato_1999]: https://doi.org/10.1142/9789814447317_0043
[research_fan_jiang_2026]: https://doi.org/10.1108/aeat-01-2026-0033
[research_fan_zhu_2006]: https://doi.org/10.1109/isda.2006.162
[research_fang_cao_2026]: https://doi.org/10.1109/ccdc69976.2026.11560046
[research_farcy_khrabrov_2020]: https://doi.org/10.2514/1.c035882
[research_farhadi_2017]: https://doi.org/10.18372/1990-5548.54.12319
[research_fault_tolerant_2025]: https://doi.org/10.37285/bsp.sacad2025.17
[research_faure_leogrande_2020]: https://doi.org/10.1063/5.0025327
[research_fayaz_fathima_2022]: https://doi.org/10.47893/gret.2022.1054
[research_featherjb_joshids_1981]: https://ntrs.nasa.gov/citations/19810059705
[research_fediaevsky_1935]: https://doi.org/10.2514/8.114
[research_fegely_carl_2017]: https://doi.org/10.4050/f-0073-2017-12074
[research_fegely_tischler_2016]: https://doi.org/10.4050/f-0072-2016-11500
[research_fegely_xin_2017]: https://doi.org/10.4050/sm_2017_hq-2372
[research_fei_li_2023]: https://doi.org/10.1016/j.neunet.2023.01.005
[research_feldwisch_2026]: https://doi.org/10.2514/1.c038330
[research_fell_owen_2015]: https://doi.org/10.4050/f-0071-2015-10167
[research_feng_peng_2017]: https://doi.org/10.2514/6.2017-0503
[research_feng_wang_2022]: https://doi.org/10.1109/ccdc55256.2022.10034211
[research_feng_wang_2024]: https://doi.org/10.5220/0013444700004558
[research_ferguson_thomson_2015]: https://doi.org/10.2514/1.c032657
[research_ferguson_thomson_2017]: https://doi.org/10.4050/sm_2017_hq-3260
[research_ferlauto_marsilio_2016]: https://doi.org/10.12989/aas.2016.3.4.367
[research_fernandes_cardosoribeiro_2025]: https://doi.org/10.26678/abcm.cobem2023.cob2023-0896
[research_ferrand_gowree_2026]: https://doi.org/10.2514/1.c038572
[research_ferrari_stengel_2004]: https://doi.org/10.2514/1.12597
[research_fialho_balas_1997]: https://doi.org/10.1109/acc.1997.611769
[research_fielding_southworth_2001]: https://doi.org/10.2514/6.2001-4263
[research_filinov_ostapyuk_2019]: https://doi.org/10.5220/0007948103380343
[research_filinov_tkachenko_2020]: https://doi.org/10.1109/fareastcon50210.2020.9271150
[research_filippoli_perri_2026]: https://doi.org/10.3390/safety12040096
[research_filippoli_perri_2026_b]: https://doi.org/10.3390/engproc2026142013
[research_finigian_kavounas_2024]: https://doi.org/10.3390/aerospace11020133
[research_fischenberg_1995]: https://doi.org/10.2514/6.1995-3438
[research_fitzgerald_gingras_1996]: https://doi.org/10.2514/6.1996-3524
[research_flanagan_chao_2020]: https://doi.org/10.1109/icuas48674.2020.9213906
[research_fleeman_nelson_1974]: https://doi.org/10.2514/6.1974-110
[research_flight_test_1970]: https://doi.org/10.1108/eb034622
[research_flight_test_2016]: https://doi.org/10.21535/dnk59q51
[research_flight_test_evaluation_1985]: https://doi.org/10.2514/3.45139
[research_flow_control_2016]: https://doi.org/10.21152/1750-9548.10.2.117
[research_fogel_englund_1974]: https://doi.org/10.21236/ad0782581
[research_ford_1977]: https://doi.org/10.1108/eb035404
[research_ford_1989]: https://doi.org/10.1108/eb036732
[research_forkun_medzatyi_2020]: https://doi.org/10.31891/2307-5732-2020-289-5-57-64
[research_fosdick_1970]: https://doi.org/10.21236/ad0880677
[research_foss_1944]: https://doi.org/10.1108/eb031139
[research_foster_hartman_2017]: https://doi.org/10.2514/6.2017-3271
[research_foster_miller_2020]: https://doi.org/10.2514/6.2020-1504
[research_foster_ross_1993]: https://doi.org/10.2514/6.1993-3647
[research_franco_correia_2019]: https://doi.org/10.1109/icuas.2019.8798217
[research_francois_probst_2021]: https://doi.org/10.2514/1.c036273
[research_franklin_1970]: https://doi.org/10.2514/6.1970-998
[research_franklin_1971]: https://doi.org/10.2514/3.44303
[research_franklin_hynes_1985]: https://doi.org/10.2514/6.1985-1944
[research_franklin_miller_1967]: https://doi.org/10.2514/6.1967-577
[research_fratello_shearin_1975]: https://doi.org/10.2514/6.1975-512
[research_fratellodavidj_croommarka_1987]: https://ntrs.nasa.gov/citations/19870062335
[research_frazier_1991]: https://doi.org/10.2514/6.1991-3173
[research_fremaux_1995]: https://doi.org/10.2514/3.46895
[research_freudenberg_looze_1985]: https://doi.org/10.1109/tac.1985.1104004
[research_friedland_1982]: https://doi.org/10.2514/3.19782
[research_friehmelt_1996]: https://doi.org/10.2514/6.1996-3412
[research_friehmelt_1997]: https://doi.org/10.1016/s1474-6670(17)42879-5
[research_friend_1964]: https://doi.org/10.2514/6.1964-787
[research_froning_1981]: https://doi.org/10.2514/6.1981-289
[research_frostsusana_bodsonmarc_2009]: https://ntrs.nasa.gov/citations/20110012890
[research_fry_2008]: https://doi.org/10.21236/ada494062
[research_fry_sage_1974]: https://doi.org/10.1109/taes.1974.307926
[research_frycm_sageap_1974]: https://ntrs.nasa.gov/citations/19740017468
[research_fu_yu_2021]: https://doi.org/10.1109/icuas51884.2021.9476716
[research_fuad_matute_2024]: https://doi.org/10.1109/icns60906.2024.10550646
[research_fujimori_nikiforuk_1999]: https://doi.org/10.1016/s1474-6670(17)57358-9
[research_fujimori_wu_1997]: https://doi.org/10.2514/6.1997-3760
[research_fujimori_wu_1998]: https://doi.org/10.2514/6.1998-4486
[research_fujita_uechi_2019]: https://doi.org/10.2514/6.2019-1893
[research_fukami_higashino_2004]: https://doi.org/10.2514/6.2004-5176
[research_fukui_harada_2020]: https://doi.org/10.1299/jsmecs.2020.58.10c6
[research_fukushima_tsubone_2019]: https://doi.org/10.1109/isocc47750.2019.9027701
[research_fulkerson_hershberger_1980]: https://doi.org/10.1177/107118138002400115
[research_funk_1975]: https://doi.org/10.21236/ada021328
[research_gacy_2011]: https://doi.org/10.21236/ada550675
[research_gadient_weltz_2004]: https://doi.org/10.2514/6.2004-5001
[research_gagg_1937]: https://doi.org/10.4271/370171
[research_gagnon_zingg_2016]: https://doi.org/10.2514/1.c033592
[research_gain_scheduled_2004]: https://doi.org/10.5302/j.icros.2004.10.2.125
[research_gainer_1963]: https://doi.org/10.21236/ad0404850
[research_gaithersa_agarwalak_1989]: https://ntrs.nasa.gov/citations/19890065157
[research_galeani_grasselli_2004]: https://doi.org/10.1080/00207170410001669691
[research_gallagher_1971]: https://doi.org/10.2514/3.59189
[research_gallay_laurendeau_2016]: https://doi.org/10.2514/1.c033460
[research_galor_1992]: https://doi.org/10.2514/3.46214
[research_galor_1994]: https://doi.org/10.1515/tjj.1994.11.2-3.119
[research_galor_2001]: https://doi.org/10.1515/tjj.2001.18.1.41
[research_galor_baumann_1993]: https://doi.org/10.2514/3.48273
[research_galor_sherbaum_1995]: https://doi.org/10.2514/3.46758
[research_gamal_sadek_2016]: https://doi.org/10.1016/j.aej.2016.04.005
[research_gamble_inman_2016]: https://doi.org/10.4028/www.scientific.net/ast.101.127
[research_gan_botre_2021]: https://doi.org/10.4050/f-0077-2021-16693
[research_gan_zha_2015]: https://doi.org/10.2514/6.2015-1249
[research_gandhi_whitcher_2019]: https://doi.org/10.2514/6.2019-1982
[research_gao_liu_2020]: https://doi.org/10.1109/icuas48674.2020.9213836
[research_gao_shi_2022]: https://doi.org/10.1109/icuas54217.2022.9836203
[research_gao_wang_2015]: https://doi.org/10.2514/6.2015-3094
[research_gao_wang_2021]: https://doi.org/10.3390/atmos12040470
[research_garbarino_genito_2023]: https://doi.org/10.1109/dasc58513.2023.10311145
[research_gardner_downey_1950]: https://doi.org/10.21236/ad0069271
[research_garkushenko_vinogradov_2016]: https://doi.org/10.3103/s1068799816040085
[research_garrard_1998]: https://doi.org/10.2514/2.7612
[research_garretsoniii_1986]: https://doi.org/10.2514/6.1986-9828
[research_gassler_robens_2025]: https://doi.org/10.2514/6.2025-0313
[research_gaudet_furfaro_2023]: https://doi.org/10.2514/6.2023-1628
[research_gavra_vankampen_2024]: https://doi.org/10.2514/1.g008112
[research_gavra_vankampen_2024_b]: https://doi.org/10.2514/6.2024-0954
[research_gaylor_1984]: https://doi.org/10.2514/6.1984-2489
[research_ge_zhan_2024]: https://doi.org/10.1117/12.3039498
[research_gebert_kelly_2000]: https://doi.org/10.2514/6.2000-829
[research_geeken_rizkyehiam_1992]: https://ntrs.nasa.gov/citations/19920062906
[research_geesw_1978]: https://ntrs.nasa.gov/citations/19780010099
[research_genc_koca_2022]: https://doi.org/10.1051/epjconf/202226901016
[research_geng_kalkman_2018]: https://doi.org/10.1016/j.jweia.2018.11.009
[research_geng_li_2023]: https://doi.org/10.23919/ccc58697.2023.10239932
[research_genito_garbarino_2024]: https://doi.org/10.1109/dasc62030.2024.10749339
[research_gerhardtha_chenws_1978]: https://ntrs.nasa.gov/citations/19790001855
[research_gerken_1979]: https://doi.org/10.21236/ada132587
[research_gerosa_zanoni_2018]: https://doi.org/10.4050/f-0074-2018-12718
[research_gertsen_shomber_1965]: https://doi.org/10.2514/6.1965-780
[research_geuther_ackerman_2024]: https://doi.org/10.4050/f-0080-2024-1185
[research_ghanchi_gururajan_2026]: https://doi.org/10.2514/6.2026-1866
[research_ghasemzadeh_banazadeh_2025]: https://doi.org/10.2514/1.c038159
[research_ghazi_1993]: https://doi.org/10.2514/6.1993-3641
[research_ghiglino_forshaw_2015]: https://doi.org/10.2514/1.g000376
[research_ghofurm_darmawan_2020]: https://doi.org/10.54317/kom.v2ioktober.180
[research_ghorawat_lee_2015]: https://doi.org/10.2514/6.2015-2555
[research_ghosh_raisinghani_1998]: https://doi.org/10.2514/2.2407
[research_ghosh_raisinghani_2000]: https://doi.org/10.2514/6.2000-4102
[research_ghosh_raisinghani_2002]: https://doi.org/10.2514/2.3012
[research_ghoshroy_peyada_2016]: https://doi.org/10.2514/6.2016-3708
[research_ghoshroy_peyada_2017]: https://doi.org/10.2514/6.2017-3896
[research_giacomini_westerberg_2025]: https://doi.org/10.3390/app151810299
[research_gibson_1990]: https://doi.org/10.2514/6.1990-2844
[research_gilbreath_markofski_2001]: https://doi.org/10.2514/6.2001-4007
[research_gill_1974]: https://doi.org/10.2514/3.60411
[research_gillard_1998]: https://doi.org/10.21236/ada362903
[research_gillard_dorsett_1997]: https://doi.org/10.2514/6.1997-3487
[research_gilyard_berry_1972]: https://doi.org/10.2514/6.1972-961
[research_gingrich_child_1977]: https://ntrs.nasa.gov/citations/19770019132
[research_glad_1982]: https://doi.org/10.1109/cdc.1982.268287
[research_glad_1984]: https://doi.org/10.1109/cdc.1984.272154
[research_glenn_1988]: https://doi.org/10.1177/154193128803201611
[research_glezer_leonard_2012]: https://doi.org/10.21236/ada564094
[research_glizde_2017]: https://doi.org/10.1515/tae-2017-0010
[research_gnatowska_gajewska_2024]: https://doi.org/10.3390/en18010066
[research_go_maqsood_2015]: https://doi.org/10.1016/j.ast.2015.01.009
[research_goerttler_2025]: https://doi.org/10.2514/1.c038181
[research_goetz_young_1976]: https://doi.org/10.2514/6.1976-626
[research_goetzendorfgrabowski_antoniewski_2016]: https://doi.org/10.1108/aeat-02-2015-0055
[research_goetzendorfgrabowski_kwiek_2023]: https://doi.org/10.3390/app132212522
[research_gold_walchli_1974]: https://doi.org/10.2514/6.1974-952
[research_goldberger_1966]: https://doi.org/10.21236/ad0644191
[research_goldstein_1982]: https://doi.org/10.4050/sm_handling_1982-4947
[research_goman_kolesnikov_1998]: https://doi.org/10.2514/6.1998-4208
[research_gomes_suleman_2004]: https://doi.org/10.2514/6.2004-4608
[research_gong_wang_2019]: https://doi.org/10.1177/0020294019830434
[research_gonzalez_aranda_2017]: https://doi.org/10.1016/j.ifacol.2017.08.1667
[research_goodrich_sliwa_1987]: https://doi.org/10.2514/6.1987-2590
[research_goodwinfrederickk_kaattarigeorgee_1958]: https://ntrs.nasa.gov/citations/19980228369
[research_gopalarathnam_broughton_2001]: https://doi.org/10.2514/6.2001-2463
[research_gopalarathnam_mcavoy_2002]: https://doi.org/10.2514/2.2968
[research_gopalarothnam_mcgowan_2008]: https://doi.org/10.21236/ada479418
[research_goparaju_gaitonde_2015]: https://doi.org/10.2514/6.2015-3065
[research_gordnier_1995]: https://doi.org/10.2514/3.46746
[research_gorin_gubankov_2025]: https://doi.org/10.1109/rusautocon65989.2025.11177273
[research_gorski_1998]: https://doi.org/10.21236/ada360504
[research_gossett_1981]: https://ntrs.nasa.gov/citations/19810009770
[research_gottlicher_gnoth_2016]: https://doi.org/10.2514/6.2016-1534
[research_gou_liu_2023]: https://doi.org/10.1017/aer.2023.93
[research_goud_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1057
[research_govindaraj_rynaski_1979]: https://doi.org/10.21236/ada074092
[research_graftonsb_chambersjr_1974]: https://ntrs.nasa.gov/citations/19740018330
[research_graftonsb_gilberwp_1982]: https://ntrs.nasa.gov/citations/19820055564
[research_granasy_1995]: https://doi.org/10.2514/6.1995-3923
[research_granata_mancini_2026]: https://doi.org/10.1016/j.ast.2026.112734
[research_grant_stol_2015]: https://doi.org/10.2514/1.g000826
[research_granthamwd_nguyenlt_1976]: https://ntrs.nasa.gov/citations/19770011064
[research_grauer_2015]: https://doi.org/10.2514/1.c033182
[research_grauer_2016]: https://doi.org/10.2514/6.2016-2009
[research_grauer_2020]: https://doi.org/10.2514/6.2020-0288
[research_grauer_2021]: https://doi.org/10.2514/1.c035933
[research_grauer_boucher_2018]: https://doi.org/10.2514/6.2018-3155
[research_grauer_morelli_2015]: https://doi.org/10.2514/6.2015-2704
[research_grauer_morelli_2015_b]: https://doi.org/10.2514/1.c032888
[research_gray_1964]: https://doi.org/10.21236/ad0602769
[research_grayjr_1964]: https://doi.org/10.2514/6.1964-192
[research_green_1958]: https://doi.org/10.1119/1.1934653
[research_green_1988]: https://doi.org/10.2514/6.1988-4142
[research_greene_kunz_2015]: https://doi.org/10.2514/6.2015-2393
[research_greenwell_2003]: https://doi.org/10.2514/2.3110
[research_greer_hamory_1999]: https://doi.org/10.2514/6.1999-3183
[research_gregory_1998]: https://doi.org/10.2514/6.1998-4323
[research_gregory_2001]: https://doi.org/10.2514/6.2001-4284
[research_gregoryirenem_chowdhryrajivs_1994]: https://ntrs.nasa.gov/citations/19950006425
[research_gres_stoura_2025]: https://doi.org/10.13052/97887-438-0148-1_14
[research_gresham_simmons_2023]: https://doi.org/10.2514/1.c036942
[research_griffin_bellaire_1968]: https://doi.org/10.21236/ad0850270
[research_grimminger_williams_1950]: https://doi.org/10.2514/8.1775
[research_grismer_myatt_1997]: https://doi.org/10.2514/6.1997-3644
[research_grogan_durham_1994]: https://doi.org/10.2514/6.1994-3644
[research_grondman_looye_2018]: https://doi.org/10.2514/6.2018-0385
[research_grossman_1957]: https://doi.org/10.4271/570202
[research_gu_2025]: https://doi.org/10.1049/icp.2024.3065
[research_gu_lee_1988]: https://doi.org/10.23919/acc.1988.4790111
[research_gu_lyu_2017]: https://doi.org/10.1109/icuas.2017.7991420
[research_gu_valavanis_2019]: https://doi.org/10.1109/icuas.2019.8797853
[research_guan_shi_2019]: https://doi.org/10.1109/ccdc.2019.8832672
[research_guay_drolet_2017]: https://doi.org/10.1049/iet-rsn.2016.0520
[research_guenther_eichner_2026]: https://doi.org/10.2514/6.2026-4744
[research_guerrero_martinez_2015]: https://doi.org/10.1109/icuas.2015.7152403
[research_guerrerobonilla_mohta_2017]: https://doi.org/10.1109/icuas.2017.7991473
[research_guiler]: https://doi.org/10.33915/etd.2779
[research_guiler_huebsch_2005]: https://doi.org/10.2514/6.2005-4981
[research_guler_durhasan_2021]: https://doi.org/10.21597/jist.897982
[research_gumusboga_iftar_2021]: https://doi.org/10.1017/aer.2021.66
[research_gundry_1977]: https://doi.org/10.2514/3.58832
[research_gungordu_tayfuner_2026]: https://doi.org/10.1051/epjconf/202635801006
[research_guo_2021]: https://doi.org/10.1088/1742-6596/1877/1/012019
[research_guo_2021_b]: https://doi.org/10.1088/1742-6596/1877/1/012022
[research_guo_lin_2018]: https://doi.org/10.1109/icmmt.2018.8563643
[research_guo_liu_2026]: https://doi.org/10.1007/s42401-026-00489-8
[research_guo_zhang_2024]: https://doi.org/10.3390/aerospace12010010
[research_guo_zhu_2017]: https://doi.org/10.1016/j.cja.2016.12.034
[research_guoqiang_jinkun_2015]: https://doi.org/10.1155/2015/591789
[research_gupta_aswathanarayana_2025]: https://doi.org/10.1007/s40032-025-01173-0
[research_guptaroopn_leekampui_1991]: https://ntrs.nasa.gov/citations/19920002067
[research_gursoy_yavrucuk_2015]: https://doi.org/10.2514/6.2015-0748
[research_gursul_srinivas_1995]: https://doi.org/10.2514/3.12721
[research_gursul_yang_1994]: https://doi.org/10.2514/6.1994-536
[research_gursul_yang_1995]: https://doi.org/10.1006/jfls.1995.1032
[research_guy_1976]: https://doi.org/10.2514/3.44533
[research_h_s_2016]: https://doi.org/10.4172/2168-9792.1000165
[research_ha_1990]: https://doi.org/10.2514/6.1990-3226
[research_ha_kim_2025]: https://doi.org/10.6108/kspe.2025.29.6.045
[research_haber_chung_2016]: https://doi.org/10.1139/juvs-2015-0039
[research_hacker_1977]: https://doi.org/10.2514/3.44571
[research_hadidoolabi_ansarian_2017]: https://doi.org/10.24200/sci.2017.4246
[research_hadidoolabi_ansarian_2018]: https://doi.org/10.1007/s40430-018-1021-z
[research_hafez_kamel_2016]: https://doi.org/10.1109/icuas.2016.7502660
[research_haffley_1982]: https://doi.org/10.4050/sm_handling_1982-1307
[research_hageman_smith_2003]: https://doi.org/10.2514/6.2003-5700
[research_hajiyev_2016]: https://doi.org/10.1109/aucc.2016.7868210
[research_hajiyevt_caliskan_2001]: https://doi.org/10.1017/s0001924000017966
[research_hakim_choukri_2023]: https://doi.org/10.1007/s42405-023-00670-9
[research_hale_patil_2015]: https://doi.org/10.2514/6.2015-1538
[research_hale_patil_2017]: https://doi.org/10.2514/1.g000582
[research_halefom_gresham_2022]: https://doi.org/10.2514/6.2022-0554
[research_hall_1965]: https://doi.org/10.2514/3.43658
[research_hall_1971]: https://doi.org/10.2514/3.59106
[research_hall_1987]: https://doi.org/10.2514/6.1987-2274
[research_hall_boothe_1972]: https://doi.org/10.2514/3.58945
[research_hall_kern_1996]: https://doi.org/10.2514/6.1996-2400
[research_hall_lawrence_2006]: https://doi.org/10.2514/6.2006-6689
[research_hall_weingarten_1974]: https://doi.org/10.2514/3.60377
[research_halljr_perkins_1999]: https://doi.org/10.2514/6.1999-535
[research_hallrobertm_ericksongarye_1998]: https://ntrs.nasa.gov/citations/19980137574
[research_hamel_jategaonkar_1996]: https://doi.org/10.2514/3.46898
[research_hamidani_kunz_2018]: https://doi.org/10.2514/6.2018-1019
[research_hammer_degraaf_2026]: https://doi.org/10.3390/engproc2026133106
[research_hammer_shumway_2026]: https://doi.org/10.2514/1.c038997
[research_hammer_shumway_2026_b]: https://doi.org/10.2514/6.2026-2839
[research_hamza_samir_2020]: https://doi.org/10.35840/2631-5106/4123
[research_han_cheng_2023]: https://doi.org/10.1016/j.neucom.2023.126789
[research_han_hu_2019]: https://doi.org/10.23919/chicc.2019.8865734
[research_han_kim_2026]: https://doi.org/10.1145/3772363.3798932
[research_han_patel_1977]: https://doi.org/10.21236/ada045245
[research_han_wang_2025]: https://doi.org/10.2514/1.c038201
[research_han_yang_2024]: https://doi.org/10.1109/access.2024.3411015
[research_han_zhang_2019]: https://doi.org/10.1109/safeprocess45799.2019.9213409
[research_hansencfrederick_1959]: https://ntrs.nasa.gov/citations/19980237039
[research_hansoncurtise_2012]: https://ntrs.nasa.gov/citations/20150000179
[research_hantla_wang_2025]: https://doi.org/10.2514/1.c038430
[research_hardy_sturgeon_1979]: https://doi.org/10.1109/cdc.1979.270266
[research_harkegard_2003]: https://doi.org/10.23919/ecc.2003.7085231
[research_harmats_weihs_1999]: https://doi.org/10.2514/2.2443
[research_harper_cooper_1986]: https://doi.org/10.2514/3.20142
[research_harper_robertp_1955]: https://doi.org/10.21236/ad0092496
[research_harper_sardanowsky_1969]: https://doi.org/10.21236/ad0858184
[research_harperjr_cooper_1984]: https://doi.org/10.2514/6.1984-2442
[research_harrington_1939]: https://doi.org/10.1103/physrev.55.230
[research_harris_2000]: https://doi.org/10.1177/002029400003300805
[research_harris_arthurs_2016]: https://doi.org/10.1109/icuas.2016.7502624
[research_harris_elliott_2019]: https://doi.org/10.2514/6.2019-0141
[research_harris_gautrey_2000]: https://doi.org/10.1017/s0001924000028098
[research_harris_harris_1997]: https://doi.org/10.2514/6.1997-5505
[research_harris_rickard_1979]: https://doi.org/10.2514/3.58598
[research_harry_trobaugh_1966]: https://doi.org/10.21236/ad0641246
[research_hart_1956]: https://doi.org/10.21236/ad0108104
[research_hart_1968]: https://doi.org/10.2514/6.1968-817
[research_hart_picha_1979]: https://doi.org/10.2514/6.1979-1801
[research_hart_sytsma_2016]: https://doi.org/10.1177/1756829316653696
[research_hartley_cwynar_1984]: https://doi.org/10.1177/154193128402800112
[research_hartley_pulliam_1988]: https://doi.org/10.1109/62.883
[research_hartmann_meyer_2016]: https://doi.org/10.2514/6.2016-2101
[research_hartmann_meyer_2017]: https://doi.org/10.2514/1.g002168
[research_hasan_redonnet_2025]: https://doi.org/10.1016/j.advengsoft.2024.103801
[research_hashemipour_vasegh_2017]: https://doi.org/10.1007/s12555-015-0416-1
[research_hashemzadeh_sharifi_2016]: https://doi.org/10.1016/j.conengprac.2016.08.004
[research_hassan_janakiram_1997]: https://doi.org/10.2514/6.1997-2326
[research_hastedt_theis_2022]: https://doi.org/10.2514/6.2022-0283
[research_hauser_1999]: https://doi.org/10.21236/ada387263
[research_he_hu_2022]: https://doi.org/10.3390/aerospace9070352
[research_he_hu_2022_b]: https://doi.org/10.1016/j.isatra.2022.04.041
[research_he_tan_2020]: https://doi.org/10.1109/access.2020.3035436
[research_he_zhang_2021]: https://doi.org/10.23919/ccc52363.2021.9550496
[research_head_1962]: https://doi.org/10.4050/jahs.7.28
[research_heald_brassell_1976]: https://doi.org/10.2514/6.1976-891
[research_healyfrederickm_1958]: https://ntrs.nasa.gov/citations/20050028462
[research_hebbar_pashilkar_2016]: https://doi.org/10.14429/dsj.66.9196
[research_hebbar_platzer_1991]: https://doi.org/10.2514/6.1991-280
[research_hegde_2020]: https://doi.org/10.5373/jardcs/v12sp3/20201352
[research_hegde_george_2019]: https://doi.org/10.1109/iceca.2019.8822119
[research_helicopter_yaw_1990]: https://doi.org/10.1108/eb036942
[research_heller_clemente_1973]: https://doi.org/10.2514/6.1973-998
[research_hemingyi_jianghailin_1998]: https://doi.org/10.1109/62.715536
[research_hemsch_1985]: https://doi.org/10.2514/6.1985-1775
[research_hemsch_1987]: https://doi.org/10.2514/6.1987-267
[research_hemsch_1988]: https://doi.org/10.2514/6.1988-216
[research_hemsch_1989]: https://doi.org/10.2514/6.1989-2176
[research_henkenjohann_nolte_2023]: https://doi.org/10.1109/icuas57906.2023.10156317
[research_henkenjohann_nolte_2024]: https://doi.org/10.3390/act13050187
[research_henn_boronow_1959]: https://doi.org/10.1109/tac.1959.1104881
[research_herbst_kahler_2018]: https://doi.org/10.2514/6.2018-3490
[research_herrera_njeh_2018]: https://doi.org/10.1109/csci46756.2018.00275
[research_herrick_1992]: https://doi.org/10.1515/tjj.1992.9.1.29
[research_herrington_zahed_2023]: https://doi.org/10.1142/s2301385024500080
[research_herrlinger_1991]: https://doi.org/10.2514/6.1991-3172
[research_herrmann_benasher_2016]: https://doi.org/10.2514/1.c033517
[research_herrmann_schmidt_2018]: https://doi.org/10.1515/icom-2018-0001
[research_heryana_krisnandi_2022]: https://doi.org/10.1145/3575882.3575891
[research_hess_1980]: https://doi.org/10.2514/6.1980-1624
[research_hess_1981]: https://doi.org/10.2514/6.1981-1771
[research_hess_1984]: https://doi.org/10.2514/6.1984-236
[research_hess_1987]: https://doi.org/10.2514/6.1987-2537
[research_hess_1995]: https://doi.org/10.1109/21.364831
[research_hess_1997]: https://doi.org/10.2514/2.4169
[research_hess_1998]: https://doi.org/10.2514/2.4203
[research_hess_2016]: https://doi.org/10.1016/j.ifacol.2016.12.206
[research_hess_hess_1997]: https://doi.org/10.2514/6.1997-454
[research_hess_hess_1997_b]: https://doi.org/10.2514/6.1997-3498
[research_hess_peng_2018]: https://doi.org/10.2514/1.c034497
[research_hess_wells_2002]: https://doi.org/10.2514/6.2002-245
[research_hess_wells_2003]: https://doi.org/10.2514/2.5083
[research_hessronalda_mcleanc_2000]: https://ntrs.nasa.gov/citations/20000109866
[research_heyer_kroezen_2020]: https://doi.org/10.2514/6.2020-1844
[research_hicksjohnw_mathenyneilw_1989]: https://ntrs.nasa.gov/citations/19890061478
[research_hienz_vedova_1984]: https://doi.org/10.2514/6.1984-1212
[research_higgins_shomber_1964]: https://doi.org/10.2514/6.1964-603
[research_higgins_shomber_1965]: https://doi.org/10.2514/3.43684
[research_hill_1987]: https://doi.org/10.21236/ada186949
[research_hines_gaffin_1976]: https://doi.org/10.2514/6.1976-666
[research_hirai_satoh_1980]: https://doi.org/10.1109/tac.1980.1102355
[research_hirano_uchiyama_2019]: https://doi.org/10.1109/icuas.2019.8797724
[research_hitzel_1988]: https://doi.org/10.2514/6.1988-2518
[research_hitzel_2017]: https://doi.org/10.2514/1.c034025
[research_hitzel_zimper_2018]: https://doi.org/10.2514/1.c033696
[research_ho_hang_1993]: https://doi.org/10.1016/s1474-6670(17)48453-9
[research_ho_hang_1995]: https://doi.org/10.1016/0005-1098(94)00130-b
[research_ho_lim_1998]: https://doi.org/10.1016/s0005-1098(98)00032-6
[research_ho_zhou_2023]: https://doi.org/10.15607/rss.2023.xix.081
[research_hodgkinson_2003]: https://doi.org/10.2514/6.2003-5466
[research_hodgkinson_lamanna_1977]: https://doi.org/10.2514/6.1977-1122
[research_hodgkinson_potsdam_1990]: https://doi.org/10.2514/6.1990-2825
[research_hoegarrison_owensdonaldb_2012]: https://ntrs.nasa.gov/citations/20120014506
[research_hoffer_coopmans_2015]: https://doi.org/10.1109/icuas.2015.7152430
[research_hoffler_rao_1988]: https://doi.org/10.2514/3.45563
[research_hoffman_stalford_1991]: https://doi.org/10.2514/6.1991-2667
[research_hofmann_hosseini_2025]: https://doi.org/10.2514/6.2025-2175
[research_hofsa_holzapfel_2024]: https://doi.org/10.1109/dasc62030.2024.10748693
[research_hogan_rinde_1978]: https://doi.org/10.21236/ada062030
[research_hoh_1982]: https://doi.org/10.4050/sm_handling_1982-3589
[research_hoh_1988]: https://doi.org/10.2514/6.1988-4328
[research_hoh_mitchell_1983]: https://doi.org/10.21236/ada132857
[research_hoholis_steijl_2016]: https://doi.org/10.2514/1.c033642
[research_hollingsworth_cohen_1971]: https://doi.org/10.2514/3.59167
[research_hollmeier_kopp_1999]: https://doi.org/10.1515/tjj.1999.16.4.207
[research_holman_1876]: https://doi.org/10.2307/25138434
[research_holman_1885]: https://doi.org/10.2307/25129807
[research_holmes_woehr_1971]: https://doi.org/10.2514/6.1971-278
[research_homola_li_2025]: https://doi.org/10.2514/6.2025-2793
[research_hong_ma_2016]: https://doi.org/10.4028/www.scientific.net/amm.829.110
[research_hongyan_xiaoyong_2026]: https://doi.org/10.1109/access.2026.3692889
[research_horn_thorsen_2017]: https://doi.org/10.4050/f-0073-2017-12066
[research_horowitz_1964]: https://doi.org/10.1109/tac.1964.1105627
[research_horowitz_1965]: https://doi.org/10.1016/0005-1098(65)90007-5
[research_horst_sommerwerk_2017]: https://doi.org/10.2514/6.2017-3560
[research_hosseini_bridges_2025]: https://doi.org/10.4050/f-0081-2025-0403
[research_hosseini_hofmann_2025]: https://doi.org/10.2514/6.2025-2173
[research_hossny_elbadawy_2020]: https://doi.org/10.1109/icuas48674.2020.9213902
[research_hou_xue_2011]: https://doi.org/10.4028/www.scientific.net/amm.105-107.2055
[research_hougui_balas_1995]: https://doi.org/10.2514/6.1995-3253
[research_houston_1937]: https://doi.org/10.1103/physrev.52.751
[research_how_2008]: https://doi.org/10.21236/ada484530
[research_howard_1975]: https://ntrs.nasa.gov/citations/19750022085
[research_howard_1976]: https://ntrs.nasa.gov/citations/19990117220
[research_howard_bray_1992]: https://doi.org/10.2514/6.1992-4075
[research_hoxey_robertson_1997]: https://doi.org/10.1016/s0167-6105(97)00185-2
[research_hoyt_kempel_1980]: https://doi.org/10.2514/6.1980-1761
[research_hreha_lutze_1983]: https://doi.org/10.2514/6.1983-367
[research_hreha_lutze_1984]: https://doi.org/10.2514/3.48223
[research_hsiao_1988]: https://doi.org/10.2514/6.1988-2575
[research_hsiao_ho_1997]: https://doi.org/10.2514/6.1997-3693
[research_hsiao_wang_2004]: https://doi.org/10.1299/jsmemecjsm.2004.8.0_13
[research_hsieh_wang_1976]: https://doi.org/10.2514/3.7145
[research_hu_huang_2017]: https://doi.org/10.1109/icus.2017.8278366
[research_hu_song_2024]: https://doi.org/10.1142/s2737480724300026
[research_hu_wen_2025]: https://doi.org/10.3390/drones9090635
[research_hu_zhao_2025]: https://doi.org/10.1007/s11768-025-00268-4
[research_huang_2016]: https://doi.org/10.1109/ecc.2016.7810266
[research_huang_celi_1999]: https://doi.org/10.4050/jahs.44.50
[research_huang_li_2026]: https://doi.org/10.2514/1.c038842
[research_huang_pool_2017]: https://doi.org/10.1016/j.ifacol.2017.08.837
[research_huang_tylock_1992]: https://doi.org/10.2514/6.1992-4394
[research_huang_wang_2001]: https://doi.org/10.1016/s0016-0032(00)00080-6
[research_huang_zhang_2020]: https://doi.org/10.1109/icuas48674.2020.9213966
[research_huang_zhang_2022]: https://doi.org/10.2514/1.g006024
[research_hubener_luckner_2026]: https://doi.org/10.1007/s13272-025-00930-2
[research_huber_1995]: https://doi.org/10.2514/6.1995-3199
[research_huber_2022]: https://doi.org/10.2514/6.2022-3438
[research_huberpeter_schellengerharveyg_1994]: https://ntrs.nasa.gov/citations/19950007829
[research_hueschenrm_1984]: https://ntrs.nasa.gov/citations/19840012521
[research_huff_ww_1949]: https://doi.org/10.21236/ad0035641
[research_huguenin_1981]: https://doi.org/10.2514/6.1981-973
[research_hull_roger_1975]: https://doi.org/10.21236/adb011143
[research_humphreys_watkinson_1972]: https://doi.org/10.1109/oceans.1972.1161117
[research_humphreysjennings_lappas_2020]: https://doi.org/10.3390/aerospace7050051
[research_hung_1979]: https://doi.org/10.2514/6.1979-1547
[research_hung_1980]: https://doi.org/10.2514/3.50835
[research_hunt_gowadia_1981]: https://doi.org/10.2514/6.1981-1692
[research_huntercraiga_vikensallya_2001]: https://ntrs.nasa.gov/citations/20010013824
[research_huntley_woods_2019]: https://doi.org/10.2514/6.2019-2914
[research_huntoon_schohan_1979]: https://doi.org/10.21236/ada072402
[research_huo_duan_2021]: https://doi.org/10.1142/s2301385021410053
[research_hushengwu_weizonglu_2015]: https://doi.org/10.1109/cac.2015.7382829
[research_hutt_east_1985]: https://doi.org/10.1177/002029408501800302
[research_huzmezan_1998]: https://doi.org/10.1049/cp:19980393
[research_huzmezan_maciejowski_1999]: https://doi.org/10.1016/s1474-6670(17)57361-9
[research_hwang_yoo_2024]: https://doi.org/10.5302/j.icros.2024.23.0205
[research_hydecharlesr_massiejeffreyj_1993]: https://ntrs.nasa.gov/citations/19930068757
[research_hydedavidc_shweykkamalm_2014]: https://ntrs.nasa.gov/citations/20140006174
[research_ibraheem_2019]: https://doi.org/10.31026/j.eng.2020.01.08
[research_ibuka_ishiguro_2023]: https://doi.org/10.12792/jiiae.11.15
[research_idan_merhav_1990]: https://doi.org/10.2514/3.25380
[research_identification_method_2023]: https://doi.org/10.36652/0869-4931-2023-77-12-560-566
[research_identification_modelling_2015]: https://doi.org/10.26634/jic.3.1.3420
[research_iglesis_horri_2021]: https://doi.org/10.1109/icuas51884.2021.9476852
[research_ignatyev_2018]: https://doi.org/10.1051/eucass/201810073
[research_iharasani_2015]: https://doi.org/10.5176/2382-5758_1.2.10
[research_ikeda_atobe_2015]: https://doi.org/10.2514/1.j053664
[research_iliff_1980]: https://doi.org/10.2514/6.1980-1563
[research_iliff_1987]: https://doi.org/10.2514/6.1987-623
[research_iliff_maine_1983]: https://doi.org/10.2514/3.48210
[research_iloputaife_ma_1987]: https://doi.org/10.2514/6.1987-2450
[research_imran_stolkin_2021]: https://doi.org/10.1016/j.ifacol.2021.08.457
[research_inanc_habboush_2025]: https://doi.org/10.1002/acs.4029
[research_incorporating_agility_1994]: https://doi.org/10.2514/6.1994-2135
[research_inertially_augmented_1971]: https://doi.org/10.2514/6.1971-795
[research_influence_of_interference_2018]: https://doi.org/10.20535/2219-3804182018152273
[research_innocenti_1989]: https://doi.org/10.2514/6.1989-3391
[research_innocenti_petretti_1998]: https://doi.org/10.2514/6.1998-4146
[research_innocenti_thukral_1991]: https://doi.org/10.2514/3.20784
[research_inoue_yasuda_2019]: https://doi.org/10.1299/jsmemecj.2019.s05124p
[research_ioannis_ioannis_2026]: https://doi.org/10.70322/dav.2026.10005
[research_ionita_1996]: https://doi.org/10.2514/6.1996-3424
[research_irwanto_artono_2018]: https://doi.org/10.1088/1742-6596/1130/1/012014
[research_isaac_pena_2024]: https://doi.org/10.1142/s2301385025500396
[research_ishibashi_miyaji_2015]: https://doi.org/10.2514/1.c032628
[research_ishikawa_yamazaki_2021]: https://doi.org/10.1299/jsmecmd.2021.34.113
[research_ishmaelsd_wierzbanowskit_1985]: https://ntrs.nasa.gov/citations/19860060204
[research_ishola_whidborne_2024]: https://doi.org/10.3390/robotics13120179
[research_islam_faraz_2015]: https://doi.org/10.1109/icuas.2015.7152272
[research_ito_endo_2016]: https://doi.org/10.1299/jsmermd.2016.1a2-18a4
[research_ito_murayama_2017]: https://doi.org/10.2514/6.2017-3804
[research_itsariyapinyo_sharma_2016]: https://doi.org/10.2514/6.2016-3772
[research_ivan_1985]: https://doi.org/10.2514/6.1985-1749
[research_ivler_geyer_2024]: https://doi.org/10.4050/f-0080-2024-1171
[research_ivler_truong_2022]: https://doi.org/10.4050/jahs.67.012002
[research_iyengar_mavris_2025]: https://doi.org/10.2514/1.c038020
[research_jabbari_esmaeili_2021]: https://doi.org/10.1016/j.oceaneng.2021.109731
[research_jackjohnr_1951]: https://ntrs.nasa.gov/citations/19930086899
[research_jacob_stewart_2026]: https://doi.org/10.2514/6.2026-2485
[research_jacobson_joshi_1977]: https://doi.org/10.2514/3.44591
[research_jacobson_joshi_1978]: https://doi.org/10.2514/3.58351
[research_jafari_fehr_2017]: https://doi.org/10.1109/icuas.2017.7991512
[research_jafari_khakisedigh_2022]: https://doi.org/10.1007/s40435-022-01054-9
[research_jafari_spong_2017]: https://doi.org/10.23919/acc.2017.7963805
[research_jaffe_1972]: https://doi.org/10.2514/6.1972-983
[research_jaffrezic_ruetten_2015]: https://doi.org/10.2514/6.2015-2949
[research_jaganraj_velu_2019]: https://doi.org/10.4273/ijvss.11.2.05
[research_jain_singla_2025]: https://doi.org/10.2514/6.2025-0464
[research_jain_sitaram_2015]: https://doi.org/10.1155/2015/628632
[research_jamesfstewart_1992]: https://ntrs.nasa.gov/citations/19930027279
[research_jamesfstewart_frankwburchamjr_1992]: https://ntrs.nasa.gov/citations/19920018344
[research_jameson_2009]: https://doi.org/10.21236/ada500380
[research_jansen_1980]: https://doi.org/10.2514/6.1980-1568
[research_jansen_vankampen_2025]: https://doi.org/10.2514/6.2025-2794
[research_jardin_mueller_2009]: https://doi.org/10.2514/1.34015
[research_jarrah_1989]: https://doi.org/10.2514/6.1989-295
[research_jategaonkar_monnich_1997]: https://doi.org/10.2514/2.2169
[research_jayaraman_gaurav_2022]: https://doi.org/10.2514/6.2022-0751
[research_jayaraman_ghosh_2021]: https://doi.org/10.1109/anzcc53563.2021.9628256
[research_jayaraman_giri_2021]: https://doi.org/10.1109/icuas51884.2021.9476803
[research_jeffreymmaddalon_kurtaswieringa_2021]: https://ntrs.nasa.gov/citations/20205011606
[research_jeffrie_rolston_1972]: https://doi.org/10.2514/6.1972-761
[research_jenkins_2008]: https://doi.org/10.21236/ada478613
[research_jenney_1979]: https://doi.org/10.21236/ada080133
[research_jenney_1980]: https://doi.org/10.21236/ada091559
[research_jenney_schreadley_1982]: https://doi.org/10.21236/ada117244
[research_jentys_breitsamter_2023]: https://doi.org/10.1016/j.ast.2023.108652
[research_jentzsch_taubert_2017]: https://doi.org/10.2514/6.2017-3042
[research_jentzsch_taubert_2019]: https://doi.org/10.2514/1.j056962
[research_jeong_jeong_2024]: https://doi.org/10.2514/6.2024-2566
[research_jeong_kim_2024]: https://doi.org/10.5302/j.icros.2024.23.0206
[research_jeong_lee_2015]: https://doi.org/10.2514/1.c032747
[research_jeong_park_2018]: https://doi.org/10.1155/2018/5435837
[research_jesudasan_doherty_2026]: https://doi.org/10.1016/j.ast.2025.110727
[research_jewell_heffley_1979]: https://doi.org/10.2514/3.58536
[research_jewellwf_1982]: https://ntrs.nasa.gov/citations/19820026185
[research_ji_avedisov_2025]: https://doi.org/10.1080/00423114.2025.2537409
[research_ji_chen_2022]: https://doi.org/10.1109/ccdc55256.2022.10034235
[research_ji_kim_2021]: https://doi.org/10.3390/aerospace8050126
[research_ji_lu_2022]: https://doi.org/10.1016/j.ast.2022.107501
[research_jiang_li_2025]: https://doi.org/10.1007/978-981-96-2268-9_44
[research_jiang_parimi_2021]: https://doi.org/10.1109/naecon49338.2021.9696437
[research_jiang_zhang_2019]: https://doi.org/10.23919/chicc.2019.8866455
[research_jianhong_yanxiang_2026]: https://doi.org/10.1108/aeat-01-2025-0009
[research_jianliangwang_sundararajan_1994]: https://doi.org/10.1109/cca.1994.381242
[research_jianminwang_jinbowang_2016]: https://doi.org/10.1109/cgncc.2016.7828759
[research_jiechen_1995]: https://doi.org/10.1109/9.467680
[research_jiechen_1998]: https://doi.org/10.1109/9.661594
[research_jiguangli_xinchen_2016]: https://doi.org/10.1109/cgncc.2016.7828811
[research_jimenez_faerevaag_2016]: https://doi.org/10.15394/ijaaa.2016.1118
[research_jimeneze_icaza_2000]: https://doi.org/10.1016/s1474-6670(17)35476-9
[research_jin_liao_2020]: https://doi.org/10.2514/6.2020-2556
[research_jin_song_2018]: https://doi.org/10.1109/icarcv.2018.8581064
[research_jingwei_jiaming_2020]: https://doi.org/10.1109/icmeas51739.2020.00036
[research_jo_choi_2018]: https://doi.org/10.14257/ijca.2018.11.10.01
[research_jo_park_2015]: https://doi.org/10.2514/6.2015-3235
[research_jo_park_2016]: https://doi.org/10.2514/6.2016-0163
[research_johnsen_runnels_2022]: https://doi.org/10.3390/app12167961
[research_johnson_1940]: https://doi.org/10.4271/400149
[research_johnson_1972]: https://doi.org/10.21236/ad0754909
[research_johnson_1986]: https://doi.org/10.23919/acc.1986.4789000
[research_johnsonjljr_newsomwa_1980]: https://ntrs.nasa.gov/citations/19800059132
[research_johnsonjosephl_1949]: https://ntrs.nasa.gov/citations/20090026465
[research_johnston_ashkenas_1974]: https://doi.org/10.21236/ada014366
[research_johnston_culver_1965]: https://doi.org/10.21236/ad0622578
[research_johnston_hogge_1974]: https://doi.org/10.2514/6.1974-792
[research_johnston_hogge_1976]: https://doi.org/10.2514/3.58639
[research_johnston_myers_1983]: https://ntrs.nasa.gov/citations/19890004857
[research_johnvfoster_davidchartman_2017]: https://ntrs.nasa.gov/citations/20170006073
[research_jones_1995]: https://doi.org/10.2514/3.46791
[research_jones_hunter_1993]: https://doi.org/10.1007/bf00203126
[research_jones_milholen_2017]: https://doi.org/10.2514/6.2017-3044
[research_jonesrt_1979]: https://ntrs.nasa.gov/citations/19800006774
[research_joosten_stroosma_2023]: https://doi.org/10.2514/6.2023-0906
[research_jordan_1974]: https://doi.org/10.2514/6.1974-941
[research_jordanthomas_langfordwilliam_2004]: https://ntrs.nasa.gov/citations/20040085988
[research_jordanthomasl_langfordwilliamm_2005]: https://ntrs.nasa.gov/citations/20050232785
[research_jorgensenlh_1977]: https://ntrs.nasa.gov/citations/19770026166
[research_jorgensenlh_1979]: https://ntrs.nasa.gov/citations/19790013852
[research_josephrchambers_1988]: https://ntrs.nasa.gov/citations/19880051465
[research_joshi_rickard_1981]: https://doi.org/10.2514/6.1981-1887
[research_jothiraj_miles_2019]: https://doi.org/10.1109/icuas.2019.8798234
[research_jothiraj_sharf_2020]: https://doi.org/10.1109/icuas48674.2020.9214036
[research_joy_ibrahim_2016]: https://doi.org/10.2514/6.2016-3949
[research_jugo_2001]: https://doi.org/10.23919/ecc.2001.7076341
[research_juhasz_celi_2022]: https://doi.org/10.4050/jahs.67.022003
[research_juhasz_xin_2020]: https://doi.org/10.4050/f-0076-2020-16291
[research_juliana_chu_2004]: https://doi.org/10.2514/6.2004-5330
[research_jun_2024]: https://doi.org/10.1049/icp.2024.1652
[research_junfeng_wuzhou_2017]: https://doi.org/10.1109/iaeac.2017.8053978
[research_junfeng_wuzhou_2020]: https://doi.org/10.1109/icus50048.2020.9274833
[research_jung_baeder_2023]: https://doi.org/10.2514/1.c037124
[research_juniorkuitche_yanezbadillo_2024]: https://doi.org/10.1109/uvs59630.2024.10467044
[research_junnarkar_seiler_2026]: https://doi.org/10.1109/lcsys.2026.3701072
[research_jusko_jones_2022]: https://doi.org/10.4050/f-0078-2022-0016
[research_jyothy_johnwessley_2023]: https://doi.org/10.1108/ijius-11-2022-0131
[research_kadosh_cukurel_2016]: https://doi.org/10.1115/gt2016-56274
[research_kaletka_fu_1993]: https://doi.org/10.2514/6.1993-3635
[research_kalyankar_pompe_2024]: https://doi.org/10.2514/6.2024-3758
[research_kamath_sivakumar_2025]: https://doi.org/10.1109/icuas65942.2025.11007914
[research_kamel_ghamry_2015]: https://doi.org/10.1109/icuas.2015.7152346
[research_kamel_ghamry_2016]: https://doi.org/10.1109/icuas.2016.7502638
[research_kaminetovyhaber_bendrickgregga_2008]: https://ntrs.nasa.gov/citations/20090001293
[research_kamiyama_yamazaki_2020]: https://doi.org/10.1299/jsmehs.2020.57.n011
[research_kammer_2025]: https://doi.org/10.23919/acc63710.2025.11107654
[research_kan_yao_2023]: https://doi.org/10.1016/j.ast.2023.108705
[research_kanai_nikiforuk_1982]: https://doi.org/10.2514/6.1982-1349
[research_kanai_nikiforuk_1990]: https://doi.org/10.2514/6.1990-3409
[research_kaneba_mu_2022]: https://doi.org/10.1016/j.amc.2021.126714
[research_kang_park_2016]: https://doi.org/10.5139/ijass.2016.17.1.120
[research_kanneganti_charan_2022]: https://doi.org/10.47893/gret.2022.1085
[research_kao_1975]: https://doi.org/10.2514/3.44428
[research_kao_anderson_1981]: https://doi.org/10.2514/6.1981-2419
[research_kapuscinski_szczerba_2020]: https://doi.org/10.3390/s20082401
[research_karabetsky_2018]: https://doi.org/10.18372/1990-5548.56.12938
[research_karali_demirezen_2020]: https://doi.org/10.2514/6.2020-1288
[research_karimikelayeh_djavareshkian_2024]: https://doi.org/10.1061/jaeeez.aseng-5073
[research_karmah_2018]: https://doi.org/10.19080/raej.2018.02.555598
[research_karn_kumar_2021]: https://doi.org/10.14429/dsj.71.15959
[research_karthikeyan_ajay_2024]: https://doi.org/10.1063/5.0196198
[research_kase_fujita_2021]: https://doi.org/10.1299/jsmemecj.2021.s055-26
[research_kase_mizoguchi_2023]: https://doi.org/10.2514/6.2023-2279
[research_kashikawa_akagi_1995]: https://doi.org/10.2514/6.1995-2749
[research_kastner_epple_2021]: https://doi.org/10.1115/imece2021-69672
[research_katayanagi_2001]: https://doi.org/10.2514/2.4688
[research_katayanagi_2004]: https://doi.org/10.2514/6.2004-4998
[research_katsanikakis_bekiarisliberis_2025]: https://doi.org/10.23919/ecc65951.2025.11186990
[research_katsuyama_sato_2023]: https://doi.org/10.1109/globecom54140.2023.10437076
[research_katz_2017]: https://doi.org/10.2514/1.c034373
[research_kaufman_berry_1976]: https://doi.org/10.1016/0005-1098(76)90038-8
[research_kauser_burcham_2001]: https://doi.org/10.2514/6.2001-1115
[research_kaygan_ulusoy_2018]: https://doi.org/10.30518/jav.482507
[research_kazarin_golubev_2016]: https://doi.org/10.2514/6.2016-3884
[research_kazarin_mackunis_2017]: https://doi.org/10.2514/6.2017-3730
[research_kc_ngo_2019]: https://doi.org/10.2514/6.2019-1947
[research_keidel_fasel_2019]: https://doi.org/10.2514/6.2019-0854
[research_keidel_fasel_2020]: https://doi.org/10.2514/1.c035606
[research_keldysh_1958]: https://doi.org/10.1016/0021-8928(58)90091-1
[research_keller_mckillipjr_2026]: https://doi.org/10.4050/f-0082-2026-0225
[research_kellett_1996]: https://doi.org/10.1049/cp:19960650
[research_kellett_baguley_1996]: https://doi.org/10.2514/6.1996-3929
[research_kellock_miller_1971]: https://doi.org/10.21236/ad0742232
[research_kellstrom_1936]: https://doi.org/10.1103/physrev.50.190
[research_kemper_cotting_2016]: https://doi.org/10.2514/6.2016-1664
[research_kentfield_1975]: https://doi.org/10.2514/3.44486
[research_kentfield_1975_b]: https://doi.org/10.2514/3.44483
[research_kerney_white_1975]: https://doi.org/10.21236/ada023995
[research_keshmiri_lan_2017]: https://doi.org/10.1108/aeat-11-2014-0181
[research_key_1971]: https://doi.org/10.21236/ad0725746
[research_key_1982]: https://doi.org/10.2514/3.57366
[research_keyes_1927]: https://doi.org/10.1515/zpch-1927-0174
[research_khalid_2016]: https://doi.org/10.1115/gt2016-57724
[research_khalid_2017]: https://doi.org/10.1115/1.4037316
[research_khamvilai_huang_2024]: https://doi.org/10.1109/icuas60882.2024.10557076
[research_khan_2019]: https://doi.org/10.18178/ijmmm.2019.7.5.464
[research_khan_2023]: https://doi.org/10.2514/6.2023-4803
[research_khan_iqbal_2022]: https://doi.org/10.2514/6.2022-4202
[research_khan_nahon_2015]: https://doi.org/10.1109/icuas.2015.7152411
[research_kharchenko_kuzmenko_2017]: https://doi.org/10.1109/apuavd.2017.8308789
[research_kharchenko_matiychyk_2017]: https://doi.org/10.1109/apuavd.2017.8308771
[research_kharitonov_1999]: https://doi.org/10.1016/s1367-5788(99)90087-1
[research_kharrat_2024]: https://doi.org/10.1002/acs.3936
[research_khouloud_ali_2023]: https://doi.org/10.1016/j.jprocont.2023.103126
[research_kidd_bull_1963]: https://doi.org/10.21236/ad0400265
[research_kieferjm_johnsonmd_2016]: https://ntrs.nasa.gov/citations/20160001833
[research_kiely_agarwal_2023]: https://doi.org/10.2514/6.2023-4373
[research_kigotho_bodylski_2022]: https://doi.org/10.2514/1.c036582
[research_kikkawa_uchiyama_2017]: https://doi.org/10.1109/red-uas.2017.8101677
[research_kikkawa_uchiyama_2017_b]: https://doi.org/10.1109/icuas.2017.7991508
[research_kikuchi_misaka_2016]: https://doi.org/10.1080/10618562.2016.1198782
[research_kim_1995]: https://doi.org/10.2514/3.21529
[research_kim_2023]: https://doi.org/10.1002/asjc.3101
[research_kim_jung_2015]: https://doi.org/10.1109/icuas.2015.7152335
[research_kim_koh_2025]: https://doi.org/10.1007/s42405-025-01059-6
[research_kim_kunz_2016]: https://doi.org/10.2514/6.2016-3542
[research_kim_kunz_2017]: https://doi.org/10.2514/1.g002306
[research_kim_lee_2003]: https://doi.org/10.2514/2.5103
[research_kim_oh_2017]: https://doi.org/10.1109/icuas.2017.7991455
[research_kim_sohn_2022]: https://doi.org/10.2514/6.2022-3241
[research_kimathi_lantos_2024]: https://doi.org/10.12700/aph.21.2.2024.2.16
[research_kimberlin_2001]: https://doi.org/10.2514/6.2001-5270
[research_kingcombe_dunning_1980]: https://doi.org/10.1115/80-gt-141
[research_kirkdonnb_1961]: https://ntrs.nasa.gov/citations/20040006368
[research_kirsch_fathi_2025]: https://doi.org/10.1115/1.4071802
[research_kish_leggett_1996]: https://doi.org/10.2514/6.1996-3431
[research_kish_mosle_1997]: https://doi.org/10.21236/ada286959
[research_kish_mosleiii_1997]: https://doi.org/10.2514/6.1997-3703
[research_kisslinger_wendl_1971]: https://doi.org/10.21236/ad0727762
[research_kistyarev_wang_2025]: https://doi.org/10.1007/s42496-025-00249-5
[research_kiyak_ermeydan_2018]: https://doi.org/10.11128/sne.28.sn.10422
[research_klafin_1988]: https://doi.org/10.2514/6.1988-4499
[research_klauck_kessler_2025]: https://doi.org/10.4050/f-0081-2025-0197
[research_klein_1977]: https://doi.org/10.2514/6.1977-1123
[research_klein_1978]: https://doi.org/10.2514/6.1978-1344
[research_klein_1989]: https://doi.org/10.2514/6.1989-3356
[research_klein_kashawlic_2016]: https://doi.org/10.4050/f-0072-2016-11554
[research_klein_krainski_2017]: https://doi.org/10.4050/sm_2017_hq-1572
[research_klein_murphy_2001]: https://doi.org/10.2514/6.2001-4016
[research_kleinrw_lapinsm_1982]: https://ntrs.nasa.gov/citations/19820036249
[research_klimas_kilikevicius_2024]: https://doi.org/10.5755/e01.2351-7034.2024.p871-876
[research_klinarwalterj_healyfrederickm_1955]: https://ntrs.nasa.gov/citations/20050030056
[research_klose_jacobs_2018]: https://doi.org/10.2514/6.2018-3731
[research_klyde_aponso_1995]: https://doi.org/10.2514/6.1995-3205
[research_klyde_brenner_2001]: https://doi.org/10.2514/6.2001-4009
[research_klyde_lampton_2021]: https://doi.org/10.2514/6.2021-0178
[research_klyde_mitchell_2020]: https://doi.org/10.4050/f-0076-2020-16397
[research_klyde_schulze_2018]: https://doi.org/10.2514/6.2018-0299
[research_knightondonnal_1992]: https://ntrs.nasa.gov/citations/19930029267
[research_ko_kang_2019]: https://doi.org/10.5139/jksas.2019.47.2.114
[research_kochersberger_ohanian_2017]: https://doi.org/10.1177/1045389x17698590
[research_kocurek_durham_1997]: https://doi.org/10.2514/6.1997-3777
[research_koduri_rodriguezayerbe_2016]: https://doi.org/10.1109/cdc.2016.7798610
[research_koduri_rodriguezayerbe_2016_b]: https://doi.org/10.1109/icstcc.2016.7790767
[research_kofman_becus_1996]: https://doi.org/10.2514/3.46996
[research_kogler_quam_1983]: https://doi.org/10.2514/6.1983-366
[research_koh_1968]: https://doi.org/10.2514/6.1968-715
[research_kohlman_1977]: https://doi.org/10.4271/770441
[research_kohlman_1979]: https://doi.org/10.2514/3.58513
[research_kohlman_brainerd_1974]: https://doi.org/10.2514/3.60366
[research_kohnhorst_magnacca_1980]: https://doi.org/10.21236/ada094688
[research_kojima_hidaka_2024]: https://doi.org/10.2514/6.2024-0906
[research_kokolios_1994]: https://doi.org/10.2514/6.1994-10
[research_konar_mahesh_1974]: https://doi.org/10.21236/ada002320
[research_konatala_milz_2024]: https://doi.org/10.2514/1.g008321
[research_konatala_vankampen_2021]: https://doi.org/10.2514/6.2021-0883
[research_konishi_kojima_2023]: https://doi.org/10.2514/6.2023-1758
[research_koopman_zammitmangion_2024]: https://doi.org/10.2514/6.2024-4648
[research_kopecki_2016]: https://doi.org/10.1108/aeat-10-2012-0187
[research_korkischko_konrath_2017]: https://doi.org/10.2514/1.c033941
[research_korsun_mounghtang_2023]: https://doi.org/10.3934/mina.2024003
[research_korsun_stulovskii_2018]: https://doi.org/10.1088/1757-899x/312/1/012015
[research_koryanov_kukharenko_2023]: https://doi.org/10.18698/2308-6033-2023-2-2254
[research_kostic_simonovic_2024]: https://doi.org/10.3390/aerospace11030223
[research_kotikalpudi_pfifer_2015]: https://doi.org/10.2514/6.2015-2854
[research_kotsabasis_1981]: https://ntrs.nasa.gov/citations/19810008519
[research_kou_wang_2021]: https://doi.org/10.1109/tte.2021.3068724
[research_kouser_aliyu_2024]: https://doi.org/10.1109/mepe64515.2024.11115296
[research_kouser_kurtulus_2024]: https://doi.org/10.1109/access.2024.3413153
[research_kouvaritakis_murray_1979]: https://doi.org/10.1080/00207177908922702
[research_kowal_2002]: https://doi.org/10.5589/q02-020
[research_kraft_2018]: https://doi.org/10.2514/6.2018-2853
[research_kramer_williams_2018]: https://doi.org/10.2514/6.2018-3411
[research_kramerbrian_smithbrooke_1994]: https://ntrs.nasa.gov/citations/19950007840
[research_krause_funke_2024]: https://doi.org/10.1109/aero58975.2024.10521033
[research_kriechbaum_stineman_1972]: https://doi.org/10.2514/3.58994
[research_krimphove_schutt_2023]: https://doi.org/10.1109/ccta54093.2023.10252262
[research_krishnamurthy_luckner_2017]: https://doi.org/10.2514/6.2017-4332
[research_krohn_1988]: https://doi.org/10.21236/ada396413
[research_kuang_zhu_2015]: https://doi.org/10.1007/s11432-015-5353-3
[research_kubo_1999]: https://doi.org/10.1080/002071799221037
[research_kuchar_2018]: https://doi.org/10.2514/6.2018-0126
[research_kuchar_looye_2018]: https://doi.org/10.2514/6.2018-0386
[research_kuester_borgoltz_2016]: https://doi.org/10.2514/6.2016-3880
[research_kuhn_1981]: https://doi.org/10.21236/ada100386
[research_kumar_2015]: https://doi.org/10.1109/epetsg.2015.7510085
[research_kumar_bhargavapuri_2020]: https://doi.org/10.23919/acc45564.2020.9147794
[research_kumar_bombuwela_2018]: https://doi.org/10.1109/anzcc.2018.8606571
[research_kumar_ghosh_2017]: https://doi.org/10.2514/6.2017-0936
[research_kumar_ghosh_2018]: https://doi.org/10.2514/6.2018-0768
[research_kumar_ghosh_2018_b]: https://doi.org/10.15866/irease.v11i6.14521
[research_kumar_ghosh_2018_c]: https://doi.org/10.1177/0954410018791621
[research_kumar_ghosh_2023]: https://doi.org/10.1108/aeat-09-2019-0179
[research_kumar_hote_2022]: https://doi.org/10.1109/cdc51059.2022.9992756
[research_kumar_kothari_2024]: https://doi.org/10.2514/6.2024-0748
[research_kumar_kumar_2022]: https://doi.org/10.4018/ijsda.302634
[research_kumar_mittal_2026]: https://doi.org/10.2514/6.2026-4389
[research_kumar_prakash_2022]: https://doi.org/10.1109/iconat53423.2022.9726117
[research_kumar_rao_2004]: https://doi.org/10.14429/dsj.54.2041
[research_kumar_shankar_2024]: https://doi.org/10.4271/2023-01-5143
[research_kumar_srivastava_2018]: https://doi.org/10.1002/acs.2916
[research_kumar_steck_2015]: https://doi.org/10.2514/6.2015-1803
[research_kumar_tomar_2015]: https://doi.org/10.4271/2015-01-2576
[research_kumarg_mukherjee_2024]: https://doi.org/10.1134/s0015462824602043
[research_kumargupta_aaswathanaray_2018]: https://doi.org/10.14419/ijet.v7i4.25.22240
[research_kumari_raghunath_2016]: https://doi.org/10.18535/ijecs/v5i6.05
[research_kumtepe_pollack_2022]: https://doi.org/10.2514/6.2022-1597
[research_kunwar_chakraborty_2025]: https://doi.org/10.2514/6.2025-0739
[research_kunwar_putra_2026]: https://doi.org/10.2514/6.2026-2288
[research_kurade_venkatakrishnan_2021]: https://doi.org/10.1017/aer.2021.99
[research_kurbanismailov_tarlanov_2021]: https://doi.org/10.32362/2500-316x-2021-9-1-58-72
[research_kurtulus_2019]: https://doi.org/10.1177/1756829319890609
[research_kurtulus_2021]: https://doi.org/10.1177/17568293211055653
[research_kus_ergazi_2025]: https://doi.org/10.2514/6.2025-3447
[research_kutschera_render_1999]: https://doi.org/10.2514/6.1999-4020
[research_kuwamura_hara_2017]: https://doi.org/10.1299/jsmetokai.2017.66.322
[research_kuzu_bogosyan_2015]: https://doi.org/10.15837/ijccc.2016.1.1577
[research_kwiek_2019]: https://doi.org/10.1108/aeat-01-2018-0032
[research_lacaille_loro_2016]: https://doi.org/10.1109/ftc.2016.7821629
[research_lackey_hadfield_1992]: https://doi.org/10.2514/6.1992-4107
[research_lafflitto_anderson_2018]: https://doi.org/10.1109/mcs.2018.2810559
[research_lai_kamaruddin_2018]: https://doi.org/10.1088/1757-899x/370/1/012055
[research_laiosa_1985]: https://ntrs.nasa.gov/citations/19850037442
[research_laitone_1947]: https://doi.org/10.2514/8.1476
[research_laitone_lin_1972]: https://doi.org/10.2514/6.1972-951
[research_laitone_lin_1973]: https://doi.org/10.2514/3.60207
[research_lakkur_schmidt_2025]: https://doi.org/10.1109/urtc68753.2025.11533008
[research_lallemand_2000]: https://doi.org/10.51257/a-v1-be8159
[research_lam_stollenwerk_1966]: https://doi.org/10.2514/6.1966-771
[research_lampard_1978]: https://doi.org/10.2514/6.1978-1020
[research_lamperski_2022]: https://doi.org/10.1109/cdc51059.2022.9992994
[research_lampton_klyde_2024]: https://doi.org/10.2514/1.g008058
[research_lampton_klyde_2024_b]: https://doi.org/10.2514/6.2024-2479
[research_landa_klug_2018]: https://doi.org/10.2514/6.2018-4157
[research_landgraf_1964]: https://doi.org/10.2514/6.1964-288
[research_landgraf_1965]: https://doi.org/10.2514/3.43632
[research_lane_carignan_2001]: https://doi.org/10.1117/12.417326
[research_lang_li_2024]: https://doi.org/10.1109/ccdc62350.2024.10587543
[research_langan_samuels_1995]: https://doi.org/10.2514/6.1995-442
[research_lanserwendyr_meynlarrya_1992]: https://ntrs.nasa.gov/citations/19920062959
[research_lanteigne_oreilly_2020]: https://doi.org/10.1109/icuas48674.2020.9213950
[research_lapinsm_kleinrw_1982]: https://ntrs.nasa.gov/citations/19820055547
[research_larsen_1975]: https://doi.org/10.4271/751109
[research_larson_1986]: https://doi.org/10.2514/6.1986-2237
[research_larsonrichardr_burkenjohnj_2009]: https://ntrs.nasa.gov/citations/20090029243
[research_larsson_2025]: https://doi.org/10.3384/wcc215.1202
[research_larsson_sobron_2020]: https://doi.org/10.3390/aerospace7090135
[research_lateral_control_2025]: https://doi.org/10.37285/bsp.sacad2025.09
[research_laudeman_1972]: https://doi.org/10.2514/6.1972-780
[research_laughterseana_2012]: https://ntrs.nasa.gov/citations/20120016700
[research_lavretsky_2019]: https://doi.org/10.2514/1.g004328
[research_lavretsky_misovec_2002]: https://doi.org/10.2514/6.2002-3429
[research_lawrence_mills_2002]: https://doi.org/10.2514/6.2002-168
[research_lawrence_theodore_2018]: https://doi.org/10.1017/aer.2018.43
[research_laytongp_1974]: https://ntrs.nasa.gov/citations/19740060853
[research_lebacqzjv_1974]: https://ntrs.nasa.gov/citations/19740017465
[research_lecuyer_1970]: https://doi.org/10.2514/6.1970-612
[research_lee_1946]: https://doi.org/10.1017/s0368393100120863
[research_lee_1947]: https://doi.org/10.1017/s036839310011185x
[research_lee_2016]: https://doi.org/10.1115/1.4032301
[research_lee_2024]: https://doi.org/10.54097/b56kmh05
[research_lee_benedict_2021]: https://doi.org/10.4050/f-0077-2021-16863
[research_lee_chang_1998]: https://doi.org/10.1109/acc.1998.694683
[research_lee_han_2019]: https://doi.org/10.1007/s42405-019-00215-z
[research_lee_hedrick_1994]: https://doi.org/10.1115/1.2899238
[research_lee_horn_2026]: https://doi.org/10.4050/sm-2026-vlada-5203
[research_lee_huang_2021]: https://doi.org/10.2514/6.2021-1943
[research_lee_huang_2021_b]: https://doi.org/10.2514/6.2021-2610
[research_lee_kawai_2015]: https://doi.org/10.1063/1.4913500
[research_lee_kawai_2015_b]: https://doi.org/10.1615/tsfp9.620
[research_lee_kim_2001]: https://doi.org/10.2514/2.4794
[research_lee_kim_2020]: https://doi.org/10.1007/s12555-018-9403-7
[research_lee_kim_2021]: https://doi.org/10.1155/2021/5513337
[research_lee_ko_2017]: https://doi.org/10.1115/1.4035639
[research_lee_ko_2018]: https://doi.org/10.1115/1.4039232
[research_lee_lan_1992]: https://doi.org/10.2514/3.46191
[research_lee_marnineaumes_1996]: https://doi.org/10.2514/6.1996-2510
[research_lee_nonomura_2015]: https://doi.org/10.2514/1.c032721
[research_lee_nonomura_2015_b]: https://doi.org/10.1115/ajkfluids2015-13489
[research_lee_rodchenko_2003]: https://doi.org/10.2514/6.2003-5310
[research_lee_saj_2021]: https://doi.org/10.2514/6.2021-3218
[research_lee_shin_2001]: https://doi.org/10.1016/s0967-0661(00)00090-3
[research_lee_song_2018]: https://doi.org/10.2514/1.j056598
[research_lee_tai_2024]: https://doi.org/10.2514/6.2024-4614
[research_lee_vankampen_2021]: https://doi.org/10.2514/6.2021-0392
[research_lee_vining_2018]: https://doi.org/10.2514/6.2018-4171
[research_leehenrya_1952]: https://ntrs.nasa.gov/citations/20050029463
[research_leehenrya_1963]: https://ntrs.nasa.gov/citations/19630002367
[research_leehenrya_libbeycharlese_1961]: https://ntrs.nasa.gov/citations/19980227452
[research_legowo_sulaeman_2019]: https://doi.org/10.1109/icaset.2019.8714531
[research_lei_dong_2025]: https://doi.org/10.1117/12.3081983
[research_lei_liu_2017]: https://doi.org/10.1177/0954410017727025
[research_leishman_2026]: https://doi.org/10.2514/1.c039163
[research_leonardrg_arnettem_1980]: https://ntrs.nasa.gov/citations/19810003590
[research_lerro_brandl_2020]: https://doi.org/10.3390/aerospace7050063
[research_lesalli_cahyono_2020]: https://doi.org/10.28989/senatik.v6i0.402
[research_leshikar_eves_2021]: https://doi.org/10.1109/icuas51884.2021.9476871
[research_lessinghenryc_butlerjamesk_1959]: https://ntrs.nasa.gov/citations/19980228050
[research_lestari_ridwan_2025]: https://doi.org/10.21070/jeeeu.v9i2.1710
[research_leung_moszczynski_2019]: https://doi.org/10.2514/6.2019-0013
[research_leung_redonnet_2022]: https://doi.org/10.2514/6.2022-2617
[research_levi_nelson_1963]: https://doi.org/10.2514/6.1963-1801
[research_levison_1982]: https://doi.org/10.2514/3.57394
[research_levison_papazian_1987]: https://doi.org/10.2514/6.1987-2371
[research_levy_2003]: https://doi.org/10.2514/6.2003-3412
[research_levyjr_tobak_1970]: https://doi.org/10.2514/6.1970-205
[research_leyiwang_jifengzhang_2001]: https://doi.org/10.1109/acc.2001.945742
[research_leylek_costello_2015]: https://doi.org/10.2514/1.c033056
[research_li_2024]: https://doi.org/10.1109/irac63143.2024.10871858
[research_li_bai_2022]: https://doi.org/10.2514/1.c036413
[research_li_cai_2026]: https://doi.org/10.1088/1742-6596/3256/1/012016
[research_li_dong_2018]: https://doi.org/10.1051/jnwpu/20183650978
[research_li_gao_2025]: https://doi.org/10.1088/1742-6596/3073/1/012018
[research_li_ge_1994]: https://doi.org/10.2514/6.1994-3494
[research_li_gu_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001462
[research_li_guo_2016]: https://doi.org/10.1108/aeat-12-2013-0234
[research_li_han_2026]: https://doi.org/10.1016/j.displa.2025.103292
[research_li_li_2026]: https://doi.org/10.1016/j.ast.2025.110752
[research_li_lian_2025]: https://doi.org/10.23919/ccc64809.2025.11179660
[research_li_liu_2015]: https://doi.org/10.1109/icuas.2015.7152368
[research_li_liu_2016]: https://doi.org/10.1115/gt2016-57137
[research_li_liu_2021]: https://doi.org/10.1016/j.conengprac.2021.104938
[research_li_ma_2014]: https://doi.org/10.4028/www.scientific.net/amm.472.185
[research_li_nagata_2023]: https://doi.org/10.2514/1.c037253
[research_li_qin_2017]: https://doi.org/10.1109/ccdc.2017.7978762
[research_li_sheng_2026]: https://doi.org/10.3390/aerospace13060552
[research_li_shi_2018]: https://doi.org/10.1088/2058-6272/aacaf0
[research_li_sun_2022]: https://doi.org/10.1109/access.2022.3157878
[research_li_sun_2023]: https://doi.org/10.1088/1742-6596/2472/1/012019
[research_li_vankampen_2024]: https://doi.org/10.23919/ecc64448.2024.10591030
[research_li_wang_2017]: https://doi.org/10.1109/ddcls.2017.8067720
[research_li_xu_2022]: https://doi.org/10.1108/aeat-11-2021-0351
[research_li_yang_2017]: https://doi.org/10.2514/1.c033670
[research_li_yang_2017_b]: https://doi.org/10.2514/1.c034293
[research_li_yong_2017]: https://doi.org/10.23919/chicc.2017.8027800
[research_li_yu_2016]: https://doi.org/10.1109/chicc.2016.7553129
[research_li_zhang_2018]: https://doi.org/10.1109/gncc42960.2018.9019083
[research_li_zhang_2019]: https://doi.org/10.2514/6.2019-1214
[research_li_zhang_2024]: https://doi.org/10.3390/aerospace11121020
[research_li_zheng_2024]: https://doi.org/10.1063/5.0216603
[research_liang_2025]: https://doi.org/10.65904/3083-3450.2025.01.03
[research_liang_kou_2026]: https://doi.org/10.1109/tie.2025.3634460
[research_liang_wang_2025]: https://doi.org/10.1117/12.3081984
[research_liang_yang_2022]: https://doi.org/10.2514/1.c036558
[research_liberatori_valorani_2023]: https://doi.org/10.1615/ichmt.thmt-23.700
[research_liborio_pimentel_2025]: https://doi.org/10.1109/iccc65605.2025.11022852
[research_lichota_2016]: https://doi.org/10.15632/jtam-pl.54.1.87
[research_lichota_2023]: https://doi.org/10.1108/aeat-01-2023-0013
[research_lichota_ohme_2016]: https://doi.org/10.2514/6.2016-3704
[research_liem_mader_2015]: https://doi.org/10.1016/j.ast.2015.02.019
[research_liewkh_uripe_2005]: https://ntrs.nasa.gov/citations/20050207438
[research_liewkh_uripe_2005_b]: https://ntrs.nasa.gov/citations/20050188445
[research_liewkh_uripe_2005_c]: https://ntrs.nasa.gov/citations/20050207442
[research_lijewski_1986]: https://doi.org/10.2514/6.1986-1082
[research_lim_hur_2025]: https://doi.org/10.9766/kimst.2025.28.1.092
[research_lim_kurahashi_2026]: https://doi.org/10.2514/6.2026-4553
[research_lin_2025]: https://doi.org/10.5220/0014773000004818
[research_lin_ge_1998]: https://doi.org/10.2514/6.1998-4301
[research_lin_han_1986]: https://doi.org/10.1109/tia.1986.4504680
[research_lin_robinson_1992]: https://doi.org/10.2514/6.1992-2636
[research_lin_rockwell_1995]: https://doi.org/10.2514/3.12325
[research_lin_yeh_1999]: https://doi.org/10.1515/tjj.1999.16.3.127
[research_lin_zhang_2019]: https://doi.org/10.23919/chicc.2019.8865352
[research_lind_protopapas_1977]: https://doi.org/10.1115/77-gt-101
[research_lindberg_pates_2023]: https://doi.org/10.1109/lcsys.2022.3185928
[research_linear_and_1996]: https://doi.org/10.1109/37.526912
[research_linehan_1996]: https://doi.org/10.1049/cp:19960649
[research_linehan_mohseni_2016]: https://doi.org/10.2514/6.2016-1063
[research_ling_1983]: https://doi.org/10.21236/ada176577
[research_littjonathans_sowerst_2012]: https://ntrs.nasa.gov/citations/20120015476
[research_littleboy_smith_1997]: https://doi.org/10.2514/6.1997-3717
[research_liu_2023]: https://doi.org/10.1007/s11424-023-1047-x
[research_liu_2024]: https://doi.org/10.1088/1742-6596/2691/1/012030
[research_liu_2024_b]: https://doi.org/10.12694/scpe.v25i3.2700
[research_liu_an_2024]: https://doi.org/10.1002/asjc.3355
[research_liu_brandel_2004]: https://doi.org/10.2514/6.2004-5002
[research_liu_chen_2016]: https://doi.org/10.2514/1.g001958
[research_liu_di_2024]: https://doi.org/10.1088/1742-6596/2764/1/012019
[research_liu_dong_2019]: https://doi.org/10.1016/j.jfranklin.2018.11.043
[research_liu_gao_2018]: https://doi.org/10.1109/access.2018.2814958
[research_liu_gao_2022]: https://doi.org/10.3390/aerospace9110678
[research_liu_gao_2024]: https://doi.org/10.1002/rnc.7571
[research_liu_hao_2023]: https://doi.org/10.1109/cfasta57821.2023.10243292
[research_liu_hao_2024]: https://doi.org/10.1109/fasta61401.2024.10595103
[research_liu_hu_2014]: https://doi.org/10.2514/6.2014-3015
[research_liu_huang_2017]: https://doi.org/10.1016/j.cja.2017.02.015
[research_liu_jiang_2015]: https://doi.org/10.1016/j.jfranklin.2015.02.026
[research_liu_jiang_2024]: https://doi.org/10.1109/cac63892.2024.10865178
[research_liu_jiao_2017]: https://doi.org/10.1109/iccis.2017.8274866
[research_liu_li_2021]: https://doi.org/10.1016/j.jweia.2021.104726
[research_liu_li_2026]: https://doi.org/10.3390/electronics15163532
[research_liu_li_2026_b]: https://doi.org/10.1109/jiot.2026.3697060
[research_liu_litvinenko_2017]: https://doi.org/10.1137/15m1050239
[research_liu_lu_2024]: https://doi.org/10.1088/1742-6596/2820/1/012003
[research_liu_luo_2016]: https://doi.org/10.2514/6.2016-1039
[research_liu_luo_2018]: https://doi.org/10.1016/j.ast.2017.10.008
[research_liu_luo_2021]: https://doi.org/10.3390/app11041555
[research_liu_luo_2022]: https://doi.org/10.1117/12.2653094
[research_liu_nakata_2018]: https://doi.org/10.1117/12.2296483
[research_liu_shan_2020]: https://doi.org/10.1109/icca51439.2020.9264361
[research_liu_sirignano_2000]: https://doi.org/10.2514/6.2000-741
[research_liu_sun_2018]: https://doi.org/10.1109/gncc42960.2018.9018671
[research_liu_wang_2015]: https://doi.org/10.1016/j.cja.2014.12.013
[research_liu_wang_2022]: https://doi.org/10.23919/ccc55666.2022.9902299
[research_liu_wang_2026]: https://doi.org/10.2514/1.c038847
[research_liu_xiao_2020]: https://doi.org/10.2514/1.j058598
[research_liu_yang_2024]: https://doi.org/10.1186/s42774-024-00180-6
[research_liu_yuan_2016]: https://doi.org/10.1109/icuas.2016.7502543
[research_liu_zhang_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001495
[research_liu_zhang_2022_b]: https://doi.org/10.3390/aerospace9020079
[research_liu_zhang_2023]: https://doi.org/10.1109/cac59555.2023.10451170
[research_liu_zhang_2025]: https://doi.org/10.1063/5.0282257
[research_liu_zheng_2025]: https://doi.org/10.2514/1.c038200
[research_liu_zhou_2018]: https://doi.org/10.1109/ijcnn.2018.8489118
[research_liu_zhu_2021]: https://doi.org/10.1016/j.neunet.2021.06.011
[research_livneh_1995]: https://doi.org/10.2514/3.56682
[research_livneh_1995_b]: https://doi.org/10.2514/6.1995-3307
[research_liyan_sundarajan_2000]: https://doi.org/10.1109/acc.2000.879220
[research_lloydsraja_ali_2017]: https://doi.org/10.1016/j.jprocont.2017.01.007
[research_lockenour_layton_1976]: https://ntrs.nasa.gov/citations/19760042755
[research_loechert_huber_2018]: https://doi.org/10.2514/6.2018-3329
[research_lofthouse_cummings_2015]: https://doi.org/10.2514/6.2015-2875
[research_lofthouse_cummings_2017]: https://doi.org/10.2514/1.c034045
[research_loh_lustyjr_1974]: https://doi.org/10.2514/6.1974-814
[research_long_1968]: https://doi.org/10.2514/6.1968-264
[research_long_2016]: https://doi.org/10.3901/jme.2016.14.079
[research_long_2016_b]: https://doi.org/10.3901/jme.2016.22.101
[research_longlu_turkoglu_2015]: https://doi.org/10.1109/aero.2015.7118952
[research_loo_1969]: https://doi.org/10.1080/00207176908905731
[research_loposerjdan_rumseycharlesb_1954]: https://ntrs.nasa.gov/citations/20030068110
[research_loranchet_tiako_2025]: https://doi.org/10.2514/6.2025-98091
[research_lorell_1989]: https://doi.org/10.21236/ada214500
[research_lorenzetti_nelsen_1969]: https://doi.org/10.2514/3.44042
[research_lorincz_1980]: https://ntrs.nasa.gov/citations/19800022875
[research_loro_lacaille_2017]: https://doi.org/10.1109/aero.2017.7943699
[research_lovellpowellmjr_1954]: https://ntrs.nasa.gov/citations/20050028502
[research_lowry_rich_1978]: https://doi.org/10.21236/ada058906
[research_lowson_riley_1994]: https://doi.org/10.2514/6.1994-3487
[research_lowson_riley_1995]: https://doi.org/10.2514/3.46798
[research_lu_2017]: https://doi.org/10.1109/icctec.2017.00244
[research_lu_martos_2021]: https://doi.org/10.2514/6.2021-0718
[research_lu_turkoglu_2016]: https://doi.org/10.2514/6.2016-1624
[research_lu_turkoglu_2018]: https://doi.org/10.1155/2018/8654031
[research_lu_vankampen_2015]: https://doi.org/10.2514/6.2015-0859
[research_lu_vankampen_2016]: https://doi.org/10.1016/j.conengprac.2016.09.010
[research_lu_wu_2024]: https://doi.org/10.1002/acs.3897
[research_lu_zhang_2015]: https://doi.org/10.1016/j.ssci.2014.12.005
[research_lu_zhang_2016]: https://doi.org/10.1016/j.ssci.2016.06.018
[research_lu_zhang_2019]: https://doi.org/10.1016/j.cja.2019.09.010
[research_luattnguyen_williampgilbert_1980]: https://ntrs.nasa.gov/citations/19800020743
[research_lubing_yang_2017]: https://doi.org/10.23919/chicc.2017.8027532
[research_lucarini_dirito_2025]: https://doi.org/10.3390/act14080407
[research_lucas_1978]: https://doi.org/10.21236/adb028240
[research_luckert_1973]: https://doi.org/10.2514/3.61951
[research_luckring_taylor_2022]: https://doi.org/10.2514/6.2022-0025
[research_luckringjamesm_foxcharleshjr_1989]: https://ntrs.nasa.gov/citations/19910014821
[research_lueckhof_stumpf_2018]: https://doi.org/10.2514/6.2018-0043
[research_luhanga_mwandosya_1986]: https://doi.org/10.52339/tjet.v10i2.78
[research_lungu_lungu_2015]: https://doi.org/10.1002/asjc.1133
[research_lungu_lungu_2016]: https://doi.org/10.1016/j.neucom.2015.12.118
[research_lungu_lungu_2016_b]: https://doi.org/10.1016/j.neucom.2015.06.084
[research_luo_cui_2025]: https://doi.org/10.3390/drones9100689
[research_luo_du_2019]: https://doi.org/10.3390/electronics8090931
[research_luo_wang_2017]: https://doi.org/10.2514/6.2017-2443
[research_luo_zhang_2022]: https://doi.org/10.1109/access.2022.3175164
[research_luria_2017]: https://doi.org/10.4050/sm_2017_hq-3965
[research_lusardi_2023]: https://doi.org/10.4050/sm_2023_hq-1186
[research_luu_ochi_2023]: https://doi.org/10.2322/tastj.21.1
[research_luz_silva_2023]: https://doi.org/10.1109/access.2023.3240307
[research_ly_2002]: https://doi.org/10.2514/6.2002-5001
[research_lynch_2012]: https://doi.org/10.21236/ada570367
[research_lytovchenko_2026]: https://doi.org/10.62717/3083-7057-2026-1-040
[research_lyu_gong_2022]: https://doi.org/10.1155/2022/2490675
[research_lyu_sun_2024]: https://doi.org/10.2514/6.2024-3979
[research_lyu_ye_2023]: https://doi.org/10.3390/app13116598
[research_lyu_yin_2023]: https://doi.org/10.3390/app13063518
[research_lyu_zhang_2023]: https://doi.org/10.1016/j.ast.2023.108384
[research_lyul_hojk_1986]: https://ntrs.nasa.gov/citations/19870000967
[research_ma_2019]: https://doi.org/10.23919/chicc.2019.8866165
[research_ma_2025]: https://doi.org/10.5220/0014450700004861
[research_ma_dong_2019]: https://doi.org/10.1109/access.2019.2949061
[research_ma_du_2015]: https://doi.org/10.1109/ccdc.2015.7162865
[research_ma_hui_2023]: https://doi.org/10.23919/ccc58697.2023.10241099
[research_ma_li_2008]: https://doi.org/10.1109/isscaa.2008.4776304
[research_ma_peng_2021]: https://doi.org/10.1016/j.ast.2021.107204
[research_ma_shi_2020]: https://doi.org/10.2514/6.2020-2508
[research_ma_yao_2025]: https://doi.org/10.1016/j.neunet.2025.107563
[research_ma_yu_2024]: https://doi.org/10.3390/drones8020058
[research_ma_zhu_2019]: https://doi.org/10.1017/aer.2018.167
[research_ma_zhu_2019_b]: https://doi.org/10.3390/app9204236
[research_maadani_lopezmuro_2023]: https://doi.org/10.2514/6.2023-2243
[research_macallister_1955]: https://doi.org/10.21236/ad0062045
[research_mace_smereczniak_1989]: https://doi.org/10.2514/6.1989-2816
[research_maeda_vidyasagar_1985]: https://doi.org/10.1016/0167-6911(85)90010-6
[research_magrini_buosi_2021]: https://doi.org/10.2514/6.2021-0606
[research_mahesh_shah_2023]: https://doi.org/10.2514/6.2023-4346
[research_mahgoub_cortelezzi_2020]: https://doi.org/10.2514/1.j058021
[research_mahns_amitay_2025]: https://doi.org/10.2514/6.2025-1871
[research_mahulikar_rastogi_2022]: https://doi.org/10.2514/1.c036370
[research_mahulkar_2010]: https://doi.org/10.21236/ada534168
[research_maji_pandi_2024]: https://doi.org/10.1063/5.0195947
[research_makarenko_makarov_2017]: https://doi.org/10.21778/2413-9599-2017-1-96-103
[research_makgantai_subaschandar_2021]: https://doi.org/10.1109/icuas51884.2021.9476801
[research_malaek_sajjadikia_2004]: https://doi.org/10.2514/6.2004-5363
[research_malaek_soltanmohammed_2001]: https://doi.org/10.1016/s1369-8869(00)00024-0
[research_malcolmgn_ngtt_1990]: https://ntrs.nasa.gov/citations/19910063943
[research_malcom_1969]: https://doi.org/10.2514/3.59426
[research_maldonado_sarker_2017]: https://doi.org/10.2514/6.2017-0224
[research_malik_asrar_2018]: https://doi.org/10.15394/ijaaa.2018.1209
[research_malik_masud_2020]: https://doi.org/10.1108/aeat-08-2019-0174
[research_malik_masud_2021]: https://doi.org/10.1108/aeat-04-2021-0136
[research_mallavalli_fekih_2018]: https://doi.org/10.1109/ccta.2018.8511427
[research_mallavalli_fekih_2019]: https://doi.org/10.23919/acc.2019.8815190
[research_mallery_neebe_1965]: https://doi.org/10.2514/6.1965-1206
[research_malloy_chang_1998]: https://doi.org/10.1115/1.2802410
[research_malmuth_wu_1983]: https://doi.org/10.2514/6.1983-184
[research_malpica_lusardi_2013]: https://doi.org/10.21236/ada589936
[research_malpica_suh_2023]: https://doi.org/10.4050/f-0079-2023-18079
[research_mammadova_slavov_2025]: https://doi.org/10.23919/irs64527.2025.11046140
[research_mamou_broughton_2023]: https://doi.org/10.2514/1.c036818
[research_manar_cassell_2016]: https://doi.org/10.2514/6.2016-3633
[research_mandal_gu_2016]: https://doi.org/10.2514/6.2016-0636
[research_mandal_gu_2016_b]: https://doi.org/10.3390/aerospace3040042
[research_mannmichaelj_huffmanjarrettk_1987]: https://ntrs.nasa.gov/citations/19870017441
[research_manoilo_2025]: https://doi.org/10.62717/2221-4550-2025-1-097
[research_manolescu_1994]: https://doi.org/10.2514/6.1994-3528
[research_mansor_nogoud_2015]: https://doi.org/10.1109/iccneee.2015.7381444
[research_mansur_lanteigne_2020]: https://doi.org/10.32393/csme.2020.33
[research_mao_chen_2026]: https://doi.org/10.1016/j.sysconle.2026.106478
[research_mao_gong_2022]: https://doi.org/10.3390/math10183333
[research_maraye_pholdee_2020]: https://doi.org/10.1088/1757-899x/886/1/012026
[research_marchman_1987]: https://doi.org/10.2514/6.1987-2350
[research_marchmaniii_1981]: https://doi.org/10.2514/6.1981-1660
[research_margason_hoad_1980]: https://doi.org/10.2514/3.57883
[research_margetts_bingham_2015]: https://doi.org/10.4271/2015-01-2468
[research_marinoalfreda_mastrocolan_1952]: https://ntrs.nasa.gov/citations/19930083049
[research_markofski_bailey_1999]: https://doi.org/10.2514/6.1999-4005
[research_marques_2013]: https://doi.org/10.14323/ijuseng.2013.5
[research_martin_2025]: https://doi.org/10.4050/sm_handling_2025-5290
[research_martin_lind_2025]: https://doi.org/10.2514/6.2025-0465
[research_martin_saunders_1976]: https://doi.org/10.21236/adb013340
[research_martinezramirez_rodriguezcortes_2022]: https://doi.org/10.58571/cnca.amca.2022.041
[research_martorella_kelly_1981]: https://doi.org/10.2514/6.1981-1710
[research_marvasti_boutayeb_2024]: https://doi.org/10.1109/iccims61672.2024.10690568
[research_masak_1965]: https://doi.org/10.2514/6.1965-315
[research_masaoka_hashimoto_2024]: https://doi.org/10.1109/icrca60878.2024.10649279
[research_mason_1991]: https://doi.org/10.2514/6.1991-3325
[research_mason_crowther_2004]: https://doi.org/10.2514/6.2004-2210
[research_mason_ravi_1994]: https://doi.org/10.2514/3.46520
[research_masubuchi_kato_2004]: https://doi.org/10.1109/cdc.2004.1428770
[research_matamoros_devisser_2018]: https://doi.org/10.2514/6.2018-1116
[research_mateescu_1986]: https://doi.org/10.2514/6.1986-1826
[research_mateescu_1987]: https://doi.org/10.2514/3.45432
[research_mathur_atkins_2023]: https://doi.org/10.2514/1.c036916
[research_matiasgarcia_bardera_2025]: https://doi.org/10.1109/icuas65942.2025.11007814
[research_matos_marta_2025]: https://doi.org/10.3390/aerospace12050369
[research_matt_chao_2025]: https://doi.org/10.2514/1.c038147
[research_matternduane_gargsanjay_1989]: https://ntrs.nasa.gov/citations/19890065930
[research_matthews_yi_2019]: https://doi.org/10.1109/southeastcon42311.2019.9020447
[research_matthews_yi_2021]: https://doi.org/10.1109/southeastcon45413.2021.9401817
[research_mattingly_1998]: https://doi.org/10.2514/6.1998-3894
[research_matveev_wheeler_2022]: https://doi.org/10.1504/ijad.2022.10055158
[research_maughmer_axten_2021]: https://doi.org/10.2514/6.2021-2514
[research_maughmer_axten_2023]: https://doi.org/10.2514/1.c036705
[research_maughmer_somers_1987]: https://doi.org/10.2514/6.1987-2554
[research_maughmer_somers_1987_b]: https://ntrs.nasa.gov/citations/19900003229
[research_maughmermarkd_ozoroskil_1990]: https://ntrs.nasa.gov/citations/19900012419
[research_maunder_1979]: https://doi.org/10.2514/6.1979-1803
[research_maurya_patel_2025]: https://doi.org/10.1109/etaav66793.2025.11213250
[research_mavris_delaurentis_1998]: https://doi.org/10.2514/6.1998-492
[research_maybeck_stevens_1990]: https://doi.org/10.1109/cdc.1990.203417
[research_maybeck_stevens_1991]: https://doi.org/10.1109/7.81428
[research_mayhew_gleason_1988]: https://doi.org/10.2514/6.1988-3860
[research_mayya_karnick_2022]: https://doi.org/10.2514/6.2022-4173
[research_mazenc_malisoff_2020]: https://doi.org/10.23919/acc45564.2020.9148032
[research_mazenc_malisoff_2022]: https://doi.org/10.1016/j.sysconle.2022.105212
[research_mazza_1992]: https://doi.org/10.4271/921017
[research_mcclinton_voland_1998]: https://doi.org/10.2514/6.1998-2866
[research_mccormick_1969]: https://doi.org/10.21236/ad0863818
[research_mccrink_gregory_2017]: https://doi.org/10.2514/6.2017-4061
[research_mcdaniel_2017]: https://doi.org/10.2514/6.2017-3138
[research_mcdonald_farris_1964]: https://doi.org/10.21236/ad0603704
[research_mcfarland_dsouza_1994]: https://doi.org/10.2514/6.1994-3604
[research_mcgough_moses_1974]: https://doi.org/10.21236/ada006411
[research_mcgregor_smith_1966]: https://doi.org/10.2514/3.43780
[research_mcguigan_1970]: https://doi.org/10.2514/6.1970-513
[research_mcinally_1963]: https://doi.org/10.1119/1.1969796
[research_mcinville_moore_1994]: https://doi.org/10.21236/ada277965
[research_mckeehen_1998]: https://doi.org/10.2514/6.1998-4159
[research_mckeehen_cord_1997]: https://doi.org/10.21236/ada327802
[research_mckenzie_1973]: https://doi.org/10.2514/6.1973-782
[research_mclean_1994]: https://doi.org/10.1049/cp:19940361
[research_mclean_aslammir_1992]: https://doi.org/10.1016/s1474-6670(17)49641-8
[research_mclean_aslammir_1994]: https://doi.org/10.1016/0967-0661(94)90783-8
[research_mclean_aslammir_1994_b]: https://doi.org/10.1016/s1474-6670(17)45784-3
[research_mcmaster_schenk_1974]: https://doi.org/10.2514/3.59224
[research_mcminn_jackson_2002]: https://doi.org/10.2514/6.2002-4673
[research_meckstroth_blake_2015]: https://doi.org/10.2514/6.2015-2324
[research_meckstroth_ordonez_2020]: https://doi.org/10.2514/6.2020-3177
[research_meckstroth_ordonez_2020_b]: https://doi.org/10.2514/6.2020-3178
[research_mehaliccm_ziemianskija_1980]: https://ntrs.nasa.gov/citations/19810049750
[research_mehrark_euptank_1975]: https://ntrs.nasa.gov/citations/19750021936
[research_mehrark_tylerjs_1973]: https://ntrs.nasa.gov/citations/19740042090
[research_mei_zhou_2023]: https://doi.org/10.2514/6.2023-1561
[research_melekhin_khachumov_2021]: https://doi.org/10.17587/mau.22.650-659
[research_mello_agnew_1979]: https://doi.org/10.4271/791081
[research_meng_wang_2026]: https://doi.org/10.1016/j.ast.2026.112804
[research_meng_yan_2015]: https://doi.org/10.2514/6.2015-2954
[research_mengali_2003]: https://doi.org/10.2514/2.g6330tc
[research_menke_gursul_1999]: https://doi.org/10.2514/2.2481
[research_menner_lawless_2025]: https://doi.org/10.2514/6.2025-3571
[research_merhav_1989]: https://doi.org/10.2514/6.1989-3518
[research_merhav_grunwald_1978]: https://doi.org/10.2514/3.58338
[research_mestriner_desouza_2018]: https://doi.org/10.2514/6.2018-4201
[research_metin_uzuner_2023]: https://doi.org/10.2514/6.2023-1572
[research_metkowski_axten_2022]: https://doi.org/10.2514/6.2022-1530
[research_metodiev_2022]: https://doi.org/10.3897/arb.v34.e06
[research_metodiev_2024]: https://doi.org/10.3897/arb.v36.e10
[research_metzger_2012]: https://doi.org/10.21236/ada575815
[research_meyer_1983]: https://doi.org/10.2514/6.1983-2071
[research_meyerhf_yiplp_1989]: https://ntrs.nasa.gov/citations/19890060320
[research_miao_wang_2020]: https://doi.org/10.1115/gt2020-16048
[research_michaelttong_2020]: https://ntrs.nasa.gov/citations/20205007448
[research_michaltoddr_1998]: https://ntrs.nasa.gov/citations/19980137606
[research_michelsen_mueller_1987]: https://doi.org/10.2514/6.1987-2351
[research_michna_rogowski_2022]: https://doi.org/10.3390/pr10051004
[research_michna_sledziewski_2025]: https://doi.org/10.3390/en18112884
[research_mikami_uchiyama_2015]: https://doi.org/10.1109/icuas.2015.7152364
[research_miles_1952]: https://doi.org/10.2514/8.2249
[research_miles_1953]: https://doi.org/10.1093/qjmam/6.3.286
[research_miles_broughton_2017]: https://doi.org/10.2514/1.c033900
[research_milillo_1972]: https://doi.org/10.21236/ad0751461
[research_miller_1970]: https://doi.org/10.2514/3.44206
[research_miller_1983]: https://doi.org/10.2514/6.1983-2482
[research_miller_1986]: https://doi.org/10.2514/3.45268
[research_miller_clark_1965]: https://doi.org/10.2514/3.43639
[research_miller_franklin_1968]: https://doi.org/10.2514/3.43919
[research_miller_hackney_1976]: https://doi.org/10.21236/ada033532
[research_millerchristopherj_2011]: https://ntrs.nasa.gov/citations/20110015945
[research_millerchristopherj_2011_b]: https://ntrs.nasa.gov/citations/20110015950
[research_millerjr_1973]: https://doi.org/10.2514/6.1973-823
[research_mineck_1976]: https://doi.org/10.2514/6.1976-1933
[research_mineckre_1977]: https://ntrs.nasa.gov/citations/19770016117
[research_mineckre_freemancr_1976]: https://ntrs.nasa.gov/citations/19760021072
[research_mirchandani_2020]: https://doi.org/10.2514/6.2020-0219
[research_miroslaw_dominik_2022]: https://doi.org/10.2478/fas-2022-0009
[research_mirzal_2017]: https://doi.org/10.21742/ijcmdi.2017.3.1.01
[research_mitchell_doman_2003]: https://doi.org/10.21236/ada417898
[research_mitchell_hoh_1983]: https://doi.org/10.2514/6.1983-2106
[research_mitchell_hoh_1984]: https://doi.org/10.2514/3.8551
[research_mitchell_hoh_1991]: https://doi.org/10.2514/6.1991-2892
[research_mitchell_myers_1980]: https://doi.org/10.21236/ada101648
[research_mitchelldavidg_aponsobimall_1992]: https://ntrs.nasa.gov/citations/19920019341
[research_mitrut_bucur_2021]: https://doi.org/10.1109/ciem52821.2021.9614834
[research_miwa_2021]: https://doi.org/10.1299/jsmermd.2021.1p3-b17
[research_miwa_maruhashi_2016]: https://doi.org/10.1299/jsmermd.2016.1p1-17b6
[research_model_following_2003]: https://doi.org/10.5302/j.icros.2003.9.2.099
[research_moens_2022]: https://doi.org/10.3390/aerospace10010007
[research_moerderdanield_halyonesim_1989]: https://ntrs.nasa.gov/citations/19890049560
[research_moestimothyr_iliffkenneth_2002]: https://ntrs.nasa.gov/citations/20020057965
[research_moestimothyr_smithmarks_2003]: https://ntrs.nasa.gov/citations/20030107571
[research_mohamed_2024]: https://doi.org/10.1016/j.ifacol.2024.05.062
[research_mohamed_joy_2021]: https://doi.org/10.1017/aer.2021.61
[research_mohamed_madhavan_2019]: https://doi.org/10.1088/1742-6596/1215/1/012025
[research_mohamed_wood_2021]: https://doi.org/10.3390/en14164958
[research_mohamedibren_ameldadianneandan_2021]: https://doi.org/10.37934/cfdl.13.10.3651
[research_mohammadi_ebrahimi_2025]: https://doi.org/10.1007/s44245-025-00090-x
[research_mohammadifarhadi_kortunov_2018]: https://doi.org/10.14311/ap.2018.58.0077
[research_mohan_kumar_2024]: https://doi.org/10.1134/s0015462824603887
[research_mohan_kumar_2025]: https://doi.org/10.47176/jafm.18.9.3328
[research_mokhtar_elbadawy_2023]: https://doi.org/10.1109/icuas57906.2023.10156126
[research_molander_willems_1980]: https://doi.org/10.1109/tac.1980.1102462
[research_molinari_arrieta_2015]: https://doi.org/10.1117/12.2179176
[research_molinari_arrieta_2018]: https://doi.org/10.1177/1045389x18798952
[research_molloy_shekar_2026]: https://doi.org/10.2514/6.2026-2808
[research_molusis_1973]: https://doi.org/10.4050/jahs.18.12
[research_molusisja_1973]: https://ntrs.nasa.gov/citations/19740010561
[research_molusisjh_briczinskis_1974]: https://ntrs.nasa.gov/citations/19740017466
[research_monaco_ward_1997]: https://doi.org/10.2514/6.1997-3738
[research_moniruzzaman_rassau_2021]: https://doi.org/10.2139/ssrn.4082840
[research_moniruzzaman_rassau_2022]: https://doi.org/10.1007/s10846-022-01749-3
[research_montalvo_costello_2015]: https://doi.org/10.2514/1.c032634
[research_montgomery_caglayan_1976]: https://doi.org/10.2514/3.58633
[research_montgomery_hunsaker_2022]: https://doi.org/10.2514/6.2022-2531
[research_montgomery_price_1976]: https://doi.org/10.2514/3.58634
[research_montgomeryraymondc_scottmichaela_1998]: https://ntrs.nasa.gov/citations/19980032587
[research_mooij_vangool_1978]: https://doi.org/10.2514/3.58407
[research_moore_skow_1980]: https://doi.org/10.2514/6.1980-173
[research_morelli_2021]: https://doi.org/10.2514/6.2021-2795
[research_morelli_2021_b]: https://doi.org/10.2514/6.2021-1642
[research_morelli_2022]: https://doi.org/10.2514/1.g006072
[research_morelli_cooper_2015]: https://doi.org/10.2514/1.c033121
[research_morelli_klein_1995]: https://doi.org/10.2514/6.1995-3499
[research_morellieugenea_deloachrichard_2003]: https://ntrs.nasa.gov/citations/20030014297
[research_moreschi_guardone_2024]: https://doi.org/10.2514/6.2024-4609
[research_moretti_1965]: https://doi.org/10.21236/ad0632440
[research_mori_1988]: https://doi.org/10.1002/ecja.4410710405
[research_morlang_strassburger_2025]: https://doi.org/10.1109/wsc68292.2025.11339105
[research_moroney_pruitt_1979]: https://doi.org/10.1177/1071181379023001126
[research_morra_nicolosi_2025]: https://doi.org/10.2514/6.2025-3424
[research_morris_1964]: https://doi.org/10.2514/3.43597
[research_morris_1966]: https://doi.org/10.2514/6.1966-770
[research_morris_1981]: https://ntrs.nasa.gov/citations/19810013510
[research_morris_1992]: https://doi.org/10.2514/6.1992-4604
[research_morris_allison_2014]: https://doi.org/10.2514/1.c032340
[research_morris_kroo_1990]: https://doi.org/10.2514/3.45982
[research_morrisjr_1983]: https://doi.org/10.2514/6.1983-1825
[research_morse_ossman_1989]: https://doi.org/10.23919/acc.1989.4790181
[research_morse_ossman_1990]: https://doi.org/10.2514/3.20568
[research_morton_2003]: https://doi.org/10.2514/6.2003-4217
[research_morton_enns_1996]: https://doi.org/10.1080/00207179608921828
[research_morton_mitchell_2002]: https://doi.org/10.2514/6.2002-2968
[research_moses_pferschjr_1965]: https://doi.org/10.2514/6.1965-1205
[research_moszczynski_grant_2017]: https://doi.org/10.2514/6.2017-3893
[research_moszczynski_leung_2019]: https://doi.org/10.2514/6.2019-0433
[research_mottermarka_highjamesw_2009]: https://ntrs.nasa.gov/citations/20090030001
[research_motycka_skowronek_1968]: https://doi.org/10.4271/680296
[research_motyka_1975]: https://doi.org/10.21236/ada025359
[research_motyka_reynolds_1971]: https://doi.org/10.2514/6.1971-961
[research_mouacheng_mcwhertershaunh_2007]: https://ntrs.nasa.gov/citations/20090009810
[research_mouachengm_mcwhertershaunc_2012]: https://ntrs.nasa.gov/citations/20120013435
[research_mouritsen_1994]: https://doi.org/10.2514/6.1994-3488
[research_mrusek_2021]: https://doi.org/10.19080/ttsr.2021.05.555651
[research_mueller_1965]: https://doi.org/10.2514/3.43667
[research_mueller_theodoulis_2026]: https://doi.org/10.2514/6.2026-0548
[research_mueller_torres_2001]: https://doi.org/10.21236/ada397533
[research_muhammed_virk_2024]: https://doi.org/10.3390/drones8040148
[research_muir_1993]: https://doi.org/10.2514/6.1993-3779
[research_muir_bradshaw_1996]: https://doi.org/10.1243/pime_proc_1996_210_378_02
[research_mukai_hunter_1996]: https://doi.org/10.2514/6.1996-3504
[research_mukherjee_sinha_2016]: https://doi.org/10.2514/6.2016-1037
[research_mukohara_anyoji_2021]: https://doi.org/10.1299/jsmekyushu.2021.74.a22
[research_mulder_1985]: https://doi.org/10.1016/s1474-6670(17)60606-2
[research_mulgund_stengel_1993]: https://doi.org/10.23919/acc.1993.4792883
[research_mulgund_stengel_1995]: https://doi.org/10.2514/3.21508
[research_muller_1967]: https://doi.org/10.2514/3.59369
[research_muller_moormann_2023]: https://doi.org/10.1142/s2301385024430040
[research_mullinsjr_tipton_1996]: https://doi.org/10.2514/6.1996-894
[research_multi_rotors_a_2015]: https://doi.org/10.21275/v4i11.nov151540
[research_munday_taira_2015]: https://doi.org/10.2514/1.c032983
[research_munkmaxm_1922]: https://ntrs.nasa.gov/citations/19930080900
[research_munkmaxm_1924]: https://ntrs.nasa.gov/citations/19930091249
[research_munkmm_1979]: https://ntrs.nasa.gov/citations/19800006780
[research_muravyev_2022]: https://doi.org/10.52348/2712-8873_mmtt_2022_10_73
[research_murphy_1966]: https://doi.org/10.2514/3.3471
[research_murphy_klein_2004]: https://doi.org/10.2514/6.2004-5277
[research_murphy_schmidt_1953]: https://doi.org/10.21236/ad0023468
[research_murri_croom_1983]: https://doi.org/10.2514/6.1983-1837
[research_murri_rao_1987]: https://doi.org/10.2514/6.1987-2557
[research_murridanielg_shahgautamh_1994]: https://ntrs.nasa.gov/citations/19950007843
[research_murridg_nguyenlt_1984]: https://ntrs.nasa.gov/citations/19840009116
[research_murugappa_kazerani_2025]: https://doi.org/10.1109/isie62713.2025.11124611
[research_musso_vo_2026]: https://doi.org/10.2514/6.2026-2763
[research_myatt_schumacher_1998]: https://doi.org/10.2514/6.1998-4455
[research_myschik_kinast_2022]: https://doi.org/10.2514/6.2022-3282
[research_nadda_swarup_2017]: https://doi.org/10.14429/dsj.67.9536
[research_nadell_berger_2023]: https://doi.org/10.4050/f-0079-2023-0143
[research_nadi_zeid_1955]: https://doi.org/10.1021/j150532a029
[research_nae_2026]: https://doi.org/10.2514/6.2026-2110
[research_nagata_skinner_1973]: https://doi.org/10.21236/ad0776360
[research_nagel_thomas_1965]: https://doi.org/10.2514/6.1965-208
[research_nagy_kirsten_1976]: https://doi.org/10.21236/adb012970
[research_naigle_hiltner_2022]: https://doi.org/10.2514/6.2022-2326
[research_nam_2026]: https://doi.org/10.5139/jksas.2026.54.8.877
[research_napolitano_2002]: https://doi.org/10.21236/ada400639
[research_napolitano_casanova_1997]: https://doi.org/10.2514/6.1997-3539
[research_napolitano_kerrian_2024]: https://doi.org/10.2514/6.2024-0619
[research_napolitano_kincheloe_1996]: https://doi.org/10.2514/6.1996-3851
[research_napolitano_song_2001]: https://doi.org/10.1016/s1369-8869(00)00023-9
[research_napolitano_windon_1998]: https://doi.org/10.1109/87.709495
[research_nardi_1970]: https://doi.org/10.2514/6.1970-515
[research_nasiri_montazerigh_2021]: https://doi.org/10.1007/s12555-019-0875-x
[research_nasuhbeyoglu_akca_2024]: https://doi.org/10.2514/6.2024-4228
[research_nataraj_sardar_1999]: https://doi.org/10.1115/1.1286867
[research_natarajan_kapania_2004]: https://doi.org/10.2514/1.477
[research_navaratna_pontillo_2022]: https://doi.org/10.33424/futurum331
[research_neal_smith_1970]: https://doi.org/10.21236/ad0880426
[research_nealbradford_senguptaupal_1989]: https://ntrs.nasa.gov/citations/19900010770
[research_nedilko_kolisnichenko_2026]: https://doi.org/10.32782/1995-0519.2026.1.1.15
[research_negre_1975]: https://doi.org/10.2514/6.1975-1023
[research_neitzke_2025]: https://doi.org/10.47191/etj/v10i05.34
[research_nelms_axelson_1974]: https://ntrs.nasa.gov/citations/19740010564
[research_nelms_bailey_1974]: https://ntrs.nasa.gov/citations/19740020394
[research_nelson_1985]: https://doi.org/10.2514/6.1985-102
[research_nelson_durham_2002]: https://doi.org/10.2514/6.2002-4498
[research_nelson_mouch_1978]: https://doi.org/10.21236/ada056045
[research_nenadic_debeljkovic_1997]: https://doi.org/10.23919/ecc.1997.7082217
[research_nepomuceno_annesdasilva_2021]: https://doi.org/10.26678/abcm.cobem2021.cob2021-1010
[research_nepomuceno_fischer_2022]: https://doi.org/10.2514/6.2022-0880
[research_nettleton_1965]: https://doi.org/10.2514/6.1965-713
[research_neuwerth_peiter_1998]: https://doi.org/10.2514/6.1998-1578
[research_neuwerth_peiter_1999]: https://doi.org/10.2514/2.3441
[research_neves_lawson_2020]: https://doi.org/10.1016/j.ast.2020.106179
[research_neville_stephens_1993]: https://doi.org/10.2514/6.1993-3596
[research_newman_1965]: https://doi.org/10.21236/ad0628161
[research_newton_kroo_2023]: https://doi.org/10.2514/6.2023-3319
[research_newton_kroo_2024]: https://doi.org/10.2514/6.2024-4581
[research_newton_kroo_2025]: https://doi.org/10.2514/1.g008400
[research_ngo_reigelsperger_1996]: https://doi.org/10.2514/6.1996-3866
[research_nguyen_1979]: https://doi.org/10.4271/791083
[research_nguyen_cord_1997]: https://doi.org/10.2514/6.1997-3730
[research_nguyen_cord_1999]: https://doi.org/10.2514/6.1999-4004
[research_nguyen_han_2025]: https://doi.org/10.1016/j.automatica.2025.112270
[research_nguyen_lowenberg_2021]: https://doi.org/10.2514/1.g005840
[research_nguyen_lowenberg_2021_b]: https://doi.org/10.2514/6.2021-0759
[research_nguyen_reynolds_2016]: https://doi.org/10.2514/6.2016-3413
[research_nguyen_reynolds_2018]: https://doi.org/10.2514/1.c034448
[research_nguyen_tran_2021]: https://doi.org/10.1109/icsse52999.2021.9538444
[research_ni_chen_2024]: https://doi.org/10.2514/1.c037865
[research_ni_wu_2021]: https://doi.org/10.1109/access.2021.3095224
[research_nicholson_1985]: https://doi.org/10.21236/ada159292
[research_nicola_dicapua_2025]: https://doi.org/10.1109/aero63441.2025.11068526
[research_nicolosi_ciliberti_2020]: https://doi.org/10.1016/j.ast.2020.106099
[research_nicolosi_dellavecchia_2015]: https://doi.org/10.2514/6.2015-2257
[research_nicolosi_dellavecchia_2016]: https://doi.org/10.1016/j.ast.2016.06.012
[research_nicolosi_demarco_2015]: https://doi.org/10.2514/6.2015-2238
[research_nie_liu_2020]: https://doi.org/10.1109/access.2020.3001913
[research_nie_liu_2021]: https://doi.org/10.3390/app11041407
[research_nield_iv_1981]: https://doi.org/10.21236/ada106742
[research_nielsen_1985]: https://doi.org/10.2514/6.1985-449
[research_niemiec_j_2020]: https://doi.org/10.4050/f-0076-2020-16384
[research_niestroy_2025]: https://doi.org/10.2514/6.2025-1636
[research_niestroy_dorsett_2017]: https://doi.org/10.2514/6.2017-1757
[research_niestroy_williams_2019]: https://doi.org/10.2514/6.2019-0279
[research_nietocentenero_martinezcava_2024]: https://doi.org/10.23967/eccomas.2024.161
[research_nietowire_sobel_2007]: https://doi.org/10.2514/6.2007-6417
[research_nietowire_sobel_2009]: https://doi.org/10.2514/6.2009-6306
[research_nietowire_sobel_2011]: https://doi.org/10.1155/2011/549131
[research_nietowire_sobel_2013]: https://doi.org/10.2514/6.2013-4778
[research_nietowire_sobel_2014]: https://doi.org/10.2514/1.g000036
[research_niewald_parker_2000]: https://doi.org/10.2514/2.2598
[research_niewoehnerkevinr_carterjohn_2001]: https://ntrs.nasa.gov/citations/20010056315
[research_nihtila_1989]: https://doi.org/10.1016/0167-6911(89)90046-7
[research_nikiforuk_gupta_1977]: https://doi.org/10.2514/6.1977-1092
[research_nikiforuk_ohta_1979]: https://doi.org/10.2514/3.55835
[research_nikmohd_2017]: https://doi.org/10.5028/jatm.v9i1.610
[research_nikolaou_kilimtzidis_2025]: https://doi.org/10.3390/aerospace12040359
[research_nivison_khargonekar_2017]: https://doi.org/10.2514/6.2017-1249
[research_nivison_khargonekar_2017_b]: https://doi.org/10.23919/acc.2017.7963784
[research_nivison_khargonekar_2018]: https://doi.org/10.2514/6.2018-0842
[research_nnagy_altikriti_1970]: https://doi.org/10.1177/002029407000300304
[research_nogami_maeda_1986]: https://doi.org/10.9746/sicetr1965.22.542
[research_nonlinear_adaptive_1998]: https://doi.org/10.1109/37.736008
[research_nonlinear_discrete_time_2004]: https://doi.org/10.5302/j.icros.2004.10.2.112
[research_nonlinear_model_1989]: https://doi.org/10.2514/6.1989-3308
[research_norsell_2003]: https://doi.org/10.2514/2.3115
[research_northropaircraftinchawthorneca_1952]: https://doi.org/10.21236/ad0024361
[research_noury_yang_2020]: https://doi.org/10.1115/imece2020-23095
[research_nudson_stanfieldbrown_2025]: https://doi.org/10.2514/1.c038055
[research_numerical_analysis_2017]: https://doi.org/10.15372/pmtf20170303
[research_nvarsha_deshpande_2023]: https://doi.org/10.61653/joast.v71i3.2019.156
[research_o_three_a_1990]: https://ntrs.nasa.gov/citations/19910008851
[research_obeid_alqadi_2019]: https://doi.org/10.1007/s00162-019-00503-0
[research_obermark_2004]: https://doi.org/10.21236/ada422954
[research_oblique_wing_1974]: https://ntrs.nasa.gov/citations/19740013546
[research_odendaal_smith_2024]: https://doi.org/10.1108/aeat-11-2023-0297
[research_odonnell_mohseni_2018]: https://doi.org/10.2514/6.2018-0294
[research_ogburn_foster_1993]: https://doi.org/10.2514/6.1993-3623
[research_ogren_sotanski_1974]: https://doi.org/10.21236/ad0784134
[research_oh_choi_2018]: https://doi.org/10.1088/1748-3190/aad578
[research_okolo_dogan_2015]: https://doi.org/10.2514/6.2015-0902
[research_oktay_kose_2021]: https://doi.org/10.31590/ejosat.946884
[research_ol_2007]: https://doi.org/10.21236/ada472788
[research_olejnik_kachel_2019]: https://doi.org/10.1051/matecconf/201930402010
[research_olejnik_rogolski_2022]: https://doi.org/10.1088/1757-899x/1226/1/012004
[research_oliva_2001]: https://doi.org/10.2514/6.2001-4082
[research_olson_selberg_1976]: https://doi.org/10.2514/3.44523
[research_olsson_1982]: https://doi.org/10.2514/3.44761
[research_ong_chan_2016]: https://doi.org/10.1080/10618562.2016.1245417
[research_onken_stuckenberg_1978]: https://doi.org/10.1109/cdc.1978.267964
[research_oosedo_wada_2022]: https://doi.org/10.1299/jsmermd.2022.2a2-k05
[research_oosterom_bergsten_2002]: https://doi.org/10.2514/6.2002-4748
[research_oosterom_schram_2000]: https://doi.org/10.2514/6.2000-4253
[research_oosterom_vos_2022]: https://doi.org/10.2514/6.2022-3200
[research_oppenheimer_doman_2004]: https://doi.org/10.2514/6.2004-5017
[research_optimized_pi_pd_2024]: https://doi.org/10.22266/ijies2024.0229.30
[research_optimum_neural_1993]: https://doi.org/10.1016/0967-0661(93)92168-4
[research_orhan_subbarao_2021]: https://doi.org/10.2514/6.2021-0108
[research_orlosky_theofilis_2018]: https://doi.org/10.1162/pres_a_00328
[research_orourke_1995]: https://doi.org/10.2514/6.1995-1798
[research_orourke_sedor_1995]: https://doi.org/10.2514/6.1995-3490
[research_orozco_walsh_2026]: https://doi.org/10.1109/icuas69441.2026.11598640
[research_ortiztorres_castillo_2018]: https://doi.org/10.1109/icuas.2018.8453288
[research_osawa_hewitt_1986]: https://doi.org/10.2514/6.1986-1828
[research_osipov_2019]: https://doi.org/10.1615/tsagiscij.2019030599
[research_ossmann_luspay_2019]: https://doi.org/10.1109/aero.2019.8741853
[research_ostermann_laubner_2024]: https://doi.org/10.2514/6.2024-0453
[research_ostheimer_giguere_1963]: https://doi.org/10.21236/ad0402379
[research_ostroff_bacon_2002]: https://doi.org/10.1109/acc.2002.1024492
[research_ostroffaaronj_1998]: https://ntrs.nasa.gov/citations/19980039322
[research_othman_kanazaki_2015]: https://doi.org/10.1016/j.proeng.2014.12.592
[research_othman_kanazaki_2015_b]: https://doi.org/10.2514/6.2015-0543
[research_ouyang_lin_2017]: https://doi.org/10.1002/rnc.3883
[research_ouyang_zhou_2022]: https://doi.org/10.1109/iciea54703.2022.10006047
[research_ovcharenko_poplavsky_2021]: https://doi.org/10.1134/s1064230721060149
[research_owashi_tanaka_2017]: https://doi.org/10.1299/jsmermd.2017.1p2-e04
[research_owen_johnson_1978]: https://doi.org/10.2514/6.1978-23
[research_owensdonaldb_coxdavide_2006]: https://ntrs.nasa.gov/citations/20060022541
[research_ozdemir_2020]: https://doi.org/10.26833/ijeg.648847
[research_ozdemir_kucuk_2024]: https://doi.org/10.1109/dasc62030.2024.10749317
[research_ozgoren_sahin_2002]: https://doi.org/10.2514/2.1644
[research_oznurlu_bayri_2023]: https://doi.org/10.1109/rast57548.2023.10197871
[research_ozturk_1986]: https://doi.org/10.1109/cdc.1986.267503
[research_ozturk_1991]: https://doi.org/10.23919/acc.1991.4791735
[research_p5_ramasubramanian1_2026]: https://doi.org/10.55041/ijsrem61623
[research_pachecogutierrez_niu_2021]: https://doi.org/10.3390/robotics10030089
[research_padhi_balakrishnan_2003]: https://doi.org/10.2514/6.2003-5505
[research_page_steinberg_1999]: https://doi.org/10.21236/ada368467
[research_pagliuca_timme_2016]: https://doi.org/10.2514/6.2016-3850
[research_pagliuca_timme_2017]: https://doi.org/10.1016/j.ast.2017.06.013
[research_pahlejosephw_bundickwthomas_1996]: https://ntrs.nasa.gov/citations/19960041445
[research_pakzad_2021]: https://doi.org/10.23919/acc50511.2021.9482907
[research_pal_gaberson_1973]: https://doi.org/10.1121/1.1978066
[research_palacios_owens_1998]: https://doi.org/10.21236/ada337601
[research_palframan_fry_2019]: https://doi.org/10.1109/tcst.2017.2766598
[research_palkin_zenchenko_2025]: https://doi.org/10.18127/j20700784-202509-06
[research_pallister_parker_1992]: https://doi.org/10.2514/6.1992-3985
[research_palmer_wright_2002]: https://doi.org/10.2514/6.2002-3342
[research_pan_huang_2018]: https://doi.org/10.1177/0954410018817449
[research_pan_huang_2019]: https://doi.org/10.5028/jatm.v11.1074
[research_pan_huang_2019_b]: https://doi.org/10.1108/aeat-04-2018-0119
[research_pan_liu_2016]: https://doi.org/10.1016/j.neunet.2015.12.009
[research_pan_ma_2025]: https://doi.org/10.1088/1742-6596/3126/1/012065
[research_pan_mao_2026]: https://doi.org/10.1088/1742-6596/3207/1/012030
[research_pan_sun_2017]: https://doi.org/10.1016/j.neunet.2017.08.005
[research_pandi_mittal_2025]: https://doi.org/10.1017/jfm.2024.1152
[research_panish_nicholls_2023]: https://doi.org/10.2514/6.2023-1910
[research_papadales_basils_1979]: https://doi.org/10.21236/ada073100
[research_papageorgiou_glover_2002]: https://doi.org/10.3182/20020721-6-es-1901.01262
[research_papageorgiou_tarkian_2018]: https://doi.org/10.2514/1.c034314
[research_papoutsiskiachagias_asouti_2021]: https://doi.org/10.7712/120221.8043.19104
[research_parameter_estimation_1974]: https://ntrs.nasa.gov/citations/19740017456
[research_paranjape_ananthkrishnan_2023]: https://doi.org/10.61653/joast.v58i2.2006.706
[research_paranjape_chung_2010]: https://doi.org/10.2514/6.2010-7633
[research_paranjape_chung_2011]: https://doi.org/10.1088/1748-3182/6/2/026005
[research_paranjapesv_thomastj_1966]: https://ntrs.nasa.gov/citations/19670061214
[research_park_1977]: https://doi.org/10.2514/3.58770
[research_park_choi_2016]: https://doi.org/10.2514/6.2016-2024
[research_park_choi_2017]: https://doi.org/10.2514/1.c034052
[research_park_jo_2016]: https://doi.org/10.2514/6.2016-4038
[research_park_jo_2017]: https://doi.org/10.2514/6.2017-1754
[research_park_lee_2001]: https://doi.org/10.2514/6.2001-4014
[research_park_ocheltree_2015]: https://doi.org/10.2514/6.2015-3387
[research_park_ramirezserrano_2024]: https://doi.org/10.3390/aerospace11080671
[research_park_ramirezserrano_2025]: https://doi.org/10.3390/aerospace12040312
[research_park_ramirezserrano_2025_b]: https://doi.org/10.2514/6.2025-1809
[research_park_shim_2019]: https://doi.org/10.2514/6.2019-3644
[research_park_shin_2019]: https://doi.org/10.1016/j.ifacol.2019.11.261
[research_park_yang_2025]: https://doi.org/10.5302/j.icros.2025.24.0218
[research_parlange_1968]: https://doi.org/10.2514/3.43966
[research_parra_uraldeguinea_2026]: https://doi.org/10.1016/j.ijheatfluidflow.2026.110423
[research_passive_flow_2020]: https://doi.org/10.47176/jafm.13.06.31087
[research_patel_deodhare_2002]: https://doi.org/10.2514/6.2002-5820
[research_patel_prince_2002]: https://doi.org/10.2514/6.2002-3170
[research_patel_ramaprian_1978]: https://doi.org/10.21236/ada060469
[research_patel_smith_1996]: https://doi.org/10.2514/6.1996-3369
[research_patel_smith_1998]: https://doi.org/10.2514/2.4219
[research_patera_1981]: https://doi.org/10.1119/1.12677
[research_patience_nahon_2020]: https://doi.org/10.1109/icuas48674.2020.9213952
[research_patten_1988]: https://doi.org/10.2514/6.1988-4052
[research_patterson_arena_2015]: https://doi.org/10.2514/6.2015-2858
[research_paul_garrard_1997]: https://doi.org/10.2514/6.1997-3776
[research_paulson_price_1977]: https://doi.org/10.1117/12.955862
[research_paulsonjwjr_thomasjl_1979]: https://ntrs.nasa.gov/citations/19790035660
[research_payne_1968]: https://doi.org/10.2514/6.1968-57
[research_pedersini_toscano_2015]: https://doi.org/10.1145/2750675.2750676
[research_pedreiro_rock_1998]: https://doi.org/10.2514/2.2261
[research_pedreironelson_1997]: https://ntrs.nasa.gov/citations/19980201173
[research_pei_huang_2025]: https://doi.org/10.1109/raiic65850.2025.11170302
[research_pelikan_1974]: https://doi.org/10.2514/6.1974-68
[research_pelletier_mueller_1999]: https://doi.org/10.2514/6.1999-3182
[research_pelletier_nelson_2000]: https://doi.org/10.2514/2.2663
[research_pena_voulgaris_2001]: https://doi.org/10.1177/107754630100700805
[research_peng_chen_2019]: https://doi.org/10.1016/j.egypro.2019.01.446
[research_peng_li_2016]: https://doi.org/10.2514/6.2016-4337
[research_peng_lin_2018]: https://doi.org/10.1109/icuas.2018.8453408
[research_pepelea_cojocaru_2016]: https://doi.org/10.19062/2247-3173.2016.18.1.22
[research_perhinschi_1998]: https://doi.org/10.2514/6.1998-4148
[research_perhinschi_prasad_1995]: https://doi.org/10.2514/6.1995-3456
[research_peristy_perez_2016]: https://doi.org/10.2514/6.2016-3260
[research_peristy_perez_2019]: https://doi.org/10.2514/6.2019-0583
[research_peristy_perez_2020]: https://doi.org/10.2514/6.2020-1261
[research_perng_wu_2004]: https://doi.org/10.1109/tsmcb.2004.831772
[research_perry_mueller_1986]: https://doi.org/10.2514/6.1986-1787
[research_perrybiii_1976]: https://ntrs.nasa.gov/citations/19760011057
[research_persson_2017]: https://doi.org/10.2514/1.c033932
[research_persson_bull_2016]: https://doi.org/10.2514/1.c033566
[research_petersen_1976]: https://ntrs.nasa.gov/citations/19760014130
[research_petersen_1976_b]: https://ntrs.nasa.gov/citations/19760053941
[research_peterson_1968]: https://doi.org/10.2514/6.1968-20
[research_peterson_2024]: https://doi.org/10.2514/6.2024-2873
[research_peterson_2025]: https://doi.org/10.2514/6.2025-2439
[research_peterson_sarigulklijn_2016]: https://doi.org/10.2514/6.2016-5554
[research_petersonvictorl_1961]: https://ntrs.nasa.gov/citations/19980227076
[research_petersonwaynel_2004]: https://ntrs.nasa.gov/citations/20110011625
[research_petnga_2018]: https://doi.org/10.2514/6.2018-1214
[research_petrenko_gasparovic_2025]: https://doi.org/10.35116/aa.2025.0002
[research_petrie_1968]: https://doi.org/10.2514/3.43948
[research_petrovic_sajn_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000555
[research_pfeifle_fichter_2022]: https://doi.org/10.2514/6.2022-1596
[research_pfeifle_fichter_2023]: https://doi.org/10.2514/1.g006929
[research_pfenninger_vemuru_1988]: https://doi.org/10.2514/6.1988-2572
[research_pfifer_danowsky_2016]: https://doi.org/10.2514/6.2016-1750
[research_pfifer_seiler_2015]: https://doi.org/10.1109/acc.2015.7170725
[research_pfnur_breitsamter_2019]: https://doi.org/10.2514/1.c035491
[research_phelps_1979]: https://ntrs.nasa.gov/citations/19790022980
[research_phillips_2000]: https://doi.org/10.2514/2.2623
[research_phillips_2000_b]: https://doi.org/10.2514/6.2000-499
[research_phillips_jentzsch_2019]: https://doi.org/10.2514/6.2019-0045
[research_phillips_santana_2002]: https://doi.org/10.2514/2.3050
[research_pi_control_1999]: https://doi.org/10.1109/acc.1999.786342
[research_piccinelli_muradore_2021]: https://doi.org/10.1016/j.ejcon.2021.06.030
[research_piccirillo_1996]: https://doi.org/10.4271/965538
[research_pieper_perry_2018]: https://doi.org/10.2514/6.2018-4996
[research_pinebrook_dalton_1983]: https://doi.org/10.1016/0270-0255(83)90048-9
[research_pinebrook_dalton_1983_b]: https://doi.org/10.1016/0045-7825(83)90020-8
[research_pittsfl_holmesdce_1974]: https://ntrs.nasa.gov/citations/19750009281
[research_place_altmann_1974]: https://doi.org/10.21236/ad0785104
[research_plaetschke_mulder_1982]: https://doi.org/10.1016/s1474-6670(17)63152-5
[research_planeaux_barth_1988]: https://doi.org/10.2514/6.1988-4368
[research_platanitisgeorge_shkarayevsergey_2005]: https://ntrs.nasa.gov/citations/20050185598
[research_platou_1968]: https://doi.org/10.2514/6.1968-388
[research_platzer_hoffman_1966]: https://doi.org/10.2514/3.3763
[research_plyashechnik_ivanov_1999]: https://doi.org/10.2514/6.1999-3208
[research_pollack_theodoulis_2026]: https://doi.org/10.2514/6.2026-0108
[research_poojari_2022]: https://doi.org/10.47893/gret.2022.1089
[research_popescu_rasvan_2003]: https://doi.org/10.14232/ejqtde.2003.6.18
[research_portapas_cooke_2020]: https://doi.org/10.3846/aviation.2020.12175
[research_portapas_yusuf_2017]: https://doi.org/10.2514/6.2017-0577
[research_portermbjr_swaimrl_1975]: https://ntrs.nasa.gov/citations/19750025633
[research_pose_giribet_2017]: https://doi.org/10.1109/icuas.2017.7991321
[research_posingies_1979]: https://doi.org/10.21236/ada070387
[research_postlethwaite_konstantopoulos_1999]: https://doi.org/10.23919/ecc.1999.7099469
[research_postlethwaite_konstantopoulos_2000]: https://doi.org/10.1016/s0947-3580(00)71119-8
[research_potter_whitfield_1957]: https://doi.org/10.21236/ad0135338
[research_potvin_grant_2026]: https://doi.org/10.2514/6.2026-1883
[research_poudel_yu_2021]: https://doi.org/10.1063/5.0065234
[research_pounds_walker_1980]: https://doi.org/10.2514/6.1980-461
[research_power_1969]: https://doi.org/10.1109/tac.1969.1099276
[research_prabhakar_prazenica_2019]: https://doi.org/10.2514/6.2019-1921
[research_prakash_vignati_2019]: https://doi.org/10.1115/detc2019-98159
[research_prediction_of_1994]: https://doi.org/10.2514/6.1994-1883
[research_price_1943]: https://doi.org/10.1108/eb031078
[research_pricejr_glidewell_1981]: https://doi.org/10.2514/6.1981-1442
[research_pritchard_wallace_2016]: https://doi.org/10.2514/6.2016-1772
[research_priyanka_sivapragasam_2021]: https://doi.org/10.1007/s12046-021-01580-w
[research_prizirembel_wen_1978]: https://doi.org/10.21236/ada064583
[research_probst_knopp_2019]: https://doi.org/10.2514/6.2019-0331
[research_prochazka_eduardo_2018]: https://doi.org/10.1109/ccta.2018.8511538
[research_prochazka_stomberg_2020]: https://doi.org/10.23919/acc45564.2020.9147655
[research_protz_sparks_1998]: https://doi.org/10.2514/6.1998-4298
[research_provost_hawlader_2026]: https://doi.org/10.1109/vnc69225.2026.11629145
[research_provost_hawlader_2026_b]: https://doi.org/10.23919/wons68803.2026.11501834
[research_pryor_vagvolgyi_2020]: https://doi.org/10.1109/iros45743.2020.9340800
[research_ps_jv_2021]: https://doi.org/10.1108/aeat-03-2021-0089
[research_ptitsin_2017]: https://doi.org/10.1615/tsagiscij.2018025104
[research_pulk_stolarik_1977]: https://doi.org/10.2514/6.1977-1065
[research_pusztai_lowenberg_2024]: https://doi.org/10.2514/6.2024-1497
[research_putman_1969]: https://doi.org/10.21236/ad0859807
[research_putnamtw_petersenkl_1986]: https://ntrs.nasa.gov/citations/19860046595
[research_putra_mobedbachtiar_2022]: https://doi.org/10.1109/ies55876.2022.9888714
[research_qi_gao_2016]: https://doi.org/10.1016/j.mechatronics.2016.04.005
[research_qi_zhongke_2015]: https://doi.org/10.1016/j.cja.2014.12.022
[research_qian_ma_2024]: https://doi.org/10.1109/iwceaa63616.2024.10823887
[research_qian_xinhui_2025]: https://doi.org/10.65904/3083-3450.2025.01.05
[research_qian_yang_2022]: https://doi.org/10.1049/icp.2022.1719
[research_qin_2026]: https://doi.org/10.1142/s021812662642017x
[research_qiu_gourishankar_1984]: https://doi.org/10.1002/oca.4660050404
[research_qu_li_2011]: https://doi.org/10.1109/icciautom.2011.6183979
[research_queen_1976]: https://doi.org/10.21236/adb009060
[research_quenzer_barzgaran_2018]: https://doi.org/10.23919/acc.2018.8430839
[research_quitter_marino_2021]: https://doi.org/10.2514/6.2021-0324
[research_r_saderla_2018]: https://doi.org/10.1108/aeat-03-2016-0050
[research_rabenberg_palarz_1983]: https://doi.org/10.2514/6.1983-2487
[research_radar_cross_1979]: https://doi.org/10.2514/6.1979-1818
[research_raffel_dillmann_2021]: https://doi.org/10.2514/6.2021-0769
[research_raffel_wienke_2019]: https://doi.org/10.2514/1.c035399
[research_raffel_wienke_2021]: https://doi.org/10.2514/1.c036022
[research_rahal_dutta_2024]: https://doi.org/10.1007/s12046-023-02349-z
[research_rainbird_peiro_2015]: https://doi.org/10.1016/j.jweia.2015.06.006
[research_raisinghani_adak_1983]: https://doi.org/10.1080/00207728308926538
[research_rajagopal_lick_1988]: https://doi.org/10.2514/6.1988-5
[research_rajarajan_mudhangulla_2024]: https://doi.org/10.23919/acc60939.2024.10644849
[research_rajeswari_prabhu_1987]: https://doi.org/10.2514/3.45461
[research_rajput_zhangweiguo_2015]: https://doi.org/10.1109/ascc.2015.7244649
[research_rajukulkarni_larocca_2019]: https://doi.org/10.2514/6.2019-1208
[research_rakich_cleary_1970]: https://doi.org/10.2514/3.5698
[research_rakich_cleary_2003]: https://doi.org/10.2514/2.6903
[research_rakita_mutlu_2020]: https://doi.org/10.1145/3319502.3374838
[research_rakshith_deshpande_2015]: https://doi.org/10.2514/1.c032997
[research_ramdin_visser_2023]: https://doi.org/10.1115/gt2023-103548
[research_ramirez_breda_2021]: https://doi.org/10.1137/19m1307408
[research_ramirez_nahon_2021]: https://doi.org/10.1109/icuas51884.2021.9476776
[research_rampy_1966]: https://doi.org/10.21236/ad0641371
[research_raneydavidl_montgomeryraymondc_2000]: https://ntrs.nasa.gov/citations/20000057292
[research_ransom_1983]: https://doi.org/10.2514/3.44917
[research_ransquin_chatelain_2021]: https://doi.org/10.2514/6.2021-0885
[research_rao_1989]: https://doi.org/10.2514/6.1989-3350
[research_rao_moskovitz_1987]: https://doi.org/10.2514/3.45433
[research_rao_murri_1986]: https://doi.org/10.2514/6.1986-333
[research_rao_srinath_1965]: https://doi.org/10.1049/el:19650199
[research_raodm_moskovitzc_1986]: https://ntrs.nasa.gov/citations/19860064309
[research_ratcliff_bodkin_2016]: https://doi.org/10.2514/6.2016-3854
[research_raulazinheira_carneirodepaiva_2001]: https://doi.org/10.1108/eum0000000005880
[research_ravi_mason_1994]: https://doi.org/10.2514/3.46519
[research_rayleigh_1915]: https://doi.org/10.1038/095644b0
[research_raza_silverthorn_1985]: https://doi.org/10.2514/6.1985-1900
[research_reaser_hallissy_1983]: https://doi.org/10.2514/6.1983-1792
[research_reconfigurable_flight_2003]: https://doi.org/10.5302/j.icros.2003.9.4.329
[research_reed_1974]: https://ntrs.nasa.gov/citations/19740043660
[research_reed_1990]: https://doi.org/10.21236/ada225167
[research_reeder_1958]: https://doi.org/10.4050/jahs.3.4
[research_reel_baltadjiev_2018]: https://doi.org/10.2514/6.2018-4211
[research_reghunath_ramaiah_2022]: https://doi.org/10.2139/ssrn.4001327
[research_reichstein_schopferer_2022]: https://doi.org/10.1109/icuas54217.2022.9836194
[research_reigelsperger_hammett_1995]: https://doi.org/10.2514/6.1995-3249
[research_reinbold_breitsamter_2026]: https://doi.org/10.2514/1.c038409
[research_reiner_balas_1994]: https://doi.org/10.2514/6.1994-3682
[research_reiner_balas_1995]: https://doi.org/10.2514/3.56651
[research_reiner_balas_1996]: https://doi.org/10.1016/s0005-1098(96)00101-x
[research_reist_koo_2022]: https://doi.org/10.2514/1.c036754
[research_reist_zingg_2015]: https://doi.org/10.2514/6.2015-3292
[research_reist_zingg_2016]: https://doi.org/10.2514/6.2016-3874
[research_reist_zingg_2017]: https://doi.org/10.2514/1.c033798
[research_reklis_1980]: https://doi.org/10.21236/ada083296
[research_ren_ghopa_2026]: https://doi.org/10.3389/fmech.2026.1850561
[research_ren_quan_2016]: https://doi.org/10.1109/ccdc.2016.7532030
[research_ren_su_2022]: https://doi.org/10.3390/aerospace9120759
[research_ren_wang_2026]: https://doi.org/10.1177/00202940261460734
[research_ren_zha_2025]: https://doi.org/10.2514/6.2025-3639
[research_renard_deck_2015]: https://doi.org/10.2514/1.j054143
[research_repperger_koivo_1997]: https://doi.org/10.1109/acc.1997.611837
[research_research_and_2022]: https://doi.org/10.47939/et.v3i2.102
[research_research_and_2022_b]: https://doi.org/10.47939/et.v3i2.104
[research_resta_marsilio_2021]: https://doi.org/10.3390/fluids6120441
[research_reuther_jameson_1995]: https://doi.org/10.2514/6.1995-123
[research_rezek_1985]: https://ntrs.nasa.gov/citations/19850000120
[research_rhew_parker_2017]: https://doi.org/10.2514/6.2017-4427
[research_rhoads_1967]: https://doi.org/10.21236/ad0820790
[research_rhodeside_1986]: https://doi.org/10.2514/6.1986-492
[research_ribeiro_deresende_1993]: https://doi.org/10.2514/6.1993-3509
[research_riboldi_alessi_2026]: https://doi.org/10.2514/1.c038971
[research_riccardi_mamino_2025]: https://doi.org/10.4050/sm_handling_2025-5298
[research_richardson_1976]: https://doi.org/10.21236/adb012971
[research_richter_calix_2024]: https://doi.org/10.1109/access.2024.3433540
[research_rickard_1978]: https://doi.org/10.2514/6.1978-1371
[research_riethausen_2026]: https://doi.org/10.21741/9781644904251-86
[research_rigden_1938]: https://doi.org/10.1038/141082a0
[research_rinauto_gupta_2017]: https://doi.org/10.2514/6.2017-1159
[research_rios_tamayo_2017]: https://doi.org/10.2316/p.2017.853-018
[research_risingjj_daviswj_1984]: https://ntrs.nasa.gov/citations/19850030442
[research_rist_1996]: https://doi.org/10.2514/6.1996-2403
[research_rithirun_charean_2021]: https://doi.org/10.1109/icpei52436.2021.9690689
[research_rivers_wahls_2001]: https://doi.org/10.2514/6.2001-2462
[research_robertson_1997]: https://doi.org/10.1049/ic:19971287
[research_robertspa_swaimrl_1977]: https://ntrs.nasa.gov/citations/19770016183
[research_roberttbiedron_davidlwhitaker_1994]: https://ntrs.nasa.gov/citations/19950007819
[research_robinson_1968]: https://doi.org/10.2514/6.1968-832
[research_robinson_1969]: https://doi.org/10.2514/3.44013
[research_robinson_wissler_1988]: https://doi.org/10.2514/6.1988-2577
[research_robinsonrb_1958]: https://ntrs.nasa.gov/citations/19650014456
[research_rocharibeiro_wolf_2025]: https://doi.org/10.26678/abcm.cobem2025.cob2025-2122
[research_rodchenko_zaichik_2002]: https://doi.org/10.2514/6.2002-4801
[research_rodchenko_zaichik_2003]: https://doi.org/10.2514/2.6920
[research_rodden_farkas_1962]: https://doi.org/10.21236/ad0295013
[research_rodden_giesing_1970]: https://doi.org/10.2514/3.44159
[research_rodgers_1963]: https://doi.org/10.21236/ad0404748
[research_rodriguezdecos_acosta_2020]: https://doi.org/10.1115/1.4047388
[research_rodzewicz_2024]: https://doi.org/10.24425/ame.2024.151335
[research_rogalski_2018]: https://doi.org/10.1108/aeat-02-2018-0088
[research_rogalski_rzucidlo_2020]: https://doi.org/10.1108/aeat-05-2019-0099
[research_rogalski_rzucidlo_2021]: https://doi.org/10.1108/aeat-11-2020-0269
[research_roganov_roganova_2017]: https://doi.org/10.2991/aime-17.2017.109
[research_rohani_jahangirian_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001494
[research_rohith_sinha_2017]: https://doi.org/10.1063/1.4972723
[research_rojascarvajal_amitay_2023]: https://doi.org/10.2514/6.2023-0456
[research_rolls_aoyagi_1977]: https://doi.org/10.2514/6.1977-805
[research_rolston_2001]: https://doi.org/10.2514/6.2001-2411
[research_rom_almosnino_1987]: https://doi.org/10.2514/6.1987-2275
[research_ronflenadaud_2009]: https://doi.org/10.21236/ada512960
[research_rong_2026]: https://doi.org/10.54254/2753-8818/2026.dl33792
[research_rooneyrh_chungjc_1982]: https://ntrs.nasa.gov/citations/19820055409
[research_roos_1996]: https://doi.org/10.2514/6.1996-543
[research_roos_2001]: https://doi.org/10.2514/2.2813
[research_rosa_belo_2021]: https://doi.org/10.1109/icuas51884.2021.9476810
[research_rosa_sanneman_1974]: https://doi.org/10.21236/ad0783690
[research_rosales_gross_2017]: https://doi.org/10.2514/6.2017-3920
[research_rosariogabriel_cortes_2018]: https://doi.org/10.1109/icuas.2018.8453350
[research_rosebergew_1982]: https://ntrs.nasa.gov/citations/19820012269
[research_rosic_diekmann_2015]: https://doi.org/10.2514/1.c032856
[research_ross_jacob_2019]: https://doi.org/10.2514/6.2019-3136
[research_rossetti_beblo_2022]: https://doi.org/10.2514/6.2022-1156
[research_rossi_miller_1999]: https://doi.org/10.1016/s0167-6911(99)00016-x
[research_roth_mavris_2001]: https://doi.org/10.2514/6.2001-391
[research_roy_bhasin_2019]: https://doi.org/10.1109/cdc40024.2019.9029970
[research_roy_biswas_2023]: https://doi.org/10.18311/jmmf/2023/35861
[research_roy_mukherjee_2021]: https://doi.org/10.2514/6.2021-1197
[research_roy_sengupta_2017]: https://doi.org/10.1109/calcon.2017.8280696
[research_rs_2024]: https://doi.org/10.69759/ijadr1101
[research_rs_a_2018]: https://doi.org/10.5539/mas.v12n10p195
[research_ruan_aagren_2025]: https://doi.org/10.4050/f-0081-2025-0283
[research_rubertusdp_1983]: https://ntrs.nasa.gov/citations/19830025631
[research_rubin_mummolo_1973]: https://doi.org/10.21236/ad0773362
[research_ruetten_2018]: https://doi.org/10.2514/6.2018-3340
[research_ruflin_grantham_1984]: https://doi.org/10.2514/6.1984-2096
[research_ruifeng_2015]: https://doi.org/10.1088/0169-5983/47/4/045503
[research_russell_werner_2022]: https://doi.org/10.2514/6.2022-0158
[research_rutkay_laliberte_2016]: https://doi.org/10.1139/juvs-2014-0019
[research_rutowski_1954]: https://doi.org/10.2514/8.2956
[research_ryangeorgewiii_downingdavidr_1993]: https://ntrs.nasa.gov/citations/19930064333
[research_ryanlaurae_1990]: https://ntrs.nasa.gov/citations/19900011620
[research_rynaski_1994]: https://doi.org/10.2514/6.1994-3514
[research_rysdyk_calise_1998]: https://doi.org/10.2514/6.1998-4483
[research_rysdyk_calise_1999]: https://doi.org/10.2514/2.4411
[research_s_c_2025]: https://doi.org/10.1108/aeat-08-2024-0241
[research_sabo_bugaj_2021]: https://doi.org/10.26552/pas.z.2021.1.25
[research_sabra_hafez_2025]: https://doi.org/10.1109/iceeng64546.2025.11031385
[research_sachan_r_2025]: https://doi.org/10.1109/space65882.2025.11170809
[research_sacksalvinh_1954]: https://ntrs.nasa.gov/citations/19930083872
[research_sadeghi_1984]: https://doi.org/10.1109/cdc.1984.272088
[research_saderla_dhayalan_2016]: https://doi.org/10.14429/dsj.67.9995
[research_saderla_r_2016]: https://doi.org/10.1108/ijius-07-2015-0008
[research_saderla_rajaram_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000679
[research_sadovnitchii_ryabkov_1997]: https://doi.org/10.2514/6.1997-3792
[research_sadovnychiy_betin_1998]: https://doi.org/10.2514/6.1998-4166
[research_sadraey_2017]: https://doi.org/10.2514/6.2017-3731
[research_saeed_graham_2015]: https://doi.org/10.2514/1.c032862
[research_saephan_vandam_2006]: https://doi.org/10.2514/6.2006-3321
[research_saephan_vandam_2006_b]: https://doi.org/10.2514/6.2006-6131
[research_saetti_rogers_2020]: https://doi.org/10.4050/sm_2020_hq-916
[research_saetti_rogers_2024]: https://doi.org/10.4050/jahs.69.042007
[research_safie_yunus_2024]: https://doi.org/10.1109/icsima62563.2024.10675578
[research_safonov_athans_1976]: https://doi.org/10.1109/cdc.1976.267760
[research_safonov_athans_1977]: https://doi.org/10.1109/tac.1977.1101470
[research_safwat_zhang_2018]: https://doi.org/10.1109/gncc42960.2018.9018990
[research_sagan_krishnamurthy_2021]: https://doi.org/10.2514/6.2021-3216
[research_sahasrabudhe_celi_1997]: https://doi.org/10.2514/2.2251
[research_sahin_yayla_2026]: https://doi.org/10.1016/j.ast.2026.113372
[research_saini_kumar_2024]: https://doi.org/10.1002/acs.3823
[research_saiteja_vaghela_2017]: https://doi.org/10.18520/cs/v112/i05/1020-1023
[research_sakata_2002]: https://doi.org/10.2514/6.2002-527
[research_salagame_pandya_2025]: https://doi.org/10.1109/lcsys.2025.3589412
[research_salahudden_2024]: https://doi.org/10.1016/j.conengprac.2024.105872
[research_salahudden_2025]: https://doi.org/10.1109/taes.2024.3485604
[research_salahudden_agrawal_2024]: https://doi.org/10.1016/j.ast.2024.109156
[research_salahudden_das_2022]: https://doi.org/10.1109/taes.2022.3146114
[research_salahudden_ghosh_2021]: https://doi.org/10.1016/j.ast.2021.106823
[research_salahudden_giri_2020]: https://doi.org/10.1109/icuas48674.2020.9213975
[research_salahudden_kumar_2025]: https://doi.org/10.2514/6.2025-1053
[research_salahudden_singh_2024]: https://doi.org/10.2514/6.2024-4654
[research_salehian_khan_2022]: https://doi.org/10.2514/6.2022-0939
[research_salehian_khan_2024]: https://doi.org/10.2514/6.2024-0301
[research_salehian_khan_2025]: https://doi.org/10.2514/6.2025-2405
[research_salinas_slawinski_2015]: https://doi.org/10.1155/2015/305314
[research_samoylovitch_strelets_2000]: https://doi.org/10.1016/s1369-8869(00)00012-4
[research_sanchez_cajas_2024]: https://doi.org/10.3846/aviation.2024.22577
[research_sanchezrivera_lozano_2019]: https://doi.org/10.1109/icuas.2019.8797952
[research_sanchezrivera_lozano_2020]: https://doi.org/10.1109/icuas48674.2020.9214061
[research_sanci_okegunel_2024]: https://doi.org/10.1007/s11063-024-11456-9
[research_sanders_1997]: https://doi.org/10.2514/2.2213
[research_sanfilippo_1970]: https://doi.org/10.2514/6.1970-962
[research_sangermburkjr_charleselibbey_1961]: https://ntrs.nasa.gov/citations/19720075828
[research_santos_honorio_2022]: https://doi.org/10.1016/j.isatra.2021.08.010
[research_saporito_daronch_2021]: https://doi.org/10.2514/6.2021-3101
[research_saraf_deodhare_1998]: https://doi.org/10.2514/6.1998-4206
[research_saraswathi_2000]: https://doi.org/10.14429/dsj.50.3366
[research_sarathy_murthy_1993]: https://doi.org/10.2514/6.1993-3550
[research_sarathy_murthy_1993_b]: https://doi.org/10.2514/6.1993-3618
[research_sariyildiz_mutlu_2018]: https://doi.org/10.1016/j.ejcon.2018.01.002
[research_sarker_pudasaini_2026]: https://doi.org/10.4050/sm-2026-vlada-5186
[research_sarrafian_1984]: https://doi.org/10.2514/6.1984-2095
[research_sarrafian_1986]: https://doi.org/10.2514/3.20070
[research_sato_kashihara_2021]: https://doi.org/10.1109/iv48863.2021.9575817
[research_sato_muraoka_2015]: https://doi.org/10.2514/1.g000263
[research_sato_muraoka_2017]: https://doi.org/10.2514/1.c034244
[research_satoh_sugimoto_2002]: https://doi.org/10.3166/ejc.8.213-219
[research_saunders_1996]: https://doi.org/10.2514/6.1996-227
[research_saxena_faruque_2016]: https://doi.org/10.2514/6.2016-3712
[research_sayyed_konar_2025]: https://doi.org/10.1109/icc69100.2025.11372428
[research_schaefer_bekemeyer_2024]: https://doi.org/10.2514/6.2024-2532
[research_schaefer_cary_2019]: https://doi.org/10.2514/6.2019-1492
[research_schaeffler_rediniotis_1995]: https://doi.org/10.2514/6.1995-116
[research_schaff_prazenica_2024]: https://doi.org/10.2514/6.2024-0344
[research_schaff_prazenica_2025]: https://doi.org/10.2514/6.2025-0347
[research_schairer_1964]: https://doi.org/10.2514/3.27731
[research_schalk_2017]: https://doi.org/10.1109/icnsurv.2017.8012018
[research_schierman_devore_2015]: https://doi.org/10.21236/ad1010277
[research_schiermanjohnd_schmidtdavidk_1991]: https://ntrs.nasa.gov/citations/19910065117
[research_schiff_1971]: https://doi.org/10.2514/6.1971-275
[research_schirmer_capone_1989]: https://doi.org/10.2514/6.1989-2812
[research_schmidt_1983]: https://doi.org/10.2514/6.1983-2074
[research_schmidt_1985]: https://doi.org/10.1115/85-igt-150
[research_schmidt_danowsky_2019]: https://doi.org/10.2514/6.2019-1816
[research_schmidt_hartl_2025]: https://doi.org/10.2514/6.2025-3660
[research_schmidtdavidk_newmanbrett_1990]: https://ntrs.nasa.gov/citations/19900060644
[research_schnell_2023]: https://doi.org/10.2514/6.2023-3726
[research_schnetter_kaste_2015]: https://doi.org/10.2514/6.2015-1323
[research_scholcover_gillan_2017]: https://doi.org/10.1177/0018720817734727
[research_schoombie_tuling_2017]: https://doi.org/10.1016/j.ast.2017.06.011
[research_schrader_reynolds_1988]: https://doi.org/10.2514/6.1988-122
[research_schrage_1990]: https://doi.org/10.2514/6.1990-3300
[research_schreadley_1977]: https://doi.org/10.21236/ada043979
[research_schroeder_chung_1998]: https://doi.org/10.2514/6.1998-4333
[research_schuck_1959]: https://doi.org/10.1109/tac.1959.1104871
[research_schuck_1960]: https://doi.org/10.1016/s1474-6670(17)70145-0
[research_schultz_zagalsky_1972]: https://doi.org/10.2514/3.44326
[research_schumacher_1952]: https://doi.org/10.21236/ada075866
[research_schumacher_1999]: https://doi.org/10.2514/6.1999-4086
[research_schuman_1981]: https://doi.org/10.21236/ada096048
[research_schwanz_1972]: https://doi.org/10.21236/ada006391
[research_schwanz_grimes_1980]: https://doi.org/10.2514/6.1980-1635
[research_schwartz_malick_1957]: https://doi.org/10.1108/eb032869
[research_schwartz_shearer_1964]: https://doi.org/10.2514/6.1964-773
[research_schwithal_wallace_2025]: https://doi.org/10.2514/6.2025-1825
[research_scordamaglia_mattei_2025]: https://doi.org/10.1109/ojcsys.2025.3619810
[research_scott_1977]: https://doi.org/10.1108/eb035363
[research_scott_2021]: https://doi.org/10.2514/6.2021-1062
[research_seaberg_etter_1972]: https://doi.org/10.4271/720857
[research_seacordcharlesl_campbelljohnp_1945]: https://ntrs.nasa.gov/citations/19930092552
[research_seaver_bennett_2023]: https://doi.org/10.2514/6.2023-3293
[research_sedlacek_breitsamter_2022]: https://doi.org/10.2514/6.2022-0565
[research_sedlackova_kurdel_2020]: https://doi.org/10.1016/j.trpro.2020.02.037
[research_sedlmair_theis_2022]: https://doi.org/10.2514/1.g005917
[research_seiferth_kugler_2018]: https://doi.org/10.2514/6.2018-4276
[research_seiffalvin_sandahlcarla_1951]: https://ntrs.nasa.gov/citations/20030067331
[research_sellerswilliamliii_meyersjamesf_1988]: https://ntrs.nasa.gov/citations/19890040847
[research_sellerswilliamliii_meyersjamesf_2004]: https://ntrs.nasa.gov/citations/20040161542
[research_semmelhack_hoppe_1967]: https://doi.org/10.1109/sap.1967.272966
[research_sens_1978]: https://doi.org/10.1115/78-gt-192
[research_seo_kim_2019]: https://doi.org/10.2514/6.2019-0112
[research_sepulvedapalacios_smith_2019]: https://doi.org/10.1108/aeat-09-2018-0249
[research_seraj_martins_2022]: https://doi.org/10.2514/1.c036618
[research_seres_liu_2023]: https://doi.org/10.1016/j.ifacol.2023.10.1097
[research_servo_control_device_1984]: https://doi.org/10.1016/0094-114x(84)90080-6
[research_setati_botha_2022]: https://doi.org/10.1051/matecconf/202237005001
[research_setiawarman_sasongko_2026]: https://doi.org/10.1142/s2737480726400078
[research_sever_demir_2025]: https://doi.org/10.1016/j.ast.2024.109682
[research_sezer_siljak_1980]: https://doi.org/10.1109/cdc.1980.271927
[research_sezer_siljak_1981]: https://doi.org/10.1109/tac.1981.1102740
[research_shafer_smith_1983]: https://doi.org/10.2514/6.1983-2107
[research_shah_2017]: https://doi.org/10.2514/6.2017-3568
[research_shah_granda_1998]: https://doi.org/10.2514/6.1998-4448
[research_shahgautamh_1991]: https://ntrs.nasa.gov/citations/19910062564
[research_shahjahan_enriquez_2026]: https://doi.org/10.2514/6.2026-0891
[research_shams_alishah_2018]: https://doi.org/10.1109/inmic.2018.8595611
[research_shams_khouli_2023]: https://doi.org/10.2514/6.2023-0337
[research_shankar_l_2023]: https://doi.org/10.18090/samriddhi.v15i03.06
[research_shankar_yedavalli_2004]: https://doi.org/10.2514/6.2004-4871
[research_shao_chen_2019]: https://doi.org/10.1109/tnnls.2019.2893643
[research_sharif_2019]: https://doi.org/10.2514/6.2019-2288
[research_sharif_2022]: https://doi.org/10.2514/6.2022-1504
[research_sharma_hosder_2021]: https://doi.org/10.2514/6.2021-0114
[research_sharma_rajamani_2024]: https://doi.org/10.23919/acc60939.2024.10644988
[research_sharma_sekaran_1998]: https://doi.org/10.2514/6.1998-4274
[research_sharpe_hansman_2024]: https://doi.org/10.2514/6.2024-1306
[research_shayak_girdhar_2024]: https://doi.org/10.3389/fpace.2024.1308872
[research_shayan_vankampen_2021]: https://doi.org/10.2514/6.2021-0884
[research_shearwood_nabawy_2019]: https://doi.org/10.2514/6.2019-3686
[research_shearwood_nabawy_2020]: https://doi.org/10.3390/aerospace7100150
[research_shearwood_nabawy_2020_b]: https://doi.org/10.2514/6.2020-2677
[research_shearwood_nabawy_2021]: https://doi.org/10.2514/6.2021-1826
[research_shearwood_nabawy_2021_b]: https://doi.org/10.2514/6.2021-2530
[research_shekarriz_fu_1991]: https://doi.org/10.2514/6.1991-3307
[research_shen_chen_2025]: https://doi.org/10.3390/drones9090624
[research_shen_lv_2025]: https://doi.org/10.23919/ccc64809.2025.11178710
[research_shen_wang_2023]: https://doi.org/10.1002/acs.3705
[research_shen_xu_2021]: https://doi.org/10.1016/j.ast.2021.107062
[research_shendge_2021]: https://doi.org/10.22214/ijraset.2021.37787
[research_shenoy_manjunatha_2023]: https://doi.org/10.1109/icsses58299.2023.10199786
[research_sherbaum_lichtsinder_1998]: https://doi.org/10.1515/tjj.1998.15.2.91
[research_sheridan_jr_1968]: https://doi.org/10.21236/ad0683787
[research_shi_hui_2024]: https://doi.org/10.1115/gt2024-126499
[research_shi_liu_2021]: https://doi.org/10.1109/cac53003.2021.9727275
[research_shi_wan_2015]: https://doi.org/10.1108/aeat-01-2013-0004
[research_shi_wang_2023]: https://doi.org/10.1088/1742-6596/2658/1/012023
[research_shi_wu_2022]: https://doi.org/10.1016/j.procs.2022.10.049
[research_shin_johnson_2003]: https://doi.org/10.2514/6.2003-5717
[research_shin_kim_2004]: https://doi.org/10.1109/tcst.2003.821957
[research_shinjongyeob_belcastrochristine_2008]: https://ntrs.nasa.gov/citations/20080033682
[research_shinoda_niwa_1998]: https://doi.org/10.1163/156855399x00685
[research_shinoda_niwa_1999]: https://doi.org/10.1163/156855399x01486
[research_shishkin_2025]: https://doi.org/10.30898/1684-1719.2025.8.12
[research_shivam_verma_2019]: https://doi.org/10.13111/2066-8201.2019.11.2.14
[research_shlien_1991]: https://doi.org/10.2514/6.1991-2931
[research_shmelv_vladov_2019]: https://doi.org/10.30929/1995-0519.2019.1.27-32
[research_shmilovich_princen_2026]: https://doi.org/10.2514/1.c038755
[research_shojae_salehi_2025]: https://doi.org/10.1016/j.oceaneng.2025.121086
[research_shomber_gertsen_1967]: https://doi.org/10.2514/3.43851
[research_shore_bodson_2004]: https://doi.org/10.23919/acc.2004.1384495
[research_shrivastava_stengel_1989]: https://doi.org/10.2514/3.20369
[research_shtessel_buffington_1999]: https://doi.org/10.2514/6.1999-4136
[research_shtessel_buffington_1999_b]: https://doi.org/10.2514/2.4465
[research_shtessel_buffington_2002]: https://doi.org/10.1109/87.987075
[research_shuang_zhang_2016]: https://doi.org/10.1109/cgncc.2016.7828825
[research_shubert_jones_2025]: https://doi.org/10.4050/sm_handling_2025-5291
[research_shufan_heng_2017]: https://doi.org/10.1109/iccsec.2017.8446702
[research_shukla_benyamen_2025]: https://doi.org/10.1109/tcst.2024.3516383
[research_shukla_mitra_2026]: https://doi.org/10.1615/interjfluidmechres.2025058570
[research_shuo_tuan_2025]: https://doi.org/10.1109/icesa66763.2025.11281122
[research_siegel_1961]: https://doi.org/10.1109/tap.1961.1144970
[research_sijabat_indriyanto_2021]: https://doi.org/10.47355/avia.v2i2.19
[research_silva_dewagter_2018]: https://doi.org/10.1142/s2301385018500024
[research_silva_nunes_2022]: https://doi.org/10.2514/6.2022-0689
[research_silva_souza_2026]: https://doi.org/10.2514/6.2026-4386
[research_silva_wolf_2024]: https://doi.org/10.26678/abcm.eptt2024.ept24-0024
[research_silva_wolf_2026]: https://doi.org/10.2514/6.2026-2683
[research_silvershnorman_fournierrogerh_1958]: https://ntrs.nasa.gov/citations/20050028468
[research_simmons_2022]: https://doi.org/10.2514/6.2022-2409
[research_simmons_2023]: https://doi.org/10.2514/1.c036896
[research_simmons_ackerman_2026]: https://doi.org/10.2514/6.2026-2088
[research_simmons_gresham_2023]: https://doi.org/10.2514/1.c037260
[research_simmons_gresham_2023_b]: https://doi.org/10.2514/1.c036773
[research_simmons_gresham_2023_c]: https://doi.org/10.2514/1.c037259
[research_simmons_gresham_2023_d]: https://doi.org/10.2514/6.2023-0040
[research_simmons_mcclelland_2019]: https://doi.org/10.2514/1.c035160
[research_simmons_murphy_2021]: https://doi.org/10.2514/6.2021-1298
[research_simon_blake_1993]: https://doi.org/10.2514/6.1993-4000
[research_simon_williams_2023]: https://doi.org/10.2514/6.2023-3565
[research_simon_williams_2024]: https://doi.org/10.2514/6.2024-0491
[research_simon_zekry_2025]: https://doi.org/10.2514/6.2025-0004
[research_simpson_1972]: https://doi.org/10.2514/6.1972-785
[research_simpson_1979]: https://doi.org/10.21236/ada075226
[research_singh_2025]: https://doi.org/10.54941/ahfe1006896
[research_singh_jategaonkar_1996]: https://doi.org/10.2514/3.46993
[research_singh_jategaonkar_1996_b]: https://doi.org/10.2514/6.1996-3441
[research_singh_lambeth_2024]: https://doi.org/10.1109/lcsys.2023.3342094
[research_singh_padhy_2017]: https://doi.org/10.1109/icpces.2017.8117658
[research_singh_raol_2000]: https://doi.org/10.1017/s0001924000091442
[research_singh_steinberg_1996]: https://doi.org/10.2514/3.21712
[research_singh_steinberg_1999]: https://doi.org/10.2514/6.1999-4280
[research_singhal_thorpe_2019]: https://doi.org/10.4050/f-0075-2019-14600
[research_singhb_1986]: https://ntrs.nasa.gov/citations/19910014895
[research_singkang_singh_2024]: https://doi.org/10.1109/cybercom63683.2024.10803126
[research_sinha_2004]: https://doi.org/10.2514/6.2004-2121
[research_sinha_ananthkrishnan_2002]: https://doi.org/10.2514/2.3014
[research_sirbaugh_1983]: https://doi.org/10.2514/6.1983-1850
[research_sisson_dogan_2025]: https://doi.org/10.2514/6.2025-2799
[research_sisson_sarioglu_2024]: https://doi.org/10.1109/cdc56724.2024.10885988
[research_sivan_1971]: https://doi.org/10.2514/6.1971-792
[research_siwakosit_hess_2001]: https://doi.org/10.2514/2.4841
[research_siwakosit_snell_2000]: https://doi.org/10.1109/87.845879
[research_sizlotr_bergra_1979]: https://ntrs.nasa.gov/citations/19820024501
[research_skarka_mateja_2024]: https://doi.org/10.1109/uvs59630.2024.10467148
[research_sklaroff_kilmer_1973]: https://doi.org/10.2514/6.1973-846
[research_skow_moore_1982]: https://doi.org/10.2514/3.61562
[research_skowam_peakedj_1983]: https://ntrs.nasa.gov/citations/19840002021
[research_slaby_hartley_1985]: https://doi.org/10.1177/154193128502901214
[research_sliwasm_1980]: https://ntrs.nasa.gov/citations/19810005457
[research_slongo_moraes_2020]: https://doi.org/10.5028/jatm.cab.1150
[research_sluis_dellacorte_2023]: https://doi.org/10.2514/6.2023-4069
[research_smetanafo_summerydc_1972]: https://ntrs.nasa.gov/citations/19720017341
[research_smit_craig_1998]: https://doi.org/10.2514/6.1998-4132
[research_smit_pollack_2022]: https://doi.org/10.2514/6.2022-1394
[research_smith_1977_b]: https://doi.org/10.21236/ada069198
[research_smith_1991]: https://doi.org/10.1177/002029409102400303
[research_smith_1994]: https://doi.org/10.2514/6.1994-3516
[research_smith_1998]: https://doi.org/10.2514/6.1998-4461
[research_smith_2023]: https://doi.org/10.4050/sm_2023_hq-1192
[research_smith_berry_2000]: https://doi.org/10.2514/6.2000-3914
[research_smith_garland_1992]: https://doi.org/10.2514/6.1992-3094
[research_smith_geddes_1979]: https://doi.org/10.21236/ada077858
[research_smith_meyer_1984]: https://doi.org/10.2514/6.1984-2627
[research_smith_meyer_1987]: https://doi.org/10.2514/3.20213
[research_smith_patel_1995]: https://doi.org/10.2514/6.1995-3452
[research_smith_sarrafian_1986]: https://doi.org/10.2514/3.20149
[research_smith_ward_1998]: https://doi.org/10.2514/6.1998-4201
[research_smithfm_1960]: https://ntrs.nasa.gov/citations/19650014315
[research_smithjw_edwardsjw_1980]: https://ntrs.nasa.gov/citations/19800012870
[research_smithmarks_moestimothyr_2003]: https://ntrs.nasa.gov/citations/20030079970
[research_smithrh_chisholmjd_1991]: https://ntrs.nasa.gov/citations/19910039021
[research_smithrogerse_schroederkurtc_1986]: https://ntrs.nasa.gov/citations/19870060567
[research_snell_1992]: https://doi.org/10.2514/6.1992-4330
[research_snell_1993]: https://doi.org/10.2514/6.1993-3775
[research_snell_enns_1992]: https://doi.org/10.2514/3.20932
[research_snell_garrardjr_1990]: https://doi.org/10.2514/6.1990-3406
[research_snell_garrardjr_1991]: https://doi.org/10.2514/6.1991-2711
[research_snell_hess_1998]: https://doi.org/10.2514/6.1998-4421
[research_snell_stout_1994]: https://doi.org/10.1016/s1474-6670(17)45810-1
[research_snell_stout_1998]: https://doi.org/10.1115/1.2802411
[research_snow_1990]: https://doi.org/10.4271/901848
[research_sobel_chung_1983]: https://doi.org/10.23919/acc.1983.4788322
[research_sobel_shapiro_1984]: https://doi.org/10.1109/cdc.1984.272270
[research_sobhani_jayasuriya_1994]: https://doi.org/10.1115/1.2899257
[research_sobron_lundstrom_2021]: https://doi.org/10.3390/aerospace8030074
[research_soinne_1999]: https://doi.org/10.2514/6.1999-3147
[research_sokolov_beklemichev_2017]: https://doi.org/10.5220/0006477504940501
[research_solies_1994]: https://doi.org/10.2514/3.46602
[research_solies_1995]: https://doi.org/10.2514/6.1995-3912
[research_soloway_haley_2000]: https://doi.org/10.2514/6.2000-5328
[research_soltmann_hall_2017]: https://doi.org/10.2514/1.c033982
[research_somashekar_immanuelselwynraj_2018]: https://doi.org/10.1088/1757-899x/376/1/012046
[research_son_sa_2015]: https://doi.org/10.6112/kscfe.2015.20.2.073
[research_son_sa_2015_b]: https://doi.org/10.1007/s12206-015-0720-y
[research_song_2008]: https://doi.org/10.21236/ada477568
[research_song_han_2016]: https://doi.org/10.2514/6.2016-3869
[research_song_huang_2026]: https://doi.org/10.3390/s26031078
[research_song_sanchezcuevas_2022]: https://doi.org/10.1109/icuas54217.2022.9836134
[research_song_song_2002]: https://doi.org/10.1007/bf03185230
[research_song_yang_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000625
[research_soundararajan_btn_2022]: https://doi.org/10.1108/aeat-12-2021-0387
[research_soundararajan_sridhar_2024]: https://doi.org/10.1017/aer.2024.121
[research_souza_castillozuniga_2019]: https://doi.org/10.26678/abcm.diname2019.din2019-0192
[research_sowers_tabakoff_1983]: https://doi.org/10.2514/6.1983-88
[research_spaans_gilbert_2024]: https://doi.org/10.1109/icuas60882.2024.10556907
[research_sparavalo_2021]: https://doi.org/10.1007/s13272-021-00526-6
[research_sparks]: https://doi.org/10.1109/cca.1998.728594
[research_sparks_2003]: https://doi.org/10.1016/s0005-1098(03)00102-x
[research_sparks_buffington_1994]: https://doi.org/10.1080/00207179408923110
[research_sparks_sparks_1997]: https://doi.org/10.2514/6.1997-3636
[research_spearmanml_1979]: https://ntrs.nasa.gov/citations/19790043411
[research_speyer_crues_1985]: https://doi.org/10.2514/6.1985-1762
[research_speyer_crues_1987]: https://doi.org/10.2514/3.20212
[research_spreiter_stahara_1970]: https://doi.org/10.2514/6.1970-798
[research_spurlin_lueck_1984]: https://doi.org/10.2514/6.1984-612
[research_srazhidinov_liang_2023]: https://doi.org/10.1016/j.ifacol.2023.10.1881
[research_sreejith_sathyabhama_2020]: https://doi.org/10.1007/s40430-020-2229-2
[research_srinathkumar_2015]: https://doi.org/10.4050/jahs.60.022010
[research_srinathkumar_parameswaran_1995]: https://doi.org/10.2514/6.1995-3501
[research_srinivasa_sridhara_2016]: https://doi.org/10.1109/aero.2016.7500911
[research_srivastava_duraisamy_2018]: https://doi.org/10.2514/6.2018-2175
[research_ss_networked_2017]: https://doi.org/10.1109/iecon.2017.8217259
[research_stable_multiple_1999]: https://doi.org/10.1109/acc.1999.786187
[research_stalford_1979]: https://doi.org/10.21236/ada080025
[research_stalford_hoffman_1989]: https://doi.org/10.2514/6.1989-3521
[research_stam_devisser_2025]: https://doi.org/10.2514/6.2025-0082
[research_stanek_visbal_1991]: https://doi.org/10.2514/6.1991-3273
[research_stanley_1980]: https://doi.org/10.2514/6.1980-1867
[research_starke_1983]: https://doi.org/10.2514/6.1983-2740
[research_starr_varner_1976]: https://doi.org/10.2514/6.1976-90
[research_steer_2000]: https://doi.org/10.1017/s0001924000091533
[research_steer_2000_b]: https://doi.org/10.2514/6.2000-4109
[research_stein_hartmann_1975]: https://doi.org/10.1109/cdc.1975.270682
[research_stein_hartmann_1977]: https://doi.org/10.1109/tac.1977.1101605
[research_steinberg_1999]: https://doi.org/10.2514/6.1999-4044
[research_steinberg_2001]: https://doi.org/10.2514/2.4796
[research_steinberg_carlson_1989]: https://doi.org/10.1109/5.32057
[research_steinberg_digirolamo_1991]: https://doi.org/10.1109/ijcnn.1991.155479
[research_steinberg_page_1998]: https://doi.org/10.2514/6.1998-4230
[research_steinberg_page_1999]: https://doi.org/10.1002/(sici)1099-1239(19991215)9:14<1097::aid-rnc454>3.0.co;2-9
[research_steinhoff_2002]: https://doi.org/10.21236/ada410942
[research_steinleitner_frenzel_2022]: https://doi.org/10.2514/6.2022-1228
[research_steinmetzgg_parrishrv_1972]: https://ntrs.nasa.gov/citations/19720010363
[research_stenfelt_ringertz_2009]: https://doi.org/10.2514/1.41092
[research_stenfelt_ringertz_2010]: https://doi.org/10.2514/1.c031017
[research_stenfelt_ringertz_2013]: https://doi.org/10.2514/1.c031868
[research_stengel_1975]: https://doi.org/10.2514/3.44482
[research_stengel_1980]: https://doi.org/10.2514/3.55959
[research_stengel_miller_1978]: https://doi.org/10.2514/6.1978-1361
[research_stephan_stumpf_2023]: https://doi.org/10.2514/1.c036717
[research_stephens_1931]: https://doi.org/10.1108/eb029443
[research_stewart_dooher_2026]: https://doi.org/10.3390/aerospace13070616
[research_stewartjamesf_shuckthomasl_1990]: https://ntrs.nasa.gov/citations/19900015828
[research_stifel_1979]: https://doi.org/10.21236/ada085873
[research_stojanovic_ljdebeljkovic_2004]: https://doi.org/10.1142/9789812702289_0021
[research_stojanovic_ljdebeljkovic_2004_b]: https://doi.org/10.1142/9789812702289_0004
[research_stolarik_2007]: https://doi.org/10.21236/ada470308
[research_stoldt_johansen_2020]: https://doi.org/10.2514/6.2020-2758
[research_stoldt_korobenko_2021]: https://doi.org/10.1115/1.4052150
[research_stollf_koenigdg_1983]: https://ntrs.nasa.gov/citations/19830067155
[research_storms_tilbury_2015]: https://doi.org/10.1109/icra.2015.7139813
[research_stortzmichaelw_odonoghuedennisp_1995]: https://ntrs.nasa.gov/citations/19960020260
[research_stouder_1981]: https://doi.org/10.2514/6.1981-2398
[research_stougie_pollack_2024]: https://doi.org/10.2514/6.2024-2565
[research_strader_harper_2016]: https://doi.org/10.2514/6.2016-3653
[research_stradtner_bekemeyer_2025]: https://doi.org/10.2514/1.c038179
[research_strelkov_bozhko_2026]: https://doi.org/10.46684/2026.2.3
[research_stremel_1994]: https://doi.org/10.2514/3.12007
[research_stricklandmarke_bundickwthomas_1996]: https://ntrs.nasa.gov/citations/19960027892
[research_study_of_2023]: https://doi.org/10.36652/0869-4931-2023-77-10-460-465
[research_su_chu_2022]: https://doi.org/10.1109/iros47612.2022.9981140
[research_su_shyr_1993]: https://doi.org/10.23919/acc.1993.4793029
[research_suarezcarlosj_kramerbrianr_1992]: https://ntrs.nasa.gov/citations/19920062931
[research_suarezcarlosj_malcolmgeraldn_1992]: https://ntrs.nasa.gov/citations/19920039520
[research_suarezcarlosj_smithbrookec_1993]: https://ntrs.nasa.gov/citations/19940011307
[research_subagyo_2019]: https://doi.org/10.30536/j.jtd.2019.v17.a3033
[research_subbarao_tule_2015]: https://doi.org/10.2514/6.2015-2857
[research_sudderthrw_bohnjg_1975]: https://ntrs.nasa.gov/citations/19750012273
[research_suga_yamazaki_2015]: https://doi.org/10.2514/6.2015-1815
[research_sugino_harada_2019]: https://doi.org/10.1299/jsmemovic.2019.16.c112
[research_sun_boyd_2004]: https://doi.org/10.1017/s0022112003007717
[research_sun_carmody_2026]: https://doi.org/10.2514/6.2026-0711
[research_sun_devisser_2019]: https://doi.org/10.2514/1.c035135
[research_sun_liu_2025]: https://doi.org/10.3390/electronics14163288
[research_sun_sengupta_2022]: https://doi.org/10.1109/ssci51031.2022.10022215
[research_sun_shi_2020]: https://doi.org/10.1016/j.ast.2020.106126
[research_sun_vankampen_2021]: https://doi.org/10.2514/1.g005715
[research_sun_wang_2020]: https://doi.org/10.3390/act9040122
[research_sundaram_wu_1983]: https://doi.org/10.2514/6.1983-1852
[research_sung_spreizer_2025]: https://doi.org/10.1115/detc2025-168977
[research_surmann_myschik_2024]: https://doi.org/10.4050/f-0080-2024-1206
[research_suryakumar_babbar_2016]: https://doi.org/10.2514/1.c033602
[research_sutherland_maass_1932]: https://doi.org/10.1139/cjr32-033
[research_swaim_1977]: https://doi.org/10.2514/6.1977-1125
[research_swaim_1978]: https://doi.org/10.2514/6.1978-1365
[research_swaim_connor_1968]: https://doi.org/10.2514/3.43907
[research_swaim_yen_1979]: https://doi.org/10.2514/3.58579
[research_swankaaronj_2012]: https://ntrs.nasa.gov/citations/20120016864
[research_swarnkar_kothari_2016]: https://doi.org/10.1016/j.ifacol.2016.03.117
[research_syed_erhart_1990]: https://doi.org/10.2514/6.1990-2023
[research_syed_erhart_1992]: https://doi.org/10.2514/3.23552
[research_symposium_on_2003]: https://ntrs.nasa.gov/citations/20040040215
[research_szabolcsi_2018]: https://doi.org/10.19062/1842-9238.2018.16.1.5
[research_szabolcsi_2018_b]: https://doi.org/10.19062/1842-9238.2018.16.1.7
[research_szabolcsi_2018_c]: https://doi.org/10.19062/1842-9238.2018.16.3.6
[research_szymanski_ghazi_2025]: https://doi.org/10.2514/6.2025-2228
[research_tachinina_lysenko_2024]: https://doi.org/10.1109/apuavd64488.2024.10765892
[research_taherinezhad_ramirezserrano_2023]: https://doi.org/10.3390/aerospace10100843
[research_tai_wang_2023]: https://doi.org/10.3390/aerospace10040350
[research_tai_wang_2026]: https://doi.org/10.2514/1.g009489
[research_taj_bilal_2023]: https://doi.org/10.1016/j.ast.2023.108114
[research_takarics_mocsanyi_2020]: https://doi.org/10.1109/gpmc50267.2020.9333823
[research_takita_kashitani_2016]: https://doi.org/10.1299/jsmedmc.2016.431
[research_tal_karaman_2021]: https://doi.org/10.2514/6.2021-3214
[research_tal_karaman_2022]: https://doi.org/10.2514/1.g006645
[research_tamaskani_alfi_2026]: https://doi.org/10.1016/j.ast.2026.111656
[research_tamboli_1956]: https://doi.org/10.1017/s0001925900010313
[research_tamrat_1988]: https://doi.org/10.2514/6.1988-4400
[research_tamrat_2004]: https://doi.org/10.2514/6.2004-5173
[research_tamura_oyama_2019]: https://doi.org/10.2514/6.2019-0033
[research_tan_2004]: https://doi.org/10.1016/j.compeleceng.2002.07.001
[research_tan_ma_2018]: https://doi.org/10.1109/yac.2018.8406385
[research_tang_lai_2020]: https://doi.org/10.1109/icuas48674.2020.9213987
[research_tang_zhao_2024]: https://doi.org/10.3390/a17050196
[research_tantrairatn_veres_2015]: https://doi.org/10.1109/icuas.2015.7152286
[research_tanveer_ahmad_2023]: https://doi.org/10.3390/aerospace10060563
[research_tanveer_ahmad_2023_b]: https://doi.org/10.3390/asec2023-15315
[research_tarlanov_kurbanismailov_2021]: https://doi.org/10.1088/1757-899x/1027/1/012027
[research_tate_gillard_1975]: https://doi.org/10.21236/ada018691
[research_tavakoli_2024]: https://doi.org/10.1049/ell2.13309
[research_tavella_lee_1986]: https://doi.org/10.2514/6.1986-1806
[research_tavella_lee_1987]: https://doi.org/10.2514/3.45485
[research_tavoularis_1999]: https://doi.org/10.2514/2.2526
[research_taylor_1988]: https://doi.org/10.2514/6.1988-2998
[research_taylor_2015]: https://doi.org/10.2514/6.2015-3408
[research_taylor_bennett_1992]: https://doi.org/10.2514/6.1992-170
[research_taylor_skow_1988]: https://doi.org/10.2514/3.45660
[research_teel_1999]: https://doi.org/10.21236/ada367012
[research_teel_1999_b]: https://doi.org/10.21236/ada367415
[research_tenhave_joiner_2026]: https://doi.org/10.3390/aerospace13010059
[research_teofilatto_2001]: https://doi.org/10.1016/s1369-8869(00)00025-2
[research_teper_stapleford_1965]: https://doi.org/10.2514/6.1965-1237
[research_teper_stapleford_1966]: https://doi.org/10.2514/3.43725
[research_terrell_zeinsabatto_2017]: https://doi.org/10.1109/secon.2017.7925309
[research_terry_1964]: https://doi.org/10.21236/ad0452725
[research_thacker_lan_1993]: https://doi.org/10.2514/6.1993-3617
[research_thamann_smith_2015]: https://doi.org/10.1139/juvs-2014-0024
[research_thatoelijah_ruivasconcellos_2026]: https://doi.org/10.59535/jece.v4i1.450
[research_the_design_of_2015]: https://doi.org/10.12677/airr.2015.41001
[research_theilliol_weber_2015]: https://doi.org/10.1109/icuas.2015.7152415
[research_theodore_celi_2002]: https://doi.org/10.2514/2.2995
[research_theys_devos_2016]: https://doi.org/10.1109/icuas.2016.7502519
[research_thomas_1991]: https://doi.org/10.2514/6.1991-3295
[research_thomas_paulsonjr_1977]: https://doi.org/10.2514/6.1977-887
[research_thompson_1965]: https://doi.org/10.2514/6.1965-1209
[research_thompson_1970]: https://doi.org/10.1080/00207177008905894
[research_thompson_chiang_1990]: https://doi.org/10.1109/cdc.1990.203419
[research_thompson_xu_2017]: https://doi.org/10.2514/1.c033898
[research_thompsonfl_gilruthrr_1940]: https://ntrs.nasa.gov/citations/19930081526
[research_thorsen_horn_2017]: https://doi.org/10.4050/sm_2017_hq-1256
[research_tian_2021]: https://doi.org/10.1515/auto-2020-0020
[research_tian_li_2015]: https://doi.org/10.3390/a8010003
[research_tian_zhou_2021]: https://doi.org/10.23919/ccc52363.2021.9550746
[research_tich_shaw_1987]: https://doi.org/10.2514/6.1987-1929
[research_ting_shun_2016]: https://doi.org/10.1109/chicc.2016.7554502
[research_tinger_1987]: https://doi.org/10.2514/6.1987-2561
[research_tinoco_2020]: https://doi.org/10.2514/6.2020-2745
[research_tipton_smith_1995]: https://doi.org/10.4271/952053
[research_tipton_smith_1996]: https://doi.org/10.2514/6.1996-408
[research_tischler_hoh_1982]: https://doi.org/10.2514/6.1982-1292
[research_tischlermarkb_fletcherjayw_1991]: https://ntrs.nasa.gov/citations/19910067397
[research_tissir_hmamed_1994]: https://doi.org/10.1016/0167-6911(94)90048-5
[research_tohidi_yildiz_2017]: https://doi.org/10.1016/j.ifacol.2017.08.1088
[research_tohidi_yildiz_2018]: https://doi.org/10.1109/ccta.2018.8511389
[research_tohidi_yildiz_2021]: https://doi.org/10.1109/ccta48906.2021.9659190
[research_tokugawa_ishida_2026]: https://doi.org/10.2514/1.c038397
[research_tokutake_ohta_1999]: https://doi.org/10.1016/s1474-6670(17)57356-5
[research_toloei_ghaderi_2026]: https://doi.org/10.1007/s42401-026-00472-3
[research_tomainerl_bryantwh_1978]: https://ntrs.nasa.gov/citations/19780061530
[research_tomczyk_1998]: https://doi.org/10.2514/6.1998-4253
[research_tomczyk_2001]: https://doi.org/10.2514/6.2001-4264
[research_tomczyk_2002]: https://doi.org/10.1108/00022660210448456
[research_tomlins_1983]: https://doi.org/10.1139/tcs-1983-0020
[research_toppings_yarusevych_2021]: https://doi.org/10.2514/6.2021-2819
[research_torres_candelas_2017]: https://doi.org/10.5220/0006186701530158
[research_torres_xu_2022]: https://doi.org/10.1115/imece2022-97224
[research_totah_totah_1997]: https://doi.org/10.2514/6.1997-3537
[research_tournes_johnson_1999]: https://doi.org/10.2514/6.1999-3982
[research_tournes_landrum_2003]: https://doi.org/10.2514/2.5028
[research_tournes_shtessel_1997]: https://doi.org/10.2514/6.1997-3633
[research_towfighi_rockwell_1993]: https://doi.org/10.2514/3.11744
[research_traas_atmaca_2026]: https://doi.org/10.2514/6.2026-0549
[research_tran_2025]: https://doi.org/10.56651/lqdtu.jst.v20.n02.934
[research_tran_sakamoto_2017]: https://doi.org/10.1016/j.ast.2017.05.010
[research_tran_sawan_1983]: https://doi.org/10.23919/acc.1983.4788153
[research_tranchero_latorre_2001]: https://doi.org/10.1016/s1474-6670(17)40763-4
[research_transonic_theory_1970]: https://doi.org/10.2514/6.1970-556
[research_traub_2021]: https://doi.org/10.2514/1.c036445
[research_traub_2024]: https://doi.org/10.2514/1.c037907
[research_traub_2024_b]: https://doi.org/10.3390/aerospace11040320
[research_traub_botero_2015]: https://doi.org/10.2514/1.c032559
[research_traub_coffman_2019]: https://doi.org/10.2514/1.c035515
[research_traub_moeller_1998]: https://doi.org/10.2514/2.2352
[research_travassos_kaufman_1979]: https://doi.org/10.2514/6.1979-1636
[research_traven_whitley_1995]: https://doi.org/10.21236/ada300965
[research_tribuno_klein_1976]: https://doi.org/10.21236/ada029021
[research_trippenseegary_1991]: https://ntrs.nasa.gov/citations/19920062783
[research_trueman_kubina_1993]: https://doi.org/10.1109/cjece.1993.6592816
[research_tsagkaris_holzapfel_2026]: https://doi.org/10.1109/icuas69441.2026.11598703
[research_tsai_chiang_2016]: https://doi.org/10.1109/iwem.2016.7504915
[research_tsench_kurbanov_2023]: https://doi.org/10.22314/2073-7599-2023-17-3-4-15
[research_tsench_kurbanov_2024]: https://doi.org/10.22314/2073-7599-2024-18-2-11-19
[research_tsien_1938]: https://doi.org/10.2514/8.722
[research_tsushima_saitoh_2024]: https://doi.org/10.2514/6.2024-2401
[research_tsutianlee_shiowharnlee_1988]: https://doi.org/10.1049/ip-d.1988.0072
[research_tsutsui_takagi_2021]: https://doi.org/10.2514/6.2021-0137
[research_tu_1992]: https://doi.org/10.2514/6.1992-2602
[research_tuckermanlb_1923]: https://ntrs.nasa.gov/citations/19930080922
[research_tumerdem_yilmaz_2021]: https://doi.org/10.1016/j.conengprac.2021.104931
[research_turner_padfield_2002]: https://doi.org/10.2514/2.3004
[research_tusa_nicolaescu_2015]: https://doi.org/10.1109/ecai.2015.7301211
[research_tvaryanas_2006]: https://doi.org/10.21236/ada444925
[research_tvaryanas_maupin_2013]: https://doi.org/10.21236/ada591019
[research_tvaryanas_singer_2012]: https://doi.org/10.21236/ada593691
[research_tzafestas_1975]: https://doi.org/10.1109/proc.1975.10040
[research_uchida_shimemura_1986]: https://doi.org/10.9746/sicetr1965.22.1222
[research_uddin_ryu_2016]: https://doi.org/10.1016/j.arcontrol.2016.09.003
[research_uhlig_selig_2017]: https://doi.org/10.2514/1.c033755
[research_ulizar_1997]: https://doi.org/10.1115/97-gt-258
[research_ummeaymon_shah_2016]: https://doi.org/10.1109/icet.2016.7813243
[research_unal_2021]: https://doi.org/10.1108/aeat-12-2020-0293
[research_ungermann_1988]: https://doi.org/10.1117/12.942263
[research_uppoor_chopra_2026]: https://doi.org/10.4050/f-0082-2026-0148
[research_uribe_marty_2017]: https://doi.org/10.2514/6.2017-4279
[research_uribequintero_takahashi_2024]: https://doi.org/10.2514/6.2024-4048
[research_urnes_davidson_2001]: https://doi.org/10.1109/acc.2001.946344
[research_urnesjamesm_hoystephene_1993]: https://ntrs.nasa.gov/citations/19930013179
[research_urnesjamesm_stewartjames_1990]: https://ntrs.nasa.gov/citations/19910003389
[research_uthra_antony_2020]: https://doi.org/10.4273/ijvss.12.3.22
[research_utsumi_2025]: https://doi.org/10.2514/1.c038054
[research_uybarreta_grant_2025]: https://doi.org/10.2514/6.2025-3610
[research_v_a_2022]: https://doi.org/10.1108/aeat-12-2021-0379
[research_valasek_chakravorty_2015]: https://doi.org/10.21236/ada614672
[research_valasek_walchli_1998]: https://doi.org/10.2514/6.1998-4449
[research_valasekjohn_downingdavidr_1993]: https://ntrs.nasa.gov/citations/19940014975
[research_valavanis_2017]: https://doi.org/10.1109/romoco.2017.8003896
[research_valej_2013]: https://doi.org/10.4172/2168-9792.1000119
[research_vandam_holmes_1980]: https://doi.org/10.2514/6.1980-1870
[research_vandam_holmes_1981]: https://doi.org/10.2514/3.57531
[research_vandenaarssen_visser_2019]: https://doi.org/10.2514/6.2019-1320
[research_vanderhoeven_1981]: https://doi.org/10.2514/6.1981-367
[research_vandersteen_1987]: https://doi.org/10.1109/maes.1987.5005419
[research_vandommelen_1995]: https://doi.org/10.21236/ada329654
[research_vangool_1982]: https://doi.org/10.2514/3.56164
[research_vankadari_das_2018]: https://doi.org/10.1109/icuas.2018.8453468
[research_vanorden_2001]: https://doi.org/10.21236/ada390275
[research_vanovereem_wang_2022]: https://doi.org/10.2514/6.2022-1429
[research_vanovereem_wang_2023]: https://doi.org/10.2514/6.2023-0105
[research_vanrooij_cummings_2018]: https://doi.org/10.2514/6.2018-2840
[research_vanrooyen_eshelby_1981]: https://doi.org/10.2514/3.44710
[research_vanschalkwyk_smit_2017]: https://doi.org/10.1049/cp.2017.0429
[research_vansluis_sinnige_2026]: https://doi.org/10.2514/1.c038109
[research_vantuyl_1988]: https://doi.org/10.2514/3.9883
[research_vauchel_caro_2026]: https://doi.org/10.2514/1.c038715
[research_vechtel_buch_2022]: https://doi.org/10.1007/s13272-022-00595-1
[research_veismann_gharib_2023]: https://doi.org/10.2514/1.j062561
[research_veletas_2026]: https://doi.org/10.2514/6.2026-2636
[research_vendemia_rj_1965]: https://doi.org/10.21236/ad0630342
[research_vengate_erturk_2016]: https://doi.org/10.2514/6.2016-3713
[research_venkatachari_mullane_2015]: https://doi.org/10.2514/6.2015-3010
[research_venkataraman_doman_2001]: https://doi.org/10.1109/acc.2001.945998
[research_venkataraman_seiler_2017]: https://doi.org/10.2514/1.c033832
[research_venkataraman_seiler_2019]: https://doi.org/10.2514/1.c035141
[research_venkateswararao_go_2019]: https://doi.org/10.1016/j.ast.2019.04.046
[research_vepa_2021]: https://doi.org/10.1109/iria53009.2021.9588777
[research_veresnikov_goncharenko_2025]: https://doi.org/10.1007/s42401-025-00371-z
[research_verhaagen_1999]: https://doi.org/10.2514/6.1999-3117
[research_verhaegen_1988]: https://doi.org/10.2514/3.20272
[research_verma_junkins_1999]: https://doi.org/10.2514/6.1999-4241
[research_verma_peyada_2018]: https://doi.org/10.2514/6.2018-0526
[research_vernyi_stanko_2026]: https://doi.org/10.3390/jeta4020015
[research_viavattene_mooij_2019]: https://doi.org/10.2514/6.2019-1669
[research_vicroy_huber_2018]: https://doi.org/10.2514/1.c033782
[research_viegasjohnr_howejohnt_1962]: https://ntrs.nasa.gov/citations/19620006838
[research_vieira_maughmer_2017]: https://doi.org/10.2514/1.c033960
[research_vieiradossantos_vankampen_2025]: https://doi.org/10.2514/6.2025-2795
[research_vieten_1992]: https://doi.org/10.2514/6.1992-1123
[research_vigh_1977]: https://doi.org/10.1007/bf02093139
[research_vile_alwi_2020]: https://doi.org/10.1049/cth2.12042
[research_vinje_miller_1973]: https://doi.org/10.21236/ad0769868
[research_vinkler_wood_1978]: https://doi.org/10.2514/6.1978-1274
[research_vinkler_wood_1979]: https://doi.org/10.2514/6.1979-1745
[research_vinkler_wood_1980]: https://doi.org/10.2514/3.56031
[research_viola_angel_2015]: https://doi.org/10.1109/ccac.2015.7345223
[research_virnig_bodden_1994]: https://doi.org/10.2514/6.1994-3609
[research_visbal_1993]: https://doi.org/10.2514/6.1993-434
[research_visbal_1993_b]: https://doi.org/10.2514/6.1993-2974
[research_visbal_1994]: https://doi.org/10.2514/3.12145
[research_visbal_1995]: https://doi.org/10.2514/6.1995-2309
[research_visbal_1997]: https://doi.org/10.1063/1.4739140
[research_visonneau_guilmineau_2022]: https://doi.org/10.2514/6.2022-0027
[research_visser_1999]: https://doi.org/10.1108/00022669910276884
[research_vite_mondie_2022]: https://doi.org/10.1109/icsc57768.2022.9993930
[research_vlahostergios_komnos_2018]: https://doi.org/10.1504/pcfd.2018.096620
[research_vlasceanu_popescu_2018]: https://doi.org/10.1109/ecai.2018.8679050
[research_vogel_2016]: https://doi.org/10.1109/aps.2016.7696391
[research_vogel_junqueira_2017]: https://doi.org/10.1109/imoc.2017.8121117
[research_vonhor_guess_2017]: https://doi.org/10.4050/sm_2017_hq-3457
[research_voracek_clarke_1994]: https://doi.org/10.2514/3.46505
[research_vorobieff_rockwell_1996]: https://doi.org/10.2514/3.13369
[research_vos_brown_2002]: https://doi.org/10.2514/6.2002-3428
[research_voting_software_1993]: https://doi.org/10.1016/0967-0661(93)92298-i
[research_vranics_2020]: https://doi.org/10.32560/rk.2020.1.12
[research_wagdi_1984]: https://doi.org/10.2514/6.1984-239
[research_wahler_varriale_2023]: https://doi.org/10.2514/6.2023-3485
[research_walchli_guyton_1992]: https://doi.org/10.2514/6.1992-4427
[research_waldmann_2015]: https://doi.org/10.2514/6.2015-1096
[research_waldmann_ehrle_2023]: https://doi.org/10.1007/s00348-023-03642-7
[research_walker_1960]: https://doi.org/10.1049/sqj.1960.0043
[research_walker_1961]: https://doi.org/10.1049/jiee-3.1961.0061
[research_walkerlaurencea_1997]: https://ntrs.nasa.gov/citations/19970031950
[research_walter_ivler_2019]: https://doi.org/10.4050/f-0075-2019-14753
[research_wan_ghoreyshi_2023]: https://doi.org/10.2514/6.2023-3946
[research_wandini_mulyanto_2016]: https://doi.org/10.4028/www.scientific.net/amm.842.208
[research_wang_1971]: https://doi.org/10.2514/6.1971-130
[research_wang_1972]: https://doi.org/10.2514/3.50292
[research_wang_2025]: https://doi.org/10.1117/12.3060578
[research_wang_2025_b]: https://doi.org/10.5220/0014767900004818
[research_wang_chen_2015]: https://doi.org/10.1504/ijmic.2015.072641
[research_wang_demiroz_1986]: https://doi.org/10.2514/6.1986-9772
[research_wang_fang_2025]: https://doi.org/10.3390/drones9030165
[research_wang_gao_2016]: https://doi.org/10.1007/s00348-016-2184-y
[research_wang_gong_2020]: https://doi.org/10.1109/icus50048.2020.9274980
[research_wang_guo_2017]: https://doi.org/10.1016/j.cja.2017.03.004
[research_wang_guo_2024]: https://doi.org/10.1109/meae62008.2024.11026361
[research_wang_hu_2023]: https://doi.org/10.3390/aerospace10020198
[research_wang_huang_2017]: https://doi.org/10.23919/chicc.2017.8027830
[research_wang_huang_2026]: https://doi.org/10.1177/09544100261455583
[research_wang_iliff_2004]: https://doi.org/10.2514/1.332
[research_wang_lan_1999]: https://doi.org/10.2514/6.1999-4012
[research_wang_li_2018]: https://doi.org/10.1109/gncc42960.2018.9019116
[research_wang_liu_2016]: https://doi.org/10.2514/6.2016-3528
[research_wang_liu_2018]: https://doi.org/10.1016/j.microrel.2018.03.032
[research_wang_liu_2021]: https://doi.org/10.3390/aerospace8070177
[research_wang_lu_2023]: https://doi.org/10.3390/aerospace10090799
[research_wang_luo_2025]: https://doi.org/10.1016/j.ast.2024.109773
[research_wang_luo_2025_b]: https://doi.org/10.1016/j.cja.2024.103327
[research_wang_ma_2021]: https://doi.org/10.2514/1.c035687
[research_wang_mu_2017]: https://doi.org/10.1109/ccdc.2017.7978092
[research_wang_pei_2025]: https://doi.org/10.7717/peerj-cs.3444
[research_wang_qi_2021]: https://doi.org/10.1088/1742-6596/1924/1/012005
[research_wang_qi_2021_b]: https://doi.org/10.1109/cacre52464.2021.9501289
[research_wang_shen_2023]: https://doi.org/10.2514/1.c037327
[research_wang_song_2018]: https://doi.org/10.2514/6.2018-4210
[research_wang_sutton_2004]: https://doi.org/10.1016/s1474-6670(17)31753-6
[research_wang_tai_2022]: https://doi.org/10.3390/aerospace9110689
[research_wang_tang_2020]: https://doi.org/10.1088/1742-6596/1509/1/012022
[research_wang_vankampen_2018]: https://doi.org/10.2514/6.2018-0774
[research_wang_vankampen_2018_b]: https://doi.org/10.2514/6.2018-1115
[research_wang_vankampen_2019]: https://doi.org/10.2514/1.g003980
[research_wang_wang_2016]: https://doi.org/10.1109/aus.2016.7748145
[research_wang_wang_2020]: https://doi.org/10.1109/auteee50969.2020.9315589
[research_wang_wang_2020_b]: https://doi.org/10.1016/j.ast.2019.105534
[research_wang_wang_2023]: https://doi.org/10.1016/j.cja.2023.05.023
[research_wang_wu_2020]: https://doi.org/10.1109/icca51439.2020.9264481
[research_wang_xiang_2018]: https://doi.org/10.1016/j.cja.2018.03.018
[research_wang_xu_2020]: https://doi.org/10.1360/sst-2020-0211
[research_wang_xu_2024]: https://doi.org/10.1061/jaeeez.aseng-5410
[research_wang_yang_2021]: https://doi.org/10.3390/aerospace8120360
[research_wang_yang_2025_b]: https://doi.org/10.1109/iwrfat65352.2025.11102930
[research_wang_ye_2017]: https://doi.org/10.1109/iccss.2017.8091479
[research_wang_ye_2022]: https://doi.org/10.1002/mop.33304
[research_wang_yi_2026]: https://doi.org/10.1007/s11431-025-3198-1
[research_wang_yuan_2019]: https://doi.org/10.2514/1.c035209
[research_wang_zhang_2016]: https://doi.org/10.1109/chicc.2016.7553921
[research_wang_zhang_2020]: https://doi.org/10.1016/j.ast.2020.106114
[research_wang_zhang_2021]: https://doi.org/10.23919/acc50511.2021.9483364
[research_wang_zhang_2022]: https://doi.org/10.2514/6.2022-2079
[research_wang_zhang_2025]: https://doi.org/10.1109/icus66297.2025.11295617
[research_wang_zhao_2022]: https://doi.org/10.3390/aerospace9080433
[research_wang_zhao_2023]: https://doi.org/10.3390/aerospace10040333
[research_wang_zheng_2022]: https://doi.org/10.1088/1742-6596/2187/1/012046
[research_wang_zhou_2022]: https://doi.org/10.3390/aerospace9010036
[research_wang_zhu_2020]: https://doi.org/10.1109/icuas48674.2020.9213976
[research_wang_zhu_2020_b]: https://doi.org/10.1007/s11432-018-9795-y
[research_wang_zuo_2019]: https://doi.org/10.1016/j.ast.2019.04.032
[research_wangfawei_2016]: https://doi.org/10.1109/cgncc.2016.7828898
[research_ward_1968]: https://doi.org/10.2514/3.43928
[research_ward_collins_2026]: https://doi.org/10.2514/6.2026-4688
[research_ward_ho_2025]: https://doi.org/10.2514/6.2025-3539
[research_ward_katz_1987]: https://doi.org/10.2514/6.1987-2276
[research_ward_katz_1987_b]: https://doi.org/10.2514/6.1987-1247
[research_ward_katz_1989]: https://doi.org/10.2514/3.45746
[research_ward_katz_1989_b]: https://doi.org/10.2514/6.1989-143
[research_ward_monaco_1998]: https://doi.org/10.2514/2.4329
[research_wardlaw_andrewb_1975]: https://doi.org/10.21236/ada020356
[research_warren_1989]: https://doi.org/10.2514/6.1989-3559
[research_warren_1990]: https://doi.org/10.2514/6.1990-3328
[research_warsop_crowther_2019]: https://doi.org/10.2514/6.2019-0044
[research_warsop_crowther_2019_b]: https://doi.org/10.2514/6.2019-0282
[research_wasickorj_1966]: https://ntrs.nasa.gov/citations/19660026368
[research_watson_komechak_1977]: https://doi.org/10.2514/6.1977-1078
[research_wauters_browaeys_2019]: https://doi.org/10.2514/6.2019-2987
[research_way_sescu_2026]: https://doi.org/10.2514/6.2026-0689
[research_webb_li_2016]: https://doi.org/10.1109/acc.2016.7526794
[research_webster_shang_1989]: https://doi.org/10.2514/6.1989-1802
[research_wei_1964]: https://doi.org/10.2514/6.1964-428
[research_wei_2020]: https://doi.org/10.2514/6.2020-1642
[research_wei_chen_2017]: https://doi.org/10.2514/1.c034079
[research_wei_renliang_2015]: https://doi.org/10.2514/1.c032774
[research_weibel_lawrence_2015]: https://doi.org/10.2514/1.g000888
[research_weiland_2021]: https://doi.org/10.2514/1.c035823
[research_weilj_1981]: https://ntrs.nasa.gov/citations/19810017618
[research_weinstein_hubbard_2018]: https://doi.org/10.2514/6.2018-3313
[research_weinstein_posingies_1986]: https://doi.org/10.2514/6.1986-2236
[research_weiser_looye_2024]: https://doi.org/10.2514/6.2024-2204
[research_weiser_ossmann_2020]: https://doi.org/10.1007/s13272-020-00461-y
[research_weiss_thielecke_2000]: https://doi.org/10.2514/6.2000-4098
[research_weisshaar_1977]: https://doi.org/10.2514/3.44579
[research_weissman_1972]: https://doi.org/10.2514/6.1972-984
[research_weissman_1973]: https://doi.org/10.2514/3.60216
[research_weissman_1974]: https://doi.org/10.2514/6.1974-791
[research_weissman_1975]: https://doi.org/10.2514/3.59904
[research_wells_banda_1979]: https://doi.org/10.2514/6.1979-1638
[research_wells_banda_1982]: https://doi.org/10.2514/3.57377
[research_wells_hess_2002]: https://doi.org/10.2514/6.2002-4650
[research_wells_hess_2003]: https://doi.org/10.2514/2.5084
[research_wellsscottr_2002]: https://ntrs.nasa.gov/citations/20020080707
[research_welp_chace_1975]: https://doi.org/10.21236/ada022025
[research_wen_tian_2020]: https://doi.org/10.23919/ccc50068.2020.9188619
[research_wendel_boland_1991]: https://doi.org/10.2514/6.1991-2627
[research_wendorff_alonso_2016]: https://doi.org/10.2514/6.2016-3999
[research_werbos_2001]: https://doi.org/10.1109/acc.2001.946341
[research_werner_schutte_2022]: https://doi.org/10.2514/6.2022-0295
[research_werner_schutte_2024]: https://doi.org/10.2514/1.c037421
[research_west_phillips_2020]: https://doi.org/10.2514/1.c035496
[research_west_reuter_2017]: https://doi.org/10.2514/1.c033907
[research_westbrook_1964]: https://doi.org/10.2514/6.1964-777
[research_weyl_1944]: https://doi.org/10.1108/eb031199
[research_weyl_1945]: https://doi.org/10.1108/eb031247
[research_weyl_1945_b]: https://doi.org/10.1108/eb031237
[research_weyl_1945_c]: https://doi.org/10.1108/eb031207
[research_weyl_1945_d]: https://doi.org/10.1108/eb031288
[research_weyl_1945_e]: https://doi.org/10.1108/eb031295
[research_whitaker_gowadia_1994]: https://doi.org/10.2514/3.46592
[research_whitbeck_hofmann_1978]: https://doi.org/10.21236/ada067177
[research_white_1977]: https://doi.org/10.21236/ada038392
[research_white_1977_b]: https://doi.org/10.21236/ada046782
[research_white_1995]: https://doi.org/10.2514/6.1995-1893
[research_white_narsipur_2025]: https://doi.org/10.2514/6.2025-3774
[research_whitefield_griffith_1981]: https://doi.org/10.2514/6.1981-2474
[research_whitemauriced_innisrobertc_1959]: https://ntrs.nasa.gov/citations/19980232080
[research_whitingmatthewrobert_1996]: https://ntrs.nasa.gov/citations/19960012279
[research_whoric_1974]: https://doi.org/10.21236/ad0787657
[research_wickens_dixon_2002]: https://doi.org/10.21236/ada496813
[research_wickman_1953]: https://doi.org/10.21236/ada953108
[research_widiyanti_asmoro_2024]: https://doi.org/10.1007/s10055-023-00914-9
[research_wilcox_1913]: https://doi.org/10.1038/scientificamerican04051913-212supp
[research_wilhelm_schafranek_1986]: https://doi.org/10.2514/3.45377
[research_willebeeklemair_rhinehart_2023]: https://doi.org/10.4050/sm_2023_hq-1196
[research_williams_1926]: https://doi.org/10.1098/rspa.1926.0150
[research_williams_2004]: https://doi.org/10.2514/6.2004-6283
[research_williams_niestroy_2025]: https://doi.org/10.2514/6.2025-1451
[research_williamson_1951]: https://doi.org/10.1038/167316a0
[research_wills_wise_1976]: https://doi.org/10.2514/6.1976-618
[research_wilson_riccardi_2022]: https://doi.org/10.1016/j.actaastro.2022.07.013
[research_wilson_riley_1993]: https://doi.org/10.21236/ada273685
[research_winchenbach_chelekis_1982]: https://doi.org/10.2514/6.1982-1365
[research_winchenbach_uselton_1984]: https://doi.org/10.2514/3.48215
[research_wingroverc_1978]: https://ntrs.nasa.gov/citations/19790066419
[research_winslow_hrishikeshavan_2018]: https://doi.org/10.2514/1.c034483
[research_wisbacher_ossmann_2025]: https://doi.org/10.2514/6.2025-0857
[research_wise_1992]: https://doi.org/10.23919/acc.1992.4792318
[research_wise_brinker_1999]: https://doi.org/10.1002/(sici)1099-1239(19991215)9:14<999::aid-rnc449>3.3.co;2-f
[research_wise_sedwick_1998]: https://doi.org/10.2514/6.1998-4111
[research_wise_sedwick_1999]: https://doi.org/10.21236/ada386935
[research_withrowmaser_malpica_2021]: https://doi.org/10.4050/f-0077-2021-16791
[research_witkowski_williams_2022]: https://doi.org/10.2514/6.2022-2737
[research_witte_monson_2003]: https://doi.org/10.21236/ada421043
[research_wittenberg_2001]: https://doi.org/10.1016/s1369-8869(00)00026-4
[research_wolf_1978]: https://ntrs.nasa.gov/citations/19790003893
[research_wolf_shelley_2016]: https://doi.org/10.2514/6.2016-0406
[research_wolfe_oberkampf_1982]: https://doi.org/10.2514/6.1982-1359
[research_wolowiczch_brownjsjr_1979]: https://ntrs.nasa.gov/citations/19790022005
[research_wood_2003]: https://doi.org/10.2514/6.2003-209
[research_wood_araujoestrada_2019]: https://doi.org/10.2514/1.c035416
[research_wood_murphy_1955]: https://doi.org/10.21236/ad0066178
[research_woodbury_valasek_2015]: https://doi.org/10.2514/6.2015-1481
[research_woodrichardm_bauerstevenxs_1999]: https://ntrs.nasa.gov/citations/20000012648
[research_woodruffstephenl_2009]: https://ntrs.nasa.gov/citations/20090032249
[research_woods_sillence_1996]: https://doi.org/10.2514/6.1996-3346
[research_woolcock_schmid_2026]: https://doi.org/10.1109/tac.2026.3664332
[research_woolley_1978]: https://doi.org/10.2514/6.1978-1273
[research_wornomde_1960]: https://ntrs.nasa.gov/citations/19660012274
[research_wortman_duket_1975]: https://doi.org/10.1177/154193127501900313
[research_wright_1975]: https://doi.org/10.21236/ada022015
[research_wrist_hubner_2017]: https://doi.org/10.1177/1756829317705327
[research_wu_1981]: https://doi.org/10.2514/3.50966
[research_wu_2025]: https://doi.org/10.3390/aerospace12010065
[research_wu_chen_2016]: https://doi.org/10.2514/6.2016-3377
[research_wu_chen_2018]: https://doi.org/10.1016/j.neucom.2018.04.038
[research_wu_li_2015]: https://doi.org/10.2991/icmmita-15.2015.111
[research_wu_lian_2026]: https://doi.org/10.1016/j.jfranklin.2026.108638
[research_wu_lv_2018]: https://doi.org/10.1016/j.ast.2018.07.037
[research_wu_perng_2004]: https://doi.org/10.2514/1.9285
[research_wu_sankar_1980]: https://doi.org/10.2514/6.1980-11
[research_wu_xiao_2017]: https://doi.org/10.2514/1.c034356
[research_wu_yang_2017]: https://doi.org/10.1109/icinfa.2017.8078898
[research_wu_zhu_2024]: https://doi.org/10.1155/2024/2054883
[research_x_29_research_1991]: https://ntrs.nasa.gov/citations/19940014489
[research_xi_dai_2025]: https://doi.org/10.1063/5.0255492
[research_xi_zhao_2017]: https://doi.org/10.1109/ascc.2017.8287228
[research_xia_zhang_2019]: https://doi.org/10.1002/acs.3010
[research_xiao_belt_2018]: https://doi.org/10.4050/f-0074-2018-12791
[research_xiao_fan_2025]: https://doi.org/10.1016/j.ifacol.2025.11.222
[research_xiao_li_2016]: https://doi.org/10.1177/1756829316638204
[research_xiao_zhang_2018]: https://doi.org/10.1088/1757-899x/439/3/032103
[research_xiaofengai_fengzhao_2016]: https://doi.org/10.1109/piers.2016.7734870
[research_xie_cabecinhas_2022]: https://doi.org/10.1109/tie.2021.3055181
[research_xie_low_2017]: https://doi.org/10.2514/6.2017-1745
[research_xie_yang_2011]: https://doi.org/10.4028/www.scientific.net/amr.213.334
[research_xin_chen_2024]: https://doi.org/10.1155/2024/6336361
[research_xing_zhang_2017]: https://doi.org/10.1109/icfst.2017.8210552
[research_xinghua_2018]: https://doi.org/10.1109/iicspi.2018.8690525
[research_xiong_nguyen_2023]: https://doi.org/10.2514/6.2023-4528
[research_xiong_nguyen_2026]: https://doi.org/10.2514/6.2026-1111
[research_xiumingliu_yingwang_2016]: https://doi.org/10.1109/iecon.2016.7793023
[research_xu_2025]: https://doi.org/10.61173/1xj9nn24
[research_xu_feng_2025]: https://doi.org/10.1016/j.cja.2025.103443
[research_xu_ge_2020]: https://doi.org/10.1016/j.ast.2019.105653
[research_xu_jiang_2016]: https://doi.org/10.1007/s10409-016-0565-3
[research_xu_jiang_2017]: https://doi.org/10.1504/ijmic.2017.086559
[research_xu_petrunin_2019]: https://doi.org/10.1109/reduas47371.2019.8999707
[research_xu_tan_2019]: https://doi.org/10.1016/j.cja.2019.06.003
[research_xu_tian_2024]: https://doi.org/10.1061/jaeeez.aseng-5007
[research_xu_yu_2025]: https://doi.org/10.3390/aerospace13010017
[research_xu_zhang_2024]: https://doi.org/10.1109/cac63892.2024.10865127
[research_xu_zhang_2025]: https://doi.org/10.3390/act14050222
[research_xu_zhou_2015]: https://doi.org/10.1016/j.ast.2015.07.022
[research_xue_yunsong_2021]: https://doi.org/10.1177/0036850421998137
[research_yajnik_1977]: https://doi.org/10.2514/3.44605
[research_yamaguchi_ohara_2001]: https://doi.org/10.2514/6.2001-4104
[research_yamaguchi_ohno_2000]: https://doi.org/10.2322/jjsass.48.322
[research_yamaoka_1963]: https://doi.org/10.21236/ad0431277
[research_yamazaki_yamagishi_2017]: https://doi.org/10.2514/6.2017-3404
[research_yamazaki_yamagishi_2018]: https://doi.org/10.2514/1.c034654
[research_yan_li_2019]: https://doi.org/10.1051/jnwpu/20193740656
[research_yan_shi_2024]: https://doi.org/10.1109/isaes61964.2024.10751145
[research_yan_shi_2025]: https://doi.org/10.56028/aetr.14.1.1702.2025
[research_yan_sun_2025]: https://doi.org/10.1080/23307706.2025.2546106
[research_yanagihara_suzuki_1991]: https://doi.org/10.4271/911979
[research_yang_2024]: https://doi.org/10.1002/adc2.194
[research_yang_2024_b]: https://doi.org/10.54097/3fb71s08
[research_yang_agarwal_2019]: https://doi.org/10.2514/6.2019-2923
[research_yang_chen_2015]: https://doi.org/10.2514/6.2015-0549
[research_yang_kabamba_1991]: https://doi.org/10.23919/acc.1991.4791585
[research_yang_liu_2019]: https://doi.org/10.1016/j.conengprac.2019.07.015
[research_yang_meng_2016]: https://doi.org/10.2514/6.2016-4342
[research_yang_tan_2023]: https://doi.org/10.23919/acc55779.2023.10155880
[research_yang_wang_2026]: https://doi.org/10.1016/j.cja.2026.104412
[research_yang_xiong_2023]: https://doi.org/10.1117/12.2671734
[research_yang_xu_2026]: https://doi.org/10.1109/fasta70174.2026.11548915
[research_yang_yee_2022]: https://doi.org/10.2514/1.c036489
[research_yang_zhen_2025]: https://doi.org/10.1016/j.ifacol.2025.11.325
[research_yaniv_1992]: https://doi.org/10.1016/0005-1098(92)90156-a
[research_yao_wu_2019]: https://doi.org/10.1109/access.2019.2905628
[research_yarlett_adrezin_2000]: https://doi.org/10.2514/6.2000-1694
[research_yasue_2020]: https://doi.org/10.2514/1.c035564
[research_yavuzturk_topbas_2017]: https://doi.org/10.2514/6.2017-1865
[research_yavuzturk_topbas_2020]: https://doi.org/10.2514/6.2020-1645
[research_yazdi_gray_2026]: https://doi.org/10.2514/6.2026-1490
[research_yazdi_reist_2026]: https://doi.org/10.2514/1.c038519
[research_yeagerjessiec_1997]: https://ntrs.nasa.gov/citations/19970014822
[research_yechout_1988]: https://doi.org/10.2514/3.45626
[research_yechout_schweikhard_1984]: https://doi.org/10.2514/6.1984-563
[research_yedavalli_2024]: https://doi.org/10.1109/aero58975.2024.10521282
[research_yegin_ozbay_2023]: https://doi.org/10.1016/j.sysconle.2022.105453
[research_yeo_atkins_2015]: https://doi.org/10.2514/1.c032682
[research_yi_heimbold_1979]: https://doi.org/10.1115/1.3446439
[research_yifei_zongxia_2015]: https://doi.org/10.1109/fpm.2015.7337174
[research_yijie_deshuang_2023]: https://doi.org/10.1109/icipnp62754.2023.00023
[research_yilmaz_german_2024]: https://doi.org/10.1016/j.ast.2024.109595
[research_yiming_mei_2019]: https://doi.org/10.1109/iccais46528.2019.9074698
[research_yin_chu_2019]: https://doi.org/10.2514/6.2019-0951
[research_yin_wang_2017]: https://doi.org/10.12783/dtetr/amsm2017/14821
[research_yin_wang_2019]: https://doi.org/10.1109/icmae.2019.8881023
[research_yip_fratello_1990]: https://doi.org/10.2514/6.1990-1261
[research_yip_fratello_1990_b]: https://ntrs.nasa.gov/citations/19900014922
[research_yip_fratello_1991]: https://doi.org/10.2514/3.46089
[research_yondo_andres_2018]: https://doi.org/10.1016/j.paerosci.2017.11.003
[research_yong_wu_2020]: https://doi.org/10.1109/icca51439.2020.9264484
[research_yongming_yuanqing_2015]: https://doi.org/10.1109/chicc.2015.7260696
[research_yonke_terrell_1985]: https://doi.org/10.2514/6.1985-1425
[research_yoo_2018]: https://doi.org/10.2514/6.2018-3009
[research_yoo_duensing_2019]: https://doi.org/10.2514/6.2019-3698
[research_yoo_jang_2021]: https://doi.org/10.1109/lcsys.2020.3001663
[research_york_anderson_1994]: https://doi.org/10.2514/6.1994-3684
[research_you_bromby_2013]: https://doi.org/10.21236/ada608653
[research_youceftoumi_bobbett_1991]: https://doi.org/10.23919/acc.1991.4791873
[research_youceftoumi_wu_1992]: https://doi.org/10.23919/acc.1992.4792631
[research_younes_noura_2019]: https://doi.org/10.1109/icuas.2019.8798232
[research_yu_2021]: https://doi.org/10.33552/gjes.2021.08.000682
[research_yu_bi_2024]: https://doi.org/10.1002/acs.3814
[research_yu_fu_2017]: https://doi.org/10.1109/tfuzz.2017.2760860
[research_yu_hrynuk_2024]: https://doi.org/10.1016/j.ast.2024.109145
[research_yu_kim_2024]: https://doi.org/10.23919/iccas63016.2024.10773016
[research_yu_li_2022]: https://doi.org/10.1007/s11071-022-07904-7
[research_yu_li_2023]: https://doi.org/10.1002/rnc.6570
[research_yu_li_2023_b]: https://doi.org/10.1016/j.ast.2023.108472
[research_yu_li_2023_c]: https://doi.org/10.1007/s11071-023-08849-1
[research_yu_wang_2017]: https://doi.org/10.1109/icmic.2017.8321524
[research_yu_wang_2024]: https://doi.org/10.1109/access.2024.3425462
[research_yu_xiaoxiong_2019]: https://doi.org/10.1109/cac48633.2019.8997433
[research_yu_zhang_2017]: https://doi.org/10.1109/icuas.2017.7991334
[research_yu_zhang_2019]: https://doi.org/10.1109/icuas.2019.8798328
[research_yu_zhang_2023]: https://doi.org/10.3390/s23020574
[research_yuan_2026]: https://doi.org/10.54254/2755-2721/2026.mh32172
[research_yuan_anderson_2021]: https://doi.org/10.4050/f-0077-2021-16815
[research_yuan_thomson_2020]: https://doi.org/10.2514/1.c035811
[research_yuan_zhou_2024]: https://doi.org/10.3390/aerospace11040281
[research_yue_wang_2009]: https://doi.org/10.2514/6.2009-6155
[research_yue_wang_2013]: https://doi.org/10.2514/6.2013-623
[research_yue_wang_2017]: https://doi.org/10.2514/6.2017-3396
[research_yue_won_2003]: https://doi.org/10.1049/ip-cta:20030080
[research_yuezhao_letianlin_2016]: https://doi.org/10.1109/acc.2016.7525286
[research_yuksek_inalhan_2020]: https://doi.org/10.1002/acs.3181
[research_yuksek_inalhan_2022]: https://doi.org/10.2514/6.2022-0879
[research_yumatestcenteryumaprovinggroundaz_2008]: https://doi.org/10.21236/ada503063
[research_yunerovna_valerievich_2015]: https://doi.org/10.1109/sibcon.2015.7147051
[research_yuzawa_ogami_2002]: https://doi.org/10.1299/jsmemecjo.2002.3.0_333
[research_zagranski_lamart_1974]: https://doi.org/10.21236/ad0785580
[research_zahedi_haeri_2017]: https://doi.org/10.1109/icciautom.2017.8258647
[research_zanette_almeida_2015]: https://doi.org/10.2514/6.2015-3227
[research_zannetti_onofri_1984]: https://doi.org/10.2514/6.1984-284
[research_zanoni_gerosa_2022]: https://doi.org/10.1007/s42496-022-00107-8
[research_zastawny_2016]: https://doi.org/10.1017/aer.2016.13
[research_zaytseva_kuznetsov_2021]: https://doi.org/10.18698/0536-1044-2021-12-3-10
[research_zeitler_schwierz_2018]: https://doi.org/10.1109/dasc.2018.8569693
[research_zellerj_lehtinenb_1982]: https://ntrs.nasa.gov/citations/19820042991
[research_zennir_larabi_2017]: https://doi.org/10.5220/0006426105980605
[research_zennir_larabi_2017_b]: https://doi.org/10.5220/0006399805430550
[research_zeyada_hess_1998]: https://doi.org/10.2514/6.1998-4334
[research_zeyada_hess_1999]: https://doi.org/10.2514/2.4463
[research_zha_li_2025]: https://doi.org/10.1002/acs.4052
[research_zhai_li_2025]: https://doi.org/10.3724/j.gter.20250056
[research_zhang_2023]: https://doi.org/10.1038/s41598-023-46753-1
[research_zhang_2026]: https://doi.org/10.1109/icaace69793.2026.11508762
[research_zhang_bradley_2022]: https://doi.org/10.3390/s22041525
[research_zhang_chen_2018]: https://doi.org/10.2514/1.c034232
[research_zhang_chen_2023]: https://doi.org/10.1109/raiic59453.2023.10280846
[research_zhang_devisser_2017]: https://doi.org/10.2514/6.2017-1863
[research_zhang_du_2021]: https://doi.org/10.1109/ccdc52312.2021.9602605
[research_zhang_duan_2017]: https://doi.org/10.1108/aeat-05-2016-0065
[research_zhang_han_2020]: https://doi.org/10.3390/act9030070
[research_zhang_he_2026]: https://doi.org/10.1016/j.cja.2025.103811
[research_zhang_he_2026_b]: https://doi.org/10.1016/j.cja.2025.103582
[research_zhang_huang_2023]: https://doi.org/10.1016/j.cja.2023.03.017
[research_zhang_jiang_2023]: https://doi.org/10.1016/j.isatra.2022.07.032
[research_zhang_liu_2017]: https://doi.org/10.2514/1.c033511
[research_zhang_liu_2024]: https://doi.org/10.1108/aeat-05-2024-0128
[research_zhang_meng_2019]: https://doi.org/10.1016/j.isatra.2019.02.037
[research_zhang_pang_2016]: https://doi.org/10.1109/chicc.2016.7554548
[research_zhang_ran_2023]: https://doi.org/10.3390/app132111844
[research_zhang_saeki_1992]: https://doi.org/10.1109/9.256349
[research_zhang_samtaney_2016]: https://doi.org/10.1063/1.4945005
[research_zhang_shuang_2018]: https://doi.org/10.1007/s12555-017-0454-y
[research_zhang_su_2021]: https://doi.org/10.1109/ccdc52312.2021.9601405
[research_zhang_sun_2025]: https://doi.org/10.1109/ccdc65474.2025.11090360
[research_zhang_tomizuka_2015]: https://doi.org/10.1109/acc.2015.7172166
[research_zhang_wang_2017]: https://doi.org/10.1504/ijmic.2017.083785
[research_zhang_wang_2017_b]: https://doi.org/10.2991/mme-16.2017.1
[research_zhang_wang_2019]: https://doi.org/10.2514/6.2019-1922
[research_zhang_wang_2026_b]: https://doi.org/10.1016/j.cja.2026.104377
[research_zhang_xu_2024]: https://doi.org/10.1115/gt2024-127703
[research_zhang_yang_2026]: https://doi.org/10.1016/j.applthermaleng.2025.129428
[research_zhang_zhang_2017]: https://doi.org/10.4208/cicp.oa-2016-0132
[research_zhang_zhang_2023]: https://doi.org/10.3390/aerospace10060521
[research_zhang_zhou_2019]: https://doi.org/10.1109/access.2018.2889858
[research_zhang_zhou_2024]: https://doi.org/10.1007/s11424-024-3364-0
[research_zhao_duan_2021]: https://doi.org/10.1109/icuas51884.2021.9476886
[research_zhao_li_2022]: https://doi.org/10.1080/19942060.2021.1997824
[research_zhao_luo_2023]: https://doi.org/10.1016/j.cja.2023.06.023
[research_zhao_wang_2024]: https://doi.org/10.2514/1.j064345
[research_zhao_xu_2024]: https://doi.org/10.3390/drones8090429
[research_zhao_zhang_2024]: https://doi.org/10.1109/wcnc57260.2024.10570967
[research_zhao_zhu_2016]: https://doi.org/10.1109/icuas.2016.7502671
[research_zhen_hao_2020]: https://doi.org/10.1109/ddcls49620.2020.9275205
[research_zheng_horn_2015]: https://doi.org/10.4050/f-0071-2015-10176
[research_zheng_li_2019]: https://doi.org/10.1109/ccdc.2019.8833258
[research_zhishuai_lingling_2022]: https://doi.org/10.1109/ccdc55256.2022.10034339
[research_zhong_huang_2023]: https://doi.org/10.1007/s11768-023-00128-z
[research_zhong_pu_2023]: https://doi.org/10.1145/3598151.3598155
[research_zhou_2023]: https://doi.org/10.4273/ijvss.15.2.22
[research_zhou_canova_2015]: https://doi.org/10.1109/acc.2015.7172048
[research_zhou_canova_2016]: https://doi.org/10.1016/j.automatica.2016.01.045
[research_zhou_deng_2024]: https://doi.org/10.1142/s2301385025500487
[research_zhou_diskin_2019]: https://doi.org/10.2514/6.2019-3524
[research_zhou_ho_2021]: https://doi.org/10.1016/j.ast.2021.106889
[research_zhou_huang_2021]: https://doi.org/10.1038/s41598-021-87756-0
[research_zhou_huang_2021_b]: https://doi.org/10.3390/photonics8060175
[research_zhou_huang_2021_c]: https://doi.org/10.3390/s21248459
[research_zhou_huang_2022_b]: https://doi.org/10.1108/aeat-10-2021-0317
[research_zhou_huang_2022_c]: https://doi.org/10.1038/s41598-022-08385-9
[research_zhou_huang_2023]: https://doi.org/10.1108/aeat-12-2022-0340
[research_zhou_huang_2023_b]: https://doi.org/10.1108/ec-11-2022-0694
[research_zhou_liu_2019]: https://doi.org/10.1051/jnwpu/20193750935
[research_zhou_liu_2023]: https://doi.org/10.1108/aeat-05-2023-0145
[research_zhou_ma_2025]: https://doi.org/10.1109/ieeeconf65522.2025.11137169
[research_zhou_wang_2022]: https://doi.org/10.3390/sym14091837
[research_zhou_wang_2026]: https://doi.org/10.2514/1.c038092
[research_zhou_yang_2022]: https://doi.org/10.1002/rnc.6503
[research_zhou_zhong_2021]: https://doi.org/10.1063/5.0039416
[research_zhu_2024]: https://doi.org/10.54097/a49jqw20
[research_zhu_duan_2015]: https://doi.org/10.1108/aeat-06-2013-0112
[research_zhu_gao_2016]: https://doi.org/10.1142/9789814740616_0016
[research_zhu_guo_2019]: https://doi.org/10.1109/ccdc.2019.8832768
[research_zhu_liu_2019]: https://doi.org/10.1109/icus48101.2019.8996021
[research_zhu_qin_2023]: https://doi.org/10.3390/drones7060350
[research_zhu_shi_2022]: https://doi.org/10.1063/5.0076173
[research_zhu_zhang_2018]: https://doi.org/10.1109/icisce.2018.00180
[research_ziemianskija_1981]: https://ntrs.nasa.gov/citations/19810015551
[research_zilli_sutton_2017]: https://doi.org/10.2514/6.2017-0302
[research_zilliac_degani_1990]: https://doi.org/10.2514/6.1990-388
[research_zilstra_johnson_2026]: https://doi.org/10.1115/1.4070836
[research_zimbelman_rouser_2025]: https://doi.org/10.1115/gt2025-153304
[research_zimmnau_cremer_2025]: https://doi.org/10.2514/6.2025-0003
[research_zimper_hummel_2018]: https://doi.org/10.2514/1.c033697
[research_zipperer_jenney_1975]: https://doi.org/10.21236/ada012233
[research_zohar_erel_1988]: https://doi.org/10.2514/3.45578
[research_zolanvari_teixeira_2018]: https://doi.org/10.1109/icuas.2018.8453394
[research_zolotas_2023]: https://doi.org/10.3390/machines11040498
[research_zou_xie_2026]: https://doi.org/10.2514/6.2026-4710
[research_zou_yin_2017]: https://doi.org/10.1109/ccsse.2017.8087893
[research_zou_zhen_2026]: https://doi.org/10.2139/ssrn.6802811
[research_zugaj_2017]: https://doi.org/10.2478/tar-2017-0017
[research_zuhri_2025]: https://doi.org/10.55981/ijoa.2025.9106
[research_zwerger_hickel_2015]: https://doi.org/10.2514/6.2015-2572
[research_zwerneman_eller_1994]: https://doi.org/10.2514/6.1994-3513
