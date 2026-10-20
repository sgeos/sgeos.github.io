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
way, and **after four articles about aircraft that were not built for research, that sentence marks a break**. The
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
It did not. A theory of wing [divergence][ref_divergence] was published in 1926
\[[Aeroelastic divergence][ref_divergence]\], the fall in divergence speed with forward sweep was charted and
checked experimentally by the National Advisory Committee for Aeronautics by 1948 \[[Diederich and Budiansky 1948][research_diederichfranklinw_budianskybernard_1948]\],
it is in every aeroelasticity textbook, and no research aeroplane was needed to establish it. A forward-swept wing
bends upward under load, the bending increases the local angle of attack, the increased angle increases the
lift, and the loop closes on itself at a computable dynamic pressure. That much was arithmetic by 1948.

**What was new was the claim that the divergence could be held rather than avoided**, by two means working
at once. The first is [aeroelastic tailoring][ref_tailoring], which uses the bend-twist coupling of an
unbalanced [composite laminate][ref_laminate] to cancel the aerodynamic coupling inside the structure. The
second is active control of an airframe deliberately made unstable, held by a triplex digital
[fly-by-wire][ref_fbw] system running at forty hertz.

* Contents
{:toc}

## The Research Question

**The keystone is the structure and the control law together, and separating them misses the aircraft.**

The X-29A was **statically unstable by a nominal thirty-five percent of the mean aerodynamic chord**, which
is to say its [static margin][ref_static_margin] was that far negative, in subsonic flight, and the primary
record is unusually direct about why. The instability was not a side effect of the forward sweep. It was
created by the canard \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\]. National Aeronautics and Space Administration
Technical Memorandum 100407 states that
**the presence of the canards results in an otherwise neutrally stable airframe having a negative static margin of nominally thirty-five percent**,
which makes the instability a deliberate purchase rather than a penalty \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].

So the aircraft posed two coupled questions that had to be answered by the same airframe at the same time.

- **Can a wing be made to resist divergence by the arrangement of its fibres**, rather than by
  being made thicker, heavier or less swept.
- **Can an airframe that doubles a pitch disturbance in a fraction of a second be flown**, by a
  sampled digital controller with a finite update rate and a finite failure probability.

**Neither question can be settled on the ground.** A wind tunnel model can be tailored and tested, and
several were, but a tunnel model does not carry a flight control system, a hydraulic actuator, a
failure-tolerant voter or a pilot \[[Landsberger and Dugundji 1985][research_landsberger_dugundji_1985]\]
\[[Chen and Dugundji 1987][research_chen_dugundji_1987]\]. An iron-bird simulator carries all of those and does not carry an elastic
wing in a real airflow.
**The X-29 exists because those two halves had to be connected, and connecting them required an aeroplane.**

### Why the Keystone Is Not the Planform

The obvious alternative keystone is the forward sweep itself, treated as an aerodynamic choice, and that
framing is available because the programme did claim aerodynamic benefits. Its flight test overview gives a
prediction of **up to thirteen percent lower aircraft drag for wings of the same aspect ratio**, arising
from reduced transonic wing profile drag \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\].

**That claim is examined below and its geometric mechanism survives, but it is not what needed an aeroplane.**
The flight programme did not demonstrate the overall drag reduction that earlier studies had suggested
\[[Gelzer 2015][ref_gelzer_x29]\] \[[Jenkins, Landis and Miller][ref_xvehicles]\]. Transonic drag is measurable in a tunnel. What is not measurable in a tunnel is whether a wing designed to sit inside a
divergence boundary actually sits inside it once built, instrumented and flown, and whether the boundary can
be located from flight data before it is reached.
**The X-29 answered that, and the answer arrived by a method that had never previously been used in flight.**
\[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\]

## Programme Origin

**The programme began with a government agency rather than a manufacturer**, which distinguishes it sharply
from the four articles before it.

### The Agency

The [Defense Advanced Research Projects Agency][ref_darpa] began the X-29A project **in 1977**. The aircraft
was designed and built by the [Grumman Aerospace Corporation][ref_grumman] and delivered to the
[Dryden Flight Research Facility][ref_dryden] of the National Aeronautics and Space Administration at
Edwards, California, where the flight programme was conducted jointly \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\] \[[Gelzer 2015][ref_gelzer_x29]\].

**Two aircraft were built.** They carried a shared research agenda that was divided between them, the first
taking the envelope expansion and performance work and the second taking the high angle of attack
investigation \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\] \[[Gelzer 2015][ref_gelzer_x29]\].

### Why Forward Sweep Became Buildable in the 1970s

The idea was old. The [Junkers Ju 287][ref_ju287] flew a forward-swept wing in 1944, and the
[Hansa Jet][ref_hansajet] carried one into production in the 1960s.
**What changed was not the aerodynamic idea but the material.**

A metal wing resists divergence only through its torsional stiffness, and buying enough of that at a
useful sweep angle costs weight that consumes the configuration's advantages.
**A composite laminate can be made to twist in a chosen direction when it bends**, because the fibres need
not run along the principal axes of the structure. That converts divergence resistance from a mass problem
into a geometry problem, and the structural loads report describes the outcome directly, crediting the tailored
skins with achieving their result
**with an insignificant weight penalty over that required for the basic strength design** \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].

**That sentence carries the justification for the programme**, and the article's structural half is an
examination of whether the physics supports it.

### Where the Aircraft Came From

The airframe was assembled from existing parts wherever the research did not require otherwise. The flight test
overview lists the **forward fuselage and nose gear of an [F-5A][ref_f5]**, the
**main landing gear and servo-actuators of an [F-16][ref_f16]**, and **[F-14][ref_f14] avionics**
\[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\].

**Only the parts carrying the research question were new.** The wing, the canard, the strake flaps and the
flight control system were designed for this aircraft \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\]. Everything else was bought from the company's own
back catalogue and from its competitors, which is why two research aeroplanes were affordable at all.

## The Vehicle

| Quantity | Value |
|---|---|
| Wing area | 188.84 ft² |
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

The table draws on the flight reports \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\] \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\]
\[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\], except the wing area of 188.84 square feet, which is taken from the encyclopaedia
entry \[[Grumman X-29][ref_x29]\]. The reports use a trapezoidal reference area of 185 square feet.

### What the Table Implies

Before either of those, the table supports a handful of ratios that it does not state, and they place the
aircraft among its contemporaries. The sizing conventions used here follow [Raymer][book_raymer], with the
airframe practice in [Niu][book_niu].

The wing loading is the gross weight carried per unit of reference area.

$$ \frac{W}{S} = \frac{17{,}800\ \mathrm{lb}}{188.84\ \mathrm{ft}^2} = 94.26\ \mathrm{lb/ft^2} $$

At the manoeuvre design gross weight the same relation gives 79.43 pounds per square foot, and both figures
are ordinary for a fighter-sized aircraft of the period.

The thrust-to-weight ratio uses the engine's class rating, because the record gives no installed thrust
figure.

$$ \frac{T}{W} = \frac{16{,}000\ \mathrm{lb}}{17{,}800\ \mathrm{lb}} = 0.899 $$

$$ \left.\frac{T}{W}\right|_{\mathrm{manoeuvre}} = \frac{16{,}000\ \mathrm{lb}}{15{,}000\ \mathrm{lb}} = 1.067 $$

**At the manoeuvre design weight the aircraft has more thrust than weight**, which matters below because it
makes the airframe rather than the engine the binding limit in a sustained turn.

The canard is quoted only as a percentage, so its area and chord follow.

$$ S_c = 0.20\,S = 0.20 \times 188.84\ \mathrm{ft}^2 = 37.77\ \mathrm{ft}^2 $$

$$ \bar{c}_c = 0.76\,\bar{c} = 0.76 \times 7.217\ \mathrm{ft} = 5.485\ \mathrm{ft} $$

The design load and the fuel fraction complete the picture.

$$ n W = 8.0 \times 15{,}000\ \mathrm{lb} = 120{,}000\ \mathrm{lb} $$

**The wing carries 120,000 pounds at the subsonic design limit**, the load the structural box and
its tailored skins had to survive while also satisfying the divergence requirement.

$$ \frac{W_{\mathrm{fuel}}}{W_{\max}} = \frac{4{,}000\ \mathrm{lb}}{17{,}800\ \mathrm{lb}} = 0.225 $$

**The heaviest weight flown exceeded the manoeuvre design weight by eighteen percent**, which the
record states and which the ratio confirms \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].

$$ \frac{17{,}700}{15{,}000} - 1 = 0.180 $$

**Two entries in that table are the aeroplane and the rest follows from them.**

The first is the **structural axis sweep of 36.2 degrees forward**, seven degrees more forward than
the leading edge \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\]. That difference is not incidental. It means the structure is swept further forward than
the planform suggests, and since divergence is governed by the elastic axis rather than by the leading edge,
**the wing is aeroelastically more forward-swept than it looks.**

Beside it stands the **static margin of minus thirty-five percent**, and the number is not small. The
[F-16][ref_f16], the first production fighter designed to be intentionally unstable, was only slightly so
\[[General Dynamics F-16 Fighting Falcon][ref_f16]\].
**This aircraft was built much further into instability than the aircraft it was meant to inform.**

### A Consistency Check on the Published Geometry

The flight reports give the aspect ratio as 4.0 \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\], and the encyclopaedia
entry gives the wing area as 188.84 square feet and the span as 27 feet 2.5 inches \[[Grumman X-29][ref_x29]\].
Those are three statements about two quantities, so one of them can be checked.

$$ b = \sqrt{A S} = \sqrt{4.0 \times 188.84\ \mathrm{ft}^2} = 27.48\ \mathrm{ft} $$

Against a quoted span of 27.21 feet that is an agreement to **0.99 percent**. The residual is not rounding.
The same relation applied to the reports' own reference area of 185 square feet returns 27.20 feet, against
the span of 27 feet 2.44 inches in the structural loads report \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\], so the aspect ratio of
4.0 is defined on the trapezoidal reference area and the larger figure is a different definition of wing area.
**The published geometry is mutually consistent**, and that needs establishing before anything is built
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

**The X-29's divergence boundary is not stated as a number in the reports cited here.** What was published is something better,
because it can be inverted.

### The Relation Behind the Inversion

A wing that washes in under load amplifies its own lift. At any dynamic pressure below the divergence
boundary the elastic wing produces more lift per degree of angle of attack than the same wing would produce
if it were rigid, and the ratio between the two grows without limit as the boundary is approached.
**That growth without limit is the definition of divergence rather than a consequence of it.**

For the single-degree-of-freedom case the relation is exact.

$$ \frac{C_{L_\alpha}^{\mathrm{elastic}}}{C_{L_\alpha}^{\mathrm{rigid}}} = \frac{1}{1 - q/q_D} $$

Here $q$ is the free-stream dynamic pressure and $q_D$ is the divergence dynamic pressure, the value at
which the amplification becomes unbounded.

### Where the Amplification Comes From

The relation is not asserted. It follows from the feedback loop the wing closes.

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

For the research literature behind this relation, see the cluster on structural mechanics, buckling and structural weight under The Contemporary Literature.

**The amplification is the same factor for lift, for twist and for the loads**, so a prediction of it is
worth publishing and an error in it moves every quantity at once.

**A single report states both of the quantities needed to invert this.** The structural loads memorandum,
Technical Memorandum 101715, gives the wing's **predicted elastic-to-rigid lift-curve-slope ratio as about 1.6**, and gives the
**design dynamic pressure as 1,700 pounds per square foot at Mach 1.07 at sea level**
\[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\]. Neither figure was derived from the other.

### Checking the Design Point Against Itself

Before inverting anything, the design point is quoted twice over, once as a dynamic pressure and once as a
Mach number at an altitude, so the two statements can be checked against one another.

$$ q = \tfrac{1}{2} \rho_0 \left(M a_0\right)^2 = \tfrac{1}{2} \times 0.0023769 \times \left(1.07 \times 1116.45\ \mathrm{ft/s}\right)^2 = 1695.9\ \mathrm{lb/ft^2} $$

Against the quoted 1,700 pounds per square foot that agrees to **0.24 percent**.
**The check is on the source alone**, and it passes, so the two statements
in the report describe the same flight condition and either may be used.

### Inverting for the Divergence Boundary

Rearranging the amplification relation for $q_D$ gives the boundary directly.

$$ q_D = \frac{q}{1 - 1/r}, \qquad r = \frac{C_{L_\alpha}^{\mathrm{elastic}}}{C_{L_\alpha}^{\mathrm{rigid}}} $$

Substituting the two published figures,

$$ \frac{q}{q_D} = 1 - \frac{1}{1.6} = 0.375 $$

$$ q_D = \frac{1700\ \mathrm{lb/ft^2}}{0.375} = 4533\ \mathrm{lb/ft^2} $$

**The X-29A's wing diverged at about 4,533 pounds per square foot**, and that number appears in none of the
reports cited here. It follows from two figures that do appear, through a relation neither was derived from, and
**it requires no knowledge whatever of the wing's stiffness, its geometry, its material or its ply angles.**

### What That Margin Was

The margin is best stated twice, because dynamic pressure and speed are not the same statement.

$$ \frac{q_D}{q_{\mathrm{design}}} = 2.667, \qquad \frac{V_D}{V_{\mathrm{design}}} = \sqrt{2.667} = 1.633 $$

Dynamic pressure and equivalent airspeed are related through sea-level density alone, so equivalent
airspeed is the natural currency for a structural limit.

$$ q = \tfrac{1}{2}\rho V^2 = \tfrac{1}{2}\rho_0 V_e^2, \qquad V_e = \sqrt{\frac{2q}{\rho_0}} $$

Expressed as equivalent airspeeds,

$$ V_{e,\mathrm{design}} = 709\ \mathrm{kt}, \qquad V_{e,D} = 1157\ \mathrm{kt} $$

**A factor of 2.667 in dynamic pressure sounds comfortable and a factor of 1.633 in speed sounds much less so**,
and a pilot experiences the latter. The aircraft's design point sat at
**thirty-seven and a half percent of the way to a structural instability with no natural limit**, and the
amplification at that point was already sixty percent.

The approach is tabulated below, because the relation is strongly non-linear and its behaviour near the
boundary makes the problem difficult.

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

The boundary was inverted from a ratio quoted to two significant figures, so the cost of
that rounding needs measuring. Writing the inversion as a product makes the sensitivity immediate.

$$ q_D = \frac{q\,r}{r - 1} \quad \Longrightarrow \quad \frac{d \ln q_D}{d \ln r} = -\frac{1}{r - 1} $$

$$ \left.\frac{d \ln q_D}{d \ln r}\right|_{r = 1.6} = -\frac{1}{0.6} = -1.667 $$

**A one percent error in the published ratio is a 1.67 percent error in the boundary derived from it**, and
the sign is negative, so a ratio that was optimistically low produces a boundary that is optimistically
high. That elasticity is used again in the section on where the framing breaks down.

**The 3,000 and 4,000 rows of the table under What That Margin Was explain why the margin had to be as large as it was.** Between 3,000 and 4,000 pounds
per square foot the wing's lift amplification triples, and a design error of ten percent in the predicted
boundary moves the loads by far more than ten percent.
**The penalty for being wrong is not proportional to the size of the error.**

For comparison, the same report notes that
**conventional aft-swept wings have elastic-to-rigid ratios below one** \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\], because bending washes them out
rather than in. The X-29's wing sits on the other side of unity by construction, and the sign alone separates
the two.

The Contemporary Literature gathers the work on this subject in the cluster on divergence and static aeroelasticity.

### Where the Washin Comes From

The inverted boundary is a number without a mechanism. The mechanism is one line of geometry.

Let $y$ run along the wing's elastic axis and let $\Lambda$ be the sweep of that axis, positive aft. A
deformed section rotates for two reasons, namely the elastic twist $\theta$ about the axis and the bending
slope $w'$ perpendicular to it. Resolving both onto the spanwise direction that a streamwise section pitches
about gives the change in streamwise angle of attack.

$$ \Delta\alpha(y) = \theta(y)\cos\Lambda - w'(y)\sin\Lambda $$

**That single relation contains the forward-sweep problem.** For an aft-swept wing $\sin\Lambda$ is
positive, so upward bending subtracts from the angle of attack and the wing washes out, a stabilising effect
that makes swept-back wings difficult to diverge.
**For a forward-swept wing $\sin\Lambda$ is negative, the sign of the bending term reverses, and upward bending adds to the angle of attack.**
The wing washes in, the lift grows, the bending grows, and the loop closes.

**The sign of one trigonometric function is the difference between a wing that is safe and a wing that needs a research programme.**

### What a Two-Mode Model Is For

The boundary is already known from the inversion above and needs no model. What a model supplies is
the **scaling**, meaning how the boundary moves with sweep and with bend-twist coupling, and the rest of
this section uses that scaling.

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

**The characteristic equation is linear rather than quadratic, an exact consequence of the model and not an approximation.**
The quadratic coefficient is

$$ (ca)^2 e\,L\cos\Lambda\sin\Lambda\left(-\tfrac{1}{6} + \tfrac{1}{6}\right) = 0 $$

identically. The point matters because a solver that does not know it will find the cancellation only to
floating-point precision, take the quadratic branch, and return values with no physical content whatever.
**A solver that takes that branch reports a divergence dynamic pressure many orders of magnitude beyond any physical value.**
A residue sixteen orders of magnitude below the terms that produced it is enormous in absolute terms, so an
absolute tolerance cannot catch it and the test has to be made relative to the magnitude of what cancelled.

Work on assumed-mode methods is surveyed in the cluster on the Southwell method, Rayleigh-Ritz and assumed modes.

### The Root in Closed Form

Because the characteristic equation is linear, the untailored root can be written out, and the closed form is far more
informative than the eigenvalue it came from.

$$ \frac{1}{q_D} = \underbrace{\frac{c\,a\,e\,L^2\cos\Lambda}{3\,GJ}}_{\text{torsion}} \;-\; \underbrace{\frac{c\,a\,L^3\sin\Lambda}{8\,EI}}_{\text{bending}} $$

**The first term is ordinary torsional divergence and is always positive.** What follows it is the bending
contribution, and **its sign is the sign of the sweep**. Aft sweep subtracts from the reciprocal and raises
the boundary. Forward sweep adds to it and lowers the boundary. The forward-sweep problem is one minus sign
in one term.

**The relation also shows something the eigenvalue does not.** If aft sweep is carried far enough the two
terms cancel, the reciprocal vanishes, and the boundary goes to infinity. Setting them equal and dividing
through by the cosine gives the critical angle in closed form.

$$ \tan\Lambda_{\mathrm{crit}} = \frac{8\,e\,EI}{3\,GJ\,L} = 48.013^\circ $$

**The closed form checks the numerical solver as much as it delivers a result.** It and the eigenvalue scan
agree to every digit printed at every sweep angle tested, from forty degrees forward to forty-eight aft,
and that agreement makes the sweep table below trustworthy although its stiffnesses were never published.

Its literature appears under The Contemporary Literature, mostly in the cluster on transonic wing design and sweep.

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

**Sweeping aft raises the boundary steeply and sweeping forward lowers it**, as
expected. Pushed further, the model does something better than agreeing in direction.

$$ \Lambda \geq \Lambda_{\mathrm{crit}} = 48.0^\circ \implies \text{no positive root, and therefore no divergence boundary at all} $$

**Sufficient sweepback removes divergence entirely**. The classical textbook result agrees, and the
model was not fitted to reproduce it. Recovering it from an independent scan of the determinant is the
strongest available evidence that the formulation is sound, and on that evidence the sweep trend above can
be trusted even though the absolute numbers cannot.

### What Aeroelastic Tailoring Had to Supply

Bend-twist coupling is reported here as a non-dimensional ratio, because the raw stiffness is meaningless
without the others. The laminate mechanics behind it are in [Jones][book_jones_composite] and
[Tsai and Hahn][book_tsai_hahn], and the aeroelastic consequences in
[Bisplinghoff, Ashley and Halfman][book_bisplinghoff] and [Hodges and Pierce][book_hodges].

$$ \psi = \frac{K}{\sqrt{EI \cdot GJ}} $$

The bound on it is the determinant of the stiffness matrix staying positive.

$$ EI \cdot GJ - K^2 > 0 \quad \Longleftrightarrow \quad \lvert \psi \rvert < 1 $$

**The bound $\lvert \psi \rvert < 1$ is not a modelling convenience. It is positive definiteness of the stiffness matrix**,
a condition on strain energy, and no laminate at any ply angle can exceed it. Because of that bound the
following question has a definite answer.

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
wing's boundary and multiplying it by the 2.667 established from the inversion. That comes to
**roughly five eighths of the theoretical maximum**, a large fraction of a hard physical bound to
spend on one requirement.

**Second, there is a value of coupling beyond which the wing does not diverge at any speed.** At $\psi =
0.812$ the positive root disappears, as it does under sufficient sweepback.
**The technology does not merely raise the boundary. It can remove it.**

### Whether That Number Survives the Assumptions

The required coupling was computed with unpublished stiffnesses, so the obvious objection is that it is
an artefact of the assumption. It is not, and the reason follows.

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

The cluster on aeroelastic tailoring and bend-twist coupling, under The Contemporary Literature, holds the research records on this question.

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
strain-gauge loads and twist from the flight deflection measurement system. The preliminary flight
assessment notes that
**although this was the first application of the Southwell technique to flight test data, it had been used previously to analyse wind tunnel data.**
\[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\]

The report also records that the resulting estimate was
**sensitive to a number of factors including measurement uncertainties, manoeuvre technique, aerodynamic phenomena, and strain gauge loads measurement stations**,
and does not say how sensitive \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\]. That is computable.

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
**The X-29A sat at 0.375 on that table at its design point**, so the geometry of its envelope put it
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
This gives the report's warning its quantitative content. A five percent error in twist becomes a seven
percent error in the divergence boundary, and at the amplification rates tabulated earlier a seven percent
error in the boundary is a large error in the loads.

**The method is sound and the flight application was a genuine first** \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\]. What limited it was that the
aircraft could not fly close enough to the thing it was trying to measure, which is the same difficulty in a
different form.

Records on the method's flight use and on the wing it measured fall in the clusters on the X-29 and forward-swept wing aircraft and on aeroelastic tailoring and bend-twist coupling.

## Dependent Systems

### The Wing Structure

The wing skins are **graphite-epoxy composite**, upper and lower, and the flight assessment is explicit that
they exist to **aeroelastically tailor the wing deflection and inhibit wing structural divergence**
\[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\]. The
mechanism is stated as **proper ply orientation** producing
**bend-twist coupling combined with high material stiffness properties** to minimise
**the natural washin tendencies under load** \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].

The structural axis is swept further forward than the planform, and the difference is not small.

$$ \Lambda_{\mathrm{struct}} - \Lambda_{LE} = 36.2^\circ - 29.3^\circ = 6.9^\circ $$

**Because divergence is governed by the elastic axis**, the wing is aeroelastically almost seven degrees
more forward-swept than it appears, and the closed-form root above depends on the sine of the larger
angle.

The amplification applies to the loads as well as to the lift, so it binds the structure and is more than
an aerodynamic curiosity.

$$ \frac{M_{\mathrm{root}}^{\mathrm{elastic}}}{M_{\mathrm{root}}^{\mathrm{rigid}}} \;\geq\; \frac{1}{1 - q/q_D} = 1.6 \quad \text{at the design point} $$

**The inequality runs that way because washin loads the tip preferentially**, moving the centre of pressure
outboard and lengthening the lever arm, so the bending moment grows by at least the lift amplification and
in general by more.

**The same report is equally explicit that the cure was partial.** Even so, it adds, the aeroelastic
properties **remain significantly adverse**, and the elastic-to-rigid ratio of 1.6 quantifies that
sentence \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\]. The wing was not made to behave like an aft-swept wing. It was made to diverge far enough
outside the envelope to be flyable, and it still amplified its lift by sixty percent at the design
point.

The structural box **transitions from unswept inboard to swept constant chord lines outboard**, and the four
load measurement stations were oriented to place the torsion axes midway through the box.
**Eighteen strain gauge bridges were installed at each station**, some of them on the composite itself, and
the record notes that equation accuracies were
**typical of Dryden's experience with conventional all-metallic structures**, a quietly significant
result about instrumenting composites at all \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].

The span load distribution was expected to be unconventional,
**particularly in the inboard region because of the strong canard downwash** \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\], the first appearance
of a theme that recurs across the aircraft. **The canard and the wing cannot be analysed separately.**

The survey places the literature on composite wing structure in the cluster on composite structures, damage and certification.

### The Flight Control System

**A thirty-five percent negative static margin translates into time.**

The unstable airframe's pitch response splits into two real roots, one of them positive, and the positive
root sets how long the aircraft takes to double a disturbance. Neglecting pitch damping, which errs toward
less available time,

$$ M_\alpha = \frac{q\,S\,\bar{c}\,C_{m_\alpha}}{I_{yy}}, \qquad t_2 = \frac{\ln 2}{\sqrt{M_\alpha}} $$

The lift-curve slope in the table below is not quoted anywhere in the record and is estimated from the
planform by the standard low-aspect-ratio relation, which follows [Etkin][book_etkin] and
[Stevens and Lewis][book_stevens_lewis].

$$ C_{L_\alpha} = \frac{2\pi A}{2 + \sqrt{\dfrac{A^2\beta^2}{\eta^2}\left(1 + \dfrac{\tan^2\Lambda_{c/2}}{\beta^2}\right) + 4}}, \qquad \beta^2 = 1 - M^2 $$

At Mach 0.9 that returns 5.037 per radian, and the pitching moment derivative follows from the static
margin.

$$ C_{m_\alpha} = -C_{L_\alpha}\,\mathrm{SM} = -5.037 \times (-0.35) = 1.763 $$

**A positive pitching moment derivative is the source of the aircraft's difficulty**, because it means a
disturbance in angle of attack produces a moment that increases it.

Here $C_{m_\alpha} = -C_{L_\alpha} \cdot \mathrm{SM}$, so that a negative static margin makes the pitching
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

The lift-curve estimate draws on the literature in the cluster on lift, induced drag and aerodynamic estimation.

### Two Doubling Times That Are Easy to Confuse

The figure above is the doubling time of an established exponential. A disturbance released from rest with
zero pitch rate does not follow an exponential, because both roots are excited, and the response is a
hyperbolic cosine.

$$ \alpha(t) = \alpha_0 \cosh\left(\lambda t\right), \qquad \lambda = \sqrt{M_\alpha} = 6.931\ \mathrm{s^{-1}} $$

The two doubling times therefore differ by a fixed factor.

$$ t_2^{\exp} = \frac{\ln 2}{\lambda} = 0.100\ \mathrm{s}, \qquad t_2^{\cosh} = \frac{\operatorname{arcosh} 2}{\lambda} = 0.190\ \mathrm{s} $$

$$ \frac{t_2^{\cosh}}{t_2^{\exp}} = \frac{\operatorname{arcosh} 2}{\ln 2} = 1.900 $$

**A factor of 1.900 is large enough to read as a real discrepancy if the two are mixed up**, and this
article uses the exponential figure, the conservative one, throughout.

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
The ratio makes the case for forty hertz without any appeal to a specification, and it explains why the
primary literature quotes the update rate as though it were a design feature and not an implementation
detail. **It was a design feature.**

The survey treats sampled-data delay in the cluster on sampled-data control and time delay.

### Redundancy Measured Against the Same Clock

Triplex redundancy with majority voting tolerates one channel failure. The probability that fewer than two
of three independent channels survive follows the binomial.

$$ P_{\mathrm{loss}} = \sum_{k=0}^{1} \binom{3}{k}(1-p)^k p^{3-k} $$

| Per-channel failure probability | Triplex loss | Simplex loss | Improvement |
|---|---|---|---|
| 10⁻³ | 3.00 × 10⁻⁶ | 10⁻³ | 334 |
| 10⁻⁴ | 3.00 × 10⁻⁸ | 10⁻⁴ | 3,334 |
| 10⁻⁵ | 3.00 × 10⁻¹⁰ | 10⁻⁵ | 33,334 |

**Voting arithmetic is the easy half of the redundancy argument, and it does not bind.** Voting requires
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
and that inversion is one of the transferable results of the programme.

The system carried three flight modes, the **normal digital** mode as prime, with **digital reversion** and
**analog reversion** below it, each having an up-and-away and a power-approach configuration, and extensive
gain scheduling in every mode except the two reversionary power-approach cases
\[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].

Three clusters under The Contemporary Literature cover this ground, on handling qualities and pilot-vehicle interaction, on digital fly-by-wire, redundancy and fault tolerance, and on flight control law design.

### A Canard Boundary Set by the Control Loop

**The single most interesting structural fact about this aircraft is that its canard was also divergence prone, and that a control law requirement fixed the structural boundary.**

An all-moving surface on a torsional spring diverges when the aerodynamic moment about its axis overcomes
the spring.

$$ q_{D,\mathrm{surface}} = \frac{K_\theta}{e\,S\,a} $$

The structural loads report places the canard's torsion axis
**about midway between the 25 percent and 50 percent mean aerodynamic chord points**, chosen to balance
subsonic against supersonic hinge moments, and describes that location in as many words as
**not conservatively located from a divergence viewpoint**. It then states the fact that defines this
aircraft.
**The pitch-loop stiffness required for control system stability resulted in a predicted divergence boundary that was well beyond that for the wing.**
\[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\]

**The spring is not only the spindle.** It is the spindle in series with the actuator, and through the
actuator with the flight control system's pitch loop. A stiffness bought to make the control law stable
turned out to be the stiffness that kept the surface from diverging.

$$ K_\theta^{\mathrm{req}} = q_D\,e\,S_c\,a, \qquad e = \left(x_{\mathrm{axis}} - x_{ac}\right)\bar{c}_c $$

Inverting the relation for the loop stiffness that would place the canard's boundary at the wing's 4,533
pounds per square foot gives the scale of what was required.

| Torsion axis, percent of mean aerodynamic chord | Moment arm, ft | Required stiffness, 10⁶ ft·lb/rad |
|---|---|---|
| 30.0 | 0.274 | 0.295 |
| 37.5 | 0.686 | 0.738 |
| 45.0 | 1.097 | 1.180 |
| 50.0 | 1.371 | 1.475 |

**Moving the axis from thirty percent to fifty percent of the chord multiplies the required stiffness by five**,
because the moment arm grows from a quarter of a foot to nearly a foot and a half. The record's remark that
the chosen location was a **major tradeoff** is therefore an understatement of the sensitivity rather than
of the difficulty \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].

**Canard free play was tracked as a major concern throughout** \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\], which follows directly. Free play is a
region of zero stiffness, and a spring with a dead band in it has no stiffness at all near the origin.

Research on the interaction of control loops with structural modes is collected in the cluster on aeroservoelasticity and structural mode control.

### Trim and the Case for Putting the Surface in Front

The static margin is the distance from the centre of gravity to the neutral point, measured in mean
aerodynamic chords, and it is negative when the neutral point lies ahead.

$$ \mathrm{SM} = \frac{x_{np} - x_{cg}}{\bar{c}} = -0.35 $$

A supercritical section carries a large nose-down pitching moment about its aerodynamic centre, the
price of its aft loading. That moment must be trimmed at every flight condition, and
**the sign of the load that trims it is the core of the argument for a canard.**

The moment balance uses the surface's own lift coefficient against the tail volume coefficient, which is
defined as

$$ V_H = \frac{S_s}{S}\cdot\frac{l}{\bar{c}} $$

$$ C_{L_{\mathrm{surface}}} V_H = -C_{m_{ac}} $$

The quantity that enters the drag comparison, however, is the lift the surface contributes referenced to the
wing, which is $C_{L_{\mathrm{surface}}} S_s / S$. Substituting the volume coefficient,

$$ \Delta C_L = -\frac{C_{m_{ac}}}{l/\bar{c}} $$

and **the surface area cancels completely.** The trim increment depends only on the aerofoil's moment and
the moment arm. That deserves emphasis, because it is easy to carry the surface's own lift coefficient into
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

| Section moment $C_{m_{ac}}$ | Arm, mean aerodynamic chords | Surface $C_L$ | Wing-referenced $\Delta C_L$ | Drag ratio |
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

**The advantage is real across the tabulated range and it is modest**, running from about eleven percent to
about sixty-five percent depending on how aft-loaded the section is and how long the arm. It is not the
dominant term in the aircraft's drag, and an article that presented the canard purely as a drag reduction
device would be overstating a secondary effect.

The canard was **truly close coupled to provide mutual interference with the wing aerodynamics**, coplanar
and without dihedral. The record states that
**canard lift due to angle of attack is approximately 1.5 times that due to canard incidence**, and warns
that
**any misprediction of these interference effects could have a large influence on the load distributions of both surfaces.**
\[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\]

The literature on trimming surfaces sits under The Contemporary Literature in the cluster on canards, trim and multiple lifting surfaces.

### The Transonic Argument

The programme's aerodynamic claim was a drag saving of
**up to thirteen percent for wings of the same aspect ratio**, and the primary sources give a specific
mechanism \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\].
**A forward-swept wing requires less leading-edge sweep for the same shock sweep and location.**
\[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\]

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
because the trailing edge moves in opposite directions in the two cases. The effects compound, and
matching the isobar costs the aft-swept wing a great deal of leading-edge sweep.

$$ \Lambda_{LE}^{\mathrm{aft}} = 44.70^\circ \quad \text{to match} \quad \Lambda_{50\%} = 37.79^\circ $$

**The aft-swept wing needs 44.70 degrees of leading-edge sweep to achieve what the forward-swept wing achieves with 29.30, a difference of 15.40 degrees.**
The primary source's claim is therefore correct and now has a number attached to it.

Sweep earns its keep by reducing the Mach number the section sees, and the isobar sweep governs that
reduction rather than the leading-edge sweep.

$$ M_n = M\cos\Lambda_{50\%} $$

| Flight Mach | Normal to the 50 percent isobar |
|---|---|
| 0.90 | 0.711 |
| 1.07 | 0.846 |
| 1.48 | 1.170 |

**At the design point of Mach 1.07 the section sees 0.846**, which is subsonic, and keeping the normal
Mach number subsonic is the purpose of sweeping a wing.

The structural consequence follows. Computing the box length between a fifteen percent front spar and a
seventy percent rear spar for both planforms at equal isobar sweep gives
**17.12 feet forward-swept against 17.66 feet aft-swept**, a ratio of 0.969, so the forward-swept box is
**about three percent shorter**.

A shorter box shortens the lever arm the root bending moment acts
through.

$$ M_{\mathrm{root}} = \tfrac{1}{2}n\,W\,\eta_{cp}\,\frac{b}{2} = \tfrac{1}{2} \times 8.0 \times 15{,}000 \times 0.4 \times 13.74\ \mathrm{ft} = 3.30 \times 10^{5}\ \mathrm{ft\,lb} $$

**That comparison must be made at equal shock sweep and not at equal leading-edge sweep, and the difference between those two questions reverses the answer.**
At equal leading-edge sweep the same calculation gives 17.12 feet forward against 14.70 feet aft, making the
forward-swept box the longer of the two. **Both numbers are correct and they answer different questions.**
The one that bears on the programme's claim is the first, because a wing is designed to a shock position
rather than to a leading-edge angle.

The contemporary records on this argument are in the clusters on transonic wing design and sweep and on flutter, gusts and very flexible aircraft.

### Propulsion and the Rest

The engine is a single **General Electric F404-GE-400 of the 16,000 pound class**, mounted in the fuselage
with **two side-mounted fixed-geometry inlets optimised for transonic performance** \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\]. Fixed geometry is the
correct choice for an aircraft whose supersonic excursions are incidental to its purpose, and the inlets are one of
the places where the programme declined to spend money on a technology it was not investigating.

Maximum takeoff gross weight is 17,800 pounds with 4,000 pounds of fuel in two fuselage and two strake
tanks \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\]. Design symmetric load factors were
**8 g subsonic and 6.5 g supersonic at a manoeuvre design gross weight of 15,000 pounds**, and the record
notes that gross weights flown ranged from about 14,800 to 17,700 pounds, the upper figure being
**an eighteen percent increase over the manoeuvre design gross weight** \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].

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
design weight, so **at low altitude the airframe binds before the engine does**. The result follows from
the thrust-to-weight ratio computed at the top of the article exceeding unity at that weight.

**Ten to eleven is an unremarkable figure for a fighter-sized aircraft of this aspect ratio**, and the
X-29's aerodynamic interest was never in its cruise efficiency.

Performance work of this kind is surveyed in the cluster on manoeuvre performance, agility and energy methods.

### Instrumentation

**Six hundred and ninety-one measured parameters were telemetered to the ground**, and the aircraft
**had no onboard recording capability at all**, a striking design decision that made the telemetry
link a single point of failure for the research product if not for the aircraft \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].

The ten-bit remote-unit pulse-code modulation system sampled **from 25 to 400 samples per second** depending
on the frequency range required \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\], with fourteen selected parameters raised to
200 or 400 when substantial buffet loads were encountered \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\]. Those rates are
chosen against the same criterion that governs the flight control system, and the range from 25 to 400
samples per second corresponds to a usable band an order of magnitude wide.

$$ f_{\max} \leq \frac{f_s}{2} \quad \Longrightarrow \quad 12.5\ \mathrm{Hz} \leq f_{\max} \leq 200\ \mathrm{Hz} $$

**The structural modes the aeroservoelastic work needed to see lie inside that band**, and the fourteen
parameters raised to the top of it were raised for buffet loads \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].

A constant-bandwidth frequency modulation system handled high-response acceleration and vibration data. The
**flight deflection measurement system** supplied the wing twist that the Southwell analysis depended on,
so the keystone result depends on that instrument \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].

Records on the aircraft's instrumentation and test methods appear under The Contemporary Literature, in the clusters on high angle of attack and vortex flow and on flight test, instrumentation and identification.

## The Flight Test Record

**Two aircraft flew, and they flew a divided programme.**

The first X-29A made its first flight on **14 December 1984** and carried the envelope expansion and the
performance work. The second flew from **1989** and carried the high angle of attack investigation
\[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\] \[[Gelzer 2015][ref_gelzer_x29]\]. The record of how many flights each made is not consistent across
sources \[[Gelzer 2015][ref_gelzer_x29]\] \[[Jenkins, Landis and Miller][ref_xvehicles]\] \[[Grumman X-29][ref_x29]\], and the source base below
reports the disagreement without resolving it.

**The envelope expansion itself is precisely documented.** The primary record states that expansion of the
aircraft's one-g and manoeuvre flight envelopes **was completed over a two-year period in 84 flights** \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\],
a slow rate by the standards of the aircraft in this series and an appropriate one for an
airframe whose failure modes included a structural instability with no natural limit.

**The overall verdict in the primary literature is favourable and is stated without hedging.** Flight
results **confirmed the viability of the aircraft design**, good agreement with preflight predictions
**was obtained**, and the individual technologies' operational workability and performance
**were confirmed** \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].

### What Was Measured

Four of the measured things need separating, because they did not all succeed equally
\[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\] \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].

- **The static loads distribution**, from four wing stations and the canard, with eighteen strain gauge
  bridges per station.
- **The structural dynamic characteristics**, from natural turbulence, control surface raps and a
  frequency-sweep flaperon exciter.
- **The flight control system characteristics**, across three modes and two configurations.
- **The aerodynamic performance**, meaning the drag polar shape above minimum parasite drag.

**The drag polar work was compromised by instrumentation rather than by the aircraft.** Polar shape data
could only be obtained subsonically, because
**a lack of afterburner fuel flow instrumentation prevented the calculation of accurate afterburner thrust in supersonic flight**.
Further difficulties arose in the angle-of-attack calibration and from manoeuvre dynamics effects caused by
being off the optimum wing camber schedule. **The engine was not thrust-calibrated**, and a
thrust-calibrated engine was planned for the follow-on phase \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\]
\[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\].

**The admission is honest and unusual for a programme report**, and it means the aircraft's
supersonic drag, where the forward-swept wing's transonic argument would have been most directly
testable, was not measured during this phase at all \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\].

## Comparison With Ground Prediction

**Four comparisons are available in the primary record and they do not all point the same way.**

### The Drag Polar Beat Its Prediction

**Induced drag levels were as much as twenty percent less than wind tunnel estimates**, particularly at lift
coefficients above 0.8, and the basic drag polar shapes **met or exceeded wind-tunnel-based predictions**.
Comparison with other modern fighters showed the X-29A to have the better overall Oswald efficiency factor
for the same aspect ratio \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\] \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].

**A twenty percent overprediction of induced drag by a tunnel is a large error in the conservative direction**,
and a result of that kind supports the configuration more strongly than a matching prediction would
have. In the subsonic and low transonic polar data the aircraft was better than the ground said it would be.

### The Divergence Boundary Was Worse Than Predicted

**Preliminary results indicated a lower divergence speed than predicted**, though the boundary was
**still outside the flight envelope** \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].

This finding matters most and needs careful statement.
**The prediction was optimistic about the single quantity the aircraft existed to demonstrate.** The margin
survived, the aeroplane was never in danger, and the technology was vindicated. But the ground analysis was
wrong in the direction that costs margin rather than the direction that wastes it, and the loads analysis
had framed the underlying risk in terms that anticipate this.
**Errors in the predicted load distributions or stiffness characteristics could lead to greater load amplifications and a lower divergence boundary for a forward-swept-wing design.**
\[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\]

**The programme predicted its own failure mode correctly and then experienced a mild version of it.**

### The Canard Loads Were Worse Than Predicted

**Canard torsion loads were consistently higher than predicted at transonic Mach numbers**, especially at
high dynamic pressure, and were **highly sensitive to sideslip angle**. The report adds that
**the difference between the flight test data and the predictions is not fully understood** and was still
under investigation \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].

**This is the surface whose divergence boundary the control loop set**, and the torsion loads are the second
independent sign that the canard was the least well predicted part of the aircraft. The warning quoted
earlier, that any misprediction of the canard-wing interference could have a large influence on the load
distributions of both surfaces, turned out to be the right thing to have worried about.

### The Buffet and Control System Interacted

A separate body of the flight record concerns
**buffet-induced structural and flight control system interaction**, and an
**in-flight interaction of the canard and the flight control system** significant enough to be the subject
of its own report \[[Voracek and Clarke 1991][research_voracekdavidf_clarkerobert_1991]\]
\[[Kehoe et al 1990][research_kehoemichaelw_bjarkelisaj_1990]\].

**An aeroservoelastic interaction occurs when a structure and a control law that were designed separately meet.**
For an aircraft whose canard stiffness was partly supplied by its pitch loop, the appearance of one is close
to inevitable, and its appearance in the flight record is the clearest possible evidence that the structure
and the control law were a single system rather than two.

The survey follows this interaction into the cluster on flutter, gusts and very flexible aircraft.

## What the Data Changed

**The X-29's forward-swept wing was never adopted, and the aircraft's influence ran through everything except its most visible feature.**

No forward-swept fighter has entered series production since, the [Su-47][ref_su47] having remained a
prototype, and the moderate forward sweep of some sailplanes and light aircraft serves visibility and spar
placement rather than high-speed performance \[[Forward-swept wing][ref_fsw]\]. The configuration's
aerodynamic case was modest, since the programme did not demonstrate the overall drag reduction that earlier
studies had suggested \[[Gelzer 2015][ref_gelzer_x29]\], its structural case depended on a technology that
had other uses, and advances in thrust vectoring and a shift toward medium-range missile engagements reduced
its relevance to fighter design \[[Forward-swept wing][ref_fsw]\]. **The planform lost.**

**What won was everything the planform forced.**

- **Aeroelastic tailoring became ordinary.** The technique that kept the X-29's wing inside its
  boundary is now applied to wings that are not forward-swept at all, for load alleviation,
  flutter margin and weight, and the design literature that supports it is large
  \[[Aeroelastic tailoring of transport aircraft wings][ref_tailoring]\].
- **Flying a deeply unstable airframe became ordinary.** Thirty-five percent negative static margin was
  extreme in 1984 and the practice of designing around relaxed static stability is now unremarkable
  \[[Relaxed stability][ref_relaxed_stability]\].
- **Real-time redundancy management became a recognised discipline.** The insight that failure
  detection and isolation must be fast compared with the airframe's divergence time, as well as
  reliable, transfers to every unstable aircraft.

**The aircraft's most transferable finding is the one it did not set out to make**, namely that a structure
and a control law for an unstable airframe cannot be specified independently. The canard's divergence
boundary being set by pitch-loop stiffness is a small fact with a large generalisation behind it.

Under The Contemporary Literature, the cluster on relaxed static stability and the unstable airframe carries this line of work forward.

## The Run of Four Purchased Designations Ends Here

**The pattern named across the last four articles stops with this one, and the stopping is itself evidence.**

- **[X-25][related_post_a322_bensen_x25]**, a civil autogyro design ordered in modified form to investigate a rescue concept.
- **[X-26][related_post_a323_schweizer_x26]**, a commercially available sailplane bought twice, for training and for quiet observation.
- **[X-27][related_post_a324_lockheed_x27]**, a manufacturer's private-venture export fighter that was never built at all.
- **[X-28][related_post_a325_osprey_x28]**, a homebuilt sport flying boat bought off a private individual for five thousand dollars.
- **X-29**, an aircraft designed and built to answer a question that could not be answered any other
  way.

**Three of the first four already existed and were bought for properties they already had. The X-27 never existed. The fifth had to be created.**

The X-series was established for aircraft like the X-29. A government agency identified a question, funded a
purpose-built aeroplane, built two of them, flew them for years, and published the result
\[[Gelzer 2015][ref_gelzer_x29]\].
**That the series could still do this in 1984, after a decade in which the designation had been applied to catalogue purchases and unbuilt proposals, is a fact about the institution, not the aircraft.**

**This article does not claim the four before it were misuse.** Evaluating an existing aircraft against a
requirement is research and it produced answers. The observation is narrower.
**The designation had become capable of meaning either thing, and which one it meant in a given year depended on who was paying rather than on any property of the aircraft.**
That observation joins the evidence the closing article of this series assembles, and it now has a run of four
followed by a clean break behind it.

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Flight control law design | 329 |
| Flutter, gusts and very flexible aircraft | 305 |
| Digital fly-by-wire, redundancy and fault tolerance | 274 |
| Composite structures, damage and certification | 263 |
| Aeroservoelasticity and structural mode control | 192 |
| Handling qualities and pilot-vehicle interaction | 176 |
| The X-29 and forward-swept wing aircraft | 175 |
| Transonic wing design and sweep | 153 |
| High angle of attack and vortex flow | 145 |
| Morphing and adaptive structures | 123 |
| Aerostructural and aerodynamic design optimisation | 118 |
| Flight test, instrumentation and identification | 107 |
| Aeroelastic tailoring and bend-twist coupling | 104 |
| Divergence and static aeroelasticity | 95 |
| Sampled-data control and time delay | 91 |
| Canards, trim and multiple lifting surfaces | 88 |
| Structural mechanics, buckling and structural weight | 83 |
| Machine learning and data-driven modelling | 81 |
| Lift, induced drag and aerodynamic estimation | 64 |
| Relaxed static stability and the unstable airframe | 62 |
| Structural health monitoring and the digital twin | 51 |
| Topology optimisation and additive manufacture | 41 |
| Uncertainty quantification and reliability | 35 |
| The Southwell method, Rayleigh-Ritz and assumed modes | 28 |
| Manoeuvre performance, agility and energy methods | 18 |
| **Total** | **3,201** |

The bodies of work in the sections before this one are the ones the argument sits inside.
**This section reviews what has happened since.** The table above counts the research records in each
cluster of the survey, the review subsections that follow read the literature against the aircraft, and the
clusters themselves close the section.

**The short version is that the X-29's two answers went in opposite directions. The planform is a historical curiosity and the techniques it forced are now everywhere.**

### Aeroelastic tailoring outlived the wing that needed it

**Tailoring is now a design variable rather than a rescue.** The X-29 used bend-twist coupling to cancel a
destabilising aerodynamic coupling, which is the hardest case. Contemporary work uses the same mechanism for
gust load alleviation, for flutter margin, for manoeuvre load control and for structural weight, on wings
whose sweep creates no divergence problem at all.

**The change is in the optimisation framing.** The X-29's laminate was designed to satisfy a constraint.
Modern practice treats ply orientation as a continuous design variable inside a multidisciplinary
optimisation, which makes the question not whether a coupling is achievable but what it is worth.

The cluster on aeroelastic tailoring and bend-twist coupling below gathers these records.

### Very flexible aircraft made the X-29's problem general

**The X-29 was a stiff aircraft with an inconvenient coupling. The contemporary problem is aircraft that are not stiff at all.**
High-aspect-ratio wings for efficiency, and the extreme case of solar-powered high-altitude platforms,
deform enough that the rigid-body and elastic degrees of freedom cannot be separated.

**That dissolves the distinction the X-29 was designed around.** Its static divergence analysis treated the
wing as elastic and the aircraft as rigid, although the programme also predicted and monitored body freedom
flutter, a coupling of the wing's first bending mode with the short-period mode that was expected to act as a
precursor to static divergence \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\]. The modern formulation abandons the
separation, and body freedom flutter, which appears in the nomenclature list of the X-29 reports, is the
canonical example.

Its records are in the cluster on flutter, gusts and very flexible aircraft below.

### Control of unstable airframes became a solved problem and then a harder one

**Nothing in the contemporary literature would regard a thirty-five percent negative static margin as remarkable**,
the clearest measure of what the programme settled. What has replaced it is the question of doing
the same thing with guarantees.

**The X-29's control law was gain-scheduled, a family of linear designs stitched together.**
Contemporary work asks for robustness certificates across the whole envelope, for adaptive laws that retain
stability proofs, and for control allocation across redundant surfaces of the kind the X-29 had three of.
**The X-29 has served as a benchmark for this work.** An adaptive augmentation study takes its lateral and
directional dynamics as the test case because they are difficult, in
[Griffin et al 2010][research_griffinbrianjoseph_burkenjohnj_2010], and procedures for optimising its handling
qualities and for closed-loop control of its forebody vortices appear in
[Bosworth and Cox 1989][research_bosworth_cox_1989] and [Valasek and Downing 1995][research_valasek_downing_1995].

The records for this subsection fall in three clusters below, on flight control law design, on digital fly-by-wire, redundancy and fault tolerance, and on relaxed static stability and the unstable airframe.

### Aeroservoelasticity became its own discipline

**The interaction the X-29 encountered in flight now has a name, a literature and a place in the design process.**
Structural modes inside the control bandwidth, notch filters that trade stability against delay, and the
fact that a delay bought to suppress a structural mode is a delay taken from an unstable airframe's budget.
**The X-29 met the first of them in flight**, when a canard pitch-mode response was aliased by the digital
sampling of the canard-position feedback loop \[[Kehoe et al 1990][research_kehoemichaelw_bjarkelisaj_1990]\].

The research records on this subject are gathered below in the cluster on aeroservoelasticity and structural mode control.

### High angle of attack aerodynamics

The second X-29A was devoted to high angle of attack work, and vortex flow control was tested on it
\[[Gelzer 2015][ref_gelzer_x29]\] \[[Hancock and Fullerton 1992][research_hancockregis_fullertongordon_1992]\].
**Contemporary work has moved from characterising the flow to controlling it**, with active flow control,
and the computational methods that were merely supporting evidence for the X-29 now carry the prediction.

See the cluster on high angle of attack and vortex flow below.

### Composite structures and how they are certified

**The X-29's wing skins were an early large primary composite structure on a research aircraft**, and the
record's remark that strain-gauge equation accuracies on composite were typical of experience with metal is
a small early data point in a large modern subject \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].

The certification literature is listed below in the cluster on composite structures, damage and certification.

### Transonic wing design is computed now

**The Grumman K Mod 2 section was developed for a design competition** \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\]. Its modern
equivalent is produced by optimisation against a computational model, and the shock position that the X-29's
planform argument was built around is now an output rather than an input.

Two clusters below hold this work, on transonic wing design and sweep and on aerostructural and aerodynamic design optimisation.

### Handling qualities of augmented aircraft

**The X-29's flying qualities were the flying qualities of its control law**, as is true of every modern
combat aircraft, and in 1984 the point was still novel enough to need saying. The equivalent-system criteria and the
treatment of control system time delay that the contemporary literature uses were being worked out in the
same decade \[[Bischoff 1983][research_bischoff_1983]\] \[[Berry et al 1982][research_berry_powers_1982]\].

The cluster on handling qualities and pilot-vehicle interaction, below, lists the records.

### Five Subjects That Were Not Fields in 1984

**The sections above track what happened to bodies of work the X-29 was part of.** The five that follow are
different. They are subjects that barely existed when the aircraft flew and that now bear directly on the
problems it was built to attack. They make up the more useful half of a survey.

### Machine learning arrived in the middle of the problem

**The X-29's predictions came from wind tunnels and computation, and the gaps between them and flight are documented in this article.**
\[[Waggoner et al 1986][research_waggonereg_jennettla_1986]\] \[[Waggoner and Bates 1989][research_waggonereg_batesbl_1989]\]
Contemporary practice inserts a learned model at those points, for unsteady aerodynamic prediction,
for reduced-order models of the flow, and for surrogate models that make an optimisation affordable.

**The relevant question is no longer whether these models are accurate but whether they can be trusted inside a control loop**.
The X-29's designers faced that question about their reduced-order models and answered it with a flight
envelope and a great deal of instrumentation.

Below, the cluster on machine learning and data-driven modelling collects this literature.

### Morphing structures are the tailoring idea carried further

**Aeroelastic tailoring changes a wing's response to load by fixing its internal geometry once.** Morphing
changes it while flying. The X-29's automatic camber control, which scheduled the flaperons as a function of
flight condition, is a coarse ancestor of this, and the reports' description of it as
**discrete variable camber** and as a low-cost alternative to smooth variable camber shows the designers
knew which approximation they were making \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\]
\[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].

Morphing research is gathered in the cluster on morphing and adaptive structures below.

### The structure now carries a model of itself

**The X-29A had 691 measured parameters and no onboard recording, so its divergence estimate could only be computed on the ground from telemetered data.**
\[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\]
The modern version of that arrangement keeps a structural model current against sensor data continuously,
under the names structural health monitoring, model updating and digital twin.

**The X-29's Southwell analysis is a small early instance of the same idea**, since it inferred a structural
property the aircraft could not be flown to from measurements taken well below it.

The cluster on structural health monitoring and the digital twin holds the corresponding records.

### Manufacture changed which shapes are affordable

**Every structural choice in the X-29 was constrained by what could be laid up, machined or fastened in 1982.**
Additive manufacture and topology optimisation together relax that constraint, and the literature on
designing for them rather than merely with them is substantial.

That literature appears below as the cluster on topology optimisation and additive manufacture.

### Uncertainty became something computed rather than covered

**Of the contemporary subjects, this one bears most directly on the X-29's keystone.**

The X-29 handled uncertainty in its divergence boundary the way its era did, with a margin. The margin was a
factor of 2.667 in dynamic pressure, the flight data then indicated the real boundary was lower than
predicted, and the margin absorbed the error \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].
**The margin was doing the work that a probability distribution does now.**

Contemporary practice computes a probabilistic flutter or divergence margin, propagates uncertainty in
stiffness and in the aerodynamic model through to the boundary, and states a confidence rather than a
factor. **Applied to this aircraft it would have answered the question the flight test could not**, namely
how much of the discrepancy between predicted and measured divergence speed was model error and how much was
measurement error.

Probabilistic margins and reliability methods make up the cluster on uncertainty quantification and reliability below.

### Flight control law design

Flight control law design for aircraft and unmanned vehicles, adaptive, robust and nonlinear, including dynamic inversion and envelope protection, together with the general control theory those laws rest on.

**329 records.** \[[A Generalization for Model Reference Adaptive Control and Robust Model Reference Adaptive Control Adaptive Laws for a Class of Nonlinear Uncertain Systems with Application to Control of Wing Rock Phenomenon 2020][research_a_generalization_2020]\] \[[Acquatella et al 2017][research_acquatellab_vanekeren_2017]\] \[[Advanced Control Techniques for Unmanned Aerial Vehicle (UAV) Navigation and Flight Control 2023][research_advanced_control_2023]\] \[[Aghababa 2018][research_aghababa_2018]\] \[[Aguilar-Ibañez 2016][research_aguilaribanez_2016]\] \[[Ahmadian et al 2025][research_ahmadian_alitalebi_2025]\] \[[Ahmed and Chen 2021][research_ahmed_chen_2021]\] \[[Ajel et al 2021][research_ajel_humaidi_2021]\] \[[Alag and Kaufman 1975][research_alag_kaufman_1975]\] \[[An et al 2020][research_an_guo_2020]\] \[[Autenrieb 2025][research_autenrieb_2025]\] \[[Autonomous flight control of drone equipped with microcomputer for flight control and GPS 2018][research_autonomous_flight_2018]\] \[[Axten et al 2024][research_axten_khamvilai_2024]\] \[[Balakrishnan 2000][research_balakrishnan_2000]\] \[[Banerjee 2019][research_banerjee_2019]\] \[[Banks 1988][research_banks_1988]\] \[[Bao et al 2025][research_bao_li_2025]\] \[[Bar-Shalom 1985][research_barshalom_1985]\] \[[Bar-Shalom 1989][research_barshalom_1989]\] \[[Bar-Shalom 1990][research_barshalom_1990]\] \[[Barabanov and Ortega 2017][research_barabanov_ortega_2017]\] \[[Bartoszewicz and Adamiak 2018][research_bartoszewicz_adamiak_2018]\] \[[Bastin et al 2025][research_bastin_coron_2025]\] \[[Basu Roy and Bhasin 2019][research_basuroy_bhasin_2019]\] \[[Benaddy et al 2022][research_benaddy_labbadi_2022]\] \[[Beppu et al 1966][research_beppu_curtiss_1966]\] \[[Bernstein 2000][research_bernstein_2000]\] \[[Bhatia et al 2021][research_bhatia_jiang_2021]\] \[[Biezad and Chou 1993][research_biezaddanielj_chouhweilan_1993]\] \[[Binz et al 2019][research_binz_islam_2019]\] \[[Bottasso and Montinari 2015][research_bottasso_montinari_2015]\] \[[Bouadi and Mora-Camino 2018][research_bouadi_moracamino_2018]\] \[[Bu et al 2025][research_bu_luo_2025]\] \[[Campbell and Terrell 1987][research_campbell_terrell_1987]\] \[[Cao et al 2017][research_cao_tang_2017]\] \[[Castañeda and Gordillo 2019][research_castaneda_gordillo_2019]\] \[[Center 1975][research_center_1975]\] \[[Chabir et al 2017][research_chabir_bouteraa_2017]\] \[[Chen and Holohan 2015][research_chen_holohan_2015]\] \[[Chen et al 2019][research_chen_wang_2019]\] \[[Chen et al 2025][research_chen_meng_2025]\] \[[Cheng et al 2017][research_cheng_wei_2017]\] \[[Cheng et al 2023][research_cheng_li_2023]\] \[[Choi and Choi 2026][research_choi_choi_2026]\] \[[Clark and LeTron 1989][research_clark_letron_1989]\] \[[Clements 2016][research_clementskeith_2016]\] \[[Cochran 2015][research_cochran_2015]\] \[[Combined flight control/utility system 1974][research_combined_flight_1974]\] \[[Coppin et al 2018][research_coppin_birch_2018]\] \[[Craig 1965][research_craig_1965]\] \[[Crandall et al 1973][research_crandall_maund_1973]\] \[[Cunis et al 2020][research_cunis_condomines_2020]\] \[[D'Andrea 2003][research_dandrea_2003]\] \[[D'Andrea 2008][research_dandrea_2008]\] \[[Davanipour et al 2017][research_davanipour_khayatian_2017]\] \[[De Gaspari and Mantegazza 2024][research_degaspari_mantegazza_2024]\] \[[Deng et al 2026][research_deng_xu_2026]\] \[[Devi 2019][research_devi_2019]\] \[[Dhiman et al 2022][research_dhiman_abhishek_2022]\] \[[Di Donato et al 2017][research_didonato_balachandran_2017]\] \[[Di Francesco and Mattei 2016][research_difrancesco_mattei_2016]\] \[[Di Rito and Schettini 2016][research_dirito_schettini_2016]\] \[[Ding et al 2025][research_ding_shi_2025]\] \[[Dong et al 2023][research_dong_li_2023]\] \[[Dukes 1970][research_dukes_1970]\] \[[Elenchezhiyan and Kumar 2025][research_elenchezhiyan_kumar_2025]\] \[[Enns 2003][research_enns_2003]\] \[[Evald et al 2023][research_evald_hollweg_2023]\] \[[Fan et al 2023][research_fan_wang_2023]\] \[[Fardad and Bamieh 2006][research_fardad_bamieh_2006]\] \[[Feliu‐Batlle 2016][research_feliubatlle_2016]\] \[[Feroskhan and Go 2016][research_feroskhan_go_2016]\] \[[Feroskhan and Go 2018][research_feroskhan_go_2018]\] \[[Ferreres and Hardier 2017][research_ferreres_hardier_2017]\] \[[Feuer et al 1977][research_feuer_barmish_1977]\] \[[Filimonov et al 2026][research_filimonov_filimonov_2026]\] \[[Fleming and Kushner 1994][research_fleming_kushner_1994]\] \[[Flight Sciences Lab Inc Buffalo Ny 1964][research_flightscienceslabincbuffalony_1964]\] \[[Flores et al 2025][research_flores_bazan_2025]\] \[[Franco et al 2022][research_franco_rios_2022]\] \[[Franklin 1993][research_franklinjamesa_1993]\] \[[Franklin et al 1990][research_franklinjamesa_stortzmichaelw_1990]\] \[[Fresconi et al 2014][research_fresconi_celmins_2014]\] \[[Furtat and Gushchin 2021][research_furtat_gushchin_2021]\] \[[Fuzzy logic for control of roll and moment for a flexible wing aircraft 1991][research_fuzzy_logic_1991]\] \[[Gabrys et al 2019][research_gabrys_steffensen_2019]\] \[[Gainer 1963][research_gainer_1963]\] \[[Galffy et al 2019][research_galffy_bock_2019]\] \[[Gamagedara et al 2024][research_gamagedara_lee_2024]\] \[[Gao et al 2025][research_gao_jiang_2025]\] \[[Garrard and Low 1990][research_garrard_low_1990]\] \[[Gibson 1999][research_gibson_1999]\] \[[Glezer and Leonard 2012][research_glezer_leonard_2012]\] \[[Goel and Roy 2021][research_goel_roy_2021]\] \[[Gong et al 2024][research_gong_xu_2024]\] \[[González et al 2020][research_gonzalez_silvestre_2020]\] \[[Govindaraj et al 1979][research_govindaraj_rynaski_1979]\] \[[Greenberg and Sternfield 1944][research_greenbergharry_sternfieldleonard_1944]\] \[[Gross et al 2017][research_gross_clark_2017]\] \[[Gruenwald et al 2020][research_gruenwald_yucelen_2020]\] \[[Guo et al 2020][research_guo_zhou_2020]\] \[[Guo et al 2026][research_guo_liu_2026_b]\] \[[Hai 2022][research_hai_2022]\] \[[Hallauer 1983][research_hallauer_jr_1983]\] \[[Hamissi et al 2019][research_hamissi_bouzid_2019]\] \[[Hart 1956][research_hart_1956]\] \[[Heersink et al 2022][research_heersink_sylla_2022]\] \[[Heinrich et al 2022][research_heinrich_vogt_2022]\] \[[Rediess 1976][research_hermanarediess_1976]\] \[[Hess and Peng 2018][research_hess_peng_2018]\] \[[Hobbs et al 2023][research_hobbs_mote_2023]\] \[[Hodgins and Freeman 2025][research_hodgins_freeman_2025]\] \[[Hodgkinson 2017][research_hodgkinson_2017]\] \[[Hongyan and Xiaoyong 2026][research_hongyan_xiaoyong_2026]\] \[[Horowitz et al 1980][research_horowitz_golubev_1980]\] \[[How 2004][research_how_2004]\] \[[Huang et al 2023][research_huang_zhen_2023]\] \[[Huo et al 2021][research_huo_duan_2021]\] \[[Invernizzi and Lovera 2018][research_invernizzi_lovera_2018]\] \[[Franklin 1993][research_jamesafranklin_1993]\] \[[Jeong et al 2024][research_jeong_suk_2024]\] \[[Ji et al 2024][research_ji_ke_2024]\] \[[Jia et al 2023][research_jia_sun_2023]\] \[[Jiang et al 2024][research_jiang_liu_2024]\] \[[Jianhong and Yanxiang 2026][research_jianhong_yanxiang_2026]\] \[[Jin et al 2015][research_jin_bifeng_2015]\] \[[Kai 2024][research_kai_2024]\] \[[Kamaletdinova and Romanov 2024][research_kamaletdinova_romanov_2024]\] \[[Kassapakis and Warwick 1994][research_kassapakis_warwick_1994]\] \[[Kazarin et al 2021][research_kazarin_golubev_2021]\] \[[Kevrekidis 2002][research_kevrekidis_2002]\] \[[Khalaf et al 2017][research_khalaf_gan_2017]\] \[[Khankalantary et al 2021][research_khankalantary_rezaeeahvanouee_2021]\] \[[Kim and Kim 2024][research_kim_kim_2024]\] \[[Kim et al 2016][research_kim_lee_2016]\] \[[Kim et al 2019][research_kim_oh_2019]\] \[[Klema 1981][research_klema_1981]\] \[[Konatala et al 2024][research_konatala_milz_2024]\] \[[Kopecki 2021][research_kopecki_2021]\] \[[Krause et al 1990][research_krause_khargonekar_1990]\] \[[L'Afflitto 2018][research_lafflitto_2018]\] \[[L'Afflitto 2023][research_lafflitto_2023]\] \[[L'Afflitto and Blackford 2018][research_lafflitto_blackford_2018]\] \[[Lang et al 2024][research_lang_li_2024]\] \[[Laub 1991][research_laub_1991]\] \[[Le 2026][research_le_2026]\] \[[Lee 1977][research_lee_1977]\] \[[Lee et al 2017][research_lee_snyder_2017]\] \[[Lepri et al 2024][research_lepri_bacciu_2024]\] \[[Li and Sanfelice 2016][research_li_sanfelice_2016]\] \[[Li et al 2021][research_li_liu_2021_b]\] \[[Li et al 2022][research_li_liu_2022]\] \[[Li et al 2024][research_li_he_2024]\] \[[Li et al 2025][research_li_li_2025]\] \[[Li et al 2026][research_li_shen_2026]\] \[[Li et al 2026][research_li_xu_2026]\] \[[Liang et al 2025][research_liang_ye_2025]\] \[[Lindsay and Jordan 1975][research_lindsay_jordan_1975]\] \[[Liu and Buss 2022][research_liu_buss_2022]\] \[[Liu et al 2016][research_liu_ye_2016]\] \[[Liu et al 2018][research_liu_an_2018]\] \[[Liu et al 2021][research_liu_dong_2021]\] \[[Liu et al 2023][research_liu_chen_2023]\] \[[Liu et al 2026][research_liu_li_2026]\] \[[Liu et al 2026][research_liu_yang_2026]\] \[[Lo 1978][research_lo_1978]\] \[[Lo 1979][research_lo_1979]\] \[[Lo 1980][research_lo_1980]\] \[[Lo 1981][research_lo_1981]\] \[[Long 2019][research_long_2019]\] \[[Lu et al 2015][research_lu_zhang_2015]\] \[[Lu et al 2022][research_lu_hong_2022]\] \[[Lu et al 2025][research_lu_cao_2025]\] \[[Ludeña Cervantes et al 2020][research_ludenacervantes_choi_2020]\] \[[Lungu and Lungu 2015][research_lungu_lungu_2015]\] \[[Luo et al 2022][research_luo_zhang_2022]\] \[[Ma and Chen 2023][research_ma_chen_2023]\] \[[Ma et al 2025][research_ma_liu_2025]\] \[[Mahmood 2025][research_mahmood_2025]\] \[[Maity et al 2019][research_maity_hocht_2019]\] \[[Marcus 1994][research_marcus_1994]\] \[[McAllister and Esfahani 2025][research_mcallister_esfahani_2025]\] \[[McEneaney 1999][research_mceneaney_1999]\] \[[McIntosh et al 2024][research_mcintosh_mishra_2024]\] \[[McKillip 1991][research_mckillip_1991]\] \[[Meng et al 2024][research_meng_fu_2024]\] \[[Miles and Broughton 2017][research_miles_broughton_2017]\] \[[Mirtaba et al 2022][research_mirtaba_jeddi_2022]\] \[[Mohseni and Bernstein 2024][research_mohseni_bernstein_2024]\] \[[Mojallizadeh 2026][research_mojallizadeh_2026]\] \[[Mukherjee and Halder 2017][research_mukherjee_halder_2017]\] \[[Mukherjee and Sinha 2017][research_mukherjee_sinha_2017]\] \[[Newkirk 1979][research_newkirk_1979]\] \[[Nguyen et al 2026][research_nguyen_prodan_2026]\] \[[Nield 1981][research_nield_iv_1981]\] \[[Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]\] \[[Okumoto and Elsanker 1973][research_okumoto_elsanker_1973]\] \[[Oland et al 2016][research_oland_andersen_2016]\] \[[Ostheimer and Giguere 1963][research_ostheimer_giguere_1963]\] \[[O’Donnell and Mohseni 2019][research_odonnell_mohseni_2019]\] \[[O’Rourke et al 2019][research_orourke_kolmanovsky_2019]\] \[[Palframan et al 2019][research_palframan_fry_2019]\] \[[Palkin and Zenchenko 2025][research_palkin_zenchenko_2025]\] \[[Pan and Huang 2019][research_pan_huang_2019]\] \[[Park and Oh 2017][research_park_oh_2017]\] \[[Park et al 2017][research_park_choi_2017]\] \[[Park et al 2017][research_park_jung_2017]\] \[[Park et al 2024][research_park_ramirezserrano_2024]\] \[[Park et al 2025][research_park_ramirezserrano_2025]\] \[[Patne et al 2020][research_patne_ingole_2020]\] \[[Pollack and van Kampen 2023][research_pollack_vankampen_2023]\] \[[Pollack et al 2026][research_pollack_theodoulis_2026]\] \[[Prajapati and Prasad 2019][research_prajapati_prasad_2019]\] \[[Qi and Zhao 2020][research_qi_zhao_2020]\] \[[Qi et al 2018][research_qi_zhao_2018]\] \[[Qu and Annaswamy 2016][research_qu_annaswamy_2016]\] \[[Radetskaya 2022][research_radetskaya_2022]\] \[[Rafi et al 2017][research_rafi_steck_2017]\] \[[Rahima et al 2026][research_rahima_yassine_2026]\] \[[Rath and Fichter 2020][research_rath_fichter_2020]\] \[[Refinement of aircraft dynamics model and control system according to the flight-tests results 2023][research_refinement_of_2023]\] \[[Regulator with reference model for u nmanned aircraft control when boarding on unmanned vehicle 2022][research_regulator_with_2022]\] \[[Ren et al 2022][research_ren_zhang_2022]\] \[[Rigatos 2021][research_rigatos_2021]\] \[[Robust Controller Design Based on L1 Adaptive Control Method 2016][research_robust_controller_2016]\] \[[Rogalski 2018][research_rogalski_2018]\] \[[Rogalski et al 2020][research_rogalski_rzucidlo_2020]\] \[[Rogalski et al 2021][research_rogalski_rzucidlo_2021]\] \[[Rokhsaz and Selberg 1990][research_rokhsaz_selberg_1990]\] \[[Ronfle-Nadaud 2009][research_ronflenadaud_2009]\] \[[Rong et al 2022][research_rong_huang_2022]\] \[[Rowley 2008][research_rowley_2008]\] \[[Rustenburg 1972][research_rustenburg_1972]\] \[[Sachan and Padhi 2020][research_sachan_padhi_2020]\] \[[Saetti 2025][research_saetti_2025_b]\] \[[Salagame et al 2025][research_salagame_pandya_2025]\] \[[Salahudden et al 2024][research_salahudden_agrawal_2024]\] \[[Sang and Zhang 2022][research_sang_zhang_2022]\] \[[Sato et al 2017][research_sato_muraoka_2017]\] \[[Saviolo and Loianno 2023][research_saviolo_loianno_2023]\] \[[Schieni et al 2024][research_schieni_modasiya_2024]\] \[[Schmeichel 1967][research_schmeichel_1967]\] \[[Schmidt and Schierman 1990][research_schmidtdavidk_schiermanjohnd_1990]\] \[[Schuet et al 2017][research_schuet_lombaerts_2017]\] \[[Schütte et al 2018][research_schutte_huber_2018]\] \[[Shen and Chen 2023][research_shen_chen_2023]\] \[[Shi et al 2022][research_shi_wang_2022]\] \[[Shi et al 2025][research_shi_gao_2025]\] \[[Shiota and Ohmori 2015][research_shiota_ohmori_2015]\] \[[Shtessel 2001][research_shtessel_2001]\] \[[Simon et al 2017][research_simon_harkegard_2017]\] \[[Sleptsov and Andrianova 2021][research_sleptsov_andrianova_2021]\] \[[Smith 1968][research_smith_1968]\] \[[Smith 1978][research_smith_1978]\] \[[Snyder et al 2019][research_snyder_zhao_2019]\] \[[Snyder et al 2022][research_snyder_zhao_2022]\] \[[Soltani et al 2025][research_soltani_turner_2025]\] \[[Song and Huang 2022][research_song_huang_2022]\] \[[Spillman and Ridgely 1995][research_spillman_ridgely_1995]\] \[[Stefanello and Gründling 2016][research_stefanello_grundling_2016]\] \[[Stefanovski 2022][research_stefanovski_2022]\] \[[Steinberg and Page 1998][research_steinberg_page_1998]\] \[[Stolarik 2007][research_stolarik_2007]\] \[[Subramanian et al 2022][research_subramanian_abdelsalam_2022]\] \[[Suikat et al 1987][research_suikatreiner_donaldsonkent_1987]\] \[[Sultan 2026][research_sultan_2026]\] \[[Sun and van Kampen 2021][research_sun_vankampen_2021]\] \[[Sushchenko and Bezkorovainyi 2023][research_sushchenko_bezkorovainyi_2023]\] \[[Taherinezhad and Ramirez-Serrano 2023][research_taherinezhad_ramirezserrano_2023]\] \[[Tamaskani et al 2026][research_tamaskani_alfi_2026]\] \[[Tanveer and Ahmad 2023][research_tanveer_ahmad_2023]\] \[[Tanyer et al 2016][research_tanyer_tatlicioglu_2016]\] \[[Tao 2025][research_tao_2025]\] \[[Tao et al 2016][research_tao_li_2016]\] \[[Thien and Kim 2018][research_thien_kim_2018]\] \[[Thu and Gavrilov 2017][research_thu_gavrilov_2017]\] \[[Tingting et al 2018][research_tingting_aijun_2018]\] \[[Tipàn et al 2020][research_tipan_theodoulis_2020]\] \[[Tran and Nguyen 2022][research_tran_nguyen_2022]\] \[[Trindade Nascimento and Cunha 2019][research_trindadenascimento_cunha_2019]\] \[[Tsubakino and Saito 2020][research_tsubakino_saito_2020]\] \[[Tu et al 2026][research_tu_lu_2026]\] \[[UAV control with active disturbance suppression for the safety landing on an aircraft carrier 2023][research_uav_control_2023]\] \[[Wang and Li 2025][research_wang_li_2025_c]\] \[[Wang et al 2015][research_wang_wu_2015]\] \[[Wang et al 2016][research_wang_xu_2016]\] \[[Wang et al 2017][research_wang_chu_2017]\] \[[Wang et al 2019][research_wang_vankampen_2019_b]\] \[[Wang et al 2020][research_wang_zhu_2020]\] \[[Wang et al 2021][research_wang_wen_2021]\] \[[Wang et al 2022][research_wang_zheng_2022]\] \[[Wang et al 2024][research_wang_liu_2024]\] \[[Wang et al 2024][research_wang_sun_2024]\] \[[Wang et al 2024][research_wang_zhou_2024]\] \[[Wang et al 2026][research_wang_liu_2026]\] \[[Wang et al 2026][research_wang_wei_2026]\] \[[Webb and Rogers 2021][research_webb_rogers_2021]\] \[[Wei et al 2020][research_wei_xu_2020]\] \[[Weidemann and Leondes 1979][research_weidemann_leondes_1979]\] \[[Weiser et al 2020][research_weiser_ossmann_2020]\] \[[Willsky 1984][research_willsky_1984]\] \[[Willsky and Verghese 1984][research_willsky_verghese_1984]\] \[[Willsky and Verghese 1985][research_willsky_verghese_1985]\] \[[Wise et al 1999][research_wise_sedwick_1999]\] \[[Wood et al 2019][research_wood_araujoestrada_2019]\] \[[Wu et al 2019][research_wu_li_2019]\] \[[Wu et al 2021][research_wu_zhang_2021]\] \[[Wu et al 2024][research_wu_ye_2024]\] \[[Xie and Zhao 2016][research_xie_zhao_2016]\] \[[Xiong et al 2025][research_xiong_xu_2025]\] \[[Xu et al 2015][research_xu_fan_2015]\] \[[Xue et al 2021][research_xue_yunsong_2021]\] \[[Yang et al 2018][research_yang_guan_2018]\] \[[Yeo et al 2015][research_yeo_atkins_2015]\] \[[Yu et al 2023][research_yu_zhang_2023]\] \[[Yuan and Li 2019][research_yuan_li_2019]\] \[[Yuan et al 2024][research_yuan_wang_2024]\] \[[Zhang and He 2026][research_zhang_he_2026]\] \[[Zhang and Ran 2023][research_zhang_ran_2023]\] \[[Zhang et al 2018][research_zhang_chen_2018]\] \[[Zhang et al 2018][research_zhang_devisser_2018]\] \[[Zhang et al 2019][research_zhang_devisser_2019]\] \[[Zhang et al 2020][research_zhang_sun_2020]\] \[[Zhang et al 2025][research_zhang_song_2025]\] \[[Zhou et al 2022][research_zhou_yang_2022]\] \[[Zhu et al 2017][research_zhu_du_2017]\] \[[Zvonarev and Leont’ev 2025][research_zvonarev_leontev_2025]\] \[[Çabuk 2026][research_cabuk_2026]\] \[[Калиновский 2016][research_anon_2016]\]

### Flutter, gusts and very flexible aircraft

Flutter analysis and testing, gust response, panel flutter and the aeroelasticity of very flexible and high-aspect-ratio wings, with bridge and hydrofoil flutter kept for their shared mechanics.

**305 records.** \[[Abbas and Morgenthal 2016][research_abbas_morgenthal_2016]\] \[[Abel et al 1966][research_abeli_ruhlincl_1966]\] \[[Abichandani and Rosenberg 1952][research_abichandani_rosenberg_1952]\] \[[Abou-Kebeh et al 2025][research_aboukebeh_gilpita_2025]\] \[[Alizadeh et al 2020][research_alizadeh_ebrahimi_2020]\] \[[An et al 2017][research_an_khoo_2017]\] \[[An et al 2026][research_an_zhang_2026]\] \[[Ang and Ng 2026][research_ang_ng_2026]\] \[[Ang et al 2024][research_ang_leo_2024]\] \[[Arnold 1942][research_arnold_1942]\] \[[Asgari and Kouchakzadeh 2016][research_asgari_kouchakzadeh_2016]\] \[[Badhurshah et al 2024][research_badhurshah_alvarez_2024]\] \[[Bai et al 2022][research_bai_xu_2022]\] \[[Balunov et al 2023][research_balunov_solyaev_2023]\] \[[Bartels and Stanford 2018][research_bartels_stanford_2018]\] \[[Bennett et al 1993][research_bennett_dansberry_1993]\] \[[Bennett et al 1988][research_bennettrobertm_batinajohnt_1988]\] \[[Bergen and Arnold 1940][research_bergen_arnold_1940]\] \[[Besch and Liu 1973][research_besch_liu_1973]\] \[[Besch et al 1976][research_besch_rood_1976]\] \[[Bismarck-Nasr 1994][research_bismarcknasr_1994]\] \[[Bolding and Stearman 1976][research_boldingrm_stearmanro_1976]\] \[[Bondarenko and Shkolnyi 2024][research_bondarenko_shkolnyi_2024]\] \[[Boyd 1977][research_boyd_1977]\] \[[Bras et al 2022][research_bras_warwick_2022]\] \[[Brouwer and McNamara 2020][research_brouwer_mcnamara_2020]\] \[[Busan 1998][research_busan_1998]\] \[[Byreddy et al 2003][research_byreddy_grandhi_2003]\] \[[Thinesh and Y Harmin 2018][research_c_yharmin_2018]\] \[[Camacho et al 2021][research_camacho_akhavan_2021]\] \[[Campagna et al 2025][research_campagna_benedetti_2025]\] \[[Candon et al 2026][research_candon_marzocca_2026]\] \[[Casey 1988][research_casey_1988]\] \[[Cavallaro et al 2015][research_cavallaro_bombardieri_2015]\] \[[Chajjed et al 2024][research_chajjed_khalil_2024]\] \[[Chakravarthy et al 2015][research_chakravarthy_evans_2015]\] \[[Changchuan et al 2018][research_changchuan_lan_2018]\] \[[Chen and Li 2017][research_chen_li_2017]\] \[[Chen et al 2017][research_chen_qiu_2017]\] \[[Chen et al 2018][research_chen_li_2018]\] \[[Chen et al 2019][research_chen_chen_2019]\] \[[Chen et al 2020][research_chen_gao_2020]\] \[[Chen et al 2025][research_chen_he_2025]\] \[[Chiarelli and Bonomo 2019][research_chiarelli_bonomo_2019]\] \[[Chowdary et al 1994][research_chowdary_parthan_1994]\] \[[Cid Montoya et al 2018][research_cidmontoya_hernandez_2018]\] \[[Cooper and Stroud 1972][research_cooperpa_stroudwj_1972]\] \[[Crimi and Grace 1965][research_crimi_grace_1965]\] \[[Crimi and Ordway 1962][research_crimi_ordway_1962]\] \[[Crittenden et al 1978][research_crittenden_weishaar_1978]\] \[[Crother et al 1973][research_crother_gabelman_1973]\] \[[Crouse and Leishman 1992][research_crouse_leishman_1992]\] \[[Cunningham et al 1988][research_cunningham_batina_1988]\] \[[Cunningham et al 1987][research_cunninghamherbertj_batinajohnt_1987]\] \[[Birdsall 1970][research_dlbirdsall_1970]\] \[[Dagilis and Kilikevičius 2023][research_dagilis_kilikevicius_2023]\] \[[Daniel de Almeida Pereira and Flávio Donizeti Marques 2015][research_danieldealmeidapereira_flaviodonizetimarques_2015]\] \[[del Carre and Palacios 2020][research_delcarre_palacios_2020]\] \[[Deskos et al 2020][research_deskos_delcarre_2020]\] \[[Dhital and Chouvion 2024][research_dhital_chouvion_2024]\] \[[Doggett et al 1995][research_doggettrobertvjr_riverajoseajr_1995]\] \[[Dowell and Hall 2003][research_dowell_hall_2003]\] \[[Duan and Zhang 2018][research_duan_zhang_2018]\] \[[Dugundji 1965][research_dugundji_1965]\] \[[Dugundji et al 1962][research_dugundji_dowell_1962]\] \[[Eastep and Olsen 1980][research_eastep_olsen_1980]\] \[[Ebrahimzade et al 2016][research_ebrahimzade_dardel_2016]\] \[[Eckhaus 1962][research_eckhaus_1962]\] \[[Fang et al 2020][research_fang_cao_2020]\] \[[Farbridge et al 1956][research_farbridge_woodward_1956]\] \[[Farhat 1998][research_farhat_1998]\] \[[Farhat 2000][research_farhat_2000]\] \[[Farhat 2001][research_farhat_2001]\] \[[Farmer and Hanson 1976][research_farmermg_hansonpw_1976]\] \[[Farsadi et al 2020][research_farsadi_rahmanian_2020]\] \[[Farsadi et al 2024][research_farsadi_ahmadi_2024]\] \[[Fazilati and Khalafi 2019][research_fazilati_khalafi_2019]\] \[[Fedorenko and Bondarenko 2024][research_fedorenko_bondarenko_2024]\] \[[Feldt and Herrmann 1974][research_feldt_herrmann_1974]\] \[[Flax 1943][research_flax_1943]\] \[[Freudinger 1989][research_freudingerlawrencec_1989]\] \[[Freudinger and Kehoe 1990][research_freudingerlawrencec_kehoemichaelw_1990]\] \[[Fu et al 2021][research_fu_yang_2021]\] \[[Garrick and Rubinow 1946][research_garrickie_rubinowsi_1946]\] \[[Garrick and Rubinow 1946][research_garrickie_rubinowsi_1946_b]\] \[[Ghalandari et al 2022][research_ghalandari_mahariq_2022]\] \[[Ghasemikaram et al 2021][research_ghasemikaram_mazidi_2021]\] \[[Goizueta et al 2022][research_goizueta_wynn_2022_b]\] \[[Goland 1945][research_goland_1945]\] \[[Grauer and Boucher 2017][research_grauerjareda_bouchermatthewj_2017]\] \[[Gray and Mei 1993][research_gray_mei_1993]\] \[[Gray et al 2023][research_gray_riso_2023]\] \[[Greene 1928][research_greene_1928]\] \[[Grifò et al 2023][research_grifo_gulizzi_2023]\] \[[Gu and Zhou 2020][research_gu_zhou_2020]\] \[[Gu and Zhou 2022][research_gu_zhou_2022]\] \[[Guimarães et al 2019][research_guimaraes_castro_2019]\] \[[Guimarães et al 2020][research_guimaraes_silva_2020]\] \[[Guo et al 2017][research_guo_jing_2017]\] \[[Gurley and Ruhlin 1962][research_gurleyjrjr_ruhlincl_1962]\] \[[Guruswamy et al 1987][research_guruswamy_goorjian_1987]\] \[[Haas and Chopra 1990][research_haas_chopra_1990]\] \[[Hao et al 2022][research_hao_du_2022]\] \[[Hao et al 2023][research_hao_ma_2023]\] \[[Hao et al 2026][research_hao_yu_2026]\] \[[Henry 1961][research_henry_1961]\] \[[Hermanutz and Hornung 2020][research_hermanutz_hornung_2020]\] \[[Herrmann et al 1966][research_herrmanng_nematnassers_1966]\] \[[Hilger and Ritter 2021][research_hilger_ritter_2021]\] \[[Hitch 1978][research_hitch_1978]\] \[[Hodges 2004][research_hodges_2004]\] \[[Hoseini and Hodges 2019][research_hoseini_hodges_2019]\] \[[Housner and Stein 1974][research_housnerjm_steinm_1974]\] \[[Huang et al 2018][research_huang_yang_2018]\] \[[Huang et al 2024][research_huang_zheng_2024]\] \[[Iannelli et al 2017][research_iannelli_marcos_2017]\] \[[Iannelli et al 2018][research_iannelli_marcos_2018]\] \[[Iovnovich et al 2018][research_iovnovich_nahom_2018]\] \[[Isogai 1979][research_isogai_1979]\] \[[Isogai 1981][research_isogai_1981]\] \[[Ji et al 2021][research_ji_zhao_2021]\] \[[Ji et al 2024][research_ji_guo_2024]\] \[[Jianhong 2022][research_jianhong_2022]\] \[[Jonsson et al 2019][research_jonsson_riso_2019]\] \[[Jonsson et al 2023][research_jonsson_riso_2023]\] \[[Juhasz et al 2023][research_juhasz_tischler_2023]\] \[[Kapania and Issac 1994][research_kapania_issac_1994]\] \[[Kapania et al 1991][research_kapania_bergen_1991]\] \[[Karpouzian 1991][research_karpouzian_1991]\] \[[Kearns 1962][research_kearns_1962]\] \[[Kehoe 1984][research_kehoemw_1984]\] \[[Kehoe and Ellison 1985][research_kehoemw_ellisonjf_1985]\] \[[Kehoe 1987][research_kehoemichaelw_1987]\] \[[Khajah and Natarajan 2023][research_khajah_natarajan_2023]\] \[[Khalil et al 2016][research_khalil_poirel_2016]\] \[[Kheiri and Riazat 2025][research_kheiri_riazat_2025]\] \[[Kholodar 2023][research_kholodar_2023]\] \[[Kilimtzidis and Kostopoulos 2023][research_kilimtzidis_kostopoulos_2023_b]\] \[[Kim 2016][research_kim_2016]\] \[[Klyde et al 2004][research_klyde_harris_2004]\] \[[Kolar and Lile 1971][research_kolar_lile_1971]\] \[[Kousen and Bendiksen 1994][research_kousen_bendiksen_1994]\] \[[Kretov and Tiniakov 2022][research_kretov_tiniakov_2022]\] \[[Krzywoblocki 1943][research_krzywoblocki_1943]\] \[[Kumar et al 2019][research_kumar_onkar_2019]\] \[[Kuo-Jiun et al 1989][research_kuojiun_pongjeu_1989]\] \[[Kusni et al 2021][research_kusni_widiramdhani_2021]\] \[[Lee and Cho 1991][research_lee_cho_1991]\] \[[Lee and Cho 1991][research_lee_cho_1991_b]\] \[[Lehman and Stearman 1977][research_lehman_stearman_1977]\] \[[Lei et al 2021][research_lei_guo_2021]\] \[[Lemley 1968][research_lemley_1968]\] \[[Lesoinne 2007][research_lesoinne_2007]\] \[[Li and Pak 2015][research_li_pak_2015]\] \[[Li and Zhou 2024][research_li_zhou_2024]\] \[[Li et al 2018][research_li_huang_2018]\] \[[Liao and Sun 1993][research_liao_sun_1993]\] \[[Lin et al 1989][research_lin_lu_1989]\] \[[Lind et al 1997][research_lindrickc_brennermartinj_1997]\] \[[Liu and Gao 2020][research_liu_gao_2020_b]\] \[[Lottati 1987][research_lottati_1987]\] \[[Lu and Murthy 1990][research_lu_murthy_1990]\] \[[Lunghitano et al 2024][research_lunghitano_afonso_2024]\] \[[Maewal 1984][research_maewal_1984]\] \[[Mahapatra and Halbe 2024][research_mahapatra_halbe_2024]\] \[[Mallik et al 2015][research_mallik_kapania_2015]\] \[[Mannini and Bartoli 2015][research_mannini_bartoli_2015]\] \[[Mardanpour et al 2018][research_mardanpour_izadpanahi_2018]\] \[[Marqui et al 2017][research_marqui_bueno_2017]\] \[[Martini et al 2022][research_martini_innocenti_2022]\] \[[Miele 1976][research_miele_1976]\] \[[Modaress-Aval et al 2019][research_modaressaval_bakhtiarinejad_2019]\] \[[Mottershead and Cooper 2012][research_mottershead_cooper_2012]\] \[[Murphy et al 1976][research_murphy_peloubet_1976]\] \[[Nagaraja et al 1981][research_nagaraja_lakin_1981]\] \[[Nagaraja et al 1982][research_nagaraja_lakin_1982]\] \[[Naresh and Srinivas 2024][research_naresh_srinivas_2024]\] \[[Ni et al 2023][research_ni_li_2023]\] \[[Nibbelink and Peters 1993][research_nibbelinkbruced_petersdavida_1993]\] \[[Niblett 1988][research_niblett_1988]\] \[[Nitschke et al 2019][research_nitschke_vincenti_2019]\] \[[Ohkuma 1993][research_ohkuma_1993]\] \[[Olsen 1965][research_olsen_1965]\] \[[Onkar et al 2024][research_onkar_kumar_2024]\] \[[Otsuka and Makihara 2017][research_otsuka_makihara_2017]\] \[[Pan and Cheng 1995][research_pan_cheng_1995]\] \[[Pan and Liu 2019][research_pan_liu_2019]\] \[[Pendleton et al 1995][research_pendleton_moster_1995]\] \[[Pengelley and Wilson 1954][research_pengelley_wilson_1954]\] \[[Perkins and Brice 1966][research_perkins_brice_1966]\] \[[Perry 2025][research_perry_2025]\] \[[Persoon et al 1984][research_persoon_horsten_1984]\] \[[Petre and Ashley 1976][research_petre_ashley_1976]\] \[[Pidaparti 1993][research_pidaparti_1993]\] \[[Pidaparti and Yang 1993][research_pidaparti_yang_1993]\] \[[Pizzoli et al 2022][research_pizzoli_saltari_2022]\] \[[Prasad et al 1967][research_prasad_nematnasser_1967]\] \[[Price and Lee 1993][research_price_lee_1993]\] \[[Pushtaev 1989][research_pushtaev_1989]\] \[[Qi et al 2026][research_qi_yuan_2026]\] \[[Rao 1975][research_rao_1975]\] \[[Reding and Ericsson 1977][research_reding_ericsson_1977]\] \[[Rehman 2022][research_rehman_2022]\] \[[Richards et al 2016][research_richards_yao_2016]\] \[[Riso and Cesnik 2023][research_riso_cesnik_2023]\] \[[Rizzetta 1977][research_rizzetta_1977]\] \[[Rizzetta 1979][research_rizzetta_1979]\] \[[Rogers 1970][research_rogers_1970]\] \[[Rogólski and Olejnik 2018][research_rogolski_olejnik_2018]\] \[[Roizner et al 2019][research_roizner_raveh_2019]\] \[[Ruhlin et al 1982][research_ruhlin_watson_1982]\] \[[Ruhlin et al 1983][research_ruhlin_rauch_1983]\] \[[Ruhlin et al 1983][research_ruhlin_watson_1983]\] \[[Runyan et al 1952][research_runyan_cunningham_1952]\] \[[Rutkowski 1979][research_rutkowski_1979]\] \[[Saputra and Purabaya 2018][research_saputra_purabaya_2018]\] \[[Sawyer 1976][research_sawyerjw_1976]\] \[[Schewe and Mai 2018][research_schewe_mai_2018]\] \[[Schmidt 2016][research_schmidt_2016_b]\] \[[Schuster 1995][research_schuster_1995]\] \[[Schwanz 1972][research_schwanz_1972]\] \[[Schäfer et al 2018][research_schafer_vidy_2018]\] \[[Seidel et al 1989][research_seidel_eckstrom_1989]\] \[[Shi et al 2020][research_shi_liu_2020]\] \[[Shi et al 2021][research_shi_liu_2021]\] \[[Shiau and Chang 1991][research_shiau_chang_1991]\] \[[Shrivastava et al 2020][research_shrivastava_tilala_2020]\] \[[Shukla and Patil 2017][research_shukla_patil_2017]\] \[[Silva and Bennett 1990][research_silvawaltera_bennettrobertm_1990]\] \[[Smith 2025][research_smith_2025]\] \[[Sodja et al 2021][research_sodja_werter_2021]\] \[[Sohst et al 2022][research_sohst_lobodovale_2022]\] \[[Soleymani and Arani 2019][research_soleymani_arani_2019]\] \[[Song et al 2016][research_song_zhang_2016]\] \[[Steger and Bailey 1980][research_steger_bailey_1980]\] \[[Stegmüller et al 2026][research_stegmuller_haybock_2026]\] \[[Striz 1991][research_striz_1991]\] \[[Swaim 1961][research_swaim_1961]\] \[[Swaim and Yen 1979][research_swaim_yen_1979]\] \[[Swain et al 2019][research_swain_adhikari_2019]\] \[[Tang et al 2015][research_tang_wu_2015]\] \[[Tang et al 2017][research_tang_wu_2017]\] \[[Teixeira and Cesnik 2020][research_teixeira_cesnik_2020]\] \[[Tian et al 2019][research_tian_li_2019]\] \[[Tian et al 2026][research_tian_li_2026]\] \[[Tian et al 2026][research_tian_wang_2026]\] \[[Tijdeman et al 1979][research_tijdeman_vannunen_1979]\] \[[Tijdeman et al 1979][research_tijdeman_vannunen_1979_b]\] \[[Triplett et al 1971][research_triplett_burkhart_1971]\] \[[Tsatsas et al 2022][research_tsatsas_pontillo_2022]\] \[[Tsunematsu and Donadon 2019][research_tsunematsu_donadon_2019]\] \[[Turner 1982][research_turner_1982]\] \[[Turner 1982][research_turner_1982_b]\] \[[Veley et al 2008][research_veley_khot_2008]\] \[[Verma et al 2024][research_verma_cidmontoya_2024]\] \[[Verma et al 2025][research_verma_cidmontoya_2025]\] \[[Wahler et al 2025][research_wahler_ma_2025]\] \[[Wang 2024][research_wang_2024_b]\] \[[Wang et al 2016][research_wang_zhu_2016]\] \[[Wang et al 2021][research_wang_chen_2021]\] \[[Wang et al 2021][research_wang_wu_2021]\] \[[Wang et al 2022][research_wang_zhao_2022]\] \[[Wang et al 2024][research_wang_song_2024]\] \[[Wang et al 2025][research_wang_liuxu_2025]\] \[[Wang et al 2026][research_wang_hu_2026]\] \[[Weatherill and Zartarian 1958][research_weatherill_zartarian_1958]\] \[[Werdes 1953][research_werdes_1953]\] \[[Westin et al 2023][research_westin_balthazar_2023]\] \[[White et al 1961][research_white_richardp_1961]\] \[[Woods et al 1990][research_woods_gilbert_1990]\] \[[Woods et al 1989][research_woodsjessicaa_gilbertmichaelg_1989]\] \[[Wu and Livne 2017][research_wu_livne_2017]\] \[[Wu et al 2025][research_wu_wang_2025]\] \[[Wunderlich et al 2022][research_wunderlich_dahne_2022]\] \[[Xie et al 2016][research_xie_liu_2016]\] \[[Xu et al 2015][research_xu_gao_2015]\] \[[Yagil et al 2018][research_yagil_raveh_2018]\] \[[Yamasaki and Epureanu 2017][research_yamasaki_epureanu_2017]\] \[[Yang and Wan 1978][research_yang_wan_1978]\] \[[Yang and Zhao 1989][research_yang_zhao_1989]\] \[[Yang and Zhao 1992][research_yang_zhao_1992]\] \[[Yang et al 1980][research_yang_guruswamy_1980]\] \[[Yang et al 1981][research_yang_striz_1981]\] \[[Yang et al 2016][research_yang_yue_2016]\] \[[Yang et al 2019][research_yang_xie_2019]\] \[[Yates 1966][research_yates_1966]\] \[[Yates et al 1982][research_yates_wynne_1982]\] \[[Yates et al 1983][research_yates_wynne_1983]\] \[[Yates et al 1981][research_yatesecjr_wynneec_1981]\] \[[Yates and Chu 1987][research_yatesecarsonjr_chulichuan_1987]\] \[[Ye et al 2024][research_ye_yang_2024]\] \[[Yuan et al 2018][research_yuan_huo_2018]\] \[[Zhang et al 2015][research_zhang_wang_2015]\] \[[Zhang et al 2019][research_zhang_zhao_2019]\] \[[Zhao et al 2023][research_zhao_yang_2023]\] \[[Zhao et al 2026][research_zhao_liu_2026]\] \[[Zhong et al 2025][research_zhong_ying_2025]\] \[[Zhou and Huang 2021][research_zhou_huang_2021_b]\] \[[Zhou et al 2019][research_zhou_xu_2019]\] \[[Zhou et al 2025][research_zhou_raze_2025]\] \[[Zhuang et al 2021][research_zhuang_yang_2021]\] \[[Zong et al 2021][research_zong_sun_2021]\] \[[Zou et al 2024][research_zou_huang_2024]\] \[[Zou et al 2025][research_zou_huang_2025]\] \[[Zou et al 2025][research_zou_huang_2025_b]\]

### Digital fly-by-wire, redundancy and fault tolerance

Digital fly-by-wire flight control systems, redundancy management, fault detection, fault-tolerant control and control allocation.

**274 records.** \[[214 Application of restructurable flight control system to an airliner 1994][research_214_application_1994]\] \[[Abdul Huq and Beebi M 2015][research_abdulhuq_beebim_2015]\] \[[Abdul Rashid et al 2025][research_abdulrashid_syedmohddardin_2025]\] \[[Ackerman et al 2017][research_ackerman_xargay_2017]\] \[[AHarrah 2007][research_aharrahralphc_2007]\] \[[Ahmadi Dastgerdi et al 2022][research_ahmadidastgerdi_asadi_2022]\] \[[Akbari et al 2025][research_akbari_galeani_2025]\] \[[Aker and Alukonis 1976][research_aker_alukonis_1976]\] \[[Ale Isaac et al 2023][research_aleisaac_ragab_2023]\] \[[Ali et al 2026][research_ali_chen_2026]\] \[[Anderson 1976][research_andersonca_1976]\] \[[Anikin et al 2015][research_anikin_animitsa_2015]\] \[[Antonakis and Biannic 2024][research_antonakis_biannic_2024]\] \[[Application Analysis on Fly-by-Wire Flight Control System on Large Transport Aircraft 2022][research_application_analysis_2022]\] \[[Argha et al 2018][research_argha_su_2018]\] \[[Argha et al 2019][research_argha_su_2019]\] \[[Atmaca et al 2025][research_atmaca_devisser_2025]\] \[[Bai 2018][research_bai_2018]\] \[[Bazhenov and Lysenkova 2015][research_bazhenov_lysenkova_2015]\] \[[Belmont 1983][research_belmont_1983]\] \[[Bessa et al 2020][research_bessa_puig_2020]\] \[[Bessadi et al 2016][research_bessadi_saussie_2016]\] \[[Bian et al 2018][research_bian_nener_2018]\] \[[Bian et al 2019][research_bian_nener_2019]\] \[[Binz and Moormann 2020][research_binz_moormann_2020]\] \[[Boby et al 2019][research_boby_abdullah_2019]\] \[[Bodson 2000][research_bodson_2000]\] \[[Bosch and Kuehl 1976][research_boschja_kuehlwj_1976]\] \[[Bouras 2020][research_bouras_2020]\] \[[Brock and Goodman 1981][research_brockld_goodmanha_1981]\] \[[Brodecki and Subbarao 2015][research_brodecki_subbarao_2015]\] \[[Brown and Szalai 1977][research_brownsr_szalaikj_1977]\] \[[Buffington 1997][research_buffington_1997]\] \[[Buffington 1999][research_buffington_1999_b]\] \[[Bullock and Fields 1998][research_bullock_fields_1998]\] \[[Burken 2007][research_burkenjohnj_2007]\] \[[Burns 1975][research_burns_1975]\] \[[Cano and Sobel 2016][research_cano_sobel_2016]\] \[[Cao and Liu 2025][research_cao_liu_2025_b]\] \[[Cao et al 2020][research_cao_jia_2020]\] \[[Chakravarty and Mahanta 2015][research_chakravarty_mahanta_2015]\] \[[Chang et al 2022][research_chang_debreuker_2022]\] \[[Chang et al 2022][research_chang_guo_2022]\] \[[Chen et al 2018][research_chen_edwards_2018]\] \[[Chen et al 2018][research_chen_niu_2018]\] \[[Chen et al 2020][research_chen_edwards_2020]\] \[[Chen et al 2020][research_chen_jing_2020]\] \[[Chen et al 2026][research_chen_cai_2026]\] \[[Choi 2016][research_choi_2016]\] \[[Clews 1973][research_clews_1973]\] \[[Comer and Chakraborty 2024][research_comer_chakraborty_2024]\] \[[Concorde Automatic Flight Control System 1971][research_concorde_automatic_1971]\] \[[Cong et al 2023][research_cong_hu_2023]\] \[[Cordeiro et al 2024][research_cordeiro_azinheira_2024]\] \[[Corliss and Talbot 1977][research_corlissld_talbotpd_1977]\] \[[Cotton 1974][research_cotton_1974]\] \[[Cui et al 2016][research_cui_yang_2016]\] \[[Cully and Boller 1973][research_cully_boller_1973]\] \[[Dagal 2026][research_dagal_2026]\] \[[Davis et al 1977][research_davis_garnett_1977]\] \[[Deets 1975][research_deetsda_1975]\] \[[Demarchi and Haning 1978][research_demarchi_haning_1978]\] \[[Demir and Seyfullah Babaarslan 2021][research_demir_seyfullahbabaarslan_2021]\] \[[Deng et al 2024][research_deng_stoica_2024]\] \[[Description and Flight Test 1975][research_description_and_1975]\] \[[Dhadekar et al 2021][research_dhadekar_misra_2021]\] \[[Dlamini and Jones 2016][research_dlamini_jones_2016]\] \[[Dobos-Bubno and Hartsook 1977][research_dobosbubno_hartsook_1977]\] \[[Dong et al 2016][research_dong_lu_2016]\] \[[Dong et al 2025][research_dong_zhou_2025]\] \[[Drtil and Schulz 1978][research_drtil_schulz_1978]\] \[[Duan and Okwudire 2019][research_duan_okwudire_2019]\] \[[Dunn et al 1986][research_dunnwr_cottrelld_1986]\] \[[Ebner and Mark 1977][research_ebnerre_markjg_1977]\] \[[El-Mahdy et al 2025][research_elmahdy_ali_2025]\] \[[Fadel et al 2019][research_fadel_rabie_2019]\] \[[Fearnside 1962][research_fearnside_1962]\] \[[Feng et al 2021][research_feng_wang_2021]\] \[[Garcia-Hernandez et al 2017][research_garciahernandez_cuernorejado_2017]\] \[[Garmendia and Mavris 2016][research_garmendia_mavris_2016]\] \[[Gaurav et al 2023][research_gaurav_sekou_2023]\] \[[Gavra and van Kampen 2024][research_gavra_vankampen_2024]\] \[[Gill 1995][research_gill_1995]\] \[[Govoni and Cristofaro 2023][research_govoni_cristofaro_2023]\] \[[Guo 2021][research_guo_2021]\] \[[Hammer and Bright 1998][research_hammer_bright_1998]\] \[[Han and Pei 2026][research_han_pei_2026]\] \[[He et al 2020][research_he_tan_2020]\] \[[Henschel and Chetty 1989][research_henschel_chetty_1989]\] \[[Herrmann and Ben-Asher 2016][research_herrmann_benasher_2016]\] \[[Hill 1987][research_hill_1987]\] \[[Hogan and Rinde 1978][research_hogan_rinde_1978]\] \[[Hübener and Luckner 2026][research_hubener_luckner_2026]\] \[[Ijaz et al 2019][research_ijaz_hamayun_2019]\] \[[Ijaz et al 2019][research_ijaz_hamayun_2019_b]\] \[[Immersion and Invariance Adaptive Fault-Tolerant Attitude Control for a Coaxial Tilt-Rotor eVTOL Aircraft 2026][research_immersion_and_2026]\] \[[İnan and Aliskan 2025][research_inan_aliskan_2025]\] \[[Elliott 1977][research_jelliott_1977]\] \[[Elliott 1976][research_jarrellrelliott_1976]\] \[[Jarvis 1975][research_jarviscr_1975]\] \[[Jarvis and Szalai 1981][research_jarviscr_szalaikj_1981]\] \[[Jenney and Schreadley 1984][research_jenney_schreadley_1984]\] \[[Jenney et al 1982][research_jenney_schreadley_1982]\] \[[Ji et al 2023][research_ji_kim_2023]\] \[[Jiao and Jiang 2015][research_jiao_jiang_2015]\] \[[Johnson 1965][research_johnson_1965]\] \[[Armah 2018][research_karmah_2018]\] \[[Nagarathna and Deodhare 2023][research_k_deodhare_2023]\] \[[Kaczmarek 2026][research_kaczmarek_2026]\] \[[Kang et al 2016][research_kang_park_2016]\] \[[Kim and Choi 2015][research_kim_choi_2015]\] \[[Kim et al 2017][research_kim_sung_2017]\] \[[Kineyko 1982][research_kineyko_1982]\] \[[Kisslinger and Wendl 1971][research_kisslinger_wendl_1971]\] \[[Kizildeniz and Kiyak 2025][research_kizildeniz_kiyak_2025]\] \[[Knox-Seith 1963][research_knoxseith_1963]\] \[[Ko et al 2019][research_ko_kang_2019]\] \[[Kohnhorst and Magnacca 1980][research_kohnhorst_magnacca_1980]\] \[[Komnatska and Bondarenko 2017][research_komnatska_bondarenko_2017]\] \[[Konar et al 1974][research_konar_mahesh_1974]\] \[[Kopecki 2016][research_kopecki_2016]\] \[[Kosyanchuk et al 2015][research_kosyanchuk_selvesyuk_2015]\] \[[Kosyanchuk et al 2021][research_kosyanchuk_zheltov_2021]\] \[[Kotitschke et al 2026][research_kotitschke_rupprecht_2026]\] \[[Krachmalnick et al 1968][research_krachmalnick_vetsch_1968]\] \[[Kubica et al 1995][research_kubica_livet_1995]\] \[[Kuvshinov 2016][research_kuvshinov_2016]\] \[[Kuvshinov 2016][research_kuvshinov_2016_b]\] \[[Kuvshinov and Leontiev 2019][research_kuvshinov_leontiev_2019]\] \[[Larson 1987][research_larsonrichardr_1987]\] \[[Li and Shi 2021][research_li_shi_2021]\] \[[Li et al 2018][research_li_dong_2018]\] \[[Li et al 2021][research_li_liu_2021]\] \[[Li et al 2023][research_li_liu_2023]\] \[[Li et al 2025][research_li_lin_2025]\] \[[Li et al 2025][research_li_shi_2025]\] \[[Li et al 2025][research_li_xiong_2025]\] \[[Lian and Cao 2026][research_lian_cao_2026]\] \[[Liang et al 2024][research_liang_gao_2024]\] \[[Liu and Tian 2019][research_liu_tian_2019]\] \[[Liu et al 2023][research_liu_zhou_2023]\] \[[Lock et al 1975][research_lockwp_petersenwr_1975]\] \[[Lu et al 2016][research_lu_vankampen_2016]\] \[[Lu et al 2019][research_lu_ma_2019]\] \[[Lucarini et al 2025][research_lucarini_dirito_2025]\] \[[Ma et al 2019][research_ma_dong_2019]\] \[[Mackall and Allen 1989][research_mackalldalea_allenjamesg_1989]\] \[[Mackall and Allen 1991][research_mackalldalea_allenjamesg_1991]\] \[[Mahulkar 2010][research_mahulkar_2010]\] \[[Malcom and Husband 1976][research_malcomlg_husbandjh_1976]\] \[[Mammadov and Hajiyev 2018][research_mammadov_hajiyev_2018]\] \[[Mant 1972][research_mant_1972]\] \[[Martínez-Heredia et al 2026][research_martinezheredia_fernandezprada_2026]\] \[[Matsuki et al 2018][research_matsuki_nishiyama_2018]\] \[[McGough et al 1974][research_mcgough_moses_1974]\] \[[McMaster and Schenk 1974][research_mcmaster_schenk_1974]\] \[[Mhenni et al 2016][research_mhenni_choley_2016]\] \[[Milz et al 2026][research_milz_may_2026]\] \[[Mohamed and G 2020][research_mohamed_g_2020]\] \[[Mohammadi et al 2025][research_mohammadi_ebrahimi_2025]\] \[[Montgomery and Caglayan 1976][research_montgomery_caglayan_1976]\] \[[Montgomery and Price 1976][research_montgomery_price_1976]\] \[[Montgomery and Price 1974][research_montgomeryrc_pricedb_1974]\] \[[Moreira et al 2022][research_moreira_gripp_2022]\] \[[Morozov and Chermoshentsev 2019][research_morozov_chermoshentsev_2019]\] \[[Morozov and Janschek 2016][research_morozov_janschek_2016]\] \[[Myers and Walsh 1991][research_myers_walsh_1991]\] \[[Napolitano 2002][research_napolitano_2002]\] \[[Nazari et al 2017][research_nazari_seron_2017]\] \[[Nguyen et al 2016][research_nguyen_olaru_2016]\] \[[Nguyen et al 2025][research_nguyen_han_2025]\] \[[Niu et al 2018][research_niu_chen_2018]\] \[[Noordin et al 2023][research_noordin_mohdbasri_2023]\] \[[Ochi and Kanai 1995][research_ochi_kanai_1995]\] \[[Ogunvoul et al 2017][research_ogunvoul_balanchuk_2017]\] \[[Om et al 2020][research_om_park_2020]\] \[[Osder et al 1976][research_osder_mossman_1976]\] \[[Ossmann and Joos 2016][research_ossmann_joos_2016]\] \[[Ossmann and Joos 2017][research_ossmann_joos_2017]\] \[[Ouyang and Lin 2017][research_ouyang_lin_2017]\] \[[Packard et al 2009][research_packard_seiler_2009]\] \[[Passenbrunner et al 2016][research_passenbrunner_sassano_2016]\] \[[Pendem 2023][research_pendem_2023]\] \[[Peng et al 2026][research_peng_li_2026]\] \[[Pfeifle and Fichter 2023][research_pfeifle_fichter_2023]\] \[[Pollack et al 2024][research_pollack_theodoulis_2024]\] \[[Posingies 1979][research_posingies_1979]\] \[[Prototype Digital Flight Control Computer 1986][research_prototype_digital_1986]\] \[[Pérez et al 2022][research_perez_theodoulis_2022]\] \[[Qian et al 2025][research_qian_xinhui_2025]\] \[[Qin et al 2023][research_qin_liu_2023]\] \[[Ren et al 2025][research_ren_xu_2025]\] \[[Research and Design of Automatic Flight Control System Test System 2022][research_research_and_2022]\] \[[Review of Fault-tolerant Control for Flight Control System 2024][research_review_of_2024]\] \[[Rickard 1978][research_rickardww_1978]\] \[[Robbins et al 2023][research_robbins_stansbury_2023]\] \[[Saetti 2025][research_saetti_2025]\] \[[Savelev and Neretin 2022][research_savelev_neretin_2022]\] \[[Schreadley 1977][research_schreadley_1977]\] \[[Scordamaglia et al 2025][research_scordamaglia_mattei_2025]\] \[[Seegmiller 1963][research_seegmiller_1963]\] \[[Shearwood et al 2020][research_shearwood_nabawy_2020]\] \[[Shen et al 2022][research_shen_chang_2022]\] \[[Shi et al 2018][research_shi_tan_2018]\] \[[Siddiqui et al 2016][research_siddiqui_elferik_2016]\] \[[Sisson and Dogan 2026][research_sisson_dogan_2026]\] \[[Sitz and Vernon 1990][research_sitzjoelr_vernontoddh_1990]\] \[[Smith 1991][research_smith_1991]\] \[[Smith and Meyer 1987][research_smith_meyer_1987]\] \[[Speyer 2003][research_speyer_2003]\] \[[Staroswiecki and Amani 2015][research_staroswiecki_amani_2015]\] \[[Steffensen et al 2023][research_steffensen_steinert_2023]\] \[[Stephan et al 2023][research_stephan_stumpf_2023]\] \[[Stirling 1983][research_stirling_1983]\] \[[Sugino et al 2019][research_sugino_harada_2019]\] \[[Sun et al 2020][research_sun_wang_2020]\] \[[Sun et al 2022][research_sun_han_2022]\] \[[Szalai 1975][research_szalaikj_1975]\] \[[Szalai 1976][research_szalaikj_1976]\] \[[Szalai et al 1976][research_szalaikj_fellemanpg_1976]\] \[[Szalai et al 1978][research_szalaikj_jarviscr_1978]\] \[[Tai et al 2023][research_tai_wang_2023]\] \[[Taimoor and Aijun 2019][research_taimoor_aijun_2019]\] \[[Tameh et al 2018][research_tameh_sawan_2018]\] \[[Tang et al 2025][research_tang_tang_2025]\] \[[Teixeira et al 2018][research_teixeira_araujo_2018]\] \[[Terekhov 2022][research_terekhov_2022]\] \[[Tohidi et al 2016][research_tohidi_khakisedigh_2016]\] \[[Tokunaga et al 2015][research_tokunaga_masui_2015]\] \[[Tribuno et al 1976][research_tribuno_klein_1976]\] \[[Unal 2021][research_unal_2021]\] \[[Unal 2021][research_unal_2021_b]\] \[[Uzun 2024][research_uzun_2024]\] \[[Venkataraman and Seiler 2019][research_venkataraman_seiler_2019]\] \[[Vile et al 2020][research_vile_alwi_2020]\] \[[Vitushkin V.V. 2025][research_vitushkinvv_2025]\] \[[Voting software for fault-tolerant aircraft flight control systems 1993][research_voting_software_1993]\] \[[Vukobratović and Stojić 1985][research_vukobratovic_stojic_1985]\] \[[Wang and Guo 2015][research_wang_guo_2015]\] \[[Wang et al 2019][research_wang_kampen_2019]\] \[[Wang et al 2020][research_wang_zhang_2020]\] \[[Wang et al 2025][research_wang_li_2025]\] \[[Wang et al 2025][research_wang_li_2025_b]\] \[[Weinert and Meyer 1984][research_weinert_meyer_1984]\] \[[Wells 2002][research_wells_2002]\] \[[Wen et al 2023][research_wen_song_2023]\] \[[Whitbeck et al 1982][research_whitbeck_smith_1982]\] \[[Wolfe 1967][research_wolfe_1967]\] \[[Xiao and Dong 2019][research_xiao_dong_2019]\] \[[Xiao and Liu 2018][research_xiao_liu_2018]\] \[[Xu and Wang 2016][research_xu_wang_2016]\] \[[Xu et al 2015][research_xu_guo_2015]\] \[[Xu et al 2020][research_xu_zhang_2020]\] \[[Xue and Yao 2020][research_xue_yao_2020]\] \[[Yang and Gao 2020][research_yang_gao_2020]\] \[[Yang et al 2015][research_yang_lee_2015]\] \[[Yildiz et al 2011][research_yildizyidiray_kolmanovskyilyav_2011]\] \[[You 2020][research_you_2020]\] \[[Yu et al 2016][research_yu_zhang_2016]\] \[[Yuksek and Inalhan 2020][research_yuksek_inalhan_2020]\] \[[Zakharov et al 2015][research_zakharov_zattoni_2015]\] \[[Zelenkov 2018][research_zelenkov_2018]\] \[[Zhang et al 2018][research_zhang_yang_2018]\] \[[Zhang et al 2020][research_zhang_han_2020]\] \[[Zhang et al 2023][research_zhang_zhang_2023]\] \[[Zhao and Li 2019][research_zhao_li_2019]\] \[[Zhao et al 2024][research_zhao_lu_2024]\] \[[Zhirabok et al 2024][research_zhirabok_filaretov_2024]\] \[[Zhou et al 2026][research_zhou_gong_2026]\] \[[Zhu and Duan 2015][research_zhu_duan_2015]\] \[[Zipperer et al 1975][research_zipperer_jenney_1975]\] \[[Zipperer et al 1975][research_zipperer_jenney_1975_b]\] \[[Zuhri 2025][research_zuhri_2025]\] \[[Морозов 2015][research_anon_2015]\]

### Composite structures, damage and certification

Composite and variable-stiffness laminate structures, their damage, fatigue and repair, and composite wing design and test.

**263 records.** \[[Acoustic emission monitors damage progression in graphite/epoxy composite structure 1981][research_acoustic_emission_1981]\] \[[Adan and Sheinman 1988][research_adan_sheinman_1988]\] \[[Adney and Horn 1984][research_adneyps_hornwj_1984]\] \[[Alexander et al 1996][research_alexander_tzeng_1996]\] \[[Alhajahmad and Mittelstedt 2021][research_alhajahmad_mittelstedt_2021]\] \[[Allen et al 1983][research_allen_bradley_1983]\] \[[Allen et al 1984][research_allen_bradley_1984]\] \[[Ansell et al 1982][research_ansellgs_loewyrg_1982]\] \[[Aston and Williams 1994][research_aston_williams_1994]\] \[[Audoin and Baste 1994][research_audoin_baste_1994]\] \[[Badaliance and Dill 1981][research_badaliance_dill_1981]\] \[[Badalló et al 2015][research_badallo_trias_2015]\] \[[Baker et al 1985][research_baker_jones_1985]\] \[[Balaji et al 2024][research_balaji_manickam_2024]\] \[[Baranovski and Mikhailovskiy 2020][research_baranovski_mikhailovskiy_2020]\] \[[Bauchau 1981][research_bauchau_1981]\] \[[Bellini and Sorrentino 2018][research_bellini_sorrentino_2018]\] \[[Bendahmane et al 2019][research_bendahmane_hamzacherif_2019]\] \[[Bending of cross-ply laminated plates using Lagrange multipliers 1991][research_bending_of_1991]\] \[[Biskner and Higgins 2005][research_biskner_higgins_2005]\] \[[Biswas 1993][research_biswas_1993]\] \[[Bradley 1986][research_bradley_1986]\] \[[Brooks and Martins 2018][research_brooks_martins_2018]\] \[[Bruno and Libeskind 1990][research_brunojoseph_libeskindmark_1990]\] \[[Cagdas 2017][research_cagdas_2017]\] \[[Chen and Sun 1987][research_chen_sun_1987]\] \[[Chen et al 2018][research_chen_nie_2018]\] \[[Chinvorarat 2021][research_chinvorarat_2021]\] \[[Christoforou 1993][research_christoforou_1993]\] \[[Cohen 1978][research_cohenga_1978]\] \[[Composite Materials in Aircraft Structures 1989][research_composite_materials_1989]\] \[[Crabtree 1979][research_crabtree_1979]\] \[[Crawley and Lee 1978][research_crawley_lee_1978]\] \[[Crews and Naik 1986][research_crews_naik_1986]\] \[[Croop 1985][research_croop_1985]\] \[[Daghighi et al 2020][research_daghighi_rouhi_2020]\] \[[Daken and Mar 1985][research_daken_mar_1985]\] \[[Daniel 1976][research_daniel_1976]\] \[[Darabi and Ganesan 2016][research_darabi_ganesan_2016]\] \[[Darabi and Ganesan 2017][research_darabi_ganesan_2017]\] \[[Daudeville and Ladevèze 1993][research_daudeville_ladeveze_1993]\] \[[Davis et al 1993][research_davisddjr_farleygaryl_1993]\] \[[Deformational behaviour of a unidirectional graphite/epoxy composite under compressive fatigue 1990][research_deformational_behaviour_1990]\] \[[Derkach et al 2022][research_derkach_zinkovskii_2022]\] \[[Dhonau et al 1974][research_dhonau_blosser_1974]\] \[[Ding et al 2022][research_ding_xu_2022]\] \[[Dubary et al 2018][research_dubary_bouvet_2018]\] \[[Dunmire 1982][research_dunmire_1982]\] \[[Durlofsky and Mayers 1970][research_durlofsky_mayers_1970]\] \[[Dutta and Zhao 2025][research_dutta_zhao_2025]\] \[[Dávila and Bisagni 2017][research_davila_bisagni_2017]\] \[[Eckstrom and Spain 1982][research_eckstromcv_spaincv_1982]\] \[[Effects of a controlled modulus interlayer upon the properties of graphite/epoxy composite 1988][research_effects_of_1988]\] \[[Elshazly et al 2025][research_elshazly_kassem_2025]\] \[[Eriksson 1990][research_eriksson_1990]\] \[[Ewing et al 1988][research_ewing_hinger_1988]\] \[[Fanucci 1987][research_fanucci_1987]\] \[[Fatigue behaviour of composite laminate 1977][research_fatigue_behaviour_1977]\] \[[Fazilati and Khalafi 2019][research_fazilati_khalafi_2019_b]\] \[[Filamentary-plastic composite laminate 1974][research_filamentary_plastic_composite_1974]\] \[[Fina and Bisagni 2025][research_fina_bisagni_2025]\] \[[Florance et al 2004][research_florancejamesr_heegjennifer_2004]\] \[[Fukunaga 1990][research_fukunaga_1990]\] \[[Fukunaga and Sekine 1994][research_fukunaga_sekine_1994]\] \[[Fukunaga et al 1993][research_fukunaga_sekine_1993]\] \[[Furtado et al 2019][research_furtado_catalanotti_2019]\] \[[Galasso et al 2024][research_galasso_ciminello_2024]\] \[[Graves and Sawicki 1994][research_graves_sawicki_1994]\] \[[Greenhalgh et al 1993][research_greenhalgh_pastore_1993]\] \[[Greszczuk and Chao 1975][research_greszczuk_chao_1975]\] \[[Griffin and Harvill 1988][research_griffincharlesf_harvillwilliame_1988]\] \[[Griffis et al 1981][research_griffis_masumura_1981]\] \[[Groh and Wu 2022][research_groh_wu_2022]\] \[[Gunnink 1988][research_gunnink_1988]\] \[[Gupta 1998][research_gupta_1998]\] \[[Had and Růžička 2016][research_had_ruzicka_2016]\] \[[Hagnell et al 2016][research_hagnell_langbeck_2016]\] \[[Hahn and Kim 1976][research_hahn_kim_1976]\] \[[Harvill and Kizer 1976][research_harvillwe_kizerja_1976]\] \[[Hirai and Kline 1973][research_hirai_kline_1973]\] \[[Hisada et al 2020][research_hisada_minakuchi_2020]\] \[[Honeycomb-laminate composite structure 1979][research_honeycomb_laminate_composite_1979]\] \[[Hong and Cheong 1993][research_hong_cheong_1993]\] \[[Howdyshell et al 1998][research_howdyshell_trovillion_1998]\] \[[Huang et al 2016][research_huang_wang_2016]\] \[[Huang et al 2024][research_huang_wang_2024]\] \[[Hui 1986][research_hui_1986]\] \[[Hybrid composite laminate structures 1978][research_hybrid_composite_1978]\] \[[Ilcewicz et al 1991][research_ilcewiczlb_walkerth_1991]\] \[[Interlaminar shear fracture of interleaved graphite/epoxy composite materials 1992][research_interlaminar_shear_1992]\] \[[Iryani et al 2019][research_iryani_kadir_2019]\] \[[Jaffar Syed Mohamed Ali and Shahzatul Sakinah Binti Haron 2021][research_jaffarsyedmohamedali_shahzatulsakinahbintiharon_2021]\] \[[Jegley and Bush 1997][research_jegleydawnc_bushharoldg_1997]\] \[[Jegley and Bush 2001][research_jegleydawnc_bushharoldg_2001]\] \[[Jegley et al 2001][research_jegleydawnc_bushharoldg_2001_b]\] \[[Jegley et al 2001][research_jegleydawnc_lovejoyandrewe_2001]\] \[[Jeyachandrabose and Kirkhope 1985][research_jeyachandrabose_kirkhope_1985]\] \[[Jiang et al 2018][research_jiang_li_2018]\] \[[Jing and Tzeng 1995][research_jing_tzeng_1995]\] \[[Jing et al 2022][research_jing_li_2022]\] \[[Jing et al 2023][research_jing_duan_2023]\] \[[Jing et al 2024][research_jing_duan_2024]\] \[[Johnson and June 1972][research_johnsonrw_junerr_1972]\] \[[Johnson and McCarty 1977][research_johnsonrw_mccartyje_1977]\] \[[Jones et al 1985][research_jones_broughton_1985]\] \[[Kalam et al 2022][research_kalam_seshaiah_2022]\] \[[Karal 2001][research_karalmichael_2001]\] \[[Karimi et al 2022][research_karimi_khorshidi_2022]\] \[[Katunin et al 2015][research_katunin_dragan_2015]\] \[[Kcs et al 2024][research_kcs_james_2024]\] \[[Kennedy 1991][research_kennedy_1991]\] \[[Khani et al 2017][research_khani_abdalla_2017]\] \[[Kharghani and Mittelstedt 2022][research_kharghani_mittelstedt_2022]\] \[[Kieffer 2006][research_kieffer_2006]\] \[[Kilimtzidis et al 2023][research_kilimtzidis_giannaros_2023]\] \[[Klasztorny et al 2018][research_klasztorny_nycz_2018]\] \[[Klotzsche 1984][research_klotzschem_1984]\] \[[Knauss and Stone 1982][research_knaussjf_stonerh_1982]\] \[[Knight 1982][research_knight_1982]\] \[[Kota et al 1997][research_kota_hetrick_1997]\] \[[Kubiak et al 2019][research_kubiak_gliszczynski_2019]\] \[[Kumar et al 2025][research_kumar_asha_2025]\] \[[Kumar Shakya and Sekhar Padhee 2023][research_kumarshakya_sekharpadhee_2023]\] \[[Lai and Young 1995][research_lai_young_1995]\] \[[Lee and Lee 1990][research_lee_lee_1990]\] \[[Lee and Mall 1989][research_lee_mall_1989]\] \[[Lee et al 1994][research_lee_kim_1994]\] \[[Lei et al 2020][research_lei_wang_2020]\] \[[Leitch et al 2024][research_leitch_stodieck_2024]\] \[[Leitch et al 2025][research_leitch_stodieck_2025]\] \[[Li et al 2026][research_li_miranda_2026]\] \[[Libeskind et al 1973][research_libeskind_minecci_1973]\] \[[Liguori et al 2024][research_liguori_zucco_2024]\] \[[Liu et al 2015][research_liu_toropov_2015]\] \[[Liu et al 2019][research_liu_featherston_2019]\] \[[Liu et al 2023][research_liu_featherston_2023]\] \[[Liu et al 2023][research_liu_li_2023]\] \[[Loja et al 2017][research_loja_barbosa_2017]\] \[[Long et al 2021][research_long_mu_2021]\] \[[Loos and Springer 1983][research_loos_springer_1983]\] \[[Loughlan and Ata 1995][research_loughlan_ata_1995]\] \[[Lovejoy and Scotti 2019][research_lovejoyandrewe_scottistephenj_2019]\] \[[Luo et al 2024][research_luo_ferrari_2024]\] \[[Magliacano et al 2025][research_magliacano_tufano_2025]\] \[[Manickam et al 2025][research_manickam_polit_2025]\] \[[Mar and Lin 1979][research_mar_lin_1979]\] \[[Marín and Graciani 2022][research_marin_graciani_2022]\] \[[Matrix cracking and stiffness reduction during the fatigue of a (0/90)9 GFRP laminate 1985][research_matrix_cracking_1985]\] \[[Mayer et al 2016][research_mayer_prowe_2016]\] \[[McKinney 1972][research_mckinney_1972]\] \[[Meng et al 2019][research_meng_yan_2019]\] \[[Mengzhu et al 2026][research_mengzhu_zhitao_2026]\] \[[Mijovic 1985][research_mijovic_1985]\] \[[Mingong and Sun 2022][research_mingong_sun_2022]\] \[[Molent and Haddad 2020][research_molent_haddad_2020]\] \[[Morris 1977][research_morris_1977]\] \[[Mukhopadhyay and Sorokach 2015][research_mukhopadhyayvivek_sorokachmichaelr_2015]\] \[[Naganarayana and Atluri 1995][research_naganarayana_atluri_1995]\] \[[Negahban et al 2025][research_negahbanb_khalafi_2025]\] \[[Neu and Huang 1973][research_neu_huang_1973]\] \[[Nikrad et al 2015][research_nikrad_asadi_2015]\] \[[Niu and Zhang 2022][research_niu_zhang_2022]\] \[[Non-linear bending of antisymmetric angle ply laminated plates 1977][research_non_linear_bending_1977]\] \[[Norwood 1992][research_norwood_1992]\] \[[Ozdil and Carlsson 1992][research_ozdil_carlsson_1992]\] \[[Pagano 1974][research_pagano_1974]\] \[[Palm et al 2000][research_palmtod_mahlermary_2000]\] \[[Papirno 1977][research_papirno_1977]\] \[[Park 2015][research_park_2015]\] \[[Park 2016][research_park_2016]\] \[[Patni et al 2019][research_patni_minera_2019]\] \[[Patterson and Grenestedt 2018][research_patterson_grenestedt_2018]\] \[[Pellerin 1988][research_pellerin_1988]\] \[[Pereira et al 2021][research_pereira_sales_2021]\] \[[Philippidis 1994][research_philippidis_1994]\] \[[Polyester, fibreglass-reinforced composite laminate 1978][research_polyester_fibreglass_reinforced_1978]\] \[[Pritt 1980][research_pritt_1980]\] \[[Pryor and Barker 1970][research_pryor_barker_1970]\] \[[Przekop and Jegley 2014][research_przekopadam_jegleydawnc_2014_b]\] \[[Przekop et al 2014][research_przekopadam_jegleydawnc_2014]\] \[[Qiao et al 2018][research_qiao_gao_2018]\] \[[Qiu 2022][research_qiu_2022]\] \[[Ramroop et al 2025][research_ramroop_chinchamee_2025]\] \[[Rao and Uma Maheswara Rao 1992][research_rao_umamaheswararao_1992]\] \[[Rao and Hofer 1973][research_rao_hofer_1973]\] \[[Rapoff et al 1990][research_rapoffandrewj_dillharoldd_1990]\] \[[Rashed and Demir 2022][research_rashed_demir_2022]\] \[[Rate sensitivity of Mode II interlaminar fracture toughness in graphite/epoxy and graphite/PEEK composite materials 1988][research_rate_sensitivity_1988]\] \[[Rathnasabapathy et al 2022][research_rathnasabapathy_mouritz_2022]\] \[[Rich et al 1974][research_richmj_ridgleygf_1974]\] \[[Rouhi et al 2018][research_rouhi_ghayoor_2018]\] \[[Roylance 1980][research_roylance_1980]\] \[[Rumble 1987][research_rumble_1987]\] \[[Ryder and Walker 1976][research_ryder_walker_1976]\] \[[Sabido et al 2017][research_sabido_bahamonde_2017]\] \[[Samukham et al 2017][research_samukham_raju_2017]\] \[[Samukham et al 2019][research_samukham_raju_2019]\] \[[Samukham et al 2020][research_samukham_vyasarayani_2020]\] \[[Sandhu et al 1991][research_sandhu_wolfe_1991]\] \[[Schpey 1980][research_schpey_1980]\] \[[Serhat et al 2020][research_serhat_bediz_2020]\] \[[Seshadri and Krishnamurthy 2017][research_seshadri_krishnamurthy_2017]\] \[[Seyoung 1990][research_seyoung_1990]\] \[[Shafei et al 2024][research_shafei_faroughi_2024]\] \[[Shafighfard et al 2019][research_shafighfard_demir_2019]\] \[[Shcherban et al 2022][research_shcherban_sterlin_2022]\] \[[Sheikhi et al 2024][research_sheikhi_rafieianamagh_2024]\] \[[Sheikhi et al 2024][research_sheikhi_rafieianamagh_2024_b]\] \[[Short 1995][research_short_1995]\] \[[Shrivastava et al 2020][research_shrivastava_sharma_2020]\] \[[Sinha et al 2021][research_sinha_klimmek_2021]\] \[[Soovere 1982][research_soovere_1982]\] \[[Spencer and Watson 1992][research_spencer_watson_1992]\] \[[Stanton and Crain 1980][research_stanton_crain_1980]\] \[[Stauffer and James 1978][research_staufferwa_jamesam_1978]\] \[[Study of advanced composite 1978][research_study_of_1978]\] \[[Sulaeman et al 2017][research_sulaeman_abdullah_2017]\] \[[Sun and Yoon 1988][research_sun_yoon_1988]\] \[[Suraj et al 2023][research_suraj_anilkumar_2023]\] \[[Synaszko et al 2015][research_synaszko_salacinski_2015]\] \[[Talreja and Phan 2019][research_talreja_phan_2019]\] \[[Tang 1989][research_tang_1989]\] \[[Tang and Liu 2018][research_tang_liu_2018]\] \[[The viscoelastic behaviour of the principal compliance matrix of a unidirectional graphite/epoxy composite 1981][research_the_viscoelastic_1981]\] \[[Thermal damage effects and delamination toughness of a graphite/epoxy composite 1989][research_thermal_damage_1989]\] \[[Thermal expansion and swelling of cured epoxy resin used in graphite/epoxy composite materials 1981][research_thermal_expansion_1981]\] \[[Thomas et al 2020][research_thomas_hallett_2020]\] \[[Tian et al 2025][research_tian_sun_2025]\] \[[Toledano and Murakami 1987][research_toledano_murakami_1987]\] \[[Torsional stiffness of plastic tubes reinforced with glass fibres 1972][research_torsional_stiffness_1972]\] \[[Trabocco 1980][research_trabocco_1980]\] \[[Tungikar and Rao 1994][research_tungikar_rao_1994]\] \[[Turner and Hoy 1976][research_turnermj_hoyjm_1976]\] \[[Ulry et al 1976][research_ulry_gehring_1976]\] \[[Urso et al 2026][research_urso_giunta_2026]\] \[[van Dooren and Bisagni 2024][research_vandooren_bisagni_2024]\] \[[Varun et al 2022][research_varun_mondal_2022]\] \[[Vescovini and Dozio 2016][research_vescovini_dozio_2016]\] \[[Vilela and Donadon 2025][research_vilela_donadon_2025]\] \[[Walker et al 1997][research_walkerth_minguetpj_1997]\] \[[Wang et al 2019][research_wang_baker_2019]\] \[[Wang et al 2021][research_wang_wan_2021]\] \[[Wang et al 2022][research_wang_zhang_2022_b]\] \[[Wang et al 2025][research_wang_wang_2025]\] \[[Wang 1996][research_wangjohnt_1996]\] \[[Wang et al 1996][research_wangjohnt_jegleydawnc_1996]\] \[[Weisshaar and Ehlers 1990][research_weisshaarta_ehlerssm_1990]\] \[[White et al 2005][research_white_geubelle_2005]\] \[[Whitehead et al 1992][research_whiteheadrs_foremancr_1992]\] \[[Whitworth 1987][research_whitworth_1987]\] \[[Wiggenraad and Bauld 1993][research_wiggenraadjfm_bauldnrjr_1993]\] \[[Wu et al 2015][research_wu_gunnion_2015]\] \[[Xiao and Harrison 2021][research_xiao_harrison_2021]\] \[[Xie et al 2025][research_xie_zhang_2025]\] \[[Yalvaç et al 1991][research_yalvac_yats_1991]\] \[[Yang and Liu 1976][research_yang_liu_1976]\] \[[Yang et al 1994][research_yang_batra_1994]\] \[[York and Williams 1995][research_york_williams_1995]\] \[[You et al 2019][research_you_yasaee_2019]\] \[[Yu 1987][research_yu_1987]\] \[[Yu et al 2017][research_yu_fang_2017]\] \[[Yuan and Reeder 2001][research_yuanfg_reederjamesr_2001]\] \[[Zhou et al 2019][research_zhou_ruan_2019]\]

### Aeroservoelasticity and structural mode control

Active flutter suppression, gust load alleviation and the coupling of structural modes with the control system.

**192 records.** \[[Ahmadi et al 2024][research_ahmadi_farsadi_2024_b]\] \[[Alam et al 2015][research_alam_hromcik_2015]\] \[[Armanious and Lind 2017][research_armanious_lind_2017]\] \[[Armstrong et al 2006][research_armstrong_lindberg_2006]\] \[[Balatti et al 2022][research_balatti_khodaparast_2022]\] \[[Barbosa et al 2022][research_barbosa_bertolin_2022]\] \[[Batina and Yang 1985][research_batina_yang_1985]\] \[[Berg et al 2025][research_berg_ting_2025]\] \[[Beyer et al 2024][research_beyer_steen_2024]\] \[[Beyer et al 2024][research_beyer_ullah_2024]\] \[[Bi et al 2017][research_bi_xie_2017]\] \[[Broussard and Halyo 1983][research_broussardjr_halyon_1983]\] \[[Brüderlin et al 2018][research_bruderlin_hosters_2018]\] \[[Burnett et al 2016][research_burnett_beranek_2016]\] \[[Carlson et al 2017][research_carlson_verberg_2017]\] \[[Cavaliere and Fezans 2024][research_cavaliere_fezans_2024]\] \[[Cavaliere et al 2024][research_cavaliere_fezans_2024_b]\] \[[Chai et al 2017][research_chai_song_2017]\] \[[Chen and Zhao 2020][research_chen_zhao_2020]\] \[[Chen et al 2018][research_chen_yang_2018]\] \[[Chen et al 2022][research_chen_han_2022]\] \[[Chen et al 2023][research_chen_shi_2023]\] \[[Chen et al 2023][research_chen_shi_2023_b]\] \[[Chen et al 2025][research_chen_zhai_2025]\] \[[Chipman et al 1982][research_chipman_zislin_1982]\] \[[Chipman et al 1983][research_chipman_zislin_1983]\] \[[Cobo-González et al 2026][research_cobogonzalez_rodriguezrobles_2026]\] \[[Dai and Yang 2015][research_dai_yang_2015]\] \[[Darabseh et al 2022][research_darabseh_tarabulsi_2022]\] \[[de Souza et al 2023][research_desouza_vuillemin_2023]\] \[[Di Leone et al 2021][research_dileone_lobalbo_2021]\] \[[Dillinger et al 2020][research_dillinger_meddaikar_2020]\] \[[Dilmi 2022][research_dilmi_2022]\] \[[Dul 2018][research_dul_2018]\] \[[Edwards 1983][research_edwards_1983]\] \[[Farhat and Amsallem 2011][research_farhat_amsallem_2011]\] \[[Farsadi et al 2026][research_farsadi_ahmadi_2026]\] \[[Fonte et al 2015][research_fonte_ricci_2015]\] \[[Fournier et al 2022][research_fournier_massioni_2022]\] \[[Friedmann 1998][research_friedmann_1998]\] \[[Gao and Cai 2016][research_gao_cai_2016]\] \[[Gao et al 2024][research_gao_liu_2024]\] \[[Gilbert et al 1982][research_gilbert_schmidt_1982]\] \[[Goizueta et al 2022][research_goizueta_wynn_2022]\] \[[Griffin and Eastep 1981][research_griffin_eastep_1981]\] \[[Gupta et al 1987][research_gupta_brenner_1987]\] \[[Gupta et al 1989][research_gupta_brenner_1989]\] \[[Guruswamy 2019][research_guruswamy_2019]\] \[[Guruswamy and Tu 1989][research_guruswamy_tu_1989]\] \[[Haley and Soloway 2022][research_haley_soloway_2022]\] \[[Hamada et al 2019][research_hamada_saitoh_2019]\] \[[Hansen et al 2022][research_hansen_duan_2022]\] \[[Heckl et al 1962][research_heckl_lyon_1962]\] \[[Huang et al 2019][research_huang_yang_2019]\] \[[Huang et al 2022][research_huang_yu_2022]\] \[[Ibren et al 2020][research_ibren_sulaeman_2020]\] \[[Jalalnezhad 2026][research_jalalnezhad_2026]\] \[[Kassem et al 2020][research_kassem_yang_2020]\] \[[Kassem et al 2021][research_kassem_yang_2021]\] \[[Khalil and Bauknecht 2024][research_khalil_bauknecht_2024]\] \[[Khalil and Fezans 2020][research_khalil_fezans_2020]\] \[[Kholodar 2016][research_kholodar_2016]\] \[[Klepl 1995][research_klepl_1995]\] \[[Kratochvíl and Valenta 2024][research_kratochvil_valenta_2024]\] \[[Krener 2001][research_krener_2001]\] \[[Kuvshinov et al 2019][research_kuvshinov_lazurin_2019]\] \[[Kuz'mina et al 2020][research_kuzmina_ishmuratov_2020]\] \[[Lee and Kim 2021][research_lee_kim_2021]\] \[[Lee and Singh 2018][research_lee_singh_2018]\] \[[Li and Qin 2020][research_li_qin_2020]\] \[[Li and Qin 2021][research_li_qin_2021]\] \[[Li and Qin 2021][research_li_qin_2021_b]\] \[[Li and Qin 2022][research_li_qin_2022]\] \[[Liu 2018][research_liu_2018]\] \[[Liu and Sun 2016][research_liu_sun_2016]\] \[[Liu and Sun 2017][research_liu_sun_2017]\] \[[Liu and Wang 2019][research_liu_wang_2019]\] \[[Liu et al 2017][research_liu_huang_2017]\] \[[Liu et al 2017][research_liu_sun_2017_b]\] \[[Liu et al 2020][research_liu_gao_2020]\] \[[Liu et al 2022][research_liu_sun_2022]\] \[[Liu et al 2023][research_liu_gao_2023]\] \[[Liu et al 2025][research_liu_zheng_2025]\] \[[Livne 2018][research_livne_2018]\] \[[Mahgoub and El-Badawy 2022][research_mahgoub_elbadawy_2022]\] \[[Mamedov et al 2018][research_mamedov_paryshev_2018]\] \[[Micheli 2024][research_micheli_2024]\] \[[Moosavi and Elasha 2022][research_moosavi_elasha_2022]\] \[[Moreira et al 2024][research_moreira_moleiro_2024]\] \[[Morino and Obayashi 2015][research_morino_obayashi_2015]\] \[[Mu et al 2022][research_mu_huang_2022]\] \[[Mu et al 2026][research_mu_huang_2026]\] \[[Muscarello et al 2016][research_muscarello_quaranta_2016]\] \[[Muñoz and García-Fogeda 2022][research_munoz_garciafogeda_2022]\] \[[Muñoz and García-Fogeda 2024][research_munoz_garciafogeda_2024]\] \[[Nam et al 2000][research_nam_chen_2000]\] \[[Narimani et al 2025][research_narimani_haddadpour_2025]\] \[[Niel et al 2017][research_niel_seuret_2017]\] \[[Noll et al 1983][research_noll_calico_1983]\] \[[Onkar 2021][research_onkar_2021]\] \[[Ouyang et al 2021][research_ouyang_gu_2021]\] \[[Passive wing/store flutter suppression 1982][research_passive_wing_store_1982]\] \[[Patartics et al 2022][research_patartics_liptak_2022]\] \[[Pena et al 2018][research_penafrancisco_martinsbenjamin_2018]\] \[[Phan 2020][research_phan_2020]\] \[[Piao et al 2019][research_piao_zhang_2019]\] \[[Pourtakdoust and Khodabakhsh 2026][research_pourtakdoust_khodabakhsh_2026]\] \[[Poussot-Vassal et al 2017][research_poussotvassal_demourant_2017]\] \[[Pusch et al 2019][research_pusch_knoblach_2019]\] \[[Qian 2018][research_qian_2018]\] \[[Qu and Li 2022][research_qu_li_2022]\] \[[Quero et al 2019][research_quero_vuillemin_2019]\] \[[Rao and Padmanabhan 2019][research_rao_padmanabhan_2019]\] \[[Rekik et al 2024][research_rekik_khaled_2024]\] \[[Reyes et al 2019][research_reyes_climent_2019]\] \[[Rieck et al 2026][research_rieck_herrmann_2026]\] \[[Rimer et al 1983][research_rimer_chipman_1983]\] \[[Ro et al 1992][research_ro_barlow_1992]\] \[[Roizner and Karpel 2018][research_roizner_karpel_2018]\] \[[Roizner and Karpel 2019][research_roizner_karpel_2019]\] \[[Rosique et al 2019][research_rosique_alamin_2019]\] \[[Sabatini et al 2026][research_sabatini_coppotelli_2026]\] \[[Sahyoun et al 2026][research_sahyoun_boose_2026]\] \[[Schildkamp et al 2023][research_schildkamp_chang_2023]\] \[[Schmidt 2016][research_schmidt_2016]\] \[[Schmidt et al 2020][research_schmidt_danowsky_2020]\] \[[Scott et al 2016][research_scott_bartels_2016]\] \[[sekhar et al 2024][research_sekhar_suresh_2024]\] \[[Sharma et al 2022][research_sharma_agrawal_2022]\] \[[Simbuerger et al 2022][research_simbuerger_raveh_2022]\] \[[Singh et al 2016][research_singh_brown_2016]\] \[[Soneda et al 2022][research_soneda_tsushima_2022]\] \[[Stanford 2016][research_stanford_2016]\] \[[Stanford 2017][research_stanford_2017]\] \[[Stanford 2019][research_stanford_2019]\] \[[Structural Aspects of Flexible 2000][research_structural_aspects_2000]\] \[[Suh et al 2014][research_suhpeterm_conyershowardj_2014]\] \[[Suh et al 2015][research_suhpeterm_conyershowardjason_2015]\] \[[Szollosi and Baranyi 2016][research_szollosi_baranyi_2016]\] \[[Szymanski et al 2025][research_szymanski_alstrom_2025]\] \[[Takarics and Vanek 2019][research_takarics_vanek_2019]\] \[[Tang et al 2016][research_tang_wu_2016]\] \[[Tang et al 2018][research_tang_chen_2018]\] \[[Tang et al 2020][research_tang_chen_2020]\] \[[Tang et al 2020][research_tang_wang_2020]\] \[[Tantaroudas and Karachalios 2026][research_tantaroudas_karachalios_2026]\] \[[Theis et al 2020][research_theis_pfifer_2020]\] \[[Ting et al 2023][research_ting_mesbahi_2023]\] \[[Ting et al 2026][research_ting_berg_2026]\] \[[Toffol 2024][research_toffol_2024]\] \[[Toffol and Ricci 2023][research_toffol_ricci_2023]\] \[[Triplett 1972][research_triplett_1972]\] \[[Triplett et al 1973][research_triplett_kappus_1973]\] \[[Tsushima and Su 2017][research_tsushima_su_2017]\] \[[Ursu et al 2018][research_ursu_ionguta_2018]\] \[[Vepa and Kwon 2021][research_vepa_kwon_2021]\] \[[Verhaegen and Żbikowski 2017][research_verhaegen_zbikowski_2017]\] \[[Waitman and Marcos 2019][research_waitman_marcos_2019]\] \[[Waitman and Marcos 2020][research_waitman_marcos_2020]\] \[[Wang and Xu 2018][research_wang_xu_2018]\] \[[Wang et al 2018][research_wang_daronch_2018]\] \[[Wang et al 2019][research_wang_vankampen_2019]\] \[[Wang et al 2025][research_wang_sun_2025]\] \[[Wheatcroft et al 2025][research_wheatcroft_groh_2025]\] \[[Wheatcroft et al 2025][research_wheatcroft_mahadik_2025]\] \[[Wie and Byun 1989][research_wie_byun_1989]\] \[[Wu and Livne 2016][research_wu_livne_2016]\] \[[Wu and Tong 2017][research_wu_tong_2017]\] \[[Wu et al 2025][research_wu_fu_2025]\] \[[Xiang and Wang 2023][research_xiang_wang_2023]\] \[[Xiong et al 2026][research_xiong_tang_2026]\] \[[Yang et al 2017][research_yang_huang_2017]\] \[[Yang et al 2019][research_yang_huang_2019]\] \[[Yang et al 2019][research_yang_yang_2019]\] \[[Yang et al 2026][research_yang_zhang_2026]\] \[[Yin et al 2025][research_yin_huang_2025]\] \[[Yingsong et al 2015][research_yingsong_zhichun_2015]\] \[[Yoo 2017][research_yoo_2017]\] \[[Yue and Zhao 2020][research_yue_zhao_2020]\] \[[Yurtsever et al 2026][research_yurtsever_sahin_2026]\] \[[Zhang and Zhao 2023][research_zhang_zhao_2023_b]\] \[[Zhang et al 2015][research_zhang_marzocca_2015]\] \[[Zhang et al 2018][research_zhang_liu_2018]\] \[[Zhang et al 2024][research_zhang_qiu_2024]\] \[[Zhang et al 2026][research_zhang_dai_2026]\] \[[Zhao et al 2016][research_zhao_yue_2016]\] \[[Zheng et al 2024][research_zheng_pontillo_2024]\] \[[Zheng et al 2026][research_zheng_dai_2026]\] \[[Zhou et al 2018][research_zhou_yu_2018]\] \[[Zhu et al 2017][research_zhu_wang_2017]\] \[[Zou et al 2021][research_zou_mu_2021]\] \[[Zou et al 2022][research_zou_huang_2022]\]

### Handling qualities and pilot-vehicle interaction

Handling and flying qualities criteria for augmented aircraft, pilot-induced oscillation and pilot modelling.

**176 records.** \[[Adams and Hatch 1971][research_adams_hatch_1971]\] \[[Air Force Test Pilot School Edwards Afb Ca 1969][research_airforcetestpilotschooledwardsafbca_1969]\] \[[Air Force Test Pilot School Edwards Afb Ca 1981][research_airforcetestpilotschooledwardsafbca_1981]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_c]\] \[[Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_d]\] \[[Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_e]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991_b]\] \[[Ali 1997][research_alisyedfirasat_1997]\] \[[Anderson 1970][research_anderson_1970]\] \[[Anderson 1985][research_anderson_1985]\] \[[Anderson and Toivanen 1970][research_anderson_toivanen_1970]\] \[[Antonakis 2025][research_antonakis_2025]\] \[[Antonakis 2025][research_antonakis_2025_b]\] \[[Ashkenas 1984][research_ashkenas_1984]\] \[[Bahr et al 2021][research_bahr_mckay_2021]\] \[[Bailey and Knotts 1990][research_baileyre_knottslh_1990]\] \[[Bailey and Smith 1981][research_baileyre_smithre_1981]\] \[[Bailey et al 1988][research_baileyrandalle_powersbruceg_1988]\] \[[Bar-Gill and Stengel 1986][research_bargill_stengel_1986]\] \[[Berger et al 2021][research_berger_tischler_2021]\] \[[Berger et al 2022][research_berger_blanken_2022]\] \[[Berger et al 2022][research_berger_blanken_2022_b]\] \[[Berry 1981][research_berrydt_1981]\] \[[Bidinotto et al 2021][research_bidinotto_moura_2021]\] \[[Bischoff 1983][research_bischoff_1983]\] \[[Black and Moorhouse 1979][research_black_moorhouse_1979]\] \[[Boothe et al 1974][research_boothe_chen_1974]\] \[[Bowes and Miller 1976][research_bowes_miller_1976]\] \[[Broussard and Stengel 1977][research_broussard_stengel_1977]\] \[[Callaghan and Kunz 2021][research_callaghan_kunz_2021]\] \[[Campos and Marques 2021][research_campos_marques_2021]\] \[[Cavalcanti et al 2026][research_cavalcanti_uehara_2026]\] \[[Chalk 1964][research_chalk_1964]\] \[[Chalk et al 1969][research_chalk_neal_1969]\] \[[Chance Vought Corp Dallas Tx 1979][research_chancevoughtcorpdallastx_1979]\] \[[Chetty and Lakshmi 1991][research_chetty_lakshmi_1991]\] \[[Chowhan et al 2019][research_chowhan_arya_2019]\] \[[Coldsnow et al 2009][research_coldsnow_uybarreta_2009]\] \[[Connelly 1982][research_connelly_1982]\] \[[Crane and Sommer 1961][research_craneharoldl_sommerrobertw_1961]\] \[[Curry et al 1965][research_curry_matthews_1965]\] \[[Difranco 1970][research_difranco_1970]\] \[[Dorey et al 1980][research_dorey_good_1980]\] \[[Durand and Teper 1964][research_durand_teper_1964]\] \[[Dussart et al 2019][research_dussart_lone_2019]\] \[[Efremov et al 2020][research_efremov_efremov_2020]\] \[[Efremov et al 2022][research_efremov_shcherbakov_2022]\] \[[Eichler 1970][research_eichler_1970]\] \[[Eney 1968][research_eney_1968]\] \[[Engelland et al 1992][research_engellandsa_franklinja_1992]\] \[[Favaro et al 2025][research_favaro_rylko_2025]\] \[[Ford 1989][research_ford_1989]\] \[[Fortiş et al 2015][research_fortis_fortis_2015]\] \[[Franklin and Innis 1978][research_franklin_innis_1978]\] \[[Franklin and Innis 1972][research_franklinja_innisrc_1972]\] \[[Gallagher 1971][research_gallagher_1971]\] \[[Garg and Schmidt 1988][research_gargsanjay_schmidtdavidk_1988]\] \[[Gerdes and Hynes 1972][research_gerdes_hynes_1972]\] \[[Gerken 1979][research_gerken_1979]\] \[[Giles 1972][research_giles_1972]\] \[[Grant et al 2015][research_grant_stol_2015]\] \[[Grantham et al 1976][research_granthamwd_nguyenlt_1976]\] \[[Guo 2021][research_guo_2021_b]\] \[[Hall 1971][research_hall_1971]\] \[[Hall et al 1974][research_hall_weingarten_1974]\] \[[Hanson et al 2011][research_hansoncurt_schaeferjacob_2011]\] \[[Harper and Robert P. 1955][research_harper_robertp_1955]\] \[[Hebbar and Pashilkar 2016][research_hebbar_pashilkar_2016]\] \[[Henriquez Huecas et al 2022][research_henriquezhuecas_white_2022]\] \[[Herrington et al 2023][research_herrington_zahed_2023]\] \[[Hess 1984][research_hess_1984]\] \[[Hess 1989][research_hess_1989]\] \[[Hess 1991][research_hess_1991]\] \[[Hess 2016][research_hess_2016]\] \[[Hess 2018][research_hess_2018]\] \[[Hess and Sunyoto 1985][research_hess_sunyoto_1985]\] \[[Higgins and Shomber 1965][research_higgins_shomber_1965]\] \[[Hirsch and McCORMICK 1966][research_hirsch_mccormick_1966]\] \[[Hodgkinson et al 1976][research_hodgkinson_lamanna_1976]\] \[[Hoh and Mitchell 1983][research_hoh_mitchell_1983]\] \[[Huff 1949][research_huff_ww_1949]\] \[[Humphreys-Jennings et al 2020][research_humphreysjennings_lappas_2020]\] \[[Ioannis and Ioannis 2026][research_ioannis_ioannis_2026]\] \[[Ivler et al 2022][research_ivler_truong_2022]\] \[[Jacobson and Joshi 1977][research_jacobson_joshi_1977]\] \[[Jacobson and Joshi 1978][research_jacobson_joshi_1978]\] \[[Jewell et al 1979][research_jewell_heffley_1979]\] \[[Ji et al 2021][research_ji_kim_2021]\] \[[Ji et al 2022][research_ji_lu_2022]\] \[[Jing et al 2020][research_jing_qi_2020]\] \[[Jusko and Berger 2026][research_jusko_berger_2026]\] \[[Key 1971][research_key_1971]\] \[[Key 1982][research_key_1982]\] \[[Kim and Kunz 2017][research_kim_kunz_2017]\] \[[Kim et al 2022][research_kim_ji_2022]\] \[[Kish et al 1997][research_kish_mosle_1997]\] \[[Kriechbaum and Stineman 1972][research_kriechbaum_stineman_1972]\] \[[Lampton et al 2024][research_lampton_klyde_2024]\] \[[Lawrence et al 2018][research_lawrence_theodore_2018]\] \[[Lee et al 2020][research_lee_kim_2020]\] \[[Leondes and Rankine 1972][research_leondes_rankine_1972]\] \[[Levi and Nelson 1964][research_levi_nelson_1964]\] \[[Levison 1982][research_levison_1982]\] \[[Li et al 2024][research_li_zhang_2024_b]\] \[[Mabboux et al 2024][research_mabboux_pommierbudinger_2024]\] \[[Malcom 1969][research_malcom_1969]\] \[[Mandal and Gu 2016][research_mandal_gu_2016]\] \[[Marr and Roderick 1975][research_marr_roderick_1975]\] \[[McGREGOR and Smith 1966][research_mcgregor_smith_1966]\] \[[Memon et al 2021][research_memon_white_2021]\] \[[Miller 1970][research_miller_1970]\] \[[Miller and Clark 1965][research_miller_clark_1965]\] \[[Miranda and Bidinotto 2025][research_miranda_bidinotto_2025]\] \[[Montgomery 1972][research_montgomery_1972]\] \[[Neal and Smith 1970][research_neal_smith_1970]\] \[[Newton and Kroo 2025][research_newton_kroo_2025]\] \[[Nguyen et al 2021][research_nguyen_lowenberg_2021]\] \[[Ohta et al 1979][research_ohta_nikiforuk_1979]\] \[[Ohta et al 1982][research_ohta_nikiforuk_1982]\] \[[Perfect et al 2015][research_perfect_jump_2015]\] \[[Perfect et al 2015][research_perfect_jump_2015_b]\] \[[Place et al 1974][research_place_altmann_1974]\] \[[Portapas and Cooke 2020][research_portapas_cooke_2020]\] \[[Powers 1982][research_powers_1982]\] \[[Powers 1980][research_powersbg_1980]\] \[[Radford et al 1980][research_radfordrc_smithr_1980]\] \[[Ranaudo et al 2000][research_ranaudorichardj_ratvaskythomasp_2000]\] \[[Rauer 2019][research_rauer_2019]\] \[[Reeder 1958][research_reeder_1958]\] \[[Reid et al 1994][research_reid_rajagopal_1994]\] \[[Roscoe et al 1975][research_roscoe_eisele_1975]\] \[[Sadoff et al 1961][research_sadoffmelvin_mcfaddennormanm_1961]\] \[[Saetti and Rogers 2024][research_saetti_rogers_2024]\] \[[Saetti et al 2020][research_saetti_horn_2020]\] \[[Sammonds et al 1982][research_sammondsroberti_mcneillwaltere_1982]\] \[[Schroeder et al 2001][research_schroederjefferya_chungwilliamwy_2001]\] \[[Shafer 1980][research_shafermf_1980]\] \[[Shafer et al 1983][research_shafermf_smithre_1983]\] \[[Shafer et al 1984][research_shafermf_smithre_1984]\] \[[Shafer and Steinmetz 2001][research_shafermaryf_steinmetzpaul_2001]\] \[[Shafer and Steinmetz 2001][research_shafermaryf_steinmetzpaul_2001_b]\] \[[Shomber and Gertsen 1967][research_shomber_gertsen_1967]\] \[[Smith and Geddes 1979][research_smith_geddes_1979]\] \[[Smith et al 1973][research_smith_lebacqz_1973]\] \[[Smith 1979][research_smithjw_1979]\] \[[Smith and Berry 1975][research_smithjw_berrydt_1975]\] \[[Srinathkumar 2015][research_srinathkumar_2015]\] \[[Sun et al 2020][research_sun_shi_2020]\] \[[Teper and Stapleford 1966][research_teper_stapleford_1966]\] \[[Theodore et al 2020][research_theodore_malpica_2020]\] \[[Tischler et al 1991][research_tischlermarkb_fletcherjayw_1991]\] \[[Tran et al 2017][research_tran_sakamoto_2017]\] \[[Tritschler and O’Connor 2016][research_tritschler_oconnor_2016]\] \[[Truong et al 2016][research_truong_rakotomamonjy_2016]\] \[[Twisdale and Kirsten 1984][research_twisdale_kirsten_1984]\] \[[Van Baelen et al 2020][research_vanbaelen_ellerbroek_2020]\] \[[van Dam et al 1981][research_vandam_holmes_1981]\] \[[Vinje and Miller 1973][research_vinje_miller_1973]\] \[[Walsh 1993][research_walshkevinr_1993]\] \[[Wang et al 2021][research_wang_lu_2021]\] \[[Wang et al 2023][research_wang_lu_2023]\] \[[Wang et al 2025][research_wang_ji_2025]\] \[[Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]\] \[[White et al 2021][research_white_padfield_2021]\] \[[Wilson et al 1993][research_wilson_riley_1993]\] \[[Witte et al 2003][research_witte_monson_2003]\] \[[Woodcock and George 1976][research_woodcockrj_georgefl_1976]\] \[[Xu et al 2019][research_xu_tan_2019]\] \[[Yildiz and Kolmanovsky 2010][research_yildizyildiray_kolmanovskyilyav_2010]\] \[[Yin and Wang 2017][research_yin_wang_2017]\] \[[Yuan et al 2022][research_yuan_thomson_2022]\] \[[Zanoni et al 2022][research_zanoni_gerosa_2022]\] \[[Zaytseva et al 2021][research_zaytseva_kuznetsov_2021]\]

**80 of the 176 records date from 1984 or earlier**, by the year the aircraft first flew.

### The X-29 and forward-swept wing aircraft

The aircraft's own reports, and the forward-swept wing as a configuration, in the tunnel, in computation and in flight.

**175 records.** \[[Abed et al 2024][research_abed_alhamadani_2024]\] \[[Adegbindin et al 2016][research_adegbindin_love_2016]\] \[[Ahmadi 1988][research_aliahmadi_1988]\] \[[Ashworth et al 1986][research_ashworth_waltrip_1986]\] \[[Ashworth et al 1988][research_ashworth_mouch_1988]\] \[[Bach et al 2016][research_bach_jebari_2016]\] \[[Bauer et al 1995][research_bauer_clarke_1995]\] \[[Baumgärtner et al 2016][research_baumgartner_viti_2016]\] \[[Bjarke et al 1992][research_bjarke_delfrate_1992]\] \[[Bosworth 1992][research_bosworth_1992]\] \[[Bosworth and Cox 1989][research_bosworth_cox_1989]\] \[[Bowers 1981][research_bowers_1981]\] \[[Bowers 1984][research_bowers_1984]\] \[[Breitsamter and Laschka 2001][research_breitsamter_laschka_2001]\] \[[Budd 1984][research_budd_1984]\] \[[Budd 1987][research_budd_1987]\] \[[Calico and Fuller 1981][research_calico_fuller_1981]\] \[[Capone 1981][research_caponefj_1981]\] \[[Chacon and McBride 1988][research_chacon_mcbride_1988]\] \[[Chacon and McBride 1990][research_chacon_mcbride_1990]\] \[[Chen and Dugundji 1987][research_chen_dugundji_1987]\] \[[Chin et al 1982][research_chin_berman_1982]\] \[[Chin et al 1987][research_chinj_chaconv_1987]\] \[[Chipman et al 1984][research_chipmanr_rauchf_1984]\] \[[Chipman et al 1985][research_chipmanr_rauchf_1985]\] \[[Choosak Ngaongam and Rapee Ujjin 2024][research_choosakngaongam_rapeeujjin_2024]\] \[[Clarke et al 1994][research_clarkerobert_burkenjohnj_1994]\] \[[Coe et al 1990][research_coepaulljr_perkinsjohnn_1990]\] \[[Collins 1988][research_collins_1988]\] \[[Cotton and Bjarke 1994][research_cotton_bjarke_1994]\] \[[Croom et al 1988][research_croommarka_whippleraymondd_1988]\] \[[Curry et al 1989][research_curry_moulton_1989]\] \[[Curry et al 1990][research_curry_moulton_1990]\] \[[Dawson and Fortin 1987][research_dawson_fortin_1987]\] \[[Deandrea et al 1991][research_deandrea_roache_1991]\] \[[Del Frate 1992][research_delfrate_1992]\] \[[Delfrate and Saltzman 1992][research_delfrate_saltzman_1992]\] \[[Dillinger et al 2019][research_dillinger_abdalla_2019]\] \[[Doggett and Ricketts 1980][research_doggett_ricketts_1980]\] \[[Earls and Sitz 1989][research_earls_sitz_1989]\] \[[Fehrs and Kaiser 2025][research_fehrs_kaiser_2025]\] \[[Fisher et al 1992][research_fisher_richwine_1992]\] \[[Fratello et al 1987][research_fratello_croom_1987]\] \[[Frei 1982][research_frei_1982]\] \[[Gera 1986][research_gera_1986]\] \[[Gera et al 1987][research_gera_andrisani_1987]\] \[[Gera et al 1989][research_gera_andrisani_1989]\] \[[Gilbert et al 1984][research_gilbert_schmidt_1984]\] \[[Goradia et al 1989][research_goradiash_bobbittpj_1989]\] \[[Grafton et al 1982][research_graftonsb_gilberwp_1982]\] \[[Griffin et al 1983][research_griffin_haerter_1983]\] \[[Griffin et al 2010][research_griffinbrianjoseph_burkenjohnj_2010]\] \[[Guo et al 1988][research_guo_wang_1988]\] \[[Haase et al][research_haase_aslund]\] \[[Hancock and Fullerton 1992][research_hancockregis_fullertongordon_1992]\] \[[Hertz et al 1982][research_hertztj_shirkmh_1982]\] \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\] \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\] \[[Hicks and Matheny 1989][research_hicksjohnw_mathenyneilw_1989]\] \[[Hicks and Moulton 1988][research_hicksjohnw_moultonbryanj_1988]\] \[[Hicks and Petersen 1988][research_hicksjohnw_petersenkevinl_1988]\] \[[Hicks and Petersen 1989][research_hicksjohnw_petersenkevinl_1989]\] \[[Hicks et al 1987][research_hicksjohnw_cooperjamesmjr_1987]\] \[[Hicks et al 1987][research_hicksjohnw_kaniajan_1987]\] \[[Iliff and Wang 1996][research_iliff_wang_1996]\] \[[Ishmael and Wierzbanowski 1985][research_ishmaelsd_wierzbanowskit_1985]\] \[[Ishmael et al 1990][research_ishmaelstephend_smithrogerse_1990]\] \[[Jackuliak and Bugaj 2026][research_jackuliak_bugaj_2026]\] \[[Jiang et al 2011][research_jiang_zhang_2011]\] \[[Hicks et al 1987][research_johnwhicks_jankania_1987]\] \[[Jun-yi et al 2021][research_junyi_xinbing_2021]\] \[[Kanazaki and Setoguchi 2023][research_kanazaki_setoguchi_2023]\] \[[Kehoe et al 1990][research_kehoemichaelw_bjarkelisaj_1990]\] \[[Keller 2019][research_keller_2019]\] \[[Kishi et al 2022][research_kishi_kanazaki_2022]\] \[[Klafin 1988][research_klafin_1988]\] \[[Kohara et al 2016][research_kohara_tomoeda_2016]\] \[[Krone 1980][research_krone_1980_b]\] \[[Krone 1980][research_krone_1980]\] \[[Krüger et al 2014][research_kruger_klimmek_2014]\] \[[Landsberger and Dugundji 1985][research_landsberger_dugundji_1985]\] \[[Lee and Ko 2009][research_lee_ko_2009]\] \[[Li 2023][research_li_2023]\] \[[Li et al 2019][research_li_qian_2019]\] \[[Librescu and Thangjitham 1988][research_librescu_thangjitham_1988]\] \[[Librescu and Thangjitham 1989][research_librescu_thangjitham_1989]\] \[[Librescu and Thangjitham 1991][research_librescu_thangjitham_1991]\] \[[Lokos 1990][research_lokoswilliama_1990]\] \[[Lombardi and Morelli 1994][research_lombardi_morelli_1994]\] \[[Lombardi et al 1996][research_lombardi_morelli_1996]\] \[[Lombardi et al 1997][research_lombardi_salvetti_1997]\] \[[Mann and Mercer 1985][research_mannmj_mercerce_1985]\] \[[Mann and Mercer 1986][research_mannmj_mercerce_1986]\] \[[Marske 1975][research_marske_1975]\] \[[Mason and Capone 1983][research_masonml_caponefj_1983]\] \[[McCormack and Stevens 1947][research_mccormack_stevens_1947]\] \[[Miller 1983][research_miller_1983]\] \[[Miller 1986][research_miller_1986]\] \[[Miller et al 1983][research_miller_wykes_1983]\] \[[Miyakawa et al 1991][research_miyakawa_ohnuki_1991]\] \[[Moore and Frei 1983][research_moore_frei_1983]\] \[[Mourey 1979][research_moureydj_1979]\] \[[Murri et al 1983][research_murridg_croomma_1983]\] \[[Murri et al 1984][research_murridg_nguyenlt_1984]\] \[[Nangia and Palmer 2002][research_nangia_palmer_2002]\] \[[nath and ana 2017][research_nath_ana_2017]\] \[[Noll et al 1984][research_noll_eastep_1984]\] \[[Ouyang et al 2021][research_ouyang_zeng_2021]\] \[[Owens and Perkins 1996][research_owens_perkins_1996]\] \[[Oyibo 1984][research_oyibo_1984]\] \[[Puthisikamani et al 2023][research_puthisikamani_sreenivasaraja_2023]\] \[[Putnam 1983][research_putnamtw_1983]\] \[[Putnam 1984][research_putnamtw_1984]\] \[[Putnam 1984][research_putnamtw_1984_b]\] \[[Putnam et al 1986][research_putnamtw_petersenkl_1986]\] \[[Raney and Batterson 1989][research_raney_batterson_1989]\] \[[Raney 1987][research_raneydavidl_1987]\] \[[Ray et al 1988][research_ray_hicks_1988]\] \[[Ray et al 1990][research_ray_hicks_1990]\] \[[Redeker and Wichmann 1991][research_redeker_wichmann_1991]\] \[[Rhodes and Selberg 1982][research_rhodesmd_selbergbp_1982]\] \[[Rimer et al 1986][research_rimer_chipman_1986]\] \[[Rimer et al 1984][research_rimerm_chipmanr_1984]\] \[[Robinson and Robinson 1980][research_robinson_robinson_1980]\] \[[Rongrong et al 2018][research_rongrong_zhengyin_2018]\] \[[Ross 1984][research_ross_1984]\] \[[Ross and Matarazzo 1982][research_ross_matarazzo_1982]\] \[[Russo et al 1986][research_russo_healy_1986]\] \[[Saheby et al 2026][research_saheby_jialu_2026]\] \[[Saltzman et al 1994][research_saltzmanedwinj_hicksjohnw_1994]\] \[[Sefic and Cutler 1986][research_sefic_cutler_1986]\] \[[Sefic and Maxwell 1986][research_sefic_maxwell_1986]\] \[[Sefic and Maxwell 1987][research_sefic_maxwell_1987]\] \[[Seitz et al 2019][research_seitz_hubner_2019]\] \[[Setoguchi and Kanazaki 2020][research_setoguchi_kanazaki_2020]\] \[[Sharif et al 2022][research_sharif_abbas_2022]\] \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\] \[[Smith and Schroeder 1986][research_smithrogerse_schroederkurtc_1986]\] \[[Spacht 1980][research_spacht_1980]\] \[[Stewart and Bauer 1983][research_stewart_bauer_1983]\] \[[Takahashi et al 2019][research_takahashi_boccieri_2019]\] \[[Taufik and Qasem 2025][research_taufik_qasem_2025]\] \[[Triplett 1980][research_triplett_1980_b]\] \[[Trippensee 1991][research_trippensee_1991]\] \[[Trippensee and Lux 1987][research_trippenseegarya_luxdavidp_1987]\] \[[Trippensee and Lux 1988][research_trippenseegarya_luxdavidp_1988]\] \[[Underwood et al 2003][research_underwoodpamelaj_owenslewisr_2003]\] \[[Valasek and Downing 1995][research_valasek_downing_1995]\] \[[Voracek 1990][research_voracek_1990]\] \[[Voracek and Clarke 1994][research_voracek_clarke_1994]\] \[[Voracek and Clarke 1991][research_voracekdavidf_clarkerobert_1991]\] \[[Waggoner and Bates 1989][research_waggonereg_batesbl_1989]\] \[[Waggoner et al 1986][research_waggonereg_jennettla_1986]\] \[[Walchli et al 1992][research_walchli_guyton_1992]\] \[[Wang et al 2006][research_wang_zhan_2006]\] \[[Wang et al 2017][research_wang_su_2017]\] \[[Wang et al 2018][research_wang_su_2018]\] \[[Wang et al 2025][research_wang_wang_2025_b]\] \[[Wauters 2022][research_wauters_2022]\] \[[Weisshaar 1978][research_weisshaar_1978]\] \[[Weisshaar 1979][research_weisshaar_1979]\] \[[Weisshaar 1985][research_weisshaar_1985]\] \[[Weisshaar and Zeiler 1983][research_weisshaar_zeiler_1983]\] \[[Weisshaar 1983][research_weisshaarta_1983]\] \[[Weisshaar and Zeiler 1982][research_weisshaarta_zeilerta_1982]\] \[[Wissler et al 1987][research_wissler_gilliam_1987]\] \[[X-29 Experiment in Flight 1991][research_x_29_experiment_1991]\] \[[X-29 Research Aircraft 1991][research_x_29_research_1991]\] \[[Xinbing et al 2020][research_xinbing_wen_2020]\] \[[Xue et al 2019][research_xue_ye_2019]\] \[[Yang and Przekwas 1993][research_yang_przekwas_1993]\] \[[Yeh 1988][research_yeh_1988]\] \[[Yeh 1988][research_yeh_1988_b]\] \[[Yeh and Yeh 1989][research_yeh_yeh_1989]\] \[[Zhang et al 2013][research_zhang_yu_2013]\]

**Of the 175 records, 74 titles name the X-29, published from 1982 to 2010, and 65 of those are report primaries.** Of all 175 records, 88 date from 1985 to 1995, the years of the flight programme and its reports.

### Transonic wing design and sweep

Transonic aerofoil and wing design, supercritical sections, transonic buffet and shock control, swept-wing flow and transonic unsteady pressures.

**153 records.** \[[Al-Jaburi et al 2019][research_aljaburi_feszty_2019]\] \[[Allison and Dagenhart 1987][research_allisondenniso_dagenhartjray_1987]\] \[[Andrés-Pérez et al 2016][research_andresperez_gonzalezjuarez_2016]\] \[[Ardema and Williams 1972][research_ardemamd_williamslj_1972]\] \[[Arnault et al 2016][research_arnault_dandois_2016]\] \[[Bergman 1948][research_bergman_1948]\] \[[Blackwell and Pounds 1977][research_blackwell_pounds_1977]\] \[[Bons and Martins 2020][research_bons_martins_2020]\] \[[Boyden 1974][research_boydenrp_1974]\] \[[Cahn and Garcia 1971][research_cahn_garcia_1971]\] \[[Campbell and Smith 1989][research_campbellrichardl_smithleigha_1989]\] \[[Carlson 1976][research_carlson_1976]\] \[[Cebeci 1974][research_cebeci_1974]\] \[[Chaparro et al 2016][research_chaparrodaniel_fujiwaragustavoec_2016]\] \[[Chau and Zingg 2022][research_chau_zingg_2022]\] \[[Chau and Zingg 2023][research_chau_zingg_2023]\] \[[Chau et al 2026][research_chau_piotrowski_2026]\] \[[Chen 1982][research_chen_1982]\] \[[Chen and Tang 2017][research_chen_tang_2017]\] \[[Chen et al 2015][research_chen_zhang_2015]\] \[[Chen et al 2022][research_chen_gao_2022]\] \[[Chen et al 2023][research_chen_gao_2023]\] \[[Cheng et al 1980][research_chenghk_mengsy_1980]\] \[[Droney et al 2020][research_christopherkdroney_anthonyjsclafani_2020]\] \[[Chu and Lawing 1990][research_chujulio_lawingpiercel_1990]\] \[[Clyde et al 1984][research_clyde_bonner_1984]\] \[[Coder 2021][research_coder_2021]\] \[[Coder 2026][research_coder_2026]\] \[[Cole 1988][research_cole_1988_b]\] \[[Cole et al 1980][research_cole_cook_1980]\] \[[Cook 1979][research_cook_1979]\] \[[Currao and Jiang 2026][research_currao_jiang_2026]\] \[[Damodaran and Caughey 1988][research_damodaran_caughey_1988]\] \[[Dandois 2016][research_dandois_2016]\] \[[Deng and Qin 2021][research_deng_qin_2021]\] \[[Deng and Yi 2023][research_deng_yi_2023]\] \[[Deng et al 2023][research_deng_zhang_2023]\] \[[Deng et al 2026][research_deng_yi_2026]\] \[[Design and CFD Analysis of Supercritical Airfoil 0714 Under Ground-Level Atmospheric Conditions 2024][research_design_and_2024]\] \[[Di Pasquale and Prince 2023][research_dipasquale_prince_2023]\] \[[Ecer 1985][research_ecer_1985]\] \[[Erickson 2003][research_ericksongarye_2003]\] \[[Fan et al 2021][research_fan_yu_2021]\] \[[Fung 1982][research_fung_1982]\] \[[Garabedian 1979][research_garabedianpr_1979]\] \[[Geoghegan et al 2020][research_geoghegan_giannelis_2020]\] \[[Guderley 1956][research_guderley_1956]\] \[[Hanman et al 2025][research_hanman_yao_2025]\] \[[Harris 1974][research_harriscd_1974]\] \[[Harris 1974][research_harriscd_1974_b]\] \[[Hess et al 1989][research_hess_seidel_1989]\] \[[Hinchliffe and Qin 2017][research_hinchliffe_qin_2017]\] \[[Holst and Brown 1983][research_holst_brown_1983]\] \[[Hope and Kunz 2019][research_hope_kunz_2019]\] \[[Hortsen et al 1983][research_hortsen_boer_1983]\] \[[Houtman et al 2023][research_houtman_timme_2023]\] \[[Hurley 1975][research_hurley_1975]\] \[[Janardhan and Grandhi 2003][research_janardhan_grandhi_2003]\] \[[Ji et al 2025][research_ji_yang_2025]\] \[[Jiang et al 2018][research_jiang_tian_2018]\] \[[Jiang et al 2019][research_jiang_tian_2019]\] \[[Jones and Jarrett 2018][research_jones_jarrett_2018]\] \[[Jou and Metcalfe 1984][research_jou_metcalfe_1984]\] \[[Kakkar et al 2026][research_kakkar_streit_2026]\] \[[Kasim Biber and Trenton White 2019][research_kasimbiber_trentonwhite_2019]\] \[[King and Johnson 1986][research_king_johnson_1986]\] \[[Kishi et al 2016][research_kishi_kanazaki_2016]\] \[[Koenig 1984][research_koenig_1984]\] \[[Lee and Eyi 1993][research_lee_eyi_1993]\] \[[Lee and Ohman 1984][research_lee_ohman_1984]\] \[[Lee and Tang 1989][research_lee_tang_1989]\] \[[Lei et al 2021][research_lei_bai_2021]\] \[[Li et al 2019][research_li_he_2019]\] \[[Li et al 2020][research_li_wang_2020]\] \[[Li et al 2024][research_li_zhang_2024_d]\] \[[Lifshits and Ryzhov 1978][research_lifshits_ryzhov_1978]\] \[[Liu et al 2016][research_liu_song_2016]\] \[[Liu et al 2024][research_liu_zhang_2024]\] \[[Magnus and Yoshihara 1975][research_magnus_yoshihara_1975]\] \[[Mann et al 1983][research_mannmj_campbellrl_1983]\] \[[Mann et al 1984][research_mannmj_campbellrl_1984]\] \[[Masini et al 2019][research_masini_timme_2019]\] \[[Masini et al 2020][research_masini_timme_2020]\] \[[Mateer et al 1987][research_mateergeorgec_seegmillerhlee_1987]\] \[[Mayer et al 2019][research_mayer_lutz_2019]\] \[[Mazaheri and Nejati 2015][research_mazaheri_nejati_2015]\] \[[Mazaheri et al 2015][research_mazaheri_kiani_2015]\] \[[Mazaheri et al 2015][research_mazaheri_nejati_2015_b]\] \[[Mazaheri et al 2016][research_mazaheri_nejati_2016]\] \[[Mazaheri et al 2017][research_mazaheri_nejati_2017]\] \[[Maślanka et al 2025][research_maslanka_kachel_2025]\] \[[Nakamura 1982][research_nakamura_1982]\] \[[Nazarenko and Nevezhina 1972][research_nazarenko_nevezhina_1972]\] \[[Niu and Li 2022][research_niu_li_2022]\] \[[Ntantis and Xezonakis 2024][research_ntantis_xezonakis_2024]\] \[[Olsen 1966][research_olsen_1966]\] \[[Park et al 2026][research_park_kang_2026]\] \[[Paul and Rein 2017][research_paul_rein_2017]\] \[[Pelykh and Andryushchenko 2024][research_pelykh_andryushchenko_2024]\] \[[Persoon et al 1980][research_persoon_roos_1980]\] \[[Pham 2022][research_pham_2022]\] \[[Placek and Ruchała 2018][research_placek_ruchala_2018]\] \[[Plotkin 1978][research_plotkin_1978]\] \[[Poole et al 2026][research_poole_allen_2026]\] \[[Quagliarella and Iuliano 2017][research_quagliarella_iuliano_2017]\] \[[Ricketts et al 1983][research_rickettsrh_sandfordmc_1983]\] \[[Ricketts et al 1983][research_rickettsrh_watsonjj_1983]\] \[[Roberts et al 2015][research_roberts_reed_2015]\] \[[Rodemich and Andrew 1965][research_rodemich_andrew_1965]\] \[[Rose and Seginer 1978][research_rose_seginer_1978]\] \[[Ruo et al 1985][research_ruo_malone_1985]\] \[[Sabater et al 2022][research_sabater_bekemeyer_2022]\] \[[Viken et al 2022][research_sallyaviken_craigahunter_2022]\] \[[Samputh et al 2024][research_samputh_moey_2024]\] \[[Sato 1973][research_sato_1973]\] \[[Seidel et al 1987][research_seidel_sandford_1987]\] \[[Seidel et al 1985][research_seidelda_sandfordmc_1985]\] \[[Serani et al 2024][research_serani_diez_2024]\] \[[Singh and Dwivedi 2022][research_singh_dwivedi_2022]\] \[[Smetana 1973][research_smetana_1973]\] \[[Sobieczky 1984][research_sobieczky_1984]\] \[[Stanewsky and Little 1971][research_stanewsky_little_1971]\] \[[Streit et al 2015][research_streit_wedler_2015]\] \[[Sudhi et al 2023][research_sudhi_radespiel_2023]\] \[[Sun et al 2020][research_sun_miao_2020]\] \[[Sun et al 2026][research_sun_zhang_2026]\] \[[Surwase and Kumar 2025][research_surwase_kumar_2025]\] \[[Tang et al 2017][research_tang_chen_2017]\] \[[Tian et al 2017][research_tian_gao_2017]\] \[[Tian et al 2023][research_tian_jin_2023]\] \[[Ting et al 2018][research_ting_chaparro_2018]\] \[[Tsushima et al 2021][research_tsushima_saitoh_2021]\] \[[Van Den Berg et al 1975][research_vandenberg_elsenaar_1975]\] \[[Velkova 2017][research_velkova_2017]\] \[[Weed et al 1983][research_weed_carlson_1983]\] \[[Williams 1980][research_williams_1980]\] \[[Wing Buffeting Control at Transonic Flight Velocities with the Use of Ejector-Type Pulse Thermal Actuators 2018][research_wing_buffeting_2018]\] \[[Wu and Squires 1995][research_wu_squires_1995]\] \[[Wu et al 2022][research_wu_zuo_2022]\] \[[Xu et al 2019][research_xu_saleh_2019]\] \[[Xu et al 2019][research_xu_han_2019]\] \[[Yang et al 2025][research_yang_wu_2025]\] \[[Yang et al 2026][research_yang_tang_2026]\] \[[Zauner and Sandham 2020][research_zauner_sandham_2020]\] \[[Zauner et al 2023][research_zauner_moise_2023]\] \[[Zhang et al 2015][research_zhang_fang_2015]\] \[[Zhang et al 2021][research_zhang_yang_2021]\] \[[Zhang et al 2022][research_zhang_deng_2022]\] \[[Zhang et al 2026][research_zhang_deng_2026]\] \[[Zhao et al 2016][research_zhao_zhang_2016]\] \[[Zhong et al 2026][research_zhong_wang_2026]\] \[[Zhou et al 2017][research_zhou_chen_2017]\] \[[Zhu et al 2019][research_zhu_li_2019]\]

### High angle of attack and vortex flow

High angle of attack aerodynamics and control, vortex flow and vortex breakdown, post-stall flight and thrust vectoring.

**145 records.** \[[A feasibility review of SMC-MIMO based control architecture for high angle of attack flight 2019][research_a_feasibility_2019]\] \[[A Spreadsheet Tool for the AERODAS Model for Calculating Airfoil Pre-Stall and Post-Stall Lift and Drag Characteristics 2018][research_a_spreadsheet_2018]\] \[[Ahmed et al 2025][research_ahmed_elbanna_2025]\] \[[Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]\] \[[Almosnino 1985][research_almosnino_1985]\] \[[Altunkaya and Özkol 2025][research_altunkaya_ozkol_2025]\] \[[Axelson 1977][research_axelson_1977]\] \[[Bagherzadeh 2026][research_bagherzadeh_2026]\] \[[Bagherzadeh et al 2025][research_bagherzadeh_mohammadkarimi_2025]\] \[[Banks 1988][research_banksdanielw_1988]\] \[[Ben-Gida and Gurka 2022][research_bengida_gurka_2022]\] \[[Bihrle and Billy 1980][research_bihrle_jr_1980]\] \[[Briggs et al 1982][research_briggs_reed_1982]\] \[[Buffington and Adams 1995][research_buffington_adams_1995]\] \[[Buzica et al 2018][research_buzica_biswanger_2018]\] \[[Cen et al 2020][research_cen_li_2020]\] \[[Chin 1989][research_chin_1989]\] \[[Clark and Spurlin 1962][research_clark_spurlin_1962]\] \[[Cornelius and Lucius 1994][research_cornelius_lucius_1994]\] \[[Cunis et al 2019][research_cunis_burlion_2019]\] \[[Cunis et al 2020][research_cunis_condomines_2020_b]\] \[[Richwine and Fisher 1992][research_davidmrichwine_davidffisher_1992]\] \[[Dawe et al 2025][research_dawe_bull_2025]\] \[[Dexter 1993][research_dexter_1993]\] \[[Dodayav et al 2024][research_dodayav_biswas_2024]\] \[[Ekaterinaris and Schiff 1990][research_ekaterinarisja_schifflewisb_1990]\] \[[Ekaterinaris and Schiff 1994][research_ekaterinarisja_schifflewisb_1994]\] \[[Esfahani et al 2018][research_esfahani_webb_2018]\] \[[Experimental investigation of synthetic jet control of wing rock for a flying wing aircraft 2023][research_experimental_investigation_2023]\] \[[Faure et al 2019][research_faure_dumas_2019]\] \[[Favier et al 1987][research_favier_maresca_1987]\] \[[Fujii 1985][research_fujii_1985]\] \[[Golmirzaee and Wood 2026][research_golmirzaee_wood_2026]\] \[[Hadidoolabi and Ansarian 2017][research_hadidoolabi_ansarian_2017]\] \[[Hadidoolabi and Ansarian 2018][research_hadidoolabi_ansarian_2018]\] \[[Hemsch 1989][research_hemsch_1989]\] \[[Hirato et al 2019][research_hirato_shen_2019]\] \[[Hitzel 2017][research_hitzel_2017]\] \[[Huang et al 2026][research_huang_li_2026]\] \[[Jiang et al 2024][research_jiang_li_2024]\] \[[Johari et al 1995][research_johari_olinger_1995]\] \[[Johnston et al 1974][research_johnston_ashkenas_1974]\] \[[Kolb et al 2019][research_kolb_montagnier_2019]\] \[[Kurade et al 2021][research_kurade_venkatakrishnan_2021]\] \[[Lamar 1978][research_lamarje_1978]\] \[[Lamar and Frink 1981][research_lamarje_frinknt_1981]\] \[[Lamar and Frink 1981][research_lamarje_frinknt_1981_b]\] \[[Lamar and Luckring 1979][research_lamarje_luckringjm_1979]\] \[[Lamar et al 1980][research_lamarje_schemenskyrt_1980]\] \[[Lan and Tseng 1987][research_lancedward_tsengjb_1987]\] \[[Lee 2016][research_lee_2016]\] \[[Lee and Ko 2018][research_lee_ko_2018]\] \[[Lee and Singh 2017][research_lee_singh_2017]\] \[[Lemay et al 1988][research_lemaysp_batillsm_1988]\] \[[Li and Yang 2017][research_li_yang_2017]\] \[[Li et al 2017][research_li_jin_2017]\] \[[Li et al 2021][research_li_wang_2021]\] \[[Li et al 2025][research_li_hu_2025]\] \[[Li et al 2025][research_li_ji_2025]\] \[[Liu et al 2018][research_liu_luo_2018]\] \[[Liu et al 2019][research_liu_chen_2019]\] \[[Liu et al 2024][research_liu_ji_2024]\] \[[Nguyen et al 1980][research_luattnguyen_williampgilbert_1980]\] \[[Lyu et al 2018][research_lyu_cao_2018]\] \[[Lyu et al 2019][research_lyu_zhang_2019]\] \[[Ma et al 2015][research_ma_guo_2015]\] \[[Magness et al 1993][research_magness_robinson_1993]\] \[[Mahgoub and Cortelezzi 2020][research_mahgoub_cortelezzi_2020]\] \[[Malik et al 2017][research_malik_akhtar_2017]\] \[[Mamonova et al 2019][research_mamonova_soudakov_2019]\] \[[Manzoor et al 2016][research_manzoor_maqsood_2016]\] \[[Mareca Rios et al 2023][research_marecarios_montesbarrenetxea_2023]\] \[[Ogburn et al 1991][research_marilyneogburn_johnvfoster_1991]\] \[[McKeehen and Cord 1997][research_mckeehen_cord_1997]\] \[[Menet et al 1993][research_menet_menart_1993]\] \[[Menon and Yousefpor 1996][research_menon_yousefpor_1996]\] \[[Mitchell et al 1980][research_mitchell_myers_1980]\] \[[Mobayen and Izadbakhsh 2025][research_mobayen_izadbakhsh_2025]\] \[[Muir et al 2017][research_muir_arredondogaleana_2017]\] \[[Narayanan et al 2026][research_narayanan_kumar_2026]\] \[[Nelson and Mouch 1978][research_nelson_mouch_1978]\] \[[Numerical Analysis of the Flow Pattern and Vortex Breakdown over a Pitching Delta wing at Supersonic Speeds 2017][research_numerical_analysis_2017]\] \[[Numerical Study of Geometrical Properties of Full-Span Tubercle Leading Edge Wing at Post-Stall Condition 2023][research_numerical_study_2023]\] \[[Oberkampf and Nicolaides 1971][research_oberkampf_nicolaides_1971]\] \[[Orkwis 1995][research_orkwis_1995]\] \[[Orlik-Ruckemann 1983][research_orlikruckemann_1983]\] \[[Osipov 2016][research_osipov_2016]\] \[[Osipov 2017][research_osipov_2017]\] \[[Osipov 2019][research_osipov_2019]\] \[[Peng et al 2026][research_peng_cao_2026]\] \[[Pfnür and Breitsamter 2019][research_pfnur_breitsamter_2019]\] \[[Poll 1986][research_poll_1986]\] \[[Ragab et al 2018][research_ragab_hajj_2018]\] \[[Rainbird et al 2015][research_rainbird_peiro_2015]\] \[[Reddy 1987][research_reddy_1987]\] \[[Richwine and Fisher 1991][research_richwinedavidm_fisherdavidf_1991]\] \[[Rockwell 1994][research_rockwell_1994]\] \[[Rohith and Sinha 2020][research_rohith_sinha_2020]\] \[[Sahin et al 2026][research_sahin_yayla_2026]\] \[[Sahu et al 2000][research_sahu_heavey_2000]\] \[[Salahudden 2025][research_salahudden_2025]\] \[[Sellers et al 1988][research_sellerswilliamliii_meyersjamesf_1988]\] \[[Sellers et al 2004][research_sellerswilliamliii_meyersjamesf_2004]\] \[[Shen and Chen 2022][research_shen_chen_2022]\] \[[Shen and Chen 2024][research_shen_chen_2024]\] \[[Shen and Wen 2018][research_shen_wen_2018]\] \[[Shi et al 2019][research_shi_lyu_2019]\] \[[Shivam and Verma 2019][research_shivam_verma_2019]\] \[[Shojae et al 2025][research_shojae_salehi_2025]\] \[[Son et al 2015][research_son_sa_2015]\] \[[Son et al 2015][research_son_sa_2015_b]\] \[[Sternberg et al 1994][research_sternberg_traven_1994]\] \[[Stollery 1992][research_stollery_1992]\] \[[Tahir et al 2026][research_tahir_maqsood_2026]\] \[[Tan et al 2021][research_tan_wang_2021]\] \[[Telionis 1995][research_telionis_1995]\] \[[Telionis 2001][research_telionis_2001]\] \[[Theisen et al 1973][research_theisen_scruggs_1973]\] \[[Van Dommelen 1995][research_vandommelen_1995]\] \[[Van Tuyl 1988][research_vantuyl_1988]\] \[[Vlahostergios et al 2018][research_vlahostergios_komnos_2018]\] \[[Walchli 1994][research_walchlilawrencea_1994]\] \[[Wang et al 2016][research_wang_gao_2016]\] \[[Wang et al 2021][research_wang_ma_2021]\] \[[Wang et al 2025][research_wang_luo_2025]\] \[[Wang et al 2025][research_wang_luo_2025_b]\] \[[Wang et al 2025][research_wang_luo_2025_c]\] \[[Wang et al 2026][research_wang_li_2026]\] \[[Wardlaw et al 1975][research_wardlaw_andrewb_1975]\] \[[Wei et al 2017][research_wei_chen_2017]\] \[[Wilson et al 1994][research_wilsondavidj_citurskevind_1994]\] \[[Wood and Miller 1985][research_woodrm_millerds_1985]\] \[[Wu et al 2017][research_wu_chen_2017]\] \[[Wu et al 2020][research_wu_chen_2020]\] \[[Wu et al 2021][research_wu_sun_2021]\] \[[Yang et al 2025][research_yang_wang_2025]\] \[[Ye et al 2015][research_ye_chen_2015]\] \[[Yu and Yu 2026][research_yu_yu_2026]\] \[[Zhang et al 2017][research_zhang_zhang_2017]\] \[[Zhang et al 2022][research_zhang_wang_2022_b]\] \[[Zhao et al 2026][research_zhao_liu_2026_b]\] \[[Zhou et al 2019][research_zhou_dowell_2019]\] \[[Zhu et al 2022][research_zhu_shi_2022]\] \[[Zohar and Er-El 1988][research_zohar_erel_1988]\] \[[Özkan 2020][research_ozkan_2020]\]

### Morphing and adaptive structures

Morphing wings, variable camber and adaptive structures.

**123 records.** \[[Aamir et al 2026][research_aamir_abbasi_2026]\] \[[Ajaj et al 2021][research_ajaj_parancheerivilakkathil_2021]\] \[[Alsaidi et al 2019][research_alsaidi_joe_2019]\] \[[Alsaidi et al 2019][research_alsaidi_joe_2019_b]\] \[[Application Status and Future Prospect of Aircraft Morphing Wing 2023][research_application_status_2023]\] \[[Babu et al 2026][research_babu_khan_2026]\] \[[Badihi et al 2026][research_badihi_nezhad_2026]\] \[[Bartels et al 2019][research_bartelsroberte_stanfordbretk_2019]\] \[[Bashir et al 2021][research_bashir_longtinmartel_2021]\] \[[Bashir et al 2024][research_bashir_negahban_2024]\] \[[Bataineh and Shawabkeh 2023][research_bataineh_shawabkeh_2023]\] \[[Battaglia and Riccio 2026][research_battaglia_riccio_2026]\] \[[Beatty et al 1977][research_beatty_brooks_1977]\] \[[Bhattacharyya et al 2019][research_bhattacharyya_conlansmith_2019]\] \[[Bradley et al 2026][research_bradley_haughn_2026]\] \[[Burdette and Martins 2018][research_burdette_martins_2018]\] \[[Changchuan et al 2022][research_changchuan_zhiying_2022]\] \[[Chen et al 2026][research_chen_wang_2026]\] \[[Clark 2001][research_clark_2001]\] \[[Clements and Djidjeli 2023][research_clements_djidjeli_2023]\] \[[Coban 2020][research_coban_2020]\] \[[Contell Asins et al 2021][research_contellasins_landersheim_2021]\] \[[Dai et al 2025][research_dai_hu_2025]\] \[[De Gaspari et al 2018][research_degaspari_riccobene_2018]\] \[[Dexl et al 2020][research_dexl_hauffe_2020]\] \[[Ding and Zhou 2018][research_ding_zhou_2018]\] \[[El-Salamony and Aziz 2020][research_elsalamony_aziz_2020]\] \[[Eraslan and Oktay 2023][research_eraslan_oktay_2023]\] \[[Feng et al 2023][research_feng_guo_2023]\] \[[Fichera et al 2019][research_fichera_isnardi_2019]\] \[[Gong et al 2019][research_gong_wang_2019]\] \[[Gu and Hong 2020][research_gu_hong_2020]\] \[[Guo et al 2017][research_guo_bai_2017]\] \[[Guo et al 2017][research_guo_hou_2017]\] \[[Guo et al 2025][research_guo_wang_2025]\] \[[Hu et al 2016][research_hu_yang_2016]\] \[[Hua et al 2025][research_hua_wang_2025]\] \[[Hübler et al 2016][research_hubler_nissle_2016]\] \[[Jin and Xue 2026][research_jin_xue_2026]\] \[[Jo and Majid 2023][research_jo_majid_2023]\] \[[Joshi et al 2026][research_joshi_kalra_2026]\] \[[Kambayashi and Kogiso 2026][research_kambayashi_kogiso_2026]\] \[[Karimi Kelayeh and Djavareshkian 2024][research_karimikelayeh_djavareshkian_2024]\] \[[Kaul and Nguyen 2018][research_kaul_nguyen_2018]\] \[[Kaygan and Ulusoy 2018][research_kaygan_ulusoy_2018]\] \[[Keidel et al 2020][research_keidel_fasel_2020]\] \[[Klimczyk and Goraj 2019][research_klimczyk_goraj_2019]\] \[[Koyuncuoglu and He 2022][research_koyuncuoglu_he_2022]\] \[[Kuder et al 2015][research_kuder_arrieta_2015]\] \[[Lee and Sheikh 2025][research_lee_sheikh_2025]\] \[[Lendraitis 2019][research_lendraitis_2019]\] \[[Lendraitis and Lukoševičius 2023][research_lendraitis_lukosevicius_2023]\] \[[Lendraitis and Lukoševičius 2025][research_lendraitis_lukosevicius_2025]\] \[[Li et al 2024][research_li_zhang_2024]\] \[[Lin and Crawley 1995][research_lin_crawley_1995]\] \[[Liu et al 2026][research_liu_qian_2026]\] \[[Lu et al 2017][research_lu_tian_2017]\] \[[Lyu and Martins 2015][research_lyu_martins_2015]\] \[[Ma et al 2025][research_ma_zhou_2025]\] \[[Mao et al 2019][research_mao_xie_2019]\] \[[Michaud et al 2018][research_michaud_dalir_2018]\] \[[Mkhoyan et al 2022][research_mkhoyan_thakrar_2022]\] \[[Moens 2019][research_moens_2019]\] \[[Morton et al 2023][research_morton_xu_2023]\] \[[Nazeer et al 2021][research_nazeer_wang_2021]\] \[[Negahban et al 2024][research_negahban_bashir_2024]\] \[[Nguyen et al 2018][research_nguyen_reynolds_2018]\] \[[Nguyen and Urnes 2012][research_nguyennhan_jamesurnessr_2012]\] \[[Nguyen et al 2015][research_nguyennhan_kaulupender_2015]\] \[[Olivett et al 2021][research_olivett_corrao_2021]\] \[[Ozbek et al 2024][research_ozbek_ekici_2024]\] \[[Shah et al 2023][research_parthivnshah_ericlblades_2023]\] \[[Patel et al 2022][research_patel_kumar_2022]\] \[[Rea et al 2018][research_rea_pecora_2018]\] \[[Reist et al 2022][research_reist_koo_2022]\] \[[Rivero et al 2021][research_rivero_fournier_2021]\] \[[Rodinò and Maletta 2024][research_rodino_maletta_2024]\] \[[Roy and Mukherjee 2026][research_roy_mukherjee_2026]\] \[[Runkel et al 2018][research_runkel_fasel_2018]\] \[[Sabri et al 2022][research_sabri_elzaabalawy_2022]\] \[[Sheikh et al 2023][research_sheikh_lee_2023]\] \[[Shen et al 2015][research_shen_bai_2015]\] \[[Shi and Wan 2015][research_shi_wan_2015]\] \[[Sivanandi et al 2025][research_sivanandi_sanjay_2025]\] \[[Su et al 2016][research_su_swei_2016]\] \[[Svoboda et al 2023][research_svoboda_hengstermovric_2023]\] \[[Syed et al 2022][research_syed_moshtaghzadeh_2022]\] \[[Takahashi et al 2016][research_takahashi_yokozeki_2016]\] \[[Tarnowski 2017][research_tarnowski_2017]\] \[[Ting et al 2015][research_tingeric_daotung_2015]\] \[[Traub 2019][research_traub_2019]\] \[[Tsushima et al 2018][research_tsushima_arizono_2018]\] \[[Tsushima et al 2019][research_tsushima_arizono_2019]\] \[[Tsushima et al 2019][research_tsushima_yokozeki_2019]\] \[[Uzun and Oktay 2023][research_uzun_oktay_2023]\] \[[Wang 2026][research_wang_2026]\] \[[Wang et al 2021][research_wang_mkhoyan_2021]\] \[[Wang et al 2025][research_wang_feng_2025]\] \[[Webb et al 1988][research_webblannied_mccainwilliame_1988]\] \[[Weisshaar and Ehlers 1992][research_weisshaarterrencea_ehlersstevenm_1992]\] \[[Woods et al 2015][research_woods_dayyani_2015]\] \[[Wu and Xu 2023][research_wu_xu_2023]\] \[[Wu et al 2017][research_wu_xiao_2017]\] \[[Xiang et al 2018][research_xiang_liu_2018]\] \[[Xijuan et al 2016][research_xijuan_qiang_2016]\] \[[Xu et al 2018][research_xu_zhang_2018]\] \[[Yan et al 2025][research_yan_han_2025]\] \[[Yang et al 2024][research_yang_xiao_2024]\] \[[Yang et al 2024][research_yang_xu_2024]\] \[[You et al 2020][research_you_kim_2020]\] \[[Yu et al 2024][research_yu_zhou_2024]\] \[[Yue et al 2017][research_yue_zhang_2017]\] \[[Zha et al 2026][research_zha_qiao_2026]\] \[[Zhang and Wang 2019][research_zhang_wang_2019]\] \[[Zhang and Zhao 2023][research_zhang_zhao_2023]\] \[[Zhang et al 2015][research_zhang_zhou_2015]\] \[[Zhang et al 2021][research_zhang_shaw_2021]\] \[[Zhang et al 2025][research_zhang_yang_2025]\] \[[Zhou and Huang 2021][research_zhou_huang_2021]\] \[[Zhu et al 2024][research_zhu_zhang_2024]\] \[[Zhu et al 2025][research_zhu_zhou_2025]\] \[[Şahin and Yaman 2018][research_sahin_yaman_2018]\] \[[Şahin and Yaman 2018][research_sahin_yaman_2018_b]\]

**117 of the 123 records date from 2015 or later.**

### Aerostructural and aerodynamic design optimisation

Aerostructural and aerodynamic shape optimisation of wings and aircraft, including optimisation under aeroelastic constraints.

**118 records.** \[[Abdul-Kaiyoom et al 2025][research_abdulkaiyoom_yildirim_2025]\] \[[Adler and Martins 2023][research_adler_martins_2023]\] \[[Aero structural optimization for sailplane wing in preliminary design 2018][research_aero_structural_2018]\] \[[Ariyarit and Kanazaki 2017][research_ariyarit_kanazaki_2017]\] \[[Bahamonde Jacome and Elham 2017][research_bahamondejacome_elham_2017]\] \[[Benaouali and Boutemedjet 2024][research_benaouali_boutemedjet_2024]\] \[[Bombardieri et al 2021][research_bombardieri_cavallaro_2021]\] \[[Bons et al 2022][research_bons_martins_2022]\] \[[Bowman et al 1989][research_bowmankeithb_grandhiramanav_1989]\] \[[Brooks et al 2019][research_brooks_martins_2019]\] \[[Bryson and Rumpfkeil 2019][research_bryson_rumpfkeil_2019]\] \[[Bugała 2025][research_bugala_2025]\] \[[Bugała and Payenskyy 2025][research_bugala_payenskyy_2025]\] \[[Chauhan and Martins 2021][research_chauhan_martins_2021]\] \[[Chauhan and Martins 2024][research_chauhan_martins_2024]\] \[[Chauhan et al 2023][research_chauhan_praveen_2023]\] \[[Chen et al 2023][research_chen_rao_2023]\] \[[Choi and Park 2019][research_choi_park_2019]\] \[[Conlan-Smith and Andreasen 2022][research_conlansmith_andreasen_2022]\] \[[Cui et al 2025][research_cui_he_2025]\] \[[Dababneh et al 2018][research_dababneh_kipouros_2018]\] \[[De et al 2019][research_de_jrad_2019]\] \[[Demir et al 2023][research_demir_gorguluarslan_2023]\] \[[Design Optimization for SG6043 Airfoil for Using Finite Elements Analysis 2025][research_design_optimization_2025]\] \[[Dinler 2025][research_dinler_2025]\] \[[Elham 2015][research_elham_2015]\] \[[Elham and van Tooren 2016][research_elham_vantooren_2016]\] \[[Elham and van Tooren 2016][research_elham_vantooren_2016_b]\] \[[Feng 2023][research_feng_2023]\] \[[Filippou et al 2024][research_filippou_kilimtzidis_2024]\] \[[Fontana et al 2024][research_fontana_piperni_2024]\] \[[Garner et al 2023][research_garner_wu_2023]\] \[[Gray et al 2025][research_gray_kennedy_2025]\] \[[Guo et al 2021][research_guo_li_2021]\] \[[Gurdal 2002][research_gurdal_2002]\] \[[Gurdal et al 1999][research_gurdal_haftka_1999]\] \[[Hoogervorst and Elham 2017][research_hoogervorst_elham_2017]\] \[[Hu et al 2025][research_hu_an_2025]\] \[[Jacome and Elham 2018][research_jacome_elham_2018]\] \[[Jelovica and Cai 2022][research_jelovica_cai_2022]\] \[[Kafkas et al 2021][research_kafkas_kilimtzidis_2021]\] \[[Kalinowski 2015][research_kalinowski_2015]\] \[[Kambampati and Smith 2017][research_kambampati_smith_2017]\] \[[Kano et al 2025][research_kano_ryuzono_2025]\] \[[Kapania et al 1997][research_kapaniarakeshk_issacj_1997]\] \[[Kenway and Martins 2016][research_kenway_martins_2016]\] \[[Kilimtzidis and Kostopoulos 2023][research_kilimtzidis_kostopoulos_2023]\] \[[Kontogiannis et al 2024][research_kontogiannis_savill_2024]\] \[[Lei et al 2019][research_lei_bai_2019]\] \[[Li and Zhang 2021][research_li_zhang_2021]\] \[[Li and Zhang 2021][research_li_zhang_2021_b]\] \[[Li et al 2018][research_li_bai_2018]\] \[[Li et al 2019][research_li_bai_2019]\] \[[Li et al 2019][research_li_daronch_2019]\] \[[Li et al 2021][research_li_wan_2021]\] \[[Li et al 2022][research_li_bai_2022]\] \[[Li et al 2022][research_li_zhang_2022]\] \[[Li et al 2023][research_li_yang_2023]\] \[[Li et al 2024][research_li_kou_2024]\] \[[Li and Pak 2014][research_liwesleyw_pakchangi_2014]\] \[[Liu and He 2018][research_liu_he_2018]\] \[[Liu et al 2017][research_liu_bai_2017]\] \[[Lv et al 2019][research_lv_lei_2019]\] \[[Lyu et al 2015][research_lyu_kenway_2015]\] \[[Ma et al 2023][research_ma_abouhamzeh_2023]\] \[[Ma et al 2024][research_ma_abouhamzeh_2024]\] \[[Matos and Marta 2025][research_matos_marta_2025]\] \[[McDonnell and Ning 2020][research_mcdonnell_ning_2020]\] \[[Miura and Neill 1992][research_miurahirokazu_neilldouglasj_1992]\] \[[Mohammad Zadeh and Sayadi 2018][research_mohammadzadeh_sayadi_2018]\] \[[Moon 1996][research_moon_1996]\] \[[Navrátil 2017][research_navratil_2017]\] \[[Nejati and Mazaheri 2017][research_nejati_mazaheri_2017]\] \[[Nikolaev 2019][research_nikolaev_2019]\] \[[Nikolaou et al 2026][research_nikolaou_kilimtzidis_2026]\] \[[Oza and Vala 2021][research_oza_vala_2021]\] \[[Phuekpan et al 2025][research_phuekpan_khammee_2025]\] \[[Poole et al 2022][research_poole_allen_2022]\] \[[Rais-Rohani et al 1992][research_raisrohanim_haftkart_1992]\] \[[Rais-Rohani 1999][research_raisrohanimasound_1999]\] \[[Rajpal et al 2019][research_rajpal_kassapoglou_2019]\] \[[Rao et al 2023][research_rao_shi_2023]\] \[[Rashmikant and Abe 2026][research_rashmikant_abe_2026]\] \[[Reist et al 2019][research_reist_zingg_2019]\] \[[Reist et al 2020][research_reist_koo_2020]\] \[[Ringertz 1994][research_ringertz_1994]\] \[[Saporito et al 2023][research_saporito_daronch_2023]\] \[[Sheshanarayana et al 2026][research_sheshanarayana_armstrong_2026]\] \[[Shi et al 2021][research_shi_mader_2021]\] \[[Shi et al 2023][research_shi_lan_2023]\] \[[Shimoda et al 2018][research_shimoda_nagano_2018]\] \[[Shinde et al 2021][research_shinde_ohol_2021]\] \[[Stodieck et al 2018][research_stodieck_cooper_2018]\] \[[Sun 2024][research_sun_2024]\] \[[Sun et al 2026][research_sun_chen_2026]\] \[[Tsiakas et al 2024][research_tsiakas_trompoukis_2024]\] \[[van den Kieboom and Elham 2017][research_vandenkieboom_elham_2017]\] \[[Wang et al 2021][research_wang_peeters_2021]\] \[[Wansasueb et al 2023][research_wansasueb_panagant_2023]\] \[[Wollner 1972][research_wollner_1972]\] \[[Wunderlich 2015][research_wunderlich_2015]\] \[[Wunderlich et al 2021][research_wunderlich_dahne_2021]\] \[[Xia and Chen 2015][research_xia_chen_2015]\] \[[Xie et al 2017][research_xie_meng_2017]\] \[[Xu and Xia 2016][research_xu_xia_2016]\] \[[Xu et al 2026][research_xu_zhang_2026]\] \[[Yang et al 2015][research_yang_yue_2015]\] \[[Yang et al 2026][research_yang_li_2026]\] \[[Yu 2018][research_yu_2018]\] \[[Yu et al 2018][research_yu_lyu_2018]\] \[[Zhang and Rizzi 2017][research_zhang_rizzi_2017]\] \[[Zhang et al 2018][research_zhang_han_2018]\] \[[Zhang et al 2020][research_zhang_wang_2020]\] \[[Zhang et al 2024][research_zhang_zhou_2024]\] \[[Zhao and Cheng 2019][research_zhao_cheng_2019]\] \[[Ziakos et al 2025][research_ziakos_kilimtzidis_2025]\] \[[Zou et al 2017][research_zou_yao_2017]\] \[[Zuo et al 2015][research_zuo_chen_2015]\]

### Flight test, instrumentation and identification

Flight test method, the identification of stability and control derivatives from flight data, wind tunnel technique, and the measurement of wing deformation in flight.

**107 records.** \[[Abele and Sanlorenzo 1975][research_abele_sanlorenzo_1975]\] \[[Abele et al 1973][research_abele_ruger_1973]\] \[[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]\] \[[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967]\] \[[Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967_b]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_d]\] \[[Air Force Test Pilot School Edwards Afb Ca 1993][research_airforcetestpilotschooledwardsafbca_1993]\] \[[Alexander 1991][research_alexander_1991]\] \[[Arif and Sasongko 2021][research_arif_sasongko_2021]\] \[[Armstrong 1977][research_armstrong_1977]\] \[[Bakunowicz and Meyer 2016][research_bakunowicz_meyer_2016]\] \[[Balatti et al 2021][research_balatti_haddadkhodaparast_2021]\] \[[Bantscheff and Breitsamter 2023][research_bantscheff_breitsamter_2023]\] \[[Batterson and Omara 1989][research_battersonjamesg_omarathomasm_1989]\] \[[Beharie et al 2015][research_beharie_pedro_2015]\] \[[Bennett et al 1977][research_bennettrm_farmermg_1977]\] \[[Beyers 1988][research_beyers_1988]\] \[[Billingsley 1976][research_billingsley_1976]\] \[[Binion 1971][research_binion_tw_1971]\] \[[Binion 1975][research_binion_tw_1975]\] \[[Bliss 1980][research_bliss_1980]\] \[[Boden et al 2013][research_boden_lanari_2013]\] \[[Boden et al 2013][research_boden_jentink_2013]\] \[[Brooks and Beamish 1977][research_brooksjd_beamishjk_1977]\] \[[Burner and Martinson 1996][research_burner_martinson_1996]\] \[[Burt 1975][research_burt_1975]\] \[[Butler 1976][research_butler_1976]\] \[[Carico 1998][research_carico_1998]\] \[[Chen et al 2017][research_chen_zhang_2017]\] \[[Chen et al 2024][research_chen_li_2024]\] \[[Clarke et al 1982][research_clarker_shaned_1982]\] \[[Cohen and Le 1991][research_cohendorothea_lejeanetteh_1991]\] \[[Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornellaeronauticallabincbuffalony_1947]\] \[[Czysz 1963][research_czysz_1963]\] \[[De Wagter and Meulenbeld 2019][research_dewagter_meulenbeld_2019]\] \[[Deangelis 1981][research_deangelis_1981]\] \[[DeAngelis 1982][research_deangelis_1982]\] \[[Deepa and Gupta 2023][research_deepa_gupta_2023]\] \[[Dehghan Manshadi and Saghafi 2021][research_dehghanmanshadi_saghafi_2021]\] \[[Dias 2023][research_dias_2023]\] \[[Dowell and Bliss 1978][research_dowell_bliss_1978]\] \[[Enciu 2019][research_enciu_2019]\] \[[Fan 2026][research_fan_2026]\] \[[Feng et al 2024][research_feng_liu_2024]\] \[[Flight Test Data Analysis of Hybrid Vertical Take-off and Landing Unmanned Aerial Vehicle 2016][research_flight_test_2016]\] \[[Hopwood et al 2023][research_hopwood_gresham_2023]\] \[[Hou 2025][research_hou_2025]\] \[[Hu et al 2026][research_hu_traisnel_2026]\] \[[Iliff et al 1978][research_iliffkw_mainere_1978]\] \[[Jategaonkar 2023][research_jategaonkar_2023]\] \[[Jenks et al 1977][research_jenksge_henryhf_1977]\] \[[Kannemans 1995][research_kannemans_1995]\] \[[Kashitani et al 2019][research_kashitani_takita_2019]\] \[[Kilgore and Averett 1964][research_kilgore_averett_1964]\] \[[Kim et al 2023][research_kim_philip_2023]\] \[[Kirmse 2016][research_kirmse_2016]\] \[[Kraft and Reeder 1948][research_kraftchristophercjr_reederjp_1948]\] \[[Kurita et al 2013][research_kurita_koike_2013]\] \[[Kurita et al 2019][research_kurita_koike_2019]\] \[[Lavretsky 2019][research_lavretsky_2019]\] \[[Li and Wang 2021][research_li_wang_2021_b]\] \[[Li et al 2014][research_li_liang_2014]\] \[[Liang et al 2026][research_liang_chen_2026]\] \[[Lichota 2023][research_lichota_2023]\] \[[Liu et al 2026][research_liu_wang_2026]\] \[[Lu et al 2019][research_lu_zhang_2019]\] \[[Ma and Chen 2020][research_ma_chen_2020]\] \[[Mackall et al 1988][research_mackallda_pickettmd_1988]\] \[[Matt et al 2025][research_matt_chao_2025]\] \[[Meng and Jiang 2025][research_meng_jiang_2025]\] \[[Moes et al 2000][research_moestimothyr_noffzgregoryk_2000]\] \[[Moes et al 2003][research_moestimothyr_smithmarks_2003]\] \[[Mulder 1988][research_mulder_1988]\] \[[Murphy 1996][research_murphypatrickc_1996]\] \[[Napolitano 1996][research_napolitanomarcellor_1996]\] \[[Napolitano and Spagnuolo 1993][research_napolitanomarcellor_spagnuolojoellem_1993]\] \[[Narendra and Tripathi 1973][research_narendra_tripathi_1973]\] \[[Norton 1990][research_norton_1990]\] \[[Pang et al 2014][research_pang_cesnik_2014]\] \[[Patel et al 2023][research_patel_deodhare_2023]\] \[[Murphy 1999][research_patrickcmurphy_1999]\] \[[Pena 2020][research_penafrancisco_2020]\] \[[Petersen 1981][research_petersenkl_1981]\] \[[Plaetschke et al 1982][research_plaetschke_mulder_1982]\] \[[Ružička et al 2013][research_ruzicka_rydel_2013]\] \[[Saderla et al 2016][research_saderla_dhayalan_2016]\] \[[Saderla et al 2018][research_saderla_kim_2018]\] \[[Simmons 2023][research_simmons_2023_b]\] \[[Simmons et al 2023][research_simmons_gresham_2023]\] \[[Singh and Raisinghani 1993][research_singh_raisinghani_1993]\] \[[Srivastava 2019][research_srivastava_2019]\] \[[Stalford 1979][research_stalford_1979]\] \[[Steinmetz et al 1972][research_steinmetzgg_parrishrv_1972]\] \[[Stottier 1995][research_stottier_1995]\] \[[Sun et al 2019][research_sun_devisser_2019]\] \[[Tagai et al 2016][research_tagai_nakakita_2016]\] \[[Tai et al 2023][research_tai_wang_2023_b]\] \[[Traven and Whitley 1995][research_traven_whitley_1995]\] \[[Van Doren 1955][research_vandoren_1955]\] \[[Veerman et al 2013][research_veerman_kannemans_2013]\] \[[Wakimoto et al 2021][research_wakimoto_chiba_2021]\] \[[Wang et al 2022][research_wang_tai_2022]\] \[[Wang et al 2022][research_wang_zhao_2022_b]\] \[[Whitlow et al 1991][research_whitlowwoodrowjr_bennettrobertm_1991]\] \[[Yasue 2020][research_yasue_2020]\] \[[Yu et al 2025][research_yu_he_2025]\]

### Aeroelastic tailoring and bend-twist coupling

Aeroelastic tailoring, bend-twist coupling and the mechanics of anisotropic laminated plates.

**104 records.** \[[Ahmadi and Farsadi 2024][research_ahmadi_farsadi_2024]\] \[[Alyanak and Pendleton 2017][research_alyanak_pendleton_2017]\] \[[Annadata et al 2024][research_annadata_endesfelder_2024]\] \[[Ansari et al 2023][research_ansari_zucco_2023]\] \[[Ayaz et al 2024][research_ayaz_rasoolmemon_2024]\] \[[Ayorinde and Gibson 1993][research_ayorinde_gibson_1993]\] \[[Babuska et al 2018][research_babuska_wiebe_2018]\] \[[Bi-quan and Huan-wen 1990][research_biquan_huanwen_1990]\] \[[Binder et al 2021][research_binder_wildschek_2021]\] \[[Bohlmann et al 1990][research_bohlmann_eckstrom_1990]\] \[[Bohlmann and Scott 1991][research_bohlmannjonathand_scottrobertc_1991]\] \[[Bohlmann et al 1988][research_bohlmannjonathand_weisshaarterrencea_1988]\] \[[Bordogna et al 2020][research_bordogna_lancelot_2020]\] \[[Cesnik 2002][research_cesnik_2002]\] \[[Cesnik 2005][research_cesnik_2005]\] \[[Chattopadhyay and Jha 1996][research_chattopadhyayaditi_jharatneshwar_1996]\] \[[Chattopadhyay and Zhang 1995][research_chattopadhyayaditi_zhangsen_1995]\] \[[Chen and Han 2017][research_chen_han_2017]\] \[[Choi et al 2020][research_choi_lim_2020]\] \[[Cui et al 2022][research_cui_li_2022]\] \[[Cui et al 2026][research_cui_miao_2026]\] \[[Das and Kapuria 2016][research_das_kapuria_2016]\] \[[de Souza and de Leon 2023][research_desouza_deleon_2023]\] \[[Dunning et al 2014][research_dunningpeterd_stanfordbretk_2014]\] \[[Fazeli et al 2022][research_fazeli_stokesgriffin_2022]\] \[[Feil et al 2020][research_feil_pflumm_2020]\] \[[Fraihat and Ajaj 2024][research_fraihat_ajaj_2024]\] \[[Francois et al 2017][research_francois_cooper_2017]\] \[[Fung and Doong 1988][research_fung_doong_1988]\] \[[Giese et al 1996][research_giese_reich_1996]\] \[[González-Montijo et al 2026][research_gonzalezmontijo_vanness_2026]\] \[[Green 1987][research_green_1987]\] \[[Green 1986][research_greenja_1986]\] \[[Grenestedt 1989][research_grenestedt_1989]\] \[[Gu et al 2022][research_gu_taghipour_2022]\] \[[Hahn and Haupt 2022][research_hahn_haupt_2022]\] \[[He et al 2023][research_he_wang_2023]\] \[[Heeg 2006][research_heegjennifer_2006]\] \[[Heeg et al 2005][research_heegjennifer_spaincharlesv_2005]\] \[[Isogai 1988][research_isogai_1988]\] \[[Isogai 1989][research_isogai_1989]\] \[[Jang and Ahn 2022][research_jang_ahn_2022]\] \[[Jegley and Wijayratne 2004][research_jegleydawnc_wijayratnedulnathd_2004]\] \[[Jensen and Crawley 1984][research_jensen_crawley_1984]\] \[[Jensen et al 1982][research_jensen_crawley_1982]\] \[[Jonnalagadda et al 2015][research_jonnalagadda_sawant_2015]\] \[[Kim et al 2016][research_kim_shin_2016]\] \[[Kirsch et al 2020][research_kirsch_montagnier_2020]\] \[[Krüger et al 2022][research_kruger_meddaikar_2022]\] \[[Li et al 2018][research_li_wang_2018_b]\] \[[Li et al 2019][research_li_gong_2019]\] \[[Librescu and Song 1992][research_librescu_song_1992]\] \[[Liu et al 2023][research_liu_zhang_2023]\] \[[Lottati 1988][research_lottati_1988]\] \[[Loughlan 2019][research_loughlan_2019]\] \[[Marano et al 2022][research_marano_belardo_2022]\] \[[Marques et al 2017][research_marques_natarajan_2017]\] \[[McWilliam et al 2018][research_mcwilliam_zahle_2018]\] \[[Meirovitch 1995][research_meirovitch_1995]\] \[[Melville et al 2020][research_melville_bramesfeld_2020]\] \[[Mihaila-Andres et al 2019][research_mihailaandres_rosu_2019]\] \[[Miranda et al 2025][research_miranda_li_2025]\] \[[Monaghan 1981][research_monaghanrc_1981]\] \[[Murray et al 2015][research_murray_doman_2015]\] \[[Najmi et al 2024][research_najmi_khan_2024]\] \[[Namani Koureh et al 2026][research_namanikoureh_shahverdi_2026]\] \[[Opgenoord and Willcox 2019][research_opgenoord_willcox_2019]\] \[[Othman et al 2019][research_othman_silva_2019]\] \[[Padovan 1973][research_padovan_1973]\] \[[Padovan 1974][research_padovan_1974]\] \[[Rais-Rohani 1994][research_raisrohanimasoud_1994]\] \[[Rajpal et al 2021][research_rajpal_mitrotta_2021]\] \[[Raouf 1994][research_raouf_1994]\] \[[Ren 1986][research_ren_1986]\] \[[Shakya and Padhee 2023][research_shakya_padhee_2023]\] \[[Shao et al 2025][research_shao_sun_2025]\] \[[Sharifi et al 2025][research_sharifi_vincenti_2025]\] \[[Sherrer et al 1981][research_sherrer_hertz_1981]\] \[[Shirk et al 1986][research_shirk_hertz_1986]\] \[[Shyprykevich 1979][research_shyprykevichp_1979]\] \[[Stanford 2016][research_stanford_2016_b]\] \[[Stanford and Jutte 2017][research_stanford_jutte_2017]\] \[[Stanford et al 2016][research_stanford_jutte_2016]\] \[[Stanford and Jutte 2014][research_stanfordbretk_juttechristinev_2014]\] \[[Stanford et al 2015][research_stanfordbretk_wiesemancarold_2015]\] \[[Stodieck et al 2015][research_stodieck_cooper_2015]\] \[[Stodieck et al 2017][research_stodieck_cooper_2017]\] \[[Targoff 1947][research_targoff_1947]\] \[[Tian et al 2016][research_tian_yang_2016]\] \[[Triplett 1980][research_triplett_1980]\] \[[Vertonghen et al 2026][research_vertonghen_irisarri_2026]\] \[[Viglietti et al 2019][research_viglietti_zappino_2019]\] \[[Wang and Rogers 1991][research_wang_rogers_1991]\] \[[Weisshaar 1981][research_weisshaar_1981]\] \[[Weisshaar and Ryan 1986][research_weisshaar_ryan_1986]\] \[[Werter and De Breuker 2016][research_werter_debreuker_2016]\] \[[Wunderlich and Dähne 2017][research_wunderlich_dahne_2017_b]\] \[[Wunderlich et al 2017][research_wunderlich_dahne_2017]\] \[[Ying et al 2021][research_ying_liqiang_2021]\] \[[Young et al 2018][research_young_garg_2018]\] \[[Yu et al 2017][research_yu_wang_2017]\] \[[Zaw and Baranovski 2026][research_zaw_baranovski_2026]\] \[[Zhang et al 2019][research_zhang_liu_2019]\] \[[Zhang et al 2020][research_zhang_chen_2020]\]

### Divergence and static aeroelasticity

Static aeroelasticity and divergence, of swept, forward-swept and oblique wings and of wind tunnel models.

**95 records.** \[[A study of the 1973][research_a_study_1973]\] \[[Arena and Lacarbonara 2012][research_arena_lacarbonara_2012]\] \[[Asadi Khanouki et al 2019][research_asadikhanouki_javadiaghdam_2019]\] \[[Awadalla Ali Haj Ahmed 2024][research_awadallaalihajahmed_2024]\] \[[Awadalla Ali Haj Ahmed 2024][research_awadallaalihajahmed_2024_b]\] \[[Balakrishnan and Tuffaha 2012][research_balakrishnan_tuffaha_2012]\] \[[Bhardwaj and Kapania 1995][research_bhardwaj_kapania_1995]\] \[[Blair and Weisshaar 1981][research_blair_weisshaar_1981]\] \[[Blair and Weisshaar 1982][research_blair_weisshaar_1982]\] \[[Bland 1980][research_bland_1980]\] \[[Bohlmann 1989][research_bohlmannjonathand_1989]\] \[[Bolotin et al 1996][research_bolotin_grishko_1996]\] \[[Bueno and Dowell 2020][research_bueno_dowell_2020]\] \[[Campagna et al 2025][research_campagna_gulizzi_2025]\] \[[Carrera et al 2013][research_carrera_varello_2013]\] \[[Castellani et al 2017][research_castellani_cooper_2017]\] \[[Cestino and Iannuzzo 2026][research_cestino_iannuzzo_2026]\] \[[Cole 1988][research_cole_1988]\] \[[Cole 1986][research_colesr_1986]\] \[[Craig and Erbug 1976][research_craig_erbug_1976]\] \[[Diederich and Budiansky 1948][research_diederichfranklinw_budianskybernard_1948]\] \[[Eastep et al 1984][research_eastep_venkayya_1984]\] \[[Edwards 1992][research_edwards_1992]\] \[[Edwards and Wieseman 2003][research_edwards_wieseman_2003]\] \[[Edwards and Wieseman 2008][research_edwards_wieseman_2008]\] \[[Ehlers and Weisshaar 1993][research_ehlers_weisshaar_1993]\] \[[Griffin and Eastep 1982][research_griffin_eastep_1982]\] \[[Guo et al 2022][research_guo_zhang_2022]\] \[[Gwin 1976][research_gwin_1976]\] \[[Gwin 1974][research_gwinlb_1974]\] \[[Haas and Chopra 1988][research_haas_chopra_1988]\] \[[Heeg et al 2004][research_heegjennifer_spaincharlesv_2004]\] \[[Hildebrand and Reissner 1944][research_hildebrandfrancisb_reissnereric_1944]\] \[[Hollowell and Dugundji 1982][research_hollowell_dugundji_1982]\] \[[Hollowell and Dugundji 1984][research_hollowell_dugundji_1984]\] \[[Hopkins and Yee 1977][research_hopkinsej_yeesc_1977]\] \[[Hunn 1953][research_hunn_1953]\] \[[Hwu and Tsai 2002][research_hwu_tsai_2002]\] \[[Isogai 1992][research_isogai_1992]\] \[[Jones 1976][research_jones_1976]\] \[[Jones and Nisbet 1976][research_jones_nisbet_1976]\] \[[Kobelev 2019][research_kobelev_2019]\] \[[Koo and Lee 1994][research_koo_lee_1994]\] \[[Kornev et al 2021][research_kornev_ambrozhevich_2021]\] \[[Kulikov 2020][research_kulikov_2020]\] \[[Kunaporn et al 2014][research_kunaporn_singh_2014]\] \[[Lee and Kim 1995][research_lee_kim_1995]\] \[[Lerner and Markowitz 1979][research_lerner_markowitz_1979]\] \[[Li and Wang 2018][research_li_wang_2018]\] \[[Li et al 2024][research_li_qian_2024]\] \[[Librescu and Khdeir 1988][research_librescu_khdeir_1988]\] \[[Librescu and Maalawi 2009][research_librescu_maalawi_2009]\] \[[Librescu and Simovich 1988][research_librescu_simovich_1988]\] \[[Liu 2019][research_liu_2019]\] \[[Lottati 1985][research_lottati_1985]\] \[[Maalawi 2019][research_maalawi_2019]\] \[[Mathur et al 2026][research_mathur_huang_2026]\] \[[Niblett 1986][research_niblett_1986]\] \[[Pearson and Aiken 1944][research_pearsonhenrya_aikenwilliamsjr_1944]\] \[[Rajamurugu et al 2024][research_rajamurugu_satyam_2024]\] \[[Rea J B Co Inc Santa Monica Ca 1957][research_reajbcoincsantamonicaca_1957]\] \[[Reinbold et al 2026][research_reinbold_breitsamter_2026]\] \[[Ricketts and Doggett 1980][research_rickettsrh_doggettrvjr_1980]\] \[[Rimer et al 1984][research_rimer_chipman_1984]\] \[[Rodden 1981][research_rodden_1981]\] \[[Rodden 1984][research_rodden_1984]\] \[[Rodden 1989][research_rodden_1989]\] \[[Rodden 1989][research_rodden_1989_b]\] \[[Rodden and Bellinger 1982][research_rodden_bellinger_1982]\] \[[Roskam and Lan 1973][research_roskamj_lanc_1973]\] \[[Ruscheweyh 1983][research_ruscheweyh_1983]\] \[[Sachs 1975][research_sachs_1975]\] \[[Satt and Ilanko 2007][research_satt_ilanko_2007]\] \[[Schuster and Lokos 1988][research_schuster_lokos_1988]\] \[[Schuster and Edwards 2004][research_schusterdavidm_edwardsjohnw_2004]\] \[[Segel 1952][research_segel_1952]\] \[[Shivaji et al 2025][research_shivaji_basavaraju_2025]\] \[[Silva][research_silva]\] \[[Song and Librescu 1991][research_song_librescu_1991]\] \[[Targoff 1947][research_targoff_1947_b]\] \[[Taylor 1959][research_taylor_1959]\] \[[Taylor et al 1999][research_taylor_butler_1999]\] \[[Thwapiah and Campanile 2010][research_thwapiah_campanile_2010]\] \[[Ting et al 2014][research_tingeric_lebofskysonia_2014]\] \[[Townsend et al 2018][research_townsend_picelli_2018]\] \[[Van Zyl 2001][research_vanzyl_2001]\] \[[van Zyl and Maserumule 2001][research_vanzyl_maserumule_2001]\] \[[Vedeneev 2020][research_vedeneev_2020]\] \[[Verri et al 2025][research_verri_desilvabussamra_2025]\] \[[Wan et al 2003][research_wan_yang_2003]\] \[[Wang 2019][research_wang_2019]\] \[[Weisshaar 1980][research_weisshaar_1980]\] \[[Wooldridge 1960][research_wooldridge_1960]\] \[[Zeiler 1999][research_zeiler_1999]\] \[[Zhang et al 2021][research_zhang_guo_2021]\]

**Of the 95 records, 33 date from 1984 or earlier, and 17 titles name forward sweep.**

### Sampled-data control and time delay

Sampled-data and digital control, time delay and networked control.

**91 records.** \[[044 Finite worldlength control of sampled data systems by covariance assignment 1994][research_044_finite_1994]\] \[[057 H∞ control design for a class of uncertain sampled-data systems 1994][research_057_h_1994]\] \[[130 Sampled-data decentralized controller design 1994][research_130_sampled_data_1994]\] \[[185 A fourier series lifting approach to H∞ sampled data control 1994][research_185_a_1994]\] \[[A hybrid adaptive control scheme using sampled data and intersampling compensation 1995][research_a_hybrid_1995]\] \[[Ackermann and Isermann 1973][research_ackermann_isermann_1973]\] \[[Alcaina et al 2019][research_alcaina_cuenca_2019]\] \[[Aslam and Chen 2018][research_aslam_chen_2018]\] \[[Azadegan and Beheshti 2017][research_azadegan_beheshti_2017]\] \[[Berman and Gran 1974][research_berman_gran_1974]\] \[[Bernstein and Hollot 1989][research_bernstein_hollot_1989]\] \[[Berry et al 1982][research_berry_powers_1982]\] \[[Chen et al 2017][research_chen_gao_2017]\] \[[Chen et al 2022][research_chen_edwards_2022]\] \[[Chin et al 1994][research_chin_lee_1994]\] \[[Crane 1983][research_cranedf_1983]\] \[[Crane 1984][research_cranedf_1984]\] \[[Czyba and Stajer 2019][research_czyba_stajer_2019]\] \[[Design of discrete-time adaptive control in presence of uncertain time delay 1995][research_design_of_1995]\] \[[Digital model-reference flight control of aircraft with unstable sampling zeros 1994][research_digital_model_reference_1994]\] \[[Farkh et al 2021][research_farkh_ksouri_2021]\] \[[G.S.S.S.S.V. 2020][research_gssssv_2020]\] \[[Halder et al 2020][research_halder_das_2020]\] \[[Hirai and Satoh 1980][research_hirai_satoh_1980]\] \[[Ishii 2023][research_ishii_2023]\] \[[Jajarmi and Hajipour 2016][research_jajarmi_hajipour_2016]\] \[[Khargonekar and Sivashankar 1991][research_khargonekar_sivashankar_1991]\] \[[Kodama 1962][research_kodama_1962]\] \[[Kumar et al 2022][research_kumar_kumar_2022]\] \[[Kuzu et al 2015][research_kuzu_bogosyan_2015]\] \[[Lee and Sheu 1994][research_lee_sheu_1994]\] \[[Lennartson 1989][research_lennartson_1989]\] \[[Li et al 2016][research_li_bai_2016]\] \[[Liu and Zhang 2018][research_liu_zhang_2018]\] \[[Liu et al 2026][research_liu_liu_2026]\] \[[Lu et al 2019][research_lu_hu_2019]\] \[[Jury 1959][research_m_jury_1959]\] \[[Ma et al 2024][research_ma_yu_2024]\] \[[Mishra et al 2025][research_mishra_yadav_2025]\] \[[Miyasato 1992][research_miyasato_1992]\] \[[Miyazawa 1993][research_miyazawa_1993]\] \[[Mohanty and Chhotaray 1979][research_mohanty_chhotaray_1979]\] \[[Narenshakthi and Dharani 2025][research_narenshakthi_dharani_2025]\] \[[Nekooei et al 2021][research_nekooei_farsangi_2021]\] \[[Nihtilä 1989][research_nihtila_1989]\] \[[Ocali and Sezer 1992][research_ocali_sezer_1992]\] \[[Ohkawa 1985][research_ohkawa_1985]\] \[[Ohkawa 1986][research_ohkawa_1986]\] \[[Panuntun et al 2020][research_panuntun_wahyunggoro_2020]\] \[[Peled and Powell 1978][research_peledu_powelljd_1978]\] \[[Phillips 1965][research_phillips_1965]\] \[[Plyako 1977][research_plyako_1977]\] \[[Qiao et al 2018][research_qiao_wu_2018]\] \[[Raghavan 1971][research_raghavan_1971]\] \[[Rehan et al 2015][research_rehan_iqbal_2015]\] \[[Rohella and Chatterjee 1979][research_rohella_chatterjee_1979]\] \[[Sampling schemes in sampled-data control systems 1961][research_sampling_schemes_1961]\] \[[Shah and Desai 1973][research_shah_desai_1973]\] \[[Shah and Mehta 2017][research_shah_mehta_2017]\] \[[Shen et al 2021][research_shen_huang_2021]\] \[[Shieh and Chen 1998][research_shieh_chen_1998]\] \[[Shields and Cook 1971][research_shields_cook_1971]\] \[[Tang 2025][research_tang_2025]\] \[[Tharp and Zhang 1994][research_tharp_zhang_1994]\] \[[Tian 2016][research_tian_2016]\] \[[Tian 2020][research_tian_2020]\] \[[Tian 2021][research_tian_2021]\] \[[Tian and Tang 2025][research_tian_tang_2025]\] \[[Tian et al 2015][research_tian_li_2015]\] \[[Tsoutsinos 1994][research_tsoutsinos_1994]\] \[[Tsypkin and Fu 1993][research_tsypkin_fu_1993]\] \[[Viola et al 2020][research_viola_oziablo_2020]\] \[[Voulgaris 1994][research_voulgaris_1994]\] \[[Wang et al 2016][research_wang_liang_2016]\] \[[Wang et al 2022][research_wang_hou_2022]\] \[[Weissenberger 1969][research_weissenberger_1969]\] \[[Wu and Deng 2015][research_wu_deng_2015]\] \[[Xiang and Liu 2024][research_xiang_liu_2024]\] \[[Yahagi 1971][research_yahagi_1971]\] \[[Yang 2024][research_yang_2024]\] \[[Yang et al 2023][research_yang_zhang_2023]\] \[[Yang et al 2024][research_yang_fu_2024]\] \[[Yao 2018][research_yao_2018]\] \[[Yaseen and Bayart 2018][research_yaseen_bayart_2018]\] \[[Yi et al 2017][research_yi_an_2017]\] \[[You et al 2022][research_you_lei_2022]\] \[[Zhang 2023][research_zhang_2023]\] \[[Zhang et al 2024][research_zhang_zhou_2024_b]\] \[[Zhou et al 1989][research_zhou_ye_1989]\] \[[Zuo et al 2016][research_zuo_min_2016]\] \[[Ženíšek 1973][research_zenisek_1973]\]

### Canards, trim and multiple lifting surfaces

Canard aerodynamics, canard-wing interaction, trim and multiple lifting surfaces.

**88 records.** \[[Agrell and Elmeland 1985][research_agrell_elmeland_1985]\] \[[Aidala 1985][research_aidala_1985]\] \[[Bandyopadhyay 1989][research_bandyopadhyay_1989]\] \[[Bandyopadhyay 1991][research_bandyopadhyay_1991]\] \[[Boyden 1978][research_boydenrp_1978]\] \[[Bright and Peterson 1960][research_brightlg_petersonvl_1960]\] \[[Burkhalter 1993][research_burkhalter_1993]\] \[[Calarese 1984][research_calarese_1984]\] \[[Chen et al 2016][research_chen_liu_2016]\] \[[Chen et al 2023][research_chen_gao_2023_b]\] \[[Das and Longo 1995][research_das_longo_1995]\] \[[de Silva and Carmichael 1978][research_desilva_carmichael_1978]\] \[[Desilva and Medan 1978][research_desilvabme_medanrt_1978]\] \[[Dong et al 2019][research_dong_shi_2019]\] \[[Durston and Schreiner 1983][research_durstonda_schreinerja_1983]\] \[[Dwivedi et al 2022][research_dwivedi_anitha_2022]\] \[[Er-El 1988][research_erel_1988]\] \[[Er-El and Seginer 1985][research_erel_seginer_1985]\] \[[Eugene 1996][research_eugeneltu_1996]\] \[[Fan et al 2025][research_fan_wang_2025]\] \[[Finkleman 1972][research_finkleman_1972]\] \[[Gao et al 2019][research_gao_gao_2019]\] \[[Gloss and Washburn 1978][research_gloss_washburn_1978]\] \[[Gloss and Washburn 1977][research_glossbb_washburnke_1977]\] \[[Goodrich et al 1989][research_goodrichkennethh_sliwastevenm_1989]\] \[[Gupta 2023][research_gupta_2023]\] \[[Hitzel and Osterhuber 2018][research_hitzel_osterhuber_2018]\] \[[Howard and O'Leary 1994][research_howard_oleary_1994]\] \[[Huffman 1975][research_huffmanjk_1975]\] \[[Hummel and Oelker 1994][research_hummel_oelker_1994]\] \[[Ignatyev and Khrabrov 2018][research_ignatyev_khrabrov_2018]\] \[[Ingram et al 1986][research_ingramwc_yiplp_1986]\] \[[Ito and Iwashita 2017][research_ito_iwashita_2017]\] \[[Jiang et al 2022][research_jiang_tong_2022]\] \[[Kalugin et al 2022][research_kalugin_voropaev_2022]\] \[[Katz and Levin 1986][research_katz_levin_1986]\] \[[Katz et al 1986][research_katz_davidovitch_1986]\] \[[Keith and Selberg 1984][research_keith_selberg_1984]\] \[[Keith and Selberg 1985][research_keith_selberg_1985]\] \[[Kim and Kang 2025][research_kim_kang_2025]\] \[[Komarov and Zinchenko 2023][research_komarov_zinchenko_2023]\] \[[Lai 2024][research_lai_2024]\] \[[Landfield and Rajkovic 1986][research_landfield_rajkovic_1986]\] \[[Lee et al 2023][research_lee_lee_2023]\] \[[Lijewski 1988][research_lijewski_1988]\] \[[Lin et al 1994][research_lin_chin_1994]\] \[[Lombardi 1995][research_lombardi_1995]\] \[[McCutchen 1980][research_mccutchen_1980]\] \[[McKlNNEY and DOLLYHlGH 1971][research_mcklnney_dollyhlgh_1971]\] \[[Miner and Gloss 1975][research_minerdd_glossbb_1975]\] \[[Mochizuki and Yamada 2018][research_mochizuki_yamada_2018]\] \[[Moul and Wineman 1952][research_moulmartint_winemanandrewr_1952]\] \[[Nicholas et al 1984][research_nicholaswu_navillegl_1984]\] \[[Numerical and Experimental Determination of Canard Controlled Missile Aerodynamic Coefficients in Subsonic Regime 2019][research_numerical_and_2019]\] \[[Oelker and Hummel 1989][research_oelker_hummel_1989]\] \[[Paulson and Thomas 1978][research_paulsonjwjr_thomasjl_1978]\] \[[Paulson and Thomas 1979][research_paulsonjwjr_thomasjl_1979_b]\] \[[Paulson et al 1979][research_paulsonjwjr_thomasjl_1979]\] \[[Qin et al 2017][research_qin_liu_2017]\] \[[Selberg and Cronin 1985][research_selbergbp_cronindl_1985]\] \[[Shankar and Malmuth 1982][research_shankar_malmuth_1982]\] \[[Shankar and Malmuth 1983][research_shankar_malmuth_1983]\] \[[Shankar et al 1981][research_shankar_malmuth_1981]\] \[[Shrivastava and Mohite 2015][research_shrivastava_mohite_2015]\] \[[Silton and Fresconi 2015][research_silton_fresconi_2015]\] \[[Silton et al 2014][research_silton_fresconi_2014]\] \[[Smeltzer et al 1983][research_smeltzer_durston_1983]\] \[[Stark 1989][research_stark_1989]\] \[[Stoll and Koenig 1983][research_stollf_koenigdg_1983]\] \[[Szklarski and Głębocki 2025][research_szklarski_glebocki_2025]\] \[[Tahani et al 2017][research_tahani_masdari_2017]\] \[[Theerthamalai et al 2025][research_theerthamalai_mukesh_2025]\] \[[Thomas et al 1978][research_thomas_paulson_1978]\] \[[Thompson 1992][research_thompson_1992]\] \[[Ting et al 2014][research_tingeric_nguyennhan_2014]\] \[[Tu 1992][research_tu_1992]\] \[[Tu 1994][research_tu_1994]\] \[[Tu 1994][research_tu_1994_b]\] \[[Tu 1991][research_tueugenel_1991]\] \[[Tu 1992][research_tueugenel_1992]\] \[[Tu 1992][research_tueugenel_1992_b]\] \[[Tu and VanDalsem 1996][research_tueugenel_vandalsemwilliamr_1996]\] \[[Varun and Dwivedi 2022][research_varun_dwivedi_2022]\] \[[Wei et al 2019][research_wei_zhan_2019]\] \[[Yip and Paulson 1977][research_yiplp_paulsonjwjr_1977]\] \[[Yoo et al 2023][research_yoo_jeong_2023]\] \[[Yutuk et al 2021][research_yutuk_tikenogullari_2021]\] \[[Комаров and Зінченко 2019][research___2019]\]

### Structural mechanics, buckling and structural weight

The structural mechanics of plates, beams and shells, structural weight estimation, and the design and test of aircraft structures.

**83 records.** \[[Abdullah et al 2019][research_abdullah_akbar_2019]\] \[[Acoustic emissions and transient elastic waves in an orthotropic laminate plate 1989][research_acoustic_emissions_1989]\] \[[Aggarwal and Cranch 1967][research_aggarwal_cranch_1967]\] \[[Ascani 1974][research_ascani_1974]\] \[[Ashton 1970][research_ashton_1970]\] \[[Becker 1992][research_becker_1992]\] \[[Berezhnitskii and Denisyuk 1985][research_berezhnitskii_denisyuk_1985]\] \[[Bogan 1981][research_bogan_1981]\] \[[Brigham et al 1973][research_brigham_barrie_1973]\] \[[Broglio 1957][research_broglio_1957]\] \[[Clay and Rockafellow 1973][research_clay_rockafellow_1973]\] \[[Cohen 1982][research_cohen_1982]\] \[[Cuschieri 1990][research_cuschieri_1990]\] \[[Cutchins and Purvis 1982][research_cutchinsma_purvisjw_1982]\] \[[Davis 1973][research_davis_1973]\] \[[Design of an Aircraft Wing Structure for Static&amp; Fatigue Life Prediction 2019][research_design_of_2019]\] \[[Doi and Kataoka 1982][research_doi_kataoka_1982]\] \[[Dooley 1965][research_dooley_1965]\] \[[Dubigeon 1992][research_dubigeon_1992]\] \[[Edwards 1963][research_edwards_1963]\] \[[Effective Torsional Stiffness of Equivalent Beams 1976][research_effective_torsional_1976]\] \[[Figge 1973][research_figge_1973]\] \[[Gilbert and Schneider 1981][research_gilbert_schneider_1981]\] \[[Grigolyuk and Kulikov 1990][research_grigolyuk_kulikov_1990]\] \[[Harpur 1968][research_harpur_1968]\] \[[Hayase 1974][research_hayase_1974]\] \[[Hayashi 1949][research_hayashi_1949]\] \[[Hiyama 1974][research_hiyama_1974]\] \[[Horsburgh 1911][research_horsburgh_1911]\] \[[Horton and Mayers 1965][research_horton_mayers_1965]\] \[[Hu 1984][research_hu_1984]\] \[[Jaeger and Hendry 1959][research_jaeger_hendry_1959]\] \[[Jensen et al 1966][research_jensen_falby_1966]\] \[[Johnson 1973][research_johnson_1973]\] \[[Johnson et al 1962][research_johnson_henderson_1962]\] \[[Kalnins 1968][research_kalnins_1968]\] \[[Kaloerov 1983][research_kaloerov_1983]\] \[[Karniadakis 2004][research_karniadakis_2004]\] \[[Kataoka et al 1986][research_kataoka_dol_1986]\] \[[Kosmodamianskii and Mitrakov 1976][research_kosmodamianskii_mitrakov_1976]\] \[[Kuang et al 2025][research_kuang_hu_2025]\] \[[Kuznetsov and Kartashov 1980][research_kuznetsov_kartashov_1980]\] \[[Lee 1995][research_lee_1995]\] \[[Liang et al 2024][research_liang_yin_2024]\] \[[Lyubchak and Fil'shtinskii 1982][research_lyubchak_filshtinskii_1982]\] \[[Mansour 1970][research_mansour_1970]\] \[[Meglinskii 1966][research_meglinskii_1966]\] \[[Micks 1950][research_micks_1950]\] \[[Miller 1965][research_miller_1965]\] \[[Moriya 1982][research_moriya_1982]\] \[[Padovan and Gosset 1974][research_padovan_gosset_1974]\] \[[Parbery and Karihaloo 1980][research_parbery_karihaloo_1980]\] \[[Parbery∗ and Olhoff 1987][research_parbery_olhoff_1987]\] \[[Peck and Hudson 1956][research_peck_hudson_1956]\] \[[Perry and Rievley 1961][research_perry_rievley_1961]\] \[[Reddy 1982][research_reddy_1982]\] \[[Robinson 2004][research_robinson_2004]\] \[[Sciuva 1992][research_sciuva_1992]\] \[[Seraj and Ganesan 2018][research_seraj_ganesan_2018]\] \[[Shanley 1943][research_shanley_1943]\] \[[Shi and Bezine 1988][research_shi_bezine_1988]\] \[[Simmonds 1971][research_simmonds_1971]\] \[[Somashekar et al 1987][research_somashekar_prathap_1987]\] \[[Structural Fundamentals 1955][research_structural_fundamentals_1955]\] \[[Sugimoto and Saito 1968][research_sugimoto_saito_1968]\] \[[Sugimoto and Saito 1969][research_sugimoto_saito_1969]\] \[[Tahraoui 1994][research_tahraoui_1994]\] \[[Tan 1988][research_tan_1988]\] \[[Tang 1972][research_tang_1972]\] \[[Toader 1987][research_toader_1987]\] \[[Wagg 2022][research_wagg_2022]\] \[[Wang 2024][research_wang_2024]\] \[[Wasson and Mehus 1967][research_wasson_mehus_1967]\] \[[Wickman 1953][research_wickman_1953]\] \[[Wildermuth et al 1974][research_wildermuth_rothammer_1974]\] \[[Wildermuth et al 1974][research_wildermuth_rothammer_1974_b]\] \[[Williams 1952][research_williams_1952]\] \[[Winny 1950][research_winny_1950]\] \[[Wu 1976][research_wu_1976]\] \[[Wu and Chiu 1992][research_wu_chiu_1992]\] \[[Yamasaki and Gotoh 1971][research_yamasaki_gotoh_1971]\] \[[Zadvornyak and Martynovich 1983][research_zadvornyak_martynovich_1983]\] \[[Zhang et al 2026][research_zhang_zhao_2026]\]

### Machine learning and data-driven modelling

Machine learning, surrogate and reduced-order models and reinforcement learning applied to aerodynamics, structures and flight control.

**81 records.** \[[Abouheaf et al 2020][research_abouheaf_gueaieb_2020]\] \[[Baldan and Guardone 2024][research_baldan_guardone_2024]\] \[[Beitalmal 2025][research_beitalmal_2025]\] \[[Benyamen et al 2024][research_benyamen_chowdhury_2024]\] \[[Cai et al 2026][research_cai_fan_2026]\] \[[Caixeta and Marques 2018][research_caixeta_marques_2018]\] \[[Cao and Lu 2024][research_cao_lu_2024]\] \[[Cao et al 2026][research_cao_chen_2026]\] \[[Chen et al 2020][research_chen_he_2020]\] \[[Choi et al 2023][research_choi_kim_2023]\] \[[Cui et al 2021][research_cui_azuara_2021]\] \[[Data-driven Model-Free Adaptive Control Tuned by Virtual Reference 2016][research_data_driven_model_free_2016]\] \[[Divakar and B L 2026][research_divakar_bl_2026]\] \[[D’Amico et al 2025][research_damico_labella_2025]\] \[[d’Apolito and Sulzbachner 2021][research_dapolito_sulzbachner_2021]\] \[[Fan et al 2026][research_fan_jiang_2026]\] \[[Fina and Bisagni 2026][research_fina_bisagni_2026]\] \[[Ghazi et al 2022][research_ghazi_alhazmi_2022]\] \[[Golombek et al 2026][research_golombek_bustamante_2026]\] \[[Gong et al 2019][research_gong_wang_2019_b]\] \[[Haeri and Fadaee 2016][research_haeri_fadaee_2016]\] \[[Halder et al 2020][research_halder_damodaran_2020]\] \[[Han et al 2023][research_han_cheng_2023]\] \[[Han et al 2024][research_han_yang_2024]\] \[[Grauer 2018][research_jaredagrauer_2018]\] \[[Jianhong and Ramirez-Mendoza 2023][research_jianhong_ramirezmendoza_2023]\] \[[Kanou and Ibuki 2025][research_kanou_ibuki_2025]\] \[[Khodaverdian et al 2025][research_khodaverdian_gohil_2025]\] \[[Kirsch et al 2025][research_kirsch_fathi_2025]\] \[[Kou and Zhang 2021][research_kou_zhang_2021]\] \[[Lerro et al 2020][research_lerro_brandl_2020]\] \[[Liao et al 2021][research_liao_song_2021]\] \[[Lindhorst et al 2015][research_lindhorst_haupt_2015]\] \[[Liu and Liu 2025][research_liu_liu_2025]\] \[[Liu and Zhao 2026][research_liu_zhao_2026]\] \[[Maiworm et al 2021][research_maiworm_limon_2021]\] \[[Moni et al 2024][research_moni_yao_2024]\] \[[Monshizadeh 2020][research_monshizadeh_2020]\] \[[Na and Lee 2024][research_na_lee_2024]\] \[[Nagy and Fossati 2022][research_nagy_fossati_2022]\] \[[Nan et al 2024][research_nan_zheng_2024]\] \[[Peyada and Ghosh 2023][research_peyada_ghosh_2023]\] \[[Raiola et al 2021][research_raiola_discetti_2021]\] \[[Restifo et al 2026][research_restifo_villa_2026]\] \[[Richter et al 2024][research_richter_calix_2024]\] \[[Alwan and Hussain 2026][research_salwan_hussain_2026]\] \[[Kandasamy et al 2018][research_s_sinha_2018]\] \[[Seres et al 2023][research_seres_liu_2023]\] \[[Setiawarman and Sasongko 2026][research_setiawarman_sasongko_2026]\] \[[Shukla et al 2025][research_shukla_benyamen_2025]\] \[[Toloei and Ghaderi 2026][research_toloei_ghaderi_2026]\] \[[Tong et al 2025][research_tong_du_2025]\] \[[Torregrosa et al 2022][research_torregrosa_gil_2022]\] \[[Uzun et al 2023][research_uzun_bilgic_2023]\] \[[van Waarde 2022][research_vanwaarde_2022]\] \[[Volpe et al 2026][research_volpe_salcuni_2026]\] \[[Wada et al 2020][research_wada_tamayama_2020]\] \[[Walker and Claudio 2024][research_walker_claudio_2024]\] \[[Wang and Zhou 2026][research_wang_zhou_2026]\] \[[Wang et al 2026][research_wang_weng_2026]\] \[[Wang et al 2026][research_wang_yi_2026]\] \[[Wei and Freris 2024][research_wei_freris_2024]\] \[[Wei et al 2024][research_wei_meng_2024]\] \[[White and Hartl 2025][research_white_hartl_2025]\] \[[Wilson and Riccardi 2022][research_wilson_riccardi_2022]\] \[[Xia et al 2026][research_xia_li_2026]\] \[[Xu et al 2024][research_xu_tian_2024]\] \[[Xu et al 2026][research_xu_liu_2026]\] \[[Yan et al 2019][research_yan_li_2019]\] \[[Yang et al 2026][research_yang_wang_2026]\] \[[Yonekura and Suzuki 2021][research_yonekura_suzuki_2021]\] \[[Yoo et al 2021][research_yoo_jang_2021]\] \[[Yuan and Zhou 2024][research_yuan_zhou_2024]\] \[[Zhang et al 2021][research_zhang_xie_2021]\] \[[Zhang et al 2022][research_zhang_ji_2022]\] \[[Zhang et al 2026][research_zhang_wang_2026]\] \[[Zhao et al 2024][research_zhao_xu_2024]\] \[[Zhao et al 2024][research_zhao_zhang_2024]\] \[[Zhiqiang et al 2016][research_zhiqiang_xiaozhe_2016]\] \[[Zhou et al 2024][research_zhou_cheng_2024]\] \[[Zhou et al 2025][research_zhou_liu_2025]\]

**All 81 records date from 2015 or later.**

### Lift, induced drag and aerodynamic estimation

Lift-curve slope, induced drag and its minimum, flow-control effectors used for flight control and load alleviation, and the estimation of aerodynamic coefficients and the data compendia that tabulate them.

**64 records.** \[[AbuNawas and Qawasmeh 2026][research_abunawas_qawasmeh_2026]\] \[[Aerodynamic Performance of Swayasa Aircraft Wing Model against the Effect of Airfoil Flap Angle Configuration 2025][research_aerodynamic_performance_2025]\] \[[Ando and Yashiro 1976][research_ando_yashiro_1976]\] \[[Ashill 1970][research_ashill_1970]\] \[[Bay and Kara 2026][research_bay_kara_2026]\] \[[Bouton 1950][research_bouton_1950]\] \[[Burkett 1989][research_burkett_1989]\] \[[Butler 1982][research_butler_1982]\] \[[Butler 1983][research_butler_1983]\] \[[Chen and Mangione 1967][research_chen_mangione_1967]\] \[[Coe and Kulla 1974][research_coe_kulla_1974]\] \[[Finck 1978][research_finck_1978]\] \[[Frost and Rutherford 1963][research_frost_rutherford_1963]\] \[[GlBBINGS 1969][research_glbbings_1969]\] \[[Gu et al 2023][research_gu_ducvo_2023]\] \[[Haftka 1977][research_haftka_1977]\] \[[Hancock 1971][research_hancock_1971]\] \[[Hancock 1972][research_hancock_1972]\] \[[Hemsch and Nielsen 1983][research_hemsch_nielsen_1983]\] \[[Kendall 1985][research_kendall_1985]\] \[[Khalil et al 2022][research_khalil_asaro_2022]\] \[[Kida 1982][research_kida_1982]\] \[[Klein and Viswanathan 1973][research_klein_viswanathan_1973]\] \[[Kroo 1982][research_kroo_1982]\] \[[Laitone 1978][research_laitone_1978]\] \[[Laitone 1989][research_laitone_1989]\] \[[Lakshminarayana 1962][research_lakshminarayana_1962]\] \[[Lam 1993][research_lam_1993]\] \[[Lan 1986][research_lance_1986]\] \[[Li et al 2018][research_li_shen_2018]\] \[[Li et al 2018][research_li_zhang_2018]\] \[[Lockwood Taylor 1942][research_lockwoodtaylor_1942]\] \[[Lombardi and Vicini 1994][research_lombardi_vicini_1994]\] \[[Loth and Boyle 1969][research_loth_boyle_1969]\] \[[Lowe 1988][research_lowe_1988]\] \[[Lowson 1990][research_lowson_1990]\] \[[Lundry 1967][research_lundry_1967]\] \[[Lundry 1977][research_lundry_1977]\] \[[Lyapunov 1993][research_lyapunov_1993]\] \[[Mahdavi Zafarghandi and Reza Soltani 2024][research_mahdavizafarghandi_rezasoltani_2024]\] \[[Nangia et al 2003][research_nangia_palmer_2003]\] \[[Nonweiler 1960][research_nonweiler_1960]\] \[[Pangas and Gamboa 2025][research_pangas_gamboa_2025]\] \[[Report no. 121, The minimum induced Drag of aerofoils 1921][research_report_no_1921]\] \[[Report No. 349. A proof of the theorem regarding the distribution of lift over the span, for minimum induced drag 1930][research_report_no_1930]\] \[[Roskam et al 1972][research_roskamj_lanc_1972]\] \[[Sanders 1965][research_sanders_1965]\] \[[Shmilovich and Princen 2026][research_shmilovich_princen_2026]\] \[[Sibert 1937][research_sibert_1937]\] \[[Sibert 1943][research_sibert_1943]\] \[[Smith et al 2001][research_smith_komerath_2001]\] \[[Stanbrook 1954][research_stanbrook_1954]\] \[[Sugimoto 1992][research_sugimoto_1992]\] \[[Tormalm et al 2018][research_tormalm_leroy_2018]\] \[[Vukelich et al 1988][research_vukelich_stoy_1988_b]\] \[[Weihs and Katz 1986][research_weihs_katz_1986]\] \[[Weisshaar 1977][research_weisshaar_1977]\] \[[White et al 2015][research_whiteedwardv_kapaniarakeshk_2015]\] \[[Xu and Feng 2025][research_xu_feng_2025]\] \[[Xu and Zha 2021][research_xu_zha_2021]\] \[[Yamamoto 1992][research_yamamoto_1992]\] \[[Zeleke et al 2023][research_zeleke_asfaw_2023]\] \[[Zhai et al 2020][research_zhai_li_2020]\] \[[Zhijie et al 2025][research_zhijie_taiyu_2025]\]

### Relaxed static stability and the unstable airframe

Relaxed static stability, active control technology, the neutral point and the identification of unstable aircraft.

**62 records.** \[[Accelerated development and flight 1979][research_accelerated_development_1979]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]\] \[[Anderson et al 1973][research_anderson_berger_1973]\] \[[Ashkenas and Klyde 1989][research_ashkenasirvingl_klydedavidh_1989]\] \[[Blight et al 1986][research_blight_gangsaas_1986]\] \[[Boudreau 1977][research_boudreau_1977]\] \[[Buffington 1999][research_buffington_1999]\] \[[Crowe 1937][research_crowe_1937]\] \[[Curtiss 1971][research_curtiss_1971]\] \[[Curtiss and Howard C. 1961][research_curtiss_howardc_1961]\] \[[Enns et al 1992][research_enns_ozbay_1992]\] \[[Gilbert 1987][research_gilbertmichaelg_1987]\] \[[Guinn 1984][research_guinnwileya_1984]\] \[[Guinn et al 1983][research_guinnwileya_willeycraigs_1983]\] \[[Guinn et al 1984][research_guinnwileya_risingjerryj_1984]\] \[[Hanson and Stengel 1984][research_hanson_stengel_1984]\] \[[Hanson and Stengel 1981][research_hansongd_stengelrf_1981]\] \[[Hanson and Stengel 1983][research_hansongd_stengelrf_1983]\] \[[Jategaonkar and Thielecke 1994][research_jategaonkar_thielecke_1994]\] \[[Klein et al 1982][research_kleinrw_lapinsm_1982]\] \[[Kurzhals 1978][research_kurzhalspr_1978]\] \[[Kuttieri and Sinha 2023][research_kuttieri_sinha_2023]\] \[[Kwatny et al 1991][research_kwatny_bennett_1991]\] \[[Lapins et al 1982][research_lapinsm_kleinrw_1982]\] \[[Li et al 2016][research_li_guo_2016]\] \[[Li et al 2022][research_li_sun_2022]\] \[[Maine and Murray 1988][research_maine_murray_1988]\] \[[McRuer et al 1986][research_mcruerd_johnstond_1986]\] \[[Moorhouse and Jenkins 1975][research_moorhouse_jenkins_1975]\] \[[Moul and Brown 1959][research_moulmartint_brownlawrencew_1959]\] \[[Nagabhushan 1991][research_nagabhushan_1991]\] \[[Naihong et al 1993][research_naihong_yaohua_1993]\] \[[Nguyen et al 1979][research_nguyenlt_gilbertwp_1979]\] \[[Perry 1976][research_perrybiii_1976]\] \[[Perry 1982][research_perrybiii_1982]\] \[[Preissler and Schaufele 1991][research_preissler_schaufele_1991]\] \[[Ramamoorthy 1992][research_ramamoorthy_1992]\] \[[Rediess and Szalai 1975][research_rediessha_szalaikj_1975]\] \[[Rising et al 1984][research_risingjj_daviswj_1984]\] \[[Roache 1965][research_roache_1965]\] \[[Roberts et al 1977][research_robertspa_swaimrl_1977]\] \[[Rodgers 1965][research_rodgers_1965]\] \[[Rodgers 1966][research_rodgers_1966]\] \[[Rooney et al 1982][research_rooneyrh_chungjc_1982]\] \[[Sachs 1977][research_sachs_1977]\] \[[Shrivastava and Stengel 1989][research_shrivastava_stengel_1989]\] \[[Shrivastava 1987][research_shrivastavapc_1987]\] \[[Sizlo et al 1979][research_sizlotr_bergra_1979]\] \[[Sliwa 1980][research_sliwasm_1980]\] \[[Smith et al 1971][research_smith_hammer_1971]\] \[[Solies 1994][research_solies_1994]\] \[[Solies 1994][research_solies_1994_b]\] \[[Swaim 1970][research_swaim_1970]\] \[[Teel 1999][research_teel_1999]\] \[[Teel 1999][research_teel_1999_b]\] \[[Tomlinson 1973][research_tomlinson_1973]\] \[[Walker 1976][research_walkersa_1976]\] \[[Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]\] \[[Yang et al 2016][research_yang_zhao_2016]\] \[[Yin et al 2019][research_yin_chu_2019]\] \[[Zhang et al 2026][research_zhang_li_2026]\] \[[Zhou et al 2022][research_zhou_wang_2022]\]

**52 of the 62 records date from 1995 or earlier**, which is the shape a settled subject takes.

### Structural health monitoring and the digital twin

Structural health monitoring, model updating and the digital twin.

**51 records.** \[[Al-Hussein and Haldar 2015][research_alhussein_haldar_2015]\] \[[Broer et al 2022][research_broer_benedictus_2022]\] \[[Büchter et al 2021][research_buchter_sebastiasaez_2021]\] \[[Chabod and Baron 2020][research_chabod_baron_2020]\] \[[Chen et al 2015][research_chen_ren_2015]\] \[[Choi et al 2017][research_choi_shrestha_2017]\] \[[de Medeiros et al 2017][research_demedeiros_vandepitte_2017]\] \[[Deng et al 2024][research_deng_zeng_2024]\] \[[Di Sante 2015][research_disante_2015]\] \[[Galiana et al 2024][research_galiana_moradi_2024]\] \[[Gao et al 2017][research_gao_wu_2017]\] \[[Gao et al 2021][research_gao_ma_2021]\] \[[Giannakeas et al 2022][research_giannakeas_sharifkhodaei_2022]\] \[[Hervin and Fromme 2022][research_hervin_fromme_2022]\] \[[Houzibe and Chaki 2026][research_houzibe_chaki_2026]\] \[[Ibrahim 2026][research_ibrahim_2026]\] \[[Jeon et al 2025][research_jeon_choi_2025]\] \[[Kabashkin 2024][research_kabashkin_2024]\] \[[Karuskevich et al 2022][research_karuskevich_maslak_2022]\] \[[Kim and Youn 2025][research_kim_youn_2025]\] \[[Kong et al 2025][research_kong_jeon_2025]\] \[[Kwon et al 2019][research_kwon_park_2019]\] \[[Mei and Giurgiutiu 2018][research_mei_giurgiutiu_2018]\] \[[Ochôa et al 2019][research_ochoa_groves_2019]\] \[[Oyarhossein et al 2025][research_oyarhossein_sugiyama_2025]\] \[[Pedrioli et al 2026][research_pedrioli_vaiuso_2026]\] \[[Petriconi et al 2026][research_petriconi_lomazzi_2026]\] \[[Philibert et al 2022][research_philibert_yao_2022]\] \[[Qiu et al 2017][research_qiu_yuan_2017]\] \[[Qiu et al 2018][research_qiu_fang_2018]\] \[[Ren and Lissenden 2016][research_ren_lissenden_2016]\] \[[Ren et al 2017][research_ren_qiu_2017]\] \[[Ren et al 2018][research_ren_qiu_2018]\] \[[Romano et al 2019][research_romano_ciminello_2019]\] \[[Sen and Bhattacharya 2016][research_sen_bhattacharya_2016]\] \[[Sharqi and Cesnik 2023][research_sharqi_cesnik_2023]\] \[[Si and Baier 2016][research_si_baier_2016]\] \[[Sugumaran 2024][research_sugumaran_2024]\] \[[Walker and Kaufman 1977][research_walker_kaufman_1977]\] \[[Wang et al 2018][research_wang_wynn_2018]\] \[[Wang et al 2019][research_wang_qiu_2019]\] \[[Wang et al 2020][research_wang_liu_2020]\] \[[Wang et al 2021][research_wang_hu_2021]\] \[[Wang et al 2023][research_wang_wang_2023]\] \[[White et al 2017][research_white_mongru_2017]\] \[[Wilson et al 2024][research_wilson_champneys_2024]\] \[[Yue et al 2021][research_yue_khodaei_2021]\] \[[Yunker et al 2024][research_yunker_lake_2024]\] \[[Zhou et al 2025][research_zhou_shen_2025]\] \[[Zhou et al 2026][research_zhou_guan_2026]\] \[[Zhou et al 2026][research_zhou_li_2026]\]

### Topology optimisation and additive manufacture

Additive manufacture, lattice structures and topology optimisation of aerospace components.

**41 records.** \[[Abc 2023][research_abc_2023]\] \[[Ackermann and Haase 2023][research_ackermann_haase_2023]\] \[[Agrawal et al 2022][research_agrawal_gupta_2022]\] \[[Bester 2023][research_bester_2023]\] \[[Boado-Cuartero et al 2024][research_boadocuartero_perezalvarez_2024]\] \[[Cannella et al 2018][research_cannella_garinei_2018]\] \[[Carneiro and Gamboa 2019][research_carneiro_gamboa_2019]\] \[[Cheng et al 2019][research_cheng_liang_2019]\] \[[Chougule and Sonawane 2017][research_chougule_sonawane_2017]\] \[[Dagkolu et al 2021][research_dagkolu_gokdag_2021]\] \[[Daynes 2024][research_daynes_2024]\] \[[Di Caprio et al 2019][research_dicaprio_acanfora_2019]\] \[[Dzhurynskyi 2026][research_dzhurynskyi_2026]\] \[[Geng et al 2026][research_geng_zhao_2026]\] \[[Hu 2022][research_hu_2022]\] \[[Jia et al 2026][research_jia_feng_2026]\] \[[Kalms and Bergmann 2020][research_kalms_bergmann_2020]\] \[[Kambampati et al 2020][research_kambampati_townsend_2020]\] \[[Khan and Riccio 2024][research_khan_riccio_2024]\] \[[Kumar et al 2020][research_kumar_collini_2020]\] \[[Lee and Yun 2022][research_lee_yun_2022]\] \[[Li et al 2016][research_li_chen_2016]\] \[[Li et al 2021][research_li_wang_2021_c]\] \[[Li et al 2025][research_li_shi_2025_b]\] \[[Li et al 2026][research_li_yoon_2026]\] \[[Liu et al 2022][research_liu_kan_2022]\] \[[Lomo et al 2023][research_lomo_patel_2023]\] \[[Mei et al 2021][research_mei_wang_2021]\] \[[Nguyen 2019][research_nguyen_2019]\] \[[Obilanade et al 2025][research_obilanade_torlind_2025]\] \[[Oshima and Takano 2024][research_oshima_takano_2024]\] \[[Pierre et al 2023][research_pierre_iervolino_2023]\] \[[Su et al 2025][research_su_mo_2025]\] \[[Tsushima et al 2021][research_tsushima_tamayama_2021]\] \[[Wang 2021][research_wang_2021]\] \[[Wang and Song 2025][research_wang_song_2025]\] \[[Wang and Xia 2022][research_wang_xia_2022]\] \[[Wang et al 2021][research_wang_zhang_2021]\] \[[Wang et al 2022][research_wang_zhang_2022]\] \[[Zhang et al 2025][research_zhang_bai_2025]\] \[[Zhao et al 2022][research_zhao_ji_2022]\]

**All 41 records date from 2016 or later.**

### Uncertainty quantification and reliability

Uncertainty quantification, reliability and robust design optimisation.

**35 records.** \[[Ballester Claret et al 2024][research_ballesterclaret_coelho_2024]\] \[[Bhachu et al 2015][research_bhachu_haftka_2015]\] \[[Chatterjee et al 2019][research_chatterjee_chowdhury_2019]\] \[[Cheng et al 2015][research_cheng_zhou_2015]\] \[[Da Ronch et al 2019][research_daronch_drofelnik_2019]\] \[[Elyasi et al 2020][research_elyasi_roudbari_2020]\] \[[Geisler and Junker 2024][research_geisler_junker_2024]\] \[[Gong et al 2026][research_gong_he_2026]\] \[[Hanazaki and Yamazaki 2024][research_hanazaki_yamazaki_2024]\] \[[Hozić et al 2023][research_hozic_thore_2023]\] \[[Jagana et al 2026][research_jagana_rajagopalan_2026]\] \[[McGurk et al 2024][research_mcgurk_stodieck_2024]\] \[[Missoum 2012][research_missoum_2012]\] \[[Savin and Hantrais-Gervois 2020][research_savin_hantraisgervois_2020]\] \[[Sharma et al 2023][research_sharma_swain_2023]\] \[[Sleesongsom et al 2022][research_sleesongsom_kumar_2022]\] \[[Sofi 2015][research_sofi_2015]\] \[[Song and Mignolet 2018][research_song_mignolet_2018]\] \[[Spagnol et al 2019][research_spagnol_riche_2019]\] \[[Suryawanshi and Ghosh 2015][research_suryawanshi_ghosh_2015]\] \[[Thanusha and Sarkar 2016][research_thanusha_sarkar_2016]\] \[[Thomas and Dowell 2025][research_thomas_dowell_2025]\] \[[Tsai and Malak 2024][research_tsai_malak_2024]\] \[[van den Brandt and de Visser 2018][research_vandenbrandt_devisser_2018]\] \[[Vermiglio 2017][research_vermiglio_2017]\] \[[Wang and Qing 2016][research_wang_qing_2016]\] \[[Wang et al 2025][research_wang_tian_2025]\] \[[Wansaseub et al 2020][research_wansaseub_sleesongsom_2020]\] \[[Wauters 2021][research_wauters_2021]\] \[[Wei and Du 2019][research_wei_du_2019]\] \[[Xia et al 2016][research_xia_li_2016]\] \[[Xie et al 2021][research_xie_li_2021]\] \[[Zhao and Zhou 2024][research_zhao_zhou_2024]\] \[[Zhou et al 2019][research_zhou_ruan_2019_b]\] \[[Özdemir 2021][research_ozdemir_2021]\]

### The Southwell method, Rayleigh-Ritz and assumed modes

The Southwell method of predicting a critical load from subcritical measurement, and the Rayleigh-Ritz and assumed-modes methods of the article's structural model.

**28 records.** \[[An anal ysis of the test loading of a flexible pipe arch, using the Southwell plot, shows that the method has promise as a general inspection technique for buried structures such as large diameter corrugated plate arches on motorw y construction projects 1974][research_an_anal_1974]\] \[[Ariaratnam 1961][research_ariaratnam_1961]\] \[[Craver and Egle 1972][research_craver_egle_1972]\] \[[Crisfield 1978][research_crisfield_1978]\] \[[Dawe and Roufaeil 1980][research_dawe_roufaeil_1980]\] \[[Deobald and Gibson 1988][research_deobald_gibson_1988]\] \[[Gelos and Laura 1990][research_gelos_laura_1990]\] \[[Gorman and Singhal 1993][research_gorman_singhal_1993]\] \[[Hatake 1985][research_hatake_1985]\] \[[Hatake 1986][research_hatake_1986]\] \[[Kalam 1981][research_kalam_1981]\] \[[Koh and Kelly 1989][research_koh_kelly_1989]\] \[[Lam et al 1989][research_lam_hung_1989]\] \[[Laura and Viazzi 1985][research_laura_viazzi_1985]\] \[[Leicester 1970][research_leicester_1970]\] \[[Liew and Wang 1993][research_liew_wang_1993]\] \[[Lim et al 1989][research_lim_senthilnathan_1989]\] \[[Roorda 1967][research_roorda_1967]\] \[[Roufaeil and Dawe 1982][research_roufaeil_dawe_1982]\] \[[Savithri and Varadan 1990][research_savithri_varadan_1990]\] \[[Singer 1989][research_singer_1989]\] \[[Singhvi and Kapania 1994][research_singhvi_kapania_1994]\] \[[Southwell et al 1981][research_southwell_gunn_1981]\] \[[Spencer and Walker 1975][research_spencer_walker_1975]\] \[[Valsangkar et al 1982][research_valsangkar_britto_1982]\] \[[Walker and Hall 1968][research_walker_hall_1968]\] \[[Wang and Thevendran 1993][research_wang_thevendran_1993]\] \[[Wang et al 1994][research_wang_wang_1994]\]

**None of the 28 records is later than 1994.** Nine titles name the Southwell method, and none of them names a wing, an aircraft or flight.

### Manoeuvre performance, agility and energy methods

Manoeuvre performance, agility, energy methods and the minimum-time climb.

**18 records.** \[[Bryson et al 1969][research_bryson_desai_1969]\] \[[Calise 1977][research_calise_1977]\] \[[Flight performance handbook for powered flight operations 1963][research_flight_performance_1963]\] \[[Friend and Sakamoto 1978][research_friendel_sakamotogm_1978]\] \[[Godwin et al 1964][research_godwin_frazier_1964]\] \[[Hallissy and Ayers 1977][research_hallissyjb_ayerstg_1977]\] \[[Johnson 1972][research_johnson_1972]\] \[[Liefer 1990][research_lieferrandallk_1990]\] \[[Nguyen and Gilert 1990][research_nguyenluatt_gilertwilliamp_1990]\] \[[Papadales and Basil S. 1979][research_papadales_basils_1979]\] \[[Ray et al 1972][research_rayej_mckinneylw_1972]\] \[[Ray et al 1973][research_rayej_mckinneylw_1973]\] \[[Shayak et al 2024][research_shayak_girdhar_2024]\] \[[Tamboli 1956][research_tamboli_1956]\] \[[Theodorsen 1959][research_theodorsen_1959]\] \[[Well and Berger 1982][research_well_berger_1982]\] \[[Wood and Livingston 1971][research_wood_livingston_1971]\] \[[Wrestler and Clifton G. 1965][research_wrestler_cliftong_1965]\]

## Where the Framing Breaks Down

**The keystone inversion rests on a single quoted figure, and the figure is a prediction rather than a measurement.**
The elastic-to-rigid ratio of 1.6 is described in the source as predicted, so the divergence dynamic
pressure derived from it is the boundary the designers believed in and not the one the aircraft had \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\]. The
flight record says the real boundary was lower \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].
**Every number in this article that descends from 4,533 pounds per square foot inherits that, and it matters most in the Southwell sensitivity analysis, because that analysis uses the same figure to describe how well the figure could have been measured.**

**The elasticity derived earlier puts a number on that rounding.**

$$ \frac{\Delta q_D}{q_D} \approx -\frac{1}{r-1}\cdot\frac{\Delta r}{r} = -1.667 \times \left(\pm\frac{0.05}{1.6}\right) = \mp 5.2\ \mathrm{percent} $$

**The ratio is also quoted as about 1.6, and the rounding is not harmless.** At 1.55 the implied boundary is
4,791 pounds per square foot and at 1.65 it is 4,315, a spread of about ten percent from a figure given to
two significant figures. The margin of 2.667 is really a margin between about 2.54 and 2.82.

**The two-mode structural model is a scaling argument and nothing more.** It uses strip theory, neglects
compressibility, neglects the canard's downwash entirely on a wing whose inboard loading is
strongly influenced by that downwash \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\], and assumes a uniform wing where the real structural box transitions from
unswept to swept. **Its absolute numbers are meaningless and are never quoted.** The results taken from it
are the sweep trend, the coupling requirement and the elimination threshold, all of which are ratios.

**The pitch inertia is assumed and the doubling times scale as its square root.** A factor of two error in
inertia is a factor of 1.41 in every time in that table.

**The trim comparison assumes a section pitching moment that was never published**, and the taper ratio
behind the transonic argument is likewise assumed. Both are stated in their tables as sensitivities for that
reason.

**The aircraft was not asked the question that would have tested the planform hardest.** The supersonic drag
was never measured during the phase reported here, because afterburner fuel flow was not instrumented
\[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\]. The
forward-swept wing's transonic case therefore rests on subsonic polar data and on tunnel work.

**And the largest limitation is not technical.** The programme was a success by its own criteria and the
configuration was never adopted.
**An article organised around whether the aeroplane worked will conclude that it did and will miss the fact that this changed nothing about how aircraft are shaped.**

## The Source Base

**This is the best-documented subject in this series in a long while, and the contrast with the X-27 and the X-28 is the point.**

**The vehicle's own record is deep.** The National Aeronautics and Space Administration's Technical Reports
Server returns a large body of work under the aircraft's own designation, including the preliminary flight
assessment, the structural loads flight testing, the flight-determined lift and drag characteristics, the
flight control system lessons learned, the buffet and control system interaction, and the canard and control
system interaction. **This subject's literature is found under the aircraft's own name**, which is the
reverse of the X-27 and the X-28, whose designations carry essentially no literature of their own and whose
evidence lies in the physics beneath them.

**Two primary documents carry most of the quantitative content of this article.** The preliminary flight
assessment supplies the control system description, the static margin, the update rate and the
Southwell application. The structural loads flight testing paper supplies the planform geometry, which the
flight test overview of [Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989] also gives, the structural axis sweep, the
elastic-to-rigid ratio, the design dynamic pressure and the canard torsion axis location.
**The keystone result exists because those two figures appear in the same paragraph of the same report.**

**The vehicle facts nonetheless disagree between secondary sources**, principally on the number of flights
each aircraft made and on the total for the programme. The article reports the disagreement rather than
choosing.

**The physics record is deeper still and long predates the aircraft.** Divergence, aeroelastic tailoring,
relaxed static stability and digital flight control each have substantial primary literatures, and the wind
tunnel divergence experiments on forward-swept wings that the flight programme cites are themselves a
well-documented body of work.

**The research survey holds 3,201 research records drawn from the National Aeronautics and Space Administration's Technical Reports Server, the Defense Technical Information Center and the journal literature indexed by Crossref**, of which 709 are report primaries, being 22.1 percent, by the identifier rule set out under The Definition of Primary. **The median publication year is 2017.** Of the 3,199 dated records, 1,196 were published in 1995 or earlier, the period of the aircraft's design, flight programme and reports, being 37.4 percent, and 1,840 were published in 2015 or later, being 57.5 percent.

### The Definition of Primary

**Primacy is a property of the document, and this survey derives it from the identifier.** A record is a report primary when its address is on the NASA Technical Reports Server or it carries a digital object identifier under the 10.21236 prefix, which Crossref registers for Defense Technical Information Center reports. **Of the 76 titles that name the X-29, 67 are report primaries**, which is what the aircraft's own record looks like under that rule. **The rule does not reach the journal papers**, such as the divergence and tailoring papers of the Journal of Aircraft, so 22.1 percent is a lower bound on how much of the survey is first-hand.

### Thin Subjects

**Writing an equation down creates a citation obligation for the mechanics beneath it, and the mechanics are not the same literature as the technology.** The survey therefore holds, beside the literature of the aircraft's technologies, clusters on the Southwell method and assumed modes, on sampled-data control and time delay, and on divergence and static aeroelasticity. **Ten subjects that this article's derivations depend on nonetheless have thin literatures.** Each count below is the number of research records in this survey whose title carries at least one of the listed terms, with a hyphen read as a space. Where a row joins two groups of terms with the word together, a title must carry a term from each group.

| Subject | Title terms counted | Records |
|---|---|---|
| the time to double of an unstable airframe | time to double, doubling time, time to half | 0 |
| the elastic-to-rigid lift ratio | elastic to rigid, flexible to rigid, rigid to flexible, lift effectiveness | 0 |
| washin of a swept wing under load | washin, wash in | 0 |
| isobar sweep | isobar, isobars | 0 |
| torsion of a canard | canard, canards together with torsion, torsional, spindle, pitch stiffness | 0 |
| sustained turning performance | sustained turn, specific excess power, excess thrust, excess power | 0 |
| the laminate stiffness matrix | positive definite, stiffness matrix | 0 |
| the Southwell method applied to a wing or in flight | Southwell together with wing, aeroelastic, divergence, flight, flutter, aircraft | 0 |
| divergence measured in flight | divergence together with flight | 1 |
| failure voting in a redundant control system | voter, voters, voting | 2 |

**Most of the quantities the derivations turn on are never the subject of a title.** No title names the time to double of an unstable airframe, the elastic-to-rigid lift ratio, washin of a swept wing under load, isobar sweep or torsion of a canard. Each appears in this literature, if at all, inside work titled by its subject, being unstable airframe control, static aeroelasticity, transonic wing design and canard aerodynamics, so the article's figures for them stand on the relations derived above.

**The Southwell method has a literature, and it is not about wings.** Nine titles name it, and none names a wing, an aircraft or flight. They treat the method itself, columns and beam-columns, buried flexible pipes and plastic buckling, which agrees with the primary record's statement that the X-29 was the first aircraft to which it was applied in flight.

**Divergence measured in flight is the subject of one title**, a 1988 report of flight test experience with the structural divergence of forward-swept wings, the configuration the X-29 flew.

**Failure voting appears in two titles**, from 1977 and 1993, while the redundancy literature itself is large, with 274 records in the cluster on digital fly-by-wire, redundancy and fault tolerance. The argument that redundancy on this aircraft was a question about time rests on the article's own arithmetic rather than on a published analysis of voter latency.

**No research record carries sustained turn, specific excess power or excess thrust in its title, and the work is not missing.** It lives under **energy state, energy manoeuvrability and time to climb**, the vocabulary the period actually used, and 6 titles name energy state, energy manoeuvrability, energy methods or the time to climb.

**No research record carries positive definite or stiffness matrix in its title either**, because the mechanics of the bend-twist coupling matrix are written up inside the composite structure literature, where 394 of this article's research records carry composite or composites in their titles, and inside the aeroelastic tailoring literature, where 74 carry tailored or tailoring in theirs.
**A paper on tailoring a wing is a paper about that stiffness matrix**, and reporting a gap there would misdescribe where the work is.

### What the Survey Admits

**A record is admitted only when a person reading its title finds it on this article's subject.** Several words this subject depends on also name something else, and a record that shares only such a word is excluded. Southwell is also the name of the Jesuit poet Robert Southwell, of Southwell Cathedral and of a cestode parasite of the Indian shad. Canard also names the duck, in poultry science and cookery, and a false story. Agility also names a quality of military doctrine and of enterprise management, and divergence names quantities in intracranial pressure, meteorology, statistics and economics. Flutter also names the motion of paper sheets, air-cushion skirts and planing plates, and transonic also describes compressors, fans and turbines. Control, vehicle and fault tolerance also name automotive suspension, steering and braking, ships and submarines, power converters and electric motors, industrial robots and cranes, chemical reactors, civil structures, supply chains, airfares and flight delays. Spacecraft, rockets and launch vehicles, missile guidance, and helicopter rotors and helicopter test reports share the vocabulary of aeroelasticity, stability and control without sharing this aircraft's problem, and records about them alone are excluded, as are insect, bird and bat flight and the notch filters of power electronics and signal processing. Flow-control, drag-reduction and lift-augmentation devices on wings and sections are excluded unless the record concerns vortex flow at high angle of attack, shock control within transonic section design, buffet, or a flight-control or load-alleviation effect. So are engine, inlet, nacelle and nozzle hardware, marine and tidal hydrodynamics, store carriage and separation, fuel tanks, landing gear, icing, lightning protection and crashworthiness, the inspection and fatigue of metal airframes, propeller, proprotor and turbomachinery blades, and wind-turbine rotors other than their bend-twist coupling, because the argument uses none of them. Program listings, user and programmer's manuals, textbook chapters on general mathematics, and conference volumes and their front matter are excluded as items rather than research works. Civil structures, reliability theory and digital-twin frameworks that name no aircraft, the numerical analysis of approximation methods, and rotorcraft subsystems are excluded as well, while structural model updating stays admitted. Correction, errata, retraction and withdrawal notices, retracted articles, book reviews, conference announcements, news items and reference entries are excluded as well, because a survey counts research works and those are notices attached to works rather than works. Where the same document is registered twice, as a digest and as the paper or under two identifiers for one paper, one record is kept.

**Some records of doubtful relevance are kept.** Generic control, estimation and optimisation theory, structural mechanics theory, quadrotor and other unmanned-vehicle flight control, networked control theory, bridge and hydrofoil flutter, marine and wind-turbine bend-twist coupling, canard and high angle of attack aerodynamics of missiles, and rotorcraft handling qualities each share the mathematics or the vocabulary of the aircraft's structural, aerodynamic or control problem, so each is kept and a reader may weigh it accordingly.

**Every research title has been read for relevance, so the off-topic share that remains is a matter of reading judgement.** A reading of titles cannot show that a work is relevant in substance, so this is a statement about titles only.

## Epistemic State

**Historical fact, well attested.**

- The Defense Advanced Research Projects Agency began the X-29A project in 1977 \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].
- The aircraft was designed and built by the Grumman Aerospace Corporation and flown at the Dryden
  Flight Research Facility \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].
- Two aircraft were built, the first flying on 14 December 1984 \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\] \[[Gelzer 2015][ref_gelzer_x29]\].
- The wing has a leading edge swept 29.3 degrees forward, a structural axis swept 36.2 degrees forward,
  an aspect ratio of 4.0 and a trapezoidal reference area of 185 square feet \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\]
  \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\]. The wing area of 188.84 square feet used for the ratios in this article comes from
  the encyclopaedia entry alone \[[Grumman X-29][ref_x29]\].
- The wing skins are graphite-epoxy composite, aeroelastically tailored to inhibit structural
  divergence \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].
- The static margin is nominally 35 percent negative subsonically, and the instability is created by
  the canard rather than by the wing \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\] \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].
- The flight control system is triplex digital fly-by-wire updating at 40 hertz, with digital and
  analog reversionary modes \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].
- Pitch control is by three surfaces, namely the all-moving canard, the dual-hinged full-span
  flaperons, and the aft strake flaps \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].
- The canard area is 20 percent of the wing reference area \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].
- The airframe reuses the forward fuselage and nose gear of an F-5A, the main landing gear and
  servo-actuators of an F-16, and F-14 avionics \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\].
- Envelope expansion was completed in 84 flights over two years \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].
- The Southwell technique was applied to flight test data for the first time on this aircraft \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].

**Reported in the primary literature and taken as given here.**

- That the predicted elastic-to-rigid wing lift-curve-slope ratio was about 1.6 at the design dynamic
  pressure of 1,700 pounds per square foot \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].
- That induced drag in flight was as much as 20 percent below wind tunnel estimates above a lift
  coefficient of 0.8 \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\].
- That the flight-estimated divergence speed was lower than predicted but remained outside the flight
  envelope \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].
- That canard torsion loads exceeded predictions transonically and were not fully understood \[[Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]\].
- That the tailored skins carried an insignificant weight penalty over the basic strength design \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].

**Contested in the sources and left contested.**

- The number of flights made by each aircraft and by the programme as a whole \[[Gelzer 2015][ref_gelzer_x29]\] \[[Jenkins, Landis and Miller][ref_xvehicles]\]
  \[[Grumman X-29][ref_x29]\].
- Whether the configuration reduced drag, which the subsonic polar data support \[[Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]\] and
  which the agency history and the inventory deny overall \[[Gelzer 2015][ref_gelzer_x29]\] \[[Jenkins, Landis and Miller][ref_xvehicles]\].

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
  The primary record states the fact in one sentence and draws no conclusion from it \[[Sims et al 1989][research_simsrobert_mccrossonpaul_1989]\].
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
requirement holds across the plausible range of the stiffnesses the record does not give.
**The technology worked and it was not working easily.**

**The margin itself was smaller than it sounds.** A factor of 2.667 in dynamic pressure is a factor of 1.633
in speed, and at the design point the wing was already amplifying its lift by sixty percent. Between
three thousand and four thousand pounds per square foot that amplification triples.
**The aircraft lived on the flat part of a curve that has no flat part near its end.**

**The control system's problem was the same problem in a different currency.** At the corner of the envelope
the airframe doubled a pitch disturbance in about a tenth of a second, which is four frames at forty hertz,
of which the act of sampling consumed thirty-seven milliseconds. A voter needing three frames to isolate a
failed channel spent three quarters of a doubling time doing it.
**Redundancy on this aircraft was a question about time rather than about probability**, the finding
most worth carrying forward.

**And the two halves were never separable, which the aircraft demonstrated in the most direct way available.**
The canard's own divergence boundary was set not by its spindle but by the stiffness of the pitch loop that
a control law required. **A control requirement fixed a structural boundary.** The programme was organised
as a structures problem and a controls problem, and the aeroplane declined to be divided that way.

**The planform lost and everything it forced won.** No production fighter flies a forward-swept wing \[[Forward-swept wing][ref_fsw]\].
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
- [Forward-swept wing][ref_fsw]
- [General Dynamics F-16 Fighting Falcon][ref_f16]
- [General Electric F404][ref_f404]
- [Gelzer, X-29 Advanced Technology Demonstrator Aircraft][ref_gelzer_x29]
- [Grumman Aerospace Corporation][ref_grumman]
- [Grumman F-14 Tomcat][ref_f14]
- [Grumman X-29][ref_x29]
- [HFB 320 Hansa Jet][ref_hansajet]
- [Jenkins, Landis and Miller, American X-Vehicles][ref_xvehicles]
- [Junkers Ju 287][ref_ju287]
- [Northrop F-5][ref_f5]
- [Relaxed stability][ref_relaxed_stability]
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
[ref_fsw]: https://en.wikipedia.org/wiki/Forward-swept_wing
[ref_gelzer_x29]: https://www.nasa.gov/aeronautics/nasa-aircraft/x-29-demonstrator/
[ref_grumman]: https://en.wikipedia.org/wiki/Grumman
[ref_hansajet]: https://en.wikipedia.org/wiki/HFB_320_Hansa_Jet
[ref_himat]: https://en.wikipedia.org/wiki/Rockwell_HiMAT
[ref_ju287]: https://en.wikipedia.org/wiki/Junkers_Ju_287
[ref_laminate]: https://en.wikipedia.org/wiki/Composite_laminate
[ref_relaxed_stability]: https://en.wikipedia.org/wiki/Relaxed_stability
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

- [044 Finite worldlength control of sampled data systems by covariance assignment 1994][research_044_finite_1994]
- [057 H∞ control design for a class of uncertain sampled-data systems 1994][research_057_h_1994]
- [130 Sampled-data decentralized controller design 1994][research_130_sampled_data_1994]
- [185 A fourier series lifting approach to H∞ sampled data control 1994][research_185_a_1994]
- [214 Application of restructurable flight control system to an airliner 1994][research_214_application_1994]
- [A feasibility review of SMC-MIMO based control architecture for high angle of attack flight 2019][research_a_feasibility_2019]
- [A Generalization for Model Reference Adaptive Control and Robust Model Reference Adaptive Control Adaptive Laws for a Class of Nonlinear Uncertain Systems with Application to Control of Wing Rock Phenomenon 2020][research_a_generalization_2020]
- [A hybrid adaptive control scheme using sampled data and intersampling compensation 1995][research_a_hybrid_1995]
- [A Spreadsheet Tool for the AERODAS Model for Calculating Airfoil Pre-Stall and Post-Stall Lift and Drag Characteristics 2018][research_a_spreadsheet_2018]
- [A study of the 1973][research_a_study_1973]
- [Aamir et al 2026][research_aamir_abbasi_2026]
- [Abbas and Morgenthal 2016][research_abbas_morgenthal_2016]
- [Abc 2023][research_abc_2023]
- [Abdul Huq and Beebi M 2015][research_abdulhuq_beebim_2015]
- [Abdul Rashid et al 2025][research_abdulrashid_syedmohddardin_2025]
- [Abdul-Kaiyoom et al 2025][research_abdulkaiyoom_yildirim_2025]
- [Abdullah et al 2019][research_abdullah_akbar_2019]
- [Abed et al 2024][research_abed_alhamadani_2024]
- [Abel et al 1966][research_abeli_ruhlincl_1966]
- [Abele and Sanlorenzo 1975][research_abele_sanlorenzo_1975]
- [Abele et al 1973][research_abele_ruger_1973]
- [Abichandani and Rosenberg 1952][research_abichandani_rosenberg_1952]
- [Abou-Kebeh et al 2025][research_aboukebeh_gilpita_2025]
- [Abouheaf et al 2020][research_abouheaf_gueaieb_2020]
- [AbuNawas and Qawasmeh 2026][research_abunawas_qawasmeh_2026]
- [Accelerated development and flight 1979][research_accelerated_development_1979]
- [Ackerman et al 2017][research_ackerman_xargay_2017]
- [Ackermann and Haase 2023][research_ackermann_haase_2023]
- [Ackermann and Isermann 1973][research_ackermann_isermann_1973]
- [Acoustic emission monitors damage progression in graphite/epoxy composite structure 1981][research_acoustic_emission_1981]
- [Acoustic emissions and transient elastic waves in an orthotropic laminate plate 1989][research_acoustic_emissions_1989]
- [Acquatella et al 2017][research_acquatellab_vanekeren_2017]
- [Adams and Hatch 1971][research_adams_hatch_1971]
- [Adan and Sheinman 1988][research_adan_sheinman_1988]
- [Adegbindin et al 2016][research_adegbindin_love_2016]
- [Adler and Martins 2023][research_adler_martins_2023]
- [Adney and Horn 1984][research_adneyps_hornwj_1984]
- [Advanced Control Techniques for Unmanned Aerial Vehicle (UAV) Navigation and Flight Control 2023][research_advanced_control_2023]
- [Aero structural optimization for sailplane wing in preliminary design 2018][research_aero_structural_2018]
- [Aerodynamic Performance of Swayasa Aircraft Wing Model against the Effect of Airfoil Flap Angle Configuration 2025][research_aerodynamic_performance_2025]
- [Aggarwal and Cranch 1967][research_aggarwal_cranch_1967]
- [Aghababa 2018][research_aghababa_2018]
- [Agrawal et al 2022][research_agrawal_gupta_2022]
- [Agrell and Elmeland 1985][research_agrell_elmeland_1985]
- [Aguilar-Ibañez 2016][research_aguilaribanez_2016]
- [AHarrah 2007][research_aharrahralphc_2007]
- [Ahmadi 1988][research_aliahmadi_1988]
- [Ahmadi and Farsadi 2024][research_ahmadi_farsadi_2024]
- [Ahmadi Dastgerdi et al 2022][research_ahmadidastgerdi_asadi_2022]
- [Ahmadi et al 2024][research_ahmadi_farsadi_2024_b]
- [Ahmadian et al 2025][research_ahmadian_alitalebi_2025]
- [Ahmed and Chen 2021][research_ahmed_chen_2021]
- [Ahmed et al 2025][research_ahmed_elbanna_2025]
- [Aidala 1985][research_aidala_1985]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]
- [Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967]
- [Air Force Test Pilot School Edwards Afb Ca 1967][research_airforcetestpilotschooledwardsafbca_1967_b]
- [Air Force Test Pilot School Edwards Afb Ca 1969][research_airforcetestpilotschooledwardsafbca_1969]
- [Air Force Test Pilot School Edwards Afb Ca 1981][research_airforcetestpilotschooledwardsafbca_1981]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_c]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988_d]
- [Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_d]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_e]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991]
- [Air Force Test Pilot School Edwards Afb Ca 1991][research_airforcetestpilotschooledwardsafbca_1991_b]
- [Air Force Test Pilot School Edwards Afb Ca 1993][research_airforcetestpilotschooledwardsafbca_1993]
- [Ajaj et al 2021][research_ajaj_parancheerivilakkathil_2021]
- [Ajel et al 2021][research_ajel_humaidi_2021]
- [Akbari et al 2025][research_akbari_galeani_2025]
- [Aker and Alukonis 1976][research_aker_alukonis_1976]
- [Al-Hussein and Haldar 2015][research_alhussein_haldar_2015]
- [Al-Jaburi et al 2019][research_aljaburi_feszty_2019]
- [Alag and Kaufman 1975][research_alag_kaufman_1975]
- [Alam et al 2015][research_alam_hromcik_2015]
- [Alcaina et al 2019][research_alcaina_cuenca_2019]
- [Ale Isaac et al 2023][research_aleisaac_ragab_2023]
- [Alexander 1991][research_alexander_1991]
- [Alexander et al 1996][research_alexander_tzeng_1996]
- [Alhajahmad and Mittelstedt 2021][research_alhajahmad_mittelstedt_2021]
- [Ali 1997][research_alisyedfirasat_1997]
- [Ali et al 2026][research_ali_chen_2026]
- [Alizadeh et al 2020][research_alizadeh_ebrahimi_2020]
- [Allen et al 1983][research_allen_bradley_1983]
- [Allen et al 1984][research_allen_bradley_1984]
- [Allison and Dagenhart 1987][research_allisondenniso_dagenhartjray_1987]
- [Almosnino 1985][research_almosnino_1985]
- [Alsaidi et al 2019][research_alsaidi_joe_2019]
- [Alsaidi et al 2019][research_alsaidi_joe_2019_b]
- [Altunkaya and Özkol 2025][research_altunkaya_ozkol_2025]
- [Alwan and Hussain 2026][research_salwan_hussain_2026]
- [Alyanak and Pendleton 2017][research_alyanak_pendleton_2017]
- [An anal ysis of the test loading of a flexible pipe arch, using the Southwell plot, shows that the method has promise as a general inspection technique for buried structures such as large diameter corrugated plate arches on motorw y construction projects 1974][research_an_anal_1974]
- [An et al 2017][research_an_khoo_2017]
- [An et al 2020][research_an_guo_2020]
- [An et al 2026][research_an_zhang_2026]
- [Anderson 1970][research_anderson_1970]
- [Anderson 1976][research_andersonca_1976]
- [Anderson 1985][research_anderson_1985]
- [Anderson and Toivanen 1970][research_anderson_toivanen_1970]
- [Anderson et al 1973][research_anderson_berger_1973]
- [Ando and Yashiro 1976][research_ando_yashiro_1976]
- [Andrés-Pérez et al 2016][research_andresperez_gonzalezjuarez_2016]
- [Ang and Ng 2026][research_ang_ng_2026]
- [Ang et al 2024][research_ang_leo_2024]
- [Anikin et al 2015][research_anikin_animitsa_2015]
- [Annadata et al 2024][research_annadata_endesfelder_2024]
- [Ansari et al 2023][research_ansari_zucco_2023]
- [Ansell et al 1982][research_ansellgs_loewyrg_1982]
- [Antonakis 2025][research_antonakis_2025]
- [Antonakis 2025][research_antonakis_2025_b]
- [Antonakis and Biannic 2024][research_antonakis_biannic_2024]
- [Application Analysis on Fly-by-Wire Flight Control System on Large Transport Aircraft 2022][research_application_analysis_2022]
- [Application Status and Future Prospect of Aircraft Morphing Wing 2023][research_application_status_2023]
- [Ardema and Williams 1972][research_ardemamd_williamslj_1972]
- [Arena and Lacarbonara 2012][research_arena_lacarbonara_2012]
- [Argha et al 2018][research_argha_su_2018]
- [Argha et al 2019][research_argha_su_2019]
- [Ariaratnam 1961][research_ariaratnam_1961]
- [Arif and Sasongko 2021][research_arif_sasongko_2021]
- [Ariyarit and Kanazaki 2017][research_ariyarit_kanazaki_2017]
- [Armah 2018][research_karmah_2018]
- [Armanious and Lind 2017][research_armanious_lind_2017]
- [Armstrong 1977][research_armstrong_1977]
- [Armstrong et al 2006][research_armstrong_lindberg_2006]
- [Arnault et al 2016][research_arnault_dandois_2016]
- [Arnold 1942][research_arnold_1942]
- [Asadi Khanouki et al 2019][research_asadikhanouki_javadiaghdam_2019]
- [Ascani 1974][research_ascani_1974]
- [Asgari and Kouchakzadeh 2016][research_asgari_kouchakzadeh_2016]
- [Ashill 1970][research_ashill_1970]
- [Ashkenas 1984][research_ashkenas_1984]
- [Ashkenas and Klyde 1989][research_ashkenasirvingl_klydedavidh_1989]
- [Ashton 1970][research_ashton_1970]
- [Ashworth et al 1986][research_ashworth_waltrip_1986]
- [Ashworth et al 1988][research_ashworth_mouch_1988]
- [Aslam and Chen 2018][research_aslam_chen_2018]
- [Aston and Williams 1994][research_aston_williams_1994]
- [Atmaca et al 2025][research_atmaca_devisser_2025]
- [Audoin and Baste 1994][research_audoin_baste_1994]
- [Autenrieb 2025][research_autenrieb_2025]
- [Autonomous flight control of drone equipped with microcomputer for flight control and GPS 2018][research_autonomous_flight_2018]
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
- [Badaliance and Dill 1981][research_badaliance_dill_1981]
- [Badalló et al 2015][research_badallo_trias_2015]
- [Badhurshah et al 2024][research_badhurshah_alvarez_2024]
- [Badihi et al 2026][research_badihi_nezhad_2026]
- [Bagherzadeh 2026][research_bagherzadeh_2026]
- [Bagherzadeh et al 2025][research_bagherzadeh_mohammadkarimi_2025]
- [Bahamonde Jacome and Elham 2017][research_bahamondejacome_elham_2017]
- [Bahr et al 2021][research_bahr_mckay_2021]
- [Bai 2018][research_bai_2018]
- [Bai et al 2022][research_bai_xu_2022]
- [Bailey and Knotts 1990][research_baileyre_knottslh_1990]
- [Bailey and Smith 1981][research_baileyre_smithre_1981]
- [Bailey et al 1988][research_baileyrandalle_powersbruceg_1988]
- [Baker et al 1985][research_baker_jones_1985]
- [Bakunowicz and Meyer 2016][research_bakunowicz_meyer_2016]
- [Balaji et al 2024][research_balaji_manickam_2024]
- [Balakrishnan 2000][research_balakrishnan_2000]
- [Balakrishnan and Tuffaha 2012][research_balakrishnan_tuffaha_2012]
- [Balatti et al 2021][research_balatti_haddadkhodaparast_2021]
- [Balatti et al 2022][research_balatti_khodaparast_2022]
- [Baldan and Guardone 2024][research_baldan_guardone_2024]
- [Ballester Claret et al 2024][research_ballesterclaret_coelho_2024]
- [Balunov et al 2023][research_balunov_solyaev_2023]
- [Bandyopadhyay 1989][research_bandyopadhyay_1989]
- [Bandyopadhyay 1991][research_bandyopadhyay_1991]
- [Banerjee 2019][research_banerjee_2019]
- [Banks 1988][research_banks_1988]
- [Banks 1988][research_banksdanielw_1988]
- [Bantscheff and Breitsamter 2023][research_bantscheff_breitsamter_2023]
- [Bao et al 2025][research_bao_li_2025]
- [Bar-Gill and Stengel 1986][research_bargill_stengel_1986]
- [Bar-Shalom 1985][research_barshalom_1985]
- [Bar-Shalom 1989][research_barshalom_1989]
- [Bar-Shalom 1990][research_barshalom_1990]
- [Barabanov and Ortega 2017][research_barabanov_ortega_2017]
- [Baranovski and Mikhailovskiy 2020][research_baranovski_mikhailovskiy_2020]
- [Barbosa et al 2022][research_barbosa_bertolin_2022]
- [Bartels and Stanford 2018][research_bartels_stanford_2018]
- [Bartels et al 2019][research_bartelsroberte_stanfordbretk_2019]
- [Bartoszewicz and Adamiak 2018][research_bartoszewicz_adamiak_2018]
- [Bashir et al 2021][research_bashir_longtinmartel_2021]
- [Bashir et al 2024][research_bashir_negahban_2024]
- [Bastin et al 2025][research_bastin_coron_2025]
- [Basu Roy and Bhasin 2019][research_basuroy_bhasin_2019]
- [Bataineh and Shawabkeh 2023][research_bataineh_shawabkeh_2023]
- [Batina and Yang 1985][research_batina_yang_1985]
- [Battaglia and Riccio 2026][research_battaglia_riccio_2026]
- [Batterson and Omara 1989][research_battersonjamesg_omarathomasm_1989]
- [Bauchau 1981][research_bauchau_1981]
- [Bauer et al 1995][research_bauer_clarke_1995]
- [Baumgärtner et al 2016][research_baumgartner_viti_2016]
- [Bay and Kara 2026][research_bay_kara_2026]
- [Bazhenov and Lysenkova 2015][research_bazhenov_lysenkova_2015]
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
- [Bending of cross-ply laminated plates using Lagrange multipliers 1991][research_bending_of_1991]
- [Bennett et al 1977][research_bennettrm_farmermg_1977]
- [Bennett et al 1988][research_bennettrobertm_batinajohnt_1988]
- [Bennett et al 1993][research_bennett_dansberry_1993]
- [Benyamen et al 2024][research_benyamen_chowdhury_2024]
- [Beppu et al 1966][research_beppu_curtiss_1966]
- [Berezhnitskii and Denisyuk 1985][research_berezhnitskii_denisyuk_1985]
- [Berg et al 2025][research_berg_ting_2025]
- [Bergen and Arnold 1940][research_bergen_arnold_1940]
- [Berger et al 2021][research_berger_tischler_2021]
- [Berger et al 2022][research_berger_blanken_2022]
- [Berger et al 2022][research_berger_blanken_2022_b]
- [Bergman 1948][research_bergman_1948]
- [Berman and Gran 1974][research_berman_gran_1974]
- [Bernstein 2000][research_bernstein_2000]
- [Bernstein and Hollot 1989][research_bernstein_hollot_1989]
- [Berry 1981][research_berrydt_1981]
- [Berry et al 1982][research_berry_powers_1982]
- [Besch and Liu 1973][research_besch_liu_1973]
- [Besch et al 1976][research_besch_rood_1976]
- [Bessa et al 2020][research_bessa_puig_2020]
- [Bessadi et al 2016][research_bessadi_saussie_2016]
- [Bester 2023][research_bester_2023]
- [Beyer et al 2024][research_beyer_steen_2024]
- [Beyer et al 2024][research_beyer_ullah_2024]
- [Beyers 1988][research_beyers_1988]
- [Bhachu et al 2015][research_bhachu_haftka_2015]
- [Bhardwaj and Kapania 1995][research_bhardwaj_kapania_1995]
- [Bhatia et al 2021][research_bhatia_jiang_2021]
- [Bhattacharyya et al 2019][research_bhattacharyya_conlansmith_2019]
- [Bi et al 2017][research_bi_xie_2017]
- [Bi-quan and Huan-wen 1990][research_biquan_huanwen_1990]
- [Bian et al 2018][research_bian_nener_2018]
- [Bian et al 2019][research_bian_nener_2019]
- [Bidinotto et al 2021][research_bidinotto_moura_2021]
- [Biezad and Chou 1993][research_biezaddanielj_chouhweilan_1993]
- [Bihrle and Billy 1980][research_bihrle_jr_1980]
- [Billingsley 1976][research_billingsley_1976]
- [Binder et al 2021][research_binder_wildschek_2021]
- [Binion 1971][research_binion_tw_1971]
- [Binion 1975][research_binion_tw_1975]
- [Binz and Moormann 2020][research_binz_moormann_2020]
- [Binz et al 2019][research_binz_islam_2019]
- [Birdsall 1970][research_dlbirdsall_1970]
- [Bischoff 1983][research_bischoff_1983]
- [Biskner and Higgins 2005][research_biskner_higgins_2005]
- [Bismarck-Nasr 1994][research_bismarcknasr_1994]
- [Biswas 1993][research_biswas_1993]
- [Bjarke et al 1992][research_bjarke_delfrate_1992]
- [Black and Moorhouse 1979][research_black_moorhouse_1979]
- [Blackwell and Pounds 1977][research_blackwell_pounds_1977]
- [Blair and Weisshaar 1981][research_blair_weisshaar_1981]
- [Blair and Weisshaar 1982][research_blair_weisshaar_1982]
- [Bland 1980][research_bland_1980]
- [Blight et al 1986][research_blight_gangsaas_1986]
- [Bliss 1980][research_bliss_1980]
- [Boado-Cuartero et al 2024][research_boadocuartero_perezalvarez_2024]
- [Boby et al 2019][research_boby_abdullah_2019]
- [Boden et al 2013][research_boden_jentink_2013]
- [Boden et al 2013][research_boden_lanari_2013]
- [Bodson 2000][research_bodson_2000]
- [Bogan 1981][research_bogan_1981]
- [Bohlmann 1989][research_bohlmannjonathand_1989]
- [Bohlmann and Scott 1991][research_bohlmannjonathand_scottrobertc_1991]
- [Bohlmann et al 1988][research_bohlmannjonathand_weisshaarterrencea_1988]
- [Bohlmann et al 1990][research_bohlmann_eckstrom_1990]
- [Bolding and Stearman 1976][research_boldingrm_stearmanro_1976]
- [Bolotin et al 1996][research_bolotin_grishko_1996]
- [Bombardieri et al 2021][research_bombardieri_cavallaro_2021]
- [Bondarenko and Shkolnyi 2024][research_bondarenko_shkolnyi_2024]
- [Bons and Martins 2020][research_bons_martins_2020]
- [Bons et al 2022][research_bons_martins_2022]
- [Boothe et al 1974][research_boothe_chen_1974]
- [Bordogna et al 2020][research_bordogna_lancelot_2020]
- [Bosch and Kuehl 1976][research_boschja_kuehlwj_1976]
- [Bosworth 1992][research_bosworth_1992]
- [Bosworth and Cox 1989][research_bosworth_cox_1989]
- [Bottasso and Montinari 2015][research_bottasso_montinari_2015]
- [Bouadi and Mora-Camino 2018][research_bouadi_moracamino_2018]
- [Boudreau 1977][research_boudreau_1977]
- [Bouras 2020][research_bouras_2020]
- [Bouton 1950][research_bouton_1950]
- [Bowers 1981][research_bowers_1981]
- [Bowers 1984][research_bowers_1984]
- [Bowes and Miller 1976][research_bowes_miller_1976]
- [Bowman et al 1989][research_bowmankeithb_grandhiramanav_1989]
- [Boyd 1977][research_boyd_1977]
- [Boyden 1974][research_boydenrp_1974]
- [Boyden 1978][research_boydenrp_1978]
- [Bradley 1986][research_bradley_1986]
- [Bradley et al 2026][research_bradley_haughn_2026]
- [Bras et al 2022][research_bras_warwick_2022]
- [Breitsamter and Laschka 2001][research_breitsamter_laschka_2001]
- [Briggs et al 1982][research_briggs_reed_1982]
- [Brigham et al 1973][research_brigham_barrie_1973]
- [Bright and Peterson 1960][research_brightlg_petersonvl_1960]
- [Brock and Goodman 1981][research_brockld_goodmanha_1981]
- [Brodecki and Subbarao 2015][research_brodecki_subbarao_2015]
- [Broer et al 2022][research_broer_benedictus_2022]
- [Broglio 1957][research_broglio_1957]
- [Brooks and Beamish 1977][research_brooksjd_beamishjk_1977]
- [Brooks and Martins 2018][research_brooks_martins_2018]
- [Brooks et al 2019][research_brooks_martins_2019]
- [Broussard and Halyo 1983][research_broussardjr_halyon_1983]
- [Broussard and Stengel 1977][research_broussard_stengel_1977]
- [Brouwer and McNamara 2020][research_brouwer_mcnamara_2020]
- [Brown and Szalai 1977][research_brownsr_szalaikj_1977]
- [Bruno and Libeskind 1990][research_brunojoseph_libeskindmark_1990]
- [Bryson and Rumpfkeil 2019][research_bryson_rumpfkeil_2019]
- [Bryson et al 1969][research_bryson_desai_1969]
- [Brüderlin et al 2018][research_bruderlin_hosters_2018]
- [Bu et al 2025][research_bu_luo_2025]
- [Budd 1984][research_budd_1984]
- [Budd 1987][research_budd_1987]
- [Bueno and Dowell 2020][research_bueno_dowell_2020]
- [Buffington 1997][research_buffington_1997]
- [Buffington 1999][research_buffington_1999]
- [Buffington 1999][research_buffington_1999_b]
- [Buffington and Adams 1995][research_buffington_adams_1995]
- [Bugała 2025][research_bugala_2025]
- [Bugała and Payenskyy 2025][research_bugala_payenskyy_2025]
- [Bullock and Fields 1998][research_bullock_fields_1998]
- [Burdette and Martins 2018][research_burdette_martins_2018]
- [Burken 2007][research_burkenjohnj_2007]
- [Burkett 1989][research_burkett_1989]
- [Burkhalter 1993][research_burkhalter_1993]
- [Burner and Martinson 1996][research_burner_martinson_1996]
- [Burnett et al 2016][research_burnett_beranek_2016]
- [Burns 1975][research_burns_1975]
- [Burt 1975][research_burt_1975]
- [Busan 1998][research_busan_1998]
- [Butler 1976][research_butler_1976]
- [Butler 1982][research_butler_1982]
- [Butler 1983][research_butler_1983]
- [Buzica et al 2018][research_buzica_biswanger_2018]
- [Byreddy et al 2003][research_byreddy_grandhi_2003]
- [Büchter et al 2021][research_buchter_sebastiasaez_2021]
- [Cagdas 2017][research_cagdas_2017]
- [Cahn and Garcia 1971][research_cahn_garcia_1971]
- [Cai et al 2026][research_cai_fan_2026]
- [Caixeta and Marques 2018][research_caixeta_marques_2018]
- [Calarese 1984][research_calarese_1984]
- [Calico and Fuller 1981][research_calico_fuller_1981]
- [Calise 1977][research_calise_1977]
- [Callaghan and Kunz 2021][research_callaghan_kunz_2021]
- [Camacho et al 2021][research_camacho_akhavan_2021]
- [Campagna et al 2025][research_campagna_benedetti_2025]
- [Campagna et al 2025][research_campagna_gulizzi_2025]
- [Campbell and Smith 1989][research_campbellrichardl_smithleigha_1989]
- [Campbell and Terrell 1987][research_campbell_terrell_1987]
- [Campos and Marques 2021][research_campos_marques_2021]
- [Candon et al 2026][research_candon_marzocca_2026]
- [Cannella et al 2018][research_cannella_garinei_2018]
- [Cano and Sobel 2016][research_cano_sobel_2016]
- [Cao and Liu 2025][research_cao_liu_2025_b]
- [Cao and Lu 2024][research_cao_lu_2024]
- [Cao et al 2017][research_cao_tang_2017]
- [Cao et al 2020][research_cao_jia_2020]
- [Cao et al 2026][research_cao_chen_2026]
- [Capone 1981][research_caponefj_1981]
- [Carico 1998][research_carico_1998]
- [Carlson 1976][research_carlson_1976]
- [Carlson et al 2017][research_carlson_verberg_2017]
- [Carneiro and Gamboa 2019][research_carneiro_gamboa_2019]
- [Carrera et al 2013][research_carrera_varello_2013]
- [Casey 1988][research_casey_1988]
- [Castañeda and Gordillo 2019][research_castaneda_gordillo_2019]
- [Castellani et al 2017][research_castellani_cooper_2017]
- [Cavalcanti et al 2026][research_cavalcanti_uehara_2026]
- [Cavaliere and Fezans 2024][research_cavaliere_fezans_2024]
- [Cavaliere et al 2024][research_cavaliere_fezans_2024_b]
- [Cavallaro et al 2015][research_cavallaro_bombardieri_2015]
- [Cebeci 1974][research_cebeci_1974]
- [Cen et al 2020][research_cen_li_2020]
- [Center 1975][research_center_1975]
- [Cesnik 2002][research_cesnik_2002]
- [Cesnik 2005][research_cesnik_2005]
- [Cestino and Iannuzzo 2026][research_cestino_iannuzzo_2026]
- [Chabir et al 2017][research_chabir_bouteraa_2017]
- [Chabod and Baron 2020][research_chabod_baron_2020]
- [Chacon and McBride 1988][research_chacon_mcbride_1988]
- [Chacon and McBride 1990][research_chacon_mcbride_1990]
- [Chai et al 2017][research_chai_song_2017]
- [Chajjed et al 2024][research_chajjed_khalil_2024]
- [Chakravarthy et al 2015][research_chakravarthy_evans_2015]
- [Chakravarty and Mahanta 2015][research_chakravarty_mahanta_2015]
- [Chalk 1964][research_chalk_1964]
- [Chalk et al 1969][research_chalk_neal_1969]
- [Chance Vought Corp Dallas Tx 1979][research_chancevoughtcorpdallastx_1979]
- [Chang et al 2022][research_chang_debreuker_2022]
- [Chang et al 2022][research_chang_guo_2022]
- [Changchuan et al 2018][research_changchuan_lan_2018]
- [Changchuan et al 2022][research_changchuan_zhiying_2022]
- [Chaparro et al 2016][research_chaparrodaniel_fujiwaragustavoec_2016]
- [Chatterjee et al 2019][research_chatterjee_chowdhury_2019]
- [Chattopadhyay and Jha 1996][research_chattopadhyayaditi_jharatneshwar_1996]
- [Chattopadhyay and Zhang 1995][research_chattopadhyayaditi_zhangsen_1995]
- [Chau and Zingg 2022][research_chau_zingg_2022]
- [Chau and Zingg 2023][research_chau_zingg_2023]
- [Chau et al 2026][research_chau_piotrowski_2026]
- [Chauhan and Martins 2021][research_chauhan_martins_2021]
- [Chauhan and Martins 2024][research_chauhan_martins_2024]
- [Chauhan et al 2023][research_chauhan_praveen_2023]
- [Chen 1982][research_chen_1982]
- [Chen and Dugundji 1987][research_chen_dugundji_1987]
- [Chen and Han 2017][research_chen_han_2017]
- [Chen and Holohan 2015][research_chen_holohan_2015]
- [Chen and Li 2017][research_chen_li_2017]
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
- [Chen et al 2019][research_chen_chen_2019]
- [Chen et al 2019][research_chen_wang_2019]
- [Chen et al 2020][research_chen_edwards_2020]
- [Chen et al 2020][research_chen_gao_2020]
- [Chen et al 2020][research_chen_he_2020]
- [Chen et al 2020][research_chen_jing_2020]
- [Chen et al 2022][research_chen_edwards_2022]
- [Chen et al 2022][research_chen_gao_2022]
- [Chen et al 2022][research_chen_han_2022]
- [Chen et al 2023][research_chen_gao_2023]
- [Chen et al 2023][research_chen_gao_2023_b]
- [Chen et al 2023][research_chen_rao_2023]
- [Chen et al 2023][research_chen_shi_2023]
- [Chen et al 2023][research_chen_shi_2023_b]
- [Chen et al 2024][research_chen_li_2024]
- [Chen et al 2025][research_chen_he_2025]
- [Chen et al 2025][research_chen_meng_2025]
- [Chen et al 2025][research_chen_zhai_2025]
- [Chen et al 2026][research_chen_cai_2026]
- [Chen et al 2026][research_chen_wang_2026]
- [Cheng et al 1980][research_chenghk_mengsy_1980]
- [Cheng et al 2015][research_cheng_zhou_2015]
- [Cheng et al 2017][research_cheng_wei_2017]
- [Cheng et al 2019][research_cheng_liang_2019]
- [Cheng et al 2023][research_cheng_li_2023]
- [Chetty and Lakshmi 1991][research_chetty_lakshmi_1991]
- [Chiarelli and Bonomo 2019][research_chiarelli_bonomo_2019]
- [Chin 1989][research_chin_1989]
- [Chin et al 1982][research_chin_berman_1982]
- [Chin et al 1987][research_chinj_chaconv_1987]
- [Chin et al 1994][research_chin_lee_1994]
- [Chinvorarat 2021][research_chinvorarat_2021]
- [Chipman et al 1982][research_chipman_zislin_1982]
- [Chipman et al 1983][research_chipman_zislin_1983]
- [Chipman et al 1984][research_chipmanr_rauchf_1984]
- [Chipman et al 1985][research_chipmanr_rauchf_1985]
- [Choi 2016][research_choi_2016]
- [Choi and Choi 2026][research_choi_choi_2026]
- [Choi and Park 2019][research_choi_park_2019]
- [Choi et al 2017][research_choi_shrestha_2017]
- [Choi et al 2020][research_choi_lim_2020]
- [Choi et al 2023][research_choi_kim_2023]
- [Choosak Ngaongam and Rapee Ujjin 2024][research_choosakngaongam_rapeeujjin_2024]
- [Chougule and Sonawane 2017][research_chougule_sonawane_2017]
- [Chowdary et al 1994][research_chowdary_parthan_1994]
- [Chowhan et al 2019][research_chowhan_arya_2019]
- [Christoforou 1993][research_christoforou_1993]
- [Chu and Lawing 1990][research_chujulio_lawingpiercel_1990]
- [Cid Montoya et al 2018][research_cidmontoya_hernandez_2018]
- [Clark 2001][research_clark_2001]
- [Clark and LeTron 1989][research_clark_letron_1989]
- [Clark and Spurlin 1962][research_clark_spurlin_1962]
- [Clarke et al 1982][research_clarker_shaned_1982]
- [Clarke et al 1994][research_clarkerobert_burkenjohnj_1994]
- [Clay and Rockafellow 1973][research_clay_rockafellow_1973]
- [Clements 2016][research_clementskeith_2016]
- [Clements and Djidjeli 2023][research_clements_djidjeli_2023]
- [Clews 1973][research_clews_1973]
- [Clyde et al 1984][research_clyde_bonner_1984]
- [Coban 2020][research_coban_2020]
- [Cobo-González et al 2026][research_cobogonzalez_rodriguezrobles_2026]
- [Cochran 2015][research_cochran_2015]
- [Coder 2021][research_coder_2021]
- [Coder 2026][research_coder_2026]
- [Coe and Kulla 1974][research_coe_kulla_1974]
- [Coe et al 1990][research_coepaulljr_perkinsjohnn_1990]
- [Cohen 1978][research_cohenga_1978]
- [Cohen 1982][research_cohen_1982]
- [Cohen and Le 1991][research_cohendorothea_lejeanetteh_1991]
- [Coldsnow et al 2009][research_coldsnow_uybarreta_2009]
- [Cole 1986][research_colesr_1986]
- [Cole 1988][research_cole_1988]
- [Cole 1988][research_cole_1988_b]
- [Cole et al 1980][research_cole_cook_1980]
- [Collins 1988][research_collins_1988]
- [Combined flight control/utility system 1974][research_combined_flight_1974]
- [Comer and Chakraborty 2024][research_comer_chakraborty_2024]
- [Composite Materials in Aircraft Structures 1989][research_composite_materials_1989]
- [Concorde Automatic Flight Control System 1971][research_concorde_automatic_1971]
- [Cong et al 2023][research_cong_hu_2023]
- [Conlan-Smith and Andreasen 2022][research_conlansmith_andreasen_2022]
- [Connelly 1982][research_connelly_1982]
- [Contell Asins et al 2021][research_contellasins_landersheim_2021]
- [Cook 1979][research_cook_1979]
- [Cooper and Stroud 1972][research_cooperpa_stroudwj_1972]
- [Coppin et al 2018][research_coppin_birch_2018]
- [Cordeiro et al 2024][research_cordeiro_azinheira_2024]
- [Corliss and Talbot 1977][research_corlissld_talbotpd_1977]
- [Cornelius and Lucius 1994][research_cornelius_lucius_1994]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornellaeronauticallabincbuffalony_1947]
- [Cotton 1974][research_cotton_1974]
- [Cotton and Bjarke 1994][research_cotton_bjarke_1994]
- [Crabtree 1979][research_crabtree_1979]
- [Craig 1965][research_craig_1965]
- [Craig and Erbug 1976][research_craig_erbug_1976]
- [Crandall et al 1973][research_crandall_maund_1973]
- [Crane 1983][research_cranedf_1983]
- [Crane 1984][research_cranedf_1984]
- [Crane and Sommer 1961][research_craneharoldl_sommerrobertw_1961]
- [Craver and Egle 1972][research_craver_egle_1972]
- [Crawley and Lee 1978][research_crawley_lee_1978]
- [Crews and Naik 1986][research_crews_naik_1986]
- [Crimi and Grace 1965][research_crimi_grace_1965]
- [Crimi and Ordway 1962][research_crimi_ordway_1962]
- [Crisfield 1978][research_crisfield_1978]
- [Crittenden et al 1978][research_crittenden_weishaar_1978]
- [Croom et al 1988][research_croommarka_whippleraymondd_1988]
- [Croop 1985][research_croop_1985]
- [Crother et al 1973][research_crother_gabelman_1973]
- [Crouse and Leishman 1992][research_crouse_leishman_1992]
- [Crowe 1937][research_crowe_1937]
- [Cui et al 2016][research_cui_yang_2016]
- [Cui et al 2021][research_cui_azuara_2021]
- [Cui et al 2022][research_cui_li_2022]
- [Cui et al 2025][research_cui_he_2025]
- [Cui et al 2026][research_cui_miao_2026]
- [Cully and Boller 1973][research_cully_boller_1973]
- [Cunis et al 2019][research_cunis_burlion_2019]
- [Cunis et al 2020][research_cunis_condomines_2020]
- [Cunis et al 2020][research_cunis_condomines_2020_b]
- [Cunningham et al 1987][research_cunninghamherbertj_batinajohnt_1987]
- [Cunningham et al 1988][research_cunningham_batina_1988]
- [Currao and Jiang 2026][research_currao_jiang_2026]
- [Curry et al 1965][research_curry_matthews_1965]
- [Curry et al 1989][research_curry_moulton_1989]
- [Curry et al 1990][research_curry_moulton_1990]
- [Curtiss 1971][research_curtiss_1971]
- [Curtiss and Howard C. 1961][research_curtiss_howardc_1961]
- [Cuschieri 1990][research_cuschieri_1990]
- [Cutchins and Purvis 1982][research_cutchinsma_purvisjw_1982]
- [Czyba and Stajer 2019][research_czyba_stajer_2019]
- [Czysz 1963][research_czysz_1963]
- [D'Andrea 2003][research_dandrea_2003]
- [D'Andrea 2008][research_dandrea_2008]
- [Da Ronch et al 2019][research_daronch_drofelnik_2019]
- [Dababneh et al 2018][research_dababneh_kipouros_2018]
- [Dagal 2026][research_dagal_2026]
- [Daghighi et al 2020][research_daghighi_rouhi_2020]
- [Dagilis and Kilikevičius 2023][research_dagilis_kilikevicius_2023]
- [Dagkolu et al 2021][research_dagkolu_gokdag_2021]
- [Dai and Yang 2015][research_dai_yang_2015]
- [Dai et al 2025][research_dai_hu_2025]
- [Daken and Mar 1985][research_daken_mar_1985]
- [Damodaran and Caughey 1988][research_damodaran_caughey_1988]
- [Dandois 2016][research_dandois_2016]
- [Daniel 1976][research_daniel_1976]
- [Daniel de Almeida Pereira and Flávio Donizeti Marques 2015][research_danieldealmeidapereira_flaviodonizetimarques_2015]
- [Darabi and Ganesan 2016][research_darabi_ganesan_2016]
- [Darabi and Ganesan 2017][research_darabi_ganesan_2017]
- [Darabseh et al 2022][research_darabseh_tarabulsi_2022]
- [Das and Kapuria 2016][research_das_kapuria_2016]
- [Das and Longo 1995][research_das_longo_1995]
- [Data-driven Model-Free Adaptive Control Tuned by Virtual Reference 2016][research_data_driven_model_free_2016]
- [Daudeville and Ladevèze 1993][research_daudeville_ladeveze_1993]
- [Davanipour et al 2017][research_davanipour_khayatian_2017]
- [Davis 1973][research_davis_1973]
- [Davis et al 1977][research_davis_garnett_1977]
- [Davis et al 1993][research_davisddjr_farleygaryl_1993]
- [Dawe and Roufaeil 1980][research_dawe_roufaeil_1980]
- [Dawe et al 2025][research_dawe_bull_2025]
- [Dawson and Fortin 1987][research_dawson_fortin_1987]
- [Daynes 2024][research_daynes_2024]
- [De et al 2019][research_de_jrad_2019]
- [De Gaspari and Mantegazza 2024][research_degaspari_mantegazza_2024]
- [De Gaspari et al 2018][research_degaspari_riccobene_2018]
- [de Medeiros et al 2017][research_demedeiros_vandepitte_2017]
- [de Silva and Carmichael 1978][research_desilva_carmichael_1978]
- [de Souza and de Leon 2023][research_desouza_deleon_2023]
- [de Souza et al 2023][research_desouza_vuillemin_2023]
- [De Wagter and Meulenbeld 2019][research_dewagter_meulenbeld_2019]
- [Deandrea et al 1991][research_deandrea_roache_1991]
- [Deangelis 1981][research_deangelis_1981]
- [DeAngelis 1982][research_deangelis_1982]
- [Deepa and Gupta 2023][research_deepa_gupta_2023]
- [Deets 1975][research_deetsda_1975]
- [Deformational behaviour of a unidirectional graphite/epoxy composite under compressive fatigue 1990][research_deformational_behaviour_1990]
- [Dehghan Manshadi and Saghafi 2021][research_dehghanmanshadi_saghafi_2021]
- [del Carre and Palacios 2020][research_delcarre_palacios_2020]
- [Del Frate 1992][research_delfrate_1992]
- [Delfrate and Saltzman 1992][research_delfrate_saltzman_1992]
- [Demarchi and Haning 1978][research_demarchi_haning_1978]
- [Demir and Seyfullah Babaarslan 2021][research_demir_seyfullahbabaarslan_2021]
- [Demir et al 2023][research_demir_gorguluarslan_2023]
- [Deng and Qin 2021][research_deng_qin_2021]
- [Deng and Yi 2023][research_deng_yi_2023]
- [Deng et al 2023][research_deng_zhang_2023]
- [Deng et al 2024][research_deng_stoica_2024]
- [Deng et al 2024][research_deng_zeng_2024]
- [Deng et al 2026][research_deng_xu_2026]
- [Deng et al 2026][research_deng_yi_2026]
- [Deobald and Gibson 1988][research_deobald_gibson_1988]
- [Derkach et al 2022][research_derkach_zinkovskii_2022]
- [Description and Flight Test 1975][research_description_and_1975]
- [Design and CFD Analysis of Supercritical Airfoil 0714 Under Ground-Level Atmospheric Conditions 2024][research_design_and_2024]
- [Design of an Aircraft Wing Structure for Static&amp; Fatigue Life Prediction 2019][research_design_of_2019]
- [Design of discrete-time adaptive control in presence of uncertain time delay 1995][research_design_of_1995]
- [Design Optimization for SG6043 Airfoil for Using Finite Elements Analysis 2025][research_design_optimization_2025]
- [Desilva and Medan 1978][research_desilvabme_medanrt_1978]
- [Deskos et al 2020][research_deskos_delcarre_2020]
- [Devi 2019][research_devi_2019]
- [Dexl et al 2020][research_dexl_hauffe_2020]
- [Dexter 1993][research_dexter_1993]
- [Dhadekar et al 2021][research_dhadekar_misra_2021]
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
- [Diederich and Budiansky 1948][research_diederichfranklinw_budianskybernard_1948]
- [Difranco 1970][research_difranco_1970]
- [Digital model-reference flight control of aircraft with unstable sampling zeros 1994][research_digital_model_reference_1994]
- [Dillinger et al 2019][research_dillinger_abdalla_2019]
- [Dillinger et al 2020][research_dillinger_meddaikar_2020]
- [Dilmi 2022][research_dilmi_2022]
- [Ding and Zhou 2018][research_ding_zhou_2018]
- [Ding et al 2022][research_ding_xu_2022]
- [Ding et al 2025][research_ding_shi_2025]
- [Dinler 2025][research_dinler_2025]
- [Divakar and B L 2026][research_divakar_bl_2026]
- [Dlamini and Jones 2016][research_dlamini_jones_2016]
- [Dobos-Bubno and Hartsook 1977][research_dobosbubno_hartsook_1977]
- [Dodayav et al 2024][research_dodayav_biswas_2024]
- [Doggett and Ricketts 1980][research_doggett_ricketts_1980]
- [Doggett et al 1995][research_doggettrobertvjr_riverajoseajr_1995]
- [Doi and Kataoka 1982][research_doi_kataoka_1982]
- [Dong et al 2016][research_dong_lu_2016]
- [Dong et al 2019][research_dong_shi_2019]
- [Dong et al 2023][research_dong_li_2023]
- [Dong et al 2025][research_dong_zhou_2025]
- [Dooley 1965][research_dooley_1965]
- [Dorey et al 1980][research_dorey_good_1980]
- [Dowell and Bliss 1978][research_dowell_bliss_1978]
- [Dowell and Hall 2003][research_dowell_hall_2003]
- [Droney et al 2020][research_christopherkdroney_anthonyjsclafani_2020]
- [Drtil and Schulz 1978][research_drtil_schulz_1978]
- [Duan and Okwudire 2019][research_duan_okwudire_2019]
- [Duan and Zhang 2018][research_duan_zhang_2018]
- [Dubary et al 2018][research_dubary_bouvet_2018]
- [Dubigeon 1992][research_dubigeon_1992]
- [Dugundji 1965][research_dugundji_1965]
- [Dugundji et al 1962][research_dugundji_dowell_1962]
- [Dukes 1970][research_dukes_1970]
- [Dul 2018][research_dul_2018]
- [Dunmire 1982][research_dunmire_1982]
- [Dunn et al 1986][research_dunnwr_cottrelld_1986]
- [Dunning et al 2014][research_dunningpeterd_stanfordbretk_2014]
- [Durand and Teper 1964][research_durand_teper_1964]
- [Durlofsky and Mayers 1970][research_durlofsky_mayers_1970]
- [Durston and Schreiner 1983][research_durstonda_schreinerja_1983]
- [Dussart et al 2019][research_dussart_lone_2019]
- [Dutta and Zhao 2025][research_dutta_zhao_2025]
- [Dwivedi et al 2022][research_dwivedi_anitha_2022]
- [Dzhurynskyi 2026][research_dzhurynskyi_2026]
- [Dávila and Bisagni 2017][research_davila_bisagni_2017]
- [D’Amico et al 2025][research_damico_labella_2025]
- [d’Apolito and Sulzbachner 2021][research_dapolito_sulzbachner_2021]
- [Earls and Sitz 1989][research_earls_sitz_1989]
- [Eastep and Olsen 1980][research_eastep_olsen_1980]
- [Eastep et al 1984][research_eastep_venkayya_1984]
- [Ebner and Mark 1977][research_ebnerre_markjg_1977]
- [Ebrahimzade et al 2016][research_ebrahimzade_dardel_2016]
- [Ecer 1985][research_ecer_1985]
- [Eckhaus 1962][research_eckhaus_1962]
- [Eckstrom and Spain 1982][research_eckstromcv_spaincv_1982]
- [Edwards 1963][research_edwards_1963]
- [Edwards 1983][research_edwards_1983]
- [Edwards 1992][research_edwards_1992]
- [Edwards and Wieseman 2003][research_edwards_wieseman_2003]
- [Edwards and Wieseman 2008][research_edwards_wieseman_2008]
- [Effective Torsional Stiffness of Equivalent Beams 1976][research_effective_torsional_1976]
- [Effects of a controlled modulus interlayer upon the properties of graphite/epoxy composite 1988][research_effects_of_1988]
- [Efremov et al 2020][research_efremov_efremov_2020]
- [Efremov et al 2022][research_efremov_shcherbakov_2022]
- [Ehlers and Weisshaar 1993][research_ehlers_weisshaar_1993]
- [Eichler 1970][research_eichler_1970]
- [Ekaterinaris and Schiff 1990][research_ekaterinarisja_schifflewisb_1990]
- [Ekaterinaris and Schiff 1994][research_ekaterinarisja_schifflewisb_1994]
- [El-Mahdy et al 2025][research_elmahdy_ali_2025]
- [El-Salamony and Aziz 2020][research_elsalamony_aziz_2020]
- [Elenchezhiyan and Kumar 2025][research_elenchezhiyan_kumar_2025]
- [Elham 2015][research_elham_2015]
- [Elham and van Tooren 2016][research_elham_vantooren_2016]
- [Elham and van Tooren 2016][research_elham_vantooren_2016_b]
- [Elliott 1976][research_jarrellrelliott_1976]
- [Elliott 1977][research_jelliott_1977]
- [Elshazly et al 2025][research_elshazly_kassem_2025]
- [Elyasi et al 2020][research_elyasi_roudbari_2020]
- [Enciu 2019][research_enciu_2019]
- [Eney 1968][research_eney_1968]
- [Engelland et al 1992][research_engellandsa_franklinja_1992]
- [Enns 2003][research_enns_2003]
- [Enns et al 1992][research_enns_ozbay_1992]
- [Er-El 1988][research_erel_1988]
- [Er-El and Seginer 1985][research_erel_seginer_1985]
- [Eraslan and Oktay 2023][research_eraslan_oktay_2023]
- [Erickson 2003][research_ericksongarye_2003]
- [Eriksson 1990][research_eriksson_1990]
- [Esfahani et al 2018][research_esfahani_webb_2018]
- [Eugene 1996][research_eugeneltu_1996]
- [Evald et al 2023][research_evald_hollweg_2023]
- [Ewing et al 1988][research_ewing_hinger_1988]
- [Experimental investigation of synthetic jet control of wing rock for a flying wing aircraft 2023][research_experimental_investigation_2023]
- [Fadel et al 2019][research_fadel_rabie_2019]
- [Fan 2026][research_fan_2026]
- [Fan et al 2021][research_fan_yu_2021]
- [Fan et al 2023][research_fan_wang_2023]
- [Fan et al 2025][research_fan_wang_2025]
- [Fan et al 2026][research_fan_jiang_2026]
- [Fang et al 2020][research_fang_cao_2020]
- [Fanucci 1987][research_fanucci_1987]
- [Farbridge et al 1956][research_farbridge_woodward_1956]
- [Fardad and Bamieh 2006][research_fardad_bamieh_2006]
- [Farhat 1998][research_farhat_1998]
- [Farhat 2000][research_farhat_2000]
- [Farhat 2001][research_farhat_2001]
- [Farhat and Amsallem 2011][research_farhat_amsallem_2011]
- [Farkh et al 2021][research_farkh_ksouri_2021]
- [Farmer and Hanson 1976][research_farmermg_hansonpw_1976]
- [Farsadi et al 2020][research_farsadi_rahmanian_2020]
- [Farsadi et al 2024][research_farsadi_ahmadi_2024]
- [Farsadi et al 2026][research_farsadi_ahmadi_2026]
- [Fatigue behaviour of composite laminate 1977][research_fatigue_behaviour_1977]
- [Faure et al 2019][research_faure_dumas_2019]
- [Favaro et al 2025][research_favaro_rylko_2025]
- [Favier et al 1987][research_favier_maresca_1987]
- [Fazeli et al 2022][research_fazeli_stokesgriffin_2022]
- [Fazilati and Khalafi 2019][research_fazilati_khalafi_2019]
- [Fazilati and Khalafi 2019][research_fazilati_khalafi_2019_b]
- [Fearnside 1962][research_fearnside_1962]
- [Fedorenko and Bondarenko 2024][research_fedorenko_bondarenko_2024]
- [Fehrs and Kaiser 2025][research_fehrs_kaiser_2025]
- [Feil et al 2020][research_feil_pflumm_2020]
- [Feldt and Herrmann 1974][research_feldt_herrmann_1974]
- [Feliu‐Batlle 2016][research_feliubatlle_2016]
- [Feng 2023][research_feng_2023]
- [Feng et al 2021][research_feng_wang_2021]
- [Feng et al 2023][research_feng_guo_2023]
- [Feng et al 2024][research_feng_liu_2024]
- [Feroskhan and Go 2016][research_feroskhan_go_2016]
- [Feroskhan and Go 2018][research_feroskhan_go_2018]
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
- [Finkleman 1972][research_finkleman_1972]
- [Fisher et al 1992][research_fisher_richwine_1992]
- [Flax 1943][research_flax_1943]
- [Fleming and Kushner 1994][research_fleming_kushner_1994]
- [Flight performance handbook for powered flight operations 1963][research_flight_performance_1963]
- [Flight Sciences Lab Inc Buffalo Ny 1964][research_flightscienceslabincbuffalony_1964]
- [Flight Test Data Analysis of Hybrid Vertical Take-off and Landing Unmanned Aerial Vehicle 2016][research_flight_test_2016]
- [Florance et al 2004][research_florancejamesr_heegjennifer_2004]
- [Flores et al 2025][research_flores_bazan_2025]
- [Fontana et al 2024][research_fontana_piperni_2024]
- [Fonte et al 2015][research_fonte_ricci_2015]
- [Ford 1989][research_ford_1989]
- [Fortiş et al 2015][research_fortis_fortis_2015]
- [Fournier et al 2022][research_fournier_massioni_2022]
- [Fraihat and Ajaj 2024][research_fraihat_ajaj_2024]
- [Franco et al 2022][research_franco_rios_2022]
- [Francois et al 2017][research_francois_cooper_2017]
- [Franklin 1993][research_franklinjamesa_1993]
- [Franklin 1993][research_jamesafranklin_1993]
- [Franklin and Innis 1972][research_franklinja_innisrc_1972]
- [Franklin and Innis 1978][research_franklin_innis_1978]
- [Franklin et al 1990][research_franklinjamesa_stortzmichaelw_1990]
- [Fratello et al 1987][research_fratello_croom_1987]
- [Frei 1982][research_frei_1982]
- [Fresconi et al 2014][research_fresconi_celmins_2014]
- [Freudinger 1989][research_freudingerlawrencec_1989]
- [Freudinger and Kehoe 1990][research_freudingerlawrencec_kehoemichaelw_1990]
- [Friedmann 1998][research_friedmann_1998]
- [Friend and Sakamoto 1978][research_friendel_sakamotogm_1978]
- [Frost and Rutherford 1963][research_frost_rutherford_1963]
- [Fu et al 2021][research_fu_yang_2021]
- [Fujii 1985][research_fujii_1985]
- [Fukunaga 1990][research_fukunaga_1990]
- [Fukunaga and Sekine 1994][research_fukunaga_sekine_1994]
- [Fukunaga et al 1993][research_fukunaga_sekine_1993]
- [Fung 1982][research_fung_1982]
- [Fung and Doong 1988][research_fung_doong_1988]
- [Furtado et al 2019][research_furtado_catalanotti_2019]
- [Furtat and Gushchin 2021][research_furtat_gushchin_2021]
- [Fuzzy logic for control of roll and moment for a flexible wing aircraft 1991][research_fuzzy_logic_1991]
- [G.S.S.S.S.V. 2020][research_gssssv_2020]
- [Gabrys et al 2019][research_gabrys_steffensen_2019]
- [Gainer 1963][research_gainer_1963]
- [Galasso et al 2024][research_galasso_ciminello_2024]
- [Galffy et al 2019][research_galffy_bock_2019]
- [Galiana et al 2024][research_galiana_moradi_2024]
- [Gallagher 1971][research_gallagher_1971]
- [Gamagedara et al 2024][research_gamagedara_lee_2024]
- [Gao and Cai 2016][research_gao_cai_2016]
- [Gao et al 2017][research_gao_wu_2017]
- [Gao et al 2019][research_gao_gao_2019]
- [Gao et al 2021][research_gao_ma_2021]
- [Gao et al 2024][research_gao_liu_2024]
- [Gao et al 2025][research_gao_jiang_2025]
- [Garabedian 1979][research_garabedianpr_1979]
- [Garcia-Hernandez et al 2017][research_garciahernandez_cuernorejado_2017]
- [Garg and Schmidt 1988][research_gargsanjay_schmidtdavidk_1988]
- [Garmendia and Mavris 2016][research_garmendia_mavris_2016]
- [Garner et al 2023][research_garner_wu_2023]
- [Garrard and Low 1990][research_garrard_low_1990]
- [Garrick and Rubinow 1946][research_garrickie_rubinowsi_1946]
- [Garrick and Rubinow 1946][research_garrickie_rubinowsi_1946_b]
- [Gaurav et al 2023][research_gaurav_sekou_2023]
- [Gavra and van Kampen 2024][research_gavra_vankampen_2024]
- [Geisler and Junker 2024][research_geisler_junker_2024]
- [Gelos and Laura 1990][research_gelos_laura_1990]
- [Geng et al 2026][research_geng_zhao_2026]
- [Geoghegan et al 2020][research_geoghegan_giannelis_2020]
- [Gera 1986][research_gera_1986]
- [Gera et al 1987][research_gera_andrisani_1987]
- [Gera et al 1989][research_gera_andrisani_1989]
- [Gerdes and Hynes 1972][research_gerdes_hynes_1972]
- [Gerken 1979][research_gerken_1979]
- [Ghalandari et al 2022][research_ghalandari_mahariq_2022]
- [Ghasemikaram et al 2021][research_ghasemikaram_mazidi_2021]
- [Ghazi et al 2022][research_ghazi_alhazmi_2022]
- [Giannakeas et al 2022][research_giannakeas_sharifkhodaei_2022]
- [Gibson 1999][research_gibson_1999]
- [Giese et al 1996][research_giese_reich_1996]
- [Gilbert 1987][research_gilbertmichaelg_1987]
- [Gilbert and Schneider 1981][research_gilbert_schneider_1981]
- [Gilbert et al 1982][research_gilbert_schmidt_1982]
- [Gilbert et al 1984][research_gilbert_schmidt_1984]
- [Giles 1972][research_giles_1972]
- [Gill 1995][research_gill_1995]
- [GlBBINGS 1969][research_glbbings_1969]
- [Glezer and Leonard 2012][research_glezer_leonard_2012]
- [Gloss and Washburn 1977][research_glossbb_washburnke_1977]
- [Gloss and Washburn 1978][research_gloss_washburn_1978]
- [Godwin et al 1964][research_godwin_frazier_1964]
- [Goel and Roy 2021][research_goel_roy_2021]
- [Goizueta et al 2022][research_goizueta_wynn_2022]
- [Goizueta et al 2022][research_goizueta_wynn_2022_b]
- [Goland 1945][research_goland_1945]
- [Golmirzaee and Wood 2026][research_golmirzaee_wood_2026]
- [Golombek et al 2026][research_golombek_bustamante_2026]
- [Gong et al 2019][research_gong_wang_2019]
- [Gong et al 2019][research_gong_wang_2019_b]
- [Gong et al 2024][research_gong_xu_2024]
- [Gong et al 2026][research_gong_he_2026]
- [González et al 2020][research_gonzalez_silvestre_2020]
- [González-Montijo et al 2026][research_gonzalezmontijo_vanness_2026]
- [Goodrich et al 1989][research_goodrichkennethh_sliwastevenm_1989]
- [Goradia et al 1989][research_goradiash_bobbittpj_1989]
- [Gorman and Singhal 1993][research_gorman_singhal_1993]
- [Govindaraj et al 1979][research_govindaraj_rynaski_1979]
- [Govoni and Cristofaro 2023][research_govoni_cristofaro_2023]
- [Grafton et al 1982][research_graftonsb_gilberwp_1982]
- [Grant et al 2015][research_grant_stol_2015]
- [Grantham et al 1976][research_granthamwd_nguyenlt_1976]
- [Grauer 2018][research_jaredagrauer_2018]
- [Grauer and Boucher 2017][research_grauerjareda_bouchermatthewj_2017]
- [Graves and Sawicki 1994][research_graves_sawicki_1994]
- [Gray and Mei 1993][research_gray_mei_1993]
- [Gray et al 2023][research_gray_riso_2023]
- [Gray et al 2025][research_gray_kennedy_2025]
- [Green 1986][research_greenja_1986]
- [Green 1987][research_green_1987]
- [Greenberg and Sternfield 1944][research_greenbergharry_sternfieldleonard_1944]
- [Greene 1928][research_greene_1928]
- [Greenhalgh et al 1993][research_greenhalgh_pastore_1993]
- [Grenestedt 1989][research_grenestedt_1989]
- [Greszczuk and Chao 1975][research_greszczuk_chao_1975]
- [Griffin and Eastep 1981][research_griffin_eastep_1981]
- [Griffin and Eastep 1982][research_griffin_eastep_1982]
- [Griffin and Harvill 1988][research_griffincharlesf_harvillwilliame_1988]
- [Griffin et al 1983][research_griffin_haerter_1983]
- [Griffin et al 2010][research_griffinbrianjoseph_burkenjohnj_2010]
- [Griffis et al 1981][research_griffis_masumura_1981]
- [Grifò et al 2023][research_grifo_gulizzi_2023]
- [Grigolyuk and Kulikov 1990][research_grigolyuk_kulikov_1990]
- [Groh and Wu 2022][research_groh_wu_2022]
- [Gross et al 2017][research_gross_clark_2017]
- [Gruenwald et al 2020][research_gruenwald_yucelen_2020]
- [Gu and Hong 2020][research_gu_hong_2020]
- [Gu and Zhou 2020][research_gu_zhou_2020]
- [Gu and Zhou 2022][research_gu_zhou_2022]
- [Gu et al 2022][research_gu_taghipour_2022]
- [Gu et al 2023][research_gu_ducvo_2023]
- [Guderley 1956][research_guderley_1956]
- [Guimarães et al 2019][research_guimaraes_castro_2019]
- [Guimarães et al 2020][research_guimaraes_silva_2020]
- [Guinn 1984][research_guinnwileya_1984]
- [Guinn et al 1983][research_guinnwileya_willeycraigs_1983]
- [Guinn et al 1984][research_guinnwileya_risingjerryj_1984]
- [Gunnink 1988][research_gunnink_1988]
- [Guo 2021][research_guo_2021]
- [Guo 2021][research_guo_2021_b]
- [Guo et al 1988][research_guo_wang_1988]
- [Guo et al 2017][research_guo_bai_2017]
- [Guo et al 2017][research_guo_hou_2017]
- [Guo et al 2017][research_guo_jing_2017]
- [Guo et al 2020][research_guo_zhou_2020]
- [Guo et al 2021][research_guo_li_2021]
- [Guo et al 2022][research_guo_zhang_2022]
- [Guo et al 2025][research_guo_wang_2025]
- [Guo et al 2026][research_guo_liu_2026_b]
- [Gupta 1998][research_gupta_1998]
- [Gupta 2023][research_gupta_2023]
- [Gupta et al 1987][research_gupta_brenner_1987]
- [Gupta et al 1989][research_gupta_brenner_1989]
- [Gurdal 2002][research_gurdal_2002]
- [Gurdal et al 1999][research_gurdal_haftka_1999]
- [Gurley and Ruhlin 1962][research_gurleyjrjr_ruhlincl_1962]
- [Guruswamy 2019][research_guruswamy_2019]
- [Guruswamy and Tu 1989][research_guruswamy_tu_1989]
- [Guruswamy et al 1987][research_guruswamy_goorjian_1987]
- [Gwin 1974][research_gwinlb_1974]
- [Gwin 1976][research_gwin_1976]
- [Haas and Chopra 1988][research_haas_chopra_1988]
- [Haas and Chopra 1990][research_haas_chopra_1990]
- [Haase et al][research_haase_aslund]
- [Had and Růžička 2016][research_had_ruzicka_2016]
- [Hadidoolabi and Ansarian 2017][research_hadidoolabi_ansarian_2017]
- [Hadidoolabi and Ansarian 2018][research_hadidoolabi_ansarian_2018]
- [Haeri and Fadaee 2016][research_haeri_fadaee_2016]
- [Haftka 1977][research_haftka_1977]
- [Hagnell et al 2016][research_hagnell_langbeck_2016]
- [Hahn and Haupt 2022][research_hahn_haupt_2022]
- [Hahn and Kim 1976][research_hahn_kim_1976]
- [Hai 2022][research_hai_2022]
- [Halder et al 2020][research_halder_damodaran_2020]
- [Halder et al 2020][research_halder_das_2020]
- [Haley and Soloway 2022][research_haley_soloway_2022]
- [Hall 1971][research_hall_1971]
- [Hall et al 1974][research_hall_weingarten_1974]
- [Hallauer 1983][research_hallauer_jr_1983]
- [Hallissy and Ayers 1977][research_hallissyjb_ayerstg_1977]
- [Hamada et al 2019][research_hamada_saitoh_2019]
- [Hamissi et al 2019][research_hamissi_bouzid_2019]
- [Hammer and Bright 1998][research_hammer_bright_1998]
- [Han and Pei 2026][research_han_pei_2026]
- [Han et al 2023][research_han_cheng_2023]
- [Han et al 2024][research_han_yang_2024]
- [Hanazaki and Yamazaki 2024][research_hanazaki_yamazaki_2024]
- [Hancock 1971][research_hancock_1971]
- [Hancock 1972][research_hancock_1972]
- [Hancock and Fullerton 1992][research_hancockregis_fullertongordon_1992]
- [Hanman et al 2025][research_hanman_yao_2025]
- [Hansen et al 2022][research_hansen_duan_2022]
- [Hanson and Stengel 1981][research_hansongd_stengelrf_1981]
- [Hanson and Stengel 1983][research_hansongd_stengelrf_1983]
- [Hanson and Stengel 1984][research_hanson_stengel_1984]
- [Hanson et al 2011][research_hansoncurt_schaeferjacob_2011]
- [Hao et al 2022][research_hao_du_2022]
- [Hao et al 2023][research_hao_ma_2023]
- [Hao et al 2026][research_hao_yu_2026]
- [Harper and Robert P. 1955][research_harper_robertp_1955]
- [Harpur 1968][research_harpur_1968]
- [Harris 1974][research_harriscd_1974]
- [Harris 1974][research_harriscd_1974_b]
- [Hart 1956][research_hart_1956]
- [Harvill and Kizer 1976][research_harvillwe_kizerja_1976]
- [Hatake 1985][research_hatake_1985]
- [Hatake 1986][research_hatake_1986]
- [Hayase 1974][research_hayase_1974]
- [Hayashi 1949][research_hayashi_1949]
- [He et al 2020][research_he_tan_2020]
- [He et al 2023][research_he_wang_2023]
- [Hebbar and Pashilkar 2016][research_hebbar_pashilkar_2016]
- [Heckl et al 1962][research_heckl_lyon_1962]
- [Heeg 2006][research_heegjennifer_2006]
- [Heeg et al 2004][research_heegjennifer_spaincharlesv_2004]
- [Heeg et al 2005][research_heegjennifer_spaincharlesv_2005]
- [Heersink et al 2022][research_heersink_sylla_2022]
- [Heinrich et al 2022][research_heinrich_vogt_2022]
- [Hemsch 1989][research_hemsch_1989]
- [Hemsch and Nielsen 1983][research_hemsch_nielsen_1983]
- [Henriquez Huecas et al 2022][research_henriquezhuecas_white_2022]
- [Henry 1961][research_henry_1961]
- [Henschel and Chetty 1989][research_henschel_chetty_1989]
- [Hermanutz and Hornung 2020][research_hermanutz_hornung_2020]
- [Herrington et al 2023][research_herrington_zahed_2023]
- [Herrmann and Ben-Asher 2016][research_herrmann_benasher_2016]
- [Herrmann et al 1966][research_herrmanng_nematnassers_1966]
- [Hertz et al 1982][research_hertztj_shirkmh_1982]
- [Hervin and Fromme 2022][research_hervin_fromme_2022]
- [Hess 1984][research_hess_1984]
- [Hess 1989][research_hess_1989]
- [Hess 1991][research_hess_1991]
- [Hess 2016][research_hess_2016]
- [Hess 2018][research_hess_2018]
- [Hess and Peng 2018][research_hess_peng_2018]
- [Hess and Sunyoto 1985][research_hess_sunyoto_1985]
- [Hess et al 1989][research_hess_seidel_1989]
- [Hicks and Huckabone 1989][research_hicksjohnw_huckabinethomas_1989]
- [Hicks and Matheny 1987][research_hicksjohnw_mathenyneilw_1987]
- [Hicks and Matheny 1989][research_hicksjohnw_mathenyneilw_1989]
- [Hicks and Moulton 1988][research_hicksjohnw_moultonbryanj_1988]
- [Hicks and Petersen 1988][research_hicksjohnw_petersenkevinl_1988]
- [Hicks and Petersen 1989][research_hicksjohnw_petersenkevinl_1989]
- [Hicks et al 1987][research_hicksjohnw_cooperjamesmjr_1987]
- [Hicks et al 1987][research_hicksjohnw_kaniajan_1987]
- [Hicks et al 1987][research_johnwhicks_jankania_1987]
- [Higgins and Shomber 1965][research_higgins_shomber_1965]
- [Hildebrand and Reissner 1944][research_hildebrandfrancisb_reissnereric_1944]
- [Hilger and Ritter 2021][research_hilger_ritter_2021]
- [Hill 1987][research_hill_1987]
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
- [Hobbs et al 2023][research_hobbs_mote_2023]
- [Hodges 2004][research_hodges_2004]
- [Hodgins and Freeman 2025][research_hodgins_freeman_2025]
- [Hodgkinson 2017][research_hodgkinson_2017]
- [Hodgkinson et al 1976][research_hodgkinson_lamanna_1976]
- [Hogan and Rinde 1978][research_hogan_rinde_1978]
- [Hoh and Mitchell 1983][research_hoh_mitchell_1983]
- [Hollowell and Dugundji 1982][research_hollowell_dugundji_1982]
- [Hollowell and Dugundji 1984][research_hollowell_dugundji_1984]
- [Holst and Brown 1983][research_holst_brown_1983]
- [Honeycomb-laminate composite structure 1979][research_honeycomb_laminate_composite_1979]
- [Hong and Cheong 1993][research_hong_cheong_1993]
- [Hongyan and Xiaoyong 2026][research_hongyan_xiaoyong_2026]
- [Hoogervorst and Elham 2017][research_hoogervorst_elham_2017]
- [Hope and Kunz 2019][research_hope_kunz_2019]
- [Hopkins and Yee 1977][research_hopkinsej_yeesc_1977]
- [Hopwood et al 2023][research_hopwood_gresham_2023]
- [Horowitz et al 1980][research_horowitz_golubev_1980]
- [Horsburgh 1911][research_horsburgh_1911]
- [Horton and Mayers 1965][research_horton_mayers_1965]
- [Hortsen et al 1983][research_hortsen_boer_1983]
- [Hoseini and Hodges 2019][research_hoseini_hodges_2019]
- [Hou 2025][research_hou_2025]
- [Housner and Stein 1974][research_housnerjm_steinm_1974]
- [Houtman et al 2023][research_houtman_timme_2023]
- [Houzibe and Chaki 2026][research_houzibe_chaki_2026]
- [How 2004][research_how_2004]
- [Howard and O'Leary 1994][research_howard_oleary_1994]
- [Howdyshell et al 1998][research_howdyshell_trovillion_1998]
- [Hozić et al 2023][research_hozic_thore_2023]
- [Hu 1984][research_hu_1984]
- [Hu 2022][research_hu_2022]
- [Hu et al 2016][research_hu_yang_2016]
- [Hu et al 2025][research_hu_an_2025]
- [Hu et al 2026][research_hu_traisnel_2026]
- [Hua et al 2025][research_hua_wang_2025]
- [Huang et al 2016][research_huang_wang_2016]
- [Huang et al 2018][research_huang_yang_2018]
- [Huang et al 2019][research_huang_yang_2019]
- [Huang et al 2022][research_huang_yu_2022]
- [Huang et al 2023][research_huang_zhen_2023]
- [Huang et al 2024][research_huang_wang_2024]
- [Huang et al 2024][research_huang_zheng_2024]
- [Huang et al 2026][research_huang_li_2026]
- [Huff 1949][research_huff_ww_1949]
- [Huffman 1975][research_huffmanjk_1975]
- [Hui 1986][research_hui_1986]
- [Hummel and Oelker 1994][research_hummel_oelker_1994]
- [Humphreys-Jennings et al 2020][research_humphreysjennings_lappas_2020]
- [Hunn 1953][research_hunn_1953]
- [Huo et al 2021][research_huo_duan_2021]
- [Hurley 1975][research_hurley_1975]
- [Hwu and Tsai 2002][research_hwu_tsai_2002]
- [Hybrid composite laminate structures 1978][research_hybrid_composite_1978]
- [Hübener and Luckner 2026][research_hubener_luckner_2026]
- [Hübler et al 2016][research_hubler_nissle_2016]
- [Iannelli et al 2017][research_iannelli_marcos_2017]
- [Iannelli et al 2018][research_iannelli_marcos_2018]
- [Ibrahim 2026][research_ibrahim_2026]
- [Ibren et al 2020][research_ibren_sulaeman_2020]
- [Ignatyev and Khrabrov 2018][research_ignatyev_khrabrov_2018]
- [Ijaz et al 2019][research_ijaz_hamayun_2019]
- [Ijaz et al 2019][research_ijaz_hamayun_2019_b]
- [Ilcewicz et al 1991][research_ilcewiczlb_walkerth_1991]
- [Iliff and Wang 1996][research_iliff_wang_1996]
- [Iliff et al 1978][research_iliffkw_mainere_1978]
- [Immersion and Invariance Adaptive Fault-Tolerant Attitude Control for a Coaxial Tilt-Rotor eVTOL Aircraft 2026][research_immersion_and_2026]
- [Ingram et al 1986][research_ingramwc_yiplp_1986]
- [Interlaminar shear fracture of interleaved graphite/epoxy composite materials 1992][research_interlaminar_shear_1992]
- [Invernizzi and Lovera 2018][research_invernizzi_lovera_2018]
- [Ioannis and Ioannis 2026][research_ioannis_ioannis_2026]
- [Iovnovich et al 2018][research_iovnovich_nahom_2018]
- [Iryani et al 2019][research_iryani_kadir_2019]
- [Ishii 2023][research_ishii_2023]
- [Ishmael and Wierzbanowski 1985][research_ishmaelsd_wierzbanowskit_1985]
- [Ishmael et al 1990][research_ishmaelstephend_smithrogerse_1990]
- [Isogai 1979][research_isogai_1979]
- [Isogai 1981][research_isogai_1981]
- [Isogai 1988][research_isogai_1988]
- [Isogai 1989][research_isogai_1989]
- [Isogai 1992][research_isogai_1992]
- [Ito and Iwashita 2017][research_ito_iwashita_2017]
- [Ivler et al 2022][research_ivler_truong_2022]
- [İnan and Aliskan 2025][research_inan_aliskan_2025]
- [Jackuliak and Bugaj 2026][research_jackuliak_bugaj_2026]
- [Jacobson and Joshi 1977][research_jacobson_joshi_1977]
- [Jacobson and Joshi 1978][research_jacobson_joshi_1978]
- [Jacome and Elham 2018][research_jacome_elham_2018]
- [Jaeger and Hendry 1959][research_jaeger_hendry_1959]
- [Jaffar Syed Mohamed Ali and Shahzatul Sakinah Binti Haron 2021][research_jaffarsyedmohamedali_shahzatulsakinahbintiharon_2021]
- [Jagana et al 2026][research_jagana_rajagopalan_2026]
- [Jajarmi and Hajipour 2016][research_jajarmi_hajipour_2016]
- [Jalalnezhad 2026][research_jalalnezhad_2026]
- [Janardhan and Grandhi 2003][research_janardhan_grandhi_2003]
- [Jang and Ahn 2022][research_jang_ahn_2022]
- [Jarvis 1975][research_jarviscr_1975]
- [Jarvis and Szalai 1981][research_jarviscr_szalaikj_1981]
- [Jategaonkar 2023][research_jategaonkar_2023]
- [Jategaonkar and Thielecke 1994][research_jategaonkar_thielecke_1994]
- [Jegley and Bush 1997][research_jegleydawnc_bushharoldg_1997]
- [Jegley and Bush 2001][research_jegleydawnc_bushharoldg_2001]
- [Jegley and Wijayratne 2004][research_jegleydawnc_wijayratnedulnathd_2004]
- [Jegley et al 2001][research_jegleydawnc_bushharoldg_2001_b]
- [Jegley et al 2001][research_jegleydawnc_lovejoyandrewe_2001]
- [Jelovica and Cai 2022][research_jelovica_cai_2022]
- [Jenks et al 1977][research_jenksge_henryhf_1977]
- [Jenney and Schreadley 1984][research_jenney_schreadley_1984]
- [Jenney et al 1982][research_jenney_schreadley_1982]
- [Jensen and Crawley 1984][research_jensen_crawley_1984]
- [Jensen et al 1966][research_jensen_falby_1966]
- [Jensen et al 1982][research_jensen_crawley_1982]
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
- [Jia et al 2023][research_jia_sun_2023]
- [Jia et al 2026][research_jia_feng_2026]
- [Jiang et al 2011][research_jiang_zhang_2011]
- [Jiang et al 2018][research_jiang_li_2018]
- [Jiang et al 2018][research_jiang_tian_2018]
- [Jiang et al 2019][research_jiang_tian_2019]
- [Jiang et al 2022][research_jiang_tong_2022]
- [Jiang et al 2024][research_jiang_li_2024]
- [Jiang et al 2024][research_jiang_liu_2024]
- [Jianhong 2022][research_jianhong_2022]
- [Jianhong and Ramirez-Mendoza 2023][research_jianhong_ramirezmendoza_2023]
- [Jianhong and Yanxiang 2026][research_jianhong_yanxiang_2026]
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
- [Johnson 1965][research_johnson_1965]
- [Johnson 1972][research_johnson_1972]
- [Johnson 1973][research_johnson_1973]
- [Johnson and June 1972][research_johnsonrw_junerr_1972]
- [Johnson and McCarty 1977][research_johnsonrw_mccartyje_1977]
- [Johnson et al 1962][research_johnson_henderson_1962]
- [Johnston et al 1974][research_johnston_ashkenas_1974]
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
- [Jun-yi et al 2021][research_junyi_xinbing_2021]
- [Jury 1959][research_m_jury_1959]
- [Jusko and Berger 2026][research_jusko_berger_2026]
- [Kabashkin 2024][research_kabashkin_2024]
- [Kaczmarek 2026][research_kaczmarek_2026]
- [Kafkas et al 2021][research_kafkas_kilimtzidis_2021]
- [Kai 2024][research_kai_2024]
- [Kakkar et al 2026][research_kakkar_streit_2026]
- [Kalam 1981][research_kalam_1981]
- [Kalam et al 2022][research_kalam_seshaiah_2022]
- [Kalinowski 2015][research_kalinowski_2015]
- [Kalms and Bergmann 2020][research_kalms_bergmann_2020]
- [Kalnins 1968][research_kalnins_1968]
- [Kaloerov 1983][research_kaloerov_1983]
- [Kalugin et al 2022][research_kalugin_voropaev_2022]
- [Kamaletdinova and Romanov 2024][research_kamaletdinova_romanov_2024]
- [Kambampati and Smith 2017][research_kambampati_smith_2017]
- [Kambampati et al 2020][research_kambampati_townsend_2020]
- [Kambayashi and Kogiso 2026][research_kambayashi_kogiso_2026]
- [Kanazaki and Setoguchi 2023][research_kanazaki_setoguchi_2023]
- [Kandasamy et al 2018][research_s_sinha_2018]
- [Kang et al 2016][research_kang_park_2016]
- [Kannemans 1995][research_kannemans_1995]
- [Kano et al 2025][research_kano_ryuzono_2025]
- [Kanou and Ibuki 2025][research_kanou_ibuki_2025]
- [Kapania and Issac 1994][research_kapania_issac_1994]
- [Kapania et al 1991][research_kapania_bergen_1991]
- [Kapania et al 1997][research_kapaniarakeshk_issacj_1997]
- [Karal 2001][research_karalmichael_2001]
- [Karimi et al 2022][research_karimi_khorshidi_2022]
- [Karimi Kelayeh and Djavareshkian 2024][research_karimikelayeh_djavareshkian_2024]
- [Karniadakis 2004][research_karniadakis_2004]
- [Karpouzian 1991][research_karpouzian_1991]
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
- [Kaygan and Ulusoy 2018][research_kaygan_ulusoy_2018]
- [Kazarin et al 2021][research_kazarin_golubev_2021]
- [Kcs et al 2024][research_kcs_james_2024]
- [Kearns 1962][research_kearns_1962]
- [Kehoe 1984][research_kehoemw_1984]
- [Kehoe 1987][research_kehoemichaelw_1987]
- [Kehoe and Ellison 1985][research_kehoemw_ellisonjf_1985]
- [Kehoe et al 1990][research_kehoemichaelw_bjarkelisaj_1990]
- [Keidel et al 2020][research_keidel_fasel_2020]
- [Keith and Selberg 1984][research_keith_selberg_1984]
- [Keith and Selberg 1985][research_keith_selberg_1985]
- [Keller 2019][research_keller_2019]
- [Kendall 1985][research_kendall_1985]
- [Kennedy 1991][research_kennedy_1991]
- [Kenway and Martins 2016][research_kenway_martins_2016]
- [Kevrekidis 2002][research_kevrekidis_2002]
- [Key 1971][research_key_1971]
- [Key 1982][research_key_1982]
- [Khajah and Natarajan 2023][research_khajah_natarajan_2023]
- [Khalaf et al 2017][research_khalaf_gan_2017]
- [Khalil and Bauknecht 2024][research_khalil_bauknecht_2024]
- [Khalil and Fezans 2020][research_khalil_fezans_2020]
- [Khalil et al 2016][research_khalil_poirel_2016]
- [Khalil et al 2022][research_khalil_asaro_2022]
- [Khan and Riccio 2024][research_khan_riccio_2024]
- [Khani et al 2017][research_khani_abdalla_2017]
- [Khankalantary et al 2021][research_khankalantary_rezaeeahvanouee_2021]
- [Kharghani and Mittelstedt 2022][research_kharghani_mittelstedt_2022]
- [Khargonekar and Sivashankar 1991][research_khargonekar_sivashankar_1991]
- [Kheiri and Riazat 2025][research_kheiri_riazat_2025]
- [Khodaverdian et al 2025][research_khodaverdian_gohil_2025]
- [Kholodar 2016][research_kholodar_2016]
- [Kholodar 2023][research_kholodar_2023]
- [Kida 1982][research_kida_1982]
- [Kieffer 2006][research_kieffer_2006]
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
- [King and Johnson 1986][research_king_johnson_1986]
- [Kirmse 2016][research_kirmse_2016]
- [Kirsch et al 2020][research_kirsch_montagnier_2020]
- [Kirsch et al 2025][research_kirsch_fathi_2025]
- [Kish et al 1997][research_kish_mosle_1997]
- [Kishi et al 2016][research_kishi_kanazaki_2016]
- [Kishi et al 2022][research_kishi_kanazaki_2022]
- [Kisslinger and Wendl 1971][research_kisslinger_wendl_1971]
- [Kizildeniz and Kiyak 2025][research_kizildeniz_kiyak_2025]
- [Klafin 1988][research_klafin_1988]
- [Klasztorny et al 2018][research_klasztorny_nycz_2018]
- [Klein and Viswanathan 1973][research_klein_viswanathan_1973]
- [Klein et al 1982][research_kleinrw_lapinsm_1982]
- [Klema 1981][research_klema_1981]
- [Klepl 1995][research_klepl_1995]
- [Klimczyk and Goraj 2019][research_klimczyk_goraj_2019]
- [Klotzsche 1984][research_klotzschem_1984]
- [Klyde et al 2004][research_klyde_harris_2004]
- [Knauss and Stone 1982][research_knaussjf_stonerh_1982]
- [Knight 1982][research_knight_1982]
- [Knox-Seith 1963][research_knoxseith_1963]
- [Ko et al 2019][research_ko_kang_2019]
- [Kobelev 2019][research_kobelev_2019]
- [Kodama 1962][research_kodama_1962]
- [Koenig 1984][research_koenig_1984]
- [Koh and Kelly 1989][research_koh_kelly_1989]
- [Kohara et al 2016][research_kohara_tomoeda_2016]
- [Kohnhorst and Magnacca 1980][research_kohnhorst_magnacca_1980]
- [Kolar and Lile 1971][research_kolar_lile_1971]
- [Kolb et al 2019][research_kolb_montagnier_2019]
- [Komarov and Zinchenko 2023][research_komarov_zinchenko_2023]
- [Komnatska and Bondarenko 2017][research_komnatska_bondarenko_2017]
- [Konar et al 1974][research_konar_mahesh_1974]
- [Konatala et al 2024][research_konatala_milz_2024]
- [Kong et al 2025][research_kong_jeon_2025]
- [Kontogiannis et al 2024][research_kontogiannis_savill_2024]
- [Koo and Lee 1994][research_koo_lee_1994]
- [Kopecki 2016][research_kopecki_2016]
- [Kopecki 2021][research_kopecki_2021]
- [Kornev et al 2021][research_kornev_ambrozhevich_2021]
- [Kosmodamianskii and Mitrakov 1976][research_kosmodamianskii_mitrakov_1976]
- [Kosyanchuk et al 2015][research_kosyanchuk_selvesyuk_2015]
- [Kosyanchuk et al 2021][research_kosyanchuk_zheltov_2021]
- [Kota et al 1997][research_kota_hetrick_1997]
- [Kotitschke et al 2026][research_kotitschke_rupprecht_2026]
- [Kou and Zhang 2021][research_kou_zhang_2021]
- [Kousen and Bendiksen 1994][research_kousen_bendiksen_1994]
- [Koyuncuoglu and He 2022][research_koyuncuoglu_he_2022]
- [Krachmalnick et al 1968][research_krachmalnick_vetsch_1968]
- [Kraft and Reeder 1948][research_kraftchristophercjr_reederjp_1948]
- [Kratochvíl and Valenta 2024][research_kratochvil_valenta_2024]
- [Krause et al 1990][research_krause_khargonekar_1990]
- [Krener 2001][research_krener_2001]
- [Kretov and Tiniakov 2022][research_kretov_tiniakov_2022]
- [Kriechbaum and Stineman 1972][research_kriechbaum_stineman_1972]
- [Krone 1980][research_krone_1980]
- [Krone 1980][research_krone_1980_b]
- [Kroo 1982][research_kroo_1982]
- [Krzywoblocki 1943][research_krzywoblocki_1943]
- [Krüger et al 2014][research_kruger_klimmek_2014]
- [Krüger et al 2022][research_kruger_meddaikar_2022]
- [Kuang et al 2025][research_kuang_hu_2025]
- [Kubiak et al 2019][research_kubiak_gliszczynski_2019]
- [Kubica et al 1995][research_kubica_livet_1995]
- [Kuder et al 2015][research_kuder_arrieta_2015]
- [Kulikov 2020][research_kulikov_2020]
- [Kumar et al 2019][research_kumar_onkar_2019]
- [Kumar et al 2020][research_kumar_collini_2020]
- [Kumar et al 2022][research_kumar_kumar_2022]
- [Kumar et al 2025][research_kumar_asha_2025]
- [Kumar Shakya and Sekhar Padhee 2023][research_kumarshakya_sekharpadhee_2023]
- [Kunaporn et al 2014][research_kunaporn_singh_2014]
- [Kuo-Jiun et al 1989][research_kuojiun_pongjeu_1989]
- [Kurade et al 2021][research_kurade_venkatakrishnan_2021]
- [Kurita et al 2013][research_kurita_koike_2013]
- [Kurita et al 2019][research_kurita_koike_2019]
- [Kurzhals 1978][research_kurzhalspr_1978]
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
- [Lamar 1978][research_lamarje_1978]
- [Lamar and Frink 1981][research_lamarje_frinknt_1981]
- [Lamar and Frink 1981][research_lamarje_frinknt_1981_b]
- [Lamar and Luckring 1979][research_lamarje_luckringjm_1979]
- [Lamar et al 1980][research_lamarje_schemenskyrt_1980]
- [Lampton et al 2024][research_lampton_klyde_2024]
- [Lan 1986][research_lance_1986]
- [Lan and Tseng 1987][research_lancedward_tsengjb_1987]
- [Landfield and Rajkovic 1986][research_landfield_rajkovic_1986]
- [Landsberger and Dugundji 1985][research_landsberger_dugundji_1985]
- [Lang et al 2024][research_lang_li_2024]
- [Lapins et al 1982][research_lapinsm_kleinrw_1982]
- [Larson 1987][research_larsonrichardr_1987]
- [Laub 1991][research_laub_1991]
- [Laura and Viazzi 1985][research_laura_viazzi_1985]
- [Lavretsky 2019][research_lavretsky_2019]
- [Lawrence et al 2018][research_lawrence_theodore_2018]
- [Le 2026][research_le_2026]
- [Lee 1977][research_lee_1977]
- [Lee 1995][research_lee_1995]
- [Lee 2016][research_lee_2016]
- [Lee and Cho 1991][research_lee_cho_1991]
- [Lee and Cho 1991][research_lee_cho_1991_b]
- [Lee and Eyi 1993][research_lee_eyi_1993]
- [Lee and Kim 1995][research_lee_kim_1995]
- [Lee and Kim 2021][research_lee_kim_2021]
- [Lee and Ko 2009][research_lee_ko_2009]
- [Lee and Ko 2018][research_lee_ko_2018]
- [Lee and Lee 1990][research_lee_lee_1990]
- [Lee and Mall 1989][research_lee_mall_1989]
- [Lee and Ohman 1984][research_lee_ohman_1984]
- [Lee and Sheikh 2025][research_lee_sheikh_2025]
- [Lee and Sheu 1994][research_lee_sheu_1994]
- [Lee and Singh 2017][research_lee_singh_2017]
- [Lee and Singh 2018][research_lee_singh_2018]
- [Lee and Tang 1989][research_lee_tang_1989]
- [Lee and Yun 2022][research_lee_yun_2022]
- [Lee et al 1994][research_lee_kim_1994]
- [Lee et al 2017][research_lee_snyder_2017]
- [Lee et al 2020][research_lee_kim_2020]
- [Lee et al 2023][research_lee_lee_2023]
- [Lehman and Stearman 1977][research_lehman_stearman_1977]
- [Lei et al 2019][research_lei_bai_2019]
- [Lei et al 2020][research_lei_wang_2020]
- [Lei et al 2021][research_lei_bai_2021]
- [Lei et al 2021][research_lei_guo_2021]
- [Leicester 1970][research_leicester_1970]
- [Leitch et al 2024][research_leitch_stodieck_2024]
- [Leitch et al 2025][research_leitch_stodieck_2025]
- [Lemay et al 1988][research_lemaysp_batillsm_1988]
- [Lemley 1968][research_lemley_1968]
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
- [Li and Pak 2014][research_liwesleyw_pakchangi_2014]
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
- [Li and Zhou 2024][research_li_zhou_2024]
- [Li et al 2014][research_li_liang_2014]
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
- [Li et al 2019][research_li_daronch_2019]
- [Li et al 2019][research_li_gong_2019]
- [Li et al 2019][research_li_he_2019]
- [Li et al 2019][research_li_qian_2019]
- [Li et al 2020][research_li_wang_2020]
- [Li et al 2021][research_li_liu_2021]
- [Li et al 2021][research_li_liu_2021_b]
- [Li et al 2021][research_li_wan_2021]
- [Li et al 2021][research_li_wang_2021]
- [Li et al 2021][research_li_wang_2021_c]
- [Li et al 2022][research_li_bai_2022]
- [Li et al 2022][research_li_liu_2022]
- [Li et al 2022][research_li_sun_2022]
- [Li et al 2022][research_li_zhang_2022]
- [Li et al 2023][research_li_liu_2023]
- [Li et al 2023][research_li_yang_2023]
- [Li et al 2024][research_li_he_2024]
- [Li et al 2024][research_li_kou_2024]
- [Li et al 2024][research_li_qian_2024]
- [Li et al 2024][research_li_zhang_2024]
- [Li et al 2024][research_li_zhang_2024_b]
- [Li et al 2024][research_li_zhang_2024_d]
- [Li et al 2025][research_li_hu_2025]
- [Li et al 2025][research_li_ji_2025]
- [Li et al 2025][research_li_li_2025]
- [Li et al 2025][research_li_lin_2025]
- [Li et al 2025][research_li_shi_2025]
- [Li et al 2025][research_li_shi_2025_b]
- [Li et al 2025][research_li_xiong_2025]
- [Li et al 2026][research_li_miranda_2026]
- [Li et al 2026][research_li_shen_2026]
- [Li et al 2026][research_li_xu_2026]
- [Li et al 2026][research_li_yoon_2026]
- [Lian and Cao 2026][research_lian_cao_2026]
- [Liang et al 2024][research_liang_gao_2024]
- [Liang et al 2024][research_liang_yin_2024]
- [Liang et al 2025][research_liang_ye_2025]
- [Liang et al 2026][research_liang_chen_2026]
- [Liao and Sun 1993][research_liao_sun_1993]
- [Liao et al 2021][research_liao_song_2021]
- [Libeskind et al 1973][research_libeskind_minecci_1973]
- [Librescu and Khdeir 1988][research_librescu_khdeir_1988]
- [Librescu and Maalawi 2009][research_librescu_maalawi_2009]
- [Librescu and Simovich 1988][research_librescu_simovich_1988]
- [Librescu and Song 1992][research_librescu_song_1992]
- [Librescu and Thangjitham 1988][research_librescu_thangjitham_1988]
- [Librescu and Thangjitham 1989][research_librescu_thangjitham_1989]
- [Librescu and Thangjitham 1991][research_librescu_thangjitham_1991]
- [Lichota 2023][research_lichota_2023]
- [Liefer 1990][research_lieferrandallk_1990]
- [Liew and Wang 1993][research_liew_wang_1993]
- [Lifshits and Ryzhov 1978][research_lifshits_ryzhov_1978]
- [Liguori et al 2024][research_liguori_zucco_2024]
- [Lijewski 1988][research_lijewski_1988]
- [Lim et al 1989][research_lim_senthilnathan_1989]
- [Lin and Crawley 1995][research_lin_crawley_1995]
- [Lin et al 1989][research_lin_lu_1989]
- [Lin et al 1994][research_lin_chin_1994]
- [Lind et al 1997][research_lindrickc_brennermartinj_1997]
- [Lindhorst et al 2015][research_lindhorst_haupt_2015]
- [Lindsay and Jordan 1975][research_lindsay_jordan_1975]
- [Liu 2018][research_liu_2018]
- [Liu 2019][research_liu_2019]
- [Liu and Buss 2022][research_liu_buss_2022]
- [Liu and Gao 2020][research_liu_gao_2020_b]
- [Liu and He 2018][research_liu_he_2018]
- [Liu and Liu 2025][research_liu_liu_2025]
- [Liu and Sun 2016][research_liu_sun_2016]
- [Liu and Sun 2017][research_liu_sun_2017]
- [Liu and Tian 2019][research_liu_tian_2019]
- [Liu and Wang 2019][research_liu_wang_2019]
- [Liu and Zhang 2018][research_liu_zhang_2018]
- [Liu and Zhao 2026][research_liu_zhao_2026]
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
- [Liu et al 2023][research_liu_gao_2023]
- [Liu et al 2023][research_liu_li_2023]
- [Liu et al 2023][research_liu_zhang_2023]
- [Liu et al 2023][research_liu_zhou_2023]
- [Liu et al 2024][research_liu_ji_2024]
- [Liu et al 2024][research_liu_zhang_2024]
- [Liu et al 2025][research_liu_zheng_2025]
- [Liu et al 2026][research_liu_li_2026]
- [Liu et al 2026][research_liu_liu_2026]
- [Liu et al 2026][research_liu_qian_2026]
- [Liu et al 2026][research_liu_wang_2026]
- [Liu et al 2026][research_liu_yang_2026]
- [Livne 2018][research_livne_2018]
- [Lo 1978][research_lo_1978]
- [Lo 1979][research_lo_1979]
- [Lo 1980][research_lo_1980]
- [Lo 1981][research_lo_1981]
- [Lock et al 1975][research_lockwp_petersenwr_1975]
- [Lockwood Taylor 1942][research_lockwoodtaylor_1942]
- [Loja et al 2017][research_loja_barbosa_2017]
- [Lokos 1990][research_lokoswilliama_1990]
- [Lombardi 1995][research_lombardi_1995]
- [Lombardi and Morelli 1994][research_lombardi_morelli_1994]
- [Lombardi and Vicini 1994][research_lombardi_vicini_1994]
- [Lombardi et al 1996][research_lombardi_morelli_1996]
- [Lombardi et al 1997][research_lombardi_salvetti_1997]
- [Lomo et al 2023][research_lomo_patel_2023]
- [Long 2019][research_long_2019]
- [Long et al 2021][research_long_mu_2021]
- [Loos and Springer 1983][research_loos_springer_1983]
- [Loth and Boyle 1969][research_loth_boyle_1969]
- [Lottati 1985][research_lottati_1985]
- [Lottati 1987][research_lottati_1987]
- [Lottati 1988][research_lottati_1988]
- [Loughlan 2019][research_loughlan_2019]
- [Loughlan and Ata 1995][research_loughlan_ata_1995]
- [Lovejoy and Scotti 2019][research_lovejoyandrewe_scottistephenj_2019]
- [Lowe 1988][research_lowe_1988]
- [Lowson 1990][research_lowson_1990]
- [Lu and Murthy 1990][research_lu_murthy_1990]
- [Lu et al 2015][research_lu_zhang_2015]
- [Lu et al 2016][research_lu_vankampen_2016]
- [Lu et al 2017][research_lu_tian_2017]
- [Lu et al 2019][research_lu_hu_2019]
- [Lu et al 2019][research_lu_ma_2019]
- [Lu et al 2019][research_lu_zhang_2019]
- [Lu et al 2022][research_lu_hong_2022]
- [Lu et al 2025][research_lu_cao_2025]
- [Lucarini et al 2025][research_lucarini_dirito_2025]
- [Ludeña Cervantes et al 2020][research_ludenacervantes_choi_2020]
- [Lundry 1967][research_lundry_1967]
- [Lundry 1977][research_lundry_1977]
- [Lunghitano et al 2024][research_lunghitano_afonso_2024]
- [Lungu and Lungu 2015][research_lungu_lungu_2015]
- [Luo et al 2022][research_luo_zhang_2022]
- [Luo et al 2024][research_luo_ferrari_2024]
- [Lv et al 2019][research_lv_lei_2019]
- [Lyapunov 1993][research_lyapunov_1993]
- [Lyu and Martins 2015][research_lyu_martins_2015]
- [Lyu et al 2015][research_lyu_kenway_2015]
- [Lyu et al 2018][research_lyu_cao_2018]
- [Lyu et al 2019][research_lyu_zhang_2019]
- [Lyubchak and Fil'shtinskii 1982][research_lyubchak_filshtinskii_1982]
- [Ma and Chen 2020][research_ma_chen_2020]
- [Ma and Chen 2023][research_ma_chen_2023]
- [Ma et al 2015][research_ma_guo_2015]
- [Ma et al 2019][research_ma_dong_2019]
- [Ma et al 2023][research_ma_abouhamzeh_2023]
- [Ma et al 2024][research_ma_abouhamzeh_2024]
- [Ma et al 2024][research_ma_yu_2024]
- [Ma et al 2025][research_ma_liu_2025]
- [Ma et al 2025][research_ma_zhou_2025]
- [Maalawi 2019][research_maalawi_2019]
- [Mabboux et al 2024][research_mabboux_pommierbudinger_2024]
- [Mackall and Allen 1989][research_mackalldalea_allenjamesg_1989]
- [Mackall and Allen 1991][research_mackalldalea_allenjamesg_1991]
- [Mackall et al 1988][research_mackallda_pickettmd_1988]
- [Maewal 1984][research_maewal_1984]
- [Magliacano et al 2025][research_magliacano_tufano_2025]
- [Magness et al 1993][research_magness_robinson_1993]
- [Magnus and Yoshihara 1975][research_magnus_yoshihara_1975]
- [Mahapatra and Halbe 2024][research_mahapatra_halbe_2024]
- [Mahdavi Zafarghandi and Reza Soltani 2024][research_mahdavizafarghandi_rezasoltani_2024]
- [Mahgoub and Cortelezzi 2020][research_mahgoub_cortelezzi_2020]
- [Mahgoub and El-Badawy 2022][research_mahgoub_elbadawy_2022]
- [Mahmood 2025][research_mahmood_2025]
- [Mahulkar 2010][research_mahulkar_2010]
- [Maine and Murray 1988][research_maine_murray_1988]
- [Maity et al 2019][research_maity_hocht_2019]
- [Maiworm et al 2021][research_maiworm_limon_2021]
- [Malcom 1969][research_malcom_1969]
- [Malcom and Husband 1976][research_malcomlg_husbandjh_1976]
- [Malik et al 2017][research_malik_akhtar_2017]
- [Mallik et al 2015][research_mallik_kapania_2015]
- [Mamedov et al 2018][research_mamedov_paryshev_2018]
- [Mammadov and Hajiyev 2018][research_mammadov_hajiyev_2018]
- [Mamonova et al 2019][research_mamonova_soudakov_2019]
- [Mandal and Gu 2016][research_mandal_gu_2016]
- [Manickam et al 2025][research_manickam_polit_2025]
- [Mann and Mercer 1985][research_mannmj_mercerce_1985]
- [Mann and Mercer 1986][research_mannmj_mercerce_1986]
- [Mann et al 1983][research_mannmj_campbellrl_1983]
- [Mann et al 1984][research_mannmj_campbellrl_1984]
- [Mannini and Bartoli 2015][research_mannini_bartoli_2015]
- [Mansour 1970][research_mansour_1970]
- [Mant 1972][research_mant_1972]
- [Manzoor et al 2016][research_manzoor_maqsood_2016]
- [Mao et al 2019][research_mao_xie_2019]
- [Mar and Lin 1979][research_mar_lin_1979]
- [Marano et al 2022][research_marano_belardo_2022]
- [Marcus 1994][research_marcus_1994]
- [Mardanpour et al 2018][research_mardanpour_izadpanahi_2018]
- [Mareca Rios et al 2023][research_marecarios_montesbarrenetxea_2023]
- [Marques et al 2017][research_marques_natarajan_2017]
- [Marqui et al 2017][research_marqui_bueno_2017]
- [Marr and Roderick 1975][research_marr_roderick_1975]
- [Marske 1975][research_marske_1975]
- [Martini et al 2022][research_martini_innocenti_2022]
- [Martínez-Heredia et al 2026][research_martinezheredia_fernandezprada_2026]
- [Marín and Graciani 2022][research_marin_graciani_2022]
- [Masini et al 2019][research_masini_timme_2019]
- [Masini et al 2020][research_masini_timme_2020]
- [Mason and Capone 1983][research_masonml_caponefj_1983]
- [Mateer et al 1987][research_mateergeorgec_seegmillerhlee_1987]
- [Mathur et al 2026][research_mathur_huang_2026]
- [Matos and Marta 2025][research_matos_marta_2025]
- [Matrix cracking and stiffness reduction during the fatigue of a (0/90)9 GFRP laminate 1985][research_matrix_cracking_1985]
- [Matsuki et al 2018][research_matsuki_nishiyama_2018]
- [Matt et al 2025][research_matt_chao_2025]
- [Mayer et al 2016][research_mayer_prowe_2016]
- [Mayer et al 2019][research_mayer_lutz_2019]
- [Mazaheri and Nejati 2015][research_mazaheri_nejati_2015]
- [Mazaheri et al 2015][research_mazaheri_kiani_2015]
- [Mazaheri et al 2015][research_mazaheri_nejati_2015_b]
- [Mazaheri et al 2016][research_mazaheri_nejati_2016]
- [Mazaheri et al 2017][research_mazaheri_nejati_2017]
- [Maślanka et al 2025][research_maslanka_kachel_2025]
- [McAllister and Esfahani 2025][research_mcallister_esfahani_2025]
- [McCormack and Stevens 1947][research_mccormack_stevens_1947]
- [McCutchen 1980][research_mccutchen_1980]
- [McDonnell and Ning 2020][research_mcdonnell_ning_2020]
- [McEneaney 1999][research_mceneaney_1999]
- [McGough et al 1974][research_mcgough_moses_1974]
- [McGREGOR and Smith 1966][research_mcgregor_smith_1966]
- [McGurk et al 2024][research_mcgurk_stodieck_2024]
- [McIntosh et al 2024][research_mcintosh_mishra_2024]
- [McKeehen and Cord 1997][research_mckeehen_cord_1997]
- [McKillip 1991][research_mckillip_1991]
- [McKinney 1972][research_mckinney_1972]
- [McKlNNEY and DOLLYHlGH 1971][research_mcklnney_dollyhlgh_1971]
- [McMaster and Schenk 1974][research_mcmaster_schenk_1974]
- [McRuer et al 1986][research_mcruerd_johnstond_1986]
- [McWilliam et al 2018][research_mcwilliam_zahle_2018]
- [Meglinskii 1966][research_meglinskii_1966]
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
- [Menon and Yousefpor 1996][research_menon_yousefpor_1996]
- [Mhenni et al 2016][research_mhenni_choley_2016]
- [Michaud et al 2018][research_michaud_dalir_2018]
- [Micheli 2024][research_micheli_2024]
- [Micks 1950][research_micks_1950]
- [Miele 1976][research_miele_1976]
- [Mihaila-Andres et al 2019][research_mihailaandres_rosu_2019]
- [Mijovic 1985][research_mijovic_1985]
- [Miles and Broughton 2017][research_miles_broughton_2017]
- [Miller 1965][research_miller_1965]
- [Miller 1970][research_miller_1970]
- [Miller 1983][research_miller_1983]
- [Miller 1986][research_miller_1986]
- [Miller and Clark 1965][research_miller_clark_1965]
- [Miller et al 1983][research_miller_wykes_1983]
- [Milz et al 2026][research_milz_may_2026]
- [Miner and Gloss 1975][research_minerdd_glossbb_1975]
- [Mingong and Sun 2022][research_mingong_sun_2022]
- [Miranda and Bidinotto 2025][research_miranda_bidinotto_2025]
- [Miranda et al 2025][research_miranda_li_2025]
- [Mirtaba et al 2022][research_mirtaba_jeddi_2022]
- [Mishra et al 2025][research_mishra_yadav_2025]
- [Missoum 2012][research_missoum_2012]
- [Mitchell et al 1980][research_mitchell_myers_1980]
- [Miura and Neill 1992][research_miurahirokazu_neilldouglasj_1992]
- [Miyakawa et al 1991][research_miyakawa_ohnuki_1991]
- [Miyasato 1992][research_miyasato_1992]
- [Miyazawa 1993][research_miyazawa_1993]
- [Mkhoyan et al 2022][research_mkhoyan_thakrar_2022]
- [Mobayen and Izadbakhsh 2025][research_mobayen_izadbakhsh_2025]
- [Mochizuki and Yamada 2018][research_mochizuki_yamada_2018]
- [Modaress-Aval et al 2019][research_modaressaval_bakhtiarinejad_2019]
- [Moens 2019][research_moens_2019]
- [Moes et al 2000][research_moestimothyr_noffzgregoryk_2000]
- [Moes et al 2003][research_moestimothyr_smithmarks_2003]
- [Mohamed and G 2020][research_mohamed_g_2020]
- [Mohammad Zadeh and Sayadi 2018][research_mohammadzadeh_sayadi_2018]
- [Mohammadi et al 2025][research_mohammadi_ebrahimi_2025]
- [Mohanty and Chhotaray 1979][research_mohanty_chhotaray_1979]
- [Mohseni and Bernstein 2024][research_mohseni_bernstein_2024]
- [Mojallizadeh 2026][research_mojallizadeh_2026]
- [Molent and Haddad 2020][research_molent_haddad_2020]
- [Monaghan 1981][research_monaghanrc_1981]
- [Moni et al 2024][research_moni_yao_2024]
- [Monshizadeh 2020][research_monshizadeh_2020]
- [Montgomery 1972][research_montgomery_1972]
- [Montgomery and Caglayan 1976][research_montgomery_caglayan_1976]
- [Montgomery and Price 1974][research_montgomeryrc_pricedb_1974]
- [Montgomery and Price 1976][research_montgomery_price_1976]
- [Moon 1996][research_moon_1996]
- [Moore and Frei 1983][research_moore_frei_1983]
- [Moorhouse and Jenkins 1975][research_moorhouse_jenkins_1975]
- [Moosavi and Elasha 2022][research_moosavi_elasha_2022]
- [Moreira et al 2022][research_moreira_gripp_2022]
- [Moreira et al 2024][research_moreira_moleiro_2024]
- [Morino and Obayashi 2015][research_morino_obayashi_2015]
- [Moriya 1982][research_moriya_1982]
- [Morozov and Chermoshentsev 2019][research_morozov_chermoshentsev_2019]
- [Morozov and Janschek 2016][research_morozov_janschek_2016]
- [Morris 1977][research_morris_1977]
- [Morton et al 2023][research_morton_xu_2023]
- [Mottershead and Cooper 2012][research_mottershead_cooper_2012]
- [Moul and Brown 1959][research_moulmartint_brownlawrencew_1959]
- [Moul and Wineman 1952][research_moulmartint_winemanandrewr_1952]
- [Mourey 1979][research_moureydj_1979]
- [Mu et al 2022][research_mu_huang_2022]
- [Mu et al 2026][research_mu_huang_2026]
- [Muir et al 2017][research_muir_arredondogaleana_2017]
- [Mukherjee and Halder 2017][research_mukherjee_halder_2017]
- [Mukherjee and Sinha 2017][research_mukherjee_sinha_2017]
- [Mukhopadhyay and Sorokach 2015][research_mukhopadhyayvivek_sorokachmichaelr_2015]
- [Mulder 1988][research_mulder_1988]
- [Murphy 1996][research_murphypatrickc_1996]
- [Murphy 1999][research_patrickcmurphy_1999]
- [Murphy et al 1976][research_murphy_peloubet_1976]
- [Murray et al 2015][research_murray_doman_2015]
- [Murri et al 1983][research_murridg_croomma_1983]
- [Murri et al 1984][research_murridg_nguyenlt_1984]
- [Muscarello et al 2016][research_muscarello_quaranta_2016]
- [Muñoz and García-Fogeda 2022][research_munoz_garciafogeda_2022]
- [Muñoz and García-Fogeda 2024][research_munoz_garciafogeda_2024]
- [Myers and Walsh 1991][research_myers_walsh_1991]
- [Na and Lee 2024][research_na_lee_2024]
- [Nagabhushan 1991][research_nagabhushan_1991]
- [Naganarayana and Atluri 1995][research_naganarayana_atluri_1995]
- [Nagaraja et al 1981][research_nagaraja_lakin_1981]
- [Nagaraja et al 1982][research_nagaraja_lakin_1982]
- [Nagarathna and Deodhare 2023][research_k_deodhare_2023]
- [Nagy and Fossati 2022][research_nagy_fossati_2022]
- [Naihong et al 1993][research_naihong_yaohua_1993]
- [Najmi et al 2024][research_najmi_khan_2024]
- [Nakamura 1982][research_nakamura_1982]
- [Nam et al 2000][research_nam_chen_2000]
- [Namani Koureh et al 2026][research_namanikoureh_shahverdi_2026]
- [Nan et al 2024][research_nan_zheng_2024]
- [Nangia and Palmer 2002][research_nangia_palmer_2002]
- [Nangia et al 2003][research_nangia_palmer_2003]
- [Napolitano 1996][research_napolitanomarcellor_1996]
- [Napolitano 2002][research_napolitano_2002]
- [Napolitano and Spagnuolo 1993][research_napolitanomarcellor_spagnuolojoellem_1993]
- [Narayanan et al 2026][research_narayanan_kumar_2026]
- [Narendra and Tripathi 1973][research_narendra_tripathi_1973]
- [Narenshakthi and Dharani 2025][research_narenshakthi_dharani_2025]
- [Naresh and Srinivas 2024][research_naresh_srinivas_2024]
- [Narimani et al 2025][research_narimani_haddadpour_2025]
- [nath and ana 2017][research_nath_ana_2017]
- [Navrátil 2017][research_navratil_2017]
- [Nazarenko and Nevezhina 1972][research_nazarenko_nevezhina_1972]
- [Nazari et al 2017][research_nazari_seron_2017]
- [Nazeer et al 2021][research_nazeer_wang_2021]
- [Neal and Smith 1970][research_neal_smith_1970]
- [Negahban et al 2024][research_negahban_bashir_2024]
- [Negahban et al 2025][research_negahbanb_khalafi_2025]
- [Nejati and Mazaheri 2017][research_nejati_mazaheri_2017]
- [Nekooei et al 2021][research_nekooei_farsangi_2021]
- [Nelson and Mouch 1978][research_nelson_mouch_1978]
- [Neu and Huang 1973][research_neu_huang_1973]
- [Newkirk 1979][research_newkirk_1979]
- [Newton and Kroo 2025][research_newton_kroo_2025]
- [Nguyen 2019][research_nguyen_2019]
- [Nguyen and Gilert 1990][research_nguyenluatt_gilertwilliamp_1990]
- [Nguyen and Urnes 2012][research_nguyennhan_jamesurnessr_2012]
- [Nguyen et al 1979][research_nguyenlt_gilbertwp_1979]
- [Nguyen et al 1980][research_luattnguyen_williampgilbert_1980]
- [Nguyen et al 2015][research_nguyennhan_kaulupender_2015]
- [Nguyen et al 2016][research_nguyen_olaru_2016]
- [Nguyen et al 2018][research_nguyen_reynolds_2018]
- [Nguyen et al 2021][research_nguyen_lowenberg_2021]
- [Nguyen et al 2025][research_nguyen_han_2025]
- [Nguyen et al 2026][research_nguyen_prodan_2026]
- [Ni et al 2023][research_ni_li_2023]
- [Nibbelink and Peters 1993][research_nibbelinkbruced_petersdavida_1993]
- [Niblett 1986][research_niblett_1986]
- [Niblett 1988][research_niblett_1988]
- [Nicholas et al 1984][research_nicholaswu_navillegl_1984]
- [Niel et al 2017][research_niel_seuret_2017]
- [Nield 1981][research_nield_iv_1981]
- [Nihtilä 1989][research_nihtila_1989]
- [Nikolaev 2019][research_nikolaev_2019]
- [Nikolaou et al 2026][research_nikolaou_kilimtzidis_2026]
- [Nikrad et al 2015][research_nikrad_asadi_2015]
- [Nitschke et al 2019][research_nitschke_vincenti_2019]
- [Niu and Li 2022][research_niu_li_2022]
- [Niu and Zhang 2022][research_niu_zhang_2022]
- [Niu et al 2018][research_niu_chen_2018]
- [Noll et al 1983][research_noll_calico_1983]
- [Noll et al 1984][research_noll_eastep_1984]
- [Non-linear bending of antisymmetric angle ply laminated plates 1977][research_non_linear_bending_1977]
- [Nonweiler 1960][research_nonweiler_1960]
- [Noordin et al 2023][research_noordin_mohdbasri_2023]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]
- [Norton 1990][research_norton_1990]
- [Norwood 1992][research_norwood_1992]
- [Ntantis and Xezonakis 2024][research_ntantis_xezonakis_2024]
- [Numerical Analysis of the Flow Pattern and Vortex Breakdown over a Pitching Delta wing at Supersonic Speeds 2017][research_numerical_analysis_2017]
- [Numerical and Experimental Determination of Canard Controlled Missile Aerodynamic Coefficients in Subsonic Regime 2019][research_numerical_and_2019]
- [Numerical Study of Geometrical Properties of Full-Span Tubercle Leading Edge Wing at Post-Stall Condition 2023][research_numerical_study_2023]
- [Oberkampf and Nicolaides 1971][research_oberkampf_nicolaides_1971]
- [Obilanade et al 2025][research_obilanade_torlind_2025]
- [Ocali and Sezer 1992][research_ocali_sezer_1992]
- [Ochi and Kanai 1995][research_ochi_kanai_1995]
- [Ochôa et al 2019][research_ochoa_groves_2019]
- [Oelker and Hummel 1989][research_oelker_hummel_1989]
- [Ogburn et al 1991][research_marilyneogburn_johnvfoster_1991]
- [Ogunvoul et al 2017][research_ogunvoul_balanchuk_2017]
- [Ohkawa 1985][research_ohkawa_1985]
- [Ohkawa 1986][research_ohkawa_1986]
- [Ohkuma 1993][research_ohkuma_1993]
- [Ohta et al 1979][research_ohta_nikiforuk_1979]
- [Ohta et al 1982][research_ohta_nikiforuk_1982]
- [Okumoto and Elsanker 1973][research_okumoto_elsanker_1973]
- [Oland et al 2016][research_oland_andersen_2016]
- [Olivett et al 2021][research_olivett_corrao_2021]
- [Olsen 1965][research_olsen_1965]
- [Olsen 1966][research_olsen_1966]
- [Om et al 2020][research_om_park_2020]
- [Onkar 2021][research_onkar_2021]
- [Onkar et al 2024][research_onkar_kumar_2024]
- [Opgenoord and Willcox 2019][research_opgenoord_willcox_2019]
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
- [Othman et al 2019][research_othman_silva_2019]
- [Otsuka and Makihara 2017][research_otsuka_makihara_2017]
- [Ouyang and Lin 2017][research_ouyang_lin_2017]
- [Ouyang et al 2021][research_ouyang_gu_2021]
- [Ouyang et al 2021][research_ouyang_zeng_2021]
- [Owens and Perkins 1996][research_owens_perkins_1996]
- [Oyarhossein et al 2025][research_oyarhossein_sugiyama_2025]
- [Oyibo 1984][research_oyibo_1984]
- [Oza and Vala 2021][research_oza_vala_2021]
- [Ozbek et al 2024][research_ozbek_ekici_2024]
- [Ozdil and Carlsson 1992][research_ozdil_carlsson_1992]
- [O’Donnell and Mohseni 2019][research_odonnell_mohseni_2019]
- [O’Rourke et al 2019][research_orourke_kolmanovsky_2019]
- [Packard et al 2009][research_packard_seiler_2009]
- [Padovan 1973][research_padovan_1973]
- [Padovan 1974][research_padovan_1974]
- [Padovan and Gosset 1974][research_padovan_gosset_1974]
- [Pagano 1974][research_pagano_1974]
- [Palframan et al 2019][research_palframan_fry_2019]
- [Palkin and Zenchenko 2025][research_palkin_zenchenko_2025]
- [Palm et al 2000][research_palmtod_mahlermary_2000]
- [Pan and Cheng 1995][research_pan_cheng_1995]
- [Pan and Huang 2019][research_pan_huang_2019]
- [Pan and Liu 2019][research_pan_liu_2019]
- [Pang et al 2014][research_pang_cesnik_2014]
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
- [Passenbrunner et al 2016][research_passenbrunner_sassano_2016]
- [Passive wing/store flutter suppression 1982][research_passive_wing_store_1982]
- [Patartics et al 2022][research_patartics_liptak_2022]
- [Patel et al 2022][research_patel_kumar_2022]
- [Patel et al 2023][research_patel_deodhare_2023]
- [Patne et al 2020][research_patne_ingole_2020]
- [Patni et al 2019][research_patni_minera_2019]
- [Patterson and Grenestedt 2018][research_patterson_grenestedt_2018]
- [Paul and Rein 2017][research_paul_rein_2017]
- [Paulson and Thomas 1978][research_paulsonjwjr_thomasjl_1978]
- [Paulson and Thomas 1979][research_paulsonjwjr_thomasjl_1979_b]
- [Paulson et al 1979][research_paulsonjwjr_thomasjl_1979]
- [Pearson and Aiken 1944][research_pearsonhenrya_aikenwilliamsjr_1944]
- [Peck and Hudson 1956][research_peck_hudson_1956]
- [Pedrioli et al 2026][research_pedrioli_vaiuso_2026]
- [Peled and Powell 1978][research_peledu_powelljd_1978]
- [Pellerin 1988][research_pellerin_1988]
- [Pelykh and Andryushchenko 2024][research_pelykh_andryushchenko_2024]
- [Pena 2020][research_penafrancisco_2020]
- [Pena et al 2018][research_penafrancisco_martinsbenjamin_2018]
- [Pendem 2023][research_pendem_2023]
- [Pendleton et al 1995][research_pendleton_moster_1995]
- [Peng et al 2026][research_peng_cao_2026]
- [Peng et al 2026][research_peng_li_2026]
- [Pengelley and Wilson 1954][research_pengelley_wilson_1954]
- [Pereira et al 2021][research_pereira_sales_2021]
- [Perfect et al 2015][research_perfect_jump_2015]
- [Perfect et al 2015][research_perfect_jump_2015_b]
- [Perkins and Brice 1966][research_perkins_brice_1966]
- [Perry 1976][research_perrybiii_1976]
- [Perry 1982][research_perrybiii_1982]
- [Perry 2025][research_perry_2025]
- [Perry and Rievley 1961][research_perry_rievley_1961]
- [Persoon et al 1980][research_persoon_roos_1980]
- [Persoon et al 1984][research_persoon_horsten_1984]
- [Petersen 1981][research_petersenkl_1981]
- [Petre and Ashley 1976][research_petre_ashley_1976]
- [Petriconi et al 2026][research_petriconi_lomazzi_2026]
- [Peyada and Ghosh 2023][research_peyada_ghosh_2023]
- [Pfeifle and Fichter 2023][research_pfeifle_fichter_2023]
- [Pfnür and Breitsamter 2019][research_pfnur_breitsamter_2019]
- [Pham 2022][research_pham_2022]
- [Phan 2020][research_phan_2020]
- [Philibert et al 2022][research_philibert_yao_2022]
- [Philippidis 1994][research_philippidis_1994]
- [Phillips 1965][research_phillips_1965]
- [Phuekpan et al 2025][research_phuekpan_khammee_2025]
- [Piao et al 2019][research_piao_zhang_2019]
- [Pidaparti 1993][research_pidaparti_1993]
- [Pidaparti and Yang 1993][research_pidaparti_yang_1993]
- [Pierre et al 2023][research_pierre_iervolino_2023]
- [Pizzoli et al 2022][research_pizzoli_saltari_2022]
- [Place et al 1974][research_place_altmann_1974]
- [Placek and Ruchała 2018][research_placek_ruchala_2018]
- [Plaetschke et al 1982][research_plaetschke_mulder_1982]
- [Plotkin 1978][research_plotkin_1978]
- [Plyako 1977][research_plyako_1977]
- [Poll 1986][research_poll_1986]
- [Pollack and van Kampen 2023][research_pollack_vankampen_2023]
- [Pollack et al 2024][research_pollack_theodoulis_2024]
- [Pollack et al 2026][research_pollack_theodoulis_2026]
- [Polyester, fibreglass-reinforced composite laminate 1978][research_polyester_fibreglass_reinforced_1978]
- [Poole et al 2022][research_poole_allen_2022]
- [Poole et al 2026][research_poole_allen_2026]
- [Portapas and Cooke 2020][research_portapas_cooke_2020]
- [Posingies 1979][research_posingies_1979]
- [Pourtakdoust and Khodabakhsh 2026][research_pourtakdoust_khodabakhsh_2026]
- [Poussot-Vassal et al 2017][research_poussotvassal_demourant_2017]
- [Powers 1980][research_powersbg_1980]
- [Powers 1982][research_powers_1982]
- [Prajapati and Prasad 2019][research_prajapati_prasad_2019]
- [Prasad et al 1967][research_prasad_nematnasser_1967]
- [Preissler and Schaufele 1991][research_preissler_schaufele_1991]
- [Price and Lee 1993][research_price_lee_1993]
- [Pritt 1980][research_pritt_1980]
- [Prototype Digital Flight Control Computer 1986][research_prototype_digital_1986]
- [Pryor and Barker 1970][research_pryor_barker_1970]
- [Przekop and Jegley 2014][research_przekopadam_jegleydawnc_2014_b]
- [Przekop et al 2014][research_przekopadam_jegleydawnc_2014]
- [Pusch et al 2019][research_pusch_knoblach_2019]
- [Pushtaev 1989][research_pushtaev_1989]
- [Puthisikamani et al 2023][research_puthisikamani_sreenivasaraja_2023]
- [Putnam 1983][research_putnamtw_1983]
- [Putnam 1984][research_putnamtw_1984]
- [Putnam 1984][research_putnamtw_1984_b]
- [Putnam et al 1986][research_putnamtw_petersenkl_1986]
- [Pérez et al 2022][research_perez_theodoulis_2022]
- [Qi and Zhao 2020][research_qi_zhao_2020]
- [Qi et al 2018][research_qi_zhao_2018]
- [Qi et al 2026][research_qi_yuan_2026]
- [Qian 2018][research_qian_2018]
- [Qian et al 2025][research_qian_xinhui_2025]
- [Qiao et al 2018][research_qiao_gao_2018]
- [Qiao et al 2018][research_qiao_wu_2018]
- [Qin et al 2017][research_qin_liu_2017]
- [Qin et al 2023][research_qin_liu_2023]
- [Qiu 2022][research_qiu_2022]
- [Qiu et al 2017][research_qiu_yuan_2017]
- [Qiu et al 2018][research_qiu_fang_2018]
- [Qu and Annaswamy 2016][research_qu_annaswamy_2016]
- [Qu and Li 2022][research_qu_li_2022]
- [Quagliarella and Iuliano 2017][research_quagliarella_iuliano_2017]
- [Quero et al 2019][research_quero_vuillemin_2019]
- [Radetskaya 2022][research_radetskaya_2022]
- [Radford et al 1980][research_radfordrc_smithr_1980]
- [Rafi et al 2017][research_rafi_steck_2017]
- [Ragab et al 2018][research_ragab_hajj_2018]
- [Raghavan 1971][research_raghavan_1971]
- [Rahima et al 2026][research_rahima_yassine_2026]
- [Rainbird et al 2015][research_rainbird_peiro_2015]
- [Raiola et al 2021][research_raiola_discetti_2021]
- [Rais-Rohani 1994][research_raisrohanimasoud_1994]
- [Rais-Rohani 1999][research_raisrohanimasound_1999]
- [Rais-Rohani et al 1992][research_raisrohanim_haftkart_1992]
- [Rajamurugu et al 2024][research_rajamurugu_satyam_2024]
- [Rajpal et al 2019][research_rajpal_kassapoglou_2019]
- [Rajpal et al 2021][research_rajpal_mitrotta_2021]
- [Ramamoorthy 1992][research_ramamoorthy_1992]
- [Ramroop et al 2025][research_ramroop_chinchamee_2025]
- [Ranaudo et al 2000][research_ranaudorichardj_ratvaskythomasp_2000]
- [Raney 1987][research_raneydavidl_1987]
- [Raney and Batterson 1989][research_raney_batterson_1989]
- [Rao 1975][research_rao_1975]
- [Rao and Hofer 1973][research_rao_hofer_1973]
- [Rao and Padmanabhan 2019][research_rao_padmanabhan_2019]
- [Rao and Uma Maheswara Rao 1992][research_rao_umamaheswararao_1992]
- [Rao et al 2023][research_rao_shi_2023]
- [Raouf 1994][research_raouf_1994]
- [Rapoff et al 1990][research_rapoffandrewj_dillharoldd_1990]
- [Rashed and Demir 2022][research_rashed_demir_2022]
- [Rashmikant and Abe 2026][research_rashmikant_abe_2026]
- [Rate sensitivity of Mode II interlaminar fracture toughness in graphite/epoxy and graphite/PEEK composite materials 1988][research_rate_sensitivity_1988]
- [Rath and Fichter 2020][research_rath_fichter_2020]
- [Rathnasabapathy et al 2022][research_rathnasabapathy_mouritz_2022]
- [Rauer 2019][research_rauer_2019]
- [Ray et al 1972][research_rayej_mckinneylw_1972]
- [Ray et al 1973][research_rayej_mckinneylw_1973]
- [Ray et al 1988][research_ray_hicks_1988]
- [Ray et al 1990][research_ray_hicks_1990]
- [Rea et al 2018][research_rea_pecora_2018]
- [Rea J B Co Inc Santa Monica Ca 1957][research_reajbcoincsantamonicaca_1957]
- [Reddy 1982][research_reddy_1982]
- [Reddy 1987][research_reddy_1987]
- [Redeker and Wichmann 1991][research_redeker_wichmann_1991]
- [Rediess 1976][research_hermanarediess_1976]
- [Rediess and Szalai 1975][research_rediessha_szalaikj_1975]
- [Reding and Ericsson 1977][research_reding_ericsson_1977]
- [Reeder 1958][research_reeder_1958]
- [Refinement of aircraft dynamics model and control system according to the flight-tests results 2023][research_refinement_of_2023]
- [Regulator with reference model for u nmanned aircraft control when boarding on unmanned vehicle 2022][research_regulator_with_2022]
- [Rehan et al 2015][research_rehan_iqbal_2015]
- [Rehman 2022][research_rehman_2022]
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
- [Report no. 121, The minimum induced Drag of aerofoils 1921][research_report_no_1921]
- [Report No. 349. A proof of the theorem regarding the distribution of lift over the span, for minimum induced drag 1930][research_report_no_1930]
- [Research and Design of Automatic Flight Control System Test System 2022][research_research_and_2022]
- [Restifo et al 2026][research_restifo_villa_2026]
- [Review of Fault-tolerant Control for Flight Control System 2024][research_review_of_2024]
- [Reyes et al 2019][research_reyes_climent_2019]
- [Rhodes and Selberg 1982][research_rhodesmd_selbergbp_1982]
- [Rich et al 1974][research_richmj_ridgleygf_1974]
- [Richards et al 2016][research_richards_yao_2016]
- [Richter et al 2024][research_richter_calix_2024]
- [Richwine and Fisher 1991][research_richwinedavidm_fisherdavidf_1991]
- [Richwine and Fisher 1992][research_davidmrichwine_davidffisher_1992]
- [Rickard 1978][research_rickardww_1978]
- [Ricketts and Doggett 1980][research_rickettsrh_doggettrvjr_1980]
- [Ricketts et al 1983][research_rickettsrh_sandfordmc_1983]
- [Ricketts et al 1983][research_rickettsrh_watsonjj_1983]
- [Rieck et al 2026][research_rieck_herrmann_2026]
- [Rigatos 2021][research_rigatos_2021]
- [Rimer et al 1983][research_rimer_chipman_1983]
- [Rimer et al 1984][research_rimer_chipman_1984]
- [Rimer et al 1984][research_rimerm_chipmanr_1984]
- [Rimer et al 1986][research_rimer_chipman_1986]
- [Ringertz 1994][research_ringertz_1994]
- [Rising et al 1984][research_risingjj_daviswj_1984]
- [Riso and Cesnik 2023][research_riso_cesnik_2023]
- [Rivero et al 2021][research_rivero_fournier_2021]
- [Rizzetta 1977][research_rizzetta_1977]
- [Rizzetta 1979][research_rizzetta_1979]
- [Ro et al 1992][research_ro_barlow_1992]
- [Roache 1965][research_roache_1965]
- [Robbins et al 2023][research_robbins_stansbury_2023]
- [Roberts et al 1977][research_robertspa_swaimrl_1977]
- [Roberts et al 2015][research_roberts_reed_2015]
- [Robinson 2004][research_robinson_2004]
- [Robinson and Robinson 1980][research_robinson_robinson_1980]
- [Robust Controller Design Based on L1 Adaptive Control Method 2016][research_robust_controller_2016]
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
- [Rogólski and Olejnik 2018][research_rogolski_olejnik_2018]
- [Rohella and Chatterjee 1979][research_rohella_chatterjee_1979]
- [Rohith and Sinha 2020][research_rohith_sinha_2020]
- [Roizner and Karpel 2018][research_roizner_karpel_2018]
- [Roizner and Karpel 2019][research_roizner_karpel_2019]
- [Roizner et al 2019][research_roizner_raveh_2019]
- [Rokhsaz and Selberg 1990][research_rokhsaz_selberg_1990]
- [Romano et al 2019][research_romano_ciminello_2019]
- [Ronfle-Nadaud 2009][research_ronflenadaud_2009]
- [Rong et al 2022][research_rong_huang_2022]
- [Rongrong et al 2018][research_rongrong_zhengyin_2018]
- [Rooney et al 1982][research_rooneyrh_chungjc_1982]
- [Roorda 1967][research_roorda_1967]
- [Roscoe et al 1975][research_roscoe_eisele_1975]
- [Rose and Seginer 1978][research_rose_seginer_1978]
- [Rosique et al 2019][research_rosique_alamin_2019]
- [Roskam and Lan 1973][research_roskamj_lanc_1973]
- [Roskam et al 1972][research_roskamj_lanc_1972]
- [Ross 1984][research_ross_1984]
- [Ross and Matarazzo 1982][research_ross_matarazzo_1982]
- [Roufaeil and Dawe 1982][research_roufaeil_dawe_1982]
- [Rouhi et al 2018][research_rouhi_ghayoor_2018]
- [Rowley 2008][research_rowley_2008]
- [Roy and Mukherjee 2026][research_roy_mukherjee_2026]
- [Roylance 1980][research_roylance_1980]
- [Ruhlin et al 1982][research_ruhlin_watson_1982]
- [Ruhlin et al 1983][research_ruhlin_rauch_1983]
- [Ruhlin et al 1983][research_ruhlin_watson_1983]
- [Rumble 1987][research_rumble_1987]
- [Runkel et al 2018][research_runkel_fasel_2018]
- [Runyan et al 1952][research_runyan_cunningham_1952]
- [Ruo et al 1985][research_ruo_malone_1985]
- [Ruscheweyh 1983][research_ruscheweyh_1983]
- [Russo et al 1986][research_russo_healy_1986]
- [Rustenburg 1972][research_rustenburg_1972]
- [Rutkowski 1979][research_rutkowski_1979]
- [Ružička et al 2013][research_ruzicka_rydel_2013]
- [Ryder and Walker 1976][research_ryder_walker_1976]
- [Sabater et al 2022][research_sabater_bekemeyer_2022]
- [Sabatini et al 2026][research_sabatini_coppotelli_2026]
- [Sabido et al 2017][research_sabido_bahamonde_2017]
- [Sabri et al 2022][research_sabri_elzaabalawy_2022]
- [Sachan and Padhi 2020][research_sachan_padhi_2020]
- [Sachs 1975][research_sachs_1975]
- [Sachs 1977][research_sachs_1977]
- [Saderla et al 2016][research_saderla_dhayalan_2016]
- [Saderla et al 2018][research_saderla_kim_2018]
- [Sadoff et al 1961][research_sadoffmelvin_mcfaddennormanm_1961]
- [Saetti 2025][research_saetti_2025]
- [Saetti 2025][research_saetti_2025_b]
- [Saetti and Rogers 2024][research_saetti_rogers_2024]
- [Saetti et al 2020][research_saetti_horn_2020]
- [Saheby et al 2026][research_saheby_jialu_2026]
- [Sahin et al 2026][research_sahin_yayla_2026]
- [Sahu et al 2000][research_sahu_heavey_2000]
- [Sahyoun et al 2026][research_sahyoun_boose_2026]
- [Salagame et al 2025][research_salagame_pandya_2025]
- [Salahudden 2025][research_salahudden_2025]
- [Salahudden et al 2024][research_salahudden_agrawal_2024]
- [Saltzman et al 1994][research_saltzmanedwinj_hicksjohnw_1994]
- [Sammonds et al 1982][research_sammondsroberti_mcneillwaltere_1982]
- [Sampling schemes in sampled-data control systems 1961][research_sampling_schemes_1961]
- [Samputh et al 2024][research_samputh_moey_2024]
- [Samukham et al 2017][research_samukham_raju_2017]
- [Samukham et al 2019][research_samukham_raju_2019]
- [Samukham et al 2020][research_samukham_vyasarayani_2020]
- [Sanders 1965][research_sanders_1965]
- [Sandhu et al 1991][research_sandhu_wolfe_1991]
- [Sang and Zhang 2022][research_sang_zhang_2022]
- [Saporito et al 2023][research_saporito_daronch_2023]
- [Saputra and Purabaya 2018][research_saputra_purabaya_2018]
- [Sato 1973][research_sato_1973]
- [Sato et al 2017][research_sato_muraoka_2017]
- [Satt and Ilanko 2007][research_satt_ilanko_2007]
- [Savelev and Neretin 2022][research_savelev_neretin_2022]
- [Savin and Hantrais-Gervois 2020][research_savin_hantraisgervois_2020]
- [Saviolo and Loianno 2023][research_saviolo_loianno_2023]
- [Savithri and Varadan 1990][research_savithri_varadan_1990]
- [Sawyer 1976][research_sawyerjw_1976]
- [Schewe and Mai 2018][research_schewe_mai_2018]
- [Schieni et al 2024][research_schieni_modasiya_2024]
- [Schildkamp et al 2023][research_schildkamp_chang_2023]
- [Schmeichel 1967][research_schmeichel_1967]
- [Schmidt 2016][research_schmidt_2016]
- [Schmidt 2016][research_schmidt_2016_b]
- [Schmidt and Schierman 1990][research_schmidtdavidk_schiermanjohnd_1990]
- [Schmidt et al 2020][research_schmidt_danowsky_2020]
- [Schpey 1980][research_schpey_1980]
- [Schreadley 1977][research_schreadley_1977]
- [Schroeder et al 2001][research_schroederjefferya_chungwilliamwy_2001]
- [Schuet et al 2017][research_schuet_lombaerts_2017]
- [Schuster 1995][research_schuster_1995]
- [Schuster and Edwards 2004][research_schusterdavidm_edwardsjohnw_2004]
- [Schuster and Lokos 1988][research_schuster_lokos_1988]
- [Schwanz 1972][research_schwanz_1972]
- [Schäfer et al 2018][research_schafer_vidy_2018]
- [Schütte et al 2018][research_schutte_huber_2018]
- [Sciuva 1992][research_sciuva_1992]
- [Scordamaglia et al 2025][research_scordamaglia_mattei_2025]
- [Scott et al 2016][research_scott_bartels_2016]
- [Seegmiller 1963][research_seegmiller_1963]
- [Sefic and Cutler 1986][research_sefic_cutler_1986]
- [Sefic and Maxwell 1986][research_sefic_maxwell_1986]
- [Sefic and Maxwell 1987][research_sefic_maxwell_1987]
- [Segel 1952][research_segel_1952]
- [Seidel et al 1985][research_seidelda_sandfordmc_1985]
- [Seidel et al 1987][research_seidel_sandford_1987]
- [Seidel et al 1989][research_seidel_eckstrom_1989]
- [Seitz et al 2019][research_seitz_hubner_2019]
- [sekhar et al 2024][research_sekhar_suresh_2024]
- [Selberg and Cronin 1985][research_selbergbp_cronindl_1985]
- [Sellers et al 1988][research_sellerswilliamliii_meyersjamesf_1988]
- [Sellers et al 2004][research_sellerswilliamliii_meyersjamesf_2004]
- [Sen and Bhattacharya 2016][research_sen_bhattacharya_2016]
- [Seraj and Ganesan 2018][research_seraj_ganesan_2018]
- [Serani et al 2024][research_serani_diez_2024]
- [Seres et al 2023][research_seres_liu_2023]
- [Serhat et al 2020][research_serhat_bediz_2020]
- [Seshadri and Krishnamurthy 2017][research_seshadri_krishnamurthy_2017]
- [Setiawarman and Sasongko 2026][research_setiawarman_sasongko_2026]
- [Setoguchi and Kanazaki 2020][research_setoguchi_kanazaki_2020]
- [Seyoung 1990][research_seyoung_1990]
- [Shafei et al 2024][research_shafei_faroughi_2024]
- [Shafer 1980][research_shafermf_1980]
- [Shafer and Steinmetz 2001][research_shafermaryf_steinmetzpaul_2001]
- [Shafer and Steinmetz 2001][research_shafermaryf_steinmetzpaul_2001_b]
- [Shafer et al 1983][research_shafermf_smithre_1983]
- [Shafer et al 1984][research_shafermf_smithre_1984]
- [Shafighfard et al 2019][research_shafighfard_demir_2019]
- [Shah and Desai 1973][research_shah_desai_1973]
- [Shah and Mehta 2017][research_shah_mehta_2017]
- [Shah et al 2023][research_parthivnshah_ericlblades_2023]
- [Shakya and Padhee 2023][research_shakya_padhee_2023]
- [Shankar and Malmuth 1982][research_shankar_malmuth_1982]
- [Shankar and Malmuth 1983][research_shankar_malmuth_1983]
- [Shankar et al 1981][research_shankar_malmuth_1981]
- [Shanley 1943][research_shanley_1943]
- [Shao et al 2025][research_shao_sun_2025]
- [Sharif et al 2022][research_sharif_abbas_2022]
- [Sharifi et al 2025][research_sharifi_vincenti_2025]
- [Sharma et al 2022][research_sharma_agrawal_2022]
- [Sharma et al 2023][research_sharma_swain_2023]
- [Sharqi and Cesnik 2023][research_sharqi_cesnik_2023]
- [Shayak et al 2024][research_shayak_girdhar_2024]
- [Shcherban et al 2022][research_shcherban_sterlin_2022]
- [Shearwood et al 2020][research_shearwood_nabawy_2020]
- [Sheikh et al 2023][research_sheikh_lee_2023]
- [Sheikhi et al 2024][research_sheikhi_rafieianamagh_2024]
- [Sheikhi et al 2024][research_sheikhi_rafieianamagh_2024_b]
- [Shen and Chen 2022][research_shen_chen_2022]
- [Shen and Chen 2023][research_shen_chen_2023]
- [Shen and Chen 2024][research_shen_chen_2024]
- [Shen and Wen 2018][research_shen_wen_2018]
- [Shen et al 2015][research_shen_bai_2015]
- [Shen et al 2021][research_shen_huang_2021]
- [Shen et al 2022][research_shen_chang_2022]
- [Sherrer et al 1981][research_sherrer_hertz_1981]
- [Sheshanarayana et al 2026][research_sheshanarayana_armstrong_2026]
- [Shi and Bezine 1988][research_shi_bezine_1988]
- [Shi and Wan 2015][research_shi_wan_2015]
- [Shi et al 2018][research_shi_tan_2018]
- [Shi et al 2019][research_shi_lyu_2019]
- [Shi et al 2020][research_shi_liu_2020]
- [Shi et al 2021][research_shi_liu_2021]
- [Shi et al 2021][research_shi_mader_2021]
- [Shi et al 2022][research_shi_wang_2022]
- [Shi et al 2023][research_shi_lan_2023]
- [Shi et al 2025][research_shi_gao_2025]
- [Shiau and Chang 1991][research_shiau_chang_1991]
- [Shieh and Chen 1998][research_shieh_chen_1998]
- [Shields and Cook 1971][research_shields_cook_1971]
- [Shimoda et al 2018][research_shimoda_nagano_2018]
- [Shinde et al 2021][research_shinde_ohol_2021]
- [Shiota and Ohmori 2015][research_shiota_ohmori_2015]
- [Shirk et al 1986][research_shirk_hertz_1986]
- [Shivaji et al 2025][research_shivaji_basavaraju_2025]
- [Shivam and Verma 2019][research_shivam_verma_2019]
- [Shmilovich and Princen 2026][research_shmilovich_princen_2026]
- [Shojae et al 2025][research_shojae_salehi_2025]
- [Shomber and Gertsen 1967][research_shomber_gertsen_1967]
- [Short 1995][research_short_1995]
- [Shrivastava 1987][research_shrivastavapc_1987]
- [Shrivastava and Mohite 2015][research_shrivastava_mohite_2015]
- [Shrivastava and Stengel 1989][research_shrivastava_stengel_1989]
- [Shrivastava et al 2020][research_shrivastava_sharma_2020]
- [Shrivastava et al 2020][research_shrivastava_tilala_2020]
- [Shtessel 2001][research_shtessel_2001]
- [Shukla and Patil 2017][research_shukla_patil_2017]
- [Shukla et al 2025][research_shukla_benyamen_2025]
- [Shyprykevich 1979][research_shyprykevichp_1979]
- [Si and Baier 2016][research_si_baier_2016]
- [Sibert 1937][research_sibert_1937]
- [Sibert 1943][research_sibert_1943]
- [Siddiqui et al 2016][research_siddiqui_elferik_2016]
- [Silton and Fresconi 2015][research_silton_fresconi_2015]
- [Silton et al 2014][research_silton_fresconi_2014]
- [Silva][research_silva]
- [Silva and Bennett 1990][research_silvawaltera_bennettrobertm_1990]
- [Simbuerger et al 2022][research_simbuerger_raveh_2022]
- [Simmonds 1971][research_simmonds_1971]
- [Simmons 2023][research_simmons_2023_b]
- [Simmons et al 2023][research_simmons_gresham_2023]
- [Simon et al 2017][research_simon_harkegard_2017]
- [Sims et al 1989][research_simsrobert_mccrossonpaul_1989]
- [Singer 1989][research_singer_1989]
- [Singh and Dwivedi 2022][research_singh_dwivedi_2022]
- [Singh and Raisinghani 1993][research_singh_raisinghani_1993]
- [Singh et al 2016][research_singh_brown_2016]
- [Singhvi and Kapania 1994][research_singhvi_kapania_1994]
- [Sinha et al 2021][research_sinha_klimmek_2021]
- [Sisson and Dogan 2026][research_sisson_dogan_2026]
- [Sitz and Vernon 1990][research_sitzjoelr_vernontoddh_1990]
- [Sivanandi et al 2025][research_sivanandi_sanjay_2025]
- [Sizlo et al 1979][research_sizlotr_bergra_1979]
- [Sleesongsom et al 2022][research_sleesongsom_kumar_2022]
- [Sleptsov and Andrianova 2021][research_sleptsov_andrianova_2021]
- [Sliwa 1980][research_sliwasm_1980]
- [Smeltzer et al 1983][research_smeltzer_durston_1983]
- [Smetana 1973][research_smetana_1973]
- [Smith 1968][research_smith_1968]
- [Smith 1978][research_smith_1978]
- [Smith 1979][research_smithjw_1979]
- [Smith 1991][research_smith_1991]
- [Smith 2025][research_smith_2025]
- [Smith and Berry 1975][research_smithjw_berrydt_1975]
- [Smith and Geddes 1979][research_smith_geddes_1979]
- [Smith and Meyer 1987][research_smith_meyer_1987]
- [Smith and Schroeder 1986][research_smithrogerse_schroederkurtc_1986]
- [Smith et al 1971][research_smith_hammer_1971]
- [Smith et al 1973][research_smith_lebacqz_1973]
- [Smith et al 2001][research_smith_komerath_2001]
- [Snyder et al 2019][research_snyder_zhao_2019]
- [Snyder et al 2022][research_snyder_zhao_2022]
- [Sobieczky 1984][research_sobieczky_1984]
- [Sodja et al 2021][research_sodja_werter_2021]
- [Sofi 2015][research_sofi_2015]
- [Sohst et al 2022][research_sohst_lobodovale_2022]
- [Soleymani and Arani 2019][research_soleymani_arani_2019]
- [Solies 1994][research_solies_1994]
- [Solies 1994][research_solies_1994_b]
- [Soltani et al 2025][research_soltani_turner_2025]
- [Somashekar et al 1987][research_somashekar_prathap_1987]
- [Son et al 2015][research_son_sa_2015]
- [Son et al 2015][research_son_sa_2015_b]
- [Soneda et al 2022][research_soneda_tsushima_2022]
- [Song and Huang 2022][research_song_huang_2022]
- [Song and Librescu 1991][research_song_librescu_1991]
- [Song and Mignolet 2018][research_song_mignolet_2018]
- [Song et al 2016][research_song_zhang_2016]
- [Soovere 1982][research_soovere_1982]
- [Southwell et al 1981][research_southwell_gunn_1981]
- [Spacht 1980][research_spacht_1980]
- [Spagnol et al 2019][research_spagnol_riche_2019]
- [Spencer and Walker 1975][research_spencer_walker_1975]
- [Spencer and Watson 1992][research_spencer_watson_1992]
- [Speyer 2003][research_speyer_2003]
- [Spillman and Ridgely 1995][research_spillman_ridgely_1995]
- [Srinathkumar 2015][research_srinathkumar_2015]
- [Srivastava 2019][research_srivastava_2019]
- [Stalford 1979][research_stalford_1979]
- [Stanbrook 1954][research_stanbrook_1954]
- [Stanewsky and Little 1971][research_stanewsky_little_1971]
- [Stanford 2016][research_stanford_2016]
- [Stanford 2016][research_stanford_2016_b]
- [Stanford 2017][research_stanford_2017]
- [Stanford 2019][research_stanford_2019]
- [Stanford and Jutte 2014][research_stanfordbretk_juttechristinev_2014]
- [Stanford and Jutte 2017][research_stanford_jutte_2017]
- [Stanford et al 2015][research_stanfordbretk_wiesemancarold_2015]
- [Stanford et al 2016][research_stanford_jutte_2016]
- [Stanton and Crain 1980][research_stanton_crain_1980]
- [Stark 1989][research_stark_1989]
- [Staroswiecki and Amani 2015][research_staroswiecki_amani_2015]
- [Stauffer and James 1978][research_staufferwa_jamesam_1978]
- [Stefanello and Gründling 2016][research_stefanello_grundling_2016]
- [Stefanovski 2022][research_stefanovski_2022]
- [Steffensen et al 2023][research_steffensen_steinert_2023]
- [Steger and Bailey 1980][research_steger_bailey_1980]
- [Stegmüller et al 2026][research_stegmuller_haybock_2026]
- [Steinberg and Page 1998][research_steinberg_page_1998]
- [Steinmetz et al 1972][research_steinmetzgg_parrishrv_1972]
- [Stephan et al 2023][research_stephan_stumpf_2023]
- [Sternberg et al 1994][research_sternberg_traven_1994]
- [Stewart and Bauer 1983][research_stewart_bauer_1983]
- [Stirling 1983][research_stirling_1983]
- [Stodieck et al 2015][research_stodieck_cooper_2015]
- [Stodieck et al 2017][research_stodieck_cooper_2017]
- [Stodieck et al 2018][research_stodieck_cooper_2018]
- [Stolarik 2007][research_stolarik_2007]
- [Stoll and Koenig 1983][research_stollf_koenigdg_1983]
- [Stollery 1992][research_stollery_1992]
- [Stottier 1995][research_stottier_1995]
- [Streit et al 2015][research_streit_wedler_2015]
- [Striz 1991][research_striz_1991]
- [Structural Aspects of Flexible 2000][research_structural_aspects_2000]
- [Structural Fundamentals 1955][research_structural_fundamentals_1955]
- [Study of advanced composite 1978][research_study_of_1978]
- [Su et al 2016][research_su_swei_2016]
- [Su et al 2025][research_su_mo_2025]
- [Subramanian et al 2022][research_subramanian_abdelsalam_2022]
- [Sudhi et al 2023][research_sudhi_radespiel_2023]
- [Sugimoto 1992][research_sugimoto_1992]
- [Sugimoto and Saito 1968][research_sugimoto_saito_1968]
- [Sugimoto and Saito 1969][research_sugimoto_saito_1969]
- [Sugino et al 2019][research_sugino_harada_2019]
- [Sugumaran 2024][research_sugumaran_2024]
- [Suh et al 2014][research_suhpeterm_conyershowardj_2014]
- [Suh et al 2015][research_suhpeterm_conyershowardjason_2015]
- [Suikat et al 1987][research_suikatreiner_donaldsonkent_1987]
- [Sulaeman et al 2017][research_sulaeman_abdullah_2017]
- [Sultan 2026][research_sultan_2026]
- [Sun 2024][research_sun_2024]
- [Sun and van Kampen 2021][research_sun_vankampen_2021]
- [Sun and Yoon 1988][research_sun_yoon_1988]
- [Sun et al 2019][research_sun_devisser_2019]
- [Sun et al 2020][research_sun_miao_2020]
- [Sun et al 2020][research_sun_shi_2020]
- [Sun et al 2020][research_sun_wang_2020]
- [Sun et al 2022][research_sun_han_2022]
- [Sun et al 2026][research_sun_chen_2026]
- [Sun et al 2026][research_sun_zhang_2026]
- [Suraj et al 2023][research_suraj_anilkumar_2023]
- [Surwase and Kumar 2025][research_surwase_kumar_2025]
- [Suryawanshi and Ghosh 2015][research_suryawanshi_ghosh_2015]
- [Sushchenko and Bezkorovainyi 2023][research_sushchenko_bezkorovainyi_2023]
- [Svoboda et al 2023][research_svoboda_hengstermovric_2023]
- [Swaim 1961][research_swaim_1961]
- [Swaim 1970][research_swaim_1970]
- [Swaim and Yen 1979][research_swaim_yen_1979]
- [Swain et al 2019][research_swain_adhikari_2019]
- [Syed et al 2022][research_syed_moshtaghzadeh_2022]
- [Synaszko et al 2015][research_synaszko_salacinski_2015]
- [Szalai 1975][research_szalaikj_1975]
- [Szalai 1976][research_szalaikj_1976]
- [Szalai et al 1976][research_szalaikj_fellemanpg_1976]
- [Szalai et al 1978][research_szalaikj_jarviscr_1978]
- [Szklarski and Głębocki 2025][research_szklarski_glebocki_2025]
- [Szollosi and Baranyi 2016][research_szollosi_baranyi_2016]
- [Szymanski et al 2025][research_szymanski_alstrom_2025]
- [Tagai et al 2016][research_tagai_nakakita_2016]
- [Tahani et al 2017][research_tahani_masdari_2017]
- [Taherinezhad and Ramirez-Serrano 2023][research_taherinezhad_ramirezserrano_2023]
- [Tahir et al 2026][research_tahir_maqsood_2026]
- [Tahraoui 1994][research_tahraoui_1994]
- [Tai et al 2023][research_tai_wang_2023]
- [Tai et al 2023][research_tai_wang_2023_b]
- [Taimoor and Aijun 2019][research_taimoor_aijun_2019]
- [Takahashi et al 2016][research_takahashi_yokozeki_2016]
- [Takahashi et al 2019][research_takahashi_boccieri_2019]
- [Takarics and Vanek 2019][research_takarics_vanek_2019]
- [Talreja and Phan 2019][research_talreja_phan_2019]
- [Tamaskani et al 2026][research_tamaskani_alfi_2026]
- [Tamboli 1956][research_tamboli_1956]
- [Tameh et al 2018][research_tameh_sawan_2018]
- [Tan 1988][research_tan_1988]
- [Tan et al 2021][research_tan_wang_2021]
- [Tang 1972][research_tang_1972]
- [Tang 1989][research_tang_1989]
- [Tang 2025][research_tang_2025]
- [Tang and Liu 2018][research_tang_liu_2018]
- [Tang et al 2015][research_tang_wu_2015]
- [Tang et al 2016][research_tang_wu_2016]
- [Tang et al 2017][research_tang_chen_2017]
- [Tang et al 2017][research_tang_wu_2017]
- [Tang et al 2018][research_tang_chen_2018]
- [Tang et al 2020][research_tang_chen_2020]
- [Tang et al 2020][research_tang_wang_2020]
- [Tang et al 2025][research_tang_tang_2025]
- [Tantaroudas and Karachalios 2026][research_tantaroudas_karachalios_2026]
- [Tanveer and Ahmad 2023][research_tanveer_ahmad_2023]
- [Tanyer et al 2016][research_tanyer_tatlicioglu_2016]
- [Tao 2025][research_tao_2025]
- [Tao et al 2016][research_tao_li_2016]
- [Targoff 1947][research_targoff_1947]
- [Targoff 1947][research_targoff_1947_b]
- [Tarnowski 2017][research_tarnowski_2017]
- [Taufik and Qasem 2025][research_taufik_qasem_2025]
- [Taylor 1959][research_taylor_1959]
- [Taylor et al 1999][research_taylor_butler_1999]
- [Teel 1999][research_teel_1999]
- [Teel 1999][research_teel_1999_b]
- [Teixeira and Cesnik 2020][research_teixeira_cesnik_2020]
- [Teixeira et al 2018][research_teixeira_araujo_2018]
- [Telionis 1995][research_telionis_1995]
- [Telionis 2001][research_telionis_2001]
- [Teper and Stapleford 1966][research_teper_stapleford_1966]
- [Terekhov 2022][research_terekhov_2022]
- [Thanusha and Sarkar 2016][research_thanusha_sarkar_2016]
- [Tharp and Zhang 1994][research_tharp_zhang_1994]
- [The viscoelastic behaviour of the principal compliance matrix of a unidirectional graphite/epoxy composite 1981][research_the_viscoelastic_1981]
- [Theerthamalai et al 2025][research_theerthamalai_mukesh_2025]
- [Theis et al 2020][research_theis_pfifer_2020]
- [Theisen et al 1973][research_theisen_scruggs_1973]
- [Theodore et al 2020][research_theodore_malpica_2020]
- [Theodorsen 1959][research_theodorsen_1959]
- [Thermal damage effects and delamination toughness of a graphite/epoxy composite 1989][research_thermal_damage_1989]
- [Thermal expansion and swelling of cured epoxy resin used in graphite/epoxy composite materials 1981][research_thermal_expansion_1981]
- [Thien and Kim 2018][research_thien_kim_2018]
- [Thinesh and Y Harmin 2018][research_c_yharmin_2018]
- [Thomas and Dowell 2025][research_thomas_dowell_2025]
- [Thomas et al 1978][research_thomas_paulson_1978]
- [Thomas et al 2020][research_thomas_hallett_2020]
- [Thompson 1992][research_thompson_1992]
- [Thu and Gavrilov 2017][research_thu_gavrilov_2017]
- [Thwapiah and Campanile 2010][research_thwapiah_campanile_2010]
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
- [Tian et al 2026][research_tian_li_2026]
- [Tian et al 2026][research_tian_wang_2026]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979]
- [Tijdeman et al 1979][research_tijdeman_vannunen_1979_b]
- [Ting et al 2014][research_tingeric_lebofskysonia_2014]
- [Ting et al 2014][research_tingeric_nguyennhan_2014]
- [Ting et al 2015][research_tingeric_daotung_2015]
- [Ting et al 2018][research_ting_chaparro_2018]
- [Ting et al 2023][research_ting_mesbahi_2023]
- [Ting et al 2026][research_ting_berg_2026]
- [Tingting et al 2018][research_tingting_aijun_2018]
- [Tipàn et al 2020][research_tipan_theodoulis_2020]
- [Tischler et al 1991][research_tischlermarkb_fletcherjayw_1991]
- [Toader 1987][research_toader_1987]
- [Toffol 2024][research_toffol_2024]
- [Toffol and Ricci 2023][research_toffol_ricci_2023]
- [Tohidi et al 2016][research_tohidi_khakisedigh_2016]
- [Tokunaga et al 2015][research_tokunaga_masui_2015]
- [Toledano and Murakami 1987][research_toledano_murakami_1987]
- [Toloei and Ghaderi 2026][research_toloei_ghaderi_2026]
- [Tomlinson 1973][research_tomlinson_1973]
- [Tong et al 2025][research_tong_du_2025]
- [Tormalm et al 2018][research_tormalm_leroy_2018]
- [Torregrosa et al 2022][research_torregrosa_gil_2022]
- [Torsional stiffness of plastic tubes reinforced with glass fibres 1972][research_torsional_stiffness_1972]
- [Townsend et al 2018][research_townsend_picelli_2018]
- [Trabocco 1980][research_trabocco_1980]
- [Tran and Nguyen 2022][research_tran_nguyen_2022]
- [Tran et al 2017][research_tran_sakamoto_2017]
- [Traub 2019][research_traub_2019]
- [Traven and Whitley 1995][research_traven_whitley_1995]
- [Tribuno et al 1976][research_tribuno_klein_1976]
- [Trindade Nascimento and Cunha 2019][research_trindadenascimento_cunha_2019]
- [Triplett 1972][research_triplett_1972]
- [Triplett 1980][research_triplett_1980]
- [Triplett 1980][research_triplett_1980_b]
- [Triplett et al 1971][research_triplett_burkhart_1971]
- [Triplett et al 1973][research_triplett_kappus_1973]
- [Trippensee 1991][research_trippensee_1991]
- [Trippensee and Lux 1987][research_trippenseegarya_luxdavidp_1987]
- [Trippensee and Lux 1988][research_trippenseegarya_luxdavidp_1988]
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
- [Tu 1991][research_tueugenel_1991]
- [Tu 1992][research_tu_1992]
- [Tu 1992][research_tueugenel_1992]
- [Tu 1992][research_tueugenel_1992_b]
- [Tu 1994][research_tu_1994]
- [Tu 1994][research_tu_1994_b]
- [Tu and VanDalsem 1996][research_tueugenel_vandalsemwilliamr_1996]
- [Tu et al 2026][research_tu_lu_2026]
- [Tungikar and Rao 1994][research_tungikar_rao_1994]
- [Turner 1982][research_turner_1982]
- [Turner 1982][research_turner_1982_b]
- [Turner and Hoy 1976][research_turnermj_hoyjm_1976]
- [Twisdale and Kirsten 1984][research_twisdale_kirsten_1984]
- [UAV control with active disturbance suppression for the safety landing on an aircraft carrier 2023][research_uav_control_2023]
- [Ulry et al 1976][research_ulry_gehring_1976]
- [Unal 2021][research_unal_2021]
- [Unal 2021][research_unal_2021_b]
- [Underwood et al 2003][research_underwoodpamelaj_owenslewisr_2003]
- [Urso et al 2026][research_urso_giunta_2026]
- [Ursu et al 2018][research_ursu_ionguta_2018]
- [Uzun 2024][research_uzun_2024]
- [Uzun and Oktay 2023][research_uzun_oktay_2023]
- [Uzun et al 2023][research_uzun_bilgic_2023]
- [Valasek and Downing 1995][research_valasek_downing_1995]
- [Valsangkar et al 1982][research_valsangkar_britto_1982]
- [Van Baelen et al 2020][research_vanbaelen_ellerbroek_2020]
- [van Dam et al 1981][research_vandam_holmes_1981]
- [Van Den Berg et al 1975][research_vandenberg_elsenaar_1975]
- [van den Brandt and de Visser 2018][research_vandenbrandt_devisser_2018]
- [van den Kieboom and Elham 2017][research_vandenkieboom_elham_2017]
- [Van Dommelen 1995][research_vandommelen_1995]
- [van Dooren and Bisagni 2024][research_vandooren_bisagni_2024]
- [Van Doren 1955][research_vandoren_1955]
- [Van Tuyl 1988][research_vantuyl_1988]
- [van Waarde 2022][research_vanwaarde_2022]
- [Van Zyl 2001][research_vanzyl_2001]
- [van Zyl and Maserumule 2001][research_vanzyl_maserumule_2001]
- [Varun and Dwivedi 2022][research_varun_dwivedi_2022]
- [Varun et al 2022][research_varun_mondal_2022]
- [Vedeneev 2020][research_vedeneev_2020]
- [Veerman et al 2013][research_veerman_kannemans_2013]
- [Veley et al 2008][research_veley_khot_2008]
- [Velkova 2017][research_velkova_2017]
- [Venkataraman and Seiler 2019][research_venkataraman_seiler_2019]
- [Vepa and Kwon 2021][research_vepa_kwon_2021]
- [Verhaegen and Żbikowski 2017][research_verhaegen_zbikowski_2017]
- [Verma et al 2024][research_verma_cidmontoya_2024]
- [Verma et al 2025][research_verma_cidmontoya_2025]
- [Vermiglio 2017][research_vermiglio_2017]
- [Verri et al 2025][research_verri_desilvabussamra_2025]
- [Vertonghen et al 2026][research_vertonghen_irisarri_2026]
- [Vescovini and Dozio 2016][research_vescovini_dozio_2016]
- [Viglietti et al 2019][research_viglietti_zappino_2019]
- [Viken et al 2022][research_sallyaviken_craigahunter_2022]
- [Vile et al 2020][research_vile_alwi_2020]
- [Vilela and Donadon 2025][research_vilela_donadon_2025]
- [Vinje and Miller 1973][research_vinje_miller_1973]
- [Viola et al 2020][research_viola_oziablo_2020]
- [Vitushkin V.V. 2025][research_vitushkinvv_2025]
- [Vlahostergios et al 2018][research_vlahostergios_komnos_2018]
- [Volpe et al 2026][research_volpe_salcuni_2026]
- [Voracek 1990][research_voracek_1990]
- [Voracek and Clarke 1991][research_voracekdavidf_clarkerobert_1991]
- [Voracek and Clarke 1994][research_voracek_clarke_1994]
- [Voting software for fault-tolerant aircraft flight control systems 1993][research_voting_software_1993]
- [Voulgaris 1994][research_voulgaris_1994]
- [Vukelich et al 1988][research_vukelich_stoy_1988_b]
- [Vukobratović and Stojić 1985][research_vukobratovic_stojic_1985]
- [Wada et al 2020][research_wada_tamayama_2020]
- [Wagg 2022][research_wagg_2022]
- [Waggoner and Bates 1989][research_waggonereg_batesbl_1989]
- [Waggoner et al 1986][research_waggonereg_jennettla_1986]
- [Wahler et al 2025][research_wahler_ma_2025]
- [Waitman and Marcos 2019][research_waitman_marcos_2019]
- [Waitman and Marcos 2020][research_waitman_marcos_2020]
- [Wakimoto et al 2021][research_wakimoto_chiba_2021]
- [Walchli 1994][research_walchlilawrencea_1994]
- [Walchli et al 1992][research_walchli_guyton_1992]
- [Walker 1976][research_walkersa_1976]
- [Walker and Claudio 2024][research_walker_claudio_2024]
- [Walker and Hall 1968][research_walker_hall_1968]
- [Walker and Kaufman 1977][research_walker_kaufman_1977]
- [Walker et al 1997][research_walkerth_minguetpj_1997]
- [Walsh 1993][research_walshkevinr_1993]
- [Wan et al 2003][research_wan_yang_2003]
- [Wang 1996][research_wangjohnt_1996]
- [Wang 2019][research_wang_2019]
- [Wang 2021][research_wang_2021]
- [Wang 2024][research_wang_2024]
- [Wang 2024][research_wang_2024_b]
- [Wang 2026][research_wang_2026]
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
- [Wang et al 1996][research_wangjohnt_jegleydawnc_1996]
- [Wang et al 2006][research_wang_zhan_2006]
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
- [Wang et al 2024][research_wang_liu_2024]
- [Wang et al 2024][research_wang_song_2024]
- [Wang et al 2024][research_wang_sun_2024]
- [Wang et al 2024][research_wang_zhou_2024]
- [Wang et al 2025][research_wang_feng_2025]
- [Wang et al 2025][research_wang_ji_2025]
- [Wang et al 2025][research_wang_li_2025]
- [Wang et al 2025][research_wang_li_2025_b]
- [Wang et al 2025][research_wang_liuxu_2025]
- [Wang et al 2025][research_wang_luo_2025]
- [Wang et al 2025][research_wang_luo_2025_b]
- [Wang et al 2025][research_wang_luo_2025_c]
- [Wang et al 2025][research_wang_sun_2025]
- [Wang et al 2025][research_wang_tian_2025]
- [Wang et al 2025][research_wang_wang_2025]
- [Wang et al 2025][research_wang_wang_2025_b]
- [Wang et al 2026][research_wang_hu_2026]
- [Wang et al 2026][research_wang_li_2026]
- [Wang et al 2026][research_wang_liu_2026]
- [Wang et al 2026][research_wang_wei_2026]
- [Wang et al 2026][research_wang_weng_2026]
- [Wang et al 2026][research_wang_yi_2026]
- [Wansaseub et al 2020][research_wansaseub_sleesongsom_2020]
- [Wansasueb et al 2023][research_wansasueb_panagant_2023]
- [Wardlaw et al 1975][research_wardlaw_andrewb_1975]
- [Wasson and Mehus 1967][research_wasson_mehus_1967]
- [Wauters 2021][research_wauters_2021]
- [Wauters 2022][research_wauters_2022]
- [Weatherill and Zartarian 1958][research_weatherill_zartarian_1958]
- [Webb and Rogers 2021][research_webb_rogers_2021]
- [Webb et al 1988][research_webblannied_mccainwilliame_1988]
- [Weed et al 1983][research_weed_carlson_1983]
- [Wei and Du 2019][research_wei_du_2019]
- [Wei and Freris 2024][research_wei_freris_2024]
- [Wei et al 2017][research_wei_chen_2017]
- [Wei et al 2019][research_wei_zhan_2019]
- [Wei et al 2020][research_wei_xu_2020]
- [Wei et al 2024][research_wei_meng_2024]
- [Weidemann and Leondes 1979][research_weidemann_leondes_1979]
- [Weihs and Katz 1986][research_weihs_katz_1986]
- [Weinert and Meyer 1984][research_weinert_meyer_1984]
- [Weiser et al 2020][research_weiser_ossmann_2020]
- [Weissenberger 1969][research_weissenberger_1969]
- [Weisshaar 1977][research_weisshaar_1977]
- [Weisshaar 1978][research_weisshaar_1978]
- [Weisshaar 1979][research_weisshaar_1979]
- [Weisshaar 1980][research_weisshaar_1980]
- [Weisshaar 1981][research_weisshaar_1981]
- [Weisshaar 1983][research_weisshaarta_1983]
- [Weisshaar 1985][research_weisshaar_1985]
- [Weisshaar and Ehlers 1990][research_weisshaarta_ehlerssm_1990]
- [Weisshaar and Ehlers 1992][research_weisshaarterrencea_ehlersstevenm_1992]
- [Weisshaar and Ryan 1986][research_weisshaar_ryan_1986]
- [Weisshaar and Zeiler 1982][research_weisshaarta_zeilerta_1982]
- [Weisshaar and Zeiler 1983][research_weisshaar_zeiler_1983]
- [Well and Berger 1982][research_well_berger_1982]
- [Wells 2002][research_wells_2002]
- [Wen et al 2023][research_wen_song_2023]
- [Werdes 1953][research_werdes_1953]
- [Werter and De Breuker 2016][research_werter_debreuker_2016]
- [Westin et al 2023][research_westin_balthazar_2023]
- [Wheatcroft et al 2025][research_wheatcroft_groh_2025]
- [Wheatcroft et al 2025][research_wheatcroft_mahadik_2025]
- [Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]
- [Whitbeck et al 1982][research_whitbeck_smith_1982]
- [White and Hartl 2025][research_white_hartl_2025]
- [White et al 1961][research_white_richardp_1961]
- [White et al 2005][research_white_geubelle_2005]
- [White et al 2015][research_whiteedwardv_kapaniarakeshk_2015]
- [White et al 2017][research_white_mongru_2017]
- [White et al 2021][research_white_padfield_2021]
- [Whitehead et al 1992][research_whiteheadrs_foremancr_1992]
- [Whitlow et al 1991][research_whitlowwoodrowjr_bennettrobertm_1991]
- [Whitworth 1987][research_whitworth_1987]
- [Wickman 1953][research_wickman_1953]
- [Wie and Byun 1989][research_wie_byun_1989]
- [Wiggenraad and Bauld 1993][research_wiggenraadjfm_bauldnrjr_1993]
- [Wildermuth et al 1974][research_wildermuth_rothammer_1974]
- [Wildermuth et al 1974][research_wildermuth_rothammer_1974_b]
- [Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]
- [Williams 1952][research_williams_1952]
- [Williams 1980][research_williams_1980]
- [Willsky 1984][research_willsky_1984]
- [Willsky and Verghese 1984][research_willsky_verghese_1984]
- [Willsky and Verghese 1985][research_willsky_verghese_1985]
- [Wilson and Riccardi 2022][research_wilson_riccardi_2022]
- [Wilson et al 1993][research_wilson_riley_1993]
- [Wilson et al 1994][research_wilsondavidj_citurskevind_1994]
- [Wilson et al 2024][research_wilson_champneys_2024]
- [Wing Buffeting Control at Transonic Flight Velocities with the Use of Ejector-Type Pulse Thermal Actuators 2018][research_wing_buffeting_2018]
- [Winny 1950][research_winny_1950]
- [Wise et al 1999][research_wise_sedwick_1999]
- [Wissler et al 1987][research_wissler_gilliam_1987]
- [Witte et al 2003][research_witte_monson_2003]
- [Wolfe 1967][research_wolfe_1967]
- [Wollner 1972][research_wollner_1972]
- [Wood and Livingston 1971][research_wood_livingston_1971]
- [Wood and Miller 1985][research_woodrm_millerds_1985]
- [Wood et al 2019][research_wood_araujoestrada_2019]
- [Woodcock and George 1976][research_woodcockrj_georgefl_1976]
- [Woods et al 1989][research_woodsjessicaa_gilbertmichaelg_1989]
- [Woods et al 1990][research_woods_gilbert_1990]
- [Woods et al 2015][research_woods_dayyani_2015]
- [Wooldridge 1960][research_wooldridge_1960]
- [Wrestler and Clifton G. 1965][research_wrestler_cliftong_1965]
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
- [Wu et al 2022][research_wu_zuo_2022]
- [Wu et al 2024][research_wu_ye_2024]
- [Wu et al 2025][research_wu_fu_2025]
- [Wu et al 2025][research_wu_wang_2025]
- [Wunderlich 2015][research_wunderlich_2015]
- [Wunderlich and Dähne 2017][research_wunderlich_dahne_2017_b]
- [Wunderlich et al 2017][research_wunderlich_dahne_2017]
- [Wunderlich et al 2021][research_wunderlich_dahne_2021]
- [Wunderlich et al 2022][research_wunderlich_dahne_2022]
- [X-29 Experiment in Flight 1991][research_x_29_experiment_1991]
- [X-29 Research Aircraft 1991][research_x_29_research_1991]
- [Xia and Chen 2015][research_xia_chen_2015]
- [Xia et al 2016][research_xia_li_2016]
- [Xia et al 2026][research_xia_li_2026]
- [Xiang and Liu 2024][research_xiang_liu_2024]
- [Xiang and Wang 2023][research_xiang_wang_2023]
- [Xiang et al 2018][research_xiang_liu_2018]
- [Xiao and Dong 2019][research_xiao_dong_2019]
- [Xiao and Harrison 2021][research_xiao_harrison_2021]
- [Xiao and Liu 2018][research_xiao_liu_2018]
- [Xie and Zhao 2016][research_xie_zhao_2016]
- [Xie et al 2016][research_xie_liu_2016]
- [Xie et al 2017][research_xie_meng_2017]
- [Xie et al 2021][research_xie_li_2021]
- [Xie et al 2025][research_xie_zhang_2025]
- [Xijuan et al 2016][research_xijuan_qiang_2016]
- [Xinbing et al 2020][research_xinbing_wen_2020]
- [Xiong et al 2025][research_xiong_xu_2025]
- [Xiong et al 2026][research_xiong_tang_2026]
- [Xu and Feng 2025][research_xu_feng_2025]
- [Xu and Wang 2016][research_xu_wang_2016]
- [Xu and Xia 2016][research_xu_xia_2016]
- [Xu and Zha 2021][research_xu_zha_2021]
- [Xu et al 2015][research_xu_fan_2015]
- [Xu et al 2015][research_xu_gao_2015]
- [Xu et al 2015][research_xu_guo_2015]
- [Xu et al 2018][research_xu_zhang_2018]
- [Xu et al 2019][research_xu_han_2019]
- [Xu et al 2019][research_xu_saleh_2019]
- [Xu et al 2019][research_xu_tan_2019]
- [Xu et al 2020][research_xu_zhang_2020]
- [Xu et al 2024][research_xu_tian_2024]
- [Xu et al 2026][research_xu_liu_2026]
- [Xu et al 2026][research_xu_zhang_2026]
- [Xue and Yao 2020][research_xue_yao_2020]
- [Xue et al 2019][research_xue_ye_2019]
- [Xue et al 2021][research_xue_yunsong_2021]
- [Yagil et al 2018][research_yagil_raveh_2018]
- [Yahagi 1971][research_yahagi_1971]
- [Yalvaç et al 1991][research_yalvac_yats_1991]
- [Yamamoto 1992][research_yamamoto_1992]
- [Yamasaki and Epureanu 2017][research_yamasaki_epureanu_2017]
- [Yamasaki and Gotoh 1971][research_yamasaki_gotoh_1971]
- [Yan et al 2019][research_yan_li_2019]
- [Yan et al 2025][research_yan_han_2025]
- [Yang 2024][research_yang_2024]
- [Yang and Gao 2020][research_yang_gao_2020]
- [Yang and Liu 1976][research_yang_liu_1976]
- [Yang and Przekwas 1993][research_yang_przekwas_1993]
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
- [Yang et al 2023][research_yang_zhang_2023]
- [Yang et al 2024][research_yang_fu_2024]
- [Yang et al 2024][research_yang_xiao_2024]
- [Yang et al 2024][research_yang_xu_2024]
- [Yang et al 2025][research_yang_wang_2025]
- [Yang et al 2025][research_yang_wu_2025]
- [Yang et al 2026][research_yang_li_2026]
- [Yang et al 2026][research_yang_tang_2026]
- [Yang et al 2026][research_yang_wang_2026]
- [Yang et al 2026][research_yang_zhang_2026]
- [Yao 2018][research_yao_2018]
- [Yaseen and Bayart 2018][research_yaseen_bayart_2018]
- [Yasue 2020][research_yasue_2020]
- [Yates 1966][research_yates_1966]
- [Yates and Chu 1987][research_yatesecarsonjr_chulichuan_1987]
- [Yates et al 1981][research_yatesecjr_wynneec_1981]
- [Yates et al 1982][research_yates_wynne_1982]
- [Yates et al 1983][research_yates_wynne_1983]
- [Ye et al 2015][research_ye_chen_2015]
- [Ye et al 2024][research_ye_yang_2024]
- [Yeh 1988][research_yeh_1988]
- [Yeh 1988][research_yeh_1988_b]
- [Yeh and Yeh 1989][research_yeh_yeh_1989]
- [Yeo et al 2015][research_yeo_atkins_2015]
- [Yi et al 2017][research_yi_an_2017]
- [Yildiz and Kolmanovsky 2010][research_yildizyildiray_kolmanovskyilyav_2010]
- [Yildiz et al 2011][research_yildizyidiray_kolmanovskyilyav_2011]
- [Yin and Wang 2017][research_yin_wang_2017]
- [Yin et al 2019][research_yin_chu_2019]
- [Yin et al 2025][research_yin_huang_2025]
- [Ying et al 2021][research_ying_liqiang_2021]
- [Yingsong et al 2015][research_yingsong_zhichun_2015]
- [Yip and Paulson 1977][research_yiplp_paulsonjwjr_1977]
- [Yonekura and Suzuki 2021][research_yonekura_suzuki_2021]
- [Yoo 2017][research_yoo_2017]
- [Yoo et al 2021][research_yoo_jang_2021]
- [Yoo et al 2023][research_yoo_jeong_2023]
- [York and Williams 1995][research_york_williams_1995]
- [You 2020][research_you_2020]
- [You et al 2019][research_you_yasaee_2019]
- [You et al 2020][research_you_kim_2020]
- [You et al 2022][research_you_lei_2022]
- [Young et al 2018][research_young_garg_2018]
- [Yu 1987][research_yu_1987]
- [Yu 2018][research_yu_2018]
- [Yu and Yu 2026][research_yu_yu_2026]
- [Yu et al 2016][research_yu_zhang_2016]
- [Yu et al 2017][research_yu_fang_2017]
- [Yu et al 2017][research_yu_wang_2017]
- [Yu et al 2018][research_yu_lyu_2018]
- [Yu et al 2023][research_yu_zhang_2023]
- [Yu et al 2024][research_yu_zhou_2024]
- [Yu et al 2025][research_yu_he_2025]
- [Yuan and Li 2019][research_yuan_li_2019]
- [Yuan and Reeder 2001][research_yuanfg_reederjamesr_2001]
- [Yuan and Zhou 2024][research_yuan_zhou_2024]
- [Yuan et al 2018][research_yuan_huo_2018]
- [Yuan et al 2022][research_yuan_thomson_2022]
- [Yuan et al 2024][research_yuan_wang_2024]
- [Yue and Zhao 2020][research_yue_zhao_2020]
- [Yue et al 2017][research_yue_zhang_2017]
- [Yue et al 2021][research_yue_khodaei_2021]
- [Yuksek and Inalhan 2020][research_yuksek_inalhan_2020]
- [Yunker et al 2024][research_yunker_lake_2024]
- [Yurtsever et al 2026][research_yurtsever_sahin_2026]
- [Yutuk et al 2021][research_yutuk_tikenogullari_2021]
- [Zadvornyak and Martynovich 1983][research_zadvornyak_martynovich_1983]
- [Zakharov et al 2015][research_zakharov_zattoni_2015]
- [Zanoni et al 2022][research_zanoni_gerosa_2022]
- [Zauner and Sandham 2020][research_zauner_sandham_2020]
- [Zauner et al 2023][research_zauner_moise_2023]
- [Zaw and Baranovski 2026][research_zaw_baranovski_2026]
- [Zaytseva et al 2021][research_zaytseva_kuznetsov_2021]
- [Zeiler 1999][research_zeiler_1999]
- [Zeleke et al 2023][research_zeleke_asfaw_2023]
- [Zelenkov 2018][research_zelenkov_2018]
- [Zha et al 2026][research_zha_qiao_2026]
- [Zhai et al 2020][research_zhai_li_2020]
- [Zhang 2023][research_zhang_2023]
- [Zhang and He 2026][research_zhang_he_2026]
- [Zhang and Ran 2023][research_zhang_ran_2023]
- [Zhang and Rizzi 2017][research_zhang_rizzi_2017]
- [Zhang and Wang 2019][research_zhang_wang_2019]
- [Zhang and Zhao 2023][research_zhang_zhao_2023]
- [Zhang and Zhao 2023][research_zhang_zhao_2023_b]
- [Zhang et al 2013][research_zhang_yu_2013]
- [Zhang et al 2015][research_zhang_fang_2015]
- [Zhang et al 2015][research_zhang_marzocca_2015]
- [Zhang et al 2015][research_zhang_wang_2015]
- [Zhang et al 2015][research_zhang_zhou_2015]
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
- [Zhang et al 2021][research_zhang_shaw_2021]
- [Zhang et al 2021][research_zhang_xie_2021]
- [Zhang et al 2021][research_zhang_yang_2021]
- [Zhang et al 2022][research_zhang_deng_2022]
- [Zhang et al 2022][research_zhang_ji_2022]
- [Zhang et al 2022][research_zhang_wang_2022_b]
- [Zhang et al 2023][research_zhang_zhang_2023]
- [Zhang et al 2024][research_zhang_qiu_2024]
- [Zhang et al 2024][research_zhang_zhou_2024]
- [Zhang et al 2024][research_zhang_zhou_2024_b]
- [Zhang et al 2025][research_zhang_bai_2025]
- [Zhang et al 2025][research_zhang_song_2025]
- [Zhang et al 2025][research_zhang_yang_2025]
- [Zhang et al 2026][research_zhang_dai_2026]
- [Zhang et al 2026][research_zhang_deng_2026]
- [Zhang et al 2026][research_zhang_li_2026]
- [Zhang et al 2026][research_zhang_wang_2026]
- [Zhang et al 2026][research_zhang_zhao_2026]
- [Zhao and Cheng 2019][research_zhao_cheng_2019]
- [Zhao and Li 2019][research_zhao_li_2019]
- [Zhao and Zhou 2024][research_zhao_zhou_2024]
- [Zhao et al 2016][research_zhao_yue_2016]
- [Zhao et al 2016][research_zhao_zhang_2016]
- [Zhao et al 2022][research_zhao_ji_2022]
- [Zhao et al 2023][research_zhao_yang_2023]
- [Zhao et al 2024][research_zhao_lu_2024]
- [Zhao et al 2024][research_zhao_xu_2024]
- [Zhao et al 2024][research_zhao_zhang_2024]
- [Zhao et al 2026][research_zhao_liu_2026]
- [Zhao et al 2026][research_zhao_liu_2026_b]
- [Zheng et al 2024][research_zheng_pontillo_2024]
- [Zheng et al 2026][research_zheng_dai_2026]
- [Zhijie et al 2025][research_zhijie_taiyu_2025]
- [Zhiqiang et al 2016][research_zhiqiang_xiaozhe_2016]
- [Zhirabok et al 2024][research_zhirabok_filaretov_2024]
- [Zhong et al 2025][research_zhong_ying_2025]
- [Zhong et al 2026][research_zhong_wang_2026]
- [Zhou and Huang 2021][research_zhou_huang_2021]
- [Zhou and Huang 2021][research_zhou_huang_2021_b]
- [Zhou et al 1989][research_zhou_ye_1989]
- [Zhou et al 2017][research_zhou_chen_2017]
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
- [Zhu and Duan 2015][research_zhu_duan_2015]
- [Zhu et al 2017][research_zhu_du_2017]
- [Zhu et al 2017][research_zhu_wang_2017]
- [Zhu et al 2019][research_zhu_li_2019]
- [Zhu et al 2022][research_zhu_shi_2022]
- [Zhu et al 2024][research_zhu_zhang_2024]
- [Zhu et al 2025][research_zhu_zhou_2025]
- [Zhuang et al 2021][research_zhuang_yang_2021]
- [Ziakos et al 2025][research_ziakos_kilimtzidis_2025]
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
- [Zuhri 2025][research_zuhri_2025]
- [Zuo et al 2015][research_zuo_chen_2015]
- [Zuo et al 2016][research_zuo_min_2016]
- [Zvonarev and Leont’ev 2025][research_zvonarev_leontev_2025]
- [Çabuk 2026][research_cabuk_2026]
- [Özdemir 2021][research_ozdemir_2021]
- [Özkan 2020][research_ozkan_2020]
- [Şahin and Yaman 2018][research_sahin_yaman_2018]
- [Şahin and Yaman 2018][research_sahin_yaman_2018_b]
- [Ženíšek 1973][research_zenisek_1973]
- [Калиновский 2016][research_anon_2016]
- [Комаров and Зінченко 2019][research___2019]
- [Морозов 2015][research_anon_2015]

[research_044_finite_1994]: https://doi.org/10.1016/0967-0661(94)90059-0
[research_057_h_1994]: https://doi.org/10.1016/0967-0661(94)90072-8
[research_130_sampled_data_1994]: https://doi.org/10.1016/0967-0661(94)90919-9
[research_185_a_1994]: https://doi.org/10.1016/0967-0661(94)90974-1
[research_214_application_1994]: https://doi.org/10.1016/0967-0661(94)91003-0
[research___2019]: https://doi.org/10.20535/0203-3771372019186954
[research_a_feasibility_2019]: https://doi.org/10.21152/1750-9548.13.4.339
[research_a_generalization_2020]: https://doi.org/10.5829/ije.2020.33.11b.28
[research_a_hybrid_1995]: https://doi.org/10.1016/0967-0661(95)90150-7
[research_a_spreadsheet_2018]: https://doi.org/10.20508/ijrer.v8i4.8480.g7550
[research_a_study_1973]: https://ntrs.nasa.gov/citations/19730009309
[research_aamir_abbasi_2026]: https://doi.org/10.2514/1.c038958
[research_abbas_morgenthal_2016]: https://doi.org/10.1016/j.probengmech.2015.12.007
[research_abc_2023]: https://doi.org/10.61653/joast.v70i01.2018.347
[research_abdulhuq_beebim_2015]: https://doi.org/10.70729/ijser15423
[research_abdulkaiyoom_yildirim_2025]: https://doi.org/10.2514/1.c037365
[research_abdullah_akbar_2019]: https://doi.org/10.1016/j.compstruct.2019.111414
[research_abdulrashid_syedmohddardin_2025]: https://doi.org/10.58247/jdset-2025-0802-20
[research_abed_alhamadani_2024]: https://doi.org/10.18280/mmep.111029
[research_abele_ruger_1973]: https://doi.org/10.21236/ad0766892
[research_abele_sanlorenzo_1975]: https://doi.org/10.21236/ada013139
[research_abeli_ruhlincl_1966]: https://ntrs.nasa.gov/citations/19660021918
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
[research_acquatellab_vanekeren_2017]: https://doi.org/10.1016/j.ifacol.2017.08.1265
[research_adams_hatch_1971]: https://doi.org/10.2514/3.59103
[research_adan_sheinman_1988]: https://doi.org/10.1016/0045-7949(88)90296-9
[research_adegbindin_love_2016]: https://doi.org/10.2514/6.2016-3361
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
[research_aharrahralphc_2007]: https://ntrs.nasa.gov/citations/20100011189
[research_ahmadi_farsadi_2024]: https://doi.org/10.1016/j.ast.2023.108849
[research_ahmadi_farsadi_2024_b]: https://doi.org/10.1016/j.ast.2024.109023
[research_ahmadian_alitalebi_2025]: https://doi.org/10.1002/acs.3957
[research_ahmadidastgerdi_asadi_2022]: https://doi.org/10.55212/ijaa.1033224
[research_ahmed_chen_2021]: https://doi.org/10.1108/aeat-11-2020-0277
[research_ahmed_elbanna_2025]: https://doi.org/10.1142/s2301385026500366
[research_aidala_1985]: https://doi.org/10.21236/ada171075
[research_airforceflighttestcenteredwardsafbca_1974]: https://doi.org/10.21236/ada011561
[research_airforceflighttestcenteredwardsafbca_1974_b]: https://doi.org/10.21236/ada011562
[research_airforcetestpilotschooledwardsafbca_1967]: https://doi.org/10.21236/ada320224
[research_airforcetestpilotschooledwardsafbca_1967_b]: https://doi.org/10.21236/ada320209
[research_airforcetestpilotschooledwardsafbca_1969]: https://doi.org/10.21236/ada319985
[research_airforcetestpilotschooledwardsafbca_1981]: https://doi.org/10.21236/ada320347
[research_airforcetestpilotschooledwardsafbca_1988]: https://doi.org/10.21236/ada319979
[research_airforcetestpilotschooledwardsafbca_1988_c]: https://doi.org/10.21236/ada319984
[research_airforcetestpilotschooledwardsafbca_1988_d]: https://doi.org/10.21236/ada319975
[research_airforcetestpilotschooledwardsafbca_1989]: https://doi.org/10.21236/ada319980
[research_airforcetestpilotschooledwardsafbca_1990]: https://doi.org/10.21236/ada319976
[research_airforcetestpilotschooledwardsafbca_1990_b]: https://doi.org/10.21236/ada319978
[research_airforcetestpilotschooledwardsafbca_1990_d]: https://doi.org/10.21236/ada320062
[research_airforcetestpilotschooledwardsafbca_1990_e]: https://doi.org/10.21236/ada319977
[research_airforcetestpilotschooledwardsafbca_1991]: https://doi.org/10.21236/ada319981
[research_airforcetestpilotschooledwardsafbca_1991_b]: https://doi.org/10.21236/ada319972
[research_airforcetestpilotschooledwardsafbca_1993]: https://doi.org/10.21236/ada320063
[research_ajaj_parancheerivilakkathil_2021]: https://doi.org/10.1016/j.paerosci.2020.100682
[research_ajel_humaidi_2021]: https://doi.org/10.3390/act10070162
[research_akbari_galeani_2025]: https://doi.org/10.1109/lcsys.2025.3633369
[research_aker_alukonis_1976]: https://doi.org/10.21236/ada028416
[research_alag_kaufman_1975]: https://doi.org/10.2514/3.59859
[research_alam_hromcik_2015]: https://doi.org/10.1016/j.ast.2014.12.020
[research_alcaina_cuenca_2019]: https://doi.org/10.1016/j.ins.2019.01.059
[research_aleisaac_ragab_2023]: https://doi.org/10.3390/s23125561
[research_alexander_1991]: https://doi.org/10.21236/ada240263
[research_alexander_tzeng_1996]: https://doi.org/10.21236/ada306454
[research_alhajahmad_mittelstedt_2021]: https://doi.org/10.1016/j.compstruct.2020.113271
[research_alhussein_haldar_2015]: https://doi.org/10.1002/stc.1764
[research_ali_chen_2026]: https://doi.org/10.1115/1.4071137
[research_aliahmadi_1988]: https://ntrs.nasa.gov/citations/19880010912
[research_alisyedfirasat_1997]: https://ntrs.nasa.gov/citations/19970026582
[research_alizadeh_ebrahimi_2020]: https://doi.org/10.1142/s0219455420500820
[research_aljaburi_feszty_2019]: https://doi.org/10.1016/j.cja.2019.05.009
[research_allen_bradley_1983]: https://doi.org/10.21236/ada134059
[research_allen_bradley_1984]: https://doi.org/10.21236/ada150802
[research_allisondenniso_dagenhartjray_1987]: https://ntrs.nasa.gov/citations/19890009895
[research_almosnino_1985]: https://doi.org/10.2514/3.9057
[research_alsaidi_joe_2019]: https://doi.org/10.3390/aerospace6080090
[research_alsaidi_joe_2019_b]: https://doi.org/10.3390/aerospace6070079
[research_altunkaya_ozkol_2025]: https://doi.org/10.2514/1.g008752
[research_alyanak_pendleton_2017]: https://doi.org/10.2514/1.c033040
[research_an_anal_1974]: https://doi.org/10.1016/0148-9062(74)90690-1
[research_an_guo_2020]: https://doi.org/10.1007/s11071-020-05531-8
[research_an_khoo_2017]: https://doi.org/10.1016/j.compstruct.2017.07.042
[research_an_zhang_2026]: https://doi.org/10.1016/j.ast.2025.111209
[research_anderson_1970]: https://doi.org/10.21236/ad0710590
[research_anderson_1985]: https://doi.org/10.2514/3.45218
[research_anderson_berger_1973]: https://doi.org/10.2514/3.60204
[research_anderson_toivanen_1970]: https://doi.org/10.21236/ad0706001
[research_andersonca_1976]: https://ntrs.nasa.gov/citations/19760024050
[research_ando_yashiro_1976]: https://doi.org/10.2514/3.48148
[research_andresperez_gonzalezjuarez_2016]: https://doi.org/10.1080/0305215x.2016.1165568
[research_ang_leo_2024]: https://doi.org/10.1016/j.ast.2023.108798
[research_ang_ng_2026]: https://doi.org/10.2514/1.j065873
[research_anikin_animitsa_2015]: https://doi.org/10.1615/tsagiscij.2015014083
[research_annadata_endesfelder_2024]: https://doi.org/10.1088/2053-1591/ad8397
[research_anon_2015]: https://doi.org/10.18372/2073-4751.2.8948
[research_anon_2016]: https://doi.org/10.18698/2541-8009-2016-1-10
[research_ansari_zucco_2023]: https://doi.org/10.1016/j.compstruct.2023.116691
[research_ansellgs_loewyrg_1982]: https://ntrs.nasa.gov/citations/19830009326
[research_antonakis_2025]: https://doi.org/10.1016/j.ast.2025.110020
[research_antonakis_2025_b]: https://doi.org/10.1007/s13272-025-00815-4
[research_antonakis_biannic_2024]: https://doi.org/10.2514/1.c037707
[research_application_analysis_2022]: https://doi.org/10.47939/et.v3i5(02).13
[research_application_status_2023]: https://doi.org/10.3901/jme.2023.19.001
[research_ardemamd_williamslj_1972]: https://ntrs.nasa.gov/citations/19720018366
[research_arena_lacarbonara_2012]: https://doi.org/10.1007/s11071-012-0636-3
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
[research_asadikhanouki_javadiaghdam_2019]: https://doi.org/10.1016/j.tws.2019.01.001
[research_ascani_1974]: https://doi.org/10.21236/ada002850
[research_asgari_kouchakzadeh_2016]: https://doi.org/10.1016/j.compstruct.2016.02.015
[research_ashill_1970]: https://doi.org/10.1017/s0001925900005400
[research_ashkenas_1984]: https://doi.org/10.2514/3.44963
[research_ashkenasirvingl_klydedavidh_1989]: https://ntrs.nasa.gov/citations/19890011628
[research_ashton_1970]: https://doi.org/10.1177/002199837000400201
[research_ashworth_mouch_1988]: https://doi.org/10.2514/6.1988-563
[research_ashworth_waltrip_1986]: https://doi.org/10.2514/6.1986-1104
[research_aslam_chen_2018]: https://doi.org/10.1080/00207179.2018.1484172
[research_aston_williams_1994]: https://doi.org/10.1016/0263-8223(94)90050-7
[research_atmaca_devisser_2025]: https://doi.org/10.2514/1.g009147
[research_audoin_baste_1994]: https://doi.org/10.1115/1.2901446
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
[research_badaliance_dill_1981]: https://doi.org/10.21236/ada105034
[research_badallo_trias_2015]: https://doi.org/10.1016/j.compstruct.2015.07.025
[research_badhurshah_alvarez_2024]: https://doi.org/10.3390/app14135531
[research_badihi_nezhad_2026]: https://doi.org/10.2514/1.c038688
[research_bagherzadeh_2026]: https://doi.org/10.3390/mca31030085
[research_bagherzadeh_mohammadkarimi_2025]: https://doi.org/10.3390/mca30020041
[research_bahamondejacome_elham_2017]: https://doi.org/10.2514/1.c034050
[research_bahr_mckay_2021]: https://doi.org/10.1017/aer.2021.114
[research_bai_2018]: https://doi.org/10.1049/joe.2018.0025
[research_bai_xu_2022]: https://doi.org/10.9734/jerr/2022/v22i517537
[research_baileyrandalle_powersbruceg_1988]: https://ntrs.nasa.gov/citations/19880063393
[research_baileyre_knottslh_1990]: https://ntrs.nasa.gov/citations/19910005040
[research_baileyre_smithre_1981]: https://ntrs.nasa.gov/citations/19820026927
[research_baker_jones_1985]: https://doi.org/10.1016/0263-8223(85)90018-2
[research_bakunowicz_meyer_2016]: https://doi.org/10.1017/aer.2016.98
[research_balaji_manickam_2024]: https://doi.org/10.1016/j.compstruct.2024.118199
[research_balakrishnan_2000]: https://doi.org/10.21236/ada377873
[research_balakrishnan_tuffaha_2012]: https://doi.org/10.1016/j.jfranklin.2011.10.004
[research_balatti_haddadkhodaparast_2021]: https://doi.org/10.1016/j.ast.2021.106805
[research_balatti_khodaparast_2022]: https://doi.org/10.2139/ssrn.4258795
[research_baldan_guardone_2024]: https://doi.org/10.1016/j.ast.2024.109345
[research_ballesterclaret_coelho_2024]: https://doi.org/10.1016/j.compstruct.2024.118461
[research_balunov_solyaev_2023]: https://doi.org/10.34759/trd-2023-129-04
[research_bandyopadhyay_1989]: https://doi.org/10.1017/s0001924000016651
[research_bandyopadhyay_1991]: https://doi.org/10.2514/3.46077
[research_banerjee_2019]: https://doi.org/10.2514/1.c034888
[research_banks_1988]: https://doi.org/10.21236/ada204640
[research_banksdanielw_1988]: https://ntrs.nasa.gov/citations/19890063987
[research_bantscheff_breitsamter_2023]: https://doi.org/10.3390/aerospace10070581
[research_bao_li_2025]: https://doi.org/10.3390/machines13060525
[research_barabanov_ortega_2017]: https://doi.org/10.1002/acs.2851
[research_baranovski_mikhailovskiy_2020]: https://doi.org/10.1615/tsagiscij.2020036204
[research_barbosa_bertolin_2022]: https://doi.org/10.2514/1.g006271
[research_bargill_stengel_1986]: https://doi.org/10.2514/3.45276
[research_barshalom_1985]: https://doi.org/10.21236/ada159053
[research_barshalom_1989]: https://doi.org/10.21236/ada215486
[research_barshalom_1990]: https://doi.org/10.21236/ada219629
[research_bartels_stanford_2018]: https://doi.org/10.2514/1.c034675
[research_bartelsroberte_stanfordbretk_2019]: https://ntrs.nasa.gov/citations/20200002388
[research_bartoszewicz_adamiak_2018]: https://doi.org/10.1002/acs.2922
[research_bashir_longtinmartel_2021]: https://doi.org/10.3390/app11041664
[research_bashir_negahban_2024]: https://doi.org/10.3390/biomimetics9020109
[research_bastin_coron_2025]: https://doi.org/10.1016/j.automatica.2024.112048
[research_basuroy_bhasin_2019]: https://doi.org/10.1002/acs.3046
[research_bataineh_shawabkeh_2023]: https://doi.org/10.15866/irease.v16i6.24344
[research_batina_yang_1985]: https://doi.org/10.2514/3.45137
[research_battaglia_riccio_2026]: https://doi.org/10.3390/act15080414
[research_battersonjamesg_omarathomasm_1989]: https://ntrs.nasa.gov/citations/19890006554
[research_bauchau_1981]: https://doi.org/10.1177/002199838101500205
[research_bauer_clarke_1995]: https://ntrs.nasa.gov/citations/19950016389
[research_baumgartner_viti_2016]: https://doi.org/10.2514/6.2016-3368
[research_bay_kara_2026]: https://doi.org/10.17798/bitlisfen.1847172
[research_bazhenov_lysenkova_2015]: https://doi.org/10.1615/tsagiscij.2015013712
[research_beatty_brooks_1977]: https://doi.org/10.21236/ada045951
[research_becker_1992]: https://doi.org/10.1016/0263-8223(92)90079-r
[research_beharie_pedro_2015]: https://doi.org/10.1017/s0001924000010587
[research_beitalmal_2025]: https://doi.org/10.47191/rajar/v11i4.11
[research_bellini_sorrentino_2018]: https://doi.org/10.1016/j.prostr.2018.06.027
[research_belmont_1983]: https://doi.org/10.21236/ada133274
[research_benaddy_labbadi_2022]: https://doi.org/10.1016/j.ifacol.2022.07.323
[research_benaouali_boutemedjet_2024]: https://doi.org/10.1108/aeat-11-2023-0310
[research_bendahmane_hamzacherif_2019]: https://doi.org/10.1080/15376494.2018.1553257
[research_bending_of_1991]: https://doi.org/10.1016/0010-4361(91)90115-w
[research_bengida_gurka_2022]: https://doi.org/10.1088/1748-3190/ac9bb5
[research_bennett_dansberry_1993]: https://doi.org/10.2514/3.46314
[research_bennettrm_farmermg_1977]: https://ntrs.nasa.gov/citations/19770060309
[research_bennettrobertm_batinajohnt_1988]: https://ntrs.nasa.gov/citations/19880010035
[research_benyamen_chowdhury_2024]: https://doi.org/10.1115/1.4065804
[research_beppu_curtiss_1966]: https://doi.org/10.21236/ad0640945
[research_berezhnitskii_denisyuk_1985]: https://doi.org/10.1007/bf01150635
[research_berg_ting_2025]: https://doi.org/10.2514/1.g008589
[research_bergen_arnold_1940]: https://doi.org/10.2514/8.1231
[research_berger_blanken_2022]: https://doi.org/10.4050/jahs.67.032009
[research_berger_blanken_2022_b]: https://doi.org/10.4050/jahs.67.032008
[research_berger_tischler_2021]: https://doi.org/10.2514/1.g005768
[research_bergman_1948]: https://doi.org/10.21236/ada301214
[research_berman_gran_1974]: https://doi.org/10.2514/3.60358
[research_bernstein_2000]: https://doi.org/10.21236/ada382981
[research_bernstein_hollot_1989]: https://doi.org/10.1016/0167-6911(89)90067-4
[research_berry_powers_1982]: https://doi.org/10.2514/3.57395
[research_berrydt_1981]: https://ntrs.nasa.gov/citations/19810059723
[research_besch_liu_1973]: https://doi.org/10.21236/ad0757645
[research_besch_rood_1976]: https://doi.org/10.21236/ada027188
[research_bessa_puig_2020]: https://doi.org/10.1016/j.jfranklin.2020.02.002
[research_bessadi_saussie_2016]: https://doi.org/10.1016/j.ifacol.2016.09.017
[research_bester_2023]: https://doi.org/10.1051/matecconf/202338805002
[research_beyer_steen_2024]: https://doi.org/10.2514/1.g007984
[research_beyer_ullah_2024]: https://doi.org/10.1007/s13272-024-00760-8
[research_beyers_1988]: https://doi.org/10.2514/3.45559
[research_bhachu_haftka_2015]: https://doi.org/10.2514/1.c032945
[research_bhardwaj_kapania_1995]: https://doi.org/10.2514/3.46814
[research_bhatia_jiang_2021]: https://doi.org/10.1002/acs.3228
[research_bhattacharyya_conlansmith_2019]: https://doi.org/10.1016/j.cad.2018.11.001
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
[research_binz_islam_2019]: https://doi.org/10.1177/1756829319861370
[research_binz_moormann_2020]: https://doi.org/10.1177/1756829320961925
[research_biquan_huanwen_1990]: https://doi.org/10.1007/bf02015201
[research_bischoff_1983]: https://doi.org/10.2514/3.44899
[research_biskner_higgins_2005]: https://doi.org/10.21236/ada443361
[research_bismarcknasr_1994]: https://doi.org/10.2514/3.46590
[research_biswas_1993]: https://doi.org/10.1016/0263-8223(93)90233-g
[research_bjarke_delfrate_1992]: https://ntrs.nasa.gov/citations/19930003165
[research_black_moorhouse_1979]: https://doi.org/10.21236/ada085085
[research_blackwell_pounds_1977]: https://doi.org/10.2514/3.58877
[research_blair_weisshaar_1981]: https://doi.org/10.2514/6.1981-1670
[research_blair_weisshaar_1982]: https://doi.org/10.2514/3.44806
[research_bland_1980]: https://doi.org/10.2514/3.44684
[research_blight_gangsaas_1986]: https://doi.org/10.2514/3.20145
[research_bliss_1980]: https://doi.org/10.21236/ada093301
[research_boadocuartero_perezalvarez_2024]: https://doi.org/10.3390/aerospace11090748
[research_boby_abdullah_2019]: https://doi.org/10.12928/telkomnika.v17i5.12810
[research_boden_jentink_2013]: https://doi.org/10.1007/978-3-642-34738-2_7
[research_boden_lanari_2013]: https://doi.org/10.1007/978-3-642-34738-2_5
[research_bodson_2000]: https://doi.org/10.21236/ada381657
[research_bogan_1981]: https://doi.org/10.1007/bf00884128
[research_bohlmann_eckstrom_1990]: https://doi.org/10.2514/3.25319
[research_bohlmannjonathand_1989]: https://ntrs.nasa.gov/citations/19890009883
[research_bohlmannjonathand_scottrobertc_1991]: https://ntrs.nasa.gov/citations/19910047245
[research_bohlmannjonathand_weisshaarterrencea_1988]: https://ntrs.nasa.gov/citations/19880044993
[research_boldingrm_stearmanro_1976]: https://ntrs.nasa.gov/citations/19770014087
[research_bolotin_grishko_1996]: https://doi.org/10.1006/jsvi.1996.0132
[research_bombardieri_cavallaro_2021]: https://doi.org/10.1007/s00158-021-02884-5
[research_bondarenko_shkolnyi_2024]: https://doi.org/10.20535/0203-3771482024318185
[research_bons_martins_2020]: https://doi.org/10.3390/aerospace7080118
[research_bons_martins_2022]: https://doi.org/10.1115/1.4055630
[research_boothe_chen_1974]: https://doi.org/10.21236/ad0782218
[research_bordogna_lancelot_2020]: https://doi.org/10.1007/s00158-019-02446-w
[research_boschja_kuehlwj_1976]: https://ntrs.nasa.gov/citations/19760058477
[research_bosworth_1992]: https://ntrs.nasa.gov/citations/19920009932
[research_bosworth_cox_1989]: https://ntrs.nasa.gov/citations/19890065158
[research_bottasso_montinari_2015]: https://doi.org/10.4050/jahs.60.022005
[research_bouadi_moracamino_2018]: https://doi.org/10.2514/1.c034477
[research_boudreau_1977]: https://doi.org/10.2514/3.58889
[research_bouras_2020]: https://doi.org/10.5373/jardcs/v12sp3/20201258
[research_bouton_1950]: https://doi.org/10.2514/8.1573
[research_bowers_1981]: https://doi.org/10.2514/3.57530
[research_bowers_1984]: https://ntrs.nasa.gov/citations/19870001428
[research_bowes_miller_1976]: https://doi.org/10.21236/ada026963
[research_bowmankeithb_grandhiramanav_1989]: https://ntrs.nasa.gov/citations/19890015800
[research_boyd_1977]: https://doi.org/10.21236/ada053640
[research_boydenrp_1974]: https://ntrs.nasa.gov/citations/19830002753
[research_boydenrp_1978]: https://ntrs.nasa.gov/citations/19780025107
[research_bradley_1986]: https://doi.org/10.21236/ada173255
[research_bradley_haughn_2026]: https://doi.org/10.2514/1.c038700
[research_bras_warwick_2022]: https://doi.org/10.1016/j.ast.2022.107400
[research_breitsamter_laschka_2001]: https://doi.org/10.2514/2.2758
[research_briggs_reed_1982]: https://doi.org/10.21236/ada125764
[research_brigham_barrie_1973]: https://doi.org/10.21236/ad0782258
[research_brightlg_petersonvl_1960]: https://ntrs.nasa.gov/citations/19650018341
[research_brockld_goodmanha_1981]: https://ntrs.nasa.gov/citations/19820004206
[research_brodecki_subbarao_2015]: https://doi.org/10.2514/1.g000220
[research_broer_benedictus_2022]: https://doi.org/10.3390/aerospace9040183
[research_broglio_1957]: https://doi.org/10.2514/8.3851
[research_brooks_martins_2018]: https://doi.org/10.1016/j.compstruct.2018.07.100
[research_brooks_martins_2019]: https://doi.org/10.1016/j.jfluidstructs.2019.04.005
[research_brooksjd_beamishjk_1977]: https://ntrs.nasa.gov/citations/19780002105
[research_broussard_stengel_1977]: https://doi.org/10.2514/3.44630
[research_broussardjr_halyon_1983]: https://ntrs.nasa.gov/citations/19840042741
[research_brouwer_mcnamara_2020]: https://doi.org/10.1016/j.jfluidstructs.2019.102838
[research_brownsr_szalaikj_1977]: https://ntrs.nasa.gov/citations/19780028344
[research_bruderlin_hosters_2018]: https://doi.org/10.1007/s13272-018-0322-3
[research_brunojoseph_libeskindmark_1990]: https://ntrs.nasa.gov/citations/19920023270
[research_bryson_desai_1969]: https://doi.org/10.2514/3.44093
[research_bryson_rumpfkeil_2019]: https://doi.org/10.2514/1.c035152
[research_bu_luo_2025]: https://doi.org/10.1109/jmass.2024.3507735
[research_buchter_sebastiasaez_2021]: https://doi.org/10.1177/14759217211048149
[research_budd_1984]: https://ntrs.nasa.gov/citations/19860014095
[research_budd_1987]: https://ntrs.nasa.gov/citations/19890009047
[research_bueno_dowell_2020]: https://doi.org/10.2514/1.c035885
[research_buffington_1997]: https://doi.org/10.21236/ada327799
[research_buffington_1999]: https://doi.org/10.21236/ada375713
[research_buffington_1999_b]: https://doi.org/10.21236/ada374954
[research_buffington_adams_1995]: https://doi.org/10.1016/0967-0661(95)00039-w
[research_bugala_2025]: https://doi.org/10.2478/tar-2025-0008
[research_bugala_payenskyy_2025]: https://doi.org/10.1108/aeat-05-2025-0183
[research_bullock_fields_1998]: https://doi.org/10.21236/ada357847
[research_burdette_martins_2018]: https://doi.org/10.1016/j.ast.2018.08.004
[research_burkenjohnj_2007]: https://ntrs.nasa.gov/citations/20090007779
[research_burkett_1989]: https://doi.org/10.1017/s0001924000022235
[research_burkhalter_1993]: https://doi.org/10.2514/3.46447
[research_burner_martinson_1996]: https://doi.org/10.2514/6.1996-2253
[research_burnett_beranek_2016]: https://doi.org/10.1017/aer.2016.41
[research_burns_1975]: https://doi.org/10.1017/s0001924000034862
[research_burt_1975]: https://doi.org/10.2514/3.59795
[research_busan_1998]: https://doi.org/10.21236/ada340820
[research_butler_1976]: https://doi.org/10.21236/ada023690
[research_butler_1982]: https://doi.org/10.2514/3.44764
[research_butler_1983]: https://doi.org/10.1017/s0001924000051046
[research_buzica_biswanger_2018]: https://doi.org/10.1016/j.trpro.2018.02.005
[research_byreddy_grandhi_2003]: https://doi.org/10.21236/ada417124
[research_c_yharmin_2018]: https://doi.org/10.14419/ijet.v7i4.13.21355
[research_cabuk_2026]: https://doi.org/10.1016/j.ast.2026.111844
[research_cagdas_2017]: https://doi.org/10.1016/j.oceaneng.2017.09.011
[research_cahn_garcia_1971]: https://doi.org/10.2514/3.44233
[research_cai_fan_2026]: https://doi.org/10.2514/1.c038462
[research_caixeta_marques_2018]: https://doi.org/10.1007/s40430-017-0958-7
[research_calarese_1984]: https://doi.org/10.2514/3.48231
[research_calico_fuller_1981]: https://doi.org/10.2514/6.1981-1884
[research_calise_1977]: https://doi.org/10.2514/3.63239
[research_callaghan_kunz_2021]: https://doi.org/10.2514/1.g004748
[research_camacho_akhavan_2021]: https://doi.org/10.1016/j.compstruct.2021.113765
[research_campagna_benedetti_2025]: https://doi.org/10.1016/j.compstruct.2025.119508
[research_campagna_gulizzi_2025]: https://doi.org/10.1016/j.compstruct.2024.118697
[research_campbell_terrell_1987]: https://doi.org/10.21236/ada190882
[research_campbellrichardl_smithleigha_1989]: https://ntrs.nasa.gov/citations/19910001577
[research_campos_marques_2021]: https://doi.org/10.3390/aerospace8030077
[research_candon_marzocca_2026]: https://doi.org/10.2514/1.j066515
[research_cannella_garinei_2018]: https://doi.org/10.1016/j.compstruct.2017.11.029
[research_cano_sobel_2016]: https://doi.org/10.4236/eng.2016.84016
[research_cao_chen_2026]: https://doi.org/10.1016/j.neucom.2025.132460
[research_cao_jia_2020]: https://doi.org/10.1016/j.jfranklin.2020.08.028
[research_cao_liu_2025_b]: https://doi.org/10.1016/j.ast.2025.110036
[research_cao_lu_2024]: https://doi.org/10.3390/biomimetics9050263
[research_cao_tang_2017]: https://doi.org/10.1631/fitee.1601363
[research_caponefj_1981]: https://ntrs.nasa.gov/citations/19810010493
[research_carico_1998]: https://doi.org/10.21236/ada350677
[research_carlson_1976]: https://doi.org/10.2514/3.58667
[research_carlson_verberg_2017]: https://doi.org/10.1063/1.4975673
[research_carneiro_gamboa_2019]: https://doi.org/10.1108/rpj-02-2018-0044
[research_carrera_varello_2013]: https://doi.org/10.1007/s13272-013-0063-2
[research_casey_1988]: https://doi.org/10.21236/ada195699
[research_castaneda_gordillo_2019]: https://doi.org/10.3390/electronics8070793
[research_castellani_cooper_2017]: https://doi.org/10.2514/1.c033825
[research_cavalcanti_uehara_2026]: https://doi.org/10.2514/1.c038528
[research_cavaliere_fezans_2024]: https://doi.org/10.2514/1.g007762
[research_cavaliere_fezans_2024_b]: https://doi.org/10.2514/1.g008040
[research_cavallaro_bombardieri_2015]: https://doi.org/10.1016/j.jfluidstructs.2015.08.016
[research_cebeci_1974]: https://doi.org/10.2514/3.49207
[research_cen_li_2020]: https://doi.org/10.1177/0954410020944085
[research_center_1975]: https://doi.org/10.21236/adb006719
[research_cesnik_2002]: https://doi.org/10.21236/ada401331
[research_cesnik_2005]: https://doi.org/10.21236/ada439640
[research_cestino_iannuzzo_2026]: https://doi.org/10.2514/1.c038607
[research_chabir_bouteraa_2017]: https://doi.org/10.1504/ijmic.2017.082487
[research_chabod_baron_2020]: https://doi.org/10.2478/fas-2020-0005
[research_chacon_mcbride_1988]: https://ntrs.nasa.gov/citations/19880011768
[research_chacon_mcbride_1990]: https://ntrs.nasa.gov/citations/19900000158
[research_chai_song_2017]: https://doi.org/10.1016/j.compstruct.2017.07.053
[research_chajjed_khalil_2024]: https://doi.org/10.1016/j.jsv.2023.117819
[research_chakravarthy_evans_2015]: https://doi.org/10.1080/01630563.2015.1057286
[research_chakravarty_mahanta_2015]: https://doi.org/10.1002/rnc.3392
[research_chalk_1964]: https://doi.org/10.2514/3.43604
[research_chalk_neal_1969]: https://doi.org/10.21236/ad0860856
[research_chancevoughtcorpdallastx_1979]: https://doi.org/10.21236/ada358711
[research_chang_debreuker_2022]: https://doi.org/10.2514/1.g006690
[research_chang_guo_2022]: https://doi.org/10.1016/j.ifacol.2022.07.214
[research_changchuan_lan_2018]: https://doi.org/10.2514/1.c034162
[research_changchuan_zhiying_2022]: https://doi.org/10.2514/1.j061138
[research_chaparrodaniel_fujiwaragustavoec_2016]: https://ntrs.nasa.gov/citations/20160008102
[research_chatterjee_chowdhury_2019]: https://doi.org/10.1007/s00158-018-2167-0
[research_chattopadhyayaditi_jharatneshwar_1996]: https://ntrs.nasa.gov/citations/19970028021
[research_chattopadhyayaditi_zhangsen_1995]: https://ntrs.nasa.gov/citations/19950026507
[research_chau_piotrowski_2026]: https://doi.org/10.2514/1.c038646
[research_chau_zingg_2022]: https://doi.org/10.2514/1.c036389
[research_chau_zingg_2023]: https://doi.org/10.2514/1.c037158
[research_chauhan_martins_2021]: https://doi.org/10.2514/1.c035991
[research_chauhan_martins_2024]: https://doi.org/10.3390/aerospace11070512
[research_chauhan_praveen_2023]: https://doi.org/10.61653/joast.v62i4.2010.508
[research_chen_1982]: https://doi.org/10.2514/3.51069
[research_chen_cai_2026]: https://doi.org/10.1109/tie.2025.3639811
[research_chen_chen_2019]: https://doi.org/10.2514/1.j058522
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
[research_chen_li_2024]: https://doi.org/10.3390/s24051597
[research_chen_liu_2016]: https://doi.org/10.2514/1.c033305
[research_chen_mangione_1967]: https://doi.org/10.2514/3.4365
[research_chen_meng_2025]: https://doi.org/10.1016/j.ast.2025.110043
[research_chen_nie_2018]: https://doi.org/10.1016/j.compstruct.2017.12.042
[research_chen_niu_2018]: https://doi.org/10.1109/access.2018.2820008
[research_chen_qiu_2017]: https://doi.org/10.1016/j.ast.2017.09.018
[research_chen_rao_2023]: https://doi.org/10.1016/j.cja.2023.03.039
[research_chen_ren_2015]: https://doi.org/10.1504/ijasm.2015.073525
[research_chen_shi_2023]: https://doi.org/10.1063/5.0130370
[research_chen_shi_2023_b]: https://doi.org/10.1063/5.0162013
[research_chen_sun_1987]: https://doi.org/10.1016/0263-8223(87)90019-5
[research_chen_tang_2017]: https://doi.org/10.1177/0954410017746199
[research_chen_wang_2019]: https://doi.org/10.1061/(asce)as.1943-5525.0001004
[research_chen_wang_2026]: https://doi.org/10.1016/j.ast.2026.112682
[research_chen_yang_2018]: https://doi.org/10.1360/n092017-00428
[research_chen_zhai_2025]: https://doi.org/10.1186/s42774-025-00227-2
[research_chen_zhang_2015]: https://doi.org/10.1360/sspma2015-00338
[research_chen_zhang_2017]: https://doi.org/10.1177/1729881416678141
[research_chen_zhao_2020]: https://doi.org/10.1061/(asce)as.1943-5525.0001201
[research_cheng_li_2023]: https://doi.org/10.3390/aerospace10090786
[research_cheng_liang_2019]: https://doi.org/10.1016/j.addma.2019.03.001
[research_cheng_wei_2017]: https://doi.org/10.1002/acs.2779
[research_cheng_zhou_2015]: https://doi.org/10.1115/1.4029026
[research_chenghk_mengsy_1980]: https://ntrs.nasa.gov/citations/19800038581
[research_chetty_lakshmi_1991]: https://doi.org/10.1016/s1474-6670(17)54311-6
[research_chiarelli_bonomo_2019]: https://doi.org/10.1155/2019/8210235
[research_chin_1989]: https://doi.org/10.2514/3.45888
[research_chin_berman_1982]: https://doi.org/10.2514/6.1982-1538
[research_chin_lee_1994]: https://doi.org/10.1016/0967-0661(94)90572-x
[research_chinj_chaconv_1987]: https://ntrs.nasa.gov/citations/19880027032
[research_chinvorarat_2021]: https://doi.org/10.1016/j.heliyon.2021.e08410
[research_chipman_zislin_1982]: https://doi.org/10.2514/6.1982-684
[research_chipman_zislin_1983]: https://doi.org/10.2514/3.48204
[research_chipmanr_rauchf_1984]: https://ntrs.nasa.gov/citations/19840013485
[research_chipmanr_rauchf_1985]: https://ntrs.nasa.gov/citations/19850048205
[research_choi_2016]: https://doi.org/10.5762/kais.2016.17.1.159
[research_choi_choi_2026]: https://doi.org/10.3390/aerospace13060526
[research_choi_kim_2023]: https://doi.org/10.3390/drones7070418
[research_choi_lim_2020]: https://doi.org/10.5139/jksas.2020.48.8.555
[research_choi_park_2019]: https://doi.org/10.1016/j.compstruct.2019.111027
[research_choi_shrestha_2017]: https://doi.org/10.1177/1475921716686963
[research_choosakngaongam_rapeeujjin_2024]: https://doi.org/10.37934/cfdl.16.5.18
[research_chougule_sonawane_2017]: https://doi.org/10.2139/ssrn.3101358
[research_chowdary_parthan_1994]: https://doi.org/10.1016/0045-7949(94)90200-3
[research_chowhan_arya_2019]: https://doi.org/10.1002/j.2334-5837.2019.00697.x
[research_christoforou_1993]: https://doi.org/10.1016/0263-8223(93)90046-s
[research_christopherkdroney_anthonyjsclafani_2020]: https://ntrs.nasa.gov/citations/20205005698
[research_chujulio_lawingpiercel_1990]: https://ntrs.nasa.gov/citations/19930020260
[research_cidmontoya_hernandez_2018]: https://doi.org/10.1016/j.jweia.2017.12.018
[research_clark_2001]: https://doi.org/10.21236/ada399161
[research_clark_letron_1989]: https://doi.org/10.2514/3.20392
[research_clark_spurlin_1962]: https://doi.org/10.21236/ad0329345
[research_clarker_shaned_1982]: https://ntrs.nasa.gov/citations/19820015371
[research_clarkerobert_burkenjohnj_1994]: https://ntrs.nasa.gov/citations/19940029878
[research_clay_rockafellow_1973]: https://doi.org/10.21236/ad0758891
[research_clements_djidjeli_2023]: https://doi.org/10.1061/jaeeez.aseng-4707
[research_clementskeith_2016]: https://ntrs.nasa.gov/citations/20160013364
[research_clews_1973]: https://doi.org/10.1108/eb035015
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
[research_collins_1988]: https://doi.org/10.4271/881504
[research_combined_flight_1974]: https://doi.org/10.1108/eb035139
[research_comer_chakraborty_2024]: https://doi.org/10.4050/jahs.69.032003
[research_composite_materials_1989]: https://doi.org/10.1108/eb036810
[research_concorde_automatic_1971]: https://doi.org/10.1108/eb034745
[research_cong_hu_2023]: https://doi.org/10.3390/aerospace10030241
[research_conlansmith_andreasen_2022]: https://doi.org/10.1007/s00158-022-03246-5
[research_connelly_1982]: https://doi.org/10.21236/ada120473
[research_contellasins_landersheim_2021]: https://doi.org/10.3390/app11062752
[research_cook_1979]: https://doi.org/10.1090/qam/542990
[research_cooperpa_stroudwj_1972]: https://ntrs.nasa.gov/citations/19730028903
[research_coppin_birch_2018]: https://doi.org/10.2514/1.c033988
[research_cordeiro_azinheira_2024]: https://doi.org/10.1016/j.conengprac.2024.105909
[research_corlissld_talbotpd_1977]: https://ntrs.nasa.gov/citations/19770024230
[research_cornelius_lucius_1994]: https://doi.org/10.2514/3.46566
[research_cornellaeronauticallabincbuffalony_1947]: https://doi.org/10.21236/ada800190
[research_cotton_1974]: https://doi.org/10.21236/ada000894
[research_cotton_bjarke_1994]: https://ntrs.nasa.gov/citations/19950004446
[research_crabtree_1979]: https://doi.org/10.21236/ada081738
[research_craig_1965]: https://doi.org/10.21236/ad0628087
[research_craig_erbug_1976]: https://doi.org/10.1016/0045-7949(76)90049-3
[research_crandall_maund_1973]: https://doi.org/10.21236/ad0766642
[research_cranedf_1983]: https://ntrs.nasa.gov/citations/19830055004
[research_cranedf_1984]: https://ntrs.nasa.gov/citations/19850009674
[research_craneharoldl_sommerrobertw_1961]: https://ntrs.nasa.gov/citations/19980227996
[research_craver_egle_1972]: https://doi.org/10.1016/0022-460x(72)90530-5
[research_crawley_lee_1978]: https://doi.org/10.21236/ada062582
[research_crews_naik_1986]: https://doi.org/10.1016/0263-8223(86)90066-8
[research_crimi_grace_1965]: https://doi.org/10.21236/ad0619661
[research_crimi_ordway_1962]: https://doi.org/10.2514/8.9560
[research_crisfield_1978]: https://doi.org/10.1016/0045-7949(78)90144-x
[research_crittenden_weishaar_1978]: https://doi.org/10.2514/3.58383
[research_croommarka_whippleraymondd_1988]: https://ntrs.nasa.gov/citations/19890063988
[research_croop_1985]: https://doi.org/10.21236/ada368444
[research_crother_gabelman_1973]: https://doi.org/10.21236/ada004416
[research_crouse_leishman_1992]: https://doi.org/10.2514/3.46139
[research_crowe_1937]: https://doi.org/10.1108/eb030157
[research_cui_azuara_2021]: https://doi.org/10.1177/14759217211023934
[research_cui_he_2025]: https://doi.org/10.3390/aerospace12050404
[research_cui_li_2022]: https://doi.org/10.1016/j.oceaneng.2022.113138
[research_cui_miao_2026]: https://doi.org/10.1016/j.compstruct.2026.120413
[research_cui_yang_2016]: https://doi.org/10.1061/(asce)as.1943-5525.0000528
[research_cully_boller_1973]: https://doi.org/10.21236/ad0916279
[research_cunis_burlion_2019]: https://doi.org/10.2514/1.g003618
[research_cunis_condomines_2020]: https://doi.org/10.2514/1.c035455
[research_cunis_condomines_2020_b]: https://doi.org/10.2514/1.g004753
[research_cunningham_batina_1988]: https://doi.org/10.2514/3.45686
[research_cunninghamherbertj_batinajohnt_1987]: https://ntrs.nasa.gov/citations/19880064102
[research_currao_jiang_2026]: https://doi.org/10.1017/flo.2026.10056
[research_curry_matthews_1965]: https://doi.org/10.21236/ad0617748
[research_curry_moulton_1989]: https://ntrs.nasa.gov/citations/19900004886
[research_curry_moulton_1990]: https://ntrs.nasa.gov/citations/19900019217
[research_curtiss_1971]: https://doi.org/10.2514/3.59098
[research_curtiss_howardc_1961]: https://doi.org/10.21236/ad0263838
[research_cuschieri_1990]: https://doi.org/10.21236/ada279431
[research_cutchinsma_purvisjw_1982]: https://ntrs.nasa.gov/citations/19820025882
[research_czyba_stajer_2019]: https://doi.org/10.24425/acs.2019.127525
[research_czysz_1963]: https://doi.org/10.21236/ad0407689
[research_dababneh_kipouros_2018]: https://doi.org/10.3390/aerospace5010003
[research_dagal_2026]: https://doi.org/10.1016/j.ress.2025.111841
[research_daghighi_rouhi_2020]: https://doi.org/10.1016/j.compstruct.2019.111630
[research_dagilis_kilikevicius_2023]: https://doi.org/10.3390/aerospace10090801
[research_dagkolu_gokdag_2021]: https://doi.org/10.1016/j.promfg.2021.07.037
[research_dai_hu_2025]: https://doi.org/10.1016/j.cja.2024.09.021
[research_dai_yang_2015]: https://doi.org/10.2322/tjsass.58.237
[research_daken_mar_1985]: https://doi.org/10.1016/0263-8223(85)90002-9
[research_damico_labella_2025]: https://doi.org/10.1016/j.sysconle.2024.105974
[research_damodaran_caughey_1988]: https://doi.org/10.2514/3.10046
[research_dandois_2016]: https://doi.org/10.1063/1.4937426
[research_dandrea_2003]: https://doi.org/10.21236/ada422201
[research_dandrea_2008]: https://doi.org/10.21236/ada530333
[research_daniel_1976]: https://doi.org/10.21236/ada041490
[research_danieldealmeidapereira_flaviodonizetimarques_2015]: https://doi.org/10.20906/cps/cob-2015-0339
[research_dapolito_sulzbachner_2021]: https://doi.org/10.1016/j.ifacol.2021.10.454
[research_darabi_ganesan_2016]: https://doi.org/10.1016/j.compstruct.2016.02.064
[research_darabi_ganesan_2017]: https://doi.org/10.1016/j.compstruct.2017.04.059
[research_darabseh_tarabulsi_2022]: https://doi.org/10.3390/aerospace9090475
[research_daronch_drofelnik_2019]: https://doi.org/10.1016/j.ast.2019.04.057
[research_das_kapuria_2016]: https://doi.org/10.1016/j.jfluidstructs.2015.11.008
[research_das_longo_1995]: https://doi.org/10.2514/3.46782
[research_data_driven_model_free_2016]: https://doi.org/10.12700/aph.13.1.2016.1.7
[research_daudeville_ladeveze_1993]: https://doi.org/10.1016/0263-8223(93)90203-3
[research_davanipour_khayatian_2017]: https://doi.org/10.1002/acs.2849
[research_davidmrichwine_davidffisher_1992]: https://ntrs.nasa.gov/citations/19920022032
[research_davila_bisagni_2017]: https://doi.org/10.1177/0021998317715785
[research_davis_1973]: https://doi.org/10.21236/ad0781807
[research_davis_garnett_1977]: https://doi.org/10.21236/ada050059
[research_davisddjr_farleygaryl_1993]: https://ntrs.nasa.gov/citations/19930049917
[research_dawe_bull_2025]: https://doi.org/10.2514/1.j064731
[research_dawe_roufaeil_1980]: https://doi.org/10.1016/0022-460x(80)90477-0
[research_dawson_fortin_1987]: https://ntrs.nasa.gov/citations/19880003104
[research_daynes_2024]: https://doi.org/10.1016/j.addma.2024.104010
[research_de_jrad_2019]: https://doi.org/10.2514/1.c034818
[research_deandrea_roache_1991]: https://doi.org/10.2514/6.1991-5
[research_deangelis_1981]: https://ntrs.nasa.gov/citations/19820030846
[research_deangelis_1982]: https://doi.org/10.2514/3.44816
[research_deepa_gupta_2023]: https://doi.org/10.61653/joast.v65i2.2013.727
[research_deetsda_1975]: https://ntrs.nasa.gov/citations/19750010175
[research_deformational_behaviour_1990]: https://doi.org/10.1016/0010-4361(90)90242-o
[research_degaspari_mantegazza_2024]: https://doi.org/10.1109/access.2024.3390557
[research_degaspari_riccobene_2018]: https://doi.org/10.2514/1.c034860
[research_dehghanmanshadi_saghafi_2021]: https://doi.org/10.2514/1.c035941
[research_delcarre_palacios_2020]: https://doi.org/10.2514/1.c035901
[research_delfrate_1992]: https://doi.org/10.1007/978-3-642-84824-7_44
[research_delfrate_saltzman_1992]: https://ntrs.nasa.gov/citations/19930004134
[research_demarchi_haning_1978]: https://doi.org/10.21236/ada060326
[research_demedeiros_vandepitte_2017]: https://doi.org/10.1177/1475921716688442
[research_demir_gorguluarslan_2023]: https://doi.org/10.1007/s00158-023-03557-1
[research_demir_seyfullahbabaarslan_2021]: https://doi.org/10.11648/j.ajset.20210602.13
[research_deng_qin_2021]: https://doi.org/10.2514/1.j060528
[research_deng_stoica_2024]: https://doi.org/10.1016/j.ifacol.2025.01.196
[research_deng_xu_2026]: https://doi.org/10.1142/s2301385027500622
[research_deng_yi_2023]: https://doi.org/10.3390/aerospace10020125
[research_deng_yi_2026]: https://doi.org/10.3390/aerospace13060540
[research_deng_zeng_2024]: https://doi.org/10.1177/14759217241233181
[research_deng_zhang_2023]: https://doi.org/10.3390/aerospace10060537
[research_deobald_gibson_1988]: https://doi.org/10.1016/s0022-460x(88)80187-1
[research_derkach_zinkovskii_2022]: https://doi.org/10.1016/j.prostr.2022.01.005
[research_description_and_1975]: https://ntrs.nasa.gov/citations/19750010173
[research_design_and_2024]: https://doi.org/10.52783/jisem.v9i4.74
[research_design_of_1995]: https://doi.org/10.1016/0967-0661(95)90151-5
[research_design_of_2019]: https://doi.org/10.35940/ijrte.b1316.0982s1119
[research_design_optimization_2025]: https://doi.org/10.14445/23488360/ijme-v12i9p109
[research_desilva_carmichael_1978]: https://doi.org/10.2514/3.58435
[research_desilvabme_medanrt_1978]: https://ntrs.nasa.gov/citations/19790005851
[research_deskos_delcarre_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.102981
[research_desouza_deleon_2023]: https://doi.org/10.1080/0305215x.2023.2243455
[research_desouza_vuillemin_2023]: https://doi.org/10.2514/1.g007153
[research_devi_2019]: https://doi.org/10.21275/sr231208204149
[research_dewagter_meulenbeld_2019]: https://doi.org/10.1177/1756829319880302
[research_dexl_hauffe_2020]: https://doi.org/10.1007/s00158-020-02613-4
[research_dexter_1993]: https://doi.org/10.1243/pime_proc_1993_207_241_02
[research_dhadekar_misra_2021]: https://doi.org/10.1108/aeat-07-2020-0149
[research_dhiman_abhishek_2022]: https://doi.org/10.2514/1.c036390
[research_dhital_chouvion_2024]: https://doi.org/10.3390/aerospace11121043
[research_dhonau_blosser_1974]: https://doi.org/10.21236/ada032816
[research_dias_2023]: https://doi.org/10.2514/1.c037252
[research_dicaprio_acanfora_2019]: https://doi.org/10.3390/aerospace6060071
[research_didonato_balachandran_2017]: https://doi.org/10.2514/1.g000252
[research_diederichfranklinw_budianskybernard_1948]: https://ntrs.nasa.gov/citations/19930082318
[research_difrancesco_mattei_2016]: https://doi.org/10.2514/1.c033183
[research_difranco_1970]: https://doi.org/10.2514/3.44199
[research_digital_model_reference_1994]: https://doi.org/10.1016/0967-0661(94)90529-0
[research_dileone_lobalbo_2021]: https://doi.org/10.3390/aerospace8110334
[research_dillinger_abdalla_2019]: https://doi.org/10.1007/s13272-019-00397-y
[research_dillinger_meddaikar_2020]: https://doi.org/10.3390/fluids5010035
[research_dilmi_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001401
[research_ding_shi_2025]: https://doi.org/10.3390/aerospace12070580
[research_ding_xu_2022]: https://doi.org/10.1016/j.compstruct.2022.116067
[research_ding_zhou_2018]: https://doi.org/10.1007/s42401-018-0008-x
[research_dinler_2025]: https://doi.org/10.3390/app152010882
[research_dipasquale_prince_2023]: https://doi.org/10.3390/aerospace10060569
[research_dirito_schettini_2016]: https://doi.org/10.1016/j.ress.2015.12.012
[research_disante_2015]: https://doi.org/10.3390/s150818666
[research_divakar_bl_2026]: https://doi.org/10.1002/adc2.70054
[research_dlamini_jones_2016]: https://doi.org/10.1017/aer.2016.42
[research_dlbirdsall_1970]: https://doi.org/10.1017/s0001924000114812
[research_dobosbubno_hartsook_1977]: https://doi.org/10.21236/ada062008
[research_dodayav_biswas_2024]: https://doi.org/10.2139/ssrn.4875854
[research_doggett_ricketts_1980]: https://ntrs.nasa.gov/citations/19810003937
[research_doggettrobertvjr_riverajoseajr_1995]: https://ntrs.nasa.gov/citations/19950019961
[research_doi_kataoka_1982]: https://doi.org/10.1299/jsme1958.25.1373
[research_dong_li_2023]: https://doi.org/10.1002/rnc.6722
[research_dong_lu_2016]: https://doi.org/10.1155/2016/5037678
[research_dong_shi_2019]: https://doi.org/10.1063/1.5093559
[research_dong_zhou_2025]: https://doi.org/10.1016/j.ast.2025.110199
[research_dooley_1965]: https://doi.org/10.1016/0020-7403(65)90017-2
[research_dorey_good_1980]: https://doi.org/10.1080/00423118008968613
[research_dowell_bliss_1978]: https://doi.org/10.21236/ada055735
[research_dowell_hall_2003]: https://doi.org/10.21236/ada426408
[research_drtil_schulz_1978]: https://doi.org/10.1108/eb035443
[research_duan_okwudire_2019]: https://doi.org/10.1016/j.automatica.2018.11.049
[research_duan_zhang_2018]: https://doi.org/10.1007/s42401-018-0009-9
[research_dubary_bouvet_2018]: https://doi.org/10.1016/j.compstruct.2018.08.045
[research_dubigeon_1992]: https://doi.org/10.2514/3.11232
[research_dugundji_1965]: https://doi.org/10.21236/ad0624995
[research_dugundji_dowell_1962]: https://doi.org/10.21236/ad0278235
[research_dukes_1970]: https://doi.org/10.21236/ad0871424
[research_dul_2018]: https://doi.org/10.1108/aeat-11-2016-0215
[research_dunmire_1982]: https://doi.org/10.21236/ada148595
[research_dunningpeterd_stanfordbretk_2014]: https://ntrs.nasa.gov/citations/20140007305
[research_dunnwr_cottrelld_1986]: https://ntrs.nasa.gov/citations/19860019473
[research_durand_teper_1964]: https://doi.org/10.21236/ad0606040
[research_durlofsky_mayers_1970]: https://doi.org/10.21236/ad0871426
[research_durstonda_schreinerja_1983]: https://ntrs.nasa.gov/citations/19840027787
[research_dussart_lone_2019]: https://doi.org/10.3390/aerospace6060070
[research_dutta_zhao_2025]: https://doi.org/10.1016/j.compstruct.2025.119221
[research_dwivedi_anitha_2022]: https://doi.org/10.1002/masy.202100364
[research_dzhurynskyi_2026]: https://doi.org/10.32620/aktt.2026.1.03
[research_earls_sitz_1989]: https://ntrs.nasa.gov/citations/19890065304
[research_eastep_olsen_1980]: https://doi.org/10.2514/3.50866
[research_eastep_venkayya_1984]: https://doi.org/10.2514/3.45063
[research_ebnerre_markjg_1977]: https://ntrs.nasa.gov/citations/19770059956
[research_ebrahimzade_dardel_2016]: https://doi.org/10.1007/s11071-016-2948-1
[research_ecer_1985]: https://doi.org/10.21236/ada162168
[research_eckhaus_1962]: https://doi.org/10.2514/8.9589
[research_eckstromcv_spaincv_1982]: https://ntrs.nasa.gov/citations/19820046611
[research_edwards_1963]: https://doi.org/10.21236/ad0401458
[research_edwards_1983]: https://doi.org/10.2514/3.44863
[research_edwards_1992]: https://doi.org/10.2514/6.1992-4002
[research_edwards_wieseman_2003]: https://doi.org/10.2514/6.2003-1489
[research_edwards_wieseman_2008]: https://doi.org/10.2514/1.30078
[research_effective_torsional_1976]: https://doi.org/10.14359/11098
[research_effects_of_1988]: https://doi.org/10.1016/0010-4361(88)90589-7
[research_efremov_efremov_2020]: https://doi.org/10.2514/1.g004409
[research_efremov_shcherbakov_2022]: https://doi.org/10.34759/vst-2022-1-201-210
[research_ehlers_weisshaar_1993]: https://doi.org/10.2514/3.46376
[research_eichler_1970]: https://doi.org/10.2514/3.44170
[research_ekaterinarisja_schifflewisb_1990]: https://ntrs.nasa.gov/citations/19900058795
[research_ekaterinarisja_schifflewisb_1994]: https://ntrs.nasa.gov/citations/19950037635
[research_elenchezhiyan_kumar_2025]: https://doi.org/10.1017/aer.2025.10069
[research_elham_2015]: https://doi.org/10.1016/j.ast.2014.12.024
[research_elham_vantooren_2016]: https://doi.org/10.1007/s00158-016-1447-9
[research_elham_vantooren_2016_b]: https://doi.org/10.1007/s00158-016-1613-0
[research_elmahdy_ali_2025]: https://doi.org/10.1038/s41598-025-99500-z
[research_elsalamony_aziz_2020]: https://doi.org/10.1142/s2301385021500138
[research_elshazly_kassem_2025]: https://doi.org/10.1088/1742-6596/3070/1/012001
[research_elyasi_roudbari_2020]: https://doi.org/10.1007/s40430-020-02633-7
[research_enciu_2019]: https://doi.org/10.7763/ijmo.2019.v9.729
[research_eney_1968]: https://doi.org/10.2514/3.43938
[research_engellandsa_franklinja_1992]: https://ntrs.nasa.gov/citations/19930029331
[research_enns_2003]: https://doi.org/10.21236/ada411755
[research_enns_ozbay_1992]: https://doi.org/10.2514/3.20863
[research_eraslan_oktay_2023]: https://doi.org/10.5755/j01.itc.52.4.33527
[research_erel_1988]: https://doi.org/10.2514/3.45535
[research_erel_seginer_1985]: https://doi.org/10.2514/3.45180
[research_ericksongarye_2003]: https://ntrs.nasa.gov/citations/20040016158
[research_eriksson_1990]: https://doi.org/10.1177/002199839002401201
[research_esfahani_webb_2018]: https://doi.org/10.1007/s00348-018-2588-y
[research_eugeneltu_1996]: https://ntrs.nasa.gov/citations/19960047050
[research_evald_hollweg_2023]: https://doi.org/10.1002/acs.3628
[research_ewing_hinger_1988]: https://doi.org/10.1016/0263-8223(88)90050-5
[research_experimental_investigation_2023]: https://doi.org/10.1063/5.0147213
[research_fadel_rabie_2019]: https://doi.org/10.18280/jesa.520307
[research_fan_2026]: https://doi.org/10.1109/iceaai68945.2026.11442354
[research_fan_jiang_2026]: https://doi.org/10.1108/aeat-01-2026-0033
[research_fan_wang_2023]: https://doi.org/10.1002/rnc.7006
[research_fan_wang_2025]: https://doi.org/10.3390/aerospace12090784
[research_fan_yu_2021]: https://doi.org/10.2514/1.c036138
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
[research_farsadi_ahmadi_2024]: https://doi.org/10.3390/aerospace11030193
[research_farsadi_ahmadi_2026]: https://doi.org/10.2514/1.j066652
[research_farsadi_rahmanian_2020]: https://doi.org/10.1016/j.jfluidstructs.2019.102812
[research_fatigue_behaviour_1977]: https://doi.org/10.1016/0010-4361(77)90034-9
[research_faure_dumas_2019]: https://doi.org/10.1016/j.apm.2018.12.013
[research_favaro_rylko_2025]: https://doi.org/10.3390/aerospace12060559
[research_favier_maresca_1987]: https://doi.org/10.2514/3.45497
[research_fazeli_stokesgriffin_2022]: https://doi.org/10.1016/j.compstruct.2022.115756
[research_fazilati_khalafi_2019]: https://doi.org/10.1177/0731684419854800
[research_fazilati_khalafi_2019_b]: https://doi.org/10.1016/j.tws.2019.106287
[research_fearnside_1962]: https://doi.org/10.1108/eb033507
[research_fedorenko_bondarenko_2024]: https://doi.org/10.20535/0203-3771472024307685
[research_fehrs_kaiser_2025]: https://doi.org/10.1007/s13272-025-00856-9
[research_feil_pflumm_2020]: https://doi.org/10.1016/j.compstruct.2020.112755
[research_feldt_herrmann_1974]: https://doi.org/10.1016/0016-0032(74)90123-9
[research_feliubatlle_2016]: https://doi.org/10.1002/rnc.3677
[research_feng_2023]: https://doi.org/10.54254/2753-8818/11/20230408
[research_feng_guo_2023]: https://doi.org/10.2514/1.g007591
[research_feng_liu_2024]: https://doi.org/10.1109/tim.2024.3366272
[research_feng_wang_2021]: https://doi.org/10.1016/j.ast.2021.106938
[research_feroskhan_go_2016]: https://doi.org/10.1016/j.ast.2016.01.005
[research_feroskhan_go_2018]: https://doi.org/10.1016/j.ast.2017.11.002
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
[research_finkleman_1972]: https://doi.org/10.2514/3.59003
[research_fisher_richwine_1992]: https://ntrs.nasa.gov/citations/19930002344
[research_flax_1943]: https://doi.org/10.2514/8.10981
[research_fleming_kushner_1994]: https://doi.org/10.21236/ada281219
[research_flight_performance_1963]: https://doi.org/10.1016/0016-0032(63)90546-5
[research_flight_test_2016]: https://doi.org/10.21535/dnk59q51
[research_flightscienceslabincbuffalony_1964]: https://doi.org/10.21236/ad0442900
[research_florancejamesr_heegjennifer_2004]: https://ntrs.nasa.gov/citations/20040066092
[research_flores_bazan_2025]: https://doi.org/10.1002/asjc.70025
[research_fontana_piperni_2024]: https://doi.org/10.2514/1.j063533
[research_fonte_ricci_2015]: https://doi.org/10.2514/1.c032995
[research_ford_1989]: https://doi.org/10.1108/eb036732
[research_fortis_fortis_2015]: https://doi.org/10.1504/ijais.2015.072146
[research_fournier_massioni_2022]: https://doi.org/10.2514/1.g006084
[research_fraihat_ajaj_2024]: https://doi.org/10.1017/aer.2024.16
[research_franco_rios_2022]: https://doi.org/10.1002/acs.3399
[research_francois_cooper_2017]: https://doi.org/10.12989/aas.2017.4.2.093
[research_franklin_innis_1978]: https://doi.org/10.2514/3.58306
[research_franklinja_innisrc_1972]: https://ntrs.nasa.gov/citations/19770026207
[research_franklinjamesa_1993]: https://ntrs.nasa.gov/citations/19940006662
[research_franklinjamesa_stortzmichaelw_1990]: https://ntrs.nasa.gov/citations/19920062696
[research_fratello_croom_1987]: https://ntrs.nasa.gov/citations/19870062335
[research_frei_1982]: https://ntrs.nasa.gov/citations/19820017333
[research_fresconi_celmins_2014]: https://doi.org/10.21236/ada593328
[research_freudingerlawrencec_1989]: https://ntrs.nasa.gov/citations/19900002416
[research_freudingerlawrencec_kehoemichaelw_1990]: https://ntrs.nasa.gov/citations/19900015819
[research_friedmann_1998]: https://doi.org/10.21236/ada351094
[research_friendel_sakamotogm_1978]: https://ntrs.nasa.gov/citations/19790004885
[research_frost_rutherford_1963]: https://doi.org/10.2514/3.1680
[research_fu_yang_2021]: https://doi.org/10.1038/s41598-021-95187-0
[research_fujii_1985]: https://doi.org/10.2322/jjsass1969.33.339
[research_fukunaga_1990]: https://doi.org/10.1177/002199839002400504
[research_fukunaga_sekine_1993]: https://doi.org/10.1299/kikaia.59.2343
[research_fukunaga_sekine_1994]: https://doi.org/10.1177/002199839402800802
[research_fung_1982]: https://doi.org/10.21236/ada215096
[research_fung_doong_1988]: https://doi.org/10.1016/0263-8223(88)90043-8
[research_furtado_catalanotti_2019]: https://doi.org/10.1016/j.compstruct.2019.111168
[research_furtat_gushchin_2021]: https://doi.org/10.1109/access.2021.3056942
[research_fuzzy_logic_1991]: https://doi.org/10.1109/37.88591
[research_gabrys_steffensen_2019]: https://doi.org/10.1016/j.ifacol.2019.11.281
[research_gainer_1963]: https://doi.org/10.21236/ad0404850
[research_galasso_ciminello_2024]: https://doi.org/10.3390/s24165216
[research_galffy_bock_2019]: https://doi.org/10.1016/j.conengprac.2019.03.006
[research_galiana_moradi_2024]: https://doi.org/10.1177/14759217241247766
[research_gallagher_1971]: https://doi.org/10.2514/3.59189
[research_gamagedara_lee_2024]: https://doi.org/10.1016/j.conengprac.2023.105791
[research_gao_cai_2016]: https://doi.org/10.1016/j.cja.2016.06.014
[research_gao_gao_2019]: https://doi.org/10.1109/access.2019.2917316
[research_gao_jiang_2025]: https://doi.org/10.1017/aer.2025.41
[research_gao_liu_2024]: https://doi.org/10.1016/j.ast.2024.109671
[research_gao_ma_2021]: https://doi.org/10.32604/sdhm.2021.013737
[research_gao_wu_2017]: https://doi.org/10.1177/1475921717717312
[research_garabedianpr_1979]: https://ntrs.nasa.gov/citations/19790011863
[research_garciahernandez_cuernorejado_2017]: https://doi.org/10.1109/access.2017.2758903
[research_gargsanjay_schmidtdavidk_1988]: https://ntrs.nasa.gov/citations/19880063045
[research_garmendia_mavris_2016]: https://doi.org/10.2514/1.c033184
[research_garner_wu_2023]: https://doi.org/10.1007/s00158-023-03678-7
[research_garrard_low_1990]: https://doi.org/10.21236/ada231588
[research_garrickie_rubinowsi_1946]: https://ntrs.nasa.gov/citations/19930081835
[research_garrickie_rubinowsi_1946_b]: https://ntrs.nasa.gov/citations/19930090942
[research_gaurav_sekou_2023]: https://doi.org/10.1051/e3sconf/202344606005
[research_gavra_vankampen_2024]: https://doi.org/10.2514/1.g008112
[research_geisler_junker_2024]: https://doi.org/10.1016/j.probengmech.2024.103618
[research_gelos_laura_1990]: https://doi.org/10.1016/0003-682x(90)90014-l
[research_geng_zhao_2026]: https://doi.org/10.1016/j.addma.2026.105207
[research_geoghegan_giannelis_2020]: https://doi.org/10.3390/fluids5020046
[research_gera_1986]: https://ntrs.nasa.gov/citations/19860009842
[research_gera_andrisani_1987]: https://ntrs.nasa.gov/citations/19870035296
[research_gera_andrisani_1989]: https://ntrs.nasa.gov/citations/19890040365
[research_gerdes_hynes_1972]: https://doi.org/10.4050/jahs.17.47
[research_gerken_1979]: https://doi.org/10.21236/ada132587
[research_ghalandari_mahariq_2022]: https://doi.org/10.32604/cmc.2022.020884
[research_ghasemikaram_mazidi_2021]: https://doi.org/10.1142/s021945542250016x
[research_ghazi_alhazmi_2022]: https://doi.org/10.1080/10618562.2022.2138863
[research_giannakeas_sharifkhodaei_2022]: https://doi.org/10.1177/14759217221095415
[research_gibson_1999]: https://doi.org/10.21236/ada386878
[research_giese_reich_1996]: https://doi.org/10.21236/ada399629
[research_gilbert_schmidt_1982]: https://doi.org/10.2514/6.1982-1544
[research_gilbert_schmidt_1984]: https://doi.org/10.2514/3.8566
[research_gilbert_schneider_1981]: https://doi.org/10.1177/002199838101500106
[research_gilbertmichaelg_1987]: https://ntrs.nasa.gov/citations/19870009427
[research_giles_1972]: https://doi.org/10.2514/3.58942
[research_gill_1995]: https://doi.org/10.21236/ada305293
[research_glbbings_1969]: https://doi.org/10.2514/3.48096
[research_glezer_leonard_2012]: https://doi.org/10.21236/ada564094
[research_gloss_washburn_1978]: https://doi.org/10.2514/3.58347
[research_glossbb_washburnke_1977]: https://ntrs.nasa.gov/citations/19770060346
[research_godwin_frazier_1964]: https://doi.org/10.21236/ad0613504
[research_goel_roy_2021]: https://doi.org/10.1109/lcsys.2020.3045086
[research_goizueta_wynn_2022]: https://doi.org/10.2514/1.j062050
[research_goizueta_wynn_2022_b]: https://doi.org/10.2514/1.c036710
[research_goland_1945]: https://doi.org/10.1115/1.4009489
[research_golmirzaee_wood_2026]: https://doi.org/10.1186/s42774-025-00222-7
[research_golombek_bustamante_2026]: https://doi.org/10.1007/s13272-026-00996-6
[research_gong_he_2026]: https://doi.org/10.1016/j.probengmech.2026.103892
[research_gong_wang_2019]: https://doi.org/10.1007/s11071-019-04834-9
[research_gong_wang_2019_b]: https://doi.org/10.1177/0020294019830434
[research_gong_xu_2024]: https://doi.org/10.1016/j.ast.2024.108875
[research_gonzalez_silvestre_2020]: https://doi.org/10.2514/1.j058692
[research_gonzalezmontijo_vanness_2026]: https://doi.org/10.1016/j.marstruc.2025.103924
[research_goodrichkennethh_sliwastevenm_1989]: https://ntrs.nasa.gov/citations/19890014097
[research_goradiash_bobbittpj_1989]: https://ntrs.nasa.gov/citations/19910014825
[research_gorman_singhal_1993]: https://doi.org/10.1006/jsvi.1993.1135
[research_govindaraj_rynaski_1979]: https://doi.org/10.21236/ada074092
[research_govoni_cristofaro_2023]: https://doi.org/10.1109/lcsys.2023.3324565
[research_graftonsb_gilberwp_1982]: https://ntrs.nasa.gov/citations/19820055564
[research_grant_stol_2015]: https://doi.org/10.2514/1.g000826
[research_granthamwd_nguyenlt_1976]: https://ntrs.nasa.gov/citations/19770011064
[research_grauerjareda_bouchermatthewj_2017]: https://ntrs.nasa.gov/citations/20170001227
[research_graves_sawicki_1994]: https://doi.org/10.1016/0263-8223(94)90088-4
[research_gray_kennedy_2025]: https://doi.org/10.1007/s00158-025-04181-x
[research_gray_mei_1993]: https://doi.org/10.2514/3.49051
[research_gray_riso_2023]: https://doi.org/10.2514/1.j062127
[research_green_1987]: https://doi.org/10.2514/3.45525
[research_greenbergharry_sternfieldleonard_1944]: https://ntrs.nasa.gov/citations/19960024284
[research_greene_1928]: https://doi.org/10.1115/1.4058514
[research_greenhalgh_pastore_1993]: https://doi.org/10.1016/0956-7143(93)90004-r
[research_greenja_1986]: https://ntrs.nasa.gov/citations/19860054140
[research_grenestedt_1989]: https://doi.org/10.1016/0263-8223(89)90076-7
[research_greszczuk_chao_1975]: https://doi.org/10.21236/ada012269
[research_griffin_eastep_1981]: https://doi.org/10.2514/6.1981-637
[research_griffin_eastep_1982]: https://doi.org/10.2514/3.61570
[research_griffin_haerter_1983]: https://doi.org/10.21236/ada133188
[research_griffinbrianjoseph_burkenjohnj_2010]: https://ntrs.nasa.gov/citations/20100037212
[research_griffincharlesf_harvillwilliame_1988]: https://ntrs.nasa.gov/citations/19910019939
[research_griffis_masumura_1981]: https://doi.org/10.1177/002199838101500503
[research_grifo_gulizzi_2023]: https://doi.org/10.1016/j.compstruct.2023.117315
[research_grigolyuk_kulikov_1990]: https://doi.org/10.1007/bf00851843
[research_groh_wu_2022]: https://doi.org/10.2514/1.j061755
[research_gross_clark_2017]: https://doi.org/10.2514/1.i010471
[research_gruenwald_yucelen_2020]: https://doi.org/10.1002/acs.3095
[research_gssssv_2020]: https://doi.org/10.5373/jardcs/v12sp4/20201597
[research_gu_ducvo_2023]: https://doi.org/10.2514/1.c036702
[research_gu_hong_2020]: https://doi.org/10.1088/1742-6596/1600/1/012013
[research_gu_taghipour_2022]: https://doi.org/10.1016/j.compstruct.2022.116151
[research_gu_zhou_2020]: https://doi.org/10.2514/1.c035833
[research_gu_zhou_2022]: https://doi.org/10.2514/1.c036508
[research_guderley_1956]: https://doi.org/10.2514/8.3697
[research_guimaraes_castro_2019]: https://doi.org/10.2514/1.j057282
[research_guimaraes_silva_2020]: https://doi.org/10.2514/1.j059106
[research_guinnwileya_1984]: https://ntrs.nasa.gov/citations/19870008278
[research_guinnwileya_risingjerryj_1984]: https://ntrs.nasa.gov/citations/19870008280
[research_guinnwileya_willeycraigs_1983]: https://ntrs.nasa.gov/citations/19870008279
[research_gunnink_1988]: https://doi.org/10.1016/0263-8223(88)90062-1
[research_guo_2021]: https://doi.org/10.1088/1742-6596/1877/1/012019
[research_guo_2021_b]: https://doi.org/10.1088/1742-6596/1877/1/012022
[research_guo_bai_2017]: https://doi.org/10.1360/n092016-00362
[research_guo_hou_2017]: https://doi.org/10.1109/access.2017.2743059
[research_guo_jing_2017]: https://doi.org/10.1016/j.ast.2017.08.008
[research_guo_li_2021]: https://doi.org/10.1007/s00158-021-02888-1
[research_guo_liu_2026_b]: https://doi.org/10.1007/s42401-026-00489-8
[research_guo_wang_1988]: https://doi.org/10.21236/ada191553
[research_guo_wang_2025]: https://doi.org/10.1016/j.ast.2025.109966
[research_guo_zhang_2022]: https://doi.org/10.32604/cmes.2022.020638
[research_guo_zhou_2020]: https://doi.org/10.3390/electronics9020364
[research_gupta_1998]: https://doi.org/10.21236/ada397678
[research_gupta_2023]: https://doi.org/10.61653/joast.v68i4.2016.368
[research_gupta_brenner_1987]: https://ntrs.nasa.gov/citations/19870046442
[research_gupta_brenner_1989]: https://ntrs.nasa.gov/citations/19890036940
[research_gurdal_2002]: https://doi.org/10.21236/ada402571
[research_gurdal_haftka_1999]: https://doi.org/10.21236/ada387245
[research_gurleyjrjr_ruhlincl_1962]: https://ntrs.nasa.gov/citations/19660025705
[research_guruswamy_2019]: https://doi.org/10.1016/j.ifacsc.2019.100057
[research_guruswamy_goorjian_1987]: https://doi.org/10.2514/3.45508
[research_guruswamy_tu_1989]: https://doi.org/10.2514/3.45820
[research_gwin_1976]: https://doi.org/10.2514/3.58668
[research_gwinlb_1974]: https://ntrs.nasa.gov/citations/19740045423
[research_haas_chopra_1988]: https://doi.org/10.2514/3.45684
[research_haas_chopra_1990]: https://doi.org/10.2514/3.45937
[research_haase_aslund]: https://doi.org/10.1007/978-3-540-39507-2_34
[research_had_ruzicka_2016]: https://doi.org/10.1016/j.compstruct.2015.09.009
[research_hadidoolabi_ansarian_2017]: https://doi.org/10.24200/sci.2017.4246
[research_hadidoolabi_ansarian_2018]: https://doi.org/10.1007/s40430-018-1021-z
[research_haeri_fadaee_2016]: https://doi.org/10.1016/j.compstruct.2016.04.013
[research_haftka_1977]: https://doi.org/10.2514/3.7400
[research_hagnell_langbeck_2016]: https://doi.org/10.1016/j.compstruct.2016.06.032
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
[research_hamissi_bouzid_2019]: https://doi.org/10.1016/j.ifacol.2019.11.260
[research_hammer_bright_1998]: https://doi.org/10.21236/ada359476
[research_han_cheng_2023]: https://doi.org/10.1016/j.neucom.2023.126789
[research_han_pei_2026]: https://doi.org/10.1109/maes.2025.3566023
[research_han_yang_2024]: https://doi.org/10.1109/access.2024.3411015
[research_hanazaki_yamazaki_2024]: https://doi.org/10.3390/aerospace11010064
[research_hancock_1971]: https://doi.org/10.2514/3.59157
[research_hancock_1972]: https://doi.org/10.1017/s0001924000044055
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
[research_harper_robertp_1955]: https://doi.org/10.21236/ad0092496
[research_harpur_1968]: https://doi.org/10.2514/3.43926
[research_harriscd_1974]: https://ntrs.nasa.gov/citations/19830002756
[research_harriscd_1974_b]: https://ntrs.nasa.gov/citations/19830002761
[research_hart_1956]: https://doi.org/10.21236/ad0108104
[research_harvillwe_kizerja_1976]: https://ntrs.nasa.gov/citations/19770004089
[research_hatake_1985]: https://doi.org/10.1299/kikaic.51.1897
[research_hatake_1986]: https://doi.org/10.1299/jsme1958.29.1225
[research_hayase_1974]: https://doi.org/10.21236/ada002866
[research_hayashi_1949]: https://doi.org/10.2534/jjasnaoe1903.1949.85
[research_he_tan_2020]: https://doi.org/10.1109/access.2020.3035436
[research_he_wang_2023]: https://doi.org/10.1155/2023/1711088
[research_hebbar_pashilkar_2016]: https://doi.org/10.14429/dsj.66.9196
[research_heckl_lyon_1962]: https://doi.org/10.21236/ad0290798
[research_heegjennifer_2006]: https://ntrs.nasa.gov/citations/20060018311
[research_heegjennifer_spaincharlesv_2004]: https://ntrs.nasa.gov/citations/20040068163
[research_heegjennifer_spaincharlesv_2005]: https://ntrs.nasa.gov/citations/20050203672
[research_heersink_sylla_2022]: https://doi.org/10.1109/lcsys.2021.3119258
[research_heinrich_vogt_2022]: https://doi.org/10.2514/1.g006412
[research_hemsch_1989]: https://doi.org/10.2514/3.45723
[research_hemsch_nielsen_1983]: https://doi.org/10.2514/3.25606
[research_henriquezhuecas_white_2022]: https://doi.org/10.4050/jahs.67.032007
[research_henry_1961]: https://doi.org/10.21236/ad0273328
[research_henschel_chetty_1989]: https://doi.org/10.2514/3.20415
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
[research_hildebrandfrancisb_reissnereric_1944]: https://ntrs.nasa.gov/citations/19930084742
[research_hilger_ritter_2021]: https://doi.org/10.3390/aerospace8100308
[research_hill_1987]: https://doi.org/10.21236/ada186949
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
[research_hobbs_mote_2023]: https://doi.org/10.1109/mcs.2023.3234380
[research_hodges_2004]: https://doi.org/10.21236/ada424568
[research_hodgins_freeman_2025]: https://doi.org/10.1080/00207179.2025.2513674
[research_hodgkinson_2017]: https://doi.org/10.4050/jahs.62.047001
[research_hodgkinson_lamanna_1976]: https://doi.org/10.1017/s0001924000033510
[research_hogan_rinde_1978]: https://doi.org/10.21236/ada062030
[research_hoh_mitchell_1983]: https://doi.org/10.21236/ada132857
[research_hollowell_dugundji_1982]: https://doi.org/10.2514/6.1982-722
[research_hollowell_dugundji_1984]: https://doi.org/10.2514/3.48224
[research_holst_brown_1983]: https://doi.org/10.2514/3.8069
[research_honeycomb_laminate_composite_1979]: https://doi.org/10.1016/0010-4361(79)90475-0
[research_hong_cheong_1993]: https://doi.org/10.1016/0013-7944(93)90174-q
[research_hongyan_xiaoyong_2026]: https://doi.org/10.1109/access.2026.3692889
[research_hoogervorst_elham_2017]: https://doi.org/10.1016/j.ast.2017.02.012
[research_hope_kunz_2019]: https://doi.org/10.2514/1.j057456
[research_hopkinsej_yeesc_1977]: https://ntrs.nasa.gov/citations/19770014154
[research_hopwood_gresham_2023]: https://doi.org/10.2514/1.g007016
[research_horowitz_golubev_1980]: https://doi.org/10.21236/ada082424
[research_horsburgh_1911]: https://doi.org/10.1017/s0013091500033976
[research_horton_mayers_1965]: https://doi.org/10.21236/ad0622585
[research_hortsen_boer_1983]: https://doi.org/10.21236/ada130488
[research_hoseini_hodges_2019]: https://doi.org/10.2514/1.c035098
[research_hou_2025]: https://doi.org/10.1007/978-981-96-6235-7_5
[research_housnerjm_steinm_1974]: https://ntrs.nasa.gov/citations/19740024243
[research_houtman_timme_2023]: https://doi.org/10.1017/flo.2023.8
[research_houzibe_chaki_2026]: https://doi.org/10.1177/14759217261453871
[research_how_2004]: https://doi.org/10.21236/ada420937
[research_howard_oleary_1994]: https://doi.org/10.2514/3.46578
[research_howdyshell_trovillion_1998]: https://doi.org/10.21236/ada354825
[research_hozic_thore_2023]: https://doi.org/10.1016/j.compstruct.2023.117336
[research_hu_1984]: https://doi.org/10.1016/0045-7949(84)90204-9
[research_hu_2022]: https://doi.org/10.3390/aerospace9030154
[research_hu_an_2025]: https://doi.org/10.1063/5.0258928
[research_hu_traisnel_2026]: https://doi.org/10.2139/ssrn.6790318
[research_hu_yang_2016]: https://doi.org/10.1016/j.jsv.2015.11.043
[research_hua_wang_2025]: https://doi.org/10.3390/aerospace12040327
[research_huang_li_2026]: https://doi.org/10.2514/1.c038842
[research_huang_wang_2016]: https://doi.org/10.1016/j.compstruct.2016.06.043
[research_huang_wang_2024]: https://doi.org/10.1007/s00158-024-03809-8
[research_huang_yang_2018]: https://doi.org/10.1016/j.cja.2017.12.014
[research_huang_yang_2019]: https://doi.org/10.2514/1.j058211
[research_huang_yu_2022]: https://doi.org/10.2514/1.j060923
[research_huang_zhen_2023]: https://doi.org/10.1109/tac.2023.3241282
[research_huang_zheng_2024]: https://doi.org/10.1016/j.ijnonlinmec.2024.104692
[research_hubener_luckner_2026]: https://doi.org/10.1007/s13272-025-00930-2
[research_hubler_nissle_2016]: https://doi.org/10.1007/s13272-016-0209-0
[research_huff_ww_1949]: https://doi.org/10.21236/ad0035641
[research_huffmanjk_1975]: https://ntrs.nasa.gov/citations/19750019955
[research_hui_1986]: https://doi.org/10.1016/0020-7683(86)90100-9
[research_hummel_oelker_1994]: https://doi.org/10.2514/3.46573
[research_humphreysjennings_lappas_2020]: https://doi.org/10.3390/aerospace7050051
[research_hunn_1953]: https://doi.org/10.1017/s0368393100131128
[research_huo_duan_2021]: https://doi.org/10.1142/s2301385021410053
[research_hurley_1975]: https://doi.org/10.2514/3.49684
[research_hwu_tsai_2002]: https://doi.org/10.2514/2.2945
[research_hybrid_composite_1978]: https://doi.org/10.1016/0010-4361(78)90462-7
[research_iannelli_marcos_2017]: https://doi.org/10.1002/rnc.3878
[research_iannelli_marcos_2018]: https://doi.org/10.2514/1.g003165
[research_ibrahim_2026]: https://doi.org/10.22161/ijebm.10.2.9
[research_ibren_sulaeman_2020]: https://doi.org/10.37934/cfdl.12.4.7989
[research_ignatyev_khrabrov_2018]: https://doi.org/10.3390/aerospace5010026
[research_ijaz_hamayun_2019]: https://doi.org/10.1007/s12555-017-0399-1
[research_ijaz_hamayun_2019_b]: https://doi.org/10.1177/0142331219835589
[research_ilcewiczlb_walkerth_1991]: https://ntrs.nasa.gov/citations/19940028357
[research_iliff_wang_1996]: https://ntrs.nasa.gov/citations/19970004545
[research_iliffkw_mainere_1978]: https://ntrs.nasa.gov/citations/19780010132
[research_immersion_and_2026]: https://doi.org/10.66967/jaics.2026.v2i104
[research_inan_aliskan_2025]: https://doi.org/10.29130/dubited.1595224
[research_ingramwc_yiplp_1986]: https://ntrs.nasa.gov/citations/19870026764
[research_interlaminar_shear_1992]: https://doi.org/10.1016/0010-4361(92)90207-b
[research_invernizzi_lovera_2018]: https://doi.org/10.1016/j.automatica.2018.05.024
[research_ioannis_ioannis_2026]: https://doi.org/10.70322/dav.2026.10005
[research_iovnovich_nahom_2018]: https://doi.org/10.2514/1.c034716
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
[research_jackuliak_bugaj_2026]: https://doi.org/10.23919/ntca68808.2026.11524172
[research_jacobson_joshi_1977]: https://doi.org/10.2514/3.44591
[research_jacobson_joshi_1978]: https://doi.org/10.2514/3.58351
[research_jacome_elham_2018]: https://doi.org/10.1007/s13272-018-0342-z
[research_jaeger_hendry_1959]: https://doi.org/10.1680/iicep.1959.12063
[research_jaffarsyedmohamedali_shahzatulsakinahbintiharon_2021]: https://doi.org/10.37934/cfdl.13.11.7886
[research_jagana_rajagopalan_2026]: https://doi.org/10.1002/aic.70222
[research_jajarmi_hajipour_2016]: https://doi.org/10.1002/asjc.1371
[research_jalalnezhad_2026]: https://doi.org/10.1007/s40430-025-06274-6
[research_jamesafranklin_1993]: https://ntrs.nasa.gov/citations/19940008824
[research_janardhan_grandhi_2003]: https://doi.org/10.21236/ada417106
[research_jang_ahn_2022]: https://doi.org/10.3390/app12199436
[research_jaredagrauer_2018]: https://ntrs.nasa.gov/citations/20190000878
[research_jarrellrelliott_1976]: https://ntrs.nasa.gov/citations/19770045950
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
[research_jenksge_henryhf_1977]: https://ntrs.nasa.gov/citations/19770014139
[research_jenney_schreadley_1982]: https://doi.org/10.21236/ada117244
[research_jenney_schreadley_1984]: https://doi.org/10.21236/ada144283
[research_jensen_crawley_1982]: https://doi.org/10.1177/073168448200100305
[research_jensen_crawley_1984]: https://doi.org/10.2514/3.48463
[research_jensen_falby_1966]: https://doi.org/10.21236/ad0486295
[research_jeon_choi_2025]: https://doi.org/10.3390/math13050738
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
[research_jia_feng_2026]: https://doi.org/10.30919/es2092
[research_jia_sun_2023]: https://doi.org/10.3390/drones7030200
[research_jiang_li_2018]: https://doi.org/10.1016/j.matdes.2018.03.028
[research_jiang_li_2024]: https://doi.org/10.1007/s11071-024-10134-8
[research_jiang_liu_2024]: https://doi.org/10.3390/act13060227
[research_jiang_tian_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000875
[research_jiang_tian_2019]: https://doi.org/10.1016/j.ast.2019.03.043
[research_jiang_tong_2022]: https://doi.org/10.1088/1742-6596/2235/1/012001
[research_jiang_zhang_2011]: https://doi.org/10.1109/ical.2011.6024717
[research_jianhong_2022]: https://doi.org/10.1108/aeat-08-2021-0254
[research_jianhong_ramirezmendoza_2023]: https://doi.org/10.1108/aeat-12-2022-0342
[research_jianhong_yanxiang_2026]: https://doi.org/10.1108/aeat-01-2025-0009
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
[research_johnson_1965]: https://doi.org/10.21236/ad0617567
[research_johnson_1972]: https://doi.org/10.21236/ad0754909
[research_johnson_1973]: https://doi.org/10.1016/0020-7683(73)90068-1
[research_johnson_henderson_1962]: https://doi.org/10.1016/s0020-7403(62)80002-2
[research_johnsonrw_junerr_1972]: https://ntrs.nasa.gov/citations/19720025911
[research_johnsonrw_mccartyje_1977]: https://ntrs.nasa.gov/citations/19770023236
[research_johnston_ashkenas_1974]: https://doi.org/10.21236/ada014366
[research_johnwhicks_jankania_1987]: https://ntrs.nasa.gov/citations/19870011558
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
[research_junyi_xinbing_2021]: https://doi.org/10.1088/1757-899x/1102/1/012004
[research_jusko_berger_2026]: https://doi.org/10.4050/jahs.71.022007
[research_k_deodhare_2023]: https://doi.org/10.61653/joast.v75i2.2023.58
[research_kabashkin_2024]: https://doi.org/10.3390/math12192979
[research_kaczmarek_2026]: https://doi.org/10.1016/j.neucom.2026.133215
[research_kafkas_kilimtzidis_2021]: https://doi.org/10.3390/aerospace8120398
[research_kai_2024]: https://doi.org/10.2514/1.g007917
[research_kakkar_streit_2026]: https://doi.org/10.3390/aerospace13020171
[research_kalam_1981]: https://doi.org/10.1080/01495738108909950
[research_kalam_seshaiah_2022]: https://doi.org/10.1016/j.matpr.2021.10.271
[research_kalinowski_2015]: https://doi.org/10.1515/meceng-2015-0003
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
[research_kannemans_1995]: https://doi.org/10.2514/6.1995-3434
[research_kano_ryuzono_2025]: https://doi.org/10.1016/j.ast.2025.110652
[research_kanou_ibuki_2025]: https://doi.org/10.1109/lcsys.2025.3647557
[research_kapania_bergen_1991]: https://doi.org/10.2514/3.59930
[research_kapania_issac_1994]: https://doi.org/10.2514/3.59995
[research_kapaniarakeshk_issacj_1997]: https://ntrs.nasa.gov/citations/19970021182
[research_karalmichael_2001]: https://ntrs.nasa.gov/citations/20010033249
[research_karimi_khorshidi_2022]: https://doi.org/10.1016/j.compstruct.2022.115630
[research_karimikelayeh_djavareshkian_2024]: https://doi.org/10.1061/jaeeez.aseng-5073
[research_karmah_2018]: https://doi.org/10.19080/raej.2018.02.555598
[research_karniadakis_2004]: https://doi.org/10.21236/ada420891
[research_karpouzian_1991]: https://doi.org/10.2514/3.10655
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
[research_kenway_martins_2016]: https://doi.org/10.2514/1.j054154
[research_kevrekidis_2002]: https://doi.org/10.21236/ada405411
[research_key_1971]: https://doi.org/10.21236/ad0725746
[research_key_1982]: https://doi.org/10.2514/3.57366
[research_khajah_natarajan_2023]: https://doi.org/10.1016/j.compstruct.2023.116748
[research_khalaf_gan_2017]: https://doi.org/10.1186/s40638-017-0068-0
[research_khalil_asaro_2022]: https://doi.org/10.2514/1.c036426
[research_khalil_bauknecht_2024]: https://doi.org/10.2514/1.c037503
[research_khalil_fezans_2020]: https://doi.org/10.1017/aer.2020.85
[research_khalil_poirel_2016]: https://doi.org/10.1016/j.jsv.2016.07.016
[research_khan_riccio_2024]: https://doi.org/10.1016/j.paerosci.2024.101021
[research_khani_abdalla_2017]: https://doi.org/10.1016/j.compstruct.2017.07.086
[research_khankalantary_rezaeeahvanouee_2021]: https://doi.org/10.1177/09596518211003400
[research_kharghani_mittelstedt_2022]: https://doi.org/10.1016/j.compstruct.2021.115139
[research_khargonekar_sivashankar_1991]: https://doi.org/10.1016/0167-6911(91)90082-p
[research_kheiri_riazat_2025]: https://doi.org/10.1017/aer.2025.10028
[research_khodaverdian_gohil_2025]: https://doi.org/10.1016/j.dche.2025.100262
[research_kholodar_2016]: https://doi.org/10.2514/1.c033772
[research_kholodar_2023]: https://doi.org/10.2514/1.c036846
[research_kida_1982]: https://doi.org/10.1002/zamm.19820620912
[research_kieffer_2006]: https://doi.org/10.21236/ada462805
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
[research_king_johnson_1986]: https://doi.org/10.2514/3.9448
[research_kirmse_2016]: https://doi.org/10.1088/0957-0233/27/5/054001
[research_kirsch_fathi_2025]: https://doi.org/10.1115/1.4071802
[research_kirsch_montagnier_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.102930
[research_kish_mosle_1997]: https://doi.org/10.21236/ada286959
[research_kishi_kanazaki_2016]: https://doi.org/10.4236/jfcmv.2016.41004
[research_kishi_kanazaki_2022]: https://doi.org/10.2514/1.c036422
[research_kisslinger_wendl_1971]: https://doi.org/10.21236/ad0727762
[research_kizildeniz_kiyak_2025]: https://doi.org/10.1108/aeat-03-2025-0127
[research_klafin_1988]: https://doi.org/10.2514/6.1988-4499
[research_klasztorny_nycz_2018]: https://doi.org/10.1016/j.compstruct.2017.10.046
[research_klein_viswanathan_1973]: https://doi.org/10.1007/bf01590797
[research_kleinrw_lapinsm_1982]: https://ntrs.nasa.gov/citations/19820036249
[research_klema_1981]: https://doi.org/10.21236/ada106000
[research_klepl_1995]: https://doi.org/10.2514/3.46702
[research_klimczyk_goraj_2019]: https://doi.org/10.1108/aeat-12-2017-0289
[research_klotzschem_1984]: https://ntrs.nasa.gov/citations/19870019180
[research_klyde_harris_2004]: https://doi.org/10.21236/ada426452
[research_knaussjf_stonerh_1982]: https://ntrs.nasa.gov/citations/19830039267
[research_knight_1982]: https://doi.org/10.1177/002199838201600206
[research_knoxseith_1963]: https://doi.org/10.21236/ad0438911
[research_ko_kang_2019]: https://doi.org/10.5139/jksas.2019.47.2.114
[research_kobelev_2019]: https://doi.org/10.1108/mmms-02-2018-0019
[research_kodama_1962]: https://doi.org/10.1109/tac.1962.1105413
[research_koenig_1984]: https://doi.org/10.21236/ada150667
[research_koh_kelly_1989]: https://doi.org/10.1520/jte11130j
[research_kohara_tomoeda_2016]: https://doi.org/10.1299/jsmecs.2016.54._1408-1_
[research_kohnhorst_magnacca_1980]: https://doi.org/10.21236/ada094688
[research_kolar_lile_1971]: https://doi.org/10.21236/ada377254
[research_kolb_montagnier_2019]: https://doi.org/10.2514/1.g003729
[research_komarov_zinchenko_2023]: https://doi.org/10.20535/0203-3771452023290873
[research_komnatska_bondarenko_2017]: https://doi.org/10.15407/usim.2017.04.024
[research_konar_mahesh_1974]: https://doi.org/10.21236/ada002320
[research_konatala_milz_2024]: https://doi.org/10.2514/1.g008321
[research_kong_jeon_2025]: https://doi.org/10.1177/14759217251339812
[research_kontogiannis_savill_2024]: https://doi.org/10.1016/j.ast.2024.109080
[research_koo_lee_1994]: https://doi.org/10.1016/0045-7949(94)90293-3
[research_kopecki_2016]: https://doi.org/10.1108/aeat-10-2012-0187
[research_kopecki_2021]: https://doi.org/10.1108/aeat-11-2020-0248
[research_kornev_ambrozhevich_2021]: https://doi.org/10.3103/s1068799821010049
[research_kosmodamianskii_mitrakov_1976]: https://doi.org/10.1007/bf00882705
[research_kosyanchuk_selvesyuk_2015]: https://doi.org/10.3846/16487788.2015.1015290
[research_kosyanchuk_zheltov_2021]: https://doi.org/10.1088/1742-6596/1864/1/012005
[research_kota_hetrick_1997]: https://doi.org/10.21236/ada361152
[research_kotitschke_rupprecht_2026]: https://doi.org/10.1007/s42401-026-00498-7
[research_kou_zhang_2021]: https://doi.org/10.1016/j.paerosci.2021.100725
[research_kousen_bendiksen_1994]: https://doi.org/10.2514/3.46644
[research_koyuncuoglu_he_2022]: https://doi.org/10.1016/j.ast.2022.107876
[research_krachmalnick_vetsch_1968]: https://doi.org/10.2514/3.43925
[research_kraftchristophercjr_reederjp_1948]: https://ntrs.nasa.gov/citations/20050028754
[research_kratochvil_valenta_2024]: https://doi.org/10.1007/s13272-024-00745-7
[research_krause_khargonekar_1990]: https://doi.org/10.21236/ada219259
[research_krener_2001]: https://doi.org/10.21236/ada430327
[research_kretov_tiniakov_2022]: https://doi.org/10.3390/aerospace9090497
[research_kriechbaum_stineman_1972]: https://doi.org/10.2514/3.58994
[research_krone_1980]: https://doi.org/10.2514/6.1980-1882
[research_krone_1980_b]: https://doi.org/10.2514/6.1980-3047
[research_kroo_1982]: https://doi.org/10.2514/3.61557
[research_kruger_klimmek_2014]: https://doi.org/10.1007/s13272-014-0117-0
[research_kruger_meddaikar_2022]: https://doi.org/10.3390/aerospace9100535
[research_krzywoblocki_1943]: https://doi.org/10.2514/8.11023
[research_kuang_hu_2025]: https://doi.org/10.1142/s0219455427501756
[research_kubiak_gliszczynski_2019]: https://doi.org/10.1016/j.compstruct.2019.111222
[research_kubica_livet_1995]: https://doi.org/10.1016/0967-0661(95)00119-f
[research_kuder_arrieta_2015]: https://doi.org/10.1016/j.compstruct.2014.11.061
[research_kulikov_2020]: https://doi.org/10.1007/s10958-020-04994-9
[research_kumar_asha_2025]: https://doi.org/10.1016/j.prostr.2025.08.045
[research_kumar_collini_2020]: https://doi.org/10.1016/j.addma.2020.101168
[research_kumar_kumar_2022]: https://doi.org/10.4018/ijsda.302634
[research_kumar_onkar_2019]: https://doi.org/10.1007/s11012-019-01061-9
[research_kumarshakya_sekharpadhee_2023]: https://doi.org/10.1016/j.matpr.2023.05.731
[research_kunaporn_singh_2014]: https://doi.org/10.2514/1.c031885
[research_kuojiun_pongjeu_1989]: https://doi.org/10.1016/0045-7949(89)90030-8
[research_kurade_venkatakrishnan_2021]: https://doi.org/10.1017/aer.2021.99
[research_kurita_koike_2013]: https://doi.org/10.2514/6.2013-967
[research_kurita_koike_2019]: https://doi.org/10.2322/tjsass.62.108
[research_kurzhalspr_1978]: https://ntrs.nasa.gov/citations/19790008693
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
[research_lang_li_2024]: https://doi.org/10.1016/j.ast.2024.109526
[research_lapinsm_kleinrw_1982]: https://ntrs.nasa.gov/citations/19820055547
[research_larsonrichardr_1987]: https://ntrs.nasa.gov/citations/19870007386
[research_laub_1991]: https://doi.org/10.21236/ada248481
[research_laura_viazzi_1985]: https://doi.org/10.1016/0029-8018(85)90008-3
[research_lavretsky_2019]: https://doi.org/10.2514/1.g004328
[research_lawrence_theodore_2018]: https://doi.org/10.1017/aer.2018.43
[research_le_2026]: https://doi.org/10.1007/s40435-026-02198-8
[research_lee_1977]: https://doi.org/10.21236/ada038281
[research_lee_1995]: https://doi.org/10.1017/s0001924000028815
[research_lee_2016]: https://doi.org/10.1115/1.4032301
[research_lee_cho_1991]: https://doi.org/10.1016/0045-7949(91)90084-y
[research_lee_cho_1991_b]: https://doi.org/10.2514/3.10656
[research_lee_eyi_1993]: https://doi.org/10.2514/3.46419
[research_lee_kim_1994]: https://doi.org/10.2514/3.46667
[research_lee_kim_1995]: https://doi.org/10.2514/3.46803
[research_lee_kim_2020]: https://doi.org/10.1007/s12555-018-9403-7
[research_lee_kim_2021]: https://doi.org/10.3390/aerospace8090257
[research_lee_ko_2009]: https://doi.org/10.2514/1.39352
[research_lee_ko_2018]: https://doi.org/10.1115/1.4039232
[research_lee_lee_1990]: https://doi.org/10.1016/0045-7949(90)90019-x
[research_lee_lee_2023]: https://doi.org/10.5139/jksas.2023.51.11.751
[research_lee_mall_1989]: https://doi.org/10.1177/002199838902300403
[research_lee_ohman_1984]: https://doi.org/10.2514/3.44987
[research_lee_sheikh_2025]: https://doi.org/10.1093/jcde/qwaf124
[research_lee_sheu_1994]: https://doi.org/10.1002/oca.4660150204
[research_lee_singh_2017]: https://doi.org/10.1007/s11071-016-3287-y
[research_lee_singh_2018]: https://doi.org/10.2514/1.g003087
[research_lee_snyder_2017]: https://doi.org/10.2514/1.g001742
[research_lee_tang_1989]: https://doi.org/10.2514/3.45785
[research_lee_yun_2022]: https://doi.org/10.1016/j.addma.2022.102627
[research_lehman_stearman_1977]: https://doi.org/10.21236/ada039245
[research_lei_bai_2019]: https://doi.org/10.1016/j.ast.2019.07.018
[research_lei_bai_2021]: https://doi.org/10.1016/j.ast.2021.107101
[research_lei_guo_2021]: https://doi.org/10.3390/machines9100243
[research_lei_wang_2020]: https://doi.org/10.21595/jve.2019.20968
[research_leicester_1970]: https://doi.org/10.1061/jmcea3.0001329
[research_leitch_stodieck_2024]: https://doi.org/10.2139/ssrn.4786120
[research_leitch_stodieck_2025]: https://doi.org/10.1016/j.compstruct.2025.119706
[research_lemaysp_batillsm_1988]: https://ntrs.nasa.gov/citations/19880053508
[research_lemley_1968]: https://doi.org/10.21236/ad0840550
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
[research_li_bai_2022]: https://doi.org/10.2514/1.c036413
[research_li_chen_2016]: https://doi.org/10.1007/s00158-016-1459-5
[research_li_daronch_2019]: https://doi.org/10.1016/j.ast.2019.105354
[research_li_dong_2018]: https://doi.org/10.1002/asjc.1841
[research_li_gong_2019]: https://doi.org/10.1016/j.jfluidstructs.2018.10.011
[research_li_guo_2016]: https://doi.org/10.1108/aeat-12-2013-0234
[research_li_he_2019]: https://doi.org/10.1016/j.ast.2019.06.008
[research_li_he_2024]: https://doi.org/10.1007/s11071-024-10600-3
[research_li_hu_2025]: https://doi.org/10.1016/j.ifacol.2025.11.380
[research_li_huang_2018]: https://doi.org/10.1177/1077546318810033
[research_li_ji_2025]: https://doi.org/10.1002/rnc.7925
[research_li_jin_2017]: https://doi.org/10.1016/j.ast.2016.11.029
[research_li_kou_2024]: https://doi.org/10.1016/j.jfluidstructs.2023.104055
[research_li_li_2025]: https://doi.org/10.1109/taes.2025.3596214
[research_li_liang_2014]: https://doi.org/10.1088/0957-0233/25/6/065202
[research_li_lin_2025]: https://doi.org/10.1002/acs.3967
[research_li_liu_2021]: https://doi.org/10.1051/jnwpu/20213950995
[research_li_liu_2021_b]: https://doi.org/10.1016/j.conengprac.2021.104938
[research_li_liu_2022]: https://doi.org/10.1007/s10846-022-01691-4
[research_li_liu_2023]: https://doi.org/10.1002/rnc.6641
[research_li_miranda_2026]: https://doi.org/10.1016/j.compstruct.2026.120662
[research_li_pak_2015]: https://doi.org/10.2514/1.c033044
[research_li_qian_2019]: https://doi.org/10.1007/978-981-13-3305-7_108
[research_li_qian_2024]: https://doi.org/10.3390/aerospace11121015
[research_li_qin_2020]: https://doi.org/10.1016/j.ast.2019.105622
[research_li_qin_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103407
[research_li_qin_2021_b]: https://doi.org/10.1016/j.ast.2021.106919
[research_li_qin_2022]: https://doi.org/10.3390/app122010537
[research_li_sanfelice_2016]: https://doi.org/10.1109/tcns.2015.2428351
[research_li_shen_2018]: https://doi.org/10.1109/access.2018.2883067
[research_li_shen_2026]: https://doi.org/10.3390/aerospace13040325
[research_li_shi_2021]: https://doi.org/10.3390/aerospace8070176
[research_li_shi_2025]: https://doi.org/10.1108/aeat-08-2024-0233
[research_li_shi_2025_b]: https://doi.org/10.1016/j.addma.2025.104639
[research_li_sun_2022]: https://doi.org/10.1109/access.2022.3157878
[research_li_wan_2021]: https://doi.org/10.3390/app112411800
[research_li_wang_2018]: https://doi.org/10.1016/j.ast.2018.01.001
[research_li_wang_2018_b]: https://doi.org/10.1360/sspma2018-00072
[research_li_wang_2020]: https://doi.org/10.1155/2020/5812129
[research_li_wang_2021]: https://doi.org/10.3390/app11020505
[research_li_wang_2021_b]: https://doi.org/10.1002/stc.2908
[research_li_wang_2021_c]: https://doi.org/10.1016/j.addma.2021.102063
[research_li_xiong_2025]: https://doi.org/10.1088/1742-6596/3044/1/012002
[research_li_xu_2026]: https://doi.org/10.3390/vibration9010008
[research_li_yang_2017]: https://doi.org/10.2514/1.c033670
[research_li_yang_2023]: https://doi.org/10.3390/aerospace10100866
[research_li_yoon_2026]: https://doi.org/10.1007/s00158-026-04296-9
[research_li_zhang_2018]: https://doi.org/10.1109/access.2018.2853145
[research_li_zhang_2021]: https://doi.org/10.1016/j.ast.2021.106639
[research_li_zhang_2021_b]: https://doi.org/10.2514/1.j059921
[research_li_zhang_2022]: https://doi.org/10.1016/j.ast.2021.107309
[research_li_zhang_2024]: https://doi.org/10.1080/0305215x.2024.2420746
[research_li_zhang_2024_b]: https://doi.org/10.3390/aerospace11121020
[research_li_zhang_2024_d]: https://doi.org/10.2514/1.j063387
[research_li_zhou_2024]: https://doi.org/10.1007/s12206-024-0901-7
[research_lian_cao_2026]: https://doi.org/10.5890/jand.2026.03.015
[research_liang_chen_2026]: https://doi.org/10.1016/j.measurement.2025.119491
[research_liang_gao_2024]: https://doi.org/10.1002/rnc.7559
[research_liang_ye_2025]: https://doi.org/10.3390/machines13060439
[research_liang_yin_2024]: https://doi.org/10.1016/j.camwa.2024.06.014
[research_liao_song_2021]: https://doi.org/10.1063/5.0076538
[research_liao_sun_1993]: https://doi.org/10.2514/3.11865
[research_libeskind_minecci_1973]: https://doi.org/10.21236/ada326073
[research_librescu_khdeir_1988]: https://doi.org/10.2514/3.10050
[research_librescu_maalawi_2009]: https://doi.org/10.1016/j.tws.2008.05.007
[research_librescu_simovich_1988]: https://doi.org/10.2514/3.45572
[research_librescu_song_1992]: https://doi.org/10.1016/0961-9526(92)90039-9
[research_librescu_thangjitham_1988]: https://doi.org/10.2514/6.1988-2209
[research_librescu_thangjitham_1989]: https://doi.org/10.4271/891056
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
[research_lindsay_jordan_1975]: https://doi.org/10.21236/ada009137
[research_liu_2018]: https://doi.org/10.1049/joe.2018.9016
[research_liu_2019]: https://doi.org/10.1177/0020294019858106
[research_liu_an_2018]: https://doi.org/10.1109/tmech.2018.2800089
[research_liu_bai_2017]: https://doi.org/10.2514/1.j055054
[research_liu_buss_2022]: https://doi.org/10.1002/rnc.6015
[research_liu_chen_2019]: https://doi.org/10.2514/1.c035338
[research_liu_chen_2023]: https://doi.org/10.1002/acs.3664
[research_liu_dong_2021]: https://doi.org/10.1016/j.cja.2020.04.026
[research_liu_featherston_2019]: https://doi.org/10.1016/j.compstruct.2018.12.054
[research_liu_featherston_2023]: https://doi.org/10.1016/j.compstruct.2023.116853
[research_liu_gao_2020]: https://doi.org/10.1016/j.jfluidstructs.2020.103098
[research_liu_gao_2020_b]: https://doi.org/10.1007/s11071-020-05553-2
[research_liu_gao_2023]: https://doi.org/10.3390/aerospace10050406
[research_liu_he_2018]: https://doi.org/10.3390/a11100163
[research_liu_huang_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000682
[research_liu_ji_2024]: https://doi.org/10.1007/s12555-022-0318-y
[research_liu_kan_2022]: https://doi.org/10.1016/j.addma.2021.102503
[research_liu_li_2023]: https://doi.org/10.1016/j.compstruct.2023.116817
[research_liu_li_2026]: https://doi.org/10.3390/electronics15163532
[research_liu_liu_2025]: https://doi.org/10.1016/j.compstruct.2025.119588
[research_liu_liu_2026]: https://doi.org/10.1016/j.jfranklin.2026.108625
[research_liu_luo_2018]: https://doi.org/10.1016/j.ast.2017.10.008
[research_liu_qian_2026]: https://doi.org/10.1016/j.ast.2026.112709
[research_liu_song_2016]: https://doi.org/10.1007/s00158-016-1546-7
[research_liu_sun_2016]: https://doi.org/10.1155/2016/1060574
[research_liu_sun_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000712
[research_liu_sun_2017_b]: https://doi.org/10.1016/j.ast.2017.10.006
[research_liu_sun_2022]: https://doi.org/10.3390/en15030787
[research_liu_tian_2019]: https://doi.org/10.1088/1757-899x/677/5/052056
[research_liu_toropov_2015]: https://doi.org/10.1007/s00158-015-1244-x
[research_liu_wang_2019]: https://doi.org/10.1016/j.jfluidstructs.2019.04.010
[research_liu_wang_2026]: https://doi.org/10.1016/j.cej.2026.180391
[research_liu_yang_2026]: https://doi.org/10.1002/rnc.70564
[research_liu_ye_2016]: https://doi.org/10.1002/acs.2693
[research_liu_zhang_2018]: https://doi.org/10.1016/j.sysconle.2018.07.012
[research_liu_zhang_2023]: https://doi.org/10.1016/j.ijmultiphaseflow.2022.104286
[research_liu_zhang_2024]: https://doi.org/10.1007/s00158-024-03755-5
[research_liu_zhao_2026]: https://doi.org/10.1038/s41598-026-48452-z
[research_liu_zheng_2025]: https://doi.org/10.2514/1.c038200
[research_liu_zhou_2023]: https://doi.org/10.1088/1742-6596/2658/1/012051
[research_livne_2018]: https://doi.org/10.2514/1.c034442
[research_liwesleyw_pakchangi_2014]: https://ntrs.nasa.gov/citations/20140010035
[research_lo_1978]: https://doi.org/10.21236/ada050578
[research_lo_1979]: https://doi.org/10.21236/ada077707
[research_lo_1980]: https://doi.org/10.21236/ada092386
[research_lo_1981]: https://doi.org/10.21236/ada113019
[research_lockwoodtaylor_1942]: https://doi.org/10.1108/eb030921
[research_lockwp_petersenwr_1975]: https://ntrs.nasa.gov/citations/19750010176
[research_loja_barbosa_2017]: https://doi.org/10.1016/j.compstruct.2017.09.046
[research_lokoswilliama_1990]: https://ntrs.nasa.gov/citations/19920053312
[research_lombardi_1995]: https://doi.org/10.2514/3.46804
[research_lombardi_morelli_1994]: https://doi.org/10.2514/3.46517
[research_lombardi_morelli_1996]: https://doi.org/10.2514/3.47077
[research_lombardi_salvetti_1997]: https://doi.org/10.2514/6.1997-1838
[research_lombardi_vicini_1994]: https://doi.org/10.1017/s0001924000049733
[research_lomo_patel_2023]: https://doi.org/10.1016/j.addma.2023.103891
[research_long_2019]: https://doi.org/10.1002/rnc.4539
[research_long_mu_2021]: https://doi.org/10.1016/j.compstruct.2020.113005
[research_loos_springer_1983]: https://doi.org/10.21236/ada130071
[research_loth_boyle_1969]: https://doi.org/10.21236/ad0704502
[research_lottati_1985]: https://doi.org/10.2514/3.45238
[research_lottati_1987]: https://doi.org/10.2514/3.45523
[research_lottati_1988]: https://doi.org/10.2514/3.45588
[research_loughlan_2019]: https://doi.org/10.1016/j.tws.2019.01.045
[research_loughlan_ata_1995]: https://doi.org/10.1016/0263-8223(95)00050-x
[research_lovejoyandrewe_scottistephenj_2019]: https://ntrs.nasa.gov/citations/20200002432
[research_lowe_1988]: https://doi.org/10.2514/3.45606
[research_lowson_1990]: https://doi.org/10.2514/3.25332
[research_lu_cao_2025]: https://doi.org/10.1007/s12555-025-0311-3
[research_lu_hong_2022]: https://doi.org/10.2514/1.g006219
[research_lu_hu_2019]: https://doi.org/10.1155/2019/1648576
[research_lu_ma_2019]: https://doi.org/10.1109/access.2019.2956818
[research_lu_murthy_1990]: https://doi.org/10.2514/3.45947
[research_lu_tian_2017]: https://doi.org/10.1016/j.cja.2017.03.003
[research_lu_vankampen_2016]: https://doi.org/10.1016/j.conengprac.2016.09.010
[research_lu_zhang_2015]: https://doi.org/10.1016/j.ssci.2014.12.005
[research_lu_zhang_2019]: https://doi.org/10.1016/j.cja.2019.09.010
[research_luattnguyen_williampgilbert_1980]: https://ntrs.nasa.gov/citations/19800020743
[research_lucarini_dirito_2025]: https://doi.org/10.3390/act14080407
[research_ludenacervantes_choi_2020]: https://doi.org/10.1007/s42405-020-00273-8
[research_lundry_1967]: https://doi.org/10.2514/3.43797
[research_lundry_1977]: https://doi.org/10.2514/3.44595
[research_lunghitano_afonso_2024]: https://doi.org/10.3390/app14062384
[research_lungu_lungu_2015]: https://doi.org/10.1016/j.ast.2015.07.005
[research_luo_ferrari_2024]: https://doi.org/10.1016/j.compositesb.2024.111739
[research_luo_zhang_2022]: https://doi.org/10.1109/access.2022.3175164
[research_lv_lei_2019]: https://doi.org/10.1088/1742-6596/1300/1/012085
[research_lyapunov_1993]: https://doi.org/10.1007/bf01051213
[research_lyu_cao_2018]: https://doi.org/10.1016/j.ast.2018.06.037
[research_lyu_kenway_2015]: https://doi.org/10.2514/1.j053318
[research_lyu_martins_2015]: https://doi.org/10.2514/1.c033116
[research_lyu_zhang_2019]: https://doi.org/10.1051/jnwpu/20193730523
[research_lyubchak_filshtinskii_1982]: https://doi.org/10.1007/bf00883592
[research_m_jury_1959]: https://doi.org/10.2307/3007623
[research_ma_abouhamzeh_2023]: https://doi.org/10.2514/1.c036988
[research_ma_abouhamzeh_2024]: https://doi.org/10.2514/1.c037388
[research_ma_chen_2020]: https://doi.org/10.1016/j.ijleo.2020.164468
[research_ma_chen_2023]: https://doi.org/10.1051/sands/2023020
[research_ma_dong_2019]: https://doi.org/10.1109/access.2019.2949061
[research_ma_guo_2015]: https://doi.org/10.1016/j.ast.2015.06.003
[research_ma_liu_2025]: https://doi.org/10.1016/j.isatra.2025.10.014
[research_ma_yu_2024]: https://doi.org/10.3390/drones8020058
[research_ma_zhou_2025]: https://doi.org/10.1109/access.2024.3519800
[research_maalawi_2019]: https://doi.org/10.1016/j.tws.2019.04.009
[research_mabboux_pommierbudinger_2024]: https://doi.org/10.1016/j.ast.2023.108778
[research_mackallda_pickettmd_1988]: https://ntrs.nasa.gov/citations/19880011793
[research_mackalldalea_allenjamesg_1989]: https://ntrs.nasa.gov/citations/19900023436
[research_mackalldalea_allenjamesg_1991]: https://ntrs.nasa.gov/citations/19910015825
[research_maewal_1984]: https://doi.org/10.21236/ada149071
[research_magliacano_tufano_2025]: https://doi.org/10.1016/j.compstruct.2025.119675
[research_magness_robinson_1993]: https://doi.org/10.2514/3.11786
[research_magnus_yoshihara_1975]: https://doi.org/10.2514/3.60585
[research_mahapatra_halbe_2024]: https://doi.org/10.1016/j.ifacol.2024.05.017
[research_mahdavizafarghandi_rezasoltani_2024]: https://doi.org/10.2514/1.c037347
[research_mahgoub_cortelezzi_2020]: https://doi.org/10.2514/1.j058021
[research_mahgoub_elbadawy_2022]: https://doi.org/10.1007/s11071-022-07213-z
[research_mahmood_2025]: https://doi.org/10.1177/10775463241312815
[research_mahulkar_2010]: https://doi.org/10.21236/ada534168
[research_maine_murray_1988]: https://doi.org/10.2514/3.20296
[research_maity_hocht_2019]: https://doi.org/10.1016/j.ejcon.2019.04.007
[research_maiworm_limon_2021]: https://doi.org/10.1002/rnc.5361
[research_malcom_1969]: https://doi.org/10.2514/3.59426
[research_malcomlg_husbandjh_1976]: https://ntrs.nasa.gov/citations/19760058464
[research_malik_akhtar_2017]: https://doi.org/10.15632/jtam-pl.55.3.963
[research_mallik_kapania_2015]: https://doi.org/10.2514/1.c033096
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
[research_mant_1972]: https://doi.org/10.1108/eb034920
[research_manzoor_maqsood_2016]: https://doi.org/10.15866/irease.v9i3.8119
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
[research_marr_roderick_1975]: https://doi.org/10.4050/jahs.20.23
[research_marske_1975]: https://doi.org/10.4271/750548
[research_martinezheredia_fernandezprada_2026]: https://doi.org/10.3390/en19153498
[research_martini_innocenti_2022]: https://doi.org/10.1016/j.chaos.2022.111892
[research_masini_timme_2019]: https://doi.org/10.1017/jfm.2019.906
[research_masini_timme_2020]: https://doi.org/10.2514/1.j059219
[research_maslanka_kachel_2025]: https://doi.org/10.15866/irease.v18i2.25886
[research_masonml_caponefj_1983]: https://ntrs.nasa.gov/citations/19830013890
[research_mateergeorgec_seegmillerhlee_1987]: https://ntrs.nasa.gov/citations/19870057640
[research_mathur_huang_2026]: https://doi.org/10.2514/1.j066300
[research_matos_marta_2025]: https://doi.org/10.3390/aerospace12050369
[research_matrix_cracking_1985]: https://doi.org/10.1016/0010-4361(85)90361-1
[research_matsuki_nishiyama_2018]: https://doi.org/10.1108/aeat-03-2016-0052
[research_matt_chao_2025]: https://doi.org/10.2514/1.c038147
[research_mayer_lutz_2019]: https://doi.org/10.2514/1.c034969
[research_mayer_prowe_2016]: https://doi.org/10.1016/j.compstruct.2016.01.023
[research_mazaheri_kiani_2015]: https://doi.org/10.1016/j.ast.2015.01.007
[research_mazaheri_nejati_2015]: https://doi.org/10.1007/s10494-015-9671-8
[research_mazaheri_nejati_2015_b]: https://doi.org/10.1007/s00193-015-0591-2
[research_mazaheri_nejati_2016]: https://doi.org/10.1080/0305215x.2016.1139811
[research_mazaheri_nejati_2017]: https://doi.org/10.24200/sci.2017.4032
[research_mcallister_esfahani_2025]: https://doi.org/10.1109/tac.2024.3498702
[research_mccormack_stevens_1947]: https://ntrs.nasa.gov/citations/19930085677
[research_mccutchen_1980]: https://doi.org/10.2514/3.44655
[research_mcdonnell_ning_2020]: https://doi.org/10.2514/1.c035566
[research_mceneaney_1999]: https://doi.org/10.21236/ada383810
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
[research_meglinskii_1966]: https://doi.org/10.1007/bf00887749
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
[research_menon_yousefpor_1996]: https://doi.org/10.21236/ada436537
[research_mhenni_choley_2016]: https://doi.org/10.1016/j.ifacol.2016.07.076
[research_michaud_dalir_2018]: https://doi.org/10.2514/1.c034340
[research_micheli_2024]: https://doi.org/10.2514/1.g008146
[research_micks_1950]: https://doi.org/10.2514/8.1784
[research_miele_1976]: https://doi.org/10.21236/ada053727
[research_mihailaandres_rosu_2019]: https://doi.org/10.1051/itmconf/20192402010
[research_mijovic_1985]: https://doi.org/10.1177/002199838501900205
[research_miles_broughton_2017]: https://doi.org/10.2514/1.c033900
[research_miller_1965]: https://doi.org/10.2514/3.43649
[research_miller_1970]: https://doi.org/10.2514/3.44206
[research_miller_1983]: https://doi.org/10.2514/6.1983-2482
[research_miller_1986]: https://doi.org/10.2514/3.45268
[research_miller_clark_1965]: https://doi.org/10.2514/3.43639
[research_miller_wykes_1983]: https://doi.org/10.2514/3.44931
[research_milz_may_2026]: https://doi.org/10.2514/1.g009361
[research_minerdd_glossbb_1975]: https://ntrs.nasa.gov/citations/19750013175
[research_mingong_sun_2022]: https://doi.org/10.34759/trd-2022-126-10
[research_miranda_bidinotto_2025]: https://doi.org/10.1590/jatm.v17.1368
[research_miranda_li_2025]: https://doi.org/10.1016/j.compstruct.2025.119291
[research_mirtaba_jeddi_2022]: https://doi.org/10.1007/s40435-022-01016-1
[research_mishra_yadav_2025]: https://doi.org/10.1504/ijscc.2025.145789
[research_missoum_2012]: https://doi.org/10.21236/ada582315
[research_mitchell_myers_1980]: https://doi.org/10.21236/ada101648
[research_miurahirokazu_neilldouglasj_1992]: https://ntrs.nasa.gov/citations/19930036331
[research_miyakawa_ohnuki_1991]: https://doi.org/10.4271/912021
[research_miyasato_1992]: https://doi.org/10.9746/sicetr1965.28.1141
[research_miyazawa_1993]: https://doi.org/10.2514/3.20995
[research_mkhoyan_thakrar_2022]: https://doi.org/10.1088/1361-665x/aca18b
[research_mobayen_izadbakhsh_2025]: https://doi.org/10.1007/s11071-025-11076-5
[research_mochizuki_yamada_2018]: https://doi.org/10.1051/matecconf/201814503010
[research_modaressaval_bakhtiarinejad_2019]: https://doi.org/10.1016/j.jfluidstructs.2019.01.003
[research_moens_2019]: https://doi.org/10.3390/biomimetics4030064
[research_moestimothyr_noffzgregoryk_2000]: https://ntrs.nasa.gov/citations/20010002099
[research_moestimothyr_smithmarks_2003]: https://ntrs.nasa.gov/citations/20030107571
[research_mohamed_g_2020]: https://doi.org/10.1016/j.ifacol.2020.06.013
[research_mohammadi_ebrahimi_2025]: https://doi.org/10.1007/s44245-025-00090-x
[research_mohammadzadeh_sayadi_2018]: https://doi.org/10.1016/j.cja.2018.04.004
[research_mohanty_chhotaray_1979]: https://doi.org/10.1080/03772063.1979.11451910
[research_mohseni_bernstein_2024]: https://doi.org/10.1002/acs.3810
[research_mojallizadeh_2026]: https://doi.org/10.1080/00207179.2026.2676813
[research_molent_haddad_2020]: https://doi.org/10.1016/j.compstruct.2019.111568
[research_monaghanrc_1981]: https://ntrs.nasa.gov/citations/19810009523
[research_moni_yao_2024]: https://doi.org/10.1063/5.0177577
[research_monshizadeh_2020]: https://doi.org/10.1109/lcsys.2020.2993986
[research_montgomery_1972]: https://doi.org/10.2514/3.59015
[research_montgomery_caglayan_1976]: https://doi.org/10.2514/3.58633
[research_montgomery_price_1976]: https://doi.org/10.2514/3.58634
[research_montgomeryrc_pricedb_1974]: https://ntrs.nasa.gov/citations/19740055499
[research_moon_1996]: https://doi.org/10.21236/ada361169
[research_moore_frei_1983]: https://doi.org/10.2514/6.1983-1834
[research_moorhouse_jenkins_1975]: https://doi.org/10.2514/3.44474
[research_moosavi_elasha_2022]: https://doi.org/10.3390/designs6020029
[research_moreira_gripp_2022]: https://doi.org/10.2514/1.g006443
[research_moreira_moleiro_2024]: https://doi.org/10.1016/j.compstruct.2024.118287
[research_morino_obayashi_2015]: https://doi.org/10.2514/1.c032775
[research_moriya_1982]: https://doi.org/10.1299/jsme1958.25.1202
[research_morozov_chermoshentsev_2019]: https://doi.org/10.21683/1729-2646-2019-19-1-30-35
[research_morozov_janschek_2016]: https://doi.org/10.1016/j.ifacol.2016.09.043
[research_morris_1977]: https://doi.org/10.21236/ada049528
[research_morton_xu_2023]: https://doi.org/10.1177/00219983231151397
[research_mottershead_cooper_2012]: https://doi.org/10.21236/ada571493
[research_moulmartint_brownlawrencew_1959]: https://ntrs.nasa.gov/citations/19980228212
[research_moulmartint_winemanandrewr_1952]: https://ntrs.nasa.gov/citations/19930086980
[research_moureydj_1979]: https://ntrs.nasa.gov/citations/19800001956
[research_mu_huang_2022]: https://doi.org/10.1016/j.jsv.2022.116916
[research_mu_huang_2026]: https://doi.org/10.1016/j.jsv.2025.119440
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
[research_nagabhushan_1991]: https://doi.org/10.2514/3.46064
[research_naganarayana_atluri_1995]: https://doi.org/10.1007/s004660050032
[research_nagaraja_lakin_1981]: https://doi.org/10.2514/6.1981-656
[research_nagaraja_lakin_1982]: https://doi.org/10.2514/3.61555
[research_nagy_fossati_2022]: https://doi.org/10.3390/fluids7040130
[research_naihong_yaohua_1993]: https://doi.org/10.2514/3.46361
[research_najmi_khan_2024]: https://doi.org/10.1016/j.heliyon.2024.e24151
[research_nakamura_1982]: https://doi.org/10.1143/jpsj.51.4084
[research_nam_chen_2000]: https://doi.org/10.21236/ada379722
[research_namanikoureh_shahverdi_2026]: https://doi.org/10.1007/s00158-026-04311-z
[research_nan_zheng_2024]: https://doi.org/10.3390/machines12120907
[research_nangia_palmer_2002]: https://doi.org/10.2514/6.2002-4616
[research_nangia_palmer_2003]: https://doi.org/10.2514/6.2003-605
[research_napolitano_2002]: https://doi.org/10.21236/ada400639
[research_napolitanomarcellor_1996]: https://ntrs.nasa.gov/citations/19960014815
[research_napolitanomarcellor_spagnuolojoellem_1993]: https://ntrs.nasa.gov/citations/19940020331
[research_narayanan_kumar_2026]: https://doi.org/10.1051/e3sconf/202669202008
[research_narendra_tripathi_1973]: https://doi.org/10.2514/3.44364
[research_narenshakthi_dharani_2025]: https://doi.org/10.1007/s11785-025-01829-w
[research_naresh_srinivas_2024]: https://doi.org/10.1142/s0219455425501664
[research_narimani_haddadpour_2025]: https://doi.org/10.1016/j.ast.2025.109992
[research_nath_ana_2017]: https://doi.org/10.14445/22315381/ijett-v54p212
[research_navratil_2017]: https://doi.org/10.1051/itmconf/20171400006
[research_nazarenko_nevezhina_1972]: https://doi.org/10.1007/bf01186488
[research_nazari_seron_2017]: https://doi.org/10.1016/j.automatica.2016.09.012
[research_nazeer_wang_2021]: https://doi.org/10.3390/act10060107
[research_neal_smith_1970]: https://doi.org/10.21236/ad0880426
[research_negahban_bashir_2024]: https://doi.org/10.3390/drones8080392
[research_negahbanb_khalafi_2025]: https://doi.org/10.1080/15397734.2025.2553328
[research_nejati_mazaheri_2017]: https://doi.org/10.1080/17797179.2017.1386022
[research_nekooei_farsangi_2021]: https://doi.org/10.1016/j.nahs.2021.101019
[research_nelson_mouch_1978]: https://doi.org/10.21236/ada056045
[research_neu_huang_1973]: https://doi.org/10.21236/ada325972
[research_newkirk_1979]: https://doi.org/10.21236/ada089350
[research_newton_kroo_2025]: https://doi.org/10.2514/1.g008400
[research_nguyen_2019]: https://doi.org/10.1299/jamdsm.2019jamdsm0057
[research_nguyen_han_2025]: https://doi.org/10.1016/j.automatica.2025.112270
[research_nguyen_lowenberg_2021]: https://doi.org/10.2514/1.g005840
[research_nguyen_olaru_2016]: https://doi.org/10.1016/j.automatica.2015.10.048
[research_nguyen_prodan_2026]: https://doi.org/10.1016/j.ejcon.2025.101442
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
[research_niel_seuret_2017]: https://doi.org/10.1016/j.ifacol.2017.08.2041
[research_nield_iv_1981]: https://doi.org/10.21236/ada106742
[research_nihtila_1989]: https://doi.org/10.1016/0167-6911(89)90046-7
[research_nikolaev_2019]: https://doi.org/10.1061/(asce)as.1943-5525.0001086
[research_nikolaou_kilimtzidis_2026]: https://doi.org/10.3390/drones10050352
[research_nikrad_asadi_2015]: https://doi.org/10.1016/j.compstruct.2015.07.019
[research_nitschke_vincenti_2019]: https://doi.org/10.1016/j.compstruct.2019.03.072
[research_niu_chen_2018]: https://doi.org/10.1007/s11071-018-4127-z
[research_niu_li_2022]: https://doi.org/10.3390/app122211820
[research_niu_zhang_2022]: https://doi.org/10.3103/s0025654422060103
[research_noll_calico_1983]: https://doi.org/10.2514/6.1983-2220
[research_noll_eastep_1984]: https://doi.org/10.2514/3.48246
[research_non_linear_bending_1977]: https://doi.org/10.1016/0010-4361(77)90121-5
[research_nonweiler_1960]: https://doi.org/10.1017/s0368393100072485
[research_noordin_mohdbasri_2023]: https://doi.org/10.3390/aerospace10010059
[research_northropaircraftinchawthorneca_1952]: https://doi.org/10.21236/ad0024361
[research_norton_1990]: https://doi.org/10.21236/ada257262
[research_norwood_1992]: https://doi.org/10.21236/ada249881
[research_ntantis_xezonakis_2024]: https://doi.org/10.1016/j.rineng.2024.103189
[research_numerical_analysis_2017]: https://doi.org/10.15372/pmtf20170303
[research_numerical_and_2019]: https://doi.org/10.17559/tv-20180724143418
[research_numerical_study_2023]: https://doi.org/10.47176/jafm.16.09.1755
[research_oberkampf_nicolaides_1971]: https://doi.org/10.2514/3.50043
[research_obilanade_torlind_2025]: https://doi.org/10.1017/dsj.2025.10042
[research_ocali_sezer_1992]: https://doi.org/10.1109/9.256390
[research_ochi_kanai_1995]: https://doi.org/10.2514/3.21393
[research_ochoa_groves_2019]: https://doi.org/10.1002/stc.2340
[research_odonnell_mohseni_2019]: https://doi.org/10.2514/1.c034704
[research_oelker_hummel_1989]: https://doi.org/10.2514/3.45817
[research_ogunvoul_balanchuk_2017]: https://doi.org/10.26467/2079-0619-2017-20-4-41-51
[research_ohkawa_1985]: https://doi.org/10.1080/00207178508933423
[research_ohkawa_1986]: https://doi.org/10.1080/00207178608933588
[research_ohkuma_1993]: https://doi.org/10.1016/0167-6105(93)90365-u
[research_ohta_nikiforuk_1979]: https://doi.org/10.2514/3.55828
[research_ohta_nikiforuk_1982]: https://doi.org/10.2514/3.56143
[research_okumoto_elsanker_1973]: https://doi.org/10.21236/ad0767182
[research_oland_andersen_2016]: https://doi.org/10.1016/j.automatica.2016.02.034
[research_olivett_corrao_2021]: https://doi.org/10.1088/1361-665x/abd347
[research_olsen_1965]: https://doi.org/10.21236/ad0626928
[research_olsen_1966]: https://doi.org/10.21236/ad0647369
[research_om_park_2020]: https://doi.org/10.9728/jcc.2020.06.2.1.95
[research_onkar_2021]: https://doi.org/10.1007/s11012-021-01390-8
[research_onkar_kumar_2024]: https://doi.org/10.1007/s12046-024-02629-2
[research_opgenoord_willcox_2019]: https://doi.org/10.2514/1.j058169
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
[research_othman_silva_2019]: https://doi.org/10.1016/j.compstruct.2018.09.086
[research_otsuka_makihara_2017]: https://doi.org/10.1299/jsmedmc.2017.715
[research_ouyang_gu_2021]: https://doi.org/10.1016/j.ast.2020.106457
[research_ouyang_lin_2017]: https://doi.org/10.1002/rnc.3883
[research_ouyang_zeng_2021]: https://doi.org/10.1155/2021/5535192
[research_owens_perkins_1996]: https://doi.org/10.2514/3.47079
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
[research_palframan_fry_2019]: https://doi.org/10.1109/tcst.2017.2766598
[research_palkin_zenchenko_2025]: https://doi.org/10.18127/j20700784-202509-06
[research_palmtod_mahlermary_2000]: https://ntrs.nasa.gov/citations/20000052504
[research_pan_cheng_1995]: https://doi.org/10.2514/3.46853
[research_pan_huang_2019]: https://doi.org/10.5028/jatm.v11.1074
[research_pan_liu_2019]: https://doi.org/10.2514/1.j058120
[research_pang_cesnik_2014]: https://doi.org/10.2514/6.2014-0330
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
[research_parthivnshah_ericlblades_2023]: https://ntrs.nasa.gov/citations/20220001748
[research_passenbrunner_sassano_2016]: https://doi.org/10.1016/j.ejcon.2016.04.002
[research_passive_wing_store_1982]: https://doi.org/10.1121/1.387660
[research_patartics_liptak_2022]: https://doi.org/10.1109/tcst.2021.3066096
[research_patel_deodhare_2023]: https://doi.org/10.61653/joast.v58i4.2006.741
[research_patel_kumar_2022]: https://doi.org/10.1016/j.ifacol.2022.11.241
[research_patne_ingole_2020]: https://doi.org/10.1016/j.ifacol.2020.12.443
[research_patni_minera_2019]: https://doi.org/10.1016/j.compstruct.2019.111034
[research_patrickcmurphy_1999]: https://ntrs.nasa.gov/citations/19990032463
[research_patterson_grenestedt_2018]: https://doi.org/10.1016/j.compstruct.2018.08.052
[research_paul_rein_2017]: https://doi.org/10.2514/1.c034080
[research_paulsonjwjr_thomasjl_1978]: https://ntrs.nasa.gov/citations/19780018153
[research_paulsonjwjr_thomasjl_1979]: https://ntrs.nasa.gov/citations/19790035660
[research_paulsonjwjr_thomasjl_1979_b]: https://ntrs.nasa.gov/citations/19800004739
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
[research_peng_li_2026]: https://doi.org/10.1002/rnc.70594
[research_pengelley_wilson_1954]: https://doi.org/10.21236/ad0061591
[research_pereira_sales_2021]: https://doi.org/10.1016/j.compstruct.2020.112932
[research_perez_theodoulis_2022]: https://doi.org/10.1016/j.ifacol.2022.09.057
[research_perfect_jump_2015]: https://doi.org/10.2514/1.g001073
[research_perfect_jump_2015_b]: https://doi.org/10.2514/1.g000862
[research_perkins_brice_1966]: https://doi.org/10.21236/ad0632829
[research_perry_2025]: https://doi.org/10.2514/1.c038025
[research_perry_rievley_1961]: https://doi.org/10.21236/ad0259391
[research_perrybiii_1976]: https://ntrs.nasa.gov/citations/19760011057
[research_perrybiii_1982]: https://ntrs.nasa.gov/citations/19820020423
[research_persoon_horsten_1984]: https://doi.org/10.2514/3.45061
[research_persoon_roos_1980]: https://doi.org/10.21236/ada097094
[research_petersenkl_1981]: https://ntrs.nasa.gov/citations/19820030322
[research_petre_ashley_1976]: https://doi.org/10.2514/3.58707
[research_petriconi_lomazzi_2026]: https://doi.org/10.58286/33896
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
[research_pidaparti_1993]: https://doi.org/10.1016/0263-8223(93)90154-i
[research_pidaparti_yang_1993]: https://doi.org/10.2514/3.11735
[research_pierre_iervolino_2023]: https://doi.org/10.1016/j.addma.2022.103344
[research_pizzoli_saltari_2022]: https://doi.org/10.3390/app12178762
[research_place_altmann_1974]: https://doi.org/10.21236/ad0785104
[research_placek_ruchala_2018]: https://doi.org/10.1016/j.trpro.2018.02.029
[research_plaetschke_mulder_1982]: https://doi.org/10.1016/s1474-6670(17)63152-5
[research_plotkin_1978]: https://doi.org/10.1115/1.3424324
[research_plyako_1977]: https://doi.org/10.1007/bf00967161
[research_poll_1986]: https://doi.org/10.1017/s0001924000015670
[research_pollack_theodoulis_2024]: https://doi.org/10.1016/j.ast.2024.109377
[research_pollack_theodoulis_2026]: https://doi.org/10.2514/1.g009559
[research_pollack_vankampen_2023]: https://doi.org/10.2514/1.g006576
[research_polyester_fibreglass_reinforced_1978]: https://doi.org/10.1016/0010-4361(78)90633-x
[research_poole_allen_2022]: https://doi.org/10.1007/s00158-022-03174-4
[research_poole_allen_2026]: https://doi.org/10.2514/1.c038630
[research_portapas_cooke_2020]: https://doi.org/10.3846/aviation.2020.12175
[research_posingies_1979]: https://doi.org/10.21236/ada070387
[research_pourtakdoust_khodabakhsh_2026]: https://doi.org/10.1016/j.ast.2025.111214
[research_poussotvassal_demourant_2017]: https://doi.org/10.1109/tcst.2016.2630505
[research_powers_1982]: https://doi.org/10.2514/3.56150
[research_powersbg_1980]: https://ntrs.nasa.gov/citations/19800061700
[research_prajapati_prasad_2019]: https://doi.org/10.1177/0142331219874595
[research_prasad_nematnasser_1967]: https://doi.org/10.2514/3.3959
[research_preissler_schaufele_1991]: https://doi.org/10.2514/3.46003
[research_price_lee_1993]: https://doi.org/10.2514/3.56887
[research_pritt_1980]: https://doi.org/10.21236/ada106425
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
[research_qian_xinhui_2025]: https://doi.org/10.65904/3083-3450.2025.01.05
[research_qiao_gao_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.07.009
[research_qiao_wu_2018]: https://doi.org/10.1080/21642583.2018.1558421
[research_qin_liu_2017]: https://doi.org/10.1016/j.ast.2017.06.012
[research_qin_liu_2023]: https://doi.org/10.1049/cth2.12427
[research_qiu_2022]: https://doi.org/10.21595/vp.2022.23045
[research_qiu_fang_2018]: https://doi.org/10.1177/1475921718759344
[research_qiu_yuan_2017]: https://doi.org/10.1177/1475921717692571
[research_qu_annaswamy_2016]: https://doi.org/10.2514/1.g001282
[research_qu_li_2022]: https://doi.org/10.1088/1742-6596/2258/1/012074
[research_quagliarella_iuliano_2017]: https://doi.org/10.1109/mci.2017.2742718
[research_quero_vuillemin_2019]: https://doi.org/10.3390/aerospace6010009
[research_radetskaya_2022]: https://doi.org/10.18698/2541-8009-2022-10-833
[research_radfordrc_smithr_1980]: https://ntrs.nasa.gov/citations/19810005458
[research_rafi_steck_2017]: https://doi.org/10.2514/1.g002693
[research_ragab_hajj_2018]: https://doi.org/10.1504/ijad.2018.10010814
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
[research_ramroop_chinchamee_2025]: https://doi.org/10.14455/isec.2025.12(1).str-54
[research_ranaudorichardj_ratvaskythomasp_2000]: https://ntrs.nasa.gov/citations/20000120385
[research_raney_batterson_1989]: https://ntrs.nasa.gov/citations/19890012431
[research_raneydavidl_1987]: https://ntrs.nasa.gov/citations/19870062350
[research_rao_1975]: https://doi.org/10.1016/s0022-460x(75)80007-1
[research_rao_hofer_1973]: https://doi.org/10.21236/ada305383
[research_rao_padmanabhan_2019]: https://doi.org/10.1504/ijndc.2019.103285
[research_rao_shi_2023]: https://doi.org/10.3390/aerospace10050420
[research_rao_umamaheswararao_1992]: https://doi.org/10.1016/0263-8223(92)90002-t
[research_raouf_1994]: https://doi.org/10.1016/0263-8223(94)90023-x
[research_rapoffandrewj_dillharoldd_1990]: https://ntrs.nasa.gov/citations/19920023336
[research_rashed_demir_2022]: https://doi.org/10.1016/j.compstruct.2021.115151
[research_rashmikant_abe_2026]: https://doi.org/10.1016/j.ast.2026.112653
[research_rate_sensitivity_1988]: https://doi.org/10.1016/0010-4361(88)90610-6
[research_rath_fichter_2020]: https://doi.org/10.4050/jahs.66.022003
[research_rathnasabapathy_mouritz_2022]: https://doi.org/10.1016/j.compstruct.2022.115368
[research_rauer_2019]: https://doi.org/10.1007/s42496-019-00020-7
[research_ray_hicks_1988]: https://ntrs.nasa.gov/citations/19880011767
[research_ray_hicks_1990]: https://ntrs.nasa.gov/citations/19900057683
[research_rayej_mckinneylw_1972]: https://ntrs.nasa.gov/citations/19730006292
[research_rayej_mckinneylw_1973]: https://ntrs.nasa.gov/citations/19730017272
[research_rea_pecora_2018]: https://doi.org/10.18178/ijmerr.6.6.440-450
[research_reajbcoincsantamonicaca_1957]: https://doi.org/10.21236/ad0126837
[research_reddy_1982]: https://doi.org/10.1016/0015-0568(82)90058-6
[research_reddy_1987]: https://doi.org/10.2514/3.45421
[research_redeker_wichmann_1991]: https://doi.org/10.2514/3.45997
[research_rediessha_szalaikj_1975]: https://ntrs.nasa.gov/citations/19750020942
[research_reding_ericsson_1977]: https://doi.org/10.2514/3.58883
[research_reeder_1958]: https://doi.org/10.4050/jahs.3.4
[research_refinement_of_2023]: https://doi.org/10.36652/0869-4931-2023-77-2-86-94
[research_regulator_with_2022]: https://doi.org/10.36652/0869-4931-2022-76-2-73-77
[research_rehan_iqbal_2015]: https://doi.org/10.1002/rnc.3372
[research_rehman_2022]: https://doi.org/10.13111/2066-8201.2022.14.3.8
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
[research_report_no_1921]: https://doi.org/10.1016/s0016-0032(21)90863-9
[research_report_no_1930]: https://doi.org/10.1016/s0016-0032(30)90271-2
[research_research_and_2022]: https://doi.org/10.47939/et.v3i2.104
[research_restifo_villa_2026]: https://doi.org/10.1016/j.mlwa.2026.100896
[research_review_of_2024]: https://doi.org/10.3901/jme.2024.04.050
[research_reyes_climent_2019]: https://doi.org/10.1007/s13272-019-00361-w
[research_rhodesmd_selbergbp_1982]: https://ntrs.nasa.gov/citations/19820057396
[research_richards_yao_2016]: https://doi.org/10.2514/1.c033435
[research_richmj_ridgleygf_1974]: https://ntrs.nasa.gov/citations/19740053860
[research_richter_calix_2024]: https://doi.org/10.1109/access.2024.3433540
[research_richwinedavidm_fisherdavidf_1991]: https://ntrs.nasa.gov/citations/19910069136
[research_rickardww_1978]: https://ntrs.nasa.gov/citations/19780062649
[research_rickettsrh_doggettrvjr_1980]: https://ntrs.nasa.gov/citations/19800020786
[research_rickettsrh_sandfordmc_1983]: https://ntrs.nasa.gov/citations/19830048631
[research_rickettsrh_watsonjj_1983]: https://ntrs.nasa.gov/citations/19860014096
[research_rieck_herrmann_2026]: https://doi.org/10.1007/s13272-026-00991-x
[research_rigatos_2021]: https://doi.org/10.1142/s2737480721500126
[research_rimer_chipman_1983]: https://doi.org/10.2514/6.1983-2125
[research_rimer_chipman_1984]: https://doi.org/10.2514/3.45034
[research_rimer_chipman_1986]: https://doi.org/10.2514/3.20069
[research_rimerm_chipmanr_1984]: https://ntrs.nasa.gov/citations/19840060637
[research_ringertz_1994]: https://doi.org/10.1007/bf01742928
[research_risingjj_daviswj_1984]: https://ntrs.nasa.gov/citations/19850030442
[research_riso_cesnik_2023]: https://doi.org/10.1016/j.jfluidstructs.2023.103897
[research_rivero_fournier_2021]: https://doi.org/10.2514/1.j059606
[research_rizzetta_1977]: https://doi.org/10.21236/ada057505
[research_rizzetta_1979]: https://doi.org/10.2514/3.61058
[research_ro_barlow_1992]: https://doi.org/10.2514/6.1992-46
[research_roache_1965]: https://doi.org/10.2514/3.59234
[research_robbins_stansbury_2023]: https://doi.org/10.1504/ijvd.2023.10060015
[research_roberts_reed_2015]: https://doi.org/10.2514/1.c032779
[research_robertspa_swaimrl_1977]: https://ntrs.nasa.gov/citations/19770016183
[research_robinson_2004]: https://doi.org/10.21236/ada425641
[research_robinson_robinson_1980]: https://doi.org/10.2514/6.1980-1884
[research_robust_controller_2016]: https://doi.org/10.21311/001.39.6.30
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
[research_rogolski_olejnik_2018]: https://doi.org/10.1108/aeat-01-2018-0059
[research_rohella_chatterjee_1979]: https://doi.org/10.1080/03772063.1979.11451847
[research_rohith_sinha_2020]: https://doi.org/10.1007/s11071-020-05604-8
[research_roizner_karpel_2018]: https://doi.org/10.2514/1.j056514
[research_roizner_karpel_2019]: https://doi.org/10.2514/1.c035286
[research_roizner_raveh_2019]: https://doi.org/10.2514/1.c035045
[research_rokhsaz_selberg_1990]: https://doi.org/10.2514/3.25271
[research_romano_ciminello_2019]: https://doi.org/10.1177/0021998319843333
[research_ronflenadaud_2009]: https://doi.org/10.21236/ada512960
[research_rong_huang_2022]: https://doi.org/10.1002/acs.3390
[research_rongrong_zhengyin_2018]: https://doi.org/10.1177/0954410018807810
[research_rooneyrh_chungjc_1982]: https://ntrs.nasa.gov/citations/19820055409
[research_roorda_1967]: https://doi.org/10.1061/jmcea3.0000919
[research_roscoe_eisele_1975]: https://doi.org/10.21236/ada022459
[research_rose_seginer_1978]: https://doi.org/10.2514/3.58399
[research_rosique_alamin_2019]: https://doi.org/10.1016/j.ifacol.2019.11.293
[research_roskamj_lanc_1972]: https://ntrs.nasa.gov/citations/19730013170
[research_roskamj_lanc_1973]: https://ntrs.nasa.gov/citations/19730013169
[research_ross_1984]: https://doi.org/10.2514/6.1984-2402
[research_ross_matarazzo_1982]: https://doi.org/10.4271/821467
[research_roufaeil_dawe_1982]: https://doi.org/10.1016/0022-460x(82)90521-1
[research_rouhi_ghayoor_2018]: https://doi.org/10.1016/j.compstruct.2017.09.090
[research_rowley_2008]: https://doi.org/10.21236/ada476708
[research_roy_mukherjee_2026]: https://doi.org/10.1016/j.euromechflu.2025.204348
[research_roylance_1980]: https://doi.org/10.1177/002199838001400203
[research_ruhlin_rauch_1983]: https://doi.org/10.2514/3.44933
[research_ruhlin_watson_1982]: https://doi.org/10.2514/6.1982-644
[research_ruhlin_watson_1983]: https://doi.org/10.2514/3.44951
[research_rumble_1987]: https://doi.org/10.21236/ada194418
[research_runkel_fasel_2018]: https://doi.org/10.1016/j.compstruct.2018.07.095
[research_runyan_cunningham_1952]: https://doi.org/10.2514/8.2220
[research_ruo_malone_1985]: https://doi.org/10.2514/3.45076
[research_ruscheweyh_1983]: https://doi.org/10.1016/0167-6105(83)90017-x
[research_russo_healy_1986]: https://doi.org/10.2514/6.1986-9737
[research_rustenburg_1972]: https://doi.org/10.21236/ada004456
[research_rutkowski_1979]: https://doi.org/10.2514/3.58539
[research_ruzicka_rydel_2013]: https://doi.org/10.1007/978-3-642-34738-2_6
[research_ryder_walker_1976]: https://doi.org/10.21236/ada043365
[research_s_sinha_2018]: https://doi.org/10.1016/j.ifacol.2018.05.052
[research_sabater_bekemeyer_2022]: https://doi.org/10.2514/1.j060676
[research_sabatini_coppotelli_2026]: https://doi.org/10.2514/1.g009632
[research_sabido_bahamonde_2017]: https://doi.org/10.1016/j.compstruct.2016.10.081
[research_sabri_elzaabalawy_2022]: https://doi.org/10.1007/s00707-021-03138-7
[research_sachan_padhi_2020]: https://doi.org/10.1016/j.conengprac.2020.104526
[research_sachs_1975]: https://doi.org/10.2514/3.44471
[research_sachs_1977]: https://doi.org/10.2514/3.44623
[research_saderla_dhayalan_2016]: https://doi.org/10.14429/dsj.67.9995
[research_saderla_kim_2018]: https://doi.org/10.1016/j.ast.2018.07.008
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
[research_salagame_pandya_2025]: https://doi.org/10.1109/lcsys.2025.3589412
[research_salahudden_2025]: https://doi.org/10.1109/taes.2024.3485604
[research_salahudden_agrawal_2024]: https://doi.org/10.1016/j.ast.2024.109156
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
[research_saporito_daronch_2023]: https://doi.org/10.1016/j.ast.2023.108349
[research_saputra_purabaya_2018]: https://doi.org/10.1088/1742-6596/1005/1/012019
[research_sato_1973]: https://doi.org/10.2514/3.6669
[research_sato_muraoka_2017]: https://doi.org/10.2514/1.c034244
[research_satt_ilanko_2007]: https://doi.org/10.1016/j.jfluidstructs.2007.05.003
[research_savelev_neretin_2022]: https://doi.org/10.14489/vkit.2022.10.pp.003-014
[research_savin_hantraisgervois_2020]: https://doi.org/10.1016/j.probengmech.2020.103027
[research_saviolo_loianno_2023]: https://doi.org/10.1016/j.arcontrol.2023.03.009
[research_savithri_varadan_1990]: https://doi.org/10.1016/0022-460x(90)90534-7
[research_sawyerjw_1976]: https://ntrs.nasa.gov/citations/19760047048
[research_schafer_vidy_2018]: https://doi.org/10.1007/s13272-018-0353-9
[research_schewe_mai_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.04.021
[research_schieni_modasiya_2024]: https://doi.org/10.2514/1.g008048
[research_schildkamp_chang_2023]: https://doi.org/10.3390/act12070280
[research_schmeichel_1967]: https://doi.org/10.21236/ad0658073
[research_schmidt_2016]: https://doi.org/10.2514/1.g001484
[research_schmidt_2016_b]: https://doi.org/10.2514/1.c033539
[research_schmidt_danowsky_2020]: https://doi.org/10.2514/1.c035720
[research_schmidtdavidk_schiermanjohnd_1990]: https://ntrs.nasa.gov/citations/19900060642
[research_schpey_1980]: https://doi.org/10.21236/ada083721
[research_schreadley_1977]: https://doi.org/10.21236/ada043979
[research_schroederjefferya_chungwilliamwy_2001]: https://ntrs.nasa.gov/citations/20010037958
[research_schuet_lombaerts_2017]: https://doi.org/10.2514/1.g001729
[research_schuster_1995]: https://doi.org/10.2514/3.46686
[research_schuster_lokos_1988]: https://ntrs.nasa.gov/citations/19880015249
[research_schusterdavidm_edwardsjohnw_2004]: https://ntrs.nasa.gov/citations/20040086524
[research_schutte_huber_2018]: https://doi.org/10.2514/1.c033700
[research_schwanz_1972]: https://doi.org/10.21236/ada006391
[research_sciuva_1992]: https://doi.org/10.1016/0263-8223(92)90003-u
[research_scordamaglia_mattei_2025]: https://doi.org/10.1109/ojcsys.2025.3619810
[research_scott_bartels_2016]: https://doi.org/10.2514/1.g000265
[research_seegmiller_1963]: https://doi.org/10.1109/tce.1963.6373252
[research_sefic_cutler_1986]: https://ntrs.nasa.gov/citations/19860047338
[research_sefic_maxwell_1986]: https://ntrs.nasa.gov/citations/19860016856
[research_sefic_maxwell_1987]: https://ntrs.nasa.gov/citations/19870000497
[research_segel_1952]: https://doi.org/10.21236/ada076043
[research_seidel_eckstrom_1989]: https://doi.org/10.2514/3.45853
[research_seidel_sandford_1987]: https://doi.org/10.2514/3.45430
[research_seidelda_sandfordmc_1985]: https://ntrs.nasa.gov/citations/19850048176
[research_seitz_hubner_2019]: https://doi.org/10.1007/s13272-019-00421-1
[research_sekhar_suresh_2024]: https://doi.org/10.1051/matecconf/202439201016
[research_selbergbp_cronindl_1985]: https://ntrs.nasa.gov/citations/19850008520
[research_sellerswilliamliii_meyersjamesf_1988]: https://ntrs.nasa.gov/citations/19890040847
[research_sellerswilliamliii_meyersjamesf_2004]: https://ntrs.nasa.gov/citations/20040161542
[research_sen_bhattacharya_2016]: https://doi.org/10.1002/stc.1961
[research_seraj_ganesan_2018]: https://doi.org/10.1016/j.compstruct.2018.05.133
[research_serani_diez_2024]: https://doi.org/10.1016/j.ast.2024.109611
[research_seres_liu_2023]: https://doi.org/10.1016/j.ifacol.2023.10.1097
[research_serhat_bediz_2020]: https://doi.org/10.1016/j.compstruct.2020.112183
[research_seshadri_krishnamurthy_2017]: https://doi.org/10.2514/1.c033940
[research_setiawarman_sasongko_2026]: https://doi.org/10.1142/s2737480726400078
[research_setoguchi_kanazaki_2020]: https://doi.org/10.2514/6.2020-0534
[research_seyoung_1990]: https://doi.org/10.1016/0020-7683(90)90098-g
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
[research_shankar_malmuth_1981]: https://doi.org/10.2514/3.44699
[research_shankar_malmuth_1982]: https://doi.org/10.21236/ada121662
[research_shankar_malmuth_1983]: https://doi.org/10.2514/3.44893
[research_shanley_1943]: https://doi.org/10.1108/eb031034
[research_shao_sun_2025]: https://doi.org/10.1007/s11029-025-10258-x
[research_sharif_abbas_2022]: https://doi.org/10.47893/gret.2022.1084
[research_sharifi_vincenti_2025]: https://doi.org/10.1016/j.compstruct.2025.118839
[research_sharma_agrawal_2022]: https://doi.org/10.1016/j.ifacol.2023.03.027
[research_sharma_swain_2023]: https://doi.org/10.1177/00219983231175468
[research_sharqi_cesnik_2023]: https://doi.org/10.2514/1.c036894
[research_shayak_girdhar_2024]: https://doi.org/10.3389/fpace.2024.1308872
[research_shcherban_sterlin_2022]: https://doi.org/10.26896/1028-6861-2022-88-4-66-75
[research_shearwood_nabawy_2020]: https://doi.org/10.3390/aerospace7100150
[research_sheikh_lee_2023]: https://doi.org/10.1093/jcde/qwad059
[research_sheikhi_rafieianamagh_2024]: https://doi.org/10.1016/j.compstruct.2023.117836
[research_sheikhi_rafieianamagh_2024_b]: https://doi.org/10.1016/j.matdes.2024.113142
[research_shen_bai_2015]: https://doi.org/10.21742/ijiace.2015.2.2.02
[research_shen_chang_2022]: https://doi.org/10.1088/1742-6596/2338/1/012092
[research_shen_chen_2022]: https://doi.org/10.1002/oca.2952
[research_shen_chen_2023]: https://doi.org/10.1108/aeat-09-2022-0250
[research_shen_chen_2024]: https://doi.org/10.1109/tcyb.2022.3213178
[research_shen_huang_2021]: https://doi.org/10.1016/j.cja.2020.07.022
[research_shen_wen_2018]: https://doi.org/10.2514/1.j056565
[research_sherrer_hertz_1981]: https://doi.org/10.2514/3.57589
[research_sheshanarayana_armstrong_2026]: https://doi.org/10.2514/1.c037564
[research_shi_bezine_1988]: https://doi.org/10.1177/002199838802200801
[research_shi_gao_2025]: https://doi.org/10.3390/aerospace12060532
[research_shi_lan_2023]: https://doi.org/10.1007/s00158-023-03559-z
[research_shi_liu_2020]: https://doi.org/10.3390/fluids5010034
[research_shi_liu_2021]: https://doi.org/10.3390/aerospace8120390
[research_shi_lyu_2019]: https://doi.org/10.1109/access.2019.2938013
[research_shi_mader_2021]: https://doi.org/10.1007/s00158-021-02936-w
[research_shi_tan_2018]: https://doi.org/10.1360/n092017-00215
[research_shi_wan_2015]: https://doi.org/10.1108/aeat-01-2013-0004
[research_shi_wang_2022]: https://doi.org/10.3390/drones6100272
[research_shiau_chang_1991]: https://doi.org/10.1016/0045-7949(91)90025-h
[research_shieh_chen_1998]: https://doi.org/10.21236/ada344559
[research_shields_cook_1971]: https://doi.org/10.1080/00207177108932075
[research_shimoda_nagano_2018]: https://doi.org/10.1007/s00158-018-2144-7
[research_shinde_ohol_2021]: https://doi.org/10.2139/ssrn.3808560
[research_shiota_ohmori_2015]: https://doi.org/10.1016/j.ifacol.2015.09.436
[research_shirk_hertz_1986]: https://doi.org/10.2514/3.45260
[research_shivaji_basavaraju_2025]: https://doi.org/10.1063/5.0265477
[research_shivam_verma_2019]: https://doi.org/10.13111/2066-8201.2019.11.2.14
[research_shmilovich_princen_2026]: https://doi.org/10.2514/1.c038755
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
[research_shukla_patil_2017]: https://doi.org/10.1007/s11071-017-3332-5
[research_shyprykevichp_1979]: https://ntrs.nasa.gov/citations/19800036960
[research_si_baier_2016]: https://doi.org/10.1177/1475921716636334
[research_sibert_1937]: https://doi.org/10.2514/8.367
[research_sibert_1943]: https://doi.org/10.2514/8.10986
[research_siddiqui_elferik_2016]: https://doi.org/10.1016/j.ifacol.2016.07.510
[research_silton_fresconi_2014]: https://doi.org/10.21236/ada611082
[research_silton_fresconi_2015]: https://doi.org/10.2514/1.a33219
[research_silva]: https://doi.org/10.11606/003273318
[research_silvawaltera_bennettrobertm_1990]: https://ntrs.nasa.gov/citations/19900010731
[research_simbuerger_raveh_2022]: https://doi.org/10.2514/1.c036626
[research_simmonds_1971]: https://doi.org/10.1090/qam/99753
[research_simmons_2023_b]: https://doi.org/10.2514/1.c036896
[research_simmons_gresham_2023]: https://doi.org/10.2514/1.c036773
[research_simon_harkegard_2017]: https://doi.org/10.2514/1.g002272
[research_simsrobert_mccrossonpaul_1989]: https://ntrs.nasa.gov/citations/19900009909
[research_singer_1989]: https://doi.org/10.1007/bf02321376
[research_singh_brown_2016]: https://doi.org/10.2514/1.c033658
[research_singh_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1050
[research_singh_raisinghani_1993]: https://doi.org/10.2514/3.46373
[research_singhvi_kapania_1994]: https://doi.org/10.1061/(asce)0733-9399(1994)120:10(2126)
[research_sinha_klimmek_2021]: https://doi.org/10.1007/s13272-021-00494-x
[research_sisson_dogan_2026]: https://doi.org/10.1002/acs.70091
[research_sitzjoelr_vernontoddh_1990]: https://ntrs.nasa.gov/citations/19930021575
[research_sivanandi_sanjay_2025]: https://doi.org/10.3390/eng6120354
[research_sizlotr_bergra_1979]: https://ntrs.nasa.gov/citations/19820024501
[research_sleesongsom_kumar_2022]: https://doi.org/10.3390/sym14102125
[research_sleptsov_andrianova_2021]: https://doi.org/10.1016/j.ifacol.2021.10.446
[research_sliwasm_1980]: https://ntrs.nasa.gov/citations/19810005457
[research_smeltzer_durston_1983]: https://doi.org/10.2514/3.44950
[research_smetana_1973]: https://doi.org/10.21236/ad0763295
[research_smith_1968]: https://doi.org/10.21236/ad0667521
[research_smith_1978]: https://doi.org/10.21236/ada059716
[research_smith_1991]: https://doi.org/10.1177/002029409102400303
[research_smith_2025]: https://doi.org/10.33548/scientia1180
[research_smith_geddes_1979]: https://doi.org/10.21236/ada077858
[research_smith_hammer_1971]: https://doi.org/10.21236/ad0730571
[research_smith_komerath_2001]: https://doi.org/10.21236/ada454384
[research_smith_lebacqz_1973]: https://doi.org/10.21236/ad0754840
[research_smith_meyer_1987]: https://doi.org/10.2514/3.20213
[research_smithjw_1979]: https://ntrs.nasa.gov/citations/19790023049
[research_smithjw_berrydt_1975]: https://ntrs.nasa.gov/citations/19750008488
[research_smithrogerse_schroederkurtc_1986]: https://ntrs.nasa.gov/citations/19870060567
[research_snyder_zhao_2019]: https://doi.org/10.1016/j.ifacol.2019.12.047
[research_snyder_zhao_2022]: https://doi.org/10.2514/1.g006305
[research_sobieczky_1984]: https://doi.org/10.1146/annurev.fluid.16.1.337
[research_sodja_werter_2021]: https://doi.org/10.2514/1.c035955
[research_sofi_2015]: https://doi.org/10.1016/j.probengmech.2015.09.001
[research_sohst_lobodovale_2022]: https://doi.org/10.1016/j.ast.2022.107531
[research_soleymani_arani_2019]: https://doi.org/10.1016/j.compstruct.2019.111532
[research_solies_1994]: https://doi.org/10.2514/3.46602
[research_solies_1994_b]: https://doi.org/10.2514/3.46495
[research_soltani_turner_2025]: https://doi.org/10.1109/lcsys.2025.3577574
[research_somashekar_prathap_1987]: https://doi.org/10.1016/0045-7949(87)90127-1
[research_son_sa_2015]: https://doi.org/10.6112/kscfe.2015.20.2.073
[research_son_sa_2015_b]: https://doi.org/10.1007/s12206-015-0720-y
[research_soneda_tsushima_2022]: https://doi.org/10.1007/s42405-022-00474-3
[research_song_huang_2022]: https://doi.org/10.1007/s11071-022-07742-7
[research_song_librescu_1991]: https://doi.org/10.2514/6.1991-1187
[research_song_mignolet_2018]: https://doi.org/10.1016/j.probengmech.2017.12.002
[research_song_zhang_2016]: https://doi.org/10.1016/j.compstruct.2016.01.005
[research_soovere_1982]: https://doi.org/10.2514/3.44755
[research_southwell_gunn_1981]: https://doi.org/10.1680/iicep.1981.2140
[research_spacht_1980]: https://doi.org/10.2514/6.1980-1885
[research_spagnol_riche_2019]: https://doi.org/10.1137/18m1167978
[research_spencer_walker_1975]: https://doi.org/10.1007/bf02318661
[research_spencer_watson_1992]: https://doi.org/10.1016/0022-5096(92)90041-y
[research_speyer_2003]: https://doi.org/10.21236/ada416352
[research_spillman_ridgely_1995]: https://doi.org/10.21236/ada320244
[research_srinathkumar_2015]: https://doi.org/10.4050/jahs.60.022010
[research_srivastava_2019]: https://doi.org/10.15394/ijaaa.2019.1370
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
[research_stanton_crain_1980]: https://doi.org/10.21236/ada088317
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
[research_stewart_bauer_1983]: https://ntrs.nasa.gov/citations/19840033063
[research_stirling_1983]: https://doi.org/10.1177/003754978304000504
[research_stodieck_cooper_2015]: https://doi.org/10.2514/1.j053599
[research_stodieck_cooper_2017]: https://doi.org/10.2514/1.j055364
[research_stodieck_cooper_2018]: https://doi.org/10.2514/1.j056952
[research_stolarik_2007]: https://doi.org/10.21236/ada470308
[research_stollery_1992]: https://doi.org/10.1016/0021-9169(92)90172-h
[research_stollf_koenigdg_1983]: https://ntrs.nasa.gov/citations/19830067155
[research_stottier_1995]: https://doi.org/10.21236/ada293962
[research_streit_wedler_2015]: https://doi.org/10.1017/s0001924000011283
[research_striz_1991]: https://doi.org/10.21236/ada248487
[research_structural_aspects_2000]: https://ntrs.nasa.gov/citations/20000053157
[research_structural_fundamentals_1955]: https://doi.org/10.1108/eb032631
[research_study_of_1978]: https://ntrs.nasa.gov/citations/19780012169
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
[research_sultan_2026]: https://doi.org/10.65664/jeie.v2i02.20
[research_sun_2024]: https://doi.org/10.1088/1742-6596/2882/1/012087
[research_sun_chen_2026]: https://doi.org/10.1007/s00158-026-04375-x
[research_sun_devisser_2019]: https://doi.org/10.2514/1.c035135
[research_sun_han_2022]: https://doi.org/10.3934/mbe.2022262
[research_sun_miao_2020]: https://doi.org/10.1063/5.0018763
[research_sun_shi_2020]: https://doi.org/10.1016/j.ast.2020.106126
[research_sun_vankampen_2021]: https://doi.org/10.2514/1.g005715
[research_sun_wang_2020]: https://doi.org/10.3390/act9040122
[research_sun_yoon_1988]: https://doi.org/10.21236/ada199311
[research_sun_zhang_2026]: https://doi.org/10.1016/j.ast.2025.110841
[research_suraj_anilkumar_2023]: https://doi.org/10.1016/j.compstruct.2023.117072
[research_surwase_kumar_2025]: https://doi.org/10.1186/s44147-025-00749-y
[research_suryawanshi_ghosh_2015]: https://doi.org/10.1007/s00158-015-1322-0
[research_sushchenko_bezkorovainyi_2023]: https://doi.org/10.18372/1990-5548.77.18006
[research_svoboda_hengstermovric_2023]: https://doi.org/10.1016/j.ast.2023.108415
[research_swaim_1961]: https://doi.org/10.2514/8.9241
[research_swaim_1970]: https://doi.org/10.2514/3.44151
[research_swaim_yen_1979]: https://doi.org/10.2514/3.58579
[research_swain_adhikari_2019]: https://doi.org/10.1016/j.compstruct.2019.110916
[research_syed_moshtaghzadeh_2022]: https://doi.org/10.2514/1.j061574
[research_synaszko_salacinski_2015]: https://doi.org/10.1515/fas-2015-0004
[research_szalaikj_1975]: https://ntrs.nasa.gov/citations/19750010179
[research_szalaikj_1976]: https://ntrs.nasa.gov/citations/19760024056
[research_szalaikj_fellemanpg_1976]: https://ntrs.nasa.gov/citations/19760058525
[research_szalaikj_jarviscr_1978]: https://ntrs.nasa.gov/citations/19790005938
[research_szklarski_glebocki_2025]: https://doi.org/10.24425/ame.2025.155873
[research_szollosi_baranyi_2016]: https://doi.org/10.1002/asjc.1418
[research_szymanski_alstrom_2025]: https://doi.org/10.2514/1.c037978
[research_tagai_nakakita_2016]: https://doi.org/10.2514/6.2016-3355
[research_tahani_masdari_2017]: https://doi.org/10.1108/aeat-01-2016-0019
[research_taherinezhad_ramirezserrano_2023]: https://doi.org/10.3390/aerospace10100843
[research_tahir_maqsood_2026]: https://doi.org/10.2514/1.c038034
[research_tahraoui_1994]: https://doi.org/10.1017/s0308210500022447
[research_tai_wang_2023]: https://doi.org/10.1061/jaeeez.aseng-4565
[research_tai_wang_2023_b]: https://doi.org/10.2514/1.j062188
[research_taimoor_aijun_2019]: https://doi.org/10.1108/aeat-05-2019-0106
[research_takahashi_boccieri_2019]: https://doi.org/10.2514/6.2019-0813
[research_takahashi_yokozeki_2016]: https://doi.org/10.1177/1045389x16642298
[research_takarics_vanek_2019]: https://doi.org/10.1016/j.ifacol.2019.11.149
[research_talreja_phan_2019]: https://doi.org/10.1016/j.compstruct.2019.03.052
[research_tamaskani_alfi_2026]: https://doi.org/10.1016/j.ast.2026.111656
[research_tamboli_1956]: https://doi.org/10.1017/s0001925900010313
[research_tameh_sawan_2018]: https://doi.org/10.1109/tie.2017.2786202
[research_tan_1988]: https://doi.org/10.1177/002199838802201105
[research_tan_wang_2021]: https://doi.org/10.1103/physrevfluids.6.l102701
[research_tang_1972]: https://doi.org/10.2514/3.30382
[research_tang_1989]: https://doi.org/10.21236/ada216966
[research_tang_2025]: https://doi.org/10.1080/23307706.2025.2474671
[research_tang_chen_2017]: https://doi.org/10.1016/j.apm.2017.04.012
[research_tang_chen_2018]: https://doi.org/10.1177/1077546317750504
[research_tang_chen_2020]: https://doi.org/10.1177/1077546320929153
[research_tang_liu_2018]: https://doi.org/10.1016/j.compstruct.2018.07.111
[research_tang_tang_2025]: https://doi.org/10.23919/jsee.2025.000136
[research_tang_wang_2020]: https://doi.org/10.1016/j.cja.2020.05.027
[research_tang_wu_2015]: https://doi.org/10.1016/j.cja.2014.12.024
[research_tang_wu_2016]: https://doi.org/10.1016/j.cja.2015.12.001
[research_tang_wu_2017]: https://doi.org/10.1016/j.cja.2016.12.024
[research_tantaroudas_karachalios_2026]: https://doi.org/10.24132/acm.2026.1114
[research_tanveer_ahmad_2023]: https://doi.org/10.3390/aerospace10060563
[research_tanyer_tatlicioglu_2016]: https://doi.org/10.1080/00207721.2016.1261200
[research_tao_2025]: https://doi.org/10.1016/j.automatica.2025.112174
[research_tao_li_2016]: https://doi.org/10.1016/j.ins.2015.08.033
[research_targoff_1947]: https://doi.org/10.2514/8.1458
[research_targoff_1947_b]: https://doi.org/10.2514/8.1420
[research_tarnowski_2017]: https://doi.org/10.1108/aeat-11-2016-0208
[research_taufik_qasem_2025]: https://doi.org/10.1016/j.trpro.2025.03.120
[research_taylor_1959]: https://doi.org/10.1017/s0001924000092502
[research_taylor_butler_1999]: https://doi.org/10.1017/s0001924000027809
[research_teel_1999]: https://doi.org/10.21236/ada367012
[research_teel_1999_b]: https://doi.org/10.21236/ada367415
[research_teixeira_araujo_2018]: https://doi.org/10.1109/tcns.2017.2732158
[research_teixeira_cesnik_2020]: https://doi.org/10.1017/aer.2019.165
[research_telionis_1995]: https://doi.org/10.21236/ada299820
[research_telionis_2001]: https://doi.org/10.21236/ada398139
[research_teper_stapleford_1966]: https://doi.org/10.2514/3.43725
[research_terekhov_2022]: https://doi.org/10.34759/vst-2022-1-211-225
[research_thanusha_sarkar_2016]: https://doi.org/10.1016/j.proeng.2016.05.128
[research_tharp_zhang_1994]: https://doi.org/10.1007/bf02115737
[research_the_viscoelastic_1981]: https://doi.org/10.1016/0010-4361(81)90470-5
[research_theerthamalai_mukesh_2025]: https://doi.org/10.1063/5.0256726
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
[research_thu_gavrilov_2017]: https://doi.org/10.1016/j.procs.2017.01.046
[research_thwapiah_campanile_2010]: https://doi.org/10.1115/smasis2010-3678
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
[research_toader_1987]: https://doi.org/10.1016/0263-8231(87)90019-x
[research_toffol_2024]: https://doi.org/10.3390/app14219883
[research_toffol_ricci_2023]: https://doi.org/10.3390/aerospace10080693
[research_tohidi_khakisedigh_2016]: https://doi.org/10.1002/rnc.3518
[research_tokunaga_masui_2015]: https://doi.org/10.1016/j.proeng.2014.12.638
[research_toledano_murakami_1987]: https://doi.org/10.1115/1.3172955
[research_toloei_ghaderi_2026]: https://doi.org/10.1007/s42401-026-00472-3
[research_tomlinson_1973]: https://doi.org/10.2514/3.60266
[research_tong_du_2025]: https://doi.org/10.1002/rnc.70057
[research_tormalm_leroy_2018]: https://doi.org/10.2514/1.c033820
[research_torregrosa_gil_2022]: https://doi.org/10.1016/j.compstruct.2022.115845
[research_torsional_stiffness_1972]: https://doi.org/10.1016/0010-4361(72)90404-1
[research_townsend_picelli_2018]: https://doi.org/10.2514/1.j056748
[research_trabocco_1980]: https://doi.org/10.21236/ada326379
[research_tran_nguyen_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001393
[research_tran_sakamoto_2017]: https://doi.org/10.1016/j.ast.2017.05.010
[research_traub_2019]: https://doi.org/10.2514/1.c035600
[research_traven_whitley_1995]: https://doi.org/10.21236/ada300965
[research_tribuno_klein_1976]: https://doi.org/10.21236/ada029021
[research_trindadenascimento_cunha_2019]: https://doi.org/10.1049/iet-cta.2018.5293
[research_triplett_1972]: https://doi.org/10.2514/3.59009
[research_triplett_1980]: https://doi.org/10.2514/3.57932
[research_triplett_1980_b]: https://doi.org/10.2514/6.1980-794
[research_triplett_burkhart_1971]: https://doi.org/10.2514/3.59109
[research_triplett_kappus_1973]: https://doi.org/10.2514/3.60281
[research_trippensee_1991]: https://ntrs.nasa.gov/citations/19920062783
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
[research_urso_giunta_2026]: https://doi.org/10.1016/j.compstruct.2025.119762
[research_ursu_ionguta_2018]: https://doi.org/10.1088/1742-6596/1106/1/012033
[research_uzun_2024]: https://doi.org/10.1108/aeat-11-2023-0287
[research_uzun_bilgic_2023]: https://doi.org/10.1017/aer.2023.73
[research_uzun_oktay_2023]: https://doi.org/10.1108/aeat-09-2022-0259
[research_valasek_downing_1995]: https://doi.org/10.2514/6.1995-3248
[research_valsangkar_britto_1982]: https://doi.org/10.1680/iicep.1982.1992
[research_vanbaelen_ellerbroek_2020]: https://doi.org/10.2514/1.g004596
[research_vandam_holmes_1981]: https://doi.org/10.2514/3.57531
[research_vandenberg_elsenaar_1975]: https://doi.org/10.1017/s0022112075001930
[research_vandenbrandt_devisser_2018]: https://doi.org/10.1016/j.ifacol.2018.09.641
[research_vandenkieboom_elham_2017]: https://doi.org/10.1007/s00158-017-1787-0
[research_vandommelen_1995]: https://doi.org/10.21236/ada329654
[research_vandooren_bisagni_2024]: https://doi.org/10.1016/j.compstruct.2024.118295
[research_vandoren_1955]: https://doi.org/10.1109/irettrc.1955.6538793
[research_vantuyl_1988]: https://doi.org/10.2514/3.9883
[research_vanwaarde_2022]: https://doi.org/10.1109/lcsys.2021.3073860
[research_vanzyl_2001]: https://doi.org/10.2514/2.2806
[research_vanzyl_maserumule_2001]: https://doi.org/10.2514/2.2808
[research_varun_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1061
[research_varun_mondal_2022]: https://doi.org/10.1016/j.compstruct.2022.115662
[research_vedeneev_2020]: https://doi.org/10.2514/1.j058959
[research_veerman_kannemans_2013]: https://doi.org/10.1007/978-3-642-34738-2_3
[research_veley_khot_2008]: https://doi.org/10.21236/ada478915
[research_velkova_2017]: https://doi.org/10.19062/1842-9238.2017.15.3.1
[research_venkataraman_seiler_2019]: https://doi.org/10.2514/1.g003824
[research_vepa_kwon_2021]: https://doi.org/10.1017/aer.2021.38
[research_verhaegen_zbikowski_2017]: https://doi.org/10.1016/j.ast.2017.03.001
[research_verma_cidmontoya_2024]: https://doi.org/10.2139/ssrn.5039067
[research_verma_cidmontoya_2025]: https://doi.org/10.1016/j.jweia.2025.106133
[research_vermiglio_2017]: https://doi.org/10.1137/15m1029618
[research_verri_desilvabussamra_2025]: https://doi.org/10.2514/1.c037829
[research_vertonghen_irisarri_2026]: https://doi.org/10.1016/j.compstruct.2026.120658
[research_vescovini_dozio_2016]: https://doi.org/10.1016/j.compstruct.2016.01.068
[research_viglietti_zappino_2019]: https://doi.org/10.2514/1.c034795
[research_vile_alwi_2020]: https://doi.org/10.1049/cth2.12042
[research_vilela_donadon_2025]: https://doi.org/10.1016/j.tws.2025.113547
[research_vinje_miller_1973]: https://doi.org/10.21236/ad0769868
[research_viola_oziablo_2020]: https://doi.org/10.1016/j.ifacol.2020.12.1617
[research_vitushkinvv_2025]: https://doi.org/10.36652/0869-4931-2025-79-11-509-513
[research_vlahostergios_komnos_2018]: https://doi.org/10.1504/pcfd.2018.096620
[research_volpe_salcuni_2026]: https://doi.org/10.1109/lcsys.2026.3704983
[research_voracek_1990]: https://ntrs.nasa.gov/citations/19910009768
[research_voracek_clarke_1994]: https://doi.org/10.2514/3.46505
[research_voracekdavidf_clarkerobert_1991]: https://ntrs.nasa.gov/citations/19910047389
[research_voting_software_1993]: https://doi.org/10.1016/0967-0661(93)92298-i
[research_voulgaris_1994]: https://doi.org/10.1109/9.299632
[research_vukelich_stoy_1988_b]: https://doi.org/10.21236/ada211086
[research_vukobratovic_stojic_1985]: https://doi.org/10.1016/s1474-6670(17)60398-7
[research_wada_tamayama_2020]: https://doi.org/10.1088/2631-8695/abbb59
[research_wagg_2022]: https://doi.org/10.25518/2684-6500.84
[research_waggonereg_batesbl_1989]: https://ntrs.nasa.gov/citations/19910014824
[research_waggonereg_jennettla_1986]: https://ntrs.nasa.gov/citations/19870045310
[research_wahler_ma_2025]: https://doi.org/10.3390/aerospace12020077
[research_waitman_marcos_2019]: https://doi.org/10.1016/j.ifacol.2019.11.184
[research_waitman_marcos_2020]: https://doi.org/10.2514/1.g004618
[research_wakimoto_chiba_2021]: https://doi.org/10.3390/aerospace8080217
[research_walchli_guyton_1992]: https://doi.org/10.2514/6.1992-4427
[research_walchlilawrencea_1994]: https://ntrs.nasa.gov/citations/19950007845
[research_walker_claudio_2024]: https://doi.org/10.1007/s42979-024-02874-6
[research_walker_hall_1968]: https://doi.org/10.1017/s0001925900004741
[research_walker_kaufman_1977]: https://doi.org/10.21236/ada042114
[research_walkersa_1976]: https://ntrs.nasa.gov/citations/19760024070
[research_walkerth_minguetpj_1997]: https://ntrs.nasa.gov/citations/19970016009
[research_walshkevinr_1993]: https://ntrs.nasa.gov/citations/19930013934
[research_wan_yang_2003]: https://doi.org/10.2514/6.2003-1416
[research_wang_2019]: https://doi.org/10.1063/1.5087963
[research_wang_2021]: https://doi.org/10.1080/0305215x.2021.2004136
[research_wang_2024]: https://doi.org/10.2316/j.2024.201-0461
[research_wang_2024_b]: https://doi.org/10.1088/1742-6596/2762/1/012050
[research_wang_2026]: https://doi.org/10.1590/jatm.v18.1450
[research_wang_baker_2019]: https://doi.org/10.1016/j.compstruct.2018.09.038
[research_wang_chen_2021]: https://doi.org/10.1016/j.compstruct.2020.113422
[research_wang_chu_2017]: https://doi.org/10.1016/j.ifacol.2017.08.320
[research_wang_daronch_2018]: https://doi.org/10.3390/aerospace5030086
[research_wang_feng_2025]: https://doi.org/10.3390/aerospace12080659
[research_wang_gao_2016]: https://doi.org/10.1007/s00348-016-2184-y
[research_wang_guo_2015]: https://doi.org/10.1002/acs.2585
[research_wang_hou_2022]: https://doi.org/10.1109/access.2022.3213938
[research_wang_hu_2021]: https://doi.org/10.1177/14759217211056831
[research_wang_hu_2026]: https://doi.org/10.1016/j.ast.2025.111272
[research_wang_ji_2025]: https://doi.org/10.1016/j.ast.2025.110533
[research_wang_kampen_2019]: https://doi.org/10.2514/1.g003497
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
[research_wang_mkhoyan_2021]: https://doi.org/10.2514/1.g005870
[research_wang_peeters_2021]: https://doi.org/10.1088/1757-899x/1024/1/012020
[research_wang_qing_2016]: https://doi.org/10.1115/1.4032630
[research_wang_qiu_2019]: https://doi.org/10.1177/1475921719850641
[research_wang_rogers_1991]: https://doi.org/10.1177/002199839102500405
[research_wang_song_2024]: https://doi.org/10.1155/2024/7481513
[research_wang_song_2025]: https://doi.org/10.1016/j.amf.2025.200202
[research_wang_su_2017]: https://doi.org/10.1088/1742-6596/916/1/012006
[research_wang_su_2018]: https://doi.org/10.1088/1757-899x/452/4/042048
[research_wang_sun_2024]: https://doi.org/10.3390/aerospace11050366
[research_wang_sun_2025]: https://doi.org/10.2514/1.g009257
[research_wang_tai_2022]: https://doi.org/10.3390/aerospace9110689
[research_wang_thevendran_1993]: https://doi.org/10.1006/jsvi.1993.1153
[research_wang_tian_2025]: https://doi.org/10.1016/j.cma.2025.118323
[research_wang_vankampen_2019]: https://doi.org/10.2514/1.g003980
[research_wang_vankampen_2019_b]: https://doi.org/10.2514/1.g003791
[research_wang_wan_2021]: https://doi.org/10.1016/j.compstruct.2020.113201
[research_wang_wang_1994]: https://doi.org/10.1061/(asce)0733-9445(1994)120:1(200)
[research_wang_wang_2023]: https://doi.org/10.1177/14759217231166119
[research_wang_wang_2025]: https://doi.org/10.1016/j.compstruct.2025.119590
[research_wang_wang_2025_b]: https://doi.org/10.3390/aerospace12121076
[research_wang_wei_2026]: https://doi.org/10.1109/taes.2026.3663140
[research_wang_wen_2021]: https://doi.org/10.1177/0142331221989007
[research_wang_weng_2026]: https://doi.org/10.1016/j.engappai.2026.115261
[research_wang_wu_2015]: https://doi.org/10.1007/s11071-015-2083-4
[research_wang_wu_2021]: https://doi.org/10.1016/j.jfluidstructs.2021.103286
[research_wang_wynn_2018]: https://doi.org/10.2514/1.c034684
[research_wang_xia_2022]: https://doi.org/10.1016/j.addma.2022.102717
[research_wang_xu_2016]: https://doi.org/10.1016/j.cja.2016.10.010
[research_wang_xu_2018]: https://doi.org/10.3390/s18103447
[research_wang_yi_2026]: https://doi.org/10.1007/s11431-025-3198-1
[research_wang_zhan_2006]: https://doi.org/10.2514/1.20283
[research_wang_zhang_2020]: https://doi.org/10.1016/j.cja.2020.03.016
[research_wang_zhang_2021]: https://doi.org/10.1016/j.addma.2021.102341
[research_wang_zhang_2022]: https://doi.org/10.3390/sym14061154
[research_wang_zhang_2022_b]: https://doi.org/10.3390/app12189268
[research_wang_zhao_2022]: https://doi.org/10.2514/1.j060909
[research_wang_zhao_2022_b]: https://doi.org/10.3390/aerospace9080433
[research_wang_zheng_2022]: https://doi.org/10.1088/1742-6596/2187/1/012046
[research_wang_zhou_2024]: https://doi.org/10.1016/j.apm.2024.01.044
[research_wang_zhou_2026]: https://doi.org/10.2514/1.c038983
[research_wang_zhu_2016]: https://doi.org/10.1016/j.jfluidstructs.2016.01.009
[research_wang_zhu_2020]: https://doi.org/10.1007/s11432-018-9795-y
[research_wangjohnt_1996]: https://ntrs.nasa.gov/citations/19960020473
[research_wangjohnt_jegleydawnc_1996]: https://ntrs.nasa.gov/citations/19960048076
[research_wansaseub_sleesongsom_2020]: https://doi.org/10.1007/s42405-019-00246-6
[research_wansasueb_panagant_2023]: https://doi.org/10.1007/s00707-023-03756-3
[research_wardlaw_andrewb_1975]: https://doi.org/10.21236/ada020356
[research_wasson_mehus_1967]: https://doi.org/10.2514/3.43843
[research_wauters_2021]: https://doi.org/10.1115/1.4052009
[research_wauters_2022]: https://doi.org/10.1177/17568293221092139
[research_weatherill_zartarian_1958]: https://doi.org/10.21236/ad0142154
[research_webb_rogers_2021]: https://doi.org/10.2514/1.c036206
[research_webblannied_mccainwilliame_1988]: https://ntrs.nasa.gov/citations/19890006537
[research_weed_carlson_1983]: https://doi.org/10.21236/ada129573
[research_wei_chen_2017]: https://doi.org/10.2514/1.c034079
[research_wei_du_2019]: https://doi.org/10.1115/1.4045599
[research_wei_freris_2024]: https://doi.org/10.1007/s00371-024-03402-6
[research_wei_meng_2024]: https://doi.org/10.1002/rnc.7526
[research_wei_xu_2020]: https://doi.org/10.1109/access.2020.2964728
[research_wei_zhan_2019]: https://doi.org/10.1108/aeat-08-2017-0181
[research_weidemann_leondes_1979]: https://doi.org/10.21236/ada072259
[research_weihs_katz_1986]: https://doi.org/10.2514/3.9418
[research_weinert_meyer_1984]: https://doi.org/10.21236/ada141875
[research_weiser_ossmann_2020]: https://doi.org/10.1007/s13272-020-00461-y
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
[research_wells_2002]: https://doi.org/10.21236/ada398917
[research_wen_song_2023]: https://doi.org/10.3390/aerospace10121001
[research_werdes_1953]: https://doi.org/10.2514/8.2666
[research_werter_debreuker_2016]: https://doi.org/10.1016/j.compstruct.2016.09.044
[research_westin_balthazar_2023]: https://doi.org/10.3390/axioms12090826
[research_wheatcroft_groh_2025]: https://doi.org/10.1017/aer.2025.10113
[research_wheatcroft_mahadik_2025]: https://doi.org/10.2514/1.j065343
[research_whitbeck_hofmann_1978]: https://doi.org/10.21236/ada067177
[research_whitbeck_smith_1982]: https://doi.org/10.21236/ada134175
[research_white_geubelle_2005]: https://doi.org/10.21236/ada443864
[research_white_hartl_2025]: https://doi.org/10.1016/j.cma.2025.117911
[research_white_mongru_2017]: https://doi.org/10.1177/1475921717738389
[research_white_padfield_2021]: https://doi.org/10.1007/s13272-021-00542-6
[research_white_richardp_1961]: https://doi.org/10.21236/ad0328509
[research_whiteedwardv_kapaniarakeshk_2015]: https://ntrs.nasa.gov/citations/20150017734
[research_whiteheadrs_foremancr_1992]: https://ntrs.nasa.gov/citations/19950022016
[research_whitlowwoodrowjr_bennettrobertm_1991]: https://ntrs.nasa.gov/citations/19930063025
[research_whitworth_1987]: https://doi.org/10.1177/002199838702100405
[research_wickman_1953]: https://doi.org/10.21236/ada953108
[research_wie_byun_1989]: https://doi.org/10.2514/3.20384
[research_wiggenraadjfm_bauldnrjr_1993]: https://ntrs.nasa.gov/citations/19930044546
[research_wildermuth_rothammer_1974]: https://doi.org/10.21236/ada002873
[research_wildermuth_rothammer_1974_b]: https://doi.org/10.21236/ada002854
[research_wilhelm_schafranek_1986]: https://doi.org/10.2514/3.45377
[research_williams_1952]: https://doi.org/10.2514/8.2400
[research_williams_1980]: https://doi.org/10.2514/3.50797
[research_willsky_1984]: https://doi.org/10.21236/ada147758
[research_willsky_verghese_1984]: https://doi.org/10.21236/ada140931
[research_willsky_verghese_1985]: https://doi.org/10.21236/ada166234
[research_wilson_champneys_2024]: https://doi.org/10.1177/14759217241297098
[research_wilson_riccardi_2022]: https://doi.org/10.1016/j.actaastro.2022.07.013
[research_wilson_riley_1993]: https://doi.org/10.21236/ada273685
[research_wilsondavidj_citurskevind_1994]: https://ntrs.nasa.gov/citations/19950007833
[research_wing_buffeting_2018]: https://doi.org/10.15372/pmtf20180406
[research_winny_1950]: https://doi.org/10.1017/s0001925900000196
[research_wise_sedwick_1999]: https://doi.org/10.21236/ada386935
[research_wissler_gilliam_1987]: https://doi.org/10.2514/6.1987-1322
[research_witte_monson_2003]: https://doi.org/10.21236/ada421043
[research_wolfe_1967]: https://doi.org/10.1108/eb034268
[research_wollner_1972]: https://doi.org/10.2514/3.58993
[research_wood_araujoestrada_2019]: https://doi.org/10.2514/1.c035416
[research_wood_livingston_1971]: https://doi.org/10.21236/ada021266
[research_woodcockrj_georgefl_1976]: https://ntrs.nasa.gov/citations/19760024077
[research_woodrm_millerds_1985]: https://ntrs.nasa.gov/citations/19850053430
[research_woods_dayyani_2015]: https://doi.org/10.2514/1.c032725
[research_woods_gilbert_1990]: https://doi.org/10.2514/3.25336
[research_woodsjessicaa_gilbertmichaelg_1989]: https://ntrs.nasa.gov/citations/19890014953
[research_wooldridge_1960]: https://doi.org/10.1108/eb033272
[research_wrestler_cliftong_1965]: https://doi.org/10.21236/ad0622404
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
[research_wu_tong_2017]: https://doi.org/10.36959/422/431
[research_wu_wang_2025]: https://doi.org/10.1007/s11071-025-10975-x
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
[research_x_29_experiment_1991]: https://ntrs.nasa.gov/citations/19940010854
[research_x_29_research_1991]: https://ntrs.nasa.gov/citations/19940014489
[research_xia_chen_2015]: https://doi.org/10.1016/j.proeng.2015.11.214
[research_xia_li_2016]: https://doi.org/10.1115/1.4034113
[research_xia_li_2026]: https://doi.org/10.26599/ocean.2026.9470017
[research_xiang_liu_2018]: https://doi.org/10.1108/aeat-04-2017-0101
[research_xiang_liu_2024]: https://doi.org/10.1177/01423312241277269
[research_xiang_wang_2023]: https://doi.org/10.1061/jaeeez.aseng-4658
[research_xiao_dong_2019]: https://doi.org/10.1002/acs.3069
[research_xiao_harrison_2021]: https://doi.org/10.1016/j.compstruct.2020.113526
[research_xiao_liu_2018]: https://doi.org/10.1016/j.ifacol.2018.09.371
[research_xie_li_2021]: https://doi.org/10.1137/20m1345517
[research_xie_liu_2016]: https://doi.org/10.1155/2016/5090719
[research_xie_meng_2017]: https://doi.org/10.1155/2017/2564314
[research_xie_zhang_2025]: https://doi.org/10.3390/aerospace12060525
[research_xie_zhao_2016]: https://doi.org/10.1002/acs.2666
[research_xijuan_qiang_2016]: https://doi.org/10.2514/1.c033252
[research_xinbing_wen_2020]: https://doi.org/10.1088/1742-6596/1605/1/012075
[research_xiong_tang_2026]: https://doi.org/10.1109/taes.2026.3683617
[research_xiong_xu_2025]: https://doi.org/10.2514/1.c038510
[research_xu_fan_2015]: https://doi.org/10.1016/j.neucom.2015.02.069
[research_xu_feng_2025]: https://doi.org/10.1016/j.cja.2025.103443
[research_xu_gao_2015]: https://doi.org/10.1155/2015/258315
[research_xu_guo_2015]: https://doi.org/10.1002/acs.2596
[research_xu_han_2019]: https://doi.org/10.2514/6.2019-3291
[research_xu_liu_2026]: https://doi.org/10.1177/14759217261457103
[research_xu_saleh_2019]: https://doi.org/10.2514/1.j057573
[research_xu_tan_2019]: https://doi.org/10.1016/j.cja.2019.06.003
[research_xu_tian_2024]: https://doi.org/10.1061/jaeeez.aseng-5007
[research_xu_wang_2016]: https://doi.org/10.1371/journal.pone.0167168
[research_xu_xia_2016]: https://doi.org/10.1155/2016/4706925
[research_xu_zha_2021]: https://doi.org/10.2514/1.c035727
[research_xu_zhang_2018]: https://doi.org/10.12783/dtcse/mmsta2017/19666
[research_xu_zhang_2020]: https://doi.org/10.1109/access.2020.3041855
[research_xu_zhang_2026]: https://doi.org/10.1007/s00158-026-04374-y
[research_xue_yao_2020]: https://doi.org/10.2322/tjsass.63.1
[research_xue_ye_2019]: https://doi.org/10.1080/19942060.2019.1663264
[research_xue_yunsong_2021]: https://doi.org/10.1177/0036850421998137
[research_yagil_raveh_2018]: https://doi.org/10.2514/1.c034353
[research_yahagi_1971]: https://doi.org/10.1080/00207177108932066
[research_yalvac_yats_1991]: https://doi.org/10.1177/002199839102501206
[research_yamamoto_1992]: https://doi.org/10.2514/3.11227
[research_yamasaki_epureanu_2017]: https://doi.org/10.1016/j.ijnonlinmec.2016.12.009
[research_yamasaki_gotoh_1971]: https://doi.org/10.2208/jscej1969.1971.187_49
[research_yan_han_2025]: https://doi.org/10.2174/0118722121302573240527051750
[research_yan_li_2019]: https://doi.org/10.1051/jnwpu/20193740656
[research_yang_2024]: https://doi.org/10.3390/electronics13020308
[research_yang_batra_1994]: https://doi.org/10.1088/0964-1726/3/4/011
[research_yang_fu_2024]: https://doi.org/10.3390/aerospace11020107
[research_yang_gao_2020]: https://doi.org/10.1109/tac.2019.2918122
[research_yang_guan_2018]: https://doi.org/10.2514/1.g003586
[research_yang_guruswamy_1980]: https://doi.org/10.21236/ada084172
[research_yang_huang_2017]: https://doi.org/10.2514/1.g002690
[research_yang_huang_2019]: https://doi.org/10.1016/j.jsv.2019.01.006
[research_yang_lee_2015]: https://doi.org/10.1155/2015/218384
[research_yang_li_2026]: https://doi.org/10.2514/1.c038587
[research_yang_liu_1976]: https://doi.org/10.21236/ada040077
[research_yang_przekwas_1993]: https://doi.org/10.2514/6.1993-2976
[research_yang_striz_1981]: https://doi.org/10.2514/3.57576
[research_yang_tang_2026]: https://doi.org/10.1038/s41597-026-07769-0
[research_yang_wan_1978]: https://doi.org/10.21236/ada061942
[research_yang_wang_2025]: https://doi.org/10.1080/23307706.2025.2486673
[research_yang_wang_2026]: https://doi.org/10.1016/j.cja.2026.104412
[research_yang_wu_2025]: https://doi.org/10.1063/5.0280452
[research_yang_xiao_2024]: https://doi.org/10.2514/1.c037399
[research_yang_xie_2019]: https://doi.org/10.1177/0954410019885238
[research_yang_xu_2024]: https://doi.org/10.1007/s11071-024-09764-9
[research_yang_yang_2019]: https://doi.org/10.1016/j.ast.2018.11.050
[research_yang_yue_2015]: https://doi.org/10.1080/0305215x.2014.995175
[research_yang_yue_2016]: https://doi.org/10.1177/0954410016629497
[research_yang_zhang_2023]: https://doi.org/10.1002/rnc.7026
[research_yang_zhang_2026]: https://doi.org/10.1017/aer.2026.10162
[research_yang_zhao_1989]: https://doi.org/10.2514/3.45806
[research_yang_zhao_1992]: https://doi.org/10.1016/0022-460x(92)90528-6
[research_yang_zhao_2016]: https://doi.org/10.1177/1687814016677207
[research_yao_2018]: https://doi.org/10.1504/ijscip.2018.092320
[research_yaseen_bayart_2018]: https://doi.org/10.1016/j.ifacol.2018.09.631
[research_yasue_2020]: https://doi.org/10.2514/1.c035564
[research_yates_1966]: https://doi.org/10.2514/3.43702
[research_yates_wynne_1982]: https://doi.org/10.2514/3.44803
[research_yates_wynne_1983]: https://doi.org/10.2514/3.44952
[research_yatesecarsonjr_chulichuan_1987]: https://ntrs.nasa.gov/citations/19870012837
[research_yatesecjr_wynneec_1981]: https://ntrs.nasa.gov/citations/19810016896
[research_ye_chen_2015]: https://doi.org/10.1155/2015/254975
[research_ye_yang_2024]: https://doi.org/10.1016/j.ast.2024.109161
[research_yeh_1988]: https://ntrs.nasa.gov/citations/19880017310
[research_yeh_1988_b]: https://ntrs.nasa.gov/citations/19890005085
[research_yeh_yeh_1989]: https://doi.org/10.1007/978-94-009-1125-3_30
[research_yeo_atkins_2015]: https://doi.org/10.2514/1.c032682
[research_yi_an_2017]: https://doi.org/10.15837/ijccc.2017.3.2617
[research_yildizyidiray_kolmanovskyilyav_2011]: https://ntrs.nasa.gov/citations/20110016004
[research_yildizyildiray_kolmanovskyilyav_2010]: https://ntrs.nasa.gov/citations/20100033693
[research_yin_chu_2019]: https://doi.org/10.2514/1.g004193
[research_yin_huang_2025]: https://doi.org/10.1007/s11768-024-00240-8
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
[research_young_garg_2018]: https://doi.org/10.1016/j.compstruct.2017.09.112
[research_yu_1987]: https://doi.org/10.1115/1.3173110
[research_yu_2018]: https://doi.org/10.4236/mme.2018.84017
[research_yu_fang_2017]: https://doi.org/10.1016/j.compstruct.2017.05.042
[research_yu_he_2025]: https://doi.org/10.1142/s2301385027500440
[research_yu_lyu_2018]: https://doi.org/10.1016/j.ast.2018.01.016
[research_yu_wang_2017]: https://doi.org/10.1155/2017/1592527
[research_yu_yu_2026]: https://doi.org/10.1109/access.2026.3668314
[research_yu_zhang_2016]: https://doi.org/10.2514/1.g001414
[research_yu_zhang_2023]: https://doi.org/10.3390/s23020574
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
[research_zadvornyak_martynovich_1983]: https://doi.org/10.1007/bf00905638
[research_zakharov_zattoni_2015]: https://doi.org/10.1016/j.jprocont.2015.07.006
[research_zanoni_gerosa_2022]: https://doi.org/10.1007/s42496-022-00107-8
[research_zauner_moise_2023]: https://doi.org/10.1007/s10494-023-00415-4
[research_zauner_sandham_2020]: https://doi.org/10.1103/physrevfluids.5.083903
[research_zaw_baranovski_2026]: https://doi.org/10.3390/aerospace13060563
[research_zaytseva_kuznetsov_2021]: https://doi.org/10.18698/0536-1044-2021-12-3-10
[research_zeiler_1999]: https://doi.org/10.2514/2.2495
[research_zeleke_asfaw_2023]: https://doi.org/10.3103/s1068799823040190
[research_zelenkov_2018]: https://doi.org/10.18372/1990-5548.58.13520
[research_zenisek_1973]: https://doi.org/10.1080/00207177308932381
[research_zha_qiao_2026]: https://doi.org/10.1002/msd2.70061
[research_zhai_li_2020]: https://doi.org/10.2514/1.c035766
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
[research_zhang_ji_2022]: https://doi.org/10.1063/5.0090394
[research_zhang_li_2026]: https://doi.org/10.1080/21642583.2026.2634446
[research_zhang_liu_2018]: https://doi.org/10.1002/asjc.1821
[research_zhang_liu_2019]: https://doi.org/10.1115/1.4043240
[research_zhang_marzocca_2015]: https://doi.org/10.1177/1077546315597180
[research_zhang_qiu_2024]: https://doi.org/10.3390/act13060229
[research_zhang_ran_2023]: https://doi.org/10.3390/app132111844
[research_zhang_rizzi_2017]: https://doi.org/10.1108/aeat-04-2015-0098
[research_zhang_shaw_2021]: https://doi.org/10.1016/j.ast.2021.106534
[research_zhang_song_2025]: https://doi.org/10.1016/j.cja.2025.103463
[research_zhang_sun_2020]: https://doi.org/10.1002/acs.3145
[research_zhang_wang_2015]: https://doi.org/10.4028/www.scientific.net/msf.813.54
[research_zhang_wang_2019]: https://doi.org/10.2514/1.c035182
[research_zhang_wang_2020]: https://doi.org/10.1016/j.jfluidstructs.2019.102836
[research_zhang_wang_2022_b]: https://doi.org/10.1007/s00348-022-03528-0
[research_zhang_wang_2026]: https://doi.org/10.1016/j.cja.2026.104377
[research_zhang_xie_2021]: https://doi.org/10.1016/j.cma.2020.113485
[research_zhang_yang_2018]: https://doi.org/10.1016/j.ast.2018.04.043
[research_zhang_yang_2021]: https://doi.org/10.3390/aerospace8080203
[research_zhang_yang_2025]: https://doi.org/10.2514/1.c038158
[research_zhang_yu_2013]: https://doi.org/10.2514/1.c031740
[research_zhang_zhang_2017]: https://doi.org/10.4208/cicp.oa-2016-0132
[research_zhang_zhang_2023]: https://doi.org/10.3390/aerospace10060521
[research_zhang_zhao_2019]: https://doi.org/10.1016/j.jfluidstructs.2019.01.014
[research_zhang_zhao_2023]: https://doi.org/10.3390/aerospace10020197
[research_zhang_zhao_2023_b]: https://doi.org/10.3390/aerospace10120981
[research_zhang_zhao_2026]: https://doi.org/10.1007/s11071-026-12701-7
[research_zhang_zhou_2015]: https://doi.org/10.2514/1.c032739
[research_zhang_zhou_2024]: https://doi.org/10.1007/s00158-024-03820-z
[research_zhang_zhou_2024_b]: https://doi.org/10.1007/s11424-024-3364-0
[research_zhao_cheng_2019]: https://doi.org/10.1088/1742-6596/1284/1/012010
[research_zhao_ji_2022]: https://doi.org/10.1016/j.addma.2022.102676
[research_zhao_li_2019]: https://doi.org/10.1109/access.2019.2930658
[research_zhao_liu_2026]: https://doi.org/10.1016/j.compstruct.2026.120628
[research_zhao_liu_2026_b]: https://doi.org/10.1155/ijae/4223020
[research_zhao_lu_2024]: https://doi.org/10.1109/taes.2023.3333763
[research_zhao_xu_2024]: https://doi.org/10.3390/drones8090429
[research_zhao_yang_2023]: https://doi.org/10.1109/access.2023.3235482
[research_zhao_yue_2016]: https://doi.org/10.2514/1.c033713
[research_zhao_zhang_2016]: https://doi.org/10.1016/j.ast.2016.07.010
[research_zhao_zhang_2024]: https://doi.org/10.1016/j.jweia.2024.105905
[research_zhao_zhou_2024]: https://doi.org/10.1016/j.probengmech.2024.103686
[research_zheng_dai_2026]: https://doi.org/10.1016/j.ast.2026.113066
[research_zheng_pontillo_2024]: https://doi.org/10.1061/jaeeez.aseng-5003
[research_zhijie_taiyu_2025]: https://doi.org/10.1007/s00348-025-04112-y
[research_zhiqiang_xiaozhe_2016]: https://doi.org/10.5139/ijass.2016.17.4.491
[research_zhirabok_filaretov_2024]: https://doi.org/10.31857/s0005231024070026
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
[research_zhou_raze_2025]: https://doi.org/10.2514/1.c038195
[research_zhou_ruan_2019]: https://doi.org/10.1016/j.compstruct.2019.110932
[research_zhou_ruan_2019_b]: https://doi.org/10.1016/j.compstruct.2019.110985
[research_zhou_shen_2025]: https://doi.org/10.1177/14759217251343880
[research_zhou_wang_2022]: https://doi.org/10.3390/sym14091837
[research_zhou_xu_2019]: https://doi.org/10.1016/j.compstruct.2018.10.035
[research_zhou_yang_2022]: https://doi.org/10.1002/rnc.6503
[research_zhou_ye_1989]: https://doi.org/10.1016/b978-0-08-040185-0.50012-9
[research_zhou_yu_2018]: https://doi.org/10.1016/j.jfluidstructs.2018.03.009
[research_zhu_du_2017]: https://doi.org/10.1007/s11071-017-3382-8
[research_zhu_duan_2015]: https://doi.org/10.1108/aeat-06-2013-0112
[research_zhu_li_2019]: https://doi.org/10.2514/1.j058011
[research_zhu_shi_2022]: https://doi.org/10.1063/5.0076173
[research_zhu_wang_2017]: https://doi.org/10.2514/1.c034129
[research_zhu_zhang_2024]: https://doi.org/10.1016/j.ast.2024.109745
[research_zhu_zhou_2025]: https://doi.org/10.2514/1.g008194
[research_zhuang_yang_2021]: https://doi.org/10.1016/j.compstruct.2020.112996
[research_ziakos_kilimtzidis_2025]: https://doi.org/10.1007/s13272-025-00851-0
[research_zipperer_jenney_1975]: https://doi.org/10.21236/ada012233
[research_zipperer_jenney_1975_b]: https://doi.org/10.21236/ada009156
[research_zohar_erel_1988]: https://doi.org/10.2514/3.45578
[research_zong_sun_2021]: https://doi.org/10.1088/1742-6596/1786/1/012024
[research_zou_huang_2022]: https://doi.org/10.2514/1.g006114
[research_zou_huang_2024]: https://doi.org/10.1016/j.ymssp.2024.111717
[research_zou_huang_2025]: https://doi.org/10.1016/j.ast.2025.110155
[research_zou_huang_2025_b]: https://doi.org/10.1115/1.4070097
[research_zou_mu_2021]: https://doi.org/10.1016/j.jfranklin.2021.01.012
[research_zou_yao_2017]: https://doi.org/10.2514/1.c034029
[research_zuhri_2025]: https://doi.org/10.55981/ijoa.2025.9106
[research_zuo_chen_2015]: https://doi.org/10.1155/2015/753042
[research_zuo_min_2016]: https://doi.org/10.1177/0142331216636189
[research_zvonarev_leontev_2025]: https://doi.org/10.3103/s1068799825040014
