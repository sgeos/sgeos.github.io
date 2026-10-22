---
layout: post
mathjax: true
comments: true
title: "Mass Drivers"
date: 2026-08-19 09:00:00 +0000
categories: space space-studies
---

<!-- A383 -->
<script>console.log("A383");</script>

A mass driver is an electromagnetic launcher that accelerates a payload along a track and releases it at high speed
[Mass Driver][ref_mass_driver].
Mass drivers are not yet treated in orbital mechanics textbooks the way rockets and orbital manoeuvres are.
This article attempts that treatment.
It begins with a description of the machine and the equations that govern it,
then follows a payload from release into orbit around the launching body,
then into orbit around that body's parent,
then to another body,
and ends with tracks that circle an entire world.
Every equation is written without assuming a particular body,
track or power source,
and the equations are then evaluated for real bodies in the solar system with hypothetical but plausible infrastructure.

This article builds on two earlier articles on this site.
The first introduces the basic orbital mechanics
[Introduction to Space Studies][related_post_space_studies],
and the second treats the standard orbital manoeuvres in terms of delta-v
[Orbital Manoeuvres in Terms of Delta-v][related_post_orbital_manoeuvres],
which is the language used here for every correction a payload must make after release.
Every number is computed for point masses or uniform spheres of the cited mean radius,
with Keplerian orbits and patched conics,
unless stated otherwise.

## What a Mass Driver Is

A mass driver uses a linear motor to accelerate a payload.
Existing and proposed designs energize coils of wire in sequence,
so that a row of electromagnets pulls or pushes a magnetizable carrier along a path
[Mass Driver][ref_mass_driver].
In the classic design the carrier is a bucket that holds the payload.
At the end of the track the bucket and payload separate,
and the bucket is slowed and recycled for the next launch.
A related design uses linear induction motors of the kind used for the electromagnetic aircraft launch system on modern carriers
[Mass Driver][ref_mass_driver].
A coilgun is the same idea at small scale,
and a railgun drives its projectile by a current through two rails rather than through coils
[Coilgun][ref_coilgun]
[Railgun][ref_railgun].

Because the payload is guided by magnetic levitation,
a mass driver needs no physical contact between moving parts,
and its working life could in principle reach millions of launches.
Most serious designs use superconducting coils and reach efficiencies of 50 to over 90 percent.
A mass driver track has two sections.
In the first the coils are evenly spaced and the acceleration rises with speed up to the maximum the bucket can bear,
and in the second the coils are spaced ever further apart to hold that acceleration constant
[Mass Driver][ref_mass_driver].

The idea is old.
Edwin Northrup described an electric gun in 1937,
and Gerard O'Neill built his first mass driver in 1976 and 1977,
a short test model that fired a projectile at 40 metres per second with an acceleration of 33 times standard gravity
[Mass Driver][ref_mass_driver].
Kolm's reference design for a basic coaxial mass driver explained the principles and optimization procedures
and expected even a table-top system to reach accelerations near 1,000 metres per second squared
[Kolm 1977][research_kolm_1977].
The application that motivated this work was the transport of lunar material to space habitats
[Mass Driver][ref_mass_driver].

On Earth the atmosphere and gravity dominate the problem.
McNab estimated that a railgun launching directly to orbit would need muzzle speeds of at least 7.5 kilometres per second,
and that even launchers over 1,000 metres long would need accelerations over 1,000 times standard gravity,
so only rugged payloads such as fuel,
water
and raw material could be launched
[McNab 2003][research_mcnab_2003].
The StarTram concept accelerates cargo craft in an evacuated tunnel,
and a small rocket burn after release establishes orbit
[Powell and Maise 2008][research_powell_maise_2008].
Wikipedia's summary makes the same point,
that well under a tenth of orbital speed from a small rocket is enough to raise perigee after release
[Mass Driver][ref_mass_driver].
That post-release burn is the central subject of this article.

A mass driver can also be carried by a spacecraft as an engine,
throwing pieces of material backward
[Mass Driver][ref_mass_driver].
One such design study for a Space Shuttle upper stage threw 14 gram segments at 8 to 10 kilometres per second
with a thrust of 560 newtons from 2.9 megawatts at 75 percent efficiency
[Unattributed 1977][research_mass_driver_reaction_engine_1977].
This article treats only fixed mass drivers on the surface of a body.

## Principles and Parametric Equations

### Kinematics

A payload accelerated from rest at a constant acceleration $a$ along a track of length $L$ leaves at speed $v$ after a time $t$.

$$
v^{2} = 2aL, \qquad L = \frac{v^{2}}{2a}, \qquad t = \frac{v}{a}
$$

For a varying acceleration $a(x)$ the first relation generalizes to $v^{2} = 2\int_{0}^{L} a(x)\,dx$.
The track length grows with the square of the release speed,
so doubling the speed needs four times the track at the same acceleration.

### Energy and Power

The kinetic energy delivered per kilogram is $v^{2}/2$.
The instantaneous power that the track must supply to a payload of mass $m$ is greatest at release,
and a launcher that throws a mass flow $\dot{m}$ with electrical efficiency $\eta$ needs an average power that is set only by the speed and the throughput.

$$
\frac{E}{m} = \frac{v^{2}}{2}, \qquad
P_{\mathrm{peak}} = m\,a\,v, \qquad
\bar{P} = \frac{\dot{m}\,v^{2}}{2\eta}
$$

The difference between peak and average power is why energy storage dominates mass driver design,
and why the limits are generally the cost of storing energy that can be discharged quickly and of switching it
[Mass Driver][ref_mass_driver].
The fraction $(1-\eta)$ of the electrical input becomes heat in the track and must be rejected.

### Force from Changing Inductance

The force in any electromagnetic launcher follows from energy conservation.
For a circuit carrying a current $I$ whose inductance $\mathcal{L}(x)$ changes as the payload moves,
the mechanical force at constant current is the following.

$$
F = \frac{1}{2}\,I^{2}\,\frac{d\mathcal{L}}{dx}
$$

In a railgun the inductance grows as the projectile lengthens the circuit,
and in a coilgun it changes as the carrier enters and leaves each coil.
Every design is a way of making $d\mathcal{L}/dx$ large and keeping $I$ high without destroying the conductors.

### Release in the Inertial Frame

A track on a rotating body moves with the surface.
Let the release point be at latitude $\phi$ and radius $r_{0}$,
let the track direction have azimuth $A$ measured from north,
let the payload leave at speed $v_{r}$ relative to the track and at an angle $\gamma$ above the local horizontal,
and let the body rotate with angular rate $\omega$.
The inertial velocity components toward east,
north
and up are the following.

$$
v_{E} = v_{r}\cos\gamma\sin A + \omega r_{0}\cos\phi, \qquad
v_{N} = v_{r}\cos\gamma\cos A, \qquad
v_{U} = v_{r}\sin\gamma
$$

Everything about the payload's subsequent orbit follows from $r_{0}$ and these three components.

### Track Geometry

A straight track of length $L$ that is tangent to a sphere of radius $R$ at its start ends above the surface,
and at its end it points upward relative to the local horizontal.

$$
h_{\mathrm{end}} = \sqrt{R^{2} + L^{2}} - R \approx \frac{L^{2}}{2R}, \qquad
\gamma_{\mathrm{end}} = \arctan\frac{L}{R}
$$

A track that follows the curve of the surface instead must hold the payload on a circular path of radius $R$.
At speed $v$ the payload needs a centripetal acceleration $v^{2}/R$,
of which gravity supplies $g$,
so the track must push it toward the body's centre with the following acceleration.

$$
a_{n} = \frac{v^{2}}{R} - g = g\left[\left(\frac{v}{v_{c}}\right)^{2} - 1\right], \qquad v_{c} = \sqrt{g R}
$$

Below the surface circular speed $v_{c}$ the track supports the payload,
and above it the track holds the payload down.
At the escape speed $\sqrt{2gR}$ the hold-down load equals one local gravity.

### Reaction on the Body

Every launch pushes the body the other way.
A payload of mass $m$ launched at speed $v$ changes the velocity of a body of mass $M$ by $mv/M$,
and a launch along the surface at the equator of a uniform sphere changes its spin rate by the following.

$$
\Delta\omega = \frac{m v R}{I} = \frac{5}{2}\,\frac{m v}{M R}
$$

### The Bodies Used in the Examples

<div style="overflow-x: auto;" markdown="1">

| Body | Mean radius, km | Surface gravity, m/s² | Circular speed at surface, m/s | Escape speed, m/s | Equatorial spin speed, m/s | Hill radius, km |
|---|---|---|---|---|---|---|
| Moon | 1,737.4 | 1.625 | 1,680 | 2,376 | 4.6 | 61,533 |
| Mercury | 2,439.7 | 3.70 | 3,005 | 4,250 | 3.0 | 220,675 |
| Ceres | 469.7 | 0.284 | 365 | 516 | 90.3 | 223,378 |
| Vesta | 262.7 | 0.251 | 257 | 363 | 85.8 | 124,092 |
| Phobos | 11.08 | 0.0058 | 8.0 | 11.3 | 2.5 | 16.6 |
| Deimos | 6.27 | 0.0025 | 3.9 | 5.5 | 0.4 | 21.3 |

</div>

The masses,
radii,
rotation periods
and orbits come from Wikipedia
[Moon][ref_moon]
[Mercury][ref_mercury]
[Ceres][ref_ceres]
[Vesta][ref_vesta]
[Phobos][ref_phobos]
[Deimos][ref_deimos],
and the derived columns are computed for uniform spheres.
Wikipedia lists the escape speed of Phobos as 11.39 metres per second,
slightly above the 11.32 computed for a sphere.
The Hill radius marks roughly where the parent's tides overwhelm the body's own gravity
[Hill Sphere][ref_hill_sphere],
for a body of mass $m$ orbiting a parent of mass $M$ at distance $a$.

$$
r_{H} \approx a\sqrt[3]{\frac{m}{3M}}
$$

Phobos's Hill radius of 16.6 kilometres is smaller than its longest dimension of 25.9 kilometres,
so its surface lies close to the edge of its own gravitational domain.

### Plugging In

A lunar launcher that releases at 2.52 kilometres per second,
a speed used below for sending cargo to Earth,
needs a track of 3.24 kilometres at 100 times standard gravity,
or 0.32 kilometres at 1,000 times,
and delivers 3.18 megajoules per kilogram.
Releasing a 100 kilogram payload at 100 times standard gravity draws a peak power of 247 megawatts.
Exporting a million tonnes a year at that speed with an efficiency of 0.8 needs an average of 126 megawatts.
A 10 kilometre track at 100 times standard gravity reaches 4.43 kilometres per second.
Wikipedia's example of a 1 kilometre superconducting driver that throws 20 kilograms at 10.5 kilometres per second with an average acceleration of 5,600 times standard gravity
[Mass Driver][ref_mass_driver]
is consistent with the kinematic equation,
which gives 1.004 kilometres.
The accelerations assumed here are far beyond the 33 times standard gravity of the first test model
and suit only rugged cargo.

## Launching into Orbit Around the Same Body

### The Orbit After Release

From the release radius $r_{0}$ and inertial speed $v$,
with horizontal component $v_{h} = \sqrt{v_{E}^{2} + v_{N}^{2}}$,
the orbit around a body of gravitational parameter $\mu$ follows from the conservation of energy and angular momentum.

$$
h = r_{0} v_{h}, \qquad
\varepsilon = \frac{v^{2}}{2} - \frac{\mu}{r_{0}}, \qquad
e = \sqrt{1 + \frac{2\varepsilon h^{2}}{\mu^{2}}}, \qquad
r_{p} = \frac{h^{2}/\mu}{1+e}, \qquad
r_{a} = \frac{h^{2}/\mu}{1-e}
$$

The orbit's inclination to the body's equator depends on the latitude and on the inertial azimuth $A_{i}$ of the horizontal velocity,
by spherical trigonometry.

$$
\cos i = \cos\phi\,\sin A_{i}
$$

### Every Release Orbit Returns to the Ground

A Keplerian orbit is a closed curve,
and it passes through every point the payload has occupied,
including the release point.
A payload released horizontally at the surface therefore has its periapsis at the surface,
and one revolution later it returns to the same point in inertial space,
skimming the ground or striking whatever terrain stands there.
A payload released even slightly upward has its periapsis below the surface and strikes the ground before completing the revolution.
A mass driver can therefore never place a payload in a lasting orbit around its own body by itself.
At least one burn by the payload after release is required.

The numbers for the Moon show how unforgiving this is.
Released horizontally at the surface with enough speed to rise to 100 kilometres at apoapsis,
a payload released 0.1 degrees above horizontal has its periapsis 97 metres below the surface and strikes the ground after 352.7 degrees of arc.
Released 1 degree above horizontal,
its periapsis lies 8.9 kilometres down,
and it strikes after 294.1 degrees.
The point of impact follows from the orbit equation $r = p/(1 + e\cos\nu)$ with $p = h^{2}/\mu$.
A payload released upward is already climbing,
so the release point lies at true anomaly $+\nu_{0}$ just after periapsis.
The orbit meets the surface again at $-\nu_{0}$,
just before the next periapsis,
and the arc flown before impact is the following.

$$
\cos\nu_{0} = \frac{p/R - 1}{e}, \qquad
\Delta\psi_{\mathrm{impact}} = 2\left(\pi - \nu_{0}\right)
$$
Even a perfect horizontal release returns after 113 minutes to a point that the Moon's rotation has carried 31.4 kilometres west of the track,
so the return point is wherever the terrain happens to be.
The offset is the distance the surface moves in one orbital period $T$,
at latitude $\phi$.

$$
\Delta x = \omega R\cos\phi\;T
$$

Releasing from a mountain or a tower raises the periapsis to the release height,
which helps only if no terrain under any later pass is higher.
On the Moon,
mass concentrations beneath the large impact basins also perturb low orbits
[Mass Concentration][ref_mass_concentration],
and most low lunar orbits are unstable
[Frozen Orbit][ref_frozen_orbit].

### Corrective Manoeuvres After Release

The standard correction is a single burn at apoapsis that raises the periapsis.
It is the second half of a Hohmann transfer that begins at the surface,
and the equations below are the Hohmann equations of the companion article on manoeuvres specialized to that case
[Orbital Manoeuvres in Terms of Delta-v, The Hohmann Transfer][related_post_orbital_manoeuvres_hohmann].
For a horizontal release at the surface radius $R$ that reaches an apoapsis $r_{a}$,
the release speed and the circularizing burn are the following.

$$
v_{\mathrm{release}} = \sqrt{\frac{2\mu\,r_{a}}{R\,(R + r_{a})}}, \qquad
\Delta v_{\mathrm{circ}} = \sqrt{\frac{\mu}{r_{a}}} - \sqrt{\frac{2\mu R}{r_{a}(R + r_{a})}}
$$

<div style="overflow-x: auto;" markdown="1">

| Lunar apoapsis altitude, km | Inertial release speed, m/s | Track speed eastward at the equator, m/s | Burn to circularize, m/s | Time to apoapsis, min |
|---|---|---|---|---|
| 20 | 1,685.0 | 1,680.4 | 4.79 | 54.6 |
| 50 | 1,692.1 | 1,687.5 | 11.79 | 55.3 |
| 100 | 1,703.5 | 1,698.9 | 23.01 | 56.5 |
| 500 | 1,782.8 | 1,778.1 | 96.25 | 66.2 |

</div>

The burn is small.
Circularizing at 100 kilometres takes 23 metres per second,
1.4 percent of the lunar circular speed,
and costs 0.8 percent of the payload's mass in propellant at an exhaust speed of 3 kilometres per second,
by the propellant fraction $1 - \exp(-\Delta v/v_{e})$ from the rocket equation
[Orbital Manoeuvres in Terms of Delta-v, The Rocket Equation][related_post_orbital_manoeuvres_rocket].
If the goal is only to stop the payload from hitting the ground,
raising the periapsis from the surface to 5,
10
or 20 kilometres costs 1.19,
2.37
or 4.73 metres per second at a 100 kilometre apoapsis.
Raising the periapsis from $R$ to $r_{p}'$ at an apoapsis $r_{a}$ costs the following,
the difference between the apoapsis speeds of the two ellipses.

$$
\Delta v_{\mathrm{raise}} = \sqrt{\frac{2\mu\,r_{p}'}{r_{a}\left(r_{a} + r_{p}'\right)}} - \sqrt{\frac{2\mu R}{r_{a}\left(r_{a} + R\right)}}
$$

Errors in release set the size of the correction budget.

- **Speed.** An error of 1 metre per second in release speed moves a 100 kilometre apoapsis by about 4.44 kilometres, which the apoapsis burn absorbs at little extra cost.
- **Angle.** An upward error of 0.1 degree puts the periapsis 97 metres below the surface, and the burn to raise it to 10 kilometres becomes 2.40 metres per second instead of 2.37. An error of 1 degree raises that burn to 4.50 metres per second.
- **Timing.** The burn must happen within the first revolution, about 56 minutes after release for a 100 kilometre apoapsis. A payload that fails to burn is lost against the ground.
- **Plane.** A plane error is the expensive one. In a 100 kilometre lunar orbit each degree of plane change costs 28.5 metres per second by the plane change equation $2v\sin(\Delta i/2)$ [Orbital Manoeuvres in Terms of Delta-v, Plane Change][related_post_orbital_manoeuvres_plane], more than the whole circularization, so the release azimuth and timing must be right.

The speed sensitivity follows from differentiating the vis-viva equation at the release radius.
With $a$ the transfer ellipse's semi-major axis and $v$ the release speed,
the apoapsis radius $r_{a} = 2a - R$ changes as follows.

$$
\frac{dr_{a}}{dv} = \frac{4a^{2}v}{\mu}
$$

For the 100 kilometre lunar case this is 4.44 kilometres per metre per second.

Over longer times a low orbit needs station-keeping against the perturbations described above,
unless it is one of the lunar frozen orbits,
which lie at inclinations of 27,
50,
76
and 86 degrees
[Frozen Orbit][ref_frozen_orbit].

### Varying Speed, Angle and Point of Release

A mass driver can in principle vary all three of its release parameters,
and each controls a different part of the orbit.

- **Release speed** sets the energy, and for a horizontal release the apoapsis altitude, through the equation above.
- **Release angle** moves the periapsis below the release height and rotates the line of apsides. A horizontal release puts the periapsis exactly at the release point, which is the best case.
- **Release latitude and azimuth** set the inclination through $\cos i = \cos\phi\sin A_{i}$.
- **Release time** sets the orientation of the orbital plane in space, because the body's rotation carries the track around.

Rotation also changes the speed the track must supply.
An eastward track gains the surface speed $\omega R\cos\phi$ and a westward track loses it.
For a circular orbit at the surface the track must therefore supply the following.

$$
v_{\mathrm{track}} = v_{c} \mp \omega R\cos\phi
$$

<div style="overflow-x: auto;" markdown="1">

| Body | Circular speed at the equator, m/s | Spin speed, m/s | Eastward track speed, m/s | Westward track speed, m/s | Ratio |
|---|---|---|---|---|---|
| Moon | 1,680.2 | 4.6 | 1,675.6 | 1,684.8 | 1.006 |
| Mercury | 3,005.1 | 3.0 | 3,002.1 | 3,008.1 | 1.002 |
| Ceres | 365.2 | 90.3 | 274.8 | 455.5 | 1.657 |
| Vesta | 256.5 | 85.8 | 170.7 | 342.4 | 2.005 |

</div>

On the Moon and Mercury rotation hardly matters.
On rapidly spinning small bodies such as Ceres and Vesta it changes the required track speed by a factor of 1.66 to 2.

### A Note on Unbound Launches

A payload whose inertial speed at release exceeds the local escape speed $\sqrt{2\mu/r_{0}}$ is no longer bound to the launching body.
It leaves on a hyperbola and becomes a satellite of the body's parent,
which is the subject of the sections that follow.
Such a payload does not return to the release point,
so the ground-return problem above does not apply,
but its correction problem moves to the parent's orbit and to its destination.

## Positioning a Mass Driver for Orbits Around Its Own Body

The release equations translate directly into siting rules.

**Latitude limits inclination.**
Since $\cos i = \cos\phi\sin A_{i}$,
a site at latitude $\phi$ can reach inclinations only between $\phi$ and $180^{\circ} - \phi$.
An equatorial site can reach every inclination,
while a site at 50 degrees cannot reach an orbit inclined less than 50 degrees.
From the lunar equator,
the frozen inclinations of 27,
50,
76
and 86 degrees need track azimuths of 63.0,
40.0,
14.0
and 4.0 degrees from north.

<div style="overflow-x: auto;" markdown="1">

| Latitude | Azimuth 90° | Azimuth 60° | Azimuth 30° | Azimuth 0° |
|---|---|---|---|---|
| 0° | 0.0° | 30.0° | 60.0° | 90.0° |
| 27° | 27.0° | 39.5° | 63.5° | 90.0° |
| 50° | 50.0° | 56.2° | 71.3° | 90.0° |

</div>

**A fixed track gives fixed inclinations.**
A straight track with azimuth $A$ launches into inclination $i$ in one direction and $180^{\circ} - i$ in the other,
since reversing the azimuth reverses the sign of $\sin A$.
Reaching a different inclination needs a different track.

**Timing gives the plane's orientation.**
The rotation of the body carries a fixed track through every orientation of its plane once per sidereal rotation.
A desired plane is available twice per rotation,
once on the ascending and once on the descending pass,
which on the Moon means about every 13.7 days and on Ceres about every 4.5 hours.
With $P_{\mathrm{sid}}$ the sidereal rotation period the interval between opportunities for one plane is the following.

$$
\Delta t_{\mathrm{plane}} = \frac{P_{\mathrm{sid}}}{2}
$$

A rendezvous with a depot in lunar orbit therefore waits for the plane to come round rather than paying 28.5 metres per second per degree to correct it.

**Direction of launch should follow the spin.**
Eastward tracks gain the surface speed,
which matters on fast-spinning small bodies.

**Straight tracks tilt on small bodies.**
A straight track tangent to the Moon is still within 0.33 degrees of horizontal and 29 metres of the ground after 10 kilometres.
A 1.8 kilometre straight track on Phobos ends 145 metres above the surface and tilted 9.2 degrees upward.
On small bodies a horizontal release needs a curved track that follows the surface,
which brings the curvature load of the earlier equation.

**Elevation helps but does not suffice.**
Releasing from high ground lifts the periapsis above the lowest terrain,
but the orbit's ground track shifts with each revolution as the body turns,
so only a corrective burn makes the orbit safe.

## Launching into Orbit Around the Parent Body

### From the Launching Body to the Parent

A payload released above escape speed leaves the launching body with a hyperbolic excess velocity $\vec{v}_{\infty}$.
In the patched conic approximation the release speed and the payload's velocity relative to the parent are the following,
where $\vec{V}_{B}$ is the launching body's orbital velocity.

$$
v_{\mathrm{release}} = \sqrt{v_{\infty}^{2} + \frac{2\mu_{B}}{R_{B}}}, \qquad
\vec{V}_{\mathrm{payload}} = \vec{V}_{B} + \vec{v}_{\infty}
$$

The direction of $\vec{v}_{\infty}$ relative to $\vec{V}_{B}$ shapes the new orbit.
A prograde excess raises the far apsis of the payload's orbit around the parent,
a retrograde excess lowers the near apsis,
a radial excess rotates the line of apsides,
and an excess out of the body's orbital plane tilts the payload's plane.
For a launching body on a circular orbit of radius $a_{B}$,
the excess needed to reach a near apsis $r_{p}$ by a retrograde release is the following.

$$
v_{\infty} = \sqrt{\frac{\mu_{P}}{a_{B}}} - \sqrt{\frac{2\mu_{P}\,r_{p}}{a_{B}(a_{B} + r_{p})}}
$$

### Release Geometry on a Tidally Locked Body

A payload released horizontally at the surface leaves on a hyperbola with its periapsis at the release point,
and its direction of motion turns as it climbs away.
The hyperbola's eccentricity and the true anomaly $\nu_{\infty}$ of its outgoing asymptote are the following.

$$
e = 1 + \frac{R_{B}\,v_{\infty}^{2}}{\mu_{B}}, \qquad
\nu_{\infty} = \arccos\left(-\frac{1}{e}\right)
$$

Measure the release site by an angle $\theta$ around the body's equator from the sub-parent point,
the point directly beneath the parent,
in the direction of the body's orbital motion.
The asymptote then points at $\theta + \nu_{\infty}$ for a release on a lane moving in the body's direction of spin,
which this article calls the eastward lane,
and at $\theta - \nu_{\infty}$ on a westward lane.
To send the payload in a desired direction $\theta_{d}$,
the site must be at the following angle.

$$
\theta_{\mathrm{east}} = \theta_{d} - \nu_{\infty}, \qquad
\theta_{\mathrm{west}} = \theta_{d} + \nu_{\infty}
$$

The Moon,
Phobos
and Deimos all rotate synchronously,
keeping one face toward their parent
[Tidal Locking][ref_tidal_locking]
[Phobos][ref_phobos]
[Deimos][ref_deimos].
On a synchronous body the direction of orbital motion is fixed relative to the surface,
so a given site always launches in the same direction relative to the body's orbit.
In the frame used here the direction of orbital motion is $\theta_{d} = 90^{\circ}$ and the retrograde direction is $270^{\circ}$.

<div style="overflow-x: auto;" markdown="1">

| Launch | Excess speed, m/s | Release speed, m/s | Eccentricity | $\nu_{\infty}$ | Eastward-lane site | Westward-lane site |
|---|---|---|---|---|---|---|
| Moon to Earth perigee 300 km | 830 | 2,517 | 1.244 | 143.5° | 126.5° | 53.5° |
| Moon to Earth perigee at geostationary radius | 566 | 2,443 | 1.113 | 153.9° | 116.1° | 63.9° |
| Moon to escape from Earth | 422 | 2,413 | 1.063 | 160.2° | 289.8° | 250.2° |
| Phobos to Mars periapsis 100 km | 563 | 563 | 4,950 | 90.0° | 180.0° | 0.0° |
| Phobos to escape from Mars | 885 | 885 | 12,234 | 90.0° | 0.0° | 180.0° |
| Deimos to Mars periapsis 100 km | 664 | 664 | 28,707 | 90.0° | 180.0° | 0.0° |
| Deimos to escape from Mars | 560 | 560 | 20,423 | 90.0° | 0.0° | 180.0° |

</div>

The Moon's gravity is strong enough to bend the departure by about 54 to 70 degrees,
so the site lies well away from the obvious point.
On Phobos and Deimos the release speed is fifty to a few hundred times the escape speed,
the hyperbola is almost a straight line,
and the sites are simply the point beneath Mars and the point opposite it.
At the point beneath Mars an eastward release goes forward along the orbit,
and at the opposite point it goes backward.
These figures ignore the parent's gravity during the departure.
That is a fair approximation for the Moon,
whose Hill radius is 61,533 kilometres,
but not near Phobos,
whose surface lies close to its Hill radius.
Because the release speeds from Phobos are so much larger than its escape speed,
the payload's path is governed almost entirely by Mars from the moment of release.

### Launching into Solar Orbit

The same equations apply with the Sun as the parent.
A mass driver on a moon can also throw a payload clear of the moon's planet and into solar orbit,
which needs the excess relative to the planet to exceed the planet's escape speed at the moon's distance.
Leaving Mars for a Hohmann transfer to Earth needs an excess of about 2.65 kilometres per second relative to Mars,
which requires a release speed of 1.88 kilometres per second from Phobos
and 1.92 from Deimos,
aligned with the moon's own orbital motion at the point in its orbit where that motion points the required way.
The release speed relative to a moon of orbital speed $V_{B} = \sqrt{\mu_{P}/a_{B}}$ needed for a planet-relative excess $v_{\infty,P}$ is the departure equation of the companion article on manoeuvres
[Orbital Manoeuvres in Terms of Delta-v, Departure][related_post_orbital_manoeuvres_departure],
applied at the moon's orbit with the moon's own speed credited.
Its special case $v_{\infty,P} = 0$ is the release needed merely to escape the planet,
885 metres per second from Phobos and 560 from Deimos.

$$
v_{\mathrm{rel}} = \sqrt{v_{\infty,P}^{2} + \frac{2\mu_{P}}{a_{B}}} - \sqrt{\frac{\mu_{P}}{a_{B}}}, \qquad
v_{\mathrm{rel}}\left(v_{\infty,P} = 0\right) = \left(\sqrt{2} - 1\right)\sqrt{\frac{\mu_{P}}{a_{B}}}
$$

Phobos is deeper in Mars's gravity well,
so it benefits more from the Oberth effect,
and the two requirements are nearly equal despite Phobos's higher orbital speed.

From an asteroid the launching body's gravity is almost negligible.
A Hohmann transfer from Ceres's orbit to Earth's needs a departure excess of 4.86 kilometres per second and a release speed of 4.89,
and from Vesta 4.43 and 4.44.
Ceres and Vesta rotate in 9.07 and 5.34 hours,
so a fixed track points in the required direction only at one moment in each rotation.

### Positioning for Parent Orbits

On a synchronous moon a track laid along the equator,
through the sub-parent point and the point opposite it,
covers prograde and retrograde launches.
Launches with an out-of-plane excess need the track at an azimuth away from east and west,
by the same spherical trigonometry as before.
Because the body's orientation relative to its orbit never changes,
a fixed site produces the same departure relative to the moon's orbit at every launch.
The orientation of the payload's orbit relative to the stars then rotates with the moon's position in its orbit,
so release time selects the orientation and the site selects the shape.

On a body that is not synchronous,
such as Ceres or Vesta,
the track sweeps around the sky once per rotation,
and each departure direction is available once per rotation.
An equatorial track serves departures in the body's orbital plane,
and the rotation adds the surface speed when the track points with the spin.

## Payload Transfer Between Bodies

### The Timing Problem

A payload thrown from one body must arrive where another body will be.
For a Hohmann transfer the departure must occur when the target leads the launching body by a particular phase angle,
which recurs once per synodic period
[Orbital Manoeuvres in Terms of Delta-v][related_post_orbital_manoeuvres].
For a general transfer between two positions in a given time,
the departure and arrival velocities come from Lambert's problem
[Lambert's Problem][ref_lamberts_problem].
The mass driver then has to supply the departure excess $\vec{v}_{\infty}$ found from Lambert's solution,
which fixes the release speed and,
through the hyperbola geometry above,
the release site.

### Examples

**Phobos to Deimos.**
A Hohmann transfer needs a prograde release of 417.6 metres per second from Phobos,
takes 8.87 hours,
and arrives 330.1 metres per second slower than Deimos.
Deimos must lead Phobos by 74.6 degrees at release,
and that alignment recurs every 10.24 hours,
the synodic period of the two moons.
Both numbers come from the patched-conic relations of the companion article on manoeuvres
[Orbital Manoeuvres in Terms of Delta-v, Patched Conics][related_post_orbital_manoeuvres_patched],
with the moons' orbital radii $r_{1}$ and $r_{2}$ and periods $T_{1}$ and $T_{2}$.

$$
\theta_{H} = \pi\left[1 - \left(\frac{r_{1}+r_{2}}{2r_{2}}\right)^{3/2}\right], \qquad
T_{\mathrm{syn}} = \left|\frac{1}{T_{1}} - \frac{1}{T_{2}}\right|^{-1}
$$

The release site is the point on Phobos beneath Mars,
on an eastward lane.

**The Moon to low Earth orbit.**
A release of 2.52 kilometres per second from the site found above sends the payload to a perigee 300 kilometres above Earth in 4.98 days.
It arrives at 10.83 kilometres per second.
Circularizing there costs 3.11 kilometres per second,
so the practical route is to shed the speed in Earth's atmosphere by aerocapture or aerobraking,
which an earlier article on this site describes
[Introduction to Space Studies][related_post_space_studies].

**Ceres or Vesta to Earth's orbit.**
A Hohmann transfer from Ceres takes 472 days and arrives with an excess of 6.31 kilometres per second relative to Earth,
with windows every 467 days.
From Vesta it takes 398 days,
arrives with an excess of 5.52,
and has windows every 504 days.

### Corrective Manoeuvres for the Payload

A mass driver fixes the departure once,
and every error grows with the distance travelled.

<div style="overflow-x: auto;" markdown="1">

| Transfer | Effect of a 1 m/s release speed error |
|---|---|
| Moon to Earth perigee 300 km | Perigee moved by 72 km |
| Phobos to Deimos | Apoapsis moved by 64 km |
| Ceres to Earth's orbit | Perihelion moved by about 31,000 km |

</div>

Timing errors matter too.
Ceres moves along its orbit at 17.9 kilometres per second,
so each second of release timing error shifts the departure point by 17.9 kilometres.

The corrections follow a simple rule.
A miss $\delta r$ corrected at a time $t_{\mathrm{go}}$ before arrival costs roughly the following,
a straight-line approximation that is accurate when the correction is small and the time short compared with the orbit.

$$
\Delta v_{\mathrm{mid}} \approx \frac{\delta r}{t_{\mathrm{go}}}
$$

Correcting a miss of 40,000 kilometres costs about 4.6 metres per second with 100 days to go and about 463 with one day to go.
The payload should therefore measure its trajectory and correct it early.
On arrival it must also deal with its excess speed,
330 metres per second at Deimos,
over 6 kilometres per second at Earth from the asteroid belt,
by an engine burn,
by aerocapture where there is an atmosphere,
or by some catching device at the destination,
an option this article does not analyse.
Wikipedia describes a related idea in which a mass driver on a spacecraft reflects masses thrown from a stationary one
[Mass Driver][ref_mass_driver].
A mass driver therefore replaces the departure burn,
which is usually the largest,
but not the guidance or the arrival.

## Tracks Around the Whole Body

### The Idea

A track that runs all the way around a body along a great circle has no end.
A payload can circle it as many times as needed to reach its release speed,
so the track length no longer limits the speed,
and the acceleration can be kept low.
Wikipedia notes that such a track around the Moon,
or any body without a significant atmosphere,
would free a reusable bucket from the limit of track length,
but would have to withstand substantial centrifugal forces at high speeds
[Mass Driver][ref_mass_driver].
Those forces set the real limit.

### The Curvature Limit

A payload circling at speed $v$ needs the hold-down acceleration $a_{n} = v^{2}/R - g$ from the track,
and the tangential acceleration $a_{t}$ that raises its speed adds to it,
so the total acceleration it feels and the power the track delivers to a payload of mass $m$ are the following.

$$
a_{\mathrm{total}} = \sqrt{a_{n}^{2} + a_{t}^{2}}, \qquad
P = m\,a_{t}\,v
$$

Extending the track around more laps reduces $a_{t}$ but does nothing to $a_{n}$.
If the cargo can tolerate a total acceleration $a_{\max}$,
the release speed cannot exceed the following,
however many laps it travels.

$$
v_{\max} = \sqrt{R\left(a_{\max} + g\right)}
$$

The path length and the number of laps needed at a tangential acceleration $a_{t}$ are the following.

$$
s = \frac{v^{2}}{2a_{t}}, \qquad N = \frac{v^{2}}{4\pi R\,a_{t}}
$$

<div style="overflow-x: auto;" markdown="1">

| Body | Example release speed, km/s | Hold-down load at that speed, g₀ | Laps at 1 g₀ tangential | Largest release speed at 3 g₀, km/s | At 100 g₀, km/s |
|---|---|---|---|---|---|
| Moon | 2.52, to low Earth perigee | 0.207 | 0.03 | 7.34 | 41.3 |
| Mercury | 20.28, to escape from the Sun | 16.8 | 1.37 | 8.99 | 49.0 |
| Ceres | 4.89, to Earth's orbit | 5.16 | 0.41 | 3.74 | 21.5 |
| Vesta | 4.44, to Earth's orbit | 7.64 | 0.61 | 2.79 | 16.1 |
| Phobos | 1.88, to Earth's orbit | 32.5 | 2.59 | 0.57 | 3.30 |
| Deimos | 1.92, to Earth's orbit | 60.0 | 4.77 | 0.43 | 2.48 |

</div>

The Mercury release speed is the one needed to leave the solar system from Mercury's surface.
Large bodies make good ring tracks.
The Moon can release lunar cargo to Earth with less than a quarter of standard gravity of hold-down load,
and could reach 7.34 kilometres per second at 3 g₀.
Small bodies make poor ones.
On Phobos and Deimos,
where a straight track would need only a couple of kilometres at 100 g₀,
a ring needs several laps at 1 g₀ but then holds the cargo down at 32 to 60 g₀ at release.
The infinite track solves the length problem only where the body is large.
Phobos and Deimos are also irregular,
at 25.90 by 22.60 by 18.32 kilometres and 16.08 by 11.78 by 10.22 kilometres,
so a circular ring would have to stand above much of their surface.

### Lanes and Directions

A payload released from a ring leaves along the tangent to the ring at the release point,
in the direction it was circulating.
Any point on the ring can be the release point,
so a single lane can send payloads in every direction in the ring's plane by choosing where to let go.
Releasing at the opposite edge of the body sends the payload in the opposite direction in space,
without a second lane.

The single lane has one restriction.
Every payload it releases circulates the body in the same sense as the lane.
For orbits bound to the body,
a prograde lane gives only prograde orbits,
and retrograde orbits need a second lane running the other way.
For unbound launches the restriction disappears where the release speed far exceeds the escape speed,
as on Phobos,
Deimos
and the asteroids,
because the outgoing direction is then simply the release direction.
On the Moon both lanes can reach the same departure direction from different sites,
126.5 and 53.5 degrees from the sub-Earth point for the low Earth perigee transfer,
so the second lane adds flexibility rather than new directions.

Two lanes running in opposite directions also balance the reaction on the body.
Launching a million tonnes tangentially at 1.9 kilometres per second changes the spin of Phobos by 0.018 percent and that of Deimos by 0.91 percent,
if every launch goes the same way.
Alternating lanes cancels the spin change,
although the momentum carried away still changes the moon's orbit,
by up to 0.18 millimetres per second for Phobos and 1.3 for Deimos per million tonnes.

The ring's plane matters as well.
An equatorial ring keeps its plane fixed in space as the body turns.
A ring through the poles sweeps through every orientation once per rotation,
so it can serve every orbital plane at some time,
much as a fixed straight track does.

## What the Cargo Experiences at Release

Release is the moment when the forces on the cargo change most abruptly.

**On a straight track** the tangential acceleration ends.
A payload that has felt 100 or 1,000 times standard gravity along the track goes to free fall at once.

**On a ring track** two things end.
The tangential acceleration can be removed in advance by coasting the last lap.
The hold-down load cannot,
because it is what keeps the payload on the ring.
Before release the track pushes the payload toward the body's centre with $a_{n}$,
and the payload feels pressed outward against its restraint.
At release that load drops to zero.
The step is 2.03 metres per second squared for the Moon example,
165 for Mercury
and 319 for Phobos.
If the release takes 10 milliseconds,
the jerk is about 200,
16,500
and 32,000 metres per second cubed.
For a release that removes the load over a time $\tau$ the jerk is the following.

$$
j \approx \frac{a_{n}}{\tau}
$$

**The cargo's structure springs back.**
A structure carrying a steady load is deflected by an amount set by its stiffness.
If the load vanishes instantly,
the structure does not settle at its unloaded shape but oscillates about it,
with an amplitude equal to the deflection it had under load.
This is the step response of an undamped spring and mass.
For a structure of stiffness $k$ and mass $m_{c}$ carrying a load $m_{c}a_{n}$,
the static deflection and the motion after a sudden release,
measured from the unloaded shape,
are the following,
with $\omega_{n} = \sqrt{k/m_{c}}$ the natural frequency.

$$
\delta = \frac{m_{c}\,a_{n}}{k}, \qquad
x(t) = \delta\cos\omega_{n}t
$$

Cargo and carrier should therefore be designed for the release transient as well as the launch load,
and a release that removes the load over several periods of the structure's lowest vibration avoids most of the oscillation.

**The cargo rises away from the track.**
After a horizontal release faster than the local circular speed,
the payload's path curves less sharply than the surface,
and its height above the track grows at first as follows.

$$
h_{\mathrm{sep}}(t) \approx \frac{1}{2}\,a_{n}\,t^{2}
$$

It is 1.0 metre after one second on the Moon,
82 metres on Mercury
and 159 metres on Phobos.
On the Moon the payload remains within a few metres of the track for the first seconds,
so the track and any parallel lane must leave clear space above the release point.
Below circular speed a horizontally released payload would fall back onto the track,
so a ring cannot release into a low ballistic hop without a ramp.

**A bucket must separate.**
In designs where a recycled bucket carries the payload,
payload and bucket separate at the end of the acceleration section,
and the bucket is then slowed
[Mass Driver][ref_mass_driver].
Any difference in their speeds or directions at separation becomes a release error of the kind analysed above.

## Epistemic State

**Facts reported by the cited sources.**
The description of mass drivers,
their history,
the efficiencies,
the two-section track,
the example of a 1 kilometre superconducting driver,
the remark about rocket burns after release,
the remark about circumferential tracks,
the physical data for the bodies,
the Hill sphere formula,
the lunar mascons
and the lunar frozen orbits come from the Wikipedia entries cited.
The findings attributed to Kolm,
McNab,
Powell and Maise,
and the 1977 reaction engine study are taken from their abstracts as recorded by OpenAlex.
Neither Crossref nor OpenAlex records an author for the 1977 reaction engine study,
so it is cited as unattributed.
None of the sources was read in full.

**Analysis in this article.**
Every equation is either standard orbital mechanics or derived here,
and every number is computed from those equations for uniform spheres of the cited mean radius,
point-mass gravity,
Keplerian orbits
and patched conics.
These assumptions misstate irregular bodies such as Phobos and Deimos,
ignore the parent's gravity during departures,
and ignore the gravity anomalies that perturb low orbits.
The accelerations,
payload masses,
throughput,
efficiency,
exhaust speed
and release duration are illustrative assumptions.
The midcourse correction rule is a straight-line approximation.

**Inference and judgment.**
The siting rules,
the claim that a ring track's benefit depends on the body's size,
the analysis of lanes,
and the statement that a release removing the load slowly avoids most structural oscillation are inferences from the equations.

**Unaddressed concerns.**
This article does not treat the electrical design of the track,
energy storage,
heat rejection,
the structural design of a ring,
debris from failed launches,
or the safety of payloads that might strike inhabited places.

## Out of Scope

This article does not cover mass drivers on Earth beyond their history,
mass drivers carried on spacecraft as engines,
or the economics of any launcher.
The specific case of a mass driver on Mercury is left to its own article.

## Conclusion

A mass driver is a linear electric motor that throws its payload,
and its basic equations are those of constant acceleration,
kinetic energy
and electromechanical force.
What makes it an orbital mechanics problem is that it acts only once,
at one point.
A payload released into orbit around its own body returns to the release point,
so it always needs at least one corrective burn,
which on the Moon costs only a few metres per second if the release is accurate in angle and plane.
Release speed sets the energy,
release angle the depth of the periapsis,
and release latitude,
azimuth
and time the orbital plane,
so the position and orientation of the track are design decisions about which orbits it can serve.

Thrown clear of its body,
a payload enters orbit around the parent,
and on a synchronous moon the release site fixes the direction of departure relative to the moon's orbit.
Sending payloads between bodies adds timing set by synodic periods,
release sites set by the hyperbolic turn,
and corrections that should be made early.
A track around a whole body removes the limit of length but not the limit of curvature,
which makes ring tracks attractive on large bodies such as the Moon and impractical for fast launches on small ones such as Phobos and Deimos.
At release the cargo goes abruptly from a sustained load to free fall,
and its design must allow for that step as much as for the launch itself.

## References

- [Reference, Ceres, Wikipedia][ref_ceres]
- [Reference, Coilgun, Wikipedia][ref_coilgun]
- [Reference, Deimos, Wikipedia][ref_deimos]
- [Reference, Frozen Orbit, Wikipedia][ref_frozen_orbit]
- [Reference, Hill Sphere, Wikipedia][ref_hill_sphere]
- [Reference, Lambert's Problem, Wikipedia][ref_lamberts_problem]
- [Reference, Mass Concentration, Wikipedia][ref_mass_concentration]
- [Reference, Mass Driver, Wikipedia][ref_mass_driver]
- [Reference, Mercury, Wikipedia][ref_mercury]
- [Reference, Moon, Wikipedia][ref_moon]
- [Reference, Phobos, Wikipedia][ref_phobos]
- [Reference, Railgun, Wikipedia][ref_railgun]
- [Reference, Tidal Locking, Wikipedia][ref_tidal_locking]
- [Reference, Vesta, Wikipedia][ref_vesta]
- [Related Post, Introduction to Space Studies][related_post_space_studies]
- [Related Post, Orbital Manoeuvres in Terms of Delta-v][related_post_orbital_manoeuvres]
- [Related Post, Orbital Manoeuvres in Terms of Delta-v, Departure][related_post_orbital_manoeuvres_departure]
- [Related Post, Orbital Manoeuvres in Terms of Delta-v, Patched Conics][related_post_orbital_manoeuvres_patched]
- [Related Post, Orbital Manoeuvres in Terms of Delta-v, Plane Change][related_post_orbital_manoeuvres_plane]
- [Related Post, Orbital Manoeuvres in Terms of Delta-v, The Hohmann Transfer][related_post_orbital_manoeuvres_hohmann]
- [Related Post, Orbital Manoeuvres in Terms of Delta-v, The Rocket Equation][related_post_orbital_manoeuvres_rocket]
- [Research, Kolm 1977, Basic Coaxial Mass Driver Reference Design][research_kolm_1977]
- [Research, McNab 2003, Launch to Space with an Electromagnetic Railgun][research_mcnab_2003]
- [Research, Powell and Maise 2008, StarTram, The Magnetic Launch Path to Very Low Cost, Very High Volume Launch to Space][research_powell_maise_2008]
- [Research, Unattributed 1977, Mass-Driver Reaction Engine as Shuttle Upper-Stage][research_mass_driver_reaction_engine_1977]

[ref_ceres]: https://en.wikipedia.org/wiki/Ceres_(dwarf_planet)
[ref_coilgun]: https://en.wikipedia.org/wiki/Coilgun
[ref_deimos]: https://en.wikipedia.org/wiki/Deimos_(moon)
[ref_frozen_orbit]: https://en.wikipedia.org/wiki/Frozen_orbit
[ref_hill_sphere]: https://en.wikipedia.org/wiki/Hill_sphere
[ref_lamberts_problem]: https://en.wikipedia.org/wiki/Lambert%27s_problem
[ref_mass_concentration]: https://en.wikipedia.org/wiki/Mass_concentration_(astronomy)
[ref_mass_driver]: https://en.wikipedia.org/wiki/Mass_driver
[ref_mercury]: https://en.wikipedia.org/wiki/Mercury_(planet)
[ref_moon]: https://en.wikipedia.org/wiki/Moon
[ref_phobos]: https://en.wikipedia.org/wiki/Phobos_(moon)
[ref_railgun]: https://en.wikipedia.org/wiki/Railgun
[ref_tidal_locking]: https://en.wikipedia.org/wiki/Tidal_locking
[ref_vesta]: https://en.wikipedia.org/wiki/4_Vesta
[related_post_orbital_manoeuvres]: {% post_url 2026-08-17-orbital_manoeuvres %}
[related_post_orbital_manoeuvres_departure]: {% post_url 2026-08-17-orbital_manoeuvres %}#departure
[related_post_orbital_manoeuvres_hohmann]: {% post_url 2026-08-17-orbital_manoeuvres %}#the-hohmann-transfer
[related_post_orbital_manoeuvres_patched]: {% post_url 2026-08-17-orbital_manoeuvres %}#patched-conics
[related_post_orbital_manoeuvres_plane]: {% post_url 2026-08-17-orbital_manoeuvres %}#plane-change
[related_post_orbital_manoeuvres_rocket]: {% post_url 2026-08-17-orbital_manoeuvres %}#the-rocket-equation
[related_post_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[research_kolm_1977]: https://doi.org/10.2514/6.1977-534
[research_mass_driver_reaction_engine_1977]: https://doi.org/10.2514/6.1977-536
[research_mcnab_2003]: https://doi.org/10.1109/tmag.2002.805923
[research_powell_maise_2008]: https://doi.org/10.1109/elt.2008.76
