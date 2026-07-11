---
layout: post
mathjax: true
comments: true
title:  "Rocket Propellant Chemistry, Solid Propellants"
date:   2026-02-02 09:00:00 +0000
categories: aerospace propulsion chemistry
---

<!-- A218 -->
<script>console.log("A218");</script>

Solid propellants combine fuel and oxidizer into a single cast grain that
burns from an exposed surface into the chamber volume. The entire delivery
system, the pumps and the injectors and the tank pressurization that a
liquid engine requires, collapses into the grain itself and its case. The
resulting engine is mechanically simple, storable for decades, and delivers
a high density specific impulse at the cost of lower absolute specific
impulse than a liquid engine and the loss of throttling and restart
capability. This article treats solid propellant chemistry at the level
[the previous article][related_post_a217] establishes.

The design space of solid rocket propellants divides into two historical
families and one composite-of-composites. The composite family, dominated
by ammonium perchlorate oxidizer with a hydroxyl-terminated polybutadiene
binder and aluminum fuel, delivers the highest specific impulse routinely
achievable with solids and dominates large boost applications. The
double-base family, dominated by nitrocellulose plasticized with
nitroglycerin, carries the older munitions heritage and delivers modestly
lower specific impulse. Composite modified double-base combinations blend
the two chemistries and reach specific impulse values in the composite
range while retaining some of the mechanical and manufacturing
characteristics of double-base grains. The current research frontier
pursues alternatives to ammonium perchlorate that eliminate the hydrogen
chloride from the exhaust, and higher-energy binders and fuels that push
delivered specific impulse toward the theoretical maximum for a solid.

## Solid Rocket Motor Anatomy

A solid rocket motor consists of a pressure-containing case, an insulation
layer that protects the case from the hot combustion gases, a cast
propellant grain that combines fuel and oxidizer, an igniter at the
forward end that starts combustion, and a nozzle at the aft end that
accelerates the exhaust. The grain is bonded to the insulation, which is
bonded to the case, so that no significant relative motion occurs during
firing. A central perforation through the grain, or a set of shaped
perforations, exposes the initial burning surface. Combustion propagates
radially outward from that surface into the grain until the grain is
consumed or the case fails.

The case is typically wound from glass, aramid, or carbon fiber in an
epoxy or polyester matrix for the highest performance-to-mass ratio, or
fabricated from steel for the highest mechanical robustness and lowest
unit cost. The insulation layer is typically a filled elastomer,
often ethylene propylene diene monomer rubber loaded with silica or
Kevlar fibers, that ablates during firing at a controlled rate. The
igniter is a smaller solid rocket motor of its own, whose exhaust
impinges on the main grain surface to start ignition. The nozzle is
typically a graphite or carbon-carbon throat insert set in a steel or
composite housing, with the throat sized to produce the desired chamber
pressure at the design mass flow rate.

The mechanical simplicity of this arrangement is the principal engineering
attraction of solid propellants. A single pressure vessel with an igniter
and a nozzle is all the vehicle needs to produce thrust. There are no
turbopumps, no valves, no cooling passages, no injectors, and no
propellant tanks in the ordinary sense. The engineering complexity moves
into the chemistry of the propellant itself and into the grain design that
shapes the thrust profile over the burn duration.

## Composite Propellants

The composite family combines a granular crystalline oxidizer, a polymer
binder that also serves as fuel, and typically a metal fuel additive,
into a heterogeneous cast mixture. Ammonium perchlorate is the standard
oxidizer for high-performance applications. Hydroxyl-terminated
polybutadiene is the standard binder in modern formulations, having
displaced the older polybutadiene acrylonitrile and polybutadiene acrylic
acid binders that dominated through the nineteen sixties and nineteen
seventies. Aluminum powder is the standard metal fuel additive.

A representative modern formulation contains approximately $68$ percent
ammonium perchlorate by mass, $18$ percent aluminum by mass, and $12$
percent hydroxyl-terminated polybutadiene by mass, with the remaining $2$
percent divided among bond agents, curing agents, plasticizers, and
ballistic modifiers. The specific fractions vary across manufacturers and
applications by a few percentage points. The Space Shuttle solid rocket
booster propellant, produced by Thiokol and later ATK, used $69.6$
percent ammonium perchlorate, $16$ percent aluminum, $12.04$ percent
polybutadiene acrylonitrile, $1.96$ percent epoxy curing agent, and $0.4$
percent iron oxide as a burn rate catalyst. The Ariane 5 solid rocket
booster propellant, produced by Europropulsion, uses approximately $68$
percent ammonium perchlorate, $18$ percent aluminum, and $14$ percent
hydroxyl-terminated polybutadiene.

### Ammonium Perchlorate

Ammonium perchlorate, chemical formula $NH_4 ClO_4$ and molecular weight
$117.49$ grams per mole, is a crystalline salt that provides both nitrogen
and oxygen to the combustion process. It decomposes at approximately $600$
kelvin through a two-step mechanism whose products depend on temperature
and pressure. At low temperatures the decomposition produces chlorine
oxides, hydrogen chloride, nitrogen oxides, water, and oxygen. At the
temperatures of rocket combustion, above $2000$ kelvin, the decomposition
proceeds essentially to the following net reaction with released oxygen
available to burn the binder and the aluminum.

$$
4 NH_4 ClO_4 \rightarrow 4 HCl + 2 N_2 + 5 O_2 + 6 H_2 O
$$

Ammonium perchlorate is manufactured in controlled particle-size grades.
Formulations typically use a bimodal or trimodal blend of coarse and fine
grades to reach high packing density, which allows high oxidizer loading
without compromising the grain's mechanical integrity. A representative
coarse grade has a mean particle diameter of approximately $200$
micrometers. A representative fine grade has a mean particle diameter of
approximately $20$ micrometers. Ultrafine grades below $10$ micrometers
are used to accelerate burn rate.

The presence of chlorine in ammonium perchlorate is the principal
environmental drawback of composite propellants. The combustion exhaust
contains approximately $20$ percent hydrogen chloride by mass. Hydrogen
chloride combines with atmospheric water vapor near the launch site to
form a corrosive acidic aerosol that damages ground equipment and vegetation
in the immediate launch area. This effect motivates the research on
chlorine-free oxidizers discussed later.

### Hydroxyl-Terminated Polybutadiene

Hydroxyl-terminated polybutadiene, abbreviated HTPB, is a liquid prepolymer
that cures into a solid elastomer through reaction with a diisocyanate or
polyisocyanate curing agent. The polymer backbone consists of repeating
butadiene units, chemical formula $(C_4H_6)_n$, terminated by hydroxyl
groups at both ends. The typical molecular weight of the uncured prepolymer
is approximately $2500$ to $3000$ grams per mole. The cured elastomer
provides the mechanical binder that holds the oxidizer and metal
particles in place, and the polybutadiene backbone contributes carbon and
hydrogen to the combustion, so the binder serves simultaneously as
structural matrix and as fuel.

The curing reaction crosslinks the prepolymer into a rubbery solid over
several days at elevated temperatures, typically $60$ to $80$ degrees
Celsius. During curing the propellant slurry is either poured into the
motor case directly, called case bonding, or into a separate mandrel and
transferred to the case after cure. The isocyanate curing agent is
typically isophorone diisocyanate, abbreviated IPDI, chosen for its slow
reaction rate that allows adequate pot life during casting. Toluene
diisocyanate and diphenylmethane diisocyanate are used in some
applications but are less common in modern practice because of the
higher toxicity of their vapors.

Hydroxyl-terminated polybutadiene displaced polybutadiene acrylic acid and
polybutadiene acrylonitrile as the dominant binder in the nineteen
seventies and nineteen eighties. Hydroxyl-terminated polybutadiene delivers
higher specific impulse, better mechanical properties at low temperatures,
and longer shelf life than the older binders. Polybutadiene acrylonitrile
retains a niche in legacy applications where the case-insulation-grain
bond chemistry was qualified for that binder and requalification would be
prohibitively expensive.

### Aluminum Fuel

Metallic aluminum in powder form serves as the principal fuel additive in
composite propellants. Aluminum combusts to aluminum oxide, chemical
formula $Al_2 O_3$ and molecular weight $101.96$ grams per mole, releasing
approximately $31$ megajoules per kilogram of heat.

$$
4 Al + 3 O_2 \rightarrow 2 Al_2 O_3
$$

That heat of combustion raises the chamber temperature by hundreds of
kelvin above the value the binder alone would produce, and the higher
chamber temperature translates directly to higher specific impulse.

Aluminum powder is used in particle sizes from approximately $5$ to $30$
micrometers. The particles are typically spherical or spheroidal, produced
by atomization of molten aluminum in an inert atmosphere. The as-received
surfaces carry a thin native oxide layer of approximately $2$ to $5$
nanometers that protects the metal from further oxidation during storage
and mixing.

During combustion, the aluminum particles do not burn instantaneously.
They melt at $933$ kelvin, and the molten droplets are carried by the
gas flow away from the burning grain surface. The droplets ignite once
the surface oxide is disrupted and the underlying aluminum contacts the
oxidizer-rich gas. They burn as diffusion-limited spheres until the metal
is consumed. The resulting aluminum oxide is present in the exhaust as
condensed liquid droplets at the chamber temperature and as condensed
solid particles once the exhaust cools below the melting point of
aluminum oxide at approximately $2345$ kelvin. The transition from liquid
to solid aluminum oxide occurs inside the nozzle for most engines.

The presence of condensed aluminum oxide particles in the exhaust produces
a specific impulse penalty called the two-phase-flow loss. Gas expansion
in the nozzle accelerates the gas but does not accelerate the condensed
particles as efficiently, because the particles have thermal and
mechanical inertia that resist rapid acceleration. The particles arrive at
the nozzle exit at lower velocity than the gas, and the mass-weighted
average exit velocity is lower than the pure-gas expansion would produce.
The magnitude of the loss is typically $3$ to $8$ percent of ideal
specific impulse, with larger losses at smaller aluminum loadings and at
larger particle sizes.

### Composite Propellant Combustion

Combustion proceeds through a coupled physical and chemical process at the
grain surface. Heat from the combustion zone above the surface radiates
and conducts back to the surface, raising the surface temperature to
approximately $700$ to $1000$ kelvin. At this temperature the ammonium
perchlorate crystals decompose and the hydroxyl-terminated polybutadiene
binder pyrolyzes. Gaseous products diffuse away from the surface into a
premixed reaction zone where the fuel-rich binder products react with the
oxidizer-rich ammonium perchlorate products. Aluminum particles are
liberated from the surface as the binder pyrolyzes around them, and the
particles agglomerate on the surface before detaching to burn as droplets
in the gas flow.

The steady-state burn rate depends primarily on chamber pressure. The
empirical relationship, called Vieille's law or Saint-Robert's law after
its independent nineteenth-century discoverers, expresses linear burn rate
$r$ as a power function of chamber pressure $P_c$.

$$
r = a \, P_c^n
$$

The coefficient $a$ has units that depend on the units of $r$ and $P_c$
and is typically tabulated for a specific reference temperature. The
pressure exponent $n$ is dimensionless and typically ranges from $0.2$ to
$0.4$ for modern composite propellants. Stable combustion requires $n$
less than $1$. If $n$ were $1$ or greater, small pressure increases would
accelerate combustion enough to further increase pressure without bound.
The condition $n < 1$ produces a stable chamber pressure that any small
perturbation naturally returns to.

Typical burn rates at chamber pressures near $70$ bar range from $5$
millimeters per second for slow-burning grain formulations to $30$
millimeters per second for fast-burning formulations. Iron oxide, copper
chromite, and other transition-metal oxides in small percentages accelerate
the burn rate. Oxamide slows it. Modern composite propellants can be
formulated with burn rates spanning approximately a factor of ten from
the slowest to fastest catalyzed variants.

Combustion also depends on the initial grain temperature. Cold grains
burn more slowly than warm grains because the surface takes longer to
reach ignition temperature. The temperature sensitivity coefficient
$\pi_K$ expresses the fractional change in burn rate per kelvin of
initial temperature change at constant chamber pressure.

$$
\pi_K = \left( \frac{\partial \ln r}{\partial T_i} \right)_{P_c}
$$

Typical values range from $0.001$ to $0.005$ per kelvin. Motors designed
for wide temperature ranges must accommodate the burn rate variation
from cold storage to warm storage, which propagates directly into
chamber pressure and thrust variation.

## Double-Base Propellants

Double-base propellants combine nitrocellulose and nitroglycerin into a
gelatinous colloidal mixture. Neither ingredient requires separate
oxidizer because both molecules contain oxygen in sufficient quantities
to sustain their own combustion. Both are chemically related to organic
nitrates and share the general behavior of that compound family.

Nitrocellulose, chemical formula approximately $C_6H_7N_3O_{11}$ for
fully nitrated cellulose, is prepared by nitrating cellulose fiber with a
mixture of nitric and sulfuric acids. The degree of nitration varies from
approximately $10.5$ percent nitrogen for propellant-grade nitrocellulose
to approximately $13.5$ percent for the highest energy grades. The
nitrated cellulose retains the fibrous character of the parent cellulose
but is now an energetic material that decomposes exothermically when
heated.

Nitroglycerin, chemical formula $C_3H_5N_3O_9$ and molecular weight
$227.09$ grams per mole, is prepared by nitrating glycerin with nitric
and sulfuric acid. Pure nitroglycerin is a viscous liquid at room
temperature and a shock-sensitive high explosive. Its combination with
nitrocellulose gelatinizes the fibrous nitrocellulose into a plastic mass
that can be extruded, rolled, or cast into propellant grains, and the
gelatinization substantially reduces the shock sensitivity from the
value of pure nitroglycerin.

A representative double-base propellant contains approximately $50$
percent nitrocellulose, $35$ percent nitroglycerin, and the remaining $15$
percent divided among diethyl phthalate as plasticizer, diphenylamine or
centralite as stabilizer against slow acid-catalyzed decomposition, and
lead compounds or other catalysts to control burn rate. The
plasticizer softens the mixture during processing. The stabilizer absorbs
nitrogen oxides that would otherwise catalyze further decomposition and
shorten shelf life.

Double-base propellants are manufactured by two principal processes.
Extruded double-base is prepared as a viscous dough that is forced through
a die to produce cylindrical grains of the required diameter, then cut to
length and cured. This process produces smaller grains suitable for
tactical missiles, sounding rockets, and gun propellants. Cast double-base
is prepared as a slurry of nitrocellulose fibers in a mixture of
nitroglycerin, plasticizer, and stabilizer that is poured into the motor
case and cured at low temperature for several days. This process
accommodates larger grains but requires more elaborate handling because
the pourable slurry is more shock sensitive than the extruded dough.

The delivered specific impulse of a double-base propellant ranges from
approximately $210$ to $240$ seconds at sea level, depending on the
specific composition and the chamber conditions. The chamber temperature
is approximately $2600$ to $3000$ kelvin, lower than a composite propellant
because the fuel-oxygen balance is more constrained by the fixed
nitrocellulose and nitroglycerin chemistry. The exhaust contains no
chlorine or aluminum, so the two-phase-flow loss is negligible and the
delivered specific impulse comes closer to the theoretical value than in
a composite formulation.

The principal disadvantages of double-base propellants are lower
absolute specific impulse than composites, greater sensitivity to
impact and thermal insult than modern composite formulations, and the
slow acid-catalyzed decomposition that limits shelf life. The principal
advantages are the absence of a corrosive exhaust, the finer control of
combustion products for smoke-free operation, and the mature
manufacturing base built up over more than a century of use in gun
propellants and small rockets.

## Composite Modified Double-Base Propellants

Composite modified double-base propellants, abbreviated CMDB, combine the
nitrocellulose and nitroglycerin base of a double-base formulation with
solid oxidizer particles and metal fuel particles suspended in the
gelatinized matrix. A representative CMDB formulation contains
approximately $30$ percent nitrocellulose, $25$ percent nitroglycerin,
$20$ percent cyclotetramethylenetetranitramine, abbreviated HMX, as a
solid energetic oxidizer, $15$ percent aluminum, and the remaining $10$
percent divided among plasticizer, stabilizer, and burn rate modifier.

The presence of HMX increases both the energy density and the chamber
temperature above pure double-base values. HMX is a high explosive in
its pure form and contributes carbon and hydrogen as fuel elements
along with oxygen and nitrogen as oxidizer elements, all of which
release energy during combustion. Aluminum contributes fuel and additional combustion energy in
the same manner as in composite formulations. The nitrocellulose and
nitroglycerin matrix serves both as the binder that holds the solid
particles in place and as an additional energetic fuel-oxidizer
combination.

CMDB propellants deliver specific impulse in the range of $250$ to $270$
seconds at sea level, comparable to composite formulations. They preserve
the lower two-phase-flow loss of double-base because the aluminum
loading is smaller than in a pure composite, and they preserve the
smoke-free operation for the same reason. Their principal industrial
niche has been strategic ballistic missile upper stages, where high
specific impulse and reduced smoke are both required. American Navy and
Air Force propulsion programs that developed classical CMDB in the
nineteen seventies and nineteen eighties, along with modernized nitrate
ester plasticized polyether descendants that displaced classical CMDB in
newer strategic missile third stages, invested in the manufacturing base
that persists today.

CMDB carries the shock sensitivity of double-base combined with the
manufacturing complexity of composite. Its handling requirements are
stricter than either pure family, and its cost per unit specific impulse
is correspondingly higher. It is used where the specific-impulse advantage
over pure composite justifies the additional cost, primarily in
weight-critical strategic missile applications.

## The Research Frontier

Two research directions occupy the current solid propellant frontier, both
motivated by the environmental disadvantage of hydrogen chloride in
composite exhaust and by the desire to push specific impulse beyond the
composite ceiling.

### Ammonium Dinitramide

Ammonium dinitramide, chemical formula $NH_4 N(NO_2)_2$ and molecular
weight $124.06$ grams per mole, abbreviated ADN, is a crystalline
oxidizer that produces exhaust containing water, nitrogen, and oxygen but
no chlorine. It was developed in the nineteen seventies at the Zelinsky
Institute in the Soviet Union and independently rediscovered at the SRI
International research institute in the United States in the nineteen
eighties. A composite propellant with ADN in place of ammonium
perchlorate produces a chlorine-free exhaust and delivers specific
impulse approximately $10$ seconds higher than a comparable ammonium
perchlorate formulation, in exchange for the higher cost of ADN and the
more limited production base. Its representative net decomposition
proceeds according to the following equation.

$$
NH_4 N(NO_2)_2 \rightarrow 2 N_2 + O_2 + 2 H_2 O
$$

ADN has been used in production monopropellant systems as a liquid
solution known as LMP-103S, treated in [the next article on storable
liquid propellants][related_post_a220], but has seen only limited
adoption in production solid propellants because the cost premium over
ammonium perchlorate is not justified for most industrial applications
absent a specific environmental driver.

### Hydroxyl-Terminated Polyether

Hydroxyl-terminated polyether, abbreviated HTPE, is an alternative
polymer binder chemistry with better mechanical properties at low
temperatures than HTPB. HTPE grains retain useful mechanical strength at
temperatures where HTPB grains become brittle. This makes HTPE binders
attractive for applications with wide temperature ranges, particularly
missile systems that must be stored at low temperatures and fired at any
temperature within the operational envelope.

HTPE binders are being adopted incrementally in new missile programs but
have not displaced HTPB in the large majority of solid propellant
applications because HTPB delivers slightly higher specific impulse and
has a mature manufacturing base.

### Aluminum Hydride

Aluminum hydride, chemical formula $AlH_3$ and molecular weight $30.01$
grams per mole, abbreviated alane, is a metal hydride that contains
approximately $10$ percent hydrogen by mass. As a solid propellant fuel
additive it delivers substantially higher specific impulse than metallic
aluminum, because the hydrogen contributes to the exhaust as low-molecular-weight
water vapor rather than remaining as bound aluminum oxide. Theoretical
specific impulse gains of $10$ to $20$ seconds over comparable aluminum
formulations have been calculated.

Aluminum hydride has been studied since the nineteen sixties as a solid
propellant additive but has not seen production use because the compound
is unstable at room temperature and decomposes slowly to aluminum and
hydrogen gas over months to years of storage. Grain shelf life has been
the principal barrier. Research on stabilized formulations continues,
particularly for high-performance missile applications where the
specific-impulse advantage is worth substantial cost.

## Grain Geometry and Thrust Profile

The exposed burning surface of the grain determines the mass flow rate of
combustion products and therefore the thrust. As the surface recedes
during burning, its area changes, and the thrust changes with it. Grain
geometry design produces the thrust profile the mission requires, from
the initial spike a booster needs to accelerate against gravity to the
sustained neutral thrust an upper stage needs to burn efficiently at
altitude.

Four principal thrust-versus-time behaviors are named. A progressive
grain has an increasing burning area as it burns, producing increasing
thrust. A regressive grain has a decreasing burning area, producing
decreasing thrust. A neutral grain has a constant burning area, producing
constant thrust. A dual-thrust grain has a boost phase of high thrust
followed by a sustain phase of lower thrust, produced by a burning
surface that regresses through two distinct area regimes.

A cylindrical end-burning grain, in which combustion propagates from the
aft face toward the forward face with the sidewalls insulated, produces a
neutral thrust profile because the burning area equals the case
cross-section throughout the burn. A central-perforated cylindrical grain,
in which combustion propagates radially outward from a cylindrical hole
along the axis, produces a progressive thrust profile because the burning
area increases with the perforation diameter. A star grain, in which the
perforation has a star-shaped cross-section, produces a neutral thrust
profile because the tips of the star burn back while the valleys burn
forward, and the two rates roughly balance.

Modern boost applications typically use finocyl grains, in which the aft
end has star-shaped fins for high initial thrust and the forward end is a
plain cylindrical perforation for sustained thrust. The Space Shuttle
solid rocket boosters used an eleven-point star aft configuration
transitioning to a double-cone cylindrical configuration forward,
producing an initial thrust spike of approximately $14.7$ meganewtons that
tapered to approximately $10.7$ meganewtons at motor midpoint and
recovered to approximately $11.7$ meganewtons before tailoff. This shape
produced thrust proportional to atmospheric density during ascent,
minimizing max-Q loading on the vehicle.

## Performance and Density Specific Impulse

Modern composite solid propellants deliver specific impulse in the range
of $240$ to $270$ seconds at sea level and $260$ to $290$ seconds in
vacuum. The Space Shuttle solid rocket booster propellant delivered $237$
seconds at sea level and $268$ seconds in vacuum. The Ariane 5 solid
rocket booster propellant delivers similar values. Modern strategic
missile CMDB propellants deliver $250$ to $270$ seconds in vacuum. The
theoretical maximum for a solid propellant, computed for an idealized
combination that eliminates two-phase-flow losses, is approximately $310$
seconds vacuum, and no known formulation reaches this value.

Density specific impulse for solid propellants is exceptionally high
because the propellant grain density is high. The density specific
impulse of a propellant is the product of its bulk density and its
specific impulse.

$$
I_d = \rho_p \, I_{sp}
$$

A typical composite propellant grain has a density $\rho_p$ of
approximately $1780$ kilograms per cubic meter and a sea-level specific
impulse of approximately $267$ seconds, giving a density specific impulse
of approximately $476000$ seconds times kilograms per cubic meter. This
value exceeds every liquid propellant combination and is one of the
principal reasons solids dominate first-stage boost applications and
tactical missiles where volume is more constrained than mass.

The characteristic velocity of a composite solid propellant is
approximately $1520$ meters per second at typical chamber conditions. The
thrust coefficient is comparable to a liquid engine of the same
expansion ratio because the nozzle physics is identical once the
combustion products are formed. The specific impulse is lower than a
liquid engine of comparable chemistry primarily because the chamber
temperature is lower and because the two-phase-flow loss reduces the
effective exit velocity.

## Tradeoffs

Solid propellants win over liquid propellants on storability, mechanical
simplicity, and density specific impulse. They lose on absolute specific
impulse, throttleability, restart capability, and exhaust cleanliness.

Storability is the strongest solid-propellant advantage. A well-designed
composite motor stored in a controlled environment retains its
performance for two to three decades. The principal decomposition mode
is slow migration of plasticizer and slow oxidation of the polymer
binder at the grain surface. Double-base motors show slower shelf life
because of the nitroglycerin decomposition pathway, with typical usable
life of one to two decades. This storability advantage is why every
American ballistic missile in service uses solid propellant for all
propulsion stages.

Mechanical simplicity is the second strong solid-propellant advantage.
A solid motor consists of a case, an insulation layer, a grain, an
igniter, and a nozzle. There are no pumps, no valves, no cooling
passages, no injectors, and no propellant tanks. This makes solid
motors substantially cheaper to manufacture per unit thrust and
substantially more reliable in service, at the cost of throttling and
restart flexibility.

Throttling is the strongest solid-propellant disadvantage. Once ignited,
a solid motor produces the thrust its grain geometry dictates and cannot
be reduced or shut down. The thrust profile is designed into the grain
at manufacture. Some solids can be extinguished by rapid depressurization
below a critical pressure, and thrust termination ports on ballistic
missile third stages exploit this behavior for range control, but true
throttling is unavailable.

Restart is impossible. Once a solid motor has burned out, its grain is
consumed. Restart requires a second motor. This limitation prohibits
solid propulsion from applications requiring multiple burns separated by
coast phases, such as most upper-stage and spacecraft propulsion
applications.

Exhaust cleanliness is the second-strongest solid-propellant disadvantage.
Composite propellants produce hydrogen chloride and aluminum oxide
particles that damage ground equipment near the launch pad, that add
weight and volume to the exhaust plume, and that reduce specific impulse
through two-phase-flow losses. Double-base propellants avoid the
hydrogen chloride and the aluminum oxide but pay for the cleaner exhaust
with lower absolute specific impulse. The composite modified double-base
combinations recover most of the composite specific impulse advantage
while accepting the aluminum oxide penalty.

Safety and detonation hazard is a mixed consideration. Modern composite
propellants meet the Insensitive Munitions specifications that require
resistance to bullet impact, sympathetic detonation, fuel fire, and
slow cook-off. Double-base propellants are less resistant to these
insults because of the nitroglycerin content. CMDB propellants require
substantial care in production and handling because of the combination
of high explosive constituents and metal particles. Absolute safety
records depend as much on manufacturing quality and handling procedure as
on chemistry.

Cost per unit specific impulse is lowest for composite propellants at
production scale. Double-base propellants cost approximately twice as
much per unit specific impulse because of the nitrocellulose and
nitroglycerin manufacturing base's higher unit costs. CMDB propellants
cost three to five times as much because of the combined handling
complexity and the high-explosive constituents. Advanced formulations
using ammonium dinitramide or aluminum hydride cost substantially more
than either standard family per unit specific impulse.

## Applications and Industrial Base

Solid propellants dominate three application categories and appear in
several others.

Large space launch boosters are one dominant category. The Space Shuttle
solid rocket boosters, the Space Launch System boosters, the Ariane 5
solid rocket boosters, and the Vega first stage all use composite HTPB
or PBAN propellants with ammonium perchlorate oxidizer and aluminum
fuel. The Delta IV Heavy first stage and the Falcon 9 first stage are
notable exceptions using liquid propellants, and the trend in
next-generation launch vehicles is toward liquid first stages with
smaller solid strap-on boosters where any solids appear at all.

Ballistic missiles are the second dominant category. Every American,
Russian, French, British, and Chinese intercontinental ballistic missile
in service uses solid propellant for all three stages. The Trident II
D5, the Minuteman III, the Sineva, the M51, and the DF-31 all use
composite or CMDB propellants. The choice of solid propulsion is driven
by the storability advantage, since ballistic missiles must sit ready to
fire for years or decades without maintenance.

Tactical missiles are the third dominant category. Air-to-air missiles,
air-to-ground missiles, ship-to-ship missiles, and surface-to-air
missiles use solid propellants almost exclusively. The AIM-9 Sidewinder,
the AIM-120 AMRAAM, the AGM-114 Hellfire, the Harpoon, the Tomahawk
boost phase, and the Patriot all use solid propellants. The choice is
driven by storability and by the compact thrust-to-volume ratio that
solids deliver.

Solid propellants also appear in sounding rockets, some upper stages,
gas generators, ejection seat catapults, and hobbyist model rockets. In
each case the mechanical simplicity and storability of the solid
propellant is worth more than the specific impulse penalty against a
liquid alternative.

The industrial base is dominated by a small number of manufacturers.
Northrop Grumman, whose solid propulsion heritage runs back through
Orbital ATK, ATK, and Thiokol, manufactures the American composite
propellant products for space launch and strategic missile applications. Aerojet Rocketdyne manufactures a
significant secondary line. Europropulsion, a joint venture of
ArianeGroup and Avio, manufactures the European composite propellant
products. The Russian manufacturers, formerly consolidated in the Soviet
industrial complex, continue in production for Russian domestic
requirements. The Chinese and Indian manufacturers serve their domestic
requirements.

## Conclusion

Solid propellants combine fuel and oxidizer into a single cast grain,
producing a mechanically simple engine that delivers high density
specific impulse and excellent storability at the cost of lower absolute
specific impulse than a liquid engine and the loss of throttling and
restart capability. The composite family, dominated by ammonium
perchlorate oxidizer with hydroxyl-terminated polybutadiene binder and
aluminum fuel, is the current industrial standard. The double-base
family retains a smoke-free-exhaust niche. Composite modified double-base
combinations serve strategic missile applications where the specific
impulse advantage over pure composite justifies the additional cost. The
research frontier pursues chlorine-free oxidizers and higher-energy
fuels that promise to raise the ceiling on solid-propellant specific
impulse in the next decade.

The next article, A219, covers cryogenic liquid propellants.

## References

- [Sutton, George P. and Biblarz, Oscar, Rocket Propulsion Elements, ninth edition, Wiley, 2016][ref_sutton_biblarz]
- [Kubota, Naminosuke, Propellants and Explosives, Thermochemical Aspects of Combustion, third edition, Wiley-VCH, 2015][ref_kubota]
- [Davenas, Alain (editor), Solid Rocket Propulsion Technology, Pergamon, 1993][ref_davenas]
- [Kuo, Kenneth K. and Summerfield, Martin (editors), Fundamentals of Solid-Propellant Combustion, AIAA, 1984][ref_kuo_summerfield]
- [Related Post, Rocket Propellant Chemistry, A Design-Tradeoff Space][related_post_a217]
- [Related Post, Rocket Propellant Chemistry, Storable and Hypergolic Liquid Propellants][related_post_a220]

[ref_davenas]: https://www.sciencedirect.com/book/9780080409993/solid-rocket-propulsion-technology
[ref_kubota]: https://onlinelibrary.wiley.com/doi/book/10.1002/9783527693481
[ref_kuo_summerfield]: https://arc.aiaa.org/doi/book/10.2514/4.865671
[ref_sutton_biblarz]: https://www.wiley.com/en-us/Rocket+Propulsion+Elements%2C+9th+Edition-p-9781118753651
[related_post_a217]: {% post_url 2026-02-01-rocket_propellant_chemistry_a_design_tradeoff_space %}
[related_post_a220]: {% post_url 2026-02-04-rocket_propellant_chemistry_storable_and_hypergolic_liquid_propellants %}
