---
layout: post
mathjax: true
comments: true
title:  "Water Systems and Life Support Recovery for Off-Grid Space Colonization Analogs"
date:   2026-06-30 09:00:00 +0000
categories: aerospace engineering space-studies analog-facilities
---

<!-- A154 -->
<script>console.log("A154");</script>

The
[introduction to off-grid space colonization analog facilities][related_post_analog_intro]
that opened this category
identifies water recovery
as the highest-leverage subsystem
in any space mission,
and the
[electricity and energy storage article][related_post_electricity]
that followed
treats the electrical layer
under a battery-as-keystone framing
that the present article mirrors
for the water layer.
The architectural keystone
for any off-grid water system
is the storage tank
that decouples
intermittent supply
from continuous demand.
The closed-system extension
that any long-duration space colony
or terrestrial closed analog
adds on top of the storage layer
is the recovery loop
that approaches
a closure ratio of one
as the makeup water rate
approaches zero.

The space-colonization analog
provides the contextual flavour
of the analysis,
but the engineering content
generalises
without modification
to any off-grid water system
that the same supply-demand mismatch governs.
A remote research station,
an off-grid residential cabin,
a disaster relief installation,
a remote mining or oilfield camp,
a maritime vessel at extended range,
and a forward operating base
each face
the same intermittent-supply and continuous-demand problem
that the analog faces.
The sizing equations,
the treatment train,
the standards references,
and the recovery-loop reasoning
apply across all such cases.
The space-only options
and the high-closure recovery requirement
are the parts
that are specific
to the closed-system case.

The framing
is constrained
to the dominant off-grid water architecture,
which is
intermittent freshwater supply
through rainwater capture, well extraction,
or recovery flows,
buffered by a storage tank,
treated to potable standard
through filtration and disinfection,
and distributed to point of use
through a pumped or gravity-fed network.
The closed-system extension
adds
a greywater and blackwater recovery loop
that returns treated water
to the storage tank
across treatment stages
that match the contamination level
of each recovered stream.

## The Storage and Recovery Keystone

The off-grid water system
faces a generation-load mismatch
that mirrors the electrical case.
Demand is approximately continuous
across drinking, hygiene, cooking,
sanitation, and process water uses.
Supply is intermittent
because rainfall is episodic,
well replenishment rates are finite,
atmospheric water generation
operates on the diurnal humidity cycle,
and recovery flows
match the consumption cycle
but lag behind demand
by the treatment-train residence time.
The storage tank
absorbs the supply-demand mismatch
in the same way
the battery bank absorbs
the electrical generation-load mismatch.

The closed-system architecture
that any long-duration space colony
or rigorous terrestrial analog
must implement
adds a second consideration
that the open-system architecture
does not.
The closure ratio,
which is the fraction of consumed water
the system recovers
and returns to the storage tank,
determines
whether the long-duration mission
remains sustainable
on the imported makeup water supply
that the resupply schedule provides.
A closure ratio of zero
demands
full external makeup at the consumption rate.
A closure ratio of one
demands
zero external makeup,
which is the theoretical limit
that no real system reaches
because evaporative losses,
biological consumption,
and irreducible waste
each draw water out
of the recoverable loop.

The
[International Space Station Water Recovery System][ref_iss_wrs]
operates at approximately
ninety-eight percent closure
following the addition
of the Brine Processor Assembly
that the 2023 milestone documented.
The system recovers
urine,
condensate,
and humidity
through the Urine Processor Assembly
and the Water Processor Assembly
into potable water
that the crew drinks
without external resupply
across crew rotations.
The terrestrial analog
can match
this closure ratio
or report
the achieved closure ratio
against the standard.

## Storage Sizing From First Principles

The required storage volume
follows from the daily demand
and the worst-case supply gap.
Let $D_{daily}$ denote
the daily water demand
across all uses
in litres per day,
let $t_{gap}$ denote
the duration of the worst expected supply gap
in days,
and let $\sigma$ denote
the dimensionless safety factor
that absorbs forecast uncertainty,
typically in the range
of one point five to two.
The required storage volume is

$$ V_{storage} = D_{daily} \cdot t_{gap} \cdot \sigma $$

A small worked example
makes the magnitudes concrete.
A modest analog habitat
of four crew
at one hundred litres per crew per day
across a fourteen-day worst-case dry period
at a safety factor of one point five
requires

$$ V_{storage} = 4 \cdot 100 \text{ L/day} \cdot 14 \text{ days} \cdot 1.5 = 8{,}400 \text{ L} $$

which is a single eight-thousand-litre polyethylene tank
of standard residential or commercial size.
The same crew
under a strict
spaceflight-level consumption regime
of approximately three to five litres per crew per day
for drinking and food preparation
across the same fourteen-day gap
at the same safety factor
requires only
approximately two hundred and fifty to four hundred and twenty litres
of storage
across the consumption range,
which is the magnitude
the International Space Station operates against
because the resupply mass cost
forces the crew water use
down by an order of magnitude
relative to terrestrial residential expectations.

The daily demand
itself
is composed of several streams
that admit independent budgeting.
A terrestrial residential off-grid system
typically distributes the daily demand
across approximately
thirty percent toilet flushing,
twenty percent shower and bath,
fifteen percent laundry,
fifteen percent faucet,
ten percent leakage and process,
and ten percent other.
A spaceflight regime
eliminates the toilet flushing demand
through vacuum-toilet operation
that uses no water,
substantially reduces shower and bath demand
through wipe-bath protocols,
and eliminates laundry water demand
through disposable garment cycling
or low-water-laundry technology.
The remaining
drinking, food preparation,
and hygiene demand
is what the
three-to-five-litre-per-crew-per-day
spaceflight figure represents.

The closure ratio
$C$
defined as

$$ C = \frac{V_{recovered}}{V_{consumed}} $$

determines the effective makeup demand
across the mission.
The makeup water demand
across the mission duration $T_{mission}$
is

$$ V_{makeup} = D_{daily} \cdot T_{mission} \cdot (1 - C) $$

which the resupply schedule
or the imported reserve
must satisfy.
A six-month mission
of four crew
at one hundred litres per crew per day
on a closed loop
at $C = 0.95$
requires approximately
three thousand six hundred litres
of makeup water
across the mission,
which the resupply or reserve provides.
The same mission
on an open loop
at $C = 0$
requires approximately
seventy-two thousand litres
of makeup water,
which is a twenty-fold mass cost
that the closed-loop architecture
saves.

## Dependent Components in Order of Dependency

The storage tank
dimensioned in the previous section
sets the rating of every component
in the water system,
just as the battery bank
sets the rating of every component
in the electrical system.

### Water Sources

The off-grid water system
draws water
from one or more
of four principal source categories.

The first
is rainwater harvesting,
which captures
precipitation
through a roof or other catchment surface
into a storage tank
through a first-flush diverter
that rejects the initial dirty fraction.
The rainwater yield
is approximately
one litre
per square metre of catchment surface
per millimetre of rainfall
at the gross conversion,
reduced to approximately
zero point eight to zero point nine litres
per square metre per millimetre
after the runoff coefficient
that accounts for evaporation,
first-flush diversion,
and surface losses.
The
American conversion of
zero point six two gallons per square foot per inch
expresses the gross factor
in customary units.
A two-hundred-square-metre roof
in a region receiving
five hundred millimetres of annual rainfall
yields approximately
eighty to ninety thousand litres per year
after runoff losses,
which divided by three hundred and sixty-five days
is approximately
two hundred to two hundred and fifty litres per day
of average supply
that the storage tank
absorbs the seasonal variation against.

The second
is groundwater extraction
through a drilled or driven well.
A well draws water
from a saturated aquifer
through a pump
that lifts the water
against the static head
and the dynamic head losses.
The pumping power is

$$ P_{pump} = \frac{\rho \cdot g \cdot Q \cdot h}{\eta_{pump}} $$

where $\rho$ is water density,
$g$ is gravitational acceleration,
$Q$ is volumetric flow rate,
$h$ is total head,
and $\eta_{pump}$ is the pump efficiency
typically in the
forty to seventy percent range
for submersible well pumps.
A residential well
producing one cubic metre per hour
at thirty metres of lift
through a fifty-percent-efficient pump
consumes approximately
one hundred and sixty watts
of continuous electrical power
during pumping.

The third
is atmospheric water generation
through condensation
on a refrigeration coil
or sorption on a hygroscopic medium
that releases water
on regeneration.
The specific energy consumption
of atmospheric water generation
is approximately
zero point two to zero point five kilowatt-hours per litre
under moderate humidity
in the forty to sixty percent range,
degrading sharply
under arid conditions
below thirty percent relative humidity.
A Mars colony
extracting water from the Martian atmosphere
faces a humidity regime
of approximately zero point zero three percent water vapour by volume,
which makes
direct condensation impractical
and forces the use
of sorbent regeneration cycles
that the terrestrial analog
does not need to consider.

The fourth
is recovery from the closed loop,
which the next section
treats in its own right
because the recovery loop
is the architectural extension
that the closed-system case requires.

### Treatment Train

The treatment train
processes incoming water
to potable standard
through a sequence
of physical, chemical, and biological treatment stages
that match
the contamination level
of the source stream.

The first stage
is typically sedimentation
in a settling tank
that removes
suspended solids
through gravitational settling.
The second
is filtration
through a multi-media filter,
a cartridge filter,
or an ultrafiltration membrane.
A cartridge filter
at five micrometre absolute rating
removes
visible particulates
and reduces the load
on the downstream stages.
An ultrafiltration membrane
at zero point zero one to zero point one micrometre pore size
removes
bacteria, protozoa,
and most viruses
at energy consumption
of approximately
zero point one to zero point five kilowatt-hours per cubic metre.

The third stage
is disinfection,
typically through
ultraviolet irradiation
or chlorination.
The ultraviolet dose
required for four-log inactivation
of typical waterborne bacteria and protozoa
is approximately
thirty to forty millijoules per square centimetre,
which the
[National Sanitation Foundation Standard 55][ref_nsf_55]
specifies
for residential ultraviolet treatment units.
Certain viruses
require higher doses
as the treatment-technologies section details.
The disinfection contact time and concentration
for chlorination
follow the Chick-Watson model

$$ \log\left(\frac{N_t}{N_0}\right) = -k \cdot C \cdot t $$

where $N_t$ is the surviving pathogen population
at contact time $t$,
$N_0$ is the initial pathogen population,
$C$ is the disinfectant concentration,
and $k$ is the
pathogen-specific and condition-specific rate constant
that tabulated values
provide.

The fourth stage
is final polishing,
typically through
activated carbon
that removes residual organics
and improves taste and odour,
or through
ion exchange
that removes hardness ions
or specific contaminants of concern.

The
[National Sanitation Foundation Standard 61][ref_nsf_61]
governs the materials
that contact drinking water
in any United States system.
The
[National Sanitation Foundation Standard 53][ref_nsf_53]
governs the health-effect performance
of point-of-use and point-of-entry filters.
The
[Environmental Protection Agency Safe Drinking Water Act][ref_epa_sdwa]
under
40 CFR Part 141
publishes maximum contaminant levels
for inorganic and organic constituents
that the treated water
must satisfy
in the United States.
The
[World Health Organization Guidelines for Drinking-Water Quality][ref_who_dwg]
fourth edition
incorporating the first, second, and third addenda
through June 2026
publishes the international equivalent
that the analog at a non-US site
operates against.

### Storage Materials and Geometry

The storage tank
must contain
the dimensioned volume
in a material
that the
[National Sanitation Foundation Standard 61][ref_nsf_61]
permits
for drinking water contact.
Polyethylene tanks
in the range of
one hundred litres to fifty thousand litres
are the standard residential and small commercial choice.
Fiberglass-reinforced plastic tanks
are the standard
for larger volumes
up to several hundred thousand litres.
Stainless steel tanks
are the choice
where mechanical strength,
pressurisation,
or sanitary cleaning
require it.
Concrete cisterns
are the historical choice
for large volumes
where cost dominates
and the lining material
isolates the water
from the concrete.

The tank geometry
sets the secondary characteristics.
A vertical cylindrical tank
maximises volume
for a given footprint.
A horizontal cylindrical tank
fits low-ceiling installations
at the cost of
slightly higher capital expense
per litre.
A spherical tank
minimises material mass
for pressurised service,
which the spaceflight case
requires for transport mass budget.

### Distribution Network

The distribution network
delivers water
from the storage tank
to point of use
through a pumped or gravity-fed system.
A gravity-fed system
places the storage tank
at sufficient elevation
above the consumption points
to produce
the required line pressure
through the hydrostatic relationship

$$ P_{static} = \rho \cdot g \cdot h $$

which yields
approximately
ten kilopascals per metre of elevation difference,
or approximately
one and a half pounds per square inch per metre
in customary units.
A typical residential service pressure
of forty pounds per square inch
requires approximately
twenty-seven metres of elevation difference,
which the analog site
rarely provides naturally.

A pumped system
substitutes a pressure pump
with a pressure tank
or a variable-speed drive
that maintains the line pressure
without continuous pump operation.
The pump operates intermittently
to recharge the pressure tank
or modulates speed
under variable-frequency drive control
to match the instantaneous demand.
The pump power
follows the same formula
as the well pump
with the head equal to
the line pressure
expressed as head
plus the friction losses
through the distribution piping.

The friction head loss
through a section of pipe
follows the Darcy-Weisbach equation

$$ h_f = f \cdot \frac{L}{D} \cdot \frac{v^2}{2 g} $$

where $h_f$ is the friction head loss in metres,
$f$ is the Darcy friction factor,
$L$ is the pipe length,
$D$ is the inside diameter,
$v$ is the average flow velocity,
and $g$ is gravitational acceleration.
The friction factor
follows the Moody chart
or the Colebrook-White correlation
based on Reynolds number
and pipe roughness.
A typical residential cold-water line
in copper tube
at one and a half metres per second flow velocity
through a fifteen-millimetre-diameter pipe
incurs approximately
one and a half metres of head loss
per ten metres of pipe length,
which the pump head budget
must absorb.

The
[International Plumbing Code][ref_ipc]
governs the distribution piping
material and sizing
in the adopting jurisdictions.

### Heating and Pressure Management

The water heating subsystem
provides domestic hot water
through a tankless,
storage-tank,
or heat-pump water heater
at energy consumption
that matches the heating load.
The heating energy
to raise water mass $m$
through temperature rise $\Delta T$
is

$$ E_{heat} = m \cdot c_p \cdot \Delta T $$

where $c_p$
is the specific heat capacity of water
at approximately
four point one eight kilojoules per kilogram per kelvin,
which is equivalent to
one point one six watt-hours per kilogram per kelvin.
Heating one hundred litres of water
from ten degrees Celsius to fifty degrees Celsius
through a forty-degree rise
requires approximately
four point six kilowatt-hours
of delivered heat,
which a thirteen-amp resistance heater
at two hundred and forty volts
delivers in approximately
one and a half hours
of continuous operation.
A tankless heater
sized for a single shower head
draws approximately
twenty kilowatts of electrical power
during operation,
which is well above
the continuous load capacity
of the analog electrical system
sized in the prior article
unless the heater is propane- or wood-fired
or operates on a thermal storage buffer
that the photovoltaic generation charges.
A heat-pump water heater
delivers thermal energy
at a coefficient of performance
of approximately three to four,
reducing the electrical consumption
to roughly one quarter
of the resistance heating budget
at the cost
of higher capital expense
and reduced cold-weather performance.

The pressure management subsystem
handles the thermal expansion
of the stored water
and the surge pressures
that pump cycling produces.
An expansion tank
absorbs the thermal expansion
of heated water.
A surge tank
or pulsation dampener
absorbs the pump-cycling transients.

## The Recovery Loop and Closure Ratio

The closed-system architecture
that any long-duration space colony
or rigorous terrestrial analog
must implement
adds a recovery loop
to the open-system foundation
that the previous sections describe.
The recovery loop
collects
greywater, blackwater, and atmospheric humidity
across separate streams,
treats each stream
to the standard
that its recovered use will demand,
and returns the treated water
to the storage tank
or to a parallel reuse tank
that the system distributes from.

The greywater stream
includes
shower, bath, laundry,
and lavatory sink water
that contains
soap, body oils,
hair, and dilute organic matter
but not faecal contamination.
Greywater treatment
through coarse filtration
and chlorine or ultraviolet disinfection
produces water
suitable for toilet flushing,
irrigation,
or limited non-potable industrial use.
Treatment to potable standard
requires
additional stages
of membrane filtration
and advanced oxidation.

The blackwater stream
includes
toilet water
universally
and includes
kitchen sink water
under the jurisdictions
that classify
kitchen waste streams
as dark greywater or blackwater
because of grease, fats, and food particles.
California, Hawaii, and several other jurisdictions
classify kitchen sink output
as blackwater,
while the International Plumbing Code
and the Uniform Plumbing Code
exclude kitchen sink output
from greywater
without explicitly classifying it
as blackwater.
The blackwater stream
contains
faecal contamination
and concentrated organic matter.
Blackwater treatment
through anaerobic digestion,
aerobic biological treatment,
membrane bioreactor,
and disinfection
produces effluent
that the analog
either discharges
to a leach field,
returns to the storage tank
through additional polishing,
or holds for off-site disposal
on the resupply schedule.

The atmospheric humidity stream
includes
respiration water vapour,
sweat,
and cooking and washing humidity
that the habitat heating, ventilation, and air conditioning system
condenses on a cooling coil
and routes
to the recovery loop
as relatively clean condensate
that requires
only minimal treatment
to return to potable standard.
The
[International Space Station Water Processor Assembly][ref_iss_wrs]
processes
condensate
alongside the urine distillate
through a multi-stage treatment
that includes
multifiltration beds,
catalytic oxidation,
ion exchange,
and gas separation.

The urine stream
in a high-closure system
is the highest-organic-loading recovery stream
and requires
the most aggressive treatment.
The
[International Space Station Urine Processor Assembly][ref_iss_wrs]
uses vapor compression distillation
to separate water from urine solids,
recovering
approximately seventy to eighty-five percent of urine water
in current operation.
The Brine Processor Assembly
that NASA installed
in the early 2020s
recovers additional water
from the urine brine residue
that the Urine Processor Assembly leaves behind,
pushing total system recovery
to approximately
ninety-eight percent.

The closure ratio
$C$
that the article defined in the sizing section
is the system-wide aggregate
that the analog reports.
Subsystem-specific closure ratios
are usually more informative
than a single facility-wide value.
The honest analog
reports the closure ratio
for each recovery stream
alongside the aggregate
so the reader
can deduce
which recovery pathways
the system implements
and which it bypasses.

## Treatment Technologies in Detail

The treatment train introduced earlier
admits several technology choices
that the system designer
selects against
the source stream characteristics
and the energy budget.

Reverse osmosis
forces water
across a semipermeable membrane
under pressure
that exceeds the osmotic pressure
of the contaminant solution.
The specific energy consumption
of reverse osmosis
is approximately
three to four kilowatt-hours per cubic metre
for seawater desalination
at thirty to fifty percent recovery,
and approximately
zero point five to one point five kilowatt-hours per cubic metre
for brackish water
at seventy-five to eighty-five percent recovery.
The flux $J$
across the membrane
follows

$$ J = k_w \cdot (\Delta P - \Delta \pi) $$

where $k_w$ is the membrane water permeability,
$\Delta P$ is the applied transmembrane pressure,
and $\Delta \pi$ is the osmotic pressure difference
across the membrane.

Distillation
separates water from contaminants
by evaporation and recondensation
across a thermal gradient.
The latent heat of vaporisation
sets a thermodynamic minimum
of approximately
zero point six three kilowatt-hours per litre,
which a practical poorly insulated single-stage still
inflates to approximately
one to two kilowatt-hours per litre.
Multi-stage flash and multi-effect distillation
recover the latent heat
across cascaded stages
that reduce the net energy consumption
to approximately
eighteen to twenty-eight kilowatt-hours per cubic metre
for multi-stage flash
and approximately
four to seven kilowatt-hours thermal plus one and a half to two kilowatt-hours electrical per cubic metre
for multi-effect distillation
at large-scale seawater desalination.
The performance of a multi-stage distillation system
is characterised
by the gain output ratio

$$ GOR = \frac{m_{distillate} \cdot L_v}{Q_{heat}} $$

where $m_{distillate}$ is the mass flow rate of produced distillate,
$L_v$ is the latent heat of vaporisation,
and $Q_{heat}$ is the input heat rate.
A single-effect still
operates at $GOR \approx 1$
because each unit of input heat
vaporises approximately one unit of water mass.
A modern multi-effect distillation plant
operates at $GOR$ in the range of
eight to fifteen
by reusing the latent heat
across cascaded stages,
which is the operational basis
for the order-of-magnitude energy savings
the multi-effect architecture provides.
Vapor compression distillation
that the
International Space Station Urine Processor Assembly uses
recovers the latent heat
through mechanical compression of the vapour
at electrical consumption
of approximately
twenty kilowatt-hours per cubic metre.

Ultraviolet disinfection
inactivates pathogens
through ultraviolet-C irradiation
in the two-hundred-and-fifty to two-hundred-and-eighty nanometre wavelength range
that damages microbial nucleic acid.
The required dose
follows from the
log-reduction target
and the pathogen-specific dose-response curve.
A four-log inactivation
of typical waterborne bacteria and protozoa
requires approximately
thirty to forty millijoules per square centimetre,
while certain viruses
such as adenovirus
require higher doses
above one hundred millijoules per square centimetre
for the same log reduction.
The lamp electrical power
required to deliver the dose
at a given flow rate
depends on the lamp efficiency
and the reactor geometry,
typically resolving to approximately
five to fifteen watts of ultraviolet-C lamp power
per cubic metre per hour of treated water.

Chemical disinfection
through chlorine, chloramine, ozone,
or chlorine dioxide
provides a different tradeoff.
Chlorine
provides residual disinfection
through the distribution network
that ultraviolet does not provide
but produces disinfection by-products
that the maximum contaminant level
regulates.
Ozone
provides stronger oxidation
without halogenated by-products
but does not provide
distribution-system residual.
The disinfectant selection
depends on
the distribution-system characteristics
and the contaminant profile.

Activated carbon
adsorbs residual organics
and dissolved gases
through the high surface area
of activated carbon granules or blocks.
The bed volume sizing
follows
the empty bed contact time
that the target removal requires,
typically in the range
of ten to thirty minutes
for residential applications.

Ion exchange
substitutes
desirable ions
for problematic ions
in the water
through a resin bed
that the system regenerates
on a cycle.
The most common residential application
is water softening,
which substitutes
sodium for calcium and magnesium hardness ions.

## No-Recovery Architectures

The dominant closed-system architecture
implements a recovery loop
that approaches a closure ratio of one.
A subset of architectures
operates without a recovery loop
and accepts
the open-system mass cost
that the imported makeup supply
or the local source extraction
imposes.

A single-pass system
draws fresh water
from the source,
treats it to potable standard,
distributes it through the building,
and discharges the used water
to a leach field, sewer, or surface water body.
A residential off-grid cabin
with a deep well producing
several thousand litres per day
operates this way
without recovery
because the source extraction
costs less
than the recovery treatment.
A short-duration analog mission
operates this way
because the open-system mass cost
across a two-week mission
is acceptable
and the recovery infrastructure
capital cost
is not.

A continuous resupply system
imports fresh water
on a scheduled cadence
that the resupply vehicle delivers.
A military forward operating base
or a remote construction site
operates this way
because the recovery infrastructure
is not yet built
and the operational cadence
is short enough
that the resupply mass cost
is acceptable.
A short-duration space mission
in low Earth orbit
operates this way
when the closed-system Water Recovery System
is not yet installed
or is undergoing maintenance.

A hybrid architecture
implements partial recovery
of the easiest streams
and accepts open operation
on the difficult streams.
A residential off-grid system
that recovers laundry and shower greywater
for toilet flushing and irrigation
but discharges toilet blackwater
to a septic system
implements partial recovery
at modest capital cost.
The closure ratio
this hybrid achieves
typically falls
in the thirty to sixty percent range.

## Terrestrial-Only Cheats

The terrestrial analog
operates inside
a planet that provides
a freshwater supply chain,
an electricity grid powering atmospheric water generators,
adjacent rivers or aquifers,
and a network of resupply paths
that no space colony will have access to.
The analog
can lean on these
to varying degrees
and report the dependence honestly,
or it can hide the dependence
and report the result
as if it were closed.

The first cheat
is municipal water connection
that draws
treated potable water
from the local utility
through a service line.
A municipal-connected analog
imposes effectively
no constraint on its water budget
and reports
on the local utility distribution
rather than on its closed-system performance.

The second cheat
is trucked-in water delivery
on a cadence shorter
than any plausible space mission resupply schedule.
A weekly water delivery
of several thousand litres
to the analog site
is a confession
that the analog
is dependent
on the terrestrial freshwater supply chain
at the weekly cadence
rather than producing or recovering
its own water inside the envelope.

The third cheat
is hose-coupled supply
from an adjacent research station,
hotel,
or military base
that the analog shares infrastructure with.
The cogeneration arrangement
reduces the analog operating cost
but means
the analog
operates on the combined water budget
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
of water sources
that the actual space mission can exercise
but that the terrestrial analog cannot.

### Lunar Polar Water Ice

The lunar polar regions
contain water ice
in permanently shadowed regions
near the south and north poles
that the
[Lunar Crater Observation and Sensing Satellite][ref_lcross]
or LCROSS impactor mission
confirmed in October 2009
through the spectral signature
of the ejecta plume
the impactor produced.
The
[Lunar Reconnaissance Orbiter][ref_lro]
has mapped
the distribution
through subsequent observations.
Estimates of total lunar polar water ice
range from approximately
six hundred million tonnes
to several billion tonnes
in concentrations
that range from
trace to several weight percent
depending on the specific deposit.
A lunar polar colony
extracting water ice from regolith
faces a heating energy cost
for ice sublimation
and capture
that the recovery-loop architecture
does not impose
but receives in exchange
an effectively unlimited source
that no terrestrial analog provides.

### Mars Subsurface Water Ice

The Mars subsurface
contains water ice
distributed across
polar caps,
high-latitude terrain,
and mid-latitude deposits
that the
[Mars Reconnaissance Orbiter Shallow Radar][ref_mro_sharad]
or SHARAD instrument
has mapped
through the present.
The
[Phoenix lander mission][ref_phoenix]
in 2008
directly observed
subsurface water ice
at high northern latitudes.
A Mars colony
extracting water ice
faces a similar regolith heating
and capture cost
to the lunar case
but at the elevated complexity
of operating
under partial gravity,
under thin atmosphere,
and under significantly lower temperatures
than the lunar permanently shadowed regions
that have stable thermal environments.

### Mars Atmospheric Water

The Mars atmosphere
contains
approximately zero point zero three percent water vapour by volume,
which is substantially less
than terrestrial atmospheric humidity
even in arid regions.
A
[Water Vapor Adsorption Reactor][ref_wavar]
or WAVAR concept
that Adam Bruckner and colleagues described
in the late 1990s
proposes
extracting Mars atmospheric water
through sorbent regeneration cycles
that capture water vapour
on a zeolite or other hygroscopic medium
and release it
on heating.
The terrestrial analog
cannot exercise this option
at the same humidity regime
because the terrestrial atmosphere
has approximately
two orders of magnitude more water vapour
than the Martian atmosphere
at the same temperature.

### Asteroid and Comet Volatiles

Carbonaceous asteroids
and short-period comets
contain
water ice and hydrated minerals
that an in-space colony
could extract
through a dedicated mining mission.
A near-Earth asteroid mining operation
that delivers water
to a cislunar facility
removes
the gravity-well launch cost
that lunar polar ice extraction faces
but at the substantial mission cost
of the rendezvous and extraction operation.
The terrestrial analog
cannot exercise this option
because the source
is not on Earth.

## Where the Keystone Framing Breaks Down

The storage-tank-plus-recovery-loop framing
holds across
the dominant terrestrial and space analog cases.
Three cases
break the framing.

The first is the
sub-day mission duration.
A mission
of hours to a day
demands
neither significant storage
nor recovery infrastructure
because the crew can carry
sufficient water
in personal containers
across the entire mission.
The mass cost
of the carried water
is acceptable
because the mission is short.

The second is the
trace-water environment
that demands
extreme conservation
beyond what
the recovery loop can deliver.
A long-duration mission
to the outer solar system
operates against
a mass budget
that forbids
even the recovery loop
from sustaining
significant water demand
because every kilogram
imported from Earth
costs orders of magnitude more
than the cislunar case.
Such missions
default to
minimal hydration
and substitute
hygiene practices
that use no water at all.

The third is the
in-situ-resource-abundance regime
in which
the local water source
is so abundant
that the recovery infrastructure
costs more
than continuous fresh extraction.
A Mars polar colony
sited at a polar ice cap
or a lunar polar colony
sited at a high-grade ice deposit
might find
the open-loop extraction architecture
economically competitive
with the recovery architecture
at certain ice grade and extraction-rate combinations.
The architecture choice
in this regime
becomes
a trade study
rather than a default.

## Generalisation Beyond the Space Analog Context

The architecture and sizing reasoning
that this article presents
applies without modification
to any off-grid water system
that the same supply-demand mismatch governs.
A few representative cases
make the generalisation concrete.

A residential off-grid cabin
in a remote terrestrial location
implements
the storage tank
buffered against the rainwater catchment
or the well as primary source,
with a treatment train
through cartridge filtration and ultraviolet disinfection
that satisfies
the
[Safe Drinking Water Act standards][ref_epa_sdwa].
The greywater system
that captures
shower and laundry water
for irrigation or toilet flushing
implements
partial closure
at modest capital cost.
The blackwater system
that routes toilet output
to a septic system or composting toilet
manages the difficult stream
without returning it to the storage tank.

A remote research station
in the Antarctic, the Arctic,
or another remote terrestrial environment
implements
a melted-ice water source
or a well-fed system
with a treatment train
matched to the source water quality.
The closure ratio
that the research station operates against
typically falls
in the thirty to fifty percent range
because the research station
discharges blackwater
to a managed disposal system
rather than recovering it.

A disaster relief installation
that operates
after a grid and water utility outage
faces an off-grid water problem
on a shorter time scale
than the multi-year analog.
The trucked-in water delivery
combined with the local treatment train
typically dominates
the architecture
because the duration is short
and the closed-loop infrastructure
deployment time
is constrained.

A maritime vessel at extended range
operates a closed water system
with a reverse osmosis seawater desalination unit
as the makeup source
and a recovery loop
that returns
shower and laundry water
through limited treatment
to the non-potable distribution.
The closure ratio
the maritime case achieves
typically falls
in the sixty to eighty percent range.

A military forward operating base
operates a hybrid water system
with trucked-in or airlifted bulk water
as the primary source,
local treatment
through reverse osmosis water purification units,
and limited recovery
for non-potable uses.
The closure ratio
the forward operating base achieves
typically falls
in the ten to thirty percent range
because the operational tempo
does not justify
the closed-loop infrastructure
capital cost.

The recommended reading sequence
for an engineer
who is designing
a new off-grid water installation
in any of these contexts
is to read this article
for the architecture,
then to consult
the relevant standards
through the
[Safe Drinking Water Act][ref_epa_sdwa]
and the
[World Health Organization Guidelines for Drinking-Water Quality][ref_who_dwg]
for the specific
maximum contaminant levels
and treatment requirements
the chosen jurisdiction imposes.

## Out of Scope

This article
treats the water layer
of the analog facility
in survey form
and necessarily defers
several topics
to subsequent treatments.

**Detailed treatment-train engineering.**
The pilot-scale and full-scale design
of the membrane modules,
the disinfection reactors,
the activated carbon beds,
and the ion exchange columns
sits inside
a process-engineering treatment
that this article
does not attempt
beyond the conceptual coverage
in the treatment-technologies section.

**Bioregenerative life support biology.**
The biology
of a fully closed bioregenerative life support system
that supports a crew
across multiple years
through coupled water,
nutrient,
oxygen, and carbon dioxide cycles
is an active research subject
that
the BIOS-3, Biosphere 2, MELiSSA,
and Yuegong programmes
have advanced
without reaching closure.
The biology
deserves a dedicated treatment
that this article
does not attempt.

**Pharmaceutical and personal care product treatment.**
The recovery of water
from streams containing
pharmaceutical residues
and personal care product residues
that the spaceflight crew metabolises
and excretes
is an active area
of advanced oxidation research
that this article
does not treat.

**Trace organic contaminant analysis.**
The analytical chemistry
that detects
parts-per-trillion concentrations
of trace organic contaminants
that the maximum contaminant level
regulates
or that the human dose-response curve
flags as concerning
is a self-contained analytical chemistry subject
that this article
does not treat.

**Microbial control in the distribution network.**
The legionella, mycobacteria,
and biofilm control
that the
[American Society of Heating, Refrigerating, and Air-Conditioning Engineers Standard 188][ref_ashrae_188]
addresses
in building water systems
is a self-contained microbial-ecology subject
that this article
does not treat
beyond noting the governing standard.

**In-situ resource utilisation engineering.**
The engineering
of regolith water extraction,
atmospheric water extraction,
and asteroid mining operations
that the space-only options section mentions
sits inside
a dedicated in-situ-resource-utilisation engineering subject
that this article
does not treat.

## Conclusion

The off-grid water subsystem
of a space-colonization analog
is best dimensioned
around the storage tank
as the architectural keystone
and the recovery loop
as the closed-system extension
that determines long-duration sustainability.
The storage sizing
follows from
the daily demand,
the worst-case supply gap,
and the chosen safety factor.
The closure ratio
follows from
the recovery infrastructure
implemented
across each contamination-level stream.
Every dependent component
takes its rating
from the storage sizing
and the closure ratio target.

A small number of alternative architectures
operate without a recovery loop
and accept the open-system mass cost
that the imported makeup supply
or the local source extraction
imposes.
Each alternative
applies in a regime
where the recovery infrastructure
capital cost
exceeds
the recovered water value
across the mission duration.

The terrestrial analog
can cheat
by leaning on
the municipal water utility,
the trucked-in delivery,
or an adjacent facility,
and the honest analog
documents the dependence
rather than reporting
on a closed system
it does not operate.
The actual space mission
has options
that the terrestrial analog cannot exercise,
including the lunar polar water ice,
the Mars subsurface water ice,
the Mars atmospheric water vapour,
and the asteroid and comet volatiles,
which the analog tradition
should mention
even though
it cannot reproduce them.

The engineering content
that this article presents
is general
across the off-grid water system
category as a whole.
A residential cabin,
a remote research station,
a disaster relief installation,
a maritime vessel,
or a forward operating base
inherits the same sizing equations,
the same dependent-component reasoning,
the same standards references,
and the same recovery-loop logic
that the analog facility uses.
The space-colonization context
provides the framing
under which the analysis is presented
but does not constrain its applicability.
Subsequent articles
in this category
will treat
the remaining subsystems
of the nine-subsystem stack
that the survey opener identified.

## References

- [Reference, ASHRAE Standard 188 Legionellosis Risk Management][ref_ashrae_188]
- [Reference, Environmental Protection Agency Safe Drinking Water Act][ref_epa_sdwa]
- [Reference, International Plumbing Code][ref_ipc]
- [Reference, International Space Station Water Recovery System][ref_iss_wrs]
- [Reference, Lunar Crater Observation and Sensing Satellite][ref_lcross]
- [Reference, Lunar Reconnaissance Orbiter][ref_lro]
- [Reference, Mars Phoenix Lander Subsurface Ice][ref_phoenix]
- [Reference, Mars Reconnaissance Orbiter SHARAD Radar][ref_mro_sharad]
- [Reference, NSF Standard 53 Drinking Water Treatment Health Effects][ref_nsf_53]
- [Reference, NSF Standard 55 Ultraviolet Microbiological Water Treatment][ref_nsf_55]
- [Reference, NSF Standard 61 Drinking Water System Components][ref_nsf_61]
- [Reference, Water Vapor Adsorption Reactor WAVAR Concept][ref_wavar]
- [Reference, World Health Organization Drinking-Water Guidelines][ref_who_dwg]
- [Related Post, Electricity and Energy Storage for Off-Grid Space Colonization Analogs][related_post_electricity]
- [Related Post, Simulating Space Colonization on Earth Using Off-Grid Facilities][related_post_analog_intro]

[ref_ashrae_188]: https://www.ashrae.org/technical-resources/bookstore/ansi-ashrae-standard-188-2021-legionellosis-risk-management-for-building-water-systems
[ref_epa_sdwa]: https://www.epa.gov/sdwa
[ref_ipc]: https://www.iccsafe.org/products-and-services/i-codes/2024-i-codes/ipc/
[ref_iss_wrs]: https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/
[ref_lcross]: https://en.wikipedia.org/wiki/LCROSS
[ref_lro]: https://en.wikipedia.org/wiki/Lunar_Reconnaissance_Orbiter
[ref_mro_sharad]: https://en.wikipedia.org/wiki/SHARAD
[ref_nsf_53]: https://www.nsf.org/standards-development/standards-portfolio/water-treatment-distribution-systems/nsf-ansi-53
[ref_nsf_55]: https://www.nsf.org/standards-development/standards-portfolio/water-treatment-distribution-systems/nsf-ansi-55
[ref_nsf_61]: https://www.nsf.org/standards-development/standards-portfolio/water-treatment-distribution-systems/nsf-ansi-61
[ref_phoenix]: https://en.wikipedia.org/wiki/Phoenix_(spacecraft)
[ref_wavar]: https://ntrs.nasa.gov/citations/19990033319
[ref_who_dwg]: https://www.who.int/publications/i/item/9789240045064
[related_post_analog_intro]: {% post_url 2026-06-28-simulating_space_colonization_on_earth_using_off_grid_facilities %}
[related_post_electricity]: {% post_url 2026-06-29-electricity_and_energy_storage_for_off_grid_space_colonization_analogs %}

