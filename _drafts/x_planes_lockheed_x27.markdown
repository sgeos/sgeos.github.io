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

Three sections below answer the three halves of that, and two of the answers are negative.

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
namely to climb fast and go fast in a straight line. It has a wing of 196.1 square feet, a span of 21 feet
11 inches, and a thickness-to-chord ratio of 3.36 percent, with a leading edge sharp enough that ground
crews fitted protective covers over it. The aircraft was a superb interceptor and a poor fighter, and the
reason is in the geometry rather than in any failing of manufacture.

The [aspect ratio][ref_aspect_ratio] follows from the span and the area.

$$ A = \frac{b^2}{S} = \frac{(21.94\ \mathrm{ft})^2}{196.1\ \mathrm{ft}^2} = 2.455 $$

**That is a very low number for a wing meant to turn.** The wing loading is the other half of the problem.

$$ \frac{W}{S} = \frac{20{,}640\ \mathrm{lb}}{196.1\ \mathrm{ft}^2} = 105.3\ \mathrm{lb/ft}^2 $$

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
| Empty weight | 14,082 lb | 16,640 lb | +18.2 percent |
| Normal loaded | 20,640 lb | 24,385 lb | +18.1 percent |
| Maximum takeoff | 29,027 lb | 35,000 lb | +20.6 percent |
| Engine | J79-GE-11A turbojet | TF30-P-100 turbofan | a change of class |
| Thrust with afterburner | 15,600 lbf | 25,000 lbf | +60.3 percent |
| Wing loading | 105.3 lb/ft² | 81.3 lb/ft² | −22.8 percent |
| Thrust to weight | 0.756 | 1.025 | +35.6 percent |

**Four changes matter and the rest follow from them.**

**The wing grew by half and moved.** It went from a mid-set position to a shoulder position and moved aft,
while retaining the F-104's 10 degrees of [anhedral][ref_anhedral] and, importantly, its aerofoil section.

**The tail came down.** The F-104's [T-tail][ref_t_tail], with the horizontal surface on top of the fin, was
replaced by a conventional horizontal tail on the rear fuselage.

**The engine changed class.** The [J79][ref_j79] turbojet became the [TF30][ref_tf30] turbofan, and the
difference in physical envelope is not incidental.

| Engine | Length | Diameter | Dry weight | Airflow |
|---|---|---|---|---|
| J79-GE-17 | 208.69 in | 39.06 in | 3,835 lb | 170 lb/s |
| TF30-P-100 | 241.70 in | 48.90 in | 3,985 lb | 260 lb/s |
| Difference | +33.01 in | +9.84 in | +150 lb | +52.9 percent |

**The fuselage was stretched 30 inches**, which the record attributes to a 46 percent increase in internal
fuel. **The engine that had to go inside it is 33.01 inches longer than the one it replaced.** The article
notes that the stretch is within three inches of the engine length difference and declines to claim which
consideration drove it, because the record states only the fuel figure.

### The Intakes, Which Are the Article's Subject

**The F-104 uses fixed half-cone side inlets.** The CL-1200 replaced them with translating shock cones
having four inches of axial movement.
**The X-27, according to the record, was to have had intakes of rectangular form instead.**

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

The density follows from the equation of state rather than from the pressure directly, and the draft quotes
it without showing where it comes from.

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

The literature on supersonic flight conditions, atmospheric modelling and high-speed flight testing is
extensive.

- [MAGNETOHYDRODYNAMICS AND AERODYNAMIC HEATING][research_meyer_1938]
- [Deflections of a Supersonic Wing Due to Aerodynamic Heating][research_luce_jr_1949]
- [Design Charts for Transient Temperature Distribution...][research_kaye_yeh_1955]
- [Flight Measurements of Aerodynamic Heating and Boundary Layer...][research_snodgrass_1955]
- [The Structural Effects of Kinetic Heating in Supersonic Flight][research_walker_1955]
- [Effects of aerodynamic heating on X-15 temperatures][research_kinslermartinr_1958]
- [Free-Flight Investigation of a Rocket-Propelled Model to...][research_stephensemilyw_1959]
- [Magnetohydrodynamics and Aerodynamic Heating][research_meyer_1959]
- [Heat Transfer, Recovery Factor, and Pressure Distributions...][research_tewfik_giedt_1960]
- [Measurements of Aerodynamic Heat Transfer and Boundary-Layer...][research_rumseycharlesb_leedorothyb_1961]
- [THE THERMAL BEHAVIOR OF EXPLOSIVES SUBJECTED TO SIMULATED...][research_coleburn_drimmer_1961]
- [THE THERMAL BEHAVIOR OF EXPLOSIVES SUBJECTED TO SIMULATED...][research_coleburn_drimmer_1962]
- [AERODYNAMIC HEATING AND OTHER PARAMETERS AFFECTING SPACE...][research_gros_1963]
- [THE AERODYNAMIC HEATING OF A COMPOSITE FLAT PLATE][research_rand_1963]
- [THERMAL STRESS DETERMINATION TECHNIQUES FOR SUPERSONIC...][research_gellatly_gallagher_1964]
- [Re-Entry Module/Adapter Interconnect Fairing Aerodynamic...][research_sheldon_1967]
- [TIME RESPONSE AND AERODYNAMIC HEATING OF ATMOSPHERIC...][research_rubio_ballard_1967]
- [A Transducer for Controlling Simulated Aerodynamic Heating][research_alexander_1970]
- [Aerodynamic Heating of Supersonic Blunt Bodies][research_chou_smith_1974]
- [Experimental Heat Transfer Behavior of a Turbulent Boundary...][research_moffat_healzer_1978]
- [Aerodynamic Heating of Conventional Weapons][research_maples_1979]
- [Analysis of a Pyroceram Radome Subjected to Aerodynamic...][research_negaard_1979]
- [Base pressure and heat transfer tests of the 0.0225-scale...][research_foustjw_1979]
- [Predictions of Aerodynamic Heating on Tactical Missile Domes][research_zien_ragsdale_1979]
- [The Structure of a Boundary Layer on a Rough Wall with...][research_pimenta_moffat_1979]
- [Boundary-layer Trip Effectiveness and Computations of...][research_sturek_kayser_1983_b]
- [Computational Study of Swept-Fin Aerodynamic Heating for the...][research_sturek_kayser_1983]
- [Aerodynamic Heating Computations for Projectiles - Vol. 2...][research_strawn_kobayashi_1984_b]
- [Aerodynamic Heating Computations for Projectiles - Vol. 3 BRL...][research_beck_1984]
- [Aerodynamic Heating Computations for Projectiles. Volume 1...][research_kobayashi_1984]
- [Aerodynamic Heating Computations for Projectiles. Volume 2...][research_strawn_kobayashi_1984]
- [Aerodynamic Heating Computations for Projectiles. Volume 3...][research_beck_1984_b]
- [Kinetic Energy Finned Projectile Aerodynamic Heating...][research_schoeler_1987]
- [Thermal stress analysis of space shuttle orbiter subjected to...][research_kowilliaml_fieldsrogera_1987]
- [Laboratory Simulation of Kinetic Heating][research_horton_1954]
- [STAGNATION TEMPERATURE PROBES FOR USE AT HIGH SUPERSONIC...][research_winkler_1954]
- [Heat Transfer to Dry Ice Spheres Subjected to Supersonic Air...][research_brooke_1957]
- [Oblique Shock Relations for Air at Mach 7.8 and 7200 R...][research_nagamatsu_workman_1960]
- [Experimental Investigation at Mach Number 3.0 of the Effects...][research_dixonsidneyc_griffithgeorgee_1961]
- [COMPARISONS OF EXPERIMENTAL AND THEORETICAL HEAT TRANSFER TO...][research_pasiuk_1963]
- [Flow phenomena and convective heat transfer in a conical...][research_back_massier_1967]
- [THE FLOW FIELD AND HEAT TRANSFER DOWNSTREAM OF A REARWARD...][research_smith_1967]
- [Thrust Vector Control, Heat Transfer Modeling][research_leitner_1986]
- [Time dependent heat transfer rates in high Reynolds number...][research_flanaganmichaelj_1992]

### The Temperature the Skin Reaches

Air brought to rest against a surface gives up its kinetic energy as heat. The
[total temperature][ref_total_temperature] follows from energy conservation in a compressible flow.

$$ \frac{T_t}{T} = 1 + \frac{\gamma - 1}{2} M^2 $$

**A real surface does not recover all of it**, because the boundary layer conducts some heat away along the
surface as it converts the rest. The [recovery factor][ref_recovery_factor] accounts for that, and for a
turbulent boundary layer it is the cube root of the [Prandtl number][ref_prandtl].

$$ T_r = T\left(1 + r\,\frac{\gamma - 1}{2} M^2\right), \qquad r = \Pr^{1/3} \approx 0.896 $$

Evaluating at 35,000 feet gives the table the whole structural argument rests on.

| Mach | Speed | Total temperature | Recovery temperature | Yield retained by 2024-T81 |
|---|---|---|---|---|
| 1.00 | 663 mph | −10.6 °C | −15.1 °C | 100 percent |
| 2.00 | 1,327 mph | 120.7 °C | 102.5 °C | 94.7 percent |
| 2.20 | 1,459 mph | 157.5 °C | 135.5 °C | 91.5 percent |
| 2.50 | 1,658 mph | 219.2 °C | 190.8 °C | 77.2 percent |
| 2.56 | 1,698 mph | 232.5 °C | 202.7 °C | 72.8 percent |
| 2.60 | 1,725 mph | 241.5 °C | 210.8 °C | 68.8 percent |

The standard treatments of compressible flow used throughout this section are [Shapiro][book_shapiro] and
[Anderson][book_anderson], and the aerodynamic design context is [Kuchemann][book_kuchemann].

**The last column is a reading of published handbook curves for aluminium alloy after long exposure**,
interpolated linearly between tabulated points, and it is presented as a reading rather than as a law.

**The shape of that column is the finding.** At Mach 2.0, where the F-104 lived, the structure keeps 95
percent of its strength and the designer can ignore the problem. At Mach 2.6 it keeps 69 percent, and a wing
sized for a given load factor at full strength is a wing that no longer reaches it.

The literature on aerodynamic heating, elevated-temperature alloy behaviour, creep, and hot structures is
large and spans the whole period.

- [Aircraft Armor - Ballistic Characteristics of a Magnesium...][research_sullivan_1943]
- [Armor Plate, Metallurgical Examination of Laminated Aluminum...][research_riffin_1943]
- [Aluminum Alloy Armor][research_navalprovinggrounddahlgrenva_1945]
- [ELEVATED TEMPERATURE FATIGUE PROPERTIES OF SAE 4340 STEEL][research_trapp_1952]
- [Investigation of Compressive-Creep Properties of Aluminum...][research_carlson_schwope_1952]
- [FUNDAMENTAL DEFORMATION CHARACTERISTICS OF 80 NICKEL-20...][research_chang_nordheim_1953]
- [16 percent. Aluminium-iron alloy cold-rolled in the...][research_16_percent_1954]
- [Preliminary investigation of the compressive strength and...][research_mathausereldone_deveikiswilliamd_1955]
- [Investigation of the Compressive Strength and Creep Lifetime...][research_mathausereldone_deveikiswilliamd_1957]
- [MATERIAL - MAGNESIUM - ALUMINUM - ZINC - SACRIFICIAL ANODE...][research_hooper_whidden_1957]
- [Strength at Elevated Temperatures of Aluminium and Certain...][research_inglis_larke_1958]
- [Supersonic Aerodynamic Experiments Using Very High...][research_bloxsom_1958]
- [Complex Stress Creep Relaxation of Metallic Alloys at...][research_johnson_henderson_1959]
- [EFFECT OF HEATING ALUMINUM ALLOY WING STRUCTURE TO 325 F ON...][research_bergstedt_turner_1959]
- [Temperature dependence of the strength of zone hardened...][research_fine_1959]
- [Titanium - 6% Aluminum - 4% Vanadium Alloy Effects of Sponge...][research_croan_rizzitano_1959]
- [Complex Stress Creep Fracture of an Aluminium Alloy][research_johnson_henderson_1960]
- [RELATIONSHIP OF HOT HARDNESS TO ELEVATED TEMPERATURE...][research_glorioso_1960]
- [A STUDY OF THE SHORT TIME ELEVATED TEMPERATURE PROPERTIES OF...][research_mahorter_robertg_1961]
- [Aluminium Alloy Recrystallizing at Room Temperature][research_maeda_1961]
- [CATEGORY II HIGH TEMPERATURE EVALUATION OF A T-38 AIRCRAFT][research_sandstrom_white_1961]
- [Design Properties of Aluminium Alloys at Elevated Temperatures][research_taig_1961]
- [EFFECT OF CORROSION ON THE FATIGUE BEHAVIOR OF 2024-T4...][research_harmsworth_1961]
- [The Influence of Elevated Temperature on the Strength of...][research_finnie_1961]
- [The Low Temperature Specific Heat of an Aluminium-Manganese...][research_martin_1961]
- [A-356 TYPE ALUMINUM CASTING ALLOY. PART I. EFFECT OF...][research_bailey_1963]
- [EFFECTS OF ANTI-SEIZING COMPOUNDS AND LUBRICANTS ON HIGH...][research_mcdonnellaircraftcorpstlouismo_1963]
- [FRACTOGRAPHY. PART XI. EXAMINATION OF 7075 T-6 ALUMINUM ALLOY...][research_dahlberg_1963]
- [MECHANICAL PROPERTIES OF WELDED ALUMINUM MAGNESIUM ALLOY...][research_carosiello_1963]
- [STRESS CORROSION CRACKING OF HIGH STRENGTH NICKEL ALLOY...][research_hildebrand_1963]
- [INVESTIGATION INTO THE ELECTRICAL CONDUCTIVITY AND MECHANICAL...][research_allen_mahorter_1964]
- [MECHANICAL PROPERTIES OF STRESS-RELIEVED STRETCHED ALUMINUM...][research_stickley_brownhill_1964]
- [WELDING 214, 356, AND ALMAG 35 CAST ALUMINUM ALLOYS TO 5456...][research_orysh_betz_1964]
- [An Assessment of a Titanium Alloy for Supersonic Transport...][research_heimerlgeorgej_hardrathherbertf_1965]
- [Development of high strength, brazed aluminum, honeycomb...][research_kramerbe_potterdy_1966]
- [HIGH TEMPERATURE, LOW DENSITY BOUNDARY-LAYER CONTROL BY...][research_macdermott_dix_1966]
- [CORROSION-RESISTANT CLADDING FOR 7075-T6 ALUMINUM ALLOY][research_lowe_1967]
- [STRESS-CORROSION STUDIES OF ALUMINUM ALLOY 5456-H321 IN...][research_wacker_1967]
- [Short-time elevated temperature mechanical properties of...][research_montanojw_1967]
- [Strength of Metals under Impulsive Loading 1st Report, For...][research_nisiyama_tanimura_1967]
- [EVALUATION OF LOW COST ALUMINUM ALLOY GRANULES FOR USE IN...][research_hogge_1969]
- [Elevated-temperature sensitivity of �I437B alloy to cycle...][research_balashov_petukhov_1969]
- [Fracture properties of a high strength aluminium alloy/ Les...][research_radon_1969]
- [Titanium diffusion-bonded honeycomb - Optimum structure for...][research_kolom_1969]
- [Creep and fracture of ot-4 titanium alloy at constant...][research_sosnin_torshenov_1970]
- [INELASTIC DEFORMATION OF AN ALUMINUM ALLOY UNDER COMBINED...][research_brown_1970]
- [Rapid Heating and Loading of 7075 - T6 Aluminum Alloy Sheet][research_honeycutt_1970]
- [High-temperature creep and long-term creep strength of the...][research_krivenyuk_tsvilyuk_1971]
- [Room and elevated temperature properties of ball-milled...][research_kothari_1971]
- [The Effects of Temperature and Strain-Rate on the Strength of...][research_tanaka_nojima_1971]
- [An integrated evaluation on the mechanical strength of...][research_sato_kon_1972]
- [Elevated temperature ductility minimum in Hastelloy alloy X][research_arkoosh_fiore_1972]
- [Experimental study of L-96 brass and AMts aluminum alloy at...][research_yagn_kalko_1972]
- [Room and elevated temperature properties of ball-milled...][research_hansen_1972]
- [The influence of test temperature on the fatigue strength of...][research_sinaiskii_pogrebnyak_1972]
- [Titanium honeycomb structure][research_davisra_elrodsd_1972]
- [Engineering Design Data for Aluminum Alloy 7050-T73651 Plate][research_jones_1973]
- [Reply to comments on “room and elevated temperature...][research_kothari_1973]
- [The effect of different contact materials on the fretting...][research_wharton_waterhouse_1973]
- [Effect of quenching temperature on the nature of serrations...][research_thomas_srinivasan_1974]
- [Fabrication of angleply carbon-aluminum composites][research_novakrc_1974]
- [High temperature-high strength alloy glass fiber forming...][research_high_temperature_high_1974]
- [Titanium or titanium alloy clad aluminium or aluminium alloy...][research_titanium_or_1974]
- [Density fluctuations and radiated noise for a...][research_parthasarathysp_massierpf_1975]
- [Development of an Improved Elevated Temperature Aluminium...][research_development_of_1975]
- [New High Strength Aluminium Alloy][research_holl_1975]
- [Temperature Effect on the Mechanical Properties of Aluminum...][research_cervay_1975]
- [Temperature sensitivity of the yield strength of low-alloy...][research_malashenko_vashchilo_1975]
- [Effect of elevated temperature on the deformation of titanium...][research_shkaraputa_1976]
- [Effect of elevated temperature on the endurance of an alloy...][research_galkin_sergeev_1976]
- [Effect of the prolonged action of elevated temperatures on...][research_palienko_pogrebnyak_1976]
- [Effect of reinforcement with boron and silicon carbide...][research_maksimovich_karpinos_1977]
- [Ellipsometric Determination of Properties of Films on Rough...][research_reichert_brock_1977]
- [Real-time testing of titanium sheet and extrusion coupon...][research_lundet_1977]
- [Temperature-time relation in structural strengthening of D16...][research_vorobev_bich_1977]
- [Composite material comprising reinforced aluminium or...][research_composite_material_1978]
- [Effect of an Elevated Temperature High Humidity Environment...][research_haskins_1978]
- [Elevated temperature properties of boron/aluminum composites][research_sullivanpg_1978]
- [Mechanical Properties in Bending at Elevated Temperature of...][research_fox_fuchs_1978]
- [The Room Temperature and Elevated Temperature Fracture...][research_mills_1978]
- [Cast Titanium Compressor Casing][research_ficht_1979]
- [Penetration behaviour of a high-strength aluminium alloy][research_woodward_1979]
- [Reduced ductility of high-strength aluminium alloy during or...][research_hardie_holroyd_1979]
- [The elevated temperature strengths of alumina-aluminium and...][research_iseki_nicholas_1979]
- [Development of a Mechanically Alloyed Aluminum alloy for...][research_erich_1980]
- [Elevated Temperature Behavior of Metal- Matrix Composites][research_hashin_humphreys_1980]
- [Fracture Behavior of Boron Aluminum Composites at Room and...][research_awerbuch_1980]
- [Simultaneous Stress Relaxation in Tension and Creep in...][research_lai_findley_1980]
- [THE High Temperature oxidation of AISİL2CUNİ aluminium alloy][research_baykal_sarikaya_1980]
- [The effect of molybdenum ion implantation on the general and...][research_alsaffar_ashworth_1980]
- [Effect of temperature and strain rate on mechanisms and...][research_krashchenko_statsenko_1981]
- [Resistance of �I826 alloy to thermal cycling in a...][research_semenov_1981]
- [Strain-rate effects in the environmentally assisted fracture...][research_holroyd_hardie_1981]
- [Supersaturated Aluminum Alloy Powders][research_shechtman_1981]
- [Effect of low-temperature thermomechanical treatment on the...][research_demina_volkov_1982]
- [Fatigue resistance of heat-resistant alloy ÉI698VD under high...][research_zheldubovskii_ishchenko_1982]
- [Inelastic stress-responses of an aluminium alloy in...][research_ohashi_ohno_1982]
- [Synthesis and Properties of Elevated Temperature P/M Aluminum...][research_fine_weertman_1983]
- [A Fundamental Study of P/M Processed Elevated Temperature...][research_lawley_koczak_1984]
- [A Fundamental Study of P/M Processed Elevated Temperature...][research_lawley_koczak_1985]
- [Elevated Temperature Properties of Cast Aluminum Alloys...][research_tirpak_1985]
- [Weldability of 2519-T87 Aluminum Alloy][research_devletian_devincent_1988]
- [Titanium honeycomb panel testing][research_richardswl_thompsonrandolphc_1991]
- [MBE Grown Copper-Aluminum Alloy Films][research_kornreich_1992]
- [Process Zone Modeling of Elevated Temperature Structural...][research_white_1997]
- [Elevated Temperature Crack Growth Behavior in HSCT Structural...][research_saxenaashok_1998]
- [High-Strength Aluminum Casting Alloy for High-Temperature...][research_leeja_1998]
- [Demonstration and Validation of Trivalent Aluminum...][research_matzdorf_kane_1999]
- [Aluminum-Silicon Alloy Having Improved Properties at Elevated...][research_leejonathana_chenposhou_2002]
- [High Strength and Wear Resistant Aluminum Alloy for High...][research_leejonathana_munafopaulm_2002]
- [Microstructural Effect on Fatigue of 7075 Aluminum Alloy][research_lee_sanders_2002]
- [Sol-Gel Derived Surface Treatments for Aircraft Aluminum...][research_knobbe_2002]
- [Commercialization of NASA's High Strength Cast Aluminum Alloy...][research_leejonathana_2003]
- [Analysis of Erosion Transition in Tungsten-Alloy Rods into...][research_segletes_2004]
- [High Strength Aluminum Alloy For High Temperature Applications][research_jonathanalee_poshouchen_2005]
- [Aluminum Alloy 7068 Mechanical Characterization][research_minnicino_gray_2009]

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
| 30 s | 148.4 °C | 68.1 percent | 90.2 percent |
| 60 s | 190.9 °C | 89.9 percent | 77.2 percent |
| 120 s | 208.8 °C | 99.0 percent | 69.9 percent |
| 180 s | 210.6 °C | 99.9 percent | 68.9 percent |

#### The Heating Also Loads the Structure, Which Is a Separate Objection

**Losing yield strength is not the only thing high temperature does.** A skin that wants to expand and is
restrained by cooler structure behind it develops stress without any aerodynamic load at all.

Thermal stress, thermal buckling of heated panels, and the thermoelastic analysis of restrained structure
are a substantial period literature, driven by exactly the aircraft that were trying to fly faster than
aluminium comfortably allows.

- [Transient Thermal Stresses in Wings][research_parkes_1953]
- [A Conference on Thermal Stress][research_a_conference_1954]
- [The Problem of Thermal Stresses in Aircraft Structures][research_loveless_boswell_1954]
- [Wings Under Repeated Thermal Stress][research_parkes_1954]
- [STUDIES ON THERMAL STRESSES FOR AIRCRAFT STRUCTURES EXPOSED...][research_mahlmeister_ishimoto_1955]
- [SUBMICROSCOPIC STRUCTURE OF RABBIT CORNEA STUDIED BY...][research_kikkawa_1955]
- [Incremental Collapse Due to Thermal Stress][research_parkes_1956]
- [Panels under Thermal Stress][research_parkes_1956_b]
- [SIMILARITY LAWS REQUIRED FOR EXPERIMENTAL AERO-THERMOELASTIC...][research_calligeros_dugundji_1961]
- [Thermal Stresses in I‐section Beams][research_ayers_1962]
- [THERMAL STRESS ON CELLULAR STRUCTURE AND FUNCTION][research_buchsbaum_1963]
- [THERMOELASTICITY AND TEMPERATURE VARIATION OF UNPERTURBED...][research_nakajima_yanagawa_1963]
- [THERMAL STRESS ANALYSIS OF SANDWICH CYLINDERS][research_rivello_1965]
- [Temperature variation of unperturbed chain dimension of...][research_sakurada_nakajima_1965]
- [Thermal stress and instability of sandwich cylinders on rigid...][research_gellatly_bijlaard_1965]
- [STRESS REVIEWS. I. THERMAL STRESS - COLD][research_findikyan_duke_1966]
- [Thermal Buckling of a Circular Plate][research_mansfield_1967]
- [Thermoelasticity and the temperature coefficient of...][research_puett_1967]
- [Thermoelasticity and the Temperature Coefficient of...][research_puett_1968]
- [Low Temperature Effects and Generalized Thermoelasticity][research_fox_1969]
- [Some problems in thermoelasticity with temperature-dependent...][research_tang_1969]
- [Effect of Side-Chain Structure on Thermoelasticity of Acrylic...][research_cirlin_shen_1971]
- [Thermal Buckling of Rotating Orthotropic Annular Plates][research_uthgenannt_1971]
- [Stability of waves and shock structure in generalised...][research_beevers_1973]
- [Wave propagation in the two temperature theory of...][research_warren_chen_1973]
- [1554. Thermal regime and thermal stresses in bodies on...][research_1554_thermal_1974]
- [Thermal Buckling of Parallelogram Panels Subjected to Heating][research_matsumoto_sekiya_1975]
- [Calculation of temperature fields in problems of...][research_soltanov_1977]
- [Construction of the equations of thermoelasticity of a...][research_khoroshun_soltanov_1977]
- [A THEORY OF ANISOTROPIC THERMOELASTICITY AT LOW REFERENCE...][research_pao_banerjee_1978]
- [A UNIQUENESS THEOREM FOR STRESS-TEMPERATURE EQUATIONS OF...][research_ignaczak_1978]
- [Axisymmetric thermoelasticity problem for two-temperature...][research_khoroshun_soltanov_1978]
- [Thermal Buckling of an Annular Plate With Axisymmetric...][research_tani_1978]
- [Analysis of Interim Thermal Stress Limits for a Portable...][research_bondi_1979]
- [Correlation of predicted and measured thermal stresses on an...][research_jenkinsjm_1979]
- [Thermal Stress and Gas Bending Effects on Vibration of...][research_chen_dugundji_1980]
- [Axisymmetric problem of thermoelasticity for a...][research_soltanov_1982]

$$ \sigma_{\mathrm{th}} = E\,\alpha\,\Delta T $$

Taking aluminium alloy at a Young's modulus of 72 gigapascals and a coefficient of thermal expansion of 23
parts per million per kelvin, and the full excursion from a cold start to the recovery temperature at Mach
2.6,

$$ \sigma_{\mathrm{th}} = 72 \times 10^{9} \times 23 \times 10^{-6} \times 190.8 = 316\ \mathrm{MPa} $$

**The retained yield at that temperature is about 275 megapascals**, taking 400 at room temperature and the
68.8 percent from the table above. **The fully restrained thermal stress exceeds it, at 115 percent.**

**That number is an upper bound and not a prediction**, because no real airframe is fully restrained. The
whole structure heats, so what matters is the **difference** in temperature between skin and substructure,
and the honest way to use the relation is to invert it and ask how much difference the material can afford.

$$ \Delta T_{1/2} = \frac{0.5\,\sigma_{\mathrm{yield}}(T)}{E\,\alpha} = \frac{0.5 \times 275 \times 10^{6}}{72 \times 10^{9} \times 23 \times 10^{-6}} = 83\ \mathrm{K} $$

**Eighty-three kelvin of differential consumes half the remaining strength.** That is not a large number for
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
of work in the whole of applied gas dynamics.

- [Preliminary Investigation of a New Type of Supersonic Inlet][research_ferriantonio_nuccilouism_1946]
- [Diffuser Investigations in a Supersonic Wind Tunnel][research_diggins_1951]
- [Preliminary Investigation of a New Type of Supersonic Inlet][research_ferriantonio_nuccilouism_1951]
- [Preliminary Investigation of a Translating Cowl Technique for...][research_cortrightedgarmjr_1951]
- [Amplitude of Supersonic Diffuser Flow Pulsations][research_sterbentzwilliamh_davidsjoseph_1952]
- [Evaluation of five conical center-body supersonic diffusers...][research_englertgeraldw_oberyleonardj_1952]
- [Performance of Air Inlets at Transonic and Low Supersonic...][research_nicholsmarkr_pendleyroberte_1952]
- [Pressure Recovery, Drag, and Subcritical Stability...][research_nussdorfertheodorej_oberyleonardj_1952]
- [Pressure recovery, drag, and subcritical stability...][research_obeyleonardt_englertgeraldw_1952]
- [Investigation of Translating-spike Supersonic Inlet as Means...][research_gortongeraldc_1953]
- [Investigation of a Half-Conical Scoop Inlet Mounted at Five...][research_hasellowelle_lankfordjohnl_1953]
- [Investigation at Supersonic Speeds of a Translating-spike...][research_gortongeraldc_1954]
- [Estimation of Inlet Lip Forces at Subsonic and Supersonic...][research_moeckelwe_1955]
- [Use of Subsonic Diffuser Mach Number as a Supersonic-Inlet...][research_whalenpaulp_wilcoxfreda_1956]
- [Effects of Inlet Boundary Layer on Pressure Recovery, Energy...][research_winternitz_ramsay_1957]
- [Investigation of Translating-Double-Cone Axisymmetric Inlets...][research_jamesfconnors_georgeawise_1957]
- [Investigation of a continuous normal-shock positioning...][research_wilcoxfreda_1957]
- [Performance of a translating-double-cone axisymmetric inlet...][research_connorsjamesf_wisegeorgea_1957]
- [Investigation of Inlet Control Parameters for an...][research_andersonbh_bowditchdn_1958]
- [Note on Matching a Supersonic Intake to an Aircraft Gas...][research_stephenson_1958]
- [Aerodynamic Instability of Supersonic Inlet Diffusers][research_chang_hsu_1960]
- [Supersonic Inlet Dynamics][research_fraiser_1960]
- [On the Inlet-Flow Field for a Two-Dimensional Supersonic...][research_yamaguchi_1964]
- [Analytical study of aerodynamic means of controlling...][research_rosenbaumh_zeibergsl_1965]
- [Effect of inlet additive drag on aircraft performance][research_mount_1965]
- [Structure of the Flow Associated with a Two-Dimensional...][research_henderson_1965]
- [Studies of drag-reduction methods for subsonic operation of...][research_muller_gasko_1967_b]
- [Subsonic-transonic-drag of supersonic inlets][research_muller_gasko_1967]
- [Design and development of an air intake for a supersonic...][research_rettie_lewis_1968]
- [Development of atmospheric gust criteria for supersonic inlet...][research_barryfw_1968]
- [Inlet Duct-Engine Exhaust Nozzle Airflow Matching for the...][research_taylor_1968]
- [Static performance of an auxiliary inlet ejector nozzle for...][research_jonesjr_shrewsburygd_1968]
- [A control system concept for an axisymmetric supersonic inlet][research_chun_burr_1969]
- [Study of a family of supersonic inlet systems][research_sorensen_smeltzer_1969]
- [Pitot inlet additive drag][research_crosthwait_1970]
- [Some Experimental Results of Two-Dimensional Compressor...][research_starken_lichtfuss_1970]
- [A Supersonic Intake Control System for the External...][research_schweikhardt_grippe_1971]
- [An explicit formula for additive drag of a supersonic conical...][research_barry_1971]
- [Application of quadratic optimization to supersonic inlet...][research_lehtinenb_zellerjr_1971]
- [Effects of swirling inlet flow on pressure recovery in...][research_mcdonald_fox_1971]
- [Instantaneous and dynamic analysis of supersonic inlet-engine...][research_burstadtpl_calogerasje_1971]
- [Application of quadratic optimization to supersonic inlet...][research_lehtinen_zeller_1972]
- [Bleed system design technology for supersonic inlets][research_sybergj_koncsekjl_1972]
- [Combined Viscous-Inviscid Analysis of Supersonic Inlet...][research_reyhner_hickcox_1972]
- [Experimental Correlation of Installation Effects on Inlet...][research_ball_ross_1972]
- [Tests of a mixed compression axisymmetric inlet with large...][research_smeltzerdb_sorensenne_1972]
- [Advanced supersonic inlet technology][research_sorensen_smeltzer_1973]
- [Local flow measurements at the inlet spike tip of a Mach 3...][research_johnsonhj_montoyaej_1973]
- [Possibilities for improved supersonic inlet performance][research_sorensenne_benczedp_1973]
- [Digital integrated control of a Mach 2.5 mixed-compression...][research_battertonpg_arpasidj_1974]
- [Possibilities for Improved Supersonic Inlet Performance][research_sorensen_bencze_1974]
- [Pressure Recovery and Related Properties in Supersonic...][research_johnsoniii_wu_1974]
- [The effects of inlet conditions on supersonic cascade noise][research_hawkings_1974]
- [Unsteady supersonic inlet cascade aerodynamics a schlieren...][research_fleeter_mcclure_1974]
- [Pressure Recovery in Rectangular Adjustable Area Supersonic...][research_merkli_1975]
- [Pressure Recovery in Supersonic Diffusers][research_johnson_wu_1975]
- [Supersonic Inlet-Torsional Cascade Flutter][research_fleeter_mcclure_1975]
- [Supersonic inlet contour interpolation][research_sorensen_latham_1975]
- [Control system design using frequency domain models and...][research_control_system_1976]
- [Experimental Evaluation of an Analytically Derived Bleed...][research_syberg_koncsek_1976]

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

- [A Wing-Body Problem in a Supersonic Conical Flow][research_browne_friedman_1948]
- [Aerodynamic Characteristics of a Slender Cone-cylinder Body...][research_jackjohnr_1951]
- [Preliminary Investigation of Use of Conical Flow Separation...][research_moeckelwe_evanspjjr_1951]
- [Transonic Flow Past Cone Cylinders][research_solomongeorgee_1955]
- [A Review of Source Superposition and Conical Flow Methods in...][research_stewart_1956]
- [The Numerical Calculation of Flow Past Conical Bodies...][research_briggsbenjaminr_1960]
- [Effect of Deceleration on Pressure Distribution Along a...][research_hsu_anderson_1961]
- [An approximate analysis for the turbulent boundary layer...][research_hrubecky_1963]
- [Study of base pressure fluctuations behind a cone in...][research_panov_shvets_1966]
- [Study of flow structure behind a cone in supersonic flow][research_panov_shvets_1967]
- [Aerodynamic Force Tests of Cone Cylinder Flechette Models at...][research_opalka_1968]
- [PRESSURE MEASUREMENTS ON FOUR CONE-CYLINDER-FLARE...][research_washington_humphrey_1969]
- [Supersonic gas flow past a cone at angle of attack][research_vasilev_1970]
- [Approximate analytic solution for the position and strength...][research_davis_1971]
- [A pressure formula for an inclined circular cone in...][research_jones_1972]
- [Experimental Study of Separation from the Base of a Cone at...][research_kayser_danberg_1974]
- [An Experimental Investigation of Three-Dimensional Shock...][research_yamanaka_kamimura_1975]
- [Simple Formulae for Supersonic Flow past a Cone][research_hui_1975]
- [A Numerical Method for Supersonic Conical Flow without Axial...][research_isugiyama_1976]
- [A NUMERICAL METHOD FOR SUPERSONIC CONICAL FLOW WITHOUT AXIAL...][research_sugiyama_1977]
- [Supersonic Laminar Viscous Flow Past a Cone at Angle of...][research_agarwal_rakich_1982] The governing relation is the
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

**The result that says how to divide the compression is [Oswatitsch's][ref_oswatitsch], and the draft named it without writing it down.**
For a given number of oblique shocks the recovery is greatest when they are of equal strength, meaning equal
normal Mach components.

$$ M_1 \sin\beta_1 = M_2 \sin\beta_2 = \cdots = M_n \sin\beta_n $$

**That is a theorem worth checking rather than quoting**, and checking it required fixing an unfair
comparison. An earlier version searched equal pairs without the turning constraint while searching unequal
pairs with it, so the equal pair appeared to win by exceeding a limit the other obeyed. Under the same
twenty-five degree cap the two agree closely.

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
half of this subject and is equally large.

- [Effect of Inlet Air Distortion on the Steady-State and Surge...][research_ciepluchcarlc_1948]
- [Analytical and Experimental Investigation of Inlet-engine...][research_esenweinfredt_schuellercarlf_1952]
- [Estimation of the Effects of Distortion on the Longitudinal...][research_campion_1954]
- [Preliminary Results of the Determination of Inlet-Pressure...][research_wallnerle_lubickrj_1955]
- [PERFORMANCE OF VARIABLE TWO-DIMENSIONAL INLET DESIGNED FOR...][research_beheimma_gertsmalw_1956]
- [Jet Engine Inlet Noise Studies][research_old_1957]
- [Total-Pressure Distortion and Recovery of Supersonic Nose...][research_gelderthomasf_1957]
- [An Actuator Disc Analysis of Inlet Distortion and Rotating...][research_yeh_1959]
- [Comment on An Actuator-Disc Analysis of Inlet Distortion and...][research_dunham_1962]
- [Application of Pressure and Velocity Criteria to the Design...][research_cooper_1964]
- [Study of Wall-Pressure Fluctuations in a Supersonic-Engine...][research_shulman_parry_1966]
- [An experimental investigation of VTOL lift- engine inlet][research_lavi_1967]
- [Ch‐54A Engine Inlet Air Particle Separator][research_stephenson_shohet_1967]
- [A remark concerning engine-inlet distortion][research_sussman_1968]
- [Attenuation of circumferential inlet distortion in multistage...][research_plourde_stenning_1968]
- [DESIGN AND COMPONENT TEST OF ENGINE AIR INLET PARTICLE...][research_duffy_1968]
- [TESTS OF ONE-THIRD-SCALE NASA HYPERSONIC RESEARCH ENGINE...][research_hube_1968]
- [Reingestion characteristics and inlet flow distortion of...][research_kirk_barrack_1969]
- [Supersonic wind tunnel investigation of inlet- engine...][research_calogerasje_coltrinre_1969]
- [Investigation of Feasibility of Integral Gas Turbine Engine...][research_mcanally_williamj_1970]
- [Attenuation of inlet flow distortion upstream of axial flow...][research_callahan_stenning_1971]
- [Development of high-response data analysis aids for...][research_rowe_sussman_1971]
- [Engine/Inlet Compatibility Analysis Procedure][research_campbell_ellis_1971]
- [Evaluation of range and distortion tolerance for high Mach...][research_bilwakeshkr_doylevl_1971]
- [Investigation of Feasibility of Integral Gas Turbine Engine...][research_mcanally_iii_1971]
- [The Calculation of Optimal Linings for Jet-Engine Inlet Ducts][research_wilkinson_1971]
- [Analytical Method for Combining the Interaction of Inlet...][research_panton_1972]
- [Comments on "Attenuation of Inlet Flow Distortion Upstream of...][research_greitzer_1972]
- [Distortion and Turbulence Interaction - A Method for...][research_vandeusen_mardoc_1972]
- [Evaluation of range and distortion tolerance for high Mach...][research_bilwakeshkr_kochcc_1972]
- [Inlet airflow distortion in turbomachinery][research_tanida_1972]
- [Analysis of inlet flow distortion and turbulence effects on...][research_melickhcjr_1973]
- [Development of Sonic Inlets for Turbofan Engines][research_klujber_1973]
- [Distortion Data Analysis][research_moore_1973]
- [Errata-Analytical Method for Combining the Interaction of...][research_panton_1973]
- [Experimental Verification of a Technique for Testing...][research_palko_1973]
- [Experimental evaluation of a TF30-P-3 turbofan engine in an...][research_braithwaitewm_1973]
- [Some aspects of inlet/engine flow compatibility][research_williams_yost_1973]
- [A Similarity Parameter for Scaling Dynamic Inlet Distortion][research_moore_lueke_1974]
- [Analog computer implementation of four instantaneous...][research_costakiswg_1974]
- [Compressor Distortion Estimates Using Parallel Compressor...][research_korn_1974]
- [Effect of screen-induced total-pressure distortion on...][research_calogerasje_johnsenrl_1974]
- [Experimental Verification of a Transonic Test Technique for...][research_palko_1974]
- [Formulation of a distortion index based on peak compressor...][research_calogerasje_burstadtpl_1974]
- [Inlet Distortion Evaluation from Limited...][research_ellis_brownstein_1974]
- [Instantaneous distortion in a Mach 2.5...][research_burstadtpl_calogerasje_1974]
- [Some comparisons of the flow characteristics of a turbofan...][research_evansdg_debogdance_1974]
- [Aerodynamic Loads on Devices for Simulating Inlet/Engine Flow...][research_palko_1975]
- [Axial flow fan noise caused by inlet flow distortion][research_mugridge_1975]
- [Effect of a 180 deg-extent inlet pressure distortion on the...][research_debogdance_dicusjh_1975]
- [Experimental investigation of a simple distortion index...][research_costakiswg_1975]
- [FORTRAN program to generate engine inlet flow contour maps...][research_dicus_1975]
- [Integral Engine Inlet Particle Separator. Volume 1...][research_duffy_shattuck_1975]
- [Integral Engine Inlet Particle Separator. Volume 2. Design...][research_duffy_shattuck_1975_b]
- [Investigation of the Stall Hammershock at the Engine Inlet][research_kurkov_soeder_1975]
- [Statistical Prediction of Maximum Time-Variant Inlet...][research_jacocks_kneile_1975]
- [A method to account for variation of average compressor inlet...][research_burstadtpl_wenzellm_1976]
- [Analysis of distortion data from TF30-P-3 mixed compression...][research_kingrw_schuermanja_1976]
- [Evaluation of F-15 Inlet Dynamic Distortion][research_farr_1976]
- [Evaluation of an Airjet Distortion Generator used to Produce...][research_overall_1976]
- [Experiments Concerning the Response of Supersonic Nozzles to...][research_zukoski_auerbach_1976]
- [Modeling and analysis of the TF30-P-3 compressor system with...][research_mazzawyrs_banksga_1976]
- [Advanced Scavenge Systems for an Integrated Engine Inlet...][research_zoccoli_1977]
- [Circumferential distortion modeling of the TF30-P-3...][research_mazzawyrs_banksga_1977]
- [Computational experiments on the effects of inlet turbulence...][research_groeneweg_1977]
- [Effects of temperature transients at fan inlet of a turbofan...][research_abdelwahabm_1977]
- [Internal flow characteristics of a multistage compressor with...][research_debogdance_mossjejr_1977]
- [Mach 6 flowfield survey at the engine inlet of a research...][research_johnson_lawing_1977]
- [Signal Distortion at a Nonlinear Element][research_rees_1977]
- [Steady and non-steady flow through an i.c. engine inlet valve...][research_benson_1977]
- [Blade row dynamic digital compression program. Volume 2 J85...][research_teschwa_steenkenwg_1978]
- [Digital Computer Application in the F-15 Engine Air Inlet...][research_scherz_williams_1978]
- [Inlet-engine matching for SCAR including application of a...][research_wasserbauerjf_gerstenmaierwh_1978]
- [Nonaxisymmetric Flow through Annular Actuator Disks Inlet...][research_hawthorne_mitchell_1978]
- [Performance of Rotating Cascades under the Inlet-Distortion...][research_maekawa_higashi_1978]
- [Combined pressure and temperature distortion effects on...][research_braithwaitewm_soederrh_1979]
- [Effect of steady-state pressure distortion on flow...][research_soederrh_bobulaga_1979_b]
- [Effect of steady-state temperature distortion and combined...][research_soederrh_bobulaga_1979]
- [Evaluation of an Airjet Distortion Generator Used to Produce...][research_hubble_smith_1979]
- [Combined Pressure and Temperature Distortion Effects on...][research_braithwaite_soeder_1980]
- [Inlet Distortion Effects in Axial Compressors][research_stenning_1980]
- [Inlet Flow Distortion in Turbomachinery][research_seidel_matwey_1980]
- [Predicted and Observed Modal Radiation Patterns from JT15D...][research_heidmann_saule_1980]
- [A large-scale investigation of engine influence on inlet...][research_hodderbk_farquharbw_1981]
- [An investigation of engine influence on inlet performance][research_hodderbk_1981]
- [RALS/VCE Turbine Inlet Temperature and Engine Complexity...][research_willis_1981]
- [Effect of steady-state pressure distortion on inlet flow to a...][research_soederrh_bobulaga_1982]
- [Electromagnetic-Field Distortion Due to a Conducting...][research_kanda_1982]
- [A survey of inlet/engine distortion compatibility][research_bowditchdn_coltrinre_1983]
- [A flight study of tone radiation patterns generated by inlet...][research_preisserjs_silcoxrj_1984]
- [Effect of combined pressure and temperature distortion...][research_soederrh_mehaliccm_1984]
- [Effects of inlet distortion on a static pressure probe...][research_hughesdl_mackallkg_1984]
- [Temperature distortion generator for turboshaft engine testing][research_klannga_barthrl_1984]
- [Improved Statistical Analysis Method for Prediction of...][research_sedlock_1985]
- [PTA test bed aircraft engine inlet model test report, revised][research_hancockjp_1985]
- [A Navier-Stokes Study of Cascade Flow Fields Including Inlet...][research_davoudzadeh_liu_1987]
- [Enhancing compressor distortion tolerance by asymmetric...][research_chengt_greitzerem_1987]
- [Flow Visualization of Four-Inlet Ducted Rocket Engine...][research_brophy_hawk_1990]
- [Vortex generator design for aircraft inlet distortion as a...][research_andersonbernhardh_levyralph_1991]
- [Concept Designed and Developed for Distortion- Tolerant...][research_concept_designed_1995]
- [Universal Controller For Supersonic Engine Inlet][research_yonkewilliama_robbendaniell_1995]
- [Factors Affecting Inlet-Engine Compatibility During Aircraft...][research_steenkenwg_williamsjg_1999]
- [Active Control of Rotating Stall Demonstrated for a...][research_vanschalkwykchristian_brightmichellem_2001]
- [F/A-18A/B/C/D F404-GE-400/402 Engine Slotted Spraybar Inlet...][research_picard_whitley_2002]
- [Task IV Development of Circumferential Inlet Distortion...][research_tanchoonsooi_suderkenneth_2003]
- [Combined Cycle Engine Large-Scale Inlet for Mode Transition...][research_thomasrandy_stueberthomasj_2013]
- [Inlet Engineering Toolbox][research_frey_2014]

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

- [Some Stall and Surge Phenomena in Axial-Flow Compressors][research_huppert_benser_1953]
- [Closure to “Discussions of ‘Compressor Surge and Stall...][research_emmons_pearson_1955_b]
- [Compressor Surge and Stall Propagation][research_emmons_pearson_1955]
- [Discussion “Compressor Surge and Stall Propagation” Emmons...][research_rains_1955]
- [Experimental Investigation of the Rotating Stall in a...][research_valensi_1958]
- [The Measured and Visualized Behavior of Rotating Stall in an...][research_sovran_1959]
- [Compressor Surge in Gas Turbines and Blast Furnace Compressor...][research_strub_suter_1965]
- [Paper 17 Stage Matching, Stall, and Surge in Multi-Stage...][research_gray_1969]
- [Inlet dynamics and compressor surge][research_mays_1971]
- [Prediction of Inlet Duct Overpressures Resulting from Engine...][research_marshall_1973]
- [Casing Modification for Increasing the Surge Margin of a...][research_amann_nordenson_1975]
- [On the Partial Flow Rate Characteristic of Axial-Flow...][research_tanaka_murata_1975_b]
- [On the Partial Flow Rate Performance of Axial-Flow Compressor...][research_tanaka_murata_1975_c]
- [On the Partial Flow Rate Performance of Axial-Flow Compressor...][research_tanaka_murata_1975]
- [Prediction of Compressor Stall for Distorted and Undistorted...][research_daniele_teren_1975]
- [Prediction of compressor stall for distorted and undistorted...][research_danielecj_terenf_1975]
- [Closure to “Discussions of ‘Surge and Rotating Stall in Axial...][research_greitzer_1976_c]
- [Discussion “Surge and Rotating Stall in Axial Flow...][research_prince_1976]
- [On the Dynamics of Compressor Surge][research_mcqueen_1976]
- [Surge and Rotating Stall in Axial Flow Compressors Part I...][research_greitzer_1976]
- [Surge and Rotating Stall in Axial Flow Compressors Part II...][research_greitzer_1976_b]
- [The Time Domain of Centrifugal Compressor and Pump Stability...][research_dean_young_1977]
- [Closure to “Discussion of ‘Prediction of Compressor...][research_day_greitzer_1978_b]
- [Discussion “Prediction of Compressor Performance in Rotating...][research_harman_1978]
- [Investigation on Compressor Surge 1st Report, Compressor...][research_ohyama_1978]
- [Prediction of Compressor Performance in Rotating Stall][research_day_greitzer_1978]
- [On the dynamics of compressor surge][research_tondl_1979]
- [Reasons for Centrifugal Compressor Surging and Surge Control][research_kolnsberg_1979]
- [Tests of an Improved Rotating Stall Control System on a J-85...][research_ludwig_1979]
- [Compressor Rotating Stall in Uniform and Nonuniform Flow][research_cossar_moffatt_1980]
- [Review Axial Compressor Stall Phenomena][research_greitzer_1980]
- [Rotating Stall and Surge][research_stenning_1980_b]
- [Experimental and Theoretical Study of Surge in a Small...][research_hansen_jorgensen_1981]
- [A Consideration Concerning Stall and Surge Limitations Within...][research_kosuge_ito_1982]
- [A Simple Model for Compressor Stall Cell Propagation][research_cumpsty_greitzer_1982]
- [Fatigue, Workload, and Personality Indices of Air Traffic...][research_rokicki_1982]
- [Performance and surge limits of a TF30-P-3 turbofan...][research_wasserbauerjf_neumannhe_1985]
- [Active Control of Compressor Surge and Stall][research_boussios_epstein_1992]

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

**The record gives the travel and not the radius.** Four inches of movement is documented; the diameter of
the Lancer's inlets is not. **So the relation is inverted**, which is the honest move when a parameter is
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
operating away from the design point is where this calculation comes from.

- [Inlet spillage drag tests and numerical flow-field analysis...][research_hawkinsje_kirklandfp_1976]
- [Pressure Recovery in Rectangular Constant Area Supersonic...][research_merkli_1976]
- [Supersonic Diffuser Research][research_wegener_1977]
- [Optimal control of a supersonic inlet to minimize frequency...][research_lehtinenb_zellerjr_1978]
- [Effects of Airframe-Inlet Integration on Half -Axisymmetric...][research_surber_sedlock_1979]
- [Inlet design studies for a Mach 2.2 advanced supersonic...][research_shimabukurokm_welgehr_1979]
- [A Simulation of a Supersonic Intake on a Hybrid Computer][research_colbourne_1980]
- [Effect of Intake Conditions on Supersonic Unstalled Flutter...][research_halliwell_1980]
- [Experimental Study of Supersonic Diffusers with Large Aspect...][research_krause_1981]
- [Small-Scale Supersonic Inlet Test Facility][research_haas_karanian_1981]
- [Inlet Design Studies for a Mach 2.2 Advanced Supersonic...][research_shimabukuro_welge_1982]
- [Pressure recovery in a constant-area, two-stream supersonic...][research_amatucci_addy_1982]
- [Some Effects of Cruise Speed and Engine Matching on...][research_bangert_santman_1982]
- [One-dimensional unsteady modeling of supersonic inlet...][research_adamsjcjr_martindalewr_1984]
- [Low-speed aerodynamic test of an axisymmetric supersonic...][research_powellag_welgehr_1985]
- [Low-speed performance of an axisymmetric, mixed-compression...][research_trefnycj_wasserbauerjw_1986]
- [Numerical simulation of three-dimensional supersonic inlet...][research_kawamurat_chyuwj_1987]
- [Theoretical evaluation of engine auxiliary inlet design for...][research_bolesmichaela_heavnerrichardl_1988]
- [Results from computational analysis of a mixed compression...][research_saundersjd_keithtgjr_1991]
- [Theoretical evaluation of engine auxiliary inlet design for...][research_bolesmichaela_heavnerrichardl_1991]
- [Analytical and experimental studies of a short compact...][research_iekchanthy_burleyrichardr_1993]
- [A Full Navier-Stokes Analysis of Subsonic Diffuser of a...][research_kapoorkamlesh_andersonbernhardh_1994]
- [Large Eddy Simulation of Supersonic Inlet Flows][research_moin_lele_1998]
- [Two-Dimensional Bifurcated Inlet Variable Cowl Lip Test...][research_hoffmantr_2000]
- [Supersonic Inlet with Pylons Set and Star-Shaped Forebody for...][research_gilinskym_gonoral_2003]
- [Supersonic Test of the 10-Inch Bifurcated Two-Stage...][research_carlincm_frischi_2003]
- [Two Stage Supersonic Inlet TSSI 10-inch Model Calculations][research_chapmandave_smithcf_2005]
- [Analysis of a Channeled Centerbody Supersonic Inlet for F-15B...][research_ratnayakenalina_2010]
- [Axisymmetric Calculations of a Low-Boom Inlet in a Supersonic...][research_chimarodrickv_hirtstefaniem_2011]
- [Computational Analysis of the Large Scale Low-Boom Supersonic...][research_chimarodrickv_2011]
- [External-Compression Supersonic Inlet Design Code][research_slaterjohnw_2011]
- [Flow Simulation of Supersonic Inlet with Bypass Annular Duct][research_kimhyoungjin_kumanotakayasu_2011]
- [Supersonic Inlet Flow Control Using Localized Arc Filament...][research_samimy_webb_2011]
- [Analysis of Buzz in a Supersonic Inlet][research_chimarodrickv_2012]
- [Quasi 1D Modeling of Mixed Compression Supersonic Inlets][research_kopasakisgeorge_connollyjosephw_2012_b]
- [Quasi One-Dimensional Unsteady Modeling of External...][research_kopasakisgeorge_connollyjosephw_2012]
- [Research on Supersonic Inlet Bleed][research_davisdavido_vyasmanana_2012]
- [Flow Control for Supersonic Inlet Applications][research_babinsky_2014]
- [Methodology for the Design of Streamline-Traced...][research_slaterjohnw_2014]
- [The Origin of Inlet Buzz in a Mach 1.7 Low Boom Inlet Design][research_andersonbernhardh_weirlois_2014]

#### The Check That Makes This Worth Doing

An inversion that cannot be tested is a rearrangement. This one can be tested, because the engine's airflow
is documented independently.

The capture area needed to admit a given physical mass flow at full capture is

$$ A_c = \frac{\dot m}{\rho_\infty V_\infty} $$

**The TF30-P-100 is documented at 260 pounds per second, which is 117.93 kilograms per second.** At Mach 2.0
and 35,000 feet the free-stream mass flux is $\rho_\infty V_\infty = 225.0$ kilograms per square metre per
second, so

$$ A_c = \frac{117.93}{225.0} = 0.524\ \mathrm{m}^2 = 5.639\ \mathrm{ft}^2 $$

| Assumed cone half-angle | Implied capture from the travel | Required by the engine | Error |
|---|---|---|---|
| 20° | 3.417 ft² | 5.639 ft² | −39.4 percent |
| **25°** | **5.401 ft²** | **5.639 ft²** | **−4.2 percent** |
| 27.5° | 6.500 ft² | 5.639 ft² | +15.3 percent |
| 30° | 7.535 ft² | 5.639 ft² | +33.6 percent |

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

#### A Note on Corrected Flow, Because an Earlier Version Got It Wrong

A first attempt at this comparison converted the engine's maximum *corrected* airflow to physical airflow at
Mach 2.6 and obtained 356 kilograms per second, three times the sea-level rating. The
[corrected flow][ref_corrected_flow] relation is

$$ \dot m_{\mathrm{corr}} = \frac{\dot m \sqrt{\theta}}{\delta}, \qquad \theta = \frac{T_{t2}}{288.15}, \qquad \delta = \frac{p_{t2}}{101325} $$

**The arithmetic was right and the premise was wrong.** Corrected airflow and the engine matching it governs
are treated in [Oates][book_oates] and [Mattingly][book_mattingly_engine]. A compressor does not hold its
maximum corrected flow while its inlet total temperature rises by two hundred kelvin, because the corrected
speed falls and the operating point walks down the map.
**The engine's flow schedule at high Mach is not in the public record**, so the comparison above is made at
Mach 2.0 using physical flow, where the engine is near its rating and the assumption is defensible. The
point is recorded because a number that is not credible is a finding rather than a nuisance.

### The Metric the Competition Actually Used

By 1970 the argument about fighters had moved. Top speed and rate of climb had been the currency of the
1950s, and the F-104 was designed to win on them.
**What replaced them was [energy manoeuvrability][ref_energy_maneuverability]**, the framework associated
with [John Boyd][ref_boyd] and [Thomas Christie][ref_christie], which asks not how fast an aircraft can go
but how much energy it can gain or hold while turning.

The framework's primitive is energy height, the altitude an aircraft would reach if it traded all its speed
for height without loss, and the draft named it without writing it. The treatment followed here is
[Whitford][book_whitford], with the equations of motion behind it in
[Stevens and Lewis][book_stevens_lewis].

**This heading is thinner than any other in the article and the thinness is a finding.** Of the same 6,518
records, seven carry energy height, energy state or minimum time to climb in their titles, and all seven are
cited here. **The subject is not small. It is indexed elsewhere**, inside trajectory optimisation and inside
the optimum-climb literature, and its foundational documents are Air Force internal reports that no journal
indexed.

- [Optimum Climb to Height][research_corner_1940]
- [The Rate of Climb of Turbo‐Jet Aircraft][research_whittley_1952]
- [On the solution of a degenerate variational problem and the...][research_egorov_1958]
- [Optimum Path of an Airplane -- Minimum Time to Climb][research_theodorsen_1959]
- [Optimum climb trajectories at constant lift coefficient][research_andrews_1969]
- [Optimum Climb to Cruise Noise Trajectories for the High Speed...][research_bertonjeffreyj_2003]

$$ h_e = h + \frac{V^2}{2g} $$

At 15,000 feet and Mach 0.9 that is

$$ h_e = 4{,}572 + \frac{290.0^2}{2 \times 9.80665} = 4{,}572 + 4{,}289 = 8{,}861\ \mathrm{m} = 29{,}072\ \mathrm{ft} $$

The central quantity is [specific excess power][ref_specific_excess_power],
**which is the rate of change of that height and not an independent definition**.

$$ P_s = \frac{dh_e}{dt} = V\,\frac{T - D}{W} $$

**The thrust-to-weight ratio is the other term the comparison turns on**, and it is tabulated below without
ever being written.

$$ \frac{T}{W} = \frac{25{,}000\ \mathrm{lbf}}{24{,}385\ \mathrm{lb}} = 1.025 $$

**A re-winged F-104 improves on the old metrics. The question is what it does to this one.**

The framework and its consequences for fighter design are set out in [Whitford][book_whitford], and Boyd's
own part in it is treated at length in [Coram][book_coram].

The literature on energy manoeuvrability, sustained turning performance and combat aircraft performance
comparison is smaller than the others treated here, and the article says so rather than padding it.

- [An Energy Approach to Climb Performance Estimation of a...][research_tamboli_1956]
- [Agility performance of several vstol and stol aircraft][research_stutz_price_1964]
- [Flight determined acceleration and climb performance of an...][research_marshallrt_1971]
- [Design for Air Combat][research_herbst_krogull_1973]
- [Preliminary performance estimates of an oblique, all-wing...][research_nelmswpjr_baileyro_1974]
- [An Initial Investigation of Those ACMR Air Combat Maneuvering...][research_hutchins_jones_1975]
- [Army Preliminary Evaluation YAH-1R Improved Cobra Agility and...][research_stewart_dominick_1975]
- [Structural Concept Analysis Report for the East Coast Air...][research_crestengineeringinctulsaok_1976]
- [Study of a very low cost air combat maneuvering trainer...][research_hillgc_bowlesjv_1976]
- [Flight comparison of the transonic agility of the F-111A...][research_friendel_sakamotogm_1978]
- [The Relationship between Air Combat Maneuvering Range ACMB...][research_hutchins_jr_1978]
- [An investigation into possible back profiles for reclined...][research_an_investigation_1979]

**That thinness is itself worth reporting.** The first harvest returned 28 records against 232 for materials
at elevated temperature, and a second harvest written in the period vocabulary of specific excess power,
minimum time to climb and turning performance raised it to 51.
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
area rule underpins every line of that table.

- [Aerodynamic characteristics of several airfoils of low aspect...][research_zimmermanch_1935]
- [Preliminary Investigation in the NACA Low-Turbulence Tunnel...][research_vondoenhoffalberte_hortonelmera_1942]
- [Theoretical lift and drag of thin triangular wings at...][research_brownclintone_1946]
- [An Application of Lifting-surface Theory to the Prediction of...][research_jonesarthurl_flanaganmildredg_1947]
- [An Investigation at Low Speed of a Large-scale Triangular...][research_andersonadriene_1947]
- [Distribution of wave drag and lift in the vicinity of wing...][research_evvardjohnc_1947]
- [Stability and control characteristics of an airplane model...][research_schuldenfreimarvin_comisarowpaul_1947]
- [Supersonic Wave Drag of Sweptback Tapered Wings at Zero Lift][research_margoliskenneth_1947]
- [Aerodynamic Characteristics at Subsonic and Supersonic Mach...][research_walkerharoldj_berggrenroberte_1948]
- [An Analysis of the Effects of Wing Aspect Ratio and Tail...][research_axelsonjohna_crownjconrad_1948]
- [Free-flight Investigation of the Rolling Effectiveness of...][research_sandahlcarla_1948]
- [Spanwise loading for wings and control surfaces of low aspect...][research_deyoungjohn_1950]
- [Supersonic flow over an inclined wing of zero aspect ratio][research_stewartson_1950]
- [Effects of Horizontal-tail Position, Area, and Aspect Ratio...][research_jaquetbyronm_1951]
- [Lift, Drag, and Pitching Moment of Low-aspect-ratio Wings at...][research_hallcharlesf_heitmeyerjohnc_1951]
- [Stability and Control Characteristics of a Complete Airplane...][research_schulderfreimarvin_comisarowpaul_1951]
- [Supersonic Flow Past Bodies of Revolution with Thin Wings of...][research_stocker_1951]
- [Wind tunnel test of a wing of finite aspect ratio of...][research_orman_rae_1951]
- [A note on the drag due to lift of delta wings at Mach numbers...][research_osborneroberts_kellythomasc_1953]
- [AERODYNAMIC CHARACTERISTICS OF LOW-ASPECT-RATIO WINGS AT HIGH...][research_bertrammh_ulmannef_1953]
- [On the Low Aspect Ratio Oscillating Rectangular Wing in...][research_miles_1953]
- [Recent Results Pertaining to the Application of the "Area...][research_whitcombrichardt_1953]
- [The Aerodynamic Characteristics of Low Aspect Ratio Wing-Body...][research_lawrence_1953]
- [Theory of Wing-Body Drag at Supersonic Speeds][research_jonesrobertt_1953]
- [Some Aerodynamic Effects of Streamwise Gaps in Low Aspect...][research_bleviss_struble_1954]
- [THE EFFECT OF AN AXIALLY SYMMETRIC FUSELAGE ON THE...][research_epstein_1954]
- [Wave drag of wings at supersonic speeds][research_leslie_perry_1954]
- [A Programme for Low Aspect Ratio Wing Analysis][research_morton_1956]
- [A special method for finding body distortions that reduce the...][research_lomaxharvard_heasletmaxa_1956]
- [Aeroelastic Problems of Low Aspect Ratio Wings][research_woodward_1956]
- [Numerical Results for the Longitudinal Stability Derivatives...][research_winograd_miles_1956]
- [Theory of wing-body drag at supersonic speeds][research_jonesrobertt_1956]
- [A note on the application of the supersonic area rule to the...][research_lock_1957]
- [Nonlifting wing-body combinations with certain geometric...][research_lomaxharvard_1957]
- [On the Wave Drag of Wing-Body Combination Moving at...][research_kawamura_karashima_1957]
- [Aerodynamic Characteristics in Sideslip of a Large-Scale 49...][research_mclemorehclyde_1958]
- [Theoretical Calculations of Supersonic Wave Drag at Zero Lift...][research_margoliskenneth_malvestutofranksjr_1958]
- [Vibration of a thin rectangular wing of large aspect ratio in...][research_kopzon_1958]
- [A Numerical Method for Calculating the Wave Drag of a...][research_levylionelljr_yoshikawakennethk_1959]
- [An Experimental Investigation of the Effect of a Canard...][research_meneesgenep_boydjohnw_1959]
- [Divergence of Plate Airfoils of Low Aspect Ratio at...][research_hancock_1959]
- [Effects of Outboard Thickened and Blunted Leading Edges on...][research_holdawaygeorgeh_lazzeronifranka_1959]
- [Notes on Thin Wing Theory at Low Supersonic Speeds][research_hancock_1959_b]
- [On the wave drag of non anixymmetric bodies at supersonic...][research_maikapar_1959]
- [Predicted Static Aeroelastic Effects on Wings with Supersonic...][research_brownstuartc_1959]
- [Supersonic and Moment-of-Area Rules Combined for Rapid...][research_levylionelljr_1959]
- [The Effect of Moment of Area Rule Modifications on the Drag...][research_dickeyrobertr_1959]
- [The Limiting Circulatory Lift of a Wing of Finite Aspect Ratio][research_mccormick_1959]
- [A Note on the Drag Due to Lift of Delta Wings at Mach Numbers...][research_robertsosborne_thomasckelly_1960]
- [A Supersonic Area Rule and an Application to the Design of a...][research_whitcombrichardt_sevierjohnrjr_1960]
- [Aerodynamic Characteristics of a Large-Scale Unswept...][research_mclemorehclyde_petersonjohnbjr_1960]
- [Comments on "Limiting Circulatory Lift of a Wing of Finite...][research_hancock_1960]
- [Further Comments on "Limiting Circulatory Lift of a Wing of...][research_ribner_1960]
- [On the calculation of the minimum wave plus vortex drag of...][research_hunziker_1960]
- [Some Examples of the Applications of the Transonic and...][research_nelsonrobertl_welshclementj_1960]
- [Supersonic Aerodynamic Characteristics of a Low-Drag Aircraft...][research_gillespiewarrenjr_1960]
- [Effects of Canard Planform and Wing-Leading-Edge Modification...][research_spencerbernardjr_1961]
- [Large-Scale Wind-Tunnel Tests of an Airplane Model with an...][research_weibergjamesa_holzhausercurta_1961]
- [On the Aerodynamic Forces Acting on a Delta‐wing in...][research_stanisic_1961]
- [Some Effects of Sweep and Aspect Ratio on the Transonic...][research_jonesgwjr_unangstjr_1963]
- [Low Aspect Ratio Turbines][research_ohlsson_1964]
- [FORCE AND PRESSURE TESTS ON A SEMI-SPAN DELTA WING AT...][research_pfaff_1965]
- [THE MARVEL PROJECT. PART E. A UNIQUE SOLUTION TO THE PROBLEM...][research_roberts_1965]
- [A concept of the vortex lift of sharp-edge delta wings based...][research_polhamusec_1966]
- [Errata "Hypersonic Flow over a Delta Wing of Moderate Aspect...][research_malmuth_1966_b]
- [Hypersonic flow over a delta wing of moderate aspect ratio][research_malmuth_1966]
- [WIND TUNNEL INVESTIGATION OF AN ASPECT RATIO 10 TANDEM WING...][research_harry_trobaugh_1966]
- [Static aerodynamic characteristics of three ram-air-inflated...][research_burksmjr_waregm_1967]
- [Thin flat bodies of minimum wave drag in nonequilibrium...][research_kraiko_tkalenko_1967]
- [Application of the leading-edge-suction analogy of vortex...][research_polhamusec_1968]
- [Aspect Ratio, Loading, Wing Span, and Membrane Areas of Bats][research_farney_fleharty_1969]
- [Slender bodies of revolution with minimum wave drag in...][research_tkalenko_1969]
- [A vortex wake model for optimum heavily loaded ducted fans][research_gray_wright_1970]
- [Flutter of low aspect ratio plates][research_dowell_ventres_1970]
- [Wave drag of optimum and other boat tails][research_maise_1970]
- [Cambered wing of small aspect ratio near a boundary surface][research_kholyavko_1971]
- [Experimental investigation of the performance of vortex...][research_michellga_1971]
- [On the Characteristics of Wing with Tip Clearance 3rd Report...][research_sugiyama_1971_b]
- [On the Characteristics of Wing with Tip Clearance Part 3, The...][research_sugiyama_1971]
- [Vibration Characteristics of Low Aspect Ratio Compressor...][research_petricone_sisto_1971]
- [Jet noise of an augmentor wing-advanced supersonic transport][research_franciscusl_1972]
- [Stability of Swivel Wing Supersonic Aircraft][research_bennetclark_1972]
- [Trapped-ion instability in the low-aspect ratio limit][research_jablon_1972]
- [Aircraft wing-tip vortex modification][research_jarvinen_1973]
- [Collisional resistivity in low aspect ratio tori][research_coppi_sigmar_1973]
- [On constructing the contour of minimum wave drag in an...][research_kraiko_tilliaeva_1973]
- [Aerodynamic characteristics of a hypersonic research airplane...][research_penlandja_fournierrh_1975]
- [Design study of structural concepts for an arrow-wing...][research_sakataif_davisgw_1975]
- [Effects of wing bend on the aerodynamic characteristics of a...][research_hopkinsej_1975]
- [Estimation of velocities and roll-up in aircraft vortex wakes][research_bilanin_donaldson_1975]
- [Low-speed wind-tunnel investigation of a large-scale advanced...][research_shiversjp_mclemorehc_1975]
- [On the wave drag integral for slender bodies][research_bera_1975]
- [Preservation of wing leading edge suction at the plane of...][research_larrabeeee_1975]
- [Some observations on the Adams body of minimum wave drag][research_ramaswamy_viswanathan_1975]
- [The Flow Over a “High” Aspect Ratio Gothic Wing at Supersonic...][research_narayan_1975]
- [The influence of the interface on the strength and elastic...][research_the_influence_1975]
- [Augmentation of Vortex Lift by Spanwise Blowing][research_campbell_1976]
- [Preliminary wind tunnel tests of a finite aspect ratio high...][research_rice_oetting_1976]
- [Propulsive-lift concepts for improved low-speed performance...][research_coepljr_1976]
- [Theory of wing-body drag at supersonic speeds][research_jonesrt_1976]
- [Aerodynamic characteristics at Mach 6 of a hypersonic...][research_clarkle_richiecb_1977]
- [Effects of external stores on the air combat capability of a...][research_spearmanml_sawyerwc_1977]
- [Evaluation of structural design concepts for an arrow-wing...][research_sakataif_davisgw_1977]
- [Numerical evaluation of transonic wave drag][research_desai_viswanathan_1977]
- [Supersonic Wave Drag for Nonplanar Singularity Distributions][research_chin_1977]
- [Aerodynamic characteristics of a hypersonic research airplane...][research_penlandja_creeltrjr_1978]
- [An Alternative Approach to the High Aspect Ratio Wing With...][research_kida_miyai_1978]
- [Arrow Wings for Supersonic Cruise Aircraft][research_wright_bruckman_1978]
- [Low-speed aerodynamic characteristics from wind-tunnel tests...][research_smithpm_1978]
- [Supersonic wave drag of planar singularity distributions][research_chin_1978]
- [Improved Wave Drag Predictions Using Modified Linear Theory][research_stancil_1979]
- [Airplane wing leading edge variable camber flap][research_colejb_1980]
- [Determination of the vorticity on a wing of small aspect...][research_golubkin_1980_b]
- [Experimental Study of Low Aspect Ratio Compressor Blading][research_reid_moore_1980]
- [Low-aspect ratio ignimbrites][research_walker_heming_1980]
- [On the theory of a wing with small aspect ratio in a...][research_golubkin_1980]
- [Optimal flight paths for winged, supersonic flight vehicles...][research_large_1981]
- [Closed-form solutions of supersonic wing-body interference][research_viranr_fandn_1982]
- [Control of Forebody Vortex Orientation to Enhance Departure...][research_skow_moore_1982]
- [Flow with separation of an ideal fluid past a wing of...][research_zubtsov_sudakov_1982]
- [Load distribution on deformed wings in supersonic flow][research_burkhalter_1982]
- [A supersonic maneuver wing designed for nonlinear attached...][research_masonwh_siclarimj_1983]
- [A wing concept for supersonic maneuvering][research_masonwh_1983]
- [An overview of two nonlinear supersonic wing design studies][research_millerds_pittmanjl_1983]
- [Status review of a supersonically-biased fighter wing-design...][research_woodrm_millerds_1983]
- [Arrays for minimum wave drag of bodies of revolution][research_nielsenjn_1985]
- [Assessment of preliminary prediction techniques for wing...][research_woodrm_millerds_1985_b]
- [Fundamental aerodynamic characteristics of delta wings with...][research_woodrm_millerds_1985]
- [Basic studies on delta wing flow modifications by means of...][research_hofflerkd_raodm_1986]
- [Computation of leading-edge vortex flows][research_newsomerw_thomasjl_1986]
- [Nonlinear lift control at high speed and high angle of attack...][research_lamarje_1986]
- [Planform effects for low-fineness ratio multibody...][research_mcmillinsn_woodrm_1986]
- [Zero-Lift Wave Drag of Complex Aircraft Configurations][research_craidoncb_1986]
- [Nonlinear lift control at high speed and high angle of attack...][research_lamarjohne_1987]
- [Experimental and theoretical study of the effects of wing...][research_bauerstevenxs_mcmillinsnaomi_1988]
- [Leading edge vortex dynamics on a pitching delta wing][research_lemaysp_batillsm_1988]
- [Some low-speed flutter characteristics of simple...][research_doggettrobertvjr_soistmanndavidl_1989]
- [The aerodynamic design of the oblique flying wing supersonic...][research_vanderveldenalexanderjm_krooilan_1990]
- [Lift augmentation on a delta wing via leading edge fences and...][research_buchholzmarkd_1992]
- [RTJ-303 Variable geometry, oblique wing supersonic aircraft][research_antaranalbert_beletehailu_1992]
- [An Experimental Study of Wing Tip Vortex in the Near Wake of...][research_zheng_ramaprian_1993]
- [Computational Method in Optimal Bending-Twisting...][research_dehua_changyou_1993]
- [Lift Augmentation on a Delta Wing via Leading Edge Fences and...][research_buchholzmarkd_tsojin_1993]
- [Effect of leading- and trailing-edge flaps on clipped delta...][research_hernandezgloria_woodrichardm_1994]
- [An assessment of viscous effects in computational simulation...][research_kinardtima_harrisbrendaw_1995]
- [Thrust-Induced Effects on a Pitching-Up Delta Wing Flow Field...][research_vandommelen_1995]
- [Thrust-Induced Effects on a Pitching-Up Delta Wing Flow Field][research_lourenco_shih_1996]
- [Simulation Study of VISTA/F-16 Maneuverability Enhancement...][research_mckeehen_cord_1997]
- [Vortex leading edge flap assembly for supersonic airplanes][research_rudolphpeterkc_1997]
- [Origin and Control of Unsteady Loading of Aerodynamic...][research_rockwell_2001]
- [An Assessment of CFD Effectiveness for Vortex Flow Simulation...][research_praj_fghaffari_2003]
- [Turbulent Vortex-Flow Simulation Over a 65 deg Sharp and...][research_ghaffarifarhad_2005]
- [Trapped Vortex Combustor Development for Military Aircraft][research_barlow_burrus_2008]
- [Development of Advanced High Lift Leading Edge Technology for...][research_brightmichellem_korntheuerandrea_2013]
- [The Lift Distribution on Conical and Nonconical Flow Regions...][research_goodman_1949]
- [Supersonic Flow Past Wing-Body Combinations][research_chester_1953]
- [REDUCTION OF DRAG DUE TO LIFT AT SUPERSONIC SPEEDS][research_graham_lagerstrom_1954]
- [An Extension of the Method of Generalised Conical Flows for...][research_portnoy_1963]
- [Uniform second-order solution for supersonic flow over delta...][research_clarke_wallace_1964]
- [LEADING-EDGE WEDGES TO REDUCE THE DRAG OF THICK WINGS AT...][research_hartley_furey_1965]
- [LIFT-TO-DRAG RATIOS OF SEMISPAN DELTA WING CONFIGURATIONS AT...][research_pfaff_1968]
- [Tests of Vortex Generators to Prevent Separation of...][research_gartling_1970]
- [The Effects of Yaw on Conical Wings at High Supersonic Speeds][research_hillier_1970]
- [A Numerical Method for Calculating the Trailing Vortex System...][research_butter_hancock_1971]
- [Structure of Betz Vortex Cores][research_jordan_1973]
- [Vortex Measurements Behind a Swept Wing Transport Model][research_orloff_ciffone_1974]
- [Recent Loads Calibration Experience With a Delta Wing Airplane][research_jenkinsjeraldm_kuhlalberte_1977]
- [Measured Wake-Vortex Characteristics of Aircraft in Ground...][research_ciffone_pedley_1979]
- [An Integral Equation for the Linearized Unsteady Supersonic...][research_guderley_1987]
- [An Integral Equation for the Linearized Supersonic Flow Over...][research_guderley_1988]
- [Measurements of Supersonic Wing Tip Vortices][research_smartmichaelk_kalkhoranirajm_1994]
- [Invariance of Hypersonic Normal Force Coefficients with...][research_hawkinsrichard_penlandjima_1997]
- [Experimental Investigation of Vortex-Tail Interaction on a...][research_ghee_gonzalez_1999]

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
| 0.0 | F-104G | 3.89 | 7.28 °/s | 582 ft/s |
| 0.0 | **CL-1200-2** | **5.50** | **10.48 °/s** | **823 ft/s** |
| 0.0 | F-5E | 4.58 | 8.67 °/s | 461 ft/s |
| 0.0 | F-15A | 6.04 | 11.54 °/s | 854 ft/s |
| 0.5 | F-104G | 4.46 | 8.43 °/s | 592 ft/s |
| 0.5 | **CL-1200-2** | **6.34** | **12.13 °/s** | **830 ft/s** |
| 0.5 | F-5E | 5.33 | 10.15 °/s | 467 ft/s |
| 0.5 | F-15A | 6.97 | 13.37 °/s | 860 ft/s |
| 1.0 | F-104G | 5.41 | 10.29 °/s | 601 ft/s |
| 1.0 | **CL-1200-2** | **7.73** | limit binds | 836 ft/s |
| 1.0 | F-5E | 6.64 | 12.71 °/s | 473 ft/s |
| 1.0 | F-15A | 8.53 | limit binds | 866 ft/s |

The period and contemporary work on turning performance, load factor and combat aircraft comparison stands
behind this table.

- [Performance and human factors results from thrust vectoring...][research_penningtonje_meintelajjr_1980]
- [Impact of flying qualities on mission effectiveness for...][research_harristm_beermanda_1983]
- [Impact of flying qualities on mission effectiveness for...][research_harristm_beermanda_1984]
- [Army Aviation and Air Combat Evolutionary or Revolutionary][research_cox_roy_1988]
- [Piloted simulator assessments of agility][research_schneideredwardt_1990]
- [Development and evaluation of an inverse solution technique...][research_whalleymatthews_1991]
- [Aircraft Maneuvers for the Evaluation of Flying Qualities and...][research_wilson_riley_1993]
- [Aviators, Air Combat, and Combat Stress An Air Force...][research_wells_1993]
- [Utilization of an agility assessment module in analysis and...][research_nganangelen_biezaddaniel_1996]
- [Night Air Combat. A United States Military-Technical...][research_krause_1997]
- [Time Sensitive Control of Air Combat Operations][research_lewis_1998]

**The result is favourable to Lockheed and it is robust.** At every leading-edge suction fraction the Lancer
out-turns the F-5E that beat it, comfortably, and it sits close behind the F-15A.

**The specific excess power comparison is the striking one. At 830 feet per second against the F-15A's 860, the Lancer is within 3.5 percent of an aeroplane that cost several times as much.**

The ranking does not depend on the parasite drag assumption.

| $C_{D_0}$ | F-104G | CL-1200-2 | F-5E | F-15A |
|---|---|---|---|---|
| 0.0150 | 4.48 | 6.36 | 5.36 | 7.00 |
| 0.0175 | 4.43 | 6.29 | 5.26 | 6.91 |
| 0.0200 | 4.37 | 6.21 | 5.15 | 6.82 |
| 0.0250 | 4.26 | 6.06 | 4.93 | 6.64 |

**A model with a free parameter that reproduces an expectation has demonstrated very little.** What this one
has demonstrated is narrower and firmer, because
**the ordering is invariant across the whole plausible range of both free parameters**, which is a statement
about the ordering and not about the absolute numbers, and the absolute numbers should not be quoted as
predictions of what the aircraft would have achieved.

**And it makes the political story quantitative.** The claim that some in the Air Force saw the Lancer as a
threat to the F-15 is usually reported as an attitude.
**The arithmetic says the attitude was not unreasonable.** An aeroplane within four percent of the F-15's
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
this, and the F-104 needed blown flaps to land at all.

- [Analysis of the effects of boundary-layer control in the...][research_hortonelmera_loftinlaurencek_1951]
- [RESEARCH ON HIGH LIFT BOUNDARY LAYER SUCTION INVESTIGATIONS...][research_northropaircraftinchawthorneca_1952_b]
- [STRUCTURAL CONSIDERATIONS OF PERFORATED MATERIALS USED IN...][research_cliett_1952]
- [RESEARCH ON HIGH LIFT BOUNDARY LAYER SUCTION INVESTIGATIONS...][research_northropaircraftinchawthorneca_1953]
- [Full-scale-wind-tunnel Tests of a 35 Degree Sweptback Wing...][research_kelleymarkw_tolhurstwilliamhjr_1955]
- [RESEARCH AND REPORTS ON LAMINAR FLOW BOUNDARY LAYER CONTROL...][research_northropaircraftinchawthorneca_1956]
- [APPLICATIONS OF HIGH EFFICIENCY BOUNDARY LAYER CONTROL][research_raspet_1957]
- [ANALYSIS OF THE POWER REQUIREMENT OF A BLOWING AIRFOIL WITH...][research_helmbold_1958]
- [Blowing-Type Boundary-Layer Control as Applied to the...][research_kellymarkw_andersonsethb_1958]
- [Effectiveness of Boundary-layer Control, Obtained by Blowing...][research_spreemannkennethp_1958]
- [Large-Scale Wind-Tunnel Tests of an Airplane Model with an...][research_griffinroynjr_holzhausercurta_1958]
- [Approach and Landing Investigation at Lift-Drag Ratios of 2...][research_matrangagenej_armstrongneila_1959]
- [Force-Test Investigation of the Stability and Control...][research_newsomwilliamajr_tostilouisp_1959]
- [Full-Scale Wind-Tunnel Investigation of a Jet Flap in...][research_aoyagikiyoshi_hickeydavidh_1959]
- [Low-Speed Wind-Tunnel Investigation of Blowing Boundary-Layer...][research_makiralphl_1959]
- [Wind-Tunnel Investigation of Subsonic Longitudinal...][research_thompsonrobertf_voglerraymondd_1959]
- [Aerodynamic and Landing Measurements Obtained During the...][research_aerodynamic_and_1960]
- [Flight Investigation of the Low-Speed Characteristics of a 45...][research_quigleyherveyc_andersonsethb_1960]
- [Large-Scale Wind-Tunnel Tests and Evaluation of the Low-Speed...][research_hickeydavidh_aoyagikiyoshi_1960]
- [Reynolds-Analogy Parameter for the Laminar Boundary Layer...][research_faulders_1960]
- [A Flight Examination of Operating Problems of V/STOL Aircraft...][research_innisrobertc_quigleyherveyc_1961]
- [Aerodynamic Aspects of Boundary Layer Control for High Lift...][research_williams_butler_1963]
- [Calculation of the laminar boundary layer in a compressible...][research_lyu_1963]
- [LARGE-SCALE WIND-TUNNEL TESTS IN GROUND EFFECT OF A 35 DEG...][research_aoyagik_hickeydh_1963]
- [SUMMARY OF LAMINAR BOUNDARY LAYER CONTROL RESEARCH, VOLUME 2][research_northropcorphawthornecanorairdiv_1964_b]
- [SUMMARY OF LAMINAR BOUNDARY LAYER CONTROL RESEARCH, VOLUME I][research_northropcorphawthornecanorairdiv_1964]
- [Displacement thickness of the boundary layer with blowing][research_hayasi_1965]
- [LOW DENSITY BOUNDARY LAYER CONTROL BY LIQUID HYDROGEN...][research_macdermott_dix_1965]
- [On boundary-layer control for increasing lift by blowing][research_thomas_1965]
- [Variations of landing distance of fixed-wing aircraft in stol...][research_puvrez_1965]
- [A wing with the maximum lift/drag ratio at supersonic velocity][research_maikapar_1966]
- [FLIGHT TEST EVALUATION OF A DISTRIBUTED SUCTION HIGH-LIFT...][research_roberts_smith_1966]
- [Integration of the equations of a three-dimensional boundary...][research_kozlov_1966]
- [Military and civil all weather landing systems for C-141][research_cannon_1966]
- [The equation of similar profiles in boundary layer theory...][research_watson_1966]
- [XV5A Aircraft Flight Tests Landing Strip Evaluations][research_fenwick_1966]
- [BOUNDARY LAYER CONTROL SYSTEM INSTALLATION FOR THE YCV-2B...][research_cordner_1967]
- [Experimental study of boundary-layer control by blowing on a...][research_grin_1967]
- [XC-142A Aircraft Flight Tests Landing Strip Evaluations][research_fenwick_1967]
- [TWO-DIMENSIONAL BOUNDARY LAYER THEORY WITH STRONG BLOWING][research_elliott_1968]
- [Investigation of a Highly Loaded Two-Stage Fan-Drive Turbine...][research_welna_dahlberg_1969]
- [Laminar boundary-layer control by combined blowing and...][research_anderson_murthy_1969]
- [Minimum weight design of aircraft landing-gear reinforcement...][research_rldha_1969]
- [An approximate solution of the boundary layer equations with...][research_golovin_sergievskii_1970]
- [Quasi-optimum design of an aircraft landing control system][research_ling_1970]
- [Effects of blowing or suction on the laminar boundary layer...][research_fukusako_kiya_1971]
- [The effect of a discontinuity in wall blowing on the...][research_simpson_1971]
- [Acoustic results obtained with upper-surface-blowing...][research_vonglahnu_reshotkom_1972]
- [Breakaway self-similar flows in a laminar magnetohydrodynamic...][research_gotovtsev_1972]
- [Certain solutions of the equations of laminar boundary layer...][research_filimonov_1972]
- [Optimal paths for minimising landing transition distance for...][research_huntley_1972]
- [Simulator evaluation of the flying qualities of externally...][research_kierda_powersbg_1972]
- [Flight Investigation of Various Longitudinal Short-Term...][research_smith_lebacqz_1973]
- [Noise measurements for various configurations of a model of a...][research_goodykoontzjh_wagnerjm_1973]
- [Noise tests of a mixer nozzle-externally blown flap system][research_goodykoontzjh_dorschrg_1973]
- [STOL Tactical Aircraft Investigation, Externally Blown Flap...][research_okumoto_elsanker_1973]
- [Landing aircraft automatically][research_hart_1974]
- [Taylor-Gortler Instability of a Boundary Layer with Suction...][research_kobayashi_1974]
- [The supersonic-hypersonic flow around a circular cone with...][research_carafoli_berbente_1974]
- [Turbulent boundary layer in an incompressible fluid with...][research_lapin_sharov_1974]
- [Boundary Layer and Flow Control by Slot-Blowing Applied to...][research_ueda_tanaka_1975]
- [Circulation Control for High Lift and Drag Generation on STOL...][research_englar_1975]
- [Compatibility of Take-Off and Landing With Mission and...][research_dieterreich_josefwimbauer_1975]
- [Investigation of a compressible turbulent boundary layer in...][research_kuzmich_sekundov_1975]
- [A Control System for the Wind Tunnel Model of a...][research_reader_1976]
- [Boundary Layer and Flow Control by Slot-Blowing Applied to a...][research_ueda_tanaka_1976]
- [Oblique slot blowing into a supersonic laminar boundary layer][research_riley_1976]
- [Supersonic Cone with Surface Blowing][research_carafoli_berbente_1976]
- [Turbulent boundary layer on a permeable surface with...][research_baryshev_leontev_1976]
- [Boundary Layer and Flow Control by Slot-Blowing Applied to...][research_ueda_tanaka_1977]
- [Transition Behavior of a Blasius-Type Boundary Layer...][research_sokolov_karpati_1978]
- [Transonic Shockwave/Turbulent-Boundary-Layer Interaction with...][research_inger_zee_1978]
- [Laminar boundary layer on a partly moving surface in the...][research_gershbein_peigin_1979]
- [The Performance of a Conceptual Vertical Attitude Takeoff and...][research_papadales_basils_1979]
- [USAF Flying Qualities Requirements for a STOL Short Takeoff...][research_gerken_1979]
- [An experimental investigation of three dimensional low speed...][research_shindos_jopparg_1980]
- [Effects of Spanwise Blowing on Two Fighter Airplane...][research_anglin_satran_1980]
- [Development and evaluation of automatic landing control laws...][research_feinreichb_deganio_1981]
- [Experimental investigation of tangential blowing for control...][research_schwendemannmf_1981]
- [Influence of Landing Gear Flexibility on Aircraft Performance...][research_sivaramakrishnan_1981]
- [Influence of blowing on the characteristics of the...][research_kornienko_shmanenkov_1981]
- [A parametric differentiation version with finite-difference...][research_krishnaswamy_nath_1982]
- [Tangential blowing of hydrogen into a turbulent supersonic...][research_gromov_larin_1982]
- [A flight-test and simulation evaluation of the longitudinal...][research_brownsc_hardygh_1983]
- [Stability and control of a supersonic transport airplane...][research_oehmanwi_1983]
- [Tentative STOL Short-Takeoff-and-Landing Flying Qualities...][research_hoh_mitchell_1983]
- [Low-speed aerodynamic characteristics of a wing-canard...][research_banksdanielw_paulsonjohnwjr_1987]
- [Preliminary design of a supersonic Short Takeoff and Vertical...][research_coxbrian_borcherspaul_1990]
- [Shock Wave and Boundary Layer Control for Aero-Optic...][research_smits_miles_2002]
- [Computational Modeling of MEMS Microjets for Turbulent...][research_goldstein_2004]
- [DNS for New Applications of Surface Textures and MEMS...][research_goldstein_2006]
- [Hybrid LES/RANS Simulation of the Effects of Boundary Layer...][research_edwards_2010]
- [Langley Full-scale-tunnel Investigation of Maximum Lift and...][research_lovelljcalvin_wilsonherbertajr_1947]
- [TAKEOFF AND LANDING CAPABILITIES OF THE CARIBOU CV-2B...][research_kidwell_1963]
- [Trailing Vortices of Jet Transport Aircraft during Takeoff...][research_zwieback_1964]
- [Preliminary Measurements of Take-Off and Landing Noise from a...][research_tannercaroles_mcleodnormanj_1965]
- [Measurement of takeoff and landing performance using an...][research_baker_1966]
- [Prediction of off-runway takeoff and landing performance][research_kuchinka_1966]
- [STOL Tactical Aircraft Investigation. Volume 3. Performance...][research_hebert_j_1973]
- [Laser system for aircraft takeoff and landing - "Glissada"][research_basov_berezhnoy_1977]
- [Height of Spray Produced by Vertical Takeoff and Landing VTOL...][research_kuhn_1979]
- [The size and performance effects of high lift system...][research_sullivanrl_1979]

## Dependent Systems

**Every system below is dimensioned against the keystone rather than described for its own sake.** The order
is by dependency, since the engine change drives the fuselage, the fuselage drives the intakes, and the wing
follows from the manoeuvre requirement that the engine change made reachable.

### Propulsion

Treated at length above.
**The summary is that the engine change is the largest single change in the aircraft and the one that drives most of the others.**
It is 33.01 inches longer, 9.84 inches wider, and it swallows 52.9 percent more air. The fuselage stretch,
the redesigned centre and rear fuselage, the enlarged intakes and the translating cones all follow from it.

- [Theoretical evaluation of the ducted-fan turbojet engine][research_parisenrichardb_armstrongjohnc_1948]
- [Supersonic Nozzle Design][research_crown_1950]
- [Investigations of the boundary-layer control on a full scale...][research_rebuffetpierre_poissonquintonph_1952]
- [The Fiat G80 Turbojet Fighter‐Trainer][research_the_fiat_1952]
- [An analytical study of the comparative performance of six...][research_watsonearlc_1953]
- [Analysis of the turbojet engine for propulsion of supersonic...][research_gabrieldavids_krebsrichardp_1953]
- [On the Nonsteady Climb of Turbojet Aircraft][research_miele_1954]
- [Preliminary Data on the Effects of Inlet Pressure Distortions...][research_wallnerlewise_lubickrobertj_1954]
- [Optimum flight paths of turbojet aircraft][research_mieleangelo_1955]
- [PERFORMANCE OF A TURBOJET ENGINE IN COMBINATION WITH AN...][research_andersonbh_bowditchdn_1960]
- [EFFECTS OF XLR-99 ENGINE NOZZLE OPTIMIZATION ON MAXIMUM...][research_eggers_1961]
- [EFFECTS OF EXHAUST NOZZLE RECOMBINATION ON HYPERSONIC RAMJET...][research_franciscuslc_lezbergea_1963]
- [AIR-FILM COOLING OF A SUPERSONIC NOZZLE][research_lieu_1964]
- [HEAVY-LIFT TIP TURBOJET ROTOR SYSTEM. VOLUME 13. PRELIMINARY...][research_hilleraircraftcorppaloaltoca_1965_b]
- [HEAVY-LIFT TIP TURBOJET ROTOR SYSTEM. VOLUME 9. PERFORMANCE...][research_hilleraircraftcorppaloaltoca_1965]
- [Effect of turbofan cycle variables on aircraft cruise...][research_bagby_andersen_1966]
- [High-bypass turbofan cycles for long-range subsonic transports][research_neitzel_hemsworth_1966]
- [PARTIAL ALTITUDE MILITARY QUALIFICATION TEST OF THE TF37-GE-1...][research_evans_chamblee_1966]
- [The Rolls‐Royce Spey Junior Turbofan Engine][research_the_rollsroyce_1967]
- [CALCULATING THE BYPASS RATIO OF A TURBOFAN ENGINE BY USING...][research_coalson_1968]
- [The Rolls‐Royce RB.211 Three Shaft Turbofan][research_the_rollsroyce_1968]
- [The Rolls‐Royce Three Shaft Turbofan Engine][research_wilde_pickerell_1968]
- [Theory and test of flow mixing for turbofan engines][research_hartmann_1968]
- [Turbofan-engine noise suppression][research_pendley_marsh_1968]
- [Gross thrust coefficient - Turbofan engines][research_boytos_1969]
- [Internal thrust and pumping performance of an auxiliary inlet...][research_burleyrr_mansourah_1969]
- [Anatomy of a turbofan engine][research_anatomy_of_1970]
- [Development Testing of the RB.211 Turbofan Engine][research_development_testing_1970]
- [Flight performance of auxiliary inlet ejector and plug nozzle...][research_burleyrr_samanichne_1970]
- [Performance of an auxiliary inlet ejector nozzle with fixed...][research_johnsal_steffenfw_1970]
- [Static performance of an auxiliary inlet ejector nozzle using...][research_burleyrr_mansourah_1970]
- [Supersonic Nozzle Design][research_brodsky_1970]
- [An all turbofan VTOL or STOL intercity transport][research_hill_1971]
- [Comment on "Optimizing the Propulsion/Lift System for...][research_pyle_1971]
- [Correlation of Turbofan Engine Thrust Performance with...][research_lecuyer_morrison_1971]
- [Development of JT8D Turbofan Engine Composite Fan Blades][research_sattar_stargardter_1971]
- [Dynamic performance characteristics of mixed and unmixed...][research_fett_1971]
- [Effect of exit area variation on the performance of an...][research_blahabj_johnsal_1971]
- [Experimental performance and combustion stability of a full...][research_branstetterjr_juhaszaj_1971]
- [Optimizing the Propulsion/Lift System for Turbofan STOL...][research_bowling_hurkamp_1971]
- [Engine selection for transport and combat aircraft][research_duganjfjr_1972]
- [Experimental evaluation of a TF30-P-3 turbofan engine in an...][research_mcaulayje_abdelwahabm_1972]
- [Small-scale tests of the mixer nozzle concept for reducing...][research_goodykoontzjh_olsenwa_1972]
- [An Altitude Test Facility for Large Turbofan Engines][research_ashwood_1973]
- [Dynamic Modeling of High Bypass Ratio Turbofan Engines][research_breaks_1973]
- [Experimental cold-flow evaluation of a ram air cooled plug...][research_straightdm_harringtonde_1973]
- [Model Induction Test Facility Capability for Testing Turbofan...][research_hale_1973]
- [Assessment of an analytical procedure for predicting...][research_andersonbh_1974]
- [Chronology and Analysis of the Development of Altitude...][research_tate_gillard_1975]
- [Altitude performance of a low-noise-technology fan in a...][research_biesiadnytj_greyre_1976]
- [Fan Noise from Turbofan Engines][research_feiler_conrad_1976]
- [Performance Correction Models for Advanced Turbofan Engines][research_coalson_csavina_1976]
- [Conceptual design of single turbofan engine powered light...][research_snyderfs_voorheescg_1977]
- [Core Noise Measurements on a YF-102 Turbofan Engine][research_reshotko_karchmer_1977]
- [Jet Noise Characteristics of Unsuppressed Duct Burning...][research_packman_kozlowski_1977]
- [Canard configured aircraft with 2-D nozzle][research_childrd_hendersonwp_1978]
- [Ground Effects on Lift for Turbofan Powered-Lift STOL Aircraft][research_campbell_hassel_1978]
- [Numerical Modeling of Three-Dimensional Flows in Turbofan...][research_birch_paynter_1978]
- [Wind Tunnel Results from a Nozzle Afterbody Test of A...][research_lucas_1978]
- [Analytical study of the effects of wind tunnel turbulence on...][research_gliebepr_kerschenej_1979]
- [Design and Verification of a Turbofan Swirl Augmentor][research_egan_shadowen_1979]
- [High Bypass Turbofan Component Development. Phase II. Fan...][research_chapman_1979]
- [Vectoring Nonaxisymmetric Nozzle Jet Induced Effects on a...][research_schnell_grossman_1979]
- [Analytical study of the effects of wind tunnel turbulence on...][research_gliebepr_1980]
- [High Bypass Turbofan Component Development. Amendment I...][research_mauch_oldakowski_1980]
- [High Bypass Turbofan Component Development. Modification 2][research_armstrong_palladino_1980]
- [Analytical Study of the Effects of Wind Tunnel Turbulence on...][research_gliebe_1981]
- [Effects of fan inlet temperature disturbances on the...][research_abdelwahabm_1981]
- [Experimental Modeling of Unstalled Supersonic Turbofan Flutter][research_riffel_fleeter_1981]
- [Flight and Wind-Tunnel Test Results of a Mechanical Jet Noise...][research_fitzsimmons_mckinnon_1981]
- [Pratt and Whitney PW2037 Turbofan][research_cowles_1981]
- [Propulsive Aerodynamics of an Advanced Nozzle/Forward Swept...][research_bowers_1981]
- [Unsteady fan blade pressure and acoustic radiation from a...][research_preisserjs_schoensterja_1981]
- [Establishing Cruise-Engine Cycle Payoffs for a Supersonic...][research_cyrus_piscopo_1982]
- [Effects of varying podded nacelle-nozzle installations on...][research_caponefj_reubushde_1983]
- [Ejector nozzle test results at simulated flight conditions...][research_nelsondp_bresnahandl_1983]
- [Model aerodynamic test results for a refined actuated inlet...][research_nelsondp_1983]
- [Effects of Test Cell Recirculation on High-Bypass Turbofan...][research_dugas_1986]
- [The supersonic through-flow turbofan for high Mach propulsion][research_franciscusleoc_1987]
- [Interference effects of very high bypass ratio nacelle...][research_ingraldianthonym_rerichardj_1991]
- [Internal performance of a hybrid axisymmetric/nonaxisymmetric...][research_taylorjohng_1991]
- [The effects of compressor seventh-stage bleed air extraction...][research_evansalisonb_1991]
- [Turbofan engine demonstration of sensor failure detection][research_merrillwalterc_delaatjohnc_1991]
- [Acoustic Mode Measurements in the Inlet of a Model Turbofan...][research_heidelberglaurencej_halldavidg_1992]
- [Effects of bleed air extraction of thrust levels on the...][research_yuhasandrewj_rayronaldj_1992]
- [Effects of bleed air extraction on thrust levels on the...][research_yuhasandrewj_rayronaldj_1992_b]
- [Installation effects of wing-mounted turbofan nacelle-pylons...][research_pendergraftodiscjr_ingraldianthonym_1992]
- [Acoustic mode measurements in the inlet of a model turbofan...][research_heidelberglaurencej_halldavidg_1993]
- [An Integration of the Turbojet and Single-Throat Ramjet][research_trefnycj_bensontj_1995]
- [Interactive Educational Tool for Turbofan and Afterburning...][research_bensonthomasj_1997]
- [Assessment of Integrated Nozzle Performance][research_lamberthh_mizukamim_1999]
- [Installed Transonic 2D Nozzle Nacelle Boattail Drag Study][research_malonemichaelb_peaveycharlesc_1999]
- [Advanced Methods for Aircraft Engine Thrust and Noise...][research_gilinskymikhail_morganmorrish_2000]
- [KLIN Cycle Engine - Deeply Cooled Turbojet DCTJ Engine...][research_airforceresearchlabedwardsafbca_2000]
- [The Performance of a Subsonic Diffuser Designed for High...][research_biesiadnythomasj_wendtbrucej_2004]
- [Sea Level Operation Demonstration of F404-GE-400 Turbofan...][research_chippa_2010]
- [Altitude Performance of a Turbojet Engine Using Pentaborane...][research_sivojosephn_1957]
- [The Thrust of a Supersonic Conical Nozzle with Non-Isentropic...][research_rowe_1958]
- [HEAVY-LIFT TIP TURBOJET ROTOR SYSTEM. VOLUME 10. STABILITY...][research_hilleraircraftcorppaloaltoca_1965_c]
- [Detection of oblique shocks in a conical nozzle with a...][research_backlh_cuffelrf_1966]
- [Flight investigation of airframe installation effects on an...][research_burleyrr_1971]
- [Prediction of Installed Nozzle Flowfields][research_presz_konarski_1971]
- [Solution of the variational problem of shaping a nozzle to...][research_rylov_1974]
- [On the Conventional Definitions of Thrust/Drag of an Aircraft...][research_cassetti_1978]
- [Numerical Solution of a Supersonic Nozzle Afterbody Flow with...][research_mikhail_1979]
- [Two-Component Simultaneous LDV Laser Doppler Velocimeter...][research_heltsley_crosswy_1983]
- [Performance Off-Design Cycle Analysis for a Turbofan Engine...][research_liewkh_uripe_2005]
- [Calibration for Thrust and Airflow Measurements in the CE-22...][research_wernerrogera_wolterjohnd_2010]

#### Ram Drag, Which the Draft Did Not Mention and the Keystone Needs

**An engine at high Mach spends a large part of its gross thrust cancelling the momentum of the air it swallowed.**
Net thrust is the difference between what leaves and what arrived.

**The literature under this heading is genuinely thin and the reason is worth stating.** Of 6,518 records
harvested for this article, thirteen carry ram drag, momentum drag or installed performance in their titles,
and nine of those are cited here. **The subject is not thin. The heading is.** Thrust and drag bookkeeping
is settled inside the papers on inlet additive drag and spillage already cited above, because deciding what
counts as inlet drag and what counts as lost thrust is the same accounting question.

- [The Propulsive Efficiency and Best Division of Power in an...][research_stephenson_1953]
- [Measurement of net thrust in flight][research_davidson_1964]
- [PROPULSIVE EFFICIENCY OF MAN IN THE SEA][research_taggart_1966]
- [Propulsive efficiency of breaststroke and freestyle swimming][research_holmr_1974]
- [Propulsive efficiency from an energy utilization standpoint][research_lewis_1976]
- [A new method for flight test determination of propulsive...][research_bullg_bridgespd_1983]

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
relations below are mostly period work.

- [The Effect of Horizontal Variations in Center of Gravity...][research_jenney_1935]
- [A Simplified Analysis of Static Longitudinal Stability][research_reid_1937]
- [Report no. 609, Experimental investigation of wind-tunnel...][research_report_no_1937]
- [Wind-tunnel interference with particular reference to...][research_silversteinabe_whitejamesa_1937]
- [Report No. 648, Design charts for predicting downwash angles...][research_report_no_1939]
- [Estimation of Static Longitudinal Stability][research_archbold_1945]
- [Calculation of Downwash Behind a Supersonic Wing][research_ward_1949]
- [The Calculation of Supersonic Downwash Using Line Vortex...][research_harold_haefeli_1950]
- [Theoretical Analysis of the Downwash Distribution Over...][research_hazen_seckel_1950]
- [The Rolling Up of the Trailing Vortex Sheet and Its Effect on...][research_spreiter_sacks_1951]
- [Downwash Behind a Two-Dimensional Wing Oscillating in...][research_lapin_crookshanks_1952]
- [Investigation of the Influence of Fuselage and Tail Surfaces...][research_birdjohnd_lichtensteinjacobh_1952]
- [SUPERSONIC THEORY OF DOWNWASH FIELDS][research_leslie_1952]
- [The Measurement of Downwash and Sidewash Behind a Rectangular...][research_davis_1952]
- [A Method for Estimating the Rolling Moments Caused by...][research_edwardssherman_hikidokatsumi_1953]
- [A method for calculating the lift and center of pressure of...][research_nielsenjackn_kaattarigeorgee_1953]
- [Further Note on the Use of the Neutral Point as a Stability...][research_deitchman_1953]
- [On the Use of the Neutral Point as a Stability Parameter][research_baron_1953]
- [A Note on the Evaluation of the Supersonic Downwash Integral][research_hunn_1954]
- [An Empirical Method for Correction of a Wing Downwash Field...][research_deitchman_1954]
- [STATIC STABILITY AND MAGNUS CHARACTERISTICS OF THE 5-INCH...][research_greene_1955]
- [STATIC STABILITY AND MAGNUS CHARACTERISTICS OF A LOW-DRAG...][research_greene_1956]
- [The Effect of Wing Plan Form on the Downwash behind Wings][research_mitsuyasu_1956]
- [Comparison of Experimental and Theoretical Zero-Lift...][research_petersenrb_1957]
- [STATIC STABILITY AND MAGNUS CHARACTERISTICS OF THE U.S. NAVY...][research_greene_1957]
- [The Transient Downwash Resulting From the Encounter of an...][research_hobbs_1957]
- [Wind-Tunnel Investigation of Some Effects of Wing Sweep and...][research_fisherlewisr_williamsjamesl_1958]
- [A Buffet Investigation at High Subsonic Speeds of...][research_suttonfredb_1959]
- [A Transonic Wind-Tunnel Investigation of the Performance and...][research_bielatralphp_1959]
- [The downwash of the flow behind the swept vortex of finite...][research_biriukov_1959]
- [STATIC STABILITY AND DRAG OF THE HOPI WEAPON][research_carroll_1960]
- [Hovering Static Stability and Performance Experiments on...][research_carmichael_mcnay_1961]
- [INVESTIGATION OF STATIC STABILITY AND AERODYNAMIC EFFECTS OF...][research_anderson_1961]
- [Aerodynamic Processes in the Downwash-Impingement Problem][research_vidal_1962]
- [Corrections and Comments on "Aerodynamic Processes in the...][research_vidal_1963]
- [STATIC STABILITY TESTS ON A 0.098 SCALE STANDARD LAUNCH...][research_ziegler_1963]
- [DOWNWASH IMPINGEMENT DESIGN CRITERIA FOR VTOL AIRCRAFT][research_george_perlmutter_1964]
- [Comment on "The Neutral Point in Stability and Control...][research_roache_1965]
- [DOWNWASH TESTS OF THE DUAL TANDEM DUCTED PROPELLER VTOL...][research_curtiss_hc_1965]
- [LIFT, DRAG, AND STATIC STABILITY OF A BLUNT CONICAL MODEL IN...][research_boylan_1965]
- [The neutral point in stability and control analysis][research_rodgers_1965]
- [Relationship between the neutral point, maneuver point, and...][research_rodgers_1966]
- [Static stability characteristics at Mach numbers from 1.90 to...][research_fullerde_1967]
- [BOATTAIL EFFECTS ON STATIC STABILITY AT SMALL ANGLES OF ATTACK][research_washington_pettis_1968]
- [LIFTING SURFACE THEORY AND TAIL DOWNWASH CALCULATIONS FOR...][research_levinsky_thommen_1968]
- [Model experiments of soil erosion by V.T.O.L. aircraft...][research_barton_edwards_1968]
- [The Static Stability of a Cone-Cylinder Flare and Two...][research_mathur_1969]
- [Contrails and aircraft downwash][research_scorer_davenport_1970]
- [Downwash correction for a two-dimensional finite wing][research_ness_1971]
- [Effects of Modifying a Rotor Tip Vortex by Injection on...][research_rinehart_1971]
- [Maneuver Load Control and Relaxed Static Stability Applied to...][research_anderson_berger_1973]
- [Effect of canard location and size on canard-wing...][research_glossbb_1974]
- [Rotor Downwash Velocities about the UH-1M Helicopter - Flight...][research_jenkins_marks_1975]
- [Static stability and aperiodic divergence][research_sachs_1975]
- [Static Stability Characteristics of the MK-82/84...][research_paulk_anderson_1976]
- [A new concept of static stability and its flight testing in...][research_sachs_1977]
- [Static Stability and Drag Effects of Various External Store...][research_whoric_1977]
- [Downwash and induced drag corrections for a lifting wing at...][research_bera_1980]
- [Effect of downwash on the induced drag of canard-wing...][research_butler_1982]
- [Volume II. Flying Qualities Phase. Chapter 5 Longitudinal...][research_airforcetestpilotschooledwardsafbca_1990]
- [Volume II. Flying Qualities Phase. Chapter 7...][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Modeling of Longitudinal Unsteady Aerodynamics of a Wing-Tail...][research_kleinvladislav_1999]
- [Estimation of Longitudinal Unsteady Aerodynamics of a...][research_murphypatrickc_kleinvladislav_2006]

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

- [Analysis and prediction of longitudinal stability of airplanes][research_gilruthrr_whitemd_1941]
- [Calculated effects of full-span slotted and Fowler flaps on...][research_goransonrfabian_1942]
- [Power-On Longitudinal-Stability and Control Tests of the...][research_tollthomasa_1942]
- [Preliminary Flight Research on an All-Movable Horizontal Tail...][research_klecknerharoldf_1945]
- [Flight Tests of an All-movable Horizontal Tail with Geared...][research_klecknerharoldf_1946]
- [Dynamic Longitudinal Stability and Control Flight Tests of a...][research_cornellaeronauticallabincbuffalony_1947]
- [Flight investigation of a combined geared unbalancing-tab and...][research_mungallrobertc_1948]
- [Longitudinal Stability Characteristics of a 42 Degree...][research_spoonerstanleyh_martinaalbertp_1948]
- [Longitudinal Stability of Autopilot-Controlled Aircraft][research_vazsonyi_1950]
- [Longitudinal Stability, Speed and Height][research_neumark_1950]
- [The Longitudinal Stability, Control Effectiveness, and...][research_niewaldroyj_moulmartint_1950]
- [A flight evaluation of the longitudinal stability...][research_andersonsethb_brayrichards_1951]
- [Longitudinal Stability Fundamentals][research_wisniewski_1951]
- [Note on "Longitudinal Stability of Autopilot-Controlled...][research_sissingh_1951]
- [Wind-tunnel investigation of the effects of horizontal-tail...][research_queijomj_wolhartwalterd_1951]
- [Experimental Determination of the Effect of Horizontal-Tail...][research_lichtensteinjacobh_1952]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]
- [Low-Speed Longitudinal Stability Characteristics of a...][research_sleemanwilliamc_byrnesandrewl_1953]
- [TANDEM HELICOPTER LONGITUDINAL STABILITY AND CONTROL][research_gebhard_1953]
- [Low-Speed Longitudinal Stability and Lateral-Control...][research_bollechthomasv_kellyhneale_1954]
- [Wind-Tunnel Investigation at Low Speed of the Effects of...][research_queijomj_jaquetbyronm_1954]
- [Wind-Tunnel Investigation at Subsonic and Supersonic Speeds...][research_smithwilliardg_1954]
- [A Flight Evaluation of the Longitudinal Stability...][research_andersonsethb_brayrichards_1955]
- [Wind-tunnel Investigation at Subsonic and Supersonic Speeds...][research_wetzelbentone_1955]
- [AUTOMATIC FLIGHT CONTROL SYSTEMS FOR PILOTED AIRCRAFT][research_hart_1956]
- [Full-scale Wind-tunnel Tests of the Longitudinal Stability...][research_hickeydavidh_1956]
- [Helicopter Longitudinal Stability][research_payne_1957]
- [Investigation at High Subsonic Speeds of the Static...][research_sleemanwilliamcjr_1957]
- [Longitudinal and Lateral Stability and Control...][research_drivercornelius_1958]
- [Low-Speed Investigation Of The Effects Of Horizontal-Tail...][research_hayeswcjr_sleemanwcjr_1959]
- [Static Longitudinal Stability and Control Characteristics of...][research_petersonvictorl_meneesgenep_1959]
- [LONGITUDINAL STABILITY AND CONTROL CHARACTERISTICS OF A...][research_kayser_hillsamer_1960]
- [Investigation at High Subsonic Speeds of the Use of Low...][research_sleemanwilliamcjr_1961]
- [Static Longitudinal Stability and Control Characteristics at...][research_fostergv_robinsonrb_1961]
- [A systematic study of the factors contributing to post-stall...][research_rayej_taylorrt_1965]
- [A parametric study of factors influencing the deep-stall...][research_powersbg_1966]
- [AN ANALYTICAL STUDY OF FACTORS INFLUENCING THE LONGITUDINAL...][research_beppu_curtiss_1966]
- [Low-speed wind-tunnel studies relating to pitch-up on a...][research_lockwoodve_1966]
- [Effect of supersonic interference on lateral stability of...][research_hart_1968]
- [Elastic wind-tunnel models for predicting longitudinal...][research_roskam_holgate_1968]
- [A method for predicting longitudinal stability derivatives of...][research_roskam_dusto_1969]
- [An Investigation of the Dynamic Stability Characteristics of...][research_curtiss_howardc_1969]
- [A new model performance index for engineering design of...][research_whitaker_rediess_1970]
- [Aircraft Flight Control Systems with Optimally Selected...][research_mclean_stacey_1970]
- [Longitudinal Stability Characteristics of a Series of...][research_brazzel_henderson_1970]
- [Space shuttle IRLV straight wing orbiter model 130c...][research_mennellr_1970]
- [Concorde Automatic Flight Control System][research_concorde_automatic_1971]
- [Position of the thrust line and longitudinal stability][research_katz_1971]
- [Recent Experience with Techniques for Prediction of Spin...][research_chambers_bowman_1971]
- [Space shuttle Effects of horizontal tail geometry and...][research_popeha_1971]
- [Formulations of the Equations of Motion of an Elastic...][research_schwanz_1972]
- [Effect of Various External Stores on the Static Longitudinal...][research_whoric_1973]
- [In-Flight Simulation of Minimum Longitudinal Stability for...][research_wasserman_mitchell_1973]
- [Preliminary Criteria for Predicting Departure...][research_weissman_1973]
- [Digital Flight Control System for Tactical Fighter. Volume 1...][research_konar_mahesh_1974]
- [Digital adaptive model following flight control][research_alaggs_kaufmanh_1974]
- [Effect of Upper-Surface Blowing on Static Longitudinal...][research_coe_kulla_1974]
- [Identification of the Longitudinal Stability and Control...][research_eulrich_mesiah_1974]
- [Three-Axis Fluidic/Electronic Automatic Flight Control System...][research_cotton_1974]
- [Use of short period frequency requirements in horizontal tail...][research_moorhouse_jenkins_1975]
- [Current status of longitudinal stability, 24 May 1948][research_donlancj_1976]
- [New MIL-F-9490D Requirements and Implications on Future...][research_townsend_blatt_1976]
- [Propulsion system/flight control integration for supersonic...][research_reukaufpj_burchamfwjr_1976]
- [Recent research related to prediction of stall/spin...][research_nguyenlt_anglinel_1976]
- [Impact of CCV Requirements on Flight Control System Design][research_boudreau_1977]
- [Validation of MIL-F-9490D - General Specification for Flight...][research_dobosbubno_hartsook_1977]
- [Aerodynamic Characteristics of Fighter Configurations During...][research_anglin_1978]
- [Analysis of Digital Flight Control Systems with Flying...][research_whitbeck_hofmann_1978]
- [Flight Verification of the Advanced Flight Control Actuation...][research_demarchi_haning_1978]
- [Influence of Ballonet Motions on the Longitudinal Stability...][research_delaurier_1980]
- [Departure susceptibility and uncoordinated roll-reversal...][research_bihrle_barnhart_1982]
- [Preliminary performance of a vertical-attitude takeoff and...][research_robinsaw_beissnerfljr_1985]
- [An experimental study of the lift, drag and static...][research_ostowaric_naikd_1986]
- [The effects of canard-wing flow-field interactions on...][research_muchmorecbjr_1988]
- [Volume II. Flying Qualities Phase. Chapter 14 Flight Control...][research_airforcetestpilotschooledwardsafbca_1988]
- [Schleicher ASK - 21 Glider TG-9 Stall and Spin Evaluation][research_janzen_precourt_1989]
- [Volume II. Flying Qualities Phase. Chapter 9 Roll Coupling][research_airforcetestpilotschooledwardsafbca_1989]
- [ACSYNT inner loop flight control design study][research_bortinsrichard_sorensenjohna_1993]
- [Optimal nonlinear estimation for aircraft flight control in...][research_mulgundsandeeps_1994]
- [Computational Fluid Dynamics Study for a Deep Stall Air...][research_ramamurti_2011]
- [Theory, Guidance, and Flight Control for High Maneuverability...][research_fresconi_celmins_2014]
- [Longitudinal Stability in Aeroplanes][research_bryant_1933]
- [Longitudinal Stability][research_crowe_1937]
- [Longitudinal Stability and Control][research_gates_1940]
- [Wind-Tunnel Investigation of Effects of Unsymmetrical...][research_purserpaule_spearmargaretf_1947]
- [Longitudinal Stability Characteristics of a 1/40-Scale Model...][research_craneharoldl_beckhardtarnoldr_1948]
- [Longitudinal-stability Investigation of High-lift and...][research_fostergeraldv_fitzpatrickjamese_1948]
- [Preliminary Results of an Investigation by the Wing-Flow...][research_craneharoldl_1948]
- [Static Longitudinal Stability of a Tandem-Coupled...][research_hewesdonalde_1950]
- [An analysis of the effects of aeroelasticity on static...][research_skoogrichardb_1951]
- [Aircraft Wake Flow Effect and Horizontal Tail Buffet][research_hwang_pi_1979]
- [Assessment of propeller influence on lateral-directional...][research_vanrooyen_eshelby_1981]
- [Performance improvements of an F-15 airplane with an...][research_myerslawrencep_walshkevinr_1988]
- [A New Approach to Prediction of Aircraft Spin][research_squires_2002]

### Structure and Materials

The airframe is aluminium alloy, and the analysis above establishes that this is the constraint the Mach 2.6
objective runs into. **At Mach 2.0 the structure is comfortable and at Mach 2.6 it is not**, and the
transition happens across a narrow band because the recovery temperature goes as the square of the Mach
number while the strength curve falls steeply through the same range.

### Armament and Stores

Nine stations, one on the fuselage centreline, three under each wing and one at each wingtip. The gun is the
20 millimetre [M61][ref_m61] with 725 rounds, with a 30 millimetre [DEFA][ref_defa] offered as an
alternative for customers already equipped for it. Up to 12,000 pounds of ordnance on short-range missions,
a maximum of four [AIM-7][ref_aim7] or typically six and up to ten [AIM-9][ref_aim9].

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

This section exists because the genre requires it and because its emptiness is the most important fact about
the subject. **No X-27 was built. No CL-1200 was built. Nothing flew.**

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
| Initial climb 60,000 ft/min | Best sea-level $P_s$ 48,585 ft/min | **Claim exceeds the estimate by 23.5 percent** |
| Takeoff run 1,450 ft | 1,078 ft at $C_{L_{\max}}$ 1.2 | Claim is conservative |
| Combat radius 367 nmi | 0.171 of still-air range | Consistent with practice |
| Fuel increase 46 percent | Weights imply 29 to 33 percent | **Mild internal inconsistency** |
| Spike travel 4 in | Implies 5.401 ft² against 5.639 ft² needed | **Agrees to 4.2 percent** |

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

**The claim exceeds the computed ceiling by 21.6 percent.**

**That figure is a correction.** An earlier version of this article evaluated $P_s$ on a four-point grid and
reported the peak as 48,585 feet per minute at Mach 1.2, giving a 23.5 percent shortfall. A fine scan puts
the maximum at Mach 1.095, so the shortfall is smaller than first stated.
**The independent checker did not catch it because its tolerance on that value was three percent and the error was one and a half**,
which is a tolerance wide enough to hide the quantity it was checking.

**Two explanations fit and the article cannot choose between them.** The figure may be a zoom rather than a
steady climb, in which case it is a transient trade of speed for height and is not a rate of climb in the
sense the ceiling applies to. Quoted climb figures for fighters of this era are often exactly that.
Alternatively the thrust or weight assumptions here are conservative.
**What can be said is that the figure is not supported by the aircraft's own published thrust and weight under a steady interpretation**,
and that this is the only headline claim in the brochure of which that is true.

### The Fuel Claim, Inverted

The record states a 46 percent increase in internal fuel from a 30-inch stretch. The weight breakdown can be
asked whether it agrees.

$$ W_{\mathrm{fuel,\ clean}} = W_{\mathrm{loaded}} - W_{\mathrm{empty}} = 24{,}385 - 16{,}640 = 7{,}745\ \mathrm{lb} $$

The F-104G holds 896 United States gallons internally, which is 3,392 litres.

| Fuel density | F-104G fuel | Implied Lancer increase | Claimed |
|---|---|---|---|
| 6.5 lb/gal | 5,824 lb | +33.0 percent | 46 percent |
| 6.7 lb/gal | 6,003 lb | +29.0 percent | 46 percent |

Read the other way, applying the claimed 46 percent to the F-104G's tankage and adding the empty weight
gives 25,143 pounds against a quoted normal loaded weight of 24,385, an overshoot of 3.1 percent.

**This is a mild inconsistency and it is reported as one.** Brochure figures of this vintage carry rounding,
the two numbers may refer to volume and weight respectively, and a three percent disagreement is close to
the resolution of the source material.
**It is recorded because reporting the small disagreements is what makes the large agreement in the inlet section credible.**

### The Takeoff Claim, Which Is Conservative

The ground roll is not taken from a rule of thumb. The acceleration is integrated from rest to lift-off
against thrust, drag, and the rolling friction on whatever weight the wing is not yet carrying, following
the method in [Raymer][book_raymer].

Takeoff and landing ground-run prediction is a small and practical literature, and the period work is where
the friction coefficients and the lift-off margins used here come from.

- [NOISE CONTROL FOR AIRCRAFT ENGINE TEST CELLS AND GROUND...][research_doelling_bolt_1961]
- [ESTIMATION OF TAKEOFF GROUND-RUN DISTANCES FOR JET-PROPELLED...][research_linnell_1963]
- [Takeoff performance of jet-propelled conventional and...][research_krenkel_salzman_1968]
- [Landing and Takeoff Roll-Out Augmentation][research_muehter_1974]
- [Airworthiness and Flight Characteristics Test, OV-1C Takeoff...][research_smith_yamakawa_1979]
- [Propagation of aircraft ground run-up noise including the...][research_chessell_1979]
- [Take-off ground roll of propeller driven aircraft][research_hawks_1982]
- [Short Takeoff Performance Using a Gravity Assist Ski Jump][research_furey_1983]

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

An earlier attempt at this check produced 27 nautical miles against a claim of 367, which looked devastating
and was a defect in the checker.
**A discrepancy near an order of magnitude is a hint that the checker is at fault**, exactly as a
suspiciously clean factor is, and it was.

The [Breguet range equation][ref_breguet] carries no gravitational constant when the specific fuel
consumption is quoted per hour, because such a figure is already a weight of fuel per unit thrust per unit
time.

$$ R = \frac{V}{c_t}\,\frac{L}{D}\,\ln\frac{W_0}{W_1} $$

The Breguet relation and the mission bookkeeping around it are as given in [Raymer][book_raymer] and
[Nicolai][book_nicolai]. The end weight is the start weight less the usable fraction of the fuel, and the
ratio is what the logarithm acts on.

$$ W_1 = W_0 - f\,W_{\mathrm{fuel}} = 35{,}000 - 0.85 \times 14{,}360 = 22{,}794\ \mathrm{lb} $$

$$ \frac{W_0}{W_1} = \frac{35{,}000}{22{,}794} = 1.5355 $$

The mission factor is then a defined ratio rather than a rule of thumb, and quoting it is what keeps a
Breguet integral from being mistaken for a mission.

$$ k_m = \frac{R_{\mathrm{combat}}}{R_{\mathrm{still\,air}}} = \frac{367}{2{,}141} = 0.171 $$

| $L/D$ | $c_t$ | Still-air range | The 367 nmi claim as a fraction |
|---|---|---|---|
| 6.0 | 0.85 /h | 1,606 nmi | 0.229 |
| 7.0 | 0.85 /h | 1,873 nmi | 0.196 |
| 8.0 | 0.85 /h | 2,141 nmi | 0.171 |
| 9.0 | 0.85 /h | 2,408 nmi | 0.152 |

**A combat radius is not half a range.** It pays for climb, descent, a combat allowance at maximum power,
reserves, and an outbound leg flown with stores hung on it. The ratio runs about 0.15 to 0.25 in practice.
**The claim lands inside that band and is therefore credible.**

**This is a negative result for a suspicion the article started with, and it is reported as such.**

## What the Data Changed

**Nothing, because there was no data.**

That sentence is the finding rather than an admission. Every other article in this series can point to a
measurement that entered the literature.
**This one cannot, and the reason is worth stating: the programme was cancelled at precisely the point where it would have begun producing evidence.**

What the *programme* changed is a different question and the answer is small but not zero.

- **It did not influence the F-15.** No evidence connects the Lancer to any F-15 design decision.
- **It did not influence the Lightweight Fighter programme technically**, though it demonstrates that
  the argument for funding lightweight-fighter prototypes was in the air before that programme existed.
- **It produced no literature.** This is the second consecutive article in the series to report that,
  and the third in which the subject generated no development literature because nothing was developed.

The literature on procurement, competitive prototyping, export fighters and acquisition policy is where this
programme's traces actually survive.

- [ANALYSIS OF MILITARY ASSISTANCE PROGRAM. PART 3. APPENDIX B...][research_whitson_bartimo_1950]
- [Procurement of Regular Medical Officers][research_mcdonough_1953]
- [Conflicts in Military Procurement][research_gordon_1960]
- [The Ordance Department Procurement and Supply][research_morgan_thomson_1961]
- [ADVANCED LAND NAVIGATION DEVELOPMENT AND EVALUATION OF A...][research_powers_1964]
- [Procurement Problems Affecting Para-Medical Personnel in the...][research_longest_1964]
- [Buying Aircraft Materiel Procurement for the Army Air Forces][research_higham_holley_1966]
- [Report and discussion on “Some aspects of military aircraft...][research_report_and_1966]
- [Some Aspects of Military Aircraft Procurement][research_beesly_1966]
- [The 1966 Lord Sempill memorial paper Some aspects of military...][research_beesly_1966_b]
- [Preparation and Utilization of Military Assistance Officers][research_graham_1969]
- [The Organization of a Military Procurement Function][research_farrer_1969]
- [Military Manpower Procurement in Australia][research_forward_1970]
- [Procurement Techniques to Reduce Military Systems' Costs][research_gansler_1972]
- [Rational Drug Procurement or Caveat Emptor?][research_pflag_1972]
- [The Draft and Public Policy Issues in Military Manpower...][research_kennedy_gerhardt_1972]
- [The Draft and Public Policy Issues in Military Manpower...][research_jacobs_1973]
- [The Foreign Area Officer Program. Volume II. Implications of...][research_sizemore_jr_1973]
- [The financing of aircraft procurement][research_sowter_1973]
- [Military Hardware Procurement Some Comparative Observations...][research_herold_mahoney_1974]
- [Military Procurement][research_cary_walker_1974]
- [Comparison of Military and Commercial Design-To-Cost Aircraft...][research_carlyle_1976]
- [Military Manpower Procurement A Policy Analysis. By Steven B...][research_wamsley_1976]
- [The Acquisition and Retention of Visual Aircraft Recognition...][research_baldwin_cliborn_1976]
- [Zoster Immune Plasma Procurement in Military Hospitals A...][research_fisher_1977]
- [Acquisition Cost Estimating Using Simulation][research_parrish_jr_1978]
- [Future Procurement of Medical Talent for the Federal Medical...][research_custis_1978]
- [Reliability, Maintainability, Strategic Reliability, and Life...][research_klimowitch_1978]
- [Convergent vs. Conflicting Interests in Processes of...][research_harle_1979]
- [Military Manpower Procurement From Conscription to a...][research_mushkat_1979]
- [A Community of Interests NATO and the Military Assistance...][research_kaplan_1980]
- [Department Of The Air Force Washington Dc 1980][research_departmentoftheairforcewashingtondc_1980]
- [Procurement Process Geared Up for New Airplanes][research_procurement_process_1980]
- [An Acquisition Strategy Comparison Model ASCM . Volume 1...][research_cox_bohn_1982_b]
- [An Acquisition Strategy Comparison Model ASCM . Volume 2...][research_cox_bohn_1982]
- [Department of the Air Force Justification of Estimates for...][research_stuart_1982]
- [International Arms Procurement New Directions and Estimating...][research_carey_1982]
- [A Program Manager's Acquisition Strategy Guide][research_wickert_1985]
- [Department Of The Navy Washington Dc 1985][research_departmentofthenavywashingtondc_1985]
- [A Finite Element Expert System an Initial Study and Prototype...][research_morris_1986]
- [Procurement Source Selection Administration][research_armymaterielcommandalexandriava_1987]
- [The Role of Learning Strategies in Second Language...][research_omalley_chamot_1987]
- [Department Of The Navy Washington Dc 1988][research_departmentofthenavywashingtondc_1988]
- [History of the KC-10A Aircraft Acquisition][research_holubik_1988]
- [The V-22 Program's Need for a More Flexible and Farsighted...][research_bacon_1988]
- [Competitive Weapon Systems Acquisition Myths and Facts][research_boger_greer_1989]
- [Strategy for Educating the Department of Defense Acquisition...][research_greebler_suarez_1989]
- [A Cost-Reduction Strategy for Weapon System Acquisition][research_cloos_nelson_1990]
- [Analyses of a Coproduction Acquisition Strategy for the Light...][research_shafer_junghans_1990]
- [Competition in Weapon Systems Acquisition Cost Analyses of...][research_boger_nussbaum_1990]
- [Demand Based Initial Spares Cost Estimating in Early...][research_dement_1990]
- [Department Of The Army Washington Dc 1990][research_departmentofthearmywashingtondc_1990]
- [Joint Service Acquisition An Essential Strategy Fundamentally...][research_lyga_1990]
- [Strategy and Mechanisms for Encouraging Reuse in the...][research_baldo_will_1990]
- [Department Of The Navy Washington Dc 1991][research_departmentofthenavywashingtondc_1991]
- [The Army Acquisition Corps as an Attractive and Competitive...][research_knight_1991]
- [A Strategy Balancing Act The Peacekeeper Rail Garrison...][research_crossey_1992]
- [Department Of The Air Force Washington Dc 1994][research_departmentoftheairforcewashingtondc_1994]
- [Acquisition Strategy Guide][research_mcdaniel_bull_1995]
- [Department Of The Army Washington Dc 1995][research_departmentofthearmywashingtondc_1995_b]
- [Department Of The Air Force Washington Dc 1995, Department of the Air Force, Comm][research_departmentoftheairforcewashingtondc_1995]
- [Department Of The Army Washington Dc 1995][research_departmentofthearmywashingtondc_1995]
- [Joint Logistics Commanders Guidance for Use of Evolutionary...][research_alberts_1995]
- [The Next Generation Munitions Handler Prototype Acquisition...][research_leahy_michaelb_1995]
- [Defense Acquisition Univ Alexandria Va 1996, Acquisition Review quarterly Vol][research_defenseacquisitionunivalexandriava_1996]
- [Department Of The Army Washington Dc 1996][research_departmentofthearmywashingtondc_1996]
- [Defense Acquisition Univ Alexandria Va 1997][research_defenseacquisitionunivalexandriava_1997]
- [Design of a Windblast Data Acquisition System][research_crothers_1997]
- [Foreign Military Assistance Act Report to Congress Authorized...][research_departmentofdefensewashingtondc_1997]
- [Military Assistance to Civil Authorities][research_wauchop_1997]
- [Acquisition Strategy Guide, Third Edition][research_mcdaniel_bull_1998]
- [CBT Data /Knowledge Acquisition Using Knowledge Objects to...][research_muraida_grimes_1998]
- [Department Of The Army Washington Dc 1998, Department of the Army, Procureme][research_departmentofthearmywashingtondc_1998]
- [Joint Logistics Commanders Guidance for Use of Evolutionary...][research_hirsch_1998]
- [Research, Development, and Acquisition. Army Acquisition...][research_reimer_hudson_1998]
- [Acquisition Strategy Guide, Fourth Edition][research_mcdaniel_cooper_1999]
- [Military Assistance to Jordan. What Happened to the Peace...][research_phillips_jr_1999]
- [Defense Acquisition Univ Alexandria Va 2000, Acquisition Review Quarterly. Vol][research_defenseacquisitionunivalexandriava_2000]
- [Committee Staff Procurement Backup Book FY 2001 Budget...][research_departmentofthearmywashingtondc_2000_b]
- [Department Of The Air Force Washington Dc 2000][research_departmentoftheairforcewashingtondc_2000]
- [Department Of The Army Washington Dc 2000][research_departmentofthearmywashingtondc_2000]
- [Department Of The Air Force Washington Dc 2000][research_departmentoftheairforcewashingtondc_2000_c]
- [Department Of The Air Force Washington Dc 2000][research_departmentoftheairforcewashingtondc_2000_b]
- [E-Procurement and the U.S. Military][research_doe_2002]
- [The Quality of Quantity Mini-UAVS As An Alternative UAV...][research_weed_2002]
- [2003 IDA Cost Research Symposium Cost of Evolutionary...][research_balut_davis_2003]
- [Globalization U.S. Export Control Policy and Implications for...][research_bennett_2003]
- [Acquisition Contracting for and Performance of the C-130...][research_burton_noordhuizen_2004]
- [How Compensation in Test and Evaluation Affects Aircraft...][research_alford_2004]
- [Procurement Fraud Case Studies][research_gayton_2004]
- [The Current and Future Force Acquisition Strategy and...][research_koster_2004]
- [DoN Procurement Metrics Evaluation][research_brianas_2005]
- [Innovative Procurement Strategies][research_eiband_2005]
- [Military Assistance to Civil Authority When and Where Should...][research_chesney_2005]
- [A Transactions Cost Economics Approach to Defense Acquisition...][research_franck_dillard_2006]
- [Getting the Most from Acquisition Reforms FAR 13.5 Test...][research_yoder_2006]
- [Defense Acquisition Univ Ft Belvoir Va 2007][research_defenseacquisitionunivftbelvoirva_2007]
- [Developing an Acquisition Strategy for the Colombian Navy's...][research_cubilloschacon_2007]
- [An Application of Cost-Effectiveness Analysis in a Major...][research_greer_2010]
- [Naval Sea Systems Command Washington Dc 2010][research_navalseasystemscommandwashingtondc_2010]
- [Small Ground Robot's Effectiveness and Acquisition Strategy][research_bedell_2010]
- [The 2009 DOD Cost Research Workshop Acquisition Reform][research_roark_cuda_2010]
- [Defense Acquisition Univ Ft Belvoir Va 2010][research_defenseacquisitionunivftbelvoirva_2010]
- [When More is Better -- Design Principles for Prediction...][research_aggarwal_valerdi_2010]
- [Acquisition Program Transition Workshops An Element of the...][research_stewart_bull_2011]
- [References for Capability Assessment, Acquisition Planning...][research_hinkle_tulkoff_2011]
- [International Defense Acquisition Management and the...][research_franck_lewis_2012]
- [Military Compensation in the Armenian Armed Forces Life Cycle...][research_zurlippe_2013]
- [Cost Growth, Acquisition Policy, and Budget Climate][research_mcnicol_2014]
- [Cost Growth, Acquisition Policy, and Budget Climate. Revision][research_mcnicol_2014_b]
- [Evidence on the Effect of DoD Acquisition Policy and Process...][research_mcnicol_wu_2014]
- [Improving The Prototyping Process In Department Of Defense...][research_coble_royster_2014]

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
**The observation is narrower: by 1971 an X-designation could be allocated to an aeroplane whose primary purpose was commercial, and the allocation could precede any commitment to build it.**
That is a fact about what the system had come to permit, and it belongs with the evidence the closing
article of this series assembles.

## The Contemporary Literature

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

- [A Numerical Analysis of Supersonic Intake Buzz in an...][research_yeom_sung_2015]
- [Conical shock waves in supersonic flow][research_chen_li_2020]
- [Additive Drag Computation of Supersonic Inlet by Numerical...][research_jung_lee_2015]
- [The scaling of separation bubble in the conical shock...][research_zuo_2021]
- [Effects of Boundary-Layer Bleed Parameters on Supersonic...][research_soltani_younsi_2015]
- [Hypersonic Conical Shock-Wave/Turbulent-Boundary-Layer...][research_zuo_2023]
- [Improved Large-Eddy Simulation Validation Methodology...][research_burns_koo_2015]
- [A Local Inverse Conical Shock Problem for the Steady...][research_zhang_2024]
- [Influence of combustion-preheating vitiation on operability...][research_liu_zhu_2015]
- [Morphing Supersonic Inlet with Deforming Air Cell][research_zhang_tan_2015]
- [Numerical Simulation of Supersonic Inlet Flow with Movable...][research_kim_kwon_2015]
- [Numerical validation and back-pressure effect on internal...][research_ding_shen_2015]
- [Performance Evaluation of Compression Ramp for Supersonic...][research_miki_watanabe_2015]
- [Simulations and Experiments of a Dual-Stream Low-Boom...][research_gillen_loth_2015]
- [Effects of Bleed Position on the Stability of a Supersonic...][research_soltani_daliri_2016]
- [Flow in a Y-Intake at Supersonic Speeds][research_krushnaraokotteda_mittal_2016]
- [Design and Optimization of Supersonic Intake][research_merchant_radhakrishnan_2017]
- [Effect of back pressure and freestream dynamic pressure on a...][research_saravanan_desikan_2017]
- [Forced Shock Oscillation Control in Supersonic Intake Using...][research_yao_zhang_2017]
- [INFLUENCE OF BACK PRESSURE ON THE FLOW IN THE DIFFUSER OF A...][research_influence_of_2017]
- [Large eddy simulation of reacting flow in a hydrogen jet into...][research_zhao_zhou_2017]
- [Numerical study on hypersonic nozzle-inlet starting...][research_jiao_chang_2017]
- [Prediction of flow field for a 2-D mixed compression...][research_m_v_2017]
- [Experimental investigations of flow through wide angle...][research_hemalatha_mahalakshmi_2018]
- [Numerical investigation on behaviors of shock train in a...][research_shi_chang_2018]
- [Preliminary experimental assessment of supersonic airflow...][research_kotov_ruleva_2018]
- [Ramp Shock Regulation of Supersonic Inlet with Shape Memory...][research_zhang_tan_2018]
- [Angle of Attack Investigations on the Performance of a...][research_askari_soltani_2019_b]
- [Buzz evolution process investigation of a two-ramp inlet with...][research_shi_chang_2019]
- [Design and performance study of a parametric diverterless...][research_bsaheby_shen_2019]
- [Effects of inlet parameters on the supersonic condensation...][research_bian_cao_2019]
- [Load characterization on the joints of the A320 engine inlet...][research_conceicao_anes_2019]
- [Numerical investigation on the forced oscillation of shock...][research_shi_chang_2019_b]
- [Numerical study of the flow structure in the supersonic...][research_seleznev_2019]
- [Starting Characteristic of Supersonic Mixed Compression Air...][research_gahlot_singh_2019]
- [CFD analysis of conical diffuser under swirl flow inlet...][research_agarwal_mthembu_2020]
- [Study on integrated control for supersonic inlet and turbofan...][research_chen_zhang_2020]
- [Supersonic flow in the rectangular duct of an air inlet with...][research_mazhul_2020]
- [Analysis of intake swirl in a compression ignition engine at...][research_kumar_darsigunta_2021]
- [Effect of added struts and intake velocity on flame...][research_mohammad_2021]
- [Experimental Study of the Buzz Phenomenon Occurring on the...][research_fujii_fujimori_2021]
- [Experimental and numerical investigation on a supersonic...][research_yuan_zhang_2021]
- [Reconstruction of numerical inlet boundary conditions using...][research_veras_balarac_2021]
- [Review of variable leading-edge patents for aircraft wings...][research_kazula_hoschler_2021]
- [Control of shock wave/boundary layer interactions in a...][research_khobragade_kumar_2022]
- [Effects of bleed type on the performance of a supersonic...][research_rezamaadi_sepahiyounsi_2022]
- [Experimental Study on the Dynamic Characteristics and Surface...][research_kong_li_2022]
- [Flow response hysteresis of throat regulation process of a...][research_jin_sun_2022]
- [Influence of Inlet Pressure Distortion on the Engine...][research_alendar_grunin_2022]
- [Joint discriminative learning and classification for...][research_wu_zhao_2022]
- [Simulation and validation of the gas flow in close-coupled...][research_urionabarrenetxea_martin_2022]
- [Duct Height Effect on Terminal Shock/Boundary-Layer...][research_wang_sun_2023_b]
- [Inlet static pressure ratio effect on vortex structure...][research_huang_yao_2023]
- [Mixed-Compression Supersonic Intake and Engine Airframe...][research_gaglio_visone_2023]
- [Suppression of flow response hysteresis in the...][research_jin_zhang_2023]
- [The analysis on the flow characteristics of supersonic inlet...][research_chen_chen_2023]
- [Characterization of a supersonic mixed-compression air intake...][research_khobragade_gustavsson_2024]
- [Design of Pitot Intake for Supersonic Micro Gas Turbine Engine][research_kang_kang_2024]
- [Experimental Investigation of the Performance of a Novel...][research_xu_gu_2024]
- [Inlet Mach number ratio and static temperature ratio coupling...][research_huang_yao_2024]
- [Measurement of Flow Field Characteristics in a Supersonic...][research_liu_zhu_2024]
- [Transient and POD analyses of supersonic intake for...][research_choi_2024]
- [A proposed methodology for diverterless supersonic inlet...][research_vacarios_ceronmunoz_2025]
- [Aerodynamic enhancement of diverterless supersonic inlets via...][research_ma_li_2025]
- [An investigation on bleed flow control of an axisymmetric...][research_xie_liu_2025]
- [Controlled Flow in a Serpentine Diffuser with a Cowl Inlet][research_burrows_vukasinovic_2025]
- [Design concept of compression wave and opposite cowl shock...][research_tang_cai_2025]
- [Effect of Inlet Subsonic Velocity and Area Ratio on the...][research_priya_arora_2025]
- [Fiber Bragg Grating-based sensor for measuring supersonic...][research_liu_zhu_2025_b]
- [Influence of active cowl deflection during buzz cycle of an...][research_rao_kumar_2025]
- [Multi-sensor flow state identification and schlieren image...][research_wang_zhao_2025_b]
- [Numerical investigation on the effect of cowl angle in the...][research_ajay_kundu_2025]
- [Numerical study on the flow characteristics of a start...][research_sun_yu_2025]
- [On the centered-compression waves/cowl shock interaction from...][research_tang_cai_2025_b]
- [Study on CFD Analysis for Preliminary Design of Semi-Freejet...][research_moon_2025]
- [An Integrated FBG Pressure Sensing and Profile Matching...][research_liu_zhu_2026]
- [Characteristics of shoulder separation bubble and internal...][research_zhang_ning_2026]
- [Design and optimization of a fuselage-integrated diverterless...][research_choi_choi_2026]
- [Design and research on wide-speed-range variable-geometry...][research_luo_meng_2026]
- [High subsonic performance of a diverterless supersonic inlet...][research_askari_abedi_2026]
- [Optimization Of Hypersonic Scramjet Triple-Ramped Inlet...][research_rajdeepbosemondal_2026]
- [Restart control for a two-dimensional twin-duct supersonic...][research_he_xie_2026]

- [Discussion of Some Myths/Features Associated With Gas Turbine...][research_wang_khan_2015]
- [Enhanced Performance of Streamline-Traced...][research_slaterjohnw_2015]
- [Enhancing micro gas turbine performance in hot climates...][research_comodi_renzi_2015]
- [Research on the Design Methods of Channeled Centerbody...][research_tongguang_changhui_2015]
- [A Study on Blended Inlet Body Design for a High Supersonic...][research_you_yu_2016]
- [A study of unsteady-state operating conditions of a...][research_lyubimov_potekhina_2016]
- [Investigation on Frequency Responses for Supersonic Intake...][research_qin_liang_2016]
- [SUPIN A Computational Tool for Supersonic Inlet Design][research_slaterjohnw_2016]
- [Supersonic Inlet Control Design for Integrated Aero...][research_sun_zhang_2016]
- [Vortex Generators in a Two-Dimensional, External-Compression...][research_baydarezgihan_lufrankk_2016]
- [AUTOMATIC CONTROL SYSTEM FOR AN AIRCRAFT PLAN SUPERSONIC...][research_tudosie_paunescu_2017]
- [Aerodynamic response of internal passages to pulsating inlet...][research_sousa_paniagua_2017]
- [Buzz Flows in an External-Compression Inlet with Partially...][research_chen_tan_2017]
- [CHOICE AND DESIGN OF A 3D FIXED-GEOMETRY INLET FOR A SMALL...][research_vinogradov_melnikov_2017]
- [CONTROL LAWS FOR AN AIRCRAFT SUPERSONIC INLET WITH MOBILE...][research_tudosie_2017]
- [EXPERIMENTAL INVESTIGATION OF A 3D FIXED-GEOMETRY INLET FOR A...][research_vinogradov_makarov_2017]
- [Off-Design Performance of a Streamline-Traced...][research_slaterjohnw_2017]
- [PNEUMO-HYDRO-MECHANICAL CONTROL SYSTEM FOR AN AIRCRAFT...][research_tudosie_2017_b]
- [Vortex Generators in a Streamline-Traced...][research_baydarezgihan_lufrankk_2017]
- [AXISYMMETRIC FRONTAL SUPERSONIC INLET FOR TRISONIC AIRCRAFT][research_tudosie_2018]
- [Analysis the optimum inlet air temperature for controlling...][research_gowthaman_sathiyagnanam_2018]
- [Novel Method for Supersonic Inlet Buzz Measurement in Wind...][research_daliri_farahani_2018]
- [Numerical study of the flow structure in the supersonic...][research_seleznev_2018]
- [Throttling Process and Buzz Mechanism of a Supersonic Inlet...][research_chen_tan_2018]
- [Vortex Generators in a Two-Dimensional External-Compression...][research_baydar_lu_2018]
- [A proposed design method for supersonic inlet to improve...][research_farahani_mahdavi_2019]
- [Buzz flow diversity in a supersonic inlet ingesting strong...][research_chen_tan_2019]
- [CONTROL LAW FOR AN AIRCRAFT SUPERSONIC AIR INLET WITH...][research_tudosie_dumitru_2019]
- [Design of Inward-Turning External Compression Supersonic...][research_utomo_bura_2019]
- [Effect of Side Gust on Performance of External Compression...][research_halwas_aggarwal_2019]
- [Effects of Mach Number on the Performance of a Diverterless...][research_askari_soltani_2019]
- [Evaluation of Variable Pitot Inlet Concepts for Transonic and...][research_kazula_mischke_2019]
- [External-Compression Supersonic Inlet Free from Violent Buzz][research_chen_tan_2019_b]
- [Investigation of the mixing characteristics in a transverse...][research_zhao_li_2019]
- [Numerical Analysis on Supersonic Inlet Buzz][research_nagao_yoshida_2019]
- [On the performance of a body integrated diverterless...][research_soltani_askari_2019]
- [Side Gust Effects on the Performance of a Supersonic Inlet...][research_halwas_aggarwal_2019_b]
- [Supersonic inlet buzz detection using pressure measurement on...][research_farahani_daliri_2019]
- [Acoustic Modeling and Vibration Characteristics of Supersonic...][research_zhu_luo_2020]
- [Control of a Supersonic Inlet in Off-Design Conditions with...][research_ferrero_2020]
- [Design and Experimental Assessment of Bladeless Turbines for...][research_braun_paniagua_2020]
- [Effects of Optimized Bleed System on Supersonic Inlet...][research_choe_kim_2020]
- [Evaluation of variable pitot inlet concepts for transonic and...][research_kazula_hoschler_2020]
- [Experiment and numerical investigation of flow control on a...][research_zhang_yuan_2020]
- [Flow Asymmetry in a Y-Shaped Diverterless Supersonic Inlet A...][research_askari_soltani_2020]
- [Flow Field Study of Mixed Compression Supersonic Air Intake...][research_flow_field_2020]
- [Inlet air and fuel flow pressure fluctuation effect on...][research_tahsini_2020]
- [Investigation on the effect of intake air pressure in a...][research_patel_dubey_2020]
- [Numerical Simulation of Supersonic Flow through Scramjet...][research_numerical_simulation_2020]
- [Numerical simulation of inlet buzz][research_abedi_askari_2020]
- [Prediction of the onset of supersonic inlet buzz][research_yamamoto_kojima_2020]
- [Repetitive Energy Deposition at a Supersonic Intake in...][research_myokan_kubota_2020]
- [Spatiotemporal Characterization and Suppression Mechanism of...][research_luo_wei_2020]
- [Time-Accurate Experimental Investigation of Hypersonic Inlet...][research_berto_benini_2020]
- [A compatible inlet condition for simulation of supersonic...][research_chen_zhang_2021]
- [Buzz characteristics and separation bubble dynamics in...][research_kjames_suryan_2021]
- [Design and Evaluation of Generic Bump for Flow Control in a...][research_khan_hasan_2021]
- [Design and analysis of a Ventral Diverterless Supersonic Inlet][research_ge_shang_2021]
- [Design and optimization of bump compression surface for...][research_arif_iftikhar_2021]
- [Exergetic and Exergoeconomic Optimization of Gas Turbine...][research_abedi_salehi_2021]
- [Linear and Nonlinear Flow Analysis of Elements of a...][research_khobragade_unnikrishnan_2021]
- [Optimization of scramjet inlet based on temperature and Mach...][research_araujo_pereira_2021]
- [Parameters for evaluating the efficiency of inlet compression][research_chen_yue_2021]
- [Research on Computational Method of Supersonic Inlet/Isolator...][research_liu_wang_2021]
- [Testing of a Supersonic Nozzle with Supersonic Intake][research_veereshkumar_nagasailaja_2021]
- [A real-time online unstart prediction approach for supersonic...][research_wang_zhao_2022]
- [Effects of boundary-layer bleed parameters on supersonic...][research_sepahiyounsi_2022]
- [Experimental Study of the Unstart/Restart Process of a...][research_experimental_study_2022]
- [High Speed Inlet Distortion Test for the X 59 Low Boom Flight...][research_vancefdippoldiii_2022]
- [Inlet buzz phenomenon driven by flow choking in high-enthalpy...][research_liu_kang_2022]
- [Investigation of Shock Wave Oscillation Suppression by...][research_cai_huang_2022]
- [Performance Characteristics of Hypersonic External...][research_kim_lee_2022]
- [Review of Supersonic Intake buzz, problems associated and...][research_kumar_2022]
- [Stall Inception in a Compressor with Subsonic, Transonic, and...][research_kim_choi_2022]
- [Study on Self-Excited Oscillation Suppression of Supersonic...][research_cai_huang_2022_c]
- [Study on a Two-Dimensional Supersonic Inlet with Inner...][research_cai_huang_2022_b]
- [Study on the mechanism of the buzz flow in a supersonic intake][research_kjames_kim_2022]
- [Symmetric and Asymmetric Performance Investigation of a...][research_askari_soltani_2022]
- [Comparison of the unstart/restart processes of a...][research_li_ding_2023]
- [Control of Cowl Shock/Boundary Layer Interaction in...][research_wang_wang_2023]
- [Effect of inlet Mach number on performance and flow structure...][research_effect_of_2023]
- [Effects of backpressure on unstart and restart...][research_wang_wang_2023_b]
- [Experimental investigation on unstart-restart hysteresis of a...][research_jin_tan_2023]
- [Flow Field Investigation of a Rectangular Supersonic...][research_das_prasad_2023]
- [Numerical Simulation of a Y-Shaped Diverterless Supersonic...][research_askari_soltani_2023]
- [Real-time online unstart prediction of supersonic inlet based...][research_wang_zhao_2023_b]
- [The Effect of Upstream Unsteadiness on the Unstarting of a...][research_mushtaq_gaetani_2023_b]
- [Understanding and modeling unstarting phenomena in a...][research_mushtaq_gaetani_2023]
- [Advanced Design of a Transition Duct for Supersonic Inlet...][research_mushtaq_pini_2024]
- [Evolution Characteristics Analysis of Supersonic Inlet Buzz...][research_luo_tao_2024]
- [Hysteresis of oscillatory airflow in a supersonic intake model][research_kuzmin_2024]
- [Intake Characteristics and Inhomogeneity of Supersonic Passage][research_hu_2024]
- [Optimization of Plenum for Control of Boundary Layer-Shock...][research_turkkahraman_ozcan_2024]
- [Shock Wave Control for Supersonic Inlet with High-Frequency...][research_sun_zhang_2024]
- [Experimental study of the buzz phenomenon in a supersonic...][research_sepahiyounsi_2025]
- [Freejet tests on a variable geometry supersonic inlet driven...][research_wang_zhang_2025]
- [HIGH BYPASS TURBOFAN ENGINE PERFORMANCE INTAKE PRESSURE...][research_abdelghany_2025]
- [Integrated aerodynamic optimization of diverterless...][research_shu_gao_2025]
- [Measurement of Buzz Flows in a Supersonic Inlet by FBG Sensors][research_liu_zhu_2025]
- [Multi-Regime CFD Optimization of Diverter-less Supersonic...][research_ali_khan_2025]
- [Multi-level and multi-scale cross attention network of...][research_wang_zhao_2025]
- [Numerical investigation of inlet pressure effects on...][research_qian_2025]
- [Optimization and Research of the Power Plant Inlet Device for...][research_safoklov_demidov_2025]
- [Research on starting characteristics of two-dimensional...][research_li_qu_2025]
- [An efficient multi-domain encoded fusion network for...][research_wang_zhao_2026]
- [Delaying the buzz onset in a supersonic inlet by multi-row...][research_taghiabad_esfandabadi_2026]
- [Effect of Preoperative Oral Carbohydrate Intake on Quality of...][research_effect_of_2026]
- [Experimental investigation on the inlet shock wave/boundary...][research_kong_su_2026]
- [FLOW SEPARATION SUPPRESSION OF SWEPT SHOCK WAVE-BOUNDARY...][research_kim_park_2026]
- [Inverse design method of inward-turning inlet based on...][research_zhang_yang_2026]
- [Multi-objective and multi-point adjoint optimization of...][research_ma_li_2026]
- [Numerical investigation of axisymmetric supersonic...][research_huang_wang_2026]
- [Optimization of supersonic inlet configuration using...][research_yang_kong_2026]
- [Optimizing MRD inlet performance through disk geometry...][research_sinha_singh_2026]
- [Triangular-cell surrogate model for rapid prediction of...][research_nagler_2026]
- [Unstarting/starting characteristics of supersonic inlet...][research_wang_guan_2026]
- [Unsteady flow regimes and bleed-controlled flow splitting in...][research_miao_guan_2026]

### Distortion is better understood and no less dangerous

The X-27's exposure was a distortion-sensitive fan behind a marginal inlet.
**That combination is now a named design discipline with its own descriptors and standards**, and the
surrounding work covers distortion descriptors, fan stability under circumferential and radial defects, and
the closely related problem of boundary-layer-ingesting propulsion, which deliberately accepts distortion in
exchange for propulsive efficiency.

**The comparison is instructive.** A modern boundary-layer-ingesting fan accepts distortion the TF30 could
not survive, and it does so because the fan is designed for it from the outset.
**The X-27 proposed the opposite, an engine designed for clean flow placed behind an inlet asked to work beyond its ancestry.**

- [Assessment of angular distortion of structures adjacent to a...][research_kim_kim_2015]
- [Measurement of Distortion Using the Moire Interferometry][research_wenzel_2015]
- [Preliminary Integrated Design of Hypersonic Vehicle...][research_wang_tian_2015]
- [Flow Distortion Measurements in Convoluted Aeroengine Intakes][research_zachos_macmanus_2016]
- [Histogram of Radon transform with angle correlation matrix...][research_hasegawa_tabbone_2016]
- [Low Frequency Distortion in Civil Aero-engine Intake][research_carnevale_wang_2016]
- [Strip distortion generator for simulating inlet flow...][research_saleemyusoof_sivapragasam_2016]
- [Approach to Modeling Boundary Layer Ingestion Using a Fully...][research_grayjustins_madercharlesa_2017]
- [Complex Aeroengine Intake Ducts and Dynamic Distortion][research_macmanus_chiereghin_2017]
- [Effects of bending-torsional duct-induced swirl distortion on...][research_hou_wang_2017]
- [Estimation and hypothesis test on partial linear models with...][research_zhang_zhou_2017]
- [Impact of inlet distortion on turbocharger compressor stage...][research_zhao_sun_2017]
- [Aerodynamic Design and Optimization of Fan Stage for Boundary...][research_leebyungjoon_lioumayfun_2018]
- [Aeromechanics Analysis of a Distortion-Tolerant Fan with...][research_bakhlemilinda_reddytsr_2018]
- [Assessing the Impact of the Inlet Total Pressure Distortion...][research_ezrokhi_khoreva_2018]
- [Complex Flow Generation and Development in a Full-Scale...][research_guimaraes_toddlowe_2018]
- [Conceptual Aerodynamic Design of a Tail-Cone Thruster System...][research_leebj_lioumayfun_2018]
- [Cyclic Symmetry Finite Element Forced Response Analysis of a...][research_minjb_reddytsr_2018]
- [Effects of Stall Precursor-Suppressed Casing Treatment on a...][research_dong_sun_2018]
- [Investigation of inlet distortion effects on axial compressor...][research_abbasi_pirnia_2018]
- [StreamVane Turbofan Inlet Swirl Distortion Generator Mean...][research_guimaraes_lowe_2018]
- [The Influence of Measurement Methodology on the Accuracy of...][research_bartman_kwiatkowski_2018]
- [Assessing Stability Performance of Non-Metric Camera’s Lens...][research_etjahjadi_dagustina_2019]
- [Coupled Fan Stator Aerodynamic and Acoustic Response to...][research_atassi_kozlov_2019]
- [Dynamic inspection of a rail profile under affine distortion...][research_yang_liu_2019]
- [Experimental investigation and detached-eddy simulation of...][research_zhou_li_2019]
- [Heteromorphic Optical Window Design and Imaging Distortion...][research_guopengyu_xuezhiliang_2019]
- [Non-uniform stator loss reduction design strategy in a...][research_lu_yang_2019]
- [The Flashed Face Distortion Effect Does Not Depend on...][research_balas_pearson_2019]
- [Tonal Noise Prediction of a Modern Turbofan Engine With Large...][research_daroukh_moreau_2019]
- [An experimental investigation on the interaction between...][research_wang_hu_2020]
- [Artificial Thickening of a Transonic Boundary Layer in the...][research_gregorysjones_williammilholen_2020]
- [Boundary Layer Ingestion Propulsion A Review on Numerical...][research_menegozzo_benini_2020]
- [Experimental investigation of flow and distortion mitigation...][research_maghsoudi_vaziry_2020]
- [Laser velocimetry for turbofan inlet distortion applications][research_lowe_2020]
- [Optimization of a transonic axial-flow compressor under inlet...][research_da_hanan_2020]
- [Scaling of Incidence Variations With Inlet Distortion for a...][research_hill_defoe_2020]
- [Shock Wave Generation and Radiation from a Turbofan Engine...][research_daroukh_polacsek_2020]
- [The effect of inlet distortion on low bypass ratio turbofan...][research_verma_singh_2020]
- [Tip air injection to extend stall margin of multi-stage axial...][research_li_du_2020_b]
- [An Improved Design of a Swirl Distortion Generator][research_luning_bangqin_2021]
- [Assessment of the Influence of Boundary Layer Ingestion BLI...][research_masaki_ogushi_2021]
- [Efficient Modeling of an Axial Compressor with Swirl...][research_guo_hu_2021]
- [Experimental Investigation of Rotating Instability in an...][research_xu_hu_2021]
- [Experimental and Numerical Analysis of a Compressor Stage...][research_baretter_godard_2021]
- [Improvement of the Parallel Compressor Model and Application...][research_benichou_binder_2021]
- [Performance analysis of turbo-electric propulsion system with...][research_samuelsson_gronstedt_2021]
- [Response and stabilization of a two-stage axial flow...][research_li_dong_2021]
- [Strain Response and Aerodynamic Damping of a Swirl Distortion...][research_hayden_untaroiu_2021]
- [A fast computational method of the aerodynamic performance of...][research_tao_jin_2022]
- [Body Image Distortion in Patients with Depression and Normal...][research_bidaki_2022]
- [Calibration of S-duct Swirl Distortion Based on Vortex...][research_sun_li_2022]
- [Chip distortion error post-processing method based on dynamic...][research_lu_zhang_2022]
- [Detached-Eddy Simulation and Swirl Distortion...][research_feng_tianyu_2022]
- [Diesel Engine Cylinder Liner Distortion Analysis][research_diesel_engine_2022]
- [Effect of circumferential non-uniform tip clearance on the...][research_xu_hu_2022_b]
- [Effect of inlet distortion with crosswind on aircraft-engine...][research_naruse_ishii_2022]
- [Experimental Research on Inlet Steady Swirl Distortion in an...][research_xu_hu_2022]
- [Numerical Investigation on the Performance of a Transonic...][research_li_zhu_2022]
- [Parameter Sensitivity Study on Inflow Distortion of Boundary...][research_zhao_vanhoorn_2022]
- [Recent Advances in Boundary Layer Ingestion Technology of...][research_diamantidou_hosain_2022]
- [Research on flexible skin technique for adaptive bump inlet...][research_zhao_zhou_2022]
- [Response of a Tandem-Staged Compressor to Circumferential...][research_kumar_pradeep_2022]
- [The influence of visual distortion on face recognition][research_dear_harrison_2022]
- [Unsteady Analysis of Aeroengine Intake Distortion Mechanisms...][research_rao_sureshkumar_2022]
- [Updated Assessment of Turboelectric Boundary Layer Ingestion...][research_jameslfelder_michaelttong_2022]
- [A Modified Circumferentially Averaged Method for Compressor...][research_zhao_jin_2023]
- [A parametric hypothesis test for a global power law and local...][research_zhang_feng_2023]
- [Advancements and prospects of boundary layer ingestion...][research_moirou_sanders_2023]
- [Effects of Stage Loading on Performance and Flow Field of a...][research_sitaram_govardhan_2023]
- [Efficient numerical prediction of blade forced response under...][research_fang_wang_2023]
- [Experimental and Numerical Research on a Three-Dimensional...][research_yuan_li_2023]
- [Experimental investigation of aerodynamic characteristics of...][research_pouryoussefi_abdolali_2023]
- [High Throughflow StreamVane Swirl Distortion Generators...][research_hayden_gillespie_2023]
- [High-precision projection moiré measurement method for the...][research_cai_sun_2023]
- [Investigation of the Stability Criterion for Axial Compressor...][research_xu_hu_2023]
- [Large eddy simulation investigation of S-shaped intake...][research_ming_wu_2023]
- [Study on erosion wear characteristics of aero-compressor...][research_yang_li_2023]
- [The decelerator tester twisting distortion caused angular...][research_yu_xu_2023]
- [The influence of a coupled casing on the performance of a...][research_xie_zhu_2023]
- [Towards More Efficient Electric Propulsion UAV Systems Using...][research_arias_martinez_2023]
- [Unsteady characteristics of pressure and swirl distortion in...][research_dimarco_jacob_2023]
- [A new point cloud simplification method for reducing visual...][research_wu_yang_2024]
- [A region-segmentation combinational loss model based on...][research_pan_shi_2024]
- [Aeroacoustic Effects on the Forcing of Fan and Compressor...][research_martensson_billson_2024_b]
- [Analysis of Flow Field Distortion in Ship Inlet System and...][research_analysis_of_2024]
- [Analysis on stall mechanism of axial flow compressor with...][research_qiu_zhong_2024]
- [Effect of Exhaust Jet from Takeoff Aircraft on the Inlet...][research_effect_of_2024]
- [Effects of Swirl Distortion on Flow Field and Blade Load of a...][research_li_hou_2024]
- [Enhancing Wireless Communication Efficiency Using Dynamic...][research_jayarani_narmadhai_2024]
- [Equivalent simulation method for total pressure distortion of...][research_wang_he_2024]
- [Erosion wear patterns of turboshaft engine compressor under...][research_yang_li_2024_b]
- [Face adaptation induces duration distortion of subsequent...][research_sarodo_yamamoto_2024]
- [Forced Vibration Induced by Dynamic Response Under Different...][research_pan_mu_2024]
- [Influence of the shock wave-turbulence interaction on the...][research_wu_li_2024_b]
- [Isolator shape transition impact on hypersonic internal...][research_musa_huang_2024]
- [Jackknife empirical likelihood for the correlation...][research_chen_dai_2024]
- [Objectively quantifying subjective phenomena Measuring the...][research_gao_wang_2024]
- [Proper Orthogonal Decomposition Based Response Analysis of...][research_cao_yue_2024]
- [Stall Warning and Adaptive Control Subjected to Rotating...][research_li_liu_2024_b]
- [Sweep Optimization to Reduce Aerodynamic Loss in a Transonic...][research_sweep_optimization_2024]
- [The numerical simulation and test verification of the inlet...][research_wu_li_2024]
- [Unsteady numerical study on the effects of inlet distortion...][research_zhang_liu_2024]
- [Unsupervised correction algorithm of engine inlet total...][research_yan_qian_2024]
- [A Flow Physics Approach to Determining Critical Angle of...][research_bond_key_2025]
- [A loss reduction design strategy for a ducted fan under...][research_lu_wang_2025]
- [Aerodynamic behavior of a transonic compressor under...][research_karl_werner_2025]
- [Aerodynamic design of a radially-segmented 2-DOF VIGV for...][research_mao_zhang_2025]
- [Application of Neural Network Models for Analyzing the Impact...][research_kozakiewicz_adamczyk_2025]
- [Body Force Modelling of a Multi-Stage High-Pressure...][research_crea_marty_2025]
- [Effects of Swirl Distortion on a Centrifugal Compressor at...][research_bond_brown_2025]
- [Extension of the Throughflow Solver for Predicting the...][research_petkovic_banjac_2025]
- [Momentum- and Energy-Based Analyses of the Aerodynamic...][research_wang_li_2025]
- [Phase response measurement and dynamic distortion correction...][research_han_jia_2025]
- [Response and stall mechanism for axial compressor under...][research_ma_wang_2025]
- [Shock train stabilization by a high-speed jet injection in an...][research_wang_chen_2025_b]
- [The impact of the combined total pressure-swirl distortion on...][research_xu_wu_2025]
- [Unsteady Swirl Distortion in a Short Intake Under Crosswind...][research_piovesan_zachos_2025]
- [Wide-angle lens distortion influence on modulation transfer...][research_wide_angle_lens_2025]
- [An accurate underwater camera calibration method based on a...][research_hu_qian_2026]

- [Applying CFD Technology to Determine the Effect of Two New...][research_zhipeng_chao_2015]
- [Effects of Rotating Inlet Distortion on Compressor Stability...][research_dong_sun_2015]
- [Investigation on stall inception of axial compressor under...][research_zhang_hou_2015]
- [Numerical investigation of effect of inlet swirl and...][research_naseri_boroomand_2016]
- [Analysis of Fan Stage Conceptual Design Attributes for...][research_hall_greitzer_2017]
- [Discretized Miller approach to assess effects on boundary...][research_valencia_hidalgo_2017]
- [JET ENGINE INLET DISTORTION SCREEN AND DESCRIPTOR EVALUATION][research_pecinka_bugajski_2017]
- [A Parametric Study of the Effects of Inlet Distortion on Fan...][research_zhang_vahdati_2018]
- [Aeromechanical Response of a Distortion-Tolerant Boundary...][research_provenza_duffy_2018]
- [Characteristics of unsteady total pressure distortion for a...][research_tanguy_macmanus_2018]
- [Effect of Fan on Inlet Distortion Mixed-Fidelity Approach][research_ma_cui_2018]
- [Effect of Inlet Distortion Features on Transonic Fan Rotor...][research_page_hield_2018]
- [Experimental Quantification of Fan Rotor Effects on Inlet...][research_frohnapfel_toddlowe_2018]
- [Sensitivity of high-speed boundary-layer stability to...][research_park_zaki_2018]
- [Distortion of pipe-flow development by boundary layer growth...][research_haustein_kashi_2019]
- [Effect of Inlet Boundary Layer Suction on Flow Distortion in...][research_lee_lee_2019]
- [High-Frequency Electric Machines for Boundary Layer Ingestion...][research_yoon_xiao_2019]
- [Stall and Recovery Process of a Transonic Fan With and...][research_zhang_vahdati_2019]
- [Coupled Aeropropulsive Optimization of a Three-Dimensional...][research_gray_mader_2020]
- [Effect of inlet radial distortion on aerodynamic stability in...][research_li_du_2020]
- [Influence of the inlet distortion on fan stall margin at...][research_zhang_stapelfeldt_2020]
- [Minimizing local drag by shaping a flanged slotted hood along...][research_ziganshin_logachev_2020]
- [Novel fan configuration for distributed propulsion systems...][research_valencia_alulema_2020]
- [Shock Boundary Layer-Interaction Control Through...][research_ruban_menezes_2020]
- [Evaluation of a Regional Aircraft with Boundary Layer...][research_secchi_lacava_2021]
- [Harmonic Forcing from Distortion in a Boundary Layer...][research_martensson_2021]
- [Hybrid Flow Control on Boundary Layer Ingestion Inlet][research_shang_ge_2021]
- [Mechanism of Affecting the Performance and Stability of an...][research_zhang_li_2021]
- [Numerical Investigation on the Influences of Boundary Layer...][research_yang_lu_2021]
- [Prestall Disturbances and Stall Inception for an Eccentric...][research_wang_hu_2021]
- [Spike-type disturbances due to inlet distortion in a...][research_cao_zhu_2021]
- [A Data-Driven Tip Flow Loss Prediction Method for a Transonic...][research_yang_lu_2022]
- [Adaptive feedback control of stability in an axial flow...][research_liu_li_2022]
- [Design of a sub-scale fan for a boundary layer ingestion test...][research_martensson_lejon_2022]
- [Inlet Flow Distortion in an Advanced Civil Transport Boundary...][research_hall_greitzer_2022_b]
- [Method of Designing a Distortion Gauze for Testing a Boundary...][research_kwiatkowski_sieradzki_2022]
- [Mitigation of Boundary Layer Ingestion Circumferential...][research_hall_greitzer_2022]
- [Numerical Investigations of a Non-Uniform Stator Dihedral...][research_pan_shi_2022]
- [Numerical simulation of S-shaped inlet under the intake total...][research_liu_zhang_2022]
- [Robust Adaptive Control of Hypersonic Vehicle Considering...][research_wang_fan_2022]
- [Using Tip Injection to Stability Enhancement of a Transonic...][research_using_tip_2022]
- [A modified small perturbation stability prediction model for...][research_gu_xu_2023]
- [Adaptive feedback control of stability in an axial compressor...][research_du_liu_2023]
- [Coupling Effect between Inlet Distortion Vortex and Fan][research_liu_huang_2023]
- [Effect of bend-induced inlet distortion on a centrifugal...][research_wang_zhao_2023]
- [Effects of Inlet Swirl Distortion on a Multi-Stage Compressor...][research_fang_sun_2023]
- [Effects of rotating inlet distortion on the stall mechanism...][research_qiu_du_2023]
- [Installed performance seeking control based on supersonic...][research_wang_sun_2023]
- [Numerical study on the Re effects on the tip flow structures...][research_li_zhu_2023]
- [Stall and stability enhancement mechanisms of transonic...][research_qiu_zhao_2023]
- [Suction Control of a Boundary Layer Ingestion Inlet][research_liu_li_2023]
- [4D printed NiTi variable-geometry inlet for aero engines][research_kang_li_2024]
- [A Methodology for Assessing Axial Compressor Stability with...][research_sun_gu_2024_b]
- [Adjoint based aerodynamic shape optimization of a...][research_kucuk_tuncer_2024]
- [Attenuation of Inlet Distortion Effects on Fans Using...][research_liu_vo_2024]
- [Behavior of flow distortion within a boundary layer ingestion...][research_wang_liu_2024]
- [Effect of Rotating Inlet Distortion with Multi-distorted...][research_wang_fan_2024]
- [Effect of fore/aft-loaded rotor on compressor stability under...][research_sun_gu_2024]
- [Effect of inlet distortion on internal flow and performance...][research_zhang_chen_2024]
- [Effect of radial inlet distortion on aerodynamic stability in...][research_fan_liu_2024]
- [Effects of Re on blade load temporal-spatial distribution and...][research_li_zhu_2024_b]
- [Experimental investigation on a lightweight, efficient...][research_lengyelkampmann_karboujian_2024]
- [Inlet distortion of a rear engines concept aircraft and its...][research_qiang_xue_2024]
- [Numerical Study on the Effects of Re on the Unsteady...][research_li_zhu_2024]
- [Research on the additional drag of turboshaft engine inlet...][research_cheng_huang_2024]
- [Unsteady Aerodynamic Forcing Due to Distortion in a Boundary...][research_martensson_billson_2024]
- [A Three-Dimensional Actuator Disk Model for Fan Response to...][research_prasad_2025]
- [A review on aero-engine inlet-compressor integration and...][research_li_sun_2025]
- [A systematic review of boundary layer ingestion BLI fan...][research_ma_lu_2025]
- [Analysis of Radial Inlet Distortion on Transonic Fan...][research_reedy_gorrell_2025]
- [Analysis of flow characteristics and flow stability on an...][research_sun_shen_2025]
- [Experimental Investigation of Stall Mechanism and Warning...][research_fan_du_2025]
- [Experimental and prediction of stability of a two-stage...][research_sun_yang_2025]
- [Impact of Fan Aerodynamics on Inlet Distortion at Crosswind][research_chennuru_corral_2025]
- [Numerical investigation of the flow characteristics in a...][research_lu_li_2025]
- [Rotating nonuniformity induced by distortion inlet and its...][research_yan_pan_2025]
- [Stability enhancement of an axial fan by foam metal casing...][research_geng_yang_2025]
- [Stall Inception Transition Mechanism and Warning...][research_liu_du_2025]
- [Thermodynamic modeling and performance analysis of RBCC...][research_huang_lv_2025]
- [A Spatially Adaptive Threshold Strategy for Compressor...][research_fan_xu_2026]
- [Adaptive Stability Control of a High-Speed Axial Flow Fan...][research_fan_li_2026]
- [Aerodynamic performance in a boundary layer ingesting fan...][research_deng_li_2026]
- [Analisis Geometri Engine Inlet terhadap Induced Drag pada...][research_agungsaputra_bhimashaktiarafat_2026]
- [Collaboration of GTCC-Powered CAES with Residual Compression...][research_yang_qi_2026]
- [Effect of Inlet Distortion Reduced Frequency on Centrifugal...][research_bond_key_2026]
- [Effects of high-temperature steam ingestion-induced inlet...][research_wu_du_2026]
- [Experimental Investigation on the Effects of Inlet...][research_fan_xu_2026_b]
- [Experimental study of boundary layer ingestion Propulsive...][research_park_kim_2026]
- [Flow distortion effects on the aerodynamics and performance...][research_magrini_benini_2026]
- [Influence of inlet distortion on stall inception in...][research_yuan_lu_2026]
- [Inlet Pressure Distortion Related Studies on an Experimental...][research_bhunia_abbas_2026]
- [Mitigation of Circumferential Inlet Distortion Effects Using...][research_kramer_hall_2026]
- [Stability control using tip air injection in an axial...][research_liu_du_2026]
- [Unsteady loss mechanisms in a boundary layer ingestion fan...][research_yu_zhao_2026]

### Compressor stall is a control problem now

Stall and surge were phenomena to be avoided by margin in 1971.
**They are now phenomena to be detected and actively suppressed**, with stall-precursor detection, casing
treatment, and active control all mature subjects.

**Had the X-27 flown, this is the technology that would have rescued it, and it did not exist.**

- [Experimental Investigation of Surge and Stall in a High-Speed...][research_xinqian_anxiong_2015]
- [Experimental Study of Surge and Rotating Stall Occurring in...][research_li_xu_2015]
- [Rotating Stall Observations in a High Speed Compressor Part I...][research_dodds_vahdati_2015_b]
- [Rotating Stall Observations in a High Speed Compressor Part...][research_dodds_vahdati_2015]
- [Unsteady Investigation on Tip Flow Field and Rotating Stall...][research_gao_li_2015]
- [Casing Treatment for Desensitization of Compressor...][research_cevik_ducvo_2016]
- [Stability management of high speed axial flow compressor...][research_alone_kumar_2016]
- [Stall Margin Improvement in a Centrifugal Compressor through...][research_koyyalamudi_nagpurwala_2016]
- [The stall inceptions in an axial compressor with single...][research_liu_li_2016]
- [Coexisting state of surge and rotating stall in a two-stage...][research_sakata_ohta_2017]
- [Numerical Investigation for the Impact of Single Groove on...][research_mao_liu_2017]
- [Observations of the Growth and Decay of Stall Cells during...][research_hickman_morris_2017]
- [Performance Enhancement of a Low Speed Axial Compressor...][research_taghavizenouz_ababafbehbaha_2017]
- [Design of a high-performance centrifugal compressor with new...][research_pakle_jiang_2018]
- [The Inner Workings of Axial Casing Grooves in a One and a...][research_hah_2018]
- [Three-dimensional through-flow modelling of axial flow...][research_righi_pachidis_2018]
- [Effect of a Recirculating Type Casing Treatment on a Highly...][research_kawase_rona_2019_b]
- [Numerical Optimization of a Stall Margin Enhancing...][research_kawase_rona_2019]
- [Rotating Stall Induced Non-Synchronous Blade Vibration...][research_zhao_zhou_2019]
- [Stability enhancement using a new hybrid casing treatment in...][research_li_du_2019]
- [Transonic Compressor Blade Optimization Integrated With...][research_song_zhang_2019]
- [Failure mechanism of casing treatment in improving stability...][research_wang_lu_2020]
- [Optimization of Slots-Groove Coupled Casing Treatment for an...][research_zhu_yang_2020]
- [CFD Investigation of an Axial Compressor with Casing...][research_ahmad_zheng_2021]
- [Dual stability enhancement mechanisms of axial-slot casing...][research_zhang_du_2021]
- [Effects of the foam metal casing treatment on aerodynamic...][research_sun_li_2021_b]
- [Foam-Metal Casing Treatment on an Axial Flow Compressor...][research_sun_li_2021]
- [Mechanism of Stability Enhancement with Shallow ‎Reversed...][research_mechanism_of_2021]
- [Numerical and Experimental Study on Rotating Stall in...][research_miura_yamashita_2021]
- [The role of radial secondary flow in the process of rotating...][research_li_zheng_2021]
- [A Computational Method of Rotating Stall and Surge Transients...][research_ji_hu_2022]
- [AXIAL TRANSONIC COMPRESSOR STALL MECHANISM WITH DIFFERENT...][research_axial_transonic_2022]
- [Analysis of the Flow Field at the Tip of an Axial Flow...][research_wang_song_2022]
- [Analysis on spike-type rotating stall in transonic axial...][research_moru_bo_2022]
- [Effect of self-recirculating casing treatment on the unsteady...][research_guo_gao_2022]
- [Flow Pattern of Rotating Stall Cell in Axial Compressor][research_zhang_wang_2022]
- [Investigation on Mode Characteristics of Rotating Instability...][research_yang_wu_2022]
- [Numerical Investigations on the Rotating Stall in an Axial...][research_marty_castillon_2022]
- [Numerical study on the stability enhancement mechanism of...][research_guo_mao_2022]
- [Research on the stability enhancement mechanism of...][research_chi_chu_2022]
- [Stability Enhancement and Noise Reduction of an Axial...][research_li_dong_2022]
- [Stability improvement without efficiency penalty of a...][research_li_liu_2022]
- [Stall Margin Improvement in a Transonic Compressor With a...][research_hah_2022]
- [Effect of Different Radial Inclined Angles of...][research_effect_of_2023_b]
- [Influence of rotor-stator axial clearance on compressor...][research_li_zheng_2023]
- [Investigation of Vaned-Recessed Casing Treatment in a...][research_akhlaghi_azizi_2023]
- [Mechanism study on the effect of self-circulating casing...][research_mechanism_study_2023]
- [Unsteady body force model for rotating stall in axial...][research_guo_2023]
- [An Optimization Study of Circumferential Groove Casing...][research_liu_chu_2024]
- [Data Mining-Based optimization study on T-shaped multiple...][research_li_chu_2024]
- [Detection of Rotating Stall Inception of Axial Compressors...][research_quan_sun_2024]
- [Effect of wire mesh casing treatment on axial compressor...][research_zhang_zhang_2024_b]
- [Effects of the vena contracta for perforations on stability...][research_sun_yang_2024]
- [Experimental and numerical investigation on rotating stall...][research_zhang_an_2024]
- [Stability enhancement using a new combined casing treatment...][research_ding_chen_2024]
- [Surge-Elimination Strategy for Aero-Engine Transient Control][research_wang_fang_2024]
- [URANS Simulation of Self-Recirculation Casing Treatment in a...][research_urans_simulation_2024]
- [Using Machine Learning Tools for Rotating Stall Warning in a...][research_xue_wang_2024]
- [Analysis of mechanisms affecting the compressor rotor...][research_zhang_yang_2025]
- [Effect of Circumferential Groove Casing Treatment on Surge...][research_gunaydin_dogu_2025]
- [Effect of axial position of wire mesh casing treatment on the...][research_sun_zheng_2025]
- [Experimental and numerical study on stability enhancement...][research_guo_liu_2025]
- [Influence of the casing treatment combined with the tip...][research_wu_cao_2025]
- [Stability Enhancement Using Foam Metal Casing Treatment...][research_dong_liu_2025]
- [Stability Improvement with Slot-Groove Hybrid Casing...][research_liu_chu_2025]
- [Unsteady mechanisms of flow stability improvement for a...][research_zhao_li_2025]
- [Contrastive representation learning for surge prediction in...][research_kim_kim_2026]
- [Experimental and numerical investigation on stability...][research_wang_zhang_2026]
- [Modeling of Impedance Boundary-Controlled Casing Treatment on...][research_dong_wang_2026]
- [Reducing Effect of Secondary Flows on Axial Compressor Rotor...][research_yaylak_pinarbasi_2026]

- [Analyzing and Presenting New Ideas for Anti-Surge Control in...][research_paraguassu_2015]
- [Further Investigation on Transonic Compressor Stall Margin...][research_sun_nie_2015]
- [J0520305 Large-Scale DES Analysis of Rotating Stall Inception...][research_furukawa_yamada_2015]
- [Stall inception and control in a transonic fan, part A...][research_khaleghi_2015]
- [Active Compressor Surge Control System by Using Piston...][research_uddin_gravdahl_2016]
- [Flow phenomena leading to surge in a centrifugal compressor][research_semlitsch_mihaescu_2016]
- [Large eddy simulation of surge inception and active surge...][research_shahin_alqaradawi_2016]
- [Numerical study of the unsteady behaviors and rotating stall...][research_mao_liu_2016]
- [Using wavelets to study spike-type compressor rotating stall...][research_zhang_yu_2016]
- [Constrained nonlinear model predictive control for...][research_imani_jahedmotlagh_2017]
- [Experimental investigation of characteristic frequency in...][research_gao_liu_2017]
- [Simulation of Gas Turbine Engines Considering the Rotating...][research_mikhailov_mikhailova_2017]
- [Stall/surge dynamics of a multi-stage air compressor in...][research_azizi_brouwer_2017]
- [Active Control of Surge Compressor System][research_ka_2018]
- [CFD Analysis of Turbocharger Compressor to Study the Effect...][research_patil_2018]
- [Surge explicit nonlinear model predictive control using...][research_imani_malekizade_2018]
- [Compressor surge based on a 1D-3D coupled method Part 2 Surge...][research_huang_zhang_2019]
- [Determination of Serviceability Limits of a Turboshaft Engine...][research_dvirnyk_pavlenko_2019]
- [Influence of different operating conditions on centrifugal...][research_guan_zhou_2019]
- [Analysis and simulation of active surge control in...][research_molana_khodaparast_2020]
- [Comparison and Sensibility Analysis of Warning Parameters for...][research_margalida_joseph_2020]
- [Compressor Surge Control Using Lyapunov Neural Networks][research_neverlien_moe_2020]
- [Compressor surge control using a new robust adaptive method...][research_zhang_malekgoudarzi_2020]
- [Effect of Forward-Swept Rotor on Stall Margin in an Axial...][research_hamaguchi_sakata_2020]
- [Fractional-Order Surge Control of Active Magnetic Bearings...][research_anantachaisilp_lin_2020]
- [Robust adaptive backstepping active control of compressor...][research_sheng_chen_2020]
- [Surge and Stall Detection Using Acoustic Analysis for Gas...][research_cabreracruz_pezzini_2020]
- [A computational study on compressor inlet restriction to...][research_dehner_selamet_2021]
- [Analysis of Anti-surge Control Method for Axial Flow...][research_analysis_of_2021]
- [Anti-Surge Control of Centrifugal Compressor and...][research_anti_surge_control_2021]
- [Anti-surge Reason and Control Technology of Large Centrifugal...][research_anti_surge_reason_2021]
- [Application Practice of Anti-surge Control in Compressor...][research_application_practice_2021]
- [Application of Centrifugal Compressor Control and Anti-surge...][research_application_of_2021]
- [Application of PLC in Anti-surge Control System of...][research_application_of_2021_b]
- [Design of a robust LMI-based model predictive control method...][research_xie_marrani_2021]
- [Discussion on Anti-surge Control System of Centrifugal...][research_discussion_on_2021_b]
- [Discussion on Control Points of Surge and Anti-surge of...][research_discussion_on_2021]
- [Discussion on the Anti-surge Control Method and Realization...][research_discussion_on_2021_d]
- [Discussion on the Application of Anti-surge Intelligent...][research_discussion_on_2021_c]
- [Finite-time active fuzzy sliding mode approach for deep surge...][research_fu_fu_2021]
- [Finite-time adaptive sliding mode control for compressor...][research_fu_fu_2021_b]
- [Robust active finite-time control of gas compressor system...][research_sun_gu_2021]
- [The Reason and Strategy of Centrifugal Compressor Surge][research_the_reason_2021]
- [Centrifugal compressor anti-surge control system modelling][research_batayev_suleimenov_2022]
- [Compressor Surge Mitigation in Turbocharged Spark-Ignition...][research_galindo_climent_2022]
- [Estimations of Compressor Stall and Surge Using Passage Stall...][research_akhlaghi_azizi_2022]
- [Investigation of Surge in a Transonic Centrifugal Compressor...][research_lou_harrison_2022]
- [Investigation on Broadening Compressor Surge Margin by Using...][research_lin_bai_2022]
- [Stall Behavior in an Ultrahigh-Pressure-Ratio Centrifugal...][research_zhang_lu_2022]
- [Transition from Unsteady Flow Inception to Rotating Stall and...][research_cao_yuan_2022]
- [A Novel Approach for Active Surge Control in Multistage...][research_aribi_boushaki_2023]
- [A high-safety active/passive hybrid control approach for...][research_sheng_chen_2023]
- [Comparative studies on the propagation of rotating stall in a...][research_comparative_studies_2023]
- [Improvement of a Centrifugal Compressor Test Bench to...][research_faltin_beneda_2023]
- [Rapid Prediction of Compressor Rotating Stall Inception Using...][research_fang_sun_2023_b]
- [A new model for compressor surge and stall control][research_shahriyari_firouzabadi_2024]
- [Anti-surge intelligent control of series centrifugal...][research_jia_chen_2024]
- [Research and Simulation of Fuzzy Expert Anti-surge Control...][research_yi_sun_2024]
- [Stall Inception Prediction of Transonic Compressor with Wire...][research_sun_hu_2024]
- [A Unified Framework for Compressor Stall Inception][research_grimshaw_pullan_2025]
- [Gradient-Free Aerodynamic Optimization With Structural...][research_schaffrath_nicke_2025]
- [Review on Compressor Surge Monitoring, Modeling and...][research_du_zhang_2025]
- [Spike Stall Precursor Detection in a Single-Stage Axial...][research_thapa_li_2025]
- [Tip clearance control in conical active magnetic...][research_vu_nguyen_2025]
- [Compressor stall characteristics based on variational mode...][research_zhang_wu_2026]
- [Dynamic coupling evolution mechanism of shock waves and...][research_qiao_chu_2026]
- [On boundedness of solutions of three-state Moore Greitzer...][research_shiriaev_freidovich_2026]
- [Research Overview on Spike Stall Inception and Slotted Casing...][research_zhang_bo_2026]
- [Stability Analysis of a Nonlinear Compressor System Using an...][research_hosseindokht_matas_2026]
- [Surge Disturbance Suppression for a Magnetically Levitated...][research_sun_ding_2026]

### Hot structures moved to materials the X-27 did not have

The aluminium limit computed above is a property of the alloy.
**The contemporary answer is not a better aluminium but a different material**, and the literature covers
titanium alloys, thermal barrier coatings, metallic thermal protection and elevated-temperature creep in
aerospace alloys.

- [Elevated temperature creep deformation of a single crystal...][research_jeffs_lancaster_2015]
- [Aerodynamic Heating of a Hypersonic Projectile with...][research_yadav_guven_2015]
- [Osmotic stress Response of Saccharomyces cerevisiae under HG...][research_gul_2015]
- [Experimental and Numerical Heat Transfer Analyses of Exhaust...][research_dincer_sarioglu_2015]
- [Creep behaviour characterisation of a ferritic steel alloy...][research_alipour_nejad_2016]
- [Optimised Cockpit Heat Load Analysis using Skin Temperature...][research_gupta_rajput_2015]
- [Cryogenic hardening and its effect on properties of an...][research_cryogenic_hardening_2016]
- [Quasi-periodic Aerodynamic Heating in Blunt-fin Induced Shock...][research_zhuang_lu_2015]
- [Effect of heat treatment on elevated temperature tensile and...][research_yuan_shi_2016]
- [Study on Correlation of Aerodynamic Heating Data of a...][research_xinguo_xing_2015]
- [Electrochemical Machining of High-temperature Titanium Alloy...][research_xu_chen_2016]
- [Study on the Unsteady Aerodynamic Heating of the Oscillating...][research_pengju_liang_2015]
- [INFLUENCE OF ANNEALING TEMPERATURE ON THE STRUCTURE AND PHASE...][research_uglov_kuleshov_2016]
- [A method for transient thermal load estimation and its...][research_duda_2016]
- [10.37 Mechanical properties of high strength aluminium alloy...][research_su_young_2017]
- [Comparative study on aerodynamic heating under perfect and...][research_wang_li_2016]
- [A comparative study between conventional and elevated...][research_okorokov_gorash_2017]
- [Study on helium impingement cooling for a sharp leading edge...][research_zhu_zhao_2016]
- [A review on the effect of creep and microstructural change...][research_ochonogor_akinlabi_2017]
- [Thermal and Thermomechanical Performances of Pyramidal Core...][research_xie_zhang_2016]
- [Beta-Phase Decomposition Sequence during Continuous Cooling...][research_gadeev_demakov_2017]
- [A wall grid scale criterion for hypersonic aerodynamic...][research_yang_liu_2017]
- [Disappearance of Strengthening Structure at Elevated...][research_shinozaki_suzuki_2017]
- [Experimental Study on Aerodynamic Heating Induced by Dual...][research_taguchi_mori_2017]
- [Effect of Temperature Field on Formation of Friction Stir...][research_yue_wen_2017]
- [Increasing the heat transfer in intercooler of a two stage...][research_narendhiran_2017]
- [Fatigue life of EN AW-2024 alloy accounting for creep...][research_tomczyk_seweryn_2017]
- [Study of predicting aerodynamic heating for hypersonic...][research_liu_cao_2017]
- [High Temperature Oxidation and Wear Behaviors of Ti V Cr...][research_mi_yao_2017]
- [Aerodynamic Heating of Inflatable Aeroshell in Orbital Reentry][research_takahashi_koike_2018]
- [Laser Welding of BTi-6431S High Temperature Titanium Alloy][research_zeng_oliveira_2017]
- [Aerodynamic heating in transitional hypersonic boundary...][research_zhu_chen_2018]
- [The Effect of ECAP on the Al6061 Matrix and Al-SiCp at...][research_hamid_hammouda_2017]
- [Effects of Transient Heat Transfer on Compressor Stability][research_kiss_spakovszky_2018]
- [Thermal and volumetric property analysis of polymer networks...][research_knowles_tu_2017]
- [Investigation and recent developments in aerodynamic heating...][research_karimi_oboodi_2018]
- [Thermal degradation analysis of innovative PEKK-based carbon...][research_tadini_grange_2017]
- [Investigation of aerodynamic heating in V-shaped cowl-lip of...][research_meng_fan_2018]
- [Creep-rupture Time Prediction of Sanicro25 Austenitic Heat...][research_jing_2018]
- [Newly identified principle for aerodynamic heating in...][research_zhu_lee_2018]
- [Effect of Graphite Addition on Mechanical Properties and...][research_ritapure_kharde_2018]
- [Numerical Simulation of Aerodynamic Heating over Solid Blunt...][research_li_sun_2018]
- [Evolution of Elevated-Temperature Strength and Creep...][research_wang_liu_2018]
- [Numerical investigation of the effect of disk position on the...][research_yadav_bodavula_2018]
- [High temperature oxidation behavior in dieless drawing of...][research_hwang_kuo_2018]
- [The Measurement Method Research of the Aerodynamic Heating...][research_peng_tu_2018]
- [High-Temperature Flow Behaviour and Constitutive Equations...][research_shifeng_jiamin_2018]
- [A grid strategy for predicting the space plane's hypersonic...][research_qu_chen_2019]
- [High-temperature deformation behavior and microstructural...][research_ebied_hamada_2018]
- [Behavior of Titanium Alloys in Aerodynamic Heating of...][research_afanasev_nikitin_2019]
- [Regenerative Cooling Channel Design of a Supersonic Combustor...][research_yang_2018]
- [Hypersonic aerodynamic heating over a flared cone with wavy...][research_si_huang_2019]
- [Design of aluminium alloy beams at elevated temperatures][research_su_zhang_2019]
- [Numerical study on the impact of Mach number on the coupling...][research_niu_sui_2019]
- [Initial Damage Mechanism of Nickel-Based Alloy 625 Under...][research_initial_damage_2019]
- [One-Dimensional Aerodynamic Heating and Ablation Prediction][research_simsek_uslu_2019]
- [Isothermal fatigue damage mechanisms at ambient and elevated...][research_wilson_saintier_2019]
- [Shock-stable flux scheme for predicting aerodynamic heating...][research_qu_kong_2019]
- [Multi-Scale Microstructure Regulation Technology of Near-α...][research_qiao_li_2019]
- [Efficiency and effectiveness enhancement of an intercooler of...][research_chintala_s_2020]
- [Analysis of Resistance of Clad Composite of Structural Steel...][research_sikora_2020]
- [ILES of an array of three subsonic counter-flow jets issuing...][research_shimada_ohwada_2020]
- [Degradation Mechanism of the Strength of a Grain Boundary of...][research_suzuki_suzuki_2020]
- [Numerical Prediction of Flow Field and Aerodynamic Heating in...][research_sun_yang_2020]
- [Degradation Mechanism of the Strength of a Grain Boundary of...][research_ishihara_suzuki_2020]
- [Transient nonlinear heat transfer analysis using a generic...][research_feng_tao_2020]
- [Exploration of Appropriate Tool Material and Lubricant for...][research_singh_priyadarshi_2020]
- [Aerodynamic heating in hypersonic flows][research_smith_2021]
- [Hot Gas Pressure Forming of Ti-55 High Temperature Titanium...][research_wang_shi_2020]
- [Behaviors of Hypersonic Wing under Aerodynamic Heating][research_yang_li_2021]
- [Laser Oscillating Welding of TC31 High-Temperature Titanium...][research_wang_sun_2020]
- [CFD Simulation Strategy for Hypersonic Aerodynamic Heating...][research_yu_ni_2021]
- [Microstructure and Tensile Properties of...][research_chen_mi_2020]
- [Effect of Radiation on Heat Transfer Inside Aeroengine...][research_tang_owen_2021]
- [Non-destructive Evaluation of Precipitation of NbC in Alloy...][research_kasama_suzuki_2020]
- [Optimization of multilayer thermal protection system by using...][research_ren_zhang_2021]
- [Nonlinear flutter and random response of composite panel...][research_lin_shao_2020]
- [Thermal insulation performance and heat transfer mechanism of...][research_chen_zhang_2021_b]
- [Creep Damage and Deformation Mechanism of a Directionally...][research_li_tian_2021]
- [Aerodynamic Heating Ground Simulation of Hypersonic Vehicles...][research_lv_zhang_2022]
- [Creep crack growth of GH3535 alloy at elevated temperatures][research_fan_wang_2021]
- [Enhanced resistance to hypersonic aerodynamic heating of...][research_hao_jiang_2022]
- [Elevated Temperature Tensile Creep Behavior of Aluminum...][research_ji_yuan_2021]
- [Internal energy balance and aerodynamic heating predictions...][research_barone_nicholson_2022]
- [Elevated temperature performance and creep behavior of Y2O3...][research_guo_tian_2021]
- [Numerical Analyses and a Nonlinear Composite Controller for a...][research_lv_zhang_2022_b]
- [Experimental Investigation and Modeling of Damage...][research_tomczyk_seweryn_2021]
- [Reduced aerodynamic heating in a hypersonic boundary layer by...][research_zhu_gu_2022]
- [Extremely high beta-transus temperature of graphene oxide...][research_chen_mi_2021]
- [An IPID Control Method for Aerodynamic Heating Ground...][research_li_kedeng_2023]
- [Influence of high-temperature annealing on structure of...][research_bazhina_bazhin_2021]
- [Conjugate Heat Transfer Validation of Gas Turbine Engine...][research_gorelov_2023]
- [The High-Temperature Deformation Behavior of As-Cast Ti90...][research_wang_zhao_2021]
- [Engineering calculation and analysis of aerodynamic heating...][research_hu_qu_2023]
- [The Influence of Cooling Conditions of Titanium Alloy After...][research_vlasov_gomorova_2021]
- [Machine Learning Strategy for Wall Heat Flux Prediction in...][research_dai_zhao_2023]
- [Thermal Post-Buckling Strength Prediction and Improvement of...][research_mehar_mishra_2021]
- [Transient heat transfer and temperatures in closed compressor...][research_nicholas_pernak_2023]
- [Coupling influences of elevated temperature and strain rate...][research_zhang_zhao_2022]
- [Aerodynamic heating in hypersonic shock wave and turbulent...][research_tang_xu_2024]
- [Dispersoid characteristics and elevated temperature creep...][research_huang_li_2022]
- [Effect of surface ablation on aerodynamic heating over a...][research_han_han_2024]
- [Elevated Temperature Creep and Tensile Performance of...][research_kozakevich_stroh_2022]
- [Evaluation of Various Flow Control Methods in Reducing Drag...][research_evaluation_of_2024]
- [Excellent high-temperature strength and ductility of graphene...][research_chen_mi_2022]
- [Experimental Study on Aerodynamic Heating of Hypersonic...][research_li_liu_2024]
- [Fast Charging of Lithium-Ion Pouch Cells at Elevated...][research_tran_read_2022]
- [Gas turbine engine transient performance and heat transfer...][research_yang_nikolaidis_2024]
- [High-temperature failure mechanism and defect sensitivity of...][research_li_sun_2022]
- [Numerical Method for Predicting Transient Aerodynamic Heating...][research_gozukara_ceylan_2024]
- [Mechanism of stress- and thermal-induced fct → hcp → fcc...][research_wen_kong_2022]
- [Optimization of MTI structure based on material...][research_hao_liu_2024]
- [New HPDC Mg-RE based alloy with exceptional strength and...][research_bai_yu_2022]
- [Simulation of coupling characteristics of motion and heat...][research_huang_bu_2024]
- [Numerical investigation on fatigue life of aluminum brazing...][research_ma_jia_2022]
- [Thermal modal analysis of hypersonic composite wing on...][research_wang_wang_2024]
- [Study on Tensile Fracture Behavior of New Type High...][research_fang_zhang_2022]
- [Transient heat transfer and deformation characteristics of a...][research_zhang_huang_2024]
- [A Study on the High-Temperature Molten Salt Corrosion...][research_wang_li_2023]
- [A Control Method for Thermal Structural Tests of Hypersonic...][research_lu_zhang_2025]
- [Composition and morphology of oxide films formed on PT-7M...][research_composition_and_2023]
- [An engineering method of aerodynamic heating prediction for...][research_chen_he_2025]
- [Elevated Temperature Tensile and Creep Performance of...][research_stroh_sediako_2023]
- [Analysis of Aerodynamic Heating Modes in Thermochemical...][research_he_zhao_2025]
- [Elevated temperature tensile behaviour of 5183 aluminium...][research_geng_zhang_2023]
- [Analysis of the convective heat transfer performance of...][research_zhang_yang_2025_b]
- [Experimental research on online monitoring of high...][research_ren_zheng_2023]
- [Communication blackout and aerodynamic heating reduction via...][research_miyashita_sugihara_2025]
- [Low cycle fatigue and fatigue-creep interaction effects on...][research_cao_zhang_2023]
- [Coupling effects of flow separation and aerodynamic heating...][research_tang_li_2025]

- [A Dendrite-Free Reversible Metallic Lithium Anode in a...][research_imanishi_wang_2015]
- [Degradation of Creep Resistant Ni - Alloy During Aging at...][research_kaczorowski_skoczylas_2015]
- [Microscopic Origin of Strength and Microhardness of Titanium...][research_islam_fermin_2015]
- [Reducing Non Value Adding Aluminium Alloy in Production of...][research_pereira_williams_2015]
- [SiAlON Ceramics for the High Temperature Applications High...][research_uludag_turan_2015]
- [Temperature Distribution in Mechanically Stabilized Earth...][research_kasozi_siddharthan_2015]
- [Test and Analysis of Electric Arc Machining Characteristics...][research_peng_zhai_2015]
- [Titanium Aluminides for Metallic Thermal Protection System of...][research_gupta_ramkumar_2015]
- [Wear Behaviour of Polyurethane Coated Aerospace Aluminium...][research_vijayakumar_senthilvelan_2015]
- [Dissimilar ultrasonic spot welding of aerospace aluminum...][research_zhang_robson_2016]
- [High Temperature Creep Properties of Al-Al4C3-Al2O3 Alloy by...][research_han_seo_2016]
- [On the constitutive equation of AA2017 aluminium alloy at...][research_giuliano_2016]
- [Research on High Temperature Compression and Creep Properties...][research_chen_chen_2016]
- [Reworkable Edgebond Applied Wafer-Level Chip-Scale Package...][research_reworkable_edgebond_2016]
- [The Examination of the Aluminum Alloy 7017 as a Replacement...][research_jones_placzankis_2016]
- [Thermal Aging of Dissimilar-Metal Weld Joints for Reactor...][research_kong_kim_2016]
- [Constitutive Equations for 6061 Aluminum Alloy at Elevated...][research_shen_2017]
- [Corrosion Analysis of Fuel Cell Metallic Materials at...][research_finsgar_2017]
- [Effect of Heat Treatment Temperature-Rate Parameters on...][research_zhelnina_illarionov_2017]
- [Evaluation of metallic filter media for sub-micrometer soot...][research_ou_maricq_2017]
- [Experimental Analysis of the Behaviour of Aluminium Alloy EN...][research_toric_brnic_2017]
- [Influence of Heating Temperature and Cooling Conditions on...][research_vodolazskiy_zhloba_2017]
- [Johnson-Cook based criterion incorporating stress triaxiality...][research_valoppi_bruschi_2017]
- [Optimization of Machiining Parameters in Turning Operation of...][research_kumar_gaur_2017]
- [PHYSICAL AND THERMAL PROPERTIES OF RICE HUSK ASH BLENDED HIGH...][research_physical_and_2017]
- [Structural evolution of Zr-Cu-Ni-Al-N thin film metallic...][research_lee_duh_2017]
- [An additively manufactured metallic manifold-microchannel...][research_zhang_tiwari_2018]
- [Application of the Taguchi method for efficient studying of...][research_khazaali_fereshtehsaniee_2018]
- [Development of a rheological model for creep strain evolution...][research_toric_glavinic_2018]
- [Effect of 1.0% Ni on high-temperature impression creep and...][research_faisal_mazni_2018]
- [Elevated Temperature Deformation Behavior of TA7 Titanium...][research_xiaokang_kuaishe_2018]
- [Experimental determination of the temperature in the cutting...][research_experimental_determination_2018]
- [High-Temperature Creep-Fatigue Behavior of Alloy 617][research_dewa_park_2018]
- [Low cycle fatigue of metallic materials under uniaxialloading...][research_szusta_2018]
- [MATHEMATICAL MODELING AND EXPERIMENTAL STUDY OF FORMING AND...][research_mathematical_modeling_2018]
- [Structure and corrosion resistance of titanium oxide layers...][research_kaminski_witkowska_2018]
- [Vaporization of water droplets with non-metallic inclusions...][research_legros_lutoshkina_2018]
- [Assessment of creep damage models in the prediction of...][research_kan_muransky_2019]
- [Atomic Origins of Radiation-Induced Defects and Interfacial...][research_zhu_qin_2019]
- [Atomic origins of radiation-induced defects and the role of...][research_zhu_qin_2019_b]
- [Effect of Temperature and Microstructural Evolution of...][research_nimal_m_2019]
- [Friction based joining process for high strength aerospace...][research_nithinjosephreddy_sathiskumar_2019]
- [High-Temperature Creep Mechanism of Dual-Ductile-Phase...][research_fujiwara_takagi_2019]
- [High-temperature creep of a CoNiCrAlY bond coat alloy][research_dobes_dymacek_2019]
- [High-temperature creep properties of NIFS-HEAT-2 high-purity...][research_nagasaka_muroga_2019]
- [Numerical investigation of an active TPS for a wing leading...][research_ohwada_shimada_2019]
- [Room and elevated temperature sliding wear behavior and...][research_torgerson_mantri_2019]
- [The Elevated-Temperature Strength Enhancement of a Low-Cost β...][research_khademi_ikeda_2019]
- [Weldability of high-strength aluminium alloy EN AW-7475-T761...][research_kwee_dewaele_2019]
- [Effect of Strain Range on High Temperature Creep-Fatigue...][research_alsmadi_murty_2020]
- [Effect of Substrate Temperature on Structure Formation in...][research_gorunov_2020]
- [Elevated temperature performance of reinforced concrete beams...][research_abdulrasoul_radhi_2020]
- [Experimental Study on the High-Temperature Creep Behavior of...][research_experimental_study_2020]
- [Foreign Object Damage Performance and Constitutive Modeling...][research_xu_cheng_2020]
- [High temperature creep behavior and creep microstructure...][research_ouyang_yang_2020]
- [High-temperature creep deformation in FeCrAl-oxide dispersion...][research_ukai_kato_2020]
- [Microstructural evolution during high-temperature tensile...][research_uemura_kamata_2020]
- [Microstructure of aluminium oxide formed on ferritic FeCrAl...][research_falaakh_kim_2020]
- [Stimulation of Insect Herbivory by Elevated Temperature...][research_havko_kapali_2020]
- [The effect of high-temperature creep on buckling behaviour of...][research_toric_boko_2020]
- [Thermal Behavior of Single-Crystal Diamonds Catalyzed by...][research_hou_zhou_2020]
- [Unravelling the effects of elevated temperature on the...][research_baag_mahapatra_2020]
- [Analysis of Deformation Behavior and Microstructure Changes...][research_yang_ji_2021]
- [Comment on “Theoretical and Experimental Study of Creep...][research_wu_2021]
- [Creep Behavior of Near α High Temperature...][research_yang_tian_2021]
- [Crystallization behavior and mechanical response of metallic...][research_zhang_wang_2021]
- [Elevated Temperature Erosion of Plasma Sprayed Thermal...][research_malvi_roy_2021]
- [Heating and Compression at Elevated Temperature of...][research_gliszczynski_czechowski_2021]
- [High-temperature effects on creep-fatigue interaction of the...][research_alsmadi_murty_2021]
- [Impact of elevated temperature on physiological energetics of...][research_nandy_baag_2021]
- [Influence of solution temperature on microstructure and high...][research_tian_shunke_2021]
- [Method for Rapid Small-Scale Simulated Aluminum Alloy Castings][research_cain_mogonye_2021]
- [Multiaxial fatigue damage and reliability assessment of...][research_li_zhou_2021]
- [Shaping the structure and properties of titanium and Ti6Al7Nb...][research_tarnowski_borowski_2021]
- [Structural rearrangements in confined n-hexane at elevated...][research_zaleski_stefaniak_2021]
- [Theoretical and experimental study of creep damage in alloy...][research_huang_sauzay_2021]
- [Very long life fatigue failure mechanism of electron beam...][research_liu_chen_2021]
- [Creep behavior of 50at%Ni 25at%Ti 25at%Hf high temperature...][research_tugrul_akgul_2022]
- [Heat Behavior and Axial Temperature Optimization of a...][research_ping_hong_2022]
- [Hematological adaptations in diploid and triploid Salvelinus...][research_lahnsteiner_2022]
- [High temperature creep deformation behavior of heat-treated α...][research_mineta_saijo_2022]
- [Microstructure-sensitive modeling of high temperature creep...][research_kumar_capolungo_2022]
- [Oxidation Resistant Nickel Aluminide Coating on Niobium Alloy...][research_zubair_ejaz_2022]
- [Properties of Titanium Zirconium Molybdenum Alloy after...][research_metzger_rienzi_2022]
- [Some Aerospace Applications of 7075 B95 Aluminium Alloy][research_bouzekovapenkova_miteva_2022]
- [The Comparation of Arrhenius-Type and Modified Johnson Cook...][research_yang_liang_2022]
- [Thermal conductivity evaluation for bentonite buffer...][research_yoon_lee_2022]
- [β-Phase-Induced Quasi-Cleavage Fracture Mechanism by...][research_wei_qu_2022]
- [Dry wear characteristics of TC21 titanium alloy at elevated...][research_chen_sun_2023]
- [Effect of Elevated Temperature on the Behavior of Amorphous...][research_shaikh_kahlon_2023]
- [Elevated Temperature Mechanical Characteristics and Fracture...][research_sajadifar_maier_2023]
- [Experimental Study of the Bending Behaviour of the Neovius...][research_monkova_monka_2023]
- [Experimental study on high temperature tensile behaviour of...][research_shirinzadehdastgiri_fuerth_2023]
- [Fine-grained aluminium crossover alloy for high-temperature...][research_samberger_weissensteiner_2023]
- [Fire resistance of low alloy Q420d high-strength steel column...][research_zhu_xing_2023]
- [Room temperature nanoindentation creep behavior of...][research_zhu_wu_2023]
- [Statistical Analysis of Titanium Alloy Surface Processing on...][research_zeng_buckley_2023]
- [Strength and Toughness of Hot-Rolled TA15 Aviation Titanium...][research_li_pan_2023]
- [Structure and Wear Performance of a Titanium Alloy by Using...][research_li_wang_2023]
- [Superior resistance to high temperature creep in an...][research_kim_ramlim_2023]
- [The development of ultrafine grain structure in an additively...][research_simonelli_zou_2023]
- [Thermal stability investigations of different aerogel...][research_kovacs_csik_2023]
- [Titanium Alloy Fasteners for Aerospace Engineering][research_vorobev_galiakhmetov_2023]
- [A Combined Experimental and Numerical Calibration Approach...][research_tuninetti_sepulveda_2024]
- [Characterization and unified modelling of creep and...][research_li_chen_2024]
- [Design and Rate Control of Large Titanium Alloy Springs for...][research_li_xu_2024]
- [Design and performance verification of thermal protection...][research_zhang_zhang_2024]
- [Fatigue Behaviour and Life Prediction of YSZ Thermal Barrier...][research_tao_wang_2024]
- [Fatigue Life Prediction for 2060 Aluminium Lithium Alloy with...][research_li_li_2024]
- [High-Temperature Creep Resistance of FeAlOY ODS Ferritic Alloy][research_dymacek_jary_2024]
- [High-temperature oxidation behavior of TA15 aerospace...][research_zhong_yu_2024]
- [Structure and Properties of Bioactive Titanium Dioxide...][research_witkowska_borowski_2024]
- [Thermal-structural analysis for reusable thrust chamber using...][research_qi_jin_2024]
- [A New Continuous Bending and Straightening Curve Based on the...][research_sui_lu_2025]
- [A Study on the Evaluation of Ultrasonic Propagation...][research_park_lee_2025]
- [Constitutive Description of Flow Curve for Duplex Titanium...][research_shimomura_park_2025]
- [Effect of elevated temperature and stress state on ductile...][research_feng_chen_2025]
- [Experimental Investigation on the Residual Compressive...][research_kumar_sastri_2025]
- [Experimental investigation of ultrasonic surface rolling...][research_zhang_cheng_2025]
- [High-Temperature Tensile Grain Evolution and Mechanical...][research_li_dong_2025]
- [High-temperature fatigue and creep damage mechanism in...][research_bhandari_gaur_2025]
- [Research of twist-bend forming and performance control of...][research_feng_chen_2025_b]
- [Shape memory polybutene-1 alloy with superior...][research_meng_ma_2025]
- [Effect of Elevated Temperature Thermal Aging/Exposure on...][research_acharya_karbhari_2026]
- [Effect of vacuum annealing on the structure of...][research_bilous_vrzhizhevskyi_2026]
- [Efficient and sustainable surface modification of TC17...][research_ye_chuai_2026]
- [Elevated Temperature Creep of a Eutectic FeNiMnAlCr High...][research_jiang_liu_2026]
- [Multidirectional forging induced deformation mechanisms and...][research_chakraborty_khan_2026]
- [Oxidation Kinetics, Phase Evolution, and Surface...][research_singh_borras_2026]
- [Remarkable enhancement of high temperature creep resistance...][research_yu_yu_2026]
- [Structure and fatigue of titanium alloy samples under laser...][research_shiryaev_milenin_2026]
- [Thermal contact conductance and thermal rectification at...][research_khan_tariq_2026]

### Conceptual design became a numerical discipline

The sizing exercise above is a 1970s method executed by hand.
**Contemporary conceptual design is multidisciplinary optimisation**, and the part of it most relevant here
is the literature on *derivative* design, meaning how much of an existing aircraft can be kept when the
requirement changes.

**The Lancer is a derivative-design problem and the modern literature has a name for its failure mode.**
Reusing a fuselage, an aerofoil and a systems architecture constrains the solution far more than the
retained parts are worth, and quantifying that trade is now a research subject in its own right.

- [A knowledge-based integrated aircraft conceptual design...][research_munjulury_staack_2015]
- [A robust optimization methodology for preliminary aircraft...][research_prigent_marechal_2015]
- [Development of a multidisciplinary design optimization...][research_allison_morris_2015]
- [Aircraft derivative design optimization considering global...][research_park_chung_2016_b]
- [A digital thread approach to support manufacturing-influenced...][research_siedlak_pinon_2017]
- [An instructive algorithm for aircraft elevator sizing to be...][research_alshamma_ali_2017]
- [Database Adaptive Fuzzy Membership Function Generation for...][research_tyan_nguyen_2017]
- [Coupled aeropropulsive design optimisation of a...][research_gray_martins_2018]
- [Design Optimization of the Cowl Cross Bar - Light Cowl Cross...][research_kong_park_2018]
- [Design optimization of the last stage of a 4.5-stage...][research_luo_2018]
- [Uncertainty quantification and robust design optimization...][research_panzeri_savelyev_2018]
- [Aerostructural Design Optimization Using a Multifidelity...][research_bryson_rumpfkeil_2019]
- [Application of Agile Model-Based Systems Engineering in...][research_krupa_2019]
- [Application of deep learning based multi-fidelity surrogate...][research_tao_sun_2019]
- [Conceptual Design of a Counter-Rotating Fan System for...][research_leebyungjoon_lioumayfun_2019]
- [Three-dimensional optimal design of a cooled turbine...][research_ba_wang_2019]
- [A framework for enhanced decision-making in aircraft...][research_bianchi_secco_2020]
- [Application of a PCA-DBN-based surrogate model to robust...][research_tao_sun_2020]
- [Multi-objective design optimization of the combinational...][research_ju_sun_2020]
- [Multidisciplinary Design Optimization of Low-Boom Supersonic...][research_wuli_karlgeiselhart_2020]
- [Robust aerodynamic shape optimization using a novel...][research_tian_li_2020]
- [Aerodynamic Design Optimization of a Staggered Rotors...][research_zhu_nie_2021]
- [Analysis of the Impact of Requirement-Sketch Sequencing on...][research_spivey_ortiz_2021]
- [Conceptual Design of Extreme Sea-Level Early Warning Systems...][research_denamiel_huan_2021]
- [Conceptual design and integration of a propulsion system for...][research_hutchinson_lawrence_2021]
- [Enhanced pin-access prediction and design optimization with...][research_abazyan_melikyan_2021]
- [Global Aerostructural Design Optimization of More Flexible...][research_wunderlich_dahne_2021]
- [Single commercial aircraft system value evaluation method...][research_chen_ma_2021]
- [Structural Design Synthesis of Aircraft Engine Pylons at...][research_stefanovic_livne_2021]
- [The use of FEA and semi-empirical equations for weight...][research_kowalski_goraj_2021]
- [A Safety-Focused System Architecting Framework for the...][research_jeyaraj_liscouethanke_2022]
- [Aerodynamic Design Optimization of a Transonic...][research_chau_zingg_2022]
- [Airplane Design Optimization for Minimal Global Warming Impact][research_proesmans_vos_2022]
- [An analysis method of dynamic requirement change in product...][research_sun_guo_2022]
- [Conceptual design of sonic boom stealth supersonic transports][research_sun_smith_2022]
- [Machine-Learning-Aided Design Optimization of Internal Flow...][research_pai_weibel_2022]
- [A Simulation Framework for Aircraft Take-Off Considering...][research_abusalem_palaia_2023_b]
- [A self-adaptive local diversity-preserving NSGA-II for the...][research_yan_zhang_2023]
- [A sequential algorithm for decoupling the multidisciplinary...][research_wang_xu_2023]
- [Annual Energy Production Design Optimization for PM...][research_yang_zhang_2023]
- [Framework for Initializing the Conceptual Design of...][research_wilson_figliola_2023]
- [Machine learning algorithms in ship design optimization][research_peri_2023]
- [Medium-Range Aircraft Conceptual Design from a Local Air...][research_abusalem_palaia_2023]
- [Model‐based‐systems‐engineering for conceptual design An...][research_shoshanytavory_peleg_2023]
- [Preliminary Design and Performance-Stability Analysis of a...][research_victorantonio_yan_2023]
- [Supersystem digital twin-driven framework for new product...][research_haynes_yang_2023]
- [Aerodynamic and aeroacoustic design optimization of UAVs...][research_sarikaya_zarri_2024]
- [Aerodynamic design optimization of the hypersonic inward...][research_qu_wang_2024]
- [Computational fluid dynamics-based design optimization of...][research_zhang_zhang_2024_c]
- [Conceptual Design of Layered Distributed Propulsion System to...][research_li_lu_2024]
- [Conceptual design methodology and performance evaluation of...][research_hu_li_2024]
- [Investigation about Partial Turboelectric Propulsion System...][research_yamada_himeno_2024]
- [Neural-Network-Based Model for Trailing-Edge Flap Loads in...][research_stephan_heyen_2024]
- [Surrogate-based integrated design optimization for...][research_ji_huang_2024]
- [Variable-fidelity surrogate model based on transfer learning...][research_leng_feng_2024]
- [A Digital Twin-Enhanced KJ-Kano Framework for User-Centric...][research_niu_ye_2025]
- [A Robust Aerodynamic Design Optimization Methodology for UAV...][research_wang_huo_2025]
- [A Study on the Conceptual Design of a 50-Seat Supersonic...][research_kawanabe_lei_2025]
- [A novel explainable AI-based design optimization framework to...][research_iqbal_shabbir_2025]
- [Comparison of Actual Hybrid-Electric Flights with a Digital...][research_eisenhut_bender_2025]
- [Design Optimization of Rear-Fuselage Boundary-Layer Ingestion...][research_battiston_magrini_2025]
- [Fast Buckling Analysis of Stiffened Composite Structures for...][research_stamatelos_labeas_2025]
- [Integrated Design Optimization of Environmental Control...][research_giuffre_ascione_2025]
- [Integrated Surrogate Model-Based Approach for Aerodynamic...][research_cheng_li_2025]
- [Methods for Conceptual Design of Aircraft under Uncertainty][research_veresnikov_2025]
- [Preliminary Design Criteria for Supersonic Biplane][research_he_shi_2025]
- [Using Global Market Demand Analysis to Guide Conceptual...][research_wuli_karlgeiselhart_2025]
- [Aircraft Weight Estimation Using Surveillance Data Based on...][research_matsuda_matsuno_2026]
- [An MDAO Method for Assessing Benefits of Variable Cycle...][research_yang_yu_2026]
- [Computational Framework for Aerodynamic Structural Coupling...][research_qin_2026]

- [Collaborative multidisciplinary design optimization A...][research_safavi_tarkian_2015]
- [Comparative Assessment of Strut-Braced and Truss-Braced Wing...][research_chakraborty_nam_2015]
- [Conceptual Design and Experimental Demonstration of a...][research_zhang_zhou_2015]
- [Conceptual Design of Low-Boom Aircraft with Flight Trim...][research_ordaz_geiselhart_2015]
- [Conceptual design and performance simulation of a space...][research_tahmasebi_karimim_2015]
- [Coupling equivalent plate and beam models at conceptual...][research_riccobene_ricci_2015]
- [Effect of Flutter on the Multidisciplinary Design...][research_mallik_kapania_2015]
- [LMI based robust controller design approach in aircraft...][research_zeng_chen_2015]
- [Uncertainty-based MDO for aircraft conceptual design][research_park_lee_2015]
- [Application of Multidisciplinary Systems‐of‐Systems...][research_subramanian_delaurentis_2016]
- [Approximation of Off-Body Sonic-Boom Analysis for Low-Boom...][research_ordaz_li_2016]
- [CONCEPTUAL DESIGN OF A VTOL REMOTELY PILOTED AIRCRAFT FOR...][research_udroiu_blaj_2016]
- [Conceptual Design Study on Liquid Hydrogen-Fueled Supersonic...][research_yuhara_makino_2016]
- [Conceptual design of a nonplanar wing airliner][research_garciabenitez_cuernorejado_2016]
- [Development of an Augmented Conceptual Design Tool for...][research_development_of_2016]
- [Framework of Conceptual Design Methodology for Hybrid Buoyant...][research_haque_asrar_2016]
- [Integration Analysis of Conceptual Design and...][research_cheng_yue_2016]
- [Kriging-assisted design optimization of S-shape supersonic...][research_venturelli_benini_2016]
- [Monte Carlo Information-Reuse Approach to Aircraft Conceptual...][research_ng_willcox_2016]
- [Multi-criteria optimization of an aircraft propeller...][research_schatz_hermanutz_2016]
- [Multi-disciplinary analysis and optimisation methodology for...][research_roysalam_bil_2016]
- [Multidisciplinary Design Optimization of Quiet...][research_bryson_marks_2016]
- [Transport Aircraft Conceptual Design Optimization Using Real...][research_singh_sharma_2016]
- [Uncertainty based aircraft derivative design for requirement...][research_park_chung_2016]
- [Aircraft Design Optimization for Lowering Community Noise...][research_sahai_snellen_2017]
- [Application of Multidisciplinary Design Optimization on...][research_pan_huang_2017]
- [Cross-flow effects regarding laminar flow control within...][research_schueltke_stumpf_2017]
- [Performance based multidisciplinary design optimization of...][research_afonso_vale_2017]
- [The relevance of reliability-based topology optimization in...][research_lopez_baldomir_2017]
- [Wing Fuel-Tank Heat-Sink Calculation for Conceptual Aircraft...][research_roland_rumpfkeil_2017]
- [Aerodynamics and Conceptual Design Studies on an Unmanned...][research_cummings_liersch_2018]
- [Aircraft robust multidisciplinary design optimization...][research_babaei_setayandeh_2018]
- [Application of virtual flight test framework with derivative...][research_park_chung_2018]
- [Comparison of Aircraft Conceptual Design Weight Estimation...][research_brycelhorvath_douglaspwells_2018]
- [Composite stiffened panel sizing for conceptual tail design][research_sanchezcarmona_cuernorejado_2018]
- [Conceptual Design Code Validation and Optimization of...][research_thein_2018]
- [Conceptual Design and Evaluation of Upset-Recovery Systems...][research_smaili_rouwhorst_2018]
- [Development of Conceptual Design Methodology and Initial...][research_lee_lim_2018]
- [Efficient Aircraft Multidisciplinary Design Optimization and...][research_york_ozturk_2018]
- [Evaluation of the Impacts of Objective Function Definition in...][research_dibianchi_orra_2018]
- [Low-Boom/Low-Drag Design Optimization of Innovative...][research_ban_yamazaki_2018]
- [Mission-Based Multidisciplinary Aircraft Design Optimization...][research_albuquerque_gamboa_2018]
- [Multidisciplinary Optimization of Unmanned Aircraft...][research_papageorgiou_tarkian_2018]
- [Multipoint optimization on fuel efficiency in conceptual...][research_chai_yu_2018]
- [Multistage Reliability-Based Design Optimization and...][research_nam_mavris_2018]
- [Preliminary design study for a future unmanned cargo aircraft...][research_hasan_sachs_2018]
- [Range and Payload Trades Study on Aircraft Conceptual Design][research_mintint_2018]
- [Topology optimization of a novel fuselage structure in the...][research_liu_zhang_2018]
- [Conceptual Design and Performance Optimization of a Tip...][research_lappas_ikenaga_2019]
- [Conceptual design of an aircraft for Mars mission][research_kwiek_2019]
- [Integration assessment of conceptual design and intake...][research_bravomosquera_abdalla_2019]
- [Low-boom low-drag optimization in a multidisciplinary design...][research_sun_smith_2019]
- [Multidisciplinary design optimization of aircraft wing using...][research_benaouali_kachel_2019]
- [On the benefits of applying topology optimization to...][research_munk_auld_2019]
- [Pattern Search Algorithm for Blackboard-Based...][research_jelev_keane_2019]
- [Remotely Piloted Aircraft Systems conceptual design...][research_gomezrodriguez_sanchezcarmona_2019]
- [Design optimization of a business aircraft seat considering...][research_trivers_carrick_2020]
- [Engine weight estimation of fifth generation fighter aircraft...][research_karabacak_turan_2020]
- [Multidisciplinary Design Optimization Framework with Coupled...][research_sgueglia_schmollgruber_2020]
- [Multidisciplinary design and optimization of an innovative...][research_zhang_zhang_2020]
- [Multidisciplinary design optimization of an aircraft by using...][research_setayandeh_babaei_2020]
- [Simulation Methodologies of Engine Noise Shielding by Wings...][research_vieira_koch_2020]
- [Thermal risk prediction methodology for conceptual design of...][research_sanchez_liscouethanke_2020]
- [A multidisciplinary design optimization for conceptual design...][research_silva_resende_2021]
- [Application of Noise Certification Regulations within...][research_noding_bertsch_2021]
- [Comparing Filtering Multifidelity Optimization Strategies...][research_chell_hoffenson_2021]
- [Conceptual design and optimization of a general aviation...][research_nicolay_karpuk_2021]
- [Design of an aircraft engine bracket using stress-constrained...][research_wu_qiu_2021]
- [Improving aircraft conceptual design through parametric CAD...][research_sanchez_liscouethanke_2021]
- [Multidisciplinary Design Optimization of Low-Boom Supersonic...][research_li_geiselhart_2021]
- [Multidisciplinary Design Optimization of the Actuation System...][research_pettesduler_roboam_2021]
- [Selecting Technologies in Aircraft Conceptual Design Using...][research_roelofs_kurowicka_2021]
- [Sensitivity factors of aircraft mass for the conceptual design][research_kretov_2021]
- [A Fast Aerodynamic Model for Aircraft Multidisciplinary...][research_moens_2022]
- [Conceptual Aircraft Empennage Design Based on...][research_liu_jiang_2022]
- [Conceptual Design for Assembly methodology formalization...][research_formentini_bouissiere_2022]
- [Conceptual Design of Boundary-Layer-Ingesting Aircraft...][research_ahuja_mavris_2022]
- [Development of a Flight Simulator for Conceptual Aircraft...][research_hon_karpuk_2022]
- [Multi-objective, Multidisciplinary Optimization of Low-Boom...][research_li_geiselhart_2022]
- [Multidisciplinary Design Optimization of Twin-Fuselage...][research_ma_zhang_2022]
- [A Bifurcation Theoretic Integrated Methodology for Aircraft...][research_khatri_sinha_2023]
- [A Meta-Model for composite wingbox sizing in aircraft...][research_toffol_ricci_2023]
- [Adjoint-Based Aerodynamic Design Optimization and Drag...][research_rao_chen_2023]
- [Conceptual Design and Optimization of Distributed Electric...][research_wu_gao_2023]
- [Conceptual Design of a Nonconstant Swept Flying Wing Unmanned...][research_aleisa_kontis_2023]
- [Conceptual design modeling by the novel aircraft conceptual...][research_unal_oz_2023]
- [Robust multidisciplinary analysis and optimization for...][research_saporito_daronch_2023]
- [Robust shape optimization under model uncertainty of an...][research_demir_gorguluarslan_2023]
- [Scoring Approach to Assess Maintenance Risk for Aircraft...][research_selim_liscouethanke_2023]
- [Structured Expert Judgment Elicitation in Conceptual Aircraft...][research_todorov_rakov_2023]
- [A Framework for Aircraft Conceptual Design and...][research_hosseini_vaziryzanjany_2024]
- [Atmospheric Aircraft Conceptual Design Based on...][research_lukyanov_hoang_2024]
- [Bayesian optimization with hidden constraints for aircraft...][research_tfaily_diouane_2024]
- [Design optimization for the entire aircraft structure of...][research_zhang_zhou_2024]
- [High-dimensional mixed-categorical Gaussian processes with...][research_saves_diouane_2024]
- [Multidisciplinary Design Optimization of Transonic Wings with...][research_mosca_sudhi_2024]
- [Robust Design Optimization of Supersonic Biplane Airfoil...][research_hanazaki_yamazaki_2024]
- [Structural and Aerodynamic Preliminary Design Optimization...][research_krawczyk_paul_2024]
- [Wing design optimization and stall analysis with Co-flow Jet...][research_jiang_yao_2024]
- [An equal-margin control method for inlet unstart protection...][research_wang_tang_2025]
- [Conceptual Design of Aircraft System Routing Architectures...][research_taneich_rinoie_2025]
- [Conceptual design of next-generation stealth fighter aircraft...][research_surwase_kumar_2025]
- [Coupled Aeropropulsive Design Optimization of an Over-wing...][research_abdulkaiyoom_yildirim_2025]
- [Credibility-Based Multidisciplinary Design Optimization of...][research_wahler_maruyama_2025]
- [Improved FPA for aircraft conceptual design][research_shi_2025]
- [Initial Weight Modeling and Parameter Optimization for...][research_yang_wan_2025]
- [Multi-objective topology optimization design of aircraft...][research_xiao_meng_2025]
- [Multidisciplinary Design Optimization of Aircraft for Climate...][research_palaia_2025]
- [Parametric Geometry Modeling for Conceptual Design of...][research_xu_yu_2025]
- [Revitalizing Intangible cultural heritage via derivative...][research_wang_chen_2025]
- [Weight Estimation and Architecture Definition of Fuel Systems...][research_rodriguez_liscouethanke_2025]
- [A Roadmap for Twin-Fuselage Aircraft Conceptual Design][research_cobogonzalez_cuernorejado_2026]
- [Advancing early-phase conceptual design tool AVDS with...][research_patel_chudoba_2026]
- [An automated surrogate model generation framework for rapid...][research_golombek_bustamante_2026]
- [Bayesian optimization framework for mixed-variable wing...][research_xu_zhang_2026]
- [Comparative Study of Optimization Models for Conceptual...][research_veresnikov_goncharenko_2026]
- [Consistent Coupling of Aeropropulsive and Engine Performance...][research_li_geiselhart_2026]
- [FAST A Future Aircraft Sizing Tool for Conventional and...][research_mokotoff_arnson_2026]
- [Generative AI-driven inverse design optimization of composite...][research_sun_chen_2026]
- [Multidisciplinary Design Optimization for the Conceptual...][research_duan_wan_2026]
- [Parametric Reduced-Order Model Drag Polars for Supersonic...][research_felix_perron_2026]
- [Predicting Conceptual Aircraft Design Parameters Using...][research_arnson_aljaber_2026]
- [Preliminary Conceptual Design of a Closed-Wing High-Altitude...][research_riccio_giaquinto_2026]
- [Simultaneous Trajectory and Design Optimization of Small VTOL...][research_fernandez_bronz_2026]
- [Solid Oxide Fuel Cell Performance and Sizing Model for Novel...][research_warsch_carbone_2026]
- [Spatial all-wing configuration for the conceptual design of...][research_hu_zhao_2026]
- [System-Level, Large-Scale Multidisciplinary Design...][research_ruh_warner_2026]
- [Transfer learning in surrogate modeling with emphasis on...][research_tfaily_bartoli_2026]
- [Two-dimensional principal component analysis and stall...][research_chen_zheng_2026]
- [Aircraft Wing Weight Estimation][research_carreyette_1950]
- [RAMJET TECHNOLOGY. CHAPTER 3. ENGINE REQUIREMENTS FOR...][research_walker_1952]
- [Ramjet supersonic “flight tests”][research_ramjet_supersonic_1958]
- [RESULTS OF THE PHASE II LONG-TERM ENVIRONMENTAL STORAGE TEST...][research_whitney_1963]
- [Design optimization of aircraft structures with thermal...][research_hackman_richardson_1964]
- [A fundamental approach to aircraft manufacturing cost...][research_gregorytj_wilcoxde_1970]
- [Prediction of wing group weight for preliminary design][research_torenbeek_1971]
- [Preliminary Design and Cost Study of Recirculating Chromate...][research_clark_hallow_1972]

### Agility metrics settled the argument the competition was having

Energy manoeuvrability was contested in 1970 and is standard now.
**The contemporary literature on agility metrics, air-combat modelling and trajectory optimisation is the direct descendant of the diagrams Boyd was drawing**,
and it vindicates the framework on which the Lancer performs well.

**Which sharpens the historical point.** On the metric that won the argument, the Lancer was a good
aeroplane. It lost anyway, and it lost on cost, logistics and timing rather than on performance.

- [Agility and Motor Coordination Assessment of Children of...][research_fernandodelimapaulo_2015]
- [Benchmarking agility assessment approaches a case study][research_vinodh_aravindraj_2015]
- [The metric characteristics of specific speed and agility...][research_erceg_miletic_2016]
- [Agility assessment using fuzzy logic approach a case of...][research_suresh_patri_2017]
- [Assessment of repeated reactive agility performance in...][research_matlak_racz_2017]
- [Research on the Air Combat Countermeasure Generation of...][research_ji_yu_2018]
- [Design and assessment of energetic agility measures in...][research_kuhlmann_sauer_2019]
- [A Catalogue of Agile Smells for Agility Assessment][research_telemaco_oliveira_2020]
- [Agility and Assessment in the Age of COVID‐19 How Fast Can a...][research_kolb_2020]
- [Air Combat Maneuver Decision Based on Reinforcement Genetic...][research_xie_yang_2020]
- [Business Intelligence Agility, Informing Agility and...][research_skyrius_valentukevice_2020]
- [Evaluation of a Reactive Agility Assessment Device in Youth...][research_hoffman_2020]
- [Evasive Maneuver Strategy for UCAV in Beyond-Visual-Range Air...][research_yang_zhou_2020]
- [Improving Maneuver Strategy in Air Combat by Alternate Freeze...][research_wang_li_2020]
- [Learning agility in a high change world][research_bywater_hezlett_2020]
- [Maneuver Decision of UAV in Short-Range Air Combat Based on...][research_yang_zhang_2020]
- [Maneuver Strategy Generation of UCAV for within Visual Range...][research_kong_zhou_2020]
- [Performances of the Canadian Agility and Movement Skill...][research_cao_zhang_2020]
- [Application of Deep Reinforcement Learning in Maneuver...][research_hu_yang_2021]
- [Assessment of Organizational Agility in Software Projects][research_masilamani_suresh_2021]
- [Assessment of Team Agility in Internet of Things Projects][research_patil_suresh_2021]
- [Autonomous maneuver strategy of swarm air combat based on DDPG][research_wang_hu_2021_b]
- [CARAF Crypto Agility Risk Assessment Framework][research_ma_colon_2021]
- [Sensor Based Agility Assessment in Sport][research_hribernik_kes_2021]
- [The Link Between Organizational Agility And VUCA An Agile...][research_bundtzen_hinrichs_2021]
- [UAV cooperative air combat maneuver decision based on...][research_jiandong_qiming_2021]
- [WITHDRAWN Agility assessment framework for automotive service...][research_suresh_nirmal_2021]
- [WITHDRAWN Agility assessment in retail store environment...][research_sandeeprameshkumar_suresh_2021]
- [A New Organizational Agility Assessment Approach Applied in...][research_gergin_colak_2022]
- [ASSESSMENT OF ORGANIZATIONAL AGILITY ADAPTATION AND...][research_gurbuz_hatunoglu_2022]
- [Air Combat Maneuver Decision Method Based on A3C Deep...][research_fan_xu_2022]
- [Assessment framework for workforce agility in higher...][research_menon_suresh_2022]
- [Autonomous Maneuver Decision Making of Dual-UAV Cooperative...][research_hu_wang_2022]
- [Autonomous Maneuver Decision of Air Combat Based on Simulated...][research_li_lyu_2022]
- [Comparison of Speed, Agility and Reactive Agility Performance...][research_egesoy_2022]
- [Maneuver Decision-Making for Autonomous Air Combat Based on...][research_zhang_wei_2022]
- [Vision-Based 3D Aerial Target Detection and Tracking for...][research_zhong_zhao_2022]
- [Agility assessment framework for modular and offsite...][research_salama_said_2023]
- [Air combat target maneuver trajectory prediction based on...][research_zhifei_yingxin_2023]
- [Assessment of Change of Direction and Agility. Running and...][research_bekris_gioldasis_2023]
- [Assessment of Factors Influencing Agility in Start-Ups...][research_sreenivasan_ma_2023]
- [Assessment of Speed and Agility Female Students Using the...][research_assessment_of_2023]
- [Deep Reinforcement Learning-Based Air-to-Air Combat Maneuver...][research_bae_jung_2023]
- [Deep reinforcement learning-based air combat maneuver...][research_wang_wang_2023_c]
- [UAV maneuver decision-making via deep reinforcement learning...][research_zheng_duan_2023]
- [Air combat maneuver decision based on deep reinforcement...][research_zhang_wang_2024]
- [An Intelligent Maneuver Decision-Making Approach for Air...][research_li_fang_2024]
- [Autonomous Air Combat Maneuver Decision-Making Based on...][research_wang_zhou_2024]
- [Effects of Plyometrics, Agility, and Resistance Training on A...][research_effects_of_2024]
- [Explainable Basic-Fighter-Maneuver Decision Support Scheme...][research_wang_tu_2024]
- [It Takes a Campus Agility in the Development of Directed...][research_whitney_skinner_2024]
- [Mixed-Reward Multiagent Proximal Policy Optimization Method...][research_peng_li_2024]
- [Research on the Reward Design Method for Deep Reinforcement...][research_zhang_dong_2024]
- [UAV swarm air combat maneuver decision-making method based on...][research_zheng_wei_2024]
- [Air Combat Maneuver Decision Based on Deep Reinforcement...][research_li_dong_2025_b]
- [An air combat maneuver decision-making approach using coupled...][research_yang_wang_2025]
- [Development and Evaluation of Transformer-Based Basic Fighter...][research_dong_he_2025]
- [Hybrid deep learning network-based approach for air combat...][research_sheeba_lingeshwari_2025]
- [Identifying Key Assessment Factors for Human Capital Agility...][research_sumadireja_dachyar_2025]
- [Robust Close-Range Air Combat Maneuver Decision-Making Method...][research_liu_yu_2025]

- [Future Challenges for Civil Aircraft Systems How to Combine...][research_comes_2015]
- [Visual Perception-Based Target Aircraft Movement Prediction...][research_dong_huang_2015]
- [SELECTION OF A FIGHTER AIRCRAFT TO IMPROVE THE EFFECTIVENESS...][research_ali_asghar_2017]
- [Suggestion for aircraft flying qualities requirements of a...][research_wang_guo_2017]
- [Using agility to combat cyber attacks][research_anderson_2017]
- [Agility and coordination testing in combat sports and martial...][research_nikitenko_2018]
- [Assessment of Plyometric Training on Agility In Basketball...][research_singh_2018]
- [Control Allocation for an Over-Actuated Aircraft Based on...][research_liu_gao_2018]
- [Agility and Coordination Testing in Hand-to-Hand Combat Sports][research_platonov_nikitenko_2019]
- [Deep Learning-Based Opponent Aircraft Attitude Detection in...][research_dong_2019]
- [Metrics Towards Measuring Cyber Agility][research_mireles_ficke_2019]
- [Influence of unmanned combat aerial vehicle agility on...][research_wang_wang_2020]
- [Organizational Agility Assessment for Higher Education...][research_menon_2020]
- [A hierarchical decision-making method for multi-aircraft air...][research___2022]
- [Deriving Priorities between Autonomous Functions of Unmanned...][research_jung_oh_2022]
- [Hierarchical multi‐agent reinforcement learning for...][research_kong_zhou_2022]
- [High-Fidelity Decision-Making and Simulation for Cooperative...][research_wang_wang_2022]
- [Modeling of aircraft performance parameters with...][research_oruc_baklacioglu_2022]
- [Proverse Yaw Agility of Lift Distributions][research_kigotho_bodylski_2022]
- [Combat Aircraft Agility Metrics - A Review][research_paranjape_ananthkrishnan_2023]
- [Employee Experience A Metric for Future Workforce Agility][research___2023]
- [Hierarchical reinforcement learning from competitive...][research_kong_zhou_2023]
- [Modeling of energy maneuverability based specific excess...][research_oruc_baklacioglu_2023]
- [THE INFLUENCE OF LEARNING AGILITY, CHANGE AGILITY, MENTAL...][research_mjamhuri_nizar_2024]
- [Design and implementation of airborne information-energy...][research_lin_li_2025]
- [Pengaruh Latihan Speed Agility untuk Meningkatkan Kecepatan...][research_ladiaapsarihasibuan_agussulastio_2025]
- [Aerodynamic and Static Aeroelastic Analysis of a High-Agility...][research_reinbold_breitsamter_2026]
- [Unpacking marketing agility Effects on customer mindset...][research_agag_ali_2026]

### Acquisition scholarship has a category for what happened

The Lancer's fate is a case in a well-developed literature on competitive prototyping, defence acquisition
and arms transfer.
**A private venture seeking government funds to build a demonstrator for an export market it had already lost is a recognisable pattern**,
and the modern work on prototype policy and on foreign military sales is where a reader should go for the
general case.

- [Aircraft Acquisition Conceptual Framework][research_yusof_rahim_2017]
- [Study on longitudinal stability improvement of flying wing...][research_xu_zhou_2015]
- [No wings attached? Civil military relations and agent...][research_reykers_fonck_2019]
- [Advanced Distributed Flight Control System Architecture with...][research_rao_vpatel_2016]
- [The United States and European Defense Cooperation European...][research_hellemeier_2019]
- [Longitudinal Stability Augmentation of Seaplanes in Planing][research_ito_dhaene_2016]
- [The Comparative Analysis of the Industrial Policy Impact on...][research_azam_2020]
- [Longitudinal stability characteristics of the LASTA airplane][research_milenkovicbabic_samardzic_2017]
- [ANALYSIS OF THE CURRENT STATE OF THE EXPORT POTENTIAL OF...][research_romanov_2021]
- [Design for Robust Aircraft Flight Control][research_hess_peng_2018]
- [Review of Indonesian government policy in procurement plan of...][research_wardana_cahyana_2022]
- [Flight control and flight experiments of a tilt-propeller...][research_oznalbant_kavsaoglu_2018]
- [UN Peacekeeping Operations Features of Arms and Equipment...][research_rebizov_2022]
- [Propeller thrust force contribution to airplane longitudinal...][research_milenkovicbabic_2018]
- [Joint Optimization of Resource Utilization, Latency and UAV...][research_xiao_jin_2023]
- [The development requirement and design considerations for...][research_shi_tan_2018]
- [Review Transfer of Technology and Local Content and Offsets...][research_taufikbudicahyana_achmadwardana_2023]
- [Effect of Aerodynamic Configuration Parameters on...][research_pan_huang_2019]
- [Failures in Ukrainian Arms Procurement 2014 2023][research_bukkvoll_2024]
- [Open and closed loop gust loads analyses for a flying wing...][research_voss_2019]
- [Key Aspects of India’s Arms Export Policy amid...][research_likhachev_2024]
- [Dynamic Stability Analysis of Aircraft Flight in Deep Stall][research_cunis_condomines_2020]
- [Small arms procurement and corruption in small NATO countries][research_pernica_palavenis_2024]
- [Lateral Stability and Control of a Flying Wing Configuration...][research_wang_tang_2020]
- [External shock and diversified landscape of China’s product...][research_gao_kong_2025]
- [Application Analysis on Fly-by-Wire Flight Control System on...][research_application_analysis_2022]
- [Jump further or climb higher? Impact of different export...][research_zhou_chen_2025]
- [Development and interaction of vortices over a very low...][research_dong_choi_2022]
- [Legitimising Proactivity Japan’s Use of the FOIP in Defence...][research_thankachan_2025]
- [Performance analysis of electrical flight control actuation...][research_ercan_akin_2022]
- [Policy Support for Exporting Complete Aircraft Focusing on...][research_moon_2025_b]
- [Conceptual design of a new experimental setup to simulate...][research_mahjouri_shabani_2023]
- [Transformation of the EU Policy in the Field of Export...][research_grytsyshen_abramova_2025]
- [Flight Control Law for Stabilizing Transient Response of the...][research_ji_kim_2023]
- [Aircraft export modes with MRO integration leasing vs. direct...][research_chen_jiang_2026]
- [Flight-Test Determination of Longitudinal Stability Using...][research_dias_2023]
- [Defence Diplomacy and the Deepening of Indonesia-Türkiye...][research_diphda_wiswayana_2026]
- [ADVANCEMENTS IN SUPERSONIC FLIGHT CONTROL REVIEW OF CAVITY...][research_balakrishnan_abdrahimabutalib_2024]
- [Testing times Swiss military weapons procurement 1870 1900][research_wren_2026]
- [Design optimization of anti-spin parachute for fighter-class...][research_zhang_cheng_2024]
- [Research on Wave-Added Resistance and Longitudinal Stability...][research_sun_ju_2024]
- [Research on torque measurement in flight test for all-moving...][research_min_xian_2024]
- [Energy Configuration Design and Configuration Scheme of...][research_qian_xinhui_2025]
- [Study on the influence of horizontal tail position and nose...][research_shao_xu_2025]
- [Evaluating Longitudinal Stability-and-Control Characteristics...][research_xie_cai_2026]

- [Competition watchdog considers Lloydspharmacy’s acquisition...][research_competition_watchdog_2015]
- [International Acquisition Programs Variables Beyond Cost...][research_chace_2015]
- [Celesio’s acquisition of wholesaler Sangers gets competition...][research_celesios_acquisition_2016]
- [Defence, Acquisition or Non-Competition? How Did the Form and...][research_linek_chytilek_2016]
- [Park Chung Hee Administration’s Fighter Experimental F-X...][research_um_2016]
- [Striking a deal on the F-35 multinational politics and US...][research_vonhlatky_rice_2018]
- [User = Buyer = Seller = Problematic Defence Acquisitions?...][research_verma_2018]
- [Fighter aircraft acquisition in Croatia failure of policy...][research_watkins_2019]
- [DEFENCE PROCUREMENT ACQUISITION SYSTEM OF UKRAINE THEORETICAL...][research_holota_2020]
- [Delivering Capability Through Competition in Defense...][research_duddy_landucci_2020]
- [Big Tech mergers Innovation, competition for the market, and...][research_katz_2021]
- [Comparing Government Social Welfare Service Acquisition...][research_pue_2021]
- [No-capability defence acquisition A literature review on...][research_na_2021]
- [Biotechnology and Biodefense Enterprise An Industry...][research_yeh_du_2022]
- [No-capability defence acquisition a literature review on...][research_verlaine_2023]
- [Organisational Restructuring for Defence Planning and...][research_cowshish_2023]
- [Preaching Peace, Selling Arms The Evolution of Canadian...][research_esau_2024]
- [Prohibition of Arms Export to a State with an Overriding Risk...][research_kim_2024]
- [Defence and Security Procurement Regulation after Brexit][research_butler_2025]
- [Delivering more competition to the EU defence markets?...][research_kananoja_kosonen_2025]
- [MILITARY PRESENCE AND ARMS EXPORT IN FRANCE’S MIDDLE EAST...][research_military_presence_2025]
- [Transparency in Defence Procurement Without Competition][research_kegels_skovgaardlykke_2025]
- [Developing multi-type sensor network acquisition devices in a...][research_justiciaalados_trezza_2026]
- [Japan's Narrow Defense Export Path Structural Constraints...][research_choi_2026]
- [Joint Defence Procurement in a Bottleneck Economy][research_oconnell_komsic_2026]

### Ram drag came back as a subject when supersonic cruise did

**The keystone's other half is the one the survey above never reached.** The engine section computed that 45
percent of gross thrust at Mach 2.6 is spent on the momentum of the air the engine swallowed, and that the
exhaust velocity the rating implies needs total pressure the inlet was struggling to deliver.
**That is a propulsion-integration problem and it went quiet for thirty years** because nothing was being
designed to cruise supersonically.

**It is live again.** Supersonic civil transport, variable-cycle engines and boundary-layer-ingesting
propulsion have all put thrust-and-drag bookkeeping back at the centre of the design problem, and the
question of where the airframe ends and the engine begins is being argued in the same terms the X-27 would
have had to settle.

- [A Study on the Installed Performance Seeking Control for...][research_sun_miao_2015]
- [A Numerical Study on a Supersonic Turbine Performance...][research_jeong_choi_2015]
- [Drag prediction method of powered-on civil aircraft based on...][research_zhang_chen_2015]
- [A full engine cycle analysis of a turbofan engine for optimum...][research_kim_kim_2015_b]
- [Civil turbofan propulsion aerodynamics Thrust-drag accounting...][research_goulos_otter_2021]
- [An exergy way to quantify sustainability metrics for a high...][research_turan_2015]
- [Numerical modeling on installed performance of turbofan...][research_chen_cai_2021]
- [Analysis of Combustion Efficiency for Turbofan Engine...][research_sohret_turan_2015]
- [Numerical investigation of the powered take-off configuration...][research_cui_zhang_2024]
- [Computational Modeling of a Typical Supersonic...][research_shariatzadeh_abrishamkar_2015]
- [Improving Base-Drag Corrections for Rotating Detonation...][research_feleo_gamba_2025]
- [Modeling of Start-Up From Engine-Off Conditions Using High...][research_bretschneider_reed_2015]
- [NUMERICAL ANALYSIS OF SINGLE-EXPANSION RAMP NOZZLE...][research_mazurov_2015]
- [NUMERICAL SIMULATION AND OPTIMIZATION OF HIGH PERFORMANCE...][research_anon_2015]
- [An analytical study on the performance of the organic Rankine...][research_saadon_talib_2016]
- [Broadband noise suppression for turbofan inlet applications][research_eversman_2016]
- [CFD study on particle separation performance by shock...][research_jassim_2016]
- [Conceptual study of supersonic transports employing...][research_takahashi_2017]
- [Cycle parametric study on the performance of aeroderivative...][research_effiom_abam_2017]
- [Numerical Investigation on the Performance of Different...][research_xue_li_2017]
- [Numerical determination of transmission losses of a turbofan...][research_chan_perreydebain_2017]
- [The optimal cruise altitude of LNG-fuelled turbofan aircraft][research_vos_wortmann_2017]
- [Thrust Performance Evaluation of a Turbofan Engine Based on...][research_yalcin_2017]
- [Turbofan Engine Performance under Reliability Measures...][research_turbofan_engine_2017]
- [Using a Bowed Blade to Improve the Supersonic Flow...][research_yao_zhou_2017]
- [Wedge Shock and Nozzle Exhaust Plume Interaction in a...][research_castner_zaman_2017]
- [Design of a double parabolic supersonic nozzle and...][research_ak_ps_2018]
- [IMPROVEMENT OF WIDE-CHORD ROTOR BLADE FAN PERFORMANCE IN...][research_berezovsky_2018]
- [Nonlinear Propagation of Supersonic Fan Tones in Turbofan...][research_adetifa_mcalpine_2018]
- [Numerical simulation of nozzle flow for design of the devices...][research_kimura_imai_2018]
- [Performance analysis of an Organic Rankine Cycle system with...][research_amnasir_saadon_2018]
- [Ramjet Nozzle Analysis for Transport Aircraft Configuration...][research_baidya_pesyridis_2018]
- [Research on Performance Seeking Control of Turbofan Engine at...][research_shufan_heng_2018]
- [Turbojet Engine Industrial Min Max Controller Performance...][research_jafari_nikolaidis_2018]
- [F-16 turbofan engine monitoring system][research_szrama_2019]
- [NUMERICAL INVESTIGATION OF ELLIPTICAL MIXED EXPANSION NOZZLE...][research_mazurov_2019]
- [Numerical studies of nozzle thrust characteristics of...][research_gorbovskoi_kazhan_2019]
- [Study of Bypass Ratio Increasing Possibility for Turbofan...][research_jakubowski_2019]
- [Turbofan engine performance optimization based on aircraft...][research_dafonsecafilho_gamaribeiro_2019]
- [Enhanced cruise range prediction for narrow-body turbofan...][research_atasoy_cetek_2020]
- [Performance of Universal Reciprocating Heat-Engine Cycle with...][research_chen_ge_2020]
- [THRUST VECTORING OF A SUPERSONIC RECTANGULAR NOZZLE BY USING...][research_thrust_vectoring_2020]
- [Underexpanded Supersonic Jets from Elliptical Nozzle with Aft...][research_nageswararao_kushari_2020]
- [WITHDRAWN Effect of reacting gas on the fluidic thrust...][research_chouicha_sellam_2020]
- [Estimation of aircraft turbofan engine exhaust emissions with...][research_akdeniz_2021]
- [Evaluation of Injection Strategies in Supersonic Nozzle Flow][research_semlitsch_mihaescu_2021]
- [Examination of parametric cycle analysis of a turbofan engine...][research_dislitas_albayrakceper_2021]
- [Relation between total pressure loss in supersonic nozzle and...][research_sakamoto_sasaki_2021]
- [The aerothermodynamic cycle optimal design of a turbofan...][research_chen_chen_2021]
- [Thermal Structure Strength Analysis of Nozzle of Solid Rocket...][research_wang_tian_2021]
- [Thrust Vectoring of a Fixed Axisymmetric Supersonic Nozzle...][research_resta_marsilio_2021]
- [Turbofan engine performances from aviation, thermodynamic and...][research_balli_caliskan_2021]
- [Cooling rocket nozzle extensions with supersonic gas injection][research_thompson_2022]
- [Değişken Çevrimli Mikro Turbofan Jet Motoru için Bütünleşik...][research_gurbuz_acarer_2022]
- [EFFICIENCY OF THE INTRODUCTION THE INTERMEDIATE HEATING IN...][research_ivanov_2022]
- [EXPERIMENTAL AND COMPUTATIONAL ANALYSIS OF n-DECANE SPRAY...][research_ju_deng_2022]
- [Exergo-Economic Analysis of a Cfm56-7c Turbofan Engine][research_turan_2022]
- [Exergo-economic analysis of a CFM56-7B turbofan engine][research_turan_2022_b]
- [Experimental investigation on carbon deposition...][research_qiu_chen_2022]
- [Modeling and Cycle Parameter Matching of a High-Speed...][research_yao_zhang_2022]
- [Numerical simulation of supersonic gas flow in a conical...][research_voroninst_2022]
- [Study on the Effect of Swallowing Birds on the Performance of...][research_study_on_2022]
- [The Peculiarities of Applying CAD/CAE Systems for the Primary...][research_pashchenko_kharchenko_2022]
- [A novel compound fault-tolerant method based on online...][research_zhou_huang_2023]
- [Aeropropulsive assessment of engine installation at cruise...][research_magrini_benini_2023]
- [Analysis of cruise conditions on energy, exergy and NOx...][research_aygun_turan_2023]
- [Design Process and Flow Field Analysis of a Double Divergent...][research_kbab_haif_2023]
- [Design and Computational Analysis of an Axisymmetric...][research_dai_boughazi_2023]
- [Flow structure and parameter evaluation of conical convergent...][research_flow_structure_2023]
- [Influence of shock wave/boundary layer interaction on...][research_liu_cao_2023]
- [Optimization of CD nozzle length for a particular supersonic...][research_zahir_aamer_2023]
- [Performance comparison of rectangular nozzle with circular...][research_menon_sanjayshivam_2023]
- [Supersonic Plug Nozzle Conception and Comparison to the MLN...][research_zebbiche_youbi_2023]
- [Supersonic nozzle performance prediction considering the...][research_zhang_wang_2023]
- [Thermodynamic and Exergo-economic Analyses of Waste Heat...][research_kamani_mirzaee_2023]
- [A COMMERCIAL TURBOFAN ENGINE MODELING AND EXERGY ANALYSIS][research_kalkan_2024]
- [Aerodynamic Instabilities in High-Speed Air Intakes and Their...][research_philippou_zachos_2024]
- [Design and Numerical Analysis of E-D Nozzle with Throat...][research_design_and_2024]
- [Effect of Bypass Duct on the Thrust Vectoring Performance of...][research_afridi_khan_2024]
- [Experimental and numerical studies on the performance of...][research_li_xu_2024_b]
- [Flow and Aeroacoustic Characteristics of Underexpanded...][research_volkov_2024]
- [Influence of the swirl vanes in convergent-divergent nozzle...][research_sekar_kengaiah_2024]
- [Mechanism of adjusting bypass ratio by front variable area...][research_li_xia_2024]
- [Mixed-Flow Turbofan Engine Model for the Conceptual Design of...][research_piccirillo_gregorio_2024]
- [Research on Optimization Technology of Minimum Specific Fuel...][research_guo_zhang_2024]
- [Turbofan engine health status prediction with artificial...][research_szrama_lodygowski_2024]
- [Two parallel expansions for improving supersonic axisymmetric...][research_yahiaoui_2024]
- [An investigation of a plug-nozzle for supersonic aircraft...][research_zaman_korth_2025]
- [Component Sizing and Design-Point Performance Evaluation of a...][research_ajain_2025]
- [Conceptual Design and Energy Management Analysis of...][research_beschorner_kriewall_2025]

### Thermal stress is now a coupled problem rather than a hand calculation

**The article computes a thermal stress with a modulus, an expansion coefficient and a temperature difference, and gets a number comparable to the mechanical allowable.**
That calculation is a century old and it is the right first move.
**What has changed is that the coupling is no longer neglected.**

Contemporary work treats the aerodynamic heating, the temperature field, the resulting stress and the change
in stiffness as one problem rather than four, under the name aerothermoelasticity, and the reason is that at
high Mach the structure's deformation changes the flow that is heating it.
**For the X-27 this would have mattered less than for a hypersonic vehicle, but the eighty-three kelvin figure computed above is exactly the kind of number that a coupled analysis exists to refine.**

- [Efficient C0 Finite Element Formulation for Thermal Stress...][research_zhen_kun_2015]
- [Effect of heat transfer on shock train oscillations in a...][research_chen_sethuraman_2025]
- [Heat transfer and thermal stress analysis in fluid-structure...][research_li_pan_2015]
- [Effect of opposing jet layouts on flow and aerodynamic...][research_guo_luo_2025]
- [Thermal buckling and free vibration analysis of size...][research_ebrahimi_salari_2015]
- [Experimental Observations on Film Cooling Effectiveness on...][research_sreekumar_vamsikrishna_2025]
- [Thermal buckling of composite plates with spatial varying...][research_duran_fasanella_2015]
- [Influence of Wall Temperature on Shock Train in a Unilateral...][research_wang_liu_2025]
- [Thermal buckling of temperature dependent FG-CNT reinforced...][research_mirzaei_kiani_2015]
- [Inverse heat transfer for real-time thermal evaluation of...][research_zhao_jin_2025]
- [Analytical solution for thermal buckling analysis of...][research_thang_2016]
- [Reliability analysis of hypersonic vehicles under aerodynamic...][research_yu_wang_2025]
- [CONTOUR INTEGRAL EVALUATION OF CENTRE CRACKED RECTANGULAR...][research_anon_2016]
- [Validation and enhancement of aerodynamic heating method with...][research_xie_ye_2025_b]
- [Flutter and Thermal Buckling Analysis for Composite Laminated...][research_shao_cao_2016]
- [A Modular Conjugate Heat Transfer Optimization Framework for...][research_christianpsenica_leanfang_2026]
- [Thermal buckling and post-buckling behaviour of continuous...][research_pucillo_2016]
- [Effects and coupling mechanisms of nitrogen and oxygen...][research_zheng_huang_2026]
- [Thermal buckling and post-buckling of FGM Timoshenko beams on...][research_sun_li_2016]
- [Forecasting the temperature of the coolant in an aerodynamic...][research_ai_2026]
- [Thermal buckling and vibration analysis of laminated...][research_katariya_panda_2016]
- [GCN-HF A graph convolutional network approach for efficient...][research_li_zhao_2026]
- [Thermal buckling behaviour of shear deformable functionally...][research_kar_panda_2016]
- [Influence of Super-catalytic Wall on the Aerodynamic Heating...][research_gao_zhang_2026]
- [Thermal buckling of laminated composite plates using...][research_cetkovic_2016]
- [Multifidelity Data Fusion Method for Aerodynamic Heating...][research_duan_zhao_2026]
- [Thermal stress analysis of PCM containers for temperature...][research_dalmagro_benasciutti_2016]
- [Numerical analysis of thermal response and failure threshold...][research_he_zhang_2026]
- [Analysis of thermal temperature fields and thermal stress...][research_lu_zhang_2017]
- [Numerical investigation of aerodynamic heating by electron...][research_gao_he_2026]
- [Exact solution of thermal buckling and post buckling of...][research_bayat_ekhteraeitoussi_2017]
- [Investigations on the influences of elastic foundations on...][research_chai_song_2017]
- [Nonlinear analysis of bending, thermal buckling and...][research_she_yuan_2017]
- [Thermal buckling of temperature-dependent FG-CNT-reinforced...][research_kiani_2017]
- [Transient thermal stress analysis of a functionally graded...][research_manthena_kedar_2017]
- [Analysis and homogenization of residual stress in aerospace...][research_wu_wu_2019]
- [Computational fluid dynamic and thermal stress analysis of...][research_kadir_beg_2019]
- [Elastoplastic thermal buckling of functionally graded...][research_zhang_chen_2019]
- [Thermal Buckling Analysis of Axially Layered Functionally...][research_evran_2019]
- [Thermal buckling and sound radiation behavior of truss core...][research_fu_chen_2019]
- [Buckling and post-buckling of pinned Euler beams on weakened...][research_wen_tang_2020]
- [Flutter and Thermal Buckling Properties and Active Control of...][research_xue_li_2020]
- [Influence of the boundary relaxation on the flutter and...][research_chai_li_2020]
- [Thermal buckling of curvilinearly stiffened laminated...][research_devarajan_kapania_2020]
- [Vibration and thermal buckling analysis of rotating nonlocal...][research_fang_zheng_2020]
- [A Study on Thermal Buckling and Mode Jumping of Metallic and...][research_gutierrezalvarez_bisagni_2021]
- [Acclimation History of Elevated Temperature Reduces the...][research_page_bergstrom_2021]
- [Dimensional analysis and inertial effects in transient...][research_ma_2021]
- [Experimental investigation of the thermoelastic performance...][research_ganilova_cartmell_2021]
- [Study on thermal buckling temperature of a lattice sandwich...][research_sebata_ushijima_2021]
- [Transient thermal stress analysis of temperature-dependent...][research_su_hwu_2021]
- [Analyzing thermal buckling in curvilinearly stiffened...][research_devarajan_kapania_2022]
- [Application of a dynamic thermoelastic coupled model for an...][research_ganilova_cartmell_2022]
- [Physics-Informed MTA-UNet Prediction of Thermal Stress and...][research_cao_yao_2022]
- [Simulation analysis of thermal stress/strain of single fiber...][research_lin_zhang_2022]
- [Study on the Leading Edge of a Hypersonic Vehicle Using the...][research_chen_xia_2022]
- [Study on thermal buckling temperature of a lattice sandwich...][research_sebata_ushijima_2022]
- [Dynamic and Thermal Buckling Behaviors of Multi-Span...][research_wang_gao_2023]
- [Fluid-Structure Coupled Analysis of the Transient Thermal...][research_yi_2023]
- [Temperature Field and Thermal Stress Analysis of Rocket...][research_liu_feng_2023]
- [Thermal Buckling of Functionally Graded Plates With Cutouts][research_scpradhan_2023]
- [Thermal buckling and post-buckling analyses of rotating...][research_eyvazian_zhang_2023]
- [Turbulent Flow Heat Transfer and Thermal Stress Improvement...][research_yeranee_rao_2023]
- [Nonlinear Aero-Thermo-Elastic Stability Analysis of a Curve...][research_kang_liang_2024]
- [Novel evidence theory-based reliability analysis of...][research_wang_song_2024]
- [On the hysteretic response of mechanical strain induced by...][research_cong_yu_2024]
- [Coupled influence of blowing ratio and temperature ratio on...][research_lv_wang_2025]
- [Influence of non-uniform surface temperature distribution on...][research_cm_2025]
- [Investigation of Thermal Stress Performance of Si₃N₄ Discs...][research_kayiran_2025]
- [Mechanisms of structural thermal stress influence on...][research_xie_ye_2025]
- [Temperature Field and Thermal Stress Analysis of a Composite...][research_hu_wang_2025]
- [Study on the Thermal Stress and Thermal Deformation of the...][research_kong_sun_2026]
- [Thermal Stress Analysis of Free-Free Trusses under...][research_chen_lee_2026]

### The Lancer is now a recognised design problem with a literature of its own

**A derivative aircraft is not a cheap aircraft, and the modern literature says so with numbers.** Reusing a
fuselage cross-section, an aerofoil and a systems architecture buys development cost and schedule at the
price of a constrained design space, and the size of that price is now a research subject.

**This is the one contemporary thread that takes the article's own subject as its object of study.** The
Lancer retained the F-104's aerofoil section and its 3.36 percent thickness ratio, which is why its aspect
ratio could only reach 2.836 and why its drag-due-to-lift stayed above the F-5E's at every assumption
tested.
**The modern framing would call that inherited constraint the dominant term in the trade, and would try to price it before committing rather than after losing a competition.**

- [Generalizable Multifidelity Aerodynamic Wing Shape Design...][research_yang_li_2026]
- [A CFD Study on Leading Edge Wing Surface Modification of a...][research_ramprasadh_devanandh_2015]
- [Generative Artificial Intelligence in Aircraft Design...][research_du_2026]
- [Aerodynamic Impact of Vortex Generators on a...][research_rybalko_loth_2015]
- [Tailplane sizing for LH2 aircraft families commonality...][research_garmillamanzano_fritzsche_2026]
- [Aircraft Wake-Vortex Encounter Analysis for Upper Levels][research_schumann_sharman_2015]
- [Effect of aspect ratio on the near-wake flow structure of an...][research_corallo_sheridan_2015]
- [Effect of aspect ratio on wing rock at low Reynolds number][research_go_maqsood_2015]
- [Leading edge vortex development on a pitch-up airfoil][research_hord_lian_2015]
- [Leading-Edge Geometry Effects on the Vortex Formation of a...][research_hovelmann_breitsamter_2015]
- [Mechanism of Generation and Collapse of a Longitudinal Vortex...][research_ogawa_takeda_2015]
- [Strong geographical variation in wing aspect ratio of a...][research_hassall_2015]
- [The Adaptive Aspect Ratio morphing wing Design concept and...][research_woods_friswell_2015]
- [The effect of aspect ratio on the leading-edge vortex over an...][research_phillips_knowles_2015]
- [AVT-183 diamond wing flow field characteristics Part 2...][research_hovelmann_grawunder_2016]
- [Camber Effects on Minimum Power and Thrust Relations for...][research_traub_2016]
- [Characterizing a burst leading-edge vortex on a rotating flat...][research_jones_medina_2016]
- [Computational modeling of interference between helicopter...][research_ignatkin_makeev_2016]
- [Evolution of supersonic corner vortex in a hypersonic...][research_huang_tan_2016]
- [Experimental and numerical studies of low aspect ratio wing...][research_chen_bai_2016]
- [Numerical study of micro-ramp vortex generator for supersonic...][research_yan_chen_2016]
- [Thermal structural analysis of the platelet heat-pipe-cooled...][research_hongpeng_weiqiang_2016]
- [Behaviour of trailing wing s in echelon formation due to wing...][research_m_mukherjee_2017]
- [Effect of nose thickness distribution on the stall...][research_zhang_shan_2017]
- [Numerical Optimization of Plate-Line Design for Enhanced...][research_stephan_schrall_2017]
- [The leading-edge vortex of swift wing-shaped delta wings][research_muir_arredondogaleana_2017]
- [Analytical solution of the wave drag minimization problem for...][research_takovitsky_2018]
- [Effect of fuselage diameter on aerodynamic characteristics...][research_lai_kamaruddin_2018]
- [Effects of Leading Edge Enlargement on the Primary Vortex of...][research_said_mat_2018]
- [Enhanced Maneuverability of a Delta-Canard Combat Aircraft by...][research_hitzel_osterhuber_2018]
- [Ground Effect on the Vortex Flow and Aerodynamics of a...][research_lee_ko_2018]
- [IMPROVING THE AERODYNAMICS OF A TRANSPORT AIRCRAFT WING USING...][research_gueraiche_popov_2018]
- [Leading-edge vortex development on a pitching flat plate with...][research_leknys_arjomandi_2018]
- [Mid-wake wing tip vortex dynamics with active flow control][research_dghim_ferchichi_2018]
- [Numerical and theoretical investigations on the leading-edge...][research_chen_liu_2018]
- [On a Recently Proposed Vorticity-Based Definition of Wave Drag][research_ostieri_tognaccini_2018]
- [On the leading edge noise and aerodynamics of thin aerofoil...][research_juknevicius_chong_2018]
- [On the lift-optimal aspect ratio of a revolving wing at low...][research_jardin_colonius_2018]
- [On the mechanism of wave drag reduction by concentrated laser...][research_joarder_2018]
- [Optimization of Variable-Camber Continuous Trailing-Edge Flap...][research_ting_chaparro_2018]
- [Oscillations of Leading-Edge Vortex Breakdown Locations over...][research_shen_wen_2018]
- [Pitching effect on transonic wing stall of a blended flying...][research_tao_zhao_2018]
- [Relationship between Configuration of Longitudinal Vortex...][research_yano_okada_2018]
- [The leading-edge vortex on a rotating wing changes markedly...][research_bhat_zhao_2018]
- [Volumetric measurement and vorticity dynamics of leading-edge...][research_chen_wu_2018]
- [A physical model for solving the dredging thermal protection...][research_sun_zhu_2019]
- [Active Control of Wing-tip Vortex Development Using...][research_himeda_naka_2019]
- [Drag Reduction on the Basis of the Area Rule of the...][research_yamazaki_mizobata_2019]
- [Effect of duct aspect ratio on normal shock wave/boundary...][research_vaisakh_namratha_2019]
- [Influence of aspect ratio on wing wake interaction for...][research_addoakoto_han_2019]
- [Influence of leading edge shapes on vortex behaviour of delta...][research_ramakrishna_senthilkumar_2019]
- [Leading-Edge Vortex Interactions at a Generic Multiple...][research_pfnur_breitsamter_2019]
- [Vortex flow on the wing of aircraft and flow control to...][research_mamonova_soudakov_2019]
- [Aerodynamics Analysis on the Effect of Canard Aspect Ratio on...][research_ali_kuntjoro_2020]
- [Analysis for spiral vortex and effect of profile of nozzle...][research_wang_2020]
- [Effects of leading-edge separation on the vortex shedding and...][research_duan_laima_2020]
- [Evolution of the leading-edge vortex over a flapping wing...][research_arifin_yusoff_2020]
- [Free-stream turbulence interaction with a wing-tip vortex][research_benmiloud_dghim_2020]
- [Interplay of the leading-edge vortex and the tip vortex of a...][research_dong_choi_2020]
- [Leading-edge vortex formation and transient lift generation...][research_chen_wu_2020]
- [Low Reynolds Number Flow over Low Aspect Ratio Corrugated Wing][research_chandra_2020]
- [Numerical investigation on a double layer combined cooling...][research_ding_wang_2020]
- [Numerical simulation of support interference characteristics...][research_zhang_li_2020]
- [PIV Flow Visualization around Low Aspect Ratio Wing at Low...][research_kase_mizoguchi_2020]
- [Potential of Micro-Vortex Generators in Enhancing the Quality...][research_cheidris_saad_2020]
- [Pulsed Blowing Interacting with a Leading-Edge Vortex][research_buzica_breitsamter_2020]
- [Scaling trends of bird’s alular feathers in connection to...][research_linehan_mohseni_2020]
- [The effect of wake from forward wing on performance of wing...][research_ueki_yasuda_2020]
- [Vertically Optimal Close Formation Flight Control Based on...][research_zhai_li_2020]
- [Adapted Linear Forcing for Inlet Turbulent Fluctuations...][research_perrin_2021]
- [Effects of leading-edge separation on the vortex-induced...][research_duan_laima_2021]
- [High Speed Microactuators for Low Aspect Ratio High Speed...][research_barrettgonzalez_wolf_2021]
- [Locating the Isolator Shock-Train Leading Edge with Limited...][research_hunt_hunt_2021]
- [Numerical Simulation of the Streamwise Transport of a Delta...][research_francois_probst_2021]
- [Numerical study on the influence of wall temperature gradient...][research_lin_liu_2021]
- [On the accuracy of wave drag acting on a supersonic moving...][research_goto_nakayama_2021]
- [Size effects of vane-type rectangular vortex generators...][research_ichikawa_koike_2021]
- [Smooth Particle Hydrodynamics Birdstrike Analysis on Aircraft...][research_smooth_particle_2021]
- [A species-transport model for circulation in a leading-edge...][research_ginermorency_wong_2022]
- [Aircraft Cruise Drag Reduction Through Variable Camber Using...][research_reist_koo_2022]
- [Conceptual design and comparative study of strut-braced wing...][research_ma_karpuk_2022]
- [Experimental Investigation of Flow Control on a High-Lift...][research_abdolahipour_mani_2022]
- [IMPLEMENTATION OF TRANSONIC AREA RULE AND SWEPT BACK DELTA...][research_singh_dwivedi_2022]
- [Numerical study on the effect of tangential intake on vortex...][research_chang_wei_2022]
- [On Trapeze Wing Aerodynamics Calculations Based on Improved...][research_nagler_2022]
- [Pressure Improvement on a Supercritical High-Lift Wing Using...][research_abdolahipour_mani_2022_b]
- [Research on dynamic aerodynamic characteristics of flying...][research_zeng_zhao_2022]
- [Supersonic Forward-Swept Wing Design Using Multifidelity...][research_kishi_kanazaki_2022]
- [The leading-edge vortex over a swift-like high-aspect-ratio...][research_bengida_gurka_2022]
- [Time-domain Analytical Method for Aeroelastic Analysis of...][research_rehman_2022]

### The X-27's real problem has a modern answer, and it is the one thing that would have helped

**Nobody could tell whether the Lancer would work without building it.** That is the whole of the
programme's difficulty. The mock-up settled nothing, the brochure figures were the manufacturer's own, and
the competition was decided on cost and logistics rather than on any measurement of the aeroplane.

**Evaluating an aircraft that does not exist is now a research programme.** Surrogate modelling, uncertainty
quantification in conceptual design, model-based systems engineering and the digital twin all exist to
answer, before metal is cut, the question the X-27 could only have answered by flying.

**This is the closest thing to a resolution the article's central difficulty has, and it arrived fifty years late.**
It is also the reason this article could be written at all. The analysis above is a primitive version of the
same idea, taking published geometry and published ratings and asking what they imply, and its one genuine
success, the reconciliation of the spike travel with the engine's airflow, is exactly the kind of
consistency check a modern framework automates.

- [Characterization of Aeroelastic Behavior in a High Aspect...][research_westin_balthazar_2023]
- [Robustness Analysis of an Aircraft Design for Short Takeoff...][research_krosche_heinze_2015]
- [CRITERION TO SELECT OPTIMUM VALUES OF AIRCRAFT LATERAL STATIC...][research_desyatnik_2015]
- [The impacts of rising temperatures on aircraft takeoff...][research_coffel_thompson_2017]
- [Design of a new sweptback wing for a future supersonic...][research_xu_2023]
- [A mathematical model of transforming the vertical takeoff and...][research_pavlov_2016]
- [Static stability of manipulator configuration Influence of...][research_klimchik_chablat_2015]
- [Decreased takeoff performance of aircraft due to climate...][research_zhou_zhang_2018]
- [Effect of Air Jet Vortex Generators on the Shock Wave...][research_dai_zhang_2023]
- [Active flow control for high lift with steady blowing][research_radespiel_burnazzi_2016]
- [Estimation of Lateral/Directional Static Stability...][research_wandini_mulyanto_2016]
- [Impact of 1.5 °C and 2.0 °C global warming on aircraft...][research_zhou_ren_2018]
- [Leading-Edge Vortex Controller LEVCON Influence on the...][research_malicki_malecha_2023]
- [Bayesian Sensitivity Analysis of Flight Parameters in a...][research_sartor_becker_2016]
- [Helicopter stabilizer optimization considering rotor downwash...][research_minervino_vitagliano_2016]
- [Aerodynamic Flow Effects on Aircraft Carrier Takeoff...][research_barderamora_garciamagarino_2019]
- [Multidisciplinary structural optimization of novel...][research_kilimtzidis_kostopoulos_2023]
- [Development of multiobjective trajectory-optimization method...][research_othman_kanazaki_2016]
- [Aerodynamics analysis of the main rotor influence on the...][research_figat_2017]
- [Aircraft Takeoff Performance in a Changing Climate for...][research_zhao_sushama_2020]
- [Numerical investigation on the characteristics of...][research_wang_pan_2023]
- [Design optimization of aircraft landing gear assembly under...][research_wong_ryan_2017]
- [Wing-Body and Vertical Tail Interference Effects on Downwash...][research_paziresh_nikseresht_2017]
- [Estimating the Impact of Global Warming on Aircraft Takeoff...][research_yuan_dai_2021]
- [Numerical study of flow characteristics of tornado-like...][research_zhang_liu_2023]
- [Drag reduction capability of uniform blowing in supersonic...][research_kametani_kotake_2017]
- [Longitudinal Static Stability and wake visualization of high...][research_irsyadlukman_agoesmoelyadi_2018]
- [Flight-Test Validation of a Takeoff Performance Uncertainty...][research_sobester_2021]
- [Research on low-speed aerodynamic characterictics of flying...][research_zhao_zeng_2023]
- [High-performance aircraft short-takeoff and vertical-landing...][research_wall_mckinley_2017]
- [The Influence of Forest Canopies on the Decay of Aircraft...][research_teske_thistle_2018]
- [Decreased Aircraft Takeoff Performance under Global Warming][research_wang_peng_2023]
- [Transient leading-edge vortex development on a wing rolling...][research_wabick_johnson_2023]
- [Numerical Investigation of Powered High-Lift Model with...][research_jie_zhibin_2017]
- [Vortex Approach for Downwash and Outwash of Tandem Rotors in...][research_tan_sun_2018]
- [Effect of Spray Rails on Takeoff Performance of Amphibian...][research_bahulekar_mello_2024]
- [Aero-spike and aero-disk effects of on wave drag reduction of...][research_balusamy_a_2024]
- [High lift control system design for a transport aircraft][research_du_gao_2018]
- [INFLUENCE OF THE AT "WINGLETS" TYPE ON THE LONGITUDINAL...][research_malikov_miltsov_2019]
- [Aerodynamic Performance Enhancement of Low Aspect Ratio...][research_anon_2024]
- [Improved design of an active landing gear for a passenger...][research_zarchi_attaran_2018]
- [Effects of downwash during unmanned aircraft system‐assisted...][research_miura_kohzu_2020]
- [Bifurcation analysis of wing rock and routes to chaos of a...][research_jiang_li_2024]
- [Nacelle Strake Design for Short Takeoff and Landing...][research_keller_hasan_2018]
- [Low speed longitudinal aerodynamic, static stability and...][research_bykerk_verstraete_2020]
- [Design Optimization of Lambda-Wing Planform and Vortex...][research_lee_kim_2024]
- [Visual estimation of deviations for the civil aircraft landing][research_gibert_plestan_2018]
- [Aerodynamic and static stability investigation into aircraft...][research_figat_kwiek_2021]
- [Drag Reduction on the Basis of the Area Rule of the...][research_mizobata_mio_2024]
- [Conceptual Design, Material, and Structural Optimization of a...][research_paul_suresh_2019]
- [Investigation on improving longitudinal static stability of a...][research_qi_zong_2021]
- [Exploration of bio-inspired wingtip devices for low aspect...][research_verma_kulkarni_2024]
- [EXPERIMENTAL INVESTIGATIONS OF EXTERNALLY BLOWN FLAP...][research_petrov_pigusov_2019]
- [Aerodynamic Performance and Static Stability Characteristics...][research_vanarnhem_devries_2022]
- [Exploring Aerodynamics The Impact of Aspect Ratio on Paper...][research_sun_2024]
- [Flight Mechanical Challenges of STOL Aircraft Using Active...][research_diekmann_2019]
- [Effect of T-tail on the Aerodynamic Characteristics and...][research_ansari_m_2022]
- [Lattice Structures for Supersonic Passenger Aircraft Wing...][research_lomakin_fedorenko_2024]
- [Hydrogen Fuel Cells and Batteries for Electric-Vertical...][research_ng_datta_2019]
- [Effect of Twin Vertical Stabilizers on Lateral Directional...][research_goud_dwivedi_2022]
- [Multifidelity Comparison of Supersonic Wave Drag Prediction...][research_abraham_lazzara_2024]
- [Model-Based Systems Engineering for Aircraft Design With...][research_li_soskin_2019]
- [Downwash modelling for three-lifting-surface aircraft...][research_corcione_bonavolonta_2023]
- [On the conditions for absolute minimum fuel burn for turbofan...][research_poll_schumann_2024]
- [Overview and Summary of the Third AIAA High Lift Prediction...][research_rumsey_slotnick_2019]
- [Effect of Horizontal Position and Width of Box Tail Wing on...][research_lee_nam_2023]
- [Research on the cooling performance of the discontinuous...][research_wang_pan_2024]
- [Simulation of Observer Based Tracking Control for the...][research_makarov_2019]
- [Effects of Static Stability Margin on Aerodynamic Design...][research_li_qiao_2023]
- [Study of the Vortex-Resolving Method of the Throttling Effect...][research_lyubimov_2024]
- [Stability Analysis of Tailsitters in Vertical Takeoff and...][research_wang_yuan_2019]
- [High Crosswind-Tolerance Airplane by Adjusting Dihedral Angle...][research_watanabe_sunada_2023]
- [Wave drag and wave patterns by ships moving in a single-file...][research_zhu_yuan_2024]
- [Vertical Takeoff and Landing Aircraft, Vertical Takeoff and...][research_greene_2020]
- [Research on Longitudinal Static Stability Compensation of...][research_ding_2023]
- [A quantitative analysis of leading edge vortices in flapping...][research_gonzalo_garciavillalba_2025]
- [Environmental and enviroeconomic analyses of two different...][research_aygun_caliskan_2021]
- [Downwash Investigation of Horizontal Tail Plane Configuration...][research_herdiana_pinindriya_2024]
- [Computational Analysis of Tandem Micro-Vortex Generators for...][research_chen_yang_2025]
- [Experimental study on wing adaptive high-lift devices of...][research_pigusov_2021]
- [Influence of Single Engine Failure on Control and Stability...][research_zhou_liu_2025]
- [Evolution and stability analysis of supersonic Coanda jets of...][research_he_zhang_2025]
- [Hybrid RANS/LES of a generic high-lift aircraft configuration...][research_probst_melberwilkending_2021]
- [Numerical simulation and validation of downwash airflow...][research_guo_huang_2025]
- [Flow mechanism and performance modeling for variable camber...][research_zhang_ji_2025]
- [Takeoff and Landing of a Wing-Tip-Connected Meta Aircraft...][research_cobar_montalvo_2021]
- [Effects of distributed propulsion on commuter aircraft...][research_ciliberti_nicolosi_2026]
- [Impact of Aspect Ratio on Structural Integrity and...][research_uzun_2025]
- [Theoretical model proposal on direct calculation of wetted...][research_durmus_2021]
- [Effects of forebody shape on directional static stability of...][research_lin_zong_2026]
- [Impact of aspect ratio on unstart flow characteristics in...][research_lian_xiong_2025]
- [Analysis of Factors Affecting Landing Performance of Civil...][research_analysis_of_2022]
- [Influence of Euler acceleration on the aerodynamic loading...][research_gururaj_morris_2025]
- [Computing Aerodynamic Characteristics of Passenger Aircraft...][research_vlasov_2022]
- [Leading-edge vortex enhancement of a flexible flapping wing...][research_wu_wang_2025]
- [Correlated Bayesian Model of Aircraft Encounters in the...][research_weinert_underhill_2022]
- [Normal Shock/Boundary-Layer Interaction Control Using...][research_verma_manisankar_2025]
- [Custer Channel Wings for Short Takeoff and Landing of...][research_mihalik_keane_2022]
- [Numerical analysis on the active cooling characteristics for...][research_yu_guo_2025]
- [Generic Design Methodology for Vertical Takeoff and Landing...][research_lee_lim_2022]
- [Numerical investigation of low-frequency shock train...][research_wang_he_2025]
- [Study of the static and endurance strength of reinforced...][research_sklyarov_vartazarova_2022]
- [On Wing Tip Flow Around a Low Aspect Ratio Wing at Low Flight...][research_lampropoulos_sarris_2025]
- [A Novel Safe Life Extension Method for Aircraft Main Landing...][research_fu_fu_2023]
- [On the investigation of near-wake flow structures and the...][research_pinapatruni_sinha_2025]
- [Liquid Cooling Systems for Batteries of Electric Vertical...][research_zhao_clarke_2024]
- [Steering the laminar leading-edge vortex through jet-induced...][research_anonymous_2025]
- [Novel Electric Propulsion System Analysis Method for Electric...][research_lee_yee_2024]
- [Strategy and mechanism of roll attitude regulation for a...][research_wang_feng_2025]
- [Optimal Performance Trim Procedure for Multirotor Vertical...][research_poggi_bernardini_2024]

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
[Swanborough and Bowers][book_swanborough] on United States military aircraft, [Buttler][book_buttler] on
American secret projects, [Johnson][book_johnson] for the Skunk Works memoir, and [Jenkins][book_jenkins]
for the surrounding experimental-aircraft context, and
**those sources disagree with one another on the matter of who wanted the X-designation**, which the article
reports rather than resolves.

**The physics comes from primary literature about everything except the vehicle.** Supersonic inlet design,
conical flow, compressor stall, elevated-temperature alloy behaviour and fighter performance analysis are
all richly documented in period reports and journals, and the article is built on those.
**That is the methodological move this subject requires: harvest the physics rather than the vehicle.**

**The engine and airframe numbers are the load-bearing figures and they come from reference sources rather than from documents.**
The 260 pounds per second, the four inches of spike travel, the 896 gallons and the weight breakdown are
each stated in secondary literature without a cited primary source.
**The inlet agreement computed above is a check on their mutual consistency and is offered as partial corroboration of figures that are otherwise uncorroborated.**

**Period coverage, and both figures are given because either alone misleads.** Of the research references
cited, **912 date from 1982 or earlier and 1,535 from 2015 or later**, and 1,188 are primary in the sense of
an original report or a paper contemporary with the work.

| | Count | Fraction of cited research |
|---|---|---|
| Primary | 1,188 | 44.0 percent |
| Period, through 1982 | 912 | 33.8 percent |
| Contemporary, 2015 onward | 1,535 | 56.8 percent |

**Read those fractions without the counts and this article looks as though it lost most of its period base. It lost none of it.**
The period count is 912 and was 912 before the contemporary survey was written.
**The primary count rose, from 1,176 to 1,188.** Both fractions fell only because the denominator grew by
more than a thousand contemporary references, which is the survey directive working rather than a
regression.

**The same trap runs in the other direction and this article has now been caught by both ends of it.** At
the reference pass the contemporary count sat unchanged while its fraction fell, because the period base was
growing. At this pass the period count sits unchanged while its fraction falls, because the contemporary
base is growing. **Neither movement is a fact about coverage. Both are facts about the denominator**, which
is why every figure in this article is given as a count and a fraction together.

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
degrees Celsius, where aluminium alloy retains about 69 percent of its yield strength, and the skin reaches
nine-tenths of that in one minute, so a dash does not evade it.

**Against that, the aeroplane was a better fighter than the one that beat it.** On sustained turn rate and
on specific excess power the Lancer clears the F-5E comfortably at every assumption tested, and sits within
3.5 percent of the F-15A's specific excess power.
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

- [Administration, National Aeronautics and Space, Jenkins, Dennis R...][book_jenkins]
- [Ascher H. Shapiro 1953, The dynamics and thermodynamics of compressible...][book_shapiro]
- [Brian L. Stevens 2015, Aircraft Control and Simulation][book_stevens_lewis]
- [Daniel P. Raymer 1989, Aircraft Design][book_raymer]
- [Dietrich Küchemann 2012, The aerodynamic design of aircraft][book_kuchemann]
- [E. L. Goldsmith 1993, Practical intake aerodynamic design][book_seddon_goldsmith]
- [Gordon C. Oates 1984, Aerothermodynamics of gas turbine and rocket...][book_oates]
- [Gordon Swanborough 1963, United States military aircraft since 1909][book_swanborough]
- [Jack D. Mattingly 1987, Aircraft engine design][book_mattingly_engine]
- [John Anderson 1982, Modern compressible flow][book_anderson]
- [Johnson, Clarence L. 1989, Kelly][book_johnson]
- [Leland M. Nicolai 2010, Fundamentals of aircraft and airship design][book_nicolai]
- [Ray Whitford 1987, Design for air combat][book_whitford]
- [Robert Coram 2002, Boyd][book_coram]
- [S F. Hoerner 1965, Fluid dynamic drag][book_hoerner]
- [Tony Buttler 2004, American Secret Projects][book_buttler]

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
[book_swanborough]: https://openlibrary.org/works/OL4484859W
[book_whitford]: https://openlibrary.org/works/OL5054670W

### Reference

- [Aerodynamic heating and recovery temperature][ref_recovery_factor]
- [AIM-7 Sparrow][ref_aim7]
- [AIM-9 Sidewinder][ref_aim9]
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
- [M61 Vulcan][ref_m61]
- [Mach number][ref_mach]
- [McDonnell Douglas F-15 Eagle][ref_f15]
- [McDonnell Douglas F-4 Phantom II][ref_f4]
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
[ref_helmbold]: https://en.wikipedia.org/wiki/Lift_coefficient
[ref_ifa]: https://en.wikipedia.org/wiki/Military_Assistance_Program
[ref_inconel]: https://en.wikipedia.org/wiki/Inconel
[ref_isa]: https://en.wikipedia.org/wiki/International_Standard_Atmosphere
[ref_j79]: https://en.wikipedia.org/wiki/General_Electric_J79
[ref_kelly_johnson]: https://en.wikipedia.org/wiki/Kelly_Johnson_(engineer)
[ref_lwf]: https://en.wikipedia.org/wiki/Lightweight_Fighter_program
[ref_m61]: https://en.wikipedia.org/wiki/M61_Vulcan
[ref_mach]: https://en.wikipedia.org/wiki/Mach_number
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

- [1554. Thermal regime and 1974][research_1554_thermal_1974]
- [16 percent. Aluminium-iron alloy 1954][research_16_percent_1954]
- [2015][research_anon_2015]
- [2016][research_anon_2016]
- [2024][research_anon_2024]
- [A Conference on Thermal 1954][research_a_conference_1954]
- [A Jain 2025][research_ajain_2025]
- [A M Nasir et al 2018][research_amnasir_saadon_2018]
- [A.I. 2026][research_ai_2026]
- [A.K. and P.S. 2018][research_ak_ps_2018]
- [Abazyan and Melikyan 2021][research_abazyan_melikyan_2021]
- [Abbasi et al 2018][research_abbasi_pirnia_2018]
- [Abdelghany 2025][research_abdelghany_2025]
- [Abdelwahab, M. 1977][research_abdelwahabm_1977]
- [Abdelwahab, M. 1981][research_abdelwahabm_1981]
- [Abdolahipour et al 2022][research_abdolahipour_mani_2022]
- [Abdolahipour et al 2022][research_abdolahipour_mani_2022_b]
- [Abdul Rasoul et al 2020][research_abdulrasoul_radhi_2020]
- [Abdul-Kaiyoom et al 2025][research_abdulkaiyoom_yildirim_2025]
- [Abedi et al 2020][research_abedi_askari_2020]
- [Abedi̇ et al 2021][research_abedi_salehi_2021]
- [Abraham et al 2024][research_abraham_lazzara_2024]
- [Abu Salem et al 2023][research_abusalem_palaia_2023]
- [Abu Salem et al 2023][research_abusalem_palaia_2023_b]
- [Acharya and Karbhari 2026][research_acharya_karbhari_2026]
- [Adams, J. C., Jr. et al 1984][research_adamsjcjr_martindalewr_1984]
- [Addo-Akoto et al 2019][research_addoakoto_han_2019]
- [Adetifa et al 2018][research_adetifa_mcalpine_2018]
- [Aerodynamic and Landing Measurements 1960][research_aerodynamic_and_1960]
- [Afanas’ev et al 2019][research_afanasev_nikitin_2019]
- [Afonso et al 2017][research_afonso_vale_2017]
- [Afridi et al 2024][research_afridi_khan_2024]
- [Agag et al 2026][research_agag_ali_2026]
- [Agarwal and Mthembu 2020][research_agarwal_mthembu_2020]
- [Agarwal and Rakich 1982][research_agarwal_rakich_1982]
- [Aggarwal et al 2010][research_aggarwal_valerdi_2010]
- [Agung Saputra et al 2026][research_agungsaputra_bhimashaktiarafat_2026]
- [Ahmad et al 2021][research_ahmad_zheng_2021]
- [Ahuja and Mavris 2022][research_ahuja_mavris_2022]
- [Air Force Research Lab Edwards Afb Ca 2000][research_airforceresearchlabedwardsafbca_2000]
- [Air Force Test Pilot School Edwards Afb Ca 1988][research_airforcetestpilotschooledwardsafbca_1988]
- [Air Force Test Pilot School Edwards Afb Ca 1989][research_airforcetestpilotschooledwardsafbca_1989]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Ajay and Kundu 2025][research_ajay_kundu_2025]
- [Akdeniz 2021][research_akdeniz_2021]
- [Akhlaghi and Azizi 2023][research_akhlaghi_azizi_2023]
- [Akhlaghi et al 2022][research_akhlaghi_azizi_2022]
- [Al-Saffar et al 1980][research_alsaffar_ashworth_1980]
- [Al-Shamma et al 2017][research_alshamma_ali_2017]
- [Alag, G. S. and Kaufman, H. 1974][research_alaggs_kaufmanh_1974]
- [Alberts 1995][research_alberts_1995]
- [Albuquerque et al 2018][research_albuquerque_gamboa_2018]
- [Aleisa et al 2023][research_aleisa_kontis_2023]
- [Alendar et al 2022][research_alendar_grunin_2022]
- [Alexander 1970][research_alexander_1970]
- [Alford 2004][research_alford_2004]
- [Ali et al 2017][research_ali_asghar_2017]
- [Ali et al 2020][research_ali_kuntjoro_2020]
- [Ali et al 2025][research_ali_khan_2025]
- [Alipour and Nejad 2016][research_alipour_nejad_2016]
- [Allen and Mahorter 1964][research_allen_mahorter_1964]
- [Allison et al 2015][research_allison_morris_2015]
- [Alone et al 2016][research_alone_kumar_2016]
- [Alsmadi and Murty 2020][research_alsmadi_murty_2020]
- [Alsmadi and Murty 2021][research_alsmadi_murty_2021]
- [Amann et al 1975][research_amann_nordenson_1975]
- [Amatucci et al 1982][research_amatucci_addy_1982]
- [An investigation into possible 1979][research_an_investigation_1979]
- [Analysis of Anti-surge Control 2021][research_analysis_of_2021]
- [Analysis of Factors Affecting 2022][research_analysis_of_2022]
- [Analysis of Flow Field 2024][research_analysis_of_2024]
- [Anantachaisilp and Lin 2020][research_anantachaisilp_lin_2020]
- [Anatomy of a turbofan 1970][research_anatomy_of_1970]
- [Anderson 1961][research_anderson_1961]
- [Anderson 2017][research_anderson_2017]
- [Anderson et al 1969][research_anderson_murthy_1969]
- [Anderson et al 1973][research_anderson_berger_1973]
- [Anderson, Adrien E 1947][research_andersonadriene_1947]
- [Anderson, B. H. 1974][research_andersonbh_1974]
- [Anderson, B. H. and Bowditch, D. N. 1958][research_andersonbh_bowditchdn_1958]
- [Anderson, B. H. et al 1960][research_andersonbh_bowditchdn_1960]
- [Anderson, Bernhard H. and Levy, Ralph 1991][research_andersonbernhardh_levyralph_1991]
- [Anderson, Bernhard H. and Weir, Lois 2014][research_andersonbernhardh_weirlois_2014]
- [Anderson, Seth B and Bray, Richard S 1951][research_andersonsethb_brayrichards_1951]
- [Anderson, Seth B and Bray, Richard S 1955][research_andersonsethb_brayrichards_1955]
- [Andrews 1969][research_andrews_1969]
- [Anglin 1978][research_anglin_1978]
- [Anglin and Satran 1980][research_anglin_satran_1980]
- [Anonymous 2025][research_anonymous_2025]
- [Ansari et al 2022][research_ansari_m_2022]
- [Antaran, Albert et al 1992][research_antaranalbert_beletehailu_1992]
- [Anti-Surge Control of Centrifugal 2021][research_anti_surge_control_2021]
- [Anti-surge Reason and Control 2021][research_anti_surge_reason_2021]
- [Aoyagi, K. and Hickey, D. H. 1963][research_aoyagik_hickeydh_1963]
- [Aoyagi, Kiyoshi and Hickey, David H. 1959][research_aoyagikiyoshi_hickeydavidh_1959]
- [Application Analysis on Fly-by-Wire 2022][research_application_analysis_2022]
- [Application of Centrifugal Compressor 2021][research_application_of_2021]
- [Application of PLC in 2021][research_application_of_2021_b]
- [Application Practice of Anti-surge 2021][research_application_practice_2021]
- [Araújo et al 2021][research_araujo_pereira_2021]
- [Archbold 1945][research_archbold_1945]
- [Arias et al 2023][research_arias_martinez_2023]
- [Aribi and Boushaki 2023][research_aribi_boushaki_2023]
- [Arif et al 2021][research_arif_iftikhar_2021]
- [Arifin et al 2020][research_arifin_yusoff_2020]
- [Arkoosh and Fiore 1972][research_arkoosh_fiore_1972]
- [Armstrong et al 1980][research_armstrong_palladino_1980]
- [Army Materiel Command Alexandria Va 1987][research_armymaterielcommandalexandriava_1987]
- [Arnson et al 2026][research_arnson_aljaber_2026]
- [Ashwood 1973][research_ashwood_1973]
- [Askari and Abedi 2026][research_askari_abedi_2026]
- [Askari and Soltani 2019][research_askari_soltani_2019]
- [Askari and Soltani 2020][research_askari_soltani_2020]
- [Askari and Soltani 2022][research_askari_soltani_2022]
- [Askari and Soltani 2023][research_askari_soltani_2023]
- [Askari et al 2019][research_askari_soltani_2019_b]
- [Assessment of Speed and 2023][research_assessment_of_2023]
- [Atasoy and Cetek 2020][research_atasoy_cetek_2020]
- [Atassi et al 2019][research_atassi_kozlov_2019]
- [Awerbuch 1980][research_awerbuch_1980]
- [Axelson, John A. and Crown, J. Conrad 1948][research_axelsonjohna_crownjconrad_1948]
- [AXIAL TRANSONIC COMPRESSOR STALL 2022][research_axial_transonic_2022]
- [Ayers 1962][research_ayers_1962]
- [Aygun and Caliskan 2021][research_aygun_caliskan_2021]
- [Aygun and Turan 2023][research_aygun_turan_2023]
- [Azam 2020][research_azam_2020]
- [Azizi and Brouwer 2017][research_azizi_brouwer_2017]
- [B Saheby et al 2019][research_bsaheby_shen_2019]
- [Ba et al 2019][research_ba_wang_2019]
- [Baag et al 2020][research_baag_mahapatra_2020]
- [Babaei et al 2018][research_babaei_setayandeh_2018]
- [Babinsky 2014][research_babinsky_2014]
- [Back et al 1967][research_back_massier_1967]
- [Back, L. H. and Cuffel, R. F. 1966][research_backlh_cuffelrf_1966]
- [Bacon 1988][research_bacon_1988]
- [Bae et al 2023][research_bae_jung_2023]
- [Bagby and Andersen 1966][research_bagby_andersen_1966]
- [Bahulekar and Mello 2024][research_bahulekar_mello_2024]
- [Bai et al 2022][research_bai_yu_2022]
- [Baidya et al 2018][research_baidya_pesyridis_2018]
- [Bailey 1963][research_bailey_1963]
- [Baker 1966][research_baker_1966]
- [Bakhle, Milind A. et al 2018][research_bakhlemilinda_reddytsr_2018]
- [Balakrishnan et al 2024][research_balakrishnan_abdrahimabutalib_2024]
- [Balas and Pearson 2019][research_balas_pearson_2019]
- [Balashov and Petukhov 1969][research_balashov_petukhov_1969]
- [Baldo and Will 1990][research_baldo_will_1990]
- [Baldwin et al 1976][research_baldwin_cliborn_1976]
- [Ball and Ross 1972][research_ball_ross_1972]
- [Balli and Caliskan 2021][research_balli_caliskan_2021]
- [Balusamy et al 2024][research_balusamy_a_2024]
- [Balut et al 2003][research_balut_davis_2003]
- [Ban et al 2018][research_ban_yamazaki_2018]
- [Bangert et al 1982][research_bangert_santman_1982]
- [Banks, Daniel W. and Paulson, John W., Jr. 1987][research_banksdanielw_paulsonjohnwjr_1987]
- [Bardera-Mora et al 2019][research_barderamora_garciamagarino_2019]
- [Baretter et al 2021][research_baretter_godard_2021]
- [Barlow et al 2008][research_barlow_burrus_2008]
- [Baron 1953][research_baron_1953]
- [Barone et al 2022][research_barone_nicholson_2022]
- [Barrett-Gonzalez and Wolf 2021][research_barrettgonzalez_wolf_2021]
- [Barry 1971][research_barry_1971]
- [Barry, F. W. 1968][research_barryfw_1968]
- [Bartman and Kwiatkowski 2018][research_bartman_kwiatkowski_2018]
- [Barton and Edwards 1968][research_barton_edwards_1968]
- [Baryshev et al 1976][research_baryshev_leontev_1976]
- [Basov et al 1977][research_basov_berezhnoy_1977]
- [Batayev et al 2022][research_batayev_suleimenov_2022]
- [Batterton, P. G. et al 1974][research_battertonpg_arpasidj_1974]
- [Battiston et al 2025][research_battiston_magrini_2025]
- [Bauer, Steven X. S. and Mcmillin, S. Naomi 1988][research_bauerstevenxs_mcmillinsnaomi_1988]
- [Bayat and EkhteraeiToussi 2017][research_bayat_ekhteraeitoussi_2017]
- [Baydar et al 2018][research_baydar_lu_2018]
- [Baydar, Ezgihan et al 2016][research_baydarezgihan_lufrankk_2016]
- [Baydar, Ezgihan et al 2017][research_baydarezgihan_lufrankk_2017]
- [Baykal and Sarikaya 1980][research_baykal_sarikaya_1980]
- [Bazhina et al 2021][research_bazhina_bazhin_2021]
- [Beck 1984][research_beck_1984]
- [Beck 1984][research_beck_1984_b]
- [Bedell 2010][research_bedell_2010]
- [Beesly 1966][research_beesly_1966]
- [Beesly 1966][research_beesly_1966_b]
- [Beevers 1973][research_beevers_1973]
- [Beheim, M. A. and Gertsma, L. W. 1956][research_beheimma_gertsmalw_1956]
- [Bekris et al 2023][research_bekris_gioldasis_2023]
- [Ben Miloud et al 2020][research_benmiloud_dghim_2020]
- [Ben-Gida and Gurka 2022][research_bengida_gurka_2022]
- [Benaouali and Kachel 2019][research_benaouali_kachel_2019]
- [Benichou et al 2021][research_benichou_binder_2021]
- [Bennet-Clark 1972][research_bennetclark_1972]
- [Bennett 2003][research_bennett_2003]
- [Benson 1977][research_benson_1977]
- [Benson, Thomas J. 1997][research_bensonthomasj_1997]
- [Beppu et al 1966][research_beppu_curtiss_1966]
- [Bera 1975][research_bera_1975]
- [Bera† 1980][research_bera_1980]
- [Berezovsky 2018][research_berezovsky_2018]
- [Bergstedt et al 1959][research_bergstedt_turner_1959]
- [Berto et al 2020][research_berto_benini_2020]
- [Berton, Jeffrey J. 2003][research_bertonjeffreyj_2003]
- [Bertram, M. H. and Ulmann, E. F. 1953][research_bertrammh_ulmannef_1953]
- [Beschorner et al 2025][research_beschorner_kriewall_2025]
- [Bhandari et al 2025][research_bhandari_gaur_2025]
- [Bhat et al 2018][research_bhat_zhao_2018]
- [Bhunia et al 2026][research_bhunia_abbas_2026]
- [Bian et al 2019][research_bian_cao_2019]
- [Bianchi et al 2020][research_bianchi_secco_2020]
- [Bidaki 2022][research_bidaki_2022]
- [Bielat, Ralph P. 1959][research_bielatralphp_1959]
- [Biesiadny, T. J. et al 1976][research_biesiadnytj_greyre_1976]
- [Biesiadny, Thomas J. and Wendt, Bruce J. 2004][research_biesiadnythomasj_wendtbrucej_2004]
- [Bihrle and Barnhart 1982][research_bihrle_barnhart_1982]
- [Bilanin and Donaldson 1975][research_bilanin_donaldson_1975]
- [Bilous et al 2026][research_bilous_vrzhizhevskyi_2026]
- [Bilwakesh, K. R. et al 1971][research_bilwakeshkr_doylevl_1971]
- [Bilwakesh, K. R. et al 1972][research_bilwakeshkr_kochcc_1972]
- [Birch et al 1978][research_birch_paynter_1978]
- [Bird, John D et al 1952][research_birdjohnd_lichtensteinjacobh_1952]
- [Biriukov 1959][research_biriukov_1959]
- [Blaha, B. J. and Johns, A. L. 1971][research_blahabj_johnsal_1971]
- [Bleviss and Struble 1954][research_bleviss_struble_1954]
- [Bloxsom 1958][research_bloxsom_1958]
- [Boger and Nussbaum 1990][research_boger_nussbaum_1990]
- [Boger et al 1989][research_boger_greer_1989]
- [Boles, Michael A. and Heavner, Richard L. 1988][research_bolesmichaela_heavnerrichardl_1988]
- [Boles, Michael A. and Heavner, Richard L. 1991][research_bolesmichaela_heavnerrichardl_1991]
- [Bollech, Thomas V. and Kelly, H. Neale 1954][research_bollechthomasv_kellyhneale_1954]
- [Bond and Key 2025][research_bond_key_2025]
- [Bond and Key 2026][research_bond_key_2026]
- [Bond et al 2025][research_bond_brown_2025]
- [Bondi 1979][research_bondi_1979]
- [Bortins, Richard and Sorensen, John A. 1993][research_bortinsrichard_sorensenjohna_1993]
- [Boudreau 1977][research_boudreau_1977]
- [Boussios et al 1992][research_boussios_epstein_1992]
- [Bouzekova-Penkova and Miteva 2022][research_bouzekovapenkova_miteva_2022]
- [Bowditch, D. N. and Coltrin, R. E. 1983][research_bowditchdn_coltrinre_1983]
- [Bowers 1981][research_bowers_1981]
- [Bowling et al 1971][research_bowling_hurkamp_1971]
- [Boylan 1965][research_boylan_1965]
- [Boytos 1969][research_boytos_1969]
- [Braithwaite and Soeder 1980][research_braithwaite_soeder_1980]
- [Braithwaite, W. M. 1973][research_braithwaitewm_1973]
- [Braithwaite, W. M. and Soeder, R. H. 1979][research_braithwaitewm_soederrh_1979]
- [Branstetter, J. R. et al 1971][research_branstetterjr_juhaszaj_1971]
- [Braun et al 2020][research_braun_paniagua_2020]
- [Bravo-Mosquera et al 2019][research_bravomosquera_abdalla_2019]
- [Brazzel et al 1970][research_brazzel_henderson_1970]
- [Breaks 1973][research_breaks_1973]
- [Bretschneider and Reed 2015][research_bretschneider_reed_2015]
- [Brianas 2005][research_brianas_2005]
- [Briggs, Benjamin R. 1960][research_briggsbenjaminr_1960]
- [Bright, Michelle M. et al 2013][research_brightmichellem_korntheuerandrea_2013]
- [Brodsky 1970][research_brodsky_1970]
- [Brooke 1957][research_brooke_1957]
- [Brophy and Hawk 1990][research_brophy_hawk_1990]
- [Brown 1970][research_brown_1970]
- [Brown, Clinton E 1946][research_brownclintone_1946]
- [Brown, S. C. et al 1983][research_brownsc_hardygh_1983]
- [Brown, Stuart C. 1959][research_brownstuartc_1959]
- [Browne et al 1948][research_browne_friedman_1948]
- [Bryant 1933][research_bryant_1933]
- [Bryce L Horvath and Douglas P Wells 2018][research_brycelhorvath_douglaspwells_2018]
- [Bryson and Rumpfkeil 2019][research_bryson_rumpfkeil_2019]
- [Bryson et al 2016][research_bryson_marks_2016]
- [Buchholz, Mark D. 1992][research_buchholzmarkd_1992]
- [Buchholz, Mark D. and Tso, Jin 1993][research_buchholzmarkd_tsojin_1993]
- [Buchsbaum 1963][research_buchsbaum_1963]
- [Bukkvoll 2024][research_bukkvoll_2024]
- [Bull, G. and Bridges, P. D. 1983][research_bullg_bridgespd_1983]
- [Bundtzen and Hinrichs 2021][research_bundtzen_hinrichs_2021]
- [Burk, S. M., Jr. and Ware, G. M. 1967][research_burksmjr_waregm_1967]
- [Burkhalter 1982][research_burkhalter_1982]
- [Burley, R. R. 1971][research_burleyrr_1971]
- [Burley, R. R. and Mansour, A. H. 1969][research_burleyrr_mansourah_1969]
- [Burley, R. R. and Mansour, A. H. 1970][research_burleyrr_mansourah_1970]
- [Burley, R. R. and Samanich, N. E. 1970][research_burleyrr_samanichne_1970]
- [Burns et al 2015][research_burns_koo_2015]
- [Burrows et al 2025][research_burrows_vukasinovic_2025]
- [Burstadt, P. L. and Calogeras, J. E. 1974][research_burstadtpl_calogerasje_1974]
- [Burstadt, P. L. and Wenzel, L. M. 1976][research_burstadtpl_wenzellm_1976]
- [Burstadt, P. L. et al 1971][research_burstadtpl_calogerasje_1971]
- [Burton et al 2004][research_burton_noordhuizen_2004]
- [Butler 1982][research_butler_1982]
- [Butler 2025][research_butler_2025]
- [Butter and Hancock 1971][research_butter_hancock_1971]
- [Buzica and Breitsamter 2020][research_buzica_breitsamter_2020]
- [Bykerk et al 2020][research_bykerk_verstraete_2020]
- [Bywater et al 2020][research_bywater_hezlett_2020]
- [C. M. 2025][research_cm_2025]
- [Cabrera Cruz et al 2020][research_cabreracruz_pezzini_2020]
- [Cai and Huang 2022][research_cai_huang_2022_c]
- [Cai et al 2022][research_cai_huang_2022]
- [Cai et al 2022][research_cai_huang_2022_b]
- [Cai et al 2023][research_cai_sun_2023]
- [Cain and Mogonye 2021][research_cain_mogonye_2021]
- [Callahan and Stenning 1971][research_callahan_stenning_1971]
- [Calligeros and Dugundji 1961][research_calligeros_dugundji_1961]
- [Calogeras, J. E. and Burstadt, P. L. 1974][research_calogerasje_burstadtpl_1974]
- [Calogeras, J. E. and Coltrin, R. E. 1969][research_calogerasje_coltrinre_1969]
- [Calogeras, J. E. et al 1974][research_calogerasje_johnsenrl_1974]
- [Campbell 1976][research_campbell_1976]
- [Campbell and Ellis 1971][research_campbell_ellis_1971]
- [Campbell et al 1978][research_campbell_hassel_1978]
- [Campion 1954][research_campion_1954]
- [Cannon 1966][research_cannon_1966]
- [Cao and Zhang 2023][research_cao_zhang_2023]
- [Cao et al 2020][research_cao_zhang_2020]
- [Cao et al 2021][research_cao_zhu_2021]
- [Cao et al 2022][research_cao_yao_2022]
- [Cao et al 2022][research_cao_yuan_2022]
- [Cao et al 2024][research_cao_yue_2024]
- [Capone, F. J. and Reubush, D. E. 1983][research_caponefj_reubushde_1983]
- [Carafoli and Berbente 1974][research_carafoli_berbente_1974]
- [Carafoli and Berbente 1976][research_carafoli_berbente_1976]
- [Carey 1982][research_carey_1982]
- [Carlin, C. M. et al 2003][research_carlincm_frischi_2003]
- [Carlson and Schwope 1952][research_carlson_schwope_1952]
- [Carlyle 1976][research_carlyle_1976]
- [Carmichael and McNay 1961][research_carmichael_mcnay_1961]
- [Carnevale et al 2016][research_carnevale_wang_2016]
- [Carosiello 1963][research_carosiello_1963]
- [Carreyette 1950][research_carreyette_1950]
- [Carroll 1960][research_carroll_1960]
- [Cary and Walker 1974][research_cary_walker_1974]
- [Cassetti 1978][research_cassetti_1978]
- [Castner et al 2017][research_castner_zaman_2017]
- [Celesio’s acquisition of wholesaler 2016][research_celesios_acquisition_2016]
- [Cervay 1975][research_cervay_1975]
- [Cetkovic 2016][research_cetkovic_2016]
- [Cevik et al 2016][research_cevik_ducvo_2016]
- [Chace 2015][research_chace_2015]
- [Chai et al 2017][research_chai_song_2017]
- [Chai et al 2018][research_chai_yu_2018]
- [Chai et al 2020][research_chai_li_2020]
- [Chakraborty et al 2015][research_chakraborty_nam_2015]
- [Chakraborty et al 2026][research_chakraborty_khan_2026]
- [Chambers and Bowman 1971][research_chambers_bowman_1971]
- [Chan et al 2017][research_chan_perreydebain_2017]
- [Chandra 2020][research_chandra_2020]
- [Chang and Hsu 1960][research_chang_hsu_1960]
- [Chang and Wei 2022][research_chang_wei_2022]
- [Chang et al 1953][research_chang_nordheim_1953]
- [Chapman 1979][research_chapman_1979]
- [Chapman, Dave et al 2005][research_chapmandave_smithcf_2005]
- [Chau and Zingg 2022][research_chau_zingg_2022]
- [Che Idris et al 2020][research_cheidris_saad_2020]
- [Chell et al 2021][research_chell_hoffenson_2021]
- [Chen and Dugundji 1980][research_chen_dugundji_1980]
- [Chen and He 2025][research_chen_he_2025]
- [Chen and Li 2020][research_chen_li_2020]
- [Chen and Tan 2019][research_chen_tan_2019]
- [Chen and Xia 2022][research_chen_xia_2022]
- [Chen and Zhang 2021][research_chen_zhang_2021]
- [Chen et al 2016][research_chen_bai_2016]
- [Chen et al 2016][research_chen_chen_2016]
- [Chen et al 2017][research_chen_tan_2017]
- [Chen et al 2018][research_chen_liu_2018]
- [Chen et al 2018][research_chen_tan_2018]
- [Chen et al 2018][research_chen_wu_2018]
- [Chen et al 2019][research_chen_tan_2019_b]
- [Chen et al 2020][research_chen_ge_2020]
- [Chen et al 2020][research_chen_mi_2020]
- [Chen et al 2020][research_chen_wu_2020]
- [Chen et al 2020][research_chen_zhang_2020]
- [Chen et al 2021][research_chen_cai_2021]
- [Chen et al 2021][research_chen_chen_2021]
- [Chen et al 2021][research_chen_ma_2021]
- [Chen et al 2021][research_chen_mi_2021]
- [Chen et al 2021][research_chen_yue_2021]
- [Chen et al 2021][research_chen_zhang_2021_b]
- [Chen et al 2022][research_chen_mi_2022]
- [Chen et al 2023][research_chen_chen_2023]
- [Chen et al 2023][research_chen_sun_2023]
- [Chen et al 2024][research_chen_dai_2024]
- [Chen et al 2025][research_chen_sethuraman_2025]
- [Chen et al 2025][research_chen_yang_2025]
- [Chen et al 2026][research_chen_jiang_2026]
- [Chen et al 2026][research_chen_lee_2026]
- [Chen et al 2026][research_chen_zheng_2026]
- [Chen, G. T. et al 1987][research_chengt_greitzerem_1987]
- [Cheng et al 2016][research_cheng_yue_2016]
- [Cheng et al 2024][research_cheng_huang_2024]
- [Cheng et al 2025][research_cheng_li_2025]
- [Chennuru et al 2025][research_chennuru_corral_2025]
- [Chesney 2005][research_chesney_2005]
- [Chessell 1979][research_chessell_1979]
- [Chester 1953][research_chester_1953]
- [Chi et al 2022][research_chi_chu_2022]
- [Child, R. D. and Henderson, W. P. 1978][research_childrd_hendersonwp_1978]
- [Chima, ROdrick V. 2011][research_chimarodrickv_2011]
- [Chima, Rodrick V. 2012][research_chimarodrickv_2012]
- [Chima, Rodrick V. et al 2011][research_chimarodrickv_hirtstefaniem_2011]
- [Chin 1977][research_chin_1977]
- [Chin 1978][research_chin_1978]
- [Chintala et al 2020][research_chintala_s_2020]
- [Chippa 2010][research_chippa_2010]
- [Choe et al 2020][research_choe_kim_2020]
- [Choi 2024][research_choi_2024]
- [Choi 2026][research_choi_2026]
- [Choi et al 2026][research_choi_choi_2026]
- [Chou and Smith 1974][research_chou_smith_1974]
- [Chouicha et al 2020][research_chouicha_sellam_2020]
- [Christian Psenica et al 2026][research_christianpsenica_leanfang_2026]
- [Chun and Burr 1969][research_chun_burr_1969]
- [Ciepluch, Carl C. 1948][research_ciepluchcarlc_1948]
- [Ciffone and Pedley 1979][research_ciffone_pedley_1979]
- [Ciliberti and Nicolosi 2026][research_ciliberti_nicolosi_2026]
- [Cirlin and Shen 1971][research_cirlin_shen_1971]
- [Clark and Hallow 1972][research_clark_hallow_1972]
- [Clark, L. E. and Richie, C. B. 1977][research_clarkle_richiecb_1977]
- [Clarke and Wallace 1964][research_clarke_wallace_1964]
- [Cliett 1952][research_cliett_1952]
- [Cloos and Nelson 1990][research_cloos_nelson_1990]
- [Coalson 1968][research_coalson_1968]
- [Coalson and Csavina 1976][research_coalson_csavina_1976]
- [Cobar and Montalvo 2021][research_cobar_montalvo_2021]
- [Coble et al 2014][research_coble_royster_2014]
- [Cobo-González and Cuerno-Rejado 2026][research_cobogonzalez_cuernorejado_2026]
- [Coe and Kulla 1974][research_coe_kulla_1974]
- [Coe, P. L., Jr. 1976][research_coepljr_1976]
- [Coffel et al 2017][research_coffel_thompson_2017]
- [Colbourne 1980][research_colbourne_1980]
- [Cole, J. B. 1980][research_colejb_1980]
- [Coleburn and Drimmer 1961][research_coleburn_drimmer_1961]
- [Coleburn and Drimmer 1962][research_coleburn_drimmer_1962]
- [Comes 2015][research_comes_2015]
- [Comodi et al 2015][research_comodi_renzi_2015]
- [Comparative studies on the 2023][research_comparative_studies_2023]
- [Competition watchdog considers Lloydspharmacy’s 2015][research_competition_watchdog_2015]
- [Composite material comprising reinforced 1978][research_composite_material_1978]
- [Composition and morphology of 2023][research_composition_and_2023]
- [Conceição et al 2019][research_conceicao_anes_2019]
- [Concept Designed and Developed 1995][research_concept_designed_1995]
- [Concorde Automatic Flight Control 1971][research_concorde_automatic_1971]
- [Cong et al 2024][research_cong_yu_2024]
- [Connors, James F and Wise, George A 1957][research_connorsjamesf_wisegeorgea_1957]
- [Control system design using 1976][research_control_system_1976]
- [Cooper 1964][research_cooper_1964]
- [Coppi and Sigmar 1973][research_coppi_sigmar_1973]
- [Corallo et al 2015][research_corallo_sheridan_2015]
- [Corcione et al 2023][research_corcione_bonavolonta_2023]
- [Cordner 1967][research_cordner_1967]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1947][research_cornellaeronauticallabincbuffalony_1947]
- [Corner 1940][research_corner_1940]
- [Cortright, Edgar M , Jr 1951][research_cortrightedgarmjr_1951]
- [Cossar et al 1980][research_cossar_moffatt_1980]
- [Costakis, W. G. 1974][research_costakiswg_1974]
- [Costakis, W. G. 1975][research_costakiswg_1975]
- [Cotton 1974][research_cotton_1974]
- [Cowles 1981][research_cowles_1981]
- [Cowshish 2023][research_cowshish_2023]
- [Cox and Bohn 1982][research_cox_bohn_1982]
- [Cox and Bohn 1982][research_cox_bohn_1982_b]
- [Cox and Roy 1988][research_cox_roy_1988]
- [Cox, Brian et al 1990][research_coxbrian_borcherspaul_1990]
- [Craidon, C., B. 1986][research_craidoncb_1986]
- [Crane, Harold L. 1948][research_craneharoldl_1948]
- [Crane, Harold L. and Beckhardt, Arnold R. 1948][research_craneharoldl_beckhardtarnoldr_1948]
- [Crea et al 2025][research_crea_marty_2025]
- [Crest Engineering Inc Tulsa Ok 1976][research_crestengineeringinctulsaok_1976]
- [Croan et al 1959][research_croan_rizzitano_1959]
- [Crossey 1992][research_crossey_1992]
- [Crosthwait 1970][research_crosthwait_1970]
- [Crothers 1997][research_crothers_1997]
- [Crowe 1937][research_crowe_1937]
- [Crown 1950][research_crown_1950]
- [Cryogenic hardening and its 2016][research_cryogenic_hardening_2016]
- [Cubillos Chacon 2007][research_cubilloschacon_2007]
- [Cui et al 2024][research_cui_zhang_2024]
- [Cummings et al 2018][research_cummings_liersch_2018]
- [Cumpsty and Greitzer 1982][research_cumpsty_greitzer_1982]
- [Cunis et al 2020][research_cunis_condomines_2020]
- [Curtiss and H. C. 1965][research_curtiss_hc_1965]
- [Curtiss and Howard C. 1969][research_curtiss_howardc_1969]
- [Custis 1978][research_custis_1978]
- [Cyrus et al 1982][research_cyrus_piscopo_1982]
- [Da et al 2020][research_da_hanan_2020]
- [da Fonseca Filho et al 2019][research_dafonsecafilho_gamaribeiro_2019]
- [Dahlberg 1963][research_dahlberg_1963]
- [Dai and Zhang 2023][research_dai_zhang_2023]
- [Dai et al 2023][research_dai_boughazi_2023]
- [Dai et al 2023][research_dai_zhao_2023]
- [Dal Magro et al 2016][research_dalmagro_benasciutti_2016]
- [Daliri et al 2018][research_daliri_farahani_2018]
- [Daniele and Teren 1975][research_daniele_teren_1975]
- [Daniele, C. J. and Teren, F. 1975][research_danielecj_terenf_1975]
- [Daroukh et al 2019][research_daroukh_moreau_2019]
- [Daroukh et al 2020][research_daroukh_polacsek_2020]
- [Das and Prasad 2023][research_das_prasad_2023]
- [Davidson 1964][research_davidson_1964]
- [Davis 1952][research_davis_1952]
- [Davis 1971][research_davis_1971]
- [Davis, David O. et al 2012][research_davisdavido_vyasmanana_2012]
- [Davis, R. A. et al 1972][research_davisra_elrodsd_1972]
- [Davoudzadeh et al 1987][research_davoudzadeh_liu_1987]
- [Day et al 1978][research_day_greitzer_1978]
- [Day et al 1978][research_day_greitzer_1978_b]
- [Dean and Young 1977][research_dean_young_1977]
- [Dear and Harrison 2022][research_dear_harrison_2022]
- [Debogdan, C. E. et al 1975][research_debogdance_dicusjh_1975]
- [Debogdan, C. E. et al 1977][research_debogdance_mossjejr_1977]
- [Defense Acquisition Univ Alexandria Va 1996, Acquisition Review quarterly Vol][research_defenseacquisitionunivalexandriava_1996]
- [Defense Acquisition Univ Alexandria Va 1997][research_defenseacquisitionunivalexandriava_1997]
- [Defense Acquisition Univ Alexandria Va 2000, Acquisition Review Quarterly. Vol][research_defenseacquisitionunivalexandriava_2000]
- [Defense Acquisition Univ Ft Belvoir Va 2007][research_defenseacquisitionunivftbelvoirva_2007]
- [Defense Acquisition Univ Ft Belvoir Va 2010][research_defenseacquisitionunivftbelvoirva_2010]
- [Dehner et al 2021][research_dehner_selamet_2021]
- [Dehua and Changyou 1993][research_dehua_changyou_1993]
- [Deitchman 1953][research_deitchman_1953]
- [Deitchman 1954][research_deitchman_1954]
- [DeLaurier 1980][research_delaurier_1980]
- [Demarchi and Haning 1978][research_demarchi_haning_1978]
- [Dement 1990][research_dement_1990]
- [Demina and Volkov 1982][research_demina_volkov_1982]
- [Demir et al 2023][research_demir_gorguluarslan_2023]
- [Denamiel et al 2021][research_denamiel_huan_2021]
- [Deng et al 2026][research_deng_li_2026]
- [Department Of Defense Washington Dc 1997][research_departmentofdefensewashingtondc_1997]
- [Department Of The Air Force Washington Dc 1980][research_departmentoftheairforcewashingtondc_1980]
- [Department Of The Air Force Washington Dc 1994][research_departmentoftheairforcewashingtondc_1994]
- [Department Of The Air Force Washington Dc 1995, Department of the Air Force, Comm][research_departmentoftheairforcewashingtondc_1995]
- [Department Of The Air Force Washington Dc 2000][research_departmentoftheairforcewashingtondc_2000]
- [Department Of The Air Force Washington Dc 2000][research_departmentoftheairforcewashingtondc_2000_b]
- [Department Of The Air Force Washington Dc 2000][research_departmentoftheairforcewashingtondc_2000_c]
- [Department Of The Army Washington Dc 1990][research_departmentofthearmywashingtondc_1990]
- [Department Of The Army Washington Dc 1995][research_departmentofthearmywashingtondc_1995]
- [Department Of The Army Washington Dc 1995][research_departmentofthearmywashingtondc_1995_b]
- [Department Of The Army Washington Dc 1996][research_departmentofthearmywashingtondc_1996]
- [Department Of The Army Washington Dc 1998, Department of the Army, Procureme][research_departmentofthearmywashingtondc_1998]
- [Department Of The Army Washington Dc 2000][research_departmentofthearmywashingtondc_2000]
- [Department Of The Army Washington Dc 2000][research_departmentofthearmywashingtondc_2000_b]
- [Department Of The Navy Washington Dc 1985][research_departmentofthenavywashingtondc_1985]
- [Department Of The Navy Washington Dc 1988][research_departmentofthenavywashingtondc_1988]
- [Department Of The Navy Washington Dc 1991][research_departmentofthenavywashingtondc_1991]
- [Desai et al 1977][research_desai_viswanathan_1977]
- [Design and Numerical Analysis 2024][research_design_and_2024]
- [Desyatnik 2015][research_desyatnik_2015]
- [Devarajan and Kapania 2020][research_devarajan_kapania_2020]
- [Devarajan and Kapania 2022][research_devarajan_kapania_2022]
- [Development of an Augmented 2016][research_development_of_2016]
- [Development of an Improved 1975][research_development_of_1975]
- [Development Testing of the 1970][research_development_testing_1970]
- [Devletian et al 1988][research_devletian_devincent_1988]
- [Dewa et al 2018][research_dewa_park_2018]
- [Deyoung, John 1950][research_deyoungjohn_1950]
- [Dghim et al 2018][research_dghim_ferchichi_2018]
- [Di Bianchi et al 2018][research_dibianchi_orra_2018]
- [Di-Marco et al 2023][research_dimarco_jacob_2023]
- [Diamantidou et al 2022][research_diamantidou_hosain_2022]
- [Dias 2023][research_dias_2023]
- [Dickey, Robert R. 1959][research_dickeyrobertr_1959]
- [Dicus 1975][research_dicus_1975]
- [Diekmann 2019][research_diekmann_2019]
- [Diesel Engine Cylinder Liner 2022][research_diesel_engine_2022]
- [Dieter Reich and Josef Wimbauer 1975][research_dieterreich_josefwimbauer_1975]
- [Diggins 1951][research_diggins_1951]
- [Dincer et al 2015][research_dincer_sarioglu_2015]
- [Ding 2023][research_ding_2023]
- [Ding et al 2015][research_ding_shen_2015]
- [Ding et al 2020][research_ding_wang_2020]
- [Ding et al 2024][research_ding_chen_2024]
- [Diphda and Wiswayana 2026][research_diphda_wiswayana_2026]
- [Discussion on Anti-surge Control 2021][research_discussion_on_2021_b]
- [Discussion on Control Points 2021][research_discussion_on_2021]
- [Discussion on the Anti-surge 2021][research_discussion_on_2021_d]
- [Discussion on the Application 2021][research_discussion_on_2021_c]
- [Dixon, Sidney C. et al 1961][research_dixonsidneyc_griffithgeorgee_1961]
- [Di̇şli̇taş and Albayrak Çeper 2021][research_dislitas_albayrakceper_2021]
- [Dobeš et al 2019][research_dobes_dymacek_2019]
- [Dobos-Bubno and Hartsook 1977][research_dobosbubno_hartsook_1977]
- [Dodds and Vahdati 2015][research_dodds_vahdati_2015]
- [Dodds and Vahdati 2015][research_dodds_vahdati_2015_b]
- [Doe 2002][research_doe_2002]
- [Doelling and Bolt 1961][research_doelling_bolt_1961]
- [Doggett, Robert V., Jr. and Soistmann, David L. 1989][research_doggettrobertvjr_soistmanndavidl_1989]
- [Dong 2019][research_dong_2019]
- [Dong et al 2015][research_dong_huang_2015]
- [Dong et al 2015][research_dong_sun_2015]
- [Dong et al 2018][research_dong_sun_2018]
- [Dong et al 2020][research_dong_choi_2020]
- [Dong et al 2022][research_dong_choi_2022]
- [Dong et al 2025][research_dong_he_2025]
- [Dong et al 2025][research_dong_liu_2025]
- [Dong et al 2026][research_dong_wang_2026]
- [Donlan, C. J. 1976][research_donlancj_1976]
- [Dowell and Ventres 1970][research_dowell_ventres_1970]
- [Driver, Cornelius 1958][research_drivercornelius_1958]
- [Du 2026][research_du_2026]
- [Du and Gao 2018][research_du_gao_2018]
- [Du et al 2023][research_du_liu_2023]
- [Du et al 2025][research_du_zhang_2025]
- [Duan et al 2020][research_duan_laima_2020]
- [Duan et al 2021][research_duan_laima_2021]
- [Duan et al 2026][research_duan_wan_2026]
- [Duan et al 2026][research_duan_zhao_2026]
- [Duda 2016][research_duda_2016]
- [Duddy et al 2020][research_duddy_landucci_2020]
- [Duffy 1968][research_duffy_1968]
- [Duffy and Shattuck 1975][research_duffy_shattuck_1975]
- [Duffy and Shattuck 1975][research_duffy_shattuck_1975_b]
- [Dugan, J. F., Jr. 1972][research_duganjfjr_1972]
- [Dugas 1986][research_dugas_1986]
- [Dunham 1962][research_dunham_1962]
- [Duran et al 2015][research_duran_fasanella_2015]
- [Durmus 2021][research_durmus_2021]
- [Dvirnyk et al 2019][research_dvirnyk_pavlenko_2019]
- [Dymáček et al 2024][research_dymacek_jary_2024]
- [E Tjahjadi et al 2019][research_etjahjadi_dagustina_2019]
- [Ebied et al 2018][research_ebied_hamada_2018]
- [Ebrahimi and Salari 2015][research_ebrahimi_salari_2015]
- [Edwards 2010][research_edwards_2010]
- [Edwards, Sherman and Hikido, Katsumi 1953][research_edwardssherman_hikidokatsumi_1953]
- [Effect of Different Radial 2023][research_effect_of_2023_b]
- [Effect of Exhaust Jet 2024][research_effect_of_2024]
- [Effect of inlet Mach 2023][research_effect_of_2023]
- [Effect of Preoperative Oral 2026][research_effect_of_2026]
- [Effects of Plyometrics, Agility 2024][research_effects_of_2024]
- [Effiom et al 2017][research_effiom_abam_2017]
- [Egan and Shadowen 1979][research_egan_shadowen_1979]
- [Egesoy 2022][research_egesoy_2022]
- [Eggers 1961][research_eggers_1961]
- [Egorov 1958][research_egorov_1958]
- [Eiband 2005][research_eiband_2005]
- [Eisenhut et al 2025][research_eisenhut_bender_2025]
- [Elliott 1968][research_elliott_1968]
- [Ellis and Brownstein 1974][research_ellis_brownstein_1974]
- [Emmons et al 1955][research_emmons_pearson_1955]
- [Emmons et al 1955][research_emmons_pearson_1955_b]
- [Englar 1975][research_englar_1975]
- [Englert, Gerald W and Obery, Leonard J 1952][research_englertgeraldw_oberyleonardj_1952]
- [Epstein 1954][research_epstein_1954]
- [Ercan and Akın 2022][research_ercan_akin_2022]
- [Erceg et al 2016][research_erceg_miletic_2016]
- [Erich 1980][research_erich_1980]
- [Esau 2024][research_esau_2024]
- [Esenwein, Fred T and Schueller, Carl F 1952][research_esenweinfredt_schuellercarlf_1952]
- [et al 2023][research___2023]
- [Eulrich and Mesiah 1974][research_eulrich_mesiah_1974]
- [Evaluation of Various Flow 2024][research_evaluation_of_2024]
- [Evans and Chamblee 1966][research_evans_chamblee_1966]
- [Evans, Alison B. 1991][research_evansalisonb_1991]
- [Evans, D. G. et al 1974][research_evansdg_debogdance_1974]
- [Eversman 2016][research_eversman_2016]
- [Evran 2019][research_evran_2019]
- [Evvard, John C 1947][research_evvardjohnc_1947]
- [Experimental determination of the 2018][research_experimental_determination_2018]
- [Experimental Study of the 2022][research_experimental_study_2022]
- [Experimental Study on the 2020][research_experimental_study_2020]
- [Eyvazian et al 2023][research_eyvazian_zhang_2023]
- [Ezrokhi and Khoreva 2018][research_ezrokhi_khoreva_2018]
- [Faisal et al 2018][research_faisal_mazni_2018]
- [Falaakh et al 2020][research_falaakh_kim_2020]
- [Faltin and Beneda 2023][research_faltin_beneda_2023]
- [Fan et al 2021][research_fan_wang_2021]
- [Fan et al 2022][research_fan_xu_2022]
- [Fan et al 2024][research_fan_liu_2024]
- [Fan et al 2025][research_fan_du_2025]
- [Fan et al 2026][research_fan_li_2026]
- [Fan et al 2026][research_fan_xu_2026]
- [Fan et al 2026][research_fan_xu_2026_b]
- [Fang and Wang 2023][research_fang_wang_2023]
- [Fang et al 2020][research_fang_zheng_2020]
- [Fang et al 2022][research_fang_zhang_2022]
- [Fang et al 2023][research_fang_sun_2023]
- [Fang et al 2023][research_fang_sun_2023_b]
- [Farahani and Mahdavi 2019][research_farahani_mahdavi_2019]
- [Farahani et al 2019][research_farahani_daliri_2019]
- [Farney and Fleharty 1969][research_farney_fleharty_1969]
- [Farr 1976][research_farr_1976]
- [Farrer 1969][research_farrer_1969]
- [Faulders 1960][research_faulders_1960]
- [Feiler and Conrad 1976][research_feiler_conrad_1976]
- [Feinreich, B. et al 1981][research_feinreichb_deganio_1981]
- [Feleo and Gamba 2025][research_feleo_gamba_2025]
- [Felix et al 2026][research_felix_perron_2026]
- [Feng et al 2020][research_feng_tao_2020]
- [Feng et al 2022][research_feng_tianyu_2022]
- [Feng et al 2025][research_feng_chen_2025]
- [Feng et al 2025][research_feng_chen_2025_b]
- [Fenwick 1966][research_fenwick_1966]
- [Fenwick 1967][research_fenwick_1967]
- [Fernandez et al 2026][research_fernandez_bronz_2026]
- [Fernando de Lima Paulo 2015][research_fernandodelimapaulo_2015]
- [Ferrero 2020][research_ferrero_2020]
- [Ferri, Antonio and Nucci, Louis M 1946][research_ferriantonio_nuccilouism_1946]
- [Ferri, Antonio and Nucci, Louis M 1951][research_ferriantonio_nuccilouism_1951]
- [Fett 1971][research_fett_1971]
- [Ficht 1979][research_ficht_1979]
- [Figat 2017][research_figat_2017]
- [Figat and Kwiek 2021][research_figat_kwiek_2021]
- [Filimonov 1972][research_filimonov_1972]
- [Findikyan et al 1966][research_findikyan_duke_1966]
- [Fine 1959][research_fine_1959]
- [Fine and Weertman 1983][research_fine_weertman_1983]
- [Finnie 1961][research_finnie_1961]
- [Finsgar 2017][research_finsgar_2017]
- [Fisher 1977][research_fisher_1977]
- [Fisher, Lewis R. and Williams, James L. 1958][research_fisherlewisr_williamsjamesl_1958]
- [FitzSimmons et al 1981][research_fitzsimmons_mckinnon_1981]
- [Flanagan, Michael J. 1992][research_flanaganmichaelj_1992]
- [Fleeter et al 1974][research_fleeter_mcclure_1974]
- [Fleeter et al 1975][research_fleeter_mcclure_1975]
- [Flow Field Study of 2020][research_flow_field_2020]
- [Flow structure and parameter 2023][research_flow_structure_2023]
- [Formentini et al 2022][research_formentini_bouissiere_2022]
- [Forward 1970][research_forward_1970]
- [Foster, G. V. and Robinson, R. B. 1961][research_fostergv_robinsonrb_1961]
- [Foster, Gerald V and Fitzpatrick, James E 1948][research_fostergeraldv_fitzpatrickjamese_1948]
- [Foust, J. W. 1979][research_foustjw_1979]
- [Fox 1969][research_fox_1969]
- [Fox and Fuchs 1978][research_fox_fuchs_1978]
- [Fraiser 1960][research_fraiser_1960]
- [Franciscus, L. 1972][research_franciscusl_1972]
- [Franciscus, L. C. and Lezberg, E. A. 1963][research_franciscuslc_lezbergea_1963]
- [Franciscus, Leo C. 1987][research_franciscusleoc_1987]
- [Franck and Dillard 2006][research_franck_dillard_2006]
- [Franck et al 2012][research_franck_lewis_2012]
- [François et al 2021][research_francois_probst_2021]
- [Fresconi et al 2014][research_fresconi_celmins_2014]
- [Frey 2014][research_frey_2014]
- [Friend, E. L. and Sakamoto, G. M. 1978][research_friendel_sakamotogm_1978]
- [Frohnapfel et al 2018][research_frohnapfel_toddlowe_2018]
- [Fu et al 2019][research_fu_chen_2019]
- [Fu et al 2021][research_fu_fu_2021]
- [Fu et al 2021][research_fu_fu_2021_b]
- [Fu et al 2023][research_fu_fu_2023]
- [Fujii et al 2021][research_fujii_fujimori_2021]
- [Fujiwara et al 2019][research_fujiwara_takagi_2019]
- [Fukusako et al 1971][research_fukusako_kiya_1971]
- [Fuller, D. E. 1967][research_fullerde_1967]
- [Furey 1983][research_furey_1983]
- [Furukawa et al 2015][research_furukawa_yamada_2015]
- [Gabriel, David S et al 1953][research_gabrieldavids_krebsrichardp_1953]
- [Gadeev et al 2017][research_gadeev_demakov_2017]
- [Gaglio et al 2023][research_gaglio_visone_2023]
- [Gahlot and Singh 2019][research_gahlot_singh_2019]
- [Galindo et al 2022][research_galindo_climent_2022]
- [Galkin and Sergeev 1976][research_galkin_sergeev_1976]
- [Ganilova et al 2021][research_ganilova_cartmell_2021]
- [Ganilova et al 2022][research_ganilova_cartmell_2022]
- [Gansler 1972][research_gansler_1972]
- [Gao et al 2015][research_gao_li_2015]
- [Gao et al 2017][research_gao_liu_2017]
- [Gao et al 2024][research_gao_wang_2024]
- [Gao et al 2025][research_gao_kong_2025]
- [Gao et al 2026][research_gao_he_2026]
- [Gao et al 2026][research_gao_zhang_2026]
- [Garcia-Benitez et al 2016][research_garciabenitez_cuernorejado_2016]
- [Garmilla Manzano et al 2026][research_garmillamanzano_fritzsche_2026]
- [Gartling 1970][research_gartling_1970]
- [Gates 1940][research_gates_1940]
- [Gayton 2004][research_gayton_2004]
- [Ge et al 2021][research_ge_shang_2021]
- [Gebhard 1953][research_gebhard_1953]
- [Gelder, Thomas F 1957][research_gelderthomasf_1957]
- [Gellatly and Gallagher 1964][research_gellatly_gallagher_1964]
- [Gellatly et al 1965][research_gellatly_bijlaard_1965]
- [Geng et al 2023][research_geng_zhang_2023]
- [Geng et al 2025][research_geng_yang_2025]
- [George et al 1964][research_george_perlmutter_1964]
- [Gergin et al 2022][research_gergin_colak_2022]
- [Gerken 1979][research_gerken_1979]
- [Gershbein and Peigin 1979][research_gershbein_peigin_1979]
- [Ghaffari, Farhad 2005][research_ghaffarifarhad_2005]
- [Ghee et al 1999][research_ghee_gonzalez_1999]
- [Gibert et al 2018][research_gibert_plestan_2018]
- [Gilinsky, M. et al 2003][research_gilinskym_gonoral_2003]
- [Gilinsky, Mikhail et al 2000][research_gilinskymikhail_morganmorrish_2000]
- [Gillen and Loth 2015][research_gillen_loth_2015]
- [Gillespie, Warren, Jr. 1960][research_gillespiewarrenjr_1960]
- [Gilruth, R R and White, M D 1941][research_gilruthrr_whitemd_1941]
- [Giner-Morency and Wong 2022][research_ginermorency_wong_2022]
- [Giuffre’ et al 2025][research_giuffre_ascione_2025]
- [Giuliano 2016][research_giuliano_2016]
- [Gliebe 1981][research_gliebe_1981]
- [Gliebe, P. R. 1980][research_gliebepr_1980]
- [Gliebe, P. R. and Kerschen, E. J. 1979][research_gliebepr_kerschenej_1979]
- [Gliszczyński et al 2021][research_gliszczynski_czechowski_2021]
- [Glorioso 1960][research_glorioso_1960]
- [Gloss, B. B. 1974][research_glossbb_1974]
- [Go and Maqsood 2015][research_go_maqsood_2015]
- [Goldstein 2004][research_goldstein_2004]
- [Goldstein 2006][research_goldstein_2006]
- [Golombek et al 2026][research_golombek_bustamante_2026]
- [Golovin and Sergievskii 1970][research_golovin_sergievskii_1970]
- [Golubkin 1980][research_golubkin_1980]
- [Golubkin 1980][research_golubkin_1980_b]
- [Gonzalo et al 2025][research_gonzalo_garciavillalba_2025]
- [Goodman 1949][research_goodman_1949]
- [Goodykoontz, J. H. et al 1972][research_goodykoontzjh_olsenwa_1972]
- [Goodykoontz, J. H. et al 1973][research_goodykoontzjh_dorschrg_1973]
- [Goodykoontz, J. H. et al 1973][research_goodykoontzjh_wagnerjm_1973]
- [Goranson, R Fabian 1942][research_goransonrfabian_1942]
- [Gorbovskoi et al 2019][research_gorbovskoi_kazhan_2019]
- [Gordon 1960][research_gordon_1960]
- [Gorelov 2023][research_gorelov_2023]
- [Gorton, Gerald C 1953][research_gortongeraldc_1953]
- [Gorton, Gerald C 1954][research_gortongeraldc_1954]
- [Gorunov 2020][research_gorunov_2020]
- [Goto et al 2021][research_goto_nakayama_2021]
- [Gotovtsev 1972][research_gotovtsev_1972]
- [Goud and Dwivedi 2022][research_goud_dwivedi_2022]
- [Goulos et al 2021][research_goulos_otter_2021]
- [Gowthaman and Sathiyagnanam 2018][research_gowthaman_sathiyagnanam_2018]
- [Graham 1969][research_graham_1969]
- [Graham et al 1954][research_graham_lagerstrom_1954]
- [Gray 1969][research_gray_1969]
- [Gray and Martins 2018][research_gray_martins_2018]
- [Gray and Wright 1970][research_gray_wright_1970]
- [Gray et al 2020][research_gray_mader_2020]
- [Gray, Justin S. et al 2017][research_grayjustins_madercharlesa_2017]
- [Greebler and Suarez 1989][research_greebler_suarez_1989]
- [Greene 1955][research_greene_1955]
- [Greene 1956][research_greene_1956]
- [Greene 1957][research_greene_1957]
- [Greene 2020][research_greene_2020]
- [Greer 2010][research_greer_2010]
- [Gregory S Jones et al 2020][research_gregorysjones_williammilholen_2020]
- [Gregory, T. J. and Wilcox, D. E. 1970][research_gregorytj_wilcoxde_1970]
- [Greitzer 1972][research_greitzer_1972]
- [Greitzer 1976][research_greitzer_1976]
- [Greitzer 1976][research_greitzer_1976_b]
- [Greitzer 1976][research_greitzer_1976_c]
- [Greitzer 1980][research_greitzer_1980]
- [Griffin, Roy N., Jr. et al 1958][research_griffinroynjr_holzhausercurta_1958]
- [Grimshaw et al 2025][research_grimshaw_pullan_2025]
- [Grin 1967][research_grin_1967]
- [Groeneweg 1977][research_groeneweg_1977]
- [Gromov and Larin 1982][research_gromov_larin_1982]
- [Gros 1963][research_gros_1963]
- [Grytsyshen et al 2025][research_grytsyshen_abramova_2025]
- [Gu et al 2023][research_gu_xu_2023]
- [Guan et al 2019][research_guan_zhou_2019]
- [Guderley 1987][research_guderley_1987]
- [Guderley 1988][research_guderley_1988]
- [Gueraiche and Popov 2018][research_gueraiche_popov_2018]
- [Guimarães et al 2018][research_guimaraes_lowe_2018]
- [Guimarães et al 2018][research_guimaraes_toddlowe_2018]
- [Gul 2015][research_gul_2015]
- [Guo 2023][research_guo_2023]
- [Guo et al 2021][research_guo_hu_2021]
- [Guo et al 2021][research_guo_tian_2021]
- [Guo et al 2022][research_guo_gao_2022]
- [Guo et al 2022][research_guo_mao_2022]
- [Guo et al 2024][research_guo_zhang_2024]
- [Guo et al 2025][research_guo_huang_2025]
- [Guo et al 2025][research_guo_liu_2025]
- [Guo et al 2025][research_guo_luo_2025]
- [Guo Pengyu et al 2019][research_guopengyu_xuezhiliang_2019]
- [Gupta and Rajput 2015][research_gupta_rajput_2015]
- [Gupta and Ramkumar 2015][research_gupta_ramkumar_2015]
- [Gurbuz and Hatunoglu 2022][research_gurbuz_hatunoglu_2022]
- [Gururaj et al 2025][research_gururaj_morris_2025]
- [Gutiérrez Álvarez and Bisagni 2021][research_gutierrezalvarez_bisagni_2021]
- [Gómez-Rodríguez et al 2019][research_gomezrodriguez_sanchezcarmona_2019]
- [Gözükara and Ceylan 2024][research_gozukara_ceylan_2024]
- [Günaydın and Doğu 2025][research_gunaydin_dogu_2025]
- [Gürbüz and Acarer 2022][research_gurbuz_acarer_2022]
- [Haas and Karanian 1981][research_haas_karanian_1981]
- [Hackman and Richardson 1964][research_hackman_richardson_1964]
- [Hah 2018][research_hah_2018]
- [Hah 2022][research_hah_2022]
- [Hale 1973][research_hale_1973]
- [Hall et al 2017][research_hall_greitzer_2017]
- [Hall et al 2022][research_hall_greitzer_2022]
- [Hall et al 2022][research_hall_greitzer_2022_b]
- [Hall, Charles F and Heitmeyer, John C 1951][research_hallcharlesf_heitmeyerjohnc_1951]
- [Halliwell 1980][research_halliwell_1980]
- [Halwas and Aggarwal 2019][research_halwas_aggarwal_2019]
- [Halwas and Aggarwal 2019][research_halwas_aggarwal_2019_b]
- [Hamaguchi et al 2020][research_hamaguchi_sakata_2020]
- [Hamid et al 2017][research_hamid_hammouda_2017]
- [Han and Han 2024][research_han_han_2024]
- [Han and Seo 2016][research_han_seo_2016]
- [Han et al 2025][research_han_jia_2025]
- [Hanazaki and Yamazaki 2024][research_hanazaki_yamazaki_2024]
- [Hancock 1959][research_hancock_1959]
- [Hancock 1959][research_hancock_1959_b]
- [Hancock 1960][research_hancock_1960]
- [Hancock, J. P. 1985][research_hancockjp_1985]
- [Hansen 1972][research_hansen_1972]
- [Hansen et al 1981][research_hansen_jorgensen_1981]
- [Hao and Jiang 2022][research_hao_jiang_2022]
- [Hao et al 2024][research_hao_liu_2024]
- [Haque et al 2016][research_haque_asrar_2016]
- [Hardie et al 1979][research_hardie_holroyd_1979]
- [Harle 1979][research_harle_1979]
- [Harman 1978][research_harman_1978]
- [Harmsworth 1961][research_harmsworth_1961]
- [Harold and Haefeli 1950][research_harold_haefeli_1950]
- [Harris, T. M. and Beerman, D. A. 1983][research_harristm_beermanda_1983]
- [Harris, T. M. et al 1984][research_harristm_beermanda_1984]
- [Harry and Trobaugh 1966][research_harry_trobaugh_1966]
- [Hart 1956][research_hart_1956]
- [Hart 1968][research_hart_1968]
- [Hart 1974][research_hart_1974]
- [Hartley et al 1965][research_hartley_furey_1965]
- [Hartmann 1968][research_hartmann_1968]
- [Hasan et al 2018][research_hasan_sachs_2018]
- [Hasegawa and Tabbone 2016][research_hasegawa_tabbone_2016]
- [Hasel, Lowell E. et al 1953][research_hasellowelle_lankfordjohnl_1953]
- [Hashin and Humphreys 1980][research_hashin_humphreys_1980]
- [Haskins 1978][research_haskins_1978]
- [Hassall 2015][research_hassall_2015]
- [Haustein and Kashi 2019][research_haustein_kashi_2019]
- [Havko et al 2020][research_havko_kapali_2020]
- [Hawkings 1974][research_hawkings_1974]
- [Hawkins, J. E. et al 1976][research_hawkinsje_kirklandfp_1976]
- [Hawkins, Richard and Penland, Jim A. 1997][research_hawkinsrichard_penlandjima_1997]
- [Hawks 1982][research_hawks_1982]
- [Hawthorne et al 1978][research_hawthorne_mitchell_1978]
- [Hayasi 1965][research_hayasi_1965]
- [Hayden and Untaroiu 2021][research_hayden_untaroiu_2021]
- [Hayden et al 2023][research_hayden_gillespie_2023]
- [Hayes, W. C., Jr. and Sleeman, W. C., Jr. 1959][research_hayeswcjr_sleemanwcjr_1959]
- [Haynes and Yang 2023][research_haynes_yang_2023]
- [Hazen and Seckel 1950][research_hazen_seckel_1950]
- [He and Shi 2025][research_he_shi_2025]
- [He and Zhang 2025][research_he_zhang_2025]
- [He et al 2025][research_he_zhao_2025]
- [He et al 2026][research_he_xie_2026]
- [He et al 2026][research_he_zhang_2026]
- [Hebert et al 1973][research_hebert_j_1973]
- [Heidelberg, Laurence J. and Hall, David G. 1992][research_heidelberglaurencej_halldavidg_1992]
- [Heidelberg, Laurence J. and Hall, David G. 1993][research_heidelberglaurencej_halldavidg_1993]
- [Heidmann et al 1980][research_heidmann_saule_1980]
- [Heimerl, George J. and Hardrath, Herbert F. 1965][research_heimerlgeorgej_hardrathherbertf_1965]
- [Hellemeier 2019][research_hellemeier_2019]
- [Helmbold 1958][research_helmbold_1958]
- [Heltsley and Crosswy 1983][research_heltsley_crosswy_1983]
- [Hemalatha and Mahalakshmi 2018][research_hemalatha_mahalakshmi_2018]
- [Henderson 1965][research_henderson_1965]
- [Herbst and Krogull 1973][research_herbst_krogull_1973]
- [Herdiana et al 2024][research_herdiana_pinindriya_2024]
- [Hernandez, Gloria et al 1994][research_hernandezgloria_woodrichardm_1994]
- [Herold and Mahoney 1974][research_herold_mahoney_1974]
- [Hess and Peng 2018][research_hess_peng_2018]
- [Hewes, Donald E. 1950][research_hewesdonalde_1950]
- [Hickey, David H 1956][research_hickeydavidh_1956]
- [Hickey, David H. and Aoyagi, Kiyoshi 1960][research_hickeydavidh_aoyagikiyoshi_1960]
- [Hickman and Morris 2017][research_hickman_morris_2017]
- [High temperature-high strength alloy 1974][research_high_temperature_high_1974]
- [Higham and Holley 1966][research_higham_holley_1966]
- [Hildebrand 1963][research_hildebrand_1963]
- [Hill 1971][research_hill_1971]
- [Hill and Defoe 2020][research_hill_defoe_2020]
- [Hill, G. C. and Bowles, J. V. 1976][research_hillgc_bowlesjv_1976]
- [Hiller Aircraft Corp Palo Alto Ca 1965][research_hilleraircraftcorppaloaltoca_1965]
- [Hiller Aircraft Corp Palo Alto Ca 1965][research_hilleraircraftcorppaloaltoca_1965_b]
- [Hiller Aircraft Corp Palo Alto Ca 1965][research_hilleraircraftcorppaloaltoca_1965_c]
- [Hillier 1970][research_hillier_1970]
- [Himeda and Naka 2019][research_himeda_naka_2019]
- [Hinkle et al 2011][research_hinkle_tulkoff_2011]
- [Hirsch 1998][research_hirsch_1998]
- [Hitzel and Osterhuber 2018][research_hitzel_osterhuber_2018]
- [Hobbs 1957][research_hobbs_1957]
- [Hodder, B. K. 1981][research_hodderbk_1981]
- [Hodder, B. K. et al 1981][research_hodderbk_farquharbw_1981]
- [Hoffler, K. D. et al 1986][research_hofflerkd_raodm_1986]
- [Hoffman 2020][research_hoffman_2020]
- [Hoffman, T. R. 2000][research_hoffmantr_2000]
- [Hogge 1969][research_hogge_1969]
- [Hoh and Mitchell 1983][research_hoh_mitchell_1983]
- [Holdaway, George H. et al 1959][research_holdawaygeorgeh_lazzeronifranka_1959]
- [Holl 1975][research_holl_1975]
- [Holm�r 1974][research_holmr_1974]
- [Holota 2020][research_holota_2020]
- [Holroyd and Hardie 1981][research_holroyd_hardie_1981]
- [Holubik 1988][research_holubik_1988]
- [Hon et al 2022][research_hon_karpuk_2022]
- [Honeycutt 1970][research_honeycutt_1970]
- [Hongpeng and Weiqiang 2016][research_hongpeng_weiqiang_2016]
- [Hooper et al 1957][research_hooper_whidden_1957]
- [Hopkins, E. J. 1975][research_hopkinsej_1975]
- [Hord and Lian 2015][research_hord_lian_2015]
- [Horton 1954][research_horton_1954]
- [Horton, Elmer A et al 1951][research_hortonelmera_loftinlaurencek_1951]
- [Hosseindokht et al 2026][research_hosseindokht_matas_2026]
- [Hosseini et al 2024][research_hosseini_vaziryzanjany_2024]
- [Hou et al 2017][research_hou_wang_2017]
- [Hou et al 2020][research_hou_zhou_2020]
- [Hribernik et al 2021][research_hribernik_kes_2021]
- [Hrubecky 1963][research_hrubecky_1963]
- [Hsu and Anderson 1961][research_hsu_anderson_1961]
- [Hu 2024][research_hu_2024]
- [Hu et al 2021][research_hu_yang_2021]
- [Hu et al 2022][research_hu_wang_2022]
- [Hu et al 2023][research_hu_qu_2023]
- [Hu et al 2024][research_hu_li_2024]
- [Hu et al 2025][research_hu_wang_2025]
- [Hu et al 2026][research_hu_qian_2026]
- [Hu et al 2026][research_hu_zhao_2026]
- [Huang et al 2016][research_huang_tan_2016]
- [Huang et al 2019][research_huang_zhang_2019]
- [Huang et al 2021][research_huang_sauzay_2021]
- [Huang et al 2022][research_huang_li_2022]
- [Huang et al 2023][research_huang_yao_2023]
- [Huang et al 2024][research_huang_bu_2024]
- [Huang et al 2024][research_huang_yao_2024]
- [Huang et al 2025][research_huang_lv_2025]
- [Huang et al 2026][research_huang_wang_2026]
- [Hubble and Smith 1979][research_hubble_smith_1979]
- [Hube 1968][research_hube_1968]
- [Hughes, D. L. and Mackall, K. G. 1984][research_hughesdl_mackallkg_1984]
- [Hui 1975][research_hui_1975]
- [Hunn 1954][research_hunn_1954]
- [Hunt and Hunt 2021][research_hunt_hunt_2021]
- [Huntley 1972][research_huntley_1972]
- [Hunziker 1960][research_hunziker_1960]
- [Huppert and Benser 1953][research_huppert_benser_1953]
- [Hutchins and Jones 1975][research_hutchins_jones_1975]
- [Hutchins and Jr 1978][research_hutchins_jr_1978]
- [Hutchinson et al 2021][research_hutchinson_lawrence_2021]
- [Hwang and Pi 1979][research_hwang_pi_1979]
- [Hwang et al 2018][research_hwang_kuo_2018]
- [Hövelmann and Breitsamter 2015][research_hovelmann_breitsamter_2015]
- [Hövelmann et al 2016][research_hovelmann_grawunder_2016]
- [Ichikawa et al 2021][research_ichikawa_koike_2021]
- [Iek, Chanthy et al 1993][research_iekchanthy_burleyrichardr_1993]
- [Ignaczak 1978][research_ignaczak_1978]
- [Ignatkin et al 2016][research_ignatkin_makeev_2016]
- [Imani et al 2017][research_imani_jahedmotlagh_2017]
- [Imani et al 2018][research_imani_malekizade_2018]
- [Imanishi et al 2015][research_imanishi_wang_2015]
- [INFLUENCE OF BACK PRESSURE 2017][research_influence_of_2017]
- [Inger and Zee 1978][research_inger_zee_1978]
- [Inglis and Larke 1958][research_inglis_larke_1958]
- [Ingraldi, Anthony M. et al 1991][research_ingraldianthonym_rerichardj_1991]
- [Initial Damage Mechanism of 2019][research_initial_damage_2019]
- [Innis, Robert C. and Quigley, Hervey C. 1961][research_innisrobertc_quigleyherveyc_1961]
- [Iqbal et al 2025][research_iqbal_shabbir_2025]
- [Irsyad Lukman and Agoes Moelyadi 2018][research_irsyadlukman_agoesmoelyadi_2018]
- [Iseki and Nicholas 1979][research_iseki_nicholas_1979]
- [Ishihara et al 2020][research_ishihara_suzuki_2020]
- [Islam et al 2015][research_islam_fermin_2015]
- [Isugiyama 1976][research_isugiyama_1976]
- [Ito et al 2016][research_ito_dhaene_2016]
- [Ivanov 2022][research_ivanov_2022]
- [Jablon 1972][research_jablon_1972]
- [Jack, John R 1951][research_jackjohnr_1951]
- [Jacobs 1973][research_jacobs_1973]
- [Jacocks and Kneile 1975][research_jacocks_kneile_1975]
- [Jafari and Nikolaidis 2018][research_jafari_nikolaidis_2018]
- [Jakubowski 2019][research_jakubowski_2019]
- [James F Connors et al 1957][research_jamesfconnors_georgeawise_1957]
- [James L Felder et al 2022][research_jameslfelder_michaelttong_2022]
- [Janzen and Precourt 1989][research_janzen_precourt_1989]
- [Jaquet, Byron M 1951][research_jaquetbyronm_1951]
- [Jardin and Colonius 2018][research_jardin_colonius_2018]
- [Jarvinen 1973][research_jarvinen_1973]
- [Jassim 2016][research_jassim_2016]
- [Jayarani and Narmadhai 2024][research_jayarani_narmadhai_2024]
- [Jeffs and Lancaster 2015][research_jeffs_lancaster_2015]
- [Jelev et al 2019][research_jelev_keane_2019]
- [Jenkins and Marks 1975][research_jenkins_marks_1975]
- [Jenkins, J. M. 1979][research_jenkinsjm_1979]
- [Jenkins, Jerald M. and Kuhl, Albert E. 1977][research_jenkinsjeraldm_kuhlalberte_1977]
- [Jenney 1935][research_jenney_1935]
- [Jeong et al 2015][research_jeong_choi_2015]
- [Jeyaraj and Liscouët-Hanke 2022][research_jeyaraj_liscouethanke_2022]
- [Ji et al 2018][research_ji_yu_2018]
- [Ji et al 2021][research_ji_yuan_2021]
- [Ji et al 2022][research_ji_hu_2022]
- [Ji et al 2023][research_ji_kim_2023]
- [Ji et al 2024][research_ji_huang_2024]
- [Jia et al 2024][research_jia_chen_2024]
- [Jiandong et al 2021][research_jiandong_qiming_2021]
- [Jiang et al 2024][research_jiang_li_2024]
- [Jiang et al 2024][research_jiang_yao_2024]
- [Jiang et al 2026][research_jiang_liu_2026]
- [Jiao et al 2017][research_jiao_chang_2017]
- [Jie et al 2017][research_jie_zhibin_2017]
- [Jin et al 2022][research_jin_sun_2022]
- [Jin et al 2023][research_jin_tan_2023]
- [Jin et al 2023][research_jin_zhang_2023]
- [Jing 2018][research_jing_2018]
- [Joarder 2018][research_joarder_2018]
- [Johns, A. L. and Steffen, F. W. 1970][research_johnsal_steffenfw_1970]
- [Johnson and Lawing 1977][research_johnson_lawing_1977]
- [Johnson and Wu 1975][research_johnson_wu_1975]
- [Johnson et al 1959][research_johnson_henderson_1959]
- [Johnson et al 1960][research_johnson_henderson_1960]
- [Johnson III and Wu 1974][research_johnsoniii_wu_1974]
- [Johnson, H. J. and Montoya, E. J. 1973][research_johnsonhj_montoyaej_1973]
- [Jonathan A Lee and Po-Shou Chen 2005][research_jonathanalee_poshouchen_2005]
- [Jones 1972][research_jones_1972]
- [Jones 1973][research_jones_1973]
- [Jones and Placzankis 2016][research_jones_placzankis_2016]
- [Jones et al 2016][research_jones_medina_2016]
- [Jones, Arthur L et al 1947][research_jonesarthurl_flanaganmildredg_1947]
- [Jones, G. W., Jr. and Unangst, J. R. 1963][research_jonesgwjr_unangstjr_1963]
- [Jones, J. R. and Shrewsbury, G. D. 1968][research_jonesjr_shrewsburygd_1968]
- [Jones, R. T. 1976][research_jonesrt_1976]
- [Jones, Robert T 1956][research_jonesrobertt_1956]
- [Jones, Robert T. 1953][research_jonesrobertt_1953]
- [Jordan 1973][research_jordan_1973]
- [Ju et al 2020][research_ju_sun_2020]
- [Ju et al 2022][research_ju_deng_2022]
- [Juknevicius and Chong 2018][research_juknevicius_chong_2018]
- [Jung et al 2015][research_jung_lee_2015]
- [Jung et al 2022][research_jung_oh_2022]
- [Justicia Alados et al 2026][research_justiciaalados_trezza_2026]
- [K James et al 2021][research_kjames_suryan_2021]
- [K. James and Kim 2022][research_kjames_kim_2022]
- [Ka 2018][research_ka_2018]
- [Kaczorowski et al 2015][research_kaczorowski_skoczylas_2015]
- [Kadir et al 2019][research_kadir_beg_2019]
- [Kalkan 2024][research_kalkan_2024]
- [Kamani et al 2023][research_kamani_mirzaee_2023]
- [Kametani et al 2017][research_kametani_kotake_2017]
- [Kaminski et al 2018][research_kaminski_witkowska_2018]
- [Kan et al 2019][research_kan_muransky_2019]
- [Kananoja et al 2025][research_kananoja_kosonen_2025]
- [Kanda 1982][research_kanda_1982]
- [Kang et al 2024][research_kang_kang_2024]
- [Kang et al 2024][research_kang_li_2024]
- [Kang et al 2024][research_kang_liang_2024]
- [Kaplan 1980][research_kaplan_1980]
- [Kapoor, Kamlesh et al 1994][research_kapoorkamlesh_andersonbernhardh_1994]
- [Kar et al 2016][research_kar_panda_2016]
- [Karabacak and Turan 2020][research_karabacak_turan_2020]
- [Karimi and Oboodi 2018][research_karimi_oboodi_2018]
- [Karl et al 2025][research_karl_werner_2025]
- [Kasama et al 2020][research_kasama_suzuki_2020]
- [Kase et al 2020][research_kase_mizoguchi_2020]
- [Kasozi et al 2015][research_kasozi_siddharthan_2015]
- [Katariya and Panda 2016][research_katariya_panda_2016]
- [Katz 1971][research_katz_1971]
- [Katz 2021][research_katz_2021]
- [Kawamura and Karashima 1957][research_kawamura_karashima_1957]
- [Kawamura, T. et al 1987][research_kawamurat_chyuwj_1987]
- [Kawanabe and Lei 2025][research_kawanabe_lei_2025]
- [Kawase and Rona 2019][research_kawase_rona_2019]
- [Kawase and Rona 2019][research_kawase_rona_2019_b]
- [Kaye and Yeh 1955][research_kaye_yeh_1955]
- [Kayiran 2025][research_kayiran_2025]
- [Kayser and Danberg 1974][research_kayser_danberg_1974]
- [Kayser and Hillsamer 1960][research_kayser_hillsamer_1960]
- [Kazula and Höschler 2020][research_kazula_hoschler_2020]
- [Kazula and Höschler 2021][research_kazula_hoschler_2021]
- [Kazula et al 2019][research_kazula_mischke_2019]
- [Kbab et al 2023][research_kbab_haif_2023]
- [Kegels and Skovgaard Ølykke 2025][research_kegels_skovgaardlykke_2025]
- [Keller et al 2018][research_keller_hasan_2018]
- [Kelley, Mark W and Tolhurst, William H JR 1955][research_kelleymarkw_tolhurstwilliamhjr_1955]
- [Kelly, Mark W et al 1958][research_kellymarkw_andersonsethb_1958]
- [Kennedy and Gerhardt 1972][research_kennedy_gerhardt_1972]
- [Khademi et al 2019][research_khademi_ikeda_2019]
- [Khaleghi 2015][research_khaleghi_2015]
- [Khan and Hasan 2021][research_khan_hasan_2021]
- [Khan and Tariq 2026][research_khan_tariq_2026]
- [Khatri and Sinha 2023][research_khatri_sinha_2023]
- [Khazaali and Fereshteh-Saniee 2018][research_khazaali_fereshtehsaniee_2018]
- [Khobragade and Kumar 2022][research_khobragade_kumar_2022]
- [Khobragade et al 2021][research_khobragade_unnikrishnan_2021]
- [Khobragade et al 2024][research_khobragade_gustavsson_2024]
- [Kholyavko 1971][research_kholyavko_1971]
- [Khoroshun and Soltanov 1977][research_khoroshun_soltanov_1977]
- [Khoroshun and Soltanov 1978][research_khoroshun_soltanov_1978]
- [Kiani 2017][research_kiani_2017]
- [Kida and Miyai 1978][research_kida_miyai_1978]
- [Kidwell 1963][research_kidwell_1963]
- [Kier, D. A. et al 1972][research_kierda_powersbg_1972]
- [Kigotho et al 2022][research_kigotho_bodylski_2022]
- [Kikkawa 1955][research_kikkawa_1955]
- [Kilimtzidis and Kostopoulos 2023][research_kilimtzidis_kostopoulos_2023]
- [Kim 2024][research_kim_2024]
- [Kim and Kwon 2015][research_kim_kwon_2015]
- [Kim and Lee 2022][research_kim_lee_2022]
- [Kim and Park 2026][research_kim_park_2026]
- [Kim et al 2015][research_kim_kim_2015]
- [Kim et al 2015][research_kim_kim_2015_b]
- [Kim et al 2022][research_kim_choi_2022]
- [Kim et al 2023][research_kim_ramlim_2023]
- [Kim et al 2026][research_kim_kim_2026]
- [Kim, HyoungJin et al 2011][research_kimhyoungjin_kumanotakayasu_2011]
- [Kimura et al 2018][research_kimura_imai_2018]
- [Kinard, Tim A. et al 1995][research_kinardtima_harrisbrendaw_1995]
- [King, R. W. et al 1976][research_kingrw_schuermanja_1976]
- [Kinsler, Martin R 1958][research_kinslermartinr_1958]
- [Kirk and Barrack 1969][research_kirk_barrack_1969]
- [Kishi et al 2022][research_kishi_kanazaki_2022]
- [Kiss and Spakovszky 2018][research_kiss_spakovszky_2018]
- [Klann, G. A. et al 1984][research_klannga_barthrl_1984]
- [Kleckner, Harold F 1945][research_klecknerharoldf_1945]
- [Kleckner, Harold F 1946][research_klecknerharoldf_1946]
- [Klein, Vladislav 1999][research_kleinvladislav_1999]
- [Klimchik et al 2015][research_klimchik_chablat_2015]
- [Klimowitch 1978][research_klimowitch_1978]
- [Klujber 1973][research_klujber_1973]
- [Knight 1991][research_knight_1991]
- [Knobbe 2002][research_knobbe_2002]
- [Knowles et al 2017][research_knowles_tu_2017]
- [Ko, William L. and Fields, Roger A. 1987][research_kowilliaml_fieldsrogera_1987]
- [Kobayashi 1974][research_kobayashi_1974]
- [Kobayashi 1984][research_kobayashi_1984]
- [Kolb 2020][research_kolb_2020]
- [Kolnsberg 1979][research_kolnsberg_1979]
- [Kolom 1969][research_kolom_1969]
- [Konar et al 1974][research_konar_mahesh_1974]
- [Kong and Kim 2016][research_kong_kim_2016]
- [Kong and Park 2018][research_kong_park_2018]
- [Kong et al 2020][research_kong_zhou_2020]
- [Kong et al 2022][research_kong_li_2022]
- [Kong et al 2022][research_kong_zhou_2022]
- [Kong et al 2023][research_kong_zhou_2023]
- [Kong et al 2026][research_kong_su_2026]
- [Kong et al 2026][research_kong_sun_2026]
- [Kopasakis, George et al 2012][research_kopasakisgeorge_connollyjosephw_2012]
- [Kopasakis, George et al 2012][research_kopasakisgeorge_connollyjosephw_2012_b]
- [Kopzon 1958][research_kopzon_1958]
- [Korn 1974][research_korn_1974]
- [Kornienko and Shmanenkov 1981][research_kornienko_shmanenkov_1981]
- [Kornreich 1992][research_kornreich_1992]
- [Koster 2004][research_koster_2004]
- [Kosuge et al 1982][research_kosuge_ito_1982]
- [Kothari 1971][research_kothari_1971]
- [Kothari 1973][research_kothari_1973]
- [Kotov et al 2018][research_kotov_ruleva_2018]
- [Kovács et al 2023][research_kovacs_csik_2023]
- [Kowalski et al 2021][research_kowalski_goraj_2021]
- [Koyyalamudi and Nagpurwala 2016][research_koyyalamudi_nagpurwala_2016]
- [Kozakevich et al 2022][research_kozakevich_stroh_2022]
- [Kozakiewicz et al 2025][research_kozakiewicz_adamczyk_2025]
- [Kozlov 1966][research_kozlov_1966]
- [Kraiko and Tilliaeva 1973][research_kraiko_tilliaeva_1973]
- [Kraiko and Tkalenko 1967][research_kraiko_tkalenko_1967]
- [Kramer and Hall 2026][research_kramer_hall_2026]
- [Kramer, B. E. and Potter, D. Y. 1966][research_kramerbe_potterdy_1966]
- [Krashchenko and Statsenko 1981][research_krashchenko_statsenko_1981]
- [Krause 1981][research_krause_1981]
- [Krause 1997][research_krause_1997]
- [Krawczyk et al 2024][research_krawczyk_paul_2024]
- [Krenkel and Salzman 1968][research_krenkel_salzman_1968]
- [Kretov 2021][research_kretov_2021]
- [Krishnaswamy and Nath 1982][research_krishnaswamy_nath_1982]
- [Krivenyuk et al 1971][research_krivenyuk_tsvilyuk_1971]
- [Krosche and Heinze 2015][research_krosche_heinze_2015]
- [Krupa 2019][research_krupa_2019]
- [Krushnarao Kotteda and Mittal 2016][research_krushnaraokotteda_mittal_2016]
- [Kuchinka 1966][research_kuchinka_1966]
- [Kuhlmann and Sauer 2019][research_kuhlmann_sauer_2019]
- [Kuhn 1979][research_kuhn_1979]
- [Kumar 2022][research_kumar_2022]
- [Kumar and Capolungo 2022][research_kumar_capolungo_2022]
- [Kumar and Gaur 2017][research_kumar_gaur_2017]
- [Kumar and Pradeep 2022][research_kumar_pradeep_2022]
- [Kumar et al 2021][research_kumar_darsigunta_2021]
- [Kumar et al 2025][research_kumar_sastri_2025]
- [Kurkov et al 1975][research_kurkov_soeder_1975]
- [Kuz'mich et al 1975][research_kuzmich_sekundov_1975]
- [Kuzmin 2024][research_kuzmin_2024]
- [Kwee et al 2019][research_kwee_dewaele_2019]
- [Kwiatkowski et al 2022][research_kwiatkowski_sieradzki_2022]
- [Kwiek 2019][research_kwiek_2019]
- [Küçük and Tuncer 2024][research_kucuk_tuncer_2024]
- [L'Ecuyer et al 1971][research_lecuyer_morrison_1971]
- [Ladia Apsari Hasibuan et al 2025][research_ladiaapsarihasibuan_agussulastio_2025]
- [Lahnsteiner 2022][research_lahnsteiner_2022]
- [Lai and Findley 1980][research_lai_findley_1980]
- [Lai and Kamaruddin 2018][research_lai_kamaruddin_2018]
- [Lamar, J. E. 1986][research_lamarje_1986]
- [Lamar, John E. 1987][research_lamarjohne_1987]
- [Lambert, H. H. and Mizukami, M. 1999][research_lamberthh_mizukamim_1999]
- [Lampropoulos and Sarris 2025][research_lampropoulos_sarris_2025]
- [Lapin and Sharov 1974][research_lapin_sharov_1974]
- [Lapin et al 1952][research_lapin_crookshanks_1952]
- [Lappas and Ikenaga 2019][research_lappas_ikenaga_2019]
- [Large 1981][research_large_1981]
- [Larrabee, E. E. 1975][research_larrabeeee_1975]
- [Lavi 1967][research_lavi_1967]
- [Lawley and Koczak 1984][research_lawley_koczak_1984]
- [Lawley and Koczak 1985][research_lawley_koczak_1985]
- [Lawrence 1953][research_lawrence_1953]
- [Leahy et al 1995][research_leahy_michaelb_1995]
- [Lee and Duh 2017][research_lee_duh_2017]
- [Lee and Kim 2024][research_lee_kim_2024]
- [Lee and Ko 2018][research_lee_ko_2018]
- [Lee and Sanders 2002][research_lee_sanders_2002]
- [Lee and Yee 2024][research_lee_yee_2024]
- [Lee et al 2018][research_lee_lim_2018]
- [Lee et al 2019][research_lee_lee_2019]
- [Lee et al 2022][research_lee_lim_2022]
- [Lee et al 2023][research_lee_nam_2023]
- [Lee, B. J. et al 2018][research_leebj_lioumayfun_2018]
- [Lee, Byung Joon and Liou, May-Fun 2018][research_leebyungjoon_lioumayfun_2018]
- [Lee, Byung Joon et al 2019][research_leebyungjoon_lioumayfun_2019]
- [Lee, J. A. 1998][research_leeja_1998]
- [Lee, Jonathan A. 2003][research_leejonathana_2003]
- [Lee, Jonathan A. and Chen, Po-Shou 2002][research_leejonathana_chenposhou_2002]
- [Lee, Jonathan A. and Munafo, Paul M. 2002][research_leejonathana_munafopaulm_2002]
- [Legros et al 2018][research_legros_lutoshkina_2018]
- [Lehtinen and Zeller 1972][research_lehtinen_zeller_1972]
- [Lehtinen, B. and Zeller, J. R. 1971][research_lehtinenb_zellerjr_1971]
- [Lehtinen, B. et al 1978][research_lehtinenb_zellerjr_1978]
- [Leitner 1986][research_leitner_1986]
- [Leknys et al 2018][research_leknys_arjomandi_2018]
- [Lemay, S. P. et al 1988][research_lemaysp_batillsm_1988]
- [Leng et al 2024][research_leng_feng_2024]
- [Lengyel-Kampmann et al 2024][research_lengyelkampmann_karboujian_2024]
- [Leslie 1952][research_leslie_1952]
- [Leslie and Perry 1954][research_leslie_perry_1954]
- [Levinsky et al 1968][research_levinsky_thommen_1968]
- [Levy, Lionel L., Jr. 1959][research_levylionelljr_1959]
- [Levy, Lionel L., Jr. and Yoshikawa, Kenneth K. 1959][research_levylionelljr_yoshikawakennethk_1959]
- [Lewis 1976][research_lewis_1976]
- [Lewis 1998][research_lewis_1998]
- [Li and Geiselhart 2021][research_li_geiselhart_2021]
- [Li and Geiselhart 2022][research_li_geiselhart_2022]
- [Li and Geiselhart 2026][research_li_geiselhart_2026]
- [Li and Sun 2022][research_li_sun_2022]
- [Li et al 2015][research_li_pan_2015]
- [Li et al 2015][research_li_xu_2015]
- [Li et al 2018][research_li_sun_2018]
- [Li et al 2019][research_li_du_2019]
- [Li et al 2019][research_li_soskin_2019]
- [Li et al 2020][research_li_du_2020]
- [Li et al 2020][research_li_du_2020_b]
- [Li et al 2021][research_li_dong_2021]
- [Li et al 2021][research_li_tian_2021]
- [Li et al 2021][research_li_zheng_2021]
- [Li et al 2021][research_li_zhou_2021]
- [Li et al 2022][research_li_dong_2022]
- [Li et al 2022][research_li_liu_2022]
- [Li et al 2022][research_li_lyu_2022]
- [Li et al 2022][research_li_zhu_2022]
- [Li et al 2023][research_li_ding_2023]
- [Li et al 2023][research_li_kedeng_2023]
- [Li et al 2023][research_li_pan_2023]
- [Li et al 2023][research_li_qiao_2023]
- [Li et al 2023][research_li_wang_2023]
- [Li et al 2023][research_li_zheng_2023]
- [Li et al 2023][research_li_zhu_2023]
- [Li et al 2024][research_li_chen_2024]
- [Li et al 2024][research_li_chu_2024]
- [Li et al 2024][research_li_fang_2024]
- [Li et al 2024][research_li_hou_2024]
- [Li et al 2024][research_li_li_2024]
- [Li et al 2024][research_li_liu_2024]
- [Li et al 2024][research_li_liu_2024_b]
- [Li et al 2024][research_li_lu_2024]
- [Li et al 2024][research_li_xia_2024]
- [Li et al 2024][research_li_xu_2024]
- [Li et al 2024][research_li_xu_2024_b]
- [Li et al 2024][research_li_zhu_2024]
- [Li et al 2024][research_li_zhu_2024_b]
- [Li et al 2025][research_li_dong_2025]
- [Li et al 2025][research_li_dong_2025_b]
- [Li et al 2025][research_li_qu_2025]
- [Li et al 2025][research_li_sun_2025]
- [Li et al 2026][research_li_zhao_2026]
- [Lian et al 2025][research_lian_xiong_2025]
- [Lichtenstein, Jacob H 1952][research_lichtensteinjacobh_1952]
- [Lieu 1964][research_lieu_1964]
- [Liew, K. H. et al 2005][research_liewkh_uripe_2005]
- [Likhachev 2024][research_likhachev_2024]
- [Lin et al 2020][research_lin_shao_2020]
- [Lin et al 2021][research_lin_liu_2021]
- [Lin et al 2022][research_lin_bai_2022]
- [Lin et al 2022][research_lin_zhang_2022]
- [Lin et al 2025][research_lin_li_2025]
- [Lin et al 2026][research_lin_zong_2026]
- [Linehan and Mohseni 2020][research_linehan_mohseni_2020]
- [Linek et al 2016][research_linek_chytilek_2016]
- [Ling 1970][research_ling_1970]
- [Linnell 1963][research_linnell_1963]
- [Liu and Cao 2017][research_liu_cao_2017]
- [Liu and Jiang 2022][research_liu_jiang_2022]
- [Liu and Vo 2024][research_liu_vo_2024]
- [Liu et al 2015][research_liu_zhu_2015]
- [Liu et al 2016][research_liu_li_2016]
- [Liu et al 2018][research_liu_gao_2018]
- [Liu et al 2018][research_liu_zhang_2018]
- [Liu et al 2021][research_liu_chen_2021]
- [Liu et al 2021][research_liu_wang_2021]
- [Liu et al 2022][research_liu_kang_2022]
- [Liu et al 2022][research_liu_li_2022]
- [Liu et al 2022][research_liu_zhang_2022]
- [Liu et al 2023][research_liu_cao_2023]
- [Liu et al 2023][research_liu_feng_2023]
- [Liu et al 2023][research_liu_huang_2023]
- [Liu et al 2023][research_liu_li_2023]
- [Liu et al 2024][research_liu_chu_2024]
- [Liu et al 2024][research_liu_zhu_2024]
- [Liu et al 2025][research_liu_chu_2025]
- [Liu et al 2025][research_liu_du_2025]
- [Liu et al 2025][research_liu_yu_2025]
- [Liu et al 2025][research_liu_zhu_2025]
- [Liu et al 2025][research_liu_zhu_2025_b]
- [Liu et al 2026][research_liu_du_2026]
- [Liu et al 2026][research_liu_zhu_2026]
- [Lock 1957][research_lock_1957]
- [Lockwood, V. E. 1966][research_lockwoodve_1966]
- [Lomakin et al 2024][research_lomakin_fedorenko_2024]
- [Lomax, Harvard 1957][research_lomaxharvard_1957]
- [Lomax, Harvard and Heaslet, Max A 1956][research_lomaxharvard_heasletmaxa_1956]
- [Longest 1964][research_longest_1964]
- [Lou et al 2022][research_lou_harrison_2022]
- [Lourenco et al 1996][research_lourenco_shih_1996]
- [Loveless and Boswell 1954][research_loveless_boswell_1954]
- [Lovell, J Calvin and Wilson, Herbert A JR 1947][research_lovelljcalvin_wilsonherbertajr_1947]
- [Lowe 1967][research_lowe_1967]
- [Lowe 2020][research_lowe_2020]
- [Lu et al 2017][research_lu_zhang_2017]
- [Lu et al 2019][research_lu_yang_2019]
- [Lu et al 2022][research_lu_zhang_2022]
- [Lu et al 2025][research_lu_li_2025]
- [Lu et al 2025][research_lu_wang_2025]
- [Lu et al 2025][research_lu_zhang_2025]
- [Lu-ning et al 2021][research_luning_bangqin_2021]
- [Lucas 1978][research_lucas_1978]
- [Luce and Jr 1949][research_luce_jr_1949]
- [Ludwig 1979][research_ludwig_1979]
- [Lukyanov et al 2024][research_lukyanov_hoang_2024]
- [Lunde, T. 1977][research_lundet_1977]
- [Luo 2018][research_luo_2018]
- [Luo et al 2020][research_luo_wei_2020]
- [Luo et al 2024][research_luo_tao_2024]
- [Luo et al 2026][research_luo_meng_2026]
- [Lv et al 2022][research_lv_zhang_2022]
- [Lv et al 2022][research_lv_zhang_2022_b]
- [Lv et al 2025][research_lv_wang_2025]
- [Lyga 1990][research_lyga_1990]
- [Lyu 1963][research_lyu_1963]
- [Lyubimov 2024][research_lyubimov_2024]
- [Lyubimov and Potekhina 2016][research_lyubimov_potekhina_2016]
- [López et al 2017][research_lopez_baldomir_2017]
- [M et al 2017][research_m_v_2017]
- [M. and Mukherjee 2017][research_m_mukherjee_2017]
- [M. Jamhuri et al 2024][research_mjamhuri_nizar_2024]
- [Ma 2021][research_ma_2021]
- [Ma et al 2018][research_ma_cui_2018]
- [Ma et al 2021][research_ma_colon_2021]
- [Ma et al 2022][research_ma_jia_2022]
- [Ma et al 2022][research_ma_karpuk_2022]
- [Ma et al 2022][research_ma_zhang_2022]
- [Ma et al 2025][research_ma_li_2025]
- [Ma et al 2025][research_ma_lu_2025]
- [Ma et al 2025][research_ma_wang_2025]
- [Ma et al 2026][research_ma_li_2026]
- [MacDermott et al 1965][research_macdermott_dix_1965]
- [MacDermott et al 1966][research_macdermott_dix_1966]
- [MacManus et al 2017][research_macmanus_chiereghin_2017]
- [Maeda 1961][research_maeda_1961]
- [Maekawa et al 1978][research_maekawa_higashi_1978]
- [Maghsoudi et al 2020][research_maghsoudi_vaziry_2020]
- [Magrini and Benini 2023][research_magrini_benini_2023]
- [Magrini and Benini 2026][research_magrini_benini_2026]
- [Mahjouri et al 2023][research_mahjouri_shabani_2023]
- [Mahlmeister et al 1955][research_mahlmeister_ishimoto_1955]
- [Mahorter and Robert G. 1961][research_mahorter_robertg_1961]
- [Maikapar 1959][research_maikapar_1959]
- [Maikapar 1966][research_maikapar_1966]
- [Maise 1970][research_maise_1970]
- [Makarov 2019][research_makarov_2019]
- [Maki, Ralph L. 1959][research_makiralphl_1959]
- [Maksimovich et al 1977][research_maksimovich_karpinos_1977]
- [Malashenko and Vashchilo 1975][research_malashenko_vashchilo_1975]
- [Malicki et al 2023][research_malicki_malecha_2023]
- [Malikov and Miltsov 2019][research_malikov_miltsov_2019]
- [Mallik et al 2015][research_mallik_kapania_2015]
- [Malmuth 1966][research_malmuth_1966]
- [Malmuth 1966][research_malmuth_1966_b]
- [Malone, Michael B. and Peavey, Charles C. 1999][research_malonemichaelb_peaveycharlesc_1999]
- [Malvi and Roy 2021][research_malvi_roy_2021]
- [Mamonova et al 2019][research_mamonova_soudakov_2019]
- [Mansfield 1967][research_mansfield_1967]
- [Manthena and Kedar 2017][research_manthena_kedar_2017]
- [Mao and Liu 2016][research_mao_liu_2016]
- [Mao and Zhang 2025][research_mao_zhang_2025]
- [Mao et al 2017][research_mao_liu_2017]
- [Maples 1979][research_maples_1979]
- [Margalida et al 2020][research_margalida_joseph_2020]
- [Margolis, Kenneth 1947][research_margoliskenneth_1947]
- [Margolis, Kenneth et al 1958][research_margoliskenneth_malvestutofranksjr_1958]
- [Marshall 1973][research_marshall_1973]
- [Marshall, R. T. 1971][research_marshallrt_1971]
- [Martin 1961][research_martin_1961]
- [Marty et al 2022][research_marty_castillon_2022]
- [Masaki et al 2021][research_masaki_ogushi_2021]
- [Masilamani and Suresh 2021][research_masilamani_suresh_2021]
- [Mason, W. H. 1983][research_masonwh_1983]
- [Mason, W. H. et al 1983][research_masonwh_siclarimj_1983]
- [Mathauser, Eldon E and Deveikis, William D 1955][research_mathausereldone_deveikiswilliamd_1955]
- [Mathauser, Eldon E and Deveikis, William D 1957][research_mathausereldone_deveikiswilliamd_1957]
- [MATHEMATICAL MODELING AND EXPERIMENTAL 2018][research_mathematical_modeling_2018]
- [Mathur 1969][research_mathur_1969]
- [Matlák et al 2017][research_matlak_racz_2017]
- [Matranga, Gene J. and Armstrong, Neil A. 1959][research_matrangagenej_armstrongneila_1959]
- [Matsuda et al 2026][research_matsuda_matsuno_2026]
- [Matsumoto and Sekiya 1975][research_matsumoto_sekiya_1975]
- [Matzdorf et al 1999][research_matzdorf_kane_1999]
- [Mauch et al 1980][research_mauch_oldakowski_1980]
- [Mays 1971][research_mays_1971]
- [Mazhul 2020][research_mazhul_2020]
- [Mazurov 2015][research_mazurov_2015]
- [Mazurov 2019][research_mazurov_2019]
- [Mazzawy, R. S. and Banks, G. A. 1976][research_mazzawyrs_banksga_1976]
- [Mazzawy, R. S. and Banks, G. A. 1977][research_mazzawyrs_banksga_1977]
- [McAnally et al 1970][research_mcanally_williamj_1970]
- [McAnally et al 1971][research_mcanally_iii_1971]
- [Mcaulay, J. E. and Abdelwahab, M. 1972][research_mcaulayje_abdelwahabm_1972]
- [McCormick 1959][research_mccormick_1959]
- [McDaniel and Cooper 1999][research_mcdaniel_cooper_1999]
- [McDaniel et al 1995][research_mcdaniel_bull_1995]
- [McDaniel et al 1998][research_mcdaniel_bull_1998]
- [Mcdonald et al 1971][research_mcdonald_fox_1971]
- [Mcdonnell Aircraft Corp St Louis Mo 1963][research_mcdonnellaircraftcorpstlouismo_1963]
- [Mcdonough 1953][research_mcdonough_1953]
- [McKeehen and Cord 1997][research_mckeehen_cord_1997]
- [McLean and Stacey 1970][research_mclean_stacey_1970]
- [McLemore, H. Clyde 1958][research_mclemorehclyde_1958]
- [McLemore, H. Clyde and Peterson, John B., Jr. 1960][research_mclemorehclyde_petersonjohnbjr_1960]
- [Mcmillin, S. N. and Wood, R. M. 1986][research_mcmillinsn_woodrm_1986]
- [McNicol 2014][research_mcnicol_2014]
- [McNicol 2014][research_mcnicol_2014_b]
- [McNicol and Wu 2014][research_mcnicol_wu_2014]
- [McQueen 1976][research_mcqueen_1976]
- [Mechanism of Stability Enhancement 2021][research_mechanism_of_2021]
- [Mechanism study on the 2023][research_mechanism_study_2023]
- [Mehar et al 2021][research_mehar_mishra_2021]
- [Melick, H. C., Jr. 1973][research_melickhcjr_1973]
- [Menees, Gene P. and Boyd, John W. 1959][research_meneesgenep_boydjohnw_1959]
- [Menegozzo and Benini 2020][research_menegozzo_benini_2020]
- [Meng et al 2018][research_meng_fan_2018]
- [Meng et al 2025][research_meng_ma_2025]
- [Mennell, R. 1970][research_mennellr_1970]
- [Menon 2020][research_menon_2020]
- [Menon and Suresh 2022][research_menon_suresh_2022]
- [Menon et al 2023][research_menon_sanjayshivam_2023]
- [Merchant and Radhakrishnan 2017][research_merchant_radhakrishnan_2017]
- [Merkli 1975][research_merkli_1975]
- [Merkli 1976][research_merkli_1976]
- [Merrill, Walter C. et al 1991][research_merrillwalterc_delaatjohnc_1991]
- [Metzger et al 2022][research_metzger_rienzi_2022]
- [Meyer 1938][research_meyer_1938]
- [Meyer 1959][research_meyer_1959]
- [Mi et al 2017][research_mi_yao_2017]
- [Miao et al 2026][research_miao_guan_2026]
- [Michell, G. A. 1971][research_michellga_1971]
- [Miele 1954][research_miele_1954]
- [Miele, Angelo 1955][research_mieleangelo_1955]
- [Mihalik and Keane 2022][research_mihalik_keane_2022]
- [Mikhail 1979][research_mikhail_1979]
- [Mikhailov et al 2017][research_mikhailov_mikhailova_2017]
- [Miki et al 2015][research_miki_watanabe_2015]
- [Milenković-Babić 2018][research_milenkovicbabic_2018]
- [Milenković-Babić et al 2017][research_milenkovicbabic_samardzic_2017]
- [Miles 1953][research_miles_1953]
- [MILITARY PRESENCE AND ARMS 2025][research_military_presence_2025]
- [Miller, D. S. et al 1983][research_millerds_pittmanjl_1983]
- [Mills 1978][research_mills_1978]
- [Min et al 2024][research_min_xian_2024]
- [Min Tint 2018][research_mintint_2018]
- [Min, J. B. et al 2018][research_minjb_reddytsr_2018]
- [Minervino et al 2016][research_minervino_vitagliano_2016]
- [Mineta et al 2022][research_mineta_saijo_2022]
- [Ming et al 2023][research_ming_wu_2023]
- [Minnicino et al 2009][research_minnicino_gray_2009]
- [Mireles et al 2019][research_mireles_ficke_2019]
- [Mirzaei and Kiani 2015][research_mirzaei_kiani_2015]
- [Mitsuyasu 1956][research_mitsuyasu_1956]
- [Miura and Kohzu 2020][research_miura_kohzu_2020]
- [Miura et al 2021][research_miura_yamashita_2021]
- [Miyashita et al 2025][research_miyashita_sugihara_2025]
- [Mizobata et al 2024][research_mizobata_mio_2024]
- [Moeckel, W E 1955][research_moeckelwe_1955]
- [Moeckel, W E and Evans, P J , Jr 1951][research_moeckelwe_evanspjjr_1951]
- [Moffat et al 1978][research_moffat_healzer_1978]
- [Mohammad 2021][research_mohammad_2021]
- [Moin and Lele 1998][research_moin_lele_1998]
- [Moirou et al 2023][research_moirou_sanders_2023]
- [Mokotoff et al 2026][research_mokotoff_arnson_2026]
- [Molana et al 2020][research_molana_khodaparast_2020]
- [Monkova et al 2023][research_monkova_monka_2023]
- [Montano, J. W. 1967][research_montanojw_1967]
- [Moon 2025][research_moon_2025]
- [Moon 2025][research_moon_2025_b]
- [Moore 1973][research_moore_1973]
- [Moore and Lueke 1974][research_moore_lueke_1974]
- [Moorhouse and Jenkins 1975][research_moorhouse_jenkins_1975]
- [Morgan et al 1961][research_morgan_thomson_1961]
- [Morris 1986][research_morris_1986]
- [Morton 1956][research_morton_1956]
- [Moru et al 2022][research_moru_bo_2022]
- [Mosca et al 2024][research_mosca_sudhi_2024]
- [Mount 1965][research_mount_1965]
- [Moëns 2022][research_moens_2022]
- [Muchmore, C. B., Jr. 1988][research_muchmorecbjr_1988]
- [Muehter 1974][research_muehter_1974]
- [Mugridge 1975][research_mugridge_1975]
- [Muir et al 2017][research_muir_arredondogaleana_2017]
- [Mulgund, Sandeep S. 1994][research_mulgundsandeeps_1994]
- [Muller and Gasko 1967][research_muller_gasko_1967]
- [Muller and Gasko 1967][research_muller_gasko_1967_b]
- [Mungall, Robert C 1948][research_mungallrobertc_1948]
- [Munjulury et al 2015][research_munjulury_staack_2015]
- [Munk et al 2019][research_munk_auld_2019]
- [Muraida et al 1998][research_muraida_grimes_1998]
- [Murphy, Patrick C. and Klein, Vladislav 2006][research_murphypatrickc_kleinvladislav_2006]
- [Musa et al 2024][research_musa_huang_2024]
- [Mushkat 1979][research_mushkat_1979]
- [Mushtaq and Gaetani 2023][research_mushtaq_gaetani_2023]
- [Mushtaq and Gaetani 2023][research_mushtaq_gaetani_2023_b]
- [Mushtaq et al 2024][research_mushtaq_pini_2024]
- [Myers, Lawrence P. and Walsh, Kevin R. 1988][research_myerslawrencep_walshkevinr_1988]
- [Myokan et al 2020][research_myokan_kubota_2020]
- [Mårtensson 2021][research_martensson_2021]
- [Mårtensson and Billson 2024][research_martensson_billson_2024]
- [Mårtensson and Billson 2024][research_martensson_billson_2024_b]
- [Mårtensson et al 2022][research_martensson_lejon_2022]
- [N.A. 2021][research_na_2021]
- [Nagamatsu et al 1960][research_nagamatsu_workman_1960]
- [Nagao et al 2019][research_nagao_yoshida_2019]
- [Nagasaka et al 2019][research_nagasaka_muroga_2019]
- [Nageswara Rao and Kushari 2020][research_nageswararao_kushari_2020]
- [Nagler 2022][research_nagler_2022]
- [Nagler 2026][research_nagler_2026]
- [Nakajima and Yanagawa 1963][research_nakajima_yanagawa_1963]
- [Nam and Mavris 2018][research_nam_mavris_2018]
- [Nandy et al 2021][research_nandy_baag_2021]
- [Narayan 1975][research_narayan_1975]
- [Narendhiran 2017][research_narendhiran_2017]
- [Naruse et al 2022][research_naruse_ishii_2022]
- [Naseri et al 2016][research_naseri_boroomand_2016]
- [Naval Proving Ground Dahlgren Va 1945][research_navalprovinggrounddahlgrenva_1945]
- [Naval Sea Systems Command Washington Dc 2010][research_navalseasystemscommandwashingtondc_2010]
- [Negaard 1979][research_negaard_1979]
- [Neitzel and Hemsworth 1966][research_neitzel_hemsworth_1966]
- [Nelms, W. P., Jr. and Bailey, R. O. 1974][research_nelmswpjr_baileyro_1974]
- [Nelson, D. P. 1983][research_nelsondp_1983]
- [Nelson, D. P. and Bresnahan, D. L. 1983][research_nelsondp_bresnahandl_1983]
- [Nelson, Robert L. and Welsh, Clement J. 1960][research_nelsonrobertl_welshclementj_1960]
- [Ness 1971][research_ness_1971]
- [Neumark 1950][research_neumark_1950]
- [Neverlien et al 2020][research_neverlien_moe_2020]
- [Newsom, William A., Jr. and Tosti, Louis P. 1959][research_newsomwilliamajr_tostilouisp_1959]
- [Newsome, R. W. and Thomas, J. L. 1986][research_newsomerw_thomasjl_1986]
- [Ng and Datta 2019][research_ng_datta_2019]
- [Ng and Willcox 2016][research_ng_willcox_2016]
- [Ngan, Angelen and Biezad, Daniel 1996][research_nganangelen_biezaddaniel_1996]
- [Nguyen, L. T. et al 1976][research_nguyenlt_anglinel_1976]
- [Nicholas et al 2023][research_nicholas_pernak_2023]
- [Nichols, Mark R and Pendley, Robert E 1952][research_nicholsmarkr_pendleyroberte_1952]
- [Nicolay et al 2021][research_nicolay_karpuk_2021]
- [Nielsen, J. N. 1985][research_nielsenjn_1985]
- [Nielsen, Jack N et al 1953][research_nielsenjackn_kaattarigeorgee_1953]
- [Niewald, Roy J and Moul, Martin T 1950][research_niewaldroyj_moulmartint_1950]
- [Nikitenko 2018][research_nikitenko_2018]
- [Nimal et al 2019][research_nimal_m_2019]
- [Nisiyama and Tanimura 1967][research_nisiyama_tanimura_1967]
- [Nithin Joseph Reddy et al 2019][research_nithinjosephreddy_sathiskumar_2019]
- [Niu et al 2019][research_niu_sui_2019]
- [Niu et al 2025][research_niu_ye_2025]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952_b]
- [Northrop Aircraft Inc Hawthorne Ca 1953][research_northropaircraftinchawthorneca_1953]
- [Northrop Aircraft Inc Hawthorne Ca 1956][research_northropaircraftinchawthorneca_1956]
- [Northrop Corp Hawthorne Ca Norair Div 1964][research_northropcorphawthornecanorairdiv_1964]
- [Northrop Corp Hawthorne Ca Norair Div 1964][research_northropcorphawthornecanorairdiv_1964_b]
- [Novak, R. C. 1974][research_novakrc_1974]
- [Numerical Simulation of Supersonic 2020][research_numerical_simulation_2020]
- [Nussdorfer, Theodore J et al 1952][research_nussdorfertheodorej_oberyleonardj_1952]
- [Nöding and Bertsch 2021][research_noding_bertsch_2021]
- [O'Connell and Komšić 2026][research_oconnell_komsic_2026]
- [O'Malley et al 1987][research_omalley_chamot_1987]
- [Obey, Leonard T et al 1952][research_obeyleonardt_englertgeraldw_1952]
- [Ochonogor et al 2017][research_ochonogor_akinlabi_2017]
- [Oehman, W. I. 1983][research_oehmanwi_1983]
- [Ogawa and Takeda 2015][research_ogawa_takeda_2015]
- [Ohashi and Ohno 1982][research_ohashi_ohno_1982]
- [Ohlsson 1964][research_ohlsson_1964]
- [Ohwada et al 2019][research_ohwada_shimada_2019]
- [Ohyama 1978][research_ohyama_1978]
- [Okorokov and Gorash 2017][research_okorokov_gorash_2017]
- [Okumoto and Elsanker 1973][research_okumoto_elsanker_1973]
- [Old 1957][research_old_1957]
- [Opalka 1968][research_opalka_1968]
- [Ordaz and Li 2016][research_ordaz_li_2016]
- [Ordaz et al 2015][research_ordaz_geiselhart_2015]
- [Orloff and Ciffone 1974][research_orloff_ciffone_1974]
- [Orman et al 1951][research_orman_rae_1951]
- [Oruc and Baklacioglu 2022][research_oruc_baklacioglu_2022]
- [Oruc and Baklacioglu 2023][research_oruc_baklacioglu_2023]
- [Orysh and Betz 1964][research_orysh_betz_1964]
- [Osborne, Robert S and Kelly, Thomas C 1953][research_osborneroberts_kellythomasc_1953]
- [Ostieri and Tognaccini 2018][research_ostieri_tognaccini_2018]
- [Ostowari, C. and Naik, D. 1986][research_ostowaric_naikd_1986]
- [Othman and Kanazaki 2016][research_othman_kanazaki_2016]
- [Ou et al 2017][research_ou_maricq_2017]
- [Ouyang et al 2020][research_ouyang_yang_2020]
- [Overall 1976][research_overall_1976]
- [P Raj et al 2003][research_praj_fghaffari_2003]
- [Packman et al 1977][research_packman_kozlowski_1977]
- [Page et al 2018][research_page_hield_2018]
- [Page et al 2021][research_page_bergstrom_2021]
- [Pai and Weibel 2022][research_pai_weibel_2022]
- [Pakle and Jiang 2018][research_pakle_jiang_2018]
- [Palaia 2025][research_palaia_2025]
- [Palienko et al 1976][research_palienko_pogrebnyak_1976]
- [Palko 1973][research_palko_1973]
- [Palko 1974][research_palko_1974]
- [Palko 1975][research_palko_1975]
- [Pan and Huang 2019][research_pan_huang_2019]
- [Pan et al 2017][research_pan_huang_2017]
- [Pan et al 2022][research_pan_shi_2022]
- [Pan et al 2024][research_pan_mu_2024]
- [Pan et al 2024][research_pan_shi_2024]
- [Panov and Shvets 1967][research_panov_shvets_1967]
- [Panov et al 1966][research_panov_shvets_1966]
- [Panton 1972][research_panton_1972]
- [Panton 1973][research_panton_1973]
- [Panzeri et al 2018][research_panzeri_savelyev_2018]
- [Pao and Banerjee 1978][research_pao_banerjee_1978]
- [Papadales and Basil S. 1979][research_papadales_basils_1979]
- [Papageorgiou et al 2018][research_papageorgiou_tarkian_2018]
- [Paraguassu 2015][research_paraguassu_2015]
- [Paranjape and Ananthkrishnan 2023][research_paranjape_ananthkrishnan_2023]
- [Parisen, Richard B et al 1948][research_parisenrichardb_armstrongjohnc_1948]
- [Park and Lee 2025][research_park_lee_2025]
- [Park and Zaki 2018][research_park_zaki_2018]
- [Park et al 2015][research_park_lee_2015]
- [Park et al 2016][research_park_chung_2016]
- [Park et al 2016][research_park_chung_2016_b]
- [Park et al 2018][research_park_chung_2018]
- [Park et al 2026][research_park_kim_2026]
- [Parkes 1953][research_parkes_1953]
- [Parkes 1954][research_parkes_1954]
- [Parkes 1956][research_parkes_1956]
- [Parkes 1956][research_parkes_1956_b]
- [Parrish and Jr 1978][research_parrish_jr_1978]
- [Parthasarathy, S. P. et al 1975][research_parthasarathysp_massierpf_1975]
- [Pashchenko et al 2022][research_pashchenko_kharchenko_2022]
- [Pasiuk 1963][research_pasiuk_1963]
- [Patel and Chudoba 2026][research_patel_chudoba_2026]
- [Patel et al 2020][research_patel_dubey_2020]
- [Patil 2018][research_patil_2018]
- [Patil and Suresh 2021][research_patil_suresh_2021]
- [Paul et al 2019][research_paul_suresh_2019]
- [Paulk and Anderson 1976][research_paulk_anderson_1976]
- [Pavlov 2016][research_pavlov_2016]
- [Payne 1957][research_payne_1957]
- [Paziresh et al 2017][research_paziresh_nikseresht_2017]
- [Pendergraft, Odis C., Jr. et al 1992][research_pendergraftodiscjr_ingraldianthonym_1992]
- [Pendley and Marsh 1968][research_pendley_marsh_1968]
- [Peng and Zhai 2015][research_peng_zhai_2015]
- [Peng et al 2018][research_peng_tu_2018]
- [Peng et al 2024][research_peng_li_2024]
- [Peng-ju et al 2015][research_pengju_liang_2015]
- [Penland, J. A. et al 1975][research_penlandja_fournierrh_1975]
- [Penland, J. A. et al 1978][research_penlandja_creeltrjr_1978]
- [Pennington, J. E. and Meintel, A. J., Jr. 1980][research_penningtonje_meintelajjr_1980]
- [Pereira and Williams 2015][research_pereira_williams_2015]
- [Peri 2023][research_peri_2023]
- [Pernica et al 2024][research_pernica_palavenis_2024]
- [Perrin 2021][research_perrin_2021]
- [Petersen, R. B. 1957][research_petersenrb_1957]
- [Peterson, Victor L. and Menees, Gene P. 1959][research_petersonvictorl_meneesgenep_1959]
- [Petkovic et al 2025][research_petkovic_banjac_2025]
- [Petricone and Sisto 1971][research_petricone_sisto_1971]
- [Petrov and Pigusov 2019][research_petrov_pigusov_2019]
- [Pettes-Duler et al 2021][research_pettesduler_roboam_2021]
- [Pečinka et al 2017][research_pecinka_bugajski_2017]
- [Pfaff 1965][research_pfaff_1965]
- [Pfaff 1968][research_pfaff_1968]
- [Pflag 1972][research_pflag_1972]
- [Pfnür and Breitsamter 2019][research_pfnur_breitsamter_2019]
- [Philippou et al 2024][research_philippou_zachos_2024]
- [Phillips and Jr 1999][research_phillips_jr_1999]
- [Phillips et al 2015][research_phillips_knowles_2015]
- [PHYSICAL AND THERMAL PROPERTIES 2017][research_physical_and_2017]
- [Picard and Whitley 2002][research_picard_whitley_2002]
- [Piccirillo et al 2024][research_piccirillo_gregorio_2024]
- [Pigusov 2021][research_pigusov_2021]
- [Pimenta et al 1979][research_pimenta_moffat_1979]
- [Pinapatruni et al 2025][research_pinapatruni_sinha_2025]
- [ping and Hong 2022][research_ping_hong_2022]
- [Piovesan et al 2025][research_piovesan_zachos_2025]
- [Platonov and Nikitenko 2019][research_platonov_nikitenko_2019]
- [Plourde and Stenning 1968][research_plourde_stenning_1968]
- [Poggi et al 2024][research_poggi_bernardini_2024]
- [Polhamus, E. C. 1966][research_polhamusec_1966]
- [Polhamus, E. C. 1968][research_polhamusec_1968]
- [Poll and Schumann 2024][research_poll_schumann_2024]
- [Pope, H. A. 1971][research_popeha_1971]
- [Portnoy 1963][research_portnoy_1963]
- [Pouryoussefi et al 2023][research_pouryoussefi_abdolali_2023]
- [Powell, A. G. et al 1985][research_powellag_welgehr_1985]
- [Powers 1964][research_powers_1964]
- [Powers, B. G. 1966][research_powersbg_1966]
- [Prasad 2025][research_prasad_2025]
- [Preisser, J. S. et al 1981][research_preisserjs_schoensterja_1981]
- [Preisser, J. S. et al 1984][research_preisserjs_silcoxrj_1984]
- [Presz et al 1971][research_presz_konarski_1971]
- [Prigent et al 2015][research_prigent_marechal_2015]
- [Prince 1976][research_prince_1976]
- [Priya and Arora 2025][research_priya_arora_2025]
- [Probst and Melber-Wilkending 2021][research_probst_melberwilkending_2021]
- [Procurement Process Geared Up 1980][research_procurement_process_1980]
- [Proesmans and Vos 2022][research_proesmans_vos_2022]
- [Provenza et al 2018][research_provenza_duffy_2018]
- [Pucillo 2016][research_pucillo_2016]
- [Pue 2021][research_pue_2021]
- [Puett 1967][research_puett_1967]
- [Puett 1968][research_puett_1968]
- [Purser, Paul E. and Spear, Margaret F. 1947][research_purserpaule_spearmargaretf_1947]
- [Puvrez 1965][research_puvrez_1965]
- [Pyle 1971][research_pyle_1971]
- [Qi et al 2021][research_qi_zong_2021]
- [Qi et al 2024][research_qi_jin_2024]
- [Qian 2025][research_qian_2025]
- [Qian et al 2025][research_qian_xinhui_2025]
- [Qiang et al 2024][research_qiang_xue_2024]
- [Qiao et al 2019][research_qiao_li_2019]
- [Qiao et al 2026][research_qiao_chu_2026]
- [Qin 2026][research_qin_2026]
- [Qin and Liang 2016][research_qin_liang_2016]
- [Qiu et al 2022][research_qiu_chen_2022]
- [Qiu et al 2023][research_qiu_du_2023]
- [Qiu et al 2023][research_qiu_zhao_2023]
- [Qiu et al 2024][research_qiu_zhong_2024]
- [Qu et al 2019][research_qu_chen_2019]
- [Qu et al 2019][research_qu_kong_2019]
- [Qu et al 2024][research_qu_wang_2024]
- [Quan et al 2024][research_quan_sun_2024]
- [Queijo, M J and Wolhart, Walter D 1951][research_queijomj_wolhartwalterd_1951]
- [Queijo, M J et al 1954][research_queijomj_jaquetbyronm_1954]
- [Quigley, Hervey C. et al 1960][research_quigleyherveyc_andersonsethb_1960]
- [Radespiel et al 2016][research_radespiel_burnazzi_2016]
- [Radon 1969][research_radon_1969]
- [Rains 1955][research_rains_1955]
- [Rajdeep Bose Mondal 2026][research_rajdeepbosemondal_2026]
- [Ramakrishna et al 2019][research_ramakrishna_senthilkumar_2019]
- [Ramamurti 2011][research_ramamurti_2011]
- [Ramaswamy and Viswanathan 1975][research_ramaswamy_viswanathan_1975]
- [Ramjet supersonic “flight tests” 1958][research_ramjet_supersonic_1958]
- [Ramprasadh and Devanandh 2015][research_ramprasadh_devanandh_2015]
- [Rand 1963][research_rand_1963]
- [Rao et al 2016][research_rao_vpatel_2016]
- [Rao et al 2022][research_rao_sureshkumar_2022]
- [Rao et al 2023][research_rao_chen_2023]
- [Rao et al 2025][research_rao_kumar_2025]
- [Raspet 1957][research_raspet_1957]
- [Ratnayake, Nalin A. 2010][research_ratnayakenalina_2010]
- [Ray, E. J. and Taylor, R. T. 1965][research_rayej_taylorrt_1965]
- [Reader 1976][research_reader_1976]
- [Rebizov 2022][research_rebizov_2022]
- [Rebuffet, Pierre and Poisson-Quinton, PH 1952][research_rebuffetpierre_poissonquintonph_1952]
- [Reedy and Gorrell 2025][research_reedy_gorrell_2025]
- [Rees 1977][research_rees_1977]
- [Rehman 2022][research_rehman_2022]
- [Reichert and Brock 1977][research_reichert_brock_1977]
- [Reid 1937][research_reid_1937]
- [Reid and Moore 1980][research_reid_moore_1980]
- [Reimer and Hudson 1998][research_reimer_hudson_1998]
- [Reinbold et al 2026][research_reinbold_breitsamter_2026]
- [Reist et al 2022][research_reist_koo_2022]
- [Ren et al 2021][research_ren_zhang_2021]
- [Ren et al 2023][research_ren_zheng_2023]
- [Report and discussion on 1966][research_report_and_1966]
- [Report no. 609, Experimental 1937][research_report_no_1937]
- [Report No. 648, Design 1939][research_report_no_1939]
- [Reshotko et al 1977][research_reshotko_karchmer_1977]
- [Resta et al 2021][research_resta_marsilio_2021]
- [Rettie and Lewis 1968][research_rettie_lewis_1968]
- [Reukauf, P. J. and Burcham, F. W., Jr. 1976][research_reukaufpj_burchamfwjr_1976]
- [Reworkable Edgebond Applied Wafer-Level 2016][research_reworkable_edgebond_2016]
- [Reyhner and Hickcox 1972][research_reyhner_hickcox_1972]
- [Reykers and Fonck 2019][research_reykers_fonck_2019]
- [Reza Maadi and Sepahi-Younsi 2022][research_rezamaadi_sepahiyounsi_2022]
- [Ribner 1960][research_ribner_1960]
- [Riccio et al 2026][research_riccio_giaquinto_2026]
- [Riccobene and Ricci 2015][research_riccobene_ricci_2015]
- [Rice and Oetting 1976][research_rice_oetting_1976]
- [Richards, W. L. and Thompson, Randolph C. 1991][research_richardswl_thompsonrandolphc_1991]
- [Riffel and Fleeter 1981][research_riffel_fleeter_1981]
- [Riffin 1943][research_riffin_1943]
- [Righi et al 2018][research_righi_pachidis_2018]
- [Riley 1976][research_riley_1976]
- [Rinehart 1971][research_rinehart_1971]
- [Ritapure and Kharde 2018][research_ritapure_kharde_2018]
- [Rivello 1965][research_rivello_1965]
- [RlDHA 1969][research_rldha_1969]
- [Roache 1965][research_roache_1965]
- [Roark and Cuda 2010][research_roark_cuda_2010]
- [Robert S. Osborne and Thomas C. Kelly 1960][research_robertsosborne_thomasckelly_1960]
- [Roberts 1965][research_roberts_1965]
- [Roberts et al 1966][research_roberts_smith_1966]
- [Robins, A. W. et al 1985][research_robinsaw_beissnerfljr_1985]
- [Rockwell 2001][research_rockwell_2001]
- [Rodgers 1965][research_rodgers_1965]
- [Rodgers 1966][research_rodgers_1966]
- [Rodriguez and Liscouët-Hanke 2025][research_rodriguez_liscouethanke_2025]
- [Roelofs et al 2021][research_roelofs_kurowicka_2021]
- [Rokicki 1982][research_rokicki_1982]
- [Roland and Rumpfkeil 2017][research_roland_rumpfkeil_2017]
- [Romanov 2021][research_romanov_2021]
- [Rosenbaum, H. and Zeiberg, S. L. 1965][research_rosenbaumh_zeibergsl_1965]
- [Roskam and Dusto 1969][research_roskam_dusto_1969]
- [Roskam et al 1968][research_roskam_holgate_1968]
- [Rowe 1958][research_rowe_1958]
- [Rowe and Sussman 1971][research_rowe_sussman_1971]
- [Roy Salam and Bil 2016][research_roysalam_bil_2016]
- [Ruban et al 2020][research_ruban_menezes_2020]
- [Rubio and Ballard 1967][research_rubio_ballard_1967]
- [Rudolph, Peter K. C. 1997][research_rudolphpeterkc_1997]
- [Ruh et al 2026][research_ruh_warner_2026]
- [Rumsey et al 2019][research_rumsey_slotnick_2019]
- [Rumsey, Charles B. and Lee, Dorothy B. 1961][research_rumseycharlesb_leedorothyb_1961]
- [Rybalko and Loth 2015][research_rybalko_loth_2015]
- [Rylov 1974][research_rylov_1974]
- [S.C. Pradhan 2023][research_scpradhan_2023]
- [Saadon and Talib 2016][research_saadon_talib_2016]
- [Sachs 1975][research_sachs_1975]
- [Sachs 1977][research_sachs_1977]
- [Safavi et al 2015][research_safavi_tarkian_2015]
- [Safoklov et al 2025][research_safoklov_demidov_2025]
- [Sahai et al 2017][research_sahai_snellen_2017]
- [Said et al 2018][research_said_mat_2018]
- [Sajadifar et al 2023][research_sajadifar_maier_2023]
- [Sakamoto et al 2021][research_sakamoto_sasaki_2021]
- [Sakata and Ohta 2017][research_sakata_ohta_2017]
- [Sakata, I. F. and Davis, G. W. 1977][research_sakataif_davisgw_1977]
- [Sakata, I. F. et al 1975][research_sakataif_davisgw_1975]
- [Sakurada et al 1965][research_sakurada_nakajima_1965]
- [Salama and Said 2023][research_salama_said_2023]
- [Saleem Yusoof et al 2016][research_saleemyusoof_sivapragasam_2016]
- [Samberger et al 2023][research_samberger_weissensteiner_2023]
- [Samimy et al 2011][research_samimy_webb_2011]
- [Samuelsson and Grönstedt 2021][research_samuelsson_gronstedt_2021]
- [Sanchez and Liscouët-Hanke 2020][research_sanchez_liscouethanke_2020]
- [Sanchez et al 2021][research_sanchez_liscouethanke_2021]
- [Sanchez-Carmona and Cuerno-Rejado 2018][research_sanchezcarmona_cuernorejado_2018]
- [Sandahl, Carl A 1948][research_sandahlcarla_1948]
- [Sandeep Ramesh Kumar and Suresh 2021][research_sandeeprameshkumar_suresh_2021]
- [Sandstrom and White 1961][research_sandstrom_white_1961]
- [Saporito et al 2023][research_saporito_daronch_2023]
- [Saravanan et al 2017][research_saravanan_desikan_2017]
- [Sarikaya et al 2024][research_sarikaya_zarri_2024]
- [Sarodo et al 2024][research_sarodo_yamamoto_2024]
- [Sartor et al 2016][research_sartor_becker_2016]
- [Sato and Kon 1972][research_sato_kon_1972]
- [Sattar et al 1971][research_sattar_stargardter_1971]
- [Saunders, J. D. and Keith, T. G., Jr. 1991][research_saundersjd_keithtgjr_1991]
- [Saves et al 2024][research_saves_diouane_2024]
- [Saxena, Ashok 1998][research_saxenaashok_1998]
- [Schaffrath et al 2025][research_schaffrath_nicke_2025]
- [Schatz et al 2016][research_schatz_hermanutz_2016]
- [Scherz and Williams 1978][research_scherz_williams_1978]
- [Schneider, Edward T. 1990][research_schneideredwardt_1990]
- [Schnell and Grossman 1979][research_schnell_grossman_1979]
- [Schoeler 1987][research_schoeler_1987]
- [Schueltke and Stumpf 2017][research_schueltke_stumpf_2017]
- [Schuldenfrei, Marvin et al 1947][research_schuldenfreimarvin_comisarowpaul_1947]
- [Schulderfrei, Marvin et al 1951][research_schulderfreimarvin_comisarowpaul_1951]
- [Schumann and Sharman 2015][research_schumann_sharman_2015]
- [Schwanz 1972][research_schwanz_1972]
- [Schweikhardt and Grippe 1971][research_schweikhardt_grippe_1971]
- [Schwendemann, M. F. 1981][research_schwendemannmf_1981]
- [Scorer and Davenport 1970][research_scorer_davenport_1970]
- [Sebata and Ushijima 2021][research_sebata_ushijima_2021]
- [Sebata and Ushijima 2022][research_sebata_ushijima_2022]
- [Secchi et al 2021][research_secchi_lacava_2021]
- [Sedlock 1985][research_sedlock_1985]
- [Segletes 2004][research_segletes_2004]
- [Seidel et al 1980][research_seidel_matwey_1980]
- [Sekar et al 2024][research_sekar_kengaiah_2024]
- [Seleznev 2018][research_seleznev_2018]
- [Seleznev 2019][research_seleznev_2019]
- [Semenov 1981][research_semenov_1981]
- [Semlitsch and Mihăescu 2016][research_semlitsch_mihaescu_2016]
- [Semlitsch and Mihăescu 2021][research_semlitsch_mihaescu_2021]
- [Sepahi-Younsi 2022][research_sepahiyounsi_2022]
- [Sepahi-Younsi 2025][research_sepahiyounsi_2025]
- [Setayandeh and Babaei 2020][research_setayandeh_babaei_2020]
- [Sgueglia et al 2020][research_sgueglia_schmollgruber_2020]
- [Shafer et al 1990][research_shafer_junghans_1990]
- [Shahin et al 2016][research_shahin_alqaradawi_2016]
- [Shahriyari et al 2024][research_shahriyari_firouzabadi_2024]
- [Shaikh et al 2023][research_shaikh_kahlon_2023]
- [Shang et al 2021][research_shang_ge_2021]
- [Shao et al 2016][research_shao_cao_2016]
- [Shao et al 2025][research_shao_xu_2025]
- [Shariatzadeh et al 2015][research_shariatzadeh_abrishamkar_2015]
- [She et al 2017][research_she_yuan_2017]
- [Shechtman 1981][research_shechtman_1981]
- [Sheeba et al 2025][research_sheeba_lingeshwari_2025]
- [Sheldon 1967][research_sheldon_1967]
- [Shen 2017][research_shen_2017]
- [Shen and Wen 2018][research_shen_wen_2018]
- [Sheng et al 2020][research_sheng_chen_2020]
- [Sheng et al 2023][research_sheng_chen_2023]
- [Shi 2025][research_shi_2025]
- [Shi et al 2018][research_shi_chang_2018]
- [Shi et al 2018][research_shi_tan_2018]
- [Shi et al 2019][research_shi_chang_2019]
- [Shi et al 2019][research_shi_chang_2019_b]
- [Shi-feng et al 2018][research_shifeng_jiamin_2018]
- [Shimabukuro et al 1982][research_shimabukuro_welge_1982]
- [Shimabukuro, K. M. et al 1979][research_shimabukurokm_welgehr_1979]
- [Shimada and Ohwada 2020][research_shimada_ohwada_2020]
- [Shimomura et al 2025][research_shimomura_park_2025]
- [Shindo, S. and Joppa, R. G. 1980][research_shindos_jopparg_1980]
- [Shinozaki et al 2017][research_shinozaki_suzuki_2017]
- [Shiriaev et al 2026][research_shiriaev_freidovich_2026]
- [Shirinzadeh Dastgiri et al 2023][research_shirinzadehdastgiri_fuerth_2023]
- [Shiryaev et al 2026][research_shiryaev_milenin_2026]
- [Shivers, J. P. et al 1975][research_shiversjp_mclemorehc_1975]
- [Shkaraputa 1976][research_shkaraputa_1976]
- [Shoshany‐Tavory et al 2023][research_shoshanytavory_peleg_2023]
- [Shu et al 2025][research_shu_gao_2025]
- [Shufan et al 2018][research_shufan_heng_2018]
- [Shulman et al 1966][research_shulman_parry_1966]
- [Si et al 2019][research_si_huang_2019]
- [Siedlak et al 2017][research_siedlak_pinon_2017]
- [Sikora 2020][research_sikora_2020]
- [Silva et al 2021][research_silva_resende_2021]
- [Silverstein, Abe and White, James A 1937][research_silversteinabe_whitejamesa_1937]
- [Simonelli et al 2023][research_simonelli_zou_2023]
- [Simpson 1971][research_simpson_1971]
- [Sinaiskii et al 1972][research_sinaiskii_pogrebnyak_1972]
- [Singh 2018][research_singh_2018]
- [Singh and Dwivedi 2022][research_singh_dwivedi_2022]
- [Singh et al 2016][research_singh_sharma_2016]
- [Singh et al 2020][research_singh_priyadarshi_2020]
- [Singh et al 2026][research_singh_borras_2026]
- [Sinha et al 2026][research_sinha_singh_2026]
- [Sissingh 1951][research_sissingh_1951]
- [Sitaram et al 2023][research_sitaram_govardhan_2023]
- [Sivaramakrishnan 1981][research_sivaramakrishnan_1981]
- [Sivo, Joseph N 1957][research_sivojosephn_1957]
- [Sizemore and Jr 1973][research_sizemore_jr_1973]
- [Sklyarov et al 2022][research_sklyarov_vartazarova_2022]
- [Skoog, Richard B 1951][research_skoogrichardb_1951]
- [Skow et al 1982][research_skow_moore_1982]
- [Skyrius and Valentukevičė 2020][research_skyrius_valentukevice_2020]
- [Slater, John W. 2011][research_slaterjohnw_2011]
- [Slater, John W. 2014][research_slaterjohnw_2014]
- [Slater, John W. 2015][research_slaterjohnw_2015]
- [Slater, John W. 2016][research_slaterjohnw_2016]
- [Slater, John W. 2017][research_slaterjohnw_2017]
- [Sleeman, William C. and Byrnes, Andrew L. 1953][research_sleemanwilliamc_byrnesandrewl_1953]
- [Sleeman, William C., Jr. 1957][research_sleemanwilliamcjr_1957]
- [Sleeman, William C., Jr. 1961][research_sleemanwilliamcjr_1961]
- [Smaili et al 2018][research_smaili_rouwhorst_2018]
- [Smart, Michael K. et al 1994][research_smartmichaelk_kalkhoranirajm_1994]
- [Smeltzer, D. B. and Sorensen, N. E. 1972][research_smeltzerdb_sorensenne_1972]
- [Smith 1967][research_smith_1967]
- [Smith 2021][research_smith_2021]
- [Smith et al 1973][research_smith_lebacqz_1973]
- [Smith et al 1979][research_smith_yamakawa_1979]
- [Smith, P. M. 1978][research_smithpm_1978]
- [Smith, Williard G. 1954][research_smithwilliardg_1954]
- [Smits and Miles 2002][research_smits_miles_2002]
- [Smooth Particle Hydrodynamics Birdstrike 2021][research_smooth_particle_2021]
- [Snodgrass 1955][research_snodgrass_1955]
- [Snyder, F. S. et al 1977][research_snyderfs_voorheescg_1977]
- [Soeder, R. H. and Bobula, G. A. 1979][research_soederrh_bobulaga_1979]
- [Soeder, R. H. and Bobula, G. A. 1979][research_soederrh_bobulaga_1979_b]
- [Soeder, R. H. and Bobula, G. A. 1982][research_soederrh_bobulaga_1982]
- [Soeder, R. H. and Mehalic, C. M. 1984][research_soederrh_mehaliccm_1984]
- [Sokolov and Karpati 1978][research_sokolov_karpati_1978]
- [Solomon, George E 1955][research_solomongeorgee_1955]
- [Soltani and Askari 2019][research_soltani_askari_2019]
- [Soltani et al 2015][research_soltani_younsi_2015]
- [Soltani et al 2016][research_soltani_daliri_2016]
- [Soltanov 1977][research_soltanov_1977]
- [Soltanov 1982][research_soltanov_1982]
- [Song et al 2019][research_song_zhang_2019]
- [Sorensen and Bencze 1974][research_sorensen_bencze_1974]
- [Sorensen and Latham 1975][research_sorensen_latham_1975]
- [Sorensen et al 1969][research_sorensen_smeltzer_1969]
- [Sorensen et al 1973][research_sorensen_smeltzer_1973]
- [Sorensen, N. E. and Bencze, D. P. 1973][research_sorensenne_benczedp_1973]
- [Sosnin and Torshenov 1970][research_sosnin_torshenov_1970]
- [Sousa et al 2017][research_sousa_paniagua_2017]
- [Sovran 1959][research_sovran_1959]
- [Sowter 1973][research_sowter_1973]
- [Spearman, M. L. and Sawyer, W. C. 1977][research_spearmanml_sawyerwc_1977]
- [Spencer, Bernard, Jr. 1961][research_spencerbernardjr_1961]
- [Spivey et al 2021][research_spivey_ortiz_2021]
- [Spooner, Stanley H and Martina, Albert P 1948][research_spoonerstanleyh_martinaalbertp_1948]
- [Spreemann, Kenneth P 1958][research_spreemannkennethp_1958]
- [Spreiter and Sacks 1951][research_spreiter_sacks_1951]
- [Squires 2002][research_squires_2002]
- [Sreekumar et al 2025][research_sreekumar_vamsikrishna_2025]
- [Sreenivasan et al 2023][research_sreenivasan_ma_2023]
- [Stamatelos and Labeas 2025][research_stamatelos_labeas_2025]
- [Stancil 1979][research_stancil_1979]
- [Stanišić 1961][research_stanisic_1961]
- [Starken and Lichtfuss 1970][research_starken_lichtfuss_1970]
- [Steenken, W. G. et al 1999][research_steenkenwg_williamsjg_1999]
- [Stefanovic and Livne 2021][research_stefanovic_livne_2021]
- [Stenning 1980][research_stenning_1980]
- [Stenning 1980][research_stenning_1980_b]
- [Stephan et al 2017][research_stephan_schrall_2017]
- [Stephan et al 2024][research_stephan_heyen_2024]
- [Stephens, Emily W. 1959][research_stephensemilyw_1959]
- [Stephenson 1953][research_stephenson_1953]
- [Stephenson 1958][research_stephenson_1958]
- [Stephenson and Shohet 1967][research_stephenson_shohet_1967]
- [Sterbentz, William H. and Davids, Joseph 1952][research_sterbentzwilliamh_davidsjoseph_1952]
- [Stewart 1956][research_stewart_1956]
- [Stewart et al 1975][research_stewart_dominick_1975]
- [Stewart et al 2011][research_stewart_bull_2011]
- [Stewartson 1950][research_stewartson_1950]
- [Stickley and Brownhill 1964][research_stickley_brownhill_1964]
- [Stocker 1951][research_stocker_1951]
- [Straight, D. M. and Harrington, D. E. 1973][research_straightdm_harringtonde_1973]
- [Strawn and Kobayashi 1984][research_strawn_kobayashi_1984]
- [Strawn and Kobayashi 1984][research_strawn_kobayashi_1984_b]
- [Stroh and Sediako 2023][research_stroh_sediako_2023]
- [Strub and Suter 1965][research_strub_suter_1965]
- [Stuart 1982][research_stuart_1982]
- [Study on the Effect 2022][research_study_on_2022]
- [Sturek et al 1983][research_sturek_kayser_1983]
- [Sturek et al 1983][research_sturek_kayser_1983_b]
- [Stutz and Price 1964][research_stutz_price_1964]
- [Su and Young 2017][research_su_young_2017]
- [Su et al 2019][research_su_zhang_2019]
- [Su et al 2021][research_su_hwu_2021]
- [Subramanian and DeLaurentis 2016][research_subramanian_delaurentis_2016]
- [Sugiyama 1971][research_sugiyama_1971]
- [Sugiyama 1971][research_sugiyama_1971_b]
- [Sugiyama 1977][research_sugiyama_1977]
- [Sui et al 2025][research_sui_lu_2025]
- [Sullivan 1943][research_sullivan_1943]
- [Sullivan, P. G. 1978][research_sullivanpg_1978]
- [Sullivan, R. L. 1979][research_sullivanrl_1979]
- [Sumadireja et al 2025][research_sumadireja_dachyar_2025]
- [Sun 2024][research_sun_2024]
- [Sun and Smith 2019][research_sun_smith_2019]
- [Sun and Smith 2022][research_sun_smith_2022]
- [Sun and Zhang 2016][research_sun_zhang_2016]
- [Sun and Zhu 2019][research_sun_zhu_2019]
- [Sun et al 2015][research_sun_miao_2015]
- [Sun et al 2015][research_sun_nie_2015]
- [Sun et al 2016][research_sun_li_2016]
- [Sun et al 2020][research_sun_yang_2020]
- [Sun et al 2021][research_sun_gu_2021]
- [Sun et al 2021][research_sun_li_2021]
- [Sun et al 2021][research_sun_li_2021_b]
- [Sun et al 2022][research_sun_guo_2022]
- [Sun et al 2022][research_sun_li_2022]
- [Sun et al 2024][research_sun_gu_2024]
- [Sun et al 2024][research_sun_gu_2024_b]
- [Sun et al 2024][research_sun_hu_2024]
- [Sun et al 2024][research_sun_ju_2024]
- [Sun et al 2024][research_sun_yang_2024]
- [Sun et al 2024][research_sun_zhang_2024]
- [Sun et al 2025][research_sun_shen_2025]
- [Sun et al 2025][research_sun_yang_2025]
- [Sun et al 2025][research_sun_yu_2025]
- [Sun et al 2025][research_sun_zheng_2025]
- [Sun et al 2026][research_sun_chen_2026]
- [Sun et al 2026][research_sun_ding_2026]
- [Surber and Sedlock 1979][research_surber_sedlock_1979]
- [Suresh and Patri 2017][research_suresh_patri_2017]
- [Suresh et al 2021][research_suresh_nirmal_2021]
- [Surwase and Kumar 2025][research_surwase_kumar_2025]
- [Sussman 1968][research_sussman_1968]
- [Sutton, Fred B. 1959][research_suttonfredb_1959]
- [Suzuki et al 2020][research_suzuki_suzuki_2020]
- [Sweep Optimization to Reduce 2024][research_sweep_optimization_2024]
- [Syberg and Koncsek 1976][research_syberg_koncsek_1976]
- [Syberg, J. and Koncsek, J. L. 1972][research_sybergj_koncsekjl_1972]
- [Szrama 2019][research_szrama_2019]
- [Szrama and Lodygowski 2024][research_szrama_lodygowski_2024]
- [Szusta 2018][research_szusta_2018]
- [Sélim et al 2023][research_selim_liscouethanke_2023]
- [Sóbester 2021][research_sobester_2021]
- [Tadini et al 2017][research_tadini_grange_2017]
- [Taggart 1966][research_taggart_1966]
- [Taghavi-Zenouz and Ababaf Behbaha 2017][research_taghavizenouz_ababafbehbaha_2017]
- [Taghi-Abad et al 2026][research_taghiabad_esfandabadi_2026]
- [Taguchi et al 2017][research_taguchi_mori_2017]
- [Tahmasebi and Karimi M. 2015][research_tahmasebi_karimim_2015]
- [Tahsini 2020][research_tahsini_2020]
- [Taig 1961][research_taig_1961]
- [Takahashi 2017][research_takahashi_2017]
- [Takahashi et al 2018][research_takahashi_koike_2018]
- [Takovitsky 2018][research_takovitsky_2018]
- [Tamboli 1956][research_tamboli_1956]
- [Tan et al 2018][research_tan_sun_2018]
- [Tan, Choon-Sooi and Suder, Kenneth 2003][research_tanchoonsooi_suderkenneth_2003]
- [Tanaka and Murata 1975][research_tanaka_murata_1975]
- [Tanaka and Murata 1975][research_tanaka_murata_1975_b]
- [Tanaka and Murata 1975][research_tanaka_murata_1975_c]
- [Tanaka and Nojima 1971][research_tanaka_nojima_1971]
- [Taneich and Rinoie 2025][research_taneich_rinoie_2025]
- [Tang 1969][research_tang_1969]
- [Tang and Owen 2021][research_tang_owen_2021]
- [Tang et al 2024][research_tang_xu_2024]
- [Tang et al 2025][research_tang_cai_2025]
- [Tang et al 2025][research_tang_cai_2025_b]
- [Tang et al 2025][research_tang_li_2025]
- [Tanguy et al 2018][research_tanguy_macmanus_2018]
- [Tani 1978][research_tani_1978]
- [Tanida 1972][research_tanida_1972]
- [Tanner, Carole S. and McLeod, Norman J. 1965][research_tannercaroles_mcleodnormanj_1965]
- [Tao and Sun 2019][research_tao_sun_2019]
- [Tao et al 2018][research_tao_zhao_2018]
- [Tao et al 2020][research_tao_sun_2020]
- [Tao et al 2022][research_tao_jin_2022]
- [Tao et al 2024][research_tao_wang_2024]
- [Tarnowski et al 2021][research_tarnowski_borowski_2021]
- [Tate and Gillard 1975][research_tate_gillard_1975]
- [Taufik Budi Cahyana et al 2023][research_taufikbudicahyana_achmadwardana_2023]
- [Taylor 1968][research_taylor_1968]
- [Taylor, John G. 1991][research_taylorjohng_1991]
- [Telemaco et al 2020][research_telemaco_oliveira_2020]
- [Tesch, W. A. and Steenken, W. G. 1978][research_teschwa_steenkenwg_1978]
- [Teske and Thistle 2018][research_teske_thistle_2018]
- [Tewfik and Giedt 1960][research_tewfik_giedt_1960]
- [Tfaily et al 2024][research_tfaily_diouane_2024]
- [Tfaily et al 2026][research_tfaily_bartoli_2026]
- [Thang 2016][research_thang_2016]
- [Thankachan 2025][research_thankachan_2025]
- [Thapa et al 2025][research_thapa_li_2025]
- [The Fiat G80 Turbojet 1952][research_the_fiat_1952]
- [The influence of the 1975][research_the_influence_1975]
- [The Reason and Strategy 2021][research_the_reason_2021]
- [The Rolls‐Royce RB.211 Three 1968][research_the_rollsroyce_1968]
- [The Rolls‐Royce Spey Junior 1967][research_the_rollsroyce_1967]
- [Thein 2018][research_thein_2018]
- [Theodorsen 1959][research_theodorsen_1959]
- [Thomas 1965][research_thomas_1965]
- [Thomas and Srinivasan 1974][research_thomas_srinivasan_1974]
- [Thomas, Randy and Stueber, Thomas J. 2013][research_thomasrandy_stueberthomasj_2013]
- [Thompson 2022][research_thompson_2022]
- [Thompson, Robert F. et al 1959][research_thompsonrobertf_voglerraymondd_1959]
- [THRUST VECTORING OF A 2020][research_thrust_vectoring_2020]
- [Tian and Li 2020][research_tian_li_2020]
- [Tian et al 2021][research_tian_shunke_2021]
- [Ting et al 2018][research_ting_chaparro_2018]
- [Tirpak 1985][research_tirpak_1985]
- [Titanium or titanium alloy 1974][research_titanium_or_1974]
- [Tkalenko 1969][research_tkalenko_1969]
- [Todorov et al 2023][research_todorov_rakov_2023]
- [Toffol and Ricci 2023][research_toffol_ricci_2023]
- [Toll, Thomas A 1942][research_tollthomasa_1942]
- [Tomczyk and Seweryn 2017][research_tomczyk_seweryn_2017]
- [Tomczyk and Seweryn 2021][research_tomczyk_seweryn_2021]
- [Tondl 1979][research_tondl_1979]
- [Tongguang et al 2015][research_tongguang_changhui_2015]
- [Torenbeek 1971][research_torenbeek_1971]
- [Torgerson et al 2019][research_torgerson_mantri_2019]
- [Torić et al 2017][research_toric_brnic_2017]
- [Torić et al 2018][research_toric_glavinic_2018]
- [Torić et al 2020][research_toric_boko_2020]
- [Townsend and Blatt 1976][research_townsend_blatt_1976]
- [Tran and Read 2022][research_tran_read_2022]
- [Trapp 1952][research_trapp_1952]
- [Traub 2016][research_traub_2016]
- [Trefny, C. J. and Benson, T. J. 1995][research_trefnycj_bensontj_1995]
- [Trefny, C. J. and Wasserbauer, J. W. 1986][research_trefnycj_wasserbauerjw_1986]
- [Trivers et al 2020][research_trivers_carrick_2020]
- [Tudosie 2017][research_tudosie_2017]
- [Tudosie 2017][research_tudosie_2017_b]
- [Tudosie 2018][research_tudosie_2018]
- [Tudosie and Păunescu 2017][research_tudosie_paunescu_2017]
- [Tudosie et al 2019][research_tudosie_dumitru_2019]
- [Tugrul et al 2022][research_tugrul_akgul_2022]
- [Tuninetti et al 2024][research_tuninetti_sepulveda_2024]
- [Turan 2015][research_turan_2015]
- [Turan 2022][research_turan_2022]
- [Turan 2022][research_turan_2022_b]
- [Turbofan Engine Performance under 2017][research_turbofan_engine_2017]
- [Tyan et al 2017][research_tyan_nguyen_2017]
- [Türkkahraman et al 2024][research_turkkahraman_ozcan_2024]
- [Uddin and Gravdahl 2016][research_uddin_gravdahl_2016]
- [Udroiu and Blaj 2016][research_udroiu_blaj_2016]
- [Ueda and Tanaka 1975][research_ueda_tanaka_1975]
- [Ueda and Tanaka 1976][research_ueda_tanaka_1976]
- [Ueda and Tanaka 1977][research_ueda_tanaka_1977]
- [Ueki et al 2020][research_ueki_yasuda_2020]
- [Uemura et al 2020][research_uemura_kamata_2020]
- [Uglov et al 2016][research_uglov_kuleshov_2016]
- [Ukai et al 2020][research_ukai_kato_2020]
- [Uludag and Turan 2015][research_uludag_turan_2015]
- [Um 2016][research_um_2016]
- [URANS Simulation of Self-Recirculation 2024][research_urans_simulation_2024]
- [Urionabarrenetxea et al 2022][research_urionabarrenetxea_martin_2022]
- [Using Tip Injection to 2022][research_using_tip_2022]
- [Uthgenannt 1971][research_uthgenannt_1971]
- [Utomo and Bura 2019][research_utomo_bura_2019]
- [Uzun 2025][research_uzun_2025]
- [Vaca-Rios and Cerón-Muñoz 2025][research_vacarios_ceronmunoz_2025]
- [Vaisakh et al 2019][research_vaisakh_namratha_2019]
- [Valencia et al 2017][research_valencia_hidalgo_2017]
- [Valencia et al 2020][research_valencia_alulema_2020]
- [Valensi 1958][research_valensi_1958]
- [Valoppi et al 2017][research_valoppi_bruschi_2017]
- [van Arnhem et al 2022][research_vanarnhem_devries_2022]
- [Van Deusen and Mardoc 1972][research_vandeusen_mardoc_1972]
- [Van Dommelen 1995][research_vandommelen_1995]
- [van Rooyen and Eshelby 1981][research_vanrooyen_eshelby_1981]
- [Vance F. Dippold III 2022][research_vancefdippoldiii_2022]
- [Vandervelden, Alexander J. M. and Kroo, Ilan 1990][research_vanderveldenalexanderjm_krooilan_1990]
- [VanSchalkwyk, Christian et al 2001][research_vanschalkwykchristian_brightmichellem_2001]
- [Vasil'ev 1970][research_vasilev_1970]
- [Vazsonyi 1950][research_vazsonyi_1950]
- [Veeresh Kumar et al 2021][research_veereshkumar_nagasailaja_2021]
- [Venturelli and Benini 2016][research_venturelli_benini_2016]
- [Veresnikov 2025][research_veresnikov_2025]
- [Veresnikov et al 2026][research_veresnikov_goncharenko_2026]
- [Verlaine 2023][research_verlaine_2023]
- [Verma 2018][research_verma_2018]
- [Verma and Kulkarni 2024][research_verma_kulkarni_2024]
- [Verma and Manisankar 2025][research_verma_manisankar_2025]
- [Verma et al 2020][research_verma_singh_2020]
- [Victor Antonio and Yan 2023][research_victorantonio_yan_2023]
- [Vidal 1962][research_vidal_1962]
- [Vidal 1963][research_vidal_1963]
- [Vieira et al 2020][research_vieira_koch_2020]
- [Vijayakumar et al 2015][research_vijayakumar_senthilvelan_2015]
- [Vinodh and Aravindraj 2015][research_vinodh_aravindraj_2015]
- [Vinogradov et al 2017][research_vinogradov_makarov_2017]
- [Vinogradov et al 2017][research_vinogradov_melnikov_2017]
- [Vira, N. R. and Fan, D.-N. 1982][research_viranr_fandn_1982]
- [Vlasov 2022][research_vlasov_2022]
- [Vlasov et al 2021][research_vlasov_gomorova_2021]
- [Vodolazskiy et al 2017][research_vodolazskiy_zhloba_2017]
- [Volkov 2024][research_volkov_2024]
- [von Doenhoff, Albert E. and Horton, Elmer A. 1942][research_vondoenhoffalberte_hortonelmera_1942]
- [Von Glahn, U. et al 1972][research_vonglahnu_reshotkom_1972]
- [von Hlatky and Rice 2018][research_vonhlatky_rice_2018]
- [Vorob'ev and Bich 1977][research_vorobev_bich_1977]
- [Vorob’ev and Galiakhmetov 2023][research_vorobev_galiakhmetov_2023]
- [Voronin S. T. 2022][research_voroninst_2022]
- [Vos et al 2017][research_vos_wortmann_2017]
- [Voß 2019][research_voss_2019]
- [Vu et al 2025][research_vu_nguyen_2025]
- [Véras et al 2021][research_veras_balarac_2021]
- [Wabick et al 2023][research_wabick_johnson_2023]
- [Wacker 1967][research_wacker_1967]
- [Wahler et al 2025][research_wahler_maruyama_2025]
- [Walker 1952][research_walker_1952]
- [Walker 1955][research_walker_1955]
- [Walker et al 1980][research_walker_heming_1980]
- [Walker, Harold J and Berggren, Robert E 1948][research_walkerharoldj_berggrenroberte_1948]
- [Wall et al 2017][research_wall_mckinley_2017]
- [Wallner, L. E. et al 1955][research_wallnerle_lubickrj_1955]
- [Wallner, Lewis E. et al 1954][research_wallnerlewise_lubickrobertj_1954]
- [Wamsley 1976][research_wamsley_1976]
- [Wandini et al 2016][research_wandini_mulyanto_2016]
- [Wang 2020][research_wang_2020]
- [Wang and Chen 2025][research_wang_chen_2025]
- [Wang and Feng 2025][research_wang_feng_2025]
- [Wang and Khan 2015][research_wang_khan_2015]
- [Wang and Li 2023][research_wang_li_2023]
- [Wang et al 2015][research_wang_tian_2015]
- [Wang et al 2016][research_wang_li_2016]
- [Wang et al 2017][research_wang_guo_2017]
- [Wang et al 2018][research_wang_liu_2018]
- [Wang et al 2019][research_wang_yuan_2019]
- [Wang et al 2020][research_wang_hu_2020]
- [Wang et al 2020][research_wang_li_2020]
- [Wang et al 2020][research_wang_lu_2020]
- [Wang et al 2020][research_wang_shi_2020]
- [Wang et al 2020][research_wang_sun_2020]
- [Wang et al 2020][research_wang_tang_2020]
- [Wang et al 2020][research_wang_wang_2020]
- [Wang et al 2021][research_wang_hu_2021]
- [Wang et al 2021][research_wang_hu_2021_b]
- [Wang et al 2021][research_wang_tian_2021]
- [Wang et al 2021][research_wang_zhao_2021]
- [Wang et al 2022][research_wang_fan_2022]
- [Wang et al 2022][research_wang_song_2022]
- [Wang et al 2022][research_wang_wang_2022]
- [Wang et al 2022][research_wang_zhao_2022]
- [Wang et al 2023][research_wang_gao_2023]
- [Wang et al 2023][research_wang_pan_2023]
- [Wang et al 2023][research_wang_peng_2023]
- [Wang et al 2023][research_wang_sun_2023]
- [Wang et al 2023][research_wang_sun_2023_b]
- [Wang et al 2023][research_wang_wang_2023]
- [Wang et al 2023][research_wang_wang_2023_b]
- [Wang et al 2023][research_wang_wang_2023_c]
- [Wang et al 2023][research_wang_xu_2023]
- [Wang et al 2023][research_wang_zhao_2023]
- [Wang et al 2023][research_wang_zhao_2023_b]
- [Wang et al 2024][research_wang_fan_2024]
- [Wang et al 2024][research_wang_fang_2024]
- [Wang et al 2024][research_wang_he_2024]
- [Wang et al 2024][research_wang_liu_2024]
- [Wang et al 2024][research_wang_pan_2024]
- [Wang et al 2024][research_wang_song_2024]
- [Wang et al 2024][research_wang_tu_2024]
- [Wang et al 2024][research_wang_wang_2024]
- [Wang et al 2024][research_wang_zhou_2024]
- [Wang et al 2025][research_wang_chen_2025_b]
- [Wang et al 2025][research_wang_he_2025]
- [Wang et al 2025][research_wang_huo_2025]
- [Wang et al 2025][research_wang_li_2025]
- [Wang et al 2025][research_wang_liu_2025]
- [Wang et al 2025][research_wang_tang_2025]
- [Wang et al 2025][research_wang_zhang_2025]
- [Wang et al 2025][research_wang_zhao_2025]
- [Wang et al 2025][research_wang_zhao_2025_b]
- [Wang et al 2026][research_wang_guan_2026]
- [Wang et al 2026][research_wang_zhang_2026]
- [Wang et al 2026][research_wang_zhao_2026]
- [Ward 1949][research_ward_1949]
- [Wardana et al 2022][research_wardana_cahyana_2022]
- [Warren and Chen 1973][research_warren_chen_1973]
- [Warsch et al 2026][research_warsch_carbone_2026]
- [Washington and Humphrey 1969][research_washington_humphrey_1969]
- [Washington et al 1968][research_washington_pettis_1968]
- [Wasserbauer, J. F. and Gerstenmaier, W. H. 1978][research_wasserbauerjf_gerstenmaierwh_1978]
- [Wasserbauer, J. F. et al 1985][research_wasserbauerjf_neumannhe_1985]
- [Wasserman and Mitchell 1973][research_wasserman_mitchell_1973]
- [Watanabe et al 2023][research_watanabe_sunada_2023]
- [Watkins 2019][research_watkins_2019]
- [Watson 1966][research_watson_1966]
- [Watson, Earl C 1953][research_watsonearlc_1953]
- [Wauchop 1997][research_wauchop_1997]
- [Weed 2002][research_weed_2002]
- [Wegener 1977][research_wegener_1977]
- [Wei et al 2022][research_wei_qu_2022]
- [Weiberg, James A. and Holzhauser, Curt A. 1961][research_weibergjamesa_holzhausercurta_1961]
- [Weinert et al 2022][research_weinert_underhill_2022]
- [Weissman 1973][research_weissman_1973]
- [Wells 1993][research_wells_1993]
- [Welna et al 1969][research_welna_dahlberg_1969]
- [Wen et al 2020][research_wen_tang_2020]
- [Wen et al 2022][research_wen_kong_2022]
- [Wenzel 2015][research_wenzel_2015]
- [Werner, Roger A. and Wolter, John D. 2010][research_wernerrogera_wolterjohnd_2010]
- [Westin et al 2023][research_westin_balthazar_2023]
- [Wetzel, Benton E 1955][research_wetzelbentone_1955]
- [Whalen, Paul P and Wilcox, Fred A 1956][research_whalenpaulp_wilcoxfreda_1956]
- [Whalley, Matthew S. 1991][research_whalleymatthews_1991]
- [Wharton et al 1973][research_wharton_waterhouse_1973]
- [Whitaker and Rediess 1970][research_whitaker_rediess_1970]
- [Whitbeck and Hofmann 1978][research_whitbeck_hofmann_1978]
- [Whitcomb, Richard T. 1953][research_whitcombrichardt_1953]
- [Whitcomb, Richard T. and Sevier, John R., Jr. 1960][research_whitcombrichardt_sevierjohnrjr_1960]
- [White 1997][research_white_1997]
- [Whitney 1963][research_whitney_1963]
- [Whitney and Skinner 2024][research_whitney_skinner_2024]
- [Whitson et al 1950][research_whitson_bartimo_1950]
- [Whittley 1952][research_whittley_1952]
- [Whoric 1973][research_whoric_1973]
- [Whoric 1977][research_whoric_1977]
- [Wickert 1985][research_wickert_1985]
- [Wide-angle lens distortion influence 2025][research_wide_angle_lens_2025]
- [Wilcox, Fred A 1957][research_wilcoxfreda_1957]
- [Wilde and Pickerell 1968][research_wilde_pickerell_1968]
- [Wilkinson 1971][research_wilkinson_1971]
- [Williams and Butler 1963][research_williams_butler_1963]
- [Williams and Yost 1973][research_williams_yost_1973]
- [Willis 1981][research_willis_1981]
- [Wilson et al 1993][research_wilson_riley_1993]
- [Wilson et al 2019][research_wilson_saintier_2019]
- [Wilson et al 2023][research_wilson_figliola_2023]
- [Winkler 1954][research_winkler_1954]
- [Winograd and Miles 1956][research_winograd_miles_1956]
- [Winternitz and Ramsay 1957][research_winternitz_ramsay_1957]
- [Wisniewski 1951][research_wisniewski_1951]
- [Witkowska et al 2024][research_witkowska_borowski_2024]
- [Wong et al 2017][research_wong_ryan_2017]
- [Wood, R. M. and Miller, D. S. 1985][research_woodrm_millerds_1985]
- [Wood, R. M. and Miller, D. S. 1985][research_woodrm_millerds_1985_b]
- [Wood, R. M. et al 1983][research_woodrm_millerds_1983]
- [Woods and Friswell 2015][research_woods_friswell_2015]
- [Woodward 1956][research_woodward_1956]
- [Woodward 1979][research_woodward_1979]
- [Wren 2026][research_wren_2026]
- [Wright et al 1978][research_wright_bruckman_1978]
- [Wu 2021][research_wu_2021]
- [Wu et al 2019][research_wu_wu_2019]
- [Wu et al 2021][research_wu_qiu_2021]
- [Wu et al 2022][research_wu_zhao_2022]
- [Wu et al 2023][research_wu_gao_2023]
- [Wu et al 2024][research_wu_li_2024]
- [Wu et al 2024][research_wu_li_2024_b]
- [Wu et al 2024][research_wu_yang_2024]
- [Wu et al 2025][research_wu_cao_2025]
- [Wu et al 2025][research_wu_wang_2025]
- [Wu et al 2026][research_wu_du_2026]
- [Wu Li and Karl Geiselhart 2020][research_wuli_karlgeiselhart_2020]
- [Wu Li et al 2025][research_wuli_karlgeiselhart_2025]
- [Wunderlich et al 2021][research_wunderlich_dahne_2021]
- [Xiao et al 2023][research_xiao_jin_2023]
- [Xiao et al 2025][research_xiao_meng_2025]
- [Xiaokang et al 2018][research_xiaokang_kuaishe_2018]
- [Xie and Marrani 2021][research_xie_marrani_2021]
- [Xie et al 2016][research_xie_zhang_2016]
- [Xie et al 2020][research_xie_yang_2020]
- [Xie et al 2023][research_xie_zhu_2023]
- [Xie et al 2025][research_xie_liu_2025]
- [Xie et al 2025][research_xie_ye_2025]
- [Xie et al 2025][research_xie_ye_2025_b]
- [Xie et al 2026][research_xie_cai_2026]
- [Xin-guo et al 2015][research_xinguo_xing_2015]
- [Xinqian and Anxiong 2015][research_xinqian_anxiong_2015]
- [Xu 2023][research_xu_2023]
- [Xu and Hu 2022][research_xu_hu_2022_b]
- [Xu and Yu 2025][research_xu_yu_2025]
- [Xu and Zhou 2015][research_xu_zhou_2015]
- [Xu et al 2016][research_xu_chen_2016]
- [Xu et al 2020][research_xu_cheng_2020]
- [Xu et al 2021][research_xu_hu_2021]
- [Xu et al 2022][research_xu_hu_2022]
- [Xu et al 2023][research_xu_hu_2023]
- [Xu et al 2024][research_xu_gu_2024]
- [Xu et al 2025][research_xu_wu_2025]
- [Xu et al 2026][research_xu_zhang_2026]
- [Xue et al 2017][research_xue_li_2017]
- [Xue et al 2020][research_xue_li_2020]
- [Xue et al 2024][research_xue_wang_2024]
- [Yadav and Guven 2015][research_yadav_guven_2015]
- [Yadav et al 2018][research_yadav_bodavula_2018]
- [Yagn and Kal'ko 1972][research_yagn_kalko_1972]
- [Yahiaoui 2024][research_yahiaoui_2024]
- [Yalcin 2017][research_yalcin_2017]
- [Yamada et al 2024][research_yamada_himeno_2024]
- [Yamaguchi 1964][research_yamaguchi_1964]
- [Yamamoto et al 2020][research_yamamoto_kojima_2020]
- [Yamanaka and Kamimura 1975][research_yamanaka_kamimura_1975]
- [Yamazaki et al 2019][research_yamazaki_mizobata_2019]
- [Yan and Zhang 2023][research_yan_zhang_2023]
- [Yan et al 2016][research_yan_chen_2016]
- [Yan et al 2024][research_yan_qian_2024]
- [Yan et al 2025][research_yan_pan_2025]
- [Yang 2018][research_yang_2018]
- [Yang and Liu 2017][research_yang_liu_2017]
- [Yang and Yu 2026][research_yang_yu_2026]
- [Yang et al 2019][research_yang_liu_2019]
- [Yang et al 2020][research_yang_zhang_2020]
- [Yang et al 2020][research_yang_zhou_2020]
- [Yang et al 2021][research_yang_ji_2021]
- [Yang et al 2021][research_yang_li_2021]
- [Yang et al 2021][research_yang_lu_2021]
- [Yang et al 2021][research_yang_tian_2021]
- [Yang et al 2022][research_yang_liang_2022]
- [Yang et al 2022][research_yang_lu_2022]
- [Yang et al 2022][research_yang_wu_2022]
- [Yang et al 2023][research_yang_li_2023]
- [Yang et al 2023][research_yang_zhang_2023]
- [Yang et al 2024][research_yang_li_2024_b]
- [Yang et al 2024][research_yang_nikolaidis_2024]
- [Yang et al 2025][research_yang_wan_2025]
- [Yang et al 2025][research_yang_wang_2025]
- [Yang et al 2026][research_yang_kong_2026]
- [Yang et al 2026][research_yang_li_2026]
- [Yang et al 2026][research_yang_qi_2026]
- [Yano et al 2018][research_yano_okada_2018]
- [Yao et al 2017][research_yao_zhang_2017]
- [Yao et al 2017][research_yao_zhou_2017]
- [Yao et al 2022][research_yao_zhang_2022]
- [Yaylak et al 2026][research_yaylak_pinarbasi_2026]
- [Ye et al 2026][research_ye_chuai_2026]
- [Yeh 1959][research_yeh_1959]
- [Yeh et al 2022][research_yeh_du_2022]
- [Yeom et al 2015][research_yeom_sung_2015]
- [Yeranee et al 2023][research_yeranee_rao_2023]
- [Yi 2023][research_yi_2023]
- [Yi and Sun 2024][research_yi_sun_2024]
- [Yoder 2006][research_yoder_2006]
- [Yonke, William A. et al 1995][research_yonkewilliama_robbendaniell_1995]
- [Yoon et al 2019][research_yoon_xiao_2019]
- [Yoon et al 2022][research_yoon_lee_2022]
- [York et al 2018][research_york_ozturk_2018]
- [You et al 2016][research_you_yu_2016]
- [Yu et al 2021][research_yu_ni_2021]
- [Yu et al 2023][research_yu_xu_2023]
- [Yu et al 2025][research_yu_guo_2025]
- [Yu et al 2025][research_yu_wang_2025]
- [Yu et al 2026][research_yu_yu_2026]
- [Yu et al 2026][research_yu_zhao_2026]
- [Yuan et al 2016][research_yuan_shi_2016]
- [Yuan et al 2021][research_yuan_dai_2021]
- [Yuan et al 2021][research_yuan_zhang_2021]
- [Yuan et al 2023][research_yuan_li_2023]
- [Yuan et al 2026][research_yuan_lu_2026]
- [Yue et al 2017][research_yue_wen_2017]
- [Yuhara et al 2016][research_yuhara_makino_2016]
- [Yuhas, Andrew J. and Ray, Ronald J. 1992][research_yuhasandrewj_rayronaldj_1992]
- [Yuhas, Andrew J. and Ray, Ronald J. 1992][research_yuhasandrewj_rayronaldj_1992_b]
- [Yusof and Rahim 2017][research_yusof_rahim_2017]
- [Zachos et al 2016][research_zachos_macmanus_2016]
- [Zahir et al 2023][research_zahir_aamer_2023]
- [Zaleski et al 2021][research_zaleski_stefaniak_2021]
- [Zaman et al 2025][research_zaman_korth_2025]
- [Zarchi and Attaran 2018][research_zarchi_attaran_2018]
- [Zebbiche and Youbi 2023][research_zebbiche_youbi_2023]
- [Zeng and Buckley 2023][research_zeng_buckley_2023]
- [Zeng and Chen 2015][research_zeng_chen_2015]
- [Zeng et al 2017][research_zeng_oliveira_2017]
- [Zeng et al 2022][research_zeng_zhao_2022]
- [Zhai et al 2020][research_zhai_li_2020]
- [Zhang 2024][research_zhang_2024]
- [Zhang and Cheng 2024][research_zhang_cheng_2024]
- [Zhang and Feng 2023][research_zhang_feng_2023]
- [Zhang and Hou 2015][research_zhang_hou_2015]
- [Zhang and Malekgoudarzi 2020][research_zhang_malekgoudarzi_2020]
- [Zhang and Vahdati 2018][research_zhang_vahdati_2018]
- [Zhang and Vahdati 2019][research_zhang_vahdati_2019]
- [Zhang and Wang 2022][research_zhang_wang_2022]
- [Zhang and Wu 2026][research_zhang_wu_2026]
- [Zhang and Zhang 2020][research_zhang_zhang_2020]
- [Zhang et al 2015][research_zhang_chen_2015]
- [Zhang et al 2015][research_zhang_tan_2015]
- [Zhang et al 2015][research_zhang_zhou_2015]
- [Zhang et al 2016][research_zhang_robson_2016]
- [Zhang et al 2016][research_zhang_yu_2016]
- [Zhang et al 2017][research_zhang_shan_2017]
- [Zhang et al 2017][research_zhang_zhou_2017]
- [Zhang et al 2018][research_zhang_tan_2018]
- [Zhang et al 2018][research_zhang_tiwari_2018]
- [Zhang et al 2019][research_zhang_chen_2019]
- [Zhang et al 2020][research_zhang_li_2020]
- [Zhang et al 2020][research_zhang_stapelfeldt_2020]
- [Zhang et al 2020][research_zhang_yuan_2020]
- [Zhang et al 2021][research_zhang_du_2021]
- [Zhang et al 2021][research_zhang_li_2021]
- [Zhang et al 2021][research_zhang_wang_2021]
- [Zhang et al 2022][research_zhang_lu_2022]
- [Zhang et al 2022][research_zhang_wei_2022]
- [Zhang et al 2022][research_zhang_zhao_2022]
- [Zhang et al 2023][research_zhang_liu_2023]
- [Zhang et al 2023][research_zhang_wang_2023]
- [Zhang et al 2024][research_zhang_an_2024]
- [Zhang et al 2024][research_zhang_chen_2024]
- [Zhang et al 2024][research_zhang_dong_2024]
- [Zhang et al 2024][research_zhang_huang_2024]
- [Zhang et al 2024][research_zhang_liu_2024]
- [Zhang et al 2024][research_zhang_wang_2024]
- [Zhang et al 2024][research_zhang_zhang_2024]
- [Zhang et al 2024][research_zhang_zhang_2024_b]
- [Zhang et al 2024][research_zhang_zhang_2024_c]
- [Zhang et al 2024][research_zhang_zhou_2024]
- [Zhang et al 2025][research_zhang_cheng_2025]
- [Zhang et al 2025][research_zhang_ji_2025]
- [Zhang et al 2025][research_zhang_yang_2025]
- [Zhang et al 2025][research_zhang_yang_2025_b]
- [Zhang et al 2026][research_zhang_bo_2026]
- [Zhang et al 2026][research_zhang_ning_2026]
- [Zhang et al 2026][research_zhang_yang_2026]
- [Zhao and Sushama 2020][research_zhao_sushama_2020]
- [Zhao et al 2017][research_zhao_sun_2017]
- [Zhao et al 2017][research_zhao_zhou_2017]
- [Zhao et al 2019][research_zhao_li_2019]
- [Zhao et al 2019][research_zhao_zhou_2019]
- [Zhao et al 2022][research_zhao_vanhoorn_2022]
- [Zhao et al 2022][research_zhao_zhou_2022]
- [Zhao et al 2023][research_zhao_jin_2023]
- [Zhao et al 2023][research_zhao_zeng_2023]
- [Zhao et al 2024][research_zhao_clarke_2024]
- [Zhao et al 2025][research_zhao_jin_2025]
- [Zhao et al 2025][research_zhao_li_2025]
- [Zheldubovskii and Ishchenko 1982][research_zheldubovskii_ishchenko_1982]
- [Zhelnina et al 2017][research_zhelnina_illarionov_2017]
- [Zhen and Kun 2015][research_zhen_kun_2015]
- [Zheng and Duan 2023][research_zheng_duan_2023]
- [Zheng and Ramaprian 1993][research_zheng_ramaprian_1993]
- [Zheng et al 2024][research_zheng_wei_2024]
- [Zheng et al 2026][research_zheng_huang_2026]
- [Zhi-fei et al 2023][research_zhifei_yingxin_2023]
- [Zhipeng et al 2015][research_zhipeng_chao_2015]
- [Zhong et al 2022][research_zhong_zhao_2022]
- [Zhong et al 2024][research_zhong_yu_2024]
- [Zhou et al 2018][research_zhou_ren_2018]
- [Zhou et al 2018][research_zhou_zhang_2018]
- [Zhou et al 2019][research_zhou_li_2019]
- [Zhou et al 2023][research_zhou_huang_2023]
- [Zhou et al 2025][research_zhou_chen_2025]
- [Zhou et al 2025][research_zhou_liu_2025]
- [Zhu and Yang 2020][research_zhu_yang_2020]
- [Zhu and Yuan 2024][research_zhu_yuan_2024]
- [Zhu and Zhao 2016][research_zhu_zhao_2016]
- [Zhu et al 2018][research_zhu_chen_2018]
- [Zhu et al 2018][research_zhu_lee_2018]
- [Zhu et al 2019][research_zhu_qin_2019]
- [Zhu et al 2019][research_zhu_qin_2019_b]
- [Zhu et al 2020][research_zhu_luo_2020]
- [Zhu et al 2021][research_zhu_nie_2021]
- [Zhu et al 2022][research_zhu_gu_2022]
- [Zhu et al 2023][research_zhu_wu_2023]
- [Zhu et al 2023][research_zhu_xing_2023]
- [Zhuang and Lu 2015][research_zhuang_lu_2015]
- [Ziegler 1963][research_ziegler_1963]
- [Zien and Ragsdale 1979][research_zien_ragsdale_1979]
- [Ziganshin and Logachev 2020][research_ziganshin_logachev_2020]
- [Zimmerman, C H 1935][research_zimmermanch_1935]
- [Zoccoli 1977][research_zoccoli_1977]
- [Zubair et al 2022][research_zubair_ejaz_2022]
- [Zubtsov and Sudakov 1982][research_zubtsov_sudakov_1982]
- [Zukoski and Auerbach 1976][research_zukoski_auerbach_1976]
- [Zuo 2021][research_zuo_2021]
- [Zuo 2023][research_zuo_2023]
- [zurLippe 2013][research_zurlippe_2013]
- [Zwieback 1964][research_zwieback_1964]
- [Öznalbant and Kavsaoğlu 2018][research_oznalbant_kavsaoglu_2018]
- [Ünal et al 2023][research_unal_oz_2023]
- [Şimşek and Uslu 2019][research_simsek_uslu_2019]
- [Şöhret et al 2015][research_sohret_turan_2015]
- [王 et al 2022][research___2022]

[research_1554_thermal_1974]: https://doi.org/10.1016/0042-207x(74)92406-3
[research_16_percent_1954]: https://doi.org/10.1016/s0042-207x(54)80174-6
[research___2022]: https://doi.org/10.1360/ssi-2022-0185
[research___2023]: https://doi.org/10.36948/ijfmr.2023.v05i05.7351
[research_a_conference_1954]: https://doi.org/10.1108/eb032393
[research_abazyan_melikyan_2021]: https://doi.org/10.1016/j.mejo.2021.105198
[research_abbasi_pirnia_2018]: https://doi.org/10.15632/jtam-pl.56.4.1005
[research_abdelghany_2025]: https://doi.org/10.21608/ijaes.2024.319394.1027
[research_abdelwahabm_1977]: https://ntrs.nasa.gov/citations/19770024209
[research_abdelwahabm_1981]: https://ntrs.nasa.gov/citations/19820010348
[research_abdolahipour_mani_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001463
[research_abdolahipour_mani_2022_b]: https://doi.org/10.1007/s10494-022-00327-9
[research_abdulkaiyoom_yildirim_2025]: https://doi.org/10.2514/1.c037678
[research_abdulrasoul_radhi_2020]: https://doi.org/10.1016/j.csite.2020.100705
[research_abedi_askari_2020]: https://doi.org/10.1016/j.ast.2019.105547
[research_abedi_salehi_2021]: https://doi.org/10.5541/ijot.785357
[research_abraham_lazzara_2024]: https://doi.org/10.3390/aerospace11050359
[research_abusalem_palaia_2023]: https://doi.org/10.3390/en16104013
[research_abusalem_palaia_2023_b]: https://doi.org/10.3390/aerospace10050459
[research_acharya_karbhari_2026]: https://doi.org/10.3390/polym18030354
[research_adamsjcjr_martindalewr_1984]: https://ntrs.nasa.gov/citations/19840035307
[research_addoakoto_han_2019]: https://doi.org/10.1007/s00348-019-2816-0
[research_adetifa_mcalpine_2018]: https://doi.org/10.2514/1.j056121
[research_aerodynamic_and_1960]: https://ntrs.nasa.gov/citations/19980228350
[research_afanasev_nikitin_2019]: https://doi.org/10.3103/s1068798x1901012x
[research_afonso_vale_2017]: https://doi.org/10.1016/j.ast.2017.03.029
[research_afridi_khan_2024]: https://doi.org/10.1115/1.4064608
[research_agag_ali_2026]: https://doi.org/10.1016/j.tourman.2026.105427
[research_agarwal_mthembu_2020]: https://doi.org/10.1016/j.matpr.2020.02.621
[research_agarwal_rakich_1982]: https://doi.org/10.2514/3.51132
[research_aggarwal_valerdi_2010]: https://doi.org/10.21236/ada568331
[research_agungsaputra_bhimashaktiarafat_2026]: https://doi.org/10.55606/teknik.v6i1.8537
[research_ahmad_zheng_2021]: https://doi.org/10.24200/sci.2021.56486.4742
[research_ahuja_mavris_2022]: https://doi.org/10.2514/1.c036654
[research_ai_2026]: https://doi.org/10.26897/2687-1149-2026-3-27-35
[research_airforceresearchlabedwardsafbca_2000]: https://doi.org/10.21236/ada404927
[research_airforcetestpilotschooledwardsafbca_1988]: https://doi.org/10.21236/ada319984
[research_airforcetestpilotschooledwardsafbca_1989]: https://doi.org/10.21236/ada319980
[research_airforcetestpilotschooledwardsafbca_1990]: https://doi.org/10.21236/ada319976
[research_airforcetestpilotschooledwardsafbca_1990_b]: https://doi.org/10.21236/ada319978
[research_ajain_2025]: https://doi.org/10.21275/sr251223120745
[research_ajay_kundu_2025]: https://doi.org/10.1017/aer.2025.7
[research_ak_ps_2018]: https://doi.org/10.1108/aeat-12-2017-0275
[research_akdeniz_2021]: https://doi.org/10.1108/aeat-11-2020-0264
[research_akhlaghi_azizi_2022]: https://doi.org/10.3390/machines10080706
[research_akhlaghi_azizi_2023]: https://doi.org/10.3390/aerospace10090763
[research_alaggs_kaufmanh_1974]: https://ntrs.nasa.gov/citations/19740055118
[research_alberts_1995]: https://doi.org/10.21236/ada296175
[research_albuquerque_gamboa_2018]: https://doi.org/10.2514/1.c034403
[research_aleisa_kontis_2023]: https://doi.org/10.2514/1.c037257
[research_alendar_grunin_2022]: https://doi.org/10.3103/s1068798x2207005x
[research_alexander_1970]: https://doi.org/10.21236/ad0875525
[research_alford_2004]: https://doi.org/10.21236/ada423468
[research_ali_asghar_2017]: https://doi.org/10.13033/ijahp.v9i2.489
[research_ali_khan_2025]: https://doi.org/10.55524/ijircst.2025.13.3.24
[research_ali_kuntjoro_2020]: https://doi.org/10.1088/1757-899x/834/1/012015
[research_alipour_nejad_2016]: https://doi.org/10.3139/146.111362
[research_allen_mahorter_1964]: https://doi.org/10.21236/ad0609355
[research_allison_morris_2015]: https://doi.org/10.12989/aas.2015.2.1.017
[research_alone_kumar_2016]: https://doi.org/10.1016/j.jppr.2016.01.009
[research_alsaffar_ashworth_1980]: https://doi.org/10.1016/0010-938x(80)90116-x
[research_alshamma_ali_2017]: https://doi.org/10.5937/jaes15-14829
[research_alsmadi_murty_2020]: https://doi.org/10.1080/09603409.2020.1859310
[research_alsmadi_murty_2021]: https://doi.org/10.1016/j.ijfatigue.2020.105987
[research_amann_nordenson_1975]: https://doi.org/10.1115/1.3445996
[research_amatucci_addy_1982]: https://doi.org/10.2514/3.7977
[research_amnasir_saadon_2018]: https://doi.org/10.14419/ijet.v7i4.13.21342
[research_an_investigation_1979]: https://doi.org/10.1016/0003-6870(79)90096-6
[research_analysis_of_2021]: https://doi.org/10.47939/et.v2i6.122
[research_analysis_of_2022]: https://doi.org/10.23977/ieim.2022.050802
[research_analysis_of_2024]: https://doi.org/10.47176/jafm.17.02.2101
[research_anantachaisilp_lin_2020]: https://doi.org/10.3390/act9030075
[research_anatomy_of_1970]: https://doi.org/10.1016/0010-4361(70)90311-3
[research_anderson_1961]: https://doi.org/10.21236/ad0322137
[research_anderson_2017]: https://doi.org/10.69554/kqzv7354
[research_anderson_berger_1973]: https://doi.org/10.2514/3.60204
[research_anderson_murthy_1969]: https://doi.org/10.2514/3.48102
[research_andersonadriene_1947]: https://ntrs.nasa.gov/citations/19930085723
[research_andersonbernhardh_levyralph_1991]: https://ntrs.nasa.gov/citations/19920004741
[research_andersonbernhardh_weirlois_2014]: https://ntrs.nasa.gov/citations/20140016538
[research_andersonbh_1974]: https://ntrs.nasa.gov/citations/19740013281
[research_andersonbh_bowditchdn_1958]: https://ntrs.nasa.gov/citations/19650013032
[research_andersonbh_bowditchdn_1960]: https://ntrs.nasa.gov/citations/19630002315
[research_andersonsethb_brayrichards_1951]: https://ntrs.nasa.gov/citations/19930086840
[research_andersonsethb_brayrichards_1955]: https://ntrs.nasa.gov/citations/19930092243
[research_andrews_1969]: https://doi.org/10.2514/3.44090
[research_anglin_1978]: https://doi.org/10.2514/3.58445
[research_anglin_satran_1980]: https://doi.org/10.2514/3.57980
[research_anon_2015]: https://doi.org/10.15623/ijret.2015.0409049
[research_anon_2016]: https://doi.org/10.15623/ijret.2016.0505016
[research_anon_2024]: https://doi.org/10.36948/ijfmr.2024.v06i01.11628
[research_anonymous_2025]: https://doi.org/10.1103/jkhd-xmj6
[research_ansari_m_2022]: https://doi.org/10.47893/gret.2022.1086
[research_antaranalbert_beletehailu_1992]: https://ntrs.nasa.gov/citations/19930008977
[research_anti_surge_control_2021]: https://doi.org/10.47939/et.v2i10.438
[research_anti_surge_reason_2021]: https://doi.org/10.47939/et.v2i3.33
[research_aoyagik_hickeydh_1963]: https://ntrs.nasa.gov/citations/19630006046
[research_aoyagikiyoshi_hickeydavidh_1959]: https://ntrs.nasa.gov/citations/19980228317
[research_application_analysis_2022]: https://doi.org/10.47939/et.v3i5(02).13
[research_application_of_2021]: https://doi.org/10.47939/et.v2i7.51
[research_application_of_2021_b]: https://doi.org/10.47939/et.v2i5.118
[research_application_practice_2021]: https://doi.org/10.47939/et.v2i10.366
[research_araujo_pereira_2021]: https://doi.org/10.1016/j.ast.2021.106864
[research_archbold_1945]: https://doi.org/10.1017/s0001924000108632
[research_arias_martinez_2023]: https://doi.org/10.3390/drones7120686
[research_aribi_boushaki_2023]: https://doi.org/10.37394/232016.2023.18.1
[research_arif_iftikhar_2021]: https://doi.org/10.1177/09544100211002970
[research_arifin_yusoff_2020]: https://doi.org/10.15282/jmes.14.2.2020.27.0539
[research_arkoosh_fiore_1972]: https://doi.org/10.1007/bf02643237
[research_armstrong_palladino_1980]: https://doi.org/10.21236/ada093156
[research_armymaterielcommandalexandriava_1987]: https://doi.org/10.21236/ada192046
[research_arnson_aljaber_2026]: https://doi.org/10.2514/1.c038387
[research_ashwood_1973]: https://doi.org/10.2514/3.60249
[research_askari_abedi_2026]: https://doi.org/10.1016/j.flowmeasinst.2025.103045
[research_askari_soltani_2019]: https://doi.org/10.2514/1.c035328
[research_askari_soltani_2019_b]: https://doi.org/10.29252/jafm.12.06.29880
[research_askari_soltani_2020]: https://doi.org/10.2514/1.j059006
[research_askari_soltani_2022]: https://doi.org/10.2514/1.j061201
[research_askari_soltani_2023]: https://doi.org/10.2514/1.c037043
[research_assessment_of_2023]: https://doi.org/10.13187/ejpe.2023.1.31
[research_atasoy_cetek_2020]: https://doi.org/10.1017/aer.2020.121
[research_atassi_kozlov_2019]: https://doi.org/10.1115/1.4043963
[research_awerbuch_1980]: https://doi.org/10.21236/ada111006
[research_axelsonjohna_crownjconrad_1948]: https://ntrs.nasa.gov/citations/19930085834
[research_axial_transonic_2022]: https://doi.org/10.55787/jtams.22.52.2.144
[research_ayers_1962]: https://doi.org/10.1108/eb033637
[research_aygun_caliskan_2021]: https://doi.org/10.1016/j.enconman.2021.114797
[research_aygun_turan_2023]: https://doi.org/10.1016/j.energy.2022.126468
[research_azam_2020]: https://doi.org/10.34021/ve.2020.03.02(4)
[research_azizi_brouwer_2017]: https://doi.org/10.1016/j.jpowsour.2017.09.010
[research_ba_wang_2019]: https://doi.org/10.1515/phys-2019-0080
[research_baag_mahapatra_2020]: https://doi.org/10.1016/j.jtherbio.2019.102494
[research_babaei_setayandeh_2018]: https://doi.org/10.1016/j.cja.2018.04.018
[research_babinsky_2014]: https://doi.org/10.21236/ada602774
[research_back_massier_1967]: https://doi.org/10.2514/3.29015
[research_backlh_cuffelrf_1966]: https://ntrs.nasa.gov/citations/19670036104
[research_bacon_1988]: https://doi.org/10.21236/ada192789
[research_bae_jung_2023]: https://doi.org/10.1109/access.2023.3257849
[research_bagby_andersen_1966]: https://doi.org/10.2514/3.43750
[research_bahulekar_mello_2024]: https://doi.org/10.4236/wjet.2024.121008
[research_bai_yu_2022]: https://doi.org/10.1016/j.msea.2022.142921
[research_baidya_pesyridis_2018]: https://doi.org/10.3390/app8040574
[research_bailey_1963]: https://doi.org/10.21236/ad0437102
[research_baker_1966]: https://doi.org/10.2514/3.43708
[research_bakhlemilinda_reddytsr_2018]: https://ntrs.nasa.gov/citations/20180002211
[research_balakrishnan_abdrahimabutalib_2024]: https://doi.org/10.11113/jtse.v11.218
[research_balas_pearson_2019]: https://doi.org/10.1038/s41598-018-37991-9
[research_balashov_petukhov_1969]: https://doi.org/10.1007/bf01543222
[research_baldo_will_1990]: https://doi.org/10.21236/ada239727
[research_baldwin_cliborn_1976]: https://doi.org/10.21236/ada035863
[research_ball_ross_1972]: https://doi.org/10.2514/3.59042
[research_balli_caliskan_2021]: https://doi.org/10.1016/j.energy.2021.121031
[research_balusamy_a_2024]: https://doi.org/10.1108/aeat-04-2023-0088
[research_balut_davis_2003]: https://doi.org/10.21236/ada418948
[research_ban_yamazaki_2018]: https://doi.org/10.2514/1.c034171
[research_bangert_santman_1982]: https://doi.org/10.2514/3.57356
[research_banksdanielw_paulsonjohnwjr_1987]: https://ntrs.nasa.gov/citations/19870005747
[research_barderamora_garciamagarino_2019]: https://doi.org/10.2514/1.c035188
[research_baretter_godard_2021]: https://doi.org/10.3390/ijtpp6040043
[research_barlow_burrus_2008]: https://doi.org/10.21236/ada478871
[research_baron_1953]: https://doi.org/10.2514/8.2565
[research_barone_nicholson_2022]: https://doi.org/10.1103/physrevfluids.7.084604
[research_barrettgonzalez_wolf_2021]: https://doi.org/10.3390/act10100265
[research_barry_1971]: https://doi.org/10.2514/3.44269
[research_barryfw_1968]: https://ntrs.nasa.gov/citations/19710028359
[research_bartman_kwiatkowski_2018]: https://doi.org/10.1515/msr-2018-0011
[research_barton_edwards_1968]: https://doi.org/10.1016/0022-4898(68)90110-9
[research_baryshev_leontev_1976]: https://doi.org/10.1007/bf00863655
[research_basov_berezhnoy_1977]: https://doi.org/10.1109/jqe.1977.1069590
[research_batayev_suleimenov_2022]: https://doi.org/10.11591/ijece.v12i2.pp1419-1428
[research_battertonpg_arpasidj_1974]: https://ntrs.nasa.gov/citations/19740025659
[research_battiston_magrini_2025]: https://doi.org/10.2514/1.c038084
[research_bauerstevenxs_mcmillinsnaomi_1988]: https://ntrs.nasa.gov/citations/19880053539
[research_bayat_ekhteraeitoussi_2017]: https://doi.org/10.1016/j.ast.2017.04.029
[research_baydar_lu_2018]: https://doi.org/10.2514/1.b36414
[research_baydarezgihan_lufrankk_2016]: https://ntrs.nasa.gov/citations/20170000948
[research_baydarezgihan_lufrankk_2017]: https://ntrs.nasa.gov/citations/20170001419
[research_baykal_sarikaya_1980]: https://doi.org/10.1501/commub_0000000155
[research_bazhina_bazhin_2021]: https://doi.org/10.1016/j.intermet.2021.107313
[research_beck_1984]: https://doi.org/10.21236/ada328840
[research_beck_1984_b]: https://doi.org/10.21236/ada143254
[research_bedell_2010]: https://doi.org/10.21236/ada561210
[research_beesly_1966]: https://doi.org/10.1108/eb034195
[research_beesly_1966_b]: https://doi.org/10.1049/tpe.1966.0073
[research_beevers_1973]: https://doi.org/10.1007/bf01260879
[research_beheimma_gertsmalw_1956]: https://ntrs.nasa.gov/citations/19630002647
[research_bekris_gioldasis_2023]: https://doi.org/10.18276/cej.2023.4-06
[research_benaouali_kachel_2019]: https://doi.org/10.1016/j.ast.2019.06.040
[research_bengida_gurka_2022]: https://doi.org/10.1088/1748-3190/ac9bb5
[research_benichou_binder_2021]: https://doi.org/10.3390/ijtpp6030034
[research_benmiloud_dghim_2020]: https://doi.org/10.1016/j.jweia.2020.104211
[research_bennetclark_1972]: https://doi.org/10.1038/239451b0
[research_bennett_2003]: https://doi.org/10.21236/ada415479
[research_benson_1977]: https://doi.org/10.1016/0020-7403(77)90072-8
[research_bensonthomasj_1997]: https://ntrs.nasa.gov/citations/20050179350
[research_beppu_curtiss_1966]: https://doi.org/10.21236/ad0640945
[research_bera_1975]: https://doi.org/10.2514/3.44499
[research_bera_1980]: https://doi.org/10.1080/0020739800110412
[research_berezovsky_2018]: https://doi.org/10.15588/1727-0219-2018-1-6
[research_bergstedt_turner_1959]: https://doi.org/10.21236/ad0402171
[research_berto_benini_2020]: https://doi.org/10.2514/1.j058764
[research_bertonjeffreyj_2003]: https://ntrs.nasa.gov/citations/20040008601
[research_bertrammh_ulmannef_1953]: https://ntrs.nasa.gov/citations/19630010653
[research_beschorner_kriewall_2025]: https://doi.org/10.2514/1.c038220
[research_bhandari_gaur_2025]: https://doi.org/10.1016/j.engfailanal.2025.109534
[research_bhat_zhao_2018]: https://doi.org/10.1098/rsos.172197
[research_bhunia_abbas_2026]: https://doi.org/10.61653/joast.v78i2.2026.1160
[research_bian_cao_2019]: https://doi.org/10.1016/j.energy.2019.116082
[research_bianchi_secco_2020]: https://doi.org/10.1017/aer.2020.134
[research_bidaki_2022]: https://doi.org/10.31579/2642-9730/017
[research_bielatralphp_1959]: https://ntrs.nasa.gov/citations/19980232001
[research_biesiadnythomasj_wendtbrucej_2004]: https://ntrs.nasa.gov/citations/20050040781
[research_biesiadnytj_greyre_1976]: https://ntrs.nasa.gov/citations/19760014125
[research_bihrle_barnhart_1982]: https://doi.org/10.2514/3.44789
[research_bilanin_donaldson_1975]: https://doi.org/10.2514/3.44476
[research_bilous_vrzhizhevskyi_2026]: https://doi.org/10.37434/tpwj2026.07.05
[research_bilwakeshkr_doylevl_1971]: https://ntrs.nasa.gov/citations/19710023725
[research_bilwakeshkr_kochcc_1972]: https://ntrs.nasa.gov/citations/19720020168
[research_birch_paynter_1978]: https://doi.org/10.2514/3.58395
[research_birdjohnd_lichtensteinjacobh_1952]: https://ntrs.nasa.gov/citations/19930083189
[research_biriukov_1959]: https://doi.org/10.1016/0021-8928(59)90174-1
[research_blahabj_johnsal_1971]: https://ntrs.nasa.gov/citations/19710009388
[research_bleviss_struble_1954]: https://doi.org/10.2514/8.3176
[research_bloxsom_1958]: https://doi.org/10.2514/8.7403
[research_boger_greer_1989]: https://doi.org/10.21236/ada207345
[research_boger_nussbaum_1990]: https://doi.org/10.21236/ada229704
[research_bolesmichaela_heavnerrichardl_1988]: https://ntrs.nasa.gov/citations/19910004130
[research_bolesmichaela_heavnerrichardl_1991]: https://ntrs.nasa.gov/citations/19910014810
[research_bollechthomasv_kellyhneale_1954]: https://ntrs.nasa.gov/citations/20090022756
[research_bond_brown_2025]: https://doi.org/10.2514/1.j065421
[research_bond_key_2025]: https://doi.org/10.1115/1.4070057
[research_bond_key_2026]: https://doi.org/10.2514/1.j066481
[research_bondi_1979]: https://doi.org/10.21236/ada077035
[research_bortinsrichard_sorensenjohna_1993]: https://ntrs.nasa.gov/citations/19950004810
[research_boudreau_1977]: https://doi.org/10.2514/3.58889
[research_boussios_epstein_1992]: https://doi.org/10.21236/ada252771
[research_bouzekovapenkova_miteva_2022]: https://doi.org/10.3897/arb.v34.e15
[research_bowditchdn_coltrinre_1983]: https://ntrs.nasa.gov/citations/19830064291
[research_bowers_1981]: https://doi.org/10.2514/3.57530
[research_bowling_hurkamp_1971]: https://doi.org/10.2514/3.59119
[research_boylan_1965]: https://doi.org/10.21236/ad0460154
[research_boytos_1969]: https://doi.org/10.2514/3.44107
[research_braithwaite_soeder_1980]: https://doi.org/10.2514/3.57927
[research_braithwaitewm_1973]: https://ntrs.nasa.gov/citations/19740002609
[research_braithwaitewm_soederrh_1979]: https://ntrs.nasa.gov/citations/19790015792
[research_branstetterjr_juhaszaj_1971]: https://ntrs.nasa.gov/citations/19710009407
[research_braun_paniagua_2020]: https://doi.org/10.1115/1.4045359
[research_bravomosquera_abdalla_2019]: https://doi.org/10.1016/j.ast.2019.01.059
[research_brazzel_henderson_1970]: https://doi.org/10.21236/ad0871756
[research_breaks_1973]: https://doi.org/10.2514/3.60235
[research_bretschneider_reed_2015]: https://doi.org/10.1115/1.4031474
[research_brianas_2005]: https://doi.org/10.21236/ada435694
[research_briggsbenjaminr_1960]: https://ntrs.nasa.gov/citations/19980227791
[research_brightmichellem_korntheuerandrea_2013]: https://ntrs.nasa.gov/citations/20130003192
[research_brodsky_1970]: https://doi.org/10.21236/ad0716026
[research_brooke_1957]: https://doi.org/10.21236/ad0154531
[research_brophy_hawk_1990]: https://doi.org/10.21236/ada378098
[research_brown_1970]: https://doi.org/10.21236/ad0712047
[research_brownclintone_1946]: https://ntrs.nasa.gov/citations/19930090940
[research_browne_friedman_1948]: https://doi.org/10.2514/8.11620
[research_brownsc_hardygh_1983]: https://ntrs.nasa.gov/citations/19830018574
[research_brownstuartc_1959]: https://ntrs.nasa.gov/citations/19980228294
[research_bryant_1933]: https://doi.org/10.1108/eb029696
[research_brycelhorvath_douglaspwells_2018]: https://ntrs.nasa.gov/citations/20190000431
[research_bryson_marks_2016]: https://doi.org/10.2514/1.c033455
[research_bryson_rumpfkeil_2019]: https://doi.org/10.2514/1.c035152
[research_bsaheby_shen_2019]: https://doi.org/10.1177/0954410019875384
[research_buchholzmarkd_1992]: https://ntrs.nasa.gov/citations/19940019630
[research_buchholzmarkd_tsojin_1993]: https://ntrs.nasa.gov/citations/19970022303
[research_buchsbaum_1963]: https://doi.org/10.21236/ad0402905
[research_bukkvoll_2024]: https://doi.org/10.1525/cpcs.2024.2279103
[research_bullg_bridgespd_1983]: https://ntrs.nasa.gov/citations/19840029551
[research_bundtzen_hinrichs_2021]: https://doi.org/10.21272/sec.5(1).35-43.2021
[research_burkhalter_1982]: https://doi.org/10.2514/3.44793
[research_burksmjr_waregm_1967]: https://ntrs.nasa.gov/citations/19670027396
[research_burleyrr_1971]: https://ntrs.nasa.gov/citations/19720004062
[research_burleyrr_mansourah_1969]: https://ntrs.nasa.gov/citations/19690025535
[research_burleyrr_mansourah_1970]: https://ntrs.nasa.gov/citations/19700015497
[research_burleyrr_samanichne_1970]: https://ntrs.nasa.gov/citations/19700057447
[research_burns_koo_2015]: https://doi.org/10.2514/1.j053049
[research_burrows_vukasinovic_2025]: https://doi.org/10.2514/1.c037992
[research_burstadtpl_calogerasje_1971]: https://ntrs.nasa.gov/citations/19710050036
[research_burstadtpl_calogerasje_1974]: https://ntrs.nasa.gov/citations/19740022130
[research_burstadtpl_wenzellm_1976]: https://ntrs.nasa.gov/citations/19760055251
[research_burton_noordhuizen_2004]: https://doi.org/10.21236/ada432867
[research_butler_1982]: https://doi.org/10.2514/3.44764
[research_butler_2025]: https://doi.org/10.21552/edseq/2026/1/7
[research_butter_hancock_1971]: https://doi.org/10.1017/s0001924000046133
[research_buzica_breitsamter_2020]: https://doi.org/10.3390/aerospace7010004
[research_bykerk_verstraete_2020]: https://doi.org/10.1016/j.ast.2019.105531
[research_bywater_hezlett_2020]: https://doi.org/10.53841/bpsadm.2020.12.2.3
[research_cabreracruz_pezzini_2020]: https://doi.org/10.1115/1.4045218
[research_cai_huang_2022]: https://doi.org/10.3390/en15113879
[research_cai_huang_2022_b]: https://doi.org/10.3390/en15145057
[research_cai_huang_2022_c]: https://doi.org/10.3389/fenrg.2022.884540
[research_cai_sun_2023]: https://doi.org/10.1016/j.measurement.2023.112437
[research_cain_mogonye_2021]: https://doi.org/10.21236/ad1153484
[research_callahan_stenning_1971]: https://doi.org/10.2514/3.44259
[research_calligeros_dugundji_1961]: https://doi.org/10.21236/ad0253970
[research_calogerasje_burstadtpl_1974]: https://ntrs.nasa.gov/citations/19740021193
[research_calogerasje_coltrinre_1969]: https://ntrs.nasa.gov/citations/19690054687
[research_calogerasje_johnsenrl_1974]: https://ntrs.nasa.gov/citations/19740014513
[research_campbell_1976]: https://doi.org/10.2514/3.58703
[research_campbell_ellis_1971]: https://doi.org/10.2514/3.59101
[research_campbell_hassel_1978]: https://doi.org/10.2514/3.58318
[research_campion_1954]: https://doi.org/10.1017/s0001925900001232
[research_cannon_1966]: https://doi.org/10.2514/3.43772
[research_cao_yao_2022]: https://doi.org/10.3390/aerospace9100603
[research_cao_yuan_2022]: https://doi.org/10.1007/s11630-022-1551-7
[research_cao_yue_2024]: https://doi.org/10.3390/w16091282
[research_cao_zhang_2020]: https://doi.org/10.7717/peerj.8784
[research_cao_zhang_2023]: https://doi.org/10.1016/j.mtcomm.2023.106796
[research_cao_zhu_2021]: https://doi.org/10.1016/j.renene.2020.11.060
[research_caponefj_reubushde_1983]: https://ntrs.nasa.gov/citations/19830018550
[research_carafoli_berbente_1974]: https://doi.org/10.1016/0093-6413(74)90071-8
[research_carafoli_berbente_1976]: https://doi.org/10.1017/s0001925900007757
[research_carey_1982]: https://doi.org/10.2307/2617820
[research_carlincm_frischi_2003]: https://ntrs.nasa.gov/citations/20030065839
[research_carlson_schwope_1952]: https://doi.org/10.21236/ada076046
[research_carlyle_1976]: https://doi.org/10.21236/ada956001
[research_carmichael_mcnay_1961]: https://doi.org/10.21236/ad0282125
[research_carnevale_wang_2016]: https://doi.org/10.1115/1.4034600
[research_carosiello_1963]: https://doi.org/10.21236/ad0406931
[research_carreyette_1950]: https://doi.org/10.1108/eb031848
[research_carroll_1960]: https://doi.org/10.21236/ad0316227
[research_cary_walker_1974]: https://doi.org/10.1080/03071847409421162
[research_cassetti_1978]: https://doi.org/10.1108/eb035480
[research_castner_zaman_2017]: https://doi.org/10.2514/1.c033623
[research_celesios_acquisition_2016]: https://doi.org/10.1211/pj.2016.20201477
[research_cervay_1975]: https://doi.org/10.21236/ada021689
[research_cetkovic_2016]: https://doi.org/10.1016/j.compstruct.2016.01.082
[research_cevik_ducvo_2016]: https://doi.org/10.1115/1.4033420
[research_chace_2015]: https://doi.org/10.21236/ada619434
[research_chai_li_2020]: https://doi.org/10.1016/j.ast.2020.106000
[research_chai_song_2017]: https://doi.org/10.1016/j.actaastro.2017.08.016
[research_chai_yu_2018]: https://doi.org/10.1016/j.cja.2017.10.006
[research_chakraborty_khan_2026]: https://doi.org/10.1016/j.jallcom.2026.187122
[research_chakraborty_nam_2015]: https://doi.org/10.2514/1.c033120
[research_chambers_bowman_1971]: https://doi.org/10.2514/3.59136
[research_chan_perreydebain_2017]: https://doi.org/10.1016/j.apacoust.2016.09.024
[research_chandra_2020]: https://doi.org/10.1007/s42405-019-00247-5
[research_chang_hsu_1960]: https://doi.org/10.2514/8.5121
[research_chang_nordheim_1953]: https://doi.org/10.21236/ad0000961
[research_chang_wei_2022]: https://doi.org/10.1080/19942060.2022.2072954
[research_chapman_1979]: https://doi.org/10.21236/ada082821
[research_chapmandave_smithcf_2005]: https://ntrs.nasa.gov/citations/20050061002
[research_chau_zingg_2022]: https://doi.org/10.2514/1.c036389
[research_cheidris_saad_2020]: https://doi.org/10.37934/arfmts.77.1.110
[research_chell_hoffenson_2021]: https://doi.org/10.1115/1.4049657
[research_chen_bai_2016]: https://doi.org/10.1016/j.euromechflu.2016.06.005
[research_chen_cai_2021]: https://doi.org/10.1016/j.ast.2021.106590
[research_chen_chen_2016]: https://doi.org/10.4028/www.scientific.net/amm.853.122
[research_chen_chen_2021]: https://doi.org/10.1515/tjj-2021-0045
[research_chen_chen_2023]: https://doi.org/10.1088/1742-6596/2441/1/012001
[research_chen_dai_2024]: https://doi.org/10.1007/s11749-024-00941-x
[research_chen_dugundji_1980]: https://doi.org/10.2514/3.57942
[research_chen_ge_2020]: https://doi.org/10.3390/e22040397
[research_chen_he_2025]: https://doi.org/10.1177/16878132251348391
[research_chen_jiang_2026]: https://doi.org/10.1016/j.tra.2025.104849
[research_chen_lee_2026]: https://doi.org/10.1061/jaeeez.aseng-6621
[research_chen_li_2020]: https://doi.org/10.1016/j.jde.2019.12.018
[research_chen_liu_2018]: https://doi.org/10.1299/jsmebiofro.2018.29.2c26
[research_chen_ma_2021]: https://doi.org/10.1504/ijise.2021.115093
[research_chen_mi_2020]: https://doi.org/10.3390/ma13153358
[research_chen_mi_2021]: https://doi.org/10.1016/j.matlet.2021.129575
[research_chen_mi_2022]: https://doi.org/10.1016/j.coco.2022.101077
[research_chen_sethuraman_2025]: https://doi.org/10.1016/j.ast.2025.110262
[research_chen_sun_2023]: https://doi.org/10.1088/2053-1591/acc831
[research_chen_tan_2017]: https://doi.org/10.2514/1.j056066
[research_chen_tan_2018]: https://doi.org/10.2514/1.j056674
[research_chen_tan_2019]: https://doi.org/10.1016/j.ast.2019.105471
[research_chen_tan_2019_b]: https://doi.org/10.2514/1.j057811
[research_chen_wu_2018]: https://doi.org/10.1007/s00348-018-2657-2
[research_chen_wu_2020]: https://doi.org/10.1016/j.ast.2019.105589
[research_chen_xia_2022]: https://doi.org/10.3390/aerospace9120835
[research_chen_yang_2025]: https://doi.org/10.3390/computation13040101
[research_chen_yue_2021]: https://doi.org/10.1016/j.cja.2021.01.020
[research_chen_zhang_2020]: https://doi.org/10.1177/0954410020944068
[research_chen_zhang_2021]: https://doi.org/10.1016/j.ast.2021.106545
[research_chen_zhang_2021_b]: https://doi.org/10.1016/j.ast.2021.106539
[research_chen_zheng_2026]: https://doi.org/10.1016/j.ast.2025.110751
[research_cheng_huang_2024]: https://doi.org/10.1088/1742-6596/2683/1/012027
[research_cheng_li_2025]: https://doi.org/10.3390/en18174514
[research_cheng_yue_2016]: https://doi.org/10.5028/jatm.v8i1.514
[research_chengt_greitzerem_1987]: https://ntrs.nasa.gov/citations/19870058127
[research_chennuru_corral_2025]: https://doi.org/10.1115/1.4070233
[research_chesney_2005]: https://doi.org/10.21236/ada434426
[research_chessell_1979]: https://doi.org/10.1121/1.2017371
[research_chester_1953]: https://doi.org/10.1017/s0001925900000950
[research_chi_chu_2022]: https://doi.org/10.1177/09544100211063079
[research_childrd_hendersonwp_1978]: https://ntrs.nasa.gov/citations/19780063995
[research_chimarodrickv_2011]: https://ntrs.nasa.gov/citations/20110011335
[research_chimarodrickv_2012]: https://ntrs.nasa.gov/citations/20120009203
[research_chimarodrickv_hirtstefaniem_2011]: https://ntrs.nasa.gov/citations/20110023762
[research_chin_1977]: https://doi.org/10.2514/3.60721
[research_chin_1978]: https://doi.org/10.2514/3.7537
[research_chintala_s_2020]: https://doi.org/10.1002/htj.21735
[research_chippa_2010]: https://doi.org/10.21236/ada517278
[research_choe_kim_2020]: https://doi.org/10.2514/1.b37474
[research_choi_2024]: https://doi.org/10.1007/s12206-024-0533-y
[research_choi_2026]: https://doi.org/10.2139/ssrn.6742239
[research_choi_choi_2026]: https://doi.org/10.1016/j.ast.2026.113190
[research_chou_smith_1974]: https://doi.org/10.21236/ada001135
[research_chouicha_sellam_2020]: https://doi.org/10.1016/j.jppr.2020.04.002
[research_christianpsenica_leanfang_2026]: https://ntrs.nasa.gov/citations/20260000381
[research_chun_burr_1969]: https://doi.org/10.2514/3.44056
[research_ciepluchcarlc_1948]: https://ntrs.nasa.gov/citations/20050040787
[research_ciffone_pedley_1979]: https://doi.org/10.2514/3.58491
[research_ciliberti_nicolosi_2026]: https://doi.org/10.1016/j.ast.2026.113231
[research_cirlin_shen_1971]: https://doi.org/10.1080/00222337108061110
[research_clark_hallow_1972]: https://doi.org/10.21236/ad0753214
[research_clarke_wallace_1964]: https://doi.org/10.1017/s0022112064000179
[research_clarkle_richiecb_1977]: https://ntrs.nasa.gov/citations/19770017117
[research_cliett_1952]: https://doi.org/10.21236/ad0006050
[research_cloos_nelson_1990]: https://doi.org/10.21236/ada238985
[research_cm_2025]: https://doi.org/10.1080/15397734.2025.2524529
[research_coalson_1968]: https://doi.org/10.21236/ad0833750
[research_coalson_csavina_1976]: https://doi.org/10.2514/3.58723
[research_cobar_montalvo_2021]: https://doi.org/10.2514/1.c035787
[research_coble_royster_2014]: https://doi.org/10.21236/ada608062
[research_cobogonzalez_cuernorejado_2026]: https://doi.org/10.3390/aerospace13040379
[research_coe_kulla_1974]: https://doi.org/10.2514/3.60383
[research_coepljr_1976]: https://ntrs.nasa.gov/citations/19760053942
[research_coffel_thompson_2017]: https://doi.org/10.1007/s10584-017-2018-9
[research_colbourne_1980]: https://doi.org/10.1017/s0001925900008891
[research_coleburn_drimmer_1961]: https://doi.org/10.21236/ad0326783
[research_coleburn_drimmer_1962]: https://doi.org/10.21236/ad0329109
[research_colejb_1980]: https://ntrs.nasa.gov/citations/19800015023
[research_comes_2015]: https://doi.org/10.1016/j.ifacol.2015.09.598
[research_comodi_renzi_2015]: https://doi.org/10.1016/j.apenergy.2015.02.076
[research_comparative_studies_2023]: https://doi.org/10.1063/5.0144617
[research_competition_watchdog_2015]: https://doi.org/10.1211/pj.2015.20069370
[research_composite_material_1978]: https://doi.org/10.1016/0010-4361(78)90398-1
[research_composition_and_2023]: https://doi.org/10.17675/2305-6894-2023-12-3-26
[research_conceicao_anes_2019]: https://doi.org/10.1016/j.engfailanal.2019.06.070
[research_concept_designed_1995]: https://ntrs.nasa.gov/citations/20050169187
[research_concorde_automatic_1971]: https://doi.org/10.1108/eb034745
[research_cong_yu_2024]: https://doi.org/10.1007/s42401-024-00312-2
[research_connorsjamesf_wisegeorgea_1957]: https://ntrs.nasa.gov/citations/19930089864
[research_control_system_1976]: https://doi.org/10.1016/0010-4485(76)90126-3
[research_cooper_1964]: https://doi.org/10.1115/1.3677572
[research_coppi_sigmar_1973]: https://doi.org/10.1063/1.1694486
[research_corallo_sheridan_2015]: https://doi.org/10.1016/j.jweia.2015.09.006
[research_corcione_bonavolonta_2023]: https://doi.org/10.1016/j.cja.2023.03.035
[research_cordner_1967]: https://doi.org/10.21236/ad0656480
[research_cornellaeronauticallabincbuffalony_1947]: https://doi.org/10.21236/ada800190
[research_corner_1940]: https://doi.org/10.1108/eb030643
[research_cortrightedgarmjr_1951]: https://ntrs.nasa.gov/citations/19930086879
[research_cossar_moffatt_1980]: https://doi.org/10.1115/1.3230338
[research_costakiswg_1974]: https://ntrs.nasa.gov/citations/19740010284
[research_costakiswg_1975]: https://ntrs.nasa.gov/citations/19750005753
[research_cotton_1974]: https://doi.org/10.21236/ada000894
[research_cowles_1981]: https://doi.org/10.1108/eb035758
[research_cowshish_2023]: https://doi.org/10.32381/ns.2023.06.01.1
[research_cox_bohn_1982]: https://doi.org/10.21236/ada125202
[research_cox_bohn_1982_b]: https://doi.org/10.21236/ada125201
[research_cox_roy_1988]: https://doi.org/10.21236/ada202871
[research_coxbrian_borcherspaul_1990]: https://ntrs.nasa.gov/citations/19900014078
[research_craidoncb_1986]: https://ntrs.nasa.gov/citations/19850000541
[research_craneharoldl_1948]: https://ntrs.nasa.gov/citations/20050028619
[research_craneharoldl_beckhardtarnoldr_1948]: https://ntrs.nasa.gov/citations/20050031072
[research_crea_marty_2025]: https://doi.org/10.3390/ijtpp10020012
[research_crestengineeringinctulsaok_1976]: https://doi.org/10.21236/ada955268
[research_croan_rizzitano_1959]: https://doi.org/10.21236/ada952362
[research_crossey_1992]: https://doi.org/10.21236/ada262148
[research_crosthwait_1970]: https://doi.org/10.2514/3.44216
[research_crothers_1997]: https://doi.org/10.21236/ada343061
[research_crowe_1937]: https://doi.org/10.1108/eb030157
[research_crown_1950]: https://doi.org/10.21236/ad0062509
[research_cryogenic_hardening_2016]: https://doi.org/10.21172/1.81.074
[research_cubilloschacon_2007]: https://doi.org/10.21236/ada473261
[research_cui_zhang_2024]: https://doi.org/10.1088/1742-6596/2707/1/012112
[research_cummings_liersch_2018]: https://doi.org/10.2514/1.c033808
[research_cumpsty_greitzer_1982]: https://doi.org/10.1115/1.3227246
[research_cunis_condomines_2020]: https://doi.org/10.2514/1.c035455
[research_curtiss_hc_1965]: https://doi.org/10.21236/ad0628669
[research_curtiss_howardc_1969]: https://doi.org/10.21236/ad0859276
[research_custis_1978]: https://doi.org/10.1093/milmed/143.2.81
[research_cyrus_piscopo_1982]: https://doi.org/10.1115/1.3227281
[research_da_hanan_2020]: https://doi.org/10.1080/19942060.2020.1792348
[research_dafonsecafilho_gamaribeiro_2019]: https://doi.org/10.1007/s40430-018-1562-1
[research_dahlberg_1963]: https://doi.org/10.21236/ad0412465
[research_dai_boughazi_2023]: https://doi.org/10.59287/ijanser.1160
[research_dai_zhang_2023]: https://doi.org/10.3390/aerospace10060553
[research_dai_zhao_2023]: https://doi.org/10.2514/1.t6675
[research_daliri_farahani_2018]: https://doi.org/10.2514/1.b36760
[research_dalmagro_benasciutti_2016]: https://doi.org/10.1016/j.applthermaleng.2016.06.074
[research_daniele_teren_1975]: https://doi.org/10.2514/3.59880
[research_danielecj_terenf_1975]: https://ntrs.nasa.gov/citations/19750034195
[research_daroukh_moreau_2019]: https://doi.org/10.1115/1.4042163
[research_daroukh_polacsek_2020]: https://doi.org/10.2514/1.j058799
[research_das_prasad_2023]: https://doi.org/10.61653/joast.v61i2.2009.526
[research_davidson_1964]: https://doi.org/10.2514/3.43575
[research_davis_1952]: https://doi.org/10.2514/8.2275
[research_davis_1971]: https://doi.org/10.2514/3.6508
[research_davisdavido_vyasmanana_2012]: https://ntrs.nasa.gov/citations/20120013594
[research_davisra_elrodsd_1972]: https://ntrs.nasa.gov/citations/19740022813
[research_davoudzadeh_liu_1987]: https://doi.org/10.21236/ada193109
[research_day_greitzer_1978]: https://doi.org/10.1115/1.3446318
[research_day_greitzer_1978_b]: https://doi.org/10.1115/1.3446311
[research_dean_young_1977]: https://doi.org/10.1115/1.3448553
[research_dear_harrison_2022]: https://doi.org/10.1016/j.cortex.2021.10.008
[research_debogdance_dicusjh_1975]: https://ntrs.nasa.gov/citations/19750024052
[research_debogdance_mossjejr_1977]: https://ntrs.nasa.gov/citations/19770010127
[research_defenseacquisitionunivalexandriava_1996]: https://doi.org/10.21236/ada341472
[research_defenseacquisitionunivalexandriava_1997]: https://doi.org/10.21236/ada341512
[research_defenseacquisitionunivalexandriava_2000]: https://doi.org/10.21236/ada376404
[research_defenseacquisitionunivftbelvoirva_2007]: https://doi.org/10.21236/ada470388
[research_defenseacquisitionunivftbelvoirva_2010]: https://doi.org/10.21236/ada522556
[research_dehner_selamet_2021]: https://doi.org/10.3397/1/376925
[research_dehua_changyou_1993]: https://doi.org/10.21236/ada262374
[research_deitchman_1953]: https://doi.org/10.2514/8.2659
[research_deitchman_1954]: https://doi.org/10.2514/8.2924
[research_delaurier_1980]: https://doi.org/10.2514/3.57906
[research_demarchi_haning_1978]: https://doi.org/10.21236/ada060326
[research_dement_1990]: https://doi.org/10.21236/ada231970
[research_demina_volkov_1982]: https://doi.org/10.1007/bf01151166
[research_demir_gorguluarslan_2023]: https://doi.org/10.1007/s00158-023-03557-1
[research_denamiel_huan_2021]: https://doi.org/10.3389/fmars.2021.650279
[research_deng_li_2026]: https://doi.org/10.1016/j.ast.2026.111642
[research_departmentofdefensewashingtondc_1997]: https://doi.org/10.21236/ada330041
[research_departmentoftheairforcewashingtondc_1980]: https://doi.org/10.21236/ada097782
[research_departmentoftheairforcewashingtondc_1994]: https://doi.org/10.21236/ada277389
[research_departmentoftheairforcewashingtondc_1995]: https://doi.org/10.21236/ada291992
[research_departmentoftheairforcewashingtondc_2000]: https://doi.org/10.21236/ada374468
[research_departmentoftheairforcewashingtondc_2000_b]: https://doi.org/10.21236/ada374433
[research_departmentoftheairforcewashingtondc_2000_c]: https://doi.org/10.21236/ada374994
[research_departmentofthearmywashingtondc_1990]: https://doi.org/10.21236/ada218768
[research_departmentofthearmywashingtondc_1995]: https://doi.org/10.21236/ada292109
[research_departmentofthearmywashingtondc_1995_b]: https://doi.org/10.21236/ada294294
[research_departmentofthearmywashingtondc_1996]: https://doi.org/10.21236/ada306691
[research_departmentofthearmywashingtondc_1998]: https://doi.org/10.21236/ada338470
[research_departmentofthearmywashingtondc_2000]: https://doi.org/10.21236/ada373921
[research_departmentofthearmywashingtondc_2000_b]: https://doi.org/10.21236/ada374462
[research_departmentofthenavywashingtondc_1985]: https://doi.org/10.21236/ada155657
[research_departmentofthenavywashingtondc_1988]: https://doi.org/10.21236/ada197654
[research_departmentofthenavywashingtondc_1991]: https://doi.org/10.21236/ada232593
[research_desai_viswanathan_1977]: https://doi.org/10.2514/3.44585
[research_design_and_2024]: https://doi.org/10.31534/engmod.2024.2.ri.03v
[research_desyatnik_2015]: https://doi.org/10.1615/tsagiscij.v46.i7.50
[research_devarajan_kapania_2020]: https://doi.org/10.1016/j.compstruct.2020.111881
[research_devarajan_kapania_2022]: https://doi.org/10.1016/j.ast.2022.107350
[research_development_of_1975]: https://doi.org/10.1108/eb035217
[research_development_of_2016]: https://doi.org/10.21152/1750-9548.10.1.53
[research_development_testing_1970]: https://doi.org/10.1108/eb034695
[research_devletian_devincent_1988]: https://doi.org/10.21236/ada203519
[research_dewa_park_2018]: https://doi.org/10.3390/met8020103
[research_deyoungjohn_1950]: https://ntrs.nasa.gov/citations/19930082673
[research_dghim_ferchichi_2018]: https://doi.org/10.1016/j.expthermflusci.2018.05.011
[research_diamantidou_hosain_2022]: https://doi.org/10.3390/su14031731
[research_dias_2023]: https://doi.org/10.2514/1.c037252
[research_dibianchi_orra_2018]: https://doi.org/10.2514/1.c034277
[research_dickeyrobertr_1959]: https://ntrs.nasa.gov/citations/19980231999
[research_dicus_1975]: https://doi.org/10.1016/0010-4485(75)90046-9
[research_diekmann_2019]: https://doi.org/10.2514/1.c034910
[research_diesel_engine_2022]: https://doi.org/10.46632/jemm/8/3/4
[research_dieterreich_josefwimbauer_1975]: https://ntrs.nasa.gov/citations/19750013149
[research_diggins_1951]: https://doi.org/10.21236/ad0895227
[research_dimarco_jacob_2023]: https://doi.org/10.1016/j.ast.2023.108333
[research_dincer_sarioglu_2015]: https://doi.org/10.7763/ijmmm.2015.v3.157
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
[research_dobosbubno_hartsook_1977]: https://doi.org/10.21236/ada062008
[research_dodds_vahdati_2015]: https://doi.org/10.1115/1.4028558
[research_dodds_vahdati_2015_b]: https://doi.org/10.1115/1.4028557
[research_doe_2002]: https://doi.org/10.21236/ada420718
[research_doelling_bolt_1961]: https://doi.org/10.21236/ad0403730
[research_doggettrobertvjr_soistmanndavidl_1989]: https://ntrs.nasa.gov/citations/19890010723
[research_dong_2019]: https://doi.org/10.2514/1.i010684
[research_dong_choi_2020]: https://doi.org/10.1007/s00348-020-03023-4
[research_dong_choi_2022]: https://doi.org/10.1017/jfm.2022.451
[research_dong_he_2025]: https://doi.org/10.3390/aerospace12020073
[research_dong_huang_2015]: https://doi.org/10.2514/1.c032764
[research_dong_liu_2025]: https://doi.org/10.1115/1.4069059
[research_dong_sun_2015]: https://doi.org/10.1115/1.4030492
[research_dong_sun_2018]: https://doi.org/10.1115/1.4039707
[research_dong_wang_2026]: https://doi.org/10.2514/1.j066254
[research_donlancj_1976]: https://ntrs.nasa.gov/citations/19770022128
[research_dowell_ventres_1970]: https://doi.org/10.2514/3.5858
[research_drivercornelius_1958]: https://ntrs.nasa.gov/citations/19980232000
[research_du_2026]: https://doi.org/10.3390/pr14040719
[research_du_gao_2018]: https://doi.org/10.1360/n092017-00203
[research_du_liu_2023]: https://doi.org/10.1016/j.cja.2023.02.005
[research_du_zhang_2025]: https://doi.org/10.37965/jdmd.2025.889
[research_duan_laima_2020]: https://doi.org/10.1016/j.jweia.2020.104356
[research_duan_laima_2021]: https://doi.org/10.1016/j.jweia.2020.104500
[research_duan_wan_2026]: https://doi.org/10.3390/aerospace13010096
[research_duan_zhao_2026]: https://doi.org/10.2514/1.j066092
[research_duda_2016]: https://doi.org/10.1016/j.ast.2016.01.015
[research_duddy_landucci_2020]: https://doi.org/10.22594/dau.20-855.27.04
[research_duffy_1968]: https://doi.org/10.21236/ad0678493
[research_duffy_shattuck_1975]: https://doi.org/10.21236/ada013834
[research_duffy_shattuck_1975_b]: https://doi.org/10.21236/ada015064
[research_duganjfjr_1972]: https://ntrs.nasa.gov/citations/19720048461
[research_dugas_1986]: https://doi.org/10.21236/ada171418
[research_dunham_1962]: https://doi.org/10.2514/8.9442
[research_duran_fasanella_2015]: https://doi.org/10.1016/j.compstruct.2014.12.065
[research_durmus_2021]: https://doi.org/10.1108/aeat-02-2021-0038
[research_dvirnyk_pavlenko_2019]: https://doi.org/10.3390/aerospace6120132
[research_dymacek_jary_2024]: https://doi.org/10.3390/ma17204984
[research_ebied_hamada_2018]: https://doi.org/10.1016/j.matchar.2018.03.004
[research_ebrahimi_salari_2015]: https://doi.org/10.1016/j.compstruct.2015.03.023
[research_edwards_2010]: https://doi.org/10.21236/ada547418
[research_edwardssherman_hikidokatsumi_1953]: https://ntrs.nasa.gov/citations/19930087843
[research_effect_of_2023]: https://doi.org/10.1063/5.0146900
[research_effect_of_2023_b]: https://doi.org/10.47176/jafm.16.03.1449
[research_effect_of_2024]: https://doi.org/10.47176/jafm.17.12.2645
[research_effect_of_2026]: https://doi.org/10.29271/jcpsp.2026.04.476
[research_effects_of_2024]: https://doi.org/10.53797/fphj.v3i1.3.2024
[research_effiom_abam_2017]: https://doi.org/10.1080/23311916.2017.1368115
[research_egan_shadowen_1979]: https://doi.org/10.2514/3.58573
[research_egesoy_2022]: https://doi.org/10.38021/asbid.1200559
[research_eggers_1961]: https://doi.org/10.21236/ad0256165
[research_egorov_1958]: https://doi.org/10.1016/0021-8928(58)90081-9
[research_eiband_2005]: https://doi.org/10.21236/ada441760
[research_eisenhut_bender_2025]: https://doi.org/10.3390/aerospace12050401
[research_elliott_1968]: https://doi.org/10.1093/qjmam/21.1.77
[research_ellis_brownstein_1974]: https://doi.org/10.2514/3.60331
[research_emmons_pearson_1955]: https://doi.org/10.1115/1.4014389
[research_emmons_pearson_1955_b]: https://doi.org/10.1115/1.4014393
[research_englar_1975]: https://doi.org/10.2514/3.59824
[research_englertgeraldw_oberyleonardj_1952]: https://ntrs.nasa.gov/citations/19930090601
[research_epstein_1954]: https://doi.org/10.21236/ad0037709
[research_ercan_akin_2022]: https://doi.org/10.1108/aeat-11-2021-0326
[research_erceg_miletic_2016]: https://doi.org/10.31382/eqol201601011e
[research_erich_1980]: https://doi.org/10.21236/ada090597
[research_esau_2024]: https://doi.org/10.51644/ldvj3253
[research_esenweinfredt_schuellercarlf_1952]: https://ntrs.nasa.gov/citations/19930087893
[research_etjahjadi_dagustina_2019]: https://doi.org/10.18502/keg.v4i3.5878
[research_eulrich_mesiah_1974]: https://doi.org/10.21236/ada021994
[research_evaluation_of_2024]: https://doi.org/10.47176/jafm.17.3.2150
[research_evans_chamblee_1966]: https://doi.org/10.21236/ad0628775
[research_evansalisonb_1991]: https://ntrs.nasa.gov/citations/19910010772
[research_evansdg_debogdance_1974]: https://ntrs.nasa.gov/citations/19740020647
[research_eversman_2016]: https://doi.org/10.1177/1475472x16642131
[research_evran_2019]: https://doi.org/10.2339/politeknik.498684
[research_evvardjohnc_1947]: https://ntrs.nasa.gov/citations/19930082018
[research_experimental_determination_2018]: https://doi.org/10.4467/2353737xct.18.125.8900
[research_experimental_study_2020]: https://doi.org/10.20431/2454-8693.0601001
[research_experimental_study_2022]: https://doi.org/10.47176/jafm.15.02.33220
[research_eyvazian_zhang_2023]: https://doi.org/10.1016/j.compstruct.2022.116358
[research_ezrokhi_khoreva_2018]: https://doi.org/10.24108/0118.0001360
[research_faisal_mazni_2018]: https://doi.org/10.1088/1757-899x/319/1/012066
[research_falaakh_kim_2020]: https://doi.org/10.1080/09603409.2020.1742526
[research_faltin_beneda_2023]: https://doi.org/10.32560/rk.2023.3.7
[research_fan_du_2025]: https://doi.org/10.1115/1.4068876
[research_fan_li_2026]: https://doi.org/10.1115/1.4072311
[research_fan_liu_2024]: https://doi.org/10.1063/5.0235393
[research_fan_wang_2021]: https://doi.org/10.1016/j.matchar.2021.111412
[research_fan_xu_2022]: https://doi.org/10.3390/machines10111033
[research_fan_xu_2026]: https://doi.org/10.1007/s11630-026-2309-4
[research_fan_xu_2026_b]: https://doi.org/10.1115/1.4070987
[research_fang_sun_2023]: https://doi.org/10.3390/aerospace10020141
[research_fang_sun_2023_b]: https://doi.org/10.2514/1.j062482
[research_fang_wang_2023]: https://doi.org/10.1016/j.ast.2023.108612
[research_fang_zhang_2022]: https://doi.org/10.4028/www.scientific.net/kem.905.14
[research_fang_zheng_2020]: https://doi.org/10.1016/j.ast.2020.106146
[research_farahani_daliri_2019]: https://doi.org/10.1016/j.ast.2019.02.002
[research_farahani_mahdavi_2019]: https://doi.org/10.1016/j.ast.2019.05.014
[research_farney_fleharty_1969]: https://doi.org/10.2307/1378361
[research_farr_1976]: https://doi.org/10.2514/3.58627
[research_farrer_1969]: https://doi.org/10.1111/j.1745-493x.1969.tb00108.x
[research_faulders_1960]: https://doi.org/10.2514/8.8676
[research_feiler_conrad_1976]: https://doi.org/10.2514/3.58642
[research_feinreichb_deganio_1981]: https://ntrs.nasa.gov/citations/19820002170
[research_feleo_gamba_2025]: https://doi.org/10.2514/1.b39429
[research_felix_perron_2026]: https://doi.org/10.2514/1.c038369
[research_feng_chen_2025]: https://doi.org/10.1016/j.intermet.2025.108708
[research_feng_chen_2025_b]: https://doi.org/10.1016/j.jmrt.2025.03.076
[research_feng_tao_2020]: https://doi.org/10.1016/j.ijthermalsci.2020.106357
[research_feng_tianyu_2022]: https://doi.org/10.1007/s13369-022-06827-0
[research_fenwick_1966]: https://doi.org/10.21236/ad0737274
[research_fenwick_1967]: https://doi.org/10.21236/ad0738376
[research_fernandez_bronz_2026]: https://doi.org/10.2514/1.c038553
[research_fernandodelimapaulo_2015]: https://doi.org/10.18483/irjsci.86
[research_ferrero_2020]: https://doi.org/10.3390/aerospace7030032
[research_ferriantonio_nuccilouism_1946]: https://ntrs.nasa.gov/citations/19930093800
[research_ferriantonio_nuccilouism_1951]: https://ntrs.nasa.gov/citations/19930083137
[research_fett_1971]: https://doi.org/10.2514/3.44306
[research_ficht_1979]: https://doi.org/10.21236/ada071051
[research_figat_2017]: https://doi.org/10.1108/aeat-01-2017-0047
[research_figat_kwiek_2021]: https://doi.org/10.1108/aeat-05-2020-0085
[research_filimonov_1972]: https://doi.org/10.1016/0021-8928(72)90108-6
[research_findikyan_duke_1966]: https://doi.org/10.21236/ad0681038
[research_fine_1959]: https://doi.org/10.1080/14786435908233372
[research_fine_weertman_1983]: https://doi.org/10.21236/ada135956
[research_finnie_1961]: https://doi.org/10.1115/1.3658952
[research_finsgar_2017]: https://doi.org/10.1149/ma2017-03/1/171
[research_fisher_1977]: https://doi.org/10.1093/milmed/142.2.165
[research_fisherlewisr_williamsjamesl_1958]: https://ntrs.nasa.gov/citations/19980232008
[research_fitzsimmons_mckinnon_1981]: https://doi.org/10.2514/3.57553
[research_flanaganmichaelj_1992]: https://ntrs.nasa.gov/citations/19930004476
[research_fleeter_mcclure_1974]: https://doi.org/10.1121/1.1919886
[research_fleeter_mcclure_1975]: https://doi.org/10.2514/3.59853
[research_flow_field_2020]: https://doi.org/10.47176/jafm.13.06.31428
[research_flow_structure_2023]: https://doi.org/10.1063/5.0151556
[research_formentini_bouissiere_2022]: https://doi.org/10.1016/j.jii.2022.100327
[research_forward_1970]: https://doi.org/10.2307/20634400
[research_fostergeraldv_fitzpatrickjamese_1948]: https://ntrs.nasa.gov/citations/19930085540
[research_fostergv_robinsonrb_1961]: https://ntrs.nasa.gov/citations/19650014316
[research_foustjw_1979]: https://ntrs.nasa.gov/citations/19790008738
[research_fox_1969]: https://doi.org/10.1093/imamat/5.4.373
[research_fox_fuchs_1978]: https://doi.org/10.1520/jte10944j
[research_fraiser_1960]: https://doi.org/10.2514/8.8575
[research_franciscusl_1972]: https://ntrs.nasa.gov/citations/19730006301
[research_franciscuslc_lezbergea_1963]: https://ntrs.nasa.gov/citations/19630026662
[research_franciscusleoc_1987]: https://ntrs.nasa.gov/citations/19870014193
[research_franck_dillard_2006]: https://doi.org/10.21236/ada534750
[research_franck_lewis_2012]: https://doi.org/10.21236/ada584635
[research_francois_probst_2021]: https://doi.org/10.2514/1.c036273
[research_fresconi_celmins_2014]: https://doi.org/10.21236/ada593328
[research_frey_2014]: https://doi.org/10.21236/ada622072
[research_friendel_sakamotogm_1978]: https://ntrs.nasa.gov/citations/19790004885
[research_frohnapfel_toddlowe_2018]: https://doi.org/10.1115/1.4039425
[research_fu_chen_2019]: https://doi.org/10.1016/j.ijmecsci.2019.105055
[research_fu_fu_2021]: https://doi.org/10.1080/00051144.2021.1990629
[research_fu_fu_2021_b]: https://doi.org/10.1080/21642583.2021.1888818
[research_fu_fu_2023]: https://doi.org/10.3390/sym15040880
[research_fujii_fujimori_2021]: https://doi.org/10.1299/jsmefed.2021.os11-01
[research_fujiwara_takagi_2019]: https://doi.org/10.2320/matertrans.m2018366
[research_fukusako_kiya_1971]: https://doi.org/10.1007/bf00413203
[research_fullerde_1967]: https://ntrs.nasa.gov/citations/19670024546
[research_furey_1983]: https://doi.org/10.21236/ada126456
[research_furukawa_yamada_2015]: https://doi.org/10.1299/jsmemecj.2015._j0520305-
[research_gabrieldavids_krebsrichardp_1953]: https://ntrs.nasa.gov/citations/19930087143
[research_gadeev_demakov_2017]: https://doi.org/10.4028/www.scientific.net/ssp.265.575
[research_gaglio_visone_2023]: https://doi.org/10.2514/1.a35532
[research_gahlot_singh_2019]: https://doi.org/10.1088/1742-6596/1240/1/012008
[research_galindo_climent_2022]: https://doi.org/10.3390/app12031751
[research_galkin_sergeev_1976]: https://doi.org/10.1007/bf01529858
[research_ganilova_cartmell_2021]: https://doi.org/10.1016/j.compstruct.2020.113159
[research_ganilova_cartmell_2022]: https://doi.org/10.1016/j.compstruct.2022.115423
[research_gansler_1972]: https://doi.org/10.1002/j.2161-4296.1972.tb01691.x
[research_gao_he_2026]: https://doi.org/10.1063/5.0322431
[research_gao_kong_2025]: https://doi.org/10.1016/j.eap.2025.08.040
[research_gao_li_2015]: https://doi.org/10.1115/1.4029101
[research_gao_liu_2017]: https://doi.org/10.3397/1/3773
[research_gao_wang_2024]: https://doi.org/10.1016/j.cognition.2024.105861
[research_gao_zhang_2026]: https://doi.org/10.47176/jafm.19.2.3660
[research_garciabenitez_cuernorejado_2016]: https://doi.org/10.1108/aeat-11-2014-0204
[research_garmillamanzano_fritzsche_2026]: https://doi.org/10.1007/s13272-026-00993-9
[research_gartling_1970]: https://doi.org/10.21236/ad0734154
[research_gates_1940]: https://doi.org/10.1108/eb030684
[research_gayton_2004]: https://doi.org/10.21236/ada424697
[research_ge_shang_2021]: https://doi.org/10.1088/1742-6596/1985/1/012037
[research_gebhard_1953]: https://doi.org/10.21236/ad0015832
[research_gelderthomasf_1957]: https://ntrs.nasa.gov/citations/19930093764
[research_gellatly_bijlaard_1965]: https://doi.org/10.2514/3.43617
[research_gellatly_gallagher_1964]: https://doi.org/10.21236/ad0431959
[research_geng_yang_2025]: https://doi.org/10.1016/j.ast.2024.109778
[research_geng_zhang_2023]: https://doi.org/10.1016/j.msea.2023.144746
[research_george_perlmutter_1964]: https://doi.org/10.21236/ad0608185
[research_gergin_colak_2022]: https://doi.org/10.20491/isarder.2022.1431
[research_gerken_1979]: https://doi.org/10.21236/ada132587
[research_gershbein_peigin_1979]: https://doi.org/10.1007/bf01409803
[research_ghaffarifarhad_2005]: https://ntrs.nasa.gov/citations/20050198856
[research_ghee_gonzalez_1999]: https://doi.org/10.21236/ada368657
[research_gibert_plestan_2018]: https://doi.org/10.1016/j.conengprac.2018.03.004
[research_gilinskym_gonoral_2003]: https://ntrs.nasa.gov/citations/20040053459
[research_gilinskymikhail_morganmorrish_2000]: https://ntrs.nasa.gov/citations/20010012156
[research_gillen_loth_2015]: https://doi.org/10.2514/1.b35610
[research_gillespiewarrenjr_1960]: https://ntrs.nasa.gov/citations/20040046997
[research_gilruthrr_whitemd_1941]: https://ntrs.nasa.gov/citations/19930091789
[research_ginermorency_wong_2022]: https://doi.org/10.1186/s42774-022-00129-7
[research_giuffre_ascione_2025]: https://doi.org/10.2514/1.c038093
[research_giuliano_2016]: https://doi.org/10.1016/j.mfglet.2016.08.003
[research_gliebe_1981]: https://doi.org/10.2514/3.57567
[research_gliebepr_1980]: https://ntrs.nasa.gov/citations/19800051808
[research_gliebepr_kerschenej_1979]: https://ntrs.nasa.gov/citations/19800014610
[research_gliszczynski_czechowski_2021]: https://doi.org/10.3390/ma14112928
[research_glorioso_1960]: https://doi.org/10.21236/ad0281801
[research_glossbb_1974]: https://ntrs.nasa.gov/citations/19740020361
[research_go_maqsood_2015]: https://doi.org/10.1016/j.ast.2015.01.009
[research_goldstein_2004]: https://doi.org/10.21236/ada430475
[research_goldstein_2006]: https://doi.org/10.21236/ada472644
[research_golombek_bustamante_2026]: https://doi.org/10.1007/s13272-026-00996-6
[research_golovin_sergievskii_1970]: https://doi.org/10.1007/bf00828368
[research_golubkin_1980]: https://doi.org/10.1007/bf01089616
[research_golubkin_1980_b]: https://doi.org/10.1007/bf01089658
[research_gomezrodriguez_sanchezcarmona_2019]: https://doi.org/10.1016/j.ast.2019.04.041
[research_gonzalo_garciavillalba_2025]: https://doi.org/10.1186/s42774-025-00205-8
[research_goodman_1949]: https://doi.org/10.2514/8.11808
[research_goodykoontzjh_dorschrg_1973]: https://ntrs.nasa.gov/citations/19730015332
[research_goodykoontzjh_olsenwa_1972]: https://ntrs.nasa.gov/citations/19730002285
[research_goodykoontzjh_wagnerjm_1973]: https://ntrs.nasa.gov/citations/19730012332
[research_goransonrfabian_1942]: https://ntrs.nasa.gov/citations/19930092510
[research_gorbovskoi_kazhan_2019]: https://doi.org/10.34759/vst-2019-4-7-16
[research_gordon_1960]: https://doi.org/10.1525/curh.1960.38.224.234
[research_gorelov_2023]: https://doi.org/10.3103/s1068799823020150
[research_gortongeraldc_1953]: https://ntrs.nasa.gov/citations/19930087622
[research_gortongeraldc_1954]: https://ntrs.nasa.gov/citations/19930089376
[research_gorunov_2020]: https://doi.org/10.1007/s11015-020-01005-9
[research_goto_nakayama_2021]: https://doi.org/10.1299/jsmehs.2021.58.g011
[research_gotovtsev_1972]: https://doi.org/10.1007/bf01209043
[research_goud_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1057
[research_goulos_otter_2021]: https://doi.org/10.1016/j.ast.2021.106533
[research_gowthaman_sathiyagnanam_2018]: https://doi.org/10.1016/j.aej.2017.08.011
[research_gozukara_ceylan_2024]: https://doi.org/10.3390/computation12080162
[research_graham_1969]: https://doi.org/10.21236/ad0859822
[research_graham_lagerstrom_1954]: https://doi.org/10.21236/ad0063453
[research_gray_1969]: https://doi.org/10.1243/pime_conf_1969_184_182_02
[research_gray_mader_2020]: https://doi.org/10.2514/1.c035845
[research_gray_martins_2018]: https://doi.org/10.1017/aer.2018.120
[research_gray_wright_1970]: https://doi.org/10.2514/3.44139
[research_grayjustins_madercharlesa_2017]: https://ntrs.nasa.gov/citations/20170001424
[research_greebler_suarez_1989]: https://doi.org/10.21236/ada208222
[research_greene_1955]: https://doi.org/10.21236/ad0086878
[research_greene_1956]: https://doi.org/10.21236/ad0092484
[research_greene_1957]: https://doi.org/10.21236/ad0132012
[research_greene_2020]: https://doi.org/10.4271/01-14-01-0001
[research_greer_2010]: https://doi.org/10.21236/ada537484
[research_gregorysjones_williammilholen_2020]: https://ntrs.nasa.gov/citations/20200003091
[research_gregorytj_wilcoxde_1970]: https://ntrs.nasa.gov/citations/19700064255
[research_greitzer_1972]: https://doi.org/10.2514/3.59027
[research_greitzer_1976]: https://doi.org/10.1115/1.3446138
[research_greitzer_1976_b]: https://doi.org/10.1115/1.3446139
[research_greitzer_1976_c]: https://doi.org/10.1115/1.3446143
[research_greitzer_1980]: https://doi.org/10.1115/1.3240634
[research_griffinroynjr_holzhausercurta_1958]: https://ntrs.nasa.gov/citations/19980228056
[research_grimshaw_pullan_2025]: https://doi.org/10.1115/1.4070355
[research_grin_1967]: https://doi.org/10.1007/bf01013719
[research_groeneweg_1977]: https://doi.org/10.1121/1.2016398
[research_gromov_larin_1982]: https://doi.org/10.1007/bf01091296
[research_gros_1963]: https://doi.org/10.21236/ad0436090
[research_grytsyshen_abramova_2025]: https://doi.org/10.26642/ppa-2025-1(11)-44-49
[research_gu_xu_2023]: https://doi.org/10.1016/j.ast.2022.108079
[research_guan_zhou_2019]: https://doi.org/10.1080/19942060.2019.1639216
[research_guderley_1987]: https://doi.org/10.21236/ada193773
[research_guderley_1988]: https://doi.org/10.21236/ada191408
[research_gueraiche_popov_2018]: https://doi.org/10.26467/2079-0619-2018-21-1-124-136
[research_guimaraes_lowe_2018]: https://doi.org/10.2514/1.b36422
[research_guimaraes_toddlowe_2018]: https://doi.org/10.1115/1.4039179
[research_gul_2015]: https://doi.org/10.11648/j.ijema.20150304.15
[research_gunaydin_dogu_2025]: https://doi.org/10.29137/ijerad.1602783
[research_guo_2023]: https://doi.org/10.15632/jtam-pl/174960
[research_guo_gao_2022]: https://doi.org/10.1515/tjj-2022-0016
[research_guo_hu_2021]: https://doi.org/10.1007/s11630-021-1483-7
[research_guo_huang_2025]: https://doi.org/10.1016/j.measurement.2025.116782
[research_guo_liu_2025]: https://doi.org/10.1016/j.ast.2025.110290
[research_guo_luo_2025]: https://doi.org/10.1016/j.ast.2024.109891
[research_guo_mao_2022]: https://doi.org/10.1080/19942060.2022.2072955
[research_guo_tian_2021]: https://doi.org/10.1016/j.jallcom.2021.159497
[research_guo_zhang_2024]: https://doi.org/10.3390/aerospace12010010
[research_guopengyu_xuezhiliang_2019]: https://doi.org/10.3788/aos201939.1211004
[research_gupta_rajput_2015]: https://doi.org/10.14429/dsj.65.7200
[research_gupta_ramkumar_2015]: https://doi.org/10.12783/fae.2015.0401.02
[research_gurbuz_acarer_2022]: https://doi.org/10.21205/deufmd.2022247222
[research_gurbuz_hatunoglu_2022]: https://doi.org/10.17261/pressacademia.2022.1546
[research_gururaj_morris_2025]: https://doi.org/10.1103/1qq8-s6bz
[research_gutierrezalvarez_bisagni_2021]: https://doi.org/10.3390/aerospace8020056
[research_haas_karanian_1981]: https://doi.org/10.2514/3.57819
[research_hackman_richardson_1964]: https://doi.org/10.2514/3.43555
[research_hah_2018]: https://doi.org/10.1115/1.4041133
[research_hah_2022]: https://doi.org/10.1115/1.4055678
[research_hale_1973]: https://doi.org/10.21236/ad0757197
[research_hall_greitzer_2017]: https://doi.org/10.1115/1.4035631
[research_hall_greitzer_2022]: https://doi.org/10.1115/1.4055645
[research_hall_greitzer_2022_b]: https://doi.org/10.1115/1.4054035
[research_hallcharlesf_heitmeyerjohnc_1951]: https://ntrs.nasa.gov/citations/19930086624
[research_halliwell_1980]: https://doi.org/10.2514/3.57905
[research_halwas_aggarwal_2019]: https://doi.org/10.2514/1.c035093
[research_halwas_aggarwal_2019_b]: https://doi.org/10.2514/1.c035481
[research_hamaguchi_sakata_2020]: https://doi.org/10.38036/jgpp.11.4_13
[research_hamid_hammouda_2017]: https://doi.org/10.21608/asat.2017.22803
[research_han_han_2024]: https://doi.org/10.1063/5.0196415
[research_han_jia_2025]: https://doi.org/10.1364/ol.565204
[research_han_seo_2016]: https://doi.org/10.3740/mrsk.2016.26.7.370
[research_hanazaki_yamazaki_2024]: https://doi.org/10.3390/aerospace11010064
[research_hancock_1959]: https://doi.org/10.2514/8.8168
[research_hancock_1959_b]: https://doi.org/10.1017/s0001925900001487
[research_hancock_1960]: https://doi.org/10.2514/8.8377
[research_hancockjp_1985]: https://ntrs.nasa.gov/citations/19870001433
[research_hansen_1972]: https://doi.org/10.1016/0022-3115(72)90066-9
[research_hansen_jorgensen_1981]: https://doi.org/10.1115/1.3240796
[research_hao_jiang_2022]: https://doi.org/10.1007/s00339-022-05687-7
[research_hao_liu_2024]: https://doi.org/10.1016/j.tsep.2024.102516
[research_haque_asrar_2016]: https://doi.org/10.1007/bf03404719
[research_hardie_holroyd_1979]: https://doi.org/10.1179/msc.1979.13.11.603
[research_harle_1979]: https://doi.org/10.1177/001083677901400103
[research_harman_1978]: https://doi.org/10.1115/1.3446305
[research_harmsworth_1961]: https://doi.org/10.21236/ad0268569
[research_harold_haefeli_1950]: https://doi.org/10.2514/8.1512
[research_harristm_beermanda_1983]: https://ntrs.nasa.gov/citations/19880004718
[research_harristm_beermanda_1984]: https://ntrs.nasa.gov/citations/19840059567
[research_harry_trobaugh_1966]: https://doi.org/10.21236/ad0641246
[research_hart_1956]: https://doi.org/10.21236/ad0108104
[research_hart_1968]: https://doi.org/10.2514/3.29502
[research_hart_1974]: https://doi.org/10.1049/ep.1974.0461
[research_hartley_furey_1965]: https://doi.org/10.21236/ad0626655
[research_hartmann_1968]: https://doi.org/10.2514/3.43978
[research_hasan_sachs_2018]: https://doi.org/10.1007/s13272-018-0309-0
[research_hasegawa_tabbone_2016]: https://doi.org/10.1016/j.neucom.2015.04.100
[research_hasellowelle_lankfordjohnl_1953]: https://ntrs.nasa.gov/citations/20050019413
[research_hashin_humphreys_1980]: https://doi.org/10.21236/ada089414
[research_haskins_1978]: https://doi.org/10.21236/ada056733
[research_hassall_2015]: https://doi.org/10.7717/peerj.1219
[research_haustein_kashi_2019]: https://doi.org/10.1063/1.5091602
[research_havko_kapali_2020]: https://doi.org/10.3390/plants9020172
[research_hawkings_1974]: https://doi.org/10.1016/s0022-460x(74)80007-6
[research_hawkinsje_kirklandfp_1976]: https://ntrs.nasa.gov/citations/19760017152
[research_hawkinsrichard_penlandjima_1997]: https://ntrs.nasa.gov/citations/19980008542
[research_hawks_1982]: https://doi.org/10.2514/3.44751
[research_hawthorne_mitchell_1978]: https://doi.org/10.1115/1.3446409
[research_hayasi_1965]: https://doi.org/10.2514/3.3372
[research_hayden_gillespie_2023]: https://doi.org/10.1115/1.4063709
[research_hayden_untaroiu_2021]: https://doi.org/10.1115/1.4052139
[research_hayeswcjr_sleemanwcjr_1959]: https://ntrs.nasa.gov/citations/19630010604
[research_haynes_yang_2023]: https://doi.org/10.1016/j.aei.2023.102149
[research_hazen_seckel_1950]: https://doi.org/10.21236/ada952420
[research_he_shi_2025]: https://doi.org/10.2514/1.c037918
[research_he_xie_2026]: https://doi.org/10.1016/j.ast.2025.110859
[research_he_zhang_2025]: https://doi.org/10.1063/5.0276968
[research_he_zhang_2026]: https://doi.org/10.1016/j.ast.2026.112271
[research_he_zhao_2025]: https://doi.org/10.3390/en18133417
[research_hebert_j_1973]: https://doi.org/10.21236/ad0766942
[research_heidelberglaurencej_halldavidg_1992]: https://ntrs.nasa.gov/citations/19930007516
[research_heidelberglaurencej_halldavidg_1993]: https://ntrs.nasa.gov/citations/19930040786
[research_heidmann_saule_1980]: https://doi.org/10.2514/3.57930
[research_heimerlgeorgej_hardrathherbertf_1965]: https://ntrs.nasa.gov/citations/20000011991
[research_hellemeier_2019]: https://doi.org/10.1515/peps-2019-0030
[research_helmbold_1958]: https://doi.org/10.21236/ad0209045
[research_heltsley_crosswy_1983]: https://doi.org/10.21236/ada129606
[research_hemalatha_mahalakshmi_2018]: https://doi.org/10.2298/tsci170817223h
[research_henderson_1965]: https://doi.org/10.1017/s0001925900003358
[research_herbst_krogull_1973]: https://doi.org/10.2514/3.60220
[research_herdiana_pinindriya_2024]: https://doi.org/10.4186/ej.2024.28.12.29
[research_hernandezgloria_woodrichardm_1994]: https://ntrs.nasa.gov/citations/19950003616
[research_herold_mahoney_1974]: https://doi.org/10.2307/421338
[research_hess_peng_2018]: https://doi.org/10.2514/1.c034497
[research_hewesdonalde_1950]: https://ntrs.nasa.gov/citations/20050028478
[research_hickeydavidh_1956]: https://ntrs.nasa.gov/citations/19930088539
[research_hickeydavidh_aoyagikiyoshi_1960]: https://ntrs.nasa.gov/citations/19980227096
[research_hickman_morris_2017]: https://doi.org/10.1155/2017/6329382
[research_high_temperature_high_1974]: https://doi.org/10.1016/0010-4361(74)90482-0
[research_higham_holley_1966]: https://doi.org/10.2307/3101879
[research_hildebrand_1963]: https://doi.org/10.21236/ad0423391
[research_hill_1971]: https://doi.org/10.2514/3.44264
[research_hill_defoe_2020]: https://doi.org/10.1115/1.4045464
[research_hilleraircraftcorppaloaltoca_1965]: https://doi.org/10.21236/ad0625821
[research_hilleraircraftcorppaloaltoca_1965_b]: https://doi.org/10.21236/ad0625823
[research_hilleraircraftcorppaloaltoca_1965_c]: https://doi.org/10.21236/ad0625822
[research_hillgc_bowlesjv_1976]: https://ntrs.nasa.gov/citations/19760026102
[research_hillier_1970]: https://doi.org/10.1017/s0001925900005394
[research_himeda_naka_2019]: https://doi.org/10.1299/jsmefed.2019.os1-21
[research_hinkle_tulkoff_2011]: https://doi.org/10.21236/ada552348
[research_hirsch_1998]: https://doi.org/10.21236/ada352323
[research_hitzel_osterhuber_2018]: https://doi.org/10.2514/1.c034473
[research_hobbs_1957]: https://doi.org/10.2514/8.3955
[research_hodderbk_1981]: https://ntrs.nasa.gov/citations/19810021546
[research_hodderbk_farquharbw_1981]: https://ntrs.nasa.gov/citations/19820030404
[research_hofflerkd_raodm_1986]: https://ntrs.nasa.gov/citations/19860017727
[research_hoffman_2020]: https://doi.org/10.1519/jsc.0000000000003867
[research_hoffmantr_2000]: https://ntrs.nasa.gov/citations/20050194574
[research_hogge_1969]: https://doi.org/10.21236/ad0692432
[research_hoh_mitchell_1983]: https://doi.org/10.21236/ada132857
[research_holdawaygeorgeh_lazzeronifranka_1959]: https://ntrs.nasa.gov/citations/19980223578
[research_holl_1975]: https://doi.org/10.1108/eb035216
[research_holmr_1974]: https://doi.org/10.1007/bf00449511
[research_holota_2020]: https://doi.org/10.32702/2307-2105-2020.4.72
[research_holroyd_hardie_1981]: https://doi.org/10.1016/0010-938x(81)90097-4
[research_holubik_1988]: https://doi.org/10.21236/ada194398
[research_hon_karpuk_2022]: https://doi.org/10.2478/tar-2022-0009
[research_honeycutt_1970]: https://doi.org/10.21236/ad0875636
[research_hongpeng_weiqiang_2016]: https://doi.org/10.1016/j.actaastro.2016.05.014
[research_hooper_whidden_1957]: https://doi.org/10.21236/ad0407619
[research_hopkinsej_1975]: https://ntrs.nasa.gov/citations/19750055435
[research_hord_lian_2015]: https://doi.org/10.1504/ijad.2015.074629
[research_horton_1954]: https://doi.org/10.1108/eb032421
[research_hortonelmera_loftinlaurencek_1951]: https://ntrs.nasa.gov/citations/19930092102
[research_hosseindokht_matas_2026]: https://doi.org/10.3390/app16104616
[research_hosseini_vaziryzanjany_2024]: https://doi.org/10.3390/aerospace11040273
[research_hou_wang_2017]: https://doi.org/10.1007/s11630-017-0916-9
[research_hou_zhou_2020]: https://doi.org/10.3390/app10134651
[research_hovelmann_breitsamter_2015]: https://doi.org/10.2514/1.c033014
[research_hovelmann_grawunder_2016]: https://doi.org/10.1016/j.ast.2015.12.023
[research_hribernik_kes_2021]: https://doi.org/10.1016/j.procs.2021.04.082
[research_hrubecky_1963]: https://doi.org/10.1007/bf03184628
[research_hsu_anderson_1961]: https://doi.org/10.2514/8.8910
[research_hu_2024]: https://doi.org/10.1088/1742-6596/2731/1/012048
[research_hu_li_2024]: https://doi.org/10.1016/j.ast.2024.109309
[research_hu_qian_2026]: https://doi.org/10.1016/j.measurement.2025.119024
[research_hu_qu_2023]: https://doi.org/10.1088/1742-6596/2478/8/082009
[research_hu_wang_2022]: https://doi.org/10.3390/electronics11030467
[research_hu_wang_2025]: https://doi.org/10.3390/aerospace12040346
[research_hu_yang_2021]: https://doi.org/10.1109/access.2021.3060426
[research_hu_zhao_2026]: https://doi.org/10.1016/j.ast.2026.112874
[research_huang_bu_2024]: https://doi.org/10.1016/j.jppr.2024.04.003
[research_huang_li_2022]: https://doi.org/10.1016/j.msea.2021.142570
[research_huang_lv_2025]: https://doi.org/10.1016/j.energy.2025.135239
[research_huang_sauzay_2021]: https://doi.org/10.1016/j.msea.2021.140953
[research_huang_tan_2016]: https://doi.org/10.1063/1.4971448
[research_huang_wang_2026]: https://doi.org/10.1016/j.ast.2026.112309
[research_huang_yao_2023]: https://doi.org/10.1063/5.0167136
[research_huang_yao_2024]: https://doi.org/10.1063/5.0182681
[research_huang_zhang_2019]: https://doi.org/10.1016/j.ast.2019.04.042
[research_hubble_smith_1979]: https://doi.org/10.21236/ada072743
[research_hube_1968]: https://doi.org/10.21236/ad0388036
[research_hughesdl_mackallkg_1984]: https://ntrs.nasa.gov/citations/19860015876
[research_hui_1975]: https://doi.org/10.1017/s0001925900007150
[research_hunn_1954]: https://doi.org/10.1017/s0001925900001128
[research_hunt_hunt_2021]: https://doi.org/10.2514/1.b38334
[research_huntley_1972]: https://doi.org/10.1017/s0001924000043104
[research_hunziker_1960]: https://doi.org/10.1007/bf01595402
[research_huppert_benser_1953]: https://doi.org/10.2514/8.2871
[research_hutchins_jones_1975]: https://doi.org/10.21236/ada955236
[research_hutchins_jr_1978]: https://doi.org/10.21236/ada062134
[research_hutchinson_lawrence_2021]: https://doi.org/10.1177/09544100211016952
[research_hwang_kuo_2018]: https://doi.org/10.1016/j.promfg.2018.07.222
[research_hwang_pi_1979]: https://doi.org/10.2514/3.58518
[research_ichikawa_koike_2021]: https://doi.org/10.1007/s00348-021-03198-4
[research_iekchanthy_burleyrichardr_1993]: https://ntrs.nasa.gov/citations/19930014929
[research_ignaczak_1978]: https://doi.org/10.1080/01495737808926939
[research_ignatkin_makeev_2016]: https://doi.org/10.3103/s1068799816010074
[research_imani_jahedmotlagh_2017]: https://doi.org/10.1080/21642583.2017.1367732
[research_imani_malekizade_2018]: https://doi.org/10.1080/00051144.2018.1498204
[research_imanishi_wang_2015]: https://doi.org/10.1149/ma2015-01/2/392
[research_influence_of_2017]: https://doi.org/10.15593/2224-9982/2017.49.02
[research_inger_zee_1978]: https://doi.org/10.2514/3.58442
[research_inglis_larke_1958]: https://doi.org/10.1243/pime_proc_1958_172_076_02
[research_ingraldianthonym_rerichardj_1991]: https://ntrs.nasa.gov/citations/19920033022
[research_initial_damage_2019]: https://doi.org/10.1299/jsmemecj.2019.j02334
[research_innisrobertc_quigleyherveyc_1961]: https://ntrs.nasa.gov/citations/20040008110
[research_iqbal_shabbir_2025]: https://doi.org/10.1016/j.mlwa.2025.100760
[research_irsyadlukman_agoesmoelyadi_2018]: https://doi.org/10.1088/1742-6596/1005/1/012050
[research_iseki_nicholas_1979]: https://doi.org/10.1007/bf00772731
[research_ishihara_suzuki_2020]: https://doi.org/10.1299/jsmeth.2020.55.166_paper
[research_islam_fermin_2015]: https://doi.org/10.1017/s1431927615002238
[research_isugiyama_1976]: https://doi.org/10.1299/kikai1938.42.3186
[research_ito_dhaene_2016]: https://doi.org/10.2514/1.c033588
[research_ivanov_2022]: https://doi.org/10.54708/19926502_2022_2619559
[research_jablon_1972]: https://doi.org/10.1016/0375-9601(72)90195-8
[research_jackjohnr_1951]: https://ntrs.nasa.gov/citations/19930086899
[research_jacobs_1973]: https://doi.org/10.2307/1958810
[research_jacocks_kneile_1975]: https://doi.org/10.21236/ada004104
[research_jafari_nikolaidis_2018]: https://doi.org/10.3390/electronics7110314
[research_jakubowski_2019]: https://doi.org/10.2478/kones-2019-0033
[research_jamesfconnors_georgeawise_1957]: https://ntrs.nasa.gov/citations/19930089639
[research_jameslfelder_michaelttong_2022]: https://ntrs.nasa.gov/citations/20210016661
[research_janzen_precourt_1989]: https://doi.org/10.21236/ada213513
[research_jaquetbyronm_1951]: https://ntrs.nasa.gov/citations/19930086998
[research_jardin_colonius_2018]: https://doi.org/10.1098/rsif.2017.0933
[research_jarvinen_1973]: https://doi.org/10.2514/3.44352
[research_jassim_2016]: https://doi.org/10.1504/pcfd.2016.078755
[research_jayarani_narmadhai_2024]: https://doi.org/10.2478/msr-2024-0024
[research_jeffs_lancaster_2015]: https://doi.org/10.1016/j.msea.2014.12.085
[research_jelev_keane_2019]: https://doi.org/10.2514/1.c034897
[research_jenkins_marks_1975]: https://doi.org/10.21236/ada008965
[research_jenkinsjeraldm_kuhlalberte_1977]: https://ntrs.nasa.gov/citations/20020086520
[research_jenkinsjm_1979]: https://ntrs.nasa.gov/citations/19790012818
[research_jenney_1935]: https://doi.org/10.2514/8.126
[research_jeong_choi_2015]: https://doi.org/10.6108/kspe.2015.19.3.029
[research_jeyaraj_liscouethanke_2022]: https://doi.org/10.3390/aerospace9120791
[research_ji_hu_2022]: https://doi.org/10.3390/en15145246
[research_ji_huang_2024]: https://doi.org/10.1016/j.ast.2024.109416
[research_ji_kim_2023]: https://doi.org/10.3390/aerospace10040365
[research_ji_yu_2018]: https://doi.org/10.1088/1757-899x/435/1/012062
[research_ji_yuan_2021]: https://doi.org/10.3390/ma14051217
[research_jia_chen_2024]: https://doi.org/10.1049/icp.2024.3929
[research_jiandong_qiming_2021]: https://doi.org/10.23919/jsee.2021.000121
[research_jiang_li_2024]: https://doi.org/10.1007/s11071-024-10134-8
[research_jiang_liu_2026]: https://doi.org/10.1007/s44210-025-00077-z
[research_jiang_yao_2024]: https://doi.org/10.1063/5.0197991
[research_jiao_chang_2017]: https://doi.org/10.1016/j.actaastro.2016.10.027
[research_jie_zhibin_2017]: https://doi.org/10.2514/1.c034270
[research_jin_sun_2022]: https://doi.org/10.1016/j.cja.2021.06.013
[research_jin_tan_2023]: https://doi.org/10.1016/j.cja.2023.08.004
[research_jin_zhang_2023]: https://doi.org/10.1016/j.actaastro.2022.09.052
[research_jing_2018]: https://doi.org/10.3901/jme.2018.12.165
[research_joarder_2018]: https://doi.org/10.1007/s00193-018-0868-3
[research_johnsal_steffenfw_1970]: https://ntrs.nasa.gov/citations/19700022736
[research_johnson_henderson_1959]: https://doi.org/10.1108/eb033103
[research_johnson_henderson_1960]: https://doi.org/10.1108/eb033263
[research_johnson_lawing_1977]: https://doi.org/10.2514/3.44604
[research_johnson_wu_1975]: https://doi.org/10.1115/1.3447318
[research_johnsonhj_montoyaej_1973]: https://ntrs.nasa.gov/citations/19730015310
[research_johnsoniii_wu_1974]: https://doi.org/10.21236/ada017631
[research_jonathanalee_poshouchen_2005]: https://ntrs.nasa.gov/citations/20050237966
[research_jones_1972]: https://doi.org/10.2514/3.6568
[research_jones_1973]: https://doi.org/10.21236/ad0773559
[research_jones_medina_2016]: https://doi.org/10.1007/s00348-016-2143-7
[research_jones_placzankis_2016]: https://doi.org/10.21236/ad1012477
[research_jonesarthurl_flanaganmildredg_1947]: https://ntrs.nasa.gov/citations/19930082115
[research_jonesgwjr_unangstjr_1963]: https://ntrs.nasa.gov/citations/19630002604
[research_jonesjr_shrewsburygd_1968]: https://ntrs.nasa.gov/citations/19680026292
[research_jonesrobertt_1953]: https://ntrs.nasa.gov/citations/20050081861
[research_jonesrobertt_1956]: https://ntrs.nasa.gov/citations/19930092281
[research_jonesrt_1976]: https://ntrs.nasa.gov/citations/19760012011
[research_jordan_1973]: https://doi.org/10.2514/3.60285
[research_ju_deng_2022]: https://doi.org/10.1615/atomizspr.2022040171
[research_ju_sun_2020]: https://doi.org/10.1016/j.ast.2020.105941
[research_juknevicius_chong_2018]: https://doi.org/10.1016/j.jsv.2018.02.038
[research_jung_lee_2015]: https://doi.org/10.5139/jksas.2015.43.5.387
[research_jung_oh_2022]: https://doi.org/10.11627/jksie.2022.45.1.010
[research_justiciaalados_trezza_2026]: https://doi.org/10.58286/33934
[research_ka_2018]: https://doi.org/10.4172/2332-0796.1000267
[research_kaczorowski_skoczylas_2015]: https://doi.org/10.1515/afe-2015-0077
[research_kadir_beg_2019]: https://doi.org/10.1002/htj.21493
[research_kalkan_2024]: https://doi.org/10.36306/konjes.1332160
[research_kamani_mirzaee_2023]: https://doi.org/10.5829/ijee.2023.14.02.10
[research_kametani_kotake_2017]: https://doi.org/10.1103/physrevfluids.2.123904
[research_kaminski_witkowska_2018]: https://doi.org/10.3139/146.111616
[research_kan_muransky_2019]: https://doi.org/10.1016/j.ijpvp.2019.103974
[research_kananoja_kosonen_2025]: https://doi.org/10.1080/10242694.2025.2533753
[research_kanda_1982]: https://doi.org/10.1109/temc.1982.304040
[research_kang_kang_2024]: https://doi.org/10.6108/kspe.2024.28.6.001
[research_kang_li_2024]: https://doi.org/10.1080/17452759.2024.2382166
[research_kang_liang_2024]: https://doi.org/10.3390/aerospace11120992
[research_kaplan_1980]: https://doi.org/10.21236/ada089051
[research_kapoorkamlesh_andersonbernhardh_1994]: https://ntrs.nasa.gov/citations/19950004408
[research_kar_panda_2016]: https://doi.org/10.12989/amr.2016.5.4.205
[research_karabacak_turan_2020]: https://doi.org/10.1504/ijsa.2020.112087
[research_karimi_oboodi_2018]: https://doi.org/10.1007/s00231-018-2416-1
[research_karl_werner_2025]: https://doi.org/10.33737/jgpps/213325
[research_kasama_suzuki_2020]: https://doi.org/10.1299/jsmemecj.2020.j03135
[research_kase_mizoguchi_2020]: https://doi.org/10.1299/jsmemecj.2020.s05403
[research_kasozi_siddharthan_2015]: https://doi.org/10.1115/1.4029354
[research_katariya_panda_2016]: https://doi.org/10.1108/aeat-11-2013-0202
[research_katz_1971]: https://doi.org/10.2514/3.44296
[research_katz_2021]: https://doi.org/10.1016/j.infoecopol.2020.100883
[research_kawamura_karashima_1957]: https://doi.org/10.2322/jjsass1953.5.93
[research_kawamurat_chyuwj_1987]: https://ntrs.nasa.gov/citations/19870037658
[research_kawanabe_lei_2025]: https://doi.org/10.3390/aerospace12070625
[research_kawase_rona_2019]: https://doi.org/10.3390/fluids4020088
[research_kawase_rona_2019_b]: https://doi.org/10.3390/ijtpp4010005
[research_kaye_yeh_1955]: https://doi.org/10.2514/8.3454
[research_kayiran_2025]: https://doi.org/10.65773/came.1.1.24
[research_kayser_danberg_1974]: https://doi.org/10.2514/3.49559
[research_kayser_hillsamer_1960]: https://doi.org/10.21236/ad0318532
[research_kazula_hoschler_2020]: https://doi.org/10.1108/aeat-11-2019-0225
[research_kazula_hoschler_2021]: https://doi.org/10.1007/s13272-021-00520-y
[research_kazula_mischke_2019]: https://doi.org/10.1051/matecconf/201930402016
[research_kbab_haif_2023]: https://doi.org/10.59287/icpis.851
[research_kegels_skovgaardlykke_2025]: https://doi.org/10.21552/edseq/2026/1/10
[research_keller_hasan_2018]: https://doi.org/10.2514/1.c035065
[research_kelleymarkw_tolhurstwilliamhjr_1955]: https://ntrs.nasa.gov/citations/19930093777
[research_kellymarkw_andersonsethb_1958]: https://ntrs.nasa.gov/citations/19930092354
[research_kennedy_gerhardt_1972]: https://doi.org/10.2307/1985673
[research_khademi_ikeda_2019]: https://doi.org/10.1007/s11837-019-03598-2
[research_khaleghi_2015]: https://doi.org/10.1016/j.ast.2014.12.004
[research_khan_hasan_2021]: https://doi.org/10.1115/1.4049677
[research_khan_tariq_2026]: https://doi.org/10.1016/j.ijthermalsci.2025.110440
[research_khatri_sinha_2023]: https://doi.org/10.61653/joast.v68i4.2016.367
[research_khazaali_fereshtehsaniee_2018]: https://doi.org/10.1007/s40430-018-1003-1
[research_khobragade_gustavsson_2024]: https://doi.org/10.1007/s00193-024-01192-3
[research_khobragade_kumar_2022]: https://doi.org/10.1007/s00193-022-01091-5
[research_khobragade_unnikrishnan_2021]: https://doi.org/10.2514/1.j060591
[research_kholyavko_1971]: https://doi.org/10.1007/bf01019800
[research_khoroshun_soltanov_1977]: https://doi.org/10.1007/bf00901811
[research_khoroshun_soltanov_1978]: https://doi.org/10.1007/bf00883729
[research_kiani_2017]: https://doi.org/10.1080/01495739.2017.1336742
[research_kida_miyai_1978]: https://doi.org/10.1017/s0001925900008477
[research_kidwell_1963]: https://doi.org/10.21236/ad0440406
[research_kierda_powersbg_1972]: https://ntrs.nasa.gov/citations/19730024215
[research_kigotho_bodylski_2022]: https://doi.org/10.2514/1.c036582
[research_kikkawa_1955]: https://doi.org/10.2170/jjphysiol.5.167
[research_kilimtzidis_kostopoulos_2023]: https://doi.org/10.1007/s00158-023-03600-1
[research_kim_2024]: https://doi.org/10.18703/silj.2024.12.31.2.151
[research_kim_choi_2022]: https://doi.org/10.2514/1.b38484
[research_kim_kim_2015]: https://doi.org/10.1016/j.measurement.2015.06.002
[research_kim_kim_2015_b]: https://doi.org/10.1016/j.ast.2015.09.007
[research_kim_kim_2026]: https://doi.org/10.1016/j.measurement.2025.119228
[research_kim_kwon_2015]: https://doi.org/10.2514/1.b35742
[research_kim_lee_2022]: https://doi.org/10.5139/jksas.2022.50.5.297
[research_kim_park_2026]: https://doi.org/10.6112/kscfe.2026.31.2.084
[research_kim_ramlim_2023]: https://doi.org/10.1016/j.matdes.2023.111761
[research_kimhyoungjin_kumanotakayasu_2011]: https://ntrs.nasa.gov/citations/20110011992
[research_kimura_imai_2018]: https://doi.org/10.1299/jsmefed.2018.os9-4
[research_kinardtima_harrisbrendaw_1995]: https://ntrs.nasa.gov/citations/19950016768
[research_kingrw_schuermanja_1976]: https://ntrs.nasa.gov/citations/19760019074
[research_kinslermartinr_1958]: https://ntrs.nasa.gov/citations/19930092395
[research_kirk_barrack_1969]: https://doi.org/10.2514/3.44017
[research_kishi_kanazaki_2022]: https://doi.org/10.2514/1.c036422
[research_kiss_spakovszky_2018]: https://doi.org/10.1115/1.4041290
[research_kjames_kim_2022]: https://doi.org/10.1016/j.ast.2022.107982
[research_kjames_suryan_2021]: https://doi.org/10.1016/j.ast.2021.106795
[research_klannga_barthrl_1984]: https://ntrs.nasa.gov/citations/19850056914
[research_klecknerharoldf_1945]: https://ntrs.nasa.gov/citations/19930092870
[research_klecknerharoldf_1946]: https://ntrs.nasa.gov/citations/19930081790
[research_kleinvladislav_1999]: https://ntrs.nasa.gov/citations/19990100653
[research_klimchik_chablat_2015]: https://doi.org/10.1016/j.euromechsol.2014.12.010
[research_klimowitch_1978]: https://doi.org/10.21236/ada061148
[research_klujber_1973]: https://doi.org/10.2514/3.60264
[research_knight_1991]: https://doi.org/10.21236/ada235867
[research_knobbe_2002]: https://doi.org/10.21236/ada405721
[research_knowles_tu_2017]: https://doi.org/10.1016/j.polymertesting.2016.12.013
[research_kobayashi_1974]: https://doi.org/10.2514/3.49247
[research_kobayashi_1984]: https://doi.org/10.21236/ada143252
[research_kolb_2020]: https://doi.org/10.1002/au.30235
[research_kolnsberg_1979]: https://doi.org/10.1115/1.3446465
[research_kolom_1969]: https://doi.org/10.2514/3.44079
[research_konar_mahesh_1974]: https://doi.org/10.21236/ada002320
[research_kong_kim_2016]: https://doi.org/10.4028/www.scientific.net/msf.857.271
[research_kong_li_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001470
[research_kong_park_2018]: https://doi.org/10.1007/s12239-018-0037-9
[research_kong_su_2026]: https://doi.org/10.1016/j.ast.2026.111722
[research_kong_sun_2026]: https://doi.org/10.1590/jatm.v18.1429
[research_kong_zhou_2020]: https://doi.org/10.3390/app10155198
[research_kong_zhou_2022]: https://doi.org/10.1049/cth2.12413
[research_kong_zhou_2023]: https://doi.org/10.1093/jcde/qwad020
[research_kopasakisgeorge_connollyjosephw_2012]: https://ntrs.nasa.gov/citations/20120018047
[research_kopasakisgeorge_connollyjosephw_2012_b]: https://ntrs.nasa.gov/citations/20120000915
[research_kopzon_1958]: https://doi.org/10.1016/0021-8928(58)90040-6
[research_korn_1974]: https://doi.org/10.2514/3.60390
[research_kornienko_shmanenkov_1981]: https://doi.org/10.1007/bf01094829
[research_kornreich_1992]: https://doi.org/10.21236/ada252486
[research_koster_2004]: https://doi.org/10.21236/ada423699
[research_kosuge_ito_1982]: https://doi.org/10.1115/1.3227344
[research_kothari_1971]: https://doi.org/10.1016/0022-3115(71)90167-x
[research_kothari_1973]: https://doi.org/10.1016/0022-3115(73)90191-8
[research_kotov_ruleva_2018]: https://doi.org/10.1088/1742-6596/1009/1/012038
[research_kovacs_csik_2023]: https://doi.org/10.1016/j.tsep.2023.101906
[research_kowalski_goraj_2021]: https://doi.org/10.1108/aeat-12-2020-0287
[research_kowilliaml_fieldsrogera_1987]: https://ntrs.nasa.gov/citations/19880001007
[research_koyyalamudi_nagpurwala_2016]: https://doi.org/10.1155/2016/2371524
[research_kozakevich_stroh_2022]: https://doi.org/10.1007/s11665-022-06935-w
[research_kozakiewicz_adamczyk_2025]: https://doi.org/10.3390/en18082064
[research_kozlov_1966]: https://doi.org/10.1007/bf00895613
[research_kraiko_tilliaeva_1973]: https://doi.org/10.1016/0021-8928(73)90088-9
[research_kraiko_tkalenko_1967]: https://doi.org/10.1007/bf01019533
[research_kramer_hall_2026]: https://doi.org/10.1115/1.4072203
[research_kramerbe_potterdy_1966]: https://ntrs.nasa.gov/citations/19670016544
[research_krashchenko_statsenko_1981]: https://doi.org/10.1007/bf00762177
[research_krause_1981]: https://doi.org/10.2514/3.50927
[research_krause_1997]: https://doi.org/10.21236/ada397873
[research_krawczyk_paul_2024]: https://doi.org/10.2514/1.c037420
[research_krenkel_salzman_1968]: https://doi.org/10.2514/3.43962
[research_kretov_2021]: https://doi.org/10.1108/aeat-11-2020-0256
[research_krishnaswamy_nath_1982]: https://doi.org/10.1016/0045-7930(82)90017-2
[research_krivenyuk_tsvilyuk_1971]: https://doi.org/10.1007/bf01533595
[research_krosche_heinze_2015]: https://doi.org/10.2514/1.c032876
[research_krupa_2019]: https://doi.org/10.1017/aer.2019.53
[research_krushnaraokotteda_mittal_2016]: https://doi.org/10.2514/1.b35699
[research_kuchinka_1966]: https://doi.org/10.2514/3.43727
[research_kucuk_tuncer_2024]: https://doi.org/10.1007/s11081-023-09877-x
[research_kuhlmann_sauer_2019]: https://doi.org/10.1016/j.procir.2019.01.009
[research_kuhn_1979]: https://doi.org/10.21236/ada073099
[research_kumar_2022]: https://doi.org/10.26706/jtfs.3.1.20211202
[research_kumar_capolungo_2022]: https://doi.org/10.1016/j.ijplas.2022.103411
[research_kumar_darsigunta_2021]: https://doi.org/10.1016/j.matpr.2021.03.663
[research_kumar_gaur_2017]: https://doi.org/10.31142/ijtsrd5779
[research_kumar_pradeep_2022]: https://doi.org/10.1115/1.4053955
[research_kumar_sastri_2025]: https://doi.org/10.13189/cea.2025.131310
[research_kurkov_soeder_1975]: https://doi.org/10.2514/3.59818
[research_kuzmich_sekundov_1975]: https://doi.org/10.1007/bf01023266
[research_kuzmin_2024]: https://doi.org/10.1007/s42401-023-00268-9
[research_kwee_dewaele_2019]: https://doi.org/10.1007/s40194-019-00732-1
[research_kwiatkowski_sieradzki_2022]: https://doi.org/10.2478/tar-2022-0001
[research_kwiek_2019]: https://doi.org/10.1108/aeat-08-2018-0231
[research_ladiaapsarihasibuan_agussulastio_2025]: https://doi.org/10.31258/jassi.4.2.112-122
[research_lahnsteiner_2022]: https://doi.org/10.1016/j.jtherbio.2022.103256
[research_lai_findley_1980]: https://doi.org/10.21236/ada095410
[research_lai_kamaruddin_2018]: https://doi.org/10.1088/1757-899x/370/1/012055
[research_lamarje_1986]: https://ntrs.nasa.gov/citations/19860052312
[research_lamarjohne_1987]: https://ntrs.nasa.gov/citations/19880003937
[research_lamberthh_mizukamim_1999]: https://ntrs.nasa.gov/citations/19990110638
[research_lampropoulos_sarris_2025]: https://doi.org/10.3844/jastsp.2025.1.11
[research_lapin_crookshanks_1952]: https://doi.org/10.2514/8.2336
[research_lapin_sharov_1974]: https://doi.org/10.1007/bf01092647
[research_lappas_ikenaga_2019]: https://doi.org/10.3390/aerospace6100107
[research_large_1981]: https://doi.org/10.1017/s0001924000030062
[research_larrabeeee_1975]: https://ntrs.nasa.gov/citations/19760003917
[research_lavi_1967]: https://doi.org/10.2514/3.43808
[research_lawley_koczak_1984]: https://doi.org/10.21236/ada141780
[research_lawley_koczak_1985]: https://doi.org/10.21236/ada170697
[research_lawrence_1953]: https://doi.org/10.2514/8.2724
[research_leahy_michaelb_1995]: https://doi.org/10.21236/ada327933
[research_lecuyer_morrison_1971]: https://doi.org/10.2514/3.59131
[research_lee_duh_2017]: https://doi.org/10.1016/j.vacuum.2017.05.009
[research_lee_kim_2024]: https://doi.org/10.2514/1.c037495
[research_lee_ko_2018]: https://doi.org/10.1115/1.4039232
[research_lee_lee_2019]: https://doi.org/10.1007/s42405-019-00175-4
[research_lee_lim_2018]: https://doi.org/10.5139/jksas.2018.46.6.452
[research_lee_lim_2022]: https://doi.org/10.2514/1.c036214
[research_lee_nam_2023]: https://doi.org/10.5139/jksas.2023.51.6.363
[research_lee_sanders_2002]: https://doi.org/10.21236/ada398914
[research_lee_yee_2024]: https://doi.org/10.2514/1.c037225
[research_leebj_lioumayfun_2018]: https://ntrs.nasa.gov/citations/20190002760
[research_leebyungjoon_lioumayfun_2018]: https://ntrs.nasa.gov/citations/20180005439
[research_leebyungjoon_lioumayfun_2019]: https://ntrs.nasa.gov/citations/20190031843
[research_leeja_1998]: https://ntrs.nasa.gov/citations/19990019483
[research_leejonathana_2003]: https://ntrs.nasa.gov/citations/20040035597
[research_leejonathana_chenposhou_2002]: https://ntrs.nasa.gov/citations/20020060119
[research_leejonathana_munafopaulm_2002]: https://ntrs.nasa.gov/citations/20030001009
[research_legros_lutoshkina_2018]: https://doi.org/10.1016/j.ijthermalsci.2018.02.011
[research_lehtinen_zeller_1972]: https://doi.org/10.1016/0005-1098(72)90027-1
[research_lehtinenb_zellerjr_1971]: https://ntrs.nasa.gov/citations/19720004248
[research_lehtinenb_zellerjr_1978]: https://ntrs.nasa.gov/citations/19780015081
[research_leitner_1986]: https://doi.org/10.21236/ada522372
[research_leknys_arjomandi_2018]: https://doi.org/10.1016/j.expthermflusci.2018.03.001
[research_lemaysp_batillsm_1988]: https://ntrs.nasa.gov/citations/19880053508
[research_leng_feng_2024]: https://doi.org/10.1063/5.0188386
[research_lengyelkampmann_karboujian_2024]: https://doi.org/10.1007/s13272-024-00717-x
[research_leslie_1952]: https://doi.org/10.1093/qjmam/5.3.292
[research_leslie_perry_1954]: https://doi.org/10.1098/rspa.1954.0198
[research_levinsky_thommen_1968]: https://doi.org/10.21236/ad0680969
[research_levylionelljr_1959]: https://ntrs.nasa.gov/citations/19980232076
[research_levylionelljr_yoshikawakennethk_1959]: https://ntrs.nasa.gov/citations/19980228237
[research_lewis_1976]: https://doi.org/10.2514/3.44525
[research_lewis_1998]: https://doi.org/10.21236/ada346210
[research_li_chen_2024]: https://doi.org/10.1016/j.ijplas.2024.103892
[research_li_chu_2024]: https://doi.org/10.1063/5.0236969
[research_li_ding_2023]: https://doi.org/10.1016/j.ast.2023.108667
[research_li_dong_2021]: https://doi.org/10.1016/j.cja.2021.02.005
[research_li_dong_2022]: https://doi.org/10.3390/aerospace9100628
[research_li_dong_2025]: https://doi.org/10.3390/met15060677
[research_li_dong_2025_b]: https://doi.org/10.1007/s42405-025-01036-z
[research_li_du_2019]: https://doi.org/10.1016/j.ast.2018.12.018
[research_li_du_2020]: https://doi.org/10.1016/j.ast.2020.105886
[research_li_du_2020_b]: https://doi.org/10.1016/j.ast.2019.105554
[research_li_fang_2024]: https://doi.org/10.3390/e26121036
[research_li_geiselhart_2021]: https://doi.org/10.2514/1.j059237
[research_li_geiselhart_2022]: https://doi.org/10.2514/1.c036656
[research_li_geiselhart_2026]: https://doi.org/10.2514/1.c038747
[research_li_hou_2024]: https://doi.org/10.2478/amns-2024-1078
[research_li_kedeng_2023]: https://doi.org/10.1088/1742-6596/2527/1/012059
[research_li_li_2024]: https://doi.org/10.3390/aerospace11070536
[research_li_liu_2022]: https://doi.org/10.1016/j.ast.2022.107685
[research_li_liu_2024]: https://doi.org/10.2514/1.j064454
[research_li_liu_2024_b]: https://doi.org/10.1115/1.4065617
[research_li_lu_2024]: https://doi.org/10.3390/aerospace11020141
[research_li_lyu_2022]: https://doi.org/10.3390/aerospace9110658
[research_li_pan_2015]: https://doi.org/10.1016/j.applthermaleng.2014.09.071
[research_li_pan_2023]: https://doi.org/10.3390/aerospace10050436
[research_li_qiao_2023]: https://doi.org/10.3390/aerospace10070603
[research_li_qu_2025]: https://doi.org/10.1063/5.0270314
[research_li_soskin_2019]: https://doi.org/10.1109/access.2019.2915917
[research_li_sun_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000901
[research_li_sun_2022]: https://doi.org/10.1016/j.jmst.2022.01.010
[research_li_sun_2025]: https://doi.org/10.1016/j.fmre.2024.03.018
[research_li_tian_2021]: https://doi.org/10.3390/cryst11060646
[research_li_wang_2023]: https://doi.org/10.3390/ma16103609
[research_li_xia_2024]: https://doi.org/10.1016/j.cja.2024.07.007
[research_li_xu_2015]: https://doi.org/10.1016/j.proeng.2014.12.707
[research_li_xu_2024]: https://doi.org/10.3390/aerospace11070514
[research_li_xu_2024_b]: https://doi.org/10.1016/j.applthermaleng.2024.122409
[research_li_zhao_2026]: https://doi.org/10.1016/j.ast.2025.110962
[research_li_zheng_2021]: https://doi.org/10.1016/j.ast.2021.106752
[research_li_zheng_2023]: https://doi.org/10.1016/j.ast.2023.108373
[research_li_zhou_2021]: https://doi.org/10.1016/j.ast.2021.107107
[research_li_zhu_2022]: https://doi.org/10.3390/en15103612
[research_li_zhu_2023]: https://doi.org/10.1016/j.ast.2023.108530
[research_li_zhu_2024]: https://doi.org/10.1115/1.4064421
[research_li_zhu_2024_b]: https://doi.org/10.1016/j.ast.2024.109007
[research_lian_xiong_2025]: https://doi.org/10.1088/1742-6596/3085/1/012011
[research_lichtensteinjacobh_1952]: https://ntrs.nasa.gov/citations/19930092137
[research_lieu_1964]: https://doi.org/10.21236/ad0448477
[research_liewkh_uripe_2005]: https://ntrs.nasa.gov/citations/20050207438
[research_likhachev_2024]: https://doi.org/10.22363/2313-0660-2024-24-1-92-106
[research_lin_bai_2022]: https://doi.org/10.1155/2022/1139648
[research_lin_li_2025]: https://doi.org/10.1049/icp.2024.2995
[research_lin_liu_2021]: https://doi.org/10.1038/s41598-021-94261-x
[research_lin_shao_2020]: https://doi.org/10.1016/j.ast.2020.105785
[research_lin_zhang_2022]: https://doi.org/10.1088/1742-6596/2285/1/012016
[research_lin_zong_2026]: https://doi.org/10.1063/5.0334699
[research_linehan_mohseni_2020]: https://doi.org/10.1038/s41598-020-63181-7
[research_linek_chytilek_2016]: https://doi.org/10.13060/00380288.2016.52.5.275
[research_ling_1970]: https://doi.org/10.2514/3.44119
[research_linnell_1963]: https://doi.org/10.21236/ad0408661
[research_liu_cao_2017]: https://doi.org/10.1016/j.ijheatmasstransfer.2017.04.001
[research_liu_cao_2023]: https://doi.org/10.1016/j.energy.2022.125662
[research_liu_chen_2021]: https://doi.org/10.1016/j.ijfatigue.2021.106446
[research_liu_chu_2024]: https://doi.org/10.3390/aerospace11070541
[research_liu_chu_2025]: https://doi.org/10.1007/s42405-025-00934-6
[research_liu_du_2025]: https://doi.org/10.1115/1.4069738
[research_liu_du_2026]: https://doi.org/10.1016/j.cja.2026.104346
[research_liu_feng_2023]: https://doi.org/10.1088/1742-6596/2489/1/012005
[research_liu_gao_2018]: https://doi.org/10.1109/access.2018.2814958
[research_liu_huang_2023]: https://doi.org/10.1007/s11630-023-1780-4
[research_liu_jiang_2022]: https://doi.org/10.1155/2022/9288966
[research_liu_kang_2022]: https://doi.org/10.1016/j.actaastro.2022.01.030
[research_liu_li_2016]: https://doi.org/10.1016/j.ast.2016.10.014
[research_liu_li_2022]: https://doi.org/10.1049/icp.2022.1963
[research_liu_li_2023]: https://doi.org/10.3390/aerospace10120989
[research_liu_vo_2024]: https://doi.org/10.1115/1.4065288
[research_liu_wang_2021]: https://doi.org/10.3390/app11199272
[research_liu_yu_2025]: https://doi.org/10.1007/s11518-025-5699-z
[research_liu_zhang_2018]: https://doi.org/10.1108/aeat-04-2017-0100
[research_liu_zhang_2022]: https://doi.org/10.1051/matecconf/202235501017
[research_liu_zhu_2015]: https://doi.org/10.1007/s00193-015-0605-0
[research_liu_zhu_2024]: https://doi.org/10.1109/jsen.2023.3335858
[research_liu_zhu_2025]: https://doi.org/10.1109/tim.2025.3547093
[research_liu_zhu_2025_b]: https://doi.org/10.1016/j.measurement.2024.115985
[research_liu_zhu_2026]: https://doi.org/10.1109/tim.2026.3666019
[research_lock_1957]: https://doi.org/10.1017/s0022112057000385
[research_lockwoodve_1966]: https://ntrs.nasa.gov/citations/19660023730
[research_lomakin_fedorenko_2024]: https://doi.org/10.1134/s0025654424606190
[research_lomaxharvard_1957]: https://ntrs.nasa.gov/citations/19930092292
[research_lomaxharvard_heasletmaxa_1956]: https://ntrs.nasa.gov/citations/19930092279
[research_longest_1964]: https://doi.org/10.1093/milmed/129.5.432
[research_lopez_baldomir_2017]: https://doi.org/10.1007/s00158-017-1740-2
[research_lou_harrison_2022]: https://doi.org/10.1115/1.4055866
[research_lourenco_shih_1996]: https://doi.org/10.21236/ada310244
[research_loveless_boswell_1954]: https://doi.org/10.1108/eb032412
[research_lovelljcalvin_wilsonherbertajr_1947]: https://ntrs.nasa.gov/citations/19930093794
[research_lowe_1967]: https://doi.org/10.21236/ad0823139
[research_lowe_2020]: https://doi.org/10.1108/aeat-11-2018-0285
[research_lu_li_2025]: https://doi.org/10.1063/5.0288892
[research_lu_wang_2025]: https://doi.org/10.1177/09576509251317280
[research_lu_yang_2019]: https://doi.org/10.1016/j.ast.2019.06.015
[research_lu_zhang_2017]: https://doi.org/10.1016/j.applthermaleng.2016.11.070
[research_lu_zhang_2022]: https://doi.org/10.1016/j.measurement.2022.111434
[research_lu_zhang_2025]: https://doi.org/10.3390/math13030380
[research_lucas_1978]: https://doi.org/10.21236/adb028240
[research_luce_jr_1949]: https://doi.org/10.21236/ada278113
[research_ludwig_1979]: https://doi.org/10.21236/ada077704
[research_lukyanov_hoang_2024]: https://doi.org/10.3390/drones8080388
[research_lundet_1977]: https://ntrs.nasa.gov/citations/19780005535
[research_luning_bangqin_2021]: https://doi.org/10.1088/1757-899x/1081/1/012047
[research_luo_2018]: https://doi.org/10.1016/j.ast.2018.01.043
[research_luo_meng_2026]: https://doi.org/10.1016/j.ast.2026.112752
[research_luo_tao_2024]: https://doi.org/10.1061/jaeeez.aseng-5388
[research_luo_wei_2020]: https://doi.org/10.3390/en13010217
[research_lv_wang_2025]: https://doi.org/10.1016/j.ast.2025.110544
[research_lv_zhang_2022]: https://doi.org/10.3390/math10101664
[research_lv_zhang_2022_b]: https://doi.org/10.3390/math10163022
[research_lyga_1990]: https://doi.org/10.21236/ada227483
[research_lyu_1963]: https://doi.org/10.1016/0041-5553(63)90508-1
[research_lyubimov_2024]: https://doi.org/10.1134/s2070048224010071
[research_lyubimov_potekhina_2016]: https://doi.org/10.1134/s0018151x16050187
[research_m_mukherjee_2017]: https://doi.org/10.1016/j.ast.2017.01.009
[research_m_v_2017]: https://doi.org/10.14445/23488360/ijme-v4i6p106
[research_ma_2021]: https://doi.org/10.1016/j.tsep.2020.100787
[research_ma_colon_2021]: https://doi.org/10.1093/cybsec/tyab013
[research_ma_cui_2018]: https://doi.org/10.2514/1.j056858
[research_ma_jia_2022]: https://doi.org/10.1016/j.engfailanal.2021.105918
[research_ma_karpuk_2022]: https://doi.org/10.1016/j.ast.2022.107395
[research_ma_li_2025]: https://doi.org/10.1063/5.0278832
[research_ma_li_2026]: https://doi.org/10.1016/j.dt.2026.07.017
[research_ma_lu_2025]: https://doi.org/10.1016/j.paerosci.2025.101082
[research_ma_wang_2025]: https://doi.org/10.1063/5.0254496
[research_ma_zhang_2022]: https://doi.org/10.2514/1.c036559
[research_macdermott_dix_1965]: https://doi.org/10.21236/ad0467446
[research_macdermott_dix_1966]: https://doi.org/10.21236/ad0643963
[research_macmanus_chiereghin_2017]: https://doi.org/10.2514/1.j054905
[research_maeda_1961]: https://doi.org/10.2320/matertrans1960.2.44
[research_maekawa_higashi_1978]: https://doi.org/10.1299/kikai1938.44.2304
[research_maghsoudi_vaziry_2020]: https://doi.org/10.1016/j.cja.2019.12.002
[research_magrini_benini_2023]: https://doi.org/10.1016/j.ast.2022.108048
[research_magrini_benini_2026]: https://doi.org/10.1063/5.0329926
[research_mahjouri_shabani_2023]: https://doi.org/10.1108/aeat-07-2022-0197
[research_mahlmeister_ishimoto_1955]: https://doi.org/10.21236/ad0093337
[research_mahorter_robertg_1961]: https://doi.org/10.21236/ad0266590
[research_maikapar_1959]: https://doi.org/10.1016/0021-8928(59)90104-2
[research_maikapar_1966]: https://doi.org/10.1016/0021-8928(66)90071-2
[research_maise_1970]: https://doi.org/10.2514/3.44202
[research_makarov_2019]: https://doi.org/10.24108/mathm.0618.0000164
[research_makiralphl_1959]: https://ntrs.nasa.gov/citations/19980228300
[research_maksimovich_karpinos_1977]: https://doi.org/10.1007/bf01528510
[research_malashenko_vashchilo_1975]: https://doi.org/10.1007/bf01522859
[research_malicki_malecha_2023]: https://doi.org/10.3390/en16227590
[research_malikov_miltsov_2019]: https://doi.org/10.18372/2310-5461.40.13278
[research_mallik_kapania_2015]: https://doi.org/10.2514/1.c033096
[research_malmuth_1966]: https://doi.org/10.2514/3.3483
[research_malmuth_1966_b]: https://doi.org/10.2514/3.55271
[research_malonemichaelb_peaveycharlesc_1999]: https://ntrs.nasa.gov/citations/20000044629
[research_malvi_roy_2021]: https://doi.org/10.1007/s11666-021-01189-9
[research_mamonova_soudakov_2019]: https://doi.org/10.1088/1742-6596/1268/1/012067
[research_mansfield_1967]: https://doi.org/10.1017/s000192400005418x
[research_manthena_kedar_2017]: https://doi.org/10.1080/01495739.2017.1402669
[research_mao_liu_2016]: https://doi.org/10.1177/0954410016630565
[research_mao_liu_2017]: https://doi.org/10.3390/en10081153
[research_mao_zhang_2025]: https://doi.org/10.56028/aetr.15.1.2134.2025
[research_maples_1979]: https://doi.org/10.21236/ada069807
[research_margalida_joseph_2020]: https://doi.org/10.3390/ijtpp5030016
[research_margoliskenneth_1947]: https://ntrs.nasa.gov/citations/19930082080
[research_margoliskenneth_malvestutofranksjr_1958]: https://ntrs.nasa.gov/citations/19930084830
[research_marshall_1973]: https://doi.org/10.2514/3.60226
[research_marshallrt_1971]: https://ntrs.nasa.gov/citations/19710017526
[research_martensson_2021]: https://doi.org/10.3390/aerospace8030058
[research_martensson_billson_2024]: https://doi.org/10.1115/1.4065517
[research_martensson_billson_2024_b]: https://doi.org/10.1115/1.4063867
[research_martensson_lejon_2022]: https://doi.org/10.1017/aer.2022.28
[research_martin_1961]: https://doi.org/10.1088/0370-1328/78/6/349
[research_marty_castillon_2022]: https://doi.org/10.1115/1.4056090
[research_masaki_ogushi_2021]: https://doi.org/10.1088/1742-6596/1909/1/012081
[research_masilamani_suresh_2021]: https://doi.org/10.14704/web/v18si01/web18051
[research_masonwh_1983]: https://ntrs.nasa.gov/citations/19840007047
[research_masonwh_siclarimj_1983]: https://ntrs.nasa.gov/citations/19830035489
[research_mathausereldone_deveikiswilliamd_1955]: https://ntrs.nasa.gov/citations/19930093819
[research_mathausereldone_deveikiswilliamd_1957]: https://ntrs.nasa.gov/citations/19930092300
[research_mathematical_modeling_2018]: https://doi.org/10.15593/perm.mech/eng.2018.3.09
[research_mathur_1969]: https://doi.org/10.1017/s0001924000052477
[research_matlak_racz_2017]: https://doi.org/10.1016/j.scispo.2017.06.001
[research_matrangagenej_armstrongneila_1959]: https://ntrs.nasa.gov/citations/19980235626
[research_matsuda_matsuno_2026]: https://doi.org/10.2514/1.c038130
[research_matsumoto_sekiya_1975]: https://doi.org/10.1299/kikai1938.41.736
[research_matzdorf_kane_1999]: https://doi.org/10.21236/ada375739
[research_mauch_oldakowski_1980]: https://doi.org/10.21236/ada089067
[research_mays_1971]: https://doi.org/10.2514/3.44258
[research_mazhul_2020]: https://doi.org/10.1134/s0869864320040046
[research_mazurov_2015]: https://doi.org/10.1615/tsagiscij.v46.i6.40
[research_mazurov_2019]: https://doi.org/10.1615/tsagiscij.2019030084
[research_mazzawyrs_banksga_1976]: https://ntrs.nasa.gov/citations/19760014117
[research_mazzawyrs_banksga_1977]: https://ntrs.nasa.gov/citations/19770009079
[research_mcanally_iii_1971]: https://doi.org/10.21236/ad0725593
[research_mcanally_williamj_1970]: https://doi.org/10.21236/ad0875953
[research_mcaulayje_abdelwahabm_1972]: https://ntrs.nasa.gov/citations/19720019364
[research_mccormick_1959]: https://doi.org/10.2514/8.8022
[research_mcdaniel_bull_1995]: https://doi.org/10.21236/ada302481
[research_mcdaniel_bull_1998]: https://doi.org/10.21236/ada339007
[research_mcdaniel_cooper_1999]: https://doi.org/10.21236/ada372637
[research_mcdonald_fox_1971]: https://doi.org/10.2514/3.6456
[research_mcdonnellaircraftcorpstlouismo_1963]: https://doi.org/10.21236/ad0417153
[research_mcdonough_1953]: https://doi.org/10.1093/milmed/113.2.83
[research_mckeehen_cord_1997]: https://doi.org/10.21236/ada327802
[research_mclean_stacey_1970]: https://doi.org/10.1177/002029407000300902
[research_mclemorehclyde_1958]: https://ntrs.nasa.gov/citations/19980231988
[research_mclemorehclyde_petersonjohnbjr_1960]: https://ntrs.nasa.gov/citations/19980228270
[research_mcmillinsn_woodrm_1986]: https://ntrs.nasa.gov/citations/19860053087
[research_mcnicol_2014]: https://doi.org/10.21236/ada603849
[research_mcnicol_2014_b]: https://doi.org/10.21236/ada610317
[research_mcnicol_wu_2014]: https://doi.org/10.21236/ada609472
[research_mcqueen_1976]: https://doi.org/10.1243/jmes_jour_1976_018_038_02
[research_mechanism_of_2021]: https://doi.org/10.47176/jafm.14.06.32577
[research_mechanism_study_2023]: https://doi.org/10.1063/5.0149263
[research_mehar_mishra_2021]: https://doi.org/10.1115/1.4050934
[research_melickhcjr_1973]: https://ntrs.nasa.gov/citations/19730012966
[research_meneesgenep_boydjohnw_1959]: https://ntrs.nasa.gov/citations/19980228046
[research_menegozzo_benini_2020]: https://doi.org/10.1115/1.4048174
[research_meng_fan_2018]: https://doi.org/10.1177/0954410018787137
[research_meng_ma_2025]: https://doi.org/10.1016/j.polymer.2025.128266
[research_mennellr_1970]: https://ntrs.nasa.gov/citations/19710025637
[research_menon_2020]: https://doi.org/10.36872/lepi/v51i1/301050
[research_menon_sanjayshivam_2023]: https://doi.org/10.1016/j.matpr.2022.08.231
[research_menon_suresh_2022]: https://doi.org/10.1108/heswbl-01-2022-0014
[research_merchant_radhakrishnan_2017]: https://doi.org/10.1088/1757-899x/225/1/012298
[research_merkli_1975]: https://doi.org/10.21236/ada033630
[research_merkli_1976]: https://doi.org/10.2514/3.61352
[research_merrillwalterc_delaatjohnc_1991]: https://ntrs.nasa.gov/citations/19910045152
[research_metzger_rienzi_2022]: https://doi.org/10.3390/ma15155270
[research_meyer_1938]: https://doi.org/10.21236/ad0608024
[research_meyer_1959]: https://doi.org/10.2514/8.4717
[research_mi_yao_2017]: https://doi.org/10.3390/met7060226
[research_miao_guan_2026]: https://doi.org/10.1016/j.ast.2026.112758
[research_michellga_1971]: https://ntrs.nasa.gov/citations/19720002377
[research_miele_1954]: https://doi.org/10.2514/8.3207
[research_mieleangelo_1955]: https://ntrs.nasa.gov/citations/19930093841
[research_mihalik_keane_2022]: https://doi.org/10.2514/1.c035944
[research_mikhail_1979]: https://doi.org/10.21236/ada076116
[research_mikhailov_mikhailova_2017]: https://doi.org/10.1016/j.proeng.2017.02.290
[research_miki_watanabe_2015]: https://doi.org/10.2322/jjsass.63.265
[research_milenkovicbabic_2018]: https://doi.org/10.1108/aeat-04-2017-0104
[research_milenkovicbabic_samardzic_2017]: https://doi.org/10.1108/aeat-02-2016-0026
[research_miles_1953]: https://doi.org/10.1017/s0001925900000901
[research_military_presence_2025]: https://doi.org/10.31249/ape/2025.04.08
[research_millerds_pittmanjl_1983]: https://ntrs.nasa.gov/citations/19830047131
[research_mills_1978]: https://doi.org/10.1115/1.3443471
[research_min_xian_2024]: https://doi.org/10.1108/mmms-11-2023-0376
[research_minervino_vitagliano_2016]: https://doi.org/10.1108/aeat-03-2015-0082
[research_mineta_saijo_2022]: https://doi.org/10.1016/j.jallcom.2022.164938
[research_ming_wu_2023]: https://doi.org/10.1016/j.ast.2023.108578
[research_minjb_reddytsr_2018]: https://ntrs.nasa.gov/citations/20180002213
[research_minnicino_gray_2009]: https://doi.org/10.21236/ada506416
[research_mintint_2018]: https://doi.org/10.47119/ijrp10020112019484
[research_mireles_ficke_2019]: https://doi.org/10.1109/tifs.2019.2912551
[research_mirzaei_kiani_2015]: https://doi.org/10.1016/j.ast.2015.09.011
[research_mitsuyasu_1956]: https://doi.org/10.2322/jjsass1953.4.131
[research_miura_kohzu_2020]: https://doi.org/10.1002/lom3.10367
[research_miura_yamashita_2021]: https://doi.org/10.1115/1.4050439
[research_miyashita_sugihara_2025]: https://doi.org/10.1063/5.0250348
[research_mizobata_mio_2024]: https://doi.org/10.3390/aerospace11090777
[research_mjamhuri_nizar_2024]: https://doi.org/10.66187/jipski.v2i1.251
[research_moeckelwe_1955]: https://ntrs.nasa.gov/citations/19930084178
[research_moeckelwe_evanspjjr_1951]: https://ntrs.nasa.gov/citations/19930090411
[research_moens_2022]: https://doi.org/10.3390/aerospace10010007
[research_moffat_healzer_1978]: https://doi.org/10.1115/1.3450487
[research_mohammad_2021]: https://doi.org/10.36909/jer.v9i1.7152
[research_moin_lele_1998]: https://doi.org/10.21236/ada343835
[research_moirou_sanders_2023]: https://doi.org/10.1016/j.paerosci.2023.100897
[research_mokotoff_arnson_2026]: https://doi.org/10.2514/1.c038452
[research_molana_khodaparast_2020]: https://doi.org/10.1007/s40435-020-00681-4
[research_monkova_monka_2023]: https://doi.org/10.3390/aerospace10040361
[research_montanojw_1967]: https://ntrs.nasa.gov/citations/19670045542
[research_moon_2025]: https://doi.org/10.6108/kspe.2025.29.4.055
[research_moon_2025_b]: https://doi.org/10.31691/kasl40.1.4
[research_moore_1973]: https://doi.org/10.21236/ad0756481
[research_moore_lueke_1974]: https://doi.org/10.1115/1.3438443
[research_moorhouse_jenkins_1975]: https://doi.org/10.2514/3.44474
[research_morgan_thomson_1961]: https://doi.org/10.2307/1983469
[research_morris_1986]: https://doi.org/10.21236/ada183371
[research_morton_1956]: https://doi.org/10.1108/eb032772
[research_moru_bo_2022]: https://doi.org/10.1016/j.ast.2022.108008
[research_mosca_sudhi_2024]: https://doi.org/10.2514/1.c037362
[research_mount_1965]: https://doi.org/10.2514/3.43670
[research_muchmorecbjr_1988]: https://ntrs.nasa.gov/citations/19880053479
[research_muehter_1974]: https://doi.org/10.21236/ada043526
[research_mugridge_1975]: https://doi.org/10.1016/s0022-460x(75)80059-9
[research_muir_arredondogaleana_2017]: https://doi.org/10.1098/rsos.170077
[research_mulgundsandeeps_1994]: https://ntrs.nasa.gov/citations/19940022793
[research_muller_gasko_1967]: https://doi.org/10.2514/3.43825
[research_muller_gasko_1967_b]: https://doi.org/10.2514/3.43842
[research_mungallrobertc_1948]: https://ntrs.nasa.gov/citations/19930082436
[research_munjulury_staack_2015]: https://doi.org/10.1007/s13272-015-0174-z
[research_munk_auld_2019]: https://doi.org/10.1007/s00158-019-02250-6
[research_muraida_grimes_1998]: https://doi.org/10.21236/ada362149
[research_murphypatrickc_kleinvladislav_2006]: https://ntrs.nasa.gov/citations/20060047570
[research_musa_huang_2024]: https://doi.org/10.1063/5.0239660
[research_mushkat_1979]: https://doi.org/10.1177/003231877903100202
[research_mushtaq_gaetani_2023]: https://doi.org/10.1063/5.0160706
[research_mushtaq_gaetani_2023_b]: https://doi.org/10.1115/1.4064135
[research_mushtaq_pini_2024]: https://doi.org/10.1115/1.4067242
[research_myerslawrencep_walshkevinr_1988]: https://ntrs.nasa.gov/citations/19880051520
[research_myokan_kubota_2020]: https://doi.org/10.2514/1.j058519
[research_na_2021]: https://doi.org/10.1504/ijpm.2021.10045018
[research_nagamatsu_workman_1960]: https://doi.org/10.2514/8.5173
[research_nagao_yoshida_2019]: https://doi.org/10.2322/astj.jsass-d-18-00007
[research_nagasaka_muroga_2019]: https://doi.org/10.1088/1741-4326/ab1c8f
[research_nageswararao_kushari_2020]: https://doi.org/10.2514/1.b37674
[research_nagler_2022]: https://doi.org/10.37394/232022.2022.2.14
[research_nagler_2026]: https://doi.org/10.1177/15485129261459679
[research_nakajima_yanagawa_1963]: https://doi.org/10.1021/j100797a028
[research_nam_mavris_2018]: https://doi.org/10.2514/1.c032099
[research_nandy_baag_2021]: https://doi.org/10.1016/j.jtherbio.2020.102829
[research_narayan_1975]: https://doi.org/10.1017/s0001925900007332
[research_narendhiran_2017]: https://doi.org/10.26808/rs.ed.i7v6.10
[research_naruse_ishii_2022]: https://doi.org/10.1299/transjsme.21-00357
[research_naseri_boroomand_2016]: https://doi.org/10.1007/s11630-016-0891-6
[research_navalprovinggrounddahlgrenva_1945]: https://doi.org/10.21236/ad0310024
[research_navalseasystemscommandwashingtondc_2010]: https://doi.org/10.21236/ada550109
[research_negaard_1979]: https://doi.org/10.21236/ada363019
[research_neitzel_hemsworth_1966]: https://doi.org/10.2514/3.43746
[research_nelmswpjr_baileyro_1974]: https://ntrs.nasa.gov/citations/19740020394
[research_nelsondp_1983]: https://ntrs.nasa.gov/citations/19830018545
[research_nelsondp_bresnahandl_1983]: https://ntrs.nasa.gov/citations/19830055105
[research_nelsonrobertl_welshclementj_1960]: https://ntrs.nasa.gov/citations/19980227964
[research_ness_1971]: https://doi.org/10.2514/3.44301
[research_neumark_1950]: https://doi.org/10.1108/eb031964
[research_neverlien_moe_2020]: https://doi.org/10.4173/mic.2020.2.1
[research_newsomerw_thomasjl_1986]: https://ntrs.nasa.gov/citations/19860017733
[research_newsomwilliamajr_tostilouisp_1959]: https://ntrs.nasa.gov/citations/19980228402
[research_ng_datta_2019]: https://doi.org/10.2514/1.c035218
[research_ng_willcox_2016]: https://doi.org/10.2514/1.c033352
[research_nganangelen_biezaddaniel_1996]: https://ntrs.nasa.gov/citations/19960041232
[research_nguyenlt_anglinel_1976]: https://ntrs.nasa.gov/citations/19760053944
[research_nicholas_pernak_2023]: https://doi.org/10.1016/j.applthermaleng.2023.120759
[research_nicholsmarkr_pendleyroberte_1952]: https://ntrs.nasa.gov/citations/19930086995
[research_nicolay_karpuk_2021]: https://doi.org/10.1016/j.ijhydene.2021.07.127
[research_nielsenjackn_kaattarigeorgee_1953]: https://ntrs.nasa.gov/citations/19930093732
[research_nielsenjn_1985]: https://ntrs.nasa.gov/citations/19850037607
[research_niewaldroyj_moulmartint_1950]: https://ntrs.nasa.gov/citations/19930086447
[research_nikitenko_2018]: https://doi.org/10.32652/olympic2018.3_5
[research_nimal_m_2019]: https://doi.org/10.37200/ijpr/v23i4/pr190166
[research_nisiyama_tanimura_1967]: https://doi.org/10.1299/kikai1938.33.182
[research_nithinjosephreddy_sathiskumar_2019]: https://doi.org/10.1088/2053-1591/ab220c
[research_niu_sui_2019]: https://doi.org/10.1016/j.jweia.2019.04.001
[research_niu_ye_2025]: https://doi.org/10.3390/app16010135
[research_noding_bertsch_2021]: https://doi.org/10.3390/aerospace8080210
[research_northropaircraftinchawthorneca_1952]: https://doi.org/10.21236/ad0024361
[research_northropaircraftinchawthorneca_1952_b]: https://doi.org/10.21236/ad0004591
[research_northropaircraftinchawthorneca_1953]: https://doi.org/10.21236/ad0013465
[research_northropaircraftinchawthorneca_1956]: https://doi.org/10.21236/ad0092134
[research_northropcorphawthornecanorairdiv_1964]: https://doi.org/10.21236/ad0605185
[research_northropcorphawthornecanorairdiv_1964_b]: https://doi.org/10.21236/ad0605186
[research_novakrc_1974]: https://ntrs.nasa.gov/citations/19740025954
[research_numerical_simulation_2020]: https://doi.org/10.36884/jafm.13.05.31018
[research_nussdorfertheodorej_oberyleonardj_1952]: https://ntrs.nasa.gov/citations/19930086890
[research_obeyleonardt_englertgeraldw_1952]: https://ntrs.nasa.gov/citations/19930094389
[research_ochonogor_akinlabi_2017]: https://doi.org/10.1016/j.matpr.2017.01.019
[research_oconnell_komsic_2026]: https://doi.org/10.21552/edseq/2026/2/6
[research_oehmanwi_1983]: https://ntrs.nasa.gov/citations/19830015046
[research_ogawa_takeda_2015]: https://doi.org/10.4236/ojfd.2015.53028
[research_ohashi_ohno_1982]: https://doi.org/10.1016/0022-5096(82)90001-1
[research_ohlsson_1964]: https://doi.org/10.1115/1.3675408
[research_ohwada_shimada_2019]: https://doi.org/10.1186/s42774-019-0001-z
[research_ohyama_1978]: https://doi.org/10.1299/kikai1938.44.3810
[research_okorokov_gorash_2017]: https://doi.org/10.1016/j.prostr.2017.07.110
[research_okumoto_elsanker_1973]: https://doi.org/10.21236/ad0767182
[research_old_1957]: https://doi.org/10.1121/1.1918877
[research_omalley_chamot_1987]: https://doi.org/10.21236/ada192006
[research_opalka_1968]: https://doi.org/10.21236/ad0393552
[research_ordaz_geiselhart_2015]: https://doi.org/10.2514/1.c033160
[research_ordaz_li_2016]: https://doi.org/10.2514/1.c033159
[research_orloff_ciffone_1974]: https://doi.org/10.2514/3.59259
[research_orman_rae_1951]: https://doi.org/10.1098/rspa.1951.0206
[research_oruc_baklacioglu_2022]: https://doi.org/10.1016/j.energy.2022.125069
[research_oruc_baklacioglu_2023]: https://doi.org/10.1016/j.energy.2023.126819
[research_orysh_betz_1964]: https://doi.org/10.21236/ad0444513
[research_osborneroberts_kellythomasc_1953]: https://ntrs.nasa.gov/citations/19930087537
[research_ostieri_tognaccini_2018]: https://doi.org/10.2514/1.c034820
[research_ostowaric_naikd_1986]: https://ntrs.nasa.gov/citations/19860041891
[research_othman_kanazaki_2016]: https://doi.org/10.1016/j.ast.2016.08.019
[research_ou_maricq_2017]: https://doi.org/10.1080/02786826.2017.1349871
[research_ouyang_yang_2020]: https://doi.org/10.1016/j.msea.2020.139138
[research_overall_1976]: https://doi.org/10.21236/ada033883
[research_oznalbant_kavsaoglu_2018]: https://doi.org/10.1177/0142331218754618
[research_packman_kozlowski_1977]: https://doi.org/10.2514/3.58767
[research_page_bergstrom_2021]: https://doi.org/10.3389/fmars.2021.660196
[research_page_hield_2018]: https://doi.org/10.1115/1.4040030
[research_pai_weibel_2022]: https://doi.org/10.2139/ssrn.4065420
[research_pakle_jiang_2018]: https://doi.org/10.1016/j.jppr.2018.02.004
[research_palaia_2025]: https://doi.org/10.3390/aerospace13010046
[research_palienko_pogrebnyak_1976]: https://doi.org/10.1007/bf01528209
[research_palko_1973]: https://doi.org/10.21236/ad0769307
[research_palko_1974]: https://doi.org/10.21236/ad0787659
[research_palko_1975]: https://doi.org/10.21236/ada012880
[research_pan_huang_2017]: https://doi.org/10.5028/jatm.v9i1.736
[research_pan_huang_2019]: https://doi.org/10.5028/jatm.v11.1074
[research_pan_mu_2024]: https://doi.org/10.3390/aerospace11110911
[research_pan_shi_2022]: https://doi.org/10.3390/en15165791
[research_pan_shi_2024]: https://doi.org/10.1016/j.ast.2023.108780
[research_panov_shvets_1966]: https://doi.org/10.1007/bf01022287
[research_panov_shvets_1967]: https://doi.org/10.1007/bf01015152
[research_panton_1972]: https://doi.org/10.2514/3.59052
[research_panton_1973]: https://doi.org/10.2514/3.60212
[research_panzeri_savelyev_2018]: https://doi.org/10.1016/j.trpro.2018.02.026
[research_pao_banerjee_1978]: https://doi.org/10.1080/01495737808926934
[research_papadales_basils_1979]: https://doi.org/10.21236/ada073100
[research_papageorgiou_tarkian_2018]: https://doi.org/10.2514/1.c034314
[research_paraguassu_2015]: https://doi.org/10.17485/ijst/2015/v8i31/87309
[research_paranjape_ananthkrishnan_2023]: https://doi.org/10.61653/joast.v58i2.2006.706
[research_parisenrichardb_armstrongjohnc_1948]: https://ntrs.nasa.gov/citations/19930082371
[research_park_chung_2016]: https://doi.org/10.1017/aer.2015.17
[research_park_chung_2016_b]: https://doi.org/10.5139/ijass.2016.17.2.268
[research_park_chung_2018]: https://doi.org/10.1108/aeat-06-2017-0149
[research_park_kim_2026]: https://doi.org/10.1016/j.ast.2026.112263
[research_park_lee_2015]: https://doi.org/10.1108/aeat-07-2013-0128
[research_park_lee_2025]: https://doi.org/10.3390/s25247494
[research_park_zaki_2018]: https://doi.org/10.1017/jfm.2018.819
[research_parkes_1953]: https://doi.org/10.1108/eb032367
[research_parkes_1954]: https://doi.org/10.1108/eb032500
[research_parkes_1956]: https://doi.org/10.1108/eb032761
[research_parkes_1956_b]: https://doi.org/10.1108/eb032699
[research_parrish_jr_1978]: https://doi.org/10.21236/ada093689
[research_parthasarathysp_massierpf_1975]: https://ntrs.nasa.gov/citations/19750043862
[research_pashchenko_kharchenko_2022]: https://doi.org/10.2478/jok-2022-0048
[research_pasiuk_1963]: https://doi.org/10.21236/ad0448887
[research_patel_chudoba_2026]: https://doi.org/10.1108/aeat-01-2025-0015
[research_patel_dubey_2020]: https://doi.org/10.1080/15567036.2020.1785592
[research_patil_2018]: https://doi.org/10.23940/ijpe.18.01.p2.916
[research_patil_suresh_2021]: https://doi.org/10.14704/web/v18si01/web18050
[research_paul_suresh_2019]: https://doi.org/10.4271/01-12-02-0009
[research_paulk_anderson_1976]: https://doi.org/10.21236/adb014346
[research_pavlov_2016]: https://doi.org/10.3103/s1068799816040115
[research_payne_1957]: https://doi.org/10.1108/eb032840
[research_paziresh_nikseresht_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000704
[research_pecinka_bugajski_2017]: https://doi.org/10.14311/ap.2017.57.0022
[research_pendergraftodiscjr_ingraldianthonym_1992]: https://ntrs.nasa.gov/citations/19920009760
[research_pendley_marsh_1968]: https://doi.org/10.2514/3.43930
[research_peng_li_2024]: https://doi.org/10.1109/icjece.2024.3451965
[research_peng_tu_2018]: https://doi.org/10.1088/1757-899x/381/1/012103
[research_peng_zhai_2015]: https://doi.org/10.4028/www.scientific.net/kem.667.123
[research_pengju_liang_2015]: https://doi.org/10.1016/j.proeng.2014.12.563
[research_penlandja_creeltrjr_1978]: https://ntrs.nasa.gov/citations/19780023102
[research_penlandja_fournierrh_1975]: https://ntrs.nasa.gov/citations/19760004991
[research_penningtonje_meintelajjr_1980]: https://ntrs.nasa.gov/citations/19810061133
[research_pereira_williams_2015]: https://doi.org/10.4028/www.scientific.net/msf.828-829.93
[research_peri_2023]: https://doi.org/10.1080/09377255.2023.2250160
[research_pernica_palavenis_2024]: https://doi.org/10.1108/jopp-04-2024-0045
[research_perrin_2021]: https://doi.org/10.1007/s10494-021-00263-0
[research_petersenrb_1957]: https://ntrs.nasa.gov/citations/19660010455
[research_petersonvictorl_meneesgenep_1959]: https://ntrs.nasa.gov/citations/19980228241
[research_petkovic_banjac_2025]: https://doi.org/10.1115/1.4069811
[research_petricone_sisto_1971]: https://doi.org/10.1115/1.3445372
[research_petrov_pigusov_2019]: https://doi.org/10.1615/tsagiscij.2019030595
[research_pettesduler_roboam_2021]: https://doi.org/10.3390/electronics10111297
[research_pfaff_1965]: https://doi.org/10.21236/ad0467448
[research_pfaff_1968]: https://doi.org/10.21236/ad0832104
[research_pflag_1972]: https://doi.org/10.1093/milmed/137.8.321
[research_pfnur_breitsamter_2019]: https://doi.org/10.2514/1.c035491
[research_philippou_zachos_2024]: https://doi.org/10.3390/aerospace11010075
[research_phillips_jr_1999]: https://doi.org/10.21236/ada397472
[research_phillips_knowles_2015]: https://doi.org/10.1088/1748-3190/10/5/056020
[research_physical_and_2017]: https://doi.org/10.21884/ijmter.2017.4354.igqdx
[research_picard_whitley_2002]: https://doi.org/10.21236/ada407860
[research_piccirillo_gregorio_2024]: https://doi.org/10.3390/aerospace11090740
[research_pigusov_2021]: https://doi.org/10.34759/vst-2021-4-39-47
[research_pimenta_moffat_1979]: https://doi.org/10.1115/1.3450945
[research_pinapatruni_sinha_2025]: https://doi.org/10.1063/5.0264438
[research_ping_hong_2022]: https://doi.org/10.2139/ssrn.4184416
[research_piovesan_zachos_2025]: https://doi.org/10.2514/1.j064226
[research_platonov_nikitenko_2019]: https://doi.org/10.2478/pjst-2019-0008
[research_plourde_stenning_1968]: https://doi.org/10.2514/3.43933
[research_poggi_bernardini_2024]: https://doi.org/10.2514/1.c037486
[research_polhamusec_1966]: https://ntrs.nasa.gov/citations/19670003842
[research_polhamusec_1968]: https://ntrs.nasa.gov/citations/19680022518
[research_poll_schumann_2024]: https://doi.org/10.1017/aer.2024.10
[research_popeha_1971]: https://ntrs.nasa.gov/citations/19710025608
[research_portnoy_1963]: https://doi.org/10.1017/s0001925900002833
[research_pouryoussefi_abdolali_2023]: https://doi.org/10.1007/s40430-023-04205-x
[research_powellag_welgehr_1985]: https://ntrs.nasa.gov/citations/19850018399
[research_powers_1964]: https://doi.org/10.21236/ad0600749
[research_powersbg_1966]: https://ntrs.nasa.gov/citations/19660023036
[research_praj_fghaffari_2003]: https://ntrs.nasa.gov/citations/20040040269
[research_prasad_2025]: https://doi.org/10.1115/1.4069510
[research_preisserjs_schoensterja_1981]: https://ntrs.nasa.gov/citations/19810036194
[research_preisserjs_silcoxrj_1984]: https://ntrs.nasa.gov/citations/19840035345
[research_presz_konarski_1971]: https://doi.org/10.2514/3.59196
[research_prigent_marechal_2015]: https://doi.org/10.1080/0305215x.2015.1062985
[research_prince_1976]: https://doi.org/10.1115/1.3446142
[research_priya_arora_2025]: https://doi.org/10.5750/ijme.v167ia3(s).1711
[research_probst_melberwilkending_2021]: https://doi.org/10.1108/hff-08-2021-0525
[research_procurement_process_1980]: https://doi.org/10.1108/eb035653
[research_proesmans_vos_2022]: https://doi.org/10.2514/1.c036529
[research_provenza_duffy_2018]: https://doi.org/10.1115/1.4040739
[research_pucillo_2016]: https://doi.org/10.1080/00423114.2016.1237665
[research_pue_2021]: https://doi.org/10.1017/s0047279421000751
[research_puett_1967]: https://doi.org/10.1002/macp.1967.021000121
[research_puett_1968]: https://doi.org/10.5254/1.3547195
[research_purserpaule_spearmargaretf_1947]: https://ntrs.nasa.gov/citations/19930082127
[research_puvrez_1965]: https://doi.org/10.2514/3.43654
[research_pyle_1971]: https://doi.org/10.2514/3.59202
[research_qi_jin_2024]: https://doi.org/10.1016/j.ast.2023.108782
[research_qi_zong_2021]: https://doi.org/10.1007/s13272-021-00538-2
[research_qian_2025]: https://doi.org/10.1515/cppm-2024-0022
[research_qian_xinhui_2025]: https://doi.org/10.65904/3083-3450.2025.01.05
[research_qiang_xue_2024]: https://doi.org/10.1016/j.csite.2024.105032
[research_qiao_chu_2026]: https://doi.org/10.1063/5.0332543
[research_qiao_li_2019]: https://doi.org/10.4028/www.scientific.net/msf.944.92
[research_qin_2026]: https://doi.org/10.1142/s021812662642017x
[research_qin_liang_2016]: https://doi.org/10.12783/fae.2016.0501.02
[research_qiu_chen_2022]: https://doi.org/10.1016/j.fuel.2022.124431
[research_qiu_du_2023]: https://doi.org/10.1063/5.0171892
[research_qiu_zhao_2023]: https://doi.org/10.1063/5.0173396
[research_qiu_zhong_2024]: https://doi.org/10.33737/jgpps/191166
[research_qu_chen_2019]: https://doi.org/10.1016/j.ast.2019.01.049
[research_qu_kong_2019]: https://doi.org/10.1007/s11433-018-9347-6
[research_qu_wang_2024]: https://doi.org/10.1063/5.0234961
[research_quan_sun_2024]: https://doi.org/10.1109/tase.2023.3258602
[research_queijomj_jaquetbyronm_1954]: https://ntrs.nasa.gov/citations/19930092215
[research_queijomj_wolhartwalterd_1951]: https://ntrs.nasa.gov/citations/19930086818
[research_quigleyherveyc_andersonsethb_1960]: https://ntrs.nasa.gov/citations/19980223993
[research_radespiel_burnazzi_2016]: https://doi.org/10.1017/aer.2015.7
[research_radon_1969]: https://doi.org/10.1515/mt-1969-111201
[research_rains_1955]: https://doi.org/10.1115/1.4014392
[research_rajdeepbosemondal_2026]: https://doi.org/10.55041/ijsrem60571
[research_ramakrishna_senthilkumar_2019]: https://doi.org/10.1088/1742-6596/1276/1/012008
[research_ramamurti_2011]: https://doi.org/10.21236/ada546062
[research_ramaswamy_viswanathan_1975]: https://doi.org/10.2514/3.44506
[research_ramjet_supersonic_1958]: https://doi.org/10.1016/0016-0032(58)90466-6
[research_ramprasadh_devanandh_2015]: https://doi.org/10.1260/1756-8293.7.3.361
[research_rand_1963]: https://doi.org/10.21236/ad0419249
[research_rao_chen_2023]: https://doi.org/10.3390/aerospace10040331
[research_rao_kumar_2025]: https://doi.org/10.1017/aer.2025.37
[research_rao_sureshkumar_2022]: https://doi.org/10.1115/1.4055279
[research_rao_vpatel_2016]: https://doi.org/10.14445/22315381/ijett-v42p272
[research_raspet_1957]: https://doi.org/10.21236/ad0135753
[research_ratnayakenalina_2010]: https://ntrs.nasa.gov/citations/20100001729
[research_rayej_taylorrt_1965]: https://ntrs.nasa.gov/citations/19660033257
[research_reader_1976]: https://doi.org/10.21236/ada026548
[research_rebizov_2022]: https://doi.org/10.7256/2454-0617.2022.4.38905
[research_rebuffetpierre_poissonquintonph_1952]: https://ntrs.nasa.gov/citations/19930093899
[research_reedy_gorrell_2025]: https://doi.org/10.1115/1.4070352
[research_rees_1977]: https://doi.org/10.1109/temc.1977.303553
[research_rehman_2022]: https://doi.org/10.13111/2066-8201.2022.14.3.8
[research_reichert_brock_1977]: https://doi.org/10.21236/ada056782
[research_reid_1937]: https://doi.org/10.2514/8.438
[research_reid_moore_1980]: https://doi.org/10.1115/1.3230353
[research_reimer_hudson_1998]: https://doi.org/10.21236/ada343448
[research_reinbold_breitsamter_2026]: https://doi.org/10.2514/1.c038409
[research_reist_koo_2022]: https://doi.org/10.2514/1.c036754
[research_ren_zhang_2021]: https://doi.org/10.1016/j.applthermaleng.2021.116677
[research_ren_zheng_2023]: https://doi.org/10.1177/14759217221149224
[research_report_and_1966]: https://doi.org/10.1049/tpe.1966.0074
[research_report_no_1937]: https://doi.org/10.1016/s0016-0032(37)90824-x
[research_report_no_1939]: https://doi.org/10.1016/s0016-0032(39)90757-x
[research_reshotko_karchmer_1977]: https://doi.org/10.2514/3.58830
[research_resta_marsilio_2021]: https://doi.org/10.3390/fluids6120441
[research_rettie_lewis_1968]: https://doi.org/10.2514/3.43977
[research_reukaufpj_burchamfwjr_1976]: https://ntrs.nasa.gov/citations/19770011066
[research_reworkable_edgebond_2016]: https://doi.org/10.37665/smbgevn44704
[research_reyhner_hickcox_1972]: https://doi.org/10.2514/3.59041
[research_reykers_fonck_2019]: https://doi.org/10.1177/0010836719850203
[research_rezamaadi_sepahiyounsi_2022]: https://doi.org/10.1016/j.expthermflusci.2021.110568
[research_ribner_1960]: https://doi.org/10.2514/8.8580
[research_riccio_giaquinto_2026]: https://doi.org/10.2514/1.c038477
[research_riccobene_ricci_2015]: https://doi.org/10.1108/aeat-03-2013-0055
[research_rice_oetting_1976]: https://doi.org/10.2514/3.44522
[research_richardswl_thompsonrandolphc_1991]: https://ntrs.nasa.gov/citations/19920068787
[research_riffel_fleeter_1981]: https://doi.org/10.2514/3.57552
[research_riffin_1943]: https://doi.org/10.21236/ada954228
[research_righi_pachidis_2018]: https://doi.org/10.1016/j.ast.2018.04.021
[research_riley_1976]: https://doi.org/10.1017/s0305004100053160
[research_rinehart_1971]: https://doi.org/10.4050/jahs.16.48
[research_ritapure_kharde_2018]: https://doi.org/10.2139/ssrn.3332400
[research_rivello_1965]: https://doi.org/10.21236/ad0471246
[research_rldha_1969]: https://doi.org/10.2514/3.44045
[research_roache_1965]: https://doi.org/10.2514/3.59234
[research_roark_cuda_2010]: https://doi.org/10.21236/ada519882
[research_roberts_1965]: https://doi.org/10.21236/ad0615928
[research_roberts_smith_1966]: https://doi.org/10.21236/ad0635953
[research_robertsosborne_thomasckelly_1960]: https://ntrs.nasa.gov/citations/20040047133
[research_robinsaw_beissnerfljr_1985]: https://ntrs.nasa.gov/citations/19850010668
[research_rockwell_2001]: https://doi.org/10.21236/ada402569
[research_rodgers_1965]: https://doi.org/10.2514/3.43615
[research_rodgers_1966]: https://doi.org/10.2514/3.43765
[research_rodriguez_liscouethanke_2025]: https://doi.org/10.2514/1.c037723
[research_roelofs_kurowicka_2021]: https://doi.org/10.2514/1.c035985
[research_rokicki_1982]: https://doi.org/10.21236/ada121908
[research_roland_rumpfkeil_2017]: https://doi.org/10.2514/1.c033958
[research_romanov_2021]: https://doi.org/10.47576/2712-7559_2021_3_2_89
[research_rosenbaumh_zeibergsl_1965]: https://ntrs.nasa.gov/citations/19660030698
[research_roskam_dusto_1969]: https://doi.org/10.2514/3.44100
[research_roskam_holgate_1968]: https://doi.org/10.2514/3.43981
[research_rowe_1958]: https://doi.org/10.1243/pime_proc_1958_172_066_02
[research_rowe_sussman_1971]: https://doi.org/10.2514/3.44275
[research_roysalam_bil_2016]: https://doi.org/10.1017/aer.2016.59
[research_ruban_menezes_2020]: https://doi.org/10.1115/1.4048141
[research_rubio_ballard_1967]: https://doi.org/10.21236/ad0660321
[research_rudolphpeterkc_1997]: https://ntrs.nasa.gov/citations/20080004619
[research_ruh_warner_2026]: https://doi.org/10.2514/1.c038533
[research_rumsey_slotnick_2019]: https://doi.org/10.2514/1.c034940
[research_rumseycharlesb_leedorothyb_1961]: https://ntrs.nasa.gov/citations/19980235513
[research_rybalko_loth_2015]: https://doi.org/10.2514/1.j054050
[research_rylov_1974]: https://doi.org/10.1007/bf01031315
[research_saadon_talib_2016]: https://doi.org/10.1088/1757-899x/152/1/012011
[research_sachs_1975]: https://doi.org/10.2514/3.44471
[research_sachs_1977]: https://doi.org/10.2514/3.44623
[research_safavi_tarkian_2015]: https://doi.org/10.1177/1063293x15587020
[research_safoklov_demidov_2025]: https://doi.org/10.3103/s1068799825070025
[research_sahai_snellen_2017]: https://doi.org/10.2514/1.c034009
[research_said_mat_2018]: https://doi.org/10.12700/aph.15.8.2018.8.1
[research_sajadifar_maier_2023]: https://doi.org/10.3390/cryst13020269
[research_sakamoto_sasaki_2021]: https://doi.org/10.1002/eej.23342
[research_sakata_ohta_2017]: https://doi.org/10.1007/s11630-017-0907-x
[research_sakataif_davisgw_1975]: https://ntrs.nasa.gov/citations/19750055457
[research_sakataif_davisgw_1977]: https://ntrs.nasa.gov/citations/19770018637
[research_sakurada_nakajima_1965]: https://doi.org/10.1002/macp.1965.020870109
[research_salama_said_2023]: https://doi.org/10.1108/ci-09-2022-0238
[research_saleemyusoof_sivapragasam_2016]: https://doi.org/10.1016/j.jppr.2016.11.004
[research_samberger_weissensteiner_2023]: https://doi.org/10.1016/j.actamat.2023.118952
[research_samimy_webb_2011]: https://doi.org/10.21236/ada564713
[research_samuelsson_gronstedt_2021]: https://doi.org/10.1016/j.ast.2020.106412
[research_sanchez_liscouethanke_2020]: https://doi.org/10.1016/j.ast.2020.105946
[research_sanchez_liscouethanke_2021]: https://doi.org/10.1016/j.compind.2021.103467
[research_sanchezcarmona_cuernorejado_2018]: https://doi.org/10.1108/aeat-05-2017-0129
[research_sandahlcarla_1948]: https://ntrs.nasa.gov/citations/19930085426
[research_sandeeprameshkumar_suresh_2021]: https://doi.org/10.1016/j.matpr.2021.01.763
[research_sandstrom_white_1961]: https://doi.org/10.21236/ad0257074
[research_saporito_daronch_2023]: https://doi.org/10.1016/j.ast.2023.108349
[research_saravanan_desikan_2017]: https://doi.org/10.1017/aer.2017.115
[research_sarikaya_zarri_2024]: https://doi.org/10.1016/j.jsv.2024.118539
[research_sarodo_yamamoto_2024]: https://doi.org/10.1167/jov.24.2.7
[research_sartor_becker_2016]: https://doi.org/10.2514/1.c032757
[research_sato_kon_1972]: https://doi.org/10.1016/0008-6223(72)90485-x
[research_sattar_stargardter_1971]: https://doi.org/10.2514/3.59152
[research_saundersjd_keithtgjr_1991]: https://ntrs.nasa.gov/citations/19910061195
[research_saves_diouane_2024]: https://doi.org/10.1007/s00158-024-03785-z
[research_saxenaashok_1998]: https://ntrs.nasa.gov/citations/19990116061
[research_schaffrath_nicke_2025]: https://doi.org/10.1115/1.4067687
[research_schatz_hermanutz_2016]: https://doi.org/10.1007/s00158-016-1541-z
[research_scherz_williams_1978]: https://doi.org/10.2514/3.55805
[research_schneideredwardt_1990]: https://ntrs.nasa.gov/citations/19900048975
[research_schnell_grossman_1979]: https://doi.org/10.2514/3.58614
[research_schoeler_1987]: https://doi.org/10.21236/ada195832
[research_schueltke_stumpf_2017]: https://doi.org/10.1108/aeat-11-2016-0210
[research_schuldenfreimarvin_comisarowpaul_1947]: https://ntrs.nasa.gov/citations/19930093791
[research_schulderfreimarvin_comisarowpaul_1951]: https://ntrs.nasa.gov/citations/19930083056
[research_schumann_sharman_2015]: https://doi.org/10.2514/1.c032909
[research_schwanz_1972]: https://doi.org/10.21236/ada006391
[research_schweikhardt_grippe_1971]: https://doi.org/10.2514/3.59197
[research_schwendemannmf_1981]: https://ntrs.nasa.gov/citations/19830003774
[research_scorer_davenport_1970]: https://doi.org/10.1017/s0022112070002501
[research_scpradhan_2023]: https://doi.org/10.61653/joast.v60i1.2008.816
[research_sebata_ushijima_2021]: https://doi.org/10.1299/jsmemm.2021.os0106
[research_sebata_ushijima_2022]: https://doi.org/10.1299/transjsme.21-00273
[research_secchi_lacava_2021]: https://doi.org/10.2514/1.c035932
[research_sedlock_1985]: https://doi.org/10.21236/ada153767
[research_segletes_2004]: https://doi.org/10.21236/ada421229
[research_seidel_matwey_1980]: https://doi.org/10.1115/1.3230362
[research_sekar_kengaiah_2024]: https://doi.org/10.1108/aeat-02-2024-0046
[research_seleznev_2018]: https://doi.org/10.1088/1742-6596/1009/1/012034
[research_seleznev_2019]: https://doi.org/10.1088/1742-6596/1250/1/012004
[research_selim_liscouethanke_2023]: https://doi.org/10.2514/1.c037142
[research_semenov_1981]: https://doi.org/10.1007/bf00769005
[research_semlitsch_mihaescu_2016]: https://doi.org/10.1016/j.energy.2016.03.032
[research_semlitsch_mihaescu_2021]: https://doi.org/10.3390/aerospace8120369
[research_sepahiyounsi_2022]: https://doi.org/10.1016/j.ast.2021.107246
[research_sepahiyounsi_2025]: https://doi.org/10.1016/j.ast.2025.110346
[research_setayandeh_babaei_2020]: https://doi.org/10.1007/s00500-020-04684-3
[research_sgueglia_schmollgruber_2020]: https://doi.org/10.2514/1.c035509
[research_shafer_junghans_1990]: https://doi.org/10.21236/ada226109
[research_shahin_alqaradawi_2016]: https://doi.org/10.1016/j.apm.2016.07.030
[research_shahriyari_firouzabadi_2024]: https://doi.org/10.1038/s41598-024-55816-w
[research_shaikh_kahlon_2023]: https://doi.org/10.3390/fib11040031
[research_shang_ge_2021]: https://doi.org/10.1088/1742-6596/1985/1/012025
[research_shao_cao_2016]: https://doi.org/10.1155/2016/8562716
[research_shao_xu_2025]: https://doi.org/10.1088/1742-6596/3078/1/012012
[research_shariatzadeh_abrishamkar_2015]: https://doi.org/10.7763/jocet.2015.v3.198
[research_she_yuan_2017]: https://doi.org/10.1016/j.compstruct.2017.01.013
[research_shechtman_1981]: https://doi.org/10.21236/ada102746
[research_sheeba_lingeshwari_2025]: https://doi.org/10.26634/jcom.13.2.22102
[research_sheldon_1967]: https://doi.org/10.21236/ad0856658
[research_shen_2017]: https://doi.org/10.4028/www.scientific.net/msf.898.387
[research_shen_wen_2018]: https://doi.org/10.2514/1.j056565
[research_sheng_chen_2020]: https://doi.org/10.1016/j.ast.2020.106139
[research_sheng_chen_2023]: https://doi.org/10.1016/j.cja.2022.08.021
[research_shi_2025]: https://doi.org/10.1016/j.jer.2024.05.002
[research_shi_chang_2018]: https://doi.org/10.1016/j.actaastro.2018.09.015
[research_shi_chang_2019]: https://doi.org/10.1016/j.ast.2018.11.016
[research_shi_chang_2019_b]: https://doi.org/10.1016/j.ast.2019.02.022
[research_shi_tan_2018]: https://doi.org/10.1360/n092017-00215
[research_shifeng_jiamin_2018]: https://doi.org/10.1515/htmp-2017-0145
[research_shimabukuro_welge_1982]: https://doi.org/10.2514/3.57423
[research_shimabukurokm_welgehr_1979]: https://ntrs.nasa.gov/citations/19790067234
[research_shimada_ohwada_2020]: https://doi.org/10.1186/s42774-020-00037-8
[research_shimomura_park_2025]: https://doi.org/10.2355/isijinternational.isijint-2024-014
[research_shindos_jopparg_1980]: https://ntrs.nasa.gov/citations/19810016502
[research_shinozaki_suzuki_2017]: https://doi.org/10.1299/jsmeth.2017.52.125
[research_shiriaev_freidovich_2026]: https://doi.org/10.1016/j.sysconle.2026.106510
[research_shirinzadehdastgiri_fuerth_2023]: https://doi.org/10.1038/s41598-023-40527-5
[research_shiryaev_milenin_2026]: https://doi.org/10.18287/2541-7533-2026-25-1-147-157
[research_shiversjp_mclemorehc_1975]: https://ntrs.nasa.gov/citations/19770021165
[research_shkaraputa_1976]: https://doi.org/10.1007/bf01533037
[research_shoshanytavory_peleg_2023]: https://doi.org/10.1002/sys.21688
[research_shu_gao_2025]: https://doi.org/10.1063/5.0279923
[research_shufan_heng_2018]: https://doi.org/10.1051/matecconf/201817903015
[research_shulman_parry_1966]: https://doi.org/10.1121/1.1942873
[research_si_huang_2019]: https://doi.org/10.1063/1.5098543
[research_siedlak_pinon_2017]: https://doi.org/10.1007/s00163-017-0269-0
[research_sikora_2020]: https://doi.org/10.54570/atpet2020/03/03/0071
[research_silva_resende_2021]: https://doi.org/10.1007/s00158-021-03033-8
[research_silversteinabe_whitejamesa_1937]: https://ntrs.nasa.gov/citations/19930091622
[research_simonelli_zou_2023]: https://doi.org/10.1016/j.mtla.2023.101856
[research_simpson_1971]: https://doi.org/10.1016/0017-9310(71)90029-9
[research_simsek_uslu_2019]: https://doi.org/10.1061/(asce)as.1943-5525.0001042
[research_sinaiskii_pogrebnyak_1972]: https://doi.org/10.1007/bf01527569
[research_singh_2018]: https://doi.org/10.29070/13/57895
[research_singh_borras_2026]: https://doi.org/10.1007/s11085-026-10409-y
[research_singh_dwivedi_2022]: https://doi.org/10.47893/gret.2022.1050
[research_singh_priyadarshi_2020]: https://doi.org/10.1007/s12541-020-00447-0
[research_singh_sharma_2016]: https://doi.org/10.1155/2016/2813541
[research_sinha_singh_2026]: https://doi.org/10.5937/fme2602380s
[research_sissingh_1951]: https://doi.org/10.2514/8.1843
[research_sitaram_govardhan_2023]: https://doi.org/10.61653/joast.v67i3.2015.385
[research_sivaramakrishnan_1981]: https://doi.org/10.2514/3.57591
[research_sivojosephn_1957]: https://ntrs.nasa.gov/citations/19930090576
[research_sizemore_jr_1973]: https://doi.org/10.21236/ada024610
[research_sklyarov_vartazarova_2022]: https://doi.org/10.15862/02sats422
[research_skoogrichardb_1951]: https://ntrs.nasa.gov/citations/19930086551
[research_skow_moore_1982]: https://doi.org/10.2514/3.61562
[research_skyrius_valentukevice_2020]: https://doi.org/10.15388/im.2020.90.47
[research_slaterjohnw_2011]: https://ntrs.nasa.gov/citations/20110011374
[research_slaterjohnw_2014]: https://ntrs.nasa.gov/citations/20140016826
[research_slaterjohnw_2015]: https://ntrs.nasa.gov/citations/20150021040
[research_slaterjohnw_2016]: https://ntrs.nasa.gov/citations/20160010068
[research_slaterjohnw_2017]: https://ntrs.nasa.gov/citations/20170008734
[research_sleemanwilliamc_byrnesandrewl_1953]: https://ntrs.nasa.gov/citations/20090023635
[research_sleemanwilliamcjr_1957]: https://ntrs.nasa.gov/citations/20050019253
[research_sleemanwilliamcjr_1961]: https://ntrs.nasa.gov/citations/20040047139
[research_smaili_rouwhorst_2018]: https://doi.org/10.2514/1.c034422
[research_smartmichaelk_kalkhoranirajm_1994]: https://ntrs.nasa.gov/citations/19970001786
[research_smeltzerdb_sorensenne_1972]: https://ntrs.nasa.gov/citations/19730005050
[research_smith_1967]: https://doi.org/10.21236/ad0655370
[research_smith_2021]: https://doi.org/10.1063/pt.3.4888
[research_smith_lebacqz_1973]: https://doi.org/10.21236/ad0754840
[research_smith_yamakawa_1979]: https://doi.org/10.21236/ada069827
[research_smithpm_1978]: https://ntrs.nasa.gov/citations/19780013110
[research_smithwilliardg_1954]: https://ntrs.nasa.gov/citations/20090025453
[research_smits_miles_2002]: https://doi.org/10.21236/ada405454
[research_smooth_particle_2021]: https://doi.org/10.21152/1750-9548.15.3.291
[research_snodgrass_1955]: https://doi.org/10.2514/8.6860
[research_snyderfs_voorheescg_1977]: https://ntrs.nasa.gov/citations/19780008102
[research_sobester_2021]: https://doi.org/10.2514/1.c036180
[research_soederrh_bobulaga_1979]: https://ntrs.nasa.gov/citations/19790022016
[research_soederrh_bobulaga_1979_b]: https://ntrs.nasa.gov/citations/19790015798
[research_soederrh_bobulaga_1982]: https://ntrs.nasa.gov/citations/19830007035
[research_soederrh_mehaliccm_1984]: https://ntrs.nasa.gov/citations/19850001760
[research_sohret_turan_2015]: https://doi.org/10.7763/ijet.2015.v7.772
[research_sokolov_karpati_1978]: https://doi.org/10.1115/1.3424330
[research_solomongeorgee_1955]: https://ntrs.nasa.gov/citations/19930090996
[research_soltani_askari_2019]: https://doi.org/10.1016/j.ast.2019.05.045
[research_soltani_daliri_2016]: https://doi.org/10.2514/1.b36162
[research_soltani_younsi_2015]: https://doi.org/10.2514/1.b35461
[research_soltanov_1977]: https://doi.org/10.1007/bf00882946
[research_soltanov_1982]: https://doi.org/10.1007/bf00605903
[research_song_zhang_2019]: https://doi.org/10.1115/1.4041699
[research_sorensen_bencze_1974]: https://doi.org/10.2514/3.59241
[research_sorensen_latham_1975]: https://doi.org/10.2514/3.44491
[research_sorensen_smeltzer_1969]: https://doi.org/10.2514/3.44033
[research_sorensen_smeltzer_1973]: https://doi.org/10.2514/3.44367
[research_sorensenne_benczedp_1973]: https://ntrs.nasa.gov/citations/19740028534
[research_sosnin_torshenov_1970]: https://doi.org/10.1007/bf01527239
[research_sousa_paniagua_2017]: https://doi.org/10.1016/j.compfluid.2017.03.005
[research_sovran_1959]: https://doi.org/10.1115/1.4007999
[research_sowter_1973]: https://doi.org/10.1017/s0001924000040677
[research_spearmanml_sawyerwc_1977]: https://ntrs.nasa.gov/citations/19780034893
[research_spencerbernardjr_1961]: https://ntrs.nasa.gov/citations/19980228059
[research_spivey_ortiz_2021]: https://doi.org/10.1115/1.4051079
[research_spoonerstanleyh_martinaalbertp_1948]: https://ntrs.nasa.gov/citations/19930085375
[research_spreemannkennethp_1958]: https://ntrs.nasa.gov/citations/19930085045
[research_spreiter_sacks_1951]: https://doi.org/10.2514/8.1830
[research_squires_2002]: https://doi.org/10.21236/ada410100
[research_sreekumar_vamsikrishna_2025]: https://doi.org/10.2514/1.a35907
[research_sreenivasan_ma_2023]: https://doi.org/10.3390/su15097564
[research_stamatelos_labeas_2025]: https://doi.org/10.3390/aerospace12080726
[research_stancil_1979]: https://doi.org/10.2514/3.58481
[research_stanisic_1961]: https://doi.org/10.1002/zamm.19610410903
[research_starken_lichtfuss_1970]: https://doi.org/10.1115/1.3445351
[research_steenkenwg_williamsjg_1999]: https://ntrs.nasa.gov/citations/19990024943
[research_stefanovic_livne_2021]: https://doi.org/10.2514/1.c035953
[research_stenning_1980]: https://doi.org/10.1115/1.3240630
[research_stenning_1980_b]: https://doi.org/10.1115/1.3240618
[research_stephan_heyen_2024]: https://doi.org/10.2514/1.c037632
[research_stephan_schrall_2017]: https://doi.org/10.2514/1.c033973
[research_stephensemilyw_1959]: https://ntrs.nasa.gov/citations/19980232232
[research_stephenson_1953]: https://doi.org/10.2514/8.2736
[research_stephenson_1958]: https://doi.org/10.1017/s0368393100068395
[research_stephenson_shohet_1967]: https://doi.org/10.4050/jahs.12.3.26
[research_sterbentzwilliamh_davidsjoseph_1952]: https://ntrs.nasa.gov/citations/20090016318
[research_stewart_1956]: https://doi.org/10.2514/8.3590
[research_stewart_bull_2011]: https://doi.org/10.21236/ada606209
[research_stewart_dominick_1975]: https://doi.org/10.21236/ada018420
[research_stewartson_1950]: https://doi.org/10.1017/s0305004100025779
[research_stickley_brownhill_1964]: https://doi.org/10.21236/ad0602083
[research_stocker_1951]: https://doi.org/10.1017/s0001925900000548
[research_straightdm_harringtonde_1973]: https://ntrs.nasa.gov/citations/19730017096
[research_strawn_kobayashi_1984]: https://doi.org/10.21236/ada143253
[research_strawn_kobayashi_1984_b]: https://doi.org/10.21236/ada328841
[research_stroh_sediako_2023]: https://doi.org/10.1007/s40962-022-00949-9
[research_strub_suter_1965]: https://doi.org/10.1115/1.3678166
[research_stuart_1982]: https://doi.org/10.21236/ada114181
[research_study_on_2022]: https://doi.org/10.47939/et.v3i6(02).36
[research_sturek_kayser_1983]: https://doi.org/10.21236/ada134992
[research_sturek_kayser_1983_b]: https://doi.org/10.21236/ada128036
[research_stutz_price_1964]: https://doi.org/10.2514/3.43593
[research_su_hwu_2021]: https://doi.org/10.1080/01495739.2021.2000344
[research_su_young_2017]: https://doi.org/10.1002/cepa.334
[research_su_zhang_2019]: https://doi.org/10.1016/j.tws.2019.03.052
[research_subramanian_delaurentis_2016]: https://doi.org/10.1002/sys.21358
[research_sugiyama_1971]: https://doi.org/10.1299/jsme1958.14.1077
[research_sugiyama_1971_b]: https://doi.org/10.1299/kikai1938.37.295
[research_sugiyama_1977]: https://doi.org/10.1299/jsme1958.20.711
[research_sui_lu_2025]: https://doi.org/10.3390/met15091059
[research_sullivan_1943]: https://doi.org/10.21236/ada954458
[research_sullivanpg_1978]: https://ntrs.nasa.gov/citations/19790008753
[research_sullivanrl_1979]: https://ntrs.nasa.gov/citations/19790065319
[research_sumadireja_dachyar_2025]: https://doi.org/10.3390/su17093849
[research_sun_2024]: https://doi.org/10.54097/54mphq42
[research_sun_chen_2026]: https://doi.org/10.1007/s00158-026-04375-x
[research_sun_ding_2026]: https://doi.org/10.1360/sst-2025-0362
[research_sun_gu_2021]: https://doi.org/10.1177/09596518211057423
[research_sun_gu_2024]: https://doi.org/10.1016/j.cja.2024.01.036
[research_sun_gu_2024_b]: https://doi.org/10.1007/s11630-024-1961-9
[research_sun_guo_2022]: https://doi.org/10.1016/j.cie.2022.108477
[research_sun_hu_2024]: https://doi.org/10.2514/1.j063397
[research_sun_ju_2024]: https://doi.org/10.3390/jmse12040585
[research_sun_li_2016]: https://doi.org/10.1080/01495739.2015.1120627
[research_sun_li_2021]: https://doi.org/10.1115/1.4051782
[research_sun_li_2021_b]: https://doi.org/10.1016/j.ast.2021.106793
[research_sun_li_2022]: https://doi.org/10.1007/s11630-022-1547-3
[research_sun_miao_2015]: https://doi.org/10.1515/tjj-2015-0036
[research_sun_nie_2015]: https://doi.org/10.1115/1.4031775
[research_sun_shen_2025]: https://doi.org/10.1016/j.ast.2025.110457
[research_sun_smith_2019]: https://doi.org/10.1016/j.ast.2019.105387
[research_sun_smith_2022]: https://doi.org/10.1007/s13272-021-00567-x
[research_sun_yang_2020]: https://doi.org/10.12783/dtcse/cmso2019/33628
[research_sun_yang_2024]: https://doi.org/10.1063/5.0243466
[research_sun_yang_2025]: https://doi.org/10.3724/j.gter.20250021
[research_sun_yu_2025]: https://doi.org/10.1063/5.0257367
[research_sun_zhang_2016]: https://doi.org/10.2322/tjsass.59.349
[research_sun_zhang_2024]: https://doi.org/10.2514/1.j064672
[research_sun_zheng_2025]: https://doi.org/10.1016/j.ast.2025.110574
[research_sun_zhu_2019]: https://doi.org/10.1063/1.5083820
[research_surber_sedlock_1979]: https://doi.org/10.2514/3.58575
[research_suresh_nirmal_2021]: https://doi.org/10.1016/j.matpr.2021.09.412
[research_suresh_patri_2017]: https://doi.org/10.1186/s12913-017-2332-y
[research_surwase_kumar_2025]: https://doi.org/10.1186/s44147-025-00749-y
[research_sussman_1968]: https://doi.org/10.2514/3.43914
[research_suttonfredb_1959]: https://ntrs.nasa.gov/citations/19980230678
[research_suzuki_suzuki_2020]: https://doi.org/10.1299/jsmeth.2020.55.152_paper
[research_sweep_optimization_2024]: https://doi.org/10.47176/jafm.17.12.2773
[research_syberg_koncsek_1976]: https://doi.org/10.2514/3.58712
[research_sybergj_koncsekjl_1972]: https://ntrs.nasa.gov/citations/19730028643
[research_szrama_2019]: https://doi.org/10.19206/ce-2019-205
[research_szrama_lodygowski_2024]: https://doi.org/10.3846/aviation.2024.22554
[research_szusta_2018]: https://doi.org/10.1016/j.ijfatigue.2018.05.025
[research_tadini_grange_2017]: https://doi.org/10.1016/j.ast.2017.02.011
[research_taggart_1966]: https://doi.org/10.1111/j.1559-3584.1966.tb05032.x
[research_taghavizenouz_ababafbehbaha_2017]: https://doi.org/10.5139/ijass.2017.18.1.91
[research_taghiabad_esfandabadi_2026]: https://doi.org/10.1016/j.ast.2025.110963
[research_taguchi_mori_2017]: https://doi.org/10.1155/2017/7287586
[research_tahmasebi_karimim_2015]: https://doi.org/10.1108/aeat-12-2012-0241
[research_tahsini_2020]: https://doi.org/10.1108/aeat-12-2019-0268
[research_taig_1961]: https://doi.org/10.1108/eb033408
[research_takahashi_2017]: https://doi.org/10.1299/jfst.2017jfst0026
[research_takahashi_koike_2018]: https://doi.org/10.1299/jsmemecj.2018.j1920201
[research_takovitsky_2018]: https://doi.org/10.31857/s003282350002741-5
[research_tamboli_1956]: https://doi.org/10.1017/s0001925900010313
[research_tan_sun_2018]: https://doi.org/10.2514/1.c034740
[research_tanaka_murata_1975]: https://doi.org/10.1299/jsme1958.18.1277
[research_tanaka_murata_1975_b]: https://doi.org/10.1299/kikai1938.41.863
[research_tanaka_murata_1975_c]: https://doi.org/10.1299/jsme1958.18.256
[research_tanaka_nojima_1971]: https://doi.org/10.2472/jsms.20.418
[research_tanchoonsooi_suderkenneth_2003]: https://ntrs.nasa.gov/citations/20030067316
[research_taneich_rinoie_2025]: https://doi.org/10.2514/1.c035961
[research_tang_1969]: https://doi.org/10.2514/3.29574
[research_tang_cai_2025]: https://doi.org/10.1063/5.0297492
[research_tang_cai_2025_b]: https://doi.org/10.1063/5.0277814
[research_tang_li_2025]: https://doi.org/10.1063/5.0256817
[research_tang_owen_2021]: https://doi.org/10.1115/1.4050114
[research_tang_xu_2024]: https://doi.org/10.1017/jfm.2024.641
[research_tanguy_macmanus_2018]: https://doi.org/10.1016/j.ast.2018.04.031
[research_tani_1978]: https://doi.org/10.1115/1.3424390
[research_tanida_1972]: https://doi.org/10.1007/bf01593986
[research_tannercaroles_mcleodnormanj_1965]: https://ntrs.nasa.gov/citations/20000011978
[research_tao_jin_2022]: https://doi.org/10.1177/09544062221115346
[research_tao_sun_2019]: https://doi.org/10.1016/j.ast.2019.07.002
[research_tao_sun_2020]: https://doi.org/10.1016/j.cja.2020.01.015
[research_tao_wang_2024]: https://doi.org/10.3390/coatings14080960
[research_tao_zhao_2018]: https://doi.org/10.1142/s0217984918400407
[research_tarnowski_borowski_2021]: https://doi.org/10.1016/j.jallcom.2021.158896
[research_tate_gillard_1975]: https://doi.org/10.21236/ada018691
[research_taufikbudicahyana_achmadwardana_2023]: https://doi.org/10.31572/inotera.vol8.iss1.2023.id196
[research_taylor_1968]: https://doi.org/10.1017/s0001924000084347
[research_taylorjohng_1991]: https://ntrs.nasa.gov/citations/19910004962
[research_telemaco_oliveira_2020]: https://doi.org/10.1109/access.2020.2989106
[research_teschwa_steenkenwg_1978]: https://ntrs.nasa.gov/citations/19780025160
[research_teske_thistle_2018]: https://doi.org/10.13031/trans.12921
[research_tewfik_giedt_1960]: https://doi.org/10.2514/8.8737
[research_tfaily_bartoli_2026]: https://doi.org/10.1007/s00158-025-04239-w
[research_tfaily_diouane_2024]: https://doi.org/10.1007/s00158-024-03833-8
[research_thang_2016]: https://doi.org/10.1016/j.ast.2016.06.021
[research_thankachan_2025]: https://doi.org/10.1080/09700161.2025.2604369
[research_thapa_li_2025]: https://doi.org/10.3390/machines13040338
[research_the_fiat_1952]: https://doi.org/10.1108/eb032139
[research_the_influence_1975]: https://doi.org/10.1016/0010-4361(75)90426-7
[research_the_reason_2021]: https://doi.org/10.47939/et.v2i5.121
[research_the_rollsroyce_1967]: https://doi.org/10.1108/eb034271
[research_the_rollsroyce_1968]: https://doi.org/10.1108/eb034361
[research_thein_2018]: https://doi.org/10.47119/ijrp10020112019483
[research_theodorsen_1959]: https://doi.org/10.2514/8.8239
[research_thomas_1965]: https://doi.org/10.2514/3.3031
[research_thomas_srinivasan_1974]: https://doi.org/10.1016/0036-9748(74)90488-8
[research_thomasrandy_stueberthomasj_2013]: https://ntrs.nasa.gov/citations/20140001129
[research_thompson_2022]: https://doi.org/10.1063/10.0009660
[research_thompsonrobertf_voglerraymondd_1959]: https://ntrs.nasa.gov/citations/19980228213
[research_thrust_vectoring_2020]: https://doi.org/10.37896/jxu14.10/016
[research_tian_li_2020]: https://doi.org/10.1007/s00158-020-02589-1
[research_tian_shunke_2021]: https://doi.org/10.1080/09603409.2021.1897945
[research_ting_chaparro_2018]: https://doi.org/10.2514/1.c034810
[research_tirpak_1985]: https://doi.org/10.21236/ada163487
[research_titanium_or_1974]: https://doi.org/10.1016/0010-4361(74)90155-4
[research_tkalenko_1969]: https://doi.org/10.1007/bf01032473
[research_todorov_rakov_2023]: https://doi.org/10.3390/aerospace10030287
[research_toffol_ricci_2023]: https://doi.org/10.1016/j.compstruct.2022.116557
[research_tollthomasa_1942]: https://ntrs.nasa.gov/citations/19930092608
[research_tomczyk_seweryn_2017]: https://doi.org/10.1016/j.ijfatigue.2017.06.037
[research_tomczyk_seweryn_2021]: https://doi.org/10.3390/ma14020404
[research_tondl_1979]: https://doi.org/10.1016/0020-7462(79)90014-3
[research_tongguang_changhui_2015]: https://doi.org/10.1016/j.proeng.2014.12.581
[research_torenbeek_1971]: https://doi.org/10.1108/eb034787
[research_torgerson_mantri_2019]: https://doi.org/10.1016/j.wear.2018.12.046
[research_toric_boko_2020]: https://doi.org/10.1016/j.firesaf.2020.102971
[research_toric_brnic_2017]: https://doi.org/10.3390/met7040126
[research_toric_glavinic_2018]: https://doi.org/10.1002/fam.2643
[research_townsend_blatt_1976]: https://doi.org/10.2514/3.58698
[research_tran_read_2022]: https://doi.org/10.21236/ad1165123
[research_trapp_1952]: https://doi.org/10.21236/ad0008716
[research_traub_2016]: https://doi.org/10.2514/1.c033491
[research_trefnycj_bensontj_1995]: https://ntrs.nasa.gov/citations/19960016375
[research_trefnycj_wasserbauerjw_1986]: https://ntrs.nasa.gov/citations/19860015223
[research_trivers_carrick_2020]: https://doi.org/10.1007/s00158-020-02650-z
[research_tudosie_2017]: https://doi.org/10.19062/2247-3173.2017.19.1.26
[research_tudosie_2017_b]: https://doi.org/10.19062/1842-9238.2017.15.1.16
[research_tudosie_2018]: https://doi.org/10.19062/2247-3173.2018.20.33
[research_tudosie_dumitru_2019]: https://doi.org/10.19062/2247-3173.2019.21.27
[research_tudosie_paunescu_2017]: https://doi.org/10.19062/2247-3173.2017.19.1.27
[research_tugrul_akgul_2022]: https://doi.org/10.1016/j.mtcomm.2022.104827
[research_tuninetti_sepulveda_2024]: https://doi.org/10.3390/aerospace11040285
[research_turan_2015]: https://doi.org/10.1016/j.energy.2015.04.026
[research_turan_2022]: https://doi.org/10.2139/ssrn.4100910
[research_turan_2022_b]: https://doi.org/10.1016/j.energy.2022.124936
[research_turbofan_engine_2017]: https://doi.org/10.5829/idosi.ije.2017.30.04a.21
[research_turkkahraman_ozcan_2024]: https://doi.org/10.2339/politeknik.1247300
[research_tyan_nguyen_2017]: https://doi.org/10.2514/1.c033833
[research_uddin_gravdahl_2016]: https://doi.org/10.1016/j.ifacol.2016.07.323
[research_udroiu_blaj_2016]: https://doi.org/10.19062/2247-3173.2016.18.1.27
[research_ueda_tanaka_1975]: https://doi.org/10.1299/kikai1938.41.2853
[research_ueda_tanaka_1976]: https://doi.org/10.1299/kikai1938.42.1770
[research_ueda_tanaka_1977]: https://doi.org/10.1299/kikai1938.43.570
[research_ueki_yasuda_2020]: https://doi.org/10.1299/jsmefed.2020.os03-01
[research_uemura_kamata_2020]: https://doi.org/10.1515/htmp-2020-0039
[research_uglov_kuleshov_2016]: https://doi.org/10.1615/hightempmatproc.2016017189
[research_ukai_kato_2020]: https://doi.org/10.1016/j.msea.2020.139863
[research_uludag_turan_2015]: https://doi.org/10.7763/ijmmm.2015.v3.176
[research_um_2016]: https://doi.org/10.14731/kjir.2016.03.56.1.111
[research_unal_oz_2023]: https://doi.org/10.1108/aeat-02-2022-0056
[research_urans_simulation_2024]: https://doi.org/10.47176/jafm.17.05.2121
[research_urionabarrenetxea_martin_2022]: https://doi.org/10.1016/j.powtec.2022.117688
[research_using_tip_2022]: https://doi.org/10.47176/jafm.15.06.1089
[research_uthgenannt_1971]: https://doi.org/10.2514/3.59180
[research_utomo_bura_2019]: https://doi.org/10.23960/ins.v2i2.90
[research_uzun_2025]: https://doi.org/10.30518/jav.1583881
[research_vacarios_ceronmunoz_2025]: https://doi.org/10.1016/j.ast.2025.110135
[research_vaisakh_namratha_2019]: https://doi.org/10.1007/s00193-019-00929-9
[research_valencia_alulema_2020]: https://doi.org/10.1016/j.tsep.2020.100515
[research_valencia_hidalgo_2017]: https://doi.org/10.1016/j.cja.2016.12.005
[research_valensi_1958]: https://doi.org/10.2514/8.7478
[research_valoppi_bruschi_2017]: https://doi.org/10.1016/j.ijmecsci.2017.02.005
[research_vanarnhem_devries_2022]: https://doi.org/10.2514/1.c036338
[research_vancefdippoldiii_2022]: https://ntrs.nasa.gov/citations/20220010443
[research_vanderveldenalexanderjm_krooilan_1990]: https://ntrs.nasa.gov/citations/19900019224
[research_vandeusen_mardoc_1972]: https://doi.org/10.2514/3.58933
[research_vandommelen_1995]: https://doi.org/10.21236/ada329654
[research_vanrooyen_eshelby_1981]: https://doi.org/10.2514/3.44710
[research_vanschalkwykchristian_brightmichellem_2001]: https://ntrs.nasa.gov/citations/20050196613
[research_vasilev_1970]: https://doi.org/10.1007/bf01014997
[research_vazsonyi_1950]: https://doi.org/10.2514/8.1673
[research_veereshkumar_nagasailaja_2021]: https://doi.org/10.21275/sr21713140558
[research_venturelli_benini_2016]: https://doi.org/10.1016/j.ast.2016.08.021
[research_veras_balarac_2021]: https://doi.org/10.1063/5.0058642
[research_veresnikov_2025]: https://doi.org/10.17587/it.31.451-464
[research_veresnikov_goncharenko_2026]: https://doi.org/10.1134/s1064562426700055
[research_verlaine_2023]: https://doi.org/10.1504/ijpm.2023.132139
[research_verma_2018]: https://doi.org/10.2139/ssrn.3242663
[research_verma_kulkarni_2024]: https://doi.org/10.1088/2631-8695/ad937d
[research_verma_manisankar_2025]: https://doi.org/10.2514/1.j065217
[research_verma_singh_2020]: https://doi.org/10.1177/0954410020909190
[research_victorantonio_yan_2023]: https://doi.org/10.3844/jastsp.2023.8.16
[research_vidal_1962]: https://doi.org/10.2514/8.9698
[research_vidal_1963]: https://doi.org/10.2514/3.54857
[research_vieira_koch_2020]: https://doi.org/10.2514/1.c035847
[research_vijayakumar_senthilvelan_2015]: https://doi.org/10.4028/www.scientific.net/amm.813-814.252
[research_vinodh_aravindraj_2015]: https://doi.org/10.1108/bij-04-2013-0037
[research_vinogradov_makarov_2017]: https://doi.org/10.1615/tsagiscij.2017022808
[research_vinogradov_melnikov_2017]: https://doi.org/10.1615/tsagiscij.2017021109
[research_viranr_fandn_1982]: https://ntrs.nasa.gov/citations/19820049585
[research_vlasov_2022]: https://doi.org/10.34759/vst-2022-3-7-16
[research_vlasov_gomorova_2021]: https://doi.org/10.1007/s11182-021-02472-6
[research_vodolazskiy_zhloba_2017]: https://doi.org/10.4028/www.scientific.net/ssp.265.646
[research_volkov_2024]: https://doi.org/10.3390/fluids9070148
[research_vondoenhoffalberte_hortonelmera_1942]: https://ntrs.nasa.gov/citations/19930092757
[research_vonglahnu_reshotkom_1972]: https://ntrs.nasa.gov/citations/19730035656
[research_vonhlatky_rice_2018]: https://doi.org/10.1080/14702436.2017.1417736
[research_vorobev_bich_1977]: https://doi.org/10.1007/bf01528583
[research_vorobev_galiakhmetov_2023]: https://doi.org/10.3103/s1068798x23070389
[research_voroninst_2022]: https://doi.org/10.21883/tpl.2022.05.53485.19175
[research_vos_wortmann_2017]: https://doi.org/10.3233/aop-160063
[research_voss_2019]: https://doi.org/10.1016/j.ast.2019.03.049
[research_vu_nguyen_2025]: https://doi.org/10.1088/2631-8695/adffff
[research_wabick_johnson_2023]: https://doi.org/10.1017/jfm.2023.34
[research_wacker_1967]: https://doi.org/10.21236/ad0656573
[research_wahler_maruyama_2025]: https://doi.org/10.2514/1.c037516
[research_walker_1952]: https://doi.org/10.21236/ad0041745
[research_walker_1955]: https://doi.org/10.1017/s036839310011689x
[research_walker_heming_1980]: https://doi.org/10.1038/283286a0
[research_walkerharoldj_berggrenroberte_1948]: https://ntrs.nasa.gov/citations/19930090356
[research_wall_mckinley_2017]: https://doi.org/10.1121/1.5014176
[research_wallnerle_lubickrj_1955]: https://ntrs.nasa.gov/citations/20090023603
[research_wallnerlewise_lubickrobertj_1954]: https://ntrs.nasa.gov/citations/20090021949
[research_wamsley_1976]: https://doi.org/10.2307/1959420
[research_wandini_mulyanto_2016]: https://doi.org/10.4028/www.scientific.net/amm.842.208
[research_wang_2020]: https://doi.org/10.1016/j.cep.2019.107676
[research_wang_chen_2025]: https://doi.org/10.1371/journal.pone.0318807
[research_wang_chen_2025_b]: https://doi.org/10.1063/5.0268520
[research_wang_fan_2022]: https://doi.org/10.23919/jsee.2022.000019
[research_wang_fan_2024]: https://doi.org/10.1007/s42405-024-00710-y
[research_wang_fang_2024]: https://doi.org/10.1115/1.4064512
[research_wang_feng_2025]: https://doi.org/10.1063/5.0251122
[research_wang_gao_2023]: https://doi.org/10.3390/pr11102880
[research_wang_guan_2026]: https://doi.org/10.1063/5.0316018
[research_wang_guo_2017]: https://doi.org/10.1016/j.cja.2017.03.004
[research_wang_he_2024]: https://doi.org/10.3389/fenrg.2023.1259729
[research_wang_he_2025]: https://doi.org/10.1371/journal.pone.0328630
[research_wang_hu_2020]: https://doi.org/10.1177/0036850420940920
[research_wang_hu_2021]: https://doi.org/10.1115/1.4049382
[research_wang_hu_2021_b]: https://doi.org/10.1007/s43684-021-00013-z
[research_wang_huo_2025]: https://doi.org/10.3390/drones9090607
[research_wang_khan_2015]: https://doi.org/10.1115/1.4031360
[research_wang_li_2016]: https://doi.org/10.1007/s11433-015-5708-1
[research_wang_li_2020]: https://doi.org/10.1155/2020/7180639
[research_wang_li_2023]: https://doi.org/10.3390/coatings13091516
[research_wang_li_2025]: https://doi.org/10.3390/aerospace12090846
[research_wang_liu_2018]: https://doi.org/10.3390/ma11071158
[research_wang_liu_2024]: https://doi.org/10.1016/j.ast.2024.108947
[research_wang_liu_2025]: https://doi.org/10.1080/01457632.2025.2571269
[research_wang_lu_2020]: https://doi.org/10.1016/j.ast.2020.105979
[research_wang_pan_2023]: https://doi.org/10.1016/j.applthermaleng.2023.120275
[research_wang_pan_2024]: https://doi.org/10.1016/j.applthermaleng.2023.122324
[research_wang_peng_2023]: https://doi.org/10.3390/atmos14010106
[research_wang_shi_2020]: https://doi.org/10.3390/ma13204636
[research_wang_song_2022]: https://doi.org/10.3390/pr11010069
[research_wang_song_2024]: https://doi.org/10.1016/j.ast.2024.108936
[research_wang_sun_2020]: https://doi.org/10.3390/met10091185
[research_wang_sun_2023]: https://doi.org/10.1515/tjj-2023-0030
[research_wang_sun_2023_b]: https://doi.org/10.2514/1.j062300
[research_wang_tang_2020]: https://doi.org/10.1088/1742-6596/1509/1/012022
[research_wang_tang_2025]: https://doi.org/10.1088/1742-6596/3041/1/012024
[research_wang_tian_2015]: https://doi.org/10.1061/(asce)as.1943-5525.0000480
[research_wang_tian_2021]: https://doi.org/10.1155/2021/6653824
[research_wang_tu_2024]: https://doi.org/10.2514/1.i011388
[research_wang_wang_2020]: https://doi.org/10.1016/j.ast.2019.105534
[research_wang_wang_2022]: https://doi.org/10.1109/access.2022.3227386
[research_wang_wang_2023]: https://doi.org/10.3390/aerospace10080729
[research_wang_wang_2023_b]: https://doi.org/10.1017/aer.2023.19
[research_wang_wang_2023_c]: https://doi.org/10.1007/s10462-023-10620-2
[research_wang_wang_2024]: https://doi.org/10.1038/s41598-024-61900-y
[research_wang_xu_2023]: https://doi.org/10.1007/s00158-023-03635-4
[research_wang_yuan_2019]: https://doi.org/10.2514/1.c035209
[research_wang_zhang_2025]: https://doi.org/10.1088/1742-6596/3041/1/012007
[research_wang_zhang_2026]: https://doi.org/10.1016/j.ast.2025.110951
[research_wang_zhao_2021]: https://doi.org/10.3390/met11101630
[research_wang_zhao_2022]: https://doi.org/10.1016/j.ast.2022.107883
[research_wang_zhao_2023]: https://doi.org/10.1177/09544100231154055
[research_wang_zhao_2023_b]: https://doi.org/10.1016/j.ast.2023.108420
[research_wang_zhao_2025]: https://doi.org/10.1016/j.eswa.2025.126782
[research_wang_zhao_2025_b]: https://doi.org/10.1016/j.ast.2024.109886
[research_wang_zhao_2026]: https://doi.org/10.1016/j.measurement.2026.122215
[research_wang_zhou_2024]: https://doi.org/10.1109/access.2024.3419889
[research_ward_1949]: https://doi.org/10.1017/s0001925900000056
[research_wardana_cahyana_2022]: https://doi.org/10.37868/dss.v3.id195
[research_warren_chen_1973]: https://doi.org/10.1007/bf01177123
[research_warsch_carbone_2026]: https://doi.org/10.3390/aerospace13070623
[research_washington_humphrey_1969]: https://doi.org/10.21236/ad0699359
[research_washington_pettis_1968]: https://doi.org/10.21236/ad0695658
[research_wasserbauerjf_gerstenmaierwh_1978]: https://ntrs.nasa.gov/citations/19780019182
[research_wasserbauerjf_neumannhe_1985]: https://ntrs.nasa.gov/citations/19850016950
[research_wasserman_mitchell_1973]: https://doi.org/10.21236/ad0761120
[research_watanabe_sunada_2023]: https://doi.org/10.2514/1.c036649
[research_watkins_2019]: https://doi.org/10.1080/14751798.2019.1640419
[research_watson_1966]: https://doi.org/10.1098/rspa.1966.0204
[research_watsonearlc_1953]: https://ntrs.nasa.gov/citations/19930087828
[research_wauchop_1997]: https://doi.org/10.21236/ada325473
[research_weed_2002]: https://doi.org/10.21236/ada403846
[research_wegener_1977]: https://doi.org/10.21236/ada038280
[research_wei_qu_2022]: https://doi.org/10.3390/cryst12091255
[research_weibergjamesa_holzhausercurta_1961]: https://ntrs.nasa.gov/citations/19980227077
[research_weinert_underhill_2022]: https://doi.org/10.3390/aerospace9020058
[research_weissman_1973]: https://doi.org/10.2514/3.60216
[research_wells_1993]: https://doi.org/10.21236/ada265083
[research_welna_dahlberg_1969]: https://doi.org/10.21236/ada056285
[research_wen_kong_2022]: https://doi.org/10.1016/j.msea.2022.143011
[research_wen_tang_2020]: https://doi.org/10.1080/01495739.2020.1734128
[research_wenzel_2015]: https://doi.org/10.11648/j.optics.s.2015040301.14
[research_wernerrogera_wolterjohnd_2010]: https://ntrs.nasa.gov/citations/20100042397
[research_westin_balthazar_2023]: https://doi.org/10.3390/axioms12090826
[research_wetzelbentone_1955]: https://ntrs.nasa.gov/citations/19930088409
[research_whalenpaulp_wilcoxfreda_1956]: https://ntrs.nasa.gov/citations/19930089419
[research_whalleymatthews_1991]: https://ntrs.nasa.gov/citations/19910022831
[research_wharton_waterhouse_1973]: https://doi.org/10.1016/0043-1648(73)90139-7
[research_whitaker_rediess_1970]: https://doi.org/10.2514/3.44210
[research_whitbeck_hofmann_1978]: https://doi.org/10.21236/ada067177
[research_whitcombrichardt_1953]: https://ntrs.nasa.gov/citations/20050019402
[research_whitcombrichardt_sevierjohnrjr_1960]: https://ntrs.nasa.gov/citations/19980223605
[research_white_1997]: https://doi.org/10.21236/ada330361
[research_whitney_1963]: https://doi.org/10.21236/ad0423790
[research_whitney_skinner_2024]: https://doi.org/10.5070/w4jwa.1576
[research_whitson_bartimo_1950]: https://doi.org/10.21236/ad0459075
[research_whittley_1952]: https://doi.org/10.1108/eb032129
[research_whoric_1973]: https://doi.org/10.21236/ad0914456
[research_whoric_1977]: https://doi.org/10.21236/ada038494
[research_wickert_1985]: https://doi.org/10.21236/ada157504
[research_wide_angle_lens_2025]: https://doi.org/10.17586/1023-5086-2025-92-10-41-51
[research_wilcoxfreda_1957]: https://ntrs.nasa.gov/citations/19930089790
[research_wilde_pickerell_1968]: https://doi.org/10.1108/eb034344
[research_wilkinson_1971]: https://doi.org/10.1121/1.1975605
[research_williams_butler_1963]: https://doi.org/10.1017/s0368393100078378
[research_williams_yost_1973]: https://doi.org/10.1017/s0001924000041610
[research_willis_1981]: https://doi.org/10.2514/3.57577
[research_wilson_figliola_2023]: https://doi.org/10.4271/01-16-02-0014
[research_wilson_riley_1993]: https://doi.org/10.21236/ada273685
[research_wilson_saintier_2019]: https://doi.org/10.1016/j.ijfatigue.2018.11.016
[research_winkler_1954]: https://doi.org/10.21236/ad0058826
[research_winograd_miles_1956]: https://doi.org/10.1017/s0001925900010167
[research_winternitz_ramsay_1957]: https://doi.org/10.1017/s036839310013086x
[research_wisniewski_1951]: https://doi.org/10.1108/eb032109
[research_witkowska_borowski_2024]: https://doi.org/10.3390/mi15070886
[research_wong_ryan_2017]: https://doi.org/10.1007/s00158-017-1817-y
[research_woodrm_millerds_1983]: https://ntrs.nasa.gov/citations/19830057466
[research_woodrm_millerds_1985]: https://ntrs.nasa.gov/citations/19850053430
[research_woodrm_millerds_1985_b]: https://ntrs.nasa.gov/citations/19850053429
[research_woods_friswell_2015]: https://doi.org/10.1016/j.ast.2015.01.012
[research_woodward_1956]: https://doi.org/10.1108/eb032671
[research_woodward_1979]: https://doi.org/10.1179/030716979803276020
[research_wren_2026]: https://doi.org/10.1080/17416124.2026.2614822
[research_wright_bruckman_1978]: https://doi.org/10.2514/3.58456
[research_wu_2021]: https://doi.org/10.1016/j.msea.2021.141543
[research_wu_cao_2025]: https://doi.org/10.1063/5.0276108
[research_wu_du_2026]: https://doi.org/10.1016/j.ast.2026.111695
[research_wu_gao_2023]: https://doi.org/10.3390/aerospace10050387
[research_wu_li_2024]: https://doi.org/10.3724/j.gter.20240004
[research_wu_li_2024_b]: https://doi.org/10.1186/s42774-024-00183-3
[research_wu_qiu_2021]: https://doi.org/10.1007/s00158-021-03040-9
[research_wu_wang_2025]: https://doi.org/10.1063/5.0248571
[research_wu_wu_2019]: https://doi.org/10.1016/j.ijmecsci.2019.04.040
[research_wu_yang_2024]: https://doi.org/10.1016/j.measurement.2024.114400
[research_wu_zhao_2022]: https://doi.org/10.1016/j.ast.2022.107500
[research_wuli_karlgeiselhart_2020]: https://ntrs.nasa.gov/citations/20205007182
[research_wuli_karlgeiselhart_2025]: https://ntrs.nasa.gov/citations/20250000419
[research_wunderlich_dahne_2021]: https://doi.org/10.2514/1.c036301
[research_xiao_jin_2023]: https://doi.org/10.3390/electronics12183861
[research_xiao_meng_2025]: https://doi.org/10.1007/s00158-025-04160-2
[research_xiaokang_kuaishe_2018]: https://doi.org/10.1016/s1875-5372(18)30189-9
[research_xie_cai_2026]: https://doi.org/10.2514/1.c038668
[research_xie_liu_2025]: https://doi.org/10.1016/j.ast.2025.110027
[research_xie_marrani_2021]: https://doi.org/10.1080/21642583.2021.1899999
[research_xie_yang_2020]: https://doi.org/10.1051/jnwpu/20203861330
[research_xie_ye_2025]: https://doi.org/10.1016/j.ast.2025.110396
[research_xie_ye_2025_b]: https://doi.org/10.1063/5.0294667
[research_xie_zhang_2016]: https://doi.org/10.1115/1.4034914
[research_xie_zhu_2023]: https://doi.org/10.1063/5.0185385
[research_xinguo_xing_2015]: https://doi.org/10.1016/j.proeng.2014.12.713
[research_xinqian_anxiong_2015]: https://doi.org/10.2514/1.b35448
[research_xu_2023]: https://doi.org/10.54254/2753-8818/18/20230256
[research_xu_chen_2016]: https://doi.org/10.1016/j.procir.2016.02.206
[research_xu_cheng_2020]: https://doi.org/10.1155/2020/2739131
[research_xu_gu_2024]: https://doi.org/10.3390/fluids9070155
[research_xu_hu_2021]: https://doi.org/10.3390/en14238057
[research_xu_hu_2022]: https://doi.org/10.1007/s11630-022-1729-z
[research_xu_hu_2022_b]: https://doi.org/10.1177/09544100211063164
[research_xu_hu_2023]: https://doi.org/10.1061/jaeeez.aseng-4419
[research_xu_wu_2025]: https://doi.org/10.1016/j.ast.2025.110603
[research_xu_yu_2025]: https://doi.org/10.3390/aerospace13010017
[research_xu_zhang_2026]: https://doi.org/10.1007/s00158-026-04374-y
[research_xu_zhou_2015]: https://doi.org/10.1016/j.ast.2015.07.022
[research_xue_li_2017]: https://doi.org/10.1016/j.egypro.2017.03.1000
[research_xue_li_2020]: https://doi.org/10.1007/s10338-020-00159-y
[research_xue_wang_2024]: https://doi.org/10.1115/1.4065631
[research_yadav_bodavula_2018]: https://doi.org/10.1017/aer.2018.109
[research_yadav_guven_2015]: https://doi.org/10.2514/1.a32605
[research_yagn_kalko_1972]: https://doi.org/10.1007/bf01529907
[research_yahiaoui_2024]: https://doi.org/10.1016/j.asr.2024.06.066
[research_yalcin_2017]: https://doi.org/10.1515/tjj-2015-0065
[research_yamada_himeno_2024]: https://doi.org/10.38036/jgpp.15.2_68
[research_yamaguchi_1964]: https://doi.org/10.1299/jsme1958.7.91
[research_yamamoto_kojima_2020]: https://doi.org/10.1016/j.ast.2019.105523
[research_yamanaka_kamimura_1975]: https://doi.org/10.1299/jsme1958.18.689
[research_yamazaki_mizobata_2019]: https://doi.org/10.2322/tastj.17.127
[research_yan_chen_2016]: https://doi.org/10.1007/s00193-016-0633-4
[research_yan_pan_2025]: https://doi.org/10.1063/5.0294481
[research_yan_qian_2024]: https://doi.org/10.3724/j.gter.20240005
[research_yan_zhang_2023]: https://doi.org/10.1016/j.ast.2023.108230
[research_yang_2018]: https://doi.org/10.6108/kspe.2018.22.6.037
[research_yang_ji_2021]: https://doi.org/10.3390/met11020303
[research_yang_kong_2026]: https://doi.org/10.1016/j.ast.2026.112146
[research_yang_li_2021]: https://doi.org/10.1061/(asce)as.1943-5525.0001306
[research_yang_li_2023]: https://doi.org/10.1016/j.triboint.2023.108895
[research_yang_li_2024_b]: https://doi.org/10.1016/j.triboint.2024.109907
[research_yang_li_2026]: https://doi.org/10.2514/1.c038587
[research_yang_liang_2022]: https://doi.org/10.3390/ma16010280
[research_yang_liu_2017]: https://doi.org/10.1016/j.actaastro.2016.11.043
[research_yang_liu_2019]: https://doi.org/10.1088/1361-6501/ab2e38
[research_yang_lu_2021]: https://doi.org/10.1115/1.4051403
[research_yang_lu_2022]: https://doi.org/10.1115/1.4055439
[research_yang_nikolaidis_2024]: https://doi.org/10.1016/j.applthermaleng.2023.121523
[research_yang_qi_2026]: https://doi.org/10.32604/ee.2025.070957
[research_yang_tian_2021]: https://doi.org/10.3389/fmats.2021.682831
[research_yang_wan_2025]: https://doi.org/10.3390/drones9100690
[research_yang_wang_2025]: https://doi.org/10.1007/s40747-025-01992-9
[research_yang_wu_2022]: https://doi.org/10.1115/1.4053238
[research_yang_yu_2026]: https://doi.org/10.3390/aerospace13050399
[research_yang_zhang_2020]: https://doi.org/10.1109/access.2019.2961426
[research_yang_zhang_2023]: https://doi.org/10.3390/en16104120
[research_yang_zhou_2020]: https://doi.org/10.1109/access.2020.2978883
[research_yano_okada_2018]: https://doi.org/10.1299/jsmecs.2018.56.702
[research_yao_zhang_2017]: https://doi.org/10.2514/1.j055627
[research_yao_zhang_2022]: https://doi.org/10.1115/1.4055214
[research_yao_zhou_2017]: https://doi.org/10.1115/1.4036495
[research_yaylak_pinarbasi_2026]: https://doi.org/10.64808/engineeringperspective.1905858
[research_ye_chuai_2026]: https://doi.org/10.1016/j.ast.2026.112908
[research_yeh_1959]: https://doi.org/10.2514/8.8286
[research_yeh_du_2022]: https://doi.org/10.1080/23779497.2022.2102527
[research_yeom_sung_2015]: https://doi.org/10.5139/ijass.2015.16.2.165
[research_yeranee_rao_2023]: https://doi.org/10.3390/aerospace11010037
[research_yi_2023]: https://doi.org/10.32604/fdmp.2023.021907
[research_yi_sun_2024]: https://doi.org/10.54097/d39w6055
[research_yoder_2006]: https://doi.org/10.21236/ada496662
[research_yonkewilliama_robbendaniell_1995]: https://ntrs.nasa.gov/citations/19950065546
[research_yoon_lee_2022]: https://doi.org/10.1016/j.csite.2022.101792
[research_yoon_xiao_2019]: https://doi.org/10.1109/tec.2019.2942775
[research_york_ozturk_2018]: https://doi.org/10.2514/1.j057020
[research_you_yu_2016]: https://doi.org/10.5139/ijass.2016.17.2.260
[research_yu_guo_2025]: https://doi.org/10.1016/j.ijthermalsci.2025.109703
[research_yu_ni_2021]: https://doi.org/10.1155/2021/8885074
[research_yu_wang_2025]: https://doi.org/10.1007/s12567-025-00672-1
[research_yu_xu_2023]: https://doi.org/10.1016/j.measurement.2022.112374
[research_yu_yu_2026]: https://doi.org/10.1016/j.matchar.2026.116640
[research_yu_zhao_2026]: https://doi.org/10.1017/flo.2026.10052
[research_yuan_dai_2021]: https://doi.org/10.3390/atmos12111472
[research_yuan_li_2023]: https://doi.org/10.1061/jaeeez.aseng-4249
[research_yuan_lu_2026]: https://doi.org/10.1016/j.energy.2026.140460
[research_yuan_shi_2016]: https://doi.org/10.1016/j.msea.2016.01.108
[research_yuan_zhang_2021]: https://doi.org/10.1017/aer.2021.76
[research_yue_wen_2017]: https://doi.org/10.1515/htmp-2015-0178
[research_yuhara_makino_2016]: https://doi.org/10.2514/1.c033369
[research_yuhasandrewj_rayronaldj_1992]: https://ntrs.nasa.gov/citations/19920071385
[research_yuhasandrewj_rayronaldj_1992_b]: https://ntrs.nasa.gov/citations/19920020182
[research_yusof_rahim_2017]: https://doi.org/10.5539/ass.v13n4p37
[research_zachos_macmanus_2016]: https://doi.org/10.2514/1.j054904
[research_zahir_aamer_2023]: https://doi.org/10.1049/icp.2023.1963
[research_zaleski_stefaniak_2021]: https://doi.org/10.1016/j.expthermflusci.2021.110435
[research_zaman_korth_2025]: https://doi.org/10.1177/1475472x251382217
[research_zarchi_attaran_2018]: https://doi.org/10.1007/s00158-018-2135-8
[research_zebbiche_youbi_2023]: https://doi.org/10.61653/joast.v58i3.2006.642
[research_zeng_buckley_2023]: https://doi.org/10.47611/jsrhs.v12i1.4349
[research_zeng_chen_2015]: https://doi.org/10.1177/1687814015594569
[research_zeng_oliveira_2017]: https://doi.org/10.3390/met7110504
[research_zeng_zhao_2022]: https://doi.org/10.1088/1742-6596/2228/1/012011
[research_zhai_li_2020]: https://doi.org/10.2514/1.c035766
[research_zhang_2024]: https://doi.org/10.4208/cmaa.2024-0012
[research_zhang_an_2024]: https://doi.org/10.1063/5.0212250
[research_zhang_bo_2026]: https://doi.org/10.3390/aerospace13020191
[research_zhang_chen_2015]: https://doi.org/10.1016/j.cja.2015.06.015
[research_zhang_chen_2019]: https://doi.org/10.1016/j.compstruct.2019.111014
[research_zhang_chen_2024]: https://doi.org/10.1016/j.flowmeasinst.2024.102629
[research_zhang_cheng_2024]: https://doi.org/10.1088/1742-6596/2879/1/012012
[research_zhang_cheng_2025]: https://doi.org/10.1007/s12206-025-0719-y
[research_zhang_dong_2024]: https://doi.org/10.1109/access.2024.3510723
[research_zhang_du_2021]: https://doi.org/10.1016/j.cja.2020.08.019
[research_zhang_feng_2023]: https://doi.org/10.1080/03610918.2023.2182286
[research_zhang_hou_2015]: https://doi.org/10.1177/0954406215623978
[research_zhang_huang_2024]: https://doi.org/10.1016/j.applthermaleng.2024.123083
[research_zhang_ji_2025]: https://doi.org/10.1016/j.ast.2025.110315
[research_zhang_li_2020]: https://doi.org/10.1088/1742-6596/1600/1/012036
[research_zhang_li_2021]: https://doi.org/10.1007/s11630-021-1489-1
[research_zhang_liu_2023]: https://doi.org/10.1016/j.jweia.2023.105468
[research_zhang_liu_2024]: https://doi.org/10.1063/5.0235181
[research_zhang_lu_2022]: https://doi.org/10.1115/1.4050918
[research_zhang_malekgoudarzi_2020]: https://doi.org/10.1080/21642583.2020.1785970
[research_zhang_ning_2026]: https://doi.org/10.1016/j.ast.2026.113272
[research_zhang_robson_2016]: https://doi.org/10.1016/j.jmatprotec.2016.01.008
[research_zhang_shan_2017]: https://doi.org/10.1360/n092016-00329
[research_zhang_stapelfeldt_2020]: https://doi.org/10.1016/j.ast.2019.105668
[research_zhang_tan_2015]: https://doi.org/10.2514/1.b35425
[research_zhang_tan_2018]: https://doi.org/10.2514/1.j056318
[research_zhang_tiwari_2018]: https://doi.org/10.1016/j.applthermaleng.2018.08.032
[research_zhang_vahdati_2018]: https://doi.org/10.1115/1.4041376
[research_zhang_vahdati_2019]: https://doi.org/10.1115/1.4045552
[research_zhang_wang_2021]: https://doi.org/10.1016/j.jnucmat.2020.152618
[research_zhang_wang_2022]: https://doi.org/10.2514/1.b37808
[research_zhang_wang_2023]: https://doi.org/10.1016/j.energy.2023.129274
[research_zhang_wang_2024]: https://doi.org/10.1007/s00521-024-09720-z
[research_zhang_wei_2022]: https://doi.org/10.3390/app122010230
[research_zhang_wu_2026]: https://doi.org/10.3724/j.gter.20260008
[research_zhang_yang_2025]: https://doi.org/10.1017/aer.2025.10093
[research_zhang_yang_2025_b]: https://doi.org/10.1063/5.0247913
[research_zhang_yang_2026]: https://doi.org/10.1016/j.ast.2026.112109
[research_zhang_yu_2016]: https://doi.org/10.1016/j.ast.2016.09.006
[research_zhang_yuan_2020]: https://doi.org/10.1016/j.ast.2020.106182
[research_zhang_zhang_2020]: https://doi.org/10.1016/j.actaastro.2019.11.012
[research_zhang_zhang_2024]: https://doi.org/10.1016/j.applthermaleng.2024.123745
[research_zhang_zhang_2024_b]: https://doi.org/10.1016/j.cja.2023.11.009
[research_zhang_zhang_2024_c]: https://doi.org/10.1016/j.oceaneng.2024.116820
[research_zhang_zhao_2022]: https://doi.org/10.1016/j.istruc.2022.04.052
[research_zhang_zhou_2015]: https://doi.org/10.2514/1.c032739
[research_zhang_zhou_2017]: https://doi.org/10.1016/j.csda.2017.03.009
[research_zhang_zhou_2024]: https://doi.org/10.1007/s00158-024-03820-z
[research_zhao_clarke_2024]: https://doi.org/10.2514/1.c037404
[research_zhao_jin_2023]: https://doi.org/10.3390/aerospace10030207
[research_zhao_jin_2025]: https://doi.org/10.1016/j.applthermaleng.2024.124869
[research_zhao_li_2019]: https://doi.org/10.1016/j.actaastro.2019.02.026
[research_zhao_li_2025]: https://doi.org/10.1063/5.0260713
[research_zhao_sun_2017]: https://doi.org/10.1016/j.applthermaleng.2017.05.181
[research_zhao_sushama_2020]: https://doi.org/10.3390/atmos11040418
[research_zhao_vanhoorn_2022]: https://doi.org/10.3390/aerospace9080426
[research_zhao_zeng_2023]: https://doi.org/10.54097/hset.v77i.14434
[research_zhao_zhou_2017]: https://doi.org/10.1016/j.ijhydene.2017.04.250
[research_zhao_zhou_2019]: https://doi.org/10.3390/s19224995
[research_zhao_zhou_2022]: https://doi.org/10.1108/aeat-09-2021-0270
[research_zheldubovskii_ishchenko_1982]: https://doi.org/10.1007/bf00776056
[research_zhelnina_illarionov_2017]: https://doi.org/10.4028/www.scientific.net/ssp.265.785
[research_zhen_kun_2015]: https://doi.org/10.1061/(asce)as.1943-5525.0000450
[research_zheng_duan_2023]: https://doi.org/10.20517/ir.2023.04
[research_zheng_huang_2026]: https://doi.org/10.1016/j.ast.2026.113424
[research_zheng_ramaprian_1993]: https://doi.org/10.21236/ada275389
[research_zheng_wei_2024]: https://doi.org/10.1007/s11432-023-4088-2
[research_zhifei_yingxin_2023]: https://doi.org/10.1016/j.dt.2022.06.006
[research_zhipeng_chao_2015]: https://doi.org/10.1016/j.proeng.2014.12.584
[research_zhong_yu_2024]: https://doi.org/10.1016/j.jmrt.2024.04.072
[research_zhong_zhao_2022]: https://doi.org/10.1109/access.2022.3140331
[research_zhou_chen_2025]: https://doi.org/10.1016/j.eap.2025.11.022
[research_zhou_huang_2023]: https://doi.org/10.1016/j.ast.2022.108059
[research_zhou_li_2019]: https://doi.org/10.1063/1.5095499
[research_zhou_liu_2025]: https://doi.org/10.3724/j.issn.1674-4969.20240059
[research_zhou_ren_2018]: https://doi.org/10.1016/j.scib.2018.03.018
[research_zhou_zhang_2018]: https://doi.org/10.1007/s10584-018-2335-7
[research_zhu_chen_2018]: https://doi.org/10.1063/1.5005529
[research_zhu_gu_2022]: https://doi.org/10.1016/j.scib.2022.03.006
[research_zhu_lee_2018]: https://doi.org/10.1017/jfm.2018.646
[research_zhu_luo_2020]: https://doi.org/10.3390/en13082048
[research_zhu_nie_2021]: https://doi.org/10.1061/(asce)as.1943-5525.0001280
[research_zhu_qin_2019]: https://doi.org/10.2139/ssrn.3365146
[research_zhu_qin_2019_b]: https://doi.org/10.1016/j.actamat.2019.04.043
[research_zhu_wu_2023]: https://doi.org/10.1016/j.intermet.2023.108076
[research_zhu_xing_2023]: https://doi.org/10.1177/00368504231175712
[research_zhu_yang_2020]: https://doi.org/10.1115/1.4046047
[research_zhu_yuan_2024]: https://doi.org/10.1063/5.0210836
[research_zhu_zhao_2016]: https://doi.org/10.1016/j.applthermaleng.2016.06.013
[research_zhuang_lu_2015]: https://doi.org/10.1016/j.proeng.2015.11.195
[research_ziegler_1963]: https://doi.org/10.21236/ad0405158
[research_zien_ragsdale_1979]: https://doi.org/10.21236/ada073217
[research_ziganshin_logachev_2020]: https://doi.org/10.1016/j.jobe.2020.101666
[research_zimmermanch_1935]: https://ntrs.nasa.gov/citations/19930081303
[research_zoccoli_1977]: https://doi.org/10.21236/ada047872
[research_zubair_ejaz_2022]: https://doi.org/10.4028/p-g44bm8
[research_zubtsov_sudakov_1982]: https://doi.org/10.1007/bf01091274
[research_zukoski_auerbach_1976]: https://doi.org/10.1115/1.3446114
[research_zuo_2021]: https://doi.org/10.1016/j.actaastro.2021.06.010
[research_zuo_2023]: https://doi.org/10.2514/1.j062953
[research_zurlippe_2013]: https://doi.org/10.21236/ada620525
[research_zwieback_1964]: https://doi.org/10.2514/3.59209
