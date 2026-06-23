---
layout: post
mathjax: true
comments: true
title:  "Electricity and Energy Storage for Off-Grid Space Colonization Analogs"
date:   2026-06-29 09:00:00 +0000
categories: aerospace engineering space-studies analog-facilities
---

<!-- A153 -->
<script>console.log("A153");</script>

The
[introduction to off-grid space colonization analog facilities][related_post_analog_intro]
that opened this category
treats the electricity subsystem
as the highest-leverage layer
in the facility-system stack.
Every other subsystem
draws power
from the electricity layer.
The water recovery process,
the food production cycle,
the habitat thermal control,
the communications link,
and the computational mission system
all stop
when the electricity layer stops.
This article
treats the electricity subsystem
in its own right
under the framing
that battery storage
is the architectural keystone
around which the rest of the electrical system
is dimensioned.

The space-colonization analog
provides the contextual flavour
of the analysis,
but the engineering content
generalises
without modification
to any off-grid electrical system
that the same architectural constraints govern.
A remote research station,
an off-grid residential cabin,
a disaster relief installation,
a remote mining or oilfield camp,
a maritime vessel at extended range,
and a forward operating base
each face
the same generation-load mismatch problem
that the analog faces.
The sizing equations,
the dependent-component reasoning,
the standards references,
and the no-battery alternatives
apply across all such cases.
The space-only options
and the keystone-breakdown cases
are the parts
that are specific
to the orbital and planetary context.

The framing
is constrained
to the dominant analog architecture,
which is
photovoltaic primary generation
with wind or other renewable supplementation
and a chemical-fuel generator
for redundancy.
In that architecture,
the battery bank
is the central component
because it decouples
the intermittent generation profile
from the continuous load profile
the habitat imposes.
The photovoltaic array,
the charge controllers,
the inverter,
the generator,
the wiring,
the protective devices,
and the load-shedding strategy
each take their dimensions
from the battery bank.
A subset of architectures
discards the battery bank
in favour of continuous baseload generation,
thermal storage,
or mechanical storage.
The article treats those alternatives
as a documented footnote
to the dominant architecture
rather than as the recommended choice
for a new analog programme.

## The Battery Storage Keystone

A space colony
and its terrestrial analog
both face
the same fundamental electrical problem.
The habitat
demands continuous power
across the diurnal cycle
and across the multi-day cycle
that weather or seasonal variation imposes.
The available renewable generation
matches neither cycle.
Solar generation
is zero
through the local night
and reduced
under cloud cover
or dust accumulation.
Wind generation
is variable
across hours, days, and seasons.
The chemical-fuel generator
delivers power on demand
but consumes a finite fuel supply
that the analog
must either import
or accept as a closed-system constraint.

Battery storage
resolves the mismatch
between generation profile
and load profile
by absorbing
the surplus generation
when it occurs
and releasing it
when the load demands it.
Without storage,
the architecture
must satisfy load
through one of three alternatives.
The first
is continuous baseload generation,
which requires
either chemical fuel
on a continuous resupply schedule
or a nuclear primary
that the regulatory and supply chain
will rarely permit
for a terrestrial analog.
The second
is direct-coupled operation,
in which loads
run only when generation is available.
A direct-coupled architecture
cannot support
the life-support, refrigeration,
or communication loads
that the analog must operate continuously.
The third
is acceptance of intermittent operation,
which the crewed analog
cannot accept
for safety-critical loads.

The battery bank
therefore
sits at the centre
of the architecture
as the component
that makes intermittent generation
operationally compatible
with continuous load.
Every dependent component
exists either to charge the battery
or to discharge the battery
under controlled conditions.

## Battery Sizing From First Principles

The required battery capacity
follows from the load profile
and the worst-case generation gap.
Let $P_{load}$ denote
the time-averaged load power
that the habitat draws
across the cycle of interest,
let $t_{dark}$ denote
the duration of the worst expected generation gap
in hours,
let $DoD$ denote
the allowable depth of discharge
of the chosen battery chemistry
as a fraction
of nameplate capacity,
and let $\eta_{system}$ denote
the round-trip system efficiency
across the inverter, conductor, and conversion losses.
The required usable energy
the battery bank must store
is

$$ E_{usable} = P_{load} \cdot t_{dark} $$

and the required nameplate capacity is

$$ E_{nameplate} = \frac{P_{load} \cdot t_{dark}}{DoD \cdot \eta_{system}} $$

A small worked example
makes the magnitudes concrete.
A modest analog habitat
with a continuous load
of two kilowatts
across a twelve-hour worst-case dark period,
operating on
lithium iron phosphate cells
at eighty-percent depth of discharge
and ninety-percent round-trip efficiency,
requires

$$ E_{nameplate} = \frac{2{,}000 \text{ W} \cdot 12 \text{ h}}{0.80 \cdot 0.90} \approx 33{,}000 \text{ Wh} \approx 33 \text{ kWh} $$

A larger habitat
with a twenty-kilowatt continuous load
across a forty-eight-hour worst-case generation gap
under the same chemistry
and efficiency assumptions
requires
approximately
one thousand three hundred kilowatt-hours
of nameplate storage,
which is
forty times the smaller case
in proportion
to the forty-fold increase
in load times duration.

The choice of chemistry
sets the achievable depth of discharge.
A lithium iron phosphate bank
permits eighty to ninety percent depth of discharge
with cycle life
in the three thousand to six thousand range
at that depth.
A lithium nickel manganese cobalt bank
permits similar depth of discharge
with higher energy density
but lower cycle life
in the one thousand to two thousand range.
A flooded or absorbent-glass-mat lead-acid bank
permits only
approximately fifty percent depth of discharge
without rapid degradation
and provides
cycle life
in the five hundred to one thousand five hundred range.
A vanadium redox flow battery
permits effectively unlimited depth of discharge
with cycle life
exceeding ten thousand cycles
but at lower energy density
and higher capital cost per kilowatt-hour.

The cycle-life budget
sets the replacement cadence
for the battery bank.
A three-thousand-cycle bank
operating one full cycle per day
delivers approximately eight years of service.
A one-thousand-cycle bank
under the same usage
delivers under three years.
The replacement cost
is a recurring operating expense
that the multi-year analog programme
must budget for.

The round-trip efficiency
$\eta_{system}$
that appears in the sizing equation
is the product

$$ \eta_{system} = \eta_{charge} \cdot \eta_{battery} \cdot \eta_{discharge} \cdot \eta_{inverter} $$

across the cascade
from photovoltaic generation
through the charge controller
into the battery
and back out
through the inverter
to the load.
Typical values
for the modern lithium-iron-phosphate-plus-pure-sine-wave-inverter cascade
yield
a system round-trip efficiency
of approximately
eighty-five to ninety-two percent
under nominal load,
falling
to seventy percent or below
under deep partial-load operation
where the inverter standby consumption
dominates.
The system designer
budgets against the realistic operating efficiency
rather than the rated nameplate efficiency
of any single component.

The direct-current bus voltage
that the battery bank assembles to
imposes a system-wide tradeoff.
A twelve-volt bus
is the marine and recreational-vehicle standard
that minimises shock hazard
at the cost
of large conductor cross-section
for any non-trivial power.
A twenty-four-volt or forty-eight-volt bus
halves or quarters the conductor current
for the same power
and is the standard
for residential off-grid and small commercial installations.
A four-hundred-volt or eight-hundred-volt bus
is the utility-scale and industrial standard
that minimises conductor mass
at the cost
of more demanding insulation
and electrical safety qualification.
The conductor current
at a given power $P$ and bus voltage $V$
is simply

$$ I = \frac{P}{V} $$

and the conductor mass
scales with the square
of the current
through the resistive-loss budget.

## Dependent Components in Order of Dependency

The battery bank
dimensioned in the previous section
sets the rating of every component
in the electrical system.

### Generation Capacity

The photovoltaic array
must replace
the energy discharged from the battery
within the daily solar window
under realistic capacity factor.
Let $E_{daily}$ denote
the daily energy demand,
let $G_{site}$ denote
the average solar irradiance
at the chosen site
in kilowatt-hours per square metre per day,
let $\eta_{PV}$ denote
the photovoltaic conversion efficiency,
and let $CF$ denote
the combined capacity factor
that accounts for soiling, temperature derating,
wiring losses, and seasonal variation.
The required photovoltaic array area is

$$ A_{PV} = \frac{E_{daily}}{G_{site} \cdot \eta_{PV} \cdot CF} $$

For a habitat
drawing two kilowatts continuously
across the twenty-four-hour day,
the daily energy demand
is forty-eight kilowatt-hours.
At a southwestern United States analog site
with average irradiance
of approximately five and a half kilowatt-hours per square metre per day,
monocrystalline silicon panels
at twenty-one-percent efficiency,
and combined capacity factor
of seventy-five percent,
the array area is

$$ A_{PV} = \frac{48 \text{ kWh}}{5.5 \cdot 0.21 \cdot 0.75} \approx 55 \text{ m}^2 $$

The same load
at a Mars-analog Atacama Desert site
with similar irradiance
yields a similar array area
because the terrestrial Mars analog
operates under terrestrial solar conditions,
not Martian solar conditions.
A genuine Mars-surface installation
would face
approximately forty-three percent
of the terrestrial irradiance
at the same latitude
plus the multi-month dust storm degradation
that the terrestrial analog cannot reproduce.
This is one of the
environmental fidelity limits
the prior survey article describes.

The photovoltaic panel
loses power output
as cell temperature rises
above the rated standard test condition
of twenty-five degrees Celsius
through the temperature coefficient
$\gamma$
that the panel datasheet specifies.
The temperature-derated output power is

$$ P(T) = P_{STC} \cdot \left( 1 + \gamma \cdot \left( T - 25 \text{ }^{\circ}\mathrm{C} \right) \right) $$

with $\gamma$
typically in the range
of minus zero point three
to minus zero point four percent per degree Celsius
for crystalline silicon panels.
A panel operating
under a forty-five-degree Celsius cell temperature
on a hot southwestern United States afternoon
delivers approximately
ninety-two percent
of the standard test condition rating,
which the array sizing
must absorb
into the capacity factor.

Wind generation
supplements solar
where the site provides it.
A site
with steady wind
in the seven to ten metre per second range
can carry
twenty to forty percent
of the load
under typical conditions.
The McMurdo Station
Ross Island Wind Energy Project
operates three Enercon E33 turbines
of three hundred thirty kilowatt rating each,
supplying approximately ten percent of station load
in average conditions
and reducing diesel consumption
by approximately four hundred sixty thousand litres per year.

### Charge Controllers

The charge controller
sits between the photovoltaic array
and the battery bank
and regulates the charge current
to protect the battery
from overcharging.
Two principal architectures
are in use.
The first
is pulse-width modulation
which is the simpler and lower-cost approach
that operates the array
at the battery voltage.
The second
is maximum power point tracking
which is the higher-efficiency approach
that operates the array
at its maximum-power voltage
and converts the array output
to the battery voltage
through a direct-current-to-direct-current converter.
The maximum power point tracker
adds approximately twenty to thirty percent yield
under variable conditions
at the cost
of higher capital expense.

The controller rating
must match
the maximum short-circuit current
of the photovoltaic array
with a safety margin
that the
[National Electrical Code Article 690][ref_nec_690]
specifies
at one hundred and twenty-five percent
of the array short-circuit current
under United States installations.
The equivalent international standard
is
[IEC 62548][ref_iec_62548].

### Inverters and Power Conditioning

The inverter
converts the battery direct-current output
to the alternating-current voltage
the habitat loads expect.
The inverter rating
must exceed
the maximum simultaneous load
the habitat will impose.
A pure sine-wave inverter
is required
for sensitive electronics,
motors,
and laboratory instruments.
A modified sine-wave inverter
is sometimes acceptable
for resistive loads only
and is not appropriate
for an analog facility
operating
mixed crew habitat loads.

The inverter efficiency
typically ranges
from ninety to ninety-six percent
under rated load
and falls
under light load
where the standby consumption
becomes a significant fraction
of the throughput.
A two-kilowatt inverter
drawing twenty watts of standby power
loses one percent of throughput
under full load
and ten percent under two-hundred-watt light load,
which the system designer
must account for
in the daily energy budget.

The inverter
also handles
the synchronisation
with the chemical-fuel generator
when both sources
operate simultaneously
through an automatic transfer switch.
The
[Underwriters Laboratories 1741][ref_ul_1741]
standard
governs the inverter requirements
for grid-interactive operation
under United States installations.

### Generator Backup

The chemical-fuel generator
sizes for
the worst-case continuous load
that the battery and renewable generation cannot satisfy
together.
A propane or diesel generator
at the kilowatt-to-ten-kilowatt scale
is the standard analog choice.
The fuel consumption rate
sets the resupply cadence
that the analog
must either import on schedule
or accept as a closed-system constraint.

The fuel consumption rate
follows from the engine-generator efficiency
and the fuel lower heating value.
For an electrical output power $P_{elec}$
operating across time $t$
on a fuel of lower heating value $LHV$
in joules per kilogram
through an end-to-end engine-generator efficiency $\eta_{gen}$
in the twenty to thirty-five percent range
for small internal combustion units,
the consumed fuel mass is

$$ m_{fuel} = \frac{P_{elec} \cdot t}{\eta_{gen} \cdot LHV} $$

A five-kilowatt propane generator
operating at seventy-five-percent load
consumes
approximately two litres of propane per hour,
which is forty-eight litres per twenty-four hours
of continuous operation.
A one-month standalone reserve
requires approximately one thousand four hundred litres of propane,
which fits in a single residential tank
of standard size.
The fuel-storage volume
is one of the visible signatures
that the analog
is dependent on
the terrestrial fuel supply chain
rather than producing its own fuel
inside the envelope.

### Load Shedding Strategy

The load-shedding strategy
prioritises loads
into tiers
that the system disconnects
as the battery state of charge drops
through defined thresholds.
A typical tier structure
places life support,
critical computing,
and communications
in the first tier
that the system never sheds.
Refrigeration, cooking, and water pumping
sit in the second tier
that the system sheds
under deep discharge.
Lighting beyond the essential
and laboratory equipment beyond the critical
sit in the third tier
that the system sheds
under moderate discharge.
The load-shedding logic
is implemented
either in firmware
on a battery management system
or in the building automation controller
that the analog operator monitors.

The shed schedule
is part of the analog mission rules
that the crew operates under
and matches
the procedure
the real space mission
would impose
under similar conditions.

### Conductor Sizing and Voltage Drop

The conductor cross-section
between every pair of components
in the electrical system
must satisfy two distinct constraints.
The first
is ampacity,
which is the maximum continuous current
the conductor can carry
without exceeding its insulation temperature limit.
The
[National Electrical Code Article 310][ref_nec_310]
publishes ampacity tables
for common conductor sizes,
insulation classes,
and installation conditions.
The second
is acceptable voltage drop
across the conductor length,
which the
[National Electrical Code informational note in Article 210][ref_nec_210]
recommends to be limited
to three percent
on branch circuits
and five percent
across the combined feeder and branch path.

The voltage drop
across a round-trip conductor
of length $L$
carrying current $I$
through a conductor of resistance per unit length $r$
is

$$ V_{drop} = 2 \cdot I \cdot r \cdot L $$

where the factor of two
accounts for both
the source and return conductors.
A fifty-amp direct-current circuit
running thirty metres
on standard six-gauge American Wire Gauge copper
at a resistance of approximately one point three milliohms per metre
suffers approximately
four volts of drop,
which is
acceptable on a forty-eight-volt bus
at eight percent
but unacceptable
on a twelve-volt bus
at thirty-three percent.
The system designer
sizes conductor cross-section
upward
until both ampacity
and voltage-drop constraints
are satisfied
across the worst case.

## No-Battery Architectures

The dominant analog architecture
uses chemical battery storage
as the keystone.
A subset of architectures
discards the battery bank
in favour of other strategies
that satisfy
the continuous-load constraint.

### Continuous Baseload Fission

A small modular fission reactor
delivers continuous power
without the intermittency
that solar and wind impose.
The
[NASA Kilopower demonstrator][ref_kilopower]
known as KRUSTY
ran the full-power twenty-eight-hour test
on 20 March 2018
at the Nevada National Security Site,
demonstrating
the one-kilowatt-electric design point
from approximately five and a half kilowatts thermal
through a uranium-235 reactor
coupled to Stirling-cycle converters.
The
[Fission Surface Power programme][ref_fission_surface_power]
that NASA initiated in 2022
funded
forty-kilowatt-class designs
through Lockheed Martin,
Westinghouse,
and the IX team
of Intuitive Machines and X-energy,
with the programme
accelerated in August 2025
to a one-hundred-kilowatt-class target
for lunar surface deployment
in the early 2030s.
A terrestrial fission analog
faces regulatory barriers
that no contemporary analog programme
has cleared.

### Geothermal Primary

A geothermal source
delivers continuous heat
that drives an electricity generator
through a Rankine or Stirling cycle.
A geothermal-primary analog site
in Iceland
or on the Big Island of Hawaii
could plausibly operate
without batteries
because the geothermal source
is constant.
The fidelity argument
to a lunar or Mars colony
is weaker than the photovoltaic case
because no candidate space colony
has access
to a geothermal resource
on the scale a terrestrial analog
would use.

### Thermal Storage

Thermal storage
through molten salt
or phase-change materials
holds energy
in the form of heat
that the system converts back
to electricity
through a heat engine
when generation drops.
Concentrated solar power plants
in commercial operation
use molten salt storage
to deliver
six to twelve hours
of continuous power
after sunset.
A small-scale analog implementation
faces a capital-cost barrier
that the chemical battery
does not present.

### Mechanical Storage

Mechanical storage
through flywheels,
pumped-hydroelectric,
or compressed air
holds energy
in kinetic, potential, or pressure form
that the system converts back
to electricity
through a generator
when generation drops.
Flywheel storage
delivers power for seconds to minutes
and is suitable for
power-quality applications
rather than long-duration storage.
Pumped-hydroelectric
requires
two reservoirs at different elevations
that few analog sites support.
Compressed-air storage
faces round-trip efficiency
in the fifty to seventy percent range
that the battery bank exceeds.

### Hydrogen Production and Fuel Cells

Hydrogen production
through electrolysis
during surplus generation
and fuel cell consumption
during deficit
substitutes for the battery bank
across longer storage durations
than the battery economically supports.
The round-trip efficiency
of the hydrogen path
is approximately thirty to forty percent,
significantly below
the eighty to ninety percent
the lithium battery delivers.
The hydrogen path
becomes economically attractive
for storage durations
beyond approximately one week,
which is the seasonal storage regime
that lunar polar
and outer-planet missions
would face.

## Terrestrial-Only Cheats

The terrestrial analog
operates inside
a planet that provides
an electricity grid,
a fuel supply chain,
and a network of adjacent facilities
that no space colony will have access to.
The analog
can lean on these
to varying degrees
and report the dependence
honestly,
or it can hide the dependence
and report the result
as if it were closed.
Three principal cheats
are common enough
to deserve enumeration.

The first cheat
is grid-tied operation
in which
the analog connects
to the terrestrial electricity grid
through a service drop
and draws power
on demand
when the local generation
falls short.
A grid-tied analog
imposes effectively
no constraint on its electricity budget
and reports
on its terrestrial grid connection
rather than on its colonial autonomy.
The grid-tied option
is the default
for short-duration urban analogs
and is incompatible
with the honesty model
the prior survey article describes.

The second cheat
is trucked-in diesel or propane resupply
on a cadence shorter
than any plausible space mission resupply schedule.
A weekly diesel delivery
to the analog site
is a confession
that the analog
is dependent
on the terrestrial fuel supply chain
at the weekly cadence.
The honest fuel-budget regime
imports fuel
on the resupply cadence
the simulated mission would impose,
which for a Mars mission
is the synodic period
of approximately seven hundred eighty days.

The third cheat
is cogeneration with an adjacent facility
in which
the analog shares
electricity, fuel, or steam
with a neighbouring research station,
hotel,
or military base.
The cogeneration arrangement
reduces the analog operating cost
but means
the analog
is operating
on the combined energy budget
of two installations
rather than its own.

The honest analog
documents the dependence
on each of these terrestrial paths
in the mission report
so the reader
can deduce
which conclusions
the analog result
licenses.

## Space-Only Options

A symmetric category exists
of options
that the actual space mission can exercise
but that the terrestrial analog cannot.
The terrestrial analog
that ignores these options
is making an implicit choice
that the actual mission
might not make.
A brief enumeration
sets the context.

### Lunar Peaks of Eternal Light

The lunar polar regions
contain topographic peaks
whose elevation
keeps them in sunlight
through most of the lunar year
because the lunar axial tilt
of approximately one and a half degrees
keeps the polar terminator near the horizon.
A lunar polar base
that sites its photovoltaic array
on a
[peak of eternal light][ref_artemis_base_camp]
faces
a much smaller storage requirement
than a lunar equatorial base
that endures
a fourteen-day local night.
The Shackleton crater rim
near the lunar south pole
contains points
identified as Point A and Point B
that receive approximately
eighty-one and eighty-two percent
solar illumination
through the lunar year,
with other rim peaks
reaching as high as ninety-four percent
and a longest continuous eclipse
of approximately forty-three hours.
The NASA Artemis south polar landing region
catalogue
takes these illumination values
into account
in its candidate site list.

### Mars Solar at Reduced Irradiance

The Mars surface
receives
approximately forty-three percent
of Earth solar irradiance
at the same latitude
because Mars orbits
at one and a half times Earth distance.
A Mars colony
sizing for the same load profile
as a terrestrial analog
requires
approximately two and a third times
the photovoltaic array area.
The Mars atmosphere
imposes
additional intermittency
through the regional and global dust storm cycle
that can degrade solar output
by fifty to ninety percent
across the multi-week to multi-month storm duration.
The
[InSight lander mission][ref_insight]
ended in December 2022
when accumulated dust
on the solar panels
reduced power output
below the operational threshold,
which is the empirical record
the analog tradition
has on this failure mode.

### Space-Based Solar Power

The
[space-based solar power architecture][ref_sbsp]
that
Peter Glaser
proposed in 1968
places
the photovoltaic array
in geosynchronous orbit
or another space location
that receives
continuous solar irradiance
without atmospheric attenuation
or diurnal cycle,
and beams the collected power
to a ground receiver
through a microwave or laser link.
The end-to-end efficiency
of the architecture
is approximately ten to thirty percent
in current concept studies,
with theoretical ceilings
nearer forty-five percent
under optimised components,
because the conversion chain
from photovoltaic
to direct current
to microwave
through atmospheric transit
to rectenna
to alternating current
imposes losses at each stage.
The
[Caltech Space Solar Power Project][ref_caltech_sspp]
launched the
[MAPLE microwave power-transfer demonstrator][ref_maple]
in January 2023
aboard the SSPD-1 spacecraft
and beamed power
to a receiver on the Caltech campus rooftop
in June 2023,
with detected ground power
below one tenth of a microwatt
as a proof of concept
rather than as appreciable energy delivery.
The
[European Space Agency Solaris programme][ref_esa_solaris]
that ESA approved
at the 2022 Ministerial Council
funds the feasibility studies
through the mid-2020s.
The terrestrial analog
cannot exercise this option
because the orbital segment
is the principal capital expense
that no terrestrial deployment can replicate.

### Orbital Reflectors

A space mirror
in low Earth orbit
or in geosynchronous orbit
reflects solar irradiance
to a ground receiver
or to another spacecraft
that is otherwise in darkness.
The
[Znamya experiments][ref_znamya]
that the Russian space programme conducted
demonstrated
the orbital mirror concept
through the Znamya 2 deployment in February 1993,
which briefly illuminated
sites on the Earth surface
through a twenty-metre mirror
deployed from a Progress resupply vehicle.
The Znamya 2.5 deployment in 1999
failed to deploy.
The
[soletta concept][ref_soletta]
that Krafft Ehricke described
in 1978
proposed permanent orbital mirrors
for terraforming
or polar illumination
on a much larger scale,
with the related Lunetta variant
illuminating settlements
on the lunar surface
through the lunar night.
The terrestrial analog
cannot reproduce
the orbital mirror architecture
because the mirror
is by definition
above the analog site.

### Statite Architecture

The
[statite concept][ref_statite]
that
Colin McInnes
described in 1989
and Robert Forward
named and patented in 1993
uses
solar sail radiation pressure
to hold a spacecraft
in a non-Keplerian station
above the polar regions
of the Sun
where continuous solar irradiance is available
for power generation
at modest intensity
relative to the close-in case
but with full station-keeping
provided by the radiation pressure itself.
A statite-based power architecture
for a lunar or Mars colony
would beam power
to the surface site
on a continuous basis
without the diurnal cycle
that surface-mounted photovoltaic
imposes.
The architecture
is forward-looking
and no demonstrator has flown,
but the concept
sits in the public record
as the limiting case
of the orbital power generation tradition.

## Where the Keystone Framing Breaks Down

The battery-as-keystone framing
holds across
the dominant analog architecture
and across the Mars surface
and lunar polar mission cases.
Three cases
break the framing.

The first is the
lunar equatorial fourteen-day night.
A photovoltaic-and-battery architecture
at a lunar equatorial site
must store
approximately three hundred and thirty hours
of continuous load
in the battery bank,
which scales the battery mass and cost
beyond the range
where the architecture is economically competitive
with a nuclear primary.
This is the operational reason
the
[Fission Surface Power programme][ref_fission_surface_power]
targets
lunar surface deployment
through the early 2030s.

The second is the
Mars regional and global dust storm cycle.
A dust storm
can reduce
photovoltaic output
by fifty to ninety percent
across weeks to months
that no economically sized battery bank
can bridge.
The Mars colony architecture
therefore
either accepts intermittent operation
during the dust storm season
or carries
a backup chemical or nuclear primary
that the battery-keystone framing does not contemplate.

The third is the
outer planet solar weakness.
At Jupiter distance
of approximately five point two astronomical units,
solar irradiance falls
to approximately
one twenty-seventh of Earth
which is too low
to support a photovoltaic primary
on any reasonable area.
Outer-planet mission architectures
therefore default to
radioisotope thermoelectric generation
or fission primary
without the battery bank
in the central architectural role.

## Generalisation Beyond the Space Analog Context

The architecture and sizing reasoning
that this article presents
applies without modification
to any off-grid electrical system
that the same generation-load mismatch problem governs.
A few representative cases
make the generalisation concrete.

A residential off-grid cabin
in a remote terrestrial location
implements
the same photovoltaic-and-battery primary
with chemical-fuel generator backup
that the analog implements.
The sizing equations,
the chemistry choice,
the standards references,
and the load-shedding logic
transfer directly.
The terrestrial-only cheats
do not apply
because the cabin
is already a true off-grid installation.
The space-only options
do not apply
because the cabin
is not above the atmosphere.

A remote research station
in the Antarctic, the Arctic,
or another remote terrestrial environment
implements
a hybrid architecture
that combines the photovoltaic-and-battery primary
with wind generation,
chemical-fuel generator backup,
and occasionally
geothermal or hydroelectric supplementation.
The dependent-component reasoning
applies directly.
The peak-irradiance and seasonal-variation considerations
that the analog inherits
from the chosen site
also govern the remote-research-station design.

A disaster relief installation
that operates
after a grid outage
faces an off-grid problem
on a shorter time scale
than the multi-year analog.
The same battery-keystone framing applies,
with the generator runtime budget
typically dominating the architecture
because the duration is short
and the photovoltaic deployment time
is constrained.

A maritime vessel at extended range
operates an inverter-and-battery system
that the engine-generator charges
when the engine is running
and that supplies hotel and instrument loads
when the engine is shut down.
The same dependency tree applies.

A military forward operating base
operates a hybrid microgrid
under the same architecture
with security and survivability constraints
that the analog does not impose
but that do not change the underlying sizing logic.

The recommended reading sequence
for an engineer
who is designing
a new off-grid installation
in any of these contexts
is to read this article
for the architecture,
then to consult
the relevant standards
through the
[National Electrical Code][ref_nec_690]
and
[IEC 62548][ref_iec_62548]
for the specific code and component requirements
the chosen jurisdiction imposes.

## Out of Scope

This article
treats the electricity layer
of the analog facility
in survey form
and necessarily defers
several topics
to subsequent treatments.

**Detailed battery management system engineering.**
The firmware, monitoring, and protection logic
that governs a multi-cell battery bank
is a self-contained engineering subject
that this article
does not treat
beyond noting the load-shedding role.

**Power-electronics circuit design.**
The inverter, charge controller, and converter topologies
and their semiconductor selection
sit inside
a power-electronics engineering treatment
that this article
does not attempt.

**Grid-forming and islanding behaviour.**
The detailed dynamics
of an off-grid microgrid
with multiple inverters,
multiple sources,
and reactive loads
is a self-contained subject
that this article
does not treat
beyond noting the
[Underwriters Laboratories 1741][ref_ul_1741]
governing standard.

**Nuclear safety and licensing for analog use.**
The regulatory pathway
that a terrestrial fission analog
would need to clear
is a substantive obstacle
that this article
mentions but does not treat
in detail.

**Space-based solar power economics.**
The economic models
that the European Space Agency Solaris programme,
the Caltech Space Solar Power Project,
the Japan Aerospace Exploration Agency roadmap,
and the China programme
publish
deserve a dedicated treatment
that this article
does not attempt.

**Energy storage chemistry research.**
The materials research
that drives
battery chemistry development
is a self-contained research field
that this article
treats only at the level
of the chemistries
currently in commercial use.

## Conclusion

The off-grid electricity subsystem
of a space-colonization analog
is best dimensioned
around the battery bank
as the architectural keystone.
The battery sizing
follows from
the load profile,
the worst-case generation gap,
the chosen chemistry,
and the round-trip system efficiency.
Every dependent component
takes its rating
from the battery sizing
under the dominant
photovoltaic-and-wind-with-generator-backup architecture.

A small number of alternative architectures
discard the battery bank
in favour of continuous baseload generation,
thermal storage,
mechanical storage,
or hydrogen production.
Each alternative
faces a barrier
that has prevented
adoption in the current analog inventory,
ranging from
the regulatory barrier
that prevents terrestrial fission analogs
to the capital-cost barrier
that prevents commercial thermal storage
at the scale the analog needs.

The terrestrial analog
can cheat
by leaning on
the grid,
the diesel supply chain,
or an adjacent facility,
and the honest analog
documents the dependence
rather than reporting
on a closed system
it does not operate.
The actual space mission
has options
that the terrestrial analog cannot exercise,
including the lunar peaks of eternal light,
space-based solar power,
orbital reflectors,
and the statite architecture,
which the analog tradition
should mention
even though
it cannot reproduce them.

The keystone framing
breaks down
at the lunar equatorial fourteen-day night,
at the Mars dust storm season,
and at the outer-planet solar regime,
each of which
demands a non-battery primary
that the architecture
must accommodate
separately.

The engineering content
that this article presents
is general
across the off-grid electrical system
category as a whole.
A residential cabin,
a remote research station,
a disaster relief installation,
a maritime vessel,
or a forward operating base
inherits the same sizing equations,
the same dependent-component reasoning,
the same standards references,
and the same load-shedding logic
that the analog facility uses.
The space-colonization context
provides the framing
under which the analysis is presented
but does not constrain its applicability.
Subsequent articles
in this category
will treat
the per-subsystem engineering
of the dependent components
and the
non-battery alternatives
in greater depth.

## References

- [Reference, Caltech Space Solar Power Project][ref_caltech_sspp]
- [Reference, ESA Solaris Programme][ref_esa_solaris]
- [Reference, Fission Surface Power Programme][ref_fission_surface_power]
- [Reference, IEC 62548 Photovoltaic Array Standard][ref_iec_62548]
- [Reference, InSight Mars Lander End of Mission][ref_insight]
- [Reference, MAPLE Microwave Power Transfer Demonstrator][ref_maple]
- [Reference, NASA Kilopower KRUSTY Demonstrator][ref_kilopower]
- [Reference, National Electrical Code Article 210 Branch Circuits][ref_nec_210]
- [Reference, National Electrical Code Article 310 Conductors for General Wiring][ref_nec_310]
- [Reference, National Electrical Code Article 690][ref_nec_690]
- [Reference, Peak of Eternal Light at the Lunar Poles][ref_artemis_base_camp]
- [Reference, Peter Glaser Space Based Solar Power Concept][ref_sbsp]
- [Reference, Robert Forward Statite Concept][ref_statite]
- [Reference, Soletta and Krafft Ehricke Orbital Mirror Concept][ref_soletta]
- [Reference, Underwriters Laboratories 1741 Distributed Energy Inverters][ref_ul_1741]
- [Reference, Znamya Orbital Mirror Experiments][ref_znamya]
- [Related Post, Simulating Space Colonization on Earth Using Off-Grid Facilities][related_post_analog_intro]

[ref_artemis_base_camp]: https://en.wikipedia.org/wiki/Peak_of_eternal_light
[ref_caltech_sspp]: https://www.spacesolar.caltech.edu/
[ref_esa_solaris]: https://www.esa.int/Enabling_Support/Space_Engineering_Technology/SOLARIS
[ref_fission_surface_power]: https://en.wikipedia.org/wiki/Fission_Surface_Power
[ref_iec_62548]: https://webstore.iec.ch/publication/68645
[ref_insight]: https://mars.nasa.gov/insight/
[ref_kilopower]: https://en.wikipedia.org/wiki/Kilopower
[ref_maple]: https://www.caltech.edu/about/news/space-solar-power-project-ends-first-in-space-mission-with-successes-and-lessons
[ref_nec_210]: https://www.nfpa.org/codes-and-standards/nfpa-70-standard-development/70
[ref_nec_310]: https://www.nfpa.org/codes-and-standards/nfpa-70-standard-development/70
[ref_nec_690]: https://www.nfpa.org/codes-and-standards/nfpa-70-standard-development/70
[ref_sbsp]: https://en.wikipedia.org/wiki/Space-based_solar_power
[ref_soletta]: https://en.wikipedia.org/wiki/Soletta
[ref_statite]: https://en.wikipedia.org/wiki/Statite
[ref_ul_1741]: https://www.shopulstandards.com/ProductDetail.aspx?productId=UL1741
[ref_znamya]: https://en.wikipedia.org/wiki/Znamya_(satellite)
[related_post_analog_intro]: {% post_url 2026-06-28-simulating_space_colonization_on_earth_using_off_grid_facilities %}

