---
layout: post
mathjax: false
comments: true
title: "History of Rocketplanes"
date: 2026-02-27 00:00:00 +0000
categories: space history
---

<!-- A96 -->

A rocketplane is an aircraft that uses rocket engines
for primary propulsion.
Unlike conventional aircraft,
which generate thrust by accelerating ambient air
through jet engines or propellers,
rocketplanes carry both fuel and oxidizer onboard
and are therefore not dependent on atmospheric oxygen.
This self-contained propulsion allows rocketplanes
to operate at altitudes and speeds
far beyond the reach of air-breathing engines,
including flight above the atmosphere itself.
Unlike expendable rockets,
which are discarded after a single use,
rocketplanes are designed to be recovered and reflown,
combining the performance of a rocket
with the reusability of an airplane.

The history of rocketplanes
is not a collection of isolated experiments
but a single continuous thread
running from 1928 to the present day.
Each vehicle in this history
inherited knowledge from its predecessors
and contributed knowledge to its successors.
The connections are sometimes direct,
as when a designer moved from one program to the next.
They are sometimes indirect,
as when captured hardware and documents
were shipped across oceans by intelligence agencies.
And they are sometimes adversarial,
as when one nation built a vehicle
specifically to counter or replicate
what another nation had achieved.
The thread is held together
by technology transfer, espionage,
and the institutional memory
of engineers who spent entire careers
advancing the state of the art.

For the mathematical foundations
of rocket propulsion, orbital mechanics,
and atmospheric flight dynamics,
see the companion article
[Introduction to Space Studies][related_post_space_studies].

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-27 00:00:00 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64

$ sw_vers
ProductName:		macOS
ProductVersion:		14.6.1
BuildVersion:		23G93

# Hardware Information
$ system_profiler SPHardwareDataType | sed -n '8,10p'
      Chip: Apple M1 Max
      Total Number of Cores: 10 (8 performance and 2 efficiency)
      Memory: 32 GB

# Shell and Version
$ echo "${SHELL}"
/bin/bash

$ "${SHELL}" --version | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin23)

# Claude Code Installation Versions
$ claude --version
2.1.42 (Claude Code)
```

## The German Pioneers

### Lippisch Ente, 1928

The history of rocketplanes begins
on 11 June 1928 at the Wasserkuppe,
a mountain in central Germany
that had served as a center for glider flying
since the early 1920s.
On that date, the glider pilot Fritz Stamer
flew the [Lippisch Ente][ref_lippisch_ente],
a tailless canard glider designed by Alexander Lippisch
and fitted with two Sander black powder rockets.
The name "Ente" is the German word for "duck,"
a reference to the canard configuration
in which the horizontal stabilizer
is mounted ahead of the main wing.
The canard layout is called "canard"
in English and French
because the French word for "duck" is "canard."

Each Sander rocket produced approximately 200 newtons
of thrust for about 30 seconds.
Stamer fired them in sequence,
completing a 1,500-meter circuit
of the Wasserkuppe airstrip.
This was the first rocket-powered piloted aircraft flight
in history.
A second flight attempted to fire both rockets simultaneously
for greater thrust over a shorter period.
One rocket exploded,
punching holes in both wings
and setting the aircraft on fire.
Stamer brought the burning glider down
from approximately 20 meters altitude
and escaped without serious injury.
The Ente burned beyond repair.

The flight was commissioned by Fritz von Opel
as part of the Opel-RAK rocket program,
a collaboration between von Opel,
the rocket builder Friedrich Sander,
and the Austrian rocket enthusiast Max Valier.

### Opel RAK.1, 1929

Where the Ente was a modified sailplane,
the [Opel RAK.1][ref_opel_rak1] was the first aircraft
designed and built specifically for rocket propulsion.
Julius Hatry designed and constructed the airframe
under commission from Fritz von Opel.
On 30 September 1929, at Rebstock airfield near Frankfurt am Main,
von Opel himself piloted the RAK.1 before a large crowd.

The aircraft carried 16 Sander solid-fuel rockets
producing a combined thrust
of approximately 7,800 newtons.
Von Opel flew approximately 3.5 kilometers
in 75 seconds,
reaching an estimated top speed
of 150 kilometers per hour.
The landing was hard.
A downward gust at the edge of the landing ground
forced von Opel down at approximately 129 kilometers per hour.
The landing skid broke
and the cockpit floor was shaved away,
leaving von Opel hanging by his safety belt.
He emerged unscathed,
but the aircraft was significantly damaged.

Shortly after this flight,
the onset of the Great Depression
ended the Opel rocket experiments.
Von Opel left Germany before 1930.

### Heinkel He 176, 1939

A full decade passed
before the next major advance in rocketplane design.
On 20 June 1939,
the test pilot Erich Warsitz flew
the [Heinkel He 176][ref_he_176],
the first aircraft powered solely
by a liquid-fueled rocket engine.
The engine was the Walter HWK R I-203,
which burned 82 percent hydrogen peroxide
and produced 5,880 newtons of thrust
for approximately 50 seconds.

The He 176 was a private venture by Ernst Heinkel,
who had been exploring rocket propulsion
through earlier tests on modified aircraft.
Warsitz had previously flown test flights
on rocket-equipped He 72 and He 112 airframes
to demonstrate the viability of rocket propulsion.

On 3 July 1939, Warsitz demonstrated the He 176
for Adolf Hitler and senior military leadership.
The demonstration included a dramatic moment
when Warsitz miscalculated his engine shutdown,
began descending rapidly,
then restarted the engine just before hitting the ground
and performed a near-vertical climb.
Despite this spectacle,
the Reichsluftfahrtministerium
cancelled the program on 12 September 1939,
judging the aircraft too small
and its performance unimpressive
relative to conventional fighters.
The single airframe was transferred
to the Deutsche Luftfahrtsammlung in Berlin,
where it was destroyed
in an Allied bombing raid in 1943.

### DFS 194, 1940

While Heinkel pursued the He 176 as a private venture,
Alexander Lippisch continued developing
his tailless swept-wing designs
at the Deutsche Forschungsanstalt fur Segelflug,
the German Institute for Sailplane Flight.
On 2 January 1939,
Lippisch and his entire team
were transferred to the Messerschmitt company
under the code name "Project X"
to develop a rocket-powered interceptor.

The [DFS 194][ref_dfs_194] was a tailless aircraft
originally designed with a piston engine.
The airframe was modified
to accept the Walter R I-203 rocket motor,
the same engine type used in the He 176.
In August 1940, at Peenemunde-West,
the test pilot Heini Dittmar
flew the DFS 194 under rocket power,
reaching 550 kilometers per hour
and exceeding the speed of the He 176.

The DFS 194 proved
that Lippisch's tailless swept-wing configuration
was safe and effective at high speeds.
It served as the direct aerodynamic precursor
to the Messerschmitt Me 163 Komet,
which scaled up the same design philosophy
for operational combat.

## Operational Rocketplanes of World War II

### Messerschmitt Me 163 Komet

The [Messerschmitt Me 163 Komet][ref_me_163]
was the only rocket-powered fighter aircraft
to achieve operational combat status
in the history of aviation.
Its lineage ran directly from the Lippisch Ente of 1928
through the DFS 194 of 1940,
making it the culmination of over a decade
of tailless swept-wing rocketplane research.

The production Me 163B was powered
by the Walter HWK 109-509A-2 bipropellant rocket engine,
which produced 16,670 newtons of thrust.
The engine burned T-Stoff,
concentrated hydrogen peroxide used as the oxidizer,
and C-Stoff,
a mixture of hydrazine hydrate and methanol used as the fuel.
These propellants were hypergolic,
meaning they ignited spontaneously on contact.
Both were also extremely corrosive and toxic,
and fuel leaks caused numerous fatal ground accidents
throughout the program.

The Me 163 carried approximately 1,650 liters
of propellant,
providing 7.5 to 8 minutes of powered flight.
This was sufficient for a climb
to the service ceiling of 12,100 meters
in approximately 3.5 minutes,
followed by one or two high-speed passes
through an Allied bomber formation
before the pilot glided back to base unpowered.
The aircraft was armed with two 30-millimeter MK 108 cannon.

On 2 October 1941,
Heini Dittmar flew the Me 163A V4
to 1,004.5 kilometers per hour,
becoming the first pilot
to exceed 1,000 kilometers per hour.
This record was not officially surpassed until 1947.
On 6 July 1944,
Dittmar reached an unofficial 1,130 kilometers per hour
in the Me 163B V18.

Jagdgeschwader 400, the operational unit
assigned to fly the Me 163,
was formed on 1 February 1944 at Brandis airfield.
The first combat sortie occurred on 28 July 1944.
Over the course of the war,
the Me 163 achieved 9 confirmed aerial kills
while suffering 14 aircraft losses,
of which approximately 10 were in combat
and the remainder from accidents
and landing crashes.
About half of all losses occurred
during unpowered landing approaches,
when the aircraft was at its most vulnerable.
Allied fighter pilots learned
to wait for the Komet to exhaust its fuel
and then attack during the glide.

Approximately 370 Me 163s were produced.
Only 279 entered service.
Jagdgeschwader 400 was disbanded in April 1945,
and surviving pilots were transferred
to Me 262 jet fighter units.
The Me 163 demonstrated
both the extraordinary potential
and the severe practical limitations
of rocket-powered combat aircraft.

### Bachem Ba 349 Natter

The [Bachem Ba 349 Natter][ref_ba_349]
represented a fundamentally different approach
to rocket-powered interception.
Where the Me 163 was a sophisticated fighter
requiring trained pilots and prepared airfields,
the Natter was a semi-expendable vertical-launch interceptor
designed to be operated
by minimally trained personnel
from concealed forest clearings.

Designed by Erich Bachem,
the Natter was launched vertically from a guide rail
using four Schmidding SG34 solid-fuel boosters
producing 47,000 newtons of combined thrust
for 10 seconds.
After booster separation,
the main Walter HWK 109-509A-1 engine,
the same type used in the Me 163,
sustained flight.
The pilot would aim at a bomber formation,
fire a salvo of 24 unguided rockets from the nose,
and then bail out.
A separate parachute would recover the rear fuselage
containing the Walter engine for reuse.

On 1 March 1945,
the test pilot Lothar Sieber
made the first and only crewed vertical takeoff flight.
At approximately 500 meters altitude,
the cockpit canopy came loose.
The headrest was attached to the underside of the canopy,
and when it separated,
Sieber's head was pulled backward
under three times the force of gravity.
Erich Bachem concluded
that Sieber likely pulled the control column backward
involuntarily.
The Natter entered an uncontrolled trajectory
and crashed,
killing Sieber at the age of 22.
He became the first person
to launch vertically under rocket power.

Thirty-six Natters were produced by the war's end.
Twenty-five were used in unmanned test flights.
None entered operational combat.
The program stands as a measure
of the desperation that characterized
the final months of the war.

### Yokosuka MXY-7 Ohka

The [Yokosuka MXY-7 Ohka][ref_ohka]
was a rocket-powered piloted weapon
developed by the Imperial Japanese Navy
independently of any German rocketplane program.
The Ohka, whose name means "Cherry Blossom,"
was designed at the Yokosuka Naval Air Technical Arsenal
based on a concept by Ensign Mitsuo Ohta.

The aircraft carried three
Type 4 Mark 1 Model 20 solid-fuel rocket motors,
each producing 2,616 newtons of thrust
for 8 to 10 seconds.
In the nose sat a 1,200-kilogram warhead.
The Ohka was carried to altitude
beneath a Mitsubishi G4M "Betty" bomber
and released within range of Allied naval vessels.
After release,
the pilot would ignite the rockets
and dive into the target
at speeds reaching 1,040 kilometers per hour.

The first combat deployment on 21 March 1945
was a complete failure.
The G4M mother ships were intercepted
by Allied fighters before reaching release range
and were forced to jettison their Ohkas prematurely.
The first successful strike came on 12 April 1945,
when an Ohka sank the destroyer USS Mannert L. Abele
near Okinawa.
Over the course of the Okinawa campaign,
Ohka attacks sank or damaged beyond repair
three Allied ships.

Seven hundred and fifty-five operational Ohkas
were produced.
Postwar analysis concluded
that the weapon's impact was negligible,
primarily because
the slow, heavily laden G4M mother ships
were extremely vulnerable to interception
before reaching release range.

### Bereznyak-Isayev BI-1

The [Bereznyak-Isayev BI-1][ref_bi_1]
was the Soviet Union's first rocket-powered aircraft,
developed under wartime urgency
following Operation Barbarossa.
Designed by Alexander Bereznyak and Alexei Isayev
under the supervision of Viktor Bolkhovitinov,
the BI-1 was powered
by the Dushkin D-1A-1100 liquid-fueled rocket engine.
The engine burned tractor kerosene
and red fuming nitric acid
and was expected to produce 10,800 newtons at full power.

On 15 May 1942,
the test pilot Grigory Bakhchivandzhi
flew the BI-1 under rocket power
for the first time.
The engine had been de-rated
to 4,900 newtons for safety.
Bakhchivandzhi reached an altitude of 840 meters
and a maximum speed of 400 kilometers per hour
in a flight lasting 3 minutes and 9 seconds.

On 27 March 1943,
during his seventh flight in the type,
Bakhchivandzhi was killed
when the BI-3 prototype entered a 45-degree dive
and crashed.
The cause was not understood at the time.
Later wind tunnel testing
revealed the phenomenon of transonic pitch-down,
in which high-speed aerodynamic effects
created an uncontrollable nose-down pitching moment
on the stabilizers.

Seven BI prototypes were constructed.
A total of 12 powered flights were recorded.
Bereznyak went on to found OKB-155,
which became a leading cruise missile design bureau.
Isayev founded OKB-2,
specializing in liquid-propellant rocket engines
for spacecraft and launch vehicles.
In 1973, Bakhchivandzhi was posthumously
elevated to Hero of the Soviet Union.

## Technology Transfer and Espionage

### Operation Paperclip

The defeat of Nazi Germany in 1945
triggered a race among the Allied powers
to capture German aerospace engineers
and their research.
[Operation Paperclip][ref_paperclip]
was the American program
that brought German scientists and engineers
to the United States
to continue their work under American direction.

Among the rocketplane-specific captures,
[Alexander Lippisch][ref_lippisch]
was brought to the United States
and assigned to Wright Field.
After his initial assignment ended in 1946,
he joined the Naval Air Materiel Center in Philadelphia,
remaining until 1950.
His captured DM-1 delta-wing glider
was shipped to the National Advisory Committee for Aeronautics,
or NACA, at Langley for full-scale wind tunnel testing.
The data from these tests
influenced the development of the Convair XF-92A,
the first jet-propelled delta-wing aircraft to fly.

[Walter Dornberger][ref_dornberger],
who had led the V-2 rocket program at Peenemunde,
joined Bell Aircraft Corporation in 1950
and rose to vice president.
At Bell, Dornberger proposed
the Bomber-Missile concept in 1952
with Krafft Ehricke,
a vertical-launch boost-glide vehicle
directly descended from the wartime Silbervogel concept.
Dornberger also played a major role
in the development of the North American X-15
and served as a key consultant
for the Boeing X-20 Dyna-Soar.
His career at Bell, which lasted until 1965,
represents one of the clearest examples
of direct technology transfer
from German wartime rocketplane research
to American postwar programs.

Five captured Me 163 airframes
were shipped to the United States.
Unpowered glide tests were conducted
at Muroc dry lake beginning 3 May 1946,
with Me 163 airframes towed to altitude
behind Boeing B-29 aircraft.
Lippisch himself participated in the tests
and discovered wing delamination,
which led to the cancellation
of planned powered flight tests.
Walter HWK 109-509 engine documentation
captured at the Walter factory
provided detailed information
on bipropellant rocket engine design,
variable-thrust control,
and the use of hydrogen peroxide as an oxidizer.

### Operation Osoaviakhim

On the Soviet side,
the capture of German aerospace expertise
took a different and more coercive form.
During the night of 21 to 22 October 1946,
[Operation Osoaviakhim][ref_osoaviakhim]
forcibly relocated approximately 2,500 German specialists
along with nearly 3,800 family members
from the Soviet occupation zone of Germany
to facilities across the Soviet Union.
The operation was decreed
on 13 May 1946 under Council of Ministers resolution
number 1017-419
and was carried out by MVD and Soviet Army units
under the Soviet Military Administration in Germany.

The captured specialists included
experts in rocketry, aviation, and optics.
The Soviet Ministry of Aviation Industry
acquired approximately 3,558 aviation experts
through this and related programs,
enabling the transfer of swept-wing design,
turbomachinery expertise,
and rocket engine technology.
German engineers adapted
Me 163 rocket interceptor data
for Soviet air-to-surface missile prototypes.
Captured Me 163 airframes, Walter engine components,
and swept-wing aerodynamic data
all contributed to Soviet postwar aviation development.

For the broader context of German rocket technology capture,
including the parallel effort
to acquire V-2 ballistic missile expertise,
see [Introduction to Space Studies][related_post_space_studies].

### The Silbervogel Concept

Not all technology transfer
involved the physical capture
of hardware and personnel.
The [Silbervogel][ref_silbervogel],
or "Silver Bird,"
was a suborbital antipodal bomber concept
developed by Eugen Sanger and Irene Bredt
in the late 1930s and early 1940s.
The vehicle was never built,
but the idea proved
to be one of the most influential
rocketplane concepts of the twentieth century.

Sanger and Bredt proposed
a liquid-propellant rocket-powered vehicle
capable of Mach 10 at altitudes exceeding 160 kilometers.
The aircraft would be launched
from a rocket-powered sled
and then skip along the upper atmosphere
in a series of suborbital hops,
using the fuselage as a lifting body
to generate lift during each atmospheric encounter.
The final version of their research
was published in 1944 as a classified report
titled "A Rocket Drive for Long-Range Bombers."
Approximately 100 copies were produced.

Soviet intelligence discovered copies
of the Sanger-Bredt report at Peenemunde.
A condensed version reached Stalin.
In November 1946,
the NII-1 research institute was formed
under the mathematician Mstislav Keldysh
to evaluate the concept.
In 1947, the Keldysh team concluded
that the high fuel consumption
of Sanger's rocket-based design
made the concept impracticable in the short term
but proposed an alternative
using a combined ramjet and rocket propulsion system.
This analysis would later influence
the design of the MiG-105 Spiral spaceplane
in the 1960s.

On the American side,
Dornberger used the Silbervogel concept
as the basis for his Bomber-Missile proposal at Bell Aircraft.
Research at Bell showed
that the atmospheric skip-glide technique
was less practical than anticipated,
leading to the boost-glide approach
that eventually became the Boeing X-20 Dyna-Soar.
The Silbervogel concept thus influenced
both superpowers' spaceplane programs
for decades after its authors
had moved on to other work.

## The American X-Plane Program

### Bell X-1, 1947

On 14 October 1947,
Captain Charles "Chuck" Yeager
flew the [Bell X-1][ref_bell_x1]
to Mach 1.06 at an altitude of 13,100 meters,
becoming the first pilot
to exceed the speed of sound in controlled level flight.
The aircraft, serial number 46-062,
was nicknamed "Glamorous Glennis"
after Yeager's wife.

The X-1 was powered
by the Reaction Motors XLR11-RM-3,
a four-chamber liquid-fueled rocket engine
producing 26,700 newtons of thrust.
The aircraft was air-launched
from the bomb bay of a Boeing B-29 Superfortress
at 6,100 meters above Rogers Dry Lake
at Edwards Air Force Base in California.

The Bell X-1 established
the template for the entire X-plane program.
It demonstrated
that a purpose-built rocket-powered research aircraft,
air-launched from altitude
and recovered on a dry lakebed,
could systematically explore
flight regimes that were inaccessible
to conventional aircraft.
Every subsequent X-plane
followed this basic operational pattern.

### Bell X-1A and X-1B

The [X-1A][ref_bell_x1a] and X-1B extended
the original X-1 design
to higher speeds and new research objectives.
On 12 December 1953,
Yeager flew the X-1A to Mach 2.44
at an altitude of 22,800 meters.
Shortly after reaching peak speed,
the aircraft experienced inertia coupling,
a phenomenon not yet fully understood at the time,
and entered a violent spin.
The X-1A dropped from maximum altitude
to 7,600 meters,
subjecting Yeager to accelerations of up to 8 g.
He struck and cracked the canopy with his helmet
before regaining control.

The [X-1B][ref_bell_x1b]
contributed a different but equally important advance.
In November 1957,
NACA technicians installed reaction control jets
on the X-1B,
making it the first aircraft
to fly with a reaction control system.
Small rocket thrusters
provided directional control
independent of aerodynamic surfaces,
a capability essential for flight
at altitudes where the atmosphere is too thin
for conventional control surfaces to function.
The test pilot Neil Armstrong
made three flights
to evaluate the reaction control system's performance.
Cracks in the fuel tanks
forced the X-1B's retirement in 1958 after 27 flights.
The reaction control research then shifted
to the Lockheed F-104 Starfighter
and subsequently informed
the X-15's control system design.

### Douglas D-558-2 Skyrocket, 1953

On 20 November 1953,
the NACA research pilot A. Scott Crossfield
flew the [Douglas D-558-2 Skyrocket][ref_d558_2]
to Mach 2.005 at 18,900 meters,
becoming the first pilot to exceed Mach 2.

The Skyrocket was notable
for its mixed propulsion system.
It carried both a Westinghouse J34-WE-40 turbojet
producing 13,300 newtons of thrust
for takeoff, climb, and landing,
and a Reaction Motors LR8-RM-6 four-chamber rocket engine
producing 26,700 newtons of thrust
for high-speed research.
For the Mach 2 flight,
the Skyrocket was air-launched
from a Navy P2B-1S Superfortress at 9,800 meters.
Crossfield fired the rocket engine,
climbed to 22,000 meters,
entered a shallow dive,
passed Mach 2 at 18,900 meters,
and then made an unpowered dead-stick landing
on the dry lakebed at Edwards Air Force Base.

### Bell X-2 Starbuster, 1956

The [Bell X-2 Starbuster][ref_bell_x2]
was designed to explore flight
at speeds beyond Mach 2
and to investigate the aerodynamic heating
and stability challenges
that emerged at higher velocities.
It was powered by the Curtiss-Wright XLR25,
a two-chamber throttleable liquid-fueled rocket engine
with variable thrust
ranging from 11,100 to 66,700 newtons.

On 27 September 1956,
Captain Milburn "Mel" Apt
flew the X-2 to Mach 3.196 at 19,960 meters,
becoming the first pilot to exceed Mach 3.
This was Apt's first and only X-2 flight.
The engine burned 15 seconds longer than planned,
carrying the aircraft well beyond
the intended maximum of Mach 2.8.
After reaching Mach 3.196,
Apt initiated a banking turn
while still above Mach 3.
The aircraft experienced inertia coupling
and tumbled uncontrollably.
Apt ejected using the aircraft's
encapsulated cockpit escape system
but was briefly knocked unconscious
and was unable to bail out of the capsule
before it struck the ground.
He was killed.

The X-2 program demonstrated
that aerodynamic heating and stability
at Mach 3 and above
presented challenges qualitatively different
from those encountered at lower speeds.
These lessons directly informed
the thermal protection and stability augmentation systems
designed into the X-15.

### North American X-15 and X-15A-2

The [North American X-15][ref_x15]
was the most ambitious
and most productive rocketplane ever built.
Over a nine-year program
running from 8 June 1959 to 24 October 1968,
three X-15 aircraft made 199 free flights
carrying 12 pilots,
systematically exploring
the hypersonic flight regime
from Mach 4 to Mach 6.7
and from the upper atmosphere
to altitudes above 100 kilometers.

The X-15 was powered
by the Reaction Motors XLR99,
the first large throttleable,
restartable human-rated rocket engine.
It produced 253,500 newtons of thrust at vacuum
and burned liquid oxygen and anhydrous liquid ammonia.
The first 24 flights used two XLR11 engines
before the XLR99 was ready,
with the new engine installed beginning November 1960.

On 3 October 1967,
Major William "Pete" Knight
flew the X-15A-2 to Mach 6.7 at 31,120 meters,
setting the speed record for a crewed,
powered, controlled aircraft
that stands to this day.
The X-15A-2 was the number two airframe
rebuilt after an emergency landing.
It featured a 71-centimeter fuselage extension,
two external drop tanks
adding 25,900 kilograms of propellant
and providing 60 seconds of additional engine burn,
and an ablative heat shield coating.

On 22 August 1963,
the NASA research pilot Joseph Walker
flew the X-15 to 107,960 meters,
crossing the Karman line
at 100 kilometers altitude
and becoming the first person to enter space twice.
He remained weightless for approximately five minutes.

Eight X-15 pilots flew above 80,500 meters,
the 50-mile altitude that qualified them
as astronauts under the United States definition.
Five were Air Force pilots
who received military astronaut wings at the time.
Three were NASA civilian pilots
who received astronaut wings retroactively in 2005.
Among them was Michael Adams,
who was killed on 15 November 1967
when his X-15 entered a violent Mach 5 spin at 70,100 meters.
The aircraft broke apart
when aerodynamic forces exceeded design limits
during descent through the lower atmosphere.

The X-15 program bridged
the era of atmospheric rocket-powered research aircraft
and the era of orbital spaceplanes.
Its data on hypersonic aerodynamics,
thermal protection, reaction control systems,
and human factors at extreme altitudes
directly informed the design
of every subsequent American reentry vehicle,
including the Space Shuttle.

### Boeing X-20 Dyna-Soar

The [Boeing X-20 Dyna-Soar][ref_x20]
was designed as an orbital spaceplane
capable of launching vertically atop a Titan rocket,
maneuvering in orbit,
and returning to a runway landing.
The program represented
the most direct descendant
of the Silbervogel concept,
pursued through Walter Dornberger's influence at Bell Aircraft
and subsequently at Boeing
after Boeing won the prime contract in June 1959.

The X-20 was cancelled
on 10 December 1963
by Secretary of Defense Robert McNamara,
who cited escalating costs,
uncertainty over the launch vehicle,
and a lack of clearly defined mission.
The program had suffered
from persistent conflict
between the Air Force and NASA's Mercury and Apollo programs
over the role of crewed military spaceflight.
Funding was redirected
to the Manned Orbiting Laboratory.

Although the X-20 never flew,
its cancellation had significant consequences.
It prompted the Soviet Union
to initiate the MiG-105 Spiral spaceplane program.
It also advanced the state of the art
in thermal protection,
reentry guidance,
and boost-glide trajectory planning,
all of which contributed
to the Space Shuttle design a decade later.

### Martin X-24A and X-24B

The [Martin X-24A and X-24B][ref_x24]
were lifting body research vehicles
designed to test
whether a wingless vehicle shape
could generate sufficient aerodynamic lift
to make a controlled runway landing
after reentry from orbit.

The X-24A had a bulbous teardrop shape
with no conventional wings.
It was 7.5 meters long and 3.5 meters wide,
powered by the XLR11 rocket engine,
and drop-launched from a modified B-52 Stratofortress.
It completed 28 flights,
reaching a maximum speed of 1,667 kilometers per hour
and a maximum altitude of 21,800 meters.

The X-24B was created
by returning the X-24A to Martin Marietta
for modification into a new shape.
The rebuilt vehicle featured a rounded top,
a flat bottom, and a double delta planform
with a pointed nose.
It completed 36 flights,
reaching 1,873 kilometers per hour
and 22,600 meters.

On 5 August 1975,
the NASA test pilot John Manke
flew the X-24B from altitude
to an unpowered precision landing
on the main concrete runway at Edwards Air Force Base.
This was the first unpowered landing
of a lifting body on a conventional runway.
The demonstration was pivotal.
It convinced NASA engineers
that the Space Shuttle orbiter could land unpowered,
directly leading to the elimination
of jet engines
that had originally been planned
for Shuttle landing approaches.

## The Soviet Response

### MiG-105 Spiral

The [MiG-105 Spiral][ref_mig_105]
was the Soviet Union's direct response
to the American X-20 Dyna-Soar.
Work on the Spiral aerospace system
began formally in 1965,
two years after the Dyna-Soar's cancellation.
The Soviet Air Force
tasked the Mikoyan design bureau
under chief designer Gleb Lozino-Lozinsky,
with official authorization granted on 26 June 1966.

The Spiral concept differed significantly
from the Dyna-Soar's expendable-rocket launch profile.
Soviet engineers proposed
an air-launched system
in which a spaceplane and booster stage
would be released at high altitude
from a large hypersonic mothership.
The spaceplane featured a variable-geometry wing
for atmospheric flight after reentry.

The project was halted in 1969
and briefly resurrected in 1974
in response to the United States Space Shuttle program.
A subscale atmospheric test vehicle,
the MiG-105-11,
conducted eight subsonic free-flight tests
between October 1976 and September 1978
at Zhukovsky Air Base near Moscow.
All flights were piloted
by the test pilot Aviard Fastovets.
The first crewed drop test
occurred on 11 October 1976
from a modified Tu-95K bomber.
The final flight in September 1978
ended in a hard landing
that damaged the prototype.

The Spiral project was officially terminated in 1978
when the decision was made
to concentrate resources on the Buran program instead.
Data and experience from the MiG-105
contributed to the Buran shuttle's design,
most notably through the BOR-4
subscale orbital test vehicles,
which were related
to the Spiral program's lifting body research.

In an ironic twist of intelligence history,
the BOR-4 was photographed
by Western intelligence agencies
during recovery operations in the Indian Ocean in 1983.
Researchers at NASA Langley Research Center
reverse-engineered scale models from these photographs
and tested them in wind tunnels,
producing the HL-20 lifting body concept.
The HL-20 eventually became
the basis for Sierra Space's Dream Chaser,
a vehicle discussed later in this article.
Soviet intelligence thus informed American designs
just as American intelligence had informed Soviet ones.

### Buran

The [Buran][ref_buran] program
was the Soviet Union's response
to the American Space Shuttle.
At 03:00:02 UTC on 15 November 1988,
the Buran orbiter
launched from Baikonur Cosmodrome
atop an Energia super-heavy lift rocket,
completed two orbits of the Earth
in 3 hours and 25 minutes,
and performed a fully automated landing
at the shuttle runway at Baikonur.
The flight was entirely uncrewed.
No American Space Shuttle
ever performed a fully automated landing.

The Buran program
was accompanied by one of the most extensive
aerospace espionage campaigns of the Cold War.
By the time the American Shuttle first launched
in April 1981,
the KGB had acquired over 3,000 documents
related to the Shuttle program,
including approximately 300
related to wind tunnel tests,
100 on solid rocket boosters,
and others on computer systems
and military applications.
Much of the material was unclassified,
obtained from the Government Printing Office
and NASA-funded contractor studies.

Despite the external visual similarity
to the Space Shuttle,
the Buran incorporated fundamental design differences
that reflected independent Soviet engineering decisions.
The main engines were located on the Energia rocket
rather than on the orbiter,
meaning the expensive engines
were expended with each launch
but also allowing the Energia
to serve as an independent heavy-lift vehicle.
The orbiter carried ejection seats for the crew.
Most significantly,
the Buran was designed from the outset
for fully autonomous flight,
including uncrewed orbital operations
and automated landing.
These differences suggest
that espionage primarily informed
the external aerodynamic configuration,
while the propulsion architecture,
avionics, and operational philosophy
were developed independently.

The Buran program
was officially terminated on 30 June 1993
following the dissolution of the Soviet Union
and the resulting collapse in funding.
Approximately 20 billion rubles
had been spent on the program.
On 12 May 2002,
the hangar roof at Baikonur Cosmodrome collapsed,
destroying the Buran orbiter that had flown in 1988
along with a mockup of an Energia booster
and killing eight workers.

## The Space Shuttle

The [Space Shuttle][ref_shuttle]
was the largest and most complex rocketplane ever flown.
Over 30 years of operations
from 12 April 1981 to 21 July 2011,
the Shuttle fleet completed 135 missions,
carrying 355 astronauts from 16 countries.
Five operational orbiters were built.
[Columbia][ref_columbia] flew first in 1981.
[Challenger][ref_challenger] entered service in 1983.
[Discovery][ref_discovery] began flying in 1984.
[Atlantis][ref_atlantis] followed in 1985.
[Endeavour][ref_endeavour] was built in 1991
as a replacement for Challenger.

The Shuttle's place in rocketplane history
is defined by the programs that preceded it.
The X-15 provided hypersonic flight data,
thermal protection research,
and reaction control system experience
that directly informed the Shuttle's reentry profile.
The lifting body program,
culminating in the X-24B's
unpowered runway landing in 1975,
demonstrated that a winged orbiter
could glide to a conventional landing
without air-breathing engines.
The X-20 Dyna-Soar,
although cancelled before flying,
established the concept
of a piloted winged orbital vehicle
with conventional runway recovery.
The X-1B's reaction control system work
informed the Shuttle's attitude control design.

The loss of Challenger on 28 January 1986,
73 seconds after launch
due to the failure of an O-ring seal
in the right solid rocket booster,
killed all seven crew members.
The loss of Columbia on 1 February 2003,
which broke apart during reentry
after a piece of insulating foam
breached the leading edge
of the left wing's thermal protection system,
killed another seven.
The Columbia Accident Investigation Board concluded
that NASA had failed to learn many
of the organizational lessons
from the Challenger disaster.

These losses profoundly influenced
the subsequent direction of spaceflight.
After Challenger,
NASA removed commercial satellite payloads
from the Shuttle manifest
and redirected them to expendable launch vehicles.
After Columbia,
the decision was made to retire the Shuttle fleet entirely.
Crew transport to the International Space Station
shifted first to Russian Soyuz vehicles
and later to commercially operated spacecraft.
Both disasters accelerated the broader trend
toward separating crew transport from cargo delivery
and toward greater use of uncrewed vehicles.

## The Modern Era

### SpaceShipOne, 2004

On 21 June 2004,
the test pilot Mike Melvill
flew [SpaceShipOne][ref_spaceship_one]
to an altitude of 100,124 meters,
completing the first privately funded
crewed spaceflight in history.
The vehicle was designed by Burt Rutan
of Scaled Composites
and funded by Microsoft co-founder Paul Allen,
who invested approximately 25 million dollars.

SpaceShipOne was carried to approximately 15,000 meters
by White Knight,
a custom turbofan-powered carrier aircraft,
and then released for a rocket-powered climb.
The hybrid rocket motor
burned a mixture of nitrous oxide and rubber,
providing approximately 76 seconds of thrust.

SpaceShipOne introduced
the "feathered" reentry technique,
in which the rear half of the wings
and twin tail booms
folded upward approximately 70 degrees along a hinge.
This increased drag
and provided inherent aerodynamic stability
during reentry,
functioning like a badminton shuttlecock.
The system removed most of the need
to actively control attitude during early reentry.
After deceleration,
the pilot retracted the feather
and glided to a conventional runway landing.

SpaceShipOne won
the [Ansari X Prize][ref_ansari_x_prize],
a 10-million-dollar competition
requiring a non-government organization
to launch a reusable crewed spacecraft above 100 kilometers
twice within two weeks.
Mike Melvill flew the first qualifying flight
to 102,900 meters on 29 September 2004.
Brian Binnie flew the second
to 112,000 meters on 4 October 2004,
surpassing the X-15's altitude record.
The prize was won on the 47th anniversary
of the launch of Sputnik 1.

### SpaceShipTwo and Virgin Galactic

[SpaceShipTwo][ref_spaceship_two]
was the commercial successor to SpaceShipOne,
designed to carry six passengers
on suborbital spaceflights
for Richard Branson's Virgin Galactic.
The vehicle used the same feathered reentry concept
but was significantly larger
and was carried to altitude
by a purpose-built twin-fuselage carrier aircraft
called WhiteKnightTwo.

On 31 October 2014,
the first SpaceShipTwo vehicle, VSS Enterprise,
suffered a catastrophic in-flight breakup
during a powered test flight
and crashed in the Mojave Desert.
Co-pilot Michael Alsbury was killed.
Pilot Peter Siebold was seriously injured but survived.
The National Transportation Safety Board determined
that the breakup was caused
by Alsbury's premature unlocking
of the feathering mechanism.
Contributing factors included
the absence of a mechanical inhibit
preventing premature feather unlock
and insufficient pilot training
on the unlock procedure.

A second vehicle, VSS Unity,
completed the first commercial flight
on 29 June 2023,
designated Galactic 01.
Virgin Galactic subsequently retired the vehicle
after completing several additional commercial flights.

### Blue Origin New Shepard

[Blue Origin's New Shepard][ref_new_shepard]
represents a fundamentally different
design philosophy from the winged rocketplanes
discussed throughout this article.
New Shepard is a vertical-takeoff,
vertical-landing suborbital system
consisting of a reusable booster rocket
and a detachable crew capsule.
The capsule has no wings,
no aerodynamic control surfaces,
and returns to Earth under parachutes
rather than gliding to a runway.

The first crewed flight
occurred on 20 July 2021,
the 52nd anniversary of the Apollo 11 Moon landing.
The crew included Blue Origin founder Jeff Bezos,
his brother Mark Bezos,
the Mercury 13 pilot Wally Funk
who at age 82 became
the oldest person to fly in space at that time,
and the Dutch student Oliver Daemen
who at age 18 became the youngest.

New Shepard is included in this history
not as a rocketplane
but as a point of contrast.
Its capsule-on-a-rocket architecture
represents an alternative evolutionary path
for suborbital crewed spaceflight,
one that prioritizes simplicity and autonomy
over the aerodynamic sophistication
of winged reentry vehicles.

### Boeing X-37B

The [Boeing X-37B][ref_x37b]
is an uncrewed orbital spaceplane
that carries the X-plane designation,
placing it directly in the lineage
that began with the Bell X-1 in 1947.
The program originated as a NASA project in 1999,
was transferred to the Defense Advanced Research Projects Agency,
or DARPA, in 2004,
and subsequently to the Air Force
when NASA determined
that the uncrewed reusable spacecraft
did not align with its exploration objectives.
The vehicle is now operated
by the United States Space Force.

The X-37B is a 120-percent scaled derivative
of the earlier Boeing X-40,
built as part of the Air Force's
Space Maneuver Vehicle program.
It launches vertically atop an expendable rocket,
operates in orbit for extended durations,
and returns to a conventional runway landing.

The first orbital mission launched
on 22 April 2010.
Since then, mission durations have grown progressively.
The sixth mission, launched in 2020,
set the endurance record at 908 days in orbit.
All X-37B missions are classified.

The X-37B represents the application
of the X-plane tradition to autonomous orbital operations.
It demonstrates
that a lifting body spaceplane
can operate entirely without a crew,
conducting long-duration orbital missions
and returning to a precision runway landing
under automated control.

### Dream Chaser

[Dream Chaser][ref_dream_chaser],
developed by Sierra Space,
traces its lifting body design
directly to the HL-20 Personnel Launch System
studied at NASA Langley Research Center
in the late 1980s and 1990s.
The HL-20 was itself based
on the Soviet BOR-4 subscale orbital test vehicle
that Western intelligence agencies
photographed in 1983.
The broader lifting body heritage
extends through over 20,000 hours
of research and testing,
including the X-20 Dyna-Soar,
the M2-F2, M2-F3, HL-10,
X-24A, X-24B, and X-23 PRIME vehicles.

Dream Chaser was selected
under NASA's Commercial Resupply Services 2 contract
to deliver cargo
to the International Space Station.
The vehicle is designed to be reusable
for up to 15 missions
and can land on conventional runways.
As of late 2025,
the first demonstration flight
has been delayed to no earlier than late 2026.

Dream Chaser's design lineage
embodies the circular nature
of rocketplane technology transfer.
Soviet intelligence about the American Shuttle
informed the Buran program.
The Spiral program's BOR-4 test vehicle,
photographed by Western intelligence,
informed the HL-20 at NASA Langley.
The HL-20 became Dream Chaser.
Three decades of intelligence and counter-intelligence
thus contributed to a commercial cargo vehicle
intended to serve an international space station
operated jointly by nations
that were once adversaries.

### Dawn Mk-II Aurora

The [Dawn Mk-II Aurora][ref_dawn_aurora],
developed by Dawn Aerospace
in New Zealand and the Netherlands,
represents the newest generation of rocketplanes.
On 12 November 2024,
the Aurora broke the sound barrier on its 57th flight,
reaching Mach 1.1
and an altitude of 25,000 meters.
It became the first aircraft
designed and manufactured in New Zealand
to exceed the speed of sound.

The Aurora is an uncrewed, remotely piloted vehicle
with a wingspan of approximately 4 meters
and a dry weight of approximately 399 kilograms.
It is powered by a rocket engine
burning 90 percent hydrogen peroxide and kerosene.
The vehicle takes off from and lands on
conventional runways as short as 1,000 meters,
and the company has demonstrated
a turnaround time of approximately six hours
between flights.

The significance of the Aurora
lies not in its speed or altitude,
which are modest by rocketplane standards,
but in its operational tempo.
Where every rocketplane in this history
required days or weeks of preparation
between flights,
the Aurora is designed
for routine, rapid-turnaround operations
from conventional airports.
Commercial payload flights to 100 kilometers
are projected to begin in 2027.

## Conclusion

The history of rocketplanes
is a single narrative thread
spanning nearly a century.
It begins with Fritz Stamer
firing two black powder rockets
on a modified sailplane in 1928
and continues through autonomous orbital vehicles
and commercially operated spaceplanes today.

Five themes weave through this narrative.
The first is the German pioneering work
of the 1920s through the 1940s,
in which Lippisch, Sander, Opel, Heinkel,
Walter, and Messerschmitt
established the fundamental design vocabulary
of rocket-powered flight.
The second is technology capture and espionage,
through which Operation Paperclip and Operation Osoaviakhim
transferred German expertise to both superpowers,
and through which the Silbervogel concept
independently influenced
American and Soviet spaceplane programs
for decades.
The third is the systematic American X-plane program,
in which each vehicle built directly
on the achievements and failures of its predecessor,
progressing methodically
from Mach 1 in 1947 to Mach 6.7 in 1967.
The fourth is the state-level pinnacle
of the Space Shuttle and Buran,
the largest and most complex rocketplanes ever built,
which demonstrated
both the possibilities and the costs
of large-scale government spaceplane programs.
The fifth is the modern era of privatization,
in which commercial companies
are pursuing rocketplane technology
with fundamentally different cost structures,
operational models,
and risk tolerances
than the government programs that preceded them.

Connecting all five themes
is the continuous thread
of institutional knowledge and individuals.
Lippisch's tailless designs
led to the Me 163.
Dornberger moved from V-2 to Bell Aircraft
to the X-15 and Dyna-Soar.
The X-15's data informed the Shuttle.
Soviet photographs of American hardware
informed Buran.
Western photographs of Soviet hardware
informed Dream Chaser.
At every transition,
the knowledge accumulated by one program
became the foundation for the next.

The convergence of reusable vehicles,
autonomous systems,
and commercial operations
in the modern era suggests
that the century-long arc of rocketplane development
is entering a new phase.
The fundamental engineering challenges
of rocket-powered atmospheric and orbital flight
have been solved.
The remaining challenge
is to make routine
what was once extraordinary.

## Future Reading

- [Smithsonian National Air and Space Museum][ref_nasm],
  extensive historical collections
  and editorial resources on the history of flight,
  including detailed artifact pages
  for many of the vehicles discussed in this article.

- [NASA Armstrong Flight Research Center][ref_nasa_armstrong],
  the primary United States facility
  for atmospheric flight research
  and the operational base
  for the X-1, X-2, X-15, lifting body,
  and X-37B programs.

- [The Right Stuff][book_right_stuff]
  by Tom Wolfe,
  a narrative account of the early X-plane era
  and the selection of the Mercury Seven astronauts,
  centered on Edwards Air Force Base
  and the test pilots who flew the X-1, X-2, and X-15.

- [X-15 Research Results][research_x15_results],
  NASA Special Publication SP-60,
  a comprehensive technical summary
  of the aerodynamic, structural, thermal,
  and handling qualities data
  obtained from the X-15 flight program.

- [Buran — The Soviet Shuttle][ref_buran_nasm],
  the Smithsonian National Air and Space Museum
  editorial resource on the Buran program,
  covering its development, flight,
  and relationship to the American Space Shuttle.

## References

- [Book, At the Edge of Space by Milton Thompson][book_edge_space]
- [Book, Dyna-Soar by Roy Houchin][book_dyna_soar]
- [Book, Skunk Works by Ben Rich][book_skunk_works]
- [Book, The Right Stuff by Tom Wolfe][book_right_stuff]
- [Reference, Ansari X Prize][ref_ansari_x_prize]
- [Reference, Bachem Ba 349 Natter][ref_ba_349]
- [Reference, Bell X-1][ref_bell_x1]
- [Reference, Bell X-1A][ref_bell_x1a]
- [Reference, Bell X-1B][ref_bell_x1b]
- [Reference, Bell X-2 Starbuster][ref_bell_x2]
- [Reference, Bereznyak-Isayev BI-1][ref_bi_1]
- [Reference, Blue Origin New Shepard][ref_new_shepard]
- [Reference, Boeing X-20 Dyna-Soar][ref_x20]
- [Reference, Boeing X-37B][ref_x37b]
- [Reference, Buran Programme][ref_buran]
- [Reference, Dawn Aerospace][ref_dawn_aurora]
- [Reference, DFS 194][ref_dfs_194]
- [Reference, Douglas D-558-2 Skyrocket][ref_d558_2]
- [Reference, Dream Chaser][ref_dream_chaser]
- [Reference, Heinkel He 176][ref_he_176]
- [Reference, Lippisch Ente][ref_lippisch_ente]
- [Reference, Alexander Lippisch][ref_lippisch]
- [Reference, Martin X-24][ref_x24]
- [Reference, Messerschmitt Me 163 Komet][ref_me_163]
- [Reference, MiG-105 Spiral][ref_mig_105]
- [Reference, NASA Armstrong Flight Research Center][ref_nasa_armstrong]
- [Reference, North American X-15][ref_x15]
- [Reference, Opel RAK.1][ref_opel_rak1]
- [Reference, Operation Osoaviakhim][ref_osoaviakhim]
- [Reference, Operation Paperclip][ref_paperclip]
- [Reference, Silbervogel][ref_silbervogel]
- [Reference, Smithsonian NASM][ref_nasm]
- [Reference, Smithsonian NASM Buran][ref_buran_nasm]
- [Reference, Smithsonian NASM Me 163][ref_nasm_me163]
- [Reference, Space Shuttle Program][ref_shuttle]
- [Reference, Space Shuttle Atlantis][ref_atlantis]
- [Reference, Space Shuttle Challenger][ref_challenger]
- [Reference, Space Shuttle Columbia][ref_columbia]
- [Reference, Space Shuttle Discovery][ref_discovery]
- [Reference, Space Shuttle Endeavour][ref_endeavour]
- [Reference, SpaceShipOne][ref_spaceship_one]
- [Reference, SpaceShipTwo][ref_spaceship_two]
- [Reference, Walter Dornberger][ref_dornberger]
- [Reference, Walter HWK 109-509][ref_walter_hwk]
- [Reference, Yokosuka MXY-7 Ohka][ref_ohka]
- [Related Post, Introduction to Space Studies][related_post_space_studies]
- [Research, NASA SP-60 X-15 Research Results][research_x15_results]
- [Research, NASA X-15 Space Pioneers Honored as Astronauts][research_x15_astronauts]
- [Research, Smithsonian NASM Paperclip and American Rocketry][research_nasm_paperclip]
- [Research, Sutton-Graves 1971 Stagnation-Point Convective Heating][research_sutton_graves]

[book_edge_space]: https://books.google.com/books/about/At_the_Edge_of_Space.html?id=9dtTAAAAMAAJ
[book_dyna_soar]: https://books.google.com/books?id=V7N-AgAAQBAJ
[book_right_stuff]: https://en.wikipedia.org/wiki/The_Right_Stuff_(book)
[book_skunk_works]: https://books.google.com/books/about/Skunk_Works.html?id=MAHoAAAACAAJ
[ref_ansari_x_prize]: https://en.wikipedia.org/wiki/Ansari_X_Prize
[ref_atlantis]: https://en.wikipedia.org/wiki/Space_Shuttle_Atlantis
[ref_ba_349]: https://en.wikipedia.org/wiki/Bachem_Ba_349
[ref_bell_x1]: https://en.wikipedia.org/wiki/Bell_X-1
[ref_bell_x1a]: https://en.wikipedia.org/wiki/Bell_X-1A
[ref_bell_x1b]: https://en.wikipedia.org/wiki/Bell_X-1#X-1B
[ref_bell_x2]: https://en.wikipedia.org/wiki/Bell_X-2
[ref_bi_1]: https://en.wikipedia.org/wiki/Bereznyak-Isayev_BI-1
[ref_buran]: https://en.wikipedia.org/wiki/Buran_programme
[ref_buran_nasm]: https://airandspace.si.edu/stories/editorial/soviet-buran-shuttle-one-flight-long-history
[ref_challenger]: https://en.wikipedia.org/wiki/Space_Shuttle_Challenger
[ref_columbia]: https://en.wikipedia.org/wiki/Space_Shuttle_Columbia
[ref_d558_2]: https://en.wikipedia.org/wiki/Douglas_D-558-2_Skyrocket
[ref_dawn_aurora]: https://en.wikipedia.org/wiki/Dawn_Aerospace
[ref_dfs_194]: https://en.wikipedia.org/wiki/DFS_194
[ref_discovery]: https://en.wikipedia.org/wiki/Space_Shuttle_Discovery
[ref_dornberger]: https://en.wikipedia.org/wiki/Walter_Dornberger
[ref_dream_chaser]: https://en.wikipedia.org/wiki/Dream_Chaser
[ref_endeavour]: https://en.wikipedia.org/wiki/Space_Shuttle_Endeavour
[ref_he_176]: https://en.wikipedia.org/wiki/Heinkel_He_176
[ref_lippisch]: https://en.wikipedia.org/wiki/Alexander_Lippisch
[ref_lippisch_ente]: https://en.wikipedia.org/wiki/Lippisch_Ente
[ref_me_163]: https://en.wikipedia.org/wiki/Messerschmitt_Me_163_Komet
[ref_mig_105]: https://en.wikipedia.org/wiki/Mikoyan-Gurevich_MiG-105
[ref_nasa_armstrong]: https://www.nasa.gov/centers-and-facilities/armstrong/
[ref_nasm]: https://airandspace.si.edu/
[ref_nasm_me163]: https://airandspace.si.edu/collection-objects/messerschmitt-me-163b-1a-komet/nasm_A19530072000
[ref_new_shepard]: https://en.wikipedia.org/wiki/New_Shepard
[ref_ohka]: https://en.wikipedia.org/wiki/Yokosuka_MXY-7_Ohka
[ref_opel_rak1]: https://en.wikipedia.org/wiki/Opel_RAK.1
[ref_osoaviakhim]: https://en.wikipedia.org/wiki/Operation_Osoaviakhim
[ref_paperclip]: https://en.wikipedia.org/wiki/Operation_Paperclip
[ref_shuttle]: https://en.wikipedia.org/wiki/Space_Shuttle_program
[ref_silbervogel]: https://en.wikipedia.org/wiki/Silbervogel
[ref_spaceship_one]: https://en.wikipedia.org/wiki/SpaceShipOne
[ref_spaceship_two]: https://en.wikipedia.org/wiki/SpaceShipTwo
[ref_walter_hwk]: https://en.wikipedia.org/wiki/Walter_HWK_109-509
[ref_x15]: https://en.wikipedia.org/wiki/North_American_X-15
[ref_x20]: https://en.wikipedia.org/wiki/Boeing_X-20_Dyna-Soar
[ref_x24]: https://en.wikipedia.org/wiki/Martin_Marietta_X-24
[ref_x37b]: https://en.wikipedia.org/wiki/Boeing_X-37
[related_post_space_studies]: {% post_url 2026-02-21-introduction_to_space_studies %}
[research_nasm_paperclip]: https://airandspace.si.edu/stories/editorial/project-paperclip-and-american-rocketry-after-world-war-ii
[research_sutton_graves]: https://ntrs.nasa.gov/citations/19720003329
[research_x15_astronauts]: https://www.nasa.gov/news-release/x-15-space-pioneers-now-honored-as-astronauts/
[research_x15_results]: https://ntrs.nasa.gov/citations/19720005025
