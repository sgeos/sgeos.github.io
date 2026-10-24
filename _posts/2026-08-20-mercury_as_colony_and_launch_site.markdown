---
layout: post
mathjax: true
comments: true
title: "Mercury as a Colony and a Launch Site"
date: 2026-08-20 09:00:00 +0000
categories: space astronomy space-studies
---

<!-- A384 -->
<script>console.log("A384");</script>

Mercury is the planet closest to the Sun
[Mercury][ref_mercury].
This article tests a two-part hypothesis about it with standard physics.
The first part holds that Mercury is the hardest known body in the solar system to colonize.
The second part holds that,
once colonized,
Mercury is the most beneficial place from which to launch probes,
both to the other bodies of the solar system
and to neighboring stars.
The article also sets out the other advantages and disadvantages of a base on Mercury,
in a hypothetical future in which every body in the solar system has been or can be settled.
A broader form of the hypothesis holds that Mercury's value lies less in what it is than in where it is,
and that the same is true of the closest significant body to any star.
The article tests that broader form as well.

The method is to express each physical quantity that matters as a function of distance from the Sun,
then to evaluate it at Mercury and at the bodies it competes with.
The quantities are sunlight for photovoltaic power,
orbital speed and the depth of the Sun's gravity well,
the change in velocity, or delta-v, that each journey requires,
the mass ratio that the rocket equation demands for that delta-v,
the length of a mass driver,
the sunlight a launcher must collect for each kilogram it throws,
the speed a projectile loses in an atmosphere,
the force of sunlight on a sail,
and the frequency of launch windows.
In short,
the first part is refuted as stated and supported only in a narrower form.
The second part is supported for probes sent toward the Sun,
for sails and beamed propulsion,
and for mass drivers powered by local sunlight,
but refuted for rocket probes sent outward.
The broader form is supported within any one star system for launches powered by sunlight,
and it weakens around dim stars and fails where the innermost body has no surface.

This article does not design a mission,
does not estimate costs,
and does not assess human physiology beyond noting where the evidence is absent.
Every calculation uses textbook idealizations that are stated before they are used,
and the results are order-of-magnitude comparisons rather than mission figures.
An earlier article on this site introduces the rocket equation and the Hohmann transfer used here
[Introduction to Space Studies][related_post_space_studies].

## The Model and Its Assumptions

Every orbital number in this article comes from one simple model.
Each body is placed on a circular orbit around the Sun at its semi-major axis,
and all orbits lie in one plane.
Transfers between bodies are Hohmann transfers,
which are the two-burn ellipses that touch the starting orbit and the destination orbit
[Hohmann Transfer Orbit][ref_hohmann_transfer_orbit].
A companion article derives the Hohmann transfer and the other manoeuvres used here in terms of delta-v
[Orbital Manoeuvres in Terms of Delta-v][related_post_orbital_manoeuvres].
The influence of a planet is handled by patched conics,
so a spacecraft feels only the planet near the planet and only the Sun elsewhere.
Burns are instantaneous.
A departure from a surface is treated as a single burn at the surface,
with no air drag,
no loss to gravity during a finite burn,
and no credit for the planet's rotation.

These assumptions make the comparison fair between bodies,
but they misstate any single real mission.
Mercury's orbit is the most eccentric of the planets,
with an eccentricity of 0.2056,
so its distance from the Sun ranges from 0.3075 to 0.4667 astronomical units,
or AU,
[Mercury][ref_mercury].
Real missions also use gravity assists,
which use a planet's gravity to change a spacecraft's path and speed and so save propellant
[Gravity Assist][ref_gravity_assist],
and those are treated separately below.
The scripts that compute each number are kept with the drafting records of this site,
and every figure given here can be reproduced from the formulas shown.

The solar constant,
the flux of sunlight at 1 AU,
is taken as 1,361 watts per square metre.
Kopp and Lean report 1,360.8 ± 0.5 watts per square metre during the 2008 solar minimum
[Kopp and Lean 2011][research_kopp_lean_2011].

## How the Environment Changes with Distance from the Sun

Four quantities follow directly from distance.
Let $r$ be the distance from the Sun in AU,
let $S_{0}$ be the solar constant,
let $\mu$ be the Sun's gravitational parameter,
and let $\sigma$ be the Stefan-Boltzmann constant.
The flux of sunlight,
the circular orbital speed,
the delta-v needed to escape the Sun from a circular orbit,
and the equilibrium temperature of a rapidly rotating black body
are given by the following.

$$
S(r) = \frac{S_{0}}{r^{2}}, \qquad
v_{c}(r) = \sqrt{\frac{\mu}{r}}, \qquad
\Delta v_{\mathrm{esc}}(r) = \left(\sqrt{2} - 1\right) v_{c}(r), \qquad
T_{\mathrm{eq}}(r) = \left(\frac{S(r)}{4\,\sigma}\right)^{1/4}
$$

The escape delta-v is the difference between the escape speed $\sqrt{2}\,v_{c}$ and the circular speed $v_{c}$.
The table evaluates these quantities at the mean distance of each body.

<div style="overflow-x: auto;" markdown="1">

| Body | Distance, AU | Sunlight, W/m² | Relative to Earth | Orbital speed, km/s | Delta-v to escape the Sun, km/s | Equilibrium temperature, K |
|---|---|---|---|---|---|---|
| Mercury | 0.387 | 9,083 | 6.67 | 47.87 | 19.83 | 447 |
| Venus | 0.723 | 2,601 | 1.91 | 35.02 | 14.51 | 327 |
| Earth | 1.000 | 1,361 | 1.00 | 29.78 | 12.34 | 278 |
| Mars | 1.524 | 586 | 0.43 | 24.13 | 9.99 | 226 |
| Ceres | 2.768 | 178 | 0.13 | 17.90 | 7.42 | 167 |
| Jupiter | 5.204 | 50.3 | 0.037 | 13.06 | 5.41 | 122 |
| Saturn | 9.583 | 14.8 | 0.011 | 9.62 | 3.99 | 90 |
| Neptune | 30.07 | 1.5 | 0.0011 | 5.43 | 2.25 | 51 |

</div>

The table carries the whole argument in compressed form.
Sunlight at Mercury is about six and two-thirds times its value at Earth,
and at perihelion it reaches 14,394 watts per square metre,
which is 2.30 times its value at aphelion.
For an orbit of semi-major axis $a$ and eccentricity $e$ the extremes and their ratio are the following,
and Mercury's eccentricity of 0.2056 gives the ratio of 2.30.

$$
S_{\mathrm{peri}} = \frac{S_{0}}{\left[a(1-e)\right]^{2}}, \qquad
S_{\mathrm{aph}} = \frac{S_{0}}{\left[a(1+e)\right]^{2}}, \qquad
\frac{S_{\mathrm{peri}}}{S_{\mathrm{aph}}} = \left(\frac{1+e}{1-e}\right)^{2}
$$
The same closeness that supplies the light also places Mercury deepest in the Sun's gravity well.
Leaving the solar system from a circular orbit at Mercury's distance costs 19.83 kilometres per second,
against 12.34 at Earth and 2.25 at Neptune.
Each later section is an elaboration of this tradeoff between abundant energy and a deep well.

## Part One, Whether Mercury Is the Hardest Body to Colonize

Colonization is hard in two separate ways.
A body can be hard to reach,
and a body can be hard to live on once reached.
This section treats the two separately,
because Mercury ranks very differently on each.

### Getting There

The Hohmann transfer fixes the excess speed a spacecraft needs at departure and the excess speed it carries on arrival.
For a transfer between circular orbits of radii $r_{1}$ and $r_{2}$,
with $a = (r_{1} + r_{2})/2$ the semi-major axis of the transfer ellipse,
the two excess speeds and the flight time are the following.

$$
v_{\infty,1} = \left|\sqrt{\mu\left(\frac{2}{r_{1}} - \frac{1}{a}\right)} - \sqrt{\frac{\mu}{r_{1}}}\right|, \qquad
v_{\infty,2} = \left|\sqrt{\frac{\mu}{r_{2}}} - \sqrt{\mu\left(\frac{2}{r_{2}} - \frac{1}{a}\right)}\right|, \qquad
t = \pi\sqrt{\frac{a^{3}}{\mu}}
$$

A burn deep in a planet's gravity well converts more efficiently into excess speed than a burn far from it,
which is the Oberth effect
[Oberth Effect][ref_oberth_effect],
treated with the same departure equation in the companion article on manoeuvres
[Orbital Manoeuvres in Terms of Delta-v, Departure][related_post_orbital_manoeuvres_departure].
For a body with surface escape speed $v_{e}$,
or a parking orbit with local escape speed $v_{e}$ and circular speed $v_{\mathrm{orb}}$,
the burns that produce or absorb an excess speed $v_{\infty}$ are the following.

$$
\Delta v_{\mathrm{surface}} = \sqrt{v_{\infty}^{2} + v_{e}^{2}}, \qquad
\Delta v_{\mathrm{orbit}} = \sqrt{v_{\infty}^{2} + v_{e}^{2}} - v_{\mathrm{orb}}
$$

Applying these to a departure from a 300 kilometre low Earth orbit,
or LEO,
a capture into a 100 kilometre circular orbit at the destination,
and a propulsive landing on an airless body
gives the following delta-v budgets.

<div style="overflow-x: auto;" markdown="1">

| Destination | Departure from LEO, km/s | Capture into low orbit, km/s | Landing, km/s | LEO to surface, km/s | Hohmann flight time |
|---|---|---|---|---|---|
| Moon | 3.11 | 0.82 | 1.63 | 5.56 | about 5 days |
| Mars | 3.59 | 2.11 | 3.50 without aerobraking | 9.21 | 259 days |
| Ceres | 4.90 | 4.55 | 0.33 | 9.78 | 472 days |
| Callisto | 6.30 | 3.58 | 1.69 | 11.57 | 998 days |
| Pluto | 8.37 | 3.04 | 0.82 | 12.23 | 45.5 years |
| Mercury | 5.55 | 7.53 | 2.95 | 16.02 | 105 days |

</div>

Mercury tops this table by a wide margin.
Each total is the sum of three terms,
the departure from low Earth orbit,
the capture into a low orbit of speed $v_{\mathrm{orb}}$ at the destination,
and a propulsive landing that removes $v_{\mathrm{orb}}$ on an airless body.

$$
\Delta v_{\mathrm{LEO\to surface}} = \left(\sqrt{v_{\infty,1}^{2} + v_{e,\mathrm{LEO}}^{2}} - v_{\mathrm{LEO}}\right) + \left(\sqrt{v_{\infty,2}^{2} + v_{e}^{2}} - v_{\mathrm{orb}}\right) + v_{\mathrm{orb}}
$$

The departure from Earth is moderate,
but the spacecraft falls 0.61 AU toward the Sun and arrives with an excess speed of 9.61 kilometres per second,
which it must cancel against a weak planetary gravity with no atmosphere to brake in.
The computed departure of 5.55 kilometres per second and the flight of about 3.5 months agree with the published delta-v budget,
which lists 5.5 kilometres per second from LEO and a transit of 3.5 months for Mercury
[Delta-v Budget][ref_delta_v_budget].
The Mars figure overstates the real cost,
because an atmosphere lets a lander shed most of its speed by drag,
and Mercury has no such option.
The Wikipedia survey of space colonization describes Mercury as the most energy-consuming body in the solar system to land on for spacecraft launched from Earth
[Space Colonization][ref_space_colonization],
and the table is consistent with that description among bodies with landable surfaces.

Real missions avoid this cost by spending time.
The mission named MESSENGER,
for Mercury Surface, Space Environment, Geochemistry and Ranging,
reached Mercury after flybys of Earth, Venus and Mercury itself
[MESSENGER][ref_messenger],
and Solomon and coauthors give an overview of the mission
[Solomon et al. 2007][research_solomon_et_al_2007].
BepiColombo,
the joint European and Japanese mission
[Benkhoff et al. 2021][research_benkhoff_et_al_2021],
launched in October 2018 and is planned to enter Mercury orbit in November 2026
[Murakami and Jones 2025][research_murakami_jones_2025],
after one Earth flyby, two Venus flybys and six Mercury flybys
[Mangano et al. 2021][research_mangano_et_al_2021].
It carries two orbiters,
Mio from the Japanese space agency and the Mercury Planetary Orbiter from the European Space Agency
[Benkhoff et al. 2021][research_benkhoff_et_al_2021].
MESSENGER's trajectory design and manoeuvre strategy,
and its mission design and navigation,
are documented by McAdams and coauthors
[McAdams et al. 2006][research_mcadams_et_al_2006]
[McAdams et al. 2007][research_mcadams_et_al_2007].
A Hohmann flight of 105 days thus becomes a journey of several years.
For a colony that must import people and equipment,
that choice between a large delta-v and a long voyage is a real and permanent burden.

### Living There

The thermal environment is severe but structured.
At Mercury's equator the surface ranges from −173 °C to 427 °C
[Mercury][ref_mercury],
values that the encyclopedia attributes to thermal modeling by Vasavada, Paige and Wood
[Vasavada et al. 1999][research_vasavada_paige_wood_1999].
A black surface facing the Sun with no conduction into the ground would reach the following temperature,
where $S$ is the local flux.

$$
T_{\mathrm{subsolar}} = \left(\frac{S}{\sigma}\right)^{1/4}
$$

This gives 710 K at perihelion and 576 K at aphelion.
The perihelion value lies just above the reported maximum of 427 °C,
about 700 K,
as it should for an ideal black surface that reflects nothing and conducts no heat downward.
The heat is not continuous at any one place.
Mercury rotates three times for every two orbits
[Mazarico et al. 2014][research_mazarico_et_al_2014],
so one solar day lasts about 176 Earth days,
and a fixed point on the equator spends about 88 Earth days in darkness.
The line between day and night moves across the equator at the following speed.

$$
v_{\mathrm{terminator}} = \frac{2\pi R}{P_{\mathrm{solar}}} = \frac{2\pi \times 2{,}439.7\ \mathrm{km}}{175.94 \times 24\ \mathrm{h}} \approx 3.63\ \mathrm{km/h}
$$

That is walking pace.
A settlement on rails could in principle stay in the mild band near the terminator indefinitely,
an inference from the arithmetic that has not been tested by any engineering study cited here.

The poles are more favourable still.
Mercury's spin axis is tilted by only 2.04 ± 0.08 arc minutes from its orbit normal
[Margot et al. 2012][research_margot_et_al_2012],
so parts of the floors of many polar craters never see the Sun.
Radar imaging in 1991 found highly reflective material at the north pole,
with polarization ratios previously seen only from icy regions of Mars and icy outer satellites
[Slade et al. 1992][research_slade_butler_muhleman_1992].
MESSENGER neutron spectrometer data,
together with thermal modeling,
confirmed that the main component of the radar-bright material at the north pole is water ice,
and laser altimeter reflectance measurements are consistent with some of it exposed at the surface
and some beneath dark deposits interpreted as an organic lag
[Lawrence et al. 2013][research_lawrence_et_al_2013]
[Neumann et al. 2013][research_neumann_et_al_2013]
[Paige et al. 2013][research_paige_et_al_2013].
Water is among the most important materials a settlement would otherwise have to import,
and Mercury has a local supply at its poles.
Within 10 degrees of the north pole almost all craters larger than 10 kilometres host radar-bright deposits in persistently shadowed areas,
and many smaller craters and craters as far south as 66 degrees north also host radar-bright material
[Chabot et al. 2013][research_chabot_et_al_2013].
Images from inside the shadowed craters show widespread surface ice in Prokofiev crater,
ice covered by a thin layer of dark,
organic-rich material elsewhere,
and sharp boundaries that indicate the deposits are geologically young
[Chabot et al. 2014][research_chabot_et_al_2014].
Laser altimetry of small craters in permanently shadowed regions has been used to constrain the thickness of the ice
[Deutsch et al. 2018][research_deutsch_et_al_2018].

Other conditions are less extreme than the reputation suggests.
Surface gravity is about 3.7 metres per second squared
[Mercury][ref_mercury],
which is almost the same as the 3.72 of Mars
[Mars][ref_mars].
Whether people can remain healthy at about 0.38 of Earth's gravity is unknown for both planets,
so on this point Mercury is no worse than the planet most often proposed for settlement.
Mercury has a global magnetic field,
which Mariner 10 detected in 1974
[Ness et al. 1974][research_ness_et_al_1974],
whose strength is about 1.1 percent of Earth's
[Mercury][ref_mercury],
and which MESSENGER resolved as an offset dipole with a moment of about 195 nanotesla times the cube of Mercury's radius
[Anderson et al. 2011][research_anderson_et_al_2011].
The field forms a magnetosphere that deflects the solar wind
[Ness et al. 1974][research_ness_et_al_1974],
but the measurements that follow show that it offers little shelter at the surface.
MESSENGER observed magnetic reconnection in the magnetosphere
[Slavin et al. 2009][research_slavin_et_al_2009]
and bursts of electrons above 30 kiloelectronvolts but no energetic protons,
because the weak field cannot hold Van Allen-type radiation belts
[Ho et al. 2011][research_ho_et_al_2011].

Radiation from solar storms is the clearest added hazard.
Lario and coauthors fitted the radial dependence of solar energetic proton events measured within 1 AU by the two Helios spacecraft and by Interplanetary Monitoring Platform 8,
or IMP 8.
They found event fluences that scale from $R^{-2.1}$ to $R^{-1.0}$ across their two energy bands,
and peak intensities from $R^{-2.7}$ to $R^{-1.9}$
[Lario et al. 2006][research_lario_et_al_2006].
Applying those exponents at Mercury's mean distance gives event fluences 2.6 to 7.3 times those at Earth's distance,
and peak intensities 6.1 to 13.0 times as high.
With a fitted exponent $k$,
the factor relative to 1 AU at a distance $r$ in AU is the following.

$$
\frac{F(r)}{F(1\ \mathrm{AU})} = r^{-k}
$$

They also found that the longitudinal separation between the parent active region and the magnetic footpoint of the spacecraft matters more than distance,
so these factors describe averages over many events rather than any single storm.
Shielding by regolith addresses the problem at any distance,
so the burden is the mass of the shielding rather than a hard limit on settlement.
Solar energetic electrons enter Mercury's magnetosphere almost instantly,
filling the regions of open field lines,
and they carry enough energy to penetrate more than 1 millimetre of aluminium.
MESSENGER measured precipitating fluxes of about 40 percent of the upstream level over the entire polar cap
[Gershman et al. 2015][research_gershman_et_al_2015],
which bears directly on polar sites chosen for their ice.
MESSENGER was the first spacecraft since the two Helios probes to measure the interplanetary medium in place inside 0.5 AU,
and Winslow and coauthors catalogued the interplanetary coronal mass ejections its magnetometer observed from 2011 to 2014
[Winslow et al. 2015][research_winslow_et_al_2015].

### Bodies That Are Harder

A literal reading of the first part compares Mercury with every known body,
and several are harder by any physical measure.
The surface of Venus averages 737 K at a pressure of 93 bar
[Venus][ref_venus],
which is hotter than Mercury's daytime maximum and is not relieved by any night or any pole.
The case for Venus settlement rests on floating habitats in the cloud layer rather than on the surface,
as an earlier article on this site describes
[Venus Cloudtop Buoyant Analog][related_post_venus_cloudtop].
Io orbits within an intense radiation environment created by Jupiter's magnetosphere and Io's own volcanic plasma torus
[Io][ref_io].
The giant planets have no solid surface at all,
and the computation above gives about 24 kilometres per second from LEO merely to reach a circular orbit 100 kilometres above Jupiter's cloud tops.
The Sun is not colonizable in any sense.

### Verdict on Part One

As stated,
the first part is refuted.
Venus's surface,
Io,
the giant planets
and the Sun are each harder to colonize than Mercury.
A narrower version is supported.
Among the bodies with surfaces that people could plausibly occupy,
Mercury is the most expensive to reach by propulsion alone,
with an ideal LEO-to-surface delta-v of 16.02 kilometres per second against 12.23 for Pluto and 5.56 for the Moon.
It also has the widest daily temperature swing at its equator.
Once there,
however,
Mercury offers ice,
abundant power,
Mars-like gravity
and a very slow day,
so it ranks as hard to reach but comparatively tractable to inhabit.

## Part Two A, Probes to the Rest of the Solar System

### Leaving Mercury's Surface

Mercury's surface escape speed is 4.25 kilometres per second
[Mercury][ref_mercury].
This is less than the 5.03 of Mars
[Mars][ref_mars]
and much less than the 11.19 of Earth
[Earth][ref_earth],
although more than the 2.38 of the Moon
[Moon][ref_moon]
and the 0.52 of Ceres
[Ceres][ref_ceres].
Mercury's exosphere has a surface pressure of about 0.5 nanopascal or less
[Mercury][ref_mercury].
A recent conference abstract gives a looser upper limit of 10⁻¹¹ to 10⁻¹² bar,
which is 0.1 to 1 micropascal
[Lammer et al. 2026][research_lammer_et_al_2026].
Both figures are upper limits,
so this article treats the surface pressure as lying in a hypothetical range from zero to 1 micropascal.
Even the top of that range leaves an air column of only 2.7 × 10⁻⁷ kilograms per square metre,
so launching from Mercury is effectively launching from vacuum.
That makes Mercury a candidate for a mass driver,
an electromagnetic launcher that accelerates a payload along a track
[Mass Driver][ref_mass_driver].
A companion article treats mass drivers in detail
[Mass Drivers][related_post_mass_drivers],
and this article uses only the kinematics.
For a constant acceleration $a$ to a speed $v$,
the track length and the kinetic energy per kilogram are the following.

$$
L = \frac{v^{2}}{2a}, \qquad
\frac{E}{m} = \frac{v^{2}}{2}
$$

Reaching Mercury's escape speed requires a track of 9.21 kilometres at 100 times standard gravity,
or 0.92 kilometres at 1,000 times,
and an energy of 9.0 megajoules per kilogram.
A prototype mass driver demonstrated an acceleration of 33 times standard gravity
[Mass Driver][ref_mass_driver],
and launch parameters for a lunar mass accelerator carrying ice have been studied
[Beemer and McNab 2023][research_beemer_mcnab_2023].
The accelerations assumed here are therefore well beyond any demonstration,
and they would suit hardened cargo rather than people.

An atmosphere is what rules out the same approach on most other bodies.
For a projectile leaving vertically,
with ballistic coefficient $B = m/(C_{D} A)$,
air drag gives $dv/dh = -\rho v/(2B)$.
Integrating over the whole air column,
whose mass per unit area is $\Sigma = P_{0}/g$ for surface pressure $P_{0}$,
gives the following,
neglecting gravity during the passage through the air and the heating of the projectile.

$$
\frac{v_{\mathrm{out}}}{v_{\mathrm{in}}} = \exp\left(-\frac{\Sigma}{2B}\right)
$$

For a dense projectile with $B = 10{,}000$ kilograms per square metre the results are as follows.

<div style="overflow-x: auto;" markdown="1">

| Body | Surface pressure | Air column, kg/m² | Fraction of speed kept | Fraction of kinetic energy lost |
|---|---|---|---|---|
| Mercury | 0 to 1 µPa | at most 2.7 × 10⁻⁷ | 1.000 | effectively 0 |
| Mars | 0.636 kPa | 171 | 0.991 | 1.7 percent |
| Earth | 101.3 kPa | 10,332 | 0.597 | 64 percent |
| Titan | 146.7 kPa | 108,506 | 0.0044 | effectively all |
| Venus | 9.3 MPa | 1,048,478 | about 10⁻²³ | all |

</div>

The surface pressures of Mars,
Titan and Venus come from their Wikipedia entries
[Mars][ref_mars]
[Titan][ref_titan]
[Venus][ref_venus].
An Earth launch loses 40 percent of its speed and nearly two-thirds of its energy to the air in this model,
and Titan's thick atmosphere under weak gravity makes it far worse than Earth.
Among bodies with substantial gravity,
only airless ones such as Mercury and the Moon can use a surface mass driver,
with Mars a near miss.

### The Sun's Gravity Well

Leaving Mercury is cheap,
but leaving Mercury's orbit around the Sun is not.
Combining the Hohmann excess speeds with the surface departure formula gives the ideal delta-v from the surface of each origin to a flyby of each target,
with the Moon's departure computed through Earth's gravity well from the Moon's orbit.
For the Moon the excess $v_{\infty}$ relative to Earth is first converted to a speed relative to the Moon at the Moon's orbital radius $a_{M}$,
crediting the Moon's orbital speed $V_{M}$,
and then to a speed at the lunar surface,
the two-body launch geometry treated in the companion article on mass drivers
[Mass Drivers, From the Launching Body to the Parent][related_post_mass_drivers_parent].

$$
v_{\mathrm{rel}} = \sqrt{v_{\infty}^{2} + \frac{2\mu_{\oplus}}{a_{M}}} - V_{M}, \qquad
v_{\mathrm{surface}} = \sqrt{v_{\mathrm{rel}}^{2} + \frac{2\mu_{M}}{R_{M}}}
$$

<div style="overflow-x: auto;" markdown="1">

| Origin | Venus | Earth | Mars | Jupiter | Saturn | Neptune | Escape from the Sun |
|---|---|---|---|---|---|---|---|
| Mercury | 7.99 | 10.51 | 13.28 | 17.95 | 18.98 | 19.86 | 20.28 |
| Earth | 11.46 | origin | 11.57 | 14.23 | 15.20 | 16.15 | 16.65 |
| Moon | 3.02 | origin | 3.28 | 8.24 | 9.68 | 10.98 | 11.65 |
| Mars | 6.93 | 5.68 | origin | 7.74 | 9.09 | 10.45 | 11.19 |
| Ceres | 6.40 | 4.89 | 2.86 | 2.61 | 4.43 | 6.35 | 7.43 |

</div>

All values are in kilometres per second.
Earth's figures omit air drag and gravity losses,
which the published budget puts at a total of about 9.3 to 10 kilometres per second just to reach LEO
[Delta-v Budget][ref_delta_v_budget],
so Earth's real costs are higher than shown.

Mercury is the worst origin in this table for every target beyond Venus.
A probe to Jupiter needs a heliocentric excess speed of 17.44 kilometres per second from Mercury,
twice the 8.79 needed from Earth.
The Moon,
Mars
and especially Ceres are far better origins for the outer solar system.

The rocket equation turns these differences into mass
[Tsiolkovsky Rocket Equation][ref_tsiolkovsky_rocket_equation]
[Orbital Manoeuvres in Terms of Delta-v, The Rocket Equation][related_post_orbital_manoeuvres_rocket].
For a specific impulse $I_{\mathrm{sp}}$ and standard gravity $g_{0}$,
the ratio of initial to final mass is the following.

$$
R = \exp\left(\frac{\Delta v}{g_{0}\, I_{\mathrm{sp}}}\right)
$$

<div style="overflow-x: auto;" markdown="1">

| Departure to escape from the Sun | Delta-v, km/s | Mass ratio at 450 s | Mass ratio at 900 s |
|---|---|---|---|
| Mercury surface | 20.28 | 99.0 | 9.95 |
| Earth surface, ideal | 16.65 | 43.5 | 6.60 |
| Moon surface | 11.65 | 14.0 | 3.74 |

</div>

The value of 450 seconds is assumed here as representative of hydrogen and oxygen engines,
and 900 seconds is used here as a representative figure for nuclear thermal propulsion.
Both are assumptions rather than cited values.
A chemical rocket leaving the solar system from Mercury must start about 99 times as heavy as its final mass,
more than twice the ratio from an ideal Earth launch and about seven times the ratio from the Moon.

### Probes Launched by Mass Driver

A mass driver changes which cost matters.
A rocket pays for delta-v with propellant,
and the rocket equation makes that cost exponential.
An electromagnetic launcher pays for the same speed with electricity,
in proportion to $v^{2}/2$ for each kilogram.
If the electricity comes from local sunlight,
the cost to compare is the collector area multiplied by the time needed to gather the launch energy.
For a conversion efficiency $\eta$ from sunlight to launch energy and a local flux $S(r)$,
that collector time per kilogram is the following.

$$
\frac{A\,t}{m} = \frac{v^{2}}{2\,\eta\,S(r)}
$$

The table applies this to three airless origins and four kinds of launch,
using the surface speeds from the surface departure formula,
a track at 1,000 times standard gravity
and $\eta = 0.2$.

<div style="overflow-x: auto;" markdown="1">

| Origin | Launch | Surface speed, km/s | Track at 1,000 g, km | Energy, MJ/kg | Collector time, m²·h/kg |
|---|---|---|---|---|---|
| Mercury | escape Mercury only | 4.25 | 0.92 | 9.0 | 1.4 |
| Mercury | flyby of Jupiter | 17.95 | 16.43 | 161.2 | 24.6 |
| Mercury | escape from the Sun | 20.28 | 20.97 | 205.6 | 31.4 |
| Mercury | dive to 10 solar radii | 26.05 | 34.60 | 339.3 | 51.9 |
| Moon | escape the Moon only | 2.38 | 0.29 | 2.8 | 2.9 |
| Moon | flyby of Jupiter | 8.24 | 3.46 | 34.0 | 34.7 |
| Moon | escape from the Sun | 11.65 | 6.92 | 67.8 | 69.2 |
| Moon | dive to 10 solar radii | 20.08 | 20.55 | 201.6 | 205.7 |
| Ceres | escape Ceres only | 0.52 | 0.01 | 0.1 | 1.0 |
| Ceres | flyby of Jupiter | 2.61 | 0.35 | 3.4 | 26.5 |
| Ceres | escape from the Sun | 7.43 | 2.82 | 27.6 | 216.0 |
| Ceres | dive to 10 solar radii | 14.66 | 10.95 | 107.4 | 839.7 |

</div>

Mercury needs the highest speeds and the longest tracks in every row,
up to 34.6 kilometres of track for a probe thrown straight into a dive toward the Sun.
Measured by the sunlight that must be gathered,
however,
Mercury is the cheapest origin for escaping the Sun and for diving toward it,
by factors of about 2 and 4 against the Moon and about 7 and 16 against Ceres.
For a Jupiter flyby the three origins are within a factor of 1.4 of one another.
Only for leaving the launch body itself,
the smallest job in the table,
do the Moon and Ceres need less collector time.

The reason is general.
The orbital part of the launch energy scales as $\mu/r$,
while the sunlight scales as $L/r^{2}$ for a star of luminosity $L$,
so the collector time for any launch measured against orbital speed scales as follows,
with $M$ the star's mass.

$$
\frac{A\,t}{m} \propto \frac{\mu / r}{L / r^{2}} \propto \frac{M\,r}{L}
$$

For escape from a circular orbit around the Sun,
this gives 30.1 square metre hours per kilogram at Mercury's distance,
56.2 at Venus's,
77.7 at Earth's,
118.3 at Mars's
and 214.9 at Ceres's,
before the small extra cost of leaving the launch body.
Around any single star,
the collector time falls in direct proportion to the distance,
so the innermost orbit is the cheapest place from which to throw mass with sunlight.
This is the clearest support in this article for the claim that Mercury's value lies in where it is.

Three practical limits qualify the result.
First,
the conversion efficiency of 20 percent ignores losses in the launcher itself,
night,
and energy storage,
and Mercury's nights of 88 days at a fixed site are much longer than the Moon's,
which last about half of a 29.53-day synodic month
[Lunar Month][ref_lunar_month].
Second,
accelerations of 1,000 times standard gravity suit only rugged payloads,
and whether a folded sail or a delicate instrument survives them is not established here.
A track around Mercury's whole circumference would remove the limit of track length,
but at release it must hold the payload down with the curvature load derived in the mass driver article
[Mass Drivers, The Curvature Limit][related_post_mass_drivers_curvature],
which for the 20.28 kilometre per second escape from the Sun is 165 metres per second squared,
16.8 times standard gravity.

$$
a_{n} = \frac{v^{2}}{R} - g
$$

Third,
a track fixed to the ground points in a direction that turns relative to the Sun once per solar day.
That period is about 176 days on Mercury,
29.53 days for the Moon,
which is the mean synodic month
[Lunar Month][ref_lunar_month],
and about 9.07 hours for Ceres,
whose sidereal day is 9.074 hours
[Ceres][ref_ceres].
A departure toward a given target must leave in a particular direction relative to the planet's orbital motion,
so a single fixed track on Mercury lines up with that direction only about once every 176 days.
The interval is the period of the track's rotation relative to the direction of orbital motion,
which for a body spinning in the same sense as it orbits is the following,
with $P_{\mathrm{sid}}$ the sidereal rotation period and $P_{\mathrm{orb}}$ the orbital period.

$$
P_{\mathrm{align}} = \left|\frac{1}{P_{\mathrm{sid}}} - \frac{1}{P_{\mathrm{orb}}}\right|^{-1}
$$

Mercury's rotation period of 58.646 days
[Mazarico et al. 2014][research_mazarico_et_al_2014]
and orbital period of 87.969 days
[Mercury][ref_mercury]
give 176 days.
The siting rules for fixed tracks are developed in the mass driver article
[Mass Drivers, Positioning for Parent Orbits][related_post_mass_drivers_positioning].
This is an inference from the geometry.
It suggests that a Mercury launch site would need several tracks at different headings,
or a way to steer the exit,
to use its frequent launch windows.

### Launch Windows and Trip Times

Mercury's short year has one clear benefit.
Launch opportunities between two bodies recur once per synodic period,
which for orbital periods $P_{1}$ and $P_{2}$ is the following.

$$
P_{\mathrm{syn}} = \left|\frac{1}{P_{1}} - \frac{1}{P_{2}}\right|^{-1}
$$

<div style="overflow-x: auto;" markdown="1">

| Origin | Venus | Earth | Mars | Jupiter | Saturn | Neptune |
|---|---|---|---|---|---|---|
| Mercury | 145 | 116 | 101 | 90 | 89 | 88 |
| Earth | 584 | origin | 780 | 399 | 378 | 367 |
| Mars | 334 | 780 | origin | 816 | 733 | 695 |
| Ceres | 259 | 467 | 1,161 | 2,747 | 1,991 | 1,730 |

</div>

All values are in days.
From Mercury a window to any outer planet opens about every three months,
against roughly once a year from Earth and about once every two years from Mars.
For a body that wants to launch probes continuously,
this is a real logistical advantage.
The Hohmann flight time is also somewhat shorter from Mercury to the outer planets,
854 days to Jupiter against 998 from Earth,
because the transfer ellipse is smaller,
but the saving does not offset the extra delta-v.

### Probes Toward the Sun

For the opposite direction the advantage reverses.
Mercury is the best origin for missions to Venus and to the Sun itself.
The Parker Solar Probe
used seven Venus gravity assists to lower its perihelion step by step
[Fox et al. 2015][research_fox_et_al_2015]
to a minimum of 9.86 solar radii
[Ercol and Balakrishnan 2024][research_ercol_balakrishnan_2024],
which it first reached in December 2024
[Badman 2026][research_badman_2026].
From a circular orbit the delta-v to lower perihelion to 10 solar radii is 25.70 kilometres per second at Mercury's distance,
against 20.91 at Earth's,
so a direct drop is not cheaper from Mercury.
What Mercury offers instead is proximity.
Its synodic period with Venus is 145 days rather than Earth's 584,
the flight to Venus takes 0.21 years rather than 0.40,
and a probe launched from Mercury begins its mission already between 0.31 and 0.47 AU from the Sun.

### Verdict on Part Two A

Part Two A splits by propulsion.
For rocket probes to the outer solar system,
it is refuted.
Mercury costs the most delta-v of any origin for every target beyond Venus,
and Ceres,
the Moon
and Mars are each cheaper.
For probes thrown by mass drivers that run on local sunlight,
it is supported for escaping the Sun and for diving toward it,
and roughly a tie for the outer planets,
because the sunlight needed per kilogram is lowest at Mercury
even though the speeds and tracks are the largest.
For probes to Venus and toward the Sun,
and for frequent launch windows,
it is supported.

## Part Two B, Probes to Neighboring Stars

Interstellar probes face a different problem.
The nearest star system is about 4.34 light years away
[Breakthrough Starshot][ref_breakthrough_starshot],
and the coasting times at speeds within reach of a solar-system launch are as follows.

<div style="overflow-x: auto;" markdown="1">

| Speed | Basis | Years to 4.34 light years |
|---|---|---|
| 17 km/s | an illustrative slow probe | 76,535 |
| 29.8 km/s | Earth's orbital speed | 43,683 |
| 47.9 km/s | the orbital speed at Mercury's distance | 27,179 |
| 300 km/s | an illustrative fast sail | 4,337 |
| 0.1 of light speed | an illustrative beamed probe | 43 |

</div>

Each entry is the distance divided by the speed,
$t = d/v$,
for a probe coasting at constant speed.

Differences of a few kilometres per second at launch,
which dominate Part Two A,
are irrelevant here.
What matters is whether the location gives access to a propulsion method that can reach hundreds or thousands of kilometres per second.
Three methods depend on the Sun,
and Mercury's position affects each differently.

### Rockets and the Solar Oberth Manoeuvre

The Oberth effect applies to the Sun as it does to a planet
[Oberth Effect][ref_oberth_effect].
A spacecraft that falls to a low perihelion $r_{p}$,
arrives with speed $v_{p}$,
and burns $\Delta v$ there leaves the solar system with the following excess speed.

$$
v_{\infty} = \sqrt{\left(v_{p} + \Delta v\right)^{2} - \frac{2\mu}{r_{p}}}
$$

The perihelion speed is larger when the fall begins farther out,
so the manoeuvre favours an origin far from the Sun,
not near it.

<div style="overflow-x: auto;" markdown="1">

| Fall begins at | Delta-v to drop perihelion to 10 solar radii, km/s | Perihelion speed, km/s | Burn needed there to escape, km/s | Excess speed after a 10 km/s burn, km/s |
|---|---|---|---|---|
| Mercury's distance | 25.70 | 184.6 | 10.77 | does not escape |
| Earth's distance | 20.91 | 190.9 | 4.39 | 47.2 |
| Jupiter's distance | 11.32 | 194.5 | 0.87 | 60.4 |

</div>

Escape from 10 solar radii requires 195.3 kilometres per second.
A probe that starts its fall from Mercury's orbit carries the least energy and reaches perihelion with the least speed,
so it gains the least from the same burn.
Surviving such a perihelion also requires heat protection,
and a combined heat shield and solar thermal propulsion system for an Oberth manoeuvre has been studied
[Benkoski et al. 2023][research_benkoski_et_al_2023].
Lyman and coauthors studied solar thermal propulsion for an interstellar probe,
with engines that heat hydrogen to about 3,000 K
for a solar gravity assist with a perihelion of 3 to 4 solar radii
[Lyman et al. 2001][research_lyman_et_al_2001].
Project Lyra studied sending a spacecraft to the interstellar object 1I/'Oumuamua
[Hein et al. 2019][research_hein_et_al_2019],
and a later study examined such a mission without a solar Oberth manoeuvre
[Hibberd et al. 2022][research_hibberd_et_al_2022].
By comparison,
a low-altitude Jupiter flyby with a large launch vehicle can give heliocentric escape speeds above 8 AU per year,
about 38 kilometres per second,
since 1 AU per year is 4.74 kilometres per second
[Schlei et al. 2021][research_schlei_et_al_2021].
For rocket-driven interstellar probes,
Mercury is the worst starting point among the bodies considered here.

### Solar Sails

A solar sail is pushed by reflected sunlight
[Solar Sail][ref_solar_sail]
[McInnes 1999][book_mcinnes_1999].
A companion article treats solar sailing in detail
[Solar Sailing][related_post_solar_sailing],
including the lightness number for any star
[Solar Sailing, Lightness Number for Any Star][related_post_solar_sailing_lightness],
and this article uses only the results it needs.
Both the force of sunlight and the pull of gravity fall as the inverse square of distance,
so their ratio,
the lightness number $\beta$,
is independent of distance from the Sun
[Solar Sail][ref_solar_sail].
For a perfectly reflecting sail facing the Sun,
with solar luminosity $L_{\odot}$,
light speed $c$
and sail mass per unit area $\sigma_{s}$,
the lightness number and the loading at which it equals one are the following.

$$
\beta = \frac{L_{\odot}}{2\pi c\,\mu\,\sigma_{s}}, \qquad
\sigma^{*} = \frac{L_{\odot}}{2\pi c\,\mu} \approx 1.53\ \mathrm{g/m^{2}}
$$

A sail opened on a circular orbit of radius $r_{0}$ feels an effective solar gravity reduced by the factor $1 - \beta$,
so energy conservation gives the following speed far from the Sun when $\beta > 1/2$.

$$
v_{\infty} = v_{c}(r_{0})\sqrt{2\beta - 1}
$$

Opening the sail at Mercury's distance gives $1/\sqrt{0.387} = 1.61$ times the final speed of the same sail opened at Earth's distance,
which is 47.9 against 29.8 kilometres per second when $\beta = 1$,
and 33.9 against 21.1 when $\beta = 0.75$.
This advantage is the strongest result in Mercury's favour,
but it belongs to the distance rather than to the planet.
A sail can spiral inward from Earth by tilting its force against its direction of motion,
and the classic interstellar sail concept first drops into an orbit that passes close to the Sun before accelerating outward
[Solar Sail][ref_solar_sail].
A sail opened at a perihelion of 10 solar radii with $\beta = 1$ would coast away at about 185 to 194 kilometres per second depending on where the fall began,
far more than anything Mercury's orbit alone provides.
The sail must survive the light and heat at that distance in either case.

### Repeated Passes Near the Sun

Bailer-Jones showed that combining a sail with an impulse that dives toward the Sun has a threshold.
Once the available delta-v exceeds a value set by the sail's lightness number,
the best strategy is to spend it all diving as close to the Sun as possible,
and below the threshold the best strategy is not to dive at all
[Bailer-Jones 2021][research_bailer_jones_2021].
The Interstellar Heliopause Probe study used two passes at 0.25 AU,
inside Mercury's perihelion
[Lappas et al. 2005][research_lappas_et_al_2005].

A sail held face-on to the Sun feels a purely radial force that falls as the inverse square of distance.
That force only weakens the Sun's effective gravity,
so over a closed orbit it adds no energy.
A sail that is tilted so that its force has a component along its direction of motion spirals outward,
and one tilted the other way spirals inward
[Solar Sail][ref_solar_sail].
If the tilt is applied mainly near perihelion,
where the light is strongest,
each pass raises the orbit's energy while the perihelion stays low,
and the orbit grows pass by pass until the sail escapes.
This is the repeated-pass strategy.
Unlike a gravity assist,
it borrows nothing from a moving planet.
The sail is propelled by the light it reflects.

A simple reference shows what repeated passes can and cannot do.
A sail that falls from an orbit of semi-major axis $a$ to a perihelion $q$
and turns face-on there for the final departure
leaves with the following excess speed,
which rises toward a ceiling as the orbit is pumped toward escape.

$$
v_{\infty} = \sqrt{\frac{2\beta\mu}{q} - \frac{\mu}{a}}
\;\longrightarrow\;
\sqrt{\frac{2\beta\mu}{q}} \quad \text{as} \quad a \to \infty
$$

The ceiling depends only on the sail's lightness number and on the perihelion it can survive.
It does not depend on where the sail started.
With $\beta = 1$ at 10 solar radii,
one pass from the Mercury dive orbit gives 184.6 kilometres per second against a ceiling of 195.3,
so repeated passes add little for a very light sail.
With $\beta = 0.1$,
one face-on pass from the Mercury dive orbit does not escape at all,
while the ceiling is 61.8 kilometres per second,
so for weaker sails repeated passes decide whether the strategy works.

A numerical simulation tests the strategy for weaker sails.
It integrates the planar motion of an ideal flat sail around the Sun,
with a force of $\beta\mu\cos^{2}\alpha/r^{2}$ along the sail's normal,
where $\alpha$ is the angle between the normal and the direction to the Sun.
The control law is simple and is not an optimum.
Within about twice the target perihelion,
the sail takes the tilt that adds energy fastest.
Farther out,
it tilts to lower its perihelion if that has drifted more than two percent above the target,
and otherwise turns edge-on.
Each run starts at the aphelion of a dive orbit from Mercury's distance or Earth's,
so the cost of entering the dive is excluded.
The integrator reproduces the analytic results above to the precision shown,
and it conserves energy to about one part in $10^{14}$ over ten unpowered orbits.

<div style="overflow-x: auto;" markdown="1">

| Perihelion | $\beta$ | Start | Perihelion passes | Years | Final speed, km/s |
|---|---|---|---|---|---|
| 10 solar radii | 0.01 | Mercury | 9 | 80, not escaped | none |
| 10 solar radii | 0.01 | Earth | 4 | 10.3 | 16.9 |
| 10 solar radii | 0.02 | Mercury | 5 | 6.5 | 27.4 |
| 10 solar radii | 0.02 | Earth | 2 | 4.9 | 21.5 |
| 10 solar radii | 0.05 | Mercury | 2 | 2.8 | 35.0 |
| 10 solar radii | 0.05 | Earth | 1 | 2.5 | 37.6 |
| 10 solar radii | 0.1 | Mercury | 1 | 2.1 | 44.9 |
| 10 solar radii | 0.1 | Earth | 1 | 1.6 | 65.8 |
| 0.1 AU | 0.01 | Mercury | 17 | 30.9 | 11.8 |
| 0.1 AU | 0.01 | Earth | 8 | 30.7 | 12.2 |
| 0.1 AU | 0.02 | Mercury | 9 | 19.5 | 20.0 |
| 0.1 AU | 0.02 | Earth | 4 | 10.5 | 15.0 |
| 0.1 AU | 0.05 | Mercury | 4 | 6.2 | 31.0 |
| 0.1 AU | 0.05 | Earth | 2 | 5.0 | 29.1 |
| 0.1 AU | 0.1 | Mercury | 2 | 3.0 | 34.6 |
| 0.1 AU | 0.1 | Earth | 1 | 2.7 | 34.8 |

</div>

Four results follow.
First,
repeated passes let weak sails escape that could not escape in one face-on pass,
with up to 17 passes for $\beta = 0.01$ at 0.1 AU.
Second,
a tilted sail can beat the face-on ceiling,
as the 65.8 kilometres per second for $\beta = 0.1$ against a ceiling of 61.8 shows,
so the ceiling is a reference rather than a limit.
Third,
starting from Mercury's distance needs more passes than starting from Earth's,
not fewer,
because the Mercury dive orbit is more tightly bound.
Its passes come more often,
every 37 days at first against 138 for the Earth dive orbit,
but in this simulation the total time was the same or longer.
Fourth,
the final speeds are not consistently ordered by $\beta$ or by starting point,
which shows that this control law leaves much on the table.
The numbers indicate the scale of the strategy rather than its best performance.

Repeated passes therefore make the sun-diving strategy available to sails far weaker than $\beta = 1$,
but they do not favour Mercury as a starting orbit.
What favours Mercury is the cost of delivering a sail into its dive.
A mass driver on Mercury powered by local sunlight needs 51.9 square metre hours of collector per kilogram for a dive to 10 solar radii,
against 205.7 on the Moon,
if the sail survives the launch.
Mercury's role is therefore as the cheapest place to make,
launch
and stage sails,
not as a physically privileged starting orbit.

### Beamed Propulsion

A laser-driven sail shifts the energy problem to the launch site.
Directed energy can in principle push low-mass craft to relativistic speeds,
with the diffraction of the beam limiting the maximum speed
[Kulkarni et al. 2018][research_kulkarni_lubin_zhang_2018],
and Breakthrough Starshot has been modelled as a whole system
[Parkin 2018][research_parkin_2018].
Near-term beamed sail missions,
including one named Sun-Diver,
have also been proposed
[Benford and Benford 2003][research_benford_benford_2003].
Breakthrough Starshot proposed gram-scale light sails pushed to about 20 percent of light speed
[Hoang et al. 2017][research_hoang_et_al_2017]
by a kilometre-scale ground-based phased-array laser of 100 gigawatts
[Worden et al. 2021][research_worden_et_al_2021].
Whatever the power such a system needs,
its collectors scale inversely with the local sunlight.
Supplying 100 gigawatts of electricity from photovoltaics at 20 percent conversion,
which understates the input that lasers of that output would draw,
requires 55.0 square kilometres of collector at Mercury's mean distance
and 367 square kilometres at 1 AU in space,
with more on the ground at Earth because of night,
weather and the atmosphere,
by the collector area needed for an electrical power $P$ at conversion efficiency $\eta$.

$$
A = \frac{P}{\eta\,S(r)}
$$

Mercury's vacuum also removes atmospheric absorption and turbulence from the beam path.

The same caveat applies as for sails.
The sunlight is a property of the distance,
so a collector array in orbit at 0.39 AU receives the same flux as Mercury's surface.
Mercury contributes a solid foundation,
local materials,
cold polar terrain for radiators
and a slow rotation that keeps a site facing a given direction in the sky for weeks rather than hours.
No vulcanoid asteroids inside Mercury's orbit have been found
[Vulcanoid][ref_vulcanoid].
A search of coronagraph images found no object brighter than visual magnitude 7,
which rules out bodies larger than about 60 kilometres
[Schumacher and Gay 2001][research_schumacher_gay_2001],
so Mercury is the only known large source of material that close to the Sun.
Long-lived asteroid belts in the inner solar system have been proposed as possible
[Evans and Tabachnik 1999][research_evans_tabachnik_1999],
and the STEREO heliospheric imagers have been used to search for them
[Steffl et al. 2013][research_steffl_et_al_2013].

### Communication Geometry

A base close to the Sun has one persistent communication cost.
A distant probe sees its home within the following angle of the Sun,
where $r_{h}$ is the home's distance from the Sun and $d$ is the probe's distance.

$$
\theta_{\max} = \arcsin\left(\frac{r_{h}}{d}\right)
$$

Using Mercury's aphelion distance,
a probe at Jupiter's distance sees Mercury within 5.15 degrees of the Sun,
against 11.09 degrees for Earth,
and at Neptune's distance the angles are 0.89 and 1.91 degrees.
The Sun is a strong source of radio noise,
so a home that always appears closer to the Sun's disc is harder to listen to.
This penalty is a geometric fact,
but its size in decibels depends on antennas and frequencies that this article does not model.
Mercury also passes close to the Sun in the sky as seen from Earth at superior conjunction,
once in every 116-day synodic period
[Mercury][ref_mercury],
which degrades and can interrupt direct links between the two.

### Verdict on Part Two B

Part Two B is partially supported.
For rocket probes,
including the solar Oberth manoeuvre,
no body considered here is a poorer starting point than Mercury.
For sail and beamed probes,
the region near Mercury's orbit is the best,
and Mercury is the only known body in that region that can supply mass.
Repeated passes do not change this,
since the speed they reach depends on the sail and its perihelion rather than on its starting orbit,
but a sunlight-powered mass driver on Mercury is the cheapest way found here to put a sail into a dive.
A base there is therefore plausibly the most beneficial site for those methods.
The benefit comes from the distance and from Mercury's materials together,
and it would be shared by any large orbital industry at the same distance.

## Location Rather Than Substance

### What Belongs to the Distance

The broader form of the hypothesis can be tested by sorting each property by its cause.
The properties that come from Mercury's distance from the Sun are the sunlight,
the sail release speed,
the collector area for beamed power,
the collector time for a mass driver,
the short year that brings frequent launch windows,
and the short trips toward Venus and the Sun.
The penalties also come from the distance,
including the deep gravity well,
the extra solar energetic particles,
the heat
and the communication geometry.
The properties that come from Mercury itself are its ice,
its low escape speed,
its lack of air,
its iron-rich core,
its slow rotation
and its solid ground.

Every launch advantage found in this article is in the first list.
The second list supplies the platform,
meaning a place to stand,
material to build with
and an airless surface for a mass driver.
Any solid,
airless body at the same distance would serve nearly as well,
so the broader claim is supported for Mercury.
Its value as a launch site lies mostly in where it is,
and its own properties matter chiefly because it is the only body there to stand on.

### The Innermost Body of Other Stars

The same physics applies around any star of luminosity $L$ and mass $M$,
written here in solar units.
A sail with a given loading has a lightness number in proportion to $L/M$,
because the light scales with $L$ and the gravity with $M$.
If the sail can tolerate a maximum flux $F_{\max}$,
its closest perihelion is $q = \sqrt{L/(4\pi F_{\max})}$,
and the ceiling speed from the previous section becomes the following,
where $\sigma_{s}$ is the sail's mass per unit area.

$$
v_{\mathrm{ceiling}}^{2} = \frac{2\beta G M}{q} = \frac{2}{c\,\sigma_{s}}\sqrt{\frac{F_{\max}\,L}{\pi}}
$$

The stellar mass cancels,
so for the same sail and the same heat limit the ceiling scales as $L^{1/4}$.
The rocket penalty scales with the orbital speed $\sqrt{GM/r}$,
and the mass driver collector time scales as $M r/L$.

Two nearby systems test the general claim.
Proxima Centauri has a mass of 0.1221 and a luminosity of 0.001567 in solar units
[Proxima Centauri][ref_proxima_centauri],
and its innermost known planet,
Proxima d,
was found orbiting at about 0.029 AU with a minimum mass of 0.26 Earth masses
[Faria et al. 2022][research_faria_et_al_2022],
a value its confirmation refined to 0.260 ± 0.038
[Suárez Mascareño et al. 2025][research_suarez_mascareno_et_al_2025].
The calculations use the catalogued semi-major axis of 0.02881 AU
[Proxima Centauri d][ref_proxima_centauri_d].
TRAPPIST-1 has a mass of 0.0898
[TRAPPIST-1][ref_trappist_1]
and a luminosity of $5.66 \times 10^{-4}$
[Davoudi et al. 2024][research_davoudi_et_al_2024],
and its innermost planet,
TRAPPIST-1b,
orbits at 0.01154 AU
[TRAPPIST-1b][ref_trappist_1b].
The table compares them with Mercury,
using a sail that has $\beta = 1$ around the Sun
and a heat limit equal to the flux at 10 solar radii from the Sun.

<div style="overflow-x: auto;" markdown="1">

| Innermost body | Sunlight relative to Earth | Orbital speed, km/s | Rocket delta-v to escape the star, km/s | Sail $\beta$ | Sail ceiling, km/s | $M r/L$ relative to Earth's orbit |
|---|---|---|---|---|---|---|
| Mercury | 6.67 | 47.87 | 19.83 | 1.0 | 195.3 | 0.387 |
| Proxima d | 1.89 | 61.32 | 25.40 | 0.0128 | 38.9 | 2.245 |
| TRAPPIST-1b | 4.25 | 83.09 | 34.42 | 0.0063 | 30.1 | 1.831 |

</div>

The thermally limited perihelia are 0.00184 AU around Proxima Centauri and 0.00111 AU around TRAPPIST-1,
about 2.6 and 2.0 times the radius of each star,
so the dives are geometrically possible.
Around both red dwarfs the innermost body is a poorer launch site than Mercury on every measure.
Its rocket penalty is deeper,
its sails are about 80 and 160 times weaker,
the sail ceiling is a fifth to a sixth of the solar value,
and the collector time for a mass driver is about 5.8 and 4.7 times longer.

Within each of those systems,
however,
the same scaling holds,
since the collector time is in proportion to $r$ and the sunlight to $1/r^{2}$.
The innermost body is still the cheapest place in its own system to launch with sunlight.
Close-in planets add one advantage that Mercury lacks.
TRAPPIST-1b is likely tidally locked to its star
[TRAPPIST-1b][ref_trappist_1b],
and a track fixed to a tidally locked planet keeps a fixed heading relative to its orbital motion,
as the companion article on mass drivers shows for synchronous moons
[Mass Drivers, Release Geometry on a Tidally Locked Body][related_post_mass_drivers_locked],
so it would be permanently aligned for prograde launches.
That is an inference from the geometry,
and it removes the alignment problem found above for Mercury.

Two limits apply to the general claim.
The innermost known planet of a star can be a gas giant with no surface,
as with 51 Pegasi b,
the Jupiter-mass companion of a solar-type star
[Mayor and Queloz 1995][research_mayor_queloz_1995]
and the prototype of the hot Jupiters
[51 Pegasi b][ref_51_pegasi_b].
Red dwarfs also flare.
In March 2016 a superflare from Proxima Centauri raised its optical flux by a factor of about 68
[Howard et al. 2018][research_howard_et_al_2018],
which a settlement on Proxima d would have to withstand.
The generalized claim is therefore supported within any one system for launch powered by starlight,
on the condition that the innermost body is solid,
but the size of the advantage depends strongly on the star,
and the claim says nothing in favour of rockets anywhere.

## Other Advantages and Disadvantages of a Mercury Base

In a future in which every body can be settled,
Mercury competes with the others on a list of physical properties.
The advantages follow.

- The densest sunlight available on a solid body, 6.25 to 14.4 kilowatts per square metre over an orbit.
- Water ice in permanently shadowed polar craters, confirmed by several independent measurements.
- A large iron-rich core, with a model of a solid crust and mantle over a solid iron-sulfide layer and an iron-rich liquid outer core [Smith et al. 2012][research_smith_et_al_2012]. The top of the liquid core lies at a radius of 2,020 ± 30 kilometres [Hauck et al. 2013][research_hauck_et_al_2013], so with a mean radius of 2,439.36 kilometres [Perry et al. 2015][research_perry_et_al_2015] the liquid core and everything inside it occupy about 57 percent of the planet's volume, and geodetic data indicate a solid inner core [Genova et al. 2019][research_genova_et_al_2019]. The top of the liquid core therefore lies about 420 kilometres down, far below any plausible mine, and the surface itself is low in iron and at least ten times richer in sulfur than the silicate Earth or Moon [Nittler et al. 2011][research_nittler_et_al_2011], so the iron-rich core is not by itself an accessible resource.
- An escape speed of 4.25 kilometres per second with no atmosphere, which allows mass drivers.
- The lowest sunlight-collection cost per kilogram among the bodies compared for mass-driver launches that escape the Sun or dive toward it.
- Launch windows to the outer planets about every three months.
- A slow terminator that moves at walking pace, allowing mobile settlements to stay in moderate conditions.
- Surface gravity nearly equal to that of Mars.
- Proximity to the Sun for solar science, sail staging and beamed power.

The disadvantages follow.

- The highest delta-v of any landable body to reach from Earth, and the highest delta-v to leave the solar system from the surface among the bodies compared.
- No atmosphere for aerobraking, so every arrival is propulsive.
- Surface temperatures from −173 °C to 427 °C at the equator, and radiators that must reject waste heat against a hot environment by day.
- Nights of about 88 Earth days at any fixed point away from the poles, which require storage, polar siting or mobility to keep power continuous.
- A higher flux of solar energetic particles, by a factor of roughly 2.6 to 13 relative to Earth's distance depending on the measure.
- A weak magnetic field and no atmosphere to shield the surface.
- A home that always appears near the Sun from the outer solar system, and regular conjunctions that degrade links with Earth.
- A slow rotation that brings a fixed launch track into line with a given departure direction only about once every 176 days.
- Waste heat rejection that is hardest exactly where the sunlight is strongest, which limits how much of the abundant power can be used. Two-sided flat panels absorbing 90 percent of the light and emitting with an emissivity of 0.85 reach 569 K at perihelion in this simple model, against 315 K at 1 AU.

The panel temperature in the last item balances absorbed sunlight,
less the fraction $\eta$ converted to electricity,
against emission from both faces,
with absorptance $\alpha_{p}$ and emissivity $\varepsilon_{p}$.

$$
T_{\mathrm{panel}} = \left[\frac{\left(\alpha_{p} - \eta\right) S}{2\,\varepsilon_{p}\,\sigma}\right]^{1/4}
$$

MESSENGER met this problem by interleaving its solar cells with optical solar reflector mirrors at one cell to two mirrors,
to reduce the panels' absorbance,
and by tilting the panels away from the Sun as the light grew stronger
[Dakermanji et al. 2006][research_dakermanji_jenkins_ercol_2006].
Its high-temperature technologies spanned the telecommunications,
power,
guidance and control,
and thermal control subsystems
[Ercol 2007][research_ercol_2007],
and BepiColombo's multilayer insulation was described as a design at the edge of material capability
[Moser et al. 2010][research_moser_et_al_2010].

## Verdict on the Hypothesis

<div style="overflow-x: auto;" markdown="1">

| Claim | Verdict | Deciding physics |
|---|---|---|
| Part one, Mercury is the hardest body to colonize | Refuted as stated, supported for reaching landable bodies | Venus's surface, Io, the giant planets and the Sun are harder, while Mercury has the highest LEO-to-surface delta-v among landable bodies |
| Part two A, the best base for probes within the solar system | Refuted for outward rockets, supported for sunlight-powered mass drivers and for Venus and the Sun | The Sun's gravity well raises every outward delta-v, while the sunlight needed per kilogram falls in proportion to distance, windows are frequent and inward targets are close |
| Part two B, the best base for probes to other stars | Partially supported | Rockets and the solar Oberth manoeuvre favour distant origins, while sails and beamed power favour the region near Mercury, and repeated passes depend on the sail rather than the starting orbit |
| Broader form, value from location rather than substance | Supported for Mercury | Every launch advantage found is a function of distance, and Mercury supplies the only platform at that distance |
| Broader form, the innermost body of any star | Supported within each system for launch powered by starlight, conditionally | Collector time scales as $M r/L$, but sail performance scales as $L^{1/4}$, rockets are always penalized, and the innermost body may have no surface |

</div>

## A Review of the Literature

The literature relevant to a Mercury base falls into two bodies of work that rarely cite each other.
One is the planetary science of Mercury from MESSENGER and BepiColombo,
and the other is the study of fast and interstellar missions that use the Sun's proximity.
This section surveys both by topic.
Each work is described according to its published abstract,
or by its subject alone where it is cited for its title.

### Missions to Mercury

MESSENGER's mission is described by Solomon and coauthors
[Solomon et al. 2007][research_solomon_et_al_2007],
and its trajectory and navigation by McAdams and coauthors
[McAdams et al. 2006][research_mcadams_et_al_2006]
[McAdams et al. 2007][research_mcadams_et_al_2007].
BepiColombo's goals were set out in 2010
[Benkhoff et al. 2010][research_benkhoff_et_al_2010]
and its mission overview,
including the global characterization of the interior,
surface,
exosphere
and magnetosphere,
in 2021
[Benkhoff et al. 2021][research_benkhoff_et_al_2021].

### Polar Volatiles

Full-disk radar mapping in 1991 revealed reflective polar material
[Slade et al. 1992][research_slade_butler_muhleman_1992],
thermal models addressed near-surface temperatures and the stability of polar ice
[Vasavada et al. 1999][research_vasavada_paige_wood_1999],
and MESSENGER neutron data and thermal modeling confirmed water ice at the north pole,
with laser altimeter reflectance consistent with exposed and buried ice
[Lawrence et al. 2013][research_lawrence_et_al_2013]
[Neumann et al. 2013][research_neumann_et_al_2013]
[Paige et al. 2013][research_paige_et_al_2013].
Chabot and coauthors tied the radar-bright deposits to persistent shadow
[Chabot et al. 2013][research_chabot_et_al_2013]
and imaged them directly
[Chabot et al. 2014][research_chabot_et_al_2014],
and Deutsch and coauthors constrained their thickness
[Deutsch et al. 2018][research_deutsch_et_al_2018].

### Composition, Volatiles and Interior

Nittler and coauthors found a surface that rules out a lunar-like feldspar-rich crust,
with sulfur at least ten times the level in Earth's silicates and low iron,
pointing to highly reduced precursor materials
[Nittler et al. 2011][research_nittler_et_al_2011],
and later mapped the major elements globally
[Nittler et al. 2020][research_nittler_et_al_2020].
Peplowski and coauthors measured potassium at 1,150 ± 220 parts per million,
thorium at 220 ± 60 parts per billion
and uranium at 90 ± 20 parts per billion,
consistent with formation from volatile-bearing material like chondritic meteorites
[Peplowski et al. 2011][research_peplowski_et_al_2011].
Blewett and coauthors found hollows from tens of metres to a few kilometres across,
attributed to recent loss of volatiles
[Blewett et al. 2011][research_blewett_et_al_2011].
Domingue and coauthors reviewed space weathering,
finding that the processes that weather the surface are the same as those that form the exosphere,
and that impacts produce more than an order of magnitude more melt and vapour than on the Moon
[Domingue et al. 2014][research_domingue_et_al_2014].
The interior is constrained by gravity and spin
[Smith et al. 2012][research_smith_et_al_2012]
[Margot et al. 2012][research_margot_et_al_2012],
by the structure models of Hauck and coauthors
[Hauck et al. 2013][research_hauck_et_al_2013],
and by geodetic evidence for a solid inner core from a normalized polar moment of inertia of 0.333 ± 0.005
[Genova et al. 2019][research_genova_et_al_2019].

### The Space Environment

The magnetic field
[Anderson et al. 2011][research_anderson_et_al_2011],
reconnection in the magnetosphere
[Slavin et al. 2009][research_slavin_et_al_2009],
energetic electron bursts
[Ho et al. 2011][research_ho_et_al_2011]
and the entry of solar energetic electrons
[Gershman et al. 2015][research_gershman_et_al_2015]
describe the magnetic and energetic particle environment near the planet.
The radial scaling of solar energetic proton events comes from Helios and IMP 8
[Lario et al. 2006][research_lario_et_al_2006],
and coronal mass ejections inside 0.5 AU from MESSENGER
[Winslow et al. 2015][research_winslow_et_al_2015].
The exosphere is reviewed by Killen and coauthors
[Killen et al. 2007][research_killen_et_al_2007],
and its seasonal sodium component was observed from orbit
[Cassidy et al. 2015][research_cassidy_et_al_2015].

### Engineering for the Inner Solar System

MESSENGER's solar arrays
[Dakermanji et al. 2006][research_dakermanji_jenkins_ercol_2006]
and its other high-temperature technologies
[Ercol 2007][research_ercol_2007],
BepiColombo's insulation
[Moser et al. 2010][research_moser_et_al_2010],
the Parker Solar Probe
[Fox et al. 2015][research_fox_et_al_2015],
and a combined heat shield and solar thermal engine for an Oberth manoeuvre
[Benkoski et al. 2023][research_benkoski_et_al_2023]
show how hardware survives near the Sun.
Launch of lunar ice by an electromagnetic accelerator has been studied
[Beemer and McNab 2023][research_beemer_mcnab_2023].

### Settlement and Resources

Palaszewski analysed human and robotic missions to Mercury,
including landers whose chemical propulsion is enhanced by in-situ resources
[Palaszewski 2015][research_palaszewski_2015].
The settlement analysis in this article rests on the physics derived here
and not on a cited study of settling Mercury.
The search for vulcanoids
[Evans and Tabachnik 1999][research_evans_tabachnik_1999]
[Steffl et al. 2013][research_steffl_et_al_2013]
bears on whether Mercury is the only source of material near the Sun.

### Fast and Interstellar Missions from near the Sun

McNutt and coauthors made the case for a near-term interstellar probe
[McNutt et al. 2019][research_mcnutt_et_al_2019],
and Schlei and coauthors found escape speeds above 8 AU per year with a Jupiter flyby,
for a journey of about 120 AU to the interstellar medium
[Schlei et al. 2021][research_schlei_et_al_2021].
Close-perihelion alternatives include solar thermal propulsion
[Lyman et al. 2001][research_lyman_et_al_2001],
the Project Lyra studies
[Hein et al. 2019][research_hein_et_al_2019]
[Hibberd et al. 2022][research_hibberd_et_al_2022],
the sun diver that combines a sail with a dive
[Bailer-Jones 2021][research_bailer_jones_2021],
a beamed sun-diver
[Benford and Benford 2003][research_benford_benford_2003],
and the solar sail heliopause probe
[Lappas et al. 2005][research_lappas_et_al_2005]
[Lyngvi et al. 2005][research_lyngvi_et_al_2005].
Directed-energy propulsion
[Kulkarni et al. 2018][research_kulkarni_lubin_zhang_2018]
[Parkin 2018][research_parkin_2018]
is treated in the companion article on solar sailing.
None of these studies proposes Mercury as a base according to its abstract or title,
and the connection made in this article between them and Mercury is its own inference.

## Epistemic State

**Facts reported by the cited sources.**
Physical data for the bodies,
including Mercury's orbital period,
temperature range,
gravity,
escape speed,
magnetic field strength
and exospheric pressure,
come from the Wikipedia entries cited,
which draw on fact sheets of the National Aeronautics and Space Administration and on the peer-reviewed literature.
Mercury's rotation period and spin-orbit resonance come from the group led by Mazarico,
and its core fraction is computed here from the core radius of the group led by Hauck and the mean radius of the group led by Perry.
The masses,
luminosities
and orbits of Proxima Centauri,
TRAPPIST-1
and their innermost planets come from Wikipedia in the same way,
except that the minimum mass of Proxima d comes from the groups led by Faria and Suárez Mascareño
and the luminosity of TRAPPIST-1 from the group led by Davoudi.
The findings attributed to Kopp and Lean,
to Schumacher and Gay
and to the groups led by Slade,
Margot,
Anderson,
Smith,
Lario,
Mazarico,
Perry,
Mangano,
Ness,
Fox,
Hoang,
Worden,
Faria,
Suárez Mascareño,
Davoudi
and Howard
are stated according to their published abstracts.
The arrival date of BepiColombo,
the perihelion of the Parker Solar Probe
and the date it was first reached rest on the conference papers and abstracts of Murakami and Jones,
Ercol and Balakrishnan,
and Badman,
which are not peer-reviewed articles.
The looser upper limit on Mercury's exospheric pressure rests on the conference abstract of the group led by Lammer,
which is likewise not peer-reviewed.
The work of Mayor and Queloz is cited only for its title.
For the three 2013 polar ice papers the findings stated are those of the journal's shared editorial summary,
which states the joint conclusion rather than each paper's separate result.
The findings of the works in the literature review are stated according to their abstracts where the text states them,
for the groups led by Chabot,
Nittler 2011,
Peplowski,
Blewett,
Domingue,
Hauck,
Genova,
Ho,
Gershman,
Winslow,
Benkhoff 2021,
Dakermanji,
Ercol,
McNutt,
Schlei,
Lappas,
Lyman
and Kulkarni,
and of Bailer-Jones and Palaszewski,
with Lyman and coauthors cited only for the engine and perihelion stated in their abstract.
The work of Slavin and coauthors is cited only for its title,
because its published summary is an editor's note rather than the authors' abstract.
The paper of Vasavada, Paige and Wood,
the papers of the groups led by Solomon,
Benkhoff 2010
and Benkoski,
the paper of Beemer and McNab,
the book by McInnes,
and every other work in the literature review,
are cited only for what their titles state.
The conversion of 8 AU per year to about 38 kilometres per second is computed here.
The findings attributed to sources rest on their abstracts and titles rather than on their full texts.

**Analysis in this article.**
Every delta-v,
flight time,
synodic period,
mass ratio,
track length,
drag fraction,
sail speed,
collector area
and angle is computed here from the formulas shown.
The orbital model assumes circular coplanar orbits,
patched conics,
Hohmann transfers
and impulsive burns,
and these assumptions misstate Mercury's eccentric orbit and ignore the gravity assists that real missions use.
The drag model ignores gravity during the atmospheric passage,
ablation
and the variation of gravity with height,
which matters for Titan's deep atmosphere.
The repeated-pass results come from a planar simulation of an ideal flat sail under one simple control law.
They are not optimized,
they exclude the cost of entering the dive,
and they ignore heating,
sail degradation
and the solar wind.
The mass driver figures ignore launcher losses,
night
and storage.
The 450 and 900 second specific impulses,
the use of the 100 gigawatt laser output as an electrical load,
the panel properties
and the projectile's ballistic coefficient are illustrative assumptions.

**Inference and judgment.**
The verdicts depend on reading the hypothesis in a particular way.
"Hardest to colonize" is split here into reaching and inhabiting,
and "most beneficial" is judged by delta-v,
launch frequency
and access to sunlight-driven propulsion.
A different weighting,
for example one dominated by the cost of energy,
would move the verdict on Part Two A toward support.
The proposal of a mobile settlement following the terminator is an inference from the terminator speed and has not been evaluated.
The judgment that Mercury's iron-rich core is not an accessible resource is an inference from its depth,
computed here as the planet's radius less the core radius,
and from the low surface iron.
The alignment limit on a fixed launch track and the permanent alignment on a tidally locked planet are inferences from geometry.
The sorting of properties into those of distance and those of the body is a judgment,
and the polar ice in particular depends on both,
since it needs Mercury's small axial tilt and its distance from the Sun together.

**Unaddressed concerns.**
This article does not model the long-term effects of 0.38 of Earth's gravity on people,
the chemistry of Mercury's regolith as a feedstock,
the engineering of radiators or shielding,
or the economics of any base.
The solar energetic particle factors are ensemble averages and do not bound the worst event.

## Out of Scope

This article does not treat the colonization of bodies outside the solar system beyond the launch physics of their innermost planets,
the politics or law of settlement,
or the biology of the polar ice deposits.
It does not compare propulsion technologies beyond the physics needed for each verdict,
and it does not address fusion or antimatter propulsion,
for which the launch site makes little difference.

## Conclusion

The two-part hypothesis contains one claim that is mostly false and one that is true only for particular kinds of probe.
Mercury is not the hardest body to colonize,
because Venus's surface,
Io
and the giant planets are worse.
It is,
by the arithmetic here,
the most expensive landable body to reach from Earth by propulsion,
and once reached it offers ice,
power,
Mars-like gravity
and a slow day.

As a launch site,
Mercury pays for its sunlight with the depth of the Sun's gravity well.
For rockets aimed outward,
that depth makes it the worst origin among the bodies compared,
whether the destination is Jupiter or another star.
For probes sent toward the Sun,
for frequent launch windows,
and for sails and beamed propulsion,
the region near Mercury is the best,
and Mercury alone among known bodies there can supply mass.
Mass drivers powered by sunlight also favour Mercury,
because the sunlight needed per kilogram falls in proportion to distance from the Sun,
even though the speeds required rise.
Repeated passes near the Sun open the sun-diving strategy to weaker sails,
but they reward the sail and its perihelion rather than its starting orbit.
A future civilization would plausibly build its sail yards,
laser arrays
and mass drivers near Mercury
and its rocket ports far from the Sun,
which is a division of labour rather than a single best base.

The broader claim,
that Mercury's value lies in where it is rather than in what it is,
holds for every launch advantage found here.
It extends to the innermost solid body of any star,
which is the cheapest place in its own system to launch with starlight.
Around a red dwarf such as Proxima Centauri,
however,
that advantage is several times smaller than Mercury's,
and around a star whose innermost planet is a gas giant there is no surface to build on.
Self-replicating probes of the kind discussed in an earlier article on this site
[Von Neumann Probes][related_post_von_neumann_probes]
would face the same choice of origin.

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Beemer, Heidi D., and Ian R. McNab. 2023. "Launch Parameters of a Lunar Ice Payload Traveling via Electromagnetic Mass Accelerator." *Acta Astronautica* 207: 24–32. [https://doi.org/10.1016/j.actaastro.2023.02.041][research_beemer_mcnab_2023]
- Benkhoff, Johannes, Jan van Casteren, Hajime Hayakawa, et al. 2010. "BepiColombo—Comprehensive Exploration of Mercury: Mission Overview and Science Goals." *Planetary and Space Science* 58 (1–2): 2–20. [https://doi.org/10.1016/j.pss.2009.09.020][research_benkhoff_et_al_2010]
- Benkoski, Jason J., W. Lloyd Luedeman, Narendra N. De, et al. 2023. "Combined Heat Shield and Solar Thermal Propulsion System for an Oberth Maneuver." *Journal of Propulsion and Power* 39 (2): 284–93. [https://doi.org/10.2514/1.b38595][research_benkoski_et_al_2023]
- Cassidy, Timothy A., Aimee W. Merkel, Matthew H. Burger, et al. 2015. "Mercury’s Seasonal Sodium Exosphere: MESSENGER Orbital Observations." *Icarus* 248: 547–59. [https://doi.org/10.1016/j.icarus.2014.10.037][research_cassidy_et_al_2015]
- Chabot, Nancy L., Carolyn M. Ernst, Brett W. Denevi, et al. 2014. "Images of Surface Volatiles in Mercury’s Polar Craters Acquired by the MESSENGER Spacecraft." *Geology* 42 (12): 1051–54. [https://doi.org/10.1130/g35916.1][research_chabot_et_al_2014]
- Chabot, Nancy L., Carolyn M. Ernst, John K. Harmon, et al. 2013. "Craters Hosting Radar-Bright Deposits in Mercury's North Polar Region: Areas of Persistent Shadow Determined from MESSENGER Images." *Journal of Geophysical Research: Planets* 118 (1): 26–36. [https://doi.org/10.1029/2012je004172][research_chabot_et_al_2013]
- Davoudi, Fatemeh, Benjamin V. Rackham, Michaël Gillon, et al. 2024. "Updated Spectral Characteristics for the Ultracool Dwarf TRAPPIST-1." *Astrophysical Journal Letters* 970 (1): L4. [https://doi.org/10.3847/2041-8213/ad5c6c][research_davoudi_et_al_2024]
- Deutsch, Ariel N., James W. Head, Nancy L. Chabot, and Gregory A. Neumann. 2018. "Constraining the Thickness of Polar Ice Deposits on Mercury Using the Mercury Laser Altimeter and Small Craters in Permanently Shadowed Regions." *Icarus* 305: 139–48. [https://doi.org/10.1016/j.icarus.2018.01.013][research_deutsch_et_al_2018]
- Evans, N. Wyn, and Serge Tabachnik. 1999. "Possible Long-Lived Asteroid Belts in the Inner Solar System." *Nature* 399 (6731): 41–43. [https://doi.org/10.1038/19919][research_evans_tabachnik_1999]
- Genova, Antonio, Sander Goossens, Erwan Mazarico, et al. 2019. "Geodetic Evidence That Mercury Has a Solid Inner Core." *Geophysical Research Letters* 46 (7): 3625–33. [https://doi.org/10.1029/2018gl081135][research_genova_et_al_2019]
- Gershman, Daniel J., Jim M. Raines, James A. Slavin, et al. 2015. "MESSENGER Observations of Solar Energetic Electrons within Mercury's Magnetosphere." *Journal of Geophysical Research: Space Physics* 120 (10): 8559–71. [https://doi.org/10.1002/2015ja021610][research_gershman_et_al_2015]
- Hauck, Steven A., Jean-Luc Margot, Sean C. Solomon, et al. 2013. "The Curious Case of Mercury's Internal Structure." *Journal of Geophysical Research: Planets* 118 (6): 1204–20. [https://doi.org/10.1002/jgre.20091][research_hauck_et_al_2013]
- Hein, Andreas M., Nikolaos Perakis, T. Marshall Eubanks, et al. 2019. "Project Lyra: Sending a Spacecraft to 1I/’Oumuamua (Former A/2017 U1), the Interstellar Asteroid." *Acta Astronautica* 161: 552–61. [https://doi.org/10.1016/j.actaastro.2018.12.042][research_hein_et_al_2019]
- Hibberd, Adam, Andreas M. Hein, T. Marshall Eubanks, and Robert G. Kennedy. 2022. "Project Lyra: A Mission to 1I/’Oumuamua without Solar Oberth Manoeuvre." *Acta Astronautica* 199: 161–65. [https://doi.org/10.1016/j.actaastro.2022.07.032][research_hibberd_et_al_2022]
- Hoang, Thiem, A. Lazarian, Blakesley Burkhart, and Abraham Loeb. 2017. "The Interaction of Relativistic Spacecrafts with the Interstellar Medium." *Astrophysical Journal* 837 (1): 5. [https://doi.org/10.3847/1538-4357/aa5da6][research_hoang_et_al_2017]
- Howard, Ward S., Matt A. Tilley, Hank Corbett, et al. 2018. "The First Naked-Eye Superflare Detected from Proxima Centauri." *Astrophysical Journal Letters* 860 (2): L30. [https://doi.org/10.3847/2041-8213/aacaf3][research_howard_et_al_2018]
- Kopp, Greg, and Judith L. Lean. 2011. "A New, Lower Value of Total Solar Irradiance: Evidence and Climate Significance." *Geophysical Research Letters* 38 (1): L01706. [https://doi.org/10.1029/2010gl045777][research_kopp_lean_2011]
- Kulkarni, Neeraj, Philip Lubin, and Qicheng Zhang. 2018. "Relativistic Spacecraft Propelled by Directed Energy." *Astronomical Journal* 155 (4): 155. [https://doi.org/10.3847/1538-3881/aaafd2][research_kulkarni_lubin_zhang_2018]
- Lario, D., M.-B. Kallenrode, R. B. Decker, et al. 2006. "Radial and Longitudinal Dependence of Solar 4–13 MeV and 27–37 MeV Proton Peak Intensities and Fluences: Helios and IMP 8 Observations." *Astrophysical Journal* 653 (2): 1531–44. [https://doi.org/10.1086/508982][research_lario_et_al_2006]
- Lyngvi, A., P. Falkner, S. Kemble, M. Leipold, and A. Peacock. 2005. "The Interstellar Heliopause Probe." *Acta Astronautica* 57 (2–8): 104–11. [https://doi.org/10.1016/j.actaastro.2005.03.042][research_lyngvi_et_al_2005]
- Margot, Jean-Luc, Stanton J. Peale, Sean C. Solomon, et al. 2012. "Mercury's Moment of Inertia from Spin and Gravity Data." *Journal of Geophysical Research: Planets* 117 (E12): 2012JE004161. [https://doi.org/10.1029/2012je004161][research_margot_et_al_2012]
- Mayor, Michel, and Didier Queloz. 1995. "A Jupiter-Mass Companion to a Solar-Type Star." *Nature* 378 (6555): 355–59. [https://doi.org/10.1038/378355a0][research_mayor_queloz_1995]
- Mazarico, Erwan, Antonio Genova, Sander Goossens, et al. 2014. "The Gravity Field, Orientation, and Ephemeris of Mercury from MESSENGER Observations after Three Years in Orbit." *Journal of Geophysical Research: Planets* 119 (12): 2417–36. [https://doi.org/10.1002/2014je004675][research_mazarico_et_al_2014]
- McAdams, James V., David W. Dunham, Robert W. Farquhar, Anthony H. Taylor, and B. G. Williams. 2006. "Trajectory Design and Maneuver Strategy for the MESSENGER Mission to Mercury." *Journal of Spacecraft and Rockets* 43 (5): 1054–64. [https://doi.org/10.2514/1.18178][research_mcadams_et_al_2006]
- McNutt, Ralph L., Robert F. Wimmer-Schweingruber, Mike Gruntman, et al. 2019. "Near-Term Interstellar Probe: First Step." *Acta Astronautica* 162: 284–99. [https://doi.org/10.1016/j.actaastro.2019.06.013][research_mcnutt_et_al_2019]
- Nittler, Larry R., Elizabeth A. Frank, Shoshana Z. Weider, et al. 2020. "Global Major-Element Maps of Mercury from Four Years of MESSENGER X-Ray Spectrometer Observations." *Icarus* 345: 113716. [https://doi.org/10.1016/j.icarus.2020.113716][research_nittler_et_al_2020]
- Parkin, Kevin L. G. 2018. "The Breakthrough Starshot System Model." *Acta Astronautica* 152: 370–84. [https://doi.org/10.1016/j.actaastro.2018.08.035][research_parkin_2018]
- Perry, Mark E., Gregory A. Neumann, Roger J. Phillips, et al. 2015. "The Low-Degree Shape of Mercury." *Geophysical Research Letters* 42 (17): 6951–58. [https://doi.org/10.1002/2015gl065101][research_perry_et_al_2015]
- Steffl, A. J., N. J. Cunningham, A. B. Shinn, D. D. Durda, and S. A. Stern. 2013. "A Search for Vulcanoids with the STEREO Heliospheric Imager." *Icarus* 223 (1): 48–56. [https://doi.org/10.1016/j.icarus.2012.11.031][research_steffl_et_al_2013]
- Vasavada, Ashwin R., David A. Paige, and Stephen E. Wood. 1999. "Near-Surface Temperatures on Mercury and the Moon and the Stability of Polar Ice Deposits." *Icarus* 141 (2): 179–93. [https://doi.org/10.1006/icar.1999.6175][research_vasavada_paige_wood_1999]
- Winslow, Reka M., Noé Lugaz, Lydia C. Philpott, et al. 2015. "Interplanetary Coronal Mass Ejections from MESSENGER Orbital Observations at Mercury." *Journal of Geophysical Research: Space Physics* 120 (8): 6101–18. [https://doi.org/10.1002/2015ja021200][research_winslow_et_al_2015]
- Worden, S. Pete, Wesley A. Green, James Schalkwyk, Kevin Parkin, and Robert Q. Fugate. 2021. "Progress on the Starshot Laser Propulsion System." *Applied Optics* 60 (31): H20. [https://doi.org/10.1364/ao.435858][research_worden_et_al_2021]

### Primary Sources, Non-Peer-Reviewed

- Anderson, Brian J., Catherine L. Johnson, Haje Korth, et al. 2011. "The Global Magnetic Field of Mercury from MESSENGER Orbital Observations." *Science* 333 (6051): 1859–62. [https://doi.org/10.1126/science.1211001][research_anderson_et_al_2011]
- Badman, Samuel. 2026. "The Outer Reaches of the Solar Corona as Measured by Parker Solar Probe." Abstract EGU26-12552, *EGU General Assembly 2026*. Copernicus GmbH. [https://doi.org/10.5194/egusphere-egu26-12552][research_badman_2026]
- Bailer-Jones, Coryn A. L. 2021. "The Sun Diver: Combining Solar Sails with the Oberth Effect." *American Journal of Physics* 89 (3): 235–43. [https://doi.org/10.1119/10.0002178][research_bailer_jones_2021]
- Benford, James, and Gregory Benford. 2003. "Near-Term Beamed Sail Propulsion Missions: Cosmos-1 and Sun-Diver." In *Beamed Energy Propulsion: First International Symposium on Beamed Energy Propulsion*. AIP Conference Proceedings 664. AIP. [https://doi.org/10.1063/1.1582124][research_benford_benford_2003]
- Benkhoff, J., G. Murakami, W. Baumjohann, et al. 2021. "BepiColombo: Mission Overview and Science Goals." *Space Science Reviews* 217 (8): 90. [https://doi.org/10.1007/s11214-021-00861-4][research_benkhoff_et_al_2021]
- Blewett, David T., Nancy L. Chabot, Brett W. Denevi, et al. 2011. "Hollows on Mercury: MESSENGER Evidence for Geologically Recent Volatile-Related Activity." *Science* 333 (6051): 1856–59. [https://doi.org/10.1126/science.1211681][research_blewett_et_al_2011]
- Dakermanji, G., J. Jenkins, and C. Ercol. 2006. "The MESSENGER Spacecraft Solar Array Design and Early Mission Performance." In *2006 IEEE 4th World Conference on Photovoltaic Energy Conference*. IEEE. [https://doi.org/10.1109/wcpec.2006.279872][research_dakermanji_jenkins_ercol_2006]
- Ercol, C. 2007. "MESSENGER Heritage: High Temperature Technologies for Inner Solar System Spacecraft." In *AIAA SPACE 2007 Conference & Exposition*. AIAA 2007-6188. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2007-6188][research_ercol_2007]
- Ercol, Carl, and Krithika Balakrishnan. 2024. "Thermal Performance of Parker Solar Probe through Orbit Eighteen." In *53rd International Conference on Environmental Systems*. International Conference on Environmental Systems. [https://doi.org/10.32865/2346/98763][research_ercol_balakrishnan_2024]
- Faria, J. P., A. Suárez Mascareño, P. Figueira, et al. 2022. "A Candidate Short-Period Sub-Earth Orbiting Proxima Centauri." *Astronomy & Astrophysics* 658: A115. [https://doi.org/10.1051/0004-6361/202142337][research_faria_et_al_2022]
- Fox, N. J., M. C. Velli, S. D. Bale, et al. 2015. "The Solar Probe Plus Mission: Humanity’s First Visit to Our Star." *Space Science Reviews* 204 (1–4): 7–48. [https://doi.org/10.1007/s11214-015-0211-6][research_fox_et_al_2015]
- Ho, George C., Stamatios M. Krimigis, Robert E. Gold, et al. 2011. "MESSENGER Observations of Transient Bursts of Energetic Electrons in Mercury’s Magnetosphere." *Science* 333 (6051): 1865–68. [https://doi.org/10.1126/science.1211141][research_ho_et_al_2011]
- Lammer, Helmut, Fabian Weichbold, Manuel Scherf, et al. 2026. "The Role of Meteoritic Delivery to Mercury’s Surface-Exosphere Environment." Abstract EGU26-18943, *EGU General Assembly 2026*. Copernicus GmbH. [https://doi.org/10.5194/egusphere-egu26-18943][research_lammer_et_al_2026]
- Lappas, Vaios, Manfred Leipold, Peter Falkner, H. Fichtner, and S. Kraft. 2005. "Interstellar Heliopause Probe: System Design of a Solar Sail Mission to 200 AU." In *AIAA Guidance, Navigation, and Control Conference and Exhibit*. AIAA 2005-6084. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2005-6084][research_lappas_et_al_2005]
- Lawrence, David J., William C. Feldman, John O. Goldsten, et al. 2013. "Evidence for Water Ice near Mercury’s North Pole from MESSENGER Neutron Spectrometer Measurements." *Science* 339 (6117): 292–96. [https://doi.org/10.1126/science.1229953][research_lawrence_et_al_2013]
- Lyman, Ronald, Mark Ewing, Ramesh Krishnan, Dean Lester, and Ralph McNutt Jr. 2001. "Solar Thermal Propulsion for an Interstellar Probe." In *37th Joint Propulsion Conference and Exhibit*. AIAA 2001-3377. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2001-3377][research_lyman_et_al_2001]
- Mangano, Valeria, Melinda Dósa, Markus Fränz, et al. 2021. "BepiColombo Science Investigations during Cruise and Flybys at the Earth, Venus and Mercury." *Space Science Reviews* 217 (1): 23. [https://doi.org/10.1007/s11214-021-00797-9][research_mangano_et_al_2021]
- McAdams, James V., Robert W. Farquhar, Anthony H. Taylor, and Bobby G. Williams. 2007. "MESSENGER Mission Design and Navigation." *Space Science Reviews* 131 (1–4): 219–46. [https://doi.org/10.1007/s11214-007-9162-x][research_mcadams_et_al_2007]
- Moser, Martin, Christian Ranzenberger, George Varewijck, et al. 2010. "High Temperature Multilayer Insulation for the BepiColombo Spacecraft: A Design at the Edge of Material Capability." In *40th International Conference on Environmental Systems*. AIAA 2010-6091. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2010-6091][research_moser_et_al_2010]
- Murakami, Go, and Geraint Jones. 2025. "Overview and Initial Results of BepiColombo Mercury Flybys." Abstract EGU25-18018, *EGU General Assembly 2025*. Copernicus GmbH. [https://doi.org/10.5194/egusphere-egu25-18018][research_murakami_jones_2025]
- Ness, N. F., K. W. Behannon, R. P. Lepping, Y. C. Whang, and K. H. Schatten. 1974. "Magnetic Field Observations near Mercury: Preliminary Results from Mariner 10." *Science* 185 (4146): 151–60. [https://doi.org/10.1126/science.185.4146.151][research_ness_et_al_1974]
- Neumann, Gregory A., John F. Cavanaugh, Xiaoli Sun, et al. 2013. "Bright and Dark Polar Deposits on Mercury: Evidence for Surface Volatiles." *Science* 339 (6117): 296–300. [https://doi.org/10.1126/science.1229764][research_neumann_et_al_2013]
- Nittler, Larry R., Richard D. Starr, Shoshana Z. Weider, et al. 2011. "The Major-Element Composition of Mercury’s Surface from MESSENGER X-Ray Spectrometry." *Science* 333 (6051): 1847–50. [https://doi.org/10.1126/science.1211567][research_nittler_et_al_2011]
- Paige, David A., Matthew A. Siegler, John K. Harmon, et al. 2013. "Thermal Stability of Volatiles in the North Polar Region of Mercury." *Science* 339 (6117): 300–303. [https://doi.org/10.1126/science.1231106][research_paige_et_al_2013]
- Palaszewski, Bryan A. 2015. "Solar System Exploration Augmented by in-Situ Resource Utilization: Human Mercury and Saturn Exploration." In *8th Symposium on Space Resource Utilization*. AIAA 2015-1654. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2015-1654][research_palaszewski_2015]
- Peplowski, Patrick N., Larry G. Evans, Steven A. Hauck, et al. 2011. "Radioactive Elements on Mercury’s Surface from MESSENGER: Implications for the Planet’s Formation and Evolution." *Science* 333 (6051): 1850–52. [https://doi.org/10.1126/science.1211576][research_peplowski_et_al_2011]
- Schlei, Wayne, Justin Atchison, Ricardo Gomez-Cano, Brian Lathrop, and Benjamin Villac. 2021. "Pragmatic Trajectory Options Applicable to an Interstellar Probe Mission." In *2021 IEEE Aerospace Conference (50100)*. IEEE. [https://doi.org/10.1109/aero50100.2021.9438398][research_schlei_et_al_2021]
- Schumacher, G., and J. Gay. 2001. "An Attempt to Detect Vulcanoids with SOHO/LASCO Images: I. Scale Relativity and Quantization of the Solar System." *Astronomy & Astrophysics* 368 (3): 1108–14. [https://doi.org/10.1051/0004-6361:20000356][research_schumacher_gay_2001]
- Slade, Martin A., Bryan J. Butler, and Duane O. Muhleman. 1992. "Mercury Radar Imaging: Evidence for Polar Ice." *Science* 258 (5082): 635–40. [https://doi.org/10.1126/science.258.5082.635][research_slade_butler_muhleman_1992]
- Slavin, James A., Mario H. Acuña, Brian J. Anderson, et al. 2009. "MESSENGER Observations of Magnetic Reconnection in Mercury’s Magnetosphere." *Science* 324 (5927): 606–10. [https://doi.org/10.1126/science.1172011][research_slavin_et_al_2009]
- Smith, David E., Maria T. Zuber, Roger J. Phillips, et al. 2012. "Gravity Field and Internal Structure of Mercury from MESSENGER." *Science* 336 (6078): 214–17. [https://doi.org/10.1126/science.1218809][research_smith_et_al_2012]
- Solomon, Sean C., Ralph L. McNutt, Robert E. Gold, and Deborah L. Domingue. 2007. "MESSENGER Mission Overview." In *The MESSENGER Mission to Mercury*. Springer New York. [https://doi.org/10.1007/978-0-387-77214-1\_1][research_solomon_et_al_2007]
- Suárez Mascareño, Alejandro, Étienne Artigau, Lucile Mignon, et al. 2025. "Diving into the Planetary System of Proxima with NIRPS: Breaking the Metre per Second Barrier in the Infrared." *Astronomy & Astrophysics* 700: A11. [https://doi.org/10.1051/0004-6361/202553728][research_suarez_mascareno_et_al_2025]

### Secondary Sources

- Domingue, Deborah L., Clark R. Chapman, Rosemary M. Killen, et al. 2014. "Mercury’s Weather-Beaten Surface: Understanding Mercury in the Context of Lunar and Asteroidal Space Weathering Studies." *Space Science Reviews* 181 (1–4): 121–214. [https://doi.org/10.1007/s11214-014-0039-5][research_domingue_et_al_2014]
- Killen, Rosemary, Gabrielle Cremonese, Helmut Lammer, et al. 2007. "Processes That Promote and Deplete the Exosphere of Mercury." *Space Science Reviews* 132 (2–4): 433–509. [https://doi.org/10.1007/s11214-007-9232-0][research_killen_et_al_2007]
- McInnes, Colin Robert. 1999. *Solar Sailing*. Springer London. [https://doi.org/10.1007/978-1-4471-3992-8][book_mcinnes_1999]

### Tertiary Sources

- "51 Pegasi b." 2026. Wikipedia. Last modified October 21, at 09:07 (UTC). [https://en.wikipedia.org/w/index.php?title=51\_Pegasi\_b&oldid=1381285269][ref_51_pegasi_b]
- "Breakthrough Starshot." 2026. Wikipedia. Last modified September 26, at 18:09 (UTC). [https://en.wikipedia.org/w/index.php?title=Breakthrough\_Starshot&oldid=1376867919][ref_breakthrough_starshot]
- "Ceres (Dwarf Planet)." 2026. Wikipedia. Last modified October 20, at 04:55 (UTC). [https://en.wikipedia.org/w/index.php?title=Ceres\_(dwarf\_planet)&oldid=1381128658][ref_ceres]
- "Delta-v Budget." 2026. Wikipedia. Last modified July 2, at 23:47 (UTC). [https://en.wikipedia.org/w/index.php?title=Delta-v\_budget&oldid=1362285519][ref_delta_v_budget]
- "Earth." 2026. Wikipedia. Last modified October 19, at 09:27 (UTC). [https://en.wikipedia.org/w/index.php?title=Earth&oldid=1380995505][ref_earth]
- "Gravity Assist." 2026. Wikipedia. Last modified October 4, at 03:20 (UTC). [https://en.wikipedia.org/w/index.php?title=Gravity\_assist&oldid=1378359042][ref_gravity_assist]
- "Hohmann Transfer Orbit." 2026. Wikipedia. Last modified October 20, at 08:46 (UTC). [https://en.wikipedia.org/w/index.php?title=Hohmann\_transfer\_orbit&oldid=1381150738][ref_hohmann_transfer_orbit]
- "Io (Moon)." 2026. Wikipedia. Last modified October 14, at 11:17 (UTC). [https://en.wikipedia.org/w/index.php?title=Io\_(moon)&oldid=1380203631][ref_io]
- "Lunar Month." 2026. Wikipedia. Last modified October 1, at 22:44 (UTC). [https://en.wikipedia.org/w/index.php?title=Lunar\_month&oldid=1377910813][ref_lunar_month]
- "Mars." 2026. Wikipedia. Last modified October 10, at 09:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Mars&oldid=1379497097][ref_mars]
- "Mass Driver." 2026. Wikipedia. Last modified September 25, at 09:59 (UTC). [https://en.wikipedia.org/w/index.php?title=Mass\_driver&oldid=1376635859][ref_mass_driver]
- "Mercury (Planet)." 2026. Wikipedia. Last modified October 19, at 23:34 (UTC). [https://en.wikipedia.org/w/index.php?title=Mercury\_(planet)&oldid=1381089194][ref_mercury]
- "MESSENGER." 2026. Wikipedia. Last modified October 12, at 21:04 (UTC). [https://en.wikipedia.org/w/index.php?title=MESSENGER&oldid=1379942937][ref_messenger]
- "Moon." 2026. Wikipedia. Last modified October 20, at 15:52 (UTC). [https://en.wikipedia.org/w/index.php?title=Moon&oldid=1381191379][ref_moon]
- "Oberth Effect." 2026. Wikipedia. Last modified September 28, at 16:55 (UTC). [https://en.wikipedia.org/w/index.php?title=Oberth\_effect&oldid=1377271791][ref_oberth_effect]
- "Proxima Centauri." 2026. Wikipedia. Last modified October 18, at 13:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Proxima\_Centauri&oldid=1380870772][ref_proxima_centauri]
- "Proxima Centauri d." 2026. Wikipedia. Last modified September 9, at 19:24 (UTC). [https://en.wikipedia.org/w/index.php?title=Proxima\_Centauri\_d&oldid=1374087109][ref_proxima_centauri_d]
- "Solar Sail." 2026. Wikipedia. Last modified August 12, at 08:09 (UTC). [https://en.wikipedia.org/w/index.php?title=Solar\_sail&oldid=1369001629][ref_solar_sail]
- "Space Colonization." 2026. Wikipedia. Last modified October 17, at 03:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Space\_colonization&oldid=1380661105][ref_space_colonization]
- "Titan (Moon)." 2026. Wikipedia. Last modified October 22, at 13:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Titan\_(moon)&oldid=1381433485][ref_titan]
- "TRAPPIST-1." 2026. Wikipedia. Last modified September 27, at 20:43 (UTC). [https://en.wikipedia.org/w/index.php?title=TRAPPIST-1&oldid=1377085528][ref_trappist_1]
- "TRAPPIST-1b." 2026. Wikipedia. Last modified September 9, at 19:20 (UTC). [https://en.wikipedia.org/w/index.php?title=TRAPPIST-1b&oldid=1374086652][ref_trappist_1b]
- "Tsiolkovsky Rocket Equation." 2026. Wikipedia. Last modified August 18, at 02:17 (UTC). [https://en.wikipedia.org/w/index.php?title=Tsiolkovsky\_rocket\_equation&oldid=1369930570][ref_tsiolkovsky_rocket_equation]
- "Venus." 2026. Wikipedia. Last modified October 17, at 16:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Venus&oldid=1380745666][ref_venus]
- "Vulcanoid." 2026. Wikipedia. Last modified September 28, at 01:00 (UTC). [https://en.wikipedia.org/w/index.php?title=Vulcanoid&oldid=1377129642][ref_vulcanoid]

### Related Posts

- Sechter, Brendan. 2026. "Introduction to Space Studies." *Brendan A R Sechter's Development Blog*, February 21. [https://sgeos.github.io/space/math/2026/02/21/introduction\_to\_space\_studies.html][related_post_space_studies]
- Sechter, Brendan. 2026. "Von Neumann Probes." *Brendan A R Sechter's Development Blog*, March 5. [https://sgeos.github.io/science/philosophy/2026/03/05/von\_neumann\_probes.html][related_post_von_neumann_probes]
- Sechter, Brendan. 2026. "Venus Cloudtop Buoyant Analog." *Brendan A R Sechter's Development Blog*, July 6. [https://sgeos.github.io/aerospace/engineering/space-studies/analog-facilities/2026/07/06/venus\_cloudtop\_buoyant\_analog.html][related_post_venus_cloudtop]
- Sechter, Brendan. 2026. "Orbital Manoeuvres in Terms of Delta-v." *Brendan A R Sechter's Development Blog*, August 17. [https://sgeos.github.io/space/space-studies/2026/08/17/orbital\_manoeuvres.html][related_post_orbital_manoeuvres]
- Sechter, Brendan. 2026. "Solar Sailing." *Brendan A R Sechter's Development Blog*, August 18. [https://sgeos.github.io/space/space-studies/2026/08/18/solar\_sailing.html][related_post_solar_sailing]
- Sechter, Brendan. 2026. "Mass Drivers." *Brendan A R Sechter's Development Blog*, August 19. [https://sgeos.github.io/space/space-studies/2026/08/19/mass\_drivers.html][related_post_mass_drivers]

[book_mcinnes_1999]: https://doi.org/10.1007/978-1-4471-3992-8
[ref_51_pegasi_b]: https://en.wikipedia.org/w/index.php?title=51_Pegasi_b&oldid=1381285269
[ref_breakthrough_starshot]: https://en.wikipedia.org/w/index.php?title=Breakthrough_Starshot&oldid=1376867919
[ref_ceres]: https://en.wikipedia.org/w/index.php?title=Ceres_(dwarf_planet)&oldid=1381128658
[ref_delta_v_budget]: https://en.wikipedia.org/w/index.php?title=Delta-v_budget&oldid=1362285519
[ref_earth]: https://en.wikipedia.org/w/index.php?title=Earth&oldid=1380995505
[ref_gravity_assist]: https://en.wikipedia.org/w/index.php?title=Gravity_assist&oldid=1378359042
[ref_hohmann_transfer_orbit]: https://en.wikipedia.org/w/index.php?title=Hohmann_transfer_orbit&oldid=1381150738
[ref_io]: https://en.wikipedia.org/w/index.php?title=Io_(moon)&oldid=1380203631
[ref_lunar_month]: https://en.wikipedia.org/w/index.php?title=Lunar_month&oldid=1377910813
[ref_mars]: https://en.wikipedia.org/w/index.php?title=Mars&oldid=1379497097
[ref_mass_driver]: https://en.wikipedia.org/w/index.php?title=Mass_driver&oldid=1376635859
[ref_mercury]: https://en.wikipedia.org/w/index.php?title=Mercury_(planet)&oldid=1381089194
[ref_messenger]: https://en.wikipedia.org/w/index.php?title=MESSENGER&oldid=1379942937
[ref_moon]: https://en.wikipedia.org/w/index.php?title=Moon&oldid=1381191379
[ref_oberth_effect]: https://en.wikipedia.org/w/index.php?title=Oberth_effect&oldid=1377271791
[ref_proxima_centauri]: https://en.wikipedia.org/w/index.php?title=Proxima_Centauri&oldid=1380870772
[ref_proxima_centauri_d]: https://en.wikipedia.org/w/index.php?title=Proxima_Centauri_d&oldid=1374087109
[ref_solar_sail]: https://en.wikipedia.org/w/index.php?title=Solar_sail&oldid=1369001629
[ref_space_colonization]: https://en.wikipedia.org/w/index.php?title=Space_colonization&oldid=1380661105
[ref_titan]: https://en.wikipedia.org/w/index.php?title=Titan_(moon)&oldid=1381433485
[ref_trappist_1]: https://en.wikipedia.org/w/index.php?title=TRAPPIST-1&oldid=1377085528
[ref_trappist_1b]: https://en.wikipedia.org/w/index.php?title=TRAPPIST-1b&oldid=1374086652
[ref_tsiolkovsky_rocket_equation]: https://en.wikipedia.org/w/index.php?title=Tsiolkovsky_rocket_equation&oldid=1369930570
[ref_venus]: https://en.wikipedia.org/w/index.php?title=Venus&oldid=1380745666
[ref_vulcanoid]: https://en.wikipedia.org/w/index.php?title=Vulcanoid&oldid=1377129642
[related_post_mass_drivers]: {% post_url 2026-08-19-mass_drivers %}
[related_post_mass_drivers_curvature]: {% post_url 2026-08-19-mass_drivers %}#the-curvature-limit
[related_post_mass_drivers_locked]: {% post_url 2026-08-19-mass_drivers %}#release-geometry-on-a-tidally-locked-body
[related_post_mass_drivers_parent]: {% post_url 2026-08-19-mass_drivers %}#from-the-launching-body-to-the-parent
[related_post_mass_drivers_positioning]: {% post_url 2026-08-19-mass_drivers %}#positioning-for-parent-orbits
[related_post_orbital_manoeuvres]: {% post_url 2026-08-17-orbital_manoeuvres %}
[related_post_orbital_manoeuvres_departure]: {% post_url 2026-08-17-orbital_manoeuvres %}#departure
[related_post_orbital_manoeuvres_rocket]: {% post_url 2026-08-17-orbital_manoeuvres %}#the-rocket-equation
[related_post_solar_sailing]: {% post_url 2026-08-18-solar_sailing %}
[related_post_solar_sailing_lightness]: {% post_url 2026-08-18-solar_sailing %}#lightness-number-for-any-star
[related_post_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_venus_cloudtop]: {% post_url 2026-07-06-venus_cloudtop_buoyant_analog %}
[related_post_von_neumann_probes]: {% post_url 2026-03-05-von_neumann_probes %}
[research_anderson_et_al_2011]: https://doi.org/10.1126/science.1211001
[research_badman_2026]: https://doi.org/10.5194/egusphere-egu26-12552
[research_bailer_jones_2021]: https://doi.org/10.1119/10.0002178
[research_beemer_mcnab_2023]: https://doi.org/10.1016/j.actaastro.2023.02.041
[research_benford_benford_2003]: https://doi.org/10.1063/1.1582124
[research_benkhoff_et_al_2010]: https://doi.org/10.1016/j.pss.2009.09.020
[research_benkhoff_et_al_2021]: https://doi.org/10.1007/s11214-021-00861-4
[research_benkoski_et_al_2023]: https://doi.org/10.2514/1.b38595
[research_blewett_et_al_2011]: https://doi.org/10.1126/science.1211681
[research_cassidy_et_al_2015]: https://doi.org/10.1016/j.icarus.2014.10.037
[research_chabot_et_al_2013]: https://doi.org/10.1029/2012je004172
[research_chabot_et_al_2014]: https://doi.org/10.1130/g35916.1
[research_dakermanji_jenkins_ercol_2006]: https://doi.org/10.1109/wcpec.2006.279872
[research_davoudi_et_al_2024]: https://doi.org/10.3847/2041-8213/ad5c6c
[research_deutsch_et_al_2018]: https://doi.org/10.1016/j.icarus.2018.01.013
[research_domingue_et_al_2014]: https://doi.org/10.1007/s11214-014-0039-5
[research_ercol_2007]: https://doi.org/10.2514/6.2007-6188
[research_ercol_balakrishnan_2024]: https://doi.org/10.32865/2346/98763
[research_evans_tabachnik_1999]: https://doi.org/10.1038/19919
[research_faria_et_al_2022]: https://doi.org/10.1051/0004-6361/202142337
[research_fox_et_al_2015]: https://doi.org/10.1007/s11214-015-0211-6
[research_genova_et_al_2019]: https://doi.org/10.1029/2018gl081135
[research_gershman_et_al_2015]: https://doi.org/10.1002/2015ja021610
[research_hauck_et_al_2013]: https://doi.org/10.1002/jgre.20091
[research_hein_et_al_2019]: https://doi.org/10.1016/j.actaastro.2018.12.042
[research_hibberd_et_al_2022]: https://doi.org/10.1016/j.actaastro.2022.07.032
[research_ho_et_al_2011]: https://doi.org/10.1126/science.1211141
[research_hoang_et_al_2017]: https://doi.org/10.3847/1538-4357/aa5da6
[research_howard_et_al_2018]: https://doi.org/10.3847/2041-8213/aacaf3
[research_killen_et_al_2007]: https://doi.org/10.1007/s11214-007-9232-0
[research_kopp_lean_2011]: https://doi.org/10.1029/2010gl045777
[research_kulkarni_lubin_zhang_2018]: https://doi.org/10.3847/1538-3881/aaafd2
[research_lammer_et_al_2026]: https://doi.org/10.5194/egusphere-egu26-18943
[research_lappas_et_al_2005]: https://doi.org/10.2514/6.2005-6084
[research_lario_et_al_2006]: https://doi.org/10.1086/508982
[research_lawrence_et_al_2013]: https://doi.org/10.1126/science.1229953
[research_lyman_et_al_2001]: https://doi.org/10.2514/6.2001-3377
[research_lyngvi_et_al_2005]: https://doi.org/10.1016/j.actaastro.2005.03.042
[research_mangano_et_al_2021]: https://doi.org/10.1007/s11214-021-00797-9
[research_margot_et_al_2012]: https://doi.org/10.1029/2012je004161
[research_mayor_queloz_1995]: https://doi.org/10.1038/378355a0
[research_mazarico_et_al_2014]: https://doi.org/10.1002/2014je004675
[research_mcadams_et_al_2006]: https://doi.org/10.2514/1.18178
[research_mcadams_et_al_2007]: https://doi.org/10.1007/s11214-007-9162-x
[research_mcnutt_et_al_2019]: https://doi.org/10.1016/j.actaastro.2019.06.013
[research_moser_et_al_2010]: https://doi.org/10.2514/6.2010-6091
[research_murakami_jones_2025]: https://doi.org/10.5194/egusphere-egu25-18018
[research_ness_et_al_1974]: https://doi.org/10.1126/science.185.4146.151
[research_neumann_et_al_2013]: https://doi.org/10.1126/science.1229764
[research_nittler_et_al_2011]: https://doi.org/10.1126/science.1211567
[research_nittler_et_al_2020]: https://doi.org/10.1016/j.icarus.2020.113716
[research_paige_et_al_2013]: https://doi.org/10.1126/science.1231106
[research_palaszewski_2015]: https://doi.org/10.2514/6.2015-1654
[research_parkin_2018]: https://doi.org/10.1016/j.actaastro.2018.08.035
[research_peplowski_et_al_2011]: https://doi.org/10.1126/science.1211576
[research_perry_et_al_2015]: https://doi.org/10.1002/2015gl065101
[research_schlei_et_al_2021]: https://doi.org/10.1109/aero50100.2021.9438398
[research_schumacher_gay_2001]: https://doi.org/10.1051/0004-6361:20000356
[research_slade_butler_muhleman_1992]: https://doi.org/10.1126/science.258.5082.635
[research_slavin_et_al_2009]: https://doi.org/10.1126/science.1172011
[research_smith_et_al_2012]: https://doi.org/10.1126/science.1218809
[research_solomon_et_al_2007]: https://doi.org/10.1007/978-0-387-77214-1_1
[research_steffl_et_al_2013]: https://doi.org/10.1016/j.icarus.2012.11.031
[research_suarez_mascareno_et_al_2025]: https://doi.org/10.1051/0004-6361/202553728
[research_vasavada_paige_wood_1999]: https://doi.org/10.1006/icar.1999.6175
[research_winslow_et_al_2015]: https://doi.org/10.1002/2015ja021200
[research_worden_et_al_2021]: https://doi.org/10.1364/ao.435858
