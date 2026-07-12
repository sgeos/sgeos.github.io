---
layout: post
mathjax: true
comments: true
title:  "Electric Energy Systems and the Endurance Budget for Fixed-Wing UAVs"
date:   2026-06-04 09:00:00 +0000
categories: aerospace engineering uav
series: fixed_wing_uav
series_title: Fixed-Wing UAV
series_index: 6
---
<!-- A121 -->
<script>console.log("A121");</script>

The propulsion article in this series sized a single powerplant for one
flight and named solar power, fuel cells, and hybrids as topics for later.
The staged-propulsion article framed a boosted mission as a fixed deposit of
energy spent down against drag.
This article takes up the electric energy system, and its organizing idea is
the same energy budget seen from the opposite side.
Where a boosted vehicle holds a stock of energy banked once and drawn down,
an electric aircraft runs a flow account, a state of charge that is fed by
harvest and drained by consumption and buffered by storage.
The mission is feasible only while that account stays solvent,
and the most demanding version of the question, indefinite flight, is the
condition under which the account refills as fast as it empties.
This piece is framed throughout as the management of that flow budget,
and it builds on the [propulsion companion][related_post_propulsion] for the
power required, the [staged-propulsion companion][related_post_staged] for
the energy-budget idea, and the [airframe companion][related_post_lwpla] for
the wing that must carry the panels and the cells.

## The Energy-Flow Budget

The electric aircraft is governed by a power balance,

$$ \frac{dE}{dt} = P_{\text{in}} - P_{\text{out}}, $$

where $E$ is the energy in store, $P_{\text{in}}$ is whatever the aircraft
harvests or generates, and $P_{\text{out}}$ is the power required to fly plus
the avionics and payload load.
Integrated over the mission, the change in the stored energy is the running
sum of supply minus demand,

$$ \Delta E = \int \left(P_{\text{in}} - P_{\text{out}}\right) dt, $$

and the [state of charge][ref_soc] is just that store expressed as a fraction
of its full value.
This is the same budget the staged-propulsion companion managed,
with one difference that changes everything.
A boosted vehicle receives its whole budget at burnout and spends it down,
so its master variable is a stock, the total energy on hand.
An electric aircraft receives its budget continuously and spends it
continuously, so its master variable is a flow, the balance of the rates.
A mission that draws more than it harvests lives on the buffer and ends when
the buffer empties, while a mission that harvests at least as much as it
draws can in principle continue without end.
The governing condition for sustained flight is therefore not a quantity of
energy but a balance of powers, averaged over whatever cycle the harvest
follows.

## The Demand Side and the Hotel Load

The demand $P_{\text{out}}$ is not all propulsion.
It splits into the power required to fly, which the propulsion companion
sized and which falls when the aircraft flies slower, lighter, or more
efficiently, and the hotel load, the power drawn by everything that is not
the propeller.
The hotel load is the payload sensors, the communications link, the flight
computer and autopilot, and at altitude the heaters and de-icing,
and it behaves very differently from the flight power,
because it is a roughly fixed floor that does not shrink when the aircraft
slows down.
On a fast, heavy aircraft the propulsion dominates and the hotel load is a
footnote, but on the slow, low-power cruise of a long-endurance or solar
aircraft the hotel load can rival or exceed the flight power,
and because it runs through the night when nothing is harvested, it is often
the term that sizes the night-carry store.
The practical consequence is that closing an endurance budget is partly a
matter of driving the hotel load down, by duty-cycling the payload and the
radio rather than only by flying more efficiently,
which is a lever the supply side of the budget cannot reach.

## Storage as the Buffer

Between supply and demand sits the store, and its size and its limits set how
long the aircraft can run a deficit.
A battery is rated by its [specific energy][ref_specific_energy],
on the order of two hundred to two hundred sixty watt-hours per kilogram for
the [lithium-ion cells][ref_lithium_ion] used in aircraft,
and not all of that is usable, because cycling a cell to the bottom shortens
its life, so a design draws only to a chosen
[depth of discharge][ref_dod] and treats the rest as reserve.
The usable energy is the capacity times the depth of discharge times the
efficiency of the path from the cell to the propeller,
and the endurance on stored energy alone is that usable energy divided by the
power required.
Three practical limits qualify that figure.
The store has a round-trip efficiency, since charging and discharging each
lose a few percent, so carrying energy through the night costs more than the
night's demand alone.
Its usable capacity falls in the cold, which is precisely the condition a
night-flying or stratospheric aircraft meets.
And there is a tradeoff between
[specific energy and specific power][ref_specific_power],
because the cells that deliver a heavy launch or climb peak hold less energy
per kilogram than the cells built for endurance,
so a store optimized for one is poor at the other.
This is the battery wall the propulsion companion described,
seen now as the single-charge case of the flow budget,
a store that is filled once on the ground and never refilled in the air.
Everything that follows is a way of refilling it.
For brief, heavy demands such as a launch or a climb, a
[supercapacitor][ref_supercapacitor] can buffer the buffer,
supplying a short burst of power the battery would rather not, and recovering
some of it on the way back down.

## Harvesting Energy from the Sun

The most familiar in-flight source is the sun.
The power a solar array collects is

$$ P_{\text{solar}} = \eta\, S_{\text{cell}}\, G, $$

where $\eta$ is the [cell efficiency][ref_solar_cell_eff],
around twenty to twenty-five percent for good practical cells,
$S_{\text{cell}}$ is the area covered, and $G$ is the
[solar irradiance][ref_solar_irradiance],
about one thousand watts per square meter at the surface under a clear noon
sun and far less at other angles.
Because the irradiance swings from zero at night to its peak at noon, the
array rarely sits at its best operating point,
which is why a solar aircraft carries
[maximum-power-point tracking][ref_mppt] to keep the array near its optimum
as conditions change, a topic named here and left to its own treatment.
The budget over a day is what matters.
A [solar-powered aircraft][ref_solar_aircraft] collects energy through the
daylight hours, spends part of it flying and stores the rest,
then lives through the night on what it stored,
so the daily account closes only if the daylight harvest covers the whole
day's consumption and the store is large enough to carry the dark hours.

## The Scale Gate for Solar Perpetual Flight

Whether that daily account can close depends strongly on size, and the
[square-cube law][ref_square_cube] explains why.
The solar power collected scales with the area of the wing,
which grows as the square of the linear size,
while the power required to fly grows with weight and speed,
and weight grows as the cube of the size for a geometrically similar
aircraft.
Collected power therefore falls behind required power as a design shrinks,
so a small aircraft cannot gather enough sun to fly on it,
and the way to win is to break the similarity by building very light with a
very large wing, which is exactly the shape of the
[high-altitude platform station][ref_haps].
The [Pathfinder][ref_pathfinder] and the [Helios][ref_helios] research
aircraft and the [Zephyr][ref_zephyr] that flies for weeks at a time all
share enormous span, very low wing loading, and a stratospheric cruise above
the weather, and the crewed [Solar Impulse][ref_solar_impulse] made the same
choices at a larger scale.
Even for these aircraft the balance is fragile,
because the daylight is short and the sun is low in winter and at high
latitude, so the same airframe that flies perpetually over the tropics in
summer cannot always do so elsewhere.
A two-meter aircraft is far below the size where solar perpetual flight
closes, so on a small airframe the sun is a range extender rather than a
source of endless flight.

## Harvesting Energy from Hydrogen

A [fuel cell][ref_fuel_cell] carries its energy as hydrogen and converts it
electrochemically rather than by combustion,
and the hydrogen holds far more energy per kilogram than any battery.
A [proton-exchange membrane fuel cell][ref_pemfc] system reaches a specific
energy on the order of one thousand watt-hours per kilogram,
roughly five times a lithium-ion battery, and a liquid-hydrogen system
reaches higher still, which is why the Ion Tiger research vehicle flew for a
full day on compressed hydrogen and for two days on liquid hydrogen,
and why the [Boeing Phantom Eye][ref_phantom_eye] was built around hydrogen
for multi-day high-altitude flight.
In budget terms the fuel cell is a generator that converts stored chemical
energy to electrical power at a steady rate,
sitting between the battery and the combustion engine,
with more endurance than a battery and quieter, water-only exhaust compared
to an engine.
Its costs are the bulk of the hydrogen tank, the difficulty of storing
hydrogen as a compressed gas or a cryogenic liquid, and the water and heat it
must manage, all of which are left to their own treatment here.

## Hybrid Systems

A hybrid system carries two sources and lets each do what it does best.
In a series [hybrid][ref_hybrid_aircraft] arrangement a small engine drives
a generator that charges a battery, and the battery alone turns the
propeller, so the engine can run at its efficient point regardless of the
flight condition.
In a parallel arrangement both the engine and an electric motor drive the
propeller, and the usual division of labor sizes the engine for the steady
cruise and the battery and motor for the peaks of launch and climb,
recovering some energy by regeneration on the descent.
This is the same split the propulsion and staged-propulsion companions
reached from their own directions,
sustained demand met by the dense, refillable energy of fuel,
and brief peaks met by the high power of a battery.
The budget view makes the appeal plain,
because the hybrid fills the flow account from the source best suited to each
part of the mission rather than forcing one source to cover all of it.

## Harvesting Energy from the Air

The atmosphere itself holds energy that a patient airframe can take without
spending any of its own.
A glider climbs in a thermal, the rising column of warm air named in the
[soaring][ref_soaring] literature, and gains potential energy for free,
and an albatross or a suitably controlled UAV performs
[dynamic soaring][ref_dynamic_soaring], extracting energy from the gradient
of wind speed with height by climbing into the faster air and diving back.
These are [energy-harvesting][ref_energy_harvesting] terms on the supply side
of the budget that cost no stored energy at all,
and they connect to the energy-state idea of the staged-propulsion companion,
because a soaring aircraft is trading the wind's energy into the same
potential and kinetic account a boosted vehicle banks.
For a small UAV soaring is a genuine extender of endurance,
and combined with solar collection it can stretch a flight well beyond what
either source alone would allow, at the cost of a flight path dictated by
where the atmospheric energy is rather than where the mission would otherwise
go.

## The Perpetual-Flight Closure

Indefinite flight is the budget closing on itself.
Two conditions must both hold over the harvest cycle, which for a solar
aircraft is a day.
The energy collected through the daylight must at least equal the energy
consumed across the whole twenty-four hours,
and the usable store must be large enough to carry the aircraft through the
darkness at its night-time power.
When both close with margin the aircraft is a pseudo-satellite,
loitering for weeks or months with no fuel to run out,
and when either fails the flight is merely long rather than endless.
Even a closed account is bounded in the end,
because the battery cycles once a day and its usable capacity fades with
calendar and cycle aging,
so the campaign is limited by the life of the store even when the daily
balance never breaks, which is one more reason the closure is sized with
margin rather than to the edge.
The same logic applies to any refilled source.
A fuel cell or a hybrid extends the flight until the hydrogen or the fuel is
gone, a finite but large budget,
while only a harvested source, the sun or the wind, can in principle balance
the account forever.
This is the sharpest statement of the difference from the staged-propulsion
companion, whose boosted stock could only ever be spent down,
never refilled in flight.

## Putting Numbers to It

A worked example tests the budget on the twenty-five-kilogram aircraft of the
earlier articles, which needs about eight hundred watts of electrical power
to cruise.
Over a full day that is about nineteen kilowatt-hours of demand.
Give it a generous solar array, eight tenths of a square meter of cells at
twenty-two percent efficiency, and a good site with about six kilowatt-hours
per square meter of daily sun.
The daily harvest is $0.8 \times 0.22 \times 6000 \approx 1.1$
kilowatt-hours, which is about six percent of the demand,
so this aircraft cannot fly on the sun, and the array only stretches a flight
otherwise run from its battery.
Closing the daily account would require the average power to fall to about
$1100 / 24 \approx 44$ watts, almost twenty times lower,
which is unreachable at two meters and is exactly why the perpetual solar
aircraft is large, light, and slow.
A fuel cell tells a kinder story,
because at roughly one thousand watt-hours per kilogram it carries about five
times the energy of a battery of equal mass,
so the same airframe that flies for tens of minutes on a battery flies for
hours on hydrogen, which is the gap the Ion Tiger and the Phantom Eye
demonstrate.
None of these is a final design, but together they show the budget at work,
the small aircraft drawing far faster than the sun can supply,
the fuel cell deepening the store, and only the large solar craft closing the
account against the night.

## Out of Scope

Several neighboring subjects are deliberately excluded.
The cell chemistry, the battery-management electronics, and the thermal and
safety control of a large pack are a field of their own,
as is the design of a maximum-power-point tracker and the layout and physics
of the photovoltaic cells.
The stack design, the humidification, and the water and heat management of a
fuel cell, and the storage of hydrogen as a compressed gas or a cryogenic
liquid, are named but not engineered here.
The control laws that schedule a hybrid between its sources, and the
trajectory planning that finds and exploits atmospheric energy for soaring,
are left to their own treatments.
The sizing of the powerplant for a single flight is the subject of the
propulsion companion, and the one-time energy stock of a boosted vehicle is
the subject of the staged-propulsion companion, and neither is repeated here.

## Conclusion

An electric aircraft is the management of an energy account that is filled and
drained in flight.
The power balance, supply minus demand, sets whether the store grows or
shrinks, and the integral of that balance over the harvest cycle decides
whether a mission is long or endless.
A battery is the buffer, a solar array or a fuel cell or a hybrid generator
is the supply, and the atmosphere itself can be a supply for an airframe
willing to soar.
Sustained flight is a balance of powers rather than a quantity of energy,
and indefinite flight is the cycle closing on itself, the daily sun covering
the daily demand and the battery carrying the night,
which the large, light, high-flying solar aircraft achieves and the small one
does not.
Seen this way the whole series is one subject,
the management of an energy budget, told as a stock when a boost banks it all
at once and as a flow when an electric system meters it out,
and a builder who writes down the balance of powers can read off the
endurance with numbers rather than hope.

## References

- [Reference, Airbus Zephyr][ref_zephyr]
- [Reference, Boeing Phantom Eye][ref_phantom_eye]
- [Reference, Depth of Discharge][ref_dod]
- [Reference, Dynamic Soaring][ref_dynamic_soaring]
- [Reference, Energy Harvesting][ref_energy_harvesting]
- [Reference, Fuel Cell][ref_fuel_cell]
- [Reference, Helios Prototype][ref_helios]
- [Reference, High-Altitude Platform Station][ref_haps]
- [Reference, Hybrid Electric Aircraft][ref_hybrid_aircraft]
- [Reference, Lift in Soaring][ref_soaring]
- [Reference, Lithium-Ion Battery][ref_lithium_ion]
- [Reference, Maximum Power Point Tracking][ref_mppt]
- [Reference, NASA Pathfinder][ref_pathfinder]
- [Reference, Proton-Exchange Membrane Fuel Cell][ref_pemfc]
- [Reference, Solar Impulse][ref_solar_impulse]
- [Reference, Solar Irradiance][ref_solar_irradiance]
- [Reference, Solar-Cell Efficiency][ref_solar_cell_eff]
- [Reference, Solar-Powered Aircraft][ref_solar_aircraft]
- [Reference, Specific Energy][ref_specific_energy]
- [Reference, Specific Power][ref_specific_power]
- [Reference, Square-Cube Law][ref_square_cube]
- [Reference, State of Charge][ref_soc]
- [Reference, Supercapacitor][ref_supercapacitor]
- [Related Post, Propulsion and Power Sizing for Small Fixed-Wing UAVs][related_post_propulsion]
- [Related Post, Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass][related_post_lwpla]
- [Related Post, Staged and Boosted Propulsion for Small Fixed-Wing UAVs][related_post_staged]
- [Research, Comprehensive Review on Electric Propulsion System of UAVs (Frontiers)][research_frontiers_electric]
- [Research, Electric Propulsion and Hybrid Energy Systems for Solar-Powered UAVs (MDPI Drones)][research_mdpi_solar]
- [Research, Series and Parallel Hybrid Propulsion Systems for UAVs (MDPI Aerospace)][research_mdpi_hybrid]

[ref_dod]: https://en.wikipedia.org/wiki/Depth_of_discharge
[ref_dynamic_soaring]: https://en.wikipedia.org/wiki/Dynamic_soaring
[ref_energy_harvesting]: https://en.wikipedia.org/wiki/Energy_harvesting
[ref_fuel_cell]: https://en.wikipedia.org/wiki/Fuel_cell
[ref_haps]: https://en.wikipedia.org/wiki/High-altitude_platform_station
[ref_helios]: https://en.wikipedia.org/wiki/Helios_Prototype
[ref_hybrid_aircraft]: https://en.wikipedia.org/wiki/Hybrid_electric_aircraft
[ref_lithium_ion]: https://en.wikipedia.org/wiki/Lithium-ion_battery
[ref_mppt]: https://en.wikipedia.org/wiki/Maximum_power_point_tracking
[ref_pathfinder]: https://en.wikipedia.org/wiki/NASA_Pathfinder
[ref_pemfc]: https://en.wikipedia.org/wiki/Proton-exchange_membrane_fuel_cell
[ref_phantom_eye]: https://en.wikipedia.org/wiki/Boeing_Phantom_Eye
[ref_soaring]: https://en.wikipedia.org/wiki/Lift_(soaring)
[ref_soc]: https://en.wikipedia.org/wiki/State_of_charge
[ref_solar_aircraft]: https://en.wikipedia.org/wiki/Solar-powered_aircraft
[ref_solar_cell_eff]: https://en.wikipedia.org/wiki/Solar-cell_efficiency
[ref_solar_impulse]: https://en.wikipedia.org/wiki/Solar_Impulse
[ref_solar_irradiance]: https://en.wikipedia.org/wiki/Solar_irradiance
[ref_specific_energy]: https://en.wikipedia.org/wiki/Specific_energy
[ref_specific_power]: https://en.wikipedia.org/wiki/Specific_power
[ref_square_cube]: https://en.wikipedia.org/wiki/Square%E2%80%93cube_law
[ref_supercapacitor]: https://en.wikipedia.org/wiki/Supercapacitor
[ref_zephyr]: https://en.wikipedia.org/wiki/Airbus_Zephyr
[related_post_lwpla]: {% post_url 2026-05-30-prototyping_fixed_wing_aircraft_with_lightweight_pla_and_fiberglass %}
[related_post_propulsion]: {% post_url 2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs %}
[related_post_staged]: {% post_url 2026-06-03-staged_and_boosted_propulsion_for_fixed_wing_uavs %}
[research_frontiers_electric]: https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2022.752012/full
[research_mdpi_solar]: https://www.mdpi.com/2504-446X/9/12/846
[research_mdpi_hybrid]: https://www.mdpi.com/2226-4310/9/2/63
