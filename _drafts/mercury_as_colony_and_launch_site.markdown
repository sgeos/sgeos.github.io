---
layout: post
mathjax: true
comments: true
title: "Mercury as a Colony and a Launch Site"
date: 2026-08-17 09:00:00 +0000
categories: space astronomy space-studies
---

<!-- A381 -->
<script>console.log("A381");</script>

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

The method is to express each physical quantity that matters as a function of distance from the Sun,
then to evaluate it at Mercury and at the bodies it competes with.
The quantities are sunlight for photovoltaic power,
orbital speed and the depth of the Sun's gravity well,
the change in velocity, or delta-v, that each journey requires,
the mass ratio that the rocket equation demands for that delta-v,
the length of a mass driver,
the speed a projectile loses in an atmosphere,
the force of sunlight on a sail,
and the frequency of launch windows.
In short,
the first part is refuted as stated and supported only in a narrower form,
and the second part is supported for probes sent toward the Sun and for sunlight-driven propulsion,
but refuted for rocket probes sent outward.

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
[Oberth Effect][ref_oberth_effect].
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
for Mercury Surface, Space Environment, Geochemistry and Ranging
[Solomon et al. 2007][research_solomon_et_al_2007],
reached Mercury after flybys of Earth, Venus and Mercury itself
[MESSENGER][ref_messenger].
BepiColombo,
the joint European and Japanese mission
[Benkhoff et al. 2010][research_benkhoff_et_al_2010],
launched in October 2018 and is planned to enter Mercury orbit in November 2026,
after one Earth flyby, two Venus flybys and six Mercury flybys
[BepiColombo][ref_bepicolombo].
A Hohmann flight of 105 days thus becomes a journey of several years.
For a colony that must import people and equipment,
that choice between a large delta-v and a long voyage is a real and permanent burden.

### Living There

The thermal environment is severe but structured.
At Mercury's equator the surface ranges from −173 °C to 427 °C
[Mercury][ref_mercury],
values that rest on thermal modeling by Vasavada and coauthors
[Vasavada 1999][research_vasavada_1999].
A black surface facing the Sun with no conduction into the ground would reach the following temperature,
where $S$ is the local flux.

$$
T_{\mathrm{subsolar}} = \left(\frac{S}{\sigma}\right)^{1/4}
$$

This gives 710 K at perihelion and 576 K at aphelion.
The perihelion value lies just above the measured maximum of 427 °C,
about 700 K,
as it should for an ideal black surface that reflects nothing and conducts no heat downward.
The heat is not continuous at any one place.
Mercury rotates three times for every two orbits,
so one solar day lasts about 176 Earth days
[Mercury][ref_mercury],
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
so the floors of polar craters never see the Sun.
Radar imaging in 1991 found highly reflective material at the north pole,
with polarization ratios previously seen only from icy regions of Mars and icy outer satellites
[Slade, Butler and Muhleman 1992][research_slade_butler_muhleman_1992].
The MESSENGER neutron spectrometer,
together with thermal modeling and laser altimetry,
confirmed that the main component of the radar-bright material at the north pole is water ice,
some exposed at the surface and some buried beneath dark deposits interpreted as organic material
[Lawrence et al. 2013][research_lawrence_et_al_2013]
[Neumann et al. 2013][research_neumann_et_al_2013]
[Paige et al. 2013][research_paige_et_al_2013].
Water is the single most important import for a settlement,
and Mercury has a local supply at its poles.

Other conditions are less extreme than the reputation suggests.
Surface gravity is about 3.7 metres per second squared
[Mercury][ref_mercury],
which is almost the same as the 3.72 of Mars
[Mars][ref_mars].
Whether people can remain healthy at about 0.38 of Earth's gravity is unknown for both planets,
so on this point Mercury is no worse than the planet most often proposed for settlement.
Mercury has a global magnetic field,
which Mariner 10 measured at about 1.1 percent of the strength of Earth's
[Mercury][ref_mercury],
and which MESSENGER resolved as an offset dipole with a moment of about 195 nanotesla times the cube of Mercury's radius
[Anderson et al. 2011][research_anderson_et_al_2011].
The field is strong enough to deflect the solar wind but offers little shelter at the surface.

Radiation from solar storms is the clearest added hazard.
Lario and coauthors fitted the radial dependence of solar energetic proton events measured within 1 AU by the two Helios spacecraft and by Interplanetary Monitoring Platform 8.
They found event fluences that scale from $R^{-2.1}$ to $R^{-1.0}$ across their two energy bands,
and peak intensities from $R^{-2.7}$ to $R^{-1.9}$
[Lario et al. 2006][research_lario_et_al_2006].
Applying those exponents at Mercury's mean distance gives event fluences 2.6 to 7.3 times those at Earth's distance,
and peak intensities 6.1 to 13.0 times as high.
They also found that the longitude of the source region relative to the observer matters more than distance,
so these factors describe averages over many events rather than any single storm.
Shielding by regolith addresses the problem at any distance,
so the burden is the mass of the shielding rather than a hard limit on settlement.

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
This is less than the 5.03 of Mars and much less than the 11.19 of Earth,
although more than the 2.38 of the Moon and the 0.52 of Ceres.
Mercury's exosphere has a surface pressure of about 0.5 nanopascal or less
[Mercury][ref_mercury],
so launching from it is effectively launching from vacuum.
That makes Mercury a candidate for a mass driver,
an electromagnetic launcher that accelerates a payload along a track
[Mass Driver][ref_mass_driver].
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
| Mercury | ≲ 0.5 nPa | effectively 0 | 1.000 | effectively 0 |
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
[Tsiolkovsky Rocket Equation][ref_tsiolkovsky_rocket_equation].
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

The value of 450 seconds is typical of hydrogen and oxygen engines,
and 900 seconds is used here as a representative figure for nuclear thermal propulsion.
Both are assumptions rather than cited values.
A chemical rocket leaving the solar system from Mercury must start about 99 times as heavy as its final mass,
more than twice the ratio from an ideal Earth launch and about seven times the ratio from the Moon.

The mass driver changes this comparison but does not reverse it.
A track long enough to give the full 20.28 kilometres per second would be 21 kilometres at 1,000 times standard gravity,
with an energy of 206 megajoules per kilogram.
A square metre of photovoltaic panel at 20 percent efficiency at Mercury's mean distance would collect that energy in about 31 hours of sunlight.
Energy at that scale is plentiful on Mercury,
so a large enough electromagnetic launcher could substitute electricity for propellant.
A launcher on the Moon would face the same physics with a smaller delta-v,
however,
so the advantage over the Moon is only in the supply of electricity,
not in the delta-v.

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
[Fox et al. 2015][research_fox_et_al_2015]
reached a perihelion of 9.86 solar radii,
and the exact value was set by its seventh Venus gravity assist in 2024
[Parker Solar Probe][ref_parker_solar_probe].
From a circular orbit the delta-v to lower perihelion to 10 solar radii is 25.70 kilometres per second at Mercury's distance,
against 20.91 at Earth's,
so a direct drop is not cheaper from Mercury.
What Mercury offers instead is proximity.
Its synodic period with Venus is 145 days rather than Earth's 584,
the flight to Venus takes 0.21 years rather than 0.40,
and a probe launched from Mercury begins its mission already between 0.31 and 0.47 AU from the Sun.

### Verdict on Part Two A

For probes to the outer solar system,
Part Two A is refuted.
Mercury is the most expensive origin in delta-v for every target beyond Venus,
and Ceres,
the Moon
and Mars are each cheaper,
whether the probe is driven by a rocket or by a mass driver.
For probes to Venus and toward the Sun,
for frequent launch windows,
and for any mission whose cost is dominated by energy rather than delta-v,
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
For rocket-driven interstellar probes,
Mercury is the worst starting point among the bodies considered here.

### Solar Sails

A solar sail is pushed by reflected sunlight
[Solar Sail][ref_solar_sail]
[McInnes 1999][book_mcinnes_1999].
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
Mercury's role is therefore as the nearest place to manufacture and stage sails,
not as a physically privileged launch point.

### Beamed Propulsion

A laser-driven sail shifts the energy problem to the launch site.
Breakthrough Starshot proposed light sails pushed to between 15 and 20 percent of light speed
by a phased array of lasers with a combined output of up to 100 gigawatts
[Breakthrough Starshot][ref_breakthrough_starshot].
Whatever the power such a system needs,
its collectors scale inversely with the local sunlight.
Supplying 100 gigawatts of electricity from photovoltaics at 20 percent conversion,
which understates the input that lasers of that output would draw,
requires 55.0 square kilometres of collector at Mercury's mean distance
and 367 square kilometres at 1 AU in space,
with more on the ground at Earth because of night,
weather and the atmosphere.
Mercury's vacuum also removes atmospheric absorption and turbulence from the beam path.

The same caveat applies as for sails.
The sunlight is a property of the distance,
so a collector array in orbit at 0.39 AU receives the same flux as Mercury's surface.
Mercury contributes a solid foundation,
local materials,
cold polar terrain for radiators
and a slow rotation that keeps a site facing a given direction in the sky for weeks rather than hours.
No vulcanoid asteroids inside Mercury's orbit have been found
[Vulcanoid][ref_vulcanoid],
so Mercury is the only known large source of material that close to the Sun.

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
Mercury also passes behind the Sun as seen from Earth once in every 116-day synodic period,
interrupting direct links between the two.

### Verdict on Part Two B

Part Two B is partially supported.
For rocket probes,
including the solar Oberth manoeuvre,
Mercury is the worst starting point.
For sail and beamed probes,
the region near Mercury's orbit is the best,
and Mercury is the only known body in that region that can supply mass,
so a base there is plausibly the most beneficial site for those methods.
The benefit comes from the distance and from Mercury's materials together,
and it would be shared by any large orbital industry at the same distance.

## Other Advantages and Disadvantages of a Mercury Base

In a future in which every body can be settled,
Mercury competes with the others on a list of physical properties.
The advantages follow.

- The densest sunlight available on a solid body, 6.25 to 14.4 kilowatts per square metre over an orbit.
- Water ice in permanently shadowed polar craters, confirmed by several independent measurements.
- A large iron-rich core, which occupies about 57 percent of the planet's volume, against 17 percent for Earth [Mercury][ref_mercury], with a model of a solid crust and mantle over a solid iron-sulfide layer and an iron-rich liquid outer core [Smith et al. 2012][research_smith_et_al_2012].
- An escape speed of 4.25 kilometres per second with no atmosphere, which allows mass drivers.
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
- A home that always appears near the Sun from the outer solar system, and regular conjunctions that block links with Earth.
- Waste heat rejection that is hardest exactly where the sunlight is strongest, which limits how much of the abundant power can be used. Two-sided flat panels absorbing 90 percent of the light and emitting with an emissivity of 0.85 reach 569 K at perihelion in this simple model, against 315 K at 1 AU.

## Verdict on the Hypothesis

<div style="overflow-x: auto;" markdown="1">

| Claim | Verdict | Deciding physics |
|---|---|---|
| Part one, Mercury is the hardest body to colonize | Refuted as stated, supported for reaching landable bodies | Venus's surface, Io, the giant planets and the Sun are harder, while Mercury has the highest LEO-to-surface delta-v among landable bodies |
| Part two A, the best base for probes within the solar system | Refuted for outward targets, supported for Venus and the Sun | The Sun's gravity well raises every outward delta-v, while windows are frequent and inward targets are close |
| Part two B, the best base for probes to other stars | Partially supported | Rockets and the solar Oberth manoeuvre favour distant origins, while sails and beamed power favour the region near Mercury, where Mercury is the only known source of mass |

</div>

## Epistemic State

**Facts reported by the cited sources.**
Physical data for the bodies,
including Mercury's orbit,
temperature range,
rotation,
gravity,
escape speed,
exospheric pressure
and core fraction,
come from the Wikipedia entries cited,
which draw on NASA fact sheets and the peer-reviewed literature.
The findings attributed to Kopp and Lean
and to the groups led by Slade,
Margot,
Anderson,
Smith
and Lario
are taken from their abstracts as recorded by OpenAlex.
For the three 2013 polar ice papers the record available was the journal's shared editorial summary,
which states the joint conclusion rather than each paper's separate result.
The paper of Vasavada,
the papers of the groups led by Solomon,
Benkhoff,
Fox
and Benkoski,
the paper of Beemer and McNab,
and the book by McInnes,
are cited only for what their titles state,
because no abstract was retrievable.
None of the sources was read in full.

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

**Unaddressed concerns.**
This article does not model the long-term effects of 0.38 of Earth's gravity on people,
the chemistry of Mercury's regolith as a feedstock,
the engineering of radiators or shielding,
or the economics of any base.
The solar energetic particle factors are ensemble averages and do not bound the worst event.

## Out of Scope

This article does not treat the colonization of bodies outside the solar system,
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
and Mercury is the only known body there that can supply mass.
A future civilization would plausibly build its sail yards and laser arrays near Mercury
and its rocket ports far from the Sun,
which is a division of labour rather than a single best base.
Self-replicating probes of the kind discussed in an earlier article on this site
[Von Neumann Probes][related_post_von_neumann_probes]
would face the same choice of origin.

## References

- [Book, McInnes 1999, Solar Sailing][book_mcinnes_1999]
- [Reference, BepiColombo, Wikipedia][ref_bepicolombo]
- [Reference, Breakthrough Starshot, Wikipedia][ref_breakthrough_starshot]
- [Reference, Delta-v Budget, Wikipedia][ref_delta_v_budget]
- [Reference, Gravity Assist, Wikipedia][ref_gravity_assist]
- [Reference, Hohmann Transfer Orbit, Wikipedia][ref_hohmann_transfer_orbit]
- [Reference, Io, Wikipedia][ref_io]
- [Reference, Mars, Wikipedia][ref_mars]
- [Reference, Mass Driver, Wikipedia][ref_mass_driver]
- [Reference, Mercury, Wikipedia][ref_mercury]
- [Reference, MESSENGER, Wikipedia][ref_messenger]
- [Reference, Oberth Effect, Wikipedia][ref_oberth_effect]
- [Reference, Parker Solar Probe, Wikipedia][ref_parker_solar_probe]
- [Reference, Solar Sail, Wikipedia][ref_solar_sail]
- [Reference, Space Colonization, Wikipedia][ref_space_colonization]
- [Reference, Titan, Wikipedia][ref_titan]
- [Reference, Tsiolkovsky Rocket Equation, Wikipedia][ref_tsiolkovsky_rocket_equation]
- [Reference, Venus, Wikipedia][ref_venus]
- [Reference, Vulcanoid, Wikipedia][ref_vulcanoid]
- [Related Post, Introduction to Space Studies][related_post_space_studies]
- [Related Post, Venus Cloudtop Buoyant Analog][related_post_venus_cloudtop]
- [Related Post, Von Neumann Probes][related_post_von_neumann_probes]
- [Research, Anderson et al. 2011, The Global Magnetic Field of Mercury from MESSENGER Orbital Observations][research_anderson_et_al_2011]
- [Research, Beemer and McNab 2023, Launch Parameters of a Lunar Ice Payload Traveling via Electromagnetic Mass Accelerator][research_beemer_mcnab_2023]
- [Research, Benkhoff et al. 2010, BepiColombo, Comprehensive Exploration of Mercury, Mission Overview and Science Goals][research_benkhoff_et_al_2010]
- [Research, Benkoski et al. 2023, Combined Heat Shield and Solar Thermal Propulsion System for an Oberth Maneuver][research_benkoski_et_al_2023]
- [Research, Fox et al. 2015, The Solar Probe Plus Mission, Humanity's First Visit to Our Star][research_fox_et_al_2015]
- [Research, Kopp and Lean 2011, A New, Lower Value of Total Solar Irradiance, Evidence and Climate Significance][research_kopp_lean_2011]
- [Research, Lario et al. 2006, Radial and Longitudinal Dependence of Solar 4 to 13 MeV and 27 to 37 MeV Proton Peak Intensities and Fluences, Helios and IMP 8 Observations][research_lario_et_al_2006]
- [Research, Lawrence et al. 2013, Evidence for Water Ice Near Mercury's North Pole from MESSENGER Neutron Spectrometer Measurements][research_lawrence_et_al_2013]
- [Research, Margot et al. 2012, Mercury's Moment of Inertia from Spin and Gravity Data][research_margot_et_al_2012]
- [Research, Neumann et al. 2013, Bright and Dark Polar Deposits on Mercury, Evidence for Surface Volatiles][research_neumann_et_al_2013]
- [Research, Paige et al. 2013, Thermal Stability of Volatiles in the North Polar Region of Mercury][research_paige_et_al_2013]
- [Research, Slade, Butler and Muhleman 1992, Mercury Radar Imaging, Evidence for Polar Ice][research_slade_butler_muhleman_1992]
- [Research, Smith et al. 2012, Gravity Field and Internal Structure of Mercury from MESSENGER][research_smith_et_al_2012]
- [Research, Solomon et al. 2007, MESSENGER Mission Overview][research_solomon_et_al_2007]
- [Research, Vasavada 1999, Near-Surface Temperatures on Mercury and the Moon and the Stability of Polar Ice Deposits][research_vasavada_1999]

[book_mcinnes_1999]: https://doi.org/10.1007/978-1-4471-3992-8
[ref_bepicolombo]: https://en.wikipedia.org/wiki/BepiColombo
[ref_breakthrough_starshot]: https://en.wikipedia.org/wiki/Breakthrough_Starshot
[ref_delta_v_budget]: https://en.wikipedia.org/wiki/Delta-v_budget
[ref_gravity_assist]: https://en.wikipedia.org/wiki/Gravity_assist
[ref_hohmann_transfer_orbit]: https://en.wikipedia.org/wiki/Hohmann_transfer_orbit
[ref_io]: https://en.wikipedia.org/wiki/Io_(moon)
[ref_mars]: https://en.wikipedia.org/wiki/Mars
[ref_mass_driver]: https://en.wikipedia.org/wiki/Mass_driver
[ref_mercury]: https://en.wikipedia.org/wiki/Mercury_(planet)
[ref_messenger]: https://en.wikipedia.org/wiki/MESSENGER
[ref_oberth_effect]: https://en.wikipedia.org/wiki/Oberth_effect
[ref_parker_solar_probe]: https://en.wikipedia.org/wiki/Parker_Solar_Probe
[ref_solar_sail]: https://en.wikipedia.org/wiki/Solar_sail
[ref_space_colonization]: https://en.wikipedia.org/wiki/Space_colonization
[ref_titan]: https://en.wikipedia.org/wiki/Titan_(moon)
[ref_tsiolkovsky_rocket_equation]: https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation
[ref_venus]: https://en.wikipedia.org/wiki/Venus
[ref_vulcanoid]: https://en.wikipedia.org/wiki/Vulcanoid
[related_post_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[related_post_venus_cloudtop]: {% post_url 2026-07-06-venus_cloudtop_buoyant_analog %}
[related_post_von_neumann_probes]: {% post_url 2026-03-05-von_neumann_probes %}
[research_anderson_et_al_2011]: https://doi.org/10.1126/science.1211001
[research_beemer_mcnab_2023]: https://doi.org/10.1016/j.actaastro.2023.02.041
[research_benkhoff_et_al_2010]: https://doi.org/10.1016/j.pss.2009.09.020
[research_benkoski_et_al_2023]: https://doi.org/10.2514/1.b38595
[research_fox_et_al_2015]: https://doi.org/10.1007/s11214-015-0211-6
[research_kopp_lean_2011]: https://doi.org/10.1029/2010GL045777
[research_lario_et_al_2006]: https://doi.org/10.1086/508982
[research_lawrence_et_al_2013]: https://doi.org/10.1126/science.1229953
[research_margot_et_al_2012]: https://doi.org/10.1029/2012JE004161
[research_neumann_et_al_2013]: https://doi.org/10.1126/science.1229764
[research_paige_et_al_2013]: https://doi.org/10.1126/science.1231106
[research_slade_butler_muhleman_1992]: https://doi.org/10.1126/science.258.5082.635
[research_smith_et_al_2012]: https://doi.org/10.1126/science.1218809
[research_solomon_et_al_2007]: https://doi.org/10.1007/978-0-387-77214-1_1
[research_vasavada_1999]: https://doi.org/10.1006/icar.1999.6175
