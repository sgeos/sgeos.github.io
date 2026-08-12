---
layout: post
mathjax: true
comments: true
title: "X-Planes: Grumman X-29"
date: 2025-11-04 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 30
---
<!-- A326 -->
<script>console.log("A326");</script>

The [Grumman X-29][ref_x29] was built from nothing to answer a question that could not be answered any other
way, and **after four articles about aircraft that already existed, that sentence is worth pausing on**. The
[X-25][related_post_a322_bensen_x25] was a catalogue autogyro. The [X-26][related_post_a323_schweizer_x26]
was a catalogue sailplane, bought twice. The [X-27][related_post_a324_lockheed_x27] was a private-venture
fighter that was never built at all. The [X-28][related_post_a325_osprey_x28] was a homebuilt flying boat
bought off a private individual for five thousand dollars.
**The X-29 is the first purpose-built research aeroplane in this series since the [X-24][related_post_a321_martin_marietta_x24]**,
and it was built to settle something specific. This is the thirtieth article in the
[X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1], the
[X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the
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
[X-26][related_post_a323_schweizer_x26], the [X-27][related_post_a324_lockheed_x27], and the
[X-28][related_post_a325_osprey_x28].

**The easy misreading of this aircraft is that it existed to find out whether a forward-swept wing would work.**
It did not. Forward-sweep [divergence][ref_divergence] was understood before the Second World War, it is in
every aeroelasticity textbook, and no research aeroplane was needed to establish it. A forward-swept wing
bends upward under load, the bending increases the local angle of attack, the increased angle increases the
lift, and the loop closes on itself at a computable dynamic pressure. That much was arithmetic by 1940.

**What was new was the claim that the divergence could be held rather than avoided**, by two means working
at once. The first is [aeroelastic tailoring][ref_tailoring], which uses the bend-twist coupling of an
unbalanced [composite laminate][ref_laminate] to cancel the aerodynamic coupling inside the structure. The
second is active control of an airframe deliberately made unstable, held by a triplex digital
[fly-by-wire][ref_fbw] system running at forty hertz.

* Contents
{:toc}

## The Research Question

**The keystone is the structure and the control law together, and separating them misses the aircraft entirely.**

The X-29A was **statically unstable by a nominal thirty-five percent of the mean aerodynamic chord**, which
is to say its [static margin][ref_static_margin] was that far negative, in subsonic flight, and the primary
record is unusually direct about why. The instability was not a side effect of the forward sweep. It was
created by the canard. National Aeronautics and Space Administration Technical Memorandum 101715 states that
**the presence of the canards results in an otherwise neutrally stable airframe having a negative static margin of nominally thirty-five percent**,
which makes the instability a deliberate purchase rather than a penalty.

So the aircraft posed two coupled questions that had to be answered by the same airframe at the same time.

- **Can a wing be made to resist its own divergence by the arrangement of its fibres**, rather than by
  being made thicker, heavier or less swept.
- **Can an airframe that doubles its own pitch disturbance in a fraction of a second be flown**, by a
  sampled digital controller with a finite update rate and a finite failure probability.

**Neither question can be settled on the ground.** A wind tunnel model can be tailored and tested, and
several were, but a tunnel model does not carry a flight control system, a hydraulic actuator, a
failure-tolerant voter or a pilot. An iron-bird simulator carries all of those and does not carry an elastic
wing in a real airflow.
**The X-29 exists because those two halves had to be connected, and connecting them required an aeroplane.**

### Why the Keystone Is Not the Planform

The obvious alternative keystone is the forward sweep itself, treated as an aerodynamic choice, and that
framing is available because the programme did claim aerodynamic benefits. The primary record states a
prediction of **up to thirteen percent lower aircraft drag for wings of the same aspect ratio**, arising
from reduced transonic wing profile drag.

**That claim is examined below and it survives, but it is not what needed an aeroplane.** Transonic drag is
measurable in a tunnel. What is not measurable in a tunnel is whether a wing designed to sit inside a
divergence boundary actually sits inside it once built, instrumented and flown, and whether the boundary can
be located from flight data before it is reached.
**The X-29 answered that, and the answer arrived by a method that had never previously been used in flight.**

## Programme Origin

**The programme began with a government agency rather than a manufacturer**, which distinguishes it sharply
from the four articles before it.

### The Agency

The [Defense Advanced Research Projects Agency][ref_darpa] began the X-29A project **in 1977**. The aircraft
was designed and built by the [Grumman Aerospace Corporation][ref_grumman] and delivered to the
[Dryden Flight Research Facility][ref_dryden] of the National Aeronautics and Space Administration at
Edwards, California, where the flight programme was conducted jointly.

**Two aircraft were built.** They carried a shared research agenda that was divided between them, the first
taking the envelope expansion and performance work and the second taking the high angle of attack
investigation.

### Why Forward Sweep Became Buildable in the 1970s

The idea was old. The [Junkers Ju 287][ref_ju287] flew a forward-swept wing in 1944, and the
[Hansa Jet][ref_hansajet] carried one into production in the 1960s.
**What changed was not the aerodynamic idea but the material.**

A metal wing resists divergence only through its own torsional stiffness, and buying enough of that at a
useful sweep angle costs weight that consumes the configuration's advantages.
**A composite laminate can be made to twist in a chosen direction when it bends**, because the fibres need
not run along the principal axes of the structure. That converts divergence resistance from a mass problem
into a geometry problem, and the primary record reports the outcome directly, describing the tailored skins
as achieving their result
**with an insignificant weight penalty over that required for the basic strength design**.

**That sentence is the whole justification for the programme**, and the article's structural half is an
examination of whether the physics supports it.

### Where the Aircraft Came From

The airframe was assembled from existing parts wherever the research did not require otherwise. The primary
record lists the **forward fuselage and nose gear of an [F-5A][ref_f5]**, the
**main landing gear and servo-actuators of an [F-16][ref_f16]**, and **[F-14][ref_f14] avionics**.

**Only the parts carrying the research question were new.** The wing, the canard, the strake flaps and the
flight control system were designed for this aircraft. Everything else was bought from the company's own
back catalogue and from its competitors, which is why two research aeroplanes were affordable at all.

## The Vehicle

| Quantity | Value |
|---|---|
| Wing reference area | 188.84 ft² |
| Aspect ratio | 4.0 |
| Leading edge sweep | 29.3° forward |
| Structural axis sweep | 36.2° forward |
| Mean aerodynamic chord | 86.6 in |
| Thickness to chord ratio | 5 to 7 percent |
| Aerofoil | Grumman K Mod 2 [supercritical][ref_supercritical] |
| Design section lift coefficient | 0.92 at Mach 0.90 |
| Canard area | 20 percent of wing reference area |
| Canard mean aerodynamic chord | 0.76 of the wing's |
| Canard deflection | 30° leading edge up to 60° leading edge down |
| Canard rate | 100 deg/s |
| Flaperon deflection | 10° up to 24.75° down |
| Flaperon rate | 68 deg/s |
| Strake flap deflection | 30° up to 30° down |
| Static margin | 35 percent negative, subsonic |
| Flight control system | triplex digital, 40 Hz update |
| Engine | [General Electric F404-GE-400][ref_f404], 16,000 lb class |
| Maximum takeoff gross weight | 17,800 lb |
| Fuel capacity | 4,000 lb |
| Maneuver design gross weight | 15,000 lb |
| Design load factor | 8 g subsonic, 6.5 g supersonic |
| Design dynamic pressure | 1,700 lb/ft² at Mach 1.07, sea level |

### What the Table Implies

Before either of those, the table supports a handful of ratios that it does not state, and they place the
aircraft among its contemporaries. The sizing conventions used here follow [Raymer][book_raymer], with the
airframe practice in [Niu][book_niu].

The wing loading is the gross weight carried per unit of reference area.

$$ \frac{W}{S} = \frac{17{,}800\ \mathrm{lb}}{188.84\ \mathrm{ft}^2} = 94.26\ \mathrm{lb/ft^2} $$

At the manoeuvre design gross weight the same relation gives 79.43 pounds per square foot, and both figures
are ordinary for a fighter-sized aircraft of the period.

The thrust-to-weight ratio uses the engine's class rating rather than an installed figure, which is the only
thrust the record gives.

$$ \frac{T}{W} = \frac{16{,}000\ \mathrm{lb}}{17{,}800\ \mathrm{lb}} = 0.899 $$

$$ \left.\frac{T}{W}\right|_{\mathrm{manoeuvre}} = \frac{16{,}000\ \mathrm{lb}}{15{,}000\ \mathrm{lb}} = 1.067 $$

**At the manoeuvre design weight the aircraft has more thrust than weight**, which matters below because it
makes the airframe rather than the engine the binding limit in a sustained turn.

The canard is quoted only as a percentage, so its area and chord follow.

$$ S_c = 0.20\,S = 0.20 \times 188.84\ \mathrm{ft}^2 = 37.77\ \mathrm{ft}^2 $$

$$ \bar{c}_c = 0.76\,\bar{c} = 0.76 \times 7.217\ \mathrm{ft} = 5.485\ \mathrm{ft} $$

The design load and the fuel fraction complete the picture.

$$ n W = 8.0 \times 15{,}000\ \mathrm{lb} = 120{,}000\ \mathrm{lb} $$

**The wing carries 120,000 pounds at the subsonic design limit**, which is the load the structural box and
its tailored skins had to survive while also satisfying the divergence requirement.

$$ \frac{W_{\mathrm{fuel}}}{W_{\max}} = \frac{4{,}000\ \mathrm{lb}}{17{,}800\ \mathrm{lb}} = 0.225 $$

**The heaviest weight actually flown exceeded the manoeuvre design weight by eighteen percent**, which the
record states and which the ratio confirms.

$$ \frac{17{,}700}{15{,}000} - 1 = 0.180 $$

**Two entries in that table are the aeroplane and everything else follows from them.**

The first is the **structural axis sweep of 36.2 degrees forward**, which is seven degrees more forward than
the leading edge. That difference is not incidental. It means the structure is swept further forward than
the planform suggests, and since divergence is governed by the elastic axis rather than by the leading edge,
**the wing is aeroelastically more forward-swept than it looks.**

Beside it stands the **static margin of minus thirty-five percent**, which is not a small number. A
conventional fighter of the period sat within a few percent of neutral.
**This aircraft was built an order of magnitude further into instability than the aircraft it was meant to inform.**

### A Consistency Check on the Published Geometry

The record gives the aspect ratio as 4.0 and the reference area as 188.84 square feet, and separately gives
the span as 27 feet 2.5 inches. Those are three statements about two quantities, so one of them can be
checked.

$$ b = \sqrt{A S} = \sqrt{4.0 \times 188.84\ \mathrm{ft}^2} = 27.48\ \mathrm{ft} $$

Against a quoted span of 27.21 feet that is an agreement to **0.99 percent**, which is what one expects when
an aspect ratio has been rounded to two significant figures.
**The published geometry is mutually consistent**, and that is worth establishing before anything is built
on top of it.

## Sizing From First Principles

The inventory of record for the whole series, and the source for this aircraft's place in it, is
[Jenkins, Landis and Miller][ref_xvehicles].

The aeroelastic relations used throughout follow [Bisplinghoff, Ashley and Halfman][book_bisplinghoff] and
[Fung][book_fung], with the modern treatments in [Hodges and Pierce][book_hodges] and
[Wright and Cooper][book_wright_cooper]. The flight mechanics follow [Etkin][book_etkin] and the control
formulation [Stevens and Lewis][book_stevens_lewis]. The laminate mechanics behind aeroelastic tailoring are
in [Jones][book_jones_composite] and [Tsai and Hahn][book_tsai_hahn], the airframe structures in
[Megson][book_megson] and [Niu][book_niu], and the sizing and drag data in [Raymer][book_raymer],
[Anderson][book_anderson] and [Hoerner][book_hoerner].

**The X-29's divergence boundary was never published as a number.** What was published is something better,
because it can be inverted.

### The Relation That Makes the Whole Article Possible

A wing that washes in under load amplifies its own lift. At any dynamic pressure below the divergence
boundary the elastic wing produces more lift per degree of angle of attack than the same wing would produce
if it were rigid, and the ratio between the two grows without limit as the boundary is approached.
**That growth without limit is the definition of divergence rather than a consequence of it.**

For the single-degree-of-freedom case the relation is exact.

$$ \frac{C_{L_\alpha}^{\mathrm{elastic}}}{C_{L_\alpha}^{\mathrm{rigid}}} = \frac{1}{1 - q/q_D} $$

Here $q$ is the free-stream dynamic pressure and $q_D$ is the divergence dynamic pressure, the value at
which the amplification becomes unbounded.

### Where the Amplification Comes From

The relation is not asserted. It follows from the feedback the wing closes on itself.

An unswept wing with its aerodynamic centre a distance $e$ ahead of the elastic axis, restrained by a
torsional stiffness $K_\theta$, twists under its own lift until the elastic moment balances the aerodynamic
one.

$$ K_\theta\,\theta = q\,S\,e\,a\left(\alpha_0 + \theta\right) $$

Solving for the elastic twist shows the denominator that governs everything.

$$ \theta = \frac{q\,S\,e\,a\,\alpha_0}{K_\theta - q\,S\,e\,a} $$

The twist becomes unbounded when the denominator vanishes, which defines the divergence dynamic pressure.

$$ q_D = \frac{K_\theta}{S\,e\,a} $$

Substituting that back gives the total angle of attack, and therefore the lift, as the rigid value
multiplied by a single factor.

$$ \alpha_0 + \theta = \frac{\alpha_0}{1 - q/q_D} $$

- [Vector Solution of the Three-Degree Case of Wing Bending...][research_arnold_1942]
- [Effect of Torsional Stiffness Requirements on Wing Structural...][research_micks_1950]
- [On the torsional stiffness of closed-section web stiffeners][research_dooley_1965]
- [116. On selection of the method of determining tyre torsional...][research_116_on_1972]
- [Torsional stiffness of plastic tubes reinforced with glass...][research_torsional_stiffness_1972]
- [Effective Torsional Stiffness of Equivalent Beams][research_effective_torsional_1976]
- [Minimum-Weight Design of Thin-Walled Cylinders Subject to...][research_parbery_karihaloo_1980]
- [An Analysis of Traction Drive Torsional Stiffness][research_rohn_loewenthal_1985]
- [Optimal Design of Thin-Walled Cylinders of Variable...][research_parbery_olhoff_1987]
- [Torsional stiffness for circular orthotropic beams][research_dubigeon_1992]
- [Torsional stiffness of NITINOL-reinforced composite drive...][research_baz_chen_1993]
- [Maximal torsional rigidity some qualitative remarks][research_tahraoui_1994]
- [Torsional stiffness and fatigue study of surface-mounted...][research_torsional_stiffness_1994]

**The amplification is the same factor for lift, for twist and for the loads**, which is why a prediction of
it is worth publishing and why an error in it moves everything at once.

**The primary record states both of the quantities needed to invert this.** That same memorandum gives the
wing's **predicted elastic-to-rigid lift-curve-slope ratio as about 1.6**, and gives the
**design dynamic pressure as 1,700 pounds per square foot at Mach 1.07 at sea level**. Those two figures
were published for different purposes and neither was derived from the other.

### Checking the Design Point Against Itself

Before inverting anything, the design point is quoted twice over, once as a dynamic pressure and once as a
Mach number at an altitude, so the two statements can be checked against one another.

$$ q = \tfrac{1}{2} \rho_0 \left(M a_0\right)^2 = \tfrac{1}{2} \times 0.0023769 \times \left(1.07 \times 1116.45\ \mathrm{ft/s}\right)^2 = 1695.9\ \mathrm{lb/ft^2} $$

Against the quoted 1,700 pounds per square foot that agrees to **0.24 percent**.
**This is a check on the source rather than on the analysis**, and it passes, which means the two statements
in the report describe the same flight condition and either may be used.

### Inverting for the Divergence Boundary

Rearranging the amplification relation for $q_D$ gives the boundary directly.

$$ q_D = \frac{q}{1 - 1/r}, \qquad r = \frac{C_{L_\alpha}^{\mathrm{elastic}}}{C_{L_\alpha}^{\mathrm{rigid}}} $$

Substituting the two published figures,

$$ \frac{q}{q_D} = 1 - \frac{1}{1.6} = 0.375 $$

$$ q_D = \frac{1700\ \mathrm{lb/ft^2}}{0.375} = 4533\ \mathrm{lb/ft^2} $$

**The X-29A's wing diverged at about 4,533 pounds per square foot**, and that number appears nowhere in the
literature. It follows from two figures that do appear, through a relation neither was derived from, and
**it requires no knowledge whatever of the wing's stiffness, its geometry, its material or its ply angles.**

### What That Margin Actually Was

The margin is best stated twice, because dynamic pressure and speed are not the same statement.

$$ \frac{q_D}{q_{\mathrm{design}}} = 2.667, \qquad \frac{V_D}{V_{\mathrm{design}}} = \sqrt{2.667} = 1.633 $$

Dynamic pressure and equivalent airspeed are related through sea-level density alone, which is what makes
equivalent airspeed the natural currency for a structural limit.

$$ q = \tfrac{1}{2}\rho V^2 = \tfrac{1}{2}\rho_0 V_e^2, \qquad V_e = \sqrt{\frac{2q}{\rho_0}} $$

Expressed as equivalent airspeeds,

$$ V_{e,\mathrm{design}} = 709\ \mathrm{kt}, \qquad V_{e,D} = 1157\ \mathrm{kt} $$

**A factor of 2.667 in dynamic pressure sounds comfortable and a factor of 1.633 in speed sounds much less so**,
and it is the latter that a pilot experiences. The aircraft's design point sat at
**thirty-seven and a half percent of the way to a structural instability with no natural limit**, and the
amplification at that point was already sixty percent.

The approach is worth tabulating, because the relation is strongly non-linear and its behaviour near the
boundary is the reason the whole problem is difficult.

| Dynamic pressure, lb/ft² | Fraction of $q_D$ | Elastic-to-rigid ratio |
|---|---|---|
| 500 | 0.110 | 1.124 |
| 1,000 | 0.221 | 1.283 |
| 1,500 | 0.331 | 1.495 |
| 1,700 | 0.375 | 1.600 |
| 2,000 | 0.441 | 1.789 |
| 3,000 | 0.662 | 2.957 |
| 4,000 | 0.882 | 8.500 |
| 4,400 | 0.971 | 34.000 |

### How Hard the Answer Leans on a Rounded Figure

The boundary was inverted from a ratio quoted to two significant figures, so it is worth asking how much
that rounding costs. Writing the inversion as a product makes the sensitivity immediate.

$$ q_D = \frac{q\,r}{r - 1} \quad \Longrightarrow \quad \frac{d \ln q_D}{d \ln r} = -\frac{1}{r - 1} $$

$$ \left.\frac{d \ln q_D}{d \ln r}\right|_{r = 1.6} = -\frac{1}{0.6} = -1.667 $$

**A one percent error in the published ratio is a 1.67 percent error in the boundary derived from it**, and
the sign is negative, so a ratio that was optimistically low produces a boundary that is optimistically
high. That elasticity is used again in the section on where the framing breaks down.

**The last two rows are the reason the margin had to be as large as it was.** Between 3,000 and 4,000 pounds
per square foot the wing's lift amplification triples, and a design error of ten percent in the predicted
boundary moves the loads by far more than ten percent.
**The penalty for being wrong is not proportional to the size of the error.**

For comparison, the same report notes that
**conventional aft-swept wings have elastic-to-rigid ratios below one**, because bending washes them out
rather than in. The X-29's wing sits on the other side of unity by construction, and the sign is the entire
difference.

- [The Influence of the Aerodynamic Span Effect on the Magnitude...][research_hildebrandfrancisb_reissnereric_1944]
- [A Tabulation Method for the Calculation of the Critical Speed...][research_targoff_1947_b]
- [Divergence of swept wings][research_diederichfranklinw_budianskybernard_1948]
- [Divergence Paralysis with Increased Intracranial Pressure][research_chamlin_davidoff_1950]
- [DIVERGENCE PARALYSIS WITH INCREASED INTRACRANIAL PRESSURE][research_chamlin_1951]
- [On the Relation between Vorticity, Deformation and Divergence...][research_petterssen_1953]
- [A study of the effects of aeroelastic divergence on the wing...][research_a_study_1973]
- [Static stability and aperiodic divergence][research_sachs_1975]
- [Avoiding divergent stall in control configured aircraft by...][research_mccutchen_1980]
- [Illustration of airfoil shape effect on forward-swept wing...][research_bland_1980]
- [Wind-tunnel experiments on divergence of forward-swept wings][research_rickettsrh_doggettrvjr_1980]
- [of Forward Swept Composite Wings Divergence][research_weisshaar_1980]
- [Aeroelastic divergence of unrestrained vehicles][research_rodden_1981]
- [Active Control of Forward-Swept Wings with Divergence and...][research_griffin_eastep_1982]
- [Swept composite wing aeroelastic divergence experiments][research_blair_weisshaar_1982]
- [Unrestrained Aeroelastic Divergence in a Dynamic Stability...][research_rodden_bellinger_1982]
- [Real Time Divergence Measurement from Single Doppler Radar][research_koscielny_1983]
- [Aeroelastic Divergence of Unrestrained Vehicles][research_rodden_1984]
- [Divergence speed degradation of forward-swept wings with...][research_eastep_venkayya_1984]
- [Divergence/flutter suppression system for a forward...][research_rimer_chipman_1984]
- [Flutter and divergence aeroelastic characteristics for...][research_lottati_1985]
- [Aeroelastic divergence of trimmed aircraft][research_niblett_1986]
- [Divergence study of a high-aspect ratio, forward-swept wing][research_colesr_1986]
- [Aeroelastic divergence of swept-forward composite wings...][research_librescu_khdeir_1988]
- [Divergence study of a high-aspect-ratio, forward swept wing][research_cole_1988]
- [General formulation for the aeroelastic divergence of...][research_librescu_simovich_1988]
- [Comment on 'Divergence study of a high-aspect ratio, forward...][research_rodden_1989_b]
- [Comment on 'General formulation of the aeroelastic divergence...][research_rodden_1989]
- [Transonic flutter/divergence characteristics of...][research_isogai_1992]
- [Shape sensitivity analysis of divergence dynamic pressure][research_bhardwaj_kapania_1995]

### Where the Washin Comes From

The inverted boundary is a number without a mechanism. The mechanism is one line of geometry.

Let $y$ run along the wing's elastic axis and let $\Lambda$ be the sweep of that axis, positive aft. A
deformed section rotates for two reasons, namely the elastic twist $\theta$ about the axis and the bending
slope $w'$ perpendicular to it. Resolving both onto the spanwise direction that a streamwise section pitches
about gives the change in streamwise angle of attack.

$$ \Delta\alpha(y) = \theta(y)\cos\Lambda - w'(y)\sin\Lambda $$

**That single relation contains the whole forward-sweep problem.** For an aft-swept wing $\sin\Lambda$ is
positive, so upward bending subtracts from the angle of attack and the wing washes out, which is stabilising
and is why swept-back wings are difficult to diverge.
**For a forward-swept wing $\sin\Lambda$ is negative, the sign of the bending term reverses, and upward bending adds to the angle of attack.**
The wing washes in, the lift grows, the bending grows, and the loop closes.

**The sign of one trigonometric function is the difference between a wing that is safe and a wing that needs a research programme.**

### A Two-Mode Model, and What It Is For

The boundary itself is already known from the inversion above and needs no model. What a model supplies is
the **scaling**, meaning how the boundary moves with sweep and with bend-twist coupling, and that is what
the rest of this section uses.

Take a uniform cantilever wing of semispan $L$, streamwise chord $c$, bending stiffness $EI$ and torsional
stiffness $GJ$, with a composite constitutive law that couples the two.

$$ \begin{Bmatrix} M \\ T \end{Bmatrix} = \begin{bmatrix} EI & K \\ K & GJ \end{bmatrix} \begin{Bmatrix} w'' \\ \theta' \end{Bmatrix} $$

Here $K$ is the bend-twist coupling that aeroelastic tailoring exists to supply, and $K = 0$ is the
isotropic metal wing. Assume the lowest admissible mode shapes, writing $\eta = y/L$ for the fractional
station, namely $w = h\,\eta^2$ and $\theta = \Theta\,\eta$, and apply strip theory with the lift acting a
distance $e$ ahead of the elastic axis. The equilibrium condition becomes a generalised eigenvalue problem
in the dynamic pressure.

$$ \left(\mathbf{S} - q\,\mathbf{A}\right)\begin{Bmatrix} h \\ \Theta \end{Bmatrix} = \mathbf{0}, \qquad \det\left(\mathbf{S} - q\,\mathbf{A}\right) = 0 $$

with the structural and aerodynamic matrices following from the assumed modes,

$$ \mathbf{S} = \begin{bmatrix} 4EI/L^3 & 2K/L^2 \\ 2K/L^2 & GJ/L \end{bmatrix}, \qquad \mathbf{A} = c\,a\begin{bmatrix} -\tfrac{1}{2}\sin\Lambda & \tfrac{L}{4}\cos\Lambda \\ -\tfrac{2e}{3}\sin\Lambda & \tfrac{eL}{3}\cos\Lambda \end{bmatrix} $$

The structural matrix follows from the strain energy of the coupled beam evaluated on those shapes.

$$ U = \tfrac{1}{2}\int_0^L \left[ EI\,(w'')^2 + GJ\,(\theta')^2 + 2K\,w''\theta' \right] dy $$

$$ \int_0^L (\phi'')^2 dy = \frac{4}{L^3}, \qquad \int_0^L (\psi')^2 dy = \frac{1}{L}, \qquad \int_0^L \phi''\psi'\,dy = \frac{2}{L^2} $$

**The characteristic equation is linear rather than quadratic, and that is a property of the model rather than an approximation.**
The quadratic coefficient is

$$ (ca)^2 e\,L\cos\Lambda\sin\Lambda\left(-\tfrac{1}{6} + \tfrac{1}{6}\right) = 0 $$

identically. This is worth stating because a solver that does not know it will find the cancellation only to
floating-point precision, take the quadratic branch, and return values with no physical content whatever.
**The first version of this calculation did exactly that and reported a divergence dynamic pressure of 5.7 × 10²¹ pounds per square foot at twenty degrees of forward sweep.**
A residue sixteen orders of magnitude below the terms that produced it is enormous in absolute terms, so an
absolute tolerance cannot catch it and the test has to be made relative to the magnitude of what cancelled.

- [Successive Approximations by the Rayleigh-Ritz Variation...][research_macdonald_1933]
- [An Analysis of the Large Deflections of Beams using the...][research_walker_hall_1968]
- [Error Bounds for Sturm-Liouville Eigenvalue Approximations by...][research_johnson_1969]
- [Error bounds for the Rayleigh-Ritz-Galerkin method][research_schultz_1969]
- [Rayleigh Ritz Galerkin Methods for Multidimensional Problems][research_schultz_1969_b]
- [The Rayleigh-Ritz Method A Graphical Proof][research_flores_mello_1969]
- [The Rayleigh Ritz Process for the Simplest Problem in the...][research_simpson_1969]
- [Elliptic Spline Functions and the Rayleigh-Ritz-Galerkin...][research_schultz_1970]
- [$L^2 $ Error Bounds for the Rayleigh Ritz Galerkin Method][research_schultz_1971]
- [An Energy Method for Prediction of Helicopter Maneuverability][research_wood_livingston_1971]
- [A method for selection of significant terms in the assumed...][research_craver_egle_1972]
- [Higher Order Convergence Results for the Rayleigh Ritz Method...][research_pierce_varga_1972]
- [Improvement of Rayleigh Ritz Eigenfunctions][research_kohn_1972]
- [Rayleigh-Ritz Method, Secular Determinant, and Anharmonic...][research_graffi_grecchi_1973]
- [On the Numerical Stability of the Rayleigh Ritz Method][research_omodei_1977]
- [A combined Rayleigh-Ritz/finite element method for the...][research_crisfield_1978]
- [Method of generalized coordinates and an application to...][research_dienes_1978]
- [On the condition number in the rayleigh-ritz method for...][research_schiop_1979]
- [Rayleigh-Ritz vibration analysis of Mindlin plates][research_dawe_roufaeil_1980]
- [MODIFIED RAYLEIGH-RITZ METHOD IN NONAXISYMMETRIC...][research_kalam_1981]
- [Rayleigh-Ritz vibration analysis of rectangular Mindlin...][research_roufaeil_dawe_1982]
- [Analysis of vibrating orthotropic rectangular plates by a...][research_laura_viazzi_1985]
- [Generalized coordinates accounting external term in...][research_hatake_1985]
- [Generalized Coordinates Affected by External Term in...][research_hatake_1986]
- [Determination of elastic constants of orthotropic plates by a...][research_deobald_gibson_1988]
- [An a posteriori error estimation of the Rayleigh-Ritz...][research_zitnan_1989]
- [More on Rayleigh Ritz Refinement Technique for Nearly...][research_haviv_1989]
- [Rayleigh-ritz vibration analysis of thick plates by a simple...][research_lim_senthilnathan_1989]
- [Vibration analysis of plates with cutouts by the modified...][research_lam_hung_1989]
- [Comments on ‘vibration analysis of plates with cutouts by the...][research_gelos_laura_1990]
- [Comments on “Rayleigh-Ritz vibration analysis of thick plates...][research_savithri_varadan_1990]
- [Zur Konvergenz des Rayleigh-Ritz-Verfahrens bei...][research_mertins_1991]
- [Asymptotische Fehlerschranken f�r...][research_mertins_1992]
- [A Superposition-Rayleigh-Ritz Method For Free Vibration...][research_gorman_singhal_1993]
- [Vibration Analysis of Annular Plates with Concentric Supports...][research_wang_thevendran_1993]
- [Beam‐Buckling Analysis via Automated Rayleigh‐Ritz Method][research_wang_wang_1994]
- [Comparison of Simple and Chebychev Polynomials in...][research_singhvi_kapania_1994]
- [Dynamic Condition Estimation and Rayleigh Ritz Approximation][research_tang_1994]
- [A Posteriori Error Estimation for a New Stabilized...][research_romkes_prudhomme_2002]

### The Root in Closed Form, Which Is Where the Argument Actually Lives

Because the characteristic equation is linear, the untailored root can be written out, and it is far more
informative than the eigenvalue it came from.

$$ \frac{1}{q_D} = \underbrace{\frac{c\,a\,e\,L^2\cos\Lambda}{3\,GJ}}_{\text{torsion}} \;-\; \underbrace{\frac{c\,a\,L^3\sin\Lambda}{8\,EI}}_{\text{bending}} $$

**The first term is ordinary torsional divergence and is always positive.** What follows it is the bending
contribution, and **its sign is the sign of the sweep**. Aft sweep subtracts from the reciprocal and raises
the boundary. Forward sweep adds to it and lowers the boundary. The forward-sweep problem is one minus sign
in one term.

**And the relation says something the eigenvalue does not.** If aft sweep is carried far enough the two
terms cancel, the reciprocal vanishes, and the boundary goes to infinity. Setting them equal and dividing
through by the cosine gives the critical angle in closed form.

$$ \tan\Lambda_{\mathrm{crit}} = \frac{8\,e\,EI}{3\,GJ\,L} = 48.013^\circ $$

**This is a check on the numerical solver as much as a result.** The closed form and the eigenvalue scan
agree to every digit printed at every sweep angle tested, from forty degrees forward to forty-eight aft,
which is what makes the sweep table below trustworthy despite resting on stiffnesses nobody published.

- [Attachment-Line Flow on an Infinite Swept Wing][research_cebeci_1974]
- [Measurements in an incompressible three-dimensional turbulent...][research_vandenberg_elsenaar_1975]
- [Three-Dimensional Boundary Layers Over an Infinite Swept Bump...][research_wu_squires_1995]

### The Sweep Trend

With the model behaving, the boundary can be tracked across sweep at fixed stiffness. The absolute values
below depend on stiffnesses that were never published and are therefore **assumed**, so only the ratios
carry meaning and the table is normalised on the unswept case.

| Elastic axis sweep | $q_D$ relative to unswept |
|---|---|
| 40° forward | 0.744 |
| 36.2° forward | 0.747 |
| 30° forward | 0.760 |
| 20° forward | 0.801 |
| 10° forward | 0.876 |
| 0° | 1.000 |
| 10° aft | 1.207 |
| 20° aft | 1.583 |
| 30° aft | 2.404 |

**Sweeping aft raises the boundary steeply and sweeping forward lowers it**, which is the expected
direction. Pushed further, the model does something better than agreeing in direction.

$$ \Lambda \geq \Lambda_{\mathrm{crit}} = 48.0^\circ \implies \text{no positive root, and therefore no divergence boundary at all} $$

**Sufficient sweepback removes divergence entirely**, which is the classical textbook result and is not
something the model was fitted to reproduce. Recovering it from an independent scan of the determinant is
the strongest available evidence that the formulation is sound, and it is why the sweep trend above can be
trusted even though the absolute numbers cannot.

### What Aeroelastic Tailoring Had to Supply

Bend-twist coupling is reported here as a non-dimensional ratio, because the raw stiffness is meaningless
without the others. The laminate mechanics behind it are in [Jones][book_jones_composite] and
[Tsai and Hahn][book_tsai_hahn], and the aeroelastic consequences in
[Bisplinghoff, Ashley and Halfman][book_bisplinghoff] and [Hodges and Pierce][book_hodges].

$$ \psi = \frac{K}{\sqrt{EI \cdot GJ}} $$

The bound on it is the determinant of the stiffness matrix staying positive.

$$ EI \cdot GJ - K^2 > 0 \quad \Longleftrightarrow \quad \lvert \psi \rvert < 1 $$

**The bound $\lvert \psi \rvert < 1$ is not a modelling convenience. It is positive definiteness of the stiffness matrix**,
which is to say it is a statement about energy, and no laminate at any ply angle can exceed it. That bound
is what makes the following question answerable rather than open.

| Coupling $\psi$ | $q_D$ relative to untailored |
|---|---|
| 0.00 | 1.000 |
| 0.10 | 1.129 |
| 0.20 | 1.274 |
| 0.30 | 1.444 |
| 0.40 | 1.657 |
| 0.50 | 1.954 |
| 0.60 | 2.456 |
| 0.70 | 3.712 |
| 0.80 | 25.444 |
| 0.8117 | divergence eliminated entirely |

Two results follow, of which the later one carries more weight.

**First, the coupling needed to reach the X-29's actual margin is $\psi = 0.627$**, taking the untailored
wing's boundary and multiplying it by the 2.667 established from the inversion. That is
**roughly five eighths of the theoretical maximum**, which is a large fraction of a hard physical bound to
be spending on one requirement.

**Second, there is a value of coupling beyond which the wing does not diverge at any speed.** At $\psi =
0.812$ the positive root disappears, exactly as it does under sufficient sweepback.
**The technology does not merely raise the boundary. It can remove it.**

### Whether That Number Survives the Assumptions

The required coupling was computed with stiffnesses nobody published, so the obvious objection is that it is
an artefact of the assumption. It is not, and the reason is worth stating.

**The boundary scales linearly with the overall stiffness level, so the required $\psi$ is completely independent of it.**
Only the ratio $GJ/EI$ can matter, and across a wide range of that ratio the answer moves very little.

| $GJ/EI$ | Required $\psi$ | $\psi$ eliminating divergence |
|---|---|---|
| 0.15 | 0.790 | 0.921 |
| 0.30 | 0.627 | 0.813 |
| 0.50 | 0.607 | 0.795 |
| 0.80 | 0.645 | 0.827 |

**Across a factor of more than five in the stiffness ratio the required coupling stays between 0.61 and 0.79.**
The conclusion that the X-29's wing needed most of the coupling physically available to a laminate is
therefore robust to the one thing that had to be assumed, and
**the model with two free parameters has demonstrated something only because the answer barely depends on them.**

- [Inplane and Bending Fields of Anisotropic Generally Laminated...][research_padovan_1973]
- [An Exact Solution for Bending Fields in Anisotropic Balanced...][research_padovan_1974]
- [Bending theory of laminated plate][research_ren_1986]
- [Bending theory of laminated plate][research_bending_theory_1987]
- [Bending of a bimodulus laminated plate based on a...][research_fung_doong_1988]
- [Acoustic emissions and transient elastic waves in an...][research_acoustic_emissions_1989]
- [Numerical-perturbation analysis of edge effect in bending...][research_biquan_huanwen_1990]
- [Laminate Plate Theory for Spatially Distributed Induced...][research_wang_rogers_1991]
- [Closed-form analytical solutions for a Griffith crack in a...][research_becker_1992]
- [On the propagation of horizontally polarized shear waves in a...][research_wu_chiu_1992]
- [Elastic constants of orthotropic composite materials using...][research_ayorinde_gibson_1993]

### The Southwell Method, Used in Flight for the First Time

**The most striking thing in the primary flight record is not a number but a technique.**

A divergence boundary cannot be located by flying to it. The X-29 team instead used the
[Southwell method][ref_southwell], which extracts a critical value from measurements taken well below it.
For a structure carrying an initial imperfection $\theta_0$ the twist under load follows

$$ \theta(q) = \theta_0 \frac{q/q_D}{1 - q/q_D} $$

which rearranges into a straight line.

$$ \frac{\theta}{q} = \frac{1}{q_D}\theta + \frac{\theta_0}{q_D} $$

The slope is recovered by least squares over the measured points, and the boundary is its reciprocal.

$$ \hat{m} = \frac{\sum_i (\theta_i - \bar{\theta})(y_i - \bar{y})}{\sum_i (\theta_i - \bar{\theta})^2}, \qquad y_i = \frac{\theta_i}{q_i}, \qquad \hat{q}_D = \frac{1}{\hat{m}} $$

**Plotting $\theta/q$ against $\theta$ gives a line whose slope is the reciprocal of the divergence dynamic pressure.**
The X-29A generated the data from constant-altitude windup turns and pushover-pullup manoeuvres, using both
strain-gauge loads and twist from the flight deflection measurement system. The primary record states
plainly that
**although this was the first application of the Southwell technique to flight test data, it had been used previously to analyse wind tunnel data.**

The report also records that the resulting estimate was
**sensitive to a number of factors including measurement uncertainties, manoeuvre technique, aerodynamic phenomena, and strain gauge loads measurement stations**,
and does not say how sensitive. That is computable.

The lever arm of the fit is the spread in twist across the data, and the twist grows sharply only as the
boundary is approached. An aircraft that can reach just over a third of the way to divergence therefore has
very little of it.

| Reach $q/q_D$ | Twist lever, multiples of $\theta_0$ | Median error | Ninetieth percentile |
|---|---|---|---|
| 0.20 | 0.22 | 6.66 percent | 16.21 percent |
| 0.30 | 0.39 | 3.94 percent | 9.48 percent |
| 0.375 | 0.55 | 2.77 percent | 6.79 percent |
| 0.50 | 0.93 | 1.63 percent | 4.06 percent |
| 0.70 | 2.24 | 0.68 percent | 1.65 percent |
| 0.85 | 5.55 | 0.28 percent | 0.66 percent |

Those figures assume two percent noise on the twist measurement.
**The X-29A sat at 0.375 on that table at its design point**, so the geometry of its own envelope put it
near the fragile end. Holding the reach fixed there and varying the measurement quality instead gives the
sensitivity the report describes.

| Twist measurement noise | Median error in $q_D$ | Ninetieth percentile |
|---|---|---|
| 1 percent | 1.40 percent | 3.44 percent |
| 2 percent | 2.77 percent | 6.79 percent |
| 5 percent | 6.95 percent | 16.44 percent |
| 10 percent | 13.89 percent | 31.79 percent |
| 20 percent | 26.35 percent | 48.93 percent |

**The error in the estimated boundary is very close to a fixed multiple of the measurement error, at about 1.4 times it.**
That is the quantitative content of the report's warning. A five percent error in twist becomes a seven
percent error in the divergence boundary, and at the amplification rates tabulated earlier a seven percent
error in the boundary is a large error in the loads.

**The method is sound and the flight application was a genuine first.** What limited it was that the
aircraft could not fly close enough to the thing it was trying to measure, which is the same difficulty in a
different form.

- [Optimal aeroelastic design of an oblique wing structure][research_gwinlb_1974]
- [Aeroelastic Stability and Control of an Oblique Wing Wind...][research_jones_1976]
- [Aeroelastic stability and control of an oblique wing][research_jones_nisbet_1976]
- [Optimal Aeroelastic Design of an Oblique Wing Structure][research_gwin_1976]
- [Effect of wing flexibility on the experimental aerodynamic...][research_hopkinsej_yeesc_1977]
- [Aeroelastic Stability and Performance Characteristics of...][research_weisshaar_1978]
- [Forward Swept Wing Static Aeroelasticity][research_weisshaar_1979]
- [Study of the feasibility aspects of flight testing an...][research_moureydj_1979]
- [Aeropropulsive characteristics of twin nonaxisymmetric...][research_caponefj_1981]
- [Propulsive Aerodynamics of an Advanced Nozzle/Forward Swept...][research_bowers_1981]
- [Dual wing, swept forward swept rearward wing, and single wing...][research_rhodesmd_selbergbp_1982]
- [Dynamic stability of flexible forward swept wing aircraft][research_weisshaarta_zeilerta_1982]
- [High angle-of-attack characteristics of a forward-swept wing...][research_graftonsb_gilberwp_1982]
- [On the track of practical forward-swept wings][research_hertztj_shirkmh_1982]
- [Aeroelastic stability of forward swept composite winged...][research_weisshaarta_1983]
- [Aeropropulsive characteristics of twin single-expansion-ramp...][research_masonml_caponefj_1983]
- [Dynamic stability of flexible forward swept wing aircraft][research_weisshaar_zeiler_1983]
- [High angle-of-attack flight dynamics of a forward-swept wing...][research_murridg_croomma_1983]
- [Rigid-body structural mode coupling on a forward swept wing...][research_miller_wykes_1983]
- [Active suppression of aeroelastic instabilities on a...][research_noll_eastep_1984]
- [Body-freedom flutter of a 1/2-scale forward-swept-wing model...][research_chipmanr_rauchf_1984]
- [Control of forward swept wing configurations dominated by...][research_rimerm_chipmanr_1984]
- [Generic Approach to Determine Optimum Aeroelastic...][research_oyibo_1984]
- [Quadratic synthhesis of integrated active controls for an...][research_gilbert_schmidt_1984]
- [Wind-tunnel free-flight investigation of a model of a...][research_murridg_nguyenlt_1984]
- [A forward-swept wing configuration designed for high...][research_mannmj_mercerce_1985]
- [Comment on "Generic Approach to Determine Optimum Aeroelastic...][research_weisshaar_1985]
- [Experimental aeroelastic behavior of unswept and...][research_landsberger_dugundji_1985]
- [Transonic test of a forward swept wing configuration...][research_chipmanr_rauchf_1985]
- [Control of a forward-swept-wing configuration dominated by...][research_rimer_chipman_1986]
- [Forward-swept wing configuration designed for high...][research_mannmj_mercerce_1986]
- [Performance of a forward swept wing fighter utilizing thrust...][research_miller_1986]
- [Experimental aeroelastic behavior of forward-swept...][research_chen_dugundji_1987]
- [Experiment Investigation on Longitudinal Characteristics of...][research_guo_wang_1988]
- [Oblique wing aircraft flight control system][research_clark_letron_1989]
- [Static aeroelasticity of a composite oblique wing in...][research_bohlmannjonathand_1989]
- [Exploratory wind tunnel investigation of the stability and...][research_coepaulljr_perkinsjohnn_1990]
- [Predicted and measured in-flight wing deformations of a...][research_lokoswilliama_1990]
- [Analytical studies on static aeroelastic behavior of...][research_librescu_thangjitham_1991]
- [Forward sweep - A favorable concept for a laminar flow wing][research_redeker_wichmann_1991]
- [In-flight lift-drag characteristics for a forward-swept wing...][research_saltzmanedwinj_hicksjohnw_1994]
- [Pressure measurements on a forward-swept wing-canard...][research_lombardi_morelli_1994]

- [The Associated Matrices of Bending and Coupled...][research_targoff_1947]
- [THE ANALYSIS OF RECTANGULAR DIAGRIDS BY ANISOTROPIC PLATE...][research_jaeger_hendry_1959]
- [Bending of an elliptical anisotropic plate with two...][research_meglinskii_1966]
- [A Theory of Torsional and Coupled Bending Torsional Waves in...][research_aggarwal_cranch_1967]
- [A Study on Plastic Bending of an Anisotropic Plate][research_sugimoto_saito_1968]
- [A Study on Plastic Bending of an Anisotropic Plate 2nd...][research_sugimoto_saito_1969]
- [Anisotropic Plate Analysis-Boundary Conditions][research_ashton_1970]
- [Static Fields of Curved Generally Laminated Anisotropic Plate...][research_padovan_gosset_1974]
- [Bending of a finite anisotropic plate with a curvilinear hole][research_kosmodamianskii_mitrakov_1976]
- [A computer program for the analysis of the dynamic...][research_picon_alarcon_1978]
- [Characterization of graphite/epoxy laminates for aeroelastic...][research_shyprykevichp_1979]
- [Aeroelastic Tailoring Studies in Fighter Aircraft Design][research_triplett_1980]
- [Applied theory of vibrations of anisotropic laminate shells...][research_kuznetsov_kartashov_1980]
- [Aeroelastic Tailoring of Forward Swept Composite Wings][research_weisshaar_1981]
- [Description of the HiMAT Tailored composite structure and...][research_monaghanrc_1981]
- [Second boundary-value problem of the theory of elasticity for...][research_bogan_1981]
- [The Linear Anisotropic Plate][research_gilbert_schneider_1981]
- [Wind Tunnel Demonstration of Aeroelastic Tailoring Applied to...][research_sherrer_hertz_1981]
- [Bending of a semiinfinite anisotropic plate weakened by...][research_lyubchak_filshtinskii_1982]
- [Effect of Transverse Shear Deformation on Anisotropic Plate...][research_cohen_1982]
- [Residual Stress Measurement of Laminated Anisotropic Plate by...][research_doi_kataoka_1982]
- [The Effect of Bending-Torsion Coupling on Fan and Compressor...][research_bendiksen_friedmann_1982]
- [Vibration of Cantilevered Graphite/Epoxy Plates With...][research_jensen_crawley_1982]
- [Bending of an anisotropic plate containing an anisotropic...][research_zadvornyak_martynovich_1983]
- [Elasticity theory problem for a multiconnected anisotropic...][research_kaloerov_1983]
- [Frequency Determination Techniques for Cantilevered Plates...][research_jensen_crawley_1984]
- [Problem of thermoelasticity for an anisotropic plate with a...][research_berezhnitskii_denisyuk_1985]
- [Aeroelastic tailoring - Theory, practice, and promise][research_shirk_hertz_1986]
- [Aeroelastic tailoring of composite wings with external stores][research_greenja_1986]
- [Residual Stress Measurement of Laminated Anisotropic Plate by...][research_kataoka_dol_1986]
- [A field-consistent, four-noded, laminated, anisotropic...][research_somashekar_prathap_1987]
- [Aeroelastic tailoring of aft-swept high-aspect-ratio...][research_green_1987]
- [A General Boundary Integral Formulation for the Anisotropic...][research_shi_bezine_1988]
- [Aeroelastic tailoring for oblique wing lateral trim][research_bohlmannjonathand_weisshaarterrencea_1988]
- [Aeroelastic tailoring of a composite wing with a decoupler...][research_lottati_1988]
- [Aeroelastic tailoring][research_isogai_1988]
- [Finite-Width Correction Factors for Anisotropic Plate...][research_tan_1988]
- [A general boundary integral formulation for the anisotropic...][research_a_general_1989]
- [Direct search method to aeroelastic tailoring of a composite...][research_isogai_1989]
- [Analytical method for solving nonlinear multilayer...][research_grigolyuk_kulikov_1990]
- [Static aeroelastic tailoring for oblique wing lateral trim][research_bohlmann_eckstrom_1990]
- [A Taguchi study of the aeroelastic tailoring design process][research_bohlmannjonathand_scottrobertc_1991]
- [Aeroelastic tailoring analysis for advanced turbo propellers...][research_yamane_1992]
- [Multilayered anisotropic plate models with continuous...][research_sciuva_1992]
- [On the static aeroelastic tailoring of composite aircraft...][research_librescu_song_1992]
- [Aeroelastic tailoring analysis for preliminary design of...][research_yamane_friedmann_1993]
- [Thin tailored composite wing for civil tiltrotor][research_raisrohanimasoud_1994]
- [Development of a composite tailoring procedure for airplane...][research_chattopadhyayaditi_zhangsen_1995]
- [Performance Improvement of Composite Wings through...][research_meirovitch_1995]
- [The linearization of the Dirichlet to Neumann map in...][research_ikehata_1995]
- [An Investigation of the Aeroelastic Tailoring for Smart...][research_giese_reich_1996]
- [Development of a Composite Tailoring Technique for Airplane...][research_chattopadhyayaditi_jharatneshwar_1996]
- [Aeroelastic Tailoring for Stability Augmentation and...][research_nixonmarkw_piatakdavidj_1999]
- [Active Aeroelastic Tailoring of High-Aspect-Ratio Composite...][research_cesnik_2002]
- [Validation of Design and Analysis Techniques of Tailored...][research_jegleydawnc_wijayratnedulnathd_2004]
- [Active Aeroelastic Tailoring of High-Aspect-Ratio Composite...][research_cesnik_2005]
- [Aeroelastic Tailoring of a Plate Wing with Functionally...][research_dunningpeterd_stanfordbretk_2014]
- [Trim and Structural Optimization of Subsonic Transport Wings...][research_stanfordbretk_juttechristinev_2014]

- [I. Several experiments concerning the preserving of flowers...][research_southwell_1698_b]
- [IV. Some Philosophical experiments, communi­cated by the...][research_southwell_1698]
- [LXIII. Richard Southwell to Cromwell][research_southwell_1843]
- [Southwell Cathedral][research_southwell_cathedral_1885]
- [A Further Note on Ilisha Parthenogenetica Southwell and...][research_southwell_prashad_1923]
- [Robert Southwell][research_hague_1927]
- [THE SOUTHWELL METHOD FOR PREDICTING CRITICAL LOADS OF ELASTIC...][research_ariaratnam_1961]
- [Some Thoughts on the Southwell Plot][research_roorda_1967]
- [The Poems of Robert Southwell, S.J][research_bony_southwell_1969]
- [Southwell Plot for Beam-Columns][research_leicester_1970]
- [An anal ysis of the test loading of a flexible pipe arch...][research_an_anal_1974]
- [Critique of Southwell plots with proposals for alternative...][research_spencer_walker_1975]
- [APPLICATION OF THE SOUTHWELL PLOT METHOD TO THE INSPECTION...][research_southwell_gunn_1981]
- [DISCUSSION. APPLICATION OF THE SOUTHWELL PLOT METHOD TO THE...][research_valsangkar_britto_1982]
- [Applicability of the Southwell Plot to Shear Deformable...][research_koh_kelly_1989]
- [Book Reviews Miscellaneous Reviews David Crookall Kindred, M...][research_book_reviews_1989]
- [On the applicability of the Southwell plot to plastic buckling][research_singer_1989]
- [Anthony D. Cousins, The Catholic Religious Poets from...][research_grace_1992]
- [The Catholic religious poets from Southwell to Crashaw a...][research_the_catholic_1995]

## Dependent Systems

### The Wing Structure

The wing skins are **graphite-epoxy composite**, upper and lower, and the primary record is explicit that
they exist to **aeroelastically tailor the wing deflection and inhibit wing structural divergence**. The
mechanism is stated as **proper ply orientation** producing
**bend-twist coupling combined with high material stiffness properties** to minimise
**the natural washin tendencies under load**.

The structural axis is swept further forward than the planform, and the difference is not small.

$$ \Lambda_{\mathrm{struct}} - \Lambda_{LE} = 36.2^\circ - 29.3^\circ = 6.9^\circ $$

**Divergence is governed by the elastic axis rather than by the leading edge**, so the wing is
aeroelastically almost seven degrees more forward-swept than it appears, and the closed-form root above
depends on the sine of that larger angle rather than the smaller one.

The amplification applies to the loads as well as to the lift, which is what makes it a structural
requirement rather than an aerodynamic curiosity.

$$ \frac{M_{\mathrm{root}}^{\mathrm{elastic}}}{M_{\mathrm{root}}^{\mathrm{rigid}}} \;\geq\; \frac{1}{1 - q/q_D} = 1.6 \quad \text{at the design point} $$

**The inequality runs that way because washin loads the tip preferentially**, moving the centre of pressure
outboard and lengthening the lever arm, so the bending moment grows by at least the lift amplification and
in general by more.

**The record is equally explicit that the cure was partial.** It states that even so, the aeroelastic
properties **remain significantly adverse**, and it is that sentence which the elastic-to-rigid ratio of 1.6
quantifies. The wing was not made to behave like an aft-swept wing. It was made to diverge far enough
outside the envelope to be flyable, and it still amplified its own lift by sixty percent at the design
point.

The structural box **transitions from unswept inboard to swept constant chord lines outboard**, and the four
load measurement stations were oriented to place the torsion axes midway through the box.
**Eighteen strain gauge bridges were installed at each station**, some of them on the composite itself, and
the record notes that equation accuracies were
**typical of Dryden's experience with conventional all-metallic structures**, which is a quietly significant
result about instrumenting composites at all.

The span load distribution was expected to be unconventional,
**particularly in the inboard region because of the strong canard downwash**, which is the first appearance
of a theme that runs through the whole aircraft. **The canard and the wing cannot be analysed separately.**

- [Stress Analysis of Outer Wing Bulkheads and Auxiliary Spar...][research_vaughan_1948]
- [Application study of filamentary composites in a commercial...][research_johnsonrw_junerr_1972]
- [Mixed-Mode Fracture of Unidirectional Graphite/Epoxy...][research_mckinney_1972]
- [Dynamic Mechanical Properties of Graphite-Epoxy and...][research_hirai_kline_1973]
- [NAVAIRDEVCEN Graphite-Epoxy Composite Wing for BQM-34E Static...][research_libeskind_minecci_1973]
- [NAVAIRDEVCEN Graphite-Epoxy Composite Wing for BQM-34E Stress...][research_neu_huang_1973]
- [Filamentary-plastic composite laminate][research_filamentary_plastic_composite_1974]
- [On the Calculation of Interlaminar Normal Stress in Composite...][research_pagano_1974]
- [S-3A Graphite/Epoxy Spoiler Development Program. Volume 1][research_dhonau_blosser_1974]
- [Investigation of Brittle Fractures in Graphite-Epoxy...][research_greszczuk_chao_1975]
- [Ascertainment of the Effect of Compressive Loading on the...][research_ryder_walker_1976]
- [Biaxial Testing of Graphite/Epoxy Composites Containing...][research_daniel_1976]
- [Evaluation of Composite Wing for XFV-12A Airplane][research_ulry_gehring_1976]
- [Fatigue Behavior of Composite Laminate][research_hahn_kim_1976]
- [Residual Strength Degradation Model and Theory of Periodic...][research_yang_liu_1976]
- [Design and fabrication of graphite-epoxy bolted wing skin...][research_johnsonrw_mccartyje_1977]
- [Fatigue Fracture Initiation in Notched Graphite-Epoxy...][research_papirno_1977]
- [Fatigue behaviour of composite laminate][research_fatigue_behaviour_1977]
- [Mixed-Mode Fracture of Graphite/Epoxy Composites][research_morris_1977]
- [Non-linear bending of antisymmetric angle ply laminated plates][research_non_linear_bending_1977]
- [Hybrid composite laminate structures][research_hybrid_composite_1978]
- [Polyester, fibreglass-reinforced composite laminate][research_polyester_fibreglass_reinforced_1978]
- [The Natural Mode Shapes and Frequencies of Graphite Epoxy...][research_crawley_lee_1978]
- [Characterization of Splitting Process in Graphite/Epoxy...][research_mar_lin_1979]
- [Honeycomb-laminate composite structure][research_honeycomb_laminate_composite_1979]
- [Room Temperature Curing Resin Systems for Graphite/Epoxy...][research_crabtree_1979]
- [An Analysis of Interlaminar Stress Gradients and Impact...][research_stanton_crain_1980]
- [Natural Exposure of Selected Graphite/Epoxy Composite...][research_trabocco_1980]
- [Stress Wave Damage in Graphite/Epoxy Laminates][research_roylance_1980]
- [Thermal Degradation of Graphite/Epoxy Composite][research_pritt_1980]
- [Acoustic emission monitors damage progression in...][research_acoustic_emission_1981]
- [Experimental Measurement of Elastic Shear Modulus of...][research_bauchau_1981]
- [Graphite/epoxy composite violin][research_graphite_epoxy_composite_1981]
- [Over 136 000 flying hours logged by graphite/epoxy composite...][research_over_136_1981]
- [Property changes of a graphite/epoxy composite exposed to...][research_property_changes_1981]
- [The viscoelastic behaviour of the principal compliance matrix...][research_the_viscoelastic_1981]
- [Thermal Response of Graphite Epoxy Composite Subjected to...][research_griffis_masumura_1981]
- [Thermal expansion and swelling of cured epoxy resin used in...][research_thermal_expansion_1981]
- [Demonstration of repairability and repair quality on...][research_knaussjf_stonerh_1982]
- [Design considerations and experiences in the use of composite...][research_eckstromcv_spaincv_1982]
- [Development of a Compression Testing Method for...][research_dunmire_1982]
- [Three-Dimensional Elastic Moduli of Graphite/Epoxy Composites][research_knight_1982]
- [Curing of Graphite/Epoxy Composites][research_loos_springer_1983]
- [Optimal Design of High Speed Rotating Graphite/Epoxy Shafts][research_bauchau_1983]
- [Design of a composite wing extension for a general aviation...][research_adneyps_hornwj_1984]
- [Compression failures of damaged graphite epoxy laminates][research_jones_broughton_1985]
- [Damage tolerance of graphite/epoxy composites][research_baker_jones_1985]
- [Directional Thermal Conductivities of Graphite/Epoxy...][research_han_glower_1985]
- [Fabrication of Curved Graphite/Epoxy Compression Test Panels...][research_croop_1985]
- [Interplay of Physical and Chemical Aging in Graphite/Epoxy...][research_mijovic_1985]
- [Matrix cracking and stiffness reduction during the fatigue of...][research_matrix_cracking_1985]
- [Splitting initiation and propagation in notched...][research_daken_mar_1985]
- [Combined bearing and bypass loading on a graphite/epoxy...][research_crews_naik_1986]
- [Delamination Fracture in Graphite/Epoxy Materials][research_bradley_1986]
- [A Composite Plate Theory for Arbitrary Laminate Configurations][research_toledano_murakami_1987]
- [Discussion “A Composite Plate Theory for Arbitrary Laminate...][research_yu_1987]
- [Experimental Aspects of Using Time-Averaged Holographic...][research_rumble_1987]
- [Modeling Stiffness Reduction of Graphite/Epoxy Composite...][research_whitworth_1987]
- [Nonlinear analysis of interlaminar stress in graphite/epoxy...][research_chen_sun_1987]
- [Thermal Response of Radiantly Heated Kevlar and...][research_fanucci_1987]
- [Analysis of the NAVAIRDEVCEN Self-Priming Topcoat on...][research_eng_1988]
- [Damage tolerance and supportability aspects of ARALL laminate...][research_gunnink_1988]
- [Effects of a controlled modulus interlayer upon the...][research_effects_of_1988]
- [Mechanical Properties of Graphite/Epoxy Composites at Various...][research_sun_yoon_1988]
- [Rate sensitivity of Mode II interlaminar fracture toughness...][research_rate_sensitivity_1988]
- [Energy Absorption Behavior of Graphite Epoxy Composite Sine...][research_hanagud_craig_1989]
- [Strength of Composite Laminate with Reinforced Hole][research_lee_mall_1989]
- [Thermal damage effects and delamination toughness of a...][research_thermal_damage_1989]
- [Asymptotic stress field around a crack normal to the...][research_seyoung_1990]
- [Deformational behaviour of a unidirectional graphite/epoxy...][research_deformational_behaviour_1990]
- [Design, Evaluation and Experimental Effort Toward Development...][research_brunojoseph_libeskindmark_1990]
- [On Isotropic Laminate Configurations][research_fukunaga_1990]
- [On the Bearing Strength of Bolted Graphite/Epoxy Laminates][research_eriksson_1990]
- [Static aeroelastic behavior of an adaptive laminated...][research_weisshaarta_ehlerssm_1990]
- [Bending of cross-ply laminated plates using Lagrange...][research_bending_of_1991]
- [Damage Tolerance of Woven Graphite/Epoxy Buffer Strip Panels][research_kennedy_1991]
- [Tanker Operations in a Composite Wing Concept][research_raper_1991]
- [Transverse Ply Cracking in Toughened and Untoughened...][research_yalvac_yats_1991]
- [C-130 Advanced Technology Center wing box conceptual...][research_whiteheadrs_foremancr_1992]
- [Interlaminar shear fracture of interleaved graphite/epoxy...][research_interlaminar_shear_1992]
- [Mode I Interlaminar Fracture of Interleaved Graphite/Epoxy][research_ozdil_carlsson_1992]
- [Proven Force--Proof of Concept for the Composite Wing][research_norwood_1992]
- [A damage mechanics tool for laminate delamination][research_daudeville_ladeveze_1993]
- [Aeroelastic airfoil smart spar][research_greenhalgh_pastore_1993]
- [An analytically designed subcomponent test to reproduce the...][research_davisddjr_farleygaryl_1993]
- [Analysis of an anisotropic composite laminate with a...][research_hong_cheong_1993]
- [Global/local interlaminar stress analysis of a grid-stiffened...][research_wiggenraadjfm_bauldnrjr_1993]
- [Laminate characterisation in the presence of thermal stresses][research_biswas_1993]
- [On the contact of a spherical indenter and a thin composite...][research_christoforou_1993]
- [A Laminate Design for Elastic Properties of Symmetric...][research_fukunaga_sekine_1994]
- [Plane Elasticity Analysis of a Simply Supported Laminate with...][research_philippidis_1994]
- [Simplified methods for the buckling analysis of composite...][research_aston_williams_1994]
- [Static aeroelastic characteristics of a composite wing][research_lee_kim_1994]
- [The failure of integrally stiffened graphite/epoxy cylinders][research_graves_sawicki_1994]
- [Three dimensional exact solution of thermal stresses in...][research_tungikar_rao_1994]
- [Characterization of interlaminar shear failures of...][research_short_1995]
- [Dynamics of graphite/epoxy composite under delamination...][research_lai_young_1995]
- [Energy-release-rate evaluation for delamination growth...][research_naganarayana_atluri_1995]
- [Correlation of Structural Analysis and Test Results for the...][research_wangjohnt_jegleydawnc_1996]
- [Global and Local Stress Analyses of McDonnell Douglas...][research_wangjohnt_1996]
- [Design of a Variable Stiffness Spar][research_kota_hetrick_1997]
- [Structural Test Documentation and Results for the McDonnell...][research_jegleydawnc_bushharoldg_1997]
- [Mechanism Based Failure Laws for Graphite/Epoxy Composites][research_gupta_1998]
- [Nondestructive Evaluation NDE Techniques Assessment for...][research_johnson_nokes_1998]
- [BMI Sandwich Wing Box Analysis and Test][research_palmtod_mahlermary_2000]
- [Health Monitoring for Graphite/Epoxy Motor Cases][research_welle_2000]
- [AST Composite Wing Program Executive Summary][research_karalmichael_2001]
- [Crack Turning Mechanics of Composite Wing Skin Panels][research_yuanfg_reederjamesr_2001]
- [Evaluation of the Structural Response and Failure of a...][research_jegleydawnc_bushharoldg_2001_b]
- [Structural Response and Failure of a Full-Scale Stitched...][research_jegleydawnc_lovejoyandrewe_2001]
- [Structural Testing of a Stitched/Resin Film Infused...][research_jegleydawnc_bushharoldg_2001]
- [Variable Stiffness Spar Wind-Tunnel Model Development and...][research_florancejamesr_heegjennifer_2004]
- [Ram Load Simulation of Wing Skin-Spar Joints New...][research_moshier_2006]
- [Evaluation of a Metallic Repair on a Rod-Stiffened Composite...][research_przekopadam_jegleydawnc_2014_b]

- [Aircraft Structural Research][research_shanley_1943]
- [Charts for the Determination of Wing Torsional Stiffness...][research_pearsonhenrya_aikenwilliamsjr_1944]
- [Stress Analysis of Wing Center Section - Part III - Interspar...][research_mefford_voss_1948]
- [On the Elastic Instability of Orthogonal Anisotropic...][research_hayashi_1949]
- [A Review of Certain Analysis Methods for Swept-Wing Structures][research_williams_1952]
- [WING - STRESS ANALYSIS. MIG-15, SERIAL NO. 120147][research_cornellaeronauticallabincbuffalony_1953]
- [Weight, Balance and Moment of Inertia Calculations for...][research_wickman_1953]
- [Structural Fundamentals][research_structural_fundamentals_1955]
- [DESIGN PROPERTIES OF HIGH-STRENGTH STEELS IN THE PRESENCE OF...][research_sachs_muvdi_1956]
- [The Balance Method Applied to Swept-Wing Stress Analysis][research_broglio_1957]
- [EFFECT OF HEATING ALUMINUM ALLOY WING STRUCTURE TO 325 F ON...][research_bergstedt_turner_1959]
- [Aeroelastic Criterion for Leading Edge Stiffness][research_wooldridge_1960]
- [STRUCTURAL FLIGHT LOADS DATA FROM JET-TANKER OPERATIONS][research_perry_rievley_1961]
- [MOLYBDENUM STRUCTURAL COMPONENT PROGRAM][research_mcdonnellaircraftcorpstlouismo_1962]
- [NEW APPROACHES TO FLIGHT VEHICLE STRUCTURAL VIBRATION...][research_heckl_lyon_1962]
- [ELASTO-PLASTIC ANALYSIS OF STRUCTURES UNDER LOAD AND...][research_edwards_1963]
- [MOLYBDENUM STRUCTURAL COMPONENT PROGRAM][research_mcdonnellaircraftcorpstlouismo_1963]
- [STRUCTURAL DESIGN FOR ACOUSTIC FATIGUE][research_douglasaircraftcolongbeachca_1963]
- [ON INCREASING TREATMENT CONTRAST PRECISION AND THE ESTIMATION...][research_mallios_1964]
- [Structural energy absorption][research_johnson_1964]
- [Designing for structural reliability][research_switzky_1965]
- [HYDROFOIL SHIP STRUCTURAL DESIGN CRITERIA STUDY][research_martincobaltimoremd_1965]
- [Minimum weight design with structural reliability][research_switzky_1965_b]
- [RESEARCH IN AIRCRAFT STRUCTURES ANALYSIS AND DESIGN][research_horton_mayers_1965]
- [Structural analysis flexible grid technique for sst wing...][research_miller_1965]
- [MATRIX ANALYSIS METHODS FOR ANISOTROPIC INELASTIC STRUCTURES][research_jensen_falby_1966]
- [The bending of plate using a three-roll pyramid type plate...][research_bassett_johnson_1966]
- [BREAKING STRENGTH AND ENDURANCE TESTING OF AIRCRAFT CONTROL...][research_smith_1967]
- [FATIGUE STRENGTH DESIGN AND ANALYSIS OF AIRCRAFT STRUCTURES...][research_abelkis_1967]
- [A structural expansion of the cohesive energy of simple...][research_lloyd_sholl_1968]
- [Concorde structural development][research_harpur_1968]
- [ANALYSIS AND OPTIMIZATION OF STORE-AND-FORWARD COMPUTER...][research_frank_1970]
- [Effects of Interlaminar Shear on the Bending and Buckling of...][research_durlofsky_mayers_1970]
- [Finite Element Analysis of Bending-Extensional Coupling in...][research_pryor_barker_1970]
- [STRESS CONCENTRATION AROUND AN ARBITRARILY SHAPED HOLE IN...][research_yamasaki_gotoh_1971]
- [Methodology for Structural Optimization of STOL Aircraft...][research_wollner_1972]
- [Advanced Metallic Structure Air Superiority Fighter Wing...][research_figge_1973]
- [Advanced Metallic Structures Air Superiority Fighter Wing...][research_davis_1973]
- [Advanced Metallic Structures Cargo Wing Design for Improved...][research_brigham_barrie_1973]
- [Bending and torsion of anisotropic beams][research_johnson_1973]
- [Fatigue Behavior of Graphite/Glass/Epoxy Composites][research_rao_hofer_1973]
- [Identification and optimization of aircraft dynamics][research_narendra_tripathi_1973]
- [T-38 Structural Flight Loads Data for June 1970 through...][research_clay_rockafellow_1973]
- [A Structural Weight Estimation Program SWEEP for Air craft...][research_hiyama_1974_b]
- [A Structural Weight Estimation Program SWEEP for Aircraft...][research_ascani_1974]
- [A Structural Weight Estimation Program SWEEP for Aircraft...][research_wildermuth_rothammer_1974]
- [A Structural Weight Estimation Program SWEEP for Aircraft...][research_wildermuth_rothammer_1974_b]
- [A Structural Weight Estimation Program SWEEP for Aircraft...][research_martindale_rockwell_1974]
- [A Structural Weight Estimation Program SWEEP for Aircraft...][research_hayase_1974]
- [A Structural Weight Estimation Program SWEEP for Aircraft...][research_chaloff_hiyama_1974]
- [A Structural Weight Estimation Program SWEEP for Aircraft...][research_hayase_1974_b]
- [A Structural Weight Estimation Program SWEEP for Aircraft...][research_hiyama_1974]
- [A fatigue-testing machine for combined bending and torsion][research_shawki_mashhour_1974]
- [An Interferometric Investigation of Shock Structure and Its...][research_brimelo_glass_1974]
- [Application of advanced composites to helicopter airframe...][research_richmj_ridgleygf_1974]
- [Feasibility Investigation of Zero-Torsional-Stiffness...][research_vance_brown_1974]
- [Band structure of semiconductor alloys beyond the virtual...][research_baldereschi_maschke_1975]
- [Modeling engine static structures with conical shell finite...][research_kielb_1975]
- [Application of a gradient-projection method to minimum weight...][research_craig_erbug_1976]
- [F-111A Wing Fatigue Test Program][research_schneider_1976]
- [Load Analysis and Critical Area Stress Analysis of the...][research_dyess_williamw_1976]
- [Titanium and advanced composite structures for a supersonic...][research_turnermj_hoyjm_1976]
- [A-37B Fatigue Sensor Evaluation Program - Full Scale Test and...][research_walker_kaufman_1977]
- [Primary Adhesively Bonded Structure Technology PABST . Phase...][research_douglasaircraftcolongbeachca_1977]
- [A Critical Load, beyond That Door Or, before the Ultimate...][research_burke_1978]
- [Development of advanced composite structures][research_staufferwa_jamesam_1978]
- [Study of advanced composite structural design concepts for an...][research_study_of_1978]
- [Transverse shear stiffness of laminated anisotropic shells][research_cohenga_1978]
- [An Efficient Structural Resizing Procedure for Meeting Static...][research_lerner_markowitz_1979]
- [An Evaluation of the ADINA Finite Element Program for...][research_stagliano_mente_1979]
- [Fluid-Structure Interaction Dynamics in Aircraft Fuel Tanks][research_ferman_unger_1979]
- [Composite Materials for Structural Design][research_schpey_1980]
- [The History of the Aircraft Structural Integrity Program][research_negaard_1980]
- [Torsional Strength and Stiffness of Steel Structures][research_shermer_1980]
- [Effect of Fighter Attack Spectrum on Composite Fatigue Life][research_badaliance_dill_1981]
- [A simulation language approach to structural interaction...][research_cutchinsma_purvisjw_1982]
- [Bending of laminated anisotropic shells by a shear deformable...][research_reddy_1982]
- [Composite aircraft structure having lightning protection][research_olsonglenno_1982]
- [Composite structural materials][research_ansellgs_loewyrg_1982]
- [Finite Element Analysis of Cracked Plate Subjected to...][research_moriya_1982]
- [Minimum-time 180� turns of aircraft][research_well_berger_1982]
- [Sonic fatigue testing of an advanced composite aileron][research_soovere_1982]
- [Stress Analysis for Anisotropic Hardening in...][research_lee_mallett_1982]
- [Structure-Property Relationships in Intercalated Graphite][research_dresselhaus_dresselhaus_1982]
- [Aeroelastic interference effects between slender structures][research_ruscheweyh_1983]
- [Research on Composite Materials for Structural Design][research_allen_bradley_1983]
- [Structure and Properties of Intercalated Graphite...][research_forsman_1983]
- [Unsteady aerodynamics and vortex induced aeroelastic...][research_modi_slater_1983]
- [ACEE composite structures technology][research_klotzschem_1984]
- [Derivation of the classical plate bending theory from...][research_hu_1984]
- [Research on Composite Materials for Structural Design][research_allen_bradley_1984]
- [Explicit formulation for a high precision triangular...][research_jeyachandrabose_kirkhope_1985]
- [Control of aeroelastic instabilities through stiffness...][research_weisshaar_ryan_1986]
- [Imperfection sensitivity of axially compressed laminated flat...][research_hui_1986]
- [A more accurate evaluation of buckling loads of thin-walled...][research_toader_1987]
- [Aircraft Structural Crash Dynamics Progress in the 1980's][research_wittlin_1988]
- [Composite transport wing technology development Design...][research_griffincharlesf_harvillwilliame_1988]
- [Effect of stretching-bending coupling and shear deformations...][research_adan_sheinman_1988]
- [In-Plane Stress Waves for NDE Nondestructive Evaluation of...][research_pellerin_1988]
- [On the validity of the reduced bending stiffness method for...][research_ewing_hinger_1988]
- [Optimization of the conceptual design and mission profiles of...][research_simos_jenkinson_1988]
- [Prediction of aircraft-propeller-induced, structure-borne...][research_unruh_1988]
- [A study on the effect of bending-twisting coupling on...][research_grenestedt_1989]
- [Composite Materials in Aircraft Structures][research_composite_materials_1989]
- [Development of a Progressive Failure Model for Strength of...][research_tang_1989]
- [Multi-objective/loading optimization for rotating composite...][research_hamiltonbriank_petersjamesr_1989]
- [New generalized structural filtering concept for active...][research_wie_byun_1989]
- [Optimum structural design with static aeroelastic constraints][research_bowmankeithb_grandhiramanav_1989]
- [A study on the effect of bending-twisting coupling on...][research_a_study_1990]
- [Certification of damage tolerant composite structure][research_rapoffandrewj_dillharoldd_1990]
- [Mobility Power Flow Analysis of a Thick Plate Structure][research_cuschieri_1990]
- [Structural optimization with aeroelastic constraints of rotor...][research_celi_friedmann_1990]
- [Vibration analysis of composite plate wing][research_lee_lee_1990]
- [Active Structural Acoustic Control and Smart Structures][research_fuller_1991]
- [Application of a design-build-team approach to low cost and...][research_ilcewiczlb_walkerth_1991]
- [Finite Element Analysis of Free-Edge Delamination in...][research_sandhu_wolfe_1991]
- [ALN 4060 device for recognizing ultrasound wave forms...][research_directiondesrecherches_1992]
- [Adaptive aeroelastic composite wings - Control and...][research_weisshaarterrencea_ehlersstevenm_1992]
- [An improved approach for flight readiness certification...][research_moorenr_ebbelerdh_1992]
- [Buckling of laminated anisotropic plates under cylindrical...][research_spencer_watson_1992]
- [Control design of a UH-60 rotorcraft via CLTR and direct...][research_vansteenwykbrett_lyuyloi_1992]
- [Helicopter rotor blade aeroelasticity in forward flight with...][research_cell_1992]
- [Integrated aerodynamic-structural-control wing design][research_raisrohanim_haftkart_1992]
- [Stresses in edge stiffened anisotropic sandwich plate][research_rao_umamaheswararao_1992]
- [Survey - Applications of structural optimization methods to...][research_miurahirokazu_neilldouglasj_1992]
- [Effect of Bending-Twisting Coupling on Compressive Buckling...][research_fukunaga_sekine_1993]
- [For the advance of the computational structural aeroelasticity][research_ohkuma_1993]
- [pb-2 Rayleigh - Ritz method for general plate analysis][research_liew_wang_1993]
- [44408 Nondestructive analysis of aileron fatigue and aging in...][research_44408_nondestructive_1994]
- [44416 ALN 4060 device for recognizing ultrasound wave forms...][research_44416_aln_1994]
- [Aeroelastic behavior of a composite plate wing with...][research_koo_lee_1994]
- [Aircraft fleet maintenance based on structural reliability...][research_yang_manning_1994]
- [On structural optimization with aeroelasticity constraints][research_ringertz_1994]
- [Tailoring the dynamic characteristics of composite panels...][research_raouf_1994]
- [The cylindrical bending vibration of a laminated elastic...][research_yang_batra_1994]
- [Ultrasonic Evaluation of Stiffness Tensor Changes and...][research_audoin_baste_1994]
- [Unsteady Aerodynamics and Vortex-Induced Aeroelastic Response...][research_modi_slater_1994]
- [Unsteady Structure of Leading-Edge Vortices on a Delta Wing][research_rockwell_1994]
- [Using adaptive structures to attenuate rotary wing...][research_nitzsche_breitbach_1994]
- [Aeroelastic analysis of a flexible control surface with...][research_lee_kim_1995]
- [Buckling analysis of skew plate assemblies Classical plate...][research_york_williams_1995]
- [Design Considerations for a Strain Actuated Adaptive Wing for...][research_lin_crawley_1995]
- [Elasticity solution for laminated anisotropic cylindrical...][research_jing_tzeng_1995]
- [Equivalent dynamic beam rod models of aircraft wing structures][research_lee_1995]
- [Flight Control Applications of 1 sub 1 Optimization][research_spillman_ridgely_1995]
- [Interference between wind loading on group of structures][research_sun_gu_1995]
- [Parametric study for optimization of the specific cost of...][research_sultan_kattab_1995]
- [The restrained torsional response of open section carbon...][research_loughlan_ata_1995]
- [Effective Three-Dimensional 3-D Finite Element Material...][research_alexander_tzeng_1996]
- [Geodesic Wing Structural Optimization and Dynamic Analysis][research_moon_1996]
- [Site Assessment Report for F-16 Crash Site Albany County...][research_operationaltechnologiescorpsanantoniotx_1996]
- [Wing Weight Optimization Under Aeroelastic Loads Subject to...][research_kapaniarakeshk_issacj_1997]
- [Development and Demonstration of Advanced Design Composite...][research_howdyshell_trovillion_1998]
- [C-130 Flight Control Surfaces Depaint Process Optimization][research_cundiff_buckingham_1999]
- [Global-Local Analysis and Optimization of a Composite Civil...][research_raisrohanimasound_1999]
- [Wing Structural Design by Genetic Algorithms and Homotopy...][research_gurdal_haftka_1999]
- [Structural Aspects of Flexible Aircraft Control][research_structural_aspects_2000]
- [Aeroelastic Leveraging and Control through Adaptive Structures][research_clark_2001]
- [Structural Analysis of Helicopter Flight and Hangar Decks][research_stainback_2001]
- [Innovative Local-Global Methods for Wing Structural Design][research_gurdal_2002]
- [E-8/B-707 Wing Station 320 Transition Fit Fastener Finite...][research_shoales_fawaz_2004]
- [Structural Integrity of a Fighter Aircraft Undergoing Dynamic...][research_karniadakis_2004]
- [Structural Testing and Analysis of a Joined Wing Technology...][research_robinson_2004]
- [Design and Analysis of a Hybrid Composite/Metal Structural...][research_thompson_walls_2005]
- [Design and Evaluation of a Reinforced Advanced-Grid Stiffened...][research_biskner_higgins_2005]
- [Multiscale Modeling and Experiments for Design of...][research_white_geubelle_2005]
- [Multiscale Modeling for the Design of Autonomic Healing...][research_kieffer_2006]
- [Estimating Runflat Stiffness][research_bylsma_gunter_2007]
- [The Role of Guidance, Navigation, and Control in Hypersonic...][research_ouztspeterj_solowaydonaldi_2009]
- [Computational Design Optimization Under Uncertainty of...][research_missoum_2012]
- [Aeroelastic Optimization Study Based on the X-56A Model][research_liwesleyw_pakchangi_2014]
- [Analysis and Testing of a Metallic Repair Applicable to...][research_przekopadam_jegleydawnc_2014]

- [Proof of a Fundamental Relation in the Theory of Bending...][research_horsburgh_1911]
- [A Note on the Bending Moment Induced in the Booms of a Spar...][research_winny_1950]
- [PRELIMINARY WING WEIGHT DETERMINATION][research_peck_hudson_1956]
- [Reduction of Bending Moment at the Root of a Rotor Blade][research_vanleeuwen_1960]
- [Transfer of Bending Moment Between Flat Plate Floor and Column][research_transfer_of_1960]
- [Creep of a solid metallic bar or thick-walled tube of...][research_johnson_henderson_1962]
- [A segmented wing test technique for obtaining spanwise load...][research_wasson_mehus_1967]
- [Calculations of the bending moment required for the cold...][research_lukyanov_1968]
- [Effective Flange Breadth of Stiffened Plates Under Axial...][research_mansour_1970]
- [Efficient Methods for Second Order Response Statistics to...][research_wan_1974]
- [Load-bearing ability of thick-walled pipelines under the...][research_sergiev_gusev_1979]
- [Generalized Design of Columns Subjected to Combined Axial...][research_monasa_snyder_1981]
- [Bending Moment in Walls of Grouped Silos Due to Structural...][research_bending_moment_1992]
- [Bending moment-mean curvature relationship with constant...][research_creazza_dimarco_1993]
- [Limit load analysis and safety assessment of an elbow with a...][research_chattopadhyay_dutta_1995]

### The Flight Control System

**A thirty-five percent negative static margin is a statement about time.**

The unstable airframe's pitch response splits into two real roots, one of them positive, and the positive
root sets how long the aircraft takes to double a disturbance. Neglecting pitch damping, which errs toward
less available time rather than more,

$$ M_\alpha = \frac{q\,S\,\bar{c}\,C_{m_\alpha}}{I_{yy}}, \qquad t_2 = \frac{\ln 2}{\sqrt{M_\alpha}} $$

The lift-curve slope in the table below is not quoted anywhere in the record and is estimated from the
planform by the standard low-aspect-ratio relation, which follows [Etkin][book_etkin] and
[Stevens and Lewis][book_stevens_lewis].

$$ C_{L_\alpha} = \frac{2\pi A}{2 + \sqrt{\dfrac{A^2\beta^2}{\eta^2}\left(1 + \dfrac{\tan^2\Lambda_{c/2}}{\beta^2}\right) + 4}}, \qquad \beta^2 = 1 - M^2 $$

At Mach 0.9 that returns 5.037 per radian, and the pitching moment derivative follows from the static
margin.

$$ C_{m_\alpha} = -C_{L_\alpha}\,\mathrm{SM} = -5.037 \times (-0.35) = 1.763 $$

**A positive pitching moment derivative is the whole of the aircraft's difficulty**, because it means a
disturbance in angle of attack produces a moment that increases it.

with $C_{m_\alpha} = -C_{L_\alpha} \cdot \mathrm{SM}$, so that a negative static margin makes the pitching
moment derivative positive and the root real.

**The pitch inertia was never published and is assumed**, bracketed between 35,000 and 60,000 slug square
feet, which spans the range for aircraft of this size and mass. Every figure below carries that assumption.

| Mach | Altitude, ft | $q$, lb/ft² | $t_2$, ms | Frames at 40 Hz |
|---|---|---|---|---|
| 0.4 | 40,000 | 43.9 | 596 | 23.8 |
| 0.4 | 20,000 | 108.9 | 378 | 15.1 |
| 0.4 | 0 | 237.0 | 256 | 10.2 |
| 0.6 | 20,000 | 245.1 | 244 | 9.8 |
| 0.6 | 0 | 533.3 | 166 | 6.6 |
| 0.8 | 20,000 | 435.7 | 173 | 6.9 |
| 0.8 | 0 | 948.0 | 118 | 4.7 |
| 0.9 | 20,000 | 551.4 | 148 | 5.9 |
| 0.9 | 0 | 1,199.8 | 100 | 4.0 |

**At the corner of the envelope the aircraft doubles a pitch disturbance in a tenth of a second**, and at
the low inertia bracket in 76 milliseconds. **The controller gets four frames in which to notice and act**,
and at the low bracket rather closer to three.

- [Lift-Curve Slope for Swept and Unswept Wings][research_bouton_1950]
- [Lift‐Curve Slope at Subsonic and Supersonic Speeds][research_stanbrook_1954]
- [Lift-Curve Slope and Induced Drag Factors of Large Aspect...][research_nonweiler_1960]
- [Aerodynamic features of the flap-balanced swivel-airfoil...][research_glbbings_1969]
- [USAF United States Air Force Stability and Control DATCOM...][research_finck_1978]
- [Calculation of lift-curve slope using a wing tip biased...][research_lowe_1988]
- [Missile DATCOM. Volume 1][research_vukelich_stoy_1988_b]
- [Missile Datcom. Volume 2. User's Manual][research_vukelich_stoy_1988]
- [Lift-curve slope for finite-aspect-ratio wings][research_laitone_1989]
- [Missile Datcom User's Manual. Revision, 6/93][research_burns_deters_1993]
- [Missile Datcom User's Manual - 2008 Revision][research_auman_doyle_2008]
- [MISSILE DATCOM User's Manual - 2011 Revision][research_rosema_doyle_2011]
- [MISSILE DATA COMPENDIUM DATCOM User Manual 2014 Revision][research_rosema_doyle_2014]

### Two Doubling Times, and Confusing Them Looks Like a Finding

The figure above is the doubling time of an established exponential. A disturbance released from rest with
zero pitch rate does not follow an exponential, because both roots are excited, and the response is a
hyperbolic cosine.

$$ \alpha(t) = \alpha_0 \cosh\left(\lambda t\right), \qquad \lambda = \sqrt{M_\alpha} = 6.931\ \mathrm{s^{-1}} $$

The two doubling times therefore differ by a fixed factor.

$$ t_2^{\exp} = \frac{\ln 2}{\lambda} = 0.100\ \mathrm{s}, \qquad t_2^{\cosh} = \frac{\operatorname{arcosh} 2}{\lambda} = 0.190\ \mathrm{s} $$

$$ \frac{t_2^{\cosh}}{t_2^{\exp}} = \frac{\operatorname{arcosh} 2}{\ln 2} = 1.900 $$

**A factor of 1.900 is large enough to read as a real discrepancy if the two are mixed up**, and this
article uses the exponential figure throughout, which is the conservative one.

That number should be set against the delay the controller itself introduces. A zero-order hold contributes
half a sample on average and the computation contributes whole frames, so

$$ \tau_{\mathrm{eff}} = \frac{0.5 + n_{\mathrm{compute}}}{f_s} = \frac{1.5}{40\ \mathrm{Hz}} = 37.5\ \mathrm{ms} $$

The same rate sets a ceiling on what the loop can see at all, and a lag that grows with frequency.

$$ f_{\mathrm{Nyquist}} = \frac{f_s}{2} = 20\ \mathrm{Hz} $$

$$ \varphi = 360^\circ f \tau_{\mathrm{eff}} $$

| Frequency | Phase lag from 37.5 ms |
|---|---|
| 0.5 Hz | 6.75° |
| 1.0 Hz | 13.50° |
| 2.0 Hz | 27.00° |
| 5.0 Hz | 67.50° |

**Thirty-seven and a half milliseconds of the aircraft's hundred-millisecond doubling time is consumed by the act of sampling.**
That is the argument for forty hertz stated as a ratio rather than as a specification, and it explains why
the update rate is quoted in the primary literature as though it were a design feature rather than an
implementation detail. **It was a design feature.**

- [SOME BASIC CONSIDERATIONS REGARDING THE LONGITUDINAL DYNAMICS...][research_curtiss_howardc_1961]
- [An Analytical Investigation of Short-Period Flying Qualities][research_giles_1972]
- [Use of short period frequency requirements in horizontal tail...][research_moorhouse_jenkins_1975]
- [The definition of short-period flying qualities...][research_bischoff_1983]

- [Sampled-Data Control Systems][research_m_jury_1959]
- [Sampling schemes in sampled-data control systems][research_sampling_schemes_1961]
- [Stability of nonlinear sampled-data control systems][research_kodama_1962]
- [A note on sampled-data control systems][research_phillips_1965]
- [Lyapunov design of time-shared sampled-data control systems†][research_weissenberger_1969]
- [Optimal design of sampled-data control systems by linear...][research_raghavan_1971]
- [Optimum design of linear multivariate sampled-data control...][research_yahagi_1971]
- [Abtastregelung Sampled Data Control][research_ackermann_isermann_1973]
- [Linear sampled-data control systems with distributed...][research_zenisek_1973]
- [Design Principles for Digital Autopilot Synthesis][research_berman_gran_1974]
- [Robust stability for sampled-data control systems][research_bernstein_hollot_1989]
- [Sampled-data control for time-delayed plants][research_lennartson_1989]
- [2 optimal control for sampled-data systems][research_khargonekar_sivashankar_1991]
- [Dynamics and Robust Control of Sampled Data Systems for Large...][research_bainum_ericsson_1992]
- [Robust sampled-data control][research_ocali_sezer_1992]
- [044 Finite worldlength control of sampled data systems by...][research_044_finite_1994]
- [057 H∞ control design for a class of uncertain sampled-data...][research_057_h_1994]
- [130 Sampled-data decentralized controller design][research_130_sampled_data_1994]
- [185 A fourier series lifting approach to H∞ sampled data...][research_185_a_1994]
- [Control of asynchronous sampled data systems][research_voulgaris_1994]
- [PC implementation of optimal sampled-data control for robotic...][research_pc_implementation_1994]
- [A hybrid adaptive control scheme using sampled data and...][research_a_hybrid_1995]
- [Robust Optimal Digital Control of Uncertain Multi-Rate...][research_shieh_chen_1998]
- [Sampled-Data Modeling and Analysis of PWM DC-DC Converters...][research_fang_abed_1998]

### Redundancy, Measured Against the Same Clock

Triplex redundancy with majority voting tolerates one channel failure. The probability that fewer than two
of three independent channels survive follows the binomial.

$$ P_{\mathrm{loss}} = \sum_{k=0}^{1} \binom{3}{k}(1-p)^k p^{3-k} $$

| Per-channel failure probability | Triplex loss | Simplex loss | Improvement |
|---|---|---|---|
| 10⁻³ | 3.00 × 10⁻⁶ | 10⁻³ | 334 |
| 10⁻⁴ | 3.00 × 10⁻⁸ | 10⁻⁴ | 3,334 |
| 10⁻⁵ | 3.00 × 10⁻¹⁰ | 10⁻⁵ | 33,334 |

**That is the easy half of the redundancy argument and it is not the binding one.** Voting requires
detecting and isolating a failed channel, and that takes frames, which the airframe does not have many of.

$$ \frac{\Delta t_{\mathrm{isolate}}}{t_2} = \frac{n_{\mathrm{frames}}/f_s}{t_2} $$

| Frames to isolate | Fraction of a doubling time consumed |
|---|---|
| 1 | 25.0 percent |
| 2 | 50.0 percent |
| 3 | 75.0 percent |
| 5 | 125.0 percent |

**A voter that needs five frames to isolate a failure has spent more than one doubling time doing it**, by
which point the disturbance it was protecting against has grown beyond the authority available to correct
it. **Redundancy management on this aircraft was a real-time problem rather than a reliability problem**,
and that inversion is one of the genuinely transferable results of the programme.

The system carried three flight modes, the **normal digital** mode as prime, with **digital reversion** and
**analog reversion** below it, each having an up-and-away and a power-approach configuration, and extensive
gain scheduling in every mode except the two reversionary power-approach cases.

- [Part Three Flight Control System][research_fearnside_1962]
- [A REDUNDANCY TECHNIQUE FOR IMPROVING THE RELIABILITY OF...][research_knoxseith_1963]
- [Hybrid digital analog pulse-time techniques for flight...][research_seegmiller_1963]
- [Reliability Improvement of Digital Communication using...][research_kurz_1963]
- [Error Control through Coding. Volume 3 - Variable Redundancy...][research_chien_tang_1964]
- [FLIGHT CONTROL SYSTEM INVESTIGATION OF BEARING RETENTION BY...][research_spiker_1964]
- [THE X-20 FLIGHT CONTROL SYSTEM DEVELOPMENT][research_mcdonald_farris_1964]
- [Fly-by-Wire Flight Control System Experience with a...][research_jarviscr_1967]
- [The Concorde Automatic Flight Control System][research_wolfe_1967]
- [Automatic flight control system for automatic...][research_krachmalnick_vetsch_1968]
- [Application of an approximate time delay to a Posicast...][research_shields_cook_1971]
- [Concorde Automatic Flight Control System][research_concorde_automatic_1971]
- [Survivable Flight Control System. Studies, Analyses and...][research_kisslinger_wendl_1971]
- [Integrity of flight control system design][research_mant_1972]
- [Cully and Boller 1973][research_cully_boller_1973]
- [Hardware integration and improved operation of the flight...][research_clews_1973]
- [Development of the F-12 Aircraft Flight Control System][research_mcmaster_schenk_1974]
- [Digital Flight Control System Redundancy Study][research_mcgough_moses_1974]
- [Digital Flight Control System for Tactical Fighter. Volume 1...][research_konar_mahesh_1974]
- [Management of analytical redundancy in digital flight control...][research_montgomeryrc_pricedb_1974]
- [Three-Axis Fluidic/Electronic Automatic Flight Control System...][research_cotton_1974]
- [An overview of NASA's digital fly-by-wire technology...][research_jarviscr_1975]
- [Apu/hydraulic/actuator Subsystem Computer Simulation. Space...][research_apu_hydraulic_actuator_subsystem_1975]
- [Description and Flight Test Results of the NASA F-8 Digital...][research_description_and_1975]
- [Design and development experience with a digital fly-by-wire...][research_deetsda_1975]
- [Flight Control System Reliability and Maintainability...][research_zipperer_jenney_1975]
- [Flight Control System Reliability and Maintainability...][research_zipperer_jenney_1975_b]
- [Flight test experience with the F-8 digital fly-by-wire system][research_szalaikj_1975]
- [Fly-by-wire and control configured vehicles rewards and risks][research_burns_1975]
- [Mechanization of and experience with a triplex fly-by-wire...][research_lockwp_petersenwr_1975]
- [Space Shuttle flight control system][research_klinarwj_kubiaket_1975]
- [Compass Cope Flight Control System Redundancy Study][research_tribuno_klein_1976]
- [Design and test experience with a triply redundant digital...][research_szalaikj_fellemanpg_1976]
- [Development of an active fly-by-wire flight control system][research_andersonca_1976]
- [Digital flight control for the NASA 737 airplane][research_malcomlg_husbandjh_1976]
- [Failure Accommodation in Digital Flight Control Systems...][research_montgomery_price_1976]
- [Failure Accommodation in Digital Flight Control Systems by...][research_montgomery_caglayan_1976]
- [Flight test experience with the F-8 digital fly-by-wire system][research_szalaikj_1976]
- [NASA's Advanced Control Law Program for the F-8 Digital...][research_jarrellrelliott_1976]
- [Reconfigurable redundancy management for aircraft flight...][research_boschja_kuehlwj_1976]
- [Flight experience with a fail-operational digital fly-by-wire...][research_brownsr_szalaikj_1977]
- [Heavy Lift Helicopter Flight Control System. Volume 1...][research_niven_1977]
- [Heavy Lift Helicopter Flight Control System. Volume III...][research_davis_garnett_1977]
- [NASA's Advanced Control Law Program for the F-8 Digital...][research_jelliott_1977]
- [Optimal control of a linear system with time delay in the...][research_plyako_1977]
- [Redundant integrated flight control/navigation inertial...][research_ebnerre_markjg_1977]
- [Validation of MIL-F-9490D - General Specification for Flight...][research_dobosbubno_hartsook_1977]
- [Analysis of Digital Flight Control Systems with Flying...][research_whitbeck_hofmann_1978]
- [Digital Fly-By-Wire Flight Control Validation Experience][research_szalaikj_jarviscr_1978]
- [Direct Drive Control Valve for Fly-by-Wire Flight Control...][research_hogan_rinde_1978]
- [Flight Control System FRG 70 D Realization and Testing…][research_drtil_schulz_1978]
- [Modeling and parameter uncertainties for aircraft flight...][research_rickardww_1978]
- [The effect of prefilter design on sample rate selection in...][research_peledu_powelljd_1978]
- [Minimization of Time Delay Sensitivity of Time Delay Control...][research_rohella_chatterjee_1979]
- [Optimal Output Feedback Control Law for Time Delay System...][research_mohanty_chhotaray_1979]
- [Program for the Critical Components of a Fly-by-Tube Backup...][research_posingies_1979]
- [Stability of a system with variable time delay][research_hirai_satoh_1980]
- [Ground and flight test experience with a triple redundant...][research_jarviscr_szalaikj_1981]
- [Reliability analysis of the F-8 digital fly-by-wire system][research_brockld_goodmanha_1981]
- [Advanced Flight Control Actuation System AFCAS - E/P...][research_kineyko_1982]
- [Analytical Control Law for Desirable Aircraft Lateral...][research_ohta_nikiforuk_1982]
- [Flight Test of a G. E. and DCI Direct Drive Fly-By-Wire...][research_jenney_schreadley_1982]
- [Compensation for time delay in flight simulator...][research_cranedf_1983]
- [Simulation of a digital aircraft flight control system][research_stirling_1983]
- [Strict Redundancy Schemes for Non-Sequential Detector...][research_weinert_meyer_1984]
- [The effects of time delay in man-machine control systems...][research_cranedf_1984]
- [A model reference adaptive control system for a class of...][research_ohkawa_1985]
- [Computer Aided Design of Aircraft Flight Control System][research_vukobratovic_stojic_1985]
- [Investigation of an advanced fault tolerant integrated...][research_dunnwr_cottrelld_1986]
- [Model reference adaptive control system for discrete linear...][research_ohkawa_1986]
- [Prototype Digital Flight Control Computer][research_prototype_digital_1986]
- [AFTI/F-111 MAW flight control system and redundancy...][research_larsonrichardr_1987]
- [Aircraft automatic flight control system with model inversion][research_smith_meyer_1987]
- [A Dexterity Measure for the Kinematic Control of Robot...][research_chang_1988]
- [Aircraft Flight Control System Identification][research_mulder_1988]
- [Interaction of feel system and flight control system dynamics...][research_baileyrandalle_powersbruceg_1988]
- [Flight control system design for an in-flight simulator][research_henschel_chetty_1989]
- [Flight control system design factors for applying automated...][research_sitzjoelr_vernontoddh_1990]
- [High accuracy control of water temperature system with time...][research_nakamura_takesue_1990]
- [Interaction of feel system and flight control system dynamics...][research_baileyre_knottslh_1990]
- [Aircraft Flight Control System Design Concepts][research_smith_1991]
- [Performance improvements of an F-15 airplane with an...][research_myers_walsh_1991]
- [Adaptive Control for Non-Minimum Phase System with Time Delay...][research_miyasato_1992]
- [Voting software for fault-tolerant aircraft flight control...][research_voting_software_1993]
- [214 Application of restructurable flight control system to an...][research_214_application_1994]
- [An experimental study on the position control of an...][research_chin_lee_1994]
- [Flight control system mode transitions influence on handling...][research_reid_rajagopal_1994]
- [Application of restructurable flight control system to large...][research_ochi_kanai_1995]
- [Design of discrete-time adaptive control in presence of...][research_design_of_1995]
- [Flight Control Computer Development Through Application of...][research_gill_1995]
- [Parameter-robust flight control system for a flexible aircraft][research_kubica_livet_1995]
- [Closed-Loop System Identification Experience for Flight...][research_murphypatrickc_1996]
- [Tailless Aircraft Control Allocation][research_buffington_1997]
- [Application of Robust Control and Gain Scheduling to Missile...][research_bullock_fields_1998]
- [Integrated Electric Actuator Application to Flight Control...][research_hammer_bright_1998]
- [Closed-Loop System Identification Experience for Flight...][research_patrickcmurphy_1999]
- [Modular Control Law Design for the Innovative Control...][research_buffington_1999_b]
- [Constrained Control Allocation Methods for Reconfigurable...][research_bodson_2000]
- [Restoring Redundancy to the MAP Propulsion System][research_odonnelljamesrjr_davisgaryt_2002]
- [YF22 Model With On-Board On-Line Learning...][research_napolitano_2002]
- [Estimation, Control, and Redundancy Management for Uncertain...][research_speyer_2003]
- [A Control Allocation Technique to Recover From Pilot-Induced...][research_yildizyildiray_kolmanovskyilyav_2010]
- [Structural Technology Evaluation and Analysis Program STEAP...][research_mahulkar_2010]
- [A Control Allocation System for Automatic Detection and...][research_yildizyidiray_kolmanovskyilyav_2011]

- [Longitudinal Stability][research_crowe_1937]
- [A Theoretical Investigation of Longitudinal Stability of...][research_greenbergharry_sternfieldleonard_1944]
- [Control Surfaces - Elevator Hinge Bracket - Sta. 27 - Static...][research_wright_1945]
- [Control Surfaces - Elevator Rib - Outboard of 372 - Static...][research_riefe_1946]
- [Correlation of the Trim Limits of Stability Obtained for a...][research_garrisoncharliec_hacskayloandrew_1947]
- [Dynamic Longitudinal Stability and Control Flight Tests of a...][research_cornellaeronauticallabincbuffalony_1947]
- [Measurements of the Longitudinal Stability and Control and...][research_kraftchristophercjr_reederjp_1948]
- [Systematic model researches on the stability limits of the...][research_sottorfw_1949]
- [Two-Dimensional Simulation of the Automatic Aircraft...][research_paine_1950]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]
- [Static Stability Wind-Tunnel Test of 18, 22, and 26 Caliber...][research_chaplin_1953]
- [TANDEM HELICOPTER LONGITUDINAL STABILITY AND CONTROL][research_gebhard_1953]
- [THE EFFECT OF VISCOUS AND ELASTIC CONTROL SYSTEM RESTRAINTS...][research_mccaskill_1953]
- [A complete system for the flight-testing of piloted aircraft][research_vandoren_1955]
- [STATIC STABILITY AND MAGNUS CHARACTERISTICS OF THE 5-INCH...][research_greene_1955]
- [AUTOMATIC FLIGHT CONTROL SYSTEMS FOR PILOTED AIRCRAFT][research_hart_1956]
- [DUCTED PROPELLER ASSAULT TRANSPORT. STABILITY AND CONTROL][research_vollo_brassaw_1956]
- [STABILITY ANALYSES OF FLYING PLATFORM IN HOVERING AND FORWARD...][research_albachten_1956]
- [STATIC STABILITY AND MAGNUS CHARACTERISTICS OF A LOW-DRAG...][research_greene_1956]
- [Tandem Helicopter Lateral Stability and Control][research_seckel_graziani_1956]
- [Aeroelasticity in Stability and Control][research_reajbcoincsantamonicaca_1957]
- [HYDRODYNAMIC DESIGN CRITERIA FOR ADEQUATE TORPEDO STABILITY...][research_sweat_1958]
- [STATIC AND DYNAMIC STABILITY TESTS OF A PROPOSED VERSION OF...][research_shantz_demeritte_1958]
- [Effect of Artificial Pitch Damping on the Longitudinal and...][research_moulmartint_brownlawrencew_1959]
- [The Present Status of Aircraft Stability Problems in the...][research_taylor_1959]
- [STABILITY AND CONTROL CHARACTERISTICS OF SEVEN LENTICULAR...][research_anderson_1960]
- [STATIC STABILITY AND DRAG OF THE HOPI WEAPON][research_carroll_1960]
- [Static stability and control characteristics of two...][research_fosswejr_whitcombcf_1960]
- [A Note on the Effect of a Time-Varying Forward Flight...][research_swaim_1961]
- [A Study of Longitudinal Control Problems at Low and Negative...][research_sadoffmelvin_mcfaddennormanm_1961]
- [AN INVESTIGATION OF THE EFFECTS OF INDUCED NONSYMMETRIC...][research_boatwright_1961]
- [Effects of Control-Feel Configuration on Airplane...][research_craneharoldl_sommerrobertw_1961]
- [INVESTIGATION OF STATIC STABILITY AND AERODYNAMIC EFFECTS OF...][research_anderson_1961]
- [AUTOMATIC CONTROL OF STATIC ELECTRICITY FOR ARMY HELICOPTERS][research_tona_1962]
- [HYDRODYNAMICS AND STABILITY AND CONTROL OF A TANDEM PROPELLER...][research_clark_dellamico_1962]
- [MINUTEMAN WING I ENVIRONMENTAL CONTROL SYSTEM RELIABILITY...][research_gearhart_1962]
- [SIMPLIFIED ANALYSIS OF FLEXIBLE BOOSTER FLIGHT CONTROL SYSTEMS][research_hofmann_kezer_1962]
- [A GAMMA GUIDANCE SYSTEM FOR HELICOPTER FLIGHT-FORMATION...][research_wilcox_1963]
- [AIR FORCE FLIGHT CONTROL AND FLIGHT DISPLAY INTEGRATION...][research_gainer_1963]
- [DESIGN AND DEVELOPMENT OF A FLIGHT PATH CONTROL SYSTEM FOR...][research_ostheimer_giguere_1963]
- [EXPERIMENTS ON CYLINDER DRAG, SPHERE DRAG AND STABILITY IN...][research_kohlman_1963]
- [STATIC STABILITY TESTS ON A 0.098 SCALE STANDARD LAUNCH...][research_ziegler_1963]
- [THE EFFECT OF NONLINEAR STATIC COUPLING ON THE MOTION...][research_kinney_1963]
- [A GENERAL INVESTIGATION OF HYPERSONIC STABILITY AND CONTROL...][research_flightscienceslabincbuffalony_1964]
- [A forced-oscillation method for dynamic- stability testing][research_kilgore_averett_1964]
- [AN ANALYSIS OF TERMINAL FLIGHT PATH CONTROL IN CARRIER LANDING][research_durand_teper_1964]
- [ESTIMATION OF STABILITY DERIVATIVES AND INDICES OF VARIOUS...][research_jacobs_1964]
- [INVESTIGATION OF THE CONCEPT OF DIRECT FLIGHT CONTROL][research_craig_1965]
- [LIFT, DRAG, AND STATIC STABILITY OF A BLUNT CONICAL MODEL IN...][research_boylan_1965]
- [RESEARCH ON ACCELERATED RELIABILITY TESTING METHODS...][research_johnson_1965]
- [UH-2 JET-AUGMENTED HIGH-SPEED RESEARCH HELICOPTER...][research_blackburn_whitfield_1965]
- [AN ANALYTICAL STUDY OF FACTORS INFLUENCING THE LONGITUDINAL...][research_beppu_curtiss_1966]
- [COMPUTER ANALYSIS OF FORKLIFT TRUCK STABILITY WHEN OPERATING...][research_deninno_uherka_1966]
- [SIMPLIFIED SWITCHING FUNCTIONS FOR TIME-OPTIMAL CONTROL...][research_schmeichel_1967]
- [SPACE VEHICLE NAVIGATION, GUIDANCE, AND CONTROL][research_langston_1967]
- [STABILITY AND CONTROL HANDBOOK FOR HELICOPTERS][research_kisielowski_perlmutter_1967]
- [BOATTAIL EFFECTS ON STATIC STABILITY AT SMALL ANGLES OF ATTACK][research_washington_pettis_1968]
- [Investigation of tilt-rotor VTOL aircraft rotorpylon stability][research_edenborough_1968]
- [STATIC, FREE VIBRATION, AND STABILITY ANALYSIS OF THIN...][research_kalnins_1968]
- [Stability of the steady state cycle of a power reactor in...][research_postnikov_sabaev_1968]
- [TIME OPTIMAL CONTROL FOR A CLASS OF COMMON RANDOM DISTURBANCES][research_smith_1968]
- [TIME-OPTIMAL ATTITUDE CONTROL OF AN AXIALLY SYMMETRIC...][research_dedoes_1969]
- [An In-Flight Investigation to Develop Control System Design...][research_neal_smith_1970]
- [Feedback Control of VTOL Aircraft][research_dukes_1970]
- [An In-Flight Investigation of Bank-Angle Control Parameters...][research_hall_1971]
- [An improved estimate for the error in the classical, linear...][research_simmonds_1971]
- [Conceptual Study to Apply Advanced Flight Control Technology...][research_smith_hammer_1971]
- [Study to Determine the Application of Aircraft...][research_drummond_1971]
- [Formulations of the Equations of Motion of an Elastic...][research_schwanz_1972]
- [Ride Quality Design Criteria for Aircraft with Active Mode...][research_rustenburg_1972]
- [Stability of a laminated anisotropic circular plate][research_tang_1972]
- [Surface Effect Take-Off and Landing System SETOLS Subsonic...][research_davidson_hd_1972]
- [A parametric study of planform and aeroelastic effects on...][research_roskamj_lanc_1973]
- [Control System Design Considerations for a Longitudinally...][research_tomlinson_1973]
- [Effect of Various External Stores on the Static Longitudinal...][research_whoric_1973]
- [Euler-Lagrange conditions and estimation of states for a...][research_shah_desai_1973]
- [Flight Investigation of Various Longitudinal Short-Term...][research_smith_lebacqz_1973]
- [Pilot Control of Shuttle Orbiter during Approach and Landing][research_streb_1973]
- [STOL Tactical Aircraft Investigation, Externally Blown Flap...][research_okumoto_elsanker_1973]
- [STOL Tactical Aircraft Investigation. Volume V. Part I...][research_crandall_maund_1973]
- [Combined flight control/utility system][research_combined_flight_1974]
- [Effect of Upper-Surface Blowing on Static Longitudinal...][research_coe_kulla_1974]
- [Active Shimmy Control System][research_gamon_mahone_1975]
- [Advanced Integrated Aircraft Displays and Augmented Flight...][research_roscoe_eisele_1975]
- [Digital Adaptive Model following Flight Control][research_alag_kaufman_1975]
- [Experimental Static Stability Studies of Several Tactical...][research_lindsay_jordan_1975]
- [Forced-Oscillation Test Mechanism for Measuring...][research_burt_1975]
- [Systematic Design of Modular Estimators for Aircraft...][research_center_1975]
- [The Generalized Trajectory Simulation System. Volume 5...][research_debilzan_1975]
- [“Optimal Control of a Maglev Vehicle”∗][research_gottzein_cramer_1975]
- [Advanced control technology and its potential for future...][research_hermanarediess_1976]
- [Aeroelastic Rotor Stability Analysis][research_johnston_cassarino_1976]
- [Design of a control configured tanker aircraft][research_walkersa_1976]
- [Development of Design and Manufacturing Technology for...][research_aker_alukonis_1976]
- [Digital Electronic Propulsion Control System Problems and...][research_kuhlberg_newirth_1976]
- [Engine Evaluation of Advanced Technology Control Components][research_morrison_white_1976]
- [Experimental Results from a Static Stability and Pressure...][research_lindsay_fikes_1976]
- [On Stability of Free-Free Beams with and without Directional...][research_wu_1976]
- [Static Stability Characteristics of the MK-82/84...][research_paulk_anderson_1976]
- [A failure effects simulation of a low authority flight...][research_corlissld_talbotpd_1977]
- [A new concept of static stability and its flight testing in...][research_sachs_1977]
- [Aeroelastic Stability of the 747/0rbiter][research_reding_ericsson_1977]
- [An Unstable Dynamical System Associated with Model Reference...][research_feuer_barmish_1977]
- [Control and Suppression of Swirling and Secondary Flows in...][research_nagib_wigeland_1977]
- [Lateral equilibrium of asymmetrical swept wings - Aileron...][research_weisshaar_1977]
- [Stability of the pilot-aircraft system in maneuvering flight][research_broussard_stengel_1977]
- [Static Stability and Drag Effects of Various External Store...][research_whoric_1977]
- [The Evaluation of a Digital Hardware Voter/Monitor in an...][research_schreadley_1977]
- [The Study of Distributive Parameter Systems for Flight Control][research_lee_1977]
- [Aeroelastic Stability Characteristics of an Oblique-Wing...][research_crittenden_weishaar_1978]
- [Applicability of the control configured design approach to...][research_heplerak_zeckh_1978]
- [Comment on "Aeroelastic Stability Characteristics of an...][research_hitch_1978]
- [Detection, Estimation and Control on Group Manifolds][research_lo_1978]
- [Estimate of Orbiter Static Aeroelasticity Properties via...][research_cavin_holyoak_1978]
- [Flight Evaluation of Flight-Path Control for the STQL...][research_franklin_innis_1978]
- [Flight Verification of the Advanced Flight Control Actuation...][research_demarchi_haning_1978]
- [Flight-determined stability and control coefficients of the...][research_iliffkw_mainere_1978]
- [Ordinary Differential Equations Oscillation and Stability...][research_leighton_1978]
- [Studies in Optimal Control, Estimation and Linear Systems...][research_smith_1978]
- [Aeroelastic Stability Analysis of the AD-1 Manned...][research_rutkowski_1979]
- [An Adaptive Control for Vehicle Suspensions][research_sachs_1979]
- [An Extension of Engine Weight Estimation Techniques to...][research_onat_tolle_1979]
- [Computational Issues in Linear Least-Squares Estimation and...][research_newkirk_1979]
- [Design Criteria for Dry Lubricated Flight Control Bearings][research_nagy_1979]
- [Design Criteria for Optimal Flight Control Systems][research_govindaraj_rynaski_1979]
- [Detection, Estimation, and Control on Group Manifolds][research_lo_1979]
- [Entrophy Analysis of Feedback Flight Dynamic Control Systems][research_weidemann_leondes_1979]
- [Maintenance Training System 6883 Converter/Flight Control...][research_baum_clark_1979]
- [A Variable Free Control Characteristic Vehicle][research_dorey_good_1980]
- [Design and Test of a Hydra-Optic Flight Control Actuation...][research_kohnhorst_magnacca_1980]
- [Detection, Estimation, and Control on Group Manifolds][research_lo_1980]
- [Estimation of the Failure Rate. A Survey of Nonparametric...][research_singpurwalla_wong_1980]
- [Experience with an adaptive stick-gain algorithm to reduce...][research_powersbg_1980]
- [Research in Advanced Flight Control Design][research_horowitz_golubev_1980]
- [Roll Resonance Control of Angle of Attack for Reentry Vehicle...][research_platus_1980]
- [Stability of Two-Step Methods for Variable Integration Steps][research_linigier_dahlquist_1980]
- [Stability of the Boundary Layer on a Swept Wing with Wall...][research_lekoudis_1980]
- [A Model-Following Technique for Insensitive Aircraft Control...][research_nield_iv_1981]
- [Advanced Aircraft Electrical System Control Technology...][research_dunn_leong_1981]
- [Detection, Estimation, and Control on Group Manifolds][research_lo_1981]
- [Mathematical Software for Linear Control and Estimation Theory][research_klema_1981]
- [Selected stability and control derivatives from the first...][research_iliffkw_mainere_1981]
- [The Stability of Pseudospectral-Chebyshev Methods][research_gottlieb_1981]
- [Transient Response Test Procedures for Measuring Vehicle...][research_verma_1981]
- [Criteria for Side-Force Control in Air-to-Ground Target...][research_sammondsroberti_mcneillwaltere_1982]
- [In-Flight Evaluation of Control System Pure Time Delays][research_berry_powers_1982]
- [A Study of Digitally Controlled Flight Control Actuation][research_belmont_1983]
- [Equivalent angle-of-attack method for estimating nonlinear...][research_hemsch_nielsen_1983]
- [Experimental Study of Active Vibration Control][research_hallauer_jr_1983]
- [Stability of Two‐Bladed Aeroelastic Rotors on Flexible...][research_chen_1983]
- [A Digital Linear Position Sensor for Flight Control Actuation][research_jenney_schreadley_1984]
- [Analysis of Aircraft Attitude Control Systems Prone to...][research_hess_1984]
- [Asymptotic Methods for the Analysis, Estimation, and Control...][research_willsky_1984]
- [Status Report on Asymptotic Methods for the Analysis...][research_willsky_verghese_1984]
- [Theater of Operations Dental Work Load Estimation][research_king_brunner_1984]
- [Asymptotic Methods for the Analysis, Estimation, and Control...][research_willsky_verghese_1985]
- [Estimation of Steady-State Central Moments by the...][research_glynn_iglehart_1985]
- [Flight evaluation of a digital electronic engine control in...][research_burcham_myers_1985]
- [Mathematical Problems in Stability, Control and Reliability...][research_rosenkrantz_1985]
- [Stochastic Adaptive Control and Estimation Enhancement][research_barshalom_1985]
- [A perspective on superaugmented flight control - Advantages...][research_mcruerd_johnstond_1986]
- [Aircraft Battery State of Charge and Charge Control System][research_viswanathan_charkey_1986]
- [An Application of a LISP Based Expert System for Failure...][research_loh_1986]
- [Calculating Aerodynamic-Stability Derivatives][research_lance_1986]
- [Department Of The Air Force Washington Dc 1986][research_departmentoftheairforcewashingtondc_1986]
- [Experimental Study of Flight Effect on Fan Noise 1st Report...][research_kobayashi_torisaki_1986]
- [A Survey of Aircraft Integrated Control Technology][research_hill_1987]
- [Adaptive Control of Vehicle Suspension][research_hac_1987]
- [Aeroelastic stability characteristics of a composite swept...][research_lottati_1987]
- [An analysis of a candidate control algorithm for a ride...][research_suikatreiner_donaldsonkent_1987]
- [Configuration Control Method of a Control Configured Robot...][research_fukuda_kobayashi_1987]
- [Derivative Arrays, Geometric Control Theory, and Realizations...][research_campbell_terrell_1987]
- [Space radiation effects on the dimensional stability of a...][research_space_radiation_1987]
- [Stability boundaries for command augmentation systems][research_shrivastavapc_1987]
- [Aircraft Battery State of Charge and Charge Control System][research_viswanathan_charkey_1988]
- [Approximations and Optimal Control for the Pathwise Average...][research_kushner_1988]
- [Computational Methods for Control and Estimation of...][research_banks_1988]
- [Cooperative synthesis of control and display augmentation for...][research_gargsanjay_schmidtdavidk_1988]
- [Influence of support oscillation in dynamic stability tests][research_beyers_1988]
- [Measured and predicted pressure distributions on the...][research_webblannied_mccainwilliame_1988]
- [OPTIMUM CONTROL OF A DRIVER/FOUR-WHEEI-TEERED-VEHICLE SYSTEM][research_hayashi_1988]
- [Static aeroelastic characteristics of circulation control...][research_haas_chopra_1988]
- [The importance of steady and dynamic inflow on the stability...][research_petersdavida_1988]
- [A knowledge-based system design/information tool for aircraft...][research_mackalldalea_allenjamesg_1989]
- [Adaptive control of a continuous-time system with...][research_nihtila_1989]
- [An instrument control and data analysis program configured...][research_roos_mushlin_1989]
- [Application of Intelligent Control of Time-Delay Processes to...][research_huiping_yutian_1989]
- [Modelling and Control for Nonlinear Time-Delay System Via...][research_zhou_ye_1989]
- [Results of a parametric aeroelastic stability analysis of a...][research_woodsjessicaa_gilbertmichaelg_1989]
- [SDI, Arms Control, and Stability Toward a New Synthesis][research_nitz_1989]
- [Short-range nonlinear feedback strategies for aircraft...][research_menon_1989]
- [Span-Ratio Analysis Used to Estimate Effective Lift Drag...][research_pennycuick_1989]
- [Stability boundaries for aircraft with unstable...][research_shrivastava_stengel_1989]
- [Stochastic Adaptive Control and Estimation Enhancement][research_barshalom_1989]
- [Aeroelastic stability of aircraft with circulation control...][research_haas_chopra_1990]
- [Eigenspace Design of Helicopter Flight Control Systems][research_garrard_low_1990]
- [Extended implicit model following as applied to integrated...][research_schmidtdavidk_schiermanjohnd_1990]
- [Integrated flight/propulsion control for supersonic STOVL...][research_franklinjamesa_stortzmichaelw_1990]
- [On Control Laws for Vehicle Suspensions Accounting for Input...][research_sharp_wilson_1990]
- [Parametric aeroelastic stability analysis of a generic X-wing...][research_woods_gilbert_1990]
- [Stability sensitivity studies for synthesis of aeroelastic...][research_lu_murthy_1990]
- [Static stability and control characteristics of scissor wing...][research_rokhsaz_selberg_1990]
- [Stochastic Adaptive Control and Estimation Enhancement][research_barshalom_1990]
- [A Control Configured Design Method and its Application to Car...][research_kawabe_tokumaru_1991]
- [A knowledge-based system design/information tool for aircraft...][research_mackalldalea_allenjamesg_1991]
- [Analysing manipulator and feel system effects in aircraft...][research_hess_1991]
- [Control configuration of a relaxed stability airship][research_nagabhushan_1991]
- [Fuzzy logic for control of roll and moment for a flexible...][research_fuzzy_logic_1991]
- [Numerical Methods for Closed-Loop Control][research_laub_1991]
- [Periodic Model‐Following for the Control‐Configured Helicopter][research_mckillip_1991]
- [Interface Protocol Requirements for Shipboard Damage Control...][research_tate_1992]
- [Optimal Linear Preview Control of Active Vehicle Suspension][research_hac_1992]
- [PHALANX CIWS Control System Stability, Aim Bias Compensation...][research_serakos_1992]
- [Piloted simulation evaluation of pitch control designs for...][research_engellandsa_franklinja_1992]
- [Aileron and sideslip-induced unsteady aerodynamic modeling...][research_singh_raisinghani_1993]
- [An Integrated MBS Modelling Environment for Vehicle Motion...][research_cherry_costa_1993]
- [Criteria for design of integrated flight/propulsion control...][research_franklinjamesa_1993]
- [Data acquisition and control system for the neutron...][research_wegener_dhooghe_1993]
- [Design Criteria for Integrated Flight/Propulsion Control...][research_jamesafranklin_1993]
- [Improvement of Vehicle Maneuverability by Direct Yaw Moment...][research_shibahata_shimada_1993]
- [Low bandwidth robust controllers for flight][research_biezaddanielj_chouhweilan_1993]
- [Modelling of Driver/Vehicle Directional Control System][research_guo_guan_1993]
- [Optimal Control of Four Wheel Steering Vehicle][research_higuchi_saitoh_1993]
- [Robust flight-path control system design with multiple-delay...][research_miyazawa_1993]
- [Robust stability of time-delay systems with an uncertain...][research_tsypkin_fu_1993]
- [Six-degree-of-freedom guidance and control-entry analysis of...][research_powellrichardw_1993]
- [Static aeroelastic control of an adaptive lifting surface][research_ehlers_weisshaar_1993]
- [The Variable Linear Transmission for Regenerative Damping in...][research_fodor_redfield_1993]
- [Tracking control of a free-ranging automatic guided vehicle][research_tracking_control_1993]
- [011 Intelligent vehicle active suspension control using fuzzy...][research_011_intelligent_1994]
- [017 Preview control of wheeled vehicle][research_017_preview_1994]
- [024 Automated vehicle control for IVHS systems][research_024_automated_1994]
- [025 Adaptive throttle control for automatic vehicle following][research_025_adaptive_1994]
- [053 Fuzzy logic control of an autonomous underwater vehicle][research_053_fuzzy_1994]
- [056 Neural networks in autonomous vehicle control][research_056_neural_1994]
- [196 Pointing control design for autonomous space vehicle...][research_196_pointing_1994]
- [A Reusability Study of Vehicle Lateral Control System][research_peng_zhang_1994]
- [A Stochastic Dynamic Model for Vehicle Headway Control in...][research_lu_1994]
- [Active Suspension With Preview Control][research_abdelhady_1994]
- [Control of Longitudinal and Lateral Platoon Using Sliding...][research_fujioka_suzuki_1994]
- [Crosswind Feedforward Control A Measure to Improve Vehicle...][research_tran_1994]
- [Digital model-reference flight control of aircraft with...][research_digital_model_reference_1994]
- [Direct solution of the aeroelastic stability equations][research_bismarcknasr_1994]
- [Discrete time optimal control of linear time‐delay systems][research_lee_sheu_1994]
- [Dual optimal control problems with time-delay][research_tsoutsinos_1994]
- [Fuzzy logic control for lateral vehicle guidance][research_fuzzy_logic_1994]
- [Predictive algorithm for the roll control autopilot of a jet...][research_kassapakis_warwick_1994]
- [Robust control of a nonlinear time-delay system][research_tharp_zhang_1994]
- [Software Productivity Consortium Herndon Va 1994][research_softwareproductivityconsortiumherndonva_1994]
- [Stochastic Adaptive Estimation and Control][research_marcus_1994]
- [Stochastic Control and Nonlinear Estimation][research_fleming_kushner_1994]
- [COMPUTING THE STATICS AND DYNAMICS OF AIRPLANE AILERON...][research_grossschmidt_pahapill_1995]
- [Improvement of Vehicle Dynamics by Rear Braking Force Control][research_morita_matsukawa_1995]
- [Numerical study of a supersonic open cavity flow and pressure...][research_jeng_payne_1995]
- [Review of the State of Development of Advanced Vehicle...][research_shladover_1995]
- [Thrust-Induced Effects on a Pitching-Up Delta Wing Flow Field...][research_vandommelen_1995]
- [Control of Transition in Swept-Wing Boundary Layers Using...][research_saric_1997]
- [Shelf-slope Stability Assessment from Multiresolution Wavelet...][research_weissel_1997]
- [DURIP 95 Instrumentation for Phase Modulation, Stability and...][research_warren_1998]
- [Including Aeroelastic Effects in the Calculation of X-33...][research_zeilerthomasa_1998]
- [Nonlinear Adaptive Flight Control with a Backstepping Design...][research_steinberg_page_1998]
- [Adaptive Filtering and Estimation for Control and Target...][research_gibson_1999]
- [Backup Attitude Control Algorithms for the MAP Spacecraft][research_odonnelljamesrjr_andrewsstephenf_1999]
- [Methods to Control Hazardous Airborne Dust][research_dyncorprestonva_1999]
- [Modular Control Design for the Innovative Control Effectors...][research_buffington_1999]
- [Nonlinear Control of Fighter Aircraft][research_wise_sedwick_1999]
- [Nonlinear Robust Control and Estimation][research_mceneaney_1999]
- [Robust Nonlinear Control of Tailless Aircraft][research_teel_1999_b]
- [Robust Nonlinear Control of Tailless Fighter Aircraft][research_teel_1999]
- [Active Stall Control Mutlistage Compression Systems][research_abed_2000]
- [Adaptive Algorithms for Active Noise and Vibration Control][research_bodson_2000_b]
- [Effects of Inadvertent UH-60 Cockpit Airbag System Deployment...][research_brozoski_johnson_2000]
- [Hybrid Active/Passive Control of Sound Radiation from Panels...][research_cabellrandolphh_gibbsgaryp_2000]
- [Intelligenct Flight Control of Uninhabited Aerial Vehicles][research_bernstein_2000]
- [Results From F-18B Stability and Control Parameter Estimation...][research_moestimothyr_noffzgregoryk_2000]
- [Smart Mesoflaps for Aeroelastic Transpiration for SBLI Flow...][research_loth_geubelle_2000]
- [Smart-Material Actuated Missile Flight Control Surfaces...][research_giurgiutiu_pomirleanu_2000]
- [A Distributed Active Vibration Absorber DAVA and Associated...][research_fuller_2001]
- [Smooth Sliding Mode Controller Design for Robust Missile...][research_shtessel_2001]
- [Vehicle Control Unit VCU for the HMMWV][research_californiaunivlosangeles_2001]
- [Air Force Flight Test Center Edwards Afb Ca 2002, AFFTC Instruction 99-5, Test and][research_airforceflighttestcenteredwardsafbca_2002_b]
- [Closed-Loop Control of Acoustic Tones in Aircraft Cavities][research_williams_2002]
- [Enabling-Dynamic Simulators Stability, Bifurcation and...][research_kevrekidis_2002]
- [Sliding Mode Control Applied to Reconfigurable Flight Control...][research_wells_2002]
- [Steering Control Compensation of Accelerating Vehicle Motion][research_burns_2002]
- [A Distributed Flight Software Design for Satellite Formation...][research_mueller_brito_2003]
- [Control of Mobile Communication Systems With Time-Varying...][research_buche_kushner_2003]
- [Robust Flight Control][research_enns_2003]
- [Robust and Optimal Control of Spatially Interconnected...][research_dandrea_2003]
- [A New Approach to Aeroelastic Response, Stability and Loads...][research_hodges_2004]
- [Application of Computational Stability and Control Techniques...][research_schusterdavidm_edwardsjohnw_2004]
- [Control of Systems With Periodic Coefficients, With...][research_celi_lovera_2004]
- [Multi-Vehicle Experimental Platform for Distributed...][research_how_2004]
- [Dynamic-Active Flow Control - Phase I][research_soria_2006]
- [Perturbation Methods in Stability and Norm Analysis of...][research_fardad_bamieh_2006]
- [Scheduling and Control of Mobile Communications Networks with...][research_kushner_2006]
- [General Procedure for Lifetime Seaway Load Estimation LSLE...][research_richardson_2007]
- [Intelligent Flight Control Simulation Research Program][research_stolarik_2007]
- [Loss-of-Control-Inhibitor Systems for Aircraft][research_aharrahralphc_2007]
- [Reconfigurable Control with Neural Network Augmentation for a...][research_burkenjohnj_2007]
- [Control of Air Vehicle Swarms][research_dandrea_2008]
- [Unsteady Aerodynamic Models for Flight Control of Agile Micro...][research_rowley_2008]
- [Adaptive Control, Wide Speed Range Flight, and Deconfliction][research_ronflenadaud_2009]
- [Airfoil/Wing Flow Control Using Flexible Extended Trailing...][research_liu_liou_2009]
- [Combat Vehicle Fire Control Systems - Overview Document][research_aberdeentestcentermd_2009]
- [Development of Analysis Tools for Certification of Flight...][research_packard_seiler_2009]
- [Dynamic Fit and Misfit through Organizational Design...][research_nissen_2009]
- [Limited Investigation of Active Feel Control Stick System...][research_coldsnow_uybarreta_2009]
- [The Experiment is Over, the Time Has Come to Reorganize the...][research_taylor_2009]
- [Risk Assessment Using the Three Dimensions of Probability...][research_watsonclifford_2010]
- [Control of Metastatic Colonization in Prostate Cancer The...][research_szmulewitz_2011]
- [Control-Oriented Aeroelastic Reduced-Order Modeling of...][research_farhat_amsallem_2011]
- [Risk Assessment Using the Three Dimensions of Probability...][research_watsoncliffordc_2011]
- [Stability of the IMEX Methods, CNLF and BDF2-AB2, for...][research_layton_trenchea_2011]
- [Aero-Effected Flight Control Using Distributed Active Bleed][research_glezer_leonard_2012]
- [Control of Metastatic Colonization in Prostate Cancer The...][research_szmulewitz_2012]
- [An Aircraft Electric Power Testbed for Validating...][research_rogersten_xu_2013]
- [Idempotent Methods for Control and Games][research_mceneaney_2013]
- [Active Flow Control with Thermoacoustic Actuators][research_taira_2014]
- [Theory, Guidance, and Flight Control for High Maneuverability...][research_fresconi_celmins_2014]

- [STABILITY AND CONTROL CHARACTERISTICS OF DOUGLAS MODEL...][research_huff_ww_1949]
- [FLIGHT EVALUATIONS OF VARIOUS LONGITUDINAL HANDLING QUALITIES...][research_harper_robertp_1955]
- [Handling Qualities of Helicopters and VTOL Aircraft][research_reeder_1958]
- [An analytical and flight-test approach to the reduction of...][research_levi_nelson_1964]
- [Simulator investigation of the effects of l alpha and true...][research_chalk_1964]
- [Effect of variable sweep on supersonic transport handling...][research_higgins_shomber_1965]
- [Research on vtol aircraft handling qualities criteria][research_miller_clark_1965]
- [SUGGESTED REQUIREMENTS FOR V/STOL FLYING QUALITIES][research_curry_matthews_1965]
- [An assessment of the lateral-disectional handling qualities...][research_teper_stapleford_1966]
- [Experimental investigation of pilot dynamics in a...][research_hirsch_mccormick_1966]
- [Handling qualities research at the National Aeronautical...][research_mcgregor_smith_1966]
- [Longitudinal handling qualities criteria - An evaluation][research_shomber_gertsen_1967]
- [A Graphical Summary of Military Helicopter Flying and Ground...][research_griffin_bellaire_1968]
- [Navy variable-stability studies of longitudinal handling...][research_eney_1968]
- [Background Information and User Guide for Mil-F-8785B ASG...][research_chalk_neal_1969]
- [Comments on "Navy Variable-Stability Studies of Longitudinal...][research_malcom_1969]
- [Volume II. Flying Qualities Phase, Chapter 16. Chapter 16...][research_airforcetestpilotschooledwardsafbca_1969]
- [A NEW APPROACH TO THE SPECIFICATION AND EVALUATION OF FLYING...][research_anderson_1970]
- [A regression analysis of pilot-induced oscillation ratings][research_eichler_1970]
- [Category 2 Performance and Flying Qualities Tests of the...][research_barbini_balfe_1970]
- [Higher-order control system dynamics and longitudinal...][research_difranco_1970]
- [New longitudinal handling qualities data - Carrier approach][research_miller_1970]
- [An Approac e Determination of Aircraft Handling Qualities...][research_adams_hatch_1971]
- [Category II Performance and Flying Qualities Tests of the...][research_ritter_gurley_1971]
- [Requirements on Simulators Used in Handling Qualities Research][research_gallagher_1971]
- [The Development of Flying Qualities for Lifting Re-Entry...][research_difranco_1971]
- [The Generation of a Military Specification for Flying...][research_key_1971]
- [Analytic Design of Digital Flight Controllers to Realize...][research_montgomery_1972]
- [Design of Desirable Airplane Handling Qualities via Optimal...][research_kriechbaum_stineman_1972]
- [Factors Affecting Handling Qualities of a Lift‐Fan Aircraft...][research_gerdes_hynes_1972]
- [Longitudinal handling qualities during approach and landing...][research_franklinja_innisrc_1972]
- [Flight Simulator Experiments and Analyses in Support of...][research_vinje_miller_1973]
- [Structural Mode Effects on Flying Qualities in Turbulence][research_crother_gabelman_1973]
- [A Two-Phase Investigation of Longitudinal Flying Qualities...][research_boothe_chen_1974]
- [Handling Qualities Effects on Precision Weapons Delivery][research_hall_weingarten_1974]
- [Interactive Computer-Aided Design Aircraft Flying Qualities...][research_place_altmann_1974]
- [Analysis of longitudinal pilot-induced oscillation tendencies...][research_smithjw_berrydt_1975]
- [Handling Qualities Evaluation of the XV‐15 Tilt Rotor Aircraft][research_marr_roderick_1975]
- [Handling qualities of aircraft with stabilty and control...][research_hodgkinson_lamanna_1976]
- [Handling qualities requirements for control configured...][research_woodcockrj_georgefl_1976]
- [Inertially Derived Flying Qualities and Performance Parameters][research_bowes_miller_1976]
- [Simulator study of the low-speed handling qualities of a...][research_granthamwd_nguyenlt_1976]
- [Investigation of the influence of simulated turbulence on...][research_jacobson_joshi_1977]
- [Handling Qualities of Aircraft in the Presence of Simulated...][research_jacobson_joshi_1978]
- [Analysis of a lateral pilot-induced oscillation experienced...][research_smithjw_1979]
- [Design of Desirable Handling Qualities for Aircraft Lateral...][research_ohta_nikiforuk_1979]
- [Effects of Dynamic Aeroelasticity on Aircraft Handling...][research_swaim_yen_1979]
- [Flying Qualities Design Requirements for Sidestick Controllers][research_black_moorhouse_1979]
- [Handling Quality Requirements for Advanced Aircraft Design...][research_smith_geddes_1979]
- [Powered-Lift Aircraft Handling Qualities in the Presence of...][research_jewell_heffley_1979]
- [USAF Flying Qualities Requirements for a STOL Short Takeoff...][research_gerken_1979]
- [V/STOL Aircraft Design Sensitivity to Flying Qualities...][research_chancevoughtcorpdallastx_1979]
- [Flying Qualities Design Criteria. Proceedings of AFFDL Flying...][research_crombie_moorhouse_1980]
- [Landing flying qualities evaluation criteria for augmented...][research_radfordrc_smithr_1980]
- [Analysis of augmented aircraft flying qualities through...][research_baileyre_smithre_1981]
- [Effect of Winglets on Performance and Handling Qualities of...][research_vandam_holmes_1981]
- [Flying Qualities Phase, Volume II. Chapter 15 Dynamic...][research_airforcetestpilotschooledwardsafbca_1981]
- [Flying qualities criteria and flight control design][research_berrydt_1981]
- [An Adaptive Stick-Gain to Reduce Pilot-Induced Oscillation...][research_powers_1982]
- [Handling Qualities Specifications for U.S. Military...][research_key_1982]
- [Model-Based Handling Qualities Assessment Technique for Large...][research_levison_1982]
- [Helicopter Flying Qualities Characteristics-CH-46E. Volume 4][research_boeingvertolcophiladelphiapa_1983]
- [Tentative STOL Short-Takeoff-and-Landing Flying Qualities...][research_hoh_mitchell_1983]
- [Twenty-five years of handling qualities research][research_ashkenas_1984]
- [Criteria for Low-Speed Longitudinal Handling Qualities of...][research_stinton_1985]
- [Handling qualities related to stall/spin accidents of...][research_anderson_1985]
- [Toward a unifying theory for aircraft handling qualities][research_hess_sunyoto_1985]
- [Longitudinal flying qualitites criteria for single-pilot...][research_bargill_stengel_1986]
- [Volume II. Flying Qualities Phase. Chapter 14 Flight Control...][research_airforcetestpilotschooledwardsafbca_1988_c]
- [Volume II. Flying Qualities Phase. Chapter 2 Vectors and...][research_airforcetestpilotschooledwardsafbca_1988_e]
- [Volume II. Flying Qualities Phase. Chapter 3 Differential...][research_airforcetestpilotschooledwardsafbca_1988_b]
- [Volume II. Flying Qualities Phase. Chapter 4 Equations of...][research_airforcetestpilotschooledwardsafbca_1988_d]
- [Volume II. Flying Qualities Phase. Chapter 8 Dynamics][research_airforcetestpilotschooledwardsafbca_1988]
- [Helicopter Handling Qualities][research_ford_1989]
- [Theory for aircraft handling qualities based upon a...][research_hess_1989]
- [Volume II. Flying Qualities Phase. Chapter 9 Roll Coupling][research_airforcetestpilotschooledwardsafbca_1989]
- [Volume II. Flying Qualities Phase. Chapter 6 Maneuvering...][research_airforcetestpilotschooledwardsafbca_1990_e]
- [Volume II. Flying Qualities Phase. Chapter 7...][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Computer Aided Evaluation of Aircraft Handling Qualities][research_chetty_lakshmi_1991]
- [Flying quality analysis and flight evaluation of a highly...][research_tischlermarkb_fletcherjayw_1991]
- [Optimum aeroelastic design of helicopter rotors for...][research_celi_1991]
- [Volume II. Flying Qualities, Chapter 1 Introduction to Flying...][research_airforcetestpilotschooledwardsafbca_1991_b]
- [Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]
- [Aircraft Maneuvers for the Evaluation of Flying Qualities and...][research_wilson_riley_1993]
- [Piloting Vertical Flight Aircraft A Conference on Flying...][research_christopherlblanken_matthewswhalley_1993]
- [Summary of the effects of engine throttle response on...][research_walshkevinr_1993]
- [Interactive Flying Qualities Toolbox for MATLAB User's Guide...][research_doman_1995]
- [A Limited Flight Test Investigation of Pilot-Induced...][research_kish_mosle_1997]
- [A Low Cost Simulation System to Demonstrate Pilot Induced...][research_alisyedfirasat_1997]
- [Flying Qualities Evaluation of a Commuter Aircraft With an...][research_ranaudorichardj_ratvaskythomasp_2000]
- [Pilot-Induced Oscillation Prediction With Three Levels of...][research_schroederjefferya_chungwilliamwy_2001]
- [Pilot-Induced Oscillation Research Status at the End of the...][research_shafermaryf_steinmetzpaul_2001_b]
- [Pilot-Induced Oscillation Research The Status at the End of...][research_shafermaryf_steinmetzpaul_2001]
- [An Investigation Relating Longitudinal Pilot-Induced...][research_witte_monson_2003]
- [Handling Qualities Evaluations of Low Complexity Model...][research_hansoncurt_schaeferjacob_2011]

- [Comment on "The Neutral Point in Stability and Control...][research_roache_1965]
- [The neutral point in stability and control analysis][research_rodgers_1965]
- [Relationship between the neutral point, maneuver point, and...][research_rodgers_1966]
- [Volume II. Flying Qualities Phase. Chapter 5 Longitudinal...][research_airforcetestpilotschooledwardsafbca_1990]
- [Comment on 'Model flight tests and neutral point...][research_solies_1994]
- [Effects of thrust line offset on neutral point determination...][research_solies_1994_b]

### The Canard, Whose Boundary the Control Loop Set

**The single most interesting structural fact about this aircraft is that its canard was also divergence prone, and that a control law requirement fixed the structural boundary.**

An all-moving surface on a torsional spring diverges when the aerodynamic moment about its axis overcomes
the spring.

$$ q_{D,\mathrm{surface}} = \frac{K_\theta}{e\,S\,a} $$

The primary record states that the canard's torsion axis lies
**about midway between the 25 percent and 50 percent mean aerodynamic chord points**, chosen to balance
subsonic against supersonic hinge moments, and describes that location in as many words as
**not conservatively located from a divergence viewpoint**. It then says the thing that makes this aircraft
what it is.
**The pitch-loop stiffness required for control system stability resulted in a predicted divergence boundary that was well beyond that for the wing.**

**The spring is not only the spindle.** It is the spindle in series with the actuator, and through the
actuator with the flight control system's pitch loop. A stiffness bought to make the control law stable
turned out to be the stiffness that kept the surface from diverging.

$$ K_\theta^{\mathrm{req}} = q_D\,e\,S_c\,a, \qquad e = \left(x_{\mathrm{axis}} - x_{ac}\right)\bar{c}_c $$

Inverting the relation for the loop stiffness that would place the canard's boundary at the wing's 4,533
pounds per square foot gives the scale of what was required.

| Torsion axis, percent MAC | Moment arm, ft | Required stiffness, 10⁶ ft·lb/rad |
|---|---|---|
| 30.0 | 0.274 | 0.295 |
| 37.5 | 0.686 | 0.738 |
| 45.0 | 1.097 | 1.180 |
| 50.0 | 1.371 | 1.475 |

**Moving the axis from thirty percent to fifty percent of the chord multiplies the required stiffness by five**,
because the moment arm grows from a quarter of a foot to nearly a foot and a half. The record's remark that
the chosen location was a **major tradeoff** is therefore an understatement of the sensitivity rather than
of the difficulty.

**Canard free play was tracked as a major concern throughout**, which follows directly. Free play is a
region of zero stiffness, and a spring with a dead band in it has no stiffness at all near the origin.

- [Active Flutter Control-An Adaptable Applicationto Wing/Store...][research_triplett_kappus_1973]
- [Passive wing/store flutter suppression][research_passive_wing_store_1982]
- [Active flutter control using discrete optimal constrained...][research_broussardjr_halyon_1983]
- [Flight test results of an active flutter suppression system][research_edwards_1983]
- [Digital flutter suppression of active flexible wing using...][research_klepl_1995]
- [Innovative Scaling Laws for Study of Nonlinear Aeroelastic...][research_friedmann_1998]
- [Adaptive Reconfigurable Control Based on a Reduced Order...][research_nam_chen_2000]
- [Active Flutter Suppression Using Cooperative, High Frequency...][research_armstrong_lindberg_2006]
- [Rapid State Space Modeling Tool for Rectangular Wing...][research_suhpeterm_conyershowardj_2014]

### Trim and the Case for Putting the Surface in Front

The static margin itself is the distance from the centre of gravity to the neutral point, measured in mean
aerodynamic chords, and it is negative when the neutral point lies ahead.

$$ \mathrm{SM} = \frac{x_{np} - x_{cg}}{\bar{c}} = -0.35 $$

A supercritical section carries a large nose-down pitching moment about its aerodynamic centre, which is the
price of its aft loading. That moment must be trimmed at every flight condition, and
**the sign of the load that trims it is the entire argument for a canard.**

The moment balance uses the surface's own lift coefficient against the tail volume coefficient, which is
defined as

$$ V_H = \frac{S_s}{S}\cdot\frac{l}{\bar{c}} $$

$$ C_{L_{\mathrm{surface}}} V_H = -C_{m_{ac}} $$

The quantity that enters the drag comparison, however, is the lift the surface contributes referenced to the
wing, which is $C_{L_{\mathrm{surface}}} S_s / S$. Substituting the volume coefficient,

$$ \Delta C_L = -\frac{C_{m_{ac}}}{l/\bar{c}} $$

and **the surface area cancels completely.** The trim increment depends only on the aerofoil's moment and
the moment arm, which is worth stating because it is easy to carry the surface's own lift coefficient into
the comparison as though it were already wing-referenced, and doing so inflates the trim load by the inverse
area ratio, a factor of five for this aircraft.

At a canard arm of 1.75 mean aerodynamic chords and an area ratio of 0.20, giving a volume coefficient of
0.35, and taking the section moment as **assumed** at $-0.10$,

$$ \Delta C_L = \frac{0.10}{1.75} = 0.0571 $$

The induced drag both configurations pay follows the usual relation, with the wing carrying whatever the
trimming surface does not.

$$ C_{D_i} = \frac{C_L^2}{\pi A e} = k\,C_L^2, \qquad k = \frac{1}{\pi A e} = \frac{1}{\pi \times 4.0 \times 0.85} = 0.0936 $$

Evaluating both configurations at the same total lift coefficient of 0.8, so that the comparison is fair,
the wing carries 0.743 with a canard and 0.857 with an aft tail, and the induced drag follows the square.

$$ \frac{C_{D_i}^{\mathrm{tail}}}{C_{D_i}^{\mathrm{canard}}} = \left(\frac{0.857}{0.743}\right)^2 = 1.331 $$

**Trimming with a down load costs about a third more induced drag than trimming with an up load**, at this
moment and this arm. Neither was published, so both deserve a sensitivity table.

| Section moment $C_{m_{ac}}$ | Arm, MAC | Surface $C_L$ | Wing-referenced $\Delta C_L$ | Drag ratio |
|---|---|---|---|---|
| −0.05 | 1.50 | 0.167 | 0.0333 | 1.181 |
| −0.05 | 1.75 | 0.143 | 0.0286 | 1.154 |
| −0.05 | 2.50 | 0.100 | 0.0200 | 1.105 |
| −0.10 | 1.50 | 0.333 | 0.0667 | 1.397 |
| −0.10 | 1.75 | 0.286 | 0.0571 | 1.331 |
| −0.10 | 2.50 | 0.200 | 0.0400 | 1.222 |
| −0.15 | 1.50 | 0.500 | 0.1000 | 1.653 |
| −0.15 | 1.75 | 0.429 | 0.0857 | 1.538 |
| −0.15 | 2.50 | 0.300 | 0.0600 | 1.351 |

**The advantage is real across the whole range and it is modest**, running from about eleven percent to
about sixty-five percent depending on how aft-loaded the section is and how long the arm. It is not the
dominant term in the aircraft's drag, and an article that presented the canard purely as a drag reduction
device would be overstating a secondary effect.

The canard was **truly close coupled to provide mutual interference with the wing aerodynamics**, coplanar
and without dihedral. The record states that
**canard lift due to angle of attack is approximately 1.5 times that due to canard incidence**, and warns
that
**any misprediction of these interference effects could have a large influence on the load distributions of both surfaces.**

- [The Voisin “Canard” Biplane][research_the_voisin_1911]
- [Longitudinal Stability and Control Characteristics from a...][research_moulmartint_winemanandrewr_1952]
- [Canard Corrected][research_dushane_1957]
- [Effects of Deflected Wing Tips on the Aerodynamic...][research_brightlg_petersonvl_1960]
- [Modifications de caractères raciaux du canard pékin par...][research_benoit_leroy_1960]
- [Modifications héréditaires de caractères morphologiques du...][research_benoit_1969]
- [Some Trim Drag Considerations for Maneuvering Aircraft][research_mcklnney_dollyhlgh_1971]
- [Nonlinear Vortex Interactions on Wing-Canard Configurations][research_finkleman_1972]
- [Effect of vertical-tail location on the aerodynamic...][research_huffmanjk_1975]
- [Flow visualization study of close-coupled canard wing and...][research_minerdd_glossbb_1975]
- [Effects of deflected thrust on the longitudinal aerodynamic...][research_yiplp_paulsonjwjr_1977]
- [Load distribution on a close-coupled wing canard at transonic...][research_glossbb_washburnke_1977]
- [Canard-Wing Shape Optimization with Aerodynamic Requirements][research_desilva_carmichael_1978]
- [Deflected Thrust Effects on a Close-Coupled Canard...][research_thomas_paulson_1978]
- [Effect of twist and camber on the low-speed aerodynamic...][research_paulsonjwjr_thomasjl_1978]
- [Load Distribution on a Close-Coupled Wing Canard at Transonic...][research_gloss_washburn_1978]
- [Subsonic dynamic stability characteristics of two...][research_boydenrp_1978]
- [Vortex Effects for Canard-wing Configurations at High Angles...][research_desilvabme_medanrt_1978]
- [Summary of low-speed longitudinal aerodynamics of two powered...][research_paulsonjwjr_thomasjl_1979_b]
- [Transition aerodynamics for close-coupled wing-canard...][research_paulsonjwjr_thomasjl_1979]
- [Transonic flow calculations over two-dimensional canard-wing...][research_shankar_malmuth_1981]
- [Computational Treatment of Transonic Canard-Wing Interactions][research_shankar_malmuth_1982]
- [Computational treatment of three-dimensional transonic...][research_shankar_malmuth_1983]
- [Experimental wing and canard jet-flap aerodynamics][research_smeltzer_durston_1983]
- [High angle-of-attack aerodynamics of a strake-canard-wing...][research_durstonda_schreinerja_1983]
- [Large-scale wind-tunnel investigation of a close-coupled...][research_stollf_koenigdg_1983]
- [Aerodynamic design optimization trim analysis of canard...][research_keith_selberg_1984]
- [An evaluation of the relative merits of wing-canard...][research_nicholaswu_navillegl_1984]
- [Close-coupled canard-wing vortex interaction][research_calarese_1984]
- [Aerodynamic canard/wing parametric analysis for...][research_keith_selberg_1985]
- [Aerodynamic-structural study of canard wing, dual wing, and...][research_selbergbp_cronindl_1985]
- [Canard Aladodine][research_santich_1985]
- [Canard/Tail Transonic Analysis][research_aidala_1985]
- [Transonic aerodynamic computations for a canard configuration][research_agrell_elmeland_1985]
- [Vortex trajectories and breakdown on wing-canard...][research_erel_seginer_1985]
- [A split-canard configuration for improved control at high...][research_katz_davidovitch_1986]
- [Canard/tail comparison for an advanced variable-sweep-wing...][research_landfield_rajkovic_1986]
- [Self-induced roll oscillations measured on a delta...][research_katz_levin_1986]
- [Wind-tunnel investigation of the OMAC canard configuration][research_ingramwc_yiplp_1986]
- [Effect of wing/canard interference on the loading of a delta...][research_erel_1988]
- [Transonic Euler solutions on a blunt, body-wing-canard...][research_lijewski_1988]
- [A closed-form trim solution yielding minimum trim drag for...][research_goodrichkennethh_sliwastevenm_1989]
- [Canard-wing interaction in unsteady supersonic flow][research_stark_1989]
- [Investigations on the vorticity sheets of a close-coupled...][research_oelker_hummel_1989]
- [Low speed aerodynamics of canard configurations][research_bandyopadhyay_1989]
- [Low-speed aerodynamic characteristics of close-coupled canard...][research_bandyopadhyay_1991]
- [Navier-Stokes simulation of a close-coupled canard-wing-body...][research_tueugenel_1991]
- [Effect of canard deflection on close-coupled canard-wing-body...][research_tueugenel_1992]
- [Effect of canard position on the longitudinal aerodynamic...][research_tueugenel_1992_b]
- [Navier-Stokes simulation of a close-coupled canard-wing-body...][research_tu_1992]
- [The TFX Decision The Joint Canard][research_talbot_geraldl_1992]
- [Visualisation in Water of Vortex Flow Over Sharp-Edged Canard...][research_thompson_1992]
- [Downwash measurements on a pitching canard-wing configuration][research_burkhalter_1993]
- [Composition des 3 types de foie gras oie, canard mulard et...][research_salichon_guy_1994]
- [Effect of canard deflection on close-coupled canard-wing-body...][research_tu_1994]
- [Flowfield study of a close-coupled canard configuration][research_howard_oleary_1994]
- [Low-speed characteristics for the wing-canard configuration...][research_hummel_oelker_1994]
- [Numerical investigations on two-dimensional canard-wing...][research_lin_chin_1994]
- [Vortex-wing interaction of a close-coupled canard...][research_tu_1994_b]
- [Canard tip vortex splitting in a canard-wing configuration...][research_lombardi_1995]
- [Comparaison des performances de l'oie, du canard mulard et du...][research_guy_rousselotpailley_1995]
- [Numerical analysis of the vortical flow around a delta...][research_das_longo_1995]
- [Navier-Stokes Simulation of the Canard-Wing-Body Longitudinal...][research_tueugenel_vandalsemwilliamr_1996]
- [Numerical Study of Steady and Unsteady Canard-Wing-Body...][research_eugeneltu_1996]
- [High Maneuverability Airframe Investigation of Fin and Canard...][research_silton_fresconi_2014]
- [Static Aeroelastic and Longitudinal Trim Model of Flexible...][research_tingeric_nguyennhan_2014]

- [Report no. 121, The minimum induced Drag of aerofoils][research_report_no_1921]
- [Report No. 349. A proof of the theorem regarding the...][research_report_no_1930]
- [Minimum Induced Drag][research_lockwoodtaylor_1942]
- [Induced Drag of a Twisted Wing][research_sibert_1943]
- [The Wave and Induced Drag of a Hydrofoil of Finite Span in...][research_breslin_1961]
- [Lift Distribution and Lift-Induced Drag Ratio of a Finite...][research_lakshminarayana_1962]
- [SUBSONIC WING SPAN EFFICIENCY][research_frost_rutherford_1963]
- [Subsonic induced drag][research_sanders_1965]
- [Effect of flow shear on induced drag][research_chen_mangione_1967]
- [Minimum swept-wing induced drag with constraints on lift and...][research_lundry_1967]
- [Note on the solar wind-induced drag on comets][research_gonzales_1969]
- [OPTIMUM LOADING ON NONPLANAR WINGS AT MINIMUM INDUCED DRAG][research_loth_boyle_1969]
- [On the Minimum Induced Drag of Ground-Effect Wings][research_ashill_1970]
- [Comment on " Span wise Distribution of Induced Drag in...][research_hancock_1971]
- [The induced drag on a rolling wing][research_hancock_1972]
- [Minimum induced drag of wings with given lift and...][research_klein_viswanathan_1973]
- [Minimum induced drag of ground effect wings][research_ando_yashiro_1976]
- [Calculation of lift and induced drag from sparse span loading...][research_lundry_1977]
- [Optimization of flexible wing structures subject to strength...][research_haftka_1977]
- [Positive Tail Loads for Minimum Induced Drag of Subsonic...][research_laitone_1978]
- [Effect of downwash on the induced drag of canard-wing...][research_butler_1982]
- [Minimum Induced Drag of Canard Configurations][research_kroo_1982]
- [An analytical study of the induced drag of canard-wing-tail...][research_butler_1983]
- [The theoretical minimum induced drag of three-surface...][research_kendall_1985]
- [Transient induced drag][research_weihs_katz_1986]
- [Reductions in induced drag by the use of aft swept wing tips][research_burkett_1989]
- [Minimum induced drag for wings with spanwise camber][research_lowson_1990]
- [Induced drag of a wing in a circular wind tunnel][research_yamamoto_1992]
- [Wing design for hanggliders having minimum induced drag][research_sugimoto_1992]
- [Induced Drag of Wings of Finite Aspect Ratio][research_lam_1993]
- [Nonplanar wings with minimum induced drag][research_lyapunov_1993]
- [Induced drag prediction for wing-tail and canard...][research_lombardi_vicini_1994]

### The Transonic Argument

The programme's aerodynamic claim was a drag saving of
**up to thirteen percent for wings of the same aspect ratio**, and the mechanism given in the primary record
is specific.
**A forward-swept wing requires less leading-edge sweep for the same shock sweep and location.**

That claim can be checked rather than repeated. An isobar lying at a constant chord fraction has a sweep
interpolated between the two edges.

$$ \tan\Lambda_{f} = \tan\Lambda_{LE} + f\left(\tan\Lambda_{TE} - \tan\Lambda_{LE}\right) $$

and the trailing edge sweep follows from the planform.

$$ \tan\Lambda_{TE} = \tan\Lambda_{LE} - \frac{4}{A}\cdot\frac{1 - \lambda}{1 + \lambda} $$

For the X-29's leading edge at 29.3 degrees forward, an aspect ratio of 4.0 and an **assumed** taper ratio
of 0.4, the trailing edge sweeps 44.70 degrees forward, and the isobars sweep progressively more forward
across the chord.

| Chord fraction | Isobar sweep |
|---|---|
| 0 percent | 29.30° forward |
| 25 percent | 33.76° forward |
| 50 percent | 37.79° forward |
| 75 percent | 41.43° forward |
| 100 percent | 44.70° forward |

**A forward-swept wing's isobars are swept more than its leading edge, and an aft-swept wing's are swept less**,
because the trailing edge moves in opposite directions in the two cases. The transonic literature this
argument sits inside begins with the National Advisory Committee for Aeronautics, whose transonic
conferences and aileron reversal studies of the 1940s and 1950s established the relationship between shock
sweep and control effectiveness that the X-29's planform argument assumes. The effects compound, and
matching the isobar costs the aft-swept wing a great deal of leading-edge sweep.

$$ \Lambda_{LE}^{\mathrm{aft}} = 44.70^\circ \quad \text{to match} \quad \Lambda_{50\%} = 37.79^\circ $$

**The aft-swept wing needs 44.70 degrees of leading-edge sweep to achieve what the forward-swept wing achieves with 29.30, a difference of 15.40 degrees.**
The primary source's claim is therefore correct and now has a number attached to it.

Sweep earns its keep by reducing the Mach number the section actually sees, and the isobar sweep rather than
the leading-edge sweep is what governs that.

$$ M_n = M\cos\Lambda_{50\%} $$

| Flight Mach | Normal to the 50 percent isobar |
|---|---|
| 0.90 | 0.711 |
| 1.07 | 0.846 |
| 1.48 | 1.170 |

**At the design point of Mach 1.07 the section sees 0.846**, which is subsonic, and that is the whole
purpose of sweeping a wing at all.

The structural consequence follows. Computing the box length between a fifteen percent front spar and a
seventy percent rear spar for both planforms at equal isobar sweep gives
**17.12 feet forward-swept against 17.66 feet aft-swept**, a ratio of 0.969, so the forward-swept box is
**about three percent shorter**.

The reason a shorter box is worth having is that it shortens the lever arm the root bending moment acts
through.

$$ M_{\mathrm{root}} = \tfrac{1}{2}n\,W\,\eta_{cp}\,\frac{b}{2} = \tfrac{1}{2} \times 8.0 \times 15{,}000 \times 0.4 \times 13.74\ \mathrm{ft} = 3.30 \times 10^{5}\ \mathrm{ft\,lb} $$

**That comparison must be made at equal shock sweep and not at equal leading-edge sweep, and the difference between those two questions reverses the answer.**
At equal leading-edge sweep the same calculation gives 17.12 feet forward against 14.70 feet aft, making the
forward-swept box the longer of the two. **Both numbers are correct and they answer different questions.**
The one that bears on the programme's claim is the first, because a wing is designed to a shock position
rather than to a leading-edge angle.

- [Two-Dimensional Transonic Flow Patterns][research_bergman_1948]
- [NACA Conference on Aerodynamic Problems of Transonic Airplane...][research_naca_conference_1949]
- [A Note on the Problem of Aileron Reversal at Transonic Speeds][research_hunn_1953]
- [On Transonic Airfoil Theory][research_guderley_1956]
- [STATIC STABILITY AND MAGNUS CHARACTERISTICS OF THE U.S. NAVY...][research_greene_1957]
- [BASE PRESSURE EFFECTS RESULTING FROM CHANGES IN TUNNEL...][research_rittenhouse_1959]
- [INVESTIGATION OF STATIC STABILITY AND AERODYNAMIC EFFECTS OF...][research_baker_galigher_1960]
- [A Theory of Transonic Aileron Buzz, Neglecting Viscous Effects][research_eckhaus_1962]
- [STATIC AND DYNAMIC STABILITY STUDIES ON SEVERAL LAZY DOG...][research_eades_jr_1964]
- [UNSTEADY AERODYNAMICS FOR ADVANCED CONFIGURATIONS. PART 2. A...][research_rodemich_andrew_1965]
- [AN INVESTIGATION OF THE AEROELASTIC STABILITY OF THIN...][research_perkins_brice_1966]
- [DEMONSTRATION OF A TRANSONIC BOX METHOD FOR UNSTEADY...][research_olsen_1966]
- [Flight Test Evaluation of a Supercritical-Speed Shaft][research_baier_1970]
- [Separation and Reattachment in Transonic Airfoil Flow][research_stanewsky_little_1971]
- [Supercritical Wing Tested][research_supercritical_wing_1971]
- [Transonic airfoil design][research_cahn_garcia_1971]
- [Body Alone Aerodynamics of Guided and Unguided Projectiles at...][research_moore_1972]
- [Measurement of the pressure at an oscillating aileron in a...][research_nazarenko_nevezhina_1972]
- [Transonic transport study Structures and aerodynamics][research_ardemamd_williamslj_1972]
- [Inverse method of designing two-dimensional transonic airfoil...][research_sato_1973]
- [Transonic Viscous Interactions][research_smetana_1973]
- [Wind Tunnel Model Parametric Study for Use in the Proposed 8...][research_alexander_griffin_1973]
- [Aerodynamic characteristics of an improved 10-percent-thick...][research_harriscd_1974_b]
- [Aerodynamic characteristics of two 10-percent-thick NASA...][research_harriscd_1974]
- [Dynamic stability characteristics in pitch, yaw, and roll of...][research_boydenrp_1974]
- [Measured Three-Dimensional Effects in Transonic Airfoil...][research_hurley_1975]
- [Unsteady Transonic Flows over an Airfoil][research_magnus_yoshihara_1975]
- [Transonic Airfoil Analysis and Design Using Cartesian...][research_carlson_1976]
- [Data Report for a Test Program to Study Transonic Flow Fields...][research_perkins_jr_1977]
- [Estimation of Transonic Aircraft Aerodynamics to High Angles...][research_axelson_1977]
- [Investigation of a Variable Camber Wing Design][research_beatty_brooks_1977]
- [Measurement of model aeroelastic deformations in the wind...][research_brooksjd_beamishjk_1977]
- [The Aeroelastic Analysis of a Two-Dimensional Airfoil in...][research_rizzetta_1977]
- [Transonic wind-tunnel investigation of the maneuver potential...][research_hallissyjb_ayerstg_1977]
- [Wind-Tunnel Wall Interference Effects on a Supercritical...][research_blackwell_pounds_1977]
- [Calculation of Transonic Flow over Supercritical Airfoil...][research_rose_seginer_1978]
- [Flight comparison of the transonic agility of the F-111A...][research_friendel_sakamotogm_1978]
- [Transonic flows around a carrying airfoil profile][research_lifshits_ryzhov_1978]
- [Unsteady Transonic Thin-Airfoil Theory for Power-Law Upwash][research_plotkin_1978]
- [Facility Air Control Systems Design for a Pilot Transonic...][research_cain_1979]
- [Lifting-line theory for a swept wing at transonic speeds][research_cook_1979]
- [Time-Dependent Response of a Two-Dimensional Airfoil in...][research_rizzetta_1979]
- [Transonic Wind Tunnel Tests on an Oscillating Wing with...][research_tijdeman_vannunen_1979_b]
- [Transonic Wind Tunnel Tests on an Oscillating Wing with...][research_tijdeman_vannunen_1979]
- [Transonic airfoil codes][research_garabedianpr_1979]
- [Wing/Store Flow-Field Measurement at Transonic Speeds Using a...][research_heltsley_cline_1979]
- [Calculation of Transonic Aileron Buzz][research_steger_bailey_1980]
- [Transonic Aerodynamics][research_cole_cook_1980]
- [Transonic and Low Supersonic Wind-Tunnel Tests on a Wing with...][research_persoon_roos_1980]
- [Transonic swept-wing analysis using asymptotic and other...][research_chenghk_mengsy_1980]
- [Unsteady Thin Airfoil Theory for Transonic Flows with...][research_williams_1980]
- [Transonic Wing/Store Flow-Field Measurement Using a Laser...][research_heltsley_crosswy_1981]
- [Experiment of a Shockless Transonic Airfoil Partially...][research_nakamura_1982]
- [Improved Finite-Difference Scheme for Transonic Airfoil...][research_chen_1982]
- [Transonic Fan/Compressor Rotor Design Study. Volume 2][research_parker_simonson_1982_b]
- [Transonic Fan/Compressor Rotor Design Study. Volume 5][research_parker_simonson_1982_c]
- [Transonic Fan/Compressor Rotor Design Study. Volume 6][research_parker_simonson_1982]
- [Transonic Flow Research][research_fung_1982]
- [Wing-Alone Aerodynamic Characteristics to High Angles of...][research_briggs_reed_1982]
- [Aerodynamic design for improved maneuverability by the use of...][research_mannmj_campbellrl_1983]
- [Combined Direct/Inverse Three-Dimensional Transonic Wing...][research_weed_carlson_1983]
- [Geometric and structural properties of a rectangular...][research_rickettsrh_watsonjj_1983]
- [Transonic Shock-Turbulent Boundary Layer Interactions on...][research_inger_1983]
- [Transonic airfoil calculations using solution-adaptive grids][research_holst_brown_1983]
- [Transonic pressure distributions on a rectangular...][research_rickettsrh_sandfordmc_1983]
- [Unsteady Transonic Pressure Measurements on a Semi-Span Wind...][research_hortsen_boer_1983]
- [Aerodynamic design for improved manueverability by use of...][research_mannmj_campbellrl_1984]
- [Errata Unsteady Pressures and Forces During Transonic...][research_lee_ohman_1984_b]
- [Joined Wing Transonic Design and Test Validation][research_clyde_bonner_1984]
- [Pseudospectral Calculations of Two-Dimensional Transonic Flow...][research_jou_metcalfe_1984]
- [Supercritical Airfoil and Wing Design][research_sobieczky_1984]
- [Transonic Merging Separated Flows][research_koenig_1984]
- [Unsteady pressures and forces during transonic buffeting of a...][research_lee_ohman_1984]
- [A Zonal Approach to the Design of Finite Element Grids for...][research_ecer_1985]
- [Measured unsteady transonic aerodynamic characteristics of an...][research_seidelda_sandfordmc_1985]
- [Steady and unsteady transonic airloads on a supercritical wing][research_ruo_malone_1985]
- [Transonic airfoil calculations including wind tunnel...][research_king_johnson_1986]
- [An experimental investigation of a supercritical airfoil at...][research_mateergeorgec_seegmillerhlee_1987]
- [Measured unsteady transonic aerodynamic characteristics of an...][research_seidel_sandford_1987]
- [Transonic aeroelasticity of wings with tip stores][research_guruswamy_goorjian_1987]
- [Two experimental supercritical laminar-flow-control...][research_allisondenniso_dagenhartjray_1987]
- [Computation of transonic aerodynamically compensating pilot...][research_luo_bao_1988]
- [External store carriage loads prediction at transonic speeds][research_rosenbruces_1988]
- [Finite-volume calculation of inviscid transonic...][research_damodaran_caughey_1988]
- [Theoretical Aerodynamics, Transonic Flow][research_cole_1988_b]
- [Viscous transonic airfoil workshop compendium of results][research_holst_1988]
- [Applications of a transonic wing design method][research_campbellrichardl_smithleigha_1989]
- [Similarity for high-angle-of-attack subsonic/transonic...][research_hemsch_1989]
- [Transonic buffet of a supercritical airfoil with...][research_lee_tang_1989]
- [Transonic region of high dynamic response encountered on an...][research_seidel_eckstrom_1989]
- [Transonic unsteady pressure measurements on a supercritical...][research_hess_seidel_1989]
- [High-Reynolds-Number Test of a 5-Percent-Thick...][research_chujulio_lawingpiercel_1990]
- [Using transonic small disturbance theory for predicting the...][research_silvawaltera_bennettrobertm_1990]
- [Book Review High Angle of Attack Aerodynamics Subsonic...][research_rom_lamar_1992]
- [Transonic aeroelasticity analysis for rotor blades][research_gea_chow_1992]
- [Transonic aeroelasticity analysis using state-space unsteady...][research_crouse_leishman_1992]
- [“High Angle of Attack Aerodynamics Subsonic, Transonic and...][research_hancock_1992]
- [Transonic airfoil design by constrained optimization][research_lee_eyi_1993]
- [Transonic shock-induced dynamics of a flexible wing with a...][research_bennett_dansberry_1993]
- [Limit cycle phenomena in computational transonic...][research_kousen_bendiksen_1994]
- [Sensitivity Analysis of Aeroelastic Response of a Wing in...][research_kapania_issac_1994]
- [Transonic aeroelastic models of highly swept hypersonic...][research_pendleton_moster_1995]
- [Turbulent drag reduction using riblets on a supercritical...][research_viswanath_mukund_1995]
- [Desktop Computer Programs for Preliminary Design of Transonic...][research_mcdonald_2001]
- [Control of Interacting Vortex Flows at Subsonic and Transonic...][research_ericksongarye_2003]
- [Dynamic Aeroelastic Instabilities of an Aircraft Wing with...][research_byreddy_grandhi_2003]
- [Multidisciplinary Optimization of an Aircraft Wing/Tip Store...][research_janardhan_grandhi_2003]

- [Slope of Lift Curve for Any Aspect Ratio][research_sibert_1937]
- [Performance Estimation of Civil Jet Aircraft][research_edwards_1950]
- [RESEARCH ON HIGH SPEED ROTARY-FIXED WING AIRCRAFT. VOLUME IV...][research_snyder_1950]
- [Altitude Performance of Modified J71 Afterburner with Revised...][research_usellerjamesw_russeyroberte_1955]
- [Aeroelastic Problems of Low Aspect Ratio Wings][research_farbridge_woodward_1956]
- [EFFECT OF PERFORMANCE CRITERIA ON THE OPTIMUM DESIGN OF THE...][research_dallas_irvin_1956]
- [Hovering Static Stability and Performance Experiments on...][research_carmichael_mcnay_1961]
- [YHU-1B CATEGORY I PERFORMANCE, STABILITY AND CONTROL TESTS][research_westphal_balfe_1961]
- [Flight performance handbook for powered flight operations][research_flight_performance_1963]
- [INVESTIGATION OF DRAG REDUCTION BY BOUNDARY-LAYER SUCTION ON...][research_pate_deitering_1963]
- [INVESTIGATION OF DRAG REDUCTION BY BOUNDARYLAYER SUCTION ON A...][research_pate_1964]
- [ANALYTIC STUDY OF AIRCRAFT AGILITY IN THE TURNAROUND MANEUVER][research_wrestler_cliftong_1965]
- [Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967_b]
- [Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967]
- [Energy-state approximation in performance optimization of...][research_bryson_desai_1969]
- [Effects of Varying Levels of Autopilot Assistance and...][research_anderson_toivanen_1970]
- [A parametric study of planform and aeroelastic effects on...][research_roskamj_lanc_1972]
- [Maneuver and buffet characteristics of fighter aircraft][research_rayej_mckinneylw_1972]
- [Modeling the Effects of Pilot Performance on Weapon Delivery...][research_leondes_rankine_1972]
- [Effect of Salt Concentration on the Drag Reduction Efficiency...][research_little_1973]
- [Maneuver and buffet characteristics of fighter aircraft][research_rayej_mckinneylw_1973]
- [Low-speed wind-tunnel investigation of the aerodynamic and...][research_abbottjm_millerba_1974]
- [Army Preliminary Evaluation YAH-1R Improved Cobra Agility and...][research_stewart_dominick_1975]
- [Program for establishing long-time flight service performance...][research_harvillwe_kizerja_1976]
- [Effect of Display Color on Pilot Performance and Describing...][research_chase_1977]
- [Extended Energy Management Methods for Flight Performance...][research_calise_1977]
- [The Influence of Vehicle Control Dynamics on Driver-Vehicle...][research_repa_alexandridis_1977]
- [Effects of Helmet Loader Cues on Simulator Pilot Performance][research_ashworth_mckissick_1979]
- [The Performance of a Conceptual Vertical Attitude Takeoff and...][research_papadales_basils_1979]
- [Investigation of High-Angle-of-Attack Maneuver-Limiting...][research_mitchell_myers_1980]
- [Drag reduction of trailer-tractor configuration by...][research_wong_cox_1981]
- [Performance of the Fluidic Power Supply for the XM445 Fuze in...][research_goodyear_lee_1981]
- [THE AERODYNAMIC PERFORMANCE OF THE WING IN RED‐SHOULDERED...][research_withers_1981]
- [An Asymptotic Expression of Lift Slope of Elliptic Wing with...][research_kida_1982]
- [Performance Measures for Aircraft Carrier Landings as a...][research_connelly_1982]
- [Energy metabolism and ageing in Phormia terrae-novae II...][research_wilps_collatz_1983]
- [Aeroelastic behavior of low aspect ratio metal and composite...][research_whitejfiii_bendiksenoo_1986]
- [An Appreciation of Tactical Agility as a Function of the...][research_lovatt_1986]
- [Improving Light Infantry Divisional Engineer Agility the Key...][research_janecek_1986]
- [Turbulence, Turbulence Control, and Drag Reduction][research_sreenivasan_1987]
- [Agility A Key to the Operational Art][research_bryant_albert_1988]
- [Riblet drag reduction at flight conditions][research_walshmichaelj_sellerswilliamliii_1988]
- [Fighter agility metrics][research_lieferrandallk_1990]
- [Impact of emerging technologies on future combat aircraft...][research_nguyenluatt_gilertwilliamp_1990]
- [Robust Adaptive Control Stability and Asymptotic Performance][research_krause_khargonekar_1990]
- [Active Suspension Control Performance Comparisons Using...][research_crolla_abdelhady_1991]
- [Use of piloted simulation for high-angle-of-attack agility...][research_marilyneogburn_johnvfoster_1991]
- [Performance of an energy compensated time-of-flight mass...][research_deconihout_menand_1992]
- [The Army--From the Sea The Army's Initiative to Enhance...][research_brown_1994]
- [Using Grooved Surfaces to Improve the Efficiency of Air...][research_reed_1994]
- [Application of Navier-Stokes aeroelastic methods to improve...][research_schuster_1995]
- [Advanced Technology Composite Fuselage-Structural Performance][research_walkerth_minguetpj_1997]
- [Agility Measures Engineering Agile Systems][research_goranson_1997]
- [Performance of Power-Law Processor with Normalization for...][research_nuttall_1997]
- [Personality Factors Affecting Pilot Combat Performance A...][research_siem_murray_1997]
- [Robust Gain-Scheduled Nonlinear Control Design for Stability...][research_balakrishnan_2000]
- [Force Projection, Strategic Agility and the Big Meltdown][research_hill_2001]
- [High Performance Power Supply for the More Electric Aircraft][research_yuvarajan_2001]
- [Performance Analysis of a Wing With Multiple Winglets][research_smith_komerath_2001]
- [Stokes' Mechanism of Drag Reduction][research_bandyopadhyay_2001]
- [Agility Agent - Ility Architecture][research_thompson_bannon_2002]
- [Drag Reduction from Formation Flight. Flying Aircraft in...][research_blake_2002]
- [Security Agility for Dynamic Execution Environments][research_fraser_petkac_2002]
- [Viscous Drag Measurement and Its Application to Base Drag...][research_decker_2002]
- [Workload Demands of Remotely Piloted Vehicle Supervision and...][research_wickens_dixon_2002]
- [Creating Strategic Agility in Northeast Asia][research_hunter_2003]
- [High-Performance, Soft Magnetic Laminates for Aerospace Power...][research_liu_2004]
- [Turbulent Drag Reduction Using Compliant Coatings][research_choi_2004]
- [Real-Time Control for Optimal Liquid Rocket Combustor...][research_zinn_lubarsky_2005]
- [Polymer Drag Reduction and Bioluminescence Reduction][research_latz_2006]
- [High Performance and High-Fidelity Aeroelastic Simulation of...][research_lesoinne_2007]
- [Polymer Drag Reduction and Bioluminescence Reduction][research_latz_2007]
- [Optimum Design of a Flexible Wing Structure to Enhance Roll...][research_veley_khot_2008]
- [Polymer Drag Reduction and Bioluminescence Reduction][research_latz_2009]
- [The Agility Advantage A Survival Guide for Complex...][research_alberts_2011]
- [Aeroelastic Modeling of Elastically Shaped Aircraft Concept...][research_nguyennhan_jamesurnessr_2012]
- [Agility Quotient AQ][research_alberts_2014]
- [Red Teaming Agility Briefing Charts][research_hutchinson_2014]

### Propulsion and the Rest

The engine is a single **General Electric F404-GE-400 of the 16,000 pound class**, mounted in the fuselage
with **two side-mounted fixed-geometry inlets optimised for transonic performance**. Fixed geometry is the
correct choice for an aircraft whose supersonic excursions are incidental to its purpose, and it is one of
the places where the programme declined to spend money on a technology it was not investigating.

Maximum takeoff gross weight is 17,800 pounds with 4,000 pounds of fuel in two fuselage and two strake
tanks. Design symmetric load factors were
**8 g subsonic and 6.5 g supersonic at a manoeuvre design gross weight of 15,000 pounds**, and the record
notes that gross weights actually flown ranged from about 14,800 to 17,700 pounds, the upper figure being
**an eighteen percent increase over the manoeuvre design gross weight**.

The drag polar assumed for the sensitivity below is the ordinary parabolic one, and its maximum lift-to-drag
ratio has a closed form.

$$ C_D = C_{D_0} + k\,C_L^2, \qquad \left(\frac{L}{D}\right)_{\max} = \frac{1}{2}\sqrt{\frac{\pi A e}{C_{D_0}}}, \qquad C_L^{\mathrm{opt}} = \sqrt{\frac{C_{D_0}}{k}} $$

A drag polar is not published in a form that permits a clean lift-to-drag figure, but the sensitivity can
still be tabulated for an aspect ratio of 4.0 and an **assumed** span efficiency of 0.85.

| Assumed $C_{D_0}$ | Maximum lift-to-drag | At lift coefficient |
|---|---|---|
| 0.020 | 11.56 | 0.462 |
| 0.024 | 10.55 | 0.506 |
| 0.028 | 9.77 | 0.547 |

The more interesting question for this aircraft is the sustained load factor, where thrust equals drag in a
level turn.

$$ \frac{T}{W} = \frac{q\,C_{D_0}}{W/S} + \frac{k\,(W/S)\,n^2}{q} \quad \Longrightarrow \quad n = \sqrt{\frac{q}{k\,(W/S)}\left(\frac{T}{W} - \frac{q\,C_{D_0}}{W/S}\right)} $$

| Altitude | Sustained load factor at Mach 0.9 |
|---|---|
| Sea level | 10.66 |
| 20,000 ft | 8.17 |
| 40,000 ft | 5.46 |

**At sea level that exceeds the 8 g structural design limit**, on the assumed polar and at the manoeuvre
design weight, which means **the airframe rather than the engine is what binds low down**. It is a
consequence of the thrust-to-weight ratio computed at the top of the article exceeding unity at that weight.

**Ten to eleven is an unremarkable figure for a fighter-sized aircraft of this aspect ratio**, and the
X-29's aerodynamic interest was never in its cruise efficiency.

- [An Energy Approach to Climb Performance Estimation of a...][research_tamboli_1956]
- [Optimum Path of an Airplane -- Minimum Time to Climb][research_theodorsen_1959]
- [Evaluation of Energy Maneuverability Procedures in Aircraft...][research_johnson_1972]

### Instrumentation

**Six hundred and ninety-one measured parameters were telemetered to the ground**, and the aircraft
**had no onboard recording capability at all**, which is a striking design decision and made the telemetry
link a single point of failure for the research product if not for the aircraft.

The ten-bit remote-unit pulse-code modulation system sampled **from 25 to 400 samples per second** depending
on the frequency range required, with fourteen selected parameters raised to 200 or 400. Those rates are
chosen against the same criterion that governs the flight control system, and the range from 25 to 400
samples per second corresponds to a usable band an order of magnitude wide.

$$ f_{\max} \leq \frac{f_s}{2} \quad \Longrightarrow \quad 12.5\ \mathrm{Hz} \leq f_{\max} \leq 200\ \mathrm{Hz} $$

**The structural modes the aeroservoelastic work needed to see lie inside that band**, which is why fourteen
parameters were raised to the top of it.

A constant-bandwidth frequency modulation system handled high-response acceleration and vibration data. The
**flight deflection measurement system** supplied the wing twist that the Southwell analysis depended on,
which makes it the instrument the keystone result rests on.

- [Diffuser Investigations in a Supersonic Wind Tunnel][research_diggins_1951]
- [Investigation of Discrepancies between Flight-Measured and...][research_segel_1952]
- [MEASUREMENTS WITH HONEYCOMBS IN THE FULL-SCALE AND IN THE...][research_knackstedt_1952]
- [STRUCTURAL CONSIDERATIONS OF PERFORATED MATERIALS USED IN...][research_cliett_1952]
- [TERRIER BOOSTER FLIGHT TEST NUMBER 5][research_jacobson_1952]
- [CONVOPLANE PRELIMINARY DESIGN STUDY, MODEL CONSTRUCTION, AND...][research_goodyearaerospacecorpakronoh_1958]
- [Flight Test Rotary Wing Manual][research_stange_1959]
- [Wind Tunnel Tests and Further Analysis of the Floating Wing...][research_fay_johnstone_1960]
- [Recent Flight Test Results of the Bell MW Rails Integrated...][research_mitchell_1961]
- [WS 107-1 Flight Test Working Group, Flight Test Report, Atlas...][research_generaldynamicsastronauticssandiegoca_1961]
- [WS 107A-1 Flight Test Working Group, Flight Test Report...][research_generaldynamicsastronauticssandiegoca_1961_b]
- [WS 107A-1 Flight Test Working Group Flight Test Report Atlas...][research_generaldynamicsastronauticssandiegoca_1962]
- [Army‐Navy Instrumentation Program RH‐1 Flight Test Results][research_niehaus_1962]
- [CORRELATION OF WIND TUNNEL BLOCKAGE DATA][research_czysz_1963]
- [PERFORMANCE FLIGHT TEST TECHNIQUES][research_godwin_frazier_1964]
- [DESIGN AND WIND TUNNEL TEST OF A MODEL HELICOPTER ROTOR...][research_ekquist_1965]
- [WIND TUNNEL TEST OF 1/7 SCALE MODEL OV-1][research_shepheard_1965]
- [FLIGHT TEST EVALUATION OF A DISTRIBUTED SUCTION HIGH-LIFT...][research_roberts_smith_1966]
- [SSLV-5 NO. 9 POST FIRING FLIGHT TEST REPORT FINAL EVALUATION...][research_martincodenverco_1966]
- [WIND TUNNEL INVESTIGATION OF AN ASPECT RATIO 10 TANDEM WING...][research_harry_trobaugh_1966]
- [Re-Entry Module/Adapter Interconnect Fairing Aerodynamic...][research_sheldon_1967]
- [INSPECTION, REPAIRS AND MODIFICATIONS, AND FLIGHT TEST OF THE...][research_irvine_1968]
- [ROTOR/WING SERIES VI WIND TUNNEL TEST 7-FOOT DIAMETER MODEL...][research_briardy_head_1968]
- [WIND TUNNEL INVESTIGATION OF THE THROTTLE FOR THE PROPOSED...][research_anderson_1968]
- [A Flight Envelope Expansion Study for the XH-51A Compound...][research_cruz_gorenberg_1969]
- [WIND TUNNEL TESTS OF A FREE-WING TILT-PROPELLER V/STOL...][research_strand_levinsky_1969]
- [Flight Test Results of a DAVI Isolated Platform][research_jones_1970]
- [Results of the ATA CAS Flight Test Program][research_borrok_rider_1970]
- [Air Force Flight Test Center Edwards Afb Ca 1970][research_airforceflighttestcenteredwardsafbca_1970]
- [An Investigation of Several Slotted Wind Tunnel Wall...][research_binion_tw_1971]
- [Four Prop Tilt Wing with Cyclic Pitch Propellers Results of...][research_kolesar_1971]
- [Full-scale flight test base pressure results for a blunt...][research_cassanto_1971]
- [Ground and flight test results for a decelerator towline...][research_councill_goble_1971]
- [Parafoil Wind Tunnel Tests][research_nicolaides_1971]
- [Wind Tunnel Test of the Conversion Process of a Folding...][research_magee_taylor_1971]
- [Flight Test Base Pressure Results at Hypersonic Mach Numbers...][research_cassanto_1972]
- [Longitudinal stability and control derivatives of a jet...][research_steinmetzgg_parrishrv_1972]
- [Dynamic Model Wind Tunnel Tests of a Variable-Diameter...][research_fradenburgh_murrill_1973]
- [Ground and flight test results for standard VOR and double...][research_sengupta_ferris_1973]
- [Study of Moire Measuring Techniques for Wind Tunnel Model...][research_abele_ruger_1973]
- [Turbulent heat transfer to a fin leading edge - Flight test...][research_lemmon_coleman_1973]
- [ABRES Flight Test Evaluation of RV Accuracy][research_burns_1974]
- [Flight Test Base Pressure Results for Sharp 8" Cones][research_batt_1974]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]
- [An Experimental Study of Several Wind Tunnel Wall...][research_binion_tw_1975]
- [Analysis of Flight Data for Deepwell System Installed in...][research_kuhn_1975]
- [Flight Test of an Integrated TDMA Data Link/Loran-C...][research_westbrook_1975]
- [Study of Moire Measuring Techniques for Wind Tunnel Model...][research_abele_sanlorenzo_1975]
- [A Control System for the Wind Tunnel Model of a...][research_reader_1976]
- [A Wind Tunnel Captive Aircraft Testing Technique][research_butler_1976]
- [Flight Test of a Digital Guidance and Control System in a...][research_osder_mossman_1976]
- [Sting Dynamics of Wind Tunnel Models][research_billingsley_1976]
- [A wind tunnel technique for determining stability derivatives...][research_bennettrm_farmermg_1977]
- [Aeroelastic Analysis for Rotorcraft in Flight or in a Wind...][research_johnsonw_1977]
- [Flight Planning and Conduct of the X-24B Research Aircraft...][research_armstrong_1977]
- [Flight test results for a separate surface stability...][research_jenksge_henryhf_1977]
- [High Altitude Altimeter Flight Test][research_martin_1978]
- [Model Diffuser Investigation for Propulsion Wind Tunnel 16T][research_david_hale_1978]
- [Wind Tunnel Results from a Nozzle Afterbody Test of A...][research_lucas_1978]
- [Wind Tunnel Wall Interference][research_dowell_bliss_1978]
- [Analysis of Low-Speed Helicopter Flight Test Data][research_tangler_1979]
- [Flight Test Results for an Advanced Technology Light Airplane][research_kohlman_1979]
- [Comparison of Wind Tunnel and Flight Test Measurements of...][research_dix_mattasits_1980]
- [Low order equivalent models of highly augmented aircraft...][research_shafermf_1980]
- [Validation of the Rotorcraft Flight Simulation Program C81...][research_vangaasbeek_1980]
- [Wind Tunnel Wall Interference][research_bliss_1980]
- [Flight experience with a remotely augmented vehicle flight...][research_petersenkl_1981]
- [Ring Laser Gyro Navigator Flight Test Results][research_bachman_1981]
- [Calibration and Performance of the AEDC/VKF Tunnel C, Mach...][research_strike_wt_1982]
- [Development of a simple, self-contained flight test data...][research_clarker_shaned_1982]
- [Flight Test Results of Five Input Signals for Aircraft...][research_plaetschke_mulder_1982]
- [Flight Test of Advanced Digital Control Concepts][research_whitbeck_smith_1982]
- [Digital electronic engine control system - F-15 flight test][research_barrett_rembold_1983]
- [F/A-18 inlet/engine compatibility flight test results][research_amin_hollweger_1983]
- [Flight Test Results for an Experimental GPS C/A-code Receiver...][research_campbell_lafrey_1983]
- [Flight test experience with pilot-induced-oscillation...][research_shafermf_smithre_1983]
- [Flight test experience with pilot-induced-oscillation...][research_shafermf_smithre_1984]
- [Prediction and occurrence of pilot-induced oscillations in a...][research_twisdale_kirsten_1984]
- [Comparison of analytical predictions and verification flight...][research_loser_1985]
- [A Flight Test Challenge Aeroassist for Reuseable, Space-Based...][research_ried_1986]
- [Aeronautical satellite data link concept, design, and flight...][research_anderson_hogle_1986]
- [Derivation of External Store Vibration Test Spectra From...][research_roberts_1986]
- [Propfan model wind tunnel aeroelastic research results][research_mehmedoral_1988]
- [Takeoff drag prediction for airbus A300-600 and A310 compared...][research_haftmann_debbeler_1988]
- [The NASA integrated test facility and its impact on flight...][research_mackallda_pickettmd_1988]
- [Estimation of longitudinal stability and control derivatives...][research_battersonjamesg_omarathomasm_1989]
- [Structures Flight Test Handbook][research_norton_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_c]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_d]
- [Analysis of aeroelastic and resonance responses of a wind...][research_whitlowwoodrowjr_bennettrobertm_1991]
- [GPS Interferometric Attitude and Heading Determination...][research_vangraas_braasch_1991]
- [Subsonic Wind Tunnel Testing Handbook][research_alexander_1991]
- [The role of the remotely augmented vehicle RAV laboratory in...][research_cohendorothea_lejeanetteh_1991]
- [ZEST Flight Test Experiments, Kauai Test Facility, Hawaii][research_cenkci_1991]
- [Design and utilization of a Flight Test Engineering Database...][research_knightondonnal_1992]
- [Differential GPS/inertial navigation approach/landing flight...][research_snyder_schipper_1992]
- [Wide-angle high-resolution line-imager prototype flight test...][research_neville_marois_1992]
- [Determination of the stability and control derivatives of the...][research_napolitanomarcellor_spagnuolojoellem_1993]
- [GPS for Precision Approaches Flight Test Results][research_braff_till_1993]
- [Air Force Test Pilot School Edwards Afb Ca 1993][research_airforcetestpilotschooledwardsafbca_1993]
- [Airship Applications of Modern Flight Test Techniques][research_brennan_mcdaniel_1994]
- [Interferometric GPS Flight Reference/Autoland System Flight...][research_vangraas_diggle_1994]
- [Artificial Intelligence Techniques for Flight Test Planning...][research_stottier_1995]
- [Developing Flight Test Techniques to Ensure Proper Rigging of...][research_traven_whitley_1995]
- [Estimation of the longitudinal and lateral-directional...][research_napolitanomarcellor_1996]
- [Flight Test Automation Options][research_carico_1998]
- [Naval Rotary Wing Aircraft Flight Test Squadron Flight Test...][research_mertaugh_1998]
- [Air Force Flight Test Center Edwards Afb Ca 2002][research_airforceflighttestcenteredwardsafbca_2002]
- [Flight Investigation of Prescribed Simultaneous Independent...][research_moestimothyr_smithmarks_2003]
- [Instrumentation for Wind Tunnel Transient Growth Studies][research_white_2004]
- [Wind Tunnel to Atmospheric Mapping for Static Aeroelastic...][research_heegjennifer_spaincharlesv_2004]
- [Base Pressure Computations of the DERA Generic Missile Wind...][research_despirito_2005]
- [Experimental Results from the Active Aeroelastic Wing Wind...][research_heegjennifer_spaincharlesv_2005]
- [Control Surface Interaction Effects of the Active Aeroelastic...][research_heegjennifer_2006]
- [Static Aeroelastic Scaling and Analysis of a Sub-Scale...][research_tingeric_lebofskysonia_2014]

- [THE AERODYNAMIC CHARACTERISTICS OF A 75-DEG SWEPT DELTA WING...][research_clark_spurlin_1962]
- [Aerodynamics of Finned Missiles at High Angle of Attack][research_oberkampf_nicolaides_1971]
- [Theoretical and Experimental Investigations of Vortex Lift...][research_theisen_scruggs_1973]
- [Investigation of Flying Qualities of Military Aircraft at...][research_johnston_ashkenas_1974]
- [Induced Side Forces on Bodies of Revolution at High Angle of...][research_wardlaw_andrewb_1975]
- [Hypersonic Viscous Shock Layer Calculation of Leeward...][research_adams_1977]
- [Strake-wing analysis and design][research_lamarje_1978]
- [The Influence of Aerodynamic Interference on High Angle of...][research_nelson_mouch_1978]
- [Application of the Estimation-Before-Modeling EBM System...][research_stalford_1979]
- [Hypersonic Wind Tunnel Study of a 15 deg-30 deg Half Angle...][research_richards_1979]
- [Recent theoretical developments and experimental studies...][research_lamarje_luckringjm_1979]
- [Control-system techniques for improved departure/spin...][research_luattnguyen_williampgilbert_1980]
- [Development of a vortex-lift-design method and application to...][research_lamarje_schemenskyrt_1980]
- [Influence of Pitching Moment Characteristics on Departure and...][research_bihrle_jr_1980]
- [Aerodynamic features of designed strake-wing configurations][research_lamarje_frinknt_1981]
- [Experimental and analytical study of the longitudinal...][research_lamarje_frinknt_1981_b]
- [Aerodynamic aspects of aircraft dynamics at high angles of...][research_orlikruckemann_1983]
- [Fundamental aerodynamic characteristics of delta wings with...][research_woodrm_millerds_1985]
- [High angle-of-attack calculations of the subsonic vortex flow...][research_almosnino_1985]
- [Recent computational fluid dynamics works about high angle of...][research_fujii_1985]
- [Spiral vortex flow over a swept-back wing][research_poll_1986]
- [Calculation of aerodynamic characteristics at high angles of...][research_lancedward_tsengjb_1987]
- [Spanwise pressure distribution on delta wing with...][research_reddy_1987]
- [Vortex influence on oscillating airfoils at high angle of...][research_favier_maresca_1987]
- [Influence of the aspect ratio on the aerodynamics of the...][research_zohar_erel_1988]
- [LDV surveys over a fighter model at moderate to high angles...][research_sellerswilliamliii_meyersjamesf_1988]
- [Leading edge vortex dynamics on a pitching delta wing][research_lemaysp_batillsm_1988]
- [Vortex filament model of the wake behind a missile at high...][research_vantuyl_1988]
- [Wind-tunnel investigation of the forebody aerodynamics of a...][research_banksdanielw_1988]
- [Knowledge-based system of supermaneuver selection for pilot...][research_chin_1989]
- [Numerical simulation of the effects of variation of angle of...][research_ekaterinarisja_schifflewisb_1990]
- [In-flight leading-edge vortex flow-field survey measurements...][research_richwinedavidm_fisherdavidf_1991]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]
- [High angle of attack aerodynamics][research_stollery_1992]
- [In-flight leading-edge extension vortex flow-field survey...][research_davidmrichwine_davidffisher_1992]
- [High Angle of Attack Aerodynamics. By J. R OM . Springer...][research_smith_1993]
- [High Angle of Attack Missile Aerodynamics][research_dexter_1993]
- [Instantaneous topology of the unsteady leading-edge vortex at...][research_magness_robinson_1993]
- [Three-dimensional boundary layer and vortex wake over a cone...][research_menet_menart_1993]
- [Flight evaluation of pneumatic forebody vortex control in...][research_walchlilawrencea_1994]
- [High angle of attack flying qualities criteria for...][research_wilsondavidj_citurskevind_1994]
- [Navy and the HARV High Angle of Attack Tactical Utility Issues][research_sternberg_traven_1994]
- [Numerical simulation of incidence and sweep effects on delta...][research_ekaterinarisja_schifflewisb_1994]
- [Side force augmentation at high angle of attack from...][research_cornelius_lucius_1994]
- [A Study of Asymmetric Vortex Shedding Behind Missiles at High...][research_orkwis_1995]
- [Delta wing vortex control via recessed angled spanwise blowing][research_johari_olinger_1995]
- [Nonlinear vortex flow control for high-angle-of-attack...][research_buffington_adams_1995]
- [Post Stall Control of Swept Wings][research_telionis_1995]
- [Design of Nonlinear Autopilots for High Angle of Attack...][research_menon_yousefpor_1996]
- [Simulation Study of VISTA/F-16 Maneuverability Enhancement...][research_mckeehen_cord_1997]
- [Application of CFD to High Angle of Attack Missile Flow Fields][research_sahu_heavey_2000]
- [Post Stall Flow Control Over Swept Wings][research_telionis_2001]
- [Technical Evaluation Report, Part A - Vortex Flow and High...][research_jamesmluckring_2003]
- [LDV Surveys Over a Fighter Model at Moderate to High Angles...][research_sellerswilliamliii_meyersjamesf_2004]

## The Flight Test Record

**Two aircraft flew, and they flew a divided programme.**

The first X-29A made its first flight on **14 December 1984** and carried the envelope expansion and the
performance work. The second flew from **1989** and carried the high angle of attack investigation. The
record of how many flights each made is not consistent across sources, and the disagreement is reported
rather than resolved in the source base below.

**The envelope expansion itself is precisely documented.** The primary record states that expansion of the
aircraft's one-g and manoeuvre flight envelopes **was completed over a two-year period in 84 flights**,
which is a slow rate by the standards of the aircraft in this series and an entirely appropriate one for an
airframe whose failure modes included a structural instability with no natural limit.

**The overall verdict in the primary literature is favourable and is stated without hedging.** Flight
results **confirmed the viability of the aircraft design**, good agreement with preflight predictions
**was obtained**, and the individual technologies' operational workability and performance
**were confirmed**.

### What Was Actually Measured

The research product divides into four measurable things, and it is worth separating them because they did
not all succeed equally.

- **The static loads distribution**, from four wing stations and the canard, with eighteen strain gauge
  bridges per station.
- **The structural dynamic characteristics**, from frequency-sweep vibration inputs.
- **The flight control system characteristics**, across three modes and two configurations.
- **The aerodynamic performance**, meaning the drag polar shape above minimum parasite drag.

**The drag polar work was compromised by instrumentation rather than by the aircraft.** Polar shape data
could only be obtained subsonically, because
**a lack of afterburner fuel flow instrumentation prevented the calculation of accurate afterburner thrust in supersonic flight**.
Further difficulties arose in the angle-of-attack calibration and from manoeuvre dynamics effects caused by
being off the optimum wing camber schedule. **The engine was not thrust-calibrated**, and a
thrust-calibrated engine was planned for the follow-on phase.

**That is an honest and unusual admission to find in a programme report**, and it means the aircraft's
supersonic drag, which is where the forward-swept wing's transonic argument would have been most directly
testable, was not measured during this phase at all.

## Comparison With Ground Prediction

**Four comparisons are available in the primary record and they do not all point the same way.**

### The Drag Polar Beat Its Prediction

**Induced drag levels were as much as twenty percent less than wind tunnel estimates**, particularly at lift
coefficients above 0.8, and the basic drag polar shapes **met or exceeded wind-tunnel-based predictions**.
Comparison with other contemporary fighters showed the X-29A to have the better overall polar.

**A twenty percent overprediction of induced drag by a tunnel is a large error in the conservative direction**,
and it is the kind of result that supports the configuration more strongly than a matching prediction would
have. The aircraft was better than the ground said it would be.

### The Divergence Boundary Was Worse Than Predicted

**Preliminary results indicated a lower divergence speed than predicted**, though the boundary was
**still outside the flight envelope**.

This is the finding that matters most and it deserves to be stated carefully.
**The prediction was optimistic about the single quantity the aircraft existed to demonstrate.** The margin
survived, the aeroplane was never in danger, and the technology was vindicated. But the ground analysis was
wrong in the direction that costs margin rather than the direction that wastes it, and the primary record's
own framing of the underlying risk anticipates exactly this.
**Errors in the predicted load distributions or stiffness characteristics could lead to greater load amplifications and a lower divergence boundary for a forward-swept-wing design.**

**The programme predicted its own failure mode correctly and then experienced a mild version of it.**

### The Canard Loads Were Worse Than Predicted

**Canard torsion loads were consistently higher than predicted at transonic Mach numbers**, especially at
high dynamic pressure, and were **highly sensitive to sideslip angle**. The record states plainly that
**the difference between the flight test data and the predictions is not fully understood** and was still
under investigation.

**That is the same surface whose divergence boundary was set by the control loop**, and it is the second
independent sign that the canard was the least well predicted part of the aircraft. The warning quoted
earlier, that any misprediction of the canard-wing interference could have a large influence on the load
distributions of both surfaces, turned out to be the right thing to have worried about.

### The Buffet and Control System Interacted

A separate body of the flight record concerns
**buffet-induced structural and flight control system interaction**, and an
**in-flight interaction of the canard and the flight control system** significant enough to be the subject
of its own report.

**An aeroservoelastic interaction is what happens when a structure and a control law that were designed separately meet.**
For an aircraft whose canard stiffness was partly supplied by its pitch loop, the appearance of one is close
to inevitable, and its appearance in the flight record is the clearest possible evidence that the structure
and the control law were a single system rather than two.

- [Wake Characteristics and Interactions of the Canard/Wing...][research_griffin_haerter_1983]
- [X-29 flight research program][research_putnamtw_1983]
- [The X-29 flight-research program][research_putnamtw_1984_b]
- [X-29 flight-research program][research_putnamtw_1984]
- [X-29 initial flight test results][research_ishmaelsd_wierzbanowskit_1985]
- [Flight testing the X-29][research_smithrogerse_schroederkurtc_1986]
- [X-29 Flight Test Program including wind tunnel and...][research_waggonereg_jennettla_1986]
- [X-29 flight - Acid test for design predictions][research_putnamtw_petersenkl_1986]
- [Analysis of lateral stability of X-29 drop model using system...][research_raneydavidl_1987]
- [Challenges in modeling the X-29 flight test performance][research_johnwhicks_jankania_1987]
- [Challenges in modeling the X-29A flight test performance][research_hicksjohnw_kaniajan_1987]
- [Flight test techniques for the X-29A aircraft][research_hicksjohnw_cooperjamesmjr_1987]
- [Preliminary flight assessment of the X-29A advanced...][research_hicksjohnw_mathenyneilw_1987]
- [X-29A flight control system performance during flight test][research_chinj_chaconv_1987]
- [X-29A forward-swept-wing flight research program status][research_trippenseegarya_luxdavidp_1987]
- [Effects of maneuver dynamics on drag polars of the X-29A...][research_hicksjohnw_moultonbryanj_1988]
- [High-alpha flight dynamics research on the X-29 configuration...][research_croommarka_whippleraymondd_1988]
- [Real-time flight test analysis and display techniques for the...][research_hicksjohnw_petersenkevinl_1988]
- [X-29A forward-swept-wing flight research program status][research_trippenseegarya_luxdavidp_1988]
- [Computational support of the X-29A Advanced Technology...][research_waggonereg_batesbl_1989]
- [Flight tests confirm X-29 technologies][research_hicksjohnw_mathenyneilw_1989]
- [Preliminary flight-determined subsonic lift and drag...][research_hicksjohnw_huckabinethomas_1989]
- [Real-time flight test analysis and display techniques for the...][research_hicksjohnw_petersenkevinl_1989]
- [Results of correlations for transition location on a clean-up...][research_goradiash_bobbittpj_1989]
- [X-29A aircraft structural loads flight testing][research_simsrobert_mccrossonpaul_1989]
- [An in-flight interaction of the X-29A canard and flight...][research_kehoemichaelw_bjarkelisaj_1990]
- [X-29 high angle of attack][research_ishmaelstephend_smithrogerse_1990]
- [Buffet induced structural/flight-control system interaction...][research_voracekdavidf_clarkerobert_1991]
- [X-29 Research Aircraft][research_x_29_research_1991]
- [X-29 vortex flow control tests][research_hancockregis_fullertongordon_1992]
- [Buffet-induced structural/flight-control system interaction...][research_voracek_clarke_1994]
- [X-29 flight control system Lessons learned][research_clarkerobert_burkenjohnj_1994]
- [X-29 High Alpha Test in the National Transonic Facility][research_underwoodpamelaj_owenslewisr_2003]
- [L1 Adaptive Control Augmentation System with Application to...][research_griffinbrianjoseph_burkenjohnj_2010]

- [An Introduction to the Problem of Wing Flutter][research_greene_1928]
- [Graphical Solution of the Bending-Aileron Case of Flutter][research_bergen_arnold_1940]
- [Three-Dimensional Wing Flutter Analysis][research_flax_1943]
- [Torsional and Aileron Flutter][research_krzywoblocki_1943]
- [The Flutter of a Uniform Cantilever Wing][research_goland_1945]
- [Flutter and oscillating air-force calculations for an airfoil...][research_garrickie_rubinowsi_1946]
- [Flutter and oscillating air-force calculations for an airfoil...][research_garrickie_rubinowsi_1946_b]
- [Once More - Single Degree of Freedom Flutter of an Aileron][research_abichandani_rosenberg_1952]
- [Single Degree of Freedom Flutter of an Aileron][research_runyan_cunningham_1952]
- [Note on the Use of Two-Dimensional Compressible Flow...][research_werdes_1953]
- [FLUTTER CHARACTERISTICS OF A T-TAIL][research_pengelley_wilson_1954]
- [NACA Conference on Aircraft Loads, Structures, and Flutter][research_naca_conference_1957]
- [TABULAR PRESENTATION OF SUPERSONIC FLUTTER TRENDS FROM PISTON...][research_weatherill_zartarian_1958]
- [HYDROFOIL FLUTTER PHENOMENON AND AIRFOIL FLUTTER THEORY...][research_henry_1961]
- [HYPERSONIC FLUTTER MODEL RESULTS AND COMPARISON WITH PISTON...][research_white_richardp_1961]
- [Wind Tunnel Tests and Further Analysis of the Floating Wing...][research_gabel_ricks_1961]
- [FLUTTER SIMULATION][research_kearns_1962]
- [Flutter Analysis of Supersonic Ring Wing][research_crimi_ordway_1962]
- [SUBSONIC FLUTTER OF PANELS ON CONTINUOUS ELASTIC FOUNDATIONS...][research_dugundji_dowell_1962]
- [Transonic flutter investigation of models of a proposed...][research_gurleyjrjr_ruhlincl_1962]
- [FLUTTER ANALYSIS OF A HYDROFOIL NEAR A FREE SURFACE][research_crimi_grace_1965]
- [LOCAL AERODYNAMIC PARAMETERS FOR SUPERSONIC AND HYPERSONIC...][research_olsen_1965]
- [THEORETICAL CONSIDERATIONS OF PANEL FLUTTER AT HIGH...][research_dugundji_1965]
- [Bending-torsional flutter of a swept wing in a highdensity...][research_herrmanng_nematnassers_1966]
- [Flutter studies of simplified component models of a...][research_abeli_ruhlincl_1966]
- [Modified-strip-analysis method for predicting wing flutter at...][research_yates_1966]
- [Timers for Ordnance Symposium Flutter Arming and Timing...][research_gratton_donahue_1966]
- [Bending-torsional flutter of a swept wing in a high-density...][research_prasad_nematnasser_1967]
- [PRELIMINARY PARAMETRIC STUDY OF THE FLUTTER ARMING PRINCIPLE...][research_gratton_1967]
- [DESIGN CRITERIA FOR THE PREDICTION AND PREVENTION OF PANEL...][research_lemley_1968]
- [A Non-Linear Solution to a Tab-Aileron Flutter Problem][research_dlbirdsall_1970]
- [Investigation of Helicopter Control Loads Induced by Stall...][research_arcidiacono_carta_1970]
- [Optimum Selection of Design Variable Increments to Improve...][research_rogers_1970]
- [A Comparison of Methods for the Analysis of Wing-Tail...][research_triplett_burkhart_1971]
- [F-5E Flutter Model Test Report. Phase I][research_kolar_lile_1971]
- [A Feasibility Study of Active Wing/Store Flutter Control][research_triplett_1972]
- [Selective reinforcement of wing structure for flutter...][research_cooperpa_stroudwj_1972]
- [Bending Flutter and Torsional Flutter of Flexible Hydrofoil...][research_besch_liu_1973]
- [Flutter-Like Oscillations of a Planing Plate][research_ogilvie_shen_1973]
- [The Evaluation of a Stall-Flutter Spring-Damper Pushrod in...][research_adams_1973]
- [Bending-torsional flutter of a cantilevered wing containing a...][research_feldt_herrmann_1974]
- [Flutter analysis of swept-wing subsonic aircraft with...][research_housnerjm_steinm_1974]
- [Finite element flutter analysis of multi-web wing structures][research_rao_1975]
- [A Parametric Survey of Hydrofoil Strut Flutter][research_besch_rood_1976]
- [Analysis of the Power Spectral Density of Tape Recorder...][research_law_1976]
- [Comparison of supercritical and conventional wing flutter...][research_farmermg_hansonpw_1976]
- [Design, Fabrication, Testing and Analysis of Torsion Free...][research_murphy_peloubet_1976]
- [Drag Effects on Wing Flutter][research_petre_ashley_1976]
- [Flutter and buckling of general laminated plates][research_sawyerjw_1976]
- [Minimum Mass Structures with Specified Natural Frequencies][research_miele_1976]
- [The design, analysis, and testing of a low-budget wind-tunnel...][research_boldingrm_stearmanro_1976]
- [Analytical Flutter Studies of a Subsonic, Actively...][research_lehman_stearman_1977]
- [Effect of Chordwise Forces and Deformations and Deformations...][research_boyd_1977]
- [Investigation of Torsion Free Wing Trend Flutter Models][research_yang_wan_1978]
- [On the Transonic-Dip Mechanism of Flutter of a Sweptback Wing][research_isogai_1979]
- [The solution of structural dynamics problems by the...][research_collings_tee_1979]
- [Flutter Analysis of a Two-Dimensional and...][research_yang_guruswamy_1980]
- [Transonic Flutter Analysis of a Rectangular Wing with...][research_eastep_olsen_1980]
- [Flutter Analysis of MBB A-3 Supercritical Airfoil in Small...][research_yang_striz_1981]
- [Prediction of transonic flutter for a supercritical wing by...][research_yatesecjr_wynneec_1981]
- [Transonic dip mechanism of flutter of a sweptback wing. II][research_isogai_1981]
- [Effect of Store Aerodynamics on Wing/Store Flutter][research_turner_1982_b]
- [Flutter and Oscillatory Pressure Tests on a 727 Aileron in a...][research_nagaraja_lakin_1982]
- [Prediction of transonic flutter for a supercritical wing by...][research_yates_wynne_1982]
- [Wing/control surface flutter analysis using experimentally...][research_turner_1982]
- [Effects of angle of attack on transonic flutter of a...][research_yates_wynne_1983]
- [Transonic flutter model study of a supercritical wing and...][research_ruhlin_rauch_1983]
- [An Experimental Investigation of Air Cushion Flutter Using a...][research_vorum_1984]
- [Finite Element Analysis of Nonlinear Oscillations and Flutter...][research_maewal_1984]
- [Highly Maneuverable Aircraft Technology HiMAT flight-flutter...][research_kehoemw_1984]
- [Measurement of transonic dips in the flutter boundaries of a...][research_persoon_horsten_1984]
- [Flutter clearance of the Schweizer 1-36 deep-stall sailplane][research_kehoemw_ellisonjf_1985]
- [A generalized mixed time integration program for structural...][research_coyette_1987]
- [Flutter clearance of the F-14 variable-sweep transition...][research_kehoemichaelw_1987]
- [Modern wing flutter analysis by computational fluid dynamics...][research_cunninghamherbertj_batinajohnt_1987]
- [Static aeroelastic effects on the flutter of a supercritical...][research_yatesecarsonjr_chulichuan_1987]
- [Structural dynamics research in a full-scale transport...][research_mccomb_hayduk_1987]
- [Announcement European forum on aeroelasticity and structural...][research_announcement_european_1988]
- [Effect of density ratio on binary wing flutter][research_niblett_1988]
- [Empirical Flutter Prediction Method][research_casey_1988]
- [Modern wing flutter analysis by computational fluid dynamics...][research_cunningham_batina_1988]
- [Recent Trends in Aeroelasticity, Structures and Structural...][research_simpson_1988]
- [Wing flutter calculations with the CAP-TSD unsteady transonic...][research_bennettrobertm_batinajohnt_1988]
- [Flutter Clearance of the F-18 High-angle-of-attack Research...][research_freudingerlawrencec_1989]
- [Flutter analysis of cantilever composite plates in subsonic...][research_lin_lu_1989]
- [Flutter analysis of composite panels using high-precision...][research_kuojiun_pongjeu_1989]
- [The flutter of a wing with an aileron in transonic flow][research_pushtaev_1989]
- [Wing-store flutter analysis of an airfoil in incompressible...][research_yang_zhao_1989]
- [Flutter Clearance of the F-14A Variable-Sweep Transition...][research_freudingerlawrencec_kehoemichaelw_1990]
- [Asymptotic theory of bending-torsion flutter of high aspect...][research_karpouzian_1991]
- [Finite element analysis of composite panel flutter][research_lee_cho_1991]
- [Finite element analysis of supersonic flutter of multibay...][research_shiau_chang_1991]
- [Influence of Structural and Aerodynamic Modeling on Flutter...][research_striz_1991]
- [Shape Sensitivity Analysis of Flutter Response of a Laminated...][research_kapania_bergen_1991]
- [Supersonic flutter analysis of clamped symmetric composite...][research_lee_cho_1991_b]
- [Subharmonic bifurcation analysis of wing with store flutter][research_yang_zhao_1992]
- [Evaluation and Extension of the Flutter-Margin Method for...][research_price_lee_1993]
- [Flutter analysis of cantilevered curved composite panels][research_pidaparti_1993]
- [Flutter analysis of stiffened laminated composite plates and...][research_liao_sun_1993]
- [Flutter calculations for fixed and rotating wings with...][research_nibbelinkbruced_petersdavida_1993]
- [Large-Amplitude Finite Element Flutter Analysis of Composite...][research_gray_mei_1993]
- [Supersonic flutter analysis of composite plates and shells][research_pidaparti_yang_1993]
- [Finite element flutter analysis of laminated composite panels][research_chowdary_parthan_1994]
- [Flutter clearance flight tests of an OV-10A airplane modified...][research_doggettrobertvjr_riverajoseajr_1995]
- [The role of the generalized inverse in structural dynamics][research_to_ewins_1995]
- [Unstructured Euler flutter analysis of two-dimensional...][research_pan_cheng_1995]
- [Improved Flight Test Procedures for Flutter Clearance][research_lindrickc_brennermartinj_1997]
- [Flutter Model Technology][research_busan_1998]
- [Real Time Predictive Flutter Analysis and Continuous...][research_farhat_1998]
- [CEAS/AIAA/ICASE/NASA Langley International Forum on...][research_woodrowwhitlowjr_emilyntodd_1999]
- [Real-Time Predictive Flutter Analysis and Continuous...][research_farhat_2000]
- [Robust Nonlinear Control of Stall and Flutter in Aeroengines][research_kokotovic_murray_2000]
- [Bifurcations of Control Systems with Application to Flutter][research_krener_2001]
- [Real-Time Predictive Flutter Analysis and Continuous...][research_farhat_2001]
- [Theoretical Prediction of Limit Cycle Oscillations in Support...][research_dowell_hall_2003]
- [System Identification Methods for Improving Flutter Flight...][research_klyde_harris_2004]
- [Extension of Flutter Boundaries Using In-Flight Receptance...][research_mottershead_cooper_2012]

## What the Data Changed

**The X-29's forward-swept wing was never adopted, and the aircraft's influence ran through everything except its most visible feature.**

No production aircraft has flown a forward-swept wing since. The configuration's aerodynamic case was real
and modest, its structural case depended on a technology that had other uses, and its practical
disadvantages at high angle of attack and in supersonic flight were never overcome. **The planform lost.**

**What won was everything the planform forced.**

- **Aeroelastic tailoring became ordinary.** The technique that kept the X-29's wing inside its
  boundary is now applied routinely to wings that are not forward-swept at all, for load alleviation,
  flutter margin and weight, and the design literature that supports it is large.
- **Flying a deeply unstable airframe became ordinary.** Thirty-five percent negative static margin was
  extreme in 1984 and the practice of designing around relaxed static stability is now unremarkable.
- **Real-time redundancy management became a recognised discipline.** The insight that failure
  detection and isolation must be fast compared with the airframe's own divergence time, rather than
  merely reliable, transfers to every unstable aircraft.

**The aircraft's most transferable finding is the one it did not set out to make**, namely that a structure
and a control law for an unstable airframe cannot be specified independently. The canard's divergence
boundary being set by pitch-loop stiffness is a small fact with a large generalisation behind it.

- [Minimum control power for VTOL aircraft stability augmentation][research_swaim_1970]
- [Comment on "Minimum Control Power for VTOL Aircraft Stability...][research_curtiss_1971]
- [Maneuver Load Control and Relaxed Static Stability Applied to...][research_anderson_berger_1973]
- [Status and trends in active control technology][research_rediessha_szalaikj_1975]
- [An analytical study of turbulence responses, including...][research_perrybiii_1976]
- [Effects of control laws and relaxed static stability on...][research_robertspa_swaimrl_1977]
- [Impact of CCV Requirements on Flight Control System Design][research_boudreau_1977]
- [Active controls in aircraft design][research_kurzhalspr_1978]
- [Accelerated development and flight evaluation of active...][research_accelerated_development_1979]
- [Control considerations for CCV fighters at high angles of...][research_nguyenlt_gilbertwp_1979]
- [Development of a low risk augmentation system for an energy...][research_sizlotr_bergra_1979]
- [Economic evaluation of flying-qualities design criteria for a...][research_sliwasm_1980]
- [Effects of displacement and rate saturation on the control of...][research_hansongd_stengelrf_1981]
- [Control law development for a close-coupled canard, relaxed...][research_kleinrw_lapinsm_1982]
- [Design, simulation and evaluation of advanced display...][research_kleinrw_hollisterwm_1982]
- [Methodology for determining elevon deflections to trim and...][research_perrybiii_1982]
- [Modal control of relaxed static stability aircraft][research_rooneyrh_chungjc_1982]
- [Piloted simulator evaluation of a relaxed static stability...][research_lapinsm_kleinrw_1982]
- [Effects of control saturation on the command response of...][research_hansongd_stengelrf_1983]
- [Extended flight evaluation of a near-term pitch active...][research_guinnwileya_willeycraigs_1983]
- [Demonstration of relaxed static stability on a commercial...][research_risingjj_daviswj_1984]
- [Development of an advanced pitch active control system and a...][research_guinnwileya_1984]
- [Development of an advanced pitch active control system for a...][research_guinnwileya_risingjerryj_1984]
- [Effects of displacement and rate saturation on the control of...][research_hanson_stengel_1984]
- [Transonic time responses of the MBB A-3 supercritical airfoil...][research_batina_yang_1985]
- [Control law synthesis for an airplane with relaxed static...][research_blight_gangsaas_1986]
- [Landing approach handling qualities of transport aircraft...][research_wilhelm_schafranek_1986]
- [Sensitivity method for integrated structure/active control...][research_gilbertmichaelg_1987]
- [Application of parameter estimation to highly unstable...][research_maine_murray_1988]
- [Tailless aircraft performance improvements with relaxed...][research_ashkenasirvingl_klydedavidh_1989]
- [Transonic aeroelasticity of fighter wings with active control...][research_guruswamy_tu_1989]
- [Equation decoupling - A new approach to the aerodynamic...][research_preissler_schaufele_1991]
- [Regulation of relaxed static stability aircraft][research_kwatny_bennett_1991]
- [Abstract model and controller design for an unstable aircraft][research_enns_ozbay_1992]
- [Intelligent Signal Processing for Active Control][research_ramamoorthy_1992]
- [Comment on 'Equation decoupling - A new approach to the...][research_naihong_yaohua_1993]
- [Evaluation of parameter estimation methods for unstable...][research_jategaonkar_thielecke_1994]
- [Active Control of Secondary Flow in Engine Inlets][research_sullivan_2002]

## The Run of Four Purchased Designations Ends Here

**The pattern named across the last four articles stops with this one, and the stopping is itself evidence.**

- **X-25**, a commercially available autogyro bought to investigate a rescue concept.
- **X-26**, a commercially available sailplane bought twice, for training and for quiet observation.
- **X-27**, a manufacturer's private-venture export fighter that was never built at all.
- **X-28**, a homebuilt sport flying boat bought off a private individual for five thousand dollars.
- **X-29**, an aircraft designed and built to answer a question that could not be answered any other
  way.

**Three of the first four already existed and were bought for properties they already had. The fourth never existed. The fifth had to be created.**

The X-29 is what the X-series was established for. A government agency identified a question, funded a
purpose-built aeroplane, built two of them, flew them for years, and published the result.
**That the series could still do this in 1984, after a decade in which the designation had been applied to catalogue purchases and unbuilt proposals, is a fact about the institution rather than about the aircraft.**

**This article does not claim the four before it were misuse.** Evaluating an existing aircraft against a
requirement is research and it produced answers. The observation is narrower.
**The designation had become capable of meaning either thing, and which one it meant in a given year depended on who was paying rather than on any property of the aircraft.**
That belongs with the evidence the closing article of this series assembles, and it now has a run of four
followed by a clean break behind it.

## The Contemporary Literature

The bodies of work above are the ones the argument sits inside.
**This section surveys what has happened since**, on the standing expectation that an article of this kind
should double as a review of the current literature.

**The short version is that the X-29's two answers went in opposite directions. The planform is a historical curiosity and the techniques it forced are now everywhere.**

### Aeroelastic tailoring outlived the wing that needed it

**Tailoring is now a design variable rather than a rescue.** The X-29 used bend-twist coupling to cancel a
destabilising aerodynamic coupling, which is the hardest case. Contemporary work uses the same mechanism for
gust load alleviation, for flutter margin, for manoeuvre load control and for structural weight, on wings
whose sweep creates no divergence problem at all.

**The optimisation framing is what changed.** The X-29's laminate was designed to satisfy a constraint.
Modern practice treats ply orientation as a continuous design variable inside a multidisciplinary
optimisation, which makes the question not whether a coupling is achievable but what it is worth.

- [Aeroelastic Tailoring of Helicopter Blades][research_cornette_kerdreux_2015]
- [Aeroelastic Tailoring of Transport Wings Including Transonic...][research_stanfordbretk_wiesemancarold_2015]
- [An analytical model for composite tubes with bend twist...][research_jonnalagadda_sawant_2015]
- [Finite element modeling and effects of material uncertainties...][research_murray_doman_2015]
- [Optimization of Tow-Steered Composite Wing Laminates for...][research_stodieck_cooper_2015]
- [A novel dynamic aeroelastic framework for aeroelastic...][research_werter_debreuker_2016]
- [Aeroelastic Tailoring of a Composite Forward-Swept Wing Using...][research_tian_yang_2016]
- [Bend-Twist Coupling Behavior of 10 MW Composite Wind Blade][research_kim_shin_2016]
- [On the use of bend twist coupling in full-scale composite...][research_das_kapuria_2016]
- [Static and Dynamic Aeroelastic Tailoring with Variable-Camber...][research_stanford_2016_b]
- [Trim and Structural Optimization of Subsonic Transport Wings...][research_stanford_jutte_2016]
- [Aeroelastic Tailoring and Active Aeroelastic Wing Impact on a...][research_alyanak_pendleton_2017]
- [Aeroelastic Tailoring of a Representative Wing Box Using...][research_stodieck_cooper_2017]
- [Aeroelastic tailoring of an NLF forward swept wing][research_wunderlich_dahne_2017_b]
- [Aeroelastic tailoring of high-aspect-ratio composite...][research_chen_han_2017]
- [Aeroelastic tailoring using crenellated skins-modelling and...][research_francois_cooper_2017]
- [Comparison of curvilinear stiffeners and tow steered...][research_stanford_jutte_2017]
- [Efficient Method for Aeroelastic Tailoring of Composite Wing...][research_yu_wang_2017]
- [Evolutionary-based aeroelastic tailoring of stiffened...][research_marques_natarajan_2017]
- [Multidisciplinary optimization of an NLF forward swept wing...][research_wunderlich_dahne_2017]
- [A beam finite element for analysis of composite beams with...][research_babuska_wiebe_2018]
- [An automated aeroelastic performance prediction method in...][research_li_wang_2018_b]
- [Load-dependent bend-twist coupling effects on the...][research_young_garg_2018]
- [Optimal Aero-Elastic Design of a Rotor with Bend-Twist...][research_mcwilliam_zahle_2018]
- [A robust and reliability-based aeroelastic tailoring...][research_othman_silva_2019]
- [An efficient implementation of aeroelastic tailoring based on...][research_li_gong_2019]
- [Design Methodology for Aeroelastic Tailoring of Additively...][research_opgenoord_willcox_2019]
- [High-Fidelity Vibration Analysis of Tapered Swept Tailored...][research_viglietti_zappino_2019]
- [Preliminary design of aeroelastically tailored wing box...][research_mihailaandres_rosu_2019]
- [Smart Rotor With Trailing Edge Flap Considering Bend Twist...][research_zhang_liu_2019]
- [The buckling of CFRP composite plates in compression and...][research_loughlan_2019]
- [Aeroelastic Tailoring for Gust-Energy Extraction][research_melville_bramesfeld_2020]
- [Aeroelastic Tailoring of a Forward-Swept Wing Using...][research_choi_lim_2020]
- [Aeroelastic tailoring method of tow-steered composite wing...][research_zhang_chen_2020]
- [Static and dynamic aeroelastic tailoring with composite...][research_bordogna_lancelot_2020]
- [Tightly coupled aeroelastic model implementation dedicated to...][research_kirsch_montagnier_2020]
- [Design and testing of aeroelastically tailored composite wing...][research_rajpal_mitrotta_2021]
- [Location effects on bend-twist coupling modes characteristic...][research_ying_liqiang_2021]
- [The interaction between active aeroelastic control and...][research_binder_wildschek_2021]
- [Aeroelastic Tailoring of the Next Generation Civil Tiltrotor...][research_marano_belardo_2022]
- [Analytical and experimental investigation of bend-twist...][research_fazeli_stokesgriffin_2022]
- [Application of Aeroelastic Tailoring for Load Alleviation on...][research_kruger_meddaikar_2022]
- [Design of bend-twist coupled rectangular composite beams...][research_cui_li_2022]
- [Optimum Design of UAV Wing Skin Structure with a High Aspect...][research_jang_ahn_2022]
- [Tailored twist morphing achieved using graded bend twist...][research_gu_taghipour_2022]
- [Bend-twist coupling effects on the cavitation behavior and...][research_liu_zhang_2023]
- [Compression buckling of elastically supported cylindrical...][research_ansari_zucco_2023]
- [Computationally efficient optimal design of hygrothermally...][research_shakya_padhee_2023]
- [Effect of Aeroelastic Tailoring Design on Wing Mode][research_he_wang_2023]
- [Enhancing delamination resistance with intralaminar stiffness...][research_liu_li_2023]
- [A study on interactive fiber rubber composite structures...][research_annadata_endesfelder_2024]
- [Aeroelastic Tailoring Framework of Pazy Wing With Variable...][research_ayaz_rasoolmemon_2024]
- [Aeroelastic tailoring for aerospace applications][research_najmi_khan_2024]
- [Aeroelastic tailoring of stiffened cantilever plate using...][research_fraihat_ajaj_2024]
- [Multidisciplinary optimization of high aspect ratio composite...][research_ahmadi_farsadi_2024]
- [Impact of material and geometrical parameters on the...][research_sharifi_vincenti_2025]
- [Multiscale modelling strategy for a novel wingbox structure...][research_miranda_li_2025]
- [Solution of Deformation of Bend-Twist Coupling Box Beam...][research_shao_sun_2025]
- [Critical buckling analysis and multi-objective optimal design...][research_cui_miao_2026]
- [Including strength constraints in the concurrent optimization...][research_vertonghen_irisarri_2026]
- [Mechanical characterization of bend-twist coupling behavior...][research_gonzalezmontijo_vanness_2026]
- [Structural Parameter Selection for Lightweight Composite...][research_zaw_baranovski_2026]

- [1408 A study on aerodynamic characteristics of a forward...][research_kohara_tomoeda_2016]
- [Composite stacking sequence optimization for aeroelastically...][research_bach_jebari_2016]
- [Dynamic characteristics analysis and flight control design...][research_wang_xu_2016]
- [Aerodynamic Analysis of Forward Swept Wing Using Prandtl-D...][research_nath_ana_2017]
- [Numerical study on influence of single control surface on...][research_wang_su_2017]
- [Composite material structure optimization design and...][research_rongrong_zhengyin_2018]
- [Numerical Study on Influence of Canard Height on Aeroelastic...][research_wang_su_2018]
- [Active aeroelastic wing application on a forward swept wing...][research_xue_ye_2019]
- [Aerodynamic Design and Testing of an Imbedded Forward Swept...][research_wadia_niedermeier_2019]
- [High-lift design for a forward swept natural laminar flow wing][research_keller_2019]
- [Static aeroelastic stiffness optimization of a forward swept...][research_dillinger_abdalla_2019]
- [The DLR TuLam project design of a short and medium range...][research_seitz_hubner_2019]
- [Forces and Moments Generated by Swept-Forward Grid Fins and...][research_debiasi_2020]
- [Research on Aerodynamic Characteristics of Forward-swept Wing...][research_xinbing_wen_2020]
- [Experimental and Numerical Studies on Static Aeroelastic...][research_ouyang_zeng_2021]
- [Influence of Basic Airfoil Layout on Aerodynamic...][research_junyi_xinbing_2021]
- [RANCANG BANGUN DAN ANALISA SISTEM KENDALI PROPORTIONAL...][research_alim_rizianiza_2021]
- [Aerodynamics of forward swept wing][research_sharif_abbas_2022]
- [Design optimization-under-uncertainty of a forward swept wing...][research_wauters_2022]
- [Supersonic Forward-Swept Wing Design Using Multifidelity...][research_kishi_kanazaki_2022]
- [Aerodynamics-based forward-swept wing structure optimization][research_li_2023]
- [Characteristics of Vortices around Forward Swept Wing at Low...][research_kanazaki_setoguchi_2023]
- [Design and Analysis of Wing Tip Twist on a Forward Swept Wing...][research_puthisikamani_sreenivasaraja_2023]
- [Aerodynamic Characteristics of Forward Swept Wing in Subsonic...][research_choosakngaongam_rapeeujjin_2024]
- [Investigating the Effects of Canard Dihedral Angle on the...][research_abed_alhamadani_2024]
- [Sliding Mode Flight Control Law Design Requirements for...][research_wang_sun_2024]
- [Enhancing aerodynamics performance A redesign approach for...][research_taufik_qasem_2025]
- [Global Aero-Structural Optimization of Composite...][research_wang_wang_2025_b]
- [Transition prediction including turbulent wedges for a...][research_fehrs_kaiser_2025]
- [Aerodynamic shape design of oblique wing for...][research_sun_zhang_2026]
- [Flight Dynamics Modeling and Sliding Mode Control Law Design...][research_liu_li_2026]
- [Supersonic Aerodynamic Enhancement of Swept-Forward and...][research_theerthamalai_ramanan_2026]
- [Vortex behavior over a tailless forward-swept wing with chine...][research_saheby_jialu_2026]

- [On divergence tests for composite hypotheses under composite...][research_martin_pardo_2017]
- [Interval analysis of the wing divergence][research_li_wang_2018]
- [Structural Optimization of Platelike Aircraft Wings Under...][research_townsend_picelli_2018]
- [Critical elastic parameters motivating divergence instability...][research_agwa_2019]
- [Divergent instability control of aeroelastic system driven by...][research_liu_2019]
- [New Mechanism of the Aeroelastic Divergence Onset][research_vedeneev_2020]
- [The Wing Divergence Problem in a Supersonic Gas Flow][research_kulikov_2020]
- [Aerodynamic Compensation Methods for Aeroelastic Divergence...][research_kornev_ambrozhevich_2021]
- [Stability/Instability Study and Control of Autonomous...][research_furtat_gushchin_2021]
- [Aeroelastic Structural Analysis to Calculate Symmetrical...][research_awadallaalihajahmed_2024]
- [Estimate Anti-symmetrical Divergence Modes of an Aircraft...][research_awadallaalihajahmed_2024_b]
- [Sentinels of change divergence in trophic niche of New...][research_wing_wing_2025]
- [Uncertainty Quantification via Hölder Divergence for...][research_zhang_li_2025]
- [Climate risk attention divergence and supply chain instability][research_hu_qiu_2026]
- [Distributionally robust optimal uncertainty quantification...][research_nguyen_lejeune_2026]
- [Experimental Study of Aeroelastic Divergence][research_mathur_huang_2026]
- [Impact of Control Surface Stiffness on Aeroelastic Divergence...][research_cestino_iannuzzo_2026]
- [The Bifurcation Index BFX A Composite Indicator of...][research_wilson_2026]

### Very flexible aircraft made the X-29's problem general

**The X-29 was a stiff aircraft with an inconvenient coupling. The contemporary problem is aircraft that are not stiff at all.**
High-aspect-ratio wings for efficiency, and the extreme case of solar-powered high-altitude platforms,
deform enough that the rigid-body and elastic degrees of freedom cannot be separated.

**That dissolves the distinction the X-29 was designed around.** Its divergence analysis treated the wing as
elastic and the aircraft as rigid, and the two were coupled only through the trim condition. The modern
formulation abandons the separation entirely, and body freedom flutter, which appears in the X-29's own
nomenclature list, is the canonical example.

- [Aerodynamic uncertainty propagation in bridge flutter analysis][research_mannini_bartoli_2015]
- [Effect of Flutter on the Multidisciplinary Design...][research_mallik_kapania_2015]
- [Epistemic uncertainty quantification in flutter analysis...][research_tang_wu_2015]
- [Mass Balancing Optimization Study to Reduce Flutter Speeds of...][research_li_pak_2015]
- [PrandtlPlane Joined Wing Body freedom flutter, limit cycle...][research_cavallaro_bombardieri_2015]
- [Structural Dynamic Analysis of a Hypersonic Composite Wing][research_zhang_wang_2015]
- [Bayesian analysis of the flutter margin method in...][research_khalil_poirel_2016]
- [Effect of Inertial and Constitutive Properties on...][research_richards_yao_2016]
- [Framework for sensitivity and uncertainty quantification in...][research_abbas_morgenthal_2016]
- [MATLAB-Based Flight-Dynamics and Flutter Modeling of a...][research_schmidt_2016_b]
- [Rotor Structural Loads Analysis Using Coupled Computational...][research_yeo_potsdam_2016]
- [Aeroelastic modeling and stability analysis A robust approach...][research_iannelli_marcos_2017]
- [Alternative Aerodynamic Uncertainty Modeling Approaches for...][research_wu_livne_2017]
- [Gust response and body freedom flutter of a flying-wing...][research_guo_jing_2017]
- [Identification of reduced-order model for an aeroelastic...][research_tang_wu_2017]
- [Nonlinear aeroelastic flutter and dynamic response of...][research_chen_li_2017]
- [Uncertain reduced-order modeling for unsteady aerodynamics...][research_chen_qiu_2017]
- [Active Suppression of a Sheet Flutter Using Fluid Suction and...][research_kohase_watanabe_2018]
- [Adaptive nonlinear optimal control for active suppression of...][research_tang_chen_2018]
- [Aeroelastic Optimization with an Economical Transonic Flutter...][research_bartels_stanford_2018]
- [An efficient method for nonlinear flutter of the flexible...][research_duan_zhang_2018]
- [Analysis of classical flutter in steam turbine blades using...][research_prasad_pesek_2018]
- [Assessment of Advanced Flutter Flight-Test Techniques and...][research_iovnovich_nahom_2018]
- [Assessment of body-freedom flutter for an unmanned aerial...][research_schafer_vidy_2018]
- [Prediction of Flutter Boundary Using Flutter Margin for The...][research_saputra_purabaya_2018]
- [Structural model with controls of a very light airplane for...][research_rogolski_olejnik_2018]
- [Study of Flexible Aircraft Body Freedom Flutter with...][research_iannelli_marcos_2018]
- [Variations of flutter mechanism of a span-morphing wing...][research_huang_yang_2018]
- [Aeroelastic panel flutter optimization of tow-steered...][research_fazilati_khalafi_2019]
- [Flutter and post-flutter constraints in aircraft design...][research_jonsson_riso_2019]
- [Frequency domain approach for probabilistic flutter analysis...][research_kumar_onkar_2019]
- [Improving the Flutter Margin of an Unstable Fan Blade][research_stapelfeldt_vahdati_2019]
- [Influence of stochastic perturbations of composite laminate...][research_nitschke_vincenti_2019]
- [Numerical Investigation into Flutter and Flutter-Buffet...][research_chiarelli_bonomo_2019]
- [Safe Flutter Tests Using Parametric Flutter Margins][research_roizner_raveh_2019]
- [Supersonic Flutter and Buckling Optimization of Tow-Steered...][research_guimaraes_castro_2019]
- [Tensor Product Model-based Robust Flutter Control Design for...][research_takarics_vanek_2019]
- [Whirl Flutter Analysis of a Free-Flying Electric-Driven...][research_hoover_shen_2019]
- [Wing Flutter Prediction by a Small-Disturbance Euler Method...][research_pan_liu_2019]
- [Aeroelastic Wing Planform Design Optimization of a Flutter...][research_hermanutz_hornung_2020]
- [Experimental Nonlinear Flutter Analysis of a Cantilever...][research_alizadeh_ebrahimi_2020]
- [Experimental Uncertainty Quantification of Flutter...][research_fang_cao_2020]
- [Flutter Onset Prediction Based on Parametric Model Estimation][research_gu_zhou_2020]
- [Full-Span Flying Wing Wind Tunnel Test A Body Freedom Flutter...][research_shi_liu_2020]
- [Modeling, Design, and Flight Testing of Three Flutter...][research_schmidt_danowsky_2020]
- [Weight optimization of a composite wing-panel with flutter...][research_shrivastava_tilala_2020]
- [Whirl Flutter Investigation of Hingeless Proprotors][research_yeo_kreshock_2020]
- [A successive robust flutter prediction technique for...][research_onkar_2021]
- [Flutter Analysis of a 3D Box-Wing Aircraft Configuration][research_ghasemikaram_mazidi_2021]
- [Prediction and active suppression of flutter in composite...][research_wang_chen_2021]
- [Robust active suppression for body-freedom flutter of a...][research_zou_mu_2021]
- [Sensitivity study and structural optimization of an aircraft...][research_kusni_widiramdhani_2021]
- [The Development of a Flight Test Platform to Study the Body...][research_shi_liu_2021]
- [Uncertainty analysis of bridge flutter considering dependence...][research_ji_zhao_2021]
- [Verification of a Body Freedom Flutter Numerical Simulation...][research_lei_guo_2021]
- [Closed-loop identification for aircraft flutter model...][research_jianhong_2022]
- [Flutter Boundary Prediction in a Global Stochastic Framework][research_gu_zhou_2022]
- [Flutter Modelling and Computation of a Flying Wing Aircraft][research_bai_xu_2022]
- [Flutter Predictions for Very Flexible Wing Wind Tunnel Test][research_goizueta_wynn_2022_b]
- [Nonlinear disturbance observer-based control of a structural...][research_mahgoub_elbadawy_2022]
- [Normal form transformations for structural dynamics An...][research_wagg_2022]
- [Optimization and comparison of strut-braced and high aspect...][research_sohst_lobodovale_2022]
- [Aircraft Flutter and Aerodynamic Work][research_kholodar_2023]
- [High-Fidelity Aerostructural Optimization with a...][research_gray_riso_2023]
- [High-Fidelity Gradient-Based Wing Structural Optimization...][research_jonsson_riso_2023]
- [Layup optimization of tow-steered composite laminates for...][research_khajah_natarajan_2023]
- [Nonlinear stochastic flutter analysis of a...][research_hao_ma_2023]
- [Numerical Analysis of Glauert Inflow Formula for Single-Rotor...][research_dodic_krstic_2023]
- [A Study on the Surrogate-Based Optimization of Flexible Wings...][research_lunghitano_afonso_2024]
- [Active aeroelastic flutter control of supersonic smart...][research_moreira_moleiro_2024]
- [Application of a Modal Parameter Identification Method Based...][research_wang_2024_b]
- [Body-freedom flutter analysis and flight test for a...][research_zou_huang_2024]
- [Flutter margin research based on system stability analysis...][research_li_zhou_2024]
- [Probabilistic prediction of coalescence flutter using...][research_chajjed_khalil_2024]
- [Structural Dynamic Response Reconstruction Based on Recurrent...][research_wang_song_2024]
- [Time-Domain Analysis of Body Freedom Flutter Based on 6DOF...][research_ji_guo_2024]
- [Wind tunnel experiments of bending-torsion and body-freedom...][research_ang_leo_2024]
- [Application of Deep Learning to Identify Flutter Flight...][research_aboukebeh_gilpita_2025]
- [Breaking Through Flutter Barrier of Rigid-Elastic Coupling...][research_zou_huang_2025_b]
- [Experimental Nonlinear Modal Analysis of an F-16 Aircraft...][research_zhou_raze_2025]
- [Preliminary aeroelastic optimization of electric aircraft...][research_wang_liuxu_2025]
- [Research on Semi-active Suppression of Flutter in Robotic...][research_research_on_2025]
- [Studying body-freedom flutter mechanism via a rigid-elastic...][research_zou_huang_2025]
- [Theodorsen’s and Garrick’s Flutter Calculations Revisited][research_perry_2025]
- [Variable-order framework for aeroelastic flutter analysis of...][research_campagna_benedetti_2025]
- [A Lightweight Digital Twin Framework for Structural Dynamic...][research_ibrahim_2026]
- [Body-freedom flutter analysis of rigid-flexible coupled...][research_qian_gao_2026]
- [Flutter Boundary Prediction Based on Feature Extraction and...][research_wang_zhou_2026]
- [Nonlinear aeroelastic analysis and flutter control of...][research_zhao_liu_2026]
- [Nonlinear aeroelastic metastructure for wing flutter...][research_tian_wang_2026]
- [Parametric influences on the hypersonic two-degree-of-freedom...][research_hao_yu_2026]
- [Stability Analysis of Body-Freedom Flutter in Flying Wing...][research_ang_ng_2026]
- [Thermo-Aeroelastic Flutter Instability and Nonlinear...][research_qi_yuan_2026]
- [Tiltrotor Whirl Flutter Mitigation Through Active Mini-Tab...][research_adeyemi_bull_2026]

- [A Composite Method for Human Foot Structural Modeling][research_zhao_luximon_2015]
- [A New Hybrid Algorithm for Multi-Objective Robust...][research_cheng_zhou_2015]
- [Adjoint quasi-three-dimensional aerodynamic solver for...][research_elham_2015]
- [Advance ratio effects on the flow structure and unsteadiness...][research_raghav_komerath_2015]
- [Advanced Aerostructural Optimization Techniques for Aircraft...][research_zuo_chen_2015]
- [Aerodynamic Shape Optimization Investigations of the Common...][research_lyu_kenway_2015]
- [Aircraft wing structural design optimization based on...][research_yang_yue_2015]
- [Composite Structure Modeling and Analysis of Advanced...][research_mukhopadhyayvivek_sorokachmichaelr_2015]
- [Damage identification in aircraft composite structures A case...][research_katunin_dragan_2015]
- [Damage tolerance optimization of composite stringer run-out...][research_badallo_trias_2015]
- [Fatigue damage tolerance of two tapered composite patch...][research_wu_gunnion_2015]
- [Frequency and Time Domain Analysis of an Aeroelastic Wing...][research_chakravarthy_evans_2015]
- [Gradient-based Aerothermodynamic Optimization of a Hypersonic...][research_xia_chen_2015]
- [Multidisciplinary wing optimization of commercial aircraft...][research_wunderlich_2015]
- [On thermal instability of delaminated composite plates][research_nikrad_asadi_2015]
- [Pre-posterior optimization of sequence of measurement and...][research_goulet_kiureghian_2015]
- [Probabilistic Manufacturing Tolerance Optimization of...][research_bhachu_haftka_2015]
- [Reliability based optimization in aeroelastic stability...][research_suryawanshi_ghosh_2015]
- [Repair of damage in aircraft composite sound-absorbing panels][research_anoshkin_zuiko_2015]
- [Structural Optimization of Box Wing Aircraft][research_kalinowski_2015]
- [Structural response variability under spatially dependent...][research_sofi_2015]
- [The Effect of Environmental Flight Conditions on Damage...][research_synaszko_salacinski_2015]
- [Unscented Kalman filter with unknown input and weighted...][research_alhussein_haldar_2015]
- [A Sequential Robust Optimization Approach for...][research_xia_li_2016]
- [A method for nonlinear aeroelasticity trim and stability...][research_wang_zhu_2016]
- [A new filter-based pseudo-negative-stiffness control for...][research_gong_xiong_2016]
- [A variable-kinematic model for variable stiffness plates...][research_vescovini_dozio_2016]
- [Aerodynamic Optimization Based on Continuous Adjoint Method...][research_xu_xia_2016]
- [Aeroelastic analysis of CNT reinforced functionally graded...][research_song_zhang_2016]
- [Aeroelastic characteristics of magneto-rheological fluid...][research_asgari_kouchakzadeh_2016]
- [An efficient reanalysis assisted optimization for...][research_huang_wang_2016]
- [Computational analysis of damage in hybrid composite structure][research_had_ruzicka_2016]
- [Coupled adjoint aerostructural wing optimization using...][research_elham_vantooren_2016]
- [DAMAGE TOLERANCE EVALUATION OF AN AIRCRAFT SKIN STRUCTURE BY...][research_anon_2016_b]
- [Investigation on repairable damage tolerance for structural...][research_park_2016]
- [Multi-criteria optimization of an aircraft propeller...][research_schatz_hermanutz_2016]
- [Multi-fidelity wing aerostructural optimization using a trust...][research_elham_vantooren_2016_b]
- [Multipoint Aerodynamic Shape Optimization Investigations of...][research_kenway_martins_2016]
- [Non-linear dynamic instability analysis of laminated...][research_darabi_ganesan_2016]
- [Online structural damage identification technique using...][research_sen_bhattacharya_2016]
- [Parametric model reduction for aeroelastic systems Invariant...][research_kim_2016]
- [Piezoelectric energy harvester composite under dynamic...][research_akbar_curielsosa_2016]
- [Preface to the special issue on “Recent developments in...][research_luongo_casciati_2016]
- [Stability analysis of a combined direct variable structure...][research_stefanello_grundling_2016]
- [Structural analysis of composite components considering...][research_mayer_prowe_2016]
- [Supply Chain Network Design under Demand Uncertainty and...][research_qiu_wang_2016]
- [A reduced order state space model for aeroelastic analysis in...][research_marqui_bueno_2017]
- [Aerodynamic shape optimization of an airliner elastic wing][research_navratil_2017]
- [Aerodynamic wing shape optimization based on the...][research_zhang_rizzi_2017]
- [Aeroelastic Analysis of Deployable Wing using Reduced Order...][research_otsuka_makihara_2017]
- [Aeroelastic Optimization Design for High-Aspect-Ratio Wings...][research_xie_meng_2017]
- [Aeroelastic Optimization of High-Speed Tiltrotor Wings with...][research_kambampati_smith_2017]
- [Application of the adjoint optimisation of shock control bump...][research_nejati_mazaheri_2017]
- [Concurrent wing and high-lift system aerostructural...][research_vandenkieboom_elham_2017]
- [Damage Diagnosis and Prognosis Methodology to Estimate Safe...][research_seshadri_krishnamurthy_2017]
- [Design, manufacturing and testing of a fibre steered panel...][research_khani_abdalla_2017]
- [Dynamic instability of variable stiffness composite plates][research_loja_barbosa_2017]
- [Fatigue life and damage tolerance of postbuckled composite...][research_davila_bisagni_2017]
- [Flight Path Optimization for Brownout Mitigation Using a...][research_alfred_celi_2017]
- [Inverse problems in structural safety analysis with combined...][research_karuna_manohar_2017]
- [Multi-Fidelity Multi-Objective Efficient Global Optimization...][research_ariyarit_kanazaki_2017]
- [Non-linear vibration and dynamic instability of...][research_darabi_ganesan_2017]
- [Nonlinear Static Aeroelasticity of High-Aspect-Ratio-Wing...][research_castellani_cooper_2017]
- [Nonlinear aeroelastic analysis of curved laminated composite...][research_an_khoo_2017]
- [On-Line Multi-Damage Scanning Spatial-Wavenumber Filter Based...][research_ren_qiu_2017]
- [Optimal design of variable stiffness laminated composite...][research_cagdas_2017]
- [Practical Methods for Aircraft and Rotorcraft Flight Control...][research_hodgkinson_2017]
- [Robust Optimization of Variable-Camber Continuous...][research_liu_bai_2017]
- [Structural Optimization of Aircraft Families with...][research_zou_yao_2017]
- [Wing Aerostructural Optimization Under Uncertain Aircraft...][research_bahamondejacome_elham_2017]
- [Wing aerostructural optimization using the Individual...][research_hoogervorst_elham_2017]
- [A Multi-Objective Robust Optimization Design for Grid...][research_jiang_li_2018_b]
- [A review of impact testing on marine composite materials Part...][research_sutherland_2018]
- [Aero structural optimization for sailplane wing in...][research_aero_structural_2018]
- [Aerodynamic Design of the Supersonic Aircraft Wing-Shape and...][research_li_bai_2018]
- [Airfoil Optimization Design Based on the Pivot Element...][research_liu_he_2018]
- [An efficient aerodynamic shape optimization of blended wing...][research_mohammadzadeh_sayadi_2018]
- [Analytical investigation on tire dynamics by rigid elastic...][research_liu_gao_2018]
- [Application of an Efficient Gradient-Based Optimization...][research_dababneh_kipouros_2018]
- [Constraint aggregation for large number of constraints in...][research_zhang_han_2018]
- [Design and Optimization of Wing Structure for a Fixed-Wing...][research_yu_2018]
- [Design, manufacturing, and testing of a variable stiffness...][research_rouhi_ghayoor_2018]
- [Dynamic instability of rotating doubly-tapered laminated...][research_seraj_ganesan_2018]
- [Dynamic instability of variable angle tow composite plates...][research_chen_nie_2018]
- [Efficient aeroelastic reduced order model with global...][research_chen_li_2018]
- [Model reference discrete‐time variable structure control][research_bartoszewicz_adamiak_2018]
- [Non-parametric shape optimization method for robust design of...][research_shimoda_nagano_2018]
- [Notch-induced anisotropic fracture of cold drawn pearlitic...][research_toribio_2018]
- [On manufacturing constraints for tow-steered composite design...][research_brooks_martins_2018]
- [On the influence of optimization algorithm and initial design...][research_yu_lyu_2018]
- [Reduced order model-based uncertainty modeling of structures...][research_song_mignolet_2018]
- [Robust combinatorial optimization under budgeted ellipsoidal...][research_kurtz_2018]
- [Robust combinatorial optimization with knapsack uncertainty][research_poss_2018]
- [Shape optimization of streamlined decks of cable-stayed...][research_cidmontoya_hernandez_2018]
- [Slender-Wing Beam Reduction Method for Gradient-Based...][research_stodieck_cooper_2018]
- [Virtual-command-based model reference adaptive control for...][research_zhang_yang_2018]
- [Wing aerostructural optimization with an analytical fuel...][research_jacome_elham_2018]
- [Wing twisting by elastic instability A purely passive approach][research_runkel_fasel_2018]
- [A Globalized Robust Optimization Approach of Dynamic Network...][research_zhao_sun_2019]
- [A Loose Coupling Method on the Twist Angle Optimization of...][research_zhao_cheng_2019]
- [A dual family of dissipative structure-dependent integration...][research_chang_2019]
- [A gradient-based aero-stealth optimization design method for...][research_li_bai_2019]
- [A multi-objective optimization framework for robust axial...][research_martin_hartwig_2019]
- [Aerodynamic optimization of civil aircraft with wing-mounted...][research_lei_bai_2019]
- [Aeroelastic analysis of CNT reinforced functionally graded...][research_swain_adhikari_2019]
- [Aeroelastic behavior of composite panels undergoing...][research_tsunematsu_donadon_2019]
- [Aeroelastic global structural optimization using an efficient...][research_li_daronch_2019]
- [Aeroelastic optimization of composite wings including fatigue...][research_rajpal_kassapoglou_2019]
- [Aeroelastic stability analysis of curved composite panels...][research_zhou_xu_2019]
- [Aerostructural Design Optimization Using a Multifidelity...][research_bryson_rumpfkeil_2019]
- [Approximate static aeroelastic analysis of composite wings][research_kobelev_2019]
- [Assessment of damage tolerance approaches for composite...][research_talreja_phan_2019]
- [Damage Tolerance Analysis of a Commercial Aircraft Structure][research_lee_2019]
- [Design of an Aircraft Wing Structure for Staticand Fatigue...][research_design_of_2019]
- [Design of fiber-reinforced variable-stiffness composites for...][research_shafighfard_demir_2019]
- [Effects of embedded perforation geometry on the free...][research_fazilati_khalafi_2019_b]
- [Evaluations of Coupled Transverse-Rotational Galloping of...][research_chen_li_2019]
- [High-fidelity aerostructural optimization of tow-steered...][research_brooks_martins_2019]
- [Hybrid approaches for aircraft primary structure repairs][research_wang_baker_2019]
- [Modal optimization approach for composite aeroelastic wing...][research_lv_lei_2019]
- [Multifidelity Optimization of Hybrid Wing Body Aircraft with...][research_reist_zingg_2019]
- [On aeroelastic stability of a piezo-MRE sandwich plate in...][research_soleymani_arani_2019]
- [On the accuracy of localised 3D stress fields in tow-steered...][research_patni_minera_2019]
- [Optimization of Airfoils along High-Aspect-Ratio Wing of...][research_nikolaev_2019]
- [Optimized design and analysis of composite flexible wing...][research_choi_park_2019]
- [Robust Adaptive Control with Control Structure Modification...][research_chen_wang_2019]
- [Robust optimization of a post-combustion CO2 capture absorber...][research_cerrillobriones_ricardezsandoval_2019]
- [Simulation of failure in laminated polymer composites...][research_furtado_catalanotti_2019]
- [Structural Optimization of Internal Structure of Aircraft...][research_de_jrad_2019]
- [Structural and aeroelastic analyses of a wing with tip rotor][research_zhang_zhao_2019]
- [Structural integrity assessment on cracked composites...][research_abdullah_akbar_2019]
- [Systematic multiparameter design methodology for an...][research_ochoa_groves_2019]
- [Thermal buckling optimization of variable angle tow fibre...][research_zhou_ruan_2019]
- [WITHDRAWN A robust and high-fidelity aerodynamic optimization...][research_li_bai_2019_b]
- [A critical review of available composite damage growth test...][research_molent_haddad_2020]
- [A cross-sectional aeroelastic analysis and structural...][research_feil_pflumm_2020]
- [A single-loop shifting vector method with conjugate gradient...][research_biswas_sharma_2020]
- [Adaptive yaw stability control by coordination of active...][research_ahmadian_khosravi_2020]
- [An sequential optimization and aeroelastic constraint...][research_zhang_wang_2020]
- [Deskos et al 2020][research_deskos_delcarre_2020]
- [Bend-free design of ellipsoids of revolution using variable...][research_daghighi_rouhi_2020]
- [Cross Validation of Aerodynamic Shape Optimization...][research_reist_koo_2020]
- [D and DD-drop layup optimization of aircraft wing panels...][research_shrivastava_sharma_2020]
- [Damage tolerance improvement of composite T-joint under...][research_hisada_minakuchi_2020]
- [Design considerations for variable stiffness, doubly curved...][research_thomas_hallett_2020]
- [Experiments on Flexible Filaments in Air Flow for...][research_silvaleon_cioncolini_2020]
- [Fiber-Optic Strain-Based Deflection and Twist Sensing for a...][research_penafrancisco_2020]
- [Gradient-Based Optimization of Solar-Regenerative...][research_mcdonnell_ning_2020]
- [On the design of structural wing members for an unmanned...][research_lanteigne_mcleod_2020]
- [Reconfigurable Nonlinear Dynamic Inversion for Attitude...][research_he_tan_2020]
- [Reduced order nonlinear aeroelasticity of swept composite...][research_farsadi_rahmanian_2020]
- [Simulation and Optimization of Takeoff Maneuvers of Very...][research_delcarre_palacios_2020]
- [Surrogate-Assisted Reliability Optimisation of an Aircraft...][research_wansaseub_sleesongsom_2020]
- [Unifying lamination parameters with spectral-Tchebychev...][research_serhat_bediz_2020]
- [Vertically Optimal Close Formation Flight Control Based on...][research_zhai_li_2020]
- [A novel method for estimating three-domain limit cycles in a...][research_wang_wu_2021]
- [A robust multi-objective optimization model for sustainable...][research_a_robust_2021]
- [Adjoint-Free Aerodynamic Shape Optimization of the Common...][research_li_zhang_2021_b]
- [Aero-structural optimization of supersonic wing under thermal...][research_guo_li_2021]
- [Aerodynamic shape optimization of racing car front wing][research_kalinowski_szczepanik_2021]
- [Aeroelastic Optimization Design of the Global Stiffness for a...][research_li_wan_2021]
- [Aeroelastic analysis of foam-filled composite corrugated...][research_zhuang_yang_2021]
- [Aeroelastic optimisation of manufacturable tow-steered...][research_wang_peeters_2021]
- [Aerostructural wing shape optimization assisted by...][research_bombardieri_cavallaro_2021]
- [Airfoil Analysis and Effect of Wing Shape Optimization on...][research_oza_vala_2021]
- [Data-based approach for wing shape design optimization][research_li_zhang_2021]
- [Design of buckling and damage resistant steered fibre...][research_xiao_harrison_2021]
- [Energy harvesting in variable stiffness composite...][research_shukla_pradyumna_2021]
- [Global Aerostructural Design Optimization of More Flexible...][research_wunderlich_dahne_2021]
- [Handling Measurement Delay in Iterative Real-Time...][research_gottumukkula_engell_2021]
- [Impact damage tolerance of energy storage composite...][research_pattarakunnan_galos_2021]
- [Linear aeroelastic analysis of cantilever hybrid composite...][research_camacho_akhavan_2021]
- [Momentless design of variable stiffness composite cylindrical...][research_fan_liu_2021]
- [Multi-Fidelity Optimization of a Composite Airliner Wing...][research_kafkas_kilimtzidis_2021]
- [Multi-objective frequency and damping optimization of...][research_pereira_sales_2021]
- [Natural laminar flow wing optimization using a discrete...][research_shi_mader_2021]
- [Nonlinear dynamics of flexible slender structures moving in a...][research_bulin_dyk_2021]
- [Production Design Analysis for Airfoil Shape Optimization][research_shinde_ohol_2021]
- [RANS-Based Aerodynamic Shape Optimization of a Wing...][research_chauhan_martins_2021]
- [Robust Combinatorial Optimization with Locally Budgeted...][research_goerigk_lendl_2021]
- [STRUCTURE POWER AIRCRAFT FUSELAGE 5774 TRAINER][research_pratama_2021]
- [Stress Analysis of Composite Aircraft Wing using Coupled...][research_jaffarsyedmohamedali_shahzatulsakinahbintiharon_2021]
- [Using blade element momentum methods with gradient-based...][research_ning_2021]
- [A 2D-sampling optimization method for buckling layup design...][research_jing_li_2022]
- [A Robust Bayesian Optimization Framework for Microwave...][research_dewitte_qing_2022]
- [A novel CS-RBFs-based parameterization scheme for the...][research_ding_xu_2022]
- [A reduced-order multi-body model with...][research_shan_bilgen_2022]
- [Aeroelastic Shape Control Using Fiber-Optic-Measured Strain...][research_simbuerger_raveh_2022]
- [Aeroelastic optimization design of composite materials blade...][research_zhang_wang_2022]
- [Aeroelastic shape optimization of solid foam core wings...][research_conlansmith_andreasen_2022]
- [Aerostructural Wing Optimization of a Regional Jet...][research_bons_martins_2022]
- [Analysis of Damage of Typical Composite/Metal Connecting...][research_wang_zhang_2022_b]
- [Building block design for composite metamaterial with an...][research_yu_wang_2022]
- [Correction RANS-Based Aerodynamic Shape Optimization of a...][research_chauhan_martins_2022]
- [Curvature-Constrained Layup Optimization to Improve Buckling...][research_niu_zhang_2022]
- [Damage behaviour and failure response of aircraft composite...][research_kalam_seshaiah_2022]
- [Design and optimization of variable stiffness piezoelectric...][research_cao_huang_2022]
- [Design of variable stiffness composites for maximum...][research_rashed_demir_2022]
- [Distributionally robust optimization for the closed‐loop...][research_ge_zhang_2022]
- [EXPERIMENTAL STUDY OF DAMAGE TO THE STRUCTURE OF COMPOSITE...][research_mingong_sun_2022]
- [Efficient aeroelastic wing optimization through a compact...][research_poole_allen_2022]
- [Exploration of the effect of wing component post-buckling on...][research_hahn_haupt_2022]
- [Features of fatigue and damage-tolerance tests of full-scale...][research_shcherban_sterlin_2022]
- [Fracture Analysis of a Laminated Window Structure][research_swab_patel_2022]
- [Improved multi-objective structural optimization with...][research_jelovica_cai_2022]
- [Low-Reynolds-number airfoil design optimization using...][research_li_zhang_2022]
- [Multipoint Aerodynamic Shape Optimization of a...][research_li_bai_2022]
- [Nonlinear Buckling and Postbuckling Analysis of Tow-Steered...][research_groh_wu_2022]
- [Normal stress flow evaluation in composite aircraft wing...][research_marin_graciani_2022]
- [Notch-type damage influence on the frequency of the principal...][research_derkach_zinkovskii_2022]
- [Reduction of free-edge effects around a hole of a composite...][research_kharghani_mittelstedt_2022]
- [Robust Multi-Objective Design Optimization of Water...][research_boindala_ostfeld_2022]
- [Robust stabilization under structured, possibly unstable and...][research_stefanovski_2022]
- [Robustness guarantees for structured model reduction of...][research_pandey_murray_2022]
- [Structurally Nonlinear Fluttering of a Three-Degree-Freedom...][research_hao_du_2022]
- [Two-Step Multi-Objective Reliability-Based Design...][research_sleesongsom_kumar_2022]
- [Uncertainty Preferences in Robust Mixed-Integer Linear...][research_bomze_gabl_2022]
- [Vortex structure of longitudinal scale flow in a 28-row...][research_han_zhang_2022]
- [A numerical study on the optimization of an airfoil design][research_feng_2023]
- [A two-level strategy for aeroelastic optimization of a 3D...][research_desouza_deleon_2023]
- [Adjoint-based robust optimization design of laminar flow wing...][research_chen_rao_2023]
- [Aerodynamic Optimization Design of Supersonic Wing Based on...][research_rao_shi_2023]
- [Aeroelastic modeling and analysis of honeycomb plates in...][research_ni_li_2023]
- [An Improved Multi-Objective Particle Swarm Optimization...][research_wu_sun_2023]
- [An improved reduced order model for bladed disks including...][research_schwerdt_maroldt_2023]
- [An insertability constraint for shape optimization][research_garner_wu_2023]
- [Causal-relationship-assisted shape design optimization for...][research_chen_dong_2023]
- [Comparison of Linear Flexible Aircraft Model Structures on...][research_juhasz_tischler_2023]
- [Efficient Aerostructural Wing Optimization Considering...][research_adler_martins_2023]
- [Fully Coupled Aeroelastic Stability Analysis of Adaptive...][research_parthivnshah_ericlblades_2023]
- [Geometrically Nonlinear Coupled Adjoint Aerostructural...][research_ma_abouhamzeh_2023]
- [Geometrically nonlinear effects in wing aeroelastic dynamics...][research_riso_cesnik_2023]
- [Moment-based distributionally robust joint chance constrained...][research_zang_wang_2023]
- [Multiscale Aeroelastic Optimization Method for Wing Structure...][research_li_yang_2023]
- [Robust multidisciplinary analysis and optimization for...][research_saporito_daronch_2023]
- [Robust optimization design of a flying wing using adjoint and...][research_shi_lan_2023]
- [Robust shape optimization under model uncertainty of an...][research_demir_gorguluarslan_2023]
- [Static Aeroelastic Optimization of High-Aspect-Ratio...][research_kilimtzidis_kostopoulos_2023]
- [Static aeroelasticity analysis of a rotor blade using a...][research_li_luo_2023]
- [Surrogate-based optimization on bump for shock wave/boundary...][research_tian_jin_2023]
- [Variable stiffness optimization algorithm for vibration...][research_jing_duan_2023]
- [Wing Shape Optimization Using FFD and Twist Parameterization][research_chauhan_praveen_2023]
- [A reduced-order method for geometrically nonlinear analysis...][research_liang_yin_2024]
- [Aero-Structural Design of Bridge Decks under Non-Synoptic...][research_verma_cidmontoya_2024]
- [Aeroelastic Stability and Design of Laminated Composite...][research_naresh_srinivas_2024]
- [Aeroelastic reduced-order modeling for efficient static...][research_li_kou_2024]
- [Aerostructural Optimization and Comparative Study of...][research_ma_abouhamzeh_2024]
- [Aerostructural Wing Optimization Using a Structural Surrogate...][research_fontana_piperni_2024]
- [Asynchronously H∞ Tracking Control and Optimization for...][research_yang_fu_2024]
- [Buckling optimization of variable-stiffness composite plates...][research_jing_duan_2024]
- [Computational and Experimental Analysis of Optimized Dual...][research_computational_and_2024]
- [Conical-shaped variable stiffness composite laminates Design...][research_sheikhi_rafieianamagh_2024_b]
- [Damage tolerance allowable calculation for the aircraft...][research_bogenfeld_freund_2024]
- [Design of manufacturable variable stiffness composite...][research_sheikhi_rafieianamagh_2024]
- [Design optimization for the entire aircraft structure of...][research_zhang_zhou_2024]
- [Design optimization of advanced tow-steered composites with...][research_luo_ferrari_2024]
- [Discrete and Continuous Adjoint-Based Aerostructural Wing...][research_tsiakas_trompoukis_2024]
- [Multidisciplinary analysis and structural optimization for...][research_benaouali_boutemedjet_2024]
- [Multiobjective aerostructural optimization for efficient...][research_kontogiannis_savill_2024]
- [Neural Autoencoder-Based Structure-Preserving Model Order...][research_lepri_bacciu_2024]
- [Nonlinear Dynamic Properties of Rigid Elastic Liquid Coupled...][research_li_yang_2024]
- [Optimized Design and Test of Geometrically Nonlinear Static...][research_li_qian_2024]
- [Optimizing fiber paths of tow-steered laminated composites...][research_shafei_faroughi_2024]
- [Possibilities of the finite element method for the analysis...][research_fedorenko_bondarenko_2024]
- [Post-buckling damage tolerance of welded omega-stiffened...][research_vandooren_bisagni_2024]
- [Probabilistic aeroelastic analysis of high-fidelity composite...][research_mcgurk_stodieck_2024]
- [RANS-Based Aerodynamic Shape Optimization of a Wing with a...][research_chauhan_martins_2024]
- [Reliability based optimisation of composite plates under...][research_ballesterclaret_coelho_2024]
- [STRUCTURAL MECHANICAL PROPERTIES AND MULTI-FIELD COUPLING...][research_wang_2024]
- [Static Aeroelastic Characterization of a Slender Straight Wing][research_rajamurugu_satyam_2024]
- [Surrogate-assisted constraint-handling technique for...][research_tsai_malak_2024]
- [Towards Structural and Aeroelastic Similarity in Scaled Wing...][research_filippou_kilimtzidis_2024]
- [Variable angle tow-steered curvilinear fibres-based rotating...][research_balaji_manickam_2024]
- [Wing optimization for static aeroelastic effect][research_sun_2024]
- [A DG-VLM framework for computational static aeroelastic...][research_campagna_gulizzi_2025]
- [A collision model for very flexible Cosserat rods and...][research_lohrer_krause_2025]
- [Aero-structural design of bridge decks under synoptic and...][research_verma_cidmontoya_2025]
- [Aerodynamic Shape Optimization of Wing Fuselage Intersection...][research_matos_marta_2025]
- [Airfoil Separation Constraint Formulation for Aerodynamic...][research_abdulkaiyoom_yildirim_2025]
- [BUCKLING ROBUSTNESS TO IMPERFECTIONS IN TOW-STEERED COMPARED...][research_ramroop_chinchamee_2025]
- [Broad Flight Envelope Acceleration Control Method of...][research_li_zheng_2025]
- [Buckling design optimization of tow-steered composite panels...][research_fina_bisagni_2025]
- [Buckling of variable angle tow steered laminates considering...][research_dutta_zhao_2025]
- [Computational Optimization of Flow Control over Aircraft Wing...][research_balasubramanian_jayanarasimhan_2025]
- [Design Optimization for SG6043 Airfoil for Using Finite...][research_design_optimization_2025]
- [Design of Variable-Stiffness Bistable Composite Laminates and...][research_xie_zhang_2025]
- [Efficient static aeroelastic wing optimization based on PSO...][research_bugala_payenskyy_2025]
- [Enhanced Airfoil Design Optimization Using Hybrid Geometric...][research_dinler_2025]
- [Enhancing airfoil design optimization surrogate models using...][research_hu_an_2025]
- [Evaluation of a Biomathematical Modeling Software Tool for...][research_devine_choynowski_2025]
- [Flexural free vibration behaviors of bimodular composite...][research_manickam_polit_2025]
- [Genetic algorithm optimized artificial immune system for...][research_kizildeniz_kiyak_2025]
- [Geometrically nonlinear high-fidelity aerostructural...][research_gray_kennedy_2025]
- [High angle-of-attack control of fixed-wing UAVs using...][research_li_hu_2025]
- [Low-Fidelity Static Aeroelastic Analysis for Jig Shape...][research_bugala_2025]
- [Multi-Point Optimization Design of Blended Wing Body Based on...][research_cui_he_2025]
- [Multidisciplinary aeroelastic optimization of high...][research_ziakos_kilimtzidis_2025]
- [Nonlinear Vibration Control of a Slender Beam with...][research_kuang_hu_2025]
- [Outcomes of Nonlinear Static Aeroelasticity for Wing Stress...][research_verri_desilvabussamra_2025]
- [STRUCTURAL MECHANICAL PROPERTIES AND MULTI-FIELD COUPLING...][research_wang_2025]
- [Sequential-based non-probabilistic reliability optimization...][research_wang_tian_2025]
- [Static Strength Evaluation of Composite Aircraft Wing for...][research_kumar_asha_2025]
- [Stochastic isogeometric analysis of the free vibration of...][research_negahbanb_khalafi_2025]
- [Structural Analysis and Control Optimization of Finger...][research_dong_2025]
- [Structural optimization of composite aircraft wing...][research_kano_ryuzono_2025]
- [The Benefit of Uncertainty Coupling in Robust and Adaptive...][research_bertsimas_na_2025]
- [Time-dependent reliability index for continuum structures...][research_zhan_li_2025]
- [Variable-fidelity optimization method with dynamic search...][research_tian_sun_2025]
- [Vibroacoustic model-based structure design optimization for...][research_ye_wang_2025]
- [Additive technologies in the polymer components manufacturing...][research_dzhurynskyi_2026]
- [Adjoint-Based Optimization of Overwing Nacelle and Wing...][research_yu_zhang_2026]
- [Aeroacoustic Optimizations of Internal Bay Cavity Flow...][research_lee_lua_2026]
- [Aerostructural Optimization of a Composite Low Reynolds Wing...][research_nikolaou_kilimtzidis_2026]
- [An Adaptive Coupled Frequency-Domain Model for Rigid Elastic...][research_guo_liu_2026]
- [Bayesian optimization framework for mixed-variable wing...][research_xu_zhang_2026]
- [CFD-Based Aerodynamic Shape Optimization and Comparative...][research_sumnu_2026]
- [Concurrent topology and anisotropy optimisation of...][research_urso_giunta_2026]
- [Coordinated robust optimization of building and surrounding...][research_zhao_li_2026]
- [Design and Optimization of PID Controller for Renewable...][research_ramdewangan_dewangan_2026]
- [Design for flexibility An adjustable robust optimization...][research_jagana_rajagopalan_2026]
- [Failure driven design for variable stiffness conformable...][research_daghighi_2026]
- [Feature-Driven Distributionally Robust Optimization for...][research_li_yang_2026]
- [Generalizable Multifidelity Aerodynamic Wing Shape Design...][research_yang_li_2026]
- [Generative AI-driven inverse design optimization of composite...][research_sun_chen_2026]
- [Integrated aerostructural design of composite aircraft using...][research_rashmikant_abe_2026]
- [Load Case and Constraint Downselection for Structural...][research_sheshanarayana_armstrong_2026]
- [Structural reduced-order model including geometrical...][research_an_zhang_2026]

### Control of unstable airframes became a solved problem and then a harder one

**Nothing in the contemporary literature would regard a thirty-five percent negative static margin as remarkable**,
which is the clearest measure of what the programme settled. What has replaced it is the question of doing
the same thing with guarantees.

**The X-29's control law was gain-scheduled, which is to say it was a family of linear designs stitched together.**
Contemporary work asks for robustness certificates across the whole envelope, for adaptive laws that retain
stability proofs, and for control allocation across redundant surfaces of the kind the X-29 had three of.
**The X-29 is still used as a benchmark for exactly this**, and the literature contains adaptive
augmentation studies that take its lateral and directional dynamics as the test case precisely because they
are difficult.

- [6-DOF Virtual Flight Control Simulation of Wire-Driven...][research_wang_wang_2015]
- [AEROELASTIC VIBRATIONS CALCULATION FOR WIND POWER PLANTS...][research_sineglazov_2015]
- [Adaptive aeroelastic control of nonlinear airfoil with...][research_zhang_marzocca_2015]
- [Aeroelastic Dynamic Response and Control of an Aeroelastic...][research_xu_gao_2015]
- [Aircraft Enroute Command and Control Comms Redesign...][research_callaway_2015]
- [Aircraft Flight Dynamics and Control][research_cochran_2015]
- [Airfoil Stall Suppression Using Feedback-Controlled...][research_rinoie_komuro_2015]
- [Application of H 2 /H ∞ and dynamic inversion techniques to...][research_lungu_lungu_2015]
- [Degree reduction of Bézier curves with restricted control...][research_gospodarczyk_2015]
- [Delay-range-dependent control of nonlinear time-delay systems...][research_rehan_iqbal_2015]
- [Design, Simulation, Implementation and Control of Digital...][research_design_simulation_2015]
- [Effect of storage time on the antinutritional factors...][research_hussain_anjum_2015]
- [Fixed-Wing Unmanned Aircraft In-Flight Pitch and Yaw Control...][research_yeo_atkins_2015]
- [FlightQM a multi-agent system for the analysis of flight...][research_fortis_fortis_2015]
- [Flow separation control on swept wing with nanosecond pulse...][research_zhao_li_2015]
- [Human Supervisory Control of Robotic Teams Integrating...][research_human_supervisory_2015]
- [L1 Adaptive Dynamic Inversion Controller for an X-wing...][research_jin_bifeng_2015]
- [Liposomal and edible coating as control release delivery...][research_alikhanikoupaei_2015]
- [Micro Vortex Generators for Boundary Layer Control Principles...][research_sun_2015]
- [Minimal-learning-parameter technique based adaptive neural...][research_xu_fan_2015]
- [Model reduction and MIMO model predictive control of gas...][research_wiese_blom_2015]
- [Modeling and Delay Propagation Analysis for Flight Operation...][research_zhang_zhu_2015]
- [Networked Control System Time-Delay Compensation Based on...][research_tian_li_2015]
- [Nonlinear Aeroelastic Analysis of Control Surface with...][research_morino_obayashi_2015]
- [Novel Control Effectors for Truss Braced Wing][research_whiteedwardv_kapaniarakeshk_2015]
- [Predictive Input Delay Compensation with Grey Predictor for...][research_kuzu_bogosyan_2015]
- [Recursive terminal sliding mode control for hypersonic flight...][research_wang_wu_2015]
- [Robust adaptive control scheme for uncertain non‐linear model...][research_wu_deng_2015]
- [Rotorcraft Flight Envelope Protection by Model Predictive...][research_bottasso_montinari_2015]
- [STAMP-based safety control approach for flight testing of a...][research_lu_zhang_2015]
- [Stability robustness of linear quadratic regulators][research_chen_holohan_2015]
- [Variable Reference Model for Model Reference Adaptive Control...][research_shiota_ohmori_2015]
- [mcfTRaptor Toward unobtrusive on-the-fly control-flow tracing...][research_tewar_myers_2015]
- [Adaptive Neural Control of Active Power Filter Using Fuzzy...][research_wang_fei_2016]
- [Adaptive Output-Feedback Control with Closed-Loop Reference...][research_qu_annaswamy_2016]
- [Adaptive control for a class of uncertain linear...][research_liu_ye_2016]
- [Aircraft Control Surface and Store Freeplay-Induced...][research_kholodar_2016]
- [An Efficient Finite Difference Method for The Time‐Delay...][research_jajarmi_hajipour_2016]
- [Analysis of Pilot-Induced-Oscillation and Pilot Vehicle...][research_mandal_gu_2016]
- [Digital memory look-up based implementation of sliding mode...][research_banerjee_kotecha_2016]
- [Flight Control Test of Quadrotor-Plane with Hybrid Flight...][research_kim_lee_2016]
- [Impacts of safety on the design of light remotely-piloted...][research_dirito_schettini_2016]
- [Influence of Attack Angle on Magnetohydrodynamic Flow Control...][research_masuda_shimosawa_2016]
- [Model reference adaptive control for nonlinear switched...][research_xie_zhao_2016]
- [Model reference tracking control of an aircraft a robust...][research_tanyer_tatlicioglu_2016]
- [Modeling and Incremental Nonlinear Dynamic Inversion Control...][research_difrancesco_mattei_2016]
- [Multiple model predictive control for large envelope flight...][research_tao_li_2016]
- [Novel delay-partitioning stabilization approach for networked...][research_li_bai_2016]
- [Open loop control of the five-axis missile and target flight...][research_kljajic_kostic_2016]
- [Optimal Control Framework for Cruise Economy Mode of Flight...][research_villarroel_rodrigues_2016]
- [Optimal control for discrete-time singular stochastic systems...][research_wang_liang_2016]
- [Parabolized Stability Equations Code with Automatic Inflow...][research_kosarev_seror_2016]
- [Robust Controller Design Based on L1 Adaptive Control Method][research_robust_controller_2016]
- [Robust isophase margin control of oscillatory systems with...][research_feliubatlle_2016]
- [Simple Adaptive Delta Operator Aircraft Flight Control for...][research_cano_sobel_2016]
- [Simulation of Laminar-Flow Compatible High-Lift Wing...][research_rizzetta_visbal_2016]
- [Stabilization of the PVTOL aircraft based on a sliding mode...][research_aguilaribanez_2016]
- [Subsumption architecture applied to flight control using...][research_oland_andersen_2016]
- [The Time-Delay Compensation Method for Networked Control...][research_tian_2016]
- [The self-tuning networked control system with online delay...][research_zuo_min_2016]
- [Time-Domain Stability Margin Assessment][research_clementskeith_2016]
- [A New Parabolic Sliding Mode Filter Augmented by a Linear...][research_aung_shi_2017]
- [A TIME-DELAY-DEPENDENT QUANTIZATION FEEDBACK CONTROL APPROACH...][research_chen_gao_2017]
- [A UAV Flight Control Algorithm for Improving Flight Safety][research_park_jung_2017]
- [Active coupling suppression and real-time control system...][research_miao_wei_2017]
- [Adaptive LFT control of a civil aircraft with online...][research_ferreres_hardier_2017]
- [Analysis of Airfoil Stall Control Using Dynamic Mode...][research_mohan_gaitonde_2017]
- [Autonomous Flight Envelope Estimation for Loss-of-Control...][research_schuet_lombaerts_2017]
- [Compensation of Time-Varying Delay in Networked Control...][research_yi_an_2017]
- [Cross-flow effects regarding laminar flow control within...][research_schueltke_stumpf_2017]
- [Designing and Modeling of Quadcopter Control System Using L1...][research_thu_gavrilov_2017]
- [Dynamics and control of separable coupled rigid body systems][research_khalaf_gan_2017]
- [Envelope-Aware Flight Management for Loss of Control...][research_didonato_balachandran_2017]
- [FAULT DIAGNOSIS OF AN AIRCRAFT CONTROL SURFACES WITH AN...][research_ogunvoul_balanchuk_2017]
- [FLOW CONTROL THROUGH VORTEX SHEDDING INTERACTION OF ONE...][research_payton_2017]
- [Flight Demonstration of Simple Preview Altitude Control...][research_sato_muraoka_2017]
- [Flight control for air-breathing hypersonic vehicles using...][research_cao_tang_2017]
- [Fly-by-Feel Control of an Aeroelastic Aircraft Using...][research_armanious_lind_2017]
- [Fractional delay compensated discrete-time SMC for networked...][research_shah_mehta_2017]
- [Fractional‐order multivariable composite model reference...][research_cheng_wei_2017]
- [Hovering control for quadrotor aircraft based on finite-time...][research_zhu_du_2017]
- [Immersion and invariance-based adaptive wing rock control...][research_lee_singh_2017]
- [In-flight tracking and vibration control using the DLR’s...][research_kufmann_brillante_2017]
- [Incremental Nonlinear Dynamic Inversion Control for Hydraulic...][research_huang_pool_2017]
- [Kalman-Filter-Based Adaptive Control Flight Testing on...][research_rafi_steck_2017]
- [L1 Adaptive Control Within a Flight Envelope Protection System][research_lee_snyder_2017]
- [Model Reduction Design of Multivariable Aircraft System Using...][research_park_oh_2017]
- [On the need of projections in input‐error model reference...][research_barabanov_ortega_2017]
- [Optimal Control Surface Mixing of a Rhomboid-Wing Unmanned...][research_miles_broughton_2017]
- [PI D tuning for Flight Control Systems via Incremental...][research_acquatellab_vanekeren_2017]
- [Reduced-Order Modeling of Unsteady Aerodynamics for an...][research_liu_huang_2017]
- [Robust Design of a Supersonic Natural Laminar Flow Wing-Body][research_quagliarella_iuliano_2017]
- [Robust Stability and Stabilization Of TCP‐Networked Control...][research_azadegan_beheshti_2017]
- [Robust launch vehicle’s generalized dynamic inversion...][research_ansari_bajodah_2017]
- [Run-Time Assurance and Formal Methods Analysis Nonlinear...][research_gross_clark_2017]
- [Stability and Control of Tailless Aircraft Using...][research_park_choi_2017]
- [Stabilization and Control of Chaos Based on Nonlinear Dynamic...][research_mukherjee_halder_2017]
- [Trirotor mechatronic design and reduction of dynamic model...][research_chabir_bouteraa_2017]
- [Variable Gain Output Feedback Control of A Networked...][research_suryendu_ghosh_2017]
- [A Learn-To-Fly Approach for Adaptively Tuning Flight Control...][research_jaredagrauer_2018]
- [A Model-Free Approach to Networked Control System with...][research_yaseen_bayart_2018]
- [Active Flow Vector Flight Control Using Only SJAs for a...][research_li_shen_2018]
- [Active suppression of freeplay aeroelastic vibrations of...][research_dul_2018]
- [Adaptive Control of Hypersonic Flight Vehicles With Limited...][research_liu_an_2018]
- [Adaptive Feedforward Control for Gust-Induced Aeroelastic...][research_wang_daronch_2018]
- [Adaptive Load Control of Flexible Aircraft Wings Using Fiber...][research_penafrancisco_martinsbenjamin_2018]
- [Adaptive switching control of uncertain fractional systems...][research_aghababa_2018]
- [Aeroelastic and Trajectory Control of High Altitude Long...][research_qi_zhao_2018]
- [Aircraft Damage Identification and Classification for...][research_zhang_devisser_2018]
- [An alternative stability proof for “Adaptive type-2 fuzzy...][research_izadbakhsh_kheirkhahan_2018]
- [Attitude Control of Aircraft Using Only Synthetic Jet...][research_li_zhang_2018]
- [Autonomous flight control of drone equipped with...][research_autonomous_flight_2018]
- [Barrier Lyapunov Functions and Constrained Model Reference...][research_lafflitto_2018]
- [Bidirectional Thrust Vectoring Control of a Rectangular Sonic...][research_lee_song_2018]
- [Constrained dynamical systems, robust model reference...][research_lafflitto_blackford_2018]
- [Decentralized Formation Flight via PID and Integral Sliding...][research_thien_kim_2018]
- [Deformation Control of Highly Flexible Aircraft in Trimmed...][research_yagil_raveh_2018]
- [Design for Robust Aircraft Flight Control][research_hess_peng_2018]
- [Design of L1 Adaptive Controller for Position Control of...][research_design_of_2018]
- [Distributed Propulsion Aircraft with Aeroelastic Wing Shaping...][research_nguyen_reynolds_2018]
- [Event-triggered reliable dissipative filtering for the delay...][research_aslam_chen_2018]
- [Experimental investigation of plasma vortex generator in flow...][research_ghayour_mani_2018]
- [Finite-time control for fuzzy networked systems with state...][research_yao_2018]
- [High AOA short landing robust control for an aircraft][research_tingting_aijun_2018]
- [Mid-wake wing tip vortex dynamics with active flow control][research_dghim_ferchichi_2018]
- [Modeling and Adaptive Flight Control for Quadrotor Trajectory...][research_bouadi_moracamino_2018]
- [Nonlinear control for underactuated multi-rope cranes...][research_lu_fang_2018]
- [Numerical Assessment of Leading- and Trailing-Edge Control on...][research_tormalm_leroy_2018]
- [Overlapping-Decomposition-Based Control Design for Switched...][research_yang_guan_2018]
- [Prediction of Control Effectiveness for a Highly Swept...][research_coppin_birch_2018]
- [Providing Flight-Path Control Bandwidth for Carrier Landings][research_hess_2018]
- [Reduced-order model for robust aeroelastic control][research_bruderlin_hosters_2018]
- [Robust Finite-Time Continuous Control of an Unsteady...][research_lee_singh_2018]
- [Stability and Control Investigations of Generic 53 Degree...][research_schutte_huber_2018]
- [Stability of Very Flexible Aircraft with Coupled Nonlinear...][research_changchuan_lan_2018]
- [Stabilization of nonlinear time-delay systems...][research_liu_zhang_2018]
- [Tentacle-Based Guidance for Entry Flight with No-Fly Zone...][research_liang_ren_2018]
- [Trajectory tracking control of thrust-vectoring UAVs][research_invernizzi_lovera_2018]
- [Transitional Flight of Tail-Sitter Unmanned Aerial Vehicle...][research_zhang_chen_2018]
- [Underactuated Stratospheric Airship Trajectory Control Using...][research_liu_sang_2018]
- [A Multi-loop Switching Controller for Aircraft Gas Turbine...][research_imani_montazerigh_2019]
- [A Physically Consistent Reduced Order Model for Plasma...][research_motta_malzacher_2019]
- [A Tutorial on Robust Control, Adaptive Control and Robust...][research_wei_2019]
- [A new model order reduction method for the design of...][research_prajapati_prasad_2019]
- [Abbott Alinity Control Module Software][research_abbott_alinity_2019]
- [Active Separation Control at the Pylon-Wing Junction of a...][research_schloesser_soudakov_2019]
- [Active flow separation control at the outer wing][research_rosenblum_vrchota_2019]
- [Aeroelastic Stability Analysis of Damaged High-Aspect-Ratio...][research_hoseini_hodges_2019]
- [An alternative stability proof for robust control of...][research_izadbakhsh_khorashadizadeh_2019]
- [Attitude control of tiltwing aircraft using a wing-fixed...][research_binz_islam_2019]
- [Back‐stepping sliding mode control of one degree of freedom...][research_zarei_arvan_2019]
- [Chaos control of nonlinear aeroelastic pitch plunge model][research_rao_padmanabhan_2019]
- [Combining Homogeneous High Order Sliding Mode and Nonlinear...][research_hamissi_bouzid_2019]
- [Database Building and Interpolation for an Online Safe Flight...][research_zhang_devisser_2019]
- [Delay-independent dual-rate PID controller for a packet-based...][research_alcaina_cuenca_2019]
- [Design and Flight Evaluation of Primary Control System for...][research_lavretsky_2019]
- [Determination of the flight dynamic envelope via stable...][research_yuan_li_2019]
- [Distributed Pressure Sensing Based Flight Control for Small...][research_wood_araujoestrada_2019]
- [Dynamic Contraction Method approach to digital longitudinal...][research_czyba_stajer_2019]
- [Effect of Aerodynamic Configuration Parameters on...][research_pan_huang_2019]
- [Embedded Flight Control Based on Adaptive Sliding Mode...][research_castaneda_gordillo_2019]
- [Flight Parameter Analysis of an L1 Adaptive Controller of a...][research_banerjee_2019]
- [From Theory to Flight Design and Application of Pitch Rate...][research_devi_2019]
- [In-flight Catering Service and Food Safety Implementation of...][research_kharisma_2019]
- [Input/output‐to‐state stability for switched nonlinear...][research_long_2019]
- [Integration of Phase Plane Flight Envelope Protections in...][research_gabrys_steffensen_2019]
- [L1 Adaptive Control for Switching Reference Systems...][research_snyder_zhao_2019]
- [Method of improving the functional dependability of the...][research_morozov_chermoshentsev_2019]
- [Neural-sliding mode approach-based adaptive estimation...][research_taimoor_aijun_2019]
- [Nonlinear 3D path following control of a fixed-wing aircraft...][research_galffy_bock_2019]
- [Nonlinear Lipschitz measure and adaptive control for...][research_aouiti_assali_2019]
- [Novel model reference adaptive control architecture using...][research_basuroy_bhasin_2019]
- [Numerical studies of active flow control on wing tip extension][research_vrchota_prachar_2019]
- [Operational Control in the Process Safety Assurance][research_karkoszka_2019]
- [Passive control of nonlinear aeroelasticity in hypersonic 3-D...][research_tian_li_2019]
- [Piecewise Polynomial Modeling for Control and Analysis of...][research_cunis_burlion_2019]
- [Position Tracking Control of Tailsitter VTOL UAV With Bounded...][research_wu_li_2019]
- [Positive filter synthesis for sliding‐mode control][research_trindadenascimento_cunha_2019]
- [Probabilistic Flight Envelope Estimation with Application to...][research_yin_chu_2019]
- [Real-Time Detection of an Aircraft Deep Stall and Recovery...][research_kolb_montagnier_2019]
- [Robustness Analysis of Flight Controllers for Fixed-Wing...][research_palframan_fry_2019]
- [Roll Control of Low-Aspect-Ratio Wings Using Articulated...][research_odonnell_mohseni_2019]
- [Stability Analysis for Incremental Nonlinear Dynamic...][research_wang_vankampen_2019_b]
- [Thrust Vectoring Control of Supersonic Jet Using Proportional...][research_lee_lee_2019]
- [Time-varying parameter model reference adaptive control and...][research_maity_hocht_2019]
- [Transient Aeroelastic Response Control of Shipboard Rotors...][research_han_yu_2019]
- [A Generalization for Model Reference Adaptive Control and...][research_a_generalization_2020]
- [A Method to Predict Random Time-Delay of Networked Control...][research_tian_2020]
- [A Sliding Mode Control Strategy with Repetitive Sliding...][research_gao_li_2020]
- [A Study of the Influence of Stochastic Fractional-Order Delay...][research_viola_oziablo_2020]
- [Adaptive Neural Networks-Based Dynamic Inversion Applied to...][research_wei_xu_2020]
- [Adaptive model predictive control with extended state...][research_zhang_sun_2020]
- [Aeroelastic Stability of Conventional and Tow-Steered...][research_guimaraes_silva_2020]
- [Agile Spacecraft Attitude Control an Incremental Nonlinear...][research_acquatella_chu_2020]
- [Aircraft Turbine Engine Automatic Control Based on Adaptive...][research_yepifanov_2020]
- [An Optimal Control Model of the Low-Carbon Supply Chain Joint...][research_yu_bai_2020]
- [Auto-tuning Smith-predictive Control of Delayed Processes...][research_gssssv_2020]
- [Automatic Control and Model Verification for a Small...][research_guo_zhou_2020]
- [Control of a Thrust-Vectoring CubeSat Using a Single...][research_biggs_livornese_2020]
- [Design of a Haptic Feedback System for Flight Envelope...][research_vanbaelen_ellerbroek_2020]
- [Digital Marketing Implementation in State Banking Industries...][research_sofiatiefi_2020]
- [Dynamic Stability Analysis of Aircraft Flight in Deep Stall][research_cunis_condomines_2020]
- [FPGA Implementation Framework for Low Latency Nonlinear Model...][research_patne_ingole_2020]
- [Flight Control Design for the Systematic Improvement of Ride...][research_rath_fichter_2020]
- [Flight Control Design using Incremental Nonlinear Dynamic...][research_ludenacervantes_choi_2020]
- [Flight Control for Very Flexible Aircraft Using Model-Free...][research_qi_zhao_2020]
- [Flight envelope estimation for helicopters under icing...][research_harno_kim_2020]
- [Handling-Qualities Perspective on Rotorcraft Load Alleviation...][research_saetti_horn_2020]
- [Improved fault diagnosis for aircraft flap control system...][research_chen_jing_2020]
- [Integrated supervised adaptive control for the more Electric...][research_cavallo_canciello_2020]
- [Joystick Steering in Recreational Boats Using L1 Adaptive...][research_bayless_voglewede_2020]
- [Loop-Separation Control for Very Flexible Aircraft][research_gonzalez_silvestre_2020]
- [Low-complexity hypersonic flight control with asymmetric...][research_an_guo_2020]
- [Modeling and Control Design of an Autonomous Hybrid...][research_abdalla_mansor_2020]
- [Nonlinear Dynamic Inversion Flight Control Design for Guided...][research_tipan_theodoulis_2020]
- [Nonlinear control of a pusher-configured small tail-sitter...][research_tsubakino_saito_2020]
- [Nonlinear robust neuro-adaptive flight control for hypersonic...][research_sachan_padhi_2020]
- [ON THE STABILITY OF COUPLED OSCILLATIONS OF THE ELASTIC...][research_kononov_lymar_2020]
- [On the effect of active flow control on the meandering of a...][research_dghim_ferchichi_2020]
- [Propeller influence on the aeroelastic stability of High...][research_teixeira_cesnik_2020]
- [Reusable and Reliable Flight-Control Software for a Fail-Safe...][research_latachi_rachidi_2020]
- [Revisiting the Fundamentals of Control Surface Reversal...][research_bueno_dowell_2020]
- [Sum-of-Squares Flight Control Synthesis for Deep-Stall...][research_cunis_condomines_2020_b]
- [Thrust vectoring control of vertical/short takeoff and...][research_wang_zhu_2020]
- [Timing precision in fly flight control integrating...][research_dickerson_2020]
- [Tube‐based robust economic model predictive control with...][research_sebghati_shamaghdari_2020]
- [A Nonlinear Optimal Control Approach for the Vertical...][research_rigatos_2021]
- [Adaptive Control Design for Multi-UAV Cooperative Lift Systems][research_webb_rogers_2021]
- [Adaptive preview control with deck motion compensation for...][research_bhatia_jiang_2021]
- [Aircraft control with the use of model reference adaptive...][research_kopecki_2021]
- [Aircraft system modeling under turbulence conditions and...][research_wang_wen_2021]
- [Angular acceleration estimation-based incremental nonlinear...][research_li_liu_2021_b]
- [Assessment of the efficiency of control of local budges][research_lisovyi_petrovska_2021]
- [Closed-Loop Reference Model Based Distributed Model Reference...][research_goel_roy_2021]
- [Control Theory Concepts Analysis and Design, Control and...][research_sleptsov_andrianova_2021]
- [DEVELOPMENT OF AN ACTIVE POWER FILTER BASED ON SLIDING MODE...][research_zhang_li_2021]
- [High Control Authority Three-Dimensional Aircraft Control...][research_xu_zha_2021]
- [Impulsive effect on fixed-time control for distributed delay...][research_miaadi_li_2021]
- [L1 Adaptive integrated guidance and control for flexible...][research_khankalantary_rezaeeahvanouee_2021]
- [L1 adaptive backstepping control for path-following of...][research_xu_oliveira_2021]
- [Manned Aircraft and Unmanned Aerial Vehicle Heterogeneous...][research_huo_duan_2021]
- [Method of predicting nonlinear pilot-induced oscillations due...][research_wang_lu_2021]
- [Networked control system time-delay compensation based on...][research_tian_2021]
- [Nonlinear Aeroelastic Simulations and Stability Analysis of...][research_hilger_ritter_2021]
- [Numerical Investigations for Passive and Active Flow Control...][research_zhao_zhao_2021]
- [Optimal Robust Control for Unstable Delay System][research_farkh_ksouri_2021]
- [Phase plane design based fast altitude tracking control for...][research_liu_dong_2021]
- [Pose and shape error control in automated machining of...][research_mei_wang_2021]
- [RELIABILITY OF EC 155 B1 AIRCRAFT COMPONENTS USING UPPER...][research_mahroni_2021]
- [Reinforcement-Learning-Based Adaptive Optimal Flight Control...][research_sun_vankampen_2021]
- [Research on control effectiveness of fluidic thrust vectoring][research_xue_yunsong_2021]
- [Review of flight simulation fidelity requirements to help...][research_white_padfield_2021]
- [Robust Model Reference Adaptive Control for Tail-Sitter VTOL...][research_ajel_humaidi_2021]
- [Robust Nonlinear Tracking Control for Unmanned Aircraft in...][research_kazarin_golubev_2021]
- [Robust adaptive finite‐time trajectory tracking control of a...][research_wu_zhang_2021]
- [Robust model reference adaptive backstepping sliding-mode...][research_ahmed_chen_2021]
- [Thrust Vectoring of a Fixed Axisymmetric Supersonic Nozzle...][research_resta_marsilio_2021]
- [6DOF nonlinear control loading system for a large transport...][research_amirahmadichomachar_kuppusamy_2022]
- [A control scheme for 360°thrust vectoring of cycloidal...][research_desai_halder_2022]
- [Active Flow Control Devices for Wing Load Alleviation][research_khalil_asaro_2022]
- [Adaptive Sampling for Interpolation of Reduced-Order...][research_goizueta_wynn_2022]
- [Aeroelastic Damping Estimation for a Flexible...][research_tsatsas_pontillo_2022]
- [Aircraft flight control using method of robustness aimed at...][research_wang_zheng_2022]
- [Amplitude Control of Stall-Induced Nonlinear Aeroelastic...][research_liu_sun_2022]
- [Analisis Umur Fatik Rangka Penyangga Aileron Flight Control...][research_kurniawan_2022]
- [Applying Model Order Reduction Algorithm for Control Design...][research_hai_2022]
- [Carrier-Based Aircraft Precision Landing Using Direct Lift...][research_luo_zhang_2022]
- [Central bank digital currency and flight to safety][research_williamson_2022]
- [Characteristics analysis and drive type selection for aileron...][research_radetskaya_2022]
- [Concave Bump for Impinging-Shock Control in Supersonic Flows][research_schulein_schnepf_2022]
- [Design and implementation of a low-complexity flight...][research_mirtaba_jeddi_2022]
- [Development of Discrete-Time Waterjet Control Systems Used in...][research_loghis_xiros_2022]
- [Discrete time partial‐state feedback model reference...][research_sang_zhang_2022]
- [Discussion of “Central bank digital currency and flight to...][research_carapella_2022]
- [Dynamic Event-Triggered Fault Detection for Discrete...][research_wang_hou_2022]
- [Dynamics and anti-disturbance control for tethered aircraft...][research_song_huang_2022]
- [Effects of anisotropic supports on the stability of...][research_defelice_sorrentino_2022]
- [Expandable Fully Actuated Aerial Vehicle Assembly Geometric...][research_shi_wang_2022]
- [Flight Dynamics and Control of an Unmanned Helicopter with...][research_dhiman_abhishek_2022]
- [Flight Envelope Prediction via Optimal Control-Based...][research_lu_hong_2022]
- [Flow separation control in a two-airfoil system by trailing...][research_parmar_singh_2022]
- [Formal Verification of Octorotor Flight Envelope Using...][research_heersink_sylla_2022]
- [In-Wing Pressure Measurements for Airspeed and Airflow Angle...][research_heinrich_vogt_2022]
- [Incremental Dual Heuristic Dynamic Programming Based Hybrid...][research_li_sun_2022]
- [Incremental nonlinear dynamic inversion based path‐following...][research_zhou_yang_2022]
- [Investigation of active flow control of jet deflection rate...][research_chi_gu_2022]
- [L1 Adaptive Control with Switched Reference Models...][research_snyder_zhao_2022]
- [Linear and Nonlinear Reduced Order Models for Sloshing for...][research_pizzoli_saltari_2022]
- [Model Reference Adaptive Control Based on Adjustable...][research_peng_chen_2022]
- [Model reference adaptive control A finite‐time approach][research_franco_rios_2022]
- [Model reference safety‐critical adaptive control for...][research_rong_huang_2022]
- [Nacelle intake flow separation reduction at cruise condition...][research_nambiar_pachidis_2022]
- [Networked control system stability analysis of pipeline...][research_rosa_susanto_2022]
- [Nonlinear Control of Aircraft Flight Dynamics Using...][research_tran_nguyen_2022]
- [Numerical study on strut insertion based thrust vectoring...][research_soundararajan_btn_2022]
- [Proportional Predictive Control of Networked Linear Switched...][research_qiu_deng_2022]
- [Rapid scan EPR Automated digital resonator control for...][research_oconnell_tseytlin_2022]
- [Regulator with reference model for u nmanned aircraft control...][research_regulator_with_2022]
- [Review on Model Based Design of Advanced Control Algorithms...][research_dini_saponara_2022]
- [Robust Tube-Enhanced Multi-Stage NMPC With Stability...][research_subramanian_abdelsalam_2022]
- [Robust flight control for a quadrotor under external...][research_benaddy_labbadi_2022]
- [The Construction of an Aircraft Control Multilayer Network...][research_ren_zhang_2022]
- [A hybrid robust model reference adaptive controller and...][research_evald_hollweg_2023]
- [Adaptive nonsingular fixed‐time control for hypersonic flight...][research_dong_li_2023]
- [Advanced Control Techniques for Unmanned Aerial Vehicle UAV...][research_advanced_control_2023]
- [Aircraft Wing Design for Extended Hybrid Laminar Flow Control][research_lobitz_traub_2023]
- [An Approach to Robust Control of Aircraft Motion][research_sushchenko_bezkorovainyi_2023]
- [An Enhanced Incremental Nonlinear Dynamic Inversion Control...][research_taherinezhad_ramirezserrano_2023]
- [Carrier Aircraft Flight Controller Design by Synthesizing...][research_jia_sun_2023]
- [Combined passive and active flow control for fixed-wing micro...][research_esmaeili_sousa_2023]
- [Coupled physics analysis of blended-wing-body underwater...][research_du_liu_2023]
- [Cross-Condition Fault Diagnosis of an Aircraft Environmental...][research_jia_ezhilarasu_2023]
- [DC motor control using model reference adaptive control][research_mosaad_2023]
- [Development of an Active Wingtip for Aeroelastic Control][research_toffol_ricci_2023]
- [Dynamic event-triggered delay compensation control for...][research_zhang_2023]
- [Efficient Flight Control by Use of EJ200 Thrust Vectoring][research_marecarios_montesbarrenetxea_2023]
- [Experimental investigation of synthetic jet control of wing...][research_experimental_investigation_2023]
- [Flight-Test Determination of Longitudinal Stability Using...][research_dias_2023]
- [Flow separation control in a two-airfoil system by trailing...][research_singh_parmar_2023]
- [Food safety management system certification - the...][research_food_safety_2023]
- [Fractional Sliding Mode Harmonic Control of an Active Power...][research_fei_hua_2023]
- [Implementation of a cascaded fuzzy sliding mode control of...][research_bessadet_2023]
- [Implementation of control technology for mechanical...][research_implementation_of_2023]
- [Impulsive control of unstable homogeneous positive systems of...][research_yang_zhang_2023]
- [Intelligent Global Fast Terminal Sliding Mode Control of...][research_yang_li_2023]
- [Learning quadrotor dynamics for precise, safe, and agile...][research_saviolo_loianno_2023]
- [Loss of control in flight accident case study icing-related...][research_bromfield_horri_2023]
- [Mathematical Modelling and Fluidic Thrust Vectoring Control...][research_tanveer_ahmad_2023]
- [Meta-Learning-Based Incremental Nonlinear Dynamic Inversion...][research_zhang_ran_2023]
- [Model complexity reduction and controller design for managed...][research_naderilordejani_besselink_2023]
- [Model reference adaptive control for nonlinear time‐varying...][research_lafflitto_2023]
- [Multihop networked control system considering communication...][research_ishii_2023]
- [Plasma Gurney Flap Flight Control at Low Angle of Attack][research_gu_ducvo_2023]
- [Proposed active flow control enabled hybrid tilt...][research_taubert_kay_2023]
- [Refinement of aircraft dynamics model and control system...][research_refinement_of_2023]
- [Runtime Assurance for Safety-Critical Systems An Introduction...][research_hobbs_mote_2023]
- [Safety flight envelope calculation and protection control of...][research_ma_chen_2023]
- [Scaling of sense organs that control flight Size and sensory...][research_simmons_2023]
- [Swept-Wing Active Flow Control with a Streamwise Row of...][research_mcfadden_brandt_2023]
- [The aerodynamic force estimation of a swept-wing UAV using...][research_uzun_bilgic_2023]
- [Thrust Vectoring Control of a Novel Tilt-Rotor UAV Based on...][research_yu_zhang_2023]
- [UAV control with active disturbance suppression for the...][research_uav_control_2023]
- [Adaptive Incremental Nonlinear Dynamic Inversion Control for...][research_park_ramirezserrano_2024]
- [Adaptive dynamic programming base on MMC device of a flexible...][research_yuan_wang_2024]
- [Adaptive predefined time neural filtered control design for...][research_wang_zhou_2024]
- [Aerodynamic Feedforward-Feedback Architecture for Tailsitter...][research_mcintosh_mishra_2024]
- [Aeroelastic vibrations control system of an unmanned aircraft][research_bondarenko_shkolnyi_2024]
- [Aggressive flight control of quadrotors using incremental...][research_wu_ye_2024]
- [Channel Switching Algorithms for a Robust Networked Control...][research_yang_2024]
- [Control System Design][research_kamaletdinova_romanov_2024]
- [Decoupled incremental nonlinear dynamic inversion control for...][research_salahudden_agrawal_2024]
- [Delayed Kalman filter for vision-based autonomous flight in...][research_gamagedara_lee_2024]
- [Dual Loop PI m PI n Control for an Aileron Positioning][research_degaspari_mantegazza_2024]
- [Enhancing Flow Separation Control Using Hybrid Passive and...][research_li_zhang_2024_c]
- [Experimental Investigation of the Active Flow Control over a...][research_mahdavizafarghandi_rezasoltani_2024]
- [Finite-Time Robust Flight Control of Logistic Unmanned Aerial...][research_ma_yu_2024]
- [Flight Testing Reinforcement-Learning-Based Online Adaptive...][research_konatala_milz_2024]
- [Full-Envelope Flight Control for Compound Vertical Takeoff...][research_kai_2024]
- [Geometrically Exact Aeroelastic Stability Analysis of...][research_shang_xia_2024]
- [HARDWARE IMPLEMENTATION OF AN ANALOG SPIKING NEURON WITH...][research_gnilenko_2024]
- [Hybrid Incremental Nonlinear Dynamic Inversion-based Control...][research_jeong_suk_2024]
- [Incremental Nonlinear Dynamics Inversion Control with...][research_kim_kim_2024]
- [Individual Blade Control Approach for Active Vibration...][research_hong_kim_2024]
- [Investigation of Hybrid Laminar Flow Control Capabilities...][research_karpuk_mosca_2024]
- [Multi-Outer Loop Dynamic Inversion Control An Application to...][research_axten_khamvilai_2024]
- [New geometric formulation for libration dynamics and...][research_shi_zhu_2024]
- [Nonlinear dynamic inversion based full envelope robust flight...][research_lang_li_2024]
- [Observer based nonlinear robust control for a flexible wing...][research_meng_fu_2024]
- [Observer-based adaptive robust control of aircraft antiskid...][research_wang_bai_2024]
- [On Resilience Guarantees by Finite-Time Robust Control...][research_hassan_selvaratnam_2024]
- [Optimal control for networked control system with Markovian...][research_wang_liu_2024]
- [Output feedback finite‐time boundary control for an unstable...][research_ghaderi_mojallali_2024]
- [Passive Aeroelastic Control of a Near-Ground Airfoil with a...][research_dhital_chouvion_2024]
- [Predefined time formation control for glide multiple aircraft...][research_ji_ke_2024]
- [Quadrotor Flight Envelope Protection with Trajectory and Yaw...][research_schieni_modasiya_2024]
- [Reducing flight risks through wildlife control John F...][research_uzun_2024_b]
- [Research on an Ice Tolerance Control Method for Large...][research_jiang_liu_2024]
- [Retrospective‐cost‐based model reference adaptive control of...][research_mohseni_bernstein_2024]
- [Robust Aeroelastic Response Estimation for Flexible Aircraft][research_mahapatra_halbe_2024]
- [Robust fault detection for switched systems with unstable...][research_liang_gao_2024]
- [Robust flight control based on a nonlinear-L1 adaptive...][research_li_he_2024]
- [Run Time Assurance for Spacecraft Attitude Control Under...][research_abate_mote_2024]
- [Self-organizing model reference adaptive control for aircraft...][research_gong_xu_2024]
- [The Impact of Flight Revenue and Control Loads on Flight...][research_the_impact_2024]
- [Triplex event-triggered recursive quantizer-based networked...][research_xiang_liu_2024]
- [Visualization and control of the free-flight transfer...][research_maruyama_ogino_2024]
- [A Heuristic Method to Improve the Robustness of Flight...][research_khusnulnovianingsih_2025]
- [Adaptive Fuzzy Nonsingular Fixed-Time Safety Flight...][research_wang_li_2025_c]
- [Adaptive Global Predefined-Time Control Method of Aerospace...][research_ding_shi_2025]
- [Adaptive Incremental Nonlinear Dynamic Inversion Control with...][research_park_ramirezserrano_2025]
- [Adaptive aircraft anti-skid braking control for runway...][research_liu_sun_2025]
- [Adaptive output tracking control with reference model system...][research_tao_2025]
- [Adaptive stabilization methodic of aircraft based on...][research_palkin_zenchenko_2025]
- [Aeroelastic stability of imperfectly supported...][research_kheiri_riazat_2025]
- [Anti-Windup Compensation for Nonlinear Dynamic Inversion...][research_soltani_turner_2025]
- [Attitude control of variable swept-wing aircraft A novel...][research_chen_meng_2025]
- [Composite Actuation and Adaptive Control for Hypersonic...][research_wei_cui_2025]
- [Computational Investigation of Fluidic Thrust Vectoring...][research_computational_investigation_2025]
- [Control of wing aeroelastic system in presence of wind gust...][research_mahmood_2025]
- [Delay compensation and stability analysis of networked...][research_mishra_yadav_2025]
- [Delay compensation strategy of networked control system based...][research_tang_2025]
- [Designing Multicopters with Active Attitude Control A Thrust...][research_zvonarev_leontev_2025]
- [Direct Force Control Technology for Longitudinal Trajectory...][research_bao_li_2025]
- [Distributionally Robust Model Predictive Control Closed-Loop...][research_mcallister_esfahani_2025]
- [Dynamic Inversion Flight Control Laws for Automatic...][research_saetti_2025_b]
- [Enhanced Control System for Thrust Vectoring Design...][research_ahmed_elbanna_2025]
- [Enhanced Three-Phase Inverter Control Robust Sliding Mode...][research_hoyos_candelobecerra_2025]
- [Event-Triggered Formation Control for High-Speed Flight...][research_li_li_2025]
- [Experimental research on three-axis control of flying-wing...][research_xu_feng_2025]
- [Flight Control Design for Rudder Failure Event on Cessna 172...][research_zuhri_2025]
- [Flight envelope constrained UAV shipboard landing control...][research_zhang_song_2025]
- [Flow Control Devices for Aeroacoustic Noise Suppression in...][research_lee_lua_2025]
- [Fragility-Rejection UAV Flight Control With Discrete-Time...][research_bu_luo_2025]
- [Hybrid-Triggered Control for Uncertain Networked Control...][research_narenshakthi_dharani_2025]
- [Incremental Nonlinear Dynamic Inversion Considering Centroid...][research_tang_gan_2025]
- [Kinematic Design and Control Analysis of A Subsonic Ejector...][research_oganyan_loginov_2025]
- [Latency Control in Real-Time Advertising Recommendation under...][research_latency_control_2025]
- [Linear parameter-varying model order reduction and control...][research_gao_jiang_2025]
- [NMPC-Based Unified Posture Manipulation and Thrust Vectoring...][research_salagame_pandya_2025]
- [Numerical investigation of vortex dynamics control in the...][research_wang_luo_2025_c]
- [Optimal Control of a Small Flexible Aircraft Using an Active...][research_wu_fu_2025]
- [Optimal Reaching Filter for Sliding Mode Control to Achieve...][research_lu_cao_2025]
- [Quadratic Programming Approach to Flight Envelope Protection...][research_autenrieb_2025]
- [RETRACTED ARTICLE Fractional-order fast terminal sliding mode...][research_xu_2025]
- [Research on Aircraft Control System Fault Risk Assessment...][research_shi_gao_2025]
- [Robust Cascaded Control with Antisaturation for Fixed-Wing...][research_xiong_xu_2025]
- [Robust iterative learning control for unstable MIMO systems][research_hodgins_freeman_2025]
- [Robust prescribed-time observer-based sliding mode control...][research_ma_liu_2025]
- [Robustness analysis of nonlinear filters for aircraft state...][research_elenchezhiyan_kumar_2025]
- [Rudderless flight control in flying wing aircraft core active...][research_zhijie_taiyu_2025]
- [Separation control applied to the turbulent flow around a...][research_wang_mallor_2025]
- [Soaring to New Heights Investigating the Aeroelastic...][research_smith_2025]
- [Stability of Gossamer Propellers for High-Altitude Ballooning][research_kenny_lawrence_2025]
- [Suppressing wing rock motion through differential equation...][research_mobayen_izadbakhsh_2025]
- [Suppression of flow separation of a high-lift wing with...][research_sun_bahri_2025]
- [Terrain Envelope for Landing Stability of a Multirotor UAV...][research_yin_ni_2025]
- [The SpHelico A coaxial drone inside a gimbal system...][research_flores_bazan_2025]
- [The usefulness of viscosity for the robustness of boundary...][research_bastin_coron_2025]
- [Trailing-Edge Beveling Effect on Passive Fluidic Thrust...][research_huang_gu_2025]
- [Transition Process Control of Tiltrotor Aircraft Based on...][research_liang_ye_2025]
- [Understanding High-Speed Aeroelastic Stability of a Gimballed...][research_akinwale_datta_2025]
- [$$\mathcal L _1$$ adaptive nonlinear dynamic inversion based...][research_guo_liu_2026_b]
- [A Run-Time Assurance Approach for Safe Control of a Quadrotor][research_ali_chen_2026]
- [A dual-network framework integrating adaptive data refinement...][research_zheng_wang_2026]
- [A neural connectivity atlas for fly flight control][research_dhawan_huang_2026]
- [A neuromorphic safety monitor for verifiable runtime...][research_kaczmarek_2026]
- [Active Flow Control for Enhanced High-Lift Aileron...][research_shmilovich_yadlin_2026]
- [Active flow control via valve system on hole-drawn array wing...][research_teimourian_altmeyer_2026]
- [Adaptive Augmentation of Incremental Nonlinear Dynamic...][research_wang_wei_2026]
- [Adaptive Runway Brake Control for Aircraft Based on Brake...][research_liu_li_2026_b]
- [Adaptive nonlinear aircraft pitch control via LS-SDRE][research_le_2026]
- [Advanced flight control Systems integration of AI and...][research_sultan_2026]
- [Aerodynamic Configuration and Stability Analysis of a...][research_li_shen_2026]
- [Aeroelastic suppression and stability tailoring mechanism of...][research_tian_li_2026]
- [An adaptive second‐order sliding mode control based on...][research_liu_huang_2026]
- [Combined Flow Control Method for Supersonic Jet Noise...][research_kabaliswaran_das_2026]
- [Comparative Analysis of Parametric Robustness of Nonlinear...][research_filimonov_filimonov_2026]
- [Design and Implementation of a Web-Based It-Enabled Internal...][research_design_and_2026]
- [Design and hardware implementation of a dynamically variable...][research_ming_hu_2026]
- [Design and implementation of real-time dihedral angle control...][research_cabuk_2026]
- [Development and application of a dynamic obstacle avoidance...][research_marquis_farhood_2026]
- [Digital implementation of the twisting controller using the...][research_mojallizadeh_2026]
- [Distributed Formation Control Method with Hierarchical Leader...][research_choi_choi_2026]
- [Duality Between Incremental Nonlinear Dynamic Inversion and...][research_pollack_theodoulis_2026]
- [Dynamic behavior and vibration control of a coupled...][research_zhang_zhao_2026]
- [Efficacy of Active Flow Control in Suppression of Wing Rock...][research_tahir_maqsood_2026]
- [Enhanced Pitch Angle of Aircraft System Using Fractional...][research_rahima_yassine_2026]
- [Experimental Closed-Loop Active Flow Control of Separation...][research_wang_wu_2026]
- [Finite-time control of multi-loop networked control systems A...][research_liu_liu_2026]
- [Flight Safety Control and Test Flight Experiments under...][research_zhou_gong_2026]
- [Fuzzy Extended-State Adaptive Sliding Mode Flight Control of...][research_deng_xu_2026]
- [Hybrid classical quantum ensemble learning for real-time...][research_khanal_adhikari_2026]
- [Improved active disturbance rejection-based full-envelope...][research_wang_liu_2026]
- [Improving Estimation and Control Accuracy of Underwater...][research_toan_2026]
- [Influence of shock control bump geometry in impinging shock...][research_bulut_schrijer_2026]
- [Integrated application of barrier function super-twisting...][research_tu_lu_2026]
- [LMI-based robust incremental nonlinear dynamic inversion...][research_tamaskani_alfi_2026]
- [Model Reference Adaptive Control for Wing-Rock Suppression in...][research_narayanan_kumar_2026]
- [Modeling and Control of Rigid Elastic Coupled Hypersonic...][research_li_xu_2026]
- [Neural Learning Control of Fighter Aircraft at...][research_yu_yu_2026]
- [Nonlinear Precise Tracking and Regulation for Unmanned...][research_hongyan_xiaoyong_2026]
- [Nonlinear geometric multivariable control for unmanned...][research_jianhong_yanxiang_2026]
- [Pneumatic-Based Approach for Flight Control][research_shmilovich_princen_2026]
- [Retraction Note Fractional-order fast terminal sliding mode...][research_xu_2026]
- [Separation control and lift enhancement of a conformal-slot...][research_du_zhao_2026]
- [Set‐Theoretic Safety Control With Formal Guarantees for...][research_liu_yang_2026]
- [Shock Control on a Double-Fuselage Aircraft with a Natural...][research_deng_yi_2026]
- [Study, Design, Modeling, Simulation, and Control Analysis of...][research_shneen_2026]
- [Synthetic jet-based active flow control for hydrodynamic...][research_liu_du_2026]
- [Three-Dimensional Guidance Law with LOS Angle and Attack Lead...][research_niu_li_2026]
- [Time-Varying Aerodynamic Model and Adaptive Control of the...][research_peng_cao_2026]
- [Understanding High-Speed Aeroelastic Stability of Swept-Tip...][research_delgado_datta_2026]
- [Understanding High-Speed Aeroelastic Stability of a Hingeless...][research_obrien_datta_2026]
- [WAIR Enabled by Thrust Vectoring Through Posture Manipulation...][research_krishnamurthy_ramezani_2026]
- [Yaw stabilization and maneuvering control of tailless flying...][research_zhang_he_2026]

- [A Study on Fly-By-Wire Helicopter Control Law Design using...][research_kim_choi_2015]
- [A performance optimization algorithm for controller...][research_zakharov_zattoni_2015]
- [AIRCRAFT CONTROL LAW RECONFIGURATION][research_kosyanchuk_selvesyuk_2015]
- [Actuator fault-tolerant control FTC design with post-fault...][research_chakravarty_mahanta_2015]
- [Adaptive compensation for infinite number of actuator...][research_wang_guo_2015]
- [Autonomous Formation Flight Control System Using In-Flight...][research_brodecki_subbarao_2015]
- [Body Freedom Flutter of a Blended Wing Body Model Coupled...][research_yingsong_zhichun_2015]
- [Constrained Information Pattern reconfiguration in Fault...][research_staroswiecki_amani_2015]
- [DESIGN OF FLY-BY-WIRE CONTROL SYSTEM ALGORITHMS FOR ADVANCED...][research_anikin_animitsa_2015]
- [Fault Tolerance System running on Distributed Multimedia][research_hong_ko_2015]
- [Fault‐tolerant control using command‐filtered adaptive...][research_xu_guo_2015]
- [Flight Evaluation of Fault-tolerant Control System Using...][research_tokunaga_masui_2015]
- [Learning Control Law of Mode Switching for Hypersonic...][research_jiao_jiang_2015]
- [Predator-prey biogeography-based optimization for parameters...][research_zhu_duan_2015]
- [Reconfiguration Criterion for Fault-Tolerant Control][research_yang_lee_2015]
- [Review on Fault Detection and Fault Tolerant Control Applied...][research_abdulhuq_beebim_2015]
- [SELECTION METHOD OF MONITORING ALGORITHM THRESHOLDS FOR...][research_bazhenov_lysenkova_2015]
- [The control law of the available energy of the aircraft for...][research_anon_2015]
- [A Novel Approach for Fault Tolerance Control System and...][research_khadse_karmore_2016]
- [Aircraft fault-tolerant trajectory control using Incremental...][research_lu_vankampen_2016]
- [Alternative Trim Analysis Formulations for Vehicles with...][research_garmendia_mavris_2016]
- [Combining sensor monitoring and fault tolerant control to...][research_ossmann_joos_2016]
- [Constraint finite-time control of redundant manipulators][research_galicki_2016]
- [Control computers diagnostics for UAV flight control system][research_kopecki_2016]
- [DESIGN OF INTEGRAL CONTROL ALGORITHMS FOR FLY-BY-WIRE CONTROL...][research_kuvshinov_2016]
- [DESIGN OF INTEGRAL CONTROL ALGORITHMS FOR THE LATERAL CHANNEL...][research_kuvshinov_2016_b]
- [Development of Flight Control System and Troubleshooting on...][research_kang_park_2016]
- [Explicit robustness and fragility margins for linear discrete...][research_nguyen_olaru_2016]
- [Fault Tolerant Control with Reconfiguration Mechanism for a...][research_ganesh_manoharan_2016]
- [Fault Tolerant Flight Control Using Sliding Modes and...][research_siddiqui_elferik_2016]
- [Fault tolerant control design using adaptive control...][research_tohidi_khakisedigh_2016]
- [Fault-Tolerant Flight Control Design with Explicit...][research_yu_zhang_2016]
- [Flight Control Law Clearance Using Optimal Control Theory][research_herrmann_benasher_2016]
- [Flight Control Software Failure Mitigation Design...][research_morozov_janschek_2016]
- [Flight Control System Modeling with SysML to Support...][research_mhenni_choley_2016]
- [Flight Envelope Load Factor Limit Logic Design for Helicopter...][research_choi_2016]
- [Fly-by-wire robustness to flight dynamics change under...][research_dlamini_jones_2016]
- [Optimality-based dynamic allocation with nonlinear...][research_passenbrunner_sassano_2016]
- [Real-Time Reliability Verification for UAV Flight Control...][research_xu_wang_2016]
- [Receptance-Based Active Aeroelastic Control with Embedded...][research_singh_brown_2016]
- [Robust Fault-Tolerant Control Allocation for an...][research_cui_yang_2016]
- [Robust fault-tolerant control for wing flutter under actuator...][research_gao_cai_2016]
- [Robustness Assessment of a Load Factor Flight Control Law...][research_bessadi_saussie_2016]
- [SKF divests fly-by-wire business][research_skf_divests_2016]
- [Tracking Control Based on Control Allocation with an...][research_dong_lu_2016]
- [Actuator fault tolerant control of systems with polytopic...][research_nazari_seron_2017]
- [Evaluation of an L1 Adaptive Flight Control Law on Calspan’s...][research_ackerman_xargay_2017]
- [Fault-Tolerant Certifiable Control for a V-Tail Remotely...][research_garciahernandez_cuernorejado_2017]
- [Handling Qualities Evaluation of Time Delay and Predictive...][research_zhang_huang_2017]
- [Higher-order Iterative Learning Control Law Design using...][research_wang_chu_2017]
- [Influence of flight control law on spin dynamics of...][research_malik_akhtar_2017]
- [Intelligent Flight Control System Design for the Small UAV...][research_komnatska_bondarenko_2017]
- [Multiobjective optimization based fault‐tolerant flight...][research_ossmann_joos_2017]
- [Multiple Fault-Tolerant In-Wheel Vehicle Control Based on...][research_mihaly_gaspar_2017]
- [Nonlinear Dynamic Inversion Control Law Development of High...][research_kim_sung_2017]
- [Supervisory adaptive fault‐tolerant control against actuator...][research_ouyang_lin_2017]
- [Wing Flow Separation Control Using Asymmetrical and...][research_zhang_li_2017]
- [Adaptive Control for Quadrotor UAVs Considering Time Delay...][research_karmah_2018]
- [Adaptive fault‐tolerant control for a nonlinear flexible...][research_zhang_liu_2018]
- [An improved NSGA-II based control allocation optimisation for...][research_bian_nener_2018]
- [Design of Shape Memory Alloy Coil Spring Actuator for...][research_koh_2018]
- [Distributed Sensor and Actuator Reconfiguration for...][research_teixeira_araujo_2018]
- [FLIGHT CONTROL SYSTEM NETWORK ARCHITECTURE DESIGN AND...][research_bai_2018]
- [Ursu et al 2018][research_ursu_ionguta_2018]
- [Flight test of fault-tolerant flight control system using...][research_matsuki_nishiyama_2018]
- [IMITATION MODELING OF THE RECOVERY PROCESS OF THE ON-BOARD...][research_zelenkov_2018]
- [Integral sliding mode fault‐tolerant control allocation for a...][research_chen_edwards_2018]
- [Modified L1 Adaptive Control Design for Satellite FMC Systems...][research_modified_l1_2018]
- [Nonlinear Aeroelasticity of Morphing Wing with Piezoelectric...][research_tsushima_arizono_2018]
- [Nonlinear Fault-Tolerant Control for Hypersonic Flight...][research_chen_niu_2018]
- [Nonlinear fuzzy fault-tolerant control of hypersonic flight...][research_niu_chen_2018]
- [Reconfigurable Fault Tolerant Flight Control for UAV with...][research_mammadov_hajiyev_2018]
- [Robust Actuator‐Fault‐Tolerant Control System Based on...][research_li_dong_2018]
- [Smart Integrated Optical Rotation Sensor Incorporating a...][research_tameh_sawan_2018]
- [Static output feedback fault tolerant control using control...][research_argha_su_2018]
- [System Reconfiguration and Fault-Tolerant for Distributed...][research_xiao_liu_2018]
- [The development requirement and design considerations for...][research_shi_tan_2018]
- [A Modified NSGA-II for Solving Control Allocation...][research_bian_nener_2019]
- [A Novel RFDI-FTC System for Thrust-Vectoring Aircraft...][research_ma_dong_2019]
- [Adaptive Closed-Loop Control Allocation-Based Fault Tolerant...][research_lu_ma_2019]
- [Adaptive control of nonlinear system based on QFT application...][research_boby_abdullah_2019]
- [Adaptive fault tolerant control of dissimilar redundant...][research_ijaz_hamayun_2019_b]
- [Application of LQG and H∞ Gain Scheduling Techniques to...][research_rosique_alamin_2019]
- [CONTROL LAW FOR AN AIRCRAFT SUPERSONIC AIR INLET WITH...][research_tudosie_dumitru_2019]
- [Connections between control allocation and linear quadratic...][research_duan_okwudire_2019]
- [DESIGN OF FLY-BY-WIRE CONTROL SYSTEM ALGORITHMS FOR...][research_kuvshinov_leontiev_2019]
- [Design and Implementation of UAV’s Flight Control System Test...][research_liu_tian_2019]
- [Design and Performance Verification of L1 Adaptive Flight...][research_ko_kang_2019]
- [Design of Control Law of Post Stall Maneuver under Unsteady...][research_lyu_zhang_2019]
- [Fault-Tolerant Flight Control Using One Aerodynamic Control...][research_venkataraman_seiler_2019]
- [Flight control system Design of unmanned fixed wing aircraft...][research_sugino_harada_2019]
- [High-Bandwidth Morphing Actuator for Aeroelastic Model Control][research_fichera_isnardi_2019]
- [Incremental Sliding-Mode Fault-Tolerant Flight Control][research_wang_kampen_2019]
- [LPV Modeling and Tracking Control of Dissimilar Redundant...][research_ijaz_hamayun_2019]
- [Modeling, Simulation and Control of a Fly-by-wire Flight...][research_fadel_rabie_2019]
- [New Stability Criteria for Event‐Triggered Nonlinear...][research_lu_hu_2019]
- [Output feedback adaptive fault‐tolerant compensation tracking...][research_xiao_dong_2019]
- [Prescribed Performance Fault Tolerant Control for Hypersonic...][research_zhao_li_2019]
- [Sliding‐mode fault‐tolerant control using the control...][research_argha_su_2019]
- [A New Method for Control Allocation of Aircraft Flight...][research_yang_gao_2020]
- [A Novel Control Allocation Method for Yaw Control of Tailless...][research_shearwood_nabawy_2020]
- [A Review of the Most Adopted Fault Tolerance Approaches for...][research_bouras_2020]
- [A Way to Mitigate Force-Fight Oscillation Based on Pressure...][research_xue_yao_2020]
- [A simple and efficient control allocation scheme for...][research_sadien_roos_2020]
- [Active Fault Tolerance Control Based on Consistent Matrix for...][research_mao_li_2020]
- [Active Fault-Tolerant Control Strategy for More Electric...][research_sun_wang_2020]
- [Actuator modelling for attitude control using incremental...][research_binz_moormann_2020]
- [An Innovative Control Allocation Framework for a Novel...][research_xu_zhang_2020]
- [Event-based fault-tolerant control for networked control...][research_li_tang_2020]
- [Finite Time Convergence Incremental Nonlinear Dynamic...][research_zhang_han_2020]
- [Flight evaluation of a sliding mode online control allocation...][research_chen_edwards_2020]
- [Flying qualities evaluation based nonlinear flight control...][research_sun_shi_2020]
- [Implementation of Flight Control Computer Redundancy System...][research_om_park_2020]
- [LPV modeling and controller design for body freedom flutter...][research_tang_wang_2020]
- [Networked Control System in Quadrotor Altitude Control with...][research_panuntun_wahyunggoro_2020]
- [Reduced Order Model Based Flight Control System for a...][research_mohamed_g_2020]
- [Reinforcement learning based closed‐loop reference model...][research_yuksek_inalhan_2020]
- [Research on Air Flight Simulation Control Law of Large...][research_you_2020]
- [Robust fault tolerant control allocation for a modern...][research_vile_alwi_2020]
- [Self-triggered sliding mode control for Digital Fly-by-Wire...][research_cao_jia_2020]
- [TS fuzzy reconfiguration blocks for fault tolerant control of...][research_bessa_puig_2020]
- [Three-axis coupled flight control law design for flying wing...][research_wang_zhang_2020]
- [Time delay handling in dominant pole placement with PID...][research_halder_das_2020]
- [A Software Verification Approach That Complies with DO-178B...][research_demir_seyfullahbabaarslan_2021]
- [Aircraft flight control system fault tolerance under...][research_kosyanchuk_zheltov_2021]
- [Business Jet Fly-by-Wire Control Laws Handling Qualities...][research_berger_tischler_2021]
- [Distributed optimal control allocation for 6-dof spacecraft...][research_lang_deruiter_2021]
- [Effect of Actuator Saturation on Pilot-Induced Oscillation A...][research_nguyen_lowenberg_2021]
- [Fault Analysis and Non-Redundant Fault Tolerance in 3-Level...][research_caseiro_mendes_2021]
- [Fault Tolerant Control and Reconfiguration of Mobile...][research_rayankula_pathak_2021]
- [Fault estimation and fault tolerance control for spacecraft...][research_gao_wang_2021]
- [Fuzzy robust fault estimation scheme for fault tolerant...][research_unal_2021_b]
- [Integrated design of fault-tolerant control for flight...][research_unal_2021]
- [Intelligent Fault-Tolerant Control for AC/DC Hybrid Power...][research_xiao_sattarov_2021]
- [Modeling and SPM-dependent control of multi-rate networked...][research_nekooei_farsangi_2021]
- [ROBUSTNESS OF AIRCRAFT TURBOFAN ENGINE CLOSED-LOOP CONTROL...][research___2021]
- [Research on a Passenger Aircraft Flight Control System Gain...][research_guo_2021]
- [Research on the NealandSmith Criterion Application on...][research_guo_2021_b]
- [Robust dynamic inversion control of flight control system...][research_li_liu_2021]
- [Robust fault-tolerant flight path angle control][research_dhadekar_misra_2021]
- [Robust modification of nonlinear L1 adaptive flight control...][research_feng_wang_2021]
- [Time delay compensation in lateral-directional flight control...][research_shen_huang_2021]
- [\ \mathcal L _1 \ Adaptive Loss Fault Tolerance Control of...][research_li_shi_2021]
- [Active Fault-Tolerant Incremental Sliding-Mode Flight Control...][research_chang_debreuker_2022]
- [Application Analysis on Fly-by-Wire Flight Control System on...][research_application_analysis_2022]
- [Automatic weighting filter tuning for robust flight control...][research_perez_theodoulis_2022]
- [Design and Application of Electromechanical Control System...][research_wei_2022]
- [Design of generalized fault diagnosis observer and active...][research_sun_han_2022]
- [Digital twin-based fault tolerance approach for Cyber...][research_saraeian_shirazi_2022]
- [Dynamic control allocation between onboard and delayed remote...][research_tabassum_bai_2022]
- [ESTIMATION OF FLY-BY-WIRE EMERGENCY SERVO-CONTROL OF REGIONAL...][research_terekhov_2022]
- [Enhancing Flight Envelope for a Nonlinear Aeroelastic...][research_dilmi_2022]
- [Fault tolerant control of a quadrotor based on incremental...][research_ahmadidastgerdi_asadi_2022]
- [Fly-by-wire Flight Control Comparative Analysis of Resident...][research_shen_chang_2022]
- [Health management using fault detection and fault tolerant...][research_mahboub_rouabah_2022]
- [In-Depth Assessment and Optimized Actuation Method of a Novel...][research_almadani_osman_2022]
- [In-Flight Demonstration of Stall Improvement Using a Plasma...][research_sekimoto_kato_2022]
- [Load Alleviation of Flexible Aircraft by Dynamic Control...][research_hansen_duan_2022]
- [Longitudinal Flight Control Law Design with Integrated...][research_moreira_gripp_2022]
- [METHODOLOGY FOR QUORUM CONTROL OF THE REDUNDANT IRS SIGNALS...][research_savelev_neretin_2022]
- [Predictor-based Adaptive Incremental Nonlinear Dynamic...][research_chang_guo_2022]
- [Research and Design of Automatic Flight Control System Test...][research_research_and_2022]
- [Review on Flight Control Law Technologies of Fighter Jets for...][research_kim_ji_2022]
- [Simulation and experimental research on adaptive control...][research_zhang_shao_2022]
- [Simultaneous Fault and Input Time Delay Estimation for an...][research_chen_edwards_2022]
- [Simultaneous wing shape and actuator parameter optimization...][research_koyuncuoglu_he_2022]
- [A comparative study of redundant and non-redundant flight...][research_robbins_stansbury_2023]
- [A smooth control allocation method for a distributed electric...][research_qin_liu_2023]
- [Control Allocation for Windup Mitigation in Weakly Redundant...][research_govoni_cristofaro_2023]
- [Development of Fault Tolerant Flight Control System For...][research_k_deodhare_2023]
- [Fault-Tolerant Attitude Control Incorporating Reconfiguration...][research_cong_hu_2023]
- [Flight Control Law for Stabilizing Transient Response of the...][research_ji_kim_2023]
- [Fly by Wire Advancements in Aviation over Conventional Flight...][research_pendem_2023]
- [Grouped Multilayer Practical Byzantine Fault Tolerance...][research_liu_feng_2023]
- [Hybrid Adaptive Control for Tiltrotor Aircraft Flight Control...][research_wen_song_2023]
- [Improved model reference‐based adaptive nonlinear dynamic...][research_li_liu_2023]
- [Incremental Nonlinear Dynamic Inversion Attitude Control for...][research_zhang_zhang_2023]
- [Methodology for Preliminary Flight Control Actuator Design][research_stephan_stumpf_2023]
- [Minimum Power Control Allocation for Incremental Control of...][research_pfeifle_fichter_2023]
- [Nonlinear Dynamic Inversion with Actuator Dynamics An...][research_steffensen_steinert_2023]
- [Open-Phase Fault-Tolerant Control Strategy for Dual...][research_song_jia_2023]
- [Optimal resource allocation method and fault-tolerant control...][research_rong_dou_2023]
- [Real-Time Implementation of an Adaptive PID Controller for...][research_noordin_mohdbasri_2023]
- [Research on Dynamic Characteristics Analysis and Control Law...][research_tai_wang_2023]
- [Research on automatic flight control system flight mode...][research_liu_zhou_2023]
- [Simultaneous UAV having actively sweep angle morphing wing...][research_uzun_oktay_2023]
- [Suggestions for Criteria to Evaluate Lateral-Directional...][research_wang_lu_2023]
- [Synthesis of Control Law Based on Nonlinear Dynamic Inversion...][research_gaurav_sekou_2023]
- [Thrust Vectoring Control for Heavy UAVs, Employing a...][research_aleisaac_ragab_2023]
- [A pair of two-stage Kalman filters to detect and isolate...][research_cordeiro_azinheira_2024]
- [Active Fault-Tolerant Strategy for Flight Vehicles Transfer...][research_zhao_lu_2024]
- [Active Flutter Suppression Quantification of Performance Loss...][research_micheli_2024]
- [Adaptive PI Control Based Stability Margin Configuration of...][research_zhang_zhou_2024_b]
- [Commonalities between robust hybrid incremental nonlinear...][research_pollack_theodoulis_2024]
- [Design, modeling and optimal control of a novel compliant...][research_sun_xu_2024]
- [Evolutionary Reinforcement Learning Hybrid Approach for...][research_gavra_vankampen_2024]
- [Flight control system design of UAV with wing incidence angle...][research_uzun_2024]
- [Full Envelope Flight Control System Design and Optimization...][research_comer_chakraborty_2024]
- [Markov multi-fault tolerance control of intelligent...][research_wang_sun_2024_b]
- [Method of Control System Fault Tolerance Based on Full or...][research_zhirabok_filaretov_2024]
- [Minimum-Drag Fault-Tolerant Aircraft Control Allocation via...][research_antonakis_biannic_2024]
- [PCA-Kriging-Based Oscillating Jet Actuator Optimization and...][research_sun_wang_2024]
- [Rack force fault tolerance estimation of steer-by-wire system...][research_zhao_zhao_2024]
- [Reconfiguration-based fault tolerant control algorithm for...][research_deng_stoica_2024]
- [Retracted Design and Application of Electromechanical Control...][research_robotics_2024]
- [Review of Fault-tolerant Control for Flight Control System][research_review_of_2024]
- [A Method for PIO Suppression in Aircraft with Fly-By-Wire...][research_miranda_bidinotto_2025]
- [A Model Reference Adaptive Control Approach to Terrain...][research_inan_aliskan_2025]
- [A twisted string actuator using a shape memory alloy for dual...][research_nam_choi_2025]
- [Active Fault-tolerant Control of Parallel Digital Valves and...][research_active_fault_tolerant_2025]
- [Aerodynamic Analysis and Application of the Channel Wing...][research_cao_liu_2025]
- [Control allocation design for equal control sensitivity of...][research_wang_li_2025]
- [Design and Analysis of a Launcher Flight Control System Based...][research_simplicio_acquatella_2025]
- [Digital Twin Enabled Flight Control System Testing Design...][research_ren_xu_2025]
- [Dynamic Control Allocation for Nonlinear Systems via a...][research_akbari_galeani_2025]
- [Dynamic load alleviation of input-redundant flexible aircraft...][research_dong_zhou_2025]
- [Energy Configuration Design and Configuration Scheme of...][research_qian_xinhui_2025]
- [Fault Detection and Fault-Tolerant Control Based on Bi-LSTM...][research_li_shang_2025]
- [Fault-tolerant reconfiguration estimation and control of...][research_luo_yin_2025]
- [Fault‐Tolerant Control of Post‐Stall Maneuver for Fighter...][research_li_ji_2025]
- [INDI Application in Flight Control Law Design of Civil...][research_li_xiong_2025]
- [Intelligent fault tolerance control using long short-term...][research_elmahdy_ali_2025]
- [Kernel-based predictive control allocation for a class of...][research_nguyen_han_2025]
- [LITERATURE STUDY ON DESIGNING CONTROL LAW FOR CONVENTIONAL...][research_abdulrashid_syedmohddardin_2025]
- [Managing reconfiguration time in optimal spacecraft active...][research_moradi_zalaghi_2025]
- [Methods for selecting the best automated flight control...][research_vitushkinvv_2025]
- [Nonlinear dynamic inversion control with unknown control...][research_cao_liu_2025_b]
- [Norm-Bounded Model Predictive Control Allocation Strategy for...][research_scordamaglia_mattei_2025]
- [Online Inertial Measurement Unit Fault Identification and...][research_atmaca_devisser_2025]
- [Redundancy design and research of safety fly-by-wire flight...][research_wang_li_2025_b]
- [Redundant Control Allocation Strategies for the RACER...][research_saetti_2025]
- [Reinforcement Q-learning based flight control for a passenger...][research_mohammadi_ebrahimi_2025]
- [Research on a Safety-Critical Architecture of Large...][research_tang_tang_2025]
- [Research on adaptive nonlinear dynamic inversion...][research_li_shi_2025]
- [Research on control law of more-electric aircraft...][research_zheng_shao_2025]
- [Robustness Analysis of the Model Predictive Position Control...][research_lucarini_dirito_2025]
- [Super‐Maneuver Flight Control Based on Predefined Time...][research_li_lin_2025]
- [Thrust Allocation Control of an Underwater Vehicle with a...][research_deng_tao_2025]
- [Cascaded Nonlinear Active Disturbance Rejection Control with...][research_xu_zhang_2026_b]
- [Design of Intelligent Control Law Embedded With Dynamic Flow...][research_zhao_liu_2026_b]
- [Effectiveness and robustness of an independent flight control...][research_hubener_luckner_2026]
- [Electromechanical Flight-Control Actuation Systems for...][research_martinezheredia_fernandezprada_2026]
- [Fault Transmission Modeling and Non-Bypass Fault Tolerance...][research_yang_yu_2026]
- [Fault-Tolerant Control and Fault Diagnosis of Symmetrical...][research_liu_yu_2026]
- [First integration of triboelectric sensing into flight...][research_liu_wang_2026]
- [Force Control of Hydraulic Actuator Based on Incremental...][research_lian_cao_2026]
- [Immersion and Invariance Adaptive Fault-Tolerant Attitude...][research_immersion_and_2026]
- [Kriging-accelerated worst-case search for envelope-wide...][research_kotitschke_rupprecht_2026]
- [Maximum-system-reliability control allocation for spacecraft...][research_zhang_yu_2026]
- [Passive Fault-Tolerant Control of Lifting-Wing Quadrotors...][research_chen_cai_2026]
- [Probabilistic fault tree analysis and dynamic redundancy...][research_dagal_2026]
- [Reduced-Order Nonlinear Dynamic Analysis and Lyapunov-Based...][research_jin_xue_2026]
- [Rigid Flexible Coupling Model-Driven Simulation of UAV...][research_shao_li_2026]
- [Safety Assessment and Fault Tolerance in eVTOL Aircraft...][research_han_pei_2026]
- [Self‐Learning Robust Fault‐Tolerant Control for Aircraft...][research_peng_li_2026]
- [Stability Analysis of Discrete Adaptive Control With Adaptive...][research_sisson_dogan_2026]
- [Structural Design Optimization of Bellcrank 3 in the N219...][research_hartini_bachtiar_2026]
- [Tandem Tilt-Wing Control Law Design Using Hybrid Nonlinear...][research_milz_may_2026]
- [Vehicle Sensor Steering System Control Based on Steering by...][research_vehicle_sensor_2026]

- [Active control design for an unmanned air vehicle with a...][research_li_guo_2016]
- [Energy efficient active control of the flow past an aircraft...][research_skarolek_jkarabelas_2016]
- [Robust kernel-based model reference adaptive control for...][research_yang_zhao_2016]
- [Stability Augmentation and Active Flutter Suppression of a...][research_schmidt_2016]
- [Active Control of Aeroelastic Vibrations for...][research_yoo_2017]
- [Comparison of the passive and active control gust alleviation...][research_liu_2018]
- [Active Control of Wing-tip Vortex Development Using...][research_himeda_naka_2019]
- [Active control of supersonic transport aeroelastic...][research_guruswamy_2019]
- [DESIGN OF ACTIVE CONTROL SYSTEM OF PASSENGER AIRCRAFT FOR...][research_kuvshinov_lazurin_2019]
- [Aeroelastic control of bridge using active control surfaces...][research_phan_2020]
- [Design and Flight Test of a Stability Augmentation System for...][research_barbosa_bertolin_2022]
- [Design of Thrust Vectoring Vertical/Short Takeoff and Landing...][research_zhou_wang_2022]
- [Experimental studies on flaps flow-around active control by...][research_sha_sun_2022]
- [Unstable Aircraft Parameter Estimation Using Neural Partial...][research_kuttieri_sinha_2023]
- [A Comparative Analysis of Active Control vs. Folding Wing Tip...][research_toffol_2024]
- [Wing design optimization and stall analysis with Co-flow Jet...][research_jiang_yao_2024]
- [Dynamic performance analysis of attitude control for...][research_zhang_li_2026]
- [Flexible wingtip active control test and mechanism for gust...][research_zheng_dai_2026]

### Aeroservoelasticity became its own discipline

**The interaction the X-29 encountered in flight now has a name, a literature and a place in the design process.**
Structural modes inside the control bandwidth, notch filters that trade stability against delay, and the
fact that a delay bought to suppress a structural mode is a delay taken from an unstable airframe's budget.
**The X-29 had all three problems and met them one at a time in flight.**

- [Active gust load alleviation system for flexible aircraft...][research_alam_hromcik_2015]
- [Aeroservoelastic Model Modification and Uncertainty...][research_dai_yang_2015]
- [Gust Load Alleviation for a Regional Aircraft Through a...][research_fonte_ricci_2015]
- [Optical notch filter with tunable bandwidth based on...][research_qian_zhang_2015]
- [Rapid State Space Modeling Tool for Rectangular Wing...][research_suhpeterm_conyershowardjason_2015]
- [Active Balancing Control of AMB-Rotor Systems Using a...][research_zheng_chen_2016]
- [Aeroelastic scaling laws for gust load alleviation control...][research_tang_wu_2016]
- [Aeroservoelastic Test of the Subsonic Ultra-Green Aircraft...][research_scott_bartels_2016]
- [Design and flight test of active flutter suppression on the...][research_burnett_beranek_2016]
- [Gust Load Alleviation on a Large Transport Airplane][research_zhao_yue_2016]
- [Gust Load Alleviation with Robust Control for a Flexible Wing][research_liu_sun_2016]
- [Optimization of an Aeroservoelastic Wing with Distributed...][research_stanford_2016]
- [Prediction and Simulator Verification of Roll/Lateral Adverse...][research_muscarello_quaranta_2016]
- [Probabilistic Aeroservoelastic Reliability Assessment...][research_wu_livne_2016]
- [WITHDRAWN Robust aeroservoelastic design with mixed...][research_dai_wu_2016]
- [Active Flutter Suppression of Stochastic Airfoil with...][research_wu_tong_2017]
- [Active aerothermoelastic flutter suppression of composite...][research_chai_song_2017]
- [Aeroservoelastic modeling with proper orthogonal decomposition][research_carlson_verberg_2017]
- [Aeroservoelastic modelling and control of a slender anti-air...][research_verhaegen_zbikowski_2017]
- [An Adaptive Notch Gain Using an Inverse Notch Filter and a...][research_nakamura_kawamura_2017]
- [Design of an Active Disturbance Rejection Control for...][research_yang_huang_2017]
- [Flutter suppression for highly flexible wings using passive...][research_tsushima_su_2017]
- [Genetic Algorithm-Based Model Order Reduction of...][research_zhu_wang_2017]
- [Gust Load Alleviation Identification, Control, and Wind...][research_poussotvassal_demourant_2017]
- [Gust load alleviation wind tunnel tests of a...][research_bi_xie_2017]
- [Improved LQG Method for Active Gust Load Alleviation][research_liu_sun_2017]
- [LQG based model predictive control for gust load alleviation][research_liu_sun_2017_b]
- [Mid-wave infrared narrow bandwidth guided mode resonance...][research_zhong_goldenfeld_2017]
- [Optimal Control Surface Layout for an Aeroservoelastic Wingbox][research_stanford_2017]
- [Robust LQR control for stall flutter suppression A polytopic...][research_niel_seuret_2017]
- [ACTIVE FLUTTER SUPPRESSION OF A HIGH ASPECT RATIO WING...][research_mamedov_paryshev_2018]
- [Adaptive Feedforward Compensating Self-Sensing Method for...][research_wang_xu_2018]
- [Aircraft Active Flutter Suppression State of the Art and...][research_livne_2018]
- [Attitude control synthesis of unstable hypersonic vehicle...][research_chen_yang_2018]
- [Delayed sub-optimal control for active flutter suppression of...][research_zhou_yu_2018]
- [Parametric Flutter Margin Method for Aeroservoelastic...][research_roizner_karpel_2018]
- [Reentry attitude control for a reusable launch vehicle with...][research_mao_dou_2018]
- [Robust Flutter Suppression and Wind-Tunnel Tests of a...][research_qian_2018]
- [Speed Regulation System of a Flux-Modulated Permanent-Magnet...][research_fan_zhang_2018]
- [A Generalized State-Space Aeroservoelastic Model Based on...][research_quero_vuillemin_2019]
- [Active flutter suppression non-structured and structured H∞...][research_waitman_marcos_2019]
- [Adaptive aeroservoelastic mode stabilization of flexible...][research_piao_zhang_2019]
- [Aeroservoelastic design of piezo-composite wings for gust...][research_liu_wang_2019]
- [Examples on increased-order aeroservoelastic modeling][research_reyes_climent_2019]
- [Flexible Aircraft Gust Load Alleviation with Incremental...][research_wang_vankampen_2019]
- [Gradient-Based Aeroservoelastic Optimization with Static...][research_stanford_2019]
- [Integrated optimization of control surface layout for gust...][research_pusch_knoblach_2019]
- [Optimization and control application of sensor placement in...][research_yang_yang_2019]
- [Parameterized Modeling Methodology for Efficient...][research_huang_yang_2019]
- [Protection of Sensitive Loads Using Sliding Mode Controlled...][research_biricik_komurcugil_2019]
- [Sensitivity of Aeroservoelastic Stability Characteristics...][research_roizner_karpel_2019]
- [Transonic flutter suppression for a three-dimensional elastic...][research_yang_huang_2019]
- [A neural network approach for improving airfoil active...][research_tang_chen_2020]
- [Active Disturbance Rejection Control for Hypersonic Flutter...][research_chen_zhao_2020]
- [Active dynamic vibration absorber for flutter suppression][research_kassem_yang_2020]
- [Airfoil gust load alleviation by circulation control][research_li_qin_2020]
- [An improved aeroservoelastic modeling approach for...][research_yue_zhao_2020]
- [Analysis of dynamic response and flutter suppression system...][research_kuzmina_ishmuratov_2020]
- [Design and Optimization of an Aeroservoelastic Wind Tunnel...][research_dillinger_meddaikar_2020]
- [Gust Load Alleviation of Flexible Composite Wing][research_ibren_sulaeman_2020]
- [Gust load alleviation for flexible aircraft using...][research_khalil_fezans_2020]
- [H∞ Control Design for Active Flutter Suppression of...][research_waitman_marcos_2020]
- [Parametric active aeroelastic control of a morphing wing...][research_liu_gao_2020]
- [Robust Modal Damping Control for Active Flutter Suppression][research_theis_pfifer_2020]
- [Synchronous vibration control for magnetically suspended...][research_peng_zhu_2020]
- [Active Flutter Suppression of Smart-Skin Antenna Structures...][research_lee_kim_2021]
- [Active flutter suppression of wing with morphing flap][research_ouyang_gu_2021]
- [Cross-Domain Collaborative Oscillation Control Strategy for a...][research_wang_xu_2021]
- [Gust load alleviation by normal microjet][research_li_qin_2021_b]
- [Gust load alleviation on an aircraft wing by trailing edge...][research_li_qin_2021]
- [Model Updating and Aeroelastic Correlation of a Scaled Wind...][research_dileone_lobalbo_2021]
- [Modeling and Control Design for Flutter Suppression Using...][research_kassem_yang_2021]
- [Synthesis of an active flutter suppression system in the...][research_vepa_kwon_2021]
- [A Review of Flow Control for Gust Load Alleviation][research_li_qin_2022]
- [A narrowband active noise control system with autoregressive...][research_liu_wang_2022]
- [Active Flutter Suppression and Aeroelastic Response of...][research_chen_han_2022]
- [Active Flutter Suppression of a Wing Section in a...][research_munoz_garciafogeda_2022]
- [Aeroservoelastic Characteristics of a Corrugated Morphing...][research_soneda_tsushima_2022]
- [Application of Structured Robust Synthesis for Flexible...][research_patartics_liptak_2022]
- [Body-Freedom Flutter Suppression for a Flexible Flying-Wing...][research_zou_huang_2022]
- [Composite Design of Disturbance Observer and Reentry Attitude...][research_yang_mao_2022]
- [Control of tremor by frequency-tracking notch filter][research_yamakoshi_komatsuzaki_2022]
- [Design of Gust Load Alleviation Control Based on UD-PSO for...][research_qu_li_2022]
- [Design of feedback-structured IIR notch filter with transient...][research_amini_mozaffaritazehkand_2022]
- [Discrete-Time Model Predictive Controller Using Laguerre...][research_darabseh_tarabulsi_2022]
- [Efficient Nonlinear Aeroservoelastic Modeling for Morphing...][research_huang_yu_2022]
- [Generalized Predictive Control for Active Flutter Suppression...][research_haley_soloway_2022]
- [Improving Gust Load Alleviation Performance of Hinge Wingtip...][research_balatti_khodaparast_2022]
- [Machine learning-based active flutter suppression for a...][research_mu_huang_2022]
- [Nonlinear Helicopter Rigid-Elastic Coupled Modeling with Its...][research_wang_chen_2022]
- [Partial Feedback Linearized RISE Controller for Active...][research_sharma_agrawal_2022]
- [Robust Gust Load Alleviation of Flexible Aircraft Equipped...][research_fournier_massioni_2022]
- [Smart Wing Flutter Suppression][research_moosavi_elasha_2022]
- [Whirl Flutter Suppression of Tiltrotor Aircraft Using...][research_dong_li_2022]
- [Active Flutter Suppression for a T-Tail via Optimal Control][research_xiang_wang_2023]
- [Active flutter suppression for a flexible wing model with...][research_chen_shi_2023]
- [Active flutter suppression on a flexible wing via...][research_chen_shi_2023_b]
- [Adaptive Feed-Forward Control for Gust Load Alleviation on a...][research_zhang_zhao_2023_b]
- [Aeroservoelastic Wind Tunnel Evaluation of Preview H2 and H∞...][research_ting_mesbahi_2023]
- [Gust Load Alleviation Using Reduced-Order Aeroelastic Models...][research_desouza_vuillemin_2023]
- [Identification of exon locations in DNA sequences using a...][research_lehilahy_ferdi_2023]
- [Incremental Nonlinear Control for Aeroelastic Wing Load...][research_schildkamp_chang_2023]
- [Oblique Projection-Based Modal Matching Algorithm for LPV...][research_liu_gao_2023]
- [Two New and Improved Electronically Adjustable Voltage-Mode...][research_chen_wang_2023]
- [Active Flutter Suppression of a Wing Section in the Subsonic...][research_munoz_garciafogeda_2024]
- [Active Stall Flutter Suppression for a Revised Leishman...][research_zheng_pontillo_2024]
- [Active flutter suppression for an aircraft wing structure by...][research_sekhar_suresh_2024]
- [Active flutter suppression for light sport aircraft by a...][research_kratochvil_valenta_2024]
- [Boosted Incremental Nonlinear Dynamic Inversion for Flexible...][research_beyer_steen_2024]
- [Enhancing gust load alleviation performance in an optimized...][research_ahmadi_farsadi_2024_b]
- [Fluidic Flow Control Devices for Gust Load Alleviation][research_khalil_bauknecht_2024]
- [Gust Load Alleviation Control Strategies for Large Civil...][research_zhang_qiu_2024]
- [Gust load alleviation of a flexible flying wing with linear...][research_gao_liu_2024]
- [LHS-GA Based H-Infinity Control for Robust Airfoil Flutter...][research_rekik_khaled_2024]
- [Linear Modeling of Doppler Wind Lidar Systems for Gust Load...][research_cavaliere_fezans_2024_b]
- [Toward Automated Gust Load Alleviation Control Design via...][research_cavaliere_fezans_2024]
- [Unsteady nonlinear lifting line model for active gust load...][research_beyer_ullah_2024]
- [Active disturbance rejection controller for flutter...][research_chen_zhai_2025]
- [Aerodynamic Nonlinear Modeling and Body-Freedom Flutter...][research_liu_zheng_2025]
- [Destabilize/Stabilize Approach to Experimental Active Flutter...][research_berg_ting_2025]
- [Edge computing aileron mechatronics using antiphase...][research_yin_huang_2025]
- [Event-Triggered Adaptive Dynamic Programming for an...][research_wang_sun_2025]
- [Experimental Active Flutter Suppression Control with Inertial...][research_szymanski_alstrom_2025]
- [Gust load alleviation performance of a passively actuated...][research_wheatcroft_groh_2025]
- [Model predictive control of a flared folding wingtip for gust...][research_narimani_haddadpour_2025]
- [Robust Control Design for the Higher Harmonic Vibration...][research_im_kong_2025]
- [Wind Tunnel Testing of a Passive Gust Load Alleviation Spoiler][research_wheatcroft_mahadik_2025]
- [A deep learning density shaping model predictive gust load...][research_pourtakdoust_khodabakhsh_2026]
- [Active vibration control and optimized flutter suppression in...][research_jalalnezhad_2026]
- [Aeroservoelastic Modeling and Analysis of Aircraft with...][research_yurtsever_sahin_2026]
- [Aeroservoelastic Modeling, Control, and Optimization of...][research_xiong_tang_2026]
- [Aeroservoelastic Wind Tunnel Evaluation of H∞ Active Flutter...][research_ting_berg_2026]
- [Design and manufacturing of an aileron for a high-aspect...][research_sahyoun_boose_2026]
- [Gust Load Alleviation Test via Adaptive Dynamic Programming...][research_zhang_dai_2026]
- [Gust Load Alleviation via Active Folding Wingtip Concept...][research_farsadi_ahmadi_2026]
- [Gust Load Alleviation with Active Flutter Suppression Design...][research_sabatini_coppotelli_2026]
- [H∞ robust control for gust load alleviation of geometrically...][research_tantaroudas_karachalios_2026]
- [Model predictive gust load alleviation for a flexible wing...][research_rieck_herrmann_2026]
- [Recent advances in active flutter suppression a comprehensive...][research_cobogonzalez_rodriguezrobles_2026]
- [Rigid-elastic-coupled aeroservoelastic modeling and flight...][research_mu_huang_2026]
- [Transonic buffeting control via a nonlinear aeroservoelastic...][research_yang_zhang_2026]

### High angle of attack aerodynamics

The second X-29A was devoted to high angle of attack work, and vortex flow control was tested on it.
**Contemporary work has moved from characterising the flow to controlling it**, with active flow control,
and the computational methods that were merely supporting evidence for the X-29 now carry the prediction.

- [Blockage-tolerant wind tunnel measurements for a NACA 0012 at...][research_rainbird_peiro_2015]
- [Delayed detached-eddy simulation of vortex breakdown over a...][research_son_sa_2015_b]
- [Flight Envelope Protection Control Based on Reference...][research_ye_chen_2015]
- [High angle of attack command generation technique and...][research_ma_guo_2015]
- [NUMERICAL ANALYSIS OF PRESSURE PERTURBATION OF DELTA WING...][research_son_sa_2015]
- [3D flow visualization and tomographic particle image...][research_wang_gao_2016]
- [A comparison of post-stall models extended for propeller...][research_morgado_silvestre_2016]
- [ANALYSIS OF SUBSONIC VORTEX FLOW OVER THE MODEL OF...][research_osipov_2016]
- [EFFECT OF END CONTROL PLUGS ON THE PERFORMANCE OF VORTEX TUBE...][research_gowd_2016]
- [Impact of Gurney Flaplike Strips on the Aerodynamic and...][research_lee_2016]
- [Quadratic Optimal Control of Aerodynamic Vectored UAV at High...][research_manzoor_maqsood_2016]
- [CONTROL OF VORTEX FLOW OVER A MANEUVERABLE AIRCRAFT MODEL...][research_osipov_2017]
- [Comment on “Roll Control Using Only Synthetic Jet Actuators...][research_wei_chen_2017]
- [Computational Investigation of Vortex Breakdown over a...][research_hadidoolabi_ansarian_2017]
- [Detached Eddy Simulation of Complex Separation Flows over a...][research_zhang_zhang_2017]
- [Efficient nonlinear reduced-order modeling for...][research_li_jin_2017]
- [Introduction to the Special Section on F-16XL Flight...][research_introduction_to_2017]
- [Numerical Analysis of the Flow Pattern and Vortex Breakdown...][research_numerical_analysis_2017]
- [Robust control of post-stall pitching maneuver based on...][research_wu_chen_2017]
- [Roll Control Using Only Synthetic Jet Actuators at High Angle...][research_li_yang_2017]
- [The leading-edge vortex of swift wing-shaped delta wings][research_muir_arredondogaleana_2017]
- [A Spreadsheet Tool for the AERODAS Model for Calculating...][research_a_spreadsheet_2018]
- [A computational study of vortex shedding from a NACA-0012...][research_ragab_hajj_2018]
- [Detached Eddy-Simulation of Delta-Wing Post-Stall Flow Control][research_buzica_biswanger_2018]
- [Dynamic response of vortex breakdown flows to a pitching...][research_liu_luo_2018]
- [Dynamic surface control design of post-stall maneuver under...][research_lyu_cao_2018]
- [Ground Effect on the Vortex Flow and Aerodynamics of a...][research_lee_ko_2018]
- [Modelling of vortex breakdown and calculation of large-scale...][research_vlahostergios_komnos_2018]
- [Oscillations of Leading-Edge Vortex Breakdown Locations over...][research_shen_wen_2018]
- [Stall cell formation over a post-stall airfoil effects of...][research_esfahani_webb_2018]
- [A feasibility review of SMC-MIMO based control architecture...][research_a_feasibility_2019]
- [A modified discrete-vortex method algorithm with shedding...][research_faure_dumas_2019]
- [ASYMMETRIC VORTEX FLOW WITH DOUBLE VORTEX BREAKDOWN ON A...][research_osipov_2019]
- [Computational investigation of wind tunnel wall effects on...][research_zhou_dowell_2019]
- [Geometrically exact vortex lattice and panel methods in...][research_yang_xie_2019]
- [Leading-Edge Vortex Interactions at a Generic Multiple...][research_pfnur_breitsamter_2019]
- [Minimum Parameters Learning-Based Dynamic Surface Control for...][research_shi_lyu_2019]
- [Static Aeroelastic Characteristics of Morphing Trailing-Edge...][research_mao_xie_2019]
- [Study of Vortex Breakdown and Pitch up on a Compound Delta...][research_shivam_verma_2019]
- [Vortex flow on the wing of aircraft and flow control to...][research_mamonova_soudakov_2019]
- [Vortex-Sheet Representation of Leading-Edge Vortex Shedding...][research_hirato_shen_2019]
- [Experimental Investigation of the Flow Characteristics around...][research_ozkan_2020]
- [High angle of attack flight control based on switched...][research_wu_chen_2020]
- [Post-stall flight dynamics of commercial transport aircraft...][research_cen_li_2020]
- [Routes to chaos in the post-stall dynamics of...][research_rohith_sinha_2020]
- [Vortex Flow and Aerodynamic Performance of a Reverse Delta...][research_mahgoub_cortelezzi_2020]
- [A Model for Predicting Post-Stall Behavior of Axial...][research_a_model_2021]
- [Adaptive neural tracking control for high angle of attack...][research_wu_sun_2021]
- [Fan Aerodynamics With a Short Intake at High Angle of Attack][research_mohankumar_hall_2021]
- [Roll Control of Morphing Aircraft with Synthetic Jet...][research_li_wang_2021]
- [Self-excited flag vibrations produce post-stall flow control][research_tan_wang_2021]
- [Analysis of ridge ice induced unsteadiness flow under...][research_tan_zhang_2022]
- [Event‐triggering‐based robust optimal control for post‐stall...][research_shen_chen_2022]
- [Post-stall flow control with upstream flags][research_zhang_wang_2022_b]
- [Sweep Effects on Fan Intake Aerodynamics at High Angle of...][research_mohankumar_hall_2022]
- [The leading-edge vortex over a swift-like high-aspect-ratio...][research_bengida_gurka_2022]
- [Vortex breakdown characteristics of flying wing aircraft...][research_zhu_shi_2022]
- [Aeroelasticity Model for Highly Flexible Aircraft Based on...][research_dagilis_kilikevicius_2023]
- [METHODOLOGICAL PROPOSAL FOR THE SELECTION AND ANALYSIS OF THE...][research_recaluque_aguilartorres_2023]
- [Numerical Study of Geometrical Properties of Full-Span...][research_numerical_study_2023]
- [Event-Triggering-Learning-Based ADP Control for Post-Stall...][research_shen_chen_2024]
- [Extended State Observer Based Generalized Predictive Control...][research_liu_ji_2024]
- [Flow Separation Control of an Airfoil by Using External Fluid...][research_dodayav_biswas_2024]
- [Decoupled Incremental Nonlinear Dynamic Inversion Control for...][research_salahudden_2025]
- [Enhanced Synchrosqueezing Transform for Detecting...][research_bagherzadeh_mohammadkarimi_2025]
- [Enhancement of flying wing aerodynamics in crossflow at high...][research_wang_luo_2025]
- [Integrated flow control of adaptive cycle engine under high...][research_wang_chen_2025]
- [Lift Recovery in Post-Stall Region][research_dawe_bull_2025]
- [Novel control method of vortex breakdown over delta wing...][research_wang_luo_2025_b]
- [Passive control of vortex breakdown on slender delta wing...][research_shojae_salehi_2025]
- [Robust intelligent control of aircraft at high angle of...][research_yang_wang_2025]
- [Supermaneuver Control Using a Self-Tuning Strategy Without...][research_altunkaya_ozkol_2025]
- [Control of vortex breakdown over the non-slender lambda wing][research_sahin_yayla_2026]
- [Design and Wind Tunnel Test of Control Laws for High Angle of...][research_wang_li_2026]
- [Far-field boundary conditions for airfoil simulation at high...][research_golmirzaee_wood_2026]
- [On-Board Flow Sensing for Forebody Vortex-Induced Yaw at High...][research_huang_li_2026]
- [Two-phase wing-tip vortex breakdown][research_solis_leweke_2026]
- [Using the LSTM Network for Gray-Box Dynamic Identification of...][research_bagherzadeh_2026]

- [811 Flight Test of Rapid Trajectory Planner Based on Random...][research_ohki_itakura_2015]
- [Design and Flight Test of a Medium Range UAV for Aerial...][research_anggraeni_hidayat_2015]
- [Design of a quadrotor flight test stand for system...][research_beharie_pedro_2015]
- [Flight Test Result for the Ground-Based Radio Navigation...][research_jang_ahn_2015]
- [Aircraft and Rotorcraft System Identification Engineering...][research_aircraft_and_2016]
- [Flight Test Data Analysis of Hybrid Vertical Take-off and...][research_flight_test_2016]
- [Geometrically Nonlinear Aeroelastic Stability Analysis and...][research_xie_liu_2016]
- [Parameter Estimation from Near Stall Flight Data using...][research_saderla_dhayalan_2016]
- [Aeroelastic Modeling of X-56A Stiff-Wing Configuration Flight...][research_grauerjareda_bouchermatthewj_2017]
- [Aeroelastic Stability Analysis of a Wind Tunnel Wing Model...][research_rea_pecora_2017]
- [Control and flight test of a tilt-rotor unmanned aerial...][research_chen_zhang_2017]
- [Aeroelastic Stability Analysis of a Wind Tunnel Wing Model...][research_rea_pecora_2018]
- [An application of Deep Neural Networks to the in-flight...][research_dong_2018]
- [Best Practices for Training the Structures Flight Test...][research_hashiiwendyn_thompsonrandolphc_2018]
- [Design, Manufacturing and Wind Tunnel Validation of a...][research_degaspari_riccobene_2018]
- [Online system identification of mini cropped delta UAVs using...][research_saderla_kim_2018]
- [Cancellation Prediction for Flight Data Using Machine Learning][research_ansari_shaikh_2019]
- [Design and implementation of flight test parameter...][research_bai_tang_2019]
- [Flight Envelope Expansion Via Piezoelectric Actuation...][research_enciu_2019]
- [Gust Alleviation Control using Prior Gust Information Wind...][research_hamada_saitoh_2019]
- [Identification of a degradation of aerodynamic...][research_kulhanek_2019]
- [Modeling the unstable DelftaCopter vertical take-off and...][research_dewagter_meulenbeld_2019]
- [Multiple hierarchy risk assessment with hybrid model for...][research_lu_zhang_2019]
- [Preliminary Study on Flight/Wind Tunnel Testing of Aircraft...][research_kashitani_takita_2019]
- [Quadrotor Gray-Box Model Identification from High-Speed...][research_sun_devisser_2019]
- [A Data-Driven Approach to Identify Flight Test Data Suitable...][research_lerro_brandl_2020]
- [Design and flight test of a linear parameter varying flight...][research_weiser_ossmann_2020]
- [Extraction of Monophasic Data from Flight Test Data via...][research_yasue_2020]
- [Flight Trajectory Simulation and Aerodynamic Parameter...][research_cao_wei_2020]
- [A comparison of two novel approaches for conducting detect...][research_ellis_borshchova_2021]
- [Acquisition of Swept Aerodynamic Data by the Consecutive...][research_wakimoto_chiba_2021]
- [Aircraft turbulence and gust identification using simulated...][research_balatti_haddadkhodaparast_2021]
- [Constrained unscented Kalman filter for parameter...][research_li_wang_2021_b]
- [Flight Test Evaluation for Tilt Rotor Unmanned Aerial Vehicle...][research_arif_sasongko_2021]
- [Sensing, Actuation, and Control of the SmartX Prototype...][research_nazeer_wang_2021]
- [Aircraft Lateral-Directional Aerodynamic Parameter...][research_wang_zhao_2022_b]
- [Integration and Flight Test of a 7 kW Turboelectric Vertical...][research_johnsen_runnels_2022]
- [Longitudinal Aerodynamic Parameter Identification for...][research_wang_tai_2022]
- [Accelerated Flight Envelope Expansion Using Near Real Time...][research_patel_deodhare_2023]
- [Aero-Propulsive Modeling for Propeller Aircraft Using Flight...][research_simmons_gresham_2023]
- [Aerodynamic Modeling and System Identification from Flight...][research_jategaonkar_2023]
- [Characterization of Aeroelastic Behavior in a High Aspect...][research_westin_balthazar_2023]
- [Control Design and Flight Test of Aerodynamics-Driven...][research_feng_guo_2023]
- [Deep Learning and Machine Learning Algorithms for Enhanced...][research_helgo_2023]
- [Development and Verification of a ROS-Based Multi-DOF Flight...][research_kim_philip_2023]
- [Dynamic Structural Scaling Concept for a Delta Wing Wind...][research_bantscheff_breitsamter_2023]
- [Flight Dynamics Modeling and Aerodynamic Parameter...][research_tai_wang_2023_b]
- [Flight Envelope Expansion during Prototype Development][research_deepa_gupta_2023]
- [Introduction to the Advances in Aircraft System...][research_grauer_morelli_2023]
- [Parameter Identification of KT Equation Based on Flight Test...][research_shi_wang_2023]
- [Robust Stall Spin Flight Path Control with Flight Test...][research_hopwood_gresham_2023]
- [System Identification Approach for eVTOL Aircraft...][research_simmons_2023_b]
- [Unstable tilt-rotor maximum likelihood wavelet-based...][research_lichota_2023]
- [A Comparative Study on the Structural Response of...][research_sim_lee_2024]
- [Data-Driven Aircraft Modeling for Robust Reinforcement...][research_benyamen_chowdhury_2024]
- [Design and Flight Test of a Tube-Launched Unmanned Aerial...][research_finigian_kavounas_2024]
- [Identification of turbofan engine state-space model based on...][research_liu_2024]
- [Machine Learning Opportunities in Flight Test Preflight Checks][research_walker_claudio_2024]
- [Research and Flight Test on the Terminal Guidance Control...][research_cai_yang_2024]
- [Research on UAV Flight Parameter Identification Method Based...][research_chen_li_2024]
- [Aerodynamics-Driven Morphing Control and Flight Test for...][research_zhu_zhou_2025]
- [Design and Validation of a Multi-Propeller Tiltrotor UAV From...][research_yu_he_2025]
- [Flight test validation of multi-rotor flight time prediction...][research_ide_landman_2025]
- [Research and application of wing load behavior in stall...][research_meng_jiang_2025]
- [System Identification for Small Flying-Wing Unmanned Aircraft...][research_matt_chao_2025]
- [Experimental Investigations of an Aeroelastic Wind Tunnel...][research_stegmuller_haybock_2026]
- [Modeling, control stabilization and parameter identification...][research_chih_peng_2026]
- [Structure-aware fusion learning and intelligent decision...][research_liu_zhao_2026]

### Composite structures and how they are certified

**The X-29's wing skins were an early large primary composite structure on a research aircraft**, and the
record's remark that strain-gauge equation accuracies on composite were typical of experience with metal is
a small early data point in a large modern subject.

- [Investigation on Damage Tolerance of Thick Laminate Composite...][research_park_2015]
- [Weight and mechanical performance optimization of blended...][research_liu_toropov_2015]
- [Cost efficiency, integration and assembly of a generic...][research_hagnell_langbeck_2016]
- [Aeroelastic passive control optimization of supersonic...][research_sulaeman_abdullah_2017]
- [Damage resistance of a co-cured composite wing box to...][research_yu_fang_2017]
- [Maturity assessment of the laminate variable stiffness design...][research_sabido_bahamonde_2017]
- [Parametric instabilities of variable angle tow composite...][research_samukham_raju_2017]
- [Damage tolerance of an impacted composite laminate][research_dubary_bouvet_2018]
- [Design of a multistable composite laminate by variable...][research_jiang_li_2018]
- [Manufacturing of a composite wing with internal structure in...][research_patterson_grenestedt_2018]
- [Modelling, simulation and experimental validation of bend...][research_klasztorny_nycz_2018]
- [Mould design for manufacturing of isogrid structures in...][research_bellini_sorrentino_2018]
- [Nonlinear aeroelastic characteristics analysis of composite...][research_qiao_gao_2018]
- [Application of structural health monitoring techniques to...][research_romano_ciminello_2019]
- [Detailed Parametric Investigation and Optimization of a...][research_meng_yan_2019]
- [Dynamic instability of curved variable angle tow composite...][research_samukham_raju_2019]
- [Free vibration analysis of variable stiffness composite...][research_bendahmane_hamzacherif_2019]
- [Impact damage tolerance of laminate short columns subjected...][research_kubiak_gliszczynski_2019]
- [Manufacturing Spar I Beam Profile of UAV Wing Structure Made...][research_iryani_kadir_2019]
- [Potential Weight Benefits of IM7/8552 Hybrid Thin-Ply...][research_lovejoyandrewe_scottistephenj_2019]
- [Structural similitude design for a scaled composite wing box...][research_you_yasaee_2019]
- [Thermo-structural design of a Ceramic Matrix Composite wing...][research_ferraiuolo_scigliano_2019]
- [Two-level layup optimization of composite laminate using...][research_liu_featherston_2019]
- [Effect of ply angle on nonlinear static aeroelasticity of...][research_lei_wang_2020]
- [Implicit Floquet analysis for parametric instabilities in a...][research_samukham_vyasarayani_2020]
- [STRUCTURALLY OPTIMIZED POLYMER COMPOSITE WING DESIGN. PART 2...][research_baranovski_mikhailovskiy_2020]
- [Aeroelastic and local buckling optimisation of a...][research_wang_wan_2021]
- [Composite wing structure of light amphibious airplane design...][research_chinvorarat_2021]
- [Failure modeling of composite wing leading edge under bird...][research_long_mu_2021]
- [Loads analysis and structural optimization of a high aspect...][research_sinha_klimmek_2021]
- [A Reduced Order Model based on Artificial Neural Networks for...][research_torregrosa_gil_2022]
- [A quasi-zero-stiffness vibration isolator using bi-stable...][research_li_li_2022]
- [Equivalent stiffness calculation of composite hat stiffened...][research_qiu_2022]
- [Impact-under-load damage tolerance of a fibre metal laminate][research_rathnasabapathy_mouritz_2022]
- [Vibration of variable stiffness composite laminate and hybrid...][research_karimi_khorshidi_2022]
- [A novel parallel method for layup optimization of composite...][research_liu_featherston_2023]
- [Modeling, analysis and validation of the structural response...][research_kilimtzidis_giannaros_2023]
- [Optimally stacked hygrothermally stable composite laminate...][research_kumarshakya_sekharpadhee_2023]
- [Uncertainty quantification of bistable variable stiffness...][research_suraj_anilkumar_2023]
- [A geometrically nonlinear Hellinger Reissner shell element...][research_liguori_zucco_2024]
- [Analytical Assessment of Composite L Angle Strength Under...][research_kcs_james_2024]
- [Buckling optimization of variable stiffness composite wing...][research_huang_wang_2024]
- [Effects of Coupled Thickness Variation on the Aeroelastic...][research_leitch_stodieck_2024]
- [Performance Evaluation of Structural Health Monitoring System...][research_galasso_ciminello_2024]
- [A general numerical method for the design of multi-ply...][research_wang_wang_2025]
- [Aeroelastic Coupled Mode Behavior of Swept Composite Wing][research_elshazly_kassem_2025]
- [Data-driven failure criteria prediction in composite wing...][research_magliacano_tufano_2025]
- [Nonlinear aeroelastic analysis of a skew reinforced composite...][research_vilela_donadon_2025]
- [The influence of coupled thickness variation in the...][research_leitch_stodieck_2025]
- [Composite laminate damage identification via Gabor-based...][research_mengzhu_zhitao_2026]
- [Physics-guided machine learning for the failure prediction of...][research_li_miranda_2026]

### Transonic wing design is computed now

**The Grumman K Mod 2 section was developed for a design competition and refined in tunnels.** Its modern
equivalent is produced by optimisation against a computational model, and the shock position that the X-29's
planform argument was built around is now an output rather than an input.

- [Aerodynamic Load Analysis of a Variable Camber Continuous...][research_tingeric_daotung_2015]
- [Aerodynamic optimization method of supercritical airfoil...][research_chen_zhang_2015]
- [Computational Evaluation and Linear Stability of a Transonic...][research_roberts_reed_2015]
- [DLR natural and hybrid transonic laminar wing design...][research_streit_wedler_2015]
- [Development of Variable Camber Continuous Trailing Edge Flap...][research_nguyennhan_kaulupender_2015]
- [Mechanical and Aerodynamic Study of Trailing Edge Variable...][research_shen_bai_2015]
- [Multi-Objective Optimization of a Transonic Compressor Rotor...][research_luo_liu_2015]
- [Supercritical natural laminar flow airfoil optimization for...][research_zhang_fang_2015]
- [The Multi-point Optimization of Shock Control Bump with...][research_mazaheri_nejati_2015]
- [The application of the gradient-based adjoint multi-point...][research_mazaheri_nejati_2015_b]
- [Aerodynamic Modeling of Transonic Aircraft Using Vortex...][research_chaparrodaniel_fujiwaragustavoec_2016]
- [Application of the adjoint multi-point and the robust...][research_mazaheri_nejati_2016]
- [Comparison of Passive Flow Control Methods for a Cavity in...][research_saddington_thangamani_2016]
- [Comparison of stochastic estimation methods with conditional...][research_arnault_dandois_2016]
- [Development of variable camber wing with morphing leading and...][research_takahashi_yokozeki_2016]
- [Efficient aerodynamic shape optimization of transonic wings...][research_liu_song_2016]
- [Experimental study of transonic buffet phenomenon on a 3D...][research_dandois_2016]
- [Influence of the number and location of design parameters in...][research_andresperez_gonzalezjuarez_2016]
- [Planform Dependency on Airfoil Design Results for Supersonic...][research_kishi_kanazaki_2016]
- [Supercritical wing design based on airfoil optimization and...][research_zhao_zhang_2016]
- [Adjoint method-based inverse design of transonic compressor...][research_ziegler_2017]
- [Aerodynamic optimization and mechanism design of flexible...][research_lu_tian_2017]
- [Aerodynamic shape optimization of a transonic fan by an...][research_tang_luo_2017]
- [High-Angle-of-Attack F-16XL Flight Simulations at Sub- and...][research_hitzel_2017]
- [NUMERICAL 3D TRANSONIC FLOW SIMULATION OVER A WING][research_velkova_2017]
- [Natural laminar flow airfoil shape design at transonic...][research_chen_tang_2017]
- [Natural laminar flow shape optimization in transonic regime...][research_tang_chen_2017]
- [Optimization of bump and blowing to control the flow through...][research_mazaheri_khatibirad_2017]
- [Passive shock wave/boundary layer control of wing at...][research_zhou_chen_2017]
- [The Application of Suction and Blowing in Performance...][research_mazaheri_nejati_2017]
- [Transonic Numerical and Experimental Evaluation of...][research_paul_rein_2017]
- [Transonic buffet control research with two types of shock...][research_tian_gao_2017]
- [Using Surface Sensitivity from Mesh Adjoint for Transonic...][research_hinchliffe_qin_2017]
- [Adjoint aerodynamic optimization of a transonic fan rotor...][research_tang_luo_2018]
- [Design of a transonic wing with an adaptive morphing trailing...][research_burdette_martins_2018]
- [Designing a Shock Control Bump Array for a Transonic Wing...][research_jones_jarrett_2018]
- [Drag Characterization Study of Variable Camber Continuous...][research_kaul_nguyen_2018]
- [Influence of flexibility on the steady aeroelastic behavior...][research_schewe_mai_2018]
- [Study on Global Aerodynamic Shape Optimization of Transonic...][research_duan_fan_2018]
- [The flow separation development analysis in subsonic and...][research_placek_ruchala_2018]
- [Transonic Buffet Control Research on Supercritical Wing Using...][research_jiang_tian_2018]
- [Wing Buffeting Control at Transonic Flight Velocities with...][research_wing_buffeting_2018]
- [A methodology for simulating 2D shock-induced dynamic stall...][research_aljaburi_feszty_2019]
- [Adjoint-Based Geometrically Constrained Aerodynamic...][research_su_ma_2019]
- [Analysis of a civil aircraft wing transonic shock buffet...][research_masini_timme_2019]
- [Control of Transonic Buffet by Shock Control Bumps on...][research_mayer_lutz_2019]
- [Data-driven constraint approach to ensure low-speed...][research_li_he_2019]
- [Investigation of Shock Motion in Transonic Flow Using an...][research_hope_kunz_2019]
- [Natural Laminar Flow Optimization of Transonic Nacelle Based...][research_wang_sun_2019]
- [Optimization of Supercritical Airfoil Considering the...][research_li_zhang_2019]
- [Optimization of Supercritical Airfoil Design with Buffet...][research_xu_saleh_2019]
- [Performance Enhancement of the Flexible Transonic...][research_bartelsroberte_stanfordbretk_2019]
- [Shock Control of a Low-Sweep Transonic Laminar Flow Wing][research_zhu_li_2019]
- [Transonic Airfoil Design and Optimization for an Unmanned Air...][research_kasimbiber_trentonwhite_2019]
- [Transonic buffet control by rearward Buffet Breather on...][research_jiang_tian_2019]
- [Transonic static aeroelastic and longitudinal aerodynamic...][research_wang_2019]
- [Using Shock Control Bumps to Improve Transonic Fan/Compressor...][research_john_qin_2019]
- [A Numerical Investigation of the Geometric Parametrisation of...][research_geoghegan_giannelis_2020]
- [Aerodynamic Design Optimization of Transonic...][research_li_wang_2020]
- [Aerostructural Design Exploration of a Wing in Transonic Flow][research_bons_martins_2020]
- [Design Criteria for Variable Camber Compliant Wing Aircraft...][research_you_kim_2020]
- [Experimental investigation of the transonic...][research_sun_miao_2020]
- [Identification of nonlinear aerodynamic systems with...][research_liu_gao_2020_b]
- [Scale-Resolving Simulations of a Civil Aircraft Wing...][research_masini_timme_2020]
- [Shape optimization to improve the transonic fluid-structure...][research_chen_gao_2020]
- [Subsonic Ultra Green Aircraft Research Phase III Mach 0.75...][research_christopherkdroney_anthonyjsclafani_2020]
- [Surrogate-based aeroelastic loads prediction in the presence...][research_brouwer_mcnamara_2020]
- [Wide domain simulations of flow over an unswept laminar wing...][research_zauner_sandham_2020]
- [Adaptive-surrogate-based robust optimization of transonic...][research_yao_ma_2021]
- [Benefit Assessment of Low-Sweep Transonic Natural Laminar...][research_fan_yu_2021]
- [Control of shock-induced vortex breakdown on a...][research_kurade_venkatakrishnan_2021]
- [Deep learning based multistage method for inverse design of...][research_lei_bai_2021]
- [Design Optimization of a Dual-Bleeding Recirculation Channel...][research_vuong_kim_2021]
- [Design of Low-Speed Slotted, Natural-Laminar-Flow Airfoil...][research_coder_2021]
- [Structural and Aeroelastic Studies of Wing Model with Metal...][research_tsushima_saitoh_2021]
- [Subcritical and supercritical nonlinear aeroelastic behavior...][research_zhou_huang_2021_b]
- [Thermal control of transonic shock-boundary layer interaction...][research_sengupta_roy_2021]
- [Transonic Static Aeroelastic Numerical Analysis of Flexible...][research_zhang_guo_2021]
- [Unsteady Simulation of Transonic Buffet of a Supercritical...][research_zhang_yang_2021]
- [Vortex-Generating Shock Control Bumps for Robust Drag...][research_deng_qin_2021]
- [Adjoint-based unsteady shape optimization to suppress...][research_chen_gao_2022]
- [Aerodynamic Data-Driven Surrogate-Assisted...][research_wu_zuo_2022]
- [Aerodynamic Design Optimization of a Transonic...][research_chau_zingg_2022]
- [Aircraft Cruise Drag Reduction Through Variable Camber Using...][research_reist_koo_2022]
- [Comparison of Computational Predictions of the Mach 0.80...][research_sallyaviken_craigahunter_2022]
- [Controlling transonic shock boundary layer interactions over...][research_chakraborty_roy_2022]
- [IMPLEMENTATION OF TRANSONIC AREA RULE AND SWEPT BACK DELTA...][research_singh_dwivedi_2022]
- [Investigation and Design of the Transonic Laminar Flow...][research_niu_li_2022]
- [Low-Noise Blade Design Optimization for a Transonic Fan Using...][research_wu_wilson_2022]
- [Numerical Simulation Research on Static Aeroelastic Effect of...][research_guo_zhang_2022]
- [Numerical investigation on the thermal-hydraulic performance...][research_han_guo_2022]
- [OPTIMIZATION OF WING PROFILE IN TRANSONIC FLOW][research_pham_2022]
- [Optimal shape design and transition uncertainty analysis of...][research_tang_zhang_2022]
- [Robust Design of Transonic Natural Laminar Flow Wings Under...][research_sabater_bekemeyer_2022]
- [Aerodynamic Optimization and Fuel Burn Evaluation of a...][research_chau_zingg_2023]
- [Closed-Loop Control of Transonic Buffet Using Active Shock...][research_deng_zhang_2023]
- [Comparative study of recent metaheuristics for solving a...][research_wansasueb_panagant_2023]
- [Design Exploration of Transonic Airfoils for Natural and...][research_sudhi_radespiel_2023]
- [Design and Optimization of a New Heterogeneous Printed...][research_chen_zhao_2023]
- [Double-decoupled inverse design of natural laminar flow...][research_zhang_li_2023]
- [Effect of Air Jet Vortex Generators on the Shock Wave...][research_dai_zhang_2023]
- [Fast Inverse Design of Transonic Airfoils by Combining Deep...][research_deng_yi_2023]
- [High-fidelity aeroelastic transonic analysis using...][research_grifo_gulizzi_2023]
- [Numerical optimization of transonic natural laminar flow...][research_yan_zhang_2023]
- [On the Co-existence of Transonic Buffet and Separation-Bubble...][research_zauner_moise_2023]
- [Passive Transonic Shock Control on Bump Flow for Wing Buffet...][research_dipasquale_prince_2023]
- [Resolvent analysis of a finite wing in transonic flow][research_houtman_timme_2023]
- [Study on Optimization Design of Airfoil Transonic Buffet with...][research_chen_gao_2023]
- [A deep reinforcement learning optimization framework for...][research_liu_zhang_2024]
- [Aerodynamic shape optimization in transonic conditions...][research_serani_diez_2024]
- [Design Optimization of Blade Tip in Subsonic and Transonic...][research_duan_he_2024]
- [Design and CFD Analysis of Supercritical Airfoil 0714 Under...][research_design_and_2024]
- [Design of Hybrid-Laminar-Flow-Control Wing and Suction System...][research_prasannakumar_sudhi_2024]
- [Determination of the features of integrated design of civil...][research_pelykh_andryushchenko_2024]
- [Effects of structural geometric nonlinearities on the...][research_ye_yang_2024]
- [INVESTIGATION OF AERODYNAMIC CHARACTERISTICS OF SWEPT C-WING...][research_samputh_moey_2024]
- [Improving transonic performance with adjoint-based NACA 0012...][research_ntantis_xezonakis_2024]
- [Mesh-Agnostic Decoders for Supercritical Airfoil Prediction...][research_li_zhang_2024_d]
- [Shape optimization of annular transonic thrust nozzles via...][research_narimani_joulaei_2024]
- [Three-Dimensional Unsteady Aerodynamic Optimization of a...][research_wu_wang_2024]
- [A Comparison of Modern Metaheuristics for Multi-Objective...][research_phuekpan_khammee_2025]
- [Aerodynamic Characteristics Analysis of Transonic Wing Flow...][research_wang_2025_b]
- [Aerodynamic Shape Optimization of NACA 64-208 Airfoil at...][research_maslanka_kachel_2025]
- [Conceptual design of next-generation stealth fighter aircraft...][research_surwase_kumar_2025]
- [D-optimal polynomial chaos expansion for adjoint-based...][research_ji_yang_2025]
- [Design and aerodynamic analysis of a morphing joined-wing...][research_guo_wang_2025]
- [Multi-Objective Optimization of Transonic Variable Camber...][research_wang_feng_2025]
- [Numerical study on flow and heat transfer characteristics of...][research_zhao_wang_2025]
- [Study on leading-edge vortex/shock interaction and unsteady...][research_yang_wu_2025]
- [Transonic Aerodynamic Performance Analysis of a CRM...][research_hanman_yao_2025]
- [Transonic aeroelasticity design method with application to a...][research_zhong_ying_2025]
- [Aerodynamic Optimization of a Cruise-Slotted Transonic...][research_chau_piotrowski_2026]
- [Aerodynamic Performance of Camber-Morphing Airfoils in...][research_aamir_abbasi_2026]
- [Aeroelastic Reduced-Order Model Differential Equations in...][research_candon_marzocca_2026]
- [Analysis of Wing Section Circulation Control Jet Bistability...][research_polonsky_2026]
- [Analysis of bump winglet synergistic control in a transonic...][research_yang_guo_2026]
- [Bayesian Forward Design Methodology for Laminar Transonic...][research_kakkar_streit_2026]
- [DESIGN OF SUPERCRITICAL AIRFOIL FOR SHOCK WAVE REDUCTION...][research_park_kang_2026]
- [Multi-point aerodynamic shape optimization of transonic...][research_zhong_wang_2026]
- [Numerical Analysis of Shock Control Bumps for Delaying...][research_zhang_deng_2026]
- [Range-Based Problem with Varying Design Point for Transonic...][research_poole_allen_2026]
- [SuperWing a comprehensive transonic wing dataset for...][research_yang_tang_2026]
- [Transonic aeroelastic stability analysis of launch vehicles...][research_shi_gao_2026]
- [Transonic deep stall of a free-to-pitch rigid wing][research_currao_jiang_2026]
- [Transonic wind-tunnel testing of a slotted...][research_coder_2026]
- [Waste textile decolorization using supercritical carbon...][research_tayebwa_morshed_2026]

- [C2 Approach Agility, Autonomy Briefing Charts][research_alberts_conley_2015]
- [Hydrodynamic Drag Reduction][research_taylor_wilson_2015]
- [Optimization and analysis of shock wave/boundary layer...][research_mazaheri_kiani_2015]
- [Pitfalls of the Past Learning Disabilities That Hinder...][research_bardo_2015]
- [Comparison of hypersonic aircraft quasi horizontal maneuver...][research_anon_2016]
- [Dynamics of sideslip perching maneuver under dynamic stall...][research_feroskhan_go_2016]
- [Improved control performance of the 3‐DoF aeroelastic wing...][research_szollosi_baranyi_2016]
- [Interconnected Observers for Robust Decentralized Estimation...][research_li_sanfelice_2016]
- [Performance comparison of linear and nonlinear vibration...][research_ebrahimzade_dardel_2016]
- [Range performance evaluation from the flight tests of a...][research_minwalla_thomas_2016]
- [The aeroelastic characteristics of high aspect ratio wing][research_yang_yue_2016]
- [Using a shock control bump to improve the performance of an...][research_mazaheri_khatibirad_2016]
- [Command Governor Approach to Maneuver Limiting in Fighter...][research_simon_harkegard_2017]
- [Extreme aircraft maneuver under sudden lateral CG movement...][research_mukherjee_sinha_2017]
- [Flight Dynamics of Helicopter Under Steady Maneuver...][research_sakthivel_venkatesan_2017]
- [Numerical Investigations of Fan-in-Wing Aerodynamic...][research_sheng_zhao_2017]
- [Thermoelastic vibration and maneuver control of smart...][research_fazelzadeh_azadi_2017]
- [Transient performance improvement of model reference adaptive...][research_davanipour_khayatian_2017]
- [A new jig-shape optimization method for the high aspect ratio...][research_yuan_huo_2018]
- [A novel metal-composite joint and its structural performance][research_tang_liu_2018]
- [Computational investigation of vortex structure and breakdown...][research_hadidoolabi_ansarian_2018]
- [Control strategy of sideslip perching maneuver under dynamic...][research_feroskhan_go_2018]
- [Effect of shooting and blast-induced gust on nonlinear...][research_mardanpour_izadpanahi_2018]
- [Maneuver load alleviation for high performance aircraft...][research_li_huang_2018]
- [Nonlinear reduced order model of high aspect ratio...][research_c_yharmin_2018]
- [Optimization of Variable-Camber Continuous Trailing-Edge Flap...][research_ting_chaparro_2018]
- [Performance limitation of networked control systems with...][research_qiao_wu_2018]
- [Unmanned aircraft automatic flight control algorithm in loop...][research_rogalski_2018]
- [A comparative study of nonlinear aeroelastic models for high...][research_modaressaval_bakhtiarinejad_2019]
- [Black-box Modeling for Aircraft Maneuver Control with...][research_kim_oh_2019]
- [Determination of Parameters during Quasi-Steady Stall...][research_srivastava_2019]
- [Energy Harvesting Performance of a Wing Panel for Aeroelastic...][research_shan_tian_2019]
- [Practical Coupling Rejection Control for Herbst Maneuver with...][research_liu_chen_2019]
- [Scalar Reference Governor for Constrained Maneuver and Shape...][research_orourke_kolmanovsky_2019]
- [Transverse function control with prescribed performance...][research_dai_he_2019]
- [Adaptive control of unactuated dynamical systems through...][research_gruenwald_yucelen_2020]
- [Computational Fluid Dynamic for Performance Hydrofoil due to...][research_zaubeu_2020]
- [New Methodology for Aircraft Performance Model Identification...][research_ghazi_botez_2020]
- [Unmanned aircraft automatic flight control algorithm in a...][research_rogalski_rzucidlo_2020]
- [A Case Study on the Software Test Criteria Derivation Related...][research_baek_2021]
- [Aeroelastic Demonstrator Wing Design for Maneuver Load...][research_sodja_werter_2021]
- [Aircraft Mass Properties Estimation During Airdrop Maneuver A...][research_dehghanmanshadi_saghafi_2021]
- [An optimization design method for aerodynamic configuration...][research_zong_sun_2021]
- [Buckling performance of curvilinearly grid-stiffened...][research_alhajahmad_mittelstedt_2021]
- [CFD Simulations and External Shape Optimization of Missile...][research_cfd_simulations_2021]
- [DESIGN, PERFORMANCE ANALYSIS OF WING, AND MANUFACTURING OF...][research_daspatel_kumarkaruparthi_2021]
- [Flight-Test Validation of a Takeoff Performance Uncertainty...][research_sobester_2021]
- [Modeling and analysis of high aspect ratio wing considering...][research_fu_yang_2021]
- [Numerical Virtual Flight Simulation of Quasi-Cobra Maneuver...][research_wang_ma_2021]
- [Performance Evaluation of Stewart-Gough Flight Simulator...][research_zhao_wu_2021]
- [Structural performance of composite tidal turbine blades][research_gonabadi_oila_2021]
- [The effect of repeated high-fidelity in situ simulation-based...][research_maenhout_billiet_2021]
- [Unmanned aircraft automatic flight control algorithm in an...][research_rogalski_rzucidlo_2021]
- [Aeroelastic Optimization of the High Aspect Ratio Wing with...][research_ghalandari_mahariq_2022]
- [Aeroelastic Simulation of High-Aspect Ratio Wings with...][research_wang_zhao_2022]
- [Aeroelastic evaluation of a flexible high aspect ratio wing...][research_bras_warwick_2022]
- [Cooperation of Trailing-Edge Flap and Shock Control Bump for...][research_zhang_deng_2022]
- [Enhancement of aeroelastic performance of a smart delaminated...][research_varun_mondal_2022]
- [Evaluation of the Mass and Aerodynamic Efficiency of a High...][research_kretov_tiniakov_2022]
- [Global aero-structural design optimization of composite wings...][research_wunderlich_dahne_2022]
- [Model reference adaptive control of piecewise affine systems...][research_liu_buss_2022]
- [Performance Accretion in Delay Compensation of Networked...][research_kumar_kumar_2022]
- [Structural design and mechanical performance of composite...][research_zia_liu_2022]
- [Study on Effect of Aerodynamic Configuration on Aerodynamic...][research_li_yuan_2022]
- [Time-domain Analytical Method for Aeroelastic Analysis of...][research_rehman_2022]
- [A multi resonant wave-absorbing honeycomb sandwich structure...][research_zhao_xing_2023]
- [Application of the topological optimization method for the...][research_balunov_solyaev_2023]
- [Cessna 172 G1000 Aircraft Airfoil Optimization Using Particle...][research_zeleke_asfaw_2023]
- [Compressor and Valve Control Performance Implications on...][research_mansy_faruque_2023]
- [Influence of structural features in the performance of...][research_rosa_pouca_2023]
- [Multidisciplinary structural optimization of novel...][research_kilimtzidis_kostopoulos_2023_b]
- [Nolinear Static Aeroelastic Analysis and Optimization for...][research_zhao_yang_2023]
- [Prescribed performance control for uncertain underactuated...][research_liu_chen_2023]
- [Prescribed performance event‐triggered control for MIMO...][research_fan_wang_2023]
- [Robust Data-Enabled Predictive Control Tractable Formulations...][research_huang_zhen_2023]
- [Robust Stability and Performance Analysis of Incremental...][research_pollack_vankampen_2023]
- [Robust backstepping control for maneuver aircraft based on...][research_shen_chen_2023]
- [Aerodynamics of a flat girder Effects of its aspect ratio and...][research_li_zheng_2024]
- [Assessment of the Aerodynamic and Aeroelastic Performance of...][research_badhurshah_alvarez_2024]
- [Bifurcation analysis of wing rock and routes to chaos of a...][research_jiang_li_2024]
- [Development of high-fidelity air handling unit fault models...][research_casillas_chen_2024]
- [Fluid structure interaction analysis of a high aspect ratio...][research_onkar_kumar_2024]
- [High Aspect Ratio Composite Wings Geometrically Nonlinear...][research_farsadi_ahmadi_2024]
- [Model-based manoeuvre analysis a path to a new paradigm in...][research_shayak_girdhar_2024]
- [Study of performance of an internal strut-based thrust...][research_soundararajan_sridhar_2024]
- [Aerodynamic Performance of Swayasa Aircraft Wing Model...][research_aerodynamic_performance_2025]
- [Conceptual Design and Aerostructural Trade-Offs in Hydrogen...][research_wahler_ma_2025]
- [Low-Speed Airfoil Optimization for Improved Off-Design...][research_pangas_gamboa_2025]
- [Multi-energy field composite manufacturing of...][research_qian_lu_2025]
- [Nonlinear dynamic analysis of high aspect ratio wings via IHB...][research_wu_wang_2025]
- [Novel integrated aerodynamic configuration with ventral and...][research_sun_luo_2025]
- [Numerical Method for Aeroelastic Simulation of Flexible...][research_chen_he_2025]
- [Stealth-Maneuver Generation for Non-Stealth Aircraft A...][research_demir_altunkaya_2025]
- [Uncertainty qualification of aerodynamic performance of a...][research_xu_zhang_2025]
- [ℒasso ℳ𝒫𝒞‐Based ℒ1 Adaptive Control for Uncertain Euler...][research_ahmadian_alitalebi_2025]
- [Aerodynamic Analysis and Design of a Sliding Drag Reduction...][research_kajiwara_ton_2026]
- [Aerodynamic Performance and Vortex Structure Investigations...][research_bay_kara_2026]
- [Aerodynamic and Static Aeroelastic Analysis of a High-Agility...][research_reinbold_breitsamter_2026]
- [Coupling Dynamic Stall with Lifting-Line Theory for Gust and...][research_abunawas_qawasmeh_2026]
- [Longitudinal flight performance improvement strategy for...][research_wang_hu_2026]
- [Near-Terrain Flight Operations and Performance of Unmanned...][research_bhandari_bhandari_2026]
- [Nonlinear model predictive control trajectory tracking for a...][research_nguyen_prodan_2026]
- [Parallelized complex method for multidisciplinary...][research_namanikoureh_shahverdi_2026]
- [Trajectory Design and Control of a Small-Scale Helicopter...][research_fattizzo_giulietti_2026]

- [Effect of Canard Interactions on Aerodynamic Performance of a...][research_silton_fresconi_2015]
- [Redesigning of a Canard Control Surface of an Advanced...][research_shrivastava_mohite_2015]
- [Effect of Sideslip on High-Angle-of-Attack Vortex Flow over...][research_chen_liu_2016]
- [Aerodynamic performance improvement of a canard control...][research_tahani_masdari_2017]
- [Characteristics of Steady Aerodynamics and Aerodynamic...][research_ito_iwashita_2017]
- [Wing/canard interference of a close-coupled canard...][research_qin_liu_2017]
- [Aerodynamic characteristics and flow field of delta wings...][research_mochizuki_yamada_2018]
- [Enhanced Maneuverability of a Delta-Canard Combat Aircraft by...][research_hitzel_osterhuber_2018]
- [Experimental Study and Neural Network Modeling of Aerodynamic...][research_ignatyev_khrabrov_2018]
- [Experimental investigation of the effects of sideslip on...][research_dong_shi_2019]
- [Influence of Gurney flaps on aerodynamic characteristics of a...][research_wei_zhan_2019]
- [Numerical and Experimental Determination of Canard Controlled...][research_numerical_and_2019]
- [Trim Strategy, Control Model, and Flight Dynamics...][research_gao_gao_2019]
- [Vortex generator effect and aerodynamic characteristic for...][research___2019]
- [Numerical investigation on hydrodynamic performance of new...][research_yao_liu_2020]
- [Numerical investigation of vortical flows over a...][research_yutuk_tikenogullari_2021]
- [Aerodynamic Study of Canard Parameter Configuration Principle...][research_jiang_tong_2022]
- [Flow Features and Aerodynamic Analysis of the Canard Missiles][research_kalugin_voropaev_2022]
- [Flow Field Study of Effect of Canard Location on Aircraft...][research_dwivedi_anitha_2022]
- [Three-Dimensional Flow Analysis over Canard Configuration in...][research_varun_dwivedi_2022]
- [A novel aerodynamic layout design of composite wing unmanned...][research_chen_gao_2023_b]
- [Multi-objective aerodynamic shape design optimization of...][research_yoo_jeong_2023]
- [Optimizing Supersonic Rocket Efficiency a Numerical Analysis...][research_goucem_khiri_2023]
- [The aerodynamic behavioral study of canard plane with fan...][research_komarov_zinchenko_2023]
- [Wind Tunnel Test Research for Aerodynamic Characteristic...][research_lee_lee_2023]
- [Wing Aerodynamic Optimization in the Presence of Interacting...][research_gupta_2023]
- [The working principles of canard wings and its aerodynamic...][research_lai_2024]
- [ANALYSIS OF AERODYNAMIC CHARACTERISTICS FOR CANARD CONTROLLED...][research_kim_kang_2025]
- [Advanced aerodynamic prediction software for versatile...][research_theerthamalai_mukesh_2025]
- [Aerodynamic Interference of Lift Surfaces During Transition...][research_fan_wang_2025]
- [Aerodynamic control analysis in a canard configuration for a...][research_szklarski_glebocki_2025]
- [Numerical investigation of a canard configuration in flat...][research_li_wang_2026]

### Handling qualities of augmented aircraft

**The X-29's flying qualities were the flying qualities of its control law**, which is true of every modern
combat aircraft and was still novel enough in 1984 to require saying. The equivalent-system criteria and the
treatment of control system time delay that the contemporary literature uses were being worked out in the
same decade.

- [Eigenstructure Control A Rotorcraft Handling Qualities...][research_srinathkumar_2015]
- [Handling Qualities Requirements for Future Personal Aerial...][research_perfect_jump_2015]
- [Handling Qualities of a Twin Ducted-Fan Aircraft An...][research_grant_stol_2015]
- [Methods to Assess the Handling Qualities Requirements for...][research_perfect_jump_2015_b]
- [Application of Quantitative Measures for Analysing Aircraft...][research_hebbar_pashilkar_2016]
- [Handling qualities evaluation of an automatic slung load...][research_nonnenmacher_jones_2016]
- [Use of Time-Frequency Representations for Interpreting...][research_tritschler_oconnor_2016]
- [Vision-based control for helicopter ship landing with...][research_truong_rakotomamonjy_2016]
- [“Fast Simulation” in Evaluating Pilot/Aircraft Performance...][research_hess_2016]
- [Handling Qualities Assessment of an Unmanned Aircraft Using...][research_kim_kunz_2017]
- [Inverse simulation system for evaluating handling qualities...][research_zhou_wang_2017]
- [Longitudinal Pilot-induced Oscillation Tendencies Prediction...][research_yin_wang_2017]
- [Pilot induced oscillation suppression controller design via...][research_tran_sakamoto_2017]
- [A handling qualities analysis tool for rotorcraft conceptual...][research_lawrence_theodore_2018]
- [Development of a Multi-Directional Manoeuvre for Unified...][research_dussart_lone_2019]
- [Methodology to Analyse Handling Qualities Under Force...][research_rauer_2019]
- [Prediction of nonlinear pilot-induced oscillation using an...][research_xu_tan_2019]
- [Technical Measures Perspectives in Selection of Handling...][research_chowhan_arya_2019]
- [Advancements in Predictions of Flying Qualities...][research_efremov_efremov_2020]
- [Conceptual Design, Flying, and Handling Qualities Assessment...][research_humphreysjennings_lappas_2020]
- [Effect of Control System Augmentation on Handling Qualities...][research_theodore_malpica_2020]
- [SIMULATED PILOT-IN-THE-LOOP TESTING OF HANDLING QUALITIES OF...][research_portapas_cooke_2020]
- [Study on the Handling Qualities Enhancement of Fixed-wing...][research_lee_kim_2020]
- [Unmanned Aerial Vehicle Flying Qualities Flight Test...][research_jing_qi_2020]
- [A Hybrid Incremental Nonlinear Dynamic Inversion Control for...][research_ji_kim_2021]
- [A survey of human pilot models for study of Pilot-Induced...][research_bidinotto_moura_2021]
- [Evaluation of Unmanned Aircraft Flying/Handling Qualities...][research_callaghan_kunz_2021]
- [Handling qualities of fixed-pitch, variable-speed...][research_bahr_mckay_2021]
- [Helicopter Handling Qualities A study in pilot control...][research_memon_white_2021]
- [On the Handling Qualities of Two Flying Wing Aircraft...][research_campos_marques_2021]
- [Pilot-Induced Oscillation Prevention During the Aircraft...][research_zaytseva_kuznetsov_2021]
- [A Turbulence Model for Flight Simulation and Handling...][research_henriquezhuecas_white_2022]
- [Advanced pilot modeling for prediction of rotorcraft handling...][research_ji_lu_2022]
- [Coaxial-Compound Helicopter Flight Control Design and...][research_berger_blanken_2022_b]
- [Development and Flight Validation of Proposed Unmanned Aerial...][research_ivler_truong_2022]
- [ESO-based nonlinear flying boom attitude control with the...][research_cao_xu_2022]
- [Faster-than-realtime inverse simulation method for tiltrotor...][research_yuan_thomson_2022]
- [Handling Qualities in Rotorcraft Conceptual Design][research_zanoni_gerosa_2022]
- [Handling Qualities of a New Last-Mile Vehicle][research_dhondt_degryse_2022]
- [PREDICTED LEVELS OF HANDLING QUALITIES OF KA-62 HELICOPTER...][research_kozhanov_suvorova_2022]
- [PROSPECTIVE MEANS FOR THE AIRCRAFT PILOT INDUCED OSCILLATION...][research_efremov_shcherbakov_2022]
- [Tiltrotor Flight Control Design and High-Speed Handling...][research_berger_blanken_2022]
- [Valve control of a hydraulically interconnected suspension...][research_jafari_mashadi_2022]
- [Handling Qualities Assessment and Performance Evaluation for...][research_herrington_zahed_2023]
- [An Objective Handling Qualities Assessment Framework of...][research_li_zhang_2024_b]
- [Approach to Aircraft Handling Qualities Prediction][research_lampton_klyde_2024]
- [Co-design of a multirotor UAV with robust control considering...][research_mabboux_pommierbudinger_2024]
- [Explicit Uncertainty Quantification for Probabilistic...][research_saetti_rogers_2024]
- [Handling Qualities Assessment and Discussion for Helicopter...][research_wang_chen_2024]
- [Building Credible VTOL Flight Models for Handling Quality...][research_favaro_rylko_2025]
- [Handling Qualities sizing for aerial vehicles based on...][research_antonakis_2025]
- [Model Reference Control for Reducing Pilot-Induced...][research_newton_kroo_2025]
- [Modeling multirotor wake interference in quadrotor eVTOL...][research_wang_ji_2025]
- [Reinforcement-learning-based aircraft handling qualities...][research_antonakis_2025_b]
- [Analysis of Structural Flexibility Effects on Handling...][research_cavalcanti_uehara_2026]
- [Development and Evaluation of New Mission Task Elements to...][research_jusko_berger_2026]
- [Euclid sUAV Handling Qualities Evaluation Through Flight...][research_ioannis_ioannis_2026]

### Five Subjects That Were Not Fields in 1984

**The sections above track what happened to bodies of work the X-29 was part of.** The five that follow are
different. They are subjects that barely existed when the aircraft flew and that now bear directly on the
problems it was built to attack, which is the more useful half of a survey.

### Machine learning arrived in the middle of the problem

**The X-29's predictions came from panel methods, wind tunnels and engineering judgement, and the gaps between them and flight are documented in this article.**
Contemporary practice inserts a learned model at exactly those points, for unsteady aerodynamic prediction,
for reduced-order models of the flow, and for surrogate models that make an optimisation affordable.

**The relevant question is no longer whether these models are accurate but whether they can be trusted inside a control loop**,
which is the same question the X-29's designers faced about their own reduced-order models and answered with
a flight envelope and a great deal of instrumentation.

- [Lindhorst et al 2015][research_lindhorst_haupt_2015]
- [A Highly Efficient Aeroelastic Optimization Method Based on a...][research_zhiqiang_xiaozhe_2016]
- [An artificial neural network approach for aerodynamic...][research_tao_sun_2016]
- [Data-driven Model-Free Adaptive Control Tuned by Virtual...][research_data_driven_model_free_2016]
- [Efficient reliability analysis of laminated composites using...][research_haeri_fadaee_2016]
- [Multiobjective optimization of an aircraft wing design with...][research_caixeta_marques_2018]
- [Parametric optimization of high aspect ratio wing using...][research_s_sinha_2018]
- [Adaptive Wing Morphing Strategy and Flight Control Method of...][research_yan_li_2019]
- [Distributed Wildfire Surveillance with Autonomous Aircraft...][research_julian_kochenderfer_2019]
- [Prescribed performance control of morphing aircraft based on...][research_gong_wang_2019_b]
- [Amidst Data-Driven Model Reduction and Control][research_monshizadeh_2020]
- [Deep Learning Based Reduced Order Model for Airfoil-Gust and...][research_halder_damodaran_2020]
- [Flight Ticket Price Prediction using Machine Learning][research_flight_ticket_2020]
- [Flight performance analysis with data-driven mission...][research_lyu_liem_2020]
- [Multiple Aerodynamic Coefficient Prediction of Airfoils Using...][research_chen_he_2020]
- [Online model‐free reinforcement learning for the automatic...][research_abouheaf_gueaieb_2020]
- [Quality Control Method of Exploration and Development Data...][research_quality_control_2020]
- [Smart wing load alleviation through optical fiber sensing...][research_wada_tamayama_2020]
- [An Approach of Applying Machine Learning Model in Flight...][research_somani_2021]
- [Continuous terminal sliding mode control using novel fuzzy...][research_chu_hou_2021]
- [Damage imaging in skin-stringer composite aircraft panel by...][research_cui_azuara_2021]
- [Data-driven design exploration method using conditional...][research_yonekura_suzuki_2021]
- [Data-driven identification of unsteady-aerodynamics phenomena...][research_raiola_discetti_2021]
- [Data-driven modeling for unsteady aerodynamics and...][research_kou_zhang_2021]
- [Energy-Optimal Flight Strategy for Solar-Powered Aircraft...][research_ni_wu_2021]
- [Ensemble Machine Learning Model for Software Defect Prediction][research_ensemble_machine_2021]
- [Flight Control of a Multicopter using Reinforcement Learning][research_dapolito_sulzbachner_2021]
- [Hybrid Reinforcement Learning Control for a Micro Quadrotor...][research_yoo_jang_2021]
- [Multi-fidelity convolutional neural network surrogate model...][research_liao_song_2021]
- [Multi-fidelity deep neural network surrogate model for...][research_zhang_xie_2021]
- [Neural Network-Based Model Reduction of Hydrodynamics Forces...][research_farooq_saeed_2021]
- [Online learning‐based model predictive control with Gaussian...][research_maiworm_limon_2021]
- [Probabilistic Flight Delay Predictions Using Machine Learning...][research_zoutendijk_mitici_2021]
- [Reinforcement learning for control of valves][research_siraskar_2021]
- [A Comparative Study of Machine Learning Techniques for...][research_a_comparative_2022]
- [A machine learning application in wine quality prediction][research_bhardwaj_tiwari_2022]
- [Adaptive Data-Driven Model Order Reduction for Unsteady...][research_nagy_fossati_2022]
- [Bearings only passive location of UAV in formation flight...][research_bearings_only_2022]
- [Beyond Persistent Excitation Online Experiment Design for...][research_vanwaarde_2022]
- [Data-driven nonlinear reduced-order modeling of unsteady...][research_zhang_ji_2022]
- [Data-driven reduced order model and simplicial homology...][research_zhao_wang_2022]
- [Enabling intelligent onboard guidance, navigation, and...][research_wilson_riccardi_2022]
- [Flight Fare Prediction Using Machine Learning][research_sarao_samanta_2022]
- [Machine Learning Approaches to Ambient Air Quality Prediction][research_x_2022]
- [Networked Control System Based on PSO-RBF Neural Network...][research_you_lei_2022]
- [Noninvasive acoustic time-of-flight measurements in heated...][research_greenhall_zerkle_2022]
- [Training a Neural-Network-Based Surrogate Model for...][research_ghazi_alhazmi_2022]
- [A Second-Order Network Structure Based on Gradient-Enhanced...][research_sun_feng_2023]
- [DYNAMIC FLIGHT AND HOTEL PRICE PREDICTION USING MACHINE...][research_dynamic_flight_2023]
- [Data-driven polynomial chaos-interval metamodel for dynamics...][research_guo_jin_2023]
- [Direct data driven safety control for aircraft flight...][research_jianhong_ramirezmendoza_2023]
- [FLIGHT TICKET PRICE PREDICTION USING MACHINE LEARNING][research_flight_ticket_2023]
- [Flight Delay Prediction Using Machine Learning][research_flight_delay_2023]
- [Flight delay causality Machine learning technique in...][research_mokhtarimousavi_mehrabi_2023]
- [Longitudinal Aerodynamic Parameter Estimation Using Neural...][research_peyada_ghosh_2023]
- [Machine learning-based identification of interpretable...][research_ackermann_haase_2023]
- [Modular Reinforcement Learning for Autonomous UAV Flight...][research_choi_kim_2023]
- [Network Traffic Anomaly Detection Model Based on Feature...][research_jiang_ji_2023]
- [Research on aerodynamic shape optimization of reentry vehicle...][research_zhu_sun_2023]
- [Research on flight technology evaluation based on machine...][research_research_on_2023]
- [Risk-sensitive Distributional Reinforcement Learning for...][research_seres_liu_2023]
- [Symmetric actor critic deep reinforcement learning for...][research_han_cheng_2023]
- [A Multi-Objective Optimization Design Method for...][research_nan_zheng_2024]
- [A Review of Reinforcement Learning for Fixed-Wing Aircraft...][research_richter_calix_2024]
- [A deep neural network reduced order model for unsteady...][research_baldan_guardone_2024]
- [Application of machine learning and neural network...][research_application_of_2024]
- [Combination Of Fused Machine Learning And Cascaded Levy...][research_combination_of_2024]
- [Data-Driven Control-Oriented Modeling for Response of Fluidic...][research_zhou_cheng_2024]
- [Data-driven reduced-order modeling for nonlinear aerodynamics...][research_moni_yao_2024]
- [Data‐based nonlinear learning control for aircraft trajectory...][research_wei_meng_2024]
- [Development of helium turbine loss model based on knowledge...][research_liu_zou_2024]
- [Digital Twin Framework for Aircraft Lifecycle Management...][research_kabashkin_2024]
- [Efficient machine learning-assisted failure analysis method...][research_ghosh_2024]
- [Identification of Uncertain Parameter in Flight Vehicle Using...][research_na_lee_2024]
- [Investigation of Deep Reinforcement Learning for...][research_xu_tian_2024]
- [Large Language Model Guided Reinforcement Learning Based...][research_han_yang_2024]
- [Machine Learning Analysis of Thermal Performance Indicator of...][research_aksoz_gunay_2024]
- [Multi-scale graph neural network for physics-informed fluid...][research_wei_freris_2024]
- [Nonlinear unsteady aerodynamic forces prediction and...][research_zhao_zhang_2024]
- [Online Safe Flight Control Method Based on Constraint...][research_zhao_xu_2024]
- [Prediction of Flight Areas using Machine Learning Algorithm][research_singh_yadav_2024]
- [Reinforcement Learning for Dual-Control Aircraft...][research_yuan_zhou_2024]
- [Rocket Thrust Vectoring Attitude Control based on...][research_garciarodriguez_martinezperez_2024]
- [Simulation of thermal-fluid coupling in silicon single...][research_shi_liu_2024_c]
- [Trajectory Tracking Control of Variable Sweep Aircraft Based...][research_cao_lu_2024]
- [A Hybrid Physics-Informed Neural Network PINN And Finite...][research_beitalmal_2025]
- [A data-driven modeling framework for nonlinear static...][research_white_hartl_2025]
- [A digital twin system for long-term slope deformation...][research_lyu_xu_2025]
- [A multi-fidelity surrogate model based on convolutional...][research_qin_yang_2025]
- [A physics-informed neural network for predicting the drag...][research_tian_zhao_2025]
- [Aerodynamic Shape Optimization of Rockets Based on a...][research_chen_qin_2025]
- [Airline Flight Delay Prediction Using Machine Learning...][research___2025]
- [An effective long short-term memory neural network-based...][research_wang_zhang_2025_b]
- [An uncertainty-aware deep learning framework-based robust...][research_wang_bhaduri_2025]
- [Application of SciML-Adapted PCMM to Deep Neural Network...][research_kirsch_fathi_2025]
- [Application of computational fluid dynamics and physics...][research_rehman_ekici_2025]
- [CFD-neural network collaborative optimization drives...][research_sun_lin_2025]
- [Convolutional neural network-based optimization model for...][research_convolutional_neural_2025]
- [Data-driven control of echo state-based recurrent neural...][research_damico_labella_2025]
- [Delay Compensation Strategy of Networked Control System Based...][research_tian_tang_2025]
- [Dynamic integral sliding mode control for nonminimum phase...][research_wang_zhang_2025]
- [Enhancing aerodynamic and aeroelastic performance of axial...][research_luo_chen_2025]
- [Ensemble Neural Network‐Based Approximate Model Predictive...][research_tong_du_2025]
- [Flight, aircraft, and crew integrated recovery policies for...][research_wang_mao_2025]
- [Fluid structure interaction analysis of pulsatile flow in...][research_urrehman_ekici_2025]
- [Neural network implementation of model predictive control...][research_khodaverdian_gohil_2025]
- [Neural network-assisted design optimization with adaptive...][research_liu_liu_2025]
- [Optimizing Material Shortages in Flight Catering with Machine...][research_optimizing_material_2025]
- [Physical-guided graph deep learning for composite pipelines...][research_jiang_hu_2025]
- [Recursive Gaussian Process-Based Safety Assurance Exploration...][research_kanou_ibuki_2025]
- [Reinforcement Learning-Based Evolving Flight Controller for...][research_shukla_benyamen_2025]
- [Robust Data‐Driven Control of LPV Systems With Safety...][research_zhou_liu_2025]
- [A Physics-Stabilized Self-Updating Digital Twin Framework...][research_karkadakattil_2026]
- [A data-driven airfoil generative design method and its...][research_liu_geng_2026]
- [A dual-branch physics-informed neural network for...][research_wang_ye_2026]
- [A physics-informed neural network for fluid structure coupled...][research_xia_li_2026]
- [An automated surrogate model generation framework for rapid...][research_golombek_bustamante_2026]
- [Analysis of major segmentation models for intracranial artery...][research_sarkar_huang_2026]
- [Automated bird flight pattern extraction and classification...][research_ostojic_sethi_2026]
- [Autonomous Tactical Decision-Making for Multi-Aircraft via...][research_xue_zhao_2026]
- [Conditional disturbance utilization-based intelligent...][research_wang_yi_2026]
- [Data-Driven Reduced-Order Modeling for Aeroelastic Load...][research_luo_yu_2026]
- [Deep reinforcement learning for carrier-based aircraft flight...][research_li_han_2026]
- [Domain adaptive relational graph convolutional network for...][research_xu_liu_2026]
- [Dynamic Multi-Stream Network with Confidence Gating for...][research_restifo_villa_2026]
- [Enhancing active disturbance rejection control design for...][research_wang_zhang_2026]
- [Flight Delay Prediction Using Machine Learning][research_alshammari_2026]
- [Flight Path Planning for UAVs Using Machine Learning-Guided...][research_flight_path_2026]
- [Flight Price Prediction Using Machine Learning and Deep...][research_flight_price_2026]
- [GW-RAR-PINN a novel physics-informed neural network framework...][research_yan_zhu_2026]
- [High-angle-of-attack maneuver flight control based on deep...][research_wang_weng_2026]
- [IA2UCS An Intelligent Atmospheric‐Adaptive UAV Control System...][research_divakar_bl_2026]
- [Integrated design method of aircraft RBF neural network-based...][research_fan_jiang_2026]
- [Machine Learning Techniques for Flight Delay Prediction][research_siddamma_seervi_2026]
- [Model Reference Adaptive Inverse Control of Nonlinear Systems...][research_salwan_hussain_2026]
- [Neural Network Model for Predicting Aerodynamic Parameters of...][research_cai_fan_2026]
- [Neural network-based structural optimization of tow-steered...][research_fina_bisagni_2026]
- [Optimization Strategy of Tunnel Lining Structural Analysis...][research_li_luo_2026]
- [Physics-Informed Neural Network Simulation of Proppant...][research_liu_shen_2026]
- [Physics-informed reinforcement learning based control for...][research_yang_wang_2026]
- [Priority-driven multi-objective reinforcement learning for...][research_zhang_wang_2026]
- [Reinforcement Learning-Based Speed and Altitude Control...][research_setiawarman_sasongko_2026]
- [Reinforcement learning-based prescribed performance control...][research_cao_chen_2026]
- [Reinforcement learning enhanced non-singular super-twisting...][research_toloei_ghaderi_2026]
- [Research on orbital prediction method of automatic...][research_guan_li_2026]
- [Robust Data-Driven Safe Policy Update With Lyapunov Stability...][research_volpe_salcuni_2026]
- [Robust reinforcement learning for nonlinear process control...][research_cui_khodaverdian_2026]

### Morphing structures are the tailoring idea carried further

**Aeroelastic tailoring changes a wing's response to load by fixing its internal geometry once.** Morphing
changes it while flying. The X-29's automatic camber control, which scheduled the flaperons as a function of
flight condition, is a coarse ancestor of this, and the record's own description of it as
**discrete variable camber** and as a low-cost alternative to smooth variable camber shows the designers
knew exactly which approximation they were making.

- [Aerodynamic Shape Optimization of an Adaptive Morphing...][research_lyu_martins_2015]
- [Analysis of flight dynamics for large-scale morphing aircraft][research_shi_wan_2015]
- [Conceptual Design and Experimental Demonstration of a...][research_zhang_zhou_2015]
- [Design space of embeddable variable stiffness bi-stable...][research_kuder_arrieta_2015]
- [Fluid/Structure-Interaction Analysis of the...][research_woods_dayyani_2015]
- [Magneto-mechanical actuation of ferromagnetic shape memory...][research_glock_canal_2015]
- [Aeroelastic study for folding wing during the morphing process][research_hu_yang_2016]
- [Design Segmented Stiff Skin for a Morphing Wing][research_xijuan_qiang_2016]
- [Fiber-reinforced polymers with integrated shape memory alloy...][research_hubler_nissle_2016]
- [Optimum Wing Shape of Highly Flexible Morphing Aircraft for...][research_su_swei_2016]
- [Dynamic Modeling and Active Morphing Trajectory-Attitude...][research_guo_hou_2017]
- [Flight dynamic modeling and control for a telescopic wing...][research_yue_zhang_2017]
- [Investigation of a Morphing Wing Solar-Powered Unmanned...][research_wu_xiao_2017]
- [Morphing wing with skin discontinuity kinematic concept][research_tarnowski_2017]
- [The morphing trailing-edge wing optimization design of the...][research_guo_bai_2017]
- [Analysis of Asymmetric Control Efficiency for Folding Wing...][research_xu_zhang_2018]
- [Design and Analysis of a Novel Mechanism for the Morphing of...][research_sahin_yaman_2018]
- [Effectiveness of Twist Morphing Wing on Aerodynamic...][research_kaygan_ulusoy_2018]
- [Structural Design and Optimization of an Aircraft Morphing...][research_michaud_dalir_2018]
- [Structural design and optimization of a morphing wing...][research_ding_zhou_2018]
- [Synthesis, Analysis, and Design of a Novel Mechanism for the...][research_sahin_yaman_2018_b]
- [Unsteady aerodynamic characteristics of a morphing wing][research_xiang_liu_2018]
- [Analysis and optimization of morphing wing aerodynamics][research_klimczyk_goraj_2019]
- [Augmented Aircraft Performance with the Use of Morphing...][research_moens_2019]
- [Computational Analysis of 3D Lattice Structures for Skin in...][research_alsaidi_joe_2019_b]
- [Disturbance rejection control of morphing aircraft based on...][research_gong_wang_2019]
- [Dynamic Distributed Morphing Control of an Aeroelastic Wing...][research_zhang_wang_2019]
- [Experimental Study of a Morphing Annular Wing][research_traub_2019]
- [Geometrically nonlinear electro-aeroelastic framework for...][research_tsushima_arizono_2019]
- [Geometrically nonlinear static aeroelastic analysis of...][research_tsushima_yokozeki_2019]
- [Investigation of performance gains on a sailplane with...][research_lendraitis_2019]
- [Simplified 2D Skin Lattice Models for Multi-Axial Camber...][research_alsaidi_joe_2019]
- [Synergistically configured shape memory alloy for variable...][research_nalini_dhanalakshmi_2019]
- [Control Authority of a Camber Morphing Flying Wing][research_keidel_fasel_2020]
- [Impact of N-Shaped Wing Morphing on Solar-Powered Aircraft][research_elsalamony_aziz_2020]
- [Improving Autonomous Performance of a Passive Morphing Fixed...][research_coban_2020]
- [Multidisciplinary multi-objective design optimization of an...][research_dexl_hauffe_2020]
- [Research and improvement on design method of morphing wing...][research_gu_hong_2020]
- [Simulation of Shape Memory Alloy SMA -Bias Spring Actuation...][research_yi_2020]
- [Aerodynamic Design Optimization of a Morphing Leading Edge...][research_bashir_longtinmartel_2021]
- [Aeroelastic model and analysis of an active camber morphing...][research_zhang_shaw_2021]
- [Analysis and Design of a Leading Edge with Morphing...][research_contellasins_landersheim_2021]
- [Efficient nonlinear aeroelastic analysis of a morphing wing...][research_zhou_huang_2021]
- [Experimental Aerodynamic Comparison of Active Camber Morphing...][research_rivero_fournier_2021]
- [Flow control and separation delay in morphing wing aircraft...][research_olivett_corrao_2021]
- [Recent developments in the aeroelasticity of morphing aircraft][research_ajaj_parancheerivilakkathil_2021]
- [Seamless Active Morphing Wing Simultaneous Gust and Maneuver...][research_wang_mkhoyan_2021]
- [A flexible carbon fibre-based electrothermal film for fast...][research_yang_wang_2022]
- [Aeroelastic Response of a Z-Shaped Folding Wing During the...][research_changchuan_zhiying_2022]
- [Aeroelastic behaviour of a flexible morphing wing design for...][research_sabri_elzaabalawy_2022]
- [Aeroelasticity of Flying-Wing Aircraft Subject to Morphing A...][research_syed_moshtaghzadeh_2022]
- [Control of Hybrid Transitioning Morphing-wing VTOL UAV][research_patel_kumar_2022]
- [Effects of Shape Changing of Morphing Rotary Wing Aircraft on...][research_oktay_ozen_2022]
- [L1 Adaptive Structure-Based Nonlinear Dynamic Inversion...][research_li_liu_2022]
- [Morphing wing design using integrated and distributed...][research_mkhoyan_thakrar_2022]
- [Aerodynamic Performance of Morphing and Periodic...][research_clements_djidjeli_2023]
- [Airfoil optimization using Design-by-Morphing][research_sheikh_lee_2023]
- [Application Status and Future Prospect of Aircraft Morphing...][research_application_status_2023]
- [Autonomous material composite morphing wing][research_morton_xu_2023]
- [Binocular vision monitoring method research of wing sweep...][research_wu_xu_2023]
- [Control of Deflection Angle of Morphing Wing Using Fuzzy...][research_bataineh_shawabkeh_2023]
- [Decentralized active damping control for aeroelastic morphing...][research_svoboda_hengstermovric_2023]
- [Design development and control of a shape memory alloy linear...][research_choudhury_singh_2023]
- [Enhanced Range and Endurance Evaluation of a Camber Morphing...][research_jo_majid_2023]
- [Explorations of knitted shape memory alloy actuation behavior...][research_stroud_hartl_2023]
- [L1 Adaptive Control Based on Dynamic Inversion for Morphing...][research_cheng_li_2023]
- [Micro-actuation in bi-layered shape memory alloy structures][research_bolocan_valsan_2023]
- [Multidisciplinary Performance Enhancement on a Fixed-wing...][research_eraslan_oktay_2023]
- [Novel Approach of Airfoil Shape Representation Using Modified...][research_lendraitis_lukosevicius_2023]
- [Time-Varying Aeroelastic Modeling and Analysis of a Rapidly...][research_zhang_zhao_2023]
- [A Structural Design and Motion Characteristics Analysis of an...][research_wei_ke_2024]
- [A comprehensive review of state-of-art FishBAC fishbone...][research_ozbek_ekici_2024]
- [Aerodynamic Assessment of a Control Strategy Based on Twist...][research_karimikelayeh_djavareshkian_2024]
- [Design and rigid-flexible dynamic analysis of a morphing wing...][research_yang_xu_2024]
- [Design considerations and applications of shape memory...][research_rodino_maletta_2024]
- [Large Deflection Model and Optimal Design for a Morphing Wing...][research_yang_xiao_2024]
- [Morphing wing design of truss-braced-wing aircraft through...][research_li_zhang_2024]
- [Novel Twist Morphing Aileron and Winglet Design for UAS...][research_negahban_bashir_2024]
- [Numerical Simulation of the Transient Flow around the...][research_bashir_negahban_2024]
- [Passively morphing trailing edge design for composite tidal...][research_maguire_mamalis_2024]
- [Robust Adaptive Beamforming Based on Manifold Analysis for...][research_jia_chen_2024]
- [Rotor Power Savings and Pitch-Link Load Reductions with...][research_komp_hajek_2024]
- [Tension-twist coupling morphing wing using a novel mechanical...][research_zhu_zhang_2024]
- [The Coupled Wing Morphing of Ornithopters Improves Attitude...][research_cai_su_2024]
- [Time-Varying Aeroelastic Modeling and Analysis for a Morphing...][research_yu_zhou_2024]
- [Airfoil optimization using Design-by-Morphing with minimized...][research_lee_sheikh_2025]
- [Control Characteristics Analysis of Multi-Section Morphing...][research_ma_zhou_2025]
- [Current Status and Development Trends of Morphing Wing of...][research_yan_han_2025]
- [Design and Aerodynamic Analysis of Leading Edge for Morphing...][research_zhang_yang_2025]
- [Design and Numerical Evaluation of Trailing Edge Deflection...][research_sivanandi_sanjay_2025]
- [Effect of leading-edge and trailing-edge camber morphing on...][research_dai_hu_2025]
- [Optimization and Experimental Investigation of a...][research_lendraitis_lukosevicius_2025]
- [Rigid Elastic Coupling Dynamics of Morphing Wing Aircraft][research_hua_wang_2025]
- [A Comprehensive Numerical Study on Trailing-Edge Camber...][research_babu_khan_2026]
- [Aerodynamic superiority of trailing-edge morphing over hinged...][research_joshi_kalra_2026]
- [An Additively Manufactured Self-Recovering Morphing Airfoil...][research_battaglia_riccio_2026]
- [Dynamic Modeling and Simulation of Morphing Wing Aircraft...][research_zha_qiao_2026]
- [Effectiveness of Wing Morphing Techniques for Maneuverability...][research_bradley_haughn_2026]
- [Modeling and Integrated Control Design for Folding-Wing...][research_wang_2026]
- [Neural-network-based aerodynamic modeling and fixed-time...][research_chen_wang_2026]
- [Preliminary design of airflow-coordinated compliant morphing...][research_kambayashi_kogiso_2026]
- [Time-varying aeroelastic analysis coupled with flight...][research_liu_qian_2026]
- [Two-Stage Design of Experiment Optimization Framework for...][research_badihi_nezhad_2026]
- [Unsteady aerodynamics of the control of three dimensional...][research_roy_mukherjee_2026]

### The structure now carries a model of itself

**The X-29A had 691 measured parameters, no onboard recording, and a ground station that computed the wing's divergence estimate after the flight.**
The modern version of that arrangement keeps a structural model current against sensor data continuously,
under the names structural health monitoring, model updating and digital twin.

**The X-29's Southwell analysis is a small early instance of the same idea**, since it inferred a structural
property the aircraft could not be flown to from measurements taken well below it.

- [Fibre Optic Sensors for Structural Health Monitoring of...][research_disante_2015]
- [Integration of structural health monitoring with scheduled...][research_chen_ren_2015]
- [An in situ ensemble impact monitoring and identification...][research_si_baier_2016]
- [Modal content-based damage indicators for disbonds in...][research_ren_lissenden_2016]
- [A crack growth based individual aircraft monitoring method...][research_white_mongru_2017]
- [An adaptive guided wave-Gaussian mixture model for damage...][research_qiu_yuan_2017]
- [Development of a laser-powered wireless ultrasonic device for...][research_choi_shrestha_2017]
- [Integrated impedance and Lamb wave based structural health...][research_gao_wu_2017]
- [Structural health monitoring for impact damaged composite a...][research_demedeiros_vandepitte_2017]
- [An enhanced dynamic Gaussian mixture model based damage...][research_qiu_fang_2018]
- [Anomaly detection with the Switching Kalman Filter for...][research_nguyen_goulet_2018]
- [Gaussian mixture model based path-synthesis accumulation...][research_ren_qiu_2018]
- [Guided wave excitation and propagation in damped composite...][research_mei_giurgiutiu_2018]
- [Nonlinear Aeroelastic Control of Very Flexible Aircraft Using...][research_wang_wynn_2018]
- [A stretchable and large-scale guided wave sensor network for...][research_wang_qiu_2019]
- [Embedded fiber Bragg grating sensor based wing load...][research_kwon_park_2019]
- [Digital Twin For Fatigue Analysis][research_chabod_baron_2020]
- [In-situ monitoring of liquid composite molding process using...][research_qing_liu_2020]
- [Life prediction for aircraft structure based on Bayesian...][research_wang_liu_2020]
- [Damage detection in large composite stiffened panels based on...][research_yue_khodaei_2021]
- [Guided Wave Based Damage Detection Method for Aircraft...][research_gao_ma_2021]
- [Modeling of an aircraft structural health monitoring sensor...][research_buchter_sebastiasaez_2021]
- [Recent progress in aircraft smart skin for structural health...][research_wang_hu_2021]
- [Reliability Updating of Offshore Wind Substructures by Use of...][research_augustyn_ulriksen_2021]
- [An up-scaling temperature compensation framework for guided...][research_giannakeas_sharifkhodaei_2022]
- [Anisotropy influence on guided wave scattering for composite...][research_hervin_fromme_2022]
- [Digital Twin-Driven Reconfigurable Fixturing Optimization for...][research_hu_2022]
- [Digital twin for component health- and stress-aware...][research_sisson_karve_2022]
- [Lamb waves-based technologies for structural health...][research_philibert_yao_2022]
- [Structural health monitoring for light aircraft][research_karuskevich_maslak_2022]
- [The Need for Multi-Sensor Data Fusion in Structural Health...][research_broer_benedictus_2022]
- [A dynamic updating method of digital twin knowledge model...][research_liu_zheng_2023]
- [Digital twin-assisted gearbox dynamic model updating toward...][research_xia_huang_2023]
- [Finite Element Model Updating for Very Flexible Wings][research_sharqi_cesnik_2023]
- [Implementation of Basic MR-Based Digital Twin to Demonstrate...][research_oh_2023]
- [Processing and structural health monitoring of a composite...][research_rocha_antunes_2023]
- [Time series analysis and sparse sensor network-based impact...][research_wang_wang_2023]
- [A digital twin model of urban utility tunnels and its...][research_jiansong_chen_2024]
- [Aircraft Engine Maintenance and Digital Twin Technology in...][research_moghtadaei_2024]
- [Development of a Baseline Digital Twin Model as a...][research_roh_park_2024]
- [Digital Twin Model and Its Establishment Method for Steel...][research_liu_lin_2024]
- [Digital twin - based model updating method for mechanical...][research_shi_liu_2024]
- [Enhanced Performance of Morphing Wing Through Composite...][research_sugumaran_2024]
- [Evaluating Model Robustness for Defect Identification and...][research_yunker_lake_2024]
- [Innovative welding integration of acousto-ultrasonic...][research_galiana_moradi_2024]
- [Multi-frequency probabilistic imaging fusion for impact...][research_deng_zeng_2024]
- [Multiple-input, multiple-output modal testing of a Hawk T1A...][research_wilson_champneys_2024]
- [Optimization method of cable structure demolition driven by...][research_shi_liu_2024_b]
- [Self-updating digital twin of a hydrogen-powered furnace...][research_donato_galletti_2024]
- [An efficient and versatile Digital Twin model implementation...][research_zapata_perezgonzalez_2025]
- [Finite Element Model Updating of a Steel Cantilever Beam...][research_oyarhossein_sugiyama_2025]
- [Frequency-Based Finite Element Updating Method for...][research_jeon_choi_2025]
- [Low-Latency Edge-Enabled Digital Twin System for Multi-Robot...][research_mtowe_long_2025]
- [Mechanics-based digital twin model for structural...][research_fan_xu_2025]
- [Physics-based digital twin updating and twin-based...][research_kim_youn_2025]
- [Piezoelectric composite frequency steerable acoustic...][research_zhou_shen_2025]
- [Quality control method of steel structure construction based...][research_liu_wu_2025]
- [Review on the establishment and application of digital twin...][research_wang_rao_2025]
- [Structural damage detection on non-isotropic composite plates...][research_kong_jeon_2025]
- [TCN-TOPSIS model and its application in digital twin system...][research_li_li_2025_b]
- [Towards aircraft inerting safety digital twin modelling for...][research_wang_zheng_2025]
- [A likelihood-based time-of-flight method for localizing...][research_houzibe_chaki_2026]
- [BI-Sandwich a cross-domain model for fault diagnosis of...][research_su_kong_2026]
- [Bayesian updating with SC-MCMC for PMSM digital twin models][research_xu_yang_2026]
- [Clarifying digital Twin buzzword a novel generic evaluation...][research_liu_namakiaraghi_2026]
- [Digital twin framework with dynamic model updating for...][research_pan_jin_2026]
- [Edge-Enabled Digital Twin for Autonomous Low-Latency...][research_tomas_zaini_2026]
- [Ensemble ordinal pattern mode decomposition based on ICS2...][research_li_wang_2026_b]
- [Experimental and numerical investigation on strain-based...][research_zhou_guan_2026]
- [Flight simulation model of a multi-fidelity digital twin of...][research_pedrioli_vaiuso_2026]
- [Integrating Quantum Finite Element Method and Bayesian...][research_petriconi_lomazzi_2026]
- [Model updating approach for digital twin-driven industrial...][research_xiao_chen_2026]
- [Multiphysics-informed wavelet spatio-temporal neural networks...][research_zhou_li_2026]
- [Semantic interoperability for digital twin-driven product...][research_gebhard_wang_2026]
- [Simultaneous Digital Twin Chaining Climbing-Robot, Defect...][research_song_lu_2026]

### Manufacture changed which shapes are affordable

**Every structural choice in the X-29 was constrained by what could be laid up, machined or fastened in 1982.**
Additive manufacture and topology optimisation together relax that constraint, and the literature on
designing for them rather than merely with them is substantial.

- [Structural topology optimization considering connectivity...][research_li_chen_2016]
- [Additive Manufacturing Rectangular Lattice Structure Design...][research_chougule_sonawane_2017]
- [Design, testing, and mechanical behavior of additively...][research_lynch_mordasky_2018]
- [Dynamic mechanical analysis and thermoelasticity for...][research_cannella_garinei_2018]
- [Design of a Bi-stable Airfoil with Tailored Snap-through...][research_bhattacharyya_conlansmith_2019]
- [Design of lattice structure for additive manufacturing in CAD...][research_nguyen_2019]
- [Hybrid Metal/Composite Lattice Structures Design for Additive...][research_dicaprio_acanfora_2019]
- [On utilizing topology optimization to design support...][research_cheng_liang_2019]
- [Structural analysis of wing ribs obtained by additive...][research_carneiro_gamboa_2019]
- [Coupled Aerostructural Level Set Topology Optimization of...][research_kambampati_townsend_2020]
- [Design and additive manufacturing of closed cells from...][research_kumar_collini_2020]
- [Structure function analysis of powder beds in additive...][research_kalms_bergmann_2020]
- [Design and additive manufacturing of a fatigue-critical...][research_dagkolu_gokdag_2021]
- [Design of heterogeneous mesoscale structure for high...][research_li_wang_2021_c]
- [Effects of design sensitivity schemes for incorporating...][research_wang_2021]
- [FullControl GCode Designer Open-source software for...][research_gleadall_2021]
- [Geometrically nonlinear aeroelastic characteristics of highly...][research_tsushima_tamayama_2021]
- [Support point determination for support structure design in...][research_wang_zhang_2021]
- [Aeroelastic Topology Optimization of Wing Structure Based on...][research_wang_zhang_2022]
- [Design and mechanical performances of a novel functionally...][research_zhao_ji_2022]
- [Design optimization of thermally conductive support structure...][research_lee_yun_2022]
- [Real-time multiscale prediction of structural performance in...][research_liu_kan_2022]
- [Robust topology optimization of negative Poisson’s ratio...][research_agrawal_gupta_2022]
- [Topology optimization based channel design for powder-bed...][research_wang_xia_2022]
- [Topology optimization of an airfoil fin microchannel heat...][research_guillen_abboud_2022]
- [A design and optimisation framework for cold spray additive...][research_lomo_patel_2023]
- [Additive Manufacturing Trends in Aerospace][research_abc_2023]
- [Applying design for additive manufacturing to existing...][research_bester_2023]
- [Material extrusion additive manufacturing of multifunctional...][research_pierre_iervolino_2023]
- [A systematic review of design for additive manufacturing of...][research_khan_riccio_2024]
- [Apparent properties of porous support structure with...][research_oshima_takano_2024]
- [Isotropic cellular structure design strategies based on...][research_daynes_2024]
- [Material Characterization of High-Performance Polymers for...][research_boadocuartero_perezalvarez_2024]
- [A mapping-based graded infill structure design method and...][research_li_shi_2025_b]
- [Design and Additive Manufacturing of Metamaterial Enabling...][research_wang_song_2025]
- [Design and optimization of high stiffness tetrahedral lattice...][research_zhang_bai_2025]
- [Generative artificial intelligence in lattice structure...][research_su_mo_2025]
- [Supporting design for additive manufacturing insights from...][research_obilanade_torlind_2025]
- [Toward sustainable additive manufacturing of PEKK/Martian...][research_malekpour_abdali_2025]
- [A Concurrent Optimization of Structural Topology and 3D...][research_jia_feng_2026]
- [A novel multifunctional dimethyl adipate plasticizer for vat...][research_zhou_peng_2026]
- [A weight-reduction structural topology optimization method...][research_li_yoon_2026]
- [Hybrid additive manufacturing of high performance Ti/Al...][research_geng_zhao_2026]
- [Optimization of 3D printed grid-like ceramic composite...][research_hamza_akram_2026]
- [Performance Evaluation of Thermoplastic Composite Propellers...][research_alam_lee_2026]

### Uncertainty became something computed rather than covered

**This is the contemporary subject that bears most directly on the X-29's keystone.**

The X-29 handled uncertainty in its divergence boundary the way its era did, with a margin. The margin was a
factor of 2.667 in dynamic pressure, the flight data then indicated the real boundary was lower than
predicted, and the margin absorbed the error.
**The margin was doing the work that a probability distribution does now.**

Contemporary practice computes a probabilistic flutter or divergence margin, propagates uncertainty in
stiffness and in the aerodynamic model through to the boundary, and states a confidence rather than a
factor. **Applied to this aircraft it would have answered the question the flight test could not**, namely
how much of the discrepancy between predicted and measured divergence speed was model error and how much was
measurement error.

- [Reliability-Based Robust Design Optimization of Structures...][research_wang_li_2015]
- [Sensitivity Analysis of Continuous Time Bayesian Network...][research_sturlaugson_sheppard_2015]
- [A Mixed Interval Arithmetic/Affine Arithmetic Approach for...][research_wang_qing_2016]
- [Uncertainty Quantification of Subcritical Nonlinear...][research_thanusha_sarkar_2016]
- [Polynomial Chaos Expansions for the Stability Analysis of...][research_vermiglio_2017]
- [Safe Flight Envelope Uncertainty Quantification using...][research_vandenbrandt_devisser_2018]
- [Aerodynamic and aeroelastic uncertainty quantification of...][research_daronch_drofelnik_2019]
- [Decoupling uncertainty quantification from robust design...][research_chatterjee_chowdhury_2019]
- [Global Sensitivity Analysis for Optimization with Variable...][research_spagnol_riche_2019]
- [Robust design optimization of variable angle tow composite...][research_zhou_ruan_2019_b]
- [Robustness Metric for Robust Design Optimization Under Time...][research_wei_du_2019]
- [Fluidic Thrust Shock-Vectoring Control A Sensitivity Analysis][research_younes_hickey_2020]
- [Multi-objective robust design optimization MORDO of an...][research_elyasi_roudbari_2020]
- [Sparse polynomial surrogates for non-intrusive...][research_savin_hantraisgervois_2020]
- [A Nonparametric Bayesian Framework for Uncertainty...][research_xie_li_2021]
- [A fuzzy mixed-integer robust design optimization model to...][research_ozdemir_2021]
- [ERGO A New Robust Design Optimization Technique Combining...][research_wauters_2021]
- [Deterministic-based robust design optimization of composite...][research_hozic_thore_2023]
- [Uncertainty quantification in free vibration and aeroelastic...][research_sharma_swain_2023]
- [An imprecise multiscale uncertainty quantification framework...][research_zhao_zhou_2024]
- [Multi-objective reliability-based robust design optimization...][research_lu_zhang_2024]
- [Robust Design Optimization of Supersonic Biplane Airfoil...][research_hanazaki_yamazaki_2024]
- [Uncertainty quantification for viscoelastic composite...][research_geisler_junker_2024]
- [Nonintrusive Polynomial Chaos Approach for Nonlinear...][research_thomas_dowell_2025]
- [Reliability-based design optimization incorporating extended...][research_miska_balzani_2025]
- [Continuously nested moment quadrature for uncertainty...][research_gong_he_2026]
- [Desirability-Based Multi-Response Robust Design Optimization...][research_jeon_kim_2026]

## Where the Framing Breaks Down

**The keystone inversion rests on a single quoted figure, and the figure is a prediction rather than a measurement.**
The elastic-to-rigid ratio of 1.6 is described in the source as predicted, so the divergence dynamic
pressure derived from it is the boundary the designers believed in and not the one the aircraft had. The
flight record says the real boundary was lower.
**Every number in this article that descends from 4,533 pounds per square foot inherits that, and the Southwell sensitivity analysis is the one place where it matters most, because it uses the same figure to describe how well the figure could have been measured.**

**The elasticity derived earlier turns that rounding into a number rather than a worry.**

$$ \frac{\Delta q_D}{q_D} \approx -\frac{1}{r-1}\cdot\frac{\Delta r}{r} = -1.667 \times \left(\pm\frac{0.05}{1.6}\right) = \mp 5.2\ \mathrm{percent} $$

**The ratio is also quoted as about 1.6, and the rounding is not harmless.** At 1.55 the implied boundary is
4,791 pounds per square foot and at 1.65 it is 4,315, a spread of about ten percent from a figure given to
two significant figures. The margin of 2.667 is really a margin between about 2.54 and 2.82.

**The two-mode structural model is a scaling argument and nothing more.** It uses strip theory, neglects
compressibility, neglects the canard's downwash entirely on a wing whose inboard loading the primary record
says is dominated by exactly that, and assumes a uniform wing where the real structural box transitions from
unswept to swept. **Its absolute numbers are meaningless and are never quoted.** The results taken from it
are the sweep trend, the coupling requirement and the elimination threshold, all of which are ratios.

**The pitch inertia is assumed and the doubling times scale as its square root.** A factor of two error in
inertia is a factor of 1.41 in every time in that table.

**The trim comparison assumes a section pitching moment that was never published**, and the taper ratio
behind the transonic argument is likewise assumed. Both are stated in their tables as sensitivities for that
reason.

**The aircraft was not asked the question that would have tested the planform hardest.** The supersonic drag
was never measured during the phase reported here, because the engine was not thrust-calibrated. The
forward-swept wing's transonic case therefore rests on subsonic polar data and on tunnel work.

**And the largest limitation is not technical.** The programme was a success by its own criteria and the
configuration was never adopted.
**An article organised around whether the aeroplane worked will conclude that it did and will miss the fact that this changed nothing about how aircraft are shaped.**

## The Source Base

**This is the best-documented subject in this series in a long while, and the contrast with the two articles before it is the point.**

**The vehicle's own record is deep.** The National Aeronautics and Space Administration's Technical Reports
Server returns a large body of work under the aircraft's own designation, including the preliminary flight
assessment, the structural loads flight testing, the flight-determined lift and drag characteristics, the
flight control system lessons learned, the buffet and control system interaction, and the canard and control
system interaction. **Harvest the vehicle** is the method this subject permits, which reverses the method
the last two articles required, where the vehicle returned nothing and the physics had to be harvested
instead.

**Two primary documents carry most of the quantitative content of this article.** The preliminary flight
assessment supplies the geometry, the control system description, the static margin, the update rate and the
Southwell application. The structural loads flight testing paper supplies the structural axis sweep, the
elastic-to-rigid ratio, the design dynamic pressure and the canard torsion axis location.
**The keystone result exists because those two figures appear in the same paragraph of the same report.**

**The vehicle facts nonetheless disagree between secondary sources**, principally on the number of flights
each aircraft made and on the total for the programme. The article reports the disagreement rather than
choosing.

**The physics record is deeper still and long predates the aircraft.** Divergence, aeroelastic tailoring,
relaxed static stability and digital flight control each have substantial primary literatures, and the wind
tunnel divergence experiments on forward-swept wings that the flight programme cites are themselves a
well-documented body of work.

### What the Reference Passes Changed, and the Trap Ran Both Ways

**Two passes moved this article's reference base and they moved it in opposite directions. Both movements are recorded here because either fraction alone would misdescribe what happened.**

**The primary-reference pass took primary sources from 1,317 to 1,763, or from 61.4 to 68.0 percent of dated references**,
and the period count from 1,130 to 1,529.
**The contemporary count did not fall during that pass. It rose, from 850 to 856**, while its fraction fell
from 39.6 to 33.0 percent, purely because four hundred period sources arrived underneath it.

**The publication pass then did the reverse. The period count sits unchanged at 1,529** while its fraction
falls, because fifteen hundred contemporary sources arrived underneath that.

**Nothing was removed at any point.** The article's reference base only ever grew, and a reader watching
only the fractions would have seen two apparent regressions where there were none.

### What the Primary Pass Was Aimed At

**The primary pass was aimed at eleven subjects the equation pass had promoted and the original harvest had never asked for.**
Writing an equation down creates a citation obligation for the mechanics beneath it, and the mechanics are
not the same literature as the technology. Five of those subjects stood at zero records before this pass.

| Subject | Before | After |
|---|---|---|
| Assumed modes and the Rayleigh-Ritz method | 0 | 39 |
| The Southwell method | 0 | 19 |
| Lift-curve slope estimation | 0 | 13 |
| Time to double and unstable roots | 0 | 4 |
| Laminate stiffness and positive definiteness | 0 | 1 |
| Torsional divergence of a typical section | 3 | 14 |
| Wing root bending and structural weight | 4 | 28 |
| Static margin and the neutral point | 6 | 10 |
| Induced drag and span efficiency | 9 | 35 |
| Sampled-data control and transport delay | 16 | 23 |
| Sustained turn and manoeuvre performance | 1 | 1 |

**Two of them are reported as thin rather than padded, and in both cases the subject exists while the heading does not.**

**Sustained turn and manoeuvre performance returned one record from six targeted queries across two rounds.**
The work is not missing. It lives under **energy state, time to climb and excess thrust**, which is the
vocabulary the period actually used, and once the heading was widened to reach it the records were there. It
remains the thinnest heading in the article.

**Laminate stiffness and positive definiteness likewise returns one record**, because the mechanics of the
bend-twist coupling matrix are written up inside the composite structure literature, which this article
cites 365 times, and inside the aeroelastic tailoring literature, which it cites 108 times.
**A paper on tailoring a wing is a paper about that stiffness matrix**, and reporting a gap there would
misdescribe where the work is.

**Period coverage, with counts alongside fractions because either alone misleads.**

| | Count | Fraction of cited research |
|---|---|---|
| Period, through 1995 | 1,527 | |
| Contemporary, 2015 onward | 2,381 | |

## Epistemic State

**Historical fact, well attested.**

- The Defense Advanced Research Projects Agency began the X-29A project in 1977.
- The aircraft was designed and built by the Grumman Aerospace Corporation and flown at the Dryden
  Flight Research Facility.
- Two aircraft were built, the first flying on 14 December 1984.
- The wing has a leading edge swept 29.3 degrees forward, a structural axis swept 36.2 degrees forward,
  an aspect ratio of 4.0 and a reference area of 188.84 square feet.
- The wing skins are graphite-epoxy composite, aeroelastically tailored to inhibit structural
  divergence.
- The static margin is nominally 35 percent negative subsonically, and the instability is created by
  the canard rather than by the wing.
- The flight control system is triplex digital fly-by-wire updating at 40 hertz, with digital and
  analog reversionary modes.
- Pitch control is by three surfaces, namely the all-moving canard, the dual-hinged full-span
  flaperons, and the aft strake flaps.
- The canard area is 20 percent of the wing reference area.
- The airframe reuses the forward fuselage and nose gear of an F-5A, the main landing gear and
  servo-actuators of an F-16, and F-14 avionics.
- Envelope expansion was completed in 84 flights over two years.
- The Southwell technique was applied to flight test data for the first time on this aircraft.

**Reported in the primary literature and taken as given here.**

- That the predicted elastic-to-rigid wing lift-curve-slope ratio was about 1.6 at the design dynamic
  pressure of 1,700 pounds per square foot.
- That induced drag in flight was as much as 20 percent below wind tunnel estimates above a lift
  coefficient of 0.8.
- That the flight-estimated divergence speed was lower than predicted but remained outside the flight
  envelope.
- That canard torsion loads exceeded predictions transonically and were not fully understood.
- That the tailored skins carried an insignificant weight penalty over the basic strength design.

**Contested in the sources and left contested.**

- The number of flights made by each aircraft and by the programme as a whole.

**Engineering analysis, computed here and reproducible from the stated inputs.**

- The divergence dynamic pressure of 4,533 pounds per square foot, inverted from the elastic-to-rigid
  ratio, and the margins of 2.667 in dynamic pressure and 1.633 in equivalent airspeed.
- The agreement to 0.24 percent between the quoted design dynamic pressure and the same condition
  recomputed from the quoted Mach number and altitude.
- The agreement to 0.99 percent between the quoted span and the span implied by the quoted aspect ratio
  and area.
- The lift amplification against dynamic pressure.
- The sweep trend of the divergence boundary, and the critical sweepback of 48.013 degrees beyond
  which the boundary disappears entirely in this model, obtained in closed form and confirmed by
  bisection on an independent determinant scan.
- The bend-twist coupling of 0.627 required to reach the observed margin, and of 0.812 to remove the
  boundary, together with their insensitivity to the assumed stiffness ratio.
- The Southwell sensitivity, and that the error in the estimated boundary is about 1.4 times the twist
  measurement error at the aircraft's own reach.
- The pitch doubling times, the frames available at 40 hertz, and the 37.5 millisecond sampled delay.
- The triplex loss probabilities and the fraction of a doubling time consumed by failure isolation.
- That an aft-swept wing needs 15.40 degrees more leading edge sweep to match the isobar sweep, and
  that its structural box is about three percent longer on that basis.
- The trim drag ratio of 1.331 between an aft tail and a canard at the stated moment and arm.

**Inference, labelled as such.**

- **The canard's boundary set by pitch-loop stiffness is the aircraft's most general finding.**
  The primary record states the fact in one sentence and draws no conclusion from it.
- **The 40 hertz rate was chosen against the doubling time rather than for convenience.**
  The ratio is compelling and no source says so directly.

**Not established.**

- The wing's actual bending and torsional stiffnesses, its ply layup, or its realised coupling.
- The aircraft's pitch inertia, on which every doubling time depends.
- The measured divergence boundary, as distinct from the predicted one.
- The section pitching moment and the taper ratio, both assumed.
- Whether the configuration would have offered a net advantage in a production aircraft.

## Out of Scope

- **The [Sukhoi Su-47][ref_su47] and the [Hansa Jet][ref_hansajet]**, the other flying forward-swept
  aircraft, referenced here only as context.
- **The [Junkers Ju 287][ref_ju287]**, the first jet forward-swept aircraft, treated only as precedent.
- **The detailed high angle of attack results from the second aircraft**, which are a programme of
  their own.
- **The [HiMAT][ref_himat] programme**, from whose competition the aerofoil section came.
- **Composite laminate mechanics in detail**, surveyed here rather than derived.
- **Digital control theory**, which the references cover.

## Conclusion

**The X-29 was built to find out whether a wing that wants to tear itself off can be talked out of it, and the answer is yes, at a price that can be computed.**

The price was **most of the bend-twist coupling a laminate can physically supply**. Reaching the aircraft's
actual divergence margin required a coupling ratio of about 0.63 against a hard bound of 1.0, and that
requirement holds across the whole plausible range of the stiffnesses the record does not give.
**The technology worked and it was not working easily.**

**The margin itself was smaller than it sounds.** A factor of 2.667 in dynamic pressure is a factor of 1.633
in speed, and at the design point the wing was already amplifying its own lift by sixty percent. Between
three thousand and four thousand pounds per square foot that amplification triples.
**The aircraft lived on the flat part of a curve that has no flat part near its end.**

**The control system's problem was the same problem in a different currency.** At the corner of the envelope
the airframe doubled a pitch disturbance in about a tenth of a second, which is four frames at forty hertz,
of which the act of sampling consumed thirty-seven milliseconds. A voter needing three frames to isolate a
failed channel spent three quarters of a doubling time doing it.
**Redundancy on this aircraft was a question about time rather than about probability**, and that is the
finding most worth carrying forward.

**And the two halves were never separable, which the aircraft demonstrated in the most direct way available.**
The canard's own divergence boundary was set not by its spindle but by the stiffness of the pitch loop that
a control law required. **A control requirement fixed a structural boundary.** The programme was organised
as a structures problem and a controls problem, and the aeroplane declined to be divided that way.

**The planform lost and everything it forced won.** No production aircraft flies a forward-swept wing.
Aeroelastic tailoring, deep static instability, and real-time redundancy management are all ordinary.
**The X-29 is the rare research aircraft whose most visible feature was the least important thing it proved.**

**And it ends a run.** After an autogyro, a sailplane, a fighter that was never built and a
five-thousand-dollar flying boat, the X-29 is a purpose-built research aeroplane funded by an agency to
answer a question nobody could answer another way. **That is what the designation was for**, and this is the
first time in five articles that it meant it.

The next article treats the [X-30][ref_x30], the National Aero-Space Plane, which asked a question larger
than any aircraft in this series and never flew at all.

## References

### Books

- [Bernard Etkin 1959, Dynamics of flight][book_etkin]
- [Brian L. Stevens 2015, Aircraft Control and Simulation][book_stevens_lewis]
- [Daniel P. Raymer 1989, Aircraft Design][book_raymer]
- [Dewey H. Hodges 2011, Introduction to structural dynamics and...][book_hodges]
- [Jan R. Wright 2007, Introduction to aircraft aeroelasticity and loads][book_wright_cooper]
- [John Anderson 2016, Fundamentals of aerodynamics][book_anderson]
- [Jones, Robert M. 1975, Mechanics of composite materials][book_jones_composite]
- [Michael Chun-Yung Niu 2006, Airframe structural design][book_niu]
- [Raymond L. Bisplinghoff 1955, Aeroelasticity][book_bisplinghoff]
- [Sighard F. Hoerner 1958, Fluid-dynamic drag][book_hoerner]
- [Stephen W. Tsai 1980, Introduction to composite materials][book_tsai_hahn]
- [T. H. G. Megson 1972, Aircraft structures for engineering students][book_megson]
- [Y. C. Fung 1955, An introduction to the theory of aeroelasticity][book_fung]

[book_anderson]: https://openlibrary.org/works/OL20903326W
[book_bisplinghoff]: https://openlibrary.org/works/OL3240762W
[book_etkin]: https://openlibrary.org/works/OL2926749W
[book_fung]: https://openlibrary.org/works/OL2655267W
[book_hodges]: https://openlibrary.org/works/OL15891219W
[book_hoerner]: https://openlibrary.org/works/OL5289632W
[book_jones_composite]: https://openlibrary.org/works/OL1876296W
[book_megson]: https://openlibrary.org/works/OL4809615W
[book_niu]: https://openlibrary.org/works/OL19561185W
[book_raymer]: https://openlibrary.org/works/OL3276227W
[book_stevens_lewis]: https://openlibrary.org/works/OL21570717W
[book_tsai_hahn]: https://openlibrary.org/works/OL6341234W
[book_wright_cooper]: https://openlibrary.org/works/OL12439109W

### Reference

- [Aeroelastic divergence][ref_divergence]
- [Aeroelastic tailoring of transport aircraft wings][ref_tailoring]
- [Armstrong Flight Research Center, formerly Dryden][ref_dryden]
- [Composite laminate][ref_laminate]
- [Defense Advanced Research Projects Agency][ref_darpa]
- [Fly-by-wire][ref_fbw]
- [General Dynamics F-16 Fighting Falcon][ref_f16]
- [General Electric F404][ref_f404]
- [Grumman Aerospace Corporation][ref_grumman]
- [Grumman F-14 Tomcat][ref_f14]
- [Grumman X-29][ref_x29]
- [HFB 320 Hansa Jet][ref_hansajet]
- [Jenkins, Landis and Miller, American X-Vehicles][ref_xvehicles]
- [Junkers Ju 287][ref_ju287]
- [Northrop F-5][ref_f5]
- [Rockwell HiMAT][ref_himat]
- [Rockwell X-30 National Aero-Space Plane][ref_x30]
- [Southwell plot][ref_southwell]
- [Static margin][ref_static_margin]
- [Sukhoi Su-47][ref_su47]
- [Supercritical aerofoil][ref_supercritical]

[ref_darpa]: https://en.wikipedia.org/wiki/DARPA
[ref_divergence]: https://en.wikipedia.org/wiki/Aeroelasticity
[ref_dryden]: https://www.nasa.gov/armstrong/
[ref_f14]: https://en.wikipedia.org/wiki/Grumman_F-14_Tomcat
[ref_f16]: https://en.wikipedia.org/wiki/General_Dynamics_F-16_Fighting_Falcon
[ref_f404]: https://en.wikipedia.org/wiki/General_Electric_F404
[ref_f5]: https://en.wikipedia.org/wiki/Northrop_F-5
[ref_fbw]: https://en.wikipedia.org/wiki/Fly-by-wire
[ref_grumman]: https://en.wikipedia.org/wiki/Grumman
[ref_hansajet]: https://en.wikipedia.org/wiki/HFB_320_Hansa_Jet
[ref_himat]: https://en.wikipedia.org/wiki/Rockwell_HiMAT
[ref_ju287]: https://en.wikipedia.org/wiki/Junkers_Ju_287
[ref_laminate]: https://en.wikipedia.org/wiki/Composite_laminate
[ref_southwell]: https://en.wikipedia.org/wiki/Southwell_plot
[ref_static_margin]: https://en.wikipedia.org/wiki/Static_margin
[ref_su47]: https://en.wikipedia.org/wiki/Sukhoi_Su-47
[ref_supercritical]: https://en.wikipedia.org/wiki/Supercritical_airfoil
[ref_tailoring]: https://ntrs.nasa.gov/citations/20140006404
[ref_x29]: https://en.wikipedia.org/wiki/Grumman_X-29
[ref_x30]: https://en.wikipedia.org/wiki/Rockwell_X-30
[ref_xvehicles]: https://ntrs.nasa.gov/citations/20030067480

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
- [X-Planes: Convair X-11][related_post_a308_convair_x11]
- [X-Planes: Convair X-12][related_post_a309_convair_x12]
- [X-Planes: Convair X-6][related_post_a303_convair_x6]
- [X-Planes: Curtiss-Wright X-19][related_post_a316_curtiss_wright_x19]
- [X-Planes: Douglas X-3 Stiletto][related_post_a300_douglas_x3]
- [X-Planes: Framing and the Research Aircraft Model][related_post_a297_xplanes_framing]
- [X-Planes: Hiller X-18][related_post_a315_hiller_x18]
- [X-Planes: Lockheed X-17][related_post_a314_lockheed_x17]
- [X-Planes: Lockheed X-27][related_post_a324_lockheed_x27]
- [X-Planes: Lockheed X-7][related_post_a304_lockheed_x7]
- [X-Planes: Martin Marietta X-23 PRIME][related_post_a320_martin_marietta_x23]
- [X-Planes: Martin Marietta X-24][related_post_a321_martin_marietta_x24]
- [X-Planes: North American X-10][related_post_a307_north_american_x10]
- [X-Planes: North American X-15][related_post_a312_north_american_x15]
- [X-Planes: Northrop X-21][related_post_a318_northrop_x21]
- [X-Planes: Northrop X-4 Bantam][related_post_a301_northrop_x4]
- [X-Planes: Osprey X-28 Sea Skimmer][related_post_a325_osprey_x28]
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

### Research

- [011 Intelligent vehicle active 1994][research_011_intelligent_1994]
- [017 Preview control of 1994][research_017_preview_1994]
- [024 Automated vehicle control 1994][research_024_automated_1994]
- [025 Adaptive throttle control 1994][research_025_adaptive_1994]
- [044 Finite worldlength control 1994][research_044_finite_1994]
- [053 Fuzzy logic control 1994][research_053_fuzzy_1994]
- [056 Neural networks in 1994][research_056_neural_1994]
- [057 H∞ control design 1994][research_057_h_1994]
- [116. On selection of 1972][research_116_on_1972]
- [130 Sampled-data decentralized controller 1994][research_130_sampled_data_1994]
- [185 A fourier series 1994][research_185_a_1994]
- [196 Pointing control design 1994][research_196_pointing_1994]
- [2016][research_anon_2016_b]
- [214 Application of restructurable 1994][research_214_application_1994]
- [44408 Nondestructive analysis of 1994][research_44408_nondestructive_1994]
- [44416 ALN 4060 device 1994][research_44416_aln_1994]
- [A Comparative Study of 2022][research_a_comparative_2022]
- [A feasibility review of 2019][research_a_feasibility_2019]
- [A general boundary integral 1989][research_a_general_1989]
- [A Generalization for Model 2020][research_a_generalization_2020]
- [A hybrid adaptive control 1995][research_a_hybrid_1995]
- [A Model for Predicting 2021][research_a_model_2021]
- [A robust multi-objective optimization 2021][research_a_robust_2021]
- [A Spreadsheet Tool for 2018][research_a_spreadsheet_2018]
- [A study of the 1973][research_a_study_1973]
- [A study on the 1990][research_a_study_1990]
- [Aamir et al 2026][research_aamir_abbasi_2026]
- [Abate et al 2024][research_abate_mote_2024]
- [Abbas and Morgenthal 2016][research_abbas_morgenthal_2016]
- [Abbott Alinity Control Module 2019][research_abbott_alinity_2019]
- [Abbott, J. M. et al 1974][research_abbottjm_millerba_1974]
- [Abc 2023][research_abc_2023]
- [Abdalla et al 2020][research_abdalla_mansor_2020]
- [Abdel-Hady 1994][research_abdelhady_1994]
- [Abdul Huq and Beebi M 2015][research_abdulhuq_beebim_2015]
- [Abdul Rashid et al 2025][research_abdulrashid_syedmohddardin_2025]
- [Abdul-Kaiyoom et al 2025][research_abdulkaiyoom_yildirim_2025]
- [Abdullah et al 2019][research_abdullah_akbar_2019]
- [Abed 2000][research_abed_2000]
- [Abed et al 2024][research_abed_alhamadani_2024]
- [Abel, I. et al 1966][research_abeli_ruhlincl_1966]
- [Abele and Sanlorenzo 1975][research_abele_sanlorenzo_1975]
- [Abele et al 1973][research_abele_ruger_1973]
- [Abelkis 1967][research_abelkis_1967]
- [Aberdeen Test Center Md 2009][research_aberdeentestcentermd_2009]
- [Abichandani and Rosenberg 1952][research_abichandani_rosenberg_1952]
- [Abou-Kebeh et al 2025][research_aboukebeh_gilpita_2025]
- [Abouheaf et al 2020][research_abouheaf_gueaieb_2020]
- [AbuNawas and Qawasmeh 2026][research_abunawas_qawasmeh_2026]
- [Accelerated development and flight 1979][research_accelerated_development_1979]
- [Ackerman et al 2017][research_ackerman_xargay_2017]
- [Ackermann and Haase 2023][research_ackermann_haase_2023]
- [Ackermann and Isermann 1973][research_ackermann_isermann_1973]
- [Acoustic emission monitors damage 1981][research_acoustic_emission_1981]
- [Acoustic emissions and transient 1989][research_acoustic_emissions_1989]
- [Acquatella and Chu 2020][research_acquatella_chu_2020]
- [Acquatella B. et al 2017][research_acquatellab_vanekeren_2017]
- [Active Fault-tolerant Control of 2025][research_active_fault_tolerant_2025]
- [Adams 1973][research_adams_1973]
- [Adams 1977][research_adams_1977]
- [Adams and Hatch 1971][research_adams_hatch_1971]
- [Adan and Sheinman 1988][research_adan_sheinman_1988]
- [Adeyemi et al 2026][research_adeyemi_bull_2026]
- [Adler and Martins 2023][research_adler_martins_2023]
- [Adney, P. S. and Horn, W. J. 1984][research_adneyps_hornwj_1984]
- [Advanced Control Techniques for 2023][research_advanced_control_2023]
- [Aero structural optimization for 2018][research_aero_structural_2018]
- [Aerodynamic Performance of Swayasa 2025][research_aerodynamic_performance_2025]
- [Aggarwal and Cranch 1967][research_aggarwal_cranch_1967]
- [Aghababa 2018][research_aghababa_2018]
- [Agrawal et al 2022][research_agrawal_gupta_2022]
- [Agrell and Elmeland 1985][research_agrell_elmeland_1985]
- [Aguilar-Ibañez 2016][research_aguilaribanez_2016]
- [Agwa 2019][research_agwa_2019]
- [AHarrah, Ralph C. 2007][research_aharrahralphc_2007]
- [Ahmadi and Farsadi 2024][research_ahmadi_farsadi_2024]
- [Ahmadi Dastgerdi et al 2022][research_ahmadidastgerdi_asadi_2022]
- [Ahmadi et al 2024][research_ahmadi_farsadi_2024_b]
- [Ahmadian et al 2020][research_ahmadian_khosravi_2020]
- [Ahmadian et al 2025][research_ahmadian_alitalebi_2025]
- [Ahmed and Chen 2021][research_ahmed_chen_2021]
- [Ahmed et al 2025][research_ahmed_elbanna_2025]
- [Aidala 1985][research_aidala_1985]
- [Air Force Flight Test Center Edwards Afb Ca 1970][research_airforceflighttestcenteredwardsafbca_1970]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]
- [Air Force Flight Test Center Edwards Afb Ca 2002][research_airforceflighttestcenteredwardsafbca_2002]
- [Air Force Flight Test Center Edwards Afb Ca 2002, AFFTC Instruction 99-5, Test and][research_airforceflighttestcenteredwardsafbca_2002_b]
- [Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967]
- [Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967_b]
- [Air Force Test Pilot School Edwards Afb Ca 1969][research_airforcetestpilotschooledwardsafbca_1969]
- [Air Force Test Pilot School Edwards Afb Ca 1981][research_airforcetestpilotschooledwardsafbca_1981]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_b]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_c]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_d]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_e]
- [Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_c]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_d]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_e]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991_b]
- [Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]
- [Air Force Test Pilot School Edwards Afb Ca 1993][research_airforcetestpilotschooledwardsafbca_1993]
- [Aircraft and Rotorcraft System 2016][research_aircraft_and_2016]
- [Ajaj et al 2021][research_ajaj_parancheerivilakkathil_2021]
- [Ajel et al 2021][research_ajel_humaidi_2021]
- [Akbar and Curiel-Sosa 2016][research_akbar_curielsosa_2016]
- [Akbari et al 2025][research_akbari_galeani_2025]
- [Aker and Alukonis 1976][research_aker_alukonis_1976]
- [Akinwale and Datta 2025][research_akinwale_datta_2025]
- [Aksöz et al 2024][research_aksoz_gunay_2024]
- [Al-Hussein and Haldar 2015][research_alhussein_haldar_2015]
- [Al-Jaburi et al 2019][research_aljaburi_feszty_2019]
- [Alag and Kaufman 1975][research_alag_kaufman_1975]
- [Alam and Lee 2026][research_alam_lee_2026]
- [Alam et al 2015][research_alam_hromcik_2015]
- [Albachten 1956][research_albachten_1956]
- [Alberts 2011][research_alberts_2011]
- [Alberts 2014][research_alberts_2014]
- [Alberts and Conley 2015][research_alberts_conley_2015]
- [Alcaina et al 2019][research_alcaina_cuenca_2019]
- [Ale Isaac et al 2023][research_aleisaac_ragab_2023]
- [Alexander 1991][research_alexander_1991]
- [Alexander et al 1973][research_alexander_griffin_1973]
- [Alexander et al 1996][research_alexander_tzeng_1996]
- [Alfred et al 2017][research_alfred_celi_2017]
- [Alhajahmad and Mittelstedt 2021][research_alhajahmad_mittelstedt_2021]
- [Ali et al 2026][research_ali_chen_2026]
- [Ali, Syed Firasat 1997][research_alisyedfirasat_1997]
- [Alikhani-Koupaei 2015][research_alikhanikoupaei_2015]
- [Alim and Rizianiza 2021][research_alim_rizianiza_2021]
- [Alizadeh et al 2020][research_alizadeh_ebrahimi_2020]
- [Allen et al 1983][research_allen_bradley_1983]
- [Allen et al 1984][research_allen_bradley_1984]
- [Allison, Dennis O. and Dagenhart, J. Ray 1987][research_allisondenniso_dagenhartjray_1987]
- [Almadani et al 2022][research_almadani_osman_2022]
- [Almosnino 1985][research_almosnino_1985]
- [Alsaidi et al 2019][research_alsaidi_joe_2019]
- [Alsaidi et al 2019][research_alsaidi_joe_2019_b]
- [Alshammari 2026][research_alshammari_2026]
- [Altunkaya and Özkol 2025][research_altunkaya_ozkol_2025]
- [Alyanak and Pendleton 2017][research_alyanak_pendleton_2017]
- [Amin and Hollweger 1983][research_amin_hollweger_1983]
- [Amini and Mozaffari Tazehkand 2022][research_amini_mozaffaritazehkand_2022]
- [Amir Ahmadi Chomachar and Kuppusamy 2022][research_amirahmadichomachar_kuppusamy_2022]
- [An anal ysis of 1974][research_an_anal_1974]
- [An et al 2017][research_an_khoo_2017]
- [An et al 2020][research_an_guo_2020]
- [An et al 2026][research_an_zhang_2026]
- [and - 2025][research___2025]
- [Anderson 1960][research_anderson_1960]
- [Anderson 1961][research_anderson_1961]
- [Anderson 1968][research_anderson_1968]
- [Anderson 1970][research_anderson_1970]
- [Anderson 1985][research_anderson_1985]
- [Anderson and Toivanen 1970][research_anderson_toivanen_1970]
- [Anderson et al 1973][research_anderson_berger_1973]
- [Anderson et al 1986][research_anderson_hogle_1986]
- [Anderson, C. A. 1976][research_andersonca_1976]
- [Ando and Yashiro 1976][research_ando_yashiro_1976]
- [Andrés-Pérez et al 2016][research_andresperez_gonzalezjuarez_2016]
- [Ang and Ng 2026][research_ang_ng_2026]
- [Ang et al 2024][research_ang_leo_2024]
- [Anggraeni et al 2015][research_anggraeni_hidayat_2015]
- [Anikin et al 2015][research_anikin_animitsa_2015]
- [Annadata et al 2024][research_annadata_endesfelder_2024]
- [Announcement European forum on 1988][research_announcement_european_1988]
- [Anoshkin et al 2015][research_anoshkin_zuiko_2015]
- [Ansari and Bajodah 2017][research_ansari_bajodah_2017]
- [Ansari et al 2019][research_ansari_shaikh_2019]
- [Ansari et al 2023][research_ansari_zucco_2023]
- [Ansell, G. S. et al 1982][research_ansellgs_loewyrg_1982]
- [Antonakis 2025][research_antonakis_2025]
- [Antonakis 2025][research_antonakis_2025_b]
- [Antonakis and Biannic 2024][research_antonakis_biannic_2024]
- [Aouiti and Assali 2019][research_aouiti_assali_2019]
- [Application Analysis on Fly-by-Wire 2022][research_application_analysis_2022]
- [Application of machine learning 2024][research_application_of_2024]
- [Application Status and Future 2023][research_application_status_2023]
- [Apu/hydraulic/actuator Subsystem Computer Simulation 1975][research_apu_hydraulic_actuator_subsystem_1975]
- [Arcidiacono et al 1970][research_arcidiacono_carta_1970]
- [Ardema, M. D. and Williams, L. J. 1972][research_ardemamd_williamslj_1972]
- [Argha et al 2018][research_argha_su_2018]
- [Argha et al 2019][research_argha_su_2019]
- [Ariaratnam 1961][research_ariaratnam_1961]
- [Arif and Sasongko 2021][research_arif_sasongko_2021]
- [Ariyarit and Kanazaki 2017][research_ariyarit_kanazaki_2017]
- [Armanious and Lind 2017][research_armanious_lind_2017]
- [Armstrong 1977][research_armstrong_1977]
- [Armstrong et al 2006][research_armstrong_lindberg_2006]
- [Arnault et al 2016][research_arnault_dandois_2016]
- [Arnold 1942][research_arnold_1942]
- [Ascani 1974][research_ascani_1974]
- [Asgari and Kouchakzadeh 2016][research_asgari_kouchakzadeh_2016]
- [Ashill 1970][research_ashill_1970]
- [Ashkenas 1984][research_ashkenas_1984]
- [Ashkenas, Irving L. and Klyde, David H. 1989][research_ashkenasirvingl_klydedavidh_1989]
- [Ashton 1970][research_ashton_1970]
- [Ashworth and McKissick 1979][research_ashworth_mckissick_1979]
- [Aslam and Chen 2018][research_aslam_chen_2018]
- [Aston and Williams 1994][research_aston_williams_1994]
- [Atmaca et al 2025][research_atmaca_devisser_2025]
- [Audoin and Baste 1994][research_audoin_baste_1994]
- [Augustyn et al 2021][research_augustyn_ulriksen_2021]
- [Auman et al 2008][research_auman_doyle_2008]
- [Aung et al 2017][research_aung_shi_2017]
- [Autenrieb 2025][research_autenrieb_2025]
- [Autonomous flight control of 2018][research_autonomous_flight_2018]
- [Awadalla Ali Haj Ahmed 2024][research_awadallaalihajahmed_2024]
- [Awadalla Ali Haj Ahmed 2024][research_awadallaalihajahmed_2024_b]
- [Axelson 1977][research_axelson_1977]
- [Axten et al 2024][research_axten_khamvilai_2024]
- [Ayaz et al 2024][research_ayaz_rasoolmemon_2024]
- [Ayorinde and Gibson 1993][research_ayorinde_gibson_1993]
- [Azadegan and Beheshti 2017][research_azadegan_beheshti_2017]
- [Babu et al 2026][research_babu_khan_2026]
- [Babuska et al 2018][research_babuska_wiebe_2018]
- [Bach et al 2016][research_bach_jebari_2016]
- [Bachman 1981][research_bachman_1981]
- [Badaliance and Dill 1981][research_badaliance_dill_1981]
- [Badalló et al 2015][research_badallo_trias_2015]
- [Badhurshah et al 2024][research_badhurshah_alvarez_2024]
- [Badihi et al 2026][research_badihi_nezhad_2026]
- [Baek 2021][research_baek_2021]
- [Bagherzadeh 2026][research_bagherzadeh_2026]
- [Bagherzadeh et al 2025][research_bagherzadeh_mohammadkarimi_2025]
- [Bahamonde Jacome and Elham 2017][research_bahamondejacome_elham_2017]
- [Bahr et al 2021][research_bahr_mckay_2021]
- [Bai 2018][research_bai_2018]
- [Bai et al 2019][research_bai_tang_2019]
- [Bai et al 2022][research_bai_xu_2022]
- [Baier 1970][research_baier_1970]
- [Bailey, R. E. and Knotts, L. H. 1990][research_baileyre_knottslh_1990]
- [Bailey, R. E. and Smith, R. E. 1981][research_baileyre_smithre_1981]
- [Bailey, Randall E. et al 1988][research_baileyrandalle_powersbruceg_1988]
- [Bainum et al 1992][research_bainum_ericsson_1992]
- [Baker and Galigher 1960][research_baker_galigher_1960]
- [Baker et al 1985][research_baker_jones_1985]
- [Balaji et al 2024][research_balaji_manickam_2024]
- [Balakrishnan 2000][research_balakrishnan_2000]
- [Balasubramanian et al 2025][research_balasubramanian_jayanarasimhan_2025]
- [Balatti et al 2021][research_balatti_haddadkhodaparast_2021]
- [Balatti et al 2022][research_balatti_khodaparast_2022]
- [Baldan and Guardone 2024][research_baldan_guardone_2024]
- [Baldereschi and Maschke 1975][research_baldereschi_maschke_1975]
- [Ballester Claret et al 2024][research_ballesterclaret_coelho_2024]
- [Balunov et al 2023][research_balunov_solyaev_2023]
- [Bandyopadhyay 1989][research_bandyopadhyay_1989]
- [Bandyopadhyay 1991][research_bandyopadhyay_1991]
- [Bandyopadhyay 2001][research_bandyopadhyay_2001]
- [Banerjee 2019][research_banerjee_2019]
- [Banerjee et al 2016][research_banerjee_kotecha_2016]
- [Banks 1988][research_banks_1988]
- [Banks, Daniel W. 1988][research_banksdanielw_1988]
- [Bantscheff and Breitsamter 2023][research_bantscheff_breitsamter_2023]
- [Bao et al 2025][research_bao_li_2025]
- [Bar-Gill and Stengel 1986][research_bargill_stengel_1986]
- [Bar-Shalom 1985][research_barshalom_1985]
- [Bar-Shalom 1989][research_barshalom_1989]
- [Bar-Shalom 1990][research_barshalom_1990]
- [Barabanov and Ortega 2017][research_barabanov_ortega_2017]
- [Baranovski and Mikhailovskiy 2020][research_baranovski_mikhailovskiy_2020]
- [Barbini et al 1970][research_barbini_balfe_1970]
- [Barbosa et al 2022][research_barbosa_bertolin_2022]
- [Bardo 2015][research_bardo_2015]
- [Barrett et al 1983][research_barrett_rembold_1983]
- [Bartels and Stanford 2018][research_bartels_stanford_2018]
- [Bartels, Robert E. et al 2019][research_bartelsroberte_stanfordbretk_2019]
- [Bartoszewicz and Adamiak 2018][research_bartoszewicz_adamiak_2018]
- [Bashir et al 2021][research_bashir_longtinmartel_2021]
- [Bashir et al 2024][research_bashir_negahban_2024]
- [Bassett and Johnson 1966][research_bassett_johnson_1966]
- [Bastin et al 2025][research_bastin_coron_2025]
- [Basu Roy and Bhasin 2019][research_basuroy_bhasin_2019]
- [Bataineh and Shawabkeh 2023][research_bataineh_shawabkeh_2023]
- [Batina and Yang 1985][research_batina_yang_1985]
- [Batt 1974][research_batt_1974]
- [Battaglia and Riccio 2026][research_battaglia_riccio_2026]
- [Batterson, James G. and Omara, Thomas M. 1989][research_battersonjamesg_omarathomasm_1989]
- [Bauchau 1981][research_bauchau_1981]
- [Bauchau 1983][research_bauchau_1983]
- [Baum et al 1979][research_baum_clark_1979]
- [Bay and Kara 2026][research_bay_kara_2026]
- [Bayless and Voglewede 2020][research_bayless_voglewede_2020]
- [Baz and Chen 1993][research_baz_chen_1993]
- [Bazhenov and Lysenkova 2015][research_bazhenov_lysenkova_2015]
- [Bearings only passive location 2022][research_bearings_only_2022]
- [Beatty et al 1977][research_beatty_brooks_1977]
- [Becker 1992][research_becker_1992]
- [Beharie et al 2015][research_beharie_pedro_2015]
- [Beitalmal 2025][research_beitalmal_2025]
- [Bellini and Sorrentino 2018][research_bellini_sorrentino_2018]
- [Belmont 1983][research_belmont_1983]
- [Ben-Gida and Gurka 2022][research_bengida_gurka_2022]
- [Benaddy et al 2022][research_benaddy_labbadi_2022]
- [Benaouali and Boutemedjet 2024][research_benaouali_boutemedjet_2024]
- [Bendahmane et al 2019][research_bendahmane_hamzacherif_2019]
- [Bendiksen and Friedmann 1982][research_bendiksen_friedmann_1982]
- [Bending Moment in Walls 1992][research_bending_moment_1992]
- [Bending of cross-ply laminated 1991][research_bending_of_1991]
- [Bending theory of laminated 1987][research_bending_theory_1987]
- [Bennett et al 1993][research_bennett_dansberry_1993]
- [Bennett, R. M. et al 1977][research_bennettrm_farmermg_1977]
- [Bennett, Robert M. et al 1988][research_bennettrobertm_batinajohnt_1988]
- [Benoit 1969][research_benoit_1969]
- [Benoit et al 1960][research_benoit_leroy_1960]
- [Benyamen et al 2024][research_benyamen_chowdhury_2024]
- [Beppu et al 1966][research_beppu_curtiss_1966]
- [Berezhnitskii and Denisyuk 1985][research_berezhnitskii_denisyuk_1985]
- [Berg et al 2025][research_berg_ting_2025]
- [Bergen and Arnold 1940][research_bergen_arnold_1940]
- [Berger et al 2021][research_berger_tischler_2021]
- [Berger et al 2022][research_berger_blanken_2022]
- [Berger et al 2022][research_berger_blanken_2022_b]
- [Bergman 1948][research_bergman_1948]
- [Bergstedt et al 1959][research_bergstedt_turner_1959]
- [Berman and Gran 1974][research_berman_gran_1974]
- [Bernstein 2000][research_bernstein_2000]
- [Bernstein and Hollot 1989][research_bernstein_hollot_1989]
- [Berry et al 1982][research_berry_powers_1982]
- [Berry, D. T. 1981][research_berrydt_1981]
- [Bertsimas et al 2025][research_bertsimas_na_2025]
- [Besch and Liu 1973][research_besch_liu_1973]
- [Besch et al 1976][research_besch_rood_1976]
- [Bessa et al 2020][research_bessa_puig_2020]
- [Bessadet 2023][research_bessadet_2023]
- [Bessadi et al 2016][research_bessadi_saussie_2016]
- [Bester 2023][research_bester_2023]
- [Beyer et al 2024][research_beyer_steen_2024]
- [Beyer et al 2024][research_beyer_ullah_2024]
- [Beyers 1988][research_beyers_1988]
- [Bhachu et al 2015][research_bhachu_haftka_2015]
- [Bhandari et al 2026][research_bhandari_bhandari_2026]
- [Bhardwaj and Kapania 1995][research_bhardwaj_kapania_1995]
- [Bhardwaj et al 2022][research_bhardwaj_tiwari_2022]
- [Bhatia et al 2021][research_bhatia_jiang_2021]
- [Bhattacharyya et al 2019][research_bhattacharyya_conlansmith_2019]
- [Bi et al 2017][research_bi_xie_2017]
- [Bi-quan and Huan-wen 1990][research_biquan_huanwen_1990]
- [Bian et al 2018][research_bian_nener_2018]
- [Bian et al 2019][research_bian_nener_2019]
- [Bidinotto et al 2021][research_bidinotto_moura_2021]
- [Biezad, Daniel J. and Chou, Hwei-Lan 1993][research_biezaddanielj_chouhweilan_1993]
- [Biggs and Livornese 2020][research_biggs_livornese_2020]
- [Bihrle et al 1980][research_bihrle_jr_1980]
- [Billingsley 1976][research_billingsley_1976]
- [Binder et al 2021][research_binder_wildschek_2021]
- [Binion and T. W. 1971][research_binion_tw_1971]
- [Binion and T. W. 1975][research_binion_tw_1975]
- [Binz and Moormann 2020][research_binz_moormann_2020]
- [Binz et al 2019][research_binz_islam_2019]
- [Biricik et al 2019][research_biricik_komurcugil_2019]
- [Bischoff 1983][research_bischoff_1983]
- [Biskner and Higgins 2005][research_biskner_higgins_2005]
- [Bismarck-Nasr 1994][research_bismarcknasr_1994]
- [Biswas 1993][research_biswas_1993]
- [Biswas and Sharma 2020][research_biswas_sharma_2020]
- [Black and Moorhouse 1979][research_black_moorhouse_1979]
- [Blackburn and Whitfield 1965][research_blackburn_whitfield_1965]
- [Blackwell and Pounds 1977][research_blackwell_pounds_1977]
- [Blair and Weisshaar 1982][research_blair_weisshaar_1982]
- [Blake 2002][research_blake_2002]
- [Bland 1980][research_bland_1980]
- [Blight et al 1986][research_blight_gangsaas_1986]
- [Bliss 1980][research_bliss_1980]
- [Boado-Cuartero et al 2024][research_boadocuartero_perezalvarez_2024]
- [Boatwright 1961][research_boatwright_1961]
- [Boby et al 2019][research_boby_abdullah_2019]
- [Bodson 2000][research_bodson_2000]
- [Bodson 2000][research_bodson_2000_b]
- [Boeing Vertol Co Philadelphia Pa 1983][research_boeingvertolcophiladelphiapa_1983]
- [Bogan 1981][research_bogan_1981]
- [Bogenfeld et al 2024][research_bogenfeld_freund_2024]
- [Bohlmann et al 1990][research_bohlmann_eckstrom_1990]
- [Bohlmann, Jonathan D. 1989][research_bohlmannjonathand_1989]
- [Bohlmann, Jonathan D. and Scott, Robert C. 1991][research_bohlmannjonathand_scottrobertc_1991]
- [Bohlmann, Jonathan D. et al 1988][research_bohlmannjonathand_weisshaarterrencea_1988]
- [Boindala and Ostfeld 2022][research_boindala_ostfeld_2022]
- [Bolding, R. M. and Stearman, R. O. 1976][research_boldingrm_stearmanro_1976]
- [Bolocan et al 2023][research_bolocan_valsan_2023]
- [Bombardieri et al 2021][research_bombardieri_cavallaro_2021]
- [Bomze and Gabl 2022][research_bomze_gabl_2022]
- [Bondarenko and Shkolnyi 2024][research_bondarenko_shkolnyi_2024]
- [Bons and Martins 2020][research_bons_martins_2020]
- [Bons et al 2022][research_bons_martins_2022]
- [Bony et al 1969][research_bony_southwell_1969]
- [Book Reviews Miscellaneous Reviews 1989][research_book_reviews_1989]
- [Boothe et al 1974][research_boothe_chen_1974]
- [Bordogna et al 2020][research_bordogna_lancelot_2020]
- [Borrok and Rider 1970][research_borrok_rider_1970]
- [Bosch, J. A. and Kuehl, W. J. 1976][research_boschja_kuehlwj_1976]
- [Bottasso and Montinari 2015][research_bottasso_montinari_2015]
- [Bouadi and Mora-Camino 2018][research_bouadi_moracamino_2018]
- [Boudreau 1977][research_boudreau_1977]
- [Bouras 2020][research_bouras_2020]
- [Bouton 1950][research_bouton_1950]
- [Bowers 1981][research_bowers_1981]
- [Bowes and Miller 1976][research_bowes_miller_1976]
- [Bowman, Keith B et al 1989][research_bowmankeithb_grandhiramanav_1989]
- [Boyd 1977][research_boyd_1977]
- [Boyden, R. P. 1974][research_boydenrp_1974]
- [Boyden, R. P. 1978][research_boydenrp_1978]
- [Boylan 1965][research_boylan_1965]
- [Bradley 1986][research_bradley_1986]
- [Bradley et al 2026][research_bradley_haughn_2026]
- [Braff et al 1993][research_braff_till_1993]
- [Bras et al 2022][research_bras_warwick_2022]
- [Brennan and McDaniel 1994][research_brennan_mcdaniel_1994]
- [Breslin 1961][research_breslin_1961]
- [Briardy and Head 1968][research_briardy_head_1968]
- [Briggs et al 1982][research_briggs_reed_1982]
- [Brigham et al 1973][research_brigham_barrie_1973]
- [Bright, L. G. and Peterson, V. L. 1960][research_brightlg_petersonvl_1960]
- [Brimelo and Glass 1974][research_brimelo_glass_1974]
- [Brock, L. D. and Goodman, H. A. 1981][research_brockld_goodmanha_1981]
- [Brodecki and Subbarao 2015][research_brodecki_subbarao_2015]
- [Broer et al 2022][research_broer_benedictus_2022]
- [Broglio 1957][research_broglio_1957]
- [Bromfield et al 2023][research_bromfield_horri_2023]
- [Brooks and Martins 2018][research_brooks_martins_2018]
- [Brooks et al 2019][research_brooks_martins_2019]
- [Brooks, J. D. and Beamish, J. K. 1977][research_brooksjd_beamishjk_1977]
- [Broussard and Stengel 1977][research_broussard_stengel_1977]
- [Broussard, J. R. and Halyo, N. 1983][research_broussardjr_halyon_1983]
- [Brouwer and McNamara 2020][research_brouwer_mcnamara_2020]
- [Brown 1994][research_brown_1994]
- [Brown, S. R. and Szalai, K. J. 1977][research_brownsr_szalaikj_1977]
- [Brozoski et al 2000][research_brozoski_johnson_2000]
- [Bruno, Joseph and Libeskind, Mark 1990][research_brunojoseph_libeskindmark_1990]
- [Bryant and Albert 1988][research_bryant_albert_1988]
- [Bryson and Rumpfkeil 2019][research_bryson_rumpfkeil_2019]
- [Bryson et al 1969][research_bryson_desai_1969]
- [Brüderlin et al 2018][research_bruderlin_hosters_2018]
- [Bu et al 2025][research_bu_luo_2025]
- [Buche and Kushner 2003][research_buche_kushner_2003]
- [Bueno and Dowell 2020][research_bueno_dowell_2020]
- [Buffington 1997][research_buffington_1997]
- [Buffington 1999][research_buffington_1999]
- [Buffington 1999][research_buffington_1999_b]
- [Buffington and Adams 1995][research_buffington_adams_1995]
- [Bugała 2025][research_bugala_2025]
- [Bugała and Payenskyy 2025][research_bugala_payenskyy_2025]
- [Bullock and Fields 1998][research_bullock_fields_1998]
- [Bulut et al 2026][research_bulut_schrijer_2026]
- [Bulín et al 2021][research_bulin_dyk_2021]
- [Burcham et al 1985][research_burcham_myers_1985]
- [Burdette and Martins 2018][research_burdette_martins_2018]
- [Burke 1978][research_burke_1978]
- [Burken, John J. 2007][research_burkenjohnj_2007]
- [Burkett 1989][research_burkett_1989]
- [Burkhalter 1993][research_burkhalter_1993]
- [Burnett et al 2016][research_burnett_beranek_2016]
- [Burns 1974][research_burns_1974]
- [Burns 1975][research_burns_1975]
- [Burns 2002][research_burns_2002]
- [Burns et al 1993][research_burns_deters_1993]
- [Burt 1975][research_burt_1975]
- [Busan 1998][research_busan_1998]
- [Butler 1976][research_butler_1976]
- [Butler 1982][research_butler_1982]
- [Butler 1983][research_butler_1983]
- [Buzica et al 2018][research_buzica_biswanger_2018]
- [Bylsma and Gunter 2007][research_bylsma_gunter_2007]
- [Byreddy et al 2003][research_byreddy_grandhi_2003]
- [Büchter et al 2021][research_buchter_sebastiasaez_2021]
- [C and Y Harmin 2018][research_c_yharmin_2018]
- [Cabell, Randolph H. and Gibbs, Gary P. 2000][research_cabellrandolphh_gibbsgaryp_2000]
- [Cagdas 2017][research_cagdas_2017]
- [Cahn and Garcia 1971][research_cahn_garcia_1971]
- [Cai et al 2024][research_cai_su_2024]
- [Cai et al 2024][research_cai_yang_2024]
- [Cai et al 2026][research_cai_fan_2026]
- [Cain 1979][research_cain_1979]
- [Caixeta and Marques 2018][research_caixeta_marques_2018]
- [Calarese 1984][research_calarese_1984]
- [California Univ Los Angeles 2001][research_californiaunivlosangeles_2001]
- [Calise 1977][research_calise_1977]
- [Callaghan and Kunz 2021][research_callaghan_kunz_2021]
- [Callaway 2015][research_callaway_2015]
- [Camacho et al 2021][research_camacho_akhavan_2021]
- [Campagna et al 2025][research_campagna_benedetti_2025]
- [Campagna et al 2025][research_campagna_gulizzi_2025]
- [Campbell and LaFREY 1983][research_campbell_lafrey_1983]
- [Campbell and Terrell 1987][research_campbell_terrell_1987]
- [Campbell, Richard L. and Smith, Leigh A. 1989][research_campbellrichardl_smithleigha_1989]
- [Campos and Marques 2021][research_campos_marques_2021]
- [Candon et al 2026][research_candon_marzocca_2026]
- [Cannella et al 2018][research_cannella_garinei_2018]
- [Cano and Sobel 2016][research_cano_sobel_2016]
- [Cao and Huang 2022][research_cao_huang_2022]
- [Cao and Liu 2025][research_cao_liu_2025_b]
- [Cao and Lu 2024][research_cao_lu_2024]
- [Cao and Wei 2020][research_cao_wei_2020]
- [Cao et al 2017][research_cao_tang_2017]
- [Cao et al 2020][research_cao_jia_2020]
- [Cao et al 2022][research_cao_xu_2022]
- [Cao et al 2025][research_cao_liu_2025]
- [Cao et al 2026][research_cao_chen_2026]
- [Capone, F. J. 1981][research_caponefj_1981]
- [Carapella 2022][research_carapella_2022]
- [Carico 1998][research_carico_1998]
- [Carlson 1976][research_carlson_1976]
- [Carlson et al 2017][research_carlson_verberg_2017]
- [Carmichael and McNay 1961][research_carmichael_mcnay_1961]
- [Carneiro and Gamboa 2019][research_carneiro_gamboa_2019]
- [Carroll 1960][research_carroll_1960]
- [Caseiro and Mendes 2021][research_caseiro_mendes_2021]
- [Casey 1988][research_casey_1988]
- [Casillas et al 2024][research_casillas_chen_2024]
- [Cassanto 1971][research_cassanto_1971]
- [Cassanto 1972][research_cassanto_1972]
- [Castañeda and Gordillo 2019][research_castaneda_gordillo_2019]
- [Castellani et al 2017][research_castellani_cooper_2017]
- [Cavalcanti et al 2026][research_cavalcanti_uehara_2026]
- [Cavaliere and Fezans 2024][research_cavaliere_fezans_2024]
- [Cavaliere et al 2024][research_cavaliere_fezans_2024_b]
- [Cavallaro et al 2015][research_cavallaro_bombardieri_2015]
- [Cavallo et al 2020][research_cavallo_canciello_2020]
- [Cavin and Holyoak 1978][research_cavin_holyoak_1978]
- [Cebeci 1974][research_cebeci_1974]
- [Celi 1991][research_celi_1991]
- [Celi and Friedmann 1990][research_celi_friedmann_1990]
- [Celi et al 2004][research_celi_lovera_2004]
- [Cell 1992][research_cell_1992]
- [Cen et al 2020][research_cen_li_2020]
- [Cenkci 1991][research_cenkci_1991]
- [Center 1975][research_center_1975]
- [Cerrillo-Briones and Ricardez-Sandoval 2019][research_cerrillobriones_ricardezsandoval_2019]
- [Cesnik 2002][research_cesnik_2002]
- [Cesnik 2005][research_cesnik_2005]
- [Cestino and Iannuzzo 2026][research_cestino_iannuzzo_2026]
- [CFD Simulations and External 2021][research_cfd_simulations_2021]
- [Chabir et al 2017][research_chabir_bouteraa_2017]
- [Chabod and Baron 2020][research_chabod_baron_2020]
- [Chai et al 2017][research_chai_song_2017]
- [Chajjed et al 2024][research_chajjed_khalil_2024]
- [Chakraborty et al 2022][research_chakraborty_roy_2022]
- [Chakravarthy et al 2015][research_chakravarthy_evans_2015]
- [Chakravarty and Mahanta 2015][research_chakravarty_mahanta_2015]
- [Chalk 1964][research_chalk_1964]
- [Chalk et al 1969][research_chalk_neal_1969]
- [Chaloff et al 1974][research_chaloff_hiyama_1974]
- [Chamlin 1951][research_chamlin_1951]
- [Chamlin and Davidoff 1950][research_chamlin_davidoff_1950]
- [Chance Vought Corp Dallas Tx 1979][research_chancevoughtcorpdallastx_1979]
- [Chang 1988][research_chang_1988]
- [Chang 2019][research_chang_2019]
- [Chang et al 2022][research_chang_debreuker_2022]
- [Chang et al 2022][research_chang_guo_2022]
- [Changchuan et al 2018][research_changchuan_lan_2018]
- [Changchuan et al 2022][research_changchuan_zhiying_2022]
- [Chaparro, Daniel et al 2016][research_chaparrodaniel_fujiwaragustavoec_2016]
- [Chaplin 1953][research_chaplin_1953]
- [Chase 1977][research_chase_1977]
- [Chatterjee et al 2019][research_chatterjee_chowdhury_2019]
- [Chattopadhyay et al 1995][research_chattopadhyay_dutta_1995]
- [Chattopadhyay, Aditi and Jha, Ratneshwar 1996][research_chattopadhyayaditi_jharatneshwar_1996]
- [Chattopadhyay, Aditi and Zhang, Sen 1995][research_chattopadhyayaditi_zhangsen_1995]
- [Chau and Zingg 2022][research_chau_zingg_2022]
- [Chau and Zingg 2023][research_chau_zingg_2023]
- [Chau et al 2026][research_chau_piotrowski_2026]
- [Chauhan and Martins 2021][research_chauhan_martins_2021]
- [Chauhan and Martins 2022][research_chauhan_martins_2022]
- [Chauhan and Martins 2024][research_chauhan_martins_2024]
- [Chauhan et al 2023][research_chauhan_praveen_2023]
- [Chen 1982][research_chen_1982]
- [Chen 1983][research_chen_1983]
- [Chen and Dugundji 1987][research_chen_dugundji_1987]
- [Chen and Han 2017][research_chen_han_2017]
- [Chen and Holohan 2015][research_chen_holohan_2015]
- [Chen and Li 2017][research_chen_li_2017]
- [Chen and Li 2019][research_chen_li_2019]
- [Chen and Mangione 1967][research_chen_mangione_1967]
- [Chen and Sun 1987][research_chen_sun_1987]
- [Chen and Tang 2017][research_chen_tang_2017]
- [Chen and Zhao 2020][research_chen_zhao_2020]
- [Chen et al 2015][research_chen_ren_2015]
- [Chen et al 2015][research_chen_zhang_2015]
- [Chen et al 2016][research_chen_liu_2016]
- [Chen et al 2017][research_chen_gao_2017]
- [Chen et al 2017][research_chen_qiu_2017]
- [Chen et al 2017][research_chen_zhang_2017]
- [Chen et al 2018][research_chen_edwards_2018]
- [Chen et al 2018][research_chen_li_2018]
- [Chen et al 2018][research_chen_nie_2018]
- [Chen et al 2018][research_chen_niu_2018]
- [Chen et al 2018][research_chen_yang_2018]
- [Chen et al 2019][research_chen_wang_2019]
- [Chen et al 2020][research_chen_edwards_2020]
- [Chen et al 2020][research_chen_gao_2020]
- [Chen et al 2020][research_chen_he_2020]
- [Chen et al 2020][research_chen_jing_2020]
- [Chen et al 2022][research_chen_edwards_2022]
- [Chen et al 2022][research_chen_gao_2022]
- [Chen et al 2022][research_chen_han_2022]
- [Chen et al 2023][research_chen_dong_2023]
- [Chen et al 2023][research_chen_gao_2023]
- [Chen et al 2023][research_chen_gao_2023_b]
- [Chen et al 2023][research_chen_rao_2023]
- [Chen et al 2023][research_chen_shi_2023]
- [Chen et al 2023][research_chen_shi_2023_b]
- [Chen et al 2023][research_chen_wang_2023]
- [Chen et al 2023][research_chen_zhao_2023]
- [Chen et al 2024][research_chen_li_2024]
- [Chen et al 2025][research_chen_he_2025]
- [Chen et al 2025][research_chen_meng_2025]
- [Chen et al 2025][research_chen_qin_2025]
- [Chen et al 2025][research_chen_zhai_2025]
- [Chen et al 2026][research_chen_cai_2026]
- [Chen et al 2026][research_chen_wang_2026]
- [Cheng et al 2015][research_cheng_zhou_2015]
- [Cheng et al 2017][research_cheng_wei_2017]
- [Cheng et al 2019][research_cheng_liang_2019]
- [Cheng et al 2023][research_cheng_li_2023]
- [Cheng, H. K. et al 1980][research_chenghk_mengsy_1980]
- [Cherry et al 1993][research_cherry_costa_1993]
- [Chetty and Lakshmi 1991][research_chetty_lakshmi_1991]
- [Chi et al 2022][research_chi_gu_2022]
- [Chiarelli and Bonomo 2019][research_chiarelli_bonomo_2019]
- [Chien and Tang 1964][research_chien_tang_1964]
- [Chih and Peng 2026][research_chih_peng_2026]
- [Chin 1989][research_chin_1989]
- [Chin et al 1994][research_chin_lee_1994]
- [Chin, J. et al 1987][research_chinj_chaconv_1987]
- [Chinvorarat 2021][research_chinvorarat_2021]
- [Chipman, R. et al 1984][research_chipmanr_rauchf_1984]
- [Chipman, R. et al 1985][research_chipmanr_rauchf_1985]
- [Choi 2004][research_choi_2004]
- [Choi 2016][research_choi_2016]
- [Choi and Choi 2026][research_choi_choi_2026]
- [Choi and Park 2019][research_choi_park_2019]
- [Choi et al 2017][research_choi_shrestha_2017]
- [Choi et al 2020][research_choi_lim_2020]
- [Choi et al 2023][research_choi_kim_2023]
- [Choosak Ngaongam and Rapee Ujjin 2024][research_choosakngaongam_rapeeujjin_2024]
- [Choudhury and Singh 2023][research_choudhury_singh_2023]
- [Chougule and Sonawane 2017][research_chougule_sonawane_2017]
- [Chowdary et al 1994][research_chowdary_parthan_1994]
- [Chowhan et al 2019][research_chowhan_arya_2019]
- [Christoforou 1993][research_christoforou_1993]
- [Christopher K Droney et al 2020][research_christopherkdroney_anthonyjsclafani_2020]
- [Christopher L Blanken and Matthew S Whalley 1993][research_christopherlblanken_matthewswhalley_1993]
- [Chu et al 2021][research_chu_hou_2021]
- [Chu, Julio and Lawing, Pierce L. 1990][research_chujulio_lawingpiercel_1990]
- [Cid Montoya et al 2018][research_cidmontoya_hernandez_2018]
- [Clark 2001][research_clark_2001]
- [Clark and Dell'Amico 1962][research_clark_dellamico_1962]
- [Clark and LeTron 1989][research_clark_letron_1989]
- [Clark and Spurlin 1962][research_clark_spurlin_1962]
- [Clarke, R. et al 1982][research_clarker_shaned_1982]
- [Clarke, Robert et al 1994][research_clarkerobert_burkenjohnj_1994]
- [Clay and Rockafellow 1973][research_clay_rockafellow_1973]
- [Clements and Djidjeli 2023][research_clements_djidjeli_2023]
- [Clements, Keith 2016][research_clementskeith_2016]
- [Clews 1973][research_clews_1973]
- [Cliett 1952][research_cliett_1952]
- [Clyde et al 1984][research_clyde_bonner_1984]
- [Coban 2020][research_coban_2020]
- [Cobo-González et al 2026][research_cobogonzalez_rodriguezrobles_2026]
- [Cochran 2015][research_cochran_2015]
- [Coder 2021][research_coder_2021]
- [Coder 2026][research_coder_2026]
- [Coe and Kulla 1974][research_coe_kulla_1974]
- [Coe, Paul L., Jr. et al 1990][research_coepaulljr_perkinsjohnn_1990]
- [Cohen 1982][research_cohen_1982]
- [Cohen, Dorothea and Le, Jeanette H. 1991][research_cohendorothea_lejeanetteh_1991]
- [Cohen, G. A. 1978][research_cohenga_1978]
- [Coldsnow et al 2009][research_coldsnow_uybarreta_2009]
- [Cole 1988][research_cole_1988]
- [Cole 1988][research_cole_1988_b]
- [Cole et al 1980][research_cole_cook_1980]
- [Cole, S. R. 1986][research_colesr_1986]
- [Collings and Tee 1979][research_collings_tee_1979]
- [Combination Of Fused Machine 2024][research_combination_of_2024]
- [Combined flight control/utility system 1974][research_combined_flight_1974]
- [Comer and Chakraborty 2024][research_comer_chakraborty_2024]
- [Composite Materials in Aircraft 1989][research_composite_materials_1989]
- [Computational and Experimental Analysis 2024][research_computational_and_2024]
- [Computational Investigation of Fluidic 2025][research_computational_investigation_2025]
- [Concorde Automatic Flight Control 1971][research_concorde_automatic_1971]
- [Cong et al 2023][research_cong_hu_2023]
- [Conlan-Smith and Andreasen 2022][research_conlansmith_andreasen_2022]
- [Connelly 1982][research_connelly_1982]
- [Contell Asins et al 2021][research_contellasins_landersheim_2021]
- [Convolutional neural network-based optimization 2025][research_convolutional_neural_2025]
- [Cook 1979][research_cook_1979]
- [Cooper, P. A. and Stroud, W. J. 1972][research_cooperpa_stroudwj_1972]
- [Coppin et al 2018][research_coppin_birch_2018]
- [Cordeiro et al 2024][research_cordeiro_azinheira_2024]
- [Corliss, L. D. and Talbot, P. D. 1977][research_corlissld_talbotpd_1977]
- [Cornelius and Lucius 1994][research_cornelius_lucius_1994]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornellaeronauticallabincbuffalony_1947]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1953][research_cornellaeronauticallabincbuffalony_1953]
- [Cornette et al 2015][research_cornette_kerdreux_2015]
- [Cotton 1974][research_cotton_1974]
- [Councill and Goble 1971][research_councill_goble_1971]
- [Coyette 1987][research_coyette_1987]
- [Crabtree 1979][research_crabtree_1979]
- [Craig 1965][research_craig_1965]
- [Craig and Erbug 1976][research_craig_erbug_1976]
- [Crandall et al 1973][research_crandall_maund_1973]
- [Crane, D. F. 1983][research_cranedf_1983]
- [Crane, D. F. 1984][research_cranedf_1984]
- [Crane, Harold L. and Sommer, Robert W. 1961][research_craneharoldl_sommerrobertw_1961]
- [Craver and Egle 1972][research_craver_egle_1972]
- [Crawley and Lee 1978][research_crawley_lee_1978]
- [Creazza and Di Marco 1993][research_creazza_dimarco_1993]
- [Crews and Naik 1986][research_crews_naik_1986]
- [Crimi and Grace 1965][research_crimi_grace_1965]
- [Crimi and Ordway 1962][research_crimi_ordway_1962]
- [Crisfield 1978][research_crisfield_1978]
- [Crittenden et al 1978][research_crittenden_weishaar_1978]
- [Crolla and Abdel-Hady 1991][research_crolla_abdelhady_1991]
- [Crombie and Moorhouse 1980][research_crombie_moorhouse_1980]
- [Croom, Mark A. et al 1988][research_croommarka_whippleraymondd_1988]
- [Croop 1985][research_croop_1985]
- [Crother et al 1973][research_crother_gabelman_1973]
- [Crouse and Leishman 1992][research_crouse_leishman_1992]
- [Crowe 1937][research_crowe_1937]
- [Cruz et al 1969][research_cruz_gorenberg_1969]
- [Cui et al 2016][research_cui_yang_2016]
- [Cui et al 2021][research_cui_azuara_2021]
- [Cui et al 2022][research_cui_li_2022]
- [Cui et al 2025][research_cui_he_2025]
- [Cui et al 2026][research_cui_khodaverdian_2026]
- [Cui et al 2026][research_cui_miao_2026]
- [Cully and Boller 1973][research_cully_boller_1973]
- [Cundiff and Buckingham 1999][research_cundiff_buckingham_1999]
- [Cunis et al 2019][research_cunis_burlion_2019]
- [Cunis et al 2020][research_cunis_condomines_2020]
- [Cunis et al 2020][research_cunis_condomines_2020_b]
- [Cunningham et al 1988][research_cunningham_batina_1988]
- [Cunningham, Herbert J. et al 1987][research_cunninghamherbertj_batinajohnt_1987]
- [Currao and Jiang 2026][research_currao_jiang_2026]
- [Curry et al 1965][research_curry_matthews_1965]
- [Curtiss 1971][research_curtiss_1971]
- [Curtiss and Howard C. 1961][research_curtiss_howardc_1961]
- [Cuschieri 1990][research_cuschieri_1990]
- [Cutchins, M. A. and Purvis, J. W. 1982][research_cutchinsma_purvisjw_1982]
- [Czyba and Stajer 2019][research_czyba_stajer_2019]
- [Czysz 1963][research_czysz_1963]
- [D'Andrea 2003][research_dandrea_2003]
- [D'Andrea 2008][research_dandrea_2008]
- [D. L. Birdsall 1970][research_dlbirdsall_1970]
- [Da Ronch et al 2019][research_daronch_drofelnik_2019]
- [Dababneh et al 2018][research_dababneh_kipouros_2018]
- [Dagal 2026][research_dagal_2026]
- [Daghighi 2026][research_daghighi_2026]
- [Daghighi et al 2020][research_daghighi_rouhi_2020]
- [Dagilis and Kilikevičius 2023][research_dagilis_kilikevicius_2023]
- [Dagkolu et al 2021][research_dagkolu_gokdag_2021]
- [Dai and Yang 2015][research_dai_yang_2015]
- [Dai and Zhang 2023][research_dai_zhang_2023]
- [Dai et al 2016][research_dai_wu_2016]
- [Dai et al 2019][research_dai_he_2019]
- [Dai et al 2025][research_dai_hu_2025]
- [Daken and Mar 1985][research_daken_mar_1985]
- [Dallas and Irvin 1956][research_dallas_irvin_1956]
- [Damodaran and Caughey 1988][research_damodaran_caughey_1988]
- [Dandois 2016][research_dandois_2016]
- [Daniel 1976][research_daniel_1976]
- [Darabi and Ganesan 2016][research_darabi_ganesan_2016]
- [Darabi and Ganesan 2017][research_darabi_ganesan_2017]
- [Darabseh et al 2022][research_darabseh_tarabulsi_2022]
- [Das and Kapuria 2016][research_das_kapuria_2016]
- [Das and Longo 1995][research_das_longo_1995]
- [Das Patel and Kumar Karuparthi 2021][research_daspatel_kumarkaruparthi_2021]
- [Data-driven Model-Free Adaptive Control 2016][research_data_driven_model_free_2016]
- [Daudeville and Ladevèze 1993][research_daudeville_ladeveze_1993]
- [Davanipour et al 2017][research_davanipour_khayatian_2017]
- [David and Hale 1978][research_david_hale_1978]
- [David M Richwine and David F Fisher 1992][research_davidmrichwine_davidffisher_1992]
- [Davidson et al 1972][research_davidson_hd_1972]
- [Davis 1973][research_davis_1973]
- [Davis et al 1977][research_davis_garnett_1977]
- [Davis, D. D., Jr. et al 1993][research_davisddjr_farleygaryl_1993]
- [Dawe and Roufaeil 1980][research_dawe_roufaeil_1980]
- [Dawe et al 2025][research_dawe_bull_2025]
- [Daynes 2024][research_daynes_2024]
- [De Does 1969][research_dedoes_1969]
- [De et al 2019][research_de_jrad_2019]
- [De Felice and Sorrentino 2022][research_defelice_sorrentino_2022]
- [De Gaspari and Mantegazza 2024][research_degaspari_mantegazza_2024]
- [De Gaspari et al 2018][research_degaspari_riccobene_2018]
- [de Medeiros et al 2017][research_demedeiros_vandepitte_2017]
- [de Silva and Carmichael 1978][research_desilva_carmichael_1978]
- [de Souza and De Leon 2023][research_desouza_deleon_2023]
- [de Souza et al 2023][research_desouza_vuillemin_2023]
- [De Wagter and Meulenbeld 2019][research_dewagter_meulenbeld_2019]
- [De Witte et al 2022][research_dewitte_qing_2022]
- [Debiasi 2020][research_debiasi_2020]
- [DeBilzan 1975][research_debilzan_1975]
- [Decker 2002][research_decker_2002]
- [Deconihout et al 1992][research_deconihout_menand_1992]
- [Deepa and Gupta 2023][research_deepa_gupta_2023]
- [Deets, D. A. 1975][research_deetsda_1975]
- [Deformational behaviour of a 1990][research_deformational_behaviour_1990]
- [Dehghan Manshadi and Saghafi 2021][research_dehghanmanshadi_saghafi_2021]
- [del Carre and Palacios 2020][research_delcarre_palacios_2020]
- [Delgado et al 2026][research_delgado_datta_2026]
- [Demarchi and Haning 1978][research_demarchi_haning_1978]
- [Demir and Seyfullah Babaarslan 2021][research_demir_seyfullahbabaarslan_2021]
- [Demir et al 2023][research_demir_gorguluarslan_2023]
- [Demir et al 2025][research_demir_altunkaya_2025]
- [Deng and Qin 2021][research_deng_qin_2021]
- [Deng and Tao 2025][research_deng_tao_2025]
- [Deng and Yi 2023][research_deng_yi_2023]
- [Deng et al 2023][research_deng_zhang_2023]
- [Deng et al 2024][research_deng_stoica_2024]
- [Deng et al 2024][research_deng_zeng_2024]
- [Deng et al 2026][research_deng_xu_2026]
- [Deng et al 2026][research_deng_yi_2026]
- [DeNinno and Uherka 1966][research_deninno_uherka_1966]
- [Deobald and Gibson 1988][research_deobald_gibson_1988]
- [Department Of The Air Force Washington Dc 1986][research_departmentoftheairforcewashingtondc_1986]
- [Derkach et al 2022][research_derkach_zinkovskii_2022]
- [Desai et al 2022][research_desai_halder_2022]
- [Description and Flight Test 1975][research_description_and_1975]
- [Design and CFD Analysis 2024][research_design_and_2024]
- [Design and Implementation of 2026][research_design_and_2026]
- [Design of an Aircraft 2019][research_design_of_2019]
- [Design of discrete-time adaptive 1995][research_design_of_1995]
- [Design of L1 Adaptive 2018][research_design_of_2018]
- [Design Optimization for SG6043 2025][research_design_optimization_2025]
- [Design, Simulation, Implementation and 2015][research_design_simulation_2015]
- [Desilva, B. M. E. and Medan, R. T. 1978][research_desilvabme_medanrt_1978]
- [Deskos et al 2020][research_deskos_delcarre_2020]
- [DeSpirito 2005][research_despirito_2005]
- [Devi 2019][research_devi_2019]
- [Devine et al 2025][research_devine_choynowski_2025]
- [Dexl et al 2020][research_dexl_hauffe_2020]
- [Dexter 1993][research_dexter_1993]
- [Dghim et al 2018][research_dghim_ferchichi_2018]
- [Dghim et al 2020][research_dghim_ferchichi_2020]
- [Dhadekar et al 2021][research_dhadekar_misra_2021]
- [Dhawan et al 2026][research_dhawan_huang_2026]
- [Dhiman et al 2022][research_dhiman_abhishek_2022]
- [Dhital and Chouvion 2024][research_dhital_chouvion_2024]
- [Dhonau et al 1974][research_dhonau_blosser_1974]
- [Di Caprio et al 2019][research_dicaprio_acanfora_2019]
- [Di Donato et al 2017][research_didonato_balachandran_2017]
- [Di Francesco and Mattei 2016][research_difrancesco_mattei_2016]
- [Di Leone et al 2021][research_dileone_lobalbo_2021]
- [Di Pasquale and Prince 2023][research_dipasquale_prince_2023]
- [Di Rito and Schettini 2016][research_dirito_schettini_2016]
- [Di Sante 2015][research_disante_2015]
- [Dias 2023][research_dias_2023]
- [Dickerson 2020][research_dickerson_2020]
- [Diederich, Franklin W and Budiansky, Bernard 1948][research_diederichfranklinw_budianskybernard_1948]
- [Dienes 1978][research_dienes_1978]
- [Difranco 1970][research_difranco_1970]
- [DiFranco 1971][research_difranco_1971]
- [Diggins 1951][research_diggins_1951]
- [Digital model-reference flight control 1994][research_digital_model_reference_1994]
- [Dillinger et al 2019][research_dillinger_abdalla_2019]
- [Dillinger et al 2020][research_dillinger_meddaikar_2020]
- [Dilmi 2022][research_dilmi_2022]
- [Ding and Zhou 2018][research_ding_zhou_2018]
- [Ding et al 2022][research_ding_xu_2022]
- [Ding et al 2025][research_ding_shi_2025]
- [Dini and Saponara 2022][research_dini_saponara_2022]
- [Dinler 2025][research_dinler_2025]
- [Direction des Recherches 1992][research_directiondesrecherches_1992]
- [Divakar and B L 2026][research_divakar_bl_2026]
- [Dix and Mattasits 1980][research_dix_mattasits_1980]
- [Dlamini and Jones 2016][research_dlamini_jones_2016]
- [Dobos-Bubno and Hartsook 1977][research_dobosbubno_hartsook_1977]
- [Dodayav et al 2024][research_dodayav_biswas_2024]
- [Dodic et al 2023][research_dodic_krstic_2023]
- [Doggett, Robert V., Jr. et al 1995][research_doggettrobertvjr_riverajoseajr_1995]
- [Doi and Kataoka 1982][research_doi_kataoka_1982]
- [Doman 1995][research_doman_1995]
- [Donato et al 2024][research_donato_galletti_2024]
- [Dong 2018][research_dong_2018]
- [Dong 2025][research_dong_2025]
- [Dong and Li 2022][research_dong_li_2022]
- [Dong et al 2016][research_dong_lu_2016]
- [Dong et al 2019][research_dong_shi_2019]
- [Dong et al 2023][research_dong_li_2023]
- [Dong et al 2025][research_dong_zhou_2025]
- [Dooley 1965][research_dooley_1965]
- [Dorey et al 1980][research_dorey_good_1980]
- [Douglas Aircraft Co Long Beach Ca 1963][research_douglasaircraftcolongbeachca_1963]
- [Douglas Aircraft Co Long Beach Ca 1977][research_douglasaircraftcolongbeachca_1977]
- [Dowell and Bliss 1978][research_dowell_bliss_1978]
- [Dowell and Hall 2003][research_dowell_hall_2003]
- [Dresselhaus and Dresselhaus 1982][research_dresselhaus_dresselhaus_1982]
- [Drtil and Schulz 1978][research_drtil_schulz_1978]
- [Drummond 1971][research_drummond_1971]
- [Du et al 2023][research_du_liu_2023]
- [Du et al 2026][research_du_zhao_2026]
- [Duan and He 2024][research_duan_he_2024]
- [Duan and Okwudire 2019][research_duan_okwudire_2019]
- [Duan and Zhang 2018][research_duan_zhang_2018]
- [Duan et al 2018][research_duan_fan_2018]
- [Dubary et al 2018][research_dubary_bouvet_2018]
- [Dubigeon 1992][research_dubigeon_1992]
- [Dugundji 1965][research_dugundji_1965]
- [Dugundji et al 1962][research_dugundji_dowell_1962]
- [Dukes 1970][research_dukes_1970]
- [Dul 2018][research_dul_2018]
- [Dunmire 1982][research_dunmire_1982]
- [Dunn et al 1981][research_dunn_leong_1981]
- [Dunn, W. R. et al 1986][research_dunnwr_cottrelld_1986]
- [Dunning, Peter D. et al 2014][research_dunningpeterd_stanfordbretk_2014]
- [Durand and Teper 1964][research_durand_teper_1964]
- [Durlofsky and Mayers 1970][research_durlofsky_mayers_1970]
- [Durston, D. A. and Schreiner, J. A. 1983][research_durstonda_schreinerja_1983]
- [DuShane 1957][research_dushane_1957]
- [Dussart et al 2019][research_dussart_lone_2019]
- [Dutta and Zhao 2025][research_dutta_zhao_2025]
- [Dwivedi et al 2022][research_dwivedi_anitha_2022]
- [Dyess and William W. 1976][research_dyess_williamw_1976]
- [DYNAMIC FLIGHT AND HOTEL 2023][research_dynamic_flight_2023]
- [Dyncorp Reston Va 1999][research_dyncorprestonva_1999]
- [Dzhurynskyi 2026][research_dzhurynskyi_2026]
- [Dávila and Bisagni 2017][research_davila_bisagni_2017]
- [D’Amico et al 2025][research_damico_labella_2025]
- [d’Apolito and Sulzbachner 2021][research_dapolito_sulzbachner_2021]
- [D’hondt et al 2022][research_dhondt_degryse_2022]
- [Eades et al 1964][research_eades_jr_1964]
- [Eastep and Olsen 1980][research_eastep_olsen_1980]
- [Eastep et al 1984][research_eastep_venkayya_1984]
- [Ebner, R. E. and Mark, J. G. 1977][research_ebnerre_markjg_1977]
- [Ebrahimzade et al 2016][research_ebrahimzade_dardel_2016]
- [Ecer 1985][research_ecer_1985]
- [Eckhaus 1962][research_eckhaus_1962]
- [Eckstrom, C. V. and Spain, C. V. 1982][research_eckstromcv_spaincv_1982]
- [Edenborough 1968][research_edenborough_1968]
- [Edwards 1950][research_edwards_1950]
- [Edwards 1963][research_edwards_1963]
- [Edwards 1983][research_edwards_1983]
- [Effective Torsional Stiffness of 1976][research_effective_torsional_1976]
- [Effects of a controlled 1988][research_effects_of_1988]
- [Efremov et al 2020][research_efremov_efremov_2020]
- [Efremov et al 2022][research_efremov_shcherbakov_2022]
- [Ehlers and Weisshaar 1993][research_ehlers_weisshaar_1993]
- [Eichler 1970][research_eichler_1970]
- [Ekaterinaris, J. A. and Schiff, Lewis B. 1990][research_ekaterinarisja_schifflewisb_1990]
- [Ekaterinaris, J. A. and Schiff, Lewis B. 1994][research_ekaterinarisja_schifflewisb_1994]
- [Ekquist 1965][research_ekquist_1965]
- [El-Mahdy et al 2025][research_elmahdy_ali_2025]
- [El-Salamony and Aziz 2020][research_elsalamony_aziz_2020]
- [Elenchezhiyan and Kumar 2025][research_elenchezhiyan_kumar_2025]
- [Elham 2015][research_elham_2015]
- [Elham and van Tooren 2016][research_elham_vantooren_2016]
- [Elham and van Tooren 2016][research_elham_vantooren_2016_b]
- [Ellis et al 2021][research_ellis_borshchova_2021]
- [Elshazly et al 2025][research_elshazly_kassem_2025]
- [Elyasi et al 2020][research_elyasi_roudbari_2020]
- [Enciu 2019][research_enciu_2019]
- [Eney 1968][research_eney_1968]
- [Eng 1988][research_eng_1988]
- [Engelland, S. A. et al 1992][research_engellandsa_franklinja_1992]
- [Enns 2003][research_enns_2003]
- [Enns et al 1992][research_enns_ozbay_1992]
- [Ensemble Machine Learning Model 2021][research_ensemble_machine_2021]
- [Er-El 1988][research_erel_1988]
- [Er-El and Seginer 1985][research_erel_seginer_1985]
- [Eraslan and Oktay 2023][research_eraslan_oktay_2023]
- [Erickson, Gary E. 2003][research_ericksongarye_2003]
- [Eriksson 1990][research_eriksson_1990]
- [Esfahani et al 2018][research_esfahani_webb_2018]
- [Esmaeili and Sousa 2023][research_esmaeili_sousa_2023]
- [Eugene, L. Tu 1996][research_eugeneltu_1996]
- [Evald et al 2023][research_evald_hollweg_2023]
- [Ewing et al 1988][research_ewing_hinger_1988]
- [Experimental investigation of synthetic 2023][research_experimental_investigation_2023]
- [Fadel et al 2019][research_fadel_rabie_2019]
- [Fan et al 2018][research_fan_zhang_2018]
- [Fan et al 2021][research_fan_liu_2021]
- [Fan et al 2021][research_fan_yu_2021]
- [Fan et al 2023][research_fan_wang_2023]
- [Fan et al 2025][research_fan_wang_2025]
- [Fan et al 2025][research_fan_xu_2025]
- [Fan et al 2026][research_fan_jiang_2026]
- [Fang and Abed 1998][research_fang_abed_1998]
- [Fang et al 2020][research_fang_cao_2020]
- [Fanucci 1987][research_fanucci_1987]
- [Farbridge et al 1956][research_farbridge_woodward_1956]
- [Fardad and Bamieh 2006][research_fardad_bamieh_2006]
- [Farhat 1998][research_farhat_1998]
- [Farhat 2000][research_farhat_2000]
- [Farhat 2001][research_farhat_2001]
- [Farhat and Amsallem 2011][research_farhat_amsallem_2011]
- [Farkh et al 2021][research_farkh_ksouri_2021]
- [Farmer, M. G. and Hanson, P. W. 1976][research_farmermg_hansonpw_1976]
- [Farooq et al 2021][research_farooq_saeed_2021]
- [Farsadi et al 2020][research_farsadi_rahmanian_2020]
- [Farsadi et al 2024][research_farsadi_ahmadi_2024]
- [Farsadi et al 2026][research_farsadi_ahmadi_2026]
- [Fatigue behaviour of composite 1977][research_fatigue_behaviour_1977]
- [Fattizzo et al 2026][research_fattizzo_giulietti_2026]
- [Faure et al 2019][research_faure_dumas_2019]
- [Favaro et al 2025][research_favaro_rylko_2025]
- [Favier et al 1987][research_favier_maresca_1987]
- [Fay and Johnstone 1960][research_fay_johnstone_1960]
- [Fazeli et al 2022][research_fazeli_stokesgriffin_2022]
- [Fazelzadeh and Azadi 2017][research_fazelzadeh_azadi_2017]
- [Fazilati and Khalafi 2019][research_fazilati_khalafi_2019]
- [Fazilati and Khalafi 2019][research_fazilati_khalafi_2019_b]
- [Fearnside 1962][research_fearnside_1962]
- [Fedorenko and Bondarenko 2024][research_fedorenko_bondarenko_2024]
- [Fehrs and Kaiser 2025][research_fehrs_kaiser_2025]
- [Fei and Hua 2023][research_fei_hua_2023]
- [Feil et al 2020][research_feil_pflumm_2020]
- [Feldt and Herrmann 1974][research_feldt_herrmann_1974]
- [Feliu‐Batlle 2016][research_feliubatlle_2016]
- [Feng 2023][research_feng_2023]
- [Feng et al 2021][research_feng_wang_2021]
- [Feng et al 2023][research_feng_guo_2023]
- [Ferman and Unger 1979][research_ferman_unger_1979]
- [Feroskhan and Go 2016][research_feroskhan_go_2016]
- [Feroskhan and Go 2018][research_feroskhan_go_2018]
- [Ferraiuolo et al 2019][research_ferraiuolo_scigliano_2019]
- [Ferreres and Hardier 2017][research_ferreres_hardier_2017]
- [Feuer et al 1977][research_feuer_barmish_1977]
- [Fichera et al 2019][research_fichera_isnardi_2019]
- [Figge 1973][research_figge_1973]
- [Filamentary-plastic composite laminate 1974][research_filamentary_plastic_composite_1974]
- [Filimonov et al 2026][research_filimonov_filimonov_2026]
- [Filippou et al 2024][research_filippou_kilimtzidis_2024]
- [Fina and Bisagni 2025][research_fina_bisagni_2025]
- [Fina and Bisagni 2026][research_fina_bisagni_2026]
- [Finck 1978][research_finck_1978]
- [Finigian et al 2024][research_finigian_kavounas_2024]
- [Finkleman 1972][research_finkleman_1972]
- [Flax 1943][research_flax_1943]
- [Fleming and Kushner 1994][research_fleming_kushner_1994]
- [Flight Delay Prediction Using 2023][research_flight_delay_2023]
- [Flight Path Planning for 2026][research_flight_path_2026]
- [Flight performance handbook for 1963][research_flight_performance_1963]
- [Flight Price Prediction Using 2026][research_flight_price_2026]
- [Flight Sciences Lab Inc Buffalo Ny 1964][research_flightscienceslabincbuffalony_1964]
- [Flight Test Data Analysis 2016][research_flight_test_2016]
- [Flight Ticket Price Prediction 2020][research_flight_ticket_2020]
- [FLIGHT TICKET PRICE PREDICTION 2023][research_flight_ticket_2023]
- [Florance, James R. et al 2004][research_florancejamesr_heegjennifer_2004]
- [Flores and Mello 1969][research_flores_mello_1969]
- [Flores et al 2025][research_flores_bazan_2025]
- [Fodor and Redfield 1993][research_fodor_redfield_1993]
- [Fontana et al 2024][research_fontana_piperni_2024]
- [Fonte et al 2015][research_fonte_ricci_2015]
- [Food safety management system 2023][research_food_safety_2023]
- [Ford 1989][research_ford_1989]
- [Forsman 1983][research_forsman_1983]
- [Fortiş et al 2015][research_fortis_fortis_2015]
- [Foss, W. E., Jr. and Whitcomb, C. F. 1960][research_fosswejr_whitcombcf_1960]
- [Fournier et al 2022][research_fournier_massioni_2022]
- [Fradenburgh et al 1973][research_fradenburgh_murrill_1973]
- [Fraihat and Ajaj 2024][research_fraihat_ajaj_2024]
- [Franco et al 2022][research_franco_rios_2022]
- [Francois et al 2017][research_francois_cooper_2017]
- [Frank 1970][research_frank_1970]
- [Franklin and Innis 1978][research_franklin_innis_1978]
- [Franklin, J. A. and Innis, R. C. 1972][research_franklinja_innisrc_1972]
- [Franklin, James A. 1993][research_franklinjamesa_1993]
- [Franklin, James A. et al 1990][research_franklinjamesa_stortzmichaelw_1990]
- [Fraser et al 2002][research_fraser_petkac_2002]
- [Fresconi et al 2014][research_fresconi_celmins_2014]
- [Freudinger, Lawrence C. 1989][research_freudingerlawrencec_1989]
- [Freudinger, Lawrence C. and Kehoe, Michael W. 1990][research_freudingerlawrencec_kehoemichaelw_1990]
- [Friedmann 1998][research_friedmann_1998]
- [Friend, E. L. and Sakamoto, G. M. 1978][research_friendel_sakamotogm_1978]
- [Frost and Rutherford 1963][research_frost_rutherford_1963]
- [Fu et al 2021][research_fu_yang_2021]
- [Fujii 1985][research_fujii_1985]
- [Fujioka and Suzuki 1994][research_fujioka_suzuki_1994]
- [Fukuda and Kobayashi 1987][research_fukuda_kobayashi_1987]
- [Fukunaga 1990][research_fukunaga_1990]
- [Fukunaga and Sekine 1994][research_fukunaga_sekine_1994]
- [Fukunaga et al 1993][research_fukunaga_sekine_1993]
- [Fuller 1991][research_fuller_1991]
- [Fuller 2001][research_fuller_2001]
- [Fung 1982][research_fung_1982]
- [Fung and Doong 1988][research_fung_doong_1988]
- [Furtado et al 2019][research_furtado_catalanotti_2019]
- [Furtat and Gushchin 2021][research_furtat_gushchin_2021]
- [Fuzzy logic control for 1994][research_fuzzy_logic_1994]
- [Fuzzy logic for control 1991][research_fuzzy_logic_1991]
- [G.S.S.S.S.V. 2020][research_gssssv_2020]
- [Gabel et al 1961][research_gabel_ricks_1961]
- [Gabrys et al 2019][research_gabrys_steffensen_2019]
- [Gainer 1963][research_gainer_1963]
- [Galasso et al 2024][research_galasso_ciminello_2024]
- [Galffy et al 2019][research_galffy_bock_2019]
- [Galiana et al 2024][research_galiana_moradi_2024]
- [Galicki 2016][research_galicki_2016]
- [Gallagher 1971][research_gallagher_1971]
- [Gamagedara et al 2024][research_gamagedara_lee_2024]
- [Gamon and Mahone 1975][research_gamon_mahone_1975]
- [Ganesh and Manoharan 2016][research_ganesh_manoharan_2016]
- [Gao and Cai 2016][research_gao_cai_2016]
- [Gao and Wang 2021][research_gao_wang_2021]
- [Gao et al 2017][research_gao_wu_2017]
- [Gao et al 2019][research_gao_gao_2019]
- [Gao et al 2020][research_gao_li_2020]
- [Gao et al 2021][research_gao_ma_2021]
- [Gao et al 2024][research_gao_liu_2024]
- [Gao et al 2025][research_gao_jiang_2025]
- [Garabedian, P. R. 1979][research_garabedianpr_1979]
- [Garcia-Hernandez et al 2017][research_garciahernandez_cuernorejado_2017]
- [Garcia-Rodriguez et al 2024][research_garciarodriguez_martinezperez_2024]
- [Garg, Sanjay and Schmidt, David K. 1988][research_gargsanjay_schmidtdavidk_1988]
- [Garmendia and Mavris 2016][research_garmendia_mavris_2016]
- [Garner et al 2023][research_garner_wu_2023]
- [Garrard and Low 1990][research_garrard_low_1990]
- [Garrick, I E and Rubinow, S I 1946][research_garrickie_rubinowsi_1946]
- [Garrick, I E and Rubinow, S I 1946][research_garrickie_rubinowsi_1946_b]
- [Garrison, Charlie C. and Hacskaylo, Andrew 1947][research_garrisoncharliec_hacskayloandrew_1947]
- [Gaurav et al 2023][research_gaurav_sekou_2023]
- [Gavra and van Kampen 2024][research_gavra_vankampen_2024]
- [Ge et al 2022][research_ge_zhang_2022]
- [Gea et al 1992][research_gea_chow_1992]
- [Gearhart 1962][research_gearhart_1962]
- [Gebhard 1953][research_gebhard_1953]
- [Gebhard and Wang 2026][research_gebhard_wang_2026]
- [Geisler and Junker 2024][research_geisler_junker_2024]
- [Gelos and Laura 1990][research_gelos_laura_1990]
- [General Dynamics/Astronautics San Diego Ca 1961][research_generaldynamicsastronauticssandiegoca_1961_b]
- [General Dynamics/Astronautics San Diego Ca 1962][research_generaldynamicsastronauticssandiegoca_1962]
- [General Dynamics/Astronautics San Diegoca 1961][research_generaldynamicsastronauticssandiegoca_1961]
- [Geng et al 2026][research_geng_zhao_2026]
- [Geoghegan et al 2020][research_geoghegan_giannelis_2020]
- [Gerdes and Hynes 1972][research_gerdes_hynes_1972]
- [Gerken 1979][research_gerken_1979]
- [Ghaderi and Mojallali 2024][research_ghaderi_mojallali_2024]
- [Ghalandari et al 2022][research_ghalandari_mahariq_2022]
- [Ghasemikaram et al 2021][research_ghasemikaram_mazidi_2021]
- [Ghayour and Mani 2018][research_ghayour_mani_2018]
- [Ghazi et al 2020][research_ghazi_botez_2020]
- [Ghazi et al 2022][research_ghazi_alhazmi_2022]
- [Ghosh 2024][research_ghosh_2024]
- [Giannakeas et al 2022][research_giannakeas_sharifkhodaei_2022]
- [Gibson 1999][research_gibson_1999]
- [Giese et al 1996][research_giese_reich_1996]
- [Gilbert and Schneider 1981][research_gilbert_schneider_1981]
- [Gilbert et al 1984][research_gilbert_schmidt_1984]
- [Gilbert, Michael G. 1987][research_gilbertmichaelg_1987]
- [Giles 1972][research_giles_1972]
- [Gill 1995][research_gill_1995]
- [Giurgiutiu and Pomirleanu 2000][research_giurgiutiu_pomirleanu_2000]
- [GlBBINGS 1969][research_glbbings_1969]
- [Gleadall 2021][research_gleadall_2021]
- [Glezer and Leonard 2012][research_glezer_leonard_2012]
- [Glock et al 2015][research_glock_canal_2015]
- [Gloss and Washburn 1978][research_gloss_washburn_1978]
- [Gloss, B. B. and Washburn, K. E. 1977][research_glossbb_washburnke_1977]
- [Glynn and Iglehart 1985][research_glynn_iglehart_1985]
- [Gnilenko 2024][research_gnilenko_2024]
- [Godwin et al 1964][research_godwin_frazier_1964]
- [Goel and Roy 2021][research_goel_roy_2021]
- [Goerigk and Lendl 2021][research_goerigk_lendl_2021]
- [Goizueta et al 2022][research_goizueta_wynn_2022]
- [Goizueta et al 2022][research_goizueta_wynn_2022_b]
- [Goland 1945][research_goland_1945]
- [Golmirzaee and Wood 2026][research_golmirzaee_wood_2026]
- [Golombek et al 2026][research_golombek_bustamante_2026]
- [Gonabadi et al 2021][research_gonabadi_oila_2021]
- [Gong and Xiong 2016][research_gong_xiong_2016]
- [Gong et al 2019][research_gong_wang_2019]
- [Gong et al 2019][research_gong_wang_2019_b]
- [Gong et al 2024][research_gong_xu_2024]
- [Gong et al 2026][research_gong_he_2026]
- [Gonzales 1969][research_gonzales_1969]
- [González et al 2020][research_gonzalez_silvestre_2020]
- [González-Montijo et al 2026][research_gonzalezmontijo_vanness_2026]
- [Goodrich, Kenneth H. et al 1989][research_goodrichkennethh_sliwastevenm_1989]
- [Goodyear Aerospace Corp Akron Oh 1958][research_goodyearaerospacecorpakronoh_1958]
- [Goodyear and Lee 1981][research_goodyear_lee_1981]
- [Goradia, S. H. et al 1989][research_goradiash_bobbittpj_1989]
- [Goranson 1997][research_goranson_1997]
- [Gorman and Singhal 1993][research_gorman_singhal_1993]
- [Gospodarczyk 2015][research_gospodarczyk_2015]
- [Gottlieb 1981][research_gottlieb_1981]
- [Gottu Mukkula and Engell 2021][research_gottumukkula_engell_2021]
- [Gottzein et al 1975][research_gottzein_cramer_1975]
- [Goucem and Khiri 2023][research_goucem_khiri_2023]
- [Goulet et al 2015][research_goulet_kiureghian_2015]
- [Govindaraj et al 1979][research_govindaraj_rynaski_1979]
- [Govoni and Cristofaro 2023][research_govoni_cristofaro_2023]
- [Gowd 2016][research_gowd_2016]
- [Grace 1992][research_grace_1992]
- [Graffi and Grecchi 1973][research_graffi_grecchi_1973]
- [Grafton, S. B. et al 1982][research_graftonsb_gilberwp_1982]
- [Grant et al 2015][research_grant_stol_2015]
- [Grantham, W. D. et al 1976][research_granthamwd_nguyenlt_1976]
- [Graphite/epoxy composite violin 1981][research_graphite_epoxy_composite_1981]
- [Gratton 1967][research_gratton_1967]
- [Gratton and Donahue 1966][research_gratton_donahue_1966]
- [Grauer and Morelli 2023][research_grauer_morelli_2023]
- [Grauer, Jared A. and Boucher, Matthew J. 2017][research_grauerjareda_bouchermatthewj_2017]
- [Graves and Sawicki 1994][research_graves_sawicki_1994]
- [Gray and Mei 1993][research_gray_mei_1993]
- [Gray et al 2023][research_gray_riso_2023]
- [Gray et al 2025][research_gray_kennedy_2025]
- [Green 1987][research_green_1987]
- [Green, J. A. 1986][research_greenja_1986]
- [Greenberg, Harry and Sternfield, Leonard 1944][research_greenbergharry_sternfieldleonard_1944]
- [Greene 1928][research_greene_1928]
- [Greene 1955][research_greene_1955]
- [Greene 1956][research_greene_1956]
- [Greene 1957][research_greene_1957]
- [Greenhalgh et al 1993][research_greenhalgh_pastore_1993]
- [Greenhall et al 2022][research_greenhall_zerkle_2022]
- [Grenestedt 1989][research_grenestedt_1989]
- [Greszczuk and Chao 1975][research_greszczuk_chao_1975]
- [Griffin and Bellaire 1968][research_griffin_bellaire_1968]
- [Griffin and Eastep 1982][research_griffin_eastep_1982]
- [Griffin et al 1983][research_griffin_haerter_1983]
- [Griffin, Brian Joseph et al 2010][research_griffinbrianjoseph_burkenjohnj_2010]
- [Griffin, Charles F. and Harvill, William E. 1988][research_griffincharlesf_harvillwilliame_1988]
- [Griffis et al 1981][research_griffis_masumura_1981]
- [Grifò et al 2023][research_grifo_gulizzi_2023]
- [Grigolyuk and Kulikov 1990][research_grigolyuk_kulikov_1990]
- [Groh and Wu 2022][research_groh_wu_2022]
- [Gross et al 2017][research_gross_clark_2017]
- [Grossschmidt and Pahapill 1995][research_grossschmidt_pahapill_1995]
- [Gruenwald et al 2020][research_gruenwald_yucelen_2020]
- [Gu and Hong 2020][research_gu_hong_2020]
- [Gu and Zhou 2020][research_gu_zhou_2020]
- [Gu and Zhou 2022][research_gu_zhou_2022]
- [Gu et al 2022][research_gu_taghipour_2022]
- [Gu et al 2023][research_gu_ducvo_2023]
- [Guan and Li 2026][research_guan_li_2026]
- [Guderley 1956][research_guderley_1956]
- [Guillen et al 2022][research_guillen_abboud_2022]
- [Guimarães et al 2019][research_guimaraes_castro_2019]
- [Guimarães et al 2020][research_guimaraes_silva_2020]
- [Guinn, Wiley A. 1984][research_guinnwileya_1984]
- [Guinn, Wiley A. et al 1983][research_guinnwileya_willeycraigs_1983]
- [Guinn, Wiley A. et al 1984][research_guinnwileya_risingjerryj_1984]
- [Gunnink 1988][research_gunnink_1988]
- [Guo 2021][research_guo_2021]
- [Guo 2021][research_guo_2021_b]
- [Guo and Guan 1993][research_guo_guan_1993]
- [Guo and Jin 2023][research_guo_jin_2023]
- [Guo et al 1988][research_guo_wang_1988]
- [Guo et al 2017][research_guo_bai_2017]
- [Guo et al 2017][research_guo_hou_2017]
- [Guo et al 2017][research_guo_jing_2017]
- [Guo et al 2020][research_guo_zhou_2020]
- [Guo et al 2021][research_guo_li_2021]
- [Guo et al 2022][research_guo_zhang_2022]
- [Guo et al 2025][research_guo_wang_2025]
- [Guo et al 2026][research_guo_liu_2026]
- [Guo et al 2026][research_guo_liu_2026_b]
- [Gupta 1998][research_gupta_1998]
- [Gupta 2023][research_gupta_2023]
- [Gurdal 2002][research_gurdal_2002]
- [Gurdal et al 1999][research_gurdal_haftka_1999]
- [Gurley, J. R., Jr. and Ruhlin, C. L. 1962][research_gurleyjrjr_ruhlincl_1962]
- [Guruswamy 2019][research_guruswamy_2019]
- [Guruswamy and Tu 1989][research_guruswamy_tu_1989]
- [Guruswamy et al 1987][research_guruswamy_goorjian_1987]
- [Guy et al 1995][research_guy_rousselotpailley_1995]
- [Gwin 1976][research_gwin_1976]
- [Gwin, L. B. 1974][research_gwinlb_1974]
- [Haas and Chopra 1988][research_haas_chopra_1988]
- [Haas and Chopra 1990][research_haas_chopra_1990]
- [Had and Růžička 2016][research_had_ruzicka_2016]
- [Hadidoolabi and Ansarian 2017][research_hadidoolabi_ansarian_2017]
- [Hadidoolabi and Ansarian 2018][research_hadidoolabi_ansarian_2018]
- [Haeri and Fadaee 2016][research_haeri_fadaee_2016]
- [Haftka 1977][research_haftka_1977]
- [Haftmann et al 1988][research_haftmann_debbeler_1988]
- [Hagnell et al 2016][research_hagnell_langbeck_2016]
- [Hague 1927][research_hague_1927]
- [Hahn and Haupt 2022][research_hahn_haupt_2022]
- [Hahn and Kim 1976][research_hahn_kim_1976]
- [Hai 2022][research_hai_2022]
- [Halder et al 2020][research_halder_damodaran_2020]
- [Halder et al 2020][research_halder_das_2020]
- [Haley and Soloway 2022][research_haley_soloway_2022]
- [Hall 1971][research_hall_1971]
- [Hall et al 1974][research_hall_weingarten_1974]
- [Hallauer and Jr. 1983][research_hallauer_jr_1983]
- [Hallissy, J. B. and Ayers, T. G. 1977][research_hallissyjb_ayerstg_1977]
- [Hamada et al 2019][research_hamada_saitoh_2019]
- [Hamilton, Brian K. and Peters, James R. 1989][research_hamiltonbriank_petersjamesr_1989]
- [Hamissi et al 2019][research_hamissi_bouzid_2019]
- [Hammer and Bright 1998][research_hammer_bright_1998]
- [Hamza et al 2026][research_hamza_akram_2026]
- [Han and Glower 1985][research_han_glower_1985]
- [Han and Pei 2026][research_han_pei_2026]
- [Han et al 2019][research_han_yu_2019]
- [Han et al 2022][research_han_guo_2022]
- [Han et al 2022][research_han_zhang_2022]
- [Han et al 2023][research_han_cheng_2023]
- [Han et al 2024][research_han_yang_2024]
- [Hanagud et al 1989][research_hanagud_craig_1989]
- [Hanazaki and Yamazaki 2024][research_hanazaki_yamazaki_2024]
- [Hancock 1971][research_hancock_1971]
- [Hancock 1972][research_hancock_1972]
- [Hancock 1992][research_hancock_1992]
- [Hancock, Regis and Fullerton, Gordon 1992][research_hancockregis_fullertongordon_1992]
- [Hanman et al 2025][research_hanman_yao_2025]
- [Hansen et al 2022][research_hansen_duan_2022]
- [Hanson and Stengel 1984][research_hanson_stengel_1984]
- [Hanson, Curt et al 2011][research_hansoncurt_schaeferjacob_2011]
- [Hanson, G. D. and Stengel, R. F. 1981][research_hansongd_stengelrf_1981]
- [Hanson, G. D. and Stengel, R. F. 1983][research_hansongd_stengelrf_1983]
- [Hao et al 2022][research_hao_du_2022]
- [Hao et al 2023][research_hao_ma_2023]
- [Hao et al 2026][research_hao_yu_2026]
- [Harno and Kim 2020][research_harno_kim_2020]
- [Harper and Robert P. 1955][research_harper_robertp_1955]
- [Harpur 1968][research_harpur_1968]
- [Harris, C. D. 1974][research_harriscd_1974]
- [Harris, C. D. 1974][research_harriscd_1974_b]
- [Harry and Trobaugh 1966][research_harry_trobaugh_1966]
- [Hart 1956][research_hart_1956]
- [Hartini et al 2026][research_hartini_bachtiar_2026]
- [Harvill, W. E. and Kizer, J. A. 1976][research_harvillwe_kizerja_1976]
- [Hashii, Wendy N. and Thompson, Randolph C. 2018][research_hashiiwendyn_thompsonrandolphc_2018]
- [Hassan et al 2024][research_hassan_selvaratnam_2024]
- [Hatake 1985][research_hatake_1985]
- [Hatake 1986][research_hatake_1986]
- [Haviv 1989][research_haviv_1989]
- [Hayase 1974][research_hayase_1974]
- [Hayase 1974][research_hayase_1974_b]
- [Hayashi 1949][research_hayashi_1949]
- [Hayashi 1988][research_hayashi_1988]
- [Hać 1987][research_hac_1987]
- [Hać 1992][research_hac_1992]
- [He et al 2020][research_he_tan_2020]
- [He et al 2023][research_he_wang_2023]
- [Hebbar and Pashilkar 2016][research_hebbar_pashilkar_2016]
- [Heckl et al 1962][research_heckl_lyon_1962]
- [Heeg, Jennifer 2006][research_heegjennifer_2006]
- [Heeg, Jennifer et al 2004][research_heegjennifer_spaincharlesv_2004]
- [Heeg, Jennifer et al 2005][research_heegjennifer_spaincharlesv_2005]
- [Heersink et al 2022][research_heersink_sylla_2022]
- [Heinrich et al 2022][research_heinrich_vogt_2022]
- [Helgo 2023][research_helgo_2023]
- [Heltsley and Cline 1979][research_heltsley_cline_1979]
- [Heltsley et al 1981][research_heltsley_crosswy_1981]
- [Hemsch 1989][research_hemsch_1989]
- [Hemsch and Nielsen 1983][research_hemsch_nielsen_1983]
- [Henriquez Huecas et al 2022][research_henriquezhuecas_white_2022]
- [Henry 1961][research_henry_1961]
- [Henschel and Chetty 1989][research_henschel_chetty_1989]
- [Hepler, A. K. et al 1978][research_heplerak_zeckh_1978]
- [Herman A Rediess 1976][research_hermanarediess_1976]
- [Hermanutz and Hornung 2020][research_hermanutz_hornung_2020]
- [Herrington et al 2023][research_herrington_zahed_2023]
- [Herrmann and Ben-Asher 2016][research_herrmann_benasher_2016]
- [Herrmann, G. et al 1966][research_herrmanng_nematnassers_1966]
- [Hertz, T. J. et al 1982][research_hertztj_shirkmh_1982]
- [Hervin and Fromme 2022][research_hervin_fromme_2022]
- [Hess 1984][research_hess_1984]
- [Hess 1989][research_hess_1989]
- [Hess 1991][research_hess_1991]
- [Hess 2016][research_hess_2016]
- [Hess 2018][research_hess_2018]
- [Hess and Peng 2018][research_hess_peng_2018]
- [Hess and Sunyoto 1985][research_hess_sunyoto_1985]
- [Hess et al 1989][research_hess_seidel_1989]
- [Hicks, John W. and Huckabine, Thomas 1989][research_hicksjohnw_huckabinethomas_1989]
- [Hicks, John W. and Matheny, Neil W. 1987][research_hicksjohnw_mathenyneilw_1987]
- [Hicks, John W. and Matheny, Neil W. 1989][research_hicksjohnw_mathenyneilw_1989]
- [Hicks, John W. and Moulton, Bryan J. 1988][research_hicksjohnw_moultonbryanj_1988]
- [Hicks, John W. and Petersen, Kevin L. 1988][research_hicksjohnw_petersenkevinl_1988]
- [Hicks, John W. and Petersen, Kevin L. 1989][research_hicksjohnw_petersenkevinl_1989]
- [Hicks, John W. et al 1987][research_hicksjohnw_cooperjamesmjr_1987]
- [Hicks, John W. et al 1987][research_hicksjohnw_kaniajan_1987]
- [Higgins and Shomber 1965][research_higgins_shomber_1965]
- [Higuchi and Saitoh 1993][research_higuchi_saitoh_1993]
- [Hildebrand, Francis B and Reissner, Eric 1944][research_hildebrandfrancisb_reissnereric_1944]
- [Hilger and Ritter 2021][research_hilger_ritter_2021]
- [Hill 1987][research_hill_1987]
- [Hill 2001][research_hill_2001]
- [Himeda and Naka 2019][research_himeda_naka_2019]
- [Hinchliffe and Qin 2017][research_hinchliffe_qin_2017]
- [Hirai and Kline 1973][research_hirai_kline_1973]
- [Hirai and Satoh 1980][research_hirai_satoh_1980]
- [Hirato et al 2019][research_hirato_shen_2019]
- [Hirsch and McCORMICK 1966][research_hirsch_mccormick_1966]
- [Hisada et al 2020][research_hisada_minakuchi_2020]
- [Hitch 1978][research_hitch_1978]
- [Hitzel 2017][research_hitzel_2017]
- [Hitzel and Osterhuber 2018][research_hitzel_osterhuber_2018]
- [Hiyama 1974][research_hiyama_1974]
- [Hiyama 1974][research_hiyama_1974_b]
- [Hobbs et al 2023][research_hobbs_mote_2023]
- [Hodges 2004][research_hodges_2004]
- [Hodgins and Freeman 2025][research_hodgins_freeman_2025]
- [Hodgkinson 2017][research_hodgkinson_2017]
- [Hodgkinson et al 1976][research_hodgkinson_lamanna_1976]
- [Hofmann and Kezer 1962][research_hofmann_kezer_1962]
- [Hogan and Rinde 1978][research_hogan_rinde_1978]
- [Hoh and Mitchell 1983][research_hoh_mitchell_1983]
- [Holst 1988][research_holst_1988]
- [Holst and Brown 1983][research_holst_brown_1983]
- [Honeycomb-laminate composite structure 1979][research_honeycomb_laminate_composite_1979]
- [Hong and Cheong 1993][research_hong_cheong_1993]
- [Hong and Ko 2015][research_hong_ko_2015]
- [Hong et al 2024][research_hong_kim_2024]
- [Hongyan and Xiaoyong 2026][research_hongyan_xiaoyong_2026]
- [Hoogervorst and Elham 2017][research_hoogervorst_elham_2017]
- [Hoover and Shen 2019][research_hoover_shen_2019]
- [Hope and Kunz 2019][research_hope_kunz_2019]
- [Hopkins, E. J. and Yee, S. C. 1977][research_hopkinsej_yeesc_1977]
- [Hopwood et al 2023][research_hopwood_gresham_2023]
- [Horowitz et al 1980][research_horowitz_golubev_1980]
- [Horsburgh 1911][research_horsburgh_1911]
- [Horton and Mayers 1965][research_horton_mayers_1965]
- [Hortsen et al 1983][research_hortsen_boer_1983]
- [Hoseini and Hodges 2019][research_hoseini_hodges_2019]
- [Housner, J. M. and Stein, M. 1974][research_housnerjm_steinm_1974]
- [Houtman et al 2023][research_houtman_timme_2023]
- [Houzibe and Chaki 2026][research_houzibe_chaki_2026]
- [How 2004][research_how_2004]
- [Howard and O'Leary 1994][research_howard_oleary_1994]
- [Howdyshell et al 1998][research_howdyshell_trovillion_1998]
- [Hoyos et al 2025][research_hoyos_candelobecerra_2025]
- [Hozić et al 2023][research_hozic_thore_2023]
- [Hu 1984][research_hu_1984]
- [Hu 2022][research_hu_2022]
- [Hu et al 2016][research_hu_yang_2016]
- [Hu et al 2025][research_hu_an_2025]
- [Hu et al 2026][research_hu_qiu_2026]
- [Hua et al 2025][research_hua_wang_2025]
- [Huang et al 2016][research_huang_wang_2016]
- [Huang et al 2017][research_huang_pool_2017]
- [Huang et al 2018][research_huang_yang_2018]
- [Huang et al 2019][research_huang_yang_2019]
- [Huang et al 2022][research_huang_yu_2022]
- [Huang et al 2023][research_huang_zhen_2023]
- [Huang et al 2024][research_huang_wang_2024]
- [Huang et al 2025][research_huang_gu_2025]
- [Huang et al 2026][research_huang_li_2026]
- [Huff and W. W. 1949][research_huff_ww_1949]
- [Huffman, J. K. 1975][research_huffmanjk_1975]
- [Hui 1986][research_hui_1986]
- [Huiping et al 1989][research_huiping_yutian_1989]
- [Human Supervisory Control of 2015][research_human_supervisory_2015]
- [Hummel and Oelker 1994][research_hummel_oelker_1994]
- [Humphreys-Jennings et al 2020][research_humphreysjennings_lappas_2020]
- [Hunn 1953][research_hunn_1953]
- [Hunter 2003][research_hunter_2003]
- [Huo et al 2021][research_huo_duan_2021]
- [Hurley 1975][research_hurley_1975]
- [Hussain et al 2015][research_hussain_anjum_2015]
- [Hutchinson 2014][research_hutchinson_2014]
- [Hybrid composite laminate structures 1978][research_hybrid_composite_1978]
- [Hübener and Luckner 2026][research_hubener_luckner_2026]
- [Hübler et al 2016][research_hubler_nissle_2016]
- [Iannelli et al 2017][research_iannelli_marcos_2017]
- [Iannelli et al 2018][research_iannelli_marcos_2018]
- [Ibrahim 2026][research_ibrahim_2026]
- [Ibren et al 2020][research_ibren_sulaeman_2020]
- [Ide and Landman 2025][research_ide_landman_2025]
- [Ignatyev and Khrabrov 2018][research_ignatyev_khrabrov_2018]
- [Ijaz et al 2019][research_ijaz_hamayun_2019]
- [Ijaz et al 2019][research_ijaz_hamayun_2019_b]
- [Ikehata 1995][research_ikehata_1995]
- [Ilcewicz, L. B. et al 1991][research_ilcewiczlb_walkerth_1991]
- [Iliff, K. W. et al 1978][research_iliffkw_mainere_1978]
- [Iliff, K. W. et al 1981][research_iliffkw_mainere_1981]
- [Im et al 2025][research_im_kong_2025]
- [Imani and Montazeri-Gh 2019][research_imani_montazerigh_2019]
- [Immersion and Invariance Adaptive 2026][research_immersion_and_2026]
- [Implementation of control technology 2023][research_implementation_of_2023]
- [Inger 1983][research_inger_1983]
- [Ingram, W. C. et al 1986][research_ingramwc_yiplp_1986]
- [Interlaminar shear fracture of 1992][research_interlaminar_shear_1992]
- [Introduction to the Special 2017][research_introduction_to_2017]
- [Invernizzi and Lovera 2018][research_invernizzi_lovera_2018]
- [Ioannis and Ioannis 2026][research_ioannis_ioannis_2026]
- [Iovnovich et al 2018][research_iovnovich_nahom_2018]
- [Irvine 1968][research_irvine_1968]
- [Iryani et al 2019][research_iryani_kadir_2019]
- [Ishii 2023][research_ishii_2023]
- [Ishmael, S. D. and Wierzbanowski, T. 1985][research_ishmaelsd_wierzbanowskit_1985]
- [Ishmael, Stephen D. et al 1990][research_ishmaelstephend_smithrogerse_1990]
- [Isogai 1979][research_isogai_1979]
- [Isogai 1981][research_isogai_1981]
- [Isogai 1988][research_isogai_1988]
- [Isogai 1989][research_isogai_1989]
- [Isogai 1992][research_isogai_1992]
- [Ito and Iwashita 2017][research_ito_iwashita_2017]
- [Ivler et al 2022][research_ivler_truong_2022]
- [Izadbakhsh and Kheirkhahan 2018][research_izadbakhsh_kheirkhahan_2018]
- [Izadbakhsh and khorashadizadeh 2019][research_izadbakhsh_khorashadizadeh_2019]
- [İnan and Aliskan 2025][research_inan_aliskan_2025]
- [J Elliott 1977][research_jelliott_1977]
- [Jacobs 1964][research_jacobs_1964]
- [Jacobson 1952][research_jacobson_1952]
- [Jacobson and Joshi 1977][research_jacobson_joshi_1977]
- [Jacobson and Joshi 1978][research_jacobson_joshi_1978]
- [Jacome and Elham 2018][research_jacome_elham_2018]
- [Jaeger and Hendry 1959][research_jaeger_hendry_1959]
- [Jafari and Mashadi 2022][research_jafari_mashadi_2022]
- [Jaffar Syed Mohamed Ali and Shahzatul Sakinah Binti Haron 2021][research_jaffarsyedmohamedali_shahzatulsakinahbintiharon_2021]
- [Jagana et al 2026][research_jagana_rajagopalan_2026]
- [Jajarmi and Hajipour 2016][research_jajarmi_hajipour_2016]
- [Jalalnezhad 2026][research_jalalnezhad_2026]
- [James A Franklin 1993][research_jamesafranklin_1993]
- [James M Luckring 2003][research_jamesmluckring_2003]
- [Janardhan and Grandhi 2003][research_janardhan_grandhi_2003]
- [Janecek 1986][research_janecek_1986]
- [Jang and Ahn 2022][research_jang_ahn_2022]
- [Jang et al 2015][research_jang_ahn_2015]
- [Jared A Grauer 2018][research_jaredagrauer_2018]
- [Jarrell R Elliott 1976][research_jarrellrelliott_1976]
- [Jarvis, C. R. 1967][research_jarviscr_1967]
- [Jarvis, C. R. 1975][research_jarviscr_1975]
- [Jarvis, C. R. and Szalai, K. J. 1981][research_jarviscr_szalaikj_1981]
- [Jategaonkar 2023][research_jategaonkar_2023]
- [Jategaonkar and Thielecke 1994][research_jategaonkar_thielecke_1994]
- [Jegley, Dawn C. and Bush, Harold G. 1997][research_jegleydawnc_bushharoldg_1997]
- [Jegley, Dawn C. and Bush, Harold G. 2001][research_jegleydawnc_bushharoldg_2001]
- [Jegley, Dawn C. and Wijayratne, Dulnath D. 2004][research_jegleydawnc_wijayratnedulnathd_2004]
- [Jegley, Dawn C. et al 2001][research_jegleydawnc_bushharoldg_2001_b]
- [Jegley, Dawn C. et al 2001][research_jegleydawnc_lovejoyandrewe_2001]
- [Jelovica and Cai 2022][research_jelovica_cai_2022]
- [Jeng and Payne 1995][research_jeng_payne_1995]
- [Jenks, G. E. et al 1977][research_jenksge_henryhf_1977]
- [Jenney and Schreadley 1984][research_jenney_schreadley_1984]
- [Jenney et al 1982][research_jenney_schreadley_1982]
- [Jensen and Crawley 1984][research_jensen_crawley_1984]
- [Jensen et al 1966][research_jensen_falby_1966]
- [Jensen et al 1982][research_jensen_crawley_1982]
- [Jeon and Kim 2026][research_jeon_kim_2026]
- [Jeon et al 2025][research_jeon_choi_2025]
- [Jeong et al 2024][research_jeong_suk_2024]
- [Jewell et al 1979][research_jewell_heffley_1979]
- [Jeyachandrabose and Kirkhope 1985][research_jeyachandrabose_kirkhope_1985]
- [Ji et al 2021][research_ji_kim_2021]
- [Ji et al 2021][research_ji_zhao_2021]
- [Ji et al 2022][research_ji_lu_2022]
- [Ji et al 2023][research_ji_kim_2023]
- [Ji et al 2024][research_ji_guo_2024]
- [Ji et al 2024][research_ji_ke_2024]
- [Ji et al 2025][research_ji_yang_2025]
- [Jia et al 2023][research_jia_ezhilarasu_2023]
- [Jia et al 2023][research_jia_sun_2023]
- [Jia et al 2024][research_jia_chen_2024]
- [Jia et al 2026][research_jia_feng_2026]
- [Jiang et al 2018][research_jiang_li_2018]
- [Jiang et al 2018][research_jiang_li_2018_b]
- [Jiang et al 2018][research_jiang_tian_2018]
- [Jiang et al 2019][research_jiang_tian_2019]
- [Jiang et al 2022][research_jiang_tong_2022]
- [Jiang et al 2023][research_jiang_ji_2023]
- [Jiang et al 2024][research_jiang_li_2024]
- [Jiang et al 2024][research_jiang_liu_2024]
- [Jiang et al 2024][research_jiang_yao_2024]
- [Jiang et al 2025][research_jiang_hu_2025]
- [Jianhong 2022][research_jianhong_2022]
- [Jianhong and Ramirez-Mendoza 2023][research_jianhong_ramirezmendoza_2023]
- [Jianhong and Yanxiang 2026][research_jianhong_yanxiang_2026]
- [Jiansong et al 2024][research_jiansong_chen_2024]
- [Jiao and Jiang 2015][research_jiao_jiang_2015]
- [Jin and Xue 2026][research_jin_xue_2026]
- [Jin et al 2015][research_jin_bifeng_2015]
- [Jing and Tzeng 1995][research_jing_tzeng_1995]
- [Jing et al 2020][research_jing_qi_2020]
- [Jing et al 2022][research_jing_li_2022]
- [Jing et al 2023][research_jing_duan_2023]
- [Jing et al 2024][research_jing_duan_2024]
- [Jo and Majid 2023][research_jo_majid_2023]
- [Johari et al 1995][research_johari_olinger_1995]
- [John et al 2019][research_john_qin_2019]
- [John W Hicks et al 1987][research_johnwhicks_jankania_1987]
- [Johnsen et al 2022][research_johnsen_runnels_2022]
- [Johnson 1964][research_johnson_1964]
- [Johnson 1965][research_johnson_1965]
- [Johnson 1969][research_johnson_1969]
- [Johnson 1972][research_johnson_1972]
- [Johnson 1973][research_johnson_1973]
- [Johnson and Nokes 1998][research_johnson_nokes_1998]
- [Johnson et al 1962][research_johnson_henderson_1962]
- [Johnson, R. W. and June, R. R. 1972][research_johnsonrw_junerr_1972]
- [Johnson, R. W. and Mccarty, J. E. 1977][research_johnsonrw_mccartyje_1977]
- [Johnson, W. 1977][research_johnsonw_1977]
- [Johnston and Cassarino 1976][research_johnston_cassarino_1976]
- [Johnston et al 1974][research_johnston_ashkenas_1974]
- [Jones 1970][research_jones_1970]
- [Jones 1976][research_jones_1976]
- [Jones and Jarrett 2018][research_jones_jarrett_2018]
- [Jones and Nisbet 1976][research_jones_nisbet_1976]
- [Jones et al 1985][research_jones_broughton_1985]
- [Jonnalagadda et al 2015][research_jonnalagadda_sawant_2015]
- [Jonsson et al 2019][research_jonsson_riso_2019]
- [Jonsson et al 2023][research_jonsson_riso_2023]
- [Joshi et al 2026][research_joshi_kalra_2026]
- [Jou and Metcalfe 1984][research_jou_metcalfe_1984]
- [Juhasz et al 2023][research_juhasz_tischler_2023]
- [Julian and Kochenderfer 2019][research_julian_kochenderfer_2019]
- [Jun-yi et al 2021][research_junyi_xinbing_2021]
- [Jusko and Berger 2026][research_jusko_berger_2026]
- [K Armah 2018][research_karmah_2018]
- [K. and Deodhare 2023][research_k_deodhare_2023]
- [Kabaliswaran and Das 2026][research_kabaliswaran_das_2026]
- [Kabashkin 2024][research_kabashkin_2024]
- [Kaczmarek 2026][research_kaczmarek_2026]
- [Kafkas et al 2021][research_kafkas_kilimtzidis_2021]
- [Kai 2024][research_kai_2024]
- [Kajiwara and Ton 2026][research_kajiwara_ton_2026]
- [Kakkar et al 2026][research_kakkar_streit_2026]
- [Kalam 1981][research_kalam_1981]
- [Kalam et al 2022][research_kalam_seshaiah_2022]
- [Kalinowski 2015][research_kalinowski_2015]
- [Kalinowski and Szczepanik 2021][research_kalinowski_szczepanik_2021]
- [Kalms and Bergmann 2020][research_kalms_bergmann_2020]
- [Kalnins 1968][research_kalnins_1968]
- [Kaloerov 1983][research_kaloerov_1983]
- [Kalugin et al 2022][research_kalugin_voropaev_2022]
- [Kamaletdinova and Romanov 2024][research_kamaletdinova_romanov_2024]
- [Kambampati and Smith 2017][research_kambampati_smith_2017]
- [Kambampati et al 2020][research_kambampati_townsend_2020]
- [Kambayashi and Kogiso 2026][research_kambayashi_kogiso_2026]
- [Kanazaki and Setoguchi 2023][research_kanazaki_setoguchi_2023]
- [Kang et al 2016][research_kang_park_2016]
- [Kano et al 2025][research_kano_ryuzono_2025]
- [Kanou and Ibuki 2025][research_kanou_ibuki_2025]
- [Kapania and Issac 1994][research_kapania_issac_1994]
- [Kapania et al 1991][research_kapania_bergen_1991]
- [Kapania, Rakesh K. et al 1997][research_kapaniarakeshk_issacj_1997]
- [Karal, Michael 2001][research_karalmichael_2001]
- [Karimi et al 2022][research_karimi_khorshidi_2022]
- [Karimi Kelayeh and Djavareshkian 2024][research_karimikelayeh_djavareshkian_2024]
- [Karkadakattil 2026][research_karkadakattil_2026]
- [Karkoszka 2019][research_karkoszka_2019]
- [Karniadakis 2004][research_karniadakis_2004]
- [Karpouzian 1991][research_karpouzian_1991]
- [Karpuk and Mosca 2024][research_karpuk_mosca_2024]
- [Karuna and Manohar 2017][research_karuna_manohar_2017]
- [Karuskevich et al 2022][research_karuskevich_maslak_2022]
- [Kashitani et al 2019][research_kashitani_takita_2019]
- [Kasim Biber and Trenton White 2019][research_kasimbiber_trentonwhite_2019]
- [Kassapakis and Warwick 1994][research_kassapakis_warwick_1994]
- [Kassem et al 2020][research_kassem_yang_2020]
- [Kassem et al 2021][research_kassem_yang_2021]
- [Kataoka et al 1986][research_kataoka_dol_1986]
- [Katunin et al 2015][research_katunin_dragan_2015]
- [Katz and Levin 1986][research_katz_levin_1986]
- [Katz et al 1986][research_katz_davidovitch_1986]
- [Kaul and Nguyen 2018][research_kaul_nguyen_2018]
- [Kawabe and Tokumaru 1991][research_kawabe_tokumaru_1991]
- [Kaygan and Ulusoy 2018][research_kaygan_ulusoy_2018]
- [Kazarin et al 2021][research_kazarin_golubev_2021]
- [Kcs et al 2024][research_kcs_james_2024]
- [Kearns 1962][research_kearns_1962]
- [Kehoe, M. W. 1984][research_kehoemw_1984]
- [Kehoe, M. W. and Ellison, J. F. 1985][research_kehoemw_ellisonjf_1985]
- [Kehoe, Michael W. 1987][research_kehoemichaelw_1987]
- [Kehoe, Michael W. et al 1990][research_kehoemichaelw_bjarkelisaj_1990]
- [Keidel et al 2020][research_keidel_fasel_2020]
- [Keith and Selberg 1984][research_keith_selberg_1984]
- [Keith and Selberg 1985][research_keith_selberg_1985]
- [Keller 2019][research_keller_2019]
- [Kendall 1985][research_kendall_1985]
- [Kennedy 1991][research_kennedy_1991]
- [Kenny and Lawrence 2025][research_kenny_lawrence_2025]
- [Kenway and Martins 2016][research_kenway_martins_2016]
- [Kevrekidis 2002][research_kevrekidis_2002]
- [Key 1971][research_key_1971]
- [Key 1982][research_key_1982]
- [Khadse and Karmore 2016][research_khadse_karmore_2016]
- [Khajah and Natarajan 2023][research_khajah_natarajan_2023]
- [Khalaf et al 2017][research_khalaf_gan_2017]
- [Khalil and Bauknecht 2024][research_khalil_bauknecht_2024]
- [Khalil and Fezans 2020][research_khalil_fezans_2020]
- [Khalil et al 2016][research_khalil_poirel_2016]
- [Khalil et al 2022][research_khalil_asaro_2022]
- [Khan and Riccio 2024][research_khan_riccio_2024]
- [Khanal and Adhikari 2026][research_khanal_adhikari_2026]
- [Khani et al 2017][research_khani_abdalla_2017]
- [Khankalantary et al 2021][research_khankalantary_rezaeeahvanouee_2021]
- [Kharghani and Mittelstedt 2022][research_kharghani_mittelstedt_2022]
- [Khargonekar and Sivashankar 1991][research_khargonekar_sivashankar_1991]
- [Kharisma 2019][research_kharisma_2019]
- [Kheiri and Riazat 2025][research_kheiri_riazat_2025]
- [Khodaverdian et al 2025][research_khodaverdian_gohil_2025]
- [Kholodar 2016][research_kholodar_2016]
- [Kholodar 2023][research_kholodar_2023]
- [Khusnul Novianingsih 2025][research_khusnulnovianingsih_2025]
- [Kida 1982][research_kida_1982]
- [Kieffer 2006][research_kieffer_2006]
- [Kielb 1975][research_kielb_1975]
- [Kilgore and Averett 1964][research_kilgore_averett_1964]
- [Kilimtzidis and Kostopoulos 2023][research_kilimtzidis_kostopoulos_2023]
- [Kilimtzidis and Kostopoulos 2023][research_kilimtzidis_kostopoulos_2023_b]
- [Kilimtzidis et al 2023][research_kilimtzidis_giannaros_2023]
- [Kim 2016][research_kim_2016]
- [Kim and Choi 2015][research_kim_choi_2015]
- [Kim and Kang 2025][research_kim_kang_2025]
- [Kim and Kim 2024][research_kim_kim_2024]
- [Kim and Kunz 2017][research_kim_kunz_2017]
- [Kim and Youn 2025][research_kim_youn_2025]
- [Kim et al 2016][research_kim_lee_2016]
- [Kim et al 2016][research_kim_shin_2016]
- [Kim et al 2017][research_kim_sung_2017]
- [Kim et al 2019][research_kim_oh_2019]
- [Kim et al 2022][research_kim_ji_2022]
- [Kim et al 2023][research_kim_philip_2023]
- [Kineyko 1982][research_kineyko_1982]
- [King and Brunner 1984][research_king_brunner_1984]
- [King and Johnson 1986][research_king_johnson_1986]
- [Kinney 1963][research_kinney_1963]
- [Kirsch et al 2020][research_kirsch_montagnier_2020]
- [Kirsch et al 2025][research_kirsch_fathi_2025]
- [Kish et al 1997][research_kish_mosle_1997]
- [Kishi et al 2016][research_kishi_kanazaki_2016]
- [Kishi et al 2022][research_kishi_kanazaki_2022]
- [Kisielowski et al 1967][research_kisielowski_perlmutter_1967]
- [Kisslinger and Wendl 1971][research_kisslinger_wendl_1971]
- [Kizildeniz and Kiyak 2025][research_kizildeniz_kiyak_2025]
- [Klasztorny et al 2018][research_klasztorny_nycz_2018]
- [Klein and Viswanathan 1973][research_klein_viswanathan_1973]
- [Klein, R. W. and Hollister, W. M. 1982][research_kleinrw_hollisterwm_1982]
- [Klein, R. W. et al 1982][research_kleinrw_lapinsm_1982]
- [Klema 1981][research_klema_1981]
- [Klepl 1995][research_klepl_1995]
- [Klimczyk and Goraj 2019][research_klimczyk_goraj_2019]
- [Klinar, W. J. et al 1975][research_klinarwj_kubiaket_1975]
- [Kljajic et al 2016][research_kljajic_kostic_2016]
- [Klotzsche, M. 1984][research_klotzschem_1984]
- [Klyde et al 2004][research_klyde_harris_2004]
- [Knackstedt 1952][research_knackstedt_1952]
- [Knauss, J. F. and Stone, R. H. 1982][research_knaussjf_stonerh_1982]
- [Knight 1982][research_knight_1982]
- [Knighton, Donna L. 1992][research_knightondonnal_1992]
- [Knox-Seith 1963][research_knoxseith_1963]
- [Ko et al 2019][research_ko_kang_2019]
- [Kobayashi and Torisaki 1986][research_kobayashi_torisaki_1986]
- [Kobelev 2019][research_kobelev_2019]
- [Kodama 1962][research_kodama_1962]
- [Koenig 1984][research_koenig_1984]
- [Koh 2018][research_koh_2018]
- [Koh and Kelly 1989][research_koh_kelly_1989]
- [Kohara et al 2016][research_kohara_tomoeda_2016]
- [Kohase et al 2018][research_kohase_watanabe_2018]
- [Kohlman 1963][research_kohlman_1963]
- [Kohlman 1979][research_kohlman_1979]
- [Kohn 1972][research_kohn_1972]
- [Kohnhorst and Magnacca 1980][research_kohnhorst_magnacca_1980]
- [Kokotovic et al 2000][research_kokotovic_murray_2000]
- [Kolar and Lile 1971][research_kolar_lile_1971]
- [Kolb et al 2019][research_kolb_montagnier_2019]
- [Kolesar 1971][research_kolesar_1971]
- [Komarov and Zinchenko 2023][research_komarov_zinchenko_2023]
- [Komnatska and Bondarenko 2017][research_komnatska_bondarenko_2017]
- [Komp et al 2024][research_komp_hajek_2024]
- [Konar et al 1974][research_konar_mahesh_1974]
- [Konatala et al 2024][research_konatala_milz_2024]
- [Kong et al 2025][research_kong_jeon_2025]
- [Kononov and Lymar 2020][research_kononov_lymar_2020]
- [Kontogiannis et al 2024][research_kontogiannis_savill_2024]
- [Koo and Lee 1994][research_koo_lee_1994]
- [Kopecki 2016][research_kopecki_2016]
- [Kopecki 2021][research_kopecki_2021]
- [Kornev et al 2021][research_kornev_ambrozhevich_2021]
- [Kosarev et al 2016][research_kosarev_seror_2016]
- [Koscielny 1983][research_koscielny_1983]
- [Kosmodamianskii and Mitrakov 1976][research_kosmodamianskii_mitrakov_1976]
- [Kosyanchuk et al 2015][research_kosyanchuk_selvesyuk_2015]
- [Kosyanchuk et al 2021][research_kosyanchuk_zheltov_2021]
- [Kota et al 1997][research_kota_hetrick_1997]
- [Kotitschke et al 2026][research_kotitschke_rupprecht_2026]
- [Kou and Zhang 2021][research_kou_zhang_2021]
- [Kousen and Bendiksen 1994][research_kousen_bendiksen_1994]
- [Koyuncuoglu and He 2022][research_koyuncuoglu_he_2022]
- [Kozhanov et al 2022][research_kozhanov_suvorova_2022]
- [Krachmalnick et al 1968][research_krachmalnick_vetsch_1968]
- [Kraft, Christopher C., Jr. and Reeder, J. P. 1948][research_kraftchristophercjr_reederjp_1948]
- [Kratochvíl and Valenta 2024][research_kratochvil_valenta_2024]
- [Krause et al 1990][research_krause_khargonekar_1990]
- [Krener 2001][research_krener_2001]
- [Kretov and Tiniakov 2022][research_kretov_tiniakov_2022]
- [Kriechbaum and Stineman 1972][research_kriechbaum_stineman_1972]
- [Krishnamurthy et al 2026][research_krishnamurthy_ramezani_2026]
- [Kroo 1982][research_kroo_1982]
- [Krzywoblocki 1943][research_krzywoblocki_1943]
- [Krüger et al 2022][research_kruger_meddaikar_2022]
- [Kuang et al 2025][research_kuang_hu_2025]
- [Kubiak et al 2019][research_kubiak_gliszczynski_2019]
- [Kubica et al 1995][research_kubica_livet_1995]
- [Kuder et al 2015][research_kuder_arrieta_2015]
- [Kuhlberg and Newirth 1976][research_kuhlberg_newirth_1976]
- [Kuhn 1975][research_kuhn_1975]
- [Kulhánek 2019][research_kulhanek_2019]
- [Kulikov 2020][research_kulikov_2020]
- [Kumar et al 2019][research_kumar_onkar_2019]
- [Kumar et al 2020][research_kumar_collini_2020]
- [Kumar et al 2022][research_kumar_kumar_2022]
- [Kumar et al 2025][research_kumar_asha_2025]
- [Kumar Shakya and Sekhar Padhee 2023][research_kumarshakya_sekharpadhee_2023]
- [Kuo-Jiun et al 1989][research_kuojiun_pongjeu_1989]
- [Kurade et al 2021][research_kurade_venkatakrishnan_2021]
- [Kurniawan 2022][research_kurniawan_2022]
- [Kurtz 2018][research_kurtz_2018]
- [Kurz 1963][research_kurz_1963]
- [Kurzhals, P. R. 1978][research_kurzhalspr_1978]
- [Kushner 1988][research_kushner_1988]
- [Kushner 2006][research_kushner_2006]
- [Kusni et al 2021][research_kusni_widiramdhani_2021]
- [Kuttieri and Sinha 2023][research_kuttieri_sinha_2023]
- [Kuvshinov 2016][research_kuvshinov_2016]
- [Kuvshinov 2016][research_kuvshinov_2016_b]
- [Kuvshinov and Leontiev 2019][research_kuvshinov_leontiev_2019]
- [Kuvshinov et al 2019][research_kuvshinov_lazurin_2019]
- [Kuz'mina et al 2020][research_kuzmina_ishmuratov_2020]
- [Kuznetsov and Kartashov 1980][research_kuznetsov_kartashov_1980]
- [Kuzu et al 2015][research_kuzu_bogosyan_2015]
- [Kwatny et al 1991][research_kwatny_bennett_1991]
- [Kwon et al 2019][research_kwon_park_2019]
- [Küfmann and Brillante 2017][research_kufmann_brillante_2017]
- [L'Afflitto 2018][research_lafflitto_2018]
- [L'Afflitto 2023][research_lafflitto_2023]
- [L'Afflitto and Blackford 2018][research_lafflitto_blackford_2018]
- [Lai 2024][research_lai_2024]
- [Lai and Young 1995][research_lai_young_1995]
- [Laitone 1978][research_laitone_1978]
- [Laitone 1989][research_laitone_1989]
- [Lakshminarayana 1962][research_lakshminarayana_1962]
- [Lam 1993][research_lam_1993]
- [Lam et al 1989][research_lam_hung_1989]
- [Lamar, J. E. 1978][research_lamarje_1978]
- [Lamar, J. E. and Frink, N. T. 1981][research_lamarje_frinknt_1981]
- [Lamar, J. E. and Frink, N. T. 1981][research_lamarje_frinknt_1981_b]
- [Lamar, J. E. and Luckring, J. M. 1979][research_lamarje_luckringjm_1979]
- [Lamar, J. E. et al 1980][research_lamarje_schemenskyrt_1980]
- [Lampton et al 2024][research_lampton_klyde_2024]
- [Lan, C. E. 1986][research_lance_1986]
- [Lan, C. Edward and Tseng, J. B. 1987][research_lancedward_tsengjb_1987]
- [Landfield and Rajkovic 1986][research_landfield_rajkovic_1986]
- [Landsberger and Dugundji 1985][research_landsberger_dugundji_1985]
- [Lang and de Ruiter 2021][research_lang_deruiter_2021]
- [Lang et al 2024][research_lang_li_2024]
- [Langston 1967][research_langston_1967]
- [Lanteigne et al 2020][research_lanteigne_mcleod_2020]
- [Lapins, M. et al 1982][research_lapinsm_kleinrw_1982]
- [Larson, Richard R. 1987][research_larsonrichardr_1987]
- [Latachi et al 2020][research_latachi_rachidi_2020]
- [Latency Control in Real-Time 2025][research_latency_control_2025]
- [Latz 2006][research_latz_2006]
- [Latz 2007][research_latz_2007]
- [Latz 2009][research_latz_2009]
- [Laub 1991][research_laub_1991]
- [Laura and Viazzi 1985][research_laura_viazzi_1985]
- [Lavretsky 2019][research_lavretsky_2019]
- [Law 1976][research_law_1976]
- [Lawrence et al 2018][research_lawrence_theodore_2018]
- [Layton and Trenchea 2011][research_layton_trenchea_2011]
- [Le 2026][research_le_2026]
- [Lee 1977][research_lee_1977]
- [Lee 1995][research_lee_1995]
- [Lee 2016][research_lee_2016]
- [Lee 2019][research_lee_2019]
- [Lee and Cho 1991][research_lee_cho_1991]
- [Lee and Cho 1991][research_lee_cho_1991_b]
- [Lee and Eyi 1993][research_lee_eyi_1993]
- [Lee and Kim 1995][research_lee_kim_1995]
- [Lee and Kim 2021][research_lee_kim_2021]
- [Lee and Ko 2018][research_lee_ko_2018]
- [Lee and Lee 1990][research_lee_lee_1990]
- [Lee and Lee 2019][research_lee_lee_2019]
- [Lee and Lua 2025][research_lee_lua_2025]
- [Lee and Lua 2026][research_lee_lua_2026]
- [Lee and Mall 1989][research_lee_mall_1989]
- [Lee and Ohman 1984][research_lee_ohman_1984]
- [Lee and Ohman 1984][research_lee_ohman_1984_b]
- [Lee and Sheikh 2025][research_lee_sheikh_2025]
- [Lee and Sheu 1994][research_lee_sheu_1994]
- [Lee and Singh 2017][research_lee_singh_2017]
- [Lee and Singh 2018][research_lee_singh_2018]
- [Lee and Tang 1989][research_lee_tang_1989]
- [Lee and Yun 2022][research_lee_yun_2022]
- [Lee et al 1982][research_lee_mallett_1982]
- [Lee et al 1994][research_lee_kim_1994]
- [Lee et al 2017][research_lee_snyder_2017]
- [Lee et al 2018][research_lee_song_2018]
- [Lee et al 2020][research_lee_kim_2020]
- [Lee et al 2023][research_lee_lee_2023]
- [Lehilahy and Ferdi 2023][research_lehilahy_ferdi_2023]
- [Lehman and Stearman 1977][research_lehman_stearman_1977]
- [Lei et al 2019][research_lei_bai_2019]
- [Lei et al 2020][research_lei_wang_2020]
- [Lei et al 2021][research_lei_bai_2021]
- [Lei et al 2021][research_lei_guo_2021]
- [Leicester 1970][research_leicester_1970]
- [Leighton 1978][research_leighton_1978]
- [Leitch et al 2024][research_leitch_stodieck_2024]
- [Leitch et al 2025][research_leitch_stodieck_2025]
- [Lekoudis 1980][research_lekoudis_1980]
- [Lemay, S. P. et al 1988][research_lemaysp_batillsm_1988]
- [Lemley 1968][research_lemley_1968]
- [Lemmon and Coleman 1973][research_lemmon_coleman_1973]
- [Lendraitis 2019][research_lendraitis_2019]
- [Lendraitis and Lukoševičius 2023][research_lendraitis_lukosevicius_2023]
- [Lendraitis and Lukoševičius 2025][research_lendraitis_lukosevicius_2025]
- [Lennartson 1989][research_lennartson_1989]
- [Leondes and Rankine 1972][research_leondes_rankine_1972]
- [Lepri et al 2024][research_lepri_bacciu_2024]
- [Lerner and Markowitz 1979][research_lerner_markowitz_1979]
- [Lerro et al 2020][research_lerro_brandl_2020]
- [Lesoinne 2007][research_lesoinne_2007]
- [Levi and Nelson 1964][research_levi_nelson_1964]
- [Levison 1982][research_levison_1982]
- [Li 2023][research_li_2023]
- [Li and Luo 2026][research_li_luo_2026]
- [Li and Pak 2015][research_li_pak_2015]
- [Li and Qin 2020][research_li_qin_2020]
- [Li and Qin 2021][research_li_qin_2021]
- [Li and Qin 2021][research_li_qin_2021_b]
- [Li and Qin 2022][research_li_qin_2022]
- [Li and Sanfelice 2016][research_li_sanfelice_2016]
- [Li and Shi 2021][research_li_shi_2021]
- [Li and Wang 2018][research_li_wang_2018]
- [Li and Wang 2021][research_li_wang_2021_b]
- [Li and Yang 2017][research_li_yang_2017]
- [Li and Zhang 2021][research_li_zhang_2021]
- [Li and Zhang 2021][research_li_zhang_2021_b]
- [Li and Zhang 2024][research_li_zhang_2024_c]
- [Li and Zhou 2024][research_li_zhou_2024]
- [Li et al 2016][research_li_bai_2016]
- [Li et al 2016][research_li_chen_2016]
- [Li et al 2016][research_li_guo_2016]
- [Li et al 2017][research_li_jin_2017]
- [Li et al 2018][research_li_bai_2018]
- [Li et al 2018][research_li_dong_2018]
- [Li et al 2018][research_li_huang_2018]
- [Li et al 2018][research_li_shen_2018]
- [Li et al 2018][research_li_wang_2018_b]
- [Li et al 2018][research_li_zhang_2018]
- [Li et al 2019][research_li_bai_2019]
- [Li et al 2019][research_li_bai_2019_b]
- [Li et al 2019][research_li_daronch_2019]
- [Li et al 2019][research_li_gong_2019]
- [Li et al 2019][research_li_he_2019]
- [Li et al 2019][research_li_zhang_2019]
- [Li et al 2020][research_li_tang_2020]
- [Li et al 2020][research_li_wang_2020]
- [Li et al 2021][research_li_liu_2021]
- [Li et al 2021][research_li_liu_2021_b]
- [Li et al 2021][research_li_wan_2021]
- [Li et al 2021][research_li_wang_2021]
- [Li et al 2021][research_li_wang_2021_c]
- [Li et al 2022][research_li_bai_2022]
- [Li et al 2022][research_li_li_2022]
- [Li et al 2022][research_li_liu_2022]
- [Li et al 2022][research_li_sun_2022]
- [Li et al 2022][research_li_yuan_2022]
- [Li et al 2022][research_li_zhang_2022]
- [Li et al 2023][research_li_liu_2023]
- [Li et al 2023][research_li_luo_2023]
- [Li et al 2023][research_li_yang_2023]
- [Li et al 2024][research_li_he_2024]
- [Li et al 2024][research_li_kou_2024]
- [Li et al 2024][research_li_qian_2024]
- [Li et al 2024][research_li_yang_2024]
- [Li et al 2024][research_li_zhang_2024]
- [Li et al 2024][research_li_zhang_2024_b]
- [Li et al 2024][research_li_zhang_2024_d]
- [Li et al 2024][research_li_zheng_2024]
- [Li et al 2025][research_li_hu_2025]
- [Li et al 2025][research_li_ji_2025]
- [Li et al 2025][research_li_li_2025]
- [Li et al 2025][research_li_li_2025_b]
- [Li et al 2025][research_li_lin_2025]
- [Li et al 2025][research_li_shang_2025]
- [Li et al 2025][research_li_shi_2025]
- [Li et al 2025][research_li_shi_2025_b]
- [Li et al 2025][research_li_xiong_2025]
- [Li et al 2025][research_li_zheng_2025]
- [Li et al 2026][research_li_han_2026]
- [Li et al 2026][research_li_miranda_2026]
- [Li et al 2026][research_li_shen_2026]
- [Li et al 2026][research_li_wang_2026]
- [Li et al 2026][research_li_wang_2026_b]
- [Li et al 2026][research_li_xu_2026]
- [Li et al 2026][research_li_yang_2026]
- [Li et al 2026][research_li_yoon_2026]
- [Li, Wesley W. and Pak, Chan-Gi 2014][research_liwesleyw_pakchangi_2014]
- [Lian and Cao 2026][research_lian_cao_2026]
- [Liang and Ren 2018][research_liang_ren_2018]
- [Liang et al 2024][research_liang_gao_2024]
- [Liang et al 2024][research_liang_yin_2024]
- [Liang et al 2025][research_liang_ye_2025]
- [Liao and Sun 1993][research_liao_sun_1993]
- [Liao et al 2021][research_liao_song_2021]
- [Libeskind et al 1973][research_libeskind_minecci_1973]
- [Librescu and Khdeir 1988][research_librescu_khdeir_1988]
- [Librescu and Simovich 1988][research_librescu_simovich_1988]
- [Librescu and Song 1992][research_librescu_song_1992]
- [Librescu and Thangjitham 1991][research_librescu_thangjitham_1991]
- [Lichota 2023][research_lichota_2023]
- [Liefer, Randall K. 1990][research_lieferrandallk_1990]
- [Liew and Wang 1993][research_liew_wang_1993]
- [Lifshits and Ryzhov 1978][research_lifshits_ryzhov_1978]
- [Liguori et al 2024][research_liguori_zucco_2024]
- [Lijewski 1988][research_lijewski_1988]
- [Lim et al 1989][research_lim_senthilnathan_1989]
- [Lin and Crawley 1995][research_lin_crawley_1995]
- [Lin et al 1989][research_lin_lu_1989]
- [Lin et al 1994][research_lin_chin_1994]
- [Lind, Rick C. et al 1997][research_lindrickc_brennermartinj_1997]
- [Lindhorst et al 2015][research_lindhorst_haupt_2015]
- [Lindsay and Fikes 1976][research_lindsay_fikes_1976]
- [Lindsay and Jordan 1975][research_lindsay_jordan_1975]
- [Linigier et al 1980][research_linigier_dahlquist_1980]
- [Lisovyi and Petrovska 2021][research_lisovyi_petrovska_2021]
- [Little 1973][research_little_1973]
- [Liu 2004][research_liu_2004]
- [Liu 2018][research_liu_2018]
- [Liu 2019][research_liu_2019]
- [Liu 2024][research_liu_2024]
- [Liu and Buss 2022][research_liu_buss_2022]
- [Liu and Gao 2018][research_liu_gao_2018]
- [Liu and Gao 2020][research_liu_gao_2020_b]
- [Liu and He 2018][research_liu_he_2018]
- [Liu and Lin 2024][research_liu_lin_2024]
- [Liu and Liu 2025][research_liu_liu_2025]
- [Liu and Sang 2018][research_liu_sang_2018]
- [Liu and Sun 2016][research_liu_sun_2016]
- [Liu and Sun 2017][research_liu_sun_2017]
- [Liu and Tian 2019][research_liu_tian_2019]
- [Liu and Wang 2019][research_liu_wang_2019]
- [Liu and Wang 2022][research_liu_wang_2022]
- [Liu and Zhang 2018][research_liu_zhang_2018]
- [Liu and Zhao 2026][research_liu_zhao_2026]
- [Liu et al 2009][research_liu_liou_2009]
- [Liu et al 2015][research_liu_toropov_2015]
- [Liu et al 2016][research_liu_song_2016]
- [Liu et al 2016][research_liu_ye_2016]
- [Liu et al 2017][research_liu_bai_2017]
- [Liu et al 2017][research_liu_huang_2017]
- [Liu et al 2017][research_liu_sun_2017_b]
- [Liu et al 2018][research_liu_an_2018]
- [Liu et al 2018][research_liu_luo_2018]
- [Liu et al 2019][research_liu_chen_2019]
- [Liu et al 2019][research_liu_featherston_2019]
- [Liu et al 2020][research_liu_gao_2020]
- [Liu et al 2021][research_liu_dong_2021]
- [Liu et al 2022][research_liu_kan_2022]
- [Liu et al 2022][research_liu_sun_2022]
- [Liu et al 2023][research_liu_chen_2023]
- [Liu et al 2023][research_liu_featherston_2023]
- [Liu et al 2023][research_liu_feng_2023]
- [Liu et al 2023][research_liu_gao_2023]
- [Liu et al 2023][research_liu_li_2023]
- [Liu et al 2023][research_liu_zhang_2023]
- [Liu et al 2023][research_liu_zheng_2023]
- [Liu et al 2023][research_liu_zhou_2023]
- [Liu et al 2024][research_liu_ji_2024]
- [Liu et al 2024][research_liu_zhang_2024]
- [Liu et al 2024][research_liu_zou_2024]
- [Liu et al 2025][research_liu_sun_2025]
- [Liu et al 2025][research_liu_wu_2025]
- [Liu et al 2025][research_liu_zheng_2025]
- [Liu et al 2026][research_liu_du_2026]
- [Liu et al 2026][research_liu_geng_2026]
- [Liu et al 2026][research_liu_huang_2026]
- [Liu et al 2026][research_liu_li_2026]
- [Liu et al 2026][research_liu_li_2026_b]
- [Liu et al 2026][research_liu_liu_2026]
- [Liu et al 2026][research_liu_namakiaraghi_2026]
- [Liu et al 2026][research_liu_qian_2026]
- [Liu et al 2026][research_liu_shen_2026]
- [Liu et al 2026][research_liu_wang_2026]
- [Liu et al 2026][research_liu_yang_2026]
- [Liu et al 2026][research_liu_yu_2026]
- [Livne 2018][research_livne_2018]
- [Lloyd and Sholl 1968][research_lloyd_sholl_1968]
- [Lo 1978][research_lo_1978]
- [Lo 1979][research_lo_1979]
- [Lo 1980][research_lo_1980]
- [Lo 1981][research_lo_1981]
- [Lobitz et al 2023][research_lobitz_traub_2023]
- [Lock, W. P. et al 1975][research_lockwp_petersenwr_1975]
- [Lockwood Taylor 1942][research_lockwoodtaylor_1942]
- [Loghis and Xiros 2022][research_loghis_xiros_2022]
- [Loh 1986][research_loh_1986]
- [Loja et al 2017][research_loja_barbosa_2017]
- [Lokos, William A. 1990][research_lokoswilliama_1990]
- [Lombardi 1995][research_lombardi_1995]
- [Lombardi and Morelli 1994][research_lombardi_morelli_1994]
- [Lombardi and Vicini 1994][research_lombardi_vicini_1994]
- [Lomo et al 2023][research_lomo_patel_2023]
- [Long 2019][research_long_2019]
- [Long et al 2021][research_long_mu_2021]
- [Loos and Springer 1983][research_loos_springer_1983]
- [Loth and Boyle 1969][research_loth_boyle_1969]
- [Loth et al 2000][research_loth_geubelle_2000]
- [Lottati 1985][research_lottati_1985]
- [Lottati 1987][research_lottati_1987]
- [Lottati 1988][research_lottati_1988]
- [Loughlan 2019][research_loughlan_2019]
- [Loughlan and Ata 1995][research_loughlan_ata_1995]
- [Lovatt 1986][research_lovatt_1986]
- [Lovejoy, Andrew E. and Scotti, Stephen J. 2019][research_lovejoyandrewe_scottistephenj_2019]
- [Lowe 1988][research_lowe_1988]
- [Lowson 1990][research_lowson_1990]
- [Lu 1994][research_lu_1994]
- [Lu and Murthy 1990][research_lu_murthy_1990]
- [Lu et al 2015][research_lu_zhang_2015]
- [Lu et al 2016][research_lu_vankampen_2016]
- [Lu et al 2017][research_lu_tian_2017]
- [Lu et al 2018][research_lu_fang_2018]
- [Lu et al 2019][research_lu_hu_2019]
- [Lu et al 2019][research_lu_ma_2019]
- [Lu et al 2019][research_lu_zhang_2019]
- [Lu et al 2022][research_lu_hong_2022]
- [Lu et al 2025][research_lu_cao_2025]
- [Luat T Nguyen et al 1980][research_luattnguyen_williampgilbert_1980]
- [Lucarini et al 2025][research_lucarini_dirito_2025]
- [Lucas 1978][research_lucas_1978]
- [Ludeña Cervantes et al 2020][research_ludenacervantes_choi_2020]
- [Luk'yanov 1968][research_lukyanov_1968]
- [Lundry 1967][research_lundry_1967]
- [Lundry 1977][research_lundry_1977]
- [Lunghitano et al 2024][research_lunghitano_afonso_2024]
- [Lungu and Lungu 2015][research_lungu_lungu_2015]
- [Luo and Bao 1988][research_luo_bao_1988]
- [Luo and Liu 2015][research_luo_liu_2015]
- [Luo et al 2022][research_luo_zhang_2022]
- [Luo et al 2024][research_luo_ferrari_2024]
- [Luo et al 2025][research_luo_chen_2025]
- [Luo et al 2025][research_luo_yin_2025]
- [Luo et al 2026][research_luo_yu_2026]
- [Luongo and Casciati 2016][research_luongo_casciati_2016]
- [Lv et al 2019][research_lv_lei_2019]
- [Lyapunov 1993][research_lyapunov_1993]
- [Lynch et al 2018][research_lynch_mordasky_2018]
- [Lyu and Liem 2020][research_lyu_liem_2020]
- [Lyu and Martins 2015][research_lyu_martins_2015]
- [Lyu et al 2015][research_lyu_kenway_2015]
- [Lyu et al 2018][research_lyu_cao_2018]
- [Lyu et al 2019][research_lyu_zhang_2019]
- [Lyu et al 2025][research_lyu_xu_2025]
- [Lyubchak and Fil'shtinskii 1982][research_lyubchak_filshtinskii_1982]
- [Löhrer et al 2025][research_lohrer_krause_2025]
- [Löser 1985][research_loser_1985]
- [Lü et al 2024][research_lu_zhang_2024]
- [M. and Jury 1959][research_m_jury_1959]
- [Ma and Chen 2023][research_ma_chen_2023]
- [Ma et al 2015][research_ma_guo_2015]
- [Ma et al 2019][research_ma_dong_2019]
- [Ma et al 2023][research_ma_abouhamzeh_2023]
- [Ma et al 2024][research_ma_abouhamzeh_2024]
- [Ma et al 2024][research_ma_yu_2024]
- [Ma et al 2025][research_ma_liu_2025]
- [Ma et al 2025][research_ma_zhou_2025]
- [Mabboux et al 2024][research_mabboux_pommierbudinger_2024]
- [MacDonald 1933][research_macdonald_1933]
- [Mackall, D. A. et al 1988][research_mackallda_pickettmd_1988]
- [Mackall, Dale A. and Allen, James G. 1989][research_mackalldalea_allenjamesg_1989]
- [Mackall, Dale A. and Allen, James G. 1991][research_mackalldalea_allenjamesg_1991]
- [Maenhout et al 2021][research_maenhout_billiet_2021]
- [Maewal 1984][research_maewal_1984]
- [Magee and Taylor 1971][research_magee_taylor_1971]
- [Magliacano et al 2025][research_magliacano_tufano_2025]
- [Magness et al 1993][research_magness_robinson_1993]
- [Magnus and Yoshihara 1975][research_magnus_yoshihara_1975]
- [Maguire et al 2024][research_maguire_mamalis_2024]
- [Mahapatra and Halbe 2024][research_mahapatra_halbe_2024]
- [Mahboub et al 2022][research_mahboub_rouabah_2022]
- [Mahdavi Zafarghandi and Reza Soltani 2024][research_mahdavizafarghandi_rezasoltani_2024]
- [Mahgoub and Cortelezzi 2020][research_mahgoub_cortelezzi_2020]
- [Mahgoub and El-Badawy 2022][research_mahgoub_elbadawy_2022]
- [Mahmood 2025][research_mahmood_2025]
- [Mahroni 2021][research_mahroni_2021]
- [Mahulkar 2010][research_mahulkar_2010]
- [Maine and Murray 1988][research_maine_murray_1988]
- [Maity et al 2019][research_maity_hocht_2019]
- [Maiworm et al 2021][research_maiworm_limon_2021]
- [Malcom 1969][research_malcom_1969]
- [Malcom, L. G. and Husband, J. H. 1976][research_malcomlg_husbandjh_1976]
- [Malekpour et al 2025][research_malekpour_abdali_2025]
- [Malik et al 2017][research_malik_akhtar_2017]
- [Mallik et al 2015][research_mallik_kapania_2015]
- [Mallios 1964][research_mallios_1964]
- [Mamedov et al 2018][research_mamedov_paryshev_2018]
- [Mammadov and Hajiyev 2018][research_mammadov_hajiyev_2018]
- [Mamonova et al 2019][research_mamonova_soudakov_2019]
- [Mandal and Gu 2016][research_mandal_gu_2016]
- [Manickam et al 2025][research_manickam_polit_2025]
- [Mann, M. J. and Mercer, C. E. 1985][research_mannmj_mercerce_1985]
- [Mann, M. J. and Mercer, C. E. 1986][research_mannmj_mercerce_1986]
- [Mann, M. J. et al 1983][research_mannmj_campbellrl_1983]
- [Mann, M. J. et al 1984][research_mannmj_campbellrl_1984]
- [Mannini and Bartoli 2015][research_mannini_bartoli_2015]
- [Mansour 1970][research_mansour_1970]
- [Mansy and Faruque 2023][research_mansy_faruque_2023]
- [Mant 1972][research_mant_1972]
- [Manzoor et al 2016][research_manzoor_maqsood_2016]
- [Mao et al 2018][research_mao_dou_2018]
- [Mao et al 2019][research_mao_xie_2019]
- [Mao et al 2020][research_mao_li_2020]
- [Mar and Lin 1979][research_mar_lin_1979]
- [Marano et al 2022][research_marano_belardo_2022]
- [Marcus 1994][research_marcus_1994]
- [Mardanpour et al 2018][research_mardanpour_izadpanahi_2018]
- [Mareca Rios et al 2023][research_marecarios_montesbarrenetxea_2023]
- [Marilyn E Ogburn et al 1991][research_marilyneogburn_johnvfoster_1991]
- [Marques et al 2017][research_marques_natarajan_2017]
- [Marqui et al 2017][research_marqui_bueno_2017]
- [Marquis and Farhood 2026][research_marquis_farhood_2026]
- [Marr and Roderick 1975][research_marr_roderick_1975]
- [Martin 1978][research_martin_1978]
- [Martin Co Baltimore Md 1965][research_martincobaltimoremd_1965]
- [Martin Co Denver Co 1966][research_martincodenverco_1966]
- [Martin et al 2019][research_martin_hartwig_2019]
- [Martindale et al 1974][research_martindale_rockwell_1974]
- [Martín et al 2017][research_martin_pardo_2017]
- [Martínez-Heredia et al 2026][research_martinezheredia_fernandezprada_2026]
- [Maruyama et al 2024][research_maruyama_ogino_2024]
- [Marín and Graciani 2022][research_marin_graciani_2022]
- [Masini et al 2019][research_masini_timme_2019]
- [Masini et al 2020][research_masini_timme_2020]
- [Mason, M. L. and Capone, F. J. 1983][research_masonml_caponefj_1983]
- [Masuda et al 2016][research_masuda_shimosawa_2016]
- [Mateer, George C. et al 1987][research_mateergeorgec_seegmillerhlee_1987]
- [Mathur et al 2026][research_mathur_huang_2026]
- [Matos and Marta 2025][research_matos_marta_2025]
- [Matrix cracking and stiffness 1985][research_matrix_cracking_1985]
- [Matsuki et al 2018][research_matsuki_nishiyama_2018]
- [Matt et al 2025][research_matt_chao_2025]
- [Mayer et al 2016][research_mayer_prowe_2016]
- [Mayer et al 2019][research_mayer_lutz_2019]
- [Mazaheri and Khatibirad 2016][research_mazaheri_khatibirad_2016]
- [Mazaheri and Khatibirad 2017][research_mazaheri_khatibirad_2017]
- [Mazaheri and Nejati 2015][research_mazaheri_nejati_2015]
- [Mazaheri et al 2015][research_mazaheri_kiani_2015]
- [Mazaheri et al 2015][research_mazaheri_nejati_2015_b]
- [Mazaheri et al 2016][research_mazaheri_nejati_2016]
- [Mazaheri et al 2017][research_mazaheri_nejati_2017]
- [Maślanka et al 2025][research_maslanka_kachel_2025]
- [McAllister and Esfahani 2025][research_mcallister_esfahani_2025]
- [McCaskill 1953][research_mccaskill_1953]
- [McComb et al 1987][research_mccomb_hayduk_1987]
- [McCutchen 1980][research_mccutchen_1980]
- [McDonald 2001][research_mcdonald_2001]
- [McDonald and Farris 1964][research_mcdonald_farris_1964]
- [Mcdonnell Aircraft Corp St Louis Mo 1962][research_mcdonnellaircraftcorpstlouismo_1962]
- [Mcdonnell Aircraft Corp St Louis Mo 1963][research_mcdonnellaircraftcorpstlouismo_1963]
- [McDonnell and Ning 2020][research_mcdonnell_ning_2020]
- [McEneaney 1999][research_mceneaney_1999]
- [McEneaney 2013][research_mceneaney_2013]
- [McFadden et al 2023][research_mcfadden_brandt_2023]
- [McGough et al 1974][research_mcgough_moses_1974]
- [McGREGOR and Smith 1966][research_mcgregor_smith_1966]
- [McGurk et al 2024][research_mcgurk_stodieck_2024]
- [McIntosh et al 2024][research_mcintosh_mishra_2024]
- [McKeehen and Cord 1997][research_mckeehen_cord_1997]
- [McKillip 1991][research_mckillip_1991]
- [McKinney 1972][research_mckinney_1972]
- [McKlNNEY and DOLLYHlGH 1971][research_mcklnney_dollyhlgh_1971]
- [McMaster and Schenk 1974][research_mcmaster_schenk_1974]
- [Mcruer, D. et al 1986][research_mcruerd_johnstond_1986]
- [McWilliam et al 2018][research_mcwilliam_zahle_2018]
- [Mefford et al 1948][research_mefford_voss_1948]
- [Meglinskii 1966][research_meglinskii_1966]
- [Mehmed, Oral 1988][research_mehmedoral_1988]
- [Mei and Giurgiutiu 2018][research_mei_giurgiutiu_2018]
- [Mei et al 2021][research_mei_wang_2021]
- [Meirovitch 1995][research_meirovitch_1995]
- [Melville et al 2020][research_melville_bramesfeld_2020]
- [Memon et al 2021][research_memon_white_2021]
- [Menet et al 1993][research_menet_menart_1993]
- [Meng and Jiang 2025][research_meng_jiang_2025]
- [Meng et al 2019][research_meng_yan_2019]
- [Meng et al 2024][research_meng_fu_2024]
- [Mengzhu et al 2026][research_mengzhu_zhitao_2026]
- [Menon 1989][research_menon_1989]
- [Menon and Yousefpor 1996][research_menon_yousefpor_1996]
- [Mertaugh 1998][research_mertaugh_1998]
- [Mertins 1991][research_mertins_1991]
- [Mertins 1992][research_mertins_1992]
- [Mhenni et al 2016][research_mhenni_choley_2016]
- [Miaadi and Li 2021][research_miaadi_li_2021]
- [Miao et al 2017][research_miao_wei_2017]
- [Michaud et al 2018][research_michaud_dalir_2018]
- [Micheli 2024][research_micheli_2024]
- [Micks 1950][research_micks_1950]
- [Miele 1976][research_miele_1976]
- [Mihaila-Andres et al 2019][research_mihailaandres_rosu_2019]
- [Mihály et al 2017][research_mihaly_gaspar_2017]
- [Mijovic 1985][research_mijovic_1985]
- [Miles and Broughton 2017][research_miles_broughton_2017]
- [Miller 1965][research_miller_1965]
- [Miller 1970][research_miller_1970]
- [Miller 1986][research_miller_1986]
- [Miller and Clark 1965][research_miller_clark_1965]
- [Miller et al 1983][research_miller_wykes_1983]
- [Milz et al 2026][research_milz_may_2026]
- [Miner, D. D. and Gloss, B. B. 1975][research_minerdd_glossbb_1975]
- [Ming et al 2026][research_ming_hu_2026]
- [Mingong and Sun 2022][research_mingong_sun_2022]
- [Minwalla et al 2016][research_minwalla_thomas_2016]
- [Miranda and Bidinotto 2025][research_miranda_bidinotto_2025]
- [Miranda et al 2025][research_miranda_li_2025]
- [Mirtaba et al 2022][research_mirtaba_jeddi_2022]
- [Mishra et al 2025][research_mishra_yadav_2025]
- [Miska and Balzani 2025][research_miska_balzani_2025]
- [Missoum 2012][research_missoum_2012]
- [Mitchell 1961][research_mitchell_1961]
- [Mitchell et al 1980][research_mitchell_myers_1980]
- [Miura, Hirokazu and Neill, Douglas J. 1992][research_miurahirokazu_neilldouglasj_1992]
- [Miyasato 1992][research_miyasato_1992]
- [Miyazawa 1993][research_miyazawa_1993]
- [Mkhoyan et al 2022][research_mkhoyan_thakrar_2022]
- [Mobayen and Izadbakhsh 2025][research_mobayen_izadbakhsh_2025]
- [Mochizuki and Yamada 2018][research_mochizuki_yamada_2018]
- [Modaress-Aval et al 2019][research_modaressaval_bakhtiarinejad_2019]
- [Modi and Slater 1983][research_modi_slater_1983]
- [Modi and Slater 1994][research_modi_slater_1994]
- [Modified L1 Adaptive Control 2018][research_modified_l1_2018]
- [Moens 2019][research_moens_2019]
- [Moes, Timothy R. et al 2000][research_moestimothyr_noffzgregoryk_2000]
- [Moes, Timothy R. et al 2003][research_moestimothyr_smithmarks_2003]
- [Moghtadaei 2024][research_moghtadaei_2024]
- [Mohamed and G 2020][research_mohamed_g_2020]
- [Mohammad Zadeh and Sayadi 2018][research_mohammadzadeh_sayadi_2018]
- [Mohammadi et al 2025][research_mohammadi_ebrahimi_2025]
- [Mohan and Gaitonde 2017][research_mohan_gaitonde_2017]
- [Mohankumar et al 2021][research_mohankumar_hall_2021]
- [Mohankumar et al 2022][research_mohankumar_hall_2022]
- [Mohanty and Chhotaray 1979][research_mohanty_chhotaray_1979]
- [Mohseni and Bernstein 2024][research_mohseni_bernstein_2024]
- [Mojallizadeh 2026][research_mojallizadeh_2026]
- [Mokhtarimousavi and Mehrabi 2023][research_mokhtarimousavi_mehrabi_2023]
- [Molent and Haddad 2020][research_molent_haddad_2020]
- [Monaghan, R. C. 1981][research_monaghanrc_1981]
- [Monasa and Snyder 1981][research_monasa_snyder_1981]
- [Moni et al 2024][research_moni_yao_2024]
- [Monshizadeh 2020][research_monshizadeh_2020]
- [Montgomery 1972][research_montgomery_1972]
- [Montgomery and Caglayan 1976][research_montgomery_caglayan_1976]
- [Montgomery and Price 1976][research_montgomery_price_1976]
- [Montgomery, R. C. and Price, D. B. 1974][research_montgomeryrc_pricedb_1974]
- [Moon 1996][research_moon_1996]
- [Moore 1972][research_moore_1972]
- [Moore, N. R. et al 1992][research_moorenr_ebbelerdh_1992]
- [Moorhouse and Jenkins 1975][research_moorhouse_jenkins_1975]
- [Moosavi and Elasha 2022][research_moosavi_elasha_2022]
- [Moradi and Zalaghi 2025][research_moradi_zalaghi_2025]
- [Moreira et al 2022][research_moreira_gripp_2022]
- [Moreira et al 2024][research_moreira_moleiro_2024]
- [Morgado et al 2016][research_morgado_silvestre_2016]
- [Morino and Obayashi 2015][research_morino_obayashi_2015]
- [Morita and Matsukawa 1995][research_morita_matsukawa_1995]
- [Moriya 1982][research_moriya_1982]
- [Morozov and Chermoshentsev, 2019][research_morozov_chermoshentsev_2019]
- [Morozov and Janschek 2016][research_morozov_janschek_2016]
- [Morris 1977][research_morris_1977]
- [Morrison and White 1976][research_morrison_white_1976]
- [Morton et al 2023][research_morton_xu_2023]
- [Mosaad 2023][research_mosaad_2023]
- [Moshier 2006][research_moshier_2006]
- [Motta et al 2019][research_motta_malzacher_2019]
- [Mottershead and Cooper 2012][research_mottershead_cooper_2012]
- [Moul, Martin T and Wineman, Andrew R 1952][research_moulmartint_winemanandrewr_1952]
- [Moul, Martin T. and Brown, Lawrence W. 1959][research_moulmartint_brownlawrencew_1959]
- [Mourey, D. J. 1979][research_moureydj_1979]
- [Mtowe et al 2025][research_mtowe_long_2025]
- [Mu et al 2022][research_mu_huang_2022]
- [Mu et al 2026][research_mu_huang_2026]
- [Mueller and Brito 2003][research_mueller_brito_2003]
- [Muir et al 2017][research_muir_arredondogaleana_2017]
- [Mukherjee and Halder 2017][research_mukherjee_halder_2017]
- [Mukherjee and Sinha 2017][research_mukherjee_sinha_2017]
- [Mukhopadhyay, Vivek and Sorokach, Michael R. 2015][research_mukhopadhyayvivek_sorokachmichaelr_2015]
- [Mulder 1988][research_mulder_1988]
- [Murphy et al 1976][research_murphy_peloubet_1976]
- [Murphy, Patrick C. 1996][research_murphypatrickc_1996]
- [Murray et al 2015][research_murray_doman_2015]
- [Murri, D. G. et al 1983][research_murridg_croomma_1983]
- [Murri, D. G. et al 1984][research_murridg_nguyenlt_1984]
- [Muscarello et al 2016][research_muscarello_quaranta_2016]
- [Muñoz and García-Fogeda 2022][research_munoz_garciafogeda_2022]
- [Muñoz and García-Fogeda 2024][research_munoz_garciafogeda_2024]
- [Myers and Walsh 1991][research_myers_walsh_1991]
- [Na and Lee 2024][research_na_lee_2024]
- [NACA Conference on Aerodynamic 1949][research_naca_conference_1949]
- [NACA Conference on Aircraft 1957][research_naca_conference_1957]
- [Naderi Lordejani et al 2023][research_naderilordejani_besselink_2023]
- [Nagabhushan 1991][research_nagabhushan_1991]
- [Naganarayana and Atluri 1995][research_naganarayana_atluri_1995]
- [Nagaraja et al 1982][research_nagaraja_lakin_1982]
- [Nagib and Wigeland 1977][research_nagib_wigeland_1977]
- [Nagy 1979][research_nagy_1979]
- [Nagy and Fossati 2022][research_nagy_fossati_2022]
- [Naihong et al 1993][research_naihong_yaohua_1993]
- [Najmi et al 2024][research_najmi_khan_2024]
- [Nakamura 1982][research_nakamura_1982]
- [Nakamura and Takesue 1990][research_nakamura_takesue_1990]
- [Nakamura et al 2017][research_nakamura_kawamura_2017]
- [Nalini and Dhanalakshmi 2019][research_nalini_dhanalakshmi_2019]
- [Nam et al 2000][research_nam_chen_2000]
- [Nam et al 2025][research_nam_choi_2025]
- [Namani Koureh et al 2026][research_namanikoureh_shahverdi_2026]
- [Nambiar and Pachidis 2022][research_nambiar_pachidis_2022]
- [Nan et al 2024][research_nan_zheng_2024]
- [Napolitano 2002][research_napolitano_2002]
- [Napolitano, Marcello R. 1996][research_napolitanomarcellor_1996]
- [Napolitano, Marcello R. and Spagnuolo, Joelle M. 1993][research_napolitanomarcellor_spagnuolojoellem_1993]
- [Narayanan et al 2026][research_narayanan_kumar_2026]
- [Narendra and Tripathi 1973][research_narendra_tripathi_1973]
- [Narenshakthi and Dharani 2025][research_narenshakthi_dharani_2025]
- [Naresh and Srinivas 2024][research_naresh_srinivas_2024]
- [Narimani et al 2024][research_narimani_joulaei_2024]
- [Narimani et al 2025][research_narimani_haddadpour_2025]
- [nath and ana 2017][research_nath_ana_2017]
- [Navrátil 2017][research_navratil_2017]
- [Nazarenko and Nevezhina 1972][research_nazarenko_nevezhina_1972]
- [Nazari et al 2017][research_nazari_seron_2017]
- [Nazeer et al 2021][research_nazeer_wang_2021]
- [Neal and Smith 1970][research_neal_smith_1970]
- [Negaard 1980][research_negaard_1980]
- [Negahban B. et al 2025][research_negahbanb_khalafi_2025]
- [Negahban et al 2024][research_negahban_bashir_2024]
- [Nejati and Mazaheri 2017][research_nejati_mazaheri_2017]
- [Nekooei et al 2021][research_nekooei_farsangi_2021]
- [Nelson and Mouch 1978][research_nelson_mouch_1978]
- [Neu and Huang 1973][research_neu_huang_1973]
- [Neville et al 1992][research_neville_marois_1992]
- [Newkirk 1979][research_newkirk_1979]
- [Newton and Kroo 2025][research_newton_kroo_2025]
- [Nguyen 2019][research_nguyen_2019]
- [Nguyen and Goulet 2018][research_nguyen_goulet_2018]
- [Nguyen and Lejeune 2026][research_nguyen_lejeune_2026]
- [Nguyen et al 2016][research_nguyen_olaru_2016]
- [Nguyen et al 2018][research_nguyen_reynolds_2018]
- [Nguyen et al 2021][research_nguyen_lowenberg_2021]
- [Nguyen et al 2025][research_nguyen_han_2025]
- [Nguyen et al 2026][research_nguyen_prodan_2026]
- [Nguyen, L. T. et al 1979][research_nguyenlt_gilbertwp_1979]
- [Nguyen, Luat T. and Gilert, William P. 1990][research_nguyenluatt_gilertwilliamp_1990]
- [Nguyen, Nhan and James Urnes, Sr. 2012][research_nguyennhan_jamesurnessr_2012]
- [Nguyen, Nhan et al 2015][research_nguyennhan_kaulupender_2015]
- [Ni et al 2021][research_ni_wu_2021]
- [Ni et al 2023][research_ni_li_2023]
- [Nibbelink, Bruce D. and Peters, David A. 1993][research_nibbelinkbruced_petersdavida_1993]
- [Niblett 1986][research_niblett_1986]
- [Niblett 1988][research_niblett_1988]
- [Nicholas, W. U. et al 1984][research_nicholaswu_navillegl_1984]
- [Nicolaides 1971][research_nicolaides_1971]
- [Niehaus 1962][research_niehaus_1962]
- [Niel et al 2017][research_niel_seuret_2017]
- [Nield and Iv 1981][research_nield_iv_1981]
- [Nihtilä 1989][research_nihtila_1989]
- [Nikolaev 2019][research_nikolaev_2019]
- [Nikolaou et al 2026][research_nikolaou_kilimtzidis_2026]
- [Nikrad et al 2015][research_nikrad_asadi_2015]
- [Ning 2021][research_ning_2021]
- [Nissen 2009][research_nissen_2009]
- [Nitschke et al 2019][research_nitschke_vincenti_2019]
- [Nitz 1989][research_nitz_1989]
- [Nitzsche and Breitbach 1994][research_nitzsche_breitbach_1994]
- [Niu and Li 2022][research_niu_li_2022]
- [Niu and Zhang 2022][research_niu_zhang_2022]
- [Niu et al 2018][research_niu_chen_2018]
- [Niu et al 2026][research_niu_li_2026]
- [Niven 1977][research_niven_1977]
- [Nixon, Mark W. et al 1999][research_nixonmarkw_piatakdavidj_1999]
- [Noll et al 1984][research_noll_eastep_1984]
- [Non-linear bending of antisymmetric 1977][research_non_linear_bending_1977]
- [Nonnenmacher and Jones 2016][research_nonnenmacher_jones_2016]
- [Nonweiler 1960][research_nonweiler_1960]
- [Noordin et al 2023][research_noordin_mohdbasri_2023]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]
- [Norton 1990][research_norton_1990]
- [Norwood 1992][research_norwood_1992]
- [Ntantis and Xezonakis 2024][research_ntantis_xezonakis_2024]
- [Numerical Analysis of the 2017][research_numerical_analysis_2017]
- [Numerical and Experimental Determination 2019][research_numerical_and_2019]
- [Numerical Study of Geometrical 2023][research_numerical_study_2023]
- [Nuttall 1997][research_nuttall_1997]
- [O'Connell et al 2022][research_oconnell_tseytlin_2022]
- [O'Donnell, James R., Jr. et al 2002][research_odonnelljamesrjr_davisgaryt_2002]
- [Oberkampf and Nicolaides 1971][research_oberkampf_nicolaides_1971]
- [Obilanade et al 2025][research_obilanade_torlind_2025]
- [Ocali and Sezer 1992][research_ocali_sezer_1992]
- [Ochi and Kanai 1995][research_ochi_kanai_1995]
- [Ochôa et al 2019][research_ochoa_groves_2019]
- [ODonnell, James R., Jr. et al 1999][research_odonnelljamesrjr_andrewsstephenf_1999]
- [Oelker and Hummel 1989][research_oelker_hummel_1989]
- [Oganyan and Loginov 2025][research_oganyan_loginov_2025]
- [Ogilvie and Shen 1973][research_ogilvie_shen_1973]
- [Ogunvoul et al 2017][research_ogunvoul_balanchuk_2017]
- [Oh 2023][research_oh_2023]
- [Ohkawa 1985][research_ohkawa_1985]
- [Ohkawa 1986][research_ohkawa_1986]
- [Ohki et al 2015][research_ohki_itakura_2015]
- [Ohkuma 1993][research_ohkuma_1993]
- [Ohta et al 1979][research_ohta_nikiforuk_1979]
- [Ohta et al 1982][research_ohta_nikiforuk_1982]
- [Oktay and Özen 2022][research_oktay_ozen_2022]
- [Okumoto and Elsanker 1973][research_okumoto_elsanker_1973]
- [Oland et al 2016][research_oland_andersen_2016]
- [Olivett et al 2021][research_olivett_corrao_2021]
- [Olsen 1965][research_olsen_1965]
- [Olsen 1966][research_olsen_1966]
- [Olson, Glenn O. 1982][research_olsonglenno_1982]
- [Om et al 2020][research_om_park_2020]
- [Omodei 1977][research_omodei_1977]
- [Onat and Tolle 1979][research_onat_tolle_1979]
- [Onkar 2021][research_onkar_2021]
- [Onkar et al 2024][research_onkar_kumar_2024]
- [Operational Technologies Corp San Antonio Tx 1996][research_operationaltechnologiescorpsanantoniotx_1996]
- [Opgenoord and Willcox 2019][research_opgenoord_willcox_2019]
- [Optimizing Material Shortages in 2025][research_optimizing_material_2025]
- [Orkwis 1995][research_orkwis_1995]
- [Orlik-Ruckemann 1983][research_orlikruckemann_1983]
- [Osder et al 1976][research_osder_mossman_1976]
- [Oshima and Takano 2024][research_oshima_takano_2024]
- [Osipov 2016][research_osipov_2016]
- [Osipov 2017][research_osipov_2017]
- [Osipov 2019][research_osipov_2019]
- [Ossmann and Joos 2016][research_ossmann_joos_2016]
- [Ossmann and Joos 2017][research_ossmann_joos_2017]
- [Ostheimer and Giguere 1963][research_ostheimer_giguere_1963]
- [Ostojic and Sethi 2026][research_ostojic_sethi_2026]
- [Othman et al 2019][research_othman_silva_2019]
- [Otsuka and Makihara 2017][research_otsuka_makihara_2017]
- [Ouyang and Lin 2017][research_ouyang_lin_2017]
- [Ouyang et al 2021][research_ouyang_gu_2021]
- [Ouyang et al 2021][research_ouyang_zeng_2021]
- [Ouzts, Peter J. et al 2009][research_ouztspeterj_solowaydonaldi_2009]
- [Over 136 000 flying 1981][research_over_136_1981]
- [Oyarhossein et al 2025][research_oyarhossein_sugiyama_2025]
- [Oyibo 1984][research_oyibo_1984]
- [Oza and Vala 2021][research_oza_vala_2021]
- [Ozbek et al 2024][research_ozbek_ekici_2024]
- [Ozdil and Carlsson 1992][research_ozdil_carlsson_1992]
- [O’Brien and Datta 2026][research_obrien_datta_2026]
- [O’Donnell and Mohseni 2019][research_odonnell_mohseni_2019]
- [O’Rourke et al 2019][research_orourke_kolmanovsky_2019]
- [Packard et al 2009][research_packard_seiler_2009]
- [Padovan 1973][research_padovan_1973]
- [Padovan 1974][research_padovan_1974]
- [Padovan and Gosset 1974][research_padovan_gosset_1974]
- [Pagano 1974][research_pagano_1974]
- [Paine 1950][research_paine_1950]
- [Palframan et al 2019][research_palframan_fry_2019]
- [Palkin and Zenchenko 2025][research_palkin_zenchenko_2025]
- [Palm, Tod et al 2000][research_palmtod_mahlermary_2000]
- [Pan and Cheng 1995][research_pan_cheng_1995]
- [Pan and Huang 2019][research_pan_huang_2019]
- [Pan and Liu 2019][research_pan_liu_2019]
- [Pan et al 2026][research_pan_jin_2026]
- [Pandey and Murray 2022][research_pandey_murray_2022]
- [Pangas and Gamboa 2025][research_pangas_gamboa_2025]
- [Panuntun et al 2020][research_panuntun_wahyunggoro_2020]
- [Papadales and Basil S. 1979][research_papadales_basils_1979]
- [Papirno 1977][research_papirno_1977]
- [Parbery and Karihaloo 1980][research_parbery_karihaloo_1980]
- [Parbery∗ and Olhoff 1987][research_parbery_olhoff_1987]
- [Park 2015][research_park_2015]
- [Park 2016][research_park_2016]
- [Park and Oh 2017][research_park_oh_2017]
- [Park et al 2017][research_park_choi_2017]
- [Park et al 2017][research_park_jung_2017]
- [Park et al 2024][research_park_ramirezserrano_2024]
- [Park et al 2025][research_park_ramirezserrano_2025]
- [Park et al 2026][research_park_kang_2026]
- [Parker and Simonson 1982][research_parker_simonson_1982]
- [Parker and Simonson 1982][research_parker_simonson_1982_b]
- [Parker and Simonson 1982][research_parker_simonson_1982_c]
- [Parmar et al 2022][research_parmar_singh_2022]
- [Parthiv N Shah et al 2023][research_parthivnshah_ericlblades_2023]
- [Passenbrunner et al 2016][research_passenbrunner_sassano_2016]
- [Passive wing/store flutter suppression 1982][research_passive_wing_store_1982]
- [Patartics et al 2022][research_patartics_liptak_2022]
- [Pate 1964][research_pate_1964]
- [Pate and Deitering 1963][research_pate_deitering_1963]
- [Patel et al 2022][research_patel_kumar_2022]
- [Patel et al 2023][research_patel_deodhare_2023]
- [Patne et al 2020][research_patne_ingole_2020]
- [Patni et al 2019][research_patni_minera_2019]
- [Patrick C Murphy 1999][research_patrickcmurphy_1999]
- [Pattarakunnan et al 2021][research_pattarakunnan_galos_2021]
- [Patterson and Grenestedt 2018][research_patterson_grenestedt_2018]
- [Paul and Rein 2017][research_paul_rein_2017]
- [Paulk and Anderson 1976][research_paulk_anderson_1976]
- [Paulson, J. W., Jr. and Thomas, J. L. 1978][research_paulsonjwjr_thomasjl_1978]
- [Paulson, J. W., Jr. and Thomas, J. L. 1979][research_paulsonjwjr_thomasjl_1979_b]
- [Paulson, J. W., Jr. et al 1979][research_paulsonjwjr_thomasjl_1979]
- [Payton 2017][research_payton_2017]
- [PC implementation of optimal 1994][research_pc_implementation_1994]
- [Pearson, Henry A and Aiken, William S , Jr 1944][research_pearsonhenrya_aikenwilliamsjr_1944]
- [Peck and Hudson 1956][research_peck_hudson_1956]
- [Pedrioli et al 2026][research_pedrioli_vaiuso_2026]
- [Peled, U. and Powell, J. D. 1978][research_peledu_powelljd_1978]
- [Pellerin 1988][research_pellerin_1988]
- [Pelykh and Andryushchenko 2024][research_pelykh_andryushchenko_2024]
- [Pena, Francisco 2020][research_penafrancisco_2020]
- [Pena, Francisco et al 2018][research_penafrancisco_martinsbenjamin_2018]
- [Pendem 2023][research_pendem_2023]
- [Pendleton et al 1995][research_pendleton_moster_1995]
- [Peng and Chen 2022][research_peng_chen_2022]
- [Peng et al 1994][research_peng_zhang_1994]
- [Peng et al 2020][research_peng_zhu_2020]
- [Peng et al 2026][research_peng_cao_2026]
- [Peng et al 2026][research_peng_li_2026]
- [Pengelley and Wilson 1954][research_pengelley_wilson_1954]
- [Pennycuick 1989][research_pennycuick_1989]
- [Pereira et al 2021][research_pereira_sales_2021]
- [Perfect et al 2015][research_perfect_jump_2015]
- [Perfect et al 2015][research_perfect_jump_2015_b]
- [Perkins and Brice 1966][research_perkins_brice_1966]
- [Perkins et al 1977][research_perkins_jr_1977]
- [Perry 2025][research_perry_2025]
- [Perry and Rievley 1961][research_perry_rievley_1961]
- [Perry, B., III 1976][research_perrybiii_1976]
- [Perry, B., III 1982][research_perrybiii_1982]
- [Persoon et al 1980][research_persoon_roos_1980]
- [Persoon et al 1984][research_persoon_horsten_1984]
- [Peters, David A. 1988][research_petersdavida_1988]
- [Petersen, K. L. 1981][research_petersenkl_1981]
- [Petre and Ashley 1976][research_petre_ashley_1976]
- [Petriconi et al 2026][research_petriconi_lomazzi_2026]
- [Petterssen 1953][research_petterssen_1953]
- [Peyada and Ghosh 2023][research_peyada_ghosh_2023]
- [Pfeifle and Fichter 2023][research_pfeifle_fichter_2023]
- [Pfnür and Breitsamter 2019][research_pfnur_breitsamter_2019]
- [Pham 2022][research_pham_2022]
- [Phan 2020][research_phan_2020]
- [Philibert et al 2022][research_philibert_yao_2022]
- [Philippidis, 1994][research_philippidis_1994]
- [Phillips 1965][research_phillips_1965]
- [Phuekpan et al 2025][research_phuekpan_khammee_2025]
- [Piao et al 2019][research_piao_zhang_2019]
- [Picon and Alarcon 1978][research_picon_alarcon_1978]
- [Pidaparti 1993][research_pidaparti_1993]
- [Pidaparti and Yang 1993][research_pidaparti_yang_1993]
- [Pierce and Varga 1972][research_pierce_varga_1972]
- [Pierre et al 2023][research_pierre_iervolino_2023]
- [Pizzoli et al 2022][research_pizzoli_saltari_2022]
- [Place et al 1974][research_place_altmann_1974]
- [Placek and Ruchała 2018][research_placek_ruchala_2018]
- [Plaetschke et al 1982][research_plaetschke_mulder_1982]
- [Platus 1980][research_platus_1980]
- [Plotkin 1978][research_plotkin_1978]
- [Plyako 1977][research_plyako_1977]
- [Poll 1986][research_poll_1986]
- [Pollack and van Kampen 2023][research_pollack_vankampen_2023]
- [Pollack et al 2024][research_pollack_theodoulis_2024]
- [Pollack et al 2026][research_pollack_theodoulis_2026]
- [Polonsky 2026][research_polonsky_2026]
- [Polyester, fibreglass-reinforced composite laminate 1978][research_polyester_fibreglass_reinforced_1978]
- [Poole et al 2022][research_poole_allen_2022]
- [Poole et al 2026][research_poole_allen_2026]
- [Portapas and Cooke 2020][research_portapas_cooke_2020]
- [Posingies 1979][research_posingies_1979]
- [Poss 2018][research_poss_2018]
- [Postnikov and Sabaev 1968][research_postnikov_sabaev_1968]
- [Pourtakdoust and Khodabakhsh 2026][research_pourtakdoust_khodabakhsh_2026]
- [Poussot-Vassal et al 2017][research_poussotvassal_demourant_2017]
- [Powell, Richard W. 1993][research_powellrichardw_1993]
- [Powers 1982][research_powers_1982]
- [Powers, B. G. 1980][research_powersbg_1980]
- [Prajapati and Prasad 2019][research_prajapati_prasad_2019]
- [Prasad and Pešek 2018][research_prasad_pesek_2018]
- [Prasad et al 1967][research_prasad_nematnasser_1967]
- [Prasannakumar et al 2024][research_prasannakumar_sudhi_2024]
- [Pratama 2021][research_pratama_2021]
- [Preissler and Schaufele 1991][research_preissler_schaufele_1991]
- [Price and Lee 1993][research_price_lee_1993]
- [Pritt 1980][research_pritt_1980]
- [Property changes of a 1981][research_property_changes_1981]
- [Prototype Digital Flight Control 1986][research_prototype_digital_1986]
- [Pryor and Barker 1970][research_pryor_barker_1970]
- [Przekop, Adam and Jegley, Dawn C. 2014][research_przekopadam_jegleydawnc_2014_b]
- [Przekop, Adam et al 2014][research_przekopadam_jegleydawnc_2014]
- [Pusch et al 2019][research_pusch_knoblach_2019]
- [Pushtaev 1989][research_pushtaev_1989]
- [Puthisikamani et al 2023][research_puthisikamani_sreenivasaraja_2023]
- [Putnam, T. W. 1983][research_putnamtw_1983]
- [Putnam, T. W. 1984][research_putnamtw_1984]
- [Putnam, T. W. 1984][research_putnamtw_1984_b]
- [Putnam, T. W. et al 1986][research_putnamtw_petersenkl_1986]
- [Pérez et al 2022][research_perez_theodoulis_2022]
- [Qi and Zhao 2020][research_qi_zhao_2020]
- [Qi et al 2018][research_qi_zhao_2018]
- [Qi et al 2026][research_qi_yuan_2026]
- [Qian 2018][research_qian_2018]
- [Qian et al 2015][research_qian_zhang_2015]
- [Qian et al 2025][research_qian_lu_2025]
- [Qian et al 2025][research_qian_xinhui_2025]
- [Qian et al 2026][research_qian_gao_2026]
- [Qiao et al 2018][research_qiao_gao_2018]
- [Qiao et al 2018][research_qiao_wu_2018]
- [Qin et al 2017][research_qin_liu_2017]
- [Qin et al 2023][research_qin_liu_2023]
- [Qin et al 2025][research_qin_yang_2025]
- [Qing et al 2020][research_qing_liu_2020]
- [Qiu 2022][research_qiu_2022]
- [Qiu and Wang 2016][research_qiu_wang_2016]
- [Qiu et al 2017][research_qiu_yuan_2017]
- [Qiu et al 2018][research_qiu_fang_2018]
- [Qiu et al 2022][research_qiu_deng_2022]
- [Qu and Annaswamy 2016][research_qu_annaswamy_2016]
- [Qu and Li 2022][research_qu_li_2022]
- [Quagliarella and Iuliano 2017][research_quagliarella_iuliano_2017]
- [Quality Control Method of 2020][research_quality_control_2020]
- [Quero et al 2019][research_quero_vuillemin_2019]
- [Radetskaya 2022][research_radetskaya_2022]
- [Radford, R. C. et al 1980][research_radfordrc_smithr_1980]
- [Rafi et al 2017][research_rafi_steck_2017]
- [Ragab et al 2018][research_ragab_hajj_2018]
- [Raghav and Komerath 2015][research_raghav_komerath_2015]
- [Raghavan 1971][research_raghavan_1971]
- [Rahima et al 2026][research_rahima_yassine_2026]
- [Rainbird et al 2015][research_rainbird_peiro_2015]
- [Raiola et al 2021][research_raiola_discetti_2021]
- [Rais-Rohani, M. et al 1992][research_raisrohanim_haftkart_1992]
- [Rais-Rohani, Masoud 1994][research_raisrohanimasoud_1994]
- [Rais-Rohani, Masound 1999][research_raisrohanimasound_1999]
- [Rajamurugu et al 2024][research_rajamurugu_satyam_2024]
- [Rajpal et al 2019][research_rajpal_kassapoglou_2019]
- [Rajpal et al 2021][research_rajpal_mitrotta_2021]
- [Ram Dewangan et al 2026][research_ramdewangan_dewangan_2026]
- [Ramamoorthy 1992][research_ramamoorthy_1992]
- [Ramroop et al 2025][research_ramroop_chinchamee_2025]
- [Ranaudo, Richard J. et al 2000][research_ranaudorichardj_ratvaskythomasp_2000]
- [Raney, David L. 1987][research_raneydavidl_1987]
- [Rao 1975][research_rao_1975]
- [Rao and Padmanabhan 2019][research_rao_padmanabhan_2019]
- [Rao and Uma Maheswara Rao 1992][research_rao_umamaheswararao_1992]
- [Rao et al 1973][research_rao_hofer_1973]
- [Rao et al 2023][research_rao_shi_2023]
- [Raouf 1994][research_raouf_1994]
- [Raper 1991][research_raper_1991]
- [Rapoff, Andrew J. et al 1990][research_rapoffandrewj_dillharoldd_1990]
- [Rashed and Demir 2022][research_rashed_demir_2022]
- [Rashmikant and Abe 2026][research_rashmikant_abe_2026]
- [Rate sensitivity of Mode 1988][research_rate_sensitivity_1988]
- [Rath and Fichter 2020][research_rath_fichter_2020]
- [Rathnasabapathy et al 2022][research_rathnasabapathy_mouritz_2022]
- [Rauer 2019][research_rauer_2019]
- [Ray, E. J. et al 1972][research_rayej_mckinneylw_1972]
- [Ray, E. J. et al 1973][research_rayej_mckinneylw_1973]
- [Rayankula and Pathak 2021][research_rayankula_pathak_2021]
- [Rea et al 2017][research_rea_pecora_2017]
- [Rea et al 2018][research_rea_pecora_2018]
- [Rea J B Co Inc Santa Monica Ca 1957][research_reajbcoincsantamonicaca_1957]
- [Reader 1976][research_reader_1976]
- [Reca Luque et al 2023][research_recaluque_aguilartorres_2023]
- [Reddy 1982][research_reddy_1982]
- [Reddy 1987][research_reddy_1987]
- [Redeker and Wichmann 1991][research_redeker_wichmann_1991]
- [Rediess, H. A. and Szalai, K. J. 1975][research_rediessha_szalaikj_1975]
- [Reding and Ericsson 1977][research_reding_ericsson_1977]
- [Reed 1994][research_reed_1994]
- [Reeder 1958][research_reeder_1958]
- [Refinement of aircraft dynamics 2023][research_refinement_of_2023]
- [Regulator with reference model 2022][research_regulator_with_2022]
- [Rehan et al 2015][research_rehan_iqbal_2015]
- [Rehman 2022][research_rehman_2022]
- [Rehman et al 2025][research_rehman_ekici_2025]
- [Reid et al 1994][research_reid_rajagopal_1994]
- [Reinbold et al 2026][research_reinbold_breitsamter_2026]
- [Reist et al 2019][research_reist_zingg_2019]
- [Reist et al 2020][research_reist_koo_2020]
- [Reist et al 2022][research_reist_koo_2022]
- [Rekik et al 2024][research_rekik_khaled_2024]
- [Ren 1986][research_ren_1986]
- [Ren and Lissenden 2016][research_ren_lissenden_2016]
- [Ren et al 2017][research_ren_qiu_2017]
- [Ren et al 2018][research_ren_qiu_2018]
- [Ren et al 2022][research_ren_zhang_2022]
- [Ren et al 2025][research_ren_xu_2025]
- [Repa et al 1977][research_repa_alexandridis_1977]
- [Report no. 121, The 1921][research_report_no_1921]
- [Report No. 349. A 1930][research_report_no_1930]
- [Research and Design of 2022][research_research_and_2022]
- [Research on flight technology 2023][research_research_on_2023]
- [Research on Semi-active Suppression 2025][research_research_on_2025]
- [Resta et al 2021][research_resta_marsilio_2021]
- [Restifo et al 2026][research_restifo_villa_2026]
- [Review of Fault-tolerant Control 2024][research_review_of_2024]
- [Reyes et al 2019][research_reyes_climent_2019]
- [Rhodes, M. D. and Selberg, B. P. 1982][research_rhodesmd_selbergbp_1982]
- [Rich, M. J. et al 1974][research_richmj_ridgleygf_1974]
- [Richards 1979][research_richards_1979]
- [Richards et al 2016][research_richards_yao_2016]
- [Richardson 2007][research_richardson_2007]
- [Richter et al 2024][research_richter_calix_2024]
- [Richwine, David M. and Fisher, David F. 1991][research_richwinedavidm_fisherdavidf_1991]
- [Rickard, W. W. 1978][research_rickardww_1978]
- [Ricketts, R. H. and Doggett, R. V., Jr. 1980][research_rickettsrh_doggettrvjr_1980]
- [Ricketts, R. H. et al 1983][research_rickettsrh_sandfordmc_1983]
- [Ricketts, R. H. et al 1983][research_rickettsrh_watsonjj_1983]
- [Rieck et al 2026][research_rieck_herrmann_2026]
- [Ried 1986][research_ried_1986]
- [Riefe 1946][research_riefe_1946]
- [Rigatos 2021][research_rigatos_2021]
- [Rimer et al 1984][research_rimer_chipman_1984]
- [Rimer et al 1986][research_rimer_chipman_1986]
- [Rimer, M. et al 1984][research_rimerm_chipmanr_1984]
- [Ringertz 1994][research_ringertz_1994]
- [Rinoie et al 2015][research_rinoie_komuro_2015]
- [Rising, J. J. et al 1984][research_risingjj_daviswj_1984]
- [Riso and Cesnik 2023][research_riso_cesnik_2023]
- [Rittenhouse 1959][research_rittenhouse_1959]
- [Ritter et al 1971][research_ritter_gurley_1971]
- [Rivero et al 2021][research_rivero_fournier_2021]
- [Rizzetta 1977][research_rizzetta_1977]
- [Rizzetta 1979][research_rizzetta_1979]
- [Rizzetta and Visbal 2016][research_rizzetta_visbal_2016]
- [Roache 1965][research_roache_1965]
- [Robbins et al 2023][research_robbins_stansbury_2023]
- [Roberts 1986][research_roberts_1986]
- [Roberts et al 1966][research_roberts_smith_1966]
- [Roberts et al 2015][research_roberts_reed_2015]
- [Roberts, P. A. et al 1977][research_robertspa_swaimrl_1977]
- [Robinson 2004][research_robinson_2004]
- [Robotics 2024][research_robotics_2024]
- [Robust Controller Design Based 2016][research_robust_controller_2016]
- [Rocha et al 2023][research_rocha_antunes_2023]
- [Rockwell 1994][research_rockwell_1994]
- [Rodden 1981][research_rodden_1981]
- [Rodden 1984][research_rodden_1984]
- [Rodden 1989][research_rodden_1989]
- [Rodden 1989][research_rodden_1989_b]
- [Rodden and Bellinger 1982][research_rodden_bellinger_1982]
- [Rodemich and Andrew 1965][research_rodemich_andrew_1965]
- [Rodgers 1965][research_rodgers_1965]
- [Rodgers 1966][research_rodgers_1966]
- [Rodinò and Maletta 2024][research_rodino_maletta_2024]
- [Rogalski 2018][research_rogalski_2018]
- [Rogalski et al 2020][research_rogalski_rzucidlo_2020]
- [Rogalski et al 2021][research_rogalski_rzucidlo_2021]
- [Rogers 1970][research_rogers_1970]
- [Rogersten et al 2013][research_rogersten_xu_2013]
- [Rogólski and Olejnik 2018][research_rogolski_olejnik_2018]
- [Roh et al 2024][research_roh_park_2024]
- [Rohella and Chatterjee 1979][research_rohella_chatterjee_1979]
- [Rohith and Sinha 2020][research_rohith_sinha_2020]
- [Rohn and Loewenthal 1985][research_rohn_loewenthal_1985]
- [Roizner and Karpel 2018][research_roizner_karpel_2018]
- [Roizner and Karpel 2019][research_roizner_karpel_2019]
- [Roizner et al 2019][research_roizner_raveh_2019]
- [Rokhsaz and Selberg 1990][research_rokhsaz_selberg_1990]
- [Rom and Lamar 1992][research_rom_lamar_1992]
- [Romano et al 2019][research_romano_ciminello_2019]
- [Romkes et al 2002][research_romkes_prudhomme_2002]
- [Ronfle-Nadaud 2009][research_ronflenadaud_2009]
- [Rong et al 2022][research_rong_huang_2022]
- [Rong et al 2023][research_rong_dou_2023]
- [Rongrong et al 2018][research_rongrong_zhengyin_2018]
- [Rooney, R. H. et al 1982][research_rooneyrh_chungjc_1982]
- [Roorda 1967][research_roorda_1967]
- [Roos et al 1989][research_roos_mushlin_1989]
- [Rosa et al 2022][research_rosa_susanto_2022]
- [Rosa et al 2023][research_rosa_pouca_2023]
- [Roscoe et al 1975][research_roscoe_eisele_1975]
- [Rose and Seginer 1978][research_rose_seginer_1978]
- [Rosema et al 2011][research_rosema_doyle_2011]
- [Rosema et al 2014][research_rosema_doyle_2014]
- [Rosen, Bruce S. 1988][research_rosenbruces_1988]
- [Rosenblum et al 2019][research_rosenblum_vrchota_2019]
- [Rosenkrantz 1985][research_rosenkrantz_1985]
- [Rosique et al 2019][research_rosique_alamin_2019]
- [Roskam, J. and Lan, C. 1973][research_roskamj_lanc_1973]
- [Roskam, J. et al 1972][research_roskamj_lanc_1972]
- [Roufaeil and Dawe 1982][research_roufaeil_dawe_1982]
- [Rouhi et al 2018][research_rouhi_ghayoor_2018]
- [Rowley 2008][research_rowley_2008]
- [Roy and Mukherjee 2026][research_roy_mukherjee_2026]
- [Roylance 1980][research_roylance_1980]
- [Ruhlin et al 1983][research_ruhlin_rauch_1983]
- [Rumble 1987][research_rumble_1987]
- [Runkel et al 2018][research_runkel_fasel_2018]
- [Runyan et al 1952][research_runyan_cunningham_1952]
- [Ruo et al 1985][research_ruo_malone_1985]
- [Ruscheweyh 1983][research_ruscheweyh_1983]
- [Rustenburg 1972][research_rustenburg_1972]
- [Rutkowski 1979][research_rutkowski_1979]
- [Ryder and Walker 1976][research_ryder_walker_1976]
- [S Alwan and Hussain 2026][research_salwan_hussain_2026]
- [S et al 2018][research_s_sinha_2018]
- [Sabater et al 2022][research_sabater_bekemeyer_2022]
- [Sabatini et al 2026][research_sabatini_coppotelli_2026]
- [Sabido et al 2017][research_sabido_bahamonde_2017]
- [Sabri et al 2022][research_sabri_elzaabalawy_2022]
- [Sachan and Padhi 2020][research_sachan_padhi_2020]
- [Sachs 1975][research_sachs_1975]
- [Sachs 1977][research_sachs_1977]
- [Sachs 1979][research_sachs_1979]
- [Sachs et al 1956][research_sachs_muvdi_1956]
- [Saddington et al 2016][research_saddington_thangamani_2016]
- [Saderla et al 2016][research_saderla_dhayalan_2016]
- [Saderla et al 2018][research_saderla_kim_2018]
- [Sadien et al 2020][research_sadien_roos_2020]
- [Sadoff, Melvin et al 1961][research_sadoffmelvin_mcfaddennormanm_1961]
- [Saetti 2025][research_saetti_2025]
- [Saetti 2025][research_saetti_2025_b]
- [Saetti and Rogers 2024][research_saetti_rogers_2024]
- [Saetti et al 2020][research_saetti_horn_2020]
- [Saheby et al 2026][research_saheby_jialu_2026]
- [Sahin et al 2026][research_sahin_yayla_2026]
- [Sahu et al 2000][research_sahu_heavey_2000]
- [Sahyoun et al 2026][research_sahyoun_boose_2026]
- [Sakthivel and Venkatesan 2017][research_sakthivel_venkatesan_2017]
- [Salagame et al 2025][research_salagame_pandya_2025]
- [Salahudden 2025][research_salahudden_2025]
- [Salahudden et al 2024][research_salahudden_agrawal_2024]
- [Salichon et al 1994][research_salichon_guy_1994]
- [Sally A Viken et al 2022][research_sallyaviken_craigahunter_2022]
- [Saltzman, Edwin J. et al 1994][research_saltzmanedwinj_hicksjohnw_1994]
- [Sammonds, Robert I. et al 1982][research_sammondsroberti_mcneillwaltere_1982]
- [Sampling schemes in sampled-data 1961][research_sampling_schemes_1961]
- [Samputh et al 2024][research_samputh_moey_2024]
- [Samukham et al 2017][research_samukham_raju_2017]
- [Samukham et al 2019][research_samukham_raju_2019]
- [Samukham et al 2020][research_samukham_vyasarayani_2020]
- [Sanders 1965][research_sanders_1965]
- [Sandhu et al 1991][research_sandhu_wolfe_1991]
- [Sang and Zhang 2022][research_sang_zhang_2022]
- [Santich 1985][research_santich_1985]
- [Saporito et al 2023][research_saporito_daronch_2023]
- [Saputra and Purabaya 2018][research_saputra_purabaya_2018]
- [Saraeian and Shirazi 2022][research_saraeian_shirazi_2022]
- [Sarao and Samanta 2022][research_sarao_samanta_2022]
- [Saric 1997][research_saric_1997]
- [Sarkar et al 2026][research_sarkar_huang_2026]
- [Sato 1973][research_sato_1973]
- [Sato et al 2017][research_sato_muraoka_2017]
- [Savelev and Neretin 2022][research_savelev_neretin_2022]
- [Savin and Hantrais-Gervois 2020][research_savin_hantraisgervois_2020]
- [Saviolo and Loianno 2023][research_saviolo_loianno_2023]
- [Savithri and Varadan 1990][research_savithri_varadan_1990]
- [Sawyer, J. W. 1976][research_sawyerjw_1976]
- [Schatz et al 2016][research_schatz_hermanutz_2016]
- [Schewe and Mai 2018][research_schewe_mai_2018]
- [Schieni et al 2024][research_schieni_modasiya_2024]
- [Schildkamp et al 2023][research_schildkamp_chang_2023]
- [Schiop 1979][research_schiop_1979]
- [Schloesser et al 2019][research_schloesser_soudakov_2019]
- [Schmeichel 1967][research_schmeichel_1967]
- [Schmidt 2016][research_schmidt_2016]
- [Schmidt 2016][research_schmidt_2016_b]
- [Schmidt et al 2020][research_schmidt_danowsky_2020]
- [Schmidt, David K. and Schierman, John D. 1990][research_schmidtdavidk_schiermanjohnd_1990]
- [Schneider 1976][research_schneider_1976]
- [Schpey 1980][research_schpey_1980]
- [Schreadley 1977][research_schreadley_1977]
- [Schroeder, Jeffery A. et al 2001][research_schroederjefferya_chungwilliamwy_2001]
- [Schueltke and Stumpf 2017][research_schueltke_stumpf_2017]
- [Schuet et al 2017][research_schuet_lombaerts_2017]
- [Schultz 1969][research_schultz_1969]
- [Schultz 1969][research_schultz_1969_b]
- [Schultz 1970][research_schultz_1970]
- [Schultz 1971][research_schultz_1971]
- [Schuster 1995][research_schuster_1995]
- [Schuster, David M. and Edwards, John W. 2004][research_schusterdavidm_edwardsjohnw_2004]
- [Schwanz 1972][research_schwanz_1972]
- [Schwerdt et al 2023][research_schwerdt_maroldt_2023]
- [Schäfer et al 2018][research_schafer_vidy_2018]
- [Schülein et al 2022][research_schulein_schnepf_2022]
- [Schütte et al 2018][research_schutte_huber_2018]
- [Sciuva 1992][research_sciuva_1992]
- [Scordamaglia et al 2025][research_scordamaglia_mattei_2025]
- [Scott et al 2016][research_scott_bartels_2016]
- [Sebghati and Shamaghdari 2020][research_sebghati_shamaghdari_2020]
- [Seckel and Graziani 1956][research_seckel_graziani_1956]
- [Seegmiller 1963][research_seegmiller_1963]
- [Segel 1952][research_segel_1952]
- [Seidel et al 1987][research_seidel_sandford_1987]
- [Seidel et al 1989][research_seidel_eckstrom_1989]
- [Seidel, D. A. et al 1985][research_seidelda_sandfordmc_1985]
- [Seitz et al 2019][research_seitz_hubner_2019]
- [sekhar et al 2024][research_sekhar_suresh_2024]
- [Sekimoto et al 2022][research_sekimoto_kato_2022]
- [Selberg, B. P. and Cronin, D. L. 1985][research_selbergbp_cronindl_1985]
- [Sellers, William L., III et al 1988][research_sellerswilliamliii_meyersjamesf_1988]
- [Sellers, William L., III et al 2004][research_sellerswilliamliii_meyersjamesf_2004]
- [Sen and Bhattacharya 2016][research_sen_bhattacharya_2016]
- [Sengupta and Ferris 1973][research_sengupta_ferris_1973]
- [Sengupta et al 2021][research_sengupta_roy_2021]
- [Seraj and Ganesan 2018][research_seraj_ganesan_2018]
- [Serakos 1992][research_serakos_1992]
- [Serani et al 2024][research_serani_diez_2024]
- [Seres et al 2023][research_seres_liu_2023]
- [Sergiev and Gusev 1979][research_sergiev_gusev_1979]
- [Serhat et al 2020][research_serhat_bediz_2020]
- [Seshadri and Krishnamurthy 2017][research_seshadri_krishnamurthy_2017]
- [Setiawarman and Sasongko 2026][research_setiawarman_sasongko_2026]
- [Seyoung 1990][research_seyoung_1990]
- [Sha et al 2022][research_sha_sun_2022]
- [Shafei et al 2024][research_shafei_faroughi_2024]
- [Shafer, M. F. 1980][research_shafermf_1980]
- [Shafer, M. F. et al 1983][research_shafermf_smithre_1983]
- [Shafer, M. F. et al 1984][research_shafermf_smithre_1984]
- [Shafer, Mary F. and Steinmetz, Paul 2001][research_shafermaryf_steinmetzpaul_2001]
- [Shafer, Mary F. and Steinmetz, Paul 2001][research_shafermaryf_steinmetzpaul_2001_b]
- [Shafighfard et al 2019][research_shafighfard_demir_2019]
- [Shah and Desai 1973][research_shah_desai_1973]
- [Shah and Mehta 2017][research_shah_mehta_2017]
- [Shakya and Padhee 2023][research_shakya_padhee_2023]
- [Shan and Bilgen 2022][research_shan_bilgen_2022]
- [Shan et al 2019][research_shan_tian_2019]
- [Shang and Xia 2024][research_shang_xia_2024]
- [Shankar and Malmuth 1982][research_shankar_malmuth_1982]
- [Shankar and Malmuth 1983][research_shankar_malmuth_1983]
- [Shankar et al 1981][research_shankar_malmuth_1981]
- [Shanley 1943][research_shanley_1943]
- [Shantz and Demeritte 1958][research_shantz_demeritte_1958]
- [Shao et al 2025][research_shao_sun_2025]
- [Shao et al 2026][research_shao_li_2026]
- [Sharif et al 2022][research_sharif_abbas_2022]
- [Sharifi et al 2025][research_sharifi_vincenti_2025]
- [Sharma et al 2022][research_sharma_agrawal_2022]
- [Sharma et al 2023][research_sharma_swain_2023]
- [Sharp and Wilson 1990][research_sharp_wilson_1990]
- [Sharqi and Cesnik 2023][research_sharqi_cesnik_2023]
- [Shawki and Mashhour 1974][research_shawki_mashhour_1974]
- [Shayak et al 2024][research_shayak_girdhar_2024]
- [Shcherban et al 2022][research_shcherban_sterlin_2022]
- [Shearwood et al 2020][research_shearwood_nabawy_2020]
- [Sheikh et al 2023][research_sheikh_lee_2023]
- [Sheikhi et al 2024][research_sheikhi_rafieianamagh_2024]
- [Sheikhi et al 2024][research_sheikhi_rafieianamagh_2024_b]
- [Sheldon 1967][research_sheldon_1967]
- [Shen and Chen 2022][research_shen_chen_2022]
- [Shen and Chen 2023][research_shen_chen_2023]
- [Shen and Chen 2024][research_shen_chen_2024]
- [Shen and Wen 2018][research_shen_wen_2018]
- [Shen et al 2015][research_shen_bai_2015]
- [Shen et al 2021][research_shen_huang_2021]
- [Shen et al 2022][research_shen_chang_2022]
- [Sheng and Zhao 2017][research_sheng_zhao_2017]
- [Shepheard 1965][research_shepheard_1965]
- [Shermer 1980][research_shermer_1980]
- [Sherrer et al 1981][research_sherrer_hertz_1981]
- [Sheshanarayana et al 2026][research_sheshanarayana_armstrong_2026]
- [Shi and Bezine 1988][research_shi_bezine_1988]
- [Shi and Wan 2015][research_shi_wan_2015]
- [Shi and Zhu 2024][research_shi_zhu_2024]
- [Shi et al 2018][research_shi_tan_2018]
- [Shi et al 2019][research_shi_lyu_2019]
- [Shi et al 2020][research_shi_liu_2020]
- [Shi et al 2021][research_shi_liu_2021]
- [Shi et al 2021][research_shi_mader_2021]
- [Shi et al 2022][research_shi_wang_2022]
- [Shi et al 2023][research_shi_lan_2023]
- [Shi et al 2023][research_shi_wang_2023]
- [Shi et al 2024][research_shi_liu_2024]
- [Shi et al 2024][research_shi_liu_2024_b]
- [Shi et al 2024][research_shi_liu_2024_c]
- [Shi et al 2025][research_shi_gao_2025]
- [Shi et al 2026][research_shi_gao_2026]
- [Shiau and Chang 1991][research_shiau_chang_1991]
- [Shibahata et al 1993][research_shibahata_shimada_1993]
- [Shieh and Chen 1998][research_shieh_chen_1998]
- [Shields and Cook 1971][research_shields_cook_1971]
- [Shimoda et al 2018][research_shimoda_nagano_2018]
- [Shinde et al 2021][research_shinde_ohol_2021]
- [Shiota and Ohmori 2015][research_shiota_ohmori_2015]
- [Shirk et al 1986][research_shirk_hertz_1986]
- [Shivam and Verma 2019][research_shivam_verma_2019]
- [Shladover 1995][research_shladover_1995]
- [Shmilovich and Princen 2026][research_shmilovich_princen_2026]
- [Shmilovich et al 2026][research_shmilovich_yadlin_2026]
- [Shneen 2026][research_shneen_2026]
- [Shoales and Fawaz 2004][research_shoales_fawaz_2004]
- [Shojae et al 2025][research_shojae_salehi_2025]
- [Shomber and Gertsen 1967][research_shomber_gertsen_1967]
- [Short 1995][research_short_1995]
- [Shrivastava and Mohite 2015][research_shrivastava_mohite_2015]
- [Shrivastava and Stengel 1989][research_shrivastava_stengel_1989]
- [Shrivastava et al 2020][research_shrivastava_sharma_2020]
- [Shrivastava et al 2020][research_shrivastava_tilala_2020]
- [Shrivastava, P. C. 1987][research_shrivastavapc_1987]
- [Shtessel 2001][research_shtessel_2001]
- [Shukla and Pradyumna 2021][research_shukla_pradyumna_2021]
- [Shukla et al 2025][research_shukla_benyamen_2025]
- [Shyprykevich, P. 1979][research_shyprykevichp_1979]
- [Si and Baier 2016][research_si_baier_2016]
- [Sibert 1937][research_sibert_1937]
- [Sibert 1943][research_sibert_1943]
- [Siddamma et al 2026][research_siddamma_seervi_2026]
- [Siddiqui et al 2016][research_siddiqui_elferik_2016]
- [Siem and Murray 1997][research_siem_murray_1997]
- [Silton and Fresconi 2015][research_silton_fresconi_2015]
- [Silton et al 2014][research_silton_fresconi_2014]
- [Silva, Walter A. and Bennett, Robert M. 1990][research_silvawaltera_bennettrobertm_1990]
- [Silva-Leon and Cioncolini 2020][research_silvaleon_cioncolini_2020]
- [Sim and Lee 2024][research_sim_lee_2024]
- [Simbuerger et al 2022][research_simbuerger_raveh_2022]
- [Simmonds 1971][research_simmonds_1971]
- [Simmons 2023][research_simmons_2023]
- [Simmons 2023][research_simmons_2023_b]
- [Simmons et al 2023][research_simmons_gresham_2023]
- [Simon et al 2017][research_simon_harkegard_2017]
- [Simos and Jenkinson 1988][research_simos_jenkinson_1988]
- [Simplício et al 2025][research_simplicio_acquatella_2025]
- [Simpson 1969][research_simpson_1969]
- [Simpson 1988][research_simpson_1988]
- [Sims, Robert et al 1989][research_simsrobert_mccrossonpaul_1989]
- [Sineglazov 2015][research_sineglazov_2015]
- [Singer 1989][research_singer_1989]
- [Singh and Dwivedi 2022][research_singh_dwivedi_2022]
- [Singh and Raisinghani 1993][research_singh_raisinghani_1993]
- [Singh et al 2016][research_singh_brown_2016]
- [Singh et al 2023][research_singh_parmar_2023]
- [Singh et al 2024][research_singh_yadav_2024]
- [Singhvi and Kapania 1994][research_singhvi_kapania_1994]
- [Singpurwalla and Wong 1980][research_singpurwalla_wong_1980]
- [Sinha et al 2021][research_sinha_klimmek_2021]
- [Siraskar 2021][research_siraskar_2021]
- [Sisson and Dogan 2026][research_sisson_dogan_2026]
- [Sisson et al 2022][research_sisson_karve_2022]
- [Sitz, Joel R. and Vernon, Todd H. 1990][research_sitzjoelr_vernontoddh_1990]
- [Sivanandi et al 2025][research_sivanandi_sanjay_2025]
- [Sizlo, T. R. et al 1979][research_sizlotr_bergra_1979]
- [Skarolek and J. Karabelas 2016][research_skarolek_jkarabelas_2016]
- [SKF divests fly-by-wire business 2016][research_skf_divests_2016]
- [Sleesongsom et al 2022][research_sleesongsom_kumar_2022]
- [Sleptsov and Andrianova 2021][research_sleptsov_andrianova_2021]
- [Sliwa, S. M. 1980][research_sliwasm_1980]
- [Smeltzer et al 1983][research_smeltzer_durston_1983]
- [Smetana 1973][research_smetana_1973]
- [Smith 1967][research_smith_1967]
- [Smith 1968][research_smith_1968]
- [Smith 1978][research_smith_1978]
- [Smith 1991][research_smith_1991]
- [Smith 1993][research_smith_1993]
- [Smith 2025][research_smith_2025]
- [Smith and Geddes 1979][research_smith_geddes_1979]
- [Smith and Meyer 1987][research_smith_meyer_1987]
- [Smith et al 1971][research_smith_hammer_1971]
- [Smith et al 1973][research_smith_lebacqz_1973]
- [Smith et al 2001][research_smith_komerath_2001]
- [Smith, J. W. 1979][research_smithjw_1979]
- [Smith, J. W. and Berry, D. T. 1975][research_smithjw_berrydt_1975]
- [Smith, Rogers E. and Schroeder, Kurt C. 1986][research_smithrogerse_schroederkurtc_1986]
- [Snyder 1950][research_snyder_1950]
- [Snyder et al 1992][research_snyder_schipper_1992]
- [Snyder et al 2019][research_snyder_zhao_2019]
- [Snyder et al 2022][research_snyder_zhao_2022]
- [Sobieczky 1984][research_sobieczky_1984]
- [Sodja et al 2021][research_sodja_werter_2021]
- [Sofi 2015][research_sofi_2015]
- [Sofiati Efi 2020][research_sofiatiefi_2020]
- [Software Productivity Consortium Herndon Va 1994][research_softwareproductivityconsortiumherndonva_1994]
- [Sohst et al 2022][research_sohst_lobodovale_2022]
- [Soleymani and Arani 2019][research_soleymani_arani_2019]
- [Solies 1994][research_solies_1994]
- [Solies 1994][research_solies_1994_b]
- [Soltani et al 2025][research_soltani_turner_2025]
- [Solís et al 2026][research_solis_leweke_2026]
- [Somani 2021][research_somani_2021]
- [Somashekar et al 1987][research_somashekar_prathap_1987]
- [Son et al 2015][research_son_sa_2015]
- [Son et al 2015][research_son_sa_2015_b]
- [Soneda et al 2022][research_soneda_tsushima_2022]
- [Song and Huang 2022][research_song_huang_2022]
- [Song and Mignolet 2018][research_song_mignolet_2018]
- [Song et al 2016][research_song_zhang_2016]
- [Song et al 2023][research_song_jia_2023]
- [Song et al 2026][research_song_lu_2026]
- [Soovere 1982][research_soovere_1982]
- [Soria 2006][research_soria_2006]
- [Sottorf, W. 1949][research_sottorfw_1949]
- [Soundararajan and B.T.N. 2022][research_soundararajan_btn_2022]
- [Soundararajan and Sridhar 2024][research_soundararajan_sridhar_2024]
- [Southwell 1698][research_southwell_1698]
- [Southwell 1698][research_southwell_1698_b]
- [Southwell 1843][research_southwell_1843]
- [Southwell and Prashad 1923][research_southwell_prashad_1923]
- [Southwell Cathedral 1885][research_southwell_cathedral_1885]
- [Southwell et al 1981][research_southwell_gunn_1981]
- [Space radiation effects on 1987][research_space_radiation_1987]
- [Spagnol et al 2019][research_spagnol_riche_2019]
- [Spencer and Walker 1975][research_spencer_walker_1975]
- [Spencer and Watson 1992][research_spencer_watson_1992]
- [Speyer 2003][research_speyer_2003]
- [Spiker 1964][research_spiker_1964]
- [Spillman and Ridgely 1995][research_spillman_ridgely_1995]
- [Sreenivasan 1987][research_sreenivasan_1987]
- [Srinathkumar 2015][research_srinathkumar_2015]
- [Srivastava 2019][research_srivastava_2019]
- [Stagliano and Mente 1979][research_stagliano_mente_1979]
- [Stainback 2001][research_stainback_2001]
- [Stalford 1979][research_stalford_1979]
- [Stanbrook 1954][research_stanbrook_1954]
- [Stanewsky and Little 1971][research_stanewsky_little_1971]
- [Stanford 2016][research_stanford_2016]
- [Stanford 2016][research_stanford_2016_b]
- [Stanford 2017][research_stanford_2017]
- [Stanford 2019][research_stanford_2019]
- [Stanford and Jutte 2017][research_stanford_jutte_2017]
- [Stanford et al 2016][research_stanford_jutte_2016]
- [Stanford, Bret K. and Jutte, Christine V. 2014][research_stanfordbretk_juttechristinev_2014]
- [Stanford, Bret K. et al 2015][research_stanfordbretk_wiesemancarold_2015]
- [Stange 1959][research_stange_1959]
- [Stanton and Crain 1980][research_stanton_crain_1980]
- [Stapelfeldt and Vahdati 2019][research_stapelfeldt_vahdati_2019]
- [Stark 1989][research_stark_1989]
- [Staroswiecki and Amani 2015][research_staroswiecki_amani_2015]
- [Stauffer, W. A. and James, A. M. 1978][research_staufferwa_jamesam_1978]
- [Stefanello and Gründling 2016][research_stefanello_grundling_2016]
- [Stefanovski 2022][research_stefanovski_2022]
- [Steffensen et al 2023][research_steffensen_steinert_2023]
- [Steger and Bailey 1980][research_steger_bailey_1980]
- [Stegmüller et al 2026][research_stegmuller_haybock_2026]
- [Steinberg and Page 1998][research_steinberg_page_1998]
- [Steinmetz, G. G. et al 1972][research_steinmetzgg_parrishrv_1972]
- [Stephan et al 2023][research_stephan_stumpf_2023]
- [Sternberg et al 1994][research_sternberg_traven_1994]
- [Stewart et al 1975][research_stewart_dominick_1975]
- [Stinton 1985][research_stinton_1985]
- [Stirling 1983][research_stirling_1983]
- [Stodieck et al 2015][research_stodieck_cooper_2015]
- [Stodieck et al 2017][research_stodieck_cooper_2017]
- [Stodieck et al 2018][research_stodieck_cooper_2018]
- [Stolarik 2007][research_stolarik_2007]
- [Stoll, F. and Koenig, D. G. 1983][research_stollf_koenigdg_1983]
- [Stollery 1992][research_stollery_1992]
- [Stottier 1995][research_stottier_1995]
- [Strand and Levinsky 1969][research_strand_levinsky_1969]
- [Streb 1973][research_streb_1973]
- [Streit et al 2015][research_streit_wedler_2015]
- [Strike and W. T. 1982][research_strike_wt_1982]
- [Striz 1991][research_striz_1991]
- [Stroud and Hartl 2023][research_stroud_hartl_2023]
- [Structural Aspects of Flexible 2000][research_structural_aspects_2000]
- [Structural Fundamentals 1955][research_structural_fundamentals_1955]
- [Study of advanced composite 1978][research_study_of_1978]
- [Sturlaugson and Sheppard 2015][research_sturlaugson_sheppard_2015]
- [Su et al 2016][research_su_swei_2016]
- [Su et al 2019][research_su_ma_2019]
- [Su et al 2025][research_su_mo_2025]
- [Su et al 2026][research_su_kong_2026]
- [Subramanian et al 2022][research_subramanian_abdelsalam_2022]
- [Sudhi et al 2023][research_sudhi_radespiel_2023]
- [Sugimoto 1992][research_sugimoto_1992]
- [Sugimoto and Saito 1968][research_sugimoto_saito_1968]
- [Sugimoto and Saito 1969][research_sugimoto_saito_1969]
- [Sugino et al 2019][research_sugino_harada_2019]
- [Sugumaran 2024][research_sugumaran_2024]
- [Suh, Peter M. et al 2014][research_suhpeterm_conyershowardj_2014]
- [Suh, Peter M. et al 2015][research_suhpeterm_conyershowardjason_2015]
- [Suikat, Reiner et al 1987][research_suikatreiner_donaldsonkent_1987]
- [Sulaeman et al 2017][research_sulaeman_abdullah_2017]
- [Sullivan 2002][research_sullivan_2002]
- [Sultan 2026][research_sultan_2026]
- [Sultan and Kattab 1995][research_sultan_kattab_1995]
- [Sun 2015][research_sun_2015]
- [Sun 2024][research_sun_2024]
- [Sun and Feng 2023][research_sun_feng_2023]
- [Sun and Gu 1995][research_sun_gu_1995]
- [Sun and van Kampen 2021][research_sun_vankampen_2021]
- [Sun and Yoon 1988][research_sun_yoon_1988]
- [Sun et al 2019][research_sun_devisser_2019]
- [Sun et al 2020][research_sun_miao_2020]
- [Sun et al 2020][research_sun_shi_2020]
- [Sun et al 2020][research_sun_wang_2020]
- [Sun et al 2022][research_sun_han_2022]
- [Sun et al 2024][research_sun_wang_2024]
- [Sun et al 2024][research_sun_xu_2024]
- [Sun et al 2025][research_sun_bahri_2025]
- [Sun et al 2025][research_sun_lin_2025]
- [Sun et al 2025][research_sun_luo_2025]
- [Sun et al 2026][research_sun_chen_2026]
- [Sun et al 2026][research_sun_zhang_2026]
- [Supercritical Wing Tested 1971][research_supercritical_wing_1971]
- [Suraj et al 2023][research_suraj_anilkumar_2023]
- [Surwase and Kumar 2025][research_surwase_kumar_2025]
- [Suryawanshi and Ghosh 2015][research_suryawanshi_ghosh_2015]
- [Suryendu et al 2017][research_suryendu_ghosh_2017]
- [Sushchenko and Bezkorovainyi 2023][research_sushchenko_bezkorovainyi_2023]
- [Sutherland 2018][research_sutherland_2018]
- [Svoboda et al 2023][research_svoboda_hengstermovric_2023]
- [Swab and Patel 2022][research_swab_patel_2022]
- [Swaim 1961][research_swaim_1961]
- [Swaim 1970][research_swaim_1970]
- [Swaim and Yen 1979][research_swaim_yen_1979]
- [Swain et al 2019][research_swain_adhikari_2019]
- [Sweat 1958][research_sweat_1958]
- [Switzky 1965][research_switzky_1965]
- [Switzky 1965][research_switzky_1965_b]
- [Syed et al 2022][research_syed_moshtaghzadeh_2022]
- [Synaszko et al 2015][research_synaszko_salacinski_2015]
- [Szalai, K. J. 1975][research_szalaikj_1975]
- [Szalai, K. J. 1976][research_szalaikj_1976]
- [Szalai, K. J. et al 1976][research_szalaikj_fellemanpg_1976]
- [Szalai, K. J. et al 1978][research_szalaikj_jarviscr_1978]
- [Szklarski and Głębocki 2025][research_szklarski_glebocki_2025]
- [Szmulewitz 2011][research_szmulewitz_2011]
- [Szmulewitz 2012][research_szmulewitz_2012]
- [Szollosi and Baranyi 2016][research_szollosi_baranyi_2016]
- [Szymanski et al 2025][research_szymanski_alstrom_2025]
- [Sóbester 2021][research_sobester_2021]
- [Tabassum and Bai 2022][research_tabassum_bai_2022]
- [Tahani et al 2017][research_tahani_masdari_2017]
- [Taherinezhad and Ramirez-Serrano 2023][research_taherinezhad_ramirezserrano_2023]
- [Tahir et al 2026][research_tahir_maqsood_2026]
- [Tahraoui 1994][research_tahraoui_1994]
- [Tai et al 2023][research_tai_wang_2023]
- [Tai et al 2023][research_tai_wang_2023_b]
- [Taimoor and Aijun 2019][research_taimoor_aijun_2019]
- [Taira 2014][research_taira_2014]
- [Takahashi et al 2016][research_takahashi_yokozeki_2016]
- [Takarics and Vanek 2019][research_takarics_vanek_2019]
- [Talbot and Gerald L. 1992][research_talbot_geraldl_1992]
- [Talreja and Phan 2019][research_talreja_phan_2019]
- [Tamaskani et al 2026][research_tamaskani_alfi_2026]
- [Tamboli 1956][research_tamboli_1956]
- [Tameh et al 2018][research_tameh_sawan_2018]
- [Tan 1988][research_tan_1988]
- [Tan et al 2021][research_tan_wang_2021]
- [Tan et al 2022][research_tan_zhang_2022]
- [Tang 1972][research_tang_1972]
- [Tang 1989][research_tang_1989]
- [Tang 1994][research_tang_1994]
- [Tang 2025][research_tang_2025]
- [Tang and Liu 2018][research_tang_liu_2018]
- [Tang et al 2015][research_tang_wu_2015]
- [Tang et al 2016][research_tang_wu_2016]
- [Tang et al 2017][research_tang_chen_2017]
- [Tang et al 2017][research_tang_luo_2017]
- [Tang et al 2017][research_tang_wu_2017]
- [Tang et al 2018][research_tang_chen_2018]
- [Tang et al 2018][research_tang_luo_2018]
- [Tang et al 2020][research_tang_chen_2020]
- [Tang et al 2020][research_tang_wang_2020]
- [Tang et al 2022][research_tang_zhang_2022]
- [Tang et al 2025][research_tang_gan_2025]
- [Tang et al 2025][research_tang_tang_2025]
- [Tangler 1979][research_tangler_1979]
- [Tantaroudas and Karachalios 2026][research_tantaroudas_karachalios_2026]
- [Tanveer and Ahmad 2023][research_tanveer_ahmad_2023]
- [Tanyer et al 2016][research_tanyer_tatlicioglu_2016]
- [Tao 2025][research_tao_2025]
- [Tao and Sun 2016][research_tao_sun_2016]
- [Tao et al 2016][research_tao_li_2016]
- [Targoff 1947][research_targoff_1947]
- [Targoff 1947][research_targoff_1947_b]
- [Tarnowski 2017][research_tarnowski_2017]
- [Tate 1992][research_tate_1992]
- [Taubert et al 2023][research_taubert_kay_2023]
- [Taufik and Qasem 2025][research_taufik_qasem_2025]
- [Tayebwa et al 2026][research_tayebwa_morshed_2026]
- [Taylor 1959][research_taylor_1959]
- [Taylor 2009][research_taylor_2009]
- [Taylor et al 2015][research_taylor_wilson_2015]
- [Teel 1999][research_teel_1999]
- [Teel 1999][research_teel_1999_b]
- [Teimourian and Altmeyer 2026][research_teimourian_altmeyer_2026]
- [Teixeira and Cesnik 2020][research_teixeira_cesnik_2020]
- [Teixeira et al 2018][research_teixeira_araujo_2018]
- [Telionis 1995][research_telionis_1995]
- [Telionis 2001][research_telionis_2001]
- [Teper and Stapleford 1966][research_teper_stapleford_1966]
- [Terekhov 2022][research_terekhov_2022]
- [Tewar et al 2015][research_tewar_myers_2015]
- [Thanusha and Sarkar 2016][research_thanusha_sarkar_2016]
- [Tharp and Zhang 1994][research_tharp_zhang_1994]
- [The Catholic religious poets 1995][research_the_catholic_1995]
- [The Impact of Flight 2024][research_the_impact_2024]
- [The viscoelastic behaviour of 1981][research_the_viscoelastic_1981]
- [The Voisin “Canard” Biplane 1911][research_the_voisin_1911]
- [Theerthamalai et al 2025][research_theerthamalai_mukesh_2025]
- [Theerthamalai et al 2026][research_theerthamalai_ramanan_2026]
- [Theis et al 2020][research_theis_pfifer_2020]
- [Theisen et al 1973][research_theisen_scruggs_1973]
- [Theodore et al 2020][research_theodore_malpica_2020]
- [Theodorsen 1959][research_theodorsen_1959]
- [Thermal damage effects and 1989][research_thermal_damage_1989]
- [Thermal expansion and swelling 1981][research_thermal_expansion_1981]
- [Thien and Kim 2018][research_thien_kim_2018]
- [Thomas and Dowell 2025][research_thomas_dowell_2025]
- [Thomas et al 1978][research_thomas_paulson_1978]
- [Thomas et al 2020][research_thomas_hallett_2020]
- [Thompson 1992][research_thompson_1992]
- [Thompson et al 2002][research_thompson_bannon_2002]
- [Thompson et al 2005][research_thompson_walls_2005]
- [Thu and Gavrilov 2017][research_thu_gavrilov_2017]
- [Tian 2016][research_tian_2016]
- [Tian 2020][research_tian_2020]
- [Tian 2021][research_tian_2021]
- [Tian and Tang 2025][research_tian_tang_2025]
- [Tian et al 2015][research_tian_li_2015]
- [Tian et al 2016][research_tian_yang_2016]
- [Tian et al 2017][research_tian_gao_2017]
- [Tian et al 2019][research_tian_li_2019]
- [Tian et al 2023][research_tian_jin_2023]
- [Tian et al 2025][research_tian_sun_2025]
- [Tian et al 2025][research_tian_zhao_2025]
- [Tian et al 2026][research_tian_li_2026]
- [Tian et al 2026][research_tian_wang_2026]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979_b]
- [Ting et al 2018][research_ting_chaparro_2018]
- [Ting et al 2023][research_ting_mesbahi_2023]
- [Ting et al 2026][research_ting_berg_2026]
- [Ting, Eric et al 2014][research_tingeric_lebofskysonia_2014]
- [Ting, Eric et al 2014][research_tingeric_nguyennhan_2014]
- [Ting, Eric et al 2015][research_tingeric_daotung_2015]
- [Tingting et al 2018][research_tingting_aijun_2018]
- [Tipàn et al 2020][research_tipan_theodoulis_2020]
- [Tischler, Mark B. et al 1991][research_tischlermarkb_fletcherjayw_1991]
- [To and Ewins 1995][research_to_ewins_1995]
- [Toader 1987][research_toader_1987]
- [Toan 2026][research_toan_2026]
- [Toffol 2024][research_toffol_2024]
- [Toffol and Ricci 2023][research_toffol_ricci_2023]
- [Tohidi et al 2016][research_tohidi_khakisedigh_2016]
- [Tokunaga et al 2015][research_tokunaga_masui_2015]
- [Toledano and Murakami 1987][research_toledano_murakami_1987]
- [Toloei and Ghaderi 2026][research_toloei_ghaderi_2026]
- [Tomas et al 2026][research_tomas_zaini_2026]
- [Tomlinson 1973][research_tomlinson_1973]
- [Tona 1962][research_tona_1962]
- [Tong et al 2025][research_tong_du_2025]
- [Toribio 2018][research_toribio_2018]
- [Tormalm et al 2018][research_tormalm_leroy_2018]
- [Torregrosa et al 2022][research_torregrosa_gil_2022]
- [Torsional stiffness and fatigue 1994][research_torsional_stiffness_1994]
- [Torsional stiffness of plastic 1972][research_torsional_stiffness_1972]
- [Townsend et al 2018][research_townsend_picelli_2018]
- [Trabocco 1980][research_trabocco_1980]
- [Tracking control of a 1993][research_tracking_control_1993]
- [Tran 1994][research_tran_1994]
- [Tran and Nguyen 2022][research_tran_nguyen_2022]
- [Tran et al 2017][research_tran_sakamoto_2017]
- [Transfer of Bending Moment 1960][research_transfer_of_1960]
- [Traub 2019][research_traub_2019]
- [Traven and Whitley 1995][research_traven_whitley_1995]
- [Tribuno et al 1976][research_tribuno_klein_1976]
- [Trindade Nascimento and Cunha 2019][research_trindadenascimento_cunha_2019]
- [Triplett 1972][research_triplett_1972]
- [Triplett 1980][research_triplett_1980]
- [Triplett et al 1971][research_triplett_burkhart_1971]
- [Triplett et al 1973][research_triplett_kappus_1973]
- [Trippensee, Gary A. and Lux, David P. 1987][research_trippenseegarya_luxdavidp_1987]
- [Trippensee, Gary A. and Lux, David P. 1988][research_trippenseegarya_luxdavidp_1988]
- [Tritschler and O’Connor 2016][research_tritschler_oconnor_2016]
- [Truong et al 2016][research_truong_rakotomamonjy_2016]
- [Tsai and Malak 2024][research_tsai_malak_2024]
- [Tsatsas et al 2022][research_tsatsas_pontillo_2022]
- [Tsiakas et al 2024][research_tsiakas_trompoukis_2024]
- [Tsoutsinos 1994][research_tsoutsinos_1994]
- [Tsubakino and Saito 2020][research_tsubakino_saito_2020]
- [Tsunematsu and Donadon 2019][research_tsunematsu_donadon_2019]
- [Tsushima and Su 2017][research_tsushima_su_2017]
- [Tsushima et al 2018][research_tsushima_arizono_2018]
- [Tsushima et al 2019][research_tsushima_arizono_2019]
- [Tsushima et al 2019][research_tsushima_yokozeki_2019]
- [Tsushima et al 2021][research_tsushima_saitoh_2021]
- [Tsushima et al 2021][research_tsushima_tamayama_2021]
- [Tsypkin and Fu 1993][research_tsypkin_fu_1993]
- [Tu 1992][research_tu_1992]
- [Tu 1994][research_tu_1994]
- [Tu 1994][research_tu_1994_b]
- [Tu et al 2026][research_tu_lu_2026]
- [Tu, Eugene L. 1991][research_tueugenel_1991]
- [Tu, Eugene L. 1992][research_tueugenel_1992]
- [Tu, Eugene L. 1992][research_tueugenel_1992_b]
- [Tu, Eugene L. and VanDalsem, William R. 1996][research_tueugenel_vandalsemwilliamr_1996]
- [Tudosie et al 2019][research_tudosie_dumitru_2019]
- [Tungikar and Rao 1994][research_tungikar_rao_1994]
- [Turner 1982][research_turner_1982]
- [Turner 1982][research_turner_1982_b]
- [Turner, M. J. and Hoy, J. M. 1976][research_turnermj_hoyjm_1976]
- [Twisdale and Kirsten 1984][research_twisdale_kirsten_1984]
- [UAV control with active 2023][research_uav_control_2023]
- [Ulry et al 1976][research_ulry_gehring_1976]
- [Unal 2021][research_unal_2021]
- [Unal 2021][research_unal_2021_b]
- [Underwood, Pamela J. et al 2003][research_underwoodpamelaj_owenslewisr_2003]
- [Unruh 1988][research_unruh_1988]
- [Ur Rehman et al 2025][research_urrehman_ekici_2025]
- [Urso et al 2026][research_urso_giunta_2026]
- [Ursu et al 2018][research_ursu_ionguta_2018]
- [Useller, James W. and Russey, Robert E. 1955][research_usellerjamesw_russeyroberte_1955]
- [Uzun 2024][research_uzun_2024]
- [Uzun 2024][research_uzun_2024_b]
- [Uzun and Oktay 2023][research_uzun_oktay_2023]
- [Uzun et al 2023][research_uzun_bilgic_2023]
- [Valsangkar et al 1982][research_valsangkar_britto_1982]
- [Van Baelen et al 2020][research_vanbaelen_ellerbroek_2020]
- [van Dam et al 1981][research_vandam_holmes_1981]
- [Van Den Berg et al 1975][research_vandenberg_elsenaar_1975]
- [van den Brandt and de Visser 2018][research_vandenbrandt_devisser_2018]
- [van den Kieboom and Elham 2017][research_vandenkieboom_elham_2017]
- [Van Dommelen 1995][research_vandommelen_1995]
- [van Dooren and Bisagni 2024][research_vandooren_bisagni_2024]
- [Van Doren 1955][research_vandoren_1955]
- [Van Gaasbeek 1980][research_vangaasbeek_1980]
- [Van Graas and Braasch 1991][research_vangraas_braasch_1991]
- [Van Graas et al 1994][research_vangraas_diggle_1994]
- [van Leeuwen 1960][research_vanleeuwen_1960]
- [Van Tuyl 1988][research_vantuyl_1988]
- [van Waarde 2022][research_vanwaarde_2022]
- [Vance et al 1974][research_vance_brown_1974]
- [Vansteenwyk, Brett and Ly, Uy-Loi 1992][research_vansteenwykbrett_lyuyloi_1992]
- [Varun and Dwivedi 2022][research_varun_dwivedi_2022]
- [Varun et al 2022][research_varun_mondal_2022]
- [Vaughan 1948][research_vaughan_1948]
- [Vedeneev 2020][research_vedeneev_2020]
- [Vehicle Sensor Steering System 2026][research_vehicle_sensor_2026]
- [Veley et al 2008][research_veley_khot_2008]
- [Velkova 2017][research_velkova_2017]
- [Venkataraman and Seiler 2019][research_venkataraman_seiler_2019]
- [Vepa and Kwon 2021][research_vepa_kwon_2021]
- [Verhaegen and Żbikowski 2017][research_verhaegen_zbikowski_2017]
- [Verma 1981][research_verma_1981]
- [Verma et al 2024][research_verma_cidmontoya_2024]
- [Verma et al 2025][research_verma_cidmontoya_2025]
- [Vermiglio 2017][research_vermiglio_2017]
- [Verri et al 2025][research_verri_desilvabussamra_2025]
- [Vertonghen et al 2026][research_vertonghen_irisarri_2026]
- [Vescovini and Dozio 2016][research_vescovini_dozio_2016]
- [Viglietti et al 2019][research_viglietti_zappino_2019]
- [Vile et al 2020][research_vile_alwi_2020]
- [Vilela and Donadon 2025][research_vilela_donadon_2025]
- [Villarroel and Rodrigues 2016][research_villarroel_rodrigues_2016]
- [Vinje and Miller 1973][research_vinje_miller_1973]
- [Viola et al 2020][research_viola_oziablo_2020]
- [Viswanath and Mukund 1995][research_viswanath_mukund_1995]
- [Viswanathan and Charkey 1986][research_viswanathan_charkey_1986]
- [Viswanathan and Charkey 1988][research_viswanathan_charkey_1988]
- [Vitushkin V.V. 2025][research_vitushkinvv_2025]
- [Vlahostergios et al 2018][research_vlahostergios_komnos_2018]
- [Vollo and Brassaw 1956][research_vollo_brassaw_1956]
- [Volpe et al 2026][research_volpe_salcuni_2026]
- [Voracek and Clarke 1994][research_voracek_clarke_1994]
- [Voracek, David F. and Clarke, Robert 1991][research_voracekdavidf_clarkerobert_1991]
- [Vorum 1984][research_vorum_1984]
- [Voting software for fault-tolerant 1993][research_voting_software_1993]
- [Voulgaris 1994][research_voulgaris_1994]
- [Vrchota et al 2019][research_vrchota_prachar_2019]
- [Vukelich et al 1988][research_vukelich_stoy_1988]
- [Vukelich et al 1988][research_vukelich_stoy_1988_b]
- [Vukobratović and Stojić 1985][research_vukobratovic_stojic_1985]
- [Vuong and Kim 2021][research_vuong_kim_2021]
- [Wada et al 2020][research_wada_tamayama_2020]
- [Wadia et al 2019][research_wadia_niedermeier_2019]
- [Wagg 2022][research_wagg_2022]
- [Waggoner, E. G. and Bates, B. L. 1989][research_waggonereg_batesbl_1989]
- [Waggoner, E. G. et al 1986][research_waggonereg_jennettla_1986]
- [Wahler et al 2025][research_wahler_ma_2025]
- [Waitman and Marcos 2019][research_waitman_marcos_2019]
- [Waitman and Marcos 2020][research_waitman_marcos_2020]
- [Wakimoto et al 2021][research_wakimoto_chiba_2021]
- [Walchli, Lawrence A. 1994][research_walchlilawrencea_1994]
- [Walker and Claudio 2024][research_walker_claudio_2024]
- [Walker and Hall 1968][research_walker_hall_1968]
- [Walker and Kaufman 1977][research_walker_kaufman_1977]
- [Walker, S. A. 1976][research_walkersa_1976]
- [Walker, T. H. et al 1997][research_walkerth_minguetpj_1997]
- [Walsh, Kevin R. 1993][research_walshkevinr_1993]
- [Walsh, Michael J. et al 1988][research_walshmichaelj_sellerswilliamliii_1988]
- [Wan 1974][research_wan_1974]
- [Wang 2019][research_wang_2019]
- [Wang 2021][research_wang_2021]
- [Wang 2024][research_wang_2024]
- [Wang 2024][research_wang_2024_b]
- [Wang 2025][research_wang_2025]
- [Wang 2025][research_wang_2025_b]
- [Wang 2026][research_wang_2026]
- [Wang and Chen 2022][research_wang_chen_2022]
- [Wang and Chen 2024][research_wang_chen_2024]
- [Wang and Fei 2016][research_wang_fei_2016]
- [Wang and Guo 2015][research_wang_guo_2015]
- [Wang and Li 2025][research_wang_li_2025_c]
- [Wang and Qing 2016][research_wang_qing_2016]
- [Wang and Rogers 1991][research_wang_rogers_1991]
- [Wang and Song 2025][research_wang_song_2025]
- [Wang and Thevendran 1993][research_wang_thevendran_1993]
- [Wang and Xia 2022][research_wang_xia_2022]
- [Wang and Xu 2018][research_wang_xu_2018]
- [Wang and Zhou 2026][research_wang_zhou_2026]
- [Wang et al 1994][research_wang_wang_1994]
- [Wang et al 2015][research_wang_li_2015]
- [Wang et al 2015][research_wang_wang_2015]
- [Wang et al 2015][research_wang_wu_2015]
- [Wang et al 2016][research_wang_gao_2016]
- [Wang et al 2016][research_wang_liang_2016]
- [Wang et al 2016][research_wang_xu_2016]
- [Wang et al 2016][research_wang_zhu_2016]
- [Wang et al 2017][research_wang_chu_2017]
- [Wang et al 2017][research_wang_su_2017]
- [Wang et al 2018][research_wang_daronch_2018]
- [Wang et al 2018][research_wang_su_2018]
- [Wang et al 2018][research_wang_wynn_2018]
- [Wang et al 2019][research_wang_baker_2019]
- [Wang et al 2019][research_wang_kampen_2019]
- [Wang et al 2019][research_wang_qiu_2019]
- [Wang et al 2019][research_wang_sun_2019]
- [Wang et al 2019][research_wang_vankampen_2019]
- [Wang et al 2019][research_wang_vankampen_2019_b]
- [Wang et al 2020][research_wang_liu_2020]
- [Wang et al 2020][research_wang_zhang_2020]
- [Wang et al 2020][research_wang_zhu_2020]
- [Wang et al 2021][research_wang_chen_2021]
- [Wang et al 2021][research_wang_hu_2021]
- [Wang et al 2021][research_wang_lu_2021]
- [Wang et al 2021][research_wang_ma_2021]
- [Wang et al 2021][research_wang_mkhoyan_2021]
- [Wang et al 2021][research_wang_peeters_2021]
- [Wang et al 2021][research_wang_wan_2021]
- [Wang et al 2021][research_wang_wen_2021]
- [Wang et al 2021][research_wang_wu_2021]
- [Wang et al 2021][research_wang_xu_2021]
- [Wang et al 2021][research_wang_zhang_2021]
- [Wang et al 2022][research_wang_hou_2022]
- [Wang et al 2022][research_wang_tai_2022]
- [Wang et al 2022][research_wang_zhang_2022]
- [Wang et al 2022][research_wang_zhang_2022_b]
- [Wang et al 2022][research_wang_zhao_2022]
- [Wang et al 2022][research_wang_zhao_2022_b]
- [Wang et al 2022][research_wang_zheng_2022]
- [Wang et al 2023][research_wang_lu_2023]
- [Wang et al 2023][research_wang_wang_2023]
- [Wang et al 2024][research_wang_bai_2024]
- [Wang et al 2024][research_wang_liu_2024]
- [Wang et al 2024][research_wang_song_2024]
- [Wang et al 2024][research_wang_sun_2024]
- [Wang et al 2024][research_wang_sun_2024_b]
- [Wang et al 2024][research_wang_zhou_2024]
- [Wang et al 2025][research_wang_bhaduri_2025]
- [Wang et al 2025][research_wang_chen_2025]
- [Wang et al 2025][research_wang_feng_2025]
- [Wang et al 2025][research_wang_ji_2025]
- [Wang et al 2025][research_wang_li_2025]
- [Wang et al 2025][research_wang_li_2025_b]
- [Wang et al 2025][research_wang_liuxu_2025]
- [Wang et al 2025][research_wang_luo_2025]
- [Wang et al 2025][research_wang_luo_2025_b]
- [Wang et al 2025][research_wang_luo_2025_c]
- [Wang et al 2025][research_wang_mallor_2025]
- [Wang et al 2025][research_wang_mao_2025]
- [Wang et al 2025][research_wang_rao_2025]
- [Wang et al 2025][research_wang_sun_2025]
- [Wang et al 2025][research_wang_tian_2025]
- [Wang et al 2025][research_wang_wang_2025]
- [Wang et al 2025][research_wang_wang_2025_b]
- [Wang et al 2025][research_wang_zhang_2025]
- [Wang et al 2025][research_wang_zhang_2025_b]
- [Wang et al 2025][research_wang_zheng_2025]
- [Wang et al 2026][research_wang_hu_2026]
- [Wang et al 2026][research_wang_li_2026]
- [Wang et al 2026][research_wang_liu_2026]
- [Wang et al 2026][research_wang_wei_2026]
- [Wang et al 2026][research_wang_weng_2026]
- [Wang et al 2026][research_wang_wu_2026]
- [Wang et al 2026][research_wang_ye_2026]
- [Wang et al 2026][research_wang_yi_2026]
- [Wang et al 2026][research_wang_zhang_2026]
- [Wang, John T. 1996][research_wangjohnt_1996]
- [Wang, John T. et al 1996][research_wangjohnt_jegleydawnc_1996]
- [Wansaseub et al 2020][research_wansaseub_sleesongsom_2020]
- [Wansasueb et al 2023][research_wansasueb_panagant_2023]
- [Wardlaw et al 1975][research_wardlaw_andrewb_1975]
- [Warren 1998][research_warren_1998]
- [Washington et al 1968][research_washington_pettis_1968]
- [Wasson and Mehus 1967][research_wasson_mehus_1967]
- [Watson, Clifford 2010][research_watsonclifford_2010]
- [Watson, Clifford C. 2011][research_watsoncliffordc_2011]
- [Wauters 2021][research_wauters_2021]
- [Wauters 2022][research_wauters_2022]
- [Weatherill and Zartarian 1958][research_weatherill_zartarian_1958]
- [Webb and Rogers 2021][research_webb_rogers_2021]
- [Webb, Lannie D. et al 1988][research_webblannied_mccainwilliame_1988]
- [Weed et al 1983][research_weed_carlson_1983]
- [Wegener et al 1993][research_wegener_dhooghe_1993]
- [Wei 2019][research_wei_2019]
- [Wei 2022][research_wei_2022]
- [Wei and Du 2019][research_wei_du_2019]
- [Wei and Freris 2024][research_wei_freris_2024]
- [Wei et al 2017][research_wei_chen_2017]
- [Wei et al 2019][research_wei_zhan_2019]
- [Wei et al 2020][research_wei_xu_2020]
- [Wei et al 2024][research_wei_ke_2024]
- [Wei et al 2024][research_wei_meng_2024]
- [Wei et al 2025][research_wei_cui_2025]
- [Weidemann and Leondes 1979][research_weidemann_leondes_1979]
- [Weihs and Katz 1986][research_weihs_katz_1986]
- [Weinert and Meyer 1984][research_weinert_meyer_1984]
- [Weiser et al 2020][research_weiser_ossmann_2020]
- [Weissel 1997][research_weissel_1997]
- [Weissenberger 1969][research_weissenberger_1969]
- [Weisshaar 1977][research_weisshaar_1977]
- [Weisshaar 1978][research_weisshaar_1978]
- [Weisshaar 1979][research_weisshaar_1979]
- [Weisshaar 1980][research_weisshaar_1980]
- [Weisshaar 1981][research_weisshaar_1981]
- [Weisshaar 1985][research_weisshaar_1985]
- [Weisshaar and Ryan 1986][research_weisshaar_ryan_1986]
- [Weisshaar and Zeiler 1983][research_weisshaar_zeiler_1983]
- [Weisshaar, T. A. 1983][research_weisshaarta_1983]
- [Weisshaar, T. A. and Ehlers, S. M. 1990][research_weisshaarta_ehlerssm_1990]
- [Weisshaar, T. A. and Zeiler, T. A. 1982][research_weisshaarta_zeilerta_1982]
- [Weisshaar, Terrence A. and Ehlers, Steven M. 1992][research_weisshaarterrencea_ehlersstevenm_1992]
- [Well and Berger 1982][research_well_berger_1982]
- [Welle 2000][research_welle_2000]
- [Wells 2002][research_wells_2002]
- [Wen et al 2023][research_wen_song_2023]
- [Werdes 1953][research_werdes_1953]
- [Werter and De Breuker 2016][research_werter_debreuker_2016]
- [Westbrook 1975][research_westbrook_1975]
- [Westin et al 2023][research_westin_balthazar_2023]
- [Westphal and Balfe 1961][research_westphal_balfe_1961]
- [Wheatcroft et al 2025][research_wheatcroft_groh_2025]
- [Wheatcroft et al 2025][research_wheatcroft_mahadik_2025]
- [Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]
- [Whitbeck et al 1982][research_whitbeck_smith_1982]
- [White 2004][research_white_2004]
- [White and Hartl 2025][research_white_hartl_2025]
- [White et al 1961][research_white_richardp_1961]
- [White et al 2005][research_white_geubelle_2005]
- [White et al 2017][research_white_mongru_2017]
- [White et al 2021][research_white_padfield_2021]
- [White, Edward V. et al 2015][research_whiteedwardv_kapaniarakeshk_2015]
- [White, J. F., III and Bendiksen, O. O. 1986][research_whitejfiii_bendiksenoo_1986]
- [Whitehead, R. S. et al 1992][research_whiteheadrs_foremancr_1992]
- [Whitlow, Woodrow, Jr. et al 1991][research_whitlowwoodrowjr_bennettrobertm_1991]
- [Whitworth 1987][research_whitworth_1987]
- [Whoric 1973][research_whoric_1973]
- [Whoric 1977][research_whoric_1977]
- [Wickens and Dixon 2002][research_wickens_dixon_2002]
- [Wickman 1953][research_wickman_1953]
- [Wie and Byun 1989][research_wie_byun_1989]
- [Wiese et al 2015][research_wiese_blom_2015]
- [Wiggenraad, J. F. M. and Bauld, N. R., Jr. 1993][research_wiggenraadjfm_bauldnrjr_1993]
- [Wilcox 1963][research_wilcox_1963]
- [Wildermuth et al 1974][research_wildermuth_rothammer_1974]
- [Wildermuth et al 1974][research_wildermuth_rothammer_1974_b]
- [Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]
- [Williams 1952][research_williams_1952]
- [Williams 1980][research_williams_1980]
- [Williams 2002][research_williams_2002]
- [Williamson 2022][research_williamson_2022]
- [Willsky 1984][research_willsky_1984]
- [Willsky and Verghese 1984][research_willsky_verghese_1984]
- [Willsky and Verghese 1985][research_willsky_verghese_1985]
- [Wilps et al 1983][research_wilps_collatz_1983]
- [Wilson 2026][research_wilson_2026]
- [Wilson and Riccardi 2022][research_wilson_riccardi_2022]
- [Wilson et al 1993][research_wilson_riley_1993]
- [Wilson et al 2024][research_wilson_champneys_2024]
- [Wilson, David J. et al 1994][research_wilsondavidj_citurskevind_1994]
- [Wing Buffeting Control at 2018][research_wing_buffeting_2018]
- [Wing et al 2025][research_wing_wing_2025]
- [Winny 1950][research_winny_1950]
- [Wise et al 1999][research_wise_sedwick_1999]
- [Withers 1981][research_withers_1981]
- [Witte et al 2003][research_witte_monson_2003]
- [Wittlin 1988][research_wittlin_1988]
- [Wolfe 1967][research_wolfe_1967]
- [Wollner 1972][research_wollner_1972]
- [Wong et al 1981][research_wong_cox_1981]
- [Wood and Livingston 1971][research_wood_livingston_1971]
- [Wood et al 2019][research_wood_araujoestrada_2019]
- [Wood, R. M. and Miller, D. S. 1985][research_woodrm_millerds_1985]
- [Woodcock, R. J. and George, F. L. 1976][research_woodcockrj_georgefl_1976]
- [Woodrow Whitlow, Jr. and Emily N. Todd 1999][research_woodrowwhitlowjr_emilyntodd_1999]
- [Woods et al 1990][research_woods_gilbert_1990]
- [Woods et al 2015][research_woods_dayyani_2015]
- [Woods, Jessica A. et al 1989][research_woodsjessicaa_gilbertmichaelg_1989]
- [Wooldridge 1960][research_wooldridge_1960]
- [Wrestler and Clifton G. 1965][research_wrestler_cliftong_1965]
- [Wright 1945][research_wright_1945]
- [Wu 1976][research_wu_1976]
- [Wu and Chiu 1992][research_wu_chiu_1992]
- [Wu and Deng 2015][research_wu_deng_2015]
- [Wu and Livne 2016][research_wu_livne_2016]
- [Wu and Livne 2017][research_wu_livne_2017]
- [Wu and Squires 1995][research_wu_squires_1995]
- [Wu and Tong 2017][research_wu_tong_2017]
- [Wu and Xu 2023][research_wu_xu_2023]
- [Wu et al 2015][research_wu_gunnion_2015]
- [Wu et al 2017][research_wu_chen_2017]
- [Wu et al 2017][research_wu_xiao_2017]
- [Wu et al 2019][research_wu_li_2019]
- [Wu et al 2020][research_wu_chen_2020]
- [Wu et al 2021][research_wu_sun_2021]
- [Wu et al 2021][research_wu_zhang_2021]
- [Wu et al 2022][research_wu_wilson_2022]
- [Wu et al 2022][research_wu_zuo_2022]
- [Wu et al 2023][research_wu_sun_2023]
- [Wu et al 2024][research_wu_wang_2024]
- [Wu et al 2024][research_wu_ye_2024]
- [Wu et al 2025][research_wu_fu_2025]
- [Wu et al 2025][research_wu_wang_2025]
- [Wunderlich 2015][research_wunderlich_2015]
- [Wunderlich and Dähne 2017][research_wunderlich_dahne_2017_b]
- [Wunderlich et al 2017][research_wunderlich_dahne_2017]
- [Wunderlich et al 2021][research_wunderlich_dahne_2021]
- [Wunderlich et al 2022][research_wunderlich_dahne_2022]
- [x 2022][research_x_2022]
- [X-29 Research Aircraft 1991][research_x_29_research_1991]
- [Xia and Chen 2015][research_xia_chen_2015]
- [Xia et al 2016][research_xia_li_2016]
- [Xia et al 2023][research_xia_huang_2023]
- [Xia et al 2026][research_xia_li_2026]
- [Xiang and Liu 2024][research_xiang_liu_2024]
- [Xiang and Wang 2023][research_xiang_wang_2023]
- [Xiang et al 2018][research_xiang_liu_2018]
- [Xiao and Dong 2019][research_xiao_dong_2019]
- [Xiao and Harrison 2021][research_xiao_harrison_2021]
- [Xiao and Liu 2018][research_xiao_liu_2018]
- [Xiao et al 2021][research_xiao_sattarov_2021]
- [Xiao et al 2026][research_xiao_chen_2026]
- [Xie and Zhao 2016][research_xie_zhao_2016]
- [Xie et al 2016][research_xie_liu_2016]
- [Xie et al 2017][research_xie_meng_2017]
- [Xie et al 2021][research_xie_li_2021]
- [Xie et al 2025][research_xie_zhang_2025]
- [Xijuan et al 2016][research_xijuan_qiang_2016]
- [Xinbing et al 2020][research_xinbing_wen_2020]
- [Xiong et al 2025][research_xiong_xu_2025]
- [Xiong et al 2026][research_xiong_tang_2026]
- [Xu 2025][research_xu_2025]
- [Xu 2026][research_xu_2026]
- [Xu and Feng 2025][research_xu_feng_2025]
- [Xu and Wang 2016][research_xu_wang_2016]
- [Xu and Xia 2016][research_xu_xia_2016]
- [Xu and Zha 2021][research_xu_zha_2021]
- [Xu et al 2015][research_xu_fan_2015]
- [Xu et al 2015][research_xu_gao_2015]
- [Xu et al 2015][research_xu_guo_2015]
- [Xu et al 2018][research_xu_zhang_2018]
- [Xu et al 2019][research_xu_saleh_2019]
- [Xu et al 2019][research_xu_tan_2019]
- [Xu et al 2020][research_xu_zhang_2020]
- [Xu et al 2021][research_xu_oliveira_2021]
- [Xu et al 2024][research_xu_tian_2024]
- [Xu et al 2025][research_xu_zhang_2025]
- [Xu et al 2026][research_xu_liu_2026]
- [Xu et al 2026][research_xu_yang_2026]
- [Xu et al 2026][research_xu_zhang_2026]
- [Xu et al 2026][research_xu_zhang_2026_b]
- [Xue and Yao 2020][research_xue_yao_2020]
- [Xue et al 2019][research_xue_ye_2019]
- [Xue et al 2021][research_xue_yunsong_2021]
- [Xue et al 2026][research_xue_zhao_2026]
- [Yagil et al 2018][research_yagil_raveh_2018]
- [Yahagi 1971][research_yahagi_1971]
- [Yalvaç et al 1991][research_yalvac_yats_1991]
- [Yamakoshi and Komatsuzaki 2022][research_yamakoshi_komatsuzaki_2022]
- [Yamamoto 1992][research_yamamoto_1992]
- [Yamane 1992][research_yamane_1992]
- [Yamane and Friedmann 1993][research_yamane_friedmann_1993]
- [Yamasaki and Gotoh 1971][research_yamasaki_gotoh_1971]
- [Yan et al 2019][research_yan_li_2019]
- [Yan et al 2023][research_yan_zhang_2023]
- [Yan et al 2025][research_yan_han_2025]
- [Yan et al 2026][research_yan_zhu_2026]
- [Yang 2024][research_yang_2024]
- [Yang and Gao 2020][research_yang_gao_2020]
- [Yang and Liu 1976][research_yang_liu_1976]
- [Yang and Manning 1994][research_yang_manning_1994]
- [Yang and Wan 1978][research_yang_wan_1978]
- [Yang and Zhao 1989][research_yang_zhao_1989]
- [Yang and Zhao 1992][research_yang_zhao_1992]
- [Yang et al 1980][research_yang_guruswamy_1980]
- [Yang et al 1981][research_yang_striz_1981]
- [Yang et al 1994][research_yang_batra_1994]
- [Yang et al 2015][research_yang_lee_2015]
- [Yang et al 2015][research_yang_yue_2015]
- [Yang et al 2016][research_yang_yue_2016]
- [Yang et al 2016][research_yang_zhao_2016]
- [Yang et al 2017][research_yang_huang_2017]
- [Yang et al 2018][research_yang_guan_2018]
- [Yang et al 2019][research_yang_huang_2019]
- [Yang et al 2019][research_yang_xie_2019]
- [Yang et al 2019][research_yang_yang_2019]
- [Yang et al 2022][research_yang_mao_2022]
- [Yang et al 2022][research_yang_wang_2022]
- [Yang et al 2023][research_yang_li_2023]
- [Yang et al 2023][research_yang_zhang_2023]
- [Yang et al 2024][research_yang_fu_2024]
- [Yang et al 2024][research_yang_xiao_2024]
- [Yang et al 2024][research_yang_xu_2024]
- [Yang et al 2025][research_yang_wang_2025]
- [Yang et al 2025][research_yang_wu_2025]
- [Yang et al 2026][research_yang_guo_2026]
- [Yang et al 2026][research_yang_li_2026]
- [Yang et al 2026][research_yang_tang_2026]
- [Yang et al 2026][research_yang_wang_2026]
- [Yang et al 2026][research_yang_yu_2026]
- [Yang et al 2026][research_yang_zhang_2026]
- [Yao 2018][research_yao_2018]
- [Yao et al 2020][research_yao_liu_2020]
- [Yao et al 2021][research_yao_ma_2021]
- [Yaseen and Bayart 2018][research_yaseen_bayart_2018]
- [Yasue 2020][research_yasue_2020]
- [Yates 1966][research_yates_1966]
- [Yates et al 1982][research_yates_wynne_1982]
- [Yates et al 1983][research_yates_wynne_1983]
- [Yates, E. C., Jr. et al 1981][research_yatesecjr_wynneec_1981]
- [Yates, E. Carson, Jr. and Chu, Li-Chuan 1987][research_yatesecarsonjr_chulichuan_1987]
- [Ye et al 2015][research_ye_chen_2015]
- [Ye et al 2024][research_ye_yang_2024]
- [Ye et al 2025][research_ye_wang_2025]
- [Yeo and Kreshock 2020][research_yeo_kreshock_2020]
- [Yeo and Potsdam 2016][research_yeo_potsdam_2016]
- [Yeo et al 2015][research_yeo_atkins_2015]
- [Yepifanov 2020][research_yepifanov_2020]
- [Yi 2020][research_yi_2020]
- [Yi et al 2017][research_yi_an_2017]
- [Yildiz, Yidiray et al 2011][research_yildizyidiray_kolmanovskyilyav_2011]
- [Yildiz, Yildiray and Kolmanovsky, Ilya V. 2010][research_yildizyildiray_kolmanovskyilyav_2010]
- [Yin and Wang 2017][research_yin_wang_2017]
- [Yin et al 2019][research_yin_chu_2019]
- [Yin et al 2025][research_yin_huang_2025]
- [Yin et al 2025][research_yin_ni_2025]
- [Ying et al 2021][research_ying_liqiang_2021]
- [Yingsong et al 2015][research_yingsong_zhichun_2015]
- [Yip, L. P. and Paulson, J. W., Jr. 1977][research_yiplp_paulsonjwjr_1977]
- [Yonekura and Suzuki 2021][research_yonekura_suzuki_2021]
- [Yoo 2017][research_yoo_2017]
- [Yoo et al 2021][research_yoo_jang_2021]
- [Yoo et al 2023][research_yoo_jeong_2023]
- [York and Williams 1995][research_york_williams_1995]
- [You 2020][research_you_2020]
- [You et al 2019][research_you_yasaee_2019]
- [You et al 2020][research_you_kim_2020]
- [You et al 2022][research_you_lei_2022]
- [Younes and Hickey 2020][research_younes_hickey_2020]
- [Young et al 2018][research_young_garg_2018]
- [Yu 1987][research_yu_1987]
- [Yu 2018][research_yu_2018]
- [Yu and Yu 2026][research_yu_yu_2026]
- [Yu et al 2016][research_yu_zhang_2016]
- [Yu et al 2017][research_yu_fang_2017]
- [Yu et al 2017][research_yu_wang_2017]
- [Yu et al 2018][research_yu_lyu_2018]
- [Yu et al 2020][research_yu_bai_2020]
- [Yu et al 2022][research_yu_wang_2022]
- [Yu et al 2023][research_yu_zhang_2023]
- [Yu et al 2024][research_yu_zhou_2024]
- [Yu et al 2025][research_yu_he_2025]
- [Yu et al 2026][research_yu_zhang_2026]
- [Yuan and Li 2019][research_yuan_li_2019]
- [Yuan and Zhou 2024][research_yuan_zhou_2024]
- [Yuan et al 2018][research_yuan_huo_2018]
- [Yuan et al 2022][research_yuan_thomson_2022]
- [Yuan et al 2024][research_yuan_wang_2024]
- [Yuan, F. G. and Reeder, James R. 2001][research_yuanfg_reederjamesr_2001]
- [Yue and Zhao 2020][research_yue_zhao_2020]
- [Yue et al 2017][research_yue_zhang_2017]
- [Yue et al 2021][research_yue_khodaei_2021]
- [Yuksek and Inalhan 2020][research_yuksek_inalhan_2020]
- [Yunker et al 2024][research_yunker_lake_2024]
- [Yurtsever et al 2026][research_yurtsever_sahin_2026]
- [Yutuk et al 2021][research_yutuk_tikenogullari_2021]
- [Yuvarajan 2001][research_yuvarajan_2001]
- [Zadvornyak and Martynovich 1983][research_zadvornyak_martynovich_1983]
- [Zakharov et al 2015][research_zakharov_zattoni_2015]
- [Zang et al 2023][research_zang_wang_2023]
- [Zanoni et al 2022][research_zanoni_gerosa_2022]
- [Zapata et al 2025][research_zapata_perezgonzalez_2025]
- [Zarei et al 2019][research_zarei_arvan_2019]
- [Zau Beu 2020][research_zaubeu_2020]
- [Zauner and Sandham 2020][research_zauner_sandham_2020]
- [Zauner et al 2023][research_zauner_moise_2023]
- [Zaw and Baranovski 2026][research_zaw_baranovski_2026]
- [Zaytseva et al 2021][research_zaytseva_kuznetsov_2021]
- [Zeiler, Thomas A. 1998][research_zeilerthomasa_1998]
- [Zeleke et al 2023][research_zeleke_asfaw_2023]
- [Zelenkov 2018][research_zelenkov_2018]
- [Zha et al 2026][research_zha_qiao_2026]
- [Zhai et al 2020][research_zhai_li_2020]
- [Zhan et al 2025][research_zhan_li_2025]
- [Zhang 2023][research_zhang_2023]
- [Zhang and He 2026][research_zhang_he_2026]
- [Zhang and Ran 2023][research_zhang_ran_2023]
- [Zhang and Rizzi 2017][research_zhang_rizzi_2017]
- [Zhang and Wang 2019][research_zhang_wang_2019]
- [Zhang and Zhao 2023][research_zhang_zhao_2023]
- [Zhang and Zhao 2023][research_zhang_zhao_2023_b]
- [Zhang and Zhu 2015][research_zhang_zhu_2015]
- [Zhang et al 2015][research_zhang_fang_2015]
- [Zhang et al 2015][research_zhang_marzocca_2015]
- [Zhang et al 2015][research_zhang_wang_2015]
- [Zhang et al 2015][research_zhang_zhou_2015]
- [Zhang et al 2017][research_zhang_huang_2017]
- [Zhang et al 2017][research_zhang_li_2017]
- [Zhang et al 2017][research_zhang_zhang_2017]
- [Zhang et al 2018][research_zhang_chen_2018]
- [Zhang et al 2018][research_zhang_devisser_2018]
- [Zhang et al 2018][research_zhang_han_2018]
- [Zhang et al 2018][research_zhang_liu_2018]
- [Zhang et al 2018][research_zhang_yang_2018]
- [Zhang et al 2019][research_zhang_devisser_2019]
- [Zhang et al 2019][research_zhang_liu_2019]
- [Zhang et al 2019][research_zhang_zhao_2019]
- [Zhang et al 2020][research_zhang_chen_2020]
- [Zhang et al 2020][research_zhang_han_2020]
- [Zhang et al 2020][research_zhang_sun_2020]
- [Zhang et al 2020][research_zhang_wang_2020]
- [Zhang et al 2021][research_zhang_guo_2021]
- [Zhang et al 2021][research_zhang_li_2021]
- [Zhang et al 2021][research_zhang_shaw_2021]
- [Zhang et al 2021][research_zhang_xie_2021]
- [Zhang et al 2021][research_zhang_yang_2021]
- [Zhang et al 2022][research_zhang_deng_2022]
- [Zhang et al 2022][research_zhang_ji_2022]
- [Zhang et al 2022][research_zhang_shao_2022]
- [Zhang et al 2022][research_zhang_wang_2022]
- [Zhang et al 2022][research_zhang_wang_2022_b]
- [Zhang et al 2023][research_zhang_li_2023]
- [Zhang et al 2023][research_zhang_zhang_2023]
- [Zhang et al 2024][research_zhang_qiu_2024]
- [Zhang et al 2024][research_zhang_zhou_2024]
- [Zhang et al 2024][research_zhang_zhou_2024_b]
- [Zhang et al 2025][research_zhang_bai_2025]
- [Zhang et al 2025][research_zhang_li_2025]
- [Zhang et al 2025][research_zhang_song_2025]
- [Zhang et al 2025][research_zhang_yang_2025]
- [Zhang et al 2026][research_zhang_dai_2026]
- [Zhang et al 2026][research_zhang_deng_2026]
- [Zhang et al 2026][research_zhang_li_2026]
- [Zhang et al 2026][research_zhang_wang_2026]
- [Zhang et al 2026][research_zhang_yu_2026]
- [Zhang et al 2026][research_zhang_zhao_2026]
- [Zhao and Cheng 2019][research_zhao_cheng_2019]
- [Zhao and Li 2019][research_zhao_li_2019]
- [Zhao and Zhou 2024][research_zhao_zhou_2024]
- [Zhao et al 2015][research_zhao_li_2015]
- [Zhao et al 2015][research_zhao_luximon_2015]
- [Zhao et al 2016][research_zhao_yue_2016]
- [Zhao et al 2016][research_zhao_zhang_2016]
- [Zhao et al 2019][research_zhao_sun_2019]
- [Zhao et al 2021][research_zhao_wu_2021]
- [Zhao et al 2021][research_zhao_zhao_2021]
- [Zhao et al 2022][research_zhao_ji_2022]
- [Zhao et al 2022][research_zhao_wang_2022]
- [Zhao et al 2023][research_zhao_xing_2023]
- [Zhao et al 2023][research_zhao_yang_2023]
- [Zhao et al 2024][research_zhao_lu_2024]
- [Zhao et al 2024][research_zhao_xu_2024]
- [Zhao et al 2024][research_zhao_zhang_2024]
- [Zhao et al 2024][research_zhao_zhao_2024]
- [Zhao et al 2025][research_zhao_wang_2025]
- [Zhao et al 2026][research_zhao_li_2026]
- [Zhao et al 2026][research_zhao_liu_2026]
- [Zhao et al 2026][research_zhao_liu_2026_b]
- [Zheng and Shao 2025][research_zheng_shao_2025]
- [Zheng et al 2016][research_zheng_chen_2016]
- [Zheng et al 2024][research_zheng_pontillo_2024]
- [Zheng et al 2026][research_zheng_dai_2026]
- [Zheng et al 2026][research_zheng_wang_2026]
- [Zhijie et al 2025][research_zhijie_taiyu_2025]
- [Zhiqiang et al 2016][research_zhiqiang_xiaozhe_2016]
- [Zhirabok et al 2024][research_zhirabok_filaretov_2024]
- [Zhong et al 2017][research_zhong_goldenfeld_2017]
- [Zhong et al 2025][research_zhong_ying_2025]
- [Zhong et al 2026][research_zhong_wang_2026]
- [Zhou and Huang 2021][research_zhou_huang_2021]
- [Zhou and Huang 2021][research_zhou_huang_2021_b]
- [Zhou et al 1989][research_zhou_ye_1989]
- [Zhou et al 2017][research_zhou_chen_2017]
- [Zhou et al 2017][research_zhou_wang_2017]
- [Zhou et al 2018][research_zhou_yu_2018]
- [Zhou et al 2019][research_zhou_dowell_2019]
- [Zhou et al 2019][research_zhou_ruan_2019]
- [Zhou et al 2019][research_zhou_ruan_2019_b]
- [Zhou et al 2019][research_zhou_xu_2019]
- [Zhou et al 2022][research_zhou_wang_2022]
- [Zhou et al 2022][research_zhou_yang_2022]
- [Zhou et al 2024][research_zhou_cheng_2024]
- [Zhou et al 2025][research_zhou_liu_2025]
- [Zhou et al 2025][research_zhou_raze_2025]
- [Zhou et al 2025][research_zhou_shen_2025]
- [Zhou et al 2026][research_zhou_gong_2026]
- [Zhou et al 2026][research_zhou_guan_2026]
- [Zhou et al 2026][research_zhou_li_2026]
- [Zhou et al 2026][research_zhou_peng_2026]
- [Zhu and Duan 2015][research_zhu_duan_2015]
- [Zhu et al 2017][research_zhu_du_2017]
- [Zhu et al 2017][research_zhu_wang_2017]
- [Zhu et al 2019][research_zhu_li_2019]
- [Zhu et al 2022][research_zhu_shi_2022]
- [Zhu et al 2023][research_zhu_sun_2023]
- [Zhu et al 2024][research_zhu_zhang_2024]
- [Zhu et al 2025][research_zhu_zhou_2025]
- [Zhuang et al 2021][research_zhuang_yang_2021]
- [Zia et al 2022][research_zia_liu_2022]
- [Ziakos et al 2025][research_ziakos_kilimtzidis_2025]
- [Ziegler 1963][research_ziegler_1963]
- [Ziegler 2017][research_ziegler_2017]
- [Zinn et al 2005][research_zinn_lubarsky_2005]
- [Zipperer et al 1975][research_zipperer_jenney_1975]
- [Zipperer et al 1975][research_zipperer_jenney_1975_b]
- [Zohar and Er-El 1988][research_zohar_erel_1988]
- [Zong et al 2021][research_zong_sun_2021]
- [Zou et al 2017][research_zou_yao_2017]
- [Zou et al 2021][research_zou_mu_2021]
- [Zou et al 2022][research_zou_huang_2022]
- [Zou et al 2024][research_zou_huang_2024]
- [Zou et al 2025][research_zou_huang_2025]
- [Zou et al 2025][research_zou_huang_2025_b]
- [Zoutendijk and Mitici 2021][research_zoutendijk_mitici_2021]
- [Zuhri 2025][research_zuhri_2025]
- [Zuo et al 2015][research_zuo_chen_2015]
- [Zuo et al 2016][research_zuo_min_2016]
- [Zvonarev and Leont’ev 2025][research_zvonarev_leontev_2025]
- [Çabuk 2026][research_cabuk_2026]
- [Özdemir 2021][research_ozdemir_2021]
- [Özkan 2020][research_ozkan_2020]
- [Şahin and Yaman 2018][research_sahin_yaman_2018]
- [Şahin and Yaman 2018][research_sahin_yaman_2018_b]
- [Şumnu 2026][research_sumnu_2026]
- [Ženíšek 1973][research_zenisek_1973]
- [Žitňan 1989][research_zitnan_1989]
- [Калиновский 2016][research_anon_2016]
- [Комаров and Зінченко 2019][research___2019]
- [Лейбов and Гуревич 2021][research___2021]
- [Морозов 2015][research_anon_2015]

[research_011_intelligent_1994]: https://doi.org/10.1016/0967-0661(94)90363-8
[research_017_preview_1994]: https://doi.org/10.1016/0967-0661(94)90369-7
[research_024_automated_1994]: https://doi.org/10.1016/0967-0661(94)90376-x
[research_025_adaptive_1994]: https://doi.org/10.1016/0967-0661(94)90377-8
[research_044_finite_1994]: https://doi.org/10.1016/0967-0661(94)90059-0
[research_053_fuzzy_1994]: https://doi.org/10.1016/0967-0661(94)90635-1
[research_056_neural_1994]: https://doi.org/10.1016/0967-0661(94)90638-6
[research_057_h_1994]: https://doi.org/10.1016/0967-0661(94)90072-8
[research_116_on_1972]: https://doi.org/10.1016/0022-4898(72)90055-9
[research_130_sampled_data_1994]: https://doi.org/10.1016/0967-0661(94)90919-9
[research_185_a_1994]: https://doi.org/10.1016/0967-0661(94)90974-1
[research_196_pointing_1994]: https://doi.org/10.1016/0967-0661(94)90548-7
[research_214_application_1994]: https://doi.org/10.1016/0967-0661(94)91003-0
[research_44408_nondestructive_1994]: https://doi.org/10.1016/0963-8695(94)90687-4
[research_44416_aln_1994]: https://doi.org/10.1016/0963-8695(94)90686-6
[research___2019]: https://doi.org/10.20535/0203-3771372019186954
[research___2021]: https://doi.org/10.25791/aviakosmos.9.2021.1237
[research___2025]: https://doi.org/10.71097/ijsat.v16.i1.2685
[research_a_comparative_2022]: https://doi.org/10.59121/kjmlar2209330001
[research_a_feasibility_2019]: https://doi.org/10.21152/1750-9548.13.4.339
[research_a_general_1989]: https://doi.org/10.1016/0010-4361(89)90396-0
[research_a_generalization_2020]: https://doi.org/10.5829/ije.2020.33.11b.28
[research_a_hybrid_1995]: https://doi.org/10.1016/0967-0661(95)90150-7
[research_a_model_2021]: https://doi.org/10.47176/jafm.14.03.31488
[research_a_robust_2021]: https://doi.org/10.25236/ajbm.2021.030104
[research_a_spreadsheet_2018]: https://doi.org/10.20508/ijrer.v8i4.8480.g7550
[research_a_study_1973]: https://ntrs.nasa.gov/citations/19730009309
[research_a_study_1990]: https://doi.org/10.1016/0010-4361(90)90277-4
[research_aamir_abbasi_2026]: https://doi.org/10.2514/1.c038958
[research_abate_mote_2024]: https://doi.org/10.1109/tcst.2023.3340624
[research_abbas_morgenthal_2016]: https://doi.org/10.1016/j.probengmech.2015.12.007
[research_abbott_alinity_2019]: https://doi.org/10.1097/01.bmsas.0000576756.38556.68
[research_abbottjm_millerba_1974]: https://ntrs.nasa.gov/citations/19740008382
[research_abc_2023]: https://doi.org/10.61653/joast.v70i01.2018.347
[research_abdalla_mansor_2020]: https://doi.org/10.37200/ijpr/v24i2/pr200541
[research_abdelhady_1994]: https://doi.org/10.1080/00423119308969500
[research_abdulhuq_beebim_2015]: https://doi.org/10.70729/ijser15423
[research_abdulkaiyoom_yildirim_2025]: https://doi.org/10.2514/1.c037365
[research_abdullah_akbar_2019]: https://doi.org/10.1016/j.compstruct.2019.111414
[research_abdulrashid_syedmohddardin_2025]: https://doi.org/10.58247/jdset-2025-0802-20
[research_abed_2000]: https://doi.org/10.21236/ada381735
[research_abed_alhamadani_2024]: https://doi.org/10.18280/mmep.111029
[research_abele_ruger_1973]: https://doi.org/10.21236/ad0766892
[research_abele_sanlorenzo_1975]: https://doi.org/10.21236/ada013139
[research_abeli_ruhlincl_1966]: https://ntrs.nasa.gov/citations/19660021918
[research_abelkis_1967]: https://doi.org/10.21236/ad0818959
[research_aberdeentestcentermd_2009]: https://doi.org/10.21236/ada509433
[research_abichandani_rosenberg_1952]: https://doi.org/10.2514/8.2362
[research_abouheaf_gueaieb_2020]: https://doi.org/10.1049/iet-cta.2018.6163
[research_aboukebeh_gilpita_2025]: https://doi.org/10.3390/aerospace12010034
[research_abunawas_qawasmeh_2026]: https://doi.org/10.2514/1.c038542
[research_accelerated_development_1979]: https://ntrs.nasa.gov/citations/19790025046
[research_ackerman_xargay_2017]: https://doi.org/10.2514/1.g001730
[research_ackermann_haase_2023]: https://doi.org/10.1016/j.addma.2023.103585
[research_ackermann_isermann_1973]: https://doi.org/10.1115/1.3426752
[research_acoustic_emission_1981]: https://doi.org/10.1016/0010-4361(81)90431-6
[research_acoustic_emissions_1989]: https://doi.org/10.1016/0010-4361(89)90260-7
[research_acquatella_chu_2020]: https://doi.org/10.1016/j.ifacol.2020.12.1598
[research_acquatellab_vanekeren_2017]: https://doi.org/10.1016/j.ifacol.2017.08.1265
[research_active_fault_tolerant_2025]: https://doi.org/10.3901/jme.2025.16.321
[research_adams_1973]: https://doi.org/10.21236/ad0771962
[research_adams_1977]: https://doi.org/10.1115/1.3450686
[research_adams_hatch_1971]: https://doi.org/10.2514/3.59103
[research_adan_sheinman_1988]: https://doi.org/10.1016/0045-7949(88)90296-9
[research_adeyemi_bull_2026]: https://doi.org/10.2514/1.c037836
[research_adler_martins_2023]: https://doi.org/10.2514/1.c037096
[research_adneyps_hornwj_1984]: https://ntrs.nasa.gov/citations/19840024307
[research_advanced_control_2023]: https://doi.org/10.48047/nq.2022.20.10.nq551258
[research_aero_structural_2018]: https://doi.org/10.20474/jater-4.1.5
[research_aerodynamic_performance_2025]: https://doi.org/10.18178/ijmerr.14.1.48-58
[research_aggarwal_cranch_1967]: https://doi.org/10.1115/1.3607687
[research_aghababa_2018]: https://doi.org/10.1002/acs.2897
[research_agrawal_gupta_2022]: https://doi.org/10.1016/j.finel.2021.103649
[research_agrell_elmeland_1985]: https://doi.org/10.2514/3.45185
[research_aguilaribanez_2016]: https://doi.org/10.1002/rnc.3601
[research_agwa_2019]: https://doi.org/10.1007/s11071-019-04990-y
[research_aharrahralphc_2007]: https://ntrs.nasa.gov/citations/20100011189
[research_ahmadi_farsadi_2024]: https://doi.org/10.1016/j.ast.2023.108849
[research_ahmadi_farsadi_2024_b]: https://doi.org/10.1016/j.ast.2024.109023
[research_ahmadian_alitalebi_2025]: https://doi.org/10.1002/acs.3957
[research_ahmadian_khosravi_2020]: https://doi.org/10.1002/acs.3154
[research_ahmadidastgerdi_asadi_2022]: https://doi.org/10.55212/ijaa.1033224
[research_ahmed_chen_2021]: https://doi.org/10.1108/aeat-11-2020-0277
[research_ahmed_elbanna_2025]: https://doi.org/10.1142/s2301385026500366
[research_aidala_1985]: https://doi.org/10.21236/ada171075
[research_aircraft_and_2016]: https://doi.org/10.1109/mcs.2015.2512078
[research_airforceflighttestcenteredwardsafbca_1970]: https://doi.org/10.21236/ada529707
[research_airforceflighttestcenteredwardsafbca_1974]: https://doi.org/10.21236/ada011561
[research_airforceflighttestcenteredwardsafbca_1974_b]: https://doi.org/10.21236/ada011562
[research_airforceflighttestcenteredwardsafbca_2002]: https://doi.org/10.21236/ada402888
[research_airforceflighttestcenteredwardsafbca_2002_b]: https://doi.org/10.21236/ada403258
[research_airforcetestpilotschooledwardsafbca_1967]: https://doi.org/10.21236/ada320224
[research_airforcetestpilotschooledwardsafbca_1967_b]: https://doi.org/10.21236/ada320209
[research_airforcetestpilotschooledwardsafbca_1969]: https://doi.org/10.21236/ada319985
[research_airforcetestpilotschooledwardsafbca_1981]: https://doi.org/10.21236/ada320347
[research_airforcetestpilotschooledwardsafbca_1988]: https://doi.org/10.21236/ada319979
[research_airforcetestpilotschooledwardsafbca_1988_b]: https://doi.org/10.21236/ada319974
[research_airforcetestpilotschooledwardsafbca_1988_c]: https://doi.org/10.21236/ada319984
[research_airforcetestpilotschooledwardsafbca_1988_d]: https://doi.org/10.21236/ada319975
[research_airforcetestpilotschooledwardsafbca_1988_e]: https://doi.org/10.21236/ada319973
[research_airforcetestpilotschooledwardsafbca_1989]: https://doi.org/10.21236/ada319980
[research_airforcetestpilotschooledwardsafbca_1990]: https://doi.org/10.21236/ada319976
[research_airforcetestpilotschooledwardsafbca_1990_b]: https://doi.org/10.21236/ada319978
[research_airforcetestpilotschooledwardsafbca_1990_c]: https://doi.org/10.21236/ada320058
[research_airforcetestpilotschooledwardsafbca_1990_d]: https://doi.org/10.21236/ada320062
[research_airforcetestpilotschooledwardsafbca_1990_e]: https://doi.org/10.21236/ada319977
[research_airforcetestpilotschooledwardsafbca_1991]: https://doi.org/10.21236/ada319981
[research_airforcetestpilotschooledwardsafbca_1991_b]: https://doi.org/10.21236/ada319972
[research_airforcetestpilotschooledwardsafbca_1992]: https://doi.org/10.21236/ada319982
[research_airforcetestpilotschooledwardsafbca_1993]: https://doi.org/10.21236/ada320063
[research_ajaj_parancheerivilakkathil_2021]: https://doi.org/10.1016/j.paerosci.2020.100682
[research_ajel_humaidi_2021]: https://doi.org/10.3390/act10070162
[research_akbar_curielsosa_2016]: https://doi.org/10.1016/j.compstruct.2016.06.010
[research_akbari_galeani_2025]: https://doi.org/10.1109/lcsys.2025.3633369
[research_aker_alukonis_1976]: https://doi.org/10.21236/ada028416
[research_akinwale_datta_2025]: https://doi.org/10.2514/1.c037994
[research_aksoz_gunay_2024]: https://doi.org/10.3390/en17061380
[research_alag_kaufman_1975]: https://doi.org/10.2514/3.59859
[research_alam_hromcik_2015]: https://doi.org/10.1016/j.ast.2014.12.020
[research_alam_lee_2026]: https://doi.org/10.1016/j.compstruct.2026.120344
[research_albachten_1956]: https://doi.org/10.21236/ad0116273
[research_alberts_2011]: https://doi.org/10.21236/ada631225
[research_alberts_2014]: https://doi.org/10.21236/ada605273
[research_alberts_conley_2015]: https://doi.org/10.21236/ada617821
[research_alcaina_cuenca_2019]: https://doi.org/10.1016/j.ins.2019.01.059
[research_aleisaac_ragab_2023]: https://doi.org/10.3390/s23125561
[research_alexander_1991]: https://doi.org/10.21236/ada240263
[research_alexander_griffin_1973]: https://doi.org/10.21236/ad0763725
[research_alexander_tzeng_1996]: https://doi.org/10.21236/ada306454
[research_alfred_celi_2017]: https://doi.org/10.4050/jahs.62.032012
[research_alhajahmad_mittelstedt_2021]: https://doi.org/10.1016/j.compstruct.2020.113271
[research_alhussein_haldar_2015]: https://doi.org/10.1002/stc.1764
[research_ali_chen_2026]: https://doi.org/10.1115/1.4071137
[research_alikhanikoupaei_2015]: https://doi.org/10.3920/qas2013.0297
[research_alim_rizianiza_2021]: https://doi.org/10.24176/simet.v11i2.5428
[research_alisyedfirasat_1997]: https://ntrs.nasa.gov/citations/19970026582
[research_alizadeh_ebrahimi_2020]: https://doi.org/10.1142/s0219455420500820
[research_aljaburi_feszty_2019]: https://doi.org/10.1016/j.cja.2019.05.009
[research_allen_bradley_1983]: https://doi.org/10.21236/ada134059
[research_allen_bradley_1984]: https://doi.org/10.21236/ada150802
[research_allisondenniso_dagenhartjray_1987]: https://ntrs.nasa.gov/citations/19890009895
[research_almadani_osman_2022]: https://doi.org/10.3390/en15103807
[research_almosnino_1985]: https://doi.org/10.2514/3.9057
[research_alsaidi_joe_2019]: https://doi.org/10.3390/aerospace6080090
[research_alsaidi_joe_2019_b]: https://doi.org/10.3390/aerospace6070079
[research_alshammari_2026]: https://doi.org/10.51219/jaimld/abdulmohsen-eid-alshammari/683
[research_altunkaya_ozkol_2025]: https://doi.org/10.2514/1.g008752
[research_alyanak_pendleton_2017]: https://doi.org/10.2514/1.c033040
[research_amin_hollweger_1983]: https://doi.org/10.2514/3.44924
[research_amini_mozaffaritazehkand_2022]: https://doi.org/10.1016/j.bspc.2021.103075
[research_amirahmadichomachar_kuppusamy_2022]: https://doi.org/10.1108/aeat-08-2021-0240
[research_an_anal_1974]: https://doi.org/10.1016/0148-9062(74)90690-1
[research_an_guo_2020]: https://doi.org/10.1007/s11071-020-05531-8
[research_an_khoo_2017]: https://doi.org/10.1016/j.compstruct.2017.07.042
[research_an_zhang_2026]: https://doi.org/10.1016/j.ast.2025.111209
[research_anderson_1960]: https://doi.org/10.21236/ad0314095
[research_anderson_1961]: https://doi.org/10.21236/ad0322137
[research_anderson_1968]: https://doi.org/10.21236/ad0675550
[research_anderson_1970]: https://doi.org/10.21236/ad0710590
[research_anderson_1985]: https://doi.org/10.2514/3.45218
[research_anderson_berger_1973]: https://doi.org/10.2514/3.60204
[research_anderson_hogle_1986]: https://doi.org/10.1016/0094-5765(86)90134-7
[research_anderson_toivanen_1970]: https://doi.org/10.21236/ad0706001
[research_andersonca_1976]: https://ntrs.nasa.gov/citations/19760024050
[research_ando_yashiro_1976]: https://doi.org/10.2514/3.48148
[research_andresperez_gonzalezjuarez_2016]: https://doi.org/10.1080/0305215x.2016.1165568
[research_ang_leo_2024]: https://doi.org/10.1016/j.ast.2023.108798
[research_ang_ng_2026]: https://doi.org/10.2514/1.j065873
[research_anggraeni_hidayat_2015]: https://doi.org/10.14323/ijuseng.2015.12
[research_anikin_animitsa_2015]: https://doi.org/10.1615/tsagiscij.2015014083
[research_annadata_endesfelder_2024]: https://doi.org/10.1088/2053-1591/ad8397
[research_announcement_european_1988]: https://doi.org/10.1016/0266-8920(88)90030-6
[research_anon_2015]: https://doi.org/10.18372/2073-4751.2.8948
[research_anon_2016]: https://doi.org/10.18698/2541-8009-2016-1-10
[research_anon_2016_b]: https://doi.org/10.15623/ijret.2016.0505096
[research_anoshkin_zuiko_2015]: https://doi.org/10.1016/j.compstruct.2014.10.001
[research_ansari_bajodah_2017]: https://doi.org/10.1108/aeat-06-2015-0149
[research_ansari_shaikh_2019]: https://doi.org/10.2139/ssrn.3367683
[research_ansari_zucco_2023]: https://doi.org/10.1016/j.compstruct.2023.116691
[research_ansellgs_loewyrg_1982]: https://ntrs.nasa.gov/citations/19830009326
[research_antonakis_2025]: https://doi.org/10.1016/j.ast.2025.110020
[research_antonakis_2025_b]: https://doi.org/10.1007/s13272-025-00815-4
[research_antonakis_biannic_2024]: https://doi.org/10.2514/1.c037707
[research_aouiti_assali_2019]: https://doi.org/10.1002/acs.3042
[research_application_analysis_2022]: https://doi.org/10.47939/et.v3i5(02).13
[research_application_of_2024]: https://doi.org/10.36652/0869-4931-2024-78-12-553-557
[research_application_status_2023]: https://doi.org/10.3901/jme.2023.19.001
[research_apu_hydraulic_actuator_subsystem_1975]: https://ntrs.nasa.gov/citations/19760019175
[research_arcidiacono_carta_1970]: https://doi.org/10.21236/ad0869823
[research_ardemamd_williamslj_1972]: https://ntrs.nasa.gov/citations/19720018366
[research_argha_su_2018]: https://doi.org/10.1002/rnc.4376
[research_argha_su_2019]: https://doi.org/10.1002/rnc.4727
[research_ariaratnam_1961]: https://doi.org/10.1093/qjmam/14.2.137
[research_arif_sasongko_2021]: https://doi.org/10.47355/avia.v3i1.39
[research_ariyarit_kanazaki_2017]: https://doi.org/10.3390/app7121318
[research_armanious_lind_2017]: https://doi.org/10.2514/1.g002799
[research_armstrong_1977]: https://doi.org/10.21236/adb029224
[research_armstrong_lindberg_2006]: https://doi.org/10.21236/ada463491
[research_arnault_dandois_2016]: https://doi.org/10.1016/j.compfluid.2016.06.006
[research_arnold_1942]: https://doi.org/10.2514/8.10949
[research_ascani_1974]: https://doi.org/10.21236/ada002850
[research_asgari_kouchakzadeh_2016]: https://doi.org/10.1016/j.compstruct.2016.02.015
[research_ashill_1970]: https://doi.org/10.1017/s0001925900005400
[research_ashkenas_1984]: https://doi.org/10.2514/3.44963
[research_ashkenasirvingl_klydedavidh_1989]: https://ntrs.nasa.gov/citations/19890011628
[research_ashton_1970]: https://doi.org/10.1177/002199837000400201
[research_ashworth_mckissick_1979]: https://doi.org/10.2514/3.58605
[research_aslam_chen_2018]: https://doi.org/10.1080/00207179.2018.1484172
[research_aston_williams_1994]: https://doi.org/10.1016/0263-8223(94)90050-7
[research_atmaca_devisser_2025]: https://doi.org/10.2514/1.g009147
[research_audoin_baste_1994]: https://doi.org/10.1115/1.2901446
[research_augustyn_ulriksen_2021]: https://doi.org/10.3390/en14185859
[research_auman_doyle_2008]: https://doi.org/10.21236/ada503576
[research_aung_shi_2017]: https://doi.org/10.1115/1.4037732
[research_autenrieb_2025]: https://doi.org/10.2514/1.g009203
[research_autonomous_flight_2018]: https://doi.org/10.1299/jsmecs.2018.56.1215
[research_awadallaalihajahmed_2024]: https://doi.org/10.47191/etj/v9i10.08
[research_awadallaalihajahmed_2024_b]: https://doi.org/10.47191/etj/v9i10.09
[research_axelson_1977]: https://doi.org/10.2514/3.58819
[research_axten_khamvilai_2024]: https://doi.org/10.1109/lcsys.2023.3346458
[research_ayaz_rasoolmemon_2024]: https://doi.org/10.1109/access.2024.3435961
[research_ayorinde_gibson_1993]: https://doi.org/10.1016/0961-9526(93)90077-w
[research_azadegan_beheshti_2017]: https://doi.org/10.1002/asjc.1435
[research_babu_khan_2026]: https://doi.org/10.1007/s42405-026-01260-1
[research_babuska_wiebe_2018]: https://doi.org/10.1016/j.compstruct.2018.01.036
[research_bach_jebari_2016]: https://doi.org/10.1007/s00158-016-1477-3
[research_bachman_1981]: https://doi.org/10.1002/j.2161-4296.1981.tb00769.x
[research_badaliance_dill_1981]: https://doi.org/10.21236/ada105034
[research_badallo_trias_2015]: https://doi.org/10.1016/j.compstruct.2015.07.025
[research_badhurshah_alvarez_2024]: https://doi.org/10.3390/app14135531
[research_badihi_nezhad_2026]: https://doi.org/10.2514/1.c038688
[research_baek_2021]: https://doi.org/10.34139/jscs.2021.11.2.1
[research_bagherzadeh_2026]: https://doi.org/10.3390/mca31030085
[research_bagherzadeh_mohammadkarimi_2025]: https://doi.org/10.3390/mca30020041
[research_bahamondejacome_elham_2017]: https://doi.org/10.2514/1.c034050
[research_bahr_mckay_2021]: https://doi.org/10.1017/aer.2021.114
[research_bai_2018]: https://doi.org/10.1049/joe.2018.0025
[research_bai_tang_2019]: https://doi.org/10.1088/1742-6596/1419/1/012026
[research_bai_xu_2022]: https://doi.org/10.9734/jerr/2022/v22i517537
[research_baier_1970]: https://doi.org/10.21236/ad0878050
[research_baileyrandalle_powersbruceg_1988]: https://ntrs.nasa.gov/citations/19880063393
[research_baileyre_knottslh_1990]: https://ntrs.nasa.gov/citations/19910005040
[research_baileyre_smithre_1981]: https://ntrs.nasa.gov/citations/19820026927
[research_bainum_ericsson_1992]: https://doi.org/10.21236/ada264192
[research_baker_galigher_1960]: https://doi.org/10.21236/ad0320438
[research_baker_jones_1985]: https://doi.org/10.1016/0263-8223(85)90018-2
[research_balaji_manickam_2024]: https://doi.org/10.1016/j.compstruct.2024.118199
[research_balakrishnan_2000]: https://doi.org/10.21236/ada377873
[research_balasubramanian_jayanarasimhan_2025]: https://doi.org/10.29294/ijase.12.1.2025.5007-5016
[research_balatti_haddadkhodaparast_2021]: https://doi.org/10.1016/j.ast.2021.106805
[research_balatti_khodaparast_2022]: https://doi.org/10.2139/ssrn.4258795
[research_baldan_guardone_2024]: https://doi.org/10.1016/j.ast.2024.109345
[research_baldereschi_maschke_1975]: https://doi.org/10.1016/0038-1098(75)90799-1
[research_ballesterclaret_coelho_2024]: https://doi.org/10.1016/j.compstruct.2024.118461
[research_balunov_solyaev_2023]: https://doi.org/10.34759/trd-2023-129-04
[research_bandyopadhyay_1989]: https://doi.org/10.1017/s0001924000016651
[research_bandyopadhyay_1991]: https://doi.org/10.2514/3.46077
[research_bandyopadhyay_2001]: https://doi.org/10.21236/ada398719
[research_banerjee_2019]: https://doi.org/10.2514/1.c034888
[research_banerjee_kotecha_2016]: https://doi.org/10.1016/j.conengprac.2016.05.006
[research_banks_1988]: https://doi.org/10.21236/ada204640
[research_banksdanielw_1988]: https://ntrs.nasa.gov/citations/19890063987
[research_bantscheff_breitsamter_2023]: https://doi.org/10.3390/aerospace10070581
[research_bao_li_2025]: https://doi.org/10.3390/machines13060525
[research_barabanov_ortega_2017]: https://doi.org/10.1002/acs.2851
[research_baranovski_mikhailovskiy_2020]: https://doi.org/10.1615/tsagiscij.2020036204
[research_barbini_balfe_1970]: https://doi.org/10.21236/ad0869906
[research_barbosa_bertolin_2022]: https://doi.org/10.2514/1.g006271
[research_bardo_2015]: https://doi.org/10.21236/ad1000337
[research_bargill_stengel_1986]: https://doi.org/10.2514/3.45276
[research_barrett_rembold_1983]: https://doi.org/10.2514/3.44841
[research_barshalom_1985]: https://doi.org/10.21236/ada159053
[research_barshalom_1989]: https://doi.org/10.21236/ada215486
[research_barshalom_1990]: https://doi.org/10.21236/ada219629
[research_bartels_stanford_2018]: https://doi.org/10.2514/1.c034675
[research_bartelsroberte_stanfordbretk_2019]: https://ntrs.nasa.gov/citations/20200002388
[research_bartoszewicz_adamiak_2018]: https://doi.org/10.1002/acs.2922
[research_bashir_longtinmartel_2021]: https://doi.org/10.3390/app11041664
[research_bashir_negahban_2024]: https://doi.org/10.3390/biomimetics9020109
[research_bassett_johnson_1966]: https://doi.org/10.1243/03093247v015398
[research_bastin_coron_2025]: https://doi.org/10.1016/j.automatica.2024.112048
[research_basuroy_bhasin_2019]: https://doi.org/10.1002/acs.3046
[research_bataineh_shawabkeh_2023]: https://doi.org/10.15866/irease.v16i6.24344
[research_batina_yang_1985]: https://doi.org/10.2514/3.45137
[research_batt_1974]: https://doi.org/10.2514/3.49284
[research_battaglia_riccio_2026]: https://doi.org/10.3390/act15080414
[research_battersonjamesg_omarathomasm_1989]: https://ntrs.nasa.gov/citations/19890006554
[research_bauchau_1981]: https://doi.org/10.1177/002199838101500205
[research_bauchau_1983]: https://doi.org/10.1177/002199838301700205
[research_baum_clark_1979]: https://doi.org/10.21236/ada066669
[research_bay_kara_2026]: https://doi.org/10.17798/bitlisfen.1847172
[research_bayless_voglewede_2020]: https://doi.org/10.1115/1.4046113
[research_baz_chen_1993]: https://doi.org/10.1016/0961-9526(93)90069-v
[research_bazhenov_lysenkova_2015]: https://doi.org/10.1615/tsagiscij.2015013712
[research_bearings_only_2022]: https://doi.org/10.23977/autml.2022.030301
[research_beatty_brooks_1977]: https://doi.org/10.21236/ada045951
[research_becker_1992]: https://doi.org/10.1016/0263-8223(92)90079-r
[research_beharie_pedro_2015]: https://doi.org/10.1017/s0001924000010587
[research_beitalmal_2025]: https://doi.org/10.47191/rajar/v11i4.11
[research_bellini_sorrentino_2018]: https://doi.org/10.1016/j.prostr.2018.06.027
[research_belmont_1983]: https://doi.org/10.21236/ada133274
[research_benaddy_labbadi_2022]: https://doi.org/10.1016/j.ifacol.2022.07.323
[research_benaouali_boutemedjet_2024]: https://doi.org/10.1108/aeat-11-2023-0310
[research_bendahmane_hamzacherif_2019]: https://doi.org/10.1080/15376494.2018.1553257
[research_bendiksen_friedmann_1982]: https://doi.org/10.1115/1.3227324
[research_bending_moment_1992]: https://doi.org/10.14359/2933
[research_bending_of_1991]: https://doi.org/10.1016/0010-4361(91)90115-w
[research_bending_theory_1987]: https://doi.org/10.1016/0010-4361(87)90512-x
[research_bengida_gurka_2022]: https://doi.org/10.1088/1748-3190/ac9bb5
[research_bennett_dansberry_1993]: https://doi.org/10.2514/3.46314
[research_bennettrm_farmermg_1977]: https://ntrs.nasa.gov/citations/19770060309
[research_bennettrobertm_batinajohnt_1988]: https://ntrs.nasa.gov/citations/19880010035
[research_benoit_1969]: https://doi.org/10.4267/2042/66916
[research_benoit_leroy_1960]: https://doi.org/10.1016/0006-2952(60)90056-3
[research_benyamen_chowdhury_2024]: https://doi.org/10.1115/1.4065804
[research_beppu_curtiss_1966]: https://doi.org/10.21236/ad0640945
[research_berezhnitskii_denisyuk_1985]: https://doi.org/10.1007/bf01150635
[research_berg_ting_2025]: https://doi.org/10.2514/1.g008589
[research_bergen_arnold_1940]: https://doi.org/10.2514/8.1231
[research_berger_blanken_2022]: https://doi.org/10.4050/jahs.67.032009
[research_berger_blanken_2022_b]: https://doi.org/10.4050/jahs.67.032008
[research_berger_tischler_2021]: https://doi.org/10.2514/1.g005768
[research_bergman_1948]: https://doi.org/10.21236/ada301214
[research_bergstedt_turner_1959]: https://doi.org/10.21236/ad0402171
[research_berman_gran_1974]: https://doi.org/10.2514/3.60358
[research_bernstein_2000]: https://doi.org/10.21236/ada382981
[research_bernstein_hollot_1989]: https://doi.org/10.1016/0167-6911(89)90067-4
[research_berry_powers_1982]: https://doi.org/10.2514/3.57395
[research_berrydt_1981]: https://ntrs.nasa.gov/citations/19810059723
[research_bertsimas_na_2025]: https://doi.org/10.1287/ijoo.2023.0007
[research_besch_liu_1973]: https://doi.org/10.21236/ad0757645
[research_besch_rood_1976]: https://doi.org/10.21236/ada027188
[research_bessa_puig_2020]: https://doi.org/10.1016/j.jfranklin.2020.02.002
[research_bessadet_2023]: https://doi.org/10.15199/48.2023.06.14
[research_bessadi_saussie_2016]: https://doi.org/10.1016/j.ifacol.2016.09.017
[research_bester_2023]: https://doi.org/10.1051/matecconf/202338805002
[research_beyer_steen_2024]: https://doi.org/10.2514/1.g007984
[research_beyer_ullah_2024]: https://doi.org/10.1007/s13272-024-00760-8
[research_beyers_1988]: https://doi.org/10.2514/3.45559
[research_bhachu_haftka_2015]: https://doi.org/10.2514/1.c032945
[research_bhandari_bhandari_2026]: https://doi.org/10.2514/1.c038411
[research_bhardwaj_kapania_1995]: https://doi.org/10.2514/3.46814
[research_bhardwaj_tiwari_2022]: https://doi.org/10.1016/j.mlwa.2022.100261
[research_bhatia_jiang_2021]: https://doi.org/10.1002/acs.3228
[research_bhattacharyya_conlansmith_2019]: https://doi.org/10.1016/j.cad.2018.11.001
[research_bi_xie_2017]: https://doi.org/10.1016/j.cja.2016.12.028
[research_bian_nener_2018]: https://doi.org/10.1080/00207179.2018.1473643
[research_bian_nener_2019]: https://doi.org/10.1109/access.2019.2894961
[research_bidinotto_moura_2021]: https://doi.org/10.1017/aer.2021.82
[research_biezaddanielj_chouhweilan_1993]: https://ntrs.nasa.gov/citations/19930017967
[research_biggs_livornese_2020]: https://doi.org/10.2514/1.g005181
[research_bihrle_jr_1980]: https://doi.org/10.21236/ada082335
[research_billingsley_1976]: https://doi.org/10.21236/ada024445
[research_binder_wildschek_2021]: https://doi.org/10.1016/j.ast.2021.106516
[research_binion_tw_1971]: https://doi.org/10.21236/ad0723294
[research_binion_tw_1975]: https://doi.org/10.21236/ada012000
[research_binz_islam_2019]: https://doi.org/10.1177/1756829319861370
[research_binz_moormann_2020]: https://doi.org/10.1177/1756829320961925
[research_biquan_huanwen_1990]: https://doi.org/10.1007/bf02015201
[research_biricik_komurcugil_2019]: https://doi.org/10.1109/tie.2018.2868303
[research_bischoff_1983]: https://doi.org/10.2514/3.44899
[research_biskner_higgins_2005]: https://doi.org/10.21236/ada443361
[research_bismarcknasr_1994]: https://doi.org/10.2514/3.46590
[research_biswas_1993]: https://doi.org/10.1016/0263-8223(93)90233-g
[research_biswas_sharma_2020]: https://doi.org/10.1080/0305215x.2020.1770745
[research_black_moorhouse_1979]: https://doi.org/10.21236/ada085085
[research_blackburn_whitfield_1965]: https://doi.org/10.21236/ad0620247
[research_blackwell_pounds_1977]: https://doi.org/10.2514/3.58877
[research_blair_weisshaar_1982]: https://doi.org/10.2514/3.44806
[research_blake_2002]: https://doi.org/10.21236/ada401264
[research_bland_1980]: https://doi.org/10.2514/3.44684
[research_blight_gangsaas_1986]: https://doi.org/10.2514/3.20145
[research_bliss_1980]: https://doi.org/10.21236/ada093301
[research_boadocuartero_perezalvarez_2024]: https://doi.org/10.3390/aerospace11090748
[research_boatwright_1961]: https://doi.org/10.21236/ad0262552
[research_boby_abdullah_2019]: https://doi.org/10.12928/telkomnika.v17i5.12810
[research_bodson_2000]: https://doi.org/10.21236/ada381657
[research_bodson_2000_b]: https://doi.org/10.21236/ada390623
[research_boeingvertolcophiladelphiapa_1983]: https://doi.org/10.21236/ada134323
[research_bogan_1981]: https://doi.org/10.1007/bf00884128
[research_bogenfeld_freund_2024]: https://doi.org/10.1016/j.compstruct.2023.117803
[research_bohlmann_eckstrom_1990]: https://doi.org/10.2514/3.25319
[research_bohlmannjonathand_1989]: https://ntrs.nasa.gov/citations/19890009883
[research_bohlmannjonathand_scottrobertc_1991]: https://ntrs.nasa.gov/citations/19910047245
[research_bohlmannjonathand_weisshaarterrencea_1988]: https://ntrs.nasa.gov/citations/19880044993
[research_boindala_ostfeld_2022]: https://doi.org/10.3390/w14142199
[research_boldingrm_stearmanro_1976]: https://ntrs.nasa.gov/citations/19770014087
[research_bolocan_valsan_2023]: https://doi.org/10.1016/j.matpr.2022.11.433
[research_bombardieri_cavallaro_2021]: https://doi.org/10.1007/s00158-021-02884-5
[research_bomze_gabl_2022]: https://doi.org/10.1137/20m1355422
[research_bondarenko_shkolnyi_2024]: https://doi.org/10.20535/0203-3771482024318185
[research_bons_martins_2020]: https://doi.org/10.3390/aerospace7080118
[research_bons_martins_2022]: https://doi.org/10.1115/1.4055630
[research_bony_southwell_1969]: https://doi.org/10.2307/3723460
[research_book_reviews_1989]: https://doi.org/10.1177/104687818902000137
[research_boothe_chen_1974]: https://doi.org/10.21236/ad0782218
[research_bordogna_lancelot_2020]: https://doi.org/10.1007/s00158-019-02446-w
[research_borrok_rider_1970]: https://doi.org/10.1002/j.2161-4296.1970.tb00050.x
[research_boschja_kuehlwj_1976]: https://ntrs.nasa.gov/citations/19760058477
[research_bottasso_montinari_2015]: https://doi.org/10.4050/jahs.60.022005
[research_bouadi_moracamino_2018]: https://doi.org/10.2514/1.c034477
[research_boudreau_1977]: https://doi.org/10.2514/3.58889
[research_bouras_2020]: https://doi.org/10.5373/jardcs/v12sp3/20201258
[research_bouton_1950]: https://doi.org/10.2514/8.1573
[research_bowers_1981]: https://doi.org/10.2514/3.57530
[research_bowes_miller_1976]: https://doi.org/10.21236/ada026963
[research_bowmankeithb_grandhiramanav_1989]: https://ntrs.nasa.gov/citations/19890015800
[research_boyd_1977]: https://doi.org/10.21236/ada053640
[research_boydenrp_1974]: https://ntrs.nasa.gov/citations/19830002753
[research_boydenrp_1978]: https://ntrs.nasa.gov/citations/19780025107
[research_boylan_1965]: https://doi.org/10.21236/ad0460154
[research_bradley_1986]: https://doi.org/10.21236/ada173255
[research_bradley_haughn_2026]: https://doi.org/10.2514/1.c038700
[research_braff_till_1993]: https://doi.org/10.2514/atcq.1.2.179
[research_bras_warwick_2022]: https://doi.org/10.1016/j.ast.2022.107400
[research_brennan_mcdaniel_1994]: https://doi.org/10.21236/ada284253
[research_breslin_1961]: https://doi.org/10.5957/jsr.1961.5.3.15
[research_briardy_head_1968]: https://doi.org/10.21236/ad0673964
[research_briggs_reed_1982]: https://doi.org/10.21236/ada125764
[research_brigham_barrie_1973]: https://doi.org/10.21236/ad0782258
[research_brightlg_petersonvl_1960]: https://ntrs.nasa.gov/citations/19650018341
[research_brimelo_glass_1974]: https://doi.org/10.21236/ada000025
[research_brockld_goodmanha_1981]: https://ntrs.nasa.gov/citations/19820004206
[research_brodecki_subbarao_2015]: https://doi.org/10.2514/1.g000220
[research_broer_benedictus_2022]: https://doi.org/10.3390/aerospace9040183
[research_broglio_1957]: https://doi.org/10.2514/8.3851
[research_bromfield_horri_2023]: https://doi.org/10.1017/aer.2023.18
[research_brooks_martins_2018]: https://doi.org/10.1016/j.compstruct.2018.07.100
[research_brooks_martins_2019]: https://doi.org/10.1016/j.jfluidstructs.2019.04.005
[research_brooksjd_beamishjk_1977]: https://ntrs.nasa.gov/citations/19780002105
[research_broussard_stengel_1977]: https://doi.org/10.2514/3.44630
[research_broussardjr_halyon_1983]: https://ntrs.nasa.gov/citations/19840042741
[research_brouwer_mcnamara_2020]: https://doi.org/10.1016/j.jfluidstructs.2019.102838
[research_brown_1994]: https://doi.org/10.21236/ada279489
[research_brownsr_szalaikj_1977]: https://ntrs.nasa.gov/citations/19780028344
[research_brozoski_johnson_2000]: https://doi.org/10.21236/ada378682
[research_bruderlin_hosters_2018]: https://doi.org/10.1007/s13272-018-0322-3
[research_brunojoseph_libeskindmark_1990]: https://ntrs.nasa.gov/citations/19920023270
[research_bryant_albert_1988]: https://doi.org/10.21236/ada196620
[research_bryson_desai_1969]: https://doi.org/10.2514/3.44093
[research_bryson_rumpfkeil_2019]: https://doi.org/10.2514/1.c035152
[research_bu_luo_2025]: https://doi.org/10.1109/jmass.2024.3507735
[research_buche_kushner_2003]: https://doi.org/10.21236/ada461517
[research_buchter_sebastiasaez_2021]: https://doi.org/10.1177/14759217211048149
[research_bueno_dowell_2020]: https://doi.org/10.2514/1.c035885
[research_buffington_1997]: https://doi.org/10.21236/ada327799
[research_buffington_1999]: https://doi.org/10.21236/ada375713
[research_buffington_1999_b]: https://doi.org/10.21236/ada374954
[research_buffington_adams_1995]: https://doi.org/10.1016/0967-0661(95)00039-w
[research_bugala_2025]: https://doi.org/10.2478/tar-2025-0008
[research_bugala_payenskyy_2025]: https://doi.org/10.1108/aeat-05-2025-0183
[research_bulin_dyk_2021]: https://doi.org/10.1007/s11071-021-06582-1
[research_bullock_fields_1998]: https://doi.org/10.21236/ada357847
[research_bulut_schrijer_2026]: https://doi.org/10.1016/j.ast.2026.113138
[research_burcham_myers_1985]: https://doi.org/10.2514/3.45252
[research_burdette_martins_2018]: https://doi.org/10.1016/j.ast.2018.08.004
[research_burke_1978]: https://doi.org/10.1086/447984
[research_burkenjohnj_2007]: https://ntrs.nasa.gov/citations/20090007779
[research_burkett_1989]: https://doi.org/10.1017/s0001924000022235
[research_burkhalter_1993]: https://doi.org/10.2514/3.46447
[research_burnett_beranek_2016]: https://doi.org/10.1017/aer.2016.41
[research_burns_1974]: https://doi.org/10.21236/ada048471
[research_burns_1975]: https://doi.org/10.1017/s0001924000034862
[research_burns_2002]: https://doi.org/10.21236/ada404484
[research_burns_deters_1993]: https://doi.org/10.21236/ada267447
[research_burt_1975]: https://doi.org/10.2514/3.59795
[research_busan_1998]: https://doi.org/10.21236/ada340820
[research_butler_1976]: https://doi.org/10.21236/ada023690
[research_butler_1982]: https://doi.org/10.2514/3.44764
[research_butler_1983]: https://doi.org/10.1017/s0001924000051046
[research_buzica_biswanger_2018]: https://doi.org/10.1016/j.trpro.2018.02.005
[research_bylsma_gunter_2007]: https://doi.org/10.21236/ada466491
[research_byreddy_grandhi_2003]: https://doi.org/10.21236/ada417124
[research_c_yharmin_2018]: https://doi.org/10.14419/ijet.v7i4.13.21355
[research_cabellrandolphh_gibbsgaryp_2000]: https://ntrs.nasa.gov/citations/20040085969
[research_cabuk_2026]: https://doi.org/10.1016/j.ast.2026.111844
[research_cagdas_2017]: https://doi.org/10.1016/j.oceaneng.2017.09.011
[research_cahn_garcia_1971]: https://doi.org/10.2514/3.44233
[research_cai_fan_2026]: https://doi.org/10.2514/1.c038462
[research_cai_su_2024]: https://doi.org/10.3390/machines12070486
[research_cai_yang_2024]: https://doi.org/10.3390/aerospace11120975
[research_cain_1979]: https://doi.org/10.21236/ada379310
[research_caixeta_marques_2018]: https://doi.org/10.1007/s40430-017-0958-7
[research_calarese_1984]: https://doi.org/10.2514/3.48231
[research_californiaunivlosangeles_2001]: https://doi.org/10.21236/ada385808
[research_calise_1977]: https://doi.org/10.2514/3.63239
[research_callaghan_kunz_2021]: https://doi.org/10.2514/1.g004748
[research_callaway_2015]: https://doi.org/10.21236/ad1000591
[research_camacho_akhavan_2021]: https://doi.org/10.1016/j.compstruct.2021.113765
[research_campagna_benedetti_2025]: https://doi.org/10.1016/j.compstruct.2025.119508
[research_campagna_gulizzi_2025]: https://doi.org/10.1016/j.compstruct.2024.118697
[research_campbell_lafrey_1983]: https://doi.org/10.1002/j.2161-4296.1983.tb00853.x
[research_campbell_terrell_1987]: https://doi.org/10.21236/ada190882
[research_campbellrichardl_smithleigha_1989]: https://ntrs.nasa.gov/citations/19910001577
[research_campos_marques_2021]: https://doi.org/10.3390/aerospace8030077
[research_candon_marzocca_2026]: https://doi.org/10.2514/1.j066515
[research_cannella_garinei_2018]: https://doi.org/10.1016/j.compstruct.2017.11.029
[research_cano_sobel_2016]: https://doi.org/10.4236/eng.2016.84016
[research_cao_chen_2026]: https://doi.org/10.1016/j.neucom.2025.132460
[research_cao_huang_2022]: https://doi.org/10.1016/j.compstruct.2022.115204
[research_cao_jia_2020]: https://doi.org/10.1016/j.jfranklin.2020.08.028
[research_cao_liu_2025]: https://doi.org/10.3390/drones9060443
[research_cao_liu_2025_b]: https://doi.org/10.1016/j.ast.2025.110036
[research_cao_lu_2024]: https://doi.org/10.3390/biomimetics9050263
[research_cao_tang_2017]: https://doi.org/10.1631/fitee.1601363
[research_cao_wei_2020]: https://doi.org/10.1155/2020/5603169
[research_cao_xu_2022]: https://doi.org/10.1016/j.ast.2021.107235
[research_caponefj_1981]: https://ntrs.nasa.gov/citations/19810010493
[research_carapella_2022]: https://doi.org/10.1016/j.jedc.2021.104147
[research_carico_1998]: https://doi.org/10.21236/ada350677
[research_carlson_1976]: https://doi.org/10.2514/3.58667
[research_carlson_verberg_2017]: https://doi.org/10.1063/1.4975673
[research_carmichael_mcnay_1961]: https://doi.org/10.21236/ad0282125
[research_carneiro_gamboa_2019]: https://doi.org/10.1108/rpj-02-2018-0044
[research_carroll_1960]: https://doi.org/10.21236/ad0316227
[research_caseiro_mendes_2021]: https://doi.org/10.3390/en14082210
[research_casey_1988]: https://doi.org/10.21236/ada195699
[research_casillas_chen_2024]: https://doi.org/10.1080/19401493.2024.2382757
[research_cassanto_1971]: https://doi.org/10.2514/3.30338
[research_cassanto_1972]: https://doi.org/10.2514/3.50095
[research_castaneda_gordillo_2019]: https://doi.org/10.3390/electronics8070793
[research_castellani_cooper_2017]: https://doi.org/10.2514/1.c033825
[research_cavalcanti_uehara_2026]: https://doi.org/10.2514/1.c038528
[research_cavaliere_fezans_2024]: https://doi.org/10.2514/1.g007762
[research_cavaliere_fezans_2024_b]: https://doi.org/10.2514/1.g008040
[research_cavallaro_bombardieri_2015]: https://doi.org/10.1016/j.jfluidstructs.2015.08.016
[research_cavallo_canciello_2020]: https://doi.org/10.1016/j.automatica.2020.108956
[research_cavin_holyoak_1978]: https://doi.org/10.2514/3.58355
[research_cebeci_1974]: https://doi.org/10.2514/3.49207
[research_celi_1991]: https://doi.org/10.2514/3.45991
[research_celi_friedmann_1990]: https://doi.org/10.2514/3.25141
[research_celi_lovera_2004]: https://doi.org/10.21236/ada425484
[research_cell_1992]: https://doi.org/10.2514/3.11215
[research_cen_li_2020]: https://doi.org/10.1177/0954410020944085
[research_cenkci_1991]: https://doi.org/10.21236/ada241143
[research_center_1975]: https://doi.org/10.21236/adb006719
[research_cerrillobriones_ricardezsandoval_2019]: https://doi.org/10.1016/j.cherd.2019.02.020
[research_cesnik_2002]: https://doi.org/10.21236/ada401331
[research_cesnik_2005]: https://doi.org/10.21236/ada439640
[research_cestino_iannuzzo_2026]: https://doi.org/10.2514/1.c038607
[research_cfd_simulations_2021]: https://doi.org/10.47176/jafm.14.06.32667
[research_chabir_bouteraa_2017]: https://doi.org/10.1504/ijmic.2017.082487
[research_chabod_baron_2020]: https://doi.org/10.2478/fas-2020-0005
[research_chai_song_2017]: https://doi.org/10.1016/j.compstruct.2017.07.053
[research_chajjed_khalil_2024]: https://doi.org/10.1016/j.jsv.2023.117819
[research_chakraborty_roy_2022]: https://doi.org/10.1063/5.0104299
[research_chakravarthy_evans_2015]: https://doi.org/10.1080/01630563.2015.1057286
[research_chakravarty_mahanta_2015]: https://doi.org/10.1002/rnc.3392
[research_chalk_1964]: https://doi.org/10.2514/3.43604
[research_chalk_neal_1969]: https://doi.org/10.21236/ad0860856
[research_chaloff_hiyama_1974]: https://doi.org/10.21236/ada002858
[research_chamlin_1951]: https://doi.org/10.1001/archopht.1951.01700020151003
[research_chamlin_davidoff_1950]: https://doi.org/10.3171/jns.1950.7.6.0539
[research_chancevoughtcorpdallastx_1979]: https://doi.org/10.21236/ada358711
[research_chang_1988]: https://doi.org/10.21236/ada196223
[research_chang_2019]: https://doi.org/10.1007/s11071-019-05223-y
[research_chang_debreuker_2022]: https://doi.org/10.2514/1.g006690
[research_chang_guo_2022]: https://doi.org/10.1016/j.ifacol.2022.07.214
[research_changchuan_lan_2018]: https://doi.org/10.2514/1.c034162
[research_changchuan_zhiying_2022]: https://doi.org/10.2514/1.j061138
[research_chaparrodaniel_fujiwaragustavoec_2016]: https://ntrs.nasa.gov/citations/20160008102
[research_chaplin_1953]: https://doi.org/10.21236/ad0775892
[research_chase_1977]: https://doi.org/10.2514/3.58782
[research_chatterjee_chowdhury_2019]: https://doi.org/10.1007/s00158-018-2167-0
[research_chattopadhyay_dutta_1995]: https://doi.org/10.1016/0308-0161(95)93967-a
[research_chattopadhyayaditi_jharatneshwar_1996]: https://ntrs.nasa.gov/citations/19970028021
[research_chattopadhyayaditi_zhangsen_1995]: https://ntrs.nasa.gov/citations/19950026507
[research_chau_piotrowski_2026]: https://doi.org/10.2514/1.c038646
[research_chau_zingg_2022]: https://doi.org/10.2514/1.c036389
[research_chau_zingg_2023]: https://doi.org/10.2514/1.c037158
[research_chauhan_martins_2021]: https://doi.org/10.2514/1.c035991
[research_chauhan_martins_2022]: https://doi.org/10.2514/1.c035991.c1
[research_chauhan_martins_2024]: https://doi.org/10.3390/aerospace11070512
[research_chauhan_praveen_2023]: https://doi.org/10.61653/joast.v62i4.2010.508
[research_chen_1982]: https://doi.org/10.2514/3.51069
[research_chen_1983]: https://doi.org/10.4050/jahs.28.34
[research_chen_cai_2026]: https://doi.org/10.1109/tie.2025.3639811
[research_chen_dong_2023]: https://doi.org/10.1080/0305215x.2023.2212246
[research_chen_dugundji_1987]: https://doi.org/10.2514/3.45501
[research_chen_edwards_2018]: https://doi.org/10.1002/rnc.4282
[research_chen_edwards_2020]: https://doi.org/10.1016/j.automatica.2020.108829
[research_chen_edwards_2022]: https://doi.org/10.1109/lcsys.2021.3090654
[research_chen_gao_2017]: https://doi.org/10.2316/journal.201.2017.4.201-2838
[research_chen_gao_2020]: https://doi.org/10.1016/j.ast.2020.105871
[research_chen_gao_2022]: https://doi.org/10.1016/j.ast.2022.107668
[research_chen_gao_2023]: https://doi.org/10.3390/aerospace10050486
[research_chen_gao_2023_b]: https://doi.org/10.54254/2755-2721/9/20230085
[research_chen_han_2017]: https://doi.org/10.21595/mme.2017.18505
[research_chen_han_2022]: https://doi.org/10.3390/app12031244
[research_chen_he_2020]: https://doi.org/10.3390/sym12040544
[research_chen_he_2025]: https://doi.org/10.3390/app15084333
[research_chen_holohan_2015]: https://doi.org/10.1002/rnc.3362
[research_chen_jing_2020]: https://doi.org/10.1108/aeat-01-2020-0005
[research_chen_li_2017]: https://doi.org/10.1016/j.compstruct.2017.02.019
[research_chen_li_2018]: https://doi.org/10.1016/j.ast.2018.01.023
[research_chen_li_2019]: https://doi.org/10.1142/s0219455419501438
[research_chen_li_2024]: https://doi.org/10.3390/s24051597
[research_chen_liu_2016]: https://doi.org/10.2514/1.c033305
[research_chen_mangione_1967]: https://doi.org/10.2514/3.4365
[research_chen_meng_2025]: https://doi.org/10.1016/j.ast.2025.110043
[research_chen_nie_2018]: https://doi.org/10.1016/j.compstruct.2017.12.042
[research_chen_niu_2018]: https://doi.org/10.1109/access.2018.2820008
[research_chen_qin_2025]: https://doi.org/10.1088/1742-6596/3109/1/012066
[research_chen_qiu_2017]: https://doi.org/10.1016/j.ast.2017.09.018
[research_chen_rao_2023]: https://doi.org/10.1016/j.cja.2023.03.039
[research_chen_ren_2015]: https://doi.org/10.1504/ijasm.2015.073525
[research_chen_shi_2023]: https://doi.org/10.1063/5.0130370
[research_chen_shi_2023_b]: https://doi.org/10.1063/5.0162013
[research_chen_sun_1987]: https://doi.org/10.1016/0263-8223(87)90019-5
[research_chen_tang_2017]: https://doi.org/10.1177/0954410017746199
[research_chen_wang_2019]: https://doi.org/10.1061/(asce)as.1943-5525.0001004
[research_chen_wang_2023]: https://doi.org/10.1109/access.2023.3249790
[research_chen_wang_2026]: https://doi.org/10.1016/j.ast.2026.112682
[research_chen_yang_2018]: https://doi.org/10.1360/n092017-00428
[research_chen_zhai_2025]: https://doi.org/10.1186/s42774-025-00227-2
[research_chen_zhang_2015]: https://doi.org/10.1360/sspma2015-00338
[research_chen_zhang_2017]: https://doi.org/10.1177/1729881416678141
[research_chen_zhao_2020]: https://doi.org/10.1061/(asce)as.1943-5525.0001201
[research_chen_zhao_2023]: https://doi.org/10.1115/1.4063294
[research_cheng_li_2023]: https://doi.org/10.3390/aerospace10090786
[research_cheng_liang_2019]: https://doi.org/10.1016/j.addma.2019.03.001
[research_cheng_wei_2017]: https://doi.org/10.1002/acs.2779
[research_cheng_zhou_2015]: https://doi.org/10.1115/1.4029026
[research_chenghk_mengsy_1980]: https://ntrs.nasa.gov/citations/19800038581
[research_cherry_costa_1993]: https://doi.org/10.1080/00423119308969481
[research_chetty_lakshmi_1991]: https://doi.org/10.1016/s1474-6670(17)54311-6
[research_chi_gu_2022]: https://doi.org/10.1063/5.0077291
[research_chiarelli_bonomo_2019]: https://doi.org/10.1155/2019/8210235
[research_chien_tang_1964]: https://doi.org/10.21236/ad0609470
[research_chih_peng_2026]: https://doi.org/10.1016/j.apm.2026.117000
[research_chin_1989]: https://doi.org/10.2514/3.45888
[research_chin_lee_1994]: https://doi.org/10.1016/0967-0661(94)90572-x
[research_chinj_chaconv_1987]: https://ntrs.nasa.gov/citations/19880027032
[research_chinvorarat_2021]: https://doi.org/10.1016/j.heliyon.2021.e08410
[research_chipmanr_rauchf_1984]: https://ntrs.nasa.gov/citations/19840013485
[research_chipmanr_rauchf_1985]: https://ntrs.nasa.gov/citations/19850048205
[research_choi_2004]: https://doi.org/10.21236/ada426554
[research_choi_2016]: https://doi.org/10.5762/kais.2016.17.1.159
[research_choi_choi_2026]: https://doi.org/10.3390/aerospace13060526
[research_choi_kim_2023]: https://doi.org/10.3390/drones7070418
[research_choi_lim_2020]: https://doi.org/10.5139/jksas.2020.48.8.555
[research_choi_park_2019]: https://doi.org/10.1016/j.compstruct.2019.111027
[research_choi_shrestha_2017]: https://doi.org/10.1177/1475921716686963
[research_choosakngaongam_rapeeujjin_2024]: https://doi.org/10.37934/cfdl.16.5.18
[research_choudhury_singh_2023]: https://doi.org/10.1088/2631-8695/acca71
[research_chougule_sonawane_2017]: https://doi.org/10.2139/ssrn.3101358
[research_chowdary_parthan_1994]: https://doi.org/10.1016/0045-7949(94)90200-3
[research_chowhan_arya_2019]: https://doi.org/10.1002/j.2334-5837.2019.00697.x
[research_christoforou_1993]: https://doi.org/10.1016/0263-8223(93)90046-s
[research_christopherkdroney_anthonyjsclafani_2020]: https://ntrs.nasa.gov/citations/20205005698
[research_christopherlblanken_matthewswhalley_1993]: https://ntrs.nasa.gov/citations/19940008821
[research_chu_hou_2021]: https://doi.org/10.1016/j.conengprac.2021.104735
[research_chujulio_lawingpiercel_1990]: https://ntrs.nasa.gov/citations/19930020260
[research_cidmontoya_hernandez_2018]: https://doi.org/10.1016/j.jweia.2017.12.018
[research_clark_2001]: https://doi.org/10.21236/ada399161
[research_clark_dellamico_1962]: https://doi.org/10.21236/ad0284659
[research_clark_letron_1989]: https://doi.org/10.2514/3.20392
[research_clark_spurlin_1962]: https://doi.org/10.21236/ad0329345
[research_clarker_shaned_1982]: https://ntrs.nasa.gov/citations/19820015371
[research_clarkerobert_burkenjohnj_1994]: https://ntrs.nasa.gov/citations/19940029878
[research_clay_rockafellow_1973]: https://doi.org/10.21236/ad0758891
[research_clements_djidjeli_2023]: https://doi.org/10.1061/jaeeez.aseng-4707
[research_clementskeith_2016]: https://ntrs.nasa.gov/citations/20160013364
[research_clews_1973]: https://doi.org/10.1108/eb035015
[research_cliett_1952]: https://doi.org/10.21236/ad0006050
[research_clyde_bonner_1984]: https://doi.org/10.21236/ada148355
[research_coban_2020]: https://doi.org/10.5755/j01.itc.49.1.23275
[research_cobogonzalez_rodriguezrobles_2026]: https://doi.org/10.1017/aer.2026.10212
[research_cochran_2015]: https://doi.org/10.2514/1.g000628
[research_coder_2021]: https://doi.org/10.2514/1.c035887
[research_coder_2026]: https://doi.org/10.1007/s13272-026-00956-0
[research_coe_kulla_1974]: https://doi.org/10.2514/3.60383
[research_coepaulljr_perkinsjohnn_1990]: https://ntrs.nasa.gov/citations/19900058865
[research_cohen_1982]: https://doi.org/10.1177/002199838201600404
[research_cohendorothea_lejeanetteh_1991]: https://ntrs.nasa.gov/citations/19910063181
[research_cohenga_1978]: https://ntrs.nasa.gov/citations/19780046985
[research_coldsnow_uybarreta_2009]: https://doi.org/10.21236/ada516721
[research_cole_1988]: https://doi.org/10.2514/3.45609
[research_cole_1988_b]: https://doi.org/10.21236/ada196247
[research_cole_cook_1980]: https://doi.org/10.21236/ada207109
[research_colesr_1986]: https://ntrs.nasa.gov/citations/19860034894
[research_collings_tee_1979]: https://doi.org/10.1016/0045-7949(79)90026-9
[research_combination_of_2024]: https://doi.org/10.62441/nano-ntp.v20is14.68
[research_combined_flight_1974]: https://doi.org/10.1108/eb035139
[research_comer_chakraborty_2024]: https://doi.org/10.4050/jahs.69.032003
[research_composite_materials_1989]: https://doi.org/10.1108/eb036810
[research_computational_and_2024]: https://doi.org/10.52783/jisem.v9i4.82
[research_computational_investigation_2025]: https://doi.org/10.47176/jafm.18.3.2915
[research_concorde_automatic_1971]: https://doi.org/10.1108/eb034745
[research_cong_hu_2023]: https://doi.org/10.3390/aerospace10030241
[research_conlansmith_andreasen_2022]: https://doi.org/10.1007/s00158-022-03246-5
[research_connelly_1982]: https://doi.org/10.21236/ada120473
[research_contellasins_landersheim_2021]: https://doi.org/10.3390/app11062752
[research_convolutional_neural_2025]: https://doi.org/10.61091/jcmcc127a-259
[research_cook_1979]: https://doi.org/10.1090/qam/542990
[research_cooperpa_stroudwj_1972]: https://ntrs.nasa.gov/citations/19730028903
[research_coppin_birch_2018]: https://doi.org/10.2514/1.c033988
[research_cordeiro_azinheira_2024]: https://doi.org/10.1016/j.conengprac.2024.105909
[research_corlissld_talbotpd_1977]: https://ntrs.nasa.gov/citations/19770024230
[research_cornelius_lucius_1994]: https://doi.org/10.2514/3.46566
[research_cornellaeronauticallabincbuffalony_1947]: https://doi.org/10.21236/ada800190
[research_cornellaeronauticallabincbuffalony_1953]: https://doi.org/10.21236/ad0006796
[research_cornette_kerdreux_2015]: https://doi.org/10.1115/1.4027717
[research_cotton_1974]: https://doi.org/10.21236/ada000894
[research_councill_goble_1971]: https://doi.org/10.2514/3.30296
[research_coyette_1987]: https://doi.org/10.1108/eb023684
[research_crabtree_1979]: https://doi.org/10.21236/ada081738
[research_craig_1965]: https://doi.org/10.21236/ad0628087
[research_craig_erbug_1976]: https://doi.org/10.1016/0045-7949(76)90049-3
[research_crandall_maund_1973]: https://doi.org/10.21236/ad0766642
[research_cranedf_1983]: https://ntrs.nasa.gov/citations/19830055004
[research_cranedf_1984]: https://ntrs.nasa.gov/citations/19850009674
[research_craneharoldl_sommerrobertw_1961]: https://ntrs.nasa.gov/citations/19980227996
[research_craver_egle_1972]: https://doi.org/10.1016/0022-460x(72)90530-5
[research_crawley_lee_1978]: https://doi.org/10.21236/ada062582
[research_creazza_dimarco_1993]: https://doi.org/10.1007/bf02472612
[research_crews_naik_1986]: https://doi.org/10.1016/0263-8223(86)90066-8
[research_crimi_grace_1965]: https://doi.org/10.21236/ad0619661
[research_crimi_ordway_1962]: https://doi.org/10.2514/8.9560
[research_crisfield_1978]: https://doi.org/10.1016/0045-7949(78)90144-x
[research_crittenden_weishaar_1978]: https://doi.org/10.2514/3.58383
[research_crolla_abdelhady_1991]: https://doi.org/10.1080/00423119108968982
[research_crombie_moorhouse_1980]: https://doi.org/10.21236/ada088629
[research_croommarka_whippleraymondd_1988]: https://ntrs.nasa.gov/citations/19890063988
[research_croop_1985]: https://doi.org/10.21236/ada368444
[research_crother_gabelman_1973]: https://doi.org/10.21236/ada004416
[research_crouse_leishman_1992]: https://doi.org/10.2514/3.46139
[research_crowe_1937]: https://doi.org/10.1108/eb030157
[research_cruz_gorenberg_1969]: https://doi.org/10.21236/ad0864282
[research_cui_azuara_2021]: https://doi.org/10.1177/14759217211023934
[research_cui_he_2025]: https://doi.org/10.3390/aerospace12050404
[research_cui_khodaverdian_2026]: https://doi.org/10.1016/j.dche.2026.100291
[research_cui_li_2022]: https://doi.org/10.1016/j.oceaneng.2022.113138
[research_cui_miao_2026]: https://doi.org/10.1016/j.compstruct.2026.120413
[research_cui_yang_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000528
[research_cully_boller_1973]: https://doi.org/10.21236/ad0916279
[research_cundiff_buckingham_1999]: https://doi.org/10.21236/ada382521
[research_cunis_burlion_2019]: https://doi.org/10.2514/1.g003618
[research_cunis_condomines_2020]: https://doi.org/10.2514/1.c035455
[research_cunis_condomines_2020_b]: https://doi.org/10.2514/1.g004753
[research_cunningham_batina_1988]: https://doi.org/10.2514/3.45686
[research_cunninghamherbertj_batinajohnt_1987]: https://ntrs.nasa.gov/citations/19880064102
[research_currao_jiang_2026]: https://doi.org/10.1017/flo.2026.10056
[research_curry_matthews_1965]: https://doi.org/10.21236/ad0617748
[research_curtiss_1971]: https://doi.org/10.2514/3.59098
[research_curtiss_howardc_1961]: https://doi.org/10.21236/ad0263838
[research_cuschieri_1990]: https://doi.org/10.21236/ada279431
[research_cutchinsma_purvisjw_1982]: https://ntrs.nasa.gov/citations/19820025882
[research_czyba_stajer_2019]: https://doi.org/10.24425/acs.2019.127525
[research_czysz_1963]: https://doi.org/10.21236/ad0407689
[research_dababneh_kipouros_2018]: https://doi.org/10.3390/aerospace5010003
[research_dagal_2026]: https://doi.org/10.1016/j.ress.2025.111841
[research_daghighi_2026]: https://doi.org/10.1016/j.compstruct.2026.120715
[research_daghighi_rouhi_2020]: https://doi.org/10.1016/j.compstruct.2019.111630
[research_dagilis_kilikevicius_2023]: https://doi.org/10.3390/aerospace10090801
[research_dagkolu_gokdag_2021]: https://doi.org/10.1016/j.promfg.2021.07.037
[research_dai_he_2019]: https://doi.org/10.1002/rnc.4453
[research_dai_hu_2025]: https://doi.org/10.1016/j.cja.2024.09.021
[research_dai_wu_2016]: https://doi.org/10.1016/j.ast.2016.01.019
[research_dai_yang_2015]: https://doi.org/10.2322/tjsass.58.237
[research_dai_zhang_2023]: https://doi.org/10.3390/aerospace10060553
[research_daken_mar_1985]: https://doi.org/10.1016/0263-8223(85)90002-9
[research_dallas_irvin_1956]: https://doi.org/10.21236/ad0147926
[research_damico_labella_2025]: https://doi.org/10.1016/j.sysconle.2024.105974
[research_damodaran_caughey_1988]: https://doi.org/10.2514/3.10046
[research_dandois_2016]: https://doi.org/10.1063/1.4937426
[research_dandrea_2003]: https://doi.org/10.21236/ada422201
[research_dandrea_2008]: https://doi.org/10.21236/ada530333
[research_daniel_1976]: https://doi.org/10.21236/ada041490
[research_dapolito_sulzbachner_2021]: https://doi.org/10.1016/j.ifacol.2021.10.454
[research_darabi_ganesan_2016]: https://doi.org/10.1016/j.compstruct.2016.02.064
[research_darabi_ganesan_2017]: https://doi.org/10.1016/j.compstruct.2017.04.059
[research_darabseh_tarabulsi_2022]: https://doi.org/10.3390/aerospace9090475
[research_daronch_drofelnik_2019]: https://doi.org/10.1016/j.ast.2019.04.057
[research_das_kapuria_2016]: https://doi.org/10.1016/j.jfluidstructs.2015.11.008
[research_das_longo_1995]: https://doi.org/10.2514/3.46782
[research_daspatel_kumarkaruparthi_2021]: https://doi.org/10.33564/ijeast.2021.v05i09.038
[research_data_driven_model_free_2016]: https://doi.org/10.12700/aph.13.1.2016.1.7
[research_daudeville_ladeveze_1993]: https://doi.org/10.1016/0263-8223(93)90203-3
[research_davanipour_khayatian_2017]: https://doi.org/10.1002/acs.2849
[research_david_hale_1978]: https://doi.org/10.21236/ada065822
[research_davidmrichwine_davidffisher_1992]: https://ntrs.nasa.gov/citations/19920022032
[research_davidson_hd_1972]: https://doi.org/10.21236/ad0763365
[research_davila_bisagni_2017]: https://doi.org/10.1177/0021998317715785
[research_davis_1973]: https://doi.org/10.21236/ad0781807
[research_davis_garnett_1977]: https://doi.org/10.21236/ada050059
[research_davisddjr_farleygaryl_1993]: https://ntrs.nasa.gov/citations/19930049917
[research_dawe_bull_2025]: https://doi.org/10.2514/1.j064731
[research_dawe_roufaeil_1980]: https://doi.org/10.1016/0022-460x(80)90477-0
[research_daynes_2024]: https://doi.org/10.1016/j.addma.2024.104010
[research_de_jrad_2019]: https://doi.org/10.2514/1.c034818
[research_debiasi_2020]: https://doi.org/10.2514/1.c035626
[research_debilzan_1975]: https://doi.org/10.21236/ada019111
[research_decker_2002]: https://doi.org/10.21236/ada403228
[research_deconihout_menand_1992]: https://doi.org/10.1016/0039-6028(92)91070-r
[research_dedoes_1969]: https://doi.org/10.21236/ad0694483
[research_deepa_gupta_2023]: https://doi.org/10.61653/joast.v65i2.2013.727
[research_deetsda_1975]: https://ntrs.nasa.gov/citations/19750010175
[research_defelice_sorrentino_2022]: https://doi.org/10.1007/s11071-022-07487-3
[research_deformational_behaviour_1990]: https://doi.org/10.1016/0010-4361(90)90242-o
[research_degaspari_mantegazza_2024]: https://doi.org/10.1109/access.2024.3390557
[research_degaspari_riccobene_2018]: https://doi.org/10.2514/1.c034860
[research_dehghanmanshadi_saghafi_2021]: https://doi.org/10.2514/1.c035941
[research_delcarre_palacios_2020]: https://doi.org/10.2514/1.c035901
[research_delgado_datta_2026]: https://doi.org/10.2514/1.c038396
[research_demarchi_haning_1978]: https://doi.org/10.21236/ada060326
[research_demedeiros_vandepitte_2017]: https://doi.org/10.1177/1475921716688442
[research_demir_altunkaya_2025]: https://doi.org/10.3390/aerospace12060478
[research_demir_gorguluarslan_2023]: https://doi.org/10.1007/s00158-023-03557-1
[research_demir_seyfullahbabaarslan_2021]: https://doi.org/10.11648/j.ajset.20210602.13
[research_deng_qin_2021]: https://doi.org/10.2514/1.j060528
[research_deng_stoica_2024]: https://doi.org/10.1016/j.ifacol.2025.01.196
[research_deng_tao_2025]: https://doi.org/10.3390/math13111766
[research_deng_xu_2026]: https://doi.org/10.1142/s2301385027500622
[research_deng_yi_2023]: https://doi.org/10.3390/aerospace10020125
[research_deng_yi_2026]: https://doi.org/10.3390/aerospace13060540
[research_deng_zeng_2024]: https://doi.org/10.1177/14759217241233181
[research_deng_zhang_2023]: https://doi.org/10.3390/aerospace10060537
[research_deninno_uherka_1966]: https://doi.org/10.21236/ad0637525
[research_deobald_gibson_1988]: https://doi.org/10.1016/s0022-460x(88)80187-1
[research_departmentoftheairforcewashingtondc_1986]: https://doi.org/10.21236/ada268620
[research_derkach_zinkovskii_2022]: https://doi.org/10.1016/j.prostr.2022.01.005
[research_desai_halder_2022]: https://doi.org/10.1016/j.oceaneng.2022.110833
[research_description_and_1975]: https://ntrs.nasa.gov/citations/19750010173
[research_design_and_2024]: https://doi.org/10.52783/jisem.v9i4.74
[research_design_and_2026]: https://doi.org/10.64388/irev9i11-1718204
[research_design_of_1995]: https://doi.org/10.1016/0967-0661(95)90151-5
[research_design_of_2018]: https://doi.org/10.33103/uot.ijccce.18.2.4
[research_design_of_2019]: https://doi.org/10.35940/ijrte.b1316.0982s1119
[research_design_optimization_2025]: https://doi.org/10.14445/23488360/ijme-v12i9p109
[research_design_simulation_2015]: https://doi.org/10.21275/v4i11.nov151310
[research_desilva_carmichael_1978]: https://doi.org/10.2514/3.58435
[research_desilvabme_medanrt_1978]: https://ntrs.nasa.gov/citations/19790005851
[research_deskos_delcarre_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.102981
[research_desouza_deleon_2023]: https://doi.org/10.1080/0305215x.2023.2243455
[research_desouza_vuillemin_2023]: https://doi.org/10.2514/1.g007153
[research_despirito_2005]: https://doi.org/10.21236/ada444636
[research_devi_2019]: https://doi.org/10.21275/sr231208204149
[research_devine_choynowski_2025]: https://doi.org/10.3390/safety11010004
[research_dewagter_meulenbeld_2019]: https://doi.org/10.1177/1756829319880302
[research_dewitte_qing_2022]: https://doi.org/10.3390/electronics11142267
[research_dexl_hauffe_2020]: https://doi.org/10.1007/s00158-020-02613-4
[research_dexter_1993]: https://doi.org/10.1243/pime_proc_1993_207_241_02
[research_dghim_ferchichi_2018]: https://doi.org/10.1016/j.expthermflusci.2018.05.011
[research_dghim_ferchichi_2020]: https://doi.org/10.1017/jfm.2020.343
[research_dhadekar_misra_2021]: https://doi.org/10.1108/aeat-07-2020-0149
[research_dhawan_huang_2026]: https://doi.org/10.1016/j.cub.2025.12.024
[research_dhiman_abhishek_2022]: https://doi.org/10.2514/1.c036390
[research_dhital_chouvion_2024]: https://doi.org/10.3390/aerospace11121043
[research_dhonau_blosser_1974]: https://doi.org/10.21236/ada032816
[research_dhondt_degryse_2022]: https://doi.org/10.4236/jtts.2022.121009
[research_dias_2023]: https://doi.org/10.2514/1.c037252
[research_dicaprio_acanfora_2019]: https://doi.org/10.3390/aerospace6060071
[research_dickerson_2020]: https://doi.org/10.1098/rspb.2020.1774
[research_didonato_balachandran_2017]: https://doi.org/10.2514/1.g000252
[research_diederichfranklinw_budianskybernard_1948]: https://ntrs.nasa.gov/citations/19930082318
[research_dienes_1978]: https://doi.org/10.1063/1.862291
[research_difrancesco_mattei_2016]: https://doi.org/10.2514/1.c033183
[research_difranco_1970]: https://doi.org/10.2514/3.44199
[research_difranco_1971]: https://doi.org/10.21236/ad0742246
[research_diggins_1951]: https://doi.org/10.21236/ad0895227
[research_digital_model_reference_1994]: https://doi.org/10.1016/0967-0661(94)90529-0
[research_dileone_lobalbo_2021]: https://doi.org/10.3390/aerospace8110334
[research_dillinger_abdalla_2019]: https://doi.org/10.1007/s13272-019-00397-y
[research_dillinger_meddaikar_2020]: https://doi.org/10.3390/fluids5010035
[research_dilmi_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001401
[research_ding_shi_2025]: https://doi.org/10.3390/aerospace12070580
[research_ding_xu_2022]: https://doi.org/10.1016/j.compstruct.2022.116067
[research_ding_zhou_2018]: https://doi.org/10.1007/s42401-018-0008-x
[research_dini_saponara_2022]: https://doi.org/10.3390/en15238990
[research_dinler_2025]: https://doi.org/10.3390/app152010882
[research_dipasquale_prince_2023]: https://doi.org/10.3390/aerospace10060569
[research_directiondesrecherches_1992]: https://doi.org/10.1016/0963-8695(92)90571-w
[research_dirito_schettini_2016]: https://doi.org/10.1016/j.ress.2015.12.012
[research_disante_2015]: https://doi.org/10.3390/s150818666
[research_divakar_bl_2026]: https://doi.org/10.1002/adc2.70054
[research_dix_mattasits_1980]: https://doi.org/10.21236/ada087237
[research_dlamini_jones_2016]: https://doi.org/10.1017/aer.2016.42
[research_dlbirdsall_1970]: https://doi.org/10.1017/s0001924000114812
[research_dobosbubno_hartsook_1977]: https://doi.org/10.21236/ada062008
[research_dodayav_biswas_2024]: https://doi.org/10.2139/ssrn.4875854
[research_dodic_krstic_2023]: https://doi.org/10.3390/aerospace10030238
[research_doggettrobertvjr_riverajoseajr_1995]: https://ntrs.nasa.gov/citations/19950019961
[research_doi_kataoka_1982]: https://doi.org/10.1299/jsme1958.25.1373
[research_doman_1995]: https://doi.org/10.21236/ada305053
[research_donato_galletti_2024]: https://doi.org/10.1016/j.applthermaleng.2023.121431
[research_dong_2018]: https://doi.org/10.1016/j.ast.2018.02.026
[research_dong_2025]: https://doi.org/10.61173/d58c8037
[research_dong_li_2022]: https://doi.org/10.3390/aerospace9120795
[research_dong_li_2023]: https://doi.org/10.1002/rnc.6722
[research_dong_lu_2016]: https://doi.org/10.1155/2016/5037678
[research_dong_shi_2019]: https://doi.org/10.1063/1.5093559
[research_dong_zhou_2025]: https://doi.org/10.1016/j.ast.2025.110199
[research_dooley_1965]: https://doi.org/10.1016/0020-7403(65)90017-2
[research_dorey_good_1980]: https://doi.org/10.1080/00423118008968613
[research_douglasaircraftcolongbeachca_1963]: https://doi.org/10.21236/ad0425406
[research_douglasaircraftcolongbeachca_1977]: https://doi.org/10.21236/ada056857
[research_dowell_bliss_1978]: https://doi.org/10.21236/ada055735
[research_dowell_hall_2003]: https://doi.org/10.21236/ada426408
[research_dresselhaus_dresselhaus_1982]: https://doi.org/10.21236/ada121236
[research_drtil_schulz_1978]: https://doi.org/10.1108/eb035443
[research_drummond_1971]: https://doi.org/10.21236/ad0729870
[research_du_liu_2023]: https://doi.org/10.1016/j.oceaneng.2023.114402
[research_du_zhao_2026]: https://doi.org/10.1063/5.0326549
[research_duan_fan_2018]: https://doi.org/10.1515/tjj-2018-0013
[research_duan_he_2024]: https://doi.org/10.1115/1.4064325
[research_duan_okwudire_2019]: https://doi.org/10.1016/j.automatica.2018.11.049
[research_duan_zhang_2018]: https://doi.org/10.1007/s42401-018-0009-9
[research_dubary_bouvet_2018]: https://doi.org/10.1016/j.compstruct.2018.08.045
[research_dubigeon_1992]: https://doi.org/10.2514/3.11232
[research_dugundji_1965]: https://doi.org/10.21236/ad0624995
[research_dugundji_dowell_1962]: https://doi.org/10.21236/ad0278235
[research_dukes_1970]: https://doi.org/10.21236/ad0871424
[research_dul_2018]: https://doi.org/10.1108/aeat-11-2016-0215
[research_dunmire_1982]: https://doi.org/10.21236/ada148595
[research_dunn_leong_1981]: https://doi.org/10.21236/ada103922
[research_dunningpeterd_stanfordbretk_2014]: https://ntrs.nasa.gov/citations/20140007305
[research_dunnwr_cottrelld_1986]: https://ntrs.nasa.gov/citations/19860019473
[research_durand_teper_1964]: https://doi.org/10.21236/ad0606040
[research_durlofsky_mayers_1970]: https://doi.org/10.21236/ad0871426
[research_durstonda_schreinerja_1983]: https://ntrs.nasa.gov/citations/19840027787
[research_dushane_1957]: https://doi.org/10.1126/science.125.3250.677
[research_dussart_lone_2019]: https://doi.org/10.3390/aerospace6060070
[research_dutta_zhao_2025]: https://doi.org/10.1016/j.compstruct.2025.119221
[research_dwivedi_anitha_2022]: https://doi.org/10.1002/masy.202100364
[research_dyess_williamw_1976]: https://doi.org/10.21236/adb022406
[research_dynamic_flight_2023]: https://doi.org/10.56726/irjmets39167
[research_dyncorprestonva_1999]: https://doi.org/10.21236/ada445729
[research_dzhurynskyi_2026]: https://doi.org/10.32620/aktt.2026.1.03
[research_eades_jr_1964]: https://doi.org/10.21236/ad0352807
[research_eastep_olsen_1980]: https://doi.org/10.2514/3.50866
[research_eastep_venkayya_1984]: https://doi.org/10.2514/3.45063
[research_ebnerre_markjg_1977]: https://ntrs.nasa.gov/citations/19770059956
[research_ebrahimzade_dardel_2016]: https://doi.org/10.1007/s11071-016-2948-1
[research_ecer_1985]: https://doi.org/10.21236/ada162168
[research_eckhaus_1962]: https://doi.org/10.2514/8.9589
[research_eckstromcv_spaincv_1982]: https://ntrs.nasa.gov/citations/19820046611
[research_edenborough_1968]: https://doi.org/10.2514/3.43915
[research_edwards_1950]: https://doi.org/10.1108/eb031872
[research_edwards_1963]: https://doi.org/10.21236/ad0401458
[research_edwards_1983]: https://doi.org/10.2514/3.44863
[research_effective_torsional_1976]: https://doi.org/10.14359/11098
[research_effects_of_1988]: https://doi.org/10.1016/0010-4361(88)90589-7
[research_efremov_efremov_2020]: https://doi.org/10.2514/1.g004409
[research_efremov_shcherbakov_2022]: https://doi.org/10.34759/vst-2022-1-201-210
[research_ehlers_weisshaar_1993]: https://doi.org/10.2514/3.46376
[research_eichler_1970]: https://doi.org/10.2514/3.44170
[research_ekaterinarisja_schifflewisb_1990]: https://ntrs.nasa.gov/citations/19900058795
[research_ekaterinarisja_schifflewisb_1994]: https://ntrs.nasa.gov/citations/19950037635
[research_ekquist_1965]: https://doi.org/10.21236/ad0623129
[research_elenchezhiyan_kumar_2025]: https://doi.org/10.1017/aer.2025.10069
[research_elham_2015]: https://doi.org/10.1016/j.ast.2014.12.024
[research_elham_vantooren_2016]: https://doi.org/10.1007/s00158-016-1447-9
[research_elham_vantooren_2016_b]: https://doi.org/10.1007/s00158-016-1613-0
[research_ellis_borshchova_2021]: https://doi.org/10.1139/juvs-2021-0005
[research_elmahdy_ali_2025]: https://doi.org/10.1038/s41598-025-99500-z
[research_elsalamony_aziz_2020]: https://doi.org/10.1142/s2301385021500138
[research_elshazly_kassem_2025]: https://doi.org/10.1088/1742-6596/3070/1/012001
[research_elyasi_roudbari_2020]: https://doi.org/10.1007/s40430-020-02633-7
[research_enciu_2019]: https://doi.org/10.7763/ijmo.2019.v9.729
[research_eney_1968]: https://doi.org/10.2514/3.43938
[research_eng_1988]: https://doi.org/10.21236/ada205961
[research_engellandsa_franklinja_1992]: https://ntrs.nasa.gov/citations/19930029331
[research_enns_2003]: https://doi.org/10.21236/ada411755
[research_enns_ozbay_1992]: https://doi.org/10.2514/3.20863
[research_ensemble_machine_2021]: https://doi.org/10.33140/amlai.02.01.03
[research_eraslan_oktay_2023]: https://doi.org/10.5755/j01.itc.52.4.33527
[research_erel_1988]: https://doi.org/10.2514/3.45535
[research_erel_seginer_1985]: https://doi.org/10.2514/3.45180
[research_ericksongarye_2003]: https://ntrs.nasa.gov/citations/20040016158
[research_eriksson_1990]: https://doi.org/10.1177/002199839002401201
[research_esfahani_webb_2018]: https://doi.org/10.1007/s00348-018-2588-y
[research_esmaeili_sousa_2023]: https://doi.org/10.1177/17568293231197127
[research_eugeneltu_1996]: https://ntrs.nasa.gov/citations/19960047050
[research_evald_hollweg_2023]: https://doi.org/10.1002/acs.3628
[research_ewing_hinger_1988]: https://doi.org/10.1016/0263-8223(88)90050-5
[research_experimental_investigation_2023]: https://doi.org/10.1063/5.0147213
[research_fadel_rabie_2019]: https://doi.org/10.18280/jesa.520307
[research_fan_jiang_2026]: https://doi.org/10.1108/aeat-01-2026-0033
[research_fan_liu_2021]: https://doi.org/10.1016/j.compstruct.2021.114165
[research_fan_wang_2023]: https://doi.org/10.1002/rnc.7006
[research_fan_wang_2025]: https://doi.org/10.3390/aerospace12090784
[research_fan_xu_2025]: https://doi.org/10.1016/j.autcon.2025.106109
[research_fan_yu_2021]: https://doi.org/10.2514/1.c036138
[research_fan_zhang_2018]: https://doi.org/10.1109/tec.2018.2859338
[research_fang_abed_1998]: https://doi.org/10.21236/ada438538
[research_fang_cao_2020]: https://doi.org/10.1061/(asce)be.1943-5592.0001567
[research_fanucci_1987]: https://doi.org/10.1177/002199838702100204
[research_farbridge_woodward_1956]: https://doi.org/10.1108/eb032701
[research_fardad_bamieh_2006]: https://doi.org/10.21236/ada458858
[research_farhat_1998]: https://doi.org/10.21236/ada361695
[research_farhat_2000]: https://doi.org/10.21236/ada389378
[research_farhat_2001]: https://doi.org/10.21236/ada387498
[research_farhat_amsallem_2011]: https://doi.org/10.21236/ada566361
[research_farkh_ksouri_2021]: https://doi.org/10.32604/csse.2021.014334
[research_farmermg_hansonpw_1976]: https://ntrs.nasa.gov/citations/19760047098
[research_farooq_saeed_2021]: https://doi.org/10.3390/fluids6090332
[research_farsadi_ahmadi_2024]: https://doi.org/10.3390/aerospace11030193
[research_farsadi_ahmadi_2026]: https://doi.org/10.2514/1.j066652
[research_farsadi_rahmanian_2020]: https://doi.org/10.1016/j.jfluidstructs.2019.102812
[research_fatigue_behaviour_1977]: https://doi.org/10.1016/0010-4361(77)90034-9
[research_fattizzo_giulietti_2026]: https://doi.org/10.2514/1.c038348
[research_faure_dumas_2019]: https://doi.org/10.1016/j.apm.2018.12.013
[research_favaro_rylko_2025]: https://doi.org/10.3390/aerospace12060559
[research_favier_maresca_1987]: https://doi.org/10.2514/3.45497
[research_fay_johnstone_1960]: https://doi.org/10.21236/ad0248516
[research_fazeli_stokesgriffin_2022]: https://doi.org/10.1016/j.compstruct.2022.115756
[research_fazelzadeh_azadi_2017]: https://doi.org/10.1108/aeat-11-2015-0241
[research_fazilati_khalafi_2019]: https://doi.org/10.1177/0731684419854800
[research_fazilati_khalafi_2019_b]: https://doi.org/10.1016/j.tws.2019.106287
[research_fearnside_1962]: https://doi.org/10.1108/eb033507
[research_fedorenko_bondarenko_2024]: https://doi.org/10.20535/0203-3771472024307685
[research_fehrs_kaiser_2025]: https://doi.org/10.1007/s13272-025-00856-9
[research_fei_hua_2023]: https://doi.org/10.3390/app13063815
[research_feil_pflumm_2020]: https://doi.org/10.1016/j.compstruct.2020.112755
[research_feldt_herrmann_1974]: https://doi.org/10.1016/0016-0032(74)90123-9
[research_feliubatlle_2016]: https://doi.org/10.1002/rnc.3677
[research_feng_2023]: https://doi.org/10.54254/2753-8818/11/20230408
[research_feng_guo_2023]: https://doi.org/10.2514/1.g007591
[research_feng_wang_2021]: https://doi.org/10.1016/j.ast.2021.106938
[research_ferman_unger_1979]: https://doi.org/10.2514/3.58616
[research_feroskhan_go_2016]: https://doi.org/10.1016/j.ast.2016.01.005
[research_feroskhan_go_2018]: https://doi.org/10.1016/j.ast.2017.11.002
[research_ferraiuolo_scigliano_2019]: https://doi.org/10.1016/j.compstruct.2018.09.024
[research_ferreres_hardier_2017]: https://doi.org/10.1002/rnc.3993
[research_feuer_barmish_1977]: https://doi.org/10.21236/ada044725
[research_fichera_isnardi_2019]: https://doi.org/10.3390/aerospace6020013
[research_figge_1973]: https://doi.org/10.21236/ad0781810
[research_filamentary_plastic_composite_1974]: https://doi.org/10.1016/0010-4361(74)90417-0
[research_filimonov_filimonov_2026]: https://doi.org/10.17587/mau.27.83-96
[research_filippou_kilimtzidis_2024]: https://doi.org/10.3390/aerospace11030180
[research_fina_bisagni_2025]: https://doi.org/10.1007/s00466-024-02589-8
[research_fina_bisagni_2026]: https://doi.org/10.1016/j.compstruct.2026.120323
[research_finck_1978]: https://doi.org/10.21236/adb072483
[research_finigian_kavounas_2024]: https://doi.org/10.3390/aerospace11020133
[research_finkleman_1972]: https://doi.org/10.2514/3.59003
[research_flax_1943]: https://doi.org/10.2514/8.10981
[research_fleming_kushner_1994]: https://doi.org/10.21236/ada281219
[research_flight_delay_2023]: https://doi.org/10.48047/nq.2022.20.17.nq880278
[research_flight_path_2026]: https://doi.org/10.64643/ijirtv12i7-191833-459
[research_flight_performance_1963]: https://doi.org/10.1016/0016-0032(63)90546-5
[research_flight_price_2026]: https://doi.org/10.64388/irev9i11-1717258
[research_flight_test_2016]: https://doi.org/10.21535/dnk59q51
[research_flight_ticket_2020]: https://doi.org/10.37896/jxu14.6/289
[research_flight_ticket_2023]: https://doi.org/10.56726/irjmets-ncascte202226
[research_flightscienceslabincbuffalony_1964]: https://doi.org/10.21236/ad0442900
[research_florancejamesr_heegjennifer_2004]: https://ntrs.nasa.gov/citations/20040066092
[research_flores_bazan_2025]: https://doi.org/10.1002/asjc.70025
[research_flores_mello_1969]: https://doi.org/10.1119/1.1975727
[research_fodor_redfield_1993]: https://doi.org/10.1080/00423119308969018
[research_fontana_piperni_2024]: https://doi.org/10.2514/1.j063533
[research_fonte_ricci_2015]: https://doi.org/10.2514/1.c032995
[research_food_safety_2023]: https://doi.org/10.57263/jmq.02.03.20232
[research_ford_1989]: https://doi.org/10.1108/eb036732
[research_forsman_1983]: https://doi.org/10.21236/ada130832
[research_fortis_fortis_2015]: https://doi.org/10.1504/ijais.2015.072146
[research_fosswejr_whitcombcf_1960]: https://ntrs.nasa.gov/citations/19660024027
[research_fournier_massioni_2022]: https://doi.org/10.2514/1.g006084
[research_fradenburgh_murrill_1973]: https://doi.org/10.21236/ad0771037
[research_fraihat_ajaj_2024]: https://doi.org/10.1017/aer.2024.16
[research_franco_rios_2022]: https://doi.org/10.1002/acs.3399
[research_francois_cooper_2017]: https://doi.org/10.12989/aas.2017.4.2.093
[research_frank_1970]: https://doi.org/10.21236/ad0707438
[research_franklin_innis_1978]: https://doi.org/10.2514/3.58306
[research_franklinja_innisrc_1972]: https://ntrs.nasa.gov/citations/19770026207
[research_franklinjamesa_1993]: https://ntrs.nasa.gov/citations/19940006662
[research_franklinjamesa_stortzmichaelw_1990]: https://ntrs.nasa.gov/citations/19920062696
[research_fraser_petkac_2002]: https://doi.org/10.21236/ada407300
[research_fresconi_celmins_2014]: https://doi.org/10.21236/ada593328
[research_freudingerlawrencec_1989]: https://ntrs.nasa.gov/citations/19900002416
[research_freudingerlawrencec_kehoemichaelw_1990]: https://ntrs.nasa.gov/citations/19900015819
[research_friedmann_1998]: https://doi.org/10.21236/ada351094
[research_friendel_sakamotogm_1978]: https://ntrs.nasa.gov/citations/19790004885
[research_frost_rutherford_1963]: https://doi.org/10.2514/3.1680
[research_fu_yang_2021]: https://doi.org/10.1038/s41598-021-95187-0
[research_fujii_1985]: https://doi.org/10.2322/jjsass1969.33.339
[research_fujioka_suzuki_1994]: https://doi.org/10.1080/00423119408969079
[research_fukuda_kobayashi_1987]: https://doi.org/10.1016/s1474-6670(17)55319-7
[research_fukunaga_1990]: https://doi.org/10.1177/002199839002400504
[research_fukunaga_sekine_1993]: https://doi.org/10.1299/kikaia.59.2343
[research_fukunaga_sekine_1994]: https://doi.org/10.1177/002199839402800802
[research_fuller_1991]: https://doi.org/10.21236/ada248341
[research_fuller_2001]: https://doi.org/10.21236/ada389507
[research_fung_1982]: https://doi.org/10.21236/ada215096
[research_fung_doong_1988]: https://doi.org/10.1016/0263-8223(88)90043-8
[research_furtado_catalanotti_2019]: https://doi.org/10.1016/j.compstruct.2019.111168
[research_furtat_gushchin_2021]: https://doi.org/10.1109/access.2021.3056942
[research_fuzzy_logic_1991]: https://doi.org/10.1109/37.88591
[research_fuzzy_logic_1994]: https://doi.org/10.1109/37.295971
[research_gabel_ricks_1961]: https://doi.org/10.21236/ad0267342
[research_gabrys_steffensen_2019]: https://doi.org/10.1016/j.ifacol.2019.11.281
[research_gainer_1963]: https://doi.org/10.21236/ad0404850
[research_galasso_ciminello_2024]: https://doi.org/10.3390/s24165216
[research_galffy_bock_2019]: https://doi.org/10.1016/j.conengprac.2019.03.006
[research_galiana_moradi_2024]: https://doi.org/10.1177/14759217241247766
[research_galicki_2016]: https://doi.org/10.1002/rnc.3591
[research_gallagher_1971]: https://doi.org/10.2514/3.59189
[research_gamagedara_lee_2024]: https://doi.org/10.1016/j.conengprac.2023.105791
[research_gamon_mahone_1975]: https://doi.org/10.21236/ada022146
[research_ganesh_manoharan_2016]: https://doi.org/10.5958/2249-7315.2016.01058.3
[research_gao_cai_2016]: https://doi.org/10.1016/j.cja.2016.06.014
[research_gao_gao_2019]: https://doi.org/10.1109/access.2019.2917316
[research_gao_jiang_2025]: https://doi.org/10.1017/aer.2025.41
[research_gao_li_2020]: https://doi.org/10.3390/en13071740
[research_gao_liu_2024]: https://doi.org/10.1016/j.ast.2024.109671
[research_gao_ma_2021]: https://doi.org/10.32604/sdhm.2021.013737
[research_gao_wang_2021]: https://doi.org/10.1002/oca.2751
[research_gao_wu_2017]: https://doi.org/10.1177/1475921717717312
[research_garabedianpr_1979]: https://ntrs.nasa.gov/citations/19790011863
[research_garciahernandez_cuernorejado_2017]: https://doi.org/10.1109/access.2017.2758903
[research_garciarodriguez_martinezperez_2024]: https://doi.org/10.13053/cys-28-2-4354
[research_gargsanjay_schmidtdavidk_1988]: https://ntrs.nasa.gov/citations/19880063045
[research_garmendia_mavris_2016]: https://doi.org/10.2514/1.c033184
[research_garner_wu_2023]: https://doi.org/10.1007/s00158-023-03678-7
[research_garrard_low_1990]: https://doi.org/10.21236/ada231588
[research_garrickie_rubinowsi_1946]: https://ntrs.nasa.gov/citations/19930081835
[research_garrickie_rubinowsi_1946_b]: https://ntrs.nasa.gov/citations/19930090942
[research_garrisoncharliec_hacskayloandrew_1947]: https://ntrs.nasa.gov/citations/20050031172
[research_gaurav_sekou_2023]: https://doi.org/10.1051/e3sconf/202344606005
[research_gavra_vankampen_2024]: https://doi.org/10.2514/1.g008112
[research_ge_zhang_2022]: https://doi.org/10.1002/aic.17909
[research_gea_chow_1992]: https://doi.org/10.2514/3.46186
[research_gearhart_1962]: https://doi.org/10.21236/ad0405110
[research_gebhard_1953]: https://doi.org/10.21236/ad0015832
[research_gebhard_wang_2026]: https://doi.org/10.1080/27525783.2026.2618294
[research_geisler_junker_2024]: https://doi.org/10.1016/j.probengmech.2024.103618
[research_gelos_laura_1990]: https://doi.org/10.1016/0003-682x(90)90014-l
[research_generaldynamicsastronauticssandiegoca_1961]: https://doi.org/10.21236/ad0843112
[research_generaldynamicsastronauticssandiegoca_1961_b]: https://doi.org/10.21236/ad0843200
[research_generaldynamicsastronauticssandiegoca_1962]: https://doi.org/10.21236/ad0852659
[research_geng_zhao_2026]: https://doi.org/10.1016/j.addma.2026.105207
[research_geoghegan_giannelis_2020]: https://doi.org/10.3390/fluids5020046
[research_gerdes_hynes_1972]: https://doi.org/10.4050/jahs.17.47
[research_gerken_1979]: https://doi.org/10.21236/ada132587
[research_ghaderi_mojallali_2024]: https://doi.org/10.1002/rnc.7573
[research_ghalandari_mahariq_2022]: https://doi.org/10.32604/cmc.2022.020884
[research_ghasemikaram_mazidi_2021]: https://doi.org/10.1142/s021945542250016x
[research_ghayour_mani_2018]: https://doi.org/10.1108/aeat-07-2018-0194
[research_ghazi_alhazmi_2022]: https://doi.org/10.1080/10618562.2022.2138863
[research_ghazi_botez_2020]: https://doi.org/10.2514/1.i010791
[research_ghosh_2024]: https://doi.org/10.1016/j.mlwa.2024.100537
[research_giannakeas_sharifkhodaei_2022]: https://doi.org/10.1177/14759217221095415
[research_gibson_1999]: https://doi.org/10.21236/ada386878
[research_giese_reich_1996]: https://doi.org/10.21236/ada399629
[research_gilbert_schmidt_1984]: https://doi.org/10.2514/3.8566
[research_gilbert_schneider_1981]: https://doi.org/10.1177/002199838101500106
[research_gilbertmichaelg_1987]: https://ntrs.nasa.gov/citations/19870009427
[research_giles_1972]: https://doi.org/10.2514/3.58942
[research_gill_1995]: https://doi.org/10.21236/ada305293
[research_giurgiutiu_pomirleanu_2000]: https://doi.org/10.21236/ada384331
[research_glbbings_1969]: https://doi.org/10.2514/3.48096
[research_gleadall_2021]: https://doi.org/10.1016/j.addma.2021.102109
[research_glezer_leonard_2012]: https://doi.org/10.21236/ada564094
[research_glock_canal_2015]: https://doi.org/10.1016/j.compscitech.2015.04.009
[research_gloss_washburn_1978]: https://doi.org/10.2514/3.58347
[research_glossbb_washburnke_1977]: https://ntrs.nasa.gov/citations/19770060346
[research_glynn_iglehart_1985]: https://doi.org/10.21236/ada161435
[research_gnilenko_2024]: https://doi.org/10.15588/1607-3274-2024-4-9
[research_godwin_frazier_1964]: https://doi.org/10.21236/ad0613504
[research_goel_roy_2021]: https://doi.org/10.1109/lcsys.2020.3045086
[research_goerigk_lendl_2021]: https://doi.org/10.5802/ojmo.5
[research_goizueta_wynn_2022]: https://doi.org/10.2514/1.j062050
[research_goizueta_wynn_2022_b]: https://doi.org/10.2514/1.c036710
[research_goland_1945]: https://doi.org/10.1115/1.4009489
[research_golmirzaee_wood_2026]: https://doi.org/10.1186/s42774-025-00222-7
[research_golombek_bustamante_2026]: https://doi.org/10.1007/s13272-026-00996-6
[research_gonabadi_oila_2021]: https://doi.org/10.1016/j.compstruct.2021.114679
[research_gong_he_2026]: https://doi.org/10.1016/j.probengmech.2026.103892
[research_gong_wang_2019]: https://doi.org/10.1007/s11071-019-04834-9
[research_gong_wang_2019_b]: https://doi.org/10.1177/0020294019830434
[research_gong_xiong_2016]: https://doi.org/10.1002/stc.1912
[research_gong_xu_2024]: https://doi.org/10.1016/j.ast.2024.108875
[research_gonzales_1969]: https://doi.org/10.1007/bf00145742
[research_gonzalez_silvestre_2020]: https://doi.org/10.2514/1.j058692
[research_gonzalezmontijo_vanness_2026]: https://doi.org/10.1016/j.marstruc.2025.103924
[research_goodrichkennethh_sliwastevenm_1989]: https://ntrs.nasa.gov/citations/19890014097
[research_goodyear_lee_1981]: https://doi.org/10.21236/ada097625
[research_goodyearaerospacecorpakronoh_1958]: https://doi.org/10.21236/ad0215773
[research_goradiash_bobbittpj_1989]: https://ntrs.nasa.gov/citations/19910014825
[research_goranson_1997]: https://doi.org/10.21236/ada337932
[research_gorman_singhal_1993]: https://doi.org/10.1006/jsvi.1993.1135
[research_gospodarczyk_2015]: https://doi.org/10.1016/j.cad.2014.11.009
[research_gottlieb_1981]: https://doi.org/10.21236/ada097989
[research_gottumukkula_engell_2021]: https://doi.org/10.3390/pr9101800
[research_gottzein_cramer_1975]: https://doi.org/10.1080/00423117508968492
[research_goucem_khiri_2023]: https://doi.org/10.15866/irease.v16i5.24129
[research_goulet_kiureghian_2015]: https://doi.org/10.1016/j.strusafe.2014.08.001
[research_govindaraj_rynaski_1979]: https://doi.org/10.21236/ada074092
[research_govoni_cristofaro_2023]: https://doi.org/10.1109/lcsys.2023.3324565
[research_gowd_2016]: https://doi.org/10.18186/jte.83892
[research_grace_1992]: https://doi.org/10.3366/more.1992.29.1.15
[research_graffi_grecchi_1973]: https://doi.org/10.1103/physrevd.8.3487
[research_graftonsb_gilberwp_1982]: https://ntrs.nasa.gov/citations/19820055564
[research_grant_stol_2015]: https://doi.org/10.2514/1.g000826
[research_granthamwd_nguyenlt_1976]: https://ntrs.nasa.gov/citations/19770011064
[research_graphite_epoxy_composite_1981]: https://doi.org/10.1016/0010-4361(81)90532-2
[research_gratton_1967]: https://doi.org/10.21236/ad0834469
[research_gratton_donahue_1966]: https://doi.org/10.21236/ad0847720
[research_grauer_morelli_2023]: https://doi.org/10.2514/1.c037583
[research_grauerjareda_bouchermatthewj_2017]: https://ntrs.nasa.gov/citations/20170001227
[research_graves_sawicki_1994]: https://doi.org/10.1016/0263-8223(94)90088-4
[research_gray_kennedy_2025]: https://doi.org/10.1007/s00158-025-04181-x
[research_gray_mei_1993]: https://doi.org/10.2514/3.49051
[research_gray_riso_2023]: https://doi.org/10.2514/1.j062127
[research_green_1987]: https://doi.org/10.2514/3.45525
[research_greenbergharry_sternfieldleonard_1944]: https://ntrs.nasa.gov/citations/19960024284
[research_greene_1928]: https://doi.org/10.1115/1.4058514
[research_greene_1955]: https://doi.org/10.21236/ad0086878
[research_greene_1956]: https://doi.org/10.21236/ad0092484
[research_greene_1957]: https://doi.org/10.21236/ad0132012
[research_greenhalgh_pastore_1993]: https://doi.org/10.1016/0956-7143(93)90004-r
[research_greenhall_zerkle_2022]: https://doi.org/10.1016/j.mlwa.2022.100391
[research_greenja_1986]: https://ntrs.nasa.gov/citations/19860054140
[research_grenestedt_1989]: https://doi.org/10.1016/0263-8223(89)90076-7
[research_greszczuk_chao_1975]: https://doi.org/10.21236/ada012269
[research_griffin_bellaire_1968]: https://doi.org/10.21236/ad0850270
[research_griffin_eastep_1982]: https://doi.org/10.2514/3.61570
[research_griffin_haerter_1983]: https://doi.org/10.21236/ada133188
[research_griffinbrianjoseph_burkenjohnj_2010]: https://ntrs.nasa.gov/citations/20100037212
[research_griffincharlesf_harvillwilliame_1988]: https://ntrs.nasa.gov/citations/19910019939
[research_griffis_masumura_1981]: https://doi.org/10.1177/002199838101500503
[research_grifo_gulizzi_2023]: https://doi.org/10.1016/j.compstruct.2023.117315
[research_grigolyuk_kulikov_1990]: https://doi.org/10.1007/bf00851843
[research_groh_wu_2022]: https://doi.org/10.2514/1.j061755
[research_gross_clark_2017]: https://doi.org/10.2514/1.i010471
[research_grossschmidt_pahapill_1995]: https://doi.org/10.3176/eng.1995.1.03
[research_gruenwald_yucelen_2020]: https://doi.org/10.1002/acs.3095
[research_gssssv_2020]: https://doi.org/10.5373/jardcs/v12sp4/20201597
[research_gu_ducvo_2023]: https://doi.org/10.2514/1.c036702
[research_gu_hong_2020]: https://doi.org/10.1088/1742-6596/1600/1/012013
[research_gu_taghipour_2022]: https://doi.org/10.1016/j.compstruct.2022.116151
[research_gu_zhou_2020]: https://doi.org/10.2514/1.c035833
[research_gu_zhou_2022]: https://doi.org/10.2514/1.c036508
[research_guan_li_2026]: https://doi.org/10.1016/j.ast.2026.112192
[research_guderley_1956]: https://doi.org/10.2514/8.3697
[research_guillen_abboud_2022]: https://doi.org/10.1016/j.nucengdes.2022.111737
[research_guimaraes_castro_2019]: https://doi.org/10.2514/1.j057282
[research_guimaraes_silva_2020]: https://doi.org/10.2514/1.j059106
[research_guinnwileya_1984]: https://ntrs.nasa.gov/citations/19870008278
[research_guinnwileya_risingjerryj_1984]: https://ntrs.nasa.gov/citations/19870008280
[research_guinnwileya_willeycraigs_1983]: https://ntrs.nasa.gov/citations/19870008279
[research_gunnink_1988]: https://doi.org/10.1016/0263-8223(88)90062-1
[research_guo_2021]: https://doi.org/10.1088/1742-6596/1877/1/012019
[research_guo_2021_b]: https://doi.org/10.1088/1742-6596/1877/1/012022
[research_guo_bai_2017]: https://doi.org/10.1360/n092016-00362
[research_guo_guan_1993]: https://doi.org/10.1080/00423119308969025
[research_guo_hou_2017]: https://doi.org/10.1109/access.2017.2743059
[research_guo_jin_2023]: https://doi.org/10.1016/j.probengmech.2023.103538
[research_guo_jing_2017]: https://doi.org/10.1016/j.ast.2017.08.008
[research_guo_li_2021]: https://doi.org/10.1007/s00158-021-02888-1
[research_guo_liu_2026]: https://doi.org/10.1016/j.marstruc.2026.104127
[research_guo_liu_2026_b]: https://doi.org/10.1007/s42401-026-00489-8
[research_guo_wang_1988]: https://doi.org/10.21236/ada191553
[research_guo_wang_2025]: https://doi.org/10.1016/j.ast.2025.109966
[research_guo_zhang_2022]: https://doi.org/10.32604/cmes.2022.020638
[research_guo_zhou_2020]: https://doi.org/10.3390/electronics9020364
[research_gupta_1998]: https://doi.org/10.21236/ada397678
[research_gupta_2023]: https://doi.org/10.61653/joast.v68i4.2016.368
[research_gurdal_2002]: https://doi.org/10.21236/ada402571
[research_gurdal_haftka_1999]: https://doi.org/10.21236/ada387245
[research_gurleyjrjr_ruhlincl_1962]: https://ntrs.nasa.gov/citations/19660025705
[research_guruswamy_2019]: https://doi.org/10.1016/j.ifacsc.2019.100057
[research_guruswamy_goorjian_1987]: https://doi.org/10.2514/3.45508
[research_guruswamy_tu_1989]: https://doi.org/10.2514/3.45820
[research_guy_rousselotpailley_1995]: https://doi.org/10.1051/animres:19950308
[research_gwin_1976]: https://doi.org/10.2514/3.58668
[research_gwinlb_1974]: https://ntrs.nasa.gov/citations/19740045423
[research_haas_chopra_1988]: https://doi.org/10.2514/3.45684
[research_haas_chopra_1990]: https://doi.org/10.2514/3.45937
[research_hac_1987]: https://doi.org/10.1080/00423118708968870
[research_hac_1992]: https://doi.org/10.1080/00423119208969008
[research_had_ruzicka_2016]: https://doi.org/10.1016/j.compstruct.2015.09.009
[research_hadidoolabi_ansarian_2017]: https://doi.org/10.24200/sci.2017.4246
[research_hadidoolabi_ansarian_2018]: https://doi.org/10.1007/s40430-018-1021-z
[research_haeri_fadaee_2016]: https://doi.org/10.1016/j.compstruct.2016.04.013
[research_haftka_1977]: https://doi.org/10.2514/3.7400
[research_haftmann_debbeler_1988]: https://doi.org/10.2514/3.45707
[research_hagnell_langbeck_2016]: https://doi.org/10.1016/j.compstruct.2016.06.032
[research_hague_1927]: https://doi.org/10.5840/thought19272135
[research_hahn_haupt_2022]: https://doi.org/10.1007/s13272-022-00586-2
[research_hahn_kim_1976]: https://doi.org/10.1177/002199837601000205
[research_hai_2022]: https://doi.org/10.14445/22315381/ijett-v70i11p231
[research_halder_damodaran_2020]: https://doi.org/10.2514/1.j059027
[research_halder_das_2020]: https://doi.org/10.1080/00207179.2020.1764110
[research_haley_soloway_2022]: https://doi.org/10.1109/mcs.2022.3171473
[research_hall_1971]: https://doi.org/10.2514/3.59106
[research_hall_weingarten_1974]: https://doi.org/10.2514/3.60377
[research_hallauer_jr_1983]: https://doi.org/10.21236/ada148333
[research_hallissyjb_ayerstg_1977]: https://ntrs.nasa.gov/citations/19770026171
[research_hamada_saitoh_2019]: https://doi.org/10.1016/j.ifacol.2019.11.125
[research_hamiltonbriank_petersjamesr_1989]: https://ntrs.nasa.gov/citations/19890015786
[research_hamissi_bouzid_2019]: https://doi.org/10.1016/j.ifacol.2019.11.260
[research_hammer_bright_1998]: https://doi.org/10.21236/ada359476
[research_hamza_akram_2026]: https://doi.org/10.1016/j.amf.2026.200334
[research_han_cheng_2023]: https://doi.org/10.1016/j.neucom.2023.126789
[research_han_glower_1985]: https://doi.org/10.21236/ada152209
[research_han_guo_2022]: https://doi.org/10.1016/j.supflu.2022.105643
[research_han_pei_2026]: https://doi.org/10.1109/maes.2025.3566023
[research_han_yang_2024]: https://doi.org/10.1109/access.2024.3411015
[research_han_yu_2019]: https://doi.org/10.2514/1.c035282
[research_han_zhang_2022]: https://doi.org/10.1016/j.buildenv.2022.109362
[research_hanagud_craig_1989]: https://doi.org/10.1177/002199838902300502
[research_hanazaki_yamazaki_2024]: https://doi.org/10.3390/aerospace11010064
[research_hancock_1971]: https://doi.org/10.2514/3.59157
[research_hancock_1972]: https://doi.org/10.1017/s0001924000044055
[research_hancock_1992]: https://doi.org/10.1017/s0001924000050442
[research_hancockregis_fullertongordon_1992]: https://ntrs.nasa.gov/citations/19930054849
[research_hanman_yao_2025]: https://doi.org/10.3390/fluids10020027
[research_hansen_duan_2022]: https://doi.org/10.2514/1.g006577
[research_hanson_stengel_1984]: https://doi.org/10.2514/3.8567
[research_hansoncurt_schaeferjacob_2011]: https://ntrs.nasa.gov/citations/20110023802
[research_hansongd_stengelrf_1981]: https://ntrs.nasa.gov/citations/19810059678
[research_hansongd_stengelrf_1983]: https://ntrs.nasa.gov/citations/19830035279
[research_hao_du_2022]: https://doi.org/10.1142/s0219455423501225
[research_hao_ma_2023]: https://doi.org/10.1016/j.ast.2023.108323
[research_hao_yu_2026]: https://doi.org/10.1016/j.tws.2026.114867
[research_harno_kim_2020]: https://doi.org/10.1016/j.ast.2020.105859
[research_harper_robertp_1955]: https://doi.org/10.21236/ad0092496
[research_harpur_1968]: https://doi.org/10.2514/3.43926
[research_harriscd_1974]: https://ntrs.nasa.gov/citations/19830002756
[research_harriscd_1974_b]: https://ntrs.nasa.gov/citations/19830002761
[research_harry_trobaugh_1966]: https://doi.org/10.21236/ad0641246
[research_hart_1956]: https://doi.org/10.21236/ad0108104
[research_hartini_bachtiar_2026]: https://doi.org/10.28989/vortex.v7i1.3819
[research_harvillwe_kizerja_1976]: https://ntrs.nasa.gov/citations/19770004089
[research_hashiiwendyn_thompsonrandolphc_2018]: https://ntrs.nasa.gov/citations/20180004483
[research_hassan_selvaratnam_2024]: https://doi.org/10.1109/ojcsys.2024.3487408
[research_hatake_1985]: https://doi.org/10.1299/kikaic.51.1897
[research_hatake_1986]: https://doi.org/10.1299/jsme1958.29.1225
[research_haviv_1989]: https://doi.org/10.1137/0610022
[research_hayase_1974]: https://doi.org/10.21236/ada002866
[research_hayase_1974_b]: https://doi.org/10.21236/ada002862
[research_hayashi_1949]: https://doi.org/10.2534/jjasnaoe1903.1949.85
[research_hayashi_1988]: https://doi.org/10.1080/00423118808969254
[research_he_tan_2020]: https://doi.org/10.1109/access.2020.3035436
[research_he_wang_2023]: https://doi.org/10.1155/2023/1711088
[research_hebbar_pashilkar_2016]: https://doi.org/10.14429/dsj.66.9196
[research_heckl_lyon_1962]: https://doi.org/10.21236/ad0290798
[research_heegjennifer_2006]: https://ntrs.nasa.gov/citations/20060018311
[research_heegjennifer_spaincharlesv_2004]: https://ntrs.nasa.gov/citations/20040068163
[research_heegjennifer_spaincharlesv_2005]: https://ntrs.nasa.gov/citations/20050203672
[research_heersink_sylla_2022]: https://doi.org/10.1109/lcsys.2021.3119258
[research_heinrich_vogt_2022]: https://doi.org/10.2514/1.g006412
[research_helgo_2023]: https://doi.org/10.53759/9852/jrs202301009
[research_heltsley_cline_1979]: https://doi.org/10.21236/ada068328
[research_heltsley_crosswy_1981]: https://doi.org/10.21236/ada103929
[research_hemsch_1989]: https://doi.org/10.2514/3.45723
[research_hemsch_nielsen_1983]: https://doi.org/10.2514/3.25606
[research_henriquezhuecas_white_2022]: https://doi.org/10.4050/jahs.67.032007
[research_henry_1961]: https://doi.org/10.21236/ad0273328
[research_henschel_chetty_1989]: https://doi.org/10.2514/3.20415
[research_heplerak_zeckh_1978]: https://ntrs.nasa.gov/citations/19780022197
[research_hermanarediess_1976]: https://ntrs.nasa.gov/citations/19760024047
[research_hermanutz_hornung_2020]: https://doi.org/10.3390/aerospace7040045
[research_herrington_zahed_2023]: https://doi.org/10.1142/s2301385024500080
[research_herrmann_benasher_2016]: https://doi.org/10.2514/1.c033517
[research_herrmanng_nematnassers_1966]: https://ntrs.nasa.gov/citations/19660053477
[research_hertztj_shirkmh_1982]: https://ntrs.nasa.gov/citations/19820035536
[research_hervin_fromme_2022]: https://doi.org/10.1177/14759217221133284
[research_hess_1984]: https://doi.org/10.2514/3.56363
[research_hess_1989]: https://doi.org/10.2514/3.20483
[research_hess_1991]: https://doi.org/10.1016/0003-6870(91)90114-w
[research_hess_2016]: https://doi.org/10.1016/j.ifacol.2016.12.206
[research_hess_2018]: https://doi.org/10.2514/1.c034596
[research_hess_peng_2018]: https://doi.org/10.2514/1.c034497
[research_hess_seidel_1989]: https://doi.org/10.2514/3.45810
[research_hess_sunyoto_1985]: https://doi.org/10.2514/3.20003
[research_hicksjohnw_cooperjamesmjr_1987]: https://ntrs.nasa.gov/citations/19870012475
[research_hicksjohnw_huckabinethomas_1989]: https://ntrs.nasa.gov/citations/19910019863
[research_hicksjohnw_kaniajan_1987]: https://ntrs.nasa.gov/citations/19870035128
[research_hicksjohnw_mathenyneilw_1987]: https://ntrs.nasa.gov/citations/19870017473
[research_hicksjohnw_mathenyneilw_1989]: https://ntrs.nasa.gov/citations/19890061478
[research_hicksjohnw_moultonbryanj_1988]: https://ntrs.nasa.gov/citations/19880051510
[research_hicksjohnw_petersenkevinl_1988]: https://ntrs.nasa.gov/citations/19890004053
[research_hicksjohnw_petersenkevinl_1989]: https://ntrs.nasa.gov/citations/19900001550
[research_higgins_shomber_1965]: https://doi.org/10.2514/3.43684
[research_higuchi_saitoh_1993]: https://doi.org/10.1080/00423119308969039
[research_hildebrandfrancisb_reissnereric_1944]: https://ntrs.nasa.gov/citations/19930084742
[research_hilger_ritter_2021]: https://doi.org/10.3390/aerospace8100308
[research_hill_1987]: https://doi.org/10.21236/ada186949
[research_hill_2001]: https://doi.org/10.21236/ada390033
[research_himeda_naka_2019]: https://doi.org/10.1299/jsmefed.2019.os1-21
[research_hinchliffe_qin_2017]: https://doi.org/10.2514/1.j055319
[research_hirai_kline_1973]: https://doi.org/10.1177/002199837300700202
[research_hirai_satoh_1980]: https://doi.org/10.1109/tac.1980.1102355
[research_hirato_shen_2019]: https://doi.org/10.2514/1.c035124
[research_hirsch_mccormick_1966]: https://doi.org/10.2514/3.43778
[research_hisada_minakuchi_2020]: https://doi.org/10.1016/j.compstruct.2020.112792
[research_hitch_1978]: https://doi.org/10.2514/3.58464
[research_hitzel_2017]: https://doi.org/10.2514/1.c034025
[research_hitzel_osterhuber_2018]: https://doi.org/10.2514/1.c034473
[research_hiyama_1974]: https://doi.org/10.21236/ada002867
[research_hiyama_1974_b]: https://doi.org/10.21236/ada002868
[research_hobbs_mote_2023]: https://doi.org/10.1109/mcs.2023.3234380
[research_hodges_2004]: https://doi.org/10.21236/ada424568
[research_hodgins_freeman_2025]: https://doi.org/10.1080/00207179.2025.2513674
[research_hodgkinson_2017]: https://doi.org/10.4050/jahs.62.047001
[research_hodgkinson_lamanna_1976]: https://doi.org/10.1017/s0001924000033510
[research_hofmann_kezer_1962]: https://doi.org/10.21236/ad0403433
[research_hogan_rinde_1978]: https://doi.org/10.21236/ada062030
[research_hoh_mitchell_1983]: https://doi.org/10.21236/ada132857
[research_holst_1988]: https://doi.org/10.2514/3.45706
[research_holst_brown_1983]: https://doi.org/10.2514/3.8069
[research_honeycomb_laminate_composite_1979]: https://doi.org/10.1016/0010-4361(79)90475-0
[research_hong_cheong_1993]: https://doi.org/10.1016/0013-7944(93)90174-q
[research_hong_kim_2024]: https://doi.org/10.2514/1.c037715
[research_hong_ko_2015]: https://doi.org/10.9728/dcs.2015.16.1.123
[research_hongyan_xiaoyong_2026]: https://doi.org/10.1109/access.2026.3692889
[research_hoogervorst_elham_2017]: https://doi.org/10.1016/j.ast.2017.02.012
[research_hoover_shen_2019]: https://doi.org/10.2514/1.c035263
[research_hope_kunz_2019]: https://doi.org/10.2514/1.j057456
[research_hopkinsej_yeesc_1977]: https://ntrs.nasa.gov/citations/19770014154
[research_hopwood_gresham_2023]: https://doi.org/10.2514/1.g007016
[research_horowitz_golubev_1980]: https://doi.org/10.21236/ada082424
[research_horsburgh_1911]: https://doi.org/10.1017/s0013091500033976
[research_horton_mayers_1965]: https://doi.org/10.21236/ad0622585
[research_hortsen_boer_1983]: https://doi.org/10.21236/ada130488
[research_hoseini_hodges_2019]: https://doi.org/10.2514/1.c035098
[research_housnerjm_steinm_1974]: https://ntrs.nasa.gov/citations/19740024243
[research_houtman_timme_2023]: https://doi.org/10.1017/flo.2023.8
[research_houzibe_chaki_2026]: https://doi.org/10.1177/14759217261453871
[research_how_2004]: https://doi.org/10.21236/ada420937
[research_howard_oleary_1994]: https://doi.org/10.2514/3.46578
[research_howdyshell_trovillion_1998]: https://doi.org/10.21236/ada354825
[research_hoyos_candelobecerra_2025]: https://doi.org/10.3390/en18225889
[research_hozic_thore_2023]: https://doi.org/10.1016/j.compstruct.2023.117336
[research_hu_1984]: https://doi.org/10.1016/0045-7949(84)90204-9
[research_hu_2022]: https://doi.org/10.3390/aerospace9030154
[research_hu_an_2025]: https://doi.org/10.1063/5.0258928
[research_hu_qiu_2026]: https://doi.org/10.1080/13504851.2026.2681706
[research_hu_yang_2016]: https://doi.org/10.1016/j.jsv.2015.11.043
[research_hua_wang_2025]: https://doi.org/10.3390/aerospace12040327
[research_huang_gu_2025]: https://doi.org/10.3390/aerospace12121091
[research_huang_li_2026]: https://doi.org/10.2514/1.c038842
[research_huang_pool_2017]: https://doi.org/10.1016/j.ifacol.2017.08.837
[research_huang_wang_2016]: https://doi.org/10.1016/j.compstruct.2016.06.043
[research_huang_wang_2024]: https://doi.org/10.1007/s00158-024-03809-8
[research_huang_yang_2018]: https://doi.org/10.1016/j.cja.2017.12.014
[research_huang_yang_2019]: https://doi.org/10.2514/1.j058211
[research_huang_yu_2022]: https://doi.org/10.2514/1.j060923
[research_huang_zhen_2023]: https://doi.org/10.1109/tac.2023.3241282
[research_hubener_luckner_2026]: https://doi.org/10.1007/s13272-025-00930-2
[research_hubler_nissle_2016]: https://doi.org/10.1007/s13272-016-0209-0
[research_huff_ww_1949]: https://doi.org/10.21236/ad0035641
[research_huffmanjk_1975]: https://ntrs.nasa.gov/citations/19750019955
[research_hui_1986]: https://doi.org/10.1016/0020-7683(86)90100-9
[research_huiping_yutian_1989]: https://doi.org/10.1016/b978-0-08-040185-0.50024-5
[research_human_supervisory_2015]: https://doi.org/10.1109/mcs.2015.2471056
[research_hummel_oelker_1994]: https://doi.org/10.2514/3.46573
[research_humphreysjennings_lappas_2020]: https://doi.org/10.3390/aerospace7050051
[research_hunn_1953]: https://doi.org/10.1017/s0368393100131128
[research_hunter_2003]: https://doi.org/10.21236/ada413499
[research_huo_duan_2021]: https://doi.org/10.1142/s2301385021410053
[research_hurley_1975]: https://doi.org/10.2514/3.49684
[research_hussain_anjum_2015]: https://doi.org/10.3920/qas2013.0358
[research_hutchinson_2014]: https://doi.org/10.21236/ada607283
[research_hybrid_composite_1978]: https://doi.org/10.1016/0010-4361(78)90462-7
[research_iannelli_marcos_2017]: https://doi.org/10.1002/rnc.3878
[research_iannelli_marcos_2018]: https://doi.org/10.2514/1.g003165
[research_ibrahim_2026]: https://doi.org/10.22161/ijebm.10.2.9
[research_ibren_sulaeman_2020]: https://doi.org/10.37934/cfdl.12.4.7989
[research_ide_landman_2025]: https://doi.org/10.1108/ijius-11-2024-0335
[research_ignatyev_khrabrov_2018]: https://doi.org/10.3390/aerospace5010026
[research_ijaz_hamayun_2019]: https://doi.org/10.1007/s12555-017-0399-1
[research_ijaz_hamayun_2019_b]: https://doi.org/10.1177/0142331219835589
[research_ikehata_1995]: https://doi.org/10.1088/0266-5611/11/1/009
[research_ilcewiczlb_walkerth_1991]: https://ntrs.nasa.gov/citations/19940028357
[research_iliffkw_mainere_1978]: https://ntrs.nasa.gov/citations/19780010132
[research_iliffkw_mainere_1981]: https://ntrs.nasa.gov/citations/19820030345
[research_im_kong_2025]: https://doi.org/10.1109/access.2025.3526769
[research_imani_montazerigh_2019]: https://doi.org/10.1007/s12555-018-0803-5
[research_immersion_and_2026]: https://doi.org/10.66967/jaics.2026.v2i104
[research_implementation_of_2023]: https://doi.org/10.36652/0042-4633-2023-102-1-24-29
[research_inan_aliskan_2025]: https://doi.org/10.29130/dubited.1595224
[research_inger_1983]: https://doi.org/10.21236/ada123389
[research_ingramwc_yiplp_1986]: https://ntrs.nasa.gov/citations/19870026764
[research_interlaminar_shear_1992]: https://doi.org/10.1016/0010-4361(92)90207-b
[research_introduction_to_2017]: https://doi.org/10.2514/1.c034808
[research_invernizzi_lovera_2018]: https://doi.org/10.1016/j.automatica.2018.05.024
[research_ioannis_ioannis_2026]: https://doi.org/10.70322/dav.2026.10005
[research_iovnovich_nahom_2018]: https://doi.org/10.2514/1.c034716
[research_irvine_1968]: https://doi.org/10.21236/ad0680316
[research_iryani_kadir_2019]: https://doi.org/10.5373/jardcs/v11sp11/20193066
[research_ishii_2023]: https://doi.org/10.1587/comex.2022xbl0174
[research_ishmaelsd_wierzbanowskit_1985]: https://ntrs.nasa.gov/citations/19860060204
[research_ishmaelstephend_smithrogerse_1990]: https://ntrs.nasa.gov/citations/19920033428
[research_isogai_1979]: https://doi.org/10.2514/3.61226
[research_isogai_1981]: https://doi.org/10.2514/3.7853
[research_isogai_1988]: https://doi.org/10.6089/jscm.14.96
[research_isogai_1989]: https://doi.org/10.2514/3.45883
[research_isogai_1992]: https://doi.org/10.1016/0889-9746(92)90017-w
[research_ito_iwashita_2017]: https://doi.org/10.2534/jjasnaoe.25.63
[research_ivler_truong_2022]: https://doi.org/10.4050/jahs.67.012002
[research_izadbakhsh_kheirkhahan_2018]: https://doi.org/10.1177/1077546318802694
[research_izadbakhsh_khorashadizadeh_2019]: https://doi.org/10.1016/j.compeleceng.2019.07.001
[research_jacobs_1964]: https://doi.org/10.21236/ad0607245
[research_jacobson_1952]: https://doi.org/10.21236/ad0029208
[research_jacobson_joshi_1977]: https://doi.org/10.2514/3.44591
[research_jacobson_joshi_1978]: https://doi.org/10.2514/3.58351
[research_jacome_elham_2018]: https://doi.org/10.1007/s13272-018-0342-z
[research_jaeger_hendry_1959]: https://doi.org/10.1680/iicep.1959.12063
[research_jafari_mashadi_2022]: https://doi.org/10.1080/00423114.2022.2056490
[research_jaffarsyedmohamedali_shahzatulsakinahbintiharon_2021]: https://doi.org/10.37934/cfdl.13.11.7886
[research_jagana_rajagopalan_2026]: https://doi.org/10.1002/aic.70222
[research_jajarmi_hajipour_2016]: https://doi.org/10.1002/asjc.1371
[research_jalalnezhad_2026]: https://doi.org/10.1007/s40430-025-06274-6
[research_jamesafranklin_1993]: https://ntrs.nasa.gov/citations/19940008824
[research_jamesmluckring_2003]: https://ntrs.nasa.gov/citations/20040010871
[research_janardhan_grandhi_2003]: https://doi.org/10.21236/ada417106
[research_janecek_1986]: https://doi.org/10.21236/ada179141
[research_jang_ahn_2015]: https://doi.org/10.3390/s151128472
[research_jang_ahn_2022]: https://doi.org/10.3390/app12199436
[research_jaredagrauer_2018]: https://ntrs.nasa.gov/citations/20190000878
[research_jarrellrelliott_1976]: https://ntrs.nasa.gov/citations/19770045950
[research_jarviscr_1967]: https://ntrs.nasa.gov/citations/19670041319
[research_jarviscr_1975]: https://ntrs.nasa.gov/citations/19750010174
[research_jarviscr_szalaikj_1981]: https://ntrs.nasa.gov/citations/19810010480
[research_jategaonkar_2023]: https://doi.org/10.61653/joast.v57i1.2005.674
[research_jategaonkar_thielecke_1994]: https://doi.org/10.2514/3.46523
[research_jegleydawnc_bushharoldg_1997]: https://ntrs.nasa.gov/citations/19970022698
[research_jegleydawnc_bushharoldg_2001]: https://ntrs.nasa.gov/citations/20010047392
[research_jegleydawnc_bushharoldg_2001_b]: https://ntrs.nasa.gov/citations/20030012585
[research_jegleydawnc_lovejoyandrewe_2001]: https://ntrs.nasa.gov/citations/20010022369
[research_jegleydawnc_wijayratnedulnathd_2004]: https://ntrs.nasa.gov/citations/20040200977
[research_jelliott_1977]: https://ntrs.nasa.gov/citations/19780028448
[research_jelovica_cai_2022]: https://doi.org/10.1080/0305215x.2022.2147518
[research_jeng_payne_1995]: https://doi.org/10.2514/3.46724
[research_jenksge_henryhf_1977]: https://ntrs.nasa.gov/citations/19770014139
[research_jenney_schreadley_1982]: https://doi.org/10.21236/ada117244
[research_jenney_schreadley_1984]: https://doi.org/10.21236/ada144283
[research_jensen_crawley_1982]: https://doi.org/10.1177/073168448200100305
[research_jensen_crawley_1984]: https://doi.org/10.2514/3.48463
[research_jensen_falby_1966]: https://doi.org/10.21236/ad0486295
[research_jeon_choi_2025]: https://doi.org/10.3390/math13050738
[research_jeon_kim_2026]: https://doi.org/10.1109/access.2026.3679371
[research_jeong_suk_2024]: https://doi.org/10.1007/s12555-024-0539-3
[research_jewell_heffley_1979]: https://doi.org/10.2514/3.58536
[research_jeyachandrabose_kirkhope_1985]: https://doi.org/10.1016/0045-7949(85)90018-5
[research_ji_guo_2024]: https://doi.org/10.32604/cmes.2023.029088
[research_ji_ke_2024]: https://doi.org/10.1002/acs.3880
[research_ji_kim_2021]: https://doi.org/10.3390/aerospace8050126
[research_ji_kim_2023]: https://doi.org/10.3390/aerospace10040365
[research_ji_lu_2022]: https://doi.org/10.1016/j.ast.2022.107501
[research_ji_yang_2025]: https://doi.org/10.1016/j.ast.2025.110659
[research_ji_zhao_2021]: https://doi.org/10.1016/j.engstruct.2021.113051
[research_jia_chen_2024]: https://doi.org/10.1109/taes.2024.3381079
[research_jia_ezhilarasu_2023]: https://doi.org/10.3390/app132413120
[research_jia_feng_2026]: https://doi.org/10.30919/es2092
[research_jia_sun_2023]: https://doi.org/10.3390/drones7030200
[research_jiang_hu_2025]: https://doi.org/10.1177/14759217251368998
[research_jiang_ji_2023]: https://doi.org/10.1155/2023/2989533
[research_jiang_li_2018]: https://doi.org/10.1016/j.matdes.2018.03.028
[research_jiang_li_2018_b]: https://doi.org/10.1109/access.2018.2875786
[research_jiang_li_2024]: https://doi.org/10.1007/s11071-024-10134-8
[research_jiang_liu_2024]: https://doi.org/10.3390/act13060227
[research_jiang_tian_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000875
[research_jiang_tian_2019]: https://doi.org/10.1016/j.ast.2019.03.043
[research_jiang_tong_2022]: https://doi.org/10.1088/1742-6596/2235/1/012001
[research_jiang_yao_2024]: https://doi.org/10.1063/5.0197991
[research_jianhong_2022]: https://doi.org/10.1108/aeat-08-2021-0254
[research_jianhong_ramirezmendoza_2023]: https://doi.org/10.1108/aeat-12-2022-0342
[research_jianhong_yanxiang_2026]: https://doi.org/10.1108/aeat-01-2025-0009
[research_jiansong_chen_2024]: https://doi.org/10.12688/digitaltwin.18065.1
[research_jiao_jiang_2015]: https://doi.org/10.7763/ijmlc.2015.v5.524
[research_jin_bifeng_2015]: https://doi.org/10.1016/j.proeng.2014.12.629
[research_jin_xue_2026]: https://doi.org/10.3390/act15060337
[research_jing_duan_2023]: https://doi.org/10.1016/j.apm.2022.12.003
[research_jing_duan_2024]: https://doi.org/10.1016/j.compstruct.2023.117657
[research_jing_li_2022]: https://doi.org/10.1016/j.compstruct.2022.115934
[research_jing_qi_2020]: https://doi.org/10.1088/1757-899x/887/1/012042
[research_jing_tzeng_1995]: https://doi.org/10.1016/0263-8223(94)00045-x
[research_jo_majid_2023]: https://doi.org/10.3390/biomimetics8010034
[research_johari_olinger_1995]: https://doi.org/10.2514/3.46794
[research_john_qin_2019]: https://doi.org/10.1115/1.4042891
[research_johnsen_runnels_2022]: https://doi.org/10.3390/app12167961
[research_johnson_1964]: https://doi.org/10.2514/3.43568
[research_johnson_1965]: https://doi.org/10.21236/ad0617567
[research_johnson_1969]: https://doi.org/10.1137/0706030
[research_johnson_1972]: https://doi.org/10.21236/ad0754909
[research_johnson_1973]: https://doi.org/10.1016/0020-7683(73)90068-1
[research_johnson_henderson_1962]: https://doi.org/10.1016/s0020-7403(62)80002-2
[research_johnson_nokes_1998]: https://doi.org/10.21236/ada363261
[research_johnsonrw_junerr_1972]: https://ntrs.nasa.gov/citations/19720025911
[research_johnsonrw_mccartyje_1977]: https://ntrs.nasa.gov/citations/19770023236
[research_johnsonw_1977]: https://ntrs.nasa.gov/citations/19770021581
[research_johnston_ashkenas_1974]: https://doi.org/10.21236/ada014366
[research_johnston_cassarino_1976]: https://doi.org/10.21236/ada020871
[research_johnwhicks_jankania_1987]: https://ntrs.nasa.gov/citations/19870011558
[research_jones_1970]: https://doi.org/10.21236/ad0880948
[research_jones_1976]: https://doi.org/10.2514/3.58717
[research_jones_broughton_1985]: https://doi.org/10.1016/0263-8223(85)90042-x
[research_jones_jarrett_2018]: https://doi.org/10.2514/1.j056725
[research_jones_nisbet_1976]: https://doi.org/10.1017/s0001924000034138
[research_jonnalagadda_sawant_2015]: https://doi.org/10.1016/j.compstruct.2015.06.023
[research_jonsson_riso_2019]: https://doi.org/10.1016/j.paerosci.2019.04.001
[research_jonsson_riso_2023]: https://doi.org/10.2514/1.j061575
[research_joshi_kalra_2026]: https://doi.org/10.1016/j.ast.2026.112927
[research_jou_metcalfe_1984]: https://doi.org/10.21236/ada150123
[research_juhasz_tischler_2023]: https://doi.org/10.2514/1.c037085
[research_julian_kochenderfer_2019]: https://doi.org/10.2514/1.g004106
[research_junyi_xinbing_2021]: https://doi.org/10.1088/1757-899x/1102/1/012004
[research_jusko_berger_2026]: https://doi.org/10.4050/jahs.71.022007
[research_k_deodhare_2023]: https://doi.org/10.61653/joast.v75i2.2023.58
[research_kabaliswaran_das_2026]: https://doi.org/10.2514/1.c038269
[research_kabashkin_2024]: https://doi.org/10.3390/math12192979
[research_kaczmarek_2026]: https://doi.org/10.1016/j.neucom.2026.133215
[research_kafkas_kilimtzidis_2021]: https://doi.org/10.3390/aerospace8120398
[research_kai_2024]: https://doi.org/10.2514/1.g007917
[research_kajiwara_ton_2026]: https://doi.org/10.3390/fluids11020059
[research_kakkar_streit_2026]: https://doi.org/10.3390/aerospace13020171
[research_kalam_1981]: https://doi.org/10.1080/01495738108909950
[research_kalam_seshaiah_2022]: https://doi.org/10.1016/j.matpr.2021.10.271
[research_kalinowski_2015]: https://doi.org/10.1515/meceng-2015-0003
[research_kalinowski_szczepanik_2021]: https://doi.org/10.1088/1757-899x/1037/1/012058
[research_kalms_bergmann_2020]: https://doi.org/10.1016/j.addma.2020.101396
[research_kalnins_1968]: https://doi.org/10.21236/ad0686446
[research_kaloerov_1983]: https://doi.org/10.1007/bf00883204
[research_kalugin_voropaev_2022]: https://doi.org/10.3103/s1068799822030126
[research_kamaletdinova_romanov_2024]: https://doi.org/10.17150/2713-1734.2024.6(1).60-77
[research_kambampati_smith_2017]: https://doi.org/10.2514/1.c034195
[research_kambampati_townsend_2020]: https://doi.org/10.2514/1.j059157
[research_kambayashi_kogiso_2026]: https://doi.org/10.1299/mej.26-00075
[research_kanazaki_setoguchi_2023]: https://doi.org/10.3390/aerospace10090790
[research_kang_park_2016]: https://doi.org/10.5139/ijass.2016.17.1.120
[research_kano_ryuzono_2025]: https://doi.org/10.1016/j.ast.2025.110652
[research_kanou_ibuki_2025]: https://doi.org/10.1109/lcsys.2025.3647557
[research_kapania_bergen_1991]: https://doi.org/10.2514/3.59930
[research_kapania_issac_1994]: https://doi.org/10.2514/3.59995
[research_kapaniarakeshk_issacj_1997]: https://ntrs.nasa.gov/citations/19970021182
[research_karalmichael_2001]: https://ntrs.nasa.gov/citations/20010033249
[research_karimi_khorshidi_2022]: https://doi.org/10.1016/j.compstruct.2022.115630
[research_karimikelayeh_djavareshkian_2024]: https://doi.org/10.1061/jaeeez.aseng-5073
[research_karkadakattil_2026]: https://doi.org/10.2478/acss-2026-0003
[research_karkoszka_2019]: https://doi.org/10.2478/czoto-2019-0016
[research_karmah_2018]: https://doi.org/10.19080/raej.2018.02.555598
[research_karniadakis_2004]: https://doi.org/10.21236/ada420891
[research_karpouzian_1991]: https://doi.org/10.2514/3.10655
[research_karpuk_mosca_2024]: https://doi.org/10.2514/1.c037744
[research_karuna_manohar_2017]: https://doi.org/10.1016/j.engstruct.2017.07.044
[research_karuskevich_maslak_2022]: https://doi.org/10.1016/j.prostr.2022.01.008
[research_kashitani_takita_2019]: https://doi.org/10.1299/jsmedmc.2019.446
[research_kasimbiber_trentonwhite_2019]: https://doi.org/10.17265/2159-5275/2019.06.004
[research_kassapakis_warwick_1994]: https://doi.org/10.1002/acs.4480080405
[research_kassem_yang_2020]: https://doi.org/10.1016/j.jsv.2019.115110
[research_kassem_yang_2021]: https://doi.org/10.1007/s42417-020-00267-6
[research_kataoka_dol_1986]: https://doi.org/10.1299/jsme1958.29.393
[research_katunin_dragan_2015]: https://doi.org/10.1016/j.compstruct.2015.02.080
[research_katz_davidovitch_1986]: https://doi.org/10.2514/3.25851
[research_katz_levin_1986]: https://doi.org/10.2514/3.45386
[research_kaul_nguyen_2018]: https://doi.org/10.1115/1.4040070
[research_kawabe_tokumaru_1991]: https://doi.org/10.5687/iscie.4.277
[research_kaygan_ulusoy_2018]: https://doi.org/10.30518/jav.482507
[research_kazarin_golubev_2021]: https://doi.org/10.3390/electronics10161890
[research_kcs_james_2024]: https://doi.org/10.1016/j.prostr.2024.05.031
[research_kearns_1962]: https://doi.org/10.21236/ad0650981
[research_kehoemichaelw_1987]: https://ntrs.nasa.gov/citations/19870018230
[research_kehoemichaelw_bjarkelisaj_1990]: https://ntrs.nasa.gov/citations/19900039765
[research_kehoemw_1984]: https://ntrs.nasa.gov/citations/19860017818
[research_kehoemw_ellisonjf_1985]: https://ntrs.nasa.gov/citations/19850024805
[research_keidel_fasel_2020]: https://doi.org/10.2514/1.c035606
[research_keith_selberg_1984]: https://doi.org/10.2514/3.48244
[research_keith_selberg_1985]: https://doi.org/10.2514/3.45138
[research_keller_2019]: https://doi.org/10.1007/s13272-019-00396-z
[research_kendall_1985]: https://doi.org/10.2514/3.45214
[research_kennedy_1991]: https://doi.org/10.1177/002199839102500908
[research_kenny_lawrence_2025]: https://doi.org/10.2514/1.c037905
[research_kenway_martins_2016]: https://doi.org/10.2514/1.j054154
[research_kevrekidis_2002]: https://doi.org/10.21236/ada405411
[research_key_1971]: https://doi.org/10.21236/ad0725746
[research_key_1982]: https://doi.org/10.2514/3.57366
[research_khadse_karmore_2016]: https://doi.org/10.1016/j.procs.2016.02.059
[research_khajah_natarajan_2023]: https://doi.org/10.1016/j.compstruct.2023.116748
[research_khalaf_gan_2017]: https://doi.org/10.1186/s40638-017-0068-0
[research_khalil_asaro_2022]: https://doi.org/10.2514/1.c036426
[research_khalil_bauknecht_2024]: https://doi.org/10.2514/1.c037503
[research_khalil_fezans_2020]: https://doi.org/10.1017/aer.2020.85
[research_khalil_poirel_2016]: https://doi.org/10.1016/j.jsv.2016.07.016
[research_khan_riccio_2024]: https://doi.org/10.1016/j.paerosci.2024.101021
[research_khanal_adhikari_2026]: https://doi.org/10.12928/telkomnika.v24i2.27240
[research_khani_abdalla_2017]: https://doi.org/10.1016/j.compstruct.2017.07.086
[research_khankalantary_rezaeeahvanouee_2021]: https://doi.org/10.1177/09596518211003400
[research_kharghani_mittelstedt_2022]: https://doi.org/10.1016/j.compstruct.2021.115139
[research_khargonekar_sivashankar_1991]: https://doi.org/10.1016/0167-6911(91)90082-p
[research_kharisma_2019]: https://doi.org/10.20473/jkl.v11i1.2019.17-25
[research_kheiri_riazat_2025]: https://doi.org/10.1017/aer.2025.10028
[research_khodaverdian_gohil_2025]: https://doi.org/10.1016/j.dche.2025.100262
[research_kholodar_2016]: https://doi.org/10.2514/1.c033772
[research_kholodar_2023]: https://doi.org/10.2514/1.c036846
[research_khusnulnovianingsih_2025]: https://doi.org/10.52783/cana.v32.3458
[research_kida_1982]: https://doi.org/10.1002/zamm.19820620912
[research_kieffer_2006]: https://doi.org/10.21236/ada462805
[research_kielb_1975]: https://doi.org/10.2514/3.44437
[research_kilgore_averett_1964]: https://doi.org/10.2514/3.43598
[research_kilimtzidis_giannaros_2023]: https://doi.org/10.1016/j.compstruct.2023.116897
[research_kilimtzidis_kostopoulos_2023]: https://doi.org/10.3390/aerospace10030251
[research_kilimtzidis_kostopoulos_2023_b]: https://doi.org/10.1007/s00158-023-03600-1
[research_kim_2016]: https://doi.org/10.1016/j.jfluidstructs.2016.05.006
[research_kim_choi_2015]: https://doi.org/10.12985/ksaa.2015.23.1.067
[research_kim_ji_2022]: https://doi.org/10.1007/s42405-022-00560-6
[research_kim_kang_2025]: https://doi.org/10.6112/kscfe.2025.30.1.082
[research_kim_kim_2024]: https://doi.org/10.3390/app142210615
[research_kim_kunz_2017]: https://doi.org/10.2514/1.g002306
[research_kim_lee_2016]: https://doi.org/10.5302/j.icros.2016.16.0088
[research_kim_oh_2019]: https://doi.org/10.1007/s12555-018-0401-6
[research_kim_philip_2023]: https://doi.org/10.1109/access.2023.3267128
[research_kim_shin_2016]: https://doi.org/10.7234/composres.2016.29.6.369
[research_kim_sung_2017]: https://doi.org/10.5302/j.icros.2017.17.0075
[research_kim_youn_2025]: https://doi.org/10.1016/j.ress.2024.110515
[research_kineyko_1982]: https://doi.org/10.21236/ada119003
[research_king_brunner_1984]: https://doi.org/10.21236/ada149953
[research_king_johnson_1986]: https://doi.org/10.2514/3.9448
[research_kinney_1963]: https://doi.org/10.21236/ad0414572
[research_kirsch_fathi_2025]: https://doi.org/10.1115/1.4071802
[research_kirsch_montagnier_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.102930
[research_kish_mosle_1997]: https://doi.org/10.21236/ada286959
[research_kishi_kanazaki_2016]: https://doi.org/10.4236/jfcmv.2016.41004
[research_kishi_kanazaki_2022]: https://doi.org/10.2514/1.c036422
[research_kisielowski_perlmutter_1967]: https://doi.org/10.21236/ad0662259
[research_kisslinger_wendl_1971]: https://doi.org/10.21236/ad0727762
[research_kizildeniz_kiyak_2025]: https://doi.org/10.1108/aeat-03-2025-0127
[research_klasztorny_nycz_2018]: https://doi.org/10.1016/j.compstruct.2017.10.046
[research_klein_viswanathan_1973]: https://doi.org/10.1007/bf01590797
[research_kleinrw_hollisterwm_1982]: https://ntrs.nasa.gov/citations/19820026186
[research_kleinrw_lapinsm_1982]: https://ntrs.nasa.gov/citations/19820036249
[research_klema_1981]: https://doi.org/10.21236/ada106000
[research_klepl_1995]: https://doi.org/10.2514/3.46702
[research_klimczyk_goraj_2019]: https://doi.org/10.1108/aeat-12-2017-0289
[research_klinarwj_kubiaket_1975]: https://ntrs.nasa.gov/citations/19760045906
[research_kljajic_kostic_2016]: https://doi.org/10.5937/vojtehg64-9493
[research_klotzschem_1984]: https://ntrs.nasa.gov/citations/19870019180
[research_klyde_harris_2004]: https://doi.org/10.21236/ada426452
[research_knackstedt_1952]: https://doi.org/10.21236/ad0008717
[research_knaussjf_stonerh_1982]: https://ntrs.nasa.gov/citations/19830039267
[research_knight_1982]: https://doi.org/10.1177/002199838201600206
[research_knightondonnal_1992]: https://ntrs.nasa.gov/citations/19930029267
[research_knoxseith_1963]: https://doi.org/10.21236/ad0438911
[research_ko_kang_2019]: https://doi.org/10.5139/jksas.2019.47.2.114
[research_kobayashi_torisaki_1986]: https://doi.org/10.1299/jsme1958.29.1536
[research_kobelev_2019]: https://doi.org/10.1108/mmms-02-2018-0019
[research_kodama_1962]: https://doi.org/10.1109/tac.1962.1105413
[research_koenig_1984]: https://doi.org/10.21236/ada150667
[research_koh_2018]: https://doi.org/10.3390/ma11112324
[research_koh_kelly_1989]: https://doi.org/10.1520/jte11130j
[research_kohara_tomoeda_2016]: https://doi.org/10.1299/jsmecs.2016.54._1408-1_
[research_kohase_watanabe_2018]: https://doi.org/10.1299/jsmeiip.2018.2b06_1
[research_kohlman_1963]: https://doi.org/10.21236/ad0400562
[research_kohlman_1979]: https://doi.org/10.2514/3.58513
[research_kohn_1972]: https://doi.org/10.1137/1014067
[research_kohnhorst_magnacca_1980]: https://doi.org/10.21236/ada094688
[research_kokotovic_murray_2000]: https://doi.org/10.21236/ada387455
[research_kolar_lile_1971]: https://doi.org/10.21236/ada377254
[research_kolb_montagnier_2019]: https://doi.org/10.2514/1.g003729
[research_kolesar_1971]: https://doi.org/10.21236/ad0734236
[research_komarov_zinchenko_2023]: https://doi.org/10.20535/0203-3771452023290873
[research_komnatska_bondarenko_2017]: https://doi.org/10.15407/usim.2017.04.024
[research_komp_hajek_2024]: https://doi.org/10.2514/1.c037505
[research_konar_mahesh_1974]: https://doi.org/10.21236/ada002320
[research_konatala_milz_2024]: https://doi.org/10.2514/1.g008321
[research_kong_jeon_2025]: https://doi.org/10.1177/14759217251339812
[research_kononov_lymar_2020]: https://doi.org/10.7546/jtam.50.20.03.06
[research_kontogiannis_savill_2024]: https://doi.org/10.1016/j.ast.2024.109080
[research_koo_lee_1994]: https://doi.org/10.1016/0045-7949(94)90293-3
[research_kopecki_2016]: https://doi.org/10.1108/aeat-10-2012-0187
[research_kopecki_2021]: https://doi.org/10.1108/aeat-11-2020-0248
[research_kornev_ambrozhevich_2021]: https://doi.org/10.3103/s1068799821010049
[research_kosarev_seror_2016]: https://doi.org/10.2514/1.c033509
[research_koscielny_1983]: https://doi.org/10.21236/ada140558
[research_kosmodamianskii_mitrakov_1976]: https://doi.org/10.1007/bf00882705
[research_kosyanchuk_selvesyuk_2015]: https://doi.org/10.3846/16487788.2015.1015290
[research_kosyanchuk_zheltov_2021]: https://doi.org/10.1088/1742-6596/1864/1/012005
[research_kota_hetrick_1997]: https://doi.org/10.21236/ada361152
[research_kotitschke_rupprecht_2026]: https://doi.org/10.1007/s42401-026-00498-7
[research_kou_zhang_2021]: https://doi.org/10.1016/j.paerosci.2021.100725
[research_kousen_bendiksen_1994]: https://doi.org/10.2514/3.46644
[research_koyuncuoglu_he_2022]: https://doi.org/10.1016/j.ast.2022.107876
[research_kozhanov_suvorova_2022]: https://doi.org/10.52348/2712-8873_mmtt_2022_5_45
[research_krachmalnick_vetsch_1968]: https://doi.org/10.2514/3.43925
[research_kraftchristophercjr_reederjp_1948]: https://ntrs.nasa.gov/citations/20050028754
[research_kratochvil_valenta_2024]: https://doi.org/10.1007/s13272-024-00745-7
[research_krause_khargonekar_1990]: https://doi.org/10.21236/ada219259
[research_krener_2001]: https://doi.org/10.21236/ada430327
[research_kretov_tiniakov_2022]: https://doi.org/10.3390/aerospace9090497
[research_kriechbaum_stineman_1972]: https://doi.org/10.2514/3.58994
[research_krishnamurthy_ramezani_2026]: https://doi.org/10.1115/1.4071980
[research_kroo_1982]: https://doi.org/10.2514/3.61557
[research_kruger_meddaikar_2022]: https://doi.org/10.3390/aerospace9100535
[research_krzywoblocki_1943]: https://doi.org/10.2514/8.11023
[research_kuang_hu_2025]: https://doi.org/10.1142/s0219455427501756
[research_kubiak_gliszczynski_2019]: https://doi.org/10.1016/j.compstruct.2019.111222
[research_kubica_livet_1995]: https://doi.org/10.1016/0967-0661(95)00119-f
[research_kuder_arrieta_2015]: https://doi.org/10.1016/j.compstruct.2014.11.061
[research_kufmann_brillante_2017]: https://doi.org/10.1007/s13272-017-0265-0
[research_kuhlberg_newirth_1976]: https://doi.org/10.2514/3.58656
[research_kuhn_1975]: https://doi.org/10.21236/ada955473
[research_kulhanek_2019]: https://doi.org/10.1108/aeat-06-2018-0162
[research_kulikov_2020]: https://doi.org/10.1007/s10958-020-04994-9
[research_kumar_asha_2025]: https://doi.org/10.1016/j.prostr.2025.08.045
[research_kumar_collini_2020]: https://doi.org/10.1016/j.addma.2020.101168
[research_kumar_kumar_2022]: https://doi.org/10.4018/ijsda.302634
[research_kumar_onkar_2019]: https://doi.org/10.1007/s11012-019-01061-9
[research_kumarshakya_sekharpadhee_2023]: https://doi.org/10.1016/j.matpr.2023.05.731
[research_kuojiun_pongjeu_1989]: https://doi.org/10.1016/0045-7949(89)90030-8
[research_kurade_venkatakrishnan_2021]: https://doi.org/10.1017/aer.2021.99
[research_kurniawan_2022]: https://doi.org/10.31543/jtm.v6i1.724
[research_kurtz_2018]: https://doi.org/10.1007/s13675-018-0097-7
[research_kurz_1963]: https://doi.org/10.21236/ad0414370
[research_kurzhalspr_1978]: https://ntrs.nasa.gov/citations/19790008693
[research_kushner_1988]: https://doi.org/10.21236/ada192712
[research_kushner_2006]: https://doi.org/10.21236/ada458950
[research_kusni_widiramdhani_2021]: https://doi.org/10.1088/1757-899x/1173/1/012058
[research_kuttieri_sinha_2023]: https://doi.org/10.61653/joast.v64i3.2012.465
[research_kuvshinov_2016]: https://doi.org/10.1615/tsagiscij.2016017070
[research_kuvshinov_2016_b]: https://doi.org/10.1615/tsagiscij.2017020079
[research_kuvshinov_lazurin_2019]: https://doi.org/10.1615/tsagiscij.2020033338
[research_kuvshinov_leontiev_2019]: https://doi.org/10.1615/tsagiscij.2019031121
[research_kuzmina_ishmuratov_2020]: https://doi.org/10.34759/vst-2020-1-108-121
[research_kuznetsov_kartashov_1980]: https://doi.org/10.1007/bf00884879
[research_kuzu_bogosyan_2015]: https://doi.org/10.15837/ijccc.2016.1.1577
[research_kwatny_bennett_1991]: https://doi.org/10.1109/9.100946
[research_kwon_park_2019]: https://doi.org/10.1177/1475921719843772
[research_lafflitto_2018]: https://doi.org/10.1109/lcsys.2018.2842148
[research_lafflitto_2023]: https://doi.org/10.1002/acs.3631
[research_lafflitto_blackford_2018]: https://doi.org/10.1080/00207179.2018.1489147
[research_lai_2024]: https://doi.org/10.54254/2755-2721/91/20241080
[research_lai_young_1995]: https://doi.org/10.1016/0263-8223(94)00017-4
[research_laitone_1978]: https://doi.org/10.2514/3.58457
[research_laitone_1989]: https://doi.org/10.2514/3.45841
[research_lakshminarayana_1962]: https://doi.org/10.1017/s0368393100077920
[research_lam_1993]: https://doi.org/10.2514/3.61536
[research_lam_hung_1989]: https://doi.org/10.1016/0003-682x(89)90030-3
[research_lamarje_1978]: https://ntrs.nasa.gov/citations/19780057982
[research_lamarje_frinknt_1981]: https://ntrs.nasa.gov/citations/19810053680
[research_lamarje_frinknt_1981_b]: https://ntrs.nasa.gov/citations/19810016505
[research_lamarje_luckringjm_1979]: https://ntrs.nasa.gov/citations/19790013848
[research_lamarje_schemenskyrt_1980]: https://ntrs.nasa.gov/citations/19800034146
[research_lampton_klyde_2024]: https://doi.org/10.2514/1.g008058
[research_lance_1986]: https://ntrs.nasa.gov/citations/19860000337
[research_lancedward_tsengjb_1987]: https://ntrs.nasa.gov/citations/19870017427
[research_landfield_rajkovic_1986]: https://doi.org/10.2514/3.45328
[research_landsberger_dugundji_1985]: https://doi.org/10.2514/3.45186
[research_lang_deruiter_2021]: https://doi.org/10.1016/j.ast.2021.106971
[research_lang_li_2024]: https://doi.org/10.1016/j.ast.2024.109526
[research_langston_1967]: https://doi.org/10.21236/ad0813281
[research_lanteigne_mcleod_2020]: https://doi.org/10.1139/juvs-2019-0012
[research_lapinsm_kleinrw_1982]: https://ntrs.nasa.gov/citations/19820055547
[research_larsonrichardr_1987]: https://ntrs.nasa.gov/citations/19870007386
[research_latachi_rachidi_2020]: https://doi.org/10.3390/aerospace7100146
[research_latency_control_2025]: https://doi.org/10.38007/dps.2025.040102
[research_latz_2006]: https://doi.org/10.21236/ada521979
[research_latz_2007]: https://doi.org/10.21236/ada547640
[research_latz_2009]: https://doi.org/10.21236/ada500755
[research_laub_1991]: https://doi.org/10.21236/ada248481
[research_laura_viazzi_1985]: https://doi.org/10.1016/0029-8018(85)90008-3
[research_lavretsky_2019]: https://doi.org/10.2514/1.g004328
[research_law_1976]: https://doi.org/10.21236/adb010481
[research_lawrence_theodore_2018]: https://doi.org/10.1017/aer.2018.43
[research_layton_trenchea_2011]: https://doi.org/10.21236/ada538555
[research_le_2026]: https://doi.org/10.1007/s40435-026-02198-8
[research_lee_1977]: https://doi.org/10.21236/ada038281
[research_lee_1995]: https://doi.org/10.1017/s0001924000028815
[research_lee_2016]: https://doi.org/10.1115/1.4032301
[research_lee_2019]: https://doi.org/10.29279/kostet.2019.24.4.23
[research_lee_cho_1991]: https://doi.org/10.1016/0045-7949(91)90084-y
[research_lee_cho_1991_b]: https://doi.org/10.2514/3.10656
[research_lee_eyi_1993]: https://doi.org/10.2514/3.46419
[research_lee_kim_1994]: https://doi.org/10.2514/3.46667
[research_lee_kim_1995]: https://doi.org/10.2514/3.46803
[research_lee_kim_2020]: https://doi.org/10.1007/s12555-018-9403-7
[research_lee_kim_2021]: https://doi.org/10.3390/aerospace8090257
[research_lee_ko_2018]: https://doi.org/10.1115/1.4039232
[research_lee_lee_1990]: https://doi.org/10.1016/0045-7949(90)90019-x
[research_lee_lee_2019]: https://doi.org/10.5139/jksas.2019.47.1.1
[research_lee_lee_2023]: https://doi.org/10.5139/jksas.2023.51.11.751
[research_lee_lua_2025]: https://doi.org/10.2514/1.c038014
[research_lee_lua_2026]: https://doi.org/10.2514/1.c038959
[research_lee_mall_1989]: https://doi.org/10.1177/002199838902300403
[research_lee_mallett_1982]: https://doi.org/10.21236/ada127063
[research_lee_ohman_1984]: https://doi.org/10.2514/3.44987
[research_lee_ohman_1984_b]: https://doi.org/10.2514/3.56742
[research_lee_sheikh_2025]: https://doi.org/10.1093/jcde/qwaf124
[research_lee_sheu_1994]: https://doi.org/10.1002/oca.4660150204
[research_lee_singh_2017]: https://doi.org/10.1007/s11071-016-3287-y
[research_lee_singh_2018]: https://doi.org/10.2514/1.g003087
[research_lee_snyder_2017]: https://doi.org/10.2514/1.g001742
[research_lee_song_2018]: https://doi.org/10.2514/1.j056598
[research_lee_tang_1989]: https://doi.org/10.2514/3.45785
[research_lee_yun_2022]: https://doi.org/10.1016/j.addma.2022.102627
[research_lehilahy_ferdi_2023]: https://doi.org/10.1016/j.bspc.2022.104362
[research_lehman_stearman_1977]: https://doi.org/10.21236/ada039245
[research_lei_bai_2019]: https://doi.org/10.1016/j.ast.2019.07.018
[research_lei_bai_2021]: https://doi.org/10.1016/j.ast.2021.107101
[research_lei_guo_2021]: https://doi.org/10.3390/machines9100243
[research_lei_wang_2020]: https://doi.org/10.21595/jve.2019.20968
[research_leicester_1970]: https://doi.org/10.1061/jmcea3.0001329
[research_leighton_1978]: https://doi.org/10.21236/ada061891
[research_leitch_stodieck_2024]: https://doi.org/10.2139/ssrn.4786120
[research_leitch_stodieck_2025]: https://doi.org/10.1016/j.compstruct.2025.119706
[research_lekoudis_1980]: https://doi.org/10.2514/3.50852
[research_lemaysp_batillsm_1988]: https://ntrs.nasa.gov/citations/19880053508
[research_lemley_1968]: https://doi.org/10.21236/ad0840550
[research_lemmon_coleman_1973]: https://doi.org/10.2514/3.6801
[research_lendraitis_2019]: https://doi.org/10.5755/j01.mech.25.4.22325
[research_lendraitis_lukosevicius_2023]: https://doi.org/10.3390/math11091986
[research_lendraitis_lukosevicius_2025]: https://doi.org/10.3390/act14100498
[research_lennartson_1989]: https://doi.org/10.1080/00207178908559728
[research_leondes_rankine_1972]: https://doi.org/10.2514/3.58972
[research_lepri_bacciu_2024]: https://doi.org/10.1109/lcsys.2023.3344286
[research_lerner_markowitz_1979]: https://doi.org/10.2514/3.58486
[research_lerro_brandl_2020]: https://doi.org/10.3390/aerospace7050063
[research_lesoinne_2007]: https://doi.org/10.21236/ada481320
[research_levi_nelson_1964]: https://doi.org/10.2514/3.43579
[research_levison_1982]: https://doi.org/10.2514/3.57394
[research_li_2023]: https://doi.org/10.54254/2755-2721/10/20230134
[research_li_bai_2016]: https://doi.org/10.1016/j.isatra.2015.12.004
[research_li_bai_2018]: https://doi.org/10.1007/s42405-018-0046-y
[research_li_bai_2019]: https://doi.org/10.1016/j.ast.2019.05.067
[research_li_bai_2019_b]: https://doi.org/10.1016/j.ast.2019.105338
[research_li_bai_2022]: https://doi.org/10.2514/1.c036413
[research_li_chen_2016]: https://doi.org/10.1007/s00158-016-1459-5
[research_li_daronch_2019]: https://doi.org/10.1016/j.ast.2019.105354
[research_li_dong_2018]: https://doi.org/10.1002/asjc.1841
[research_li_gong_2019]: https://doi.org/10.1016/j.jfluidstructs.2018.10.011
[research_li_guo_2016]: https://doi.org/10.1108/aeat-12-2013-0234
[research_li_han_2026]: https://doi.org/10.1016/j.neunet.2026.108776
[research_li_he_2019]: https://doi.org/10.1016/j.ast.2019.06.008
[research_li_he_2024]: https://doi.org/10.1007/s11071-024-10600-3
[research_li_hu_2025]: https://doi.org/10.1016/j.ifacol.2025.11.380
[research_li_huang_2018]: https://doi.org/10.1177/1077546318810033
[research_li_ji_2025]: https://doi.org/10.1002/rnc.7925
[research_li_jin_2017]: https://doi.org/10.1016/j.ast.2016.11.029
[research_li_kou_2024]: https://doi.org/10.1016/j.jfluidstructs.2023.104055
[research_li_li_2022]: https://doi.org/10.1016/j.compstruct.2022.116047
[research_li_li_2025]: https://doi.org/10.1109/taes.2025.3596214
[research_li_li_2025_b]: https://doi.org/10.1080/27525783.2025.2599593
[research_li_lin_2025]: https://doi.org/10.1002/acs.3967
[research_li_liu_2021]: https://doi.org/10.1051/jnwpu/20213950995
[research_li_liu_2021_b]: https://doi.org/10.1016/j.conengprac.2021.104938
[research_li_liu_2022]: https://doi.org/10.1007/s10846-022-01691-4
[research_li_liu_2023]: https://doi.org/10.1002/rnc.6641
[research_li_luo_2023]: https://doi.org/10.1186/s42774-023-00155-z
[research_li_luo_2026]: https://doi.org/10.3390/buildings16112172
[research_li_miranda_2026]: https://doi.org/10.1016/j.compstruct.2026.120662
[research_li_pak_2015]: https://doi.org/10.2514/1.c033044
[research_li_qian_2024]: https://doi.org/10.3390/aerospace11121015
[research_li_qin_2020]: https://doi.org/10.1016/j.ast.2019.105622
[research_li_qin_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103407
[research_li_qin_2021_b]: https://doi.org/10.1016/j.ast.2021.106919
[research_li_qin_2022]: https://doi.org/10.3390/app122010537
[research_li_sanfelice_2016]: https://doi.org/10.1109/tcns.2015.2428351
[research_li_shang_2025]: https://doi.org/10.1186/s10033-025-01219-5
[research_li_shen_2018]: https://doi.org/10.1109/access.2018.2883067
[research_li_shen_2026]: https://doi.org/10.3390/aerospace13040325
[research_li_shi_2021]: https://doi.org/10.3390/aerospace8070176
[research_li_shi_2025]: https://doi.org/10.1108/aeat-08-2024-0233
[research_li_shi_2025_b]: https://doi.org/10.1016/j.addma.2025.104639
[research_li_sun_2022]: https://doi.org/10.1109/access.2022.3157878
[research_li_tang_2020]: https://doi.org/10.1016/j.ins.2019.10.039
[research_li_wan_2021]: https://doi.org/10.3390/app112411800
[research_li_wang_2018]: https://doi.org/10.1016/j.ast.2018.01.001
[research_li_wang_2018_b]: https://doi.org/10.1360/sspma2018-00072
[research_li_wang_2020]: https://doi.org/10.1155/2020/5812129
[research_li_wang_2021]: https://doi.org/10.3390/app11020505
[research_li_wang_2021_b]: https://doi.org/10.1002/stc.2908
[research_li_wang_2021_c]: https://doi.org/10.1016/j.addma.2021.102063
[research_li_wang_2026]: https://doi.org/10.1063/5.0319218
[research_li_wang_2026_b]: https://doi.org/10.1177/14759217251412365
[research_li_xiong_2025]: https://doi.org/10.1088/1742-6596/3044/1/012002
[research_li_xu_2026]: https://doi.org/10.3390/vibration9010008
[research_li_yang_2017]: https://doi.org/10.2514/1.c033670
[research_li_yang_2023]: https://doi.org/10.3390/aerospace10100866
[research_li_yang_2024]: https://doi.org/10.1142/s0219455425500853
[research_li_yang_2026]: https://doi.org/10.3390/su18020871
[research_li_yoon_2026]: https://doi.org/10.1007/s00158-026-04296-9
[research_li_yuan_2022]: https://doi.org/10.34133/2022/9790131
[research_li_zhang_2018]: https://doi.org/10.1109/access.2018.2853145
[research_li_zhang_2019]: https://doi.org/10.2514/1.j057958
[research_li_zhang_2021]: https://doi.org/10.1016/j.ast.2021.106639
[research_li_zhang_2021_b]: https://doi.org/10.2514/1.j059921
[research_li_zhang_2022]: https://doi.org/10.1016/j.ast.2021.107309
[research_li_zhang_2024]: https://doi.org/10.1080/0305215x.2024.2420746
[research_li_zhang_2024_b]: https://doi.org/10.3390/aerospace11121020
[research_li_zhang_2024_c]: https://doi.org/10.3390/aerospace11060422
[research_li_zhang_2024_d]: https://doi.org/10.2514/1.j063387
[research_li_zheng_2024]: https://doi.org/10.1063/5.0216603
[research_li_zheng_2025]: https://doi.org/10.1115/1.4069068
[research_li_zhou_2024]: https://doi.org/10.1007/s12206-024-0901-7
[research_lian_cao_2026]: https://doi.org/10.5890/jand.2026.03.015
[research_liang_gao_2024]: https://doi.org/10.1002/rnc.7559
[research_liang_ren_2018]: https://doi.org/10.2514/1.g003157
[research_liang_ye_2025]: https://doi.org/10.3390/machines13060439
[research_liang_yin_2024]: https://doi.org/10.1016/j.camwa.2024.06.014
[research_liao_song_2021]: https://doi.org/10.1063/5.0076538
[research_liao_sun_1993]: https://doi.org/10.2514/3.11865
[research_libeskind_minecci_1973]: https://doi.org/10.21236/ada326073
[research_librescu_khdeir_1988]: https://doi.org/10.2514/3.10050
[research_librescu_simovich_1988]: https://doi.org/10.2514/3.45572
[research_librescu_song_1992]: https://doi.org/10.1016/0961-9526(92)90039-9
[research_librescu_thangjitham_1991]: https://doi.org/10.2514/3.46004
[research_lichota_2023]: https://doi.org/10.1108/aeat-01-2023-0013
[research_lieferrandallk_1990]: https://ntrs.nasa.gov/citations/19900020073
[research_liew_wang_1993]: https://doi.org/10.1016/0141-0296(93)90017-x
[research_lifshits_ryzhov_1978]: https://doi.org/10.1007/bf01094463
[research_liguori_zucco_2024]: https://doi.org/10.1007/s11012-024-01799-x
[research_lijewski_1988]: https://doi.org/10.2514/3.26018
[research_lim_senthilnathan_1989]: https://doi.org/10.1016/0022-460x(89)90527-0
[research_lin_chin_1994]: https://doi.org/10.2514/3.46547
[research_lin_crawley_1995]: https://doi.org/10.1177/1045389x9500600312
[research_lin_lu_1989]: https://doi.org/10.2514/3.10228
[research_lindhorst_haupt_2015]: https://doi.org/10.2514/1.j053743
[research_lindrickc_brennermartinj_1997]: https://ntrs.nasa.gov/citations/19980018481
[research_lindsay_fikes_1976]: https://doi.org/10.21236/adb014423
[research_lindsay_jordan_1975]: https://doi.org/10.21236/ada009137
[research_linigier_dahlquist_1980]: https://doi.org/10.21236/ada098139
[research_lisovyi_petrovska_2021]: https://doi.org/10.33251/2707-8620-2021-5-36-41
[research_little_1973]: https://doi.org/10.1038/physci242079a0
[research_liu_2004]: https://doi.org/10.21236/ada430916
[research_liu_2018]: https://doi.org/10.1049/joe.2018.9016
[research_liu_2019]: https://doi.org/10.1177/0020294019858106
[research_liu_2024]: https://doi.org/10.1088/1742-6596/2820/1/012087
[research_liu_an_2018]: https://doi.org/10.1109/tmech.2018.2800089
[research_liu_bai_2017]: https://doi.org/10.2514/1.j055054
[research_liu_buss_2022]: https://doi.org/10.1002/rnc.6015
[research_liu_chen_2019]: https://doi.org/10.2514/1.c035338
[research_liu_chen_2023]: https://doi.org/10.1002/acs.3664
[research_liu_dong_2021]: https://doi.org/10.1016/j.cja.2020.04.026
[research_liu_du_2026]: https://doi.org/10.1016/j.oceaneng.2026.126111
[research_liu_featherston_2019]: https://doi.org/10.1016/j.compstruct.2018.12.054
[research_liu_featherston_2023]: https://doi.org/10.1016/j.compstruct.2023.116853
[research_liu_feng_2023]: https://doi.org/10.3390/s23218903
[research_liu_gao_2018]: https://doi.org/10.1007/s40430-018-1024-9
[research_liu_gao_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.103098
[research_liu_gao_2020_b]: https://doi.org/10.1007/s11071-020-05553-2
[research_liu_gao_2023]: https://doi.org/10.3390/aerospace10050406
[research_liu_geng_2026]: https://doi.org/10.1016/j.ast.2026.111664
[research_liu_he_2018]: https://doi.org/10.3390/a11100163
[research_liu_huang_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000682
[research_liu_huang_2026]: https://doi.org/10.1002/asjc.70049
[research_liu_ji_2024]: https://doi.org/10.1007/s12555-022-0318-y
[research_liu_kan_2022]: https://doi.org/10.1016/j.addma.2021.102503
[research_liu_li_2023]: https://doi.org/10.1016/j.compstruct.2023.116817
[research_liu_li_2026]: https://doi.org/10.3390/electronics15163532
[research_liu_li_2026_b]: https://doi.org/10.2514/1.c038309
[research_liu_lin_2024]: https://doi.org/10.3390/buildings14041043
[research_liu_liou_2009]: https://doi.org/10.21236/ada590187
[research_liu_liu_2025]: https://doi.org/10.1016/j.compstruct.2025.119588
[research_liu_liu_2026]: https://doi.org/10.1016/j.jfranklin.2026.108625
[research_liu_luo_2018]: https://doi.org/10.1016/j.ast.2017.10.008
[research_liu_namakiaraghi_2026]: https://doi.org/10.1080/27525783.2026.2694877
[research_liu_qian_2026]: https://doi.org/10.1016/j.ast.2026.112709
[research_liu_sang_2018]: https://doi.org/10.2514/1.c034923
[research_liu_shen_2026]: https://doi.org/10.3390/pr14142352
[research_liu_song_2016]: https://doi.org/10.1007/s00158-016-1546-7
[research_liu_sun_2016]: https://doi.org/10.1155/2016/1060574
[research_liu_sun_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000712
[research_liu_sun_2017_b]: https://doi.org/10.1016/j.ast.2017.10.006
[research_liu_sun_2022]: https://doi.org/10.3390/en15030787
[research_liu_sun_2025]: https://doi.org/10.1016/j.conengprac.2025.106314
[research_liu_tian_2019]: https://doi.org/10.1088/1757-899x/677/5/052056
[research_liu_toropov_2015]: https://doi.org/10.1007/s00158-015-1244-x
[research_liu_wang_2019]: https://doi.org/10.1016/j.jfluidstructs.2019.04.010
[research_liu_wang_2022]: https://doi.org/10.1016/j.sigpro.2022.108502
[research_liu_wang_2026]: https://doi.org/10.1016/j.cej.2026.180391
[research_liu_wu_2025]: https://doi.org/10.12688/digitaltwin.17824.1
[research_liu_yang_2026]: https://doi.org/10.1002/rnc.70564
[research_liu_ye_2016]: https://doi.org/10.1002/acs.2693
[research_liu_yu_2026]: https://doi.org/10.30941/cestems.2026.00002
[research_liu_zhang_2018]: https://doi.org/10.1016/j.sysconle.2018.07.012
[research_liu_zhang_2023]: https://doi.org/10.1016/j.ijmultiphaseflow.2022.104286
[research_liu_zhang_2024]: https://doi.org/10.1007/s00158-024-03755-5
[research_liu_zhao_2026]: https://doi.org/10.1038/s41598-026-48452-z
[research_liu_zheng_2023]: https://doi.org/10.1016/j.aei.2023.102115
[research_liu_zheng_2025]: https://doi.org/10.2514/1.c038200
[research_liu_zhou_2023]: https://doi.org/10.1088/1742-6596/2658/1/012051
[research_liu_zou_2024]: https://doi.org/10.1016/j.energy.2024.131327
[research_livne_2018]: https://doi.org/10.2514/1.c034442
[research_liwesleyw_pakchangi_2014]: https://ntrs.nasa.gov/citations/20140010035
[research_lloyd_sholl_1968]: https://doi.org/10.1088/0022-3719/1/6/319
[research_lo_1978]: https://doi.org/10.21236/ada050578
[research_lo_1979]: https://doi.org/10.21236/ada077707
[research_lo_1980]: https://doi.org/10.21236/ada092386
[research_lo_1981]: https://doi.org/10.21236/ada113019
[research_lobitz_traub_2023]: https://doi.org/10.3390/aerospace10110938
[research_lockwoodtaylor_1942]: https://doi.org/10.1108/eb030921
[research_lockwp_petersenwr_1975]: https://ntrs.nasa.gov/citations/19750010176
[research_loghis_xiros_2022]: https://doi.org/10.3390/jmse10121844
[research_loh_1986]: https://doi.org/10.21236/ada168970
[research_lohrer_krause_2025]: https://doi.org/10.1007/s11044-025-10120-x
[research_loja_barbosa_2017]: https://doi.org/10.1016/j.compstruct.2017.09.046
[research_lokoswilliama_1990]: https://ntrs.nasa.gov/citations/19920053312
[research_lombardi_1995]: https://doi.org/10.2514/3.46804
[research_lombardi_morelli_1994]: https://doi.org/10.2514/3.46517
[research_lombardi_vicini_1994]: https://doi.org/10.1017/s0001924000049733
[research_lomo_patel_2023]: https://doi.org/10.1016/j.addma.2023.103891
[research_long_2019]: https://doi.org/10.1002/rnc.4539
[research_long_mu_2021]: https://doi.org/10.1016/j.compstruct.2020.113005
[research_loos_springer_1983]: https://doi.org/10.21236/ada130071
[research_loser_1985]: https://doi.org/10.1016/0094-5765(85)90029-3
[research_loth_boyle_1969]: https://doi.org/10.21236/ad0704502
[research_loth_geubelle_2000]: https://doi.org/10.21236/ada378320
[research_lottati_1985]: https://doi.org/10.2514/3.45238
[research_lottati_1987]: https://doi.org/10.2514/3.45523
[research_lottati_1988]: https://doi.org/10.2514/3.45588
[research_loughlan_2019]: https://doi.org/10.1016/j.tws.2019.01.045
[research_loughlan_ata_1995]: https://doi.org/10.1016/0263-8223(95)00050-x
[research_lovatt_1986]: https://doi.org/10.21236/ada179591
[research_lovejoyandrewe_scottistephenj_2019]: https://ntrs.nasa.gov/citations/20200002432
[research_lowe_1988]: https://doi.org/10.2514/3.45606
[research_lowson_1990]: https://doi.org/10.2514/3.25332
[research_lu_1994]: https://doi.org/10.1016/s1474-6670(17)47575-6
[research_lu_cao_2025]: https://doi.org/10.1007/s12555-025-0311-3
[research_lu_fang_2018]: https://doi.org/10.1016/j.conengprac.2018.04.005
[research_lu_hong_2022]: https://doi.org/10.2514/1.g006219
[research_lu_hu_2019]: https://doi.org/10.1155/2019/1648576
[research_lu_ma_2019]: https://doi.org/10.1109/access.2019.2956818
[research_lu_murthy_1990]: https://doi.org/10.2514/3.45947
[research_lu_tian_2017]: https://doi.org/10.1016/j.cja.2017.03.003
[research_lu_vankampen_2016]: https://doi.org/10.1016/j.conengprac.2016.09.010
[research_lu_zhang_2015]: https://doi.org/10.1016/j.ssci.2014.12.005
[research_lu_zhang_2019]: https://doi.org/10.1016/j.cja.2019.09.010
[research_lu_zhang_2024]: https://doi.org/10.1007/s11081-024-09935-y
[research_luattnguyen_williampgilbert_1980]: https://ntrs.nasa.gov/citations/19800020743
[research_lucarini_dirito_2025]: https://doi.org/10.3390/act14080407
[research_lucas_1978]: https://doi.org/10.21236/adb028240
[research_ludenacervantes_choi_2020]: https://doi.org/10.1007/s42405-020-00273-8
[research_lukyanov_1968]: https://doi.org/10.1007/bf01136838
[research_lundry_1967]: https://doi.org/10.2514/3.43797
[research_lundry_1977]: https://doi.org/10.2514/3.44595
[research_lunghitano_afonso_2024]: https://doi.org/10.3390/app14062384
[research_lungu_lungu_2015]: https://doi.org/10.1016/j.ast.2015.07.005
[research_luo_bao_1988]: https://doi.org/10.2514/3.45620
[research_luo_chen_2025]: https://doi.org/10.1007/s00158-025-03994-0
[research_luo_ferrari_2024]: https://doi.org/10.1016/j.compositesb.2024.111739
[research_luo_liu_2015]: https://doi.org/10.2514/1.j053436
[research_luo_yin_2025]: https://doi.org/10.1108/sr-11-2024-0899
[research_luo_yu_2026]: https://doi.org/10.3390/aerospace13030281
[research_luo_zhang_2022]: https://doi.org/10.1109/access.2022.3175164
[research_luongo_casciati_2016]: https://doi.org/10.1007/s11071-016-3178-2
[research_lv_lei_2019]: https://doi.org/10.1088/1742-6596/1300/1/012085
[research_lyapunov_1993]: https://doi.org/10.1007/bf01051213
[research_lynch_mordasky_2018]: https://doi.org/10.1016/j.addma.2018.05.021
[research_lyu_cao_2018]: https://doi.org/10.1016/j.ast.2018.06.037
[research_lyu_kenway_2015]: https://doi.org/10.2514/1.j053318
[research_lyu_liem_2020]: https://doi.org/10.1016/j.treng.2020.100035
[research_lyu_martins_2015]: https://doi.org/10.2514/1.c033116
[research_lyu_xu_2025]: https://doi.org/10.1016/j.enggeo.2025.108325
[research_lyu_zhang_2019]: https://doi.org/10.1051/jnwpu/20193730523
[research_lyubchak_filshtinskii_1982]: https://doi.org/10.1007/bf00883592
[research_m_jury_1959]: https://doi.org/10.2307/3007623
[research_ma_abouhamzeh_2023]: https://doi.org/10.2514/1.c036988
[research_ma_abouhamzeh_2024]: https://doi.org/10.2514/1.c037388
[research_ma_chen_2023]: https://doi.org/10.1051/sands/2023020
[research_ma_dong_2019]: https://doi.org/10.1109/access.2019.2949061
[research_ma_guo_2015]: https://doi.org/10.1016/j.ast.2015.06.003
[research_ma_liu_2025]: https://doi.org/10.1016/j.isatra.2025.10.014
[research_ma_yu_2024]: https://doi.org/10.3390/drones8020058
[research_ma_zhou_2025]: https://doi.org/10.1109/access.2024.3519800
[research_mabboux_pommierbudinger_2024]: https://doi.org/10.1016/j.ast.2023.108778
[research_macdonald_1933]: https://doi.org/10.1103/physrev.43.830
[research_mackallda_pickettmd_1988]: https://ntrs.nasa.gov/citations/19880011793
[research_mackalldalea_allenjamesg_1989]: https://ntrs.nasa.gov/citations/19900023436
[research_mackalldalea_allenjamesg_1991]: https://ntrs.nasa.gov/citations/19910015825
[research_maenhout_billiet_2021]: https://doi.org/10.1016/j.nedt.2021.104849
[research_maewal_1984]: https://doi.org/10.21236/ada149071
[research_magee_taylor_1971]: https://doi.org/10.21236/ad0735733
[research_magliacano_tufano_2025]: https://doi.org/10.1016/j.compstruct.2025.119675
[research_magness_robinson_1993]: https://doi.org/10.2514/3.11786
[research_magnus_yoshihara_1975]: https://doi.org/10.2514/3.60585
[research_maguire_mamalis_2024]: https://doi.org/10.1016/j.compstruct.2024.118090
[research_mahapatra_halbe_2024]: https://doi.org/10.1016/j.ifacol.2024.05.017
[research_mahboub_rouabah_2022]: https://doi.org/10.29354/diag/151039
[research_mahdavizafarghandi_rezasoltani_2024]: https://doi.org/10.2514/1.c037347
[research_mahgoub_cortelezzi_2020]: https://doi.org/10.2514/1.j058021
[research_mahgoub_elbadawy_2022]: https://doi.org/10.1007/s11071-022-07213-z
[research_mahmood_2025]: https://doi.org/10.1177/10775463241312815
[research_mahroni_2021]: https://doi.org/10.28989/vortex.v1i2.902
[research_mahulkar_2010]: https://doi.org/10.21236/ada534168
[research_maine_murray_1988]: https://doi.org/10.2514/3.20296
[research_maity_hocht_2019]: https://doi.org/10.1016/j.ejcon.2019.04.007
[research_maiworm_limon_2021]: https://doi.org/10.1002/rnc.5361
[research_malcom_1969]: https://doi.org/10.2514/3.59426
[research_malcomlg_husbandjh_1976]: https://ntrs.nasa.gov/citations/19760058464
[research_malekpour_abdali_2025]: https://doi.org/10.1016/j.addlet.2025.100297
[research_malik_akhtar_2017]: https://doi.org/10.15632/jtam-pl.55.3.963
[research_mallik_kapania_2015]: https://doi.org/10.2514/1.c033096
[research_mallios_1964]: https://doi.org/10.21236/ad0603563
[research_mamedov_paryshev_2018]: https://doi.org/10.1615/tsagiscij.2018027114
[research_mammadov_hajiyev_2018]: https://doi.org/10.1016/j.ifacol.2018.11.253
[research_mamonova_soudakov_2019]: https://doi.org/10.1088/1742-6596/1268/1/012067
[research_mandal_gu_2016]: https://doi.org/10.3390/aerospace3040042
[research_manickam_polit_2025]: https://doi.org/10.1080/15376494.2025.2505158
[research_mannini_bartoli_2015]: https://doi.org/10.1016/j.strusafe.2014.07.005
[research_mannmj_campbellrl_1983]: https://ntrs.nasa.gov/citations/19830057468
[research_mannmj_campbellrl_1984]: https://ntrs.nasa.gov/citations/19840010093
[research_mannmj_mercerce_1985]: https://ntrs.nasa.gov/citations/19860026297
[research_mannmj_mercerce_1986]: https://ntrs.nasa.gov/citations/19870002269
[research_mansour_1970]: https://doi.org/10.5957/jsr.1970.14.1.8
[research_mansy_faruque_2023]: https://doi.org/10.2514/1.c037179
[research_mant_1972]: https://doi.org/10.1108/eb034920
[research_manzoor_maqsood_2016]: https://doi.org/10.15866/irease.v9i3.8119
[research_mao_dou_2018]: https://doi.org/10.1002/rnc.4349
[research_mao_li_2020]: https://doi.org/10.1155/2020/1426193
[research_mao_xie_2019]: https://doi.org/10.1155/2019/5847627
[research_mar_lin_1979]: https://doi.org/10.1177/002199837901300402
[research_marano_belardo_2022]: https://doi.org/10.3390/aerospace9070335
[research_marcus_1994]: https://doi.org/10.21236/ada289088
[research_mardanpour_izadpanahi_2018]: https://doi.org/10.1016/j.jsv.2018.06.067
[research_marecarios_montesbarrenetxea_2023]: https://doi.org/10.61653/joast.v61i1.2009.635
[research_marilyneogburn_johnvfoster_1991]: https://ntrs.nasa.gov/citations/19910063214
[research_marin_graciani_2022]: https://doi.org/10.1016/j.compstruct.2021.115088
[research_marques_natarajan_2017]: https://doi.org/10.1016/j.compstruct.2017.01.062
[research_marqui_bueno_2017]: https://doi.org/10.1016/j.jfluidstructs.2017.01.010
[research_marquis_farhood_2026]: https://doi.org/10.1016/j.conengprac.2025.106719
[research_marr_roderick_1975]: https://doi.org/10.4050/jahs.20.23
[research_martin_1978]: https://doi.org/10.21236/ada066904
[research_martin_hartwig_2019]: https://doi.org/10.1007/s00158-018-2164-3
[research_martin_pardo_2017]: https://doi.org/10.1007/s00362-017-0900-1
[research_martincobaltimoremd_1965]: https://doi.org/10.21236/ad0469181
[research_martincodenverco_1966]: https://doi.org/10.21236/ad0378020
[research_martindale_rockwell_1974]: https://doi.org/10.21236/ada002869
[research_martinezheredia_fernandezprada_2026]: https://doi.org/10.3390/en19153498
[research_maruyama_ogino_2024]: https://doi.org/10.1007/s40194-024-01748-y
[research_masini_timme_2019]: https://doi.org/10.1017/jfm.2019.906
[research_masini_timme_2020]: https://doi.org/10.2514/1.j059219
[research_maslanka_kachel_2025]: https://doi.org/10.15866/irease.v18i2.25886
[research_masonml_caponefj_1983]: https://ntrs.nasa.gov/citations/19830013890
[research_masuda_shimosawa_2016]: https://doi.org/10.2322/tastj.14.pe_13
[research_mateergeorgec_seegmillerhlee_1987]: https://ntrs.nasa.gov/citations/19870057640
[research_mathur_huang_2026]: https://doi.org/10.2514/1.j066300
[research_matos_marta_2025]: https://doi.org/10.3390/aerospace12050369
[research_matrix_cracking_1985]: https://doi.org/10.1016/0010-4361(85)90361-1
[research_matsuki_nishiyama_2018]: https://doi.org/10.1108/aeat-03-2016-0052
[research_matt_chao_2025]: https://doi.org/10.2514/1.c038147
[research_mayer_lutz_2019]: https://doi.org/10.2514/1.c034969
[research_mayer_prowe_2016]: https://doi.org/10.1016/j.compstruct.2016.01.023
[research_mazaheri_khatibirad_2016]: https://doi.org/10.1007/s00193-016-0672-x
[research_mazaheri_khatibirad_2017]: https://doi.org/10.1007/s00193-017-0729-5
[research_mazaheri_kiani_2015]: https://doi.org/10.1016/j.ast.2015.01.007
[research_mazaheri_nejati_2015]: https://doi.org/10.1007/s10494-015-9671-8
[research_mazaheri_nejati_2015_b]: https://doi.org/10.1007/s00193-015-0591-2
[research_mazaheri_nejati_2016]: https://doi.org/10.1080/0305215x.2016.1139811
[research_mazaheri_nejati_2017]: https://doi.org/10.24200/sci.2017.4032
[research_mcallister_esfahani_2025]: https://doi.org/10.1109/tac.2024.3498702
[research_mccaskill_1953]: https://doi.org/10.21236/ad0015833
[research_mccomb_hayduk_1987]: https://doi.org/10.2514/3.45500
[research_mccutchen_1980]: https://doi.org/10.2514/3.44655
[research_mcdonald_2001]: https://doi.org/10.21236/ada387726
[research_mcdonald_farris_1964]: https://doi.org/10.21236/ad0603704
[research_mcdonnell_ning_2020]: https://doi.org/10.2514/1.c035566
[research_mcdonnellaircraftcorpstlouismo_1962]: https://doi.org/10.21236/ad0400969
[research_mcdonnellaircraftcorpstlouismo_1963]: https://doi.org/10.21236/ad0404211
[research_mceneaney_1999]: https://doi.org/10.21236/ada383810
[research_mceneaney_2013]: https://doi.org/10.21236/ada590145
[research_mcfadden_brandt_2023]: https://doi.org/10.2514/1.j062302
[research_mcgough_moses_1974]: https://doi.org/10.21236/ada006411
[research_mcgregor_smith_1966]: https://doi.org/10.2514/3.43780
[research_mcgurk_stodieck_2024]: https://doi.org/10.1016/j.compstruct.2023.117794
[research_mcintosh_mishra_2024]: https://doi.org/10.2514/1.g008002
[research_mckeehen_cord_1997]: https://doi.org/10.21236/ada327802
[research_mckillip_1991]: https://doi.org/10.4050/jahs.36.4
[research_mckinney_1972]: https://doi.org/10.1177/002199837200600115
[research_mcklnney_dollyhlgh_1971]: https://doi.org/10.2514/3.59148
[research_mcmaster_schenk_1974]: https://doi.org/10.2514/3.59224
[research_mcruerd_johnstond_1986]: https://ntrs.nasa.gov/citations/19870030478
[research_mcwilliam_zahle_2018]: https://doi.org/10.1088/1742-6596/1037/4/042009
[research_mefford_voss_1948]: https://doi.org/10.21236/adb812175
[research_meglinskii_1966]: https://doi.org/10.1007/bf00887749
[research_mehmedoral_1988]: https://ntrs.nasa.gov/citations/19880013862
[research_mei_giurgiutiu_2018]: https://doi.org/10.1177/1475921718765955
[research_mei_wang_2021]: https://doi.org/10.1016/j.jmapro.2021.03.052
[research_meirovitch_1995]: https://doi.org/10.21236/ada293689
[research_melville_bramesfeld_2020]: https://doi.org/10.1061/(asce)as.1943-5525.0001158
[research_memon_white_2021]: https://doi.org/10.1017/aer.2021.87
[research_menet_menart_1993]: https://doi.org/10.1007/bf00194012
[research_meng_fu_2024]: https://doi.org/10.1007/s11071-024-10046-7
[research_meng_jiang_2025]: https://doi.org/10.1088/1742-6596/3026/1/012013
[research_meng_yan_2019]: https://doi.org/10.1155/2019/3684015
[research_mengzhu_zhitao_2026]: https://doi.org/10.1177/14759217251405486
[research_menon_1989]: https://doi.org/10.2514/3.20364
[research_menon_yousefpor_1996]: https://doi.org/10.21236/ada436537
[research_mertaugh_1998]: https://doi.org/10.21236/ada350674
[research_mertins_1991]: https://doi.org/10.1007/bf01385803
[research_mertins_1992]: https://doi.org/10.1007/bf01385858
[research_mhenni_choley_2016]: https://doi.org/10.1016/j.ifacol.2016.07.076
[research_miaadi_li_2021]: https://doi.org/10.1016/j.chaos.2020.110389
[research_miao_wei_2017]: https://doi.org/10.1177/0142331216683771
[research_michaud_dalir_2018]: https://doi.org/10.2514/1.c034340
[research_micheli_2024]: https://doi.org/10.2514/1.g008146
[research_micks_1950]: https://doi.org/10.2514/8.1784
[research_miele_1976]: https://doi.org/10.21236/ada053727
[research_mihailaandres_rosu_2019]: https://doi.org/10.1051/itmconf/20192402010
[research_mihaly_gaspar_2017]: https://doi.org/10.1016/j.ifacol.2017.08.1428
[research_mijovic_1985]: https://doi.org/10.1177/002199838501900205
[research_miles_broughton_2017]: https://doi.org/10.2514/1.c033900
[research_miller_1965]: https://doi.org/10.2514/3.43649
[research_miller_1970]: https://doi.org/10.2514/3.44206
[research_miller_1986]: https://doi.org/10.2514/3.45268
[research_miller_clark_1965]: https://doi.org/10.2514/3.43639
[research_miller_wykes_1983]: https://doi.org/10.2514/3.44931
[research_milz_may_2026]: https://doi.org/10.2514/1.g009361
[research_minerdd_glossbb_1975]: https://ntrs.nasa.gov/citations/19750013175
[research_ming_hu_2026]: https://doi.org/10.1016/j.dsp.2026.105904
[research_mingong_sun_2022]: https://doi.org/10.34759/trd-2022-126-10
[research_minwalla_thomas_2016]: https://doi.org/10.1139/juvs-2014-0022
[research_miranda_bidinotto_2025]: https://doi.org/10.1590/jatm.v17.1368
[research_miranda_li_2025]: https://doi.org/10.1016/j.compstruct.2025.119291
[research_mirtaba_jeddi_2022]: https://doi.org/10.1007/s40435-022-01016-1
[research_mishra_yadav_2025]: https://doi.org/10.1504/ijscc.2025.145789
[research_miska_balzani_2025]: https://doi.org/10.1016/j.probengmech.2025.103755
[research_missoum_2012]: https://doi.org/10.21236/ada582315
[research_mitchell_1961]: https://doi.org/10.4050/jahs.6.3
[research_mitchell_myers_1980]: https://doi.org/10.21236/ada101648
[research_miurahirokazu_neilldouglasj_1992]: https://ntrs.nasa.gov/citations/19930036331
[research_miyasato_1992]: https://doi.org/10.9746/sicetr1965.28.1141
[research_miyazawa_1993]: https://doi.org/10.2514/3.20995
[research_mkhoyan_thakrar_2022]: https://doi.org/10.1088/1361-665x/aca18b
[research_mobayen_izadbakhsh_2025]: https://doi.org/10.1007/s11071-025-11076-5
[research_mochizuki_yamada_2018]: https://doi.org/10.1051/matecconf/201814503010
[research_modaressaval_bakhtiarinejad_2019]: https://doi.org/10.1016/j.jfluidstructs.2019.01.003
[research_modi_slater_1983]: https://doi.org/10.1016/0167-6105(83)90110-1
[research_modi_slater_1994]: https://doi.org/10.1115/1.2930448
[research_modified_l1_2018]: https://doi.org/10.5829/ije.2018.31.11b.23
[research_moens_2019]: https://doi.org/10.3390/biomimetics4030064
[research_moestimothyr_noffzgregoryk_2000]: https://ntrs.nasa.gov/citations/20010002099
[research_moestimothyr_smithmarks_2003]: https://ntrs.nasa.gov/citations/20030107571
[research_moghtadaei_2024]: https://doi.org/10.33140/jdaedm.01.01.06
[research_mohamed_g_2020]: https://doi.org/10.1016/j.ifacol.2020.06.013
[research_mohammadi_ebrahimi_2025]: https://doi.org/10.1007/s44245-025-00090-x
[research_mohammadzadeh_sayadi_2018]: https://doi.org/10.1016/j.cja.2018.04.004
[research_mohan_gaitonde_2017]: https://doi.org/10.2514/1.c034044
[research_mohankumar_hall_2021]: https://doi.org/10.1115/1.4050606
[research_mohankumar_hall_2022]: https://doi.org/10.1115/1.4054064
[research_mohanty_chhotaray_1979]: https://doi.org/10.1080/03772063.1979.11451910
[research_mohseni_bernstein_2024]: https://doi.org/10.1002/acs.3810
[research_mojallizadeh_2026]: https://doi.org/10.1080/00207179.2026.2676813
[research_mokhtarimousavi_mehrabi_2023]: https://doi.org/10.1016/j.ijtst.2022.01.007
[research_molent_haddad_2020]: https://doi.org/10.1016/j.compstruct.2019.111568
[research_monaghanrc_1981]: https://ntrs.nasa.gov/citations/19810009523
[research_monasa_snyder_1981]: https://doi.org/10.62913/engj.v18i1.357
[research_moni_yao_2024]: https://doi.org/10.1063/5.0177577
[research_monshizadeh_2020]: https://doi.org/10.1109/lcsys.2020.2993986
[research_montgomery_1972]: https://doi.org/10.2514/3.59015
[research_montgomery_caglayan_1976]: https://doi.org/10.2514/3.58633
[research_montgomery_price_1976]: https://doi.org/10.2514/3.58634
[research_montgomeryrc_pricedb_1974]: https://ntrs.nasa.gov/citations/19740055499
[research_moon_1996]: https://doi.org/10.21236/ada361169
[research_moore_1972]: https://doi.org/10.21236/ad0754098
[research_moorenr_ebbelerdh_1992]: https://ntrs.nasa.gov/citations/19940009605
[research_moorhouse_jenkins_1975]: https://doi.org/10.2514/3.44474
[research_moosavi_elasha_2022]: https://doi.org/10.3390/designs6020029
[research_moradi_zalaghi_2025]: https://doi.org/10.1007/s12046-025-02709-x
[research_moreira_gripp_2022]: https://doi.org/10.2514/1.g006443
[research_moreira_moleiro_2024]: https://doi.org/10.1016/j.compstruct.2024.118287
[research_morgado_silvestre_2016]: https://doi.org/10.1108/aeat-07-2014-0119
[research_morino_obayashi_2015]: https://doi.org/10.2514/1.c032775
[research_morita_matsukawa_1995]: https://doi.org/10.1080/00423119508969100
[research_moriya_1982]: https://doi.org/10.1299/jsme1958.25.1202
[research_morozov_chermoshentsev_2019]: https://doi.org/10.21683/1729-2646-2019-19-1-30-35
[research_morozov_janschek_2016]: https://doi.org/10.1016/j.ifacol.2016.09.043
[research_morris_1977]: https://doi.org/10.21236/ada049528
[research_morrison_white_1976]: https://doi.org/10.21236/ada029371
[research_morton_xu_2023]: https://doi.org/10.1177/00219983231151397
[research_mosaad_2023]: https://doi.org/10.53370/001c.74154
[research_moshier_2006]: https://doi.org/10.21236/ada448143
[research_motta_malzacher_2019]: https://doi.org/10.1115/1.4043545
[research_mottershead_cooper_2012]: https://doi.org/10.21236/ada571493
[research_moulmartint_brownlawrencew_1959]: https://ntrs.nasa.gov/citations/19980228212
[research_moulmartint_winemanandrewr_1952]: https://ntrs.nasa.gov/citations/19930086980
[research_moureydj_1979]: https://ntrs.nasa.gov/citations/19800001956
[research_mtowe_long_2025]: https://doi.org/10.3390/s25154666
[research_mu_huang_2022]: https://doi.org/10.1016/j.jsv.2022.116916
[research_mu_huang_2026]: https://doi.org/10.1016/j.jsv.2025.119440
[research_mueller_brito_2003]: https://doi.org/10.21236/ada451883
[research_muir_arredondogaleana_2017]: https://doi.org/10.1098/rsos.170077
[research_mukherjee_halder_2017]: https://doi.org/10.1016/j.egypro.2017.05.188
[research_mukherjee_sinha_2017]: https://doi.org/10.1016/j.ast.2017.04.030
[research_mukhopadhyayvivek_sorokachmichaelr_2015]: https://ntrs.nasa.gov/citations/20160006012
[research_mulder_1988]: https://doi.org/10.1016/s1474-6670(17)54913-7
[research_munoz_garciafogeda_2022]: https://doi.org/10.3390/aerospace9120804
[research_munoz_garciafogeda_2024]: https://doi.org/10.3390/aerospace11030198
[research_murphy_peloubet_1976]: https://doi.org/10.21236/adb013257
[research_murphypatrickc_1996]: https://ntrs.nasa.gov/citations/19980200994
[research_murray_doman_2015]: https://doi.org/10.1016/j.compstruct.2014.11.035
[research_murridg_croomma_1983]: https://ntrs.nasa.gov/citations/19830057448
[research_murridg_nguyenlt_1984]: https://ntrs.nasa.gov/citations/19840009116
[research_muscarello_quaranta_2016]: https://doi.org/10.2514/1.g001121
[research_myers_walsh_1991]: https://doi.org/10.2514/3.46103
[research_na_lee_2024]: https://doi.org/10.2514/1.i011269
[research_naca_conference_1949]: https://ntrs.nasa.gov/citations/19650074048
[research_naca_conference_1957]: https://ntrs.nasa.gov/citations/19710070068
[research_naderilordejani_besselink_2023]: https://doi.org/10.1016/j.jprocont.2022.11.012
[research_nagabhushan_1991]: https://doi.org/10.2514/3.46064
[research_naganarayana_atluri_1995]: https://doi.org/10.1007/s004660050032
[research_nagaraja_lakin_1982]: https://doi.org/10.2514/3.61555
[research_nagib_wigeland_1977]: https://doi.org/10.21236/ada049193
[research_nagy_1979]: https://doi.org/10.21236/ada071322
[research_nagy_fossati_2022]: https://doi.org/10.3390/fluids7040130
[research_naihong_yaohua_1993]: https://doi.org/10.2514/3.46361
[research_najmi_khan_2024]: https://doi.org/10.1016/j.heliyon.2024.e24151
[research_nakamura_1982]: https://doi.org/10.1143/jpsj.51.4084
[research_nakamura_kawamura_2017]: https://doi.org/10.1002/ecj.11935
[research_nakamura_takesue_1990]: https://doi.org/10.1541/ieejias.110.693
[research_nalini_dhanalakshmi_2019]: https://doi.org/10.1177/1045389x19828487
[research_nam_chen_2000]: https://doi.org/10.21236/ada379722
[research_nam_choi_2025]: https://doi.org/10.1016/j.sna.2025.116950
[research_namanikoureh_shahverdi_2026]: https://doi.org/10.1007/s00158-026-04311-z
[research_nambiar_pachidis_2022]: https://doi.org/10.1016/j.jppr.2022.07.005
[research_nan_zheng_2024]: https://doi.org/10.3390/machines12120907
[research_napolitano_2002]: https://doi.org/10.21236/ada400639
[research_napolitanomarcellor_1996]: https://ntrs.nasa.gov/citations/19960014815
[research_napolitanomarcellor_spagnuolojoellem_1993]: https://ntrs.nasa.gov/citations/19940020331
[research_narayanan_kumar_2026]: https://doi.org/10.1051/e3sconf/202669202008
[research_narendra_tripathi_1973]: https://doi.org/10.2514/3.44364
[research_narenshakthi_dharani_2025]: https://doi.org/10.1007/s11785-025-01829-w
[research_naresh_srinivas_2024]: https://doi.org/10.1142/s0219455425501664
[research_narimani_haddadpour_2025]: https://doi.org/10.1016/j.ast.2025.109992
[research_narimani_joulaei_2024]: https://doi.org/10.1016/j.rineng.2024.102255
[research_nath_ana_2017]: https://doi.org/10.14445/22315381/ijett-v54p212
[research_navratil_2017]: https://doi.org/10.1051/itmconf/20171400006
[research_nazarenko_nevezhina_1972]: https://doi.org/10.1007/bf01186488
[research_nazari_seron_2017]: https://doi.org/10.1016/j.automatica.2016.09.012
[research_nazeer_wang_2021]: https://doi.org/10.3390/act10060107
[research_neal_smith_1970]: https://doi.org/10.21236/ad0880426
[research_negaard_1980]: https://doi.org/10.21236/ada361289
[research_negahban_bashir_2024]: https://doi.org/10.3390/drones8080392
[research_negahbanb_khalafi_2025]: https://doi.org/10.1080/15397734.2025.2553328
[research_nejati_mazaheri_2017]: https://doi.org/10.1080/17797179.2017.1386022
[research_nekooei_farsangi_2021]: https://doi.org/10.1016/j.nahs.2021.101019
[research_nelson_mouch_1978]: https://doi.org/10.21236/ada056045
[research_neu_huang_1973]: https://doi.org/10.21236/ada325972
[research_neville_marois_1992]: https://doi.org/10.1364/ao.31.003463
[research_newkirk_1979]: https://doi.org/10.21236/ada089350
[research_newton_kroo_2025]: https://doi.org/10.2514/1.g008400
[research_nguyen_2019]: https://doi.org/10.1299/jamdsm.2019jamdsm0057
[research_nguyen_goulet_2018]: https://doi.org/10.1002/stc.2136
[research_nguyen_han_2025]: https://doi.org/10.1016/j.automatica.2025.112270
[research_nguyen_lejeune_2026]: https://doi.org/10.1016/j.ejor.2026.02.036
[research_nguyen_lowenberg_2021]: https://doi.org/10.2514/1.g005840
[research_nguyen_olaru_2016]: https://doi.org/10.1016/j.automatica.2015.10.048
[research_nguyen_prodan_2026]: https://doi.org/10.1016/j.ejcon.2025.101442
[research_nguyen_reynolds_2018]: https://doi.org/10.2514/1.c034448
[research_nguyenlt_gilbertwp_1979]: https://ntrs.nasa.gov/citations/19800006901
[research_nguyenluatt_gilertwilliamp_1990]: https://ntrs.nasa.gov/citations/19900048974
[research_nguyennhan_jamesurnessr_2012]: https://ntrs.nasa.gov/citations/20170005442
[research_nguyennhan_kaulupender_2015]: https://ntrs.nasa.gov/citations/20150023531
[research_ni_li_2023]: https://doi.org/10.1016/j.compstruct.2022.116504
[research_ni_wu_2021]: https://doi.org/10.1109/access.2021.3095224
[research_nibbelinkbruced_petersdavida_1993]: https://ntrs.nasa.gov/citations/19930049880
[research_niblett_1986]: https://doi.org/10.2514/3.45369
[research_niblett_1988]: https://doi.org/10.2514/3.45590
[research_nicholaswu_navillegl_1984]: https://ntrs.nasa.gov/citations/19840062226
[research_nicolaides_1971]: https://doi.org/10.21236/ad0731564
[research_niehaus_1962]: https://doi.org/10.4050/jahs.7.24
[research_niel_seuret_2017]: https://doi.org/10.1016/j.ifacol.2017.08.2041
[research_nield_iv_1981]: https://doi.org/10.21236/ada106742
[research_nihtila_1989]: https://doi.org/10.1016/0167-6911(89)90046-7
[research_nikolaev_2019]: https://doi.org/10.1061/(asce)as.1943-5525.0001086
[research_nikolaou_kilimtzidis_2026]: https://doi.org/10.3390/drones10050352
[research_nikrad_asadi_2015]: https://doi.org/10.1016/j.compstruct.2015.07.019
[research_ning_2021]: https://doi.org/10.1007/s00158-021-02883-6
[research_nissen_2009]: https://doi.org/10.21236/ada513588
[research_nitschke_vincenti_2019]: https://doi.org/10.1016/j.compstruct.2019.03.072
[research_nitz_1989]: https://doi.org/10.21236/ada344721
[research_nitzsche_breitbach_1994]: https://doi.org/10.2514/3.46628
[research_niu_chen_2018]: https://doi.org/10.1007/s11071-018-4127-z
[research_niu_li_2022]: https://doi.org/10.3390/app122211820
[research_niu_li_2026]: https://doi.org/10.1007/s12555-026-00058-x
[research_niu_zhang_2022]: https://doi.org/10.3103/s0025654422060103
[research_niven_1977]: https://doi.org/10.21236/ada050618
[research_nixonmarkw_piatakdavidj_1999]: https://ntrs.nasa.gov/citations/19990050923
[research_noll_eastep_1984]: https://doi.org/10.2514/3.48246
[research_non_linear_bending_1977]: https://doi.org/10.1016/0010-4361(77)90121-5
[research_nonnenmacher_jones_2016]: https://doi.org/10.1007/s13272-016-0211-6
[research_nonweiler_1960]: https://doi.org/10.1017/s0368393100072485
[research_noordin_mohdbasri_2023]: https://doi.org/10.3390/aerospace10010059
[research_northropaircraftinchawthorneca_1952]: https://doi.org/10.21236/ad0024361
[research_norton_1990]: https://doi.org/10.21236/ada257262
[research_norwood_1992]: https://doi.org/10.21236/ada249881
[research_ntantis_xezonakis_2024]: https://doi.org/10.1016/j.rineng.2024.103189
[research_numerical_analysis_2017]: https://doi.org/10.15372/pmtf20170303
[research_numerical_and_2019]: https://doi.org/10.17559/tv-20180724143418
[research_numerical_study_2023]: https://doi.org/10.47176/jafm.16.09.1755
[research_nuttall_1997]: https://doi.org/10.21236/ada327076
[research_oberkampf_nicolaides_1971]: https://doi.org/10.2514/3.50043
[research_obilanade_torlind_2025]: https://doi.org/10.1017/dsj.2025.10042
[research_obrien_datta_2026]: https://doi.org/10.2514/1.c038655
[research_ocali_sezer_1992]: https://doi.org/10.1109/9.256390
[research_ochi_kanai_1995]: https://doi.org/10.2514/3.21393
[research_ochoa_groves_2019]: https://doi.org/10.1002/stc.2340
[research_oconnell_tseytlin_2022]: https://doi.org/10.1016/j.jmr.2022.107308
[research_odonnell_mohseni_2019]: https://doi.org/10.2514/1.c034704
[research_odonnelljamesrjr_andrewsstephenf_1999]: https://ntrs.nasa.gov/citations/19990064189
[research_odonnelljamesrjr_davisgaryt_2002]: https://ntrs.nasa.gov/citations/20020060756
[research_oelker_hummel_1989]: https://doi.org/10.2514/3.45817
[research_oganyan_loginov_2025]: https://doi.org/10.2478/tar-2025-0018
[research_ogilvie_shen_1973]: https://doi.org/10.21236/ad0769005
[research_ogunvoul_balanchuk_2017]: https://doi.org/10.26467/2079-0619-2017-20-4-41-51
[research_oh_2023]: https://doi.org/10.5143/jesk.2023.42.4.385
[research_ohkawa_1985]: https://doi.org/10.1080/00207178508933423
[research_ohkawa_1986]: https://doi.org/10.1080/00207178608933588
[research_ohki_itakura_2015]: https://doi.org/10.1299/jsmekyushu.2015.68.323
[research_ohkuma_1993]: https://doi.org/10.1016/0167-6105(93)90365-u
[research_ohta_nikiforuk_1979]: https://doi.org/10.2514/3.55828
[research_ohta_nikiforuk_1982]: https://doi.org/10.2514/3.56143
[research_oktay_ozen_2022]: https://doi.org/10.30518/jav.1080139
[research_okumoto_elsanker_1973]: https://doi.org/10.21236/ad0767182
[research_oland_andersen_2016]: https://doi.org/10.1016/j.automatica.2016.02.034
[research_olivett_corrao_2021]: https://doi.org/10.1088/1361-665x/abd347
[research_olsen_1965]: https://doi.org/10.21236/ad0626928
[research_olsen_1966]: https://doi.org/10.21236/ad0647369
[research_olsonglenno_1982]: https://ntrs.nasa.gov/citations/20080004217
[research_om_park_2020]: https://doi.org/10.9728/jcc.2020.06.2.1.95
[research_omodei_1977]: https://doi.org/10.1137/0714080
[research_onat_tolle_1979]: https://doi.org/10.21236/ada074454
[research_onkar_2021]: https://doi.org/10.1007/s11012-021-01390-8
[research_onkar_kumar_2024]: https://doi.org/10.1007/s12046-024-02629-2
[research_operationaltechnologiescorpsanantoniotx_1996]: https://doi.org/10.21236/ada316165
[research_opgenoord_willcox_2019]: https://doi.org/10.2514/1.j058169
[research_optimizing_material_2025]: https://doi.org/10.64388/irev9i5-1711837
[research_orkwis_1995]: https://doi.org/10.21236/ada304583
[research_orlikruckemann_1983]: https://doi.org/10.2514/3.44938
[research_orourke_kolmanovsky_2019]: https://doi.org/10.1016/j.ifacol.2019.12.064
[research_osder_mossman_1976]: https://doi.org/10.2514/3.58699
[research_oshima_takano_2024]: https://doi.org/10.1016/j.addma.2024.104090
[research_osipov_2016]: https://doi.org/10.1615/tsagiscij.2017019838
[research_osipov_2017]: https://doi.org/10.1615/tsagiscij.2018026350
[research_osipov_2019]: https://doi.org/10.1615/tsagiscij.2019030599
[research_ossmann_joos_2016]: https://doi.org/10.1016/j.ifacol.2016.09.009
[research_ossmann_joos_2017]: https://doi.org/10.1002/rnc.3955
[research_ostheimer_giguere_1963]: https://doi.org/10.21236/ad0402379
[research_ostojic_sethi_2026]: https://doi.org/10.1016/j.ecoinf.2026.103946
[research_othman_silva_2019]: https://doi.org/10.1016/j.compstruct.2018.09.086
[research_otsuka_makihara_2017]: https://doi.org/10.1299/jsmedmc.2017.715
[research_ouyang_gu_2021]: https://doi.org/10.1016/j.ast.2020.106457
[research_ouyang_lin_2017]: https://doi.org/10.1002/rnc.3883
[research_ouyang_zeng_2021]: https://doi.org/10.1155/2021/5535192
[research_ouztspeterj_solowaydonaldi_2009]: https://ntrs.nasa.gov/citations/20100021410
[research_over_136_1981]: https://doi.org/10.1016/0010-4361(81)90026-4
[research_oyarhossein_sugiyama_2025]: https://doi.org/10.3390/buildings15213890
[research_oyibo_1984]: https://doi.org/10.2514/3.48423
[research_oza_vala_2021]: https://doi.org/10.34257/gjredvol21is1pg43
[research_ozbek_ekici_2024]: https://doi.org/10.1108/aeat-04-2024-0096
[research_ozdemir_2021]: https://doi.org/10.1080/0305215x.2021.2016733
[research_ozdil_carlsson_1992]: https://doi.org/10.1177/002199839202600306
[research_ozkan_2020]: https://doi.org/10.21605/cukurovaummfd.792424
[research_packard_seiler_2009]: https://doi.org/10.21236/ada531629
[research_padovan_1973]: https://doi.org/10.1177/002199837300700412
[research_padovan_1974]: https://doi.org/10.1115/1.3423249
[research_padovan_gosset_1974]: https://doi.org/10.2514/3.49342
[research_pagano_1974]: https://doi.org/10.1177/002199837400800106
[research_paine_1950]: https://doi.org/10.21236/adc953406
[research_palframan_fry_2019]: https://doi.org/10.1109/tcst.2017.2766598
[research_palkin_zenchenko_2025]: https://doi.org/10.18127/j20700784-202509-06
[research_palmtod_mahlermary_2000]: https://ntrs.nasa.gov/citations/20000052504
[research_pan_cheng_1995]: https://doi.org/10.2514/3.46853
[research_pan_huang_2019]: https://doi.org/10.5028/jatm.v11.1074
[research_pan_jin_2026]: https://doi.org/10.1016/j.autcon.2026.106959
[research_pan_liu_2019]: https://doi.org/10.2514/1.j058120
[research_pandey_murray_2022]: https://doi.org/10.1002/rnc.6013
[research_pangas_gamboa_2025]: https://doi.org/10.3390/aerospace12080685
[research_panuntun_wahyunggoro_2020]: https://doi.org/10.1088/1742-6596/1577/1/012031
[research_papadales_basils_1979]: https://doi.org/10.21236/ada073100
[research_papirno_1977]: https://doi.org/10.1177/002199837701100106
[research_parbery_karihaloo_1980]: https://doi.org/10.1115/1.3153585
[research_parbery_olhoff_1987]: https://doi.org/10.1080/08905458708905123
[research_park_2015]: https://doi.org/10.4028/www.scientific.net/kem.665.149
[research_park_2016]: https://doi.org/10.1177/0021998316643579
[research_park_choi_2017]: https://doi.org/10.2514/1.c034052
[research_park_jung_2017]: https://doi.org/10.5626/jok.2017.44.6.559
[research_park_kang_2026]: https://doi.org/10.6112/kscfe.2026.31.1.023
[research_park_oh_2017]: https://doi.org/10.14257/ijca.2017.10.12.01
[research_park_ramirezserrano_2024]: https://doi.org/10.3390/aerospace11080671
[research_park_ramirezserrano_2025]: https://doi.org/10.3390/aerospace12040312
[research_parker_simonson_1982]: https://doi.org/10.21236/adb069628
[research_parker_simonson_1982_b]: https://doi.org/10.21236/adb069402
[research_parker_simonson_1982_c]: https://doi.org/10.21236/adb069405
[research_parmar_singh_2022]: https://doi.org/10.1504/pcfd.2022.10052371
[research_parthivnshah_ericlblades_2023]: https://ntrs.nasa.gov/citations/20220001748
[research_passenbrunner_sassano_2016]: https://doi.org/10.1016/j.ejcon.2016.04.002
[research_passive_wing_store_1982]: https://doi.org/10.1121/1.387660
[research_patartics_liptak_2022]: https://doi.org/10.1109/tcst.2021.3066096
[research_pate_1964]: https://doi.org/10.21236/ad0450195
[research_pate_deitering_1963]: https://doi.org/10.21236/ad0297204
[research_patel_deodhare_2023]: https://doi.org/10.61653/joast.v58i4.2006.741
[research_patel_kumar_2022]: https://doi.org/10.1016/j.ifacol.2022.11.241
[research_patne_ingole_2020]: https://doi.org/10.1016/j.ifacol.2020.12.443
[research_patni_minera_2019]: https://doi.org/10.1016/j.compstruct.2019.111034
[research_patrickcmurphy_1999]: https://ntrs.nasa.gov/citations/19990032463
[research_pattarakunnan_galos_2021]: https://doi.org/10.1016/j.compstruct.2021.113845
[research_patterson_grenestedt_2018]: https://doi.org/10.1016/j.compstruct.2018.08.052
[research_paul_rein_2017]: https://doi.org/10.2514/1.c034080
[research_paulk_anderson_1976]: https://doi.org/10.21236/adb014346
[research_paulsonjwjr_thomasjl_1978]: https://ntrs.nasa.gov/citations/19780018153
[research_paulsonjwjr_thomasjl_1979]: https://ntrs.nasa.gov/citations/19790035660
[research_paulsonjwjr_thomasjl_1979_b]: https://ntrs.nasa.gov/citations/19800004739
[research_payton_2017]: https://doi.org/10.21660/2017.33.2565
[research_pc_implementation_1994]: https://doi.org/10.1016/0967-0661(94)90247-x
[research_pearsonhenrya_aikenwilliamsjr_1944]: https://ntrs.nasa.gov/citations/19930091876
[research_peck_hudson_1956]: https://doi.org/10.21236/ad0140230
[research_pedrioli_vaiuso_2026]: https://doi.org/10.1007/s13272-026-00961-3
[research_peledu_powelljd_1978]: https://ntrs.nasa.gov/citations/19780066300
[research_pellerin_1988]: https://doi.org/10.21236/ada197718
[research_pelykh_andryushchenko_2024]: https://doi.org/10.15587/2706-5448.2024.298600
[research_penafrancisco_2020]: https://ntrs.nasa.gov/citations/20200001121
[research_penafrancisco_martinsbenjamin_2018]: https://ntrs.nasa.gov/citations/20190033242
[research_pendem_2023]: https://doi.org/10.22214/ijraset.2023.52971
[research_pendleton_moster_1995]: https://doi.org/10.2514/3.46860
[research_peng_cao_2026]: https://doi.org/10.1109/tsmc.2026.3657656
[research_peng_chen_2022]: https://doi.org/10.1016/j.mechatronics.2022.102894
[research_peng_li_2026]: https://doi.org/10.1002/rnc.70594
[research_peng_zhang_1994]: https://doi.org/10.1080/00423119408969061
[research_peng_zhu_2020]: https://doi.org/10.1049/el.2019.3719
[research_pengelley_wilson_1954]: https://doi.org/10.21236/ad0061591
[research_pennycuick_1989]: https://doi.org/10.1242/jeb.142.1.1
[research_pereira_sales_2021]: https://doi.org/10.1016/j.compstruct.2020.112932
[research_perez_theodoulis_2022]: https://doi.org/10.1016/j.ifacol.2022.09.057
[research_perfect_jump_2015]: https://doi.org/10.2514/1.g001073
[research_perfect_jump_2015_b]: https://doi.org/10.2514/1.g000862
[research_perkins_brice_1966]: https://doi.org/10.21236/ad0632829
[research_perkins_jr_1977]: https://doi.org/10.21236/ada062274
[research_perry_2025]: https://doi.org/10.2514/1.c038025
[research_perry_rievley_1961]: https://doi.org/10.21236/ad0259391
[research_perrybiii_1976]: https://ntrs.nasa.gov/citations/19760011057
[research_perrybiii_1982]: https://ntrs.nasa.gov/citations/19820020423
[research_persoon_horsten_1984]: https://doi.org/10.2514/3.45061
[research_persoon_roos_1980]: https://doi.org/10.21236/ada097094
[research_petersdavida_1988]: https://ntrs.nasa.gov/citations/19880017772
[research_petersenkl_1981]: https://ntrs.nasa.gov/citations/19820030322
[research_petre_ashley_1976]: https://doi.org/10.2514/3.58707
[research_petriconi_lomazzi_2026]: https://doi.org/10.58286/33896
[research_petterssen_1953]: https://doi.org/10.1111/j.2153-3490.1953.tb01052.x
[research_peyada_ghosh_2023]: https://doi.org/10.61653/joast.v61i2.2009.524
[research_pfeifle_fichter_2023]: https://doi.org/10.2514/1.g006929
[research_pfnur_breitsamter_2019]: https://doi.org/10.2514/1.c035491
[research_pham_2022]: https://doi.org/10.56651/lqdtu.jst.v17.n02.312
[research_phan_2020]: https://doi.org/10.1016/j.istruc.2020.08.035
[research_philibert_yao_2022]: https://doi.org/10.1080/26889277.2022.2094839
[research_philippidis_1994]: https://doi.org/10.1515/secm.1994.3.1.39
[research_phillips_1965]: https://doi.org/10.1109/tac.1965.1098203
[research_phuekpan_khammee_2025]: https://doi.org/10.3390/aerospace12020101
[research_piao_zhang_2019]: https://doi.org/10.1177/1077546319849775
[research_picon_alarcon_1978]: https://doi.org/10.1016/0141-1195(78)90019-0
[research_pidaparti_1993]: https://doi.org/10.1016/0263-8223(93)90154-i
[research_pidaparti_yang_1993]: https://doi.org/10.2514/3.11735
[research_pierce_varga_1972]: https://doi.org/10.1137/0709014
[research_pierre_iervolino_2023]: https://doi.org/10.1016/j.addma.2022.103344
[research_pizzoli_saltari_2022]: https://doi.org/10.3390/app12178762
[research_place_altmann_1974]: https://doi.org/10.21236/ad0785104
[research_placek_ruchala_2018]: https://doi.org/10.1016/j.trpro.2018.02.029
[research_plaetschke_mulder_1982]: https://doi.org/10.1016/s1474-6670(17)63152-5
[research_platus_1980]: https://doi.org/10.21236/ada093741
[research_plotkin_1978]: https://doi.org/10.1115/1.3424324
[research_plyako_1977]: https://doi.org/10.1007/bf00967161
[research_poll_1986]: https://doi.org/10.1017/s0001924000015670
[research_pollack_theodoulis_2024]: https://doi.org/10.1016/j.ast.2024.109377
[research_pollack_theodoulis_2026]: https://doi.org/10.2514/1.g009559
[research_pollack_vankampen_2023]: https://doi.org/10.2514/1.g006576
[research_polonsky_2026]: https://doi.org/10.2514/1.c038869
[research_polyester_fibreglass_reinforced_1978]: https://doi.org/10.1016/0010-4361(78)90633-x
[research_poole_allen_2022]: https://doi.org/10.1007/s00158-022-03174-4
[research_poole_allen_2026]: https://doi.org/10.2514/1.c038630
[research_portapas_cooke_2020]: https://doi.org/10.3846/aviation.2020.12175
[research_posingies_1979]: https://doi.org/10.21236/ada070387
[research_poss_2018]: https://doi.org/10.1016/j.disopt.2017.09.004
[research_postnikov_sabaev_1968]: https://doi.org/10.1007/bf01133465
[research_pourtakdoust_khodabakhsh_2026]: https://doi.org/10.1016/j.ast.2025.111214
[research_poussotvassal_demourant_2017]: https://doi.org/10.1109/tcst.2016.2630505
[research_powellrichardw_1993]: https://ntrs.nasa.gov/citations/19930069740
[research_powers_1982]: https://doi.org/10.2514/3.56150
[research_powersbg_1980]: https://ntrs.nasa.gov/citations/19800061700
[research_prajapati_prasad_2019]: https://doi.org/10.1177/0142331219874595
[research_prasad_nematnasser_1967]: https://doi.org/10.2514/3.3959
[research_prasad_pesek_2018]: https://doi.org/10.1051/matecconf/201821115001
[research_prasannakumar_sudhi_2024]: https://doi.org/10.2514/1.c037398
[research_pratama_2021]: https://doi.org/10.28989/vortex.v2i2.1010
[research_preissler_schaufele_1991]: https://doi.org/10.2514/3.46003
[research_price_lee_1993]: https://doi.org/10.2514/3.56887
[research_pritt_1980]: https://doi.org/10.21236/ada106425
[research_property_changes_1981]: https://doi.org/10.1016/0010-4361(81)90051-3
[research_prototype_digital_1986]: https://doi.org/10.1108/eb036284
[research_pryor_barker_1970]: https://doi.org/10.1177/002199837000400410
[research_przekopadam_jegleydawnc_2014]: https://ntrs.nasa.gov/citations/20140010013
[research_przekopadam_jegleydawnc_2014_b]: https://ntrs.nasa.gov/citations/20150001217
[research_pusch_knoblach_2019]: https://doi.org/10.1007/s13272-019-00367-4
[research_pushtaev_1989]: https://doi.org/10.1016/0041-5553(89)90024-4
[research_puthisikamani_sreenivasaraja_2023]: https://doi.org/10.61653/joast.v74i4.2022.47
[research_putnamtw_1983]: https://ntrs.nasa.gov/citations/19840030937
[research_putnamtw_1984]: https://ntrs.nasa.gov/citations/19840008100
[research_putnamtw_1984_b]: https://ntrs.nasa.gov/citations/19850031744
[research_putnamtw_petersenkl_1986]: https://ntrs.nasa.gov/citations/19860046595
[research_qi_yuan_2026]: https://doi.org/10.1061/jaeeez.aseng-6518
[research_qi_zhao_2018]: https://doi.org/10.1109/taes.2018.2836598
[research_qi_zhao_2020]: https://doi.org/10.2514/1.g004761
[research_qian_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000925
[research_qian_gao_2026]: https://doi.org/10.1016/j.ast.2025.111115
[research_qian_lu_2025]: https://doi.org/10.1093/cdm/wqaf016
[research_qian_xinhui_2025]: https://doi.org/10.65904/3083-3450.2025.01.05
[research_qian_zhang_2015]: https://doi.org/10.1364/oe.23.018300
[research_qiao_gao_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.07.009
[research_qiao_wu_2018]: https://doi.org/10.1080/21642583.2018.1558421
[research_qin_liu_2017]: https://doi.org/10.1016/j.ast.2017.06.012
[research_qin_liu_2023]: https://doi.org/10.1049/cth2.12427
[research_qin_yang_2025]: https://doi.org/10.1063/5.0282127
[research_qing_liu_2020]: https://doi.org/10.1177/1475921720958082
[research_qiu_2022]: https://doi.org/10.21595/vp.2022.23045
[research_qiu_deng_2022]: https://doi.org/10.3389/fcteg.2021.771857
[research_qiu_fang_2018]: https://doi.org/10.1177/1475921718759344
[research_qiu_wang_2016]: https://doi.org/10.1155/2016/3848520
[research_qiu_yuan_2017]: https://doi.org/10.1177/1475921717692571
[research_qu_annaswamy_2016]: https://doi.org/10.2514/1.g001282
[research_qu_li_2022]: https://doi.org/10.1088/1742-6596/2258/1/012074
[research_quagliarella_iuliano_2017]: https://doi.org/10.1109/mci.2017.2742718
[research_quality_control_2020]: https://doi.org/10.38007/ml.2020.010306
[research_quero_vuillemin_2019]: https://doi.org/10.3390/aerospace6010009
[research_radetskaya_2022]: https://doi.org/10.18698/2541-8009-2022-10-833
[research_radfordrc_smithr_1980]: https://ntrs.nasa.gov/citations/19810005458
[research_rafi_steck_2017]: https://doi.org/10.2514/1.g002693
[research_ragab_hajj_2018]: https://doi.org/10.1504/ijad.2018.10010814
[research_raghav_komerath_2015]: https://doi.org/10.1063/1.4906803
[research_raghavan_1971]: https://doi.org/10.1080/00207177108931982
[research_rahima_yassine_2026]: https://doi.org/10.5935/jetia.v12i59.3437
[research_rainbird_peiro_2015]: https://doi.org/10.1016/j.jweia.2015.06.006
[research_raiola_discetti_2021]: https://doi.org/10.1016/j.expthermflusci.2020.110234
[research_raisrohanim_haftkart_1992]: https://ntrs.nasa.gov/citations/19930036310
[research_raisrohanimasoud_1994]: https://ntrs.nasa.gov/citations/19950016897
[research_raisrohanimasound_1999]: https://ntrs.nasa.gov/citations/19990064496
[research_rajamurugu_satyam_2024]: https://doi.org/10.4273/ijvss.16.1.04
[research_rajpal_kassapoglou_2019]: https://doi.org/10.1016/j.compstruct.2019.111248
[research_rajpal_mitrotta_2021]: https://doi.org/10.1016/j.compstruct.2021.114373
[research_ramamoorthy_1992]: https://doi.org/10.21236/ada252232
[research_ramdewangan_dewangan_2026]: https://doi.org/10.1002/adc2.70051
[research_ramroop_chinchamee_2025]: https://doi.org/10.14455/isec.2025.12(1).str-54
[research_ranaudorichardj_ratvaskythomasp_2000]: https://ntrs.nasa.gov/citations/20000120385
[research_raneydavidl_1987]: https://ntrs.nasa.gov/citations/19870062350
[research_rao_1975]: https://doi.org/10.1016/s0022-460x(75)80007-1
[research_rao_hofer_1973]: https://doi.org/10.21236/ada305383
[research_rao_padmanabhan_2019]: https://doi.org/10.1504/ijndc.2019.103285
[research_rao_shi_2023]: https://doi.org/10.3390/aerospace10050420
[research_rao_umamaheswararao_1992]: https://doi.org/10.1016/0263-8223(92)90002-t
[research_raouf_1994]: https://doi.org/10.1016/0263-8223(94)90023-x
[research_raper_1991]: https://doi.org/10.21236/ada240387
[research_rapoffandrewj_dillharoldd_1990]: https://ntrs.nasa.gov/citations/19920023336
[research_rashed_demir_2022]: https://doi.org/10.1016/j.compstruct.2021.115151
[research_rashmikant_abe_2026]: https://doi.org/10.1016/j.ast.2026.112653
[research_rate_sensitivity_1988]: https://doi.org/10.1016/0010-4361(88)90610-6
[research_rath_fichter_2020]: https://doi.org/10.4050/jahs.66.022003
[research_rathnasabapathy_mouritz_2022]: https://doi.org/10.1016/j.compstruct.2022.115368
[research_rauer_2019]: https://doi.org/10.1007/s42496-019-00020-7
[research_rayankula_pathak_2021]: https://doi.org/10.1007/s10846-021-01317-1
[research_rayej_mckinneylw_1972]: https://ntrs.nasa.gov/citations/19730006292
[research_rayej_mckinneylw_1973]: https://ntrs.nasa.gov/citations/19730017272
[research_rea_pecora_2017]: https://doi.org/10.18178/ijmerr.6.6.
[research_rea_pecora_2018]: https://doi.org/10.18178/ijmerr.6.6.440-450
[research_reader_1976]: https://doi.org/10.21236/ada026548
[research_reajbcoincsantamonicaca_1957]: https://doi.org/10.21236/ad0126837
[research_recaluque_aguilartorres_2023]: https://doi.org/10.6036/10630
[research_reddy_1982]: https://doi.org/10.1016/0015-0568(82)90058-6
[research_reddy_1987]: https://doi.org/10.2514/3.45421
[research_redeker_wichmann_1991]: https://doi.org/10.2514/3.45997
[research_rediessha_szalaikj_1975]: https://ntrs.nasa.gov/citations/19750020942
[research_reding_ericsson_1977]: https://doi.org/10.2514/3.58883
[research_reed_1994]: https://doi.org/10.5957/jsr.1994.38.2.133
[research_reeder_1958]: https://doi.org/10.4050/jahs.3.4
[research_refinement_of_2023]: https://doi.org/10.36652/0869-4931-2023-77-2-86-94
[research_regulator_with_2022]: https://doi.org/10.36652/0869-4931-2022-76-2-73-77
[research_rehan_iqbal_2015]: https://doi.org/10.1002/rnc.3372
[research_rehman_2022]: https://doi.org/10.13111/2066-8201.2022.14.3.8
[research_rehman_ekici_2025]: https://doi.org/10.1016/j.cjph.2025.02.015
[research_reid_rajagopal_1994]: https://doi.org/10.2514/3.46607
[research_reinbold_breitsamter_2026]: https://doi.org/10.2514/1.c038409
[research_reist_koo_2020]: https://doi.org/10.2514/1.j059091
[research_reist_koo_2022]: https://doi.org/10.2514/1.c036754
[research_reist_zingg_2019]: https://doi.org/10.2514/1.c034703
[research_rekik_khaled_2024]: https://doi.org/10.1109/access.2024.3501682
[research_ren_1986]: https://doi.org/10.1016/0266-3538(86)90033-3
[research_ren_lissenden_2016]: https://doi.org/10.1177/1475921716650627
[research_ren_qiu_2017]: https://doi.org/10.3390/ma10050519
[research_ren_qiu_2018]: https://doi.org/10.1177/1475921717752661
[research_ren_xu_2025]: https://doi.org/10.1109/tase.2025.3532632
[research_ren_zhang_2022]: https://doi.org/10.1155/2022/7904892
[research_repa_alexandridis_1977]: https://doi.org/10.1080/00423117708968535
[research_report_no_1921]: https://doi.org/10.1016/s0016-0032(21)90863-9
[research_report_no_1930]: https://doi.org/10.1016/s0016-0032(30)90271-2
[research_research_and_2022]: https://doi.org/10.47939/et.v3i2.104
[research_research_on_2023]: https://doi.org/10.23977/acss.2023.070616
[research_research_on_2025]: https://doi.org/10.3901/jme.2025.05.228
[research_resta_marsilio_2021]: https://doi.org/10.3390/fluids6120441
[research_restifo_villa_2026]: https://doi.org/10.1016/j.mlwa.2026.100896
[research_review_of_2024]: https://doi.org/10.3901/jme.2024.04.050
[research_reyes_climent_2019]: https://doi.org/10.1007/s13272-019-00361-w
[research_rhodesmd_selbergbp_1982]: https://ntrs.nasa.gov/citations/19820057396
[research_richards_1979]: https://doi.org/10.21236/ada088129
[research_richards_yao_2016]: https://doi.org/10.2514/1.c033435
[research_richardson_2007]: https://doi.org/10.21236/ada477122
[research_richmj_ridgleygf_1974]: https://ntrs.nasa.gov/citations/19740053860
[research_richter_calix_2024]: https://doi.org/10.1109/access.2024.3433540
[research_richwinedavidm_fisherdavidf_1991]: https://ntrs.nasa.gov/citations/19910069136
[research_rickardww_1978]: https://ntrs.nasa.gov/citations/19780062649
[research_rickettsrh_doggettrvjr_1980]: https://ntrs.nasa.gov/citations/19800020786
[research_rickettsrh_sandfordmc_1983]: https://ntrs.nasa.gov/citations/19830048631
[research_rickettsrh_watsonjj_1983]: https://ntrs.nasa.gov/citations/19860014096
[research_rieck_herrmann_2026]: https://doi.org/10.1007/s13272-026-00991-x
[research_ried_1986]: https://doi.org/10.17764/jiet.1.29.5.k3328013777g1067
[research_riefe_1946]: https://doi.org/10.21236/adb813732
[research_rigatos_2021]: https://doi.org/10.1142/s2737480721500126
[research_rimer_chipman_1984]: https://doi.org/10.2514/3.45034
[research_rimer_chipman_1986]: https://doi.org/10.2514/3.20069
[research_rimerm_chipmanr_1984]: https://ntrs.nasa.gov/citations/19840060637
[research_ringertz_1994]: https://doi.org/10.1007/bf01742928
[research_rinoie_komuro_2015]: https://doi.org/10.2514/1.c032484
[research_risingjj_daviswj_1984]: https://ntrs.nasa.gov/citations/19850030442
[research_riso_cesnik_2023]: https://doi.org/10.1016/j.jfluidstructs.2023.103897
[research_rittenhouse_1959]: https://doi.org/10.21236/ad0207771
[research_ritter_gurley_1971]: https://doi.org/10.21236/ad0894406
[research_rivero_fournier_2021]: https://doi.org/10.2514/1.j059606
[research_rizzetta_1977]: https://doi.org/10.21236/ada057505
[research_rizzetta_1979]: https://doi.org/10.2514/3.61058
[research_rizzetta_visbal_2016]: https://doi.org/10.2514/1.c033596
[research_roache_1965]: https://doi.org/10.2514/3.59234
[research_robbins_stansbury_2023]: https://doi.org/10.1504/ijvd.2023.10060015
[research_roberts_1986]: https://doi.org/10.17764/jiet.1.29.5.bg524k2wr7355x02
[research_roberts_reed_2015]: https://doi.org/10.2514/1.c032779
[research_roberts_smith_1966]: https://doi.org/10.21236/ad0635953
[research_robertspa_swaimrl_1977]: https://ntrs.nasa.gov/citations/19770016183
[research_robinson_2004]: https://doi.org/10.21236/ada425641
[research_robotics_2024]: https://doi.org/10.1155/2024/9785472
[research_robust_controller_2016]: https://doi.org/10.21311/001.39.6.30
[research_rocha_antunes_2023]: https://doi.org/10.1177/14759217231204242
[research_rockwell_1994]: https://doi.org/10.21236/ada278988
[research_rodden_1981]: https://doi.org/10.2514/3.44744
[research_rodden_1984]: https://doi.org/10.2514/3.56737
[research_rodden_1989]: https://doi.org/10.2514/3.45825
[research_rodden_1989_b]: https://doi.org/10.2514/3.45842
[research_rodden_bellinger_1982]: https://doi.org/10.2514/3.61559
[research_rodemich_andrew_1965]: https://doi.org/10.21236/ad0618097
[research_rodgers_1965]: https://doi.org/10.2514/3.43615
[research_rodgers_1966]: https://doi.org/10.2514/3.43765
[research_rodino_maletta_2024]: https://doi.org/10.1016/j.pes.2024.100021
[research_rogalski_2018]: https://doi.org/10.1108/aeat-02-2018-0088
[research_rogalski_rzucidlo_2020]: https://doi.org/10.1108/aeat-05-2019-0099
[research_rogalski_rzucidlo_2021]: https://doi.org/10.1108/aeat-11-2020-0269
[research_rogers_1970]: https://doi.org/10.21236/ada367071
[research_rogersten_xu_2013]: https://doi.org/10.21236/ada587237
[research_rogolski_olejnik_2018]: https://doi.org/10.1108/aeat-01-2018-0059
[research_roh_park_2024]: https://doi.org/10.3390/buildings15010017
[research_rohella_chatterjee_1979]: https://doi.org/10.1080/03772063.1979.11451847
[research_rohith_sinha_2020]: https://doi.org/10.1007/s11071-020-05604-8
[research_rohn_loewenthal_1985]: https://doi.org/10.1115/1.3260765
[research_roizner_karpel_2018]: https://doi.org/10.2514/1.j056514
[research_roizner_karpel_2019]: https://doi.org/10.2514/1.c035286
[research_roizner_raveh_2019]: https://doi.org/10.2514/1.c035045
[research_rokhsaz_selberg_1990]: https://doi.org/10.2514/3.25271
[research_rom_lamar_1992]: https://doi.org/10.2514/3.48952
[research_romano_ciminello_2019]: https://doi.org/10.1177/0021998319843333
[research_romkes_prudhomme_2002]: https://doi.org/10.21236/ada438102
[research_ronflenadaud_2009]: https://doi.org/10.21236/ada512960
[research_rong_dou_2023]: https://doi.org/10.5194/ms-14-399-2023
[research_rong_huang_2022]: https://doi.org/10.1002/acs.3390
[research_rongrong_zhengyin_2018]: https://doi.org/10.1177/0954410018807810
[research_rooneyrh_chungjc_1982]: https://ntrs.nasa.gov/citations/19820055409
[research_roorda_1967]: https://doi.org/10.1061/jmcea3.0000919
[research_roos_mushlin_1989]: https://doi.org/10.1109/23.34590
[research_rosa_pouca_2023]: https://doi.org/10.1016/j.jmapro.2023.02.012
[research_rosa_susanto_2022]: https://doi.org/10.21303/2461-4262.2022.002469
[research_roscoe_eisele_1975]: https://doi.org/10.21236/ada022459
[research_rose_seginer_1978]: https://doi.org/10.2514/3.58399
[research_rosema_doyle_2011]: https://doi.org/10.21236/ada548461
[research_rosema_doyle_2014]: https://doi.org/10.21236/ad1000581
[research_rosenblum_vrchota_2019]: https://doi.org/10.1007/s13272-019-00402-4
[research_rosenbruces_1988]: https://ntrs.nasa.gov/citations/19880034776
[research_rosenkrantz_1985]: https://doi.org/10.21236/ada159402
[research_rosique_alamin_2019]: https://doi.org/10.1016/j.ifacol.2019.11.293
[research_roskamj_lanc_1972]: https://ntrs.nasa.gov/citations/19730013170
[research_roskamj_lanc_1973]: https://ntrs.nasa.gov/citations/19730013169
[research_roufaeil_dawe_1982]: https://doi.org/10.1016/0022-460x(82)90521-1
[research_rouhi_ghayoor_2018]: https://doi.org/10.1016/j.compstruct.2017.09.090
[research_rowley_2008]: https://doi.org/10.21236/ada476708
[research_roy_mukherjee_2026]: https://doi.org/10.1016/j.euromechflu.2025.204348
[research_roylance_1980]: https://doi.org/10.1177/002199838001400203
[research_ruhlin_rauch_1983]: https://doi.org/10.2514/3.44933
[research_rumble_1987]: https://doi.org/10.21236/ada194418
[research_runkel_fasel_2018]: https://doi.org/10.1016/j.compstruct.2018.07.095
[research_runyan_cunningham_1952]: https://doi.org/10.2514/8.2220
[research_ruo_malone_1985]: https://doi.org/10.2514/3.45076
[research_ruscheweyh_1983]: https://doi.org/10.1016/0167-6105(83)90017-x
[research_rustenburg_1972]: https://doi.org/10.21236/ada004456
[research_rutkowski_1979]: https://doi.org/10.2514/3.58539
[research_ryder_walker_1976]: https://doi.org/10.21236/ada043365
[research_s_sinha_2018]: https://doi.org/10.1016/j.ifacol.2018.05.052
[research_sabater_bekemeyer_2022]: https://doi.org/10.2514/1.j060676
[research_sabatini_coppotelli_2026]: https://doi.org/10.2514/1.g009632
[research_sabido_bahamonde_2017]: https://doi.org/10.1016/j.compstruct.2016.10.081
[research_sabri_elzaabalawy_2022]: https://doi.org/10.1007/s00707-021-03138-7
[research_sachan_padhi_2020]: https://doi.org/10.1016/j.conengprac.2020.104526
[research_sachs_1975]: https://doi.org/10.2514/3.44471
[research_sachs_1977]: https://doi.org/10.2514/3.44623
[research_sachs_1979]: https://doi.org/10.1080/00423117908968599
[research_sachs_muvdi_1956]: https://doi.org/10.21236/ad0091083
[research_saddington_thangamani_2016]: https://doi.org/10.2514/1.c033365
[research_saderla_dhayalan_2016]: https://doi.org/10.14429/dsj.67.9995
[research_saderla_kim_2018]: https://doi.org/10.1016/j.ast.2018.07.008
[research_sadien_roos_2020]: https://doi.org/10.1016/j.conengprac.2019.104228
[research_sadoffmelvin_mcfaddennormanm_1961]: https://ntrs.nasa.gov/citations/19980227090
[research_saetti_2025]: https://doi.org/10.4050/jahs.70.042007
[research_saetti_2025_b]: https://doi.org/10.4050/jahs.70.032005
[research_saetti_horn_2020]: https://doi.org/10.2514/1.g004965
[research_saetti_rogers_2024]: https://doi.org/10.4050/jahs.69.042007
[research_saheby_jialu_2026]: https://doi.org/10.1016/j.ast.2025.111026
[research_sahin_yaman_2018]: https://doi.org/10.1051/matecconf/201818804001
[research_sahin_yaman_2018_b]: https://doi.org/10.3390/aerospace5040127
[research_sahin_yayla_2026]: https://doi.org/10.1016/j.ast.2026.113372
[research_sahu_heavey_2000]: https://doi.org/10.21236/ada384925
[research_sahyoun_boose_2026]: https://doi.org/10.1007/s13272-026-00954-2
[research_sakthivel_venkatesan_2017]: https://doi.org/10.2514/1.c034226
[research_salagame_pandya_2025]: https://doi.org/10.1109/lcsys.2025.3589412
[research_salahudden_2025]: https://doi.org/10.1109/taes.2024.3485604
[research_salahudden_agrawal_2024]: https://doi.org/10.1016/j.ast.2024.109156
[research_salichon_guy_1994]: https://doi.org/10.1051/animres:19940210
[research_sallyaviken_craigahunter_2022]: https://ntrs.nasa.gov/citations/20205007879
[research_saltzmanedwinj_hicksjohnw_1994]: https://ntrs.nasa.gov/citations/19950012150
[research_salwan_hussain_2026]: https://doi.org/10.33140/jeci.03.02.02
[research_sammondsroberti_mcneillwaltere_1982]: https://ntrs.nasa.gov/citations/19980201422
[research_sampling_schemes_1961]: https://doi.org/10.1109/tac.1961.6429318
[research_samputh_moey_2024]: https://doi.org/10.3846/aviation.2024.21495
[research_samukham_raju_2017]: https://doi.org/10.1016/j.compstruct.2017.01.044
[research_samukham_raju_2019]: https://doi.org/10.1016/j.tws.2019.02.015
[research_samukham_vyasarayani_2020]: https://doi.org/10.1016/j.compstruct.2019.111637
[research_sanders_1965]: https://doi.org/10.2514/3.43662
[research_sandhu_wolfe_1991]: https://doi.org/10.21236/ada251659
[research_sang_zhang_2022]: https://doi.org/10.1002/acs.3525
[research_santich_1985]: https://doi.org/10.1558/ppc.30968
[research_saporito_daronch_2023]: https://doi.org/10.1016/j.ast.2023.108349
[research_saputra_purabaya_2018]: https://doi.org/10.1088/1742-6596/1005/1/012019
[research_saraeian_shirazi_2022]: https://doi.org/10.1016/j.isatra.2022.03.007
[research_sarao_samanta_2022]: https://doi.org/10.2139/ssrn.4269263
[research_saric_1997]: https://doi.org/10.21236/ada388392
[research_sarkar_huang_2026]: https://doi.org/10.1016/j.mlwa.2026.100843
[research_sato_1973]: https://doi.org/10.2514/3.6669
[research_sato_muraoka_2017]: https://doi.org/10.2514/1.c034244
[research_savelev_neretin_2022]: https://doi.org/10.14489/vkit.2022.10.pp.003-014
[research_savin_hantraisgervois_2020]: https://doi.org/10.1016/j.probengmech.2020.103027
[research_saviolo_loianno_2023]: https://doi.org/10.1016/j.arcontrol.2023.03.009
[research_savithri_varadan_1990]: https://doi.org/10.1016/0022-460x(90)90534-7
[research_sawyerjw_1976]: https://ntrs.nasa.gov/citations/19760047048
[research_schafer_vidy_2018]: https://doi.org/10.1007/s13272-018-0353-9
[research_schatz_hermanutz_2016]: https://doi.org/10.1007/s00158-016-1541-z
[research_schewe_mai_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.04.021
[research_schieni_modasiya_2024]: https://doi.org/10.2514/1.g008048
[research_schildkamp_chang_2023]: https://doi.org/10.3390/act12070280
[research_schiop_1979]: https://doi.org/10.1080/01630567908816033
[research_schloesser_soudakov_2019]: https://doi.org/10.2514/1.j057345
[research_schmeichel_1967]: https://doi.org/10.21236/ad0658073
[research_schmidt_2016]: https://doi.org/10.2514/1.g001484
[research_schmidt_2016_b]: https://doi.org/10.2514/1.c033539
[research_schmidt_danowsky_2020]: https://doi.org/10.2514/1.c035720
[research_schmidtdavidk_schiermanjohnd_1990]: https://ntrs.nasa.gov/citations/19900060642
[research_schneider_1976]: https://doi.org/10.21236/ada025795
[research_schpey_1980]: https://doi.org/10.21236/ada083721
[research_schreadley_1977]: https://doi.org/10.21236/ada043979
[research_schroederjefferya_chungwilliamwy_2001]: https://ntrs.nasa.gov/citations/20010037958
[research_schueltke_stumpf_2017]: https://doi.org/10.1108/aeat-11-2016-0210
[research_schuet_lombaerts_2017]: https://doi.org/10.2514/1.g001729
[research_schulein_schnepf_2022]: https://doi.org/10.2514/1.j060799
[research_schultz_1969]: https://doi.org/10.1016/0022-247x(69)90133-4
[research_schultz_1969_b]: https://doi.org/10.1137/0706047
[research_schultz_1970]: https://doi.org/10.2307/2004878
[research_schultz_1971]: https://doi.org/10.1137/0708067
[research_schuster_1995]: https://doi.org/10.2514/3.46686
[research_schusterdavidm_edwardsjohnw_2004]: https://ntrs.nasa.gov/citations/20040086524
[research_schutte_huber_2018]: https://doi.org/10.2514/1.c033700
[research_schwanz_1972]: https://doi.org/10.21236/ada006391
[research_schwerdt_maroldt_2023]: https://doi.org/10.33737/jgpps/161707
[research_sciuva_1992]: https://doi.org/10.1016/0263-8223(92)90003-u
[research_scordamaglia_mattei_2025]: https://doi.org/10.1109/ojcsys.2025.3619810
[research_scott_bartels_2016]: https://doi.org/10.2514/1.g000265
[research_sebghati_shamaghdari_2020]: https://doi.org/10.1002/rnc.5192
[research_seckel_graziani_1956]: https://doi.org/10.21236/ad0119202
[research_seegmiller_1963]: https://doi.org/10.1109/tce.1963.6373252
[research_segel_1952]: https://doi.org/10.21236/ada076043
[research_seidel_eckstrom_1989]: https://doi.org/10.2514/3.45853
[research_seidel_sandford_1987]: https://doi.org/10.2514/3.45430
[research_seidelda_sandfordmc_1985]: https://ntrs.nasa.gov/citations/19850048176
[research_seitz_hubner_2019]: https://doi.org/10.1007/s13272-019-00421-1
[research_sekhar_suresh_2024]: https://doi.org/10.1051/matecconf/202439201016
[research_sekimoto_kato_2022]: https://doi.org/10.3390/aerospace9030144
[research_selbergbp_cronindl_1985]: https://ntrs.nasa.gov/citations/19850008520
[research_sellerswilliamliii_meyersjamesf_1988]: https://ntrs.nasa.gov/citations/19890040847
[research_sellerswilliamliii_meyersjamesf_2004]: https://ntrs.nasa.gov/citations/20040161542
[research_sen_bhattacharya_2016]: https://doi.org/10.1002/stc.1961
[research_sengupta_ferris_1973]: https://doi.org/10.1109/tap.1973.1140539
[research_sengupta_roy_2021]: https://doi.org/10.1063/5.0075692
[research_seraj_ganesan_2018]: https://doi.org/10.1016/j.compstruct.2018.05.133
[research_serakos_1992]: https://doi.org/10.21236/ada264733
[research_serani_diez_2024]: https://doi.org/10.1016/j.ast.2024.109611
[research_seres_liu_2023]: https://doi.org/10.1016/j.ifacol.2023.10.1097
[research_sergiev_gusev_1979]: https://doi.org/10.1007/bf01176314
[research_serhat_bediz_2020]: https://doi.org/10.1016/j.compstruct.2020.112183
[research_seshadri_krishnamurthy_2017]: https://doi.org/10.2514/1.c033940
[research_setiawarman_sasongko_2026]: https://doi.org/10.1142/s2737480726400078
[research_seyoung_1990]: https://doi.org/10.1016/0020-7683(90)90098-g
[research_sha_sun_2022]: https://doi.org/10.34759/vst-2022-4-22-35
[research_shafei_faroughi_2024]: https://doi.org/10.1016/j.compstruct.2024.117917
[research_shafermaryf_steinmetzpaul_2001]: https://ntrs.nasa.gov/citations/20010038270
[research_shafermaryf_steinmetzpaul_2001_b]: https://ntrs.nasa.gov/citations/20010037948
[research_shafermf_1980]: https://ntrs.nasa.gov/citations/19800061745
[research_shafermf_smithre_1983]: https://ntrs.nasa.gov/citations/19830060718
[research_shafermf_smithre_1984]: https://ntrs.nasa.gov/citations/19840008145
[research_shafighfard_demir_2019]: https://doi.org/10.1016/j.compstruct.2019.111280
[research_shah_desai_1973]: https://doi.org/10.1080/00207177308932460
[research_shah_mehta_2017]: https://doi.org/10.1016/j.dcan.2016.09.006
[research_shakya_padhee_2023]: https://doi.org/10.1016/j.compositesa.2023.107546
[research_shan_bilgen_2022]: https://doi.org/10.1016/j.jfluidstructs.2022.103724
[research_shan_tian_2019]: https://doi.org/10.1142/s0219455419501025
[research_shang_xia_2024]: https://doi.org/10.1061/jaeeez.aseng-5259
[research_shankar_malmuth_1981]: https://doi.org/10.2514/3.44699
[research_shankar_malmuth_1982]: https://doi.org/10.21236/ada121662
[research_shankar_malmuth_1983]: https://doi.org/10.2514/3.44893
[research_shanley_1943]: https://doi.org/10.1108/eb031034
[research_shantz_demeritte_1958]: https://doi.org/10.21236/ad0309255
[research_shao_li_2026]: https://doi.org/10.2514/1.c038254
[research_shao_sun_2025]: https://doi.org/10.1007/s11029-025-10258-x
[research_sharif_abbas_2022]: https://doi.org/10.47893/gret.2022.1084
[research_sharifi_vincenti_2025]: https://doi.org/10.1016/j.compstruct.2025.118839
[research_sharma_agrawal_2022]: https://doi.org/10.1016/j.ifacol.2023.03.027
[research_sharma_swain_2023]: https://doi.org/10.1177/00219983231175468
[research_sharp_wilson_1990]: https://doi.org/10.1080/00423119008968952
[research_sharqi_cesnik_2023]: https://doi.org/10.2514/1.c036894
[research_shawki_mashhour_1974]: https://doi.org/10.1007/bf02323065
[research_shayak_girdhar_2024]: https://doi.org/10.3389/fpace.2024.1308872
[research_shcherban_sterlin_2022]: https://doi.org/10.26896/1028-6861-2022-88-4-66-75
[research_shearwood_nabawy_2020]: https://doi.org/10.3390/aerospace7100150
[research_sheikh_lee_2023]: https://doi.org/10.1093/jcde/qwad059
[research_sheikhi_rafieianamagh_2024]: https://doi.org/10.1016/j.compstruct.2023.117836
[research_sheikhi_rafieianamagh_2024_b]: https://doi.org/10.1016/j.matdes.2024.113142
[research_sheldon_1967]: https://doi.org/10.21236/ad0856658
[research_shen_bai_2015]: https://doi.org/10.21742/ijiace.2015.2.2.02
[research_shen_chang_2022]: https://doi.org/10.1088/1742-6596/2338/1/012092
[research_shen_chen_2022]: https://doi.org/10.1002/oca.2952
[research_shen_chen_2023]: https://doi.org/10.1108/aeat-09-2022-0250
[research_shen_chen_2024]: https://doi.org/10.1109/tcyb.2022.3213178
[research_shen_huang_2021]: https://doi.org/10.1016/j.cja.2020.07.022
[research_shen_wen_2018]: https://doi.org/10.2514/1.j056565
[research_sheng_zhao_2017]: https://doi.org/10.2514/1.c034134
[research_shepheard_1965]: https://doi.org/10.21236/ad0630924
[research_shermer_1980]: https://doi.org/10.62913/engj.v17i2.350
[research_sherrer_hertz_1981]: https://doi.org/10.2514/3.57589
[research_sheshanarayana_armstrong_2026]: https://doi.org/10.2514/1.c037564
[research_shi_bezine_1988]: https://doi.org/10.1177/002199838802200801
[research_shi_gao_2025]: https://doi.org/10.3390/aerospace12060532
[research_shi_gao_2026]: https://doi.org/10.1016/j.ast.2025.110884
[research_shi_lan_2023]: https://doi.org/10.1007/s00158-023-03559-z
[research_shi_liu_2020]: https://doi.org/10.3390/fluids5010034
[research_shi_liu_2021]: https://doi.org/10.3390/aerospace8120390
[research_shi_liu_2024]: https://doi.org/10.1016/j.jcsr.2024.108917
[research_shi_liu_2024_b]: https://doi.org/10.1016/j.istruc.2024.107425
[research_shi_liu_2024_c]: https://doi.org/10.1063/5.0203775
[research_shi_lyu_2019]: https://doi.org/10.1109/access.2019.2938013
[research_shi_mader_2021]: https://doi.org/10.1007/s00158-021-02936-w
[research_shi_tan_2018]: https://doi.org/10.1360/n092017-00215
[research_shi_wan_2015]: https://doi.org/10.1108/aeat-01-2013-0004
[research_shi_wang_2022]: https://doi.org/10.3390/drones6100272
[research_shi_wang_2023]: https://doi.org/10.1088/1742-6596/2658/1/012023
[research_shi_zhu_2024]: https://doi.org/10.1016/j.actaastro.2024.02.005
[research_shiau_chang_1991]: https://doi.org/10.1016/0045-7949(91)90025-h
[research_shibahata_shimada_1993]: https://doi.org/10.1080/00423119308969044
[research_shieh_chen_1998]: https://doi.org/10.21236/ada344559
[research_shields_cook_1971]: https://doi.org/10.1080/00207177108932075
[research_shimoda_nagano_2018]: https://doi.org/10.1007/s00158-018-2144-7
[research_shinde_ohol_2021]: https://doi.org/10.2139/ssrn.3808560
[research_shiota_ohmori_2015]: https://doi.org/10.1016/j.ifacol.2015.09.436
[research_shirk_hertz_1986]: https://doi.org/10.2514/3.45260
[research_shivam_verma_2019]: https://doi.org/10.13111/2066-8201.2019.11.2.14
[research_shladover_1995]: https://doi.org/10.1080/00423119508969108
[research_shmilovich_princen_2026]: https://doi.org/10.2514/1.c038755
[research_shmilovich_yadlin_2026]: https://doi.org/10.2514/1.c037586
[research_shneen_2026]: https://doi.org/10.59247/jfsc.v3i3.345
[research_shoales_fawaz_2004]: https://doi.org/10.21236/ada430478
[research_shojae_salehi_2025]: https://doi.org/10.1016/j.oceaneng.2025.121086
[research_shomber_gertsen_1967]: https://doi.org/10.2514/3.43851
[research_short_1995]: https://doi.org/10.1016/0010-4361(95)90916-n
[research_shrivastava_mohite_2015]: https://doi.org/10.1515/cls-2015-0010
[research_shrivastava_sharma_2020]: https://doi.org/10.1016/j.compstruct.2020.112518
[research_shrivastava_stengel_1989]: https://doi.org/10.2514/3.20369
[research_shrivastava_tilala_2020]: https://doi.org/10.1007/s00158-020-02569-5
[research_shrivastavapc_1987]: https://ntrs.nasa.gov/citations/19870013189
[research_shtessel_2001]: https://doi.org/10.21236/ada396963
[research_shukla_benyamen_2025]: https://doi.org/10.1109/tcst.2024.3516383
[research_shukla_pradyumna_2021]: https://doi.org/10.1016/j.compstruct.2021.113792
[research_shyprykevichp_1979]: https://ntrs.nasa.gov/citations/19800036960
[research_si_baier_2016]: https://doi.org/10.1177/1475921716636334
[research_sibert_1937]: https://doi.org/10.2514/8.367
[research_sibert_1943]: https://doi.org/10.2514/8.10986
[research_siddamma_seervi_2026]: https://doi.org/10.55248/gengpi.07.0226.0235
[research_siddiqui_elferik_2016]: https://doi.org/10.1016/j.ifacol.2016.07.510
[research_siem_murray_1997]: https://doi.org/10.21236/ada459823
[research_silton_fresconi_2014]: https://doi.org/10.21236/ada611082
[research_silton_fresconi_2015]: https://doi.org/10.2514/1.a33219
[research_silvaleon_cioncolini_2020]: https://doi.org/10.3390/fluids5020090
[research_silvawaltera_bennettrobertm_1990]: https://ntrs.nasa.gov/citations/19900010731
[research_sim_lee_2024]: https://doi.org/10.3390/jmse12020262
[research_simbuerger_raveh_2022]: https://doi.org/10.2514/1.c036626
[research_simmonds_1971]: https://doi.org/10.1090/qam/99753
[research_simmons_2023]: https://doi.org/10.1111/jzo.13117
[research_simmons_2023_b]: https://doi.org/10.2514/1.c036896
[research_simmons_gresham_2023]: https://doi.org/10.2514/1.c036773
[research_simon_harkegard_2017]: https://doi.org/10.2514/1.g002272
[research_simos_jenkinson_1988]: https://doi.org/10.2514/3.45632
[research_simplicio_acquatella_2025]: https://doi.org/10.3390/aerospace12040296
[research_simpson_1969]: https://doi.org/10.1137/0706024
[research_simpson_1988]: https://doi.org/10.1017/s0001924000022028
[research_simsrobert_mccrossonpaul_1989]: https://ntrs.nasa.gov/citations/19900009909
[research_sineglazov_2015]: https://doi.org/10.18372/1990-5548.46.9966
[research_singer_1989]: https://doi.org/10.1007/bf02321376
[research_singh_brown_2016]: https://doi.org/10.2514/1.c033658
[research_singh_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1050
[research_singh_parmar_2023]: https://doi.org/10.1504/pcfd.2023.134897
[research_singh_raisinghani_1993]: https://doi.org/10.2514/3.46373
[research_singh_yadav_2024]: https://doi.org/10.62486/latia202493
[research_singhvi_kapania_1994]: https://doi.org/10.1061/(asce)0733-9399(1994)120:10(2126)
[research_singpurwalla_wong_1980]: https://doi.org/10.21236/ada099430
[research_sinha_klimmek_2021]: https://doi.org/10.1007/s13272-021-00494-x
[research_siraskar_2021]: https://doi.org/10.1016/j.mlwa.2021.100030
[research_sisson_dogan_2026]: https://doi.org/10.1002/acs.70091
[research_sisson_karve_2022]: https://doi.org/10.1007/s00158-022-03413-8
[research_sitzjoelr_vernontoddh_1990]: https://ntrs.nasa.gov/citations/19930021575
[research_sivanandi_sanjay_2025]: https://doi.org/10.3390/eng6120354
[research_sizlotr_bergra_1979]: https://ntrs.nasa.gov/citations/19820024501
[research_skarolek_jkarabelas_2016]: https://doi.org/10.1016/j.apm.2015.09.028
[research_skf_divests_2016]: https://doi.org/10.1016/j.mprp.2016.04.079
[research_sleesongsom_kumar_2022]: https://doi.org/10.3390/sym14102125
[research_sleptsov_andrianova_2021]: https://doi.org/10.1016/j.ifacol.2021.10.446
[research_sliwasm_1980]: https://ntrs.nasa.gov/citations/19810005457
[research_smeltzer_durston_1983]: https://doi.org/10.2514/3.44950
[research_smetana_1973]: https://doi.org/10.21236/ad0763295
[research_smith_1967]: https://doi.org/10.21236/ad0816142
[research_smith_1968]: https://doi.org/10.21236/ad0667521
[research_smith_1978]: https://doi.org/10.21236/ada059716
[research_smith_1991]: https://doi.org/10.1177/002029409102400303
[research_smith_1993]: https://doi.org/10.1017/s002211209322359x
[research_smith_2025]: https://doi.org/10.33548/scientia1180
[research_smith_geddes_1979]: https://doi.org/10.21236/ada077858
[research_smith_hammer_1971]: https://doi.org/10.21236/ad0730571
[research_smith_komerath_2001]: https://doi.org/10.21236/ada454384
[research_smith_lebacqz_1973]: https://doi.org/10.21236/ad0754840
[research_smith_meyer_1987]: https://doi.org/10.2514/3.20213
[research_smithjw_1979]: https://ntrs.nasa.gov/citations/19790023049
[research_smithjw_berrydt_1975]: https://ntrs.nasa.gov/citations/19750008488
[research_smithrogerse_schroederkurtc_1986]: https://ntrs.nasa.gov/citations/19870060567
[research_snyder_1950]: https://doi.org/10.21236/ad0109766
[research_snyder_schipper_1992]: https://doi.org/10.1109/62.257086
[research_snyder_zhao_2019]: https://doi.org/10.1016/j.ifacol.2019.12.047
[research_snyder_zhao_2022]: https://doi.org/10.2514/1.g006305
[research_sobester_2021]: https://doi.org/10.2514/1.c036180
[research_sobieczky_1984]: https://doi.org/10.1146/annurev.fluid.16.1.337
[research_sodja_werter_2021]: https://doi.org/10.2514/1.c035955
[research_sofi_2015]: https://doi.org/10.1016/j.probengmech.2015.09.001
[research_sofiatiefi_2020]: https://doi.org/10.5373/jardcs/v12i3/20201932
[research_softwareproductivityconsortiumherndonva_1994]: https://doi.org/10.21236/ada291137
[research_sohst_lobodovale_2022]: https://doi.org/10.1016/j.ast.2022.107531
[research_soleymani_arani_2019]: https://doi.org/10.1016/j.compstruct.2019.111532
[research_solies_1994]: https://doi.org/10.2514/3.46602
[research_solies_1994_b]: https://doi.org/10.2514/3.46495
[research_solis_leweke_2026]: https://doi.org/10.1017/jfm.2026.11657
[research_soltani_turner_2025]: https://doi.org/10.1109/lcsys.2025.3577574
[research_somani_2021]: https://doi.org/10.47059/revistageintec.v11i3.2006
[research_somashekar_prathap_1987]: https://doi.org/10.1016/0045-7949(87)90127-1
[research_son_sa_2015]: https://doi.org/10.6112/kscfe.2015.20.2.073
[research_son_sa_2015_b]: https://doi.org/10.1007/s12206-015-0720-y
[research_soneda_tsushima_2022]: https://doi.org/10.1007/s42405-022-00474-3
[research_song_huang_2022]: https://doi.org/10.1007/s11071-022-07742-7
[research_song_jia_2023]: https://doi.org/10.1109/tpel.2022.3199229
[research_song_lu_2026]: https://doi.org/10.3390/buildings16030646
[research_song_mignolet_2018]: https://doi.org/10.1016/j.probengmech.2017.12.002
[research_song_zhang_2016]: https://doi.org/10.1016/j.compstruct.2016.01.005
[research_soovere_1982]: https://doi.org/10.2514/3.44755
[research_soria_2006]: https://doi.org/10.21236/ada466362
[research_sottorfw_1949]: https://ntrs.nasa.gov/citations/20050242069
[research_soundararajan_btn_2022]: https://doi.org/10.1108/aeat-12-2021-0387
[research_soundararajan_sridhar_2024]: https://doi.org/10.1017/aer.2024.121
[research_southwell_1698]: https://doi.org/10.1098/rstl.1698.0075
[research_southwell_1698_b]: https://doi.org/10.1098/rstl.1698.0007
[research_southwell_1843]: https://doi.org/10.1017/s2042169900009160
[research_southwell_cathedral_1885]: https://doi.org/10.1038/scientificamerican06131885-7876supp
[research_southwell_gunn_1981]: https://doi.org/10.1680/iicep.1981.2140
[research_southwell_prashad_1923]: https://doi.org/10.26515/rzsi/v25/i2/1923/162704
[research_space_radiation_1987]: https://doi.org/10.1016/0010-4361(87)90478-2
[research_spagnol_riche_2019]: https://doi.org/10.1137/18m1167978
[research_spencer_walker_1975]: https://doi.org/10.1007/bf02318661
[research_spencer_watson_1992]: https://doi.org/10.1016/0022-5096(92)90041-y
[research_speyer_2003]: https://doi.org/10.21236/ada416352
[research_spiker_1964]: https://doi.org/10.21236/ad0437251
[research_spillman_ridgely_1995]: https://doi.org/10.21236/ada320244
[research_sreenivasan_1987]: https://doi.org/10.21236/ada185643
[research_srinathkumar_2015]: https://doi.org/10.4050/jahs.60.022010
[research_srivastava_2019]: https://doi.org/10.15394/ijaaa.2019.1370
[research_stagliano_mente_1979]: https://doi.org/10.21236/ada074261
[research_stainback_2001]: https://doi.org/10.21236/ada389727
[research_stalford_1979]: https://doi.org/10.21236/ada080025
[research_stanbrook_1954]: https://doi.org/10.1108/eb032455
[research_stanewsky_little_1971]: https://doi.org/10.2514/3.59192
[research_stanford_2016]: https://doi.org/10.2514/1.c033613
[research_stanford_2016_b]: https://doi.org/10.2514/1.g000413
[research_stanford_2017]: https://doi.org/10.2514/1.j056070
[research_stanford_2019]: https://doi.org/10.2514/1.g004373
[research_stanford_jutte_2016]: https://doi.org/10.2514/1.j054244
[research_stanford_jutte_2017]: https://doi.org/10.1016/j.compstruc.2017.01.010
[research_stanfordbretk_juttechristinev_2014]: https://ntrs.nasa.gov/citations/20150000538
[research_stanfordbretk_wiesemancarold_2015]: https://ntrs.nasa.gov/citations/20150006025
[research_stange_1959]: https://doi.org/10.21236/ada955359
[research_stanton_crain_1980]: https://doi.org/10.21236/ada088317
[research_stapelfeldt_vahdati_2019]: https://doi.org/10.1115/1.4042645
[research_stark_1989]: https://doi.org/10.2514/3.45867
[research_staroswiecki_amani_2015]: https://doi.org/10.1016/j.ifacol.2015.09.705
[research_staufferwa_jamesam_1978]: https://ntrs.nasa.gov/citations/19780019119
[research_stefanello_grundling_2016]: https://doi.org/10.1002/acs.2681
[research_stefanovski_2022]: https://doi.org/10.1002/rnc.6115
[research_steffensen_steinert_2023]: https://doi.org/10.2514/1.g007079
[research_steger_bailey_1980]: https://doi.org/10.2514/3.50756
[research_stegmuller_haybock_2026]: https://doi.org/10.2514/1.c038577
[research_steinberg_page_1998]: https://doi.org/10.21236/ada350986
[research_steinmetzgg_parrishrv_1972]: https://ntrs.nasa.gov/citations/19720010363
[research_stephan_stumpf_2023]: https://doi.org/10.2514/1.c036717
[research_sternberg_traven_1994]: https://doi.org/10.21236/ada284128
[research_stewart_dominick_1975]: https://doi.org/10.21236/ada018420
[research_stinton_1985]: https://doi.org/10.1017/s0001924000096779
[research_stirling_1983]: https://doi.org/10.1177/003754978304000504
[research_stodieck_cooper_2015]: https://doi.org/10.2514/1.j053599
[research_stodieck_cooper_2017]: https://doi.org/10.2514/1.j055364
[research_stodieck_cooper_2018]: https://doi.org/10.2514/1.j056952
[research_stolarik_2007]: https://doi.org/10.21236/ada470308
[research_stollery_1992]: https://doi.org/10.1016/0021-9169(92)90172-h
[research_stollf_koenigdg_1983]: https://ntrs.nasa.gov/citations/19830067155
[research_stottier_1995]: https://doi.org/10.21236/ada293962
[research_strand_levinsky_1969]: https://doi.org/10.21236/ad0698355
[research_streb_1973]: https://doi.org/10.2514/3.60203
[research_streit_wedler_2015]: https://doi.org/10.1017/s0001924000011283
[research_strike_wt_1982]: https://doi.org/10.21236/ada116279
[research_striz_1991]: https://doi.org/10.21236/ada248487
[research_stroud_hartl_2023]: https://doi.org/10.1088/1361-665x/acd0e6
[research_structural_aspects_2000]: https://ntrs.nasa.gov/citations/20000053157
[research_structural_fundamentals_1955]: https://doi.org/10.1108/eb032631
[research_study_of_1978]: https://ntrs.nasa.gov/citations/19780012169
[research_sturlaugson_sheppard_2015]: https://doi.org/10.1137/140953848
[research_su_kong_2026]: https://doi.org/10.1177/14759217261426251
[research_su_ma_2019]: https://doi.org/10.1007/s11630-019-1141-5
[research_su_mo_2025]: https://doi.org/10.36922/esam025110006
[research_su_swei_2016]: https://doi.org/10.2514/1.c033490
[research_subramanian_abdelsalam_2022]: https://doi.org/10.1109/lcsys.2021.3089502
[research_sudhi_radespiel_2023]: https://doi.org/10.2514/1.c036968
[research_sugimoto_1992]: https://doi.org/10.2514/3.46234
[research_sugimoto_saito_1968]: https://doi.org/10.1299/jsme1958.11.34
[research_sugimoto_saito_1969]: https://doi.org/10.1299/jsme1958.12.1342
[research_sugino_harada_2019]: https://doi.org/10.1299/jsmemovic.2019.16.c112
[research_sugumaran_2024]: https://doi.org/10.17148/iarjset.2024.11553
[research_suhpeterm_conyershowardj_2014]: https://ntrs.nasa.gov/citations/20150000848
[research_suhpeterm_conyershowardjason_2015]: https://ntrs.nasa.gov/citations/20150020901
[research_suikatreiner_donaldsonkent_1987]: https://ntrs.nasa.gov/citations/19880027050
[research_sulaeman_abdullah_2017]: https://doi.org/10.1088/1757-899x/184/1/012010
[research_sullivan_2002]: https://doi.org/10.21236/ada428867
[research_sultan_2026]: https://doi.org/10.65664/jeie.v2i02.20
[research_sultan_kattab_1995]: https://doi.org/10.1016/0306-4549(94)00084-r
[research_sumnu_2026]: https://doi.org/10.3390/app16042078
[research_sun_2015]: https://doi.org/10.1260/1756-8250.7.1-2.67
[research_sun_2024]: https://doi.org/10.1088/1742-6596/2882/1/012087
[research_sun_bahri_2025]: https://doi.org/10.1016/j.ast.2025.110017
[research_sun_chen_2026]: https://doi.org/10.1007/s00158-026-04375-x
[research_sun_devisser_2019]: https://doi.org/10.2514/1.c035135
[research_sun_feng_2023]: https://doi.org/10.3390/e25040674
[research_sun_gu_1995]: https://doi.org/10.1016/0167-6105(94)00051-e
[research_sun_han_2022]: https://doi.org/10.3934/mbe.2022262
[research_sun_lin_2025]: https://doi.org/10.1016/j.oceaneng.2025.122971
[research_sun_luo_2025]: https://doi.org/10.1063/5.0258283
[research_sun_miao_2020]: https://doi.org/10.1063/5.0018763
[research_sun_shi_2020]: https://doi.org/10.1016/j.ast.2020.106126
[research_sun_vankampen_2021]: https://doi.org/10.2514/1.g005715
[research_sun_wang_2020]: https://doi.org/10.3390/act9040122
[research_sun_wang_2024]: https://doi.org/10.3390/aerospace11110916
[research_sun_xu_2024]: https://doi.org/10.1016/j.conengprac.2024.105967
[research_sun_yoon_1988]: https://doi.org/10.21236/ada199311
[research_sun_zhang_2026]: https://doi.org/10.1016/j.ast.2025.110841
[research_supercritical_wing_1971]: https://doi.org/10.2307/3955948
[research_suraj_anilkumar_2023]: https://doi.org/10.1016/j.compstruct.2023.117072
[research_surwase_kumar_2025]: https://doi.org/10.1186/s44147-025-00749-y
[research_suryawanshi_ghosh_2015]: https://doi.org/10.1007/s00158-015-1322-0
[research_suryendu_ghosh_2017]: https://doi.org/10.1002/asjc.1465
[research_sushchenko_bezkorovainyi_2023]: https://doi.org/10.18372/1990-5548.77.18006
[research_sutherland_2018]: https://doi.org/10.1016/j.compstruct.2018.01.042
[research_svoboda_hengstermovric_2023]: https://doi.org/10.1016/j.ast.2023.108415
[research_swab_patel_2022]: https://doi.org/10.21236/ad1161194
[research_swaim_1961]: https://doi.org/10.2514/8.9241
[research_swaim_1970]: https://doi.org/10.2514/3.44151
[research_swaim_yen_1979]: https://doi.org/10.2514/3.58579
[research_swain_adhikari_2019]: https://doi.org/10.1016/j.compstruct.2019.110916
[research_sweat_1958]: https://doi.org/10.21236/ad0215012
[research_switzky_1965]: https://doi.org/10.2514/3.43690
[research_switzky_1965_b]: https://doi.org/10.2514/3.43644
[research_syed_moshtaghzadeh_2022]: https://doi.org/10.2514/1.j061574
[research_synaszko_salacinski_2015]: https://doi.org/10.1515/fas-2015-0004
[research_szalaikj_1975]: https://ntrs.nasa.gov/citations/19750010179
[research_szalaikj_1976]: https://ntrs.nasa.gov/citations/19760024056
[research_szalaikj_fellemanpg_1976]: https://ntrs.nasa.gov/citations/19760058525
[research_szalaikj_jarviscr_1978]: https://ntrs.nasa.gov/citations/19790005938
[research_szklarski_glebocki_2025]: https://doi.org/10.24425/ame.2025.155873
[research_szmulewitz_2011]: https://doi.org/10.21236/ada554126
[research_szmulewitz_2012]: https://doi.org/10.21236/ada568979
[research_szollosi_baranyi_2016]: https://doi.org/10.1002/asjc.1418
[research_szymanski_alstrom_2025]: https://doi.org/10.2514/1.c037978
[research_tabassum_bai_2022]: https://doi.org/10.1016/j.ast.2021.107323
[research_tahani_masdari_2017]: https://doi.org/10.1108/aeat-01-2016-0019
[research_taherinezhad_ramirezserrano_2023]: https://doi.org/10.3390/aerospace10100843
[research_tahir_maqsood_2026]: https://doi.org/10.2514/1.c038034
[research_tahraoui_1994]: https://doi.org/10.1017/s0308210500022447
[research_tai_wang_2023]: https://doi.org/10.1061/jaeeez.aseng-4565
[research_tai_wang_2023_b]: https://doi.org/10.2514/1.j062188
[research_taimoor_aijun_2019]: https://doi.org/10.1108/aeat-05-2019-0106
[research_taira_2014]: https://doi.org/10.21236/ada604901
[research_takahashi_yokozeki_2016]: https://doi.org/10.1177/1045389x16642298
[research_takarics_vanek_2019]: https://doi.org/10.1016/j.ifacol.2019.11.149
[research_talbot_geraldl_1992]: https://doi.org/10.21236/ada440831
[research_talreja_phan_2019]: https://doi.org/10.1016/j.compstruct.2019.03.052
[research_tamaskani_alfi_2026]: https://doi.org/10.1016/j.ast.2026.111656
[research_tamboli_1956]: https://doi.org/10.1017/s0001925900010313
[research_tameh_sawan_2018]: https://doi.org/10.1109/tie.2017.2786202
[research_tan_1988]: https://doi.org/10.1177/002199838802201105
[research_tan_wang_2021]: https://doi.org/10.1103/physrevfluids.6.l102701
[research_tan_zhang_2022]: https://doi.org/10.1007/s42401-021-00125-7
[research_tang_1972]: https://doi.org/10.2514/3.30382
[research_tang_1989]: https://doi.org/10.21236/ada216966
[research_tang_1994]: https://doi.org/10.1137/s0895479892226603
[research_tang_2025]: https://doi.org/10.1080/23307706.2025.2474671
[research_tang_chen_2017]: https://doi.org/10.1016/j.apm.2017.04.012
[research_tang_chen_2018]: https://doi.org/10.1177/1077546317750504
[research_tang_chen_2020]: https://doi.org/10.1177/1077546320929153
[research_tang_gan_2025]: https://doi.org/10.3390/aerospace12060468
[research_tang_liu_2018]: https://doi.org/10.1016/j.compstruct.2018.07.111
[research_tang_luo_2017]: https://doi.org/10.1016/j.ast.2017.05.005
[research_tang_luo_2018]: https://doi.org/10.1016/j.ast.2017.11.015
[research_tang_tang_2025]: https://doi.org/10.23919/jsee.2025.000136
[research_tang_wang_2020]: https://doi.org/10.1016/j.cja.2020.05.027
[research_tang_wu_2015]: https://doi.org/10.1016/j.cja.2014.12.024
[research_tang_wu_2016]: https://doi.org/10.1016/j.cja.2015.12.001
[research_tang_wu_2017]: https://doi.org/10.1016/j.cja.2016.12.024
[research_tang_zhang_2022]: https://doi.org/10.1016/j.ast.2022.107345
[research_tangler_1979]: https://doi.org/10.21236/ada074141
[research_tantaroudas_karachalios_2026]: https://doi.org/10.24132/acm.2026.1114
[research_tanveer_ahmad_2023]: https://doi.org/10.3390/aerospace10060563
[research_tanyer_tatlicioglu_2016]: https://doi.org/10.1080/00207721.2016.1261200
[research_tao_2025]: https://doi.org/10.1016/j.automatica.2025.112174
[research_tao_li_2016]: https://doi.org/10.1016/j.ins.2015.08.033
[research_tao_sun_2016]: https://doi.org/10.1016/j.cja.2016.08.008
[research_targoff_1947]: https://doi.org/10.2514/8.1458
[research_targoff_1947_b]: https://doi.org/10.2514/8.1420
[research_tarnowski_2017]: https://doi.org/10.1108/aeat-11-2016-0208
[research_tate_1992]: https://doi.org/10.21236/ada256514
[research_taubert_kay_2023]: https://doi.org/10.1108/hff-11-2022-0653
[research_taufik_qasem_2025]: https://doi.org/10.1016/j.trpro.2025.03.120
[research_tayebwa_morshed_2026]: https://doi.org/10.1016/j.supflu.2025.106871
[research_taylor_1959]: https://doi.org/10.1017/s0001924000092502
[research_taylor_2009]: https://doi.org/10.21236/ada540446
[research_taylor_wilson_2015]: https://doi.org/10.21236/ada618198
[research_teel_1999]: https://doi.org/10.21236/ada367012
[research_teel_1999_b]: https://doi.org/10.21236/ada367415
[research_teimourian_altmeyer_2026]: https://doi.org/10.1108/aeat-08-2025-0305
[research_teixeira_araujo_2018]: https://doi.org/10.1109/tcns.2017.2732158
[research_teixeira_cesnik_2020]: https://doi.org/10.1017/aer.2019.165
[research_telionis_1995]: https://doi.org/10.21236/ada299820
[research_telionis_2001]: https://doi.org/10.21236/ada398139
[research_teper_stapleford_1966]: https://doi.org/10.2514/3.43725
[research_terekhov_2022]: https://doi.org/10.34759/vst-2022-1-211-225
[research_tewar_myers_2015]: https://doi.org/10.1016/j.sysarc.2015.07.005
[research_thanusha_sarkar_2016]: https://doi.org/10.1016/j.proeng.2016.05.128
[research_tharp_zhang_1994]: https://doi.org/10.1007/bf02115737
[research_the_catholic_1995]: https://doi.org/10.1353/pgn.1995.0071
[research_the_impact_2024]: https://doi.org/10.31355/147
[research_the_viscoelastic_1981]: https://doi.org/10.1016/0010-4361(81)90470-5
[research_the_voisin_1911]: https://doi.org/10.1038/scientificamerican04291911-424
[research_theerthamalai_mukesh_2025]: https://doi.org/10.1063/5.0256726
[research_theerthamalai_ramanan_2026]: https://doi.org/10.2514/1.a36413
[research_theis_pfifer_2020]: https://doi.org/10.2514/1.g004846
[research_theisen_scruggs_1973]: https://doi.org/10.21236/ad0771304
[research_theodore_malpica_2020]: https://doi.org/10.4050/jahs.65.042007
[research_theodorsen_1959]: https://doi.org/10.2514/8.8239
[research_thermal_damage_1989]: https://doi.org/10.1016/0010-4361(89)90359-5
[research_thermal_expansion_1981]: https://doi.org/10.1016/0010-4361(81)90491-2
[research_thien_kim_2018]: https://doi.org/10.1016/j.ifacol.2018.12.003
[research_thomas_dowell_2025]: https://doi.org/10.2514/1.c038249
[research_thomas_hallett_2020]: https://doi.org/10.1016/j.compstruct.2020.112170
[research_thomas_paulson_1978]: https://doi.org/10.2514/3.58357
[research_thompson_1992]: https://doi.org/10.21236/ada251673
[research_thompson_bannon_2002]: https://doi.org/10.21236/ada408751
[research_thompson_walls_2005]: https://doi.org/10.21236/ada436999
[research_thu_gavrilov_2017]: https://doi.org/10.1016/j.procs.2017.01.046
[research_tian_2016]: https://doi.org/10.14257/ijca.2016.9.1.21
[research_tian_2020]: https://doi.org/10.1080/03772063.2020.1768907
[research_tian_2021]: https://doi.org/10.1515/auto-2020-0020
[research_tian_gao_2017]: https://doi.org/10.1016/j.cja.2017.07.011
[research_tian_jin_2023]: https://doi.org/10.1016/j.actaastro.2023.08.008
[research_tian_li_2015]: https://doi.org/10.3390/a8010003
[research_tian_li_2019]: https://doi.org/10.1016/j.jsv.2019.114942
[research_tian_li_2026]: https://doi.org/10.1016/j.jsv.2026.119977
[research_tian_sun_2025]: https://doi.org/10.1016/j.compstruct.2025.119355
[research_tian_tang_2025]: https://doi.org/10.61416/ceai.v27i1.9287
[research_tian_wang_2026]: https://doi.org/10.1016/j.compstruct.2026.120104
[research_tian_yang_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000652
[research_tian_zhao_2025]: https://doi.org/10.1063/5.0279195
[research_tijdeman_vannunen_1979]: https://doi.org/10.21236/ada071420
[research_tijdeman_vannunen_1979_b]: https://doi.org/10.21236/ada077370
[research_ting_berg_2026]: https://doi.org/10.2514/1.g009557
[research_ting_chaparro_2018]: https://doi.org/10.2514/1.c034810
[research_ting_mesbahi_2023]: https://doi.org/10.2514/1.g007450
[research_tingeric_daotung_2015]: https://ntrs.nasa.gov/citations/20190025220
[research_tingeric_lebofskysonia_2014]: https://ntrs.nasa.gov/citations/20150000694
[research_tingeric_nguyennhan_2014]: https://ntrs.nasa.gov/citations/20140008648
[research_tingting_aijun_2018]: https://doi.org/10.1108/aeat-05-2017-0134
[research_tipan_theodoulis_2020]: https://doi.org/10.2514/1.g004976
[research_tischlermarkb_fletcherjayw_1991]: https://ntrs.nasa.gov/citations/19910067397
[research_to_ewins_1995]: https://doi.org/10.1006/jsvi.1995.0442
[research_toader_1987]: https://doi.org/10.1016/0263-8231(87)90019-x
[research_toan_2026]: https://doi.org/10.63680/ijsate0226014.010
[research_toffol_2024]: https://doi.org/10.3390/app14219883
[research_toffol_ricci_2023]: https://doi.org/10.3390/aerospace10080693
[research_tohidi_khakisedigh_2016]: https://doi.org/10.1002/rnc.3518
[research_tokunaga_masui_2015]: https://doi.org/10.1016/j.proeng.2014.12.638
[research_toledano_murakami_1987]: https://doi.org/10.1115/1.3172955
[research_toloei_ghaderi_2026]: https://doi.org/10.1007/s42401-026-00472-3
[research_tomas_zaini_2026]: https://doi.org/10.14416/j.asep.2026.08.002
[research_tomlinson_1973]: https://doi.org/10.2514/3.60266
[research_tona_1962]: https://doi.org/10.21236/ad0299123
[research_tong_du_2025]: https://doi.org/10.1002/rnc.70057
[research_toribio_2018]: https://doi.org/10.1016/j.prostr.2018.06.015
[research_tormalm_leroy_2018]: https://doi.org/10.2514/1.c033820
[research_torregrosa_gil_2022]: https://doi.org/10.1016/j.compstruct.2022.115845
[research_torsional_stiffness_1972]: https://doi.org/10.1016/0010-4361(72)90404-1
[research_torsional_stiffness_1994]: https://doi.org/10.1016/0026-2714(94)90317-4
[research_townsend_picelli_2018]: https://doi.org/10.2514/1.j056748
[research_trabocco_1980]: https://doi.org/10.21236/ada326379
[research_tracking_control_1993]: https://doi.org/10.1016/0967-0661(93)92253-z
[research_tran_1994]: https://doi.org/10.1080/00423119408969056
[research_tran_nguyen_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001393
[research_tran_sakamoto_2017]: https://doi.org/10.1016/j.ast.2017.05.010
[research_transfer_of_1960]: https://doi.org/10.14359/8022
[research_traub_2019]: https://doi.org/10.2514/1.c035600
[research_traven_whitley_1995]: https://doi.org/10.21236/ada300965
[research_tribuno_klein_1976]: https://doi.org/10.21236/ada029021
[research_trindadenascimento_cunha_2019]: https://doi.org/10.1049/iet-cta.2018.5293
[research_triplett_1972]: https://doi.org/10.2514/3.59009
[research_triplett_1980]: https://doi.org/10.2514/3.57932
[research_triplett_burkhart_1971]: https://doi.org/10.2514/3.59109
[research_triplett_kappus_1973]: https://doi.org/10.2514/3.60281
[research_trippenseegarya_luxdavidp_1987]: https://ntrs.nasa.gov/citations/19880008260
[research_trippenseegarya_luxdavidp_1988]: https://ntrs.nasa.gov/citations/19890023269
[research_tritschler_oconnor_2016]: https://doi.org/10.2514/1.g000401
[research_truong_rakotomamonjy_2016]: https://doi.org/10.1016/j.ifacol.2016.09.021
[research_tsai_malak_2024]: https://doi.org/10.1007/s00158-024-03859-y
[research_tsatsas_pontillo_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001390
[research_tsiakas_trompoukis_2024]: https://doi.org/10.3390/fluids9040087
[research_tsoutsinos_1994]: https://doi.org/10.1016/0167-6911(94)90067-1
[research_tsubakino_saito_2020]: https://doi.org/10.1299/jsmetokai.2020.69.412
[research_tsunematsu_donadon_2019]: https://doi.org/10.1016/j.compstruct.2018.11.065
[research_tsushima_arizono_2018]: https://doi.org/10.1299/jsmetld.2018.27.1005
[research_tsushima_arizono_2019]: https://doi.org/10.1299/transjsme.18-00506
[research_tsushima_saitoh_2021]: https://doi.org/10.3390/aerospace8080200
[research_tsushima_su_2017]: https://doi.org/10.1016/j.ast.2017.02.013
[research_tsushima_tamayama_2021]: https://doi.org/10.1016/j.ast.2021.106923
[research_tsushima_yokozeki_2019]: https://doi.org/10.1016/j.ast.2019.03.025
[research_tsypkin_fu_1993]: https://doi.org/10.1080/00207179308934419
[research_tu_1992]: https://doi.org/10.2514/3.46253
[research_tu_1994]: https://doi.org/10.2514/3.46466
[research_tu_1994_b]: https://doi.org/10.2514/3.46489
[research_tu_lu_2026]: https://doi.org/10.1007/s11071-026-12399-7
[research_tudosie_dumitru_2019]: https://doi.org/10.19062/2247-3173.2019.21.27
[research_tueugenel_1991]: https://ntrs.nasa.gov/citations/19910036733
[research_tueugenel_1992]: https://ntrs.nasa.gov/citations/19920062855
[research_tueugenel_1992_b]: https://ntrs.nasa.gov/citations/19930029307
[research_tueugenel_vandalsemwilliamr_1996]: https://ntrs.nasa.gov/citations/20020041911
[research_tungikar_rao_1994]: https://doi.org/10.1016/0263-8223(94)90268-2
[research_turner_1982]: https://doi.org/10.2514/3.44757
[research_turner_1982_b]: https://doi.org/10.2514/3.57431
[research_turnermj_hoyjm_1976]: https://ntrs.nasa.gov/citations/19770011082
[research_twisdale_kirsten_1984]: https://doi.org/10.2514/3.19871
[research_uav_control_2023]: https://doi.org/10.36652/0869-4931-2023-77-4-155-161
[research_ulry_gehring_1976]: https://doi.org/10.21236/ada041208
[research_unal_2021]: https://doi.org/10.1108/aeat-12-2020-0293
[research_unal_2021_b]: https://doi.org/10.1108/aeat-12-2020-0302
[research_underwoodpamelaj_owenslewisr_2003]: https://ntrs.nasa.gov/citations/20030007882
[research_unruh_1988]: https://doi.org/10.2514/3.45655
[research_urrehman_ekici_2025]: https://doi.org/10.1063/5.0259296
[research_urso_giunta_2026]: https://doi.org/10.1016/j.compstruct.2025.119762
[research_ursu_ionguta_2018]: https://doi.org/10.1088/1742-6596/1106/1/012033
[research_usellerjamesw_russeyroberte_1955]: https://ntrs.nasa.gov/citations/20090026462
[research_uzun_2024]: https://doi.org/10.1108/aeat-11-2023-0287
[research_uzun_2024_b]: https://doi.org/10.1016/j.aets.2024.12.001
[research_uzun_bilgic_2023]: https://doi.org/10.1017/aer.2023.73
[research_uzun_oktay_2023]: https://doi.org/10.1108/aeat-09-2022-0259
[research_valsangkar_britto_1982]: https://doi.org/10.1680/iicep.1982.1992
[research_vanbaelen_ellerbroek_2020]: https://doi.org/10.2514/1.g004596
[research_vance_brown_1974]: https://doi.org/10.21236/ad0783390
[research_vandam_holmes_1981]: https://doi.org/10.2514/3.57531
[research_vandenberg_elsenaar_1975]: https://doi.org/10.1017/s0022112075001930
[research_vandenbrandt_devisser_2018]: https://doi.org/10.1016/j.ifacol.2018.09.641
[research_vandenkieboom_elham_2017]: https://doi.org/10.1007/s00158-017-1787-0
[research_vandommelen_1995]: https://doi.org/10.21236/ada329654
[research_vandooren_bisagni_2024]: https://doi.org/10.1016/j.compstruct.2024.118295
[research_vandoren_1955]: https://doi.org/10.1109/irettrc.1955.6538793
[research_vangaasbeek_1980]: https://doi.org/10.21236/ada089008
[research_vangraas_braasch_1991]: https://doi.org/10.1002/j.2161-4296.1991.tb01864.x
[research_vangraas_diggle_1994]: https://doi.org/10.1002/j.2161-4296.1994.tb02322.x
[research_vanleeuwen_1960]: https://doi.org/10.1108/eb033314
[research_vansteenwykbrett_lyuyloi_1992]: https://ntrs.nasa.gov/citations/19920072606
[research_vantuyl_1988]: https://doi.org/10.2514/3.9883
[research_vanwaarde_2022]: https://doi.org/10.1109/lcsys.2021.3073860
[research_varun_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1061
[research_varun_mondal_2022]: https://doi.org/10.1016/j.compstruct.2022.115662
[research_vaughan_1948]: https://doi.org/10.21236/adb812170
[research_vedeneev_2020]: https://doi.org/10.2514/1.j058959
[research_vehicle_sensor_2026]: https://doi.org/10.59038/jjmie/200204
[research_veley_khot_2008]: https://doi.org/10.21236/ada478915
[research_velkova_2017]: https://doi.org/10.19062/1842-9238.2017.15.3.1
[research_venkataraman_seiler_2019]: https://doi.org/10.2514/1.g003824
[research_vepa_kwon_2021]: https://doi.org/10.1017/aer.2021.38
[research_verhaegen_zbikowski_2017]: https://doi.org/10.1016/j.ast.2017.03.001
[research_verma_1981]: https://doi.org/10.1080/00423118108968682
[research_verma_cidmontoya_2024]: https://doi.org/10.2139/ssrn.5039067
[research_verma_cidmontoya_2025]: https://doi.org/10.1016/j.jweia.2025.106133
[research_vermiglio_2017]: https://doi.org/10.1137/15m1029618
[research_verri_desilvabussamra_2025]: https://doi.org/10.2514/1.c037829
[research_vertonghen_irisarri_2026]: https://doi.org/10.1016/j.compstruct.2026.120658
[research_vescovini_dozio_2016]: https://doi.org/10.1016/j.compstruct.2016.01.068
[research_viglietti_zappino_2019]: https://doi.org/10.2514/1.c034795
[research_vile_alwi_2020]: https://doi.org/10.1049/cth2.12042
[research_vilela_donadon_2025]: https://doi.org/10.1016/j.tws.2025.113547
[research_villarroel_rodrigues_2016]: https://doi.org/10.2514/1.g001373
[research_vinje_miller_1973]: https://doi.org/10.21236/ad0769868
[research_viola_oziablo_2020]: https://doi.org/10.1016/j.ifacol.2020.12.1617
[research_viswanath_mukund_1995]: https://doi.org/10.2514/3.12838
[research_viswanathan_charkey_1986]: https://doi.org/10.21236/ada169411
[research_viswanathan_charkey_1988]: https://doi.org/10.21236/ada194979
[research_vitushkinvv_2025]: https://doi.org/10.36652/0869-4931-2025-79-11-509-513
[research_vlahostergios_komnos_2018]: https://doi.org/10.1504/pcfd.2018.096620
[research_vollo_brassaw_1956]: https://doi.org/10.21236/ad0102193
[research_volpe_salcuni_2026]: https://doi.org/10.1109/lcsys.2026.3704983
[research_voracek_clarke_1994]: https://doi.org/10.2514/3.46505
[research_voracekdavidf_clarkerobert_1991]: https://ntrs.nasa.gov/citations/19910047389
[research_vorum_1984]: https://doi.org/10.21236/adb240794
[research_voting_software_1993]: https://doi.org/10.1016/0967-0661(93)92298-i
[research_voulgaris_1994]: https://doi.org/10.1109/9.299632
[research_vrchota_prachar_2019]: https://doi.org/10.1108/aeat-01-2018-0053
[research_vukelich_stoy_1988]: https://doi.org/10.21236/ada210128
[research_vukelich_stoy_1988_b]: https://doi.org/10.21236/ada211086
[research_vukobratovic_stojic_1985]: https://doi.org/10.1016/s1474-6670(17)60398-7
[research_vuong_kim_2021]: https://doi.org/10.3390/en15010159
[research_wada_tamayama_2020]: https://doi.org/10.1088/2631-8695/abbb59
[research_wadia_niedermeier_2019]: https://doi.org/10.1115/1.4043574
[research_wagg_2022]: https://doi.org/10.25518/2684-6500.84
[research_waggonereg_batesbl_1989]: https://ntrs.nasa.gov/citations/19910014824
[research_waggonereg_jennettla_1986]: https://ntrs.nasa.gov/citations/19870045310
[research_wahler_ma_2025]: https://doi.org/10.3390/aerospace12020077
[research_waitman_marcos_2019]: https://doi.org/10.1016/j.ifacol.2019.11.184
[research_waitman_marcos_2020]: https://doi.org/10.2514/1.g004618
[research_wakimoto_chiba_2021]: https://doi.org/10.3390/aerospace8080217
[research_walchlilawrencea_1994]: https://ntrs.nasa.gov/citations/19950007845
[research_walker_claudio_2024]: https://doi.org/10.1007/s42979-024-02874-6
[research_walker_hall_1968]: https://doi.org/10.1017/s0001925900004741
[research_walker_kaufman_1977]: https://doi.org/10.21236/ada042114
[research_walkersa_1976]: https://ntrs.nasa.gov/citations/19760024070
[research_walkerth_minguetpj_1997]: https://ntrs.nasa.gov/citations/19970016009
[research_walshkevinr_1993]: https://ntrs.nasa.gov/citations/19930013934
[research_walshmichaelj_sellerswilliamliii_1988]: https://ntrs.nasa.gov/citations/19880053537
[research_wan_1974]: https://doi.org/10.21236/ada034828
[research_wang_2019]: https://doi.org/10.1063/1.5087963
[research_wang_2021]: https://doi.org/10.1080/0305215x.2021.2004136
[research_wang_2024]: https://doi.org/10.2316/j.2024.201-0461
[research_wang_2024_b]: https://doi.org/10.1088/1742-6596/2762/1/012050
[research_wang_2025]: https://doi.org/10.2316/j.2025.201-0461
[research_wang_2025_b]: https://doi.org/10.54254/2755-2721/2026.ka27405
[research_wang_2026]: https://doi.org/10.1590/jatm.v18.1450
[research_wang_bai_2024]: https://doi.org/10.1016/j.conengprac.2024.106079
[research_wang_baker_2019]: https://doi.org/10.1016/j.compstruct.2018.09.038
[research_wang_bhaduri_2025]: https://doi.org/10.1007/s00158-025-03979-z
[research_wang_chen_2021]: https://doi.org/10.1016/j.compstruct.2020.113422
[research_wang_chen_2022]: https://doi.org/10.2514/1.j060781
[research_wang_chen_2024]: https://doi.org/10.3390/aerospace11090711
[research_wang_chen_2025]: https://doi.org/10.1016/j.ast.2025.110547
[research_wang_chu_2017]: https://doi.org/10.1016/j.ifacol.2017.08.320
[research_wang_daronch_2018]: https://doi.org/10.3390/aerospace5030086
[research_wang_fei_2016]: https://doi.org/10.1109/access.2016.2591978
[research_wang_feng_2025]: https://doi.org/10.3390/aerospace12080659
[research_wang_gao_2016]: https://doi.org/10.1007/s00348-016-2184-y
[research_wang_guo_2015]: https://doi.org/10.1002/acs.2585
[research_wang_hou_2022]: https://doi.org/10.1109/access.2022.3213938
[research_wang_hu_2021]: https://doi.org/10.1177/14759217211056831
[research_wang_hu_2026]: https://doi.org/10.1016/j.ast.2025.111272
[research_wang_ji_2025]: https://doi.org/10.1016/j.ast.2025.110533
[research_wang_kampen_2019]: https://doi.org/10.2514/1.g003497
[research_wang_li_2015]: https://doi.org/10.1155/2015/280940
[research_wang_li_2025]: https://doi.org/10.1016/j.ast.2025.110134
[research_wang_li_2025_b]: https://doi.org/10.1049/icp.2024.2837
[research_wang_li_2025_c]: https://doi.org/10.1109/taes.2024.3448398
[research_wang_li_2026]: https://doi.org/10.3390/drones10080601
[research_wang_liang_2016]: https://doi.org/10.1002/oca.2237
[research_wang_liu_2020]: https://doi.org/10.36001/phmconf.2020.v12i1.1261
[research_wang_liu_2024]: https://doi.org/10.1002/asjc.3395
[research_wang_liu_2026]: https://doi.org/10.1177/01423312261465708
[research_wang_liuxu_2025]: https://doi.org/10.1016/j.ast.2024.109813
[research_wang_lu_2021]: https://doi.org/10.1016/j.ast.2021.106871
[research_wang_lu_2023]: https://doi.org/10.3390/aerospace10090799
[research_wang_luo_2025]: https://doi.org/10.1016/j.ast.2024.109773
[research_wang_luo_2025_b]: https://doi.org/10.1016/j.cja.2024.103327
[research_wang_luo_2025_c]: https://doi.org/10.1016/j.ast.2025.110369
[research_wang_ma_2021]: https://doi.org/10.2514/1.c035687
[research_wang_mallor_2025]: https://doi.org/10.1016/j.ijheatfluidflow.2025.109900
[research_wang_mao_2025]: https://doi.org/10.1016/j.tranpol.2024.11.011
[research_wang_mkhoyan_2021]: https://doi.org/10.2514/1.g005870
[research_wang_peeters_2021]: https://doi.org/10.1088/1757-899x/1024/1/012020
[research_wang_qing_2016]: https://doi.org/10.1115/1.4032630
[research_wang_qiu_2019]: https://doi.org/10.1177/1475921719850641
[research_wang_rao_2025]: https://doi.org/10.1080/27525783.2025.2493074
[research_wang_rogers_1991]: https://doi.org/10.1177/002199839102500405
[research_wang_song_2024]: https://doi.org/10.1155/2024/7481513
[research_wang_song_2025]: https://doi.org/10.1016/j.amf.2025.200202
[research_wang_su_2017]: https://doi.org/10.1088/1742-6596/916/1/012006
[research_wang_su_2018]: https://doi.org/10.1088/1757-899x/452/4/042048
[research_wang_sun_2019]: https://doi.org/10.1061/(asce)as.1943-5525.0001028
[research_wang_sun_2024]: https://doi.org/10.3390/aerospace11050366
[research_wang_sun_2024_b]: https://doi.org/10.1080/00423114.2024.2435973
[research_wang_sun_2025]: https://doi.org/10.2514/1.g009257
[research_wang_tai_2022]: https://doi.org/10.3390/aerospace9110689
[research_wang_thevendran_1993]: https://doi.org/10.1006/jsvi.1993.1153
[research_wang_tian_2025]: https://doi.org/10.1016/j.cma.2025.118323
[research_wang_vankampen_2019]: https://doi.org/10.2514/1.g003980
[research_wang_vankampen_2019_b]: https://doi.org/10.2514/1.g003791
[research_wang_wan_2021]: https://doi.org/10.1016/j.compstruct.2020.113201
[research_wang_wang_1994]: https://doi.org/10.1061/(asce)0733-9445(1994)120:1(200)
[research_wang_wang_2015]: https://doi.org/10.4028/www.scientific.net/amm.740.293
[research_wang_wang_2023]: https://doi.org/10.1177/14759217231166119
[research_wang_wang_2025]: https://doi.org/10.1016/j.compstruct.2025.119590
[research_wang_wang_2025_b]: https://doi.org/10.3390/aerospace12121076
[research_wang_wei_2026]: https://doi.org/10.1109/taes.2026.3663140
[research_wang_wen_2021]: https://doi.org/10.1177/0142331221989007
[research_wang_weng_2026]: https://doi.org/10.1016/j.engappai.2026.115261
[research_wang_wu_2015]: https://doi.org/10.1007/s11071-015-2083-4
[research_wang_wu_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103286
[research_wang_wu_2026]: https://doi.org/10.1016/j.ast.2026.113395
[research_wang_wynn_2018]: https://doi.org/10.2514/1.c034684
[research_wang_xia_2022]: https://doi.org/10.1016/j.addma.2022.102717
[research_wang_xu_2016]: https://doi.org/10.1016/j.cja.2016.10.010
[research_wang_xu_2018]: https://doi.org/10.3390/s18103447
[research_wang_xu_2021]: https://doi.org/10.1016/j.ifacol.2021.10.218
[research_wang_ye_2026]: https://doi.org/10.1016/j.jfluidstructs.2026.104643
[research_wang_yi_2026]: https://doi.org/10.1007/s11431-025-3198-1
[research_wang_zhang_2020]: https://doi.org/10.1016/j.cja.2020.03.016
[research_wang_zhang_2021]: https://doi.org/10.1016/j.addma.2021.102341
[research_wang_zhang_2022]: https://doi.org/10.3390/sym14061154
[research_wang_zhang_2022_b]: https://doi.org/10.3390/app12189268
[research_wang_zhang_2025]: https://doi.org/10.1108/aeat-07-2024-0195
[research_wang_zhang_2025_b]: https://doi.org/10.1063/5.0283461
[research_wang_zhang_2026]: https://doi.org/10.1177/10775463251410847
[research_wang_zhao_2022]: https://doi.org/10.2514/1.j060909
[research_wang_zhao_2022_b]: https://doi.org/10.3390/aerospace9080433
[research_wang_zheng_2022]: https://doi.org/10.1088/1742-6596/2187/1/012046
[research_wang_zheng_2025]: https://doi.org/10.1080/27525783.2025.2509708
[research_wang_zhou_2024]: https://doi.org/10.1016/j.apm.2024.01.044
[research_wang_zhou_2026]: https://doi.org/10.2514/1.c038983
[research_wang_zhu_2016]: https://doi.org/10.1016/j.jfluidstructs.2016.01.009
[research_wang_zhu_2020]: https://doi.org/10.1007/s11432-018-9795-y
[research_wangjohnt_1996]: https://ntrs.nasa.gov/citations/19960020473
[research_wangjohnt_jegleydawnc_1996]: https://ntrs.nasa.gov/citations/19960048076
[research_wansaseub_sleesongsom_2020]: https://doi.org/10.1007/s42405-019-00246-6
[research_wansasueb_panagant_2023]: https://doi.org/10.1007/s00707-023-03756-3
[research_wardlaw_andrewb_1975]: https://doi.org/10.21236/ada020356
[research_warren_1998]: https://doi.org/10.21236/ada359829
[research_washington_pettis_1968]: https://doi.org/10.21236/ad0695658
[research_wasson_mehus_1967]: https://doi.org/10.2514/3.43843
[research_watsonclifford_2010]: https://ntrs.nasa.gov/citations/20100024129
[research_watsoncliffordc_2011]: https://ntrs.nasa.gov/citations/20110015694
[research_wauters_2021]: https://doi.org/10.1115/1.4052009
[research_wauters_2022]: https://doi.org/10.1177/17568293221092139
[research_weatherill_zartarian_1958]: https://doi.org/10.21236/ad0142154
[research_webb_rogers_2021]: https://doi.org/10.2514/1.c036206
[research_webblannied_mccainwilliame_1988]: https://ntrs.nasa.gov/citations/19890006537
[research_weed_carlson_1983]: https://doi.org/10.21236/ada129573
[research_wegener_dhooghe_1993]: https://doi.org/10.1063/1.168480
[research_wei_2019]: https://doi.org/10.3390/inventions4030049
[research_wei_2022]: https://doi.org/10.1155/2022/7716900
[research_wei_chen_2017]: https://doi.org/10.2514/1.c034079
[research_wei_cui_2025]: https://doi.org/10.3390/aerospace12090773
[research_wei_du_2019]: https://doi.org/10.1115/1.4045599
[research_wei_freris_2024]: https://doi.org/10.1007/s00371-024-03402-6
[research_wei_ke_2024]: https://doi.org/10.3390/act13010043
[research_wei_meng_2024]: https://doi.org/10.1002/rnc.7526
[research_wei_xu_2020]: https://doi.org/10.1109/access.2020.2964728
[research_wei_zhan_2019]: https://doi.org/10.1108/aeat-08-2017-0181
[research_weidemann_leondes_1979]: https://doi.org/10.21236/ada072259
[research_weihs_katz_1986]: https://doi.org/10.2514/3.9418
[research_weinert_meyer_1984]: https://doi.org/10.21236/ada141875
[research_weiser_ossmann_2020]: https://doi.org/10.1007/s13272-020-00461-y
[research_weissel_1997]: https://doi.org/10.21236/ada627994
[research_weissenberger_1969]: https://doi.org/10.1080/00207176908905741
[research_weisshaar_1977]: https://doi.org/10.2514/3.44579
[research_weisshaar_1978]: https://doi.org/10.21236/adb032318
[research_weisshaar_1979]: https://doi.org/10.21236/adb042815
[research_weisshaar_1980]: https://doi.org/10.2514/3.57922
[research_weisshaar_1981]: https://doi.org/10.2514/3.57542
[research_weisshaar_1985]: https://doi.org/10.2514/3.48607
[research_weisshaar_ryan_1986]: https://doi.org/10.2514/3.45282
[research_weisshaar_zeiler_1983]: https://doi.org/10.2514/3.48205
[research_weisshaarta_1983]: https://ntrs.nasa.gov/citations/19840055636
[research_weisshaarta_ehlerssm_1990]: https://ntrs.nasa.gov/citations/19900042331
[research_weisshaarta_zeilerta_1982]: https://ntrs.nasa.gov/citations/19820055567
[research_weisshaarterrencea_ehlersstevenm_1992]: https://ntrs.nasa.gov/citations/19930030821
[research_well_berger_1982]: https://doi.org/10.1007/bf00934324
[research_welle_2000]: https://doi.org/10.21236/ada381453
[research_wells_2002]: https://doi.org/10.21236/ada398917
[research_wen_song_2023]: https://doi.org/10.3390/aerospace10121001
[research_werdes_1953]: https://doi.org/10.2514/8.2666
[research_werter_debreuker_2016]: https://doi.org/10.1016/j.compstruct.2016.09.044
[research_westbrook_1975]: https://doi.org/10.21236/ada004476
[research_westin_balthazar_2023]: https://doi.org/10.3390/axioms12090826
[research_westphal_balfe_1961]: https://doi.org/10.21236/ad0263413
[research_wheatcroft_groh_2025]: https://doi.org/10.1017/aer.2025.10113
[research_wheatcroft_mahadik_2025]: https://doi.org/10.2514/1.j065343
[research_whitbeck_hofmann_1978]: https://doi.org/10.21236/ada067177
[research_whitbeck_smith_1982]: https://doi.org/10.21236/ada134175
[research_white_2004]: https://doi.org/10.21236/ada421045
[research_white_geubelle_2005]: https://doi.org/10.21236/ada443864
[research_white_hartl_2025]: https://doi.org/10.1016/j.cma.2025.117911
[research_white_mongru_2017]: https://doi.org/10.1177/1475921717738389
[research_white_padfield_2021]: https://doi.org/10.1007/s13272-021-00542-6
[research_white_richardp_1961]: https://doi.org/10.21236/ad0328509
[research_whiteedwardv_kapaniarakeshk_2015]: https://ntrs.nasa.gov/citations/20150017734
[research_whiteheadrs_foremancr_1992]: https://ntrs.nasa.gov/citations/19950022016
[research_whitejfiii_bendiksenoo_1986]: https://ntrs.nasa.gov/citations/19860063533
[research_whitlowwoodrowjr_bennettrobertm_1991]: https://ntrs.nasa.gov/citations/19930063025
[research_whitworth_1987]: https://doi.org/10.1177/002199838702100405
[research_whoric_1973]: https://doi.org/10.21236/ad0914456
[research_whoric_1977]: https://doi.org/10.21236/ada038494
[research_wickens_dixon_2002]: https://doi.org/10.21236/ada496813
[research_wickman_1953]: https://doi.org/10.21236/ada953108
[research_wie_byun_1989]: https://doi.org/10.2514/3.20384
[research_wiese_blom_2015]: https://doi.org/10.1016/j.conengprac.2015.09.015
[research_wiggenraadjfm_bauldnrjr_1993]: https://ntrs.nasa.gov/citations/19930044546
[research_wilcox_1963]: https://doi.org/10.21236/ad0400570
[research_wildermuth_rothammer_1974]: https://doi.org/10.21236/ada002873
[research_wildermuth_rothammer_1974_b]: https://doi.org/10.21236/ada002854
[research_wilhelm_schafranek_1986]: https://doi.org/10.2514/3.45377
[research_williams_1952]: https://doi.org/10.2514/8.2400
[research_williams_1980]: https://doi.org/10.2514/3.50797
[research_williams_2002]: https://doi.org/10.21236/ada400135
[research_williamson_2022]: https://doi.org/10.1016/j.jedc.2021.104146
[research_willsky_1984]: https://doi.org/10.21236/ada147758
[research_willsky_verghese_1984]: https://doi.org/10.21236/ada140931
[research_willsky_verghese_1985]: https://doi.org/10.21236/ada166234
[research_wilps_collatz_1983]: https://doi.org/10.1016/0305-0491(83)90022-6
[research_wilson_2026]: https://doi.org/10.2139/ssrn.6417618
[research_wilson_champneys_2024]: https://doi.org/10.1177/14759217241297098
[research_wilson_riccardi_2022]: https://doi.org/10.1016/j.actaastro.2022.07.013
[research_wilson_riley_1993]: https://doi.org/10.21236/ada273685
[research_wilsondavidj_citurskevind_1994]: https://ntrs.nasa.gov/citations/19950007833
[research_wing_buffeting_2018]: https://doi.org/10.15372/pmtf20180406
[research_wing_wing_2025]: https://doi.org/10.3354/meps14793
[research_winny_1950]: https://doi.org/10.1017/s0001925900000196
[research_wise_sedwick_1999]: https://doi.org/10.21236/ada386935
[research_withers_1981]: https://doi.org/10.1111/j.1474-919x.1981.tb00933.x
[research_witte_monson_2003]: https://doi.org/10.21236/ada421043
[research_wittlin_1988]: https://doi.org/10.1177/058310248802001103
[research_wolfe_1967]: https://doi.org/10.1108/eb034268
[research_wollner_1972]: https://doi.org/10.2514/3.58993
[research_wong_cox_1981]: https://doi.org/10.1016/0167-6105(81)90081-7
[research_wood_araujoestrada_2019]: https://doi.org/10.2514/1.c035416
[research_wood_livingston_1971]: https://doi.org/10.21236/ada021266
[research_woodcockrj_georgefl_1976]: https://ntrs.nasa.gov/citations/19760024077
[research_woodrm_millerds_1985]: https://ntrs.nasa.gov/citations/19850053430
[research_woodrowwhitlowjr_emilyntodd_1999]: https://ntrs.nasa.gov/citations/19990052675
[research_woods_dayyani_2015]: https://doi.org/10.2514/1.c032725
[research_woods_gilbert_1990]: https://doi.org/10.2514/3.25336
[research_woodsjessicaa_gilbertmichaelg_1989]: https://ntrs.nasa.gov/citations/19890014953
[research_wooldridge_1960]: https://doi.org/10.1108/eb033272
[research_wrestler_cliftong_1965]: https://doi.org/10.21236/ad0622404
[research_wright_1945]: https://doi.org/10.21236/adb813734
[research_wu_1976]: https://doi.org/10.21236/ada036672
[research_wu_chen_2017]: https://doi.org/10.1016/j.isatra.2017.06.015
[research_wu_chen_2020]: https://doi.org/10.1002/acs.3119
[research_wu_chiu_1992]: https://doi.org/10.1016/0041-624x(92)90034-j
[research_wu_deng_2015]: https://doi.org/10.1049/iet-cta.2013.0973
[research_wu_fu_2025]: https://doi.org/10.3390/math13243986
[research_wu_gunnion_2015]: https://doi.org/10.1016/j.compstruct.2015.08.114
[research_wu_li_2019]: https://doi.org/10.1109/access.2019.2942526
[research_wu_livne_2016]: https://doi.org/10.2514/1.j054824
[research_wu_livne_2017]: https://doi.org/10.2514/1.j055334
[research_wu_squires_1995]: https://doi.org/10.1115/1.2817310
[research_wu_sun_2021]: https://doi.org/10.1002/acs.3331
[research_wu_sun_2023]: https://doi.org/10.3390/aerospace10090820
[research_wu_tong_2017]: https://doi.org/10.36959/422/431
[research_wu_wang_2024]: https://doi.org/10.1115/1.4067290
[research_wu_wang_2025]: https://doi.org/10.1007/s11071-025-10975-x
[research_wu_wilson_2022]: https://doi.org/10.2514/1.j060959
[research_wu_xiao_2017]: https://doi.org/10.2514/1.c034356
[research_wu_xu_2023]: https://doi.org/10.1016/j.measurement.2023.113214
[research_wu_ye_2024]: https://doi.org/10.1016/j.jfranklin.2024.106914
[research_wu_zhang_2021]: https://doi.org/10.1002/rnc.5743
[research_wu_zuo_2022]: https://doi.org/10.3390/aerospace9100610
[research_wunderlich_2015]: https://doi.org/10.1007/s13272-015-0151-6
[research_wunderlich_dahne_2017]: https://doi.org/10.1007/s13272-017-0266-z
[research_wunderlich_dahne_2017_b]: https://doi.org/10.1007/s13272-017-0251-6
[research_wunderlich_dahne_2021]: https://doi.org/10.2514/1.c036301
[research_wunderlich_dahne_2022]: https://doi.org/10.1007/s13272-022-00585-3
[research_x_2022]: https://doi.org/10.21275/sr22422113319
[research_x_29_research_1991]: https://ntrs.nasa.gov/citations/19940014489
[research_xia_chen_2015]: https://doi.org/10.1016/j.proeng.2015.11.214
[research_xia_huang_2023]: https://doi.org/10.1007/s11465-023-0748-0
[research_xia_li_2016]: https://doi.org/10.1115/1.4034113
[research_xia_li_2026]: https://doi.org/10.26599/ocean.2026.9470017
[research_xiang_liu_2018]: https://doi.org/10.1108/aeat-04-2017-0101
[research_xiang_liu_2024]: https://doi.org/10.1177/01423312241277269
[research_xiang_wang_2023]: https://doi.org/10.1061/jaeeez.aseng-4658
[research_xiao_chen_2026]: https://doi.org/10.1016/j.aei.2026.104678
[research_xiao_dong_2019]: https://doi.org/10.1002/acs.3069
[research_xiao_harrison_2021]: https://doi.org/10.1016/j.compstruct.2020.113526
[research_xiao_liu_2018]: https://doi.org/10.1016/j.ifacol.2018.09.371
[research_xiao_sattarov_2021]: https://doi.org/10.3390/aerospace9010004
[research_xie_li_2021]: https://doi.org/10.1137/20m1345517
[research_xie_liu_2016]: https://doi.org/10.1155/2016/5090719
[research_xie_meng_2017]: https://doi.org/10.1155/2017/2564314
[research_xie_zhang_2025]: https://doi.org/10.3390/aerospace12060525
[research_xie_zhao_2016]: https://doi.org/10.1002/acs.2666
[research_xijuan_qiang_2016]: https://doi.org/10.2514/1.c033252
[research_xinbing_wen_2020]: https://doi.org/10.1088/1742-6596/1605/1/012075
[research_xiong_tang_2026]: https://doi.org/10.1109/taes.2026.3683617
[research_xiong_xu_2025]: https://doi.org/10.2514/1.c038510
[research_xu_2025]: https://doi.org/10.1038/s41598-025-06503-x
[research_xu_2026]: https://doi.org/10.1038/s41598-026-56983-8
[research_xu_fan_2015]: https://doi.org/10.1016/j.neucom.2015.02.069
[research_xu_feng_2025]: https://doi.org/10.1016/j.cja.2025.103443
[research_xu_gao_2015]: https://doi.org/10.1155/2015/258315
[research_xu_guo_2015]: https://doi.org/10.1002/acs.2596
[research_xu_liu_2026]: https://doi.org/10.1177/14759217261457103
[research_xu_oliveira_2021]: https://doi.org/10.1016/j.ejcon.2020.08.003
[research_xu_saleh_2019]: https://doi.org/10.2514/1.j057573
[research_xu_tan_2019]: https://doi.org/10.1016/j.cja.2019.06.003
[research_xu_tian_2024]: https://doi.org/10.1061/jaeeez.aseng-5007
[research_xu_wang_2016]: https://doi.org/10.1371/journal.pone.0167168
[research_xu_xia_2016]: https://doi.org/10.1155/2016/4706925
[research_xu_yang_2026]: https://doi.org/10.1080/27525783.2026.2701580
[research_xu_zha_2021]: https://doi.org/10.2514/1.c035727
[research_xu_zhang_2018]: https://doi.org/10.12783/dtcse/mmsta2017/19666
[research_xu_zhang_2020]: https://doi.org/10.1109/access.2020.3041855
[research_xu_zhang_2025]: https://doi.org/10.1016/j.cja.2024.103332
[research_xu_zhang_2026]: https://doi.org/10.1007/s00158-026-04374-y
[research_xu_zhang_2026_b]: https://doi.org/10.1061/jaeeez.aseng-7009
[research_xue_yao_2020]: https://doi.org/10.2322/tjsass.63.1
[research_xue_ye_2019]: https://doi.org/10.1080/19942060.2019.1663264
[research_xue_yunsong_2021]: https://doi.org/10.1177/0036850421998137
[research_xue_zhao_2026]: https://doi.org/10.1142/s273748072650010x
[research_yagil_raveh_2018]: https://doi.org/10.2514/1.c034353
[research_yahagi_1971]: https://doi.org/10.1080/00207177108932066
[research_yalvac_yats_1991]: https://doi.org/10.1177/002199839102501206
[research_yamakoshi_komatsuzaki_2022]: https://doi.org/10.1299/jsmedmc.2022.109
[research_yamamoto_1992]: https://doi.org/10.2514/3.11227
[research_yamane_1992]: https://doi.org/10.1016/0045-7930(92)90023-o
[research_yamane_friedmann_1993]: https://doi.org/10.2514/3.46315
[research_yamasaki_gotoh_1971]: https://doi.org/10.2208/jscej1969.1971.187_49
[research_yan_han_2025]: https://doi.org/10.2174/0118722121302573240527051750
[research_yan_li_2019]: https://doi.org/10.1051/jnwpu/20193740656
[research_yan_zhang_2023]: https://doi.org/10.1016/j.cja.2023.04.001
[research_yan_zhu_2026]: https://doi.org/10.1080/19942060.2026.2679804
[research_yang_2024]: https://doi.org/10.3390/electronics13020308
[research_yang_batra_1994]: https://doi.org/10.1088/0964-1726/3/4/011
[research_yang_fu_2024]: https://doi.org/10.3390/aerospace11020107
[research_yang_gao_2020]: https://doi.org/10.1109/tac.2019.2918122
[research_yang_guan_2018]: https://doi.org/10.2514/1.g003586
[research_yang_guo_2026]: https://doi.org/10.1063/5.0312919
[research_yang_guruswamy_1980]: https://doi.org/10.21236/ada084172
[research_yang_huang_2017]: https://doi.org/10.2514/1.g002690
[research_yang_huang_2019]: https://doi.org/10.1016/j.jsv.2019.01.006
[research_yang_lee_2015]: https://doi.org/10.1155/2015/218384
[research_yang_li_2023]: https://doi.org/10.3390/math11040919
[research_yang_li_2026]: https://doi.org/10.2514/1.c038587
[research_yang_liu_1976]: https://doi.org/10.21236/ada040077
[research_yang_manning_1994]: https://doi.org/10.2514/3.46502
[research_yang_mao_2022]: https://doi.org/10.1007/s12555-021-0643-6
[research_yang_striz_1981]: https://doi.org/10.2514/3.57576
[research_yang_tang_2026]: https://doi.org/10.1038/s41597-026-07769-0
[research_yang_wan_1978]: https://doi.org/10.21236/ada061942
[research_yang_wang_2022]: https://doi.org/10.1088/1361-665x/ac5808
[research_yang_wang_2025]: https://doi.org/10.1080/23307706.2025.2486673
[research_yang_wang_2026]: https://doi.org/10.1016/j.cja.2026.104412
[research_yang_wu_2025]: https://doi.org/10.1063/5.0280452
[research_yang_xiao_2024]: https://doi.org/10.2514/1.c037399
[research_yang_xie_2019]: https://doi.org/10.1177/0954410019885238
[research_yang_xu_2024]: https://doi.org/10.1007/s11071-024-09764-9
[research_yang_yang_2019]: https://doi.org/10.1016/j.ast.2018.11.050
[research_yang_yu_2026]: https://doi.org/10.1109/access.2026.3690473
[research_yang_yue_2015]: https://doi.org/10.1080/0305215x.2014.995175
[research_yang_yue_2016]: https://doi.org/10.1177/0954410016629497
[research_yang_zhang_2023]: https://doi.org/10.1002/rnc.7026
[research_yang_zhang_2026]: https://doi.org/10.1017/aer.2026.10162
[research_yang_zhao_1989]: https://doi.org/10.2514/3.45806
[research_yang_zhao_1992]: https://doi.org/10.1016/0022-460x(92)90528-6
[research_yang_zhao_2016]: https://doi.org/10.1177/1687814016677207
[research_yao_2018]: https://doi.org/10.1504/ijscip.2018.092320
[research_yao_liu_2020]: https://doi.org/10.1016/j.apor.2020.102374
[research_yao_ma_2021]: https://doi.org/10.1016/j.cja.2021.01.007
[research_yaseen_bayart_2018]: https://doi.org/10.1016/j.ifacol.2018.09.631
[research_yasue_2020]: https://doi.org/10.2514/1.c035564
[research_yates_1966]: https://doi.org/10.2514/3.43702
[research_yates_wynne_1982]: https://doi.org/10.2514/3.44803
[research_yates_wynne_1983]: https://doi.org/10.2514/3.44952
[research_yatesecarsonjr_chulichuan_1987]: https://ntrs.nasa.gov/citations/19870012837
[research_yatesecjr_wynneec_1981]: https://ntrs.nasa.gov/citations/19810016896
[research_ye_chen_2015]: https://doi.org/10.1155/2015/254975
[research_ye_wang_2025]: https://doi.org/10.1177/10775463251350419
[research_ye_yang_2024]: https://doi.org/10.1016/j.ast.2024.109161
[research_yeo_atkins_2015]: https://doi.org/10.2514/1.c032682
[research_yeo_kreshock_2020]: https://doi.org/10.2514/1.c035609
[research_yeo_potsdam_2016]: https://doi.org/10.2514/1.c033194
[research_yepifanov_2020]: https://doi.org/10.2478/tar-2020-0021
[research_yi_2020]: https://doi.org/10.3390/ma13112485
[research_yi_an_2017]: https://doi.org/10.15837/ijccc.2017.3.2617
[research_yildizyidiray_kolmanovskyilyav_2011]: https://ntrs.nasa.gov/citations/20110016004
[research_yildizyildiray_kolmanovskyilyav_2010]: https://ntrs.nasa.gov/citations/20100033693
[research_yin_chu_2019]: https://doi.org/10.2514/1.g004193
[research_yin_huang_2025]: https://doi.org/10.1007/s11768-024-00240-8
[research_yin_ni_2025]: https://doi.org/10.2514/1.c038271
[research_yin_wang_2017]: https://doi.org/10.12783/dtetr/amsm2017/14821
[research_ying_liqiang_2021]: https://doi.org/10.1177/26349833211057137
[research_yingsong_zhichun_2015]: https://doi.org/10.1016/j.proeng.2014.12.506
[research_yiplp_paulsonjwjr_1977]: https://ntrs.nasa.gov/citations/19780005071
[research_yonekura_suzuki_2021]: https://doi.org/10.1007/s00158-021-02851-0
[research_yoo_2017]: https://doi.org/10.2514/1.g002821
[research_yoo_jang_2021]: https://doi.org/10.1109/lcsys.2020.3001663
[research_yoo_jeong_2023]: https://doi.org/10.1007/s11081-023-09827-7
[research_york_williams_1995]: https://doi.org/10.1016/0045-7949(94)00568-n
[research_you_2020]: https://doi.org/10.1088/1742-6596/1678/1/012032
[research_you_kim_2020]: https://doi.org/10.2514/1.j058002
[research_you_lei_2022]: https://doi.org/10.3390/app13010536
[research_you_yasaee_2019]: https://doi.org/10.1016/j.compstruct.2019.111255
[research_younes_hickey_2020]: https://doi.org/10.2514/1.j058922
[research_young_garg_2018]: https://doi.org/10.1016/j.compstruct.2017.09.112
[research_yu_1987]: https://doi.org/10.1115/1.3173110
[research_yu_2018]: https://doi.org/10.4236/mme.2018.84017
[research_yu_bai_2020]: https://doi.org/10.1109/access.2020.3000482
[research_yu_fang_2017]: https://doi.org/10.1016/j.compstruct.2017.05.042
[research_yu_he_2025]: https://doi.org/10.1142/s2301385027500440
[research_yu_lyu_2018]: https://doi.org/10.1016/j.ast.2018.01.016
[research_yu_wang_2017]: https://doi.org/10.1155/2017/1592527
[research_yu_wang_2022]: https://doi.org/10.1016/j.compstruct.2022.116131
[research_yu_yu_2026]: https://doi.org/10.1109/access.2026.3668314
[research_yu_zhang_2016]: https://doi.org/10.2514/1.g001414
[research_yu_zhang_2023]: https://doi.org/10.3390/s23020574
[research_yu_zhang_2026]: https://doi.org/10.3390/aerospace13040348
[research_yu_zhou_2024]: https://doi.org/10.2514/1.j063544
[research_yuan_huo_2018]: https://doi.org/10.1108/aeat-01-2018-0073
[research_yuan_li_2019]: https://doi.org/10.1177/0020294019830115
[research_yuan_thomson_2022]: https://doi.org/10.1016/j.ast.2022.107516
[research_yuan_wang_2024]: https://doi.org/10.1016/j.ast.2024.109305
[research_yuan_zhou_2024]: https://doi.org/10.3390/aerospace11040281
[research_yuanfg_reederjamesr_2001]: https://ntrs.nasa.gov/citations/20010069699
[research_yue_khodaei_2021]: https://doi.org/10.1088/1361-665x/abe4b4
[research_yue_zhang_2017]: https://doi.org/10.1016/j.ast.2017.08.013
[research_yue_zhao_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.103148
[research_yuksek_inalhan_2020]: https://doi.org/10.1002/acs.3181
[research_yunker_lake_2024]: https://doi.org/10.1115/1.4065474
[research_yurtsever_sahin_2026]: https://doi.org/10.3390/aerospace13070596
[research_yutuk_tikenogullari_2021]: https://doi.org/10.1016/j.compfluid.2020.104822
[research_yuvarajan_2001]: https://doi.org/10.21236/ada399688
[research_zadvornyak_martynovich_1983]: https://doi.org/10.1007/bf00905638
[research_zakharov_zattoni_2015]: https://doi.org/10.1016/j.jprocont.2015.07.006
[research_zang_wang_2023]: https://doi.org/10.1007/s11081-023-09858-0
[research_zanoni_gerosa_2022]: https://doi.org/10.1007/s42496-022-00107-8
[research_zapata_perezgonzalez_2025]: https://doi.org/10.1016/j.iot.2025.101627
[research_zarei_arvan_2019]: https://doi.org/10.1002/asjc.2085
[research_zaubeu_2020]: https://doi.org/10.31284/j.jemt.2020.v1i1.1146
[research_zauner_moise_2023]: https://doi.org/10.1007/s10494-023-00415-4
[research_zauner_sandham_2020]: https://doi.org/10.1103/physrevfluids.5.083903
[research_zaw_baranovski_2026]: https://doi.org/10.3390/aerospace13060563
[research_zaytseva_kuznetsov_2021]: https://doi.org/10.18698/0536-1044-2021-12-3-10
[research_zeilerthomasa_1998]: https://ntrs.nasa.gov/citations/19990010052
[research_zeleke_asfaw_2023]: https://doi.org/10.3103/s1068799823040190
[research_zelenkov_2018]: https://doi.org/10.18372/1990-5548.58.13520
[research_zenisek_1973]: https://doi.org/10.1080/00207177308932381
[research_zha_qiao_2026]: https://doi.org/10.1002/msd2.70061
[research_zhai_li_2020]: https://doi.org/10.2514/1.c035766
[research_zhan_li_2025]: https://doi.org/10.1016/j.probengmech.2025.103768
[research_zhang_2023]: https://doi.org/10.1038/s41598-023-46753-1
[research_zhang_bai_2025]: https://doi.org/10.1016/j.addma.2025.104719
[research_zhang_chen_2018]: https://doi.org/10.2514/1.c034232
[research_zhang_chen_2020]: https://doi.org/10.1016/j.compstruct.2019.111696
[research_zhang_dai_2026]: https://doi.org/10.2514/1.j066148
[research_zhang_deng_2022]: https://doi.org/10.3390/aerospace9110657
[research_zhang_deng_2026]: https://doi.org/10.3390/aerospace13010098
[research_zhang_devisser_2018]: https://doi.org/10.2514/1.g002866
[research_zhang_devisser_2019]: https://doi.org/10.2514/1.g003834
[research_zhang_fang_2015]: https://doi.org/10.1016/j.ast.2015.02.024
[research_zhang_guo_2021]: https://doi.org/10.1155/2021/5553304
[research_zhang_han_2018]: https://doi.org/10.1007/s00158-018-2074-4
[research_zhang_han_2020]: https://doi.org/10.3390/act9030070
[research_zhang_he_2026]: https://doi.org/10.1016/j.cja.2025.103582
[research_zhang_huang_2017]: https://doi.org/10.2514/1.a33704
[research_zhang_ji_2022]: https://doi.org/10.1063/5.0090394
[research_zhang_li_2017]: https://doi.org/10.2514/1.c033845
[research_zhang_li_2021]: https://doi.org/10.2316/j.2021.201-0238
[research_zhang_li_2023]: https://doi.org/10.1016/j.cja.2023.04.016
[research_zhang_li_2025]: https://doi.org/10.1109/tmm.2025.3604966
[research_zhang_li_2026]: https://doi.org/10.1080/21642583.2026.2634446
[research_zhang_liu_2018]: https://doi.org/10.1002/asjc.1821
[research_zhang_liu_2019]: https://doi.org/10.1115/1.4043240
[research_zhang_marzocca_2015]: https://doi.org/10.1177/1077546315597180
[research_zhang_qiu_2024]: https://doi.org/10.3390/act13060229
[research_zhang_ran_2023]: https://doi.org/10.3390/app132111844
[research_zhang_rizzi_2017]: https://doi.org/10.1108/aeat-04-2015-0098
[research_zhang_shao_2022]: https://doi.org/10.1049/icp.2022.1599
[research_zhang_shaw_2021]: https://doi.org/10.1016/j.ast.2021.106534
[research_zhang_song_2025]: https://doi.org/10.1016/j.cja.2025.103463
[research_zhang_sun_2020]: https://doi.org/10.1002/acs.3145
[research_zhang_wang_2015]: https://doi.org/10.4028/www.scientific.net/msf.813.54
[research_zhang_wang_2019]: https://doi.org/10.2514/1.c035182
[research_zhang_wang_2020]: https://doi.org/10.1016/j.jfluidstructs.2019.102836
[research_zhang_wang_2022]: https://doi.org/10.1016/j.compstruct.2022.116162
[research_zhang_wang_2022_b]: https://doi.org/10.1007/s00348-022-03528-0
[research_zhang_wang_2026]: https://doi.org/10.1016/j.cja.2026.104377
[research_zhang_xie_2021]: https://doi.org/10.1016/j.cma.2020.113485
[research_zhang_yang_2018]: https://doi.org/10.1016/j.ast.2018.04.043
[research_zhang_yang_2021]: https://doi.org/10.3390/aerospace8080203
[research_zhang_yang_2025]: https://doi.org/10.2514/1.c038158
[research_zhang_yu_2026]: https://doi.org/10.1016/j.automatica.2025.112779
[research_zhang_zhang_2017]: https://doi.org/10.4208/cicp.oa-2016-0132
[research_zhang_zhang_2023]: https://doi.org/10.3390/aerospace10060521
[research_zhang_zhao_2019]: https://doi.org/10.1016/j.jfluidstructs.2019.01.014
[research_zhang_zhao_2023]: https://doi.org/10.3390/aerospace10020197
[research_zhang_zhao_2023_b]: https://doi.org/10.3390/aerospace10120981
[research_zhang_zhao_2026]: https://doi.org/10.1007/s11071-026-12701-7
[research_zhang_zhou_2015]: https://doi.org/10.2514/1.c032739
[research_zhang_zhou_2024]: https://doi.org/10.1007/s00158-024-03820-z
[research_zhang_zhou_2024_b]: https://doi.org/10.1007/s11424-024-3364-0
[research_zhang_zhu_2015]: https://doi.org/10.2174/1874444301406010433
[research_zhao_cheng_2019]: https://doi.org/10.1088/1742-6596/1284/1/012010
[research_zhao_ji_2022]: https://doi.org/10.1016/j.addma.2022.102676
[research_zhao_li_2015]: https://doi.org/10.1016/j.cja.2014.12.036
[research_zhao_li_2019]: https://doi.org/10.1109/access.2019.2930658
[research_zhao_li_2026]: https://doi.org/10.1016/j.energy.2026.140457
[research_zhao_liu_2026]: https://doi.org/10.1016/j.compstruct.2026.120628
[research_zhao_liu_2026_b]: https://doi.org/10.1155/ijae/4223020
[research_zhao_lu_2024]: https://doi.org/10.1109/taes.2023.3333763
[research_zhao_luximon_2015]: https://doi.org/10.1016/j.promfg.2015.07.821
[research_zhao_sun_2019]: https://doi.org/10.1109/access.2019.2933540
[research_zhao_wang_2022]: https://doi.org/10.1016/j.heliyon.2022.e11036
[research_zhao_wang_2025]: https://doi.org/10.1016/j.supflu.2025.106596
[research_zhao_wu_2021]: https://doi.org/10.3390/app11073288
[research_zhao_xing_2023]: https://doi.org/10.1016/j.compstruct.2023.117581
[research_zhao_xu_2024]: https://doi.org/10.3390/drones8090429
[research_zhao_yang_2023]: https://doi.org/10.1109/access.2023.3235482
[research_zhao_yue_2016]: https://doi.org/10.2514/1.c033713
[research_zhao_zhang_2016]: https://doi.org/10.1016/j.ast.2016.07.010
[research_zhao_zhang_2024]: https://doi.org/10.1016/j.jweia.2024.105905
[research_zhao_zhao_2021]: https://doi.org/10.1061/(asce)as.1943-5525.0001288
[research_zhao_zhao_2024]: https://doi.org/10.1016/j.conengprac.2024.105941
[research_zhao_zhou_2024]: https://doi.org/10.1016/j.probengmech.2024.103686
[research_zheng_chen_2016]: https://doi.org/10.1109/tie.2016.2522948
[research_zheng_dai_2026]: https://doi.org/10.1016/j.ast.2026.113066
[research_zheng_pontillo_2024]: https://doi.org/10.1061/jaeeez.aseng-5003
[research_zheng_shao_2025]: https://doi.org/10.1049/icp.2024.2898
[research_zheng_wang_2026]: https://doi.org/10.1016/j.cja.2026.104109
[research_zhijie_taiyu_2025]: https://doi.org/10.1007/s00348-025-04112-y
[research_zhiqiang_xiaozhe_2016]: https://doi.org/10.5139/ijass.2016.17.4.491
[research_zhirabok_filaretov_2024]: https://doi.org/10.31857/s0005231024070026
[research_zhong_goldenfeld_2017]: https://doi.org/10.1364/ol.42.000223
[research_zhong_wang_2026]: https://doi.org/10.1016/j.ast.2026.112392
[research_zhong_ying_2025]: https://doi.org/10.1088/1742-6596/2977/1/012026
[research_zhou_chen_2017]: https://doi.org/10.1016/j.taml.2017.11.006
[research_zhou_cheng_2024]: https://doi.org/10.2514/1.j064022
[research_zhou_dowell_2019]: https://doi.org/10.1016/j.ast.2019.105492
[research_zhou_gong_2026]: https://doi.org/10.1061/jaeeez.aseng-6212
[research_zhou_guan_2026]: https://doi.org/10.1177/14759217251411529
[research_zhou_huang_2021]: https://doi.org/10.1007/s11071-021-06577-y
[research_zhou_huang_2021_b]: https://doi.org/10.1016/j.cnsns.2021.105946
[research_zhou_li_2026]: https://doi.org/10.1177/14759217261423169
[research_zhou_liu_2025]: https://doi.org/10.1002/rnc.70185
[research_zhou_peng_2026]: https://doi.org/10.1016/j.addma.2026.105131
[research_zhou_raze_2025]: https://doi.org/10.2514/1.c038195
[research_zhou_ruan_2019]: https://doi.org/10.1016/j.compstruct.2019.110932
[research_zhou_ruan_2019_b]: https://doi.org/10.1016/j.compstruct.2019.110985
[research_zhou_shen_2025]: https://doi.org/10.1177/14759217251343880
[research_zhou_wang_2017]: https://doi.org/10.1016/j.actaastro.2017.05.011
[research_zhou_wang_2022]: https://doi.org/10.3390/sym14091837
[research_zhou_xu_2019]: https://doi.org/10.1016/j.compstruct.2018.10.035
[research_zhou_yang_2022]: https://doi.org/10.1002/rnc.6503
[research_zhou_ye_1989]: https://doi.org/10.1016/b978-0-08-040185-0.50012-9
[research_zhou_yu_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.03.009
[research_zhu_du_2017]: https://doi.org/10.1007/s11071-017-3382-8
[research_zhu_duan_2015]: https://doi.org/10.1108/aeat-06-2013-0112
[research_zhu_li_2019]: https://doi.org/10.2514/1.j058011
[research_zhu_shi_2022]: https://doi.org/10.1063/5.0076173
[research_zhu_sun_2023]: https://doi.org/10.1016/j.ast.2023.108619
[research_zhu_wang_2017]: https://doi.org/10.2514/1.c034129
[research_zhu_zhang_2024]: https://doi.org/10.1016/j.ast.2024.109745
[research_zhu_zhou_2025]: https://doi.org/10.2514/1.g008194
[research_zhuang_yang_2021]: https://doi.org/10.1016/j.compstruct.2020.112996
[research_zia_liu_2022]: https://doi.org/10.1007/s42242-022-00201-7
[research_ziakos_kilimtzidis_2025]: https://doi.org/10.1007/s13272-025-00851-0
[research_ziegler_1963]: https://doi.org/10.21236/ad0405158
[research_ziegler_2017]: https://doi.org/10.1504/pcfd.2017.088794
[research_zinn_lubarsky_2005]: https://doi.org/10.21236/ada443134
[research_zipperer_jenney_1975]: https://doi.org/10.21236/ada012233
[research_zipperer_jenney_1975_b]: https://doi.org/10.21236/ada009156
[research_zitnan_1989]: https://doi.org/10.1007/bf01396487
[research_zohar_erel_1988]: https://doi.org/10.2514/3.45578
[research_zong_sun_2021]: https://doi.org/10.1088/1742-6596/1786/1/012024
[research_zou_huang_2022]: https://doi.org/10.2514/1.g006114
[research_zou_huang_2024]: https://doi.org/10.1016/j.ymssp.2024.111717
[research_zou_huang_2025]: https://doi.org/10.1016/j.ast.2025.110155
[research_zou_huang_2025_b]: https://doi.org/10.1115/1.4070097
[research_zou_mu_2021]: https://doi.org/10.1016/j.jfranklin.2021.01.012
[research_zou_yao_2017]: https://doi.org/10.2514/1.c034029
[research_zoutendijk_mitici_2021]: https://doi.org/10.3390/aerospace8060152
[research_zuhri_2025]: https://doi.org/10.55981/ijoa.2025.9106
[research_zuo_chen_2015]: https://doi.org/10.1155/2015/753042
[research_zuo_min_2016]: https://doi.org/10.1177/0142331216636189
[research_zvonarev_leontev_2025]: https://doi.org/10.3103/s1068799825040014
