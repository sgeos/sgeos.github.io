---
layout: post
mathjax: true
comments: true
title: "X-Planes: Lockheed X-27"
date: 2025-11-02 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 28
---
<!-- A324 -->
<script>console.log("A324");</script>

The [Lockheed X-27][ref_x27] never existed. No airframe was completed, no engine was ever run in one, and no
pilot ever sat in anything but a [mock-up][ref_mockup] of wood with a metal skin.
**The designation was issued, the aeroplane was not built, and the gap between those two facts is the subject of this article.**
This is the twenty-eighth article in the [X-Planes series][related_post_a297_xplanes_framing], following the
[X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the
[X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the
[X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the
[X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the
[X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the
[X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the
[X-13][related_post_a310_ryan_x13], the [X-14][related_post_a311_bell_x14], the
[X-15][related_post_a312_north_american_x15], the [X-16][related_post_a313_bell_x16], the
[X-17][related_post_a314_lockheed_x17], the [X-18][related_post_a315_hiller_x18], the
[X-19][related_post_a316_curtiss_wright_x19], the [X-20][related_post_a317_boeing_x20], the
[X-21][related_post_a318_northrop_x21], the [X-22][related_post_a319_bell_x22], the
[X-23][related_post_a320_martin_marietta_x23], the [X-24][related_post_a321_martin_marietta_x24], the
[X-25][related_post_a322_bensen_x25], and the [X-26][related_post_a323_schweizer_x26].

The aeroplane that was not built was the [CL-1200 Lancer][ref_cl1200], a private venture of the
[Lockheed Advanced Development Projects office][ref_skunk_works] under
[Clarence Johnson][ref_kelly_johnson], and it was a re-winged, re-engined [F-104 Starfighter][ref_f104]
offered for export. Lockheed paid for it. The [United States Air Force][ref_usaf] did not, and the
designation it issued was a promise of support that never arrived.

**This article is unusual in the series because its subject produced no data at all.** There is no flight
record, no wind-tunnel report, and no test literature under the vehicle's own name. A search of the National
Aeronautics and Space Administration's [Technical Reports Server][ref_ntrs] for the Lancer returns nothing
whatever. What survives is a set of numbers from a sales brochure and a parent aircraft that flew for thirty
years, and that turns out to be enough to do real work with, because
**a derivative can be checked against the thing it was derived from.**

* Contents
{:toc}

## The Research Question

The X-27 had two research questions, and they were not the same question.

**The stated one is on the record.** The X-27 was to be a high-performance research aircraft derived from
the CL-1200, built to test advanced-technology engines and equipment, and it was to fly at [Mach][ref_mach]
2.6. That is a specific and answerable engineering question, and it is the one this article treats as the
keystone.

**The operative one is visible in what the aeroplane was for.** The CL-1200 was a sales article. It had lost
the competition it was designed for, its manufacturer had spent its own money on it, and an X-designation
would have brought government funds to build a flying demonstrator that no customer had yet agreed to buy.
**The designation was being asked to do commercial work.**

The article treats the first as the technical keystone and the second as the historical one, and it does not
pretend that either subsumes the other.

### The Binding Unknown, Stated Precisely

Take the stated question at face value and it names one thing that had never been done in this airframe.

**The F-104's propulsion installation was designed around a turbojet at Mach 2.** The X-27 proposed a
[turbofan][ref_turbofan] at Mach 2.6. Those two changes are not independent and neither is small.

- **A turbofan is not a turbojet with better fuel consumption.** It swallows more air, it is
  physically larger, and its fan is far less tolerant of non-uniform flow at its face than a
  turbojet's first compressor stage.
- **Mach 2.6 is not Mach 2.0 with more thrust.** The total-pressure recovery an inlet can achieve
  falls steeply with Mach number, and the temperature the skin reaches rises steeply.

So the binding unknown is a single compound question.
**Can a turbofan be fed at Mach 2.6 through an inlet descended from a Mach 2.0 turbojet installation, in an airframe built of aluminium alloy?**

Three sections below answer the three parts of that, and two of the answers are negative.

### Why This Is the Right Keystone and Not the Obvious One

The obvious keystone would be manoeuvrability, because that is what the sales case was about and what the
competition turned on. **It is treated at length here**, and the answer is more favourable to Lockheed than
the outcome suggests.

But manoeuvrability is not what the X-designation was requested for. The designation was requested for a
Mach 2.6 propulsion demonstrator, and
**an article that silently replaces a programme's stated purpose with a more interesting one is writing about a different programme.**
Both are treated, and they are kept apart.

## Programme Origin

The Lancer was not commissioned. It was offered, twice, into competitions it did not win, and the
designation arrived after the first of those defeats rather than before it.
**The order of events is what makes the programme legible**, so this section takes them in order.

### What Lockheed Had, and What Was Wrong With It

The [F-104 Starfighter][ref_f104] first flew in 1954 and was designed to one requirement above all others,
namely to climb fast and go fast in a straight line. It has a wing of 196.1 square feet and a span of 21.94
feet, the reference geometry the National Aeronautics and Space Administration's handling-qualities
compilation gives for the F-104A \[[Aircraft Handling Qualities Data, NASA CR-2144][ref_heffley_jewell]\],
and a thickness-to-chord ratio of 3.36 percent, with a leading edge sharp enough that ground
crews fitted protective covers over it \[[Lockheed F-104 Starfighter][ref_f104]\]. The aircraft was a superb interceptor and a poor fighter, and the
reason is in the geometry rather than in any failing of manufacture.

The [aspect ratio][ref_aspect_ratio] follows from the span and the area.

$$ A = \frac{b^2}{S} = \frac{(21.94\ \mathrm{ft})^2}{196.1\ \mathrm{ft}^2} = 2.455 $$

**That is a very low number for a wing meant to turn.** The wing loading is the other half of the problem.

$$ \frac{W}{S} = \frac{27{,}300\ \mathrm{lb}}{196.1\ \mathrm{ft}^2} = 139.2\ \mathrm{lb/ft}^2 $$

Here $W$ is the F-104G's design gross weight of 27,300 pounds as the National Aeronautics and Space
Administration's survey of aircraft performance tabulates it, and the survey gives the same 139.2 \[[Quest for Performance, NASA SP-468][ref_sp468]\].

An aircraft that must generate lift equal to several times its weight in a turn, from a small wing of low
aspect ratio, pays for that lift in drag, and the drag is what ends the turn.

### The International Fighter Aircraft Competition

By the late 1960s the [United States][ref_usa] was supplying fighters to allied air forces under
[military assistance][ref_fms] arrangements, and the aircraft on offer were becoming too expensive for the
purpose. The [International Fighter Aircraft][ref_ifa] competition was run to select a fighter that could be
sold or granted abroad in quantity.

The entrants were what the industry already had, adapted.

- **Northrop** offered the F-5-21, a developed [F-5][ref_f5] which became the [F-5E Tiger II][ref_f5e].
- **Ling-Temco-Vought** offered the V-1000, derived from the [F-8 Crusader][ref_f8].
- **McDonnell Douglas** offered a simplified [F-4 Phantom][ref_f4].
- **Lockheed** offered the CL-1200 Lancer.

**Northrop won in November 1970.** The decision removed the Lancer's primary market at a stroke, because the
aircraft had been designed for exactly the customers the competition was about to direct elsewhere, and
**no existing F-104 operator subsequently expressed interest.**

### The Designation, and a Disagreement in the Record

What happened next is where the sources diverge, and the article does not resolve the disagreement because
the record does not.

**One reading** is that the Air Force wanted the aircraft flown. Under this reading the service planned to
buy at least one example under the designation X-27 as a technology demonstrator, and the programme died for
want of appropriated money.

**The other reading** is that the designation was sought rather than offered. Under this reading Lockheed
pursued an X-designation as a route to federal funding for a demonstrator that would carry a sales campaign,
and elements within the Air Force were actively hostile because a well-publicised Mach 2.5 fighter at a
fraction of the cost could complicate the case then being made for the [F-15][ref_f15].

**These are not compatible accounts of who wanted what**, and both appear in otherwise careful secondary
sources. What is not in dispute is the outcome.
**Congressional and Air Force support was close to absent, no money was appropriated, and nothing was built beyond a mock-up.**

### The Second Attempt

Lockheed offered the CL-1200-2 into the [Lightweight Fighter][ref_lwf] competition of 1972, and lost again.
[General Dynamics][ref_gd] and [Northrop][ref_northrop] received the prototype contracts that became the
[YF-16][ref_yf16] and the [YF-17][ref_yf17].

**The Lightweight Fighter programme is the sharpest possible commentary on the Lancer**, because it funded
exactly the thing Lockheed had asked for, namely flying prototypes of lightweight fighters built to
demonstrate a concept rather than to fill an order. It simply funded somebody else's.

A [Navy][ref_usn] derivative, the CL-1400 and CL-1400N, was studied, combining the forward fuselage, intake
and wing of the CL-1200-2 with the rear fuselage of the X-27. It went no further.

## The Vehicle

Three designations name closely related aeroplanes and the record does not always keep them apart. The
CL-1200-1 was the turbojet aircraft entered in 1970, the CL-1200-2 was the turbofan development offered in
1972, and the X-27 was the proposed demonstrator derived from the second.
**Nothing in this section was ever built**, and the figures are the manufacturer's throughout.

### What Changed From the F-104

The Lancer was not a modified Starfighter. It was a new aeroplane that reused the Starfighter's fuselage
cross-section, its aerofoil section, and a good deal of its systems philosophy.

| Quantity | F-104G | CL-1200-2 and X-27 | Change |
|---|---|---|---|
| Wing area | 196.1 ft² | 300.0 ft² | +53.0 percent |
| Span | 21.94 ft | 29.17 ft | +33.0 percent |
| Aspect ratio | 2.455 | 2.836 | +15.5 percent |
| Length | 54.75 ft | 57.25 ft | +30.0 in |
| Empty weight | 13,996 lb | 17,885 lb | +27.8 percent |
| Loaded weight as published | 27,300 lb, design gross | 24,385 lb, normal loaded | not like for like |
| Maximum takeoff | 29,083 lb | 35,000 lb | +20.3 percent |
| Engine | J79-GE-11A turbojet | TF30-P-100 turbofan | a change of class |
| Thrust with afterburner | 15,600 lbf | 25,000 lbf | +60.3 percent |
| Wing loading at the published loaded weight | 139.2 lb/ft² | 81.3 lb/ft² | −41.6 percent |
| Thrust to weight at the published loaded weight | 0.571 | 1.025 | +79.4 percent |

The F-104G weights are the National Aeronautics and Space Administration's \[[Quest for Performance, NASA SP-468][ref_sp468]\]. The CL-1200-2 weights
are Lockheed's estimates, which \[[Lockheed CL-1200 Lancer][ref_cl1200]\] attributes to \[[Air Enthusiast, Volume One][book_air_enthusiast_1971]\] and which also lists 17,250 pounds empty
and 32,500 pounds gross, the figures \[[X-27 specifications][ref_x27_specs]\] gives for the X-27. The analysis below uses the CL-1200-2 figures throughout. **The two loaded weights are defined
differently.** The F-104G figure is a design gross weight and the CL-1200-2 figure a normal loaded weight, so
the wing-loading and thrust-to-weight changes in the last two rows overstate the change at equal loading and
are best read as upper bounds.

**Four changes matter and the rest follow from them.**

**The wing grew by half and moved.** It went from a mid-set position to a shoulder position and moved aft,
while retaining the F-104's 10 degrees of [anhedral][ref_anhedral] and, importantly, its aerofoil section
\[[Lockheed CL-1200 Lancer][ref_cl1200]\].

**The tail came down.** The F-104's [T-tail][ref_t_tail], with the horizontal surface on top of the fin, was
replaced by a conventional horizontal tail on the rear fuselage.

**The engine changed class.** The [J79][ref_j79] turbojet became the [TF30][ref_tf30] turbofan, and the
difference in physical envelope is not incidental.

| Engine | Length | Diameter | Dry weight | Airflow |
|---|---|---|---|---|
| J79-GE-17 | 208.69 in | 39.06 in | 3,835 lb | 170 lb/s |
| TF30-P-100 | 241.70 in | 48.90 in | 3,985 lb | 260 lb/s |
| Difference | +33.01 in | +9.84 in | +150 lb | +52.9 percent |

The lengths, diameters, dry weights and airflows are the published ratings of the two engines
\[[General Electric J79][ref_j79]\] \[[Pratt and Whitney TF30][ref_tf30]\]. The last row gives the differences,
and its airflow entry is a ratio less one.

$$ \Delta L = 241.70 - 208.69 = 33.01\ \mathrm{in}, \qquad \Delta D = 48.90 - 39.06 = 9.84\ \mathrm{in}, \qquad \frac{\dot m_{\mathrm{TF30}}}{\dot m_{\mathrm{J79}}} - 1 = \frac{260}{170} - 1 = 0.529 $$

**The fuselage was stretched 30 inches**, which the record attributes to a 46 percent increase in internal
fuel \[[Lockheed CL-1200 Lancer][ref_cl1200]\]. **The engine that had to go inside it is 33.01 inches longer than the J79-GE-17.** The comparison table uses the J79-GE-17 because those are the J79 dimensions the article holds, while the F-104G column above names the J79-GE-11A, so the differences are measured against a sister variant of the engine the F-104G carried and not against that engine itself. The stretch
falls short of the engine length difference by

$$ \Delta L - \Delta L_{\mathrm{fus}} = 33.01 - 30 = 3.01\ \mathrm{in} $$

where $\Delta L_{\mathrm{fus}}$ is the fuselage stretch, which is close enough that either consideration
could have set it. The article declines to claim which one did, because the record states only the fuel
figure.

### The Intakes, Which Are the Article's Subject

**The F-104 uses fixed half-cone side inlets.** The CL-1200 replaced them with translating shock cones
having four inches of axial movement.
**The X-27, according to the record, was to have had intakes of rectangular form instead**
\[[Lockheed CL-1200 Lancer][ref_cl1200]\].

The record does not say why the shape changed.
**Section [Sizing From First Principles](#sizing-from-first-principles) computes an answer, and the answer is that a single cone cannot do the job at Mach 2.6.**

### The Mock-Up, and What It Tells Us

One full-scale mock-up was completed in a Lockheed hangar. Reports indicate that up to three fuselages were
worked before termination.

**A mock-up is not evidence about performance and this article does not treat it as any.** It is evidence
about intent and about how far the money went, and that is all it is used for here.

## Sizing From First Principles

Everything in this section is computed from published geometry and published engine ratings.
**None of it is a measurement, because there is nothing to measure.** What it produces is an independent
prediction to set beside the manufacturer's prediction, and the
[ground-prediction section](#comparison-with-ground-prediction) says plainly that the comparison is between
two predictions rather than between a prediction and a fact.

### The Flight Condition

The [International Standard Atmosphere][ref_isa] gives the conditions at the altitude every performance
claim is quoted at. The compressible-flow relations used from here to the end of the inlet section are
standard and are set out in [Shapiro][book_shapiro] and [Anderson][book_anderson], which are the sources for
every identity below that carries no other citation. Below 11 kilometres the temperature falls linearly with
height at the standard lapse rate.

$$ T(h) = T_0 - \lambda h, \qquad T_0 = 288.15\ \mathrm{K}, \qquad \lambda = 0.0065\ \mathrm{K/m} $$

Above the tropopause it is constant, and the pressure falls exponentially.

$$ p(h) = p_{11} \exp\left(-\frac{g_0 (h - h_{11})}{R T}\right) $$

The density follows from the equation of state rather than from the pressure directly.

$$ \rho = \frac{p}{R T} = \frac{23{,}842.3}{287.05 \times 218.81} = 0.3796\ \mathrm{kg/m^3} $$

At 35,000 feet, which is 10,668 metres and above the tropopause, this gives a temperature of 218.81 kelvin,
a density of 0.3796 kilograms per cubic metre, and a speed of sound of

$$ a = \sqrt{\gamma R T} = \sqrt{1.4 \times 287.05\ \times 218.81} = 296.54\ \mathrm{m/s} = 663.3\ \mathrm{mph} $$

The Mach number is the ratio the whole article is written in, and it is worth writing down once.

$$ M = \frac{V}{a} $$

$$ M = \frac{1{,}700\ \mathrm{mph} \times 0.44704}{296.54\ \mathrm{m/s}} = \frac{760.0}{296.54} = 2.563 $$

**The claimed maximum speed of 1,700 miles per hour at 35,000 feet is therefore Mach 2.563**, which is
consistent with the Mach 2.57 quoted in one source and with the Mach 2.5 quoted in another as a rounding.
The X-27's stated test objective of Mach 2.6 sits just above it.

Two further quantities are used throughout and are defined here so that later sections can call on them,
following [Anderson][book_anderson]. The dynamic pressure is what converts a coefficient into a force, and
the specific heat at constant pressure follows from the gas constant and the ratio of specific heats.

$$ q = \tfrac{1}{2}\rho V^2 $$

$$ c_p = \frac{\gamma R}{\gamma - 1} = \frac{1.4 \times 287.05}{0.4} = 1004.7\ \mathrm{J/(kg\,K)} $$

At 15,000 feet and Mach 0.9, the condition every manoeuvre result below is evaluated at, the dynamic
pressure is

$$ q = \tfrac{1}{2} \times 0.7708 \times 290.0^2 = 32{,}415\ \mathrm{Pa} = 677.1\ \mathrm{lb/ft^2} $$

The heating this flight condition produces is the subject of the cluster on aerodynamic heating, recovery
temperature and thermal protection below, and the period's measurements of it in flight include these.

- [Kaye and Yeh 1955][research_kaye_yeh_1955]
- [Walker 1955][research_walker_1955]
- [Snodgrass 1955][research_snodgrass_1955]
- [Stephens 1959][research_stephensemilyw_1959]
- [Rumsey and Lee 1961][research_rumseycharlesb_leedorothyb_1961]

### The Temperature the Skin Reaches

Air brought to rest against a surface gives up its kinetic energy as heat. The
[total temperature][ref_total_temperature] follows from energy conservation in a compressible flow.

$$ \frac{T_t}{T} = 1 + \frac{\gamma - 1}{2} M^2 $$

**A real surface does not recover all of it**, because the boundary layer conducts some heat away along the
surface as it converts the rest. The [recovery factor][ref_recovery_factor] accounts for that, and for a
turbulent boundary layer it is the cube root of the [Prandtl number][ref_prandtl].

$$ T_r = T\left(1 + r\,\frac{\gamma - 1}{2} M^2\right), \qquad r = \Pr^{1/3} \approx 0.896 $$

Evaluating at 35,000 feet gives the table the whole structural argument rests on.

| Mach | Speed | Total temperature | Recovery temperature | Yield retained by 2024-T81, half-hour exposure |
|---|---|---|---|---|
| 1.00 | 663 mph | −10.6 °C | −15.1 °C | 100 percent |
| 2.00 | 1,327 mph | 120.7 °C | 102.5 °C | 89 percent |
| 2.20 | 1,459 mph | 157.5 °C | 135.5 °C | 85 percent |
| 2.50 | 1,658 mph | 219.2 °C | 190.8 °C | 74 percent |
| 2.56 | 1,698 mph | 232.5 °C | 202.7 °C | 71 percent |
| 2.60 | 1,725 mph | 241.5 °C | 210.8 °C | 68 percent |

The standard treatments of compressible flow used throughout this section are [Shapiro][book_shapiro] and
[Anderson][book_anderson], and the aerodynamic design context is [Kuchemann][book_kuchemann].

**The last column is read from the Department of Defense handbook curve of tensile yield strength at
temperature for 2024-T81 aluminium alloy**, as a percentage of the room-temperature value, on the curve for
one-half hour at temperature \[[Metallic Materials and Elements for Aerospace Vehicle Structures, MIL-HDBK-5J][ref_mil_hdbk_5j]\].
That figure, Figure 3.2.3.4.1(b), is plotted in degrees Fahrenheit, so each recovery temperature is
converted before it is read.

$$ T_{\mathrm{F}} = 1.8\,T_{\mathrm{C}} + 32, \qquad 1.8 \times 210.8 + 32 = 411.4\ ^{\circ}\mathrm{F} $$

The readings are given to the nearest percentage point, which is about the precision the printed curve
allows. At Mach 1.0 the recovery temperature lies below the curve's range, and the room-temperature value
applies. **Half an hour is the shortest exposure the handbook plots, and longer exposure lowers the curve.**
At the Mach 2.6 recovery temperature the handbook's five exposure curves read as follows
\[[Metallic Materials and Elements for Aerospace Vehicle Structures, MIL-HDBK-5J][ref_mil_hdbk_5j]\].

| Exposure at 411 °F | 1/2 hour | 10 hours | 100 hours | 1,000 hours | 10,000 hours |
|---|---|---|---|---|---|
| Yield retained | 68 percent | 67 percent | 57 percent | 44 percent | 28 percent |

The half-hour column is therefore the most favourable reading the handbook supports, and an airframe that
accumulated many hours at that temperature over a service life would sit on one of the lower curves.

**The shape of that column is the finding.** At Mach 2.0, where the F-104 lived, the structure keeps 89
percent of its strength. At Mach 2.6 it keeps 68 percent, and a wing sized for a given load factor at full
strength is a wing that no longer reaches it.

The literature on elevated-temperature alloy behaviour and creep is large and spans the whole period, and it
is gathered in the clusters on aluminium alloys and their strength when hot and on titanium, other alloys and
composites at elevated temperature below. The measurements of aluminium alloys at temperature closest to the
handbook curve above are these.

- [Mathauser and Deveikis 1955][research_mathausereldone_deveikiswilliamd_1955]
- [Mathauser and Deveikis 1957][research_mathausereldone_deveikiswilliamd_1957]
- [Inglis and Larke 1958][research_inglis_larke_1958]
- [Taig 1961][research_taig_1961]
- [A Study of the Short Time Elevated Temperature Properties of...][research_mahorter_robertg_1961]
- [Montano 1967][research_montanojw_1967]

### Does a Dash Evade the Temperature?

**The obvious defence is that Mach 2.6 was a dash number rather than a cruise number**, and that a structure
does not reach its steady-state temperature in a short excursion. The defence is testable.

Treat a panel of skin as a lumped thermal mass heated by convection from the boundary layer. The balance is
first order and its time constant is

$$ \tau = \frac{\rho_s c_s t}{h} $$

where $\rho_s$ is the density of the skin, $c_s$ its specific heat, $t$ its thickness, and $h$ the
convective coefficient. The coefficient is not assumed. It comes from the turbulent flat-plate
[Stanton number][ref_stanton] evaluated at the [Eckert reference temperature][ref_eckert], which accounts
for the property variation across a high-speed boundary layer.

$$ T^* = T_e\left(0.5\left(1 + \frac{T_w}{T_e}\right) + 0.16\,r\,\frac{\gamma-1}{2}M_e^2\right) $$

$$ \mathrm{St} = 0.0296\,\mathrm{Re}_x^{-1/5}\,\Pr^{-2/3}, \qquad h = \mathrm{St}\,\rho^* u_e c_p $$

The Reynolds number in that correlation is itself a defined quantity, and the viscosity inside it comes from
Sutherland's law rather than from a table, both as given in [Anderson][book_anderson].

$$ \mathrm{Re}_x = \frac{\rho^* u_e x}{\mu^*}, \qquad \mu(T) = \frac{1.458 \times 10^{-6}\,T^{3/2}}{T + 110.4} $$

$$ \mathrm{Re}_x = \frac{0.2109 \times 771.0 \times 5.0}{2.2598 \times 10^{-5}} = 3.598 \times 10^{7} $$

For a two-millimetre aluminium skin five metres back from the nose at Mach 2.6 and 35,000 feet, the Reynolds
number is $3.60 \times 10^7$, the coefficient is 185.5 watts per square metre kelvin, and

$$ \tau = \frac{2780 \times 875 \times 0.002}{185.5} = 26.2\ \mathrm{s} $$

The transient from a cold start then follows directly.

$$ T_{\mathrm{skin}}(t) = T_\infty + \left(T_r - T_\infty\right)\left(1 - e^{-t/\tau}\right) $$

| Time at Mach 2.6 | Skin temperature | Fraction of the way | Yield retained |
|---|---|---|---|
| 30 s | 148.4 °C | 68.1 percent | 83 percent |
| 60 s | 190.9 °C | 89.9 percent | 74 percent |
| 120 s | 208.8 °C | 99.0 percent | 69 percent |
| 180 s | 210.6 °C | 99.9 percent | 68 percent |

#### The Heating Also Loads the Structure, Which Is a Separate Objection

**Losing yield strength is not the only thing high temperature does.** A skin that wants to expand and is
restrained by cooler structure behind it develops stress without any aerodynamic load at all.

Thermal stress, thermal buckling of heated panels, and the thermoelastic analysis of restrained structure
are a substantial period literature, driven by exactly the aircraft that were trying to fly faster than
aluminium comfortably allows.

- [Parkes 1953][research_parkes_1953]
- [A Conference on Thermal Stress][research_a_conference_1954]
- [Loveless and Boswell 1954][research_loveless_boswell_1954]
- [Parkes 1954][research_parkes_1954]
- [Mahlmeister et al 1955][research_mahlmeister_ishimoto_1955]
- [Parkes 1956][research_parkes_1956]
- [Parkes 1956][research_parkes_1956_b]
- [Calligeros and Dugundji 1961][research_calligeros_dugundji_1961]
- [Ayers 1962][research_ayers_1962]
- [Rivello 1965][research_rivello_1965]
- [Gellatly et al 1965][research_gellatly_bijlaard_1965]
- [Mansfield 1967][research_mansfield_1967]
- [Uthgenannt 1971][research_uthgenannt_1971]
- [Matsumoto and Sekiya 1975][research_matsumoto_sekiya_1975]
- [Tani 1978][research_tani_1978]
- [Jenkins 1979][research_jenkinsjm_1979]

$$ \sigma_{\mathrm{th}} = E\,\alpha\,\Delta T $$

Taking aluminium alloy at a Young's modulus of 72 gigapascals and a coefficient of thermal expansion of 23
parts per million per kelvin, and the full excursion from a cold start to the recovery temperature at Mach
2.6,

$$ \sigma_{\mathrm{th}} = 72 \times 10^{9} \times 23 \times 10^{-6} \times 190.8 = 316\ \mathrm{MPa} $$

**The retained yield at that temperature is about 272 megapascals.** The handbook's room-temperature
A-basis yield strength for 2024-T81 sheet from 0.010 to 0.249 inch thick is 58 ksi in the long-transverse
direction \[[Metallic Materials and Elements for Aerospace Vehicle Structures, MIL-HDBK-5J][ref_mil_hdbk_5j]\],
and with the 68 percent from the table above

$$ \sigma_{\mathrm{yield}}(T_r) = 0.68 \times 58\ \mathrm{ksi} \times 6.895\ \frac{\mathrm{MPa}}{\mathrm{ksi}} = 0.68 \times 400\ \mathrm{MPa} = 272\ \mathrm{MPa}, \qquad \frac{316}{272} = 1.16 $$

**The fully restrained thermal stress exceeds it, at 116 percent.**

**That number is an upper bound and not a prediction**, because no real airframe is fully restrained. The
whole structure heats, so what matters is the **difference** in temperature between skin and substructure,
and the honest way to use the relation is to invert it and ask how much difference the material can afford.

$$ \Delta T_{1/2} = \frac{0.5\,\sigma_{\mathrm{yield}}(T)}{E\,\alpha} = \frac{0.5 \times 272 \times 10^{6}}{72 \times 10^{9} \times 23 \times 10^{-6}} = 82\ \mathrm{K} $$

**Eighty-two kelvin of differential consumes half the remaining strength.** That is not a large number for
a structure with a thin hot skin over cooler spars and frames, and it says the Mach 2.6 objective posed a
thermal-stress problem on top of the strength problem, which the record does not discuss at all.

**The defence does not survive.** The skin is nine-tenths of the way to its equilibrium temperature after
one minute. A dash long enough to be worth making is a dash long enough to heat the structure, and
**the time constant is short because aluminium skin is thin and conductive, which is exactly why it was chosen for everything else.**

This is not a novel observation about the era. It is why the [X-15][related_post_a312_north_american_x15]
was built of [Inconel X][ref_inconel] and why the [SR-71][ref_sr71] was built of [titanium][ref_titanium].
**What is worth stating is that the X-27 proposed to reach a speed in that regime while inheriting an aluminium airframe, and that the record does not say how.**

### The Inlet, Which Is Where the Question Actually Lives

An engine at supersonic speed is fed by a device whose job is to slow the air to a speed the compressor can
accept while losing as little [total pressure][ref_total_pressure] as possible.
**Total pressure is the currency**, because thrust follows from the pressure the engine has to work with,
and every shock wave the air crosses spends some of it irreversibly.

The measure is the [total-pressure recovery][ref_pressure_recovery], the ratio of total pressure at the
engine face to total pressure in the free stream.

$$ \eta = \frac{p_{t2}}{p_{t\infty}} $$

**The standard reference for this entire subject is [Seddon and Goldsmith][book_seddon_goldsmith]**, and the
propulsion-integration side is covered by [Oates][book_oates] and by [Mattingly][book_mattingly_engine].

The literature on supersonic inlet design, shock systems, recovery and capture is one of the largest bodies
of work in the whole of applied gas dynamics. It is gathered in the cluster on supersonic inlets, shock
systems and pressure recovery below, the largest in this survey, and the period studies and reviews this
section draws on are these.

- [Ferri and Nucci 1946][research_ferriantonio_nuccilouism_1946]
- [Nussdorfer et al 1952][research_nussdorfertheodorej_oberyleonardj_1952]
- [Syberg and Koncsek 1972][research_sybergj_koncsekjl_1972]
- [Sorensen et al 1973][research_sorensen_smeltzer_1973]
- [Johnson III and Wu 1974][research_johnsoniii_wu_1974]

#### The Standard the Design Had to Meet

The military engine specification of the era defines a reference recovery against which an inlet is judged.
It is an engineering standard rather than a law of nature, which makes it exactly the right yardstick for a
claim in a brochure.

$$ \eta_{\mathrm{ref}} = 1 - 0.075\,(M - 1)^{1.35}, \qquad M > 1 $$

| Mach | Reference recovery |
|---|---|
| 1.5 | 0.9706 |
| 2.0 | 0.9250 |
| 2.2 | 0.9041 |
| 2.6 | 0.8585 |
| 3.0 | 0.8088 |

#### The Cheapest Possible Inlet, and Why It Will Not Do

A [pitot inlet][ref_pitot_inlet] is a hole facing forward. The air crosses one
[normal shock][ref_normal_shock] and that is the whole of the compression. The total-pressure ratio across a
normal shock is a closed form.

$$ \frac{p_{t2}}{p_{t1}} = \left[\frac{(\gamma+1)M^2}{2 + (\gamma-1)M^2}\right]^{\frac{\gamma}{\gamma-1}} \left[\frac{\gamma+1}{2\gamma M^2 - (\gamma-1)}\right]^{\frac{1}{\gamma-1}} $$

$$ \eta_{\mathrm{pitot}}(2.0) = 0.7209, \qquad \eta_{\mathrm{pitot}}(2.6) = 0.4601 $$

**At Mach 2.6 a pitot inlet throws away more than half the total pressure.** This is why every supersonic
aircraft of the period carried something more elaborate, and it sets the scale of what the cone is buying.

#### One Cone, Computed Rather Than Assumed

A conical spike ahead of the cowl generates a conical shock. The air crosses that oblique shock first,
losing much less total pressure than it would across a normal shock at the same free-stream Mach number, and
then crosses a weaker normal shock at the throat.

**The flow behind a conical shock is not uniform**, which is what distinguishes it from the two-dimensional
wedge case and what makes it require an integration rather than a formula.

The conical-flow literature is a distinct body of work from the inlet literature that uses it, and it is
where the tabulations that made the integration usable before computers were published.

- [Browne et al 1948][research_browne_friedman_1948]
- [Jack 1951][research_jackjohnr_1951]
- [Moeckel and Evans 1951][research_moeckelwe_evanspjjr_1951]
- [Solomon 1955][research_solomongeorgee_1955]
- [Stewart 1956][research_stewart_1956]
- [Briggs 1960][research_briggsbenjaminr_1960]
- [Hsu and Anderson 1961][research_hsu_anderson_1961]
- [Hrubecky 1963][research_hrubecky_1963]
- [Panov et al 1966][research_panov_shvets_1966]
- [Panov and Shvets 1967][research_panov_shvets_1967]
- [Vasil'ev 1970][research_vasilev_1970]
- [Davis 1971][research_davis_1971]
- [Jones 1972][research_jones_1972]
- [Kayser and Danberg 1974][research_kayser_danberg_1974]
- [Yamanaka and Kamimura 1975][research_yamanaka_kamimura_1975]
- [Hui 1975][research_hui_1975]
- [Isugiyama 1976][research_isugiyama_1976]
- [Sugiyama 1977][research_sugiyama_1977]

The governing relation is the
[Taylor-Maccoll equation][ref_taylor_maccoll], written here for the velocity components normalised by the
maximum adiabatic velocity.

$$ \frac{dV_r'}{d\theta} = V_\theta' $$

$$ \frac{dV_\theta'}{d\theta} = \frac{V_r' V_\theta'^2 - a'^2\left(2V_r' + V_\theta' \cot\theta\right)}{a'^2 - V_\theta'^2}, \qquad a'^2 = \frac{\gamma-1}{2}\left(1 - V_r'^2 - V_\theta'^2\right) $$

**Every oblique shock relation reduces to a normal one through the component of Mach number along the wave**,
which is the bookkeeping that lets a single set of formulae serve both cases.

$$ M_{n1} = M_1 \sin\beta $$

$$ M_{2}^{2} = \frac{1 + \frac{\gamma-1}{2}M_{n1}^{2}}{\gamma M_{n1}^{2} - \frac{\gamma-1}{2}} \bigg/ \sin^{2}(\beta - \theta_d) $$

The wave angle cannot fall below the Mach angle, which is the weakest disturbance the flow will carry and
therefore the lower bound on every search below. The oblique-shock and Mach-angle relations are standard, in
[Shapiro][book_shapiro] and [Anderson][book_anderson], and the inlet application of them is
[Seddon and Goldsmith][book_seddon_goldsmith].

$$ \mu = \arcsin\frac{1}{M}, \qquad \mu(2.0) = 30.00^\circ, \qquad \mu(2.6) = 22.62^\circ $$

The integration starts immediately behind the shock, where the [oblique shock][ref_oblique_shock] relations
give the deflection from the wave angle $\beta$,

$$ \tan\theta_d = 2\cot\beta\,\frac{M_1^2 \sin^2\beta - 1}{M_1^2(\gamma + \cos 2\beta) + 2} $$

and proceeds inward until the flow becomes tangent to a surface, which is the cone.
**The problem is solved in the inverse direction**, because Taylor-Maccoll integrates from a known shock
angle to whatever cone that shock implies, so a wanted cone angle is reached by search.

Running that integration and following it with a normal shock at the throat gives the recovery of a
single-cone inlet.

| Cone half-angle | Mach 2.0 shock | Mach 2.0 recovery | Mach 2.6 shock | Mach 2.6 recovery |
|---|---|---|---|---|
| 15° | 33.91° | 0.8515 | 27.69° | 0.6243 |
| 20° | 37.80° | 0.8980 | 31.86° | 0.6881 |
| 25° | 42.53° | 0.9245 | 36.64° | 0.7315 |
| 27.5° | 45.20° | 0.9269 | 39.23° | 0.7421 |
| 30° | 48.08° | 0.9210 | 41.94° | 0.7442 |
| 32.5° | 51.23° | 0.9061 | 44.78° | 0.7373 |
| 35° | 54.75° | 0.8822 | 47.77° | 0.7215 |
| 37.5° | detached | none | 50.95° | 0.6968 |

**This table contains the article's central technical result.**

**At Mach 2.0 the best single cone reaches 0.9269 against a reference of 0.9250.** It clears the standard,
by two-tenths of a point. The F-104's arrangement was adequate for the speed it was built for, which is
unsurprising and is the control that shows the method is not biased against the design.

**At Mach 2.6 the best single cone reaches 0.7442 against a reference of 0.8585. It falls short by 11.44 points.**

**And that shortfall is a floor rather than an estimate**, which is the part worth dwelling on. The
calculation above is inviscid. It charges nothing for boundary-layer bleed, nothing for duct friction,
nothing for the diffuser, and nothing for operating away from the design point.
**A real inlet does worse than this.** The reference standard, by contrast, is what a competent real inlet
was expected to achieve including all of those losses.
**An idealised calculation that still cannot reach a practical standard has established the shortfall as real rather than as an artefact of pessimistic assumptions.**

#### Two Ramps, and Why the Intakes Became Rectangular

A rectangular intake can carry two or more plane compression ramps where a round one carries a single cone.
Each additional oblique shock takes a share of the compression, and spreading the compression across more
and weaker shocks costs less total pressure than concentrating it, which is the [Oswatitsch][ref_oswatitsch]
result.

Computing the two-ramp arrangement requires the same oblique-shock relation applied twice, followed by a
normal shock.

$$ \eta_{\mathrm{2-ramp}} = \frac{p_{t2}}{p_{t1}}\bigg|_{\delta_1} \cdot \frac{p_{t3}}{p_{t2}}\bigg|_{\delta_2} \cdot \frac{p_{t4}}{p_{t3}}\bigg|_{\mathrm{normal}} $$

**The result that says how to divide the compression is [Oswatitsch's][ref_oswatitsch], and it is worth writing down.**
For a given number of oblique shocks the recovery is greatest when they are of equal strength, meaning equal
normal Mach components.

$$ M_1 \sin\beta_1 = M_2 \sin\beta_2 = \cdots = M_n \sin\beta_n $$

**That is a theorem worth checking rather than quoting**, and a fair check holds both searches to the same
constraint. An equal pair searched without the turning constraint, set against an unequal pair searched with
it, appears to win only by exceeding a limit the other obeys. Under the same twenty-five degree cap the two
agree closely.

| Mach | Best equal pair | Recovery | Best free pair | Recovery | Free advantage |
|---|---|---|---|---|---|
| 2.0 | 10.8° + 10.8° | 0.9569 | 10.4° + 11.1° | 0.9570 | 0.010 points |
| 2.6 | 12.5° + 12.5° | 0.8251 | 11.4° + 13.6° | 0.8261 | 0.104 points |

**The free optimum beats the equal-strength arrangement by a tenth of a point at most, which confirms the theorem rather than contradicting it.**

**The search must be constrained or it returns nonsense.** An unconstrained optimisation returns four
degrees followed by twenty at Mach 2.0, for a recovery of 0.9974, and that is arithmetic rather than a
design. A total deflection of thirty-six degrees has to be turned back at the cowl and would separate the
duct. Capping total turning at twenty-five degrees, which is about what external compression can physically
deliver, gives usable answers.

| Mach | Best two-ramp | Recovery | Mach before the normal shock | Gain over the best single cone |
|---|---|---|---|---|
| 2.0 | 10° + 11° | 0.9567 | 1.243 | +2.98 points |
| 2.6 | 11° + 14° | 0.8260 | 1.603 | +8.18 points |

**The two-ramp arrangement recovers 8.18 of the 11.44 points the single cone gives away at Mach 2.6, and only 2.98 points at Mach 2.0 where nothing needed recovering.**

**The record states that the X-27 was to have rectangular intakes and does not say why. This is why.** The
article states plainly that this is an inference from the physics and not a documented rationale, and it is
offered as an explanation that fits rather than as a discovered intention. It is, however, an explanation
with a sharp signature, since the change buys almost nothing at the speed the CL-1200 was sold at and a
great deal at the speed the X-27 was to be tested at, which is exactly the pattern one would expect if the
change was made for the test programme.

The literature on inlet-engine compatibility, distortion, and the compressor's response to it is the other
half of this subject, gathered in the clusters on inlet distortion and inlet-engine compatibility and on
compressor stall, surge and casing treatment below. The compatibility procedures and surveys of the period
are these.

- [Esenwein and Schueller 1952][research_esenweinfredt_schuellercarlf_1952]
- [Campbell and Ellis 1971][research_campbell_ellis_1971]
- [Williams and Yost 1973][research_williams_yost_1973]
- [Calogeras and Burstadt 1974][research_calogerasje_burstadtpl_1974]
- [Bowditch and Coltrin 1983][research_bowditchdn_coltrinre_1983]

#### Why the Engine Choice Makes the Inlet Harder

The TF30 is the wrong engine to put behind a marginal inlet, and this is documented rather than inferred.
**The engine was prone to compressor stall at high angle of attack when the throttle was moved sharply**,
and in the [F-14][ref_f14], whose widely separated nacelles turned a stall into asymmetric thrust, it was
dangerous enough to threaten departure. The [F-111][ref_f111] suffered less because its mission involved
gentler handling.

**A fan is more sensitive to inlet distortion than a turbojet's compressor**, because the fan's outer span
operates at high relative Mach number and low solidity, and a circumferential total-pressure defect passing
through it appears as a rotating incidence excursion.
**The Lancer's inlets sit on the sides of a fuselage, ahead of a wing, at whatever angle of attack the aeroplane is flying.**

The literature on compressor stall and surge, its inception, and its suppression is one of the most
sustained programmes in turbomachinery.

- [Huppert and Benser 1953][research_huppert_benser_1953]
- [Emmons et al 1955][research_emmons_pearson_1955]
- [Valensi 1958][research_valensi_1958]
- [Sovran 1959][research_sovran_1959]
- [Strub and Suter 1965][research_strub_suter_1965]
- [Gray 1969][research_gray_1969]
- [Mays 1971][research_mays_1971]
- [Marshall 1973][research_marshall_1973]
- [Amann et al 1975][research_amann_nordenson_1975]
- [Tanaka and Murata 1975][research_tanaka_murata_1975_b]
- [Tanaka and Murata 1975][research_tanaka_murata_1975_c]
- [Tanaka and Murata 1975][research_tanaka_murata_1975]
- [Daniele and Teren 1975][research_daniele_teren_1975]
- [Daniele and Teren 1975][research_danielecj_terenf_1975]
- [McQueen 1976][research_mcqueen_1976]
- [Greitzer 1976][research_greitzer_1976]
- [Greitzer 1976][research_greitzer_1976_b]
- [Dean and Young 1977][research_dean_young_1977]
- [Ohyama 1978][research_ohyama_1978]
- [Day et al 1978][research_day_greitzer_1978]
- [Tondl 1979][research_tondl_1979]
- [Kolnsberg 1979][research_kolnsberg_1979]
- [Ludwig 1979][research_ludwig_1979]
- [Cossar et al 1980][research_cossar_moffatt_1980]
- [Greitzer 1980][research_greitzer_1980]
- [Stenning 1980][research_stenning_1980_b]
- [Hansen et al 1981][research_hansen_jorgensen_1981]
- [Kosuge et al 1982][research_kosuge_ito_1982]
- [Cumpsty and Greitzer 1982][research_cumpsty_greitzer_1982]
- [Wasserbauer et al 1985][research_wasserbauerjf_neumannhe_1985]
- [Boussios et al 1992][research_boussios_epstein_1992]

**This article does not claim the Lancer would have suffered the F-14's problems.** It had a single engine,
so asymmetry was not available to it, and its inlets are differently placed. What it does claim is narrower
and better supported.
**The combination the X-27 proposed put a distortion-sensitive engine behind an inlet that the calculation above shows was working near its limit, at a Mach number beyond anything the installation's ancestor had flown, and the record contains no evidence that the combination was ever tested in any facility.**

### The Spike Travel, Inverted

The cone must move. As Mach number rises the conical shock lies closer to the axis, so holding the shock on
the cowl lip requires the apex to move forward.

With the apex a distance $L$ ahead of the lip and the lip at radius $r$, the shock-on-lip condition is
purely geometric.

$$ \tan\beta = \frac{r}{L} \qquad \Longrightarrow \qquad L = \frac{r}{\tan\beta} $$

The travel needed between two Mach numbers follows immediately.

$$ \Delta L = r\left(\cot\beta_{\mathrm{hi}} - \cot\beta_{\mathrm{lo}}\right) $$

The shock-on-lip condition and the capture-area bookkeeping that follows it are set out in
[Seddon and Goldsmith][book_seddon_goldsmith].

**The record gives the travel and not the radius.** Four inches of movement is documented, but the diameter
of the Lancer's inlets is not. **So the relation is inverted**, which is the honest move when a parameter is
unknown, and it turns a quoted number into a checkable one.

$$ r = \frac{\Delta L}{\cot\beta_{\mathrm{hi}} - \cot\beta_{\mathrm{lo}}} $$

Taking the shock held on the lip from Mach 2.0 to Mach 2.6, and the two side inlets as half-cones so that
their combined capture area is $\pi r^2$,

| Cone half-angle | Shock at M 2.0 | Shock at M 2.6 | Implied lip radius | Implied total capture area |
|---|---|---|---|---|
| 20° | 37.80° | 31.86° | 12.51 in | 3.417 ft² |
| 25° | 42.53° | 36.64° | 15.73 in | 5.401 ft² |
| 27.5° | 45.20° | 39.23° | 17.26 in | 6.500 ft² |
| 30° | 48.08° | 41.94° | 18.58 in | 7.535 ft² |

The literature on capture area, spike and cone geometry, mass-flow ratio and the spillage that follows from
operating away from the design point is where this calculation comes from. It is gathered in the cluster on
supersonic inlets, shock systems and pressure recovery below, and the translating-spike and additive-drag
work closest to this calculation is this.

- [Gorton 1953][research_gortongeraldc_1953]
- [Gorton 1954][research_gortongeraldc_1954]
- [Connors and Wise 1957][research_connorsjamesf_wisegeorgea_1957]
- [Barry 1971][research_barry_1971]
- [Hawkins et al 1976][research_hawkinsje_kirklandfp_1976]

#### The Check That Makes This Worth Doing

An inversion that cannot be tested is a rearrangement. This one can be tested, because the engine's airflow
is documented independently.

The capture area needed to admit a given physical mass flow at full capture is

$$ A_c = \frac{\dot m}{\rho_\infty V_\infty} $$

**The TF30-P-100 is documented at 260 pounds per second, which is 117.93 kilograms per second**
\[[Pratt and Whitney TF30][ref_tf30]\]. At Mach 2.0
and 35,000 feet the free-stream mass flux is $\rho_\infty V_\infty = 225.0$ kilograms per square metre per
second, so

$$ A_c = \frac{117.93}{225.0} = 0.524\ \mathrm{m}^2 = 5.639\ \mathrm{ft}^2 $$

| Assumed cone half-angle | Implied capture from the travel | Required by the engine | Error |
|---|---|---|---|
| 20° | 3.417 ft² | 5.639 ft² | −39.4 percent |
| **25°** | **5.401 ft²** | **5.639 ft²** | **−4.2 percent** |
| 27.5° | 6.500 ft² | 5.639 ft² | +15.3 percent |
| 30° | 7.535 ft² | 5.639 ft² | +33.6 percent |

The error column is the implied capture area $A_{\mathrm{travel}}$ measured against the required one,
which at twenty-five degrees is

$$ \varepsilon = \frac{A_{\mathrm{travel}} - A_c}{A_c} = \frac{5.401 - 5.639}{5.639} = -0.042 $$

**A twenty-five degree cone reconciles the two published figures to within 4.2 percent, and twenty-five degrees is an entirely ordinary half-angle for a supersonic inlet of the period.**

**This is the strongest result in the article and it is worth being precise about why.** Two numbers were
published by different people for different purposes, namely a spike travel of four inches quoted as an
airframe feature, and an airflow of 260 pounds per second quoted as an engine rating.
**Neither was derived from the other.** Shock-on-lip geometry and a mass-flow balance connect them through a
cone angle that nobody published, and asking for a cone angle that satisfies both returns a thoroughly
conventional one.

**Reproducing two independent quoted figures from one model is worth considerably more than reproducing either alone**,
and it is the closest this subject comes to a measurement.

**What it does not establish** should be equally clear. It does not confirm the aircraft would have worked.
It confirms that the published airframe and engine figures are mutually consistent, which is evidence that
the design was worked out rather than sketched, and nothing beyond that.

#### A Note on Corrected Flow

Converting the engine's maximum *corrected* airflow to physical airflow at Mach 2.6 gives 356 kilograms per
second, three times the sea-level rating. The [corrected flow][ref_corrected_flow] relation is

$$ \dot m_{\mathrm{corr}} = \frac{\dot m \sqrt{\theta}}{\delta}, \qquad \theta = \frac{T_{t2}}{288.15}, \qquad \delta = \frac{p_{t2}}{101325} $$

**The arithmetic is right and the premise is wrong.** Corrected airflow and the engine matching it governs
are treated in [Oates][book_oates] and [Mattingly][book_mattingly_engine]. A compressor does not hold its
maximum corrected flow while its inlet total temperature rises by two hundred kelvin, because the corrected
speed falls and the operating point walks down the map.
**The engine's flow schedule at high Mach is not in the public record**, so the comparison above is made at
Mach 2.0 using physical flow, where the engine is near its rating and the assumption is defensible. The
point is stated because a number that is not credible is a finding rather than a nuisance.

### The Metric the Competition Actually Used

By 1970 the argument about fighters had moved. Top speed and rate of climb had been the currency of the
1950s, and the F-104 was designed to win on them.
**What replaced them was [energy manoeuvrability][ref_energy_maneuverability]**, the framework associated
with [John Boyd][ref_boyd] and [Thomas Christie][ref_christie], which asks not how fast an aircraft can go
but how much energy it can gain or hold while turning.

The framework's primitive is energy height, the altitude an aircraft would reach if it traded all its speed
for height without loss, and it is written out below. The treatment followed here is
[Whitford][book_whitford], with the equations of motion behind it in
[Stevens and Lewis][book_stevens_lewis].

**This heading is among the thinnest in the article and the thinness is a finding.** Of the research records
the article cites, one carries energy height, energy state or minimum time to climb in its title. **The subject is not small. It is indexed elsewhere**, inside trajectory optimisation and inside
the optimum-climb literature, and its foundational documents are Air Force internal reports that no journal
indexed.

- [Corner 1940][research_corner_1940]
- [Whittley 1952][research_whittley_1952]
- [Theodorsen 1959][research_theodorsen_1959]
- [Andrews 1969][research_andrews_1969]

$$ h_e = h + \frac{V^2}{2g} $$

At 15,000 feet and Mach 0.9 that is

$$ h_e = 4{,}572 + \frac{290.0^2}{2 \times 9.80665} = 4{,}572 + 4{,}289 = 8{,}861\ \mathrm{m} = 29{,}072\ \mathrm{ft} $$

The central quantity is [specific excess power][ref_specific_excess_power],
**which is the rate of change of that height and not an independent definition**.

$$ P_s = \frac{dh_e}{dt} = V\,\frac{T - D}{W} $$

**The thrust-to-weight ratio is the other term the comparison turns on**, and the table in What Changed From
the F-104 gives it without writing it out.

$$ \frac{T}{W} = \frac{25{,}000\ \mathrm{lbf}}{24{,}385\ \mathrm{lb}} = 1.025 $$

**A re-winged F-104 improves on the old metrics. The question is what it does to this one.**

The framework and its consequences for fighter design are set out in [Whitford][book_whitford], and Boyd's
own part in it is treated at length in [Coram][book_coram].

The literature on energy manoeuvrability, sustained turning performance and combat aircraft performance
comparison is smaller than the others treated here, and the article says so rather than padding it.

- [Tamboli 1956][research_tamboli_1956]
- [Marshall 1971][research_marshallrt_1971]
- [Herbst and Krogull 1973][research_herbst_krogull_1973]
- [Nelms and Bailey 1974][research_nelmswpjr_baileyro_1974]
- [Hill and Bowles 1976][research_hillgc_bowlesjv_1976]
- [Friend and Sakamoto 1978][research_friendel_sakamotogm_1978]

**That thinness is itself worth reporting.**
**The subject is not small. Its foundational documents are Air Force internal reports that were never journal articles**,
and Boyd's own work in particular is not indexed where the rest of this article's sources live.

### Building a Drag Polar Without a Measurement

The drag polar is the relation the whole manoeuvre argument runs through.

$$ C_D = C_{D_0} + K C_L^2 $$

**Neither coefficient is available for this aircraft**, so both are constructed, and the construction is
stated rather than buried.

#### The Parasite Term, Held Deliberately Constant

$C_{D_0}$ is estimated by the equivalent-skin-friction method of [Raymer][book_raymer], in which a
coefficient standing for friction, form, interference and roughness together is applied to the wetted area.
The drag data underlying such coefficients is [Hoerner][book_hoerner], and the sizing method is also given
by [Nicolai][book_nicolai].

$$ C_{D_0} = C_{fe}\,\frac{S_{\mathrm{wet}}}{S_{\mathrm{ref}}} = 0.0035 \times 4.5 = 0.0158 $$

**The same value is used for all four aircraft compared below, and that is a deliberate control rather than an approximation.**
Holding parasite drag equal turns the comparison into one about wing loading and thrust-to-weight, which is
the question being asked.
**Where the answer depends on the value, the sensitivity is reported instead of a number.**

#### The Induced Term, Where the Aerofoil Bites

$K$ is where the F-104's inheritance shows. The elliptical result assumes the leading edge develops its full
suction peak.

$$ K_{\mathrm{full}} = \frac{1}{\pi A e} $$

**A thin wing with a sharp leading edge cannot develop it.** The flow separates at the edge rather than
turning around it, and the limiting case is that the resultant force tilts back with the surface, so that

$$ K_{\mathrm{none}} = \frac{1}{C_{L_\alpha}} $$

At these aspect ratios the lift-curve slope is nowhere near $2\pi$, and using the high-aspect-ratio value
would understate the very penalty this section exists to measure. The form used is the one given by
[Raymer][book_raymer] and [Nicolai][book_nicolai]. The [Helmbold-Diederich][ref_helmbold] form applies.

$$ C_{L_\alpha} = \frac{2\pi A}{2 + \sqrt{4 + \dfrac{A^2\beta^2}{\eta^2}\left(1 + \dfrac{\tan^2\Lambda_{c/2}}{\beta^2}\right)}}, \qquad \beta = \sqrt{|1 - M^2|} $$

The real wing sits between the two limits, so the article blends them and
**reports the whole range rather than choosing a value**, because a conclusion that survives every
leading-edge suction fraction is worth more than a point estimate.

$$ K = s\,K_{\mathrm{full}} + (1 - s)\,K_{\mathrm{none}}, \qquad 0 \le s \le 1 $$

| Aircraft | Aspect ratio | $C_{L_\alpha}$ at M 0.9 | $K$ at $s=0$ | $K$ at $s=0.5$ | $K$ at $s=1$ |
|---|---|---|---|---|---|
| F-104G | 2.455 | 3.592 | 0.2784 | 0.2113 | 0.1441 |
| CL-1200-2 | 2.836 | 4.064 | 0.2460 | 0.1854 | 0.1247 |
| F-5E | 3.824 | 5.158 | 0.1939 | 0.1432 | 0.0925 |
| F-15A | 3.014 | 4.275 | 0.2339 | 0.1756 | 0.1173 |

The literature on low-aspect-ratio and thin-wing aerodynamics, leading-edge behaviour, wave drag and the
area rule underpins every line of that table, and it is gathered in the clusters on wings, aspect ratio and
vortex flows and on drag polars, wave drag and supersonic aerodynamics below. The period work on low aspect
ratio wings, drag due to lift, leading-edge suction and the area rule includes these.

- [Hall and Heitmeyer 1951][research_hallcharlesf_heitmeyerjohnc_1951]
- [Bertram and Ulmann 1953][research_bertrammh_ulmannef_1953]
- [Osborne and Kelly 1953][research_osborneroberts_kellythomasc_1953]
- [Whitcomb 1953][research_whitcombrichardt_1953]
- [Hancock 1959][research_hancock_1959_b]
- [Polhamus 1966][research_polhamusec_1966]

### Sustained Turning

An aircraft holds a turn when thrust equals drag at the load factor concerned. Setting $T = D$ and
substituting the lift coefficient required at load factor $n$,

$$ C_L = \frac{n W}{q S} $$

then solving for the load factor gives

$$ n_{\mathrm{sus}} = \sqrt{\frac{q S}{K W}\left(\frac{T}{W} - \frac{q S C_{D_0}}{W}\right)} $$

and the turn rate follows from the load factor and the speed, as does the radius, which is the other axis of
the diagram this framework is usually drawn on.

$$ \dot\psi = \frac{g\sqrt{n^2 - 1}}{V} $$

$$ R = \frac{V^2}{g\sqrt{n^2 - 1}} $$

The load factor is also what the bank angle costs, in level flight.

$$ n = \frac{1}{\cos\phi} $$

At the sustained load factor computed below the Lancer is banked at

$$ \phi = \arccos\frac{1}{6.34} = 80.9^\circ, \qquad R = \frac{290.0^2}{9.80665\sqrt{6.34^2 - 1}} = 1{,}371\ \mathrm{m} = 4{,}496\ \mathrm{ft} $$

Evaluating at 15,000 feet and Mach 0.9, a representative combat condition, gives the comparison the whole
sales case rested on.

| Suction | Aircraft | Sustained $n$ | Turn rate | $P_s$ at 1 g |
|---|---|---|---|---|
| 0.0 | F-104G | 2.94 | 5.36 °/s | 416 ft/s |
| 0.0 | **CL-1200-2** | **5.50** | **10.48 °/s** | **823 ft/s** |
| 0.0 | F-5E | 4.58 | 8.67 °/s | 461 ft/s |
| 0.0 | F-15A | 6.06 | 11.58 °/s | 860 ft/s |
| 0.5 | F-104G | 3.38 | 6.25 °/s | 430 ft/s |
| 0.5 | **CL-1200-2** | **6.34** | **12.13 °/s** | **830 ft/s** |
| 0.5 | F-5E | 5.33 | 10.15 °/s | 467 ft/s |
| 0.5 | F-15A | 6.99 | 13.41 °/s | 866 ft/s |
| 1.0 | F-104G | 4.09 | 7.68 °/s | 443 ft/s |
| 1.0 | **CL-1200-2** | **7.73** | limit binds | 836 ft/s |
| 1.0 | F-5E | 6.64 | 12.71 °/s | 473 ft/s |
| 1.0 | F-15A | 8.56 | limit binds | 872 ft/s |

**The weights behind the table are sourced, but they are not equally loaded.** The F-104G, F-5E and F-15A
are evaluated at the design gross weights and afterburning thrusts that the National Aeronautics and Space
Administration's survey tabulates \[[Quest for Performance, NASA SP-468][ref_sp468]\]. The survey gives the
F-15C and not the F-15A, so the F-15A rows use the F-15C's 44,500 pounds and two F100-PW-100 engines of
23,904 pounds of thrust, the nearest variant it tabulates. The CL-1200-2 is evaluated at its normal loaded
weight of 24,385 pounds. As fractions of each aircraft's maximum weight these are

$$ \frac{27{,}300}{29{,}083} = 0.939, \qquad \frac{15{,}745}{20{,}486} = 0.769, \qquad \frac{44{,}500}{68{,}000} = 0.654, \qquad \frac{24{,}385}{35{,}000} = 0.697 $$

for the F-104G, F-5E, F-15A and CL-1200-2 respectively. **The F-104G is carried much nearer its maximum
than the others**, so its rows understate it by an amount the sources do not allow to be fixed. They bound
the F-104G from below and are not a like-for-like measure of what the redesign gained.

The period and contemporary work on turning performance, load factor and combat aircraft comparison stands
behind this table.

- [Pennington and Meintel 1980][research_penningtonje_meintelajjr_1980]
- [Schneider 1990][research_schneideredwardt_1990]
- [Wilson et al 1993][research_wilson_riley_1993]
- [Ngan and Biezad 1996][research_nganangelen_biezaddaniel_1996]

**The result is favourable to Lockheed and it is robust.** At every leading-edge suction fraction the Lancer
out-turns the F-5E that beat it, comfortably, and it sits close behind the F-15A.

**The specific excess power comparison is the striking one. At 830 feet per second against the F-15A's 866, the Lancer is within 4.2 percent of an aeroplane that cost several times as much.**
The shortfall is taken relative to the F-15A at a leading-edge suction fraction of 0.5,

$$ 1 - \frac{P_{s,\mathrm{CL\text{-}1200\text{-}2}}}{P_{s,\mathrm{F\text{-}15A}}} = 1 - \frac{830}{866} = 0.042 $$

The ranking does not depend on the parasite drag assumption.

| $C_{D_0}$ | F-104G | CL-1200-2 | F-5E | F-15A |
|---|---|---|---|---|
| 0.0150 | 3.39 | 6.36 | 5.36 | 7.02 |
| 0.0175 | 3.35 | 6.29 | 5.26 | 6.93 |
| 0.0200 | 3.30 | 6.21 | 5.15 | 6.84 |
| 0.0250 | 3.22 | 6.06 | 4.93 | 6.66 |

**A model with a free parameter that reproduces an expectation has demonstrated very little.** What this one
has demonstrated is narrower and firmer, because
**the ordering is invariant across the whole plausible range of both free parameters**, which is a statement
about the ordering and not about the absolute numbers, and the absolute numbers should not be quoted as
predictions of what the aircraft would have achieved.

**And it makes the political story quantitative.** The claim that some in the Air Force saw the Lancer as a
threat to the F-15 is usually reported as an attitude.
**The arithmetic says the attitude was not unreasonable.** An aeroplane within 4.2 percent of the F-15's
specific excess power, offered at a fraction of the price, is an awkward thing to have flying while the case
for the expensive one is before Congress.
**The article states this as a consistency between the physics and the reported attitude, not as evidence of anyone's motive.**

### Corner Speed and the Limit That Actually Binds

The corner speed is the lowest speed at which the structural limit load factor can be reached
aerodynamically.

$$ V^* = \sqrt{\frac{2\,n_{\mathrm{limit}}\,W}{\rho\,S\,C_{L_{\max}}}} $$

| $C_{L_{\max}}$ | Stall speed at sea level | Corner speed at 15,000 ft | Mach |
|---|---|---|---|
| 1.0 | 154.9 kt | 528.9 kt | 0.844 |
| 1.2 | 141.4 kt | 482.8 kt | 0.771 |
| 1.4 | 131.0 kt | 447.0 kt | 0.713 |

The corner speed is built on the stall speed, which is the same relation at a load factor of one, and both
are standard sizing relations in [Raymer][book_raymer] and [Nicolai][book_nicolai].

$$ V_{\mathrm{stall}} = \sqrt{\frac{2W}{\rho\,S\,C_{L_{\max}}}} , \qquad V^{*} = \sqrt{n_{\mathrm{limit}}}\;V_{\mathrm{stall}} $$

**The maximum lift coefficient is the weakest input in this article.** A thin sharp-edged wing of aspect
ratio 2.8 does not achieve much of one, and the record supplies no figure. The table is therefore given
across a range and no single value is asserted.

The literature on high lift, boundary-layer-control blowing, and approach-speed reduction bears directly on
this, and the F-104 needed blown flaps to land at all. It is gathered in the cluster on boundary-layer control,
high lift and short take-off below, and the blown-flap work on swept-wing aircraft of the F-104's period
includes these.

- [Kelly et al 1958][research_kellymarkw_andersonsethb_1958]
- [Maki 1959][research_makiralphl_1959]
- [Quigley et al 1960][research_quigleyherveyc_andersonsethb_1960]
- [Williams and Butler 1963][research_williams_butler_1963]

## Dependent Systems

**Every system below is dimensioned against the keystone rather than described for its own sake.** The order
is by dependency, since the engine change drives the fuselage, the fuselage drives the intakes, and the wing
follows from the manoeuvre requirement that the engine change made reachable.

### Propulsion

Treated at length above.
**The summary is that the engine change is the largest single change in the aircraft and the one that drives most of the others.**
Against the J79-GE-17 it is 33.01 inches longer, 9.84 inches wider, and it swallows 52.9 percent more air, differences computed in the section headed [What Changed From the F-104](#what-changed-from-the-f-104). The fuselage stretch,
the redesigned centre and rear fuselage, the enlarged intakes and the translating cones all follow from it.

The engine literature is gathered in the cluster on turbofans, turbojets and installed thrust below, and the
work on turbojets and turbofans for supersonic fighters nearest this aircraft's case includes these.

- [Gabriel et al 1953][research_gabrieldavids_krebsrichardp_1953]
- [Branstetter et al 1971][research_branstetterjr_juhaszaj_1971]
- [Dugan 1972][research_duganjfjr_1972]
- [McAulay and Abdelwahab 1972][research_mcaulayje_abdelwahabm_1972]
- [Franciscus 1987][research_franciscusleoc_1987]

#### Ram Drag, Which the Keystone Needs

**An engine at high Mach spends a large part of its gross thrust cancelling the momentum of the air it swallowed.**
Net thrust is the difference between what leaves and what arrived.

**The literature under this heading is genuinely thin and the reason is worth stating.** Of the research records
the article cites, three carry ram drag, momentum drag or installed performance in their titles, all of them
in the contemporary survey and none in the list under this heading. **The subject is not thin. The heading is.** Thrust and drag bookkeeping
is settled inside the papers on inlet additive drag and spillage already cited above, because deciding what
counts as inlet drag and what counts as lost thrust is the same accounting question.

- [Stephenson 1953][research_stephenson_1953]
- [Davidson 1964][research_davidson_1964]
- [Lewis 1976][research_lewis_1976]
- [Bull and Bridges 1983][research_bullg_bridgespd_1983]

$$ F_{\mathrm{net}} = \dot m\left(V_e - V_0\right) $$

The second term is the ram drag, and at Mach 2.6 the free stream arrives at 771 metres per second.

$$ D_{\mathrm{ram}} = \dot m V_0 = 117.93 \times 771.0 = 90{,}926\ \mathrm{N} = 20{,}441\ \mathrm{lbf} $$

**The engine's rated 25,000 pounds of net thrust therefore requires 45,441 pounds gross, so 45.0 percent of the gross thrust is spent on the air's own momentum.**

The thrust equation and the propulsive efficiency that follows from it are standard, in [Oates][book_oates]
and [Mattingly][book_mattingly_engine].

**The relation is more useful inverted than asserted**, because holding the sea-level rating across the
whole Mach range is not defensible. Asking instead what exhaust velocity the rating would require at that
condition gives a checkable number.

$$ V_e = \frac{F_{\mathrm{net}} + \dot m V_0}{\dot m} = \frac{111{,}206 + 90{,}926}{117.93} = 1{,}714\ \mathrm{m/s} $$

$$ V_{e,\,\mathrm{static}} = \frac{F_{\mathrm{net}}}{\dot m} = \frac{111{,}206}{117.93} = 943\ \mathrm{m/s} $$

**Seventeen hundred metres per second is within reach of an afterburning nozzle, so the requirement is not absurd.**
What it is not is free. A higher exhaust velocity needs a higher total pressure at the engine face,
**and total pressure at the engine face is precisely what the inlet section showed the single cone failing to deliver at this Mach number.**
The two halves of the keystone are the same problem seen from either end.

The propulsive efficiency at that condition follows.

$$ \eta_p = \frac{2V_0}{V_0 + V_e} = \frac{2 \times 771.0}{771.0 + 1714} = 0.621 $$

### Aerodynamics

The wing grew 53.0 percent in area and 33.0 percent in span while retaining the F-104's aerofoil section,
its 3.36 percent thickness ratio and its 10 degrees of anhedral. **Aspect ratio rose only 15.5 percent**,
from 2.455 to 2.836, because the area grew nearly as fast as the span squared.

The lift the wing produces is the coefficient carried on the dynamic pressure and the area, which is the
identity every load factor below is measured against, and the drag data behind the coefficients used with it
is [Hoerner][book_hoerner], with the configuration context in [Kuchemann][book_kuchemann].

$$ L = q\,S\,C_L $$

**That is the limit of what the redesign could do without a new wing.** The induced-drag penalty of a low
aspect ratio is not much relieved by going from 2.455 to 2.836, and the table above shows the Lancer's $K$
remaining above the F-5E's at every suction fraction.
**What made the Lancer competitive was not the wing. It was the thrust.**

Moving the wing to the shoulder position has consequences the record does not discuss and this article does
not resolve. A high wing changes the interference field at the wing-body junction, alters the downwash at
the tail, and modifies the rolling moment due to sideslip, which is presumably why 10 degrees of anhedral
was retained on a configuration whose wing position already supplies an effective dihedral increment.

### Stability and Control

The equations of motion and the stability derivatives behind this discussion are set out in
[Stevens and Lewis][book_stevens_lewis].

**Moving the tail off the fin is the most defensible change in the aircraft.** A T-tail on a
low-aspect-ratio wing risks the horizontal surface entering the wing wake at high angle of attack, whereupon
pitch control is lost while the aircraft is already pitching up. The F-104 had a well-documented and
unforgiving departure behaviour.

The tail's contribution to longitudinal stability is carried by the tail volume coefficient, which collects
the geometry into one number, and by the rate at which the wing's downwash turns the flow the tail sees.

Downwash surveys behind wings, neutral-point determination and the static longitudinal stability of wing and
tail combinations are among the oldest quantitative subjects in the field, and the measurements behind the
relations below are mostly period work. They are gathered in the clusters on wings, aspect ratio and vortex
flows and on stability, control and flying qualities below, and the period downwash and neutral-point work
includes these.

- [Report No. 648, Design charts for predicting downwash angles...][research_report_no_1939]
- [Ward 1949][research_ward_1949]
- [Spreiter and Sacks 1951][research_spreiter_sacks_1951]
- [Baron 1953][research_baron_1953]

$$ V_H = \frac{S_t\,l_t}{S\,\bar{c}} $$

$$ C_{m_\alpha,\,\mathrm{tail}} = -a_t\,V_H\,\eta_t\left(1 - \frac{d\varepsilon}{d\alpha}\right) $$

$$ \mathrm{SM} = -\frac{C_{m_\alpha}}{C_{L_\alpha}} = \frac{x_{np} - x_{cg}}{\bar{c}} $$

**The tail geometry of the CL-1200 is not in the public record**, so these are written to show what the
change acted on rather than to produce a number, and no static margin is asserted.

**One thing they do let us test is an expectation that turns out to be wrong.** The far-field downwash
gradient goes inversely with aspect ratio, which invites the conclusion that a low-aspect-ratio wing washes
its tail harder and therefore suffers more.

$$ \frac{d\varepsilon}{d\alpha} \approx \frac{2\,C_{L_\alpha}}{\pi A} $$

| Aircraft | Aspect ratio | $C_{L_\alpha}$ | Far-field $d\varepsilon/d\alpha$ |
|---|---|---|---|
| F-104G | 2.455 | 3.592 | 0.931 |
| CL-1200-2 | 2.836 | 4.064 | 0.912 |
| F-15A | 3.014 | 4.275 | 0.903 |
| F-5E | 3.824 | 5.158 | 0.859 |

**The expectation does not survive being written down.** The lift-curve slope falls with aspect ratio at
very nearly the same rate as the divisor, so the ratio is almost flat, and the F-104 differs from the F-5E
by eight percent rather than by the large factor the framing implied.
**The negative is reported rather than dropped**, and it means the tail-position argument has to rest on the
wake geometry at high angle of attack, which it does, rather than on a downwash gradient that does not
discriminate. The far-field form also overestimates what a tail at a finite distance actually sees, so the
absolute values should not be read as tail conditions.

The wake geometry and pitch-up literature the argument rests on is gathered in the cluster on stability,
control and flying qualities below, and it includes these.

- [Anderson and Bray 1951][research_andersonsethb_brayrichards_1951]
- [Queijo and Wolhart 1951][research_queijomj_wolhartwalterd_1951]
- [Ray and Taylor 1965][research_rayej_taylorrt_1965]
- [Powers 1966][research_powersbg_1966]
- [Bihrle and Barnhart 1982][research_bihrle_barnhart_1982]

### Structure and Materials

The airframe is aluminium alloy, and the analysis above establishes that this is the constraint the Mach 2.6
objective runs into. **At Mach 2.0 the structure gives up about a tenth of its yield strength and at Mach 2.6 about a third**, and the
transition happens across a narrow band because the recovery temperature goes as the square of the Mach
number while the strength curve falls steeply through the same range.

### Armament and Stores

Nine stations, one on the fuselage centreline, three under each wing and one at each wingtip. The gun is the
20 millimetre [M61][ref_m61] with 725 rounds, with a 30 millimetre [DEFA][ref_defa] cannon of the French Direction des Études et Fabrications
d'Armement offered as an alternative for customers already equipped for it. Up to 12,000 pounds of ordnance on short-range missions,
a maximum of four [AIM-7][ref_aim7] or typically six and up to ten [AIM-9][ref_aim9] air intercept
missiles \[[Lockheed CL-1200 Lancer][ref_cl1200]\].

**The wingtip stations are inherited thinking.** The F-104 carried tip tanks and tip-mounted missiles
because it had almost no wing to hang anything under. On a wing half again as large the tip station is a
choice rather than a necessity, and a tip store on a short span carries a large rolling-inertia penalty into
exactly the rapid rolling manoeuvres the aircraft was being sold on.

### Instrumentation

**Nothing is known about what an X-27 would have carried, because no X-27 was instrumented.** A research
aircraft built to test propulsion at Mach 2.6 would have needed inlet rakes, engine-face pressure
instrumentation dense enough to compute a distortion descriptor, and skin thermocouples. The article notes
what such a programme would have required and asserts nothing about what was planned.

## The Flight Test Record

**There is none.**

Its emptiness is the most important fact about the subject. **No X-27 was built. No CL-1200 was built. Nothing flew.**

What exists is the following, and the article is careful to distinguish the well-attested from the reported.

- **Well attested.** One full-scale mock-up, of wood with a metal skin, completed in a Lockheed hangar.
- **Reported.** Up to three fuselages worked to some degree of completion before termination.
- **Well attested.** The design was entered in two competitions, in 1970 and 1972, and lost both.
- **Absent.** Any wind-tunnel report, any test facility record, any engine run, any flight.

**An article about an aeroplane that never flew is not thereby an article without evidence.** The evidence
is the design record and the parent aircraft, and the preceding sections have used both. What must not
happen is the quiet substitution of a prediction for a measurement, and the next section exists to prevent
it.

## Comparison With Ground Prediction

**In every other article in this series, this section compares what was predicted on the ground with what was measured in the air. Here there is no air.**

So the comparison is between the manufacturer's prediction and an independent prediction, and
**that is a much weaker thing**, because two predictions that agree may share an assumption rather than
share a truth. The section is written to make the weakness explicit rather than to disguise it.

| Claim | Independent estimate | Verdict |
|---|---|---|
| 1,700 mph at 35,000 ft | Mach 2.563 by definition | Internally consistent |
| Initial climb 60,000 ft/min | Best sea-level $P_s$ 49,332 ft/min | **Claim exceeds the estimate by 21.6 percent** |
| Takeoff run 1,450 ft | 1,078 ft at $C_{L_{\max}}$ 1.2 | Claim is conservative |
| Combat radius 367 nmi | 0.192 of still-air range | Consistent with practice |
| Fuel increase 46 percent | Needs the F-104G's internal fuel, which no cited source states | **Not checked** |
| Spike travel 4 in | Implies 5.401 ft² against 5.639 ft² needed | **Agrees to 4.2 percent** |

The claims in the first column are the manufacturer's published estimates \[[Lockheed CL-1200 Lancer][ref_cl1200]\].

### The Climb Claim, Which Does Not Check Out

Specific excess power is a hard ceiling on steady rate of climb, and the reason is one line of algebra
rather than an assertion, as [Whitford][book_whitford] sets out. Differentiating energy height and holding
speed constant leaves the climb rate equal to $P_s$, and any acceleration takes from the same budget.

$$ \frac{dh_e}{dt} = \frac{dh}{dt} + \frac{V}{g}\frac{dV}{dt} = P_s \qquad \Longrightarrow \qquad \left.\frac{dh}{dt}\right|_{\max} = P_s $$

The claimed 60,000 feet per minute is 305 metres per second, and the best $P_s$ the published thrust and
weight produce at sea level is 250.6 metres per second at Mach 1.095.

| Sea-level Mach | $P_s$ |
|---|---|
| 0.3 | 17,468 ft/min |
| 0.6 | 35,803 ft/min |
| 0.9 | 47,035 ft/min |
| 1.095 | 49,332 ft/min |
| 1.2 | 48,585 ft/min |

**The claim exceeds the computed ceiling by 21.6 percent.** For claimed climb rate $\dot h_{\mathrm{claim}}$
and the largest $P_s$ in the scan,

$$ \frac{\dot h_{\mathrm{claim}}}{P_{s,\max}} - 1 = \frac{60{,}000}{49{,}332} - 1 = 0.216 $$

**The maximum lies between the round Mach numbers, so it has to be found by a fine scan.** A coarse grid
that stops at Mach 1.2 takes the peak as 48,585 feet per minute and overstates the shortfall,

$$ \frac{60{,}000}{48{,}585} - 1 = 0.235 $$

or 23.5 percent. The fine scan puts the maximum at Mach 1.095.

**Two explanations fit and the article cannot choose between them.** The figure may be a zoom rather than a
steady climb, in which case it is a transient trade of speed for height and is not a rate of climb in the
sense the ceiling applies to. Quoted climb figures for fighters of this era are often exactly that.
Alternatively the thrust or weight assumptions here are conservative.
**What can be said is that the figure is not supported by the aircraft's own published thrust and weight under a steady interpretation**,
and that this is the only headline claim in the brochure of which that is true.

### The Fuel Claim, Which Cannot Be Checked Here

The record states a 46 percent increase in internal fuel from a 30-inch stretch. The weight breakdown gives
the Lancer's clean disposable load as the difference between its normal loaded and empty weights.

$$ W_{\mathrm{fuel,\ clean}} = W_{\mathrm{loaded}} - W_{\mathrm{empty}} = 24{,}385 - 17{,}885 = 6{,}500\ \mathrm{lb} $$

**Testing the 46 percent against that figure needs the F-104G's internal fuel capacity, and none of the
sources cited here states it.** The claim is therefore left as the manufacturer's, neither confirmed nor
contradicted. The difference above is also an upper bound on the clean fuel load rather than the fuel load
itself, because a normal loaded weight ordinarily includes the pilot, ammunition and oil as well as fuel.

### The Takeoff Claim, Which Is Conservative

The ground roll is not taken from a rule of thumb. The acceleration is integrated from rest to lift-off
against thrust, drag, and the rolling friction on whatever weight the wing is not yet carrying, following
the method in [Raymer][book_raymer].

Takeoff and landing ground-run prediction is a small and practical literature, and the period work is where
the friction coefficients and the lift-off margins used here come from.

- [Linnell 1963][research_linnell_1963]
- [Krenkel and Salzman 1968][research_krenkel_salzman_1968]
- [Muehter 1974][research_muehter_1974]
- [Smith et al 1979][research_smith_yamakawa_1979]
- [Hawks 1982][research_hawks_1982]

$$ s = \int_0^{V_{\mathrm{LOF}}} \frac{V\,dV}{a(V)}, \qquad a(V) = \frac{T - D - \mu\left(W - L\right)}{W/g} $$

$$ V_{\mathrm{LOF}} = 1.1\,V_{\mathrm{stall}} $$

| $C_{L_{\max}}$ at takeoff | $V_{\mathrm{LOF}}$ | Computed roll | Claim |
|---|---|---|---|
| 1.0 | 170.4 kt | 1,296 ft | 1,450 ft |
| 1.2 | 155.6 kt | 1,078 ft | 1,450 ft |
| 1.4 | 144.1 kt | 922 ft | 1,450 ft |

**The claim is longer than the computation at every assumption**, which is the direction that does not
oversell. The integration takes full afterburner and charges nothing for installation losses, so it is
optimistic by construction, and the gap between the two is the room that optimism occupies.

### The Radius Claim, Which Survives

The [Breguet range equation][ref_breguet] carries no gravitational constant when the specific fuel
consumption is quoted per hour, because such a figure is already a weight of fuel per unit thrust per unit
time.

$$ R = \frac{V}{c_t}\,\frac{L}{D}\,\ln\frac{W_0}{W_1} $$

The Breguet relation and the mission bookkeeping around it are as given in [Raymer][book_raymer] and
[Nicolai][book_nicolai]. The end weight is the start weight less the usable fraction of the fuel, and the
ratio is what the logarithm acts on. The start weight is the maximum takeoff weight, and the fuel is what
that weight leaves after the empty weight and the 4,000 pound bombload the radius is quoted with
\[[Lockheed CL-1200 Lancer][ref_cl1200]\].

$$ W_{\mathrm{fuel}} = W_0 - W_{\mathrm{empty}} - W_{\mathrm{stores}} = 35{,}000 - 17{,}885 - 4{,}000 = 13{,}115\ \mathrm{lb} $$

$$ W_1 = W_0 - f\,W_{\mathrm{fuel}} = 35{,}000 - 0.85 \times 13{,}115 = 23{,}852\ \mathrm{lb} $$

$$ \frac{W_0}{W_1} = \frac{35{,}000}{23{,}852} = 1.4674 $$

The mission factor is then a defined ratio rather than a rule of thumb, and quoting it is what keeps a
Breguet integral from being mistaken for a mission.

$$ k_m = \frac{R_{\mathrm{combat}}}{R_{\mathrm{still\,air}}} = \frac{367}{1{,}914} = 0.192 $$

| $L/D$ | $c_t$ | Still-air range | The 367 nmi claim as a fraction |
|---|---|---|---|
| 6.0 | 0.85 /h | 1,436 nmi | 0.256 |
| 7.0 | 0.85 /h | 1,675 nmi | 0.219 |
| 8.0 | 0.85 /h | 1,914 nmi | 0.192 |
| 9.0 | 0.85 /h | 2,154 nmi | 0.170 |

**A combat radius is not half a range.** It pays for climb, descent, a combat allowance at maximum power,
reserves, and an outbound leg flown with stores hung on it. The ratio runs about 0.15 to 0.25 in practice.
**The claim lands inside that band for a lift-to-drag ratio of 7 or more and just above it at 6, and is
therefore credible**, though with less room than a lighter empty weight would give.

**This is a negative result for the suspicion that the radius claim is inflated, and it is reported as such.**

## What the Data Changed

**Nothing, because there was no data.**

That sentence is the finding rather than an admission. Every other article in this series can point to a
measurement that entered the literature.
**This one cannot, and the reason is worth stating. The programme was cancelled at precisely the point where it would have begun producing evidence.**

What the *programme* changed is a different question and the answer is small but not zero.

- **It did not influence the F-15.** No evidence connects the Lancer to any F-15 design decision.
- **It did not influence the Lightweight Fighter programme technically**, though it demonstrates that
  the argument for funding lightweight-fighter prototypes was in the air before that programme existed.
- **It produced no literature.** This is the second consecutive article in the series to report that,
  and the third in which the subject generated no development literature because nothing was developed.

The programme's context is the literature on procurement, competitive prototyping, export fighters and
acquisition policy, gathered in the cluster on defence acquisition, prototyping and the arms trade below, and
the lightweight fighter programme's own record is in the cluster on the F-104, the J79 and later named
fighters. They include these.

- [Beesly 1966][research_beesly_1966]
- [Dietz and Bailey 1973][research_dietz_bailey_1973]
- [Boger et al 1989][research_boger_greer_1989]
- [Piccirillo and Aronstein 1997][research_piccirillo_aronstein_1997]
- [Coble et al 2014][research_coble_royster_2014]

## A Designation Without an Aircraft

The X-27 is the third consecutive designation in this series that did not go to a research aeroplane, and
the pattern is now firm enough to be worth naming.

- **X-25**, a commercially available autogyro bought to investigate a rescue concept.
- **X-26**, a commercially available sailplane bought twice, for training and for quiet observation.
- **X-27**, a manufacturer's private-venture export fighter that was never built.

**The first two were aircraft that existed and were bought for properties they already had. The third did not exist at all.**
What the three have in common is that the X-designation was doing something other than marking a research
aeroplane built to answer a research question.

**In the X-27's case the designation was doing procurement work.** An X-designation carried the implication
of federal interest, and federal interest was what the Lancer needed and never obtained.
**The designation was issued and the money was not**, which makes the X-27 an unusually clean example of the
designation and the programme coming apart.

**This article does not claim the designation system was abused.** The number was allocated for a proposed
research aircraft with a stated research purpose, which is what the system is for.
**The observation is narrower. By 1971 an X-designation could be allocated to an aeroplane whose primary purpose was commercial, and the allocation could precede any commitment to build it.**
That is a fact about what the system had come to permit, and it belongs with the evidence the closing
article of this series assembles.

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Supersonic inlets, shock systems and pressure recovery | 515 |
| Inlet distortion and inlet-engine compatibility | 260 |
| Drag polars, wave drag and supersonic aerodynamics | 195 |
| Compressor stall, surge and casing treatment | 192 |
| Wings, aspect ratio and vortex flows | 166 |
| Turbofans, turbojets and installed thrust | 146 |
| Air combat, agility and aircraft performance | 114 |
| Aerodynamic heating, recovery temperature and thermal protection | 109 |
| Aluminium alloys and their strength when hot | 92 |
| Titanium, other alloys and composites at elevated temperature | 84 |
| Conceptual design, optimisation and the derivative aircraft | 81 |
| Stability, control and flying qualities | 68 |
| The F-104, the J79 and later named fighters | 59 |
| Fighter aircraft design, requirements and history | 43 |
| Defence acquisition, prototyping and the arms trade | 41 |
| Thermal stress, thermal buckling and thermoelasticity | 35 |
| Boundary-layer control, high lift and short take-off | 28 |
| Other aeronautical literature | 1 |
| **Total** | **2,229** |

The bodies of work above are the ones the argument sits inside.
**This section surveys what has happened since**, on the standing expectation that an article of this kind
should double as a review of the current literature. The reading is not neutral. Each body of work is placed
by what it says about the X-27's binding question.

**The short version is that every one of the X-27's technical problems is still an active subject, and the one that has moved least is the one that would have killed it.**

### Supersonic inlets are still hard, and are now computed rather than integrated

The Taylor-Maccoll integration above is what the era had. Contemporary inlet design is a
computational-fluid-dynamics and optimisation problem, and the subjects that dominate it are shock-wave and
boundary-layer interaction, starting and unstart, variable geometry, and the design of inward-turning and
waverider-derived compression surfaces.

**What has not changed is the total-pressure budget.** The shock losses computed above are exact inviscid
gas dynamics and no amount of computation makes them smaller.
**The modern literature buys back losses at the margins, in bleed management and in diffuser design, and confirms the size of the central problem rather than dissolving it.**

This literature is gathered in the cluster on supersonic inlets, shock systems and pressure recovery below,
and its work on bleed, buzz, unstart, diffusers and inward-turning inlets includes these.

- [Adams et al 1984][research_adamsjcjr_martindalewr_1984]
- [Soltani et al 2015][research_soltani_younsi_2015]
- [Otto et al 2015][research_otto_trefny_2015]
- [Zhang et al 2020][research_zhang_yuan_2020]
- [Reza Maadi and Sepahi-Younsi 2022][research_rezamaadi_sepahiyounsi_2022]
- [Kumar 2022][research_kumar_2022]

### Distortion is better understood and no less dangerous

The X-27's exposure was a distortion-sensitive fan behind a marginal inlet.
**That combination is now a named design discipline with its own descriptors and standards**, and the
surrounding work covers distortion descriptors, fan stability under circumferential and radial defects, and
the closely related problem of boundary-layer-ingesting propulsion, which deliberately accepts distortion in
exchange for propulsive efficiency.

**The comparison is instructive.** A modern boundary-layer-ingesting fan accepts distortion the TF30 could
not survive, and it does so because the fan is designed for it from the outset.
**The X-27 proposed the opposite, an engine designed for clean flow placed behind an inlet asked to work beyond its ancestry.**

That discipline is gathered in the cluster on inlet distortion and inlet-engine compatibility below, and its
standards, its distortion generators, the TF30's measured response and the boundary-layer-ingesting fan
include these.

- [Gas Turbine Engine Inlet Flow Distortion Guidelines][research_gas_turbine]
- [Guidelines for Characterization of Gas Turbine Engine...][research_guidelines_for]
- [Debogdan et al 1975][research_debogdance_dicusjh_1975]
- [Hall et al 2017][research_hall_greitzer_2017]
- [Guimarães et al 2018][research_guimaraes_lowe_2018]
- [Provenza et al 2018][research_provenza_duffy_2018]

### Compressor stall is a control problem now

Stall and surge were phenomena to be avoided by margin in 1971.
**They are now phenomena to be detected and actively suppressed**, with stall-precursor detection, casing
treatment, and active control all mature subjects.

**Had the X-27 flown, this is the technology that would have rescued it, and it did not exist.**

These subjects are gathered in the cluster on compressor stall, surge and casing treatment below, which
includes the following on active control, casing treatment and the detection of stall inception.

- [Boussios et al 1992][research_boussios_epstein_1992]
- [VanSchalkwyk et al 2001][research_vanschalkwykchristian_brightmichellem_2001]
- [Uddin and Gravdahl 2016][research_uddin_gravdahl_2016]
- [Dong et al 2018][research_dong_sun_2018]
- [Zhang et al 2021][research_zhang_du_2021]
- [Quan et al 2024][research_quan_sun_2024]

### Hot structures moved to materials the X-27 did not have

The aluminium limit computed above is a property of the alloy.
**The contemporary answer is not a better aluminium but a different material**, and the literature covers
titanium alloys, thermal barrier coatings, metallic thermal protection and elevated-temperature creep in
aerospace alloys.

That literature is gathered in the clusters on titanium, other alloys and composites at elevated temperature
and on aerodynamic heating, recovery temperature and thermal protection below, and it includes these.

- [Gupta and Ramkumar 2015][research_gupta_ramkumar_2015]
- [Ochonogor et al 2017][research_ochonogor_akinlabi_2017]
- [Afanas'ev et al 2019][research_afanasev_nikitin_2019]
- [Malvi and Roy 2021][research_malvi_roy_2021]
- [Tao et al 2024][research_tao_wang_2024]
- [Bhandari et al 2025][research_bhandari_gaur_2025]

### Conceptual design became a numerical discipline

The sizing exercise above is a 1970s method executed by hand.
**Contemporary conceptual design is multidisciplinary optimisation**, and the part of it most relevant here
is the literature on *derivative* design, meaning how much of an existing aircraft can be kept when the
requirement changes.

**The Lancer is a derivative-design problem and the modern literature has a name for its failure mode.**
Reusing a fuselage, an aerofoil and a systems architecture constrains the solution far more than the
retained parts are worth, and quantifying that trade is now a research subject in its own right.

This literature is gathered in the cluster on conceptual design, optimisation and the derivative aircraft
below, and its multidisciplinary and derivative-design work includes these.

- [Allison et al 2015][research_allison_morris_2015]
- [Park et al 2016][research_park_chung_2016]
- [Park et al 2016][research_park_chung_2016_b]
- [Park et al 2018][research_park_chung_2018]
- [Li and Geiselhart 2020][research_wuli_karlgeiselhart_2020]

### Agility metrics settled the argument the competition was having

Energy manoeuvrability was contested in 1970 and is standard now.
**The contemporary literature on agility metrics, specific excess power and trajectory optimisation is the direct descendant of the diagrams Boyd was drawing**,
and it still states aircraft performance in the framework on which the Lancer performs well.

**Which sharpens the historical point.** On the metric that won the argument, the Lancer was a good
aeroplane. It lost anyway, and it lost on cost, logistics and timing rather than on performance.

That literature is gathered in the cluster on air combat, agility and aircraft performance below, and its
agility metrics, specific excess power models and agility requirements include these.

- [Ali et al 2017][research_ali_asghar_2017]
- [Wang et al 2017][research_wang_guo_2017]
- [Wang et al 2020][research_wang_wang_2020]
- [Oruc and Baklacioglu 2022][research_oruc_baklacioglu_2022]
- [Kigotho et al 2022][research_kigotho_bodylski_2022]
- [Paranjape and Ananthkrishnan 2023][research_paranjape_ananthkrishnan_2023]
- [Oruc and Baklacioglu 2023][research_oruc_baklacioglu_2023]
- [Reinbold et al 2026][research_reinbold_breitsamter_2026]

### Acquisition scholarship has a category for what happened

The Lancer's fate is a case in a well-developed literature on competitive prototyping, defence acquisition
and arms transfer.
**A private venture seeking government funds to build a demonstrator for an export market it had already lost is a recognisable pattern**,
and the modern work on prototype policy and on foreign military sales is where a reader should go for the
general case.

That work is gathered in the cluster on defence acquisition, prototyping and the arms trade below, and on
prototype policy, military assistance and foreign military sales it includes these.

- [Kaplan 1980][research_kaplan_1980]
- [Carey 1982][research_carey_1982]
- [Dietz and Bailey 1973][research_dietz_bailey_1973]
- [Department Of Defense Washington Dc 1997][research_departmentofdefensewashingtondc_1997]
- [Coble et al 2014][research_coble_royster_2014]

### Ram drag never left the literature, and supersonic cruise has reframed it

**The keystone's other half is the one the subsections above do not reach.** The engine section computed that 45
percent of gross thrust at Mach 2.6 is spent on the momentum of the air the engine swallowed, and that the
exhaust velocity the rating implies needs total pressure the inlet was struggling to deliver.
**That is a propulsion-integration problem, and its literature never went quiet.** Of the 30 titles in
the survey that name spillage, additive drag or forces, ram drag, inlet drag, installed thrust or performance,
installation effects or losses, or thrust and drag bookkeeping, every decade from the 1960s to the 2020s holds
between 2 and 7.

**It is live again in new terms.** Supersonic civil transport, variable-cycle engines and boundary-layer-ingesting
propulsion have all put thrust-and-drag bookkeeping back at the centre of the design problem, and the
question of where the airframe ends and the engine begins is being argued in the same terms the X-27 would
have had to settle.

This literature is gathered in the clusters on turbofans, turbojets and installed thrust and on drag polars,
wave drag and supersonic aerodynamics below, and the thrust and drag bookkeeping, the supersonic transport and
variable-cycle work and the boundary-layer-ingesting case include these.

- [Cassetti 1978][research_cassetti_1978]
- [Zhang et al 2015][research_zhang_chen_2015]
- [Takahashi 2017][research_takahashi_2017]
- [Gray et al 2017][research_grayjustins_madercharlesa_2017]
- [Goulos et al 2021][research_goulos_otter_2021]
- [Yao et al 2022][research_yao_zhang_2022]

### Thermal stress is now a coupled problem rather than a hand calculation

**The article computes a thermal stress with a modulus, an expansion coefficient and a temperature difference, and gets a number comparable to the mechanical allowable.**
That calculation is a century old and it is the right first move.
**What has changed is that the coupling is no longer neglected.**

Contemporary work treats the aerodynamic heating, the temperature field, the resulting stress and the change
in stiffness as one problem rather than four, under the name aerothermoelasticity, and the reason is that at
high Mach the structure's deformation changes the flow that is heating it.
**For the X-27 this would have mattered less than for a hypersonic vehicle, but the eighty-two kelvin figure computed above is exactly the kind of number that a coupled analysis exists to refine.**

This literature is gathered in the cluster on thermal stress, thermal buckling and thermoelasticity below,
and its coupled and aerothermoelastic work includes these.

- [Li et al 2015][research_li_pan_2015]
- [Chai et al 2017][research_chai_song_2017]
- [Ganilova et al 2022][research_ganilova_cartmell_2022]
- [Kang et al 2024][research_kang_liang_2024]
- [Xie et al 2025][research_xie_ye_2025]

### The Lancer is now a recognised design problem with a literature of its own

**A derivative aircraft is not a cheap aircraft, and the modern literature says so with numbers.** Reusing a
fuselage cross-section, an aerofoil and a systems architecture buys development cost and schedule at the
price of a constrained design space, and the size of that price is now a research subject.

**This is the one contemporary thread that takes the article's own subject as its object of study.** The
Lancer retained the F-104's aerofoil section and its 3.36 percent thickness ratio, which is why its aspect
ratio could only reach 2.836 and why its drag-due-to-lift stayed above the F-5E's at every assumption
tested.
**The modern framing would call that inherited constraint the dominant term in the trade, and would try to price it before committing rather than after losing a competition.**

The derivative-design work is gathered in the cluster on conceptual design, optimisation and the derivative
aircraft below, and it includes these.

- [Park et al 2016][research_park_chung_2016]
- [Park et al 2016][research_park_chung_2016_b]
- [Park et al 2018][research_park_chung_2018]

### The X-27's real problem has a modern answer, and it is the one thing that would have helped

**Nobody could tell whether the Lancer would work without building it.** That is the whole of the
programme's difficulty. The mock-up settled nothing, the brochure figures were the manufacturer's own, and
the competition was decided on cost and logistics rather than on any measurement of the aeroplane.

**Evaluating an aircraft that does not exist is now a research programme.** Surrogate modelling, uncertainty
quantification in conceptual design and model-based systems engineering all exist to
answer, before metal is cut, the question the X-27 could only have answered by flying.

**This is the closest thing to a resolution the article's central difficulty has, and it arrived fifty years late.**
It is also the reason this article could be written at all. The analysis above is a primitive version of the
same idea, taking published geometry and published ratings and asking what they imply, and its one genuine
success, the reconciliation of the spike travel with the engine's airflow, is exactly the kind of
consistency check a modern framework automates.

This literature is gathered in the cluster on conceptual design, optimisation and the derivative aircraft
below, and its surrogate, uncertainty and systems-engineering work includes these.

- [Li et al 2019][research_li_soskin_2019]
- [Krupa 2019][research_krupa_2019]
- [Bianchi et al 2020][research_bianchi_secco_2020]
- [Leng et al 2024][research_leng_feng_2024]

### Supersonic inlets, shock systems and pressure recovery

**The keystone's first half.** Spike, cone, ramp and mixed-compression inlets, the shock systems that compress the flow, bleed, buzz, starting and unstart, diffusers and the total-pressure recovery the inlet sections above compute.

**54 of these titles name a spike, a centerbody, a cone or a ramp, and 10 of those date from before 1960**, so the two inlet geometries the article compares have a literature running from the period that designed them to the present. The optimum shock system the inlet sections compute is set out in [Oswatitsch 1947][research_oswatitsch_1947].

**515 records.** \[[A Study on Subcritical 2004][research_a_study_2004]\] \[[Abate et al 2023][research_abate_vasista_2023]\] \[[Abdel-Fattah 1996][research_abdelfattah_1996]\] \[[Abdelghany 2025][research_abdelghany_2025]\] \[[Abdelwahab 1977][research_abdelwahabm_1977]\] \[[Abdelwahab 1981][research_abdelwahabm_1981]\] \[[Abedi et al 2020][research_abedi_askari_2020]\] \[[Abedi et al 2020][research_abedi_askari_2020_b]\] \[[Abrahamson 1988][research_abrahamson_1988]\] \[[Adamczyk et al 2024][research_adamczyk_kozakiewicz_2024]\] \[[Adams et al 1984][research_adamsjcjr_martindalewr_1984]\] \[[Agung Saputra et al 2026][research_agungsaputra_bhimashaktiarafat_2026]\] \[[Ajay and Kundu 2025][research_ajay_kundu_2025]\] \[[Ali et al 2025][research_ali_khan_2025]\] \[[Allen and Beke 1953][research_allen_beke_1953]\] \[[Allen et al 1960][research_allen_davis_1960]\] \[[Amatucci et al 1982][research_amatucci_addy_1982]\] \[[Ananthapadmanaban and Murganandam 2016][research_ananthapadmanaban_murganandam_2016]\] \[[Anderson 1984][research_anderson_1984]\] \[[Anderson and Wong 1969][research_anderson_wong_1969]\] \[[Anderson et al 1957][research_anderson_dryer_1957]\] \[[Anderson et al 1966][research_anderson_petersen_1966]\] \[[Anderson and Bowditch 1958][research_andersonbh_bowditchdn_1958]\] \[[Anderson et al 1960][research_andersonbh_bowditchdn_1960]\] \[[Anderson and Weir 2014][research_andersonbernhardh_weirlois_2014]\] \[[Araújo et al 2021][research_araujo_pereira_2021]\] \[[Arif et al 2021][research_arif_iftikhar_2021]\] \[[Arlinger 1976][research_arlinger_1976]\] \[[Askari and Abedi 2026][research_askari_abedi_2026]\] \[[Askari and Soltani 2017][research_askari_soltani_2017]\] \[[Askari and Soltani 2019][research_askari_soltani_2019]\] \[[Askari and Soltani 2020][research_askari_soltani_2020]\] \[[Askari and Soltani 2022][research_askari_soltani_2022]\] \[[Askari and Soltani 2023][research_askari_soltani_2023]\] \[[Askari et al 2019][research_askari_soltani_2019_b]\] \[[Azevedo et al 1990][research_azevedo_liu_1990]\] \[[Saheby et al 2019][research_bsaheby_shen_2019]\] \[[Babinsky 2014][research_babinsky_2014]\] \[[Bai et al 2026][research_bai_deng_2026]\] \[[Ball and Ross 1972][research_ball_ross_1972]\] \[[Bangert et al 1980][research_bangert_santman_1980]\] \[[Bangert et al 1982][research_bangert_santman_1982]\] \[[Barnhart 1988][research_barnhart_1988]\] \[[Barr et al 2018][research_barr_ogara_2018]\] \[[Barr et al 2020][research_barr_muralidharan_2020]\] \[[Barry 1966][research_barry_1966]\] \[[Barry 1971][research_barry_1971]\] \[[Barry 1968][research_barryfw_1968]\] \[[Batterton et al 1974][research_battertonpg_arpasidj_1974]\] \[[Baydar et al 2018][research_baydar_lu_2018]\] \[[Baydar et al 2016][research_baydarezgihan_lufrankk_2016]\] \[[Baydar et al 2017][research_baydarezgihan_lufrankk_2017]\] \[[Beheim and Gertsma 1956][research_beheimma_gertsmalw_1956]\] \[[Beke and Allen 1953][research_beke_allen_1953]\] \[[Benson 1994][research_benson_1994]\] \[[Benson and Anderson 1983][research_benson_anderson_1983]\] \[[Benton et al 2021][research_benton_humphrey_2021]\] \[[Berto et al 2020][research_berto_benini_2020]\] \[[Biesiadny and Wendt 2004][research_biesiadnythomasj_wendtbrucej_2004]\] \[[Bisek 2014][research_bisek_2014]\] \[[Bisek 2015][research_bisek_2015]\] \[[Bisek et al 2012][research_bisek_rizzetta_2012]\] \[[Bogar et al 1983][research_bogar_sajben_1983]\] \[[Bowditch 1973][research_bowditch_1973]\] \[[Bowditch and Musial 1957][research_bowditch_musial_1957]\] \[[Braun and Podleski 2019][research_braun_podleski_2019]\] \[[Bravo-Mosquera et al 2019][research_bravomosquera_abdalla_2019]\] \[[Broadley et al 2023][research_broadley_hewitt_2023]\] \[[Brophy and Hawk 1990][research_brophy_hawk_1990]\] \[[Burns et al 2015][research_burns_koo_2015]\] \[[Burris 1966][research_burris_1966]\] \[[Burrows et al 2025][research_burrows_vukasinovic_2025]\] \[[Bush 1985][research_bush_1985]\] \[[Cai and Huang 2022][research_cai_huang_2022_c]\] \[[Cai et al 2022][research_cai_huang_2022]\] \[[Cai et al 2022][research_cai_huang_2022_b]\] \[[Campbell and Syberg 1984][research_campbell_syberg_1984]\] \[[Campbell et al 1985][research_campbell_syberg_1985]\] \[[Carlin et al 2003][research_carlincm_frischi_2003]\] \[[Carrier et al 2001][research_carrier_knight_2001]\] \[[Castner et al 2018][research_castner_simerly_2018]\] \[[Chang and Hsu 1960][research_chang_hsu_1960]\] \[[Chapman et al 2005][research_chapmandave_smithcf_2005]\] \[[Che Idris et al 2020][research_cheidris_saad_2020]\] \[[Cheikh and Chen 2017][research_cheikh_chen_2017]\] \[[Chen and Tan 2019][research_chen_tan_2019]\] \[[Chen et al 2017][research_chen_tan_2017]\] \[[Chen et al 2018][research_chen_tan_2018]\] \[[Chen et al 2019][research_chen_tan_2019_b]\] \[[Chen et al 2020][research_chen_zhang_2020]\] \[[Chen et al 2021][research_chen_yue_2021]\] \[[Chen et al 2023][research_chen_chen_2023]\] \[[Chen et al 2025][research_chen_martinez_2025]\] \[[Chen et al 2025][research_chen_sethuraman_2025]\] \[[Chen et al 2026][research_chen_wu_2026]\] \[[Cheng et al 2024][research_cheng_huang_2024]\] \[[Chima 2011][research_chima_2011]\] \[[Chima 2011][research_chima_2011_b]\] \[[Chima et al 2009][research_chima_conners_2009]\] \[[Chima et al 2010][research_chima_conners_2010]\] \[[Chima 2011][research_chimarodrickv_2011]\] \[[Chima 2012][research_chimarodrickv_2012]\] \[[Chima et al 2011][research_chimarodrickv_hirtstefaniem_2011]\] \[[Choe and Kim 2016][research_choe_kim_2016]\] \[[Choe et al 2020][research_choe_kim_2020]\] \[[Choi 2024][research_choi_2024]\] \[[Choi et al 2026][research_choi_choi_2026]\] \[[Chun and Burr 1969][research_chun_burr_1969]\] \[[Chun and Swanson 1964][research_chun_swanson_1964]\] \[[Chung 1994][research_chung_1994]\] \[[Clark 1995][research_clark_1995]\] \[[Colbourne 1980][research_colbourne_1980]\] \[[Coltrin 1987][research_coltrin_1987]\] \[[Conners and Howe 2006][research_conners_howe_2006]\] \[[Connors et al 1957][research_connors_lovell_1957]\] \[[Connors and Wise 1957][research_connorsjamesf_wisegeorgea_1957]\] \[[Control system design using frequency domain models and parameter optimization with application to supersonic inlet controls 1976][research_control_system_1976]\] \[[Conway et al 2010][research_conway_lavely_2010]\] \[[Conway et al 2011][research_conway_lavely_2011]\] \[[Cortright 1951][research_cortrightedgarmjr_1951]\] \[[Crosthwait 1970][research_crosthwait_1970]\] \[[Cubbison 1977][research_cubbison_1977]\] \[[Daliri et al 2018][research_daliri_farahani_2018]\] \[[Das and Prasad 2023][research_das_prasad_2023]\] \[[Dashora and Sasidharan 2024][research_dashora_sasidharan_2024]\] \[[Davis et al 2012][research_davisdavido_vyasmanana_2012]\] \[[Deese and Agarwal 1983][research_deese_agarwal_1983]\] \[[Denner et al 1998][research_denner_mccallum_1998]\] \[[Dickman and Takahashi 2016][research_dickman_takahashi_2016]\] \[[Diggins 1951][research_diggins_1951]\] \[[Ding et al 2015][research_ding_shen_2015]\] \[[Dolling 1982][research_dolling_1982]\] \[[Dryer and Beke 1952][research_dryer_beke_1952]\] \[[Effect of inlet Mach number on performance and flow structure of an axial supersonic through-flow fan cascade 2023][research_effect_of_2023]\] \[[Egorov et al 2011][research_egorov_neiland_2011]\] \[[Englert and Obery 1952][research_englertgeraldw_oberyleonardj_1952]\] \[[Esenwein and Schueller 1952][research_esenweinfredt_schuellercarlf_1952]\] \[[Experimental Study of the Unstart/Restart Process of a Two-Dimensional Supersonic Inlet Induced by Backpressure 2022][research_experimental_study_2022]\] \[[Falk et al 1998][research_falk_jumper_1998]\] \[[Falk et al 2001][research_falk_jumper_2001]\] \[[Farahani and Mahdavi 2019][research_farahani_mahdavi_2019]\] \[[Farahani et al 2019][research_farahani_daliri_2019]\] \[[Ferrero 2020][research_ferrero_2020]\] \[[Ferri and Nucci 1946][research_ferriantonio_nuccilouism_1946]\] \[[Ferri and Nucci 1951][research_ferriantonio_nuccilouism_1951]\] \[[Fink and Anderson 1983][research_fink_anderson_1983]\] \[[Fleeter et al 1974][research_fleeter_mcclure_1974]\] \[[Flow Field Study of Mixed Compression Supersonic Air Intake with Cowl Ventilation 2020][research_flow_field_2020]\] \[[Forsythe et al 1998][research_forsythe_hoffmann_1998]\] \[[Fradenburgh and Wyatt 1953][research_fradenburgh_wyatt_1953]\] \[[Fraiser 1960][research_fraiser_1960]\] \[[Frey 2014][research_frey_2014]\] \[[Frohnapfel et al 2018][research_frohnapfel_mack_2018]\] \[[Fujii et al 2021][research_fujii_fujimori_2021]\] \[[Fujimoto and Niwa 1993][research_fujimoto_niwa_1993]\] \[[Gaglio et al 2023][research_gaglio_visone_2023]\] \[[Gahlot and Singh 2019][research_gahlot_singh_2019]\] \[[Gartling 1970][research_gartling_1970]\] \[[Ge et al 2021][research_ge_shang_2021]\] \[[Gilinsky et al 2000][research_gilinskymikhail_morganmorrish_2000]\] \[[Gillen and Loth 2011][research_gillen_loth_2011]\] \[[Gillen and Loth 2015][research_gillen_loth_2015]\] \[[Goonko and Mazhul 2011][research_goonko_mazhul_2011]\] \[[Gorton 1953][research_gortongeraldc_1953]\] \[[Gorton 1954][research_gortongeraldc_1954]\] \[[Gounko and Mazhul 2012][research_gounko_mazhul_2012]\] \[[Grenson and Beneddine 2018][research_grenson_beneddine_2018]\] \[[Guan and Yarng 1984][research_guan_yarng_1984]\] \[[Guan and Yarng 1987][research_guan_yarng_1987]\] \[[Guimarães et al 2018][research_guimaraes_toddlowe_2018]\] \[[Haas and Karanian 1981][research_haas_karanian_1981]\] \[[Halwas and Aggarwal 2019][research_halwas_aggarwal_2019]\] \[[Halwas and Aggarwal 2019][research_halwas_aggarwal_2019_b]\] \[[Hamed 1995][research_hamed_1995]\] \[[Hancock 1985][research_hancockjp_1985]\] \[[Harloff and Smith 1995][research_harloff_smith_1995]\] \[[Hartsell 1960][research_hartsell_1960]\] \[[Hasel et al 1953][research_hasellowelle_lankfordjohnl_1953]\] \[[Hawkins et al 1976][research_hawkinsje_kirklandfp_1976]\] \[[He et al 2026][research_he_xie_2026]\] \[[Heath et al 2016][research_heath_slater_2016]\] \[[Henderson 1965][research_henderson_1965]\] \[[Hodder 1981][research_hodderbk_1981]\] \[[Hodder et al 1981][research_hodderbk_farquharbw_1981]\] \[[Hoffman 2000][research_hoffmantr_2000]\] \[[Howard et al 1951][research_howard_luidens_1951]\] \[[Howerton and Slater][research_howerton_slater]\] \[[Howlett and Hunter 1986][research_howlett_hunter_1986]\] \[[Hu 2024][research_hu_2024]\] \[[Hu et al 2024][research_hu_li_2024]\] \[[Huang et al 2016][research_huang_tan_2016]\] \[[Huang et al 2026][research_huang_wang_2026]\] \[[Hube 1968][research_hube_1968]\] \[[Hunt and Hunt 2021][research_hunt_hunt_2021]\] \[[Iek et al 1993][research_iekchanthy_burleyrichardr_1993]\] \[[INFLUENCE OF BACK PRESSURE ON THE FLOW IN THE DIFFUSER OF A SUPERSONIC AIR INLET 2017][research_influence_of_2017]\] \[[Inger 1986][research_inger_1986]\] \[[Connors et al 1957][research_jamesfconnors_georgeawise_1957]\] \[[Jiao et al 2017][research_jiao_chang_2017]\] \[[Jin et al 2022][research_jin_sun_2022]\] \[[Jin et al 2023][research_jin_tan_2023]\] \[[Jin et al 2023][research_jin_zhang_2023]\] \[[Johnson and Lawing 1977][research_johnson_lawing_1977]\] \[[Johnson and Wu 1975][research_johnson_wu_1975]\] \[[Johnson III and Wu 1974][research_johnsoniii_wu_1974]\] \[[Johnson and Montoya 1973][research_johnsonhj_montoyaej_1973]\] \[[Jules and Barnhart 1998][research_jules_barnhart_1998]\] \[[Jung et al 2015][research_jung_lee_2015]\] \[[James et al 2021][research_kjames_suryan_2021]\] \[[James and Kim 2022][research_kjames_kim_2022]\] \[[Kamman and Hall 1975][research_kamman_hall_1975]\] \[[Kang et al 2024][research_kang_kang_2024]\] \[[Kang et al 2024][research_kang_li_2024]\] \[[Kapoor et al 1992][research_kapoor_pai_1992]\] \[[Kapoor et al 1994][research_kapoorkamlesh_andersonbernhardh_1994]\] \[[Kawamura et al 1987][research_kawamurat_chyuwj_1987]\] \[[Kazula and Höschler 2020][research_kazula_hoschler_2020]\] \[[Kazula and Höschler 2021][research_kazula_hoschler_2021]\] \[[Kazula et al 2019][research_kazula_mischke_2019]\] \[[Kennon 1989][research_kennon_1989]\] \[[Keppler 1966][research_keppler_1966]\] \[[Khan and Hasan 2021][research_khan_hasan_2021]\] \[[Khobragade and Kumar 2022][research_khobragade_kumar_2022]\] \[[Khobragade et al 2021][research_khobragade_unnikrishnan_2021]\] \[[Khobragade et al 2024][research_khobragade_gustavsson_2024]\] \[[Kim and Kwon 2015][research_kim_kwon_2015]\] \[[Kim and Lee 2022][research_kim_lee_2022]\] \[[Kim and Park 2026][research_kim_park_2026]\] \[[Kim et al 2011][research_kimhyoungjin_kumanotakayasu_2011]\] \[[Kong and Park 2018][research_kong_park_2018]\] \[[Kong et al 2022][research_kong_li_2022]\] \[[Kong et al 2026][research_kong_su_2026]\] \[[Kopasakis et al 2012][research_kopasakisgeorge_connollyjosephw_2012]\] \[[Kopasakis et al 2012][research_kopasakisgeorge_connollyjosephw_2012_b]\] \[[Kotov et al 2018][research_kotov_ruleva_2018]\] \[[Kozakiewicz et al 2025][research_kozakiewicz_adamczyk_2025]\] \[[Krause 1981][research_krause_1981]\] \[[Krivec et al 1984][research_krivec_ling_1984]\] \[[Krushnarao Kotteda and Mittal 2016][research_krushnaraokotteda_mittal_2016]\] \[[Kumar 2022][research_kumar_2022]\] \[[Kumazaki and Shimamura 2026][research_kumazaki_shimamura_2026]\] \[[Kurkov et al 1975][research_kurkov_soeder_1975]\] \[[Kursakov et al 2016][research_kursakov_kazhan_2016]\] \[[Kuzmin 2024][research_kuzmin_2024]\] \[[Kwak et al 2013][research_kwak_lee_2013]\] \[[Küçük and Tuncer 2024][research_kucuk_tuncer_2024]\] \[[Langener et al 2009][research_langener_myrabo_2009]\] \[[Latham 1976][research_latham_1976]\] \[[Latham et al 1977][research_latham_gawienowski_1977]\] \[[Lee and Boedicker 1985][research_lee_boedicker_1985]\] \[[Lee et al 2010][research_lee_ahn_2010]\] \[[Lee et al 2016][research_lee_lee_2016]\] \[[Lehtinen and Zeller 1972][research_lehtinen_zeller_1972]\] \[[Lehtinen and Zeller 1971][research_lehtinenb_zellerjr_1971]\] \[[Lehtinen et al 1978][research_lehtinenb_zellerjr_1978]\] \[[Leissler and Nettles 1954][research_leissler_nettles_1954]\] \[[Li et al 2023][research_li_ding_2023]\] \[[Li et al 2025][research_li_qu_2025]\] \[[Lian et al 2025][research_lian_xiong_2025]\] \[[Liou and Benson 2010][research_liou_benson_2010]\] \[[Liu et al 2015][research_liu_zhu_2015]\] \[[Liu et al 2021][research_liu_wang_2021]\] \[[Liu et al 2022][research_liu_kang_2022]\] \[[Liu et al 2024][research_liu_zhu_2024]\] \[[Liu et al 2025][research_liu_zhu_2025]\] \[[Liu et al 2025][research_liu_zhu_2025_b]\] \[[Liu et al 2026][research_liu_zhu_2026]\] \[[Lokotko and Kharitonov 2006][research_lokotko_kharitonov_2006]\] \[[Loth et al 2016][research_loth_candon_2016]\] \[[Lundell et al 1961][research_lundell_scherrer_1961]\] \[[Luo et al 2020][research_luo_wei_2020]\] \[[Luo et al 2024][research_luo_tao_2024]\] \[[Luo et al 2026][research_luo_meng_2026]\] \[[Lyubimov 2024][research_lyubimov_2024]\] \[[Lyubimov and Potekhina 2016][research_lyubimov_potekhina_2016]\] \[[Harish et al 2017][research_m_v_2017]\] \[[Ma et al 2025][research_ma_li_2025]\] \[[Ma et al 2026][research_ma_li_2026]\] \[[Malan and Brown 1994][research_malan_brown_1994]\] \[[Mann and Garner 1977][research_mann_garner_1977]\] \[[Marvin 1968][research_marvin_1968]\] \[[Mascitti 1966][research_mascitti_1966]\] \[[Mascitti 1969][research_mascitti_1969]\] \[[Mayer and Paynter 1994][research_mayer_paynter_1994]\] \[[Mazhul 2020][research_mazhul_2020]\] \[[McClure and Sirbaugh 1991][research_mcclure_sirbaugh_1991]\] \[[McVey et al 1969][research_mcvey_rejeske_1969]\] \[[Medina et al 2021][research_medina_patel_2021]\] \[[Meng et al 2018][research_meng_fan_2018]\] \[[Merchant and Radhakrishnan 2017][research_merchant_radhakrishnan_2017]\] \[[Merkli 1975][research_merkli_1975]\] \[[Merkli 1976][research_merkli_1976]\] \[[Messing and Rabb 1952][research_messing_rabb_1952]\] \[[Miao and Sun 2024][research_miao_sun_2024]\] \[[Miao et al 2026][research_miao_guan_2026]\] \[[Michell 1971][research_michellga_1971]\] \[[Miki et al 2014][research_miki_kameda_2014]\] \[[Miki et al 2015][research_miki_watanabe_2015]\] \[[Miller 1977][research_miller_1977]\] \[[Miller and Smith 2003][research_miller_smith_2003]\] \[[Mironov 1965][research_mironov_1965]\] \[[Mitcham et al 1951][research_mitcham_stevens_1951]\] \[[Moeckel 1955][research_moeckelwe_1955]\] \[[Moin and Lele 1998][research_moin_lele_1998]\] \[[Moon 2025][research_moon_2025]\] \[[Mount 1965][research_mount_1965]\] \[[Muller and Gasko 1967][research_muller_gasko_1967]\] \[[Muller and Gasko 1967][research_muller_gasko_1967_b]\] \[[Murzionak][research_murzionak]\] \[[Myokan et al 2020][research_myokan_kubota_2020]\] \[[Nadell 1996][research_nadell_1996]\] \[[Nagao et al 2019][research_nagao_yoshida_2019]\] \[[Nagler 2026][research_nagler_2026]\] \[[Neaves and McRae 1995][research_neaves_mcrae_1995]\] \[[Nettles 1956][research_nettles_1956]\] \[[Nichols and Rinkoski 1952][research_nichols_rinkoski_1952]\] \[[Nichols and Pendley 1952][research_nicholsmarkr_pendleyroberte_1952]\] \[[Ning][research_ning]\] \[[Novikov 2017][research_novikov_2017]\] \[[Et.al 2021][research_numerical_simulation_2021]\] \[[Numerical Simulation of Supersonic Flow through Scramjet Intake with Concavity in Cowl Surface 2020][research_numerical_simulation_2020]\] \[[Nussdorfer et al 1952][research_nussdorfertheodorej_oberyleonardj_1952]\] \[[Obey et al 1952][research_obeyleonardt_englertgeraldw_1952]\] \[[Obikane 1984][research_obikane_1984]\] \[[Osmon 1967][research_osmon_1967]\] \[[Oswatitsch 1947][research_oswatitsch_1947]\] \[[Otto et al 2015][research_otto_trefny_2015]\] \[[Palko 1973][research_palko_1973]\] \[[Palko 1974][research_palko_1974]\] \[[Palko 1975][research_palko_1975]\] \[[Park et al 1993][research_park_chung_1993]\] \[[Park et al 2001][research_park_lee_2001]\] \[[Paynter 1994][research_paynter_1994]\] \[[Paynter and Chen 1983][research_paynter_chen_1983]\] \[[Paynter et al 1992][research_paynter_treiber_1992]\] \[[Paynter et al 1993][research_paynter_mayer_1993]\] \[[Perkins and Dillenius 1991][research_perkins_dillenius_1991]\] \[[Pfyl 1955][research_pfyl_1955]\] \[[Philippou et al 2024][research_philippou_zachos_2024]\] \[[Platzer 1964][research_platzer_1964]\] \[[Poggie 2019][research_poggie_2019]\] \[[Poggie and Porter 2018][research_poggie_porter_2018]\] \[[Powell et al 1985][research_powellag_welgehr_1985]\] \[[Preliminary Design for Axisymmetric 2006][research_preliminary_design_2006]\] \[[Presley 1975][research_presley_1975]\] \[[Pruitt and Bates 1992][research_pruitt_bates_1992]\] \[[Qin and Liang 2016][research_qin_liang_2016]\] \[[Qu et al 2024][research_qu_wang_2024]\] \[[Rademakers et al 2018][research_rademakers_probst_2018]\] \[[Rajdeep Bose Mondal 2026][research_rajdeepbosemondal_2026]\] \[[Ramachandra et al 1979][research_ramachandra_sudhakar_1979]\] \[[Ran and Mavris 2005][research_ran_mavris_2005]\] \[[Rao et al 2025][research_rao_kumar_2025]\] \[[Ratnayake 2010][research_ratnayakenalina_2010]\] \[[Reddy et al 2023][research_reddy_govardhan_2023]\] \[[Rejeske and Stava 1974][research_rejeske_stava_1974]\] \[[Rettie and Lewis 1968][research_rettie_lewis_1968]\] \[[Reyhner and Hickcox 1972][research_reyhner_hickcox_1972]\] \[[Reza Maadi and Sepahi-Younsi 2022][research_rezamaadi_sepahiyounsi_2022]\] \[[Rizzetta 1991][research_rizzetta_1991]\] \[[Rizzetta and Visbal 2001][research_rizzetta_visbal_2001]\] \[[Rosenbaum and Zeiberg 1965][research_rosenbaumh_zeibergsl_1965]\] \[[Rowe and Sussman 1971][research_rowe_sussman_1971]\] \[[Ruban et al 2020][research_ruban_menezes_2020]\] \[[Runstadler and Peter W. 1969][research_runstadler_peterw_1969]\] \[[Rybalko and Loth 2015][research_rybalko_loth_2015]\] \[[Safoklov et al 2025][research_safoklov_demidov_2025]\] \[[Samimy et al 2011][research_samimy_webb_2011]\] \[[Saravanan et al 2017][research_saravanan_desikan_2017]\] \[[Sasoh et al 2018][research_sasoh_myokan_2018]\] \[[Saunders and Keith 1991][research_saundersjd_keithtgjr_1991]\] \[[Schweikhardt and Grippe 1971][research_schweikhardt_grippe_1971]\] \[[Schwendemann 1981][research_schwendemannmf_1981]\] \[[Scribben and Withrow 2006][research_scribben_withrow_2006]\] \[[Seleznev 2018][research_seleznev_2018]\] \[[Seleznev 2018][research_seleznev_2018_b]\] \[[Seleznev 2019][research_seleznev_2019]\] \[[Selna and Schlaff 1951][research_selna_schlaff_1951]\] \[[Sepahi-Younsi 2022][research_sepahiyounsi_2022]\] \[[Sepahi-Younsi 2025][research_sepahiyounsi_2025]\] \[[Shi et al 2018][research_shi_chang_2018]\] \[[Shi et al 2019][research_shi_chang_2019]\] \[[Shi et al 2019][research_shi_chang_2019_b]\] \[[Shimabukuro et al 1982][research_shimabukuro_welge_1982]\] \[[Shimabukuro et al 1979][research_shimabukurokm_welgehr_1979]\] \[[Shu et al 2025][research_shu_gao_2025]\] \[[Shucheng and Xijun 1994][research_shucheng_xijun_1994]\] \[[Shulman et al 1966][research_shulman_parry_1966]\] \[[Shvedchenko 2009][research_shvedchenko_2009]\] \[[Shvedchenko 2010][research_shvedchenko_2010]\] \[[Sinha et al 2026][research_sinha_singh_2026]\] \[[Slater][research_slater]\] \[[Slater][research_slater_b]\] \[[Slater 2019][research_slater_2019]\] \[[Slater 2020][research_slater_2020]\] \[[Slater 2023][research_slater_2023]\] \[[Slater 2024][research_slater_2024]\] \[[Slater 2011][research_slaterjohnw_2011]\] \[[Slater 2014][research_slaterjohnw_2014]\] \[[Slater 2015][research_slaterjohnw_2015]\] \[[Slater 2016][research_slaterjohnw_2016]\] \[[Slater 2017][research_slaterjohnw_2017]\] \[[Smeltzer and Sorensen 1972][research_smeltzerdb_sorensenne_1972]\] \[[Smith et al 2007][research_smith_scribben_2007]\] \[[Soltani and Askari 2019][research_soltani_askari_2019]\] \[[Soltani et al 2011][research_soltani_farahani_2011]\] \[[Soltani et al 2015][research_soltani_younsi_2015]\] \[[Soltani et al 2016][research_soltani_daliri_2016]\] \[[Sorensen and Bencze 1974][research_sorensen_bencze_1974]\] \[[Sorensen and Latham 1975][research_sorensen_latham_1975]\] \[[Sorensen and Smeltzer 1972][research_sorensen_smeltzer_1972]\] \[[Sorensen et al 1969][research_sorensen_smeltzer_1969]\] \[[Sorensen et al 1973][research_sorensen_smeltzer_1973]\] \[[Sorensen and Bencze 1973][research_sorensenne_benczedp_1973]\] \[[Sorrells et al 1984][research_sorrells_towne_1984]\] \[[Sousa et al 2017][research_sousa_paniagua_2017]\] \[[Sowers and Stueber][research_sowers_stueber]\] \[[Sowers and Stueber 2025][research_sowers_stueber_2025]\] \[[St. John and Frederick 2013][research_stjohn_frederick_2013]\] \[[Stephenson 1958][research_stephenson_1958]\] \[[Sterbentz and Davids 1952][research_sterbentzwilliamh_davidsjoseph_1952]\] \[[Stubbs 1956][research_stubbs_1956]\] \[[Sullivan 2002][research_sullivan_2002]\] \[[Sun and Zhang 2016][research_sun_zhang_2016]\] \[[Sun et al 2024][research_sun_zhang_2024]\] \[[Sun et al 2025][research_sun_yu_2025]\] \[[Sunderroy et al 2022][research_sunderroy_karnick_2022]\] \[[Surber 1975][research_surber_1975]\] \[[Surber and Robinson 1983][research_surber_robinson_1983]\] \[[Surber and Sedlock 1979][research_surber_sedlock_1979]\] \[[Syberg and Koncsek 1976][research_syberg_koncsek_1976]\] \[[Syberg et al 1981][research_syberg_paynter_1981]\] \[[Syberg and Koncsek 1972][research_sybergj_koncsekjl_1972]\] \[[Tabanli and Yuceil 2021][research_tabanli_yuceil_2021]\] \[[Taghi-Abad et al 2026][research_taghiabad_esfandabadi_2026]\] \[[Tang et al 2025][research_tang_cai_2025]\] \[[Tang et al 2025][research_tang_cai_2025_b]\] \[[Taylor 1968][research_taylor_1968]\] \[[Thomas et al 1999][research_thomas_won_1999]\] \[[Thomas and Stueber 2013][research_thomasrandy_stueberthomasj_2013]\] \[[Tindell 1980][research_tindell_1980]\] \[[Tindell 1981][research_tindell_1981]\] \[[Tomczak 2026][research_tomczak_2026]\] \[[Tongguang et al 2015][research_tongguang_changhui_2015]\] \[[Toro et al 1999][research_toro_myrabo_1999]\] \[[Trefny et al 2014][research_trefny_hirt_2014]\] \[[Trefny and Wasserbauer 1986][research_trefnycj_wasserbauerjw_1986]\] \[[Tudosie 2017][research_tudosie_2017]\] \[[Tudosie 2017][research_tudosie_2017_b]\] \[[Tudosie 2018][research_tudosie_2018]\] \[[Tudosie and Prisacariu 2022][research_tudosie_prisacariu_2022]\] \[[Tudosie and Păunescu 2017][research_tudosie_paunescu_2017]\] \[[Tudosie et al 2019][research_tudosie_dumitru_2019]\] \[[Türkkahraman et al 2024][research_turkkahraman_ozcan_2024]\] \[[Utomo and Bura 2019][research_utomo_bura_2019]\] \[[Vaca-Rios and Cerón-Muñoz 2025][research_vacarios_ceronmunoz_2025]\] \[[Veeresh Kumar et al 2021][research_veereshkumar_nagasailaja_2021]\] \[[Vinogradov et al 2017][research_vinogradov_makarov_2017]\] \[[Vinogradov et al 2017][research_vinogradov_melnikov_2017]\] \[[Walker et al 2005][research_walker_fletcher_2005]\] \[[Wan and Guo 2007][research_wan_guo_2007]\] \[[Wang and Zhao 2026][research_wang_zhao_2026_b]\] \[[Wang et al 2013][research_wang_wang_2013]\] \[[Wang et al 2015][research_wang_tian_2015]\] \[[Wang et al 2022][research_wang_zhao_2022]\] \[[Wang et al 2023][research_wang_sun_2023]\] \[[Wang et al 2023][research_wang_sun_2023_b]\] \[[Wang et al 2023][research_wang_wang_2023]\] \[[Wang et al 2023][research_wang_wang_2023_b]\] \[[Wang et al 2023][research_wang_zhao_2023_b]\] \[[Wang et al 2025][research_wang_chen_2025_b]\] \[[Wang et al 2025][research_wang_he_2025]\] \[[Wang et al 2025][research_wang_liu_2025]\] \[[Wang et al 2025][research_wang_tang_2025]\] \[[Wang et al 2025][research_wang_zhang_2025]\] \[[Wang et al 2025][research_wang_zhao_2025]\] \[[Wang et al 2025][research_wang_zhao_2025_b]\] \[[Wang et al 2026][research_wang_guan_2026]\] \[[Wang et al 2026][research_wang_yuan_2026]\] \[[Wang et al 2026][research_wang_zhao_2026]\] \[[Wasserbauer and Willoh 1968][research_wasserbauer_willoh_1968]\] \[[Wasserbauer et al 1996][research_wasserbauer_meleason_1996]\] \[[Wasserbauer and Gerstenmaier 1978][research_wasserbauerjf_gerstenmaierwh_1978]\] \[[Watanabe et al 2019][research_watanabe_houpt_2019]\] \[[Watanabe et al 2019][research_watanabe_leonov_2019]\] \[[Wegener 1977][research_wegener_1977]\] \[[Whalen and Wilcox 1956][research_whalenpaulp_wilcoxfreda_1956]\] \[[Wilcox 1957][research_wilcoxfreda_1957]\] \[[Williams and Hunt 1980][research_williams_hunt_1980]\] \[[Williams and Stevens 2006][research_williams_stevens_2006]\] \[[Willis 1981][research_willis_1981]\] \[[Woollett et al 1974][research_woollett_meleason_1974]\] \[[Wu et al 2022][research_wu_zhao_2022]\] \[[Xie et al 2025][research_xie_liu_2025]\] \[[Yaghmaee and Roberts 1986][research_yaghmaee_roberts_1986]\] \[[Yamaguchi 1964][research_yamaguchi_1964]\] \[[Yamamoto et al 2020][research_yamamoto_kojima_2020]\] \[[Yang and Lei 2011][research_yang_lei_2011]\] \[[Yang et al 2026][research_yang_kong_2026]\] \[[Yao et al 2017][research_yao_zhang_2017]\] \[[Yeom et al 2015][research_yeom_sung_2015]\] \[[Yonke et al 1995][research_yonkewilliama_robbendaniell_1995]\] \[[You et al 2016][research_you_yu_2016]\] \[[Yu et al 2021][research_yu_huang_2021]\] \[[Yuan et al 2021][research_yuan_liu_2021]\] \[[Yuan et al 2021][research_yuan_zhang_2021]\] \[[Yuan et al 2023][research_yuan_li_2023]\] \[[Zhang 2020][research_zhang_2020_b]\] \[[Zhang et al 2015][research_zhang_tan_2015]\] \[[Zhang et al 2018][research_zhang_tan_2018]\] \[[Zhang et al 2020][research_zhang_yuan_2020]\] \[[Zhang et al 2026][research_zhang_ning_2026]\] \[[Zhang et al 2026][research_zhang_yang_2026]\] \[[Zhao et al 2022][research_zhao_zhou_2022]\] \[[Zhu et al 2020][research_zhu_luo_2020]\]

### Inlet distortion and inlet-engine compatibility

**The turbofan's exposure.** Total-pressure, swirl and temperature distortion at the engine face, its descriptors and generators, inlet and engine compatibility, and boundary-layer-ingesting propulsion, which accepts distortion by design.

**260 records.** \[[Abbasi et al 2018][research_abbasi_pirnia_2018]\] \[[Ahuja and Mavris 2022][research_ahuja_mavris_2022]\] \[[Alendar et al 2022][research_alendar_grunin_2022]\] \[[Alford et al 1962][research_alford_davies_1962]\] \[[Analysis of Flow Field Distortion in Ship Inlet System and Its Effect on Compressor Performance 2024][research_analysis_of_2024]\] \[[Anderson and Levy 1991][research_andersonbernhardh_levyralph_1991]\] \[[Assessment of the Inlet/Engine][research_assessment_of]\] \[[Assessment of Total Pressure 2023][research_assessment_of_2023_b]\] \[[Atassi et al 2019][research_atassi_kozlov_2019]\] \[[Bakhle et al 2018][research_bakhlemilinda_reddytsr_2018]\] \[[Baretter et al 2021][research_baretter_godard_2021]\] \[[Battiston et al 2025][research_battiston_magrini_2025]\] \[[Benichou et al 2021][research_benichou_binder_2021]\] \[[Bhunia et al 2026][research_bhunia_abbas_2026]\] \[[Bilwakesh et al 1971][research_bilwakeshkr_doylevl_1971]\] \[[Bilwakesh et al 1972][research_bilwakeshkr_kochcc_1972]\] \[[Bond and Key 2025][research_bond_key_2025]\] \[[Bond and Key 2026][research_bond_key_2026]\] \[[Bond et al 2025][research_bond_brown_2025]\] \[[Bowditch and Coltrin 1983][research_bowditchdn_coltrinre_1983]\] \[[Braithwaite and Soeder 1980][research_braithwaite_soeder_1980]\] \[[Braithwaite 1973][research_braithwaitewm_1973]\] \[[Braithwaite and Soeder 1979][research_braithwaitewm_soederrh_1979]\] \[[Brilliant and Bauer 1977][research_brilliant_bauer_1977]\] \[[Burstadt and Calogeras 1974][research_burstadtpl_calogerasje_1974]\] \[[Burstadt and Wenzel 1976][research_burstadtpl_wenzellm_1976]\] \[[Burstadt et al 1971][research_burstadtpl_calogerasje_1971]\] \[[Callahan and Stenning 1971][research_callahan_stenning_1971]\] \[[Calogeras and Burstadt 1974][research_calogerasje_burstadtpl_1974]\] \[[Calogeras and Coltrin 1969][research_calogerasje_coltrinre_1969]\] \[[Calogeras et al 1974][research_calogerasje_johnsenrl_1974]\] \[[Campbell and Ellis 1971][research_campbell_ellis_1971]\] \[[Campion 1954][research_campion_1954]\] \[[Carnevale et al 2016][research_carnevale_wang_2016]\] \[[Chen et al 1987][research_chengt_greitzerem_1987]\] \[[Chennuru et al 2025][research_chennuru_corral_2025]\] \[[Ciepluch 1948][research_ciepluchcarlc_1948]\] \[[Concept Designed and Developed 1995][research_concept_designed_1995]\] \[[Costakis 1974][research_costakiswg_1974]\] \[[Costakis 1975][research_costakiswg_1975]\] \[[Crea et al 2025][research_crea_marty_2025]\] \[[Da et al 2020][research_da_hanan_2020]\] \[[Davoudzadeh et al 1987][research_davoudzadeh_liu_1987]\] \[[Debogdan et al 1975][research_debogdance_dicusjh_1975]\] \[[Debogdan et al 1977][research_debogdance_mossjejr_1977]\] \[[Deng et al 2026][research_deng_li_2026]\] \[[Di-Marco et al 2023][research_dimarco_jacob_2023]\] \[[Diamantidou et al 2022][research_diamantidou_hosain_2022]\] \[[Dicus 1975][research_dicus_1975]\] \[[Dunham 1962][research_dunham_1962]\] \[[Greitzer 1972][research_greitzer_1972]\] \[[Reich and Wimbauer 1975][research_dieterreich_josefwimbauer_1975]\] \[[Dong et al 2015][research_dong_sun_2015]\] \[[Dong et al 2018][research_dong_sun_2018]\] \[[Du et al 2023][research_du_liu_2023]\] \[[Duvall and Arnaiz 1977][research_duvall_arnaiz_1977]\] \[[Effect of Exhaust Jet from Takeoff Aircraft on the Inlet Distortion of Runway-Crossing Aircraft 2024][research_effect_of_2024]\] \[[Ellis and Brownstein 1974][research_ellis_brownstein_1974]\] \[[Evans et al 1974][research_evansdg_debogdance_1974]\] \[[Ezrokhi and Khoreva 2018][research_ezrokhi_khoreva_2018]\] \[[Fan et al 2024][research_fan_liu_2024]\] \[[Fan et al 2025][research_fan_du_2025]\] \[[Fan et al 2026][research_fan_li_2026]\] \[[Fan et al 2026][research_fan_xu_2026]\] \[[Fan et al 2026][research_fan_xu_2026_b]\] \[[Fang and Wang 2023][research_fang_wang_2023]\] \[[Fang et al 2023][research_fang_sun_2023]\] \[[Feng et al 2022][research_feng_tianyu_2022]\] \[[Ferrar et al 2016][research_ferrar_schneck_2016]\] \[[Frohnapfel et al 2017][research_frohnapfel_obrien_2017]\] \[[Frohnapfel et al 2018][research_frohnapfel_toddlowe_2018]\] \[[Frohnapfel et al 2021][research_frohnapfel_tlowe_2021]\] \[[Fuqun et al 1985][research_fuqun_wenlan_1985]\] \[[GAS Turbine Engine Inlet][research_gas_turbine]\] \[[Gelder 1957][research_gelderthomasf_1957]\] \[[Geng et al 2025][research_geng_yang_2025]\] \[[Goldberg and Boxer 1959][research_goldberg_boxer_1959]\] \[[Gray and Martins 2018][research_gray_martins_2018]\] \[[Gray et al 2020][research_gray_mader_2020]\] \[[Gray et al 2017][research_grayjustins_madercharlesa_2017]\] \[[Jones et al 2020][research_gregorysjones_williammilholen_2020]\] \[[Gu et al 2023][research_gu_xu_2023]\] \[[Guidelines for Characterization of][research_guidelines_for]\] \[[Guimaraes et al 2015][research_guimaraes_lowe_2015]\] \[[Guimarães et al 2018][research_guimaraes_lowe_2018]\] \[[Guo et al 2021][research_guo_hu_2021]\] \[[Hall et al 2017][research_hall_greitzer_2017]\] \[[Hall et al 2022][research_hall_greitzer_2022]\] \[[Hall et al 2022][research_hall_greitzer_2022_b]\] \[[Hawthorne et al 1978][research_hawthorne_mitchell_1978]\] \[[Hayden and Untaroiu 2021][research_hayden_untaroiu_2021]\] \[[Hayden et al 2023][research_hayden_gillespie_2023]\] \[[Hill and Defoe 2020][research_hill_defoe_2020]\] \[[Hou et al 2017][research_hou_wang_2017]\] \[[Hubble and Smith 1979][research_hubble_smith_1979]\] \[[Inlet Total-Pressure-Distortion Considerations for][research_inlet_total_pressure_distortion]\] \[[Jacocks and Kneile 1975][research_jacocks_kneile_1975]\] \[[Karl et al 2025][research_karl_werner_2025]\] \[[King et al 1976][research_kingrw_schuermanja_1976]\] \[[Klann et al 1984][research_klannga_barthrl_1984]\] \[[Korn 1974][research_korn_1974]\] \[[Korn 1974][research_korn_1974_b]\] \[[Kramer and Hall 2026][research_kramer_hall_2026]\] \[[Kumar and Pradeep 2022][research_kumar_pradeep_2022]\] \[[Kwiatkowski et al 2022][research_kwiatkowski_sieradzki_2022]\] \[[Lee et al 2019][research_lee_lee_2019]\] \[[Lee et al 2018][research_leebj_lioumayfun_2018]\] \[[Lee and Liou 2018][research_leebyungjoon_lioumayfun_2018]\] \[[Lee et al 2019][research_leebyungjoon_lioumayfun_2019]\] \[[Leinhos et al 2000][research_leinhos_schmid_2000]\] \[[Lengyel-Kampmann et al 2024][research_lengyelkampmann_karboujian_2024]\] \[[Lesser and Niehuis 2014][research_lesser_niehuis_2014]\] \[[Li et al 2020][research_li_du_2020]\] \[[Li et al 2020][research_li_du_2020_b]\] \[[Li et al 2021][research_li_dong_2021]\] \[[Li et al 2022][research_li_zhu_2022]\] \[[Li et al 2023][research_li_zhu_2023]\] \[[Li et al 2024][research_li_hou_2024]\] \[[Li et al 2024][research_li_liu_2024_b]\] \[[Li et al 2024][research_li_lu_2024]\] \[[Li et al 2024][research_li_zhu_2024]\] \[[Li et al 2024][research_li_zhu_2024_b]\] \[[Li et al 2025][research_li_sun_2025]\] \[[Liang and Zhang 1989][research_liang_zhang_1989]\] \[[Liu and Vo 2024][research_liu_vo_2024]\] \[[Liu et al 2022][research_liu_li_2022]\] \[[Liu et al 2022][research_liu_zhang_2022]\] \[[Liu et al 2023][research_liu_huang_2023]\] \[[Liu et al 2023][research_liu_li_2023]\] \[[Liu et al 2025][research_liu_du_2025]\] \[[Liu et al 2026][research_liu_du_2026]\] \[[Lomax and Heaslet 1956][research_lomaxharvard_heasletmaxa_1956]\] \[[Lowe 2020][research_lowe_2020]\] \[[Lu et al 2019][research_lu_yang_2019]\] \[[Lu et al 2025][research_lu_li_2025]\] \[[Lu et al 2025][research_lu_wang_2025]\] \[[Lu-ning et al 2021][research_luning_bangqin_2021]\] \[[Lucas et al 2014][research_lucas_obrien_2014]\] \[[Luo Ju 2009][research_luoju_2009]\] \[[Ma et al 2018][research_ma_cui_2018]\] \[[Ma et al 2025][research_ma_lu_2025]\] \[[Ma et al 2025][research_ma_wang_2025]\] \[[MacManus et al 2017][research_macmanus_chiereghin_2017]\] \[[Maekawa et al 1978][research_maekawa_higashi_1978]\] \[[Maghsoudi et al 2020][research_maghsoudi_vaziry_2020]\] \[[Magrini and Benini 2026][research_magrini_benini_2026]\] \[[Mao and Zhang 2025][research_mao_zhang_2025]\] \[[Masaki et al 2021][research_masaki_ogushi_2021]\] \[[Mazzawy and Banks 1976][research_mazzawyrs_banksga_1976]\] \[[Mazzawy and Banks 1977][research_mazzawyrs_banksga_1977]\] \[[Mehalic 1988][research_mehalic_1988]\] \[[Melick et al 1975][research_melick_ybarra_1975]\] \[[Melick et al 1978][research_melick_ybarra_1978]\] \[[Melick 1973][research_melickhcjr_1973]\] \[[Menegozzo and Benini 2020][research_menegozzo_benini_2020]\] \[[Min et al 2018][research_minjb_reddytsr_2018]\] \[[Ming et al 2023][research_ming_wu_2023]\] \[[Moirou et al 2023][research_moirou_sanders_2023]\] \[[Moore 1973][research_moore_1973]\] \[[Moore and Lueke 1974][research_moore_lueke_1974]\] \[[Musa et al 2024][research_musa_huang_2024]\] \[[Muth et al 2009][research_muth_bindl_2009]\] \[[Mårtensson 2021][research_martensson_2021]\] \[[Mårtensson and Billson 2024][research_martensson_billson_2024]\] \[[Mårtensson et al 2022][research_martensson_lejon_2022]\] \[[Naruse et al 2022][research_naruse_ishii_2022]\] \[[Naseri et al 2016][research_naseri_boroomand_2016]\] \[[Nelson et al 2014][research_nelson_lowe_2014]\] \[[Overall 1976][research_overall_1976]\] \[[Page et al 2018][research_page_hield_2018]\] \[[Pan et al 2022][research_pan_shi_2022]\] \[[Pan et al 2024][research_pan_mu_2024]\] \[[Pan et al 2024][research_pan_shi_2024]\] \[[Panton 1972][research_panton_1972]\] \[[Park et al 2026][research_park_kim_2026]\] \[[Petkovic et al 2025][research_petkovic_banjac_2025]\] \[[Pečinka et al 2017][research_pecinka_bugajski_2017]\] \[[Piovesan et al 2025][research_piovesan_zachos_2025]\] \[[Plourde and Stenning 1968][research_plourde_stenning_1968]\] \[[Prasad 2025][research_prasad_2025]\] \[[Processing and Validating CFD][research_processing_and]\] \[[Provenza et al 2018][research_provenza_duffy_2018]\] \[[Qiang et al 2024][research_qiang_xue_2024]\] \[[Qiu et al 2023][research_qiu_du_2023]\] \[[Qiu et al 2023][research_qiu_zhao_2023]\] \[[Qiu et al 2024][research_qiu_zhong_2024]\] \[[Rao et al 2022][research_rao_sureshkumar_2022]\] \[[Reedy and Gorrell 2025][research_reedy_gorrell_2025]\] \[[Saleem Yusoof et al 2016][research_saleemyusoof_sivapragasam_2016]\] \[[Sanders 1980][research_sanders_1980]\] \[[Sedlock 1985][research_sedlock_1985]\] \[[Seidel et al 1980][research_seidel_matwey_1980]\] \[[Shang et al 2021][research_shang_ge_2021]\] \[[Sitaram et al 2023][research_sitaram_govardhan_2023]\] \[[Soeder and Bobula 1979][research_soederrh_bobulaga_1979]\] \[[Soeder and Bobula 1979][research_soederrh_bobulaga_1979_b]\] \[[Soeder and Bobula 1982][research_soederrh_bobulaga_1982]\] \[[Soeder and Mehalic 1984][research_soederrh_mehaliccm_1984]\] \[[Steenken et al 1999][research_steenkenwg_williamsjg_1999]\] \[[Stenning 1980][research_stenning_1980]\] \[[Sun et al 2022][research_sun_li_2022]\] \[[Sun et al 2024][research_sun_gu_2024]\] \[[Sun et al 2024][research_sun_gu_2024_b]\] \[[Sun et al 2025][research_sun_shen_2025]\] \[[Sun et al 2025][research_sun_yang_2025]\] \[[Sussman 1968][research_sussman_1968]\] \[[Sweep Optimization to Reduce Aerodynamic Loss in a Transonic Axial Compressor with Upstream Boundary Layer Ingestion 2024][research_sweep_optimization_2024]\] \[[Tan and Suder 2003][research_tanchoonsooi_suderkenneth_2003]\] \[[Tanguy et al 2018][research_tanguy_macmanus_2018]\] \[[Tanida 1972][research_tanida_1972]\] \[[Tao et al 2022][research_tao_jin_2022]\] \[[Tesch and Steenken 1978][research_teschwa_steenkenwg_1978]\] \[[Using Tip Injection to Stability Enhancement of a Transonic Centrifugal Impeller with Inlet Distortion 2022][research_using_tip_2022]\] \[[Valencia et al 2017][research_valencia_hidalgo_2017]\] \[[Valencia et al 2020][research_valencia_alulema_2020]\] \[[Van Deusen and Mardoc 1972][research_vandeusen_mardoc_1972]\] \[[Dippold 2022][research_vancefdippoldiii_2022]\] \[[VanSchalkwyk et al 2001][research_vanschalkwykchristian_brightmichellem_2001]\] \[[Verma et al 2020][research_verma_singh_2020]\] \[[Wallner et al 1955][research_wallnerle_lubickrj_1955]\] \[[Wallner et al 1954][research_wallnerlewise_lubickrobertj_1954]\] \[[Wang et al 2013][research_wang_wang_2013_b]\] \[[Wang et al 2017][research_wang_chen_2017]\] \[[Wang et al 2020][research_wang_hu_2020]\] \[[Wang et al 2023][research_wang_zhao_2023]\] \[[Wang et al 2024][research_wang_fan_2024]\] \[[Wang et al 2024][research_wang_he_2024]\] \[[Wang et al 2024][research_wang_liu_2024]\] \[[Wang et al 2025][research_wang_li_2025]\] \[[Williams and Yost 1973][research_williams_yost_1973]\] \[[Won 1990][research_won_1990]\] \[[Wu et al 2024][research_wu_li_2024]\] \[[Wu et al 2024][research_wu_li_2024_b]\] \[[Wu et al 2026][research_wu_du_2026]\] \[[Xie et al 2023][research_xie_zhu_2023]\] \[[Xu and Hu 2022][research_xu_hu_2022_b]\] \[[Xu et al 2021][research_xu_hu_2021]\] \[[Xu et al 2022][research_xu_hu_2022]\] \[[Xu et al 2023][research_xu_hu_2023]\] \[[Xu et al 2025][research_xu_wu_2025]\] \[[Yamamoto and Ng 1997][research_yamamoto_ng_1997]\] \[[Yan et al 2025][research_yan_pan_2025]\] \[[Yang et al 2021][research_yang_lu_2021]\] \[[Yang et al 2022][research_yang_lu_2022]\] \[[Yeh 1959][research_yeh_1959]\] \[[Yu et al 2026][research_yu_zhao_2026]\] \[[Yuan et al 2026][research_yuan_lu_2026]\] \[[Zachos et al 2016][research_zachos_macmanus_2016]\] \[[Zhang and Hou 2015][research_zhang_hou_2015]\] \[[Zhang and Vahdati 2018][research_zhang_vahdati_2018]\] \[[Zhang and Vahdati 2019][research_zhang_vahdati_2019]\] \[[Zhang et al 2020][research_zhang_stapelfeldt_2020]\] \[[Zhang et al 2021][research_zhang_li_2021]\] \[[Zhang et al 2024][research_zhang_chen_2024]\] \[[Zhang et al 2024][research_zhang_liu_2024]\] \[[Zhao et al 2017][research_zhao_sun_2017]\] \[[Zhao et al 2022][research_zhao_vanhoorn_2022]\] \[[Zhao et al 2023][research_zhao_jin_2023]\] \[[Zhipeng et al 2015][research_zhipeng_chao_2015]\] \[[Zhou et al 2019][research_zhou_li_2019]\]

### Drag polars, wave drag and supersonic aerodynamics

**The drag side of the sizing.** Drag polars and their estimation, wave drag and the area rule, conical flow, and supersonic and transonic aerodynamics of bodies and configurations.

**195 records.** \[[2015][research_anon_2015]\] \[[Abraham et al 2024][research_abraham_lazzara_2024]\] \[[Aerodynamic Drag in Cruising 2020][research_aerodynamic_drag_2020]\] \[[Afridi et al 2024][research_afridi_khan_2024]\] \[[Aircraft Drag 2010][research_aircraft_drag_2010]\] \[[Antaran et al 1992][research_antaranalbert_beletehailu_1992]\] \[[Army War Coll Carlisle Barracks Pa 1952][research_armywarcollcarlislebarrackspa_1952]\] \[[Back and Cuffel 1966][research_backlh_cuffelrf_1966]\] \[[Ban et al 2018][research_ban_yamazaki_2018]\] \[[Bennet-Clark 1972][research_bennetclark_1972]\] \[[Bera 1975][research_bera_1975]\] \[[Bera† 1980][research_bera_1980]\] \[[Bleviss and Struble 1954][research_bleviss_struble_1954]\] \[[Briggs 1960][research_briggsbenjaminr_1960]\] \[[Brown 1961][research_brown_1961]\] \[[Brown 1946][research_brownclintone_1946]\] \[[Browne et al 1948][research_browne_friedman_1948]\] \[[Bull and Bridges 1983][research_bullg_bridgespd_1983]\] \[[Burkhalter 1982][research_burkhalter_1982]\] \[[Bushnell 1990][research_bushnell_1990]\] \[[Butler 1982][research_butler_1982]\] \[[Cassetti 1978][research_cassetti_1978]\] \[[Chen and Li 2020][research_chen_li_2020]\] \[[Chester 1953][research_chester_1953]\] \[[Chin 1977][research_chin_1977]\] \[[Chin 1978][research_chin_1978]\] \[[Clarke and Wallace 1964][research_clarke_wallace_1964]\] \[[Craidon 1986][research_craidoncb_1986]\] \[[Cui et al 2024][research_cui_zhang_2024]\] \[[Dai and Zhang 2023][research_dai_zhang_2023]\] \[[Davis 1971][research_davis_1971]\] \[[de Paula et al 2017][research_depaula_porto_2017]\] \[[Dehua and Changyou 1993][research_dehua_changyou_1993]\] \[[Desai et al 1977][research_desai_viswanathan_1977]\] \[[Design and Numerical Analysis of E-D Nozzle with Throat Radius Investigation in Supersonic Flows: A Comparison Study with Tic Nozzle 2024][research_design_and_2024]\] \[[Dickey 1959][research_dickeyrobertr_1959]\] \[[Durmus 2021][research_durmus_2021]\] \[[Durston and Stonum 1987][research_durston_stonum_1987]\] \[[Evvard 1947][research_evvardjohnc_1947]\] \[[Felix et al 2026][research_felix_perron_2026]\] \[[Ferrari 1958][research_ferrari_1958]\] \[[Flow structure and parameter evaluation of conical convergent-divergent nozzle supersonic jet flows 2023][research_flow_structure_2023]\] \[[Gillespie 1960][research_gillespiewarrenjr_1960]\] \[[Gilman and Burdges 1967][research_gilman_burdges_1967]\] \[[Golubkin 1980][research_golubkin_1980]\] \[[Goodman 1949][research_goodman_1949]\] \[[Gorbovskoi et al 2019][research_gorbovskoi_kazhan_2019]\] \[[Goto et al 2021][research_goto_nakayama_2021]\] \[[Goulos et al 2021][research_goulos_otter_2021]\] \[[Graham et al 1954][research_graham_lagerstrom_1954]\] \[[Gringorten and Tattelman 1970][research_gringorten_tattelman_1970]\] \[[Groth 1961][research_groth_1961]\] \[[Guderley 1987][research_guderley_1987]\] \[[Guderley 1988][research_guderley_1988]\] \[[Gudmundsson 2014][research_gudmundsson_2014]\] \[[Gur et al 2010][research_gur_mason_2010]\] \[[Götten et al 2021][research_gotten_havermann_2021]\] \[[Hall and Heitmeyer 1951][research_hallcharlesf_heitmeyerjohnc_1951]\] \[[Hancock 1959][research_hancock_1959]\] \[[Hancock 1959][research_hancock_1959_b]\] \[[Hantrais-Gervois and Destarac 2015][research_hantraisgervois_destarac_2015]\] \[[Hartley et al 1965][research_hartley_furey_1965]\] \[[Hawkins and Penland 1997][research_hawkinsrichard_penlandjima_1997]\] \[[Hernandez et al 1994][research_hernandezgloria_woodrichardm_1994]\] \[[Hillier 1970][research_hillier_1970]\] \[[Hoerner 1936][research_hoerner_1936]\] \[[Holdaway et al 1959][research_holdawaygeorgeh_lazzeronifranka_1959]\] \[[Hrubecky 1963][research_hrubecky_1963]\] \[[Hsu and Anderson 1961][research_hsu_anderson_1961]\] \[[Hui 1975][research_hui_1975]\] \[[Hunt and Gowadia 1981][research_hunt_gowadia_1981]\] \[[Hunziker 1960][research_hunziker_1960]\] \[[Isugiyama 1976][research_isugiyama_1976]\] \[[Jack 1951][research_jackjohnr_1951]\] \[[Jones 1972][research_jones_1972]\] \[[Jones 1976][research_jonesrt_1976]\] \[[Jones 1956][research_jonesrobertt_1956]\] \[[Jones 1953][research_jonesrobertt_1953]\] \[[Kawamura and Karashima 1957][research_kawamura_karashima_1957]\] \[[Kayser and Danberg 1974][research_kayser_danberg_1974]\] \[[Kohn 1979][research_kohn_1979]\] \[[Kraiko and Tilliaeva 1973][research_kraiko_tilliaeva_1973]\] \[[Laitone 1978][research_laitone_1978]\] \[[Lee and Franz 1976][research_lee_franz_1976]\] \[[Leslie and Perry 1954][research_leslie_perry_1954]\] \[[Levy 1959][research_levylionelljr_1959]\] \[[Levy and Yoshikawa 1959][research_levylionelljr_yoshikawakennethk_1959]\] \[[Li and Geiselhart 2021][research_li_geiselhart_2021]\] \[[Li and Geiselhart 2026][research_li_geiselhart_2026]\] \[[Lock 1957][research_lock_1957]\] \[[Lomax 1957][research_lomaxharvard_1957]\] \[[Lovell 2001][research_lovell_2001]\] \[[Maikapar 1959][research_maikapar_1959]\] \[[Maikapar 1966][research_maikapar_1966]\] \[[Maise 1970][research_maise_1970]\] \[[Malmuth 1966][research_malmuth_1966]\] \[[Malmuth et al 1987][research_malmuth_wu_1987]\] \[[Malone and Peavey 1999][research_malonemichaelb_peaveycharlesc_1999]\] \[[Margolis 1947][research_margoliskenneth_1947]\] \[[Margolis et al 1958][research_margoliskenneth_malvestutofranksjr_1958]\] \[[Martin and Brazzel 1970][research_martin_brazzel_1970]\] \[[Mathur 1998][research_mathur_1998]\] \[[Matranga and Armstrong 1959][research_matrangagenej_armstrongneila_1959]\] \[[Mazurov 2015][research_mazurov_2015]\] \[[Mazurov 2019][research_mazurov_2019]\] \[[McMillin and Wood 1986][research_mcmillinsn_woodrm_1986]\] \[[Menees and Boyd 1959][research_meneesgenep_boydjohnw_1959]\] \[[Miles 1953][research_miles_1953]\] \[[Miller et al 1983][research_millerds_pittmanjl_1983]\] \[[Mizobata et al 2024][research_mizobata_mio_2024]\] \[[Moeckel and Evans 1951][research_moeckelwe_evanspjjr_1951]\] \[[Moga 1980][research_moga_1980]\] \[[Narayan 1975][research_narayan_1975]\] \[[Nelson and Welsh 1960][research_nelsonrobertl_welshclementj_1960]\] \[[Nielsen 1985][research_nielsenjn_1985]\] \[[Nielsen et al 1953][research_nielsenjackn_kaattarigeorgee_1953]\] \[[Orman et al 1951][research_orman_rae_1951]\] \[[Oruç 2026][research_oruc_2026]\] \[[Osborne and Kelly 1953][research_osborneroberts_kellythomasc_1953]\] \[[Ostieri and Tognaccini 2018][research_ostieri_tognaccini_2018]\] \[[Ostowari and Naik 1986][research_ostowaric_naikd_1986]\] \[[Oswatitsch 1952][research_oswatitsch_1952]\] \[[Oswatitsch 1958][research_oswatitsch_1958]\] \[[Oswatitsch 1980][research_oswatitsch_1980]\] \[[Panov and Shvets 1967][research_panov_shvets_1967]\] \[[Panov et al 1966][research_panov_shvets_1966]\] \[[Payne 1980][research_payne_1980]\] \[[Petersen 1957][research_petersenrb_1957]\] \[[Petruzzelli and Keane 2001][research_petruzzelli_keane_2001]\] \[[Pfaff 1965][research_pfaff_1965]\] \[[Pfaff 1968][research_pfaff_1968]\] \[[Polhamus 1968][research_polhamusec_1968]\] \[[Portnoy 1963][research_portnoy_1963]\] \[[Ramaswamy and Viswanathan 1975][research_ramaswamy_viswanathan_1975]\] \[[Reist et al 2022][research_reist_koo_2022]\] \[[Reukauf and Burcham 1976][research_reukaufpj_burchamfwjr_1976]\] \[[Osborne and Kelly 1960][research_robertsosborne_thomasckelly_1960]\] \[[Rowe 1958][research_rowe_1958]\] \[[Rylov 1974][research_rylov_1974]\] \[[Sachs 1977][research_sachs_1977]\] \[[Sachs 1980][research_sachs_1980]\] \[[Sahoo and Peetala 2010][research_sahoo_peetala_2010]\] \[[Sahu 1986][research_sahu_1986]\] \[[Sandahl 1948][research_sandahlcarla_1948]\] \[[Shevell 1978][research_shevell_1978]\] \[[Sibulkin 1951][research_sibulkin_1951]\] \[[Singh and Dwivedi 2022][research_singh_dwivedi_2022]\] \[[Smart et al 1994][research_smartmichaelk_kalkhoranirajm_1994]\] \[[Smith 1954][research_smithwilliardg_1954]\] \[[Solomon 1955][research_solomongeorgee_1955]\] \[[Stancil 1979][research_stancil_1979]\] \[[Stanišić 1961][research_stanisic_1961]\] \[[Steer 2003][research_steer_2003]\] \[[Stewart 1956][research_stewart_1956]\] \[[Stewartson 1950][research_stewartson_1950]\] \[[Stocker 1951][research_stocker_1951]\] \[[Stone 1945][research_stone_1945]\] \[[Sugiyama 1977][research_sugiyama_1977]\] \[[Sun and Smith 2019][research_sun_smith_2019]\] \[[Supersonic Flight 2014][research_supersonic_flight_2014]\] \[[Takovitskii 2020][research_takovitskii_2020]\] \[[Takovitsky 2018][research_takovitsky_2018]\] \[[Thein 2018][research_thein_2018]\] \[[Thomas 1942][research_thomas_1942]\] \[[Ting et al 2018][research_ting_chaparro_2018]\] \[[Transonic and supersonic flight 1992][research_transonic_and_1992]\] \[[Vaisakh et al 2019][research_vaisakh_namratha_2019]\] \[[van Es 2002][research_vanes_2002]\] \[[Vasil'ev 1970][research_vasilev_1970]\] \[[Vieira et al 2025][research_vieira_soltz_2025]\] \[[Vira and Fan 1982][research_viranr_fandn_1982]\] \[[von Doenhoff and Horton 1942][research_vondoenhoffalberte_hortonelmera_1942]\] \[[Walkley 1986][research_walkley_1986]\] \[[Wallskog 1954][research_wallskog_1954]\] \[[Wallskog 1954][research_wallskog_1954_b]\] \[[Ward 1949][research_ward_1949]\] \[[Ward 1968][research_ward_1968]\] \[[Wasserman 1952][research_wasserman_1952]\] \[[Wetzel 1955][research_wetzelbentone_1955]\] \[[Whitcomb 1953][research_whitcombrichardt_1953]\] \[[Whitcomb and Sevier 1960][research_whitcombrichardt_sevierjohnrjr_1960]\] \[[Winograd and Miles 1956][research_winograd_miles_1956]\] \[[Wood and Miller 1985][research_woodrm_millerds_1985_b]\] \[[Li and Geiselhart 2020][research_wuli_karlgeiselhart_2020]\] \[[Xu 2023][research_xu_2023]\] \[[Yajnik and Subbaiah 1976][research_yajnik_subbaiah_1976]\] \[[Yamanaka and Kamimura 1975][research_yamanaka_kamimura_1975]\] \[[Yamazaki et al 2019][research_yamazaki_mizobata_2019]\] \[[Yoshida 2009][research_yoshida_2009]\] \[[Zaman et al 2025][research_zaman_korth_2025]\] \[[Zhang 2020][research_zhang_2020]\] \[[Zhang 2024][research_zhang_2024]\] \[[Zhang et al 2015][research_zhang_chen_2015]\] \[[Zuo 2021][research_zuo_2021]\] \[[Zuo 2023][research_zuo_2023]\]

### Compressor stall, surge and casing treatment

**What a distorted inlet does to a compressor.** Rotating stall and surge, their inception, warning and active control, and casing treatment, in aero-engine and in industrial machines alike.

**192 records.** \[[Ahmad et al 2021][research_ahmad_zheng_2021]\] \[[Akhlaghi and Azizi 2023][research_akhlaghi_azizi_2023]\] \[[Akhlaghi et al 2022][research_akhlaghi_azizi_2022]\] \[[Alone et al 2016][research_alone_kumar_2016]\] \[[Amann et al 1975][research_amann_nordenson_1975]\] \[[Analysis of Anti-surge Control Method for Axial Flow Compressor 2021][research_analysis_of_2021]\] \[[Anantachaisilp and Lin 2020][research_anantachaisilp_lin_2020]\] \[[Anti-Surge Control of Centrifugal Compressor and Implementation Strategy 2021][research_anti_surge_control_2021]\] \[[Anti-surge Reason and Control Technology of Large Centrifugal Compressor 2021][research_anti_surge_reason_2021]\] \[[Application of Centrifugal Compressor Control and Anti-surge System Control 2021][research_application_of_2021]\] \[[Application of PLC in Anti-surge Control System of Centrifugal Compressor 2021][research_application_of_2021_b]\] \[[Application Practice of Anti-surge Control in Compressor Transformation 2021][research_application_practice_2021]\] \[[Aribi and Boushaki 2023][research_aribi_boushaki_2023]\] \[[AXIAL TRANSONIC COMPRESSOR STALL MECHANISM WITH DIFFERENT ROTATIONAL SPEEDS 2022][research_axial_transonic_2022]\] \[[Azizi and Brouwer 2017][research_azizi_brouwer_2017]\] \[[Bammert and Mobarak 1976][research_bammert_mobarak_1976]\] \[[Bammert and Mobarak 1976][research_bammert_mobarak_1976_b]\] \[[Batayev et al 2022][research_batayev_suleimenov_2022]\] \[[Boussios et al 1992][research_boussios_epstein_1992]\] \[[Breugelmans 1975][research_breugelmans_1975]\] \[[Burwell and Patterson 1985][research_burwell_patterson_1985]\] \[[Cabrera Cruz et al 2020][research_cabreracruz_pezzini_2020]\] \[[Cao et al 2022][research_cao_yuan_2022]\] \[[Cevik et al 2016][research_cevik_ducvo_2016]\] \[[Chen et al 2026][research_chen_zheng_2026]\] \[[Chi et al 2022][research_chi_chu_2022]\] \[[Cossar et al 1980][research_cossar_moffatt_1980]\] \[[Cumpsty and Greitzer 1982][research_cumpsty_greitzer_1982]\] \[[Daniele and Teren 1975][research_daniele_teren_1975]\] \[[Daniele and Teren 1975][research_danielecj_terenf_1975]\] \[[Day et al 1978][research_day_greitzer_1978]\] \[[Day et al 1978][research_day_greitzer_1978_b]\] \[[Dean and Young 1977][research_dean_young_1977]\] \[[Dehner et al 2021][research_dehner_selamet_2021]\] \[[Ding et al 2024][research_ding_chen_2024]\] \[[Discussion on Anti-surge Control System of Centrifugal Compressor 2021][research_discussion_on_2021_b]\] \[[Discussion on Control Points of Surge and Anti-surge of Centrifugal Compressor 2021][research_discussion_on_2021]\] \[[Discussion on the Anti-surge Control Method and Realization Path of Axial Flow Compressor 2021][research_discussion_on_2021_d]\] \[[Discussion on the Application of Anti-surge Intelligent Control for Centrifugal Compressor 2021][research_discussion_on_2021_c]\] \[[Dodds and Vahdati 2015][research_dodds_vahdati_2015]\] \[[Dodds and Vahdati 2015][research_dodds_vahdati_2015_b]\] \[[Dong et al 2025][research_dong_liu_2025]\] \[[Dong et al 2026][research_dong_wang_2026]\] \[[Du et al 2025][research_du_zhang_2025]\] \[[Dvirnyk et al 2019][research_dvirnyk_pavlenko_2019]\] \[[Effect of Different Radial Inclined Angles of Self-circulation Casing Treatment on the Transonic Axial Flow Compressor Performance 2023][research_effect_of_2023_b]\] \[[Emmons et al 1955][research_emmons_pearson_1955]\] \[[Emmons et al 1955][research_emmons_pearson_1955_b]\] \[[Faltin and Beneda 2023][research_faltin_beneda_2023]\] \[[Fang et al 2023][research_fang_sun_2023_b]\] \[[Fu et al 2021][research_fu_fu_2021]\] \[[Fu et al 2021][research_fu_fu_2021_b]\] \[[Furukawa et al 2015][research_furukawa_yamada_2015]\] \[[Galindo et al 2022][research_galindo_climent_2022]\] \[[Gao et al 2015][research_gao_li_2015]\] \[[Gao et al 2017][research_gao_liu_2017]\] \[[Gray 1969][research_gray_1969]\] \[[Greitzer 1976][research_greitzer_1976]\] \[[Greitzer 1976][research_greitzer_1976_b]\] \[[Greitzer 1976][research_greitzer_1976_c]\] \[[Greitzer 1980][research_greitzer_1980]\] \[[Grimshaw et al 2025][research_grimshaw_pullan_2025]\] \[[Guan et al 2019][research_guan_zhou_2019]\] \[[Guo 2023][research_guo_2023]\] \[[Guo et al 2022][research_guo_gao_2022]\] \[[Guo et al 2022][research_guo_mao_2022]\] \[[Guo et al 2025][research_guo_liu_2025]\] \[[Güllü and Aran 2023][research_gullu_aran_2023]\] \[[Günaydın and Doğu 2025][research_gunaydin_dogu_2025]\] \[[Hah 2018][research_hah_2018]\] \[[Hah 2022][research_hah_2022]\] \[[Hamaguchi et al 2020][research_hamaguchi_sakata_2020]\] \[[Hansen et al 1981][research_hansen_jorgensen_1981]\] \[[Harman 1978][research_harman_1978]\] \[[Hawthorne et al 1955][research_hawthorne_wood_1955]\] \[[Hickman and Morris 2017][research_hickman_morris_2017]\] \[[Hosseindokht et al 2026][research_hosseindokht_matas_2026]\] \[[Huang et al 2019][research_huang_zhang_2019]\] \[[Huppert 1955][research_huppert_1955]\] \[[Huppert and Benser 1953][research_huppert_benser_1953]\] \[[Imani et al 2017][research_imani_jahedmotlagh_2017]\] \[[Imani et al 2018][research_imani_malekizade_2018]\] \[[Ji et al 2022][research_ji_hu_2022]\] \[[Jia et al 2024][research_jia_chen_2024]\] \[[Ka 2018][research_ka_2018]\] \[[Kawase and Rona 2019][research_kawase_rona_2019]\] \[[Kawase and Rona 2019][research_kawase_rona_2019_b]\] \[[Khaleghi 2015][research_khaleghi_2015]\] \[[Kim et al 2022][research_kim_choi_2022]\] \[[Kim et al 2026][research_kim_kim_2026]\] \[[Kiss and Spakovszky 2018][research_kiss_spakovszky_2018]\] \[[Kolnsberg 1979][research_kolnsberg_1979]\] \[[Kosuge et al 1982][research_kosuge_ito_1982]\] \[[Koyyalamudi and Nagpurwala 2016][research_koyyalamudi_nagpurwala_2016]\] \[[Laderman 2021][research_laderman_2021]\] \[[Li et al 2015][research_li_xu_2015]\] \[[Li et al 2019][research_li_du_2019]\] \[[Li et al 2021][research_li_zheng_2021]\] \[[Li et al 2022][research_li_dong_2022]\] \[[Li et al 2022][research_li_liu_2022]\] \[[Li et al 2023][research_li_zheng_2023]\] \[[Li et al 2024][research_li_chu_2024]\] \[[Lin et al 2022][research_lin_bai_2022]\] \[[Liu et al 2016][research_liu_li_2016]\] \[[Liu et al 2024][research_liu_chu_2024]\] \[[Liu et al 2025][research_liu_chu_2025]\] \[[Lou et al 2022][research_lou_harrison_2022]\] \[[Ludwig 1979][research_ludwig_1979]\] \[[Mao and Liu 2016][research_mao_liu_2016]\] \[[Mao et al 2017][research_mao_liu_2017]\] \[[Margalida et al 2020][research_margalida_joseph_2020]\] \[[Marshall 1973][research_marshall_1973]\] \[[Marty et al 2022][research_marty_castillon_2022]\] \[[Mays 1971][research_mays_1971]\] \[[McQueen 1976][research_mcqueen_1976]\] \[[Mechanism of Stability Enhancement with Shallow ‎Reversed Slot-Type Casing Treatment in a Transonic ‎Compressor 2021][research_mechanism_of_2021]\] \[[Mechanism study on the effect of self-circulating casing treatment with different circumferential coverage ratios on the axial compressor stability 2023][research_mechanism_study_2023]\] \[[Mikhailov et al 2017][research_mikhailov_mikhailova_2017]\] \[[Miura et al 2021][research_miura_yamashita_2021]\] \[[Molana et al 2020][research_molana_khodaparast_2020]\] \[[Moru et al 2022][research_moru_bo_2022]\] \[[Neverlien et al 2020][research_neverlien_moe_2020]\] \[[Ohyama 1978][research_ohyama_1978]\] \[[Pakle and Jiang 2018][research_pakle_jiang_2018]\] \[[Paraguassu 2015][research_paraguassu_2015]\] \[[Patil 2018][research_patil_2018]\] \[[Peacock 1978][research_peacock_1978]\] \[[Prince 1976][research_prince_1976]\] \[[Qiao et al 2026][research_qiao_chu_2026]\] \[[Quan et al 2024][research_quan_sun_2024]\] \[[Rains 1955][research_rains_1955]\] \[[Righi et al 2018][research_righi_pachidis_2018]\] \[[Sakata and Ohta 2017][research_sakata_ohta_2017]\] \[[Schaffrath et al 2025][research_schaffrath_nicke_2025]\] \[[Semlitsch and Mihăescu 2016][research_semlitsch_mihaescu_2016]\] \[[Shahin et al 2016][research_shahin_alqaradawi_2016]\] \[[Shahriyari et al 2024][research_shahriyari_firouzabadi_2024]\] \[[Sheng et al 2020][research_sheng_chen_2020]\] \[[Sheng et al 2023][research_sheng_chen_2023]\] \[[Shiriaev et al 2026][research_shiriaev_freidovich_2026]\] \[[Song et al 2019][research_song_zhang_2019]\] \[[Sonoda et al 2009][research_sonoda_olhofer_2009]\] \[[Sovran 1959][research_sovran_1959]\] \[[Starken and Lichtfuss 1970][research_starken_lichtfuss_1970]\] \[[Stenning 1980][research_stenning_1980_b]\] \[[Strub and Suter 1965][research_strub_suter_1965]\] \[[Sun et al 2015][research_sun_nie_2015]\] \[[Sun et al 2021][research_sun_gu_2021]\] \[[Sun et al 2021][research_sun_li_2021]\] \[[Sun et al 2021][research_sun_li_2021_b]\] \[[Sun et al 2024][research_sun_hu_2024]\] \[[Sun et al 2024][research_sun_yang_2024]\] \[[Sun et al 2025][research_sun_zheng_2025]\] \[[Sun et al 2026][research_sun_ding_2026]\] \[[Taghavi-Zenouz and Ababaf Behbaha 2017][research_taghavizenouz_ababafbehbaha_2017]\] \[[Tanaka and Murata 1975][research_tanaka_murata_1975]\] \[[Tanaka and Murata 1975][research_tanaka_murata_1975_b]\] \[[Tanaka and Murata 1975][research_tanaka_murata_1975_c]\] \[[Thapa et al 2025][research_thapa_li_2025]\] \[[The Reason and Strategy of Centrifugal Compressor Surge 2021][research_the_reason_2021]\] \[[Tondl 1979][research_tondl_1979]\] \[[Uddin and Gravdahl 2016][research_uddin_gravdahl_2016]\] \[[URANS Simulation of Self-Recirculation Casing Treatment in a Transonic Compressor 2024][research_urans_simulation_2024]\] \[[Valensi 1958][research_valensi_1958]\] \[[Venturelli and Benini 2016][research_venturelli_benini_2016]\] \[[Vu et al 2025][research_vu_nguyen_2025]\] \[[Wang et al 2020][research_wang_lu_2020]\] \[[Wang et al 2021][research_wang_hu_2021]\] \[[Wang et al 2022][research_wang_song_2022]\] \[[Wang et al 2024][research_wang_fang_2024]\] \[[Wang et al 2026][research_wang_zhang_2026]\] \[[Wasserbauer et al 1985][research_wasserbauerjf_neumannhe_1985]\] \[[Wu et al 2025][research_wu_cao_2025]\] \[[Xie and Marrani 2021][research_xie_marrani_2021]\] \[[Xinqian and Anxiong 2015][research_xinqian_anxiong_2015]\] \[[Xue et al 2024][research_xue_wang_2024]\] \[[Yang et al 2022][research_yang_wu_2022]\] \[[Yaylak et al 2026][research_yaylak_pinarbasi_2026]\] \[[Yi and Sun 2024][research_yi_sun_2024]\] \[[Zhang and Malekgoudarzi 2020][research_zhang_malekgoudarzi_2020]\] \[[Zhang and Wang 2022][research_zhang_wang_2022]\] \[[Zhang and Wu 2026][research_zhang_wu_2026]\] \[[Zhang et al 2016][research_zhang_yu_2016]\] \[[Zhang et al 2021][research_zhang_du_2021]\] \[[Zhang et al 2022][research_zhang_lu_2022]\] \[[Zhang et al 2024][research_zhang_an_2024]\] \[[Zhang et al 2024][research_zhang_zhang_2024_b]\] \[[Zhang et al 2025][research_zhang_yang_2025]\] \[[Zhang et al 2026][research_zhang_bo_2026]\] \[[Zhao et al 2019][research_zhao_zhou_2019]\] \[[Zhao et al 2025][research_zhao_li_2025]\] \[[Zhu and Yang 2020][research_zhu_yang_2020]\]

### Wings, aspect ratio and vortex flows

**The planform the Lancer inherited and changed.** Aspect ratio, downwash, tip and leading-edge vortices, delta and low aspect ratio wings, and the lifting-surface theory behind the induced term of the drag polar.

**166 records.** \[[2024][research_anon_2024]\] \[[Abdolahipour et al 2022][research_abdolahipour_mani_2022]\] \[[Abdolahipour et al 2022][research_abdolahipour_mani_2022_b]\] \[[Abdul-Kaiyoom et al 2025][research_abdulkaiyoom_yildirim_2025]\] \[[Aleisa et al 2023][research_aleisa_kontis_2023]\] \[[Anderson 1947][research_andersonadriene_1947]\] \[[Aoyagi and Hickey 1959][research_aoyagikiyoshi_hickeydavidh_1959]\] \[[Axelson and Crown 1948][research_axelsonjohna_crownjconrad_1948]\] \[[Banks and Paulson 1987][research_banksdanielw_paulsonjohnwjr_1987]\] \[[Bauer and McMillin 1988][research_bauerstevenxs_mcmillinsnaomi_1988]\] \[[Benaouali and Kachel 2019][research_benaouali_kachel_2019]\] \[[Bertram and Ulmann 1953][research_bertrammh_ulmannef_1953]\] \[[Bilanin and Donaldson 1975][research_bilanin_donaldson_1975]\] \[[Bird et al 1952][research_birdjohnd_lichtensteinjacobh_1952]\] \[[Biriukov 1959][research_biriukov_1959]\] \[[Bowers 1981][research_bowers_1981]\] \[[Brown 1959][research_brownstuartc_1959]\] \[[Buchholz 1992][research_buchholzmarkd_1992]\] \[[Buchholz and Tso 1993][research_buchholzmarkd_tsojin_1993]\] \[[Butter and Hancock 1971][research_butter_hancock_1971]\] \[[Buzica and Breitsamter 2020][research_buzica_breitsamter_2020]\] \[[Campbell 1976][research_campbell_1976]\] \[[Carreyette 1950][research_carreyette_1950]\] \[[Chen et al 2025][research_chen_yang_2025]\] \[[Clark and Richie 1977][research_clarkle_richiecb_1977]\] \[[Coe and Kulla 1974][research_coe_kulla_1974]\] \[[Coe 1976][research_coepljr_1976]\] \[[Cole 1980][research_colejb_1980]\] \[[Corcione et al 2023][research_corcione_bonavolonta_2023]\] \[[Crane 1948][research_craneharoldl_1948]\] \[[Crane and Beckhardt 1948][research_craneharoldl_beckhardtarnoldr_1948]\] \[[Davis 1952][research_davis_1952]\] \[[Davis 1973][research_davis_1973]\] \[[Davis 1973][research_davis_1973_c]\] \[[Davis 1973][research_davis_1973_d]\] \[[Deitchman 1954][research_deitchman_1954]\] \[[Demir et al 2023][research_demir_gorguluarslan_2023]\] \[[Deyoung 1950][research_deyoungjohn_1950]\] \[[Doggett and Soistmann 1989][research_doggettrobertvjr_soistmanndavidl_1989]\] \[[Dong et al 2020][research_dong_choi_2020]\] \[[Dong et al 2022][research_dong_choi_2022]\] \[[Dowell and Ventres 1970][research_dowell_ventres_1970]\] \[[Epstein 1954][research_epstein_1954]\] \[[Figge 1973][research_figge_1973]\] \[[Fisher and Williams 1958][research_fisherlewisr_williamsjamesl_1958]\] \[[Foster and Fitzpatrick 1948][research_fostergeraldv_fitzpatrickjamese_1948]\] \[[François et al 2021][research_francois_probst_2021]\] \[[Fuller 1967][research_fullerde_1967]\] \[[Ghaffari 2005][research_ghaffarifarhad_2005]\] \[[Ghee et al 1999][research_ghee_gonzalez_1999]\] \[[Golubkin 1980][research_golubkin_1980_b]\] \[[Griffin et al 1958][research_griffinroynjr_holzhausercurta_1958]\] \[[Hanazaki and Yamazaki 2024][research_hanazaki_yamazaki_2024]\] \[[Hancock 1960][research_hancock_1960]\] \[[Harold and Haefeli 1950][research_harold_haefeli_1950]\] \[[Hayes and Sleeman 1959][research_hayeswcjr_sleemanwcjr_1959]\] \[[He and Zhang 2025][research_he_zhang_2025]\] \[[Helmbold 1958][research_helmbold_1958]\] \[[Hobbs et al 1996][research_hobbs_spaid_1996]\] \[[Hoffler et al 1986][research_hofflerkd_raodm_1986]\] \[[Hopkins 1975][research_hopkinsej_1975]\] \[[Hunn 1954][research_hunn_1954]\] \[[Hwang et al 1980][research_hwang_johnson_1980]\] \[[Hövelmann and Breitsamter 2015][research_hovelmann_breitsamter_2015]\] \[[Hövelmann et al 2016][research_hovelmann_grawunder_2016]\] \[[Ichikawa et al 2021][research_ichikawa_koike_2021]\] \[[Jaquet 1951][research_jaquetbyronm_1951]\] \[[Jenkins and Kuhl 1977][research_jenkinsjeraldm_kuhlalberte_1977]\] \[[Jones et al 1947][research_jonesarthurl_flanaganmildredg_1947]\] \[[Jones and Unangst 1963][research_jonesgwjr_unangstjr_1963]\] \[[Kelley and Tolhurst 1955][research_kelleymarkw_tolhurstwilliamhjr_1955]\] \[[Kelly et al 1958][research_kellymarkw_andersonsethb_1958]\] \[[Kholyavko 1971][research_kholyavko_1971]\] \[[Kida and Miyai 1978][research_kida_miyai_1978]\] \[[Kinard et al 1995][research_kinardtima_harrisbrendaw_1995]\] \[[Kishi et al 2022][research_kishi_kanazaki_2022]\] \[[Klein 1999][research_kleinvladislav_1999]\] \[[Kopzon 1958][research_kopzon_1958]\] \[[Lai and Kamaruddin 2018][research_lai_kamaruddin_2018]\] \[[Lamar 1986][research_lamarje_1986]\] \[[Lamar 1987][research_lamarjohne_1987]\] \[[Lampropoulos and Sarris 2025][research_lampropoulos_sarris_2025]\] \[[Lapin et al 1952][research_lapin_crookshanks_1952]\] \[[Larrabee 1975][research_larrabeeee_1975]\] \[[Lawrence 1953][research_lawrence_1953]\] \[[Lee and Kim 2024][research_lee_kim_2024]\] \[[Lee and Ko 2018][research_lee_ko_2018]\] \[[Lemay et al 1988][research_lemaysp_batillsm_1988]\] \[[Leslie 1952][research_leslie_1952]\] \[[Lichtenstein 1952][research_lichtensteinjacobh_1952]\] \[[Lin et al 2026][research_lin_zong_2026]\] \[[Lockwood 1966][research_lockwoodve_1966]\] \[[Lourenco et al 1996][research_lourenco_shih_1996]\] \[[Maki 1959][research_makiralphl_1959]\] \[[Malicki et al 2023][research_malicki_malecha_2023]\] \[[Mamonova et al 2019][research_mamonova_soudakov_2019]\] \[[McCormick 1959][research_mccormick_1959]\] \[[McLemore 1958][research_mclemorehclyde_1958]\] \[[McLemore and Peterson 1960][research_mclemorehclyde_petersonjohnbjr_1960]\] \[[Miller 1983][research_miller_1983]\] \[[Miller 1986][research_miller_1986]\] \[[Mitsuyasu 1956][research_mitsuyasu_1956]\] \[[Morton 1956][research_morton_1956]\] \[[Muchmore 1988][research_muchmorecbjr_1988]\] \[[Murphy and Klein 2006][research_murphypatrickc_kleinvladislav_2006]\] \[[Nagler 2022][research_nagler_2022]\] \[[Ness 1971][research_ness_1971]\] \[[Newsome and Thomas 1986][research_newsomerw_thomasjl_1986]\] \[[Nicholas et al 1984][research_nicholas_naville_1984]\] \[[Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952_b]\] \[[Northrop Aircraft Inc Hawthorne Ca 1953][research_northropaircraftinchawthorneca_1953]\] \[[O'Kelly 1954][research_okelly_1954]\] \[[Ogawa and Takeda 2015][research_ogawa_takeda_2015]\] \[[Raj et al 2003][research_praj_fghaffari_2003]\] \[[Paziresh et al 2017][research_paziresh_nikseresht_2017]\] \[[Penland et al 1975][research_penlandja_fournierrh_1975]\] \[[Penland et al 1978][research_penlandja_creeltrjr_1978]\] \[[Peterson and Menees 1959][research_petersonvictorl_meneesgenep_1959]\] \[[Pfnür and Breitsamter 2019][research_pfnur_breitsamter_2019]\] \[[Polhamus 1966][research_polhamusec_1966]\] \[[Queijo and Wolhart 1951][research_queijomj_wolhartwalterd_1951]\] \[[Queijo et al 1954][research_queijomj_jaquetbyronm_1954]\] \[[Quigley et al 1960][research_quigleyherveyc_andersonsethb_1960]\] \[[Ramakrishna et al 2019][research_ramakrishna_senthilkumar_2019]\] \[[Rebuffet and Poisson-Quinton 1952][research_rebuffetpierre_poissonquintonph_1952]\] \[[Report no. 609, Experimental investigation of wind-tunnel interference on the downwash behind an airfoil 1937][research_report_no_1937]\] \[[Report No. 648, Design charts for predicting downwash angles and wake characteritics behind plain and flapped wings 1939][research_report_no_1939]\] \[[Reykers and Fonck 2019][research_reykers_fonck_2019]\] \[[Ribner 1960][research_ribner_1960]\] \[[Roberts 1965][research_roberts_1965]\] \[[Rockwell 2001][research_rockwell_2001]\] \[[Roy Salam and Bil 2016][research_roysalam_bil_2016]\] \[[Rudolph 1997][research_rudolphpeterkc_1997]\] \[[Said et al 2018][research_said_mat_2018]\] \[[Sakata and Davis 1977][research_sakataif_davisgw_1977]\] \[[Sakata et al 1975][research_sakataif_davisgw_1975]\] \[[Schuldenfrei et al 1947][research_schuldenfreimarvin_comisarowpaul_1947]\] \[[Schulderfrei et al 1951][research_schulderfreimarvin_comisarowpaul_1951]\] \[[Shen and Wen 2018][research_shen_wen_2018]\] \[[Shindo and Joppa 1980][research_shindos_jopparg_1980]\] \[[Silverstein and White 1937][research_silversteinabe_whitejamesa_1937]\] \[[Skoog 1951][research_skoogrichardb_1951]\] \[[Skow et al 1982][research_skow_moore_1982]\] \[[Sogukpinar 2018][research_sogukpinar_2018]\] \[[Spencer 1961][research_spencerbernardjr_1961]\] \[[Spooner and Martina 1948][research_spoonerstanleyh_martinaalbertp_1948]\] \[[Spreiter and Sacks 1951][research_spreiter_sacks_1951]\] \[[Sugiyama 1971][research_sugiyama_1971]\] \[[Sugiyama 1971][research_sugiyama_1971_b]\] \[[Surwase and Kumar 2025][research_surwase_kumar_2025]\] \[[Sutton 1959][research_suttonfredb_1959]\] \[[Torenbeek 1971][research_torenbeek_1971]\] \[[Van Dommelen 1995][research_vandommelen_1995]\] \[[Verma and Kulkarni 2024][research_verma_kulkarni_2024]\] \[[Verma and Manisankar 2025][research_verma_manisankar_2025]\] \[[Vidal 1962][research_vidal_1962]\] \[[Wabick et al 2023][research_wabick_johnson_2023]\] \[[Walker and Berggren 1948][research_walkerharoldj_berggrenroberte_1948]\] \[[Wentz 1987][research_wentz_1987]\] \[[Wood and Miller 1985][research_woodrm_millerds_1985]\] \[[Wood et al 1983][research_woodrm_millerds_1983]\] \[[Woodward 1956][research_woodward_1956]\] \[[Wright et al 1978][research_wright_bruckman_1978]\] \[[Yan et al 2016][research_yan_chen_2016]\] \[[Yang et al 2026][research_yang_li_2026]\] \[[Zimmerman 1935][research_zimmermanch_1935]\]

### Turbofans, turbojets and installed thrust

**The engine the designation was requested to test.** Turbofan and turbojet cycles, afterburning and variable-cycle engines, nozzles, engine test and control, and the installed thrust that the ram drag argument turns on.

**146 records.** \[[Jain 2025][research_ajain_2025]\] \[[A.K. and P.S. 2018][research_ak_ps_2018]\] \[[Abdulhamitbilal et al 2021][research_abdulhamitbilal_sal_2021]\] \[[Anatomy of a turbofan engine 1970][research_anatomy_of_1970]\] \[[Armstrong et al 1980][research_armstrong_palladino_1980]\] \[[Ashry et al 2019][research_ashry_kamel_2019]\] \[[Ashwood 1973][research_ashwood_1973]\] \[[Auman 1993][research_auman_1993]\] \[[Babu 2021][research_babu_2021]\] \[[Babu 2021][research_babu_2021_b]\] \[[Baerst and Hughes 1978][research_baerst_hughes_1978]\] \[[Bagby and Andersen 1966][research_bagby_andersen_1966]\] \[[Baidya et al 2018][research_baidya_pesyridis_2018]\] \[[Balli and Caliskan 2021][research_balli_caliskan_2021]\] \[[Banks et al 1981][research_banks_quinto_1981]\] \[[Bayati and Williston 1977][research_bayati_williston_1977]\] \[[Beale and Miller 1975][research_beale_miller_1975]\] \[[Benson 1997][research_bensonthomasj_1997]\] \[[Berezovsky 2018][research_berezovsky_2018]\] \[[Bezborodova and Filinov 2021][research_bezborodova_filinov_2021]\] \[[Birch et al 1978][research_birch_paynter_1978]\] \[[Boytos 1969][research_boytos_1969]\] \[[Branstetter et al 1971][research_branstetterjr_juhaszaj_1971]\] \[[Breaks 1973][research_breaks_1973]\] \[[Briones and Rankin 2024][research_briones_rankin_2024]\] \[[Bristol Siddeley Viper Mark 1963][research_bristol_siddeley_1963]\] \[[Brodsky 1970][research_brodsky_1970]\] \[[Brodzik 2024][research_brodzik_2024_b]\] \[[Burns and Kirchgessner 1987][research_burns_kirchgessner_1987]\] \[[Capello et al 2019][research_capello_ferrero_2019]\] \[[Capone and Reubush 1983][research_caponefj_reubushde_1983]\] \[[Castner et al 2017][research_castner_zaman_2017]\] \[[Castor 1983][research_castor_1983]\] \[[Chaney 1999][research_chaney_1999]\] \[[Chapman 1979][research_chapman_1979]\] \[[Chen et al 2021][research_chen_chen_2021]\] \[[Child and Henderson 1978][research_childrd_hendersonwp_1978]\] \[[Coalson 1968][research_coalson_1968]\] \[[Coalson and Csavina 1976][research_coalson_csavina_1976]\] \[[Cowles 1981][research_cowles_1981]\] \[[Crown 1950][research_crown_1950]\] \[[da Fonseca Filho et al 2019][research_dafonsecafilho_gamaribeiro_2019]\] \[[Dai et al 2023][research_dai_boughazi_2023]\] \[[Davidson 1964][research_davidson_1964]\] \[[Development Testing of the RB.211 Turbofan Engine 1970][research_development_testing_1970]\] \[[Di̇şli̇taş and Albayrak Çeper 2021][research_dislitas_albayrakceper_2021]\] \[[Drewes 1987][research_drewes_1987]\] \[[Due 1987][research_due_1987]\] \[[Dugan 1972][research_duganjfjr_1972]\] \[[Dugas 1968][research_dugas_1968]\] \[[Egan and Shadowen 1979][research_egan_shadowen_1979]\] \[[El-Sayed 2026][research_elsayed_2026]\] \[[Evans and Chamblee 1966][research_evans_chamblee_1966]\] \[[Fett 1971][research_fett_1971]\] \[[Franciscus 1987][research_franciscusleoc_1987]\] \[[Gabriel et al 1953][research_gabrieldavids_krebsrichardp_1953]\] \[[Guo et al 2024][research_guo_zhang_2024]\] \[[Gürbüz and Acarer 2022][research_gurbuz_acarer_2022]\] \[[Hartmann 1968][research_hartmann_1968]\] \[[Heltsley and Crosswy 1983][research_heltsley_crosswy_1983]\] \[[Herrick 1986][research_herrick_1986]\] \[[Hurley 1951][research_hurley_1951]\] \[[Hutchinson et al 2021][research_hutchinson_lawrence_2021]\] \[[Jakubowski 2019][research_jakubowski_2019]\] \[[Jiali and Jihong 2015][research_jiali_jihong_2015]\] \[[Kalkan 2024][research_kalkan_2024]\] \[[Karol and Hatch 1969][research_karol_hatch_1969]\] \[[Kast 1980][research_kast_1980]\] \[[Katz 1971][research_katz_1971]\] \[[Kbab et al 2023][research_kbab_haif_2023]\] \[[Kim et al 2015][research_kim_kim_2015_b]\] \[[Klein and Abeykoon 2015][research_klein_abeykoon_2015]\] \[[Krebs 1976][research_krebs_1976]\] \[[Krenkel and Salzman 1968][research_krenkel_salzman_1968]\] \[[L'Ecuyer et al 1971][research_lecuyer_morrison_1971]\] \[[Lambert and Mizukami 1999][research_lamberthh_mizukamim_1999]\] \[[Larson 1960][research_larson_1960_d]\] \[[Lewis 1976][research_lewis_1976]\] \[[Li et al 2019][research_li_soskin_2019]\] \[[Li et al 2024][research_li_xia_2024]\] \[[Liew et al 2005][research_liewkh_uripe_2005]\] \[[Liu and Sirignano 2000][research_liu_sirignano_2000]\] \[[Lucas 1978][research_lucas_1978]\] \[[Ma et al 2025][research_ma_yang_2025]\] \[[MacInnis 1994][research_macinnis_1994]\] \[[Magrini and Benini 2023][research_magrini_benini_2023]\] \[[Mauch et al 1980][research_mauch_oldakowski_1980]\] \[[McAulay and Abdelwahab 1972][research_mcaulayje_abdelwahabm_1972]\] \[[McGuigan 1970][research_mcguigan_1970]\] \[[Menon et al 2023][research_menon_sanjayshivam_2023]\] \[[Mikhail 1979][research_mikhail_1979]\] \[[Mixed Flow Turbofan Engine 2018][research_mixed_flow_2018]\] \[[Mock 1951][research_mock_1951]\] \[[Morris et al 1976][research_morris_nelms_1976]\] \[[Nageswara Rao and Kushari 2020][research_nageswararao_kushari_2020]\] \[[Neitzel and Hemsworth 1966][research_neitzel_hemsworth_1966]\] \[[Niknamian 2019][research_niknamian_2019]\] \[[Okelah 1985][research_okelah_1985]\] \[[Panzeri et al 2018][research_panzeri_savelyev_2018]\] \[[Parisen et al 1948][research_parisenrichardb_armstrongjohnc_1948]\] \[[Parker 1991][research_parker_1991]\] \[[Patel and Chudoba 2026][research_patel_chudoba_2026]\] \[[Piccirillo et al 2024][research_piccirillo_gregorio_2024]\] \[[Pismennyi][research_pismennyi]\] \[[Prasad and Rivera 1996][research_prasad_rivera_1996]\] \[[Presz et al 1971][research_presz_konarski_1971]\] \[[Purser and Spear 1947][research_purserpaule_spearmargaretf_1947]\] \[[Rajagopalan and Siddiqi 1985][research_rajagopalan_siddiqi_1985]\] \[[Rakipoğlu and Avcı 2026][research_rakipoglu_avci_2026]\] \[[Ramjet supersonic “flight tests” 1958][research_ramjet_supersonic_1958]\] \[[Resta et al 2021][research_resta_marsilio_2021]\] \[[Robins et al 1985][research_robinsaw_beissnerfljr_1985]\] \[[Rosell][research_rosell]\] \[[Rosen 2001][research_rosen_2001]\] \[[Roth et al 2005][research_roth_doel_2005]\] \[[Rudnitski][research_rudnitski]\] \[[Schweiger 1987][research_schweiger_1987]\] \[[Semlitsch and Mihăescu 2021][research_semlitsch_mihaescu_2021]\] \[[Shariatzadeh et al 2015][research_shariatzadeh_abrishamkar_2015]\] \[[Shoshany‐Tavory et al 2023][research_shoshanytavory_peleg_2023]\] \[[Shufan et al 2018][research_shufan_heng_2018]\] \[[Stephenson 1953][research_stephenson_1953]\] \[[Suchocki et al 2015][research_suchocki_lampart_2015]\] \[[Sun et al 2015][research_sun_miao_2015]\] \[[Takahashi 2017][research_takahashi_2017]\] \[[Tate and Gillard 1975][research_tate_gillard_1975]\] \[[Taylor 1991][research_taylorjohng_1991]\] \[[The Fiat G80 Turbojet Fighter‐Trainer 1952][research_the_fiat_1952]\] \[[The Hawker P1127 vectored 1990][research_the_hawker_1990]\] \[[The Rolls‐Royce RB.211 Three Shaft Turbofan 1968][research_the_rollsroyce_1968]\] \[[The Rolls‐Royce Spey Junior Turbofan Engine 1967][research_the_rollsroyce_1967]\] \[[THRUST VECTORING OF A SUPERSONIC RECTANGULAR NOZZLE BY USING DIFFERENT PLATE EXTENSIONS 2020][research_thrust_vectoring_2020]\] \[[Trefny and Benson 1995][research_trefnycj_bensontj_1995]\] \[[Tudosie 2024][research_tudosie_2024]\] \[[Watson 1953][research_watsonearlc_1953]\] \[[Werner and Wolter 2010][research_wernerrogera_wolterjohnd_2010]\] \[[White and Wills 1972][research_white_wills_1972]\] \[[Wilde and Pickerell 1968][research_wilde_pickerell_1968]\] \[[Yahiaoui 2024][research_yahiaoui_2024]\] \[[Yalcin 2017][research_yalcin_2017]\] \[[Yang and Yu 2026][research_yang_yu_2026]\] \[[Yao et al 2022][research_yao_zhang_2022]\] \[[Yonke et al 1985][research_yonke_terrell_1985]\] \[[Zahir et al 2023][research_zahir_aamer_2023]\] \[[Zebbiche and Youbi 2023][research_zebbiche_youbi_2023]\] \[[Zhang et al 2025][research_zhang_ji_2025]\]

### Air combat, agility and aircraft performance

**The case the Lancer was sold on.** Energy manoeuvrability and specific excess power, turn performance, climb and minimum-time paths, and agility metrics and requirements.

**11 titles in the survey name energy manoeuvrability or specific excess power, from 1972 to 2026.** The measure the competition argued over is still the one in which aircraft performance is presented.

**114 records.** \[[Aircraft Performance 2010][research_aircraft_performance_2010]\] \[[Aircraft Steady Level Turning 2011][research_aircraft_steady_2011_c]\] \[[Aircraft Steady Turning Flight 2011][research_aircraft_steady_2011_d]\] \[[Aircraft, Basic Forces, and 1995][research_aircraft_basic_1995]\] \[[Alexander et al 1992][research_alexander_harris_1992]\] \[[Ali et al 2017][research_ali_asghar_2017]\] \[[Anderson 1989][research_anderson_1989]\] \[[Anderson et al 1973][research_anderson_berger_1973]\] \[[Anderson and Bray 1951][research_andersonsethb_brayrichards_1951]\] \[[Anderson and Bray 1955][research_andersonsethb_brayrichards_1955]\] \[[Andrews 1969][research_andrews_1969]\] \[[Atesoglu and Özgören 2006][research_atesoglu_ozgoren_2006]\] \[[Atesoglu and Özgören 2007][research_atesoglu_ozgoren_2007]\] \[[Beaufrere 1988][research_beaufrere_1988]\] \[[Beck and Cord 1995][research_beck_cord_1995]\] \[[Blake et al 1990][research_blake_leggett_1990]\] \[[Blank and Shinar 1982][research_blank_shinar_1982]\] \[[Caddy and Arnold 1988][research_caddy_arnold_1988]\] \[[Canard-Leading Edge Flap Scheduling 2007][research_canard_leading_edge_2007]\] \[[Capone 1979][research_capone_1979]\] \[[Chou][research_chou]\] \[[Coordinated Turning Flights of 1995][research_coordinated_turning_1995]\] \[[Cord 1989][research_cord_1989]\] \[[Corner 1940][research_corner_1940]\] \[[Crowe 1936][research_crowe_1936]\] \[[Degree Turning Performance][research_degree_turning]\] \[[Erickson and Campbell 1977][research_erickson_campbell_1977]\] \[[Erickson and Campbell 1977][research_erickson_campbell_1977_b]\] \[[Foss 1981][research_foss_1981]\] \[[Foss 1984][research_foss_1984]\] \[[Gedeon and Takahashi 2014][research_gedeon_takahashi_2014]\] \[[Gloss 1974][research_glossbb_1974]\] \[[Guang et al 2014][research_guang_ping_2014]\] \[[Guang et al 2015][research_guang_deming_2015]\] \[[Herbst and Krogull 1973][research_herbst_krogull_1973]\] \[[Hill and Bowles 1976][research_hillgc_bowlesjv_1976]\] \[[Hitzel and Osterhuber 2018][research_hitzel_osterhuber_2018]\] \[[Hoffman and Stalford 1991][research_hoffman_stalford_1991]\] \[[Hom et al 1983][research_hom_morris_1983]\] \[[Iliff 1977][research_iliff_1977]\] \[[Irwanto 2017][research_irwanto_2017]\] \[[Jeans and Tribble 1979][research_jeans_tribble_1979]\] \[[Johnson 1972][research_johnson_1972]\] \[[Karabacak and Turan 2020][research_karabacak_turan_2020]\] \[[Karniadakis 2004][research_karniadakis_2004]\] \[[Kelley 1975][research_kelley_1975]\] \[[Kelley 1975][research_kelley_1975_b]\] \[[Khalid 2025][research_khalid_2025]\] \[[Kigotho et al 2022][research_kigotho_bodylski_2022]\] \[[Kish et al 2019][research_kish_wilde_2019]\] \[[Kostin and Zhuravskiy 2023][research_kostin_zhuravskiy_2023]\] \[[Krupa 2019][research_krupa_2019]\] \[[Kutschera and Render 1999][research_kutschera_render_1999]\] \[[Kutschera and Render 2003][research_kutschera_render_2003]\] \[[Langan and Samuels 1995][research_langan_samuels_1995]\] \[[Large 1981][research_large_1981]\] \[[Levin 1997][research_levin_1997]\] \[[Lin 1982][research_lin_1982]\] \[[Lin 1982][research_lin_1982_b]\] \[[Loh and Lusty 1974][research_loh_lusty_1974]\] \[[Maitra 2010][research_maitra_2010]\] \[[Mancini and Vos 2019][research_mancini_vos_2019]\] \[[Manolescu 1994][research_manolescu_1994]\] \[[Mason 1983][research_masonwh_1983]\] \[[Mason et al 1983][research_masonwh_siclarimj_1983]\] \[[Merritt et al 1985][research_merritt_cliff_1985]\] \[[Miele 1954][research_miele_1954]\] \[[Miele 1955][research_mieleangelo_1955]\] \[[Nelms and Bailey 1974][research_nelmswpjr_baileyro_1974]\] \[[Ngan and Biezad 1996][research_nganangelen_biezaddaniel_1996]\] \[[Olwi 1995][research_olwi_1995]\] \[[Oruc and Baklacioglu 2022][research_oruc_baklacioglu_2022]\] \[[Oruc and Baklacioglu 2023][research_oruc_baklacioglu_2023]\] \[[Papageorgiou et al 2018][research_papageorgiou_tarkian_2018]\] \[[Paranjape and Ananthkrishnan 2023][research_paranjape_ananthkrishnan_2023]\] \[[Parlier 1986][research_parlier_1986]\] \[[Pennington and Meintel 1980][research_penningtonje_meintelajjr_1980]\] \[[Rafiq and Qureshi 2022][research_rafiq_qureshi_2022]\] \[[Ransom 1983][research_ransom_1983]\] \[[Ray and Taylor 1965][research_rayej_taylorrt_1965]\] \[[Raymer 1991][research_raymer_1991]\] \[[Reinbold et al 2026][research_reinbold_breitsamter_2026]\] \[[Rodgers 1966][research_rodgers_1966]\] \[[Sadraey 2017][research_sadraey_2017]\] \[[Satyanarayana et al 1975][research_satyanarayana_prasad_1975]\] \[[Schneider 1990][research_schneideredwardt_1990]\] \[[Schrage 1990][research_schrage_1990]\] \[[Schuster 1995][research_schuster_1995]\] \[[Sederstrom et al 1973][research_sederstrom_zagalsky_1973]\] \[[Seginer and Salomon 1983][research_seginer_salomon_1983]\] \[[Silton et al 2014][research_silton_fresconi_2014]\] \[[Sivaramakrishnan 1981][research_sivaramakrishnan_1981]\] \[[Spearman and Sawyer 1977][research_spearmanml_sawyerwc_1977]\] \[[Srivastav and Ponnani 2011][research_srivastav_ponnani_2011]\] \[[Takahashi 2012][research_takahashi_2012]\] \[[Tamboli 1956][research_tamboli_1956]\] \[[Tamrat 1988][research_tamrat_1988]\] \[[Theodorsen 1959][research_theodorsen_1959]\] \[[Tritschler et al 2025][research_tritschler_juhasz_2025]\] \[[Turn Performance and Maneuver 2021][research_turn_performance_2021]\] \[[Turning Flight 1997][research_turning_flight_1997]\] \[[Turning Flights of Turbojet 1995][research_turning_flights_1995]\] \[[Turning performance 1992][research_turning_performance_1992]\] \[[Voß and Klimmek 2023][research_voss_klimmek_2023]\] \[[Wang et al 2017][research_wang_guo_2017]\] \[[Wang et al 2020][research_wang_wang_2020]\] \[[Wang et al 2021][research_wang_ma_2021]\] \[[Wang et al 2026][research_wang_song_2026]\] \[[Whittley 1952][research_whittley_1952]\] \[[Wilson et al 1993][research_wilson_riley_1993]\] \[[Wood and Livingston 1971][research_wood_livingston_1971]\] \[[Yajnik 1977][research_yajnik_1977]\] \[[Yan et al 2024][research_yan_chang_2024]\] \[[Yongxi Lyu et al 2016][research_yongxilyu_weiguozhang_2016]\]

### Aerodynamic heating, recovery temperature and thermal protection

**The structural half of the keystone, as heat.** Aerodynamic and kinetic heating, the recovery temperature and the adiabatic wall, transient skin temperature, and cooling and thermal protection.

**20 titles name the recovery temperature, the recovery factor or the adiabatic wall temperature.** The relation that puts the skin at 210.8 degrees Celsius is measured and settled, and a literature of measurements is the shape a settled subject takes.

**109 records.** \[[Afanas’ev et al 2019][research_afanasev_nikitin_2019]\] \[[Air Force Research Lab Edwards Afb Ca 2000][research_airforceresearchlabedwardsafbca_2000]\] \[[Back et al 1967][research_back_massier_1967]\] \[[Barone et al 2022][research_barone_nicholson_2022]\] \[[Baryshev et al 1972][research_baryshev_vinogradov_1972]\] \[[Bergstedt et al 1959][research_bergstedt_turner_1959]\] \[[Biswas et al 2026][research_biswas_michels_2026]\] \[[Brinich 1961][research_brinich_1961]\] \[[Cess 1964][research_cess_1964]\] \[[Chen and He 2025][research_chen_he_2025]\] \[[Chen et al 2021][research_chen_zhang_2021_b]\] \[[Chen et al 2024][research_chen_zhu_2024]\] \[[Chou and Smith 1974][research_chou_smith_1974]\] \[[Dai et al 2023][research_dai_zhao_2023]\] \[[Ding et al 2020][research_ding_wang_2020]\] \[[Duan et al 2026][research_duan_zhao_2026]\] \[[Evaluation of Various Flow Control Methods in Reducing Drag and Aerodynamic Heating on the Nose of Hypersonic Flying Objects 2024][research_evaluation_of_2024]\] \[[Feng et al 2020][research_feng_tao_2020]\] \[[Fischer and Norris 1949][research_fischer_norris_1949]\] \[[Flanagan 1992][research_flanaganmichaelj_1992]\] \[[Gadeev et al 2017][research_gadeev_demakov_2017]\] \[[Gliszczyński et al 2021][research_gliszczynski_czechowski_2021]\] \[[Gridnev 1991][research_gridnev_1991]\] \[[Gupta and Ramkumar 2015][research_gupta_ramkumar_2015]\] \[[Gözükara and Ceylan 2024][research_gozukara_ceylan_2024]\] \[[Hao et al 2024][research_hao_liu_2024]\] \[[Herwig 2000][research_herwig_2000]\] \[[Hodge et al 1985][research_hodge_taylor_1985]\] \[[Hodge et al 1986][research_hodge_taylor_1986]\] \[[Honeycutt 1970][research_honeycutt_1970]\] \[[Hongpeng and Weiqiang 2016][research_hongpeng_weiqiang_2016]\] \[[Horton 1954][research_horton_1954]\] \[[Hu et al 2023][research_hu_qu_2023]\] \[[Ivanov 2022][research_ivanov_2022]\] \[[Johnson and Adcock 1981][research_johnson_adcock_1981]\] \[[Karimi and Oboodi 2018][research_karimi_oboodi_2018]\] \[[Kaye and Yeh 1955][research_kaye_yeh_1955]\] \[[Kinsler 1958][research_kinslermartinr_1958]\] \[[Kurganov 2006][research_kurganov_2006]\] \[[Leadon and Scott 1956][research_leadon_scott_1956]\] \[[Leontiev et al 2017][research_leontiev_lushchik_2017]\] \[[Leontiev et al 2017][research_leontiev_popovich_2017]\] \[[Leontiev et al 2022][research_leontiev_lushchik_2022]\] \[[Li et al 2024][research_li_liu_2024]\] \[[Li et al 2026][research_li_zhao_2026]\] \[[Lin et al 2021][research_lin_liu_2021]\] \[[Liu and Cao 2017][research_liu_cao_2017]\] \[[Luce 1949][research_luce_jr_1949]\] \[[Maples 1979][research_maples_1979]\] \[[Mugalev et al 1985][research_mugalev_savushkina_1985]\] \[[Nagamatsu et al 1960][research_nagamatsu_workman_1960]\] \[[Negaard 1979][research_negaard_1979]\] \[[Ohwada et al 2019][research_ohwada_shimada_2019]\] \[[Pasiuk 1963][research_pasiuk_1963]\] \[[Peck et al 2020][research_peck_liu_2020]\] \[[Peng-ju et al 2015][research_pengju_liang_2015]\] \[[Persh 1955][research_persh_1955]\] \[[Pfyl and Presley 1961][research_pfyl_presley_1961]\] \[[Popovich et al 2014][research_popovich_kirill_2014]\] \[[Popovich et al 2021][research_popovich_kiselev_2021]\] \[[Powell and Glickstein 1988][research_powell_glickstein_1988]\] \[[Qu et al 2019][research_qu_kong_2019]\] \[[Rand 1963][research_rand_1963]\] \[[Reggiori 1972][research_reggiori_1972]\] \[[Ren et al 2021][research_ren_zhang_2021]\] \[[Rubio and Ballard 1967][research_rubio_ballard_1967]\] \[[Rumsey and Lee 1961][research_rumseycharlesb_leedorothyb_1961]\] \[[Schoeler 1987][research_schoeler_1987]\] \[[Shimada and Ohwada 2020][research_shimada_ohwada_2020]\] \[[Shiryaev and Serebryansky 2022][research_shiryaev_serebryansky_2022]\] \[[Shiryaev et al 2023][research_shiryaev_maysak_2023]\] \[[Si et al 2019][research_si_huang_2019]\] \[[Smith 1967][research_smith_1967]\] \[[Smith 2021][research_smith_2021]\] \[[Snodgrass 1955][research_snodgrass_1955]\] \[[Sreekumar et al 2025][research_sreekumar_vamsikrishna_2025]\] \[[Stephens 1959][research_stephensemilyw_1959]\] \[[Straight and Harrington 1973][research_straightdm_harringtonde_1973]\] \[[Sturek et al 1983][research_sturek_kayser_1983]\] \[[Sturek et al 1983][research_sturek_kayser_1983_b]\] \[[Sun and Zhu 2019][research_sun_zhu_2019]\] \[[Sun et al 2020][research_sun_yang_2020]\] \[[Taguchi et al 2017][research_taguchi_mori_2017]\] \[[Tang et al 2024][research_tang_xu_2024]\] \[[Tang et al 2025][research_tang_li_2025]\] \[[Tewfik and Giedt 1960][research_tewfik_giedt_1960]\] \[[Vitols et al 2026][research_vitols_threadgill_2026]\] \[[Walker 1955][research_walker_1955]\] \[[Wang et al 2023][research_wang_pan_2023]\] \[[Wang et al 2024][research_wang_pan_2024]\] \[[Wang et al 2024][research_wang_wang_2024]\] \[[Winkler 1954][research_winkler_1954]\] \[[Xie et al 2016][research_xie_zhang_2016]\] \[[Xie et al 2025][research_xie_ye_2025_b]\] \[[Xin-guo et al 2015][research_xinguo_xing_2015]\] \[[Yadav and Guven 2015][research_yadav_guven_2015]\] \[[Yang and Liu 2017][research_yang_liu_2017]\] \[[Yang et al 2021][research_yang_li_2021]\] \[[Yih et al 1952][research_yih_cermak_1952]\] \[[Yu et al 2021][research_yu_ni_2021]\] \[[Yu et al 2025][research_yu_guo_2025]\] \[[Yu et al 2025][research_yu_wang_2025]\] \[[Zhao et al 2025][research_zhao_jin_2025]\] \[[Zhu and Zhao 2016][research_zhu_zhao_2016]\] \[[Zhu et al 2018][research_zhu_chen_2018]\] \[[Zhu et al 2018][research_zhu_lee_2018]\] \[[Zhu et al 2022][research_zhu_gu_2022]\] \[[Zhuang and Lu 2015][research_zhuang_lu_2015]\] \[[Zien and Ragsdale 1979][research_zien_ragsdale_1979]\]

### Aluminium alloys and their strength when hot

**The material the X-27 would have been built of.** Aluminium alloys at elevated temperature, and their creep, fatigue, fracture and design data.

**92 records.** \[[Allen and Mahorter 1964][research_allen_mahorter_1964]\] \[[Awerbuch 1980][research_awerbuch_1980]\] \[[Ayres 1977][research_ayres_1977]\] \[[Bouzekova-Penkova and Miteva 2022][research_bouzekovapenkova_miteva_2022]\] \[[Brodrick 1976][research_brodrick_1976]\] \[[Brown 1970][research_brown_1970]\] \[[Cao and Zhang 2023][research_cao_zhang_2023]\] \[[Carlson and Schwope 1952][research_carlson_schwope_1952]\] \[[Cervay 1972][research_cervay_1972]\] \[[Cervay 1975][research_cervay_1975]\] \[[Chang et al 1953][research_chang_nordheim_1953]\] \[[Chen et al 2013][research_chen_wang_2013]\] \[[Cho and Findley 1983][research_cho_findley_1983]\] \[[Composite material comprising reinforced aluminium or aluminium-base alloy 1978][research_composite_material_1978]\] \[[Dahlberg 1963][research_dahlberg_1963]\] \[[Development of an Improved Elevated Temperature Aluminium Alloy Alcan GBX158 1975][research_development_of_1975]\] \[[Duncheva et al 2020][research_duncheva_maximov_2020]\] \[[Edahl and Domack 2004][research_edahl_domack_2004]\] \[[Erich 1980][research_erich_1980]\] \[[Fine 1959][research_fine_1959]\] \[[Fine and Weertman 1983][research_fine_weertman_1983]\] \[[Galkin and Sergeev 1976][research_galkin_sergeev_1976]\] \[[Giuliano 2016][research_giuliano_2016]\] \[[Go and Wilshire 1992][research_go_wilshire_1992]\] \[[Golovin 1982][research_golovin_1982]\] \[[Hall et al 1997][research_hall_hamilton_1997]\] \[[Hamilton et al 1997][research_hamilton_hall_1997]\] \[[Hansen 1972][research_hansen_1972]\] \[[Hawk and Wilsdorf 1988][research_hawk_wilsdorf_1988]\] \[[Heath-Smith 1965][research_heathsmith_1965]\] \[[Holl 1975][research_holl_1975]\] \[[Inglis and Larke 1958][research_inglis_larke_1958]\] \[[Iseki and Nicholas 1979][research_iseki_nicholas_1979]\] \[[Jain and Liang 2020][research_jain_liang_2020]\] \[[Ji et al 2021][research_ji_yuan_2021]\] \[[Johnson et al 1960][research_johnson_henderson_1960]\] \[[Kothari 1973][research_kothari_1973]\] \[[Lee and Chen 2005][research_jonathanalee_poshouchen_2005]\] \[[Jones 1973][research_jones_1973]\] \[[Kothari 1971][research_kothari_1971]\] \[[Kramer and Potter 1966][research_kramerbe_potterdy_1966]\] \[[Kumar et al 2022][research_kumar_dwivedi_2022]\] \[[Kun et al 2018][research_kun_tingting_2018]\] \[[Lai and Findley 1980][research_lai_findley_1980]\] \[[Lawley and Koczak 1984][research_lawley_koczak_1984]\] \[[Lawley and Koczak 1985][research_lawley_koczak_1985]\] \[[Lee and Sanders 2002][research_lee_sanders_2002]\] \[[Lee 1998][research_leeja_1998]\] \[[Lee 2003][research_leejonathana_2003]\] \[[Lee and Chen 2002][research_leejonathana_chenposhou_2002]\] \[[Lee and Munafo 2002][research_leejonathana_munafopaulm_2002]\] \[[Li et al 2024][research_li_li_2024]\] \[[Liu et al 2016][research_liu_zhu_2016]\] \[[Lypchanskyi et al 2024][research_lypchanskyi_janus_2024]\] \[[Mahorter and Robert G. 1961][research_mahorter_robertg_1961]\] \[[Mathauser and Deveikis 1955][research_mathausereldone_deveikiswilliamd_1955]\] \[[Mathauser and Deveikis 1957][research_mathausereldone_deveikiswilliamd_1957]\] \[[Minnicino et al 2009][research_minnicino_gray_2009]\] \[[Montano 1967][research_montanojw_1967]\] \[[Mozley 1943][research_mozley_1943]\] \[[Neshpor et al 1991][research_neshpor_armyagov_1991]\] \[[Ohashi and Ohno 1982][research_ohashi_ohno_1982]\] \[[Papirno 1966][research_papirno_1966]\] \[[Papirno and Gerard 1962][research_papirno_gerard_1962]\] \[[Parris et al 1957][research_parris_sherman_1957]\] \[[Paton et al 1982][research_paton_bampton_1982]\] \[[Radon 1969][research_radon_1969]\] \[[Reynolds 1993][research_reynolds_1993]\] \[[Shechtman 1981][research_shechtman_1981]\] \[[Shen 2017][research_shen_2017]\] \[[Shirinzadeh Dastgiri et al 2023][research_shirinzadehdastgiri_fuerth_2023]\] \[[Sih and Chou 1989][research_sih_chou_1989]\] \[[Srivatsan 1999][research_srivatsan_1999]\] \[[Srivatsan and Anand 1998][research_srivatsan_anand_1998]\] \[[Stickley and Brownhill 1964][research_stickley_brownhill_1964]\] \[[Su and Young 2017][research_su_young_2017]\] \[[Su et al 2023][research_su_qu_2023]\] \[[Sullivan 1978][research_sullivanpg_1978]\] \[[Taig 1961][research_taig_1961]\] \[[Tanaka and Nojima 1971][research_tanaka_nojima_1971]\] \[[Tirpak 1985][research_tirpak_1985]\] \[[Tomczyk and Seweryn 2017][research_tomczyk_seweryn_2017]\] \[[Tomczyk and Seweryn 2021][research_tomczyk_seweryn_2021]\] \[[Torić et al 2018][research_toric_glavinic_2018]\] \[[Vorob'ev and Bich 1977][research_vorobev_bich_1977]\] \[[Wang and Trapp 1958][research_wang_trapp_1958]\] \[[Weiss and Gegal 2014][research_weiss_gegal_2014]\] \[[Yamauchi et al 1988][research_yamauchi_shibue_1988]\] \[[Zaidi 1988][research_zaidi_1988]\] \[[Zhang et al 2009][research_zhang_zhou_2009]\] \[[Zhang et al 2026][research_zhang_zhang_2026]\] \[[Zubair et al 2022][research_zubair_ejaz_2022]\]

### Titanium, other alloys and composites at elevated temperature

**The materials the X-27 did not use.** Titanium alloys and their processing, nickel and other superalloys, creep and fatigue at temperature, and composite and ceramic structure.

**84 records.** \[[Arkoosh and Fiore 1972][research_arkoosh_fiore_1972]\] \[[Balashov and Petukhov 1969][research_balashov_petukhov_1969]\] \[[Bhandari et al 2025][research_bhandari_gaur_2025]\] \[[Bloxsom 1958][research_bloxsom_1958]\] \[[Carew et al 1956][research_carew_crossley_1956]\] \[[Chen et al 2020][research_chen_mi_2020]\] \[[Chen et al 2021][research_chen_mi_2021]\] \[[Chen et al 2022][research_chen_mi_2022]\] \[[Davis 1973][research_davis_1973_b]\] \[[Davis et al 1972][research_davisra_elrodsd_1972]\] \[[Dobeš et al 2019][research_dobes_dymacek_2019]\] \[[Ebied et al 2018][research_ebied_hamada_2018]\] \[[Experimental Study on the High-Temperature Creep Behavior of Super Alloy Using Digital Image Correlation 2020][research_experimental_study_2020]\] \[[Fang et al 2022][research_fang_zhang_2022]\] \[[Feng et al 2025][research_feng_chen_2025]\] \[[Gehring and Engle 1963][research_gehring_engle_1963]\] \[[Glenn and Koch 1973][research_glenn_koch_1973]\] \[[Glorioso 1960][research_glorioso_1960]\] \[[Guo et al 2021][research_guo_tian_2021]\] \[[Han and Seo 2016][research_han_seo_2016]\] \[[Hashin and Humphreys 1980][research_hashin_humphreys_1980]\] \[[Heimerl and Hardrath 1965][research_heimerlgeorgej_hardrathherbertf_1965]\] \[[Imig 1973][research_imig_1973]\] \[[Initial Damage Mechanism of Nickel-Based Alloy 625 Under Creep Loadings at Elevated Temperatures 2019][research_initial_damage_2019]\] \[[Islam et al 2015][research_islam_fermin_2015]\] \[[Jeans et al 1983][research_jeans_grimes_1983]\] \[[Jeffs and Lancaster 2015][research_jeffs_lancaster_2015]\] \[[Johnson et al 1959][research_johnson_henderson_1959]\] \[[Kaczorowski et al 2015][research_kaczorowski_skoczylas_2015]\] \[[Khademi et al 2019][research_khademi_ikeda_2019]\] \[[Kolom 1969][research_kolom_1969]\] \[[Kovács et al 2023][research_kovacs_csik_2023]\] \[[Krashchenko and Statsenko 1981][research_krashchenko_statsenko_1981]\] \[[Krivenyuk et al 1971][research_krivenyuk_tsvilyuk_1971]\] \[[Li and Sun 2022][research_li_sun_2022]\] \[[Li et al 2021][research_li_tian_2021]\] \[[Li et al 2024][research_li_chen_2024]\] \[[Li et al 2024][research_li_xu_2024]\] \[[Li et al 2025][research_li_dong_2025]\] \[[Lin et al 2020][research_lin_shao_2020]\] \[[Lunde 1977][research_lundet_1977]\] \[[Maksimovich et al 1977][research_maksimovich_karpinos_1977]\] \[[Malashenko and Vashchilo 1975][research_malashenko_vashchilo_1975]\] \[[Malvi and Roy 2021][research_malvi_roy_2021]\] \[[Mills 1978][research_mills_1978]\] \[[Ochonogor et al 2017][research_ochonogor_akinlabi_2017]\] \[[Palienko et al 1976][research_palienko_pogrebnyak_1976]\] \[[Perepezko 2001][research_perepezko_2001]\] \[[Reymer et al 2018][research_reymer_zielinski_2018]\] \[[Rhomberg 1972][research_rhomberg_1972]\] \[[Richards and Thompson 1991][research_richardswl_thompsonrandolphc_1991]\] \[[Sajadifar et al 2023][research_sajadifar_maier_2023]\] \[[Sanchez-Carmona and Cuerno-Rejado 2018][research_sanchezcarmona_cuernorejado_2018]\] \[[Sandstrom and White 1961][research_sandstrom_white_1961]\] \[[Saxena 1998][research_saxenaashok_1998]\] \[[Semenov 1981][research_semenov_1981]\] \[[Shi-feng et al 2018][research_shifeng_jiamin_2018]\] \[[Shkaraputa 1976][research_shkaraputa_1976]\] \[[Sinaiskii et al 1972][research_sinaiskii_pogrebnyak_1972]\] \[[Sosnin and Torshenov 1970][research_sosnin_torshenov_1970]\] \[[Stamatelos and Labeas 2025][research_stamatelos_labeas_2025]\] \[[Szusta 2018][research_szusta_2018]\] \[[Tadini et al 2017][research_tadini_grange_2017]\] \[[Tao et al 2024][research_tao_wang_2024]\] \[[Tian et al 2021][research_tian_shunke_2021]\] \[[Toffol and Ricci 2023][research_toffol_ricci_2023]\] \[[Tuninetti et al 2024][research_tuninetti_sepulveda_2024]\] \[[Uemura et al 2020][research_uemura_kamata_2020]\] \[[Uludag and Turan 2015][research_uludag_turan_2015]\] \[[Valoppi et al 2017][research_valoppi_bruschi_2017]\] \[[Vorob’ev and Galiakhmetov 2023][research_vorobev_galiakhmetov_2023]\] \[[Wang et al 2018][research_wang_liu_2018]\] \[[Wang et al 2021][research_wang_zhao_2021]\] \[[Wei et al 2022][research_wei_qu_2022]\] \[[Wen et al 2022][research_wen_kong_2022]\] \[[White 1997][research_white_1997]\] \[[Xiaokang et al 2018][research_xiaokang_kuaishe_2018]\] \[[Xu et al 2020][research_xu_cheng_2020]\] \[[Yang et al 2021][research_yang_ji_2021]\] \[[Yang et al 2021][research_yang_tian_2021]\] \[[Yang et al 2022][research_yang_liang_2022]\] \[[Yu et al 2026][research_yu_yu_2026]\] \[[Zheldubovskii and Ishchenko 1982][research_zheldubovskii_ishchenko_1982]\] \[[Zhong et al 2024][research_zhong_yu_2024]\]

### Conceptual design, optimisation and the derivative aircraft

**How an unbuilt aircraft is now evaluated.** Conceptual and preliminary design, multidisciplinary optimisation, surrogate models and uncertainty, and derivative design.

**81 records.** \[[Abu Salem et al 2023][research_abusalem_palaia_2023_b]\] \[[Al-Shamma et al 2017][research_alshamma_ali_2017]\] \[[Albuquerque et al 2018][research_albuquerque_gamboa_2018]\] \[[Allison et al 2015][research_allison_morris_2015]\] \[[Arnson et al 2026][research_arnson_aljaber_2026]\] \[[Babaei et al 2018][research_babaei_setayandeh_2018]\] \[[Bianchi et al 2020][research_bianchi_secco_2020]\] \[[Horvath and Wells 2018][research_brycelhorvath_douglaspwells_2018]\] \[[Bryson and Rumpfkeil 2019][research_bryson_rumpfkeil_2019]\] \[[Chell et al 2021][research_chell_hoffenson_2021]\] \[[Cheng et al 2016][research_cheng_yue_2016]\] \[[Coen and Foss 1985][research_coen_foss_1985]\] \[[Cummings et al 2018][research_cummings_liersch_2018]\] \[[Di Bianchi et al 2018][research_dibianchi_orra_2018]\] \[[Du 2026][research_du_2026]\] \[[Duan et al 2026][research_duan_wan_2026]\] \[[Dudley 1986][research_dudley_1986]\] \[[Golombek et al 2026][research_golombek_bustamante_2026]\] \[[Hackman and Richardson 1964][research_hackman_richardson_1964]\] \[[He and Shi 2025][research_he_shi_2025]\] \[[Hon et al 2022][research_hon_karpuk_2022]\] \[[Hosseini et al 2024][research_hosseini_vaziryzanjany_2024]\] \[[Jelev et al 2019][research_jelev_keane_2019]\] \[[Ji et al 2024][research_ji_huang_2024]\] \[[Khatri and Sinha 2023][research_khatri_sinha_2023]\] \[[Kretov 2021][research_kretov_2021]\] \[[Kumar 1999][research_kumar_1999]\] \[[Leng et al 2024][research_leng_feng_2024]\] \[[Li and Geiselhart 2022][research_li_geiselhart_2022]\] \[[Liu and Jiang 2022][research_liu_jiang_2022]\] \[[Lukyanov et al 2024][research_lukyanov_hoang_2024]\] \[[Min Tint 2018][research_mintint_2018]\] \[[Mokotoff et al 2026][research_mokotoff_arnson_2026]\] \[[Moorhouse and Jenkins 1975][research_moorhouse_jenkins_1975]\] \[[Moëns 2022][research_moens_2022]\] \[[Munjulury et al 2015][research_munjulury_staack_2015]\] \[[Nam and Mavris 2018][research_nam_mavris_2018]\] \[[Ng and Willcox 2016][research_ng_willcox_2016]\] \[[Pan et al 2017][research_pan_huang_2017]\] \[[Park et al 2015][research_park_lee_2015]\] \[[Park et al 2016][research_park_chung_2016]\] \[[Park et al 2016][research_park_chung_2016_b]\] \[[Park et al 2018][research_park_chung_2018]\] \[[Powers et al 1983][research_powers_driggers_1983_b]\] \[[Prigent et al 2015][research_prigent_marechal_2015]\] \[[Qin 2026][research_qin_2026]\] \[[Ramachandran and Wells 1974][research_ramachandran_wells_1974]\] \[[Ramachandran and Wells 1975][research_ramachandran_wells_1975]\] \[[Raymer 1998][research_raymer_1998]\] \[[Riccobene and Ricci 2015][research_riccobene_ricci_2015]\] \[[Roelofs et al 2021][research_roelofs_kurowicka_2021]\] \[[Roskam and Dusto 1969][research_roskam_dusto_1969]\] \[[Roskam et al 1968][research_roskam_holgate_1968]\] \[[Safavi et al 2015][research_safavi_tarkian_2015]\] \[[Saporito et al 2023][research_saporito_daronch_2023]\] \[[Saraswathi 2000][research_saraswathi_2000]\] \[[Saves et al 2024][research_saves_diouane_2024]\] \[[Schwartz 1988][research_schwartz_1988]\] \[[Setayandeh and Babaei 2020][research_setayandeh_babaei_2020]\] \[[Sgueglia et al 2020][research_sgueglia_schmollgruber_2020]\] \[[Shi 2025][research_shi_2025]\] \[[Siedlak et al 2017][research_siedlak_pinon_2017]\] \[[Stephan et al 2024][research_stephan_heyen_2024]\] \[[Subramanian and DeLaurentis 2016][research_subramanian_delaurentis_2016]\] \[[Sóbester 2021][research_sobester_2021]\] \[[Tao and Sun 2019][research_tao_sun_2019]\] \[[Tao et al 2020][research_tao_sun_2020]\] \[[Tfaily et al 2024][research_tfaily_diouane_2024]\] \[[Tfaily et al 2026][research_tfaily_bartoli_2026]\] \[[Tian and Li 2020][research_tian_li_2020]\] \[[Tich et al 1987][research_tich_shaw_1987]\] \[[Todorov et al 2023][research_todorov_rakov_2023]\] \[[Triplett 1980][research_triplett_1980]\] \[[Tyan et al 2017][research_tyan_nguyen_2017]\] \[[Veresnikov 2025][research_veresnikov_2025]\] \[[Veresnikov et al 2026][research_veresnikov_goncharenko_2026]\] \[[Wang et al 2023][research_wang_xu_2023]\] \[[Wilson et al 2023][research_wilson_figliola_2023]\] \[[Xu and Yu 2025][research_xu_yu_2025]\] \[[York et al 2018][research_york_ozturk_2018]\] \[[Ünal et al 2023][research_unal_oz_2023]\]

### Stability, control and flying qualities

**The control problem of a high tail and a short wing.** Longitudinal and lateral stability, tail and canard effects, departure, spin and deep stall, and flying qualities.

**68 records.** \[[Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]\] \[[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]\] \[[Anderson 1985][research_anderson_1985]\] \[[Anglin 1978][research_anglin_1978]\] \[[Ansari et al 2022][research_ansari_m_2022]\] \[[Archbold 1945][research_archbold_1945]\] \[[Baron 1953][research_baron_1953]\] \[[Bielat 1959][research_bielatralphp_1959]\] \[[Bihrle and Barnhart 1982][research_bihrle_barnhart_1982]\] \[[Bihrle and Billy 1980][research_bihrle_jr_1980]\] \[[Bollech and Kelly 1954][research_bollechthomasv_kellyhneale_1954]\] \[[Bryant 1933][research_bryant_1933]\] \[[Bykerk et al 2020][research_bykerk_verstraete_2020]\] \[[Casteel and Weyl 1970][research_casteel_weyl_1970]\] \[[Chambers and Bowman 1971][research_chambers_bowman_1971]\] \[[Cook 1965][research_cook_1965]\] \[[Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornellaeronauticallabincbuffalony_1947]\] \[[Crowe 1937][research_crowe_1937]\] \[[Cunis et al 2020][research_cunis_condomines_2020]\] \[[Deitchman 1953][research_deitchman_1953]\] \[[Dias 2023][research_dias_2023]\] \[[Ding 2023][research_ding_2023]\] \[[Donlan 1976][research_donlancj_1976]\] \[[Driver 1958][research_drivercornelius_1958]\] \[[Eberle and Fowler 1971][research_eberle_fowler_1971]\] \[[Eulrich and Mesiah 1974][research_eulrich_mesiah_1974]\] \[[Farhat et al 2000][research_farhat_harris_2000]\] \[[Gates 1940][research_gates_1940]\] \[[Gilbert et al 1976][research_gilbert_nguyen_1976]\] \[[Gilruth and White 1941][research_gilruthrr_whitemd_1941]\] \[[Goud and Dwivedi 2022][research_goud_dwivedi_2022]\] \[[Hamed 1993][research_hamed_1993]\] \[[Harper and Robert P. 1955][research_harper_robertp_1955]\] \[[Hess 1986][research_hess_1986]\] \[[Hewes 1950][research_hewesdonalde_1950]\] \[[Hwang and Pi 1979][research_hwang_pi_1979]\] \[[Irsyad Lukman and Agoes Moelyadi 2018][research_irsyadlukman_agoesmoelyadi_2018]\] \[[Jenney 1935][research_jenney_1935]\] \[[Kleckner 1945][research_klecknerharoldf_1945]\] \[[Kleckner 1946][research_klecknerharoldf_1946]\] \[[Langham 1978][research_langham_1978]\] \[[Lovell and Wilson 1947][research_lovelljcalvin_wilsonherbertajr_1947]\] \[[Malcolm and Ng 1991][research_malcolm_ng_1991]\] \[[Malikov and Miltsov 2019][research_malikov_miltsov_2019]\] \[[Milenković-Babić et al 2017][research_milenkovicbabic_samardzic_2017]\] \[[Millidere et al 2022][research_millidere_yigit_2022]\] \[[Min et al 2024][research_min_xian_2024]\] \[[Mungall 1948][research_mungallrobertc_1948]\] \[[Neal and Smith 1970][research_neal_smith_1970]\] \[[Neal and Smith 1970][research_neal_smith_1970_b]\] \[[Neumark 1950][research_neumark_1950]\] \[[Nguyen et al 1976][research_nguyenlt_anglinel_1976]\] \[[Powers 1966][research_powersbg_1966]\] \[[Ramamurti 2011][research_ramamurti_2011]\] \[[Reid 1937][research_reid_1937]\] \[[Roache 1965][research_roache_1965]\] \[[Rodgers 1965][research_rodgers_1965]\] \[[Sachs 1975][research_sachs_1975]\] \[[Schwanz 1972][research_schwanz_1972]\] \[[Sleeman and Byrnes 1953][research_sleemanwilliamc_byrnesandrewl_1953]\] \[[Sleeman 1957][research_sleemanwilliamcjr_1957]\] \[[Squires 2002][research_squires_2002]\] \[[Swortzel and Barfield 1976][research_swortzel_barfield_1976]\] \[[Washington et al 1968][research_washington_pettis_1968]\] \[[Watanabe et al 2023][research_watanabe_sunada_2023]\] \[[Weissman 1973][research_weissman_1973]\] \[[Wisniewski 1951][research_wisniewski_1951]\]

### The F-104, the J79 and later named fighters

**The aircraft by name.** The F-104 and its J79, the competitors and successors the Lancer was measured against, and the later fighter and demonstrator programmes named in their titles.

**No title in the survey names the X-27, the CL-1200 or the Lancer.** The aircraft this article is about survives in the literature only through its parent, and thirteen titles name the F-104 or its J79, of which five name the engine.

**59 records.** \[[Background the Advanced Tactical 1998][research_background_the_1998]\] \[[Barham 1994][research_barham_1994]\] \[[Biesiadny et al 1978][research_biesiadny_lee_1978]\] \[[Birkler 2001][research_birkler_2001]\] \[[Bogdan 2015][research_bogdan_2015]\] \[[Brantley and Stabrylla 1979][research_brantley_stabrylla_1979]\] \[[Brignac et al 1976][research_brignac_ness_1976]\] \[[Capone and Berrier 1980][research_capone_berrier_1980]\] \[[Dietz and Bailey 1973][research_dietz_bailey_1973]\] \[[Enzinger 1988][research_enzinger_1988]\] \[[Esser and Ruff-Stahl 2021][research_esser_ruffstahl_2021]\] \[[F-104 Resource Tape 1992][research_f_104_resource_1992]\] \[[Farr 1976][research_farr_1976]\] \[[Friend and Sefic 1972][research_friend_sefic_1972]\] \[[Friend and Sakamoto 1978][research_friendel_sakamotogm_1978]\] \[[Gill and Sain 1981][research_gill_sain_1981]\] \[[Gleason and Martone 1980][research_gleason_martone_1980]\] \[[Haering and Burcham 1984][research_haering_burcham_1984]\] \[[Hebbar et al 1991][research_hebbar_platzer_1991]\] \[[Hicks and Huckabine 1989][research_hicks_huckabine_1989]\] \[[Hild and Crocker 2006][research_hild_crocker_2006]\] \[[Hild and Crocker 2006][research_hild_crocker_2006_b]\] \[[Hild and Crocker 2008][research_hild_crocker_2008]\] \[[Hoerter et al 1991][research_hoerter_powers_1991]\] \[[Hughes and Johnson 1972][research_hughes_johnson_1972]\] \[[Hughes and Mackall 1984][research_hughesdl_mackallkg_1984]\] \[[Iliff et al 1970][research_iliff_smith_1970]\] \[[Jackson 1980][research_jackson_1980]\] \[[Johns 1998][research_johns_1998]\] \[[Kim 2024][research_kim_2024]\] \[[Kohn 1964][research_kohn_1964]\] \[[Kong et al 2017][research_kong_jiang_2017]\] \[[Kurtenbach 1978][research_kurtenbach_1978]\] \[[Lane and Behenna 1991][research_lane_behenna_1991]\] \[[Latham 2020][research_latham_2020]\] \[[Loren et al 1992][research_loren_kerr_1992]\] \[[Marshall and Schweikhard 1973][research_marshall_schweikhard_1973]\] \[[Marshall 1971][research_marshallrt_1971]\] \[[McKeehen and Cord 1997][research_mckeehen_cord_1997]\] \[[Morgenfeld 1992][research_morgenfeld_1992]\] \[[Myers and Walsh 1988][research_myerslawrencep_walshkevinr_1988]\] \[[NAVY Participation and the 1998][research_navy_participation_1998]\] \[[Neville et al 1992][research_neville_oflarity_1992]\] \[[Nicholson 1985][research_nicholson_1985]\] \[[Piccirillo and Aronstein 1997][research_piccirillo_aronstein_1997]\] \[[Poorman 1980][research_poorman_1980]\] \[[Ray et al 1988][research_ray_hicks_1988]\] \[[Scherz and Williams 1978][research_scherz_williams_1978]\] \[[Siano 2014][research_siano_2014]\] \[[Smith and Burgess 1960][research_smith_burgess_1960]\] \[[Smith et al 1976][research_smith_jones_1976]\] \[[Smith et al 1984][research_smith_mead_1984]\] \[[Song et al 2019][research_song_kim_2019]\] \[[Studer 2012][research_studer_2012]\] \[[von Hlatky and Rice 2018][research_vonhlatky_rice_2018]\] \[[Weeks 1986][research_weeks_1986]\] \[[Whoric 1973][research_whoric_1973]\] \[[Whoric 1977][research_whoric_1977]\] \[[Woelk 1989][research_woelk_1989]\]

### Fighter aircraft design, requirements and history

**Fighters as a class.** Fighter design method, requirements, configuration studies and the history of fighter development, where no narrower cluster above claims the title.

**43 records.** \[[A Canadian Light Fighter 1940][research_a_canadian_1940]\] \[[A New Fighter Aircraft 2003][research_a_new_2003]\] \[[Almuradi 2021][research_almuradi_2021]\] \[[Bennett 1990][research_bennett_1990]\] \[[Branger 1972][research_branger_1972]\] \[[Bunton and Denegri 2000][research_bunton_denegri_2000]\] \[[Bureau Of Aeronautics Navy Washingtondc 1949][research_bureauofaeronauticsnavywashingtondc_1949]\] \[[Caap and Elemeland 1986][research_caap_elemeland_1986]\] \[[Cordeaux 1991][research_cordeaux_1991]\] \[[Crites et al 1992][research_crites_rueger_1992]\] \[[Design sheets for New 2003][research_design_sheets_2003]\] \[[Dollyhigh and Foss 1985][research_dollyhigh_foss_1985]\] \[[Eberhardt 2005][research_eberhardt_2005]\] \[[Fighter and Attack Aircraft 2008][research_fighter_and_2008]\] \[[Fundamentals of Fighter Design 2001][research_fundamentals_of_2001]\] \[[Griffin 2012][research_griffin_2012]\] \[[Heiss et al 1992][research_heiss_eberle_1992]\] \[[Herbst 1980][research_herbst_1980]\] \[[Jayakrishnan and Pant 2005][research_jayakrishnan_pant_2005]\] \[[Jenista and Bodden 1989][research_jenista_bodden_1989]\] \[[Kitowski 1986][research_kitowski_1986]\] \[[Kuchar and Wolf 1993][research_kuchar_wolf_1993]\] \[[Kwon and Sankar 1991][research_kwon_sankar_1991]\] \[[Kwon and Sankar 1992][research_kwon_sankar_1992]\] \[[Lewis 2002][research_lewis_2002]\] \[[Liddell 1950][research_liddell_1950]\] \[[Madelung 1977][research_madelung_1977]\] \[[Planeaux and Barth 1988][research_planeaux_barth_1988]\] \[[Powers et al 1983][research_powers_driggers_1983]\] \[[Russell 2014][research_russell_2014]\] \[[Spearman 1983][research_spearman_1983]\] \[[Spearman 1984][research_spearman_1984]\] \[[Spearman et al 1977][research_spearman_fournier_1977]\] \[[Squires 2004][research_squires_2004]\] \[[St. Aubyn 2015][research_staubyn_2015]\] \[[Stanley 1980][research_stanley_1980]\] \[[The Cutting Edge A 1998][research_the_cutting_1998]\] \[[The Potez Multi-Seater Fighter 1935][research_the_potez_1935]\] \[[Wages 1971][research_wages_1971]\] \[[Ward 1989][research_ward_1989]\] \[[Weirich and Rueger 1999][research_weirich_rueger_1999]\] \[[Whitford 1991][research_whitford_1991]\] \[[Whitford 1995][research_whitford_1995]\]

### Defence acquisition, prototyping and the arms trade

**The literature for what happened to the programme.** Military aircraft procurement and competition, prototyping policy, cost, and arms export and military assistance.

**41 records.** \[[A Comparison of Cost 1977][research_a_comparison_1977]\] \[[Anicetti 2023][research_anicetti_2023]\] \[[Arthur 2022][research_arthurw_2022]\] \[[Beesly 1966][research_beesly_1966]\] \[[Beesly 1966][research_beesly_1966_b]\] \[[Behavior Patterns of Three 2022][research_behavior_patterns_2022]\] \[[Bennett 2003][research_bennett_2003]\] \[[Boger and Nussbaum 1990][research_boger_nussbaum_1990]\] \[[Boger et al 1989][research_boger_greer_1989]\] \[[Carey 1982][research_carey_1982]\] \[[Carlyle 1976][research_carlyle_1976]\] \[[Cate 2003][research_cate_2003]\] \[[Choi 2026][research_choi_2026]\] \[[Coble et al 2014][research_coble_royster_2014]\] \[[Department Of Defense Washington Dc 1997][research_departmentofdefensewashingtondc_1997]\] \[[Diphda and Wiswayana 2026][research_diphda_wiswayana_2026]\] \[[Duddy et al 2020][research_duddy_landucci_2020]\] \[[Esau 2024][research_esau_2024]\] \[[Fellers and Patierno 1970][research_fellers_patierno_1970]\] \[[Franck et al 2012][research_franck_lewis_2012]\] \[[Gregory and Wilcox 1970][research_gregorytj_wilcoxde_1970]\] \[[Grytsyshen et al 2025][research_grytsyshen_abramova_2025]\] \[[Harle 1979][research_harle_1979]\] \[[Hellemeier 2019][research_hellemeier_2019]\] \[[Higham and Holley 1966][research_higham_holley_1966]\] \[[Kaplan 1980][research_kaplan_1980]\] \[[Likhachev 2024][research_likhachev_2024]\] \[[Linden 2022][research_linden_2022]\] \[[Lorell 1989][research_lorell_1989]\] \[[MILITARY PRESENCE AND ARMS EXPORT IN FRANCE’S MIDDLE EAST STRATEGY 2025][research_military_presence_2025]\] \[[Phillips 1999][research_phillips_jr_1999]\] \[[Procurement Process Geared Up for New Airplanes 1980][research_procurement_process_1980]\] \[[Rosenthal 1975][research_rosenthal_1975]\] \[[Rosenthal and Brandeau 1983][research_rosenthal_brandeau_1983]\] \[[Sowter 1973][research_sowter_1973]\] \[[Taufik Budi Cahyana et al 2023][research_taufikbudicahyana_achmadwardana_2023]\] \[[Thankachan 2025][research_thankachan_2025]\] \[[Um 2016][research_um_2016]\] \[[Wardana et al 2022][research_wardana_cahyana_2022]\] \[[Watkins 2019][research_watkins_2019]\] \[[Yusof and Rahim 2017][research_yusof_rahim_2017]\]

### Thermal stress, thermal buckling and thermoelasticity

**The heating as load.** Thermal stress in skins and structures, thermal buckling, and the thermoelastic and aerothermoelastic coupling the article's eighty-two kelvin figure belongs to.

**35 records.** \[[2016][research_anon_2016]\] \[[A Conference on Thermal Stress 1954][research_a_conference_1954]\] \[[Ayers 1962][research_ayers_1962]\] \[[Calligeros and Dugundji 1961][research_calligeros_dugundji_1961]\] \[[Chai et al 2017][research_chai_song_2017]\] \[[Chai et al 2020][research_chai_li_2020]\] \[[Chen and Xia 2022][research_chen_xia_2022]\] \[[Cong et al 2024][research_cong_yu_2024]\] \[[Dixon et al 1961][research_dixonsidneyc_griffithgeorgee_1961]\] \[[Ganilova et al 2021][research_ganilova_cartmell_2021]\] \[[Ganilova et al 2022][research_ganilova_cartmell_2022]\] \[[Gellatly and Gallagher 1964][research_gellatly_gallagher_1964]\] \[[Gellatly et al 1965][research_gellatly_bijlaard_1965]\] \[[Gutiérrez Álvarez and Bisagni 2021][research_gutierrezalvarez_bisagni_2021]\] \[[Jenkins 1979][research_jenkinsjm_1979]\] \[[Kang et al 2024][research_kang_liang_2024]\] \[[Li et al 2015][research_li_pan_2015]\] \[[Loveless and Boswell 1954][research_loveless_boswell_1954]\] \[[Ma 2021][research_ma_2021]\] \[[Mahlmeister et al 1955][research_mahlmeister_ishimoto_1955]\] \[[Mansfield 1967][research_mansfield_1967]\] \[[Matsumoto and Sekiya 1975][research_matsumoto_sekiya_1975]\] \[[Parkes 1953][research_parkes_1953]\] \[[Parkes 1954][research_parkes_1954]\] \[[Parkes 1956][research_parkes_1956]\] \[[Parkes 1956][research_parkes_1956_b]\] \[[Rivello 1965][research_rivello_1965]\] \[[Sebata and Ushijima 2021][research_sebata_ushijima_2021]\] \[[Sebata and Ushijima 2022][research_sebata_ushijima_2022]\] \[[Shao et al 2016][research_shao_cao_2016]\] \[[Tani 1978][research_tani_1978]\] \[[Uthgenannt 1971][research_uthgenannt_1971]\] \[[Wang et al 2023][research_wang_gao_2023]\] \[[Xie et al 2025][research_xie_ye_2025]\] \[[Xue et al 2020][research_xue_li_2020]\]

### Boundary-layer control, high lift and short take-off

**The low-speed end of the envelope.** Blowing and suction, high-lift devices, and take-off and landing, on which the article's take-off claim rests.

**28 records.** \[[Aerodynamic and Landing Measurements 1960][research_aerodynamic_and_1960]\] \[[Anglin and Satran 1980][research_anglin_satran_1980]\] \[[Baker 1966][research_baker_1966]\] \[[Cliett 1952][research_cliett_1952]\] \[[Cordner 1967][research_cordner_1967]\] \[[Desyatnik 2015][research_desyatnik_2015]\] \[[Edwards 2010][research_edwards_2010]\] \[[Goranson 1942][research_goransonrfabian_1942]\] \[[Hawks 1982][research_hawks_1982]\] \[[Horton et al 1951][research_hortonelmera_loftinlaurencek_1951]\] \[[Inger and Zee 1978][research_inger_zee_1978]\] \[[Kuchinka 1966][research_kuchinka_1966]\] \[[Kuz'mich et al 1975][research_kuzmich_sekundov_1975]\] \[[Linnell 1963][research_linnell_1963]\] \[[Muehter 1974][research_muehter_1974]\] \[[Papadales and Basil S. 1979][research_papadales_basils_1979]\] \[[Probst and Melber-Wilkending 2021][research_probst_melberwilkending_2021]\] \[[Radespiel et al 2016][research_radespiel_burnazzi_2016]\] \[[Raspet 1957][research_raspet_1957]\] \[[Roberts et al 1966][research_roberts_smith_1966]\] \[[Rumsey et al 2019][research_rumsey_slotnick_2019]\] \[[Selegan 1983][research_selegan_1983]\] \[[Sleeman 1961][research_sleemanwilliamcjr_1961]\] \[[Smith et al 1979][research_smith_yamakawa_1979]\] \[[Spreemann 1958][research_spreemannkennethp_1958]\] \[[Thomas 1965][research_thomas_1965]\] \[[Toll 1942][research_tollthomasa_1942]\] \[[Williams and Butler 1963][research_williams_butler_1963]\]

### Other aeronautical literature

**The residual, reported and not hidden.** On-subject work that belongs to no cluster above, being a wind tunnel and flight correlation of the XB-70. It is too small to name.

**1 records.** \[[Peterson 1982][research_peterson_1982]\]

## Where the Framing Breaks Down

**The keystone framing is weaker here than anywhere else in this series and the reasons should be stated plainly.**

**There was no keystone, because there was no programme.** A research aircraft's keystone is the question
its hardware was dimensioned against. The X-27's hardware was never dimensioned against anything, because it
was never built. What has been treated as the keystone is a stated test objective in a proposal, which is a
much softer thing.

**The Mach 2.6 objective may not have been serious.** A proposal written to attract funding names attractive
numbers. The article has computed what Mach 2.6 would have required and found two obstacles, but
**it cannot establish that anyone at Lockheed intended to sustain that speed** rather than to touch it
briefly in a demonstration.

**The manoeuvre comparison flatters the Lancer in one specific way.** It uses the manufacturer's weights and
the engine's rated thrust. Manufacturer's weights are optimistic in the ratio that prototypes are
historically heavier than their proposals, and installed thrust is below rated thrust by an inlet-and-nozzle
allowance this article has not applied. **Both errors push the same direction.**

**The comparison aircraft are not contemporaneous with each other.** The F-15A entered service in 1976, the
F-5E in 1973, and the CL-1200-2 never. Comparing them at a single flight condition is a comparison of
designs and not of what any of them would have done against each other.

**And the political reading is the softest thing in the article.** That the arithmetic is consistent with
the reported Air Force attitude is a consistency and not a cause.
**People are perfectly capable of opposing a programme for reasons unrelated to its specific excess power.**

## The Source Base

**This article has a poorer source base than any other in the series and the reader should know it.**

**There is no primary literature about the subject.** The National Aeronautics and Space Administration's
Technical Reports Server returns nothing for the CL-1200 or the Lancer. No wind-tunnel report exists in the
open literature. No test report exists because no test occurred.

**The vehicle facts come from secondary aviation history**, principally
Lockheed's own estimates as published in [Air Enthusiast][book_air_enthusiast_1971] in 1971 and quoted by the
[Lancer reference article][ref_cl1200], [Buttler][book_buttler] on
American secret projects, [Johnson][book_johnson] for the Skunk Works memoir, and [Jenkins][book_jenkins]
for the surrounding experimental-aircraft context, and
**those sources disagree with one another on the matter of who wanted the X-designation**, which the article
reports rather than resolves.

**The physics comes from primary literature about everything except the vehicle.** Supersonic inlet design,
conical flow, compressor stall, elevated-temperature alloy behaviour and fighter performance analysis are
all richly documented in period reports and journals, and the article is built on those.
**That is the method this subject requires. The evidence is gathered on the physics rather than on the vehicle.**

**The engine and airframe numbers are the load-bearing figures and they come from reference sources rather than from documents.**
The 260 pounds per second, the four inches of spike travel and the weight breakdown are
each stated in secondary literature without a cited primary source.
**The inlet agreement computed above is a check on their mutual consistency and is offered as partial corroboration of figures that are otherwise uncorroborated.**

**The research survey holds 2,229 research records drawn from Crossref, the NASA Technical Reports Server and the Defense Technical Information Center**, of which 601 are report primaries, being 27.0 percent, by the identifier rule set out under The Definition of Primary. **The median publication year is 2003.** Of the 2,213 dated records, 802 were published in 1982 or earlier, the period in which the aircraft was proposed and its parent was in service, being 36.2 percent, and 991 were published in 2015 or later, being 44.8 percent.

**Every figure in this article is given as a count and a fraction together**, because a fraction moves
with its denominator. A period count can stand still while its fraction falls, simply because the
contemporary base around it is larger, and neither movement is a fact about coverage.

### The Definition of Primary

**Primacy is a property of the document, and this survey derives it from the identifier.** A record is a report primary when its address is on the NASA Technical Reports Server or it carries a digital object identifier under the 10.21236 prefix, which Crossref registers for Defense Technical Information Center reports. **The NACA and NASA reports on inlets, heating and the F-104 are report primaries under that rule.** The rule does not reach the journal papers of the same period, such as the conical flow and supersonic diffuser papers of the 1950s, so 27.0 percent is a lower bound on how much of the survey is first-hand. **No document of the X-27 programme itself is in the survey under any rule**, for the reason given above.

### Thin Subjects

**Eight subjects that this article's derivations depend on have thin literatures.** Each count below is the number of research records in this survey whose title carries at least one of the listed terms, with a hyphen read as a space. Where a row joins two groups of terms with the word together, a title must carry a term from each group.

| Subject | Title terms counted | Records |
|---|---|---|
| the X-27 or the CL-1200 Lancer by name | X-27, CL-1200, Lancer | 0 |
| the F-104 and its J79 engine | F-104, Starfighter, J79 | 13 |
| the optimum multi-shock system of Oswatitsch | Oswatitsch, optimum shock, shock diffuser, shock diffusers | 2 |
| the corrected airflow of an engine | corrected airflow, corrected air flow, corrected flow, corrected mass flow | 0 |
| corner speed and sustained turn rate | corner speed, corner velocity, sustained turn, sustained turning | 1 |
| ram drag | ram drag | 1 |
| 2024 aluminium alloy when hot | 2024 together with elevated temperature, elevated temperatures, high temperature, creep, heating, 500 F, hot | 8 |
| the international and export fighter competitions | international fighter, export fighter, F-5E, Tiger II | 1 |

**The aircraft has no literature of its own.** The survey agrees with the reports server, and every vehicle figure in this article rests on the secondary sources named above.

**The parent is thin too.** Of the 13 titles, 5 name the J79 and 3 concern experiments flown in the F-104 or equipment fitted to it, so the derivative argument rests on the parent's published dimensions rather than on a body of F-104 analysis.

**The optimum shock system is a classic with almost no successors by name.** One of the two titles is Oswatitsch's own report on the efficiency of shock diffusers and the other extends a different rule of his to unsteady flow, so the single-cone and two-ramp recoveries computed above rest on the original source.

**The reconciliation of spike travel with airflow has no published counterpart.** No title in the survey names a corrected airflow, so the 4.2 percent agreement above is the article's own and cannot be compared with a published analysis.

**The two quantities the turning argument turns on are almost never a title's subject.** The single title compares corner speed with the speed for best turn, and the rest of the turning literature is framed in terms of turn performance, energy manoeuvrability and agility.

**Ram drag is almost never a title's subject.** The one title naming it concerns a laser-propelled lightcraft, and the subject otherwise appears under installed thrust and thrust and drag bookkeeping, which is where the subsection on it above places it.

**The alloy's hot strength is documented, but not for the temper the article uses.** None of the 8 titles names a T8 temper, so the handbook figure for 2024-T81 after half an hour at temperature is the only source for the strength the structural argument uses.

**The competition the Lancer lost has no technical literature.** The one title naming the F-5E uses it as a research platform, so the comparison with the winner rests on the article's own drag polars.

### What the Survey Admits

**A record is admitted only when a person reading its title finds it on this article's subject.** The records come from the National Aeronautics and Space Administration's Technical Reports Server, the Defense Technical Information Center and the journal literature. Many words this subject depends on also name something else, and a record that shares only such a word is excluded. Agility also names agility in the organisational, sporting and software senses. Distortion also names distortion in the optical, statistical, electrical and perceptual senses. Procurement and acquisition also name the procurement of medical officers, drugs and military manpower and the acquisition of language skills and data, and the procurement budget books are excluded with them. Elevated temperature, thermoelasticity, aspect ratio, inlet and prototype also reach into medicine and biology, polymer physics, civil engineering and geology, batteries, piston engines and industrial compressors, ground power plants and plasma physics. An inlet is also the inflow boundary of a simulation or of a combustor, a pump is not a compressor, and the supersonic nozzle of a condensing separator or a steam turbine shares the inlet's gas dynamics and none of its subject. Fighter also names fire fighters, freedom fighters and the pilots themselves as a subject of psychology and manpower, and Starfighter also names a film, a video game and cultivars of lettuce and lily. Drag also names a performance art, a clause in company law and the drag-reducing additives of pipelines, and Tiger names everything from the animal to a reentry test unit. A record is also excluded when its title carries this subject's vocabulary but studies something the argument never uses. Air-combat tactics and manoeuvre decision algorithms take the aircraft's performance as given and are excluded, while agility metrics and energy manoeuvrability are kept. Noise and acoustics, reentry and space vehicles, flight-control law design, engine accessories, test cells, combustors and engine health, ejector nozzles and thrust reversers, aircraft subsystems including fuel and equipment thermal systems, human factors, and acquisition administration that concerns neither competition, prototyping, cost nor export are excluded. So are design and handling studies of airliners and other transports, rotorcraft, vertical and short take-off aircraft, small unmanned aircraft, flying wings, missiles and projectiles when the title names no method or phenomenon this article uses, and materials work on welding, corrosion, forming, heat treatment and surface processing, steels, the alloys of power and nuclear plant, and the mechanics of graded and nanotube composites. Correction, erratum and withdrawal notices, journal issues, conference volumes, figure records, encyclopedia and dictionary entries, unsigned items, and trade and science news items are excluded as well, because a survey counts research works and not the notices and items attached to them. A signed comment on a paper, a discussion of a paper, the author's closure or reply to it, and a signed letter on a research subject are research works, because each argues about a result, and they are admitted when their subject is the article's. The residual cluster admits under the same rule and holds the on-subject records that no named cluster claims.

**Some records of doubtful relevance are kept.** The surge control of industrial centrifugal compressors is kept because surge is the same instability in any compression system, and studies that use the F-104 as a platform for other experiments are kept because they are part of the parent aircraft's record. Titanium, nickel and refractory alloys at temperature are kept although many of their titles concern engines rather than airframes, because the review of hot structures above turns on the materials the X-27 did not have. Design-optimisation methods demonstrated on another vehicle are kept because the article argues that such methods are the modern answer to its central difficulty, and a reader may weigh all of these accordingly.

**Every research title has been read for relevance, so the off-topic share that remains is a matter of reading judgement.** A reading of titles cannot show that a work is relevant in substance, so this is a statement about titles only.

## Epistemic State

**Historical fact, well attested.**

- The CL-1200 Lancer was a Lockheed private venture derived from the F-104.
- It was entered in the International Fighter Aircraft competition and Northrop's design won in
  November 1970.
- The designation X-27 was allocated in connection with a proposed demonstrator.
- No aircraft was built. One full-scale mock-up was completed.
- The CL-1200-2 was offered into the 1972 Lightweight Fighter competition, which selected the YF-16
  and YF-17.
- The X-27 was to have had rectangular intakes where the CL-1200 had translating cones.

**Historical fact, reported but not independently corroborated here.**

- That up to three fuselages were worked before termination.
- That elements within the Air Force viewed the design as a complication for the F-15.
- The published performance estimates, weights and dimensions, all of which trace to manufacturer's
  figures reproduced in secondary sources.

**Contested in the sources, and left contested.**

- Whether the Air Force sought the X-27 or Lockheed sought the designation. Both accounts appear in
  otherwise careful secondary sources and the article does not adjudicate.

**Engineering analysis, computed here and reproducible from the stated inputs.**

- The recovery temperature at Mach 2.6 and the resulting strength retention.
- The skin thermal time constant and the transient that follows from it.
- The single-cone and two-ramp inlet recoveries, by integration of Taylor-Maccoll.
- The implied cowl radius from the quoted spike travel and its agreement with the engine's airflow.
- The drag polar, sustained load factors, turn rates and specific excess power.
- The Breguet range and the implied mission factor.

**Inference, labelled as such.**

- **The X-27's rectangular intakes were adopted because one cone cannot meet the standard at Mach 2.6.**
  The physics supports it and no document states it.
- **The fuselage stretch was driven partly by the engine's greater length.**
  The stretch is within three inches of the difference and the record attributes it to fuel.
- **That the reported Air Force concern about the F-15 was quantitatively reasonable.** The arithmetic
  is consistent with it, which is not the same as establishing it.

**Not established, and stated so.**

- Whether the aircraft would have reached Mach 2.6 at all.
- Whether the TF30 would have proved acceptable behind that inlet.
- What maximum lift coefficient the wing achieved, which is the weakest input above.
- Whether any of the manufacturer's estimates would have survived contact with a real airframe.

## Out of Scope

- **The F-104's accident record** in European service, which is a substantial subject of its own and
  bears on the Lancer only through the handling inheritance.
- **The full history of the Lightweight Fighter programme** and the YF-16 and YF-17, which belong with
  the articles on those designations.
- **The detailed design of the F-15**, referenced here only as the aircraft the Lancer was said to
  threaten.
- **The politics of foreign military sales** in the period, treated here only far enough to explain
  what the International Fighter Aircraft competition was for.
- **The CL-1400 and CL-1400N naval studies**, for which the public record is thinner still.
- **Boyd's biography and the wider reception of energy manoeuvrability**, which the references cover.

## Conclusion

**The X-27 was a designation attached to an aeroplane that did not exist, issued for a research purpose, in support of a commercial one.**

The technical question it named was real. A turbofan at Mach 2.6 behind an inlet descended from a Mach 2.0
turbojet installation, in an aluminium airframe, is a genuinely difficult proposition, and this article has
computed two specific reasons why.

**The inlet cannot meet the standard with one cone.** The best single-cone arrangement falls 11.44 points
short of the reference recovery at Mach 2.6, and that figure is a floor because the calculation charges
nothing for viscosity. Two ramps recover 8.18 of those points, which is why the X-27's intakes were to be
rectangular.

**The structure cannot hold its strength at that speed.** The recovery temperature at Mach 2.6 is 210.8
degrees Celsius, where the handbook gives 2024-T81 aluminium alloy about 68 percent of its yield strength after half an hour, and the skin reaches
nine-tenths of that in one minute, so a dash does not evade it.

**Against that, the aeroplane was a better fighter than the one that beat it.** On sustained turn rate and
on specific excess power the Lancer clears the F-5E comfortably at every assumption tested, and sits within
4.2 percent of the F-15A's specific excess power.
**The sales case was not fraudulent. It was simply not what the customers were buying**, which was cost,
logistics and an aircraft already in production.

**And one thing in the record checks out with a precision this subject has no right to.** Four inches of
spike travel, quoted as an airframe feature, and 260 pounds per second of airflow, quoted as an engine
rating, are reconciled by a twenty-five degree cone to within 4.2 percent.
**Nobody published that cone angle. Two numbers published for unrelated reasons agree through geometry connecting them, and that is the closest an aeroplane which never existed can come to leaving a measurement behind.**

The next article treats the [X-28][ref_x28], the Osprey Sea Skimmer, and returns to the pattern the X-27
broke, namely an aircraft that existed and flew.

## References

### Books

- [Ascher H. Shapiro 1953, The dynamics and thermodynamics of compressible...][book_shapiro]
- [Brian L. Stevens 2015, Aircraft Control and Simulation][book_stevens_lewis]
- [Daniel P. Raymer 1989, Aircraft Design][book_raymer]
- [Dennis R. Jenkins 2000, Hypersonics Before the Shuttle][book_jenkins]
- [Dietrich Küchemann 2012, The aerodynamic design of aircraft][book_kuchemann]
- [E. L. Goldsmith 1993, Practical intake aerodynamic design][book_seddon_goldsmith]
- [Gordon C. Oates 1984, Aerothermodynamics of gas turbine and rocket...][book_oates]
- [Jack D. Mattingly 1987, Aircraft engine design][book_mattingly_engine]
- [John Anderson 1982, Modern compressible flow][book_anderson]
- [Johnson, Clarence L. 1989, Kelly][book_johnson]
- [Leland M. Nicolai 2010, Fundamentals of aircraft and airship design][book_nicolai]
- [Ray Whitford 1987, Design for air combat][book_whitford]
- [Robert Coram 2002, Boyd][book_coram]
- [S F. Hoerner 1965, Fluid dynamic drag][book_hoerner]
- [Tony Buttler 2004, American Secret Projects][book_buttler]
- [William Green and Gordon Swanborough 1971, Air Enthusiast, Volume One][book_air_enthusiast_1971]

[book_air_enthusiast_1971]: https://openlibrary.org/works/OL26196651W
[book_anderson]: https://openlibrary.org/works/OL1993329W
[book_buttler]: https://openlibrary.org/works/OL9047733W
[book_coram]: https://openlibrary.org/works/OL4311885W
[book_hoerner]: https://openlibrary.org/works/OL10414729W
[book_jenkins]: https://openlibrary.org/works/OL38061876W
[book_johnson]: https://openlibrary.org/works/OL8538712W
[book_kuchemann]: https://openlibrary.org/works/OL22640504W
[book_mattingly_engine]: https://openlibrary.org/works/OL3739225W
[book_nicolai]: https://openlibrary.org/works/OL15909375W
[book_oates]: https://openlibrary.org/works/OL2752750W
[book_raymer]: https://openlibrary.org/works/OL3276227W
[book_seddon_goldsmith]: https://openlibrary.org/works/OL19054186W
[book_shapiro]: https://openlibrary.org/works/OL5908243W
[book_stevens_lewis]: https://openlibrary.org/works/OL21570717W
[book_whitford]: https://openlibrary.org/works/OL5054670W

### Reference

- [Aerodynamic heating and recovery temperature][ref_recovery_factor]
- [AIM-7 Sparrow][ref_aim7]
- [AIM-9 Sidewinder][ref_aim9]
- [Aircraft Handling Qualities Data, NASA CR-2144, Heffley and Jewell 1972][ref_heffley_jewell]
- [Aspect ratio of a wing][ref_aspect_ratio]
- [Breguet range equation][ref_breguet]
- [Clarence Kelly Johnson][ref_kelly_johnson]
- [Corrected mass flow rate][ref_corrected_flow]
- [DEFA cannon][ref_defa]
- [Dihedral and anhedral][ref_anhedral]
- [Eckert reference temperature method][ref_eckert]
- [Energy manoeuvrability theory][ref_energy_maneuverability]
- [Foreign Military Sales][ref_fms]
- [General Dynamics][ref_gd]
- [General Dynamics F-111 Aardvark][ref_f111]
- [General Dynamics YF-16][ref_yf16]
- [General Electric J79][ref_j79]
- [Grumman F-14 Tomcat][ref_f14]
- [Inconel][ref_inconel]
- [International Fighter Aircraft competition][ref_ifa]
- [International Standard Atmosphere][ref_isa]
- [John Boyd][ref_boyd]
- [Klaus Oswatitsch][ref_oswatitsch]
- [Lift-curve slope][ref_helmbold]
- [Lightweight Fighter program][ref_lwf]
- [Lockheed CL-1200 Lancer][ref_cl1200]
- [Lockheed F-104 Starfighter][ref_f104]
- [Lockheed Skunk Works][ref_skunk_works]
- [Lockheed SR-71 Blackbird][ref_sr71]
- [Lockheed X-27][ref_x27]
- [Lockheed X-27 specifications][ref_x27_specs]
- [M61 Vulcan][ref_m61]
- [Mach number][ref_mach]
- [McDonnell Douglas F-15 Eagle][ref_f15]
- [McDonnell Douglas F-4 Phantom II][ref_f4]
- [Metallic Materials and Elements for Aerospace Vehicle Structures, MIL-HDBK-5J, Department of Defense 2003][ref_mil_hdbk_5j]
- [Mock-up][ref_mockup]
- [NASA Technical Reports Server][ref_ntrs]
- [Normal shock wave][ref_normal_shock]
- [Northrop Corporation][ref_northrop]
- [Northrop F-5][ref_f5]
- [Northrop F-5E Tiger II][ref_f5e]
- [Northrop YF-17][ref_yf17]
- [Oblique shock][ref_oblique_shock]
- [Osprey X-28 Sea Skimmer][ref_x28]
- [Pitot intake][ref_pitot_inlet]
- [Prandtl number][ref_prandtl]
- [Pratt and Whitney TF30][ref_tf30]
- [Pressure recovery in an intake][ref_pressure_recovery]
- [Quest for Performance, NASA SP-468, Loftin 1985][ref_sp468]
- [Specific excess power][ref_specific_excess_power]
- [Stagnation pressure][ref_total_pressure]
- [Stagnation temperature][ref_total_temperature]
- [Stanton number][ref_stanton]
- [T-tail][ref_t_tail]
- [Taylor-Maccoll flow][ref_taylor_maccoll]
- [Thomas Christie][ref_christie]
- [Titanium alloy][ref_titanium]
- [Turbofan][ref_turbofan]
- [United States][ref_usa]
- [United States Air Force][ref_usaf]
- [United States Navy][ref_usn]
- [Vought F-8 Crusader][ref_f8]

[ref_aim7]: https://en.wikipedia.org/wiki/AIM-7_Sparrow
[ref_aim9]: https://en.wikipedia.org/wiki/AIM-9_Sidewinder
[ref_anhedral]: https://en.wikipedia.org/wiki/Dihedral_(aeronautics)
[ref_aspect_ratio]: https://en.wikipedia.org/wiki/Aspect_ratio_(aeronautics)
[ref_boyd]: https://en.wikipedia.org/wiki/John_Boyd_(military_strategist)
[ref_breguet]: https://en.wikipedia.org/wiki/Range_(aeronautics)
[ref_christie]: https://en.wikipedia.org/wiki/Thomas_P._Christie
[ref_cl1200]: https://en.wikipedia.org/wiki/Lockheed_CL-1200_Lancer
[ref_corrected_flow]: https://en.wikipedia.org/wiki/Corrected_flow
[ref_defa]: https://en.wikipedia.org/wiki/DEFA_cannon
[ref_eckert]: https://en.wikipedia.org/wiki/Ernst_R._G._Eckert
[ref_energy_maneuverability]: https://en.wikipedia.org/wiki/Energy%E2%80%93maneuverability_theory
[ref_f104]: https://en.wikipedia.org/wiki/Lockheed_F-104_Starfighter
[ref_f111]: https://en.wikipedia.org/wiki/General_Dynamics_F-111_Aardvark
[ref_f14]: https://en.wikipedia.org/wiki/Grumman_F-14_Tomcat
[ref_f15]: https://en.wikipedia.org/wiki/McDonnell_Douglas_F-15_Eagle
[ref_f4]: https://en.wikipedia.org/wiki/McDonnell_Douglas_F-4_Phantom_II
[ref_f5]: https://en.wikipedia.org/wiki/Northrop_F-5
[ref_f5e]: https://en.wikipedia.org/wiki/Northrop_F-5#F-5E_and_F-5F_Tiger_II
[ref_f8]: https://en.wikipedia.org/wiki/Vought_F-8_Crusader
[ref_fms]: https://en.wikipedia.org/wiki/Foreign_Military_Sales
[ref_gd]: https://en.wikipedia.org/wiki/General_Dynamics
[ref_heffley_jewell]: https://ntrs.nasa.gov/citations/19730003312
[ref_helmbold]: https://en.wikipedia.org/wiki/Lift_coefficient
[ref_ifa]: https://en.wikipedia.org/wiki/Military_Assistance_Program
[ref_inconel]: https://en.wikipedia.org/wiki/Inconel
[ref_isa]: https://en.wikipedia.org/wiki/International_Standard_Atmosphere
[ref_j79]: https://en.wikipedia.org/wiki/General_Electric_J79
[ref_kelly_johnson]: https://en.wikipedia.org/wiki/Kelly_Johnson_(engineer)
[ref_lwf]: https://en.wikipedia.org/wiki/Lightweight_Fighter_program
[ref_m61]: https://en.wikipedia.org/wiki/M61_Vulcan
[ref_mach]: https://en.wikipedia.org/wiki/Mach_number
[ref_mil_hdbk_5j]: https://everyspec.com/MIL-HDBK/MIL-HDBK-0001-0099/MIL_HDBK_5J_139/
[ref_mockup]: https://en.wikipedia.org/wiki/Mockup
[ref_normal_shock]: https://en.wikipedia.org/wiki/Shock_wave
[ref_northrop]: https://en.wikipedia.org/wiki/Northrop_Corporation
[ref_ntrs]: https://ntrs.nasa.gov/
[ref_oblique_shock]: https://en.wikipedia.org/wiki/Oblique_shock
[ref_oswatitsch]: https://de.wikipedia.org/wiki/Klaus_Oswatitsch
[ref_pitot_inlet]: https://en.wikipedia.org/wiki/Intake_ramp
[ref_prandtl]: https://en.wikipedia.org/wiki/Prandtl_number
[ref_pressure_recovery]: https://en.wikipedia.org/wiki/Components_of_jet_engines
[ref_recovery_factor]: https://en.wikipedia.org/wiki/Aerodynamic_heating
[ref_skunk_works]: https://en.wikipedia.org/wiki/Skunk_Works
[ref_sp468]: https://ntrs.nasa.gov/citations/19850023776
[ref_specific_excess_power]: https://en.wikipedia.org/wiki/Rate_of_climb
[ref_sr71]: https://en.wikipedia.org/wiki/Lockheed_SR-71_Blackbird
[ref_stanton]: https://en.wikipedia.org/wiki/Stanton_number
[ref_t_tail]: https://en.wikipedia.org/wiki/T-tail
[ref_taylor_maccoll]: https://en.wikipedia.org/wiki/Taylor%E2%80%93Maccoll_flow
[ref_tf30]: https://en.wikipedia.org/wiki/Pratt_%26_Whitney_TF30
[ref_titanium]: https://en.wikipedia.org/wiki/Titanium_alloy
[ref_total_pressure]: https://en.wikipedia.org/wiki/Stagnation_pressure
[ref_total_temperature]: https://en.wikipedia.org/wiki/Stagnation_temperature
[ref_turbofan]: https://en.wikipedia.org/wiki/Turbofan
[ref_usa]: https://en.wikipedia.org/wiki/United_States
[ref_usaf]: https://en.wikipedia.org/wiki/United_States_Air_Force
[ref_usn]: https://en.wikipedia.org/wiki/United_States_Navy
[ref_x27]: https://www.globalsecurity.org/military/systems/aircraft/x-27.htm
[ref_x27_specs]: https://www.globalsecurity.org/military/systems/aircraft/x-27-specs.htm
[ref_x28]: https://en.wikipedia.org/wiki/Osprey_Osprey_I
[ref_yf16]: https://en.wikipedia.org/wiki/General_Dynamics_F-16_Fighting_Falcon
[ref_yf17]: https://en.wikipedia.org/wiki/Northrop_YF-17

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
- [X-Planes: Lockheed X-7][related_post_a304_lockheed_x7]
- [X-Planes: Martin Marietta X-23 PRIME][related_post_a320_martin_marietta_x23]
- [X-Planes: Martin Marietta X-24][related_post_a321_martin_marietta_x24]
- [X-Planes: North American X-10][related_post_a307_north_american_x10]
- [X-Planes: North American X-15][related_post_a312_north_american_x15]
- [X-Planes: Northrop X-21][related_post_a318_northrop_x21]
- [X-Planes: Northrop X-4 Bantam][related_post_a301_northrop_x4]
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

### Research

- [2015][research_anon_2015]
- [2016][research_anon_2016]
- [2024][research_anon_2024]
- [A Canadian Light Fighter 1940][research_a_canadian_1940]
- [A Comparison of Cost 1977][research_a_comparison_1977]
- [A Conference on Thermal Stress 1954][research_a_conference_1954]
- [A New Fighter Aircraft 2003][research_a_new_2003]
- [A Study on Subcritical 2004][research_a_study_2004]
- [A.K. and P.S. 2018][research_ak_ps_2018]
- [Abate et al 2023][research_abate_vasista_2023]
- [Abbasi et al 2018][research_abbasi_pirnia_2018]
- [Abdel-Fattah 1996][research_abdelfattah_1996]
- [Abdelghany 2025][research_abdelghany_2025]
- [Abdelwahab 1977][research_abdelwahabm_1977]
- [Abdelwahab 1981][research_abdelwahabm_1981]
- [Abdolahipour et al 2022][research_abdolahipour_mani_2022]
- [Abdolahipour et al 2022][research_abdolahipour_mani_2022_b]
- [Abdul-Kaiyoom et al 2025][research_abdulkaiyoom_yildirim_2025]
- [Abdulhamitbilal et al 2021][research_abdulhamitbilal_sal_2021]
- [Abedi et al 2020][research_abedi_askari_2020]
- [Abedi et al 2020][research_abedi_askari_2020_b]
- [Abraham et al 2024][research_abraham_lazzara_2024]
- [Abrahamson 1988][research_abrahamson_1988]
- [Abu Salem et al 2023][research_abusalem_palaia_2023_b]
- [Adamczyk et al 2024][research_adamczyk_kozakiewicz_2024]
- [Adams et al 1984][research_adamsjcjr_martindalewr_1984]
- [Aerodynamic and Landing Measurements 1960][research_aerodynamic_and_1960]
- [Aerodynamic Drag in Cruising 2020][research_aerodynamic_drag_2020]
- [Afanas’ev et al 2019][research_afanasev_nikitin_2019]
- [Afridi et al 2024][research_afridi_khan_2024]
- [Agung Saputra et al 2026][research_agungsaputra_bhimashaktiarafat_2026]
- [Ahmad et al 2021][research_ahmad_zheng_2021]
- [Ahuja and Mavris 2022][research_ahuja_mavris_2022]
- [Air Force Research Lab Edwards Afb Ca 2000][research_airforceresearchlabedwardsafbca_2000]
- [Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Aircraft Drag 2010][research_aircraft_drag_2010]
- [Aircraft Performance 2010][research_aircraft_performance_2010]
- [Aircraft Steady Level Turning 2011][research_aircraft_steady_2011_c]
- [Aircraft Steady Turning Flight 2011][research_aircraft_steady_2011_d]
- [Aircraft, Basic Forces, and 1995][research_aircraft_basic_1995]
- [Ajay and Kundu 2025][research_ajay_kundu_2025]
- [Akhlaghi and Azizi 2023][research_akhlaghi_azizi_2023]
- [Akhlaghi et al 2022][research_akhlaghi_azizi_2022]
- [Al-Shamma et al 2017][research_alshamma_ali_2017]
- [Albuquerque et al 2018][research_albuquerque_gamboa_2018]
- [Aleisa et al 2023][research_aleisa_kontis_2023]
- [Alendar et al 2022][research_alendar_grunin_2022]
- [Alexander et al 1992][research_alexander_harris_1992]
- [Alford et al 1962][research_alford_davies_1962]
- [Ali et al 2017][research_ali_asghar_2017]
- [Ali et al 2025][research_ali_khan_2025]
- [Allen and Beke 1953][research_allen_beke_1953]
- [Allen and Mahorter 1964][research_allen_mahorter_1964]
- [Allen et al 1960][research_allen_davis_1960]
- [Allison et al 2015][research_allison_morris_2015]
- [Almuradi 2021][research_almuradi_2021]
- [Alone et al 2016][research_alone_kumar_2016]
- [Amann et al 1975][research_amann_nordenson_1975]
- [Amatucci et al 1982][research_amatucci_addy_1982]
- [Analysis of Anti-surge Control Method for Axial Flow Compressor 2021][research_analysis_of_2021]
- [Analysis of Flow Field Distortion in Ship Inlet System and Its Effect on Compressor Performance 2024][research_analysis_of_2024]
- [Anantachaisilp and Lin 2020][research_anantachaisilp_lin_2020]
- [Ananthapadmanaban and Murganandam 2016][research_ananthapadmanaban_murganandam_2016]
- [Anatomy of a turbofan engine 1970][research_anatomy_of_1970]
- [Anderson 1947][research_andersonadriene_1947]
- [Anderson 1984][research_anderson_1984]
- [Anderson 1985][research_anderson_1985]
- [Anderson 1989][research_anderson_1989]
- [Anderson and Bowditch 1958][research_andersonbh_bowditchdn_1958]
- [Anderson and Bray 1951][research_andersonsethb_brayrichards_1951]
- [Anderson and Bray 1955][research_andersonsethb_brayrichards_1955]
- [Anderson and Levy 1991][research_andersonbernhardh_levyralph_1991]
- [Anderson and Weir 2014][research_andersonbernhardh_weirlois_2014]
- [Anderson and Wong 1969][research_anderson_wong_1969]
- [Anderson et al 1957][research_anderson_dryer_1957]
- [Anderson et al 1960][research_andersonbh_bowditchdn_1960]
- [Anderson et al 1966][research_anderson_petersen_1966]
- [Anderson et al 1973][research_anderson_berger_1973]
- [Andrews 1969][research_andrews_1969]
- [Anglin 1978][research_anglin_1978]
- [Anglin and Satran 1980][research_anglin_satran_1980]
- [Anicetti 2023][research_anicetti_2023]
- [Ansari et al 2022][research_ansari_m_2022]
- [Antaran et al 1992][research_antaranalbert_beletehailu_1992]
- [Anti-Surge Control of Centrifugal Compressor and Implementation Strategy 2021][research_anti_surge_control_2021]
- [Anti-surge Reason and Control Technology of Large Centrifugal Compressor 2021][research_anti_surge_reason_2021]
- [Aoyagi and Hickey 1959][research_aoyagikiyoshi_hickeydavidh_1959]
- [Application of Centrifugal Compressor Control and Anti-surge System Control 2021][research_application_of_2021]
- [Application of PLC in Anti-surge Control System of Centrifugal Compressor 2021][research_application_of_2021_b]
- [Application Practice of Anti-surge Control in Compressor Transformation 2021][research_application_practice_2021]
- [Araújo et al 2021][research_araujo_pereira_2021]
- [Archbold 1945][research_archbold_1945]
- [Aribi and Boushaki 2023][research_aribi_boushaki_2023]
- [Arif et al 2021][research_arif_iftikhar_2021]
- [Arkoosh and Fiore 1972][research_arkoosh_fiore_1972]
- [Arlinger 1976][research_arlinger_1976]
- [Armstrong et al 1980][research_armstrong_palladino_1980]
- [Army War Coll Carlisle Barracks Pa 1952][research_armywarcollcarlislebarrackspa_1952]
- [Arnson et al 2026][research_arnson_aljaber_2026]
- [Arthur 2022][research_arthurw_2022]
- [Ashry et al 2019][research_ashry_kamel_2019]
- [Ashwood 1973][research_ashwood_1973]
- [Askari and Abedi 2026][research_askari_abedi_2026]
- [Askari and Soltani 2017][research_askari_soltani_2017]
- [Askari and Soltani 2019][research_askari_soltani_2019]
- [Askari and Soltani 2020][research_askari_soltani_2020]
- [Askari and Soltani 2022][research_askari_soltani_2022]
- [Askari and Soltani 2023][research_askari_soltani_2023]
- [Askari et al 2019][research_askari_soltani_2019_b]
- [Assessment of the Inlet/Engine][research_assessment_of]
- [Assessment of Total Pressure 2023][research_assessment_of_2023_b]
- [Atassi et al 2019][research_atassi_kozlov_2019]
- [Atesoglu and Özgören 2006][research_atesoglu_ozgoren_2006]
- [Atesoglu and Özgören 2007][research_atesoglu_ozgoren_2007]
- [Auman 1993][research_auman_1993]
- [Awerbuch 1980][research_awerbuch_1980]
- [Axelson and Crown 1948][research_axelsonjohna_crownjconrad_1948]
- [AXIAL TRANSONIC COMPRESSOR STALL MECHANISM WITH DIFFERENT ROTATIONAL SPEEDS 2022][research_axial_transonic_2022]
- [Ayers 1962][research_ayers_1962]
- [Ayres 1977][research_ayres_1977]
- [Azevedo et al 1990][research_azevedo_liu_1990]
- [Azizi and Brouwer 2017][research_azizi_brouwer_2017]
- [Babaei et al 2018][research_babaei_setayandeh_2018]
- [Babinsky 2014][research_babinsky_2014]
- [Babu 2021][research_babu_2021]
- [Babu 2021][research_babu_2021_b]
- [Back and Cuffel 1966][research_backlh_cuffelrf_1966]
- [Back et al 1967][research_back_massier_1967]
- [Background the Advanced Tactical 1998][research_background_the_1998]
- [Baerst and Hughes 1978][research_baerst_hughes_1978]
- [Bagby and Andersen 1966][research_bagby_andersen_1966]
- [Bai et al 2026][research_bai_deng_2026]
- [Baidya et al 2018][research_baidya_pesyridis_2018]
- [Baker 1966][research_baker_1966]
- [Bakhle et al 2018][research_bakhlemilinda_reddytsr_2018]
- [Balashov and Petukhov 1969][research_balashov_petukhov_1969]
- [Ball and Ross 1972][research_ball_ross_1972]
- [Balli and Caliskan 2021][research_balli_caliskan_2021]
- [Bammert and Mobarak 1976][research_bammert_mobarak_1976]
- [Bammert and Mobarak 1976][research_bammert_mobarak_1976_b]
- [Ban et al 2018][research_ban_yamazaki_2018]
- [Bangert et al 1980][research_bangert_santman_1980]
- [Bangert et al 1982][research_bangert_santman_1982]
- [Banks and Paulson 1987][research_banksdanielw_paulsonjohnwjr_1987]
- [Banks et al 1981][research_banks_quinto_1981]
- [Baretter et al 2021][research_baretter_godard_2021]
- [Barham 1994][research_barham_1994]
- [Barnhart 1988][research_barnhart_1988]
- [Baron 1953][research_baron_1953]
- [Barone et al 2022][research_barone_nicholson_2022]
- [Barr et al 2018][research_barr_ogara_2018]
- [Barr et al 2020][research_barr_muralidharan_2020]
- [Barry 1966][research_barry_1966]
- [Barry 1968][research_barryfw_1968]
- [Barry 1971][research_barry_1971]
- [Baryshev et al 1972][research_baryshev_vinogradov_1972]
- [Batayev et al 2022][research_batayev_suleimenov_2022]
- [Batterton et al 1974][research_battertonpg_arpasidj_1974]
- [Battiston et al 2025][research_battiston_magrini_2025]
- [Bauer and McMillin 1988][research_bauerstevenxs_mcmillinsnaomi_1988]
- [Bayati and Williston 1977][research_bayati_williston_1977]
- [Baydar et al 2016][research_baydarezgihan_lufrankk_2016]
- [Baydar et al 2017][research_baydarezgihan_lufrankk_2017]
- [Baydar et al 2018][research_baydar_lu_2018]
- [Beale and Miller 1975][research_beale_miller_1975]
- [Beaufrere 1988][research_beaufrere_1988]
- [Beck and Cord 1995][research_beck_cord_1995]
- [Beesly 1966][research_beesly_1966]
- [Beesly 1966][research_beesly_1966_b]
- [Behavior Patterns of Three 2022][research_behavior_patterns_2022]
- [Beheim and Gertsma 1956][research_beheimma_gertsmalw_1956]
- [Beke and Allen 1953][research_beke_allen_1953]
- [Benaouali and Kachel 2019][research_benaouali_kachel_2019]
- [Benichou et al 2021][research_benichou_binder_2021]
- [Bennet-Clark 1972][research_bennetclark_1972]
- [Bennett 1990][research_bennett_1990]
- [Bennett 2003][research_bennett_2003]
- [Benson 1994][research_benson_1994]
- [Benson 1997][research_bensonthomasj_1997]
- [Benson and Anderson 1983][research_benson_anderson_1983]
- [Benton et al 2021][research_benton_humphrey_2021]
- [Bera 1975][research_bera_1975]
- [Bera† 1980][research_bera_1980]
- [Berezovsky 2018][research_berezovsky_2018]
- [Bergstedt et al 1959][research_bergstedt_turner_1959]
- [Berto et al 2020][research_berto_benini_2020]
- [Bertram and Ulmann 1953][research_bertrammh_ulmannef_1953]
- [Bezborodova and Filinov 2021][research_bezborodova_filinov_2021]
- [Bhandari et al 2025][research_bhandari_gaur_2025]
- [Bhunia et al 2026][research_bhunia_abbas_2026]
- [Bianchi et al 2020][research_bianchi_secco_2020]
- [Bielat 1959][research_bielatralphp_1959]
- [Biesiadny and Wendt 2004][research_biesiadnythomasj_wendtbrucej_2004]
- [Biesiadny et al 1978][research_biesiadny_lee_1978]
- [Bihrle and Barnhart 1982][research_bihrle_barnhart_1982]
- [Bihrle and Billy 1980][research_bihrle_jr_1980]
- [Bilanin and Donaldson 1975][research_bilanin_donaldson_1975]
- [Bilwakesh et al 1971][research_bilwakeshkr_doylevl_1971]
- [Bilwakesh et al 1972][research_bilwakeshkr_kochcc_1972]
- [Birch et al 1978][research_birch_paynter_1978]
- [Bird et al 1952][research_birdjohnd_lichtensteinjacobh_1952]
- [Biriukov 1959][research_biriukov_1959]
- [Birkler 2001][research_birkler_2001]
- [Bisek 2014][research_bisek_2014]
- [Bisek 2015][research_bisek_2015]
- [Bisek et al 2012][research_bisek_rizzetta_2012]
- [Biswas et al 2026][research_biswas_michels_2026]
- [Blake et al 1990][research_blake_leggett_1990]
- [Blank and Shinar 1982][research_blank_shinar_1982]
- [Bleviss and Struble 1954][research_bleviss_struble_1954]
- [Bloxsom 1958][research_bloxsom_1958]
- [Bogar et al 1983][research_bogar_sajben_1983]
- [Bogdan 2015][research_bogdan_2015]
- [Boger and Nussbaum 1990][research_boger_nussbaum_1990]
- [Boger et al 1989][research_boger_greer_1989]
- [Bollech and Kelly 1954][research_bollechthomasv_kellyhneale_1954]
- [Bond and Key 2025][research_bond_key_2025]
- [Bond and Key 2026][research_bond_key_2026]
- [Bond et al 2025][research_bond_brown_2025]
- [Boussios et al 1992][research_boussios_epstein_1992]
- [Bouzekova-Penkova and Miteva 2022][research_bouzekovapenkova_miteva_2022]
- [Bowditch 1973][research_bowditch_1973]
- [Bowditch and Coltrin 1983][research_bowditchdn_coltrinre_1983]
- [Bowditch and Musial 1957][research_bowditch_musial_1957]
- [Bowers 1981][research_bowers_1981]
- [Boytos 1969][research_boytos_1969]
- [Braithwaite 1973][research_braithwaitewm_1973]
- [Braithwaite and Soeder 1979][research_braithwaitewm_soederrh_1979]
- [Braithwaite and Soeder 1980][research_braithwaite_soeder_1980]
- [Branger 1972][research_branger_1972]
- [Branstetter et al 1971][research_branstetterjr_juhaszaj_1971]
- [Brantley and Stabrylla 1979][research_brantley_stabrylla_1979]
- [Braun and Podleski 2019][research_braun_podleski_2019]
- [Bravo-Mosquera et al 2019][research_bravomosquera_abdalla_2019]
- [Breaks 1973][research_breaks_1973]
- [Breugelmans 1975][research_breugelmans_1975]
- [Briggs 1960][research_briggsbenjaminr_1960]
- [Brignac et al 1976][research_brignac_ness_1976]
- [Brilliant and Bauer 1977][research_brilliant_bauer_1977]
- [Brinich 1961][research_brinich_1961]
- [Briones and Rankin 2024][research_briones_rankin_2024]
- [Bristol Siddeley Viper Mark 1963][research_bristol_siddeley_1963]
- [Broadley et al 2023][research_broadley_hewitt_2023]
- [Brodrick 1976][research_brodrick_1976]
- [Brodsky 1970][research_brodsky_1970]
- [Brodzik 2024][research_brodzik_2024_b]
- [Brophy and Hawk 1990][research_brophy_hawk_1990]
- [Brown 1946][research_brownclintone_1946]
- [Brown 1959][research_brownstuartc_1959]
- [Brown 1961][research_brown_1961]
- [Brown 1970][research_brown_1970]
- [Browne et al 1948][research_browne_friedman_1948]
- [Bryant 1933][research_bryant_1933]
- [Bryson and Rumpfkeil 2019][research_bryson_rumpfkeil_2019]
- [Buchholz 1992][research_buchholzmarkd_1992]
- [Buchholz and Tso 1993][research_buchholzmarkd_tsojin_1993]
- [Bull and Bridges 1983][research_bullg_bridgespd_1983]
- [Bunton and Denegri 2000][research_bunton_denegri_2000]
- [Bureau Of Aeronautics Navy Washingtondc 1949][research_bureauofaeronauticsnavywashingtondc_1949]
- [Burkhalter 1982][research_burkhalter_1982]
- [Burns and Kirchgessner 1987][research_burns_kirchgessner_1987]
- [Burns et al 2015][research_burns_koo_2015]
- [Burris 1966][research_burris_1966]
- [Burrows et al 2025][research_burrows_vukasinovic_2025]
- [Burstadt and Calogeras 1974][research_burstadtpl_calogerasje_1974]
- [Burstadt and Wenzel 1976][research_burstadtpl_wenzellm_1976]
- [Burstadt et al 1971][research_burstadtpl_calogerasje_1971]
- [Burwell and Patterson 1985][research_burwell_patterson_1985]
- [Bush 1985][research_bush_1985]
- [Bushnell 1990][research_bushnell_1990]
- [Butler 1982][research_butler_1982]
- [Butter and Hancock 1971][research_butter_hancock_1971]
- [Buzica and Breitsamter 2020][research_buzica_breitsamter_2020]
- [Bykerk et al 2020][research_bykerk_verstraete_2020]
- [Caap and Elemeland 1986][research_caap_elemeland_1986]
- [Cabrera Cruz et al 2020][research_cabreracruz_pezzini_2020]
- [Caddy and Arnold 1988][research_caddy_arnold_1988]
- [Cai and Huang 2022][research_cai_huang_2022_c]
- [Cai et al 2022][research_cai_huang_2022]
- [Cai et al 2022][research_cai_huang_2022_b]
- [Callahan and Stenning 1971][research_callahan_stenning_1971]
- [Calligeros and Dugundji 1961][research_calligeros_dugundji_1961]
- [Calogeras and Burstadt 1974][research_calogerasje_burstadtpl_1974]
- [Calogeras and Coltrin 1969][research_calogerasje_coltrinre_1969]
- [Calogeras et al 1974][research_calogerasje_johnsenrl_1974]
- [Campbell 1976][research_campbell_1976]
- [Campbell and Ellis 1971][research_campbell_ellis_1971]
- [Campbell and Syberg 1984][research_campbell_syberg_1984]
- [Campbell et al 1985][research_campbell_syberg_1985]
- [Campion 1954][research_campion_1954]
- [Canard-Leading Edge Flap Scheduling 2007][research_canard_leading_edge_2007]
- [Cao and Zhang 2023][research_cao_zhang_2023]
- [Cao et al 2022][research_cao_yuan_2022]
- [Capello et al 2019][research_capello_ferrero_2019]
- [Capone 1979][research_capone_1979]
- [Capone and Berrier 1980][research_capone_berrier_1980]
- [Capone and Reubush 1983][research_caponefj_reubushde_1983]
- [Carew et al 1956][research_carew_crossley_1956]
- [Carey 1982][research_carey_1982]
- [Carlin et al 2003][research_carlincm_frischi_2003]
- [Carlson and Schwope 1952][research_carlson_schwope_1952]
- [Carlyle 1976][research_carlyle_1976]
- [Carnevale et al 2016][research_carnevale_wang_2016]
- [Carreyette 1950][research_carreyette_1950]
- [Carrier et al 2001][research_carrier_knight_2001]
- [Cassetti 1978][research_cassetti_1978]
- [Casteel and Weyl 1970][research_casteel_weyl_1970]
- [Castner et al 2017][research_castner_zaman_2017]
- [Castner et al 2018][research_castner_simerly_2018]
- [Castor 1983][research_castor_1983]
- [Cate 2003][research_cate_2003]
- [Cervay 1972][research_cervay_1972]
- [Cervay 1975][research_cervay_1975]
- [Cess 1964][research_cess_1964]
- [Cevik et al 2016][research_cevik_ducvo_2016]
- [Chai et al 2017][research_chai_song_2017]
- [Chai et al 2020][research_chai_li_2020]
- [Chambers and Bowman 1971][research_chambers_bowman_1971]
- [Chaney 1999][research_chaney_1999]
- [Chang and Hsu 1960][research_chang_hsu_1960]
- [Chang et al 1953][research_chang_nordheim_1953]
- [Chapman 1979][research_chapman_1979]
- [Chapman et al 2005][research_chapmandave_smithcf_2005]
- [Che Idris et al 2020][research_cheidris_saad_2020]
- [Cheikh and Chen 2017][research_cheikh_chen_2017]
- [Chell et al 2021][research_chell_hoffenson_2021]
- [Chen and He 2025][research_chen_he_2025]
- [Chen and Li 2020][research_chen_li_2020]
- [Chen and Tan 2019][research_chen_tan_2019]
- [Chen and Xia 2022][research_chen_xia_2022]
- [Chen et al 1987][research_chengt_greitzerem_1987]
- [Chen et al 2013][research_chen_wang_2013]
- [Chen et al 2017][research_chen_tan_2017]
- [Chen et al 2018][research_chen_tan_2018]
- [Chen et al 2019][research_chen_tan_2019_b]
- [Chen et al 2020][research_chen_mi_2020]
- [Chen et al 2020][research_chen_zhang_2020]
- [Chen et al 2021][research_chen_chen_2021]
- [Chen et al 2021][research_chen_mi_2021]
- [Chen et al 2021][research_chen_yue_2021]
- [Chen et al 2021][research_chen_zhang_2021_b]
- [Chen et al 2022][research_chen_mi_2022]
- [Chen et al 2023][research_chen_chen_2023]
- [Chen et al 2024][research_chen_zhu_2024]
- [Chen et al 2025][research_chen_martinez_2025]
- [Chen et al 2025][research_chen_sethuraman_2025]
- [Chen et al 2025][research_chen_yang_2025]
- [Chen et al 2026][research_chen_wu_2026]
- [Chen et al 2026][research_chen_zheng_2026]
- [Cheng et al 2016][research_cheng_yue_2016]
- [Cheng et al 2024][research_cheng_huang_2024]
- [Chennuru et al 2025][research_chennuru_corral_2025]
- [Chester 1953][research_chester_1953]
- [Chi et al 2022][research_chi_chu_2022]
- [Child and Henderson 1978][research_childrd_hendersonwp_1978]
- [Chima 2011][research_chima_2011]
- [Chima 2011][research_chima_2011_b]
- [Chima 2011][research_chimarodrickv_2011]
- [Chima 2012][research_chimarodrickv_2012]
- [Chima et al 2009][research_chima_conners_2009]
- [Chima et al 2010][research_chima_conners_2010]
- [Chima et al 2011][research_chimarodrickv_hirtstefaniem_2011]
- [Chin 1977][research_chin_1977]
- [Chin 1978][research_chin_1978]
- [Cho and Findley 1983][research_cho_findley_1983]
- [Choe and Kim 2016][research_choe_kim_2016]
- [Choe et al 2020][research_choe_kim_2020]
- [Choi 2024][research_choi_2024]
- [Choi 2026][research_choi_2026]
- [Choi et al 2026][research_choi_choi_2026]
- [Chou][research_chou]
- [Chou and Smith 1974][research_chou_smith_1974]
- [Chun and Burr 1969][research_chun_burr_1969]
- [Chun and Swanson 1964][research_chun_swanson_1964]
- [Chung 1994][research_chung_1994]
- [Ciepluch 1948][research_ciepluchcarlc_1948]
- [Clark 1995][research_clark_1995]
- [Clark and Richie 1977][research_clarkle_richiecb_1977]
- [Clarke and Wallace 1964][research_clarke_wallace_1964]
- [Cliett 1952][research_cliett_1952]
- [Coalson 1968][research_coalson_1968]
- [Coalson and Csavina 1976][research_coalson_csavina_1976]
- [Coble et al 2014][research_coble_royster_2014]
- [Coe 1976][research_coepljr_1976]
- [Coe and Kulla 1974][research_coe_kulla_1974]
- [Coen and Foss 1985][research_coen_foss_1985]
- [Colbourne 1980][research_colbourne_1980]
- [Cole 1980][research_colejb_1980]
- [Coltrin 1987][research_coltrin_1987]
- [Composite material comprising reinforced aluminium or aluminium-base alloy 1978][research_composite_material_1978]
- [Concept Designed and Developed 1995][research_concept_designed_1995]
- [Cong et al 2024][research_cong_yu_2024]
- [Conners and Howe 2006][research_conners_howe_2006]
- [Connors and Wise 1957][research_connorsjamesf_wisegeorgea_1957]
- [Connors et al 1957][research_connors_lovell_1957]
- [Connors et al 1957][research_jamesfconnors_georgeawise_1957]
- [Control system design using frequency domain models and parameter optimization with application to supersonic inlet controls 1976][research_control_system_1976]
- [Conway et al 2010][research_conway_lavely_2010]
- [Conway et al 2011][research_conway_lavely_2011]
- [Cook 1965][research_cook_1965]
- [Coordinated Turning Flights of 1995][research_coordinated_turning_1995]
- [Corcione et al 2023][research_corcione_bonavolonta_2023]
- [Cord 1989][research_cord_1989]
- [Cordeaux 1991][research_cordeaux_1991]
- [Cordner 1967][research_cordner_1967]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornellaeronauticallabincbuffalony_1947]
- [Corner 1940][research_corner_1940]
- [Cortright 1951][research_cortrightedgarmjr_1951]
- [Cossar et al 1980][research_cossar_moffatt_1980]
- [Costakis 1974][research_costakiswg_1974]
- [Costakis 1975][research_costakiswg_1975]
- [Cowles 1981][research_cowles_1981]
- [Craidon 1986][research_craidoncb_1986]
- [Crane 1948][research_craneharoldl_1948]
- [Crane and Beckhardt 1948][research_craneharoldl_beckhardtarnoldr_1948]
- [Crea et al 2025][research_crea_marty_2025]
- [Crites et al 1992][research_crites_rueger_1992]
- [Crosthwait 1970][research_crosthwait_1970]
- [Crowe 1936][research_crowe_1936]
- [Crowe 1937][research_crowe_1937]
- [Crown 1950][research_crown_1950]
- [Cubbison 1977][research_cubbison_1977]
- [Cui et al 2024][research_cui_zhang_2024]
- [Cummings et al 2018][research_cummings_liersch_2018]
- [Cumpsty and Greitzer 1982][research_cumpsty_greitzer_1982]
- [Cunis et al 2020][research_cunis_condomines_2020]
- [Da et al 2020][research_da_hanan_2020]
- [da Fonseca Filho et al 2019][research_dafonsecafilho_gamaribeiro_2019]
- [Dahlberg 1963][research_dahlberg_1963]
- [Dai and Zhang 2023][research_dai_zhang_2023]
- [Dai et al 2023][research_dai_boughazi_2023]
- [Dai et al 2023][research_dai_zhao_2023]
- [Daliri et al 2018][research_daliri_farahani_2018]
- [Daniele and Teren 1975][research_daniele_teren_1975]
- [Daniele and Teren 1975][research_danielecj_terenf_1975]
- [Das and Prasad 2023][research_das_prasad_2023]
- [Dashora and Sasidharan 2024][research_dashora_sasidharan_2024]
- [Davidson 1964][research_davidson_1964]
- [Davis 1952][research_davis_1952]
- [Davis 1971][research_davis_1971]
- [Davis 1973][research_davis_1973]
- [Davis 1973][research_davis_1973_b]
- [Davis 1973][research_davis_1973_c]
- [Davis 1973][research_davis_1973_d]
- [Davis et al 1972][research_davisra_elrodsd_1972]
- [Davis et al 2012][research_davisdavido_vyasmanana_2012]
- [Davoudzadeh et al 1987][research_davoudzadeh_liu_1987]
- [Day et al 1978][research_day_greitzer_1978]
- [Day et al 1978][research_day_greitzer_1978_b]
- [de Paula et al 2017][research_depaula_porto_2017]
- [Dean and Young 1977][research_dean_young_1977]
- [Debogdan et al 1975][research_debogdance_dicusjh_1975]
- [Debogdan et al 1977][research_debogdance_mossjejr_1977]
- [Deese and Agarwal 1983][research_deese_agarwal_1983]
- [Degree Turning Performance][research_degree_turning]
- [Dehner et al 2021][research_dehner_selamet_2021]
- [Dehua and Changyou 1993][research_dehua_changyou_1993]
- [Deitchman 1953][research_deitchman_1953]
- [Deitchman 1954][research_deitchman_1954]
- [Demir et al 2023][research_demir_gorguluarslan_2023]
- [Deng et al 2026][research_deng_li_2026]
- [Denner et al 1998][research_denner_mccallum_1998]
- [Department Of Defense Washington Dc 1997][research_departmentofdefensewashingtondc_1997]
- [Desai et al 1977][research_desai_viswanathan_1977]
- [Design and Numerical Analysis of E-D Nozzle with Throat Radius Investigation in Supersonic Flows: A Comparison Study with Tic Nozzle 2024][research_design_and_2024]
- [Design sheets for New 2003][research_design_sheets_2003]
- [Desyatnik 2015][research_desyatnik_2015]
- [Development of an Improved Elevated Temperature Aluminium Alloy Alcan GBX158 1975][research_development_of_1975]
- [Development Testing of the RB.211 Turbofan Engine 1970][research_development_testing_1970]
- [Deyoung 1950][research_deyoungjohn_1950]
- [Di Bianchi et al 2018][research_dibianchi_orra_2018]
- [Di-Marco et al 2023][research_dimarco_jacob_2023]
- [Diamantidou et al 2022][research_diamantidou_hosain_2022]
- [Dias 2023][research_dias_2023]
- [Dickey 1959][research_dickeyrobertr_1959]
- [Dickman and Takahashi 2016][research_dickman_takahashi_2016]
- [Dicus 1975][research_dicus_1975]
- [Dietz and Bailey 1973][research_dietz_bailey_1973]
- [Diggins 1951][research_diggins_1951]
- [Ding 2023][research_ding_2023]
- [Ding et al 2015][research_ding_shen_2015]
- [Ding et al 2020][research_ding_wang_2020]
- [Ding et al 2024][research_ding_chen_2024]
- [Diphda and Wiswayana 2026][research_diphda_wiswayana_2026]
- [Dippold 2022][research_vancefdippoldiii_2022]
- [Discussion on Anti-surge Control System of Centrifugal Compressor 2021][research_discussion_on_2021_b]
- [Discussion on Control Points of Surge and Anti-surge of Centrifugal Compressor 2021][research_discussion_on_2021]
- [Discussion on the Anti-surge Control Method and Realization Path of Axial Flow Compressor 2021][research_discussion_on_2021_d]
- [Discussion on the Application of Anti-surge Intelligent Control for Centrifugal Compressor 2021][research_discussion_on_2021_c]
- [Dixon et al 1961][research_dixonsidneyc_griffithgeorgee_1961]
- [Di̇şli̇taş and Albayrak Çeper 2021][research_dislitas_albayrakceper_2021]
- [Dobeš et al 2019][research_dobes_dymacek_2019]
- [Dodds and Vahdati 2015][research_dodds_vahdati_2015]
- [Dodds and Vahdati 2015][research_dodds_vahdati_2015_b]
- [Doggett and Soistmann 1989][research_doggettrobertvjr_soistmanndavidl_1989]
- [Dolling 1982][research_dolling_1982]
- [Dollyhigh and Foss 1985][research_dollyhigh_foss_1985]
- [Dong et al 2015][research_dong_sun_2015]
- [Dong et al 2018][research_dong_sun_2018]
- [Dong et al 2020][research_dong_choi_2020]
- [Dong et al 2022][research_dong_choi_2022]
- [Dong et al 2025][research_dong_liu_2025]
- [Dong et al 2026][research_dong_wang_2026]
- [Donlan 1976][research_donlancj_1976]
- [Dowell and Ventres 1970][research_dowell_ventres_1970]
- [Drewes 1987][research_drewes_1987]
- [Driver 1958][research_drivercornelius_1958]
- [Dryer and Beke 1952][research_dryer_beke_1952]
- [Du 2026][research_du_2026]
- [Du et al 2023][research_du_liu_2023]
- [Du et al 2025][research_du_zhang_2025]
- [Duan et al 2026][research_duan_wan_2026]
- [Duan et al 2026][research_duan_zhao_2026]
- [Duddy et al 2020][research_duddy_landucci_2020]
- [Dudley 1986][research_dudley_1986]
- [Due 1987][research_due_1987]
- [Dugan 1972][research_duganjfjr_1972]
- [Dugas 1968][research_dugas_1968]
- [Duncheva et al 2020][research_duncheva_maximov_2020]
- [Dunham 1962][research_dunham_1962]
- [Durmus 2021][research_durmus_2021]
- [Durston and Stonum 1987][research_durston_stonum_1987]
- [Duvall and Arnaiz 1977][research_duvall_arnaiz_1977]
- [Dvirnyk et al 2019][research_dvirnyk_pavlenko_2019]
- [Eberhardt 2005][research_eberhardt_2005]
- [Eberle and Fowler 1971][research_eberle_fowler_1971]
- [Ebied et al 2018][research_ebied_hamada_2018]
- [Edahl and Domack 2004][research_edahl_domack_2004]
- [Edwards 2010][research_edwards_2010]
- [Effect of Different Radial Inclined Angles of Self-circulation Casing Treatment on the Transonic Axial Flow Compressor Performance 2023][research_effect_of_2023_b]
- [Effect of Exhaust Jet from Takeoff Aircraft on the Inlet Distortion of Runway-Crossing Aircraft 2024][research_effect_of_2024]
- [Effect of inlet Mach number on performance and flow structure of an axial supersonic through-flow fan cascade 2023][research_effect_of_2023]
- [Egan and Shadowen 1979][research_egan_shadowen_1979]
- [Egorov et al 2011][research_egorov_neiland_2011]
- [El-Sayed 2026][research_elsayed_2026]
- [Ellis and Brownstein 1974][research_ellis_brownstein_1974]
- [Emmons et al 1955][research_emmons_pearson_1955]
- [Emmons et al 1955][research_emmons_pearson_1955_b]
- [Englert and Obery 1952][research_englertgeraldw_oberyleonardj_1952]
- [Enzinger 1988][research_enzinger_1988]
- [Epstein 1954][research_epstein_1954]
- [Erich 1980][research_erich_1980]
- [Erickson and Campbell 1977][research_erickson_campbell_1977]
- [Erickson and Campbell 1977][research_erickson_campbell_1977_b]
- [Esau 2024][research_esau_2024]
- [Esenwein and Schueller 1952][research_esenweinfredt_schuellercarlf_1952]
- [Esser and Ruff-Stahl 2021][research_esser_ruffstahl_2021]
- [Et.al 2021][research_numerical_simulation_2021]
- [Eulrich and Mesiah 1974][research_eulrich_mesiah_1974]
- [Evaluation of Various Flow Control Methods in Reducing Drag and Aerodynamic Heating on the Nose of Hypersonic Flying Objects 2024][research_evaluation_of_2024]
- [Evans and Chamblee 1966][research_evans_chamblee_1966]
- [Evans et al 1974][research_evansdg_debogdance_1974]
- [Evvard 1947][research_evvardjohnc_1947]
- [Experimental Study of the Unstart/Restart Process of a Two-Dimensional Supersonic Inlet Induced by Backpressure 2022][research_experimental_study_2022]
- [Experimental Study on the High-Temperature Creep Behavior of Super Alloy Using Digital Image Correlation 2020][research_experimental_study_2020]
- [Ezrokhi and Khoreva 2018][research_ezrokhi_khoreva_2018]
- [F-104 Resource Tape 1992][research_f_104_resource_1992]
- [Falk et al 1998][research_falk_jumper_1998]
- [Falk et al 2001][research_falk_jumper_2001]
- [Faltin and Beneda 2023][research_faltin_beneda_2023]
- [Fan et al 2024][research_fan_liu_2024]
- [Fan et al 2025][research_fan_du_2025]
- [Fan et al 2026][research_fan_li_2026]
- [Fan et al 2026][research_fan_xu_2026]
- [Fan et al 2026][research_fan_xu_2026_b]
- [Fang and Wang 2023][research_fang_wang_2023]
- [Fang et al 2022][research_fang_zhang_2022]
- [Fang et al 2023][research_fang_sun_2023]
- [Fang et al 2023][research_fang_sun_2023_b]
- [Farahani and Mahdavi 2019][research_farahani_mahdavi_2019]
- [Farahani et al 2019][research_farahani_daliri_2019]
- [Farhat et al 2000][research_farhat_harris_2000]
- [Farr 1976][research_farr_1976]
- [Felix et al 2026][research_felix_perron_2026]
- [Fellers and Patierno 1970][research_fellers_patierno_1970]
- [Feng et al 2020][research_feng_tao_2020]
- [Feng et al 2022][research_feng_tianyu_2022]
- [Feng et al 2025][research_feng_chen_2025]
- [Ferrar et al 2016][research_ferrar_schneck_2016]
- [Ferrari 1958][research_ferrari_1958]
- [Ferrero 2020][research_ferrero_2020]
- [Ferri and Nucci 1946][research_ferriantonio_nuccilouism_1946]
- [Ferri and Nucci 1951][research_ferriantonio_nuccilouism_1951]
- [Fett 1971][research_fett_1971]
- [Figge 1973][research_figge_1973]
- [Fighter and Attack Aircraft 2008][research_fighter_and_2008]
- [Fine 1959][research_fine_1959]
- [Fine and Weertman 1983][research_fine_weertman_1983]
- [Fink and Anderson 1983][research_fink_anderson_1983]
- [Fischer and Norris 1949][research_fischer_norris_1949]
- [Fisher and Williams 1958][research_fisherlewisr_williamsjamesl_1958]
- [Flanagan 1992][research_flanaganmichaelj_1992]
- [Fleeter et al 1974][research_fleeter_mcclure_1974]
- [Flow Field Study of Mixed Compression Supersonic Air Intake with Cowl Ventilation 2020][research_flow_field_2020]
- [Flow structure and parameter evaluation of conical convergent-divergent nozzle supersonic jet flows 2023][research_flow_structure_2023]
- [Forsythe et al 1998][research_forsythe_hoffmann_1998]
- [Foss 1981][research_foss_1981]
- [Foss 1984][research_foss_1984]
- [Foster and Fitzpatrick 1948][research_fostergeraldv_fitzpatrickjamese_1948]
- [Fradenburgh and Wyatt 1953][research_fradenburgh_wyatt_1953]
- [Fraiser 1960][research_fraiser_1960]
- [Franciscus 1987][research_franciscusleoc_1987]
- [Franck et al 2012][research_franck_lewis_2012]
- [François et al 2021][research_francois_probst_2021]
- [Frey 2014][research_frey_2014]
- [Friend and Sakamoto 1978][research_friendel_sakamotogm_1978]
- [Friend and Sefic 1972][research_friend_sefic_1972]
- [Frohnapfel et al 2017][research_frohnapfel_obrien_2017]
- [Frohnapfel et al 2018][research_frohnapfel_mack_2018]
- [Frohnapfel et al 2018][research_frohnapfel_toddlowe_2018]
- [Frohnapfel et al 2021][research_frohnapfel_tlowe_2021]
- [Fu et al 2021][research_fu_fu_2021]
- [Fu et al 2021][research_fu_fu_2021_b]
- [Fujii et al 2021][research_fujii_fujimori_2021]
- [Fujimoto and Niwa 1993][research_fujimoto_niwa_1993]
- [Fuller 1967][research_fullerde_1967]
- [Fundamentals of Fighter Design 2001][research_fundamentals_of_2001]
- [Fuqun et al 1985][research_fuqun_wenlan_1985]
- [Furukawa et al 2015][research_furukawa_yamada_2015]
- [Gabriel et al 1953][research_gabrieldavids_krebsrichardp_1953]
- [Gadeev et al 2017][research_gadeev_demakov_2017]
- [Gaglio et al 2023][research_gaglio_visone_2023]
- [Gahlot and Singh 2019][research_gahlot_singh_2019]
- [Galindo et al 2022][research_galindo_climent_2022]
- [Galkin and Sergeev 1976][research_galkin_sergeev_1976]
- [Ganilova et al 2021][research_ganilova_cartmell_2021]
- [Ganilova et al 2022][research_ganilova_cartmell_2022]
- [Gao et al 2015][research_gao_li_2015]
- [Gao et al 2017][research_gao_liu_2017]
- [Gartling 1970][research_gartling_1970]
- [GAS Turbine Engine Inlet][research_gas_turbine]
- [Gates 1940][research_gates_1940]
- [Ge et al 2021][research_ge_shang_2021]
- [Gedeon and Takahashi 2014][research_gedeon_takahashi_2014]
- [Gehring and Engle 1963][research_gehring_engle_1963]
- [Gelder 1957][research_gelderthomasf_1957]
- [Gellatly and Gallagher 1964][research_gellatly_gallagher_1964]
- [Gellatly et al 1965][research_gellatly_bijlaard_1965]
- [Geng et al 2025][research_geng_yang_2025]
- [Ghaffari 2005][research_ghaffarifarhad_2005]
- [Ghee et al 1999][research_ghee_gonzalez_1999]
- [Gilbert et al 1976][research_gilbert_nguyen_1976]
- [Gilinsky et al 2000][research_gilinskymikhail_morganmorrish_2000]
- [Gill and Sain 1981][research_gill_sain_1981]
- [Gillen and Loth 2011][research_gillen_loth_2011]
- [Gillen and Loth 2015][research_gillen_loth_2015]
- [Gillespie 1960][research_gillespiewarrenjr_1960]
- [Gilman and Burdges 1967][research_gilman_burdges_1967]
- [Gilruth and White 1941][research_gilruthrr_whitemd_1941]
- [Giuliano 2016][research_giuliano_2016]
- [Gleason and Martone 1980][research_gleason_martone_1980]
- [Glenn and Koch 1973][research_glenn_koch_1973]
- [Gliszczyński et al 2021][research_gliszczynski_czechowski_2021]
- [Glorioso 1960][research_glorioso_1960]
- [Gloss 1974][research_glossbb_1974]
- [Go and Wilshire 1992][research_go_wilshire_1992]
- [Goldberg and Boxer 1959][research_goldberg_boxer_1959]
- [Golombek et al 2026][research_golombek_bustamante_2026]
- [Golovin 1982][research_golovin_1982]
- [Golubkin 1980][research_golubkin_1980]
- [Golubkin 1980][research_golubkin_1980_b]
- [Goodman 1949][research_goodman_1949]
- [Goonko and Mazhul 2011][research_goonko_mazhul_2011]
- [Goranson 1942][research_goransonrfabian_1942]
- [Gorbovskoi et al 2019][research_gorbovskoi_kazhan_2019]
- [Gorton 1953][research_gortongeraldc_1953]
- [Gorton 1954][research_gortongeraldc_1954]
- [Goto et al 2021][research_goto_nakayama_2021]
- [Goud and Dwivedi 2022][research_goud_dwivedi_2022]
- [Goulos et al 2021][research_goulos_otter_2021]
- [Gounko and Mazhul 2012][research_gounko_mazhul_2012]
- [Graham et al 1954][research_graham_lagerstrom_1954]
- [Gray 1969][research_gray_1969]
- [Gray and Martins 2018][research_gray_martins_2018]
- [Gray et al 2017][research_grayjustins_madercharlesa_2017]
- [Gray et al 2020][research_gray_mader_2020]
- [Gregory and Wilcox 1970][research_gregorytj_wilcoxde_1970]
- [Greitzer 1972][research_greitzer_1972]
- [Greitzer 1976][research_greitzer_1976]
- [Greitzer 1976][research_greitzer_1976_b]
- [Greitzer 1976][research_greitzer_1976_c]
- [Greitzer 1980][research_greitzer_1980]
- [Grenson and Beneddine 2018][research_grenson_beneddine_2018]
- [Gridnev 1991][research_gridnev_1991]
- [Griffin 2012][research_griffin_2012]
- [Griffin et al 1958][research_griffinroynjr_holzhausercurta_1958]
- [Grimshaw et al 2025][research_grimshaw_pullan_2025]
- [Gringorten and Tattelman 1970][research_gringorten_tattelman_1970]
- [Groth 1961][research_groth_1961]
- [Grytsyshen et al 2025][research_grytsyshen_abramova_2025]
- [Gu et al 2023][research_gu_xu_2023]
- [Guan and Yarng 1984][research_guan_yarng_1984]
- [Guan and Yarng 1987][research_guan_yarng_1987]
- [Guan et al 2019][research_guan_zhou_2019]
- [Guang et al 2014][research_guang_ping_2014]
- [Guang et al 2015][research_guang_deming_2015]
- [Guderley 1987][research_guderley_1987]
- [Guderley 1988][research_guderley_1988]
- [Gudmundsson 2014][research_gudmundsson_2014]
- [Guidelines for Characterization of][research_guidelines_for]
- [Guimaraes et al 2015][research_guimaraes_lowe_2015]
- [Guimarães et al 2018][research_guimaraes_lowe_2018]
- [Guimarães et al 2018][research_guimaraes_toddlowe_2018]
- [Guo 2023][research_guo_2023]
- [Guo et al 2021][research_guo_hu_2021]
- [Guo et al 2021][research_guo_tian_2021]
- [Guo et al 2022][research_guo_gao_2022]
- [Guo et al 2022][research_guo_mao_2022]
- [Guo et al 2024][research_guo_zhang_2024]
- [Guo et al 2025][research_guo_liu_2025]
- [Gupta and Ramkumar 2015][research_gupta_ramkumar_2015]
- [Gur et al 2010][research_gur_mason_2010]
- [Gutiérrez Álvarez and Bisagni 2021][research_gutierrezalvarez_bisagni_2021]
- [Götten et al 2021][research_gotten_havermann_2021]
- [Gözükara and Ceylan 2024][research_gozukara_ceylan_2024]
- [Güllü and Aran 2023][research_gullu_aran_2023]
- [Günaydın and Doğu 2025][research_gunaydin_dogu_2025]
- [Gürbüz and Acarer 2022][research_gurbuz_acarer_2022]
- [Haas and Karanian 1981][research_haas_karanian_1981]
- [Hackman and Richardson 1964][research_hackman_richardson_1964]
- [Haering and Burcham 1984][research_haering_burcham_1984]
- [Hah 2018][research_hah_2018]
- [Hah 2022][research_hah_2022]
- [Hall and Heitmeyer 1951][research_hallcharlesf_heitmeyerjohnc_1951]
- [Hall et al 1997][research_hall_hamilton_1997]
- [Hall et al 2017][research_hall_greitzer_2017]
- [Hall et al 2022][research_hall_greitzer_2022]
- [Hall et al 2022][research_hall_greitzer_2022_b]
- [Halwas and Aggarwal 2019][research_halwas_aggarwal_2019]
- [Halwas and Aggarwal 2019][research_halwas_aggarwal_2019_b]
- [Hamaguchi et al 2020][research_hamaguchi_sakata_2020]
- [Hamed 1993][research_hamed_1993]
- [Hamed 1995][research_hamed_1995]
- [Hamilton et al 1997][research_hamilton_hall_1997]
- [Han and Seo 2016][research_han_seo_2016]
- [Hanazaki and Yamazaki 2024][research_hanazaki_yamazaki_2024]
- [Hancock 1959][research_hancock_1959]
- [Hancock 1959][research_hancock_1959_b]
- [Hancock 1960][research_hancock_1960]
- [Hancock 1985][research_hancockjp_1985]
- [Hansen 1972][research_hansen_1972]
- [Hansen et al 1981][research_hansen_jorgensen_1981]
- [Hantrais-Gervois and Destarac 2015][research_hantraisgervois_destarac_2015]
- [Hao et al 2024][research_hao_liu_2024]
- [Harish et al 2017][research_m_v_2017]
- [Harle 1979][research_harle_1979]
- [Harloff and Smith 1995][research_harloff_smith_1995]
- [Harman 1978][research_harman_1978]
- [Harold and Haefeli 1950][research_harold_haefeli_1950]
- [Harper and Robert P. 1955][research_harper_robertp_1955]
- [Hartley et al 1965][research_hartley_furey_1965]
- [Hartmann 1968][research_hartmann_1968]
- [Hartsell 1960][research_hartsell_1960]
- [Hasel et al 1953][research_hasellowelle_lankfordjohnl_1953]
- [Hashin and Humphreys 1980][research_hashin_humphreys_1980]
- [Hawk and Wilsdorf 1988][research_hawk_wilsdorf_1988]
- [Hawkins and Penland 1997][research_hawkinsrichard_penlandjima_1997]
- [Hawkins et al 1976][research_hawkinsje_kirklandfp_1976]
- [Hawks 1982][research_hawks_1982]
- [Hawthorne et al 1955][research_hawthorne_wood_1955]
- [Hawthorne et al 1978][research_hawthorne_mitchell_1978]
- [Hayden and Untaroiu 2021][research_hayden_untaroiu_2021]
- [Hayden et al 2023][research_hayden_gillespie_2023]
- [Hayes and Sleeman 1959][research_hayeswcjr_sleemanwcjr_1959]
- [He and Shi 2025][research_he_shi_2025]
- [He and Zhang 2025][research_he_zhang_2025]
- [He et al 2026][research_he_xie_2026]
- [Heath et al 2016][research_heath_slater_2016]
- [Heath-Smith 1965][research_heathsmith_1965]
- [Hebbar et al 1991][research_hebbar_platzer_1991]
- [Heimerl and Hardrath 1965][research_heimerlgeorgej_hardrathherbertf_1965]
- [Heiss et al 1992][research_heiss_eberle_1992]
- [Hellemeier 2019][research_hellemeier_2019]
- [Helmbold 1958][research_helmbold_1958]
- [Heltsley and Crosswy 1983][research_heltsley_crosswy_1983]
- [Henderson 1965][research_henderson_1965]
- [Herbst 1980][research_herbst_1980]
- [Herbst and Krogull 1973][research_herbst_krogull_1973]
- [Hernandez et al 1994][research_hernandezgloria_woodrichardm_1994]
- [Herrick 1986][research_herrick_1986]
- [Herwig 2000][research_herwig_2000]
- [Hess 1986][research_hess_1986]
- [Hewes 1950][research_hewesdonalde_1950]
- [Hickman and Morris 2017][research_hickman_morris_2017]
- [Hicks and Huckabine 1989][research_hicks_huckabine_1989]
- [Higham and Holley 1966][research_higham_holley_1966]
- [Hild and Crocker 2006][research_hild_crocker_2006]
- [Hild and Crocker 2006][research_hild_crocker_2006_b]
- [Hild and Crocker 2008][research_hild_crocker_2008]
- [Hill and Bowles 1976][research_hillgc_bowlesjv_1976]
- [Hill and Defoe 2020][research_hill_defoe_2020]
- [Hillier 1970][research_hillier_1970]
- [Hitzel and Osterhuber 2018][research_hitzel_osterhuber_2018]
- [Hobbs et al 1996][research_hobbs_spaid_1996]
- [Hodder 1981][research_hodderbk_1981]
- [Hodder et al 1981][research_hodderbk_farquharbw_1981]
- [Hodge et al 1985][research_hodge_taylor_1985]
- [Hodge et al 1986][research_hodge_taylor_1986]
- [Hoerner 1936][research_hoerner_1936]
- [Hoerter et al 1991][research_hoerter_powers_1991]
- [Hoffler et al 1986][research_hofflerkd_raodm_1986]
- [Hoffman 2000][research_hoffmantr_2000]
- [Hoffman and Stalford 1991][research_hoffman_stalford_1991]
- [Holdaway et al 1959][research_holdawaygeorgeh_lazzeronifranka_1959]
- [Holl 1975][research_holl_1975]
- [Hom et al 1983][research_hom_morris_1983]
- [Hon et al 2022][research_hon_karpuk_2022]
- [Honeycutt 1970][research_honeycutt_1970]
- [Hongpeng and Weiqiang 2016][research_hongpeng_weiqiang_2016]
- [Hopkins 1975][research_hopkinsej_1975]
- [Horton 1954][research_horton_1954]
- [Horton et al 1951][research_hortonelmera_loftinlaurencek_1951]
- [Horvath and Wells 2018][research_brycelhorvath_douglaspwells_2018]
- [Hosseindokht et al 2026][research_hosseindokht_matas_2026]
- [Hosseini et al 2024][research_hosseini_vaziryzanjany_2024]
- [Hou et al 2017][research_hou_wang_2017]
- [Howard et al 1951][research_howard_luidens_1951]
- [Howerton and Slater][research_howerton_slater]
- [Howlett and Hunter 1986][research_howlett_hunter_1986]
- [Hrubecky 1963][research_hrubecky_1963]
- [Hsu and Anderson 1961][research_hsu_anderson_1961]
- [Hu 2024][research_hu_2024]
- [Hu et al 2023][research_hu_qu_2023]
- [Hu et al 2024][research_hu_li_2024]
- [Huang et al 2016][research_huang_tan_2016]
- [Huang et al 2019][research_huang_zhang_2019]
- [Huang et al 2026][research_huang_wang_2026]
- [Hubble and Smith 1979][research_hubble_smith_1979]
- [Hube 1968][research_hube_1968]
- [Hughes and Johnson 1972][research_hughes_johnson_1972]
- [Hughes and Mackall 1984][research_hughesdl_mackallkg_1984]
- [Hui 1975][research_hui_1975]
- [Hunn 1954][research_hunn_1954]
- [Hunt and Gowadia 1981][research_hunt_gowadia_1981]
- [Hunt and Hunt 2021][research_hunt_hunt_2021]
- [Hunziker 1960][research_hunziker_1960]
- [Huppert 1955][research_huppert_1955]
- [Huppert and Benser 1953][research_huppert_benser_1953]
- [Hurley 1951][research_hurley_1951]
- [Hutchinson et al 2021][research_hutchinson_lawrence_2021]
- [Hwang and Pi 1979][research_hwang_pi_1979]
- [Hwang et al 1980][research_hwang_johnson_1980]
- [Hövelmann and Breitsamter 2015][research_hovelmann_breitsamter_2015]
- [Hövelmann et al 2016][research_hovelmann_grawunder_2016]
- [Ichikawa et al 2021][research_ichikawa_koike_2021]
- [Iek et al 1993][research_iekchanthy_burleyrichardr_1993]
- [Iliff 1977][research_iliff_1977]
- [Iliff et al 1970][research_iliff_smith_1970]
- [Imani et al 2017][research_imani_jahedmotlagh_2017]
- [Imani et al 2018][research_imani_malekizade_2018]
- [Imig 1973][research_imig_1973]
- [INFLUENCE OF BACK PRESSURE ON THE FLOW IN THE DIFFUSER OF A SUPERSONIC AIR INLET 2017][research_influence_of_2017]
- [Inger 1986][research_inger_1986]
- [Inger and Zee 1978][research_inger_zee_1978]
- [Inglis and Larke 1958][research_inglis_larke_1958]
- [Initial Damage Mechanism of Nickel-Based Alloy 625 Under Creep Loadings at Elevated Temperatures 2019][research_initial_damage_2019]
- [Inlet Total-Pressure-Distortion Considerations for][research_inlet_total_pressure_distortion]
- [Irsyad Lukman and Agoes Moelyadi 2018][research_irsyadlukman_agoesmoelyadi_2018]
- [Irwanto 2017][research_irwanto_2017]
- [Iseki and Nicholas 1979][research_iseki_nicholas_1979]
- [Islam et al 2015][research_islam_fermin_2015]
- [Isugiyama 1976][research_isugiyama_1976]
- [Ivanov 2022][research_ivanov_2022]
- [Jack 1951][research_jackjohnr_1951]
- [Jackson 1980][research_jackson_1980]
- [Jacocks and Kneile 1975][research_jacocks_kneile_1975]
- [Jain 2025][research_ajain_2025]
- [Jain and Liang 2020][research_jain_liang_2020]
- [Jakubowski 2019][research_jakubowski_2019]
- [James and Kim 2022][research_kjames_kim_2022]
- [James et al 2021][research_kjames_suryan_2021]
- [Jaquet 1951][research_jaquetbyronm_1951]
- [Jayakrishnan and Pant 2005][research_jayakrishnan_pant_2005]
- [Jeans and Tribble 1979][research_jeans_tribble_1979]
- [Jeans et al 1983][research_jeans_grimes_1983]
- [Jeffs and Lancaster 2015][research_jeffs_lancaster_2015]
- [Jelev et al 2019][research_jelev_keane_2019]
- [Jenista and Bodden 1989][research_jenista_bodden_1989]
- [Jenkins 1979][research_jenkinsjm_1979]
- [Jenkins and Kuhl 1977][research_jenkinsjeraldm_kuhlalberte_1977]
- [Jenney 1935][research_jenney_1935]
- [Ji et al 2021][research_ji_yuan_2021]
- [Ji et al 2022][research_ji_hu_2022]
- [Ji et al 2024][research_ji_huang_2024]
- [Jia et al 2024][research_jia_chen_2024]
- [Jiali and Jihong 2015][research_jiali_jihong_2015]
- [Jiao et al 2017][research_jiao_chang_2017]
- [Jin et al 2022][research_jin_sun_2022]
- [Jin et al 2023][research_jin_tan_2023]
- [Jin et al 2023][research_jin_zhang_2023]
- [Johns 1998][research_johns_1998]
- [Johnson 1972][research_johnson_1972]
- [Johnson and Adcock 1981][research_johnson_adcock_1981]
- [Johnson and Lawing 1977][research_johnson_lawing_1977]
- [Johnson and Montoya 1973][research_johnsonhj_montoyaej_1973]
- [Johnson and Wu 1975][research_johnson_wu_1975]
- [Johnson et al 1959][research_johnson_henderson_1959]
- [Johnson et al 1960][research_johnson_henderson_1960]
- [Johnson III and Wu 1974][research_johnsoniii_wu_1974]
- [Jones 1953][research_jonesrobertt_1953]
- [Jones 1956][research_jonesrobertt_1956]
- [Jones 1972][research_jones_1972]
- [Jones 1973][research_jones_1973]
- [Jones 1976][research_jonesrt_1976]
- [Jones and Unangst 1963][research_jonesgwjr_unangstjr_1963]
- [Jones et al 1947][research_jonesarthurl_flanaganmildredg_1947]
- [Jones et al 2020][research_gregorysjones_williammilholen_2020]
- [Jules and Barnhart 1998][research_jules_barnhart_1998]
- [Jung et al 2015][research_jung_lee_2015]
- [Ka 2018][research_ka_2018]
- [Kaczorowski et al 2015][research_kaczorowski_skoczylas_2015]
- [Kalkan 2024][research_kalkan_2024]
- [Kamman and Hall 1975][research_kamman_hall_1975]
- [Kang et al 2024][research_kang_kang_2024]
- [Kang et al 2024][research_kang_li_2024]
- [Kang et al 2024][research_kang_liang_2024]
- [Kaplan 1980][research_kaplan_1980]
- [Kapoor et al 1992][research_kapoor_pai_1992]
- [Kapoor et al 1994][research_kapoorkamlesh_andersonbernhardh_1994]
- [Karabacak and Turan 2020][research_karabacak_turan_2020]
- [Karimi and Oboodi 2018][research_karimi_oboodi_2018]
- [Karl et al 2025][research_karl_werner_2025]
- [Karniadakis 2004][research_karniadakis_2004]
- [Karol and Hatch 1969][research_karol_hatch_1969]
- [Kast 1980][research_kast_1980]
- [Katz 1971][research_katz_1971]
- [Kawamura and Karashima 1957][research_kawamura_karashima_1957]
- [Kawamura et al 1987][research_kawamurat_chyuwj_1987]
- [Kawase and Rona 2019][research_kawase_rona_2019]
- [Kawase and Rona 2019][research_kawase_rona_2019_b]
- [Kaye and Yeh 1955][research_kaye_yeh_1955]
- [Kayser and Danberg 1974][research_kayser_danberg_1974]
- [Kazula and Höschler 2020][research_kazula_hoschler_2020]
- [Kazula and Höschler 2021][research_kazula_hoschler_2021]
- [Kazula et al 2019][research_kazula_mischke_2019]
- [Kbab et al 2023][research_kbab_haif_2023]
- [Kelley 1975][research_kelley_1975]
- [Kelley 1975][research_kelley_1975_b]
- [Kelley and Tolhurst 1955][research_kelleymarkw_tolhurstwilliamhjr_1955]
- [Kelly et al 1958][research_kellymarkw_andersonsethb_1958]
- [Kennon 1989][research_kennon_1989]
- [Keppler 1966][research_keppler_1966]
- [Khademi et al 2019][research_khademi_ikeda_2019]
- [Khaleghi 2015][research_khaleghi_2015]
- [Khalid 2025][research_khalid_2025]
- [Khan and Hasan 2021][research_khan_hasan_2021]
- [Khatri and Sinha 2023][research_khatri_sinha_2023]
- [Khobragade and Kumar 2022][research_khobragade_kumar_2022]
- [Khobragade et al 2021][research_khobragade_unnikrishnan_2021]
- [Khobragade et al 2024][research_khobragade_gustavsson_2024]
- [Kholyavko 1971][research_kholyavko_1971]
- [Kida and Miyai 1978][research_kida_miyai_1978]
- [Kigotho et al 2022][research_kigotho_bodylski_2022]
- [Kim 2024][research_kim_2024]
- [Kim and Kwon 2015][research_kim_kwon_2015]
- [Kim and Lee 2022][research_kim_lee_2022]
- [Kim and Park 2026][research_kim_park_2026]
- [Kim et al 2011][research_kimhyoungjin_kumanotakayasu_2011]
- [Kim et al 2015][research_kim_kim_2015_b]
- [Kim et al 2022][research_kim_choi_2022]
- [Kim et al 2026][research_kim_kim_2026]
- [Kinard et al 1995][research_kinardtima_harrisbrendaw_1995]
- [King et al 1976][research_kingrw_schuermanja_1976]
- [Kinsler 1958][research_kinslermartinr_1958]
- [Kish et al 2019][research_kish_wilde_2019]
- [Kishi et al 2022][research_kishi_kanazaki_2022]
- [Kiss and Spakovszky 2018][research_kiss_spakovszky_2018]
- [Kitowski 1986][research_kitowski_1986]
- [Klann et al 1984][research_klannga_barthrl_1984]
- [Kleckner 1945][research_klecknerharoldf_1945]
- [Kleckner 1946][research_klecknerharoldf_1946]
- [Klein 1999][research_kleinvladislav_1999]
- [Klein and Abeykoon 2015][research_klein_abeykoon_2015]
- [Kohn 1964][research_kohn_1964]
- [Kohn 1979][research_kohn_1979]
- [Kolnsberg 1979][research_kolnsberg_1979]
- [Kolom 1969][research_kolom_1969]
- [Kong and Park 2018][research_kong_park_2018]
- [Kong et al 2017][research_kong_jiang_2017]
- [Kong et al 2022][research_kong_li_2022]
- [Kong et al 2026][research_kong_su_2026]
- [Kopasakis et al 2012][research_kopasakisgeorge_connollyjosephw_2012]
- [Kopasakis et al 2012][research_kopasakisgeorge_connollyjosephw_2012_b]
- [Kopzon 1958][research_kopzon_1958]
- [Korn 1974][research_korn_1974]
- [Korn 1974][research_korn_1974_b]
- [Kostin and Zhuravskiy 2023][research_kostin_zhuravskiy_2023]
- [Kosuge et al 1982][research_kosuge_ito_1982]
- [Kothari 1971][research_kothari_1971]
- [Kothari 1973][research_kothari_1973]
- [Kotov et al 2018][research_kotov_ruleva_2018]
- [Kovács et al 2023][research_kovacs_csik_2023]
- [Koyyalamudi and Nagpurwala 2016][research_koyyalamudi_nagpurwala_2016]
- [Kozakiewicz et al 2025][research_kozakiewicz_adamczyk_2025]
- [Kraiko and Tilliaeva 1973][research_kraiko_tilliaeva_1973]
- [Kramer and Hall 2026][research_kramer_hall_2026]
- [Kramer and Potter 1966][research_kramerbe_potterdy_1966]
- [Krashchenko and Statsenko 1981][research_krashchenko_statsenko_1981]
- [Krause 1981][research_krause_1981]
- [Krebs 1976][research_krebs_1976]
- [Krenkel and Salzman 1968][research_krenkel_salzman_1968]
- [Kretov 2021][research_kretov_2021]
- [Krivec et al 1984][research_krivec_ling_1984]
- [Krivenyuk et al 1971][research_krivenyuk_tsvilyuk_1971]
- [Krupa 2019][research_krupa_2019]
- [Krushnarao Kotteda and Mittal 2016][research_krushnaraokotteda_mittal_2016]
- [Kuchar and Wolf 1993][research_kuchar_wolf_1993]
- [Kuchinka 1966][research_kuchinka_1966]
- [Kumar 1999][research_kumar_1999]
- [Kumar 2022][research_kumar_2022]
- [Kumar and Pradeep 2022][research_kumar_pradeep_2022]
- [Kumar et al 2022][research_kumar_dwivedi_2022]
- [Kumazaki and Shimamura 2026][research_kumazaki_shimamura_2026]
- [Kun et al 2018][research_kun_tingting_2018]
- [Kurganov 2006][research_kurganov_2006]
- [Kurkov et al 1975][research_kurkov_soeder_1975]
- [Kursakov et al 2016][research_kursakov_kazhan_2016]
- [Kurtenbach 1978][research_kurtenbach_1978]
- [Kutschera and Render 1999][research_kutschera_render_1999]
- [Kutschera and Render 2003][research_kutschera_render_2003]
- [Kuz'mich et al 1975][research_kuzmich_sekundov_1975]
- [Kuzmin 2024][research_kuzmin_2024]
- [Kwak et al 2013][research_kwak_lee_2013]
- [Kwiatkowski et al 2022][research_kwiatkowski_sieradzki_2022]
- [Kwon and Sankar 1991][research_kwon_sankar_1991]
- [Kwon and Sankar 1992][research_kwon_sankar_1992]
- [Küçük and Tuncer 2024][research_kucuk_tuncer_2024]
- [L'Ecuyer et al 1971][research_lecuyer_morrison_1971]
- [Laderman 2021][research_laderman_2021]
- [Lai and Findley 1980][research_lai_findley_1980]
- [Lai and Kamaruddin 2018][research_lai_kamaruddin_2018]
- [Laitone 1978][research_laitone_1978]
- [Lamar 1986][research_lamarje_1986]
- [Lamar 1987][research_lamarjohne_1987]
- [Lambert and Mizukami 1999][research_lamberthh_mizukamim_1999]
- [Lampropoulos and Sarris 2025][research_lampropoulos_sarris_2025]
- [Lane and Behenna 1991][research_lane_behenna_1991]
- [Langan and Samuels 1995][research_langan_samuels_1995]
- [Langener et al 2009][research_langener_myrabo_2009]
- [Langham 1978][research_langham_1978]
- [Lapin et al 1952][research_lapin_crookshanks_1952]
- [Large 1981][research_large_1981]
- [Larrabee 1975][research_larrabeeee_1975]
- [Larson 1960][research_larson_1960_d]
- [Latham 1976][research_latham_1976]
- [Latham 2020][research_latham_2020]
- [Latham et al 1977][research_latham_gawienowski_1977]
- [Lawley and Koczak 1984][research_lawley_koczak_1984]
- [Lawley and Koczak 1985][research_lawley_koczak_1985]
- [Lawrence 1953][research_lawrence_1953]
- [Leadon and Scott 1956][research_leadon_scott_1956]
- [Lee 1998][research_leeja_1998]
- [Lee 2003][research_leejonathana_2003]
- [Lee and Boedicker 1985][research_lee_boedicker_1985]
- [Lee and Chen 2002][research_leejonathana_chenposhou_2002]
- [Lee and Chen 2005][research_jonathanalee_poshouchen_2005]
- [Lee and Franz 1976][research_lee_franz_1976]
- [Lee and Kim 2024][research_lee_kim_2024]
- [Lee and Ko 2018][research_lee_ko_2018]
- [Lee and Liou 2018][research_leebyungjoon_lioumayfun_2018]
- [Lee and Munafo 2002][research_leejonathana_munafopaulm_2002]
- [Lee and Sanders 2002][research_lee_sanders_2002]
- [Lee et al 2010][research_lee_ahn_2010]
- [Lee et al 2016][research_lee_lee_2016]
- [Lee et al 2018][research_leebj_lioumayfun_2018]
- [Lee et al 2019][research_lee_lee_2019]
- [Lee et al 2019][research_leebyungjoon_lioumayfun_2019]
- [Lehtinen and Zeller 1971][research_lehtinenb_zellerjr_1971]
- [Lehtinen and Zeller 1972][research_lehtinen_zeller_1972]
- [Lehtinen et al 1978][research_lehtinenb_zellerjr_1978]
- [Leinhos et al 2000][research_leinhos_schmid_2000]
- [Leissler and Nettles 1954][research_leissler_nettles_1954]
- [Lemay et al 1988][research_lemaysp_batillsm_1988]
- [Leng et al 2024][research_leng_feng_2024]
- [Lengyel-Kampmann et al 2024][research_lengyelkampmann_karboujian_2024]
- [Leontiev et al 2017][research_leontiev_lushchik_2017]
- [Leontiev et al 2017][research_leontiev_popovich_2017]
- [Leontiev et al 2022][research_leontiev_lushchik_2022]
- [Leslie 1952][research_leslie_1952]
- [Leslie and Perry 1954][research_leslie_perry_1954]
- [Lesser and Niehuis 2014][research_lesser_niehuis_2014]
- [Levin 1997][research_levin_1997]
- [Levy 1959][research_levylionelljr_1959]
- [Levy and Yoshikawa 1959][research_levylionelljr_yoshikawakennethk_1959]
- [Lewis 1976][research_lewis_1976]
- [Lewis 2002][research_lewis_2002]
- [Li and Geiselhart 2020][research_wuli_karlgeiselhart_2020]
- [Li and Geiselhart 2021][research_li_geiselhart_2021]
- [Li and Geiselhart 2022][research_li_geiselhart_2022]
- [Li and Geiselhart 2026][research_li_geiselhart_2026]
- [Li and Sun 2022][research_li_sun_2022]
- [Li et al 2015][research_li_pan_2015]
- [Li et al 2015][research_li_xu_2015]
- [Li et al 2019][research_li_du_2019]
- [Li et al 2019][research_li_soskin_2019]
- [Li et al 2020][research_li_du_2020]
- [Li et al 2020][research_li_du_2020_b]
- [Li et al 2021][research_li_dong_2021]
- [Li et al 2021][research_li_tian_2021]
- [Li et al 2021][research_li_zheng_2021]
- [Li et al 2022][research_li_dong_2022]
- [Li et al 2022][research_li_liu_2022]
- [Li et al 2022][research_li_zhu_2022]
- [Li et al 2023][research_li_ding_2023]
- [Li et al 2023][research_li_zheng_2023]
- [Li et al 2023][research_li_zhu_2023]
- [Li et al 2024][research_li_chen_2024]
- [Li et al 2024][research_li_chu_2024]
- [Li et al 2024][research_li_hou_2024]
- [Li et al 2024][research_li_li_2024]
- [Li et al 2024][research_li_liu_2024]
- [Li et al 2024][research_li_liu_2024_b]
- [Li et al 2024][research_li_lu_2024]
- [Li et al 2024][research_li_xia_2024]
- [Li et al 2024][research_li_xu_2024]
- [Li et al 2024][research_li_zhu_2024]
- [Li et al 2024][research_li_zhu_2024_b]
- [Li et al 2025][research_li_dong_2025]
- [Li et al 2025][research_li_qu_2025]
- [Li et al 2025][research_li_sun_2025]
- [Li et al 2026][research_li_zhao_2026]
- [Lian et al 2025][research_lian_xiong_2025]
- [Liang and Zhang 1989][research_liang_zhang_1989]
- [Lichtenstein 1952][research_lichtensteinjacobh_1952]
- [Liddell 1950][research_liddell_1950]
- [Liew et al 2005][research_liewkh_uripe_2005]
- [Likhachev 2024][research_likhachev_2024]
- [Lin 1982][research_lin_1982]
- [Lin 1982][research_lin_1982_b]
- [Lin et al 2020][research_lin_shao_2020]
- [Lin et al 2021][research_lin_liu_2021]
- [Lin et al 2022][research_lin_bai_2022]
- [Lin et al 2026][research_lin_zong_2026]
- [Linden 2022][research_linden_2022]
- [Linnell 1963][research_linnell_1963]
- [Liou and Benson 2010][research_liou_benson_2010]
- [Liu and Cao 2017][research_liu_cao_2017]
- [Liu and Jiang 2022][research_liu_jiang_2022]
- [Liu and Sirignano 2000][research_liu_sirignano_2000]
- [Liu and Vo 2024][research_liu_vo_2024]
- [Liu et al 2015][research_liu_zhu_2015]
- [Liu et al 2016][research_liu_li_2016]
- [Liu et al 2016][research_liu_zhu_2016]
- [Liu et al 2021][research_liu_wang_2021]
- [Liu et al 2022][research_liu_kang_2022]
- [Liu et al 2022][research_liu_li_2022]
- [Liu et al 2022][research_liu_zhang_2022]
- [Liu et al 2023][research_liu_huang_2023]
- [Liu et al 2023][research_liu_li_2023]
- [Liu et al 2024][research_liu_chu_2024]
- [Liu et al 2024][research_liu_zhu_2024]
- [Liu et al 2025][research_liu_chu_2025]
- [Liu et al 2025][research_liu_du_2025]
- [Liu et al 2025][research_liu_zhu_2025]
- [Liu et al 2025][research_liu_zhu_2025_b]
- [Liu et al 2026][research_liu_du_2026]
- [Liu et al 2026][research_liu_zhu_2026]
- [Lock 1957][research_lock_1957]
- [Lockwood 1966][research_lockwoodve_1966]
- [Loh and Lusty 1974][research_loh_lusty_1974]
- [Lokotko and Kharitonov 2006][research_lokotko_kharitonov_2006]
- [Lomax 1957][research_lomaxharvard_1957]
- [Lomax and Heaslet 1956][research_lomaxharvard_heasletmaxa_1956]
- [Lorell 1989][research_lorell_1989]
- [Loren et al 1992][research_loren_kerr_1992]
- [Loth et al 2016][research_loth_candon_2016]
- [Lou et al 2022][research_lou_harrison_2022]
- [Lourenco et al 1996][research_lourenco_shih_1996]
- [Loveless and Boswell 1954][research_loveless_boswell_1954]
- [Lovell 2001][research_lovell_2001]
- [Lovell and Wilson 1947][research_lovelljcalvin_wilsonherbertajr_1947]
- [Lowe 2020][research_lowe_2020]
- [Lu et al 2019][research_lu_yang_2019]
- [Lu et al 2025][research_lu_li_2025]
- [Lu et al 2025][research_lu_wang_2025]
- [Lu-ning et al 2021][research_luning_bangqin_2021]
- [Lucas 1978][research_lucas_1978]
- [Lucas et al 2014][research_lucas_obrien_2014]
- [Luce 1949][research_luce_jr_1949]
- [Ludwig 1979][research_ludwig_1979]
- [Lukyanov et al 2024][research_lukyanov_hoang_2024]
- [Lunde 1977][research_lundet_1977]
- [Lundell et al 1961][research_lundell_scherrer_1961]
- [Luo et al 2020][research_luo_wei_2020]
- [Luo et al 2024][research_luo_tao_2024]
- [Luo et al 2026][research_luo_meng_2026]
- [Luo Ju 2009][research_luoju_2009]
- [Lypchanskyi et al 2024][research_lypchanskyi_janus_2024]
- [Lyubimov 2024][research_lyubimov_2024]
- [Lyubimov and Potekhina 2016][research_lyubimov_potekhina_2016]
- [Ma 2021][research_ma_2021]
- [Ma et al 2018][research_ma_cui_2018]
- [Ma et al 2025][research_ma_li_2025]
- [Ma et al 2025][research_ma_lu_2025]
- [Ma et al 2025][research_ma_wang_2025]
- [Ma et al 2025][research_ma_yang_2025]
- [Ma et al 2026][research_ma_li_2026]
- [MacInnis 1994][research_macinnis_1994]
- [MacManus et al 2017][research_macmanus_chiereghin_2017]
- [Madelung 1977][research_madelung_1977]
- [Maekawa et al 1978][research_maekawa_higashi_1978]
- [Maghsoudi et al 2020][research_maghsoudi_vaziry_2020]
- [Magrini and Benini 2023][research_magrini_benini_2023]
- [Magrini and Benini 2026][research_magrini_benini_2026]
- [Mahlmeister et al 1955][research_mahlmeister_ishimoto_1955]
- [Mahorter and Robert G. 1961][research_mahorter_robertg_1961]
- [Maikapar 1959][research_maikapar_1959]
- [Maikapar 1966][research_maikapar_1966]
- [Maise 1970][research_maise_1970]
- [Maitra 2010][research_maitra_2010]
- [Maki 1959][research_makiralphl_1959]
- [Maksimovich et al 1977][research_maksimovich_karpinos_1977]
- [Malan and Brown 1994][research_malan_brown_1994]
- [Malashenko and Vashchilo 1975][research_malashenko_vashchilo_1975]
- [Malcolm and Ng 1991][research_malcolm_ng_1991]
- [Malicki et al 2023][research_malicki_malecha_2023]
- [Malikov and Miltsov 2019][research_malikov_miltsov_2019]
- [Malmuth 1966][research_malmuth_1966]
- [Malmuth et al 1987][research_malmuth_wu_1987]
- [Malone and Peavey 1999][research_malonemichaelb_peaveycharlesc_1999]
- [Malvi and Roy 2021][research_malvi_roy_2021]
- [Mamonova et al 2019][research_mamonova_soudakov_2019]
- [Mancini and Vos 2019][research_mancini_vos_2019]
- [Mann and Garner 1977][research_mann_garner_1977]
- [Manolescu 1994][research_manolescu_1994]
- [Mansfield 1967][research_mansfield_1967]
- [Mao and Liu 2016][research_mao_liu_2016]
- [Mao and Zhang 2025][research_mao_zhang_2025]
- [Mao et al 2017][research_mao_liu_2017]
- [Maples 1979][research_maples_1979]
- [Margalida et al 2020][research_margalida_joseph_2020]
- [Margolis 1947][research_margoliskenneth_1947]
- [Margolis et al 1958][research_margoliskenneth_malvestutofranksjr_1958]
- [Marshall 1971][research_marshallrt_1971]
- [Marshall 1973][research_marshall_1973]
- [Marshall and Schweikhard 1973][research_marshall_schweikhard_1973]
- [Martin and Brazzel 1970][research_martin_brazzel_1970]
- [Marty et al 2022][research_marty_castillon_2022]
- [Marvin 1968][research_marvin_1968]
- [Masaki et al 2021][research_masaki_ogushi_2021]
- [Mascitti 1966][research_mascitti_1966]
- [Mascitti 1969][research_mascitti_1969]
- [Mason 1983][research_masonwh_1983]
- [Mason et al 1983][research_masonwh_siclarimj_1983]
- [Mathauser and Deveikis 1955][research_mathausereldone_deveikiswilliamd_1955]
- [Mathauser and Deveikis 1957][research_mathausereldone_deveikiswilliamd_1957]
- [Mathur 1998][research_mathur_1998]
- [Matranga and Armstrong 1959][research_matrangagenej_armstrongneila_1959]
- [Matsumoto and Sekiya 1975][research_matsumoto_sekiya_1975]
- [Mauch et al 1980][research_mauch_oldakowski_1980]
- [Mayer and Paynter 1994][research_mayer_paynter_1994]
- [Mays 1971][research_mays_1971]
- [Mazhul 2020][research_mazhul_2020]
- [Mazurov 2015][research_mazurov_2015]
- [Mazurov 2019][research_mazurov_2019]
- [Mazzawy and Banks 1976][research_mazzawyrs_banksga_1976]
- [Mazzawy and Banks 1977][research_mazzawyrs_banksga_1977]
- [McAulay and Abdelwahab 1972][research_mcaulayje_abdelwahabm_1972]
- [McClure and Sirbaugh 1991][research_mcclure_sirbaugh_1991]
- [McCormick 1959][research_mccormick_1959]
- [McGuigan 1970][research_mcguigan_1970]
- [McKeehen and Cord 1997][research_mckeehen_cord_1997]
- [McLemore 1958][research_mclemorehclyde_1958]
- [McLemore and Peterson 1960][research_mclemorehclyde_petersonjohnbjr_1960]
- [McMillin and Wood 1986][research_mcmillinsn_woodrm_1986]
- [McQueen 1976][research_mcqueen_1976]
- [McVey et al 1969][research_mcvey_rejeske_1969]
- [Mechanism of Stability Enhancement with Shallow ‎Reversed Slot-Type Casing Treatment in a Transonic ‎Compressor 2021][research_mechanism_of_2021]
- [Mechanism study on the effect of self-circulating casing treatment with different circumferential coverage ratios on the axial compressor stability 2023][research_mechanism_study_2023]
- [Medina et al 2021][research_medina_patel_2021]
- [Mehalic 1988][research_mehalic_1988]
- [Melick 1973][research_melickhcjr_1973]
- [Melick et al 1975][research_melick_ybarra_1975]
- [Melick et al 1978][research_melick_ybarra_1978]
- [Menees and Boyd 1959][research_meneesgenep_boydjohnw_1959]
- [Menegozzo and Benini 2020][research_menegozzo_benini_2020]
- [Meng et al 2018][research_meng_fan_2018]
- [Menon et al 2023][research_menon_sanjayshivam_2023]
- [Merchant and Radhakrishnan 2017][research_merchant_radhakrishnan_2017]
- [Merkli 1975][research_merkli_1975]
- [Merkli 1976][research_merkli_1976]
- [Merritt et al 1985][research_merritt_cliff_1985]
- [Messing and Rabb 1952][research_messing_rabb_1952]
- [Miao and Sun 2024][research_miao_sun_2024]
- [Miao et al 2026][research_miao_guan_2026]
- [Michell 1971][research_michellga_1971]
- [Miele 1954][research_miele_1954]
- [Miele 1955][research_mieleangelo_1955]
- [Mikhail 1979][research_mikhail_1979]
- [Mikhailov et al 2017][research_mikhailov_mikhailova_2017]
- [Miki et al 2014][research_miki_kameda_2014]
- [Miki et al 2015][research_miki_watanabe_2015]
- [Milenković-Babić et al 2017][research_milenkovicbabic_samardzic_2017]
- [Miles 1953][research_miles_1953]
- [MILITARY PRESENCE AND ARMS EXPORT IN FRANCE’S MIDDLE EAST STRATEGY 2025][research_military_presence_2025]
- [Miller 1977][research_miller_1977]
- [Miller 1983][research_miller_1983]
- [Miller 1986][research_miller_1986]
- [Miller and Smith 2003][research_miller_smith_2003]
- [Miller et al 1983][research_millerds_pittmanjl_1983]
- [Millidere et al 2022][research_millidere_yigit_2022]
- [Mills 1978][research_mills_1978]
- [Min et al 2018][research_minjb_reddytsr_2018]
- [Min et al 2024][research_min_xian_2024]
- [Min Tint 2018][research_mintint_2018]
- [Ming et al 2023][research_ming_wu_2023]
- [Minnicino et al 2009][research_minnicino_gray_2009]
- [Mironov 1965][research_mironov_1965]
- [Mitcham et al 1951][research_mitcham_stevens_1951]
- [Mitsuyasu 1956][research_mitsuyasu_1956]
- [Miura et al 2021][research_miura_yamashita_2021]
- [Mixed Flow Turbofan Engine 2018][research_mixed_flow_2018]
- [Mizobata et al 2024][research_mizobata_mio_2024]
- [Mock 1951][research_mock_1951]
- [Moeckel 1955][research_moeckelwe_1955]
- [Moeckel and Evans 1951][research_moeckelwe_evanspjjr_1951]
- [Moga 1980][research_moga_1980]
- [Moin and Lele 1998][research_moin_lele_1998]
- [Moirou et al 2023][research_moirou_sanders_2023]
- [Mokotoff et al 2026][research_mokotoff_arnson_2026]
- [Molana et al 2020][research_molana_khodaparast_2020]
- [Montano 1967][research_montanojw_1967]
- [Moon 2025][research_moon_2025]
- [Moore 1973][research_moore_1973]
- [Moore and Lueke 1974][research_moore_lueke_1974]
- [Moorhouse and Jenkins 1975][research_moorhouse_jenkins_1975]
- [Morgenfeld 1992][research_morgenfeld_1992]
- [Morris et al 1976][research_morris_nelms_1976]
- [Morton 1956][research_morton_1956]
- [Moru et al 2022][research_moru_bo_2022]
- [Mount 1965][research_mount_1965]
- [Mozley 1943][research_mozley_1943]
- [Moëns 2022][research_moens_2022]
- [Muchmore 1988][research_muchmorecbjr_1988]
- [Muehter 1974][research_muehter_1974]
- [Mugalev et al 1985][research_mugalev_savushkina_1985]
- [Muller and Gasko 1967][research_muller_gasko_1967]
- [Muller and Gasko 1967][research_muller_gasko_1967_b]
- [Mungall 1948][research_mungallrobertc_1948]
- [Munjulury et al 2015][research_munjulury_staack_2015]
- [Murphy and Klein 2006][research_murphypatrickc_kleinvladislav_2006]
- [Murzionak][research_murzionak]
- [Musa et al 2024][research_musa_huang_2024]
- [Muth et al 2009][research_muth_bindl_2009]
- [Myers and Walsh 1988][research_myerslawrencep_walshkevinr_1988]
- [Myokan et al 2020][research_myokan_kubota_2020]
- [Mårtensson 2021][research_martensson_2021]
- [Mårtensson and Billson 2024][research_martensson_billson_2024]
- [Mårtensson et al 2022][research_martensson_lejon_2022]
- [Nadell 1996][research_nadell_1996]
- [Nagamatsu et al 1960][research_nagamatsu_workman_1960]
- [Nagao et al 2019][research_nagao_yoshida_2019]
- [Nageswara Rao and Kushari 2020][research_nageswararao_kushari_2020]
- [Nagler 2022][research_nagler_2022]
- [Nagler 2026][research_nagler_2026]
- [Nam and Mavris 2018][research_nam_mavris_2018]
- [Narayan 1975][research_narayan_1975]
- [Naruse et al 2022][research_naruse_ishii_2022]
- [Naseri et al 2016][research_naseri_boroomand_2016]
- [NAVY Participation and the 1998][research_navy_participation_1998]
- [Neal and Smith 1970][research_neal_smith_1970]
- [Neal and Smith 1970][research_neal_smith_1970_b]
- [Neaves and McRae 1995][research_neaves_mcrae_1995]
- [Negaard 1979][research_negaard_1979]
- [Neitzel and Hemsworth 1966][research_neitzel_hemsworth_1966]
- [Nelms and Bailey 1974][research_nelmswpjr_baileyro_1974]
- [Nelson and Welsh 1960][research_nelsonrobertl_welshclementj_1960]
- [Nelson et al 2014][research_nelson_lowe_2014]
- [Neshpor et al 1991][research_neshpor_armyagov_1991]
- [Ness 1971][research_ness_1971]
- [Nettles 1956][research_nettles_1956]
- [Neumark 1950][research_neumark_1950]
- [Neverlien et al 2020][research_neverlien_moe_2020]
- [Neville et al 1992][research_neville_oflarity_1992]
- [Newsome and Thomas 1986][research_newsomerw_thomasjl_1986]
- [Ng and Willcox 2016][research_ng_willcox_2016]
- [Ngan and Biezad 1996][research_nganangelen_biezaddaniel_1996]
- [Nguyen et al 1976][research_nguyenlt_anglinel_1976]
- [Nicholas et al 1984][research_nicholas_naville_1984]
- [Nichols and Pendley 1952][research_nicholsmarkr_pendleyroberte_1952]
- [Nichols and Rinkoski 1952][research_nichols_rinkoski_1952]
- [Nicholson 1985][research_nicholson_1985]
- [Nielsen 1985][research_nielsenjn_1985]
- [Nielsen et al 1953][research_nielsenjackn_kaattarigeorgee_1953]
- [Niknamian 2019][research_niknamian_2019]
- [Ning][research_ning]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952_b]
- [Northrop Aircraft Inc Hawthorne Ca 1953][research_northropaircraftinchawthorneca_1953]
- [Novikov 2017][research_novikov_2017]
- [Numerical Simulation of Supersonic Flow through Scramjet Intake with Concavity in Cowl Surface 2020][research_numerical_simulation_2020]
- [Nussdorfer et al 1952][research_nussdorfertheodorej_oberyleonardj_1952]
- [O'Kelly 1954][research_okelly_1954]
- [Obey et al 1952][research_obeyleonardt_englertgeraldw_1952]
- [Obikane 1984][research_obikane_1984]
- [Ochonogor et al 2017][research_ochonogor_akinlabi_2017]
- [Ogawa and Takeda 2015][research_ogawa_takeda_2015]
- [Ohashi and Ohno 1982][research_ohashi_ohno_1982]
- [Ohwada et al 2019][research_ohwada_shimada_2019]
- [Ohyama 1978][research_ohyama_1978]
- [Okelah 1985][research_okelah_1985]
- [Olwi 1995][research_olwi_1995]
- [Orman et al 1951][research_orman_rae_1951]
- [Oruc and Baklacioglu 2022][research_oruc_baklacioglu_2022]
- [Oruc and Baklacioglu 2023][research_oruc_baklacioglu_2023]
- [Oruç 2026][research_oruc_2026]
- [Osborne and Kelly 1953][research_osborneroberts_kellythomasc_1953]
- [Osborne and Kelly 1960][research_robertsosborne_thomasckelly_1960]
- [Osmon 1967][research_osmon_1967]
- [Ostieri and Tognaccini 2018][research_ostieri_tognaccini_2018]
- [Ostowari and Naik 1986][research_ostowaric_naikd_1986]
- [Oswatitsch 1947][research_oswatitsch_1947]
- [Oswatitsch 1952][research_oswatitsch_1952]
- [Oswatitsch 1958][research_oswatitsch_1958]
- [Oswatitsch 1980][research_oswatitsch_1980]
- [Otto et al 2015][research_otto_trefny_2015]
- [Overall 1976][research_overall_1976]
- [Page et al 2018][research_page_hield_2018]
- [Pakle and Jiang 2018][research_pakle_jiang_2018]
- [Palienko et al 1976][research_palienko_pogrebnyak_1976]
- [Palko 1973][research_palko_1973]
- [Palko 1974][research_palko_1974]
- [Palko 1975][research_palko_1975]
- [Pan et al 2017][research_pan_huang_2017]
- [Pan et al 2022][research_pan_shi_2022]
- [Pan et al 2024][research_pan_mu_2024]
- [Pan et al 2024][research_pan_shi_2024]
- [Panov and Shvets 1967][research_panov_shvets_1967]
- [Panov et al 1966][research_panov_shvets_1966]
- [Panton 1972][research_panton_1972]
- [Panzeri et al 2018][research_panzeri_savelyev_2018]
- [Papadales and Basil S. 1979][research_papadales_basils_1979]
- [Papageorgiou et al 2018][research_papageorgiou_tarkian_2018]
- [Papirno 1966][research_papirno_1966]
- [Papirno and Gerard 1962][research_papirno_gerard_1962]
- [Paraguassu 2015][research_paraguassu_2015]
- [Paranjape and Ananthkrishnan 2023][research_paranjape_ananthkrishnan_2023]
- [Parisen et al 1948][research_parisenrichardb_armstrongjohnc_1948]
- [Park et al 1993][research_park_chung_1993]
- [Park et al 2001][research_park_lee_2001]
- [Park et al 2015][research_park_lee_2015]
- [Park et al 2016][research_park_chung_2016]
- [Park et al 2016][research_park_chung_2016_b]
- [Park et al 2018][research_park_chung_2018]
- [Park et al 2026][research_park_kim_2026]
- [Parker 1991][research_parker_1991]
- [Parkes 1953][research_parkes_1953]
- [Parkes 1954][research_parkes_1954]
- [Parkes 1956][research_parkes_1956]
- [Parkes 1956][research_parkes_1956_b]
- [Parlier 1986][research_parlier_1986]
- [Parris et al 1957][research_parris_sherman_1957]
- [Pasiuk 1963][research_pasiuk_1963]
- [Patel and Chudoba 2026][research_patel_chudoba_2026]
- [Patil 2018][research_patil_2018]
- [Paton et al 1982][research_paton_bampton_1982]
- [Payne 1980][research_payne_1980]
- [Paynter 1994][research_paynter_1994]
- [Paynter and Chen 1983][research_paynter_chen_1983]
- [Paynter et al 1992][research_paynter_treiber_1992]
- [Paynter et al 1993][research_paynter_mayer_1993]
- [Paziresh et al 2017][research_paziresh_nikseresht_2017]
- [Peacock 1978][research_peacock_1978]
- [Peck et al 2020][research_peck_liu_2020]
- [Peng-ju et al 2015][research_pengju_liang_2015]
- [Penland et al 1975][research_penlandja_fournierrh_1975]
- [Penland et al 1978][research_penlandja_creeltrjr_1978]
- [Pennington and Meintel 1980][research_penningtonje_meintelajjr_1980]
- [Perepezko 2001][research_perepezko_2001]
- [Perkins and Dillenius 1991][research_perkins_dillenius_1991]
- [Persh 1955][research_persh_1955]
- [Petersen 1957][research_petersenrb_1957]
- [Peterson 1982][research_peterson_1982]
- [Peterson and Menees 1959][research_petersonvictorl_meneesgenep_1959]
- [Petkovic et al 2025][research_petkovic_banjac_2025]
- [Petruzzelli and Keane 2001][research_petruzzelli_keane_2001]
- [Pečinka et al 2017][research_pecinka_bugajski_2017]
- [Pfaff 1965][research_pfaff_1965]
- [Pfaff 1968][research_pfaff_1968]
- [Pfnür and Breitsamter 2019][research_pfnur_breitsamter_2019]
- [Pfyl 1955][research_pfyl_1955]
- [Pfyl and Presley 1961][research_pfyl_presley_1961]
- [Philippou et al 2024][research_philippou_zachos_2024]
- [Phillips 1999][research_phillips_jr_1999]
- [Piccirillo and Aronstein 1997][research_piccirillo_aronstein_1997]
- [Piccirillo et al 2024][research_piccirillo_gregorio_2024]
- [Piovesan et al 2025][research_piovesan_zachos_2025]
- [Pismennyi][research_pismennyi]
- [Planeaux and Barth 1988][research_planeaux_barth_1988]
- [Platzer 1964][research_platzer_1964]
- [Plourde and Stenning 1968][research_plourde_stenning_1968]
- [Poggie 2019][research_poggie_2019]
- [Poggie and Porter 2018][research_poggie_porter_2018]
- [Polhamus 1966][research_polhamusec_1966]
- [Polhamus 1968][research_polhamusec_1968]
- [Poorman 1980][research_poorman_1980]
- [Popovich et al 2014][research_popovich_kirill_2014]
- [Popovich et al 2021][research_popovich_kiselev_2021]
- [Portnoy 1963][research_portnoy_1963]
- [Powell and Glickstein 1988][research_powell_glickstein_1988]
- [Powell et al 1985][research_powellag_welgehr_1985]
- [Powers 1966][research_powersbg_1966]
- [Powers et al 1983][research_powers_driggers_1983]
- [Powers et al 1983][research_powers_driggers_1983_b]
- [Prasad 2025][research_prasad_2025]
- [Prasad and Rivera 1996][research_prasad_rivera_1996]
- [Preliminary Design for Axisymmetric 2006][research_preliminary_design_2006]
- [Presley 1975][research_presley_1975]
- [Presz et al 1971][research_presz_konarski_1971]
- [Prigent et al 2015][research_prigent_marechal_2015]
- [Prince 1976][research_prince_1976]
- [Probst and Melber-Wilkending 2021][research_probst_melberwilkending_2021]
- [Processing and Validating CFD][research_processing_and]
- [Procurement Process Geared Up for New Airplanes 1980][research_procurement_process_1980]
- [Provenza et al 2018][research_provenza_duffy_2018]
- [Pruitt and Bates 1992][research_pruitt_bates_1992]
- [Purser and Spear 1947][research_purserpaule_spearmargaretf_1947]
- [Qiang et al 2024][research_qiang_xue_2024]
- [Qiao et al 2026][research_qiao_chu_2026]
- [Qin 2026][research_qin_2026]
- [Qin and Liang 2016][research_qin_liang_2016]
- [Qiu et al 2023][research_qiu_du_2023]
- [Qiu et al 2023][research_qiu_zhao_2023]
- [Qiu et al 2024][research_qiu_zhong_2024]
- [Qu et al 2019][research_qu_kong_2019]
- [Qu et al 2024][research_qu_wang_2024]
- [Quan et al 2024][research_quan_sun_2024]
- [Queijo and Wolhart 1951][research_queijomj_wolhartwalterd_1951]
- [Queijo et al 1954][research_queijomj_jaquetbyronm_1954]
- [Quigley et al 1960][research_quigleyherveyc_andersonsethb_1960]
- [Rademakers et al 2018][research_rademakers_probst_2018]
- [Radespiel et al 2016][research_radespiel_burnazzi_2016]
- [Radon 1969][research_radon_1969]
- [Rafiq and Qureshi 2022][research_rafiq_qureshi_2022]
- [Rains 1955][research_rains_1955]
- [Raj et al 2003][research_praj_fghaffari_2003]
- [Rajagopalan and Siddiqi 1985][research_rajagopalan_siddiqi_1985]
- [Rajdeep Bose Mondal 2026][research_rajdeepbosemondal_2026]
- [Rakipoğlu and Avcı 2026][research_rakipoglu_avci_2026]
- [Ramachandra et al 1979][research_ramachandra_sudhakar_1979]
- [Ramachandran and Wells 1974][research_ramachandran_wells_1974]
- [Ramachandran and Wells 1975][research_ramachandran_wells_1975]
- [Ramakrishna et al 2019][research_ramakrishna_senthilkumar_2019]
- [Ramamurti 2011][research_ramamurti_2011]
- [Ramaswamy and Viswanathan 1975][research_ramaswamy_viswanathan_1975]
- [Ramjet supersonic “flight tests” 1958][research_ramjet_supersonic_1958]
- [Ran and Mavris 2005][research_ran_mavris_2005]
- [Rand 1963][research_rand_1963]
- [Ransom 1983][research_ransom_1983]
- [Rao et al 2022][research_rao_sureshkumar_2022]
- [Rao et al 2025][research_rao_kumar_2025]
- [Raspet 1957][research_raspet_1957]
- [Ratnayake 2010][research_ratnayakenalina_2010]
- [Ray and Taylor 1965][research_rayej_taylorrt_1965]
- [Ray et al 1988][research_ray_hicks_1988]
- [Raymer 1991][research_raymer_1991]
- [Raymer 1998][research_raymer_1998]
- [Rebuffet and Poisson-Quinton 1952][research_rebuffetpierre_poissonquintonph_1952]
- [Reddy et al 2023][research_reddy_govardhan_2023]
- [Reedy and Gorrell 2025][research_reedy_gorrell_2025]
- [Reggiori 1972][research_reggiori_1972]
- [Reich and Wimbauer 1975][research_dieterreich_josefwimbauer_1975]
- [Reid 1937][research_reid_1937]
- [Reinbold et al 2026][research_reinbold_breitsamter_2026]
- [Reist et al 2022][research_reist_koo_2022]
- [Rejeske and Stava 1974][research_rejeske_stava_1974]
- [Ren et al 2021][research_ren_zhang_2021]
- [Report no. 609, Experimental investigation of wind-tunnel interference on the downwash behind an airfoil 1937][research_report_no_1937]
- [Report No. 648, Design charts for predicting downwash angles and wake characteritics behind plain and flapped wings 1939][research_report_no_1939]
- [Resta et al 2021][research_resta_marsilio_2021]
- [Rettie and Lewis 1968][research_rettie_lewis_1968]
- [Reukauf and Burcham 1976][research_reukaufpj_burchamfwjr_1976]
- [Reyhner and Hickcox 1972][research_reyhner_hickcox_1972]
- [Reykers and Fonck 2019][research_reykers_fonck_2019]
- [Reymer et al 2018][research_reymer_zielinski_2018]
- [Reynolds 1993][research_reynolds_1993]
- [Reza Maadi and Sepahi-Younsi 2022][research_rezamaadi_sepahiyounsi_2022]
- [Rhomberg 1972][research_rhomberg_1972]
- [Ribner 1960][research_ribner_1960]
- [Riccobene and Ricci 2015][research_riccobene_ricci_2015]
- [Richards and Thompson 1991][research_richardswl_thompsonrandolphc_1991]
- [Righi et al 2018][research_righi_pachidis_2018]
- [Rivello 1965][research_rivello_1965]
- [Rizzetta 1991][research_rizzetta_1991]
- [Rizzetta and Visbal 2001][research_rizzetta_visbal_2001]
- [Roache 1965][research_roache_1965]
- [Roberts 1965][research_roberts_1965]
- [Roberts et al 1966][research_roberts_smith_1966]
- [Robins et al 1985][research_robinsaw_beissnerfljr_1985]
- [Rockwell 2001][research_rockwell_2001]
- [Rodgers 1965][research_rodgers_1965]
- [Rodgers 1966][research_rodgers_1966]
- [Roelofs et al 2021][research_roelofs_kurowicka_2021]
- [Rosell][research_rosell]
- [Rosen 2001][research_rosen_2001]
- [Rosenbaum and Zeiberg 1965][research_rosenbaumh_zeibergsl_1965]
- [Rosenthal 1975][research_rosenthal_1975]
- [Rosenthal and Brandeau 1983][research_rosenthal_brandeau_1983]
- [Roskam and Dusto 1969][research_roskam_dusto_1969]
- [Roskam et al 1968][research_roskam_holgate_1968]
- [Roth et al 2005][research_roth_doel_2005]
- [Rowe 1958][research_rowe_1958]
- [Rowe and Sussman 1971][research_rowe_sussman_1971]
- [Roy Salam and Bil 2016][research_roysalam_bil_2016]
- [Ruban et al 2020][research_ruban_menezes_2020]
- [Rubio and Ballard 1967][research_rubio_ballard_1967]
- [Rudnitski][research_rudnitski]
- [Rudolph 1997][research_rudolphpeterkc_1997]
- [Rumsey and Lee 1961][research_rumseycharlesb_leedorothyb_1961]
- [Rumsey et al 2019][research_rumsey_slotnick_2019]
- [Runstadler and Peter W. 1969][research_runstadler_peterw_1969]
- [Russell 2014][research_russell_2014]
- [Rybalko and Loth 2015][research_rybalko_loth_2015]
- [Rylov 1974][research_rylov_1974]
- [Sachs 1975][research_sachs_1975]
- [Sachs 1977][research_sachs_1977]
- [Sachs 1980][research_sachs_1980]
- [Sadraey 2017][research_sadraey_2017]
- [Safavi et al 2015][research_safavi_tarkian_2015]
- [Safoklov et al 2025][research_safoklov_demidov_2025]
- [Saheby et al 2019][research_bsaheby_shen_2019]
- [Sahoo and Peetala 2010][research_sahoo_peetala_2010]
- [Sahu 1986][research_sahu_1986]
- [Said et al 2018][research_said_mat_2018]
- [Sajadifar et al 2023][research_sajadifar_maier_2023]
- [Sakata and Davis 1977][research_sakataif_davisgw_1977]
- [Sakata and Ohta 2017][research_sakata_ohta_2017]
- [Sakata et al 1975][research_sakataif_davisgw_1975]
- [Saleem Yusoof et al 2016][research_saleemyusoof_sivapragasam_2016]
- [Samimy et al 2011][research_samimy_webb_2011]
- [Sanchez-Carmona and Cuerno-Rejado 2018][research_sanchezcarmona_cuernorejado_2018]
- [Sandahl 1948][research_sandahlcarla_1948]
- [Sanders 1980][research_sanders_1980]
- [Sandstrom and White 1961][research_sandstrom_white_1961]
- [Saporito et al 2023][research_saporito_daronch_2023]
- [Saraswathi 2000][research_saraswathi_2000]
- [Saravanan et al 2017][research_saravanan_desikan_2017]
- [Sasoh et al 2018][research_sasoh_myokan_2018]
- [Satyanarayana et al 1975][research_satyanarayana_prasad_1975]
- [Saunders and Keith 1991][research_saundersjd_keithtgjr_1991]
- [Saves et al 2024][research_saves_diouane_2024]
- [Saxena 1998][research_saxenaashok_1998]
- [Schaffrath et al 2025][research_schaffrath_nicke_2025]
- [Scherz and Williams 1978][research_scherz_williams_1978]
- [Schneider 1990][research_schneideredwardt_1990]
- [Schoeler 1987][research_schoeler_1987]
- [Schrage 1990][research_schrage_1990]
- [Schuldenfrei et al 1947][research_schuldenfreimarvin_comisarowpaul_1947]
- [Schulderfrei et al 1951][research_schulderfreimarvin_comisarowpaul_1951]
- [Schuster 1995][research_schuster_1995]
- [Schwanz 1972][research_schwanz_1972]
- [Schwartz 1988][research_schwartz_1988]
- [Schweiger 1987][research_schweiger_1987]
- [Schweikhardt and Grippe 1971][research_schweikhardt_grippe_1971]
- [Schwendemann 1981][research_schwendemannmf_1981]
- [Scribben and Withrow 2006][research_scribben_withrow_2006]
- [Sebata and Ushijima 2021][research_sebata_ushijima_2021]
- [Sebata and Ushijima 2022][research_sebata_ushijima_2022]
- [Sederstrom et al 1973][research_sederstrom_zagalsky_1973]
- [Sedlock 1985][research_sedlock_1985]
- [Seginer and Salomon 1983][research_seginer_salomon_1983]
- [Seidel et al 1980][research_seidel_matwey_1980]
- [Selegan 1983][research_selegan_1983]
- [Seleznev 2018][research_seleznev_2018]
- [Seleznev 2018][research_seleznev_2018_b]
- [Seleznev 2019][research_seleznev_2019]
- [Selna and Schlaff 1951][research_selna_schlaff_1951]
- [Semenov 1981][research_semenov_1981]
- [Semlitsch and Mihăescu 2016][research_semlitsch_mihaescu_2016]
- [Semlitsch and Mihăescu 2021][research_semlitsch_mihaescu_2021]
- [Sepahi-Younsi 2022][research_sepahiyounsi_2022]
- [Sepahi-Younsi 2025][research_sepahiyounsi_2025]
- [Setayandeh and Babaei 2020][research_setayandeh_babaei_2020]
- [Sgueglia et al 2020][research_sgueglia_schmollgruber_2020]
- [Shahin et al 2016][research_shahin_alqaradawi_2016]
- [Shahriyari et al 2024][research_shahriyari_firouzabadi_2024]
- [Shang et al 2021][research_shang_ge_2021]
- [Shao et al 2016][research_shao_cao_2016]
- [Shariatzadeh et al 2015][research_shariatzadeh_abrishamkar_2015]
- [Shechtman 1981][research_shechtman_1981]
- [Shen 2017][research_shen_2017]
- [Shen and Wen 2018][research_shen_wen_2018]
- [Sheng et al 2020][research_sheng_chen_2020]
- [Sheng et al 2023][research_sheng_chen_2023]
- [Shevell 1978][research_shevell_1978]
- [Shi 2025][research_shi_2025]
- [Shi et al 2018][research_shi_chang_2018]
- [Shi et al 2019][research_shi_chang_2019]
- [Shi et al 2019][research_shi_chang_2019_b]
- [Shi-feng et al 2018][research_shifeng_jiamin_2018]
- [Shimabukuro et al 1979][research_shimabukurokm_welgehr_1979]
- [Shimabukuro et al 1982][research_shimabukuro_welge_1982]
- [Shimada and Ohwada 2020][research_shimada_ohwada_2020]
- [Shindo and Joppa 1980][research_shindos_jopparg_1980]
- [Shiriaev et al 2026][research_shiriaev_freidovich_2026]
- [Shirinzadeh Dastgiri et al 2023][research_shirinzadehdastgiri_fuerth_2023]
- [Shiryaev and Serebryansky 2022][research_shiryaev_serebryansky_2022]
- [Shiryaev et al 2023][research_shiryaev_maysak_2023]
- [Shkaraputa 1976][research_shkaraputa_1976]
- [Shoshany‐Tavory et al 2023][research_shoshanytavory_peleg_2023]
- [Shu et al 2025][research_shu_gao_2025]
- [Shucheng and Xijun 1994][research_shucheng_xijun_1994]
- [Shufan et al 2018][research_shufan_heng_2018]
- [Shulman et al 1966][research_shulman_parry_1966]
- [Shvedchenko 2009][research_shvedchenko_2009]
- [Shvedchenko 2010][research_shvedchenko_2010]
- [Si et al 2019][research_si_huang_2019]
- [Siano 2014][research_siano_2014]
- [Sibulkin 1951][research_sibulkin_1951]
- [Siedlak et al 2017][research_siedlak_pinon_2017]
- [Sih and Chou 1989][research_sih_chou_1989]
- [Silton et al 2014][research_silton_fresconi_2014]
- [Silverstein and White 1937][research_silversteinabe_whitejamesa_1937]
- [Sinaiskii et al 1972][research_sinaiskii_pogrebnyak_1972]
- [Singh and Dwivedi 2022][research_singh_dwivedi_2022]
- [Sinha et al 2026][research_sinha_singh_2026]
- [Sitaram et al 2023][research_sitaram_govardhan_2023]
- [Sivaramakrishnan 1981][research_sivaramakrishnan_1981]
- [Skoog 1951][research_skoogrichardb_1951]
- [Skow et al 1982][research_skow_moore_1982]
- [Slater][research_slater]
- [Slater][research_slater_b]
- [Slater 2011][research_slaterjohnw_2011]
- [Slater 2014][research_slaterjohnw_2014]
- [Slater 2015][research_slaterjohnw_2015]
- [Slater 2016][research_slaterjohnw_2016]
- [Slater 2017][research_slaterjohnw_2017]
- [Slater 2019][research_slater_2019]
- [Slater 2020][research_slater_2020]
- [Slater 2023][research_slater_2023]
- [Slater 2024][research_slater_2024]
- [Sleeman 1957][research_sleemanwilliamcjr_1957]
- [Sleeman 1961][research_sleemanwilliamcjr_1961]
- [Sleeman and Byrnes 1953][research_sleemanwilliamc_byrnesandrewl_1953]
- [Smart et al 1994][research_smartmichaelk_kalkhoranirajm_1994]
- [Smeltzer and Sorensen 1972][research_smeltzerdb_sorensenne_1972]
- [Smith 1954][research_smithwilliardg_1954]
- [Smith 1967][research_smith_1967]
- [Smith 2021][research_smith_2021]
- [Smith and Burgess 1960][research_smith_burgess_1960]
- [Smith et al 1976][research_smith_jones_1976]
- [Smith et al 1979][research_smith_yamakawa_1979]
- [Smith et al 1984][research_smith_mead_1984]
- [Smith et al 2007][research_smith_scribben_2007]
- [Snodgrass 1955][research_snodgrass_1955]
- [Soeder and Bobula 1979][research_soederrh_bobulaga_1979]
- [Soeder and Bobula 1979][research_soederrh_bobulaga_1979_b]
- [Soeder and Bobula 1982][research_soederrh_bobulaga_1982]
- [Soeder and Mehalic 1984][research_soederrh_mehaliccm_1984]
- [Sogukpinar 2018][research_sogukpinar_2018]
- [Solomon 1955][research_solomongeorgee_1955]
- [Soltani and Askari 2019][research_soltani_askari_2019]
- [Soltani et al 2011][research_soltani_farahani_2011]
- [Soltani et al 2015][research_soltani_younsi_2015]
- [Soltani et al 2016][research_soltani_daliri_2016]
- [Song et al 2019][research_song_kim_2019]
- [Song et al 2019][research_song_zhang_2019]
- [Sonoda et al 2009][research_sonoda_olhofer_2009]
- [Sorensen and Bencze 1973][research_sorensenne_benczedp_1973]
- [Sorensen and Bencze 1974][research_sorensen_bencze_1974]
- [Sorensen and Latham 1975][research_sorensen_latham_1975]
- [Sorensen and Smeltzer 1972][research_sorensen_smeltzer_1972]
- [Sorensen et al 1969][research_sorensen_smeltzer_1969]
- [Sorensen et al 1973][research_sorensen_smeltzer_1973]
- [Sorrells et al 1984][research_sorrells_towne_1984]
- [Sosnin and Torshenov 1970][research_sosnin_torshenov_1970]
- [Sousa et al 2017][research_sousa_paniagua_2017]
- [Sovran 1959][research_sovran_1959]
- [Sowers and Stueber][research_sowers_stueber]
- [Sowers and Stueber 2025][research_sowers_stueber_2025]
- [Sowter 1973][research_sowter_1973]
- [Spearman 1983][research_spearman_1983]
- [Spearman 1984][research_spearman_1984]
- [Spearman and Sawyer 1977][research_spearmanml_sawyerwc_1977]
- [Spearman et al 1977][research_spearman_fournier_1977]
- [Spencer 1961][research_spencerbernardjr_1961]
- [Spooner and Martina 1948][research_spoonerstanleyh_martinaalbertp_1948]
- [Spreemann 1958][research_spreemannkennethp_1958]
- [Spreiter and Sacks 1951][research_spreiter_sacks_1951]
- [Squires 2002][research_squires_2002]
- [Squires 2004][research_squires_2004]
- [Sreekumar et al 2025][research_sreekumar_vamsikrishna_2025]
- [Srivastav and Ponnani 2011][research_srivastav_ponnani_2011]
- [Srivatsan 1999][research_srivatsan_1999]
- [Srivatsan and Anand 1998][research_srivatsan_anand_1998]
- [St. Aubyn 2015][research_staubyn_2015]
- [St. John and Frederick 2013][research_stjohn_frederick_2013]
- [Stamatelos and Labeas 2025][research_stamatelos_labeas_2025]
- [Stancil 1979][research_stancil_1979]
- [Stanišić 1961][research_stanisic_1961]
- [Stanley 1980][research_stanley_1980]
- [Starken and Lichtfuss 1970][research_starken_lichtfuss_1970]
- [Steenken et al 1999][research_steenkenwg_williamsjg_1999]
- [Steer 2003][research_steer_2003]
- [Stenning 1980][research_stenning_1980]
- [Stenning 1980][research_stenning_1980_b]
- [Stephan et al 2024][research_stephan_heyen_2024]
- [Stephens 1959][research_stephensemilyw_1959]
- [Stephenson 1953][research_stephenson_1953]
- [Stephenson 1958][research_stephenson_1958]
- [Sterbentz and Davids 1952][research_sterbentzwilliamh_davidsjoseph_1952]
- [Stewart 1956][research_stewart_1956]
- [Stewartson 1950][research_stewartson_1950]
- [Stickley and Brownhill 1964][research_stickley_brownhill_1964]
- [Stocker 1951][research_stocker_1951]
- [Stone 1945][research_stone_1945]
- [Straight and Harrington 1973][research_straightdm_harringtonde_1973]
- [Strub and Suter 1965][research_strub_suter_1965]
- [Stubbs 1956][research_stubbs_1956]
- [Studer 2012][research_studer_2012]
- [Sturek et al 1983][research_sturek_kayser_1983]
- [Sturek et al 1983][research_sturek_kayser_1983_b]
- [Su and Young 2017][research_su_young_2017]
- [Su et al 2023][research_su_qu_2023]
- [Subramanian and DeLaurentis 2016][research_subramanian_delaurentis_2016]
- [Suchocki et al 2015][research_suchocki_lampart_2015]
- [Sugiyama 1971][research_sugiyama_1971]
- [Sugiyama 1971][research_sugiyama_1971_b]
- [Sugiyama 1977][research_sugiyama_1977]
- [Sullivan 1978][research_sullivanpg_1978]
- [Sullivan 2002][research_sullivan_2002]
- [Sun and Smith 2019][research_sun_smith_2019]
- [Sun and Zhang 2016][research_sun_zhang_2016]
- [Sun and Zhu 2019][research_sun_zhu_2019]
- [Sun et al 2015][research_sun_miao_2015]
- [Sun et al 2015][research_sun_nie_2015]
- [Sun et al 2020][research_sun_yang_2020]
- [Sun et al 2021][research_sun_gu_2021]
- [Sun et al 2021][research_sun_li_2021]
- [Sun et al 2021][research_sun_li_2021_b]
- [Sun et al 2022][research_sun_li_2022]
- [Sun et al 2024][research_sun_gu_2024]
- [Sun et al 2024][research_sun_gu_2024_b]
- [Sun et al 2024][research_sun_hu_2024]
- [Sun et al 2024][research_sun_yang_2024]
- [Sun et al 2024][research_sun_zhang_2024]
- [Sun et al 2025][research_sun_shen_2025]
- [Sun et al 2025][research_sun_yang_2025]
- [Sun et al 2025][research_sun_yu_2025]
- [Sun et al 2025][research_sun_zheng_2025]
- [Sun et al 2026][research_sun_ding_2026]
- [Sunderroy et al 2022][research_sunderroy_karnick_2022]
- [Supersonic Flight 2014][research_supersonic_flight_2014]
- [Surber 1975][research_surber_1975]
- [Surber and Robinson 1983][research_surber_robinson_1983]
- [Surber and Sedlock 1979][research_surber_sedlock_1979]
- [Surwase and Kumar 2025][research_surwase_kumar_2025]
- [Sussman 1968][research_sussman_1968]
- [Sutton 1959][research_suttonfredb_1959]
- [Sweep Optimization to Reduce Aerodynamic Loss in a Transonic Axial Compressor with Upstream Boundary Layer Ingestion 2024][research_sweep_optimization_2024]
- [Swortzel and Barfield 1976][research_swortzel_barfield_1976]
- [Syberg and Koncsek 1972][research_sybergj_koncsekjl_1972]
- [Syberg and Koncsek 1976][research_syberg_koncsek_1976]
- [Syberg et al 1981][research_syberg_paynter_1981]
- [Szusta 2018][research_szusta_2018]
- [Sóbester 2021][research_sobester_2021]
- [Tabanli and Yuceil 2021][research_tabanli_yuceil_2021]
- [Tadini et al 2017][research_tadini_grange_2017]
- [Taghavi-Zenouz and Ababaf Behbaha 2017][research_taghavizenouz_ababafbehbaha_2017]
- [Taghi-Abad et al 2026][research_taghiabad_esfandabadi_2026]
- [Taguchi et al 2017][research_taguchi_mori_2017]
- [Taig 1961][research_taig_1961]
- [Takahashi 2012][research_takahashi_2012]
- [Takahashi 2017][research_takahashi_2017]
- [Takovitskii 2020][research_takovitskii_2020]
- [Takovitsky 2018][research_takovitsky_2018]
- [Tamboli 1956][research_tamboli_1956]
- [Tamrat 1988][research_tamrat_1988]
- [Tan and Suder 2003][research_tanchoonsooi_suderkenneth_2003]
- [Tanaka and Murata 1975][research_tanaka_murata_1975]
- [Tanaka and Murata 1975][research_tanaka_murata_1975_b]
- [Tanaka and Murata 1975][research_tanaka_murata_1975_c]
- [Tanaka and Nojima 1971][research_tanaka_nojima_1971]
- [Tang et al 2024][research_tang_xu_2024]
- [Tang et al 2025][research_tang_cai_2025]
- [Tang et al 2025][research_tang_cai_2025_b]
- [Tang et al 2025][research_tang_li_2025]
- [Tanguy et al 2018][research_tanguy_macmanus_2018]
- [Tani 1978][research_tani_1978]
- [Tanida 1972][research_tanida_1972]
- [Tao and Sun 2019][research_tao_sun_2019]
- [Tao et al 2020][research_tao_sun_2020]
- [Tao et al 2022][research_tao_jin_2022]
- [Tao et al 2024][research_tao_wang_2024]
- [Tate and Gillard 1975][research_tate_gillard_1975]
- [Taufik Budi Cahyana et al 2023][research_taufikbudicahyana_achmadwardana_2023]
- [Taylor 1968][research_taylor_1968]
- [Taylor 1991][research_taylorjohng_1991]
- [Tesch and Steenken 1978][research_teschwa_steenkenwg_1978]
- [Tewfik and Giedt 1960][research_tewfik_giedt_1960]
- [Tfaily et al 2024][research_tfaily_diouane_2024]
- [Tfaily et al 2026][research_tfaily_bartoli_2026]
- [Thankachan 2025][research_thankachan_2025]
- [Thapa et al 2025][research_thapa_li_2025]
- [The Cutting Edge A 1998][research_the_cutting_1998]
- [The Fiat G80 Turbojet Fighter‐Trainer 1952][research_the_fiat_1952]
- [The Hawker P1127 vectored 1990][research_the_hawker_1990]
- [The Potez Multi-Seater Fighter 1935][research_the_potez_1935]
- [The Reason and Strategy of Centrifugal Compressor Surge 2021][research_the_reason_2021]
- [The Rolls‐Royce RB.211 Three Shaft Turbofan 1968][research_the_rollsroyce_1968]
- [The Rolls‐Royce Spey Junior Turbofan Engine 1967][research_the_rollsroyce_1967]
- [Thein 2018][research_thein_2018]
- [Theodorsen 1959][research_theodorsen_1959]
- [Thomas 1942][research_thomas_1942]
- [Thomas 1965][research_thomas_1965]
- [Thomas and Stueber 2013][research_thomasrandy_stueberthomasj_2013]
- [Thomas et al 1999][research_thomas_won_1999]
- [THRUST VECTORING OF A SUPERSONIC RECTANGULAR NOZZLE BY USING DIFFERENT PLATE EXTENSIONS 2020][research_thrust_vectoring_2020]
- [Tian and Li 2020][research_tian_li_2020]
- [Tian et al 2021][research_tian_shunke_2021]
- [Tich et al 1987][research_tich_shaw_1987]
- [Tindell 1980][research_tindell_1980]
- [Tindell 1981][research_tindell_1981]
- [Ting et al 2018][research_ting_chaparro_2018]
- [Tirpak 1985][research_tirpak_1985]
- [Todorov et al 2023][research_todorov_rakov_2023]
- [Toffol and Ricci 2023][research_toffol_ricci_2023]
- [Toll 1942][research_tollthomasa_1942]
- [Tomczak 2026][research_tomczak_2026]
- [Tomczyk and Seweryn 2017][research_tomczyk_seweryn_2017]
- [Tomczyk and Seweryn 2021][research_tomczyk_seweryn_2021]
- [Tondl 1979][research_tondl_1979]
- [Tongguang et al 2015][research_tongguang_changhui_2015]
- [Torenbeek 1971][research_torenbeek_1971]
- [Torić et al 2018][research_toric_glavinic_2018]
- [Toro et al 1999][research_toro_myrabo_1999]
- [Transonic and supersonic flight 1992][research_transonic_and_1992]
- [Trefny and Benson 1995][research_trefnycj_bensontj_1995]
- [Trefny and Wasserbauer 1986][research_trefnycj_wasserbauerjw_1986]
- [Trefny et al 2014][research_trefny_hirt_2014]
- [Triplett 1980][research_triplett_1980]
- [Tritschler et al 2025][research_tritschler_juhasz_2025]
- [Tudosie 2017][research_tudosie_2017]
- [Tudosie 2017][research_tudosie_2017_b]
- [Tudosie 2018][research_tudosie_2018]
- [Tudosie 2024][research_tudosie_2024]
- [Tudosie and Prisacariu 2022][research_tudosie_prisacariu_2022]
- [Tudosie and Păunescu 2017][research_tudosie_paunescu_2017]
- [Tudosie et al 2019][research_tudosie_dumitru_2019]
- [Tuninetti et al 2024][research_tuninetti_sepulveda_2024]
- [Turn Performance and Maneuver 2021][research_turn_performance_2021]
- [Turning Flight 1997][research_turning_flight_1997]
- [Turning Flights of Turbojet 1995][research_turning_flights_1995]
- [Turning performance 1992][research_turning_performance_1992]
- [Tyan et al 2017][research_tyan_nguyen_2017]
- [Türkkahraman et al 2024][research_turkkahraman_ozcan_2024]
- [Uddin and Gravdahl 2016][research_uddin_gravdahl_2016]
- [Uemura et al 2020][research_uemura_kamata_2020]
- [Uludag and Turan 2015][research_uludag_turan_2015]
- [Um 2016][research_um_2016]
- [URANS Simulation of Self-Recirculation Casing Treatment in a Transonic Compressor 2024][research_urans_simulation_2024]
- [Using Tip Injection to Stability Enhancement of a Transonic Centrifugal Impeller with Inlet Distortion 2022][research_using_tip_2022]
- [Uthgenannt 1971][research_uthgenannt_1971]
- [Utomo and Bura 2019][research_utomo_bura_2019]
- [Vaca-Rios and Cerón-Muñoz 2025][research_vacarios_ceronmunoz_2025]
- [Vaisakh et al 2019][research_vaisakh_namratha_2019]
- [Valencia et al 2017][research_valencia_hidalgo_2017]
- [Valencia et al 2020][research_valencia_alulema_2020]
- [Valensi 1958][research_valensi_1958]
- [Valoppi et al 2017][research_valoppi_bruschi_2017]
- [Van Deusen and Mardoc 1972][research_vandeusen_mardoc_1972]
- [Van Dommelen 1995][research_vandommelen_1995]
- [van Es 2002][research_vanes_2002]
- [VanSchalkwyk et al 2001][research_vanschalkwykchristian_brightmichellem_2001]
- [Vasil'ev 1970][research_vasilev_1970]
- [Veeresh Kumar et al 2021][research_veereshkumar_nagasailaja_2021]
- [Venturelli and Benini 2016][research_venturelli_benini_2016]
- [Veresnikov 2025][research_veresnikov_2025]
- [Veresnikov et al 2026][research_veresnikov_goncharenko_2026]
- [Verma and Kulkarni 2024][research_verma_kulkarni_2024]
- [Verma and Manisankar 2025][research_verma_manisankar_2025]
- [Verma et al 2020][research_verma_singh_2020]
- [Vidal 1962][research_vidal_1962]
- [Vieira et al 2025][research_vieira_soltz_2025]
- [Vinogradov et al 2017][research_vinogradov_makarov_2017]
- [Vinogradov et al 2017][research_vinogradov_melnikov_2017]
- [Vira and Fan 1982][research_viranr_fandn_1982]
- [Vitols et al 2026][research_vitols_threadgill_2026]
- [von Doenhoff and Horton 1942][research_vondoenhoffalberte_hortonelmera_1942]
- [von Hlatky and Rice 2018][research_vonhlatky_rice_2018]
- [Vorob'ev and Bich 1977][research_vorobev_bich_1977]
- [Vorob’ev and Galiakhmetov 2023][research_vorobev_galiakhmetov_2023]
- [Voß and Klimmek 2023][research_voss_klimmek_2023]
- [Vu et al 2025][research_vu_nguyen_2025]
- [Wabick et al 2023][research_wabick_johnson_2023]
- [Wages 1971][research_wages_1971]
- [Walker 1955][research_walker_1955]
- [Walker and Berggren 1948][research_walkerharoldj_berggrenroberte_1948]
- [Walker et al 2005][research_walker_fletcher_2005]
- [Walkley 1986][research_walkley_1986]
- [Wallner et al 1954][research_wallnerlewise_lubickrobertj_1954]
- [Wallner et al 1955][research_wallnerle_lubickrj_1955]
- [Wallskog 1954][research_wallskog_1954]
- [Wallskog 1954][research_wallskog_1954_b]
- [Wan and Guo 2007][research_wan_guo_2007]
- [Wang and Trapp 1958][research_wang_trapp_1958]
- [Wang and Zhao 2026][research_wang_zhao_2026_b]
- [Wang et al 2013][research_wang_wang_2013]
- [Wang et al 2013][research_wang_wang_2013_b]
- [Wang et al 2015][research_wang_tian_2015]
- [Wang et al 2017][research_wang_chen_2017]
- [Wang et al 2017][research_wang_guo_2017]
- [Wang et al 2018][research_wang_liu_2018]
- [Wang et al 2020][research_wang_hu_2020]
- [Wang et al 2020][research_wang_lu_2020]
- [Wang et al 2020][research_wang_wang_2020]
- [Wang et al 2021][research_wang_hu_2021]
- [Wang et al 2021][research_wang_ma_2021]
- [Wang et al 2021][research_wang_zhao_2021]
- [Wang et al 2022][research_wang_song_2022]
- [Wang et al 2022][research_wang_zhao_2022]
- [Wang et al 2023][research_wang_gao_2023]
- [Wang et al 2023][research_wang_pan_2023]
- [Wang et al 2023][research_wang_sun_2023]
- [Wang et al 2023][research_wang_sun_2023_b]
- [Wang et al 2023][research_wang_wang_2023]
- [Wang et al 2023][research_wang_wang_2023_b]
- [Wang et al 2023][research_wang_xu_2023]
- [Wang et al 2023][research_wang_zhao_2023]
- [Wang et al 2023][research_wang_zhao_2023_b]
- [Wang et al 2024][research_wang_fan_2024]
- [Wang et al 2024][research_wang_fang_2024]
- [Wang et al 2024][research_wang_he_2024]
- [Wang et al 2024][research_wang_liu_2024]
- [Wang et al 2024][research_wang_pan_2024]
- [Wang et al 2024][research_wang_wang_2024]
- [Wang et al 2025][research_wang_chen_2025_b]
- [Wang et al 2025][research_wang_he_2025]
- [Wang et al 2025][research_wang_li_2025]
- [Wang et al 2025][research_wang_liu_2025]
- [Wang et al 2025][research_wang_tang_2025]
- [Wang et al 2025][research_wang_zhang_2025]
- [Wang et al 2025][research_wang_zhao_2025]
- [Wang et al 2025][research_wang_zhao_2025_b]
- [Wang et al 2026][research_wang_guan_2026]
- [Wang et al 2026][research_wang_song_2026]
- [Wang et al 2026][research_wang_yuan_2026]
- [Wang et al 2026][research_wang_zhang_2026]
- [Wang et al 2026][research_wang_zhao_2026]
- [Ward 1949][research_ward_1949]
- [Ward 1968][research_ward_1968]
- [Ward 1989][research_ward_1989]
- [Wardana et al 2022][research_wardana_cahyana_2022]
- [Washington et al 1968][research_washington_pettis_1968]
- [Wasserbauer and Gerstenmaier 1978][research_wasserbauerjf_gerstenmaierwh_1978]
- [Wasserbauer and Willoh 1968][research_wasserbauer_willoh_1968]
- [Wasserbauer et al 1985][research_wasserbauerjf_neumannhe_1985]
- [Wasserbauer et al 1996][research_wasserbauer_meleason_1996]
- [Wasserman 1952][research_wasserman_1952]
- [Watanabe et al 2019][research_watanabe_houpt_2019]
- [Watanabe et al 2019][research_watanabe_leonov_2019]
- [Watanabe et al 2023][research_watanabe_sunada_2023]
- [Watkins 2019][research_watkins_2019]
- [Watson 1953][research_watsonearlc_1953]
- [Weeks 1986][research_weeks_1986]
- [Wegener 1977][research_wegener_1977]
- [Wei et al 2022][research_wei_qu_2022]
- [Weirich and Rueger 1999][research_weirich_rueger_1999]
- [Weiss and Gegal 2014][research_weiss_gegal_2014]
- [Weissman 1973][research_weissman_1973]
- [Wen et al 2022][research_wen_kong_2022]
- [Wentz 1987][research_wentz_1987]
- [Werner and Wolter 2010][research_wernerrogera_wolterjohnd_2010]
- [Wetzel 1955][research_wetzelbentone_1955]
- [Whalen and Wilcox 1956][research_whalenpaulp_wilcoxfreda_1956]
- [Whitcomb 1953][research_whitcombrichardt_1953]
- [Whitcomb and Sevier 1960][research_whitcombrichardt_sevierjohnrjr_1960]
- [White 1997][research_white_1997]
- [White and Wills 1972][research_white_wills_1972]
- [Whitford 1991][research_whitford_1991]
- [Whitford 1995][research_whitford_1995]
- [Whittley 1952][research_whittley_1952]
- [Whoric 1973][research_whoric_1973]
- [Whoric 1977][research_whoric_1977]
- [Wilcox 1957][research_wilcoxfreda_1957]
- [Wilde and Pickerell 1968][research_wilde_pickerell_1968]
- [Williams and Butler 1963][research_williams_butler_1963]
- [Williams and Hunt 1980][research_williams_hunt_1980]
- [Williams and Stevens 2006][research_williams_stevens_2006]
- [Williams and Yost 1973][research_williams_yost_1973]
- [Willis 1981][research_willis_1981]
- [Wilson et al 1993][research_wilson_riley_1993]
- [Wilson et al 2023][research_wilson_figliola_2023]
- [Winkler 1954][research_winkler_1954]
- [Winograd and Miles 1956][research_winograd_miles_1956]
- [Wisniewski 1951][research_wisniewski_1951]
- [Woelk 1989][research_woelk_1989]
- [Won 1990][research_won_1990]
- [Wood and Livingston 1971][research_wood_livingston_1971]
- [Wood and Miller 1985][research_woodrm_millerds_1985]
- [Wood and Miller 1985][research_woodrm_millerds_1985_b]
- [Wood et al 1983][research_woodrm_millerds_1983]
- [Woodward 1956][research_woodward_1956]
- [Woollett et al 1974][research_woollett_meleason_1974]
- [Wright et al 1978][research_wright_bruckman_1978]
- [Wu et al 2022][research_wu_zhao_2022]
- [Wu et al 2024][research_wu_li_2024]
- [Wu et al 2024][research_wu_li_2024_b]
- [Wu et al 2025][research_wu_cao_2025]
- [Wu et al 2026][research_wu_du_2026]
- [Xiaokang et al 2018][research_xiaokang_kuaishe_2018]
- [Xie and Marrani 2021][research_xie_marrani_2021]
- [Xie et al 2016][research_xie_zhang_2016]
- [Xie et al 2023][research_xie_zhu_2023]
- [Xie et al 2025][research_xie_liu_2025]
- [Xie et al 2025][research_xie_ye_2025]
- [Xie et al 2025][research_xie_ye_2025_b]
- [Xin-guo et al 2015][research_xinguo_xing_2015]
- [Xinqian and Anxiong 2015][research_xinqian_anxiong_2015]
- [Xu 2023][research_xu_2023]
- [Xu and Hu 2022][research_xu_hu_2022_b]
- [Xu and Yu 2025][research_xu_yu_2025]
- [Xu et al 2020][research_xu_cheng_2020]
- [Xu et al 2021][research_xu_hu_2021]
- [Xu et al 2022][research_xu_hu_2022]
- [Xu et al 2023][research_xu_hu_2023]
- [Xu et al 2025][research_xu_wu_2025]
- [Xue et al 2020][research_xue_li_2020]
- [Xue et al 2024][research_xue_wang_2024]
- [Yadav and Guven 2015][research_yadav_guven_2015]
- [Yaghmaee and Roberts 1986][research_yaghmaee_roberts_1986]
- [Yahiaoui 2024][research_yahiaoui_2024]
- [Yajnik 1977][research_yajnik_1977]
- [Yajnik and Subbaiah 1976][research_yajnik_subbaiah_1976]
- [Yalcin 2017][research_yalcin_2017]
- [Yamaguchi 1964][research_yamaguchi_1964]
- [Yamamoto and Ng 1997][research_yamamoto_ng_1997]
- [Yamamoto et al 2020][research_yamamoto_kojima_2020]
- [Yamanaka and Kamimura 1975][research_yamanaka_kamimura_1975]
- [Yamauchi et al 1988][research_yamauchi_shibue_1988]
- [Yamazaki et al 2019][research_yamazaki_mizobata_2019]
- [Yan et al 2016][research_yan_chen_2016]
- [Yan et al 2024][research_yan_chang_2024]
- [Yan et al 2025][research_yan_pan_2025]
- [Yang and Lei 2011][research_yang_lei_2011]
- [Yang and Liu 2017][research_yang_liu_2017]
- [Yang and Yu 2026][research_yang_yu_2026]
- [Yang et al 2021][research_yang_ji_2021]
- [Yang et al 2021][research_yang_li_2021]
- [Yang et al 2021][research_yang_lu_2021]
- [Yang et al 2021][research_yang_tian_2021]
- [Yang et al 2022][research_yang_liang_2022]
- [Yang et al 2022][research_yang_lu_2022]
- [Yang et al 2022][research_yang_wu_2022]
- [Yang et al 2026][research_yang_kong_2026]
- [Yang et al 2026][research_yang_li_2026]
- [Yao et al 2017][research_yao_zhang_2017]
- [Yao et al 2022][research_yao_zhang_2022]
- [Yaylak et al 2026][research_yaylak_pinarbasi_2026]
- [Yeh 1959][research_yeh_1959]
- [Yeom et al 2015][research_yeom_sung_2015]
- [Yi and Sun 2024][research_yi_sun_2024]
- [Yih et al 1952][research_yih_cermak_1952]
- [Yongxi Lyu et al 2016][research_yongxilyu_weiguozhang_2016]
- [Yonke et al 1985][research_yonke_terrell_1985]
- [Yonke et al 1995][research_yonkewilliama_robbendaniell_1995]
- [York et al 2018][research_york_ozturk_2018]
- [Yoshida 2009][research_yoshida_2009]
- [You et al 2016][research_you_yu_2016]
- [Yu et al 2021][research_yu_huang_2021]
- [Yu et al 2021][research_yu_ni_2021]
- [Yu et al 2025][research_yu_guo_2025]
- [Yu et al 2025][research_yu_wang_2025]
- [Yu et al 2026][research_yu_yu_2026]
- [Yu et al 2026][research_yu_zhao_2026]
- [Yuan et al 2021][research_yuan_liu_2021]
- [Yuan et al 2021][research_yuan_zhang_2021]
- [Yuan et al 2023][research_yuan_li_2023]
- [Yuan et al 2026][research_yuan_lu_2026]
- [Yusof and Rahim 2017][research_yusof_rahim_2017]
- [Zachos et al 2016][research_zachos_macmanus_2016]
- [Zahir et al 2023][research_zahir_aamer_2023]
- [Zaidi 1988][research_zaidi_1988]
- [Zaman et al 2025][research_zaman_korth_2025]
- [Zebbiche and Youbi 2023][research_zebbiche_youbi_2023]
- [Zhang 2020][research_zhang_2020]
- [Zhang 2020][research_zhang_2020_b]
- [Zhang 2024][research_zhang_2024]
- [Zhang and Hou 2015][research_zhang_hou_2015]
- [Zhang and Malekgoudarzi 2020][research_zhang_malekgoudarzi_2020]
- [Zhang and Vahdati 2018][research_zhang_vahdati_2018]
- [Zhang and Vahdati 2019][research_zhang_vahdati_2019]
- [Zhang and Wang 2022][research_zhang_wang_2022]
- [Zhang and Wu 2026][research_zhang_wu_2026]
- [Zhang et al 2009][research_zhang_zhou_2009]
- [Zhang et al 2015][research_zhang_chen_2015]
- [Zhang et al 2015][research_zhang_tan_2015]
- [Zhang et al 2016][research_zhang_yu_2016]
- [Zhang et al 2018][research_zhang_tan_2018]
- [Zhang et al 2020][research_zhang_stapelfeldt_2020]
- [Zhang et al 2020][research_zhang_yuan_2020]
- [Zhang et al 2021][research_zhang_du_2021]
- [Zhang et al 2021][research_zhang_li_2021]
- [Zhang et al 2022][research_zhang_lu_2022]
- [Zhang et al 2024][research_zhang_an_2024]
- [Zhang et al 2024][research_zhang_chen_2024]
- [Zhang et al 2024][research_zhang_liu_2024]
- [Zhang et al 2024][research_zhang_zhang_2024_b]
- [Zhang et al 2025][research_zhang_ji_2025]
- [Zhang et al 2025][research_zhang_yang_2025]
- [Zhang et al 2026][research_zhang_bo_2026]
- [Zhang et al 2026][research_zhang_ning_2026]
- [Zhang et al 2026][research_zhang_yang_2026]
- [Zhang et al 2026][research_zhang_zhang_2026]
- [Zhao et al 2017][research_zhao_sun_2017]
- [Zhao et al 2019][research_zhao_zhou_2019]
- [Zhao et al 2022][research_zhao_vanhoorn_2022]
- [Zhao et al 2022][research_zhao_zhou_2022]
- [Zhao et al 2023][research_zhao_jin_2023]
- [Zhao et al 2025][research_zhao_jin_2025]
- [Zhao et al 2025][research_zhao_li_2025]
- [Zheldubovskii and Ishchenko 1982][research_zheldubovskii_ishchenko_1982]
- [Zhipeng et al 2015][research_zhipeng_chao_2015]
- [Zhong et al 2024][research_zhong_yu_2024]
- [Zhou et al 2019][research_zhou_li_2019]
- [Zhu and Yang 2020][research_zhu_yang_2020]
- [Zhu and Zhao 2016][research_zhu_zhao_2016]
- [Zhu et al 2018][research_zhu_chen_2018]
- [Zhu et al 2018][research_zhu_lee_2018]
- [Zhu et al 2020][research_zhu_luo_2020]
- [Zhu et al 2022][research_zhu_gu_2022]
- [Zhuang and Lu 2015][research_zhuang_lu_2015]
- [Zien and Ragsdale 1979][research_zien_ragsdale_1979]
- [Zimmerman 1935][research_zimmermanch_1935]
- [Zubair et al 2022][research_zubair_ejaz_2022]
- [Zuo 2021][research_zuo_2021]
- [Zuo 2023][research_zuo_2023]
- [Ünal et al 2023][research_unal_oz_2023]

[research_a_canadian_1940]: https://doi.org/10.1108/eb030618
[research_a_comparison_1977]: https://doi.org/10.7249/p6011
[research_a_conference_1954]: https://doi.org/10.1108/eb032393
[research_a_new_2003]: https://doi.org/10.1017/cbo9780511809415.015
[research_a_study_2004]: https://doi.org/10.5139/jksas.2004.32.8.029
[research_abate_vasista_2023]: https://doi.org/10.1115/smasis2023-110999
[research_abbasi_pirnia_2018]: https://doi.org/10.15632/jtam-pl.56.4.1005
[research_abdelfattah_1996]: https://doi.org/10.1115/96-gt-206
[research_abdelghany_2025]: https://doi.org/10.21608/ijaes.2024.319394.1027
[research_abdelwahabm_1977]: https://ntrs.nasa.gov/citations/19770024209
[research_abdelwahabm_1981]: https://ntrs.nasa.gov/citations/19820010348
[research_abdolahipour_mani_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001463
[research_abdolahipour_mani_2022_b]: https://doi.org/10.1007/s10494-022-00327-9
[research_abdulhamitbilal_sal_2021]: https://doi.org/10.1115/gt2021-58503
[research_abdulkaiyoom_yildirim_2025]: https://doi.org/10.2514/1.c037678
[research_abedi_askari_2020]: https://doi.org/10.1016/j.ast.2019.105547
[research_abedi_askari_2020_b]: https://doi.org/10.1016/j.jppr.2020.01.002
[research_abraham_lazzara_2024]: https://doi.org/10.3390/aerospace11050359
[research_abrahamson_1988]: https://doi.org/10.2514/6.1988-2588
[research_abusalem_palaia_2023_b]: https://doi.org/10.3390/aerospace10050459
[research_adamczyk_kozakiewicz_2024]: https://doi.org/10.2139/ssrn.5076740
[research_adamsjcjr_martindalewr_1984]: https://ntrs.nasa.gov/citations/19840035307
[research_aerodynamic_and_1960]: https://ntrs.nasa.gov/citations/19980228350
[research_aerodynamic_drag_2020]: https://doi.org/10.1002/9781119667063.ch7
[research_afanasev_nikitin_2019]: https://doi.org/10.3103/s1068798x1901012x
[research_afridi_khan_2024]: https://doi.org/10.1115/1.4064608
[research_agungsaputra_bhimashaktiarafat_2026]: https://doi.org/10.55606/teknik.v6i1.8537
[research_ahmad_zheng_2021]: https://doi.org/10.24200/sci.2021.56486.4742
[research_ahuja_mavris_2022]: https://doi.org/10.2514/1.c036654
[research_aircraft_basic_1995]: https://doi.org/10.2514/5.9781600868535.0001.0028
[research_aircraft_drag_2010]: https://doi.org/10.1017/cbo9780511844652.011
[research_aircraft_performance_2010]: https://doi.org/10.1017/cbo9780511844652.015
[research_aircraft_steady_2011_c]: https://doi.org/10.2307/j.ctvcm4h26.14
[research_aircraft_steady_2011_d]: https://doi.org/10.2307/j.ctvcm4h26.15
[research_airforceresearchlabedwardsafbca_2000]: https://doi.org/10.21236/ada404927
[research_airforcetestpilotschooledwardsafbca_1989]: https://doi.org/10.21236/ada319980
[research_airforcetestpilotschooledwardsafbca_1990]: https://doi.org/10.21236/ada319976
[research_airforcetestpilotschooledwardsafbca_1990_b]: https://doi.org/10.21236/ada319978
[research_ajain_2025]: https://doi.org/10.21275/sr251223120745
[research_ajay_kundu_2025]: https://doi.org/10.1017/aer.2025.7
[research_ak_ps_2018]: https://doi.org/10.1108/aeat-12-2017-0275
[research_akhlaghi_azizi_2022]: https://doi.org/10.3390/machines10080706
[research_akhlaghi_azizi_2023]: https://doi.org/10.3390/aerospace10090763
[research_albuquerque_gamboa_2018]: https://doi.org/10.2514/1.c034403
[research_aleisa_kontis_2023]: https://doi.org/10.2514/1.c037257
[research_alendar_grunin_2022]: https://doi.org/10.3103/s1068798x2207005x
[research_alexander_harris_1992]: https://ntrs.nasa.gov/citations/19940035347
[research_alford_davies_1962]: https://doi.org/10.4271/620300
[research_ali_asghar_2017]: https://doi.org/10.13033/ijahp.v9i2.489
[research_ali_khan_2025]: https://doi.org/10.55524/ijircst.2025.13.3.24
[research_allen_beke_1953]: https://ntrs.nasa.gov/citations/19930087574
[research_allen_davis_1960]: https://ntrs.nasa.gov/citations/19630006259
[research_allen_mahorter_1964]: https://doi.org/10.21236/ad0609355
[research_allison_morris_2015]: https://doi.org/10.12989/aas.2015.2.1.017
[research_almuradi_2021]: https://doi.org/10.15866/irease.v14i1.17303
[research_alone_kumar_2016]: https://doi.org/10.1016/j.jppr.2016.01.009
[research_alshamma_ali_2017]: https://doi.org/10.5937/jaes15-14829
[research_amann_nordenson_1975]: https://doi.org/10.1115/1.3445996
[research_amatucci_addy_1982]: https://doi.org/10.2514/3.7977
[research_analysis_of_2021]: https://doi.org/10.47939/et.v2i6.122
[research_analysis_of_2024]: https://doi.org/10.47176/jafm.17.02.2101
[research_anantachaisilp_lin_2020]: https://doi.org/10.3390/act9030075
[research_ananthapadmanaban_murganandam_2016]: https://doi.org/10.2514/6.2016-5072
[research_anatomy_of_1970]: https://doi.org/10.1016/0010-4361(70)90311-3
[research_anderson_1984]: https://doi.org/10.2514/6.1984-194
[research_anderson_1985]: https://doi.org/10.2514/3.45218
[research_anderson_1989]: https://doi.org/10.2514/6.1989-15
[research_anderson_berger_1973]: https://doi.org/10.2514/3.60204
[research_anderson_dryer_1957]: https://ntrs.nasa.gov/citations/19640057037
[research_anderson_petersen_1966]: https://ntrs.nasa.gov/citations/19750065518
[research_anderson_wong_1969]: https://ntrs.nasa.gov/citations/19690054743
[research_andersonadriene_1947]: https://ntrs.nasa.gov/citations/19930085723
[research_andersonbernhardh_levyralph_1991]: https://ntrs.nasa.gov/citations/19920004741
[research_andersonbernhardh_weirlois_2014]: https://ntrs.nasa.gov/citations/20140016538
[research_andersonbh_bowditchdn_1958]: https://ntrs.nasa.gov/citations/19650013032
[research_andersonbh_bowditchdn_1960]: https://ntrs.nasa.gov/citations/19630002315
[research_andersonsethb_brayrichards_1951]: https://ntrs.nasa.gov/citations/19930086840
[research_andersonsethb_brayrichards_1955]: https://ntrs.nasa.gov/citations/19930092243
[research_andrews_1969]: https://doi.org/10.2514/3.44090
[research_anglin_1978]: https://doi.org/10.2514/3.58445
[research_anglin_satran_1980]: https://doi.org/10.2514/3.57980
[research_anicetti_2023]: https://doi.org/10.4324/9781003396956-5
[research_anon_2015]: https://doi.org/10.15623/ijret.2015.0409049
[research_anon_2016]: https://doi.org/10.15623/ijret.2016.0505016
[research_anon_2024]: https://doi.org/10.36948/ijfmr.2024.v06i01.11628
[research_ansari_m_2022]: https://doi.org/10.47893/gret.2022.1086
[research_antaranalbert_beletehailu_1992]: https://ntrs.nasa.gov/citations/19930008977
[research_anti_surge_control_2021]: https://doi.org/10.47939/et.v2i10.438
[research_anti_surge_reason_2021]: https://doi.org/10.47939/et.v2i3.33
[research_aoyagikiyoshi_hickeydavidh_1959]: https://ntrs.nasa.gov/citations/19980228317
[research_application_of_2021]: https://doi.org/10.47939/et.v2i7.51
[research_application_of_2021_b]: https://doi.org/10.47939/et.v2i5.118
[research_application_practice_2021]: https://doi.org/10.47939/et.v2i10.366
[research_araujo_pereira_2021]: https://doi.org/10.1016/j.ast.2021.106864
[research_archbold_1945]: https://doi.org/10.1017/s0001924000108632
[research_aribi_boushaki_2023]: https://doi.org/10.37394/232016.2023.18.1
[research_arif_iftikhar_2021]: https://doi.org/10.1177/09544100211002970
[research_arkoosh_fiore_1972]: https://doi.org/10.1007/bf02643237
[research_arlinger_1976]: https://doi.org/10.1007/978-3-642-81005-3_21
[research_armstrong_palladino_1980]: https://doi.org/10.21236/ada093156
[research_armywarcollcarlislebarrackspa_1952]: https://doi.org/10.21236/ada390507
[research_arnson_aljaber_2026]: https://doi.org/10.2514/1.c038387
[research_arthurw_2022]: https://doi.org/10.2514/5.9781624106255.0407.0412
[research_ashry_kamel_2019]: https://doi.org/10.2514/6.2019-3911
[research_ashwood_1973]: https://doi.org/10.2514/3.60249
[research_askari_abedi_2026]: https://doi.org/10.1016/j.flowmeasinst.2025.103045
[research_askari_soltani_2017]: https://doi.org/10.24200/sci.2017.4495
[research_askari_soltani_2019]: https://doi.org/10.2514/1.c035328
[research_askari_soltani_2019_b]: https://doi.org/10.29252/jafm.12.06.29880
[research_askari_soltani_2020]: https://doi.org/10.2514/1.j059006
[research_askari_soltani_2022]: https://doi.org/10.2514/1.j061201
[research_askari_soltani_2023]: https://doi.org/10.2514/1.c037043
[research_assessment_of]: https://doi.org/10.4271/air5867
[research_assessment_of_2023_b]: https://doi.org/10.47176/jafm.16.09.1749
[research_atassi_kozlov_2019]: https://doi.org/10.1115/1.4043963
[research_atesoglu_ozgoren_2006]: https://doi.org/10.2514/6.2006-6056
[research_atesoglu_ozgoren_2007]: https://doi.org/10.2514/1.28620
[research_auman_1993]: https://doi.org/10.2514/6.1993-36
[research_awerbuch_1980]: https://doi.org/10.21236/ada111006
[research_axelsonjohna_crownjconrad_1948]: https://ntrs.nasa.gov/citations/19930085834
[research_axial_transonic_2022]: https://doi.org/10.55787/jtams.22.52.2.144
[research_ayers_1962]: https://doi.org/10.1108/eb033637
[research_ayres_1977]: https://doi.org/10.1007/bf02661760
[research_azevedo_liu_1990]: https://doi.org/10.2514/3.10486
[research_azizi_brouwer_2017]: https://doi.org/10.1016/j.jpowsour.2017.09.010
[research_babaei_setayandeh_2018]: https://doi.org/10.1016/j.cja.2018.04.018
[research_babinsky_2014]: https://doi.org/10.21236/ada602774
[research_babu_2021]: https://doi.org/10.1007/978-3-030-79945-8_5
[research_babu_2021_b]: https://doi.org/10.1007/978-3-030-79945-8_6
[research_back_massier_1967]: https://doi.org/10.2514/3.29015
[research_background_the_1998]: https://doi.org/10.2514/5.9781600867910.0005.0036
[research_backlh_cuffelrf_1966]: https://ntrs.nasa.gov/citations/19670036104
[research_baerst_hughes_1978]: https://doi.org/10.2514/6.1978-965
[research_bagby_andersen_1966]: https://doi.org/10.2514/3.43750
[research_bai_deng_2026]: https://doi.org/10.2139/ssrn.7237152
[research_baidya_pesyridis_2018]: https://doi.org/10.3390/app8040574
[research_baker_1966]: https://doi.org/10.2514/3.43708
[research_bakhlemilinda_reddytsr_2018]: https://ntrs.nasa.gov/citations/20180002211
[research_balashov_petukhov_1969]: https://doi.org/10.1007/bf01543222
[research_ball_ross_1972]: https://doi.org/10.2514/3.59042
[research_balli_caliskan_2021]: https://doi.org/10.1016/j.energy.2021.121031
[research_bammert_mobarak_1976]: https://doi.org/10.1115/1.3446140
[research_bammert_mobarak_1976_b]: https://doi.org/10.1115/1.3446141
[research_ban_yamazaki_2018]: https://doi.org/10.2514/1.c034171
[research_bangert_santman_1980]: https://ntrs.nasa.gov/citations/19810009475
[research_bangert_santman_1982]: https://doi.org/10.2514/3.57356
[research_banks_quinto_1981]: https://doi.org/10.2514/6.1981-2612
[research_banksdanielw_paulsonjohnwjr_1987]: https://ntrs.nasa.gov/citations/19870005747
[research_baretter_godard_2021]: https://doi.org/10.3390/ijtpp6040043
[research_barham_1994]: https://doi.org/10.2514/6.1994-2105
[research_barnhart_1988]: https://ntrs.nasa.gov/citations/19880065910
[research_baron_1953]: https://doi.org/10.2514/8.2565
[research_barone_nicholson_2022]: https://doi.org/10.1103/physrevfluids.7.084604
[research_barr_muralidharan_2020]: https://doi.org/10.2514/6.2020-1366
[research_barr_ogara_2018]: https://doi.org/10.2514/6.2018-4842
[research_barry_1966]: https://doi.org/10.2514/6.1966-367
[research_barry_1971]: https://doi.org/10.2514/3.44269
[research_barryfw_1968]: https://ntrs.nasa.gov/citations/19710028359
[research_baryshev_vinogradov_1972]: https://doi.org/10.1007/bf01186475
[research_batayev_suleimenov_2022]: https://doi.org/10.11591/ijece.v12i2.pp1419-1428
[research_battertonpg_arpasidj_1974]: https://ntrs.nasa.gov/citations/19740025659
[research_battiston_magrini_2025]: https://doi.org/10.2514/1.c038084
[research_bauerstevenxs_mcmillinsnaomi_1988]: https://ntrs.nasa.gov/citations/19880053539
[research_bayati_williston_1977]: https://doi.org/10.2514/6.1977-836
[research_baydar_lu_2018]: https://doi.org/10.2514/1.b36414
[research_baydarezgihan_lufrankk_2016]: https://ntrs.nasa.gov/citations/20170000948
[research_baydarezgihan_lufrankk_2017]: https://ntrs.nasa.gov/citations/20170001419
[research_beale_miller_1975]: https://doi.org/10.21236/ada014231
[research_beaufrere_1988]: https://doi.org/10.2514/6.1988-4503
[research_beck_cord_1995]: https://doi.org/10.2514/6.1995-3448
[research_beesly_1966]: https://doi.org/10.1108/eb034195
[research_beesly_1966_b]: https://doi.org/10.1049/tpe.1966.0073
[research_behavior_patterns_2022]: https://doi.org/10.55802/ijb.027(3).004
[research_beheimma_gertsmalw_1956]: https://ntrs.nasa.gov/citations/19630002647
[research_beke_allen_1953]: https://ntrs.nasa.gov/citations/19930087580
[research_benaouali_kachel_2019]: https://doi.org/10.1016/j.ast.2019.06.040
[research_benichou_binder_2021]: https://doi.org/10.3390/ijtpp6030034
[research_bennetclark_1972]: https://doi.org/10.1038/239451b0
[research_bennett_1990]: https://doi.org/10.2514/6.1990-3223
[research_bennett_2003]: https://doi.org/10.21236/ada415479
[research_benson_1994]: https://ntrs.nasa.gov/citations/19940025669
[research_benson_anderson_1983]: https://doi.org/10.2514/6.1983-540
[research_bensonthomasj_1997]: https://ntrs.nasa.gov/citations/20050179350
[research_benton_humphrey_2021]: https://doi.org/10.2514/6.2021-0879
[research_bera_1975]: https://doi.org/10.2514/3.44499
[research_bera_1980]: https://doi.org/10.1080/0020739800110412
[research_berezovsky_2018]: https://doi.org/10.15588/1727-0219-2018-1-6
[research_bergstedt_turner_1959]: https://doi.org/10.21236/ad0402171
[research_berto_benini_2020]: https://doi.org/10.2514/1.j058764
[research_bertrammh_ulmannef_1953]: https://ntrs.nasa.gov/citations/19630010653
[research_bezborodova_filinov_2021]: https://doi.org/10.1109/ec52789.2021.10016815
[research_bhandari_gaur_2025]: https://doi.org/10.1016/j.engfailanal.2025.109534
[research_bhunia_abbas_2026]: https://doi.org/10.61653/joast.v78i2.2026.1160
[research_bianchi_secco_2020]: https://doi.org/10.1017/aer.2020.134
[research_bielatralphp_1959]: https://ntrs.nasa.gov/citations/19980232001
[research_biesiadny_lee_1978]: https://ntrs.nasa.gov/citations/19780015152
[research_biesiadnythomasj_wendtbrucej_2004]: https://ntrs.nasa.gov/citations/20050040781
[research_bihrle_barnhart_1982]: https://doi.org/10.2514/3.44789
[research_bihrle_jr_1980]: https://doi.org/10.21236/ada082335
[research_bilanin_donaldson_1975]: https://doi.org/10.2514/3.44476
[research_bilwakeshkr_doylevl_1971]: https://ntrs.nasa.gov/citations/19710023725
[research_bilwakeshkr_kochcc_1972]: https://ntrs.nasa.gov/citations/19720020168
[research_birch_paynter_1978]: https://doi.org/10.2514/3.58395
[research_birdjohnd_lichtensteinjacobh_1952]: https://ntrs.nasa.gov/citations/19930083189
[research_biriukov_1959]: https://doi.org/10.1016/0021-8928(59)90174-1
[research_birkler_2001]: https://doi.org/10.7249/rb7111
[research_bisek_2014]: https://doi.org/10.2514/6.2014-3335
[research_bisek_2015]: https://doi.org/10.2514/6.2015-1976
[research_bisek_rizzetta_2012]: https://doi.org/10.2514/6.2012-2700
[research_biswas_michels_2026]: https://doi.org/10.2514/6.2026-0511
[research_blake_leggett_1990]: https://doi.org/10.2514/6.1990-1820
[research_blank_shinar_1982]: https://doi.org/10.2514/3.19763
[research_bleviss_struble_1954]: https://doi.org/10.2514/8.3176
[research_bloxsom_1958]: https://doi.org/10.2514/8.7403
[research_bogar_sajben_1983]: https://doi.org/10.2514/6.1983-2017
[research_bogdan_2015]: https://doi.org/10.21236/ad1019428
[research_boger_greer_1989]: https://doi.org/10.21236/ada207345
[research_boger_nussbaum_1990]: https://doi.org/10.21236/ada229704
[research_bollechthomasv_kellyhneale_1954]: https://ntrs.nasa.gov/citations/20090022756
[research_bond_brown_2025]: https://doi.org/10.2514/1.j065421
[research_bond_key_2025]: https://doi.org/10.1115/1.4070057
[research_bond_key_2026]: https://doi.org/10.2514/1.j066481
[research_boussios_epstein_1992]: https://doi.org/10.21236/ada252771
[research_bouzekovapenkova_miteva_2022]: https://doi.org/10.3897/arb.v34.e15
[research_bowditch_1973]: https://ntrs.nasa.gov/citations/19740001909
[research_bowditch_musial_1957]: https://ntrs.nasa.gov/citations/19710065189
[research_bowditchdn_coltrinre_1983]: https://ntrs.nasa.gov/citations/19830064291
[research_bowers_1981]: https://doi.org/10.2514/3.57530
[research_boytos_1969]: https://doi.org/10.2514/3.44107
[research_braithwaite_soeder_1980]: https://doi.org/10.2514/3.57927
[research_braithwaitewm_1973]: https://ntrs.nasa.gov/citations/19740002609
[research_braithwaitewm_soederrh_1979]: https://ntrs.nasa.gov/citations/19790015792
[research_branger_1972]: https://doi.org/10.1016/b978-0-08-016566-0.50014-1
[research_branstetterjr_juhaszaj_1971]: https://ntrs.nasa.gov/citations/19710009407
[research_brantley_stabrylla_1979]: https://ntrs.nasa.gov/citations/19790015799
[research_braun_podleski_2019]: https://doi.org/10.2514/6.2019-4021
[research_bravomosquera_abdalla_2019]: https://doi.org/10.1016/j.ast.2019.01.059
[research_breaks_1973]: https://doi.org/10.2514/3.60235
[research_breugelmans_1975]: https://doi.org/10.1115/75-gt-26
[research_briggsbenjaminr_1960]: https://ntrs.nasa.gov/citations/19980227791
[research_brignac_ness_1976]: https://ntrs.nasa.gov/citations/19770014094
[research_brilliant_bauer_1977]: https://ntrs.nasa.gov/citations/19770055718
[research_brinich_1961]: https://ntrs.nasa.gov/citations/19980228285
[research_briones_rankin_2024]: https://doi.org/10.1115/gt2024-121649
[research_bristol_siddeley_1963]: https://doi.org/10.1108/eb033682
[research_broadley_hewitt_2023]: https://doi.org/10.1017/jfm.2023.505
[research_brodrick_1976]: https://doi.org/10.1520/jte10526j
[research_brodsky_1970]: https://doi.org/10.21236/ad0716026
[research_brodzik_2024_b]: https://doi.org/10.31648/ts.10159
[research_brophy_hawk_1990]: https://doi.org/10.21236/ada378098
[research_brown_1961]: https://doi.org/10.4271/610096
[research_brown_1970]: https://doi.org/10.21236/ad0712047
[research_brownclintone_1946]: https://ntrs.nasa.gov/citations/19930090940
[research_browne_friedman_1948]: https://doi.org/10.2514/8.11620
[research_brownstuartc_1959]: https://ntrs.nasa.gov/citations/19980228294
[research_bryant_1933]: https://doi.org/10.1108/eb029696
[research_brycelhorvath_douglaspwells_2018]: https://ntrs.nasa.gov/citations/20190000431
[research_bryson_rumpfkeil_2019]: https://doi.org/10.2514/1.c035152
[research_bsaheby_shen_2019]: https://doi.org/10.1177/0954410019875384
[research_buchholzmarkd_1992]: https://ntrs.nasa.gov/citations/19940019630
[research_buchholzmarkd_tsojin_1993]: https://ntrs.nasa.gov/citations/19970022303
[research_bullg_bridgespd_1983]: https://ntrs.nasa.gov/citations/19840029551
[research_bunton_denegri_2000]: https://doi.org/10.2514/2.2690
[research_bureauofaeronauticsnavywashingtondc_1949]: https://doi.org/10.21236/ad0223596
[research_burkhalter_1982]: https://doi.org/10.2514/3.44793
[research_burns_kirchgessner_1987]: https://ntrs.nasa.gov/citations/19870020104
[research_burns_koo_2015]: https://doi.org/10.2514/1.j053049
[research_burris_1966]: https://doi.org/10.2514/6.1966-741
[research_burrows_vukasinovic_2025]: https://doi.org/10.2514/1.c037992
[research_burstadtpl_calogerasje_1971]: https://ntrs.nasa.gov/citations/19710050036
[research_burstadtpl_calogerasje_1974]: https://ntrs.nasa.gov/citations/19740022130
[research_burstadtpl_wenzellm_1976]: https://ntrs.nasa.gov/citations/19760055251
[research_burwell_patterson_1985]: https://doi.org/10.2514/6.1985-1430
[research_bush_1985]: https://doi.org/10.2514/6.1985-1521
[research_bushnell_1990]: https://doi.org/10.2514/6.1990-1596
[research_butler_1982]: https://doi.org/10.2514/3.44764
[research_butter_hancock_1971]: https://doi.org/10.1017/s0001924000046133
[research_buzica_breitsamter_2020]: https://doi.org/10.3390/aerospace7010004
[research_bykerk_verstraete_2020]: https://doi.org/10.1016/j.ast.2019.105531
[research_caap_elemeland_1986]: https://doi.org/10.2514/6.1986-1771
[research_cabreracruz_pezzini_2020]: https://doi.org/10.1115/1.4045218
[research_caddy_arnold_1988]: https://doi.org/10.1115/88-gt-303
[research_cai_huang_2022]: https://doi.org/10.3390/en15113879
[research_cai_huang_2022_b]: https://doi.org/10.3390/en15145057
[research_cai_huang_2022_c]: https://doi.org/10.3389/fenrg.2022.884540
[research_callahan_stenning_1971]: https://doi.org/10.2514/3.44259
[research_calligeros_dugundji_1961]: https://doi.org/10.21236/ad0253970
[research_calogerasje_burstadtpl_1974]: https://ntrs.nasa.gov/citations/19740021193
[research_calogerasje_coltrinre_1969]: https://ntrs.nasa.gov/citations/19690054687
[research_calogerasje_johnsenrl_1974]: https://ntrs.nasa.gov/citations/19740014513
[research_campbell_1976]: https://doi.org/10.2514/3.58703
[research_campbell_ellis_1971]: https://doi.org/10.2514/3.59101
[research_campbell_syberg_1984]: https://doi.org/10.2514/6.1984-1275
[research_campbell_syberg_1985]: https://doi.org/10.2514/3.22794
[research_campion_1954]: https://doi.org/10.1017/s0001925900001232
[research_canard_leading_edge_2007]: https://doi.org/10.5139/jksas.2007.35.2.165
[research_cao_yuan_2022]: https://doi.org/10.1007/s11630-022-1551-7
[research_cao_zhang_2023]: https://doi.org/10.1016/j.mtcomm.2023.106796
[research_capello_ferrero_2019]: https://doi.org/10.2514/6.2019-4311
[research_capone_1979]: https://doi.org/10.2514/6.1979-1810
[research_capone_berrier_1980]: https://ntrs.nasa.gov/citations/19800015775
[research_caponefj_reubushde_1983]: https://ntrs.nasa.gov/citations/19830018550
[research_carew_crossley_1956]: https://doi.org/10.21236/ad0102829
[research_carey_1982]: https://doi.org/10.2307/2617820
[research_carlincm_frischi_2003]: https://ntrs.nasa.gov/citations/20030065839
[research_carlson_schwope_1952]: https://doi.org/10.21236/ada076046
[research_carlyle_1976]: https://doi.org/10.21236/ada956001
[research_carnevale_wang_2016]: https://doi.org/10.1115/1.4034600
[research_carreyette_1950]: https://doi.org/10.1108/eb031848
[research_carrier_knight_2001]: https://doi.org/10.2514/6.2001-1064
[research_cassetti_1978]: https://doi.org/10.1108/eb035480
[research_casteel_weyl_1970]: https://doi.org/10.2514/6.1970-928
[research_castner_simerly_2018]: https://doi.org/10.2514/6.2018-2850
[research_castner_zaman_2017]: https://doi.org/10.2514/1.c033623
[research_castor_1983]: https://doi.org/10.2514/6.1983-1338
[research_cate_2003]: https://doi.org/10.21236/ada416312
[research_cervay_1972]: https://doi.org/10.21236/ad0753709
[research_cervay_1975]: https://doi.org/10.21236/ada021689
[research_cess_1964]: https://doi.org/10.1115/1.3687123
[research_cevik_ducvo_2016]: https://doi.org/10.1115/1.4033420
[research_chai_li_2020]: https://doi.org/10.1016/j.ast.2020.106000
[research_chai_song_2017]: https://doi.org/10.1016/j.actaastro.2017.08.016
[research_chambers_bowman_1971]: https://doi.org/10.2514/3.59136
[research_chaney_1999]: https://ntrs.nasa.gov/citations/20000044624
[research_chang_hsu_1960]: https://doi.org/10.2514/8.5121
[research_chang_nordheim_1953]: https://doi.org/10.21236/ad0000961
[research_chapman_1979]: https://doi.org/10.21236/ada082821
[research_chapmandave_smithcf_2005]: https://ntrs.nasa.gov/citations/20050061002
[research_cheidris_saad_2020]: https://doi.org/10.37934/arfmts.77.1.110
[research_cheikh_chen_2017]: https://doi.org/10.2514/6.2017-3460
[research_chell_hoffenson_2021]: https://doi.org/10.1115/1.4049657
[research_chen_chen_2021]: https://doi.org/10.1515/tjj-2021-0045
[research_chen_chen_2023]: https://doi.org/10.1088/1742-6596/2441/1/012001
[research_chen_he_2025]: https://doi.org/10.1177/16878132251348391
[research_chen_li_2020]: https://doi.org/10.1016/j.jde.2019.12.018
[research_chen_martinez_2025]: https://doi.org/10.64631/abcd8901
[research_chen_mi_2020]: https://doi.org/10.3390/ma13153358
[research_chen_mi_2021]: https://doi.org/10.1016/j.matlet.2021.129575
[research_chen_mi_2022]: https://doi.org/10.1016/j.coco.2022.101077
[research_chen_sethuraman_2025]: https://doi.org/10.1016/j.ast.2025.110262
[research_chen_tan_2017]: https://doi.org/10.2514/1.j056066
[research_chen_tan_2018]: https://doi.org/10.2514/1.j056674
[research_chen_tan_2019]: https://doi.org/10.1016/j.ast.2019.105471
[research_chen_tan_2019_b]: https://doi.org/10.2514/1.j057811
[research_chen_wang_2013]: https://doi.org/10.4028/www.scientific.net/msf.770.329
[research_chen_wu_2026]: https://doi.org/10.1063/5.0348275
[research_chen_xia_2022]: https://doi.org/10.3390/aerospace9120835
[research_chen_yang_2025]: https://doi.org/10.3390/computation13040101
[research_chen_yue_2021]: https://doi.org/10.1016/j.cja.2021.01.020
[research_chen_zhang_2020]: https://doi.org/10.1177/0954410020944068
[research_chen_zhang_2021_b]: https://doi.org/10.1016/j.ast.2021.106539
[research_chen_zheng_2026]: https://doi.org/10.1016/j.ast.2025.110751
[research_chen_zhu_2024]: https://doi.org/10.2139/ssrn.5009866
[research_cheng_huang_2024]: https://doi.org/10.1088/1742-6596/2683/1/012027
[research_cheng_yue_2016]: https://doi.org/10.5028/jatm.v8i1.514
[research_chengt_greitzerem_1987]: https://ntrs.nasa.gov/citations/19870058127
[research_chennuru_corral_2025]: https://doi.org/10.1115/1.4070233
[research_chester_1953]: https://doi.org/10.1017/s0001925900000950
[research_chi_chu_2022]: https://doi.org/10.1177/09544100211063079
[research_childrd_hendersonwp_1978]: https://ntrs.nasa.gov/citations/19780063995
[research_chima_2011]: https://ntrs.nasa.gov/citations/20110023757
[research_chima_2011_b]: https://doi.org/10.2514/6.2011-3801
[research_chima_conners_2009]: https://ntrs.nasa.gov/citations/20100041304
[research_chima_conners_2010]: https://ntrs.nasa.gov/citations/20100024366
[research_chimarodrickv_2011]: https://ntrs.nasa.gov/citations/20110011335
[research_chimarodrickv_2012]: https://ntrs.nasa.gov/citations/20120009203
[research_chimarodrickv_hirtstefaniem_2011]: https://ntrs.nasa.gov/citations/20110023762
[research_chin_1977]: https://doi.org/10.2514/3.60721
[research_chin_1978]: https://doi.org/10.2514/3.7537
[research_cho_findley_1983]: https://doi.org/10.21236/ada137976
[research_choe_kim_2016]: https://doi.org/10.2514/6.2016-3564
[research_choe_kim_2020]: https://doi.org/10.2514/1.b37474
[research_choi_2024]: https://doi.org/10.1007/s12206-024-0533-y
[research_choi_2026]: https://doi.org/10.2139/ssrn.6742239
[research_choi_choi_2026]: https://doi.org/10.1016/j.ast.2026.113190
[research_chou]: https://doi.org/10.31274/rtd-180813-10072
[research_chou_smith_1974]: https://doi.org/10.21236/ada001135
[research_chun_burr_1969]: https://doi.org/10.2514/3.44056
[research_chun_swanson_1964]: https://doi.org/10.2514/6.1964-598
[research_chung_1994]: https://doi.org/10.2514/6.1994-583
[research_ciepluchcarlc_1948]: https://ntrs.nasa.gov/citations/20050040787
[research_clark_1995]: https://doi.org/10.2514/6.1995-36
[research_clarke_wallace_1964]: https://doi.org/10.1017/s0022112064000179
[research_clarkle_richiecb_1977]: https://ntrs.nasa.gov/citations/19770017117
[research_cliett_1952]: https://doi.org/10.21236/ad0006050
[research_coalson_1968]: https://doi.org/10.21236/ad0833750
[research_coalson_csavina_1976]: https://doi.org/10.2514/3.58723
[research_coble_royster_2014]: https://doi.org/10.21236/ada608062
[research_coe_kulla_1974]: https://doi.org/10.2514/3.60383
[research_coen_foss_1985]: https://doi.org/10.2514/6.1985-212
[research_coepljr_1976]: https://ntrs.nasa.gov/citations/19760053942
[research_colbourne_1980]: https://doi.org/10.1017/s0001925900008891
[research_colejb_1980]: https://ntrs.nasa.gov/citations/19800015023
[research_coltrin_1987]: https://ntrs.nasa.gov/citations/19880006429
[research_composite_material_1978]: https://doi.org/10.1016/0010-4361(78)90398-1
[research_concept_designed_1995]: https://ntrs.nasa.gov/citations/20050169187
[research_cong_yu_2024]: https://doi.org/10.1007/s42401-024-00312-2
[research_conners_howe_2006]: https://doi.org/10.2514/6.2006-30
[research_connors_lovell_1957]: https://ntrs.nasa.gov/citations/19930089784
[research_connorsjamesf_wisegeorgea_1957]: https://ntrs.nasa.gov/citations/19930089864
[research_control_system_1976]: https://doi.org/10.1016/0010-4485(76)90126-3
[research_conway_lavely_2010]: https://doi.org/10.2514/6.2010-941
[research_conway_lavely_2011]: https://doi.org/10.2514/6.2011-916
[research_cook_1965]: https://doi.org/10.2514/3.43636
[research_coordinated_turning_1995]: https://doi.org/10.2514/5.9781600868535.0363.0376
[research_corcione_bonavolonta_2023]: https://doi.org/10.1016/j.cja.2023.03.035
[research_cord_1989]: https://doi.org/10.2514/6.1989-3357
[research_cordeaux_1991]: https://doi.org/10.21236/ada437706
[research_cordner_1967]: https://doi.org/10.21236/ad0656480
[research_cornellaeronauticallabincbuffalony_1947]: https://doi.org/10.21236/ada800190
[research_corner_1940]: https://doi.org/10.1108/eb030643
[research_cortrightedgarmjr_1951]: https://ntrs.nasa.gov/citations/19930086879
[research_cossar_moffatt_1980]: https://doi.org/10.1115/1.3230338
[research_costakiswg_1974]: https://ntrs.nasa.gov/citations/19740010284
[research_costakiswg_1975]: https://ntrs.nasa.gov/citations/19750005753
[research_cowles_1981]: https://doi.org/10.1108/eb035758
[research_craidoncb_1986]: https://ntrs.nasa.gov/citations/19850000541
[research_craneharoldl_1948]: https://ntrs.nasa.gov/citations/20050028619
[research_craneharoldl_beckhardtarnoldr_1948]: https://ntrs.nasa.gov/citations/20050031072
[research_crea_marty_2025]: https://doi.org/10.3390/ijtpp10020012
[research_crites_rueger_1992]: https://doi.org/10.2514/6.1992-3983
[research_crosthwait_1970]: https://doi.org/10.2514/3.44216
[research_crowe_1936]: https://doi.org/10.1108/eb030014
[research_crowe_1937]: https://doi.org/10.1108/eb030157
[research_crown_1950]: https://doi.org/10.21236/ad0062509
[research_cubbison_1977]: https://ntrs.nasa.gov/citations/19770021130
[research_cui_zhang_2024]: https://doi.org/10.1088/1742-6596/2707/1/012112
[research_cummings_liersch_2018]: https://doi.org/10.2514/1.c033808
[research_cumpsty_greitzer_1982]: https://doi.org/10.1115/1.3227246
[research_cunis_condomines_2020]: https://doi.org/10.2514/1.c035455
[research_da_hanan_2020]: https://doi.org/10.1080/19942060.2020.1792348
[research_dafonsecafilho_gamaribeiro_2019]: https://doi.org/10.1007/s40430-018-1562-1
[research_dahlberg_1963]: https://doi.org/10.21236/ad0412465
[research_dai_boughazi_2023]: https://doi.org/10.59287/ijanser.1160
[research_dai_zhang_2023]: https://doi.org/10.3390/aerospace10060553
[research_dai_zhao_2023]: https://doi.org/10.2514/1.t6675
[research_daliri_farahani_2018]: https://doi.org/10.2514/1.b36760
[research_daniele_teren_1975]: https://doi.org/10.2514/3.59880
[research_danielecj_terenf_1975]: https://ntrs.nasa.gov/citations/19750034195
[research_das_prasad_2023]: https://doi.org/10.61653/joast.v61i2.2009.526
[research_dashora_sasidharan_2024]: https://doi.org/10.2514/6.2024-1385
[research_davidson_1964]: https://doi.org/10.2514/3.43575
[research_davis_1952]: https://doi.org/10.2514/8.2275
[research_davis_1971]: https://doi.org/10.2514/3.6508
[research_davis_1973]: https://doi.org/10.21236/ad0781807
[research_davis_1973_b]: https://doi.org/10.21236/ad0781808
[research_davis_1973_c]: https://doi.org/10.21236/ad0781809
[research_davis_1973_d]: https://doi.org/10.21236/ad0781806
[research_davisdavido_vyasmanana_2012]: https://ntrs.nasa.gov/citations/20120013594
[research_davisra_elrodsd_1972]: https://ntrs.nasa.gov/citations/19740022813
[research_davoudzadeh_liu_1987]: https://doi.org/10.21236/ada193109
[research_day_greitzer_1978]: https://doi.org/10.1115/1.3446318
[research_day_greitzer_1978_b]: https://doi.org/10.1115/1.3446311
[research_dean_young_1977]: https://doi.org/10.1115/1.3448553
[research_debogdance_dicusjh_1975]: https://ntrs.nasa.gov/citations/19750024052
[research_debogdance_mossjejr_1977]: https://ntrs.nasa.gov/citations/19770010127
[research_deese_agarwal_1983]: https://doi.org/10.2514/6.1983-1853
[research_degree_turning]: https://doi.org/10.1088/1748-3190/ae8595/data1
[research_dehner_selamet_2021]: https://doi.org/10.3397/1/376925
[research_dehua_changyou_1993]: https://doi.org/10.21236/ada262374
[research_deitchman_1953]: https://doi.org/10.2514/8.2659
[research_deitchman_1954]: https://doi.org/10.2514/8.2924
[research_demir_gorguluarslan_2023]: https://doi.org/10.1007/s00158-023-03557-1
[research_deng_li_2026]: https://doi.org/10.1016/j.ast.2026.111642
[research_denner_mccallum_1998]: https://doi.org/10.2514/6.1998-3566
[research_departmentofdefensewashingtondc_1997]: https://doi.org/10.21236/ada330041
[research_depaula_porto_2017]: https://doi.org/10.2514/6.2017-1409
[research_desai_viswanathan_1977]: https://doi.org/10.2514/3.44585
[research_design_and_2024]: https://doi.org/10.31534/engmod.2024.2.ri.03v
[research_design_sheets_2003]: https://doi.org/10.1017/cbo9780511809415.026
[research_desyatnik_2015]: https://doi.org/10.1615/tsagiscij.v46.i7.50
[research_development_of_1975]: https://doi.org/10.1108/eb035217
[research_development_testing_1970]: https://doi.org/10.1108/eb034695
[research_deyoungjohn_1950]: https://ntrs.nasa.gov/citations/19930082673
[research_diamantidou_hosain_2022]: https://doi.org/10.3390/su14031731
[research_dias_2023]: https://doi.org/10.2514/1.c037252
[research_dibianchi_orra_2018]: https://doi.org/10.2514/1.c034277
[research_dickeyrobertr_1959]: https://ntrs.nasa.gov/citations/19980231999
[research_dickman_takahashi_2016]: https://doi.org/10.2514/6.2016-0771
[research_dicus_1975]: https://doi.org/10.1016/0010-4485(75)90046-9
[research_dieterreich_josefwimbauer_1975]: https://ntrs.nasa.gov/citations/19750013149
[research_dietz_bailey_1973]: https://doi.org/10.4271/730888
[research_diggins_1951]: https://doi.org/10.21236/ad0895227
[research_dimarco_jacob_2023]: https://doi.org/10.1016/j.ast.2023.108333
[research_ding_2023]: https://doi.org/10.1088/1742-6596/2457/1/012003
[research_ding_chen_2024]: https://doi.org/10.1016/j.ast.2024.109505
[research_ding_shen_2015]: https://doi.org/10.1017/s0001924000010721
[research_ding_wang_2020]: https://doi.org/10.1016/j.applthermaleng.2020.114949
[research_diphda_wiswayana_2026]: https://doi.org/10.51612/teunuleh.v7i1.244
[research_discussion_on_2021]: https://doi.org/10.47939/et.v2i12.419
[research_discussion_on_2021_b]: https://doi.org/10.47939/et.v2i6.50
[research_discussion_on_2021_c]: https://doi.org/10.47939/et.v2i1.52
[research_discussion_on_2021_d]: https://doi.org/10.47939/et.v2i11.437
[research_dislitas_albayrakceper_2021]: https://doi.org/10.31593/ijeat.1029803
[research_dixonsidneyc_griffithgeorgee_1961]: https://ntrs.nasa.gov/citations/19980227795
[research_dobes_dymacek_2019]: https://doi.org/10.1016/j.msea.2019.05.033
[research_dodds_vahdati_2015]: https://doi.org/10.1115/1.4028558
[research_dodds_vahdati_2015_b]: https://doi.org/10.1115/1.4028557
[research_doggettrobertvjr_soistmanndavidl_1989]: https://ntrs.nasa.gov/citations/19890010723
[research_dolling_1982]: https://doi.org/10.2514/6.1982-986
[research_dollyhigh_foss_1985]: https://ntrs.nasa.gov/citations/19860053600
[research_dong_choi_2020]: https://doi.org/10.1007/s00348-020-03023-4
[research_dong_choi_2022]: https://doi.org/10.1017/jfm.2022.451
[research_dong_liu_2025]: https://doi.org/10.1115/1.4069059
[research_dong_sun_2015]: https://doi.org/10.1115/1.4030492
[research_dong_sun_2018]: https://doi.org/10.1115/1.4039707
[research_dong_wang_2026]: https://doi.org/10.2514/1.j066254
[research_donlancj_1976]: https://ntrs.nasa.gov/citations/19770022128
[research_dowell_ventres_1970]: https://doi.org/10.2514/3.5858
[research_drewes_1987]: https://doi.org/10.21236/ada187934
[research_drivercornelius_1958]: https://ntrs.nasa.gov/citations/19980232000
[research_dryer_beke_1952]: https://ntrs.nasa.gov/citations/19930087106
[research_du_2026]: https://doi.org/10.3390/pr14040719
[research_du_liu_2023]: https://doi.org/10.1016/j.cja.2023.02.005
[research_du_zhang_2025]: https://doi.org/10.37965/jdmd.2025.889
[research_duan_wan_2026]: https://doi.org/10.3390/aerospace13010096
[research_duan_zhao_2026]: https://doi.org/10.2514/1.j066092
[research_duddy_landucci_2020]: https://doi.org/10.22594/dau.20-855.27.04
[research_dudley_1986]: https://doi.org/10.2514/6.1986-2729
[research_due_1987]: https://doi.org/10.2514/6.1987-1908
[research_duganjfjr_1972]: https://ntrs.nasa.gov/citations/19720048461
[research_dugas_1968]: https://doi.org/10.21236/ad0675438
[research_duncheva_maximov_2020]: https://doi.org/10.1007/s11223-020-00144-3
[research_dunham_1962]: https://doi.org/10.2514/8.9442
[research_durmus_2021]: https://doi.org/10.1108/aeat-02-2021-0038
[research_durston_stonum_1987]: https://doi.org/10.4271/872311
[research_duvall_arnaiz_1977]: https://doi.org/10.64631/uttn4635
[research_dvirnyk_pavlenko_2019]: https://doi.org/10.3390/aerospace6120132
[research_eberhardt_2005]: https://doi.org/10.2514/6.2005-119
[research_eberle_fowler_1971]: https://doi.org/10.2514/6.1971-8
[research_ebied_hamada_2018]: https://doi.org/10.1016/j.matchar.2018.03.004
[research_edahl_domack_2004]: https://ntrs.nasa.gov/citations/20040047195
[research_edwards_2010]: https://doi.org/10.21236/ada547418
[research_effect_of_2023]: https://doi.org/10.1063/5.0146900
[research_effect_of_2023_b]: https://doi.org/10.47176/jafm.16.03.1449
[research_effect_of_2024]: https://doi.org/10.47176/jafm.17.12.2645
[research_egan_shadowen_1979]: https://doi.org/10.2514/3.58573
[research_egorov_neiland_2011]: https://doi.org/10.2514/6.2011-730
[research_ellis_brownstein_1974]: https://doi.org/10.2514/3.60331
[research_elsayed_2026]: https://doi.org/10.1201/9781003561538-5
[research_emmons_pearson_1955]: https://doi.org/10.1115/1.4014389
[research_emmons_pearson_1955_b]: https://doi.org/10.1115/1.4014393
[research_englertgeraldw_oberyleonardj_1952]: https://ntrs.nasa.gov/citations/19930090601
[research_enzinger_1988]: https://doi.org/10.2514/6.1988-2120
[research_epstein_1954]: https://doi.org/10.21236/ad0037709
[research_erich_1980]: https://doi.org/10.21236/ada090597
[research_erickson_campbell_1977]: https://ntrs.nasa.gov/citations/19770009040
[research_erickson_campbell_1977_b]: https://ntrs.nasa.gov/citations/19780007054
[research_esau_2024]: https://doi.org/10.51644/ldvj3253
[research_esenweinfredt_schuellercarlf_1952]: https://ntrs.nasa.gov/citations/19930087893
[research_esser_ruffstahl_2021]: https://doi.org/10.7771/2159-6670.1218
[research_eulrich_mesiah_1974]: https://doi.org/10.21236/ada021994
[research_evaluation_of_2024]: https://doi.org/10.47176/jafm.17.3.2150
[research_evans_chamblee_1966]: https://doi.org/10.21236/ad0628775
[research_evansdg_debogdance_1974]: https://ntrs.nasa.gov/citations/19740020647
[research_evvardjohnc_1947]: https://ntrs.nasa.gov/citations/19930082018
[research_experimental_study_2020]: https://doi.org/10.20431/2454-8693.0601001
[research_experimental_study_2022]: https://doi.org/10.47176/jafm.15.02.33220
[research_ezrokhi_khoreva_2018]: https://doi.org/10.24108/0118.0001360
[research_f_104_resource_1992]: https://ntrs.nasa.gov/citations/19950004329
[research_falk_jumper_1998]: https://doi.org/10.2514/6.1998-3294
[research_falk_jumper_2001]: https://doi.org/10.2514/2.5772
[research_faltin_beneda_2023]: https://doi.org/10.32560/rk.2023.3.7
[research_fan_du_2025]: https://doi.org/10.1115/1.4068876
[research_fan_li_2026]: https://doi.org/10.1115/1.4072311
[research_fan_liu_2024]: https://doi.org/10.1063/5.0235393
[research_fan_xu_2026]: https://doi.org/10.1007/s11630-026-2309-4
[research_fan_xu_2026_b]: https://doi.org/10.1115/1.4070987
[research_fang_sun_2023]: https://doi.org/10.3390/aerospace10020141
[research_fang_sun_2023_b]: https://doi.org/10.2514/1.j062482
[research_fang_wang_2023]: https://doi.org/10.1016/j.ast.2023.108612
[research_fang_zhang_2022]: https://doi.org/10.4028/www.scientific.net/kem.905.14
[research_farahani_daliri_2019]: https://doi.org/10.1016/j.ast.2019.02.002
[research_farahani_mahdavi_2019]: https://doi.org/10.1016/j.ast.2019.05.014
[research_farhat_harris_2000]: https://doi.org/10.2514/6.2000-1702
[research_farr_1976]: https://doi.org/10.2514/3.58627
[research_felix_perron_2026]: https://doi.org/10.2514/1.c038369
[research_fellers_patierno_1970]: https://doi.org/10.2514/6.1970-516
[research_feng_chen_2025]: https://doi.org/10.1016/j.intermet.2025.108708
[research_feng_tao_2020]: https://doi.org/10.1016/j.ijthermalsci.2020.106357
[research_feng_tianyu_2022]: https://doi.org/10.1007/s13369-022-06827-0
[research_ferrar_schneck_2016]: https://doi.org/10.1115/gt2016-57703
[research_ferrari_1958]: https://doi.org/10.1007/978-3-642-45885-9_21
[research_ferrero_2020]: https://doi.org/10.3390/aerospace7030032
[research_ferriantonio_nuccilouism_1946]: https://ntrs.nasa.gov/citations/19930093800
[research_ferriantonio_nuccilouism_1951]: https://ntrs.nasa.gov/citations/19930083137
[research_fett_1971]: https://doi.org/10.2514/3.44306
[research_figge_1973]: https://doi.org/10.21236/ad0781810
[research_fighter_and_2008]: https://doi.org/10.5040/9798400685590.ch-003
[research_fine_1959]: https://doi.org/10.1080/14786435908233372
[research_fine_weertman_1983]: https://doi.org/10.21236/ada135956
[research_fink_anderson_1983]: https://doi.org/10.2514/3.25604
[research_fischer_norris_1949]: https://doi.org/10.1115/1.4017110
[research_fisherlewisr_williamsjamesl_1958]: https://ntrs.nasa.gov/citations/19980232008
[research_flanaganmichaelj_1992]: https://ntrs.nasa.gov/citations/19930004476
[research_fleeter_mcclure_1974]: https://doi.org/10.1121/1.1919886
[research_flow_field_2020]: https://doi.org/10.47176/jafm.13.06.31428
[research_flow_structure_2023]: https://doi.org/10.1063/5.0151556
[research_forsythe_hoffmann_1998]: https://doi.org/10.2514/6.1998-2648
[research_foss_1981]: https://ntrs.nasa.gov/citations/19810011498
[research_foss_1984]: https://ntrs.nasa.gov/citations/19830000631
[research_fostergeraldv_fitzpatrickjamese_1948]: https://ntrs.nasa.gov/citations/19930085540
[research_fradenburgh_wyatt_1953]: https://ntrs.nasa.gov/citations/19930083660
[research_fraiser_1960]: https://doi.org/10.2514/8.8575
[research_franciscusleoc_1987]: https://ntrs.nasa.gov/citations/19870014193
[research_franck_lewis_2012]: https://doi.org/10.21236/ada584635
[research_francois_probst_2021]: https://doi.org/10.2514/1.c036273
[research_frey_2014]: https://doi.org/10.21236/ada622072
[research_friend_sefic_1972]: https://ntrs.nasa.gov/citations/19720022354
[research_friendel_sakamotogm_1978]: https://ntrs.nasa.gov/citations/19790004885
[research_frohnapfel_mack_2018]: https://doi.org/10.1115/gt2018-76616
[research_frohnapfel_obrien_2017]: https://doi.org/10.2514/6.2017-1623
[research_frohnapfel_tlowe_2021]: https://doi.org/10.1115/1.0002892v
[research_frohnapfel_toddlowe_2018]: https://doi.org/10.1115/1.4039425
[research_fu_fu_2021]: https://doi.org/10.1080/00051144.2021.1990629
[research_fu_fu_2021_b]: https://doi.org/10.1080/21642583.2021.1888818
[research_fujii_fujimori_2021]: https://doi.org/10.1299/jsmefed.2021.os11-01
[research_fujimoto_niwa_1993]: https://doi.org/10.2514/6.1993-289
[research_fullerde_1967]: https://ntrs.nasa.gov/citations/19670024546
[research_fundamentals_of_2001]: https://doi.org/10.1108/aeat.2001.12773aae.001
[research_fuqun_wenlan_1985]: https://doi.org/10.1115/85-igt-12
[research_furukawa_yamada_2015]: https://doi.org/10.1299/jsmemecj.2015._j0520305-
[research_gabrieldavids_krebsrichardp_1953]: https://ntrs.nasa.gov/citations/19930087143
[research_gadeev_demakov_2017]: https://doi.org/10.4028/www.scientific.net/ssp.265.575
[research_gaglio_visone_2023]: https://doi.org/10.2514/1.a35532
[research_gahlot_singh_2019]: https://doi.org/10.1088/1742-6596/1240/1/012008
[research_galindo_climent_2022]: https://doi.org/10.3390/app12031751
[research_galkin_sergeev_1976]: https://doi.org/10.1007/bf01529858
[research_ganilova_cartmell_2021]: https://doi.org/10.1016/j.compstruct.2020.113159
[research_ganilova_cartmell_2022]: https://doi.org/10.1016/j.compstruct.2022.115423
[research_gao_li_2015]: https://doi.org/10.1115/1.4029101
[research_gao_liu_2017]: https://doi.org/10.3397/1/3773
[research_gartling_1970]: https://doi.org/10.21236/ad0734154
[research_gas_turbine]: https://doi.org/10.4271/arp1420
[research_gates_1940]: https://doi.org/10.1108/eb030684
[research_ge_shang_2021]: https://doi.org/10.1088/1742-6596/1985/1/012037
[research_gedeon_takahashi_2014]: https://doi.org/10.2514/6.2014-3156
[research_gehring_engle_1963]: https://doi.org/10.21236/ad0409967
[research_gelderthomasf_1957]: https://ntrs.nasa.gov/citations/19930093764
[research_gellatly_bijlaard_1965]: https://doi.org/10.2514/3.43617
[research_gellatly_gallagher_1964]: https://doi.org/10.21236/ad0431959
[research_geng_yang_2025]: https://doi.org/10.1016/j.ast.2024.109778
[research_ghaffarifarhad_2005]: https://ntrs.nasa.gov/citations/20050198856
[research_ghee_gonzalez_1999]: https://doi.org/10.21236/ada368657
[research_gilbert_nguyen_1976]: https://ntrs.nasa.gov/citations/19760017178
[research_gilinskymikhail_morganmorrish_2000]: https://ntrs.nasa.gov/citations/20010012156
[research_gill_sain_1981]: https://doi.org/10.2514/6.1981-2353
[research_gillen_loth_2011]: https://doi.org/10.2514/6.2011-5567
[research_gillen_loth_2015]: https://doi.org/10.2514/1.b35610
[research_gillespiewarrenjr_1960]: https://ntrs.nasa.gov/citations/20040046997
[research_gilman_burdges_1967]: https://doi.org/10.2514/3.43894
[research_gilruthrr_whitemd_1941]: https://ntrs.nasa.gov/citations/19930091789
[research_giuliano_2016]: https://doi.org/10.1016/j.mfglet.2016.08.003
[research_gleason_martone_1980]: https://doi.org/10.1115/80-gt-70
[research_glenn_koch_1973]: https://doi.org/10.2514/6.1973-806
[research_gliszczynski_czechowski_2021]: https://doi.org/10.3390/ma14112928
[research_glorioso_1960]: https://doi.org/10.21236/ad0281801
[research_glossbb_1974]: https://ntrs.nasa.gov/citations/19740020361
[research_go_wilshire_1992]: https://doi.org/10.1016/0956-716x(92)90625-o
[research_goldberg_boxer_1959]: https://ntrs.nasa.gov/citations/19980230685
[research_golombek_bustamante_2026]: https://doi.org/10.1007/s13272-026-00996-6
[research_golovin_1982]: https://doi.org/10.1007/bf00776064
[research_golubkin_1980]: https://doi.org/10.1007/bf01089616
[research_golubkin_1980_b]: https://doi.org/10.1007/bf01089658
[research_goodman_1949]: https://doi.org/10.2514/8.11808
[research_goonko_mazhul_2011]: https://doi.org/10.1134/s0869864311010100
[research_goransonrfabian_1942]: https://ntrs.nasa.gov/citations/19930092510
[research_gorbovskoi_kazhan_2019]: https://doi.org/10.34759/vst-2019-4-7-16
[research_gortongeraldc_1953]: https://ntrs.nasa.gov/citations/19930087622
[research_gortongeraldc_1954]: https://ntrs.nasa.gov/citations/19930089376
[research_goto_nakayama_2021]: https://doi.org/10.1299/jsmehs.2021.58.g011
[research_gotten_havermann_2021]: https://doi.org/10.2514/1.c036032
[research_goud_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1057
[research_goulos_otter_2021]: https://doi.org/10.1016/j.ast.2021.106533
[research_gounko_mazhul_2012]: https://doi.org/10.1134/s086986431203002x
[research_gozukara_ceylan_2024]: https://doi.org/10.3390/computation12080162
[research_graham_lagerstrom_1954]: https://doi.org/10.21236/ad0063453
[research_gray_1969]: https://doi.org/10.1243/pime_conf_1969_184_182_02
[research_gray_mader_2020]: https://doi.org/10.2514/1.c035845
[research_gray_martins_2018]: https://doi.org/10.1017/aer.2018.120
[research_grayjustins_madercharlesa_2017]: https://ntrs.nasa.gov/citations/20170001424
[research_gregorysjones_williammilholen_2020]: https://ntrs.nasa.gov/citations/20200003091
[research_gregorytj_wilcoxde_1970]: https://ntrs.nasa.gov/citations/19700064255
[research_greitzer_1972]: https://doi.org/10.2514/3.59027
[research_greitzer_1976]: https://doi.org/10.1115/1.3446138
[research_greitzer_1976_b]: https://doi.org/10.1115/1.3446139
[research_greitzer_1976_c]: https://doi.org/10.1115/1.3446143
[research_greitzer_1980]: https://doi.org/10.1115/1.3240634
[research_grenson_beneddine_2018]: https://doi.org/10.2514/6.2018-3011
[research_gridnev_1991]: https://doi.org/10.1007/bf01050988
[research_griffin_2012]: https://doi.org/10.21236/ada561607
[research_griffinroynjr_holzhausercurta_1958]: https://ntrs.nasa.gov/citations/19980228056
[research_grimshaw_pullan_2025]: https://doi.org/10.1115/1.4070355
[research_gringorten_tattelman_1970]: https://doi.org/10.21236/ad0712017
[research_groth_1961]: https://doi.org/10.1016/b978-1-4832-1323-1.50018-x
[research_grytsyshen_abramova_2025]: https://doi.org/10.26642/ppa-2025-1(11)-44-49
[research_gu_xu_2023]: https://doi.org/10.1016/j.ast.2022.108079
[research_guan_yarng_1984]: https://doi.org/10.2514/6.1984-1496
[research_guan_yarng_1987]: https://doi.org/10.2514/6.1987-2053
[research_guan_zhou_2019]: https://doi.org/10.1080/19942060.2019.1639216
[research_guang_deming_2015]: https://doi.org/10.1109/chicc.2015.7261035
[research_guang_ping_2014]: https://doi.org/10.1109/cgncc.2014.7007411
[research_guderley_1987]: https://doi.org/10.21236/ada193773
[research_guderley_1988]: https://doi.org/10.21236/ada191408
[research_gudmundsson_2014]: https://doi.org/10.1016/b978-0-12-397308-5.00015-5
[research_guidelines_for]: https://doi.org/10.4271/arp6420
[research_guimaraes_lowe_2015]: https://doi.org/10.2514/6.2015-2866
[research_guimaraes_lowe_2018]: https://doi.org/10.2514/1.b36422
[research_guimaraes_toddlowe_2018]: https://doi.org/10.1115/1.4039179
[research_gullu_aran_2023]: https://doi.org/10.1115/gt2023-100874
[research_gunaydin_dogu_2025]: https://doi.org/10.29137/ijerad.1602783
[research_guo_2023]: https://doi.org/10.15632/jtam-pl/174960
[research_guo_gao_2022]: https://doi.org/10.1515/tjj-2022-0016
[research_guo_hu_2021]: https://doi.org/10.1007/s11630-021-1483-7
[research_guo_liu_2025]: https://doi.org/10.1016/j.ast.2025.110290
[research_guo_mao_2022]: https://doi.org/10.1080/19942060.2022.2072955
[research_guo_tian_2021]: https://doi.org/10.1016/j.jallcom.2021.159497
[research_guo_zhang_2024]: https://doi.org/10.3390/aerospace12010010
[research_gupta_ramkumar_2015]: https://doi.org/10.12783/fae.2015.0401.02
[research_gur_mason_2010]: https://doi.org/10.2514/1.47557
[research_gurbuz_acarer_2022]: https://doi.org/10.21205/deufmd.2022247222
[research_gutierrezalvarez_bisagni_2021]: https://doi.org/10.3390/aerospace8020056
[research_haas_karanian_1981]: https://doi.org/10.2514/3.57819
[research_hackman_richardson_1964]: https://doi.org/10.2514/3.43555
[research_haering_burcham_1984]: https://ntrs.nasa.gov/citations/19860014116
[research_hah_2018]: https://doi.org/10.1115/1.4041133
[research_hah_2022]: https://doi.org/10.1115/1.4055678
[research_hall_greitzer_2017]: https://doi.org/10.1115/1.4035631
[research_hall_greitzer_2022]: https://doi.org/10.1115/1.4055645
[research_hall_greitzer_2022_b]: https://doi.org/10.1115/1.4054035
[research_hall_hamilton_1997]: https://doi.org/10.1520/stp16315s
[research_hallcharlesf_heitmeyerjohnc_1951]: https://ntrs.nasa.gov/citations/19930086624
[research_halwas_aggarwal_2019]: https://doi.org/10.2514/1.c035093
[research_halwas_aggarwal_2019_b]: https://doi.org/10.2514/1.c035481
[research_hamaguchi_sakata_2020]: https://doi.org/10.38036/jgpp.11.4_13
[research_hamed_1993]: https://doi.org/10.21236/ada268106
[research_hamed_1995]: https://ntrs.nasa.gov/citations/19960000871
[research_hamilton_hall_1997]: https://doi.org/10.1520/stp16314s
[research_han_seo_2016]: https://doi.org/10.3740/mrsk.2016.26.7.370
[research_hanazaki_yamazaki_2024]: https://doi.org/10.3390/aerospace11010064
[research_hancock_1959]: https://doi.org/10.2514/8.8168
[research_hancock_1959_b]: https://doi.org/10.1017/s0001925900001487
[research_hancock_1960]: https://doi.org/10.2514/8.8377
[research_hancockjp_1985]: https://ntrs.nasa.gov/citations/19870001433
[research_hansen_1972]: https://doi.org/10.1016/0022-3115(72)90066-9
[research_hansen_jorgensen_1981]: https://doi.org/10.1115/1.3240796
[research_hantraisgervois_destarac_2015]: https://doi.org/10.2514/1.c033193
[research_hao_liu_2024]: https://doi.org/10.1016/j.tsep.2024.102516
[research_harle_1979]: https://doi.org/10.1177/001083677901400103
[research_harloff_smith_1995]: https://doi.org/10.2514/6.1995-38
[research_harman_1978]: https://doi.org/10.1115/1.3446305
[research_harold_haefeli_1950]: https://doi.org/10.2514/8.1512
[research_harper_robertp_1955]: https://doi.org/10.21236/ad0092496
[research_hartley_furey_1965]: https://doi.org/10.21236/ad0626655
[research_hartmann_1968]: https://doi.org/10.2514/3.43978
[research_hartsell_1960]: https://doi.org/10.2514/8.8748
[research_hasellowelle_lankfordjohnl_1953]: https://ntrs.nasa.gov/citations/20050019413
[research_hashin_humphreys_1980]: https://doi.org/10.21236/ada089414
[research_hawk_wilsdorf_1988]: https://doi.org/10.1016/0036-9748(88)90025-7
[research_hawkinsje_kirklandfp_1976]: https://ntrs.nasa.gov/citations/19760017152
[research_hawkinsrichard_penlandjima_1997]: https://ntrs.nasa.gov/citations/19980008542
[research_hawks_1982]: https://doi.org/10.2514/3.44751
[research_hawthorne_mitchell_1978]: https://doi.org/10.1115/1.3446409
[research_hawthorne_wood_1955]: https://doi.org/10.1115/1.4014390
[research_hayden_gillespie_2023]: https://doi.org/10.1115/1.4063709
[research_hayden_untaroiu_2021]: https://doi.org/10.1115/1.4052139
[research_hayeswcjr_sleemanwcjr_1959]: https://ntrs.nasa.gov/citations/19630010604
[research_he_shi_2025]: https://doi.org/10.2514/1.c037918
[research_he_xie_2026]: https://doi.org/10.1016/j.ast.2025.110859
[research_he_zhang_2025]: https://doi.org/10.1063/5.0276968
[research_heath_slater_2016]: https://ntrs.nasa.gov/citations/20170002621
[research_heathsmith_1965]: https://doi.org/10.1016/b978-1-4831-9818-7.50009-0
[research_hebbar_platzer_1991]: https://doi.org/10.2514/6.1991-280
[research_heimerlgeorgej_hardrathherbertf_1965]: https://ntrs.nasa.gov/citations/20000011991
[research_heiss_eberle_1992]: https://doi.org/10.2514/6.1992-2620
[research_hellemeier_2019]: https://doi.org/10.1515/peps-2019-0030
[research_helmbold_1958]: https://doi.org/10.21236/ad0209045
[research_heltsley_crosswy_1983]: https://doi.org/10.21236/ada129606
[research_henderson_1965]: https://doi.org/10.1017/s0001925900003358
[research_herbst_1980]: https://doi.org/10.2514/3.44674
[research_herbst_krogull_1973]: https://doi.org/10.2514/3.60220
[research_hernandezgloria_woodrichardm_1994]: https://ntrs.nasa.gov/citations/19950003616
[research_herrick_1986]: https://doi.org/10.2514/6.1986-2658
[research_herwig_2000]: https://doi.org/10.1007/978-3-642-56940-1_1
[research_hess_1986]: https://doi.org/10.2514/6.1986-2681
[research_hewesdonalde_1950]: https://ntrs.nasa.gov/citations/20050028478
[research_hickman_morris_2017]: https://doi.org/10.1155/2017/6329382
[research_hicks_huckabine_1989]: https://ntrs.nasa.gov/citations/19910019863
[research_higham_holley_1966]: https://doi.org/10.2307/3101879
[research_hild_crocker_2006]: https://doi.org/10.2139/ssrn.912049
[research_hild_crocker_2006_b]: https://doi.org/10.2139/ssrn.912050
[research_hild_crocker_2008]: https://doi.org/10.2139/ssrn.1284231
[research_hill_defoe_2020]: https://doi.org/10.1115/1.4045464
[research_hillgc_bowlesjv_1976]: https://ntrs.nasa.gov/citations/19760026102
[research_hillier_1970]: https://doi.org/10.1017/s0001925900005394
[research_hitzel_osterhuber_2018]: https://doi.org/10.2514/1.c034473
[research_hobbs_spaid_1996]: https://doi.org/10.2514/6.1996-410
[research_hodderbk_1981]: https://ntrs.nasa.gov/citations/19810021546
[research_hodderbk_farquharbw_1981]: https://ntrs.nasa.gov/citations/19820030404
[research_hodge_taylor_1985]: https://doi.org/10.2514/6.1985-1657
[research_hodge_taylor_1986]: https://doi.org/10.2514/3.9482
[research_hoerner_1936]: https://doi.org/10.1108/eb030033
[research_hoerter_powers_1991]: https://doi.org/10.4271/911171
[research_hofflerkd_raodm_1986]: https://ntrs.nasa.gov/citations/19860017727
[research_hoffman_stalford_1991]: https://doi.org/10.2514/6.1991-2667
[research_hoffmantr_2000]: https://ntrs.nasa.gov/citations/20050194574
[research_holdawaygeorgeh_lazzeronifranka_1959]: https://ntrs.nasa.gov/citations/19980223578
[research_holl_1975]: https://doi.org/10.1108/eb035216
[research_hom_morris_1983]: https://doi.org/10.2514/6.1983-426
[research_hon_karpuk_2022]: https://doi.org/10.2478/tar-2022-0009
[research_honeycutt_1970]: https://doi.org/10.21236/ad0875636
[research_hongpeng_weiqiang_2016]: https://doi.org/10.1016/j.actaastro.2016.05.014
[research_hopkinsej_1975]: https://ntrs.nasa.gov/citations/19750055435
[research_horton_1954]: https://doi.org/10.1108/eb032421
[research_hortonelmera_loftinlaurencek_1951]: https://ntrs.nasa.gov/citations/19930092102
[research_hosseindokht_matas_2026]: https://doi.org/10.3390/app16104616
[research_hosseini_vaziryzanjany_2024]: https://doi.org/10.3390/aerospace11040273
[research_hou_wang_2017]: https://doi.org/10.1007/s11630-017-0916-9
[research_hovelmann_breitsamter_2015]: https://doi.org/10.2514/1.c033014
[research_hovelmann_grawunder_2016]: https://doi.org/10.1016/j.ast.2015.12.023
[research_howard_luidens_1951]: https://ntrs.nasa.gov/citations/19930086661
[research_howerton_slater]: https://ntrs.nasa.gov/citations/20210018078
[research_howlett_hunter_1986]: https://doi.org/10.2514/6.1986-308
[research_hrubecky_1963]: https://doi.org/10.1007/bf03184628
[research_hsu_anderson_1961]: https://doi.org/10.2514/8.8910
[research_hu_2024]: https://doi.org/10.1088/1742-6596/2731/1/012048
[research_hu_li_2024]: https://doi.org/10.1016/j.ast.2024.109309
[research_hu_qu_2023]: https://doi.org/10.1088/1742-6596/2478/8/082009
[research_huang_tan_2016]: https://doi.org/10.1063/1.4971448
[research_huang_wang_2026]: https://doi.org/10.1016/j.ast.2026.112309
[research_huang_zhang_2019]: https://doi.org/10.1016/j.ast.2019.04.042
[research_hubble_smith_1979]: https://doi.org/10.21236/ada072743
[research_hube_1968]: https://doi.org/10.21236/ad0388036
[research_hughes_johnson_1972]: https://ntrs.nasa.gov/citations/19720011346
[research_hughesdl_mackallkg_1984]: https://ntrs.nasa.gov/citations/19860015876
[research_hui_1975]: https://doi.org/10.1017/s0001925900007150
[research_hunn_1954]: https://doi.org/10.1017/s0001925900001128
[research_hunt_gowadia_1981]: https://doi.org/10.2514/6.1981-1692
[research_hunt_hunt_2021]: https://doi.org/10.2514/1.b38334
[research_hunziker_1960]: https://doi.org/10.1007/bf01595402
[research_huppert_1955]: https://doi.org/10.1115/1.4014391
[research_huppert_benser_1953]: https://doi.org/10.2514/8.2871
[research_hurley_1951]: https://doi.org/10.1115/1.4016500
[research_hutchinson_lawrence_2021]: https://doi.org/10.1177/09544100211016952
[research_hwang_johnson_1980]: https://ntrs.nasa.gov/citations/19810003606
[research_hwang_pi_1979]: https://doi.org/10.2514/3.58518
[research_ichikawa_koike_2021]: https://doi.org/10.1007/s00348-021-03198-4
[research_iekchanthy_burleyrichardr_1993]: https://ntrs.nasa.gov/citations/19930014929
[research_iliff_1977]: https://doi.org/10.2514/3.58911
[research_iliff_smith_1970]: https://ntrs.nasa.gov/citations/19710048134
[research_imani_jahedmotlagh_2017]: https://doi.org/10.1080/21642583.2017.1367732
[research_imani_malekizade_2018]: https://doi.org/10.1080/00051144.2018.1498204
[research_imig_1973]: https://doi.org/10.1520/stp38845s
[research_influence_of_2017]: https://doi.org/10.15593/2224-9982/2017.49.02
[research_inger_1986]: https://doi.org/10.1007/978-3-642-82770-9_24
[research_inger_zee_1978]: https://doi.org/10.2514/3.58442
[research_inglis_larke_1958]: https://doi.org/10.1243/pime_proc_1958_172_076_02
[research_initial_damage_2019]: https://doi.org/10.1299/jsmemecj.2019.j02334
[research_inlet_total_pressure_distortion]: https://doi.org/10.4271/air1419
[research_irsyadlukman_agoesmoelyadi_2018]: https://doi.org/10.1088/1742-6596/1005/1/012050
[research_irwanto_2017]: https://doi.org/10.1109/issimm.2017.8124253
[research_iseki_nicholas_1979]: https://doi.org/10.1007/bf00772731
[research_islam_fermin_2015]: https://doi.org/10.1017/s1431927615002238
[research_isugiyama_1976]: https://doi.org/10.1299/kikai1938.42.3186
[research_ivanov_2022]: https://doi.org/10.54708/19926502_2022_2619559
[research_jackjohnr_1951]: https://ntrs.nasa.gov/citations/19930086899
[research_jackson_1980]: https://ntrs.nasa.gov/citations/19800020811
[research_jacocks_kneile_1975]: https://doi.org/10.21236/ada004104
[research_jain_liang_2020]: https://doi.org/10.1016/j.matpr.2019.12.332
[research_jakubowski_2019]: https://doi.org/10.2478/kones-2019-0033
[research_jamesfconnors_georgeawise_1957]: https://ntrs.nasa.gov/citations/19930089639
[research_jaquetbyronm_1951]: https://ntrs.nasa.gov/citations/19930086998
[research_jayakrishnan_pant_2005]: https://doi.org/10.2514/6.2005-7372
[research_jeans_grimes_1983]: https://doi.org/10.2514/3.44838
[research_jeans_tribble_1979]: https://doi.org/10.1520/stp35876s
[research_jeffs_lancaster_2015]: https://doi.org/10.1016/j.msea.2014.12.085
[research_jelev_keane_2019]: https://doi.org/10.2514/1.c034897
[research_jenista_bodden_1989]: https://doi.org/10.1115/89-gt-308
[research_jenkinsjeraldm_kuhlalberte_1977]: https://ntrs.nasa.gov/citations/20020086520
[research_jenkinsjm_1979]: https://ntrs.nasa.gov/citations/19790012818
[research_jenney_1935]: https://doi.org/10.2514/8.126
[research_ji_hu_2022]: https://doi.org/10.3390/en15145246
[research_ji_huang_2024]: https://doi.org/10.1016/j.ast.2024.109416
[research_ji_yuan_2021]: https://doi.org/10.3390/ma14051217
[research_jia_chen_2024]: https://doi.org/10.1049/icp.2024.3929
[research_jiali_jihong_2015]: https://doi.org/10.1109/ecc.2015.7330954
[research_jiao_chang_2017]: https://doi.org/10.1016/j.actaastro.2016.10.027
[research_jin_sun_2022]: https://doi.org/10.1016/j.cja.2021.06.013
[research_jin_tan_2023]: https://doi.org/10.1016/j.cja.2023.08.004
[research_jin_zhang_2023]: https://doi.org/10.1016/j.actaastro.2022.09.052
[research_johns_1998]: https://ntrs.nasa.gov/citations/20050177879
[research_johnson_1972]: https://doi.org/10.21236/ad0754909
[research_johnson_adcock_1981]: https://ntrs.nasa.gov/citations/19810054670
[research_johnson_henderson_1959]: https://doi.org/10.1108/eb033103
[research_johnson_henderson_1960]: https://doi.org/10.1108/eb033263
[research_johnson_lawing_1977]: https://doi.org/10.2514/3.44604
[research_johnson_wu_1975]: https://doi.org/10.1115/1.3447318
[research_johnsonhj_montoyaej_1973]: https://ntrs.nasa.gov/citations/19730015310
[research_johnsoniii_wu_1974]: https://doi.org/10.21236/ada017631
[research_jonathanalee_poshouchen_2005]: https://ntrs.nasa.gov/citations/20050237966
[research_jones_1972]: https://doi.org/10.2514/3.6568
[research_jones_1973]: https://doi.org/10.21236/ad0773559
[research_jonesarthurl_flanaganmildredg_1947]: https://ntrs.nasa.gov/citations/19930082115
[research_jonesgwjr_unangstjr_1963]: https://ntrs.nasa.gov/citations/19630002604
[research_jonesrobertt_1953]: https://ntrs.nasa.gov/citations/20050081861
[research_jonesrobertt_1956]: https://ntrs.nasa.gov/citations/19930092281
[research_jonesrt_1976]: https://ntrs.nasa.gov/citations/19760012011
[research_jules_barnhart_1998]: https://ntrs.nasa.gov/citations/20050177169
[research_jung_lee_2015]: https://doi.org/10.5139/jksas.2015.43.5.387
[research_ka_2018]: https://doi.org/10.4172/2332-0796.1000267
[research_kaczorowski_skoczylas_2015]: https://doi.org/10.1515/afe-2015-0077
[research_kalkan_2024]: https://doi.org/10.36306/konjes.1332160
[research_kamman_hall_1975]: https://ntrs.nasa.gov/citations/19750006694
[research_kang_kang_2024]: https://doi.org/10.6108/kspe.2024.28.6.001
[research_kang_li_2024]: https://doi.org/10.1080/17452759.2024.2382166
[research_kang_liang_2024]: https://doi.org/10.3390/aerospace11120992
[research_kaplan_1980]: https://doi.org/10.21236/ada089051
[research_kapoor_pai_1992]: https://doi.org/10.2514/3.23559
[research_kapoorkamlesh_andersonbernhardh_1994]: https://ntrs.nasa.gov/citations/19950004408
[research_karabacak_turan_2020]: https://doi.org/10.1504/ijsa.2020.112087
[research_karimi_oboodi_2018]: https://doi.org/10.1007/s00231-018-2416-1
[research_karl_werner_2025]: https://doi.org/10.33737/jgpps/213325
[research_karniadakis_2004]: https://doi.org/10.21236/ada420891
[research_karol_hatch_1969]: https://doi.org/10.21236/ad0862599
[research_kast_1980]: https://doi.org/10.21236/ada094730
[research_katz_1971]: https://doi.org/10.2514/3.44296
[research_kawamura_karashima_1957]: https://doi.org/10.2322/jjsass1953.5.93
[research_kawamurat_chyuwj_1987]: https://ntrs.nasa.gov/citations/19870037658
[research_kawase_rona_2019]: https://doi.org/10.3390/fluids4020088
[research_kawase_rona_2019_b]: https://doi.org/10.3390/ijtpp4010005
[research_kaye_yeh_1955]: https://doi.org/10.2514/8.3454
[research_kayser_danberg_1974]: https://doi.org/10.2514/3.49559
[research_kazula_hoschler_2020]: https://doi.org/10.1108/aeat-11-2019-0225
[research_kazula_hoschler_2021]: https://doi.org/10.1007/s13272-021-00520-y
[research_kazula_mischke_2019]: https://doi.org/10.1051/matecconf/201930402016
[research_kbab_haif_2023]: https://doi.org/10.59287/icpis.851
[research_kelley_1975]: https://doi.org/10.2514/3.59799
[research_kelley_1975_b]: https://doi.org/10.2514/3.59895
[research_kelleymarkw_tolhurstwilliamhjr_1955]: https://ntrs.nasa.gov/citations/19930093777
[research_kellymarkw_andersonsethb_1958]: https://ntrs.nasa.gov/citations/19930092354
[research_kennon_1989]: https://doi.org/10.2514/6.1989-113
[research_keppler_1966]: https://ntrs.nasa.gov/citations/19660000528
[research_khademi_ikeda_2019]: https://doi.org/10.1007/s11837-019-03598-2
[research_khaleghi_2015]: https://doi.org/10.1016/j.ast.2014.12.004
[research_khalid_2025]: https://doi.org/10.20944/preprints202503.0126.v1
[research_khan_hasan_2021]: https://doi.org/10.1115/1.4049677
[research_khatri_sinha_2023]: https://doi.org/10.61653/joast.v68i4.2016.367
[research_khobragade_gustavsson_2024]: https://doi.org/10.1007/s00193-024-01192-3
[research_khobragade_kumar_2022]: https://doi.org/10.1007/s00193-022-01091-5
[research_khobragade_unnikrishnan_2021]: https://doi.org/10.2514/1.j060591
[research_kholyavko_1971]: https://doi.org/10.1007/bf01019800
[research_kida_miyai_1978]: https://doi.org/10.1017/s0001925900008477
[research_kigotho_bodylski_2022]: https://doi.org/10.2514/1.c036582
[research_kim_2024]: https://doi.org/10.18703/silj.2024.12.31.2.151
[research_kim_choi_2022]: https://doi.org/10.2514/1.b38484
[research_kim_kim_2015_b]: https://doi.org/10.1016/j.ast.2015.09.007
[research_kim_kim_2026]: https://doi.org/10.1016/j.measurement.2025.119228
[research_kim_kwon_2015]: https://doi.org/10.2514/1.b35742
[research_kim_lee_2022]: https://doi.org/10.5139/jksas.2022.50.5.297
[research_kim_park_2026]: https://doi.org/10.6112/kscfe.2026.31.2.084
[research_kimhyoungjin_kumanotakayasu_2011]: https://ntrs.nasa.gov/citations/20110011992
[research_kinardtima_harrisbrendaw_1995]: https://ntrs.nasa.gov/citations/19950016768
[research_kingrw_schuermanja_1976]: https://ntrs.nasa.gov/citations/19760019074
[research_kinslermartinr_1958]: https://ntrs.nasa.gov/citations/19930092395
[research_kish_wilde_2019]: https://doi.org/10.1109/aero.2019.8741812
[research_kishi_kanazaki_2022]: https://doi.org/10.2514/1.c036422
[research_kiss_spakovszky_2018]: https://doi.org/10.1115/1.4041290
[research_kitowski_1986]: https://doi.org/10.2514/6.1986-2688
[research_kjames_kim_2022]: https://doi.org/10.1016/j.ast.2022.107982
[research_kjames_suryan_2021]: https://doi.org/10.1016/j.ast.2021.106795
[research_klannga_barthrl_1984]: https://ntrs.nasa.gov/citations/19850056914
[research_klecknerharoldf_1945]: https://ntrs.nasa.gov/citations/19930092870
[research_klecknerharoldf_1946]: https://ntrs.nasa.gov/citations/19930081790
[research_klein_abeykoon_2015]: https://doi.org/10.1109/itecha.2015.7317395
[research_kleinvladislav_1999]: https://ntrs.nasa.gov/citations/19990100653
[research_kohn_1964]: https://ntrs.nasa.gov/citations/19680070665
[research_kohn_1979]: https://doi.org/10.2514/6.1979-1833
[research_kolnsberg_1979]: https://doi.org/10.1115/1.3446465
[research_kolom_1969]: https://doi.org/10.2514/3.44079
[research_kong_jiang_2017]: https://doi.org/10.12783/dteees/edep2016/5956
[research_kong_li_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001470
[research_kong_park_2018]: https://doi.org/10.1007/s12239-018-0037-9
[research_kong_su_2026]: https://doi.org/10.1016/j.ast.2026.111722
[research_kopasakisgeorge_connollyjosephw_2012]: https://ntrs.nasa.gov/citations/20120018047
[research_kopasakisgeorge_connollyjosephw_2012_b]: https://ntrs.nasa.gov/citations/20120000915
[research_kopzon_1958]: https://doi.org/10.1016/0021-8928(58)90040-6
[research_korn_1974]: https://doi.org/10.2514/3.60390
[research_korn_1974_b]: https://doi.org/10.2514/6.1974-234
[research_kostin_zhuravskiy_2023]: https://doi.org/10.26467/2079-0619-2023-26-4-77-92
[research_kosuge_ito_1982]: https://doi.org/10.1115/1.3227344
[research_kothari_1971]: https://doi.org/10.1016/0022-3115(71)90167-x
[research_kothari_1973]: https://doi.org/10.1016/0022-3115(73)90191-8
[research_kotov_ruleva_2018]: https://doi.org/10.1088/1742-6596/1009/1/012038
[research_kovacs_csik_2023]: https://doi.org/10.1016/j.tsep.2023.101906
[research_koyyalamudi_nagpurwala_2016]: https://doi.org/10.1155/2016/2371524
[research_kozakiewicz_adamczyk_2025]: https://doi.org/10.3390/en18082064
[research_kraiko_tilliaeva_1973]: https://doi.org/10.1016/0021-8928(73)90088-9
[research_kramer_hall_2026]: https://doi.org/10.1115/1.4072203
[research_kramerbe_potterdy_1966]: https://ntrs.nasa.gov/citations/19670016544
[research_krashchenko_statsenko_1981]: https://doi.org/10.1007/bf00762177
[research_krause_1981]: https://doi.org/10.2514/3.50927
[research_krebs_1976]: https://ntrs.nasa.gov/citations/19770011069
[research_krenkel_salzman_1968]: https://doi.org/10.2514/3.43962
[research_kretov_2021]: https://doi.org/10.1108/aeat-11-2020-0256
[research_krivec_ling_1984]: https://doi.org/10.4271/841539
[research_krivenyuk_tsvilyuk_1971]: https://doi.org/10.1007/bf01533595
[research_krupa_2019]: https://doi.org/10.1017/aer.2019.53
[research_krushnaraokotteda_mittal_2016]: https://doi.org/10.2514/1.b35699
[research_kuchar_wolf_1993]: https://doi.org/10.2514/3.23668
[research_kuchinka_1966]: https://doi.org/10.2514/3.43727
[research_kucuk_tuncer_2024]: https://doi.org/10.1007/s11081-023-09877-x
[research_kumar_1999]: https://doi.org/10.14429/dsj.49.3828
[research_kumar_2022]: https://doi.org/10.26706/jtfs.3.1.20211202
[research_kumar_dwivedi_2022]: https://doi.org/10.1007/s12046-022-01996-y
[research_kumar_pradeep_2022]: https://doi.org/10.1115/1.4053955
[research_kumazaki_shimamura_2026]: https://doi.org/10.2514/6.2026-1104
[research_kun_tingting_2018]: https://doi.org/10.1515/htmp-2015-0226
[research_kurganov_2006]: https://doi.org/10.1615/atoz.a.adibwtemp
[research_kurkov_soeder_1975]: https://doi.org/10.2514/3.59818
[research_kursakov_kazhan_2016]: https://doi.org/10.1063/1.4964066
[research_kurtenbach_1978]: https://ntrs.nasa.gov/citations/19790004873
[research_kutschera_render_1999]: https://doi.org/10.2514/6.1999-4020
[research_kutschera_render_2003]: https://doi.org/10.1017/s0001924000130052
[research_kuzmich_sekundov_1975]: https://doi.org/10.1007/bf01023266
[research_kuzmin_2024]: https://doi.org/10.1007/s42401-023-00268-9
[research_kwak_lee_2013]: https://doi.org/10.6112/kscfe.2013.18.2.078
[research_kwiatkowski_sieradzki_2022]: https://doi.org/10.2478/tar-2022-0001
[research_kwon_sankar_1991]: https://doi.org/10.2514/6.1991-278
[research_kwon_sankar_1992]: https://doi.org/10.2514/3.46258
[research_laderman_2021]: https://doi.org/10.32920/ryerson.14656140
[research_lai_findley_1980]: https://doi.org/10.21236/ada095410
[research_lai_kamaruddin_2018]: https://doi.org/10.1088/1757-899x/370/1/012055
[research_laitone_1978]: https://doi.org/10.2514/3.58339
[research_lamarje_1986]: https://ntrs.nasa.gov/citations/19860052312
[research_lamarjohne_1987]: https://ntrs.nasa.gov/citations/19880003937
[research_lamberthh_mizukamim_1999]: https://ntrs.nasa.gov/citations/19990110638
[research_lampropoulos_sarris_2025]: https://doi.org/10.3844/jastsp.2025.1.11
[research_lane_behenna_1991]: https://doi.org/10.1115/1.2906527
[research_langan_samuels_1995]: https://doi.org/10.2514/6.1995-442
[research_langener_myrabo_2009]: https://doi.org/10.2514/6.2009-4806
[research_langham_1978]: https://doi.org/10.21236/ada058142
[research_lapin_crookshanks_1952]: https://doi.org/10.2514/8.2336
[research_large_1981]: https://doi.org/10.1017/s0001924000030062
[research_larrabeeee_1975]: https://ntrs.nasa.gov/citations/19760003917
[research_larson_1960_d]: https://doi.org/10.2172/12393926
[research_latham_1976]: https://ntrs.nasa.gov/citations/19760020078
[research_latham_2020]: https://doi.org/10.4324/9781003102854-5
[research_latham_gawienowski_1977]: https://ntrs.nasa.gov/citations/19770017116
[research_lawley_koczak_1984]: https://doi.org/10.21236/ada141780
[research_lawley_koczak_1985]: https://doi.org/10.21236/ada170697
[research_lawrence_1953]: https://doi.org/10.2514/8.2724
[research_leadon_scott_1956]: https://doi.org/10.21236/ad0082502
[research_lecuyer_morrison_1971]: https://doi.org/10.2514/3.59131
[research_lee_ahn_2010]: https://doi.org/10.5139/jksas.2010.38.11.1067
[research_lee_boedicker_1985]: https://doi.org/10.2514/6.1985-3073
[research_lee_franz_1976]: https://doi.org/10.2514/6.1976-672
[research_lee_kim_2024]: https://doi.org/10.2514/1.c037495
[research_lee_ko_2018]: https://doi.org/10.1115/1.4039232
[research_lee_lee_2016]: https://doi.org/10.1007/s00193-016-0630-7
[research_lee_lee_2019]: https://doi.org/10.1007/s42405-019-00175-4
[research_lee_sanders_2002]: https://doi.org/10.21236/ada398914
[research_leebj_lioumayfun_2018]: https://ntrs.nasa.gov/citations/20190002760
[research_leebyungjoon_lioumayfun_2018]: https://ntrs.nasa.gov/citations/20180005439
[research_leebyungjoon_lioumayfun_2019]: https://ntrs.nasa.gov/citations/20190031843
[research_leeja_1998]: https://ntrs.nasa.gov/citations/19990019483
[research_leejonathana_2003]: https://ntrs.nasa.gov/citations/20040035597
[research_leejonathana_chenposhou_2002]: https://ntrs.nasa.gov/citations/20020060119
[research_leejonathana_munafopaulm_2002]: https://ntrs.nasa.gov/citations/20030001009
[research_lehtinen_zeller_1972]: https://doi.org/10.1016/0005-1098(72)90027-1
[research_lehtinenb_zellerjr_1971]: https://ntrs.nasa.gov/citations/19720004248
[research_lehtinenb_zellerjr_1978]: https://ntrs.nasa.gov/citations/19780015081
[research_leinhos_schmid_2000]: https://doi.org/10.1115/2000-gt-0505
[research_leissler_nettles_1954]: https://ntrs.nasa.gov/citations/19630004111
[research_lemaysp_batillsm_1988]: https://ntrs.nasa.gov/citations/19880053508
[research_leng_feng_2024]: https://doi.org/10.1063/5.0188386
[research_lengyelkampmann_karboujian_2024]: https://doi.org/10.1007/s13272-024-00717-x
[research_leontiev_lushchik_2017]: https://doi.org/10.1134/s0018151x17020080
[research_leontiev_lushchik_2022]: https://doi.org/10.1134/s0018151x22030117
[research_leontiev_popovich_2017]: https://doi.org/10.1051/epjconf/201715900030
[research_leslie_1952]: https://doi.org/10.1093/qjmam/5.3.292
[research_leslie_perry_1954]: https://doi.org/10.1098/rspa.1954.0198
[research_lesser_niehuis_2014]: https://doi.org/10.1115/gt2014-26627
[research_levin_1997]: https://doi.org/10.2514/2.2232
[research_levylionelljr_1959]: https://ntrs.nasa.gov/citations/19980232076
[research_levylionelljr_yoshikawakennethk_1959]: https://ntrs.nasa.gov/citations/19980228237
[research_lewis_1976]: https://doi.org/10.2514/3.44525
[research_lewis_2002]: https://doi.org/10.21236/ada420631
[research_li_chen_2024]: https://doi.org/10.1016/j.ijplas.2024.103892
[research_li_chu_2024]: https://doi.org/10.1063/5.0236969
[research_li_ding_2023]: https://doi.org/10.1016/j.ast.2023.108667
[research_li_dong_2021]: https://doi.org/10.1016/j.cja.2021.02.005
[research_li_dong_2022]: https://doi.org/10.3390/aerospace9100628
[research_li_dong_2025]: https://doi.org/10.3390/met15060677
[research_li_du_2019]: https://doi.org/10.1016/j.ast.2018.12.018
[research_li_du_2020]: https://doi.org/10.1016/j.ast.2020.105886
[research_li_du_2020_b]: https://doi.org/10.1016/j.ast.2019.105554
[research_li_geiselhart_2021]: https://doi.org/10.2514/1.j059237
[research_li_geiselhart_2022]: https://doi.org/10.2514/1.c036656
[research_li_geiselhart_2026]: https://doi.org/10.2514/1.c038747
[research_li_hou_2024]: https://doi.org/10.2478/amns-2024-1078
[research_li_li_2024]: https://doi.org/10.3390/aerospace11070536
[research_li_liu_2022]: https://doi.org/10.1016/j.ast.2022.107685
[research_li_liu_2024]: https://doi.org/10.2514/1.j064454
[research_li_liu_2024_b]: https://doi.org/10.1115/1.4065617
[research_li_lu_2024]: https://doi.org/10.3390/aerospace11020141
[research_li_pan_2015]: https://doi.org/10.1016/j.applthermaleng.2014.09.071
[research_li_qu_2025]: https://doi.org/10.1063/5.0270314
[research_li_soskin_2019]: https://doi.org/10.1109/access.2019.2915917
[research_li_sun_2022]: https://doi.org/10.1016/j.jmst.2022.01.010
[research_li_sun_2025]: https://doi.org/10.1016/j.fmre.2024.03.018
[research_li_tian_2021]: https://doi.org/10.3390/cryst11060646
[research_li_xia_2024]: https://doi.org/10.1016/j.cja.2024.07.007
[research_li_xu_2015]: https://doi.org/10.1016/j.proeng.2014.12.707
[research_li_xu_2024]: https://doi.org/10.3390/aerospace11070514
[research_li_zhao_2026]: https://doi.org/10.1016/j.ast.2025.110962
[research_li_zheng_2021]: https://doi.org/10.1016/j.ast.2021.106752
[research_li_zheng_2023]: https://doi.org/10.1016/j.ast.2023.108373
[research_li_zhu_2022]: https://doi.org/10.3390/en15103612
[research_li_zhu_2023]: https://doi.org/10.1016/j.ast.2023.108530
[research_li_zhu_2024]: https://doi.org/10.1115/1.4064421
[research_li_zhu_2024_b]: https://doi.org/10.1016/j.ast.2024.109007
[research_lian_xiong_2025]: https://doi.org/10.1088/1742-6596/3085/1/012011
[research_liang_zhang_1989]: https://doi.org/10.2514/6.1989-2470
[research_lichtensteinjacobh_1952]: https://ntrs.nasa.gov/citations/19930092137
[research_liddell_1950]: https://doi.org/10.4271/500058
[research_liewkh_uripe_2005]: https://ntrs.nasa.gov/citations/20050207438
[research_likhachev_2024]: https://doi.org/10.22363/2313-0660-2024-24-1-92-106
[research_lin_1982]: https://doi.org/10.2514/6.1982-1326
[research_lin_1982_b]: https://doi.org/10.2514/6.1982-366
[research_lin_bai_2022]: https://doi.org/10.1155/2022/1139648
[research_lin_liu_2021]: https://doi.org/10.1038/s41598-021-94261-x
[research_lin_shao_2020]: https://doi.org/10.1016/j.ast.2020.105785
[research_lin_zong_2026]: https://doi.org/10.1063/5.0334699
[research_linden_2022]: https://doi.org/10.2514/5.9781624106255.0429.0434
[research_linnell_1963]: https://doi.org/10.21236/ad0408661
[research_liou_benson_2010]: https://doi.org/10.2514/6.2010-9172
[research_liu_cao_2017]: https://doi.org/10.1016/j.ijheatmasstransfer.2017.04.001
[research_liu_chu_2024]: https://doi.org/10.3390/aerospace11070541
[research_liu_chu_2025]: https://doi.org/10.1007/s42405-025-00934-6
[research_liu_du_2025]: https://doi.org/10.1115/1.4069738
[research_liu_du_2026]: https://doi.org/10.1016/j.cja.2026.104346
[research_liu_huang_2023]: https://doi.org/10.1007/s11630-023-1780-4
[research_liu_jiang_2022]: https://doi.org/10.1155/2022/9288966
[research_liu_kang_2022]: https://doi.org/10.1016/j.actaastro.2022.01.030
[research_liu_li_2016]: https://doi.org/10.1016/j.ast.2016.10.014
[research_liu_li_2022]: https://doi.org/10.1049/icp.2022.1963
[research_liu_li_2023]: https://doi.org/10.3390/aerospace10120989
[research_liu_sirignano_2000]: https://doi.org/10.2514/6.2000-741
[research_liu_vo_2024]: https://doi.org/10.1115/1.4065288
[research_liu_wang_2021]: https://doi.org/10.3390/app11199272
[research_liu_zhang_2022]: https://doi.org/10.1051/matecconf/202235501017
[research_liu_zhu_2015]: https://doi.org/10.1007/s00193-015-0605-0
[research_liu_zhu_2016]: https://doi.org/10.1142/9789813140622_0048
[research_liu_zhu_2024]: https://doi.org/10.1109/jsen.2023.3335858
[research_liu_zhu_2025]: https://doi.org/10.1109/tim.2025.3547093
[research_liu_zhu_2025_b]: https://doi.org/10.1016/j.measurement.2024.115985
[research_liu_zhu_2026]: https://doi.org/10.1109/tim.2026.3666019
[research_lock_1957]: https://doi.org/10.1017/s0022112057000385
[research_lockwoodve_1966]: https://ntrs.nasa.gov/citations/19660023730
[research_loh_lusty_1974]: https://doi.org/10.2514/6.1974-814
[research_lokotko_kharitonov_2006]: https://doi.org/10.1007/s10697-006-0084-1
[research_lomaxharvard_1957]: https://ntrs.nasa.gov/citations/19930092292
[research_lomaxharvard_heasletmaxa_1956]: https://ntrs.nasa.gov/citations/19930092279
[research_lorell_1989]: https://doi.org/10.21236/ada214500
[research_loren_kerr_1992]: https://doi.org/10.2514/6.1992-4201
[research_loth_candon_2016]: https://doi.org/10.2514/6.2016-0532
[research_lou_harrison_2022]: https://doi.org/10.1115/1.4055866
[research_lourenco_shih_1996]: https://doi.org/10.21236/ada310244
[research_loveless_boswell_1954]: https://doi.org/10.1108/eb032412
[research_lovell_2001]: https://doi.org/10.1007/978-3-540-45359-8_14
[research_lovelljcalvin_wilsonherbertajr_1947]: https://ntrs.nasa.gov/citations/19930093794
[research_lowe_2020]: https://doi.org/10.1108/aeat-11-2018-0285
[research_lu_li_2025]: https://doi.org/10.1063/5.0288892
[research_lu_wang_2025]: https://doi.org/10.1177/09576509251317280
[research_lu_yang_2019]: https://doi.org/10.1016/j.ast.2019.06.015
[research_lucas_1978]: https://doi.org/10.21236/adb028240
[research_lucas_obrien_2014]: https://doi.org/10.1115/gt2014-26666
[research_luce_jr_1949]: https://doi.org/10.21236/ada278113
[research_ludwig_1979]: https://doi.org/10.21236/ada077704
[research_lukyanov_hoang_2024]: https://doi.org/10.3390/drones8080388
[research_lundell_scherrer_1961]: https://ntrs.nasa.gov/citations/20040008090
[research_lundet_1977]: https://ntrs.nasa.gov/citations/19780005535
[research_luning_bangqin_2021]: https://doi.org/10.1088/1757-899x/1081/1/012047
[research_luo_meng_2026]: https://doi.org/10.1016/j.ast.2026.112752
[research_luo_tao_2024]: https://doi.org/10.1061/jaeeez.aseng-5388
[research_luo_wei_2020]: https://doi.org/10.3390/en13010217
[research_luoju_2009]: https://doi.org/10.1109/iccae.2009.81
[research_lypchanskyi_janus_2024]: https://doi.org/10.1016/j.ijplas.2024.103969
[research_lyubimov_2024]: https://doi.org/10.1134/s2070048224010071
[research_lyubimov_potekhina_2016]: https://doi.org/10.1134/s0018151x16050187
[research_m_v_2017]: https://doi.org/10.14445/23488360/ijme-v4i6p106
[research_ma_2021]: https://doi.org/10.1016/j.tsep.2020.100787
[research_ma_cui_2018]: https://doi.org/10.2514/1.j056858
[research_ma_li_2025]: https://doi.org/10.1063/5.0278832
[research_ma_li_2026]: https://doi.org/10.1016/j.dt.2026.07.017
[research_ma_lu_2025]: https://doi.org/10.1016/j.paerosci.2025.101082
[research_ma_wang_2025]: https://doi.org/10.1063/5.0254496
[research_ma_yang_2025]: https://doi.org/10.1016/j.applthermaleng.2025.127033
[research_macinnis_1994]: https://doi.org/10.2514/6.1994-2960
[research_macmanus_chiereghin_2017]: https://doi.org/10.2514/1.j054905
[research_madelung_1977]: https://doi.org/10.2514/6.1977-1219
[research_maekawa_higashi_1978]: https://doi.org/10.1299/kikai1938.44.2304
[research_maghsoudi_vaziry_2020]: https://doi.org/10.1016/j.cja.2019.12.002
[research_magrini_benini_2023]: https://doi.org/10.1016/j.ast.2022.108048
[research_magrini_benini_2026]: https://doi.org/10.1063/5.0329926
[research_mahlmeister_ishimoto_1955]: https://doi.org/10.21236/ad0093337
[research_mahorter_robertg_1961]: https://doi.org/10.21236/ad0266590
[research_maikapar_1959]: https://doi.org/10.1016/0021-8928(59)90104-2
[research_maikapar_1966]: https://doi.org/10.1016/0021-8928(66)90071-2
[research_maise_1970]: https://doi.org/10.2514/3.44202
[research_maitra_2010]: https://doi.org/10.1007/s12046-010-0044-7
[research_makiralphl_1959]: https://ntrs.nasa.gov/citations/19980228300
[research_maksimovich_karpinos_1977]: https://doi.org/10.1007/bf01528510
[research_malan_brown_1994]: https://doi.org/10.2514/3.46539
[research_malashenko_vashchilo_1975]: https://doi.org/10.1007/bf01522859
[research_malcolm_ng_1991]: https://ntrs.nasa.gov/citations/19920009549
[research_malicki_malecha_2023]: https://doi.org/10.3390/en16227590
[research_malikov_miltsov_2019]: https://doi.org/10.18372/2310-5461.40.13278
[research_malmuth_1966]: https://doi.org/10.2514/3.3483
[research_malmuth_wu_1987]: https://doi.org/10.2514/3.45417
[research_malonemichaelb_peaveycharlesc_1999]: https://ntrs.nasa.gov/citations/20000044629
[research_malvi_roy_2021]: https://doi.org/10.1007/s11666-021-01189-9
[research_mamonova_soudakov_2019]: https://doi.org/10.1088/1742-6596/1268/1/012067
[research_mancini_vos_2019]: https://doi.org/10.2514/6.2019-3272
[research_mann_garner_1977]: https://doi.org/10.21236/ada040707
[research_manolescu_1994]: https://doi.org/10.2514/6.1994-3528
[research_mansfield_1967]: https://doi.org/10.1017/s000192400005418x
[research_mao_liu_2016]: https://doi.org/10.1177/0954410016630565
[research_mao_liu_2017]: https://doi.org/10.3390/en10081153
[research_mao_zhang_2025]: https://doi.org/10.56028/aetr.15.1.2134.2025
[research_maples_1979]: https://doi.org/10.21236/ada069807
[research_margalida_joseph_2020]: https://doi.org/10.3390/ijtpp5030016
[research_margoliskenneth_1947]: https://ntrs.nasa.gov/citations/19930082080
[research_margoliskenneth_malvestutofranksjr_1958]: https://ntrs.nasa.gov/citations/19930084830
[research_marshall_1973]: https://doi.org/10.2514/3.60226
[research_marshall_schweikhard_1973]: https://ntrs.nasa.gov/citations/19730007281
[research_marshallrt_1971]: https://ntrs.nasa.gov/citations/19710017526
[research_martensson_2021]: https://doi.org/10.3390/aerospace8030058
[research_martensson_billson_2024]: https://doi.org/10.1115/1.4065517
[research_martensson_lejon_2022]: https://doi.org/10.1017/aer.2022.28
[research_martin_brazzel_1970]: https://doi.org/10.21236/ad0871913
[research_marty_castillon_2022]: https://doi.org/10.1115/1.4056090
[research_marvin_1968]: https://doi.org/10.2514/6.1968-648
[research_masaki_ogushi_2021]: https://doi.org/10.1088/1742-6596/1909/1/012081
[research_mascitti_1966]: https://ntrs.nasa.gov/citations/19660016261
[research_mascitti_1969]: https://ntrs.nasa.gov/citations/19700001663
[research_masonwh_1983]: https://ntrs.nasa.gov/citations/19840007047
[research_masonwh_siclarimj_1983]: https://ntrs.nasa.gov/citations/19830035489
[research_mathausereldone_deveikiswilliamd_1955]: https://ntrs.nasa.gov/citations/19930093819
[research_mathausereldone_deveikiswilliamd_1957]: https://ntrs.nasa.gov/citations/19930092300
[research_mathur_1998]: https://doi.org/10.2514/2.2400
[research_matrangagenej_armstrongneila_1959]: https://ntrs.nasa.gov/citations/19980235626
[research_matsumoto_sekiya_1975]: https://doi.org/10.1299/kikai1938.41.736
[research_mauch_oldakowski_1980]: https://doi.org/10.21236/ada089067
[research_mayer_paynter_1994]: https://doi.org/10.2514/6.1994-580
[research_mays_1971]: https://doi.org/10.2514/3.44258
[research_mazhul_2020]: https://doi.org/10.1134/s0869864320040046
[research_mazurov_2015]: https://doi.org/10.1615/tsagiscij.v46.i6.40
[research_mazurov_2019]: https://doi.org/10.1615/tsagiscij.2019030084
[research_mazzawyrs_banksga_1976]: https://ntrs.nasa.gov/citations/19760014117
[research_mazzawyrs_banksga_1977]: https://ntrs.nasa.gov/citations/19770009079
[research_mcaulayje_abdelwahabm_1972]: https://ntrs.nasa.gov/citations/19720019364
[research_mcclure_sirbaugh_1991]: https://doi.org/10.21236/ada232101
[research_mccormick_1959]: https://doi.org/10.2514/8.8022
[research_mcguigan_1970]: https://doi.org/10.2514/6.1970-513
[research_mckeehen_cord_1997]: https://doi.org/10.21236/ada327802
[research_mclemorehclyde_1958]: https://ntrs.nasa.gov/citations/19980231988
[research_mclemorehclyde_petersonjohnbjr_1960]: https://ntrs.nasa.gov/citations/19980228270
[research_mcmillinsn_woodrm_1986]: https://ntrs.nasa.gov/citations/19860053087
[research_mcqueen_1976]: https://doi.org/10.1243/jmes_jour_1976_018_038_02
[research_mcvey_rejeske_1969]: https://doi.org/10.21236/ad0861763
[research_mechanism_of_2021]: https://doi.org/10.47176/jafm.14.06.32577
[research_mechanism_study_2023]: https://doi.org/10.1063/5.0149263
[research_medina_patel_2021]: https://doi.org/10.2514/6.2021-2780
[research_mehalic_1988]: https://doi.org/10.2514/6.1988-3016
[research_melick_ybarra_1975]: https://doi.org/10.2514/6.1975-1213
[research_melick_ybarra_1978]: https://doi.org/10.2514/6.1978-970
[research_melickhcjr_1973]: https://ntrs.nasa.gov/citations/19730012966
[research_meneesgenep_boydjohnw_1959]: https://ntrs.nasa.gov/citations/19980228046
[research_menegozzo_benini_2020]: https://doi.org/10.1115/1.4048174
[research_meng_fan_2018]: https://doi.org/10.1177/0954410018787137
[research_menon_sanjayshivam_2023]: https://doi.org/10.1016/j.matpr.2022.08.231
[research_merchant_radhakrishnan_2017]: https://doi.org/10.1088/1757-899x/225/1/012298
[research_merkli_1975]: https://doi.org/10.21236/ada033630
[research_merkli_1976]: https://doi.org/10.2514/3.61352
[research_merritt_cliff_1985]: https://ntrs.nasa.gov/citations/19850053199
[research_messing_rabb_1952]: https://ntrs.nasa.gov/citations/19930087635
[research_miao_guan_2026]: https://doi.org/10.1016/j.ast.2026.112758
[research_miao_sun_2024]: https://doi.org/10.1109/epee63731.2024.10875093
[research_michellga_1971]: https://ntrs.nasa.gov/citations/19720002377
[research_miele_1954]: https://doi.org/10.2514/8.3207
[research_mieleangelo_1955]: https://ntrs.nasa.gov/citations/19930093841
[research_mikhail_1979]: https://doi.org/10.21236/ada076116
[research_mikhailov_mikhailova_2017]: https://doi.org/10.1016/j.proeng.2017.02.290
[research_miki_kameda_2014]: https://doi.org/10.2514/6.2014-3798
[research_miki_watanabe_2015]: https://doi.org/10.2322/jjsass.63.265
[research_milenkovicbabic_samardzic_2017]: https://doi.org/10.1108/aeat-02-2016-0026
[research_miles_1953]: https://doi.org/10.1017/s0001925900000901
[research_military_presence_2025]: https://doi.org/10.31249/ape/2025.04.08
[research_miller_1977]: https://doi.org/10.2514/6.1977-105
[research_miller_1983]: https://doi.org/10.2514/6.1983-2482
[research_miller_1986]: https://doi.org/10.2514/3.45268
[research_miller_smith_2003]: https://doi.org/10.1115/fedsm2003-45471
[research_millerds_pittmanjl_1983]: https://ntrs.nasa.gov/citations/19830047131
[research_millidere_yigit_2022]: https://doi.org/10.2514/6.2022-1428
[research_mills_1978]: https://doi.org/10.1115/1.3443471
[research_min_xian_2024]: https://doi.org/10.1108/mmms-11-2023-0376
[research_ming_wu_2023]: https://doi.org/10.1016/j.ast.2023.108578
[research_minjb_reddytsr_2018]: https://ntrs.nasa.gov/citations/20180002213
[research_minnicino_gray_2009]: https://doi.org/10.21236/ada506416
[research_mintint_2018]: https://doi.org/10.47119/ijrp10020112019484
[research_mironov_1965]: https://doi.org/10.1007/bf00831824
[research_mitcham_stevens_1951]: https://ntrs.nasa.gov/citations/20050030034
[research_mitsuyasu_1956]: https://doi.org/10.2322/jjsass1953.4.131
[research_miura_yamashita_2021]: https://doi.org/10.1115/1.4050439
[research_mixed_flow_2018]: https://doi.org/10.2514/5.9781624105173.0671.0678
[research_mizobata_mio_2024]: https://doi.org/10.3390/aerospace11090777
[research_mock_1951]: https://doi.org/10.4271/510198
[research_moeckelwe_1955]: https://ntrs.nasa.gov/citations/19930084178
[research_moeckelwe_evanspjjr_1951]: https://ntrs.nasa.gov/citations/19930090411
[research_moens_2022]: https://doi.org/10.3390/aerospace10010007
[research_moga_1980]: https://doi.org/10.21236/ada091235
[research_moin_lele_1998]: https://doi.org/10.21236/ada343835
[research_moirou_sanders_2023]: https://doi.org/10.1016/j.paerosci.2023.100897
[research_mokotoff_arnson_2026]: https://doi.org/10.2514/1.c038452
[research_molana_khodaparast_2020]: https://doi.org/10.1007/s40435-020-00681-4
[research_montanojw_1967]: https://ntrs.nasa.gov/citations/19670045542
[research_moon_2025]: https://doi.org/10.6108/kspe.2025.29.4.055
[research_moore_1973]: https://doi.org/10.21236/ad0756481
[research_moore_lueke_1974]: https://doi.org/10.1115/1.3438443
[research_moorhouse_jenkins_1975]: https://doi.org/10.2514/3.44474
[research_morgenfeld_1992]: https://doi.org/10.2514/6.1992-1087
[research_morris_nelms_1976]: https://ntrs.nasa.gov/citations/19770009073
[research_morton_1956]: https://doi.org/10.1108/eb032772
[research_moru_bo_2022]: https://doi.org/10.1016/j.ast.2022.108008
[research_mount_1965]: https://doi.org/10.2514/3.43670
[research_mozley_1943]: https://doi.org/10.2514/8.11032
[research_muchmorecbjr_1988]: https://ntrs.nasa.gov/citations/19880053479
[research_muehter_1974]: https://doi.org/10.21236/ada043526
[research_mugalev_savushkina_1985]: https://doi.org/10.1007/bf01529153
[research_muller_gasko_1967]: https://doi.org/10.2514/3.43825
[research_muller_gasko_1967_b]: https://doi.org/10.2514/3.43842
[research_mungallrobertc_1948]: https://ntrs.nasa.gov/citations/19930082436
[research_munjulury_staack_2015]: https://doi.org/10.1007/s13272-015-0174-z
[research_murphypatrickc_kleinvladislav_2006]: https://ntrs.nasa.gov/citations/20060047570
[research_murzionak]: https://doi.org/10.22215/etd/2013-06868
[research_musa_huang_2024]: https://doi.org/10.1063/5.0239660
[research_muth_bindl_2009]: https://doi.org/10.2514/6.2009-4826
[research_myerslawrencep_walshkevinr_1988]: https://ntrs.nasa.gov/citations/19880051520
[research_myokan_kubota_2020]: https://doi.org/10.2514/1.j058519
[research_nadell_1996]: https://doi.org/10.2514/6.1996-2550
[research_nagamatsu_workman_1960]: https://doi.org/10.2514/8.5173
[research_nagao_yoshida_2019]: https://doi.org/10.2322/astj.jsass-d-18-00007
[research_nageswararao_kushari_2020]: https://doi.org/10.2514/1.b37674
[research_nagler_2022]: https://doi.org/10.37394/232022.2022.2.14
[research_nagler_2026]: https://doi.org/10.1177/15485129261459679
[research_nam_mavris_2018]: https://doi.org/10.2514/1.c032099
[research_narayan_1975]: https://doi.org/10.1017/s0001925900007332
[research_naruse_ishii_2022]: https://doi.org/10.1299/transjsme.21-00357
[research_naseri_boroomand_2016]: https://doi.org/10.1007/s11630-016-0891-6
[research_navy_participation_1998]: https://doi.org/10.2514/5.9781600867910.0235.0240
[research_neal_smith_1970]: https://doi.org/10.21236/ad0880252
[research_neal_smith_1970_b]: https://doi.org/10.21236/ad0880426
[research_neaves_mcrae_1995]: https://doi.org/10.1115/imece1995-0407
[research_negaard_1979]: https://doi.org/10.21236/ada363019
[research_neitzel_hemsworth_1966]: https://doi.org/10.2514/3.43746
[research_nelmswpjr_baileyro_1974]: https://ntrs.nasa.gov/citations/19740020394
[research_nelson_lowe_2014]: https://doi.org/10.2514/6.2014-0533
[research_nelsonrobertl_welshclementj_1960]: https://ntrs.nasa.gov/citations/19980227964
[research_neshpor_armyagov_1991]: https://doi.org/10.1007/bf00777164
[research_ness_1971]: https://doi.org/10.2514/3.44301
[research_nettles_1956]: https://ntrs.nasa.gov/citations/19660010449
[research_neumark_1950]: https://doi.org/10.1108/eb031964
[research_neverlien_moe_2020]: https://doi.org/10.4173/mic.2020.2.1
[research_neville_oflarity_1992]: https://doi.org/10.2514/6.1992-1036
[research_newsomerw_thomasjl_1986]: https://ntrs.nasa.gov/citations/19860017733
[research_ng_willcox_2016]: https://doi.org/10.2514/1.c033352
[research_nganangelen_biezaddaniel_1996]: https://ntrs.nasa.gov/citations/19960041232
[research_nguyenlt_anglinel_1976]: https://ntrs.nasa.gov/citations/19760053944
[research_nicholas_naville_1984]: https://ntrs.nasa.gov/citations/19840062226
[research_nichols_rinkoski_1952]: https://ntrs.nasa.gov/citations/19930083216
[research_nicholsmarkr_pendleyroberte_1952]: https://ntrs.nasa.gov/citations/19930086995
[research_nicholson_1985]: https://doi.org/10.21236/ada159292
[research_nielsenjackn_kaattarigeorgee_1953]: https://ntrs.nasa.gov/citations/19930093732
[research_nielsenjn_1985]: https://ntrs.nasa.gov/citations/19850037607
[research_niknamian_2019]: https://doi.org/10.31219/osf.io/xh7s9
[research_ning]: https://doi.org/10.22215/etd/2026-17071
[research_northropaircraftinchawthorneca_1952_b]: https://doi.org/10.21236/ad0004591
[research_northropaircraftinchawthorneca_1953]: https://doi.org/10.21236/ad0013465
[research_novikov_2017]: https://doi.org/10.2514/6.2017-4517
[research_numerical_simulation_2020]: https://doi.org/10.36884/jafm.13.05.31018
[research_numerical_simulation_2021]: https://doi.org/10.17762/turcomat.v12i6.2101
[research_nussdorfertheodorej_oberyleonardj_1952]: https://ntrs.nasa.gov/citations/19930086890
[research_obeyleonardt_englertgeraldw_1952]: https://ntrs.nasa.gov/citations/19930094389
[research_obikane_1984]: https://doi.org/10.2514/6.1984-1364
[research_ochonogor_akinlabi_2017]: https://doi.org/10.1016/j.matpr.2017.01.019
[research_ogawa_takeda_2015]: https://doi.org/10.4236/ojfd.2015.53028
[research_ohashi_ohno_1982]: https://doi.org/10.1016/0022-5096(82)90001-1
[research_ohwada_shimada_2019]: https://doi.org/10.1186/s42774-019-0001-z
[research_ohyama_1978]: https://doi.org/10.1299/kikai1938.44.3810
[research_okelah_1985]: https://doi.org/10.21608/asat.1985.26520
[research_okelly_1954]: https://ntrs.nasa.gov/citations/20090023309
[research_olwi_1995]: https://doi.org/10.2514/6.1995-3465
[research_orman_rae_1951]: https://doi.org/10.1098/rspa.1951.0206
[research_oruc_2026]: https://doi.org/10.36306/konjes.1810207
[research_oruc_baklacioglu_2022]: https://doi.org/10.1016/j.energy.2022.125069
[research_oruc_baklacioglu_2023]: https://doi.org/10.1016/j.energy.2023.126819
[research_osborneroberts_kellythomasc_1953]: https://ntrs.nasa.gov/citations/19930087537
[research_osmon_1967]: https://doi.org/10.2514/6.1967-449
[research_ostieri_tognaccini_2018]: https://doi.org/10.2514/1.c034820
[research_ostowaric_naikd_1986]: https://ntrs.nasa.gov/citations/19860041891
[research_oswatitsch_1947]: https://ntrs.nasa.gov/citations/19990049423
[research_oswatitsch_1952]: https://doi.org/10.1007/978-3-7091-3502-0
[research_oswatitsch_1958]: https://ntrs.nasa.gov/citations/20030065153
[research_oswatitsch_1980]: https://doi.org/10.1007/978-3-322-91082-0
[research_otto_trefny_2015]: https://doi.org/10.2514/6.2015-3700
[research_overall_1976]: https://doi.org/10.21236/ada033883
[research_page_hield_2018]: https://doi.org/10.1115/1.4040030
[research_pakle_jiang_2018]: https://doi.org/10.1016/j.jppr.2018.02.004
[research_palienko_pogrebnyak_1976]: https://doi.org/10.1007/bf01528209
[research_palko_1973]: https://doi.org/10.21236/ad0769307
[research_palko_1974]: https://doi.org/10.21236/ad0787659
[research_palko_1975]: https://doi.org/10.21236/ada012880
[research_pan_huang_2017]: https://doi.org/10.5028/jatm.v9i1.736
[research_pan_mu_2024]: https://doi.org/10.3390/aerospace11110911
[research_pan_shi_2022]: https://doi.org/10.3390/en15165791
[research_pan_shi_2024]: https://doi.org/10.1016/j.ast.2023.108780
[research_panov_shvets_1966]: https://doi.org/10.1007/bf01022287
[research_panov_shvets_1967]: https://doi.org/10.1007/bf01015152
[research_panton_1972]: https://doi.org/10.2514/3.59052
[research_panzeri_savelyev_2018]: https://doi.org/10.1016/j.trpro.2018.02.026
[research_papadales_basils_1979]: https://doi.org/10.21236/ada073100
[research_papageorgiou_tarkian_2018]: https://doi.org/10.2514/1.c034314
[research_papirno_1966]: https://doi.org/10.21236/ad0642159
[research_papirno_gerard_1962]: https://doi.org/10.21236/ada398798
[research_paraguassu_2015]: https://doi.org/10.17485/ijst/2015/v8i31/87309
[research_paranjape_ananthkrishnan_2023]: https://doi.org/10.61653/joast.v58i2.2006.706
[research_parisenrichardb_armstrongjohnc_1948]: https://ntrs.nasa.gov/citations/19930082371
[research_park_chung_1993]: https://doi.org/10.2514/6.1993-883
[research_park_chung_2016]: https://doi.org/10.1017/aer.2015.17
[research_park_chung_2016_b]: https://doi.org/10.5139/ijass.2016.17.2.268
[research_park_chung_2018]: https://doi.org/10.1108/aeat-06-2017-0149
[research_park_kim_2026]: https://doi.org/10.1016/j.ast.2026.112263
[research_park_lee_2001]: https://doi.org/10.2514/6.2001-568
[research_park_lee_2015]: https://doi.org/10.1108/aeat-07-2013-0128
[research_parker_1991]: https://doi.org/10.2514/6.1991-2026
[research_parkes_1953]: https://doi.org/10.1108/eb032367
[research_parkes_1954]: https://doi.org/10.1108/eb032500
[research_parkes_1956]: https://doi.org/10.1108/eb032761
[research_parkes_1956_b]: https://doi.org/10.1108/eb032699
[research_parlier_1986]: https://doi.org/10.2514/6.1986-9810
[research_parris_sherman_1957]: https://doi.org/10.1520/stp44147s
[research_pasiuk_1963]: https://doi.org/10.21236/ad0448887
[research_patel_chudoba_2026]: https://doi.org/10.1108/aeat-01-2025-0015
[research_patil_2018]: https://doi.org/10.23940/ijpe.18.01.p2.916
[research_paton_bampton_1982]: https://doi.org/10.1016/b978-1-4832-8423-1.50117-6
[research_payne_1980]: https://doi.org/10.21236/ada087515
[research_paynter_1994]: https://doi.org/10.2514/6.1994-465
[research_paynter_chen_1983]: https://doi.org/10.2514/6.1983-1371
[research_paynter_mayer_1993]: https://doi.org/10.2514/6.1993-290
[research_paynter_treiber_1992]: https://doi.org/10.2514/6.1992-269
[research_paziresh_nikseresht_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000704
[research_peacock_1978]: https://doi.org/10.21236/ada062549
[research_pecinka_bugajski_2017]: https://doi.org/10.14311/ap.2017.57.0022
[research_peck_liu_2020]: https://doi.org/10.1115/gt2020-14169
[research_pengju_liang_2015]: https://doi.org/10.1016/j.proeng.2014.12.563
[research_penlandja_creeltrjr_1978]: https://ntrs.nasa.gov/citations/19780023102
[research_penlandja_fournierrh_1975]: https://ntrs.nasa.gov/citations/19760004991
[research_penningtonje_meintelajjr_1980]: https://ntrs.nasa.gov/citations/19810061133
[research_perepezko_2001]: https://doi.org/10.21236/ada391741
[research_perkins_dillenius_1991]: https://ntrs.nasa.gov/citations/19910034806
[research_persh_1955]: https://doi.org/10.21236/ad0075320
[research_petersenrb_1957]: https://ntrs.nasa.gov/citations/19660010455
[research_peterson_1982]: https://ntrs.nasa.gov/citations/19820017325
[research_petersonvictorl_meneesgenep_1959]: https://ntrs.nasa.gov/citations/19980228241
[research_petkovic_banjac_2025]: https://doi.org/10.1115/1.4069811
[research_petruzzelli_keane_2001]: https://doi.org/10.2514/2.2833
[research_pfaff_1965]: https://doi.org/10.21236/ad0467448
[research_pfaff_1968]: https://doi.org/10.21236/ad0832104
[research_pfnur_breitsamter_2019]: https://doi.org/10.2514/1.c035491
[research_pfyl_1955]: https://ntrs.nasa.gov/citations/19650003100
[research_pfyl_presley_1961]: https://ntrs.nasa.gov/citations/19980228128
[research_philippou_zachos_2024]: https://doi.org/10.3390/aerospace11010075
[research_phillips_jr_1999]: https://doi.org/10.21236/ada397472
[research_piccirillo_aronstein_1997]: https://doi.org/10.2514/4.868047
[research_piccirillo_gregorio_2024]: https://doi.org/10.3390/aerospace11090740
[research_piovesan_zachos_2025]: https://doi.org/10.2514/1.j064226
[research_pismennyi]: https://doi.org/10.34660/inf.2019.16.36674
[research_planeaux_barth_1988]: https://doi.org/10.2514/6.1988-4368
[research_platzer_1964]: https://ntrs.nasa.gov/citations/19650014528
[research_plourde_stenning_1968]: https://doi.org/10.2514/3.43933
[research_poggie_2019]: https://doi.org/10.2514/1.j058504
[research_poggie_porter_2018]: https://doi.org/10.2514/6.2018-4029
[research_polhamusec_1966]: https://ntrs.nasa.gov/citations/19670003842
[research_polhamusec_1968]: https://ntrs.nasa.gov/citations/19680022518
[research_poorman_1980]: https://ntrs.nasa.gov/citations/19800016860
[research_popovich_kirill_2014]: https://doi.org/10.1615/ihtc15.fcv.008962
[research_popovich_kiselev_2021]: https://doi.org/10.1088/1742-6596/2039/1/012029
[research_portnoy_1963]: https://doi.org/10.1017/s0001925900002833
[research_powell_glickstein_1988]: https://doi.org/10.2514/6.1988-2946
[research_powellag_welgehr_1985]: https://ntrs.nasa.gov/citations/19850018399
[research_powers_driggers_1983]: https://doi.org/10.2514/3.48214
[research_powers_driggers_1983_b]: https://doi.org/10.2514/6.1983-92
[research_powersbg_1966]: https://ntrs.nasa.gov/citations/19660023036
[research_praj_fghaffari_2003]: https://ntrs.nasa.gov/citations/20040040269
[research_prasad_2025]: https://doi.org/10.1115/1.4069510
[research_prasad_rivera_1996]: https://doi.org/10.21236/ada311100
[research_preliminary_design_2006]: https://doi.org/10.5139/jksas.2006.34.9.011
[research_presley_1975]: https://doi.org/10.2514/6.1975-1214
[research_presz_konarski_1971]: https://doi.org/10.2514/3.59196
[research_prigent_marechal_2015]: https://doi.org/10.1080/0305215x.2015.1062985
[research_prince_1976]: https://doi.org/10.1115/1.3446142
[research_probst_melberwilkending_2021]: https://doi.org/10.1108/hff-08-2021-0525
[research_processing_and]: https://doi.org/10.4271/air6345
[research_procurement_process_1980]: https://doi.org/10.1108/eb035653
[research_provenza_duffy_2018]: https://doi.org/10.1115/1.4040739
[research_pruitt_bates_1992]: https://doi.org/10.2514/6.1992-5091
[research_purserpaule_spearmargaretf_1947]: https://ntrs.nasa.gov/citations/19930082127
[research_qiang_xue_2024]: https://doi.org/10.1016/j.csite.2024.105032
[research_qiao_chu_2026]: https://doi.org/10.1063/5.0332543
[research_qin_2026]: https://doi.org/10.1142/s021812662642017x
[research_qin_liang_2016]: https://doi.org/10.12783/fae.2016.0501.02
[research_qiu_du_2023]: https://doi.org/10.1063/5.0171892
[research_qiu_zhao_2023]: https://doi.org/10.1063/5.0173396
[research_qiu_zhong_2024]: https://doi.org/10.33737/jgpps/191166
[research_qu_kong_2019]: https://doi.org/10.1007/s11433-018-9347-6
[research_qu_wang_2024]: https://doi.org/10.1063/5.0234961
[research_quan_sun_2024]: https://doi.org/10.1109/tase.2023.3258602
[research_queijomj_jaquetbyronm_1954]: https://ntrs.nasa.gov/citations/19930092215
[research_queijomj_wolhartwalterd_1951]: https://ntrs.nasa.gov/citations/19930086818
[research_quigleyherveyc_andersonsethb_1960]: https://ntrs.nasa.gov/citations/19980223993
[research_rademakers_probst_2018]: https://doi.org/10.2514/6.2018-1353
[research_radespiel_burnazzi_2016]: https://doi.org/10.1017/aer.2015.7
[research_radon_1969]: https://doi.org/10.1515/mt-1969-111201
[research_rafiq_qureshi_2022]: https://doi.org/10.3390/engproc2022023002
[research_rains_1955]: https://doi.org/10.1115/1.4014392
[research_rajagopalan_siddiqi_1985]: https://doi.org/10.2514/6.1985-253
[research_rajdeepbosemondal_2026]: https://doi.org/10.55041/ijsrem60571
[research_rakipoglu_avci_2026]: https://doi.org/10.30855/gmbd.070526n06
[research_ramachandra_sudhakar_1979]: https://doi.org/10.2514/6.1979-7004
[research_ramachandran_wells_1974]: https://doi.org/10.2514/6.1974-790
[research_ramachandran_wells_1975]: https://doi.org/10.2514/3.59883
[research_ramakrishna_senthilkumar_2019]: https://doi.org/10.1088/1742-6596/1276/1/012008
[research_ramamurti_2011]: https://doi.org/10.21236/ada546062
[research_ramaswamy_viswanathan_1975]: https://doi.org/10.2514/3.44506
[research_ramjet_supersonic_1958]: https://doi.org/10.1016/0016-0032(58)90466-6
[research_ran_mavris_2005]: https://doi.org/10.2514/6.2005-7357
[research_rand_1963]: https://doi.org/10.21236/ad0419249
[research_ransom_1983]: https://doi.org/10.2514/3.44917
[research_rao_kumar_2025]: https://doi.org/10.1017/aer.2025.37
[research_rao_sureshkumar_2022]: https://doi.org/10.1115/1.4055279
[research_raspet_1957]: https://doi.org/10.21236/ad0135753
[research_ratnayakenalina_2010]: https://ntrs.nasa.gov/citations/20100001729
[research_ray_hicks_1988]: https://ntrs.nasa.gov/citations/19880011767
[research_rayej_taylorrt_1965]: https://ntrs.nasa.gov/citations/19660033257
[research_raymer_1991]: https://doi.org/10.2514/6.1991-3170
[research_raymer_1998]: https://doi.org/10.1016/s1369-8869(98)00005-6
[research_rebuffetpierre_poissonquintonph_1952]: https://ntrs.nasa.gov/citations/19930093899
[research_reddy_govardhan_2023]: https://doi.org/10.1007/978-981-19-7709-1_3
[research_reedy_gorrell_2025]: https://doi.org/10.1115/1.4070352
[research_reggiori_1972]: https://doi.org/10.1007/bf02133600
[research_reid_1937]: https://doi.org/10.2514/8.438
[research_reinbold_breitsamter_2026]: https://doi.org/10.2514/1.c038409
[research_reist_koo_2022]: https://doi.org/10.2514/1.c036754
[research_rejeske_stava_1974]: https://doi.org/10.2514/6.1974-1145
[research_ren_zhang_2021]: https://doi.org/10.1016/j.applthermaleng.2021.116677
[research_report_no_1937]: https://doi.org/10.1016/s0016-0032(37)90824-x
[research_report_no_1939]: https://doi.org/10.1016/s0016-0032(39)90757-x
[research_resta_marsilio_2021]: https://doi.org/10.3390/fluids6120441
[research_rettie_lewis_1968]: https://doi.org/10.2514/3.43977
[research_reukaufpj_burchamfwjr_1976]: https://ntrs.nasa.gov/citations/19770011066
[research_reyhner_hickcox_1972]: https://doi.org/10.2514/3.59041
[research_reykers_fonck_2019]: https://doi.org/10.1177/0010836719850203
[research_reymer_zielinski_2018]: https://doi.org/10.2478/jok-2018-0057
[research_reynolds_1993]: https://doi.org/10.1016/0956-716x(93)90563-8
[research_rezamaadi_sepahiyounsi_2022]: https://doi.org/10.1016/j.expthermflusci.2021.110568
[research_rhomberg_1972]: https://doi.org/10.1016/b978-0-08-017526-3.50025-7
[research_ribner_1960]: https://doi.org/10.2514/8.8580
[research_riccobene_ricci_2015]: https://doi.org/10.1108/aeat-03-2013-0055
[research_richardswl_thompsonrandolphc_1991]: https://ntrs.nasa.gov/citations/19920068787
[research_righi_pachidis_2018]: https://doi.org/10.1016/j.ast.2018.04.021
[research_rivello_1965]: https://doi.org/10.21236/ad0471246
[research_rizzetta_1991]: https://doi.org/10.2514/6.1991-128
[research_rizzetta_visbal_2001]: https://doi.org/10.2514/6.2001-2858
[research_roache_1965]: https://doi.org/10.2514/3.59234
[research_roberts_1965]: https://doi.org/10.21236/ad0615928
[research_roberts_smith_1966]: https://doi.org/10.21236/ad0635953
[research_robertsosborne_thomasckelly_1960]: https://ntrs.nasa.gov/citations/20040047133
[research_robinsaw_beissnerfljr_1985]: https://ntrs.nasa.gov/citations/19850010668
[research_rockwell_2001]: https://doi.org/10.21236/ada402569
[research_rodgers_1965]: https://doi.org/10.2514/3.43615
[research_rodgers_1966]: https://doi.org/10.2514/3.43765
[research_roelofs_kurowicka_2021]: https://doi.org/10.2514/1.c035985
[research_rosell]: https://doi.org/10.63959/chalmers.dt/5862
[research_rosen_2001]: https://doi.org/10.1115/imece2001/aes-23645
[research_rosenbaumh_zeibergsl_1965]: https://ntrs.nasa.gov/citations/19660030698
[research_rosenthal_1975]: https://doi.org/10.4271/751077
[research_rosenthal_brandeau_1983]: https://doi.org/10.2514/6.1983-1052
[research_roskam_dusto_1969]: https://doi.org/10.2514/3.44100
[research_roskam_holgate_1968]: https://doi.org/10.2514/3.43981
[research_roth_doel_2005]: https://doi.org/10.1115/gt2005-68201
[research_rowe_1958]: https://doi.org/10.1243/pime_proc_1958_172_066_02
[research_rowe_sussman_1971]: https://doi.org/10.2514/3.44275
[research_roysalam_bil_2016]: https://doi.org/10.1017/aer.2016.59
[research_ruban_menezes_2020]: https://doi.org/10.1115/1.4048141
[research_rubio_ballard_1967]: https://doi.org/10.21236/ad0660321
[research_rudnitski]: https://doi.org/10.22215/etd/1983-00812
[research_rudolphpeterkc_1997]: https://ntrs.nasa.gov/citations/20080004619
[research_rumsey_slotnick_2019]: https://doi.org/10.2514/1.c034940
[research_rumseycharlesb_leedorothyb_1961]: https://ntrs.nasa.gov/citations/19980235513
[research_runstadler_peterw_1969]: https://doi.org/10.21236/ad0865300
[research_russell_2014]: https://doi.org/10.64628/aa.jcdrc3dhj
[research_rybalko_loth_2015]: https://doi.org/10.2514/1.j054050
[research_rylov_1974]: https://doi.org/10.1007/bf01031315
[research_sachs_1975]: https://doi.org/10.2514/3.44471
[research_sachs_1977]: https://doi.org/10.2514/3.44623
[research_sachs_1980]: https://doi.org/10.2514/3.44685
[research_sadraey_2017]: https://doi.org/10.1201/9781315366913-9
[research_safavi_tarkian_2015]: https://doi.org/10.1177/1063293x15587020
[research_safoklov_demidov_2025]: https://doi.org/10.3103/s1068799825070025
[research_sahoo_peetala_2010]: https://doi.org/10.1115/1.4001128
[research_sahu_1986]: https://doi.org/10.21236/ada171462
[research_said_mat_2018]: https://doi.org/10.12700/aph.15.8.2018.8.1
[research_sajadifar_maier_2023]: https://doi.org/10.3390/cryst13020269
[research_sakata_ohta_2017]: https://doi.org/10.1007/s11630-017-0907-x
[research_sakataif_davisgw_1975]: https://ntrs.nasa.gov/citations/19750055457
[research_sakataif_davisgw_1977]: https://ntrs.nasa.gov/citations/19770018637
[research_saleemyusoof_sivapragasam_2016]: https://doi.org/10.1016/j.jppr.2016.11.004
[research_samimy_webb_2011]: https://doi.org/10.21236/ada564713
[research_sanchezcarmona_cuernorejado_2018]: https://doi.org/10.1108/aeat-05-2017-0129
[research_sandahlcarla_1948]: https://ntrs.nasa.gov/citations/19930085426
[research_sanders_1980]: https://doi.org/10.2514/6.1980-1110
[research_sandstrom_white_1961]: https://doi.org/10.21236/ad0257074
[research_saporito_daronch_2023]: https://doi.org/10.1016/j.ast.2023.108349
[research_saraswathi_2000]: https://doi.org/10.14429/dsj.50.3366
[research_saravanan_desikan_2017]: https://doi.org/10.1017/aer.2017.115
[research_sasoh_myokan_2018]: https://doi.org/10.2514/6.2018-3179
[research_satyanarayana_prasad_1975]: https://doi.org/10.1109/cdc.1975.270730
[research_saundersjd_keithtgjr_1991]: https://ntrs.nasa.gov/citations/19910061195
[research_saves_diouane_2024]: https://doi.org/10.1007/s00158-024-03785-z
[research_saxenaashok_1998]: https://ntrs.nasa.gov/citations/19990116061
[research_schaffrath_nicke_2025]: https://doi.org/10.1115/1.4067687
[research_scherz_williams_1978]: https://doi.org/10.2514/3.55805
[research_schneideredwardt_1990]: https://ntrs.nasa.gov/citations/19900048975
[research_schoeler_1987]: https://doi.org/10.21236/ada195832
[research_schrage_1990]: https://doi.org/10.2514/6.1990-3300
[research_schuldenfreimarvin_comisarowpaul_1947]: https://ntrs.nasa.gov/citations/19930093791
[research_schulderfreimarvin_comisarowpaul_1951]: https://ntrs.nasa.gov/citations/19930083056
[research_schuster_1995]: https://doi.org/10.2514/3.46686
[research_schwanz_1972]: https://doi.org/10.21236/ada006391
[research_schwartz_1988]: https://doi.org/10.21236/ada200453
[research_schweiger_1987]: https://doi.org/10.2514/6.1987-2102
[research_schweikhardt_grippe_1971]: https://doi.org/10.2514/3.59197
[research_schwendemannmf_1981]: https://ntrs.nasa.gov/citations/19830003774
[research_scribben_withrow_2006]: https://doi.org/10.21236/ada463634
[research_sebata_ushijima_2021]: https://doi.org/10.1299/jsmemm.2021.os0106
[research_sebata_ushijima_2022]: https://doi.org/10.1299/transjsme.21-00273
[research_sederstrom_zagalsky_1973]: https://doi.org/10.21236/ad0763450
[research_sedlock_1985]: https://doi.org/10.21236/ada153767
[research_seginer_salomon_1983]: https://ntrs.nasa.gov/citations/19830013888
[research_seidel_matwey_1980]: https://doi.org/10.1115/1.3230362
[research_selegan_1983]: https://doi.org/10.1115/83-gt-243
[research_seleznev_2018]: https://doi.org/10.1088/1742-6596/1009/1/012034
[research_seleznev_2018_b]: https://doi.org/10.1088/1742-6596/1009/1/012030
[research_seleznev_2019]: https://doi.org/10.1088/1742-6596/1250/1/012004
[research_selna_schlaff_1951]: https://ntrs.nasa.gov/citations/19930093734
[research_semenov_1981]: https://doi.org/10.1007/bf00769005
[research_semlitsch_mihaescu_2016]: https://doi.org/10.1016/j.energy.2016.03.032
[research_semlitsch_mihaescu_2021]: https://doi.org/10.3390/aerospace8120369
[research_sepahiyounsi_2022]: https://doi.org/10.1016/j.ast.2021.107246
[research_sepahiyounsi_2025]: https://doi.org/10.1016/j.ast.2025.110346
[research_setayandeh_babaei_2020]: https://doi.org/10.1007/s00500-020-04684-3
[research_sgueglia_schmollgruber_2020]: https://doi.org/10.2514/1.c035509
[research_shahin_alqaradawi_2016]: https://doi.org/10.1016/j.apm.2016.07.030
[research_shahriyari_firouzabadi_2024]: https://doi.org/10.1038/s41598-024-55816-w
[research_shang_ge_2021]: https://doi.org/10.1088/1742-6596/1985/1/012025
[research_shao_cao_2016]: https://doi.org/10.1155/2016/8562716
[research_shariatzadeh_abrishamkar_2015]: https://doi.org/10.7763/jocet.2015.v3.198
[research_shechtman_1981]: https://doi.org/10.21236/ada102746
[research_shen_2017]: https://doi.org/10.4028/www.scientific.net/msf.898.387
[research_shen_wen_2018]: https://doi.org/10.2514/1.j056565
[research_sheng_chen_2020]: https://doi.org/10.1016/j.ast.2020.106139
[research_sheng_chen_2023]: https://doi.org/10.1016/j.cja.2022.08.021
[research_shevell_1978]: https://doi.org/10.2514/3.58419
[research_shi_2025]: https://doi.org/10.1016/j.jer.2024.05.002
[research_shi_chang_2018]: https://doi.org/10.1016/j.actaastro.2018.09.015
[research_shi_chang_2019]: https://doi.org/10.1016/j.ast.2018.11.016
[research_shi_chang_2019_b]: https://doi.org/10.1016/j.ast.2019.02.022
[research_shifeng_jiamin_2018]: https://doi.org/10.1515/htmp-2017-0145
[research_shimabukuro_welge_1982]: https://doi.org/10.2514/3.57423
[research_shimabukurokm_welgehr_1979]: https://ntrs.nasa.gov/citations/19790067234
[research_shimada_ohwada_2020]: https://doi.org/10.1186/s42774-020-00037-8
[research_shindos_jopparg_1980]: https://ntrs.nasa.gov/citations/19810016502
[research_shiriaev_freidovich_2026]: https://doi.org/10.1016/j.sysconle.2026.106510
[research_shirinzadehdastgiri_fuerth_2023]: https://doi.org/10.1038/s41598-023-40527-5
[research_shiryaev_maysak_2023]: https://doi.org/10.1051/e3sconf/202338305009
[research_shiryaev_serebryansky_2022]: https://doi.org/10.1109/mlsd55143.2022.9934688
[research_shkaraputa_1976]: https://doi.org/10.1007/bf01533037
[research_shoshanytavory_peleg_2023]: https://doi.org/10.1002/sys.21688
[research_shu_gao_2025]: https://doi.org/10.1063/5.0279923
[research_shucheng_xijun_1994]: https://doi.org/10.21236/ada289590
[research_shufan_heng_2018]: https://doi.org/10.1051/matecconf/201817903015
[research_shulman_parry_1966]: https://doi.org/10.1121/1.1942873
[research_shvedchenko_2009]: https://doi.org/10.1615/tsagiscij.v40.i5.60
[research_shvedchenko_2010]: https://doi.org/10.1615/tsagiscij.v41.i6.30
[research_si_huang_2019]: https://doi.org/10.1063/1.5098543
[research_siano_2014]: https://doi.org/10.1524/9783110348231.351
[research_sibulkin_1951]: https://ntrs.nasa.gov/citations/19930086494
[research_siedlak_pinon_2017]: https://doi.org/10.1007/s00163-017-0269-0
[research_sih_chou_1989]: https://doi.org/10.1016/0167-8442(89)90012-8
[research_silton_fresconi_2014]: https://doi.org/10.21236/ada611082
[research_silversteinabe_whitejamesa_1937]: https://ntrs.nasa.gov/citations/19930091622
[research_sinaiskii_pogrebnyak_1972]: https://doi.org/10.1007/bf01527569
[research_singh_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1050
[research_sinha_singh_2026]: https://doi.org/10.5937/fme2602380s
[research_sitaram_govardhan_2023]: https://doi.org/10.61653/joast.v67i3.2015.385
[research_sivaramakrishnan_1981]: https://doi.org/10.2514/3.57591
[research_skoogrichardb_1951]: https://ntrs.nasa.gov/citations/19930086551
[research_skow_moore_1982]: https://doi.org/10.2514/3.61562
[research_slater]: https://ntrs.nasa.gov/citations/20220009243
[research_slater_2019]: https://ntrs.nasa.gov/citations/20190004939
[research_slater_2020]: https://doi.org/10.2514/6.2020-2090
[research_slater_2023]: https://doi.org/10.2514/6.2023-4016
[research_slater_2024]: https://ntrs.nasa.gov/citations/20240008586
[research_slater_b]: https://ntrs.nasa.gov/citations/20240007797
[research_slaterjohnw_2011]: https://ntrs.nasa.gov/citations/20110011374
[research_slaterjohnw_2014]: https://ntrs.nasa.gov/citations/20140016826
[research_slaterjohnw_2015]: https://ntrs.nasa.gov/citations/20150021040
[research_slaterjohnw_2016]: https://ntrs.nasa.gov/citations/20160010068
[research_slaterjohnw_2017]: https://ntrs.nasa.gov/citations/20170008734
[research_sleemanwilliamc_byrnesandrewl_1953]: https://ntrs.nasa.gov/citations/20090023635
[research_sleemanwilliamcjr_1957]: https://ntrs.nasa.gov/citations/20050019253
[research_sleemanwilliamcjr_1961]: https://ntrs.nasa.gov/citations/20040047139
[research_smartmichaelk_kalkhoranirajm_1994]: https://ntrs.nasa.gov/citations/19970001786
[research_smeltzerdb_sorensenne_1972]: https://ntrs.nasa.gov/citations/19730005050
[research_smith_1967]: https://doi.org/10.21236/ad0655370
[research_smith_2021]: https://doi.org/10.1063/pt.3.4888
[research_smith_burgess_1960]: https://doi.org/10.4271/600405
[research_smith_jones_1976]: https://ntrs.nasa.gov/citations/19760015098
[research_smith_mead_1984]: https://ntrs.nasa.gov/citations/19850002745
[research_smith_scribben_2007]: https://doi.org/10.21236/ada470860
[research_smith_yamakawa_1979]: https://doi.org/10.21236/ada069827
[research_smithwilliardg_1954]: https://ntrs.nasa.gov/citations/20090025453
[research_snodgrass_1955]: https://doi.org/10.2514/8.6860
[research_sobester_2021]: https://doi.org/10.2514/1.c036180
[research_soederrh_bobulaga_1979]: https://ntrs.nasa.gov/citations/19790022016
[research_soederrh_bobulaga_1979_b]: https://ntrs.nasa.gov/citations/19790015798
[research_soederrh_bobulaga_1982]: https://ntrs.nasa.gov/citations/19830007035
[research_soederrh_mehaliccm_1984]: https://ntrs.nasa.gov/citations/19850001760
[research_sogukpinar_2018]: https://doi.org/10.1063/1.5025956
[research_solomongeorgee_1955]: https://ntrs.nasa.gov/citations/19930090996
[research_soltani_askari_2019]: https://doi.org/10.1016/j.ast.2019.05.045
[research_soltani_daliri_2016]: https://doi.org/10.2514/1.b36162
[research_soltani_farahani_2011]: https://doi.org/10.1016/j.scient.2011.03.019
[research_soltani_younsi_2015]: https://doi.org/10.2514/1.b35461
[research_song_kim_2019]: https://doi.org/10.31399/asm.fach.v03.c9001757
[research_song_zhang_2019]: https://doi.org/10.1115/1.4041699
[research_sonoda_olhofer_2009]: https://doi.org/10.1115/gt2009-59926
[research_sorensen_bencze_1974]: https://doi.org/10.2514/3.59241
[research_sorensen_latham_1975]: https://doi.org/10.2514/3.44491
[research_sorensen_smeltzer_1969]: https://doi.org/10.2514/3.44033
[research_sorensen_smeltzer_1972]: https://doi.org/10.2514/3.59067
[research_sorensen_smeltzer_1973]: https://doi.org/10.2514/3.44367
[research_sorensenne_benczedp_1973]: https://ntrs.nasa.gov/citations/19740028534
[research_sorrells_towne_1984]: https://doi.org/10.2514/6.1984-615
[research_sosnin_torshenov_1970]: https://doi.org/10.1007/bf01527239
[research_sousa_paniagua_2017]: https://doi.org/10.1016/j.compfluid.2017.03.005
[research_sovran_1959]: https://doi.org/10.1115/1.4007999
[research_sowers_stueber]: https://ntrs.nasa.gov/citations/20260002615
[research_sowers_stueber_2025]: https://ntrs.nasa.gov/citations/20240013421
[research_sowter_1973]: https://doi.org/10.1017/s0001924000040677
[research_spearman_1983]: https://ntrs.nasa.gov/citations/19830013886
[research_spearman_1984]: https://doi.org/10.2514/6.1984-2503
[research_spearman_fournier_1977]: https://ntrs.nasa.gov/citations/19770060336
[research_spearmanml_sawyerwc_1977]: https://ntrs.nasa.gov/citations/19780034893
[research_spencerbernardjr_1961]: https://ntrs.nasa.gov/citations/19980228059
[research_spoonerstanleyh_martinaalbertp_1948]: https://ntrs.nasa.gov/citations/19930085375
[research_spreemannkennethp_1958]: https://ntrs.nasa.gov/citations/19930085045
[research_spreiter_sacks_1951]: https://doi.org/10.2514/8.1830
[research_squires_2002]: https://doi.org/10.21236/ada410100
[research_squires_2004]: https://doi.org/10.21236/ada427305
[research_sreekumar_vamsikrishna_2025]: https://doi.org/10.2514/1.a35907
[research_srivastav_ponnani_2011]: https://doi.org/10.1115/imece2011-63381
[research_srivatsan_1999]: https://doi.org/10.1016/s0142-1123(99)00012-2
[research_srivatsan_anand_1998]: https://doi.org/10.1115/imece1998-1139
[research_stamatelos_labeas_2025]: https://doi.org/10.3390/aerospace12080726
[research_stancil_1979]: https://doi.org/10.2514/3.58481
[research_stanisic_1961]: https://doi.org/10.1002/zamm.19610410903
[research_stanley_1980]: https://doi.org/10.2514/6.1980-1867
[research_starken_lichtfuss_1970]: https://doi.org/10.1115/1.3445351
[research_staubyn_2015]: https://doi.org/10.21236/ada626008
[research_steenkenwg_williamsjg_1999]: https://ntrs.nasa.gov/citations/19990024943
[research_steer_2003]: https://doi.org/10.2514/6.2003-5308
[research_stenning_1980]: https://doi.org/10.1115/1.3240630
[research_stenning_1980_b]: https://doi.org/10.1115/1.3240618
[research_stephan_heyen_2024]: https://doi.org/10.2514/1.c037632
[research_stephensemilyw_1959]: https://ntrs.nasa.gov/citations/19980232232
[research_stephenson_1953]: https://doi.org/10.2514/8.2736
[research_stephenson_1958]: https://doi.org/10.1017/s0368393100068395
[research_sterbentzwilliamh_davidsjoseph_1952]: https://ntrs.nasa.gov/citations/20090016318
[research_stewart_1956]: https://doi.org/10.2514/8.3590
[research_stewartson_1950]: https://doi.org/10.1017/s0305004100025779
[research_stickley_brownhill_1964]: https://doi.org/10.21236/ad0602083
[research_stjohn_frederick_2013]: https://ntrs.nasa.gov/citations/20140000927
[research_stocker_1951]: https://doi.org/10.1017/s0001925900000548
[research_stone_1945]: https://doi.org/10.21236/ada801302
[research_straightdm_harringtonde_1973]: https://ntrs.nasa.gov/citations/19730017096
[research_strub_suter_1965]: https://doi.org/10.1115/1.3678166
[research_stubbs_1956]: https://doi.org/10.4271/560075
[research_studer_2012]: https://doi.org/10.1055/s-0032-1329915
[research_sturek_kayser_1983]: https://doi.org/10.21236/ada134992
[research_sturek_kayser_1983_b]: https://doi.org/10.21236/ada128036
[research_su_qu_2023]: https://doi.org/10.1002/adem.202300095
[research_su_young_2017]: https://doi.org/10.1002/cepa.334
[research_subramanian_delaurentis_2016]: https://doi.org/10.1002/sys.21358
[research_suchocki_lampart_2015]: https://doi.org/10.1515/eng-2015-0053
[research_sugiyama_1971]: https://doi.org/10.1299/jsme1958.14.1077
[research_sugiyama_1971_b]: https://doi.org/10.1299/kikai1938.37.295
[research_sugiyama_1977]: https://doi.org/10.1299/jsme1958.20.711
[research_sullivan_2002]: https://doi.org/10.21236/ada428867
[research_sullivanpg_1978]: https://ntrs.nasa.gov/citations/19790008753
[research_sun_ding_2026]: https://doi.org/10.1360/sst-2025-0362
[research_sun_gu_2021]: https://doi.org/10.1177/09596518211057423
[research_sun_gu_2024]: https://doi.org/10.1016/j.cja.2024.01.036
[research_sun_gu_2024_b]: https://doi.org/10.1007/s11630-024-1961-9
[research_sun_hu_2024]: https://doi.org/10.2514/1.j063397
[research_sun_li_2021]: https://doi.org/10.1115/1.4051782
[research_sun_li_2021_b]: https://doi.org/10.1016/j.ast.2021.106793
[research_sun_li_2022]: https://doi.org/10.1007/s11630-022-1547-3
[research_sun_miao_2015]: https://doi.org/10.1515/tjj-2015-0036
[research_sun_nie_2015]: https://doi.org/10.1115/1.4031775
[research_sun_shen_2025]: https://doi.org/10.1016/j.ast.2025.110457
[research_sun_smith_2019]: https://doi.org/10.1016/j.ast.2019.105387
[research_sun_yang_2020]: https://doi.org/10.12783/dtcse/cmso2019/33628
[research_sun_yang_2024]: https://doi.org/10.1063/5.0243466
[research_sun_yang_2025]: https://doi.org/10.3724/j.gter.20250021
[research_sun_yu_2025]: https://doi.org/10.1063/5.0257367
[research_sun_zhang_2016]: https://doi.org/10.2322/tjsass.59.349
[research_sun_zhang_2024]: https://doi.org/10.2514/1.j064672
[research_sun_zheng_2025]: https://doi.org/10.1016/j.ast.2025.110574
[research_sun_zhu_2019]: https://doi.org/10.1063/1.5083820
[research_sunderroy_karnick_2022]: https://doi.org/10.2514/6.2022-4049
[research_supersonic_flight_2014]: https://doi.org/10.2307/j.ctv15wxpxz.9
[research_surber_1975]: https://doi.org/10.2514/6.1975-1183
[research_surber_robinson_1983]: https://doi.org/10.2514/6.1983-1164
[research_surber_sedlock_1979]: https://doi.org/10.2514/3.58575
[research_surwase_kumar_2025]: https://doi.org/10.1186/s44147-025-00749-y
[research_sussman_1968]: https://doi.org/10.2514/3.43914
[research_suttonfredb_1959]: https://ntrs.nasa.gov/citations/19980230678
[research_sweep_optimization_2024]: https://doi.org/10.47176/jafm.17.12.2773
[research_swortzel_barfield_1976]: https://doi.org/10.2514/6.1976-889
[research_syberg_koncsek_1976]: https://doi.org/10.2514/3.58712
[research_syberg_paynter_1981]: https://doi.org/10.2514/6.1981-1598
[research_sybergj_koncsekjl_1972]: https://ntrs.nasa.gov/citations/19730028643
[research_szusta_2018]: https://doi.org/10.1016/j.ijfatigue.2018.05.025
[research_tabanli_yuceil_2021]: https://doi.org/10.2514/1.b38069
[research_tadini_grange_2017]: https://doi.org/10.1016/j.ast.2017.02.011
[research_taghavizenouz_ababafbehbaha_2017]: https://doi.org/10.5139/ijass.2017.18.1.91
[research_taghiabad_esfandabadi_2026]: https://doi.org/10.1016/j.ast.2025.110963
[research_taguchi_mori_2017]: https://doi.org/10.1155/2017/7287586
[research_taig_1961]: https://doi.org/10.1108/eb033408
[research_takahashi_2012]: https://doi.org/10.2514/6.2012-5704
[research_takahashi_2017]: https://doi.org/10.1299/jfst.2017jfst0026
[research_takovitskii_2020]: https://doi.org/10.2514/6.2020-3120
[research_takovitsky_2018]: https://doi.org/10.31857/s003282350002741-5
[research_tamboli_1956]: https://doi.org/10.1017/s0001925900010313
[research_tamrat_1988]: https://doi.org/10.2514/6.1988-4400
[research_tanaka_murata_1975]: https://doi.org/10.1299/jsme1958.18.1277
[research_tanaka_murata_1975_b]: https://doi.org/10.1299/kikai1938.41.863
[research_tanaka_murata_1975_c]: https://doi.org/10.1299/jsme1958.18.256
[research_tanaka_nojima_1971]: https://doi.org/10.2472/jsms.20.418
[research_tanchoonsooi_suderkenneth_2003]: https://ntrs.nasa.gov/citations/20030067316
[research_tang_cai_2025]: https://doi.org/10.1063/5.0297492
[research_tang_cai_2025_b]: https://doi.org/10.1063/5.0277814
[research_tang_li_2025]: https://doi.org/10.1063/5.0256817
[research_tang_xu_2024]: https://doi.org/10.1017/jfm.2024.641
[research_tanguy_macmanus_2018]: https://doi.org/10.1016/j.ast.2018.04.031
[research_tani_1978]: https://doi.org/10.1115/1.3424390
[research_tanida_1972]: https://doi.org/10.1007/bf01593986
[research_tao_jin_2022]: https://doi.org/10.1177/09544062221115346
[research_tao_sun_2019]: https://doi.org/10.1016/j.ast.2019.07.002
[research_tao_sun_2020]: https://doi.org/10.1016/j.cja.2020.01.015
[research_tao_wang_2024]: https://doi.org/10.3390/coatings14080960
[research_tate_gillard_1975]: https://doi.org/10.21236/ada018691
[research_taufikbudicahyana_achmadwardana_2023]: https://doi.org/10.31572/inotera.vol8.iss1.2023.id196
[research_taylor_1968]: https://doi.org/10.1017/s0001924000084347
[research_taylorjohng_1991]: https://ntrs.nasa.gov/citations/19910004962
[research_teschwa_steenkenwg_1978]: https://ntrs.nasa.gov/citations/19780025160
[research_tewfik_giedt_1960]: https://doi.org/10.2514/8.8737
[research_tfaily_bartoli_2026]: https://doi.org/10.1007/s00158-025-04239-w
[research_tfaily_diouane_2024]: https://doi.org/10.1007/s00158-024-03833-8
[research_thankachan_2025]: https://doi.org/10.1080/09700161.2025.2604369
[research_thapa_li_2025]: https://doi.org/10.3390/machines13040338
[research_the_cutting_1998]: https://doi.org/10.7249/mr939
[research_the_fiat_1952]: https://doi.org/10.1108/eb032139
[research_the_hawker_1990]: https://doi.org/10.2514/6.1990-3238
[research_the_potez_1935]: https://doi.org/10.1108/eb029902
[research_the_reason_2021]: https://doi.org/10.47939/et.v2i5.121
[research_the_rollsroyce_1967]: https://doi.org/10.1108/eb034271
[research_the_rollsroyce_1968]: https://doi.org/10.1108/eb034361
[research_thein_2018]: https://doi.org/10.47119/ijrp10020112019483
[research_theodorsen_1959]: https://doi.org/10.2514/8.8239
[research_thomas_1942]: https://doi.org/10.21236/ad0494220
[research_thomas_1965]: https://doi.org/10.2514/3.3031
[research_thomas_won_1999]: https://ntrs.nasa.gov/citations/20000057268
[research_thomasrandy_stueberthomasj_2013]: https://ntrs.nasa.gov/citations/20140001129
[research_thrust_vectoring_2020]: https://doi.org/10.37896/jxu14.10/016
[research_tian_li_2020]: https://doi.org/10.1007/s00158-020-02589-1
[research_tian_shunke_2021]: https://doi.org/10.1080/09603409.2021.1897945
[research_tich_shaw_1987]: https://doi.org/10.2514/6.1987-1929
[research_tindell_1980]: https://doi.org/10.2514/6.1980-1105
[research_tindell_1981]: https://doi.org/10.2514/3.57584
[research_ting_chaparro_2018]: https://doi.org/10.2514/1.c034810
[research_tirpak_1985]: https://doi.org/10.21236/ada163487
[research_todorov_rakov_2023]: https://doi.org/10.3390/aerospace10030287
[research_toffol_ricci_2023]: https://doi.org/10.1016/j.compstruct.2022.116557
[research_tollthomasa_1942]: https://ntrs.nasa.gov/citations/19930092608
[research_tomczak_2026]: https://doi.org/10.21741/9781644904251-111
[research_tomczyk_seweryn_2017]: https://doi.org/10.1016/j.ijfatigue.2017.06.037
[research_tomczyk_seweryn_2021]: https://doi.org/10.3390/ma14020404
[research_tondl_1979]: https://doi.org/10.1016/0020-7462(79)90014-3
[research_tongguang_changhui_2015]: https://doi.org/10.1016/j.proeng.2014.12.581
[research_torenbeek_1971]: https://doi.org/10.1108/eb034787
[research_toric_glavinic_2018]: https://doi.org/10.1002/fam.2643
[research_toro_myrabo_1999]: https://doi.org/10.2514/6.1999-2843
[research_transonic_and_1992]: https://doi.org/10.1017/cbo9780511607134.012
[research_trefny_hirt_2014]: https://ntrs.nasa.gov/citations/20140011175
[research_trefnycj_bensontj_1995]: https://ntrs.nasa.gov/citations/19960016375
[research_trefnycj_wasserbauerjw_1986]: https://ntrs.nasa.gov/citations/19860015223
[research_triplett_1980]: https://doi.org/10.2514/3.57932
[research_tritschler_juhasz_2025]: https://doi.org/10.2514/1.c037763
[research_tudosie_2017]: https://doi.org/10.19062/2247-3173.2017.19.1.26
[research_tudosie_2017_b]: https://doi.org/10.19062/1842-9238.2017.15.1.16
[research_tudosie_2018]: https://doi.org/10.19062/2247-3173.2018.20.33
[research_tudosie_2024]: https://doi.org/10.1109/iccc62069.2024.10569513
[research_tudosie_dumitru_2019]: https://doi.org/10.19062/2247-3173.2019.21.27
[research_tudosie_paunescu_2017]: https://doi.org/10.19062/2247-3173.2017.19.1.27
[research_tudosie_prisacariu_2022]: https://doi.org/10.19062/2247-3173.2021.22.19
[research_tuninetti_sepulveda_2024]: https://doi.org/10.3390/aerospace11040285
[research_turkkahraman_ozcan_2024]: https://doi.org/10.2339/politeknik.1247300
[research_turn_performance_2021]: https://doi.org/10.2514/5.9781624105920.0623.0676
[research_turning_flight_1997]: https://doi.org/10.2514/5.9781600861529.0129.0139
[research_turning_flights_1995]: https://doi.org/10.2514/5.9781600868535.0293.0312
[research_turning_performance_1992]: https://doi.org/10.1017/cbo9780511607134.010
[research_tyan_nguyen_2017]: https://doi.org/10.2514/1.c033833
[research_uddin_gravdahl_2016]: https://doi.org/10.1016/j.ifacol.2016.07.323
[research_uemura_kamata_2020]: https://doi.org/10.1515/htmp-2020-0039
[research_uludag_turan_2015]: https://doi.org/10.7763/ijmmm.2015.v3.176
[research_um_2016]: https://doi.org/10.14731/kjir.2016.03.56.1.111
[research_unal_oz_2023]: https://doi.org/10.1108/aeat-02-2022-0056
[research_urans_simulation_2024]: https://doi.org/10.47176/jafm.17.05.2121
[research_using_tip_2022]: https://doi.org/10.47176/jafm.15.06.1089
[research_uthgenannt_1971]: https://doi.org/10.2514/3.59180
[research_utomo_bura_2019]: https://doi.org/10.23960/ins.v2i2.90
[research_vacarios_ceronmunoz_2025]: https://doi.org/10.1016/j.ast.2025.110135
[research_vaisakh_namratha_2019]: https://doi.org/10.1007/s00193-019-00929-9
[research_valencia_alulema_2020]: https://doi.org/10.1016/j.tsep.2020.100515
[research_valencia_hidalgo_2017]: https://doi.org/10.1016/j.cja.2016.12.005
[research_valensi_1958]: https://doi.org/10.2514/8.7478
[research_valoppi_bruschi_2017]: https://doi.org/10.1016/j.ijmecsci.2017.02.005
[research_vancefdippoldiii_2022]: https://ntrs.nasa.gov/citations/20220010443
[research_vandeusen_mardoc_1972]: https://doi.org/10.2514/3.58933
[research_vandommelen_1995]: https://doi.org/10.21236/ada329654
[research_vanes_2002]: https://doi.org/10.2514/2.2997
[research_vanschalkwykchristian_brightmichellem_2001]: https://ntrs.nasa.gov/citations/20050196613
[research_vasilev_1970]: https://doi.org/10.1007/bf01014997
[research_veereshkumar_nagasailaja_2021]: https://doi.org/10.21275/sr21713140558
[research_venturelli_benini_2016]: https://doi.org/10.1016/j.ast.2016.08.021
[research_veresnikov_2025]: https://doi.org/10.17587/it.31.451-464
[research_veresnikov_goncharenko_2026]: https://doi.org/10.1134/s1064562426700055
[research_verma_kulkarni_2024]: https://doi.org/10.1088/2631-8695/ad937d
[research_verma_manisankar_2025]: https://doi.org/10.2514/1.j065217
[research_verma_singh_2020]: https://doi.org/10.1177/0954410020909190
[research_vidal_1962]: https://doi.org/10.2514/8.9698
[research_vieira_soltz_2025]: https://doi.org/10.29327/9786527220794.1443119
[research_vinogradov_makarov_2017]: https://doi.org/10.1615/tsagiscij.2017022808
[research_vinogradov_melnikov_2017]: https://doi.org/10.1615/tsagiscij.2017021109
[research_viranr_fandn_1982]: https://ntrs.nasa.gov/citations/19820049585
[research_vitols_threadgill_2026]: https://doi.org/10.1007/s00348-026-04224-z
[research_vondoenhoffalberte_hortonelmera_1942]: https://ntrs.nasa.gov/citations/19930092757
[research_vonhlatky_rice_2018]: https://doi.org/10.1080/14702436.2017.1417736
[research_vorobev_bich_1977]: https://doi.org/10.1007/bf01528583
[research_vorobev_galiakhmetov_2023]: https://doi.org/10.3103/s1068798x23070389
[research_voss_klimmek_2023]: https://doi.org/10.1016/j.ast.2023.108231
[research_vu_nguyen_2025]: https://doi.org/10.1088/2631-8695/adffff
[research_wabick_johnson_2023]: https://doi.org/10.1017/jfm.2023.34
[research_wages_1971]: https://doi.org/10.2514/6.1971-762
[research_walker_1955]: https://doi.org/10.1017/s036839310011689x
[research_walker_fletcher_2005]: https://doi.org/10.2514/6.2005-4935
[research_walkerharoldj_berggrenroberte_1948]: https://ntrs.nasa.gov/citations/19930090356
[research_walkley_1986]: https://doi.org/10.2514/6.1986-2627
[research_wallnerle_lubickrj_1955]: https://ntrs.nasa.gov/citations/20090023603
[research_wallnerlewise_lubickrobertj_1954]: https://ntrs.nasa.gov/citations/20090021949
[research_wallskog_1954]: https://ntrs.nasa.gov/citations/20090022754
[research_wallskog_1954_b]: https://ntrs.nasa.gov/citations/20090023601
[research_wan_guo_2007]: https://doi.org/10.1016/s1000-9361(07)60048-x
[research_wang_chen_2017]: https://doi.org/10.1115/gt2017-63427
[research_wang_chen_2025_b]: https://doi.org/10.1063/5.0268520
[research_wang_fan_2024]: https://doi.org/10.1007/s42405-024-00710-y
[research_wang_fang_2024]: https://doi.org/10.1115/1.4064512
[research_wang_gao_2023]: https://doi.org/10.3390/pr11102880
[research_wang_guan_2026]: https://doi.org/10.1063/5.0316018
[research_wang_guo_2017]: https://doi.org/10.1016/j.cja.2017.03.004
[research_wang_he_2024]: https://doi.org/10.3389/fenrg.2023.1259729
[research_wang_he_2025]: https://doi.org/10.1371/journal.pone.0328630
[research_wang_hu_2020]: https://doi.org/10.1177/0036850420940920
[research_wang_hu_2021]: https://doi.org/10.1115/1.4049382
[research_wang_li_2025]: https://doi.org/10.3390/aerospace12090846
[research_wang_liu_2018]: https://doi.org/10.3390/ma11071158
[research_wang_liu_2024]: https://doi.org/10.1016/j.ast.2024.108947
[research_wang_liu_2025]: https://doi.org/10.1080/01457632.2025.2571269
[research_wang_lu_2020]: https://doi.org/10.1016/j.ast.2020.105979
[research_wang_ma_2021]: https://doi.org/10.2514/1.c035687
[research_wang_pan_2023]: https://doi.org/10.1016/j.applthermaleng.2023.120275
[research_wang_pan_2024]: https://doi.org/10.1016/j.applthermaleng.2023.122324
[research_wang_song_2022]: https://doi.org/10.3390/pr11010069
[research_wang_song_2026]: https://doi.org/10.2139/ssrn.7560478
[research_wang_sun_2023]: https://doi.org/10.1515/tjj-2023-0030
[research_wang_sun_2023_b]: https://doi.org/10.2514/1.j062300
[research_wang_tang_2025]: https://doi.org/10.1088/1742-6596/3041/1/012024
[research_wang_tian_2015]: https://doi.org/10.1061/(asce)as.1943-5525.0000480
[research_wang_trapp_1958]: https://doi.org/10.21236/ada290447
[research_wang_wang_2013]: https://doi.org/10.1007/978-3-642-38391-5_125
[research_wang_wang_2013_b]: https://doi.org/10.4028/www.scientific.net/amr.753-755.1534
[research_wang_wang_2020]: https://doi.org/10.1016/j.ast.2019.105534
[research_wang_wang_2023]: https://doi.org/10.3390/aerospace10080729
[research_wang_wang_2023_b]: https://doi.org/10.1017/aer.2023.19
[research_wang_wang_2024]: https://doi.org/10.1038/s41598-024-61900-y
[research_wang_xu_2023]: https://doi.org/10.1007/s00158-023-03635-4
[research_wang_yuan_2026]: https://doi.org/10.3390/aerospace13030252
[research_wang_zhang_2025]: https://doi.org/10.1088/1742-6596/3041/1/012007
[research_wang_zhang_2026]: https://doi.org/10.1016/j.ast.2025.110951
[research_wang_zhao_2021]: https://doi.org/10.3390/met11101630
[research_wang_zhao_2022]: https://doi.org/10.1016/j.ast.2022.107883
[research_wang_zhao_2023]: https://doi.org/10.1177/09544100231154055
[research_wang_zhao_2023_b]: https://doi.org/10.1016/j.ast.2023.108420
[research_wang_zhao_2025]: https://doi.org/10.1016/j.eswa.2025.126782
[research_wang_zhao_2025_b]: https://doi.org/10.1016/j.ast.2024.109886
[research_wang_zhao_2026]: https://doi.org/10.1016/j.measurement.2026.122215
[research_wang_zhao_2026_b]: https://doi.org/10.1016/j.measurement.2026.123286
[research_ward_1949]: https://doi.org/10.1017/s0001925900000056
[research_ward_1968]: https://doi.org/10.2514/3.43928
[research_ward_1989]: https://doi.org/10.2514/6.1989-2074
[research_wardana_cahyana_2022]: https://doi.org/10.37868/dss.v3.id195
[research_washington_pettis_1968]: https://doi.org/10.21236/ad0695658
[research_wasserbauer_meleason_1996]: https://ntrs.nasa.gov/citations/19960026650
[research_wasserbauer_willoh_1968]: https://doi.org/10.2514/6.1968-651
[research_wasserbauerjf_gerstenmaierwh_1978]: https://ntrs.nasa.gov/citations/19780019182
[research_wasserbauerjf_neumannhe_1985]: https://ntrs.nasa.gov/citations/19850016950
[research_wasserman_1952]: https://doi.org/10.21236/ad0015929
[research_watanabe_houpt_2019]: https://doi.org/10.3390/aerospace6030035
[research_watanabe_leonov_2019]: https://doi.org/10.2514/6.2019-1348
[research_watanabe_sunada_2023]: https://doi.org/10.2514/1.c036649
[research_watkins_2019]: https://doi.org/10.1080/14751798.2019.1640419
[research_watsonearlc_1953]: https://ntrs.nasa.gov/citations/19930087828
[research_weeks_1986]: https://doi.org/10.2514/6.1986-2613
[research_wegener_1977]: https://doi.org/10.21236/ada038280
[research_wei_qu_2022]: https://doi.org/10.3390/cryst12091255
[research_weirich_rueger_1999]: https://doi.org/10.2514/6.1999-941
[research_weiss_gegal_2014]: https://doi.org/10.2172/1131418
[research_weissman_1973]: https://doi.org/10.2514/3.60216
[research_wen_kong_2022]: https://doi.org/10.1016/j.msea.2022.143011
[research_wentz_1987]: https://doi.org/10.2514/6.1987-2474
[research_wernerrogera_wolterjohnd_2010]: https://ntrs.nasa.gov/citations/20100042397
[research_wetzelbentone_1955]: https://ntrs.nasa.gov/citations/19930088409
[research_whalenpaulp_wilcoxfreda_1956]: https://ntrs.nasa.gov/citations/19930089419
[research_whitcombrichardt_1953]: https://ntrs.nasa.gov/citations/20050019402
[research_whitcombrichardt_sevierjohnrjr_1960]: https://ntrs.nasa.gov/citations/19980223605
[research_white_1997]: https://doi.org/10.21236/ada330361
[research_white_wills_1972]: https://doi.org/10.21236/ad0758173
[research_whitford_1991]: https://doi.org/10.2514/3.46102
[research_whitford_1995]: https://doi.org/10.2514/6.1995-3920
[research_whittley_1952]: https://doi.org/10.1108/eb032129
[research_whoric_1973]: https://doi.org/10.21236/ad0914456
[research_whoric_1977]: https://doi.org/10.21236/ada038494
[research_wilcoxfreda_1957]: https://ntrs.nasa.gov/citations/19930089790
[research_wilde_pickerell_1968]: https://doi.org/10.1108/eb034344
[research_williams_butler_1963]: https://doi.org/10.1017/s0368393100078378
[research_williams_hunt_1980]: https://doi.org/10.2514/6.1980-1809
[research_williams_stevens_2006]: https://doi.org/10.2514/6.2006-3871
[research_williams_yost_1973]: https://doi.org/10.1017/s0001924000041610
[research_willis_1981]: https://doi.org/10.2514/3.57577
[research_wilson_figliola_2023]: https://doi.org/10.4271/01-16-02-0014
[research_wilson_riley_1993]: https://doi.org/10.21236/ada273685
[research_winkler_1954]: https://doi.org/10.21236/ad0058826
[research_winograd_miles_1956]: https://doi.org/10.1017/s0001925900010167
[research_wisniewski_1951]: https://doi.org/10.1108/eb032109
[research_woelk_1989]: https://doi.org/10.2514/6.1989-2123
[research_won_1990]: https://ntrs.nasa.gov/citations/19910008753
[research_wood_livingston_1971]: https://doi.org/10.21236/ada021266
[research_woodrm_millerds_1983]: https://ntrs.nasa.gov/citations/19830057466
[research_woodrm_millerds_1985]: https://ntrs.nasa.gov/citations/19850053430
[research_woodrm_millerds_1985_b]: https://ntrs.nasa.gov/citations/19850053429
[research_woodward_1956]: https://doi.org/10.1108/eb032671
[research_woollett_meleason_1974]: https://ntrs.nasa.gov/citations/19740023304
[research_wright_bruckman_1978]: https://doi.org/10.2514/3.58456
[research_wu_cao_2025]: https://doi.org/10.1063/5.0276108
[research_wu_du_2026]: https://doi.org/10.1016/j.ast.2026.111695
[research_wu_li_2024]: https://doi.org/10.3724/j.gter.20240004
[research_wu_li_2024_b]: https://doi.org/10.1186/s42774-024-00183-3
[research_wu_zhao_2022]: https://doi.org/10.1016/j.ast.2022.107500
[research_wuli_karlgeiselhart_2020]: https://ntrs.nasa.gov/citations/20205007182
[research_xiaokang_kuaishe_2018]: https://doi.org/10.1016/s1875-5372(18)30189-9
[research_xie_liu_2025]: https://doi.org/10.1016/j.ast.2025.110027
[research_xie_marrani_2021]: https://doi.org/10.1080/21642583.2021.1899999
[research_xie_ye_2025]: https://doi.org/10.1016/j.ast.2025.110396
[research_xie_ye_2025_b]: https://doi.org/10.1063/5.0294667
[research_xie_zhang_2016]: https://doi.org/10.1115/1.4034914
[research_xie_zhu_2023]: https://doi.org/10.1063/5.0185385
[research_xinguo_xing_2015]: https://doi.org/10.1016/j.proeng.2014.12.713
[research_xinqian_anxiong_2015]: https://doi.org/10.2514/1.b35448
[research_xu_2023]: https://doi.org/10.54254/2753-8818/18/20230256
[research_xu_cheng_2020]: https://doi.org/10.1155/2020/2739131
[research_xu_hu_2021]: https://doi.org/10.3390/en14238057
[research_xu_hu_2022]: https://doi.org/10.1007/s11630-022-1729-z
[research_xu_hu_2022_b]: https://doi.org/10.1177/09544100211063164
[research_xu_hu_2023]: https://doi.org/10.1061/jaeeez.aseng-4419
[research_xu_wu_2025]: https://doi.org/10.1016/j.ast.2025.110603
[research_xu_yu_2025]: https://doi.org/10.3390/aerospace13010017
[research_xue_li_2020]: https://doi.org/10.1007/s10338-020-00159-y
[research_xue_wang_2024]: https://doi.org/10.1115/1.4065631
[research_yadav_guven_2015]: https://doi.org/10.2514/1.a32605
[research_yaghmaee_roberts_1986]: https://doi.org/10.2514/6.1986-552
[research_yahiaoui_2024]: https://doi.org/10.1016/j.asr.2024.06.066
[research_yajnik_1977]: https://doi.org/10.2514/3.44605
[research_yajnik_subbaiah_1976]: https://doi.org/10.2514/3.44515
[research_yalcin_2017]: https://doi.org/10.1515/tjj-2015-0065
[research_yamaguchi_1964]: https://doi.org/10.1299/jsme1958.7.91
[research_yamamoto_kojima_2020]: https://doi.org/10.1016/j.ast.2019.105523
[research_yamamoto_ng_1997]: https://doi.org/10.1006/jsvi.1996.0763
[research_yamanaka_kamimura_1975]: https://doi.org/10.1299/jsme1958.18.689
[research_yamauchi_shibue_1988]: https://doi.org/10.1007/978-94-009-1373-8_34
[research_yamazaki_mizobata_2019]: https://doi.org/10.2322/tastj.17.127
[research_yan_chang_2024]: https://doi.org/10.1063/5.0208437
[research_yan_chen_2016]: https://doi.org/10.1007/s00193-016-0633-4
[research_yan_pan_2025]: https://doi.org/10.1063/5.0294481
[research_yang_ji_2021]: https://doi.org/10.3390/met11020303
[research_yang_kong_2026]: https://doi.org/10.1016/j.ast.2026.112146
[research_yang_lei_2011]: https://doi.org/10.4028/www.scientific.net/amr.383-390.4323
[research_yang_li_2021]: https://doi.org/10.1061/(asce)as.1943-5525.0001306
[research_yang_li_2026]: https://doi.org/10.2514/1.c038587
[research_yang_liang_2022]: https://doi.org/10.3390/ma16010280
[research_yang_liu_2017]: https://doi.org/10.1016/j.actaastro.2016.11.043
[research_yang_lu_2021]: https://doi.org/10.1115/1.4051403
[research_yang_lu_2022]: https://doi.org/10.1115/1.4055439
[research_yang_tian_2021]: https://doi.org/10.3389/fmats.2021.682831
[research_yang_wu_2022]: https://doi.org/10.1115/1.4053238
[research_yang_yu_2026]: https://doi.org/10.3390/aerospace13050399
[research_yao_zhang_2017]: https://doi.org/10.2514/1.j055627
[research_yao_zhang_2022]: https://doi.org/10.1115/1.4055214
[research_yaylak_pinarbasi_2026]: https://doi.org/10.64808/engineeringperspective.1905858
[research_yeh_1959]: https://doi.org/10.2514/8.8286
[research_yeom_sung_2015]: https://doi.org/10.5139/ijass.2015.16.2.165
[research_yi_sun_2024]: https://doi.org/10.54097/d39w6055
[research_yih_cermak_1952]: https://doi.org/10.21236/ad0009799
[research_yongxilyu_weiguozhang_2016]: https://doi.org/10.1109/cgncc.2016.7828957
[research_yonke_terrell_1985]: https://ntrs.nasa.gov/citations/19850057621
[research_yonkewilliama_robbendaniell_1995]: https://ntrs.nasa.gov/citations/19950065546
[research_york_ozturk_2018]: https://doi.org/10.2514/1.j057020
[research_yoshida_2009]: https://doi.org/10.1016/j.paerosci.2009.05.002
[research_you_yu_2016]: https://doi.org/10.5139/ijass.2016.17.2.260
[research_yu_guo_2025]: https://doi.org/10.1016/j.ijthermalsci.2025.109703
[research_yu_huang_2021]: https://doi.org/10.3390/aerospace8110340
[research_yu_ni_2021]: https://doi.org/10.1155/2021/8885074
[research_yu_wang_2025]: https://doi.org/10.1007/s12567-025-00672-1
[research_yu_yu_2026]: https://doi.org/10.1016/j.matchar.2026.116640
[research_yu_zhao_2026]: https://doi.org/10.1017/flo.2026.10052
[research_yuan_li_2023]: https://doi.org/10.1061/jaeeez.aseng-4249
[research_yuan_liu_2021]: https://doi.org/10.1016/j.ast.2021.107008
[research_yuan_lu_2026]: https://doi.org/10.1016/j.energy.2026.140460
[research_yuan_zhang_2021]: https://doi.org/10.1017/aer.2021.76
[research_yusof_rahim_2017]: https://doi.org/10.5539/ass.v13n4p37
[research_zachos_macmanus_2016]: https://doi.org/10.2514/1.j054904
[research_zahir_aamer_2023]: https://doi.org/10.1049/icp.2023.1963
[research_zaidi_1988]: https://doi.org/10.1016/0025-5416(88)90159-0
[research_zaman_korth_2025]: https://doi.org/10.1177/1475472x251382217
[research_zebbiche_youbi_2023]: https://doi.org/10.61653/joast.v58i3.2006.642
[research_zhang_2020]: https://doi.org/10.1007/978-981-15-0727-4_3
[research_zhang_2020_b]: https://doi.org/10.1007/978-981-15-0727-4_9
[research_zhang_2024]: https://doi.org/10.4208/cmaa.2024-0012
[research_zhang_an_2024]: https://doi.org/10.1063/5.0212250
[research_zhang_bo_2026]: https://doi.org/10.3390/aerospace13020191
[research_zhang_chen_2015]: https://doi.org/10.1016/j.cja.2015.06.015
[research_zhang_chen_2024]: https://doi.org/10.1016/j.flowmeasinst.2024.102629
[research_zhang_du_2021]: https://doi.org/10.1016/j.cja.2020.08.019
[research_zhang_hou_2015]: https://doi.org/10.1177/0954406215623978
[research_zhang_ji_2025]: https://doi.org/10.1016/j.ast.2025.110315
[research_zhang_li_2021]: https://doi.org/10.1007/s11630-021-1489-1
[research_zhang_liu_2024]: https://doi.org/10.1063/5.0235181
[research_zhang_lu_2022]: https://doi.org/10.1115/1.4050918
[research_zhang_malekgoudarzi_2020]: https://doi.org/10.1080/21642583.2020.1785970
[research_zhang_ning_2026]: https://doi.org/10.1016/j.ast.2026.113272
[research_zhang_stapelfeldt_2020]: https://doi.org/10.1016/j.ast.2019.105668
[research_zhang_tan_2015]: https://doi.org/10.2514/1.b35425
[research_zhang_tan_2018]: https://doi.org/10.2514/1.j056318
[research_zhang_vahdati_2018]: https://doi.org/10.1115/1.4041376
[research_zhang_vahdati_2019]: https://doi.org/10.1115/1.4045552
[research_zhang_wang_2022]: https://doi.org/10.2514/1.b37808
[research_zhang_wu_2026]: https://doi.org/10.3724/j.gter.20260008
[research_zhang_yang_2025]: https://doi.org/10.1017/aer.2025.10093
[research_zhang_yang_2026]: https://doi.org/10.1016/j.ast.2026.112109
[research_zhang_yu_2016]: https://doi.org/10.1016/j.ast.2016.09.006
[research_zhang_yuan_2020]: https://doi.org/10.1016/j.ast.2020.106182
[research_zhang_zhang_2024_b]: https://doi.org/10.1016/j.cja.2023.11.009
[research_zhang_zhang_2026]: https://doi.org/10.2139/ssrn.6641999
[research_zhang_zhou_2009]: https://doi.org/10.1109/icetc.2009.31
[research_zhao_jin_2023]: https://doi.org/10.3390/aerospace10030207
[research_zhao_jin_2025]: https://doi.org/10.1016/j.applthermaleng.2024.124869
[research_zhao_li_2025]: https://doi.org/10.1063/5.0260713
[research_zhao_sun_2017]: https://doi.org/10.1016/j.applthermaleng.2017.05.181
[research_zhao_vanhoorn_2022]: https://doi.org/10.3390/aerospace9080426
[research_zhao_zhou_2019]: https://doi.org/10.3390/s19224995
[research_zhao_zhou_2022]: https://doi.org/10.1108/aeat-09-2021-0270
[research_zheldubovskii_ishchenko_1982]: https://doi.org/10.1007/bf00776056
[research_zhipeng_chao_2015]: https://doi.org/10.1016/j.proeng.2014.12.584
[research_zhong_yu_2024]: https://doi.org/10.1016/j.jmrt.2024.04.072
[research_zhou_li_2019]: https://doi.org/10.1063/1.5095499
[research_zhu_chen_2018]: https://doi.org/10.1063/1.5005529
[research_zhu_gu_2022]: https://doi.org/10.1016/j.scib.2022.03.006
[research_zhu_lee_2018]: https://doi.org/10.1017/jfm.2018.646
[research_zhu_luo_2020]: https://doi.org/10.3390/en13082048
[research_zhu_yang_2020]: https://doi.org/10.1115/1.4046047
[research_zhu_zhao_2016]: https://doi.org/10.1016/j.applthermaleng.2016.06.013
[research_zhuang_lu_2015]: https://doi.org/10.1016/j.proeng.2015.11.195
[research_zien_ragsdale_1979]: https://doi.org/10.21236/ada073217
[research_zimmermanch_1935]: https://ntrs.nasa.gov/citations/19930081303
[research_zubair_ejaz_2022]: https://doi.org/10.4028/p-g44bm8
[research_zuo_2021]: https://doi.org/10.1016/j.actaastro.2021.06.010
[research_zuo_2023]: https://doi.org/10.2514/1.j062953
