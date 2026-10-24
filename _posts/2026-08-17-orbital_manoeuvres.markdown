---
layout: post
mathjax: true
comments: true
title: "Orbital Manoeuvres in Terms of Delta-v"
date: 2026-08-17 09:00:00 +0000
categories: space space-studies
---

<!-- A381 -->
<script>console.log("A381");</script>

An orbital manoeuvre is a change in a spacecraft's velocity made to change its orbit
[Orbital Maneuver][ref_orbital_maneuver].
This article collects the manoeuvres found in a standard orbital mechanics textbook
and expresses each one as a change in velocity,
or delta-v,
written $\Delta v$.
It deliberately does not ask where the delta-v comes from.
A chemical rocket,
an ion engine,
a mass driver
and a gravity assist can all supply it,
and the manoeuvre is the same.
The one exception is a section on the rocket equation,
which connects delta-v to the mass a rocket must carry and the mass it can shed.

An earlier article on this site surveys space studies,
including the rocket equation,
the Hohmann transfer,
plane changes
and the Oberth effect,
in a few paragraphs each
[Introduction to Space Studies][related_post_space_studies].
This article treats the manoeuvres in more depth,
with worked numbers,
and adds compound and advanced manoeuvres.
General references include the orbital manoeuvres chapter of Curtis
[Curtis 2020][book_curtis_2020_maneuvers]
and the astrodynamics text of Battin
[Battin 1999][book_battin_1999].
Every number is computed from the equations shown,
for point masses and,
unless stated,
for instantaneous burns.

## Delta-v as the Currency

Delta-v is a scalar measure of the change in velocity a manoeuvre requires.
It is not the same as the physical change in the spacecraft's velocity,
and for several manoeuvres in sequence the delta-v values add
[Delta-v][ref_delta_v].
It does not depend on the spacecraft's mass,
so moving a heavy satellite and a light one between the same orbits takes the same delta-v,
although the heavy one needs more propellant
[Delta-v Budget][ref_delta_v_budget].
That independence is what makes delta-v the natural currency of mission design.

### The Impulsive Approximation

Most textbook manoeuvres treat a burn as instantaneous,
changing the velocity but not the position.
Studies and manoeuvre optimization commonly use this approximation,
and when thrust is applied in short bursts the other accelerations during the burn may be negligible
[Delta-v][ref_delta_v].
For burns that do not,
the vehicle pays an additional cost treated in the section on losses.

### Energy and Speed

Every manoeuvre in this article follows from the conservation of energy and angular momentum on a conic orbit.
For a body of gravitational parameter $\mu$,
the speed $v$ at distance $r$ on an orbit of semi-major axis $a$ is given by the vis-viva equation
[Vis-viva Equation][ref_vis_viva_equation].

$$
v^{2} = \mu\left(\frac{2}{r} - \frac{1}{a}\right)
$$

Setting $a = r$ gives the circular speed,
and letting $a$ grow without bound gives the escape speed.

$$
v_{c} = \sqrt{\frac{\mu}{r}}, \qquad
v_{\mathrm{esc}} = \sqrt{\frac{2\mu}{r}} = \sqrt{2}\,v_{c}
$$

In a circular low Earth orbit,
or LEO,
300 kilometres above Earth's equatorial radius,
the circular speed is 7.726 kilometres per second,
the escape speed is 10.926
and the period is 90.5 minutes.
In geostationary orbit,
or GEO,
at a radius of 42,164 kilometres,
the circular speed is 3.075 kilometres per second and the period is 23.934 hours.
These two orbits serve as the running example below.

Three further quantities recur throughout.
The specific orbital energy is fixed by the semi-major axis,
the specific angular momentum by the speed and the flight path angle $\gamma$ measured from the local horizontal,
and the period by the semi-major axis alone.

$$
\varepsilon = \frac{v^{2}}{2} - \frac{\mu}{r} = -\frac{\mu}{2a}, \qquad
h = r\,v\cos\gamma, \qquad
T = 2\pi\sqrt{\frac{a^{3}}{\mu}}
$$

The periods of 90.5 minutes and 23.934 hours above come from the last of these.
A burn that changes the speed at a given point changes $\varepsilon$ and therefore $a$,
which is why every manoeuvre below can be costed with the vis-viva equation.

## The Rocket Equation and Mass-Shedding Delta-v

### The Rocket Equation

A rocket gains speed by throwing mass backward.
If it expels propellant at an exhaust speed $v_{e}$ relative to itself,
conservation of momentum gives $m\,dv = -v_{e}\,dm$,
and integrating from an initial mass $m_{0}$ to a final mass $m_{f}$ gives the following.

$$
\Delta v = v_{e}\ln\frac{m_{0}}{m_{f}}, \qquad
\frac{m_{0}}{m_{f}} = \exp\left(\frac{\Delta v}{v_{e}}\right)
$$

The equation is named after Konstantin Tsiolkovsky,
who published it in 1903,
although William Moore had outlined it as early as 1810
[Tsiolkovsky Rocket Equation][ref_tsiolkovsky_rocket_equation].
Johnson has published the contents of Moore's treatise on the motion of rockets with a commentary
[Johnson 1995][research_johnson_1995].
Its consequence is that delta-v grows only with the logarithm of the mass ratio,
so the mass ratio grows exponentially with the delta-v demanded.

<div style="overflow-x: auto;" markdown="1">

| $\Delta v / v_{e}$ | Mass ratio $m_{0}/m_{f}$ | Fraction of initial mass that is propellant |
|---|---|---|
| 0.5 | 1.65 | 0.393 |
| 1 | 2.72 | 0.632 |
| 2 | 7.39 | 0.865 |
| 3 | 20.09 | 0.950 |
| 4 | 54.60 | 0.982 |

</div>

Because delta-v values add,
the mass ratios of successive burns multiply
[Delta-v][ref_delta_v],
and a mission budget can be built burn by burn.
The equation applies to any device that expels reaction mass,
including a mass driver used as a reaction engine
[Mass Driver][ref_mass_driver].
A 1977 design study of such an engine as an upper stage for the Space Shuttle
would accelerate segments of spent external tankage to exhaust velocities of 8 to 10 kilometres per second
[Unattributed 1977][research_mass_driver_reaction_engine_1977].

Two further relations connect the rocket equation to engine data.
The exhaust speed is the specific impulse $I_{\mathrm{sp}}$ multiplied by standard gravity $g_{0}$,
and the fraction of the starting mass that must be propellant follows from the mass ratio,
as in the last column of the table.

$$
v_{e} = g_{0}\,I_{\mathrm{sp}}, \qquad
\frac{m_{p}}{m_{0}} = 1 - \exp\left(-\frac{\Delta v}{v_{e}}\right)
$$

### Staging

A vehicle must carry structure,
meaning tanks,
engines
and frames,
and that structure is still aboard when the propellant runs out.
Let the structural ratio $\varepsilon$ of a stage be its empty mass divided by its empty mass plus propellant
[Multistage Rocket][ref_multistage_rocket].
A single stage carrying no payload then reaches at most the following.

$$
\Delta v_{\max} = v_{e}\ln\frac{1}{\varepsilon}
$$

With $v_{e} = 3.5$ kilometres per second,
a specific impulse of 357 seconds,
and $\varepsilon = 0.1$,
that limit is 8.06 kilometres per second,
less than the 9.3 to 10 kilometres per second needed to reach low Earth orbit from the ground
[Delta-v Budget][ref_delta_v_budget].
Both values of $v_{e}$ and $\varepsilon$ are illustrative assumptions.

Staging sheds structure on the way.
The idea is old,
and the oldest known multistage rocket is described in the fourteenth century Chinese Huolongjing
[Multistage Rocket][ref_multistage_rocket].
Malina and Summerfield addressed the problem of escape from Earth by rocket in 1947
[Malina and Summerfield 1947][research_malina_summerfield_1947],
and optimum staging was treated as an explicit optimization problem by 1957
[Schurmann 1957][research_schurmann_1957].
Each stage is dropped when its propellant is spent,
so the stages that follow do not carry it.
For $N$ identical stages sharing a total delta-v equally,
each with structural ratio $\varepsilon$,
the payload fraction of the whole vehicle is the following.

$$
\frac{m_{\mathrm{payload}}}{m_{0}} = \left[\frac{e^{-\Delta v/(N v_{e})} - \varepsilon}{1 - \varepsilon}\right]^{N}
$$

The table applies this to a delta-v of 9.4 kilometres per second with the same assumptions.

<div style="overflow-x: auto;" markdown="1">

| Number of stages | Mass ratio per stage | Payload fraction |
|---|---|---|
| 1 | 14.67 | impossible |
| 2 | 3.830 | 0.0320 |
| 3 | 2.448 | 0.0403 |
| 4 | 1.957 | 0.0435 |
| 10 | 1.308 | 0.0481 |
| continuous shedding | not applicable | 0.0506 |

</div>

Adding stages always helps under these assumptions,
which matches the general result for stages of equal specific impulse,
structural ratio and payload ratio
[Multistage Rocket][ref_multistage_rocket],
but the gains shrink quickly.
The last row is the limit of infinitely many stages,
in which structure is shed continuously in proportion to the propellant burned.
If a mass $\varepsilon/(1-\varepsilon)$ of structure is dropped for each unit of propellant,
then $m\,dv = -v_{e}(1-\varepsilon)\,dm$ for the total mass,
and the following result replaces the rocket equation.

$$
\Delta v = v_{e}\,(1-\varepsilon)\ln\frac{m_{0}}{m_{f}}
$$

Continuous shedding behaves like a single stage with no structure at a reduced exhaust speed $(1-\varepsilon)v_{e}$.
It is the upper bound that real staging approaches.

### Shedding Mass Does Not Itself Change Velocity

Dropping mass without pushing it changes nothing at that moment,
because the dropped mass leaves with the vehicle's own velocity and carries its own momentum away.
The benefit comes only in later burns,
which accelerate less mass.
Consider a vehicle of 100 tonnes carrying 80 tonnes of propellant,
with the same exhaust speed.
Burning all the propellant with the structure aboard gives 5.633 kilometres per second.
Dropping 3 tonnes of empty tank after the first 40 tonnes are burned gives 6.022.
The drop added 0.389 kilometres per second without adding any propellant.
This is the delta-v that mass shedding provides.

In symbols,
a vehicle that burns from $m_{0}$ to $m_{1}$,
drops a dead mass $m_{d}$,
and then burns to $m_{f}$ gains the following,
which exceeds the single-burn value $v_{e}\ln(m_{0}/(m_{f}+m_{d}))$ obtained by keeping the dead mass to the end.

$$
\Delta v = v_{e}\ln\frac{m_{0}}{m_{1}} + v_{e}\ln\frac{m_{1} - m_{d}}{m_{f}}
$$

### Losses

Real burns take time,
and the delta-v a vehicle must supply exceeds the ideal values in this article.
Gravity loss is the cost of holding a rocket up in a gravity field while it thrusts,
and it is smallest when thrust is high and the burn short
[Gravity Loss][ref_gravity_loss].
One of the simplest ascent programs is the gravity turn,
which keeps the thrust always parallel to the velocity,
and even its idealized equations are nonlinear and need numerical integration
[Culler and Fried 1957][research_culler_fried_1957].
A rocket rising vertically loses 0.59 kilometres per second for every minute it burns at Earth's surface.
Over a burn of duration $t_{b}$ with flight path angle $\gamma$ the loss is the following integral,
which for a vertical climb at constant gravity reduces to $g\,t_{b}$.

$$
\Delta v_{g} = \int_{0}^{t_{b}} g\sin\gamma\,dt
$$

The launch budget of 9.3 to 10 kilometres per second to low Earth orbit exceeds the circular speed of 7.73 by 1.57 to 2.27,
which is attributed to gravity losses,
steering losses
and atmospheric drag
[Gravity Loss][ref_gravity_loss].
The orbital manoeuvres that follow are calculated without losses,
which is the textbook convention.

## Single-Impulse Manoeuvres

### Raising or Lowering the Opposite Apsis

A burn along the direction of motion at one apsis raises the opposite apsis,
and a burn against it lowers the opposite apsis.
For a burn at radius $r_{1}$ that changes the orbit's semi-major axis from $a$ to $a'$,
the vis-viva equation gives the following.

$$
\Delta v = \sqrt{\mu\left(\frac{2}{r_{1}} - \frac{1}{a'}\right)} - \sqrt{\mu\left(\frac{2}{r_{1}} - \frac{1}{a}\right)}
$$

Circularization is the special case that sets $a' = r_{1}$,
and deorbiting is the case that lowers the far apsis into the atmosphere.

### Plane Change

Changing the orbital plane by an angle $\Delta i$ without changing the speed requires a burn at one of the two points where the old and new planes cross.
The delta-v is the change in the velocity vector,
which for an unchanged speed $v$ is the following.

$$
\Delta v = 2v\sin\frac{\Delta i}{2}
$$

The cost is proportional to speed,
so a plane change is cheapest where the orbit is slowest,
at apoapsis
[Orbital Inclination Change][ref_orbital_inclination_change].
In low Earth orbit a change of 1 degree costs 0.135 kilometres per second and a change of 28.5 degrees costs 3.803.
In geostationary orbit the same changes cost 0.054 and 1.514.
A change of 60 degrees costs exactly the orbital speed,
because $2\sin 30^{\circ} = 1$.
Plane changes can take a very large amount of delta-v,
so mission planners try to launch a spacecraft directly into the desired inclination or as close to it as possible
[Orbital Inclination Change][ref_orbital_inclination_change].

On an elliptical orbit the speed at the node depends on where the node lies.
For an orbit of semi-major axis $a$,
eccentricity $e$,
mean motion $n = \sqrt{\mu/a^{3}}$
and argument of periapsis $\omega$,
a burn at true anomaly $f$ that changes the inclination by $\Delta i$ costs the following
[Orbital Inclination Change][ref_orbital_inclination_change].

$$
\Delta v_{i} = \frac{2\sin\left(\Delta i/2\right)\left(1 + e\cos f\right) n\,a}{\sqrt{1 - e^{2}}\,\cos\left(\omega + f\right)}
$$

For a circular orbit this reduces to $2v\sin(\Delta i/2)$.

### Combining a Plane Change with a Speed Change

When a burn changes both speed and direction,
the delta-v is the vector difference,
given by the law of cosines.

$$
\Delta v = \sqrt{v_{1}^{2} + v_{2}^{2} - 2 v_{1} v_{2}\cos\Delta i}
$$

This is always less than doing the speed change and the plane change separately,
because the two share one burn
[Geostationary Transfer Orbit][ref_geostationary_transfer_orbit].
The example of a transfer to geostationary orbit below shows the size of the saving.

## Two-Impulse Transfers

### The Hohmann Transfer

The Hohmann transfer moves a spacecraft between two coplanar circular orbits of radii $r_{1}$ and $r_{2}$ using an ellipse that touches both,
with one burn at each end
[Hohmann Transfer Orbit][ref_hohmann_transfer_orbit].
With transfer semi-major axis $a_{t} = (r_{1}+r_{2})/2$ the two burns and the flight time are the following.

$$
\Delta v_{1} = \sqrt{\frac{\mu}{r_{1}}}\left(\sqrt{\frac{2 r_{2}}{r_{1}+r_{2}}} - 1\right), \qquad
\Delta v_{2} = \sqrt{\frac{\mu}{r_{2}}}\left(1 - \sqrt{\frac{2 r_{1}}{r_{1}+r_{2}}}\right), \qquad
t = \pi\sqrt{\frac{a_{t}^{3}}{\mu}}
$$

From the 300 kilometre orbit to geostationary orbit in the same plane,
the burns are 2.426 and 1.467 kilometres per second,
3.893 in total,
and the transfer takes 5.28 hours.
The transfer ellipse has a perigee speed of 10.151 and an apogee speed of 1.608 kilometres per second.
The published delta-v table lists 3.90 kilometres per second from an equatorial low Earth orbit to geostationary orbit
[Delta-v Budget][ref_delta_v_budget],
in agreement.

Measured as a fraction of the starting orbit's speed $v_{1}$,
the Hohmann delta-v depends only on the ratio $R = r_{2}/r_{1}$.
It is not greatest for the largest ratio.
It rises to a maximum and then falls toward $\sqrt{2}-1$,
the cost of escape.
The maximum occurs at $R = 15.5817$,
the positive root of $x^{3} - 15x^{2} - 9x - 1 = 0$
[Hohmann Transfer Orbit][ref_hohmann_transfer_orbit].
The formulas above give a maximum of 0.5363 $v_{1}$,
or 53.6 percent,
at that ratio.
The cited article states 53.0 percent,
which the formulas do not reproduce.

Written in terms of the ratio,
the normalized cost and the condition for its maximum are the following.

$$
\frac{\Delta v_{H}}{v_{1}} = \sqrt{\frac{2R}{1+R}} - 1 + \frac{1}{\sqrt{R}} - \sqrt{\frac{2}{R\,(1+R)}}, \qquad
R^{3} - 15R^{2} - 9R - 1 = 0 \ \text{at the maximum}
$$

### General Two-Impulse Transfers and Lambert's Problem

A Hohmann transfer often uses the lowest possible impulse for a transfer between circular coplanar orbits
[Hohmann Transfer Orbit][ref_hohmann_transfer_orbit],
but it fixes the flight time and requires the target to be in the right place on arrival.
Pontani showed with ordinary calculus and a graphical construction that the Hohmann and bielliptic transfers are the two possible global optima between two elliptic orbits,
with no restriction on the number of impulses,
and that the choice between them depends on the apsides of the two orbits
[Pontani 2009][research_pontani_2009].
When the departure point,
the arrival point
and the flight time are all fixed,
the transfer orbit is found by solving Lambert's problem,
which determines an orbit from two position vectors and the time of flight
[Lambert's Problem][ref_lamberts_problem].
For interplanetary missions the delta-v is often plotted against launch date on a porkchop plot
[Delta-v][ref_delta_v],
and Lambert's problem is often solved in conjunction with the patched conic approximation
to estimate the launch energy and the capture manoeuvres
[Lambert's Problem][ref_lamberts_problem].
Lambert solvers remain an active subject.
Battin and Vaughan removed the singularity of Gauss's method at a transfer angle of 180 degrees
and obtained convergence that is rapid and essentially independent of the initial guess
[Battin and Vaughan 1984][research_battin_vaughan_1984],
Gooding published a solution procedure for Lambert's orbital boundary-value problem
[Gooding 1990][research_gooding_1990],
Avanzini parameterized the solutions by the component of the eccentricity vector perpendicular to the chord
[Avanzini 2008][research_avanzini_2008],
and Izzo revisited the problem in 2014
[Izzo 2014][research_izzo_2014].
Lambert's problem also has applications in preliminary orbit determination
[Lambert's Problem][ref_lamberts_problem],
the subject of a chapter of Curtis
[Curtis 2020][book_curtis_2020_orbit_determination].

## Three-Impulse Transfers

### The Bi-elliptic Transfer

A bi-elliptic transfer uses two half-ellipses and three burns.
The first burn raises the apoapsis to an intermediate radius $r_{b}$ beyond the target,
the second burn at $r_{b}$ raises the periapsis to $r_{2}$,
and the third at $r_{2}$ circularizes.
The idea was published by Ary Sternfeld in 1934
[Bi-elliptic Transfer][ref_bi_elliptic_transfer],
and Hoelker and Silber analysed the bi-elliptical transfer between coplanar circular orbits in 1961
[Hoelker and Silber 1961][research_hoelker_silber_1961].
With $a_{1} = (r_{1}+r_{b})/2$ and $a_{2} = (r_{2}+r_{b})/2$ the three burns are the following.

$$
\Delta v_{1} = \sqrt{\mu\left(\frac{2}{r_{1}} - \frac{1}{a_{1}}\right)} - \sqrt{\frac{\mu}{r_{1}}}, \quad
\Delta v_{2} = \sqrt{\mu\left(\frac{2}{r_{b}} - \frac{1}{a_{2}}\right)} - \sqrt{\mu\left(\frac{2}{r_{b}} - \frac{1}{a_{1}}\right)}, \quad
\Delta v_{3} = \sqrt{\mu\left(\frac{2}{r_{2}} - \frac{1}{a_{2}}\right)} - \sqrt{\frac{\mu}{r_{2}}}
$$

The second burn is cheap because it happens far out,
where the spacecraft is slow.
In the limit $r_{b} \to \infty$ the transfer becomes bi-parabolic,
and its total cost in units of $v_{1}$ is the following.

$$
\frac{\Delta v_{\mathrm{biparabolic}}}{v_{1}} = \left(\sqrt{2} - 1\right)\left(1 + \frac{1}{\sqrt{R}}\right)
$$

Bisecting for the ratio at which this equals the Hohmann cost gives $R = 11.939$.
Above that ratio some bi-elliptic transfers are cheaper than the Hohmann transfer,
depending on the intermediate radius chosen
[Bi-elliptic Transfer][ref_bi_elliptic_transfer].
The table gives costs in units of $v_{1}$.

<div style="overflow-x: auto;" markdown="1">

| Ratio $R$ | Hohmann | Bi-elliptic, $r_{b} = 2r_{2}$ | Bi-elliptic, $r_{b} = 1000\,r_{1}$ | Bi-parabolic |
|---|---|---|---|---|
| 2 | 0.2845 | 0.4663 | 0.7060 | 0.7071 |
| 11.94 | 0.5341 | 0.5393 | 0.5344 | 0.5341 |
| 15.58 | 0.5363 | 0.5328 | 0.5198 | 0.5192 |
| 20 | 0.5347 | 0.5256 | 0.5079 | 0.5068 |
| 50 | 0.5137 | 0.4967 | 0.4756 | 0.4728 |
| 100 | 0.4931 | 0.4768 | 0.4604 | 0.4556 |

</div>

The saving is small and slow.
For $R = 20$ starting from the 300 kilometre orbit,
a bi-elliptic transfer with $r_{b} = 40\,r_{1}$ saves 0.070 kilometres per second,
4.061 against 4.131,
but takes 194.0 hours against 25.7 for the Hohmann transfer.
The bi-elliptic flight time is the sum of two half-periods,
which grows quickly with the intermediate radius.

$$
t_{\mathrm{bi}} = \pi\sqrt{\frac{a_{1}^{3}}{\mu}} + \pi\sqrt{\frac{a_{2}^{3}}{\mu}}
$$

That tradeoff is why the bi-elliptic transfer is a textbook staple and a rarity in practice.

### Plane Change at a High Apoapsis

The same idea applies to plane changes.
A spacecraft can raise its apoapsis,
change plane there at low speed,
and lower its apoapsis again,
for a total of three burns,
and in some cases this needs less total delta-v
[Orbital Inclination Change][ref_orbital_inclination_change].
The table compares this with a single plane change from the 300 kilometre orbit.

<div style="overflow-x: auto;" markdown="1">

| Plane change | Single burn, km/s | Via apoapsis at $5\,r_{1}$, km/s | Via apoapsis at $10\,r_{1}$, km/s | Via apoapsis at $20\,r_{1}$, km/s |
|---|---|---|---|---|
| 45 degrees | 5.913 | 6.023 | 6.181 | 6.282 |
| 60 degrees | 7.726 | 6.491 | 6.425 | 6.407 |
| 90 degrees | 10.926 | 7.317 | 6.857 | 6.628 |

</div>

The three-burn route loses at 45 degrees and wins at 60 and above in these cases.
The break-even angle and the best apoapsis depend on the case,
and in these cases a large plane change is cheaper by going far out first.

## A Compound Example, Low Earth Orbit to Geostationary Orbit

The inclination of a transfer orbit is set by the latitude of the launch site and the launch direction
[Geostationary Transfer Orbit][ref_geostationary_transfer_orbit],
so a launch due east from a site at 28.5 degrees latitude gives an inclination of about 28.5 degrees,
while geostationary orbit lies in the equatorial plane.
The orbit must be both raised and rotated.
Three strategies compare as follows,
with a 300 kilometre starting orbit.

- **Separately.** A Hohmann transfer of 3.893 kilometres per second followed by a 28.5 degree plane change in geostationary orbit, 1.514, gives 5.406.
- **Combined at apogee.** Doing the whole plane change with the apogee burn, by the law of cosines with an apogee speed of 1.608 and a final speed of 3.075, makes that burn 1.830 and the total 4.256.
- **Split optimally.** Doing 2.20 degrees of the plane change at perigee and 26.30 at apogee gives the minimum, 4.231.

The published table lists 4.33 kilometres per second to geostationary orbit
from a low Earth orbit inclined at 28 degrees as from Kennedy Space Center
[Delta-v Budget][ref_delta_v_budget],
about 0.1 kilometres per second above the optimal split computed here for 28.5 degrees.
In practice the inclination and eccentricity of a geostationary transfer orbit are usually removed together in one burn at apogee,
where the velocity is lowest
[Geostationary Transfer Orbit][ref_geostationary_transfer_orbit].
Combining the burns saves 1.15 kilometres per second over doing them separately,
which is the largest single lesson of this example.

## Phasing and Rendezvous

### Phasing

Two spacecraft in the same orbit at different positions cannot close the gap by thrusting toward each other.
Instead the chaser moves to a phasing orbit with a different period,
completes one revolution of it,
and returns to the original orbit when the target arrives at the same point
[Orbit Phasing][ref_orbit_phasing].
The same idea extends to a phasing orbit flown for several revolutions.
To catch a target that is ahead by a phase angle $\theta$ in $k$ revolutions,
the chaser needs a phasing orbit of the following period,
where $T$ is the period of the original orbit.

$$
T_{\mathrm{ph}} = T\left(1 - \frac{\theta}{2\pi k}\right)
$$

A target ahead needs a smaller and faster phasing orbit,
which the chaser enters by slowing down
[Orbit Phasing][ref_orbit_phasing],
and the return to the original orbit costs the same burn in reverse.
In a 400 kilometre circular orbit with a period of 92.56 minutes,
catching a target 30 degrees ahead in one revolution would need a phasing orbit of 84.85 minutes,
whose perigee would lie 364 kilometres below Earth's surface.
Spreading the catch over three revolutions needs a period of 89.99 minutes,
a perigee 148 kilometres up,
and a total of 146.1 metres per second.
The phasing orbit's semi-major axis follows from its period,
and since both burns happen at the same point on a circular orbit of speed $v_{c}$,
the total cost is twice the speed difference there.

$$
a_{\mathrm{ph}} = \left[\mu\left(\frac{T_{\mathrm{ph}}}{2\pi}\right)^{2}\right]^{1/3}, \qquad
\Delta v_{\mathrm{ph}} = 2\left|v_{c} - \sqrt{\mu\left(\frac{2}{r} - \frac{1}{a_{\mathrm{ph}}}\right)}\right|
$$
Phasing trades time for delta-v,
and the trade is often forced by the planet's surface or atmosphere.

### Relative Motion and the Clohessy-Wiltshire Equations

Near a target in a circular orbit,
the motion of a chaser is described to first order by the Clohessy-Wiltshire equations
[Clohessy-Wiltshire Equations][ref_clohessy_wiltshire_equations].
Clohessy and Wiltshire derived the equations of motion in a relative coordinate system for satellite rendezvous in 1960
[Clohessy and Wiltshire 1960][research_clohessy_wiltshire_1960].
Early results on relative orbital motion had been published by Hill in 1878,
in a paper on the motion of the Moon relative to Earth
[Clohessy-Wiltshire Equations][ref_clohessy_wiltshire_equations]
[Hill 1878][research_hill_1878].
For targets on elliptical orbits the equations acquire time-dependent coefficients,
and Yamanaka and Ankersen derived a state transition matrix valid for any eccentricity below one
[Yamanaka and Ankersen 2002][research_yamanaka_ankersen_2002].
With $x$ radial,
$y$ along the direction of motion,
$z$ normal to the orbit,
and $n = \sqrt{\mu/r^{3}}$ the target's mean motion,
the equations without thrust are the following.

$$
\ddot{x} - 3n^{2}x - 2n\dot{y} = 0, \qquad
\ddot{y} + 2n\dot{x} = 0, \qquad
\ddot{z} + n^{2}z = 0
$$

They explain the counterintuitive behaviour of orbital rendezvous.
A chaser in a circular orbit a small height $\Delta r$ below the target has a shorter period,
so it gains on the target by $3\pi\,\Delta r$ along the orbit in each revolution.
At 400 kilometres a chaser 1 kilometre lower gains 9.42 kilometres per orbit.
The result follows from the mean motion.
A small change in radius $\Delta r$ changes $n$,
and over one period $2\pi/n$ the along-track separation $\Delta y$ grows as follows.

$$
\Delta n = -\frac{3}{2}\,n\,\frac{\Delta r}{r}, \qquad
\Delta y_{\mathrm{orbit}} = -3\pi\,\Delta r
$$

Thrusting toward a target raises the chaser's orbit and makes it fall behind.
The equations reduce rendezvous planning to linear algebra,
and Curtis treats relative motion and rendezvous together in one chapter
[Curtis 2020][book_curtis_2020_rendezvous].

## Escape, Capture and the Oberth Effect

### Departure

A spacecraft leaving a planet for another needs a hyperbolic excess speed $v_{\infty}$,
the speed left over far from the planet
[Hyperbolic Trajectory][ref_hyperbolic_trajectory].
A single burn in a circular parking orbit of radius $r$ provides it at the following cost.

$$
\Delta v = \sqrt{v_{\infty}^{2} + \frac{2\mu}{r}} - \sqrt{\frac{\mu}{r}}
$$

Leaving the 300 kilometre orbit with an excess of 2.94 kilometres per second,
roughly what a Hohmann transfer to Mars needs
[Patched Conic Approximation][ref_patched_conic_approximation]
and what the Hohmann equations above give as 2.945,
costs 3.589.
Escaping first and then adding the excess separately would cost 6.140.
The difference is the Oberth effect.
A burn made deep in a gravity well,
where the spacecraft is fast,
adds more kinetic energy than the same burn made outside it
[Oberth Effect][ref_oberth_effect].
Blanco and Mungan show from introductory mechanics that this involves no violation of any conservation law,
only the relation between impulse and kinetic energy for a rocket that can also change its gravitational potential energy
[Blanco and Mungan 2019][research_blanco_mungan_2019].
The reason is the following identity for the change in kinetic energy per unit mass from a burn $\Delta v$ along the velocity $v$.

$$
\Delta\left(\frac{v^{2}}{2}\right) = v\,\Delta v + \frac{\Delta v^{2}}{2}
$$

A burn of 1 kilometre per second at the low orbit's 7.726 kilometres per second adds 8.23 megajoules per kilogram,
against 0.50 for the same burn from rest.
The square of the excess speed is the characteristic energy,
$C_{3} = v_{\infty}^{2}$,
which is commonly used in planning interplanetary missions
[Hyperbolic Trajectory][ref_hyperbolic_trajectory].

### Capture

Arriving at a planet is departure in reverse,
except that the best place to burn is not always as low as possible.
For capture into a circular orbit the cost $\sqrt{v_{\infty}^{2} + 2\mu/r} - \sqrt{\mu/r}$ has a minimum.
Capture into an ellipse of eccentricity $e$ is cheapest when the periapsis is at the following radius,
where the cost is also given.

$$
r_{p,\mathrm{opt}} = \frac{2\mu}{v_{\infty}^{2}}\,\frac{1-e}{1+e}, \qquad
\Delta v_{\min} = v_{\infty}\sqrt{\frac{1-e}{2}}
$$

For Mars,
arriving with an excess of 2.65 kilometres per second
[Patched Conic Approximation][ref_patched_conic_approximation],
which the Hohmann equations give as 2.649,
the best circular capture is at a radius of 12,197 kilometres for 1.874 kilometres per second,
against 2.092 at 300 kilometres altitude and 1.978 at three times the optimal radius.
Capture into an ellipse is far cheaper.
For $e = 0.9$ the formula's optimal periapsis radius of 642 kilometres lies inside Mars,
so the real optimum is the lowest safe periapsis,
and capture with a periapsis 300 kilometres up costs 0.803.
A spacecraft can capture into a long ellipse and then lower the apoapsis later,
by burning or by aerobraking.
Aerocapture and aerobraking have each been assessed,
the first in a cost-benefit analysis across a mission set
[Hall, Noca and Bailey 2005][research_hall_noca_bailey_2005]
and the second as a matter of cost and risk
[Spencer and Tolson 2007][research_spencer_tolson_2007].

### Patched Conics

Interplanetary trajectories are commonly approximated by the patched conic method,
which gives each body a sphere of influence and treats the spacecraft as moving under one body at a time
[Patched Conic Approximation][ref_patched_conic_approximation].
The departure and capture burns above are joined by a heliocentric transfer,
such as the Hohmann transfer in the worked example of a flight from Earth to Mars
[Patched Conic Approximation][ref_patched_conic_approximation].
Curtis devotes a chapter to interplanetary trajectories
[Curtis 2020][book_curtis_2020_interplanetary].

Three equations carry this method.
The sphere of influence of a planet of mass $m$ orbiting a star of mass $M$ at distance $a$ has the approximate radius below
[Sphere of Influence][ref_sphere_of_influence],
the synodic period of two orbits of periods $T_{1}$ and $T_{2}$ is the interval between alignments,
and a Hohmann transfer from radius $r_{1}$ to $r_{2}$ requires the target to lead by the phase angle $\theta_{H}$ at departure.

$$
r_{\mathrm{SOI}} \approx a\left(\frac{m}{M}\right)^{2/5}, \qquad
T_{\mathrm{syn}} = \left|\frac{1}{T_{1}} - \frac{1}{T_{2}}\right|^{-1}, \qquad
\theta_{H} = \pi\left[1 - \left(\frac{r_{1}+r_{2}}{2r_{2}}\right)^{3/2}\right]
$$

For Mars the sphere of influence is about 577,000 kilometres,
and for a Hohmann transfer from Earth to Mars the target leads by 44.3 degrees at departure.
Because the required phase angle recurs once per synodic period,
so does each launch opportunity.

## Gravity Assists

A gravity assist uses a planet's motion to change a spacecraft's heliocentric velocity without propellant,
typically to save propellant and reduce expense
[Gravity Assist][ref_gravity_assist].
In the planet's frame the spacecraft enters and leaves with the same excess speed,
only rotated.
For a flyby with periapsis radius $r_{p}$ the turn angle $\delta$ and the resulting change in velocity are the following.

$$
\sin\frac{\delta}{2} = \frac{1}{1 + r_{p}v_{\infty}^{2}/\mu}, \qquad
\left|\Delta\vec{v}\right| = 2v_{\infty}\sin\frac{\delta}{2}
$$

<div style="overflow-x: auto;" markdown="1">

| Flyby | Excess speed, km/s | Turn angle | Velocity change, km/s |
|---|---|---|---|
| Earth, 300 km altitude | 5 | 89.6 degrees | 7.05 |
| Mars, 300 km altitude | 5 | 37.0 degrees | 3.17 |
| Jupiter, periapsis at 2 Jupiter radii | 5.64 | 150.1 degrees | 10.90 |
| Jupiter, periapsis at 1.1 Jupiter radii | 5.64 | 157.7 degrees | 11.07 |

</div>

The velocity change is a change of direction in the planet's frame.
Whether it raises or lowers the heliocentric speed depends on the geometry of the flyby.
A powered flyby adds a burn at periapsis and gains from the Oberth effect
[Oberth Effect][ref_oberth_effect].
With a periapsis speed $v_{p}$ and a burn $\Delta v$ there,
the outgoing excess speed is the following.

$$
v_{p} = \sqrt{v_{\infty}^{2} + \frac{2\mu}{r_{p}}}, \qquad
v_{\infty,\mathrm{out}} = \sqrt{\left(v_{p} + \Delta v\right)^{2} - \frac{2\mu}{r_{p}}}
$$

At Jupiter with a periapsis at 2 Jupiter radii,
a burn of 0.5 kilometres per second raises the excess speed from 5.64 to 8.66,
and a burn of 1.0 raises it to 10.89.

## Low-Thrust Spirals

An engine with very low thrust cannot make impulsive burns.
It spirals slowly between orbits,
thrusting along the direction of motion.
If the orbit stays nearly circular,
its specific energy is $-v^{2}/2$,
and thrusting along the velocity with acceleration $a$ changes the energy at the rate $va$.
So $-v\,dv = va\,dt$,
and the delta-v for the whole spiral is simply the difference of circular speeds.

$$
\Delta v_{\mathrm{spiral}} = \left|v_{c1} - v_{c2}\right|
$$

From the 300 kilometre orbit to geostationary orbit this is 4.651 kilometres per second,
against 3.893 for the Hohmann transfer.
A low-thrust engine pays about 19 percent more delta-v,
but it may need far less propellant because its exhaust speed is much higher
[Delta-v Budget][ref_delta_v_budget].
At a constant acceleration $a$ the spiral takes the following time,
which for 1 millimetre per second squared from the low orbit to geostationary orbit is 53.8 days.

$$
t_{\mathrm{spiral}} = \frac{\left|v_{c1} - v_{c2}\right|}{a}
$$

Edelbaum found minimum-fuel manoeuvres for high and low thrust,
including a closed-form solution for the optimum low-thrust transfer between inclined circular orbits of different radii
[Edelbaum 1961][research_edelbaum_1961].
Kechichian later recast the problem as a minimum-time transfer with a single inverse-tangent expression for the inclination,
valid for all transfers,
at a small delta-v penalty relative to the exact solution
[Kechichian 1997][research_kechichian_1997].

## Beyond Two Bodies

Every manoeuvre above uses one or two gravitating bodies at a time.
Trajectories that exploit three bodies at once can be cheaper.
Low-energy transfers,
also called weak stability boundary trajectories,
include ballistic capture,
and they take longer than higher-energy transfers such as Hohmann transfers
[Low-Energy Transfer][ref_low_energy_transfer].
Japan's Hiten used a weak stability boundary transfer
[Belbruno and Carrico 2000][research_belbruno_carrico_2000],
and Europe's SMART-1 is also listed among missions that used low-energy transfers
[Low-Energy Transfer][ref_low_energy_transfer].
Belbruno and Miller described Sun-perturbed transfers to the Moon with ballistic capture through weak stability boundaries,
using about 18 percent less delta-v than a Hohmann transfer to reach a circular lunar orbit,
and noted Hiten's arrival at the Moon on 2 October 1991
[Belbruno and Miller 1993][research_belbruno_miller_1993].
These methods lie at the edge of what introductory textbooks cover.

## Summary of Costs

The table collects the costs computed in this article for the running examples.

<div style="overflow-x: auto;" markdown="1">

| Manoeuvre | Delta-v, km/s |
|---|---|
| Hohmann, 300 km to geostationary, coplanar | 3.893 |
| Slow spiral, same orbits | 4.651 |
| Hohmann plus separate 28.5 degree plane change | 5.406 |
| Hohmann with optimally split plane change | 4.231 |
| Plane change of 28.5 degrees in low Earth orbit | 3.803 |
| Phasing 30 degrees in three revolutions at 400 km | 0.146 |
| Departure from 300 km with an excess of 2.94 | 3.589 |
| Mars capture into a circular orbit, best radius | 1.874 |
| Mars capture into an ellipse of eccentricity 0.9, 300 km periapsis | 0.803 |

</div>

## A Review of the Literature

The manoeuvres above rest on a literature that runs from the 1940s to the present.
This section surveys it by topic.
Each work is described according to its published abstract,
or by its subject alone where it is cited for its title.

### Surveys and Textbooks

Battin's text and Curtis's chapters serve above as general textbook references
[Battin 1999][book_battin_1999]
[Curtis 2020][book_curtis_2020_maneuvers].
Gobetz and Doll surveyed impulsive trajectories,
optimal and nonoptimal,
and classified the known results for reference
[Gobetz and Doll 1969][research_gobetz_doll_1969].
Conway's edited volume on spacecraft trajectory optimization deliberately includes both analytical and numerical approaches,
and records a revolution in how the methods are applied and in the development of numerical optimization
[Conway 2010][book_conway_2010].

### The Rocket Equation, Staging and Ascent

Malina and Summerfield addressed escape from Earth by rocket in 1947
[Malina and Summerfield 1947][research_malina_summerfield_1947],
and Schurmann treated optimum staging of multistage vehicles ten years later
[Schurmann 1957][research_schurmann_1957].
Culler and Fried gave universal solutions for the gravity turn,
which depend on the initial thrust-to-weight ratio and the initial kick angle
[Culler and Fried 1957][research_culler_fried_1957].
The treatment of gravity loss above rests on the cited encyclopedia entry.

### Optimal Impulsive Transfers

Among the early contributions to the theory,
Lawden studied minimal rocket trajectories and derived necessary conditions for optimal ones
[Lawden 1953][research_lawden_1953]
[Lawden 1959][research_lawden_1959].
Ting studied optimum orbital transfer by impulses in 1960
[Ting 1960][research_ting_1960],
Hoelker and Silber analysed the bi-elliptical transfer in 1961
[Hoelker and Silber 1961][research_hoelker_silber_1961],
Barrar compared two-impulse with one-impulse transfer analytically in 1963
[Barrar 1963][research_barrar_1963],
and Edelbaum asked how many impulses a transfer needs
[Edelbaum 1966][research_edelbaum_1966].
Lion and Handelsman extended the definition of the primer vector to nonoptimal as well as optimal trajectories,
giving conditions for when an added impulse or an initial or final coast improves a trajectory,
and showed that in an inverse-square field the primer can be computed analytically
[Lion and Handelsman 1968][research_lion_handelsman_1968].
Jezewski and Rozendaal turned primer vector theory into a method that finds the time,
number
and state of all impulses
[Jezewski and Rozendaal 1968][research_jezewski_rozendaal_1968].
Prussing's chapter gives a modern account of the theory and its applications
[Prussing 2010][book_prussing_2010],
and Pontani proved that Hohmann and bielliptic transfers are the two possible global optima between two elliptic orbits,
with the choice between them set by their apoapsis and periapsis radii
[Pontani 2009][research_pontani_2009].

### Relative Motion and Rendezvous

Early results on relative orbital motion appeared in Hill's researches in lunar theory
[Hill 1878][research_hill_1878]
[Clohessy-Wiltshire Equations][ref_clohessy_wiltshire_equations],
and Clohessy and Wiltshire derived relative-motion equations for satellite rendezvous
[Clohessy and Wiltshire 1960][research_clohessy_wiltshire_1960].
Tschauner and Hempel studied minimum-fuel rendezvous techniques
[Tschauner and Hempel 1965][research_tschauner_hempel_1965],
and Prussing studied optimal fixed-time rendezvous near a circular orbit with four impulses and with two and three
[Prussing 1969][research_prussing_1969]
[Prussing 1970][research_prussing_1970].
Carter surveyed and classified much of the published work on linearized rendezvous and built a state transition matrix for terminal rendezvous near any Keplerian orbit using the Tschauner-Hempel equations
[Carter 1998][research_carter_1998],
and Yamanaka and Ankersen gave a new and simpler state transition matrix valid for arbitrary elliptical orbits
[Yamanaka and Ankersen 2002][research_yamanaka_ankersen_2002].

### Lambert's Problem

Lancaster,
Blanchard
and Devaney published a note on Lambert's theorem in 1966
[Lancaster, Blanchard and Devaney 1966][research_lancaster_blanchard_devaney_1966].
Battin and Vaughan's algorithm removed the 180 degree singularity of Gauss's method
[Battin and Vaughan 1984][research_battin_vaughan_1984],
Gooding gave a solution procedure for the orbital boundary-value problem
[Gooding 1990][research_gooding_1990],
Avanzini gave a simple algorithm that offers no speed advantage over Battin's
[Avanzini 2008][research_avanzini_2008],
and Izzo revisited the problem in 2014
[Izzo 2014][research_izzo_2014].

### Escape, Capture and the Oberth Effect

Blanco and Mungan explain the Oberth effect with introductory physics
[Blanco and Mungan 2019][research_blanco_mungan_2019].
On the use of atmospheres for capture,
Hall,
Noca
and Bailey analysed the costs and benefits of aerocapture across a set of missions
[Hall, Noca and Bailey 2005][research_hall_noca_bailey_2005],
and Spencer and Tolson examined the cost and risk decisions of aerobraking
[Spencer and Tolson 2007][research_spencer_tolson_2007].

### Gravity Assists

Negri and Prado review the theory of gravity assists in the era before spaceflight
[Negri and Prado 2020][research_negri_prado_2020].
Flandro studied solar-electric missions to Jupiter with swingby continuation to the outer planets
[Flandro 1968][research_flandro_1968],
Minovitch studied Jupiter orbiter trajectories driven by encounters with the Galilean satellites
[Minovitch 1972][research_minovitch_1972],
and Broucke treated the celestial mechanics of the gravity assist
[Broucke 1988][research_broucke_1988].
Design methods followed,
with automated design of gravity-assist trajectories to Mars and the outer planets
[Longuski and Williams 1991][research_longuski_williams_1991]
and a graphical method for gravity-assist design
[Strange and Longuski 2002][research_strange_longuski_2002].

### Low-Thrust Transfers

Edelbaum's analysis of controllable satellites gave the closed-form low-thrust transfer between inclined circular orbits
[Edelbaum 1961][research_edelbaum_1961],
and Kechichian reformulated it with optimal control theory
[Kechichian 1997][research_kechichian_1997].
Petropoulos and Longuski developed a shape-based algorithm for low-thrust trajectories with gravity assists
[Petropoulos and Longuski 2004][research_petropoulos_longuski_2004],
and Russell applied primer vector theory to global low-thrust trade studies,
reducing the problem to a few parameters and finding Pareto fronts between flight time and final mass
[Russell 2007][research_russell_2007].

### Low-Energy Transfers

Conley studied low-energy transit orbits in the restricted three-body problem in 1968
[Conley 1968][research_conley_1968].
Belbruno constructed Earth-Moon trajectories ending in lunar capture orbits
[Belbruno 1987][research_belbruno_1987],
and Belbruno and Miller defined weak stability boundaries and described Sun-perturbed transfers whose use Hiten had demonstrated
[Belbruno and Miller 1993][research_belbruno_miller_1993].
Koon,
Lo,
Marsden
and Ross numerically demonstrated a heteroclinic connection between periodic orbits around the first and second Lagrange points
and presented the associated invariant manifolds as tools for understanding dynamical channels throughout the solar system,
relevant to missions such as Genesis
[Koon et al. 2000][research_koon_et_al_2000].
They also addressed low-energy transfer to the Moon
[Koon et al. 2001][research_koon_et_al_2001],
and with Gómez and Masdemont treated connecting orbits and invariant manifolds in the spatial restricted three-body problem
[Gómez et al. 2004][research_gomez_et_al_2004].
Topputo studied optimal two-impulse Earth-Moon transfers in a four-body model
[Topputo 2013][research_topputo_2013].

### Foundations

The two-impulse transfer takes its name from Walter Hohmann,
who described it in a 1925 book
[Hohmann Transfer Orbit][ref_hohmann_transfer_orbit].
The treatment of phasing in this article rests on the cited encyclopedia entry and on the vis-viva equation.

## Epistemic State

**Facts reported by the cited sources.**
The definitions,
the history of the rocket equation and of the bi-elliptic transfer,
the comparison of staging,
the published delta-v budgets,
the bi-elliptic threshold of 11.94,
the root of the Hohmann maximum,
the practice of combining plane and apogee burns,
the description of Lambert's problem,
the Clohessy-Wiltshire history,
and the low-energy missions come from the Wikipedia entries cited.
The findings attributed to Clohessy and Wiltshire,
Edelbaum 1961,
Gobetz and Doll,
Conway,
Culler and Fried,
Pontani,
Lion and Handelsman,
Jezewski and Rozendaal,
Carter,
Yamanaka and Ankersen,
Battin and Vaughan,
Avanzini,
Blanco and Mungan,
Kechichian,
Russell,
Belbruno and Miller,
Koon and coauthors in 2000,
Belbruno and Carrico,
and the 1977 reaction engine study are stated according to their published abstracts.
The 1977 study carries no author in its bibliographic record,
so it is cited as unattributed.
Every other research work and book cited,
including the textbooks of Curtis and Battin,
are cited only for what their titles state.
The findings attributed to sources rest on their abstracts and titles rather than on their full texts.

**Analysis in this article.**
Every delta-v,
time,
mass ratio,
payload fraction
and angle is computed from the equations shown,
for point masses,
circular starting orbits and instantaneous burns.
The continuous-shedding and spiral results are derived here.
The exhaust speed,
structural ratio
and tank example are illustrative assumptions.
The Hohmann maximum computed here,
53.6 percent of the starting orbit's speed,
differs from the 53.0 percent stated in the cited article.

**Inference and judgment.**
The selection of manoeuvres reflects what standard textbooks usually cover,
judged from their chapter titles and the cited summaries rather than from a reading of each book.
The statement that bi-elliptic transfers are rare in practice is a judgment from the time penalty computed here.

**Unaddressed concerns.**
This article does not treat perturbations,
station-keeping,
finite-burn steering in detail,
attitude,
or navigation errors.

## Out of Scope

This article does not cover launch vehicle design,
propulsion technology,
atmospheric entry,
or the numerical methods used to optimize trajectories.

## Conclusion

Every textbook manoeuvre reduces to a change in velocity at a point on an orbit,
and its cost follows from the vis-viva equation and the geometry of vectors.
Tangential burns at the apsides change orbit size cheaply,
plane changes are expensive and belong at the slowest point,
and combining a plane change with a speed change saves more than any other single technique in the examples here.
Three-burn transfers beat two-burn transfers only for large ratios or large plane changes,
and they pay in time.
Burns deep in a gravity well buy more energy,
which is why departures and captures are made low,
except where a planet's gravity makes a higher capture cheaper.

The rocket equation converts all of this into mass,
and its exponential is the reason staging exists.
Shedding structure adds delta-v without adding propellant,
and the limit of shedding it continuously behaves like a structureless rocket with a slower exhaust.
Delta-v itself is indifferent to how it is supplied,
which is what allows the same manoeuvres to be flown by rockets,
sails,
mass drivers
and gravity assists.

## References

- [Book, Battin 1999, An Introduction to the Mathematics and Methods of Astrodynamics, Revised Edition][book_battin_1999]
- [Book, Conway 2010, Spacecraft Trajectory Optimization][book_conway_2010]
- [Book, Curtis 2020, Orbital Mechanics for Engineering Students, Interplanetary Trajectories][book_curtis_2020_interplanetary]
- [Book, Curtis 2020, Orbital Mechanics for Engineering Students, Orbital Maneuvers][book_curtis_2020_maneuvers]
- [Book, Curtis 2020, Orbital Mechanics for Engineering Students, Preliminary Orbit Determination][book_curtis_2020_orbit_determination]
- [Book, Curtis 2020, Orbital Mechanics for Engineering Students, Relative Motion and Rendezvous][book_curtis_2020_rendezvous]
- [Book, Prussing 2010, Primer Vector Theory and Applications, in Spacecraft Trajectory Optimization][book_prussing_2010]
- [Reference, Bi-elliptic Transfer, Wikipedia][ref_bi_elliptic_transfer]
- [Reference, Clohessy-Wiltshire Equations, Wikipedia][ref_clohessy_wiltshire_equations]
- [Reference, Delta-v Budget, Wikipedia][ref_delta_v_budget]
- [Reference, Delta-v, Wikipedia][ref_delta_v]
- [Reference, Geostationary Transfer Orbit, Wikipedia][ref_geostationary_transfer_orbit]
- [Reference, Gravity Assist, Wikipedia][ref_gravity_assist]
- [Reference, Gravity Loss, Wikipedia][ref_gravity_loss]
- [Reference, Hohmann Transfer Orbit, Wikipedia][ref_hohmann_transfer_orbit]
- [Reference, Hyperbolic Trajectory, Wikipedia][ref_hyperbolic_trajectory]
- [Reference, Lambert's Problem, Wikipedia][ref_lamberts_problem]
- [Reference, Low-Energy Transfer, Wikipedia][ref_low_energy_transfer]
- [Reference, Mass Driver, Wikipedia][ref_mass_driver]
- [Reference, Multistage Rocket, Wikipedia][ref_multistage_rocket]
- [Reference, Oberth Effect, Wikipedia][ref_oberth_effect]
- [Reference, Orbit Phasing, Wikipedia][ref_orbit_phasing]
- [Reference, Orbital Inclination Change, Wikipedia][ref_orbital_inclination_change]
- [Reference, Orbital Maneuver, Wikipedia][ref_orbital_maneuver]
- [Reference, Patched Conic Approximation, Wikipedia][ref_patched_conic_approximation]
- [Reference, Sphere of Influence, Wikipedia][ref_sphere_of_influence]
- [Reference, Tsiolkovsky Rocket Equation, Wikipedia][ref_tsiolkovsky_rocket_equation]
- [Reference, Vis-viva Equation, Wikipedia][ref_vis_viva_equation]
- [Related Post, Introduction to Space Studies][related_post_space_studies]
- [Research, Avanzini 2008, A Simple Lambert Algorithm][research_avanzini_2008]
- [Research, Barrar 1963, Two-Impulse Transfer vs One-Impulse Transfer, Analytic Theory][research_barrar_1963]
- [Research, Battin and Vaughan 1984, An Elegant Lambert Algorithm][research_battin_vaughan_1984]
- [Research, Belbruno 1987, Lunar Capture Orbits, a Method of Constructing Earth Moon Trajectories and the Lunar GAS Mission][research_belbruno_1987]
- [Research, Belbruno and Carrico 2000, Calculation of Weak Stability Boundary Ballistic Lunar Transfer Trajectories][research_belbruno_carrico_2000]
- [Research, Belbruno and Miller 1993, Sun-Perturbed Earth-to-Moon Transfers with Ballistic Capture][research_belbruno_miller_1993]
- [Research, Blanco and Mungan 2019, Rocket Propulsion, Classical Relativity, and the Oberth Effect][research_blanco_mungan_2019]
- [Research, Broucke 1988, The Celestial Mechanics of Gravity Assist][research_broucke_1988]
- [Research, Carter 1998, State Transition Matrices for Terminal Rendezvous Studies, Brief Survey and New Example][research_carter_1998]
- [Research, Clohessy and Wiltshire 1960, Terminal Guidance System for Satellite Rendezvous][research_clohessy_wiltshire_1960]
- [Research, Conley 1968, Low Energy Transit Orbits in the Restricted Three-Body Problems][research_conley_1968]
- [Research, Culler and Fried 1957, Universal Gravity Turn Trajectories][research_culler_fried_1957]
- [Research, Edelbaum 1961, Propulsion Requirements for Controllable Satellites][research_edelbaum_1961]
- [Research, Edelbaum 1966, How Many Impulses?][research_edelbaum_1966]
- [Research, Flandro 1968, Solar Electric Low-Thrust Missions to Jupiter with Swingby Continuation to the Outer Planets][research_flandro_1968]
- [Research, Gobetz and Doll 1969, A Survey of Impulsive Trajectories][research_gobetz_doll_1969]
- [Research, Gooding 1990, A Procedure for the Solution of Lambert's Orbital Boundary-Value Problem][research_gooding_1990]
- [Research, Gómez et al. 2004, Connecting Orbits and Invariant Manifolds in the Spatial Restricted Three-Body Problem][research_gomez_et_al_2004]
- [Research, Hall, Noca and Bailey 2005, Cost-Benefit Analysis of the Aerocapture Mission Set][research_hall_noca_bailey_2005]
- [Research, Hill 1878, Researches in the Lunar Theory][research_hill_1878]
- [Research, Hoelker and Silber 1961, The Bi-elliptical Transfer Between Co-planar Circular Orbits][research_hoelker_silber_1961]
- [Research, Izzo 2014, Revisiting Lambert's Problem][research_izzo_2014]
- [Research, Jezewski and Rozendaal 1968, An Efficient Method for Calculating Optimal Free-Space N-Impulse Trajectories][research_jezewski_rozendaal_1968]
- [Research, Johnson 1995, Contents and Commentary on William Moore's A Treatise on the Motion of Rockets and an Essay on Naval Gunnery][research_johnson_1995]
- [Research, Kechichian 1997, Reformulation of Edelbaum's Low-Thrust Transfer Problem Using Optimal Control Theory][research_kechichian_1997]
- [Research, Koon et al. 2000, Heteroclinic Connections Between Periodic Orbits and Resonance Transitions in Celestial Mechanics][research_koon_et_al_2000]
- [Research, Koon et al. 2001, Low Energy Transfer to the Moon][research_koon_et_al_2001]
- [Research, Lancaster, Blanchard and Devaney 1966, A Note on Lambert's Theorem][research_lancaster_blanchard_devaney_1966]
- [Research, Lawden 1953, Minimal Rocket Trajectories][research_lawden_1953]
- [Research, Lawden 1959, Necessary Conditions for Optimal Rocket Trajectories][research_lawden_1959]
- [Research, Lion and Handelsman 1968, Primer Vector on Fixed-Time Impulsive Trajectories][research_lion_handelsman_1968]
- [Research, Longuski and Williams 1991, Automated Design of Gravity-Assist Trajectories to Mars and the Outer Planets][research_longuski_williams_1991]
- [Research, Malina and Summerfield 1947, The Problem of Escape from the Earth by Rocket][research_malina_summerfield_1947]
- [Research, Minovitch 1972, Gravity Thrust Jupiter Orbiter Trajectories Generated by Encountering the Galilean Satellites][research_minovitch_1972]
- [Research, Negri and Prado 2020, A Historical Review of the Theory of Gravity-Assists in the Pre-Spaceflight Era][research_negri_prado_2020]
- [Research, Petropoulos and Longuski 2004, Shape-Based Algorithm for the Automated Design of Low-Thrust, Gravity Assist Trajectories][research_petropoulos_longuski_2004]
- [Research, Pontani 2009, Simple Method to Determine Globally Optimal Orbital Transfers][research_pontani_2009]
- [Research, Prussing 1969, Optimal Four-Impulse Fixed-Time Rendezvous in the Vicinity of a Circular Orbit][research_prussing_1969]
- [Research, Prussing 1970, Optimal Two- and Three-Impulse Fixed-Time Rendezvous in the Vicinity of a Circular Orbit][research_prussing_1970]
- [Research, Russell 2007, Primer Vector Theory Applied to Global Low-Thrust Trade Studies][research_russell_2007]
- [Research, Schurmann 1957, Optimum Staging Technique for Multistaged Rocket Vehicles][research_schurmann_1957]
- [Research, Spencer and Tolson 2007, Aerobraking Cost and Risk Decisions][research_spencer_tolson_2007]
- [Research, Strange and Longuski 2002, Graphical Method for Gravity-Assist Trajectory Design][research_strange_longuski_2002]
- [Research, Ting 1960, Optimum Orbital Transfer by Impulses][research_ting_1960]
- [Research, Topputo 2013, On Optimal Two-Impulse Earth-Moon Transfers in a Four-Body Model][research_topputo_2013]
- [Research, Tschauner and Hempel 1965, Minimum-Fuel Rendezvous Techniques][research_tschauner_hempel_1965]
- [Research, Unattributed 1977, Mass-Driver Reaction Engine as Shuttle Upper-Stage][research_mass_driver_reaction_engine_1977]
- [Research, Yamanaka and Ankersen 2002, New State Transition Matrix for Relative Motion on an Arbitrary Elliptical Orbit][research_yamanaka_ankersen_2002]

[book_battin_1999]: https://doi.org/10.2514/4.861543
[book_conway_2010]: https://doi.org/10.1017/CBO9780511778025
[book_curtis_2020_interplanetary]: https://doi.org/10.1016/b978-0-08-102133-0.00008-8
[book_curtis_2020_maneuvers]: https://doi.org/10.1016/b978-0-08-102133-0.00006-4
[book_curtis_2020_orbit_determination]: https://doi.org/10.1016/b978-0-08-102133-0.00005-2
[book_curtis_2020_rendezvous]: https://doi.org/10.1016/b978-0-08-102133-0.00007-6
[book_prussing_2010]: https://doi.org/10.1017/cbo9780511778025.003
[ref_bi_elliptic_transfer]: https://en.wikipedia.org/wiki/Bi-elliptic_transfer
[ref_clohessy_wiltshire_equations]: https://en.wikipedia.org/wiki/Clohessy%E2%80%93Wiltshire_equations
[ref_delta_v]: https://en.wikipedia.org/wiki/Delta-v
[ref_delta_v_budget]: https://en.wikipedia.org/wiki/Delta-v_budget
[ref_geostationary_transfer_orbit]: https://en.wikipedia.org/wiki/Geostationary_transfer_orbit
[ref_gravity_assist]: https://en.wikipedia.org/wiki/Gravity_assist
[ref_gravity_loss]: https://en.wikipedia.org/wiki/Gravity_loss
[ref_hohmann_transfer_orbit]: https://en.wikipedia.org/wiki/Hohmann_transfer_orbit
[ref_hyperbolic_trajectory]: https://en.wikipedia.org/wiki/Hyperbolic_trajectory
[ref_lamberts_problem]: https://en.wikipedia.org/wiki/Lambert%27s_problem
[ref_low_energy_transfer]: https://en.wikipedia.org/wiki/Low-energy_transfer
[ref_mass_driver]: https://en.wikipedia.org/wiki/Mass_driver
[ref_multistage_rocket]: https://en.wikipedia.org/wiki/Multistage_rocket
[ref_oberth_effect]: https://en.wikipedia.org/wiki/Oberth_effect
[ref_orbit_phasing]: https://en.wikipedia.org/wiki/Orbit_phasing
[ref_orbital_inclination_change]: https://en.wikipedia.org/wiki/Orbital_inclination_change
[ref_orbital_maneuver]: https://en.wikipedia.org/wiki/Orbital_maneuver
[ref_patched_conic_approximation]: https://en.wikipedia.org/wiki/Patched_conic_approximation
[ref_sphere_of_influence]: https://en.wikipedia.org/wiki/Sphere_of_influence_%28astrodynamics%29
[ref_tsiolkovsky_rocket_equation]: https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation
[ref_vis_viva_equation]: https://en.wikipedia.org/wiki/Vis-viva_equation
[related_post_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[research_avanzini_2008]: https://doi.org/10.2514/1.36426
[research_barrar_1963]: https://doi.org/10.2514/3.1470
[research_battin_vaughan_1984]: https://doi.org/10.2514/3.19910
[research_belbruno_1987]: https://doi.org/10.2514/6.1987-1054
[research_belbruno_carrico_2000]: https://doi.org/10.2514/6.2000-4142
[research_belbruno_miller_1993]: https://doi.org/10.2514/3.21079
[research_blanco_mungan_2019]: https://doi.org/10.1119/1.5126818
[research_broucke_1988]: https://doi.org/10.2514/6.1988-4220
[research_carter_1998]: https://doi.org/10.2514/2.4211
[research_clohessy_wiltshire_1960]: https://doi.org/10.2514/8.8704
[research_conley_1968]: https://doi.org/10.1137/0116060
[research_culler_fried_1957]: https://doi.org/10.1063/1.1722828
[research_edelbaum_1961]: https://doi.org/10.2514/8.5723
[research_edelbaum_1966]: https://doi.org/10.2514/6.1966-7
[research_flandro_1968]: https://doi.org/10.2514/3.29416
[research_gobetz_doll_1969]: https://doi.org/10.2514/3.5231
[research_gomez_et_al_2004]: https://doi.org/10.1088/0951-7715/17/5/002
[research_gooding_1990]: https://doi.org/10.1007/BF00049511
[research_hall_noca_bailey_2005]: https://doi.org/10.2514/1.4118
[research_hill_1878]: https://doi.org/10.2307/2369430
[research_hoelker_silber_1961]: https://doi.org/10.1016/0032-0633(61)90297-5
[research_izzo_2014]: https://doi.org/10.1007/s10569-014-9587-y
[research_jezewski_rozendaal_1968]: https://doi.org/10.2514/3.4949
[research_johnson_1995]: https://doi.org/10.1016/0734-743x(94)00052-x
[research_kechichian_1997]: https://doi.org/10.2514/2.4145
[research_koon_et_al_2000]: https://doi.org/10.1063/1.166509
[research_koon_et_al_2001]: https://doi.org/10.1023/a:1013359120468
[research_lancaster_blanchard_devaney_1966]: https://doi.org/10.2514/3.28673
[research_lawden_1953]: https://doi.org/10.2514/8.4642
[research_lawden_1959]: https://doi.org/10.1093/qjmam/12.4.476
[research_lion_handelsman_1968]: https://doi.org/10.2514/3.4452
[research_longuski_williams_1991]: https://doi.org/10.1007/bf00048484
[research_malina_summerfield_1947]: https://doi.org/10.2514/8.1417
[research_mass_driver_reaction_engine_1977]: https://doi.org/10.2514/6.1977-536
[research_minovitch_1972]: https://doi.org/10.2514/3.30391
[research_negri_prado_2020]: https://doi.org/10.1007/s40430-020-02489-x
[research_petropoulos_longuski_2004]: https://doi.org/10.2514/1.13095
[research_pontani_2009]: https://doi.org/10.2514/1.38143
[research_prussing_1969]: https://doi.org/10.2514/3.5246
[research_prussing_1970]: https://doi.org/10.2514/3.5876
[research_russell_2007]: https://doi.org/10.2514/1.22984
[research_schurmann_1957]: https://doi.org/10.2514/8.12965
[research_spencer_tolson_2007]: https://doi.org/10.2514/1.24303
[research_strange_longuski_2002]: https://doi.org/10.2514/2.3800
[research_ting_1960]: https://doi.org/10.2514/8.5305
[research_topputo_2013]: https://doi.org/10.1007/s10569-013-9513-8
[research_tschauner_hempel_1965]: https://doi.org/10.2514/3.28287
[research_yamanaka_ankersen_2002]: https://doi.org/10.2514/2.4875
