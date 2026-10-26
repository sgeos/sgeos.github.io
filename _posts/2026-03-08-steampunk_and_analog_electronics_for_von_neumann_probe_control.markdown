---
layout: post
mathjax: true
comments: true
title:  "Steampunk and Analog Electronics for Von Neumann Probe Control"
date:   2026-03-08 14:23:00 +0000
categories: science philosophy
series: intergalactic_competition
series_title: Intergalactic Competition
series_index: 7
---
<!-- A104 -->
<script>console.log("A104");</script>

The companion articles on
[von Neumann probes][related_post_von_neumann_probes]
and the
[error correction recursion problem][related_post_error_correction]
identified semiconductor fabrication
as the single hardest closure gap
for self-replicating spacecraft.
Modern integrated circuits
require silicon of 99.9999999 percent purity,
photolithography equipment
with nanometer resolution,
and clean room environments.
No pathway exists
for manufacturing modern processors
from raw ore
in an autonomous extraterrestrial facility.

This article examines
an alternative approach.
Rather than solving
the semiconductor fabrication problem,
a von Neumann probe
might sidestep it entirely
by using computing technologies
that predate the transistor.
Mechanical computers,
analog electronic circuits,
and hybrid systems
combining the two
have manufacturing requirements
that are orders of magnitude
less demanding
than semiconductor fabrication.
The tolerances are wider.
The materials are simpler.
The processes are more forgiving.

The objective is functional closure,
not technological parity.
A von Neumann probe
does not need
to replicate a modern microprocessor.
It needs to replicate
the computing capability
required for its functions.
The trade-off is performance.
Mechanical and analog systems
are slower,
larger,
and less energy-efficient
per computation
than modern digital electronics.
But a von Neumann probe
does not need
to run a web browser
or train a neural network.
It needs to control
a manufacturing process,
navigate between stars,
store and retrieve
engineering blueprints
and manufacturing procedures,
and manage quality assurance
across replication generations.
These tasks may be achievable
with computing technologies
from the 1940s,
manufactured with techniques
from the 1800s,
using materials available
on any rocky body
in the solar system.

The central architectural thesis
of this article
is that a practical probe
distributes computation
across three technological layers.
Mechanical control handles
robust low-level actuation and sensing,
including governors, cams,
and fluidic logic.
Analog computation handles
continuous signal processing
and feedback control,
including vacuum tube amplifiers
and operational amplifier circuits.
A minimal digital core handles
planning, communications encoding,
error detection and correction,
and limited symbolic reasoning.
Each layer has progressively
more demanding manufacturing requirements,
but each layer also handles
a progressively smaller share
of the total computing workload.
Distributing computation
across these three layers
reduces the semiconductor closure gap
from a system-wide impossibility
to a narrow constraint
on a single subsystem.

This article defines three categories
of alternative computing technology,
surveys their historical development
and current capabilities,
and evaluates their suitability
for von Neumann probe control systems.
The first category is steampunk electronics,
encompassing mechanical and fluidic computing.
The second is analog electronics,
encompassing vacuum tubes
and continuous-signal processing.
The third is analog steampunk electronics,
encompassing hybrid systems
that combine mechanical
and analog electronic elements.

For each category,
the article traces
the historical origins,
identifies key implementations,
assesses the current state of the art,
reviews contemporary applications,
defines the performance requirements
for von Neumann probes,
compares the state of the art
to those requirements,
surveys work in progress,
and proposes hypothetical approaches
that might meet probe requirements.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-03-08 14:23:00 +0000
```

## Steampunk Electronics

The term "steampunk electronics"
as used in this article
refers to computing and control systems
that operate through mechanical,
pneumatic, or fluidic means
without requiring electrical components.
These systems perform logical
and arithmetic operations
using physical mechanisms
such as gears, cams, levers,
fluid jets, and pressure differentials.
The defining characteristic
is that the information carrier
is a physical displacement
or a fluid flow
rather than an electrical signal.

### Historical Origins

The earliest automatic control systems
predate electronics by centuries.
Mechanical control
is the foundation
of autonomous machine operation.

**Governors and feedback control.**
James [Watt][ref_watt_governor]'s
centrifugal governor,
adapted for steam engines
in the 1780s,
is the canonical example
of mechanical feedback control.
The governor senses engine speed
through the centrifugal force
on spinning weights.
As speed increases,
the weights fly outward,
closing a throttle valve
to reduce steam flow.
The system regulates speed
without any electronics,
any human intervention,
or any awareness
of the concept
of feedback control theory.
Centrifugal governors
remained the primary speed regulators
for prime movers
throughout the Industrial Revolution
and into the twentieth century.
Modern turbine governors
use the same principle.
For a von Neumann probe,
mechanical governors demonstrate
that autonomous process regulation
is achievable
with the simplest
of manufacturing techniques.

**Cams and cam-timed machines.**
[Cam][ref_cam] mechanisms
convert rotary motion
into precisely timed
linear or oscillating motion.
Cam-timed machines
execute complex manufacturing sequences
through the geometry
of a rotating cam shaft,
with each cam lobe
triggering an operation
at a point in the cycle.
Automatic screw machines,
which have manufactured
precision threaded fasteners
since the late nineteenth century,
use cam-timed sequences
to perform turning, drilling, tapping,
and cutoff operations
without human intervention.
The manufacturing program
is encoded
in the physical shape
of the cam.
No electronics are required.
No software is required.
The program is its own hardware.

**Differential gears and mechanical computation.**
[Differential gear][ref_differential_gear] mechanisms
perform addition and subtraction
of rotational displacements.
Lord Kelvin proposed
using differential gears
for mechanical integration
in the 1870s,
a concept later realized
in Vannevar Bush's
differential analyzer.
[Ball-and-disk integrators][ref_ball_disk_integrator]
perform continuous integration
by varying the radius
at which a rotating disk
drives a ball,
which in turn drives
an output disk.
[Planimeters][ref_planimeter]
compute the area
enclosed by a curve
through mechanical integration.
These devices demonstrate
that calculus-level operations,
integration
and differentiation,
are achievable
with purely mechanical systems.

**Hydraulic and pneumatic actuation.**
Hydraulic [servo mechanisms][ref_servomechanism]
amplify small control signals
into large output forces
using pressurized fluid.
A hydraulic servo
can position a multi-ton load
with millimeter precision
based on a mechanical
or pneumatic input signal.
These systems are attractive
for long-term autonomous operation
because they tolerate radiation well,
require no semiconductor components,
and can be repaired or reproduced
using relatively primitive
industrial processes.
Their failure modes
are primarily mechanical wear,
which is gradual
and predictable
rather than sudden
and catastrophic.

**Programmable mechanical systems.**
The [Jacquard loom][ref_jacquard_loom],
developed by Joseph Marie Jacquard in 1804,
used punched cards
to control the weaving pattern
of a textile loom.
Each card encoded one row
of the pattern.
The sequence of cards
constituted a stored program.
The Jacquard loom demonstrated
that complex manufacturing processes
could be controlled
by a mechanical program
without human intervention at each step.

[Charles Babbage][ref_babbage]
designed the [Difference Engine][ref_difference_engine] in the 1820s
and the [Analytical Engine][ref_analytical_engine]
beginning in 1837.
The Difference Engine
was a special-purpose calculator
for polynomial evaluation
using the method of finite differences.
The Analytical Engine
was a general-purpose
mechanical computer
with an arithmetic logic unit,
control flow through conditional branching,
and memory.
[Ada Lovelace][ref_ada_lovelace]
wrote the first algorithm
intended for machine execution
for the Analytical Engine in 1843.
Babbage's designs
were never fully constructed
in his lifetime
due to the manufacturing precision
required by the designs.
A working Difference Engine No. 2
was completed
by the [Science Museum][ref_science_museum] in London
in 1991,
demonstrating that Babbage's design
was mechanically sound.

[Konrad Zuse][ref_zuse]
built the [Z1][ref_z1]
in 1938,
a mechanical binary computer
using sliding metal plates
as logic gates.
The Z1 was unreliable
due to manufacturing tolerances
in the mechanical components.
Zuse subsequently built
the Z3 in 1941
using electromechanical relays,
which was the first
working programmable,
fully automatic digital computer.

Relay-based computers
followed in the 1940s.
The [Harvard Mark I][ref_harvard_mark_i],
completed in 1944,
used electromechanical relays
and rotating shafts
for computation.
The Bell Labs relay computers,
including the Model I through Model VI,
performed complex mathematical calculations
using telephone switching relays.
These machines demonstrated
that general-purpose digital computation
is achievable
with mechanical switching elements.

### Fluidic Computing

In 1959,
Billy M. Horton
of the Harry Diamond Laboratories,
a U.S. Army research facility,
discovered that fluid jets
could be used
as amplifiers and logic elements
without any moving parts.
Horton and his colleagues,
R.E. Bowles and Ray Warren,
exploited the [Coanda effect][ref_coanda_effect],
in which a fluid jet
attaches to a nearby wall
and can be deflected
by a small control jet.
This discovery launched
the field of [fluidics][ref_fluidics].

Fluidic logic gates
implement Boolean operations
using fluid streams.
An OR gate passes flow
if either input jet is active.
An AND gate passes flow
only if both input jets
are active simultaneously.
A NOT gate deflects
a supply jet away from the output
when a control jet is applied.
Flip-flop memory elements
store a single bit of state
by maintaining a jet
attached to one of two walls.
All of these operations
are performed
with no moving parts
and no electrical components.

The [FLODAC][ref_flodac] computer,
built by Univac in 1964,
was a proof-of-concept
fluidic digital computer.
FLODAC demonstrated
that a complete digital computer
could be constructed
entirely from fluid logic elements.
The system was slow
compared to electronic computers
of the same era,
but it operated
without any electronic components.

Fluidic systems
found practical application
in environments
hostile to electronics.
[Nuclear reactor][ref_nuclear_reactor] shutdown systems
have used fluidic vortex valves
to control neutron poison flow,
relying on fluid logic
rather than electronic sensors
that could fail
under intense radiation.
Industrial process control systems
in explosive atmospheres
used pneumatic logic controllers
operating at the 3 to 15 psi
industry standard signal range.
These pneumatic controllers
implemented proportional-integral-derivative
control loops
entirely through fluid pressure,
without any electrical components.

### Key Historical Examples

**The Antikythera mechanism.**
Discovered in a Roman-era shipwreck in 1901,
the [Antikythera mechanism][ref_antikythera]
is an ancient Greek analog computer
dating to approximately 100 BCE.
It used approximately 30 bronze gears
to predict astronomical positions
and eclipses.
The mechanism demonstrates
that useful computation
is achievable with simple materials
and pre-industrial manufacturing techniques.

**Lord Kelvin's tide-predicting machine.**
William Thomson designed the first
[tide-predicting machine][ref_tide_predictor]
in 1872 to 1873.
The machine summed ten tidal components
using pulley-and-crank mechanisms,
predicting tidal heights
at any port
by continuously computing
the superposition
of sinusoidal harmonics.
Later versions summed
up to 24 components.
A year of tidal predictions
could be plotted in four hours.
Tide-predicting machines
remained in operational use
through the 1960s,
including service
during the planning
of the D-Day invasion.
These machines demonstrate
that mechanical systems
can perform Fourier synthesis,
a mathematical operation
directly relevant
to signal processing
and trajectory computation.

**Mechanical fire control computers.**
From the 1920s through the 1940s,
naval fire control systems
used mechanical analog computers
to calculate firing solutions.
The [Mark 37 Fire Control System][ref_mark_37],
used by the United States Navy
in World War II,
computed lead angles,
range corrections,
and ballistic trajectories
using cams, gears,
and differential analyzers.
The United States Navy's
electromechanical [rangekeepers][ref_rangekeeper]
served in combat
from World War II
through the 1991 Persian Gulf War,
demonstrating
that analog fire control computers
are serviceable
for decades
with appropriate maintenance.
These systems performed
real-time computation
in combat conditions
aboard ships subject
to vibration, temperature extremes,
and salt spray.

**Pneumatic industrial controllers.**
The Foxboro 43P controller,
introduced in the 1940s,
was a widely deployed
pneumatic PID controller
that regulated industrial processes
using compressed air signals.
Pneumatic controllers dominated
industrial process control
from the 1940s through the 1970s.
Thousands remain in service today
in refineries, chemical plants,
and other facilities
where intrinsic safety
or explosion-proof operation
is required.

### Current State of the Art

**MEMS logic gates.**
[Micro-Electro-Mechanical Systems][ref_mems], or MEMS,
represent the modern frontier
of mechanical computing.
MEMS devices fabricate
microscopic mechanical structures
on silicon wafers
using lithographic techniques
similar to those used
for semiconductor fabrication,
but with much wider tolerances.

[Tabib-Azar, Chowdhury, and Saab][research_tabib_azar]
at the University of Utah
demonstrated MEMS-based logic gates
that withstand intense ionizing radiation.
They lowered MEMS logic gates
into the core
of the university's 90-kilowatt
TRIGA research reactor
for two hours
while monitoring their operation.
The gates did not fail.
The researchers also operated
the gates for more than two months
and over one billion cycles
without failure.
These MEMS logic gates
implement Boolean operations
using microscopic cantilever beams
that make or break
electrical contact.
The key innovation was reducing
the gap between contacts
to allow activation
at only 1.5 volts,
compared to the 10 to 20 volts
required by earlier MEMS switches.

**Mechanical metamaterials.**
Recent research has explored
mechanical metamaterials
that can perform
logic operations
through their physical deformation.
These materials encode
input and output states
in the displacement
of structural elements,
achieving Boolean logic
without any electrical
or fluidic components.

**Microfluidic computing.**
Modern microfluidic devices
miniaturize the fluidic logic
pioneered in the 1960s.
Lab-on-a-chip systems
use microscale channels
and droplet manipulation
to perform logical operations
and control sequences.
While primarily developed
for biological and chemical applications,
the underlying principles
are directly applicable
to miniaturized fluidic computers.

### Contemporary Applications

Fluidic and mechanical computing
find application today
in environments
where electronic systems
are unreliable or prohibited.

**Nuclear environments.**
Fluidic sensing and control systems
operate in nuclear facilities
where radiation levels
would destroy semiconductor electronics.
Fluidic vortex valves
serve as safety shutdown mechanisms
in nuclear reactors.

**Explosive atmospheres.**
Pneumatic controllers
remain in service
in petroleum refineries,
chemical plants,
and mining operations
where electrical sparks
could ignite flammable atmospheres.
These environments require
intrinsically safe systems
that carry no electrical energy.

**Extreme temperatures.**
Mechanical systems
can operate at temperatures
that exceed the limits
of semiconductor devices.
Silicon-based electronics
typically fail above 200 degrees Celsius.
Mechanical components
made from appropriate alloys
can operate at much higher temperatures.

### Von Neumann Probe Requirements

A von Neumann probe
requires computing capability
for the following functions.

**Manufacturing process control.**
Controlling the temperature,
pressure, feed rate,
and tool position
of manufacturing equipment.
These are control loop tasks
analogous to industrial process control,
requiring cycle times
on the order of milliseconds
to seconds.

**Quality assurance.**
Measuring manufactured components
against specifications
and accepting or rejecting them.
This requires comparison operations
and threshold detection,
achievable with analog comparators.

**Navigation.**
Computing trajectory corrections
during interstellar transit.
These calculations
are infrequent
and can tolerate latencies
on the order of hours or days.

**Communication.**
Encoding and decoding
error-corrected communication signals.
This is the most computationally
demanding function
and the one most difficult
to achieve
with mechanical or fluidic computing.

**Self-diagnostics.**
Monitoring system health
and detecting failures.
This is primarily
a sensing and comparison task.

### Comparison to Requirements

Mechanical and fluidic computing
can meet the requirements
for manufacturing process control,
quality assurance,
navigation,
and self-diagnostics.
Pneumatic PID controllers
have controlled industrial manufacturing
for decades.
Mechanical analog computers
computed ballistic trajectories
in real time.
Fluidic systems
have operated reliably
in nuclear environments
where electronic systems fail.

The primary limitation
is computational throughput.
A mechanical computer
operating at 10 hertz
can perform perhaps 10 operations per second.
A fluidic computer
might achieve 100 to 1,000
operations per second.
Modern digital processors
operate at billions
of operations per second.
The gap is approximately
six to nine orders of magnitude.

For a von Neumann probe,
this throughput limitation
constrains what tasks
can be performed mechanically.
Manufacturing process control,
which operates on timescales
of seconds to minutes,
is well within reach.
Error-corrected digital communication,
which requires
millions of operations per second,
is not feasible
with purely mechanical
or fluidic systems.

The manufacturing advantage
is substantial.
Mechanical components
can be fabricated
from common metals and alloys
with tolerances
on the order of micrometers.
No clean room is required.
No ultra-pure materials are needed.
The manufacturing chain
for mechanical computing
is orders of magnitude simpler
than the manufacturing chain
for semiconductor fabrication.

### Work in Progress

**Radiation-hardened MEMS.**
The University of Utah work
on radiation-resistant MEMS logic gates
is the most directly relevant
current research.
MEMS devices combine
the radiation immunity
of mechanical switching
with fabrication techniques
that achieve microscopic feature sizes.
The challenge is scaling
from individual logic gates
to complete computing systems.

**Microfluidic logic at scale.**
Research groups
are developing increasingly complex
microfluidic circuits
for lab-on-a-chip applications.
These circuits implement
multiplexers, demultiplexers,
and sequential logic
using droplet-based computation.
The techniques could be adapted
for control system applications
in environments
hostile to electronics.

**3D-printed fluidic devices.**
Additive manufacturing
enables the fabrication
of complex fluidic channels
and logic elements
in a single print operation.
This is directly relevant
to von Neumann probes,
which are expected
to use additive manufacturing
as a primary fabrication method.

### Hypothetical Approaches

**A fluidic manufacturing controller.**
A von Neumann probe
could use a fluidic computer
to control its manufacturing processes.
The computer would implement
PID control loops
for temperature regulation,
pressure control,
and feed rate management.
The fluidic controller
would be manufactured
from the same metal alloys
used for the probe's structural components,
requiring no specialized materials
beyond what is already needed
for the mechanical systems.

**A MEMS-based navigation computer.**
MEMS logic gates
arrayed in sufficient quantity
could implement
the arithmetic operations
needed for trajectory computation.
A MEMS computer
with $10^4$ logic gates
operating at $10^3$ hertz
could perform approximately
$10^4$ operations per second,
sufficient for navigation calculations
that require minutes to hours
of computation time
per trajectory update.

**Hierarchical computing architecture.**
The most promising approach
may be a hierarchical system
in which low-level control loops
are implemented in fluidic
or mechanical hardware,
while higher-level computations
are handled by more capable
but harder-to-manufacture systems.
This architecture
concentrates the semiconductor closure gap
on a small number
of high-capability components
while using manufacturable technologies
for the bulk
of the computing workload.

## Analog Electronics

Steampunk electronics
provide the manufacturing foundation
for a self-replicating probe,
but their limited throughput
constrains them
to low-level control tasks.
The next layer
in the architectural hierarchy
is analog electronics,
which adds amplification,
signal conditioning,
and substantially higher
computational bandwidth
while remaining
far simpler to manufacture
than semiconductor digital systems.

The term "analog electronics"
as used in this article
refers to electronic systems
that process continuously varying signals
rather than discrete digital values.
Analog electronic components
include [vacuum tubes][ref_vacuum_tube],
[operational amplifiers][ref_operational_amplifier],
resistors, capacitors, and inductors.
The defining characteristic
is that the information carrier
is a continuous voltage or current
rather than a discrete binary value.

### Historical Origins

The vacuum tube era
began with [John Ambrose Fleming][ref_fleming_valve]'s
invention of the thermionic diode in 1904
and [Lee de Forest][ref_audion]'s
invention of the triode in 1906.
The triode enabled amplification,
making it possible
to build oscillators,
amplifiers,
and eventually
electronic computers.

[Vannevar Bush][ref_vannevar_bush]
built the first large-scale
analog computer
at the Massachusetts Institute
of Technology in 1931.
The [differential analyzer][ref_differential_analyzer]
used mechanical integrators
driven by electric motors
to solve ordinary differential equations.
Bush's machine
could solve sixth-order
differential equations
in minutes
that would take
a human computer
weeks to solve by hand.

[John R. Ragazzini][research_ragazzini]
coined the term
"[operational amplifier][ref_operational_amplifier]"
in a 1947 paper
published in the Proceedings
of the IRE.
Ragazzini's work formalized
the concept of a high-gain amplifier
that could be configured
by external components
to perform mathematical operations
including addition,
subtraction,
integration,
and differentiation.
The operational amplifier
became the fundamental building block
of electronic analog computers.

The [ENIAC][ref_eniac],
completed in 1945,
used approximately 17,468 vacuum tubes
and consumed 150 kilowatts of power.
While ENIAC was a digital computer,
it demonstrated
that vacuum tube electronics
could perform complex computation
at electronic speeds.
The [MONIAC][ref_moniac],
built by Bill Phillips in 1949,
was a hydraulic analog computer
that modeled the British economy
using colored water flowing
through transparent pipes.
The MONIAC demonstrated
that analog computation
could model complex dynamic systems
with intuitive physical representations.

### Key Historical Examples

**World War II fire control systems.**
The [Norden bombsight][ref_norden_bombsight],
used by the United States Army Air Forces,
was an analog computer
that calculated bomb release points
by integrating aircraft speed,
altitude,
wind velocity,
and target position.
The Mark 37 Gun Fire Control System
combined mechanical differential analyzers
with vacuum tube amplifiers
to track targets and compute
firing solutions in real time.
These systems demonstrated
that analog computation
is adequate for real-time control
of complex physical processes.

**Analog differential equation solvers.**
Analog computers historically
solved differential equations directly.
Rather than discretizing time
and computing numerical approximations
as digital computers do,
analog computers
set up physical circuits
whose voltages evolve
according to the same equations
as the system being modeled.
A circuit built from
operational amplifiers configured
as integrators, summers,
and coefficient multipliers
solves the equation
continuously and in real time.
This approach made analog computers
the preferred tool
for aerospace trajectory computation,
structural vibration analysis,
and nuclear reactor simulation
throughout the 1950s and 1960s.
For a von Neumann probe,
this capability is directly relevant.
Trajectory correction,
thermal management,
and chemical process modeling
are all differential equation problems.

**Early spacecraft guidance.**
The [V-2 rocket][ref_v2_rocket]'s
guidance system,
developed at Peenemunde
in the early 1940s,
used analog electronics
and gyroscopic instruments
for inertial guidance.
The Polaris missile guidance system,
developed in the 1950s,
continued to use analog electronics
for inertial navigation.
The [Saturn V][ref_saturn_v]
instrument unit
used analog signal conditioning
circuits alongside
its digital guidance computer.
Analog computers
were competitive with
early digital computers
for real-time control applications
because they computed
in continuous time
without the overhead
of digital sampling
and quantization.

**Analog neural networks.**
[Frank Rosenblatt][ref_perceptron]'s
[Mark I Perceptron][ref_perceptron],
built at Cornell in 1958,
was an analog electronic device
that implemented
a simple neural network
using potentiometers
for adjustable weights
and motor-driven relays
for threshold functions.
The Perceptron demonstrated
that pattern recognition
is achievable
with analog hardware.

### Current State of the Art

**Modern analog computing revival.**
Several research groups
and companies
are developing analog computing
for applications
where analog offers
advantages over digital.

Analog computing
is experiencing renewed interest
for neural network inference.
Analog matrix-vector multiplication
using resistive crossbar arrays
can perform
the dominant computation
in neural network inference,
matrix multiplication,
in a single step
using Ohm's law
and Kirchhoff's current law.
This approach achieves
energy efficiency improvements
of 10 to 100 times
compared to digital implementations
for the same computation.

**Inherent robustness of analog computation.**
[Lammie et al.][research_lammie]
demonstrated in 2025
that analog in-memory computing chips
based on phase change memory devices
exhibit inherent adversarial robustness.
The stochastic noise
present in analog computation,
which is traditionally viewed
as a disadvantage,
provides natural resistance
to adversarial perturbations.
This finding suggests
that the imprecision of analog systems
may be a feature
rather than a defect
for applications requiring
fault tolerance and robustness.

**Neuromorphic computing.**
[Neuromorphic][ref_neuromorphic] processors
mimic the analog signaling
of biological neurons.
Intel's Loihi chip
and IBM's TrueNorth chip
use analog-inspired circuits
to perform neural computation
with extremely low power consumption.
These chips process information
using spikes and analog voltages
rather than digital arithmetic.

**Vacuum tube manufacturing.**
Vacuum tubes
continue to be manufactured
for audio amplification,
military radar systems,
and specialized high-power applications.
Modern vacuum tube production
exists in Russia, China, Slovakia,
and several smaller manufacturers worldwide.
The manufacturing process
for vacuum tubes
requires glass working,
metal forming,
vacuum pumping,
and cathode coating,
but does not require
the nanometer-scale precision
or ultra-pure materials
demanded by semiconductor fabrication.

The basic materials
for vacuum tube manufacturing
are glass or ceramic
for the envelope,
tungsten or thoriated tungsten
for the filament,
nickel for the cathode sleeve,
and various metals
for the grid and plate structures.
Cathode coatings use
alkaline earth metal oxides,
typically barium oxide,
strontium oxide,
and calcium oxide.
Vacuum tube manufacturing
requires a vacuum pump
capable of achieving pressures
on the order of $10^{-6}$ torr.
While this is demanding,
it is many orders of magnitude
less demanding
than the requirements
for semiconductor clean rooms.

### Contemporary Applications

**High-power radio frequency systems.**
Vacuum tubes remain the technology
of choice for high-power
radio frequency amplification
in radar systems,
particle accelerators,
and broadcast transmitters.
The [klystron][ref_klystron]
and [magnetron][ref_magnetron]
are vacuum tube devices
that generate microwave power
at levels unachievable
by semiconductor devices.

**Audio amplification.**
The vacuum tube audio market
remains active,
with manufacturers producing
tubes for guitar amplifiers,
high-fidelity audio equipment,
and professional audio systems.
This market sustains
ongoing tube manufacturing capability.

**Military and aerospace.**
Vacuum tube technology
retains a niche
in military applications
where [electromagnetic pulse][ref_emp] resistance
is required.
Vacuum tubes are inherently resistant
to the electromagnetic pulse
generated by nuclear detonations,
which can destroy
semiconductor electronics.

### Von Neumann Probe Requirements

The computing requirements
for a von Neumann probe's
analog subsystems
include the following.

**Signal processing.**
Amplifying, filtering,
and conditioning sensor signals
from manufacturing quality control systems,
navigation sensors,
and communication receivers.
Analog electronics
excel at signal processing.

**Control loops.**
Implementing feedback control
for manufacturing processes.
Analog PID controllers
are the historical standard
for this application.

**Power electronics.**
Controlling motors,
heaters, and actuators
in the manufacturing chain.
Vacuum tubes
can serve as power amplifiers
and switches
for these applications.

**Neural computation.**
If the probe requires
any form of adaptive behavior
or pattern recognition,
analog neural network hardware
offers a path
that does not require
digital semiconductor fabrication.

### Comparison to Requirements

Analog electronics
address the closure problem
more favorably
than digital semiconductors.
Vacuum tube manufacturing
requires glass, common metals,
and a vacuum pump.
These materials and tools
are far more accessible
from asteroidal or planetary resources
than the materials
and tools required
for integrated circuit fabrication.

The manufacturing complexity hierarchy,
ranked from simplest
to most demanding, is approximately
the following.

1. Mechanical components from metal
2. Vacuum tubes from glass and metal
3. Discrete transistors from doped semiconductor
4. Integrated circuits from ultra-pure silicon

Each step in this hierarchy
increases the required purity
of raw materials,
the precision of manufacturing equipment,
and the cleanliness
of the manufacturing environment
by roughly one to two
orders of magnitude.

A von Neumann probe
that uses vacuum tube electronics
instead of integrated circuits
eliminates the hardest closure gap
identified in the companion article.
The trade-offs are significant.
Vacuum tubes are larger,
consume more power,
generate more heat,
and have shorter lifetimes
than semiconductor devices.
A vacuum tube computer
with the computing power
of a modern microcontroller
would occupy
approximately one cubic meter
and consume
approximately one kilowatt.
For a probe
with a nuclear power source
producing kilowatts to megawatts,
this power consumption
is manageable.

The radiation tolerance advantage
is substantial.
Vacuum tubes
are inherently immune
to single-event upsets
from cosmic radiation.
The active elements
in a vacuum tube
are macroscopic structures,
electrodes separated by millimeters
in a vacuum.
There is no semiconductor junction
to be disrupted
by a charged particle.
The total ionizing dose tolerance
of vacuum tubes
is effectively unlimited
for the radiation levels
encountered in interstellar space.
This eliminates
an entire class of errors
that the error correction
recursion problem
must otherwise address.

### Work in Progress

**Analog neural network accelerators.**
Research in analog computing
for neural network inference
is advancing rapidly.
Resistive crossbar arrays
using memristive devices
perform analog matrix multiplication
in a single computational step.
If these devices
can be manufactured
from simpler materials
than conventional semiconductors,
they offer a path
to adaptive computation
for von Neumann probes.

**Radiation-hardened analog circuits.**
Work on radiation-hardened
analog circuits
for space applications
continues in the aerospace industry.
While most of this work
focuses on semiconductor implementations,
the design principles
for radiation-tolerant analog computation
are directly applicable
to vacuum tube circuits.

**Miniaturized vacuum devices.**
Research into micro-scale
vacuum electronic devices
aims to combine
the radiation immunity
of vacuum electronics
with the miniaturization
of semiconductor fabrication.
Micro-vacuum tubes
fabricated using MEMS techniques
have been demonstrated
in laboratory settings.

### Hypothetical Approaches

**A vacuum tube probe computer.**
A von Neumann probe
could carry a general-purpose
vacuum tube computer
for its control system.
A computer with approximately
$10^3$ vacuum tubes
could implement
an architecture comparable
to early 1950s computers,
achieving perhaps $10^4$
operations per second.
This is sufficient
for manufacturing control,
navigation,
and basic quality assurance.
The probe would manufacture
replacement vacuum tubes
from local glass and metal resources,
eliminating the semiconductor
closure gap entirely.

**An analog neural controller.**
Rather than using
a programmed digital computer,
a probe could use
an analog neural network
to control its manufacturing processes.
The network would be trained
on Earth before launch
and would implement
control strategies
as weighted connections
in a resistive network.
The manufacturing tolerances
for resistive networks
are much wider
than for semiconductor logic,
and the system degrades gracefully
rather than failing catastrophically
when individual components drift.

**Regenerative vacuum tube manufacturing.**
A probe that manufactures
its own vacuum tubes
could implement
a regenerative replacement cycle.
As tubes age and degrade,
the probe manufactures replacements
and swaps them in.
The manufacturing process
itself is controlled
by the functioning tubes.
This creates a self-maintaining
computing system
that can operate indefinitely,
limited only
by the availability
of raw materials.

## Analog Steampunk Electronics

The term "analog steampunk electronics"
as used in this article
refers to hybrid systems
that combine mechanical
and analog electronic elements
into integrated computing
and control architectures.
These systems use
mechanical components
for tasks best suited
to physical computation
and electronic components
for tasks requiring amplification,
signal conditioning,
or faster processing.
The defining characteristic
is that neither
the mechanical nor the electronic
subsystem alone
is sufficient for the application.

### Historical Origins

Hybrid electromechanical systems
predate purely electronic computers.

The earliest automatic control systems
were electromechanical.
[Elmer Sperry][ref_sperry]
demonstrated the first
gyroscopic autopilot in 1912.
Sperry's system
connected gyroscopic sensors,
which are mechanical devices,
to hydraulic actuators
through electrical servomechanisms.
The autopilot maintained
aircraft attitude
by sensing deviations
with spinning gyroscopes
and correcting them
with electrically actuated
control surfaces.
Lawrence Sperry demonstrated
the autopilot publicly in 1914
by flying a Curtiss C-2
with his hands off the controls.

Electromechanical computers
reached their peak capability
during World War II.
The [Torpedo Data Computer][ref_torpedo_data_computer],
used by United States submarines,
was an electromechanical
analog computer
that calculated torpedo firing solutions
using mechanical differential analyzers
connected to electrical synchro transmitters
and receivers.
The system tracked
target bearing, range, speed,
and course,
computing lead angles
and gyro settings
for the torpedo in real time.

The [Kerrison Predictor][ref_kerrison_predictor],
developed in Britain in 1938,
was a mechanical analog computer
for anti-aircraft fire control.
It tracked a moving target,
predicted its future position,
and aimed the gun
automatically through
electrical servo drives.
The Kerrison Predictor
used mechanical gears
for the computational elements
and electrical motors
for the output drive,
a classic hybrid architecture.

### Key Historical Examples

**The Norden bombsight.**
The [Norden bombsight][ref_norden_bombsight]
is perhaps the most sophisticated
analog steampunk device
ever mass-produced.
It combined a mechanical gyroscope
for stabilization,
a mechanical analog computer
for ballistic calculation,
and an electrical autopilot interface
that flew the aircraft
during the bomb run.
The bombsight was manufactured
by the tens of thousands
and operated reliably
in combat conditions.

**The Apollo guidance computer.**
While the [Apollo Guidance Computer][ref_agc]
was a digital semiconductor device,
it operated alongside
extensive analog electronics
and electromechanical systems.
The inertial measurement unit
used mechanical gyroscopes
and accelerometers.
The digital-to-analog
and analog-to-digital converters
bridged the digital computer
and the analog physical world.
The Apollo program
demonstrated that hybrid architectures,
combining digital computation
with analog sensing and actuation,
are effective
for spacecraft guidance.

**Telephone switching systems.**
The [Strowger switch][ref_strowger_switch]
and its successors
implemented complex routing logic
using electromechanical relays
and stepping switches.
By the 1960s,
telephone exchanges
with millions of subscribers
were controlled entirely
by electromechanical logic.
These systems achieved
reliability levels
comparable to modern
digital systems,
with mean time between failures
measured in decades.

### Current State of the Art

**MEMS-analog hybrid sensors.**
Modern MEMS devices
commonly integrate
mechanical sensing elements
with analog electronic amplifiers
on a single chip.
Accelerometers, gyroscopes,
pressure sensors,
and microphones
all use this architecture.
A MEMS accelerometer
senses acceleration
as the displacement
of a microscopic proof mass
and converts it
to an electrical signal
through capacitive sensing.
The mechanical element
provides the physical measurement,
and the analog electronics
condition the signal
for further processing.

**Analog-mechanical control systems.**
Industrial robotics
and precision manufacturing
continue to use
hybrid analog-mechanical systems
for tasks requiring
high bandwidth
and low latency.
Servo drives
combine analog amplifiers
with mechanical actuators
to achieve positioning accuracy
on the order of micrometers.

**Electromechanical actuator systems.**
Modern spacecraft
use electromechanical actuators
for attitude control,
solar array pointing,
and antenna steering.
These systems
combine electrical control logic
with mechanical output stages,
maintaining the hybrid architecture
pioneered by Sperry's autopilot
over a century ago.

### Contemporary Applications

**Process control in hazardous environments.**
Hybrid pneumatic-electronic systems
remain in use
in chemical processing
and petroleum refining.
Electronic controllers
generate set points
and monitor process variables,
while pneumatic actuators
operate valves and dampers
in explosive atmospheres.

**Precision instrumentation.**
Analytical instruments
such as mass spectrometers,
electron microscopes,
and scanning probe microscopes
combine mechanical positioning systems
with analog electronic measurement circuits.
The mechanical components
provide physical scanning and positioning,
while the analog electronics
amplify and condition
the measurement signals.

**Automotive and aerospace.**
Modern vehicles
combine electronic control units
with mechanical actuators
for steering, braking, throttle control,
and transmission shifting.
The reliability requirements
for automotive and aerospace actuators
drive continued development
of hybrid electromechanical systems.

### Von Neumann Probe Requirements

A von Neumann probe
benefits from a hybrid architecture
because different subsystems
have different computing requirements.

**Low-level manufacturing control.**
PID loops for temperature,
pressure, and position control.
These loops operate
at millisecond timescales
and require
simple arithmetic operations.
Mechanical or fluidic controllers
are adequate
and can be manufactured
with wide tolerances.

**Mid-level quality assurance.**
Comparing sensor readings
against stored specifications.
This requires analog comparators
and threshold detectors,
achievable with vacuum tube circuits.

**High-level navigation and planning.**
Computing trajectory corrections,
managing replication schedules,
and coordinating
with other probes in a swarm.
These tasks require
the most computational capability
and benefit from
programmable digital computation.

**Communication.**
Encoding and decoding
error-corrected signals
for interstellar and inter-probe
communication.
This is the most demanding
computational task
and may require
digital computation
that is difficult to achieve
without semiconductors.

### Comparison to Requirements

A hybrid analog-steampunk architecture
distributes the computing workload
across technologies
matched to their strengths.

Manufacturing control loops
can be implemented entirely
in fluidic or mechanical hardware.
These systems
are the easiest to manufacture
and the most radiation-tolerant.
They handle the bulk
of the real-time control workload.

Quality assurance
and sensor signal processing
can be implemented
in vacuum tube analog electronics.
These systems are moderately difficult
to manufacture
but still far simpler
than semiconductor fabrication.
They provide the signal conditioning
and comparison functions
needed for quality control.

Navigation computation
and communication encoding
present the greatest challenge.
These tasks benefit from
programmable digital computation,
which is difficult to achieve
at adequate throughput
without semiconductor electronics.
A probe might carry
a small number
of radiation-hardened digital processors
manufactured on Earth,
while manufacturing
its analog and mechanical subsystems
from local resources.
Alternatively,
a sufficiently large
vacuum tube digital computer
could perform these computations,
accepting the mass
and power penalties.

The hybrid approach
reduces the semiconductor
closure problem
from a system-wide requirement
to a narrow requirement
for a small number
of high-capability components.
This is analogous
to the partial closure concept
described in the companion article,
where the probe achieves
70 to 90 percent closure
and carries the remaining components
as non-replicable seed material.

### Work in Progress

**MEMS-vacuum hybrid devices.**
Research into micro-vacuum tubes
fabricated using MEMS techniques
represents the convergence
of steampunk and analog approaches
at the microscale.
These devices
combine the radiation immunity
of vacuum electronics
with the miniaturization
achievable through lithographic fabrication.

**Bio-inspired hybrid systems.**
Research groups
are exploring systems
inspired by biological organisms,
which combine
mechanical structure,
chemical computation,
and electrical signaling
in a single integrated architecture.
Soft robotics research,
which combines
deformable mechanical structures
with embedded sensing
and actuation,
represents a contemporary version
of the hybrid approach.

**Printable electronics.**
Additive manufacturing
of electronic components,
including resistors,
capacitors,
inductors,
and simple active devices,
is an active research area.
Printable electronics
could enable a von Neumann probe
to manufacture
analog electronic circuits
using the same additive manufacturing
systems used for structural components.

### Hypothetical Approaches

**A tiered probe control architecture.**
The most promising
hybrid architecture for a von Neumann probe
distributes computation
across three tiers.

The first tier consists
of fluidic and mechanical controllers
for manufacturing process control.
These are the simplest
to manufacture
and the most radiation-tolerant.
They handle all real-time control loops
for mining, refining,
and manufacturing operations.

The second tier consists
of vacuum tube analog electronics
for quality assurance,
sensor signal processing,
and power management.
These circuits
are moderately difficult to manufacture
but well within the capability
of a system
that can work glass and metal.

The third tier consists
of a minimal digital core,
a supervisory computer
responsible for symbolic tasks
and high-level decision making.
This computer,
either manufactured from vacuum tubes
at substantial mass and power cost
or carried as non-replicable
seed material from Earth,
handles the tasks
that genuinely require
digital computation.
These tasks include
mission planning
and replication scheduling,
symbolic reasoning
about manufacturing sequences
and resource allocation,
communications encoding and decoding
with error correction,
data compression
for interstellar communication,
error detection and correction
for stored data,
and navigation calculations
involving discrete trajectory decisions.
The digital core
can be very small
relative to modern computers.
A machine comparable
to early 1950s computers,
with perhaps $10^3$ vacuum tubes,
can perform all of these functions
if they are executed sequentially
rather than concurrently.

This tiered architecture
is not exotic.
Most real-world engineering systems
already combine
mechanical components,
analog electronics,
and digital control.
An automobile engine
uses mechanical actuation,
analog sensor conditioning,
and a digital engine control unit.
A modern aircraft
uses mechanical flight surfaces,
analog servo amplifiers,
and digital flight computers.
The proposed probe architecture
extends this common engineering pattern
to its logical conclusion
by building each layer
from the simplest technology
adequate for its function.

This tiered architecture
minimizes the closure gap
by concentrating
the most demanding manufacturing requirements
in the smallest possible subsystem
while delegating
the bulk of the computing workload
to manufacturable technologies.

**A relay-based digital computer.**
Electromechanical relays
provide digital computing capability
without semiconductor fabrication.
A relay computer
comparable to the Harvard Mark I
could be constructed
from materials available
on any rocky body.
Relays require
iron for the magnetic core,
copper for the coil winding,
and a spring mechanism
for the contact return.
A relay computer
with $10^4$ relays
operating at 10 hertz
could perform perhaps $10^2$
operations per second.
This is slow
but may be sufficient
for infrequent navigation calculations
and replication management tasks.

**An evolutionary manufacturing strategy.**
A probe could launch
with semiconductor electronics
for its first-generation control system
and progressively transition
to locally manufactured alternatives
as it establishes
its industrial base.
The first generation
uses the carried semiconductor systems.
The second generation
supplements with locally manufactured
vacuum tube circuits.
Later generations
may achieve full closure
using a hybrid architecture
that eliminates
the semiconductor dependency entirely.

## Information Storage

A self-replicating probe
must store two distinct categories
of information.

The first category is operational data.
This includes navigation tables,
star maps, calibration constants,
communication protocols,
and mission parameters.
Operational data is read frequently
during normal probe operations
and may be updated occasionally
as the probe refines its models
of the local environment.

The second category is replication knowledge.
This includes detailed engineering blueprints,
manufacturing procedures,
material specifications,
quality control criteria,
and assembly sequences
for building new probes
and the industrial infrastructure
that supports probe manufacturing.
Replication knowledge
is the probe's genome.
It must be stored
with sufficient fidelity
to produce functional offspring
across many generations,
connecting directly
to the error correction
recursion problem
analyzed in the
[companion article][related_post_error_correction].

### Pre-Semiconductor Storage Technologies

Several storage technologies
that predate semiconductor memory
are candidates
for probe information storage.

**[Magnetic core memory][ref_magnetic_core].**
Magnetic core memory,
the dominant form
of computer memory
from the mid-1950s
through the mid-1970s,
stores data
as the magnetization direction
of small ferrite rings.
Each ring, or core,
stores one bit.
Core memory is non-volatile,
retaining data without power.
It is radiation-hardened,
as ferrite cores
are immune to single-event upsets.
Manufacturing requires
ferrite material,
fine copper wire,
and the ability to thread wires
through microscopic cores.
The weaving process
was historically performed by hand
at high labor cost,
but could be automated
by a probe
with sufficient dexterity.

**[Magnetic tape][ref_magnetic_tape]
and [magnetic drum][ref_magnetic_drum] storage.**
Magnetic tape
stores data as magnetization patterns
on a thin ribbon
coated with magnetic oxide.
Magnetic drums
store data on the surface
of a rotating cylinder.
Both technologies
are straightforward to manufacture
from iron oxide, a binder,
and a substrate material.
Magnetic tape can store
large volumes of data
at low cost per bit,
making it suitable
for archival storage
of replication knowledge.
The primary limitation
is access speed.
Tape is sequential access,
requiring minutes
to locate data.
For a probe
that can plan its data access
in advance,
this limitation is manageable.

**[Punched tape][ref_punched_tape]
and mechanically encoded storage.**
Punched tape
encodes data
as the presence or absence
of holes at positions.
The medium is durable,
simple to manufacture,
and readable
by purely mechanical means.
A probe could punch data
into metal tape or plates
that would survive
for millennia
without degradation.
The information density is low
compared to magnetic storage,
but for critical data
such as core manufacturing procedures,
the extreme durability
may justify the storage volume.

**[5D optical storage][ref_5d_optical_storage].**
Researchers at the University of Southampton
have demonstrated
data storage in nanostructured glass
using femtosecond laser pulses.
The data is encoded
in five dimensions of the glass structure,
three spatial dimensions
plus the orientation and magnitude
of birefringent nanostructures.
This technology can store
360 terabytes per disk
and the data is stable
for billions of years
at room temperature.
A probe could carry
its complete replication knowledge
on a small number
of glass disks
that would outlast
any other component
of the probe.
The reader requires
a polarization microscope,
which is achievable
with analog optical components.

**The [Rosetta Disk][ref_rosetta_disk].**
The Long Now Foundation's
Rosetta Disk
uses nickel microetching
to store information
as microscopic text
readable with optical magnification.
The nickel substrate
is expected to survive
for thousands of years
without degradation.
This approach demonstrates
that archival-quality data storage
is achievable
with pre-semiconductor materials.

**The [Voyager Golden Record][ref_voyager_golden_record].**
Each Voyager spacecraft carries
a 12-inch gold-plated copper
phonograph record
containing images, sounds,
and greetings from Earth.
The gold plating provides
corrosion resistance
and impermeability.
The analog groove storage
requires no electronic reader,
only a mechanical stylus
and transducer.
The records are expected to survive
longer than Earth itself,
demonstrating that analog storage
on durable metallic substrates
can preserve data
for billions of years
in interstellar space.

### Storage Longevity and Redundancy

The longevity requirements
for probe data storage
are extreme.
An interstellar probe
traveling at 10 percent
of the speed of light
requires approximately 40 years
to reach the nearest star system.
An intergalactic probe
traveling at similar speeds
requires millions of years
to reach the nearest galaxy.
The storage medium
must survive these transit times
without unacceptable data degradation.

The probe must employ
redundancy strategies
to protect against data corruption.
Replicated storage,
in which multiple copies
of critical data
are maintained on separate media,
provides protection
against localized damage.
[Error-correcting codes][related_post_error_correction],
which add structured redundancy
to the data itself,
enable detection and correction
of individual bit errors
without requiring
full data duplication.
Periodic data verification,
in which the digital core
reads stored data,
checks it against
error-correcting codes,
and repairs corrupted copies
from uncorrupted replicas,
extends the effective lifetime
of the storage system
indefinitely
as long as the verification
and repair process
itself remains functional.

[Triple modular redundancy][ref_tmr],
in which three copies
of a critical system
operate in parallel
and a majority vote
determines the output,
is applicable
to both digital and analog systems.
Modern [fly-by-wire][ref_fly_by_wire] aircraft
use triple or quadruple redundancy
for flight control computers,
with mechanical or hydraulic backup
as a final fallback.
A von Neumann probe
could apply the same principle
to its storage systems,
maintaining three copies
of critical data
on separate physical media
and voting among them
to detect and correct
individual storage failures.

A tiered storage strategy
matches the storage technology
to the criticality
and access pattern
of the data.
Critical replication knowledge
is stored on the most durable medium,
such as etched metal
or nanostructured glass.
Frequently accessed operational data
is stored on faster media
such as magnetic core memory.
Bulk data such as star maps
is stored on high-capacity media
such as magnetic tape.

## Manufacturing Implications

The proposed three-tier architecture
has direct implications
for manufacturing feasibility.

**Mechanical systems require
relatively simple machining.**
Gears, cams, levers,
and fluidic channels
can be fabricated
by a probe
with basic metalworking capability,
including casting, milling, drilling,
and surface grinding.
The tolerances are on the order
of micrometers to tens of micrometers.
The materials are common metals
and alloys available
from asteroidal resources.
No exotic materials are required.
No clean room is required.

**Analog electronics can be built
with relatively large-feature components.**
Vacuum tubes require
glass or ceramic envelopes,
metal electrodes,
and a vacuum pump.
Resistors are lengths
of resistive wire or film.
Capacitors are layers
of conductor and dielectric.
Inductors are coils of wire
wound on ferrite or iron cores.
The smallest feature size
in a vacuum tube circuit
is on the order of millimeters,
approximately six orders of magnitude
larger than the features
in a modern integrated circuit.
This difference
in manufacturing precision
is the fundamental reason
that vacuum tube electronics
are replicable
where semiconductor electronics
are not.

**Only a small portion
of the probe
requires advanced fabrication.**
If the digital core
is manufactured from vacuum tubes,
the entire probe computing system
is replicable
from materials and processes
available on any rocky body.
If a semiconductor digital core
is deemed necessary,
it constitutes
a small fraction
of the total computing system,
reducing the non-replicable seed mass
from the entire computing system
to a single subsystem.
This directly reduces
the closure gap
identified in the companion article.

## Radically Devolved Probes

The preceding analysis
has assumed interstellar probes
with transit times
on the order of decades.
For probes designed
for intergalactic exploration,
where travel times
may reach millions of years,
the engineering constraints
shift fundamentally.

### The Intergalactic Timescale Problem

Digital electronics
may degrade over extremely long timescales
even with radiation shielding.
Accumulated radiation damage,
electromigration in conductors,
dielectric breakdown,
and thermal cycling
all contribute to progressive failure.
Semiconductor devices
are particularly vulnerable
to long-term degradation
because their function depends
on precisely controlled
dopant distributions
that can diffuse
over geological timescales.

Mechanical and ceramic systems,
by contrast,
can survive for millennia
or longer
with minimal degradation.
[Presolar grains][ref_presolar_grains],
silicon carbide crystals
that condensed around distant stars
and survived the interstellar medium,
the solar nebula,
and geological time
inside meteorites,
demonstrate that certain mineral structures
persist for billions of years
in interstellar space.
[Heck et al.][research_heck]
dated presolar grains
in the Murchison meteorite
to up to seven billion years old,
the oldest solid material
found on Earth.
The [Antikythera mechanism][ref_antikythera]
survived over two thousand years
on the ocean floor.
Astronomical clocks
such as the
[Prague Astronomical Clock][ref_prague_clock],
first installed in 1410,
have operated for centuries
with periodic maintenance.
The [10,000 Year Clock][ref_long_now_clock],
designed by Danny Hillis
for the Long Now Foundation,
is engineered
to operate for ten millennia
using mechanical principles
that minimize wear
and environmental sensitivity.

### A Minimal Analog Probe

A probe designed
for intergalactic transit
lasting millions of years
might rely almost entirely
on mechanical
and analog electronic systems,
with very limited
or no digital logic.
Such a radically devolved probe
would sacrifice
computational sophistication
for maximum longevity
and robustness.

A minimal analog probe
might perform
only the following functions.
Slow navigation,
using mechanical gyroscopes
and analog star trackers
to maintain course
over million-year transit times.
Environmental sensing,
using analog sensors
to detect arrival
at a target star system
and assess resource availability.
Extremely simple replication strategies,
using cam-timed manufacturing sequences
and analog quality control
to produce copies
that are mechanically identical
to the parent probe
without the need
for complex digital computation.

The replication knowledge
for such a probe
would be stored
in the physical geometry
of its cam programs,
its wiring patterns,
and its mechanical templates,
analogous to how
the replication knowledge
of a virus
is stored
in its molecular structure
rather than
in a symbolic genome.

### The Devolution Trade-Off

A radically devolved probe
trades capability for persistence.
It cannot perform
complex trajectory optimization,
sophisticated error correction,
or adaptive manufacturing.
But it can persist
across timescales
that would destroy
any semiconductor-based system.
If even a small fraction
of such probes
arrive at target galaxies
with sufficient functionality
to begin replication,
the strategy succeeds
through numbers and patience
rather than individual capability.

This represents
the extreme end
of the architectural spectrum
described in this article.
The three-tier architecture
proposed for interstellar probes
places the boundary
between analog and digital
at the point
of acceptable manufacturing complexity.
The radically devolved probe
eliminates digital computation entirely,
pushing the boundary to zero
and accepting the resulting
limitations in capability.

## Conclusion

The semiconductor fabrication
closure gap
identified in the companion article
on [von Neumann probes][related_post_von_neumann_probes]
is the single hardest obstacle
to self-replicating spacecraft.
Modern integrated circuits
require manufacturing precision
and material purity
that appear to be beyond
the near-term capability
of any autonomous
extraterrestrial factory.

This article has examined
three categories
of alternative computing technology
that could reduce or eliminate
this closure gap.

Steampunk electronics,
encompassing mechanical
and fluidic computing,
offer the simplest manufacturing path.
Mechanical computers
can be fabricated
from common metals
with tolerances on the order
of micrometers.
Fluidic computers
use no electrical components at all.
Both are inherently immune
to radiation-induced errors.
The limitation
is computational throughput,
which is approximately
six to nine orders of magnitude
below modern digital electronics.
For manufacturing process control,
this throughput is adequate.
For communication encoding
and complex navigation,
it is not.

Analog electronics,
particularly vacuum tube technology,
occupy a middle position
in the manufacturing complexity hierarchy.
Vacuum tubes require
glass, common metals,
and a vacuum pump,
all of which are far more accessible
than the materials
and equipment needed
for semiconductor fabrication.
Vacuum tubes
are inherently immune
to single-event upsets
and can operate
in radiation environments
that would destroy
semiconductor devices.
A vacuum tube computer
with the capability
of a 1950s mainframe
could serve
as a probe's central controller,
accepting penalties
in size, power, and mass
that are manageable
for a system
with nuclear power.

Analog steampunk electronics,
combining mechanical and analog elements
in a hybrid architecture,
offer the most promising approach.
The core of this article's argument
is the three-layer architecture.
Mechanical control,
using governors, cams,
and fluidic logic,
handles robust low-level actuation
and manufacturing process control.
Analog computation,
using vacuum tube amplifiers
and operational amplifier circuits,
handles continuous signal processing,
quality assurance,
and feedback control.
A minimal digital core,
either manufactured from vacuum tubes
or carried as seed material,
handles planning, communications encoding,
error correction,
and symbolic reasoning.

This architecture distributes
the computing workload
across technologies
matched to their manufacturing feasibility.
Each layer handles
the tasks best suited
to its capabilities,
and the bulk of the computing work
falls on the layers
that are easiest to manufacture.
The semiconductor closure gap
shrinks from a system-wide impossibility
to a narrow constraint
on a single subsystem.

The probe only needs
sufficient computation,
not modern computing technology.
For extremely long-duration
intergalactic missions,
even the digital core
may be unnecessary.
A radically devolved probe
relying entirely
on mechanical and analog systems
trades computational sophistication
for maximum longevity and robustness,
persisting across timescales
that would destroy
any semiconductor-based system.

The central insight
is that the closure problem
for computing
is not binary.
A probe does not need
to replicate a modern microprocessor.
It needs to replicate
the computing capability
required for its functions.
Many of those functions
were performed competently
by technologies
that predate the transistor.
The engineering challenge
is not inventing new computing technologies
but adapting century-old technologies
to the requirements
of autonomous, self-replicating
extraterrestrial manufacturing.

## Future Reading

The following sources extend
the topics discussed in this article.

- [Analog and Hybrid Computer Programming, Karplus and Soroka, 1959][future_karplus]
- [Analog Computing, Ulmann, De Gruyter, 2022][future_ulmann]
- [Computing: A Concise History, Campbell-Kelly, 2012][future_campbell_kelly]
- [Digital Instrumentation and Control Systems in Nuclear Power Plants, National Research Council, 1997][future_nrc_nuclear]
- [Electronic Analog and Hybrid Computers, Korn and Korn, 1964][future_korn]
- [Kinematic Self-Replicating Machines, Freitas and Merkle, 2004][future_freitas_merkle]
- [Neuromorphic Computing and Engineering (Journal), IOP Publishing][future_neuromorphic]
- [The Computer from Pascal to von Neumann, Goldstine, 1972][future_goldstine]
- [The Theory of Self-Reproducing Automata, Von Neumann (ed. Burks), 1966][research_von_neumann_automata]

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Borgue, Olivia, and Andreas M. Hein. 2021. "Near-Term Self-Replicating Probes: A Concept Design." *Acta Astronautica* 187: 546–56. [https://doi.org/10.1016/j.actaastro.2021.03.004][research_borgue]
- Lammie, Corey, Julian Büchel, Athanasios Vasilopoulos, Manuel Le Gallo, and Abu Sebastian. 2025. "The Inherent Adversarial Robustness of Analog in-Memory Computing." *Nature Communications* 16 (1): 1756. [https://doi.org/10.1038/s41467-025-56595-2][research_lammie]
- Ragazzini, J. R., R. H. Randall, and F. A. Russell. 1947. "Analysis of Problems in Dynamics by Electronic Circuits." *Proceedings of the IRE* 35 (5): 444–52. [https://doi.org/10.1109/jrproc.1947.232616][research_ragazzini]

### Primary Sources, Non-Peer-Reviewed

- Analog Computing, Ulmann. 2022. *De Gruyter*. [https://scholar.google.com/scholar?q=De+Gruyter+Analog+Computing+2022][future_ulmann]
- Chowdhury, F. K., S. Han, D. Saab, and M. Tabib-Azar. 2012. "Mems Based Single Device “XOR” and “and” Logic Gates for LSI Mechanical Processors Operating in High Radiation Environments." In *2012 Solid-State, Actuators, and Microsystems Workshop Technical Digest*. Transducer Research Foundation. [https://doi.org/10.31438/trf.hh2012.110][research_tabib_azar]
- Freitas, R. A., Jr., and W. P. Gilbreath. 1982. *Advanced Automation for Space Missions*. NASA-CP-2255. NASA. [https://ntrs.nasa.gov/citations/19830007077][research_nasa_aasm]
- Heck, Philipp R., Jennika Greer, Levke Kööp, et al. 2020. "Lifetimes of Interstellar Dust from Cosmic Ray Exposure Ages of Presolar Silicon Carbide." *Proceedings of the National Academy of Sciences* 117 (4): 1884–89. [https://doi.org/10.1073/pnas.1904573117][research_heck]
- Metzger, Philip T., Anthony Muscatello, Robert P. Mueller, and James Mantovani. 2013. "Affordable, Rapid Bootstrapping of the Space Industry and Solar System Civilization." *Journal of Aerospace Engineering* 26 (1): 18–29. [https://doi.org/10.1061/(asce)as.1943-5525.0000236][research_metzger]

### Secondary Sources

- *Digital Instrumentation and Control Systems in Nuclear Power Plants: Safety and Reliability Issues*. 1997. National Academies Press. [https://doi.org/10.17226/5432][future_nrc_nuclear]

### General Sources

- A Self-Reproducing Interstellar Probe (Journal of the British Interplanetary Society). 1980. "Freitas." [https://www.rfreitas.com/Astro/ReproJBISJuly1980.htm][research_freitas_1980]
- Computing: A Concise History. 2012. "Campbell-Kelly." [https://en.wikipedia.org/wiki/Computing:\_A\_Concise\_History][future_campbell_kelly]
- Kinematic Self-Replicating Machines. 2004. "Freitas and Merkle." [http://www.molecularassembler.com/KSRM.htm][future_freitas_merkle]
- "Neuromorphic Computing and Engineering (Journal), IOP Publishing." n.d. Accessed October 25, 2026. [https://iopscience.iop.org/journal/2634-4386][future_neuromorphic]
- The Computer from Pascal to von Neumann. 1972. "Goldstine." [https://en.wikipedia.org/wiki/The\_Computer\_from\_Pascal\_to\_von\_Neumann][future_goldstine]
- The Theory of Self-Reproducing Automata. 1966. "Von Neumann (ed. Burks)." [https://cba.mit.edu/events/03.11.ASE/docs/VonNeumann.pdf][research_von_neumann_automata]

### Tertiary Sources

- "5D Optical Data Storage." 2026. Wikipedia. Last modified February 27, at 10:47 (UTC). [https://en.wikipedia.org/w/index.php?title=5D\_optical\_data\_storage&oldid=1340742394][ref_5d_optical_storage]
- "Ada Lovelace." 2026. Wikipedia. Last modified March 3, at 05:22 (UTC). [https://en.wikipedia.org/w/index.php?title=Ada\_Lovelace&oldid=1341435129][ref_ada_lovelace]
- "Analog Computer." 2026. Wikipedia. Last modified March 5, at 04:54 (UTC). [https://en.wikipedia.org/w/index.php?title=Analog\_computer&oldid=1341808805][future_karplus]
- "Analytical Engine." 2026. Wikipedia. Last modified March 4, at 02:48 (UTC). [https://en.wikipedia.org/w/index.php?title=Analytical\_engine&oldid=1341611307][ref_analytical_engine]
- "Antikythera Mechanism." 2026. Wikipedia. Last modified March 3, at 19:18 (UTC). [https://en.wikipedia.org/w/index.php?title=Antikythera\_mechanism&oldid=1341534882][ref_antikythera]
- "Apollo Guidance Computer." 2026. Wikipedia. Last modified January 24, at 04:19 (UTC). [https://en.wikipedia.org/w/index.php?title=Apollo\_Guidance\_Computer&oldid=1334538599][ref_agc]
- "Audion." 2025. Wikipedia. Last modified November 8, at 12:30 (UTC). [https://en.wikipedia.org/w/index.php?title=Audion&oldid=1321064327][ref_audion]
- "Ball-and-Disk Integrator." 2025. Wikipedia. Last modified July 28, at 16:45 (UTC). [https://en.wikipedia.org/w/index.php?title=Ball-and-disk\_integrator&oldid=1303009816][ref_ball_disk_integrator]
- "Cam." 2025. Wikipedia. Last modified November 29, at 13:28 (UTC). [https://en.wikipedia.org/w/index.php?title=Cam&oldid=1324768419][ref_cam]
- "Cavity Magnetron." 2026. Wikipedia. Last modified February 28, at 13:49 (UTC). [https://en.wikipedia.org/w/index.php?title=Cavity\_magnetron&oldid=1340922343][ref_magnetron]
- "Centrifugal Governor." 2025. Wikipedia. Last modified December 11, at 09:17 (UTC). [https://en.wikipedia.org/w/index.php?title=Centrifugal\_governor&oldid=1326863898][ref_watt_governor]
- "Charles Babbage." 2026. Wikipedia. Last modified February 26, at 18:15 (UTC). [https://en.wikipedia.org/w/index.php?title=Charles\_Babbage&oldid=1340617331][ref_babbage]
- "Clock of the Long Now." 2026. Wikipedia. Last modified February 14, at 15:24 (UTC). [https://en.wikipedia.org/w/index.php?title=Clock\_of\_the\_Long\_Now&oldid=1338334628][ref_long_now_clock]
- "Coandă Effect." 2026. Wikipedia. Last modified January 20, at 17:03 (UTC). [https://en.wikipedia.org/w/index.php?title=Coand%C4%83\_effect&oldid=1333940657][ref_coanda_effect]
- "Difference Engine." 2026. Wikipedia. Last modified January 28, at 08:42 (UTC). [https://en.wikipedia.org/w/index.php?title=Difference\_engine&oldid=1335271763][ref_difference_engine]
- "Differential (Mechanical Device)." 2026. Wikipedia. Last modified February 8, at 22:20 (UTC). [https://en.wikipedia.org/w/index.php?title=Differential\_(mechanical\_device)&oldid=1337343669][ref_differential_gear]
- "Differential Analyser." 2025. Wikipedia. Last modified October 16, at 23:56 (UTC). [https://en.wikipedia.org/w/index.php?title=Differential\_analyser&oldid=1317209481][ref_differential_analyzer]
- "Drum Memory." 2026. Wikipedia. Last modified January 24, at 02:33 (UTC). [https://en.wikipedia.org/w/index.php?title=Drum\_memory&oldid=1334527251][ref_magnetic_drum]
- "Electromagnetic Pulse." 2026. Wikipedia. Last modified January 28, at 14:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Electromagnetic\_pulse&oldid=1335306001][ref_emp]
- "ENIAC." 2026. Wikipedia. Last modified February 6, at 16:17 (UTC). [https://en.wikipedia.org/w/index.php?title=ENIAC&oldid=1336946006][ref_eniac]
- "Fleming Valve." 2025. Wikipedia. Last modified November 8, at 18:18 (UTC). [https://en.wikipedia.org/w/index.php?title=Fleming\_valve&oldid=1321101738][ref_fleming_valve]
- "Fluidics." 2025. Wikipedia. Last modified December 11, at 20:33 (UTC). [https://en.wikipedia.org/w/index.php?title=Fluidics&oldid=1326950830][ref_flodac]
- "Fly-by-Wire." 2026. Wikipedia. Last modified January 21, at 07:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Fly-by-wire&oldid=1334056316][ref_fly_by_wire]
- "Harvard Mark I." 2026. Wikipedia. Last modified February 1, at 23:13 (UTC). [https://en.wikipedia.org/w/index.php?title=Harvard\_Mark\_I&oldid=1336101003][ref_harvard_mark_i]
- "Jacquard Machine." 2026. Wikipedia. Last modified February 27, at 22:46 (UTC). [https://en.wikipedia.org/w/index.php?title=Jacquard\_machine&oldid=1340823282][ref_jacquard_loom]
- "Kerrison Predictor." 2026. Wikipedia. Last modified January 24, at 09:02 (UTC). [https://en.wikipedia.org/w/index.php?title=Kerrison\_Predictor&oldid=1334567509][ref_kerrison_predictor]
- "Klystron." 2026. Wikipedia. Last modified March 4, at 06:31 (UTC). [https://en.wikipedia.org/w/index.php?title=Klystron&oldid=1341645484][ref_klystron]
- "Konrad Zuse." 2026. Wikipedia. Last modified January 2, at 14:40 (UTC). [https://en.wikipedia.org/w/index.php?title=Konrad\_Zuse&oldid=1330784875][ref_zuse]
- "Magnetic-Core Memory." 2026. Wikipedia. Last modified February 7, at 16:15 (UTC). [https://en.wikipedia.org/w/index.php?title=Magnetic-core\_memory&oldid=1337116405][ref_magnetic_core]
- "Magnetic-Tape Data Storage." 2026. Wikipedia. Last modified February 26, at 08:47 (UTC). [https://en.wikipedia.org/w/index.php?title=Magnetic-tape\_data\_storage&oldid=1340548370][ref_magnetic_tape]
- "MEMS." 2026. Wikipedia. Last modified January 13, at 08:21 (UTC). [https://en.wikipedia.org/w/index.php?title=MEMS&oldid=1332697240][ref_mems]
- "Neuromorphic Computing." 2026. Wikipedia. Last modified January 8, at 16:28 (UTC). [https://en.wikipedia.org/w/index.php?title=Neuromorphic\_computing&oldid=1331865083][ref_neuromorphic]
- "Norden Bombsight." 2026. Wikipedia. Last modified March 1, at 16:57 (UTC). [https://en.wikipedia.org/w/index.php?title=Norden\_bombsight&oldid=1341130986][ref_norden_bombsight]
- "Nuclear Reactor." 2026. Wikipedia. Last modified February 25, at 14:42 (UTC). [https://en.wikipedia.org/w/index.php?title=Nuclear\_reactor&oldid=1340406968][ref_nuclear_reactor]
- "Operational Amplifier." 2026. Wikipedia. Last modified January 16, at 03:44 (UTC). [https://en.wikipedia.org/w/index.php?title=Operational\_amplifier&oldid=1333171229][ref_operational_amplifier]
- "Perceptron." 2026. Wikipedia. Last modified February 20, at 05:41 (UTC). [https://en.wikipedia.org/w/index.php?title=Perceptron&oldid=1339379543][ref_perceptron]
- "Phillips Machine." 2026. Wikipedia. Last modified February 23, at 03:56 (UTC). [https://en.wikipedia.org/w/index.php?title=Phillips\_Machine&oldid=1339954224][ref_moniac]
- "Planimeter." 2026. Wikipedia. Last modified February 15, at 02:03 (UTC). [https://en.wikipedia.org/w/index.php?title=Planimeter&oldid=1338422862][ref_planimeter]
- "Prague Astronomical Clock." 2026. Wikipedia. Last modified February 21, at 16:10 (UTC). [https://en.wikipedia.org/w/index.php?title=Prague\_astronomical\_clock&oldid=1339643282][ref_prague_clock]
- "Presolar Grains." 2026. Wikipedia. Last modified February 8, at 02:40 (UTC). [https://en.wikipedia.org/w/index.php?title=Presolar\_grains&oldid=1337210085][ref_presolar_grains]
- "Punched Tape." 2026. Wikipedia. Last modified February 15, at 11:14 (UTC). [https://en.wikipedia.org/w/index.php?title=Punched\_tape&oldid=1338479410][ref_punched_tape]
- "Rangekeeper." 2025. Wikipedia. Last modified June 9, at 08:06 (UTC). [https://en.wikipedia.org/w/index.php?title=Rangekeeper&oldid=1294696788][ref_rangekeeper]
- "Rosetta Project." 2026. Wikipedia. Last modified January 15, at 04:28 (UTC). [https://en.wikipedia.org/w/index.php?title=Rosetta\_Project&oldid=1333010441][ref_rosetta_disk]
- "Saturn V." 2026. Wikipedia. Last modified March 2, at 03:26 (UTC). [https://en.wikipedia.org/w/index.php?title=Saturn\_V&oldid=1341235154][ref_saturn_v]
- "Science Museum, London." 2025. Wikipedia. Last modified December 29, at 12:36 (UTC). [https://en.wikipedia.org/w/index.php?title=Science\_Museum,\_London&oldid=1330096397][ref_science_museum]
- "Servomechanism." 2026. Wikipedia. Last modified January 31, at 08:10 (UTC). [https://en.wikipedia.org/w/index.php?title=Servomechanism&oldid=1335802626][ref_servomechanism]
- "Ship Gun Fire-Control System." 2026. Wikipedia. Last modified February 22, at 05:18 (UTC). [https://en.wikipedia.org/w/index.php?title=Ship\_gun\_fire-control\_system&oldid=1339760328][ref_mark_37]
- "Sperry Corporation." 2026. Wikipedia. Last modified February 1, at 20:30 (UTC). [https://en.wikipedia.org/w/index.php?title=Sperry\_Corporation&oldid=1336073744][ref_sperry]
- "Strowger Switch." 2025. Wikipedia. Last modified June 28, at 12:21 (UTC). [https://en.wikipedia.org/w/index.php?title=Strowger\_switch&oldid=1297777579][ref_strowger_switch]
- "Tide-Predicting Machine." 2026. Wikipedia. Last modified January 29, at 18:02 (UTC). [https://en.wikipedia.org/w/index.php?title=Tide-predicting\_machine&oldid=1335519049][ref_tide_predictor]
- "Torpedo Data Computer." 2025. Wikipedia. Last modified September 27, at 06:34 (UTC). [https://en.wikipedia.org/w/index.php?title=Torpedo\_Data\_Computer&oldid=1313619639][ref_torpedo_data_computer]
- "Triple Modular Redundancy." 2025. Wikipedia. Last modified August 4, at 03:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Triple\_modular\_redundancy&oldid=1304120120][ref_tmr]
- "V-2 Rocket." 2026. Wikipedia. Last modified March 3, at 12:38 (UTC). [https://en.wikipedia.org/w/index.php?title=V-2\_rocket&oldid=1341483741][ref_v2_rocket]
- "Vacuum Tube." 2026. Wikipedia. Last modified February 22, at 11:51 (UTC). [https://en.wikipedia.org/w/index.php?title=Vacuum\_tube&oldid=1339804013][ref_vacuum_tube]
- "Vannevar Bush." 2026. Wikipedia. Last modified February 2, at 03:58 (UTC). [https://en.wikipedia.org/w/index.php?title=Vannevar\_Bush&oldid=1336140969][ref_vannevar_bush]
- "Voyager Golden Record." 2026. Wikipedia. Last modified February 22, at 13:16 (UTC). [https://en.wikipedia.org/w/index.php?title=Voyager\_Golden\_Record&oldid=1339814375][ref_voyager_golden_record]
- "Z1 (Computer)." 2026. Wikipedia. Last modified February 1, at 07:24 (UTC). [https://en.wikipedia.org/w/index.php?title=Z1\_(computer)&oldid=1335982073][ref_z1]

### Related Posts

- Sechter, Brendan. 2026. "Introduction to Astronomy." *Brendan A R Sechter's Development Blog*, February 12. [https://sgeos.github.io/space/astronomy/science/2026/02/12/introduction\_to\_astronomy.html][related_post_astronomy]
- Sechter, Brendan. 2026. "Roadmap to a Competitive Type III Civilization." *Brendan A R Sechter's Development Blog*, March 3. [https://sgeos.github.io/science/philosophy/2026/03/03/roadmap\_to\_competitive\_type\_iii\_civilization.html][related_post_roadmap]
- Sechter, Brendan. 2026. "Von Neumann Probes." *Brendan A R Sechter's Development Blog*, March 5. [https://sgeos.github.io/science/philosophy/2026/03/05/von\_neumann\_probes.html][related_post_von_neumann_probes]
- Sechter, Brendan. 2026. "The Error Correction Recursion Problem." *Brendan A R Sechter's Development Blog*, March 6. [https://sgeos.github.io/science/philosophy/2026/03/06/error\_correction\_recursion\_problem.html][related_post_error_correction]

[future_campbell_kelly]: https://en.wikipedia.org/wiki/Computing:_A_Concise_History
[future_freitas_merkle]: http://www.molecularassembler.com/KSRM.htm
[future_goldstine]: https://en.wikipedia.org/wiki/The_Computer_from_Pascal_to_von_Neumann
[future_karplus]: https://en.wikipedia.org/w/index.php?title=Analog_computer&oldid=1341808805
[future_korn]: https://en.wikipedia.org/w/index.php?title=Analog_computer&oldid=1341808805
[future_neuromorphic]: https://iopscience.iop.org/journal/2634-4386
[future_nrc_nuclear]: https://doi.org/10.17226/5432
[future_ulmann]: https://scholar.google.com/scholar?q=De+Gruyter+Analog+Computing+2022
[ref_5d_optical_storage]: https://en.wikipedia.org/w/index.php?title=5D_optical_data_storage&oldid=1340742394
[ref_ada_lovelace]: https://en.wikipedia.org/w/index.php?title=Ada_Lovelace&oldid=1341435129
[ref_agc]: https://en.wikipedia.org/w/index.php?title=Apollo_Guidance_Computer&oldid=1334538599
[ref_analytical_engine]: https://en.wikipedia.org/w/index.php?title=Analytical_engine&oldid=1341611307
[ref_antikythera]: https://en.wikipedia.org/w/index.php?title=Antikythera_mechanism&oldid=1341534882
[ref_audion]: https://en.wikipedia.org/w/index.php?title=Audion&oldid=1321064327
[ref_babbage]: https://en.wikipedia.org/w/index.php?title=Charles_Babbage&oldid=1340617331
[ref_ball_disk_integrator]: https://en.wikipedia.org/w/index.php?title=Ball-and-disk_integrator&oldid=1303009816
[ref_cam]: https://en.wikipedia.org/w/index.php?title=Cam&oldid=1324768419
[ref_coanda_effect]: https://en.wikipedia.org/w/index.php?title=Coand%C4%83_effect&oldid=1333940657
[ref_difference_engine]: https://en.wikipedia.org/w/index.php?title=Difference_engine&oldid=1335271763
[ref_differential_analyzer]: https://en.wikipedia.org/w/index.php?title=Differential_analyser&oldid=1317209481
[ref_differential_gear]: https://en.wikipedia.org/w/index.php?title=Differential_(mechanical_device)&oldid=1337343669
[ref_emp]: https://en.wikipedia.org/w/index.php?title=Electromagnetic_pulse&oldid=1335306001
[ref_eniac]: https://en.wikipedia.org/w/index.php?title=ENIAC&oldid=1336946006
[ref_fleming_valve]: https://en.wikipedia.org/w/index.php?title=Fleming_valve&oldid=1321101738
[ref_flodac]: https://en.wikipedia.org/w/index.php?title=Fluidics&oldid=1326950830
[ref_fluidics]: https://en.wikipedia.org/w/index.php?title=Fluidics&oldid=1326950830
[ref_fly_by_wire]: https://en.wikipedia.org/w/index.php?title=Fly-by-wire&oldid=1334056316
[ref_harvard_mark_i]: https://en.wikipedia.org/w/index.php?title=Harvard_Mark_I&oldid=1336101003
[ref_jacquard_loom]: https://en.wikipedia.org/w/index.php?title=Jacquard_machine&oldid=1340823282
[ref_kerrison_predictor]: https://en.wikipedia.org/w/index.php?title=Kerrison_Predictor&oldid=1334567509
[ref_klystron]: https://en.wikipedia.org/w/index.php?title=Klystron&oldid=1341645484
[ref_long_now_clock]: https://en.wikipedia.org/w/index.php?title=Clock_of_the_Long_Now&oldid=1338334628
[ref_magnetic_core]: https://en.wikipedia.org/w/index.php?title=Magnetic-core_memory&oldid=1337116405
[ref_magnetic_drum]: https://en.wikipedia.org/w/index.php?title=Drum_memory&oldid=1334527251
[ref_magnetic_tape]: https://en.wikipedia.org/w/index.php?title=Magnetic-tape_data_storage&oldid=1340548370
[ref_magnetron]: https://en.wikipedia.org/w/index.php?title=Cavity_magnetron&oldid=1340922343
[ref_mark_37]: https://en.wikipedia.org/w/index.php?title=Ship_gun_fire-control_system&oldid=1339760328
[ref_mems]: https://en.wikipedia.org/w/index.php?title=MEMS&oldid=1332697240
[ref_moniac]: https://en.wikipedia.org/w/index.php?title=Phillips_Machine&oldid=1339954224
[ref_neuromorphic]: https://en.wikipedia.org/w/index.php?title=Neuromorphic_computing&oldid=1331865083
[ref_norden_bombsight]: https://en.wikipedia.org/w/index.php?title=Norden_bombsight&oldid=1341130986
[ref_nuclear_reactor]: https://en.wikipedia.org/w/index.php?title=Nuclear_reactor&oldid=1340406968
[ref_operational_amplifier]: https://en.wikipedia.org/w/index.php?title=Operational_amplifier&oldid=1333171229
[ref_perceptron]: https://en.wikipedia.org/w/index.php?title=Perceptron&oldid=1339379543
[ref_planimeter]: https://en.wikipedia.org/w/index.php?title=Planimeter&oldid=1338422862
[ref_prague_clock]: https://en.wikipedia.org/w/index.php?title=Prague_astronomical_clock&oldid=1339643282
[ref_presolar_grains]: https://en.wikipedia.org/w/index.php?title=Presolar_grains&oldid=1337210085
[ref_punched_tape]: https://en.wikipedia.org/w/index.php?title=Punched_tape&oldid=1338479410
[ref_rangekeeper]: https://en.wikipedia.org/w/index.php?title=Rangekeeper&oldid=1294696788
[ref_rosetta_disk]: https://en.wikipedia.org/w/index.php?title=Rosetta_Project&oldid=1333010441
[ref_saturn_v]: https://en.wikipedia.org/w/index.php?title=Saturn_V&oldid=1341235154
[ref_science_museum]: https://en.wikipedia.org/w/index.php?title=Science_Museum,_London&oldid=1330096397
[ref_servomechanism]: https://en.wikipedia.org/w/index.php?title=Servomechanism&oldid=1335802626
[ref_sperry]: https://en.wikipedia.org/w/index.php?title=Sperry_Corporation&oldid=1336073744
[ref_strowger_switch]: https://en.wikipedia.org/w/index.php?title=Strowger_switch&oldid=1297777579
[ref_tide_predictor]: https://en.wikipedia.org/w/index.php?title=Tide-predicting_machine&oldid=1335519049
[ref_tmr]: https://en.wikipedia.org/w/index.php?title=Triple_modular_redundancy&oldid=1304120120
[ref_torpedo_data_computer]: https://en.wikipedia.org/w/index.php?title=Torpedo_Data_Computer&oldid=1313619639
[ref_v2_rocket]: https://en.wikipedia.org/w/index.php?title=V-2_rocket&oldid=1341483741
[ref_vacuum_tube]: https://en.wikipedia.org/w/index.php?title=Vacuum_tube&oldid=1339804013
[ref_vannevar_bush]: https://en.wikipedia.org/w/index.php?title=Vannevar_Bush&oldid=1336140969
[ref_voyager_golden_record]: https://en.wikipedia.org/w/index.php?title=Voyager_Golden_Record&oldid=1339814375
[ref_watt_governor]: https://en.wikipedia.org/w/index.php?title=Centrifugal_governor&oldid=1326863898
[ref_z1]: https://en.wikipedia.org/w/index.php?title=Z1_(computer)&oldid=1335982073
[ref_zuse]: https://en.wikipedia.org/w/index.php?title=Konrad_Zuse&oldid=1330784875
[related_post_astronomy]: {% post_url 2026-02-12-introduction_to_astronomy %}
[related_post_error_correction]: {% post_url 2026-03-06-error_correction_recursion_problem %}
[related_post_roadmap]: {% post_url 2026-03-03-roadmap_to_competitive_type_iii_civilization %}
[related_post_von_neumann_probes]: {% post_url 2026-03-05-von_neumann_probes %}
[research_borgue]: https://doi.org/10.1016/j.actaastro.2021.03.004
[research_freitas_1980]: https://www.rfreitas.com/Astro/ReproJBISJuly1980.htm
[research_heck]: https://doi.org/10.1073/pnas.1904573117
[research_lammie]: https://doi.org/10.1038/s41467-025-56595-2
[research_metzger]: https://doi.org/10.1061/(asce)as.1943-5525.0000236
[research_nasa_aasm]: https://ntrs.nasa.gov/citations/19830007077
[research_ragazzini]: https://doi.org/10.1109/jrproc.1947.232616
[research_tabib_azar]: https://doi.org/10.31438/trf.hh2012.110
[research_von_neumann_automata]: https://cba.mit.edu/events/03.11.ASE/docs/VonNeumann.pdf
