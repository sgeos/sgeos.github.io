---
layout: post
mathjax: true
comments: true
title:  "Two-Stage Flying Delta Wing Vehicles for Civil and National Security Applications"
date:   2026-03-12 16:05:00 +0000
categories: aerospace engineering
---

<!-- A106 -->
<script>console.log("A106");</script>

Multi-stage vehicles have been the foundation
of orbital access since the earliest days
of spaceflight.
The [Tsiolkovsky rocket equation][ref_rocket_equation]
imposes a fundamental relationship
between payload fraction, exhaust velocity,
and the mass ratio of a launch vehicle.
For missions requiring orbital velocity
of approximately 7.8 kilometers per second,
the mass ratios demanded by chemical propulsion
make single-stage vehicles
extraordinarily difficult to build
with current materials and engines.
[Two-stage-to-orbit][ref_tsto] architectures
address this problem
by dividing the velocity budget
between a first stage
that operates in the dense lower atmosphere
and a second stage
that completes the ascent to orbit.

Existing two-stage orbital systems
have relied on expendable hardware.
The [Space Shuttle][ref_shuttle]
discarded its external tank on every flight.
Expendable rockets from Atlas through Soyuz
discard their first stages entirely.
Even [SpaceX Starship][ref_starship],
the most ambitious reusable vehicle
currently under development,
recovers its first stage
through a vertical propulsive landing
that requires the booster to carry
significant fuel reserves
for its return.

The concept examined in this article
takes a different approach.
It proposes a vehicle architecture
in which both stages
are independently flyable aircraft.
The combined vehicle
is a pure [flying delta wing][ref_delta_wing].
The second stage retains
the nose and forward geometry
of the combined vehicle,
remaining a complete delta wing
after separation.
The first stage retains
the rear geometry
and flies as a truncated delta wing,
returning to base
under its own aerodynamic control.

This architecture offers
a distinctive advantage
over conventional reusable launch concepts.
Neither stage requires
vertical landing propulsion,
parachute recovery,
or expendable structural elements.
Both stages glide or fly
back to a runway
using the same aerodynamic surfaces
they employed during the boost phase.

The [delta wing][ref_delta_wing] planform
is uniquely suited to this concept
for several reasons.
Delta wings operate efficiently
across a wide range of [Mach numbers][ref_mach_number],
from subsonic approach speeds
through [hypersonic][ref_hypersonic] flight.
They provide large internal volumes
for fuel and payload.
Their triangular planform
distributes structural loads efficiently.
And their [vortex lift][ref_vortex_lift]
characteristics
enable controlled flight
at the high angles of attack
required for low-speed landing
of high-wing-loading vehicles.

This article examines
the two-stage flying delta wing concept
from multiple perspectives.
It describes the system architecture
and flight phases,
surveys the historical context
of related programs,
analyzes the aerodynamic
and structural properties
of delta wings
that make this concept feasible,
and evaluates potential applications
in both civil and national security domains.

For the historical development
of rocketplanes and reusable spacecraft,
see the companion article
[History of Rocketplanes][related_post_rocketplanes].
For the mathematical foundations
of orbital mechanics
and atmospheric flight dynamics,
see
[Introduction to Space Studies][related_post_space_studies].

## Software Versions

```sh
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-03-12 16:05:00 +0000
$ uname -vm
Darwin Kernel Version 23.6.0: Wed Jul 31 20:48:46 PDT 2024; root:xnu-10063.141.1.700.5~1/RELEASE_ARM64_T6000 arm64
```

## System Concept Overview

### Combined Vehicle Configuration

The combined vehicle
presents a clean [delta wing][ref_delta_wing] planform
to the airstream during the boost phase.
From the exterior,
the vehicle is indistinguishable
from a single large [flying wing][ref_flying_wing]
aircraft.
The [swept][ref_swept_wing] leading edges
extend from an apex at the nose
to a wide trailing edge at the rear.
The vehicle has no separate fuselage,
no horizontal tail,
and no vertical tail.
All internal systems,
including fuel tanks, payload bays,
propulsion systems,
and avionics,
are housed within the wing structure.

The leading edge sweep angle
of the combined vehicle
determines the [Mach number][ref_mach_number] range
over which the leading edges
remain aerodynamically subsonic.
For a vehicle designed to stage
at Mach 4 to Mach 6,
a leading edge sweep
of 70 to 75 degrees
would keep the velocity component
normal to the leading edge
below the speed of sound
throughout the first-stage burn,
reducing leading-edge heating
and wave drag.

The combined vehicle configuration
places the second stage
in the forward section
and the first stage
in the aft section.
The dividing plane
between the two stages
runs approximately perpendicular
to the vehicle centerline,
though in practice
the interface would follow
a more complex three-dimensional geometry
designed to minimize aerodynamic disruption
after separation.

### Second Stage Configuration

After separation,
the second stage retains
the nose, the forward leading edges,
and the forward structural section
of the combined vehicle.
This portion of the vehicle
is itself a complete [delta wing][ref_delta_wing],
smaller than the combined vehicle
but geometrically similar.
The second stage has a pointed nose,
swept leading edges,
and a trailing edge
that was previously
the internal separation plane
of the combined vehicle.

The second stage carries
its own propulsion system,
fuel supply, payload bay,
and flight control surfaces.
Because it retains the nose
and forward aerodynamic geometry
of the combined vehicle,
its aerodynamic characteristics
are well understood
from the combined vehicle's flight data.
The [center of pressure][ref_center_of_pressure]
and center of gravity
of the second stage
are designed to produce
a stable or controllably unstable configuration
after separation.

### First Stage Configuration

The first stage, after separation,
becomes a truncated
or noseless delta wing.
It retains the aft structural section,
the rear portion
of the swept leading edges,
the trailing edge,
the main landing gear,
and the first-stage propulsion system.
The forward face of the first stage,
where the second stage
was previously attached,
becomes a blunt or flat surface.

This surface represents
the most significant aerodynamic departure
from a conventional aircraft configuration.
At supersonic speeds,
a blunt forward face
generates a strong bow shock
and substantial wave drag.
At the subsonic speeds
characteristic of the return flight,
the drag penalty is less severe
but still significant
compared to a conventional
pointed or rounded nose.

The truncated first stage
is aerodynamically related
to several existing aircraft types.
Large [flying wing][ref_flying_wing] aircraft
such as the [Northrop Grumman B-2 Spirit][ref_b2]
and [B-21 Raider][ref_b21]
operate without a pointed nose
or forward fuselage.
[Blended wing body][ref_blended_wing_body] concepts
such as the [Boeing X-48][ref_x48]
demonstrate that wide,
blunt-forward planforms
can achieve stable,
controllable flight.
The [Northrop Grumman X-47B][ref_x47b]
demonstrated autonomous operations
with a tailless planform
that shares geometric similarities
with a truncated delta.

### Control Surfaces and Flight Systems

All three configurations
rely on elevon control surfaces
along the trailing edge
for pitch and roll authority.
Yaw control on a tailless delta wing
is achieved through
differential elevon deflection,
split drag rudders,
or thrust vectoring.

A [fly-by-wire][ref_fly_by_wire]
flight control system
is essential for all three configurations.
The combined vehicle
must maintain stability
from takeoff through supersonic flight.
The second stage
must maintain stability
from the staging Mach number
through orbital insertion or hypersonic cruise
and back through reentry and landing.
The first stage
must maintain stability
from the staging Mach number
through subsonic flight and landing,
despite the significant geometry change
that occurs when the nose section departs.

### Flight Phases

The mission proceeds through seven phases.
During takeoff,
the combined vehicle departs
a conventional runway
using first-stage propulsion.
During atmospheric climb,
the first-stage engines accelerate
the combined vehicle
through the dense lower atmosphere
to the staging altitude and velocity.
During staging,
at approximately Mach 4 to 6
and 25 to 30 kilometers altitude,
the second stage separates
forward and upward.
During first-stage return,
the truncated delta wing decelerates,
turns back toward the launch site,
and lands on a runway.
During the second-stage mission,
the second stage continues
to orbit, hypersonic cruise,
or another mission objective.
If returning from orbit,
the second stage performs
a controlled atmospheric reentry.
The mission concludes
when the second stage glides
to a runway landing.

### Propulsion Placement

The first-stage engines
are located in the aft section
and remain with the first stage
after separation.
The second-stage engines
are located in the forward section
and separate with the second stage.
Fuel tanks are distributed
throughout both sections,
with the separation plane
designed to sever fuel lines
and structural connections cleanly.
Fuel transfer between sections
before separation
allows the crew or flight computer
to position the center of gravity
of each stage
for optimal post-separation stability.

## History of Related Concepts

### Delta Wing Aircraft

The [delta wing][ref_delta_wing] planform
traces its origins
to the work of
[Alexander Lippisch][ref_lippisch]
in Germany during the 1930s and 1940s.
Lippisch recognized
that highly swept triangular wings
offered favorable characteristics
at high speeds,
including low wave drag
and structural simplicity.
His research contributed
to the [Messerschmitt Me 163 Komet][ref_me_163],
a rocket-powered interceptor
that used a highly swept wing
closely related to the delta planform.

After the war, Lippisch's work
was brought to the United States
through [Operation Paperclip][ref_paperclip].
The [Convair XF-92A][ref_xf92],
which first flew in 1948,
became the first powered aircraft
to fly with a true delta wing.
This prototype led directly
to the [Convair F-102 Delta Dagger][ref_f102],
the first operational delta wing fighter,
which entered service in 1956.
The F-102 was followed by
the [Convair F-106 Delta Dart][ref_f106],
an improved interceptor
that remained in service until 1988.

The delta wing proved
particularly effective
for supersonic flight.
The [Convair B-58 Hustler][ref_b58],
which first flew in 1956,
became the first operational supersonic bomber.
The [Dassault Mirage III][ref_mirage_iii],
which entered French Air Force service in 1961,
demonstrated that a relatively simple
tailless delta wing
could achieve Mach 2
without the complexity
of variable-geometry wings
or canard surfaces.
The Mirage III and its successors
were exported to dozens of countries
and produced in thousands of units,
establishing the delta wing
as a practical
and economical combat aircraft configuration.

In Sweden, the [Saab 35 Draken][ref_draken]
introduced the double delta planform
in 1960,
combining a sharply swept inner section
with a moderately swept outer section.
This arrangement improved
low-speed handling
compared to a simple delta
while retaining supersonic performance.
The [Saab 37 Viggen][ref_viggen],
which entered service in 1971,
used a canard-delta configuration
that further improved
short-field performance
and low-speed maneuverability.

The largest operational delta wing aircraft
in history are the [Avro Vulcan][ref_vulcan]
strategic bomber,
which served with the Royal Air Force
from 1956 to 1984,
and the supersonic transports
[Concorde][ref_concorde]
and [Tupolev Tu-144][ref_tu144].
The Concorde, with a wingspan
of 25.6 meters
and a maximum takeoff weight
of 185,000 kilograms,
routinely cruised at Mach 2
while carrying over 100 passengers
across the Atlantic Ocean.
The Concorde demonstrated
that a large delta wing aircraft
could operate reliably
in daily commercial service
for over 27 years.

More recent delta wing designs
include the [Dassault Mirage 2000][ref_mirage_2000],
the [Eurofighter Typhoon][ref_eurofighter],
and the [Saab JAS 39 Gripen][ref_gripen].
These aircraft incorporate
canard surfaces
and digital [fly-by-wire][ref_fly_by_wire] systems
that address the traditional limitations
of the pure delta wing configuration,
including limited low-speed performance
and the inability to generate
trimmed lift at high angles of attack
without significant drag penalties.

### Flying Wing Aircraft

The [flying wing][ref_flying_wing]
is an aircraft configuration
that eliminates the fuselage and tail,
housing all components
within the wing structure.
The concept dates to the earliest days
of powered flight
and has been pursued
intermittently for over a century.

Jack Northrop
was the most persistent advocate
of the flying wing concept
in the United States.
His [N-1M][ref_northrop_n1m] experimental aircraft,
first flown in 1940,
was followed by progressively larger designs
culminating in the
[YB-35][ref_yb35]
and [YB-49][ref_yb49]
flying wing bombers
in the late 1940s.
The YB-49 was a jet-powered derivative
of the propeller-driven YB-35,
with a wingspan of 52.4 meters
and no fuselage or tail.
The program was cancelled in 1949,
and no operational flying wing bomber
entered service
until four decades later.

The [Horten Ho 229][ref_horten_ho229],
developed in Germany during World War II,
was the first jet-powered flying wing
to fly.
The Horten brothers, Walter and Reimar,
designed the aircraft
as a high-speed fighter-bomber.

The flying wing concept
was vindicated
with the development
of the [Northrop Grumman B-2 Spirit][ref_b2],
which first flew in 1989
and entered service in 1997.
The B-2 demonstrated
that fly-by-wire flight control systems
could solve the stability
and control problems
that had defeated earlier flying wing designs.
Its successor,
the [B-21 Raider][ref_b21],
continues the flying wing lineage.

### Reusable Launch Systems

The pursuit of [reusable launch systems][ref_reusable_launch]
has driven aerospace engineering
for over half a century.
The [Space Shuttle][ref_shuttle]
was the first partially reusable
orbital launch system.
The solid rocket boosters
were recovered from the ocean
and refurbished for reuse.
The orbiter itself
was a delta-winged [lifting body][ref_lifting_body]
that glided to a runway landing
after each mission.
However, the external tank
was discarded on every flight,
and the refurbishment costs
far exceeded original projections.

The Soviet [Buran][ref_buran] program
produced a vehicle
aerodynamically similar to the Shuttle orbiter
but designed to be launched
atop an expendable Energia rocket.
Buran completed one uncrewed orbital flight
in November 1988
before the program was cancelled.

The [McDonnell Douglas DC-X][ref_dcx],
first flown in 1993,
demonstrated vertical takeoff
and vertical landing
with a reusable rocket vehicle.
The DC-X was a subscale technology demonstrator
for [single-stage-to-orbit][ref_ssto] concepts,
proving that rapid turnaround
of a rocket-powered vehicle
was achievable with a small ground crew.

The [Lockheed Martin X-33][ref_x33]
was intended to demonstrate
the technologies needed
for a single-stage-to-orbit vehicle
called VentureStar.
The X-33 featured
a lifting body shape,
linear [aerospike engines][ref_aerospike],
and composite fuel tanks.
The program was cancelled in 2001
when the composite liquid hydrogen tank
failed during testing.

[SpaceX Starship][ref_starship]
represents the current state of the art
in reusable launch vehicle development.
Starship is a two-stage,
fully reusable system
in which both the Super Heavy booster
and the Starship upper stage
are designed for propulsive landing and reuse.
The architecture differs fundamentally
from the flying delta wing concept
in that both stages land vertically
rather than aerodynamically,
requiring substantial fuel reserves
for the landing burns.

### Two-Stage-to-Orbit Concepts

The [two-stage-to-orbit][ref_tsto] approach
has been studied extensively
since the 1960s.
The fundamental idea
is to divide the velocity budget
between two reusable vehicles,
each optimized for a different
portion of the flight envelope.

The [Sänger][ref_saenger] concept,
named after the Austrian-German engineer
[Eugen Sänger][ref_eugen_saenger]
whose earlier [Silbervogel][ref_silbervogel]
antipodal bomber concept
had influenced a generation
of hypersonic vehicle designers,
was a German TSTO program
studied during the 1980s and 1990s.
The Sänger system
envisioned a large hypersonic aircraft
powered by turboramjet engines
carrying a smaller orbital vehicle
called HORUS
on its upper surface.
The first stage would accelerate
to approximately Mach 4 to 7,
release the HORUS orbiter,
and return to the launch site.
HORUS would continue to orbit
using rocket propulsion.

The [National Aero-Space Plane][ref_nasp]
program in the United States,
designated X-30,
pursued a more ambitious approach
during the 1980s and early 1990s.
The NASP concept
envisioned an air-breathing vehicle
capable of reaching orbit
using [scramjet][ref_scramjet] propulsion
without the need for a separate first stage.
The program was cancelled in 1993
after aerothermal
and propulsion challenges
proved more difficult
than initial projections suggested.

The British [HOTOL][ref_hotol]
concept from the 1980s
proposed an uncrewed,
horizontal-takeoff,
horizontal-landing spaceplane
powered by an air-breathing engine
that would transition to rocket mode
at high altitude.
HOTOL was cancelled
due to an unfavorable
center of gravity shift
as propellant was consumed.
Its intellectual successor,
[Skylon][ref_skylon],
proposes a more refined design
using the [SABRE][ref_sabre_engine]
precooled air-breathing engine.
SABRE uses a precooler
to chill incoming air
before it enters a turbocompressor,
enabling air-breathing operation
to approximately Mach 5.5
before transitioning to rocket mode.

The [Pegasus][ref_pegasus_rocket] air-launch system,
first flown in 1990,
demonstrated a different form
of two-stage operation.
A carrier aircraft
lifts the Pegasus rocket
to approximately 12 kilometers altitude
and Mach 0.8 before release.
The rocket then ignites
and accelerates to orbital velocity.
[Scaled Composites White Knight][ref_white_knight]
and its successor White Knight Two
carried [SpaceShipTwo][ref_spaceshiptwo]
for suborbital tourist flights,
demonstrating the air-launch concept
for crewed vehicles.

The [Star-Raker][ref_star_raker] concept,
proposed by Rockwell International
in the late 1970s,
envisioned a massive delta wing aircraft
that would take off horizontally,
climb to high altitude
using air-breathing engines,
and then transition to rocket propulsion
for the ascent to orbit.
Star-Raker was designed
to carry 100,000 kilograms of payload
to [low Earth orbit][ref_leo]
using a fleet of vehicles
launched at high frequency.

### Boost-Glide Vehicles

Boost-glide vehicles
represent the earliest conception
of aircraft that travel
through the upper atmosphere
at extreme speeds.
[Eugen Sänger][ref_eugen_saenger] and Irene Bredt
proposed the [Silbervogel][ref_silbervogel]
in 1944
as an antipodal bomber
that would skip off the upper atmosphere
like a stone across water.
The vehicle would be launched
using a rocket-powered sled,
accelerate to over Mach 10,
and then follow a series
of atmospheric skips
to reach targets
at intercontinental range.

The [Boeing X-20 Dyna-Soar][ref_x20],
studied from 1957 to 1963,
would have been the first
piloted orbital boost-glide vehicle.
The X-20 was designed
to launch atop a Titan III rocket,
orbit the Earth,
and glide to a runway landing.
The program was cancelled
before any vehicles were completed,
but its aerodynamic
and thermal protection research
contributed to the Space Shuttle program.

The [North American X-15][ref_x15],
though not a delta wing aircraft,
demonstrated the flight regime
that any boost-glide vehicle must traverse.
The X-15 reached speeds
above Mach 6.7
and altitudes above 100 kilometers,
defining the boundary
between atmospheric flight
and spaceflight.

Modern boost-glide vehicles
include the DARPA
[Falcon Hypersonic Technology Vehicle 2][ref_htv2],
the [Boeing X-51 Waverider][ref_x51],
the Russian [Avangard][ref_avangard] system,
and the Chinese DF-ZF.
These systems demonstrate
that hypersonic glide
at Mach 5 and above
is achievable with current technology,
though all existing systems
are expendable rather than reusable.

### Aerospaceplane Concepts

The [Boeing X-37B][ref_x37b],
discussed in the companion article
[History of Rocketplanes][related_post_rocketplanes],
is the only operational
orbital spaceplane
currently in service.
The X-37B launches vertically,
conducts extended orbital missions
lasting hundreds of days,
and returns to Earth
via a conventional runway landing.

[Dream Chaser][ref_dream_chaser],
developed by Sierra Space,
is a [lifting body][ref_lifting_body] spaceplane
designed for cargo delivery
to the International Space Station.
The European [Hermès][ref_hermes] program
in the 1980s and 1990s
and the Japanese [HOPE-X][ref_hope_x] program
pursued similar crewed spaceplane concepts.
Both were cancelled
before reaching flight status.
The European Space Agency's
[Intermediate eXperimental Vehicle][ref_ixv]
and its successor
[Space Rider][ref_space_rider]
continue the European spaceplane lineage
as uncrewed reentry demonstrators.

### Relationship to the Two-Stage Flying Delta Wing Concept

The proposed two-stage flying delta wing
draws on elements
from each of these historical threads.
It adopts the delta wing planform
validated by over seven decades
of operational experience.
It incorporates the fully reusable philosophy
that has driven launch vehicle development
since the DC-X.
It uses the TSTO staging approach
studied in the Sänger program.
And it applies the boost-glide trajectory
pioneered by the Silbervogel concept.

The distinguishing feature
of the proposed architecture
is geometric integration.
In the Sänger concept,
the orbital stage sat on top
of the first stage
as a separate vehicle.
In Pegasus and White Knight,
the payload vehicle
was carried underneath
or attached externally
to the carrier aircraft.
In the proposed concept,
the two stages are physically merged
into a single aerodynamic shape.
The combined vehicle is a delta wing.
The second stage is a delta wing.
The first stage is a truncated delta wing.
There are no external attachments,
no fairings to jettison,
and no structural elements
that are not integral
to one of the two flyable stages.

## Aerodynamic Characteristics of Delta Wings

### Vortex Lift

The most distinctive aerodynamic feature
of the delta wing
is [vortex lift][ref_vortex_lift].
At moderate to high angles of attack,
the flow separates
from the sharp swept leading edges
and rolls up into
a pair of strong,
conical vortex structures
on the upper surface of the wing.
These leading-edge vortices
create regions of very low pressure
on the upper surface,
generating lift
in addition to the lift
produced by conventional attached flow.

The physics of vortex lift
were first quantified by Polhamus
in 1966
through the leading-edge suction analogy.
In this formulation,
the total lift coefficient $C_L$
of a delta wing
is the sum of two components.

$$C_L = C_{L_p} + C_{L_v}$$

The potential flow component $C_{L_p}$
represents the lift that the wing
would generate
if the flow remained attached.
The vortex lift component $C_{L_v}$
represents the additional lift
generated by the leading-edge vortices.
The vortex lift component
is proportional to $\sin^2 \alpha \cos \alpha$,
where $\alpha$ is the angle of attack.

$$C_{L_v} = K_v \sin^2 \alpha \cos \alpha$$

The coefficient $K_v$
depends on the wing's aspect ratio
and leading-edge sweep angle.
For highly swept delta wings
with aspect ratios below 2,
the vortex lift component
can equal or exceed
the potential flow component
at angles of attack above 15 degrees.

Vortex lift provides
a critical capability
for the two-stage flying delta wing concept.
After separation,
both stages must decelerate
from hypersonic or supersonic speeds
to subsonic landing speeds.
During the final approach and landing,
delta wings fly at high angles of attack,
typically 15 to 25 degrees,
relying on vortex lift
to generate sufficient force
to sustain controlled flight
at low airspeeds.
The [Space Shuttle][ref_shuttle] orbiter
landed at approximately 213 knots
at an angle of attack
of approximately 14 degrees,
demonstrating this characteristic
with a double-delta planform.

### High Angle-of-Attack Performance

Delta wings can sustain
controlled flight at angles of attack
far beyond the stall angle
of conventional rectangular
or moderately swept wings.
A conventional wing
with an aspect ratio of 6 to 8
typically stalls at 14 to 18 degrees
angle of attack.
A delta wing with an aspect ratio of 1.5 to 2
can sustain flight
at angles of attack of 30 degrees or more
before the leading-edge vortices
break down and lift collapses.

This extended angle-of-attack range
is essential for the first stage
of the proposed concept.
After separation at Mach 4 to 6,
the truncated first stage
must decelerate and turn
to return to base.
High angle-of-attack maneuvering
provides both deceleration
and altitude control
during this transition.

### Stability Characteristics

A pure delta wing
without a conventional tail
is inherently unstable
or marginally stable in pitch.
The [center of pressure][ref_center_of_pressure]
of a delta wing
moves aft as the Mach number increases
from subsonic to supersonic speeds.
This shift in the center of pressure
relative to the center of gravity
changes the [static margin][ref_static_margin]
of the aircraft
and requires active flight control
to maintain stable flight.

Modern delta wing aircraft
universally employ
[fly-by-wire][ref_fly_by_wire]
flight control systems
that continuously adjust
control surface deflections
to maintain the desired flight path.
The B-2 Spirit, Eurofighter Typhoon,
and Dassault Rafale
all demonstrate
that fly-by-wire systems
can manage the stability challenges
of tailless or near-tailless configurations
across the full flight envelope.

### Lift-to-Drag Behavior Across the Speed Range

The [lift-to-drag ratio][ref_lift_to_drag]
of a delta wing
varies significantly
with Mach number.
At subsonic speeds,
a delta wing with an aspect ratio of 2
typically achieves a maximum
lift-to-drag ratio of 8 to 10.
This is lower than conventional
high-aspect-ratio wings,
which can achieve ratios of 15 to 20,
but is adequate for approach and landing.

At supersonic speeds
between Mach 1.5 and Mach 3,
the lift-to-drag ratio
of a well-designed delta wing
is typically 4 to 6.
At these speeds,
the delta wing outperforms
most other planform shapes
because its swept leading edges
remain behind the Mach cone,
minimizing wave drag.

At [hypersonic][ref_hypersonic] speeds above Mach 5,
the maximum lift-to-drag ratio
drops further to 2 to 4
for a flat delta wing.
Optimized [waverider][ref_waverider]
configurations
can achieve maximum lift-to-drag ratios
of 5 to 6 at Mach 10
by riding their own shock wave
to generate compression lift.

At hypersonic speeds,
the pressure distribution
approaches Newtonian behavior,
where the pressure coefficient
on a windward surface
is proportional to $\sin^2 \theta$,
with $\theta$ being the angle
between the surface
and the freestream flow direction.

$$C_p = 2 \sin^2 \theta$$

This Newtonian approximation
becomes increasingly accurate
as the Mach number increases
and is useful for preliminary design
of hypersonic delta wing vehicles.

### Advantages in Supersonic and Hypersonic Regimes

Delta wings are attractive
for high-speed flight
for three principal reasons.

The swept leading edges
reduce wave drag at supersonic speeds.
When the leading-edge sweep angle
exceeds the Mach angle
$\mu = \arcsin(1/M)$,
the component of velocity
normal to the leading edge
remains subsonic,
and the wave drag associated
with supersonic flow over the leading edge
is avoided.
For a Mach 4 vehicle,
the Mach angle is approximately 14.5 degrees,
so any leading-edge sweep
above 75.5 degrees
keeps the leading edge subsonic.

The thin, broad shape of a delta wing
distributes thermal loads
over a large surface area.
During hypersonic flight,
the lower surface of the vehicle
absorbs aerodynamic heating
that would be concentrated
along the nose and leading edges
of a conventional slender-body vehicle.
The large surface area
reduces the heating rate
per unit area
and simplifies
the [thermal protection system][ref_tps] design.

The structural simplicity
of the delta wing planform
makes it robust
against the thermal gradients
and mechanical loads
encountered during high-speed flight.
A delta wing has fewer structural joints,
fewer moving parts,
and fewer stress concentration points
than a conventional wing-body-tail configuration.

## Structural and Volume Advantages

### Structural Strength of Triangular Planforms

The triangular shape of a delta wing
provides inherent structural advantages.
The wide root chord
distributes bending loads
over a large area
where the wing structure
reaches maximum depth.
The taper toward the tip
reduces bending moments in the outboard sections.

For a flying delta wing
where the wing is the entire vehicle,
the structural depth is greatest
at the centerline and root,
exactly where bending moments
from aerodynamic loads
are highest.
This natural correspondence
between structural depth
and load intensity
results in an efficient
use of structural material.

### Internal Volume

A delta wing provides
substantially more internal volume
than a conventional slender-body fuselage
of comparable aerodynamic performance.
For a delta wing vehicle
with a span of 40 meters,
a root chord of 60 meters,
and an average thickness-to-chord ratio
of 6 percent,
the internal volume
is approximately 2,880 cubic meters.
A cylindrical fuselage
5 meters in diameter
and 60 meters long
contains only approximately 1,178 cubic meters.

This volume advantage
is critical for the two-stage concept.
The internal volume
must accommodate fuel tanks
for both stages,
payload bays,
propulsion systems,
landing gear,
and all subsystems.
The delta wing's large internal volume
allows these systems to be distributed
across the planform
rather than packed
into a narrow fuselage.

### Load Distribution During High-Speed Flight

During supersonic and hypersonic flight,
the aerodynamic loads
are distributed across the entire planform.
Unlike a conventional aircraft,
where the fuselage carries
concentrated loads
from the wing attachment,
a flying delta wing
distributes loads smoothly
from the leading edges
to the trailing edge.

This distributed loading
reduces peak structural stresses
and allows the structure
to be designed with more uniform
material distribution.

### Integration of Propulsion Systems

The thick root section
of a delta wing
provides ample volume
for embedding propulsion systems
within the wing structure.
Engines can be placed
at the rear of the vehicle,
taking advantage of the trailing edge span
for wide inlet and nozzle arrangements.

For the two-stage concept,
the first stage engines
are located in the aft section
and remain with the first stage
after separation.
The second stage engines
are located in the forward section.
Fuel tanks can be distributed
throughout both sections,
with the separation plane
designed to sever fuel lines
and structural connections cleanly.

## Staging and Vehicle Transformation

### Staging Altitude and Velocity Regimes

The staging conditions
define the boundary
between first-stage and second-stage flight.
For a vehicle designed
to reach [low Earth orbit][ref_leo],
the second stage must provide
sufficient velocity increment
to reach orbital speed
of approximately 7.8 kilometers per second.

If the first stage accelerates
the combined vehicle
to Mach 4 at 25 kilometers altitude,
corresponding to approximately
1.2 kilometers per second,
the second stage must provide
approximately 6.6 kilometers per second
of additional velocity,
accounting for gravity losses
and aerodynamic drag.
If the first stage reaches Mach 6
at 30 kilometers altitude,
corresponding to approximately
1.8 kilometers per second,
the second stage velocity requirement
drops to approximately 6.0 kilometers per second.

For the [Tsiolkovsky rocket equation][ref_rocket_equation],
the mass ratio required
for the second stage
depends exponentially
on the velocity increment
and the effective exhaust velocity
of the propulsion system.

$$\frac{m_0}{m_f} = e^{\Delta v / v_e}$$

Using a liquid hydrogen and liquid oxygen engine
with a [specific impulse][ref_specific_impulse] of 450 seconds
and an effective exhaust velocity
of approximately 4.4 kilometers per second,
a second stage velocity increment
of 6.0 kilometers per second
requires a mass ratio
of approximately 3.9.
This means that approximately
74 percent of the second stage's mass
at separation must be propellant.

### Separation Mechanics

The separation event
is the most critical phase
of the flight.
The second stage must cleanly depart
from the first stage
without aerodynamic interference
or structural contact
that could damage either vehicle.

At supersonic staging conditions,
the two vehicles
interact through their shock wave systems.
The forward vehicle
creates a bow shock
that can impinge
on the aft vehicle.
The aft vehicle creates
its own shock system
that is modified by
proximity to the forward vehicle.
These aerodynamic interactions
create forces and moments
on both vehicles
that change rapidly
as the separation distance increases.

Separation can be achieved
through several mechanisms.
Explosive bolts
or pyrotechnic fasteners
can release the structural connections
between the two stages.
Pneumatic or spring-loaded pushers
can provide initial separation force.
The second stage's own engines
can provide forward acceleration
to increase the separation distance.

NASA has conducted extensive research
on [multi-stage separation aerodynamics][research_nasa_staging]
for winged TSTO configurations,
including wind tunnel testing
at Mach 2.3 through 4.5
of generic wing-body staging events.
Computational fluid dynamics simulations
complement these tests
by modeling the transient shock interactions
that occur during the separation sequence.

### Aerodynamic Interactions During Staging

The aerodynamic interactions
during staging
represent one of the most challenging
aspects of the concept.
At Mach 4 to 6,
the dynamic pressure
is typically 10,000 to 50,000 pascals,
depending on altitude.
At these dynamic pressures,
even small asymmetries
in the aerodynamic forces
during separation
can generate large moments
that must be controlled
by the flight control system.

The [X-43][ref_x43] program
demonstrated the complexity
of hypersonic stage separation
when its Hyper-X Launch Vehicle
separated from a Pegasus booster
at Mach 7 and Mach 10.
Over 580 wind tunnel tests
with 16 models in 10 facilities
were required to develop
the aerodynamic database
for the [X-43 separation event][research_x43_separation].

### Geometry Changes After Separation

After separation,
the geometry of each stage changes
in ways that affect
the center of gravity,
[center of pressure][ref_center_of_pressure],
and control authority.

The second stage
retains the nose
and forward lifting surfaces.
Its center of pressure
is located forward of center,
typical of a delta wing.
Its center of gravity
must be positioned
to provide adequate
[static margin][ref_static_margin]
for stable or controllably unstable flight.

The first stage
loses the forward section
and becomes a truncated planform.
The removal of the nose section
shifts the center of pressure aft.
The center of gravity also shifts,
but the magnitude
depends on the mass distribution
of the remaining structure,
fuel, engines, and systems.
Pre-separation fuel management,
including transferring fuel
between forward and aft tanks
in the first stage,
can position the center of gravity
to ensure adequate stability
for the return flight.

### Control Authority After Separation

Control authority for the combined vehicle
is provided by elevons
along the trailing edge
and possibly by thrust vectoring.
After separation,
the second stage retains
its own elevons
and propulsion-based control.
The first stage retains
the main trailing-edge elevons,
which provide pitch and roll control.

The first stage may deploy
auxiliary control surfaces
that were stowed during the boost phase,
or activate additional drag devices
to enhance yaw control
for the return flight.
Deployable canard surfaces
or nose strakes
could alter the aerodynamic balance
of the truncated first stage,
moving the center of pressure forward
to improve pitch stability.

## First Stage Operations

### Takeoff and Initial Acceleration

The combined vehicle
takes off from a conventional runway
using the first-stage propulsion system.
The takeoff roll
depends on the vehicle's
wing loading and thrust-to-weight ratio.
A large delta wing vehicle
with a wingspan of 40 meters
and a maximum takeoff weight
of 400,000 kilograms
has a wing loading
of approximately 330 kilograms
per square meter,
comparable to the [Concorde][ref_concorde].

### Atmospheric Climb Through Dense Air

After takeoff,
the combined vehicle
climbs through the dense lower atmosphere.
This phase is the most demanding
for the first-stage propulsion system
because aerodynamic drag
is highest at low altitude
and transonic speeds.

If the first stage uses
air-breathing propulsion
such as turbojets
or turbo[ramjet][ref_ramjet] engines,
the climb profile
can be optimized for fuel efficiency
by accelerating gradually
through the transonic regime
and then steepening the climb
as the vehicle reaches supersonic speeds
and drag decreases.

### Propulsion Options for the First Stage

The choice of first-stage propulsion
depends on the desired staging conditions
and the level of technology risk.

Turbojet or turbofan engines
provide efficient propulsion
from takeoff to approximately Mach 2
but cannot operate efficiently
at higher Mach numbers.
Turboramjet or combined-cycle engines
can operate from takeoff
to Mach 4 or beyond
by transitioning from turbojet mode
to [ramjet][ref_ramjet] mode
as the vehicle accelerates.

The [SABRE][ref_sabre_engine] engine concept
represents the most advanced
combined-cycle approach,
using a precooler
to extend air-breathing operation
to approximately Mach 5.5.

Rocket engines provide the simplest
propulsion option
and can operate at any speed or altitude.
However, they carry
both fuel and oxidizer,
resulting in lower
[specific impulse][ref_specific_impulse]
relative to air-breathing engines
that use atmospheric oxygen.

### First-Stage Recovery

After separation,
the first stage
must decelerate from supersonic speeds,
turn back toward the launch site,
and land on a conventional runway.

A powered return uses
the first-stage engines
to fly a controlled trajectory
back to the launch site.
This approach consumes additional fuel
but provides maximum flexibility
in the return trajectory
and landing approach.

A glide return
relies entirely on aerodynamic performance
to bring the first stage back.
The lift-to-drag ratio
of the truncated delta wing
determines the glide range.
At subsonic speeds,
a truncated delta
with carefully managed
center of gravity
can achieve a lift-to-drag ratio
of approximately 6 to 8,
providing a glide range
of 6 to 8 kilometers
for every kilometer of altitude.
From a staging altitude
of 25 kilometers,
this provides a glide range
of 150 to 200 kilometers.

### Landing the Truncated Delta Wing

The truncated first stage
lands like any large delta wing aircraft,
approaching at a high angle of attack
with the nose pitched up
and the vehicle descending
on a steep glide path.
Landing speeds for large delta wings
are typically 140 to 180 knots,
higher than conventional aircraft
due to the high wing loading
and low aspect ratio.

The blunt forward face
of the truncated delta
increases drag during the approach,
which aids landing
by reducing the tendency
of the vehicle to float down the runway.
[Fly-by-wire][ref_fly_by_wire] control
manages the pitch attitude
and descent rate
to achieve a precise
runway touchdown.

## Second Stage Operations

### Mission Modes

The second stage
is a self-contained flying delta wing
capable of multiple mission types.

For orbital insertion,
the second stage
fires its rocket engines
after separation
and accelerates to
[orbital velocity][ref_orbital_mechanics]
of approximately 7.8 kilometers per second.
At orbital altitude,
the engines fire again
for orbital circularization.

For [hypersonic][ref_hypersonic] global transport,
the second stage
does not reach orbital velocity
but instead follows
a suborbital trajectory
that carries it to any point
on the Earth's surface
within approximately 45 to 90 minutes.

For reconnaissance missions,
the second stage
can overfly any point on Earth
at hypersonic speed
at altitudes above 30 kilometers,
where interception
is extremely difficult
with current air defense systems.

### Propulsion Options for the Second Stage

Liquid-fueled rocket engines
provide the highest specific impulse
among chemical propulsion options.
Liquid hydrogen and liquid oxygen engines
achieve [specific impulse][ref_specific_impulse]
of approximately 450 seconds
in vacuum.
Liquid methane and liquid oxygen engines
achieve approximately 360 seconds
and offer simpler handling and storage.

[Scramjet][ref_scramjet] propulsion
could sustain hypersonic cruise
between Mach 5 and Mach 10
using atmospheric oxygen,
but scramjets cannot operate
above the atmosphere.
The [NASA X-43][ref_x43]
demonstrated scramjet propulsion
at Mach 9.6 for approximately 10 seconds
in 2004.
The [Boeing X-51 Waverider][ref_x51]
demonstrated scramjet operation
at Mach 5.1 for 210 seconds in 2013.

### Thermal Protection Requirements

The second stage
experiences extreme heating
during both the ascent
above Mach 5
and the reentry from orbit.
The leading edges of the delta wing
experience the most severe heating
because the small radius of curvature
concentrates the aerodynamic heating.

[Thermal protection systems][ref_tps]
for the second stage
must be reusable
to support the operational concept.
The Space Shuttle used
a combination of reinforced
carbon-carbon for the leading edges,
high-temperature reusable
surface insulation tiles
for the lower surface,
and felt blankets
for the upper surface.

For a delta wing second stage,
the leading edges
may require
[ultra-high-temperature ceramics][ref_uhtc]
such as zirconium diboride
or hafnium diboride,
which can withstand temperatures
above 3,000 kelvin.
The flat lower surface
can use silica-based tiles
or advanced ceramic matrix composites.

### Reentry and Landing

Reentry from orbit
follows a controlled trajectory
that manages heating, deceleration,
and navigational accuracy.
The delta wing shape
provides substantial lift
during reentry,
allowing the vehicle to execute
cross-range maneuvers
of up to several thousand kilometers.
This cross-range capability
enables the vehicle to reach
a landing site
from a variety of orbital inclinations
and positions.

The landing approach
is similar to the Space Shuttle's
approach and landing.
The vehicle descends
on a steep glide path,
using its delta wing
to generate lift at a high angle of attack.
Final approach speed
is typically 150 to 200 knots
depending on wing loading.

## Civil Applications

### Reusable Orbital Launch

A fully reusable two-stage vehicle
could dramatically reduce
the cost of access to orbit.
Current expendable launch systems
cost thousands of dollars per kilogram
to [low Earth orbit][ref_leo].
A fully reusable system
with aircraft-like turnaround times
could reduce costs further
by spreading the vehicle's manufacturing cost
over hundreds or thousands of flights.

The two-stage flying delta wing concept
supports this goal
because neither stage
requires refurbishment
beyond standard aircraft maintenance.
Both stages land on runways,
are inspected and serviced,
refueled, and relaunched.
The operational cadence
could approach that
of airline operations.

### Rapid Global Transport

A two-stage delta wing system
could enable point-to-point
passenger transport
at hypersonic or suborbital speeds.
A vehicle following
a suborbital trajectory
could travel from New York to Tokyo
in approximately 45 minutes,
or from London to Sydney
in approximately 60 minutes.

The first stage
would boost the vehicle
to the staging altitude and velocity,
separate,
and return to the departure airport.
The second stage
would continue on a ballistic
or semi-ballistic trajectory
to the destination,
reenter the atmosphere,
and land on a conventional runway.

[Boom Supersonic][ref_boom_supersonic]
and other companies
are currently developing
supersonic passenger aircraft
that cruise at Mach 1.7 to 2.2.
The two-stage delta wing concept
extends this speed range
to Mach 5 and beyond,
though at significantly greater
technical complexity.

### Space Tourism and Scientific Missions

The reusable second stage
could serve as a platform
for space tourism,
carrying passengers
to suborbital or orbital altitude
and returning them to a runway landing.
The same vehicle
could deliver scientific instruments
to orbit,
service orbital platforms,
or conduct atmospheric
and Earth observation missions.

### Cargo Delivery to Orbit

A large delta wing vehicle
with the internal volume
described in the structural section
could carry substantial cargo
to [low Earth orbit][ref_leo]
or to [geostationary orbit][ref_geostationary]
with appropriate upper stages.
The reusable nature of both stages
would enable frequent launches
at costs competitive with
or lower than existing systems.

## National Security Applications

### Rapid-Response Launch Capability

The two-stage flying delta wing
could provide a military capability
to launch payloads to orbit
on very short notice.
Unlike current launch systems
that require days to weeks
of preparation on a launch pad,
a runway-based reusable system
could be fueled, loaded,
and launched within hours
of a decision to deploy.

This responsiveness
would support missions
such as deploying
replacement satellites
after an adversary
destroys or disables
existing orbital assets,
or placing new sensors
in orbit over a theater
of operations.

### Hypersonic Reconnaissance

The second stage,
operating on a suborbital
or high-hypersonic trajectory,
could overfly any point on Earth
at speeds and altitudes
that make interception
extremely difficult.
The [SR-71 Blackbird][ref_sr71]
demonstrated the value
of high-altitude, high-speed
reconnaissance
during the Cold War.
A hypersonic delta wing
operating at Mach 10 or above
and altitudes above 40 kilometers
would be far more survivable
than the SR-71's Mach 3.2 capability.

### Rapid Global Payload Delivery

The [Prompt Global Strike][ref_prompt_global_strike]
concept envisions the ability
to deliver a conventional weapon
to any point on the globe
within one hour.
The two-stage flying delta wing
could support this concept
by carrying a payload
on a suborbital trajectory.

The critical advantage
of this architecture
over existing boost-glide weapons
such as [Avangard][ref_avangard]
is reusability.
A conventional boost-glide weapon
is an expendable system
that can be used once.
A reusable delta wing vehicle
can be recovered, reloaded,
and relaunched,
providing a sustainable capability
rather than a single-use weapon.

### Operational Flexibility

The two-stage architecture
provides operational flexibility
that single-stage or expendable systems
cannot match.
The first stage can be paired
with different second stages
optimized for different missions.
An orbital insertion second stage,
a hypersonic reconnaissance second stage,
and a cargo delivery second stage
could all be designed
to mate with a common first stage.
This modularity
reduces the total fleet size
and manufacturing cost
while enabling a wider range
of mission profiles.

## Engineering Challenges

### Thermal Protection

Thermal protection
is the most demanding
engineering challenge
for any reusable [hypersonic][ref_hypersonic] vehicle.
The leading edges of the delta wing
experience the most severe heating,
with stagnation temperatures
that can exceed
the melting points
of most structural materials.

The Space Shuttle's
[thermal protection system][ref_tps]
required extensive inspection
and tile replacement
after every flight,
contributing significantly
to the Shuttle's high turnaround cost.
A two-stage flying delta wing
designed for rapid reuse
would require TPS materials
and designs
that tolerate repeated thermal cycles
without degradation.

[Ultra-high-temperature ceramics][ref_uhtc]
such as zirconium diboride
and hafnium diboride
can withstand temperatures above 3,000 kelvin.
Ceramic matrix composites
offer a combination
of thermal resistance
and structural capability.

### Propulsion Integration

Integrating propulsion systems
for both stages
within a single airframe
presents significant packaging challenges.
The first stage
may use air-breathing engines
with large inlets and nozzles.
The second stage
uses rocket engines
with propellant tanks
and associated plumbing.
Both propulsion systems
must be physically separate
and independently functional
after staging.

### Structural Loads During Staging

The staging event
imposes transient structural loads
on both vehicles
as the aerodynamic configuration
changes rapidly.
The separation hardware
must release cleanly
without creating debris
that could damage either vehicle.
The structural connections
between the two stages
must be strong enough
to carry flight loads
during the boost phase
but release completely
and reliably during staging.

### Control Across Wide Flight Regimes

The combined vehicle
and both individual stages
must maintain controlled flight
across a speed range
from approximately 60 meters per second
at takeoff and landing
to potentially 7,800 meters per second
for orbital insertion.
This speed range spans
four orders of magnitude in dynamic pressure
and requires control systems
that function in
subsonic, transonic, supersonic,
and hypersonic regimes.

Aerodynamic control surfaces
are effective at dynamic pressures
above approximately 500 pascals.
At orbital altitudes
where dynamic pressure approaches zero,
reaction control thrusters
provide attitude control.

### Stability of the Truncated First-Stage Configuration

The truncated delta wing
of the first stage
presents unique stability challenges.
The loss of the nose section
moves the center of pressure aft,
and the center of gravity also moves aft
because the forward section
that separated
carried some of the vehicle's mass.
The relative movement
of these two reference points
determines whether the first stage
is more or less stable
after separation.

Research on [clipped delta wing aerodynamics][research_clipped_delta]
has demonstrated that truncated planforms
retain controllable flight characteristics
when equipped with appropriate
control surface configurations,
though the aerodynamic efficiency
is reduced compared to the full delta.

### Landing Performance of Large Delta Wings

Large delta wing vehicles
have high wing loading
and relatively low lift-to-drag ratios
at landing speeds.
The [Concorde][ref_concorde],
with a wing loading
of approximately 410 kilograms per square meter,
landed at approximately 165 knots
with the nose drooped
to provide pilot visibility.

A two-stage delta wing vehicle
with similar wing loading
would require landing speeds
in the same range.
If the first or second stage
retains propulsive capability
for its return,
a go-around capability
could be provided,
significantly improving
operational safety.

### Manufacturing Complexity

A two-stage vehicle
that integrates seamlessly
into a single aerodynamic shape
requires high-precision manufacturing
of the interface between the two stages.
The separation plane
must be aerodynamically smooth
when the vehicle is assembled,
structurally sound
during flight loads,
and capable of clean release
during staging.

The vehicle's thermal protection system
must span both stages
without gaps or discontinuities
at the interface.
After separation,
both stages must present
aerodynamically clean surfaces
at their new forward and aft faces.

## Future Development Paths

### Scaled-Up Heavy-Lift Variants

The two-stage flying delta wing concept
can be scaled up
to create heavy-lift vehicles
capable of delivering
tens of thousands of kilograms
to orbit.
A vehicle with a wingspan of 80 meters
and a maximum takeoff weight
exceeding 1,000,000 kilograms
would provide payload capacity
comparable to or exceeding
existing heavy-lift rockets.

The [Star-Raker][ref_star_raker] concept
from the 1970s
envisioned exactly this kind
of large-scale delta wing vehicle
for routine heavy-lift access to orbit.

### Smaller Tactical Variants

The concept
can be scaled down
to create smaller vehicles
for tactical applications.
A vehicle with a wingspan of 15 meters
and a maximum takeoff weight
of 20,000 kilograms
could serve as an
autonomous or remotely piloted
system for rapid payload delivery,
hypersonic reconnaissance,
or small satellite launch.

### Autonomous and Remotely Piloted Vehicles

The operational concept
is well suited to autonomous flight.
The [X-37B][ref_x37b]
has demonstrated
that orbital spaceplanes
can operate autonomously
for extended periods.

Both stages of the two-stage concept
could operate autonomously,
with the first stage
returning to base and landing
under automated control
and the second stage
conducting its mission
and returning autonomously.

### Advanced Propulsion Systems

Future propulsion technologies
could significantly improve
the performance
of the two-stage concept.

The [SABRE][ref_sabre_engine] precooled engine
could enable an air-breathing first stage
that operates from takeoff
to Mach 5.5,
reducing the velocity requirement
for the second stage.

Rotating detonation engines,
which generate thrust through
a continuous detonation wave
rather than the deflagration
used in conventional engines,
promise higher thermodynamic efficiency
and could improve specific impulse
for both stages.

### Advanced Materials

Improvements in materials
will directly benefit
the two-stage concept.
Carbon fiber and silicon carbide composites
reduce structural weight
while maintaining strength
at high temperatures.
Ultra-high-temperature ceramic composites
could enable leading-edge structures
that withstand reentry temperatures
without the maintenance burden
of the Shuttle's TPS tiles.

## Conclusion

The two-stage flying delta wing vehicle
represents a geometrically elegant approach
to fully reusable access to orbit
and hypersonic flight.
The concept exploits
a fundamental property
of the delta wing planform.
A large delta wing
can be divided along a lateral plane
into a forward section
that is itself a complete delta wing
and an aft section
that is a truncated delta wing
capable of independent flight.

This geometric property
enables a vehicle architecture
in which no hardware is expended.
The combined vehicle
takes off as a single delta wing.
After the first stage
has accelerated
through the dense lower atmosphere,
the second stage separates
and continues to orbit
or to its hypersonic mission.
The first stage returns to base
and lands on a runway.
Both stages are inspected,
serviced, refueled,
and flown again.

The concept builds
on over seven decades
of delta wing flight experience
from the [Convair XF-92A][ref_xf92]
in 1948
to the [B-21 Raider][ref_b21]
and [Saab JAS 39 Gripen][ref_gripen]
of the 2020s.
It incorporates lessons
from [TSTO][ref_tsto] studies
including the [Sänger][ref_saenger] program,
boost-glide research
from the [Silbervogel][ref_silbervogel]
through the [X-51][ref_x51],
and operational spaceplane experience
from the [Space Shuttle][ref_shuttle]
through the [X-37B][ref_x37b].

The engineering challenges
are significant.
Thermal protection for leading edges
and lower surfaces
must be both effective and reusable.
Propulsion must operate efficiently
across the full speed range.
The staging event
imposes unique aerodynamic
and structural demands.
The truncated first stage
requires careful aerodynamic design
and active control
to fly safely back to base.

Civil applications
include reusable orbital launch
with costs potentially approaching
those of airline operations,
rapid global transport
in under 90 minutes,
and space tourism.
National security applications
include responsive space access,
hypersonic reconnaissance,
and global payload delivery
with the sustainability
that only a reusable system
can provide.

Both stages remain viable aircraft
at all times during and after the mission.
This property distinguishes
the two-stage flying delta wing
from every existing
or previously proposed
reusable launch system.
It is the foundation
of the concept's reusability,
its operational flexibility,
and its potential
to transform access to orbit
from an expendable rocket operation
to an aircraft-like operation.

## Future Reading

- [Fundamentals of Aerodynamics by John D. Anderson][future_anderson],
  a comprehensive treatment
  of subsonic, supersonic,
  and hypersonic aerodynamics
  including delta wing theory
  and vortex lift.

- [Hypersonic and High-Temperature Gas Dynamics by John D. Anderson][future_anderson_hypersonic],
  the standard reference
  for hypersonic vehicle aerothermodynamics
  covering inviscid flow, viscous flow,
  and high-temperature gas effects.

- [Aircraft Design: A Conceptual Approach by Daniel Raymer][future_raymer],
  a widely used reference
  for aircraft configuration design
  including flying wings,
  tailless configurations,
  and launch vehicle design methodology.

- [Hypersonic Airbreathing Propulsion by William Heiser and David Pratt][future_heiser],
  a detailed treatment
  of scramjet, ramjet,
  and combined-cycle engine design
  for hypersonic vehicles.

- [The Hypersonic Revolution edited by Richard Hallion][future_hallion],
  a three-volume NASA history
  covering the development
  of hypersonic flight technology
  from the X-15 through NASP.

- [The Aerodynamic Design of Aircraft by Dietrich Kuchemann][future_kuchemann],
  a classic text
  by the scientist
  whose slender delta wing research
  directly influenced Concorde design,
  covering classical, slender-wing,
  and waverider aircraft.

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Non-Peer-Reviewed

- Buning, Pieter G., Tin-Chee Wong, Arthur D. Dilley, and Jenn L. Pao. 2000. *Prediction of Hyper-X Stage Separation Aerodynamics Using CFD*. AIAA Paper 2000-4009. NASA Langley Research Center. [https://ntrs.nasa.gov/citations/20000091005][research_x43_separation]
- Erickson, Gary E. 2020. *Wind Tunnel Investigation of the Supersonic Stage Separation Aerodynamics of a Generic 0.0175-Scale Bimese Two-Stage-to-Orbit Reusable Launch Vehicle Configuration*. NASA/TM–2020-220582. NASA. [https://ntrs.nasa.gov/citations/20200002873][research_nasa_staging]
- Hernandez, Gloria, Richard M. Wood, and Peter F. Covell. 1994. *Effect of Leading- and Trailing-Edge Flaps on Clipped Delta Wings with and without Wing Camber at Supersonic Speeds*. NASA-TM-4542. NASA. [https://ntrs.nasa.gov/citations/19950003616][research_clipped_delta]
- *The Hypersonic Revolution edited by Hallion*. n.d. [https://ntrs.nasa.gov/citations/19980169782][future_hallion]
- Polhamus, E. C. 1966. *A Concept of the Vortex Lift of Sharp-Edge Delta Wings Based on a Leading-Edge-Suction Analogy*. NASA-TN-D-3767. NASA. [https://ntrs.nasa.gov/citations/19670003842][research_polhamus]

### Secondary Sources

- Anderson, John, and Chris Cadou. 2023. *Fundamentals of Aerodynamics*. McGraw-Hill Education. [https://www.mheducation.com/highered/product/fundamentals-aerodynamics-anderson/M9781264151929.html][future_anderson]
- Heiser, William, David Pratt, Daniel Daley, and Unmeel Mehta. 1994. *Hypersonic Airbreathing Propulsion*. American Institute of Aeronautics and Astronautics, Inc. [https://doi.org/10.2514/4.470356][future_heiser]
- Küchemann, Dietrich. 2012. *The Aerodynamic Design of Aircraft*. American Institute of Aeronautics and Astronautics, Inc. [https://doi.org/10.2514/4.869228][future_kuchemann]

### General Sources

- "Aircraft Design: A Conceptual Approach, Sixth Edition." n.d. AIAA Education Series. Accessed October 25, 2026. [https://arc.aiaa.org/doi/book/10.2514/4.104909][future_raymer]
- "Future Reading, Hypersonic and High-Temperature Gas Dynamics by Anderson." n.d. Accessed October 25, 2026. [https://arc.aiaa.org/doi/book/10.2514/4.105142][future_anderson_hypersonic]
- "Sänger Spaceplane Concept." n.d. Accessed October 25, 2026. [https://en.wikipedia.org/wiki/S%C3%A4nger\_II][ref_saenger]

### Tertiary Sources

- "Aerospike Engine." 2026. Wikipedia. Last modified February 4, at 01:50 (UTC). [https://en.wikipedia.org/w/index.php?title=Aerospike\_engine&oldid=1336484721][ref_aerospike]
- "Alexander Lippisch." 2026. Wikipedia. Last modified January 29, at 18:40 (UTC). [https://en.wikipedia.org/w/index.php?title=Alexander\_Lippisch&oldid=1335526007][ref_lippisch]
- "Atmospheric Entry." 2026. Wikipedia. Last modified February 23, at 00:48 (UTC). [https://en.wikipedia.org/w/index.php?title=Atmospheric\_entry&oldid=1339928327][ref_tps]
- "Avangard (Hypersonic Glide Vehicle)." 2026. Wikipedia. Last modified January 9, at 17:47 (UTC). [https://en.wikipedia.org/w/index.php?title=Avangard\_(hypersonic\_glide\_vehicle)&oldid=1332060777][ref_avangard]
- "Avro Vulcan." 2026. Wikipedia. Last modified January 31, at 11:10 (UTC). [https://en.wikipedia.org/w/index.php?title=Avro\_Vulcan&oldid=1335821152][ref_vulcan]
- "Blended Wing Body." 2026. Wikipedia. Last modified January 16, at 20:14 (UTC). [https://en.wikipedia.org/w/index.php?title=Blended\_wing\_body&oldid=1333280539][ref_blended_wing_body]
- "Boeing X-20 Dyna-Soar." 2026. Wikipedia. Last modified January 19, at 13:02 (UTC). [https://en.wikipedia.org/w/index.php?title=Boeing\_X-20\_Dyna-Soar&oldid=1333734859][ref_x20]
- "Boeing X-37." 2026. Wikipedia. Last modified February 18, at 01:58 (UTC). [https://en.wikipedia.org/w/index.php?title=Boeing\_X-37&oldid=1338933184][ref_x37b]
- "Boeing X-48." 2025. Wikipedia. Last modified November 11, at 14:49 (UTC). [https://en.wikipedia.org/w/index.php?title=Boeing\_X-48&oldid=1321603411][ref_x48]
- "Boeing X-51 Waverider." 2025. Wikipedia. Last modified April 5, at 07:29 (UTC). [https://en.wikipedia.org/w/index.php?title=Boeing\_X-51\_Waverider&oldid=1284050871][ref_x51]
- "Boom Technology." 2026. Wikipedia. Last modified January 24, at 10:17 (UTC). [https://en.wikipedia.org/w/index.php?title=Boom\_Technology&oldid=1334573387][ref_boom_supersonic]
- "British Aerospace HOTOL." 2025. Wikipedia. Last modified October 16, at 13:57 (UTC). [https://en.wikipedia.org/w/index.php?title=British\_Aerospace\_HOTOL&oldid=1317125891][ref_hotol]
- "Buran Programme." 2026. Wikipedia. Last modified March 2, at 17:41 (UTC). [https://en.wikipedia.org/w/index.php?title=Buran\_programme&oldid=1341339612][ref_buran]
- "Center of Pressure (Fluid Mechanics)." 2026. Wikipedia. Last modified March 3, at 13:45 (UTC). [https://en.wikipedia.org/w/index.php?title=Center\_of\_pressure\_(fluid\_mechanics)&oldid=1341492354][ref_center_of_pressure]
- "Concorde." 2026. Wikipedia. Last modified March 4, at 17:54 (UTC). [https://en.wikipedia.org/w/index.php?title=Concorde&oldid=1341721440][ref_concorde]
- "Convair B-58 Hustler." 2026. Wikipedia. Last modified February 25, at 07:37 (UTC). [https://en.wikipedia.org/w/index.php?title=Convair\_B-58\_Hustler&oldid=1340362074][ref_b58]
- "Convair F-102 Delta Dagger." 2026. Wikipedia. Last modified February 10, at 19:20 (UTC). [https://en.wikipedia.org/w/index.php?title=Convair\_F-102\_Delta\_Dagger&oldid=1337659517][ref_f102]
- "Convair F-106 Delta Dart." 2026. Wikipedia. Last modified February 28, at 17:29 (UTC). [https://en.wikipedia.org/w/index.php?title=Convair\_F-106\_Delta\_Dart&oldid=1340946781][ref_f106]
- "Convair XF-92." 2025. Wikipedia. Last modified September 28, at 08:42 (UTC). [https://en.wikipedia.org/w/index.php?title=Convair\_XF-92&oldid=1313820428][ref_xf92]
- "Conventional Prompt Strike." 2026. Wikipedia. Last modified February 10, at 19:44 (UTC). [https://en.wikipedia.org/w/index.php?title=Conventional\_Prompt\_Strike&oldid=1337663060][ref_prompt_global_strike]
- "Dassault Mirage 2000." 2026. Wikipedia. Last modified February 26, at 11:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Dassault\_Mirage\_2000&oldid=1340565501][ref_mirage_2000]
- "Dassault Mirage III." 2026. Wikipedia. Last modified February 28, at 12:57 (UTC). [https://en.wikipedia.org/w/index.php?title=Dassault\_Mirage\_III&oldid=1340917756][ref_mirage_iii]
- "Delta Wing." 2026. Wikipedia. Last modified February 18, at 11:20 (UTC). [https://en.wikipedia.org/w/index.php?title=Delta\_wing&oldid=1338994076][ref_delta_wing]
- "Dream Chaser." 2026. Wikipedia. Last modified February 23, at 23:42 (UTC). [https://en.wikipedia.org/w/index.php?title=Dream\_Chaser&oldid=1340098458][ref_dream_chaser]
- "Eugen Sänger." 2026. Wikipedia. Last modified February 13, at 14:46 (UTC). [https://en.wikipedia.org/w/index.php?title=Eugen\_S%C3%A4nger&oldid=1338156361][ref_eugen_saenger]
- "Eurofighter Typhoon." 2026. Wikipedia. Last modified March 2, at 19:48 (UTC). [https://en.wikipedia.org/w/index.php?title=Eurofighter\_Typhoon&oldid=1341356857][ref_eurofighter]
- "Fly-by-Wire." 2026. Wikipedia. Last modified January 21, at 07:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Fly-by-wire&oldid=1334056316][ref_fly_by_wire]
- "Flying Wing." 2026. Wikipedia. Last modified February 15, at 01:41 (UTC). [https://en.wikipedia.org/w/index.php?title=Flying\_wing&oldid=1338420107][ref_flying_wing]
- "Geostationary Orbit." 2026. Wikipedia. Last modified February 2, at 10:20 (UTC). [https://en.wikipedia.org/w/index.php?title=Geostationary\_orbit&oldid=1336184288][ref_geostationary]
- "Hermes (Spacecraft)." 2026. Wikipedia. Last modified February 13, at 04:24 (UTC). [https://en.wikipedia.org/w/index.php?title=Hermes\_(spacecraft)&oldid=1338088790][ref_hermes]
- "HOPE-X." 2024. Wikipedia. Last modified July 4, at 16:40 (UTC). [https://en.wikipedia.org/w/index.php?title=HOPE-X&oldid=1232608569][ref_hope_x]
- "Horten Ho 229." 2026. Wikipedia. Last modified January 1, at 20:05 (UTC). [https://en.wikipedia.org/w/index.php?title=Horten\_Ho\_229&oldid=1330665254][ref_horten_ho229]
- "Hypersonic Speed." 2026. Wikipedia. Last modified January 21, at 02:00 (UTC). [https://en.wikipedia.org/w/index.php?title=Hypersonic\_speed&oldid=1334016208][ref_hypersonic]
- "Hypersonic Technology Vehicle 2." 2026. Wikipedia. Last modified January 16, at 18:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Hypersonic\_Technology\_Vehicle\_2&oldid=1333268437][ref_htv2]
- "Intermediate eXperimental Vehicle." 2026. Wikipedia. Last modified January 18, at 10:40 (UTC). [https://en.wikipedia.org/w/index.php?title=Intermediate\_eXperimental\_Vehicle&oldid=1333535954][ref_ixv]
- "Lift-to-Drag Ratio." 2025. Wikipedia. Last modified October 2, at 10:41 (UTC). [https://en.wikipedia.org/w/index.php?title=Lift-to-drag\_ratio&oldid=1314615335][ref_lift_to_drag]
- "Lifting Body." 2026. Wikipedia. Last modified January 28, at 02:43 (UTC). [https://en.wikipedia.org/w/index.php?title=Lifting\_body&oldid=1335230534][ref_lifting_body]
- "Lockheed Martin X-33." 2026. Wikipedia. Last modified February 10, at 18:59 (UTC). [https://en.wikipedia.org/w/index.php?title=Lockheed\_Martin\_X-33&oldid=1337656265][ref_x33]
- "Lockheed SR-71 Blackbird." 2026. Wikipedia. Last modified February 26, at 06:27 (UTC). [https://en.wikipedia.org/w/index.php?title=Lockheed\_SR-71\_Blackbird&oldid=1340534278][ref_sr71]
- "Longitudinal Stability." 2026. Wikipedia. Last modified January 23, at 15:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Longitudinal\_stability&oldid=1334439692][ref_static_margin]
- "Low Earth Orbit." 2026. Wikipedia. Last modified February 24, at 03:26 (UTC). [https://en.wikipedia.org/w/index.php?title=Low\_Earth\_orbit&oldid=1340136028][ref_leo]
- "Mach Number." 2026. Wikipedia. Last modified March 3, at 17:18 (UTC). [https://en.wikipedia.org/w/index.php?title=Mach\_number&oldid=1341518938][ref_mach_number]
- "McDonnell Douglas DC-X." 2026. Wikipedia. Last modified February 19, at 15:38 (UTC). [https://en.wikipedia.org/w/index.php?title=McDonnell\_Douglas\_DC-X&oldid=1339220640][ref_dcx]
- "Messerschmitt Me 163 Komet." 2025. Wikipedia. Last modified December 19, at 14:47 (UTC). [https://en.wikipedia.org/w/index.php?title=Messerschmitt\_Me\_163\_Komet&oldid=1328380694][ref_me_163]
- "NASA X-43." 2026. Wikipedia. Last modified January 12, at 19:46 (UTC). [https://en.wikipedia.org/w/index.php?title=NASA\_X-43&oldid=1332600803][ref_x43]
- "North American X-15." 2026. Wikipedia. Last modified March 1, at 14:00 (UTC). [https://en.wikipedia.org/w/index.php?title=North\_American\_X-15&oldid=1341109634][ref_x15]
- "Northrop B-2 Spirit." 2026. Wikipedia. Last modified March 2, at 20:04 (UTC). [https://en.wikipedia.org/w/index.php?title=Northrop\_B-2\_Spirit&oldid=1341359106][ref_b2]
- "Northrop Grumman B-21 Raider." 2026. Wikipedia. Last modified March 4, at 02:44 (UTC). [https://en.wikipedia.org/w/index.php?title=Northrop\_Grumman\_B-21\_Raider&oldid=1341610591][ref_b21]
- "Northrop Grumman Pegasus." 2026. Wikipedia. Last modified January 23, at 18:27 (UTC). [https://en.wikipedia.org/w/index.php?title=Northrop\_Grumman\_Pegasus&oldid=1334464796][ref_pegasus_rocket]
- "Northrop Grumman X-47B." 2026. Wikipedia. Last modified February 24, at 22:43 (UTC). [https://en.wikipedia.org/w/index.php?title=Northrop\_Grumman\_X-47B&oldid=1340289892][ref_x47b]
- "Northrop N-1M." 2025. Wikipedia. Last modified June 28, at 23:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Northrop\_N-1M&oldid=1297859500][ref_northrop_n1m]
- "Northrop YB-35." 2025. Wikipedia. Last modified November 26, at 15:21 (UTC). [https://en.wikipedia.org/w/index.php?title=Northrop\_YB-35&oldid=1324258308][ref_yb35]
- "Northrop YB-49." 2026. Wikipedia. Last modified January 9, at 15:30 (UTC). [https://en.wikipedia.org/w/index.php?title=Northrop\_YB-49&oldid=1332041135][ref_yb49]
- "Operation Paperclip." 2026. Wikipedia. Last modified March 4, at 07:36 (UTC). [https://en.wikipedia.org/w/index.php?title=Operation\_Paperclip&oldid=1341653153][ref_paperclip]
- "Orbital Mechanics." 2026. Wikipedia. Last modified February 18, at 07:26 (UTC). [https://en.wikipedia.org/w/index.php?title=Orbital\_mechanics&oldid=1338973693][ref_orbital_mechanics]
- "Ramjet." 2026. Wikipedia. Last modified February 22, at 14:29 (UTC). [https://en.wikipedia.org/w/index.php?title=Ramjet&oldid=1339824211][ref_ramjet]
- "Reusable Launch Vehicle." 2026. Wikipedia. Last modified February 27, at 10:06 (UTC). [https://en.wikipedia.org/w/index.php?title=Reusable\_launch\_vehicle&oldid=1340738453][ref_reusable_launch]
- "Rockwell X-30." 2026. Wikipedia. Last modified January 28, at 05:42 (UTC). [https://en.wikipedia.org/w/index.php?title=Rockwell\_X-30&oldid=1335251084][ref_nasp]
- "Saab 35 Draken." 2026. Wikipedia. Last modified February 20, at 18:44 (UTC). [https://en.wikipedia.org/w/index.php?title=Saab\_35\_Draken&oldid=1339468913][ref_draken]
- "Saab 37 Viggen." 2026. Wikipedia. Last modified January 19, at 22:44 (UTC). [https://en.wikipedia.org/w/index.php?title=Saab\_37\_Viggen&oldid=1333817905][ref_viggen]
- "Saab JAS 39 Gripen." 2026. Wikipedia. Last modified February 24, at 04:34 (UTC). [https://en.wikipedia.org/w/index.php?title=Saab\_JAS\_39\_Gripen&oldid=1340146529][ref_gripen]
- "SABRE (Rocket Engine)." 2026. Wikipedia. Last modified March 4, at 08:28 (UTC). [https://en.wikipedia.org/w/index.php?title=SABRE\_(rocket\_engine)&oldid=1341657292][ref_sabre_engine]
- "Scaled Composites White Knight." 2025. Wikipedia. Last modified October 25, at 10:56 (UTC). [https://en.wikipedia.org/w/index.php?title=Scaled\_Composites\_White\_Knight&oldid=1318685091][ref_white_knight]
- "Scramjet." 2026. Wikipedia. Last modified February 3, at 16:24 (UTC). [https://en.wikipedia.org/w/index.php?title=Scramjet&oldid=1336403495][ref_scramjet]
- "Silbervogel." 2025. Wikipedia. Last modified October 11, at 07:02 (UTC). [https://en.wikipedia.org/w/index.php?title=Silbervogel&oldid=1316237133][ref_silbervogel]
- "Single-Stage-to-Orbit." 2026. Wikipedia. Last modified February 12, at 20:17 (UTC). [https://en.wikipedia.org/w/index.php?title=Single-stage-to-orbit&oldid=1338027163][ref_ssto]
- "Skylon (Spacecraft)." 2026. Wikipedia. Last modified January 25, at 08:27 (UTC). [https://en.wikipedia.org/w/index.php?title=Skylon\_(spacecraft)&oldid=1334726586][ref_skylon]
- "Space Rider." 2026. Wikipedia. Last modified February 23, at 22:15 (UTC). [https://en.wikipedia.org/w/index.php?title=Space\_Rider&oldid=1340087982][ref_space_rider]
- "Space Shuttle Program." 2026. Wikipedia. Last modified January 19, at 14:36 (UTC). [https://en.wikipedia.org/w/index.php?title=Space\_Shuttle\_program&oldid=1333744633][ref_shuttle]
- "SpaceShipTwo." 2026. Wikipedia. Last modified February 15, at 18:09 (UTC). [https://en.wikipedia.org/w/index.php?title=SpaceShipTwo&oldid=1338526105][ref_spaceshiptwo]
- "SpaceX Starship." 2026. Wikipedia. Last modified March 4, at 17:51 (UTC). [https://en.wikipedia.org/w/index.php?title=SpaceX\_Starship&oldid=1341721181][ref_starship]
- "Specific Impulse." 2026. Wikipedia. Last modified February 27, at 21:49 (UTC). [https://en.wikipedia.org/w/index.php?title=Specific\_impulse&oldid=1340816504][ref_specific_impulse]
- "Swept Wing." 2025. Wikipedia. Last modified December 22, at 03:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Swept\_wing&oldid=1328845509][ref_swept_wing]
- "Tsiolkovsky Rocket Equation." 2026. Wikipedia. Last modified February 19, at 19:50 (UTC). [https://en.wikipedia.org/w/index.php?title=Tsiolkovsky\_rocket\_equation&oldid=1339265602][ref_rocket_equation]
- "Tupolev Tu-144." 2026. Wikipedia. Last modified March 4, at 16:35 (UTC). [https://en.wikipedia.org/w/index.php?title=Tupolev\_Tu-144&oldid=1341710676][ref_tu144]
- "Two-Stage-to-Orbit." 2025. Wikipedia. Last modified December 3, at 16:57 (UTC). [https://en.wikipedia.org/w/index.php?title=Two-stage-to-orbit&oldid=1325537168][ref_tsto]
- "Ultra-High Temperature Ceramic." 2026. Wikipedia. Last modified February 27, at 01:46 (UTC). [https://en.wikipedia.org/w/index.php?title=Ultra-high\_temperature\_ceramic&oldid=1340676888][ref_uhtc]
- "Vortex Lift." 2025. Wikipedia. Last modified September 1, at 19:10 (UTC). [https://en.wikipedia.org/w/index.php?title=Vortex\_lift&oldid=1309024110][ref_vortex_lift]
- "Waverider." 2025. Wikipedia. Last modified September 16, at 02:42 (UTC). [https://en.wikipedia.org/w/index.php?title=Waverider&oldid=1311620728][ref_waverider]

### Related Posts

- Sechter, Brendan. 2026. "Introduction to Space Studies." *Brendan A R Sechter's Development Blog*, February 21. [https://sgeos.github.io/space/math/2026/02/21/introduction\_to\_space\_studies.html][related_post_space_studies]
- Sechter, Brendan. 2026. "History of Rocketplanes." *Brendan A R Sechter's Development Blog*, February 27. [https://sgeos.github.io/space/history/2026/02/27/history\_of\_rocketplanes.html][related_post_rocketplanes]

[future_anderson]: https://www.mheducation.com/highered/product/fundamentals-aerodynamics-anderson/M9781264151929.html
[future_anderson_hypersonic]: https://arc.aiaa.org/doi/book/10.2514/4.105142
[future_hallion]: https://ntrs.nasa.gov/citations/19980169782
[future_heiser]: https://doi.org/10.2514/4.470356
[future_kuchemann]: https://doi.org/10.2514/4.869228
[future_raymer]: https://arc.aiaa.org/doi/book/10.2514/4.104909
[ref_aerospike]: https://en.wikipedia.org/w/index.php?title=Aerospike_engine&oldid=1336484721
[ref_avangard]: https://en.wikipedia.org/w/index.php?title=Avangard_(hypersonic_glide_vehicle)&oldid=1332060777
[ref_b2]: https://en.wikipedia.org/w/index.php?title=Northrop_B-2_Spirit&oldid=1341359106
[ref_b21]: https://en.wikipedia.org/w/index.php?title=Northrop_Grumman_B-21_Raider&oldid=1341610591
[ref_b58]: https://en.wikipedia.org/w/index.php?title=Convair_B-58_Hustler&oldid=1340362074
[ref_blended_wing_body]: https://en.wikipedia.org/w/index.php?title=Blended_wing_body&oldid=1333280539
[ref_boom_supersonic]: https://en.wikipedia.org/w/index.php?title=Boom_Technology&oldid=1334573387
[ref_buran]: https://en.wikipedia.org/w/index.php?title=Buran_programme&oldid=1341339612
[ref_center_of_pressure]: https://en.wikipedia.org/w/index.php?title=Center_of_pressure_(fluid_mechanics)&oldid=1341492354
[ref_concorde]: https://en.wikipedia.org/w/index.php?title=Concorde&oldid=1341721440
[ref_dcx]: https://en.wikipedia.org/w/index.php?title=McDonnell_Douglas_DC-X&oldid=1339220640
[ref_delta_wing]: https://en.wikipedia.org/w/index.php?title=Delta_wing&oldid=1338994076
[ref_draken]: https://en.wikipedia.org/w/index.php?title=Saab_35_Draken&oldid=1339468913
[ref_dream_chaser]: https://en.wikipedia.org/w/index.php?title=Dream_Chaser&oldid=1340098458
[ref_eugen_saenger]: https://en.wikipedia.org/w/index.php?title=Eugen_S%C3%A4nger&oldid=1338156361
[ref_eurofighter]: https://en.wikipedia.org/w/index.php?title=Eurofighter_Typhoon&oldid=1341356857
[ref_f102]: https://en.wikipedia.org/w/index.php?title=Convair_F-102_Delta_Dagger&oldid=1337659517
[ref_f106]: https://en.wikipedia.org/w/index.php?title=Convair_F-106_Delta_Dart&oldid=1340946781
[ref_fly_by_wire]: https://en.wikipedia.org/w/index.php?title=Fly-by-wire&oldid=1334056316
[ref_flying_wing]: https://en.wikipedia.org/w/index.php?title=Flying_wing&oldid=1338420107
[ref_geostationary]: https://en.wikipedia.org/w/index.php?title=Geostationary_orbit&oldid=1336184288
[ref_gripen]: https://en.wikipedia.org/w/index.php?title=Saab_JAS_39_Gripen&oldid=1340146529
[ref_hermes]: https://en.wikipedia.org/w/index.php?title=Hermes_(spacecraft)&oldid=1338088790
[ref_hope_x]: https://en.wikipedia.org/w/index.php?title=HOPE-X&oldid=1232608569
[ref_horten_ho229]: https://en.wikipedia.org/w/index.php?title=Horten_Ho_229&oldid=1330665254
[ref_hotol]: https://en.wikipedia.org/w/index.php?title=British_Aerospace_HOTOL&oldid=1317125891
[ref_htv2]: https://en.wikipedia.org/w/index.php?title=Hypersonic_Technology_Vehicle_2&oldid=1333268437
[ref_hypersonic]: https://en.wikipedia.org/w/index.php?title=Hypersonic_speed&oldid=1334016208
[ref_ixv]: https://en.wikipedia.org/w/index.php?title=Intermediate_eXperimental_Vehicle&oldid=1333535954
[ref_leo]: https://en.wikipedia.org/w/index.php?title=Low_Earth_orbit&oldid=1340136028
[ref_lift_to_drag]: https://en.wikipedia.org/w/index.php?title=Lift-to-drag_ratio&oldid=1314615335
[ref_lifting_body]: https://en.wikipedia.org/w/index.php?title=Lifting_body&oldid=1335230534
[ref_lippisch]: https://en.wikipedia.org/w/index.php?title=Alexander_Lippisch&oldid=1335526007
[ref_mach_number]: https://en.wikipedia.org/w/index.php?title=Mach_number&oldid=1341518938
[ref_me_163]: https://en.wikipedia.org/w/index.php?title=Messerschmitt_Me_163_Komet&oldid=1328380694
[ref_mirage_2000]: https://en.wikipedia.org/w/index.php?title=Dassault_Mirage_2000&oldid=1340565501
[ref_mirage_iii]: https://en.wikipedia.org/w/index.php?title=Dassault_Mirage_III&oldid=1340917756
[ref_nasp]: https://en.wikipedia.org/w/index.php?title=Rockwell_X-30&oldid=1335251084
[ref_northrop_n1m]: https://en.wikipedia.org/w/index.php?title=Northrop_N-1M&oldid=1297859500
[ref_orbital_mechanics]: https://en.wikipedia.org/w/index.php?title=Orbital_mechanics&oldid=1338973693
[ref_paperclip]: https://en.wikipedia.org/w/index.php?title=Operation_Paperclip&oldid=1341653153
[ref_pegasus_rocket]: https://en.wikipedia.org/w/index.php?title=Northrop_Grumman_Pegasus&oldid=1334464796
[ref_prompt_global_strike]: https://en.wikipedia.org/w/index.php?title=Conventional_Prompt_Strike&oldid=1337663060
[ref_ramjet]: https://en.wikipedia.org/w/index.php?title=Ramjet&oldid=1339824211
[ref_reusable_launch]: https://en.wikipedia.org/w/index.php?title=Reusable_launch_vehicle&oldid=1340738453
[ref_rocket_equation]: https://en.wikipedia.org/w/index.php?title=Tsiolkovsky_rocket_equation&oldid=1339265602
[ref_sabre_engine]: https://en.wikipedia.org/w/index.php?title=SABRE_(rocket_engine)&oldid=1341657292
[ref_saenger]: https://en.wikipedia.org/wiki/S%C3%A4nger_II
[ref_scramjet]: https://en.wikipedia.org/w/index.php?title=Scramjet&oldid=1336403495
[ref_shuttle]: https://en.wikipedia.org/w/index.php?title=Space_Shuttle_program&oldid=1333744633
[ref_silbervogel]: https://en.wikipedia.org/w/index.php?title=Silbervogel&oldid=1316237133
[ref_skylon]: https://en.wikipedia.org/w/index.php?title=Skylon_(spacecraft)&oldid=1334726586
[ref_space_rider]: https://en.wikipedia.org/w/index.php?title=Space_Rider&oldid=1340087982
[ref_spaceshiptwo]: https://en.wikipedia.org/w/index.php?title=SpaceShipTwo&oldid=1338526105
[ref_specific_impulse]: https://en.wikipedia.org/w/index.php?title=Specific_impulse&oldid=1340816504
[ref_sr71]: https://en.wikipedia.org/w/index.php?title=Lockheed_SR-71_Blackbird&oldid=1340534278
[ref_ssto]: https://en.wikipedia.org/w/index.php?title=Single-stage-to-orbit&oldid=1338027163
[ref_star_raker]: https://en.wikipedia.org/w/index.php?title=Single-stage-to-orbit&oldid=1338027163
[ref_starship]: https://en.wikipedia.org/w/index.php?title=SpaceX_Starship&oldid=1341721181
[ref_static_margin]: https://en.wikipedia.org/w/index.php?title=Longitudinal_stability&oldid=1334439692
[ref_swept_wing]: https://en.wikipedia.org/w/index.php?title=Swept_wing&oldid=1328845509
[ref_tps]: https://en.wikipedia.org/w/index.php?title=Atmospheric_entry&oldid=1339928327
[ref_tsto]: https://en.wikipedia.org/w/index.php?title=Two-stage-to-orbit&oldid=1325537168
[ref_tu144]: https://en.wikipedia.org/w/index.php?title=Tupolev_Tu-144&oldid=1341710676
[ref_uhtc]: https://en.wikipedia.org/w/index.php?title=Ultra-high_temperature_ceramic&oldid=1340676888
[ref_viggen]: https://en.wikipedia.org/w/index.php?title=Saab_37_Viggen&oldid=1333817905
[ref_vortex_lift]: https://en.wikipedia.org/w/index.php?title=Vortex_lift&oldid=1309024110
[ref_vulcan]: https://en.wikipedia.org/w/index.php?title=Avro_Vulcan&oldid=1335821152
[ref_waverider]: https://en.wikipedia.org/w/index.php?title=Waverider&oldid=1311620728
[ref_white_knight]: https://en.wikipedia.org/w/index.php?title=Scaled_Composites_White_Knight&oldid=1318685091
[ref_x15]: https://en.wikipedia.org/w/index.php?title=North_American_X-15&oldid=1341109634
[ref_x20]: https://en.wikipedia.org/w/index.php?title=Boeing_X-20_Dyna-Soar&oldid=1333734859
[ref_x33]: https://en.wikipedia.org/w/index.php?title=Lockheed_Martin_X-33&oldid=1337656265
[ref_x37b]: https://en.wikipedia.org/w/index.php?title=Boeing_X-37&oldid=1338933184
[ref_x43]: https://en.wikipedia.org/w/index.php?title=NASA_X-43&oldid=1332600803
[ref_x47b]: https://en.wikipedia.org/w/index.php?title=Northrop_Grumman_X-47B&oldid=1340289892
[ref_x48]: https://en.wikipedia.org/w/index.php?title=Boeing_X-48&oldid=1321603411
[ref_x51]: https://en.wikipedia.org/w/index.php?title=Boeing_X-51_Waverider&oldid=1284050871
[ref_xf92]: https://en.wikipedia.org/w/index.php?title=Convair_XF-92&oldid=1313820428
[ref_yb35]: https://en.wikipedia.org/w/index.php?title=Northrop_YB-35&oldid=1324258308
[ref_yb49]: https://en.wikipedia.org/w/index.php?title=Northrop_YB-49&oldid=1332041135
[related_post_rocketplanes]: {% post_url 2026-02-27-history_of_rocketplanes %}
[related_post_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[research_clipped_delta]: https://ntrs.nasa.gov/citations/19950003616
[research_nasa_staging]: https://ntrs.nasa.gov/citations/20200002873
[research_polhamus]: https://ntrs.nasa.gov/citations/19670003842
[research_x43_separation]: https://ntrs.nasa.gov/citations/20000091005
