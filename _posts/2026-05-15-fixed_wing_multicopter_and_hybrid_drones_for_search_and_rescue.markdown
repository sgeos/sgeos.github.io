---
layout: post
mathjax: true
comments: true
title:  "Fixed-Wing, Multicopter, and Hybrid Drones for Search and Rescue, Physics and Economics"
date:   2026-05-15 09:00:00 +0000
categories: aerospace engineering uav search-and-rescue
---

<!-- A145 -->
<script>console.log("A145");</script>

A search and rescue operation
that runs unmanned aircraft
faces an early choice
that the platform vendor literature
does not always make clear.
Fixed-wing aircraft,
multicopters,
and hybrid vertical-takeoff-and-landing aircraft
are different vehicles
solving different parts
of the problem.
Either alone
is a partial answer.
A serious program
runs more than one,
often handed off in sequence
during a single incident.
This article
treats the three platform classes
on three axes,
namely the underlying physics
that distinguishes them,
the capital and upkeep economics
that decide
which a program can afford,
and the personnel training
that decides
which a program can operate safely.
The search and rescue use case
provides the worked example
because it exercises
every operationally interesting property
the three classes have.
The conclusions
generalise to
delivery, inspection,
surveying, and reconnaissance
without structural change.

## The Three Platform Classes

A **fixed-wing** unmanned aerial vehicle
generates lift
by moving forward
through the air.
The wing
is a fixed surface
shaped to produce lift
as a function
of relative wind speed
and angle of attack.
The vehicle
must keep moving
to stay aloft.
Its energy budget
is dominated by
drag at cruise speed.
Examples in the search-and-rescue
class
include the
[AeroVironment Puma 3 AE][ref_puma_3_ae],
the
[Insitu ScanEagle][ref_scaneagle],
the
[Elbit Skylark][ref_skylark],
and the
[UAV Factory Penguin C][ref_penguin_c].

A **multicopter**
generates lift
by accelerating air downward
through rotors.
The vehicle
can stand still in the air
above the ground.
Its energy budget
is dominated by
the cost of hovering
against gravity.
Examples in the search-and-rescue class
include the
[DJI Matrice 30T][ref_matrice_30t],
the
[DJI Matrice 350 RTK][ref_matrice_350],
the
[Skydio X10][ref_skydio_x10],
and the
[Autel EVO Max 4T][ref_autel_max_4t].

A **hybrid vertical-takeoff-and-landing**
aircraft
combines
the lift mechanism of a multicopter
with the cruise mechanism of a fixed-wing aircraft.
Three subclasses cover most of the design space.
A
[tail-sitter][ref_tail_sitter]
pivots the entire vehicle
through ninety degrees
between hover and cruise.
A
[quad-plane][ref_quad_plane]
or
[VTOL convertiplane][ref_convertiplane]
carries
separate rotors for vertical lift
and a separate propulsion system for cruise.
A
[tilt-rotor][ref_tilt_rotor]
or
[tilt-wing][ref_tilt_wing]
rotates the rotors,
or the wing carrying the rotors,
between hover and cruise orientation.
Examples in the search-and-rescue class
include the
[WingtraOne Gen II][ref_wingtra_one],
the
[Quantum Systems Trinity F90+][ref_trinity_f90],
and the
[Quantum Systems Vector][ref_quantum_vector].

The three classes
are not exhaustive.
Lighter-than-air vehicles,
helicopter-style coaxial rotorcraft,
single-main-rotor unmanned helicopters,
and ornithopters
all occupy adjacent niches.
The three named classes
dominate the small unmanned aerial vehicle market
for search and rescue
in 2026
and the analysis below
addresses them.

## The Physics of Fixed-Wing Flight

A fixed wing
produces lift
as a function
of air density, the square of airspeed,
the wing area,
and the lift coefficient.

$$L = \tfrac{1}{2} \rho V^{2} S C_{L}$$

where $L$ is lift,
$\rho$ is air density,
$V$ is airspeed,
$S$ is wing area,
and $C_{L}$ is the lift coefficient,
itself a function of angle of attack
and airfoil geometry.
The same wing
produces drag
under the same parameters
with a drag coefficient $C_{D}$.

$$D = \tfrac{1}{2} \rho V^{2} S C_{D}$$

The ratio
of lift to drag
is the principal figure of merit
for a fixed-wing aircraft.

$$\frac{L}{D} = \frac{C_{L}}{C_{D}}$$

A small unmanned aerial vehicle
in the search-and-rescue size class
operates
with $L/D$
typically in the range
of 8 to 20
depending on
configuration,
airfoil choice,
and operating Reynolds number.
The
[Reynolds number][ref_reynolds_number]
quantifies
the ratio of inertial to viscous forces
in the flow over the wing.

$$Re = \frac{\rho V c}{\mu}$$

where $c$ is a reference length,
typically the wing chord,
and $\mu$ is the dynamic viscosity of air.
Small unmanned aerial vehicles
operate at
Reynolds numbers
between $10^{4}$ and $10^{6}$,
which is below the regime
where conventional airfoil design
gives the best $L/D$.
The low-Reynolds-number penalty
on small aircraft
is real and
is one reason
fixed-wing performance
does not scale smoothly
from full-size aircraft data
to UAV-class platforms.
The
[low-Reynolds-number flight regime][ref_low_re]
is the subject of
its own engineering literature.

The
power required
to maintain cruise
is the product of drag and airspeed,
divided by the propulsive efficiency
of the propeller-and-motor system.

$$P_{cruise} = \frac{D V}{\eta_{p}}$$

where $\eta_{p}$ is the propulsive efficiency,
itself a function of propeller geometry,
motor efficiency,
and operating point.
A typical small unmanned aerial vehicle
in this class
operates with $\eta_{p}$
in the range
of 0.5 to 0.7.

The endurance
of an electric fixed-wing aircraft
is approximately
the energy stored in the battery
divided by the power required at cruise.
The
[electric Breguet endurance equation][ref_breguet]
gives this form.

$$E = \eta_{total} \frac{1}{g} \frac{C_{L}^{3/2}}{C_{D}} \sqrt{\frac{2}{\rho S}} \frac{1}{\sqrt{m}} E_{batt}$$

where $E$ is endurance,
$\eta_{total}$ is the cumulative efficiency
of battery, motor, and propeller,
$g$ is gravitational acceleration,
$m$ is total mass,
and $E_{batt}$ is the energy stored in the battery.
The dependence
on $C_{L}^{3/2} / C_{D}$
favours operation
at the airspeed and angle of attack
that maximises this ratio,
which is typically
slower
than the maximum-$L/D$ point.

The endurance
of a search-and-rescue-class
fixed-wing UAV
is typically
two to twenty hours
depending on the platform.
The
[propulsion and power sizing
article in this series][related_post_propulsion]
covers the energy budget
in more detail.
The
[electric energy systems
and endurance budget
article][related_post_electric_energy]
treats the battery side
specifically.

## The Physics of Multicopter Flight

A rotor producing thrust
imparts momentum
to a column of air
passing through the rotor disk.
The
[actuator disk theory][ref_actuator_disk]
of
Rankine and Froude,
also called
momentum theory,
gives the ideal hover power
required to produce a thrust $T$
at sea level
through a rotor of disk area $A$.

$$P_{ideal} = \frac{T^{3/2}}{\sqrt{2 \rho A}}$$

The actual hover power
exceeds the ideal
by a factor
that the
[figure of merit][ref_figure_of_merit]
$FM$
captures.

$$P_{hover} = \frac{P_{ideal}}{FM}$$

A well-designed rotor
in steady hover
achieves
$FM$ in the range of 0.7 to 0.8.
Small multicopter rotors
in the search-and-rescue size class
typically achieve $FM$
in the range
of 0.5 to 0.7
because
they are smaller,
operate at higher disk loading,
and use fixed-pitch rather than collective-pitch blades.

The thrust required to hover
equals the vehicle weight.

$$T = m g$$

Substituting,
the hover power per unit mass
scales as the square root
of disk loading,
namely thrust per unit disk area.

$$\frac{P_{hover}}{m} = \frac{g^{3/2}}{FM} \sqrt{\frac{m}{2 \rho A}} = \frac{g^{3/2}}{FM} \sqrt{\frac{DL}{2 \rho}}$$

where $DL = T/A$ is disk loading.
A lower disk loading
gives a lower hover power per unit mass.
A full-scale helicopter
operates at disk loading
in the range of 200 to 500 N per square metre.
A small multicopter
operates at disk loading
in the range of 50 to 200 N per square metre.
The multicopter's lower disk loading
partially compensates
for its lower figure of merit.

The endurance
of an electric multicopter
in hover
is approximately
the battery energy
divided by the hover power.

$$E_{hover} = \frac{\eta_{total} E_{batt}}{P_{hover}}$$

For typical search-and-rescue
multicopters,
endurance in pure hover
is twenty to ninety minutes.
The endurance figure
quoted in vendor literature
usually assumes
hover with no wind,
no payload mass increase
beyond the base configuration,
no aggressive manoeuvring,
and full battery capacity.
Real operations
under wind, payload, and manoeuvring
reduce the figure
by ten to forty percent.

In forward flight
the multicopter rotor
ingests air
not only from above
but also from the front,
which reduces the induced power
required.
A multicopter
flying at moderate forward speed
consumes less power
than the same multicopter in hover.
The forward-flight power minimum
typically occurs
at airspeeds
of 8 to 15 metres per second
for vehicles in this class.
Beyond the minimum,
parasitic drag begins to dominate
and power rises again.

The implication is structural.
A multicopter
that flies forward at moderate speed
extends its endurance
beyond the pure-hover figure
by twenty to fifty percent.
But the multicopter
cannot fly anywhere near
the cruise speed
of a fixed-wing aircraft
of comparable mass,
because the rotor lift mechanism
loses efficiency
at high forward airspeeds.

## The Physics of Hybrid Vertical-Takeoff-and-Landing Aircraft

The hybrid aircraft
combines
the multicopter lift mechanism
for hover, takeoff, and landing
with the fixed-wing lift mechanism
for cruise.
The combination
is achieved
through three architectures.

A **tail-sitter**
mounts a fixed wing
and a single propulsion system.
The vehicle takes off vertically
with the wing oriented vertically,
producing thrust from the propeller
that lifts the vehicle off the ground.
The vehicle then pitches forward
through ninety degrees
into horizontal flight,
at which point
the wing produces lift
and the propeller produces thrust
as in conventional fixed-wing flight.
The tail-sitter pays no weight penalty
for a second propulsion system,
but the transition between hover and cruise
exposes the wing
to airspeeds and angles of attack
outside the design envelope
of a conventional fixed wing.
The transition
must be controlled
through specialised flight-control software.

A **quad-plane**
or **convertiplane**
carries
separate rotors for vertical lift
and a separate propeller and motor
for forward cruise.
The vehicle takes off vertically
on the lift rotors,
transitions to forward flight
by accelerating the cruise propeller
while the lift rotors spin down,
and cruises on the fixed wing alone.
The quad-plane
pays a weight penalty
for carrying the lift rotors
through cruise
as dead weight,
and a drag penalty
for the lift rotor housings
in the cruise airflow.
The penalty
typically reduces cruise endurance
by twenty to forty percent
relative to a pure fixed-wing aircraft
of the same mass.

A **tilt-rotor**
or **tilt-wing**
rotates
the rotors,
or the wing carrying the rotors,
between vertical and horizontal orientation.
The same rotors
produce vertical thrust in hover
and forward thrust in cruise.
The tilt-rotor avoids
the dead-weight penalty
of the quad-plane
but introduces
mechanical complexity
in the tilting mechanism
and aerodynamic complexity
in the transition phase.
Most full-size examples,
including the
[Bell Boeing V-22 Osprey][ref_v_22],
are large aircraft
where the mechanical complexity
is acceptable.
Small unmanned tilt-rotors
exist
but are less common
than tail-sitters and quad-planes
in the small-UAV class.

The hybrid VTOL aircraft
solves the launch and recovery problem
that the
[launch and recovery systems
article in this series][related_post_launch_recovery]
treats
for pure fixed-wing aircraft.
A hybrid takes off and lands vertically,
which removes
the need for a runway,
a catapult,
a recovery net,
or a parachute.
The cost
is the cruise efficiency penalty
described above
and the additional mechanical or software complexity.

The hybrid endurance
is intermediate
between fixed-wing and multicopter.
Typical search-and-rescue-class
hybrids
achieve
forty-five to ninety minutes endurance
on batteries,
which is two to three times
the equivalent multicopter
but a fraction
of the equivalent fixed-wing.

## Performance Implications for Search and Rescue

The physics
yields a small number
of performance facts
that determine
how the three classes
serve a search and rescue mission.

**Area coverage rate.**
The product of cruise speed
and the swath width
of the sensor footprint
gives the rate
at which a platform
can sweep an area
on a single sortie.
A fixed-wing aircraft
at 20 metres per second cruise speed
and a 500-metre sensor swath
at altitude
sweeps 10 square kilometres per minute,
which over an eight-hour sortie
covers 4800 square kilometres.
A multicopter
at 8 metres per second cruise speed
and a 100-metre sensor swath
at low altitude
sweeps 0.48 square kilometres per minute,
which over a 60-minute sortie
covers 29 square kilometres.
The fixed-wing platform
covers more than a hundred times
the area
per sortie.

**Sensor dwell time.**
A fixed-wing aircraft
flying at altitude
over a candidate target
must orbit
to keep the sensor pointed
at the target.
Orbital geometry
limits sensor dwell time
per pass
to a few seconds
unless the orbit is small,
in which case
the bank angle
becomes a problem.
A multicopter
hovers
and points
indefinitely,
limited only by endurance.
A hybrid
hovers
to investigate
and then transitions
back to forward flight
to continue searching.

**Launch and recovery footprint.**
A fixed-wing aircraft
in this class
requires a runway,
a catapult,
or a bungee launcher,
plus a recovery method
that may be
a runway, a net, a Skyhook cable, or a parachute.
The launch-and-recovery footprint
is non-trivial and is treated in
[the launch and recovery
article in this series][related_post_launch_recovery]
and in
[the runway sizing
article][related_post_runway_sizing].
A multicopter
or hybrid
launches and lands vertically
from any flat clearing of a few metres on a side.

**Wind tolerance.**
A fixed-wing aircraft
of given wing loading
tolerates surface winds
up to a fraction of the cruise speed.
A typical small UAV
tolerates winds up to 30 to 60 percent
of cruise speed
for safe takeoff and landing.
A multicopter
tolerates winds
up to a fraction
of its maximum forward-flight speed,
typically 30 to 50 percent.
Both classes
operate marginally
in winds
above 25 knots
at the surface.

**Precision payload delivery.**
A multicopter
can descend
to a few metres
above the target,
hover,
and release a payload
with sub-metre accuracy.
A fixed-wing aircraft
delivers payloads
on a high-speed pass
or with parachute-assisted drops,
both of which
degrade accuracy
to tens of metres.
A hybrid
descends vertically
to deliver
and then ascends and transitions back.

The performance facts
yield a clear use-case
allocation
across the three classes
for the search and rescue mission.

| Performance property | Fixed-wing | Multicopter | Hybrid VTOL |
|---|---|---|---|
| Endurance per sortie | 2 to 20 hours | 20 to 90 minutes | 45 to 90 minutes |
| Cruise speed | 15 to 35 m/s | 4 to 15 m/s | 15 to 25 m/s |
| Hover capability | None | Indefinite | Limited by hover endurance |
| Area coverage per sortie | High | Low | Medium |
| Launch and recovery footprint | Large | None | None |
| Wind tolerance | Moderate to high | Low to moderate | Moderate |
| Precision payload delivery | Low | High | High |
| Sensor dwell on point | Orbital, seconds | Indefinite | Indefinite |

The table is a scorecard,
not a verdict.
A serious search-and-rescue program
uses
the high-coverage platform
for wide-area searches,
the high-dwell platform
for target investigation and intervention,
and either
for the routine patrol phase.

## The Search and Rescue Use Case Sequence

A search and rescue operation
unfolds
through a small number of phases
that exercise
the three platform classes
in characteristic order.

**Phase 1, wide-area search.**
A subject is reported missing
in a defined search area
of perhaps
twenty to two thousand square kilometres.
The operation
launches a fixed-wing aircraft
at altitude
with a thermal infrared sensor
and a daylight electro-optical sensor.
The aircraft flies
a methodical sweep pattern,
typically the
[expanding square][ref_search_pattern]
or
[parallel track][ref_parallel_track]
search,
across the area.
Sensor operators
on the ground
watch the downlinked imagery
for thermal anomalies
that match a human body
against the colder background
of vegetation, water, or snow.
The fixed-wing platform's endurance
permits one or two
operators
to cover the entire area
in a single sortie
or a small number of sorties.
A multicopter at this phase
would require
many launches
and many recoveries
to cover the same area,
which is operationally impractical.

**Phase 2, target investigation.**
The fixed-wing platform
detects a candidate
that requires
closer examination.
The operation
launches a multicopter
to the candidate coordinates.
The multicopter
descends
to a low altitude,
hovers
in the vicinity of the target,
and points its sensors
directly at the candidate.
The operator
identifies
whether the candidate is the missing subject,
whether the subject is responsive,
whether the subject is mobile,
and whether the surroundings
are hazardous
to ground rescuers.
The multicopter's hover capability
is essential
because the answers
require sustained, close visual contact.
The fixed-wing platform
cannot dwell over the target.
The hybrid
can dwell but at a higher cost
than a dedicated multicopter.

**Phase 3, intervention.**
Once the target is confirmed,
the operation
intervenes.
A multicopter
may drop
a flotation device
to a swimmer,
a radio
to a hiker who has lost contact,
an automatic external defibrillator
to a cardiac patient,
food and water
to a survivor
in a delayed-rescue situation,
or a flare
to mark the location for ground teams.
The
[Zipline][ref_zipline]
delivery system,
the
[Matternet][ref_matternet]
network,
and several manufacturer-specific drop mechanisms
provide the payload-release hardware.
A multicopter delivers
with sub-metre accuracy.
A fixed-wing platform
delivers
through parachute drops
with tens-of-metres accuracy,
which is sometimes acceptable
for non-critical payloads
and rarely acceptable
for medical interventions.

**Phase 4, sustained coverage.**
After initial contact
the operation
maintains
overwatch
of the target and the ground rescue team.
A fixed-wing platform
or a hybrid
at altitude
provides communications relay,
situational awareness,
and ground team tracking
through the duration
of the rescue.
A multicopter at this phase
exhausts its battery
in tens of minutes
and is replaced
by a fresh multicopter
or by the longer-endurance platform.

The phase allocation
is operationally typical
but not strict.
A small-area search
in confined terrain
may use multicopters only.
A water search
over open ocean
may use fixed-wing aircraft only.
The three-class breakdown
is the framework
the agency selects from,
not a prescription.

## Capital Outlay

Acquisition costs
for search-and-rescue-class
unmanned aerial vehicles
vary
by more than two orders of magnitude
across the three classes
and within them.
The figures below
are list prices or typical contract prices
from public vendor information
and public procurement records
as of 2026.
A program manager
should treat them
as orienting estimates,
not as quotes.

**Fixed-wing aircraft
in the search-and-rescue class.**
The
[AeroVironment Puma 3 AE][ref_puma_3_ae],
a battery-powered hand-launched
fixed-wing aircraft,
sells to US government customers
through the
[US Department of Defense Blue UAS list][ref_blue_uas]
in configurations
priced
in the range of 250 000 to 400 000 US dollars
per system,
where a system includes the aircraft,
a ground control station,
and a payload package.
The
[Insitu ScanEagle][ref_scaneagle],
which uses a catapult launch
and a Skyhook recovery
and runs on heavy fuel,
sells to military and commercial customers
at substantially higher prices,
typically in the
several hundreds of thousands
to over a million US dollars per system
depending on payload configuration.
The
[UAV Factory Penguin C][ref_penguin_c]
and similar long-endurance fixed-wing platforms
fall in the
two hundred thousand
to half-million dollar range
for the airframe
plus another fraction
for payload and ground station.

Lower-cost fixed-wing search-and-rescue platforms,
including
modified commercial off-the-shelf fixed-wing kits,
sell in the
ten thousand
to fifty thousand dollar range,
but these platforms
do not match
the endurance, payload, or weather tolerance
of the established public-safety systems.

**Multicopters
in the search-and-rescue class.**
The
[DJI Matrice 30T][ref_matrice_30t],
a folding quadcopter
with integrated thermal and electro-optical sensors,
sells at retail
in the range of
ten thousand to fourteen thousand US dollars
in 2026.
The
[DJI Matrice 350 RTK][ref_matrice_350],
a heavier-payload quadcopter,
sells in the range of
ten thousand
to fifteen thousand dollars
for the airframe alone,
plus another five thousand
to fifteen thousand dollars
for a thermal and electro-optical payload,
giving a typical system price
of twenty thousand to thirty thousand dollars.
The
[Skydio X10][ref_skydio_x10],
a United-States-manufactured quadcopter
that public-safety agencies
adopt where
[the National Defense Authorization Act
restrictions on Chinese-manufactured drones][ref_ndaa_drones]
apply,
sells at higher prices,
typically
fifteen thousand to twenty-five thousand dollars
per system.
The
[Autel EVO Max 4T][ref_autel_max_4t]
sells in the
seven thousand
to twelve thousand dollar range.

Higher-end multicopters
for specialised search-and-rescue payloads,
including
infrared-cooled sensors,
LiDAR scanners,
or chemical detectors,
add
ten thousand to fifty thousand dollars
to the payload cost.

**Hybrid vertical-takeoff-and-landing
aircraft
in the search-and-rescue class.**
The
[WingtraOne Gen II][ref_wingtra_one],
a tail-sitter mapping aircraft,
sells in the range of
twenty thousand to forty thousand US dollars
depending on sensor configuration.
The
[Quantum Systems Trinity F90+][ref_trinity_f90]
sells in the range of
thirty thousand to fifty thousand dollars.
The
[Quantum Systems Vector][ref_quantum_vector],
a heavier-payload tail-sitter
intended for reconnaissance applications,
sells in the
fifty thousand to one hundred thousand dollar range.
Larger hybrid platforms
in the military
or military-adjacent class
sell at higher prices,
typically
several hundred thousand dollars per system.

| Platform class | Typical platform price (USD) | Typical system price including payload (USD) |
|---|---|---|
| Multicopter (commercial off-the-shelf) | 7,000 to 25,000 | 10,000 to 35,000 |
| Hybrid VTOL (commercial) | 20,000 to 100,000 | 30,000 to 150,000 |
| Fixed-wing (commercial small) | 10,000 to 50,000 | 20,000 to 100,000 |
| Fixed-wing (government-grade) | 200,000 to 1,000,000 | 250,000 to 1,500,000 |

The price difference
between the classes
reflects three factors.
First, the engineering complexity
of the platform.
A multicopter
is mechanically simpler
than a hybrid
which is simpler
than a long-endurance fixed-wing system.
Second, the regulatory and supply-chain posture.
A platform certified
for US government use
under the Blue UAS programme
or built from
[NDAA Section 848-compliant components][ref_ndaa_848]
carries a premium
of two to ten times
relative to
the same airframe
without the compliance pedigree.
Third, the integrated capability.
A consumer multicopter
ships
with a ground control station
and payload
in the box.
A government-grade fixed-wing system
ships
with a hardened ground control station,
a catapult or launcher,
a recovery system,
spares, and training.
The integrated system
is more expensive
because it includes more.

A search-and-rescue agency
budgeting for unmanned aerial vehicle capability
should expect
to spend
fifty thousand to two hundred thousand dollars
to field a credible
multicopter-plus-fixed-wing combination
at the public-safety level,
or several hundred thousand
to a million dollars
to field a system
at the government-procurement level.

## Upkeep Costs

The total cost of ownership
of an unmanned aerial vehicle
program
extends well beyond
the acquisition cost.
Recurring upkeep
includes
batteries, propellers, motors,
airframe inspection,
sensor calibration,
ground-station maintenance,
data-link spectrum coordination,
insurance,
and
parts replacement after incidents.

**Batteries.**
Lithium-polymer flight batteries
in this class
have cycle lives
of approximately 200 to 500 cycles
before noticeable capacity decline,
and 500 to 1000 cycles
before the battery
is unsafe to use.
Each cycle is typically
twenty to ninety minutes of flight
plus charging and cooling.
A multicopter battery
costs
two hundred to fifteen hundred dollars
depending on the platform.
A platform that flies
fifty hours per year
might consume
two to ten batteries per year
at an annual cost
of four hundred to fifteen thousand dollars.
A fixed-wing platform
runs through fewer batteries
because each flight is longer,
but the batteries
are correspondingly larger and more expensive.
The
[DJI battery management notes][ref_dji_battery_care]
illustrate the routine care
required to preserve battery life.

**Propellers.**
Multicopter propellers
are typically inexpensive
at five to twenty-five dollars per propeller
and are replaced
every fifty to one hundred flight hours
or sooner if damaged.
Fixed-wing propellers
are more expensive
at twenty-five to two hundred dollars
and are replaced
less frequently.
A search-and-rescue program
typically budgets
two to five percent
of the acquisition cost
annually
for propeller replacement
across the fleet.

**Motors and electronic speed controllers.**
Motor bearings
wear out
on the order of
one hundred to one thousand flight hours
depending on the motor class.
Motors and electronic speed controllers
together
account for
one to three percent
of acquisition cost
annually
in routine maintenance.

**Airframe inspection.**
Carbon-fibre and composite airframes
require periodic inspection
for delamination, cracks, and impact damage.
Manufacturer maintenance schedules
typically prescribe
every-twenty-five-hour
or every-fifty-hour
visual inspection
plus annual non-destructive evaluation.
A program
operating multiple platforms
may need
a dedicated maintenance technician
or a contracted maintenance arrangement.

**Sensor calibration.**
Thermal infrared sensors
drift
in their calibration
over months of operation.
Electro-optical sensors
require periodic
focus and image-quality verification.
LiDAR sensors
require
factory recalibration
on multi-year intervals.
Sensor maintenance costs
are sensor-specific
and run from
a few hundred dollars per year
for consumer-grade sensors
to tens of thousands per year
for specialised payloads.

**Ground station and data-link infrastructure.**
Ground stations
typically last
five to ten years
before replacement.
Antennas and cables
wear with field use
and require periodic replacement.
Data-link spectrum,
where licensed,
involves
annual fees
to the relevant regulator.
The
[Federal Communications Commission Part 90][ref_fcc_part_90]
governs public-safety spectrum
in the United States.

**Insurance.**
[Commercial drone insurance][ref_drone_insurance]
in the United States
typically costs
five hundred to two thousand dollars
per platform per year
for liability coverage,
plus optional hull coverage
that adds
two to ten percent of the hull value
annually.
A program with multiple platforms
may negotiate
a fleet policy
at lower per-platform rates.

**Incident repair.**
Crashes happen.
A typical
operating program
should budget
five to fifteen percent
of acquisition cost annually
for incident repair,
recognising that
in any given year
the actual figure
may be zero
or may be the full replacement cost
of a destroyed platform.

| Cost category | Multicopter (annual) | Fixed-wing (annual) | Hybrid VTOL (annual) |
|---|---|---|---|
| Batteries | $400 to $5,000 | $1,000 to $10,000 | $1,000 to $7,000 |
| Propellers | $200 to $1,000 | $200 to $1,500 | $400 to $2,000 |
| Motors and ESCs | $200 to $1,500 | $500 to $5,000 | $500 to $4,000 |
| Airframe inspection | $500 to $3,000 | $1,000 to $10,000 | $1,000 to $8,000 |
| Sensor calibration | $500 to $10,000 | $1,000 to $20,000 | $1,000 to $15,000 |
| Ground station | $500 to $2,000 | $1,000 to $5,000 | $1,000 to $4,000 |
| Spectrum | $0 to $1,000 | $0 to $2,000 | $0 to $1,500 |
| Insurance | $500 to $3,000 | $2,000 to $10,000 | $1,500 to $7,000 |
| Incident repair budget | $500 to $5,000 | $5,000 to $50,000 | $2,000 to $20,000 |
| **Annual total range** | **$3,300 to $30,500** | **$11,700 to $113,500** | **$8,400 to $68,500** |

The table is per platform
under typical search-and-rescue
operational tempo,
namely
fifty to two hundred flight hours per year.
A heavily used program
or one with multiple platforms
should scale accordingly.

The annualised cost of ownership
typically runs
fifteen to thirty percent
of acquisition cost
per year
for fixed-wing platforms,
ten to twenty-five percent
for hybrids,
and twenty to forty percent
for multicopters
because of the higher relative cost
of batteries
on the smaller platforms.
Over a five-year service life
the cumulative upkeep
approaches or exceeds
the acquisition cost.

## Personnel Training

A search-and-rescue UAV program
cannot fly
without trained operators,
and the training requirements
differ
across the three platform classes.

**Regulatory minimum.**
In the United States,
the
[Federal Aviation Administration Part 107
remote pilot certificate][ref_faa_part_107]
is the minimum certification
for commercial small-UAV operation
including public-safety use.
The certificate requires
passing an aeronautical-knowledge test
covering airspace, weather,
loading and performance,
operations, and regulations.
The test costs
175 US dollars
as of 2026.
Self-study materials
are free.
Prep courses
from
[Pilot Institute][ref_pilot_institute],
[King Schools][ref_king_schools],
and others
cost
one hundred to five hundred dollars.
The certificate
must be renewed
every twenty-four months
through a free online recurrent course.

For platforms over 55 pounds gross takeoff weight,
which includes
larger fixed-wing aircraft
and some hybrid platforms,
the operator
must hold a
[Part 91 airworthiness exemption][ref_part_91_exemption]
or a
[Part 137 certificate][ref_part_137]
for specific commercial operations,
or operate
under a
[public-aircraft exemption][ref_public_aircraft]
if the operator is a government agency
conducting public-safety missions.

For operations
beyond visual line of sight,
which most search-and-rescue missions are not,
the operator
needs either a
[Section 44807 exemption][ref_section_44807],
a Part 91 exemption,
or the eventual
[Part 108 BVLOS rule][ref_part_108]
once it is finalised.

**Manufacturer-specific training.**
Each platform manufacturer
offers training
on the specific platform.
[DJI Academy][ref_dji_academy]
courses
range from
self-paced online modules
at no cost
to instructor-led week-long courses
at two thousand to five thousand dollars
per student.
[Skydio Academy][ref_skydio_academy]
courses
are typically
included with platform purchase
for the first operators
and charged
for additional operators
at lower rates than DJI's instructor-led courses.
[AeroVironment][ref_aerovironment_training]
and
[Quantum Systems training][ref_quantum_training]
courses
on the respective fixed-wing
and hybrid platforms
typically cost
five thousand to fifteen thousand dollars
per student
and require
a week to two weeks of in-person attendance.

**Operational training.**
[The Texas A&M Engineering Extension Service][ref_teex]
runs
public-safety drone training courses
for search-and-rescue operators
at rates from
five hundred to two thousand dollars per student per course.
[DRONERESPONDERS][ref_droneresponders],
a national public-safety UAS programme,
provides resources, mutual-aid coordination,
and standardised training curricula.
[NIST's Standard Test Methods for Small Unmanned Aircraft Systems][ref_nist_tests]
provide an objective test framework
that public-safety programs use
for operator proficiency evaluation.

**Search-and-rescue specific training.**
[The National Association for Search and Rescue][ref_nasar]
and
[the Search and Rescue Society of British Columbia][ref_sarbc]
provide
SAR-specific training curricula
that operators
augment with the platform-specific training above.
Search pattern execution,
sensor operator skills,
incident command integration,
and crew coordination
are taught
in courses
ranging from one-day workshops
to multi-week academies.

**Recurrency and proficiency.**
Operator proficiency
decays
with non-use.
A typical public-safety program
requires
each operator to log
a minimum of
two to ten flight hours per month
on each platform type
to maintain currency.
A program operating
both multicopters and fixed-wing aircraft
must support
recurrency on both,
which doubles the training overhead
per operator.

| Training cost category | Multicopter operator | Fixed-wing operator | Hybrid VTOL operator |
|---|---|---|---|
| FAA Part 107 (one time) | $175 plus prep | $175 plus prep | $175 plus prep |
| Manufacturer training (one time) | $0 to $3,000 | $5,000 to $15,000 | $3,000 to $10,000 |
| Search-and-rescue specific training | $500 to $3,000 | $500 to $3,000 | $500 to $3,000 |
| Annual recurrency flight hours | 20 to 60 hours | 30 to 100 hours | 30 to 80 hours |
| Annual recurrency cost (battery, fuel, range fees) | $500 to $5,000 | $1,000 to $15,000 | $1,000 to $10,000 |

A search-and-rescue program
typically operates
with
three to ten qualified operators
per platform type
to maintain
weather, illness, and turnover resilience.
The cumulative training investment
for a program
operating both fixed-wing and multicopter
platforms
runs
fifty thousand to two hundred thousand dollars
in the first year
and tens of thousands per year
in steady state.

## The Hybrid Compromise

A program manager
choosing among the three classes
under budget constraint
may consider the hybrid VTOL
as a compromise platform
that delivers
much of the fixed-wing endurance
and the multicopter launch and recovery flexibility
in a single aircraft.
The compromise is real
but it is a compromise,
not a free lunch.

**What the hybrid gives up
relative to a dedicated fixed-wing.**
The hybrid carries
either dead-weight rotors
through cruise
or mechanical-tilt complexity
across the regime transition.
Cruise endurance
is twenty to fifty percent shorter
than a fixed-wing aircraft
of equivalent mass and battery capacity.
The cruise speed
is slightly lower,
typically 15 to 25 metres per second
versus 20 to 35 for a fixed-wing.
The launch and recovery flexibility
is paid for
in the cruise performance.

**What the hybrid gives up
relative to a dedicated multicopter.**
The hybrid
is mechanically more complex,
heavier,
and harder to operate at low altitude
in confined spaces.
A hybrid in hover
is typically less manoeuvrable
than a dedicated multicopter
of equivalent mass
because the rotors
must work harder
against the additional
drag and inertia
of the wing.
Hover endurance
is shorter
than a dedicated multicopter
because the cruise propulsion system
adds dead weight in hover.

**Where the hybrid is the right choice.**
A program
whose mission profile
is moderate-area search
in unimproved terrain
that cannot support
a fixed-wing launcher and recovery
benefits from the hybrid.
A program with a single platform budget
that needs both
moderate endurance and vertical launch and recovery
benefits from the hybrid.
A program
that needs to operate in close proximity
to a small site
without a runway
and that does not need
the long endurance
of a dedicated fixed-wing
benefits from the hybrid.

**Where the hybrid is the wrong choice.**
A program
that runs frequent
high-endurance area searches
should buy a dedicated fixed-wing
and accept the launch and recovery infrastructure.
A program
that runs frequent
close-target investigations
should buy a dedicated multicopter
and accept the endurance limit.
A program
with budget
for both
should buy both
rather than a hybrid,
because each dedicated platform
outperforms the hybrid
in its native regime.

| Property | Pure fixed-wing | Hybrid VTOL | Pure multicopter |
|---|---|---|---|
| Endurance | Best | Intermediate | Worst |
| Cruise efficiency | Best | Intermediate | Worst |
| Hover and dwell | Worst | Intermediate | Best |
| Launch and recovery footprint | Worst | Best | Best |
| Mechanical complexity | Best | Worst | Best |
| Acquisition cost in class | Highest | Intermediate | Lowest |
| Maintenance complexity | Intermediate | Highest | Lowest |

The hybrid
occupies the middle of the table
on most properties.
That is the correct choice
when the operational profile
sits in the middle,
and the wrong choice
when the operational profile
sits at the edge.

## Out of Scope

This article restricts itself
to the comparative analysis
of the three platform classes
on physics, economics, and training axes
under the search-and-rescue worked example.
Five substantive topics
are deliberately deferred
to other articles or follow-up work.

**Detailed regulatory compliance.**
The Federal Aviation Administration's
[Part 107 framework][ref_faa_part_107],
the European Union Aviation Safety Agency's
[Open, Specific, and Certified categories][ref_easa_uas],
and the various national equivalents
form a substantial body
of rules and exemptions
that a real program
must navigate.
The
[regulatory and operations layer
article in this series][related_post_regulatory]
covers
the regulatory framework
for fixed-wing operations specifically.
A multicopter and hybrid
regulatory companion
would extend it.

**Sensor technology in depth.**
Thermal infrared sensors,
LiDAR scanners,
synthetic-aperture radar,
multispectral cameras,
and active emitters
each deserve
their own treatment.
The
[payload and mission systems
article in this series][related_post_payload]
covers
the payload integration
question
for fixed-wing platforms.
A sensor-comparison article
across platform classes
would be a useful follow-up.

**Weather minima and operational envelopes.**
The wind, precipitation,
temperature, altitude,
and icing limits
of specific platforms
are vendor-specific
and operationally critical.
This article gives
order-of-magnitude figures
only.
A weather operations article
would treat the question
in detail.

**Mission-system architecture.**
Search planning,
incident command system integration,
multi-aircraft coordination,
data fusion across sensors,
and post-mission analysis
all involve
substantial mission-system infrastructure
that this article does not address.

**Specific procurement guidance.**
This article gives
price ranges
for platform classes,
not procurement recommendations
for specific platforms.
The
[SBIR and STTR
worked campaign article][related_post_sbir_worked]
treats
the federal procurement
dimension
for small unmanned aerial vehicle
acquisition.

## Conclusion

Fixed-wing, multicopter,
and hybrid vertical-takeoff-and-landing
unmanned aerial vehicles
serve search and rescue
through complementary roles
that the underlying physics determines.
A fixed-wing aircraft
sweeps wide areas
because its lift mechanism
trades velocity for energy efficiency.
A multicopter
investigates targets and delivers payloads
because its lift mechanism
holds position without forward motion.
A hybrid
compromises between the two
when the operational profile sits in the middle
and the budget does not support
both dedicated platforms.

The capital outlay
spans from
ten thousand dollars
for a consumer-grade multicopter
to over a million dollars
for a government-grade
long-endurance fixed-wing system,
which is a hundred-fold range
across platforms
that share the same general purpose.
The upkeep
runs
ten to forty percent of acquisition cost
annually
and approaches or exceeds
the acquisition cost
over a five-year service life.
The training
runs from
under five hundred dollars
for a single operator
on a single multicopter
to over a hundred thousand dollars
for a multi-operator multi-platform program
with full SAR-specific curricula.

A search-and-rescue program
that takes
unmanned aerial vehicle capability
seriously
budgets
for at least one platform per role,
trains
three to ten operators per platform type,
and accepts
that the total cost of ownership
over five years
is approximately twice the acquisition cost.
A program
with that level of commitment
will outperform
both
the program that owns only multicopters
and the program that owns only fixed-wing aircraft
across the realistic range of incidents.

The physics
does not favour
a single platform class
across all phases of all incidents.
A serious program
acknowledges
the asymmetry
the physics imposes
and budgets accordingly.

## References

- [Reference, AeroVironment Puma 3 AE][ref_puma_3_ae]
- [Reference, AeroVironment Training Programs][ref_aerovironment_training]
- [Reference, Autel EVO Max 4T][ref_autel_max_4t]
- [Reference, Bell Boeing V-22 Osprey][ref_v_22]
- [Reference, Breguet Range and Endurance Equation][ref_breguet]
- [Reference, Commercial Drone Insurance Overview][ref_drone_insurance]
- [Reference, DJI Academy][ref_dji_academy]
- [Reference, DJI Battery Care][ref_dji_battery_care]
- [Reference, DJI Matrice 30T][ref_matrice_30t]
- [Reference, DJI Matrice 350 RTK][ref_matrice_350]
- [Reference, DRONERESPONDERS National Public Safety UAS Program][ref_droneresponders]
- [Reference, Elbit Systems Skylark][ref_skylark]
- [Reference, EASA Open Specific and Certified Categories for UAS][ref_easa_uas]
- [Reference, Expanding Square Search Pattern][ref_search_pattern]
- [Reference, FAA Part 107 Small Unmanned Aircraft Rule][ref_faa_part_107]
- [Reference, FAA Part 137 Agricultural Aircraft Operations][ref_part_137]
- [Reference, FAA Public Aircraft Operations Exemption][ref_public_aircraft]
- [Reference, FAA Section 44807 Exemption for Civil Operations][ref_section_44807]
- [Reference, FCC Part 90 Private Land Mobile Radio Services][ref_fcc_part_90]
- [Reference, Figure of Merit for Rotors][ref_figure_of_merit]
- [Reference, Insitu ScanEagle][ref_scaneagle]
- [Reference, King Schools Drone Pilot Test Preparation][ref_king_schools]
- [Reference, Low-Reynolds-Number Flight Regime][ref_low_re]
- [Reference, Matternet Drone Delivery Network][ref_matternet]
- [Reference, National Association for Search and Rescue][ref_nasar]
- [Reference, National Defense Authorization Act Drone Restrictions][ref_ndaa_drones]
- [Reference, NDAA Section 848 Compliant Components][ref_ndaa_848]
- [Reference, NIST Standard Test Methods for Small Unmanned Aircraft Systems][ref_nist_tests]
- [Reference, Parallel Track Search Pattern][ref_parallel_track]
- [Reference, Part 108 Beyond Visual Line of Sight Rule][ref_part_108]
- [Reference, Part 91 Airworthiness Exemption for Larger UAS][ref_part_91_exemption]
- [Reference, Pilot Institute Drone Training][ref_pilot_institute]
- [Reference, Quad-plane VTOL Convertiplane][ref_quad_plane]
- [Reference, Quantum Systems Trinity F90+][ref_trinity_f90]
- [Reference, Quantum Systems Training Programs][ref_quantum_training]
- [Reference, Quantum Systems Vector][ref_quantum_vector]
- [Reference, Rankine and Froude Actuator Disk Theory][ref_actuator_disk]
- [Reference, Reynolds Number][ref_reynolds_number]
- [Reference, Search and Rescue Society of British Columbia][ref_sarbc]
- [Reference, Skydio Academy][ref_skydio_academy]
- [Reference, Skydio X10][ref_skydio_x10]
- [Reference, Tail-Sitter Aircraft][ref_tail_sitter]
- [Reference, Texas A&M Engineering Extension Service Drone Programs][ref_teex]
- [Reference, Tilt-Rotor Aircraft][ref_tilt_rotor]
- [Reference, Tilt-Wing Aircraft][ref_tilt_wing]
- [Reference, UAV Factory Penguin C][ref_penguin_c]
- [Reference, US Department of Defense Blue UAS List][ref_blue_uas]
- [Reference, VTOL Convertiplane Configuration][ref_convertiplane]
- [Reference, WingtraOne Gen II][ref_wingtra_one]
- [Reference, Zipline Drone Delivery System][ref_zipline]
- [Related Post, Electric Energy Systems and Endurance Budget for Fixed-Wing UAVs][related_post_electric_energy]
- [Related Post, Launch and Recovery Systems for Fixed-Wing UAVs][related_post_launch_recovery]
- [Related Post, Payload and Mission Systems for Fixed-Wing UAVs][related_post_payload]
- [Related Post, Propulsion and Power Sizing for Fixed-Wing UAVs][related_post_propulsion]
- [Related Post, Regulatory and Operations Layer for Fixed-Wing UAVs][related_post_regulatory]
- [Related Post, Runway Sizing for Fixed-Wing UAVs][related_post_runway_sizing]
- [Related Post, A Worked SBIR and STTR Campaign for a Fixed-Wing UAV][related_post_sbir_worked]

[ref_actuator_disk]: https://en.wikipedia.org/wiki/Momentum_theory
[ref_aerovironment_training]: https://www.avinc.com/uas/training
[ref_autel_max_4t]: https://www.autelrobotics.com/productdetail/evo-max-4t/
[ref_blue_uas]: https://www.diu.mil/blue-uas-cleared-list
[ref_breguet]: https://en.wikipedia.org/wiki/Breguet_range_equation
[ref_convertiplane]: https://en.wikipedia.org/wiki/Convertiplane
[ref_dji_academy]: https://enterprise.dji.com/training
[ref_dji_battery_care]: https://enterprise.dji.com/news/detail/best-practices-for-dji-enterprise-drone-batteries
[ref_drone_insurance]: https://www.faa.gov/uas/getting_started/registered_drones/uas_insurance
[ref_droneresponders]: https://www.droneresponders.org/
[ref_easa_uas]: https://www.easa.europa.eu/en/domains/civil-drones/drones-regulatory-framework-background
[ref_faa_part_107]: https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107
[ref_fcc_part_90]: https://www.fcc.gov/private-land-mobile-radio-services
[ref_figure_of_merit]: https://en.wikipedia.org/wiki/Figure_of_merit
[ref_king_schools]: https://www.kingschools.com/courses/drone
[ref_low_re]: https://en.wikipedia.org/wiki/Reynolds_number
[ref_matrice_30t]: https://enterprise.dji.com/matrice-30
[ref_matrice_350]: https://enterprise.dji.com/matrice-350-rtk
[ref_matternet]: https://mttr.net/
[ref_nasar]: https://nasar.org/
[ref_ndaa_848]: https://www.diu.mil/blue-uas-cleared-list
[ref_ndaa_drones]: https://www.federalregister.gov/documents/2024/01/03/2023-28867/restricted-foreign-entities
[ref_nist_tests]: https://www.nist.gov/el/intelligent-systems-division-73500/cooperative-systems/standard-test-methods-response-robots
[ref_parallel_track]: https://en.wikipedia.org/wiki/Search_and_rescue#Search_patterns
[ref_part_108]: https://www.faa.gov/uas/advanced_operations/beyond_visual_line_of_sight
[ref_part_137]: https://www.ecfr.gov/current/title-14/chapter-I/subchapter-G/part-137
[ref_part_91_exemption]: https://www.faa.gov/uas/advanced_operations/certification
[ref_penguin_c]: https://edgeautonomy.io/uncrewed-systems/penguin-c-mk2/
[ref_pilot_institute]: https://pilotinstitute.com/
[ref_public_aircraft]: https://www.faa.gov/uas/public_safety_gov
[ref_puma_3_ae]: https://www.avinc.com/uas/puma-3-ae
[ref_quad_plane]: https://en.wikipedia.org/wiki/VTOL
[ref_quantum_training]: https://quantum-systems.com/services/
[ref_quantum_vector]: https://quantum-systems.com/vector/
[ref_reynolds_number]: https://en.wikipedia.org/wiki/Reynolds_number
[ref_sarbc]: https://www.bcsara.com/
[ref_scaneagle]: https://en.wikipedia.org/wiki/Boeing_Insitu_ScanEagle
[ref_search_pattern]: https://en.wikipedia.org/wiki/Search_and_rescue#Search_patterns
[ref_section_44807]: https://www.faa.gov/uas/advanced_operations/section_44807
[ref_skydio_academy]: https://www.skydio.com/skydio-academy
[ref_skydio_x10]: https://www.skydio.com/x10
[ref_skylark]: https://en.wikipedia.org/wiki/Elbit_Skylark
[ref_tail_sitter]: https://en.wikipedia.org/wiki/Tailsitter
[ref_teex]: https://teex.org/program/utap/
[ref_tilt_rotor]: https://en.wikipedia.org/wiki/Tiltrotor
[ref_tilt_wing]: https://en.wikipedia.org/wiki/Tiltwing
[ref_trinity_f90]: https://quantum-systems.com/trinity-f90-plus/
[ref_v_22]: https://en.wikipedia.org/wiki/Bell_Boeing_V-22_Osprey
[ref_wingtra_one]: https://wingtra.com/mapping-drone-wingtraone/
[ref_zipline]: https://www.flyzipline.com/
[related_post_electric_energy]: {% post_url 2026-06-04-electric_energy_systems_and_endurance_budget_for_fixed_wing_uavs %}
[related_post_launch_recovery]: {% post_url 2026-06-01-launch_and_recovery_systems_for_fixed_wing_uavs %}
[related_post_payload]: {% post_url 2026-06-13-payload_and_mission_systems_for_fixed_wing_uavs %}
[related_post_propulsion]: {% post_url 2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs %}
[related_post_regulatory]: {% post_url 2026-06-14-regulatory_and_operations_layer_for_fixed_wing_uavs %}
[related_post_runway_sizing]: {% post_url 2026-05-31-runway_sizing_for_fixed_wing_uavs %}
[related_post_sbir_worked]: {% post_url 2026-06-27-worked_sbir_and_sttr_campaign_for_a_fixed_wing_uav %}
