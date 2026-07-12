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

$$ T = D = \frac{W}{L/D}. $$

Power is the rate of doing work, the product of that thrust and the speed,
so the power required to hold level flight is

$$ P_{\text{req}} = T\,V = \frac{W\,V}{L/D}. $$

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

$$ C_D = C_{D,0} + \frac{C_L^2}{\pi\,e\,A\!R}, $$

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

$$ T_{\text{static}} \approx \left(2\,\rho\,A_{\text{disk}}\right)^{1/3}
   P_{\text{shaft}}^{2/3}, $$

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

$$ t = \frac{E_{\text{batt}}\,\eta_{\text{total}}}{P_{\text{req}}}, \qquad
   \eta_{\text{total}} = \eta_{\text{prop}}\,\eta_{\text{motor}}\,\eta_{\text{esc}}, $$

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

$$ \dot m_f = c\, P_{\text{shaft}}, $$

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

## References

- [Reference, AAI RQ-7 Shadow][ref_rq7]
- [Reference, Advance Ratio][ref_advance_ratio]
- [Reference, AeroVironment RQ-20 Puma][ref_puma]
- [Reference, Aspect Ratio in Aeronautics][ref_aspect_ratio]
- [Reference, Boeing Insitu MQ-27 ScanEagle][ref_scaneagle]
- [Reference, Boost-Glide][ref_boost_glide]
- [Reference, Brake-Specific Fuel Consumption][ref_bsfc]
- [Reference, Brushless DC Electric Motor][ref_bldc]
- [Reference, Density Altitude][ref_density_altitude]
- [Reference, Drag Equation][ref_drag_equation]
- [Reference, Drag Polar][ref_drag_polar]
- [Reference, Ducted Fan][ref_ducted_fan]
- [Reference, Jet Fuel][ref_jet_fuel]
- [Reference, Lift-Induced Drag][ref_induced_drag]
- [Reference, Lift-to-Drag Ratio][ref_ld]
- [Reference, Lithium Polymer Battery][ref_lipo]
- [Reference, Momentum Theory][ref_momentum_theory]
- [Reference, Oswald Efficiency Number][ref_oswald]
- [Reference, Propeller in Aeronautics][ref_propeller]
- [Reference, Ramjet][ref_ramjet]
- [Reference, Range in Aeronautics][ref_range]
- [Reference, Rocket Engine][ref_rocket_engine]
- [Reference, Scramjet][ref_scramjet]
- [Reference, Solar-Powered Aircraft][ref_solar]
- [Reference, Specific Energy][ref_specific_energy]
- [Reference, Thrust-Specific Fuel Consumption][ref_tsfc]
- [Reference, Thrust-to-Weight Ratio][ref_thrust_weight]
- [Reference, Turbofan][ref_turbofan]
- [Reference, Turbojet][ref_turbojet]
- [Reference, Two-Stroke Engine][ref_two_stroke]
- [Reference, Wankel Engine][ref_wankel]
- [Related Post, Launch and Recovery Systems for Fixed-Wing UAVs][related_post_launch]
- [Related Post, Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass][related_post_lwpla]
- [Related Post, Runway Sizing for Fixed-Wing UAVs][related_post_runway]
- [Research, Comprehensive Review on Electric Propulsion System of UAVs (Frontiers)][research_frontiers_electric]
- [Research, Propulsion Sizing Correlations for Electrical and Fuel Powered UAVs (MDPI Aerospace)][research_mdpi_propulsion]

[ref_advance_ratio]: https://en.wikipedia.org/wiki/Advance_ratio
[ref_aspect_ratio]: https://en.wikipedia.org/wiki/Aspect_ratio_(aeronautics)
[ref_bldc]: https://en.wikipedia.org/wiki/Brushless_DC_electric_motor
[ref_boost_glide]: https://en.wikipedia.org/wiki/Boost-glide
[ref_bsfc]: https://en.wikipedia.org/wiki/Brake-specific_fuel_consumption
[ref_density_altitude]: https://en.wikipedia.org/wiki/Density_altitude
[ref_drag_equation]: https://en.wikipedia.org/wiki/Drag_equation
[ref_drag_polar]: https://en.wikipedia.org/wiki/Drag_polar
[ref_ducted_fan]: https://en.wikipedia.org/wiki/Ducted_fan
[ref_induced_drag]: https://en.wikipedia.org/wiki/Lift-induced_drag
[ref_jet_fuel]: https://en.wikipedia.org/wiki/Jet_fuel
[ref_ld]: https://en.wikipedia.org/wiki/Lift-to-drag_ratio
[ref_lipo]: https://en.wikipedia.org/wiki/Lithium_polymer_battery
[ref_momentum_theory]: https://en.wikipedia.org/wiki/Momentum_theory
[ref_oswald]: https://en.wikipedia.org/wiki/Oswald_efficiency_number
[ref_propeller]: https://en.wikipedia.org/wiki/Propeller_(aeronautics)
[ref_puma]: https://en.wikipedia.org/wiki/AeroVironment_RQ-20_Puma
[ref_ramjet]: https://en.wikipedia.org/wiki/Ramjet
[ref_range]: https://en.wikipedia.org/wiki/Range_(aeronautics)
[ref_rocket_engine]: https://en.wikipedia.org/wiki/Rocket_engine
[ref_rq7]: https://en.wikipedia.org/wiki/AAI_RQ-7_Shadow
[ref_scaneagle]: https://en.wikipedia.org/wiki/Boeing_Insitu_MQ-27_ScanEagle
[ref_scramjet]: https://en.wikipedia.org/wiki/Scramjet
[ref_solar]: https://en.wikipedia.org/wiki/Solar-powered_aircraft
[ref_specific_energy]: https://en.wikipedia.org/wiki/Specific_energy
[ref_thrust_weight]: https://en.wikipedia.org/wiki/Thrust-to-weight_ratio
[ref_tsfc]: https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption
[ref_turbofan]: https://en.wikipedia.org/wiki/Turbofan
[ref_turbojet]: https://en.wikipedia.org/wiki/Turbojet
[ref_two_stroke]: https://en.wikipedia.org/wiki/Two-stroke_engine
[ref_wankel]: https://en.wikipedia.org/wiki/Wankel_engine
[related_post_launch]: {% post_url 2026-06-01-launch_and_recovery_systems_for_fixed_wing_uavs %}
[related_post_lwpla]: {% post_url 2026-05-30-prototyping_fixed_wing_aircraft_with_lightweight_pla_and_fiberglass %}
[related_post_runway]: {% post_url 2026-05-31-runway_sizing_for_fixed_wing_uavs %}
[research_frontiers_electric]: https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2022.752012/full
[research_mdpi_propulsion]: https://www.mdpi.com/2226-4310/8/7/171
