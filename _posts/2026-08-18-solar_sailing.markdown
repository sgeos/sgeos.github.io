---
layout: post
mathjax: true
comments: true
title: "Solar Sailing"
date: 2026-08-18 09:00:00 +0000
categories: space space-studies
---

<!-- A382 -->
<script>console.log("A382");</script>

A solar sail is a spacecraft propelled by the pressure of light reflecting from a large, thin surface
[Solar Sail][ref_solar_sail].
It carries no propellant,
so its thrust never runs out,
but the thrust is tiny and can never point toward the star that supplies it.
This article develops the physics of solar sailing in order.
It begins with the concept and the basic mathematics,
then gives parametric equations that assume nothing about the star or the craft,
and then evaluates them for the Sun and for several other stars.
Later sections compare sails of different quality,
different levels of steering,
and sails that can or cannot be retracted.
A section on orbital manoeuvres explains how a sail performs them,
which ones a given sail cannot perform,
and which ones no sail can perform,
and a final section covers the secondary propulsion those manoeuvres require.
One section covers the physical difficulty of folding a sail for launch,
and the last major section covers deceleration and capture when a sail arrives at another star.

This article does not design a mission
and does not recommend any material or mechanism.
Every number in it is either taken from a cited source or computed from the equations shown,
and every computed example is idealized in ways stated where it is used.
An earlier article on this site introduces the orbital mechanics used here
[Introduction to Space Studies][related_post_space_studies],
and another treats the standard orbital manoeuvres in terms of delta-v
[Orbital Manoeuvres in Terms of Delta-v][related_post_orbital_manoeuvres].

## The Concept

Light carries momentum.
A beam of power per unit area $S$ carries momentum per unit area per unit time $S/c$,
where $c$ is the speed of light.
A surface that absorbs the beam is pushed with a pressure $S/c$,
and a perfect mirror facing the beam is pushed with twice that,
because the reflected light carries its momentum away in the opposite direction
[Radiation Pressure][ref_radiation_pressure].
At Earth's distance from the Sun,
where the flux measured during the 2008 solar minimum was 1,360.8 ± 0.5 watts per square metre
[Kopp and Lean 2011][research_kopp_lean_2011],
these pressures are about 4.54 and 9.08 micropascals.
For a photon of energy $E$ the momentum is $E/c$,
so the pressures on an absorber and on a perfect mirror at normal incidence are the following.

$$
p = \frac{E}{c}, \qquad
P_{\mathrm{abs}} = \frac{S}{c}, \qquad
P_{\mathrm{mirror}} = \frac{2S}{c}
\tag{1}
$$

A square sail of 80 square metres,
the size flown by the Advanced Composite Solar Sail System of the National Aeronautics and Space Administration,
or NASA,
known as ACS3
[Solar Sail][ref_solar_sail],
would feel at most 0.726 millinewtons facing the Sun at that distance.

A force that small is useful only because it never stops.
A chemical rocket spends its propellant in minutes,
while a sail is pushed for as long as it is in sunlight.
The penalty is that the force is set by geometry.
A flat mirror is pushed along its own normal,
so the force always has a component directed away from the star,
and the craft can steer only by turning the sail.

Sunlight is not the only thing streaming from the Sun.
At 1 AU,
the astronomical unit,
the solar wind exerts a pressure typically between 1 and 6 nanopascals
[Solar Wind][ref_solar_wind],
which is between about one fifteen-hundredth and one nine-thousandth of the light pressure on a perfect mirror.
The wind's pressure is its momentum flux,
with $n$ the number density of protons,
$m_{p}$ the proton mass
and $V$ the wind speed
[Solar Wind][ref_solar_wind].

$$
P_{\mathrm{sw}} = n\,m_{p}\,V^{2}
\tag{2}
$$

With 5 protons per cubic centimetre at 400 kilometres per second this gives 1.34 nanopascals,
inside the quoted range.
A solar sail therefore ignores the wind.
Magnetic sails
[Magnetic Sail][ref_magnetic_sail]
and electric sails
[Electric Sail][ref_electric_sail]
are separate concepts that push against the wind or against the interstellar medium,
and they return below only as aids to deceleration.

Solar sailing has flown.
The Japanese IKAROS spacecraft,
launched in May 2010 together with the Venus orbiter Akatsuki,
was the first to demonstrate solar sailing in interplanetary space
[Mori and IKAROS Demonstration Team 2011][research_mori_et_al_2011]
[Yonetoku et al. 2011][research_yonetoku_et_al_2011],
and it flew past Venus in December 2010
[IKAROS][ref_ikaros].
Tsuda and coauthors report on it as a deep space solar sail demonstrator
[Tsuda et al. 2011][research_tsuda_et_al_2011]
[Tsuda et al. 2013][research_tsuda_et_al_2013].
NASA's NanoSail-D2 deployed a 10 square metre sail in Earth orbit in January 2011,
after its predecessor was lost in a launch failure
[NanoSail-D2][ref_nanosail_d2].
Johnson and coauthors describe the NanoSail-D solar sail demonstration mission
[Johnson et al. 2011][research_johnson_et_al_2011].
The Planetary Society's LightSail 2 demonstrated controlled solar sailing in Earth orbit,
where its controlled thrust measurably reduced the rate of orbital decay
[Spencer et al. 2021][research_spencer_et_al_2021].
ACS3 launched in April 2024
[Solar Sail][ref_solar_sail],
after a project that covered its sail design,
spacecraft systems,
operations
and ground testing
[Wilkie 2021][research_wilkie_2021].
NASA's Near-Earth Asteroid Scout,
or NEA Scout,
was designed to use an 86 square metre sail as its primary propulsion
[McNutt et al. 2014][research_mcnutt_et_al_2014].
These flights followed proposals made decades earlier.
Wright and Warmke estimated in 1976 that early sails could reach characteristic accelerations of 0.2 to 1.3 millimetres per second squared with an overall efficiency of 80 to 90 percent,
and proposed a rendezvous with Halley's comet as the first sail mission
[Wright and Warmke 1976][research_wright_warmke_1976].

## The Basic Mathematics

Consider a perfectly reflecting flat sail of area $A$ on a craft of total mass $m$,
at a distance $r$ from a star where the flux is $S$.
Let $\hat{n}$ be the unit normal of the sail,
pointing away from the star,
and let the cone angle $\alpha$ be the angle between $\hat{n}$ and the direction from the star to the sail.
The sail intercepts light over its projected area $A\cos\alpha$,
and each unit of intercepted momentum is reflected so that twice its normal component is transferred.
The force is therefore the following.

$$
\vec{F} = \frac{2 S A}{c}\cos^{2}\alpha\,\hat{n}
\tag{3}
$$

Two quantities describe a sail's performance.
The sail loading $\sigma = m/A$ is the total mass per unit area of sail.
The characteristic acceleration $a_{c}$ is the acceleration of the craft facing the Sun at 1 AU,
and the lightness number $\beta$ is the ratio of that acceleration to the Sun's gravity at the same distance
[Solar Sail][ref_solar_sail].

$$
a_{c} = \frac{2 S_{0}}{c\,\sigma}, \qquad
\beta = \frac{a_{c}}{\mu_{\odot}/(1\ \mathrm{AU})^{2}}
\tag{4}
$$

Here $S_{0}$ is the flux at 1 AU and $\mu_{\odot}$ is the Sun's gravitational parameter.
Because both the light and gravity fall as the inverse square of distance,
$\beta$ is the same at every distance from the Sun,
and it determines which manoeuvres a craft can perform
[Solar Sail][ref_solar_sail].
The equation of motion around the star,
with $\vec{r}$ the position relative to the star,
is the following.

$$
\ddot{\vec{r}} = -\frac{\mu}{r^{2}}\,\hat{r} + \beta\,\frac{\mu}{r^{2}}\cos^{2}\alpha\,\hat{n}
\tag{5}
$$

The first term is gravity and the second is the sail.
Every result in the rest of this article is a consequence of this equation,
of its generalization below,
or of the limits on $\beta$ and $\alpha$ that real sails impose.

## Generalized Parametric Equations

The basic equations assume a perfect mirror and the Sun.
This section removes both assumptions.
The star is described by its luminosity $L$,
its mass $M$
and its radius $R_{\ast}$.
The craft is described by its mass $m$,
its sail area $A$,
which may change with time if the sail can be retracted,
the specular reflectance $\rho$ of the sail,
the front and back emissivities $\varepsilon_{f}$ and $\varepsilon_{b}$,
and two steering angles,
the cone angle $\alpha$ and the clock angle $\delta$ that sets the direction in which the normal is tilted.
Let $\hat{u}$ be the unit vector from the star to the sail.
No other property of star or craft is assumed.

### Pressure and Force

At distance $r$ the flux and the pressure on an absorber are the following.

$$
S(r) = \frac{L}{4\pi r^{2}}, \qquad
P(r) = \frac{L}{4\pi c\,r^{2}}
\tag{6}
$$

Take a flat sail that reflects a fraction $\rho$ of the light specularly and absorbs the rest,
with no transmission and no diffuse reflection.
The absorbed light pushes along $\hat{u}$,
and the reflected light pushes along $\hat{n}$,
so the force is the following.

$$
\vec{F} = P(r)\,A\cos\alpha\left[(1-\rho)\,\hat{u} + 2\rho\cos\alpha\,\hat{n}\right]
\tag{7}
$$

Resolving this into a component along the normal and a component in the plane of the sail gives the following,
where the transverse unit vector $\hat{t}$ lies in the plane of the sail on the side toward which it is tilted.

$$
F_{n} = P A (1+\rho)\cos^{2}\alpha, \qquad
F_{t} = P A (1-\rho)\cos\alpha\sin\alpha, \qquad
\tan\phi = \frac{1-\rho}{1+\rho}\tan\alpha
\tag{8}
$$

The angle $\phi$ is the angle between the net force and the sail normal.
An imperfect sail is pushed less hard and in a direction tilted from its normal toward the Sun line.
With $\rho = 0.9$ the force is tilted 2.13 degrees from the normal at a cone angle of 35.26 degrees,
and with $\rho = 0.85$ it is tilted 3.28 degrees.
This model ignores thermal re-emission and diffuse scattering,
which a full optical model of a real film would include.
Mengali,
Quarta,
Circi
and Dachwald refined the force model with coefficients that depend on the angle of incidence,
the roughness of the surface
and the distance from the Sun,
and found from experimental data that the angle of incidence is the main variable
[Mengali et al. 2007][research_mengali_et_al_2007].
Swartzlander analysed diffractive sails,
which redirect light by diffraction rather than reflection,
and found no penalty for a transparent diffractive sail on a simple transfer from Earth to Mars
[Swartzlander 2017][research_swartzlander_2017].

### Lightness Number for Any Star

Dividing the face-on force by the star's gravitational pull on the craft,
with $\sigma = m/A$,
gives the generalized lightness number.

$$
\beta = \frac{(1+\rho)\,L}{4\pi c\,G M\,\sigma}
\tag{9}
$$

For a perfect mirror this reduces to $L/(2\pi c G M \sigma)$.
The loading at which a perfect mirror has $\beta = 1$,
so that the light exactly balances gravity,
is the critical loading.

$$
\sigma^{\ast} = \frac{L}{2\pi c\,G M}
\tag{10}
$$

The lightness number depends on the star only through $L/M$,
and on the craft only through $\sigma$ and $\rho$.

### Equation of Motion

With a retractable sail of area $A(t)$ the general equation of motion is the following.

$$
\ddot{\vec{r}} = -\frac{G M}{r^{2}}\,\hat{u}
+ \frac{L\,A(t)\cos\alpha}{4\pi c\,m\,r^{2}}\left[(1-\rho)\,\hat{u} + 2\rho\cos\alpha\,\hat{n}(\alpha,\delta)\right]
\tag{11}
$$

Four standard results follow from it.
Each is derived here for an ideal sail unless stated.

**Reduced gravity.**
A sail held face-on pushes only along $\hat{u}$,
so it acts as a reduction of the star's gravity.

$$
\mu_{\mathrm{eff}} = (1-\beta)\,G M
\tag{12}
$$

**Escape.**
A sail opened face-on on a circular orbit of radius $r_{0}$ keeps its circular speed $v_{c} = \sqrt{GM/r_{0}}$
while the effective gravity weakens,
so energy conservation gives its final speed.
It escapes when $\beta \geq 1/2$.

$$
v_{\infty} = v_{c}(r_{0})\sqrt{2\beta - 1}
\tag{13}
$$

**Departure from a close pass.**
A sail that falls from an orbit of semi-major axis $a$ to a closest distance $q$ and turns face-on there leaves with the following speed.

$$
v_{\infty} = \sqrt{\frac{2\beta\,G M}{q} - \frac{G M}{a}}
\tag{14}
$$

**Steering and spirals.**
The component of an ideal sail's force across the Sun line is $\beta (GM/r^{2})\cos^{2}\alpha\sin\alpha$,
which is greatest at $\tan\alpha = 1/\sqrt{2}$,
a cone angle of 35.26 degrees,
where $\cos^{2}\alpha\sin\alpha = 0.385$.
For a small lightness number the orbit stays nearly circular,
and Gauss's equation for the rate of change of the orbit's size gives the time to spiral from radius $r_{1}$ to radius $r_{2}$ at a fixed cone angle.

$$
t = \frac{\left|r_{2}^{3/2} - r_{1}^{3/2}\right|}{3\,\beta\,k\,\sqrt{G M}}, \qquad k = \cos^{2}\alpha\sin\alpha
\tag{15}
$$

Tilting forward spirals outward and tilting backward spirals inward.
In delta-v terms a slow spiral costs the difference of the circular speeds,
as derived for low-thrust spirals in the companion article on manoeuvres
[Orbital Manoeuvres in Terms of Delta-v, Low-Thrust Spirals][related_post_orbital_manoeuvres_spirals].

$$
\Delta v_{\mathrm{spiral}} = \left|\sqrt{\frac{GM}{r_{1}}} - \sqrt{\frac{GM}{r_{2}}}\right|
\tag{16}
$$

A sail pays this delta-v in time rather than in propellant.

### Temperature

A sail element facing the star at cone angle $\alpha$ absorbs $(1-\rho)S\cos\alpha$ per unit area
and radiates from both faces,
so its equilibrium temperature is the following,
with $\sigma_{\mathrm{SB}}$ the Stefan-Boltzmann constant.

$$
T = \left[\frac{(1-\rho)\,S(r)\cos\alpha}{\sigma_{\mathrm{SB}}\left(\varepsilon_{f}+\varepsilon_{b}\right)}\right]^{1/4}
\tag{17}
$$

The temperature depends on the flux and on the coatings,
but not on the area or the loading,
so a better sail is not a cooler sail.
A maximum allowed temperature $T_{\max}$ sets a maximum flux,
and therefore a closest approach to any star.

$$
q_{\min} = \sqrt{\frac{L}{4\pi F_{\max}}}, \qquad
F_{\max} = \frac{\sigma_{\mathrm{SB}}\left(\varepsilon_{f}+\varepsilon_{b}\right)T_{\max}^{4}}{1-\rho}
\tag{18}
$$

### Where the Equations Fail

These equations assume a star small enough to treat as a point,
a flat sail,
and speeds far below light speed.
The force varies as the inverse square of distance except extremely close to the Sun
[Solar Sail][ref_solar_sail],
where the star's finite disc matters.
A real sail billows and wrinkles,
so its normal is not single-valued.
At speeds that are a few percent of light speed,
the light reaching a receding sail is Doppler shifted and its force falls,
to first order by the following factor.

$$
\frac{F(v)}{F(0)} \approx \frac{1 - v/c}{1 + v/c}
\tag{19}
$$

That factor is 0.912 at 4.6 percent of light speed and 0.667 at 20 percent,
and it rises above one for a sail moving toward the star.

## The Values for Our Star

The Sun's luminosity is $3.828 \times 10^{26}$ watts
[Sun][ref_sun],
the nominal value adopted by the International Astronomical Union in 2015
[Prša et al. 2016][research_prsa_et_al_2016],
which gives 1,361.2 watts per square metre at 1 AU,
in agreement with the measured value
[Kopp and Lean 2011][research_kopp_lean_2011].
The Sun's gravity at 1 AU is 5.93 millimetres per second squared,
the light pressure on a perfect mirror there is 9.08 micropascals,
and the critical loading is 1.531 grams per square metre.
Wikipedia states the same relations in practical units as $a_{c} = 9.08\,\eta/\sigma$ millimetres per second squared,
with $\sigma$ in grams per square metre and $\eta$ an efficiency,
and $\beta = a_{c}/5.93$
[Solar Sail][ref_solar_sail].

$$
a_{c} = \frac{9.08\,\eta}{\sigma}\ \mathrm{mm/s^{2}}, \qquad
\beta = \frac{a_{c}}{5.93\ \mathrm{mm/s^{2}}} = \eta\,\frac{\sigma^{\ast}}{\sigma}
\tag{20}
$$

The table gives the ideal values for a range of loadings.

<div style="overflow-x: auto;" markdown="1">

| Sail loading, g/m² | Lightness number | Characteristic acceleration, mm/s² |
|---|---|---|
| 1,550 | 0.00099 | 0.0059 |
| 400 | 0.0038 | 0.023 |
| 200 | 0.0077 | 0.045 |
| 100 | 0.015 | 0.091 |
| 10 | 0.15 | 0.91 |
| 1.531 | 1.0 | 5.93 |
| 1.0 | 1.53 | 9.08 |
| 0.1 | 15.3 | 90.8 |
| 0.00076 | about 2,000 | about 12,000 |

</div>

### Other Stars

The lightness number of a given sail changes from star to star as $L/M$.
The table uses stellar masses and luminosities in solar units as listed by Wikipedia
[Alpha Centauri][ref_alpha_centauri]
[Proxima Centauri][ref_proxima_centauri]
[Sirius][ref_sirius],
which draws them from astrometry of Alpha Centauri A and B
[Akeson et al. 2021][research_akeson_et_al_2021],
a calibration of nearby M dwarfs for Proxima Centauri
[Pineda et al. 2021][research_pineda_youngblood_france_2021],
and astrometry of the Sirius system
[Bond et al. 2017][research_bond_et_al_2017].

<div style="overflow-x: auto;" markdown="1">

| Star | Luminosity | Mass | $L/M$, the factor on $\beta$ | Critical loading, g/m² |
|---|---|---|---|---|
| Sun | 1 | 1 | 1 | 1.531 |
| Alpha Centauri A | 1.5059 | 1.0788 | 1.40 | 2.14 |
| Alpha Centauri B | 0.4981 | 0.9092 | 0.548 | 0.839 |
| Proxima Centauri | 0.001567 | 0.1221 | 0.0128 | 0.0197 |
| Sirius A | 24.74 | 2.063 | 12.0 | 18.4 |

</div>

For main-sequence stars between about 0.43 and 2 solar masses,
luminosity rises roughly as the fourth power of mass
[Mass-Luminosity Relation][ref_mass_luminosity_relation],
so the factor $L/M$ rises roughly as the cube of mass.
For a given sail the lightness number at another star follows from its value at the Sun,
with $L$ and $M$ in solar units,
and on that part of the main sequence it scales with stellar mass as follows.

$$
\beta_{\ast} = \beta_{\odot}\,\frac{L}{M}, \qquad
\beta_{\ast} \propto M^{3}\quad\left(0.43 < M < 2\right)
\tag{21}
$$

A sail is about 78 times weaker around Proxima Centauri than around the Sun,
and 12 times stronger around Sirius A.
Solar sailing is a technique for bright stars,
and nearly useless around red dwarfs.

## Spacecraft with Different Quality Sails

A sail's quality has several dimensions.
The most important is the loading,
which includes the payload and structure as well as the film.
The others are reflectance,
which sets both thrust and heating,
flatness,
the maximum temperature the materials tolerate,
and durability.
A film whose optical properties degrade in space flies a different trajectory,
and such trajectories have been analysed for a sail facing the Sun
[Bassetto et al. 2020][research_bassetto_et_al_2020].

### Sails That Have Flown or Been Designed

The table gives the ideal lightness number of several real and designed sails.
For the flown craft it divides the whole spacecraft mass by the sail area,
so it is an upper bound on performance.
IKAROS had a launch mass of about 310 kilograms and a membrane spanning 20 metres
[Mori and IKAROS Demonstration Team 2011][research_mori_et_al_2011].
The membrane is square with that span as its diagonal
[IKAROS][ref_ikaros],
which is 200 square metres.
NanoSail-D2 had a mass of 4 kilograms
[NanoSail-D2][ref_nanosail_d2],
and ACS3 a mass of 16 kilograms
[Solar Sail][ref_solar_sail].
The design values for the square sail,
the heliogyro
and the lattice sailer are as listed in Wikipedia's table,
which excludes payload
[Solar Sail][ref_solar_sail],
and the graphene-class loading is the value assumed by Heller and Hippke
[Heller and Hippke 2017][research_heller_hippke_2017].

<div style="overflow-x: auto;" markdown="1">

| Craft or design | Loading, g/m² | Lightness number |
|---|---|---|
| IKAROS, flown 2010 | 1,550 | 0.00099 |
| NanoSail-D2, flown 2011 | 400 | 0.0038 |
| ACS3, flown 2024 | 200 | 0.0077 |
| Square sail design, without payload | 5.27 | 0.26 |
| Heliogyro design, without payload | 6.39 | 0.22 |
| Lattice sailer design, without payload | 0.07 | 20 |
| Graphene-class sail | 0.00076 | about 2,000 |

</div>

The design values from Wikipedia match an efficiency of 90 percent,
which Wikipedia gives as typical of an actual sail
[Solar Sail][ref_solar_sail],
and this is why they are slightly below the ideal values of 0.29 and 0.24 for the first two.
The flown sails are demonstrators whose lightness numbers are hundreds of times below those of the designs.

The loading that matters is that of the whole craft.
A sail of loading $\sigma_{s}$ and area $A$ carrying a payload $m_{\mathrm{pay}}$ has the total loading below,
so reaching a target lightness number $\beta$ with an ideal sail needs at least the following area.

$$
\sigma = \sigma_{s} + \frac{m_{\mathrm{pay}}}{A}, \qquad
A = \frac{m_{\mathrm{pay}}}{\sigma^{\ast}/\beta - \sigma_{s}}
\tag{22}
$$

A 10 kilogram payload on a sail of the square-sail design loading of 5.27 grams per square metre needs 996 square metres for $\beta = 0.1$ and 4,190 for $\beta = 0.2$.
No area suffices once $\sigma^{\ast}/\beta$ falls to $\sigma_{s}$,
so the film alone caps the lightness number at $\sigma^{\ast}/\sigma_{s}$.

### What Each Class of Sail Can Do

The lightness number divides sails into classes by what they can do.

- **Below about 0.01.** Orbit raising and slow spirals. At $\beta = 0.01$ the spiral formula gives 12.1 years from Earth's orbit to Mars's and 150 years to Jupiter's.
- **About 0.01 to 0.1.** Interplanetary transfers in years. At $\beta = 0.05$ the formula gives 2.4 years from Earth's orbit to Mars's and 2.1 years inward to Mercury's.
- **About 0.1 to 0.5.** Fast transfers, close passes to the Sun with large gains in energy, and orbits that gravity alone cannot produce.
- **One half to one.** Escape from the solar system directly from a circular orbit. At $\beta = 0.75$ the final speed is 21.1 kilometres per second from 1 AU and 66.6 from 0.1 AU.
- **Exactly one.** A face-on sail feels no net force and can hover in place, the idea behind the statite proposed independently by Robert Forward and Colin McInnes [Statite][ref_statite] [Forward 1991][research_forward_1991] [McInnes and Simmons 1992][research_mcinnes_simmons_1992].
- **Above one.** The star repels a face-on sail. This allows the fastest departures and, as shown below, braking at another star.

A numerical integration checks the spiral formula.
Starting from a circular orbit at 1 AU with the sail held at a cone angle of 35.26 degrees,
it gives 11.83 years to Mars's orbit and 10.55 years inward to Mercury's at $\beta = 0.01$,
against 12.14 and 10.46 from the formula.
At $\beta = 0.05$ it gives 2.06 and 2.16 years,
against 2.43 and 2.09.
The formula is good to a few percent at small lightness numbers and worsens as $\beta$ grows,
because it ignores the eccentricity that the sail's radial push gives the orbit.

### Heat Limits by Quality

Temperature limits how close any sail can go to its star.
Take an illustrative sail with $\rho = 0.9$,
a front emissivity of 0.05
and a back emissivity of 0.6,
values assumed here rather than measured.
Face-on,
it reaches 247 K at 1 AU,
450 K at 0.3 AU,
780 K at 0.1 AU
and 1,143 K at 10 solar radii.
If its materials tolerate 400 K it can approach no closer than 0.38 AU,
and if they tolerate 600 K no closer than 0.17 AU.
Combining the closest distance $q_{\min}$ with the departure speed from a close pass,
in the limit of an orbit pumped to escape,
gives the fastest departure a sail of loading $\sigma$ can make from any star,
which depends on the star only through its luminosity.

$$
v_{\infty,\max}^{2} = \frac{2\beta\,G M}{q_{\min}} = \frac{2}{c\,\sigma}\sqrt{\frac{F_{\max}\,L}{\pi}}
\tag{23}
$$

Close passes are where a sail gains the most energy,
so heat tolerance is as much a part of sail quality as loading.
A trajectory study for the Solar Polar Imager shows the effect.
With a film temperature limit of 100 degrees Celsius the optimal transfer took 6.4 years,
and with a limit of 240 degrees Celsius it approached the Sun to about 0.22 AU and was shorter still
[Dachwald et al. 2006][research_dachwald_ohndorf_wie_2006].

## Levels of Steering

Steering a sail means turning it.
Attitude control works by shifting the sail's centre of pressure relative to the craft's centre of mass,
which can be done with control vanes,
by moving individual sails,
by moving a control mass,
or by altering reflectivity
[Solar Sail][ref_solar_sail].
Wie emphasized spin stabilization and set out three-axis approaches with a gimbaled control boom,
control vanes,
or shifting and tilting of the sail,
designing against an uncertain offset of 0.1 metre between the centres of mass and pressure on a 40 metre sail
[Wie 2004a][research_wie_2004a]
[Wie 2004b][research_wie_2004b],
and later analysed thrust vector control for sailcraft
[Wie 2007][research_wie_2007].
NEA Scout was designed to manage momentum with a mechanism that moves mass
[McNutt et al. 2014][research_mcnutt_et_al_2014].
IKAROS steered by varying the reflectance of 80 liquid crystal panels embedded in its sail
[IKAROS][ref_ikaros].
Funase and coauthors report on-orbit verification of a fuel-free attitude control system for a spinning solar sail that uses solar radiation pressure
[Funase et al. 2011][research_funase_et_al_2011],
and spinning sails of that kind have been modelled with reflectivity control
[Furumoto et al. 2014][research_furumoto_funase_yamaguchi_2014].
LightSail 2 used a single-axis momentum wheel and magnetic torque rods,
and performed two 90-degree slews each orbit to harness solar momentum
[Spencer et al. 2021][research_spencer_et_al_2021].
In interplanetary space the required orientation often changes by less than a degree per day,
but in planetary orbit it changes much faster
[Solar Sail][ref_solar_sail].
Four levels of steering capability can be distinguished.

### No Control

A sail that tumbles is pushed in a direction that wanders with its attitude,
and its average thrust is smaller and unpredictable.
LightSail 2 spent a significant amount of its time tumbling randomly
[LightSail][ref_lightsail].
Such a craft can still be pushed but cannot be navigated.

### Fixed Face-On

A sail that is kept facing its star,
for example by passive design or by spin,
feels only a radial force.
A radial force exerts no torque about the star,
so the craft's angular momentum about the star cannot change.
Its orbit is an ordinary conic section around a star of reduced gravity $(1-\beta)GM$.
Such a sail cannot spiral inward or outward,
cannot pump energy over repeated passes,
and cannot change its orbital plane.
It can only escape,
if $\beta \geq 1/2$ on a circular orbit,
or hover,
if $\beta = 1$.

### Steering Within the Orbital Plane

A sail that can set its cone angle in the orbital plane can add or remove angular momentum,
and so spiral outward or inward,
pump energy near each close pass,
and reverse the direction of its orbit.
Vulpetti studied trajectories that reverse a sail's orbital angular momentum to reach high speeds
[Vulpetti 1997][research_vulpetti_1997]
and generalized them to three dimensions
[Vulpetti 1999][research_vulpetti_1999].
This is the minimum steering needed for most interplanetary missions.

### Full Three-Axis Steering

A sail that can also set its clock angle can push out of its orbital plane.
It can change its inclination,
reach polar orbits around its star,
and hold orbits displaced from those gravity allows.
Edge-on is the closest thing to off.
An ideal flat sail edge-on to the light feels no force,
so steering to 90 degrees switches the sail off,
but only as precisely as the attitude is controlled
and only to the extent the sail is flat.

## Fixed, Jettisonable and Retractable Sails

Whether a sail can be removed or reduced matters as much as whether it can be steered,
because $\beta$ appears in every result above.
There are three cases.

**Fixed.**
A sail that cannot be removed keeps its lightness number for the whole mission.
The craft can never follow a pure gravitational orbit,
except by turning edge-on.
This is acceptable for $\beta < 1$,
but for $\beta > 1$ it has a decisive consequence shown in the section on capture.

**Jettisonable.**
A sail that can be cut loose has a one-way switch from $\beta$ to zero.
Jettisoning after acceleration removes the sail's mass from the rest of the mission,
and jettisoning before arrival protects the payload from the sail's forces,
but the craft then has no means of braking with light.

**Retractable.**
A sail that can be reefed or rolled in has a lightness number that can be set between zero and its full value,
through $A(t)$ in the equation of motion.
This allows coasting on gravitational orbits,
stowing the sail away from heat,
and fine control of the push.
Retracting does not cool a deployed sail,
because the temperature equation does not depend on area,
but fully stowing it can shade it.

Retraction has been demonstrated on the ground.
Furuya and Satou developed folding and retraction mechanisms for a spinning sail membrane,
using a wrapping fold with tensile forces
[Furuya and Satou 2008][research_furuya_satou_2008].
Banik and Ardelean tested a 10 metre retractable sail prototype,
which they called the Flexible Unfurlable and Refurlable Lightweight sail,
through four thermal cycles and 50 deployment and retraction cycles in thermal vacuum,
and a further 25 cycles in ambient conditions
[Banik and Ardelean 2010][research_banik_ardelean_2010].
Retraction may also be dynamically harder than deployment.
For a simplified sail quadrant on two booms,
Vatankhahghadim and Damaren showed that uniform extension decreases the system's vibrational energy
while uniform retraction increases it
[Vatankhahghadim and Damaren 2018][research_vatankhahghadim_damaren_2018].
The work cited here describes ground tests and analysis,
and none reports a retraction in flight.

## Folding and Deploying a Sail

A sail must be packed small for launch and spread flat in space,
and this is one of the hardest practical problems in solar sailing.

### Thin Films

The most common material in current designs is an aluminium coating on a polymer film,
such as aluminized Kapton 2 micrometres thick
[Solar Sail][ref_solar_sail].
NASA's Near Earth Asteroid Scout and ACS3 needed metallized membranes 2 to 3 micrometres thick
[Stohlman et al. 2020][research_stohlman_et_al_2020].
Stohlman and coauthors report that such membranes do not retain creases as thicker membranes do,
and that for small spacecraft the stowed volume rather than the mass is often the driving requirement
[Stohlman et al. 2020][research_stohlman_et_al_2020].
The solid volume of a film is only its area times its thickness,
which is 0.2 litres for 80 square metres at 2.5 micrometres
and 2,500 litres for a square kilometre.

$$
V_{\mathrm{solid}} = A\,t_{\mathrm{film}}
\tag{24}
$$

Folded film cannot be packed to its solid volume,
so the real stowed volume is larger by a packing factor that depends on the fold pattern.

### Fold Patterns

The fold pattern controls how compactly a sail packs,
how reliably it deploys,
and how flat it lies afterwards.
A rotationally skew fold proposed for spinning sails deploys stably with easy packaging,
although it needs slightly higher spin rates for full deployment
[Furuya and Masuoka 2004][research_furuya_masuoka_2004].
A piecewise straight fold approximates a spiral fold with straight lines to achieve high packaging efficiency with simple folding
[Satou et al. 2014][research_satou_et_al_2014].
The Miura fold,
from origami,
has been used to pack large solar panel arrays for Japanese satellites
[Miura Fold][ref_miura_fold].
IKAROS used a square membrane of 7.5 micrometre polyimide,
20 metres on the diagonal,
deployed by the centrifugal force of the spinning spacecraft from a wrapping fold chosen for stable deployment
[Furuya et al. 2011][research_furuya_et_al_2011].

### Damage from Folding

Folds leave marks.
Seefeldt and Dachwald examined the fold lines of a 7.5 micrometre polyimide membrane under a microscope
and found that light reflected inside a fold line can raise the local temperature.
The membrane geometry allows no more than two reflections even at small tension,
and the resulting temperature rise is slight and depends on the material
[Seefeldt and Dachwald 2021][research_seefeldt_dachwald_2021].
Creases also prevent the sail from lying perfectly flat,
which reduces and redirects its thrust.

### Deployment Failures

Deployment has failed in flight.
The Russian Znamya 2.5 space mirror,
a 25 metre reflector deployed in February 1999,
caught on an antenna of its Progress spacecraft and tore,
and it was deorbited
[Znamya][ref_znamya].
NanoSail-D2 was to be ejected from its carrier satellite in December 2010,
but it ejected on its own only in January 2011 and deployed its sail three days later
[NanoSail-D2][ref_nanosail_d2].
ACS3 unfolds its 80 square metre sail on four 7 metre carbon fibre booms that roll up for storage,
and in October 2024 a bent boom was reported to have made it lose direction and spin
[Solar Sail][ref_solar_sail].

### The Thinnest Sails Cannot Be Folded

The highest-performing sails may not be foldable at all.
Eric Drexler made aluminium films 30 to 100 nanometres thick without a polymer backing,
which could reach accelerations far above those of plastic films,
but the material was too delicate to survive folding,
launch
and deployment,
and the design relied on producing the film in space
[Solar Sail][ref_solar_sail].
The materials needed for laser-driven lightsails pose further challenges
[Atwater et al. 2018][research_atwater_et_al_2018].
The physics thus sets up a tradeoff.
Thinner films raise $\beta$,
but they are harder to fold,
and the thinnest ones can only be made where they will be used.
This inference suggests that the best sails would be manufactured in space rather than launched.

## Other Considerations

A thorough treatment includes several further effects.

- **Close approaches.** Near the star the inverse square law fails because the disc is finite, and the temperature limits above set the closest pass.
- **Degradation.** If a sail's reflectance falls over time, its lightness number and the direction of its force drift with it, as the generalized force model shows.
- **Light from other sources.** A sail can be pushed by a laser instead of a star. Breakthrough Starshot proposed lasers with a combined output of up to 100 gigawatts to push light sails to between 15 and 20 percent of light speed [Breakthrough Starshot][ref_breakthrough_starshot], a programme modelled as a system by Parkin [Parkin 2018][research_parkin_2018], and Heller and Hippke describe high-power lasers accelerating 1 gram sails to 20 percent of light speed within minutes [Heller and Hippke 2017][research_heller_hippke_2017], and Forward analysed round-trip interstellar travel with laser-pushed lightsails [Forward 1984][research_forward_1984].
- **Relativity.** The Doppler factor in the section on where the equations fail matters for any sail moving at several percent of light speed.
- **Surveys.** A state of the art review of solar sail technology [Fu et al. 2016][research_fu_sperber_eke_2016] and a monograph on solar sailing [McInnes 1999b][book_mcinnes_1999] are starting points for further reading.

## Deceleration and Capture at Another Star

A sail launched toward another star arrives at high speed with no propellant.
Heller and Hippke note that a laser-launched probe at 20 percent of light speed could reach Proxima Centauri in 20 years,
but without a way to slow down it would cross the system within hours
[Heller and Hippke 2017][research_heller_hippke_2017].
The target star's own light offers a brake.

### Stopping with Starlight

A sail that faces the target star as it approaches is pushed backward.
If $\beta > 1$,
the star is a net repeller,
and a sail approaching head-on with speed $v_{\infty}$ comes to rest at the distance where its kinetic energy equals the repulsive potential.

$$
\frac{1}{2}v_{\infty}^{2} = \frac{(\beta-1)\,G M}{r_{s}}
\quad\Longrightarrow\quad
r_{s} = \frac{2(\beta-1)\,G M}{v_{\infty}^{2}}
\tag{25}
$$

If the sail must stop no closer than a distance $q$,
set by its heat tolerance or by the star's radius,
the fastest arrival it can stop is the following,
which for $\beta \gg 1$ depends on the star only through its luminosity.

$$
v_{\max} = \sqrt{\frac{2(\beta-1)\,G M}{q}}
\;\approx\;
\sqrt{\frac{(1+\rho)\,L}{2\pi c\,\sigma\,q}}
\tag{26}
$$

This is the same expression that limits the speed a sail can gain by departing from a close pass,
so a sail can stop at another star only from speeds it could also reach by departing from that star.
For the graphene-class loading at Alpha Centauri A,
$\beta$ is about 2,813.
Stopping no closer than 5 stellar radii allows an arrival speed of 13,756 kilometres per second,
which is 4.59 percent of light speed,
and stopping no closer than 10 stellar radii allows 9,727.
Heller and Hippke computed full trajectories that use the light and gravity of Alpha Centauri A and B and Proxima together.
They found a maximum injection speed of about 13,800 kilometres per second at Alpha Centauri A for a sail that is to be parked around Proxima,
a journey of about 95 years from Earth to Alpha Centauri A and B,
and a further 46 years to Proxima,
with a sail of about $10^{5}$ square metres needed for a 10 gram payload
[Heller and Hippke 2017][research_heller_hippke_2017].
At a constant cruise speed $v$ the journey over a distance $d$ takes $d/v$,
and 4.37 light years
[Breakthrough Starshot][ref_breakthrough_starshot]
at 4.6 percent of light speed gives the 95 years quoted.
The near agreement with the 5 radius figure here should not be read as validation,
because the simple bound depends on the chosen $q$ and ignores the deflections their trajectories use.

The same bound shows why the fastest proposed probes cannot stop this way.
Stopping a graphene-class sail arriving at 20 percent of light speed at Alpha Centauri A would require it to come to rest 0.26 stellar radii from the star's centre,
which is inside the star.
Approaching the light also raises the force by the Doppler factor,
about 1.10 at 4.6 percent of light speed and 1.50 at 20 percent,
which helps but does not close a gap of that size.

### Stopping Is Not Capture

A sail that has stopped is not yet in orbit.
With $\beta > 1$ and the sail face-on,
the star still repels it,
so it is pushed back the way it came.
More generally,
the energy of a face-on sail with $\beta > 1$ is $\tfrac{1}{2}v^{2} + (\beta-1)GM/r$,
which is always positive,
so such a sail can never be bound to the star.
Capture requires lowering the effective lightness number below one,
and there are three ways to do so.

- **Tilt.** The radial push of a tilted ideal sail is $\beta\cos^{3}\alpha$ times gravity, which falls below one when $\alpha > \arccos\beta^{-1/3}$. That is 37.5 degrees for $\beta = 2$, 62.3 degrees for $\beta = 10$ and 85.9 degrees for $\beta = 2{,}811$. A very light sail must be held within about four degrees of edge-on.
- **Retract.** Reducing the area by more than a factor $\beta$ does the same, a factor of about 2,800 for the graphene-class sail at Alpha Centauri A.
- **Jettison.** Releasing the sail leaves the payload on a purely gravitational path, which is bound only if it is released where its speed is below local escape speed and with enough sideways motion to miss the star.

The first two conditions,
with $A_{0}$ the full area,
are the following.

$$
\beta\cos^{3}\alpha < 1 \;\Longleftrightarrow\; \alpha > \arccos\beta^{-1/3}, \qquad
\frac{A}{A_{0}} < \frac{1}{\beta}
\tag{27}
$$

A sail approaching exactly head-on has no angular momentum about the star,
so even after its lightness is reduced it would fall straight in.
Capture into an orbit therefore also requires an approach that is offset from the star,
or steering that creates sideways motion before the sail is turned edge-on.
It follows that a fixed,
face-on sail with $\beta > 1$ cannot be captured at all.
Capture needs either steering to nearly edge-on or retraction or a planned jettison,
which is why steerability and retractability are not refinements but requirements for an interstellar sail that is meant to stay.

### Using Several Stars

Multiple star systems offer more than one brake.
Heller,
Hippke
and Kervella found that a photogravitational assist is more effective when the sail passes in front of the star,
using it as a bumper,
than when it swings around behind it as a catapult.
This raises the maximum deceleration at Alpha Centauri A and B
and cuts the travel time of a graphene-class sail from 95 to 75 years.
They also found that Sirius A offers the shortest travel times into a bound orbit among about 22,000 stars within about 300 light years,
69 years if 12.5 percent of light speed can be reached at departure
[Heller et al. 2017][research_heller_hippke_kervella_2017].
That result agrees with the parametric equations,
since Sirius A's $L/M$ of 12.0 makes any sail about 8.6 times lighter there than at Alpha Centauri A.
With the graphene-class loading and a 5 stellar radius limit,
the simple bound gives 47,101 kilometres per second,
or 15.7 percent of light speed.

### Braking Without Starlight

Sails that use the interstellar medium can brake before the starlight becomes useful.
Magnetic sails,
studied for interplanetary travel by Zubrin and Andrews
[Zubrin and Andrews 1991][research_zubrin_andrews_1991],
can create drag against the interstellar medium and so decelerate a craft without propellant,
although feasible uses involve speeds below 10 percent of light speed and take decades
[Magnetic Sail][ref_magnetic_sail],
and Perakis and Hein studied combining magnetic and electric sails for interstellar deceleration
[Perakis and Hein 2016][research_perakis_hein_2016].
A craft could use such a device to shed most of its speed over decades
and a photon sail for the final capture.

## Orbital Manoeuvres with a Solar Sail

The standard orbital manoeuvres are usually described as burns of a given delta-v,
as in the companion article on the subject
[Orbital Manoeuvres in Terms of Delta-v][related_post_orbital_manoeuvres].
A sail can supply delta-v,
but under three constraints that a rocket does not face.
The size of its thrust is fixed by its distance from the star and its angle,
the direction of its thrust is confined to the half of space facing away from the star,
and its total delta-v is limited by time rather than by propellant.
This section explains how a sail performs manoeuvres within those constraints,
gives the mathematics specific to sail steering,
and separates the manoeuvres a particular sail cannot perform from those that no sail can perform.

### How a Sail Performs a Manoeuvre

A rocket chooses its thrust direction freely,
sets its thrust with a throttle,
and spends a finite store of propellant.
A sail has no throttle and no store.
It changes the direction of its thrust by turning,
using the attitude control methods described above,
and it reduces its thrust by tilting toward edge-on or by retracting.
Every textbook burn therefore becomes a long arc of steered thrust.
A Hohmann transfer becomes a spiral,
a plane change becomes a slow twisting of the orbit over many revolutions,
and a capture becomes a gradual matching of orbits.

The delta-v a sail delivers grows with time.
At 1 AU a sail with $\beta = 0.05$ accelerates at 0.297 millimetres per second squared face-on,
which is 25.6 metres per second per day and 9.36 kilometres per second per year.
Held at the 35.26 degree tilt that maximizes the thrust along its orbit,
it delivers 3.60 kilometres per second per year in that direction.
At Mars's distance the same sail delivers only 11.0 metres per second per day face-on,
because the light has weakened by the square of the distance.
In a planet's shadow it delivers nothing.

The rate at which a sail accumulates delta-v along a direction it is steering is the following,
where the factor $f(\theta)$ is the fraction given in the table of the next subsection,
equal to one face-on and 0.385 straight across the sun line.

$$
\frac{d(\Delta v)}{dt} = \beta\,\frac{GM}{r^{2}}\,f(\theta)
\tag{28}
$$

### The Mathematics of Sail Steering

**The force cone.**
For an ideal sail the component of force along the direction from the star is the following.

$$
\vec{F}\cdot\hat{u} = \beta\,\frac{\mu}{r^{2}}\cos^{3}\alpha \;\geq\; 0
\tag{29}
$$

The force always lies within a cone around the direction away from the star.
It can be tilted up to 90 degrees from that direction,
but it shrinks as it tilts and vanishes edge-on.

**The best tilt for a desired direction.**
Suppose the manoeuvre needs as much force as possible along a direction $\hat{d}$ that makes an angle $\theta$ with the direction away from the star,
with $\hat{d}$ and the sail normal in the same plane.
The component along $\hat{d}$ is proportional to $\cos^{2}\alpha\cos(\theta-\alpha)$,
and setting its derivative to zero gives the following condition for the best cone angle.

$$
\tan(\theta - \alpha) = 2\tan\alpha
\tag{30}
$$

For $\theta = 90$ degrees,
a push straight across the sun line,
this gives the familiar 35.26 degrees.
The table gives the largest available component as a fraction of the face-on force.

<div style="overflow-x: auto;" markdown="1">

| Angle of desired direction from the anti-star direction | Best cone angle | Largest component, fraction of face-on force |
|---|---|---|
| 0 degrees | 0 | 1.000 |
| 45 degrees | 15.7 | 0.808 |
| 90 degrees | 35.3 | 0.385 |
| 120 degrees | 51.6 | 0.142 |
| 150 degrees | 70.2 | 0.020 |
| 170 degrees | 83.3 | 0.0008 |
| 180 degrees | none | 0 |

</div>

Directions with a component toward the star are reachable only weakly,
and the direction straight toward the star not at all.

**Rates of change of the orbit.**
Textbook perturbation equations give the rate at which a small force changes each orbital element.
For a nearly circular orbit of radius $r$ and speed $v$,
with $a_{t}$ the acceleration along the velocity,
$a_{h}$ the acceleration normal to the orbital plane,
and $u$ the angle from the ascending node,
the semi-major axis and the inclination change as follows.

$$
\frac{da}{dt} = 2a_{t}\sqrt{\frac{a^{3}}{\mu}}, \qquad
\frac{di}{dt} = \frac{a_{h}\cos u}{v}
\tag{31}
$$

The first gives the spiral time derived earlier.
The second shows that an out-of-plane push changes the inclination only if its sign follows $\cos u$.
A sail that tilts its normal 35.26 degrees out of the plane,
toward one side for half of each orbit and toward the other side for the other half,
switching at the nodes,
averages $|\cos u|$ to $2/\pi$ and changes the inclination per orbit by the following.

$$
\Delta i_{\mathrm{orbit}} = 4\,k\,\beta \approx 1.54\,\beta\ \text{radians}, \qquad k = \cos^{2}\alpha\sin\alpha = 0.385
\tag{32}
$$

That is 0.88 degrees per orbit for $\beta = 0.01$ and 4.41 for $\beta = 0.05$.
A three-dimensional numerical integration over one orbit at 1 AU gives 0.872 and 4.144 degrees,
so the formula is good to 1 percent at the smaller lightness number and 6 percent at the larger,
where the sail's radial thrust also changes the orbit.
A rocket pays for a plane change in delta-v,
while a sail pays in time and in closeness to the star.
Raising the inclination by 90 degrees at 0.4 AU,
where each orbit takes 0.253 years,
takes about 20 orbits or 5.2 years for $\beta = 0.05$.

**Orbits around planets.**
Around a planet the sunlight comes from a direction that is nearly fixed while the spacecraft circles,
so the sail can thrust along its velocity only on part of each orbit.
LightSail 2 performed two 90-degree slews each orbit for this reason
[Spencer et al. 2021][research_spencer_et_al_2021].
Even ignoring that loss and the shadow,
a sail with the ACS3 class acceleration of 0.045 millimetres per second squared would need at least 5.4 years of thrust along its velocity to spiral from low Earth orbit to escape,
since the slow spiral costs about the 7.73 kilometres per second of the orbital speed.
The bound is the spiral delta-v divided by the characteristic acceleration,
using the low-thrust spiral result
[Orbital Manoeuvres in Terms of Delta-v, Low-Thrust Spirals][related_post_orbital_manoeuvres_spirals].

$$
t_{\mathrm{escape}} \geq \frac{v_{c}}{a_{c}}
\tag{33}
$$

### When a Manoeuvre Is Not Possible for a Given Sail

Many manoeuvres are beyond a particular sail but would be possible for a better one.
These are limitations of the craft.

- **Too little acceleration for the time available.** A planetary capture from an incoming trajectory must happen while the craft is near the planet. Mars's sphere of influence, estimated as $r \approx a(m/M)^{2/5}$ [Sphere of Influence][ref_sphere_of_influence], has a radius of about 577,000 kilometres. Crossing it at 2.65 kilometres per second takes 5.0 days, in which a sail with $\beta = 0.05$ can change its velocity by at most 56 metres per second, and even one with $\beta = 1$ by 1.1 kilometres per second. A sail cannot be captured from such an approach. It must first match the planet's orbit around the Sun by spiralling, so that it arrives with almost no excess speed, and then spiral in.
- **Forces stronger than the light.** In low orbit, air drag competes with the light pressure. LightSail 2's controlled thrust measurably reduced its rate of orbital decay [Spencer et al. 2021][research_spencer_et_al_2021], yet the craft still decayed and re-entered in November 2022 [Mansell et al. 2023][research_mansell_et_al_2023] [LightSail][ref_lightsail]. Mansell and coauthors report that later refinements to its attitude control achieved sustained net increases in orbital energy before the deorbit in late 2022. On a planet's surface, gravity is the competing force. With the Sun overhead and no atmosphere, a sail can lift itself only if its total loading is below about 0.00093 grams per square metre on Earth, 0.0011 on Mars, 0.0056 on the Moon, 0.0042 on Ceres and 0.016 on Mercury. The graphene-class loading of 0.00076 grams per square metre carries no payload, and Earth and Mars have atmospheres, so no sail flown or designed can lift a payload from any of these bodies. Only a graphene-class sail with nothing attached could lift itself from the airless ones.
- **Too little steering.** A sail that only faces its star cannot change its angular momentum or its plane. One that steers only in its orbital plane cannot change its inclination.
- **Too much lightness to stay.** A face-on sail with $\beta > 1$ cannot be bound to a star, as the section on capture shows, unless it can turn nearly edge-on, retract or jettison its sail.
- **Too little heat tolerance.** The closest approach, and with it the largest thrust and the fastest departures, are set by the temperature limit.
- **Too far from the star.** The thrust falls as the inverse square of distance, and the spiral time grows as the orbital period. A manoeuvre that changes the orbit by the same proportion and takes a year at 1 AU takes about 164 years at 30 AU, near Neptune's distance, by the $r^{3/2}$ scaling of the spiral formula.

Two of these limits have simple forms.
A sail crossing a sphere of influence of radius $r_{\mathrm{SOI}}$,
defined in the companion article on manoeuvres
[Orbital Manoeuvres in Terms of Delta-v, Patched Conics][related_post_orbital_manoeuvres_patched],
at excess speed $v_{\infty}$ can change its velocity by at most the first expression below,
and a sail can lift itself from a surface of gravity $g$ under a flux $S$ only below the loading in the second.

$$
\Delta v_{\max} \approx \beta\,\frac{GM}{r^{2}}\cdot\frac{2\,r_{\mathrm{SOI}}}{v_{\infty}}, \qquad
\sigma_{\max} = \frac{2S}{c\,g}
\tag{34}
$$

### Manoeuvres No Sail Can Perform

Some manoeuvres are impossible for any sail driven by starlight,
because they would violate the conservation of momentum or energy.

**Pushing toward the star.**
Light from a distant star arrives travelling directly away from it.
A stationary sail that reflects a photon cannot send it back with a larger component of momentum along that direction than it arrived with,
because reflection does not change the photon's energy.
Absorbed light pushes along the same direction.
The sail could re-radiate absorbed energy as heat preferentially from its far side,
which pushes it toward the star,
but the momentum carried away is at most the radiated power divided by $c$,
and in steady state the radiated power cannot exceed the absorbed power.
At best the re-emission cancels the push of the absorbed light.
With $P_{\mathrm{abs}}$ the absorbed power and $P_{\mathrm{emit}} \leq P_{\mathrm{abs}}$ the re-radiated power,
and with reflection contributing only a non-negative term,
the component of force along the direction away from the star obeys the following.

$$
\vec{F}\cdot\hat{u} \;\geq\; \frac{P_{\mathrm{abs}}}{c} - \frac{P_{\mathrm{emit}}}{c} \;\geq\; 0
\tag{35}
$$

So the net force on a sail never has a component toward a distant point source.
It follows that a sail cannot hold an orbit faster than the local circular speed,
cannot hover closer to the star than its lightness allows,
and cannot add to the star's gravity.
A sail can still move toward its star,
but only by spiralling in after losing angular momentum,
never by being pushed there.
Very close to a star the light arrives from a disc rather than a point,
and this argument then applies to the disc as a whole rather than to its centre.

**Pushing without light.**
A starlight sail produces no force in a planet's shadow,
and none in interstellar space far from any star.
It therefore cannot brake during an interstellar cruise,
cannot manoeuvre while eclipsed,
and cannot change course in the dark between stars.

**Manoeuvres faster than any known material allows.**
Strictly this is a limit of materials rather than of physics,
but no known sail can overcome it.
The graphene-class sail with no payload accelerates at 11.9 metres per second squared at 1 AU,
about 1.2 times Earth's surface gravity,
and every real sail with a payload accelerates far less.
A textbook impulsive burn,
kilometres per second in seconds or minutes,
is beyond any known sail at any distance where it would survive the heat.

## Solar Sailing with Secondary Propulsion

Every manoeuvre a sail cannot perform needs momentum from a source other than starlight.
Five sources are known.
These are reaction mass expelled by an engine,
the gravity of a planet during a flyby,
an atmosphere,
plasma or magnetic fields,
and a beam of light from a direction other than the star.
This section matches each impossible manoeuvre to what would physically make it possible.

### Limits of the Craft That a Better Sail Could Remove

Some limitations call for a better sail rather than a second engine.

- **Steering.** Vanes, movable masses, movable sail panels and reflectivity control give a sail the steering it needs [Solar Sail][ref_solar_sail], and three-axis control allows plane changes.
- **Capture with $\beta > 1$.** Retraction, near edge-on control or a planned jettison removes the obstacle, as the section on capture shows.
- **Low acceleration.** Thinner films, lower structural mass and manufacture in space raise $\beta$.
- **Heat.** Coatings with higher back emissivity allow closer passes.

In practice small thrusters may still be the cheaper way to provide fine attitude control or to stabilize a sail during deployment,
but the manoeuvres themselves remain within the reach of sailing.
Attitude control in a planet's shadow is an exception within this group.
Momentum wheels can hold attitude there,
but they eventually need to shed stored momentum,
which takes torque from outside.
LightSail 2 controlled its attitude with magnetic torque rods as well as a momentum wheel
[Spencer et al. 2021][research_spencer_et_al_2021].

### Limits of Solar Sailing Itself

The following limitations remain for any sail,
so a second means of propulsion is physically required.

<div style="overflow-x: auto;" markdown="1">

| Manoeuvre | Why a sail cannot do it | What is physically needed |
|---|---|---|
| Thrust toward the star, or an orbit faster than local circular speed | Reflected and re-radiated light cannot push toward its source | Reaction mass from an engine, or a planetary flyby |
| Braking or course changes during interstellar cruise | No usable starlight | Drag on the interstellar medium from a magnetic sail, a beam from home, or an engine |
| Arriving faster than starlight can stop | The stopping distance falls inside the star | Prior braking by a magnetic or electric sail, or an engine |
| Capture at a planet from a fast approach | Kilometres per second needed within days | An engine burn, or aerocapture in an atmosphere |
| Landing on or launching from a planet or moon | Gravity, and often air, exceeds any sail's push with payload | An engine, or a launcher on the surface |
| Reaching a starting orbit above the atmosphere | Air drag in low orbit can exceed the light pressure | A launch vehicle or a kick stage |
| Final approach and docking | Thrust too weak and too slow to correct quickly | Small thrusters |
| Manoeuvres in a planet's shadow | No light | An engine, or waiting for sunlight |

</div>

Each entry follows from the physics above.
A planetary flyby is a natural partner for a sail,
because it alters the path and speed of a spacecraft without propellant
[Gravity Assist][ref_gravity_assist]
during a single pass,
which a sail cannot match.
Heller,
Hippke
and Kervella combined the two in photogravitational assists at Alpha Centauri
[Heller et al. 2017][research_heller_hippke_kervella_2017].
Magnetic sails can create drag against the interstellar medium and decelerate without propellant
[Magnetic Sail][ref_magnetic_sail],
and combined magnetic and electric sails have been studied for interstellar deceleration
[Perakis and Hein 2016][research_perakis_hein_2016].
Within a planetary system,
optimal rendezvous trajectories that combine an electric sail with a high-thrust engine have also been studied
[Quarta et al. 2011][research_quarta_mengali_janhunen_2011].
A beam from home can drive a sail where starlight is too weak,
and Forward analysed round-trip interstellar travel with laser-pushed lightsails
[Forward 1984][research_forward_1984].
Aerocapture uses a single pass through an atmosphere to shed speed,
as an earlier article on this site describes
[Introduction to Space Studies][related_post_space_studies].

### The Cost of Carrying a Second Engine

A secondary engine obeys the rocket equation,
and to that engine the sail is dead mass.
With a dry mass $m_{d}$,
a sail of mass $m_{s}$
and propellant $m_{p}$,
an engine of exhaust speed $v_{e}$ provides the following delta-v,
which is the rocket equation of the companion article on manoeuvres
[Orbital Manoeuvres in Terms of Delta-v, The Rocket Equation][related_post_orbital_manoeuvres_rocket]
with the sail counted as dry mass.

$$
\Delta v = v_{e}\ln\frac{m_{d} + m_{s} + m_{p}}{m_{d} + m_{s}}
\tag{36}
$$

Jettisoning the sail before a large burn removes $m_{s}$ from both terms and raises the delta-v,
which is the mass-shedding effect described in the companion article on manoeuvres,
at the price of losing the sail for the rest of the mission.
Conversely,
propellant and engines raise the sail loading and lower $\beta$ for the whole mission.
A hybrid design therefore uses its engine only for the few manoeuvres a sail cannot perform.
A sail can also be a power source.
IKAROS carried thin-film solar cells on its sail membrane to demonstrate power generation from the sail
[Mori and IKAROS Demonstration Team 2011][research_mori_et_al_2011],
and the same area could in principle power an electric engine,
an inference not tested by any source cited here.

## A Review of the Literature

The literature cited here spans five decades,
from mission proposals of the 1970s to the materials science of laser-driven sails.
This section surveys it by topic.
Each work is described according to its published abstract,
or by its subject alone where it is cited for its title.

### Reviews and Monographs

McInnes wrote a monograph on solar sailing
[McInnes 1999b][book_mcinnes_1999].
Reviews cover science mission applications
[Macdonald and McInnes 2011][research_macdonald_mcinnes_2011],
the state of the technology
[Fu et al. 2016][research_fu_sperber_eke_2016]
[Gong and Macdonald 2019][research_gong_macdonald_2019],
and the photonic materials needed for the next generation of sails,
for missions ranging from interstellar travel to imaging the poles of the Sun,
with a roadmap for their development
[Davoyan et al. 2021][research_davoyan_et_al_2021].

### Early Mission Studies and Optimal Trajectories

Wright and Warmke described solar sail mission applications in 1976,
including the delivery of large payloads throughout the solar system without propellant
[Wright and Warmke 1976][research_wright_warmke_1976].
Sauer optimized interplanetary sail trajectories by the calculus of variations,
for rendezvous with Venus,
Mars
and Mercury and for an asteroid round trip
[Sauer 1976][research_sauer_1976].
Dachwald noted that conventional optimizers depend strongly on a good initial guess,
and showed that evolutionary neurocontrol found steering strategies closer to the global optimum
for missions to a near-Earth asteroid,
to Mercury
and past Pluto
[Dachwald 2004][research_dachwald_2004].
Mengali and Quarta computed optimal three-dimensional rendezvous trajectories with a non-ideal sail
[Mengali and Quarta 2005][research_mengali_quarta_2005].

### Force Models, Materials and Degradation

The refined force model of Mengali and coauthors
[Mengali et al. 2007][research_mengali_et_al_2007]
and Swartzlander's diffractive sail
[Swartzlander 2017][research_swartzlander_2017]
extend the ideal model used in this article.
Kezerashvili and Matloff analysed the effects of the space environment on sails microscopically
[Kezerashvili and Matloff 2009][research_kezerashvili_matloff_2009],
and the effect of optical degradation on mission performance has been studied
[Dachwald et al. 2007][research_dachwald_et_al_2007]
along with trajectories of a degrading sail that faces the Sun
[Bassetto et al. 2020][research_bassetto_et_al_2020].

### Non-Keplerian Orbits and Statites

Forward proposed the statite,
a spacecraft that does not orbit
[Forward 1991][research_forward_1991].
McInnes and Simmons studied heliocentric halo orbits for sails
[McInnes and Simmons 1992][research_mcinnes_simmons_1992],
McInnes studied sail trajectories at the lunar second Lagrange point
[McInnes 1993][research_mcinnes_1993],
passive control of displaced orbits
[McInnes 1998][research_mcinnes_1998]
and mission applications of non-Keplerian orbits
[McInnes 1999a][research_mcinnes_1999b],
Bookless and McInnes studied control of Lagrange point orbits by sail
[Bookless and McInnes 2008][research_bookless_mcinnes_2008],
and Heiligers and McInnes studied heliocentric orbits that follow Earth
[Heiligers and McInnes 2015][research_heiligers_mcinnes_2015].

### Solar Polar, Close-Perihelion and Fast Missions

Macdonald and coauthors presented a solar polar orbiter as a technology reference study
[Macdonald et al. 2006][research_macdonald_et_al_2006],
and Dachwald,
Ohndorf
and Wie optimized trajectories for the Solar Polar Imager,
a 160 metre square sail with a characteristic acceleration of 0.35 millimetres per second squared
[Dachwald et al. 2006][research_dachwald_ohndorf_wie_2006].
For fast missions to the outer solar system,
Vulpetti developed angular momentum reversal trajectories
[Vulpetti 1997][research_vulpetti_1997]
[Vulpetti 1999][research_vulpetti_1999].
The Interstellar Heliopause Probe study
[Lyngvi et al. 2005][research_lyngvi_et_al_2005]
used a photonic assist with two passes at 0.25 AU and a 245 metre sail whose module is ejected after 6.5 years,
so that a 517 kilogram spacecraft reaches 200 AU in 30 years
[Lappas et al. 2005][research_lappas_et_al_2005].
Macdonald,
McInnes
and Hughes studied the technology needed to explore beyond Neptune by sail
[Macdonald et al. 2010][research_macdonald_mcinnes_hughes_2010],
and Ancona,
Kezerashvili
and Matloff studied sun-diving sails for the Kuiper Belt
[Ancona et al. 2019][research_ancona_kezerashvili_matloff_2019].

### Attitude Control and Flight

Wie's two-part study of sail attitude control and dynamics
[Wie 2004a][research_wie_2004a]
[Wie 2004b][research_wie_2004b]
and Wie's analysis of thrust vector control
[Wie 2007][research_wie_2007]
address the attitude control and thrust vector control of sails.
Demonstration missions are described for IKAROS
[Tsuda et al. 2011][research_tsuda_et_al_2011]
[Tsuda et al. 2013][research_tsuda_et_al_2013],
NanoSail-D
[Johnson et al. 2011][research_johnson_et_al_2011],
LightSail 2
[Spencer et al. 2021][research_spencer_et_al_2021],
NEA Scout
[McNutt et al. 2014][research_mcnutt_et_al_2014]
and ACS3
[Wilkie 2021][research_wilkie_2021],
the last two in papers written before launch.

### Laser-Driven Lightsails

Forward analysed round-trip interstellar travel with laser-pushed lightsails
[Forward 1984][research_forward_1984].
Kulkarni,
Lubin
and Zhang derived the relativistic motion of a spacecraft pushed by directed energy,
showed that the diffraction of the beam limits its maximum speed,
and considered recycling photons to go faster
[Kulkarni et al. 2018][research_kulkarni_lubin_zhang_2018].
Parkin built a system model of Breakthrough Starshot
[Parkin 2018][research_parkin_2018].
Manchester and Loeb showed that conical sails on Gaussian beams are unstable without active control,
while a spherical shell can ride the beam without feedback
[Manchester and Loeb 2017][research_manchester_loeb_2017].
Ilic,
Went
and Atwater showed that a laser-driven sail must absorb very little at the laser's near-infrared wavelength
yet emit strongly in the mid-infrared to cool itself,
and defined a reflectivity-adjusted area density as a figure of merit
[Ilic et al. 2018][research_ilic_went_atwater_2018].
Ilic and Atwater studied self-stabilizing photonic levitation and propulsion
[Ilic and Atwater 2019][research_ilic_atwater_2019],
Michaeli and coauthors measured radiation pressure directly on lightsail membranes
[Michaeli et al. 2025][research_michaeli_et_al_2025],
and Atwater and coauthors set out the materials challenges for the Starshot sail
[Atwater et al. 2018][research_atwater_et_al_2018].

### Interstellar Arrival

Heller and Hippke showed how the light and gravity of the Alpha Centauri stars can decelerate an incoming sail
[Heller and Hippke 2017][research_heller_hippke_2017],
and Heller,
Hippke
and Kervella extended the analysis to some 22,000 stars
[Heller et al. 2017][research_heller_hippke_kervella_2017].
Magnetic sails
[Zubrin and Andrews 1991][research_zubrin_andrews_1991]
and combined magnetic and electric sails
[Perakis and Hein 2016][research_perakis_hein_2016]
offer braking against the interstellar medium.

### Electric Sails

Janhunen described an electric sail for spacecraft propulsion in 2004
[Janhunen 2004][research_janhunen_2004].
In its developed form it uses long,
thin tethers held at a high positive potential by an electron gun,
whose effective area can be millions of times their physical area,
and its developers expected a sail of 1 newton thrust and 100 kilograms to be buildable in the near future
[Janhunen et al. 2010][research_janhunen_et_al_2010].
Bassetto and coauthors reviewed the concept and its applications
[Bassetto et al. 2022][research_bassetto_et_al_2022],
and Quarta,
Mengali
and Janhunen studied its combination with high-thrust propulsion
[Quarta et al. 2011][research_quarta_mengali_janhunen_2011].

## Epistemic State

**Facts reported by the cited sources.**
The pressure of light,
the definitions of sail loading,
characteristic acceleration
and lightness number,
the sail designs,
the attitude control methods,
the remaining mission details
and the stellar data come from the Wikipedia entries cited,
which draw on mission reports and the peer-reviewed literature,
and the stellar data are attributed to the papers that Wikipedia cites for them.
The findings attributed to Kopp and Lean,
Heller and Hippke,
Heller,
Hippke and Kervella,
the groups led by Spencer
and Stohlman,
Seefeldt and Dachwald,
the groups led by Furuya and Satou,
Banik and Ardelean,
Vatankhahghadim and Damaren,
Mori and coauthors,
Yonetoku and coauthors,
Mansell and coauthors,
and the works of the literature review whose findings are stated,
including those of Wright and Warmke,
Sauer,
Dachwald,
Mengali and coauthors,
Swartzlander,
Davoyan and coauthors,
Dachwald,
Ohndorf and Wie,
Lappas and coauthors,
Wie 2004a,
McNutt and coauthors,
Wilkie,
Kulkarni and coauthors,
Manchester and Loeb,
Ilic,
Went and Atwater,
and Janhunen and coauthors 2010,
are stated according to their published abstracts.
The works of the groups led by Tsuda,
Funase,
Johnson,
Bassetto,
Furumoto,
Atwater
and Fu,
and those of Vulpetti,
Forward,
Zubrin and Andrews,
Perakis and Hein,
and McInnes,
and every other work in the literature review,
are cited only for what their titles state.
The findings attributed to sources rest on their abstracts and titles rather than on their full texts.

**Analysis in this article.**
The force model,
the generalized lightness number,
the reduced gravity,
the escape and departure speeds,
the spiral time,
the temperature limit,
the stopping distance
and the capture conditions are derived here from the stated assumptions.
The force model ignores diffuse reflection and thermal re-emission.
The spiral time is a small-lightness approximation,
checked against a numerical integration.
The stopping bound treats a head-on approach to a single star without relativity,
and the Doppler factor is a first-order estimate.
The best-tilt condition,
the inclination change per orbit,
the minimum spiral time from low Earth orbit,
the lift-off loadings
and the argument that a sail cannot be pushed toward a distant star are derived here.
The inclination formula is checked against a three-dimensional numerical integration.
The sphere of influence of Mars uses the approximate formula from the cited article,
which lists about 578,000 kilometres.
The emissivities and reflectance in the heat example are illustrative assumptions.
The lightness numbers of flown craft are upper bounds computed from total mass and ideal reflection.

**Inference and judgment.**
The classes of sail by lightness number,
the four levels of steering,
the claim that the thinnest sails must be made in space,
the conclusion that interstellar capture requires steering or retraction,
and the division of impossible manoeuvres into limits of the craft and limits of sailing itself are judgments built on the physics above.
The statement that a sail's cells could power an electric engine is an untested inference.
The capture conclusion follows strictly for an ideal face-on sail,
and for real sails it depends on how closely edge-on can be achieved.

**Unaddressed concerns.**
This article does not model billowing,
wrinkling,
sail dynamics,
structural loads,
the interstellar dust that a fast sail would meet,
or communication from another star.

## Out of Scope

This article does not cover laser system design,
the engineering of magnetic or electric sails,
mission costs,
or the choice of a launch site.
Planetary orbits that use solar sails,
such as those around Earth,
are mentioned only where a flown mission illustrates a point.

## Conclusion

A solar sail is pushed by light with a force set by its area,
its reflectance,
its angle to the star
and the star's luminosity,
against a gravity set by the star's mass.
The ratio of the two,
the lightness number,
summarizes almost everything a sail can do,
and it depends on the star only through $L/M$ and on the craft only through its loading and reflectance.
The sails flown so far have lightness numbers below one percent,
designs reach a few tenths without payload,
and only sails far thinner than any yet folded reach one or more.

Steering and retraction decide what a given lightness number buys.
A sail that only faces its star moves on the conics of a weaker star,
one that steers in its orbital plane can spiral and pump energy,
and one that steers in three axes can leave its plane.
At another star,
a sail light enough to brake from interstellar speed is repelled by the star it is braking against,
so it can be captured only if it can turn nearly edge-on,
retract,
or drop its sail at the right moment.
The physical difficulty of folding thin films means that the sails best able to make that journey are also the hardest to build and launch,
which points toward making them in space.


## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 36 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 36, 29 are established and 7 are bespoke.
Fluxes are in watts per square metre and sail loadings are quoted in grams per square metre, so a loading must be converted to kilograms per square metre before it enters an equation with the speed of light, and the star's gravitational parameter appears in two equivalent notations.

**Equation 1, Photon Momentum and Radiation Pressure.**
Light of energy flux S carries momentum flux S over c, so an absorber feels that pressure and a perfect mirror at normal incidence feels twice it.
[Radiation Pressure][ref_radiation_pressure]

$$
p = \frac{E}{c}, \qquad
P_{\mathrm{abs}} = \frac{S}{c}, \qquad
P_{\mathrm{mirror}} = \frac{2S}{c}
\tag{1}
$$

**Equation 2, Dynamic Pressure of the Solar Wind.**
The pressure of the solar wind is its momentum flux, the product of the proton number density, the proton mass and the square of the wind speed.
[Solar Wind][ref_solar_wind]

$$
P_{\mathrm{sw}} = n\,m_{p}\,V^{2}
\tag{2}
$$

**Equation 3, Force on a Perfectly Reflecting Flat Sail.**
A flat mirror intercepts light over its projected area and is pushed along its normal by twice the normal component of the intercepted momentum, which gives a force proportional to the square of the cosine of the cone angle.

$$
\vec{F} = \frac{2 S A}{c}\cos^{2}\alpha\,\hat{n}
\tag{3}
$$

**Equation 4, Characteristic Acceleration and Lightness Number.**
The characteristic acceleration is that of an ideal sail facing the Sun at one astronomical unit, and the lightness number is its ratio to the Sun's gravity at the same distance.
[Solar Sail][ref_solar_sail]

$$
a_{c} = \frac{2 S_{0}}{c\,\sigma}, \qquad
\beta = \frac{a_{c}}{\mu_{\odot}/(1\ \mathrm{AU})^{2}}
\tag{4}
$$

**Equation 5, Equation of Motion of an Ideal Sail.**
The acceleration of an ideal sail is solar gravity plus a radiation term that is the lightness number times gravity scaled by the square of the cosine of the cone angle.

$$
\ddot{\vec{r}} = -\frac{\mu}{r^{2}}\,\hat{r} + \beta\,\frac{\mu}{r^{2}}\cos^{2}\alpha\,\hat{n}
\tag{5}
$$

**Equation 6, Inverse-Square Flux and Radiation Pressure of a Star.**
A star's luminosity spread over a sphere gives the flux at any distance, and dividing by the speed of light gives the pressure on an absorber.

$$
S(r) = \frac{L}{4\pi r^{2}}, \qquad
P(r) = \frac{L}{4\pi c\,r^{2}}
\tag{6}
$$

**Equation 7, Force on a Partially Reflecting Sail.**
A sail that reflects a fraction of the light specularly and absorbs the rest is pushed along the Sun line by the absorbed part and along its normal by the reflected part, with transmission and diffuse reflection neglected.

$$
\vec{F} = P(r)\,A\cos\alpha\left[(1-\rho)\,\hat{u} + 2\rho\cos\alpha\,\hat{n}\right]
\tag{7}
$$

**Equation 8, Normal and Transverse Force Components and the Force Angle.**
Resolving the force on a partially reflecting sail along its normal and in its plane shows that the net force is tilted from the normal toward the Sun line by an angle that grows with the absorbed fraction.

$$
F_{n} = P A (1+\rho)\cos^{2}\alpha, \qquad
F_{t} = P A (1-\rho)\cos\alpha\sin\alpha, \qquad
\tan\phi = \frac{1-\rho}{1+\rho}\tan\alpha
\tag{8}
$$

**Equation 9, Lightness Number for Any Star.**
The ratio of the face-on radiation force to the star's gravitational pull on the craft is independent of distance and depends on the star only through the ratio of its luminosity to its mass.

$$
\beta = \frac{(1+\rho)\,L}{4\pi c\,G M\,\sigma}
\tag{9}
$$

**Equation 10, Critical Sail Loading.**
The critical loading is the mass per unit area at which a perfectly reflecting face-on sail feels a radiation force exactly equal to the star's gravity.

$$
\sigma^{\ast} = \frac{L}{2\pi c\,G M}
\tag{10}
$$

**Equation 11, General Equation of Motion of a Sail.**
Gravity and the force on a partially reflecting sail of possibly varying area combine into one equation of motion from which the remaining results of the article follow.

$$
\ddot{\vec{r}} = -\frac{G M}{r^{2}}\,\hat{u}
+ \frac{L\,A(t)\cos\alpha}{4\pi c\,m\,r^{2}}\left[(1-\rho)\,\hat{u} + 2\rho\cos\alpha\,\hat{n}(\alpha,\delta)\right]
\tag{11}
$$

**Equation 12, Reduced Gravity of a Face-On Sail.**
A sail held face-on pushes only along the Sun line, so it acts as a reduction of the star's gravitational parameter by the factor one minus the lightness number.

$$
\mu_{\mathrm{eff}} = (1-\beta)\,G M
\tag{12}
$$

**Equation 13, Escape Speed of a Sail Opened on a Circular Orbit.**
Opening the sail reduces the effective gravity by the factor one minus the lightness number, and energy conservation then gives the speed far from the star.

$$
v_{\infty} = v_{c}(r_{0})\sqrt{2\beta - 1}
\tag{13}
$$

**Equation 14, Departure Speed After a Face-On Perihelion Pass.**
A sail that falls under gravity alone to its closest distance and turns face-on there leaves with the excess speed that energy conservation gives under the reduced solar gravity.

$$
v_{\infty} = \sqrt{\frac{2\beta\,G M}{q} - \frac{G M}{a}}
\tag{14}
$$

**Equation 15, Spiral Time at a Fixed Cone Angle.**
Gauss's equation for the rate of change of the orbit's size, applied to a nearly circular orbit at a small lightness number, gives the time to spiral between two radii at a fixed cone angle.

$$
t = \frac{\left|r_{2}^{3/2} - r_{1}^{3/2}\right|}{3\,\beta\,k\,\sqrt{G M}}, \qquad k = \cos^{2}\alpha\sin\alpha
\tag{15}
$$

**Equation 16, Delta-v of a Slow Spiral.**
A slow spiral between circular orbits costs the difference of the two circular speeds, which a sail pays in time rather than in propellant.
[Orbital Manoeuvres in Terms of Delta-v, Low-Thrust Spirals][related_post_orbital_manoeuvres_spirals]

$$
\Delta v_{\mathrm{spiral}} = \left|\sqrt{\frac{GM}{r_{1}}} - \sqrt{\frac{GM}{r_{2}}}\right|
\tag{16}
$$

**Equation 17, Equilibrium Temperature of a Sail.**
A sail element balances the sunlight it absorbs against thermal emission from both faces, so its temperature depends on the flux and the coatings but not on the area or the loading.

$$
T = \left[\frac{(1-\rho)\,S(r)\cos\alpha}{\sigma_{\mathrm{SB}}\left(\varepsilon_{f}+\varepsilon_{b}\right)}\right]^{1/4}
\tag{17}
$$

**Equation 18, Closest Approach Set by a Temperature Limit.**
Inverting the equilibrium temperature at its maximum allowed value gives the largest tolerable flux and therefore the closest distance to the star.

$$
q_{\min} = \sqrt{\frac{L}{4\pi F_{\max}}}, \qquad
F_{\max} = \frac{\sigma_{\mathrm{SB}}\left(\varepsilon_{f}+\varepsilon_{b}\right)T_{\max}^{4}}{1-\rho}
\tag{18}
$$

**Equation 19, First-Order Doppler Reduction of the Force.**
Light reaching a sail receding at a significant fraction of light speed is reduced in both photon energy and arrival rate, which lowers the force by the stated factor to first order.

$$
\frac{F(v)}{F(0)} \approx \frac{1 - v/c}{1 + v/c}
\tag{19}
$$

**Equation 20, Characteristic Acceleration and Lightness Number in Practical Units.**
Evaluating the characteristic acceleration at one astronomical unit with the loading in grams per square metre and an efficiency factor gives the working relations quoted by the cited source.
[Solar Sail][ref_solar_sail]

$$
a_{c} = \frac{9.08\,\eta}{\sigma}\ \mathrm{mm/s^{2}}, \qquad
\beta = \frac{a_{c}}{5.93\ \mathrm{mm/s^{2}}} = \eta\,\frac{\sigma^{\ast}}{\sigma}
\tag{20}
$$

**Equation 21, Lightness Number at Another Star.**
A given sail's lightness number scales with the ratio of the star's luminosity to its mass, which on the middle of the main sequence rises roughly as the cube of the stellar mass through the mass-luminosity relation.
[Mass-Luminosity Relation][ref_mass_luminosity_relation]

$$
\beta_{\ast} = \beta_{\odot}\,\frac{L}{M}, \qquad
\beta_{\ast} \propto M^{3}\quad\left(0.43 < M < 2\right)
\tag{21}
$$

**Equation 22, Total Loading and Required Sail Area for a Payload.**
The loading of the whole craft is the film loading plus the payload spread over the sail area, so a target lightness number fixes the smallest area that can carry a given payload.

$$
\sigma = \sigma_{s} + \frac{m_{\mathrm{pay}}}{A}, \qquad
A = \frac{m_{\mathrm{pay}}}{\sigma^{\ast}/\beta - \sigma_{s}}
\tag{22}
$$

*Equation 23, Bespoke Fastest Departure Limited by Heat Tolerance.*
Combining the closest approach that the temperature limit allows with the close-pass departure in the limit of an orbit pumped to escape gives a ceiling on departure speed that depends on the star only through its luminosity.

$$
v_{\infty,\max}^{2} = \frac{2\beta\,G M}{q_{\min}} = \frac{2}{c\,\sigma}\sqrt{\frac{F_{\max}\,L}{\pi}}
\tag{23}
$$

**Equation 24, Solid Volume of a Film.**
The solid volume of a sail film is its area times its thickness, a lower bound that any fold pattern exceeds by a packing factor.

$$
V_{\mathrm{solid}} = A\,t_{\mathrm{film}}
\tag{24}
$$

*Equation 25, Bespoke Stopping Distance with Starlight.*
A face-on sail with a lightness number above one approaching a star exactly head-on stops where its kinetic energy equals the net repulsive potential, under the stated head-on geometry and a constant face-on attitude.

$$
\frac{1}{2}v_{\infty}^{2} = \frac{(\beta-1)\,G M}{r_{s}}
\quad\Longrightarrow\quad
r_{s} = \frac{2(\beta-1)\,G M}{v_{\infty}^{2}}
\tag{25}
$$

*Equation 26, Bespoke Fastest Arrival That Starlight Can Stop.*
Requiring the head-on stopping distance to be no closer than a chosen limit gives the largest arrival speed a sail can shed, which for a large lightness number depends on the star only through its luminosity.

$$
v_{\max} = \sqrt{\frac{2(\beta-1)\,G M}{q}}
\;\approx\;
\sqrt{\frac{(1+\rho)\,L}{2\pi c\,\sigma\,q}}
\tag{26}
$$

**Equation 27, Conditions for Lowering the Effective Lightness Number Below One.**
The radial push of a tilted ideal sail falls below gravity beyond a cone angle set by the lightness number, and a retracted sail does the same when its area falls by more than that number.

$$
\beta\cos^{3}\alpha < 1 \;\Longleftrightarrow\; \alpha > \arccos\beta^{-1/3}, \qquad
\frac{A}{A_{0}} < \frac{1}{\beta}
\tag{27}
$$

**Equation 28, Rate of Accumulation of Delta-v Along a Steered Direction.**
A sail accumulates delta-v along a chosen direction at the face-on acceleration times the largest fraction of it available in that direction.

$$
\frac{d(\Delta v)}{dt} = \beta\,\frac{GM}{r^{2}}\,f(\theta)
\tag{28}
$$

**Equation 29, Radial Force Component of an Ideal Sail.**
The component of an ideal sail's force along the direction away from the star is never negative, so the force always lies within a cone around that direction.

$$
\vec{F}\cdot\hat{u} = \beta\,\frac{\mu}{r^{2}}\cos^{3}\alpha \;\geq\; 0
\tag{29}
$$

**Equation 30, Optimal Cone Angle for a Desired Thrust Direction.**
Maximizing the component of an ideal sail's force along a direction at a given angle from the anti-star direction gives the stated condition on the cone angle.

$$
\tan(\theta - \alpha) = 2\tan\alpha
\tag{30}
$$

**Equation 31, Gauss Perturbation Equations for a Nearly Circular Orbit.**
A small acceleration along the velocity changes the semi-major axis, and a small acceleration normal to the plane changes the inclination at a rate that follows the cosine of the angle from the ascending node.

$$
\frac{da}{dt} = 2a_{t}\sqrt{\frac{a^{3}}{\mu}}, \qquad
\frac{di}{dt} = \frac{a_{h}\cos u}{v}
\tag{31}
$$

*Equation 32, Bespoke Inclination Change per Orbit Under a Switched Steering Law.*
Tilting the sail normal out of the orbital plane at the cone angle of greatest transverse force and switching sides at each node averages the inclination rate over one orbit, which assumes a nearly circular orbit and this particular steering law.

$$
\Delta i_{\mathrm{orbit}} = 4\,k\,\beta \approx 1.54\,\beta\ \text{radians}, \qquad k = \cos^{2}\alpha\sin\alpha = 0.385
\tag{32}
$$

*Equation 33, Bespoke Lower Bound on Spiral Escape Time from a Planetary Orbit.*
Dividing the slow-spiral cost from a circular orbit to escape by the characteristic acceleration bounds the escape time from below, ignoring the shadow and the part of each orbit in which the sail cannot thrust along its velocity.
[Orbital Manoeuvres in Terms of Delta-v, Low-Thrust Spirals][related_post_orbital_manoeuvres_spirals]

$$
t_{\mathrm{escape}} \geq \frac{v_{c}}{a_{c}}
\tag{33}
$$

*Equation 34, Bespoke Limits on Capture During a Flyby and on Lifting from a Surface.*
The largest velocity change during a crossing of a sphere of influence is the face-on acceleration times the crossing time, and the largest loading that can lift itself is the one whose face-on radiation acceleration equals surface gravity, both bounds the article constructs from earlier results.
[Orbital Manoeuvres in Terms of Delta-v, Patched Conics][related_post_orbital_manoeuvres_patched]

$$
\Delta v_{\max} \approx \beta\,\frac{GM}{r^{2}}\cdot\frac{2\,r_{\mathrm{SOI}}}{v_{\infty}}, \qquad
\sigma_{\max} = \frac{2S}{c\,g}
\tag{34}
$$

*Equation 35, Bespoke Bound on the Sunward Force from a Distant Star.*
Because reflection adds only a non-negative term and steady re-emission cannot exceed absorption, the article's momentum argument shows that the force on a sail never has a component toward a distant point source.

$$
\vec{F}\cdot\hat{u} \;\geq\; \frac{P_{\mathrm{abs}}}{c} - \frac{P_{\mathrm{emit}}}{c} \;\geq\; 0
\tag{35}
$$

**Equation 36, Rocket Equation with the Sail as Dry Mass.**
A secondary engine obeys the rocket equation with the sail counted as part of the dry mass, so carrying the sail lowers the delta-v of every burn.
[Orbital Manoeuvres in Terms of Delta-v, The Rocket Equation][related_post_orbital_manoeuvres_rocket]

$$
\Delta v = v_{e}\ln\frac{m_{d} + m_{s} + m_{p}}{m_{d} + m_{s}}
\tag{36}
$$

### Notation

- $c$, the speed of light
- $S(r)$, the flux of starlight at distance $r$, written $S$ where the distance is understood, with $S_{0}$ the flux at one astronomical unit
- $P(r)$, the radiation pressure on an absorber at distance $r$
- $A$, the area of the sail, with $A_{0}$ the full area of a retractable sail
- $\sigma$, the loading of the whole craft, its total mass per unit area of sail, with $\sigma_{s}$ the loading of the film alone
- $\sigma^{\ast}$, the critical loading at which a perfectly reflecting face-on sail has a lightness number of one
- $a_{c}$, the characteristic acceleration of a sail facing the Sun at one astronomical unit
- $\beta$, the lightness number of a sail, the ratio of the face-on radiation force to the star's gravity
- $\mu$, the gravitational parameter of the star, equal to $GM$, with $\mu_{\odot}$ for the Sun
- $L$, the luminosity of the star, in solar units in Equation 21
- $M$, the mass of the star, in solar units in Equation 21
- $\alpha$, the cone angle between the sail normal and the direction from the star to the sail
- $\hat{n}$, the unit normal of the sail, pointing away from the star, with $\hat{u}$ the unit vector from the star to the sail and $\hat{t}$ the transverse unit vector in the sail's plane
- $\rho$, the specular reflectance of the sail
- $\phi$, the angle between the net force and the sail normal
- $\varepsilon_{f}$, the emissivity of the sail's front face, with $\varepsilon_{b}$ that of its back face
- $\sigma_{\mathrm{SB}}$, the Stefan-Boltzmann constant
- $F_{\max}$, the largest flux a sail tolerates, set by its maximum temperature $T_{\max}$
- $q$, the closest distance of a sail to the star, with $q_{\min}$ the closest the temperature limit allows
- $k$, the transverse force factor $\cos^{2}\alpha\sin\alpha$, which is 0.385 at the cone angle of greatest transverse force
- $v_{\infty}$, the hyperbolic excess speed, the speed far from the star or planet
- $r_{s}$, the distance at which a sail approaching head-on comes to rest
- $\eta$, the efficiency of a real sail relative to an ideal one
- $a_{t}$, the acceleration along the velocity, with $a_{h}$ the acceleration normal to the orbital plane and $u$ the angle from the ascending node
- $f(\theta)$, the largest fraction of the face-on force available along a direction at angle $\theta$ from the anti-star direction
- $m_{p}$, the proton mass in Equation 2 and the propellant mass in Equation 36, with $m_{d}$ the dry mass and $m_{s}$ the sail mass
- $v_{e}$, the exhaust speed of a secondary engine

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Akeson, Rachel, Charles Beichman, Pierre Kervella, Edward Fomalont, and G. Fritz Benedict. 2021. "Precision Millimeter Astrometry of the α Centauri AB System." *Astronomical Journal* 162 (1): 14. [https://doi.org/10.3847/1538-3881/abfaff][research_akeson_et_al_2021]
- Ancona, Elena, Roman Ya Kezerashvili, and Gregory L. Matloff. 2019. "Exploring the Kuiper Belt with Sun-Diving Solar Sails." *Acta Astronautica* 160: 601–5. [https://doi.org/10.1016/j.actaastro.2019.02.019][research_ancona_kezerashvili_matloff_2019]
- Atwater, Harry A., Artur R. Davoyan, Ognjen Ilic, et al. 2018. "Materials Challenges for the Starshot Lightsail." *Nature Materials* 17 (10): 861–67. [https://doi.org/10.1038/s41563-018-0075-8][research_atwater_et_al_2018]
- Bassetto, Marco, Alessandro A. Quarta, Giovanni Mengali, and Vittorio Cipolla. 2020. "Trajectory Analysis of a Sun-Facing Solar Sail with Optical Degradation." *Journal of Guidance, Control, and Dynamics* 43 (9): 1727–32. [https://doi.org/10.2514/1.g005214][research_bassetto_et_al_2020]
- Bond, Howard E., Gail H. Schaefer, Ronald L. Gilliland, et al. 2017. "The Sirius System and Its Astrophysical Puzzles: Hubble Space Telescope and Ground-Based Astrometry." *Astrophysical Journal* 840 (2): 70. [https://doi.org/10.3847/1538-4357/aa6af8][research_bond_et_al_2017]
- Bookless, John, and Colin McInnes. 2008. "Control of Lagrange Point Orbits Using Solar Sail Propulsion." *Acta Astronautica* 62 (2–3): 159–76. [https://doi.org/10.1016/j.actaastro.2006.12.051][research_bookless_mcinnes_2008]
- Dachwald, Bernd. 2004. "Optimization of Interplanetary Solar Sailcraft Trajectories Using Evolutionary Neurocontrol." *Journal of Guidance, Control, and Dynamics* 27 (1): 66–72. [https://doi.org/10.2514/1.9286][research_dachwald_2004]
- Dachwald, Bernd, Malcolm Macdonald, Colin R. McInnes, Giovanni Mengali, and Alessandro A. Quarta. 2007. "Impact of Optical Degradation on Solar Sail Mission Performance." *Journal of Spacecraft and Rockets* 44 (4): 740–49. [https://doi.org/10.2514/1.21432][research_dachwald_et_al_2007]
- Davoyan, Artur R., Jeremy N. Munday, Nelson Tabiryan, Grover A. Swartzlander, and Les Johnson. 2021. "Photonic Materials for Interstellar Solar Sailing." *Optica* 8 (5): 722. [https://doi.org/10.1364/optica.417007][research_davoyan_et_al_2021]
- Forward, Robert L. 1984. "Roundtrip Interstellar Travel Using Laser-Pushed Lightsails." *Journal of Spacecraft and Rockets* 21 (2): 187–95. [https://doi.org/10.2514/3.8632][research_forward_1984]
- Forward, Robert L. 1991. "Statite: A Spacecraft That Does Not Orbit." *Journal of Spacecraft and Rockets* 28 (5): 606–11. [https://doi.org/10.2514/3.26287][research_forward_1991]
- Funase, Ryu, Yoji Shirasawa, Yuya Mimasu, et al. 2011. "On-Orbit Verification of Fuel-Free Attitude Control System for Spinning Solar Sail Utilizing Solar Radiation Pressure." *Advances in Space Research* 48 (11): 1740–46. [https://doi.org/10.1016/j.asr.2011.02.022][research_funase_et_al_2011]
- Gong, Shengping, and Malcolm Macdonald. 2019. "Review on Solar Sail Technology." *Astrodynamics* 3 (2): 93–125. [https://doi.org/10.1007/s42064-019-0038-x][research_gong_macdonald_2019]
- Heiligers, Jeannette, and Colin R. McInnes. 2015. "Solar Sail Heliocentric Earth-Following Orbits." *Journal of Guidance, Control, and Dynamics* 38 (5): 937–44. [https://doi.org/10.2514/1.g000579][research_heiligers_mcinnes_2015]
- Heller, René, and Michael Hippke. 2017. "Deceleration of High-Velocity Interstellar Photon Sails into Bound Orbits at α Centauri." *Astrophysical Journal Letters* 835 (2): L32. [https://doi.org/10.3847/2041-8213/835/2/l32][research_heller_hippke_2017]
- Heller, René, Michael Hippke, and Pierre Kervella. 2017. "Optimized Trajectories to the Nearest Stars Using Lightweight High-Velocity Photon Sails." *Astronomical Journal* 154 (3): 115. [https://doi.org/10.3847/1538-3881/aa813f][research_heller_hippke_kervella_2017]
- Ilic, Ognjen, and Harry A. Atwater. 2019. "Self-Stabilizing Photonic Levitation and Propulsion of Nanostructured Macroscopic Objects." *Nature Photonics* 13 (4): 289–95. [https://doi.org/10.1038/s41566-019-0373-y][research_ilic_atwater_2019]
- Ilic, Ognjen, Cora M. Went, and Harry A. Atwater. 2018. "Nanophotonic Heterostructures for Efficient Propulsion and Radiative Cooling of Relativistic Light Sails." *Nano Letters* 18 (9): 5583–89. [https://doi.org/10.1021/acs.nanolett.8b02035][research_ilic_went_atwater_2018]
- Janhunen, Pekka. 2004. "Electric Sail for Spacecraft Propulsion." *Journal of Propulsion and Power* 20 (4): 763–64. [https://doi.org/10.2514/1.8580][research_janhunen_2004]
- Janhunen, P., P. K. Toivanen, J. Polkko, et al. 2010. "Electric Solar Wind Sail: Toward Test Missions." *Review of Scientific Instruments* 81 (11): 111301. [https://doi.org/10.1063/1.3514548][research_janhunen_et_al_2010]
- Johnson, Les, Mark Whorton, Andy Heaton, Robin Pinson, Greg Laue, and Charles Adams. 2011. "NanoSail-D: A Solar Sail Demonstration Mission." *Acta Astronautica* 68 (5–6): 571–75. [https://doi.org/10.1016/j.actaastro.2010.02.008][research_johnson_et_al_2011]
- Kezerashvili, Roman Ya., and Gregory L. Matloff. 2009. "Microscopic Approach to Analyze Solar-Sail Space-Environment Effects." *Advances in Space Research* 44 (7): 859–69. [https://doi.org/10.1016/j.asr.2009.05.002][research_kezerashvili_matloff_2009]
- Kopp, Greg, and Judith L. Lean. 2011. "A New, Lower Value of Total Solar Irradiance: Evidence and Climate Significance." *Geophysical Research Letters* 38 (1): L01706. [https://doi.org/10.1029/2010gl045777][research_kopp_lean_2011]
- Kulkarni, Neeraj, Philip Lubin, and Qicheng Zhang. 2018. "Relativistic Spacecraft Propelled by Directed Energy." *Astronomical Journal* 155 (4): 155. [https://doi.org/10.3847/1538-3881/aaafd2][research_kulkarni_lubin_zhang_2018]
- Lyngvi, A., P. Falkner, S. Kemble, M. Leipold, and A. Peacock. 2005. "The Interstellar Heliopause Probe." *Acta Astronautica* 57 (2–8): 104–11. [https://doi.org/10.1016/j.actaastro.2005.03.042][research_lyngvi_et_al_2005]
- Macdonald, Malcolm, Gareth W. Hughes, Colin R. McInnes, Aleksander Lyngvi, Peter Falkner, and Alessandro Atzei. 2006. "Solar Polar Orbiter: A Solar Sail Technology Reference Study." *Journal of Spacecraft and Rockets* 43 (5): 960–72. [https://doi.org/10.2514/1.16408][research_macdonald_et_al_2006]
- Macdonald, Malcolm, and Colin McInnes. 2011. "Solar Sail Science Mission Applications and Advancement." *Advances in Space Research* 48 (11): 1702–16. [https://doi.org/10.1016/j.asr.2011.03.018][research_macdonald_mcinnes_2011]
- Macdonald, Malcolm, Colin McInnes, and Gareth Hughes. 2010. "Technology Requirements of Exploration beyond Neptune by Solar Sail Propulsion." *Journal of Spacecraft and Rockets* 47 (3): 472–83. [https://doi.org/10.2514/1.46657][research_macdonald_mcinnes_hughes_2010]
- Manchester, Zachary, and Abraham Loeb. 2017. "Stability of a Light Sail Riding on a Laser Beam." *Astrophysical Journal* 837 (2): L20. [https://doi.org/10.3847/2041-8213/aa619b][research_manchester_loeb_2017]
- Mansell, Justin R., John M. Bellardo, Bruce Betts, Barbara Plante, and David A. Spencer. 2023. "LightSail 2 Solar Sail Control and Orbit Evolution." *Aerospace* 10 (7): 579. [https://doi.org/10.3390/aerospace10070579][research_mansell_et_al_2023]
- McInnes, Colin R. 1993. "Solar Sail Trajectories at the Lunar L2 Lagrange Point." *Journal of Spacecraft and Rockets* 30 (6): 782–84. [https://doi.org/10.2514/3.26393][research_mcinnes_1993]
- McInnes, Colin R. 1998. "Passive Control of Displaced Solar Sail Orbits." *Journal of Guidance, Control, and Dynamics* 21 (6): 975–82. [https://doi.org/10.2514/2.4334][research_mcinnes_1998]
- McInnes, Colin R. 1999a. "Solar Sail Mission Applications for Non-Keplerian Orbits." *Acta Astronautica* 45 (4–9): 567–75. [https://doi.org/10.1016/s0094-5765(99)00177-0][research_mcinnes_1999b]
- McInnes, C. R., and J. F. L. Simmons. 1992. "Solar Sail Halo Orbits. Part I: Heliocentric Case." *Journal of Spacecraft and Rockets* 29 (4): 466–71. [https://doi.org/10.2514/3.25487][research_mcinnes_simmons_1992]
- Mengali, Giovanni, and Alessandro A. Quarta. 2005. "Optimal Three-Dimensional Interplanetary Rendezvous Using Non-Ideal Solar Sail." *Journal of Guidance, Control, and Dynamics* 28 (1): 173–77. [https://doi.org/10.2514/1.8325][research_mengali_quarta_2005]
- Mengali, Giovanni, Alessandro A. Quarta, Christian Circi, and Bernd Dachwald. 2007. "Refined Solar Sail Force Model with Mission Application." *Journal of Guidance, Control, and Dynamics* 30 (2): 512–20. [https://doi.org/10.2514/1.24779][research_mengali_et_al_2007]
- Michaeli, Lior, Ramon Gao, Michael D. Kelzenberg, et al. 2025. "Direct Radiation Pressure Measurements for Lightsail Membranes." *Nature Photonics* 19 (4): 369–77. [https://doi.org/10.1038/s41566-024-01605-w][research_michaeli_et_al_2025]
- Parkin, Kevin L. G. 2018. "The Breakthrough Starshot System Model." *Acta Astronautica* 152: 370–84. [https://doi.org/10.1016/j.actaastro.2018.08.035][research_parkin_2018]
- Perakis, Nikolaos, and Andreas M. Hein. 2016. "Combining Magnetic and Electric Sails for Interstellar Deceleration." *Acta Astronautica* 128: 13–20. [https://doi.org/10.1016/j.actaastro.2016.07.005][research_perakis_hein_2016]
- Pineda, J. Sebastian, Allison Youngblood, and Kevin France. 2021. "The M-Dwarf Ultraviolet Spectroscopic Sample. I. Determining Stellar Parameters for Field Stars." *Astrophysical Journal* 918 (1): 40. [https://doi.org/10.3847/1538-4357/ac0aea][research_pineda_youngblood_france_2021]
- Prša, Andrej, Petr Harmanec, Guillermo Torres, et al. 2016. "Nominal Values for Selected Solar and Planetary Quantities: IAU 2015 Resolution B3." *Astronomical Journal* 152 (2): 41. [https://doi.org/10.3847/0004-6256/152/2/41][research_prsa_et_al_2016]
- Quarta, Alessandro A., Giovanni Mengali, and Pekka Janhunen. 2011. "Optimal Interplanetary Rendezvous Combining Electric Sail and High Thrust Propulsion System." *Acta Astronautica* 68 (5–6): 603–21. [https://doi.org/10.1016/j.actaastro.2010.01.024][research_quarta_mengali_janhunen_2011]
- Seefeldt, Patric, and Bernd Dachwald. 2021. "Temperature Increase on Folded Solar Sail Membranes." *Advances in Space Research* 67 (9): 2688–95. [https://doi.org/10.1016/j.asr.2020.09.026][research_seefeldt_dachwald_2021]
- Spencer, David A., Bruce Betts, John M. Bellardo, Alex Diaz, Barbara Plante, and Justin R. Mansell. 2021. "The LightSail 2 Solar Sailing Technology Demonstration." *Advances in Space Research* 67 (9): 2878–89. [https://doi.org/10.1016/j.asr.2020.06.029][research_spencer_et_al_2021]
- Swartzlander, Grover A. 2017. "Radiation Pressure on a Diffractive Sailcraft." *Journal of the Optical Society of America B* 34 (6): C25. [https://doi.org/10.1364/josab.34.000c25][research_swartzlander_2017]
- Tsuda, Y., O. Mori, R. Funase, et al. 2011. "Flight Status of IKAROS Deep Space Solar Sail Demonstrator." *Acta Astronautica* 69 (9–10): 833–40. [https://doi.org/10.1016/j.actaastro.2011.06.005][research_tsuda_et_al_2011]
- Tsuda, Yuichi, Osamu Mori, Ryu Funase, et al. 2013. "Achievement of IKAROS — Japanese Deep Space Solar Sail Demonstration Mission." *Acta Astronautica* 82 (2): 183–88. [https://doi.org/10.1016/j.actaastro.2012.03.032][research_tsuda_et_al_2013]
- Vulpetti, Giovanni. 1997. "Sailcraft at High Speed by Orbital Angular Momentum Reversal." *Acta Astronautica* 40 (10): 733–58. [https://doi.org/10.1016/s0094-5765(97)00153-7][research_vulpetti_1997]
- Vulpetti, G. 1999. "General 3D H-Reversal Trajectories for High-Speed Sailcraft." *Acta Astronautica* 44 (1): 67–73. [https://doi.org/10.1016/s0094-5765(99)00016-8][research_vulpetti_1999]
- Wie, Bong. 2004a. "Solar Sail Attitude Control and Dynamics, Part 1." *Journal of Guidance, Control, and Dynamics* 27 (4): 526–35. [https://doi.org/10.2514/1.11134][research_wie_2004a]
- Wie, Bong. 2004b. "Solar Sail Attitude Control and Dynamics, Part Two." *Journal of Guidance, Control, and Dynamics* 27 (4): 536–44. [https://doi.org/10.2514/1.11133][research_wie_2004b]
- Wie, Bong. 2007. "Thrust Vector Control Analysis and Design for Solar-Sail Spacecraft." *Journal of Spacecraft and Rockets* 44 (3): 545–57. [https://doi.org/10.2514/1.23084][research_wie_2007]
- Yonetoku, Daisuke, Toshio Murakami, Shuichi Gunji, et al. 2011. "Gamma-Ray Burst Polarimeter (GAP) aboard the Small Solar Power Sail Demonstrator IKAROS." *Publications of the Astronomical Society of Japan* 63 (3): 625–38. [https://doi.org/10.1093/pasj/63.3.625][research_yonetoku_et_al_2011]
- Zubrin, Robert M., and Dana G. Andrews. 1991. "Magnetic Sails and Interplanetary Travel." *Journal of Spacecraft and Rockets* 28 (2): 197–203. [https://doi.org/10.2514/3.26230][research_zubrin_andrews_1991]

### Primary Sources, Non-Peer-Reviewed

- Banik, Jeremy, and Emil Ardelean. 2010. "Verification of a Retractable Solar Sail in a Thermal-Vacuum Environment." In *51st AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics, and Materials Conference*. AIAA 2010-2585. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2010-2585][research_banik_ardelean_2010]
- Dachwald, Bernd, Andreas Ohndorf, and Bong Wie. 2006. "Solar Sail Trajectory Optimization for the Solar Polar Imager (SPI) Mission." In *AIAA/AAS Astrodynamics Specialist Conference and Exhibit*. AIAA 2006-6177. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2006-6177][research_dachwald_ohndorf_wie_2006]
- Furumoto, Takuro, Ryu Funase, and Tomohiro Yamaguchi. 2014. "Attitude Control Model for Spinning Solar Sail Spacecraft with Reflectivity Control Capability." In *AIAA/AAS Astrodynamics Specialist Conference*. AIAA 2014-4217. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2014-4217][research_furumoto_funase_yamaguchi_2014]
- Furuya, Hiroshi, and Tadashi Masuoka. 2004. "Concept of Rotationally Skew Fold Membrane for Spinning Solar Sail." In *55th International Astronautical Congress of the International Astronautical Federation, the International Academy of Astronautics, and the International Institute of Space Law*. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.iac-04-i.1.05][research_furuya_masuoka_2004]
- Furuya, Hiroshi, Osamu Mori, Hirotaka Sawada, et al. 2011. "Manufacturing and Folding of Solar Sail 'IKAROS'." In *52nd AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics and Materials Conference*. AIAA 2011-1967. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2011-1967][research_furuya_et_al_2011]
- Furuya, Hiroshi, and Yasutaka Satou. 2008. "Deployment and Retraction Mechanisms for Spinning Solar Sail Membrane." In *49th AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics, and Materials Conference*. AIAA 2008-2051. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2008-2051][research_furuya_satou_2008]
- Lappas, Vaios, Manfred Leipold, Peter Falkner, H. Fichtner, and S. Kraft. 2005. "Interstellar Heliopause Probe: System Design of a Solar Sail Mission to 200 AU." In *AIAA Guidance, Navigation, and Control Conference and Exhibit*. AIAA 2005-6084. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2005-6084][research_lappas_et_al_2005]
- McNutt, Leslie, Les Johnson, Pater Kahn, Julie Castillo-Rogez, and Andreas Frick. 2014. "Near-Earth Asteroid (NEA) Scout." In *AIAA SPACE 2014 Conference and Exposition*. AIAA 2014-4435. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2014-4435][research_mcnutt_et_al_2014]
- Mori, Osamu, and IKAROS Demonstration Team. 2011. "World's First Solar Power Sail Demonstration Flight by IKAROS." In *Proceedings of the 19th Space Engineering Conference*. [https://doi.org/10.1299/jsmesec.2010.19.\_a1-1\_][research_mori_et_al_2011]
- Satou, Yasutaka, Hiroshi Furuya, Hiraku Sakamoto, et al. 2014. "Wrapping Experiments of Piecewise Straight Fold Membrane for Large Solar Sail." *Transactions of the Japan Society for Aeronautical and Space Sciences, Aerospace Technology Japan* 12 (ists29): Pc\_49-Pc\_54. [https://doi.org/10.2322/tastj.12.pc\_49][research_satou_et_al_2014]
- Sauer, C., Jr. 1976. "Optimum Solar-Sail Interplanetary Trajectories." In *Astrodynamics Conference*. AIAA 1976-792. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1976-792][research_sauer_1976]
- Stohlman, Olive R., Juan M. Fernandez, Gregory Dean, et al. 2020. "Advances in Low-Cost Manufacturing and Folding of Solar Sail Membranes." In *AIAA Scitech 2020 Forum*. AIAA 2020-2167. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2020-2167][research_stohlman_et_al_2020]
- Vatankhahghadim, Behrad, and Christopher J. Damaren. 2018. "Deployment of a Membrane Attached to Two Axially Moving Beams." *Journal of Applied Mechanics* 86 (3): 031003. [https://doi.org/10.1115/1.4042134][research_vatankhahghadim_damaren_2018]
- Wilkie, William K. 2021. "Overview of the NASA Advanced Composite Solar Sail System (ACS3) Technology Demonstration Project." In *AIAA Scitech 2021 Forum*. AIAA 2021-1260. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.2021-1260][research_wilkie_2021]
- Wright, J., and J. Warmke. 1976. "Solar Sail Mission Applications." In *Astrodynamics Conference*. AIAA 1976-808. American Institute of Aeronautics and Astronautics. [https://doi.org/10.2514/6.1976-808][research_wright_warmke_1976]

### Secondary Sources

- Bassetto, Marco, Lorenzo Niccolai, Alessandro A. Quarta, and Giovanni Mengali. 2022. "A Comprehensive Review of Electric Solar Wind Sail Concept and Its Applications." *Progress in Aerospace Sciences* 128: 100768. [https://doi.org/10.1016/j.paerosci.2021.100768][research_bassetto_et_al_2022]
- Fu, Bo, Evan Sperber, and Fidelis Eke. 2016. "Solar Sail Technology—a State of the Art Review." *Progress in Aerospace Sciences* 86: 1–19. [https://doi.org/10.1016/j.paerosci.2016.07.001][research_fu_sperber_eke_2016]
- McInnes, Colin Robert. 1999b. *Solar Sailing*. Springer London. [https://doi.org/10.1007/978-1-4471-3992-8][book_mcinnes_1999]

### Tertiary Sources

- "Alpha Centauri." 2026. Wikipedia. Last modified October 15, at 01:23 (UTC). [https://en.wikipedia.org/w/index.php?title=Alpha\_Centauri&oldid=1380318503][ref_alpha_centauri]
- "Breakthrough Starshot." 2026. Wikipedia. Last modified September 26, at 18:09 (UTC). [https://en.wikipedia.org/w/index.php?title=Breakthrough\_Starshot&oldid=1376867919][ref_breakthrough_starshot]
- "Electric Sail." 2026. Wikipedia. Last modified October 6, at 17:28 (UTC). [https://en.wikipedia.org/w/index.php?title=Electric\_sail&oldid=1378875555][ref_electric_sail]
- "Gravity Assist." 2026. Wikipedia. Last modified October 4, at 03:20 (UTC). [https://en.wikipedia.org/w/index.php?title=Gravity\_assist&oldid=1378359042][ref_gravity_assist]
- "IKAROS." 2026. Wikipedia. Last modified April 29, at 07:41 (UTC). [https://en.wikipedia.org/w/index.php?title=IKAROS&oldid=1351647572][ref_ikaros]
- "LightSail." 2026. Wikipedia. Last modified June 6, at 14:46 (UTC). [https://en.wikipedia.org/w/index.php?title=LightSail&oldid=1358095072][ref_lightsail]
- "Magnetic Sail." 2026. Wikipedia. Last modified August 26, at 23:34 (UTC). [https://en.wikipedia.org/w/index.php?title=Magnetic\_sail&oldid=1371521511][ref_magnetic_sail]
- "Mass–luminosity Relation." 2026. Wikipedia. Last modified August 21, at 18:39 (UTC). [https://en.wikipedia.org/w/index.php?title=Mass%E2%80%93luminosity\_relation&oldid=1370538787][ref_mass_luminosity_relation]
- "Miura Fold." 2026. Wikipedia. Last modified July 16, at 18:10 (UTC). [https://en.wikipedia.org/w/index.php?title=Miura\_fold&oldid=1364461042][ref_miura_fold]
- "NanoSail-D2." 2026. Wikipedia. Last modified May 3, at 23:48 (UTC). [https://en.wikipedia.org/w/index.php?title=NanoSail-D2&oldid=1352397493][ref_nanosail_d2]
- "Proxima Centauri." 2026. Wikipedia. Last modified October 18, at 13:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Proxima\_Centauri&oldid=1380870772][ref_proxima_centauri]
- "Radiation Pressure." 2026. Wikipedia. Last modified August 19, at 07:00 (UTC). [https://en.wikipedia.org/w/index.php?title=Radiation\_pressure&oldid=1370125229][ref_radiation_pressure]
- "Sirius." 2026. Wikipedia. Last modified October 18, at 20:00 (UTC). [https://en.wikipedia.org/w/index.php?title=Sirius&oldid=1380920350][ref_sirius]
- "Solar Sail." 2026. Wikipedia. Last modified August 12, at 08:09 (UTC). [https://en.wikipedia.org/w/index.php?title=Solar\_sail&oldid=1369001629][ref_solar_sail]
- "Solar Wind." 2026. Wikipedia. Last modified September 21, at 17:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Solar\_wind&oldid=1376038321][ref_solar_wind]
- "Sphere of Influence (Astrodynamics)." 2026. Wikipedia. Last modified September 8, at 00:47 (UTC). [https://en.wikipedia.org/w/index.php?title=Sphere\_of\_influence\_(astrodynamics)&oldid=1373800130][ref_sphere_of_influence]
- "Statite." 2026. Wikipedia. Last modified April 22, at 01:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Statite&oldid=1350452072][ref_statite]
- "Sun." 2026. Wikipedia. Last modified October 20, at 14:05 (UTC). [https://en.wikipedia.org/w/index.php?title=Sun&oldid=1381179696][ref_sun]
- "Znamya (Satellite)." 2026. Wikipedia. Last modified August 11, at 21:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Znamya\_(satellite)&oldid=1368922851][ref_znamya]

### Related Posts

- Sechter, Brendan. 2026. "Introduction to Space Studies." *Brendan A R Sechter's Development Blog*, February 21. [https://sgeos.github.io/space/math/2026/02/21/introduction\_to\_space\_studies.html][related_post_space_studies]
- Sechter, Brendan. 2026. "Orbital Manoeuvres in Terms of Delta-v." *Brendan A R Sechter's Development Blog*, August 17. [https://sgeos.github.io/space/space-studies/2026/08/17/orbital\_manoeuvres.html][related_post_orbital_manoeuvres]

[book_mcinnes_1999]: https://doi.org/10.1007/978-1-4471-3992-8
[ref_alpha_centauri]: https://en.wikipedia.org/w/index.php?title=Alpha_Centauri&oldid=1380318503
[ref_breakthrough_starshot]: https://en.wikipedia.org/w/index.php?title=Breakthrough_Starshot&oldid=1376867919
[ref_electric_sail]: https://en.wikipedia.org/w/index.php?title=Electric_sail&oldid=1378875555
[ref_gravity_assist]: https://en.wikipedia.org/w/index.php?title=Gravity_assist&oldid=1378359042
[ref_ikaros]: https://en.wikipedia.org/w/index.php?title=IKAROS&oldid=1351647572
[ref_lightsail]: https://en.wikipedia.org/w/index.php?title=LightSail&oldid=1358095072
[ref_magnetic_sail]: https://en.wikipedia.org/w/index.php?title=Magnetic_sail&oldid=1371521511
[ref_mass_luminosity_relation]: https://en.wikipedia.org/w/index.php?title=Mass%E2%80%93luminosity_relation&oldid=1370538787
[ref_miura_fold]: https://en.wikipedia.org/w/index.php?title=Miura_fold&oldid=1364461042
[ref_nanosail_d2]: https://en.wikipedia.org/w/index.php?title=NanoSail-D2&oldid=1352397493
[ref_proxima_centauri]: https://en.wikipedia.org/w/index.php?title=Proxima_Centauri&oldid=1380870772
[ref_radiation_pressure]: https://en.wikipedia.org/w/index.php?title=Radiation_pressure&oldid=1370125229
[ref_sirius]: https://en.wikipedia.org/w/index.php?title=Sirius&oldid=1380920350
[ref_solar_sail]: https://en.wikipedia.org/w/index.php?title=Solar_sail&oldid=1369001629
[ref_solar_wind]: https://en.wikipedia.org/w/index.php?title=Solar_wind&oldid=1376038321
[ref_sphere_of_influence]: https://en.wikipedia.org/w/index.php?title=Sphere_of_influence_(astrodynamics)&oldid=1373800130
[ref_statite]: https://en.wikipedia.org/w/index.php?title=Statite&oldid=1350452072
[ref_sun]: https://en.wikipedia.org/w/index.php?title=Sun&oldid=1381179696
[ref_znamya]: https://en.wikipedia.org/w/index.php?title=Znamya_(satellite)&oldid=1368922851
[related_post_orbital_manoeuvres]: {% post_url 2026-08-17-orbital_manoeuvres %}
[related_post_orbital_manoeuvres_patched]: {% post_url 2026-08-17-orbital_manoeuvres %}#patched-conics
[related_post_orbital_manoeuvres_rocket]: {% post_url 2026-08-17-orbital_manoeuvres %}#the-rocket-equation
[related_post_orbital_manoeuvres_spirals]: {% post_url 2026-08-17-orbital_manoeuvres %}#low-thrust-spirals
[related_post_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[research_akeson_et_al_2021]: https://doi.org/10.3847/1538-3881/abfaff
[research_ancona_kezerashvili_matloff_2019]: https://doi.org/10.1016/j.actaastro.2019.02.019
[research_atwater_et_al_2018]: https://doi.org/10.1038/s41563-018-0075-8
[research_banik_ardelean_2010]: https://doi.org/10.2514/6.2010-2585
[research_bassetto_et_al_2020]: https://doi.org/10.2514/1.g005214
[research_bassetto_et_al_2022]: https://doi.org/10.1016/j.paerosci.2021.100768
[research_bond_et_al_2017]: https://doi.org/10.3847/1538-4357/aa6af8
[research_bookless_mcinnes_2008]: https://doi.org/10.1016/j.actaastro.2006.12.051
[research_dachwald_2004]: https://doi.org/10.2514/1.9286
[research_dachwald_et_al_2007]: https://doi.org/10.2514/1.21432
[research_dachwald_ohndorf_wie_2006]: https://doi.org/10.2514/6.2006-6177
[research_davoyan_et_al_2021]: https://doi.org/10.1364/optica.417007
[research_forward_1984]: https://doi.org/10.2514/3.8632
[research_forward_1991]: https://doi.org/10.2514/3.26287
[research_fu_sperber_eke_2016]: https://doi.org/10.1016/j.paerosci.2016.07.001
[research_funase_et_al_2011]: https://doi.org/10.1016/j.asr.2011.02.022
[research_furumoto_funase_yamaguchi_2014]: https://doi.org/10.2514/6.2014-4217
[research_furuya_et_al_2011]: https://doi.org/10.2514/6.2011-1967
[research_furuya_masuoka_2004]: https://doi.org/10.2514/6.iac-04-i.1.05
[research_furuya_satou_2008]: https://doi.org/10.2514/6.2008-2051
[research_gong_macdonald_2019]: https://doi.org/10.1007/s42064-019-0038-x
[research_heiligers_mcinnes_2015]: https://doi.org/10.2514/1.g000579
[research_heller_hippke_2017]: https://doi.org/10.3847/2041-8213/835/2/l32
[research_heller_hippke_kervella_2017]: https://doi.org/10.3847/1538-3881/aa813f
[research_ilic_atwater_2019]: https://doi.org/10.1038/s41566-019-0373-y
[research_ilic_went_atwater_2018]: https://doi.org/10.1021/acs.nanolett.8b02035
[research_janhunen_2004]: https://doi.org/10.2514/1.8580
[research_janhunen_et_al_2010]: https://doi.org/10.1063/1.3514548
[research_johnson_et_al_2011]: https://doi.org/10.1016/j.actaastro.2010.02.008
[research_kezerashvili_matloff_2009]: https://doi.org/10.1016/j.asr.2009.05.002
[research_kopp_lean_2011]: https://doi.org/10.1029/2010gl045777
[research_kulkarni_lubin_zhang_2018]: https://doi.org/10.3847/1538-3881/aaafd2
[research_lappas_et_al_2005]: https://doi.org/10.2514/6.2005-6084
[research_lyngvi_et_al_2005]: https://doi.org/10.1016/j.actaastro.2005.03.042
[research_macdonald_et_al_2006]: https://doi.org/10.2514/1.16408
[research_macdonald_mcinnes_2011]: https://doi.org/10.1016/j.asr.2011.03.018
[research_macdonald_mcinnes_hughes_2010]: https://doi.org/10.2514/1.46657
[research_manchester_loeb_2017]: https://doi.org/10.3847/2041-8213/aa619b
[research_mansell_et_al_2023]: https://doi.org/10.3390/aerospace10070579
[research_mcinnes_1993]: https://doi.org/10.2514/3.26393
[research_mcinnes_1998]: https://doi.org/10.2514/2.4334
[research_mcinnes_1999b]: https://doi.org/10.1016/s0094-5765(99)00177-0
[research_mcinnes_simmons_1992]: https://doi.org/10.2514/3.25487
[research_mcnutt_et_al_2014]: https://doi.org/10.2514/6.2014-4435
[research_mengali_et_al_2007]: https://doi.org/10.2514/1.24779
[research_mengali_quarta_2005]: https://doi.org/10.2514/1.8325
[research_michaeli_et_al_2025]: https://doi.org/10.1038/s41566-024-01605-w
[research_mori_et_al_2011]: https://doi.org/10.1299/jsmesec.2010.19._a1-1_
[research_parkin_2018]: https://doi.org/10.1016/j.actaastro.2018.08.035
[research_perakis_hein_2016]: https://doi.org/10.1016/j.actaastro.2016.07.005
[research_pineda_youngblood_france_2021]: https://doi.org/10.3847/1538-4357/ac0aea
[research_prsa_et_al_2016]: https://doi.org/10.3847/0004-6256/152/2/41
[research_quarta_mengali_janhunen_2011]: https://doi.org/10.1016/j.actaastro.2010.01.024
[research_satou_et_al_2014]: https://doi.org/10.2322/tastj.12.pc_49
[research_sauer_1976]: https://doi.org/10.2514/6.1976-792
[research_seefeldt_dachwald_2021]: https://doi.org/10.1016/j.asr.2020.09.026
[research_spencer_et_al_2021]: https://doi.org/10.1016/j.asr.2020.06.029
[research_stohlman_et_al_2020]: https://doi.org/10.2514/6.2020-2167
[research_swartzlander_2017]: https://doi.org/10.1364/josab.34.000c25
[research_tsuda_et_al_2011]: https://doi.org/10.1016/j.actaastro.2011.06.005
[research_tsuda_et_al_2013]: https://doi.org/10.1016/j.actaastro.2012.03.032
[research_vatankhahghadim_damaren_2018]: https://doi.org/10.1115/1.4042134
[research_vulpetti_1997]: https://doi.org/10.1016/s0094-5765(97)00153-7
[research_vulpetti_1999]: https://doi.org/10.1016/s0094-5765(99)00016-8
[research_wie_2004a]: https://doi.org/10.2514/1.11134
[research_wie_2004b]: https://doi.org/10.2514/1.11133
[research_wie_2007]: https://doi.org/10.2514/1.23084
[research_wilkie_2021]: https://doi.org/10.2514/6.2021-1260
[research_wright_warmke_1976]: https://doi.org/10.2514/6.1976-808
[research_yonetoku_et_al_2011]: https://doi.org/10.1093/pasj/63.3.625
[research_zubrin_andrews_1991]: https://doi.org/10.2514/3.26230
