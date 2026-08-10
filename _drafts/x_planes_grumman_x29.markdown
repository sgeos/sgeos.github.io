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
aircraft among its contemporaries.

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
without the others.

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
- [In-flight lift-drag characteristics for a forward-swept wing...][research_saltzmanedwinj_hicksjohnw_1994]
- [Pressure measurements on a forward-swept wing-canard...][research_lombardi_morelli_1994]

- [The Associated Matrices of Bending and Coupled...][research_targoff_1947]
- [Anisotropic Plate Analysis-Boundary Conditions][research_ashton_1970]
- [A computer program for the analysis of the dynamic...][research_picon_alarcon_1978]
- [Characterization of graphite/epoxy laminates for aeroelastic...][research_shyprykevichp_1979]
- [Aeroelastic Tailoring Studies in Fighter Aircraft Design][research_triplett_1980]
- [Applied theory of vibrations of anisotropic laminate shells...][research_kuznetsov_kartashov_1980]
- [Aeroelastic Tailoring of Forward Swept Composite Wings][research_weisshaar_1981]
- [Description of the HiMAT Tailored composite structure and...][research_monaghanrc_1981]
- [The Linear Anisotropic Plate][research_gilbert_schneider_1981]
- [Wind Tunnel Demonstration of Aeroelastic Tailoring Applied to...][research_sherrer_hertz_1981]
- [Effect of Transverse Shear Deformation on Anisotropic Plate...][research_cohen_1982]
- [The Effect of Bending-Torsion Coupling on Fan and Compressor...][research_bendiksen_friedmann_1982]
- [Vibration of Cantilevered Graphite/Epoxy Plates With...][research_jensen_crawley_1982]
- [Frequency Determination Techniques for Cantilevered Plates...][research_jensen_crawley_1984]
- [Aeroelastic tailoring - Theory, practice, and promise][research_shirk_hertz_1986]
- [Aeroelastic tailoring of composite wings with external stores][research_greenja_1986]
- [Residual Stress Measurement of Laminated Anisotropic Plate by...][research_kataoka_dol_1986]
- [Aeroelastic tailoring of aft-swept high-aspect-ratio...][research_green_1987]
- [A General Boundary Integral Formulation for the Anisotropic...][research_shi_bezine_1988]
- [Aeroelastic tailoring for oblique wing lateral trim][research_bohlmannjonathand_weisshaarterrencea_1988]
- [Aeroelastic tailoring of a composite wing with a decoupler...][research_lottati_1988]
- [Aeroelastic tailoring][research_isogai_1988]
- [Finite-Width Correction Factors for Anisotropic Plate...][research_tan_1988]
- [Direct search method to aeroelastic tailoring of a composite...][research_isogai_1989]
- [Static aeroelastic tailoring for oblique wing lateral trim][research_bohlmann_eckstrom_1990]
- [A Taguchi study of the aeroelastic tailoring design process][research_bohlmannjonathand_scottrobertc_1991]
- [Aeroelastic tailoring analysis for advanced turbo propellers...][research_yamane_1992]
- [Multilayered anisotropic plate models with continuous...][research_sciuva_1992]
- [On the static aeroelastic tailoring of composite aircraft...][research_librescu_song_1992]
- [Aeroelastic tailoring analysis for preliminary design of...][research_yamane_friedmann_1993]
- [Thin tailored composite wing for civil tiltrotor][research_raisrohanimasoud_1994]
- [Development of a composite tailoring procedure for airplane...][research_chattopadhyayaditi_zhangsen_1995]
- [Performance Improvement of Composite Wings through...][research_meirovitch_1995]
- [An Investigation of the Aeroelastic Tailoring for Smart...][research_giese_reich_1996]
- [Development of a Composite Tailoring Technique for Airplane...][research_chattopadhyayaditi_jharatneshwar_1996]
- [Aeroelastic Tailoring for Stability Augmentation and...][research_nixonmarkw_piatakdavidj_1999]
- [Active Aeroelastic Tailoring of High-Aspect-Ratio Composite...][research_cesnik_2002]
- [Validation of Design and Analysis Techniques of Tailored...][research_jegleydawnc_wijayratnedulnathd_2004]
- [Active Aeroelastic Tailoring of High-Aspect-Ratio Composite...][research_cesnik_2005]
- [Aeroelastic Tailoring of a Plate Wing with Functionally...][research_dunningpeterd_stanfordbretk_2014]
- [Trim and Structural Optimization of Subsonic Transport Wings...][research_stanfordbretk_juttechristinev_2014]

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
- [Acoustic emissions and transient elastic waves in an...][research_acoustic_emissions_1989]
- [Energy Absorption Behavior of Graphite Epoxy Composite Sine...][research_hanagud_craig_1989]
- [Strength of Composite Laminate with Reinforced Hole][research_lee_mall_1989]
- [Thermal damage effects and delamination toughness of a...][research_thermal_damage_1989]
- [Asymptotic stress field around a crack normal to the...][research_seyoung_1990]
- [Deformational behaviour of a unidirectional graphite/epoxy...][research_deformational_behaviour_1990]
- [Design, Evaluation and Experimental Effort Toward Development...][research_brunojoseph_libeskindmark_1990]
- [On Isotropic Laminate Configurations][research_fukunaga_1990]
- [On the Bearing Strength of Bolted Graphite/Epoxy Laminates][research_eriksson_1990]
- [Static aeroelastic behavior of an adaptive laminated...][research_weisshaarta_ehlerssm_1990]
- [Damage Tolerance of Woven Graphite/Epoxy Buffer Strip Panels][research_kennedy_1991]
- [Laminate Plate Theory for Spatially Distributed Induced...][research_wang_rogers_1991]
- [Tanker Operations in a Composite Wing Concept][research_raper_1991]
- [Transverse Ply Cracking in Toughened and Untoughened...][research_yalvac_yats_1991]
- [C-130 Advanced Technology Center wing box conceptual...][research_whiteheadrs_foremancr_1992]
- [Closed-form analytical solutions for a Griffith crack in a...][research_becker_1992]
- [Interlaminar shear fracture of interleaved graphite/epoxy...][research_interlaminar_shear_1992]
- [Mode I Interlaminar Fracture of Interleaved Graphite/Epoxy][research_ozdil_carlsson_1992]
- [On the propagation of horizontally polarized shear waves in a...][research_wu_chiu_1992]
- [Proven Force--Proof of Concept for the Composite Wing][research_norwood_1992]
- [A damage mechanics tool for laminate delamination][research_daudeville_ladeveze_1993]
- [Aeroelastic airfoil smart spar][research_greenhalgh_pastore_1993]
- [An analytically designed subcomponent test to reproduce the...][research_davisddjr_farleygaryl_1993]
- [Analysis of an anisotropic composite laminate with a...][research_hong_cheong_1993]
- [Global/local interlaminar stress analysis of a grid-stiffened...][research_wiggenraadjfm_bauldnrjr_1993]
- [Laminate characterisation in the presence of thermal stresses][research_biswas_1993]
- [On the contact of a spherical indenter and a thin composite...][research_christoforou_1993]
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
- [Evaluation of a Metallic Repair on a Rod-Stiffened Composite...][research_przekopadam_jegleydawnc_2014_b]

- [Aircraft Structural Research][research_shanley_1943]
- [Charts for the Determination of Wing Torsional Stiffness...][research_pearsonhenrya_aikenwilliamsjr_1944]
- [Stress Analysis of Wing Center Section - Part III - Interspar...][research_mefford_voss_1948]
- [On the Elastic Instability of Orthogonal Anisotropic...][research_hayashi_1949]
- [Effect of Torsional Stiffness Requirements on Wing Structural...][research_micks_1950]
- [WING - STRESS ANALYSIS. MIG-15, SERIAL NO. 120147][research_cornellaeronauticallabincbuffalony_1953]
- [DESIGN PROPERTIES OF HIGH-STRENGTH STEELS IN THE PRESENCE OF...][research_sachs_muvdi_1956]
- [The Balance Method Applied to Swept-Wing Stress Analysis][research_broglio_1957]
- [EFFECT OF HEATING ALUMINUM ALLOY WING STRUCTURE TO 325 F ON...][research_bergstedt_turner_1959]
- [STRUCTURAL FLIGHT LOADS DATA FROM JET-TANKER OPERATIONS][research_perry_rievley_1961]
- [NEW APPROACHES TO FLIGHT VEHICLE STRUCTURAL VIBRATION...][research_heckl_lyon_1962]
- [Designing for structural reliability][research_switzky_1965]
- [RESEARCH IN AIRCRAFT STRUCTURES ANALYSIS AND DESIGN][research_horton_mayers_1965]
- [Structural analysis flexible grid technique for sst wing...][research_miller_1965]
- [FATIGUE STRENGTH DESIGN AND ANALYSIS OF AIRCRAFT STRUCTURES...][research_abelkis_1967]
- [Torsion of Structural Concrete-Interaction Surface for...][research_torsion_of_1968]
- [Methodology for Structural Optimization of STOL Aircraft...][research_wollner_1972]
- [Advanced Metallic Structure Air Superiority Fighter Wing...][research_figge_1973]
- [Advanced Metallic Structures Air Superiority Fighter Wing...][research_davis_1973]
- [Bending and torsion of anisotropic beams][research_johnson_1973]
- [Fatigue Behavior of Graphite/Glass/Epoxy Composites][research_rao_hofer_1973]
- [Identification and optimization of aircraft dynamics][research_narendra_tripathi_1973]
- [T-38 Structural Flight Loads Data for June 1970 through...][research_clay_rockafellow_1973]
- [A Structural Weight Estimation Program SWEEP for Aircraft...][research_wildermuth_rothammer_1974]
- [A fatigue-testing machine for combined bending and torsion][research_shawki_mashhour_1974]
- [Application of advanced composites to helicopter airframe...][research_richmj_ridgleygf_1974]
- [Feasibility Investigation of Zero-Torsional-Stiffness...][research_vance_brown_1974]
- [Modeling engine static structures with conical shell finite...][research_kielb_1975]
- [F-111A Wing Fatigue Test Program][research_schneider_1976]
- [Titanium and advanced composite structures for a supersonic...][research_turnermj_hoyjm_1976]
- [A-37B Fatigue Sensor Evaluation Program - Full Scale Test and...][research_walker_kaufman_1977]
- [Development of advanced composite structures][research_staufferwa_jamesam_1978]
- [Strength of Prestressed Concrete I-Beams in Combined Torsion...][research_strength_of_1978]
- [Study of advanced composite structural design concepts for an...][research_study_of_1978]
- [Transverse shear stiffness of laminated anisotropic shells][research_cohenga_1978]
- [An Efficient Structural Resizing Procedure for Meeting Static...][research_lerner_markowitz_1979]
- [An Evaluation of the ADINA Finite Element Program for...][research_stagliano_mente_1979]
- [Composite Materials for Structural Design][research_schpey_1980]
- [The History of the Aircraft Structural Integrity Program][research_negaard_1980]
- [Effect of Fighter Attack Spectrum on Composite Fatigue Life][research_badaliance_dill_1981]
- [A simulation language approach to structural interaction...][research_cutchinsma_purvisjw_1982]
- [Composite aircraft structure having lightning protection][research_olsonglenno_1982]
- [Composite structural materials][research_ansellgs_loewyrg_1982]
- [Designing for Aircraft Structural Crashworthiness][research_thomson_caiafa_1982]
- [Sonic fatigue testing of an advanced composite aileron][research_soovere_1982]
- [Structure-Property Relationships in Intercalated Graphite][research_dresselhaus_dresselhaus_1982]
- [Aeroelastic interference effects between slender structures][research_ruscheweyh_1983]
- [Research on Composite Materials for Structural Design][research_allen_bradley_1983]
- [Structure and Properties of Intercalated Graphite...][research_forsman_1983]
- [Unsteady aerodynamics and vortex induced aeroelastic...][research_modi_slater_1983]
- [ACEE composite structures technology][research_klotzschem_1984]
- [Research on Composite Materials for Structural Design][research_allen_bradley_1984]
- [A more accurate evaluation of buckling loads of thin-walled...][research_toader_1987]
- [Aircraft Structural Crash Dynamics Progress in the 1980's][research_wittlin_1988]
- [Composite transport wing technology development Design...][research_griffincharlesf_harvillwilliame_1988]
- [In-Plane Stress Waves for NDE Nondestructive Evaluation of...][research_pellerin_1988]
- [On the validity of the reduced bending stiffness method for...][research_ewing_hinger_1988]
- [Prediction of aircraft-propeller-induced, structure-borne...][research_unruh_1988]
- [Development of a Progressive Failure Model for Strength of...][research_tang_1989]
- [Multi-objective/loading optimization for rotating composite...][research_hamiltonbriank_petersjamesr_1989]
- [Optimum structural design with static aeroelastic constraints][research_bowmankeithb_grandhiramanav_1989]
- [Certification of damage tolerant composite structure][research_rapoffandrewj_dillharoldd_1990]
- [Structural optimization with aeroelastic constraints of rotor...][research_celi_friedmann_1990]
- [Vibration analysis of composite plate wing][research_lee_lee_1990]
- [Active Structural Acoustic Control and Smart Structures][research_fuller_1991]
- [Application of a design-build-team approach to low cost and...][research_ilcewiczlb_walkerth_1991]
- [Adaptive aeroelastic composite wings - Control and...][research_weisshaarterrencea_ehlersstevenm_1992]
- [An improved approach for flight readiness certification...][research_moorenr_ebbelerdh_1992]
- [Control design of a UH-60 rotorcraft via CLTR and direct...][research_vansteenwykbrett_lyuyloi_1992]
- [Helicopter rotor blade aeroelasticity in forward flight with...][research_cell_1992]
- [Integrated aerodynamic-structural-control wing design][research_raisrohanim_haftkart_1992]
- [Stresses in edge stiffened anisotropic sandwich plate][research_rao_umamaheswararao_1992]
- [Survey - Applications of structural optimization methods to...][research_miurahirokazu_neilldouglasj_1992]
- [For the advance of the computational structural aeroelasticity][research_ohkuma_1993]
- [Aeroelastic behavior of a composite plate wing with...][research_koo_lee_1994]
- [Aircraft fleet maintenance based on structural reliability...][research_yang_manning_1994]
- [On structural optimization with aeroelasticity constraints][research_ringertz_1994]
- [Tailoring the dynamic characteristics of composite panels...][research_raouf_1994]
- [Ultrasonic Evaluation of Stiffness Tensor Changes and...][research_audoin_baste_1994]
- [Unsteady Aerodynamics and Vortex-Induced Aeroelastic Response...][research_modi_slater_1994]
- [Unsteady Structure of Leading-Edge Vortices on a Delta Wing][research_rockwell_1994]
- [Using adaptive structures to attenuate rotary wing...][research_nitzsche_breitbach_1994]
- [Aeroelastic analysis of a flexible control surface with...][research_lee_kim_1995]
- [Equivalent dynamic beam rod models of aircraft wing structures][research_lee_1995]
- [Flight Control Applications of 1 sub 1 Optimization][research_spillman_ridgely_1995]
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

### The Flight Control System

**A thirty-five percent negative static margin is a statement about time.**

The unstable airframe's pitch response splits into two real roots, one of them positive, and the positive
root sets how long the aircraft takes to double a disturbance. Neglecting pitch damping, which errs toward
less available time rather than more,

$$ M_\alpha = \frac{q\,S\,\bar{c}\,C_{m_\alpha}}{I_{yy}}, \qquad t_2 = \frac{\ln 2}{\sqrt{M_\alpha}} $$

The lift-curve slope in the table below is not quoted anywhere in the record and is estimated from the
planform by the standard low-aspect-ratio relation.

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
- [Design Guide Handbook for the Design of...][research_cully_boller_1973]
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
- [Integrated Electric Actuator Application to Flight Control...][research_hammer_bright_1998]
- [Closed-Loop System Identification Experience for Flight...][research_patrickcmurphy_1999]
- [Modular Control Law Design for the Innovative Control...][research_buffington_1999_b]
- [Constrained Control Allocation Methods for Reconfigurable...][research_bodson_2000]
- [Restoring Redundancy to the MAP Propulsion System][research_odonnelljamesrjr_davisgaryt_2002]
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
- [METHODS OF ANALYSIS AND SYNTHESIS OF PILOTED AIRCRAFT FLIGHT...][research_northropaircraftinchawthorneca_1952]
- [Static Stability Wind-Tunnel Test of 18, 22, and 26 Caliber...][research_chaplin_1953]
- [A complete system for the flight-testing of piloted aircraft][research_vandoren_1955]
- [STATIC STABILITY AND MAGNUS CHARACTERISTICS OF THE 5-INCH...][research_greene_1955]
- [AUTOMATIC FLIGHT CONTROL SYSTEMS FOR PILOTED AIRCRAFT][research_hart_1956]
- [STABILITY ANALYSES OF FLYING PLATFORM IN HOVERING AND FORWARD...][research_albachten_1956]
- [STATIC STABILITY AND MAGNUS CHARACTERISTICS OF A LOW-DRAG...][research_greene_1956]
- [STATIC AND DYNAMIC STABILITY TESTS OF A PROPOSED VERSION OF...][research_shantz_demeritte_1958]
- [Effect of Artificial Pitch Damping on the Longitudinal and...][research_moulmartint_brownlawrencew_1959]
- [The Present Status of Aircraft Stability Problems in the...][research_taylor_1959]
- [STATIC STABILITY AND DRAG OF THE HOPI WEAPON][research_carroll_1960]
- [Static stability and control characteristics of two...][research_fosswejr_whitcombcf_1960]
- [A Note on the Effect of a Time-Varying Forward Flight...][research_swaim_1961]
- [A Study of Longitudinal Control Problems at Low and Negative...][research_sadoffmelvin_mcfaddennormanm_1961]
- [AN INVESTIGATION OF THE EFFECTS OF INDUCED NONSYMMETRIC...][research_boatwright_1961]
- [Effects of Control-Feel Configuration on Airplane...][research_craneharoldl_sommerrobertw_1961]
- [INVESTIGATION OF STATIC STABILITY AND AERODYNAMIC EFFECTS OF...][research_anderson_1961]
- [AUTOMATIC CONTROL OF STATIC ELECTRICITY FOR ARMY HELICOPTERS][research_tona_1962]
- [MINUTEMAN WING I ENVIRONMENTAL CONTROL SYSTEM RELIABILITY...][research_gearhart_1962]
- [SIMPLIFIED ANALYSIS OF FLEXIBLE BOOSTER FLIGHT CONTROL SYSTEMS][research_hofmann_kezer_1962]
- [A GAMMA GUIDANCE SYSTEM FOR HELICOPTER FLIGHT-FORMATION...][research_wilcox_1963]
- [AIR FORCE FLIGHT CONTROL AND FLIGHT DISPLAY INTEGRATION...][research_gainer_1963]
- [DESIGN AND DEVELOPMENT OF A FLIGHT PATH CONTROL SYSTEM FOR...][research_ostheimer_giguere_1963]
- [STATIC STABILITY TESTS ON A 0.098 SCALE STANDARD LAUNCH...][research_ziegler_1963]
- [THE EFFECT OF NONLINEAR STATIC COUPLING ON THE MOTION...][research_kinney_1963]
- [A GENERAL INVESTIGATION OF HYPERSONIC STABILITY AND CONTROL...][research_flightscienceslabincbuffalony_1964]
- [A forced-oscillation method for dynamic- stability testing][research_kilgore_averett_1964]
- [AN ANALYSIS OF TERMINAL FLIGHT PATH CONTROL IN CARRIER LANDING][research_durand_teper_1964]
- [INVESTIGATION OF THE CONCEPT OF DIRECT FLIGHT CONTROL][research_craig_1965]
- [LIFT, DRAG, AND STATIC STABILITY OF A BLUNT CONICAL MODEL IN...][research_boylan_1965]
- [RESEARCH ON ACCELERATED RELIABILITY TESTING METHODS...][research_johnson_1965]
- [UH-2 JET-AUGMENTED HIGH-SPEED RESEARCH HELICOPTER...][research_blackburn_whitfield_1965]
- [COMPUTER ANALYSIS OF FORKLIFT TRUCK STABILITY WHEN OPERATING...][research_deninno_uherka_1966]
- [SPACE VEHICLE NAVIGATION, GUIDANCE, AND CONTROL][research_langston_1967]
- [BOATTAIL EFFECTS ON STATIC STABILITY AT SMALL ANGLES OF ATTACK][research_washington_pettis_1968]
- [Investigation of tilt-rotor VTOL aircraft rotorpylon stability][research_edenborough_1968]
- [STATIC, FREE VIBRATION, AND STABILITY ANALYSIS OF THIN...][research_kalnins_1968]
- [An In-Flight Investigation to Develop Control System Design...][research_neal_smith_1970]
- [Feedback Control of VTOL Aircraft][research_dukes_1970]
- [An In-Flight Investigation of Bank-Angle Control Parameters...][research_hall_1971]
- [Conceptual Study to Apply Advanced Flight Control Technology...][research_smith_hammer_1971]
- [Study to Determine the Application of Aircraft...][research_drummond_1971]
- [Formulations of the Equations of Motion of an Elastic...][research_schwanz_1972]
- [Surface Effect Take-Off and Landing System SETOLS Subsonic...][research_davidson_hd_1972]
- [A parametric study of planform and aeroelastic effects on...][research_roskamj_lanc_1973]
- [Effect of Various External Stores on the Static Longitudinal...][research_whoric_1973]
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
- [“Optimal Control of a Maglev Vehicle”∗][research_gottzein_cramer_1975]
- [Advanced control technology and its potential for future...][research_hermanarediess_1976]
- [Aeroelastic Rotor Stability Analysis][research_johnston_cassarino_1976]
- [Design of a control configured tanker aircraft][research_walkersa_1976]
- [Digital Electronic Propulsion Control System Problems and...][research_kuhlberg_newirth_1976]
- [Engine Evaluation of Advanced Technology Control Components][research_morrison_white_1976]
- [Experimental Results from a Static Stability and Pressure...][research_lindsay_fikes_1976]
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
- [Estimate of Orbiter Static Aeroelasticity Properties via...][research_cavin_holyoak_1978]
- [Flight Evaluation of Flight-Path Control for the STQL...][research_franklin_innis_1978]
- [Flight Verification of the Advanced Flight Control Actuation...][research_demarchi_haning_1978]
- [Flight-determined stability and control coefficients of the...][research_iliffkw_mainere_1978]
- [Ordinary Differential Equations Oscillation and Stability...][research_leighton_1978]
- [Aeroelastic Stability Analysis of the AD-1 Manned...][research_rutkowski_1979]
- [An Adaptive Control for Vehicle Suspensions][research_sachs_1979]
- [Design Criteria for Dry Lubricated Flight Control Bearings][research_nagy_1979]
- [Entrophy Analysis of Feedback Flight Dynamic Control Systems][research_weidemann_leondes_1979]
- [Maintenance Training System 6883 Converter/Flight Control...][research_baum_clark_1979]
- [A Variable Free Control Characteristic Vehicle][research_dorey_good_1980]
- [Design and Test of a Hydra-Optic Flight Control Actuation...][research_kohnhorst_magnacca_1980]
- [Experience with an adaptive stick-gain algorithm to reduce...][research_powersbg_1980]
- [Roll Resonance Control of Angle of Attack for Reentry Vehicle...][research_platus_1980]
- [Advanced Aircraft Electrical System Control Technology...][research_dunn_leong_1981]
- [Selected stability and control derivatives from the first...][research_iliffkw_mainere_1981]
- [Transient Response Test Procedures for Measuring Vehicle...][research_verma_1981]
- [Criteria for Side-Force Control in Air-to-Ground Target...][research_sammondsroberti_mcneillwaltere_1982]
- [In-Flight Evaluation of Control System Pure Time Delays][research_berry_powers_1982]
- [A Study of Digitally Controlled Flight Control Actuation][research_belmont_1983]
- [Equivalent angle-of-attack method for estimating nonlinear...][research_hemsch_nielsen_1983]
- [Experimental Study of Active Vibration Control][research_hallauer_jr_1983]
- [Stability of Two‐Bladed Aeroelastic Rotors on Flexible...][research_chen_1983]
- [A Digital Linear Position Sensor for Flight Control Actuation][research_jenney_schreadley_1984]
- [Analysis of Aircraft Attitude Control Systems Prone to...][research_hess_1984]
- [Flight evaluation of a digital electronic engine control in...][research_burcham_myers_1985]
- [A perspective on superaugmented flight control - Advantages...][research_mcruerd_johnstond_1986]
- [An Application of a LISP Based Expert System for Failure...][research_loh_1986]
- [Calculating Aerodynamic-Stability Derivatives][research_lance_1986]
- [Environmental Assessment for Proposed Aircraft Replacement...][research_departmentoftheairforcewashingtondc_1986]
- [Experimental Study of Flight Effect on Fan Noise 1st Report...][research_kobayashi_torisaki_1986]
- [A Survey of Aircraft Integrated Control Technology][research_hill_1987]
- [Adaptive Control of Vehicle Suspension][research_hac_1987]
- [Aeroelastic stability characteristics of a composite swept...][research_lottati_1987]
- [An analysis of a candidate control algorithm for a ride...][research_suikatreiner_donaldsonkent_1987]
- [Configuration Control Method of a Control Configured Robot...][research_fukuda_kobayashi_1987]
- [Space radiation effects on the dimensional stability of a...][research_space_radiation_1987]
- [Stability boundaries for command augmentation systems][research_shrivastavapc_1987]
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
- [Aeroelastic stability of aircraft with circulation control...][research_haas_chopra_1990]
- [Eigenspace Design of Helicopter Flight Control Systems][research_garrard_low_1990]
- [Extended implicit model following as applied to integrated...][research_schmidtdavidk_schiermanjohnd_1990]
- [Integrated flight/propulsion control for supersonic STOVL...][research_franklinjamesa_stortzmichaelw_1990]
- [On Control Laws for Vehicle Suspensions Accounting for Input...][research_sharp_wilson_1990]
- [Parametric aeroelastic stability analysis of a generic X-wing...][research_woods_gilbert_1990]
- [Stability sensitivity studies for synthesis of aeroelastic...][research_lu_murthy_1990]
- [Static stability and control characteristics of scissor wing...][research_rokhsaz_selberg_1990]
- [A Control Configured Design Method and its Application to Car...][research_kawabe_tokumaru_1991]
- [A knowledge-based system design/information tool for aircraft...][research_mackalldalea_allenjamesg_1991]
- [Analysing manipulator and feel system effects in aircraft...][research_hess_1991]
- [Control configuration of a relaxed stability airship][research_nagabhushan_1991]
- [Fuzzy logic for control of roll and moment for a flexible...][research_fuzzy_logic_1991]
- [Periodic Model‐Following for the Control‐Configured Helicopter][research_mckillip_1991]
- [Interface Protocol Requirements for Shipboard Damage Control...][research_tate_1992]
- [Optimal Linear Preview Control of Active Vehicle Suspension][research_hac_1992]
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
- [Robust control of a nonlinear time-delay system][research_tharp_zhang_1994]
- [COMPUTING THE STATICS AND DYNAMICS OF AIRPLANE AILERON...][research_grossschmidt_pahapill_1995]
- [Improvement of Vehicle Dynamics by Rear Braking Force Control][research_morita_matsukawa_1995]
- [Numerical study of a supersonic open cavity flow and pressure...][research_jeng_payne_1995]
- [Review of the State of Development of Advanced Vehicle...][research_shladover_1995]
- [Thrust-Induced Effects on a Pitching-Up Delta Wing Flow Field...][research_vandommelen_1995]
- [Control of Transition in Swept-Wing Boundary Layers Using...][research_saric_1997]
- [Including Aeroelastic Effects in the Calculation of X-33...][research_zeilerthomasa_1998]
- [Backup Attitude Control Algorithms for the MAP Spacecraft][research_odonnelljamesrjr_andrewsstephenf_1999]
- [Modular Control Design for the Innovative Control Effectors...][research_buffington_1999]
- [Nonlinear Control of Fighter Aircraft][research_wise_sedwick_1999]
- [Robust Nonlinear Control of Tailless Aircraft][research_teel_1999_b]
- [Robust Nonlinear Control of Tailless Fighter Aircraft][research_teel_1999]
- [Active Stall Control Mutlistage Compression Systems][research_abed_2000]
- [Adaptive Algorithms for Active Noise and Vibration Control][research_bodson_2000_b]
- [Effects of Inadvertent UH-60 Cockpit Airbag System Deployment...][research_brozoski_johnson_2000]
- [Hybrid Active/Passive Control of Sound Radiation from Panels...][research_cabellrandolphh_gibbsgaryp_2000]
- [Intelligenct Flight Control of Uninhabited Aerial Vehicles][research_bernstein_2000]
- [Results From F-18B Stability and Control Parameter Estimation...][research_moestimothyr_noffzgregoryk_2000]
- [Smart-Material Actuated Missile Flight Control Surfaces...][research_giurgiutiu_pomirleanu_2000]
- [A Distributed Active Vibration Absorber DAVA and Associated...][research_fuller_2001]
- [Vehicle Control Unit VCU for the HMMWV][research_californiaunivlosangeles_2001]
- [AFFTC Instruction 99-5, Test and Evaluation Test and Control...][research_airforceflighttestcenteredwardsafbca_2002_b]
- [Sliding Mode Control Applied to Reconfigurable Flight Control...][research_wells_2002]
- [Steering Control Compensation of Accelerating Vehicle Motion][research_burns_2002]
- [Robust Flight Control][research_enns_2003]
- [Robust and Optimal Control of Spatially Interconnected...][research_dandrea_2003]
- [Application of Computational Stability and Control Techniques...][research_schusterdavidm_edwardsjohnw_2004]
- [Control of Systems With Periodic Coefficients, With...][research_celi_lovera_2004]
- [Multi-Vehicle Experimental Platform for Distributed...][research_how_2004]
- [Dynamic-Active Flow Control - Phase I][research_soria_2006]
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
- [Aero-Effected Flight Control Using Distributed Active Bleed][research_glezer_leonard_2012]
- [Control of Metastatic Colonization in Prostate Cancer The...][research_szmulewitz_2012]
- [An Aircraft Electric Power Testbed for Validating...][research_rogersten_xu_2013]
- [Active Flow Control with Thermoacoustic Actuators][research_taira_2014]
- [Theory, Guidance, and Flight Control for High Maneuverability...][research_fresconi_celmins_2014]

- [STABILITY AND CONTROL CHARACTERISTICS OF DOUGLAS MODEL...][research_huff_ww_1949]
- [FLIGHT EVALUATIONS OF VARIOUS LONGITUDINAL HANDLING QUALITIES...][research_harper_robertp_1955]
- [Handling Qualities of Helicopters and VTOL Aircraft][research_reeder_1958]
- [An analytical and flight-test approach to the reduction of...][research_levi_nelson_1964]
- [Simulator investigation of the effects of l alpha and true...][research_chalk_1964]
- [Effect of variable sweep on supersonic transport handling...][research_higgins_shomber_1965]
- [Research on vtol aircraft handling qualities criteria][research_miller_clark_1965]
- [An assessment of the lateral-disectional handling qualities...][research_teper_stapleford_1966]
- [Experimental investigation of pilot dynamics in a...][research_hirsch_mccormick_1966]
- [Navy variable-stability studies of longitudinal handling...][research_eney_1968]
- [Comments on "Navy Variable-Stability Studies of Longitudinal...][research_malcom_1969]
- [Volume II. Flying Qualities Phase, Chapter 16. Chapter 16...][research_airforcetestpilotschooledwardsafbca_1969]
- [A regression analysis of pilot-induced oscillation ratings][research_eichler_1970]
- [Higher-order control system dynamics and longitudinal...][research_difranco_1970]
- [An Approac e Determination of Aircraft Handling Qualities...][research_adams_hatch_1971]
- [The Development of Flying Qualities for Lifting Re-Entry...][research_difranco_1971]
- [The Generation of a Military Specification for Flying...][research_key_1971]
- [Analytic Design of Digital Flight Controllers to Realize...][research_montgomery_1972]
- [Design of Desirable Airplane Handling Qualities via Optimal...][research_kriechbaum_stineman_1972]
- [Factors Affecting Handling Qualities of a Lift‐Fan Aircraft...][research_gerdes_hynes_1972]
- [Longitudinal handling qualities during approach and landing...][research_franklinja_innisrc_1972]
- [Flight Simulator Experiments and Analyses in Support of...][research_vinje_miller_1973]
- [A Two-Phase Investigation of Longitudinal Flying Qualities...][research_boothe_chen_1974]
- [Interactive Computer-Aided Design Aircraft Flying Qualities...][research_place_altmann_1974]
- [Analysis of longitudinal pilot-induced oscillation tendencies...][research_smithjw_berrydt_1975]
- [Handling Qualities Evaluation of the XV‐15 Tilt Rotor Aircraft][research_marr_roderick_1975]
- [Handling qualities of aircraft with stabilty and control...][research_hodgkinson_lamanna_1976]
- [Handling qualities requirements for control configured...][research_woodcockrj_georgefl_1976]
- [Simulator study of the low-speed handling qualities of a...][research_granthamwd_nguyenlt_1976]
- [Handling Qualities of Aircraft in the Presence of Simulated...][research_jacobson_joshi_1978]
- [Analysis of a lateral pilot-induced oscillation experienced...][research_smithjw_1979]
- [Design of Desirable Handling Qualities for Aircraft Lateral...][research_ohta_nikiforuk_1979]
- [Effects of Dynamic Aeroelasticity on Aircraft Handling...][research_swaim_yen_1979]
- [Handling Quality Requirements for Advanced Aircraft Design...][research_smith_geddes_1979]
- [Powered-Lift Aircraft Handling Qualities in the Presence of...][research_jewell_heffley_1979]
- [V/STOL Aircraft Design Sensitivity to Flying Qualities...][research_chancevoughtcorpdallastx_1979]
- [Landing flying qualities evaluation criteria for augmented...][research_radfordrc_smithr_1980]
- [Analysis of augmented aircraft flying qualities through...][research_baileyre_smithre_1981]
- [Effect of Winglets on Performance and Handling Qualities of...][research_vandam_holmes_1981]
- [Flying qualities criteria and flight control design][research_berrydt_1981]
- [An Adaptive Stick-Gain to Reduce Pilot-Induced Oscillation...][research_powers_1982]
- [Criteria for Low-Speed Longitudinal Handling Qualities of...][research_stinton_1985]
- [Handling qualities related to stall/spin accidents of...][research_anderson_1985]
- [Toward a unifying theory for aircraft handling qualities][research_hess_sunyoto_1985]
- [Longitudinal flying qualitites criteria for single-pilot...][research_bargill_stengel_1986]
- [Volume II. Flying Qualities Phase. Chapter 14 Flight Control...][research_airforcetestpilotschooledwardsafbca_1988]
- [Theory for aircraft handling qualities based upon a...][research_hess_1989]
- [Volume II. Flying Qualities Phase. Chapter 9 Roll Coupling][research_airforcetestpilotschooledwardsafbca_1989]
- [Volume II. Flying Qualities Phase. Chapter 5 Longitudinal...][research_airforcetestpilotschooledwardsafbca_1990]
- [Volume II. Flying Qualities Phase. Chapter 6 Maneuvering...][research_airforcetestpilotschooledwardsafbca_1990_e]
- [Volume II. Flying Qualities Phase. Chapter 7...][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Computer Aided Evaluation of Aircraft Handling Qualities][research_chetty_lakshmi_1991]
- [Flying quality analysis and flight evaluation of a highly...][research_tischlermarkb_fletcherjayw_1991]
- [Optimum aeroelastic design of helicopter rotors for...][research_celi_1991]
- [Volume II. Flying Qualities Flight Test. Chapter 11...][research_airforcetestpilotschooledwardsafbca_1992]
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
- [Effect of downwash on the induced drag of canard-wing...][research_butler_1982]
- [Minimum Induced Drag of Canard Configurations][research_kroo_1982]
- [An analytical study of the induced drag of canard-wing-tail...][research_butler_1983]
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
- [The theoretical minimum induced drag of three-surface...][research_kendall_1985]
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
- [Induced drag prediction for wing-tail and canard...][research_lombardi_vicini_1994]
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

- [RESEARCH ON HIGH SPEED ROTARY-FIXED WING AIRCRAFT. VOLUME IV...][research_snyder_1950]
- [Altitude Performance of Modified J71 Afterburner with Revised...][research_usellerjamesw_russeyroberte_1955]
- [Aeroelastic Problems of Low Aspect Ratio Wings][research_farbridge_woodward_1956]
- [EFFECT OF PERFORMANCE CRITERIA ON THE OPTIMUM DESIGN OF THE...][research_dallas_irvin_1956]
- [Hovering Static Stability and Performance Experiments on...][research_carmichael_mcnay_1961]
- [INVESTIGATION OF DRAG REDUCTION BY BOUNDARY-LAYER SUCTION ON...][research_pate_deitering_1963]
- [INVESTIGATION OF DRAG REDUCTION BY BOUNDARYLAYER SUCTION ON A...][research_pate_1964]
- [ANALYTIC STUDY OF AIRCRAFT AGILITY IN THE TURNAROUND MANEUVER][research_wrestler_cliftong_1965]
- [A parametric study of planform and aeroelastic effects on...][research_roskamj_lanc_1972]
- [Evaluation of Energy Maneuverability Procedures in Aircraft...][research_johnson_1972]
- [Maneuver and buffet characteristics of fighter aircraft][research_rayej_mckinneylw_1972]
- [Modeling the Effects of Pilot Performance on Weapon Delivery...][research_leondes_rankine_1972]
- [Maneuver and buffet characteristics of fighter aircraft][research_rayej_mckinneylw_1973]
- [Low-speed wind-tunnel investigation of the aerodynamic and...][research_abbottjm_millerba_1974]
- [Army Preliminary Evaluation YAH-1R Improved Cobra Agility and...][research_stewart_dominick_1975]
- [Program for establishing long-time flight service performance...][research_harvillwe_kizerja_1976]
- [Effect of Display Color on Pilot Performance and Describing...][research_chase_1977]
- [Optimization of flexible wing structures subject to strength...][research_haftka_1977]
- [The Influence of Vehicle Control Dynamics on Driver-Vehicle...][research_repa_alexandridis_1977]
- [Positive Tail Loads for Minimum Induced Drag of Subsonic...][research_laitone_1978]
- [Effects of Helmet Loader Cues on Simulator Pilot Performance][research_ashworth_mckissick_1979]
- [The Performance of a Conceptual Vertical Attitude Takeoff and...][research_papadales_basils_1979]
- [Investigation of High-Angle-of-Attack Maneuver-Limiting...][research_mitchell_myers_1980]
- [Drag reduction of trailer-tractor configuration by...][research_wong_cox_1981]
- [THE AERODYNAMIC PERFORMANCE OF THE WING IN RED‐SHOULDERED...][research_withers_1981]
- [Performance Measures for Aircraft Carrier Landings as a...][research_connelly_1982]
- [Aeroelastic behavior of low aspect ratio metal and composite...][research_whitejfiii_bendiksenoo_1986]
- [An Appreciation of Tactical Agility as a Function of the...][research_lovatt_1986]
- [Improving Light Infantry Divisional Engineer Agility the Key...][research_janecek_1986]
- [Agility A Key to the Operational Art][research_bryant_albert_1988]
- [Riblet drag reduction at flight conditions][research_walshmichaelj_sellerswilliamliii_1988]
- [Fighter agility metrics][research_lieferrandallk_1990]
- [Impact of emerging technologies on future combat aircraft...][research_nguyenluatt_gilertwilliamp_1990]
- [Active Suspension Control Performance Comparisons Using...][research_crolla_abdelhady_1991]
- [Use of piloted simulation for high-angle-of-attack agility...][research_marilyneogburn_johnvfoster_1991]
- [The Army--From the Sea The Army's Initiative to Enhance...][research_brown_1994]
- [Application of Navier-Stokes aeroelastic methods to improve...][research_schuster_1995]
- [Advanced Technology Composite Fuselage-Structural Performance][research_walkerth_minguetpj_1997]
- [Agility Measures Engineering Agile Systems][research_goranson_1997]
- [Personality Factors Affecting Pilot Combat Performance A...][research_siem_murray_1997]
- [Force Projection, Strategic Agility and the Big Meltdown][research_hill_2001]
- [High Performance Power Supply for the More Electric Aircraft][research_yuvarajan_2001]
- [Performance Analysis of a Wing With Multiple Winglets][research_smith_komerath_2001]
- [Agility Agent - Ility Architecture][research_thompson_bannon_2002]
- [Security Agility for Dynamic Execution Environments][research_fraser_petkac_2002]
- [Workload Demands of Remotely Piloted Vehicle Supervision and...][research_wickens_dixon_2002]
- [Creating Strategic Agility in Northeast Asia][research_hunter_2003]
- [High Performance and High-Fidelity Aeroelastic Simulation of...][research_lesoinne_2007]
- [Optimum Design of a Flexible Wing Structure to Enhance Roll...][research_veley_khot_2008]
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
- [Re-Entry Module/Adapter Interconnect Fairing Aerodynamic...][research_sheldon_1967]
- [INSPECTION, REPAIRS AND MODIFICATIONS, AND FLIGHT TEST OF THE...][research_irvine_1968]
- [ROTOR/WING SERIES VI WIND TUNNEL TEST 7-FOOT DIAMETER MODEL...][research_briardy_head_1968]
- [WIND TUNNEL INVESTIGATION OF THE THROTTLE FOR THE PROPOSED...][research_anderson_1968]
- [A Flight Envelope Expansion Study for the XH-51A Compound...][research_cruz_gorenberg_1969]
- [WIND TUNNEL TESTS OF A FREE-WING TILT-PROPELLER V/STOL...][research_strand_levinsky_1969]
- [Flight Test Results of a DAVI Isolated Platform][research_jones_1970]
- [Results of the ATA CAS Flight Test Program][research_borrok_rider_1970]
- [U.S. Air Force Aircraft in Southeast Asia Tested by the Air...][research_airforceflighttestcenteredwardsafbca_1970]
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
- [Stability and Control. Volume 1. Stability and Control Flight...][research_airforceflighttestcenteredwardsafbca_1974]
- [Stability and Control. Volume 2. Stability and Control Flight...][research_airforceflighttestcenteredwardsafbca_1974_b]
- [An Experimental Study of Several Wind Tunnel Wall...][research_binion_tw_1975]
- [Analysis of Flight Data for Deepwell System Installed in...][research_kuhn_1975]
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
- [Volume IV. Flight Test Management. Chapter 1. Introduction to...][research_airforcetestpilotschooledwardsafbca_1990_c]
- [Volume IV. Flight Test Management. Chapter 5. Flight Test...][research_airforcetestpilotschooledwardsafbca_1990_d]
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
- [Volume IV. Flight Test Management. Chapter 5A...][research_airforcetestpilotschooledwardsafbca_1993]
- [Airship Applications of Modern Flight Test Techniques][research_brennan_mcdaniel_1994]
- [Interferometric GPS Flight Reference/Autoland System Flight...][research_vangraas_diggle_1994]
- [Artificial Intelligence Techniques for Flight Test Planning...][research_stottier_1995]
- [Developing Flight Test Techniques to Ensure Proper Rigging of...][research_traven_whitley_1995]
- [Estimation of the longitudinal and lateral-directional...][research_napolitanomarcellor_1996]
- [Flight Test Automation Options][research_carico_1998]
- [Naval Rotary Wing Aircraft Flight Test Squadron Flight Test...][research_mertaugh_1998]
- [Flight Test Control Room Personnel Training and Evaluation][research_airforceflighttestcenteredwardsafbca_2002]
- [Flight Investigation of Prescribed Simultaneous Independent...][research_moestimothyr_smithmarks_2003]
- [Instrumentation for Wind Tunnel Transient Growth Studies][research_white_2004]
- [Wind Tunnel to Atmospheric Mapping for Static Aeroelastic...][research_heegjennifer_spaincharlesv_2004]
- [Base Pressure Computations of the DERA Generic Missile Wind...][research_despirito_2005]
- [Experimental Results from the Active Aeroelastic Wing Wind...][research_heegjennifer_spaincharlesv_2005]
- [Control Surface Interaction Effects of the Active Aeroelastic...][research_heegjennifer_2006]
- [Static Aeroelastic Scaling and Analysis of a Sub-Scale...][research_tingeric_lebofskysonia_2014]

- [THE AERODYNAMIC CHARACTERISTICS OF A 75-DEG SWEPT DELTA WING...][research_clark_spurlin_1962]
- [Aerodynamics of Finned Missiles at High Angle of Attack][research_oberkampf_nicolaides_1971]
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
- [Fundamental aerodynamic characteristics of delta wings with...][research_woodrm_millerds_1985]
- [High angle-of-attack calculations of the subsonic vortex flow...][research_almosnino_1985]
- [Recent computational fluid dynamics works about high angle of...][research_fujii_1985]
- [Spiral vortex flow over a swept-back wing][research_poll_1986]
- [Calculation of aerodynamic characteristics at high angles of...][research_lancedward_tsengjb_1987]
- [Vortex influence on oscillating airfoils at high angle of...][research_favier_maresca_1987]
- [Influence of the aspect ratio on the aerodynamics of the...][research_zohar_erel_1988]
- [LDV surveys over a fighter model at moderate to high angles...][research_sellerswilliamliii_meyersjamesf_1988]
- [Leading edge vortex dynamics on a pitching delta wing][research_lemaysp_batillsm_1988]
- [Vortex filament model of the wake behind a missile at high...][research_vantuyl_1988]
- [Wind-tunnel investigation of the forebody aerodynamics of a...][research_banksdanielw_1988]
- [Knowledge-based system of supermaneuver selection for pilot...][research_chin_1989]
- [Numerical simulation of the effects of variation of angle of...][research_ekaterinarisja_schifflewisb_1990]
- [In-flight leading-edge vortex flow-field survey measurements...][research_richwinedavidm_fisherdavidf_1991]
- [Volume II. Flying Qualities Flight Testing Phase. Chapter 10...][research_airforcetestpilotschooledwardsafbca_1991]
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
- [Vector Solution of the Three-Degree Case of Wing Bending...][research_arnold_1942]
- [Three-Dimensional Wing Flutter Analysis][research_flax_1943]
- [Torsional and Aileron Flutter][research_krzywoblocki_1943]
- [The Flutter of a Uniform Cantilever Wing][research_goland_1945]
- [Flutter and oscillating air-force calculations for an airfoil...][research_garrickie_rubinowsi_1946]
- [Flutter and oscillating air-force calculations for an airfoil...][research_garrickie_rubinowsi_1946_b]
- [Once More - Single Degree of Freedom Flutter of an Aileron][research_abichandani_rosenberg_1952]
- [Single Degree of Freedom Flutter of an Aileron][research_runyan_cunningham_1952]
- [Note on the Use of Two-Dimensional Compressible Flow...][research_werdes_1953]
- [NACA Conference on Aircraft Loads, Structures, and Flutter][research_naca_conference_1957]
- [HYDROFOIL FLUTTER PHENOMENON AND AIRFOIL FLUTTER THEORY...][research_henry_1961]
- [Wind Tunnel Tests and Further Analysis of the Floating Wing...][research_gabel_ricks_1961]
- [FLUTTER SIMULATION][research_kearns_1962]
- [Flutter Analysis of Supersonic Ring Wing][research_crimi_ordway_1962]
- [Transonic flutter investigation of models of a proposed...][research_gurleyjrjr_ruhlincl_1962]
- [Bending-torsional flutter of a swept wing in a highdensity...][research_herrmanng_nematnassers_1966]
- [Flutter studies of simplified component models of a...][research_abeli_ruhlincl_1966]
- [Modified-strip-analysis method for predicting wing flutter at...][research_yates_1966]
- [Bending-torsional flutter of a swept wing in a high-density...][research_prasad_nematnasser_1967]
- [A Non-Linear Solution to a Tab-Aileron Flutter Problem][research_dlbirdsall_1970]
- [Investigation of Helicopter Control Loads Induced by Stall...][research_arcidiacono_carta_1970]
- [A Comparison of Methods for the Analysis of Wing-Tail...][research_triplett_burkhart_1971]
- [A Feasibility Study of Active Wing/Store Flutter Control][research_triplett_1972]
- [Selective reinforcement of wing structure for flutter...][research_cooperpa_stroudwj_1972]
- [Bending Flutter and Torsional Flutter of Flexible Hydrofoil...][research_besch_liu_1973]
- [The Evaluation of a Stall-Flutter Spring-Damper Pushrod in...][research_adams_1973]
- [Flutter analysis of swept-wing subsonic aircraft with...][research_housnerjm_steinm_1974]
- [Finite element flutter analysis of multi-web wing structures][research_rao_1975]
- [Comparison of supercritical and conventional wing flutter...][research_farmermg_hansonpw_1976]
- [Design, Fabrication, Testing and Analysis of Torsion Free...][research_murphy_peloubet_1976]
- [Drag Effects on Wing Flutter][research_petre_ashley_1976]
- [Flutter and buckling of general laminated plates][research_sawyerjw_1976]
- [The design, analysis, and testing of a low-budget wind-tunnel...][research_boldingrm_stearmanro_1976]
- [Analytical Flutter Studies of a Subsonic, Actively...][research_lehman_stearman_1977]
- [Effect of Chordwise Forces and Deformations and Deformations...][research_boyd_1977]
- [Investigation of Torsion Free Wing Trend Flutter Models][research_yang_wan_1978]
- [On the Transonic-Dip Mechanism of Flutter of a Sweptback Wing][research_isogai_1979]
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
- [Highly Maneuverable Aircraft Technology HiMAT flight-flutter...][research_kehoemw_1984]
- [Measurement of transonic dips in the flutter boundaries of a...][research_persoon_horsten_1984]
- [Flutter clearance of the Schweizer 1-36 deep-stall sailplane][research_kehoemw_ellisonjf_1985]
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
- [Shape Sensitivity Analysis of Flutter Response of a Laminated...][research_kapania_bergen_1991]
- [Supersonic flutter analysis of clamped symmetric composite...][research_lee_cho_1991_b]
- [Subharmonic bifurcation analysis of wing with store flutter][research_yang_zhao_1992]
- [Flutter analysis of cantilevered curved composite panels][research_pidaparti_1993]
- [Flutter analysis of stiffened laminated composite plates and...][research_liao_sun_1993]
- [Flutter calculations for fixed and rotating wings with...][research_nibbelinkbruced_petersdavida_1993]
- [Large-Amplitude Finite Element Flutter Analysis of Composite...][research_gray_mei_1993]
- [Supersonic flutter analysis of composite plates and shells][research_pidaparti_yang_1993]
- [Finite element flutter analysis of laminated composite panels][research_chowdary_parthan_1994]
- [Flutter clearance flight tests of an OV-10A airplane modified...][research_doggettrobertvjr_riverajoseajr_1995]
- [Unstructured Euler flutter analysis of two-dimensional...][research_pan_cheng_1995]
- [Improved Flight Test Procedures for Flutter Clearance][research_lindrickc_brennermartinj_1997]
- [Flutter Model Technology][research_busan_1998]
- [CEAS/AIAA/ICASE/NASA Langley International Forum on...][research_woodrowwhitlowjr_emilyntodd_1999]
- [Robust Nonlinear Control of Stall and Flutter in Aeroengines][research_kokotovic_murray_2000]
- [Bifurcations of Control Systems with Application to Flutter][research_krener_2001]
- [System Identification Methods for Improving Flutter Flight...][research_klyde_harris_2004]

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
- [Transonic time responses of the MBB A-3 supercritical airfoil...][research_batina_yang_1985]
- [Control law synthesis for an airplane with relaxed static...][research_blight_gangsaas_1986]
- [Landing approach handling qualities of transport aircraft...][research_wilhelm_schafranek_1986]
- [Sensitivity method for integrated structure/active control...][research_gilbertmichaelg_1987]
- [Tailless aircraft performance improvements with relaxed...][research_ashkenasirvingl_klydedavidh_1989]
- [Transonic aeroelasticity of fighter wings with active control...][research_guruswamy_tu_1989]
- [Regulation of relaxed static stability aircraft][research_kwatny_bennett_1991]
- [Intelligent Signal Processing for Active Control][research_ramamoorthy_1992]
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

- [Aeroelastic Tailoring of Transport Wings Including Transonic...][research_stanfordbretk_wiesemancarold_2015]
- [An analytical model for composite tubes with bend twist...][research_jonnalagadda_sawant_2015]
- [Finite element modeling and effects of material uncertainties...][research_murray_doman_2015]
- [Optimization of Tow-Steered Composite Wing Laminates for...][research_stodieck_cooper_2015]
- [A novel dynamic aeroelastic framework for aeroelastic...][research_werter_debreuker_2016]
- [Aeroelastic Tailoring of a Composite Forward-Swept Wing Using...][research_tian_yang_2016]
- [Bend-Twist Coupling Behavior of 10 MW Composite Wind Blade][research_kim_shin_2016]
- [On the use of bend twist coupling in full-scale composite...][research_das_kapuria_2016]
- [Static and Dynamic Aeroelastic Tailoring with Variable-Camber...][research_stanford_2016_b]
- [Aeroelastic Tailoring and Active Aeroelastic Wing Impact on a...][research_alyanak_pendleton_2017]
- [Aeroelastic Tailoring of a Representative Wing Box Using...][research_stodieck_cooper_2017]
- [Aeroelastic tailoring of an NLF forward swept wing][research_wunderlich_dahne_2017_b]
- [Aeroelastic tailoring of high-aspect-ratio composite...][research_chen_han_2017]
- [Efficient Method for Aeroelastic Tailoring of Composite Wing...][research_yu_wang_2017]
- [Evolutionary-based aeroelastic tailoring of stiffened...][research_marques_natarajan_2017]
- [Multidisciplinary optimization of an NLF forward swept wing...][research_wunderlich_dahne_2017]
- [A beam finite element for analysis of composite beams with...][research_babuska_wiebe_2018]
- [Load-dependent bend-twist coupling effects on the...][research_young_garg_2018]
- [A robust and reliability-based aeroelastic tailoring...][research_othman_silva_2019]
- [An efficient implementation of aeroelastic tailoring based on...][research_li_gong_2019]
- [Preliminary design of aeroelastically tailored wing box...][research_mihailaandres_rosu_2019]
- [The buckling of CFRP composite plates in compression and...][research_loughlan_2019]
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
- [Tailored twist morphing achieved using graded bend twist...][research_gu_taghipour_2022]
- [Bend-twist coupling effects on the cavitation behavior and...][research_liu_zhang_2023]
- [Compression buckling of elastically supported cylindrical...][research_ansari_zucco_2023]
- [Computationally efficient optimal design of hygrothermally...][research_shakya_padhee_2023]
- [A study on interactive fiber rubber composite structures...][research_annadata_endesfelder_2024]
- [Multidisciplinary optimization of high aspect ratio composite...][research_ahmadi_farsadi_2024]
- [Impact of material and geometrical parameters on the...][research_sharifi_vincenti_2025]
- [Multiscale modelling strategy for a novel wingbox structure...][research_miranda_li_2025]
- [Solution of Deformation of Bend-Twist Coupling Box Beam...][research_shao_sun_2025]
- [Critical buckling analysis and multi-objective optimal design...][research_cui_miao_2026]
- [Mechanical characterization of bend-twist coupling behavior...][research_gonzalezmontijo_vanness_2026]
- [Structural Parameter Selection for Lightweight Composite...][research_zaw_baranovski_2026]

- [1408 A study on aerodynamic characteristics of a forward...][research_kohara_tomoeda_2016]
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
- [Transition prediction including turbulent wedges for a...][research_fehrs_kaiser_2025]
- [Aerodynamic shape design of oblique wing for...][research_sun_zhang_2026]
- [Flight Dynamics Modeling and Sliding Mode Control Law Design...][research_liu_li_2026]
- [Supersonic Aerodynamic Enhancement of Swept-Forward and...][research_theerthamalai_ramanan_2026]
- [Vortex behavior over a tailless forward-swept wing with chine...][research_saheby_jialu_2026]

- [On divergence tests for composite hypotheses under composite...][research_martin_pardo_2017]
- [Interval analysis of the wing divergence][research_li_wang_2018]
- [Critical elastic parameters motivating divergence instability...][research_agwa_2019]
- [Divergent instability control of aeroelastic system driven by...][research_liu_2019]
- [New Mechanism of the Aeroelastic Divergence Onset][research_vedeneev_2020]
- [The Wing Divergence Problem in a Supersonic Gas Flow][research_kulikov_2020]
- [Aerodynamic Compensation Methods for Aeroelastic Divergence...][research_kornev_ambrozhevich_2021]
- [Stability/Instability Study and Control of Autonomous...][research_furtat_gushchin_2021]
- [Aeroelastic Structural Analysis to Calculate Symmetrical...][research_awadallaalihajahmed_2024]
- [Estimate Anti-symmetrical Divergence Modes of an Aircraft...][research_awadallaalihajahmed_2024_b]
- [Sentinels of change divergence in trophic niche of New...][research_wing_wing_2025]
- [Climate risk attention divergence and supply chain instability][research_hu_qiu_2026]
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

- [Structural Dynamic Analysis of a Hypersonic Composite Wing][research_zhang_wang_2015]
- [Identification of reduced-order model for an aeroelastic...][research_tang_wu_2017]
- [Nonlinear aeroelastic flutter and dynamic response of...][research_chen_li_2017]
- [Adaptive nonlinear optimal control for active suppression of...][research_tang_chen_2018]
- [Analysis of classical flutter in steam turbine blades using...][research_prasad_pesek_2018]
- [Study of Flexible Aircraft Body Freedom Flutter with...][research_iannelli_marcos_2018]
- [Influence of stochastic perturbations of composite laminate...][research_nitschke_vincenti_2019]
- [Aeroelastic Wing Planform Design Optimization of a Flutter...][research_hermanutz_hornung_2020]
- [Weight optimization of a composite wing-panel with flutter...][research_shrivastava_tilala_2020]
- [Sensitivity study and structural optimization of an aircraft...][research_kusni_widiramdhani_2021]
- [Flutter Predictions for Very Flexible Wing Wind Tunnel Test][research_goizueta_wynn_2022_b]
- [Nonlinear disturbance observer-based control of a structural...][research_mahgoub_elbadawy_2022]
- [Numerical Analysis of Glauert Inflow Formula for Single-Rotor...][research_dodic_krstic_2023]
- [Active aeroelastic flutter control of supersonic smart...][research_moreira_moleiro_2024]
- [Experimental Nonlinear Modal Analysis of an F-16 Aircraft...][research_zhou_raze_2025]
- [Studying body-freedom flutter mechanism via a rigid-elastic...][research_zou_huang_2025]
- [Variable-order framework for aeroelastic flutter analysis of...][research_campagna_benedetti_2025]
- [Nonlinear aeroelastic analysis and flutter control of...][research_zhao_liu_2026]
- [Nonlinear aeroelastic metastructure for wing flutter...][research_tian_wang_2026]
- [Thermo-Aeroelastic Flutter Instability and Nonlinear...][research_qi_yuan_2026]
- [Tiltrotor Whirl Flutter Mitigation Through Active Mini-Tab...][research_adeyemi_bull_2026]

- [A Composite Method for Human Foot Structural Modeling][research_zhao_luximon_2015]
- [Advance ratio effects on the flow structure and unsteadiness...][research_raghav_komerath_2015]
- [Composite Structure Modeling and Analysis of Advanced...][research_mukhopadhyayvivek_sorokachmichaelr_2015]
- [Frequency and Time Domain Analysis of an Aeroelastic Wing...][research_chakravarthy_evans_2015]
- [Multidisciplinary wing optimization of commercial aircraft...][research_wunderlich_2015]
- [On thermal instability of delaminated composite plates][research_nikrad_asadi_2015]
- [Reliability based optimization in aeroelastic stability...][research_suryawanshi_ghosh_2015]
- [Static aeroelastic optimisation to wing structural weight...][research_yi_jun_2015]
- [A method for nonlinear aeroelasticity trim and stability...][research_wang_zhu_2016]
- [Aeroelastic analysis of CNT reinforced functionally graded...][research_song_zhang_2016]
- [Aeroelastic characteristics of magneto-rheological fluid...][research_asgari_kouchakzadeh_2016]
- [Non-linear dynamic instability analysis of laminated...][research_darabi_ganesan_2016]
- [Structural analysis of composite components considering...][research_mayer_prowe_2016]
- [A reduced order state space model for aeroelastic analysis in...][research_marqui_bueno_2017]
- [Aeroelastic Analysis of Deployable Wing using Reduced Order...][research_otsuka_makihara_2017]
- [Aeroelastic Optimization of High-Speed Tiltrotor Wings with...][research_kambampati_smith_2017]
- [Dynamic instability of variable stiffness composite plates][research_loja_barbosa_2017]
- [Non-linear vibration and dynamic instability of...][research_darabi_ganesan_2017]
- [Nonlinear Static Aeroelasticity of High-Aspect-Ratio-Wing...][research_castellani_cooper_2017]
- [Nonlinear aeroelastic analysis of curved laminated composite...][research_an_khoo_2017]
- [Practical Methods for Aircraft and Rotorcraft Flight Control...][research_hodgkinson_2017]
- [Aero structural optimization for sailplane wing in...][research_aero_structural_2018]
- [Constraint aggregation for large number of constraints in...][research_zhang_han_2018]
- [Design and Optimization of Wing Structure for a Fixed-Wing...][research_yu_2018]
- [Design, manufacturing and structural testing of all-composite...][research_siwowski_kulpa_2018]
- [Dynamic instability of rotating doubly-tapered laminated...][research_seraj_ganesan_2018]
- [Dynamic instability of variable angle tow composite plates...][research_chen_nie_2018]
- [Dynamic mechanical analysis and thermoelasticity for...][research_cannella_garinei_2018]
- [Efficient aeroelastic reduced order model with global...][research_chen_li_2018]
- [Multiobjective optimization of an aircraft wing design with...][research_caixeta_marques_2018]
- [Shape optimization of streamlined decks of cable-stayed...][research_cidmontoya_hernandez_2018]
- [Wing twisting by elastic instability A purely passive approach][research_runkel_fasel_2018]
- [Aeroelastic analysis of CNT reinforced functionally graded...][research_swain_adhikari_2019]
- [Aeroelastic behavior of composite panels undergoing...][research_tsunematsu_donadon_2019]
- [Aeroelastic global structural optimization using an efficient...][research_li_daronch_2019]
- [Aeroelastic optimization of composite wings including fatigue...][research_rajpal_kassapoglou_2019]
- [Aeroelastic stability analysis of curved composite panels...][research_zhou_xu_2019]
- [Approximate static aeroelastic analysis of composite wings][research_kobelev_2019]
- [Geometrically nonlinear static aeroelastic analysis of...][research_tsushima_yokozeki_2019]
- [Modal optimization approach for composite aeroelastic wing...][research_lv_lei_2019]
- [On aeroelastic stability of a piezo-MRE sandwich plate in...][research_soleymani_arani_2019]
- [Optimized design and analysis of composite flexible wing...][research_choi_park_2019]
- [Structural analysis of wing ribs obtained by additive...][research_carneiro_gamboa_2019]
- [Structural and aeroelastic analyses of a wing with tip rotor][research_zhang_zhao_2019]
- [A cross-sectional aeroelastic analysis and structural...][research_feil_pflumm_2020]
- [Assessment of low-altitude atmospheric turbulence models for...][research_deskos_delcarre_2020]
- [Experiments on Flexible Filaments in Air Flow for...][research_silvaleon_cioncolini_2020]
- [Fiber-Optic Strain-Based Deflection and Twist Sensing for a...][research_penafrancisco_2020]
- [Simulation and Optimization of Takeoff Maneuvers of Very...][research_delcarre_palacios_2020]
- [Vertically Optimal Close Formation Flight Control Based on...][research_zhai_li_2020]
- [A novel method for estimating three-domain limit cycles in a...][research_wang_wu_2021]
- [Aeroelastic Optimization Design of the Global Stiffness for a...][research_li_wan_2021]
- [Aeroelastic analysis of foam-filled composite corrugated...][research_zhuang_yang_2021]
- [Linear aeroelastic analysis of cantilever hybrid composite...][research_camacho_akhavan_2021]
- [Multi-Fidelity Optimization of a Composite Airliner Wing...][research_kafkas_kilimtzidis_2021]
- [STRUCTURE POWER AIRCRAFT FUSELAGE 5774 TRAINER][research_pratama_2021]
- [Stress Analysis of Composite Aircraft Wing using Coupled...][research_jaffarsyedmohamedali_shahzatulsakinahbintiharon_2021]
- [A reduced-order multi-body model with...][research_shan_bilgen_2022]
- [Aeroelastic Shape Control Using Fiber-Optic-Measured Strain...][research_simbuerger_raveh_2022]
- [Aeroelastic Topology Optimization of Wing Structure Based on...][research_wang_zhang_2022]
- [Aeroelastic optimization design of composite materials blade...][research_zhang_wang_2022]
- [Aeroelastic shape optimization of solid foam core wings...][research_conlansmith_andreasen_2022]
- [Efficient aeroelastic wing optimization through a compact...][research_poole_allen_2022]
- [Exploration of the effect of wing component post-buckling on...][research_hahn_haupt_2022]
- [Normal stress flow evaluation in composite aircraft wing...][research_marin_graciani_2022]
- [Vortex structure of longitudinal scale flow in a 28-row...][research_han_zhang_2022]
- [A two-level strategy for aeroelastic optimization of a 3D...][research_desouza_deleon_2023]
- [Aeroelastic modeling and analysis of honeycomb plates in...][research_ni_li_2023]
- [An improved reduced order model for bladed disks including...][research_schwerdt_maroldt_2023]
- [Causal-relationship-assisted shape design optimization for...][research_chen_dong_2023]
- [Comparison of Linear Flexible Aircraft Model Structures on...][research_juhasz_tischler_2023]
- [Finite Element Model Updating for Very Flexible Wings][research_sharqi_cesnik_2023]
- [Fully Coupled Aeroelastic Stability Analysis of Adaptive...][research_parthivnshah_ericlblades_2023]
- [Multiscale Aeroelastic Optimization Method for Wing Structure...][research_li_yang_2023]
- [Robust multidisciplinary analysis and optimization for...][research_saporito_daronch_2023]
- [Static aeroelasticity analysis of a rotor blade using a...][research_li_luo_2023]
- [Aeroelastic reduced-order modeling for efficient static...][research_li_kou_2024]
- [Morphing wing design of truss-braced-wing aircraft through...][research_li_zhang_2024]
- [Multidisciplinary analysis and structural optimization for...][research_benaouali_boutemedjet_2024]
- [Optimized Design and Test of Geometrically Nonlinear Static...][research_li_qian_2024]
- [Possibilities of the finite element method for the analysis...][research_fedorenko_bondarenko_2024]
- [Probabilistic aeroelastic analysis of high-fidelity composite...][research_mcgurk_stodieck_2024]
- [Towards Structural and Aeroelastic Similarity in Scaled Wing...][research_filippou_kilimtzidis_2024]
- [Wing optimization for static aeroelastic effect][research_sun_2024]
- [A DG-VLM framework for computational static aeroelastic...][research_campagna_gulizzi_2025]
- [Computational Optimization of Flow Control over Aircraft Wing...][research_balasubramanian_jayanarasimhan_2025]
- [Efficient static aeroelastic wing optimization based on PSO...][research_bugala_payenskyy_2025]
- [Evaluation of a Biomathematical Modeling Software Tool for...][research_devine_choynowski_2025]
- [Genetic algorithm optimized artificial immune system for...][research_kizildeniz_kiyak_2025]
- [High angle-of-attack control of fixed-wing UAVs using...][research_li_hu_2025]
- [Low-Fidelity Static Aeroelastic Analysis for Jig Shape...][research_bugala_2025]
- [Outcomes of Nonlinear Static Aeroelasticity for Wing Stress...][research_verri_desilvabussamra_2025]
- [Sequential-based non-probabilistic reliability optimization...][research_wang_tian_2025]
- [Static Strength Evaluation of Composite Aircraft Wing for...][research_kumar_asha_2025]
- [Structural Analysis and Control Optimization of Finger...][research_dong_2025]
- [Toward sustainable additive manufacturing of PEKK/Martian...][research_malekpour_abdali_2025]
- [Aeroacoustic Optimizations of Internal Bay Cavity Flow...][research_lee_lua_2026]
- [Bayesian optimization framework for mixed-variable wing...][research_xu_zhang_2026]
- [Generative AI-driven inverse design optimization of composite...][research_sun_chen_2026]
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
- [FlightQM a multi-agent system for the analysis of flight...][research_fortis_fortis_2015]
- [Human Supervisory Control of Robotic Teams Integrating...][research_human_supervisory_2015]
- [Micro Vortex Generators for Boundary Layer Control Principles...][research_sun_2015]
- [Nonlinear Aeroelastic Analysis of Control Surface with...][research_morino_obayashi_2015]
- [Novel Control Effectors for Truss Braced Wing][research_whiteedwardv_kapaniarakeshk_2015]
- [Sensor allocation with guaranteed exponential stability for...][research_moarref_rodrigues_2015]
- [Stability robustness of linear quadratic regulators][research_chen_holohan_2015]
- [mcfTRaptor Toward unobtrusive on-the-fly control-flow tracing...][research_tewar_myers_2015]
- [Adaptive Output-Feedback Control with Closed-Loop Reference...][research_qu_annaswamy_2016]
- [Aircraft Control Surface and Store Freeplay-Induced...][research_kholodar_2016]
- [Analysis of Pilot-Induced-Oscillation and Pilot Vehicle...][research_mandal_gu_2016]
- [Impacts of safety on the design of light remotely-piloted...][research_dirito_schettini_2016]
- [Influence of Attack Angle on Magnetohydrodynamic Flow Control...][research_masuda_shimosawa_2016]
- [Modeling and Incremental Nonlinear Dynamic Inversion Control...][research_difrancesco_mattei_2016]
- [Simulation of Laminar-Flow Compatible High-Lift Wing...][research_rizzetta_visbal_2016]
- [Stabilization of the PVTOL aircraft based on a sliding mode...][research_aguilaribanez_2016]
- [Subsumption architecture applied to flight control using...][research_oland_andersen_2016]
- [Time-Domain Stability Margin Assessment][research_clementskeith_2016]
- [A UAV Flight Control Algorithm for Improving Flight Safety][research_park_jung_2017]
- [Adaptive LFT control of a civil aircraft with online...][research_ferreres_hardier_2017]
- [Cross-flow effects regarding laminar flow control within...][research_schueltke_stumpf_2017]
- [Dynamic Modeling and Active Morphing Trajectory-Attitude...][research_guo_hou_2017]
- [FAULT DIAGNOSIS OF AN AIRCRAFT CONTROL SURFACES WITH AN...][research_ogunvoul_balanchuk_2017]
- [FLOW CONTROL THROUGH VORTEX SHEDDING INTERACTION OF ONE...][research_payton_2017]
- [Flight dynamic modeling and control for a telescopic wing...][research_yue_zhang_2017]
- [Fly-by-Feel Control of an Aeroelastic Aircraft Using...][research_armanious_lind_2017]
- [Hovering control for quadrotor aircraft based on finite-time...][research_zhu_du_2017]
- [A Learn-To-Fly Approach for Adaptively Tuning Flight Control...][research_jaredagrauer_2018]
- [Active suppression of freeplay aeroelastic vibrations of...][research_dul_2018]
- [Adaptive Control of Hypersonic Flight Vehicles With Limited...][research_liu_an_2018]
- [Adaptive Feedforward Control for Gust-Induced Aeroelastic...][research_wang_daronch_2018]
- [Adaptive Load Control of Flexible Aircraft Wings Using Fiber...][research_penafrancisco_martinsbenjamin_2018]
- [Analysis of Asymmetric Control Efficiency for Folding Wing...][research_xu_zhang_2018]
- [Design for Robust Aircraft Flight Control][research_hess_peng_2018]
- [Distributed Propulsion Aircraft with Aeroelastic Wing Shaping...][research_nguyen_reynolds_2018]
- [Experimental investigation of plasma vortex generator in flow...][research_ghayour_mani_2018]
- [Nonlinear Aeroelastic Control of Very Flexible Aircraft Using...][research_wang_wynn_2018]
- [Nonlinear control for underactuated multi-rope cranes...][research_lu_fang_2018]
- [Providing Flight-Path Control Bandwidth for Carrier Landings][research_hess_2018]
- [Reduced-order model for robust aeroelastic control][research_bruderlin_hosters_2018]
- [Robust Finite-Time Continuous Control of an Unsteady...][research_lee_singh_2018]
- [Stability of Very Flexible Aircraft with Coupled Nonlinear...][research_changchuan_lan_2018]
- [Tentacle-Based Guidance for Entry Flight with No-Fly Zone...][research_liang_ren_2018]
- [A Physically Consistent Reduced Order Model for Plasma...][research_motta_malzacher_2019]
- [Abbott Alinity Control Module Software][research_abbott_alinity_2019]
- [Aeroelastic Stability Analysis of Damaged High-Aspect-Ratio...][research_hoseini_hodges_2019]
- [Chaos control of nonlinear aeroelastic pitch plunge model][research_rao_padmanabhan_2019]
- [Design and Flight Evaluation of Primary Control System for...][research_lavretsky_2019]
- [Disturbance rejection control of morphing aircraft based on...][research_gong_wang_2019]
- [Dynamic Contraction Method approach to digital longitudinal...][research_czyba_stajer_2019]
- [Dynamic Distributed Morphing Control of an Aeroelastic Wing...][research_zhang_wang_2019]
- [Effect of Aerodynamic Configuration Parameters on...][research_pan_huang_2019]
- [Neural-sliding mode approach-based adaptive estimation...][research_taimoor_aijun_2019]
- [Nonlinear 3D path following control of a fixed-wing aircraft...][research_galffy_bock_2019]
- [Probabilistic Flight Envelope Estimation with Application to...][research_yin_chu_2019]
- [Robustness Analysis of Flight Controllers for Fixed-Wing...][research_palframan_fry_2019]
- [Transient Aeroelastic Response Control of Shipboard Rotors...][research_han_yu_2019]
- [Automatic Control and Model Verification for a Small...][research_guo_zhou_2020]
- [Control Authority of a Camber Morphing Flying Wing][research_keidel_fasel_2020]
- [Dynamic Stability Analysis of Aircraft Flight in Deep Stall][research_cunis_condomines_2020]
- [Flight Control Design for the Systematic Improvement of Ride...][research_rath_fichter_2020]
- [Flight Control for Very Flexible Aircraft Using Model-Free...][research_qi_zhao_2020]
- [Handling-Qualities Perspective on Rotorcraft Load Alleviation...][research_saetti_horn_2020]
- [Improved fault diagnosis for aircraft flap control system...][research_chen_jing_2020]
- [Loop-Separation Control for Very Flexible Aircraft][research_gonzalez_silvestre_2020]
- [Low-complexity hypersonic flight control with asymmetric...][research_an_guo_2020]
- [Modeling and Control Design of an Autonomous Hybrid...][research_abdalla_mansor_2020]
- [Revisiting the Fundamentals of Control Surface Reversal...][research_bueno_dowell_2020]
- [Sum-of-Squares Flight Control Synthesis for Deep-Stall...][research_cunis_condomines_2020_b]
- [Timing precision in fly flight control integrating...][research_dickerson_2020]
- [A Nonlinear Optimal Control Approach for the Vertical...][research_rigatos_2021]
- [High Control Authority Three-Dimensional Aircraft Control...][research_xu_zha_2021]
- [Nonlinear Aeroelastic Simulations and Stability Analysis of...][research_hilger_ritter_2021]
- [Phase plane design based fast altitude tracking control for...][research_liu_dong_2021]
- [Pose and shape error control in automated machining of...][research_mei_wang_2021]
- [RELIABILITY OF EC 155 B1 AIRCRAFT COMPONENTS USING UPPER...][research_mahroni_2021]
- [Robust Nonlinear Tracking Control for Unmanned Aircraft in...][research_kazarin_golubev_2021]
- [6DOF nonlinear control loading system for a large transport...][research_amirahmadichomachar_kuppusamy_2022]
- [Active Flow Control Devices for Wing Load Alleviation][research_khalil_asaro_2022]
- [Adaptive Sampling for Interpolation of Reduced-Order...][research_goizueta_wynn_2022]
- [Aeroelasticity of Flying-Wing Aircraft Subject to Morphing A...][research_syed_moshtaghzadeh_2022]
- [Aircraft flight control using method of robustness aimed at...][research_wang_zheng_2022]
- [Amplitude Control of Stall-Induced Nonlinear Aeroelastic...][research_liu_sun_2022]
- [Analisis Umur Fatik Rangka Penyangga Aileron Flight Control...][research_kurniawan_2022]
- [Beyond Persistent Excitation Online Experiment Design for...][research_vanwaarde_2022]
- [Central bank digital currency and flight to safety][research_williamson_2022]
- [Characteristics analysis and drive type selection for aileron...][research_radetskaya_2022]
- [Control of Hybrid Transitioning Morphing-wing VTOL UAV][research_patel_kumar_2022]
- [Discussion of “Central bank digital currency and flight to...][research_carapella_2022]
- [Dynamics and anti-disturbance control for tethered aircraft...][research_song_huang_2022]
- [In-Wing Pressure Measurements for Airspeed and Airflow Angle...][research_heinrich_vogt_2022]
- [Incremental Dual Heuristic Dynamic Programming Based Hybrid...][research_li_sun_2022]
- [Linear and Nonlinear Reduced Order Models for Sloshing for...][research_pizzoli_saltari_2022]
- [Nonlinear Control of Aircraft Flight Dynamics Using...][research_tran_nguyen_2022]
- [The Construction of an Aircraft Control Multilayer Network...][research_ren_zhang_2022]
- [Adaptive nonsingular fixed‐time control for hypersonic flight...][research_dong_li_2023]
- [Carrier Aircraft Flight Controller Design by Synthesizing...][research_jia_sun_2023]
- [Control of Deflection Angle of Morphing Wing Using Fuzzy...][research_bataineh_shawabkeh_2023]
- [Cross-Condition Fault Diagnosis of an Aircraft Environmental...][research_jia_ezhilarasu_2023]
- [Decentralized active damping control for aeroelastic morphing...][research_svoboda_hengstermovric_2023]
- [Development of an Active Wingtip for Aeroelastic Control][research_toffol_ricci_2023]
- [Food safety management system certification - the...][research_food_safety_2023]
- [Gust alleviation by spanwise load control applied on a...][research_klug_ullah_2023]
- [Loss of control in flight accident case study icing-related...][research_bromfield_horri_2023]
- [Plasma Gurney Flap Flight Control at Low Angle of Attack][research_gu_ducvo_2023]
- [Scaling of sense organs that control flight Size and sensory...][research_simmons_2023]
- [The aerodynamic force estimation of a swept-wing UAV using...][research_uzun_bilgic_2023]
- [UAV control with active disturbance suppression for the...][research_uav_control_2023]
- [Aerodynamic Assessment of a Control Strategy Based on Twist...][research_karimikelayeh_djavareshkian_2024]
- [Aerodynamic Feedforward-Feedback Architecture for Tailsitter...][research_mcintosh_mishra_2024]
- [Aeroelastic vibrations control system of an unmanned aircraft][research_bondarenko_shkolnyi_2024]
- [Control System Design][research_kamaletdinova_romanov_2024]
- [Data‐based nonlinear learning control for aircraft trajectory...][research_wei_meng_2024]
- [Dual Loop PI m PI n Control for an Aileron Positioning][research_degaspari_mantegazza_2024]
- [Geometrically Exact Aeroelastic Stability Analysis of...][research_shang_xia_2024]
- [Individual Blade Control Approach for Active Vibration...][research_hong_kim_2024]
- [Passive Aeroelastic Control of a Near-Ground Airfoil with a...][research_dhital_chouvion_2024]
- [Reducing flight risks through wildlife control John F...][research_uzun_2024_b]
- [Robust Aeroelastic Response Estimation for Flexible Aircraft][research_mahapatra_halbe_2024]
- [The Coupled Wing Morphing of Ornithopters Improves Attitude...][research_cai_su_2024]
- [Visualization and control of the free-flight transfer...][research_maruyama_ogino_2024]
- [Composite Actuation and Adaptive Control for Hypersonic...][research_wei_cui_2025]
- [Control Characteristics Analysis of Multi-Section Morphing...][research_ma_zhou_2025]
- [Control of wing aeroelastic system in presence of wind gust...][research_mahmood_2025]
- [Dynamic integral sliding mode control for nonminimum phase...][research_wang_zhang_2025]
- [Event-Triggered Formation Control for High-Speed Flight...][research_li_li_2025]
- [Flight Control Design for Rudder Failure Event on Cessna 172...][research_zuhri_2025]
- [Flow Control Devices for Aeroacoustic Noise Suppression in...][research_lee_lua_2025]
- [Latency Control in Real-Time Advertising Recommendation under...][research_latency_control_2025]
- [Optimal Control of a Small Flexible Aircraft Using an Active...][research_wu_fu_2025]
- [RETRACTED ARTICLE Fractional-order fast terminal sliding mode...][research_xu_2025]
- [Research on Aircraft Control System Fault Risk Assessment...][research_shi_gao_2025]
- [Research on aerodynamic design and anti-crosswind...][research_xie_wang_2025]
- [Robustness analysis of nonlinear filters for aircraft state...][research_elenchezhiyan_kumar_2025]
- [Soaring to New Heights Investigating the Aeroelastic...][research_smith_2025]
- [The SpHelico A coaxial drone inside a gimbal system...][research_flores_bazan_2025]
- [The usefulness of viscosity for the robustness of boundary...][research_bastin_coron_2025]
- [A neural connectivity atlas for fly flight control][research_dhawan_huang_2026]
- [Active Flow Control for Enhanced High-Lift Aileron...][research_shmilovich_yadlin_2026]
- [Adaptive nonlinear aircraft pitch control via LS-SDRE][research_le_2026]
- [Aerodynamic Configuration and Stability Analysis of a...][research_li_shen_2026]
- [Combined Flow Control Method for Supersonic Jet Noise...][research_kabaliswaran_das_2026]
- [Distributed Formation Control Method with Hierarchical Leader...][research_choi_choi_2026]
- [Efficacy of Active Flow Control in Suppression of Wing Rock...][research_tahir_maqsood_2026]
- [Flight Safety Control and Test Flight Experiments under...][research_zhou_gong_2026]
- [Modeling and Integrated Control Design for Folding-Wing...][research_wang_2026]
- [Neural Learning Control of Fighter Aircraft at...][research_yu_yu_2026]
- [Nonlinear geometric multivariable control for unmanned...][research_jianhong_yanxiang_2026]
- [Pneumatic-Based Approach for Flight Control][research_shmilovich_princen_2026]
- [Retraction Note Fractional-order fast terminal sliding mode...][research_xu_2026]
- [Study, Design, Modeling, Simulation, and Control Analysis of...][research_shneen_2026]
- [Three-Dimensional Guidance Law with LOS Angle and Attack Lead...][research_niu_li_2026]
- [Time-Varying Aerodynamic Model and Adaptive Control of the...][research_peng_cao_2026]

- [A Study on Fly-By-Wire Helicopter Control Law Design using...][research_kim_choi_2015]
- [AIRCRAFT CONTROL LAW RECONFIGURATION][research_kosyanchuk_selvesyuk_2015]
- [Actuator fault-tolerant control FTC design with post-fault...][research_chakravarty_mahanta_2015]
- [Autonomous Formation Flight Control System Using In-Flight...][research_brodecki_subbarao_2015]
- [DESIGN OF FLY-BY-WIRE CONTROL SYSTEM ALGORITHMS FOR ADVANCED...][research_anikin_animitsa_2015]
- [Fault Tolerance System running on Distributed Multimedia][research_hong_ko_2015]
- [Learning Control Law of Mode Switching for Hypersonic...][research_jiao_jiang_2015]
- [SELECTION METHOD OF MONITORING ALGORITHM THRESHOLDS FOR...][research_bazhenov_lysenkova_2015]
- [The control law of the available energy of the aircraft for...][research_anon_2015]
- [A Novel Approach for Fault Tolerance Control System and...][research_khadse_karmore_2016]
- [Control computers diagnostics for UAV flight control system][research_kopecki_2016]
- [DESIGN OF INTEGRAL CONTROL ALGORITHMS FOR FLY-BY-WIRE CONTROL...][research_kuvshinov_2016]
- [DESIGN OF INTEGRAL CONTROL ALGORITHMS FOR THE LATERAL CHANNEL...][research_kuvshinov_2016_b]
- [Explicit robustness and fragility margins for linear discrete...][research_nguyen_olaru_2016]
- [Fault tolerant control design using adaptive control...][research_tohidi_khakisedigh_2016]
- [Flight Control Law Clearance Using Optimal Control Theory][research_herrmann_benasher_2016]
- [Flight Control Software Failure Mitigation Design...][research_morozov_janschek_2016]
- [Flight Control System Modeling with SysML to Support...][research_mhenni_choley_2016]
- [Flight Envelope Load Factor Limit Logic Design for Helicopter...][research_choi_2016]
- [Fly-by-wire robustness to flight dynamics change under...][research_dlamini_jones_2016]
- [Real-Time Reliability Verification for UAV Flight Control...][research_xu_wang_2016]
- [Receptance-Based Active Aeroelastic Control with Embedded...][research_singh_brown_2016]
- [SKF divests fly-by-wire business][research_skf_divests_2016]
- [Tracking Control Based on Control Allocation with an...][research_dong_lu_2016]
- [Fault-Tolerant Certifiable Control for a V-Tail Remotely...][research_garciahernandez_cuernorejado_2017]
- [Higher-order Iterative Learning Control Law Design using...][research_wang_chu_2017]
- [Influence of flight control law on spin dynamics of...][research_malik_akhtar_2017]
- [Intelligent Flight Control System Design for the Small UAV...][research_komnatska_bondarenko_2017]
- [Supervisory adaptive fault‐tolerant control against actuator...][research_ouyang_lin_2017]
- [Adaptive fault‐tolerant control for a nonlinear flexible...][research_zhang_liu_2018]
- [An improved NSGA-II based control allocation optimisation for...][research_bian_nener_2018]
- [FLIGHT CONTROL SYSTEM NETWORK ARCHITECTURE DESIGN AND...][research_bai_2018]
- [Flight test of fault-tolerant flight control system using...][research_matsuki_nishiyama_2018]
- [IMITATION MODELING OF THE RECOVERY PROCESS OF THE ON-BOARD...][research_zelenkov_2018]
- [Integral sliding mode fault‐tolerant control allocation for a...][research_chen_edwards_2018]
- [Smart Integrated Optical Rotation Sensor Incorporating a...][research_tameh_sawan_2018]
- [Static output feedback fault tolerant control using control...][research_argha_su_2018]
- [The development requirement and design considerations for...][research_shi_tan_2018]
- [A Modified NSGA-II for Solving Control Allocation...][research_bian_nener_2019]
- [Adaptive Closed-Loop Control Allocation-Based Fault Tolerant...][research_lu_ma_2019]
- [CONTROL LAW FOR AN AIRCRAFT SUPERSONIC AIR INLET WITH...][research_tudosie_dumitru_2019]
- [DESIGN OF FLY-BY-WIRE CONTROL SYSTEM ALGORITHMS FOR...][research_kuvshinov_leontiev_2019]
- [Flight control system Design of unmanned fixed wing aircraft...][research_sugino_harada_2019]
- [High-Bandwidth Morphing Actuator for Aeroelastic Model Control][research_fichera_isnardi_2019]
- [Modeling, Simulation and Control of a Fly-by-wire Flight...][research_fadel_rabie_2019]
- [Sliding‐mode fault‐tolerant control using the control...][research_argha_su_2019]
- [A New Method for Control Allocation of Aircraft Flight...][research_yang_gao_2020]
- [A Novel Control Allocation Method for Yaw Control of Tailless...][research_shearwood_nabawy_2020]
- [A Review of the Most Adopted Fault Tolerance Approaches for...][research_bouras_2020]
- [A Way to Mitigate Force-Fight Oscillation Based on Pressure...][research_xue_yao_2020]
- [Active Fault Tolerance Control Based on Consistent Matrix for...][research_mao_li_2020]
- [Active Fault-Tolerant Control Strategy for More Electric...][research_sun_wang_2020]
- [An Innovative Control Allocation Framework for a Novel...][research_xu_zhang_2020]
- [Event-based fault-tolerant control for networked control...][research_li_tang_2020]
- [Flying qualities evaluation based nonlinear flight control...][research_sun_shi_2020]
- [Research on Air Flight Simulation Control Law of Large...][research_you_2020]
- [Robust fault tolerant control allocation for a modern...][research_vile_alwi_2020]
- [Self-triggered sliding mode control for Digital Fly-by-Wire...][research_cao_jia_2020]
- [Three-axis coupled flight control law design for flying wing...][research_wang_zhang_2020]
- [A Software Verification Approach That Complies with DO-178B...][research_demir_seyfullahbabaarslan_2021]
- [Aircraft flight control system fault tolerance under...][research_kosyanchuk_zheltov_2021]
- [Business Jet Fly-by-Wire Control Laws Handling Qualities...][research_berger_tischler_2021]
- [Effect of Actuator Saturation on Pilot-Induced Oscillation A...][research_nguyen_lowenberg_2021]
- [Fault Analysis and Non-Redundant Fault Tolerance in 3-Level...][research_caseiro_mendes_2021]
- [Fault estimation and fault tolerance control for spacecraft...][research_gao_wang_2021]
- [Integrated design of fault-tolerant control for flight...][research_unal_2021]
- [Intelligent Fault-Tolerant Control for AC/DC Hybrid Power...][research_xiao_sattarov_2021]
- [ROBUSTNESS OF AIRCRAFT TURBOFAN ENGINE CLOSED-LOOP CONTROL...][research___2021]
- [Research on a Passenger Aircraft Flight Control System Gain...][research_guo_2021]
- [Research on the NealandSmith Criterion Application on...][research_guo_2021_b]
- [Time delay compensation in lateral-directional flight control...][research_shen_huang_2021]
- [\ \mathcal L _1 \ Adaptive Loss Fault Tolerance Control of...][research_li_shi_2021]
- [Application Analysis on Fly-by-Wire Flight Control System on...][research_application_analysis_2022]
- [Design and Application of Electromechanical Control System...][research_wei_2022]
- [Design of generalized fault diagnosis observer and active...][research_sun_han_2022]
- [Digital twin-based fault tolerance approach for Cyber...][research_saraeian_shirazi_2022]
- [Dynamic control allocation between onboard and delayed remote...][research_tabassum_bai_2022]
- [ESTIMATION OF FLY-BY-WIRE EMERGENCY SERVO-CONTROL OF REGIONAL...][research_terekhov_2022]
- [Fly-by-wire Flight Control Comparative Analysis of Resident...][research_shen_chang_2022]
- [Health management using fault detection and fault tolerant...][research_mahboub_rouabah_2022]
- [In-Flight Demonstration of Stall Improvement Using a Plasma...][research_sekimoto_kato_2022]
- [Research and Design of Automatic Flight Control System Test...][research_research_and_2022]
- [Simulation and experimental research on adaptive control...][research_zhang_shao_2022]
- [Development of Fault Tolerant Flight Control System For...][research_k_deodhare_2023]
- [Fault-Tolerant Attitude Control Incorporating Reconfiguration...][research_cong_hu_2023]
- [Flight Control Law for Stabilizing Transient Response of the...][research_ji_kim_2023]
- [Fly by Wire Advancements in Aviation over Conventional Flight...][research_pendem_2023]
- [Grouped Multilayer Practical Byzantine Fault Tolerance...][research_liu_feng_2023]
- [Hybrid Adaptive Control for Tiltrotor Aircraft Flight Control...][research_wen_song_2023]
- [Methodology for Preliminary Flight Control Actuator Design][research_stephan_stumpf_2023]
- [Minimum Power Control Allocation for Incremental Control of...][research_pfeifle_fichter_2023]
- [Research on Dynamic Characteristics Analysis and Control Law...][research_tai_wang_2023]
- [Simultaneous UAV having actively sweep angle morphing wing...][research_uzun_oktay_2023]
- [Active Flutter Suppression Quantification of Performance Loss...][research_micheli_2024]
- [Design, modeling and optimal control of a novel compliant...][research_sun_xu_2024]
- [Flight control system design of UAV with wing incidence angle...][research_uzun_2024]
- [Markov multi-fault tolerance control of intelligent...][research_wang_sun_2024_b]
- [Method of Control System Fault Tolerance Based on Full or...][research_zhirabok_filaretov_2024]
- [Minimum-Drag Fault-Tolerant Aircraft Control Allocation via...][research_antonakis_biannic_2024]
- [Rack force fault tolerance estimation of steer-by-wire system...][research_zhao_zhao_2024]
- [Retracted Design and Application of Electromechanical Control...][research_robotics_2024]
- [A Method for PIO Suppression in Aircraft with Fly-By-Wire...][research_miranda_bidinotto_2025]
- [Active Fault-tolerant Control of Parallel Digital Valves and...][research_active_fault_tolerant_2025]
- [Aerodynamic Analysis and Application of the Channel Wing...][research_cao_liu_2025]
- [Control allocation design for equal control sensitivity of...][research_wang_li_2025]
- [Dynamic Control Allocation for Nonlinear Systems via a...][research_akbari_galeani_2025]
- [Dynamic load alleviation of input-redundant flexible aircraft...][research_dong_zhou_2025]
- [Energy Configuration Design and Configuration Scheme of...][research_qian_xinhui_2025]
- [Fault Detection and Fault-Tolerant Control Based on Bi-LSTM...][research_li_shang_2025]
- [INDI Application in Flight Control Law Design of Civil...][research_li_xiong_2025]
- [Intelligent fault tolerance control using long short-term...][research_elmahdy_ali_2025]
- [LITERATURE STUDY ON DESIGNING CONTROL LAW FOR CONVENTIONAL...][research_abdulrashid_syedmohddardin_2025]
- [Norm-Bounded Model Predictive Control Allocation Strategy for...][research_scordamaglia_mattei_2025]
- [Redundancy design and research of safety fly-by-wire flight...][research_wang_li_2025_b]
- [Research on a Safety-Critical Architecture of Large...][research_tang_tang_2025]
- [Research on control law of more-electric aircraft...][research_zheng_shao_2025]
- [Design of Intelligent Control Law Embedded With Dynamic Flow...][research_zhao_liu_2026_b]
- [Effectiveness and robustness of an independent flight control...][research_hubener_luckner_2026]
- [Electromechanical Flight-Control Actuation Systems for...][research_martinezheredia_fernandezprada_2026]
- [Fault Transmission Modeling and Non-Bypass Fault Tolerance...][research_yang_yu_2026]
- [First integration of triboelectric sensing into flight...][research_liu_wang_2026]
- [Passive Fault-Tolerant Control of Lifting-Wing Quadrotors...][research_chen_cai_2026]
- [Reduced-Order Nonlinear Dynamic Analysis and Lyapunov-Based...][research_jin_xue_2026]
- [Rigid Flexible Coupling Model-Driven Simulation of UAV...][research_shao_li_2026]
- [Safety Assessment and Fault Tolerance in eVTOL Aircraft...][research_han_pei_2026]
- [Structural Design Optimization of Bellcrank 3 in the N219...][research_hartini_bachtiar_2026]
- [Vehicle Sensor Steering System Control Based on Steering by...][research_vehicle_sensor_2026]

- [Robust kernel-based model reference adaptive control for...][research_yang_zhao_2016]
- [Stability Augmentation and Active Flutter Suppression of a...][research_schmidt_2016]
- [Active Control of Aeroelastic Vibrations for...][research_yoo_2017]
- [Comparison of the passive and active control gust alleviation...][research_liu_2018]
- [Active control of supersonic transport aeroelastic...][research_guruswamy_2019]
- [DESIGN OF ACTIVE CONTROL SYSTEM OF PASSENGER AIRCRAFT FOR...][research_kuvshinov_lazurin_2019]
- [Aeroelastic control of bridge using active control surfaces...][research_phan_2020]
- [Unstable Aircraft Parameter Estimation Using Neural Partial...][research_kuttieri_sinha_2023]
- [A Comparative Analysis of Active Control vs. Folding Wing Tip...][research_toffol_2024]
- [Two-Dimensional Static Margin for Three-Dimensional Aircraft][research_schmidt_lisoski_2025]
- [Dynamic performance analysis of attitude control for...][research_zhang_li_2026]
- [Flexible wingtip active control test and mechanism for gust...][research_zheng_dai_2026]

### Aeroservoelasticity became its own discipline

**The interaction the X-29 encountered in flight now has a name, a literature and a place in the design process.**
Structural modes inside the control bandwidth, notch filters that trade stability against delay, and the
fact that a delay bought to suppress a structural mode is a delay taken from an unstable airframe's budget.
**The X-29 had all three problems and met them one at a time in flight.**

- [Active gust load alleviation system for flexible aircraft...][research_alam_hromcik_2015]
- [Gust Load Alleviation for a Regional Aircraft Through a...][research_fonte_ricci_2015]
- [Rapid State Space Modeling Tool for Rectangular Wing...][research_suhpeterm_conyershowardjason_2015]
- [Aeroelastic scaling laws for gust load alleviation control...][research_tang_wu_2016]
- [Design and flight test of active flutter suppression on the...][research_burnett_beranek_2016]
- [Gust Load Alleviation with Robust Control for a Flexible Wing][research_liu_sun_2016]
- [Optimization of an Aeroservoelastic Wing with Distributed...][research_stanford_2016]
- [Prediction and Simulator Verification of Roll/Lateral Adverse...][research_muscarello_quaranta_2016]
- [Probabilistic Aeroservoelastic Reliability Assessment...][research_wu_livne_2016]
- [WITHDRAWN Robust aeroservoelastic design with mixed...][research_dai_wu_2016]
- [Aeroservoelastic modeling with proper orthogonal decomposition][research_carlson_verberg_2017]
- [Aeroservoelastic modelling and control of a slender anti-air...][research_verhaegen_zbikowski_2017]
- [Design of an Active Disturbance Rejection Control for...][research_yang_huang_2017]
- [Gust Load Alleviation Identification, Control, and Wind...][research_poussotvassal_demourant_2017]
- [Gust load alleviation wind tunnel tests of a...][research_bi_xie_2017]
- [Improved LQG Method for Active Gust Load Alleviation][research_liu_sun_2017]
- [LQG based model predictive control for gust load alleviation][research_liu_sun_2017_b]
- [Optimal Control Surface Layout for an Aeroservoelastic Wingbox][research_stanford_2017]
- [ACTIVE FLUTTER SUPPRESSION OF A HIGH ASPECT RATIO WING...][research_mamedov_paryshev_2018]
- [Adaptive Feedforward Compensating Self-Sensing Method for...][research_wang_xu_2018]
- [Aircraft Active Flutter Suppression State of the Art and...][research_livne_2018]
- [Attitude control synthesis of unstable hypersonic vehicle...][research_chen_yang_2018]
- [Delayed sub-optimal control for active flutter suppression of...][research_zhou_yu_2018]
- [Reentry attitude control for a reusable launch vehicle with...][research_mao_dou_2018]
- [Active flutter suppression non-structured and structured H∞...][research_waitman_marcos_2019]
- [Adaptive aeroservoelastic mode stabilization of flexible...][research_piao_zhang_2019]
- [Aeroservoelastic design of piezo-composite wings for gust...][research_liu_wang_2019]
- [Examples on increased-order aeroservoelastic modeling][research_reyes_climent_2019]
- [Flexible Aircraft Gust Load Alleviation with Incremental...][research_wang_vankampen_2019]
- [Gradient-Based Aeroservoelastic Optimization with Static...][research_stanford_2019]
- [Integrated optimization of control surface layout for gust...][research_pusch_knoblach_2019]
- [Optimization and control application of sensor placement in...][research_yang_yang_2019]
- [Parameterized Modeling Methodology for Efficient...][research_huang_yang_2019]
- [Transonic flutter suppression for a three-dimensional elastic...][research_yang_huang_2019]
- [A neural network approach for improving airfoil active...][research_tang_chen_2020]
- [Active Disturbance Rejection Control for Hypersonic Flutter...][research_chen_zhao_2020]
- [Airfoil gust load alleviation by circulation control][research_li_qin_2020]
- [An improved aeroservoelastic modeling approach for...][research_yue_zhao_2020]
- [Design and Optimization of an Aeroservoelastic Wind Tunnel...][research_dillinger_meddaikar_2020]
- [Gust Load Alleviation of Flexible Composite Wing][research_ibren_sulaeman_2020]
- [Gust load alleviation for flexible aircraft using...][research_khalil_fezans_2020]
- [H∞ Control Design for Active Flutter Suppression of...][research_waitman_marcos_2020]
- [Parametric active aeroelastic control of a morphing wing...][research_liu_gao_2020]
- [Robust Modal Damping Control for Active Flutter Suppression][research_theis_pfifer_2020]
- [Gust load alleviation by normal microjet][research_li_qin_2021_b]
- [Gust load alleviation on an aircraft wing by trailing edge...][research_li_qin_2021]
- [Modeling and Control Design for Flutter Suppression Using...][research_kassem_yang_2021]
- [A Review of Flow Control for Gust Load Alleviation][research_li_qin_2022]
- [Active Flutter Suppression of a Wing Section in a...][research_munoz_garciafogeda_2022]
- [Aeroservoelastic Characteristics of a Corrugated Morphing...][research_soneda_tsushima_2022]
- [Application of Structured Robust Synthesis for Flexible...][research_patartics_liptak_2022]
- [Composite Design of Disturbance Observer and Reentry Attitude...][research_yang_mao_2022]
- [Design of Gust Load Alleviation Control Based on UD-PSO for...][research_qu_li_2022]
- [Efficient Nonlinear Aeroservoelastic Modeling for Morphing...][research_huang_yu_2022]
- [Generalized Predictive Control for Active Flutter Suppression...][research_haley_soloway_2022]
- [Machine learning-based active flutter suppression for a...][research_mu_huang_2022]
- [Partial Feedback Linearized RISE Controller for Active...][research_sharma_agrawal_2022]
- [Robust Gust Load Alleviation of Flexible Aircraft Equipped...][research_fournier_massioni_2022]
- [Whirl Flutter Suppression of Tiltrotor Aircraft Using...][research_dong_li_2022]
- [Active Flutter Suppression for a T-Tail via Optimal Control][research_xiang_wang_2023]
- [Active flutter suppression for a flexible wing model with...][research_chen_shi_2023]
- [Active flutter suppression on a flexible wing via...][research_chen_shi_2023_b]
- [Adaptive Feed-Forward Control for Gust Load Alleviation on a...][research_zhang_zhao_2023]
- [Aeroservoelastic Wind Tunnel Evaluation of Preview H2 and H∞...][research_ting_mesbahi_2023]
- [Gust Load Alleviation Using Reduced-Order Aeroelastic Models...][research_desouza_vuillemin_2023]
- [Incremental Nonlinear Control for Aeroelastic Wing Load...][research_schildkamp_chang_2023]
- [Active Flutter Suppression of a Wing Section in the Subsonic...][research_munoz_garciafogeda_2024]
- [Active flutter suppression for an aircraft wing structure by...][research_sekhar_suresh_2024]
- [Active flutter suppression for light sport aircraft by a...][research_kratochvil_valenta_2024]
- [Boosted Incremental Nonlinear Dynamic Inversion for Flexible...][research_beyer_steen_2024]
- [Fluidic Flow Control Devices for Gust Load Alleviation][research_khalil_bauknecht_2024]
- [Gust Load Alleviation Control Strategies for Large Civil...][research_zhang_qiu_2024]
- [Gust load alleviation of a flexible flying wing with linear...][research_gao_liu_2024]
- [Linear Modeling of Doppler Wind Lidar Systems for Gust Load...][research_cavaliere_fezans_2024_b]
- [Toward Automated Gust Load Alleviation Control Design via...][research_cavaliere_fezans_2024]
- [Unsteady nonlinear lifting line model for active gust load...][research_beyer_ullah_2024]
- [Aerodynamic Nonlinear Modeling and Body-Freedom Flutter...][research_liu_zheng_2025]
- [Destabilize/Stabilize Approach to Experimental Active Flutter...][research_berg_ting_2025]
- [Edge computing aileron mechatronics using antiphase...][research_yin_huang_2025]
- [Event-Triggered Adaptive Dynamic Programming for an...][research_wang_sun_2025]
- [Experimental Active Flutter Suppression Control with Inertial...][research_szymanski_alstrom_2025]
- [Model predictive control of a flared folding wingtip for gust...][research_narimani_haddadpour_2025]
- [Robust Control Design for the Higher Harmonic Vibration...][research_im_kong_2025]
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
- [Rigid-elastic-coupled aeroservoelastic modeling and flight...][research_mu_huang_2026]
- [Transonic buffeting control via a nonlinear aeroservoelastic...][research_yang_zhang_2026]

### High angle of attack aerodynamics

The second X-29A was devoted to high angle of attack work, and vortex flow control was tested on it.
**Contemporary work has moved from characterising the flow to controlling it**, with active flow control,
and the computational methods that were merely supporting evidence for the X-29 now carry the prediction.

- [Flight Envelope Protection Control Based on Reference...][research_ye_chen_2015]
- [High angle of attack command generation technique and...][research_ma_guo_2015]
- [ANALYSIS OF SUBSONIC VORTEX FLOW OVER THE MODEL OF...][research_osipov_2016]
- [EFFECT OF END CONTROL PLUGS ON THE PERFORMANCE OF VORTEX TUBE...][research_gowd_2016]
- [Quadratic Optimal Control of Aerodynamic Vectored UAV at High...][research_manzoor_maqsood_2016]
- [CONTROL OF VORTEX FLOW OVER A MANEUVERABLE AIRCRAFT MODEL...][research_osipov_2017]
- [Comment on “Roll Control Using Only Synthetic Jet Actuators...][research_wei_chen_2017]
- [Efficient nonlinear reduced-order modeling for...][research_li_jin_2017]
- [Introduction to the Special Section on F-16XL Flight...][research_introduction_to_2017]
- [Robust control of post-stall pitching maneuver based on...][research_wu_chen_2017]
- [Roll Control Using Only Synthetic Jet Actuators at High Angle...][research_li_yang_2017]
- [A Spreadsheet Tool for the AERODAS Model for Calculating...][research_a_spreadsheet_2018]
- [Detached Eddy-Simulation of Delta-Wing Post-Stall Flow Control][research_buzica_biswanger_2018]
- [Stall cell formation over a post-stall airfoil effects of...][research_esfahani_webb_2018]
- [A feasibility review of SMC-MIMO based control architecture...][research_a_feasibility_2019]
- [Geometrically exact vortex lattice and panel methods in...][research_yang_xie_2019]
- [Minimum Parameters Learning-Based Dynamic Surface Control for...][research_shi_lyu_2019]
- [Static Aeroelastic Characteristics of Morphing Trailing-Edge...][research_mao_xie_2019]
- [Vortex flow on the wing of aircraft and flow control to...][research_mamonova_soudakov_2019]
- [Vortex-Sheet Representation of Leading-Edge Vortex Shedding...][research_hirato_shen_2019]
- [Experimental Investigation of the Flow Characteristics around...][research_ozkan_2020]
- [High angle of attack flight control based on switched...][research_wu_chen_2020]
- [Post-stall flight dynamics of commercial transport aircraft...][research_cen_li_2020]
- [A Model for Predicting Post-Stall Behavior of Axial...][research_a_model_2021]
- [Adaptive neural tracking control for high angle of attack...][research_wu_sun_2021]
- [Roll Control of Morphing Aircraft with Synthetic Jet...][research_li_wang_2021]
- [Self-excited flag vibrations produce post-stall flow control][research_tan_wang_2021]
- [Analysis of ridge ice induced unsteadiness flow under...][research_tan_zhang_2022]
- [Post-stall flow control with upstream flags][research_zhang_wang_2022_b]
- [Vortex breakdown characteristics of flying wing aircraft...][research_zhu_shi_2022]
- [Aeroelasticity Model for Highly Flexible Aircraft Based on...][research_dagilis_kilikevicius_2023]
- [METHODOLOGICAL PROPOSAL FOR THE SELECTION AND ANALYSIS OF THE...][research_recaluque_aguilartorres_2023]
- [Numerical Study of Geometrical Properties of Full-Span...][research_numerical_study_2023]
- [Extended State Observer Based Generalized Predictive Control...][research_liu_ji_2024]
- [Flow Separation Control of an Airfoil by Using External Fluid...][research_dodayav_biswas_2024]
- [Enhanced Synchrosqueezing Transform for Detecting...][research_bagherzadeh_mohammadkarimi_2025]
- [Integrated flow control of adaptive cycle engine under high...][research_wang_chen_2025]
- [Lift Recovery in Post-Stall Region][research_dawe_bull_2025]
- [Robust intelligent control of aircraft at high angle of...][research_yang_wang_2025]
- [Design and Wind Tunnel Test of Control Laws for High Angle of...][research_wang_li_2026]
- [On-Board Flow Sensing for Forebody Vortex-Induced Yaw at High...][research_huang_li_2026]
- [Using the LSTM Network for Gray-Box Dynamic Identification of...][research_bagherzadeh_2026]

- [Parameter Estimation from Near Stall Flight Data using...][research_saderla_dhayalan_2016]
- [Aeroelastic Modeling of X-56A Stiff-Wing Configuration Flight...][research_grauerjareda_bouchermatthewj_2017]
- [Aeroelastic Stability Analysis of a Wind Tunnel Wing Model...][research_rea_pecora_2017]
- [Aeroelastic Stability Analysis of a Wind Tunnel Wing Model...][research_rea_pecora_2018]
- [Best Practices for Training the Structures Flight Test...][research_hashiiwendyn_thompsonrandolphc_2018]
- [Gust Alleviation Control using Prior Gust Information Wind...][research_hamada_saitoh_2019]
- [A Data-Driven Approach to Identify Flight Test Data Suitable...][research_lerro_brandl_2020]
- [Acquisition of Swept Aerodynamic Data by the Consecutive...][research_wakimoto_chiba_2021]
- [Sensing, Actuation, and Control of the SmartX Prototype...][research_nazeer_wang_2021]
- [Control Design and Flight Test of Aerodynamics-Driven...][research_feng_guo_2023]
- [Dynamic Structural Scaling Concept for a Delta Wing Wind...][research_bantscheff_breitsamter_2023]
- [Robust Stall Spin Flight Path Control with Flight Test...][research_hopwood_gresham_2023]
- [Unstable tilt-rotor maximum likelihood wavelet-based...][research_lichota_2023]
- [Research and application of wing load behavior in stall...][research_meng_jiang_2025]

### Composite structures and how they are certified

**The X-29's wing skins were an early large primary composite structure on a research aircraft**, and the
record's remark that strain-gauge equation accuracies on composite were typical of experience with metal is
a small early data point in a large modern subject.

- [Weight and mechanical performance optimization of blended...][research_liu_toropov_2015]
- [Cost efficiency, integration and assembly of a generic...][research_hagnell_langbeck_2016]
- [Aeroelastic passive control optimization of supersonic...][research_sulaeman_abdullah_2017]
- [Damage resistance of a co-cured composite wing box to...][research_yu_fang_2017]
- [Manufacturing of a composite wing with internal structure in...][research_patterson_grenestedt_2018]
- [Modelling, simulation and experimental validation of bend...][research_klasztorny_nycz_2018]
- [Mould design for manufacturing of isogrid structures in...][research_bellini_sorrentino_2018]
- [Application of structural health monitoring techniques to...][research_romano_ciminello_2019]
- [Manufacturing Spar I Beam Profile of UAV Wing Structure Made...][research_iryani_kadir_2019]
- [Potential Weight Benefits of IM7/8552 Hybrid Thin-Ply...][research_lovejoyandrewe_scottistephenj_2019]
- [Structural similitude design for a scaled composite wing box...][research_you_yasaee_2019]
- [Thermo-structural design of a Ceramic Matrix Composite wing...][research_ferraiuolo_scigliano_2019]
- [Aeroelastic and local buckling optimisation of a...][research_wang_wan_2021]
- [Composite wing structure of light amphibious airplane design...][research_chinvorarat_2021]
- [Failure modeling of composite wing leading edge under bird...][research_long_mu_2021]
- [A Reduced Order Model based on Artificial Neural Networks for...][research_torregrosa_gil_2022]
- [Modeling, analysis and validation of the structural response...][research_kilimtzidis_giannaros_2023]
- [Optimally stacked hygrothermally stable composite laminate...][research_kumarshakya_sekharpadhee_2023]
- [Analytical Assessment of Composite L Angle Strength Under...][research_kcs_james_2024]
- [Buckling optimization of variable stiffness composite wing...][research_huang_wang_2024]
- [Effects of Coupled Thickness Variation on the Aeroelastic...][research_leitch_stodieck_2024]
- [Performance Evaluation of Structural Health Monitoring System...][research_galasso_ciminello_2024]
- [Aeroelastic Coupled Mode Behavior of Swept Composite Wing][research_elshazly_kassem_2025]
- [Data-driven failure criteria prediction in composite wing...][research_magliacano_tufano_2025]
- [Nonlinear aeroelastic analysis of a skew reinforced composite...][research_vilela_donadon_2025]
- [The influence of coupled thickness variation in the...][research_leitch_stodieck_2025]
- [Physics-guided machine learning for the failure prediction of...][research_li_miranda_2026]

### Transonic wing design is computed now

**The Grumman K Mod 2 section was developed for a design competition and refined in tunnels.** Its modern
equivalent is produced by optimisation against a computational model, and the shock position that the X-29's
planform argument was built around is now an output rather than an input.

- [Aerodynamic Load Analysis of a Variable Camber Continuous...][research_tingeric_daotung_2015]
- [DLR natural and hybrid transonic laminar wing design...][research_streit_wedler_2015]
- [Development of Variable Camber Continuous Trailing Edge Flap...][research_nguyennhan_kaulupender_2015]
- [Aerodynamic Modeling of Transonic Aircraft Using Vortex...][research_chaparrodaniel_fujiwaragustavoec_2016]
- [Comparison of Passive Flow Control Methods for a Cavity in...][research_saddington_thangamani_2016]
- [Experimental study of transonic buffet phenomenon on a 3D...][research_dandois_2016]
- [Influence of the number and location of design parameters in...][research_andresperez_gonzalezjuarez_2016]
- [Planform Dependency on Airfoil Design Results for Supersonic...][research_kishi_kanazaki_2016]
- [High-Angle-of-Attack F-16XL Flight Simulations at Sub- and...][research_hitzel_2017]
- [NUMERICAL 3D TRANSONIC FLOW SIMULATION OVER A WING][research_velkova_2017]
- [Design of a transonic wing with an adaptive morphing trailing...][research_burdette_martins_2018]
- [Influence of flexibility on the steady aeroelastic behavior...][research_schewe_mai_2018]
- [A methodology for simulating 2D shock-induced dynamic stall...][research_aljaburi_feszty_2019]
- [Performance Enhancement of the Flexible Transonic...][research_bartelsroberte_stanfordbretk_2019]
- [Transonic Airfoil Design and Optimization for an Unmanned Air...][research_kasimbiber_trentonwhite_2019]
- [Transonic static aeroelastic and longitudinal aerodynamic...][research_wang_2019]
- [Aerostructural Design Exploration of a Wing in Transonic Flow][research_bons_martins_2020]
- [Identification of nonlinear aerodynamic systems with...][research_liu_gao_2020_b]
- [Subsonic Ultra Green Aircraft Research Phase III Mach 0.75...][research_christopherkdroney_anthonyjsclafani_2020]
- [Design Optimization of a Dual-Bleeding Recirculation Channel...][research_vuong_kim_2021]
- [Structural and Aeroelastic Studies of Wing Model with Metal...][research_tsushima_saitoh_2021]
- [Subcritical and supercritical nonlinear aeroelastic behavior...][research_zhou_huang_2021]
- [Aerodynamic Data-Driven Surrogate-Assisted...][research_wu_zuo_2022]
- [Aerodynamic Design Optimization of a Transonic...][research_chau_zingg_2022]
- [Comparison of Computational Predictions of the Mach 0.80...][research_sallyaviken_craigahunter_2022]
- [IMPLEMENTATION OF TRANSONIC AREA RULE AND SWEPT BACK DELTA...][research_singh_dwivedi_2022]
- [Numerical Simulation Research on Static Aeroelastic Effect of...][research_guo_zhang_2022]
- [OPTIMIZATION OF WING PROFILE IN TRANSONIC FLOW][research_pham_2022]
- [Aerodynamic Optimization and Fuel Burn Evaluation of a...][research_chau_zingg_2023]
- [Comparative study of recent metaheuristics for solving a...][research_wansasueb_panagant_2023]
- [Fast Inverse Design of Transonic Airfoils by Combining Deep...][research_deng_yi_2023]
- [High-fidelity aeroelastic transonic analysis using...][research_grifo_gulizzi_2023]
- [Passive Transonic Shock Control on Bump Flow for Wing Buffet...][research_dipasquale_prince_2023]
- [Resolvent analysis of a finite wing in transonic flow][research_houtman_timme_2023]
- [Study on Optimization Design of Airfoil Transonic Buffet with...][research_chen_gao_2023]
- [Design Optimization of Blade Tip in Subsonic and Transonic...][research_duan_he_2024]
- [Design of Hybrid-Laminar-Flow-Control Wing and Suction System...][research_prasannakumar_sudhi_2024]
- [Determination of the features of integrated design of civil...][research_pelykh_andryushchenko_2024]
- [Effects of structural geometric nonlinearities on the...][research_ye_yang_2024]
- [INVESTIGATION OF AERODYNAMIC CHARACTERISTICS OF SWEPT C-WING...][research_samputh_moey_2024]
- [Improving transonic performance with adjoint-based NACA 0012...][research_ntantis_xezonakis_2024]
- [A Comparison of Modern Metaheuristics for Multi-Objective...][research_phuekpan_khammee_2025]
- [Design and aerodynamic analysis of a morphing joined-wing...][research_guo_wang_2025]
- [Transonic Aerodynamic Performance Analysis of a CRM...][research_hanman_yao_2025]
- [Transonic aeroelasticity design method with application to a...][research_zhong_ying_2025]
- [Aerodynamic Optimization of a Cruise-Slotted Transonic...][research_chau_piotrowski_2026]
- [Aeroelastic Reduced-Order Model Differential Equations in...][research_candon_marzocca_2026]
- [Range-Based Problem with Varying Design Point for Transonic...][research_poole_allen_2026]
- [SuperWing a comprehensive transonic wing dataset for...][research_yang_tang_2026]
- [Transonic aeroelastic stability analysis of launch vehicles...][research_shi_gao_2026]
- [Transonic deep stall of a free-to-pitch rigid wing][research_currao_jiang_2026]

- [C2 Approach Agility, Autonomy Briefing Charts][research_alberts_conley_2015]
- [Pitfalls of the Past Learning Disabilities That Hinder...][research_bardo_2015]
- [An artificial neural network approach for aerodynamic...][research_tao_sun_2016]
- [Improved control performance of the 3‐DoF aeroelastic wing...][research_szollosi_baranyi_2016]
- [A novel metal-composite joint and its structural performance][research_tang_liu_2018]
- [Effectiveness of Twist Morphing Wing on Aerodynamic...][research_kaygan_ulusoy_2018]
- [Unmanned aircraft automatic flight control algorithm in loop...][research_rogalski_2018]
- [Energy Harvesting Performance of a Wing Panel for Aeroelastic...][research_shan_tian_2019]
- [Improving Autonomous Performance of a Passive Morphing Fixed...][research_coban_2020]
- [A Case Study on the Software Test Criteria Derivation Related...][research_baek_2021]
- [Buckling performance of curvilinearly grid-stiffened...][research_alhajahmad_mittelstedt_2021]
- [DESIGN, PERFORMANCE ANALYSIS OF WING, AND MANUFACTURING OF...][research_daspatel_kumarkaruparthi_2021]
- [Seamless Active Morphing Wing Simultaneous Gust and Maneuver...][research_wang_mkhoyan_2021]
- [Structural performance of composite tidal turbine blades][research_gonabadi_oila_2021]
- [Aeroelastic Optimization of the High Aspect Ratio Wing with...][research_ghalandari_mahariq_2022]
- [Enhancement of aeroelastic performance of a smart delaminated...][research_varun_mondal_2022]
- [Structural design and mechanical performance of composite...][research_zia_liu_2022]
- [Study on Effect of Aerodynamic Configuration on Aerodynamic...][research_li_yuan_2022]
- [Compressor and Valve Control Performance Implications on...][research_mansy_faruque_2023]
- [Influence of structural features in the performance of...][research_rosa_pouca_2023]
- [Mechanical, thermogravimetric, and dynamic mechanical...][research_olhan_behera_2023]
- [Multidisciplinary Performance Enhancement on a Fixed-wing...][research_eraslan_oktay_2023]
- [Robust backstepping control for maneuver aircraft based on...][research_shen_chen_2023]
- [Bending performance of 3D printed ultra high-performance...][research_bai_guan_2024]
- [Enhanced Performance of Morphing Wing Through Composite...][research_sugumaran_2024]
- [Novel Twist Morphing Aileron and Winglet Design for UAS...][research_negahban_bashir_2024]
- [Aerodynamic Performance of Swayasa Aircraft Wing Model...][research_aerodynamic_performance_2025]
- [Multi-energy field composite manufacturing of...][research_qian_lu_2025]
- [Novel integrated aerodynamic configuration with ventral and...][research_sun_luo_2025]
- [Numerical Method for Aeroelastic Simulation of Flexible...][research_chen_he_2025]
- [Uncertainty qualification of aerodynamic performance of a...][research_xu_zhang_2025]
- [A novel multifunctional dimethyl adipate plasticizer for vat...][research_zhou_peng_2026]
- [Aerodynamic and Static Aeroelastic Analysis of a High-Agility...][research_reinbold_breitsamter_2026]
- [High-angle-of-attack maneuver flight control based on deep...][research_wang_weng_2026]
- [Longitudinal flight performance improvement strategy for...][research_wang_hu_2026]
- [Optimization of 3D printed grid-like ceramic composite...][research_hamza_akram_2026]
- [Parallelized complex method for multidisciplinary...][research_namanikoureh_shahverdi_2026]
- [Performance Evaluation of Thermoplastic Composite Propellers...][research_alam_lee_2026]

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
- [Handling Qualities of a Twin Ducted-Fan Aircraft An...][research_grant_stol_2015]
- [Application of Quantitative Measures for Analysing Aircraft...][research_hebbar_pashilkar_2016]
- [Handling qualities evaluation of an automatic slung load...][research_nonnenmacher_jones_2016]
- [Improvement of handling qualities for the aircraft...][research_garkushenko_vinogradov_2016]
- [Use of Time-Frequency Representations for Interpreting...][research_tritschler_oconnor_2016]
- [Vision-based control for helicopter ship landing with...][research_truong_rakotomamonjy_2016]
- [“Fast Simulation” in Evaluating Pilot/Aircraft Performance...][research_hess_2016]
- [Handling Qualities Assessment of an Unmanned Aircraft Using...][research_kim_kunz_2017]
- [Inverse simulation system for evaluating handling qualities...][research_zhou_wang_2017]
- [Longitudinal Pilot-induced Oscillation Tendencies Prediction...][research_yin_wang_2017]
- [Pilot induced oscillation suppression controller design via...][research_tran_sakamoto_2017]
- [Development of a Multi-Directional Manoeuvre for Unified...][research_dussart_lone_2019]
- [Prediction of nonlinear pilot-induced oscillation using an...][research_xu_tan_2019]
- [Technical Measures Perspectives in Selection of Handling...][research_chowhan_arya_2019]
- [Advancements in Predictions of Flying Qualities...][research_efremov_efremov_2020]
- [Conceptual Design, Flying, and Handling Qualities Assessment...][research_humphreysjennings_lappas_2020]
- [Effect of Control System Augmentation on Handling Qualities...][research_theodore_malpica_2020]
- [SIMULATED PILOT-IN-THE-LOOP TESTING OF HANDLING QUALITIES OF...][research_portapas_cooke_2020]
- [Study on the Handling Qualities Enhancement of Fixed-wing...][research_lee_kim_2020]
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
- [PREDICTED LEVELS OF HANDLING QUALITIES OF KA-62 HELICOPTER...][research_kozhanov_suvorova_2022]
- [PROSPECTIVE MEANS FOR THE AIRCRAFT PILOT INDUCED OSCILLATION...][research_efremov_shcherbakov_2022]
- [Tiltrotor Flight Control Design and High-Speed Handling...][research_berger_blanken_2022]
- [Valve control of a hydraulically interconnected suspension...][research_jafari_mashadi_2022]
- [Approach to Aircraft Handling Qualities Prediction][research_lampton_klyde_2024]
- [Co-design of a multirotor UAV with robust control considering...][research_mabboux_pommierbudinger_2024]
- [Handling Qualities Assessment and Discussion for Helicopter...][research_wang_chen_2024]
- [Handling Qualities sizing for aerial vehicles based on...][research_antonakis_2025]
- [Model Reference Control for Reducing Pilot-Induced...][research_newton_kroo_2025]
- [Modeling multirotor wake interference in quadrotor eVTOL...][research_wang_ji_2025]
- [Reinforcement-learning-based aircraft handling qualities...][research_antonakis_2025_b]
- [Euclid sUAV Handling Qualities Evaluation Through Flight...][research_ioannis_ioannis_2026]

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

**Period coverage, with counts alongside fractions because either alone misleads.**

| | Count | Fraction of cited research |
|---|---|---|
| Period, through 1995 | 1,130 | |
| Contemporary, 2015 onward | 850 | |

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
- The sweep trend of the divergence boundary, and that sweepback beyond about 47 degrees removes it
  entirely in this model.
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
- [053 Fuzzy logic control 1994][research_053_fuzzy_1994]
- [056 Neural networks in 1994][research_056_neural_1994]
- [196 Pointing control design 1994][research_196_pointing_1994]
- [214 Application of restructurable 1994][research_214_application_1994]
- [A feasibility review of 2019][research_a_feasibility_2019]
- [A Model for Predicting 2021][research_a_model_2021]
- [A Spreadsheet Tool for 2018][research_a_spreadsheet_2018]
- [A study of the 1973][research_a_study_1973]
- [Abbott Alinity Control Module 2019][research_abbott_alinity_2019]
- [Abbott, J. M. et al 1974][research_abbottjm_millerba_1974]
- [Abdalla et al 2020][research_abdalla_mansor_2020]
- [Abdel-Hady 1994][research_abdelhady_1994]
- [Abdul Rashid et al 2025][research_abdulrashid_syedmohddardin_2025]
- [Abed 2000][research_abed_2000]
- [Abed et al 2024][research_abed_alhamadani_2024]
- [Abel, I. et al 1966][research_abeli_ruhlincl_1966]
- [Abele and Sanlorenzo 1975][research_abele_sanlorenzo_1975]
- [Abele et al 1973][research_abele_ruger_1973]
- [Abelkis 1967][research_abelkis_1967]
- [Aberdeen Test Center Md 2009][research_aberdeentestcentermd_2009]
- [Abichandani and Rosenberg 1952][research_abichandani_rosenberg_1952]
- [Accelerated development and flight 1979][research_accelerated_development_1979]
- [Acoustic emission monitors damage 1981][research_acoustic_emission_1981]
- [Acoustic emissions and transient 1989][research_acoustic_emissions_1989]
- [Active Fault-tolerant Control of 2025][research_active_fault_tolerant_2025]
- [Adams 1973][research_adams_1973]
- [Adams 1977][research_adams_1977]
- [Adams and Hatch 1971][research_adams_hatch_1971]
- [Adeyemi et al 2026][research_adeyemi_bull_2026]
- [Adney, P. S. and Horn, W. J. 1984][research_adneyps_hornwj_1984]
- [Aero structural optimization for 2018][research_aero_structural_2018]
- [Aerodynamic Performance of Swayasa 2025][research_aerodynamic_performance_2025]
- [Agrell and Elmeland 1985][research_agrell_elmeland_1985]
- [Aguilar-Ibañez 2016][research_aguilaribanez_2016]
- [Agwa 2019][research_agwa_2019]
- [AHarrah, Ralph C. 2007][research_aharrahralphc_2007]
- [Ahmadi and Farsadi 2024][research_ahmadi_farsadi_2024]
- [Aidala 1985][research_aidala_1985]
- [Air Force Flight Test Center Edwards Afb Ca 1970][research_airforceflighttestcenteredwardsafbca_1970]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]
- [Air Force Flight Test Center Edwards Afb Ca 2002][research_airforceflighttestcenteredwardsafbca_2002]
- [Air Force Flight Test Center Edwards Afb Ca 2002][research_airforceflighttestcenteredwardsafbca_2002_b]
- [Air Force Test Pilot School Edwards Afb Ca 1969][research_airforcetestpilotschooledwardsafbca_1969]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]
- [Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_c]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_d]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_e]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]
- [Air Force Test Pilot School Edwards Afb Ca 1992][research_airforcetestpilotschooledwardsafbca_1992]
- [Air Force Test Pilot School Edwards Afb Ca 1993][research_airforcetestpilotschooledwardsafbca_1993]
- [Akbari et al 2025][research_akbari_galeani_2025]
- [Al-Jaburi et al 2019][research_aljaburi_feszty_2019]
- [Alag and Kaufman 1975][research_alag_kaufman_1975]
- [Alam and Lee 2026][research_alam_lee_2026]
- [Alam et al 2015][research_alam_hromcik_2015]
- [Albachten 1956][research_albachten_1956]
- [Alberts 2011][research_alberts_2011]
- [Alberts 2014][research_alberts_2014]
- [Alberts and Conley 2015][research_alberts_conley_2015]
- [Alexander 1991][research_alexander_1991]
- [Alexander et al 1973][research_alexander_griffin_1973]
- [Alhajahmad and Mittelstedt 2021][research_alhajahmad_mittelstedt_2021]
- [Ali, Syed Firasat 1997][research_alisyedfirasat_1997]
- [Alim and Rizianiza 2021][research_alim_rizianiza_2021]
- [Allen et al 1983][research_allen_bradley_1983]
- [Allen et al 1984][research_allen_bradley_1984]
- [Allison, Dennis O. and Dagenhart, J. Ray 1987][research_allisondenniso_dagenhartjray_1987]
- [Almosnino 1985][research_almosnino_1985]
- [Alyanak and Pendleton 2017][research_alyanak_pendleton_2017]
- [Amin and Hollweger 1983][research_amin_hollweger_1983]
- [Amir Ahmadi Chomachar and Kuppusamy 2022][research_amirahmadichomachar_kuppusamy_2022]
- [An et al 2017][research_an_khoo_2017]
- [An et al 2020][research_an_guo_2020]
- [An et al 2026][research_an_zhang_2026]
- [Anderson 1961][research_anderson_1961]
- [Anderson 1968][research_anderson_1968]
- [Anderson 1985][research_anderson_1985]
- [Anderson et al 1973][research_anderson_berger_1973]
- [Anderson et al 1986][research_anderson_hogle_1986]
- [Anderson, C. A. 1976][research_andersonca_1976]
- [Andrés-Pérez et al 2016][research_andresperez_gonzalezjuarez_2016]
- [Anikin et al 2015][research_anikin_animitsa_2015]
- [Annadata et al 2024][research_annadata_endesfelder_2024]
- [Announcement European forum on 1988][research_announcement_european_1988]
- [Ansari et al 2023][research_ansari_zucco_2023]
- [Ansell, G. S. et al 1982][research_ansellgs_loewyrg_1982]
- [Antonakis 2025][research_antonakis_2025]
- [Antonakis 2025][research_antonakis_2025_b]
- [Antonakis and Biannic 2024][research_antonakis_biannic_2024]
- [Application Analysis on Fly-by-Wire 2022][research_application_analysis_2022]
- [Apu/hydraulic/actuator Subsystem Computer Simulation 1975][research_apu_hydraulic_actuator_subsystem_1975]
- [Arcidiacono et al 1970][research_arcidiacono_carta_1970]
- [Ardema, M. D. and Williams, L. J. 1972][research_ardemamd_williamslj_1972]
- [Argha et al 2018][research_argha_su_2018]
- [Argha et al 2019][research_argha_su_2019]
- [Armanious and Lind 2017][research_armanious_lind_2017]
- [Armstrong 1977][research_armstrong_1977]
- [Armstrong et al 2006][research_armstrong_lindberg_2006]
- [Arnold 1942][research_arnold_1942]
- [Asgari and Kouchakzadeh 2016][research_asgari_kouchakzadeh_2016]
- [Ashkenas, Irving L. and Klyde, David H. 1989][research_ashkenasirvingl_klydedavidh_1989]
- [Ashton 1970][research_ashton_1970]
- [Ashworth and McKissick 1979][research_ashworth_mckissick_1979]
- [Aston and Williams 1994][research_aston_williams_1994]
- [Audoin and Baste 1994][research_audoin_baste_1994]
- [Awadalla Ali Haj Ahmed 2024][research_awadallaalihajahmed_2024]
- [Awadalla Ali Haj Ahmed 2024][research_awadallaalihajahmed_2024_b]
- [Axelson 1977][research_axelson_1977]
- [Babuska et al 2018][research_babuska_wiebe_2018]
- [Bachman 1981][research_bachman_1981]
- [Badaliance and Dill 1981][research_badaliance_dill_1981]
- [Baek 2021][research_baek_2021]
- [Bagherzadeh 2026][research_bagherzadeh_2026]
- [Bagherzadeh et al 2025][research_bagherzadeh_mohammadkarimi_2025]
- [Bahr et al 2021][research_bahr_mckay_2021]
- [Bai 2018][research_bai_2018]
- [Bai et al 2024][research_bai_guan_2024]
- [Baier 1970][research_baier_1970]
- [Bailey, R. E. and Knotts, L. H. 1990][research_baileyre_knottslh_1990]
- [Bailey, R. E. and Smith, R. E. 1981][research_baileyre_smithre_1981]
- [Bailey, Randall E. et al 1988][research_baileyrandalle_powersbruceg_1988]
- [Baker and Galigher 1960][research_baker_galigher_1960]
- [Baker et al 1985][research_baker_jones_1985]
- [Balasubramanian et al 2025][research_balasubramanian_jayanarasimhan_2025]
- [Bandyopadhyay 1989][research_bandyopadhyay_1989]
- [Bandyopadhyay 1991][research_bandyopadhyay_1991]
- [Banks, Daniel W. 1988][research_banksdanielw_1988]
- [Bantscheff and Breitsamter 2023][research_bantscheff_breitsamter_2023]
- [Bar-Gill and Stengel 1986][research_bargill_stengel_1986]
- [Bardo 2015][research_bardo_2015]
- [Barrett et al 1983][research_barrett_rembold_1983]
- [Bartels, Robert E. et al 2019][research_bartelsroberte_stanfordbretk_2019]
- [Bastin et al 2025][research_bastin_coron_2025]
- [Bataineh and Shawabkeh 2023][research_bataineh_shawabkeh_2023]
- [Batina and Yang 1985][research_batina_yang_1985]
- [Batt 1974][research_batt_1974]
- [Batterson, James G. and Omara, Thomas M. 1989][research_battersonjamesg_omarathomasm_1989]
- [Bauchau 1981][research_bauchau_1981]
- [Bauchau 1983][research_bauchau_1983]
- [Baum et al 1979][research_baum_clark_1979]
- [Bazhenov and Lysenkova 2015][research_bazhenov_lysenkova_2015]
- [Beatty et al 1977][research_beatty_brooks_1977]
- [Becker 1992][research_becker_1992]
- [Bellini and Sorrentino 2018][research_bellini_sorrentino_2018]
- [Belmont 1983][research_belmont_1983]
- [Benaouali and Boutemedjet 2024][research_benaouali_boutemedjet_2024]
- [Bendiksen and Friedmann 1982][research_bendiksen_friedmann_1982]
- [Bennett et al 1993][research_bennett_dansberry_1993]
- [Bennett, R. M. et al 1977][research_bennettrm_farmermg_1977]
- [Bennett, Robert M. et al 1988][research_bennettrobertm_batinajohnt_1988]
- [Benoit 1969][research_benoit_1969]
- [Benoit et al 1960][research_benoit_leroy_1960]
- [Berg et al 2025][research_berg_ting_2025]
- [Bergen and Arnold 1940][research_bergen_arnold_1940]
- [Berger et al 2021][research_berger_tischler_2021]
- [Berger et al 2022][research_berger_blanken_2022]
- [Berger et al 2022][research_berger_blanken_2022_b]
- [Bergman 1948][research_bergman_1948]
- [Bergstedt et al 1959][research_bergstedt_turner_1959]
- [Bernstein 2000][research_bernstein_2000]
- [Berry et al 1982][research_berry_powers_1982]
- [Berry, D. T. 1981][research_berrydt_1981]
- [Besch and Liu 1973][research_besch_liu_1973]
- [Beyer et al 2024][research_beyer_steen_2024]
- [Beyer et al 2024][research_beyer_ullah_2024]
- [Beyers 1988][research_beyers_1988]
- [Bhardwaj and Kapania 1995][research_bhardwaj_kapania_1995]
- [Bi et al 2017][research_bi_xie_2017]
- [Bian et al 2018][research_bian_nener_2018]
- [Bian et al 2019][research_bian_nener_2019]
- [Bidinotto et al 2021][research_bidinotto_moura_2021]
- [Biezad, Daniel J. and Chou, Hwei-Lan 1993][research_biezaddanielj_chouhweilan_1993]
- [Bihrle et al 1980][research_bihrle_jr_1980]
- [Billingsley 1976][research_billingsley_1976]
- [Binder et al 2021][research_binder_wildschek_2021]
- [Binion and T. W. 1971][research_binion_tw_1971]
- [Binion and T. W. 1975][research_binion_tw_1975]
- [Biskner and Higgins 2005][research_biskner_higgins_2005]
- [Bismarck-Nasr 1994][research_bismarcknasr_1994]
- [Biswas 1993][research_biswas_1993]
- [Blackburn and Whitfield 1965][research_blackburn_whitfield_1965]
- [Blackwell and Pounds 1977][research_blackwell_pounds_1977]
- [Blair and Weisshaar 1982][research_blair_weisshaar_1982]
- [Bland 1980][research_bland_1980]
- [Blight et al 1986][research_blight_gangsaas_1986]
- [Bliss 1980][research_bliss_1980]
- [Boatwright 1961][research_boatwright_1961]
- [Bodson 2000][research_bodson_2000]
- [Bodson 2000][research_bodson_2000_b]
- [Bohlmann et al 1990][research_bohlmann_eckstrom_1990]
- [Bohlmann, Jonathan D. 1989][research_bohlmannjonathand_1989]
- [Bohlmann, Jonathan D. and Scott, Robert C. 1991][research_bohlmannjonathand_scottrobertc_1991]
- [Bohlmann, Jonathan D. et al 1988][research_bohlmannjonathand_weisshaarterrencea_1988]
- [Bolding, R. M. and Stearman, R. O. 1976][research_boldingrm_stearmanro_1976]
- [Bondarenko and Shkolnyi 2024][research_bondarenko_shkolnyi_2024]
- [Bons and Martins 2020][research_bons_martins_2020]
- [Boothe et al 1974][research_boothe_chen_1974]
- [Bordogna et al 2020][research_bordogna_lancelot_2020]
- [Borrok and Rider 1970][research_borrok_rider_1970]
- [Bosch, J. A. and Kuehl, W. J. 1976][research_boschja_kuehlwj_1976]
- [Boudreau 1977][research_boudreau_1977]
- [Bouras 2020][research_bouras_2020]
- [Bowers 1981][research_bowers_1981]
- [Bowman, Keith B et al 1989][research_bowmankeithb_grandhiramanav_1989]
- [Boyd 1977][research_boyd_1977]
- [Boyden, R. P. 1974][research_boydenrp_1974]
- [Boyden, R. P. 1978][research_boydenrp_1978]
- [Boylan 1965][research_boylan_1965]
- [Bradley 1986][research_bradley_1986]
- [Braff et al 1993][research_braff_till_1993]
- [Brennan and McDaniel 1994][research_brennan_mcdaniel_1994]
- [Briardy and Head 1968][research_briardy_head_1968]
- [Briggs et al 1982][research_briggs_reed_1982]
- [Bright, L. G. and Peterson, V. L. 1960][research_brightlg_petersonvl_1960]
- [Brock, L. D. and Goodman, H. A. 1981][research_brockld_goodmanha_1981]
- [Brodecki and Subbarao 2015][research_brodecki_subbarao_2015]
- [Broglio 1957][research_broglio_1957]
- [Bromfield et al 2023][research_bromfield_horri_2023]
- [Brooks, J. D. and Beamish, J. K. 1977][research_brooksjd_beamishjk_1977]
- [Broussard and Stengel 1977][research_broussard_stengel_1977]
- [Broussard, J. R. and Halyo, N. 1983][research_broussardjr_halyon_1983]
- [Brown 1994][research_brown_1994]
- [Brown, S. R. and Szalai, K. J. 1977][research_brownsr_szalaikj_1977]
- [Brozoski et al 2000][research_brozoski_johnson_2000]
- [Bruno, Joseph and Libeskind, Mark 1990][research_brunojoseph_libeskindmark_1990]
- [Bryant and Albert 1988][research_bryant_albert_1988]
- [Brüderlin et al 2018][research_bruderlin_hosters_2018]
- [Bueno and Dowell 2020][research_bueno_dowell_2020]
- [Buffington 1997][research_buffington_1997]
- [Buffington 1999][research_buffington_1999]
- [Buffington 1999][research_buffington_1999_b]
- [Buffington and Adams 1995][research_buffington_adams_1995]
- [Bugała 2025][research_bugala_2025]
- [Bugała and Payenskyy 2025][research_bugala_payenskyy_2025]
- [Burcham et al 1985][research_burcham_myers_1985]
- [Burdette and Martins 2018][research_burdette_martins_2018]
- [Burken, John J. 2007][research_burkenjohnj_2007]
- [Burkhalter 1993][research_burkhalter_1993]
- [Burnett et al 2016][research_burnett_beranek_2016]
- [Burns 1974][research_burns_1974]
- [Burns 1975][research_burns_1975]
- [Burns 2002][research_burns_2002]
- [Burt 1975][research_burt_1975]
- [Busan 1998][research_busan_1998]
- [Butler 1976][research_butler_1976]
- [Butler 1982][research_butler_1982]
- [Butler 1983][research_butler_1983]
- [Buzica et al 2018][research_buzica_biswanger_2018]
- [Bylsma and Gunter 2007][research_bylsma_gunter_2007]
- [Byreddy et al 2003][research_byreddy_grandhi_2003]
- [Cabell, Randolph H. and Gibbs, Gary P. 2000][research_cabellrandolphh_gibbsgaryp_2000]
- [Cahn and Garcia 1971][research_cahn_garcia_1971]
- [Cai et al 2024][research_cai_su_2024]
- [Cain 1979][research_cain_1979]
- [Caixeta and Marques 2018][research_caixeta_marques_2018]
- [Calarese 1984][research_calarese_1984]
- [California Univ Los Angeles 2001][research_californiaunivlosangeles_2001]
- [Callaghan and Kunz 2021][research_callaghan_kunz_2021]
- [Callaway 2015][research_callaway_2015]
- [Camacho et al 2021][research_camacho_akhavan_2021]
- [Campagna et al 2025][research_campagna_benedetti_2025]
- [Campagna et al 2025][research_campagna_gulizzi_2025]
- [Campbell and LaFREY 1983][research_campbell_lafrey_1983]
- [Campbell, Richard L. and Smith, Leigh A. 1989][research_campbellrichardl_smithleigha_1989]
- [Campos and Marques 2021][research_campos_marques_2021]
- [Candon et al 2026][research_candon_marzocca_2026]
- [Cannella et al 2018][research_cannella_garinei_2018]
- [Cao et al 2020][research_cao_jia_2020]
- [Cao et al 2022][research_cao_xu_2022]
- [Cao et al 2025][research_cao_liu_2025]
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
- [Cassanto 1971][research_cassanto_1971]
- [Cassanto 1972][research_cassanto_1972]
- [Castellani et al 2017][research_castellani_cooper_2017]
- [Cavaliere and Fezans 2024][research_cavaliere_fezans_2024]
- [Cavaliere et al 2024][research_cavaliere_fezans_2024_b]
- [Cavin and Holyoak 1978][research_cavin_holyoak_1978]
- [Celi 1991][research_celi_1991]
- [Celi and Friedmann 1990][research_celi_friedmann_1990]
- [Celi et al 2004][research_celi_lovera_2004]
- [Cell 1992][research_cell_1992]
- [Cen et al 2020][research_cen_li_2020]
- [Cenkci 1991][research_cenkci_1991]
- [Center 1975][research_center_1975]
- [Cesnik 2002][research_cesnik_2002]
- [Cesnik 2005][research_cesnik_2005]
- [Cestino and Iannuzzo 2026][research_cestino_iannuzzo_2026]
- [Chakravarthy et al 2015][research_chakravarthy_evans_2015]
- [Chakravarty and Mahanta 2015][research_chakravarty_mahanta_2015]
- [Chalk 1964][research_chalk_1964]
- [Chamlin 1951][research_chamlin_1951]
- [Chamlin and Davidoff 1950][research_chamlin_davidoff_1950]
- [Chance Vought Corp Dallas Tx 1979][research_chancevoughtcorpdallastx_1979]
- [Chang 1988][research_chang_1988]
- [Changchuan et al 2018][research_changchuan_lan_2018]
- [Chaparro, Daniel et al 2016][research_chaparrodaniel_fujiwaragustavoec_2016]
- [Chaplin 1953][research_chaplin_1953]
- [Chase 1977][research_chase_1977]
- [Chattopadhyay, Aditi and Jha, Ratneshwar 1996][research_chattopadhyayaditi_jharatneshwar_1996]
- [Chattopadhyay, Aditi and Zhang, Sen 1995][research_chattopadhyayaditi_zhangsen_1995]
- [Chau and Zingg 2022][research_chau_zingg_2022]
- [Chau and Zingg 2023][research_chau_zingg_2023]
- [Chau et al 2026][research_chau_piotrowski_2026]
- [Chen 1982][research_chen_1982]
- [Chen 1983][research_chen_1983]
- [Chen and Dugundji 1987][research_chen_dugundji_1987]
- [Chen and Han 2017][research_chen_han_2017]
- [Chen and Holohan 2015][research_chen_holohan_2015]
- [Chen and Li 2017][research_chen_li_2017]
- [Chen and Sun 1987][research_chen_sun_1987]
- [Chen and Zhao 2020][research_chen_zhao_2020]
- [Chen et al 2016][research_chen_liu_2016]
- [Chen et al 2018][research_chen_edwards_2018]
- [Chen et al 2018][research_chen_li_2018]
- [Chen et al 2018][research_chen_nie_2018]
- [Chen et al 2018][research_chen_yang_2018]
- [Chen et al 2020][research_chen_jing_2020]
- [Chen et al 2023][research_chen_dong_2023]
- [Chen et al 2023][research_chen_gao_2023]
- [Chen et al 2023][research_chen_gao_2023_b]
- [Chen et al 2023][research_chen_shi_2023]
- [Chen et al 2023][research_chen_shi_2023_b]
- [Chen et al 2025][research_chen_he_2025]
- [Chen et al 2026][research_chen_cai_2026]
- [Cheng, H. K. et al 1980][research_chenghk_mengsy_1980]
- [Cherry et al 1993][research_cherry_costa_1993]
- [Chetty and Lakshmi 1991][research_chetty_lakshmi_1991]
- [Chien and Tang 1964][research_chien_tang_1964]
- [Chin 1989][research_chin_1989]
- [Chin et al 1994][research_chin_lee_1994]
- [Chin, J. et al 1987][research_chinj_chaconv_1987]
- [Chinvorarat 2021][research_chinvorarat_2021]
- [Chipman, R. et al 1984][research_chipmanr_rauchf_1984]
- [Chipman, R. et al 1985][research_chipmanr_rauchf_1985]
- [Choi 2016][research_choi_2016]
- [Choi and Choi 2026][research_choi_choi_2026]
- [Choi and Park 2019][research_choi_park_2019]
- [Choi et al 2020][research_choi_lim_2020]
- [Choosak Ngaongam and Rapee Ujjin 2024][research_choosakngaongam_rapeeujjin_2024]
- [Chowdary et al 1994][research_chowdary_parthan_1994]
- [Chowhan et al 2019][research_chowhan_arya_2019]
- [Christoforou 1993][research_christoforou_1993]
- [Christopher K Droney et al 2020][research_christopherkdroney_anthonyjsclafani_2020]
- [Christopher L Blanken and Matthew S Whalley 1993][research_christopherlblanken_matthewswhalley_1993]
- [Chu, Julio and Lawing, Pierce L. 1990][research_chujulio_lawingpiercel_1990]
- [Cid Montoya et al 2018][research_cidmontoya_hernandez_2018]
- [Clark 2001][research_clark_2001]
- [Clark and LeTron 1989][research_clark_letron_1989]
- [Clark and Spurlin 1962][research_clark_spurlin_1962]
- [Clarke, R. et al 1982][research_clarker_shaned_1982]
- [Clarke, Robert et al 1994][research_clarkerobert_burkenjohnj_1994]
- [Clay and Rockafellow 1973][research_clay_rockafellow_1973]
- [Clements, Keith 2016][research_clementskeith_2016]
- [Clews 1973][research_clews_1973]
- [Cliett 1952][research_cliett_1952]
- [Clyde et al 1984][research_clyde_bonner_1984]
- [Coban 2020][research_coban_2020]
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
- [Combined flight control/utility system 1974][research_combined_flight_1974]
- [Concorde Automatic Flight Control 1971][research_concorde_automatic_1971]
- [Cong et al 2023][research_cong_hu_2023]
- [Conlan-Smith and Andreasen 2022][research_conlansmith_andreasen_2022]
- [Connelly 1982][research_connelly_1982]
- [Cook 1979][research_cook_1979]
- [Cooper, P. A. and Stroud, W. J. 1972][research_cooperpa_stroudwj_1972]
- [Corliss, L. D. and Talbot, P. D. 1977][research_corlissld_talbotpd_1977]
- [Cornelius and Lucius 1994][research_cornelius_lucius_1994]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornellaeronauticallabincbuffalony_1947]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1953][research_cornellaeronauticallabincbuffalony_1953]
- [Cotton 1974][research_cotton_1974]
- [Councill and Goble 1971][research_councill_goble_1971]
- [Crabtree 1979][research_crabtree_1979]
- [Craig 1965][research_craig_1965]
- [Crandall et al 1973][research_crandall_maund_1973]
- [Crane, D. F. 1983][research_cranedf_1983]
- [Crane, D. F. 1984][research_cranedf_1984]
- [Crane, Harold L. and Sommer, Robert W. 1961][research_craneharoldl_sommerrobertw_1961]
- [Crawley and Lee 1978][research_crawley_lee_1978]
- [Crews and Naik 1986][research_crews_naik_1986]
- [Crimi and Ordway 1962][research_crimi_ordway_1962]
- [Crittenden et al 1978][research_crittenden_weishaar_1978]
- [Crolla and Abdel-Hady 1991][research_crolla_abdelhady_1991]
- [Croom, Mark A. et al 1988][research_croommarka_whippleraymondd_1988]
- [Croop 1985][research_croop_1985]
- [Crouse and Leishman 1992][research_crouse_leishman_1992]
- [Crowe 1937][research_crowe_1937]
- [Cruz et al 1969][research_cruz_gorenberg_1969]
- [Cui et al 2022][research_cui_li_2022]
- [Cui et al 2026][research_cui_miao_2026]
- [Cully and Boller 1973][research_cully_boller_1973]
- [Cundiff and Buckingham 1999][research_cundiff_buckingham_1999]
- [Cunis et al 2020][research_cunis_condomines_2020]
- [Cunis et al 2020][research_cunis_condomines_2020_b]
- [Cunningham et al 1988][research_cunningham_batina_1988]
- [Cunningham, Herbert J. et al 1987][research_cunninghamherbertj_batinajohnt_1987]
- [Currao and Jiang 2026][research_currao_jiang_2026]
- [Cutchins, M. A. and Purvis, J. W. 1982][research_cutchinsma_purvisjw_1982]
- [Czyba and Stajer 2019][research_czyba_stajer_2019]
- [Czysz 1963][research_czysz_1963]
- [D'Andrea 2003][research_dandrea_2003]
- [D'Andrea 2008][research_dandrea_2008]
- [D. L. Birdsall 1970][research_dlbirdsall_1970]
- [Dagilis and Kilikevičius 2023][research_dagilis_kilikevicius_2023]
- [Dai et al 2016][research_dai_wu_2016]
- [Daken and Mar 1985][research_daken_mar_1985]
- [Dallas and Irvin 1956][research_dallas_irvin_1956]
- [Damodaran and Caughey 1988][research_damodaran_caughey_1988]
- [Dandois 2016][research_dandois_2016]
- [Daniel 1976][research_daniel_1976]
- [Darabi and Ganesan 2016][research_darabi_ganesan_2016]
- [Darabi and Ganesan 2017][research_darabi_ganesan_2017]
- [Das and Kapuria 2016][research_das_kapuria_2016]
- [Das and Longo 1995][research_das_longo_1995]
- [Das Patel and Kumar Karuparthi 2021][research_daspatel_kumarkaruparthi_2021]
- [Daudeville and Ladevèze 1993][research_daudeville_ladeveze_1993]
- [David and Hale 1978][research_david_hale_1978]
- [David M Richwine and David F Fisher 1992][research_davidmrichwine_davidffisher_1992]
- [Davidson et al 1972][research_davidson_hd_1972]
- [Davis 1973][research_davis_1973]
- [Davis et al 1977][research_davis_garnett_1977]
- [Davis, D. D., Jr. et al 1993][research_davisddjr_farleygaryl_1993]
- [Dawe et al 2025][research_dawe_bull_2025]
- [De Gaspari and Mantegazza 2024][research_degaspari_mantegazza_2024]
- [de Silva and Carmichael 1978][research_desilva_carmichael_1978]
- [de Souza and De Leon 2023][research_desouza_deleon_2023]
- [de Souza et al 2023][research_desouza_vuillemin_2023]
- [Deets, D. A. 1975][research_deetsda_1975]
- [Deformational behaviour of a 1990][research_deformational_behaviour_1990]
- [del Carre and Palacios 2020][research_delcarre_palacios_2020]
- [Demarchi and Haning 1978][research_demarchi_haning_1978]
- [Demir and Seyfullah Babaarslan 2021][research_demir_seyfullahbabaarslan_2021]
- [Deng and Yi 2023][research_deng_yi_2023]
- [DeNinno and Uherka 1966][research_deninno_uherka_1966]
- [Department Of The Air Force Washington Dc 1986][research_departmentoftheairforcewashingtondc_1986]
- [Description and Flight Test 1975][research_description_and_1975]
- [Design of discrete-time adaptive 1995][research_design_of_1995]
- [Desilva, B. M. E. and Medan, R. T. 1978][research_desilvabme_medanrt_1978]
- [Deskos et al 2020][research_deskos_delcarre_2020]
- [DeSpirito 2005][research_despirito_2005]
- [Devine et al 2025][research_devine_choynowski_2025]
- [Dexter 1993][research_dexter_1993]
- [Dhawan et al 2026][research_dhawan_huang_2026]
- [Dhital and Chouvion 2024][research_dhital_chouvion_2024]
- [Dhonau et al 1974][research_dhonau_blosser_1974]
- [Di Francesco and Mattei 2016][research_difrancesco_mattei_2016]
- [Di Pasquale and Prince 2023][research_dipasquale_prince_2023]
- [Di Rito and Schettini 2016][research_dirito_schettini_2016]
- [Dickerson 2020][research_dickerson_2020]
- [Diederich, Franklin W and Budiansky, Bernard 1948][research_diederichfranklinw_budianskybernard_1948]
- [Difranco 1970][research_difranco_1970]
- [DiFranco 1971][research_difranco_1971]
- [Diggins 1951][research_diggins_1951]
- [Digital model-reference flight control 1994][research_digital_model_reference_1994]
- [Dillinger et al 2019][research_dillinger_abdalla_2019]
- [Dillinger et al 2020][research_dillinger_meddaikar_2020]
- [Dlamini and Jones 2016][research_dlamini_jones_2016]
- [Dobos-Bubno and Hartsook 1977][research_dobosbubno_hartsook_1977]
- [Dodayav et al 2024][research_dodayav_biswas_2024]
- [Dodic et al 2023][research_dodic_krstic_2023]
- [Doggett, Robert V., Jr. et al 1995][research_doggettrobertvjr_riverajoseajr_1995]
- [Doman 1995][research_doman_1995]
- [Dong 2025][research_dong_2025]
- [Dong and Li 2022][research_dong_li_2022]
- [Dong et al 2016][research_dong_lu_2016]
- [Dong et al 2019][research_dong_shi_2019]
- [Dong et al 2023][research_dong_li_2023]
- [Dong et al 2025][research_dong_zhou_2025]
- [Dorey et al 1980][research_dorey_good_1980]
- [Dowell and Bliss 1978][research_dowell_bliss_1978]
- [Dresselhaus and Dresselhaus 1982][research_dresselhaus_dresselhaus_1982]
- [Drtil and Schulz 1978][research_drtil_schulz_1978]
- [Drummond 1971][research_drummond_1971]
- [Duan and He 2024][research_duan_he_2024]
- [Dukes 1970][research_dukes_1970]
- [Dul 2018][research_dul_2018]
- [Dunmire 1982][research_dunmire_1982]
- [Dunn et al 1981][research_dunn_leong_1981]
- [Dunn, W. R. et al 1986][research_dunnwr_cottrelld_1986]
- [Dunning, Peter D. et al 2014][research_dunningpeterd_stanfordbretk_2014]
- [Durand and Teper 1964][research_durand_teper_1964]
- [Durston, D. A. and Schreiner, J. A. 1983][research_durstonda_schreinerja_1983]
- [DuShane 1957][research_dushane_1957]
- [Dussart et al 2019][research_dussart_lone_2019]
- [Dwivedi et al 2022][research_dwivedi_anitha_2022]
- [Eades et al 1964][research_eades_jr_1964]
- [Eastep and Olsen 1980][research_eastep_olsen_1980]
- [Eastep et al 1984][research_eastep_venkayya_1984]
- [Ebner, R. E. and Mark, J. G. 1977][research_ebnerre_markjg_1977]
- [Ecer 1985][research_ecer_1985]
- [Eckhaus 1962][research_eckhaus_1962]
- [Eckstrom, C. V. and Spain, C. V. 1982][research_eckstromcv_spaincv_1982]
- [Edenborough 1968][research_edenborough_1968]
- [Edwards 1983][research_edwards_1983]
- [Effects of a controlled 1988][research_effects_of_1988]
- [Efremov et al 2020][research_efremov_efremov_2020]
- [Efremov et al 2022][research_efremov_shcherbakov_2022]
- [Ehlers and Weisshaar 1993][research_ehlers_weisshaar_1993]
- [Eichler 1970][research_eichler_1970]
- [Ekaterinaris, J. A. and Schiff, Lewis B. 1990][research_ekaterinarisja_schifflewisb_1990]
- [Ekaterinaris, J. A. and Schiff, Lewis B. 1994][research_ekaterinarisja_schifflewisb_1994]
- [Ekquist 1965][research_ekquist_1965]
- [El-Mahdy et al 2025][research_elmahdy_ali_2025]
- [Elenchezhiyan and Kumar 2025][research_elenchezhiyan_kumar_2025]
- [Elshazly et al 2025][research_elshazly_kassem_2025]
- [Eney 1968][research_eney_1968]
- [Eng 1988][research_eng_1988]
- [Engelland, S. A. et al 1992][research_engellandsa_franklinja_1992]
- [Enns 2003][research_enns_2003]
- [Er-El 1988][research_erel_1988]
- [Er-El and Seginer 1985][research_erel_seginer_1985]
- [Eraslan and Oktay 2023][research_eraslan_oktay_2023]
- [Erickson, Gary E. 2003][research_ericksongarye_2003]
- [Eriksson 1990][research_eriksson_1990]
- [Esfahani et al 2018][research_esfahani_webb_2018]
- [Eugene, L. Tu 1996][research_eugeneltu_1996]
- [Ewing et al 1988][research_ewing_hinger_1988]
- [Fadel et al 2019][research_fadel_rabie_2019]
- [Fan et al 2025][research_fan_wang_2025]
- [Fanucci 1987][research_fanucci_1987]
- [Farbridge et al 1956][research_farbridge_woodward_1956]
- [Farhat and Amsallem 2011][research_farhat_amsallem_2011]
- [Farmer, M. G. and Hanson, P. W. 1976][research_farmermg_hansonpw_1976]
- [Farsadi et al 2026][research_farsadi_ahmadi_2026]
- [Fatigue behaviour of composite 1977][research_fatigue_behaviour_1977]
- [Favier et al 1987][research_favier_maresca_1987]
- [Fay and Johnstone 1960][research_fay_johnstone_1960]
- [Fazeli et al 2022][research_fazeli_stokesgriffin_2022]
- [Fearnside 1962][research_fearnside_1962]
- [Fedorenko and Bondarenko 2024][research_fedorenko_bondarenko_2024]
- [Fehrs and Kaiser 2025][research_fehrs_kaiser_2025]
- [Feil et al 2020][research_feil_pflumm_2020]
- [Feng et al 2023][research_feng_guo_2023]
- [Ferraiuolo et al 2019][research_ferraiuolo_scigliano_2019]
- [Ferreres and Hardier 2017][research_ferreres_hardier_2017]
- [Feuer et al 1977][research_feuer_barmish_1977]
- [Fichera et al 2019][research_fichera_isnardi_2019]
- [Figge 1973][research_figge_1973]
- [Filamentary-plastic composite laminate 1974][research_filamentary_plastic_composite_1974]
- [Filippou et al 2024][research_filippou_kilimtzidis_2024]
- [Finkleman 1972][research_finkleman_1972]
- [Flax 1943][research_flax_1943]
- [Flight Sciences Lab Inc Buffalo Ny 1964][research_flightscienceslabincbuffalony_1964]
- [Florance, James R. et al 2004][research_florancejamesr_heegjennifer_2004]
- [Flores et al 2025][research_flores_bazan_2025]
- [Fodor and Redfield 1993][research_fodor_redfield_1993]
- [Fonte et al 2015][research_fonte_ricci_2015]
- [Food safety management system 2023][research_food_safety_2023]
- [Forsman 1983][research_forsman_1983]
- [Fortiş et al 2015][research_fortis_fortis_2015]
- [Foss, W. E., Jr. and Whitcomb, C. F. 1960][research_fosswejr_whitcombcf_1960]
- [Fournier et al 2022][research_fournier_massioni_2022]
- [Fradenburgh et al 1973][research_fradenburgh_murrill_1973]
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
- [Fujii 1985][research_fujii_1985]
- [Fujioka and Suzuki 1994][research_fujioka_suzuki_1994]
- [Fukuda and Kobayashi 1987][research_fukuda_kobayashi_1987]
- [Fukunaga 1990][research_fukunaga_1990]
- [Fuller 1991][research_fuller_1991]
- [Fuller 2001][research_fuller_2001]
- [Fung 1982][research_fung_1982]
- [Furtat and Gushchin 2021][research_furtat_gushchin_2021]
- [Fuzzy logic control for 1994][research_fuzzy_logic_1994]
- [Fuzzy logic for control 1991][research_fuzzy_logic_1991]
- [Gabel et al 1961][research_gabel_ricks_1961]
- [Gainer 1963][research_gainer_1963]
- [Galasso et al 2024][research_galasso_ciminello_2024]
- [Galffy et al 2019][research_galffy_bock_2019]
- [Gamon and Mahone 1975][research_gamon_mahone_1975]
- [Gao and Wang 2021][research_gao_wang_2021]
- [Gao et al 2024][research_gao_liu_2024]
- [Garabedian, P. R. 1979][research_garabedianpr_1979]
- [Garcia-Hernandez et al 2017][research_garciahernandez_cuernorejado_2017]
- [Garg, Sanjay and Schmidt, David K. 1988][research_gargsanjay_schmidtdavidk_1988]
- [Garkushenko and Vinogradov 2016][research_garkushenko_vinogradov_2016]
- [Garrard and Low 1990][research_garrard_low_1990]
- [Garrick, I E and Rubinow, S I 1946][research_garrickie_rubinowsi_1946]
- [Garrick, I E and Rubinow, S I 1946][research_garrickie_rubinowsi_1946_b]
- [Garrison, Charlie C. and Hacskaylo, Andrew 1947][research_garrisoncharliec_hacskayloandrew_1947]
- [Gea et al 1992][research_gea_chow_1992]
- [Gearhart 1962][research_gearhart_1962]
- [General Dynamics/Astronautics San Diego Ca 1961][research_generaldynamicsastronauticssandiegoca_1961_b]
- [General Dynamics/Astronautics San Diego Ca 1962][research_generaldynamicsastronauticssandiegoca_1962]
- [General Dynamics/Astronautics San Diegoca 1961][research_generaldynamicsastronauticssandiegoca_1961]
- [Gerdes and Hynes 1972][research_gerdes_hynes_1972]
- [Ghalandari et al 2022][research_ghalandari_mahariq_2022]
- [Ghayour and Mani 2018][research_ghayour_mani_2018]
- [Giese et al 1996][research_giese_reich_1996]
- [Gilbert and Schneider 1981][research_gilbert_schneider_1981]
- [Gilbert et al 1984][research_gilbert_schmidt_1984]
- [Gilbert, Michael G. 1987][research_gilbertmichaelg_1987]
- [Gill 1995][research_gill_1995]
- [Giurgiutiu and Pomirleanu 2000][research_giurgiutiu_pomirleanu_2000]
- [Glezer and Leonard 2012][research_glezer_leonard_2012]
- [Gloss and Washburn 1978][research_gloss_washburn_1978]
- [Gloss, B. B. and Washburn, K. E. 1977][research_glossbb_washburnke_1977]
- [Godwin et al 1964][research_godwin_frazier_1964]
- [Goizueta et al 2022][research_goizueta_wynn_2022]
- [Goizueta et al 2022][research_goizueta_wynn_2022_b]
- [Goland 1945][research_goland_1945]
- [Gonabadi et al 2021][research_gonabadi_oila_2021]
- [Gong et al 2019][research_gong_wang_2019]
- [González et al 2020][research_gonzalez_silvestre_2020]
- [González-Montijo et al 2026][research_gonzalezmontijo_vanness_2026]
- [Goodrich, Kenneth H. et al 1989][research_goodrichkennethh_sliwastevenm_1989]
- [Goodyear Aerospace Corp Akron Oh 1958][research_goodyearaerospacecorpakronoh_1958]
- [Goradia, S. H. et al 1989][research_goradiash_bobbittpj_1989]
- [Goranson 1997][research_goranson_1997]
- [Gottzein et al 1975][research_gottzein_cramer_1975]
- [Goucem and Khiri 2023][research_goucem_khiri_2023]
- [Gowd 2016][research_gowd_2016]
- [Grafton, S. B. et al 1982][research_graftonsb_gilberwp_1982]
- [Grant et al 2015][research_grant_stol_2015]
- [Grantham, W. D. et al 1976][research_granthamwd_nguyenlt_1976]
- [Graphite/epoxy composite violin 1981][research_graphite_epoxy_composite_1981]
- [Grauer, Jared A. and Boucher, Matthew J. 2017][research_grauerjareda_bouchermatthewj_2017]
- [Graves and Sawicki 1994][research_graves_sawicki_1994]
- [Gray and Mei 1993][research_gray_mei_1993]
- [Green 1987][research_green_1987]
- [Green, J. A. 1986][research_greenja_1986]
- [Greenberg, Harry and Sternfield, Leonard 1944][research_greenbergharry_sternfieldleonard_1944]
- [Greene 1928][research_greene_1928]
- [Greene 1955][research_greene_1955]
- [Greene 1956][research_greene_1956]
- [Greene 1957][research_greene_1957]
- [Greenhalgh et al 1993][research_greenhalgh_pastore_1993]
- [Greszczuk and Chao 1975][research_greszczuk_chao_1975]
- [Griffin and Eastep 1982][research_griffin_eastep_1982]
- [Griffin et al 1983][research_griffin_haerter_1983]
- [Griffin, Brian Joseph et al 2010][research_griffinbrianjoseph_burkenjohnj_2010]
- [Griffin, Charles F. and Harvill, William E. 1988][research_griffincharlesf_harvillwilliame_1988]
- [Griffis et al 1981][research_griffis_masumura_1981]
- [Grifò et al 2023][research_grifo_gulizzi_2023]
- [Grossschmidt and Pahapill 1995][research_grossschmidt_pahapill_1995]
- [Gu et al 2022][research_gu_taghipour_2022]
- [Gu et al 2023][research_gu_ducvo_2023]
- [Guderley 1956][research_guderley_1956]
- [Guinn, Wiley A. 1984][research_guinnwileya_1984]
- [Guinn, Wiley A. et al 1983][research_guinnwileya_willeycraigs_1983]
- [Guinn, Wiley A. et al 1984][research_guinnwileya_risingjerryj_1984]
- [Gunnink 1988][research_gunnink_1988]
- [Guo 2021][research_guo_2021]
- [Guo 2021][research_guo_2021_b]
- [Guo and Guan 1993][research_guo_guan_1993]
- [Guo et al 1988][research_guo_wang_1988]
- [Guo et al 2017][research_guo_hou_2017]
- [Guo et al 2020][research_guo_zhou_2020]
- [Guo et al 2022][research_guo_zhang_2022]
- [Guo et al 2025][research_guo_wang_2025]
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
- [Haftka 1977][research_haftka_1977]
- [Haftmann et al 1988][research_haftmann_debbeler_1988]
- [Hagnell et al 2016][research_hagnell_langbeck_2016]
- [Hahn and Haupt 2022][research_hahn_haupt_2022]
- [Hahn and Kim 1976][research_hahn_kim_1976]
- [Haley and Soloway 2022][research_haley_soloway_2022]
- [Hall 1971][research_hall_1971]
- [Hallauer and Jr. 1983][research_hallauer_jr_1983]
- [Hallissy, J. B. and Ayers, T. G. 1977][research_hallissyjb_ayerstg_1977]
- [Hamada et al 2019][research_hamada_saitoh_2019]
- [Hamilton, Brian K. and Peters, James R. 1989][research_hamiltonbriank_petersjamesr_1989]
- [Hammer and Bright 1998][research_hammer_bright_1998]
- [Hamza et al 2026][research_hamza_akram_2026]
- [Han and Glower 1985][research_han_glower_1985]
- [Han and Pei 2026][research_han_pei_2026]
- [Han et al 2019][research_han_yu_2019]
- [Han et al 2022][research_han_zhang_2022]
- [Hanagud et al 1989][research_hanagud_craig_1989]
- [Hancock 1992][research_hancock_1992]
- [Hancock, Regis and Fullerton, Gordon 1992][research_hancockregis_fullertongordon_1992]
- [Hanman et al 2025][research_hanman_yao_2025]
- [Hanson, Curt et al 2011][research_hansoncurt_schaeferjacob_2011]
- [Hanson, G. D. and Stengel, R. F. 1981][research_hansongd_stengelrf_1981]
- [Hanson, G. D. and Stengel, R. F. 1983][research_hansongd_stengelrf_1983]
- [Harper and Robert P. 1955][research_harper_robertp_1955]
- [Harris, C. D. 1974][research_harriscd_1974]
- [Harris, C. D. 1974][research_harriscd_1974_b]
- [Hart 1956][research_hart_1956]
- [Hartini et al 2026][research_hartini_bachtiar_2026]
- [Harvill, W. E. and Kizer, J. A. 1976][research_harvillwe_kizerja_1976]
- [Hashii, Wendy N. and Thompson, Randolph C. 2018][research_hashiiwendyn_thompsonrandolphc_2018]
- [Hayashi 1949][research_hayashi_1949]
- [Hayashi 1988][research_hayashi_1988]
- [Hać 1987][research_hac_1987]
- [Hać 1992][research_hac_1992]
- [Hebbar and Pashilkar 2016][research_hebbar_pashilkar_2016]
- [Heckl et al 1962][research_heckl_lyon_1962]
- [Heeg, Jennifer 2006][research_heegjennifer_2006]
- [Heeg, Jennifer et al 2004][research_heegjennifer_spaincharlesv_2004]
- [Heeg, Jennifer et al 2005][research_heegjennifer_spaincharlesv_2005]
- [Heinrich et al 2022][research_heinrich_vogt_2022]
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
- [Herrmann and Ben-Asher 2016][research_herrmann_benasher_2016]
- [Herrmann, G. et al 1966][research_herrmanng_nematnassers_1966]
- [Hertz, T. J. et al 1982][research_hertztj_shirkmh_1982]
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
- [Hirai and Kline 1973][research_hirai_kline_1973]
- [Hirai and Satoh 1980][research_hirai_satoh_1980]
- [Hirato et al 2019][research_hirato_shen_2019]
- [Hirsch and McCORMICK 1966][research_hirsch_mccormick_1966]
- [Hitch 1978][research_hitch_1978]
- [Hitzel 2017][research_hitzel_2017]
- [Hitzel and Osterhuber 2018][research_hitzel_osterhuber_2018]
- [Hodgkinson 2017][research_hodgkinson_2017]
- [Hodgkinson et al 1976][research_hodgkinson_lamanna_1976]
- [Hofmann and Kezer 1962][research_hofmann_kezer_1962]
- [Hogan and Rinde 1978][research_hogan_rinde_1978]
- [Holst 1988][research_holst_1988]
- [Holst and Brown 1983][research_holst_brown_1983]
- [Honeycomb-laminate composite structure 1979][research_honeycomb_laminate_composite_1979]
- [Hong and Cheong 1993][research_hong_cheong_1993]
- [Hong and Ko 2015][research_hong_ko_2015]
- [Hong et al 2024][research_hong_kim_2024]
- [Hopkins, E. J. and Yee, S. C. 1977][research_hopkinsej_yeesc_1977]
- [Hopwood et al 2023][research_hopwood_gresham_2023]
- [Horton and Mayers 1965][research_horton_mayers_1965]
- [Hortsen et al 1983][research_hortsen_boer_1983]
- [Hoseini and Hodges 2019][research_hoseini_hodges_2019]
- [Housner, J. M. and Stein, M. 1974][research_housnerjm_steinm_1974]
- [Houtman et al 2023][research_houtman_timme_2023]
- [How 2004][research_how_2004]
- [Howard and O'Leary 1994][research_howard_oleary_1994]
- [Howdyshell et al 1998][research_howdyshell_trovillion_1998]
- [Hu et al 2026][research_hu_qiu_2026]
- [Huang et al 2019][research_huang_yang_2019]
- [Huang et al 2022][research_huang_yu_2022]
- [Huang et al 2024][research_huang_wang_2024]
- [Huang et al 2026][research_huang_li_2026]
- [Huff and W. W. 1949][research_huff_ww_1949]
- [Huffman, J. K. 1975][research_huffmanjk_1975]
- [Huiping et al 1989][research_huiping_yutian_1989]
- [Human Supervisory Control of 2015][research_human_supervisory_2015]
- [Hummel and Oelker 1994][research_hummel_oelker_1994]
- [Humphreys-Jennings et al 2020][research_humphreysjennings_lappas_2020]
- [Hunn 1953][research_hunn_1953]
- [Hunter 2003][research_hunter_2003]
- [Hurley 1975][research_hurley_1975]
- [Hutchinson 2014][research_hutchinson_2014]
- [Hybrid composite laminate structures 1978][research_hybrid_composite_1978]
- [Hübener and Luckner 2026][research_hubener_luckner_2026]
- [Iannelli et al 2018][research_iannelli_marcos_2018]
- [Ibren et al 2020][research_ibren_sulaeman_2020]
- [Ignatyev and Khrabrov 2018][research_ignatyev_khrabrov_2018]
- [Ilcewicz, L. B. et al 1991][research_ilcewiczlb_walkerth_1991]
- [Iliff, K. W. et al 1978][research_iliffkw_mainere_1978]
- [Iliff, K. W. et al 1981][research_iliffkw_mainere_1981]
- [Im et al 2025][research_im_kong_2025]
- [Inger 1983][research_inger_1983]
- [Ingram, W. C. et al 1986][research_ingramwc_yiplp_1986]
- [Interlaminar shear fracture of 1992][research_interlaminar_shear_1992]
- [Introduction to the Special 2017][research_introduction_to_2017]
- [Ioannis and Ioannis 2026][research_ioannis_ioannis_2026]
- [Irvine 1968][research_irvine_1968]
- [Iryani et al 2019][research_iryani_kadir_2019]
- [Ishmael, S. D. and Wierzbanowski, T. 1985][research_ishmaelsd_wierzbanowskit_1985]
- [Ishmael, Stephen D. et al 1990][research_ishmaelstephend_smithrogerse_1990]
- [Isogai 1979][research_isogai_1979]
- [Isogai 1981][research_isogai_1981]
- [Isogai 1988][research_isogai_1988]
- [Isogai 1989][research_isogai_1989]
- [Isogai 1992][research_isogai_1992]
- [Ito and Iwashita 2017][research_ito_iwashita_2017]
- [Ivler et al 2022][research_ivler_truong_2022]
- [J Elliott 1977][research_jelliott_1977]
- [Jacobson 1952][research_jacobson_1952]
- [Jacobson and Joshi 1978][research_jacobson_joshi_1978]
- [Jafari and Mashadi 2022][research_jafari_mashadi_2022]
- [Jaffar Syed Mohamed Ali and Shahzatul Sakinah Binti Haron 2021][research_jaffarsyedmohamedali_shahzatulsakinahbintiharon_2021]
- [Jalalnezhad 2026][research_jalalnezhad_2026]
- [James A Franklin 1993][research_jamesafranklin_1993]
- [James M Luckring 2003][research_jamesmluckring_2003]
- [Janardhan and Grandhi 2003][research_janardhan_grandhi_2003]
- [Janecek 1986][research_janecek_1986]
- [Jared A Grauer 2018][research_jaredagrauer_2018]
- [Jarrell R Elliott 1976][research_jarrellrelliott_1976]
- [Jarvis, C. R. 1967][research_jarviscr_1967]
- [Jarvis, C. R. 1975][research_jarviscr_1975]
- [Jarvis, C. R. and Szalai, K. J. 1981][research_jarviscr_szalaikj_1981]
- [Jegley, Dawn C. and Bush, Harold G. 1997][research_jegleydawnc_bushharoldg_1997]
- [Jegley, Dawn C. and Bush, Harold G. 2001][research_jegleydawnc_bushharoldg_2001]
- [Jegley, Dawn C. and Wijayratne, Dulnath D. 2004][research_jegleydawnc_wijayratnedulnathd_2004]
- [Jegley, Dawn C. et al 2001][research_jegleydawnc_bushharoldg_2001_b]
- [Jegley, Dawn C. et al 2001][research_jegleydawnc_lovejoyandrewe_2001]
- [Jeng and Payne 1995][research_jeng_payne_1995]
- [Jenks, G. E. et al 1977][research_jenksge_henryhf_1977]
- [Jenney and Schreadley 1984][research_jenney_schreadley_1984]
- [Jenney et al 1982][research_jenney_schreadley_1982]
- [Jensen and Crawley 1984][research_jensen_crawley_1984]
- [Jensen et al 1982][research_jensen_crawley_1982]
- [Jewell et al 1979][research_jewell_heffley_1979]
- [Ji et al 2022][research_ji_lu_2022]
- [Ji et al 2023][research_ji_kim_2023]
- [Jia et al 2023][research_jia_ezhilarasu_2023]
- [Jia et al 2023][research_jia_sun_2023]
- [Jiang et al 2022][research_jiang_tong_2022]
- [Jianhong and Yanxiang 2026][research_jianhong_yanxiang_2026]
- [Jiao and Jiang 2015][research_jiao_jiang_2015]
- [Jin and Xue 2026][research_jin_xue_2026]
- [John W Hicks et al 1987][research_johnwhicks_jankania_1987]
- [Johnson 1965][research_johnson_1965]
- [Johnson 1972][research_johnson_1972]
- [Johnson 1973][research_johnson_1973]
- [Johnson and Nokes 1998][research_johnson_nokes_1998]
- [Johnson, R. W. and June, R. R. 1972][research_johnsonrw_junerr_1972]
- [Johnson, R. W. and Mccarty, J. E. 1977][research_johnsonrw_mccartyje_1977]
- [Johnson, W. 1977][research_johnsonw_1977]
- [Johnston and Cassarino 1976][research_johnston_cassarino_1976]
- [Johnston et al 1974][research_johnston_ashkenas_1974]
- [Jones 1970][research_jones_1970]
- [Jones 1976][research_jones_1976]
- [Jones and Nisbet 1976][research_jones_nisbet_1976]
- [Jones et al 1985][research_jones_broughton_1985]
- [Jonnalagadda et al 2015][research_jonnalagadda_sawant_2015]
- [Jou and Metcalfe 1984][research_jou_metcalfe_1984]
- [Juhasz et al 2023][research_juhasz_tischler_2023]
- [Jun-yi et al 2021][research_junyi_xinbing_2021]
- [K. and Deodhare 2023][research_k_deodhare_2023]
- [Kabaliswaran and Das 2026][research_kabaliswaran_das_2026]
- [Kafkas et al 2021][research_kafkas_kilimtzidis_2021]
- [Kalnins 1968][research_kalnins_1968]
- [Kalugin et al 2022][research_kalugin_voropaev_2022]
- [Kamaletdinova and Romanov 2024][research_kamaletdinova_romanov_2024]
- [Kambampati and Smith 2017][research_kambampati_smith_2017]
- [Kanazaki and Setoguchi 2023][research_kanazaki_setoguchi_2023]
- [Kapania and Issac 1994][research_kapania_issac_1994]
- [Kapania et al 1991][research_kapania_bergen_1991]
- [Kapania, Rakesh K. et al 1997][research_kapaniarakeshk_issacj_1997]
- [Karal, Michael 2001][research_karalmichael_2001]
- [Karimi Kelayeh and Djavareshkian 2024][research_karimikelayeh_djavareshkian_2024]
- [Karniadakis 2004][research_karniadakis_2004]
- [Karpouzian 1991][research_karpouzian_1991]
- [Kasim Biber and Trenton White 2019][research_kasimbiber_trentonwhite_2019]
- [Kassem et al 2021][research_kassem_yang_2021]
- [Kataoka et al 1986][research_kataoka_dol_1986]
- [Katz and Levin 1986][research_katz_levin_1986]
- [Katz et al 1986][research_katz_davidovitch_1986]
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
- [Key 1971][research_key_1971]
- [Khadse and Karmore 2016][research_khadse_karmore_2016]
- [Khalil and Bauknecht 2024][research_khalil_bauknecht_2024]
- [Khalil and Fezans 2020][research_khalil_fezans_2020]
- [Khalil et al 2022][research_khalil_asaro_2022]
- [Kholodar 2016][research_kholodar_2016]
- [Kieffer 2006][research_kieffer_2006]
- [Kielb 1975][research_kielb_1975]
- [Kilgore and Averett 1964][research_kilgore_averett_1964]
- [Kilimtzidis et al 2023][research_kilimtzidis_giannaros_2023]
- [Kim and Choi 2015][research_kim_choi_2015]
- [Kim and Kang 2025][research_kim_kang_2025]
- [Kim and Kunz 2017][research_kim_kunz_2017]
- [Kim et al 2016][research_kim_shin_2016]
- [Kineyko 1982][research_kineyko_1982]
- [King and Johnson 1986][research_king_johnson_1986]
- [Kinney 1963][research_kinney_1963]
- [Kirsch et al 2020][research_kirsch_montagnier_2020]
- [Kish et al 1997][research_kish_mosle_1997]
- [Kishi et al 2016][research_kishi_kanazaki_2016]
- [Kishi et al 2022][research_kishi_kanazaki_2022]
- [Kisslinger and Wendl 1971][research_kisslinger_wendl_1971]
- [Kizildeniz and Kiyak 2025][research_kizildeniz_kiyak_2025]
- [Klasztorny et al 2018][research_klasztorny_nycz_2018]
- [Klein, R. W. and Hollister, W. M. 1982][research_kleinrw_hollisterwm_1982]
- [Klein, R. W. et al 1982][research_kleinrw_lapinsm_1982]
- [Klepl 1995][research_klepl_1995]
- [Klinar, W. J. et al 1975][research_klinarwj_kubiaket_1975]
- [Klotzsche, M. 1984][research_klotzschem_1984]
- [Klug et al 2023][research_klug_ullah_2023]
- [Klyde et al 2004][research_klyde_harris_2004]
- [Knackstedt 1952][research_knackstedt_1952]
- [Knauss, J. F. and Stone, R. H. 1982][research_knaussjf_stonerh_1982]
- [Knight 1982][research_knight_1982]
- [Knighton, Donna L. 1992][research_knightondonnal_1992]
- [Knox-Seith 1963][research_knoxseith_1963]
- [Kobayashi and Torisaki 1986][research_kobayashi_torisaki_1986]
- [Kobelev 2019][research_kobelev_2019]
- [Koenig 1984][research_koenig_1984]
- [Kohara et al 2016][research_kohara_tomoeda_2016]
- [Kohlman 1979][research_kohlman_1979]
- [Kohnhorst and Magnacca 1980][research_kohnhorst_magnacca_1980]
- [Kokotovic et al 2000][research_kokotovic_murray_2000]
- [Kolesar 1971][research_kolesar_1971]
- [Komarov and Zinchenko 2023][research_komarov_zinchenko_2023]
- [Komnatska and Bondarenko 2017][research_komnatska_bondarenko_2017]
- [Konar et al 1974][research_konar_mahesh_1974]
- [Koo and Lee 1994][research_koo_lee_1994]
- [Kopecki 2016][research_kopecki_2016]
- [Kornev et al 2021][research_kornev_ambrozhevich_2021]
- [Koscielny 1983][research_koscielny_1983]
- [Kosyanchuk et al 2015][research_kosyanchuk_selvesyuk_2015]
- [Kosyanchuk et al 2021][research_kosyanchuk_zheltov_2021]
- [Kousen and Bendiksen 1994][research_kousen_bendiksen_1994]
- [Kozhanov et al 2022][research_kozhanov_suvorova_2022]
- [Krachmalnick et al 1968][research_krachmalnick_vetsch_1968]
- [Kraft, Christopher C., Jr. and Reeder, J. P. 1948][research_kraftchristophercjr_reederjp_1948]
- [Kratochvíl and Valenta 2024][research_kratochvil_valenta_2024]
- [Krener 2001][research_krener_2001]
- [Kriechbaum and Stineman 1972][research_kriechbaum_stineman_1972]
- [Kroo 1982][research_kroo_1982]
- [Krzywoblocki 1943][research_krzywoblocki_1943]
- [Krüger et al 2022][research_kruger_meddaikar_2022]
- [Kubica et al 1995][research_kubica_livet_1995]
- [Kuhlberg and Newirth 1976][research_kuhlberg_newirth_1976]
- [Kuhn 1975][research_kuhn_1975]
- [Kulikov 2020][research_kulikov_2020]
- [Kumar et al 2025][research_kumar_asha_2025]
- [Kumar Shakya and Sekhar Padhee 2023][research_kumarshakya_sekharpadhee_2023]
- [Kuo-Jiun et al 1989][research_kuojiun_pongjeu_1989]
- [Kurniawan 2022][research_kurniawan_2022]
- [Kurz 1963][research_kurz_1963]
- [Kurzhals, P. R. 1978][research_kurzhalspr_1978]
- [Kusni et al 2021][research_kusni_widiramdhani_2021]
- [Kuttieri and Sinha 2023][research_kuttieri_sinha_2023]
- [Kuvshinov 2016][research_kuvshinov_2016]
- [Kuvshinov 2016][research_kuvshinov_2016_b]
- [Kuvshinov and Leontiev 2019][research_kuvshinov_leontiev_2019]
- [Kuvshinov et al 2019][research_kuvshinov_lazurin_2019]
- [Kuznetsov and Kartashov 1980][research_kuznetsov_kartashov_1980]
- [Kwatny et al 1991][research_kwatny_bennett_1991]
- [Lai 2024][research_lai_2024]
- [Lai and Young 1995][research_lai_young_1995]
- [Laitone 1978][research_laitone_1978]
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
- [Langston 1967][research_langston_1967]
- [Lapins, M. et al 1982][research_lapinsm_kleinrw_1982]
- [Larson, Richard R. 1987][research_larsonrichardr_1987]
- [Latency Control in Real-Time 2025][research_latency_control_2025]
- [Lavretsky 2019][research_lavretsky_2019]
- [Le 2026][research_le_2026]
- [Lee 1977][research_lee_1977]
- [Lee 1995][research_lee_1995]
- [Lee and Cho 1991][research_lee_cho_1991]
- [Lee and Cho 1991][research_lee_cho_1991_b]
- [Lee and Eyi 1993][research_lee_eyi_1993]
- [Lee and Kim 1995][research_lee_kim_1995]
- [Lee and Lee 1990][research_lee_lee_1990]
- [Lee and Lua 2025][research_lee_lua_2025]
- [Lee and Lua 2026][research_lee_lua_2026]
- [Lee and Mall 1989][research_lee_mall_1989]
- [Lee and Ohman 1984][research_lee_ohman_1984]
- [Lee and Ohman 1984][research_lee_ohman_1984_b]
- [Lee and Sheu 1994][research_lee_sheu_1994]
- [Lee and Singh 2018][research_lee_singh_2018]
- [Lee and Tang 1989][research_lee_tang_1989]
- [Lee et al 1994][research_lee_kim_1994]
- [Lee et al 2020][research_lee_kim_2020]
- [Lee et al 2023][research_lee_lee_2023]
- [Lehman and Stearman 1977][research_lehman_stearman_1977]
- [Leighton 1978][research_leighton_1978]
- [Leitch et al 2024][research_leitch_stodieck_2024]
- [Leitch et al 2025][research_leitch_stodieck_2025]
- [Lemay, S. P. et al 1988][research_lemaysp_batillsm_1988]
- [Lemmon and Coleman 1973][research_lemmon_coleman_1973]
- [Leondes and Rankine 1972][research_leondes_rankine_1972]
- [Lerner and Markowitz 1979][research_lerner_markowitz_1979]
- [Lerro et al 2020][research_lerro_brandl_2020]
- [Lesoinne 2007][research_lesoinne_2007]
- [Levi and Nelson 1964][research_levi_nelson_1964]
- [Li 2023][research_li_2023]
- [Li and Qin 2020][research_li_qin_2020]
- [Li and Qin 2021][research_li_qin_2021]
- [Li and Qin 2021][research_li_qin_2021_b]
- [Li and Qin 2022][research_li_qin_2022]
- [Li and Shi 2021][research_li_shi_2021]
- [Li and Wang 2018][research_li_wang_2018]
- [Li and Yang 2017][research_li_yang_2017]
- [Li et al 2017][research_li_jin_2017]
- [Li et al 2019][research_li_daronch_2019]
- [Li et al 2019][research_li_gong_2019]
- [Li et al 2020][research_li_tang_2020]
- [Li et al 2021][research_li_wan_2021]
- [Li et al 2021][research_li_wang_2021]
- [Li et al 2022][research_li_sun_2022]
- [Li et al 2022][research_li_yuan_2022]
- [Li et al 2023][research_li_luo_2023]
- [Li et al 2023][research_li_yang_2023]
- [Li et al 2024][research_li_kou_2024]
- [Li et al 2024][research_li_qian_2024]
- [Li et al 2024][research_li_zhang_2024]
- [Li et al 2025][research_li_hu_2025]
- [Li et al 2025][research_li_li_2025]
- [Li et al 2025][research_li_shang_2025]
- [Li et al 2025][research_li_xiong_2025]
- [Li et al 2026][research_li_miranda_2026]
- [Li et al 2026][research_li_shen_2026]
- [Li et al 2026][research_li_wang_2026]
- [Li, Wesley W. and Pak, Chan-Gi 2014][research_liwesleyw_pakchangi_2014]
- [Liang and Ren 2018][research_liang_ren_2018]
- [Liao and Sun 1993][research_liao_sun_1993]
- [Libeskind et al 1973][research_libeskind_minecci_1973]
- [Librescu and Khdeir 1988][research_librescu_khdeir_1988]
- [Librescu and Simovich 1988][research_librescu_simovich_1988]
- [Librescu and Song 1992][research_librescu_song_1992]
- [Librescu and Thangjitham 1991][research_librescu_thangjitham_1991]
- [Lichota 2023][research_lichota_2023]
- [Liefer, Randall K. 1990][research_lieferrandallk_1990]
- [Lifshits and Ryzhov 1978][research_lifshits_ryzhov_1978]
- [Lijewski 1988][research_lijewski_1988]
- [Lin et al 1989][research_lin_lu_1989]
- [Lin et al 1994][research_lin_chin_1994]
- [Lind, Rick C. et al 1997][research_lindrickc_brennermartinj_1997]
- [Lindsay and Fikes 1976][research_lindsay_fikes_1976]
- [Lindsay and Jordan 1975][research_lindsay_jordan_1975]
- [Liu 2018][research_liu_2018]
- [Liu 2019][research_liu_2019]
- [Liu and Gao 2020][research_liu_gao_2020_b]
- [Liu and Sun 2016][research_liu_sun_2016]
- [Liu and Sun 2017][research_liu_sun_2017]
- [Liu and Wang 2019][research_liu_wang_2019]
- [Liu et al 2009][research_liu_liou_2009]
- [Liu et al 2015][research_liu_toropov_2015]
- [Liu et al 2017][research_liu_sun_2017_b]
- [Liu et al 2018][research_liu_an_2018]
- [Liu et al 2020][research_liu_gao_2020]
- [Liu et al 2021][research_liu_dong_2021]
- [Liu et al 2022][research_liu_sun_2022]
- [Liu et al 2023][research_liu_feng_2023]
- [Liu et al 2023][research_liu_zhang_2023]
- [Liu et al 2024][research_liu_ji_2024]
- [Liu et al 2025][research_liu_zheng_2025]
- [Liu et al 2026][research_liu_li_2026]
- [Liu et al 2026][research_liu_wang_2026]
- [Livne 2018][research_livne_2018]
- [Lock, W. P. et al 1975][research_lockwp_petersenwr_1975]
- [Loh 1986][research_loh_1986]
- [Loja et al 2017][research_loja_barbosa_2017]
- [Lokos, William A. 1990][research_lokoswilliama_1990]
- [Lombardi 1995][research_lombardi_1995]
- [Lombardi and Morelli 1994][research_lombardi_morelli_1994]
- [Lombardi and Vicini 1994][research_lombardi_vicini_1994]
- [Long et al 2021][research_long_mu_2021]
- [Loos and Springer 1983][research_loos_springer_1983]
- [Lottati 1985][research_lottati_1985]
- [Lottati 1987][research_lottati_1987]
- [Lottati 1988][research_lottati_1988]
- [Loughlan 2019][research_loughlan_2019]
- [Lovatt 1986][research_lovatt_1986]
- [Lovejoy, Andrew E. and Scotti, Stephen J. 2019][research_lovejoyandrewe_scottistephenj_2019]
- [Lu 1994][research_lu_1994]
- [Lu and Murthy 1990][research_lu_murthy_1990]
- [Lu et al 2018][research_lu_fang_2018]
- [Lu et al 2019][research_lu_ma_2019]
- [Luat T Nguyen et al 1980][research_luattnguyen_williampgilbert_1980]
- [Lucas 1978][research_lucas_1978]
- [Luo and Bao 1988][research_luo_bao_1988]
- [Lv et al 2019][research_lv_lei_2019]
- [Löser 1985][research_loser_1985]
- [Ma et al 2015][research_ma_guo_2015]
- [Ma et al 2025][research_ma_zhou_2025]
- [Mabboux et al 2024][research_mabboux_pommierbudinger_2024]
- [Mackall, D. A. et al 1988][research_mackallda_pickettmd_1988]
- [Mackall, Dale A. and Allen, James G. 1989][research_mackalldalea_allenjamesg_1989]
- [Mackall, Dale A. and Allen, James G. 1991][research_mackalldalea_allenjamesg_1991]
- [Magee and Taylor 1971][research_magee_taylor_1971]
- [Magliacano et al 2025][research_magliacano_tufano_2025]
- [Magness et al 1993][research_magness_robinson_1993]
- [Magnus and Yoshihara 1975][research_magnus_yoshihara_1975]
- [Mahapatra and Halbe 2024][research_mahapatra_halbe_2024]
- [Mahboub et al 2022][research_mahboub_rouabah_2022]
- [Mahgoub and El-Badawy 2022][research_mahgoub_elbadawy_2022]
- [Mahmood 2025][research_mahmood_2025]
- [Mahroni 2021][research_mahroni_2021]
- [Mahulkar 2010][research_mahulkar_2010]
- [Malcom 1969][research_malcom_1969]
- [Malcom, L. G. and Husband, J. H. 1976][research_malcomlg_husbandjh_1976]
- [Malekpour et al 2025][research_malekpour_abdali_2025]
- [Malik et al 2017][research_malik_akhtar_2017]
- [Mamedov et al 2018][research_mamedov_paryshev_2018]
- [Mamonova et al 2019][research_mamonova_soudakov_2019]
- [Mandal and Gu 2016][research_mandal_gu_2016]
- [Mann, M. J. and Mercer, C. E. 1985][research_mannmj_mercerce_1985]
- [Mann, M. J. and Mercer, C. E. 1986][research_mannmj_mercerce_1986]
- [Mann, M. J. et al 1983][research_mannmj_campbellrl_1983]
- [Mann, M. J. et al 1984][research_mannmj_campbellrl_1984]
- [Mansy and Faruque 2023][research_mansy_faruque_2023]
- [Mant 1972][research_mant_1972]
- [Manzoor et al 2016][research_manzoor_maqsood_2016]
- [Mao et al 2018][research_mao_dou_2018]
- [Mao et al 2019][research_mao_xie_2019]
- [Mao et al 2020][research_mao_li_2020]
- [Mar and Lin 1979][research_mar_lin_1979]
- [Marano et al 2022][research_marano_belardo_2022]
- [Marilyn E Ogburn et al 1991][research_marilyneogburn_johnvfoster_1991]
- [Marques et al 2017][research_marques_natarajan_2017]
- [Marqui et al 2017][research_marqui_bueno_2017]
- [Marr and Roderick 1975][research_marr_roderick_1975]
- [Martin 1978][research_martin_1978]
- [Martin Co Denver Co 1966][research_martincodenverco_1966]
- [Martín et al 2017][research_martin_pardo_2017]
- [Martínez-Heredia et al 2026][research_martinezheredia_fernandezprada_2026]
- [Maruyama et al 2024][research_maruyama_ogino_2024]
- [Marín and Graciani 2022][research_marin_graciani_2022]
- [Mason, M. L. and Capone, F. J. 1983][research_masonml_caponefj_1983]
- [Masuda et al 2016][research_masuda_shimosawa_2016]
- [Mateer, George C. et al 1987][research_mateergeorgec_seegmillerhlee_1987]
- [Mathur et al 2026][research_mathur_huang_2026]
- [Matrix cracking and stiffness 1985][research_matrix_cracking_1985]
- [Matsuki et al 2018][research_matsuki_nishiyama_2018]
- [Mayer et al 2016][research_mayer_prowe_2016]
- [McComb et al 1987][research_mccomb_hayduk_1987]
- [McCutchen 1980][research_mccutchen_1980]
- [McDonald 2001][research_mcdonald_2001]
- [McDonald and Farris 1964][research_mcdonald_farris_1964]
- [McGough et al 1974][research_mcgough_moses_1974]
- [McGurk et al 2024][research_mcgurk_stodieck_2024]
- [McIntosh et al 2024][research_mcintosh_mishra_2024]
- [McKeehen and Cord 1997][research_mckeehen_cord_1997]
- [McKillip 1991][research_mckillip_1991]
- [McKinney 1972][research_mckinney_1972]
- [McKlNNEY and DOLLYHlGH 1971][research_mcklnney_dollyhlgh_1971]
- [McMaster and Schenk 1974][research_mcmaster_schenk_1974]
- [Mcruer, D. et al 1986][research_mcruerd_johnstond_1986]
- [Mefford et al 1948][research_mefford_voss_1948]
- [Mehmed, Oral 1988][research_mehmedoral_1988]
- [Mei et al 2021][research_mei_wang_2021]
- [Meirovitch 1995][research_meirovitch_1995]
- [Memon et al 2021][research_memon_white_2021]
- [Menet et al 1993][research_menet_menart_1993]
- [Meng and Jiang 2025][research_meng_jiang_2025]
- [Menon and Yousefpor 1996][research_menon_yousefpor_1996]
- [Mertaugh 1998][research_mertaugh_1998]
- [Mhenni et al 2016][research_mhenni_choley_2016]
- [Micheli 2024][research_micheli_2024]
- [Micks 1950][research_micks_1950]
- [Mihaila-Andres et al 2019][research_mihailaandres_rosu_2019]
- [Mijovic 1985][research_mijovic_1985]
- [Miller 1965][research_miller_1965]
- [Miller 1986][research_miller_1986]
- [Miller and Clark 1965][research_miller_clark_1965]
- [Miller et al 1983][research_miller_wykes_1983]
- [Miner, D. D. and Gloss, B. B. 1975][research_minerdd_glossbb_1975]
- [Miranda and Bidinotto 2025][research_miranda_bidinotto_2025]
- [Miranda et al 2025][research_miranda_li_2025]
- [Missoum 2012][research_missoum_2012]
- [Mitchell 1961][research_mitchell_1961]
- [Mitchell et al 1980][research_mitchell_myers_1980]
- [Miura, Hirokazu and Neill, Douglas J. 1992][research_miurahirokazu_neilldouglasj_1992]
- [Miyasato 1992][research_miyasato_1992]
- [Miyazawa 1993][research_miyazawa_1993]
- [Moarref and Rodrigues 2015][research_moarref_rodrigues_2015]
- [Mochizuki and Yamada 2018][research_mochizuki_yamada_2018]
- [Modi and Slater 1983][research_modi_slater_1983]
- [Modi and Slater 1994][research_modi_slater_1994]
- [Moes, Timothy R. et al 2000][research_moestimothyr_noffzgregoryk_2000]
- [Moes, Timothy R. et al 2003][research_moestimothyr_smithmarks_2003]
- [Mohanty and Chhotaray 1979][research_mohanty_chhotaray_1979]
- [Monaghan, R. C. 1981][research_monaghanrc_1981]
- [Montgomery 1972][research_montgomery_1972]
- [Montgomery and Caglayan 1976][research_montgomery_caglayan_1976]
- [Montgomery and Price 1976][research_montgomery_price_1976]
- [Montgomery, R. C. and Price, D. B. 1974][research_montgomeryrc_pricedb_1974]
- [Moon 1996][research_moon_1996]
- [Moore 1972][research_moore_1972]
- [Moore, N. R. et al 1992][research_moorenr_ebbelerdh_1992]
- [Moreira et al 2024][research_moreira_moleiro_2024]
- [Morino and Obayashi 2015][research_morino_obayashi_2015]
- [Morita and Matsukawa 1995][research_morita_matsukawa_1995]
- [Morozov and Janschek 2016][research_morozov_janschek_2016]
- [Morris 1977][research_morris_1977]
- [Morrison and White 1976][research_morrison_white_1976]
- [Motta et al 2019][research_motta_malzacher_2019]
- [Moul, Martin T and Wineman, Andrew R 1952][research_moulmartint_winemanandrewr_1952]
- [Moul, Martin T. and Brown, Lawrence W. 1959][research_moulmartint_brownlawrencew_1959]
- [Mourey, D. J. 1979][research_moureydj_1979]
- [Mu et al 2022][research_mu_huang_2022]
- [Mu et al 2026][research_mu_huang_2026]
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
- [NACA Conference on Aerodynamic 1949][research_naca_conference_1949]
- [NACA Conference on Aircraft 1957][research_naca_conference_1957]
- [Nagabhushan 1991][research_nagabhushan_1991]
- [Naganarayana and Atluri 1995][research_naganarayana_atluri_1995]
- [Nagaraja et al 1982][research_nagaraja_lakin_1982]
- [Nagib and Wigeland 1977][research_nagib_wigeland_1977]
- [Nagy 1979][research_nagy_1979]
- [Nakamura 1982][research_nakamura_1982]
- [Nakamura and Takesue 1990][research_nakamura_takesue_1990]
- [Nam et al 2000][research_nam_chen_2000]
- [Namani Koureh et al 2026][research_namanikoureh_shahverdi_2026]
- [Napolitano, Marcello R. 1996][research_napolitanomarcellor_1996]
- [Napolitano, Marcello R. and Spagnuolo, Joelle M. 1993][research_napolitanomarcellor_spagnuolojoellem_1993]
- [Narendra and Tripathi 1973][research_narendra_tripathi_1973]
- [Narimani et al 2025][research_narimani_haddadpour_2025]
- [nath and ana 2017][research_nath_ana_2017]
- [Nazarenko and Nevezhina 1972][research_nazarenko_nevezhina_1972]
- [Nazeer et al 2021][research_nazeer_wang_2021]
- [Neal and Smith 1970][research_neal_smith_1970]
- [Negaard 1980][research_negaard_1980]
- [Negahban et al 2024][research_negahban_bashir_2024]
- [Nelson and Mouch 1978][research_nelson_mouch_1978]
- [Neu and Huang 1973][research_neu_huang_1973]
- [Neville et al 1992][research_neville_marois_1992]
- [Newton and Kroo 2025][research_newton_kroo_2025]
- [Nguyen et al 2016][research_nguyen_olaru_2016]
- [Nguyen et al 2018][research_nguyen_reynolds_2018]
- [Nguyen et al 2021][research_nguyen_lowenberg_2021]
- [Nguyen, L. T. et al 1979][research_nguyenlt_gilbertwp_1979]
- [Nguyen, Luat T. and Gilert, William P. 1990][research_nguyenluatt_gilertwilliamp_1990]
- [Nguyen, Nhan and James Urnes, Sr. 2012][research_nguyennhan_jamesurnessr_2012]
- [Nguyen, Nhan et al 2015][research_nguyennhan_kaulupender_2015]
- [Ni et al 2023][research_ni_li_2023]
- [Nibbelink, Bruce D. and Peters, David A. 1993][research_nibbelinkbruced_petersdavida_1993]
- [Niblett 1986][research_niblett_1986]
- [Niblett 1988][research_niblett_1988]
- [Nicholas, W. U. et al 1984][research_nicholaswu_navillegl_1984]
- [Nicolaides 1971][research_nicolaides_1971]
- [Niehaus 1962][research_niehaus_1962]
- [Nihtilä 1989][research_nihtila_1989]
- [Nikrad et al 2015][research_nikrad_asadi_2015]
- [Nissen 2009][research_nissen_2009]
- [Nitschke et al 2019][research_nitschke_vincenti_2019]
- [Nitzsche and Breitbach 1994][research_nitzsche_breitbach_1994]
- [Niu et al 2026][research_niu_li_2026]
- [Niven 1977][research_niven_1977]
- [Nixon, Mark W. et al 1999][research_nixonmarkw_piatakdavidj_1999]
- [Noll et al 1984][research_noll_eastep_1984]
- [Nonnenmacher and Jones 2016][research_nonnenmacher_jones_2016]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]
- [Norton 1990][research_norton_1990]
- [Norwood 1992][research_norwood_1992]
- [Ntantis and Xezonakis 2024][research_ntantis_xezonakis_2024]
- [Numerical and Experimental Determination 2019][research_numerical_and_2019]
- [Numerical Study of Geometrical 2023][research_numerical_study_2023]
- [O'Donnell, James R., Jr. et al 2002][research_odonnelljamesrjr_davisgaryt_2002]
- [Oberkampf and Nicolaides 1971][research_oberkampf_nicolaides_1971]
- [Ochi and Kanai 1995][research_ochi_kanai_1995]
- [ODonnell, James R., Jr. et al 1999][research_odonnelljamesrjr_andrewsstephenf_1999]
- [Oelker and Hummel 1989][research_oelker_hummel_1989]
- [Ogunvoul et al 2017][research_ogunvoul_balanchuk_2017]
- [Ohkawa 1985][research_ohkawa_1985]
- [Ohkawa 1986][research_ohkawa_1986]
- [Ohkuma 1993][research_ohkuma_1993]
- [Ohta et al 1979][research_ohta_nikiforuk_1979]
- [Ohta et al 1982][research_ohta_nikiforuk_1982]
- [Okumoto and Elsanker 1973][research_okumoto_elsanker_1973]
- [Oland et al 2016][research_oland_andersen_2016]
- [Olhan and Behera 2023][research_olhan_behera_2023]
- [Olsen 1966][research_olsen_1966]
- [Olson, Glenn O. 1982][research_olsonglenno_1982]
- [Operational Technologies Corp San Antonio Tx 1996][research_operationaltechnologiescorpsanantoniotx_1996]
- [Orkwis 1995][research_orkwis_1995]
- [Osder et al 1976][research_osder_mossman_1976]
- [Osipov 2016][research_osipov_2016]
- [Osipov 2017][research_osipov_2017]
- [Ostheimer and Giguere 1963][research_ostheimer_giguere_1963]
- [Othman et al 2019][research_othman_silva_2019]
- [Otsuka and Makihara 2017][research_otsuka_makihara_2017]
- [Ouyang and Lin 2017][research_ouyang_lin_2017]
- [Ouyang et al 2021][research_ouyang_zeng_2021]
- [Ouzts, Peter J. et al 2009][research_ouztspeterj_solowaydonaldi_2009]
- [Over 136 000 flying 1981][research_over_136_1981]
- [Oyibo 1984][research_oyibo_1984]
- [Ozdil and Carlsson 1992][research_ozdil_carlsson_1992]
- [Packard et al 2009][research_packard_seiler_2009]
- [Pagano 1974][research_pagano_1974]
- [Palframan et al 2019][research_palframan_fry_2019]
- [Palm, Tod et al 2000][research_palmtod_mahlermary_2000]
- [Pan and Cheng 1995][research_pan_cheng_1995]
- [Pan and Huang 2019][research_pan_huang_2019]
- [Papadales and Basil S. 1979][research_papadales_basils_1979]
- [Papirno 1977][research_papirno_1977]
- [Park et al 2017][research_park_jung_2017]
- [Parker and Simonson 1982][research_parker_simonson_1982]
- [Parker and Simonson 1982][research_parker_simonson_1982_b]
- [Parker and Simonson 1982][research_parker_simonson_1982_c]
- [Parthiv N Shah et al 2023][research_parthivnshah_ericlblades_2023]
- [Passive wing/store flutter suppression 1982][research_passive_wing_store_1982]
- [Patartics et al 2022][research_patartics_liptak_2022]
- [Pate 1964][research_pate_1964]
- [Pate and Deitering 1963][research_pate_deitering_1963]
- [Patel et al 2022][research_patel_kumar_2022]
- [Patrick C Murphy 1999][research_patrickcmurphy_1999]
- [Patterson and Grenestedt 2018][research_patterson_grenestedt_2018]
- [Paulk and Anderson 1976][research_paulk_anderson_1976]
- [Paulson, J. W., Jr. and Thomas, J. L. 1978][research_paulsonjwjr_thomasjl_1978]
- [Paulson, J. W., Jr. and Thomas, J. L. 1979][research_paulsonjwjr_thomasjl_1979_b]
- [Paulson, J. W., Jr. et al 1979][research_paulsonjwjr_thomasjl_1979]
- [Payton 2017][research_payton_2017]
- [Pearson, Henry A and Aiken, William S , Jr 1944][research_pearsonhenrya_aikenwilliamsjr_1944]
- [Peled, U. and Powell, J. D. 1978][research_peledu_powelljd_1978]
- [Pellerin 1988][research_pellerin_1988]
- [Pelykh and Andryushchenko 2024][research_pelykh_andryushchenko_2024]
- [Pena, Francisco 2020][research_penafrancisco_2020]
- [Pena, Francisco et al 2018][research_penafrancisco_martinsbenjamin_2018]
- [Pendem 2023][research_pendem_2023]
- [Pendleton et al 1995][research_pendleton_moster_1995]
- [Peng et al 1994][research_peng_zhang_1994]
- [Peng et al 2026][research_peng_cao_2026]
- [Perkins et al 1977][research_perkins_jr_1977]
- [Perry and Rievley 1961][research_perry_rievley_1961]
- [Perry, B., III 1976][research_perrybiii_1976]
- [Perry, B., III 1982][research_perrybiii_1982]
- [Persoon et al 1980][research_persoon_roos_1980]
- [Persoon et al 1984][research_persoon_horsten_1984]
- [Peters, David A. 1988][research_petersdavida_1988]
- [Petersen, K. L. 1981][research_petersenkl_1981]
- [Petre and Ashley 1976][research_petre_ashley_1976]
- [Petterssen 1953][research_petterssen_1953]
- [Pfeifle and Fichter 2023][research_pfeifle_fichter_2023]
- [Pham 2022][research_pham_2022]
- [Phan 2020][research_phan_2020]
- [Philippidis, 1994][research_philippidis_1994]
- [Phuekpan et al 2025][research_phuekpan_khammee_2025]
- [Piao et al 2019][research_piao_zhang_2019]
- [Picon and Alarcon 1978][research_picon_alarcon_1978]
- [Pidaparti 1993][research_pidaparti_1993]
- [Pidaparti and Yang 1993][research_pidaparti_yang_1993]
- [Pizzoli et al 2022][research_pizzoli_saltari_2022]
- [Place et al 1974][research_place_altmann_1974]
- [Plaetschke et al 1982][research_plaetschke_mulder_1982]
- [Platus 1980][research_platus_1980]
- [Plotkin 1978][research_plotkin_1978]
- [Plyako 1977][research_plyako_1977]
- [Poll 1986][research_poll_1986]
- [Polyester, fibreglass-reinforced composite laminate 1978][research_polyester_fibreglass_reinforced_1978]
- [Poole et al 2022][research_poole_allen_2022]
- [Poole et al 2026][research_poole_allen_2026]
- [Portapas and Cooke 2020][research_portapas_cooke_2020]
- [Posingies 1979][research_posingies_1979]
- [Pourtakdoust and Khodabakhsh 2026][research_pourtakdoust_khodabakhsh_2026]
- [Poussot-Vassal et al 2017][research_poussotvassal_demourant_2017]
- [Powell, Richard W. 1993][research_powellrichardw_1993]
- [Powers 1982][research_powers_1982]
- [Powers, B. G. 1980][research_powersbg_1980]
- [Prasad and Pešek 2018][research_prasad_pesek_2018]
- [Prasad et al 1967][research_prasad_nematnasser_1967]
- [Prasannakumar et al 2024][research_prasannakumar_sudhi_2024]
- [Pratama 2021][research_pratama_2021]
- [Pritt 1980][research_pritt_1980]
- [Property changes of a 1981][research_property_changes_1981]
- [Prototype Digital Flight Control 1986][research_prototype_digital_1986]
- [Przekop, Adam and Jegley, Dawn C. 2014][research_przekopadam_jegleydawnc_2014_b]
- [Przekop, Adam et al 2014][research_przekopadam_jegleydawnc_2014]
- [Pusch et al 2019][research_pusch_knoblach_2019]
- [Pushtaev 1989][research_pushtaev_1989]
- [Puthisikamani et al 2023][research_puthisikamani_sreenivasaraja_2023]
- [Putnam, T. W. 1983][research_putnamtw_1983]
- [Putnam, T. W. 1984][research_putnamtw_1984]
- [Putnam, T. W. 1984][research_putnamtw_1984_b]
- [Putnam, T. W. et al 1986][research_putnamtw_petersenkl_1986]
- [Qi and Zhao 2020][research_qi_zhao_2020]
- [Qi et al 2026][research_qi_yuan_2026]
- [Qian et al 2025][research_qian_lu_2025]
- [Qian et al 2025][research_qian_xinhui_2025]
- [Qin et al 2017][research_qin_liu_2017]
- [Qu and Annaswamy 2016][research_qu_annaswamy_2016]
- [Qu and Li 2022][research_qu_li_2022]
- [Radetskaya 2022][research_radetskaya_2022]
- [Radford, R. C. et al 1980][research_radfordrc_smithr_1980]
- [Raghav and Komerath 2015][research_raghav_komerath_2015]
- [Rais-Rohani, M. et al 1992][research_raisrohanim_haftkart_1992]
- [Rais-Rohani, Masoud 1994][research_raisrohanimasoud_1994]
- [Rais-Rohani, Masound 1999][research_raisrohanimasound_1999]
- [Rajpal et al 2019][research_rajpal_kassapoglou_2019]
- [Rajpal et al 2021][research_rajpal_mitrotta_2021]
- [Ramamoorthy 1992][research_ramamoorthy_1992]
- [Ranaudo, Richard J. et al 2000][research_ranaudorichardj_ratvaskythomasp_2000]
- [Raney, David L. 1987][research_raneydavidl_1987]
- [Rao 1975][research_rao_1975]
- [Rao and Padmanabhan 2019][research_rao_padmanabhan_2019]
- [Rao and Uma Maheswara Rao 1992][research_rao_umamaheswararao_1992]
- [Rao et al 1973][research_rao_hofer_1973]
- [Raouf 1994][research_raouf_1994]
- [Raper 1991][research_raper_1991]
- [Rapoff, Andrew J. et al 1990][research_rapoffandrewj_dillharoldd_1990]
- [Rate sensitivity of Mode 1988][research_rate_sensitivity_1988]
- [Rath and Fichter 2020][research_rath_fichter_2020]
- [Ray, E. J. et al 1972][research_rayej_mckinneylw_1972]
- [Ray, E. J. et al 1973][research_rayej_mckinneylw_1973]
- [Rea et al 2017][research_rea_pecora_2017]
- [Rea et al 2018][research_rea_pecora_2018]
- [Reader 1976][research_reader_1976]
- [Reca Luque et al 2023][research_recaluque_aguilartorres_2023]
- [Rediess, H. A. and Szalai, K. J. 1975][research_rediessha_szalaikj_1975]
- [Reding and Ericsson 1977][research_reding_ericsson_1977]
- [Reeder 1958][research_reeder_1958]
- [Reid et al 1994][research_reid_rajagopal_1994]
- [Reinbold et al 2026][research_reinbold_breitsamter_2026]
- [Ren et al 2022][research_ren_zhang_2022]
- [Repa et al 1977][research_repa_alexandridis_1977]
- [Research and Design of 2022][research_research_and_2022]
- [Reyes et al 2019][research_reyes_climent_2019]
- [Rhodes, M. D. and Selberg, B. P. 1982][research_rhodesmd_selbergbp_1982]
- [Rich, M. J. et al 1974][research_richmj_ridgleygf_1974]
- [Richards 1979][research_richards_1979]
- [Richwine, David M. and Fisher, David F. 1991][research_richwinedavidm_fisherdavidf_1991]
- [Rickard, W. W. 1978][research_rickardww_1978]
- [Ricketts, R. H. and Doggett, R. V., Jr. 1980][research_rickettsrh_doggettrvjr_1980]
- [Ricketts, R. H. et al 1983][research_rickettsrh_sandfordmc_1983]
- [Ricketts, R. H. et al 1983][research_rickettsrh_watsonjj_1983]
- [Ried 1986][research_ried_1986]
- [Riefe 1946][research_riefe_1946]
- [Rigatos 2021][research_rigatos_2021]
- [Rimer et al 1984][research_rimer_chipman_1984]
- [Rimer et al 1986][research_rimer_chipman_1986]
- [Rimer, M. et al 1984][research_rimerm_chipmanr_1984]
- [Ringertz 1994][research_ringertz_1994]
- [Rising, J. J. et al 1984][research_risingjj_daviswj_1984]
- [Rittenhouse 1959][research_rittenhouse_1959]
- [Rizzetta 1977][research_rizzetta_1977]
- [Rizzetta 1979][research_rizzetta_1979]
- [Rizzetta and Visbal 2016][research_rizzetta_visbal_2016]
- [Roberts 1986][research_roberts_1986]
- [Roberts et al 1966][research_roberts_smith_1966]
- [Roberts, P. A. et al 1977][research_robertspa_swaimrl_1977]
- [Robinson 2004][research_robinson_2004]
- [Robotics 2024][research_robotics_2024]
- [Rockwell 1994][research_rockwell_1994]
- [Rodden 1981][research_rodden_1981]
- [Rodden 1984][research_rodden_1984]
- [Rodden 1989][research_rodden_1989]
- [Rodden 1989][research_rodden_1989_b]
- [Rodden and Bellinger 1982][research_rodden_bellinger_1982]
- [Rodemich and Andrew 1965][research_rodemich_andrew_1965]
- [Rogalski 2018][research_rogalski_2018]
- [Rogersten et al 2013][research_rogersten_xu_2013]
- [Rohella and Chatterjee 1979][research_rohella_chatterjee_1979]
- [Rokhsaz and Selberg 1990][research_rokhsaz_selberg_1990]
- [Rom and Lamar 1992][research_rom_lamar_1992]
- [Romano et al 2019][research_romano_ciminello_2019]
- [Ronfle-Nadaud 2009][research_ronflenadaud_2009]
- [Rongrong et al 2018][research_rongrong_zhengyin_2018]
- [Rooney, R. H. et al 1982][research_rooneyrh_chungjc_1982]
- [Roos et al 1989][research_roos_mushlin_1989]
- [Rosa et al 2023][research_rosa_pouca_2023]
- [Roscoe et al 1975][research_roscoe_eisele_1975]
- [Rose and Seginer 1978][research_rose_seginer_1978]
- [Rosen, Bruce S. 1988][research_rosenbruces_1988]
- [Roskam, J. and Lan, C. 1973][research_roskamj_lanc_1973]
- [Roskam, J. et al 1972][research_roskamj_lanc_1972]
- [Rowley 2008][research_rowley_2008]
- [Roylance 1980][research_roylance_1980]
- [Ruhlin et al 1983][research_ruhlin_rauch_1983]
- [Rumble 1987][research_rumble_1987]
- [Runkel et al 2018][research_runkel_fasel_2018]
- [Runyan et al 1952][research_runyan_cunningham_1952]
- [Ruo et al 1985][research_ruo_malone_1985]
- [Ruscheweyh 1983][research_ruscheweyh_1983]
- [Rutkowski 1979][research_rutkowski_1979]
- [Ryder and Walker 1976][research_ryder_walker_1976]
- [Sabatini et al 2026][research_sabatini_coppotelli_2026]
- [Sachs 1975][research_sachs_1975]
- [Sachs 1977][research_sachs_1977]
- [Sachs 1979][research_sachs_1979]
- [Sachs et al 1956][research_sachs_muvdi_1956]
- [Saddington et al 2016][research_saddington_thangamani_2016]
- [Saderla et al 2016][research_saderla_dhayalan_2016]
- [Sadoff, Melvin et al 1961][research_sadoffmelvin_mcfaddennormanm_1961]
- [Saetti et al 2020][research_saetti_horn_2020]
- [Saheby et al 2026][research_saheby_jialu_2026]
- [Sahu et al 2000][research_sahu_heavey_2000]
- [Sahyoun et al 2026][research_sahyoun_boose_2026]
- [Salichon et al 1994][research_salichon_guy_1994]
- [Sally A Viken et al 2022][research_sallyaviken_craigahunter_2022]
- [Saltzman, Edwin J. et al 1994][research_saltzmanedwinj_hicksjohnw_1994]
- [Sammonds, Robert I. et al 1982][research_sammondsroberti_mcneillwaltere_1982]
- [Samputh et al 2024][research_samputh_moey_2024]
- [Santich 1985][research_santich_1985]
- [Saporito et al 2023][research_saporito_daronch_2023]
- [Saraeian and Shirazi 2022][research_saraeian_shirazi_2022]
- [Saric 1997][research_saric_1997]
- [Sato 1973][research_sato_1973]
- [Sawyer, J. W. 1976][research_sawyerjw_1976]
- [Schewe and Mai 2018][research_schewe_mai_2018]
- [Schildkamp et al 2023][research_schildkamp_chang_2023]
- [Schmidt 2016][research_schmidt_2016]
- [Schmidt et al 2025][research_schmidt_lisoski_2025]
- [Schmidt, David K. and Schierman, John D. 1990][research_schmidtdavidk_schiermanjohnd_1990]
- [Schneider 1976][research_schneider_1976]
- [Schpey 1980][research_schpey_1980]
- [Schreadley 1977][research_schreadley_1977]
- [Schroeder, Jeffery A. et al 2001][research_schroederjefferya_chungwilliamwy_2001]
- [Schueltke and Stumpf 2017][research_schueltke_stumpf_2017]
- [Schuster 1995][research_schuster_1995]
- [Schuster, David M. and Edwards, John W. 2004][research_schusterdavidm_edwardsjohnw_2004]
- [Schwanz 1972][research_schwanz_1972]
- [Schwerdt et al 2023][research_schwerdt_maroldt_2023]
- [Sciuva 1992][research_sciuva_1992]
- [Scordamaglia et al 2025][research_scordamaglia_mattei_2025]
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
- [Sengupta and Ferris 1973][research_sengupta_ferris_1973]
- [Seraj and Ganesan 2018][research_seraj_ganesan_2018]
- [Seyoung 1990][research_seyoung_1990]
- [Shafer, M. F. 1980][research_shafermf_1980]
- [Shafer, M. F. et al 1983][research_shafermf_smithre_1983]
- [Shafer, M. F. et al 1984][research_shafermf_smithre_1984]
- [Shafer, Mary F. and Steinmetz, Paul 2001][research_shafermaryf_steinmetzpaul_2001]
- [Shafer, Mary F. and Steinmetz, Paul 2001][research_shafermaryf_steinmetzpaul_2001_b]
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
- [Sharp and Wilson 1990][research_sharp_wilson_1990]
- [Sharqi and Cesnik 2023][research_sharqi_cesnik_2023]
- [Shawki and Mashhour 1974][research_shawki_mashhour_1974]
- [Shearwood et al 2020][research_shearwood_nabawy_2020]
- [Sheldon 1967][research_sheldon_1967]
- [Shen and Chen 2023][research_shen_chen_2023]
- [Shen et al 2021][research_shen_huang_2021]
- [Shen et al 2022][research_shen_chang_2022]
- [Shepheard 1965][research_shepheard_1965]
- [Sherrer et al 1981][research_sherrer_hertz_1981]
- [Shi and Bezine 1988][research_shi_bezine_1988]
- [Shi et al 2018][research_shi_tan_2018]
- [Shi et al 2019][research_shi_lyu_2019]
- [Shi et al 2025][research_shi_gao_2025]
- [Shi et al 2026][research_shi_gao_2026]
- [Shiau and Chang 1991][research_shiau_chang_1991]
- [Shibahata et al 1993][research_shibahata_shimada_1993]
- [Shields and Cook 1971][research_shields_cook_1971]
- [Shirk et al 1986][research_shirk_hertz_1986]
- [Shladover 1995][research_shladover_1995]
- [Shmilovich and Princen 2026][research_shmilovich_princen_2026]
- [Shmilovich et al 2026][research_shmilovich_yadlin_2026]
- [Shneen 2026][research_shneen_2026]
- [Shoales and Fawaz 2004][research_shoales_fawaz_2004]
- [Short 1995][research_short_1995]
- [Shrivastava and Mohite 2015][research_shrivastava_mohite_2015]
- [Shrivastava et al 2020][research_shrivastava_tilala_2020]
- [Shrivastava, P. C. 1987][research_shrivastavapc_1987]
- [Shyprykevich, P. 1979][research_shyprykevichp_1979]
- [Siem and Murray 1997][research_siem_murray_1997]
- [Silton and Fresconi 2015][research_silton_fresconi_2015]
- [Silton et al 2014][research_silton_fresconi_2014]
- [Silva, Walter A. and Bennett, Robert M. 1990][research_silvawaltera_bennettrobertm_1990]
- [Silva-Leon and Cioncolini 2020][research_silvaleon_cioncolini_2020]
- [Simbuerger et al 2022][research_simbuerger_raveh_2022]
- [Simmons 2023][research_simmons_2023]
- [Simpson 1988][research_simpson_1988]
- [Sims, Robert et al 1989][research_simsrobert_mccrossonpaul_1989]
- [Sineglazov 2015][research_sineglazov_2015]
- [Singh and Dwivedi 2022][research_singh_dwivedi_2022]
- [Singh and Raisinghani 1993][research_singh_raisinghani_1993]
- [Singh et al 2016][research_singh_brown_2016]
- [Sitz, Joel R. and Vernon, Todd H. 1990][research_sitzjoelr_vernontoddh_1990]
- [Siwowski et al 2018][research_siwowski_kulpa_2018]
- [Sizlo, T. R. et al 1979][research_sizlotr_bergra_1979]
- [SKF divests fly-by-wire business 2016][research_skf_divests_2016]
- [Sliwa, S. M. 1980][research_sliwasm_1980]
- [Smeltzer et al 1983][research_smeltzer_durston_1983]
- [Smetana 1973][research_smetana_1973]
- [Smith 1991][research_smith_1991]
- [Smith 1993][research_smith_1993]
- [Smith 2025][research_smith_2025]
- [Smith and Geddes 1979][research_smith_geddes_1979]
- [Smith and Meyer 1987][research_smith_meyer_1987]
- [Smith et al 1971][research_smith_hammer_1971]
- [Smith et al 2001][research_smith_komerath_2001]
- [Smith, J. W. 1979][research_smithjw_1979]
- [Smith, J. W. and Berry, D. T. 1975][research_smithjw_berrydt_1975]
- [Smith, Rogers E. and Schroeder, Kurt C. 1986][research_smithrogerse_schroederkurtc_1986]
- [Snyder 1950][research_snyder_1950]
- [Snyder et al 1992][research_snyder_schipper_1992]
- [Sobieczky 1984][research_sobieczky_1984]
- [Soleymani and Arani 2019][research_soleymani_arani_2019]
- [Soneda et al 2022][research_soneda_tsushima_2022]
- [Song and Huang 2022][research_song_huang_2022]
- [Song et al 2016][research_song_zhang_2016]
- [Soovere 1982][research_soovere_1982]
- [Soria 2006][research_soria_2006]
- [Sottorf, W. 1949][research_sottorfw_1949]
- [Space radiation effects on 1987][research_space_radiation_1987]
- [Speyer 2003][research_speyer_2003]
- [Spiker 1964][research_spiker_1964]
- [Spillman and Ridgely 1995][research_spillman_ridgely_1995]
- [Srinathkumar 2015][research_srinathkumar_2015]
- [Stagliano and Mente 1979][research_stagliano_mente_1979]
- [Stainback 2001][research_stainback_2001]
- [Stalford 1979][research_stalford_1979]
- [Stanewsky and Little 1971][research_stanewsky_little_1971]
- [Stanford 2016][research_stanford_2016]
- [Stanford 2016][research_stanford_2016_b]
- [Stanford 2017][research_stanford_2017]
- [Stanford 2019][research_stanford_2019]
- [Stanford, Bret K. and Jutte, Christine V. 2014][research_stanfordbretk_juttechristinev_2014]
- [Stanford, Bret K. et al 2015][research_stanfordbretk_wiesemancarold_2015]
- [Stange 1959][research_stange_1959]
- [Stanton and Crain 1980][research_stanton_crain_1980]
- [Stark 1989][research_stark_1989]
- [Stauffer, W. A. and James, A. M. 1978][research_staufferwa_jamesam_1978]
- [Steger and Bailey 1980][research_steger_bailey_1980]
- [Steinmetz, G. G. et al 1972][research_steinmetzgg_parrishrv_1972]
- [Stephan et al 2023][research_stephan_stumpf_2023]
- [Sternberg et al 1994][research_sternberg_traven_1994]
- [Stewart et al 1975][research_stewart_dominick_1975]
- [Stinton 1985][research_stinton_1985]
- [Stirling 1983][research_stirling_1983]
- [Stodieck et al 2015][research_stodieck_cooper_2015]
- [Stodieck et al 2017][research_stodieck_cooper_2017]
- [Stolarik 2007][research_stolarik_2007]
- [Stoll, F. and Koenig, D. G. 1983][research_stollf_koenigdg_1983]
- [Stollery 1992][research_stollery_1992]
- [Stottier 1995][research_stottier_1995]
- [Strand and Levinsky 1969][research_strand_levinsky_1969]
- [Streb 1973][research_streb_1973]
- [Streit et al 2015][research_streit_wedler_2015]
- [Strength of Prestressed Concrete 1978][research_strength_of_1978]
- [Strike and W. T. 1982][research_strike_wt_1982]
- [Structural Aspects of Flexible 2000][research_structural_aspects_2000]
- [Study of advanced composite 1978][research_study_of_1978]
- [Sugino et al 2019][research_sugino_harada_2019]
- [Sugumaran 2024][research_sugumaran_2024]
- [Suh, Peter M. et al 2014][research_suhpeterm_conyershowardj_2014]
- [Suh, Peter M. et al 2015][research_suhpeterm_conyershowardjason_2015]
- [Suikat, Reiner et al 1987][research_suikatreiner_donaldsonkent_1987]
- [Sulaeman et al 2017][research_sulaeman_abdullah_2017]
- [Sullivan 2002][research_sullivan_2002]
- [Sun 2015][research_sun_2015]
- [Sun 2024][research_sun_2024]
- [Sun and Yoon 1988][research_sun_yoon_1988]
- [Sun et al 2020][research_sun_shi_2020]
- [Sun et al 2020][research_sun_wang_2020]
- [Sun et al 2022][research_sun_han_2022]
- [Sun et al 2024][research_sun_xu_2024]
- [Sun et al 2025][research_sun_luo_2025]
- [Sun et al 2026][research_sun_chen_2026]
- [Sun et al 2026][research_sun_zhang_2026]
- [Supercritical Wing Tested 1971][research_supercritical_wing_1971]
- [Suryawanshi and Ghosh 2015][research_suryawanshi_ghosh_2015]
- [Svoboda et al 2023][research_svoboda_hengstermovric_2023]
- [Swaim 1961][research_swaim_1961]
- [Swaim and Yen 1979][research_swaim_yen_1979]
- [Swain et al 2019][research_swain_adhikari_2019]
- [Switzky 1965][research_switzky_1965]
- [Syed et al 2022][research_syed_moshtaghzadeh_2022]
- [Szalai, K. J. 1975][research_szalaikj_1975]
- [Szalai, K. J. 1976][research_szalaikj_1976]
- [Szalai, K. J. et al 1976][research_szalaikj_fellemanpg_1976]
- [Szalai, K. J. et al 1978][research_szalaikj_jarviscr_1978]
- [Szklarski and Głębocki 2025][research_szklarski_glebocki_2025]
- [Szmulewitz 2011][research_szmulewitz_2011]
- [Szmulewitz 2012][research_szmulewitz_2012]
- [Szollosi and Baranyi 2016][research_szollosi_baranyi_2016]
- [Szymanski et al 2025][research_szymanski_alstrom_2025]
- [Tabassum and Bai 2022][research_tabassum_bai_2022]
- [Tahani et al 2017][research_tahani_masdari_2017]
- [Tahir et al 2026][research_tahir_maqsood_2026]
- [Tai et al 2023][research_tai_wang_2023]
- [Taimoor and Aijun 2019][research_taimoor_aijun_2019]
- [Taira 2014][research_taira_2014]
- [Talbot and Gerald L. 1992][research_talbot_geraldl_1992]
- [Tameh et al 2018][research_tameh_sawan_2018]
- [Tan 1988][research_tan_1988]
- [Tan et al 2021][research_tan_wang_2021]
- [Tan et al 2022][research_tan_zhang_2022]
- [Tang 1989][research_tang_1989]
- [Tang and Liu 2018][research_tang_liu_2018]
- [Tang et al 2016][research_tang_wu_2016]
- [Tang et al 2017][research_tang_wu_2017]
- [Tang et al 2018][research_tang_chen_2018]
- [Tang et al 2020][research_tang_chen_2020]
- [Tang et al 2025][research_tang_tang_2025]
- [Tangler 1979][research_tangler_1979]
- [Tantaroudas and Karachalios 2026][research_tantaroudas_karachalios_2026]
- [Tao and Sun 2016][research_tao_sun_2016]
- [Targoff 1947][research_targoff_1947]
- [Targoff 1947][research_targoff_1947_b]
- [Tate 1992][research_tate_1992]
- [Taufik and Qasem 2025][research_taufik_qasem_2025]
- [Taylor 1959][research_taylor_1959]
- [Taylor 2009][research_taylor_2009]
- [Teel 1999][research_teel_1999]
- [Teel 1999][research_teel_1999_b]
- [Telionis 1995][research_telionis_1995]
- [Telionis 2001][research_telionis_2001]
- [Teper and Stapleford 1966][research_teper_stapleford_1966]
- [Terekhov 2022][research_terekhov_2022]
- [Tewar et al 2015][research_tewar_myers_2015]
- [Tharp and Zhang 1994][research_tharp_zhang_1994]
- [The viscoelastic behaviour of 1981][research_the_viscoelastic_1981]
- [The Voisin “Canard” Biplane 1911][research_the_voisin_1911]
- [Theerthamalai et al 2025][research_theerthamalai_mukesh_2025]
- [Theerthamalai et al 2026][research_theerthamalai_ramanan_2026]
- [Theis et al 2020][research_theis_pfifer_2020]
- [Theodore et al 2020][research_theodore_malpica_2020]
- [Thermal damage effects and 1989][research_thermal_damage_1989]
- [Thermal expansion and swelling 1981][research_thermal_expansion_1981]
- [Thomas et al 1978][research_thomas_paulson_1978]
- [Thompson 1992][research_thompson_1992]
- [Thompson et al 2002][research_thompson_bannon_2002]
- [Thompson et al 2005][research_thompson_walls_2005]
- [Thomson and Caiafa 1982][research_thomson_caiafa_1982]
- [Tian et al 2016][research_tian_yang_2016]
- [Tian et al 2026][research_tian_wang_2026]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979_b]
- [Ting et al 2023][research_ting_mesbahi_2023]
- [Ting et al 2026][research_ting_berg_2026]
- [Ting, Eric et al 2014][research_tingeric_lebofskysonia_2014]
- [Ting, Eric et al 2014][research_tingeric_nguyennhan_2014]
- [Ting, Eric et al 2015][research_tingeric_daotung_2015]
- [Tischler, Mark B. et al 1991][research_tischlermarkb_fletcherjayw_1991]
- [Toader 1987][research_toader_1987]
- [Toffol 2024][research_toffol_2024]
- [Toffol and Ricci 2023][research_toffol_ricci_2023]
- [Tohidi et al 2016][research_tohidi_khakisedigh_2016]
- [Toledano and Murakami 1987][research_toledano_murakami_1987]
- [Tona 1962][research_tona_1962]
- [Torregrosa et al 2022][research_torregrosa_gil_2022]
- [Torsion of Structural Concrete-Interaction 1968][research_torsion_of_1968]
- [Trabocco 1980][research_trabocco_1980]
- [Tracking control of a 1993][research_tracking_control_1993]
- [Tran 1994][research_tran_1994]
- [Tran and Nguyen 2022][research_tran_nguyen_2022]
- [Tran et al 2017][research_tran_sakamoto_2017]
- [Traven and Whitley 1995][research_traven_whitley_1995]
- [Tribuno et al 1976][research_tribuno_klein_1976]
- [Triplett 1972][research_triplett_1972]
- [Triplett 1980][research_triplett_1980]
- [Triplett et al 1971][research_triplett_burkhart_1971]
- [Triplett et al 1973][research_triplett_kappus_1973]
- [Trippensee, Gary A. and Lux, David P. 1987][research_trippenseegarya_luxdavidp_1987]
- [Trippensee, Gary A. and Lux, David P. 1988][research_trippenseegarya_luxdavidp_1988]
- [Tritschler and O’Connor 2016][research_tritschler_oconnor_2016]
- [Truong et al 2016][research_truong_rakotomamonjy_2016]
- [Tsoutsinos 1994][research_tsoutsinos_1994]
- [Tsunematsu and Donadon 2019][research_tsunematsu_donadon_2019]
- [Tsushima et al 2019][research_tsushima_yokozeki_2019]
- [Tsushima et al 2021][research_tsushima_saitoh_2021]
- [Tsypkin and Fu 1993][research_tsypkin_fu_1993]
- [Tu 1992][research_tu_1992]
- [Tu 1994][research_tu_1994]
- [Tu 1994][research_tu_1994_b]
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
- [Underwood, Pamela J. et al 2003][research_underwoodpamelaj_owenslewisr_2003]
- [Unruh 1988][research_unruh_1988]
- [Useller, James W. and Russey, Robert E. 1955][research_usellerjamesw_russeyroberte_1955]
- [Uzun 2024][research_uzun_2024]
- [Uzun 2024][research_uzun_2024_b]
- [Uzun and Oktay 2023][research_uzun_oktay_2023]
- [Uzun et al 2023][research_uzun_bilgic_2023]
- [van Dam et al 1981][research_vandam_holmes_1981]
- [Van Dommelen 1995][research_vandommelen_1995]
- [Van Doren 1955][research_vandoren_1955]
- [Van Gaasbeek 1980][research_vangaasbeek_1980]
- [Van Graas and Braasch 1991][research_vangraas_braasch_1991]
- [Van Graas et al 1994][research_vangraas_diggle_1994]
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
- [Verhaegen and Żbikowski 2017][research_verhaegen_zbikowski_2017]
- [Verma 1981][research_verma_1981]
- [Verri et al 2025][research_verri_desilvabussamra_2025]
- [Vile et al 2020][research_vile_alwi_2020]
- [Vilela and Donadon 2025][research_vilela_donadon_2025]
- [Vinje and Miller 1973][research_vinje_miller_1973]
- [Viswanath and Mukund 1995][research_viswanath_mukund_1995]
- [Voracek and Clarke 1994][research_voracek_clarke_1994]
- [Voracek, David F. and Clarke, Robert 1991][research_voracekdavidf_clarkerobert_1991]
- [Voting software for fault-tolerant 1993][research_voting_software_1993]
- [Vukobratović and Stojić 1985][research_vukobratovic_stojic_1985]
- [Vuong and Kim 2021][research_vuong_kim_2021]
- [Wadia et al 2019][research_wadia_niedermeier_2019]
- [Waggoner, E. G. and Bates, B. L. 1989][research_waggonereg_batesbl_1989]
- [Waggoner, E. G. et al 1986][research_waggonereg_jennettla_1986]
- [Waitman and Marcos 2019][research_waitman_marcos_2019]
- [Waitman and Marcos 2020][research_waitman_marcos_2020]
- [Wakimoto et al 2021][research_wakimoto_chiba_2021]
- [Walchli, Lawrence A. 1994][research_walchlilawrencea_1994]
- [Walker and Kaufman 1977][research_walker_kaufman_1977]
- [Walker, S. A. 1976][research_walkersa_1976]
- [Walker, T. H. et al 1997][research_walkerth_minguetpj_1997]
- [Walsh, Kevin R. 1993][research_walshkevinr_1993]
- [Walsh, Michael J. et al 1988][research_walshmichaelj_sellerswilliamliii_1988]
- [Wang 2019][research_wang_2019]
- [Wang 2026][research_wang_2026]
- [Wang and Chen 2024][research_wang_chen_2024]
- [Wang and Rogers 1991][research_wang_rogers_1991]
- [Wang and Xu 2018][research_wang_xu_2018]
- [Wang et al 2015][research_wang_wang_2015]
- [Wang et al 2016][research_wang_xu_2016]
- [Wang et al 2016][research_wang_zhu_2016]
- [Wang et al 2017][research_wang_chu_2017]
- [Wang et al 2017][research_wang_su_2017]
- [Wang et al 2018][research_wang_daronch_2018]
- [Wang et al 2018][research_wang_su_2018]
- [Wang et al 2018][research_wang_wynn_2018]
- [Wang et al 2019][research_wang_vankampen_2019]
- [Wang et al 2020][research_wang_zhang_2020]
- [Wang et al 2021][research_wang_mkhoyan_2021]
- [Wang et al 2021][research_wang_wan_2021]
- [Wang et al 2021][research_wang_wu_2021]
- [Wang et al 2022][research_wang_zhang_2022]
- [Wang et al 2022][research_wang_zheng_2022]
- [Wang et al 2024][research_wang_sun_2024]
- [Wang et al 2024][research_wang_sun_2024_b]
- [Wang et al 2025][research_wang_chen_2025]
- [Wang et al 2025][research_wang_ji_2025]
- [Wang et al 2025][research_wang_li_2025]
- [Wang et al 2025][research_wang_li_2025_b]
- [Wang et al 2025][research_wang_sun_2025]
- [Wang et al 2025][research_wang_tian_2025]
- [Wang et al 2025][research_wang_zhang_2025]
- [Wang et al 2026][research_wang_hu_2026]
- [Wang et al 2026][research_wang_li_2026]
- [Wang et al 2026][research_wang_weng_2026]
- [Wang, John T. 1996][research_wangjohnt_1996]
- [Wang, John T. et al 1996][research_wangjohnt_jegleydawnc_1996]
- [Wansasueb et al 2023][research_wansasueb_panagant_2023]
- [Wardlaw et al 1975][research_wardlaw_andrewb_1975]
- [Washington et al 1968][research_washington_pettis_1968]
- [Watson, Clifford 2010][research_watsonclifford_2010]
- [Watson, Clifford C. 2011][research_watsoncliffordc_2011]
- [Wauters 2022][research_wauters_2022]
- [Webb, Lannie D. et al 1988][research_webblannied_mccainwilliame_1988]
- [Weed et al 1983][research_weed_carlson_1983]
- [Wegener et al 1993][research_wegener_dhooghe_1993]
- [Wei 2022][research_wei_2022]
- [Wei et al 2017][research_wei_chen_2017]
- [Wei et al 2019][research_wei_zhan_2019]
- [Wei et al 2024][research_wei_meng_2024]
- [Wei et al 2025][research_wei_cui_2025]
- [Weidemann and Leondes 1979][research_weidemann_leondes_1979]
- [Weinert and Meyer 1984][research_weinert_meyer_1984]
- [Weisshaar 1977][research_weisshaar_1977]
- [Weisshaar 1978][research_weisshaar_1978]
- [Weisshaar 1979][research_weisshaar_1979]
- [Weisshaar 1980][research_weisshaar_1980]
- [Weisshaar 1981][research_weisshaar_1981]
- [Weisshaar 1985][research_weisshaar_1985]
- [Weisshaar and Zeiler 1983][research_weisshaar_zeiler_1983]
- [Weisshaar, T. A. 1983][research_weisshaarta_1983]
- [Weisshaar, T. A. and Ehlers, S. M. 1990][research_weisshaarta_ehlerssm_1990]
- [Weisshaar, T. A. and Zeiler, T. A. 1982][research_weisshaarta_zeilerta_1982]
- [Weisshaar, Terrence A. and Ehlers, Steven M. 1992][research_weisshaarterrencea_ehlersstevenm_1992]
- [Welle 2000][research_welle_2000]
- [Wells 2002][research_wells_2002]
- [Wen et al 2023][research_wen_song_2023]
- [Werdes 1953][research_werdes_1953]
- [Werter and De Breuker 2016][research_werter_debreuker_2016]
- [Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]
- [Whitbeck et al 1982][research_whitbeck_smith_1982]
- [White 2004][research_white_2004]
- [White et al 2005][research_white_geubelle_2005]
- [White, Edward V. et al 2015][research_whiteedwardv_kapaniarakeshk_2015]
- [White, J. F., III and Bendiksen, O. O. 1986][research_whitejfiii_bendiksenoo_1986]
- [Whitehead, R. S. et al 1992][research_whiteheadrs_foremancr_1992]
- [Whitlow, Woodrow, Jr. et al 1991][research_whitlowwoodrowjr_bennettrobertm_1991]
- [Whitworth 1987][research_whitworth_1987]
- [Whoric 1973][research_whoric_1973]
- [Whoric 1977][research_whoric_1977]
- [Wickens and Dixon 2002][research_wickens_dixon_2002]
- [Wiggenraad, J. F. M. and Bauld, N. R., Jr. 1993][research_wiggenraadjfm_bauldnrjr_1993]
- [Wilcox 1963][research_wilcox_1963]
- [Wildermuth et al 1974][research_wildermuth_rothammer_1974]
- [Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]
- [Williams 1980][research_williams_1980]
- [Williamson 2022][research_williamson_2022]
- [Wilson 2026][research_wilson_2026]
- [Wilson et al 1993][research_wilson_riley_1993]
- [Wilson, David J. et al 1994][research_wilsondavidj_citurskevind_1994]
- [Wing et al 2025][research_wing_wing_2025]
- [Wise et al 1999][research_wise_sedwick_1999]
- [Withers 1981][research_withers_1981]
- [Witte et al 2003][research_witte_monson_2003]
- [Wittlin 1988][research_wittlin_1988]
- [Wolfe 1967][research_wolfe_1967]
- [Wollner 1972][research_wollner_1972]
- [Wong et al 1981][research_wong_cox_1981]
- [Wood, R. M. and Miller, D. S. 1985][research_woodrm_millerds_1985]
- [Woodcock, R. J. and George, F. L. 1976][research_woodcockrj_georgefl_1976]
- [Woodrow Whitlow, Jr. and Emily N. Todd 1999][research_woodrowwhitlowjr_emilyntodd_1999]
- [Woods et al 1990][research_woods_gilbert_1990]
- [Woods, Jessica A. et al 1989][research_woodsjessicaa_gilbertmichaelg_1989]
- [Wrestler and Clifton G. 1965][research_wrestler_cliftong_1965]
- [Wright 1945][research_wright_1945]
- [Wu and Chiu 1992][research_wu_chiu_1992]
- [Wu and Livne 2016][research_wu_livne_2016]
- [Wu et al 2017][research_wu_chen_2017]
- [Wu et al 2020][research_wu_chen_2020]
- [Wu et al 2021][research_wu_sun_2021]
- [Wu et al 2022][research_wu_zuo_2022]
- [Wu et al 2025][research_wu_fu_2025]
- [Wunderlich 2015][research_wunderlich_2015]
- [Wunderlich and Dähne 2017][research_wunderlich_dahne_2017_b]
- [Wunderlich et al 2017][research_wunderlich_dahne_2017]
- [X-29 Research Aircraft 1991][research_x_29_research_1991]
- [Xiang and Wang 2023][research_xiang_wang_2023]
- [Xiao et al 2021][research_xiao_sattarov_2021]
- [Xie and Wang 2025][research_xie_wang_2025]
- [Xinbing et al 2020][research_xinbing_wen_2020]
- [Xiong et al 2026][research_xiong_tang_2026]
- [Xu 2025][research_xu_2025]
- [Xu 2026][research_xu_2026]
- [Xu and Wang 2016][research_xu_wang_2016]
- [Xu and Zha 2021][research_xu_zha_2021]
- [Xu et al 2015][research_xu_gao_2015]
- [Xu et al 2018][research_xu_zhang_2018]
- [Xu et al 2019][research_xu_tan_2019]
- [Xu et al 2020][research_xu_zhang_2020]
- [Xu et al 2025][research_xu_zhang_2025]
- [Xu et al 2026][research_xu_zhang_2026]
- [Xue and Yao 2020][research_xue_yao_2020]
- [Xue et al 2019][research_xue_ye_2019]
- [Yalvaç et al 1991][research_yalvac_yats_1991]
- [Yamane 1992][research_yamane_1992]
- [Yamane and Friedmann 1993][research_yamane_friedmann_1993]
- [Yang and Gao 2020][research_yang_gao_2020]
- [Yang and Liu 1976][research_yang_liu_1976]
- [Yang and Manning 1994][research_yang_manning_1994]
- [Yang and Wan 1978][research_yang_wan_1978]
- [Yang and Zhao 1989][research_yang_zhao_1989]
- [Yang and Zhao 1992][research_yang_zhao_1992]
- [Yang et al 1980][research_yang_guruswamy_1980]
- [Yang et al 1981][research_yang_striz_1981]
- [Yang et al 2016][research_yang_zhao_2016]
- [Yang et al 2017][research_yang_huang_2017]
- [Yang et al 2019][research_yang_huang_2019]
- [Yang et al 2019][research_yang_xie_2019]
- [Yang et al 2019][research_yang_yang_2019]
- [Yang et al 2022][research_yang_mao_2022]
- [Yang et al 2025][research_yang_wang_2025]
- [Yang et al 2026][research_yang_tang_2026]
- [Yang et al 2026][research_yang_yu_2026]
- [Yang et al 2026][research_yang_zhang_2026]
- [Yao et al 2020][research_yao_liu_2020]
- [Yates 1966][research_yates_1966]
- [Yates et al 1982][research_yates_wynne_1982]
- [Yates et al 1983][research_yates_wynne_1983]
- [Yates, E. C., Jr. et al 1981][research_yatesecjr_wynneec_1981]
- [Yates, E. Carson, Jr. and Chu, Li-Chuan 1987][research_yatesecarsonjr_chulichuan_1987]
- [Ye et al 2015][research_ye_chen_2015]
- [Ye et al 2024][research_ye_yang_2024]
- [Yi et al 2015][research_yi_jun_2015]
- [Yildiz, Yidiray et al 2011][research_yildizyidiray_kolmanovskyilyav_2011]
- [Yildiz, Yildiray and Kolmanovsky, Ilya V. 2010][research_yildizyildiray_kolmanovskyilyav_2010]
- [Yin and Wang 2017][research_yin_wang_2017]
- [Yin et al 2019][research_yin_chu_2019]
- [Yin et al 2025][research_yin_huang_2025]
- [Ying et al 2021][research_ying_liqiang_2021]
- [Yip, L. P. and Paulson, J. W., Jr. 1977][research_yiplp_paulsonjwjr_1977]
- [Yoo 2017][research_yoo_2017]
- [Yoo et al 2023][research_yoo_jeong_2023]
- [You 2020][research_you_2020]
- [You et al 2019][research_you_yasaee_2019]
- [Young et al 2018][research_young_garg_2018]
- [Yu 1987][research_yu_1987]
- [Yu 2018][research_yu_2018]
- [Yu and Yu 2026][research_yu_yu_2026]
- [Yu et al 2017][research_yu_fang_2017]
- [Yu et al 2017][research_yu_wang_2017]
- [Yuan et al 2022][research_yuan_thomson_2022]
- [Yuan, F. G. and Reeder, James R. 2001][research_yuanfg_reederjamesr_2001]
- [Yue and Zhao 2020][research_yue_zhao_2020]
- [Yue et al 2017][research_yue_zhang_2017]
- [Yurtsever et al 2026][research_yurtsever_sahin_2026]
- [Yutuk et al 2021][research_yutuk_tikenogullari_2021]
- [Yuvarajan 2001][research_yuvarajan_2001]
- [Zaw and Baranovski 2026][research_zaw_baranovski_2026]
- [Zaytseva et al 2021][research_zaytseva_kuznetsov_2021]
- [Zeiler, Thomas A. 1998][research_zeilerthomasa_1998]
- [Zelenkov 2018][research_zelenkov_2018]
- [Zhai et al 2020][research_zhai_li_2020]
- [Zhang and Wang 2019][research_zhang_wang_2019]
- [Zhang and Zhao 2023][research_zhang_zhao_2023]
- [Zhang et al 2015][research_zhang_marzocca_2015]
- [Zhang et al 2015][research_zhang_wang_2015]
- [Zhang et al 2018][research_zhang_han_2018]
- [Zhang et al 2018][research_zhang_liu_2018]
- [Zhang et al 2019][research_zhang_zhao_2019]
- [Zhang et al 2020][research_zhang_chen_2020]
- [Zhang et al 2022][research_zhang_shao_2022]
- [Zhang et al 2022][research_zhang_wang_2022]
- [Zhang et al 2022][research_zhang_wang_2022_b]
- [Zhang et al 2024][research_zhang_qiu_2024]
- [Zhang et al 2026][research_zhang_dai_2026]
- [Zhang et al 2026][research_zhang_li_2026]
- [Zhao et al 2015][research_zhao_luximon_2015]
- [Zhao et al 2024][research_zhao_zhao_2024]
- [Zhao et al 2026][research_zhao_liu_2026]
- [Zhao et al 2026][research_zhao_liu_2026_b]
- [Zheng and Shao 2025][research_zheng_shao_2025]
- [Zheng et al 2026][research_zheng_dai_2026]
- [Zhirabok et al 2024][research_zhirabok_filaretov_2024]
- [Zhong et al 2025][research_zhong_ying_2025]
- [Zhou and Huang 2021][research_zhou_huang_2021]
- [Zhou et al 1989][research_zhou_ye_1989]
- [Zhou et al 2017][research_zhou_wang_2017]
- [Zhou et al 2018][research_zhou_yu_2018]
- [Zhou et al 2019][research_zhou_xu_2019]
- [Zhou et al 2025][research_zhou_raze_2025]
- [Zhou et al 2026][research_zhou_gong_2026]
- [Zhou et al 2026][research_zhou_peng_2026]
- [Zhu et al 2017][research_zhu_du_2017]
- [Zhu et al 2022][research_zhu_shi_2022]
- [Zhuang et al 2021][research_zhuang_yang_2021]
- [Zia et al 2022][research_zia_liu_2022]
- [Ziegler 1963][research_ziegler_1963]
- [Zipperer et al 1975][research_zipperer_jenney_1975]
- [Zipperer et al 1975][research_zipperer_jenney_1975_b]
- [Zohar and Er-El 1988][research_zohar_erel_1988]
- [Zou et al 2025][research_zou_huang_2025]
- [Zuhri 2025][research_zuhri_2025]
- [Özkan 2020][research_ozkan_2020]
- [Комаров and Зінченко 2019][research___2019]
- [Лейбов and Гуревич 2021][research___2021]
- [Морозов 2015][research_anon_2015]

[research_011_intelligent_1994]: https://doi.org/10.1016/0967-0661(94)90363-8
[research_017_preview_1994]: https://doi.org/10.1016/0967-0661(94)90369-7
[research_024_automated_1994]: https://doi.org/10.1016/0967-0661(94)90376-x
[research_025_adaptive_1994]: https://doi.org/10.1016/0967-0661(94)90377-8
[research_053_fuzzy_1994]: https://doi.org/10.1016/0967-0661(94)90635-1
[research_056_neural_1994]: https://doi.org/10.1016/0967-0661(94)90638-6
[research_196_pointing_1994]: https://doi.org/10.1016/0967-0661(94)90548-7
[research_214_application_1994]: https://doi.org/10.1016/0967-0661(94)91003-0
[research___2019]: https://doi.org/10.20535/0203-3771372019186954
[research___2021]: https://doi.org/10.25791/aviakosmos.9.2021.1237
[research_a_feasibility_2019]: https://doi.org/10.21152/1750-9548.13.4.339
[research_a_model_2021]: https://doi.org/10.47176/jafm.14.03.31488
[research_a_spreadsheet_2018]: https://doi.org/10.20508/ijrer.v8i4.8480.g7550
[research_a_study_1973]: https://ntrs.nasa.gov/citations/19730009309
[research_abbott_alinity_2019]: https://doi.org/10.1097/01.bmsas.0000576756.38556.68
[research_abbottjm_millerba_1974]: https://ntrs.nasa.gov/citations/19740008382
[research_abdalla_mansor_2020]: https://doi.org/10.37200/ijpr/v24i2/pr200541
[research_abdelhady_1994]: https://doi.org/10.1080/00423119308969500
[research_abdulrashid_syedmohddardin_2025]: https://doi.org/10.58247/jdset-2025-0802-20
[research_abed_2000]: https://doi.org/10.21236/ada381735
[research_abed_alhamadani_2024]: https://doi.org/10.18280/mmep.111029
[research_abele_ruger_1973]: https://doi.org/10.21236/ad0766892
[research_abele_sanlorenzo_1975]: https://doi.org/10.21236/ada013139
[research_abeli_ruhlincl_1966]: https://ntrs.nasa.gov/citations/19660021918
[research_abelkis_1967]: https://doi.org/10.21236/ad0818959
[research_aberdeentestcentermd_2009]: https://doi.org/10.21236/ada509433
[research_abichandani_rosenberg_1952]: https://doi.org/10.2514/8.2362
[research_accelerated_development_1979]: https://ntrs.nasa.gov/citations/19790025046
[research_acoustic_emission_1981]: https://doi.org/10.1016/0010-4361(81)90431-6
[research_acoustic_emissions_1989]: https://doi.org/10.1016/0010-4361(89)90260-7
[research_active_fault_tolerant_2025]: https://doi.org/10.3901/jme.2025.16.321
[research_adams_1973]: https://doi.org/10.21236/ad0771962
[research_adams_1977]: https://doi.org/10.1115/1.3450686
[research_adams_hatch_1971]: https://doi.org/10.2514/3.59103
[research_adeyemi_bull_2026]: https://doi.org/10.2514/1.c037836
[research_adneyps_hornwj_1984]: https://ntrs.nasa.gov/citations/19840024307
[research_aero_structural_2018]: https://doi.org/10.20474/jater-4.1.5
[research_aerodynamic_performance_2025]: https://doi.org/10.18178/ijmerr.14.1.48-58
[research_agrell_elmeland_1985]: https://doi.org/10.2514/3.45185
[research_aguilaribanez_2016]: https://doi.org/10.1002/rnc.3601
[research_agwa_2019]: https://doi.org/10.1007/s11071-019-04990-y
[research_aharrahralphc_2007]: https://ntrs.nasa.gov/citations/20100011189
[research_ahmadi_farsadi_2024]: https://doi.org/10.1016/j.ast.2023.108849
[research_aidala_1985]: https://doi.org/10.21236/ada171075
[research_airforceflighttestcenteredwardsafbca_1970]: https://doi.org/10.21236/ada529707
[research_airforceflighttestcenteredwardsafbca_1974]: https://doi.org/10.21236/ada011561
[research_airforceflighttestcenteredwardsafbca_1974_b]: https://doi.org/10.21236/ada011562
[research_airforceflighttestcenteredwardsafbca_2002]: https://doi.org/10.21236/ada402888
[research_airforceflighttestcenteredwardsafbca_2002_b]: https://doi.org/10.21236/ada403258
[research_airforcetestpilotschooledwardsafbca_1969]: https://doi.org/10.21236/ada319985
[research_airforcetestpilotschooledwardsafbca_1988]: https://doi.org/10.21236/ada319984
[research_airforcetestpilotschooledwardsafbca_1989]: https://doi.org/10.21236/ada319980
[research_airforcetestpilotschooledwardsafbca_1990]: https://doi.org/10.21236/ada319976
[research_airforcetestpilotschooledwardsafbca_1990_b]: https://doi.org/10.21236/ada319978
[research_airforcetestpilotschooledwardsafbca_1990_c]: https://doi.org/10.21236/ada320058
[research_airforcetestpilotschooledwardsafbca_1990_d]: https://doi.org/10.21236/ada320062
[research_airforcetestpilotschooledwardsafbca_1990_e]: https://doi.org/10.21236/ada319977
[research_airforcetestpilotschooledwardsafbca_1991]: https://doi.org/10.21236/ada319981
[research_airforcetestpilotschooledwardsafbca_1992]: https://doi.org/10.21236/ada319982
[research_airforcetestpilotschooledwardsafbca_1993]: https://doi.org/10.21236/ada320063
[research_akbari_galeani_2025]: https://doi.org/10.1109/lcsys.2025.3633369
[research_alag_kaufman_1975]: https://doi.org/10.2514/3.59859
[research_alam_hromcik_2015]: https://doi.org/10.1016/j.ast.2014.12.020
[research_alam_lee_2026]: https://doi.org/10.1016/j.compstruct.2026.120344
[research_albachten_1956]: https://doi.org/10.21236/ad0116273
[research_alberts_2011]: https://doi.org/10.21236/ada631225
[research_alberts_2014]: https://doi.org/10.21236/ada605273
[research_alberts_conley_2015]: https://doi.org/10.21236/ada617821
[research_alexander_1991]: https://doi.org/10.21236/ada240263
[research_alexander_griffin_1973]: https://doi.org/10.21236/ad0763725
[research_alhajahmad_mittelstedt_2021]: https://doi.org/10.1016/j.compstruct.2020.113271
[research_alim_rizianiza_2021]: https://doi.org/10.24176/simet.v11i2.5428
[research_alisyedfirasat_1997]: https://ntrs.nasa.gov/citations/19970026582
[research_aljaburi_feszty_2019]: https://doi.org/10.1016/j.cja.2019.05.009
[research_allen_bradley_1983]: https://doi.org/10.21236/ada134059
[research_allen_bradley_1984]: https://doi.org/10.21236/ada150802
[research_allisondenniso_dagenhartjray_1987]: https://ntrs.nasa.gov/citations/19890009895
[research_almosnino_1985]: https://doi.org/10.2514/3.9057
[research_alyanak_pendleton_2017]: https://doi.org/10.2514/1.c033040
[research_amin_hollweger_1983]: https://doi.org/10.2514/3.44924
[research_amirahmadichomachar_kuppusamy_2022]: https://doi.org/10.1108/aeat-08-2021-0240
[research_an_guo_2020]: https://doi.org/10.1007/s11071-020-05531-8
[research_an_khoo_2017]: https://doi.org/10.1016/j.compstruct.2017.07.042
[research_an_zhang_2026]: https://doi.org/10.1016/j.ast.2025.111209
[research_anderson_1961]: https://doi.org/10.21236/ad0322137
[research_anderson_1968]: https://doi.org/10.21236/ad0675550
[research_anderson_1985]: https://doi.org/10.2514/3.45218
[research_anderson_berger_1973]: https://doi.org/10.2514/3.60204
[research_anderson_hogle_1986]: https://doi.org/10.1016/0094-5765(86)90134-7
[research_andersonca_1976]: https://ntrs.nasa.gov/citations/19760024050
[research_andresperez_gonzalezjuarez_2016]: https://doi.org/10.1080/0305215x.2016.1165568
[research_anikin_animitsa_2015]: https://doi.org/10.1615/tsagiscij.2015014083
[research_annadata_endesfelder_2024]: https://doi.org/10.1088/2053-1591/ad8397
[research_announcement_european_1988]: https://doi.org/10.1016/0266-8920(88)90030-6
[research_anon_2015]: https://doi.org/10.18372/2073-4751.2.8948
[research_ansari_zucco_2023]: https://doi.org/10.1016/j.compstruct.2023.116691
[research_ansellgs_loewyrg_1982]: https://ntrs.nasa.gov/citations/19830009326
[research_antonakis_2025]: https://doi.org/10.1016/j.ast.2025.110020
[research_antonakis_2025_b]: https://doi.org/10.1007/s13272-025-00815-4
[research_antonakis_biannic_2024]: https://doi.org/10.2514/1.c037707
[research_application_analysis_2022]: https://doi.org/10.47939/et.v3i5(02).13
[research_apu_hydraulic_actuator_subsystem_1975]: https://ntrs.nasa.gov/citations/19760019175
[research_arcidiacono_carta_1970]: https://doi.org/10.21236/ad0869823
[research_ardemamd_williamslj_1972]: https://ntrs.nasa.gov/citations/19720018366
[research_argha_su_2018]: https://doi.org/10.1002/rnc.4376
[research_argha_su_2019]: https://doi.org/10.1002/rnc.4727
[research_armanious_lind_2017]: https://doi.org/10.2514/1.g002799
[research_armstrong_1977]: https://doi.org/10.21236/adb029224
[research_armstrong_lindberg_2006]: https://doi.org/10.21236/ada463491
[research_arnold_1942]: https://doi.org/10.2514/8.10949
[research_asgari_kouchakzadeh_2016]: https://doi.org/10.1016/j.compstruct.2016.02.015
[research_ashkenasirvingl_klydedavidh_1989]: https://ntrs.nasa.gov/citations/19890011628
[research_ashton_1970]: https://doi.org/10.1177/002199837000400201
[research_ashworth_mckissick_1979]: https://doi.org/10.2514/3.58605
[research_aston_williams_1994]: https://doi.org/10.1016/0263-8223(94)90050-7
[research_audoin_baste_1994]: https://doi.org/10.1115/1.2901446
[research_awadallaalihajahmed_2024]: https://doi.org/10.47191/etj/v9i10.08
[research_awadallaalihajahmed_2024_b]: https://doi.org/10.47191/etj/v9i10.09
[research_axelson_1977]: https://doi.org/10.2514/3.58819
[research_babuska_wiebe_2018]: https://doi.org/10.1016/j.compstruct.2018.01.036
[research_bachman_1981]: https://doi.org/10.1002/j.2161-4296.1981.tb00769.x
[research_badaliance_dill_1981]: https://doi.org/10.21236/ada105034
[research_baek_2021]: https://doi.org/10.34139/jscs.2021.11.2.1
[research_bagherzadeh_2026]: https://doi.org/10.3390/mca31030085
[research_bagherzadeh_mohammadkarimi_2025]: https://doi.org/10.3390/mca30020041
[research_bahr_mckay_2021]: https://doi.org/10.1017/aer.2021.114
[research_bai_2018]: https://doi.org/10.1049/joe.2018.0025
[research_bai_guan_2024]: https://doi.org/10.1016/j.addma.2024.104298
[research_baier_1970]: https://doi.org/10.21236/ad0878050
[research_baileyrandalle_powersbruceg_1988]: https://ntrs.nasa.gov/citations/19880063393
[research_baileyre_knottslh_1990]: https://ntrs.nasa.gov/citations/19910005040
[research_baileyre_smithre_1981]: https://ntrs.nasa.gov/citations/19820026927
[research_baker_galigher_1960]: https://doi.org/10.21236/ad0320438
[research_baker_jones_1985]: https://doi.org/10.1016/0263-8223(85)90018-2
[research_balasubramanian_jayanarasimhan_2025]: https://doi.org/10.29294/ijase.12.1.2025.5007-5016
[research_bandyopadhyay_1989]: https://doi.org/10.1017/s0001924000016651
[research_bandyopadhyay_1991]: https://doi.org/10.2514/3.46077
[research_banksdanielw_1988]: https://ntrs.nasa.gov/citations/19890063987
[research_bantscheff_breitsamter_2023]: https://doi.org/10.3390/aerospace10070581
[research_bardo_2015]: https://doi.org/10.21236/ad1000337
[research_bargill_stengel_1986]: https://doi.org/10.2514/3.45276
[research_barrett_rembold_1983]: https://doi.org/10.2514/3.44841
[research_bartelsroberte_stanfordbretk_2019]: https://ntrs.nasa.gov/citations/20200002388
[research_bastin_coron_2025]: https://doi.org/10.1016/j.automatica.2024.112048
[research_bataineh_shawabkeh_2023]: https://doi.org/10.15866/irease.v16i6.24344
[research_batina_yang_1985]: https://doi.org/10.2514/3.45137
[research_batt_1974]: https://doi.org/10.2514/3.49284
[research_battersonjamesg_omarathomasm_1989]: https://ntrs.nasa.gov/citations/19890006554
[research_bauchau_1981]: https://doi.org/10.1177/002199838101500205
[research_bauchau_1983]: https://doi.org/10.1177/002199838301700205
[research_baum_clark_1979]: https://doi.org/10.21236/ada066669
[research_bazhenov_lysenkova_2015]: https://doi.org/10.1615/tsagiscij.2015013712
[research_beatty_brooks_1977]: https://doi.org/10.21236/ada045951
[research_becker_1992]: https://doi.org/10.1016/0263-8223(92)90079-r
[research_bellini_sorrentino_2018]: https://doi.org/10.1016/j.prostr.2018.06.027
[research_belmont_1983]: https://doi.org/10.21236/ada133274
[research_benaouali_boutemedjet_2024]: https://doi.org/10.1108/aeat-11-2023-0310
[research_bendiksen_friedmann_1982]: https://doi.org/10.1115/1.3227324
[research_bennett_dansberry_1993]: https://doi.org/10.2514/3.46314
[research_bennettrm_farmermg_1977]: https://ntrs.nasa.gov/citations/19770060309
[research_bennettrobertm_batinajohnt_1988]: https://ntrs.nasa.gov/citations/19880010035
[research_benoit_1969]: https://doi.org/10.4267/2042/66916
[research_benoit_leroy_1960]: https://doi.org/10.1016/0006-2952(60)90056-3
[research_berg_ting_2025]: https://doi.org/10.2514/1.g008589
[research_bergen_arnold_1940]: https://doi.org/10.2514/8.1231
[research_berger_blanken_2022]: https://doi.org/10.4050/jahs.67.032009
[research_berger_blanken_2022_b]: https://doi.org/10.4050/jahs.67.032008
[research_berger_tischler_2021]: https://doi.org/10.2514/1.g005768
[research_bergman_1948]: https://doi.org/10.21236/ada301214
[research_bergstedt_turner_1959]: https://doi.org/10.21236/ad0402171
[research_bernstein_2000]: https://doi.org/10.21236/ada382981
[research_berry_powers_1982]: https://doi.org/10.2514/3.57395
[research_berrydt_1981]: https://ntrs.nasa.gov/citations/19810059723
[research_besch_liu_1973]: https://doi.org/10.21236/ad0757645
[research_beyer_steen_2024]: https://doi.org/10.2514/1.g007984
[research_beyer_ullah_2024]: https://doi.org/10.1007/s13272-024-00760-8
[research_beyers_1988]: https://doi.org/10.2514/3.45559
[research_bhardwaj_kapania_1995]: https://doi.org/10.2514/3.46814
[research_bi_xie_2017]: https://doi.org/10.1016/j.cja.2016.12.028
[research_bian_nener_2018]: https://doi.org/10.1080/00207179.2018.1473643
[research_bian_nener_2019]: https://doi.org/10.1109/access.2019.2894961
[research_bidinotto_moura_2021]: https://doi.org/10.1017/aer.2021.82
[research_biezaddanielj_chouhweilan_1993]: https://ntrs.nasa.gov/citations/19930017967
[research_bihrle_jr_1980]: https://doi.org/10.21236/ada082335
[research_billingsley_1976]: https://doi.org/10.21236/ada024445
[research_binder_wildschek_2021]: https://doi.org/10.1016/j.ast.2021.106516
[research_binion_tw_1971]: https://doi.org/10.21236/ad0723294
[research_binion_tw_1975]: https://doi.org/10.21236/ada012000
[research_biskner_higgins_2005]: https://doi.org/10.21236/ada443361
[research_bismarcknasr_1994]: https://doi.org/10.2514/3.46590
[research_biswas_1993]: https://doi.org/10.1016/0263-8223(93)90233-g
[research_blackburn_whitfield_1965]: https://doi.org/10.21236/ad0620247
[research_blackwell_pounds_1977]: https://doi.org/10.2514/3.58877
[research_blair_weisshaar_1982]: https://doi.org/10.2514/3.44806
[research_bland_1980]: https://doi.org/10.2514/3.44684
[research_blight_gangsaas_1986]: https://doi.org/10.2514/3.20145
[research_bliss_1980]: https://doi.org/10.21236/ada093301
[research_boatwright_1961]: https://doi.org/10.21236/ad0262552
[research_bodson_2000]: https://doi.org/10.21236/ada381657
[research_bodson_2000_b]: https://doi.org/10.21236/ada390623
[research_bohlmann_eckstrom_1990]: https://doi.org/10.2514/3.25319
[research_bohlmannjonathand_1989]: https://ntrs.nasa.gov/citations/19890009883
[research_bohlmannjonathand_scottrobertc_1991]: https://ntrs.nasa.gov/citations/19910047245
[research_bohlmannjonathand_weisshaarterrencea_1988]: https://ntrs.nasa.gov/citations/19880044993
[research_boldingrm_stearmanro_1976]: https://ntrs.nasa.gov/citations/19770014087
[research_bondarenko_shkolnyi_2024]: https://doi.org/10.20535/0203-3771482024318185
[research_bons_martins_2020]: https://doi.org/10.3390/aerospace7080118
[research_boothe_chen_1974]: https://doi.org/10.21236/ad0782218
[research_bordogna_lancelot_2020]: https://doi.org/10.1007/s00158-019-02446-w
[research_borrok_rider_1970]: https://doi.org/10.1002/j.2161-4296.1970.tb00050.x
[research_boschja_kuehlwj_1976]: https://ntrs.nasa.gov/citations/19760058477
[research_boudreau_1977]: https://doi.org/10.2514/3.58889
[research_bouras_2020]: https://doi.org/10.5373/jardcs/v12sp3/20201258
[research_bowers_1981]: https://doi.org/10.2514/3.57530
[research_bowmankeithb_grandhiramanav_1989]: https://ntrs.nasa.gov/citations/19890015800
[research_boyd_1977]: https://doi.org/10.21236/ada053640
[research_boydenrp_1974]: https://ntrs.nasa.gov/citations/19830002753
[research_boydenrp_1978]: https://ntrs.nasa.gov/citations/19780025107
[research_boylan_1965]: https://doi.org/10.21236/ad0460154
[research_bradley_1986]: https://doi.org/10.21236/ada173255
[research_braff_till_1993]: https://doi.org/10.2514/atcq.1.2.179
[research_brennan_mcdaniel_1994]: https://doi.org/10.21236/ada284253
[research_briardy_head_1968]: https://doi.org/10.21236/ad0673964
[research_briggs_reed_1982]: https://doi.org/10.21236/ada125764
[research_brightlg_petersonvl_1960]: https://ntrs.nasa.gov/citations/19650018341
[research_brockld_goodmanha_1981]: https://ntrs.nasa.gov/citations/19820004206
[research_brodecki_subbarao_2015]: https://doi.org/10.2514/1.g000220
[research_broglio_1957]: https://doi.org/10.2514/8.3851
[research_bromfield_horri_2023]: https://doi.org/10.1017/aer.2023.18
[research_brooksjd_beamishjk_1977]: https://ntrs.nasa.gov/citations/19780002105
[research_broussard_stengel_1977]: https://doi.org/10.2514/3.44630
[research_broussardjr_halyon_1983]: https://ntrs.nasa.gov/citations/19840042741
[research_brown_1994]: https://doi.org/10.21236/ada279489
[research_brownsr_szalaikj_1977]: https://ntrs.nasa.gov/citations/19780028344
[research_brozoski_johnson_2000]: https://doi.org/10.21236/ada378682
[research_bruderlin_hosters_2018]: https://doi.org/10.1007/s13272-018-0322-3
[research_brunojoseph_libeskindmark_1990]: https://ntrs.nasa.gov/citations/19920023270
[research_bryant_albert_1988]: https://doi.org/10.21236/ada196620
[research_bueno_dowell_2020]: https://doi.org/10.2514/1.c035885
[research_buffington_1997]: https://doi.org/10.21236/ada327799
[research_buffington_1999]: https://doi.org/10.21236/ada375713
[research_buffington_1999_b]: https://doi.org/10.21236/ada374954
[research_buffington_adams_1995]: https://doi.org/10.1016/0967-0661(95)00039-w
[research_bugala_2025]: https://doi.org/10.2478/tar-2025-0008
[research_bugala_payenskyy_2025]: https://doi.org/10.1108/aeat-05-2025-0183
[research_burcham_myers_1985]: https://doi.org/10.2514/3.45252
[research_burdette_martins_2018]: https://doi.org/10.1016/j.ast.2018.08.004
[research_burkenjohnj_2007]: https://ntrs.nasa.gov/citations/20090007779
[research_burkhalter_1993]: https://doi.org/10.2514/3.46447
[research_burnett_beranek_2016]: https://doi.org/10.1017/aer.2016.41
[research_burns_1974]: https://doi.org/10.21236/ada048471
[research_burns_1975]: https://doi.org/10.1017/s0001924000034862
[research_burns_2002]: https://doi.org/10.21236/ada404484
[research_burt_1975]: https://doi.org/10.2514/3.59795
[research_busan_1998]: https://doi.org/10.21236/ada340820
[research_butler_1976]: https://doi.org/10.21236/ada023690
[research_butler_1982]: https://doi.org/10.2514/3.44764
[research_butler_1983]: https://doi.org/10.1017/s0001924000051046
[research_buzica_biswanger_2018]: https://doi.org/10.1016/j.trpro.2018.02.005
[research_bylsma_gunter_2007]: https://doi.org/10.21236/ada466491
[research_byreddy_grandhi_2003]: https://doi.org/10.21236/ada417124
[research_cabellrandolphh_gibbsgaryp_2000]: https://ntrs.nasa.gov/citations/20040085969
[research_cahn_garcia_1971]: https://doi.org/10.2514/3.44233
[research_cai_su_2024]: https://doi.org/10.3390/machines12070486
[research_cain_1979]: https://doi.org/10.21236/ada379310
[research_caixeta_marques_2018]: https://doi.org/10.1007/s40430-017-0958-7
[research_calarese_1984]: https://doi.org/10.2514/3.48231
[research_californiaunivlosangeles_2001]: https://doi.org/10.21236/ada385808
[research_callaghan_kunz_2021]: https://doi.org/10.2514/1.g004748
[research_callaway_2015]: https://doi.org/10.21236/ad1000591
[research_camacho_akhavan_2021]: https://doi.org/10.1016/j.compstruct.2021.113765
[research_campagna_benedetti_2025]: https://doi.org/10.1016/j.compstruct.2025.119508
[research_campagna_gulizzi_2025]: https://doi.org/10.1016/j.compstruct.2024.118697
[research_campbell_lafrey_1983]: https://doi.org/10.1002/j.2161-4296.1983.tb00853.x
[research_campbellrichardl_smithleigha_1989]: https://ntrs.nasa.gov/citations/19910001577
[research_campos_marques_2021]: https://doi.org/10.3390/aerospace8030077
[research_candon_marzocca_2026]: https://doi.org/10.2514/1.j066515
[research_cannella_garinei_2018]: https://doi.org/10.1016/j.compstruct.2017.11.029
[research_cao_jia_2020]: https://doi.org/10.1016/j.jfranklin.2020.08.028
[research_cao_liu_2025]: https://doi.org/10.3390/drones9060443
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
[research_cassanto_1971]: https://doi.org/10.2514/3.30338
[research_cassanto_1972]: https://doi.org/10.2514/3.50095
[research_castellani_cooper_2017]: https://doi.org/10.2514/1.c033825
[research_cavaliere_fezans_2024]: https://doi.org/10.2514/1.g007762
[research_cavaliere_fezans_2024_b]: https://doi.org/10.2514/1.g008040
[research_cavin_holyoak_1978]: https://doi.org/10.2514/3.58355
[research_celi_1991]: https://doi.org/10.2514/3.45991
[research_celi_friedmann_1990]: https://doi.org/10.2514/3.25141
[research_celi_lovera_2004]: https://doi.org/10.21236/ada425484
[research_cell_1992]: https://doi.org/10.2514/3.11215
[research_cen_li_2020]: https://doi.org/10.1177/0954410020944085
[research_cenkci_1991]: https://doi.org/10.21236/ada241143
[research_center_1975]: https://doi.org/10.21236/adb006719
[research_cesnik_2002]: https://doi.org/10.21236/ada401331
[research_cesnik_2005]: https://doi.org/10.21236/ada439640
[research_cestino_iannuzzo_2026]: https://doi.org/10.2514/1.c038607
[research_chakravarthy_evans_2015]: https://doi.org/10.1080/01630563.2015.1057286
[research_chakravarty_mahanta_2015]: https://doi.org/10.1002/rnc.3392
[research_chalk_1964]: https://doi.org/10.2514/3.43604
[research_chamlin_1951]: https://doi.org/10.1001/archopht.1951.01700020151003
[research_chamlin_davidoff_1950]: https://doi.org/10.3171/jns.1950.7.6.0539
[research_chancevoughtcorpdallastx_1979]: https://doi.org/10.21236/ada358711
[research_chang_1988]: https://doi.org/10.21236/ada196223
[research_changchuan_lan_2018]: https://doi.org/10.2514/1.c034162
[research_chaparrodaniel_fujiwaragustavoec_2016]: https://ntrs.nasa.gov/citations/20160008102
[research_chaplin_1953]: https://doi.org/10.21236/ad0775892
[research_chase_1977]: https://doi.org/10.2514/3.58782
[research_chattopadhyayaditi_jharatneshwar_1996]: https://ntrs.nasa.gov/citations/19970028021
[research_chattopadhyayaditi_zhangsen_1995]: https://ntrs.nasa.gov/citations/19950026507
[research_chau_piotrowski_2026]: https://doi.org/10.2514/1.c038646
[research_chau_zingg_2022]: https://doi.org/10.2514/1.c036389
[research_chau_zingg_2023]: https://doi.org/10.2514/1.c037158
[research_chen_1982]: https://doi.org/10.2514/3.51069
[research_chen_1983]: https://doi.org/10.4050/jahs.28.34
[research_chen_cai_2026]: https://doi.org/10.1109/tie.2025.3639811
[research_chen_dong_2023]: https://doi.org/10.1080/0305215x.2023.2212246
[research_chen_dugundji_1987]: https://doi.org/10.2514/3.45501
[research_chen_edwards_2018]: https://doi.org/10.1002/rnc.4282
[research_chen_gao_2023]: https://doi.org/10.3390/aerospace10050486
[research_chen_gao_2023_b]: https://doi.org/10.54254/2755-2721/9/20230085
[research_chen_han_2017]: https://doi.org/10.21595/mme.2017.18505
[research_chen_he_2025]: https://doi.org/10.3390/app15084333
[research_chen_holohan_2015]: https://doi.org/10.1002/rnc.3362
[research_chen_jing_2020]: https://doi.org/10.1108/aeat-01-2020-0005
[research_chen_li_2017]: https://doi.org/10.1016/j.compstruct.2017.02.019
[research_chen_li_2018]: https://doi.org/10.1016/j.ast.2018.01.023
[research_chen_liu_2016]: https://doi.org/10.2514/1.c033305
[research_chen_nie_2018]: https://doi.org/10.1016/j.compstruct.2017.12.042
[research_chen_shi_2023]: https://doi.org/10.1063/5.0130370
[research_chen_shi_2023_b]: https://doi.org/10.1063/5.0162013
[research_chen_sun_1987]: https://doi.org/10.1016/0263-8223(87)90019-5
[research_chen_yang_2018]: https://doi.org/10.1360/n092017-00428
[research_chen_zhao_2020]: https://doi.org/10.1061/(asce)as.1943-5525.0001201
[research_chenghk_mengsy_1980]: https://ntrs.nasa.gov/citations/19800038581
[research_cherry_costa_1993]: https://doi.org/10.1080/00423119308969481
[research_chetty_lakshmi_1991]: https://doi.org/10.1016/s1474-6670(17)54311-6
[research_chien_tang_1964]: https://doi.org/10.21236/ad0609470
[research_chin_1989]: https://doi.org/10.2514/3.45888
[research_chin_lee_1994]: https://doi.org/10.1016/0967-0661(94)90572-x
[research_chinj_chaconv_1987]: https://ntrs.nasa.gov/citations/19880027032
[research_chinvorarat_2021]: https://doi.org/10.1016/j.heliyon.2021.e08410
[research_chipmanr_rauchf_1984]: https://ntrs.nasa.gov/citations/19840013485
[research_chipmanr_rauchf_1985]: https://ntrs.nasa.gov/citations/19850048205
[research_choi_2016]: https://doi.org/10.5762/kais.2016.17.1.159
[research_choi_choi_2026]: https://doi.org/10.3390/aerospace13060526
[research_choi_lim_2020]: https://doi.org/10.5139/jksas.2020.48.8.555
[research_choi_park_2019]: https://doi.org/10.1016/j.compstruct.2019.111027
[research_choosakngaongam_rapeeujjin_2024]: https://doi.org/10.37934/cfdl.16.5.18
[research_chowdary_parthan_1994]: https://doi.org/10.1016/0045-7949(94)90200-3
[research_chowhan_arya_2019]: https://doi.org/10.1002/j.2334-5837.2019.00697.x
[research_christoforou_1993]: https://doi.org/10.1016/0263-8223(93)90046-s
[research_christopherkdroney_anthonyjsclafani_2020]: https://ntrs.nasa.gov/citations/20205005698
[research_christopherlblanken_matthewswhalley_1993]: https://ntrs.nasa.gov/citations/19940008821
[research_chujulio_lawingpiercel_1990]: https://ntrs.nasa.gov/citations/19930020260
[research_cidmontoya_hernandez_2018]: https://doi.org/10.1016/j.jweia.2017.12.018
[research_clark_2001]: https://doi.org/10.21236/ada399161
[research_clark_letron_1989]: https://doi.org/10.2514/3.20392
[research_clark_spurlin_1962]: https://doi.org/10.21236/ad0329345
[research_clarker_shaned_1982]: https://ntrs.nasa.gov/citations/19820015371
[research_clarkerobert_burkenjohnj_1994]: https://ntrs.nasa.gov/citations/19940029878
[research_clay_rockafellow_1973]: https://doi.org/10.21236/ad0758891
[research_clementskeith_2016]: https://ntrs.nasa.gov/citations/20160013364
[research_clews_1973]: https://doi.org/10.1108/eb035015
[research_cliett_1952]: https://doi.org/10.21236/ad0006050
[research_clyde_bonner_1984]: https://doi.org/10.21236/ada148355
[research_coban_2020]: https://doi.org/10.5755/j01.itc.49.1.23275
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
[research_combined_flight_1974]: https://doi.org/10.1108/eb035139
[research_concorde_automatic_1971]: https://doi.org/10.1108/eb034745
[research_cong_hu_2023]: https://doi.org/10.3390/aerospace10030241
[research_conlansmith_andreasen_2022]: https://doi.org/10.1007/s00158-022-03246-5
[research_connelly_1982]: https://doi.org/10.21236/ada120473
[research_cook_1979]: https://doi.org/10.1090/qam/542990
[research_cooperpa_stroudwj_1972]: https://ntrs.nasa.gov/citations/19730028903
[research_corlissld_talbotpd_1977]: https://ntrs.nasa.gov/citations/19770024230
[research_cornelius_lucius_1994]: https://doi.org/10.2514/3.46566
[research_cornellaeronauticallabincbuffalony_1947]: https://doi.org/10.21236/ada800190
[research_cornellaeronauticallabincbuffalony_1953]: https://doi.org/10.21236/ad0006796
[research_cotton_1974]: https://doi.org/10.21236/ada000894
[research_councill_goble_1971]: https://doi.org/10.2514/3.30296
[research_crabtree_1979]: https://doi.org/10.21236/ada081738
[research_craig_1965]: https://doi.org/10.21236/ad0628087
[research_crandall_maund_1973]: https://doi.org/10.21236/ad0766642
[research_cranedf_1983]: https://ntrs.nasa.gov/citations/19830055004
[research_cranedf_1984]: https://ntrs.nasa.gov/citations/19850009674
[research_craneharoldl_sommerrobertw_1961]: https://ntrs.nasa.gov/citations/19980227996
[research_crawley_lee_1978]: https://doi.org/10.21236/ada062582
[research_crews_naik_1986]: https://doi.org/10.1016/0263-8223(86)90066-8
[research_crimi_ordway_1962]: https://doi.org/10.2514/8.9560
[research_crittenden_weishaar_1978]: https://doi.org/10.2514/3.58383
[research_crolla_abdelhady_1991]: https://doi.org/10.1080/00423119108968982
[research_croommarka_whippleraymondd_1988]: https://ntrs.nasa.gov/citations/19890063988
[research_croop_1985]: https://doi.org/10.21236/ada368444
[research_crouse_leishman_1992]: https://doi.org/10.2514/3.46139
[research_crowe_1937]: https://doi.org/10.1108/eb030157
[research_cruz_gorenberg_1969]: https://doi.org/10.21236/ad0864282
[research_cui_li_2022]: https://doi.org/10.1016/j.oceaneng.2022.113138
[research_cui_miao_2026]: https://doi.org/10.1016/j.compstruct.2026.120413
[research_cully_boller_1973]: https://doi.org/10.21236/ad0916279
[research_cundiff_buckingham_1999]: https://doi.org/10.21236/ada382521
[research_cunis_condomines_2020]: https://doi.org/10.2514/1.c035455
[research_cunis_condomines_2020_b]: https://doi.org/10.2514/1.g004753
[research_cunningham_batina_1988]: https://doi.org/10.2514/3.45686
[research_cunninghamherbertj_batinajohnt_1987]: https://ntrs.nasa.gov/citations/19880064102
[research_currao_jiang_2026]: https://doi.org/10.1017/flo.2026.10056
[research_cutchinsma_purvisjw_1982]: https://ntrs.nasa.gov/citations/19820025882
[research_czyba_stajer_2019]: https://doi.org/10.24425/acs.2019.127525
[research_czysz_1963]: https://doi.org/10.21236/ad0407689
[research_dagilis_kilikevicius_2023]: https://doi.org/10.3390/aerospace10090801
[research_dai_wu_2016]: https://doi.org/10.1016/j.ast.2016.01.019
[research_daken_mar_1985]: https://doi.org/10.1016/0263-8223(85)90002-9
[research_dallas_irvin_1956]: https://doi.org/10.21236/ad0147926
[research_damodaran_caughey_1988]: https://doi.org/10.2514/3.10046
[research_dandois_2016]: https://doi.org/10.1063/1.4937426
[research_dandrea_2003]: https://doi.org/10.21236/ada422201
[research_dandrea_2008]: https://doi.org/10.21236/ada530333
[research_daniel_1976]: https://doi.org/10.21236/ada041490
[research_darabi_ganesan_2016]: https://doi.org/10.1016/j.compstruct.2016.02.064
[research_darabi_ganesan_2017]: https://doi.org/10.1016/j.compstruct.2017.04.059
[research_das_kapuria_2016]: https://doi.org/10.1016/j.jfluidstructs.2015.11.008
[research_das_longo_1995]: https://doi.org/10.2514/3.46782
[research_daspatel_kumarkaruparthi_2021]: https://doi.org/10.33564/ijeast.2021.v05i09.038
[research_daudeville_ladeveze_1993]: https://doi.org/10.1016/0263-8223(93)90203-3
[research_david_hale_1978]: https://doi.org/10.21236/ada065822
[research_davidmrichwine_davidffisher_1992]: https://ntrs.nasa.gov/citations/19920022032
[research_davidson_hd_1972]: https://doi.org/10.21236/ad0763365
[research_davis_1973]: https://doi.org/10.21236/ad0781807
[research_davis_garnett_1977]: https://doi.org/10.21236/ada050059
[research_davisddjr_farleygaryl_1993]: https://ntrs.nasa.gov/citations/19930049917
[research_dawe_bull_2025]: https://doi.org/10.2514/1.j064731
[research_deetsda_1975]: https://ntrs.nasa.gov/citations/19750010175
[research_deformational_behaviour_1990]: https://doi.org/10.1016/0010-4361(90)90242-o
[research_degaspari_mantegazza_2024]: https://doi.org/10.1109/access.2024.3390557
[research_delcarre_palacios_2020]: https://doi.org/10.2514/1.c035901
[research_demarchi_haning_1978]: https://doi.org/10.21236/ada060326
[research_demir_seyfullahbabaarslan_2021]: https://doi.org/10.11648/j.ajset.20210602.13
[research_deng_yi_2023]: https://doi.org/10.3390/aerospace10020125
[research_deninno_uherka_1966]: https://doi.org/10.21236/ad0637525
[research_departmentoftheairforcewashingtondc_1986]: https://doi.org/10.21236/ada268620
[research_description_and_1975]: https://ntrs.nasa.gov/citations/19750010173
[research_design_of_1995]: https://doi.org/10.1016/0967-0661(95)90151-5
[research_desilva_carmichael_1978]: https://doi.org/10.2514/3.58435
[research_desilvabme_medanrt_1978]: https://ntrs.nasa.gov/citations/19790005851
[research_deskos_delcarre_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.102981
[research_desouza_deleon_2023]: https://doi.org/10.1080/0305215x.2023.2243455
[research_desouza_vuillemin_2023]: https://doi.org/10.2514/1.g007153
[research_despirito_2005]: https://doi.org/10.21236/ada444636
[research_devine_choynowski_2025]: https://doi.org/10.3390/safety11010004
[research_dexter_1993]: https://doi.org/10.1243/pime_proc_1993_207_241_02
[research_dhawan_huang_2026]: https://doi.org/10.1016/j.cub.2025.12.024
[research_dhital_chouvion_2024]: https://doi.org/10.3390/aerospace11121043
[research_dhonau_blosser_1974]: https://doi.org/10.21236/ada032816
[research_dickerson_2020]: https://doi.org/10.1098/rspb.2020.1774
[research_diederichfranklinw_budianskybernard_1948]: https://ntrs.nasa.gov/citations/19930082318
[research_difrancesco_mattei_2016]: https://doi.org/10.2514/1.c033183
[research_difranco_1970]: https://doi.org/10.2514/3.44199
[research_difranco_1971]: https://doi.org/10.21236/ad0742246
[research_diggins_1951]: https://doi.org/10.21236/ad0895227
[research_digital_model_reference_1994]: https://doi.org/10.1016/0967-0661(94)90529-0
[research_dillinger_abdalla_2019]: https://doi.org/10.1007/s13272-019-00397-y
[research_dillinger_meddaikar_2020]: https://doi.org/10.3390/fluids5010035
[research_dipasquale_prince_2023]: https://doi.org/10.3390/aerospace10060569
[research_dirito_schettini_2016]: https://doi.org/10.1016/j.ress.2015.12.012
[research_dlamini_jones_2016]: https://doi.org/10.1017/aer.2016.42
[research_dlbirdsall_1970]: https://doi.org/10.1017/s0001924000114812
[research_dobosbubno_hartsook_1977]: https://doi.org/10.21236/ada062008
[research_dodayav_biswas_2024]: https://doi.org/10.2139/ssrn.4875854
[research_dodic_krstic_2023]: https://doi.org/10.3390/aerospace10030238
[research_doggettrobertvjr_riverajoseajr_1995]: https://ntrs.nasa.gov/citations/19950019961
[research_doman_1995]: https://doi.org/10.21236/ada305053
[research_dong_2025]: https://doi.org/10.61173/d58c8037
[research_dong_li_2022]: https://doi.org/10.3390/aerospace9120795
[research_dong_li_2023]: https://doi.org/10.1002/rnc.6722
[research_dong_lu_2016]: https://doi.org/10.1155/2016/5037678
[research_dong_shi_2019]: https://doi.org/10.1063/1.5093559
[research_dong_zhou_2025]: https://doi.org/10.1016/j.ast.2025.110199
[research_dorey_good_1980]: https://doi.org/10.1080/00423118008968613
[research_dowell_bliss_1978]: https://doi.org/10.21236/ada055735
[research_dresselhaus_dresselhaus_1982]: https://doi.org/10.21236/ada121236
[research_drtil_schulz_1978]: https://doi.org/10.1108/eb035443
[research_drummond_1971]: https://doi.org/10.21236/ad0729870
[research_duan_he_2024]: https://doi.org/10.1115/1.4064325
[research_dukes_1970]: https://doi.org/10.21236/ad0871424
[research_dul_2018]: https://doi.org/10.1108/aeat-11-2016-0215
[research_dunmire_1982]: https://doi.org/10.21236/ada148595
[research_dunn_leong_1981]: https://doi.org/10.21236/ada103922
[research_dunningpeterd_stanfordbretk_2014]: https://ntrs.nasa.gov/citations/20140007305
[research_dunnwr_cottrelld_1986]: https://ntrs.nasa.gov/citations/19860019473
[research_durand_teper_1964]: https://doi.org/10.21236/ad0606040
[research_durstonda_schreinerja_1983]: https://ntrs.nasa.gov/citations/19840027787
[research_dushane_1957]: https://doi.org/10.1126/science.125.3250.677
[research_dussart_lone_2019]: https://doi.org/10.3390/aerospace6060070
[research_dwivedi_anitha_2022]: https://doi.org/10.1002/masy.202100364
[research_eades_jr_1964]: https://doi.org/10.21236/ad0352807
[research_eastep_olsen_1980]: https://doi.org/10.2514/3.50866
[research_eastep_venkayya_1984]: https://doi.org/10.2514/3.45063
[research_ebnerre_markjg_1977]: https://ntrs.nasa.gov/citations/19770059956
[research_ecer_1985]: https://doi.org/10.21236/ada162168
[research_eckhaus_1962]: https://doi.org/10.2514/8.9589
[research_eckstromcv_spaincv_1982]: https://ntrs.nasa.gov/citations/19820046611
[research_edenborough_1968]: https://doi.org/10.2514/3.43915
[research_edwards_1983]: https://doi.org/10.2514/3.44863
[research_effects_of_1988]: https://doi.org/10.1016/0010-4361(88)90589-7
[research_efremov_efremov_2020]: https://doi.org/10.2514/1.g004409
[research_efremov_shcherbakov_2022]: https://doi.org/10.34759/vst-2022-1-201-210
[research_ehlers_weisshaar_1993]: https://doi.org/10.2514/3.46376
[research_eichler_1970]: https://doi.org/10.2514/3.44170
[research_ekaterinarisja_schifflewisb_1990]: https://ntrs.nasa.gov/citations/19900058795
[research_ekaterinarisja_schifflewisb_1994]: https://ntrs.nasa.gov/citations/19950037635
[research_ekquist_1965]: https://doi.org/10.21236/ad0623129
[research_elenchezhiyan_kumar_2025]: https://doi.org/10.1017/aer.2025.10069
[research_elmahdy_ali_2025]: https://doi.org/10.1038/s41598-025-99500-z
[research_elshazly_kassem_2025]: https://doi.org/10.1088/1742-6596/3070/1/012001
[research_eney_1968]: https://doi.org/10.2514/3.43938
[research_eng_1988]: https://doi.org/10.21236/ada205961
[research_engellandsa_franklinja_1992]: https://ntrs.nasa.gov/citations/19930029331
[research_enns_2003]: https://doi.org/10.21236/ada411755
[research_eraslan_oktay_2023]: https://doi.org/10.5755/j01.itc.52.4.33527
[research_erel_1988]: https://doi.org/10.2514/3.45535
[research_erel_seginer_1985]: https://doi.org/10.2514/3.45180
[research_ericksongarye_2003]: https://ntrs.nasa.gov/citations/20040016158
[research_eriksson_1990]: https://doi.org/10.1177/002199839002401201
[research_esfahani_webb_2018]: https://doi.org/10.1007/s00348-018-2588-y
[research_eugeneltu_1996]: https://ntrs.nasa.gov/citations/19960047050
[research_ewing_hinger_1988]: https://doi.org/10.1016/0263-8223(88)90050-5
[research_fadel_rabie_2019]: https://doi.org/10.18280/jesa.520307
[research_fan_wang_2025]: https://doi.org/10.3390/aerospace12090784
[research_fanucci_1987]: https://doi.org/10.1177/002199838702100204
[research_farbridge_woodward_1956]: https://doi.org/10.1108/eb032701
[research_farhat_amsallem_2011]: https://doi.org/10.21236/ada566361
[research_farmermg_hansonpw_1976]: https://ntrs.nasa.gov/citations/19760047098
[research_farsadi_ahmadi_2026]: https://doi.org/10.2514/1.j066652
[research_fatigue_behaviour_1977]: https://doi.org/10.1016/0010-4361(77)90034-9
[research_favier_maresca_1987]: https://doi.org/10.2514/3.45497
[research_fay_johnstone_1960]: https://doi.org/10.21236/ad0248516
[research_fazeli_stokesgriffin_2022]: https://doi.org/10.1016/j.compstruct.2022.115756
[research_fearnside_1962]: https://doi.org/10.1108/eb033507
[research_fedorenko_bondarenko_2024]: https://doi.org/10.20535/0203-3771472024307685
[research_fehrs_kaiser_2025]: https://doi.org/10.1007/s13272-025-00856-9
[research_feil_pflumm_2020]: https://doi.org/10.1016/j.compstruct.2020.112755
[research_feng_guo_2023]: https://doi.org/10.2514/1.g007591
[research_ferraiuolo_scigliano_2019]: https://doi.org/10.1016/j.compstruct.2018.09.024
[research_ferreres_hardier_2017]: https://doi.org/10.1002/rnc.3993
[research_feuer_barmish_1977]: https://doi.org/10.21236/ada044725
[research_fichera_isnardi_2019]: https://doi.org/10.3390/aerospace6020013
[research_figge_1973]: https://doi.org/10.21236/ad0781810
[research_filamentary_plastic_composite_1974]: https://doi.org/10.1016/0010-4361(74)90417-0
[research_filippou_kilimtzidis_2024]: https://doi.org/10.3390/aerospace11030180
[research_finkleman_1972]: https://doi.org/10.2514/3.59003
[research_flax_1943]: https://doi.org/10.2514/8.10981
[research_flightscienceslabincbuffalony_1964]: https://doi.org/10.21236/ad0442900
[research_florancejamesr_heegjennifer_2004]: https://ntrs.nasa.gov/citations/20040066092
[research_flores_bazan_2025]: https://doi.org/10.1002/asjc.70025
[research_fodor_redfield_1993]: https://doi.org/10.1080/00423119308969018
[research_fonte_ricci_2015]: https://doi.org/10.2514/1.c032995
[research_food_safety_2023]: https://doi.org/10.57263/jmq.02.03.20232
[research_forsman_1983]: https://doi.org/10.21236/ada130832
[research_fortis_fortis_2015]: https://doi.org/10.1504/ijais.2015.072146
[research_fosswejr_whitcombcf_1960]: https://ntrs.nasa.gov/citations/19660024027
[research_fournier_massioni_2022]: https://doi.org/10.2514/1.g006084
[research_fradenburgh_murrill_1973]: https://doi.org/10.21236/ad0771037
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
[research_fujii_1985]: https://doi.org/10.2322/jjsass1969.33.339
[research_fujioka_suzuki_1994]: https://doi.org/10.1080/00423119408969079
[research_fukuda_kobayashi_1987]: https://doi.org/10.1016/s1474-6670(17)55319-7
[research_fukunaga_1990]: https://doi.org/10.1177/002199839002400504
[research_fuller_1991]: https://doi.org/10.21236/ada248341
[research_fuller_2001]: https://doi.org/10.21236/ada389507
[research_fung_1982]: https://doi.org/10.21236/ada215096
[research_furtat_gushchin_2021]: https://doi.org/10.1109/access.2021.3056942
[research_fuzzy_logic_1991]: https://doi.org/10.1109/37.88591
[research_fuzzy_logic_1994]: https://doi.org/10.1109/37.295971
[research_gabel_ricks_1961]: https://doi.org/10.21236/ad0267342
[research_gainer_1963]: https://doi.org/10.21236/ad0404850
[research_galasso_ciminello_2024]: https://doi.org/10.3390/s24165216
[research_galffy_bock_2019]: https://doi.org/10.1016/j.conengprac.2019.03.006
[research_gamon_mahone_1975]: https://doi.org/10.21236/ada022146
[research_gao_liu_2024]: https://doi.org/10.1016/j.ast.2024.109671
[research_gao_wang_2021]: https://doi.org/10.1002/oca.2751
[research_garabedianpr_1979]: https://ntrs.nasa.gov/citations/19790011863
[research_garciahernandez_cuernorejado_2017]: https://doi.org/10.1109/access.2017.2758903
[research_gargsanjay_schmidtdavidk_1988]: https://ntrs.nasa.gov/citations/19880063045
[research_garkushenko_vinogradov_2016]: https://doi.org/10.3103/s1068799816040085
[research_garrard_low_1990]: https://doi.org/10.21236/ada231588
[research_garrickie_rubinowsi_1946]: https://ntrs.nasa.gov/citations/19930081835
[research_garrickie_rubinowsi_1946_b]: https://ntrs.nasa.gov/citations/19930090942
[research_garrisoncharliec_hacskayloandrew_1947]: https://ntrs.nasa.gov/citations/20050031172
[research_gea_chow_1992]: https://doi.org/10.2514/3.46186
[research_gearhart_1962]: https://doi.org/10.21236/ad0405110
[research_generaldynamicsastronauticssandiegoca_1961]: https://doi.org/10.21236/ad0843112
[research_generaldynamicsastronauticssandiegoca_1961_b]: https://doi.org/10.21236/ad0843200
[research_generaldynamicsastronauticssandiegoca_1962]: https://doi.org/10.21236/ad0852659
[research_gerdes_hynes_1972]: https://doi.org/10.4050/jahs.17.47
[research_ghalandari_mahariq_2022]: https://doi.org/10.32604/cmc.2022.020884
[research_ghayour_mani_2018]: https://doi.org/10.1108/aeat-07-2018-0194
[research_giese_reich_1996]: https://doi.org/10.21236/ada399629
[research_gilbert_schmidt_1984]: https://doi.org/10.2514/3.8566
[research_gilbert_schneider_1981]: https://doi.org/10.1177/002199838101500106
[research_gilbertmichaelg_1987]: https://ntrs.nasa.gov/citations/19870009427
[research_gill_1995]: https://doi.org/10.21236/ada305293
[research_giurgiutiu_pomirleanu_2000]: https://doi.org/10.21236/ada384331
[research_glezer_leonard_2012]: https://doi.org/10.21236/ada564094
[research_gloss_washburn_1978]: https://doi.org/10.2514/3.58347
[research_glossbb_washburnke_1977]: https://ntrs.nasa.gov/citations/19770060346
[research_godwin_frazier_1964]: https://doi.org/10.21236/ad0613504
[research_goizueta_wynn_2022]: https://doi.org/10.2514/1.j062050
[research_goizueta_wynn_2022_b]: https://doi.org/10.2514/1.c036710
[research_goland_1945]: https://doi.org/10.1115/1.4009489
[research_gonabadi_oila_2021]: https://doi.org/10.1016/j.compstruct.2021.114679
[research_gong_wang_2019]: https://doi.org/10.1007/s11071-019-04834-9
[research_gonzalez_silvestre_2020]: https://doi.org/10.2514/1.j058692
[research_gonzalezmontijo_vanness_2026]: https://doi.org/10.1016/j.marstruc.2025.103924
[research_goodrichkennethh_sliwastevenm_1989]: https://ntrs.nasa.gov/citations/19890014097
[research_goodyearaerospacecorpakronoh_1958]: https://doi.org/10.21236/ad0215773
[research_goradiash_bobbittpj_1989]: https://ntrs.nasa.gov/citations/19910014825
[research_goranson_1997]: https://doi.org/10.21236/ada337932
[research_gottzein_cramer_1975]: https://doi.org/10.1080/00423117508968492
[research_goucem_khiri_2023]: https://doi.org/10.15866/irease.v16i5.24129
[research_gowd_2016]: https://doi.org/10.18186/jte.83892
[research_graftonsb_gilberwp_1982]: https://ntrs.nasa.gov/citations/19820055564
[research_grant_stol_2015]: https://doi.org/10.2514/1.g000826
[research_granthamwd_nguyenlt_1976]: https://ntrs.nasa.gov/citations/19770011064
[research_graphite_epoxy_composite_1981]: https://doi.org/10.1016/0010-4361(81)90532-2
[research_grauerjareda_bouchermatthewj_2017]: https://ntrs.nasa.gov/citations/20170001227
[research_graves_sawicki_1994]: https://doi.org/10.1016/0263-8223(94)90088-4
[research_gray_mei_1993]: https://doi.org/10.2514/3.49051
[research_green_1987]: https://doi.org/10.2514/3.45525
[research_greenbergharry_sternfieldleonard_1944]: https://ntrs.nasa.gov/citations/19960024284
[research_greene_1928]: https://doi.org/10.1115/1.4058514
[research_greene_1955]: https://doi.org/10.21236/ad0086878
[research_greene_1956]: https://doi.org/10.21236/ad0092484
[research_greene_1957]: https://doi.org/10.21236/ad0132012
[research_greenhalgh_pastore_1993]: https://doi.org/10.1016/0956-7143(93)90004-r
[research_greenja_1986]: https://ntrs.nasa.gov/citations/19860054140
[research_greszczuk_chao_1975]: https://doi.org/10.21236/ada012269
[research_griffin_eastep_1982]: https://doi.org/10.2514/3.61570
[research_griffin_haerter_1983]: https://doi.org/10.21236/ada133188
[research_griffinbrianjoseph_burkenjohnj_2010]: https://ntrs.nasa.gov/citations/20100037212
[research_griffincharlesf_harvillwilliame_1988]: https://ntrs.nasa.gov/citations/19910019939
[research_griffis_masumura_1981]: https://doi.org/10.1177/002199838101500503
[research_grifo_gulizzi_2023]: https://doi.org/10.1016/j.compstruct.2023.117315
[research_grossschmidt_pahapill_1995]: https://doi.org/10.3176/eng.1995.1.03
[research_gu_ducvo_2023]: https://doi.org/10.2514/1.c036702
[research_gu_taghipour_2022]: https://doi.org/10.1016/j.compstruct.2022.116151
[research_guderley_1956]: https://doi.org/10.2514/8.3697
[research_guinnwileya_1984]: https://ntrs.nasa.gov/citations/19870008278
[research_guinnwileya_risingjerryj_1984]: https://ntrs.nasa.gov/citations/19870008280
[research_guinnwileya_willeycraigs_1983]: https://ntrs.nasa.gov/citations/19870008279
[research_gunnink_1988]: https://doi.org/10.1016/0263-8223(88)90062-1
[research_guo_2021]: https://doi.org/10.1088/1742-6596/1877/1/012019
[research_guo_2021_b]: https://doi.org/10.1088/1742-6596/1877/1/012022
[research_guo_guan_1993]: https://doi.org/10.1080/00423119308969025
[research_guo_hou_2017]: https://doi.org/10.1109/access.2017.2743059
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
[research_haftka_1977]: https://doi.org/10.2514/3.7400
[research_haftmann_debbeler_1988]: https://doi.org/10.2514/3.45707
[research_hagnell_langbeck_2016]: https://doi.org/10.1016/j.compstruct.2016.06.032
[research_hahn_haupt_2022]: https://doi.org/10.1007/s13272-022-00586-2
[research_hahn_kim_1976]: https://doi.org/10.1177/002199837601000205
[research_haley_soloway_2022]: https://doi.org/10.1109/mcs.2022.3171473
[research_hall_1971]: https://doi.org/10.2514/3.59106
[research_hallauer_jr_1983]: https://doi.org/10.21236/ada148333
[research_hallissyjb_ayerstg_1977]: https://ntrs.nasa.gov/citations/19770026171
[research_hamada_saitoh_2019]: https://doi.org/10.1016/j.ifacol.2019.11.125
[research_hamiltonbriank_petersjamesr_1989]: https://ntrs.nasa.gov/citations/19890015786
[research_hammer_bright_1998]: https://doi.org/10.21236/ada359476
[research_hamza_akram_2026]: https://doi.org/10.1016/j.amf.2026.200334
[research_han_glower_1985]: https://doi.org/10.21236/ada152209
[research_han_pei_2026]: https://doi.org/10.1109/maes.2025.3566023
[research_han_yu_2019]: https://doi.org/10.2514/1.c035282
[research_han_zhang_2022]: https://doi.org/10.1016/j.buildenv.2022.109362
[research_hanagud_craig_1989]: https://doi.org/10.1177/002199838902300502
[research_hancock_1992]: https://doi.org/10.1017/s0001924000050442
[research_hancockregis_fullertongordon_1992]: https://ntrs.nasa.gov/citations/19930054849
[research_hanman_yao_2025]: https://doi.org/10.3390/fluids10020027
[research_hansoncurt_schaeferjacob_2011]: https://ntrs.nasa.gov/citations/20110023802
[research_hansongd_stengelrf_1981]: https://ntrs.nasa.gov/citations/19810059678
[research_hansongd_stengelrf_1983]: https://ntrs.nasa.gov/citations/19830035279
[research_harper_robertp_1955]: https://doi.org/10.21236/ad0092496
[research_harriscd_1974]: https://ntrs.nasa.gov/citations/19830002756
[research_harriscd_1974_b]: https://ntrs.nasa.gov/citations/19830002761
[research_hart_1956]: https://doi.org/10.21236/ad0108104
[research_hartini_bachtiar_2026]: https://doi.org/10.28989/vortex.v7i1.3819
[research_harvillwe_kizerja_1976]: https://ntrs.nasa.gov/citations/19770004089
[research_hashiiwendyn_thompsonrandolphc_2018]: https://ntrs.nasa.gov/citations/20180004483
[research_hayashi_1949]: https://doi.org/10.2534/jjasnaoe1903.1949.85
[research_hayashi_1988]: https://doi.org/10.1080/00423118808969254
[research_hebbar_pashilkar_2016]: https://doi.org/10.14429/dsj.66.9196
[research_heckl_lyon_1962]: https://doi.org/10.21236/ad0290798
[research_heegjennifer_2006]: https://ntrs.nasa.gov/citations/20060018311
[research_heegjennifer_spaincharlesv_2004]: https://ntrs.nasa.gov/citations/20040068163
[research_heegjennifer_spaincharlesv_2005]: https://ntrs.nasa.gov/citations/20050203672
[research_heinrich_vogt_2022]: https://doi.org/10.2514/1.g006412
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
[research_herrmann_benasher_2016]: https://doi.org/10.2514/1.c033517
[research_herrmanng_nematnassers_1966]: https://ntrs.nasa.gov/citations/19660053477
[research_hertztj_shirkmh_1982]: https://ntrs.nasa.gov/citations/19820035536
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
[research_hirai_kline_1973]: https://doi.org/10.1177/002199837300700202
[research_hirai_satoh_1980]: https://doi.org/10.1109/tac.1980.1102355
[research_hirato_shen_2019]: https://doi.org/10.2514/1.c035124
[research_hirsch_mccormick_1966]: https://doi.org/10.2514/3.43778
[research_hitch_1978]: https://doi.org/10.2514/3.58464
[research_hitzel_2017]: https://doi.org/10.2514/1.c034025
[research_hitzel_osterhuber_2018]: https://doi.org/10.2514/1.c034473
[research_hodgkinson_2017]: https://doi.org/10.4050/jahs.62.047001
[research_hodgkinson_lamanna_1976]: https://doi.org/10.1017/s0001924000033510
[research_hofmann_kezer_1962]: https://doi.org/10.21236/ad0403433
[research_hogan_rinde_1978]: https://doi.org/10.21236/ada062030
[research_holst_1988]: https://doi.org/10.2514/3.45706
[research_holst_brown_1983]: https://doi.org/10.2514/3.8069
[research_honeycomb_laminate_composite_1979]: https://doi.org/10.1016/0010-4361(79)90475-0
[research_hong_cheong_1993]: https://doi.org/10.1016/0013-7944(93)90174-q
[research_hong_kim_2024]: https://doi.org/10.2514/1.c037715
[research_hong_ko_2015]: https://doi.org/10.9728/dcs.2015.16.1.123
[research_hopkinsej_yeesc_1977]: https://ntrs.nasa.gov/citations/19770014154
[research_hopwood_gresham_2023]: https://doi.org/10.2514/1.g007016
[research_horton_mayers_1965]: https://doi.org/10.21236/ad0622585
[research_hortsen_boer_1983]: https://doi.org/10.21236/ada130488
[research_hoseini_hodges_2019]: https://doi.org/10.2514/1.c035098
[research_housnerjm_steinm_1974]: https://ntrs.nasa.gov/citations/19740024243
[research_houtman_timme_2023]: https://doi.org/10.1017/flo.2023.8
[research_how_2004]: https://doi.org/10.21236/ada420937
[research_howard_oleary_1994]: https://doi.org/10.2514/3.46578
[research_howdyshell_trovillion_1998]: https://doi.org/10.21236/ada354825
[research_hu_qiu_2026]: https://doi.org/10.1080/13504851.2026.2681706
[research_huang_li_2026]: https://doi.org/10.2514/1.c038842
[research_huang_wang_2024]: https://doi.org/10.1007/s00158-024-03809-8
[research_huang_yang_2019]: https://doi.org/10.2514/1.j058211
[research_huang_yu_2022]: https://doi.org/10.2514/1.j060923
[research_hubener_luckner_2026]: https://doi.org/10.1007/s13272-025-00930-2
[research_huff_ww_1949]: https://doi.org/10.21236/ad0035641
[research_huffmanjk_1975]: https://ntrs.nasa.gov/citations/19750019955
[research_huiping_yutian_1989]: https://doi.org/10.1016/b978-0-08-040185-0.50024-5
[research_human_supervisory_2015]: https://doi.org/10.1109/mcs.2015.2471056
[research_hummel_oelker_1994]: https://doi.org/10.2514/3.46573
[research_humphreysjennings_lappas_2020]: https://doi.org/10.3390/aerospace7050051
[research_hunn_1953]: https://doi.org/10.1017/s0368393100131128
[research_hunter_2003]: https://doi.org/10.21236/ada413499
[research_hurley_1975]: https://doi.org/10.2514/3.49684
[research_hutchinson_2014]: https://doi.org/10.21236/ada607283
[research_hybrid_composite_1978]: https://doi.org/10.1016/0010-4361(78)90462-7
[research_iannelli_marcos_2018]: https://doi.org/10.2514/1.g003165
[research_ibren_sulaeman_2020]: https://doi.org/10.37934/cfdl.12.4.7989
[research_ignatyev_khrabrov_2018]: https://doi.org/10.3390/aerospace5010026
[research_ilcewiczlb_walkerth_1991]: https://ntrs.nasa.gov/citations/19940028357
[research_iliffkw_mainere_1978]: https://ntrs.nasa.gov/citations/19780010132
[research_iliffkw_mainere_1981]: https://ntrs.nasa.gov/citations/19820030345
[research_im_kong_2025]: https://doi.org/10.1109/access.2025.3526769
[research_inger_1983]: https://doi.org/10.21236/ada123389
[research_ingramwc_yiplp_1986]: https://ntrs.nasa.gov/citations/19870026764
[research_interlaminar_shear_1992]: https://doi.org/10.1016/0010-4361(92)90207-b
[research_introduction_to_2017]: https://doi.org/10.2514/1.c034808
[research_ioannis_ioannis_2026]: https://doi.org/10.70322/dav.2026.10005
[research_irvine_1968]: https://doi.org/10.21236/ad0680316
[research_iryani_kadir_2019]: https://doi.org/10.5373/jardcs/v11sp11/20193066
[research_ishmaelsd_wierzbanowskit_1985]: https://ntrs.nasa.gov/citations/19860060204
[research_ishmaelstephend_smithrogerse_1990]: https://ntrs.nasa.gov/citations/19920033428
[research_isogai_1979]: https://doi.org/10.2514/3.61226
[research_isogai_1981]: https://doi.org/10.2514/3.7853
[research_isogai_1988]: https://doi.org/10.6089/jscm.14.96
[research_isogai_1989]: https://doi.org/10.2514/3.45883
[research_isogai_1992]: https://doi.org/10.1016/0889-9746(92)90017-w
[research_ito_iwashita_2017]: https://doi.org/10.2534/jjasnaoe.25.63
[research_ivler_truong_2022]: https://doi.org/10.4050/jahs.67.012002
[research_jacobson_1952]: https://doi.org/10.21236/ad0029208
[research_jacobson_joshi_1978]: https://doi.org/10.2514/3.58351
[research_jafari_mashadi_2022]: https://doi.org/10.1080/00423114.2022.2056490
[research_jaffarsyedmohamedali_shahzatulsakinahbintiharon_2021]: https://doi.org/10.37934/cfdl.13.11.7886
[research_jalalnezhad_2026]: https://doi.org/10.1007/s40430-025-06274-6
[research_jamesafranklin_1993]: https://ntrs.nasa.gov/citations/19940008824
[research_jamesmluckring_2003]: https://ntrs.nasa.gov/citations/20040010871
[research_janardhan_grandhi_2003]: https://doi.org/10.21236/ada417106
[research_janecek_1986]: https://doi.org/10.21236/ada179141
[research_jaredagrauer_2018]: https://ntrs.nasa.gov/citations/20190000878
[research_jarrellrelliott_1976]: https://ntrs.nasa.gov/citations/19770045950
[research_jarviscr_1967]: https://ntrs.nasa.gov/citations/19670041319
[research_jarviscr_1975]: https://ntrs.nasa.gov/citations/19750010174
[research_jarviscr_szalaikj_1981]: https://ntrs.nasa.gov/citations/19810010480
[research_jegleydawnc_bushharoldg_1997]: https://ntrs.nasa.gov/citations/19970022698
[research_jegleydawnc_bushharoldg_2001]: https://ntrs.nasa.gov/citations/20010047392
[research_jegleydawnc_bushharoldg_2001_b]: https://ntrs.nasa.gov/citations/20030012585
[research_jegleydawnc_lovejoyandrewe_2001]: https://ntrs.nasa.gov/citations/20010022369
[research_jegleydawnc_wijayratnedulnathd_2004]: https://ntrs.nasa.gov/citations/20040200977
[research_jelliott_1977]: https://ntrs.nasa.gov/citations/19780028448
[research_jeng_payne_1995]: https://doi.org/10.2514/3.46724
[research_jenksge_henryhf_1977]: https://ntrs.nasa.gov/citations/19770014139
[research_jenney_schreadley_1982]: https://doi.org/10.21236/ada117244
[research_jenney_schreadley_1984]: https://doi.org/10.21236/ada144283
[research_jensen_crawley_1982]: https://doi.org/10.1177/073168448200100305
[research_jensen_crawley_1984]: https://doi.org/10.2514/3.48463
[research_jewell_heffley_1979]: https://doi.org/10.2514/3.58536
[research_ji_kim_2023]: https://doi.org/10.3390/aerospace10040365
[research_ji_lu_2022]: https://doi.org/10.1016/j.ast.2022.107501
[research_jia_ezhilarasu_2023]: https://doi.org/10.3390/app132413120
[research_jia_sun_2023]: https://doi.org/10.3390/drones7030200
[research_jiang_tong_2022]: https://doi.org/10.1088/1742-6596/2235/1/012001
[research_jianhong_yanxiang_2026]: https://doi.org/10.1108/aeat-01-2025-0009
[research_jiao_jiang_2015]: https://doi.org/10.7763/ijmlc.2015.v5.524
[research_jin_xue_2026]: https://doi.org/10.3390/act15060337
[research_johnson_1965]: https://doi.org/10.21236/ad0617567
[research_johnson_1972]: https://doi.org/10.21236/ad0754909
[research_johnson_1973]: https://doi.org/10.1016/0020-7683(73)90068-1
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
[research_jones_nisbet_1976]: https://doi.org/10.1017/s0001924000034138
[research_jonnalagadda_sawant_2015]: https://doi.org/10.1016/j.compstruct.2015.06.023
[research_jou_metcalfe_1984]: https://doi.org/10.21236/ada150123
[research_juhasz_tischler_2023]: https://doi.org/10.2514/1.c037085
[research_junyi_xinbing_2021]: https://doi.org/10.1088/1757-899x/1102/1/012004
[research_k_deodhare_2023]: https://doi.org/10.61653/joast.v75i2.2023.58
[research_kabaliswaran_das_2026]: https://doi.org/10.2514/1.c038269
[research_kafkas_kilimtzidis_2021]: https://doi.org/10.3390/aerospace8120398
[research_kalnins_1968]: https://doi.org/10.21236/ad0686446
[research_kalugin_voropaev_2022]: https://doi.org/10.3103/s1068799822030126
[research_kamaletdinova_romanov_2024]: https://doi.org/10.17150/2713-1734.2024.6(1).60-77
[research_kambampati_smith_2017]: https://doi.org/10.2514/1.c034195
[research_kanazaki_setoguchi_2023]: https://doi.org/10.3390/aerospace10090790
[research_kapania_bergen_1991]: https://doi.org/10.2514/3.59930
[research_kapania_issac_1994]: https://doi.org/10.2514/3.59995
[research_kapaniarakeshk_issacj_1997]: https://ntrs.nasa.gov/citations/19970021182
[research_karalmichael_2001]: https://ntrs.nasa.gov/citations/20010033249
[research_karimikelayeh_djavareshkian_2024]: https://doi.org/10.1061/jaeeez.aseng-5073
[research_karniadakis_2004]: https://doi.org/10.21236/ada420891
[research_karpouzian_1991]: https://doi.org/10.2514/3.10655
[research_kasimbiber_trentonwhite_2019]: https://doi.org/10.17265/2159-5275/2019.06.004
[research_kassem_yang_2021]: https://doi.org/10.1007/s42417-020-00267-6
[research_kataoka_dol_1986]: https://doi.org/10.1299/jsme1958.29.393
[research_katz_davidovitch_1986]: https://doi.org/10.2514/3.25851
[research_katz_levin_1986]: https://doi.org/10.2514/3.45386
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
[research_key_1971]: https://doi.org/10.21236/ad0725746
[research_khadse_karmore_2016]: https://doi.org/10.1016/j.procs.2016.02.059
[research_khalil_asaro_2022]: https://doi.org/10.2514/1.c036426
[research_khalil_bauknecht_2024]: https://doi.org/10.2514/1.c037503
[research_khalil_fezans_2020]: https://doi.org/10.1017/aer.2020.85
[research_kholodar_2016]: https://doi.org/10.2514/1.c033772
[research_kieffer_2006]: https://doi.org/10.21236/ada462805
[research_kielb_1975]: https://doi.org/10.2514/3.44437
[research_kilgore_averett_1964]: https://doi.org/10.2514/3.43598
[research_kilimtzidis_giannaros_2023]: https://doi.org/10.1016/j.compstruct.2023.116897
[research_kim_choi_2015]: https://doi.org/10.12985/ksaa.2015.23.1.067
[research_kim_kang_2025]: https://doi.org/10.6112/kscfe.2025.30.1.082
[research_kim_kunz_2017]: https://doi.org/10.2514/1.g002306
[research_kim_shin_2016]: https://doi.org/10.7234/composres.2016.29.6.369
[research_kineyko_1982]: https://doi.org/10.21236/ada119003
[research_king_johnson_1986]: https://doi.org/10.2514/3.9448
[research_kinney_1963]: https://doi.org/10.21236/ad0414572
[research_kirsch_montagnier_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.102930
[research_kish_mosle_1997]: https://doi.org/10.21236/ada286959
[research_kishi_kanazaki_2016]: https://doi.org/10.4236/jfcmv.2016.41004
[research_kishi_kanazaki_2022]: https://doi.org/10.2514/1.c036422
[research_kisslinger_wendl_1971]: https://doi.org/10.21236/ad0727762
[research_kizildeniz_kiyak_2025]: https://doi.org/10.1108/aeat-03-2025-0127
[research_klasztorny_nycz_2018]: https://doi.org/10.1016/j.compstruct.2017.10.046
[research_kleinrw_hollisterwm_1982]: https://ntrs.nasa.gov/citations/19820026186
[research_kleinrw_lapinsm_1982]: https://ntrs.nasa.gov/citations/19820036249
[research_klepl_1995]: https://doi.org/10.2514/3.46702
[research_klinarwj_kubiaket_1975]: https://ntrs.nasa.gov/citations/19760045906
[research_klotzschem_1984]: https://ntrs.nasa.gov/citations/19870019180
[research_klug_ullah_2023]: https://doi.org/10.1007/s13272-023-00645-2
[research_klyde_harris_2004]: https://doi.org/10.21236/ada426452
[research_knackstedt_1952]: https://doi.org/10.21236/ad0008717
[research_knaussjf_stonerh_1982]: https://ntrs.nasa.gov/citations/19830039267
[research_knight_1982]: https://doi.org/10.1177/002199838201600206
[research_knightondonnal_1992]: https://ntrs.nasa.gov/citations/19930029267
[research_knoxseith_1963]: https://doi.org/10.21236/ad0438911
[research_kobayashi_torisaki_1986]: https://doi.org/10.1299/jsme1958.29.1536
[research_kobelev_2019]: https://doi.org/10.1108/mmms-02-2018-0019
[research_koenig_1984]: https://doi.org/10.21236/ada150667
[research_kohara_tomoeda_2016]: https://doi.org/10.1299/jsmecs.2016.54._1408-1_
[research_kohlman_1979]: https://doi.org/10.2514/3.58513
[research_kohnhorst_magnacca_1980]: https://doi.org/10.21236/ada094688
[research_kokotovic_murray_2000]: https://doi.org/10.21236/ada387455
[research_kolesar_1971]: https://doi.org/10.21236/ad0734236
[research_komarov_zinchenko_2023]: https://doi.org/10.20535/0203-3771452023290873
[research_komnatska_bondarenko_2017]: https://doi.org/10.15407/usim.2017.04.024
[research_konar_mahesh_1974]: https://doi.org/10.21236/ada002320
[research_koo_lee_1994]: https://doi.org/10.1016/0045-7949(94)90293-3
[research_kopecki_2016]: https://doi.org/10.1108/aeat-10-2012-0187
[research_kornev_ambrozhevich_2021]: https://doi.org/10.3103/s1068799821010049
[research_koscielny_1983]: https://doi.org/10.21236/ada140558
[research_kosyanchuk_selvesyuk_2015]: https://doi.org/10.3846/16487788.2015.1015290
[research_kosyanchuk_zheltov_2021]: https://doi.org/10.1088/1742-6596/1864/1/012005
[research_kousen_bendiksen_1994]: https://doi.org/10.2514/3.46644
[research_kozhanov_suvorova_2022]: https://doi.org/10.52348/2712-8873_mmtt_2022_5_45
[research_krachmalnick_vetsch_1968]: https://doi.org/10.2514/3.43925
[research_kraftchristophercjr_reederjp_1948]: https://ntrs.nasa.gov/citations/20050028754
[research_kratochvil_valenta_2024]: https://doi.org/10.1007/s13272-024-00745-7
[research_krener_2001]: https://doi.org/10.21236/ada430327
[research_kriechbaum_stineman_1972]: https://doi.org/10.2514/3.58994
[research_kroo_1982]: https://doi.org/10.2514/3.61557
[research_kruger_meddaikar_2022]: https://doi.org/10.3390/aerospace9100535
[research_krzywoblocki_1943]: https://doi.org/10.2514/8.11023
[research_kubica_livet_1995]: https://doi.org/10.1016/0967-0661(95)00119-f
[research_kuhlberg_newirth_1976]: https://doi.org/10.2514/3.58656
[research_kuhn_1975]: https://doi.org/10.21236/ada955473
[research_kulikov_2020]: https://doi.org/10.1007/s10958-020-04994-9
[research_kumar_asha_2025]: https://doi.org/10.1016/j.prostr.2025.08.045
[research_kumarshakya_sekharpadhee_2023]: https://doi.org/10.1016/j.matpr.2023.05.731
[research_kuojiun_pongjeu_1989]: https://doi.org/10.1016/0045-7949(89)90030-8
[research_kurniawan_2022]: https://doi.org/10.31543/jtm.v6i1.724
[research_kurz_1963]: https://doi.org/10.21236/ad0414370
[research_kurzhalspr_1978]: https://ntrs.nasa.gov/citations/19790008693
[research_kusni_widiramdhani_2021]: https://doi.org/10.1088/1757-899x/1173/1/012058
[research_kuttieri_sinha_2023]: https://doi.org/10.61653/joast.v64i3.2012.465
[research_kuvshinov_2016]: https://doi.org/10.1615/tsagiscij.2016017070
[research_kuvshinov_2016_b]: https://doi.org/10.1615/tsagiscij.2017020079
[research_kuvshinov_lazurin_2019]: https://doi.org/10.1615/tsagiscij.2020033338
[research_kuvshinov_leontiev_2019]: https://doi.org/10.1615/tsagiscij.2019031121
[research_kuznetsov_kartashov_1980]: https://doi.org/10.1007/bf00884879
[research_kwatny_bennett_1991]: https://doi.org/10.1109/9.100946
[research_lai_2024]: https://doi.org/10.54254/2755-2721/91/20241080
[research_lai_young_1995]: https://doi.org/10.1016/0263-8223(94)00017-4
[research_laitone_1978]: https://doi.org/10.2514/3.58457
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
[research_langston_1967]: https://doi.org/10.21236/ad0813281
[research_lapinsm_kleinrw_1982]: https://ntrs.nasa.gov/citations/19820055547
[research_larsonrichardr_1987]: https://ntrs.nasa.gov/citations/19870007386
[research_latency_control_2025]: https://doi.org/10.38007/dps.2025.040102
[research_lavretsky_2019]: https://doi.org/10.2514/1.g004328
[research_le_2026]: https://doi.org/10.1007/s40435-026-02198-8
[research_lee_1977]: https://doi.org/10.21236/ada038281
[research_lee_1995]: https://doi.org/10.1017/s0001924000028815
[research_lee_cho_1991]: https://doi.org/10.1016/0045-7949(91)90084-y
[research_lee_cho_1991_b]: https://doi.org/10.2514/3.10656
[research_lee_eyi_1993]: https://doi.org/10.2514/3.46419
[research_lee_kim_1994]: https://doi.org/10.2514/3.46667
[research_lee_kim_1995]: https://doi.org/10.2514/3.46803
[research_lee_kim_2020]: https://doi.org/10.1007/s12555-018-9403-7
[research_lee_lee_1990]: https://doi.org/10.1016/0045-7949(90)90019-x
[research_lee_lee_2023]: https://doi.org/10.5139/jksas.2023.51.11.751
[research_lee_lua_2025]: https://doi.org/10.2514/1.c038014
[research_lee_lua_2026]: https://doi.org/10.2514/1.c038959
[research_lee_mall_1989]: https://doi.org/10.1177/002199838902300403
[research_lee_ohman_1984]: https://doi.org/10.2514/3.44987
[research_lee_ohman_1984_b]: https://doi.org/10.2514/3.56742
[research_lee_sheu_1994]: https://doi.org/10.1002/oca.4660150204
[research_lee_singh_2018]: https://doi.org/10.2514/1.g003087
[research_lee_tang_1989]: https://doi.org/10.2514/3.45785
[research_lehman_stearman_1977]: https://doi.org/10.21236/ada039245
[research_leighton_1978]: https://doi.org/10.21236/ada061891
[research_leitch_stodieck_2024]: https://doi.org/10.2139/ssrn.4786120
[research_leitch_stodieck_2025]: https://doi.org/10.1016/j.compstruct.2025.119706
[research_lemaysp_batillsm_1988]: https://ntrs.nasa.gov/citations/19880053508
[research_lemmon_coleman_1973]: https://doi.org/10.2514/3.6801
[research_leondes_rankine_1972]: https://doi.org/10.2514/3.58972
[research_lerner_markowitz_1979]: https://doi.org/10.2514/3.58486
[research_lerro_brandl_2020]: https://doi.org/10.3390/aerospace7050063
[research_lesoinne_2007]: https://doi.org/10.21236/ada481320
[research_levi_nelson_1964]: https://doi.org/10.2514/3.43579
[research_li_2023]: https://doi.org/10.54254/2755-2721/10/20230134
[research_li_daronch_2019]: https://doi.org/10.1016/j.ast.2019.105354
[research_li_gong_2019]: https://doi.org/10.1016/j.jfluidstructs.2018.10.011
[research_li_hu_2025]: https://doi.org/10.1016/j.ifacol.2025.11.380
[research_li_jin_2017]: https://doi.org/10.1016/j.ast.2016.11.029
[research_li_kou_2024]: https://doi.org/10.1016/j.jfluidstructs.2023.104055
[research_li_li_2025]: https://doi.org/10.1109/taes.2025.3596214
[research_li_luo_2023]: https://doi.org/10.1186/s42774-023-00155-z
[research_li_miranda_2026]: https://doi.org/10.1016/j.compstruct.2026.120662
[research_li_qian_2024]: https://doi.org/10.3390/aerospace11121015
[research_li_qin_2020]: https://doi.org/10.1016/j.ast.2019.105622
[research_li_qin_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103407
[research_li_qin_2021_b]: https://doi.org/10.1016/j.ast.2021.106919
[research_li_qin_2022]: https://doi.org/10.3390/app122010537
[research_li_shang_2025]: https://doi.org/10.1186/s10033-025-01219-5
[research_li_shen_2026]: https://doi.org/10.3390/aerospace13040325
[research_li_shi_2021]: https://doi.org/10.3390/aerospace8070176
[research_li_sun_2022]: https://doi.org/10.1109/access.2022.3157878
[research_li_tang_2020]: https://doi.org/10.1016/j.ins.2019.10.039
[research_li_wan_2021]: https://doi.org/10.3390/app112411800
[research_li_wang_2018]: https://doi.org/10.1016/j.ast.2018.01.001
[research_li_wang_2021]: https://doi.org/10.3390/app11020505
[research_li_wang_2026]: https://doi.org/10.1063/5.0319218
[research_li_xiong_2025]: https://doi.org/10.1088/1742-6596/3044/1/012002
[research_li_yang_2017]: https://doi.org/10.2514/1.c033670
[research_li_yang_2023]: https://doi.org/10.3390/aerospace10100866
[research_li_yuan_2022]: https://doi.org/10.34133/2022/9790131
[research_li_zhang_2024]: https://doi.org/10.1080/0305215x.2024.2420746
[research_liang_ren_2018]: https://doi.org/10.2514/1.g003157
[research_liao_sun_1993]: https://doi.org/10.2514/3.11865
[research_libeskind_minecci_1973]: https://doi.org/10.21236/ada326073
[research_librescu_khdeir_1988]: https://doi.org/10.2514/3.10050
[research_librescu_simovich_1988]: https://doi.org/10.2514/3.45572
[research_librescu_song_1992]: https://doi.org/10.1016/0961-9526(92)90039-9
[research_librescu_thangjitham_1991]: https://doi.org/10.2514/3.46004
[research_lichota_2023]: https://doi.org/10.1108/aeat-01-2023-0013
[research_lieferrandallk_1990]: https://ntrs.nasa.gov/citations/19900020073
[research_lifshits_ryzhov_1978]: https://doi.org/10.1007/bf01094463
[research_lijewski_1988]: https://doi.org/10.2514/3.26018
[research_lin_chin_1994]: https://doi.org/10.2514/3.46547
[research_lin_lu_1989]: https://doi.org/10.2514/3.10228
[research_lindrickc_brennermartinj_1997]: https://ntrs.nasa.gov/citations/19980018481
[research_lindsay_fikes_1976]: https://doi.org/10.21236/adb014423
[research_lindsay_jordan_1975]: https://doi.org/10.21236/ada009137
[research_liu_2018]: https://doi.org/10.1049/joe.2018.9016
[research_liu_2019]: https://doi.org/10.1177/0020294019858106
[research_liu_an_2018]: https://doi.org/10.1109/tmech.2018.2800089
[research_liu_dong_2021]: https://doi.org/10.1016/j.cja.2020.04.026
[research_liu_feng_2023]: https://doi.org/10.3390/s23218903
[research_liu_gao_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.103098
[research_liu_gao_2020_b]: https://doi.org/10.1007/s11071-020-05553-2
[research_liu_ji_2024]: https://doi.org/10.1007/s12555-022-0318-y
[research_liu_li_2026]: https://doi.org/10.3390/electronics15163532
[research_liu_liou_2009]: https://doi.org/10.21236/ada590187
[research_liu_sun_2016]: https://doi.org/10.1155/2016/1060574
[research_liu_sun_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000712
[research_liu_sun_2017_b]: https://doi.org/10.1016/j.ast.2017.10.006
[research_liu_sun_2022]: https://doi.org/10.3390/en15030787
[research_liu_toropov_2015]: https://doi.org/10.1007/s00158-015-1244-x
[research_liu_wang_2019]: https://doi.org/10.1016/j.jfluidstructs.2019.04.010
[research_liu_wang_2026]: https://doi.org/10.1016/j.cej.2026.180391
[research_liu_zhang_2023]: https://doi.org/10.1016/j.ijmultiphaseflow.2022.104286
[research_liu_zheng_2025]: https://doi.org/10.2514/1.c038200
[research_livne_2018]: https://doi.org/10.2514/1.c034442
[research_liwesleyw_pakchangi_2014]: https://ntrs.nasa.gov/citations/20140010035
[research_lockwp_petersenwr_1975]: https://ntrs.nasa.gov/citations/19750010176
[research_loh_1986]: https://doi.org/10.21236/ada168970
[research_loja_barbosa_2017]: https://doi.org/10.1016/j.compstruct.2017.09.046
[research_lokoswilliama_1990]: https://ntrs.nasa.gov/citations/19920053312
[research_lombardi_1995]: https://doi.org/10.2514/3.46804
[research_lombardi_morelli_1994]: https://doi.org/10.2514/3.46517
[research_lombardi_vicini_1994]: https://doi.org/10.1017/s0001924000049733
[research_long_mu_2021]: https://doi.org/10.1016/j.compstruct.2020.113005
[research_loos_springer_1983]: https://doi.org/10.21236/ada130071
[research_loser_1985]: https://doi.org/10.1016/0094-5765(85)90029-3
[research_lottati_1985]: https://doi.org/10.2514/3.45238
[research_lottati_1987]: https://doi.org/10.2514/3.45523
[research_lottati_1988]: https://doi.org/10.2514/3.45588
[research_loughlan_2019]: https://doi.org/10.1016/j.tws.2019.01.045
[research_lovatt_1986]: https://doi.org/10.21236/ada179591
[research_lovejoyandrewe_scottistephenj_2019]: https://ntrs.nasa.gov/citations/20200002432
[research_lu_1994]: https://doi.org/10.1016/s1474-6670(17)47575-6
[research_lu_fang_2018]: https://doi.org/10.1016/j.conengprac.2018.04.005
[research_lu_ma_2019]: https://doi.org/10.1109/access.2019.2956818
[research_lu_murthy_1990]: https://doi.org/10.2514/3.45947
[research_luattnguyen_williampgilbert_1980]: https://ntrs.nasa.gov/citations/19800020743
[research_lucas_1978]: https://doi.org/10.21236/adb028240
[research_luo_bao_1988]: https://doi.org/10.2514/3.45620
[research_lv_lei_2019]: https://doi.org/10.1088/1742-6596/1300/1/012085
[research_ma_guo_2015]: https://doi.org/10.1016/j.ast.2015.06.003
[research_ma_zhou_2025]: https://doi.org/10.1109/access.2024.3519800
[research_mabboux_pommierbudinger_2024]: https://doi.org/10.1016/j.ast.2023.108778
[research_mackallda_pickettmd_1988]: https://ntrs.nasa.gov/citations/19880011793
[research_mackalldalea_allenjamesg_1989]: https://ntrs.nasa.gov/citations/19900023436
[research_mackalldalea_allenjamesg_1991]: https://ntrs.nasa.gov/citations/19910015825
[research_magee_taylor_1971]: https://doi.org/10.21236/ad0735733
[research_magliacano_tufano_2025]: https://doi.org/10.1016/j.compstruct.2025.119675
[research_magness_robinson_1993]: https://doi.org/10.2514/3.11786
[research_magnus_yoshihara_1975]: https://doi.org/10.2514/3.60585
[research_mahapatra_halbe_2024]: https://doi.org/10.1016/j.ifacol.2024.05.017
[research_mahboub_rouabah_2022]: https://doi.org/10.29354/diag/151039
[research_mahgoub_elbadawy_2022]: https://doi.org/10.1007/s11071-022-07213-z
[research_mahmood_2025]: https://doi.org/10.1177/10775463241312815
[research_mahroni_2021]: https://doi.org/10.28989/vortex.v1i2.902
[research_mahulkar_2010]: https://doi.org/10.21236/ada534168
[research_malcom_1969]: https://doi.org/10.2514/3.59426
[research_malcomlg_husbandjh_1976]: https://ntrs.nasa.gov/citations/19760058464
[research_malekpour_abdali_2025]: https://doi.org/10.1016/j.addlet.2025.100297
[research_malik_akhtar_2017]: https://doi.org/10.15632/jtam-pl.55.3.963
[research_mamedov_paryshev_2018]: https://doi.org/10.1615/tsagiscij.2018027114
[research_mamonova_soudakov_2019]: https://doi.org/10.1088/1742-6596/1268/1/012067
[research_mandal_gu_2016]: https://doi.org/10.3390/aerospace3040042
[research_mannmj_campbellrl_1983]: https://ntrs.nasa.gov/citations/19830057468
[research_mannmj_campbellrl_1984]: https://ntrs.nasa.gov/citations/19840010093
[research_mannmj_mercerce_1985]: https://ntrs.nasa.gov/citations/19860026297
[research_mannmj_mercerce_1986]: https://ntrs.nasa.gov/citations/19870002269
[research_mansy_faruque_2023]: https://doi.org/10.2514/1.c037179
[research_mant_1972]: https://doi.org/10.1108/eb034920
[research_manzoor_maqsood_2016]: https://doi.org/10.15866/irease.v9i3.8119
[research_mao_dou_2018]: https://doi.org/10.1002/rnc.4349
[research_mao_li_2020]: https://doi.org/10.1155/2020/1426193
[research_mao_xie_2019]: https://doi.org/10.1155/2019/5847627
[research_mar_lin_1979]: https://doi.org/10.1177/002199837901300402
[research_marano_belardo_2022]: https://doi.org/10.3390/aerospace9070335
[research_marilyneogburn_johnvfoster_1991]: https://ntrs.nasa.gov/citations/19910063214
[research_marin_graciani_2022]: https://doi.org/10.1016/j.compstruct.2021.115088
[research_marques_natarajan_2017]: https://doi.org/10.1016/j.compstruct.2017.01.062
[research_marqui_bueno_2017]: https://doi.org/10.1016/j.jfluidstructs.2017.01.010
[research_marr_roderick_1975]: https://doi.org/10.4050/jahs.20.23
[research_martin_1978]: https://doi.org/10.21236/ada066904
[research_martin_pardo_2017]: https://doi.org/10.1007/s00362-017-0900-1
[research_martincodenverco_1966]: https://doi.org/10.21236/ad0378020
[research_martinezheredia_fernandezprada_2026]: https://doi.org/10.3390/en19153498
[research_maruyama_ogino_2024]: https://doi.org/10.1007/s40194-024-01748-y
[research_masonml_caponefj_1983]: https://ntrs.nasa.gov/citations/19830013890
[research_masuda_shimosawa_2016]: https://doi.org/10.2322/tastj.14.pe_13
[research_mateergeorgec_seegmillerhlee_1987]: https://ntrs.nasa.gov/citations/19870057640
[research_mathur_huang_2026]: https://doi.org/10.2514/1.j066300
[research_matrix_cracking_1985]: https://doi.org/10.1016/0010-4361(85)90361-1
[research_matsuki_nishiyama_2018]: https://doi.org/10.1108/aeat-03-2016-0052
[research_mayer_prowe_2016]: https://doi.org/10.1016/j.compstruct.2016.01.023
[research_mccomb_hayduk_1987]: https://doi.org/10.2514/3.45500
[research_mccutchen_1980]: https://doi.org/10.2514/3.44655
[research_mcdonald_2001]: https://doi.org/10.21236/ada387726
[research_mcdonald_farris_1964]: https://doi.org/10.21236/ad0603704
[research_mcgough_moses_1974]: https://doi.org/10.21236/ada006411
[research_mcgurk_stodieck_2024]: https://doi.org/10.1016/j.compstruct.2023.117794
[research_mcintosh_mishra_2024]: https://doi.org/10.2514/1.g008002
[research_mckeehen_cord_1997]: https://doi.org/10.21236/ada327802
[research_mckillip_1991]: https://doi.org/10.4050/jahs.36.4
[research_mckinney_1972]: https://doi.org/10.1177/002199837200600115
[research_mcklnney_dollyhlgh_1971]: https://doi.org/10.2514/3.59148
[research_mcmaster_schenk_1974]: https://doi.org/10.2514/3.59224
[research_mcruerd_johnstond_1986]: https://ntrs.nasa.gov/citations/19870030478
[research_mefford_voss_1948]: https://doi.org/10.21236/adb812175
[research_mehmedoral_1988]: https://ntrs.nasa.gov/citations/19880013862
[research_mei_wang_2021]: https://doi.org/10.1016/j.jmapro.2021.03.052
[research_meirovitch_1995]: https://doi.org/10.21236/ada293689
[research_memon_white_2021]: https://doi.org/10.1017/aer.2021.87
[research_menet_menart_1993]: https://doi.org/10.1007/bf00194012
[research_meng_jiang_2025]: https://doi.org/10.1088/1742-6596/3026/1/012013
[research_menon_yousefpor_1996]: https://doi.org/10.21236/ada436537
[research_mertaugh_1998]: https://doi.org/10.21236/ada350674
[research_mhenni_choley_2016]: https://doi.org/10.1016/j.ifacol.2016.07.076
[research_micheli_2024]: https://doi.org/10.2514/1.g008146
[research_micks_1950]: https://doi.org/10.2514/8.1784
[research_mihailaandres_rosu_2019]: https://doi.org/10.1051/itmconf/20192402010
[research_mijovic_1985]: https://doi.org/10.1177/002199838501900205
[research_miller_1965]: https://doi.org/10.2514/3.43649
[research_miller_1986]: https://doi.org/10.2514/3.45268
[research_miller_clark_1965]: https://doi.org/10.2514/3.43639
[research_miller_wykes_1983]: https://doi.org/10.2514/3.44931
[research_minerdd_glossbb_1975]: https://ntrs.nasa.gov/citations/19750013175
[research_miranda_bidinotto_2025]: https://doi.org/10.1590/jatm.v17.1368
[research_miranda_li_2025]: https://doi.org/10.1016/j.compstruct.2025.119291
[research_missoum_2012]: https://doi.org/10.21236/ada582315
[research_mitchell_1961]: https://doi.org/10.4050/jahs.6.3
[research_mitchell_myers_1980]: https://doi.org/10.21236/ada101648
[research_miurahirokazu_neilldouglasj_1992]: https://ntrs.nasa.gov/citations/19930036331
[research_miyasato_1992]: https://doi.org/10.9746/sicetr1965.28.1141
[research_miyazawa_1993]: https://doi.org/10.2514/3.20995
[research_moarref_rodrigues_2015]: https://doi.org/10.1002/rnc.3364
[research_mochizuki_yamada_2018]: https://doi.org/10.1051/matecconf/201814503010
[research_modi_slater_1983]: https://doi.org/10.1016/0167-6105(83)90110-1
[research_modi_slater_1994]: https://doi.org/10.1115/1.2930448
[research_moestimothyr_noffzgregoryk_2000]: https://ntrs.nasa.gov/citations/20010002099
[research_moestimothyr_smithmarks_2003]: https://ntrs.nasa.gov/citations/20030107571
[research_mohanty_chhotaray_1979]: https://doi.org/10.1080/03772063.1979.11451910
[research_monaghanrc_1981]: https://ntrs.nasa.gov/citations/19810009523
[research_montgomery_1972]: https://doi.org/10.2514/3.59015
[research_montgomery_caglayan_1976]: https://doi.org/10.2514/3.58633
[research_montgomery_price_1976]: https://doi.org/10.2514/3.58634
[research_montgomeryrc_pricedb_1974]: https://ntrs.nasa.gov/citations/19740055499
[research_moon_1996]: https://doi.org/10.21236/ada361169
[research_moore_1972]: https://doi.org/10.21236/ad0754098
[research_moorenr_ebbelerdh_1992]: https://ntrs.nasa.gov/citations/19940009605
[research_moreira_moleiro_2024]: https://doi.org/10.1016/j.compstruct.2024.118287
[research_morino_obayashi_2015]: https://doi.org/10.2514/1.c032775
[research_morita_matsukawa_1995]: https://doi.org/10.1080/00423119508969100
[research_morozov_janschek_2016]: https://doi.org/10.1016/j.ifacol.2016.09.043
[research_morris_1977]: https://doi.org/10.21236/ada049528
[research_morrison_white_1976]: https://doi.org/10.21236/ada029371
[research_motta_malzacher_2019]: https://doi.org/10.1115/1.4043545
[research_moulmartint_brownlawrencew_1959]: https://ntrs.nasa.gov/citations/19980228212
[research_moulmartint_winemanandrewr_1952]: https://ntrs.nasa.gov/citations/19930086980
[research_moureydj_1979]: https://ntrs.nasa.gov/citations/19800001956
[research_mu_huang_2022]: https://doi.org/10.1016/j.jsv.2022.116916
[research_mu_huang_2026]: https://doi.org/10.1016/j.jsv.2025.119440
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
[research_naca_conference_1949]: https://ntrs.nasa.gov/citations/19650074048
[research_naca_conference_1957]: https://ntrs.nasa.gov/citations/19710070068
[research_nagabhushan_1991]: https://doi.org/10.2514/3.46064
[research_naganarayana_atluri_1995]: https://doi.org/10.1007/s004660050032
[research_nagaraja_lakin_1982]: https://doi.org/10.2514/3.61555
[research_nagib_wigeland_1977]: https://doi.org/10.21236/ada049193
[research_nagy_1979]: https://doi.org/10.21236/ada071322
[research_nakamura_1982]: https://doi.org/10.1143/jpsj.51.4084
[research_nakamura_takesue_1990]: https://doi.org/10.1541/ieejias.110.693
[research_nam_chen_2000]: https://doi.org/10.21236/ada379722
[research_namanikoureh_shahverdi_2026]: https://doi.org/10.1007/s00158-026-04311-z
[research_napolitanomarcellor_1996]: https://ntrs.nasa.gov/citations/19960014815
[research_napolitanomarcellor_spagnuolojoellem_1993]: https://ntrs.nasa.gov/citations/19940020331
[research_narendra_tripathi_1973]: https://doi.org/10.2514/3.44364
[research_narimani_haddadpour_2025]: https://doi.org/10.1016/j.ast.2025.109992
[research_nath_ana_2017]: https://doi.org/10.14445/22315381/ijett-v54p212
[research_nazarenko_nevezhina_1972]: https://doi.org/10.1007/bf01186488
[research_nazeer_wang_2021]: https://doi.org/10.3390/act10060107
[research_neal_smith_1970]: https://doi.org/10.21236/ad0880426
[research_negaard_1980]: https://doi.org/10.21236/ada361289
[research_negahban_bashir_2024]: https://doi.org/10.3390/drones8080392
[research_nelson_mouch_1978]: https://doi.org/10.21236/ada056045
[research_neu_huang_1973]: https://doi.org/10.21236/ada325972
[research_neville_marois_1992]: https://doi.org/10.1364/ao.31.003463
[research_newton_kroo_2025]: https://doi.org/10.2514/1.g008400
[research_nguyen_lowenberg_2021]: https://doi.org/10.2514/1.g005840
[research_nguyen_olaru_2016]: https://doi.org/10.1016/j.automatica.2015.10.048
[research_nguyen_reynolds_2018]: https://doi.org/10.2514/1.c034448
[research_nguyenlt_gilbertwp_1979]: https://ntrs.nasa.gov/citations/19800006901
[research_nguyenluatt_gilertwilliamp_1990]: https://ntrs.nasa.gov/citations/19900048974
[research_nguyennhan_jamesurnessr_2012]: https://ntrs.nasa.gov/citations/20170005442
[research_nguyennhan_kaulupender_2015]: https://ntrs.nasa.gov/citations/20150023531
[research_ni_li_2023]: https://doi.org/10.1016/j.compstruct.2022.116504
[research_nibbelinkbruced_petersdavida_1993]: https://ntrs.nasa.gov/citations/19930049880
[research_niblett_1986]: https://doi.org/10.2514/3.45369
[research_niblett_1988]: https://doi.org/10.2514/3.45590
[research_nicholaswu_navillegl_1984]: https://ntrs.nasa.gov/citations/19840062226
[research_nicolaides_1971]: https://doi.org/10.21236/ad0731564
[research_niehaus_1962]: https://doi.org/10.4050/jahs.7.24
[research_nihtila_1989]: https://doi.org/10.1016/0167-6911(89)90046-7
[research_nikrad_asadi_2015]: https://doi.org/10.1016/j.compstruct.2015.07.019
[research_nissen_2009]: https://doi.org/10.21236/ada513588
[research_nitschke_vincenti_2019]: https://doi.org/10.1016/j.compstruct.2019.03.072
[research_nitzsche_breitbach_1994]: https://doi.org/10.2514/3.46628
[research_niu_li_2026]: https://doi.org/10.1007/s12555-026-00058-x
[research_niven_1977]: https://doi.org/10.21236/ada050618
[research_nixonmarkw_piatakdavidj_1999]: https://ntrs.nasa.gov/citations/19990050923
[research_noll_eastep_1984]: https://doi.org/10.2514/3.48246
[research_nonnenmacher_jones_2016]: https://doi.org/10.1007/s13272-016-0211-6
[research_northropaircraftinchawthorneca_1952]: https://doi.org/10.21236/ad0024361
[research_norton_1990]: https://doi.org/10.21236/ada257262
[research_norwood_1992]: https://doi.org/10.21236/ada249881
[research_ntantis_xezonakis_2024]: https://doi.org/10.1016/j.rineng.2024.103189
[research_numerical_and_2019]: https://doi.org/10.17559/tv-20180724143418
[research_numerical_study_2023]: https://doi.org/10.47176/jafm.16.09.1755
[research_oberkampf_nicolaides_1971]: https://doi.org/10.2514/3.50043
[research_ochi_kanai_1995]: https://doi.org/10.2514/3.21393
[research_odonnelljamesrjr_andrewsstephenf_1999]: https://ntrs.nasa.gov/citations/19990064189
[research_odonnelljamesrjr_davisgaryt_2002]: https://ntrs.nasa.gov/citations/20020060756
[research_oelker_hummel_1989]: https://doi.org/10.2514/3.45817
[research_ogunvoul_balanchuk_2017]: https://doi.org/10.26467/2079-0619-2017-20-4-41-51
[research_ohkawa_1985]: https://doi.org/10.1080/00207178508933423
[research_ohkawa_1986]: https://doi.org/10.1080/00207178608933588
[research_ohkuma_1993]: https://doi.org/10.1016/0167-6105(93)90365-u
[research_ohta_nikiforuk_1979]: https://doi.org/10.2514/3.55828
[research_ohta_nikiforuk_1982]: https://doi.org/10.2514/3.56143
[research_okumoto_elsanker_1973]: https://doi.org/10.21236/ad0767182
[research_oland_andersen_2016]: https://doi.org/10.1016/j.automatica.2016.02.034
[research_olhan_behera_2023]: https://doi.org/10.1016/j.jmapro.2023.08.003
[research_olsen_1966]: https://doi.org/10.21236/ad0647369
[research_olsonglenno_1982]: https://ntrs.nasa.gov/citations/20080004217
[research_operationaltechnologiescorpsanantoniotx_1996]: https://doi.org/10.21236/ada316165
[research_orkwis_1995]: https://doi.org/10.21236/ada304583
[research_osder_mossman_1976]: https://doi.org/10.2514/3.58699
[research_osipov_2016]: https://doi.org/10.1615/tsagiscij.2017019838
[research_osipov_2017]: https://doi.org/10.1615/tsagiscij.2018026350
[research_ostheimer_giguere_1963]: https://doi.org/10.21236/ad0402379
[research_othman_silva_2019]: https://doi.org/10.1016/j.compstruct.2018.09.086
[research_otsuka_makihara_2017]: https://doi.org/10.1299/jsmedmc.2017.715
[research_ouyang_lin_2017]: https://doi.org/10.1002/rnc.3883
[research_ouyang_zeng_2021]: https://doi.org/10.1155/2021/5535192
[research_ouztspeterj_solowaydonaldi_2009]: https://ntrs.nasa.gov/citations/20100021410
[research_over_136_1981]: https://doi.org/10.1016/0010-4361(81)90026-4
[research_oyibo_1984]: https://doi.org/10.2514/3.48423
[research_ozdil_carlsson_1992]: https://doi.org/10.1177/002199839202600306
[research_ozkan_2020]: https://doi.org/10.21605/cukurovaummfd.792424
[research_packard_seiler_2009]: https://doi.org/10.21236/ada531629
[research_pagano_1974]: https://doi.org/10.1177/002199837400800106
[research_palframan_fry_2019]: https://doi.org/10.1109/tcst.2017.2766598
[research_palmtod_mahlermary_2000]: https://ntrs.nasa.gov/citations/20000052504
[research_pan_cheng_1995]: https://doi.org/10.2514/3.46853
[research_pan_huang_2019]: https://doi.org/10.5028/jatm.v11.1074
[research_papadales_basils_1979]: https://doi.org/10.21236/ada073100
[research_papirno_1977]: https://doi.org/10.1177/002199837701100106
[research_park_jung_2017]: https://doi.org/10.5626/jok.2017.44.6.559
[research_parker_simonson_1982]: https://doi.org/10.21236/adb069628
[research_parker_simonson_1982_b]: https://doi.org/10.21236/adb069402
[research_parker_simonson_1982_c]: https://doi.org/10.21236/adb069405
[research_parthivnshah_ericlblades_2023]: https://ntrs.nasa.gov/citations/20220001748
[research_passive_wing_store_1982]: https://doi.org/10.1121/1.387660
[research_patartics_liptak_2022]: https://doi.org/10.1109/tcst.2021.3066096
[research_pate_1964]: https://doi.org/10.21236/ad0450195
[research_pate_deitering_1963]: https://doi.org/10.21236/ad0297204
[research_patel_kumar_2022]: https://doi.org/10.1016/j.ifacol.2022.11.241
[research_patrickcmurphy_1999]: https://ntrs.nasa.gov/citations/19990032463
[research_patterson_grenestedt_2018]: https://doi.org/10.1016/j.compstruct.2018.08.052
[research_paulk_anderson_1976]: https://doi.org/10.21236/adb014346
[research_paulsonjwjr_thomasjl_1978]: https://ntrs.nasa.gov/citations/19780018153
[research_paulsonjwjr_thomasjl_1979]: https://ntrs.nasa.gov/citations/19790035660
[research_paulsonjwjr_thomasjl_1979_b]: https://ntrs.nasa.gov/citations/19800004739
[research_payton_2017]: https://doi.org/10.21660/2017.33.2565
[research_pearsonhenrya_aikenwilliamsjr_1944]: https://ntrs.nasa.gov/citations/19930091876
[research_peledu_powelljd_1978]: https://ntrs.nasa.gov/citations/19780066300
[research_pellerin_1988]: https://doi.org/10.21236/ada197718
[research_pelykh_andryushchenko_2024]: https://doi.org/10.15587/2706-5448.2024.298600
[research_penafrancisco_2020]: https://ntrs.nasa.gov/citations/20200001121
[research_penafrancisco_martinsbenjamin_2018]: https://ntrs.nasa.gov/citations/20190033242
[research_pendem_2023]: https://doi.org/10.22214/ijraset.2023.52971
[research_pendleton_moster_1995]: https://doi.org/10.2514/3.46860
[research_peng_cao_2026]: https://doi.org/10.1109/tsmc.2026.3657656
[research_peng_zhang_1994]: https://doi.org/10.1080/00423119408969061
[research_perkins_jr_1977]: https://doi.org/10.21236/ada062274
[research_perry_rievley_1961]: https://doi.org/10.21236/ad0259391
[research_perrybiii_1976]: https://ntrs.nasa.gov/citations/19760011057
[research_perrybiii_1982]: https://ntrs.nasa.gov/citations/19820020423
[research_persoon_horsten_1984]: https://doi.org/10.2514/3.45061
[research_persoon_roos_1980]: https://doi.org/10.21236/ada097094
[research_petersdavida_1988]: https://ntrs.nasa.gov/citations/19880017772
[research_petersenkl_1981]: https://ntrs.nasa.gov/citations/19820030322
[research_petre_ashley_1976]: https://doi.org/10.2514/3.58707
[research_petterssen_1953]: https://doi.org/10.1111/j.2153-3490.1953.tb01052.x
[research_pfeifle_fichter_2023]: https://doi.org/10.2514/1.g006929
[research_pham_2022]: https://doi.org/10.56651/lqdtu.jst.v17.n02.312
[research_phan_2020]: https://doi.org/10.1016/j.istruc.2020.08.035
[research_philippidis_1994]: https://doi.org/10.1515/secm.1994.3.1.39
[research_phuekpan_khammee_2025]: https://doi.org/10.3390/aerospace12020101
[research_piao_zhang_2019]: https://doi.org/10.1177/1077546319849775
[research_picon_alarcon_1978]: https://doi.org/10.1016/0141-1195(78)90019-0
[research_pidaparti_1993]: https://doi.org/10.1016/0263-8223(93)90154-i
[research_pidaparti_yang_1993]: https://doi.org/10.2514/3.11735
[research_pizzoli_saltari_2022]: https://doi.org/10.3390/app12178762
[research_place_altmann_1974]: https://doi.org/10.21236/ad0785104
[research_plaetschke_mulder_1982]: https://doi.org/10.1016/s1474-6670(17)63152-5
[research_platus_1980]: https://doi.org/10.21236/ada093741
[research_plotkin_1978]: https://doi.org/10.1115/1.3424324
[research_plyako_1977]: https://doi.org/10.1007/bf00967161
[research_poll_1986]: https://doi.org/10.1017/s0001924000015670
[research_polyester_fibreglass_reinforced_1978]: https://doi.org/10.1016/0010-4361(78)90633-x
[research_poole_allen_2022]: https://doi.org/10.1007/s00158-022-03174-4
[research_poole_allen_2026]: https://doi.org/10.2514/1.c038630
[research_portapas_cooke_2020]: https://doi.org/10.3846/aviation.2020.12175
[research_posingies_1979]: https://doi.org/10.21236/ada070387
[research_pourtakdoust_khodabakhsh_2026]: https://doi.org/10.1016/j.ast.2025.111214
[research_poussotvassal_demourant_2017]: https://doi.org/10.1109/tcst.2016.2630505
[research_powellrichardw_1993]: https://ntrs.nasa.gov/citations/19930069740
[research_powers_1982]: https://doi.org/10.2514/3.56150
[research_powersbg_1980]: https://ntrs.nasa.gov/citations/19800061700
[research_prasad_nematnasser_1967]: https://doi.org/10.2514/3.3959
[research_prasad_pesek_2018]: https://doi.org/10.1051/matecconf/201821115001
[research_prasannakumar_sudhi_2024]: https://doi.org/10.2514/1.c037398
[research_pratama_2021]: https://doi.org/10.28989/vortex.v2i2.1010
[research_pritt_1980]: https://doi.org/10.21236/ada106425
[research_property_changes_1981]: https://doi.org/10.1016/0010-4361(81)90051-3
[research_prototype_digital_1986]: https://doi.org/10.1108/eb036284
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
[research_qi_zhao_2020]: https://doi.org/10.2514/1.g004761
[research_qian_lu_2025]: https://doi.org/10.1093/cdm/wqaf016
[research_qian_xinhui_2025]: https://doi.org/10.65904/3083-3450.2025.01.05
[research_qin_liu_2017]: https://doi.org/10.1016/j.ast.2017.06.012
[research_qu_annaswamy_2016]: https://doi.org/10.2514/1.g001282
[research_qu_li_2022]: https://doi.org/10.1088/1742-6596/2258/1/012074
[research_radetskaya_2022]: https://doi.org/10.18698/2541-8009-2022-10-833
[research_radfordrc_smithr_1980]: https://ntrs.nasa.gov/citations/19810005458
[research_raghav_komerath_2015]: https://doi.org/10.1063/1.4906803
[research_raisrohanim_haftkart_1992]: https://ntrs.nasa.gov/citations/19930036310
[research_raisrohanimasoud_1994]: https://ntrs.nasa.gov/citations/19950016897
[research_raisrohanimasound_1999]: https://ntrs.nasa.gov/citations/19990064496
[research_rajpal_kassapoglou_2019]: https://doi.org/10.1016/j.compstruct.2019.111248
[research_rajpal_mitrotta_2021]: https://doi.org/10.1016/j.compstruct.2021.114373
[research_ramamoorthy_1992]: https://doi.org/10.21236/ada252232
[research_ranaudorichardj_ratvaskythomasp_2000]: https://ntrs.nasa.gov/citations/20000120385
[research_raneydavidl_1987]: https://ntrs.nasa.gov/citations/19870062350
[research_rao_1975]: https://doi.org/10.1016/s0022-460x(75)80007-1
[research_rao_hofer_1973]: https://doi.org/10.21236/ada305383
[research_rao_padmanabhan_2019]: https://doi.org/10.1504/ijndc.2019.103285
[research_rao_umamaheswararao_1992]: https://doi.org/10.1016/0263-8223(92)90002-t
[research_raouf_1994]: https://doi.org/10.1016/0263-8223(94)90023-x
[research_raper_1991]: https://doi.org/10.21236/ada240387
[research_rapoffandrewj_dillharoldd_1990]: https://ntrs.nasa.gov/citations/19920023336
[research_rate_sensitivity_1988]: https://doi.org/10.1016/0010-4361(88)90610-6
[research_rath_fichter_2020]: https://doi.org/10.4050/jahs.66.022003
[research_rayej_mckinneylw_1972]: https://ntrs.nasa.gov/citations/19730006292
[research_rayej_mckinneylw_1973]: https://ntrs.nasa.gov/citations/19730017272
[research_rea_pecora_2017]: https://doi.org/10.18178/ijmerr.6.6.
[research_rea_pecora_2018]: https://doi.org/10.18178/ijmerr.6.6.440-450
[research_reader_1976]: https://doi.org/10.21236/ada026548
[research_recaluque_aguilartorres_2023]: https://doi.org/10.6036/10630
[research_rediessha_szalaikj_1975]: https://ntrs.nasa.gov/citations/19750020942
[research_reding_ericsson_1977]: https://doi.org/10.2514/3.58883
[research_reeder_1958]: https://doi.org/10.4050/jahs.3.4
[research_reid_rajagopal_1994]: https://doi.org/10.2514/3.46607
[research_reinbold_breitsamter_2026]: https://doi.org/10.2514/1.c038409
[research_ren_zhang_2022]: https://doi.org/10.1155/2022/7904892
[research_repa_alexandridis_1977]: https://doi.org/10.1080/00423117708968535
[research_research_and_2022]: https://doi.org/10.47939/et.v3i2.104
[research_reyes_climent_2019]: https://doi.org/10.1007/s13272-019-00361-w
[research_rhodesmd_selbergbp_1982]: https://ntrs.nasa.gov/citations/19820057396
[research_richards_1979]: https://doi.org/10.21236/ada088129
[research_richmj_ridgleygf_1974]: https://ntrs.nasa.gov/citations/19740053860
[research_richwinedavidm_fisherdavidf_1991]: https://ntrs.nasa.gov/citations/19910069136
[research_rickardww_1978]: https://ntrs.nasa.gov/citations/19780062649
[research_rickettsrh_doggettrvjr_1980]: https://ntrs.nasa.gov/citations/19800020786
[research_rickettsrh_sandfordmc_1983]: https://ntrs.nasa.gov/citations/19830048631
[research_rickettsrh_watsonjj_1983]: https://ntrs.nasa.gov/citations/19860014096
[research_ried_1986]: https://doi.org/10.17764/jiet.1.29.5.k3328013777g1067
[research_riefe_1946]: https://doi.org/10.21236/adb813732
[research_rigatos_2021]: https://doi.org/10.1142/s2737480721500126
[research_rimer_chipman_1984]: https://doi.org/10.2514/3.45034
[research_rimer_chipman_1986]: https://doi.org/10.2514/3.20069
[research_rimerm_chipmanr_1984]: https://ntrs.nasa.gov/citations/19840060637
[research_ringertz_1994]: https://doi.org/10.1007/bf01742928
[research_risingjj_daviswj_1984]: https://ntrs.nasa.gov/citations/19850030442
[research_rittenhouse_1959]: https://doi.org/10.21236/ad0207771
[research_rizzetta_1977]: https://doi.org/10.21236/ada057505
[research_rizzetta_1979]: https://doi.org/10.2514/3.61058
[research_rizzetta_visbal_2016]: https://doi.org/10.2514/1.c033596
[research_roberts_1986]: https://doi.org/10.17764/jiet.1.29.5.bg524k2wr7355x02
[research_roberts_smith_1966]: https://doi.org/10.21236/ad0635953
[research_robertspa_swaimrl_1977]: https://ntrs.nasa.gov/citations/19770016183
[research_robinson_2004]: https://doi.org/10.21236/ada425641
[research_robotics_2024]: https://doi.org/10.1155/2024/9785472
[research_rockwell_1994]: https://doi.org/10.21236/ada278988
[research_rodden_1981]: https://doi.org/10.2514/3.44744
[research_rodden_1984]: https://doi.org/10.2514/3.56737
[research_rodden_1989]: https://doi.org/10.2514/3.45825
[research_rodden_1989_b]: https://doi.org/10.2514/3.45842
[research_rodden_bellinger_1982]: https://doi.org/10.2514/3.61559
[research_rodemich_andrew_1965]: https://doi.org/10.21236/ad0618097
[research_rogalski_2018]: https://doi.org/10.1108/aeat-02-2018-0088
[research_rogersten_xu_2013]: https://doi.org/10.21236/ada587237
[research_rohella_chatterjee_1979]: https://doi.org/10.1080/03772063.1979.11451847
[research_rokhsaz_selberg_1990]: https://doi.org/10.2514/3.25271
[research_rom_lamar_1992]: https://doi.org/10.2514/3.48952
[research_romano_ciminello_2019]: https://doi.org/10.1177/0021998319843333
[research_ronflenadaud_2009]: https://doi.org/10.21236/ada512960
[research_rongrong_zhengyin_2018]: https://doi.org/10.1177/0954410018807810
[research_rooneyrh_chungjc_1982]: https://ntrs.nasa.gov/citations/19820055409
[research_roos_mushlin_1989]: https://doi.org/10.1109/23.34590
[research_rosa_pouca_2023]: https://doi.org/10.1016/j.jmapro.2023.02.012
[research_roscoe_eisele_1975]: https://doi.org/10.21236/ada022459
[research_rose_seginer_1978]: https://doi.org/10.2514/3.58399
[research_rosenbruces_1988]: https://ntrs.nasa.gov/citations/19880034776
[research_roskamj_lanc_1972]: https://ntrs.nasa.gov/citations/19730013170
[research_roskamj_lanc_1973]: https://ntrs.nasa.gov/citations/19730013169
[research_rowley_2008]: https://doi.org/10.21236/ada476708
[research_roylance_1980]: https://doi.org/10.1177/002199838001400203
[research_ruhlin_rauch_1983]: https://doi.org/10.2514/3.44933
[research_rumble_1987]: https://doi.org/10.21236/ada194418
[research_runkel_fasel_2018]: https://doi.org/10.1016/j.compstruct.2018.07.095
[research_runyan_cunningham_1952]: https://doi.org/10.2514/8.2220
[research_ruo_malone_1985]: https://doi.org/10.2514/3.45076
[research_ruscheweyh_1983]: https://doi.org/10.1016/0167-6105(83)90017-x
[research_rutkowski_1979]: https://doi.org/10.2514/3.58539
[research_ryder_walker_1976]: https://doi.org/10.21236/ada043365
[research_sabatini_coppotelli_2026]: https://doi.org/10.2514/1.g009632
[research_sachs_1975]: https://doi.org/10.2514/3.44471
[research_sachs_1977]: https://doi.org/10.2514/3.44623
[research_sachs_1979]: https://doi.org/10.1080/00423117908968599
[research_sachs_muvdi_1956]: https://doi.org/10.21236/ad0091083
[research_saddington_thangamani_2016]: https://doi.org/10.2514/1.c033365
[research_saderla_dhayalan_2016]: https://doi.org/10.14429/dsj.67.9995
[research_sadoffmelvin_mcfaddennormanm_1961]: https://ntrs.nasa.gov/citations/19980227090
[research_saetti_horn_2020]: https://doi.org/10.2514/1.g004965
[research_saheby_jialu_2026]: https://doi.org/10.1016/j.ast.2025.111026
[research_sahu_heavey_2000]: https://doi.org/10.21236/ada384925
[research_sahyoun_boose_2026]: https://doi.org/10.1007/s13272-026-00954-2
[research_salichon_guy_1994]: https://doi.org/10.1051/animres:19940210
[research_sallyaviken_craigahunter_2022]: https://ntrs.nasa.gov/citations/20205007879
[research_saltzmanedwinj_hicksjohnw_1994]: https://ntrs.nasa.gov/citations/19950012150
[research_sammondsroberti_mcneillwaltere_1982]: https://ntrs.nasa.gov/citations/19980201422
[research_samputh_moey_2024]: https://doi.org/10.3846/aviation.2024.21495
[research_santich_1985]: https://doi.org/10.1558/ppc.30968
[research_saporito_daronch_2023]: https://doi.org/10.1016/j.ast.2023.108349
[research_saraeian_shirazi_2022]: https://doi.org/10.1016/j.isatra.2022.03.007
[research_saric_1997]: https://doi.org/10.21236/ada388392
[research_sato_1973]: https://doi.org/10.2514/3.6669
[research_sawyerjw_1976]: https://ntrs.nasa.gov/citations/19760047048
[research_schewe_mai_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.04.021
[research_schildkamp_chang_2023]: https://doi.org/10.3390/act12070280
[research_schmidt_2016]: https://doi.org/10.2514/1.g001484
[research_schmidt_lisoski_2025]: https://doi.org/10.2514/1.c038107
[research_schmidtdavidk_schiermanjohnd_1990]: https://ntrs.nasa.gov/citations/19900060642
[research_schneider_1976]: https://doi.org/10.21236/ada025795
[research_schpey_1980]: https://doi.org/10.21236/ada083721
[research_schreadley_1977]: https://doi.org/10.21236/ada043979
[research_schroederjefferya_chungwilliamwy_2001]: https://ntrs.nasa.gov/citations/20010037958
[research_schueltke_stumpf_2017]: https://doi.org/10.1108/aeat-11-2016-0210
[research_schuster_1995]: https://doi.org/10.2514/3.46686
[research_schusterdavidm_edwardsjohnw_2004]: https://ntrs.nasa.gov/citations/20040086524
[research_schwanz_1972]: https://doi.org/10.21236/ada006391
[research_schwerdt_maroldt_2023]: https://doi.org/10.33737/jgpps/161707
[research_sciuva_1992]: https://doi.org/10.1016/0263-8223(92)90003-u
[research_scordamaglia_mattei_2025]: https://doi.org/10.1109/ojcsys.2025.3619810
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
[research_sengupta_ferris_1973]: https://doi.org/10.1109/tap.1973.1140539
[research_seraj_ganesan_2018]: https://doi.org/10.1016/j.compstruct.2018.05.133
[research_seyoung_1990]: https://doi.org/10.1016/0020-7683(90)90098-g
[research_shafermaryf_steinmetzpaul_2001]: https://ntrs.nasa.gov/citations/20010038270
[research_shafermaryf_steinmetzpaul_2001_b]: https://ntrs.nasa.gov/citations/20010037948
[research_shafermf_1980]: https://ntrs.nasa.gov/citations/19800061745
[research_shafermf_smithre_1983]: https://ntrs.nasa.gov/citations/19830060718
[research_shafermf_smithre_1984]: https://ntrs.nasa.gov/citations/19840008145
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
[research_sharp_wilson_1990]: https://doi.org/10.1080/00423119008968952
[research_sharqi_cesnik_2023]: https://doi.org/10.2514/1.c036894
[research_shawki_mashhour_1974]: https://doi.org/10.1007/bf02323065
[research_shearwood_nabawy_2020]: https://doi.org/10.3390/aerospace7100150
[research_sheldon_1967]: https://doi.org/10.21236/ad0856658
[research_shen_chang_2022]: https://doi.org/10.1088/1742-6596/2338/1/012092
[research_shen_chen_2023]: https://doi.org/10.1108/aeat-09-2022-0250
[research_shen_huang_2021]: https://doi.org/10.1016/j.cja.2020.07.022
[research_shepheard_1965]: https://doi.org/10.21236/ad0630924
[research_sherrer_hertz_1981]: https://doi.org/10.2514/3.57589
[research_shi_bezine_1988]: https://doi.org/10.1177/002199838802200801
[research_shi_gao_2025]: https://doi.org/10.3390/aerospace12060532
[research_shi_gao_2026]: https://doi.org/10.1016/j.ast.2025.110884
[research_shi_lyu_2019]: https://doi.org/10.1109/access.2019.2938013
[research_shi_tan_2018]: https://doi.org/10.1360/n092017-00215
[research_shiau_chang_1991]: https://doi.org/10.1016/0045-7949(91)90025-h
[research_shibahata_shimada_1993]: https://doi.org/10.1080/00423119308969044
[research_shields_cook_1971]: https://doi.org/10.1080/00207177108932075
[research_shirk_hertz_1986]: https://doi.org/10.2514/3.45260
[research_shladover_1995]: https://doi.org/10.1080/00423119508969108
[research_shmilovich_princen_2026]: https://doi.org/10.2514/1.c038755
[research_shmilovich_yadlin_2026]: https://doi.org/10.2514/1.c037586
[research_shneen_2026]: https://doi.org/10.59247/jfsc.v3i3.345
[research_shoales_fawaz_2004]: https://doi.org/10.21236/ada430478
[research_short_1995]: https://doi.org/10.1016/0010-4361(95)90916-n
[research_shrivastava_mohite_2015]: https://doi.org/10.1515/cls-2015-0010
[research_shrivastava_tilala_2020]: https://doi.org/10.1007/s00158-020-02569-5
[research_shrivastavapc_1987]: https://ntrs.nasa.gov/citations/19870013189
[research_shyprykevichp_1979]: https://ntrs.nasa.gov/citations/19800036960
[research_siem_murray_1997]: https://doi.org/10.21236/ada459823
[research_silton_fresconi_2014]: https://doi.org/10.21236/ada611082
[research_silton_fresconi_2015]: https://doi.org/10.2514/1.a33219
[research_silvaleon_cioncolini_2020]: https://doi.org/10.3390/fluids5020090
[research_silvawaltera_bennettrobertm_1990]: https://ntrs.nasa.gov/citations/19900010731
[research_simbuerger_raveh_2022]: https://doi.org/10.2514/1.c036626
[research_simmons_2023]: https://doi.org/10.1111/jzo.13117
[research_simpson_1988]: https://doi.org/10.1017/s0001924000022028
[research_simsrobert_mccrossonpaul_1989]: https://ntrs.nasa.gov/citations/19900009909
[research_sineglazov_2015]: https://doi.org/10.18372/1990-5548.46.9966
[research_singh_brown_2016]: https://doi.org/10.2514/1.c033658
[research_singh_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1050
[research_singh_raisinghani_1993]: https://doi.org/10.2514/3.46373
[research_sitzjoelr_vernontoddh_1990]: https://ntrs.nasa.gov/citations/19930021575
[research_siwowski_kulpa_2018]: https://doi.org/10.1016/j.compstruct.2018.08.048
[research_sizlotr_bergra_1979]: https://ntrs.nasa.gov/citations/19820024501
[research_skf_divests_2016]: https://doi.org/10.1016/j.mprp.2016.04.079
[research_sliwasm_1980]: https://ntrs.nasa.gov/citations/19810005457
[research_smeltzer_durston_1983]: https://doi.org/10.2514/3.44950
[research_smetana_1973]: https://doi.org/10.21236/ad0763295
[research_smith_1991]: https://doi.org/10.1177/002029409102400303
[research_smith_1993]: https://doi.org/10.1017/s002211209322359x
[research_smith_2025]: https://doi.org/10.33548/scientia1180
[research_smith_geddes_1979]: https://doi.org/10.21236/ada077858
[research_smith_hammer_1971]: https://doi.org/10.21236/ad0730571
[research_smith_komerath_2001]: https://doi.org/10.21236/ada454384
[research_smith_meyer_1987]: https://doi.org/10.2514/3.20213
[research_smithjw_1979]: https://ntrs.nasa.gov/citations/19790023049
[research_smithjw_berrydt_1975]: https://ntrs.nasa.gov/citations/19750008488
[research_smithrogerse_schroederkurtc_1986]: https://ntrs.nasa.gov/citations/19870060567
[research_snyder_1950]: https://doi.org/10.21236/ad0109766
[research_snyder_schipper_1992]: https://doi.org/10.1109/62.257086
[research_sobieczky_1984]: https://doi.org/10.1146/annurev.fluid.16.1.337
[research_soleymani_arani_2019]: https://doi.org/10.1016/j.compstruct.2019.111532
[research_soneda_tsushima_2022]: https://doi.org/10.1007/s42405-022-00474-3
[research_song_huang_2022]: https://doi.org/10.1007/s11071-022-07742-7
[research_song_zhang_2016]: https://doi.org/10.1016/j.compstruct.2016.01.005
[research_soovere_1982]: https://doi.org/10.2514/3.44755
[research_soria_2006]: https://doi.org/10.21236/ada466362
[research_sottorfw_1949]: https://ntrs.nasa.gov/citations/20050242069
[research_space_radiation_1987]: https://doi.org/10.1016/0010-4361(87)90478-2
[research_speyer_2003]: https://doi.org/10.21236/ada416352
[research_spiker_1964]: https://doi.org/10.21236/ad0437251
[research_spillman_ridgely_1995]: https://doi.org/10.21236/ada320244
[research_srinathkumar_2015]: https://doi.org/10.4050/jahs.60.022010
[research_stagliano_mente_1979]: https://doi.org/10.21236/ada074261
[research_stainback_2001]: https://doi.org/10.21236/ada389727
[research_stalford_1979]: https://doi.org/10.21236/ada080025
[research_stanewsky_little_1971]: https://doi.org/10.2514/3.59192
[research_stanford_2016]: https://doi.org/10.2514/1.c033613
[research_stanford_2016_b]: https://doi.org/10.2514/1.g000413
[research_stanford_2017]: https://doi.org/10.2514/1.j056070
[research_stanford_2019]: https://doi.org/10.2514/1.g004373
[research_stanfordbretk_juttechristinev_2014]: https://ntrs.nasa.gov/citations/20150000538
[research_stanfordbretk_wiesemancarold_2015]: https://ntrs.nasa.gov/citations/20150006025
[research_stange_1959]: https://doi.org/10.21236/ada955359
[research_stanton_crain_1980]: https://doi.org/10.21236/ada088317
[research_stark_1989]: https://doi.org/10.2514/3.45867
[research_staufferwa_jamesam_1978]: https://ntrs.nasa.gov/citations/19780019119
[research_steger_bailey_1980]: https://doi.org/10.2514/3.50756
[research_steinmetzgg_parrishrv_1972]: https://ntrs.nasa.gov/citations/19720010363
[research_stephan_stumpf_2023]: https://doi.org/10.2514/1.c036717
[research_sternberg_traven_1994]: https://doi.org/10.21236/ada284128
[research_stewart_dominick_1975]: https://doi.org/10.21236/ada018420
[research_stinton_1985]: https://doi.org/10.1017/s0001924000096779
[research_stirling_1983]: https://doi.org/10.1177/003754978304000504
[research_stodieck_cooper_2015]: https://doi.org/10.2514/1.j053599
[research_stodieck_cooper_2017]: https://doi.org/10.2514/1.j055364
[research_stolarik_2007]: https://doi.org/10.21236/ada470308
[research_stollery_1992]: https://doi.org/10.1016/0021-9169(92)90172-h
[research_stollf_koenigdg_1983]: https://ntrs.nasa.gov/citations/19830067155
[research_stottier_1995]: https://doi.org/10.21236/ada293962
[research_strand_levinsky_1969]: https://doi.org/10.21236/ad0698355
[research_streb_1973]: https://doi.org/10.2514/3.60203
[research_streit_wedler_2015]: https://doi.org/10.1017/s0001924000011283
[research_strength_of_1978]: https://doi.org/10.14359/10974
[research_strike_wt_1982]: https://doi.org/10.21236/ada116279
[research_structural_aspects_2000]: https://ntrs.nasa.gov/citations/20000053157
[research_study_of_1978]: https://ntrs.nasa.gov/citations/19780012169
[research_sugino_harada_2019]: https://doi.org/10.1299/jsmemovic.2019.16.c112
[research_sugumaran_2024]: https://doi.org/10.17148/iarjset.2024.11553
[research_suhpeterm_conyershowardj_2014]: https://ntrs.nasa.gov/citations/20150000848
[research_suhpeterm_conyershowardjason_2015]: https://ntrs.nasa.gov/citations/20150020901
[research_suikatreiner_donaldsonkent_1987]: https://ntrs.nasa.gov/citations/19880027050
[research_sulaeman_abdullah_2017]: https://doi.org/10.1088/1757-899x/184/1/012010
[research_sullivan_2002]: https://doi.org/10.21236/ada428867
[research_sun_2015]: https://doi.org/10.1260/1756-8250.7.1-2.67
[research_sun_2024]: https://doi.org/10.1088/1742-6596/2882/1/012087
[research_sun_chen_2026]: https://doi.org/10.1007/s00158-026-04375-x
[research_sun_han_2022]: https://doi.org/10.3934/mbe.2022262
[research_sun_luo_2025]: https://doi.org/10.1063/5.0258283
[research_sun_shi_2020]: https://doi.org/10.1016/j.ast.2020.106126
[research_sun_wang_2020]: https://doi.org/10.3390/act9040122
[research_sun_xu_2024]: https://doi.org/10.1016/j.conengprac.2024.105967
[research_sun_yoon_1988]: https://doi.org/10.21236/ada199311
[research_sun_zhang_2026]: https://doi.org/10.1016/j.ast.2025.110841
[research_supercritical_wing_1971]: https://doi.org/10.2307/3955948
[research_suryawanshi_ghosh_2015]: https://doi.org/10.1007/s00158-015-1322-0
[research_svoboda_hengstermovric_2023]: https://doi.org/10.1016/j.ast.2023.108415
[research_swaim_1961]: https://doi.org/10.2514/8.9241
[research_swaim_yen_1979]: https://doi.org/10.2514/3.58579
[research_swain_adhikari_2019]: https://doi.org/10.1016/j.compstruct.2019.110916
[research_switzky_1965]: https://doi.org/10.2514/3.43690
[research_syed_moshtaghzadeh_2022]: https://doi.org/10.2514/1.j061574
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
[research_tahir_maqsood_2026]: https://doi.org/10.2514/1.c038034
[research_tai_wang_2023]: https://doi.org/10.1061/jaeeez.aseng-4565
[research_taimoor_aijun_2019]: https://doi.org/10.1108/aeat-05-2019-0106
[research_taira_2014]: https://doi.org/10.21236/ada604901
[research_talbot_geraldl_1992]: https://doi.org/10.21236/ada440831
[research_tameh_sawan_2018]: https://doi.org/10.1109/tie.2017.2786202
[research_tan_1988]: https://doi.org/10.1177/002199838802201105
[research_tan_wang_2021]: https://doi.org/10.1103/physrevfluids.6.l102701
[research_tan_zhang_2022]: https://doi.org/10.1007/s42401-021-00125-7
[research_tang_1989]: https://doi.org/10.21236/ada216966
[research_tang_chen_2018]: https://doi.org/10.1177/1077546317750504
[research_tang_chen_2020]: https://doi.org/10.1177/1077546320929153
[research_tang_liu_2018]: https://doi.org/10.1016/j.compstruct.2018.07.111
[research_tang_tang_2025]: https://doi.org/10.23919/jsee.2025.000136
[research_tang_wu_2016]: https://doi.org/10.1016/j.cja.2015.12.001
[research_tang_wu_2017]: https://doi.org/10.1016/j.cja.2016.12.024
[research_tangler_1979]: https://doi.org/10.21236/ada074141
[research_tantaroudas_karachalios_2026]: https://doi.org/10.24132/acm.2026.1114
[research_tao_sun_2016]: https://doi.org/10.1016/j.cja.2016.08.008
[research_targoff_1947]: https://doi.org/10.2514/8.1458
[research_targoff_1947_b]: https://doi.org/10.2514/8.1420
[research_tate_1992]: https://doi.org/10.21236/ada256514
[research_taufik_qasem_2025]: https://doi.org/10.1016/j.trpro.2025.03.120
[research_taylor_1959]: https://doi.org/10.1017/s0001924000092502
[research_taylor_2009]: https://doi.org/10.21236/ada540446
[research_teel_1999]: https://doi.org/10.21236/ada367012
[research_teel_1999_b]: https://doi.org/10.21236/ada367415
[research_telionis_1995]: https://doi.org/10.21236/ada299820
[research_telionis_2001]: https://doi.org/10.21236/ada398139
[research_teper_stapleford_1966]: https://doi.org/10.2514/3.43725
[research_terekhov_2022]: https://doi.org/10.34759/vst-2022-1-211-225
[research_tewar_myers_2015]: https://doi.org/10.1016/j.sysarc.2015.07.005
[research_tharp_zhang_1994]: https://doi.org/10.1007/bf02115737
[research_the_viscoelastic_1981]: https://doi.org/10.1016/0010-4361(81)90470-5
[research_the_voisin_1911]: https://doi.org/10.1038/scientificamerican04291911-424
[research_theerthamalai_mukesh_2025]: https://doi.org/10.1063/5.0256726
[research_theerthamalai_ramanan_2026]: https://doi.org/10.2514/1.a36413
[research_theis_pfifer_2020]: https://doi.org/10.2514/1.g004846
[research_theodore_malpica_2020]: https://doi.org/10.4050/jahs.65.042007
[research_thermal_damage_1989]: https://doi.org/10.1016/0010-4361(89)90359-5
[research_thermal_expansion_1981]: https://doi.org/10.1016/0010-4361(81)90491-2
[research_thomas_paulson_1978]: https://doi.org/10.2514/3.58357
[research_thompson_1992]: https://doi.org/10.21236/ada251673
[research_thompson_bannon_2002]: https://doi.org/10.21236/ada408751
[research_thompson_walls_2005]: https://doi.org/10.21236/ada436999
[research_thomson_caiafa_1982]: https://doi.org/10.2514/3.61569
[research_tian_wang_2026]: https://doi.org/10.1016/j.compstruct.2026.120104
[research_tian_yang_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000652
[research_tijdeman_vannunen_1979]: https://doi.org/10.21236/ada071420
[research_tijdeman_vannunen_1979_b]: https://doi.org/10.21236/ada077370
[research_ting_berg_2026]: https://doi.org/10.2514/1.g009557
[research_ting_mesbahi_2023]: https://doi.org/10.2514/1.g007450
[research_tingeric_daotung_2015]: https://ntrs.nasa.gov/citations/20190025220
[research_tingeric_lebofskysonia_2014]: https://ntrs.nasa.gov/citations/20150000694
[research_tingeric_nguyennhan_2014]: https://ntrs.nasa.gov/citations/20140008648
[research_tischlermarkb_fletcherjayw_1991]: https://ntrs.nasa.gov/citations/19910067397
[research_toader_1987]: https://doi.org/10.1016/0263-8231(87)90019-x
[research_toffol_2024]: https://doi.org/10.3390/app14219883
[research_toffol_ricci_2023]: https://doi.org/10.3390/aerospace10080693
[research_tohidi_khakisedigh_2016]: https://doi.org/10.1002/rnc.3518
[research_toledano_murakami_1987]: https://doi.org/10.1115/1.3172955
[research_tona_1962]: https://doi.org/10.21236/ad0299123
[research_torregrosa_gil_2022]: https://doi.org/10.1016/j.compstruct.2022.115845
[research_torsion_of_1968]: https://doi.org/10.14359/7456
[research_trabocco_1980]: https://doi.org/10.21236/ada326379
[research_tracking_control_1993]: https://doi.org/10.1016/0967-0661(93)92253-z
[research_tran_1994]: https://doi.org/10.1080/00423119408969056
[research_tran_nguyen_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001393
[research_tran_sakamoto_2017]: https://doi.org/10.1016/j.ast.2017.05.010
[research_traven_whitley_1995]: https://doi.org/10.21236/ada300965
[research_tribuno_klein_1976]: https://doi.org/10.21236/ada029021
[research_triplett_1972]: https://doi.org/10.2514/3.59009
[research_triplett_1980]: https://doi.org/10.2514/3.57932
[research_triplett_burkhart_1971]: https://doi.org/10.2514/3.59109
[research_triplett_kappus_1973]: https://doi.org/10.2514/3.60281
[research_trippenseegarya_luxdavidp_1987]: https://ntrs.nasa.gov/citations/19880008260
[research_trippenseegarya_luxdavidp_1988]: https://ntrs.nasa.gov/citations/19890023269
[research_tritschler_oconnor_2016]: https://doi.org/10.2514/1.g000401
[research_truong_rakotomamonjy_2016]: https://doi.org/10.1016/j.ifacol.2016.09.021
[research_tsoutsinos_1994]: https://doi.org/10.1016/0167-6911(94)90067-1
[research_tsunematsu_donadon_2019]: https://doi.org/10.1016/j.compstruct.2018.11.065
[research_tsushima_saitoh_2021]: https://doi.org/10.3390/aerospace8080200
[research_tsushima_yokozeki_2019]: https://doi.org/10.1016/j.ast.2019.03.025
[research_tsypkin_fu_1993]: https://doi.org/10.1080/00207179308934419
[research_tu_1992]: https://doi.org/10.2514/3.46253
[research_tu_1994]: https://doi.org/10.2514/3.46466
[research_tu_1994_b]: https://doi.org/10.2514/3.46489
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
[research_underwoodpamelaj_owenslewisr_2003]: https://ntrs.nasa.gov/citations/20030007882
[research_unruh_1988]: https://doi.org/10.2514/3.45655
[research_usellerjamesw_russeyroberte_1955]: https://ntrs.nasa.gov/citations/20090026462
[research_uzun_2024]: https://doi.org/10.1108/aeat-11-2023-0287
[research_uzun_2024_b]: https://doi.org/10.1016/j.aets.2024.12.001
[research_uzun_bilgic_2023]: https://doi.org/10.1017/aer.2023.73
[research_uzun_oktay_2023]: https://doi.org/10.1108/aeat-09-2022-0259
[research_vance_brown_1974]: https://doi.org/10.21236/ad0783390
[research_vandam_holmes_1981]: https://doi.org/10.2514/3.57531
[research_vandommelen_1995]: https://doi.org/10.21236/ada329654
[research_vandoren_1955]: https://doi.org/10.1109/irettrc.1955.6538793
[research_vangaasbeek_1980]: https://doi.org/10.21236/ada089008
[research_vangraas_braasch_1991]: https://doi.org/10.1002/j.2161-4296.1991.tb01864.x
[research_vangraas_diggle_1994]: https://doi.org/10.1002/j.2161-4296.1994.tb02322.x
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
[research_verhaegen_zbikowski_2017]: https://doi.org/10.1016/j.ast.2017.03.001
[research_verma_1981]: https://doi.org/10.1080/00423118108968682
[research_verri_desilvabussamra_2025]: https://doi.org/10.2514/1.c037829
[research_vile_alwi_2020]: https://doi.org/10.1049/cth2.12042
[research_vilela_donadon_2025]: https://doi.org/10.1016/j.tws.2025.113547
[research_vinje_miller_1973]: https://doi.org/10.21236/ad0769868
[research_viswanath_mukund_1995]: https://doi.org/10.2514/3.12838
[research_voracek_clarke_1994]: https://doi.org/10.2514/3.46505
[research_voracekdavidf_clarkerobert_1991]: https://ntrs.nasa.gov/citations/19910047389
[research_voting_software_1993]: https://doi.org/10.1016/0967-0661(93)92298-i
[research_vukobratovic_stojic_1985]: https://doi.org/10.1016/s1474-6670(17)60398-7
[research_vuong_kim_2021]: https://doi.org/10.3390/en15010159
[research_wadia_niedermeier_2019]: https://doi.org/10.1115/1.4043574
[research_waggonereg_batesbl_1989]: https://ntrs.nasa.gov/citations/19910014824
[research_waggonereg_jennettla_1986]: https://ntrs.nasa.gov/citations/19870045310
[research_waitman_marcos_2019]: https://doi.org/10.1016/j.ifacol.2019.11.184
[research_waitman_marcos_2020]: https://doi.org/10.2514/1.g004618
[research_wakimoto_chiba_2021]: https://doi.org/10.3390/aerospace8080217
[research_walchlilawrencea_1994]: https://ntrs.nasa.gov/citations/19950007845
[research_walker_kaufman_1977]: https://doi.org/10.21236/ada042114
[research_walkersa_1976]: https://ntrs.nasa.gov/citations/19760024070
[research_walkerth_minguetpj_1997]: https://ntrs.nasa.gov/citations/19970016009
[research_walshkevinr_1993]: https://ntrs.nasa.gov/citations/19930013934
[research_walshmichaelj_sellerswilliamliii_1988]: https://ntrs.nasa.gov/citations/19880053537
[research_wang_2019]: https://doi.org/10.1063/1.5087963
[research_wang_2026]: https://doi.org/10.1590/jatm.v18.1450
[research_wang_chen_2024]: https://doi.org/10.3390/aerospace11090711
[research_wang_chen_2025]: https://doi.org/10.1016/j.ast.2025.110547
[research_wang_chu_2017]: https://doi.org/10.1016/j.ifacol.2017.08.320
[research_wang_daronch_2018]: https://doi.org/10.3390/aerospace5030086
[research_wang_hu_2026]: https://doi.org/10.1016/j.ast.2025.111272
[research_wang_ji_2025]: https://doi.org/10.1016/j.ast.2025.110533
[research_wang_li_2025]: https://doi.org/10.1016/j.ast.2025.110134
[research_wang_li_2025_b]: https://doi.org/10.1049/icp.2024.2837
[research_wang_li_2026]: https://doi.org/10.3390/drones10080601
[research_wang_mkhoyan_2021]: https://doi.org/10.2514/1.g005870
[research_wang_rogers_1991]: https://doi.org/10.1177/002199839102500405
[research_wang_su_2017]: https://doi.org/10.1088/1742-6596/916/1/012006
[research_wang_su_2018]: https://doi.org/10.1088/1757-899x/452/4/042048
[research_wang_sun_2024]: https://doi.org/10.3390/aerospace11050366
[research_wang_sun_2024_b]: https://doi.org/10.1080/00423114.2024.2435973
[research_wang_sun_2025]: https://doi.org/10.2514/1.g009257
[research_wang_tian_2025]: https://doi.org/10.1016/j.cma.2025.118323
[research_wang_vankampen_2019]: https://doi.org/10.2514/1.g003980
[research_wang_wan_2021]: https://doi.org/10.1016/j.compstruct.2020.113201
[research_wang_wang_2015]: https://doi.org/10.4028/www.scientific.net/amm.740.293
[research_wang_weng_2026]: https://doi.org/10.1016/j.engappai.2026.115261
[research_wang_wu_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103286
[research_wang_wynn_2018]: https://doi.org/10.2514/1.c034684
[research_wang_xu_2016]: https://doi.org/10.1016/j.cja.2016.10.010
[research_wang_xu_2018]: https://doi.org/10.3390/s18103447
[research_wang_zhang_2020]: https://doi.org/10.1016/j.cja.2020.03.016
[research_wang_zhang_2022]: https://doi.org/10.3390/sym14061154
[research_wang_zhang_2025]: https://doi.org/10.1108/aeat-07-2024-0195
[research_wang_zheng_2022]: https://doi.org/10.1088/1742-6596/2187/1/012046
[research_wang_zhu_2016]: https://doi.org/10.1016/j.jfluidstructs.2016.01.009
[research_wangjohnt_1996]: https://ntrs.nasa.gov/citations/19960020473
[research_wangjohnt_jegleydawnc_1996]: https://ntrs.nasa.gov/citations/19960048076
[research_wansasueb_panagant_2023]: https://doi.org/10.1007/s00707-023-03756-3
[research_wardlaw_andrewb_1975]: https://doi.org/10.21236/ada020356
[research_washington_pettis_1968]: https://doi.org/10.21236/ad0695658
[research_watsonclifford_2010]: https://ntrs.nasa.gov/citations/20100024129
[research_watsoncliffordc_2011]: https://ntrs.nasa.gov/citations/20110015694
[research_wauters_2022]: https://doi.org/10.1177/17568293221092139
[research_webblannied_mccainwilliame_1988]: https://ntrs.nasa.gov/citations/19890006537
[research_weed_carlson_1983]: https://doi.org/10.21236/ada129573
[research_wegener_dhooghe_1993]: https://doi.org/10.1063/1.168480
[research_wei_2022]: https://doi.org/10.1155/2022/7716900
[research_wei_chen_2017]: https://doi.org/10.2514/1.c034079
[research_wei_cui_2025]: https://doi.org/10.3390/aerospace12090773
[research_wei_meng_2024]: https://doi.org/10.1002/rnc.7526
[research_wei_zhan_2019]: https://doi.org/10.1108/aeat-08-2017-0181
[research_weidemann_leondes_1979]: https://doi.org/10.21236/ada072259
[research_weinert_meyer_1984]: https://doi.org/10.21236/ada141875
[research_weisshaar_1977]: https://doi.org/10.2514/3.44579
[research_weisshaar_1978]: https://doi.org/10.21236/adb032318
[research_weisshaar_1979]: https://doi.org/10.21236/adb042815
[research_weisshaar_1980]: https://doi.org/10.2514/3.57922
[research_weisshaar_1981]: https://doi.org/10.2514/3.57542
[research_weisshaar_1985]: https://doi.org/10.2514/3.48607
[research_weisshaar_zeiler_1983]: https://doi.org/10.2514/3.48205
[research_weisshaarta_1983]: https://ntrs.nasa.gov/citations/19840055636
[research_weisshaarta_ehlerssm_1990]: https://ntrs.nasa.gov/citations/19900042331
[research_weisshaarta_zeilerta_1982]: https://ntrs.nasa.gov/citations/19820055567
[research_weisshaarterrencea_ehlersstevenm_1992]: https://ntrs.nasa.gov/citations/19930030821
[research_welle_2000]: https://doi.org/10.21236/ada381453
[research_wells_2002]: https://doi.org/10.21236/ada398917
[research_wen_song_2023]: https://doi.org/10.3390/aerospace10121001
[research_werdes_1953]: https://doi.org/10.2514/8.2666
[research_werter_debreuker_2016]: https://doi.org/10.1016/j.compstruct.2016.09.044
[research_whitbeck_hofmann_1978]: https://doi.org/10.21236/ada067177
[research_whitbeck_smith_1982]: https://doi.org/10.21236/ada134175
[research_white_2004]: https://doi.org/10.21236/ada421045
[research_white_geubelle_2005]: https://doi.org/10.21236/ada443864
[research_whiteedwardv_kapaniarakeshk_2015]: https://ntrs.nasa.gov/citations/20150017734
[research_whiteheadrs_foremancr_1992]: https://ntrs.nasa.gov/citations/19950022016
[research_whitejfiii_bendiksenoo_1986]: https://ntrs.nasa.gov/citations/19860063533
[research_whitlowwoodrowjr_bennettrobertm_1991]: https://ntrs.nasa.gov/citations/19930063025
[research_whitworth_1987]: https://doi.org/10.1177/002199838702100405
[research_whoric_1973]: https://doi.org/10.21236/ad0914456
[research_whoric_1977]: https://doi.org/10.21236/ada038494
[research_wickens_dixon_2002]: https://doi.org/10.21236/ada496813
[research_wiggenraadjfm_bauldnrjr_1993]: https://ntrs.nasa.gov/citations/19930044546
[research_wilcox_1963]: https://doi.org/10.21236/ad0400570
[research_wildermuth_rothammer_1974]: https://doi.org/10.21236/ada002873
[research_wilhelm_schafranek_1986]: https://doi.org/10.2514/3.45377
[research_williams_1980]: https://doi.org/10.2514/3.50797
[research_williamson_2022]: https://doi.org/10.1016/j.jedc.2021.104146
[research_wilson_2026]: https://doi.org/10.2139/ssrn.6417618
[research_wilson_riley_1993]: https://doi.org/10.21236/ada273685
[research_wilsondavidj_citurskevind_1994]: https://ntrs.nasa.gov/citations/19950007833
[research_wing_wing_2025]: https://doi.org/10.3354/meps14793
[research_wise_sedwick_1999]: https://doi.org/10.21236/ada386935
[research_withers_1981]: https://doi.org/10.1111/j.1474-919x.1981.tb00933.x
[research_witte_monson_2003]: https://doi.org/10.21236/ada421043
[research_wittlin_1988]: https://doi.org/10.1177/058310248802001103
[research_wolfe_1967]: https://doi.org/10.1108/eb034268
[research_wollner_1972]: https://doi.org/10.2514/3.58993
[research_wong_cox_1981]: https://doi.org/10.1016/0167-6105(81)90081-7
[research_woodcockrj_georgefl_1976]: https://ntrs.nasa.gov/citations/19760024077
[research_woodrm_millerds_1985]: https://ntrs.nasa.gov/citations/19850053430
[research_woodrowwhitlowjr_emilyntodd_1999]: https://ntrs.nasa.gov/citations/19990052675
[research_woods_gilbert_1990]: https://doi.org/10.2514/3.25336
[research_woodsjessicaa_gilbertmichaelg_1989]: https://ntrs.nasa.gov/citations/19890014953
[research_wrestler_cliftong_1965]: https://doi.org/10.21236/ad0622404
[research_wright_1945]: https://doi.org/10.21236/adb813734
[research_wu_chen_2017]: https://doi.org/10.1016/j.isatra.2017.06.015
[research_wu_chen_2020]: https://doi.org/10.1002/acs.3119
[research_wu_chiu_1992]: https://doi.org/10.1016/0041-624x(92)90034-j
[research_wu_fu_2025]: https://doi.org/10.3390/math13243986
[research_wu_livne_2016]: https://doi.org/10.2514/1.j054824
[research_wu_sun_2021]: https://doi.org/10.1002/acs.3331
[research_wu_zuo_2022]: https://doi.org/10.3390/aerospace9100610
[research_wunderlich_2015]: https://doi.org/10.1007/s13272-015-0151-6
[research_wunderlich_dahne_2017]: https://doi.org/10.1007/s13272-017-0266-z
[research_wunderlich_dahne_2017_b]: https://doi.org/10.1007/s13272-017-0251-6
[research_x_29_research_1991]: https://ntrs.nasa.gov/citations/19940014489
[research_xiang_wang_2023]: https://doi.org/10.1061/jaeeez.aseng-4658
[research_xiao_sattarov_2021]: https://doi.org/10.3390/aerospace9010004
[research_xie_wang_2025]: https://doi.org/10.1177/10775463251406565
[research_xinbing_wen_2020]: https://doi.org/10.1088/1742-6596/1605/1/012075
[research_xiong_tang_2026]: https://doi.org/10.1109/taes.2026.3683617
[research_xu_2025]: https://doi.org/10.1038/s41598-025-06503-x
[research_xu_2026]: https://doi.org/10.1038/s41598-026-56983-8
[research_xu_gao_2015]: https://doi.org/10.1155/2015/258315
[research_xu_tan_2019]: https://doi.org/10.1016/j.cja.2019.06.003
[research_xu_wang_2016]: https://doi.org/10.1371/journal.pone.0167168
[research_xu_zha_2021]: https://doi.org/10.2514/1.c035727
[research_xu_zhang_2018]: https://doi.org/10.12783/dtcse/mmsta2017/19666
[research_xu_zhang_2020]: https://doi.org/10.1109/access.2020.3041855
[research_xu_zhang_2025]: https://doi.org/10.1016/j.cja.2024.103332
[research_xu_zhang_2026]: https://doi.org/10.1007/s00158-026-04374-y
[research_xue_yao_2020]: https://doi.org/10.2322/tjsass.63.1
[research_xue_ye_2019]: https://doi.org/10.1080/19942060.2019.1663264
[research_yalvac_yats_1991]: https://doi.org/10.1177/002199839102501206
[research_yamane_1992]: https://doi.org/10.1016/0045-7930(92)90023-o
[research_yamane_friedmann_1993]: https://doi.org/10.2514/3.46315
[research_yang_gao_2020]: https://doi.org/10.1109/tac.2019.2918122
[research_yang_guruswamy_1980]: https://doi.org/10.21236/ada084172
[research_yang_huang_2017]: https://doi.org/10.2514/1.g002690
[research_yang_huang_2019]: https://doi.org/10.1016/j.jsv.2019.01.006
[research_yang_liu_1976]: https://doi.org/10.21236/ada040077
[research_yang_manning_1994]: https://doi.org/10.2514/3.46502
[research_yang_mao_2022]: https://doi.org/10.1007/s12555-021-0643-6
[research_yang_striz_1981]: https://doi.org/10.2514/3.57576
[research_yang_tang_2026]: https://doi.org/10.1038/s41597-026-07769-0
[research_yang_wan_1978]: https://doi.org/10.21236/ada061942
[research_yang_wang_2025]: https://doi.org/10.1080/23307706.2025.2486673
[research_yang_xie_2019]: https://doi.org/10.1177/0954410019885238
[research_yang_yang_2019]: https://doi.org/10.1016/j.ast.2018.11.050
[research_yang_yu_2026]: https://doi.org/10.1109/access.2026.3690473
[research_yang_zhang_2026]: https://doi.org/10.1017/aer.2026.10162
[research_yang_zhao_1989]: https://doi.org/10.2514/3.45806
[research_yang_zhao_1992]: https://doi.org/10.1016/0022-460x(92)90528-6
[research_yang_zhao_2016]: https://doi.org/10.1177/1687814016677207
[research_yao_liu_2020]: https://doi.org/10.1016/j.apor.2020.102374
[research_yates_1966]: https://doi.org/10.2514/3.43702
[research_yates_wynne_1982]: https://doi.org/10.2514/3.44803
[research_yates_wynne_1983]: https://doi.org/10.2514/3.44952
[research_yatesecarsonjr_chulichuan_1987]: https://ntrs.nasa.gov/citations/19870012837
[research_yatesecjr_wynneec_1981]: https://ntrs.nasa.gov/citations/19810016896
[research_ye_chen_2015]: https://doi.org/10.1155/2015/254975
[research_ye_yang_2024]: https://doi.org/10.1016/j.ast.2024.109161
[research_yi_jun_2015]: https://doi.org/10.1017/s0001924000004310
[research_yildizyidiray_kolmanovskyilyav_2011]: https://ntrs.nasa.gov/citations/20110016004
[research_yildizyildiray_kolmanovskyilyav_2010]: https://ntrs.nasa.gov/citations/20100033693
[research_yin_chu_2019]: https://doi.org/10.2514/1.g004193
[research_yin_huang_2025]: https://doi.org/10.1007/s11768-024-00240-8
[research_yin_wang_2017]: https://doi.org/10.12783/dtetr/amsm2017/14821
[research_ying_liqiang_2021]: https://doi.org/10.1177/26349833211057137
[research_yiplp_paulsonjwjr_1977]: https://ntrs.nasa.gov/citations/19780005071
[research_yoo_2017]: https://doi.org/10.2514/1.g002821
[research_yoo_jeong_2023]: https://doi.org/10.1007/s11081-023-09827-7
[research_you_2020]: https://doi.org/10.1088/1742-6596/1678/1/012032
[research_you_yasaee_2019]: https://doi.org/10.1016/j.compstruct.2019.111255
[research_young_garg_2018]: https://doi.org/10.1016/j.compstruct.2017.09.112
[research_yu_1987]: https://doi.org/10.1115/1.3173110
[research_yu_2018]: https://doi.org/10.4236/mme.2018.84017
[research_yu_fang_2017]: https://doi.org/10.1016/j.compstruct.2017.05.042
[research_yu_wang_2017]: https://doi.org/10.1155/2017/1592527
[research_yu_yu_2026]: https://doi.org/10.1109/access.2026.3668314
[research_yuan_thomson_2022]: https://doi.org/10.1016/j.ast.2022.107516
[research_yuanfg_reederjamesr_2001]: https://ntrs.nasa.gov/citations/20010069699
[research_yue_zhang_2017]: https://doi.org/10.1016/j.ast.2017.08.013
[research_yue_zhao_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.103148
[research_yurtsever_sahin_2026]: https://doi.org/10.3390/aerospace13070596
[research_yutuk_tikenogullari_2021]: https://doi.org/10.1016/j.compfluid.2020.104822
[research_yuvarajan_2001]: https://doi.org/10.21236/ada399688
[research_zaw_baranovski_2026]: https://doi.org/10.3390/aerospace13060563
[research_zaytseva_kuznetsov_2021]: https://doi.org/10.18698/0536-1044-2021-12-3-10
[research_zeilerthomasa_1998]: https://ntrs.nasa.gov/citations/19990010052
[research_zelenkov_2018]: https://doi.org/10.18372/1990-5548.58.13520
[research_zhai_li_2020]: https://doi.org/10.2514/1.c035766
[research_zhang_chen_2020]: https://doi.org/10.1016/j.compstruct.2019.111696
[research_zhang_dai_2026]: https://doi.org/10.2514/1.j066148
[research_zhang_han_2018]: https://doi.org/10.1007/s00158-018-2074-4
[research_zhang_li_2026]: https://doi.org/10.1080/21642583.2026.2634446
[research_zhang_liu_2018]: https://doi.org/10.1002/asjc.1821
[research_zhang_marzocca_2015]: https://doi.org/10.1177/1077546315597180
[research_zhang_qiu_2024]: https://doi.org/10.3390/act13060229
[research_zhang_shao_2022]: https://doi.org/10.1049/icp.2022.1599
[research_zhang_wang_2015]: https://doi.org/10.4028/www.scientific.net/msf.813.54
[research_zhang_wang_2019]: https://doi.org/10.2514/1.c035182
[research_zhang_wang_2022]: https://doi.org/10.1016/j.compstruct.2022.116162
[research_zhang_wang_2022_b]: https://doi.org/10.1007/s00348-022-03528-0
[research_zhang_zhao_2019]: https://doi.org/10.1016/j.jfluidstructs.2019.01.014
[research_zhang_zhao_2023]: https://doi.org/10.3390/aerospace10120981
[research_zhao_liu_2026]: https://doi.org/10.1016/j.compstruct.2026.120628
[research_zhao_liu_2026_b]: https://doi.org/10.1155/ijae/4223020
[research_zhao_luximon_2015]: https://doi.org/10.1016/j.promfg.2015.07.821
[research_zhao_zhao_2024]: https://doi.org/10.1016/j.conengprac.2024.105941
[research_zheng_dai_2026]: https://doi.org/10.1016/j.ast.2026.113066
[research_zheng_shao_2025]: https://doi.org/10.1049/icp.2024.2898
[research_zhirabok_filaretov_2024]: https://doi.org/10.31857/s0005231024070026
[research_zhong_ying_2025]: https://doi.org/10.1088/1742-6596/2977/1/012026
[research_zhou_gong_2026]: https://doi.org/10.1061/jaeeez.aseng-6212
[research_zhou_huang_2021]: https://doi.org/10.1016/j.cnsns.2021.105946
[research_zhou_peng_2026]: https://doi.org/10.1016/j.addma.2026.105131
[research_zhou_raze_2025]: https://doi.org/10.2514/1.c038195
[research_zhou_wang_2017]: https://doi.org/10.1016/j.actaastro.2017.05.011
[research_zhou_xu_2019]: https://doi.org/10.1016/j.compstruct.2018.10.035
[research_zhou_ye_1989]: https://doi.org/10.1016/b978-0-08-040185-0.50012-9
[research_zhou_yu_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.03.009
[research_zhu_du_2017]: https://doi.org/10.1007/s11071-017-3382-8
[research_zhu_shi_2022]: https://doi.org/10.1063/5.0076173
[research_zhuang_yang_2021]: https://doi.org/10.1016/j.compstruct.2020.112996
[research_zia_liu_2022]: https://doi.org/10.1007/s42242-022-00201-7
[research_ziegler_1963]: https://doi.org/10.21236/ad0405158
[research_zipperer_jenney_1975]: https://doi.org/10.21236/ada012233
[research_zipperer_jenney_1975_b]: https://doi.org/10.21236/ada009156
[research_zohar_erel_1988]: https://doi.org/10.2514/3.45578
[research_zou_huang_2025]: https://doi.org/10.1016/j.ast.2025.110155
[research_zuhri_2025]: https://doi.org/10.55981/ijoa.2025.9106
