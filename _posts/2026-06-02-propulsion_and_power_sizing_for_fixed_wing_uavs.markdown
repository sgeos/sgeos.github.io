---
layout: post
mathjax: true
comments: true
title:  "Propulsion and Power Sizing for Small Fixed-Wing UAVs"
date:   2026-06-02 09:00:00 +0000
categories: aerospace engineering uav
series: fixed_wing_uav
series_title: Fixed-Wing UAV
series_index: 4
---
<!-- A118 -->
<script>console.log("A118");</script>

The companion articles in this series took the propulsion of a fixed-wing
unmanned aerial vehicle as given.
One [sized the runway][related_post_runway] from a thrust-to-weight ratio
it assumed, another [sized the launch and recovery][related_post_launch]
from a flying speed and a thrust it assumed, and a third covered
[building the airframe][related_post_lwpla] those forces act upon.
This article sizes the propulsion itself.
One quantity dominates, namely the power required to fly,
because power is thrust times speed and thrust in steady flight is drag,
so the whole problem flows from the drag the aircraft must overcome and the
speed it must overcome it at.
Everything else, the propeller, the motor or the engine, the battery or the
fuel, is a way of supplying that power and the excess above it that climb
and launch demand.

## The Power Master Variable

In steady level flight the wing carries the weight and the thrust balances
the drag, so the thrust required is the weight divided by the
[lift-to-drag ratio][ref_ld],

$$
 T = D = \frac{W}{L/D}. 
\tag{1}
$$

Power is the rate of doing work, the product of that thrust and the speed,
so the power required to hold level flight is

$$
 P_{\text{req}} = T\,V = \frac{W\,V}{L/D}. 
\tag{2}
$$

This single expression is the spine of the subject.
The power rises with weight, rises with speed, and falls with the
lift-to-drag ratio, so a clean, efficient airframe flown at a sensible
speed is the cheapest aircraft to power.
The proxy worth carrying is the power loading, the weight a system carries
per unit of installed power, which plays the role here that wing loading
plays for the runway.
A propulsion system must supply this cruise power, and it must supply more,
because climb and acceleration and the launch case all demand thrust beyond
the level-flight balance.
The margin of power above $P_{\text{req}}$ is what sets the rate of climb,
and at low speed the same margin is what accelerates the aircraft to flying
speed, which is the link back to the takeoff and launch analysis.

## Drag, Lift-to-Drag, and the Polar

Because the lift-to-drag ratio sets the power, the drag deserves a closer
look.
The drag of an aircraft splits into a part that does not depend on lift and
a part that does, and the [drag polar][ref_drag_polar] writes the
coefficient as

$$
 C_D = C_{D,0} + \frac{C_L^2}{\pi\,e\,A\!R}, 
\tag{3}
$$

where $C_{D,0}$ is the parasite drag coefficient,
the second term is the [lift-induced drag][ref_induced_drag],
$A\!R$ is the wing [aspect ratio][ref_aspect_ratio],
and $e$ is the [Oswald efficiency][ref_oswald].
The total drag force follows from the [drag equation][ref_drag_equation],
$D = \tfrac{1}{2}\rho V^2 S\, C_D$.
Two facts from the polar matter for sizing.
The lift-to-drag ratio peaks at one particular speed, where parasite and
induced drag are equal, and that speed is close to the most efficient
cruise.
A high aspect ratio lowers the induced term and raises the peak lift-to-drag
ratio, which is why endurance airframes carry long, slender wings,
and the airframe-building companion treats the structural cost of that
choice.
The power required is therefore not a single number but a curve against
speed, and its minimum lies at a lower speed than the best lift-to-drag
point, because the power is the drag times the speed rather than the drag
alone.
That separation between the minimum-power speed and the best lift-to-drag
speed is what later distinguishes the speed for greatest endurance from the
speed for greatest range.

## Propellers and Efficiency

A motor or an engine produces shaft power, and a [propeller][ref_propeller]
turns that shaft power into thrust at an efficiency that is never complete.
[Momentum theory][ref_momentum_theory] models the propeller as a disk that
accelerates a column of air rearward, and it gives both the ideal
efficiency and the static thrust.
For a given shaft power the ideal static thrust rises with the disk area,

$$
 T_{\text{static}} \approx \left(2\,\rho\,A_{\text{disk}}\right)^{1/3}
   P_{\text{shaft}}^{2/3}, 
\tag{4}
$$

so a large, slow propeller makes more thrust per watt at zero speed than a
small, fast one, which favors climb and launch.
In forward flight the relevant parameter is the [advance ratio][ref_advance_ratio],
the ratio of forward speed to the product of rotational speed and diameter,
and a propeller is efficient only over a band of advance ratios,
so a propeller pitched for fast cruise is poor at static thrust and a
propeller pitched for static thrust is poor at speed.
A real propeller reaches perhaps sixty-five to eighty percent efficiency
near its design point and much less away from it.
The practical consequence is that the propeller must be matched to the job,
and an aircraft that must both launch hard and cruise efficiently either
compromises with one fixed propeller or carries a variable-pitch one.

## Thrust-to-Weight and the Launch and Climb Case

The propulsion system is rarely sized by cruise.
The [thrust-to-weight ratio][ref_thrust_weight] needed to accelerate down a
runway or off a catapult, the value the runway and launch companions
assumed near $0.35$, calls for a thrust several times the cruise thrust,
because cruise thrust is only the weight divided by the lift-to-drag ratio
while the launch thrust is a large fraction of the whole weight.
For the worked example below the cruise thrust is under twenty newtons while
the launch thrust is over eighty,
so the motor, the propeller, and the energy source must all be sized for the
launch and climb case and then throttled back for cruise.
The rate of climb is the excess power divided by the weight,
so the same surplus that lifts the aircraft over the obstacle of the runway
analysis is the surplus the propulsion must provide here.
Sizing for cruise alone is the classic error, because it yields an aircraft
that flies efficiently but cannot leave the ground or clear the trees.

## Electric Propulsion

An electric system stores energy in a battery and converts it through an
[electronic speed controller][ref_bldc], a brushless motor, and a
propeller.
The energy available is the battery capacity times the usable fraction,
and the endurance is that energy divided by the electrical power drawn,

$$
 t = \frac{E_{\text{batt}}\,\eta_{\text{total}}}{P_{\text{req}}}, \qquad
   \eta_{\text{total}} = \eta_{\text{prop}}\,\eta_{\text{motor}}\,\eta_{\text{esc}}, 
\tag{5}
$$

where the efficiencies of the propeller, the motor, and the controller
multiply.
The hard limit is the battery's [specific energy][ref_specific_energy].
A modern [lithium-polymer pack][ref_lipo] stores on the order of one hundred
fifty to two hundred fifty watt-hours per kilogram,
which is one to two orders of magnitude below liquid fuel,
so electric endurance is short unless the aircraft is light, slow, and
efficient.
The motor is chosen by its velocity constant, the speed it turns per volt,
with a low value turning a large propeller slowly for efficiency and a high
value turning a small propeller fast for compact thrust,
and the [sizing correlations][research_mdpi_propulsion] for electric and
fuel-powered UAVs make the trade quantitative.
The appeal of electric propulsion is its quiet, simple, vibration-free
operation and its instant throttle, and a
[broad review of electric UAV propulsion][research_frontiers_electric]
documents how far it has come, but the battery wall sets the ceiling on
endurance.

The propeller need not be open.
An [electric ducted fan][ref_ducted_fan] encloses a small, fast rotor in a
shroud, which trades the open propeller's efficiency at low speed and its
large diameter for a compact installation and a higher usable top speed.
For a slow, efficient cruise an open propeller of large diameter wins on
endurance, while a ducted fan suits a faster, cleaner airframe that values
the compact form over the last increment of efficiency,
and the choice is the same advance-ratio matching seen above carried to a
different part of the speed range.

## Combustion Propulsion

A combustion engine burns liquid fuel, and liquid fuel carries far more
energy per kilogram than any battery, near twelve thousand watt-hours per
kilogram before the engine's efficiency is applied.
The relevant figure of merit is the
[brake-specific fuel consumption][ref_bsfc],
the fuel mass burned per unit of shaft energy,

$$
 \dot m_f = c\, P_{\text{shaft}}, 
\tag{6}
$$

where $c$ is that consumption, so the fuel burn rate follows directly from
the shaft power and the endurance is the fuel mass divided by the burn rate.
Small UAVs favor the [two-stroke engine][ref_two_stroke] for its high
power-to-weight ratio, and at larger tactical sizes the
[Wankel rotary engine][ref_wankel] is common for the same reason,
the [RQ-7 Shadow][ref_rq7] flying behind a thirty-eight-horsepower rotary
and the [ScanEagle][ref_scaneagle] behind a small heavy-fuel piston engine.
The choice of heavy fuel on a military aircraft is a logistics and safety
decision rather than a performance one,
since a single low-volatility battlefield fuel such as
[jet kerosene of the JP-5 or JP-8 family][ref_jet_fuel] removes the hazard
and the supply burden of carrying gasoline alongside it.
The classic [range and endurance relations][ref_range] capture how a
propeller aircraft trades fuel for time and distance,
with endurance favored by flying at the best lift-to-drag speed and range by
flying a little faster.
The cost of combustion is vibration, noise, heat, a cold-start and tuning
burden, and a minimum practical size below which small engines become
inefficient and unreliable, which is the floor where electric propulsion
takes over.

## Altitude and Available Power

The power required is not the only quantity that moves with the air,
because the power available falls in thin air as well,
so a propulsion system must be sized for the worst conditions it will see
rather than for a standard sea-level day.
A naturally aspirated piston or rotary engine loses power roughly in
proportion to air density, so a hot, high field robs the engine of the very
margin the launch and climb case demands.
A propeller loses thrust as density falls, because the thrust it makes
depends on the mass of air it accelerates.
An electric motor is the exception on the supply side, since its electrical
power does not depend on air density, but its propeller still loses thrust
and its cooling is poorer in thin, warm air.
The runway companion sized the ground roll for the worst
[density altitude][ref_density_altitude], and the same condition sizes the
propulsion, because an aircraft that can just climb away at sea level may be
unable to do so on a hot afternoon at altitude.
The discipline is to size the cruise power, the climb margin, and the launch
thrust at the density altitude of the worst expected site,
not at the comfortable bench condition.

## Endurance and Range

Endurance and range are the two mission numbers that the power sizing
finally delivers.
For a propeller aircraft endurance is maximized by minimizing the power
required, which means flying slowly at the minimum-power speed, where the
induced drag is about three times the parasite drag, with the lightest wing
loading the mission allows.
Range is maximized faster, at the best lift-to-drag speed where the two
drags are equal, because range rewards distance per unit of energy rather
than time aloft.
A jet reverses the pairing, taking its best endurance at the best
lift-to-drag speed and its best range faster still, which is one more way
the jet sits apart from the propeller.
Neither number is flown to exhaustion.
As with the margins of the runway and launch companions, endurance is sized
with a reserve for diversion, headwind, loiter, and contingency,
so the usable energy is a fraction of the installed energy rather than all
of it.
For an electric aircraft both numbers are capped by the battery's specific
energy and scale directly with it,
so the same airframe carries far more endurance on fuel than on a battery of
equal mass.
The choice between the two propulsion families is therefore largely a choice
of mission duration.
A short, quiet, simple mission is an electric mission,
a long-endurance surveillance mission is a combustion mission,
and the crossover moves slowly upward in duration as batteries improve.
This is the same conclusion the airframe companion reached from a different
direction, that the sensible design is the one matched to its mission rather
than the one with the most impressive single number.

## Solar, Hybrid, and Fuel Cells

Three further families extend endurance beyond what a battery or a fuel tank
alone allows.
A [solar-powered aircraft][ref_solar] covers part or all of the cruise power
from photovoltaic cells on the wing, and a sufficiently light and efficient
airframe can fly through the night on energy stored by day.
A hybrid system pairs a small engine or a fuel cell sized near the cruise
power with a battery sized for the launch and climb surplus,
which lets each source do what it does best.
These are powerful for the endurance mission and are named here for
completeness, but their detailed energy management is its own subject and is
left to the out-of-scope list.

## Jets and Regimes Beyond the Propeller

At the upper edge of size and speed the propeller gives way to the jet.
A small gas-turbine [turbojet][ref_turbojet] or [turbofan][ref_turbofan]
produces thrust directly and is rated by thrust rather than shaft power,
so its sizing turns on thrust and on
[thrust-specific fuel consumption][ref_tsfc] rather than on a propeller
efficiency.
Small turbines power target drones and the faster, larger UAVs,
but at the one-to-two-meter scale of this series they are uncommon,
because a turbine is markedly less fuel-efficient and more costly than a
piston or rotary engine of the same output,
and it earns its place only when high speed is the point.

Four further families lie outside the regime of a subsonic small UAV and are
named here only to place them.
A [ramjet][ref_ramjet] makes no static thrust and works only once boosted to
high speed, and a [scramjet][ref_scramjet] is a hypersonic device entirely,
so both belong to missiles and high-speed vehicles rather than to an
aircraft cruising at tens of meters per second.
A [throttleable rocket][ref_rocket_engine], whether liquid or hybrid,
carries its own oxidizer, which gives it poor effective energy per unit mass
and therefore poor endurance in the atmosphere,
so it suits very high speed, very high altitude, brief boost, or space rather
than sustained flight.
A [rocket boost-glide][ref_boost_glide] profile, usually a solid booster
followed by an unpowered descent, is better seen as a launch followed by a
glide than as a powerplant,
the boost belonging to the
[launch and recovery analysis][related_post_launch] and the glide range
following from the lift-to-drag ratio already discussed.
All four are out of scope here, named so that the boundary of the propeller
regime is explicit rather than assumed.

## Putting Numbers to It

A worked example reuses the aircraft of the runway and launch companions,
a UAV of mass twenty-five kilograms, so a weight of about two hundred
forty-five newtons.
Take a lift-to-drag ratio of fourteen and a cruise speed of twenty-five
meters per second.
The cruise thrust is $245 / 14 \approx 17.5$ newtons,
and the cruise power required is $17.5 \times 25 \approx 440$ watts.
With a propeller at sixty-five percent and a motor and controller together
at eighty-five percent, the electrical power is
$440 / (0.65 \times 0.85) \approx 800$ watts.
A two-kilogram lithium-polymer pack at one hundred eighty watt-hours per
kilogram stores about three hundred sixty watt-hours, of which roughly three
hundred are usable, so the electric endurance is
$300 / 800 \approx 0.38$ hours, about twenty-three minutes,
for a range near thirty-four kilometers.
Now burn fuel instead.
The shaft power is $440 / 0.65 \approx 680$ watts,
and at a brake-specific fuel consumption of half a kilogram per
kilowatt-hour the burn rate is $0.5 \times 0.68 \approx 0.34$ kilograms per
hour, so two kilograms of fuel lasts about six hours,
more than an order of magnitude beyond the equal mass of battery.
Finally the launch case, with a thrust-to-weight ratio of $0.35$,
demands a static thrust of $0.35 \times 245 \approx 86$ newtons,
nearly five times the cruise thrust,
which is the requirement that actually sizes the motor and the propeller.
None of these is a final design, but together they show that cruise power
sets the steady draw, the energy source sets the endurance, and the launch
case sets the peak, and that the three must be sized together.

## Out of Scope

Several neighboring subjects are deliberately excluded.
The detailed electrical design of the motor and the controller, the winding,
the magnetics, and the thermal limits, is an engineering specialty of its
own.
The blade-element aerodynamics and the structural and acoustic design of the
propeller are named through momentum theory but not derived here.
The internal cycle of a piston, rotary, or turbine engine, its combustion,
cooling, and emissions, is a separate discipline, and this article treats an
engine only through its shaft power and fuel consumption.
The battery chemistry, the cell balancing, and the thermal and safety
management of a large pack are out of scope, as is the energy management of
a solar, hybrid, or fuel-cell system beyond naming it.
The guidance and control that schedule throttle through a mission,
the propulsion contribution to stability and control, and the regulatory and
noise constraints on propulsion are left to their own treatments.
And the takeoff ground roll, the launch energy, and the recovery are covered
in the companion articles and are not repeated.

## Conclusion

Propulsion sizing for a fixed-wing UAV is the management of one power.
The power required to fly is the weight times the speed divided by the
lift-to-drag ratio, and the propulsion system must supply that cruise power,
the surplus that climb and launch demand, and the energy that endurance
needs.
A propeller turns shaft power into thrust at a matched efficiency,
an electric system buys quiet simplicity at the price of a battery wall,
a combustion engine buys endurance at the price of vibration and a minimum
size, and the launch case rather than cruise usually sets the peak.
Size the cruise power from the drag, size the peak from the thrust-to-weight
the runway and launch demand, and size the energy from the mission duration,
and the result is a propulsion system a builder can defend with numbers
rather than guess at.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 6 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 6, 6 are established and 0 are bespoke.
Quantities are in SI units, with power in watts, thrust and weight in newtons and speed in metres per second, while battery energy is quoted in watt-hours and brake-specific fuel consumption in mass of fuel per unit of shaft energy, so units must be reconciled before the endurance and fuel-burn relations are evaluated.

**Equation 1, Thrust Required in Level Flight.**
In steady level flight thrust balances drag, which equals the weight divided by the lift-to-drag ratio.
[lift-to-drag ratio][ref_ld]

$$
 T = D = \frac{W}{L/D}. 
\tag{1}
$$

**Equation 2, Power Required in Level Flight.**
The power required to hold level flight is the thrust required multiplied by the airspeed.

$$
 P_{\text{req}} = T\,V = \frac{W\,V}{L/D}. 
\tag{2}
$$

**Equation 3, Parabolic Drag Polar.**
The drag coefficient is the sum of a parasite term independent of lift and a lift-induced term that grows with the square of the lift coefficient.
[drag polar][ref_drag_polar]
[lift-induced drag][ref_induced_drag]

$$
 C_D = C_{D,0} + \frac{C_L^2}{\pi\,e\,A\!R}, 
\tag{3}
$$

**Equation 4, Ideal Static Thrust from Momentum Theory.**
Momentum theory models the propeller as an actuator disk and gives the ideal static thrust as rising with the cube root of disk area and the two-thirds power of shaft power.
[Momentum theory][ref_momentum_theory]

$$
 T_{\text{static}} \approx \left(2\,\rho\,A_{\text{disk}}\right)^{1/3}
   P_{\text{shaft}}^{2/3}, 
\tag{4}
$$

**Equation 5, Electric Endurance from Stored Energy.**
Endurance is the usable battery energy, reduced by the product of propeller, motor and controller efficiencies, divided by the power required.

$$
 t = \frac{E_{\text{batt}}\,\eta_{\text{total}}}{P_{\text{req}}}, \qquad
   \eta_{\text{total}} = \eta_{\text{prop}}\,\eta_{\text{motor}}\,\eta_{\text{esc}}, 
\tag{5}
$$

**Equation 6, Fuel Burn Rate from Brake-Specific Fuel Consumption.**
The fuel mass flow is the brake-specific fuel consumption multiplied by the shaft power.
[brake-specific fuel consumption][ref_bsfc]

$$
 \dot m_f = c\, P_{\text{shaft}}, 
\tag{6}
$$

### Notation

- $T$, the thrust
- $D$, the drag
- $W$, the weight
- $L/D$, the lift-to-drag ratio
- $P_{\text{req}}$, the power required for level flight
- $C_{D,0}$, the parasite drag coefficient
- $e$, the Oswald efficiency factor
- $A\!R$, the wing aspect ratio
- $A_{\text{disk}}$, the propeller disk area
- $P_{\text{shaft}}$, the shaft power
- $E_{\text{batt}}$, the battery energy
- $\eta_{\text{total}}$, the product of the propeller, motor and controller efficiencies
- $\dot m_f$, the fuel mass flow
- $c$, the brake-specific fuel consumption

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Joshi, Dhaval, Dipankar Deb, and S. M. Muyeen. 2022. "Comprehensive Review on Electric Propulsion System of Unmanned Aerial Vehicles." *Frontiers in Energy Research* 10: 752012. [https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2022.752012/full][research_frontiers_electric]

### Primary Sources, Non-Peer-Reviewed

- *Propulsion Sizing Correlations for Electrical and Fuel Powered UAVs (MDPI Aerospace)*. n.d. [https://www.mdpi.com/2226-4310/8/7/171][research_mdpi_propulsion]

### Tertiary Sources

- "AAI RQ-7 Shadow." 2025. Wikipedia. Last modified December 6, at 06:33 (UTC). [https://en.wikipedia.org/w/index.php?title=AAI\_RQ-7\_Shadow&oldid=1325964195][ref_rq7]
- "Advance Ratio." 2025. Wikipedia. Last modified September 30, at 17:05 (UTC). [https://en.wikipedia.org/w/index.php?title=Advance\_ratio&oldid=1314290025][ref_advance_ratio]
- "AeroVironment RQ-20 Puma." 2026. Wikipedia. Last modified February 20, at 17:35 (UTC). [https://en.wikipedia.org/w/index.php?title=AeroVironment\_RQ-20\_Puma&oldid=1339456326][ref_puma]
- "Aspect Ratio (Aeronautics)." 2026. Wikipedia. Last modified May 21, at 13:38 (UTC). [https://en.wikipedia.org/w/index.php?title=Aspect\_ratio\_(aeronautics)&oldid=1355374989][ref_aspect_ratio]
- "Boeing Insitu MQ-27 ScanEagle." 2026. Wikipedia. Last modified March 19, at 00:23 (UTC). [https://en.wikipedia.org/w/index.php?title=Boeing\_Insitu\_MQ-27\_ScanEagle&oldid=1344204034][ref_scaneagle]
- "Boost-Glide." 2026. Wikipedia. Last modified May 4, at 07:19 (UTC). [https://en.wikipedia.org/w/index.php?title=Boost-glide&oldid=1352449733][ref_boost_glide]
- "Brake-Specific Fuel Consumption." 2026. Wikipedia. Last modified February 20, at 18:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Brake-specific\_fuel\_consumption&oldid=1339464508][ref_bsfc]
- "Brushless DC Electric Motor." 2026. Wikipedia. Last modified May 12, at 19:05 (UTC). [https://en.wikipedia.org/w/index.php?title=Brushless\_DC\_electric\_motor&oldid=1353847199][ref_bldc]
- "Density Altitude." 2025. Wikipedia. Last modified November 25, at 09:53 (UTC). [https://en.wikipedia.org/w/index.php?title=Density\_altitude&oldid=1324067232][ref_density_altitude]
- "Drag Curve." 2026. Wikipedia. Last modified May 13, at 22:40 (UTC). [https://en.wikipedia.org/w/index.php?title=Drag\_curve&oldid=1354034912][ref_drag_polar]
- "Drag Equation." 2025. Wikipedia. Last modified November 1, at 04:06 (UTC). [https://en.wikipedia.org/w/index.php?title=Drag\_equation&oldid=1319837239][ref_drag_equation]
- "Ducted Fan." 2025. Wikipedia. Last modified September 4, at 22:33 (UTC). [https://en.wikipedia.org/w/index.php?title=Ducted\_fan&oldid=1309578916][ref_ducted_fan]
- "Jet Fuel." 2026. Wikipedia. Last modified May 17, at 15:14 (UTC). [https://en.wikipedia.org/w/index.php?title=Jet\_fuel&oldid=1354642102][ref_jet_fuel]
- "Lift-Induced Drag." 2026. Wikipedia. Last modified January 24, at 09:29 (UTC). [https://en.wikipedia.org/w/index.php?title=Lift-induced\_drag&oldid=1334569565][ref_induced_drag]
- "Lift-to-Drag Ratio." 2026. Wikipedia. Last modified May 16, at 13:54 (UTC). [https://en.wikipedia.org/w/index.php?title=Lift-to-drag\_ratio&oldid=1354447709][ref_ld]
- "Lithium Polymer Battery." 2026. Wikipedia. Last modified May 26, at 19:49 (UTC). [https://en.wikipedia.org/w/index.php?title=Lithium\_polymer\_battery&oldid=1356275529][ref_lipo]
- "Momentum Theory." 2026. Wikipedia. Last modified April 20, at 12:48 (UTC). [https://en.wikipedia.org/w/index.php?title=Momentum\_theory&oldid=1350150547][ref_momentum_theory]
- "Oswald Efficiency Number." 2026. Wikipedia. Last modified February 21, at 03:03 (UTC). [https://en.wikipedia.org/w/index.php?title=Oswald\_efficiency\_number&oldid=1339548943][ref_oswald]
- "Propeller (Aeronautics)." 2026. Wikipedia. Last modified May 23, at 20:32 (UTC). [https://en.wikipedia.org/w/index.php?title=Propeller\_(aeronautics)&oldid=1355769074][ref_propeller]
- "Ramjet." 2026. Wikipedia. Last modified May 10, at 15:40 (UTC). [https://en.wikipedia.org/w/index.php?title=Ramjet&oldid=1353487326][ref_ramjet]
- "Range (Aeronautics)." 2026. Wikipedia. Last modified February 17, at 01:39 (UTC). [https://en.wikipedia.org/w/index.php?title=Range\_(aeronautics)&oldid=1338758805][ref_range]
- "Rocket Engine." 2026. Wikipedia. Last modified May 25, at 14:02 (UTC). [https://en.wikipedia.org/w/index.php?title=Rocket\_engine&oldid=1356058584][ref_rocket_engine]
- "Scramjet." 2026. Wikipedia. Last modified March 25, at 14:02 (UTC). [https://en.wikipedia.org/w/index.php?title=Scramjet&oldid=1345319324][ref_scramjet]
- "Solar-Powered Aircraft." 2026. Wikipedia. Last modified February 21, at 23:07 (UTC). [https://en.wikipedia.org/w/index.php?title=Solar-powered\_aircraft&oldid=1339703347][ref_solar]
- "Specific Energy." 2025. Wikipedia. Last modified December 1, at 06:59 (UTC). [https://en.wikipedia.org/w/index.php?title=Specific\_energy&oldid=1325119006][ref_specific_energy]
- "Thrust-Specific Fuel Consumption." 2025. Wikipedia. Last modified December 16, at 03:32 (UTC). [https://en.wikipedia.org/w/index.php?title=Thrust-specific\_fuel\_consumption&oldid=1327790465][ref_tsfc]
- "Thrust-to-Weight Ratio." 2026. Wikipedia. Last modified April 9, at 22:06 (UTC). [https://en.wikipedia.org/w/index.php?title=Thrust-to-weight\_ratio&oldid=1347967967][ref_thrust_weight]
- "Turbofan." 2026. Wikipedia. Last modified May 23, at 15:07 (UTC). [https://en.wikipedia.org/w/index.php?title=Turbofan&oldid=1355725190][ref_turbofan]
- "Turbojet." 2026. Wikipedia. Last modified May 20, at 15:33 (UTC). [https://en.wikipedia.org/w/index.php?title=Turbojet&oldid=1355214838][ref_turbojet]
- "Two-Stroke Engine." 2026. Wikipedia. Last modified April 29, at 07:44 (UTC). [https://en.wikipedia.org/w/index.php?title=Two-stroke\_engine&oldid=1351647849][ref_two_stroke]
- "Wankel Engine." 2026. Wikipedia. Last modified May 25, at 14:50 (UTC). [https://en.wikipedia.org/w/index.php?title=Wankel\_engine&oldid=1356065515][ref_wankel]

### Related Posts

- Sechter, Brendan. 2026. "Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass." *Brendan A R Sechter's Development Blog*, May 30. [https://sgeos.github.io/aerospace/engineering/3d-printing/2026/05/30/prototyping\_fixed\_wing\_aircraft\_with\_lightweight\_pla\_and\_fiberglass.html][related_post_lwpla]
- Sechter, Brendan. 2026. "Runway Sizing for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, May 31. [https://sgeos.github.io/aerospace/engineering/uav/2026/05/31/runway\_sizing\_for\_fixed\_wing\_uavs.html][related_post_runway]
- Sechter, Brendan. 2026. "Launch and Recovery Systems for Fixed-Wing UAVs." *Brendan A R Sechter's Development Blog*, June 1. [https://sgeos.github.io/aerospace/engineering/uav/2026/06/01/launch\_and\_recovery\_systems\_for\_fixed\_wing\_uavs.html][related_post_launch]

[ref_advance_ratio]: https://en.wikipedia.org/w/index.php?title=Advance_ratio&oldid=1314290025
[ref_aspect_ratio]: https://en.wikipedia.org/w/index.php?title=Aspect_ratio_(aeronautics)&oldid=1355374989
[ref_bldc]: https://en.wikipedia.org/w/index.php?title=Brushless_DC_electric_motor&oldid=1353847199
[ref_boost_glide]: https://en.wikipedia.org/w/index.php?title=Boost-glide&oldid=1352449733
[ref_bsfc]: https://en.wikipedia.org/w/index.php?title=Brake-specific_fuel_consumption&oldid=1339464508
[ref_density_altitude]: https://en.wikipedia.org/w/index.php?title=Density_altitude&oldid=1324067232
[ref_drag_equation]: https://en.wikipedia.org/w/index.php?title=Drag_equation&oldid=1319837239
[ref_drag_polar]: https://en.wikipedia.org/w/index.php?title=Drag_curve&oldid=1354034912
[ref_ducted_fan]: https://en.wikipedia.org/w/index.php?title=Ducted_fan&oldid=1309578916
[ref_induced_drag]: https://en.wikipedia.org/w/index.php?title=Lift-induced_drag&oldid=1334569565
[ref_jet_fuel]: https://en.wikipedia.org/w/index.php?title=Jet_fuel&oldid=1354642102
[ref_ld]: https://en.wikipedia.org/w/index.php?title=Lift-to-drag_ratio&oldid=1354447709
[ref_lipo]: https://en.wikipedia.org/w/index.php?title=Lithium_polymer_battery&oldid=1356275529
[ref_momentum_theory]: https://en.wikipedia.org/w/index.php?title=Momentum_theory&oldid=1350150547
[ref_oswald]: https://en.wikipedia.org/w/index.php?title=Oswald_efficiency_number&oldid=1339548943
[ref_propeller]: https://en.wikipedia.org/w/index.php?title=Propeller_(aeronautics)&oldid=1355769074
[ref_puma]: https://en.wikipedia.org/w/index.php?title=AeroVironment_RQ-20_Puma&oldid=1339456326
[ref_ramjet]: https://en.wikipedia.org/w/index.php?title=Ramjet&oldid=1353487326
[ref_range]: https://en.wikipedia.org/w/index.php?title=Range_(aeronautics)&oldid=1338758805
[ref_rocket_engine]: https://en.wikipedia.org/w/index.php?title=Rocket_engine&oldid=1356058584
[ref_rq7]: https://en.wikipedia.org/w/index.php?title=AAI_RQ-7_Shadow&oldid=1325964195
[ref_scaneagle]: https://en.wikipedia.org/w/index.php?title=Boeing_Insitu_MQ-27_ScanEagle&oldid=1344204034
[ref_scramjet]: https://en.wikipedia.org/w/index.php?title=Scramjet&oldid=1345319324
[ref_solar]: https://en.wikipedia.org/w/index.php?title=Solar-powered_aircraft&oldid=1339703347
[ref_specific_energy]: https://en.wikipedia.org/w/index.php?title=Specific_energy&oldid=1325119006
[ref_thrust_weight]: https://en.wikipedia.org/w/index.php?title=Thrust-to-weight_ratio&oldid=1347967967
[ref_tsfc]: https://en.wikipedia.org/w/index.php?title=Thrust-specific_fuel_consumption&oldid=1327790465
[ref_turbofan]: https://en.wikipedia.org/w/index.php?title=Turbofan&oldid=1355725190
[ref_turbojet]: https://en.wikipedia.org/w/index.php?title=Turbojet&oldid=1355214838
[ref_two_stroke]: https://en.wikipedia.org/w/index.php?title=Two-stroke_engine&oldid=1351647849
[ref_wankel]: https://en.wikipedia.org/w/index.php?title=Wankel_engine&oldid=1356065515
[related_post_launch]: {% post_url 2026-06-01-launch_and_recovery_systems_for_fixed_wing_uavs %}
[related_post_lwpla]: {% post_url 2026-05-30-prototyping_fixed_wing_aircraft_with_lightweight_pla_and_fiberglass %}
[related_post_runway]: {% post_url 2026-05-31-runway_sizing_for_fixed_wing_uavs %}
[research_frontiers_electric]: https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2022.752012/full
[research_mdpi_propulsion]: https://www.mdpi.com/2226-4310/8/7/171
