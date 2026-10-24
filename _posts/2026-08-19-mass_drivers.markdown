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
This article treats mass drivers with the orbital mechanics usually applied to rockets and orbital manoeuvres.
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
A related design uses linear induction motors of the kind used for the electromagnetic aircraft launch system on the aircraft carrier Gerald R. Ford
[Mass Driver][ref_mass_driver].
The United States Navy built a prototype electromagnetic catapult in the 1940s,
and advances in pulsed power,
power conditioning,
energy storage
and controls later made a fieldable aircraft launch system credible
[Doyle et al. 1995][research_doyle_et_al_1995].
A coilgun is the same idea at small scale,
and a railgun drives its projectile by a current through two rails rather than through coils
[Coilgun][ref_coilgun]
[Railgun][ref_railgun].

Because the payload is guided by magnetic levitation,
a mass driver needs no physical contact between moving parts,
and its working life could in principle reach millions of launches
[Mass Driver][ref_mass_driver].
Kolm's reference design anticipated a magnetically levitated superconducting bucket
[Kolm 1977][research_kolm_1977].
Most serious designs use superconducting coils
and often reach efficiencies of 50 to over 90 percent,
depending on the design
[Mass Driver][ref_mass_driver].
Kolm,
Mongeau
and Williams reported energy conversion efficiencies better than 90 percent for a mass driver with a superconducting bucket
[Kolm et al. 1980][research_kolm_et_al_1980],
and a 1977 reaction engine study assumed 75 percent
[Mass-Driver Reaction Engine 1977][research_mass_driver_reaction_engine_1977].
A mass driver track has two sections.
In the first the coils are evenly spaced and the acceleration rises with speed up to the maximum the bucket can bear,
and in the second the coils are spaced ever further apart to hold that acceleration constant
[Mass Driver][ref_mass_driver].

The idea is old.
Edwin Northrup described an electric gun in 1937,
and Gerard O'Neill built a first mass driver in 1976 and 1977,
a short test model that fired a projectile at 40 metres per second with an acceleration of 33 times standard gravity
[Mass Driver][ref_mass_driver].
Kolm's reference design for a basic coaxial mass driver explained the principles and optimization procedures
and expected even a table-top system to reach accelerations near 1,000 metres per second squared
[Kolm 1977][research_kolm_1977].
A major proposed application was the transport of lunar surface material to space habitats
[Mass Driver][ref_mass_driver],
which O'Neill had argued could be built far more comfortable,
productive
and attractive than most of Earth
[O'Neill 1974][research_oneill_1974].
Kolm,
Mongeau
and Williams surveyed electromagnetic launchers in 1980.
They described the railgun,
in which a sliding short circuit or an arc is driven along two rails by direct current,
as the simplest launcher of interest,
and the mass driver,
in which a superconducting bucket is accelerated by pulse coils energized by capacitors,
as the most sophisticated studied thus far,
with energy conversion efficiencies better than 90 percent
[Kolm et al. 1980][research_kolm_et_al_1980].

On Earth the relatively strong gravity and thick atmosphere make the problem difficult
[Mass Driver][ref_mass_driver].
McNab estimated that a railgun launching directly to orbit would need muzzle speeds of at least 7.5 kilometres per second,
and that even launchers over 1,000 metres long would need accelerations over 1,000 times standard gravity,
so only rugged payloads such as fuel,
water
and material could be launched
[McNab 2003][research_mcnab_2003].
The StarTram concept accelerates cargo craft in an evacuated tunnel,
and a small rocket burn after release establishes orbit
[Powell and Maise 2008][research_powell_maise_2008].
In the authors' projections a single facility of that kind could launch over 100,000 tons a year
at under 50 dollars per kilogram of payload
[Powell et al. 2008][research_powell_et_al_2008].
Wikipedia's summary adds a bound,
that in a design that minimizes it,
well under a tenth of orbital speed from a small rocket is enough to raise perigee after release
[Mass Driver][ref_mass_driver].
That post-release burn is the central subject of this article.

A mass driver can also be carried by a spacecraft as an engine,
throwing pieces of material backward
[Mass Driver][ref_mass_driver].
One such design study for a Space Shuttle upper stage would throw 14 gram segments at 8 to 10 kilometres per second,
and at 8 kilometres per second it would give a thrust of 560 newtons from 2.9 megawatts at 75 percent efficiency
[Mass-Driver Reaction Engine 1977][research_mass_driver_reaction_engine_1977].
Snow and Dunbar proposed such an engine for moving payloads of hundreds to thousands of tons between low Earth orbit and geosynchronous orbit,
with reaction mass of virtually any liquid or solid material,
and discussed its debris hazard and its effects on the ionosphere
[Snow and Dunbar 1982][research_snow_dunbar_1982].
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

The difference between peak and average power makes energy storage central to the design.
The limits are generally the cost of storing energy that can be discharged quickly and the cost of switching it
[Mass Driver][ref_mass_driver],
and it was advances in energy storage,
switching
and magnets that made electromagnetic launch a viable alternative to chemical propulsion for some tasks
[Kolm et al. 1980][research_kolm_et_al_1980].
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
Rashleigh and Marshall reached 5.9 kilometres per second with an arc armature in an inductively driven railgun,
and found that simple theory predicted its performance
[Rashleigh and Marshall 1978][research_rashleigh_marshall_1978].
In the coilguns developed at Sandia National Laboratories the coils are energized in sequence to create a travelling magnetic wave,
the projectile's position is tracked to trigger each coil,
and the effect of switch jitter on performance was assessed for high-speed applications
[Kaye 2005][research_kaye_2005].

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
| Mercury | 2,439.4 | 3.70 | 3,005 | 4,250 | 3.0 | 220,675 |
| Ceres | 469.7 | 0.284 | 365 | 516 | 90.3 | 223,378 |
| Vesta | 262.7 | 0.251 | 257 | 363 | 85.8 | 124,092 |
| Phobos | 11.08 | 0.0058 | 8.0 | 11.3 | 2.5 | 16.6 |
| Deimos | 6.27 | 0.0024 | 3.9 | 5.5 | 0.4 | 21.3 |

</div>

The masses,
radii,
rotation periods
and orbits are those collected by Wikipedia
[Moon][ref_moon]
[Mercury][ref_mercury]
[Ceres][ref_ceres]
[Vesta][ref_vesta]
[Phobos][ref_phobos]
[Deimos][ref_deimos],
which draw on mission and survey results.
For the Moon these are a review of the lunar interior
[Wieczorek et al. 2006][research_wieczorek_et_al_2006]
and the gravity mapping mission GRAIL,
which gives a mean density of 3,345.56 kilograms per cubic metre
[Williams et al. 2014][research_williams_et_al_2014].
For Mercury the MESSENGER mission gives a mean radius of 2,439.36 kilometres
[Perry et al. 2015][research_perry_et_al_2015],
a gravitational parameter of 22,031.87 cubic kilometres per second squared
[Verma and Margot 2016][research_verma_margot_2016]
and a rotation period of 58.646 days
[Mazarico et al. 2014][research_mazarico_et_al_2014].
For Ceres and Vesta the Dawn mission gives the shapes and gravity fields
[Ermakov et al. 2017][research_ermakov_et_al_2017]
[Konopliv et al. 2018][research_konopliv_et_al_2018]
[Russell et al. 2012][research_russell_et_al_2012]
[Konopliv et al. 2014][research_konopliv_et_al_2014].
For Phobos and Deimos the mean radii of 11.08 and 6.27 kilometres come from spacecraft shape models
[Ernst et al. 2023][research_ernst_et_al_2023],
the gravitational parameter of Phobos from two Mars Express flybys
[Guo et al. 2026][research_guo_et_al_2026],
and the orbits and the mass of Deimos from fits to astrometry and tracking
[Jacobson and Lainey 2014][research_jacobson_lainey_2014].
The derived columns are computed for uniform spheres.
With the gravitational parameter of Phobos from Mars Express tracking
[Guo et al. 2026][research_guo_et_al_2026]
and its mean radius from spacecraft shape models
[Ernst et al. 2023][research_ernst_et_al_2023],
a uniform sphere gives an escape speed of 11.32 metres per second.
The Hill radius marks roughly the extent of the region in which the body's own gravity dominates that of its parent
[Hill Sphere][ref_hill_sphere],
for a body of mass $m$ orbiting a parent of mass $M$ at distance $a$.

$$
r_{H} \approx a\sqrt[3]{\frac{m}{3M}}
$$

Phobos's Hill radius of 16.6 kilometres is smaller than the 25.9 kilometre long axis of its best-fit ellipsoid
[Ernst et al. 2023][research_ernst_et_al_2023],
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
Janhunen states the same result for the Moon,
that a passive object launched below escape speed orbits once and crashes back at the launch site,
and finds that for specific launch sites and directions
lunar gravity anomalies can keep a passive projectile in orbit for up to 9 Earth days,
long enough for a catcher to intercept it
[Janhunen 2025][research_janhunen_2025].

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
large mass concentrations lie beneath the ringed maria,
first found from the tracking of Lunar Orbiter spacecraft
[Muller and Sjogren 1968][research_muller_sjogren_1968],
and they perturb low orbits
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
families of which have been found by numerical continuation
[Elipe and Lara 2003][research_elipe_lara_2003].
Wikipedia,
quoting NASA,
places them at inclinations of 27,
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
| Mercury | 3,005.3 | 3.0 | 3,002.3 | 3,008.3 | 1.002 |
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
an option this article does not analyse beyond the literature reviewed below.
Payloads in the classic lunar scheme carried no midcourse correction of their own,
and Heppenheimer,
Ross
and Hannah proposed trimming their velocity with electrostatic fields at the launcher,
with arcing from loose dust as the most serious problem
[Heppenheimer et al. 1982a][research_heppenheimer_et_al_1982a].
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
with best-fit ellipsoids of 25.90 by 22.60 by 18.32 kilometres and 16.08 by 11.78 by 10.22 kilometres
[Ernst et al. 2023][research_ernst_et_al_2023],
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
Mass Driver Two followed its accelerator with a decelerator of identical design that brought the bucket to rest and returned its energy to the power supply
[Snow et al. 1982][research_snow_et_al_1982].
Any difference in their speeds or directions at separation becomes a release error of the kind analysed above.

## A Review of the Literature

The modern literature on mass drivers began with the space settlement studies of the 1970s,
moved into military and naval electromagnetic launch in the 1980s and 1990s,
and has returned to lunar resources in the 2010s and 2020s.
This section surveys it by topic.
Each work is described according to its published abstract,
or by its subject alone where it is cited for its title.

### Origins and the Space Settlement Programme

O'Neill's 1974 article argued for space habitats
[O'Neill 1974][research_oneill_1974].
Heppenheimer attempted an early existence proof for transporting lunar material,
with payloads accelerated to lunar escape by a magnetically levitated mass driver driven by a linear synchronous motor
and received by a catcher in a mode Heppenheimer likened to a Venus flytrap.
Heppenheimer found that each millimetre per second of velocity error at the lunar surface produced a miss of 1 kilometre at the fifth Lagrange point
[Heppenheimer 1975][research_heppenheimer_1975].
Chilton presented mass driver theory and history
[Chilton 1977][research_chilton_1977]
alongside Kolm's reference design
[Kolm 1977][research_kolm_1977].
The cryogenic module of Mass Driver Two comprised a helium-cooled bucket with two niobium-titanium coils of 44 kilo-ampere-turns,
energized inductively and injected by normal-conductor pulse coils
[Fine et al. 1979][research_fine_et_al_1979].
O'Neill and Kolm wrote on high-acceleration mass drivers in 1980
[O'Neill and Kolm 1980][research_oneill_kolm_1980],
and O'Neill reported on their development in 1981
[O'Neill 1981][research_oneill_1981].

### Launcher Physics and Technology

Kolm,
Mongeau
and Williams surveyed the launcher types and their applications,
including lunar and asteroid mining
[Kolm et al. 1980][research_kolm_et_al_1980].
Rashleigh and Marshall's railgun experiment established that simple theory predicts railgun performance up to 5.9 kilometres per second
[Rashleigh and Marshall 1978][research_rashleigh_marshall_1978].
Fair described electromagnetic propulsion as a new initiative in 1982
[Fair 1982][research_fair_1982],
reviewed the field's move into engineering programmes such as naval aircraft launch and shipboard guns in 2005
[Fair 2005][research_fair_2005],
and noted in 2008 renewed interest in launching material to orbit and beyond,
with the interface between rail and armature as a particular focus of research
[Fair 2008][research_fair_2008].
Kaye described Sandia coilguns launching projectiles of 10 grams to 5 kilograms at up to 1 kilometre per second
[Kaye 2005][research_kaye_2005],
and Doyle and coauthors described the naval electromagnetic aircraft launch system
[Doyle et al. 1995][research_doyle_et_al_1995].

### Launch from Earth

Hawke,
Brooks,
Fowler
and Peterson gave an example design of an Earth-based railgun able to launch projectiles through the atmosphere at more than 8 kilometres per second
[Hawke et al. 1981][research_hawke_et_al_1981].
Hunter and Hyde proposed a light gas gun for launching building material into low Earth orbit
[Hunter and Hyde 1989][research_hunter_hyde_1989],
and Mankins presented electromagnetic launch as one strategy for reducing launch costs
[Mankins 1994][research_mankins_1994].
Turman and Lipinski evaluated coilguns 1 to 2 kilometres long launching hardened payloads of 100 to 1,000 kilograms to low Earth orbit,
and put the energy and power requirements at 40 to 260 gigajoules and 20 to 400 gigawatts of electric power
[Turman and Lipinski 1996][research_turman_lipinski_1996].
McNab's 2003 study is described above
[McNab 2003][research_mcnab_2003].
Schmidt studied railgun launch to low Earth orbit for hardened material with a total flight mass of 1,000 kilograms,
using lifting bodies to reduce the burden of drag
[Schmidt 2006][research_schmidt_2006].
Powell and coauthors described StarTram as an international facility for magnetic launch
[Powell et al. 2006][research_powell_et_al_2006]
and projected that its first generation could accelerate cargo craft of about 35 to 40 tons to 8 kilometres per second,
leaving the tunnel at a high site about 4,000 metres or more above sea level
[Powell et al. 2008][research_powell_et_al_2008]
[Powell and Maise 2008][research_powell_maise_2008].
McNab reported 5.2 kilometres per second in a 7 metre augmented railgun with a plasma armature,
11 kilometres per second with a plasma arc in a five-stage system,
and an acceptable nosetip ablation of about 15 millimetres for a 10 kilogram projectile flying to orbit from a high-altitude launch
[McNab 2009][research_mcnab_2009].
Bolonkin and Krinker proposed a railgun launcher powered by a flywheel and a homopolar generator
[Bolonkin and Krinker 2010][research_bolonkin_krinker_2010].

### Lunar Launchers

Snow,
Kubby
and Dunbar proposed a simplified version of O'Neill's approach,
launching 125 kilogram containers with their own kick motors into a transfer orbit,
with an initial capability of about 500 tonnes of liquid oxygen a year delivered to low Earth orbit
[Snow et al. 1981][research_snow_et_al_1981].
Bilby,
Nozette
and Kolm formulated a superconducting quenchgun that stores its energy in the launcher itself
[Bilby et al. 1989][research_bilby_et_al_1989].
Lipinski and coauthors designed a 200 metre lunar coilgun launching at 2.33 kilometres per second every 30 minutes,
delivering 867 tonnes of lunar oxygen a year
[Lipinski et al. 1993][research_lipinski_et_al_1993].
Seybold and Fowler studied a lunar mass driver for sending cargo to Mars
[Seybold and Fowler 1994][research_seybold_fowler_1994].
Wright,
Kuznetsov
and Kloesel reassessed lunar electromagnetic launch within the exploration architecture of the National Aeronautics and Space Administration,
and concluded from a preliminary assessment of cost against benefit that it is not as favourable as originally suggested
[Wright et al. 2011][research_wright_et_al_2011].
Roesler estimated the mass of a lunar resource launcher from two mature terrestrial electromagnetic launchers
[Roesler 2013][research_roesler_2013].
Beemer and McNab studied the launch parameters of lunar ice payloads
[Beemer and McNab 2023][research_beemer_mcnab_2023],
Carrio and coauthors proposed an architecture for lunar electromagnetic launch
[Carrio et al. 2025][research_carrio_et_al_2025],
and Rocher,
Sarton du Jonchay
and Mavris built sizing models for lunar mass drivers as an alternative to traditional rockets such as the Human Landing System for cislunar logistics
[Rocher et al. 2025][research_rocher_et_al_2025].

### Trajectories, Guidance and Catchers

Heppenheimer and Kaplan analysed launch from the lunar surface onto ballistic trajectories to a passive catcher near the second Lagrange point.
They showed that from any launch site a target point can be chosen that is reached with zero dispersion due to errors in one selected component of launch velocity,
and that a colony orbit can be reached from the second Lagrange point for as little as 9.02 metres per second
[Heppenheimer and Kaplan 1977][research_heppenheimer_kaplan_1977].
Heppenheimer wrote on achromatic trajectories for lunar material transport
[Heppenheimer 1978a][research_heppenheimer_1978a],
described a mass catcher for large-scale lunar material transport
[Heppenheimer 1978b][research_heppenheimer_1978b],
and compared modes of transport that use them
[Heppenheimer 1979][research_heppenheimer_1979].
Heppenheimer,
Ross
and Hannah proposed electrostatic trimming of payload velocity
[Heppenheimer et al. 1982a][research_heppenheimer_et_al_1982a]
and an integrated system for precise release and aim,
with electromagnetic fins to damp oscillations of the buckets,
in which the largest residual error was a transverse velocity of about 0.003 centimetres per second
[Heppenheimer et al. 1982b][research_heppenheimer_et_al_1982b].
Janhunen showed that lunar gravity anomalies can extend the life of a sub-escape orbit
and listed coilguns,
railguns,
quenchguns
and slings among the launchers that could supply the roughly 1.7 kilometres per second required
[Janhunen 2025][research_janhunen_2025].
This literature takes a different approach from the corrective burns of this article.
It shapes the trajectory so that errors do not matter at the target,
or corrects the payload at the launcher,
because the payloads in these schemes carry no means of midcourse correction.

### Small Bodies and Reaction Engines

O'Leary discussed international crewed missions to Mars and the resources of Phobos and Deimos
[O'Leary 1992][research_oleary_1992].
Corbin and Higgins studied a mass driver that uses an asteroid's own material as reaction mass to deflect it,
noting that mass drivers had been proposed for lunar and asteroid mining since the mid-1970s
[Corbin and Higgins 2006][research_corbin_higgins_2006].
The 1977 study
[Mass-Driver Reaction Engine 1977][research_mass_driver_reaction_engine_1977]
and Snow and Dunbar
[Snow and Dunbar 1982][research_snow_dunbar_1982]
treated the mass driver as an engine on board a spacecraft.

### Circular Launchers

Bolonkin proposed a circular launcher in a book chapter
[Bolonkin 2005][research_bolonkin_2005],
and Wikipedia describes ring designs in which a vehicle circles many times before release
[Mass Driver][ref_mass_driver].

### Beyond the Cited Literature

The sections of this article on mass drivers on Phobos and Deimos
and on tracks around the whole circumference of a body
rest on the equations derived here rather than on a cited study.

## Epistemic State

**Facts reported by the cited sources.**
The description of mass drivers,
their history,
the efficiencies,
the two-section track,
the example of a 1 kilometre superconducting driver,
the remark about rocket burns after release,
the remark about circumferential tracks,
the Hill sphere formula,
the effect of mascons on low orbits
and the inclinations of the lunar frozen orbits come from the Wikipedia entries cited.
The physical data for the bodies are those collected by Wikipedia,
traced where the text says so to the mission and survey papers that Wikipedia cites.
The findings attributed to Kolm,
McNab,
Powell and Maise,
the 1977 reaction engine study,
the shape models of Ernst and coauthors,
the gravity results of Guo and coauthors,
Verma and Margot,
Mazarico and coauthors
and Williams and coauthors,
the shape result of Perry and coauthors,
Ermakov and coauthors for the approximate radius of Ceres,
Muller and Sjogren,
Snow and coauthors 1982,
Elipe and Lara,
and the works of the literature review marked by their findings rather than their titles,
from O'Neill 1974 to Rocher and coauthors 2025,
are stated according to their published abstracts.
The works of Chilton,
O'Neill and Kolm,
O'Neill 1981,
Heppenheimer 1978a,
1978b
and 1979,
Seybold and Fowler,
Beemer and McNab,
Carrio and coauthors,
Hunter and Hyde,
Powell and coauthors 2006,
Fair 1982,
O'Leary,
Bolonkin 2005,
Wieczorek and coauthors,
Konopliv and coauthors 2014 and 2018,
Russell and coauthors
and Jacobson and Lainey are cited only for what their titles state.
The figures of Powell and coauthors for cost and throughput are their projections.
The 1977 reaction engine study carries no author in its bibliographic record,
so it is cited by its title.
The findings attributed to sources rest on their abstracts and titles rather than on their full texts.

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

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Beemer, Heidi D., and Ian R. McNab. 2023. "Launch Parameters of a Lunar Ice Payload Traveling via Electromagnetic Mass Accelerator." *Acta Astronautica* 207: 24–32. [https://doi.org/10.1016/j.actaastro.2023.02.041][research_beemer_mcnab_2023]
- Doyle, M. R., D. J. Samuel, T. Conway, and R. R. Klimowski. 1995. "Electromagnetic Aircraft Launch System-EMALS." *IEEE Transactions on Magnetics* 31 (1): 528–33. [https://doi.org/10.1109/20.364638][research_doyle_et_al_1995]
- Elipe, Antonio, and Martin Lara. 2003. "Frozen Orbits about the Moon." *Journal of Guidance, Control, and Dynamics* 26 (2): 238–43. [https://doi.org/10.2514/2.5064][research_elipe_lara_2003]
- Ermakov, A. I., R. R. Fu, J. C. Castillo-Rogez, et al. 2017. "Constraints on Ceres' Internal Structure and Evolution from Its Shape and Gravity Measured by the Dawn Spacecraft." *Journal of Geophysical Research: Planets* 122 (11): 2267–93. [https://doi.org/10.1002/2017je005302][research_ermakov_et_al_2017]
- Ernst, Carolyn M., R. Terik Daly, Robert W. Gaskell, et al. 2023. "High-Resolution Shape Models of Phobos and Deimos from Stereophotoclinometry." *Earth, Planets and Space* 75 (1): 103. [https://doi.org/10.1186/s40623-023-01814-7][research_ernst_et_al_2023]
- Fair, H. 1982. "Electromagnetic Propulsion: A New Initiative." *IEEE Transactions on Magnetics* 18 (1): 4–6. [https://doi.org/10.1109/tmag.1982.1061789][research_fair_1982]
- Fair, H. D. 2005. "Electromagnetic Launch Science and Technology in the United States Enters a New Era." *IEEE Transactions on Magnetics* 41 (1): 158–64. [https://doi.org/10.1109/tmag.2004.838744][research_fair_2005]
- Guo, Xi, Jianguo Yan, Guolin Hu, et al. 2026. "Phobos’ Degree-1 Ellipsoidal Harmonic Gravity Field Recovery from Two Mars Express Flybys." *Monthly Notices of the Royal Astronomical Society* 548 (2): stag578. [https://doi.org/10.1093/mnras/stag578][research_guo_et_al_2026]
- Heppenheimer, T. A. 1978a. "Achromatic Trajectories and Lunar Material Transport for Space Colonization." *Journal of Spacecraft and Rockets* 15 (3): 176–83. [https://doi.org/10.2514/3.28004][research_heppenheimer_1978a]
- Heppenheimer, T. A. 1978b. "A Mass-Catcher for Large-Scale Lunar Material Transport." *Journal of Spacecraft and Rockets* 15 (4): 242–49. [https://doi.org/10.2514/3.28009][research_heppenheimer_1978b]
- Heppenheimer, T. A. 1979. "Lunar Material Transport: Comparison of Modes Employing Achromatic Trajectories." *Journal of Spacecraft and Rockets* 16 (1): 60–62. [https://doi.org/10.2514/3.57617][research_heppenheimer_1979]
- Heppenheimer, T. A., and David Kaplan. 1977. "Guidance and Trajectory Considerations in Lunar Mass Transportation." *AIAA Journal* 15 (4): 518–25. [https://doi.org/10.2514/3.7345][research_heppenheimer_kaplan_1977]
- Heppenheimer, T. A., David J. Ross, and Eric C. Hannah. 1982a. "Electrostatic Velocity Adjustment of Payloads Launched by Lunar Mass-Driver." *Journal of Guidance, Control, and Dynamics* 5 (2): 200–209. [https://doi.org/10.2514/3.19765][research_heppenheimer_et_al_1982a]
- Heppenheimer, T. A., David J. Ross, and Eric C. Hannah. 1982b. "Precision Release and Aim of Payloads Launched by Lunar Mass-Driver." *Journal of Guidance, Control, and Dynamics* 5 (3): 291–99. [https://doi.org/10.2514/3.19769][research_heppenheimer_et_al_1982b]
- Jacobson, R. A., and V. Lainey. 2014. "Martian Satellite Orbits and Ephemerides." *Planetary and Space Science* 102: 35–44. [https://doi.org/10.1016/j.pss.2013.06.003][research_jacobson_lainey_2014]
- Janhunen, Pekka. 2025. "Launching Mass from the Moon Helped by Lunar Gravity Anomalies." *Journal of the British Interplanetary Society* 78 (8): 290–94. [https://doi.org/10.59332/jbis-078-08-0290][research_janhunen_2025]
- Kaye, R. J. 2005. "Operational Requirements and Issues for Coilgun Electromagnetic Launchers." *IEEE Transactions on Magnetics* 41 (1): 194–99. [https://doi.org/10.1109/tmag.2004.838982][research_kaye_2005]
- Kolm, H., P. Mongeau, and F. Williams. 1980. "Electromagnetic Launchers." *IEEE Transactions on Magnetics* 16 (5): 719–21. [https://doi.org/10.1109/tmag.1980.1060806][research_kolm_et_al_1980]
- Konopliv, A. S., S. W. Asmar, R. S. Park, et al. 2014. "The Vesta Gravity Field, Spin Pole and Rotation Period, Landmark Positions, and Ephemeris from the Dawn Tracking and Optical Data." *Icarus* 240: 103–17. [https://doi.org/10.1016/j.icarus.2013.09.005][research_konopliv_et_al_2014]
- Konopliv, A. S., R. S. Park, A. T. Vaughan, et al. 2018. "The Ceres Gravity Field, Spin Pole, Rotation Period and Orbit from the Dawn Radiometric Tracking and Optical Data." *Icarus* 299: 411–29. [https://doi.org/10.1016/j.icarus.2017.08.005][research_konopliv_et_al_2018]
- Lipinski, R. J., S. Beard, J. Boyes, et al. 1993. "Space Applications for Contactless Coilguns." *IEEE Transactions on Magnetics* 29 (1): 691–95. [https://doi.org/10.1109/20.195659][research_lipinski_et_al_1993]
- Mazarico, Erwan, Antonio Genova, Sander Goossens, et al. 2014. "The Gravity Field, Orientation, and Ephemeris of Mercury from MESSENGER Observations after Three Years in Orbit." *Journal of Geophysical Research: Planets* 119 (12): 2417–36. [https://doi.org/10.1002/2014je004675][research_mazarico_et_al_2014]
- McNab, I. R. 2003. "Launch to Space with an Electromagnetic Railgun." *IEEE Transactions on Magnetics* 39 (1): 295–304. [https://doi.org/10.1109/tmag.2002.805923][research_mcnab_2003]
- McNab, I. R. 2009. "Progress on Hypervelocity Railgun Research for Launch to Space." *IEEE Transactions on Magnetics* 45 (1): 381–88. [https://doi.org/10.1109/tmag.2008.2008601][research_mcnab_2009]
- O'Leary, Brian. 1992. "International Manned Missions to Mars and the Resources of Phobos and Deimos." *Acta Astronautica* 26 (1): 37–54. [https://doi.org/10.1016/0094-5765(92)90141-5][research_oleary_1992]
- O'Neill, G. K., and H. H. Kolm. 1980. "High-Acceleration Mass Drivers." *Acta Astronautica* 7 (11): 1229–38. [https://doi.org/10.1016/0094-5765(80)90002-8][research_oneill_kolm_1980]
- Perry, Mark E., Gregory A. Neumann, Roger J. Phillips, et al. 2015. "The Low-Degree Shape of Mercury." *Geophysical Research Letters* 42 (17): 6951–58. [https://doi.org/10.1002/2015gl065101][research_perry_et_al_2015]
- Rashleigh, S. C., and R. A. Marshall. 1978. "Electromagnetic Acceleration of Macroparticles to High Velocities." *Journal of Applied Physics* 49 (4): 2540–42. [https://doi.org/10.1063/1.325107][research_rashleigh_marshall_1978]
- Snow, W., and R. Dunbar. 1982. "Mass Driver Reaction Engine Characteristics and Performance in Earth Orbital Transfer Missions." *IEEE Transactions on Magnetics* 18 (1): 176–89. [https://doi.org/10.1109/tmag.1982.1061772][research_snow_dunbar_1982]
- Snow, W., R. Dunbar, J. Kubby, and G. O'Neill. 1982. "Mass Driver Two: A Status Report." *IEEE Transactions on Magnetics* 18 (1): 127–34. [https://doi.org/10.1109/tmag.1982.1061777][research_snow_et_al_1982]
- Verma, Ashok Kumar, and Jean-Luc Margot. 2016. "Mercury's Gravity, Tides, and Spin from MESSENGER Radio Science Data." *Journal of Geophysical Research: Planets* 121 (9): 1627–40. [https://doi.org/10.1002/2016je005037][research_verma_margot_2016]
- Williams, James G., Alexander S. Konopliv, Dale H. Boggs, et al. 2014. "Lunar Interior Properties from the GRAIL Mission." *Journal of Geophysical Research: Planets* 119 (7): 1546–78. [https://doi.org/10.1002/2013je004559][research_williams_et_al_2014]
- Wright, Michael R., Steven B. Kuznetsov, and Kurt J. Kloesel. 2011. "A Lunar Electromagnetic Launch System for in Situ Resource Utilization." *IEEE Transactions on Plasma Science* 39 (1): 521–28. [https://doi.org/10.1109/tps.2010.2089066][research_wright_et_al_2011]

### Primary Sources, Non-Peer-Reviewed

- Bilby, Curt, Stewart Nozette, and Henry Kolm. 1989. "An Electomagnetic \[sic\] Lunar Launcher Utilizing Superconductivity Technology." In *25th Joint Propulsion Conference*. AIAA 1989-2440. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1989-2440][research_bilby_et_al_1989]
- Bolonkin, Alexander A. 2005. "Circle Launcher and Space Keeper." In *Non-Rocket Space Launch and Flight*. Elsevier. [https://doi.org/10.1016/b978-008044731-5/50034-2][research_bolonkin_2005]
- Bolonkin, Alexander, and Mark Krinker. 2010. "Railgun Space Launcher." *Journal of Aerospace Engineering* 23 (4): 293–99. [https://doi.org/10.1061/(asce)as.1943-5525.0000041][research_bolonkin_krinker_2010]
- Carrio, Luis, Jonathan Barr, Austin Lillard, et al. 2025. "Concept for a Lunar Electromagnetic Launch System Architecture." In *2025 IEEE Aerospace Conference*. IEEE. [https://doi.org/10.1109/aero63441.2025.11068673][research_carrio_et_al_2025]
- Chilton, F. 1977. "Mass Driver Theory and History." In *3rd Conference on Space Manufacturing Facilities*. AIAA 1977-533. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1977-533][research_chilton_1977]
- Corbin, Cole K., and John E. Higgins. 2006. "Preliminary Mission Study: Mass Driver for Earth-Bound Asteroid Threat Mitigation." In *Earth & Space 2006*. American Society of Civil Engineers. [https://doi.org/10.1061/40830(188)18][research_corbin_higgins_2006]
- Fair, H. D. 2008. "Advances in Electromagnetic Launch Science and Technology and Its Applications." In *2008 14th Symposium on Electromagnetic Launch Technology*. IEEE. [https://doi.org/10.1109/elt.2008.9][research_fair_2008]
- Fine, K., F. Williams, P. Mongeau, and H. Kolm. 1979. "Mass Driver Two: Cryogenic Module." In *4th Conference on Space Manufacturing Facilities Princeton University*. AIAA 1979-1398. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1979-1398][research_fine_et_al_1979]
- Hawke, R., A. Brooks, C. Fowler, and D. Peterson. 1981. "Electromagnetic Railgun Launchers: Space Propulsion Applications." In *15th International Electric Propulsion Conference*. AIAA 1981-751. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1981-751][research_hawke_et_al_1981]
- Heppenheimer, T. 1975. "Transport of Lunar Material to the Sites of the Colonies." In *Space Manufacturing Facilities*. AIAA 1975-2003. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1975-2003][research_heppenheimer_1975]
- Hunter, John, and Rod Hyde. 1989. "A Light Gas Gun System for Launching Building Material into Low Earth Orbit." In *25th Joint Propulsion Conference*. AIAA 1989-2439. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1989-2439][research_hunter_hyde_1989]
- Kolm, H. 1977. "Basic Coaxial Mass Driver Reference Design." In *3rd Conference on Space Manufacturing Facilities*. AIAA 1977-534. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1977-534][research_kolm_1977]
- Mankins, John. 1994. "Electromagnetic Earth-to-Orbit Launch Concepts: One Strategy in Achieving Reductions in Launch Costs beyond the 'Next Generation'." In *Space Programs and Technologies Conference and Exhibit*. AIAA 1994-4625. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1994-4625][research_mankins_1994]
- "Mass-Driver Reaction Engine as Shuttle Upper Stage." 1977. In *3rd Conference on Space Manufacturing Facilities*. AIAA 1977-536. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1977-536][research_mass_driver_reaction_engine_1977]
- Muller, P. M., and W. L. Sjogren. 1968. "Mascons: Lunar Mass Concentrations." *Science* 161 (3842): 680–84. [https://doi.org/10.1126/science.161.3842.680][research_muller_sjogren_1968]
- O'Neill, Gerard. 1981. "Recent Development in Mass Drivers." In *Space Manufacturing 4: Proceedings of the Fifth Conference*. AIAA 1981-3235. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1981-3235][research_oneill_1981]
- Powell, J., and G. Maise. 2008. "StarTram: The Magnetic Launch Path to Very Low Cost, Very High Volume Launch to Space." In *2008 14th Symposium on Electromagnetic Launch Technology*. IEEE. [https://doi.org/10.1109/elt.2008.76][research_powell_maise_2008]
- Powell, James, George Maise, John Paniagua, and James Jordan. 2006. "StarTram: An International Facility to Magnetically Launch Payloads at Ultra Low Unit Cost." In *57th International Astronautical Congress*. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.iac-06-d3.2.07][research_powell_et_al_2006]
- Powell, J., G. Maise, J. Paniagua, and J. Rather. 2008. "Maglev Launch and the Next Race to Space." In *2008 IEEE Aerospace Conference*. IEEE. [https://doi.org/10.1109/aero.2008.4526501][research_powell_et_al_2008]
- Rocher, Raphael, Tristan Sarton du Jonchay, and Dimitri Mavris. 2025. "Cost-Benefit Analysis of Lunar Mass Driver Technologies." In *AIAA AVIATION Forum and ASCEND 2025*. AIAA 2025-4123. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2025-4123][research_rocher_et_al_2025]
- Roesler, Gordon. 2013. "Mass Estimate for a Lunar Resource Launcher Based on Existing Terrestrial Electromagnetic Launchers." *Machines* 1 (1): 50–62. [https://doi.org/10.3390/machines1010050][research_roesler_2013]
- Russell, C. T., C. A. Raymond, A. Coradini, et al. 2012. "Dawn at Vesta: Testing the Protoplanetary Paradigm." *Science* 336 (6082): 684–86. [https://doi.org/10.1126/science.1219381][research_russell_et_al_2012]
- Schmidt, Edward. 2006. "Electromagnetic Launch to Low Earth Orbit." In *42nd AIAA/ASME/SAE/ASEE Joint Propulsion Conference & Exhibit*. AIAA 2006-4626. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2006-4626][research_schmidt_2006]
- Seybold, Calina, and Wallace Fowler. 1994. "A Feasibility Study for the Use of a Lunar Mass Driver to Transport Cargo to Mars." In *32nd Aerospace Sciences Meeting and Exhibit*. AIAA 1994-854. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1994-854][research_seybold_fowler_1994]
- Snow, William, Joel Kubby, and R. Dunbar. 1981. "A Small Scale Lunar Launcher for Early Lunar Material Utilization." In *Space Manufacturing 4: Proceedings of the Fifth Conference*. AIAA 1981-3233. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1981-3233][research_snow_et_al_1981]
- Turman, B. N., and R. J. Lipinski. 1996. "Electromagnetic Coilgun Launcher for Space Applications." In *AIP Conference Proceedings*, vol. 361. AIP. [https://doi.org/10.1063/1.49932][research_turman_lipinski_1996]

### Secondary Sources

- Wieczorek, Mark A., Bradley L. Jolliff, Amir Khan, et al. 2006. "The Constitution and Structure of the Lunar Interior." *Reviews in Mineralogy and Geochemistry* 60 (1): 221–364. [https://doi.org/10.2138/rmg.2006.60.3][research_wieczorek_et_al_2006]

### General Sources

- O'Neill, Gerard K. 1974. "The Colonization of Space." *Physics Today* 27 (9): 32–40. [https://doi.org/10.1063/1.3128863][research_oneill_1974]

### Tertiary Sources

- "4 Vesta." 2026. Wikipedia. Last modified October 12, at 05:39 (UTC). [https://en.wikipedia.org/w/index.php?title=4\_Vesta&oldid=1379840288][ref_vesta]
- "Ceres (Dwarf Planet)." 2026. Wikipedia. Last modified October 20, at 04:55 (UTC). [https://en.wikipedia.org/w/index.php?title=Ceres\_(dwarf\_planet)&oldid=1381128658][ref_ceres]
- "Coilgun." 2026. Wikipedia. Last modified May 14, at 20:23 (UTC). [https://en.wikipedia.org/w/index.php?title=Coilgun&oldid=1354179401][ref_coilgun]
- "Deimos (Moon)." 2026. Wikipedia. Last modified October 20, at 07:24 (UTC). [https://en.wikipedia.org/w/index.php?title=Deimos\_(moon)&oldid=1381144075][ref_deimos]
- "Frozen Orbit." 2026. Wikipedia. Last modified August 19, at 06:59 (UTC). [https://en.wikipedia.org/w/index.php?title=Frozen\_orbit&oldid=1370125132][ref_frozen_orbit]
- "Hill Sphere." 2026. Wikipedia. Last modified October 7, at 17:52 (UTC). [https://en.wikipedia.org/w/index.php?title=Hill\_sphere&oldid=1379058821][ref_hill_sphere]
- "Lambert's Problem." 2026. Wikipedia. Last modified July 13, at 17:17 (UTC). [https://en.wikipedia.org/w/index.php?title=Lambert's\_problem&oldid=1363971699][ref_lamberts_problem]
- "Mass Concentration (Astronomy)." 2026. Wikipedia. Last modified January 22, at 20:33 (UTC). [https://en.wikipedia.org/w/index.php?title=Mass\_concentration\_(astronomy)&oldid=1334317000][ref_mass_concentration]
- "Mass Driver." 2026. Wikipedia. Last modified September 25, at 09:59 (UTC). [https://en.wikipedia.org/w/index.php?title=Mass\_driver&oldid=1376635859][ref_mass_driver]
- "Mercury (Planet)." 2026. Wikipedia. Last modified October 19, at 23:34 (UTC). [https://en.wikipedia.org/w/index.php?title=Mercury\_(planet)&oldid=1381089194][ref_mercury]
- "Moon." 2026. Wikipedia. Last modified October 20, at 15:52 (UTC). [https://en.wikipedia.org/w/index.php?title=Moon&oldid=1381191379][ref_moon]
- "Phobos (Moon)." 2026. Wikipedia. Last modified October 21, at 18:55 (UTC). [https://en.wikipedia.org/w/index.php?title=Phobos\_(moon)&oldid=1381338264][ref_phobos]
- "Railgun." 2026. Wikipedia. Last modified September 27, at 16:04 (UTC). [https://en.wikipedia.org/w/index.php?title=Railgun&oldid=1377035981][ref_railgun]
- "Tidal Locking." 2026. Wikipedia. Last modified October 4, at 04:00 (UTC). [https://en.wikipedia.org/w/index.php?title=Tidal\_locking&oldid=1378366143][ref_tidal_locking]

### Related Posts

- Sechter, Brendan. 2026. "Introduction to Space Studies." *Brendan A R Sechter's Development Blog*, February 21. [https://sgeos.github.io/space/math/2026/02/21/introduction\_to\_space\_studies.html][related_post_space_studies]
- Sechter, Brendan. 2026. "Orbital Manoeuvres in Terms of Delta-v." *Brendan A R Sechter's Development Blog*, August 17. [https://sgeos.github.io/space/space-studies/2026/08/17/orbital\_manoeuvres.html][related_post_orbital_manoeuvres]

[ref_ceres]: https://en.wikipedia.org/w/index.php?title=Ceres_(dwarf_planet)&oldid=1381128658
[ref_coilgun]: https://en.wikipedia.org/w/index.php?title=Coilgun&oldid=1354179401
[ref_deimos]: https://en.wikipedia.org/w/index.php?title=Deimos_(moon)&oldid=1381144075
[ref_frozen_orbit]: https://en.wikipedia.org/w/index.php?title=Frozen_orbit&oldid=1370125132
[ref_hill_sphere]: https://en.wikipedia.org/w/index.php?title=Hill_sphere&oldid=1379058821
[ref_lamberts_problem]: https://en.wikipedia.org/w/index.php?title=Lambert's_problem&oldid=1363971699
[ref_mass_concentration]: https://en.wikipedia.org/w/index.php?title=Mass_concentration_(astronomy)&oldid=1334317000
[ref_mass_driver]: https://en.wikipedia.org/w/index.php?title=Mass_driver&oldid=1376635859
[ref_mercury]: https://en.wikipedia.org/w/index.php?title=Mercury_(planet)&oldid=1381089194
[ref_moon]: https://en.wikipedia.org/w/index.php?title=Moon&oldid=1381191379
[ref_phobos]: https://en.wikipedia.org/w/index.php?title=Phobos_(moon)&oldid=1381338264
[ref_railgun]: https://en.wikipedia.org/w/index.php?title=Railgun&oldid=1377035981
[ref_tidal_locking]: https://en.wikipedia.org/w/index.php?title=Tidal_locking&oldid=1378366143
[ref_vesta]: https://en.wikipedia.org/w/index.php?title=4_Vesta&oldid=1379840288
[related_post_orbital_manoeuvres]: {% post_url 2026-08-17-orbital_manoeuvres %}
[related_post_orbital_manoeuvres_departure]: {% post_url 2026-08-17-orbital_manoeuvres %}#departure
[related_post_orbital_manoeuvres_hohmann]: {% post_url 2026-08-17-orbital_manoeuvres %}#the-hohmann-transfer
[related_post_orbital_manoeuvres_patched]: {% post_url 2026-08-17-orbital_manoeuvres %}#patched-conics
[related_post_orbital_manoeuvres_plane]: {% post_url 2026-08-17-orbital_manoeuvres %}#plane-change
[related_post_orbital_manoeuvres_rocket]: {% post_url 2026-08-17-orbital_manoeuvres %}#the-rocket-equation
[related_post_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[research_beemer_mcnab_2023]: https://doi.org/10.1016/j.actaastro.2023.02.041
[research_bilby_et_al_1989]: https://doi.org/10.2514/6.1989-2440
[research_bolonkin_2005]: https://doi.org/10.1016/b978-008044731-5/50034-2
[research_bolonkin_krinker_2010]: https://doi.org/10.1061/(asce)as.1943-5525.0000041
[research_carrio_et_al_2025]: https://doi.org/10.1109/aero63441.2025.11068673
[research_chilton_1977]: https://doi.org/10.2514/6.1977-533
[research_corbin_higgins_2006]: https://doi.org/10.1061/40830(188)18
[research_doyle_et_al_1995]: https://doi.org/10.1109/20.364638
[research_elipe_lara_2003]: https://doi.org/10.2514/2.5064
[research_ermakov_et_al_2017]: https://doi.org/10.1002/2017je005302
[research_ernst_et_al_2023]: https://doi.org/10.1186/s40623-023-01814-7
[research_fair_1982]: https://doi.org/10.1109/tmag.1982.1061789
[research_fair_2005]: https://doi.org/10.1109/tmag.2004.838744
[research_fair_2008]: https://doi.org/10.1109/elt.2008.9
[research_fine_et_al_1979]: https://doi.org/10.2514/6.1979-1398
[research_guo_et_al_2026]: https://doi.org/10.1093/mnras/stag578
[research_hawke_et_al_1981]: https://doi.org/10.2514/6.1981-751
[research_heppenheimer_1975]: https://doi.org/10.2514/6.1975-2003
[research_heppenheimer_1978a]: https://doi.org/10.2514/3.28004
[research_heppenheimer_1978b]: https://doi.org/10.2514/3.28009
[research_heppenheimer_1979]: https://doi.org/10.2514/3.57617
[research_heppenheimer_et_al_1982a]: https://doi.org/10.2514/3.19765
[research_heppenheimer_et_al_1982b]: https://doi.org/10.2514/3.19769
[research_heppenheimer_kaplan_1977]: https://doi.org/10.2514/3.7345
[research_hunter_hyde_1989]: https://doi.org/10.2514/6.1989-2439
[research_jacobson_lainey_2014]: https://doi.org/10.1016/j.pss.2013.06.003
[research_janhunen_2025]: https://doi.org/10.59332/jbis-078-08-0290
[research_kaye_2005]: https://doi.org/10.1109/tmag.2004.838982
[research_kolm_1977]: https://doi.org/10.2514/6.1977-534
[research_kolm_et_al_1980]: https://doi.org/10.1109/tmag.1980.1060806
[research_konopliv_et_al_2014]: https://doi.org/10.1016/j.icarus.2013.09.005
[research_konopliv_et_al_2018]: https://doi.org/10.1016/j.icarus.2017.08.005
[research_lipinski_et_al_1993]: https://doi.org/10.1109/20.195659
[research_mankins_1994]: https://doi.org/10.2514/6.1994-4625
[research_mass_driver_reaction_engine_1977]: https://doi.org/10.2514/6.1977-536
[research_mazarico_et_al_2014]: https://doi.org/10.1002/2014je004675
[research_mcnab_2003]: https://doi.org/10.1109/tmag.2002.805923
[research_mcnab_2009]: https://doi.org/10.1109/tmag.2008.2008601
[research_muller_sjogren_1968]: https://doi.org/10.1126/science.161.3842.680
[research_oleary_1992]: https://doi.org/10.1016/0094-5765(92)90141-5
[research_oneill_1974]: https://doi.org/10.1063/1.3128863
[research_oneill_1981]: https://doi.org/10.2514/6.1981-3235
[research_oneill_kolm_1980]: https://doi.org/10.1016/0094-5765(80)90002-8
[research_perry_et_al_2015]: https://doi.org/10.1002/2015gl065101
[research_powell_et_al_2006]: https://doi.org/10.2514/6.iac-06-d3.2.07
[research_powell_et_al_2008]: https://doi.org/10.1109/aero.2008.4526501
[research_powell_maise_2008]: https://doi.org/10.1109/elt.2008.76
[research_rashleigh_marshall_1978]: https://doi.org/10.1063/1.325107
[research_rocher_et_al_2025]: https://doi.org/10.2514/6.2025-4123
[research_roesler_2013]: https://doi.org/10.3390/machines1010050
[research_russell_et_al_2012]: https://doi.org/10.1126/science.1219381
[research_schmidt_2006]: https://doi.org/10.2514/6.2006-4626
[research_seybold_fowler_1994]: https://doi.org/10.2514/6.1994-854
[research_snow_dunbar_1982]: https://doi.org/10.1109/tmag.1982.1061772
[research_snow_et_al_1981]: https://doi.org/10.2514/6.1981-3233
[research_snow_et_al_1982]: https://doi.org/10.1109/tmag.1982.1061777
[research_turman_lipinski_1996]: https://doi.org/10.1063/1.49932
[research_verma_margot_2016]: https://doi.org/10.1002/2016je005037
[research_wieczorek_et_al_2006]: https://doi.org/10.2138/rmg.2006.60.3
[research_williams_et_al_2014]: https://doi.org/10.1002/2013je004559
[research_wright_et_al_2011]: https://doi.org/10.1109/tps.2010.2089066
