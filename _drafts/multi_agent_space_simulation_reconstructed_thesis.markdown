---
layout: post
mathjax: true
comments: true
title: "Multi-Agent Space Simulation: A Reconstructed Thesis"
date: 2026-11-12 09:00:00 +0000
categories: space space-studies simulation
series: multi_agent_space_simulation
series_title: "Multi-Agent Space Simulation"
series_index: 1
---

<!-- A386 -->
<script>console.log("A386");</script>

This article reconstructs the thesis of a senior seminar paper
that the author wrote at the end of an undergraduate space studies programme.
The paper reviewed space simulations meant for the general public
and asked why none of them combined a physical model that does not cheat
with many independent agents in one shared world.
The paper itself is lost.
The author kept meticulous notes,
and the notes and the paper were lost together in a hardware failure
for which no backup existed.
What follows is therefore a reconstruction from memory.
It does not quote the paper,
give its title
or reproduce its figures,
because none of those survive to be checked.

The loss may be no great misfortune.
In the author's view,
an undergraduate class is a poor format for writing a good paper,
because undergraduate classes prioritise grading,
the display of knowledge
and the verification of academic honesty
above the quality of the written material,
and writing is graded against somewhat arbitrary criteria.
This reconstruction is free of those requirements.
Its aim is simply to be a good paper.

The article has three parts.
The first sets out the thesis and what a model is.
The second reviews four products as space exploration and space exploitation simulations for the general public,
namely Kerbal Space Program,
Children of a Dead Earth,
EVE Online
and Star Citizen.
The third catalogues the soft science fiction conventions
that these products and the wider media present as if they were physics,
gives the correct physics for each,
and turns the remedies into a blueprint
for a high-fidelity multi-agent predictive simulation
that is approachable enough to educate the public
and deliberately refrains from miseducating it.

Two terms are used throughout in a fixed sense.
The people and programs that act inside a simulation are called agents,
whether a human or an automaton stands behind them.
The products are called simulations,
because the question asked of each is how faithfully it simulates.
The whole article is the author's position.
A claim that carries a citation is a sourced fact,
a claim named as an inference is one,
and every other judgement is the author's.
The [Epistemic State](#epistemic-state) section sorts them.

This is the first article in a short series.
The background mechanics of delta-v,
which recur below,
are treated in an earlier article on this site
[Orbital Manoeuvres][related_post_orbital_manoeuvres],
with propulsion that needs no propellant in
[Solar Sailing][related_post_solar_sailing]
and propulsion that leaves the reaction mass behind in
[Mass Drivers][related_post_mass_drivers].

## The Thesis

The thesis has six parts.

1. **Strong single-agent models exist.**
   A single agent can already fly a spacecraft through a faithful model of orbital mechanics.
2. **Multi-agent models have poor physical models.**
   The simulations in which many people act together in one world
   simplify or replace the physics of space travel.
3. **A multi-agent simulation with a physical model that does not cheat is possible**,
   and none is known.
   None of the products the paper reviewed is one,
   and none has been found since.
   The paper's list held other simulations that were never reviewed for lack of time,
   so the claim is that none is known,
   not that none exists.
   Nothing in physics or engineering prevents one from being built.
4. **The existing products have not failed.**
   Their developers are generally competent,
   and each one's model successfully expresses its own product thesis,
   given its product-market fit and its development constraints,
   including staffing.
   The gap lies between the products,
   not in any one of them.
5. **People adapt their behaviour to conditions.**
   A high-fidelity multi-agent simulation should therefore have predictive value,
   bounded by the fidelity of its model and by how approachable it is.
   This reconstruction adds a third bound,
   the incentives its agents feel.
6. **There is market demand for such a simulation**,
   and meeting it would educate the public.
   A simulation the public will not use teaches nobody.

The paper drew on several purchased texts on modelling and simulation,
which covered subjects such as n-body simulation
and the simulation of fluids and fuel tanks.
The author no longer recalls their titles,
so they are not cited here.
The sources below are public ones,
and the argument is a broad synthesis
that leans on space agency sources wherever one exists.
A later article in this series
dates the work that has appeared since the paper
and tests the third claim against it.
Whether such a simulation is commercially viable
is a separate question from whether it is possible,
and the [Time](#time) section below treats it honestly.

## What Is a Model?

A model is an intentional simplification.
Its purpose is to help a person reason about something.
A model is judged by whether it supports the reasoning a problem needs,
not by whether it is true in every detail.

The Bohr model of the atom is the standard example.
In 1913 Niels Bohr placed the electron of hydrogen on discrete circular orbits
and allowed it to radiate only when it jumped between them
[Bohr 1913][research_bohr_1913].
Bohr himself wrote that
"the ordinary mechanics cannot have an absolute validity,
but will only hold in calculations of certain mean values of the motion of the electrons."
The model gives the energy levels of hydrogen.
With $E\_{n}$ the energy of level $n$ in electronvolts
and $n$ a positive whole number,

$$
E_{n} = -\frac{13.6\ \mathrm{eV}}{n^{2}}
\tag{1}
$$

The transition from $n = 3$ to $n = 2$ releases
$13.6 \times \left( \tfrac{1}{4} - \tfrac{1}{9} \right) = 1.89$ electronvolts,
the red Balmer line of hydrogen near 656 nanometres.
The model is wrong about what an electron is and where it goes,
and the shells it describes are not the shells of quantum mechanics.
Yet it gets that number right,
and it is still taught to students meeting atomic structure for the first time.
Physics education researchers have debated whether it should be,
and one study of the debate found that
"Although the evidence for this claim is weak, many have accepted it,"
of the claim that it should not
[McKagan et al. 2008][research_mckagan_et_al_2008].
The Bohr model survives because it is sized to the problem
of a student who needs energy levels and not orbitals.

**Fidelity should be sized to the problem.**
A simple model can be too complex for one task,
and a complicated model can be too simple for another.
A model with every perturbation included
is too complex for a student asking how long a transfer to Mars takes,
because the perturbations hide the answer.
The same model is too simple for a navigator planning a flyby to within a kilometre,
if it omits the one perturbation that matters.
**A problem that needs several models
may need a different fidelity in each.**
A spacecraft simulation might need a precise model of gravity
and a coarse model of crew morale,
or the reverse,
depending on what it is for.

This principle is the measuring stick for the reviews that follow.
A product is not faulted for simplifying.
It is faulted only where its simplification contradicts the physics it claims to show,
or where the simplification defeats the product's own purpose.
The distinction between **omission** and **contradiction**
runs through everything that follows.
A model that leaves a phenomenon out
can still teach truthfully about everything it keeps.
A model that replaces a phenomenon with its opposite
teaches the opposite.
A third case needs naming.
Changing a **parameter**,
such as the size of a planet
or the rate at which time passes,
keeps the laws of physics and teaches them truthfully.
Changing a **law**,
such as adding drag to a vacuum,
contradicts them.

## Review Criteria

Each product is reviewed against the same seven questions.

1. **The physical model.**
   How are gravity and orbits computed?
2. **Travel and propellant.**
   Does moving cost propellant,
   and does travel take the time physics says it takes?
3. **The agents.**
   How many act in one world,
   and in what roles?
4. **Approachability.**
   How much must an agent already know to act at all?
5. **The product's own thesis.**
   What is the product trying to be,
   and does its model serve that aim?
6. **Education.**
   Does a member of the public leave knowing more true physics,
   or more false physics?
7. **What the blueprint takes and refuses.**

## Kerbal Space Program

Kerbal Space Program is a single-agent spaceflight simulation
by the studio Squad.
Its first public release,
version 0.7.3,
came in 2011
[Squad 2011][dev_squad_first_release_2011].
It entered Steam Early Access in March 2013
and reached version 1.0 in April 2015
[Take-Two 2017][dev_take_two_ksp_2017].
Its store page describes it as
"based on realistic aerodynamic and orbital physics"
[Kerbal Space Program][dev_ksp_steam].

**The physical model.**
Kerbal Space Program computes orbits with patched conics.
At any moment a craft feels the gravity of exactly one body,
the one whose sphere of influence it is inside,
and its path is a conic section about that body.
When it crosses into another sphere,
the program switches bodies and patches a new conic onto the old one.
The community wiki on the program's official domain states the consequence plainly.
The design
"allows simplifying the n-body problem to a one-body problem,"
and such simplifications mean that trajectories
"such as Lagrange points"
do not exist in the program
[Sphere of Influence][community_ksp_wiki_soi].
That wiki is edited by the community and is not a statement by the developers.
No developer statement was found.

The sphere of influence comes from Laplace's treatment of the three-body problem,
and standard texts derive it
[Curtis 2020a][book_curtis_2020_interplanetary]
[Battin 1999][book_battin_1999].
With $r\_{\mathrm{SOI}}$ the radius of the sphere,
$a$ the semi-major axis of the smaller body's orbit,
$m$ the mass of the smaller body
and $M$ the mass of the larger,

$$
r_{\mathrm{SOI}} = a \left( \frac{m}{M} \right)^{2/5}
\tag{2}
$$

For Earth about the Sun,
with $a = 1.496 \times 10^{8}$ kilometres
and a mass ratio of $3.003 \times 10^{-6}$,
the radius is about 925,000 kilometres.
Inside that sphere the patched-conic method treats the Sun's pull as absent.
The method is accurate enough for the first plan of most real missions,
so textbooks teach it,
and it fails exactly where the Sun and Earth pull comparably.
That region contains the Lagrange points.
The distance from Earth to its first and second Lagrange points
is close to the Hill radius.
With $r\_{\mathrm{H}}$ the Hill radius
and the other symbols as before,

$$
r_{\mathrm{H}} \approx a \left( \frac{m}{3M} \right)^{1/3}
\tag{3}
$$

For Earth the Hill radius is about 1.5 million kilometres.
That is the distance of the second Lagrange point,
where the James Webb Space Telescope
of the National Aeronautics and Space Administration,
NASA,
orbits the Sun
[NASA Webb Orbit][agency_nasa_webb_orbit],
and it lies outside the sphere of influence computed above.
A patched-conic simulation therefore cannot host the orbit
of one of the most important observatories ever flown.
This is a **contradiction** only for an agent who goes looking for that orbit.
For an agent learning the Hohmann transfer,
it is a sound **omission**.

**Scale.**
The program's home planet,
Kerbin,
has an equatorial radius of 600 kilometres
[Kerbin][community_ksp_wiki_kerbin],
against Earth's mean radius of 6,371 kilometres
[NASA Earth Fact Sheet][agency_nasa_earth_fact_sheet].
The community wiki puts Kerbin at
"approximately one-tenth the radius of Earth."
A smaller planet needs a lower orbital speed,
so a beginner reaches orbit with a small rocket.
This is an approachability choice,
and a good one,
because it changes a parameter and keeps every law.
The program still teaches that orbit is a matter of speed and not of height.

**Higher fidelity through modifications.**
Agents who want more fidelity can install community modifications.
Principia
"implements N-body and extended body gravitation"
so that a craft is
"influenced by all the celestials,"
and its documentation calls the stock behaviour
"the toy physics of the stock game"
[Principia][dev_principia].
Real Solar System
"Changes KSP's solar system to make it like the real one"
[Real Solar System][dev_real_solar_system],
and Realism Overhaul gives parts
"realistic stats and sizes"
[Realism Overhaul][dev_realism_overhaul].
The product thus lets an agent choose fidelity.
The sizing principle of the previous section is here put into practice.

**The agents.**
The stock program has no multiplayer mode
[Multiplayer][community_ksp_wiki_multiplayer].
Community modifications add it.
Dark Multiplayer
"supports subspace style (and master controlled warp) warping"
[Dark Multiplayer][dev_dark_multiplayer],
and Luna Multiplayer
"uses some ideas from DMP like the concept of subspaces,"
DMP being Dark Multiplayer
[Luna Multiplayer][dev_luna_multiplayer].
A subspace is a private timeline.
When one agent accelerates time,
that agent leaves the shared present,
and the others see the agent's craft as it was.
The subspace is an honest answer to a hard problem,
namely that time warp cannot be shared,
and a later article in this series treats it in depth.

**Education.**
Kerbal Space Program has a recorded place in public education.
Squad released an Asteroid Redirect Mission pack in 2014
that it said
"was made in collaboration with NASA,
to make sure our Kerbal version of the Mission was not only true to its real-life counterpart,
but that it was also fun, educational"
[Squad 2014][dev_squad_arm_2014].
NASA later described through its Goddard Space Flight Center a scientist on the asteroid sample return mission
Origins, Spectral Interpretation, Resource Identification, Security, Regolith Explorer,
known as OSIRIS-REx,
challenging the program's users to fly a virtual version of the mission
[NASA 2016][agency_nasa_gamers_osiris_2016].
A school edition,
KerbalEdu,
was described by its publisher as
"an official school-ready standalone remix"
of the program
[KerbalEdu 2016][dev_kerbaledu_2016].
The original program had sold more than two million units by 2017
[Take-Two 2017][dev_take_two_ksp_2017]
and more than five million by 2023
[Take-Two 2023][dev_take_two_ksp2_2023].

**The product thesis.**
Kerbal Space Program set out to make rocketry approachable and fun,
with a textbook physical model as its core.
Its model expresses that thesis well.
**Takes.**
The blueprint takes the textbook core,
the planning tools that let an agent see a future orbit before committing to it,
and the principle that an agent may choose fidelity.
**Refuses.**
It refuses the single-agent world,
and it refuses a fixed patched-conic model where the agents' purposes need more.

## Children of a Dead Earth

Children of a Dead Earth is a space warfare simulation
by Q-Switched Productions,
released on 23 September 2016
[Children of a Dead Earth][dev_code_steam].
Its developer kept a blog through 2016
that explains the physics behind each system,
and the original paper drew on it,
as this article does.

**The product thesis.**
The developer states it directly.
The simulation
"was developed primarily to answer the question: What would space warfare actually be like?"
It was
"designed with no vision in mind,"
because the aim was
"to discover what space warfare would be like,
rather than to say what space warfare would be like"
[How Realistic Is It Actually?][dev_code_realistic_2016].
The developer adds that it is
"a simulation first, and a game second.
No amount of realism was compromised to make things more fun."
That is the right method for a predictive experiment.
It imposes no preconceived notion on the scenario
and lets the equations decide what happens.

**The physical model.**
The simulation uses n-body gravity.
The developer writes that it
"uses an N-Body Simulation to simulate its orbital mechanics,"
that it was
"Originally ... supposed to use Patched Conics,"
and that it
"simulates all manner of Lagrange Point orbits"
[Fun with Orbital Mechanics][dev_code_orbital_2016].
Propulsion,
weapons,
armour,
sensors
and heat rejection
are each derived from engineering equations in the developer's posts
[Burn Rockets Burn][dev_code_rockets_2016]
[Space Guns][dev_code_space_guns_2016]
[The Photon Lance][dev_code_photon_lance_2016]
[Raw Steel][dev_code_raw_steel_2016]
[Stealth in Space][dev_code_stealth_2016].
The developer's post on propellant tanks discusses boil-off,
pressurisation,
ullage
and anti-slosh baffles as matters of tank design and mass
[Slosh Baffles][dev_code_slosh_2016].
Whether the simulation integrates the motion of the liquid itself
is not established by that post.

**What the physics produced.**
The result of letting the equations decide is a tempo
that almost no science fiction shows.
The developer's own example is two fleets in the same orbit,
one running retrograde,
which
"may experience five seconds of combat where the enemy zooms by at ridiculous speeds,
and then ten days of downtime while the crew prepare for another five seconds of combat"
[The Essence of Space Warfare][dev_code_essence_2016].
In the author's experience,
an engagement in the simulation is a great deal of waiting
followed by a deadly high-speed exchange of about thirty seconds.
The arithmetic of closing speed shows why.
With $t\_{\mathrm{e}}$ the time two craft spend within range of each other,
$R$ the effective range of their weapons
and $v\_{\mathrm{rel}}$ their relative speed,
a pass straight through gives

$$
t_{\mathrm{e}} = \frac{2R}{v_{\mathrm{rel}}}
\tag{4}
$$

Two craft in opposite circular orbits at the height of the International Space Station
each move at about 7.7 kilometres per second,
so they close at about 15.3 kilometres per second.
With an effective range of 100 kilometres,
the exchange lasts about 13 seconds.
This equation is a simplification of the author's,
a straight pass at constant speed,
and it shows only the order of magnitude.

**Approachability.**
The developer's posts do not discuss difficulty or the intended audience.
The closest statement is that designing lasers
"is often far more difficult than designing any other system,
so there are plenty of factory-made options"
[The Photon Lance][dev_code_photon_lance_2016].
The fidelity that makes the simulation valuable also makes it a poor fit for the general public in practice.
Its users joke that playing it needs several science degrees.
The author's experience is milder.
Anyone with a proper science degree can work out the parts
that their own programme did not cover.
But a simulation that needs a degree to begin with
is not a simulation for the general public.

**The meta.**
The simulation has a meta,
a set of designs and practices that its agents converge on
because they work well against the model as built.
A meta is the agents' adaptation to the model,
and it is exactly the behaviour the fifth part of the thesis predicts.
It also bounds the experiment's predictive value.
Agents optimise against the simulation's assumptions,
its scenarios
and its omissions,
not against reality,
so where the model departs from reality,
the meta departs with it.
This is not a flaw peculiar to this product.
It is a property every predictive simulation shares,
and it is the reason the blueprint below treats fidelity and approachability together.

**Education.**
The simulation is a wonderful instrument for the people who can work with it
and a poor educational utility for everyone else,
because a lesson nobody takes teaches nothing.
**Takes.**
The blueprint takes the first-principles method,
the n-body core,
derivation from engineering equations,
and the refusal to start from a conclusion.
**Refuses.**
It refuses to expose all of that fidelity to every agent at once.

## EVE Online

EVE Online is a multi-agent space simulation
launched in May 2003
by CCP Games
[CCP 2003][dev_ccp_launch_2003],
which rebranded as Fenris Creations in 2026
after separating from its former parent company,
Pearl Abyss
[Gematsu 2026][news_gematsu_fenris_2026].
In 2013 the developer reported that it
"had surpassed the 500,000 subscriber mark worldwide for the first time,"
and that its agents
"compete for riches, power, glory and adventure in a single universe"
[CCP 2013][dev_ccp_subscribers_2013].
Its human agents are called capsuleers
[Capsuleers][dev_ccp_capsuleers].

**The market.**
The simulation's market is its strongest model.
It is
"Supported by a vast player-run economy,"
and in 2007 the developer appointed an economist,
Eyjólfur Guðmundsson,
who
"will publish quarterly reports on the state of the EVE Online economy"
[CCP 2007][dev_ccp_economist_2007].
The developer still publishes monthly economic reports
[CCP 2026][dev_ccp_mer_2026].
A real economy of real agents,
measured by a professional,
is a model of high fidelity for the thing it models.

**The physical model.**
Every other model in the simulation is
so far from the physics it depicts that it is wrong.
Ships fly as submarines move through water.
The community's own guide gives the velocity law.
With $v(t)$ the speed after $t$ seconds of full propulsion,
$v\_{\max}$ the ship's top speed,
$I$ an inertia modifier in seconds per kilogram
and $M$ the ship's mass in kilograms,
the time constant is $\tau = I M \times 10^{-6}$ seconds and

$$
v(t) = v_{\max} \left( 1 - e^{-t/\tau} \right)
\tag{5}
$$

[Acceleration][community_eve_uni_acceleration].
The same guide says that when propulsion stops,
the ship decelerates to a standstill,
because the model
"assumes that space has some substance to it and thus some friction."
That is the law of a body in a viscous fluid.
Its opposite is Newton's first law,
which NASA states as
"an object in motion remains in motion at constant speed and in a straight line
unless acted on by an unbalanced force"
[Newton's Laws of Motion][agency_nasa_newton].
The simulation's model is therefore not an **omission** of orbital mechanics
but a **contradiction** of inertia.
The community name for it,
submarine physics,
is the community's and not the developer's.

**Travel.**
A ship crosses a solar system by warp.
The developer explains that a warp
"is split in to three phases - Acceleration, Cruise and Deceleration,"
with speed
"measured in AU/s,"
and that a ship must first reach
"the alignment threshold of 75% of its maximum speed"
[CCP 2013a][dev_ccp_warp_2013].
Setting $v(t) = 0.75\,v\_{\max}$ in the velocity law
gives an alignment time of $\tau \ln 4$,
about $1.39\,\tau$.
Warp speeds run from about 1.5 to 8 astronomical units per second
by the community's figures
[Warp][community_eve_uni_warp],
so a crossing that would take a real spacecraft months takes seconds.
Stargates link systems.
No propellant is spent and no delta-v is tracked.
Ships draw on a capacitor that recharges from an onboard generator,
which powers modules and starts each warp,
and only capital jump drives burn fuel
[Capacitor][community_eve_uni_capacitor]
[Jump Drives][community_eve_uni_jump_drives].

**The agents.**
Every agent that matters is a person.
The interactions between them therefore have full fidelity,
because they are not simulated at all.
They are sandboxed interactions under the rules of the simulation,
which the developer itself calls
"sandbox-style gameplay"
[CCP 2013][dev_ccp_subscribers_2013].
**The sum is greater than the parts.**
Poor individual models,
joined by a real market and real people,
produce alliances,
wars,
espionage
and economic history
that no single component could.

### The Economy

EVE Online is fascinatingly odd here.
Its individual models are terrible,
yet they interlock so comprehensively that the whole has real predictive value.
The commodity market is the one place where the model is strong and accurate,
because it is not simulated at all.
Real agents set every price,
so the market behaves as markets do.

**The supply chain.**
The community guide describes industry as
"a catch-all term for all the industrial activities within EVE: mining, gas huffing, manufacturing, researching, invention, reprocessing, and reverse engineering"
[Industry][community_eve_uni_industry].
Agents mine ore,
reprocess it into minerals,
haul the minerals to a facility,
manufacture ships and modules from blueprints,
and sell them.
Every ship destroyed in combat is gone,
so destruction drives demand back down the chain.
In the parts,
this is complete science fantasy.
The minerals have invented names,
a blueprint turns them into a warship without any physics of manufacture,
and nothing about the process resembles a real shipyard.
As a system,
it is the best multi-agent supply chain the author knows of,
logistics included.

**Right-sized fidelity.**
EVE Online's wrong models have the right fidelity for the problem they actually serve,
which is driving meaningful interaction between agents.
By the sizing principle of this article,
that is a success.
A supply chain that is realised and workable
matters more to that problem than one that is accurate.
Being able to navigate at all,
and to operate from and in different places,
matters more than navigating realistically.
EVE Online therefore passes the fidelity test for its own purpose
and fails it for education.
The blueprint below must pass both.
The author's view is that more realistic simplified models could have worked in EVE Online,
but that the developer lacked the right people to distil them for the product.
In some cases the incorrectness serves the soft science fiction thesis itself.
EVE's base mineral is Tritanium,
which the developer describes as
"The main building block in space structures"
[Tritanium][dev_ccp_esi_tritanium].
The word is Star Trek's.
In the episode "Obsession" of 1967,
Spock reports
"Pure tritanium"
and Kirk replies
"20 times as hard as diamond"
[Obsession Transcript][community_trek_obsession_transcript].
A reporter noted in 2008 that EVE's tritanium
"hearkens back to references made in Star Trek"
[Engadget 2008][news_engadget_tritanium_2008].
No statement by the developer on the name's origin was found,
so the borrowing is the author's reading,
of technobabble pulled into the base of a supply chain.

**Industry costs.**
The developer publishes its formulas.
With $C\_{\mathrm{job}}$ the cost of installing an industry job,
$V\_{\mathrm{EIV}}$ the estimated item value of its output,
$I\_{\mathrm{SCI}}$ the cost index of the solar system,
$\beta$ the product of the facility's bonuses,
and $t\_{\mathrm{f}}$,
$t\_{\mathrm{SCC}}$
and $t\_{\alpha}$ the facility tax,
a fixed surcharge
and a surcharge on accounts without a subscription,
the developer's own statement,
"TIF = EIV * ((SCI * bonuses) + FacilityTax + SCC + AlphaClone),"
reads

$$
C_{\mathrm{job}} = V_{\mathrm{EIV}} \left( I_{\mathrm{SCI}}\, \beta + t_{\mathrm{f}} + t_{\mathrm{SCC}} + t_{\alpha} \right)
\tag{6}
$$

[CCP 2023][dev_ccp_viridian_2023].
The cost index is congestion pricing.
When it was introduced in 2014,
the developer defined it from
"the number of job-hours of that activity type in that system over the last 28 days,
divided by the number of job-hours of that activity type in the universe as a whole over the last 28 days,
and then square-rooted"
[CCP 2014][dev_ccp_industry_2014].
With $h\_{\mathrm{sys}}$ and $h\_{\mathrm{all}}$ those two totals,
the index in that form grows as

$$
I_{\mathrm{SCI}} \propto \sqrt{\frac{h_{\mathrm{sys}}}{h_{\mathrm{all}}}}
\tag{7}
$$

A system that hosts four times another's share of production
pays twice the index,
so production spreads out across the map instead of piling into one system.
The community guide warns that a later patch changed the index
and that the square-root form is probably no longer exact.

Materials obey a rule of their own.
The same 2014 account states that
"Each step of ME reduces materials by 1% (always rounded up),"
that rounding now happens per job and not per run,
and that
"every run requires a minimum of one unit of every listed material"
[CCP 2014][dev_ccp_industry_2014].
With $n\_{\mathrm{mat}}$ the quantity of one material a job consumes,
$r$ the number of runs,
$n\_{0}$ the blueprint's base quantity per run,
$E$ its material efficiency level
and $\gamma$ the facility's material modifier,
those rules assemble into

$$
n_{\mathrm{mat}} = \max\!\left( r,\ \left\lceil r\, n_{0} \left( 1 - \frac{E}{100} \right) \gamma \right\rceil \right)
\tag{8}
$$

A blueprint calling for 1,000 units per run at a material efficiency of 10,
run 10 times with no facility bonus,
consumes 9,000 units.

**The market.**
Prices are set by agents in regional markets,
and the developer's own economist has noted
"the unrelenting dominance of Jita as a central hub"
[CCP 2015][dev_ccp_economy_vegas_2015].
Every sale pays a sales tax,
raised in 2025
"from 4% to 7.5%"
[CCP 2025][dev_ccp_patch_22_02_2025],
and every order pays a broker's fee.
Player structures set their own fees,
and the developer observes that
"It is not uncommon for structure owners to give themselves and their friends a 0% fee"
[CCP 2020][dev_ccp_broker_relations_2020].
A haul between two hubs is worth making only when the margin survives the fees.
With $p\_{\mathrm{A}}$ the price paid at the source,
$p\_{\mathrm{B}}$ the price received at the destination,
$\lambda\_{\mathrm{s}}$ the sales tax rate,
$f\_{\mathrm{b}}$ the broker's fee rate
and $c\_{\mathrm{h}}$ the cost of hauling one unit,
a trade pays when

$$
p_{\mathrm{B}} \left( 1 - \lambda_{\mathrm{s}} - f_{\mathrm{b}} \right) - p_{\mathrm{A}} \left( 1 + f_{\mathrm{b}} \right) - c_{\mathrm{h}} > 0
\tag{9}
$$

The community guide gives the sales tax as 7.5 percent reduced by 11 percent per level of the Accounting skill,
and the broker's fee as 3 percent less 0.3 percent per level of Broker Relations
[Trading][community_eve_uni_trading].
At the fifth level of each,
the rates are about 3.4 and 1.5 percent.
Buying at 100 and selling at 110 then leaves about 3.1 per unit,
so a hauler earns its living on a margin near 3 percent.

**Logistics.**
Hauling is a profession.
The developer's profile of one hauling corporation,
Red Frog Freight,
says that
"It works a little bit like a real life logistics company, with around 600-700 contracts daily"
[CCP 2013b][dev_ccp_red_frog_2013].
Courier contracts carry collateral held in escrow,
so a hauler who loses the cargo pays for it.

**Money.**
The developer described its money supply in 2006 in terms an economist would use.
"We call anything that introduces money into the economy an ISK Faucet
and anything that takes it out again an ISK Sink"
[CCP 2006][dev_ccp_faucets_2006].
In 2012 it reported that bounties were the largest faucet,
"33 trillion ISK"
in one month,
and that three of four price indices showed
"considerable inflation"
[CCP 2012][dev_ccp_price_indices_2012].

**PLEX and real money.**
In 2008 the developer let subscribers convert paid game time into an item,
the
"30 Day Pilot's License Extension (PLEX),"
which could be put
"directly on to the market"
[CCP 2008][dev_ccp_plex_2008].
A PLEX
"can be bought via the in-game market for ISK and then applied to add 30 days of game time"
[CCP 2009][dev_ccp_plex_2009],
and in 2017 each was converted
"into 500 PLEX"
[CCP 2017][dev_ccp_plex_2017].
PLEX gave the economy a legal exchange rate with real money.
The developer's own announcement said it
"Opens up for a larger supply, lowering the ISK exchange rate in the long run"
[CCP 2008][dev_ccp_plex_2008],
and its economist later called it
"EVE's equivalent of the gold standard"
[CCP 2015][dev_ccp_economy_vegas_2015].
A press report of 2014 records the developer selling PLEX from a reserve
to stop a price spike
[Engadget 2014][news_engadget_plex_2014],
which is a central bank's open market operation.
Trade outside that channel is forbidden.
The licence the developer quotes says that agents may not
"transfer, sell or auction, or buy or accept any offer to transfer, sell or auction"
anything in the simulation,
"including without limitation characters, character attributes, items, currency, and objects"
[CCP 2016][dev_ccp_rmt_2016],
and its security team reported banning 70,492 accounts in 2021 for all causes
[CCP 2022][dev_ccp_security_2021].
The exchange rate also prices destruction.
Of the battle of B-R5RB in 2014,
the developer reported losses of
"11 TRILLION ISK"
and that
"According to some PLEX conversions that could equate to approximately $300,000-$330,000 USD"
[CCP 2014a][dev_ccp_b_r5rb_2014].

**Real phenomena that appeared unbidden.**
Because the interlocking parts reproduce real incentives,
real economic behaviour appeared without being designed.
- **Tax havens.**
  The simulation's starter corporations once offered
  "war declaration immunity and 0% tax,"
  which the developer said gave them
  "an inherent advantage over player corporations which was never intended"
  [CCP 2009a][dev_ccp_taxes_2009].
  The developer responded in 2009 by taxing the starter corporations at 11 percent,
  a rate it chose after researching the average taxes of player corporations.
  Its economist had already measured corporate taxation,
  finding that
  "The average tax rate is 8.6% but the median is tax rate is 5%"
  [CCP 2007a][dev_ccp_corporations_2007].
- **Bank failures and embezzlement.**
  In 2009 an agent who ran a player bank,
  EBank,
  embezzled
  "roughly 200 billion ISK, or 8.6% of EBANK's 2.3 trillion ISK in deposits"
  [Engadget 2009][news_engadget_ebank_2009],
  and sold part of it for real money,
  about five thousand United States dollars
  [The Register 2009][news_register_ebank_2009].
  The developer's economist said the bank would have to solve the problem itself,
  since it was
  "a player driven entity"
  [IEEE Spectrum 2009][news_ieee_ebank_2009].
- **Cartels.**
  A scarce resource found
  "completely in one distinct region"
  caused,
  in the developer's words,
  "wealth transfers that are simply too large for the effort and risk involved"
  [CCP 2012a][dev_ccp_technetium_2012],
  and a community history describes the cartel that formed to manipulate its price
  [EVE News24 2018][news_evenews24_otec_2018].
- **Central banking.**
  Faucets,
  sinks,
  inflation indices
  and open market sales of PLEX
  are monetary policy under other names.

**Skills that transfer.**
High-commitment simulations can hold their agents to very high expectations,
and the transfer runs both ways.
A survey reported in an article presented by the developer
found that
"56% of players said that skills they learned through playing EVE had proven to be valuable in their lives outside of the game and in their careers"
[Den of Geek 2020][news_den_of_geek_2020].
The source is sponsored,
and the underlying study was not found,
so the figure is reported as the developer's claim.

**Education.**
EVE Online largely simulates the science fiction of film and television,
and its soft science fiction sandbox borders on miseducating the public,
because it teaches a generation that ships coast to a stop
and that a solar system is a few seconds wide.
**Takes.**
The blueprint takes the market,
the single shared world,
real people as agents,
and the lesson that systemic interaction can matter more to agents
than the realism of any one component.
**Refuses.**
It refuses drag in vacuum,
free travel,
and the absence of propellant.

## Star Citizen

Star Citizen is a multi-agent space simulation by Cloud Imperium Games.
It remains in alpha testing as of this writing.
A secondary report states that its crowdfunding passed one billion dollars on 24 May 2026,
from over 6.5 million registered contributors,
with no release date
[The FPS Review 2026][news_fps_review_sc_2026].
Its Alpha 4.0 release introduced server meshing,
with shards of up to 500 agents
[Star Citizen Alpha 4.0][dev_rsi_alpha_40].

**The product thesis.**
The developer's chairman,
Chris Roberts,
describes the aim as
"a First Person Universe that allows you to live a virtual life in a compelling futuristic setting"
[Roberts 2018][dev_rsi_letter_2018],
and as the ability to
"immerse you as a player into your own adventure to rival any big budget movie"
[Roberts 2020][dev_rsi_letter_2020].
The product thesis is that agents can play out adventures
as if they were the stars of their own films.
Its roles are rich and asymmetric,
including
"exploration, hauling, trading, mercenary, outlaw, bounty hunting and mining,"
with more planned
[Roberts 2020][dev_rsi_letter_2020].

**Travel and propellant.**
Ships cross a system by quantum travel,
a warp in all but name,
and the same handwave of travel inconvenience that EVE Online makes.
Unlike EVE Online,
Star Citizen tracks propellant.
The developer explains that
"The ship's thrusters consume fuel stored in the Hydrogen Fuel Tank,"
and that
"When in Quantum Travel, thrusters use the fuel contained in the Quantum Fuel Tank"
[The Shipyard: Fuel Mechanics][dev_rsi_fuel_2018].
The fuel model is of very low fidelity,
and it would be surprising if propellant slosh were simulated at all.
The author understands Kerbal Space Program to treat each tank
as a point mass that varies between its wet and dry masses,
which also leaves slosh out.
Slosh matters in real craft.
A NASA monograph of 1966 devoted to the behaviour of liquids in moving containers
treats it as a problem of space vehicle technology
[Abramson 1966][research_abramson_1966],
because a shifting mass of propellant moves the centre of mass and couples into attitude control.

**The physical model of the system.**
The developer's release notes for Alpha 3.0 state that
"Planets and moons now rotate to give a day/night cycle"
[Star Citizen Alpha 3.0.0][dev_rsi_alpha_300_2017].
No developer statement was found on whether the bodies revolve about their star.
The community wiki states that the planets
"spin, have a day and night cycle, and are planned to eventually orbit"
[Planet][community_sc_tools_planet].
On that evidence,
which is the community's and not the developer's,
the bodies rotate in place at fixed positions,
and orbits are not simulated.
That matches the understanding
that a body sits at fixed coordinates that a ship warps to.

**Gravity.**
Ships and stations carry artificial gravity.
The developer's design brief for it says that it
"must be able to be turned on and off,"
and that
"'handwavium' is completely acceptable if it makes sense"
[Lore Builder Twenty][dev_rsi_lore_gravity_2014].
Gravity of that kind is the gravity of film and television,
and the next part treats it.

**Launch and reentry.**
Since 2020 the simulation has modelled lift and drag in atmosphere.
The developer states that
"Ships with wings are now able to stall"
and that
"In atmosphere, thrusters now lose efficiency and become much weaker"
[Flight and Fight Improvements][dev_rsi_flight_2020].
No source was found for reentry heating as a hazard
or for any requirement to reach orbital speed in order to reach orbit.
Launch and reentry are flown through but are not modelled as the challenges they are.

**Education.**
Star Citizen is a multi-agent soft science fiction reenactment,
and its model expresses that thesis well.
Like EVE Online,
it is a soft science fiction sandbox that borders on miseducating the public.
**Takes.**
The blueprint takes asymmetric roles,
the seamless movement between a ship's interior,
a planet's surface and space,
and tracked propellant.
**Refuses.**
It refuses artificial gravity without a mechanism,
travel without time,
and bodies that do not orbit.

## Why the Products Look As They Do

None of the four products has failed.
Each model expresses its product's thesis
under the constraints its makers faced,
and this is the most important finding of the review.
Kerbal Space Program wanted approachable rocketry and got it.
Children of a Dead Earth wanted to discover space warfare and did.
EVE Online wanted a single universe of real people with a real economy,
and Star Citizen wants agents to live their own films.

The developers are generally competent.
Each product reflects a combination of product-market fit and its product thesis.
Where a simulation falls short of the standard this article sets for high-fidelity space simulation,
it is because it had a different product thesis
and the developer achieved it,
or because the developer failed in the attempt,
as Kerbal Space Program 2 did.
Many other titles succeed on their own terms
as multi-agent soft science fiction simulations.
Falling short of that standard is not a failure of craft.
It is a choice of target.

Staffing is part of the explanation.
A model of high fidelity costs specialists to build and to maintain.
A small studio can afford it only in a narrow product,
as Children of a Dead Earth shows,
and a large studio can afford it only if its market rewards it.
The products that drew the largest audiences drew them with the simplest physics.
That is the gap the thesis names.
No known product has yet paid for physics that does not cheat
in a product built for many agents and the general public at once.

Management is the other part,
and two products show it.
Kerbal Space Program 2,
a sequel by a new studio,
Intercept Games,
entered early access in February 2023
[Take-Two 2023][dev_take_two_ksp2_2023].
In 2024 the press reported a state layoff notice for seventy employees
that it tied to the studio,
although the notice did not name it
[PC Gamer 2024][news_pc_gamer_intercept_2024].
The project was fatally mismanaged,
and it is a development since the paper.
Star Citizen is mismanaged in a different way.
It has stayed in alpha for well over a decade,
yet it has found an odd market equilibrium
in which a nominally unfinished product earns large recurring revenue
[The FPS Review 2026][news_fps_review_sc_2026].
Setting the ethics of that model aside,
Star Citizen is plainly doing something right
even as it does a number of other things wrong.
Neither case is evidence against the competence of developers in general.
Both show that an ambitious space simulation is expensive and risky.
The fourth claim names exactly that constraint.

## Soft Science Fiction and Its Remedies

The two multi-agent products inherit their physics from film and television.
This part traces where the conventions came from,
catalogues the ones a space simulation is likely to repeat,
and gives a remedy for each.
The remedy is usually a version of
do not do that,
or use real physics.

### Where the Conventions Came From

Star Trek began as a western.
Gene Roddenberry's pitch of 1964 opened with the line
"STAR TREK is a 'Wagon Train' concept,"
built around characters who travel to worlds
"similar" to our own
[Gizmodo 2011][news_gizmodo_trek_pitch_2011],
and the format reprinted in the 1968 account of the production
reads "Wagon Train to the Stars"
[Whitfield and Roddenberry 1968][book_whitfield_roddenberry_1968].
A western brings a fixed cast to a new town each week.
A space western needs the same cast on a new world each week,
whatever the distance.
The same account records the production reasons behind two devices.
Of landing the ship,
Roddenberry asked whether they could
"LAND A SHIP FOURTEEN STORIES TALL ON A PLANET SURFACE EVERY WEEK?"
and answered that the budget
"FORCED US INTO CONCEIVING THE TRANSPORTER DEVICE."
Planets like Earth were likewise
"a compromise with production costs."
No primary source was found that says warp drive was chosen for the same reason.
That it served the same purpose,
literally a wave of the hand that delivers the cast to the next adventure,
is the author's inference from the format.

EVE Online and Star Citizen inherit that model of travel.
They can justify it for the same reasons the series did.
Both put agents into adventures in a shared world,
and the adventures need the agents to be in the same place at the same time.
The justification is real,
but it is a justification for the format,
not a description of space.

Two causes kept these conventions alive.
The first is that the writers were often not educated in the physics they depicted.
The second is that effects budgets limited what could be shown faithfully.
The second argument weakens with every year since the arrival of computer-generated imagery.
The Last Starfighter of 1984 carried about twenty-five minutes of computer-generated imagery in about 230 scenes,
rendered on a Cray X-MP
[SIGGRAPH][ref_siggraph_last_starfighter].
On Babylon 5,
J. Michael Straczynski credited Ron Thornton
as the one who
"first suggested we use CGI"
[Straczynski 2013][news_slashdot_straczynski_2013].
The Expanse later showed that a large audience will accept spin gravity and thrust gravity.
Its co-author Daniel Abraham described ships
"having thrust gravity and spin gravity and ships that are built like towers,"
while conceding that its drive is handwavium
[Space.com 2015][news_space_com_expanse_2015].
Rendering a coasting ship now costs no more than rendering a banking one.
What remains is a choice.

### The Science Fiction Loop

Science fiction inspires children to become scientists,
and science inspires the writers of science fiction.
Michio Kaku recalls that at about eight
"I got hooked on the Saturday morning TV shows. In particular, Flash Gordon"
[Kaku 2015][news_big_think_kaku_2015].
Stephen Hawking co-wrote a series of children's adventure novels with his daughter Lucy,
beginning with George's Secret Key to the Universe in 2007
[Hawking and Hawking 2007][book_hawking_hawking_2007].
NASA chose Nichelle Nichols,
who played Uhura in Star Trek,
to record a recruiting video and speak to audiences nationwide in the late 1970s,
and NASA records that astronaut Mae Jemison
"credits Nichelle Nichols as her inspiration to become an astronaut"
[NASA 2024][agency_nasa_star_trek_55_2024].
A peer-reviewed survey of 575 Doctor Who viewers
found reported effects ranging from fact-checking the series' science
"to inspiring them to pursue a science career"
[Orthia 2019][research_orthia_2019].

The loop runs whatever the hardness of the fiction.
What the hardness changes is the fidelity of what passes through it,
the ideas the children carry
and the training they seek.
A child inspired by a ship that coasts to a stop
must later unlearn it.
For that reason solving the problem described here
is of direct relevance to educating the public
for the future benefit of humanity.
A simulation is a participatory medium.
It does not only show a convention,
it trains its agents to act on it.

### The Catalogue

Each entry gives the convention,
where it appears,
the correct physics
and the remedy.

**Ships that stop when the engine stops.**
EVE Online's velocity law above is the clearest case in a simulation,
and film and television do the same whenever a ship slows without firing a thruster.
In vacuum a ship keeps its velocity
[Newton's Laws of Motion][agency_nasa_newton].
**Remedy.**
Use Newton's first law.
A ship that wants to stop must spend as much delta-v as it spent to start.

**Banking turns, wings in vacuum and dogfights.**
A banking turn uses air.
In vacuum a craft turns by reaction control,
a set of small thrusters that the Space Shuttle used
"to provide propulsion thrust for precise attitude control and three-axis translation"
[Blevins and Hohmann 1975][agency_nasa_shuttle_rcs_1975].
Rotating a craft does not change the direction it moves.
Only thrust along the new heading does.
Star Citizen's atmospheric model is correct to give wings lift in air.
The error is to carry the behaviour into vacuum.
**Remedy.**
Separate attitude from velocity,
and give wings effect only where there is air.

**Rockets that push against air.**
NASA's educational pages address the question of
"how they can work in space where there is no air for them to push against,"
and answer that
"The answer to this question comes from the third law"
[Rocket Principles][agency_nasa_rocket_principles].
**Remedy.**
Show exhaust momentum as the source of thrust,
and let a rocket perform better in vacuum than in air,
as it does.

**Travel without time.**
Warp in EVE Online and quantum travel in Star Citizen deliver a ship in seconds.
Real travel takes time set by orbital mechanics,
and the delta-v of a transfer sets what it costs
[Orbital Manoeuvres][related_post_orbital_manoeuvres].
The rocket equation connects delta-v to propellant.
With $\Delta v$ the change in velocity,
$I\_{\mathrm{sp}}$ the specific impulse in seconds,
$g\_{0}$ standard gravity at 9.80665 metres per second squared,
$m\_{0}$ the initial mass
and $m\_{\mathrm{f}}$ the final mass,

$$
\Delta v = I_{\mathrm{sp}}\, g_{0} \ln \frac{m_{0}}{m_{\mathrm{f}}}
\tag{10}
$$

An engine with a specific impulse of 450 seconds and a mass ratio of four
gives a delta-v of about 6.1 kilometres per second.

Time is the other cost.
The cheapest transfer between two circular orbits is the Hohmann transfer,
half an ellipse that touches both
[Curtis 2020a][book_curtis_2020_interplanetary].
With $t\_{\mathrm{H}}$ the transfer time,
$a\_{\mathrm{t}}$ the semi-major axis of the transfer ellipse,
the mean of the two orbital radii,
and $\mu\_{\odot}$ the Sun's gravitational parameter at $1.327 \times 10^{11}$ cubic kilometres per second squared,

$$
t_{\mathrm{H}} = \pi \sqrt{\frac{a_{\mathrm{t}}^{3}}{\mu_{\odot}}}
\tag{11}
$$

From Earth at 1.000 astronomical units to Mars at 1.524,
the transfer ellipse has a semi-major axis of 1.262 astronomical units,
or $1.888 \times 10^{8}$ kilometres,
and the transfer takes about 259 days.
Nor can it begin at any moment.
The planets return to the same relative position once each synodic period.
With $S$ the synodic period
and $T\_{1}$ and $T\_{2}$ the orbital periods of the inner and outer planets,

$$
\frac{1}{S} = \frac{1}{T_{1}} - \frac{1}{T_{2}}
\tag{12}
$$

For Earth at 365.25 days and Mars at 686.98,
the synodic period is about 780 days,
so a window for the cheapest transfer to Mars opens about once every 26 months
[Curtis 2020a][book_curtis_2020_interplanetary].
**Remedy.**
Track propellant and delta-v,
and make travel take its true time.
The blueprint below gives travel time a job instead of hiding it.

**Bodies that do not orbit, and ships that hover.**
A planet or moon in a fixed position cannot teach orbital mechanics.
A ship that holds position above a point on a planet
needs a geostationary orbit,
which exists only above the equator
and is circular at an altitude of 35,786 kilometres,
where a satellite moves at about 3 kilometres per second,
as the European Space Agency,
ESA,
describes it
[ESA 2020][agency_esa_geo_2020].
With $r\_{\mathrm{G}}$ the radius of the orbit,
$\mu$ Earth's gravitational parameter at 398,600 cubic kilometres per second squared
and $T$ the sidereal day of 86,164 seconds,

$$
r_{\mathrm{G}} = \left( \frac{\mu T^{2}}{4 \pi^{2}} \right)^{1/3}
\tag{13}
$$

The radius is 42,164 kilometres,
or 35,786 kilometres above the equator.
Everywhere else,
holding position costs thrust continuously.
**Remedy.**
Put every body on its true orbit,
and let a ship hold position only where physics allows it.

**Space is far away.**
Space begins low.
The Fédération Aéronautique Internationale describes
"the 100km altitude used by FAI and many other organisations"
as the boundary of space
[FAI 2018][ref_fai_karman_2018].
What makes orbit hard is speed.
With $v\_{\mathrm{c}}$ the speed of a circular orbit
and $r$ its radius from Earth's centre,

$$
v_{\mathrm{c}} = \sqrt{\frac{\mu}{r}}
\tag{14}
$$

At the height of the International Space Station,
about 420 kilometres up,
the radius is 6,791 kilometres
and the speed is about 7.66 kilometres per second.
**Remedy.**
Teach that orbit is a speed,
which Kerbal Space Program already does at its smaller scale.

**Zero gravity in orbit.**
Orbiting astronauts are in free fall,
not out of gravity.
NASA's own explanation for students says that at the station's altitude
"Earth's gravity is about 90 percent of what it is on the planet's surface,"
and that microgravity
"is sometimes called 'zero gravity,' but this is misleading"
[NASA 2012][agency_nasa_microgravity].
With $g(h)$ the acceleration of gravity at altitude $h$,
$g\_{0}$ its value at the surface
and $R$ Earth's radius,

$$
g(h) = g_{0} \left( \frac{R}{R + h} \right)^{2}
\tag{15}
$$

At 420 kilometres the ratio is about 0.88.
**Remedy.**
Call it free fall or microgravity,
and show that the station is falling around Earth.

**Magic artificial gravity.**
Floors that pull downward by an unexplained mechanism,
switched on and off at will,
are the gravity of film and television
and of Star Citizen's design brief
[Lore Builder Twenty][dev_rsi_lore_gravity_2014].
The physics offers two kinds of gravity on a ship,
rotation and thrust.
NASA's 1977 design study of a space settlement chose rotation,
writing that
"To simulate Earth's normal gravity the entire habitat rotates at one revolution per minute about the central hub,"
that people living permanently in space
"should live between 0.9 g and 1 g,"
and that rates
"greater than 1 rpm should be avoided"
[Johnson and Holbrow 1977][agency_nasa_sp413_1977].
With $a\_{\mathrm{c}}$ the acceleration felt at the rim,
$\omega$ the rate of rotation in radians per second
and $r$ the radius,

$$
a_{\mathrm{c}} = \omega^{2} r
\tag{16}
$$

At one revolution per minute,
$\omega$ is about 0.105 radians per second,
and the study's radius of 830 metres
gives about 9.1 metres per second squared,
or 0.93 of standard gravity.
**Remedy.**
Give gravity a mechanism.
Use spin for habitats and thrust for ships under way,
as The Expanse does,
and let free fall be the condition of a coasting ship.

**Shields.**
The force field of film and television has no basis in physics.
Spacecraft do carry shields,
of a different kind.
NASA's Hypervelocity Impact Technology group records that
"The Whipple Shield is the first spacecraft shield ever implemented"
and
"is still in use today"
[NASA Whipple Shield][agency_nasa_whipple],
after Fred Whipple's proposal of 1947
[Whipple 1947][research_whipple_1947].
A Whipple shield is a thin bumper held off the hull,
which breaks up an impacting particle before it reaches the wall.
Active magnetic shielding against radiation has been studied
[Westover et al. 2019][agency_nasa_maarss_2019]
but remains a concept.
**Remedy.**
Model armour,
Whipple shields
and radiation shielding as mass,
and do not add force fields.

**Stealth, waste heat and radiators.**
Every powered spacecraft must reject its waste heat,
and in vacuum it can do so only by radiation.
NASA's small spacecraft guidance states that
"In a vacuum, heat is transferred only by radiation and conduction with no convection"
[NASA Thermal Control][agency_nasa_smallsat_thermal],
and the International Space Station's external thermal system has
"a total capability of 70 kW"
[ISS Active Thermal Control][agency_nasa_iss_atcs].
With $P$ the power radiated,
$\varepsilon$ the emissivity of the radiator,
$\sigma$ the Stefan-Boltzmann constant at $5.670 \times 10^{-8}$ watts per square metre per kelvin to the fourth,
$A$ the radiating area
and $T$ its temperature in kelvin,

$$
P = \varepsilon \sigma A T^{4}
\tag{17}
$$

A radiator at 275 kelvin with an emissivity of 0.9
rejects about 292 watts per square metre,
so 70 kilowatts needs about 240 square metres facing cold space,
before any allowance for sunlight absorbed.
That glowing area is visible to an infrared sensor,
and one optics study observes that
"By observing the radiator, we can catch a glimpse of a spacecraft's inner information"
[Li et al. 2017][research_li_et_al_2017].
The developer of Children of a Dead Earth goes further and argues that there is
"no stealth in space"
[The Essence of Space Warfare][dev_code_essence_2016].
No agency or peer-reviewed source makes that claim in general,
so this article treats it as the developer's argument.
**Remedy.**
Model heat as a resource that must be rejected,
give every craft a thermal signature,
and do not let a ship vanish.

**Space is cold.**
Vacuum is an insulator,
as the thermal guidance above implies.
A body in vacuum loses heat only by radiation,
which is slow,
so nothing freezes instantly.
**Remedy.**
Model thermal balance,
in which a spacecraft's harder problem is often getting rid of heat.

**Exposure to vacuum.**
Bodies do not explode,
and nobody freezes solid at once.
A NASA account of pressure suits describes a 1965 chamber accident
in which the subject
"remained conscious for about 14 seconds, then lost consciousness,"
and states that
"You would not instantly freeze solid, as some movies have shown"
[NASA 2017][agency_nasa_pressure_suits_2017].
**Remedy.**
Show the documented effects,
which are serious enough without exaggeration.

**Sound in space.**
NASA states that
"Sound waves cannot travel in the vacuum of space
because there is no medium to transmit these mechanical waves"
[Anatomy of an Electromagnetic Wave][agency_nasa_em_anatomy].
**Remedy.**
Silence outside,
and sound only where it can travel,
through the hull and the air inside.

**Visible beams and slow bolts.**
A laser beam is invisible from the side in vacuum.
A manufacturer of optics notes that
"In the absence of any type of scattering medium,
the beam will only be visible as a spot when it reaches its target"
[Edmund Optics][ref_edmund_laser],
and NASA notes that the infrared light used for its laser communications
"is invisible to human eyes"
[NASA 2021][agency_nasa_laser_comm_timeline_2021].
A bolt of light that travels slowly enough to watch is not light.
**Remedy.**
Show beams only by their effect,
and give projectiles their true speeds.

**Fireball explosions.**
An explosion in space has no air to carry a blast wave
and no oxygen to sustain a fire.
The nuclear effects literature records that the fraction of energy
"converted into blast and shock is less and decreases with increasing altitude"
[Glasstone 1964][book_glasstone_1964],
though a high-altitude nuclear test can still form a fireball,
so the physics is subtler than film and simpler than fire.
The developer of Children of a Dead Earth puts the practical result bluntly,
that in space
"explosions are pitifully weak"
[The Essence of Space Warfare][dev_code_essence_2016].
**Remedy.**
Model the energy delivered,
not the spectacle,
and let kinetic energy carry the damage.

**Dense asteroid fields.**
A ship weaving among tumbling boulders is a set piece of film.
NASA's Dawn mission team answers that if the main belt's asteroids of a mile across or larger were spread evenly,
"the average distance between individual asteroids 1 mile in diameter or larger would be about 1.9 million miles,"
nearly eight times the distance between Earth and the Moon,
and that the science fiction depiction of boulders
"jostling for space"
is
"not the case at all"
[NASA Dawn FAQ][agency_nasa_dawn_faq].
**Remedy.**
Put the asteroids where they are,
almost everywhere far apart.

**Instant communication.**
Light takes time.
NASA's Goddard communications staff note that
"Movies and television shows can make communicating with space look easy"
[NASA 2020][agency_nasa_space_comms_2020],
and a NASA technical memorandum gives Mars an
"up to 22-minute one-way (44-minute round-trip) delay at maximum distance from Earth"
[Landon et al. 2025][agency_nasa_tm_2025_mars_comms].
With $t\_{\mathrm{L}}$ the one-way delay,
$d$ the distance
and $c$ the speed of light,

$$
t_{\mathrm{L}} = \frac{d}{c}
\tag{18}
$$

At its closest,
about 0.37 astronomical units,
Mars is about 3.1 light-minutes away,
and at its farthest,
about 2.67 astronomical units,
about 22 light-minutes.
**Remedy.**
Delay every message and every sensor reading by its light time.
This single rule changes command,
markets
and warfare more than any other,
and Children of a Dead Earth's developer notes that
"seconds or even minutes of lag in command would prove fatal in combat"
[How Realistic Is It Actually?][dev_code_realistic_2016].

**Reentry by friction, and launch without cost.**
Reentry heating is popularly described as friction.
The dominant mechanism for a blunt body is compression in the shock layer ahead of it.
Allen and Eggers showed in 1958 that
"for any truly blunt body, the bow shock wave is detached,"
which is why capsules are blunt
[Allen and Eggers 1958][research_allen_eggers_1958].
NASA's own history of reentry uses both descriptions,
the heat of
"shock wave compression"
and
"aerodynamic heating, a product of the friction of the high-speed airflow"
[Launius and Jenkins 2012][agency_nasa_coming_home],
so friction is not wrong so much as incomplete.
**Remedy.**
Model ascent and reentry as the delta-v and thermal problems they are,
which no reviewed multi-agent simulation does.

**Propellant without slosh.**
A tank of liquid propellant is not a fixed mass.
The liquid moves,
shifts the craft's centre of mass
and couples into its attitude control.
The NASA monograph cited above exists for that reason
[Abramson 1966][research_abramson_1966].
**Remedy.**
Model slosh where a subsystem needs it,
in docking,
landing
and fine pointing,
and size it out where it does not.

**Humanoid aliens.**
The humanoid alien of film and television was often a prosthetic on an actor,
and the same production account that records the transporter
records that worlds like Earth were
"a compromise with production costs"
[Whitfield and Roddenberry 1968][book_whitfield_roddenberry_1968].
Science disagrees about whether evolution elsewhere would converge on human forms.
Simon Conway Morris argues for strong convergence
[Conway Morris 2003][book_conway_morris_2003],
and Levin and colleagues argue from natural selection
that alien life is predictable in its processes rather than its shapes
[Levin et al. 2017][research_levin_et_al_2017].
**Remedy.**
For a simulation of near-term space,
do not include aliens.
None is known.

**Tractor beams and inertial dampeners.**
A NASA study of optical trapping reports that
"tractor beams do exist but can only move a limited number of targets over micron-level distances"
[Stysley 2011][agency_nasa_niac_stysley_2011].
No source of any kind was found for inertial dampeners.
**Remedy.**
Do not include either.

**Black holes that suck.**
NASA states that black holes do not suck in other matter,
and that
"From far enough away, their gravitational effects are just like those of other objects of the same mass"
[NASA Black Holes][agency_nasa_black_holes].
**Remedy.**
Use the gravity of the mass,
which an n-body model does without being told.

## A Blueprint

The reviews and the remedies converge on one design.
It describes a high-fidelity multi-agent predictive simulation for the general public
that is approachable enough to educate
and refrains from miseducating.

Its nearest concrete form is a real-time,
multi-agent simulation built on the method of Children of a Dead Earth.
That simulation already has the physics,
derived from engineering equations with no vision imposed on the result.
What it lacks is the shared world.
The design below keeps the method and the physical core,
runs them in real time on a shared clock,
puts many human agents into one persistent world with a market and asymmetric roles,
and makes the whole approachable by tools rather than by fiction.
It takes a method,
not a product,
and every system in it would be derived afresh from first principles.

### Principles

1. **Omit, never contradict.**
   The simulation may leave a phenomenon out when the agents' purposes do not need it,
   and it says so.
   It never replaces a phenomenon with its opposite.
   It may change parameters,
   such as scale and the rate of time,
   but never laws.
   This is the Bohr principle of the earlier section,
   stated as a rule of design.
2. **Size fidelity per subsystem.**
   Gravity,
   propulsion,
   heat,
   sensors,
   communication,
   propellant slosh
   and the economy
   each get the fidelity the agents' decisions need.
3. **Make the physics approachable, not soft.**
   Approachability is supplied by tools that explain and compute,
   never by fiction that removes the physics.

### The Physical Core

- **Gravity.**
  The planets and moons follow ephemerides,
  precomputed positions from a real solar system model.
  That is an **omission** of their response to the agents' craft,
  which is negligible,
  and not a **contradiction**.
  Craft are integrated numerically under n-body gravity,
  so Lagrange points,
  perturbations
  and gravity assists emerge without being scripted.
  An integrator that conserves energy over long runs,
  such as a symplectic method,
  keeps orbits stable through months of simulated time.
  Symplectic methods of higher order were constructed by Yoshida
  [Yoshida 1990][research_yoshida_1990],
  and Wisdom and Holman adapted them to the n-body problem of the planets
  [Wisdom and Holman 1991][research_wisdom_holman_1991].
- **Propellant and delta-v.**
  Every manoeuvre costs propellant by the rocket equation,
  and the interface shows each agent the delta-v remaining.
- **Heat.**
  Waste heat is a resource to be rejected,
  and the radiators that reject it are a signature that others can see.
- **Light time.**
  Every message,
  order
  and sensor reading arrives late by its light time.
- **Slosh and structure.**
  Modelled where docking,
  landing
  or pointing need them,
  and sized out elsewhere.

### Equations for an Implementation

The core above needs a small set of equations,
and an implementer needs them in one place.
The manoeuvres an agent plans,
among them the Hohmann transfer,
plane changes
and the Oberth effect,
are worked with numbers in an earlier article on this site
[Orbital Manoeuvres][related_post_orbital_manoeuvres].
The equations below are the ones the simulation itself must integrate.

**Gravity and thrust.**
Each craft moves under the gravity of every massive body and its own thrust.
With $\ddot{\mathbf{r}}\_{i}$ the acceleration of craft $i$,
$G$ the gravitational constant,
$m\_{j}$ and $\mathbf{r}\_{j}$ the mass and position of body $j$,
and $\mathbf{a}\_{\mathrm{T},i}$ the acceleration of its own thrust,

$$
\ddot{\mathbf{r}}_{i} = -G \sum_{j \neq i} m_{j} \frac{\mathbf{r}_{i} - \mathbf{r}_{j}}{\lvert \mathbf{r}_{i} - \mathbf{r}_{j} \rvert^{3}} + \mathbf{a}_{\mathrm{T},i}
\tag{19}
$$

[Battin 1999][book_battin_1999].
The sum runs over the planets and moons on their ephemerides,
so a craft feels every body at once,
and Lagrange points and perturbations appear unscripted.
Thrust consumes propellant.
With $\dot{m}$ the rate of change of the craft's mass
and $F$ the thrust,

$$
\dot{m} = -\frac{F}{I_{\mathrm{sp}}\, g_{0}}
\tag{20}
$$

An engine of 100 kilonewtons at a specific impulse of 450 seconds
burns about 22.7 kilograms of propellant each second.
Integrated over a burn,
this equation is the rocket equation above.

**The step.**
The equations of motion are advanced in fixed steps by a symplectic method.
The simplest is the leapfrog in its kick-drift-kick form.
With $\Delta t$ the step,
$\mathbf{v}$ the velocity
and $\mathbf{a}(\mathbf{r})$ the acceleration at position $\mathbf{r}$,

$$
\begin{aligned}
\mathbf{v}_{n+1/2} &= \mathbf{v}_{n} + \tfrac{\Delta t}{2}\, \mathbf{a}(\mathbf{r}_{n}) \\
\mathbf{r}_{n+1} &= \mathbf{r}_{n} + \Delta t\, \mathbf{v}_{n+1/2} \\
\mathbf{v}_{n+1} &= \mathbf{v}_{n+1/2} + \tfrac{\Delta t}{2}\, \mathbf{a}(\mathbf{r}_{n+1})
\end{aligned}
\tag{21}
$$

This second-order method is the base from which Yoshida built higher orders
[Yoshida 1990][research_yoshida_1990].
Its energy error stays bounded instead of drifting,
so an orbit integrated this way does not slowly spiral in or out over a long simulation.

**Determinism.**
A shared world computed on many machines must give every machine the same answer.
With $\mathbf{x}\_{n}$ the full state of the world at step $n$,
$U\_{n}$ the set of agents' inputs committed for that step in an agreed order,
and $\Phi\_{\Delta t}$ the step function,

$$
\mathbf{x}_{n+1} = \Phi_{\Delta t}\!\left( \mathbf{x}_{n}, U_{n} \right)
\tag{22}
$$

Every machine that starts from the same state
and applies the same ordered inputs
reaches the same state,
provided the step function is exactly reproducible.
That proviso is the hard part.
Floating-point arithmetic that a compiler may reorder or fuse
can make two machines disagree in the last bit,
and an n-body system amplifies the difference.
An implementation therefore fixes the order of every operation,
or uses fixed-point arithmetic for the state.
This equation is the article's statement of the lockstep requirement,
and a later article in this series treats it in detail.

**Attitude.**
Pointing is a separate problem from moving.
With $\mathbf{I}$ the craft's inertia tensor,
$\boldsymbol{\omega}$ its angular velocity
and $\boldsymbol{\tau}$ the torque of its reaction control thrusters,
Euler's equations of rigid-body rotation give

$$
\mathbf{I}\, \dot{\boldsymbol{\omega}} + \boldsymbol{\omega} \times \left( \mathbf{I}\, \boldsymbol{\omega} \right) = \boldsymbol{\tau}
\tag{23}
$$

The torque changes where the craft points.
It does not change where the craft goes.
The remedy for banking turns now has its equation.

**Atmosphere.**
Launch and reentry need drag and heating.
With $F\_{\mathrm{D}}$ the drag force,
$\rho$ the density of the air,
$v$ the speed,
$C\_{\mathrm{D}}$ the drag coefficient
and $A$ the reference area,

$$
F_{\mathrm{D}} = \tfrac{1}{2}\, \rho v^{2} C_{\mathrm{D}} A
\tag{24}
$$

and a simple model of the density,
with $\rho\_{0}$ its value at sea level,
about 1.225 kilograms per cubic metre,
and $H$ the scale height,
about 8.5 kilometres,
is

$$
\rho(h) = \rho_{0}\, e^{-h/H}
\tag{25}
$$

Heating at the nose follows the stagnation-point correlation of Sutton and Graves
[Sutton and Graves 1971][research_sutton_graves_1971].
With $\dot{q}$ the heat flux,
$r\_{\mathrm{n}}$ the radius of the nose
and $k$ a constant for the atmosphere,
about $1.74 \times 10^{-4}$ in units that give watts per square metre for Earth's air,

$$
\dot{q} = k \sqrt{\frac{\rho}{r_{\mathrm{n}}}}\, v^{3}
\tag{26}
$$

At $10^{-4}$ kilograms per cubic metre,
a speed of 7.5 kilometres per second
and a nose radius of one metre,
the flux is about 0.73 megawatts per square metre.
The flux falls as the nose grows,
which is Allen and Eggers's argument for blunt bodies in a single term.

**Heat.**
A craft's temperature follows its energy balance.
With $m$ its thermal mass,
$c$ its specific heat,
$T$ its temperature,
$P\_{\mathrm{in}}$ the power it generates and absorbs,
and the radiator symbols as before,

$$
m c\, \frac{dT}{dt} = P_{\mathrm{in}} - \varepsilon \sigma A T^{4}
\tag{27}
$$

A craft that generates more heat than its radiators reject grows hotter,
and that constraint makes heat a resource.

**Slosh.**
Where a subsystem needs slosh,
the standard practice is an equivalent mechanical model,
in which the moving liquid behaves as a pendulum attached to the tank
[Abramson 1966][research_abramson_1966].
With $\omega\_{\mathrm{s}}$ the natural frequency of the first slosh mode,
$a$ the acceleration along the tank's axis
and $L$ the length of the equivalent pendulum,

$$
\omega_{\mathrm{s}} = \sqrt{\frac{a}{L}}
\tag{28}
$$

Under a thrust of a tenth of standard gravity,
a one-metre pendulum swings at about one radian per second,
a period of about six seconds,
slow enough to couple into a docking manoeuvre.
In a coasting craft the acceleration is nearly zero,
the restoring force vanishes,
and the liquid wanders.
Hence a small ullage thrust settles it before an engine starts.

### Time

Travel takes its true time,
and the simulation gives that time a job.
Time warp cannot be shared,
since one agent's acceleration of time would move every other agent's world.
A shared clock may still run fast,
provided it runs fast for everyone.
With $t\_{\mathrm{w}}$ the wall-clock time an agent waits,
$t\_{\mathrm{s}}$ the simulated time that passes
and $\kappa$ the compression factor shared by every agent,

$$
t_{\mathrm{w}} = \frac{t_{\mathrm{s}}}{\kappa}
\tag{29}
$$

At a compression of ten,
the 259-day transfer to Mars takes about 26 days of real time,
and at a compression of one hundred about 2.6 days.
The same factor shortens everything else.
At one hundred,
the 13-second exchange of the straight pass above lasts about a tenth of a second,
too short for any person to act in.
No single compression suits both the voyage and the engagement.
The rest of this section addresses that tension.
The inference drawn here is that a shared world needs a shared clock,
compressed by the same factor for everyone,
and agents who plan and commit manoeuvres in advance
and then do something else while the plan executes.
That is how real spaceflight operates,
and it is the tempo Children of a Dead Earth discovered,
long waits followed by short decisive exchanges.
A private timeline of the kind the Kerbal Space Program multiplayer modifications use
is a workable compromise when agents must act alone,
and a later article in this series compares the two.

Long journeys change what an agent is.
A transfer to Mars takes months,
and relativistic time dilation,
though tiny at interplanetary speeds,
would only add to the bookkeeping at higher ones.
An agent may therefore need to play several characters,
one in transit while another works at the destination.
A character can leave earlier
and arrive shortly before the role it was sent to fill begins,
much as a crew is sent ahead of a mission.

A world that runs around the clock also imposes a schedule.
EVE Online's agents,
as a class,
already work to taxing schedules across time zones
when an event matters,
even though no individual can attend every pivotal development.
Any high-fidelity simulation that runs continuously
may subject its agents to the same realities,
inconvenient as they are.
The thirty-second exchange of a pass between two fleets
happens when the orbits say it happens,
which may be the middle of the night on a Tuesday
or the middle of an important meeting.
Agents must then balance their real lives against their obligations in the simulation,
and that balance is itself a kind of stake.
Two answers follow.
Agents may need to find other stakeholders who can cover the inconvenient shifts,
as an organisation with members in several time zones does.
Run in real time,
a single simulated spaceship may need three shifts of real people,
as a real ship at sea or a mission control room does.
That sounds absurd to anyone who would never touch such a simulation,
and it is exactly what its most committed agents would organise.
Or the simulation may need a mechanism to resolve events ahead of time,
from orders committed in advance,
and that mechanism can sometimes place the decisive moment
within an agent's preferred waking hours.
Committed orders suit the physics,
since a transfer planned in advance is how real spaceflight already works.

This is where the thesis is most at risk,
and it should be said plainly.
True travel times may make multi-agent scenarios
that the general public finds palatable intractable.
Or the problem may be hard enough
that solving it is a questionable exercise for a studio that must earn a return on its investment.
Most studios must,
because for a studio the return on investment is generally an existential problem.
The claim that such a simulation is possible is a claim about physics and engineering.
It is not a claim that building one would pay.

### The Agents

- **Real people, in roles.**
  As in EVE Online,
  agents are people,
  so their interactions are sandboxed and not simulated.
  As in Star Citizen,
  their roles are asymmetric,
  among them navigation,
  propulsion,
  trade,
  mining,
  construction,
  science,
  logistics
  and defence.
- **One shared world.**
  A single persistent world,
  as EVE Online demonstrated is possible for a large population,
  so that the consequences of one agent's actions reach the others.
- **A real market.**
  An economy of real agents,
  measured and reported as EVE Online's is,
  in which propellant,
  delta-v
  and time have prices.
  In such a market,
  the rocket equation becomes an economic fact
  that every agent learns by paying it.
- **Automated agents.**
  Programs may fly craft for people,
  provided they obey the same physics and the same light time.
  The predictions the simulation offers concern its human agents,
  so automated agents are tools of those people,
  not subjects of the experiment.

### An Economy Under Physics

EVE Online proves that agents will build and run a supply chain that spans a world.
The blueprint keeps that and puts physics under it.
Freight is priced by delta-v.
With $m\_{\mathrm{p}}$ the propellant needed,
$m\_{\mathrm{pay}}$ the payload,
$m\_{\mathrm{s}}$ the structure and engines that make the trip with it,
and the other symbols as in the rocket equation,

$$
m_{\mathrm{p}} = \left( m_{\mathrm{pay}} + m_{\mathrm{s}} \right) \left( e^{\Delta v / \left( I_{\mathrm{sp}}\, g_{0} \right)} - 1 \right)
\tag{30}
$$

At a specific impulse of 450 seconds,
a delta-v of 4 kilometres per second
needs about 1.5 kilograms of propellant for every kilogram that makes the trip.
Geography becomes orbital mechanics.
A cheap route is a low delta-v route,
and the synodic period above opens the cheapest route to Mars once every 26 months,
so an honest economy would have trading seasons,
with prices rising and falling as windows open and close.
The arbitrage condition above still governs every haul,
with the propellant now part of its cost.
Congestion pricing of the kind EVE Online applies to production
fits scarce real facilities too,
such as docking ports and shipyards in a crowded orbit.

The simulation should also publish its economy.
EVE Online already does.
Its economists report on the money supply every month
[CCP 2026][dev_ccp_mer_2026],
and its official interface for third parties,
which the developer calls
"the official RESTful API for EVE third-party development,"
serves every region's market orders and price history,
some of its routes needing no authentication at all
[ESI Overview][dev_ccp_esi_overview].
Anyone can therefore study the economy from outside.
A predictive simulation needs that openness,
because predictions nobody can check are not predictions.

### Approachability Without Miseducation

The design answer to Children of a Dead Earth's difficulty is layered disclosure.
The physics stays complete.
What changes from one agent to the next is how much of it the agent must handle by hand.
A beginner sets a destination,
and a planning tool computes the transfer,
the delta-v
and the arrival time,
and explains why.
An expert inspects and edits every burn.
Kerbal Space Program's manoeuvre planning shows that the public can learn this way.
An autopilot that obeys physics is an approachability tool.
A warp drive that disobeys it is miseducation.

### Predictive Value

People adapt their behaviour to conditions.
If the conditions of a simulation are those of real near-term space,
the agents' adaptation to them is evidence about how people would behave there,
in markets,
in logistics
and in conflict.
The predictive value of such evidence is bounded by three things.
The first is fidelity,
because agents adapt to the model and not to reality,
which is what Children of a Dead Earth's meta shows.
The second is approachability,
because a model only an expert can use
yields the behaviour of a small and unrepresentative population of experts.
The third is incentives.
An agent who risks nothing it values has no reason to behave as it would where the stakes are real.

EVE Online shows that this bound can be met in a simulation.
Some of its agents take it more seriously than their real jobs,
and a saying among them holds that internet spaceships are more fun than work.
People who defend a ledger of fantasy wealth that fiercely
are displaying the incentive feedback that a predictive simulation needs,
even if the enthusiasm is questionably placed.
The author has placed significant effort in the EVE Online sandbox,
questionably,
despite being a fairly tempered participant.

The same case shows what high commitment brings with it.
A multi-agent simulation that people take seriously
can hold its agents to wildly high expectations,
and real-life skills apply directly within it,
among them logistics,
accounting,
diplomacy
and the leadership of large groups.
The transfer runs the other way too,
since skills developed in the simulation can be applied in real-life situations.
Burnout is just as real.
Obligations that run around the clock
wear people down,
and a simulation that depends on committed agents
loses them when the commitment costs more than it returns.
Yet a simulation compelling enough
will still draw people to participate of their own volition,
and that voluntary commitment is the incentive feedback a predictive simulation needs.

EVE Online adds a refinement.
Its predictive value comes less from the fidelity of any component
than from how comprehensively the components interlock,
which is how terrible parts produce tax havens and bank runs.
It is an inference that predictive value has two sources,
the fidelity of the parts and the completeness of their interlock.
EVE Online is strong in the second and weak in the first,
and Children of a Dead Earth the reverse.

A simulation that maximises one bound at the expense of the others
predicts poorly.
The blueprint's principles exist to raise all three together.
The same tension appears in the published wargames reviewed elsewhere on this site,
whose value depends on how faithfully their rules capture the conditions they model
[Published Wargames][related_post_published_wargames].

### Market Demand

There is market demand for such a simulation,
and the reviewed products support the claim indirectly.
Kerbal Space Program sold more than five million units
[Take-Two 2023][dev_take_two_ksp2_2023].
EVE Online passed half a million subscribers in one shared world
[CCP 2013][dev_ccp_subscribers_2013].
Star Citizen is reported to have raised more than a billion dollars before release
[The FPS Review 2026][news_fps_review_sc_2026].
The public pays for spaceflight,
for shared worlds
and for both together.
It is an inference that it would pay for both with honest physics.
That inference is the market half of the thesis,
and it ties to the educational half.
A product the public will not use is a poor educational utility,
however good its physics,
as Children of a Dead Earth shows.
A product the public does use
teaches whatever physics it contains,
as EVE Online shows.
The opportunity is a product the public will use
whose physics is true.

## Epistemic State

**Sourced facts.**
The descriptions of each product's models,
travel,
propellant,
gravity,
atmosphere,
sales
and subscribers
come from the developers' own pages,
publishers' releases
and space agency pages cited in place.
Where a fact rests on a community wiki or a secondary report,
the text says so.
These are Kerbal Space Program's patched conics and scale,
EVE Online's velocity law,
warp speeds and capacitor,
the fixed positions of Star Citizen's bodies,
Star Citizen's crowdfunding total,
EVE Online's market fee formulas,
and the 2009 bank embezzlement and the technetium cartel,
which rest on press reports and a community history.
The survey on transferable skills appeared in an article sponsored by the developer.
The Star Trek line about tritanium rests on a fan transcript.
The physics of each remedy comes from NASA,
ESA,
the Fédération Aéronautique Internationale
or peer-reviewed work,
with three exceptions named in the text.
The visibility of laser beams rests on an optics manufacturer,
the claim that there is no stealth in space on a simulation developer,
and the weakness of explosions on the same developer and a nuclear effects handbook.

**The author's view.**
Everything not cited and not named as an inference is the author's judgement.
That includes the thesis,
the judgement that each product's model serves its product thesis,
the characterisation of EVE Online's individual models as wrong,
the judgements on approachability,
education
and management,
the observations about engagements and the meta in Children of a Dead Earth,
the expectation that no reviewed product simulates propellant slosh,
the understanding that Kerbal Space Program treats tanks as point masses,
the two causes of the soft science fiction conventions,
the judgement that EVE Online's economy is the best multi-agent supply chain known,
that its wrong models have the right fidelity for interaction,
and that the developer lacked the people to distil more realistic models,
the characterisation of EVE Online's most committed agents,
their scheduling across time zones,
the transfer of skills
and burnout,
and the blueprint.
These are offered as judgements,
open to disagreement on the evidence.
The author discloses an interest in one of the products,
having participated in the EVE Online sandbox.

**Inferences.**
That warp drive served Star Trek's production as the transporter did
is inferred from the format,
since no primary source says it.
That a shared world needs a shared clock,
that layered disclosure resolves the conflict between fidelity and approachability,
that several characters per agent would make long journeys playable,
that resolution of events from committed orders would ease scheduling across time zones,
that predictive value has two sources, the fidelity of the parts and the completeness of their interlock,
that an honest economy would have trading seasons,
and that the public would pay for honest physics
are inferences.
The third bound on predictive value,
incentives,
is an addition of this reconstruction and was not in the paper as the author recalls it.
The engagement-time and radiator equations are the author's simplifications
and show orders of magnitude only.

**The reconstruction.**
The thesis is reconstructed from memory.
Where this article's wording differs from the paper's,
the paper cannot be consulted to settle it.
The products are reviewed as they stand in November 2026,
not as they stood when the paper was written,
which leaves the conclusions unchanged.

## Out of Scope

- **Developments since the paper.**
  Research harnesses that put many automated agents into Kerbal Space Program and into high-fidelity satellite simulators,
  and language models tested as spacecraft operators,
  are the subject of the next article in this series.
- **The hard problems in detail.**
  Shared time,
  the rarity of encounters under honest delta-v budgets,
  and deterministic networked physics
  are named here and worked in a later article.
- **Other products.**
  The paper's list held other simulations that were never reviewed for lack of time.
  Orbiter,
  Elite Dangerous,
  Space Engineers
  and others are not reviewed here either,
  so the third claim is stated as none known.
- **Play testing.**
  The reviews rest on the developers' public statements and on first principles,
  not on new hands-on testing.
- **Reverse engineering.**
  No product was reverse engineered,
  and none will be.

## Conclusion

Strong single-agent models of spaceflight exist,
and Kerbal Space Program and Children of a Dead Earth are two good ones,
the first approachable and the second faithful.
The multi-agent simulations,
EVE Online and Star Citizen,
have poor physical models inherited from film and television,
in which ships coast to a stop,
travel takes no time,
gravity has no mechanism
and planets do not move.
None of these products has failed.
Each expresses its own thesis under its own constraints,
and EVE Online in particular shows that a real economy of real agents
can make the sum greater than the parts.

What no known product offers is the combination,
a single shared world of many agents
under physics that does not cheat,
made approachable by tools rather than by fiction.
Nothing in the physics or the engineering prevents it.
Whether it would pay is another question,
and true travel times may make it a hard one.
People adapt to the conditions they are given,
so such a simulation would have predictive value,
bounded by its fidelity,
by how many people can use it,
and by how much its agents care.
The public has shown that it will pay for spaceflight and for shared worlds.
A simulation that gave it both,
truthfully,
would also teach it,
and through the loop between science fiction and science,
the children it taught would build the future it depicted.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 30 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 30, 21 are established and 9 are bespoke.
Each equation takes the units its section states. Distances are in kilometres unless the section says otherwise, the worked numbers are rounded to the precision of their inputs, and the letter a stands for a semi-major axis in Equations 2 and 3 and for an acceleration in Equation 28.

**Equation 1, Bohr Energy Levels of Hydrogen.**
The energy of each permitted level in Bohr's model, which predicts the hydrogen spectrum despite a wrong picture of the electron.
[Bohr 1913][research_bohr_1913]

$$
E_{n} = -\frac{13.6\ \mathrm{eV}}{n^{2}}
\tag{1}
$$

**Equation 2, Laplace Sphere of Influence.**
The radius within which the patched-conic method treats a smaller body's gravity as the only gravity.
[Curtis 2020a][book_curtis_2020_interplanetary]

$$
r_{\mathrm{SOI}} = a \left( \frac{m}{M} \right)^{2/5}
\tag{2}
$$

**Equation 3, Hill Radius.**
The approximate distance of a body's first and second Lagrange points, which lie outside its sphere of influence.

$$
r_{\mathrm{H}} \approx a \left( \frac{m}{3M} \right)^{1/3}
\tag{3}
$$

*Equation 4, Bespoke Engagement Time of a Straight Pass.*
The time two craft spend within weapon range on a straight pass at constant relative speed, an order-of-magnitude model of the article's.

$$
t_{\mathrm{e}} = \frac{2R}{v_{\mathrm{rel}}}
\tag{4}
$$

**Equation 5, EVE Online Velocity Law.**
The speed a ship reaches under full propulsion in EVE Online, the law of a body in a viscous fluid, as the community guide gives it.
[Acceleration][community_eve_uni_acceleration]

$$
v(t) = v_{\max} \left( 1 - e^{-t/\tau} \right)
\tag{5}
$$

**Equation 6, EVE Online Industry Job Cost.**
The cost of installing an industry job in EVE Online, as the developer states it, with the system cost index scaled by the facility's bonuses.
[CCP 2023][dev_ccp_viridian_2023]

$$
C_{\mathrm{job}} = V_{\mathrm{EIV}} \left( I_{\mathrm{SCI}}\, \beta + t_{\mathrm{f}} + t_{\mathrm{SCC}} + t_{\alpha} \right)
\tag{6}
$$

*Equation 7, Bespoke Proportional Form of the 2014 System Cost Index.*
The square-root growth of EVE Online's cost index with a system's share of production, written from the developer's description of 2014 as a proportionality, since the exact current form is not published in text.
[CCP 2014][dev_ccp_industry_2014]

$$
I_{\mathrm{SCI}} \propto \sqrt{\frac{h_{\mathrm{sys}}}{h_{\mathrm{all}}}}
\tag{7}
$$

*Equation 8, Bespoke Material Requirement from EVE Online's Stated Rules.*
The quantity of one material a job consumes, assembled from the developer's stated rules on material efficiency, rounding per job and a minimum of one unit per run.
[CCP 2014][dev_ccp_industry_2014]

$$
n_{\mathrm{mat}} = \max\!\left( r,\ \left\lceil r\, n_{0} \left( 1 - \frac{E}{100} \right) \gamma \right\rceil \right)
\tag{8}
$$

*Equation 9, Bespoke Arbitrage Condition Between Two Hubs.*
The condition under which a haul between two markets pays after sales tax, broker's fees and hauling cost, a construction of the article's.

$$
p_{\mathrm{B}} \left( 1 - \lambda_{\mathrm{s}} - f_{\mathrm{b}} \right) - p_{\mathrm{A}} \left( 1 + f_{\mathrm{b}} \right) - c_{\mathrm{h}} > 0
\tag{9}
$$

**Equation 10, Tsiolkovsky Rocket Equation.**
The delta-v a rocket gains as its mass falls from the initial to the final mass.

$$
\Delta v = I_{\mathrm{sp}}\, g_{0} \ln \frac{m_{0}}{m_{\mathrm{f}}}
\tag{10}
$$

**Equation 11, Hohmann Transfer Time.**
Half the period of the transfer ellipse, the time the cheapest transfer between two circular orbits takes.
[Curtis 2020a][book_curtis_2020_interplanetary]

$$
t_{\mathrm{H}} = \pi \sqrt{\frac{a_{\mathrm{t}}^{3}}{\mu_{\odot}}}
\tag{11}
$$

**Equation 12, Synodic Period.**
The interval between repetitions of two planets' relative position, which spaces the windows for a transfer.
[Curtis 2020a][book_curtis_2020_interplanetary]

$$
\frac{1}{S} = \frac{1}{T_{1}} - \frac{1}{T_{2}}
\tag{12}
$$

**Equation 13, Geostationary Orbit Radius.**
The radius at which a circular orbit's period equals one sidereal day, the only place a satellite holds position over the ground.
[ESA 2020][agency_esa_geo_2020]

$$
r_{\mathrm{G}} = \left( \frac{\mu T^{2}}{4 \pi^{2}} \right)^{1/3}
\tag{13}
$$

**Equation 14, Circular Orbital Speed.**
The speed of a circular orbit at a given radius, which is what makes reaching orbit hard.

$$
v_{\mathrm{c}} = \sqrt{\frac{\mu}{r}}
\tag{14}
$$

**Equation 15, Gravity at Altitude.**
The inverse-square fall of gravity with height, which leaves about nine-tenths of surface gravity at the space station.
[NASA 2012][agency_nasa_microgravity]

$$
g(h) = g_{0} \left( \frac{R}{R + h} \right)^{2}
\tag{15}
$$

**Equation 16, Centripetal Acceleration.**
The acceleration felt at the rim of a rotating habitat, the physical basis of spin gravity.
[Johnson and Holbrow 1977][agency_nasa_sp413_1977]

$$
a_{\mathrm{c}} = \omega^{2} r
\tag{16}
$$

*Equation 17, Bespoke Radiator Power Without Absorbed Sunlight.*
The Stefan-Boltzmann law applied to a radiator facing cold space with absorbed sunlight neglected, an assumption of the article's that lowers the area needed.

$$
P = \varepsilon \sigma A T^{4}
\tag{17}
$$

**Equation 18, Light-Time Delay.**
The one-way delay of any signal over a distance, which no message or sensor reading can beat.
[Landon et al. 2025][agency_nasa_tm_2025_mars_comms]

$$
t_{\mathrm{L}} = \frac{d}{c}
\tag{18}
$$

**Equation 19, N-Body Equation of Motion With Thrust.**
The acceleration of a craft under the gravity of every massive body plus its own thrust, the equation the core integrates.
[Battin 1999][book_battin_1999]

$$
\ddot{\mathbf{r}}_{i} = -G \sum_{j \neq i} m_{j} \frac{\mathbf{r}_{i} - \mathbf{r}_{j}}{\lvert \mathbf{r}_{i} - \mathbf{r}_{j} \rvert^{3}} + \mathbf{a}_{\mathrm{T},i}
\tag{19}
$$

**Equation 20, Propellant Mass Flow.**
The rate at which an engine of given thrust and specific impulse consumes propellant, which integrates to the rocket equation.

$$
\dot{m} = -\frac{F}{I_{\mathrm{sp}}\, g_{0}}
\tag{20}
$$

**Equation 21, Kick-Drift-Kick Leapfrog Step.**
The second-order symplectic step whose energy error stays bounded, the base of higher-order symplectic integrators.
[Yoshida 1990][research_yoshida_1990]

$$
\begin{aligned}
\mathbf{v}_{n+1/2} &= \mathbf{v}_{n} + \tfrac{\Delta t}{2}\, \mathbf{a}(\mathbf{r}_{n}) \\
\mathbf{r}_{n+1} &= \mathbf{r}_{n} + \Delta t\, \mathbf{v}_{n+1/2} \\
\mathbf{v}_{n+1} &= \mathbf{v}_{n+1/2} + \tfrac{\Delta t}{2}\, \mathbf{a}(\mathbf{r}_{n+1})
\end{aligned}
\tag{21}
$$

*Equation 22, Bespoke Lockstep State Transition.*
The shared world's state advanced by one deterministic step from the agents' ordered inputs, the article's statement of the lockstep requirement.

$$
\mathbf{x}_{n+1} = \Phi_{\Delta t}\!\left( \mathbf{x}_{n}, U_{n} \right)
\tag{22}
$$

**Equation 23, Euler's Equations of Rigid-Body Rotation.**
The change in a craft's angular velocity under the torque of its thrusters, which turns the craft without changing its path.

$$
\mathbf{I}\, \dot{\boldsymbol{\omega}} + \boldsymbol{\omega} \times \left( \mathbf{I}\, \boldsymbol{\omega} \right) = \boldsymbol{\tau}
\tag{23}
$$

**Equation 24, Aerodynamic Drag.**
The drag force on a body moving through air, which governs launch and reentry.

$$
F_{\mathrm{D}} = \tfrac{1}{2}\, \rho v^{2} C_{\mathrm{D}} A
\tag{24}
$$

**Equation 25, Isothermal Exponential Atmosphere.**
The simple model of air density falling exponentially with height above sea level.

$$
\rho(h) = \rho_{0}\, e^{-h/H}
\tag{25}
$$

**Equation 26, Sutton-Graves Stagnation-Point Heating.**
The convective heat flux at the nose of a vehicle entering an atmosphere, which falls as the nose grows blunter.
[Sutton and Graves 1971][research_sutton_graves_1971]

$$
\dot{q} = k \sqrt{\frac{\rho}{r_{\mathrm{n}}}}\, v^{3}
\tag{26}
$$

*Equation 27, Bespoke Lumped Thermal Balance.*
A single-node energy balance in which a craft heats when the power it gains exceeds what its radiators reject, an assumption of uniform temperature.

$$
m c\, \frac{dT}{dt} = P_{\mathrm{in}} - \varepsilon \sigma A T^{4}
\tag{27}
$$

**Equation 28, Pendulum Model of First-Mode Slosh.**
The natural frequency of the equivalent pendulum that represents a tank's first slosh mode under axial acceleration.
[Abramson 1966][research_abramson_1966]

$$
\omega_{\mathrm{s}} = \sqrt{\frac{a}{L}}
\tag{28}
$$

*Equation 29, Bespoke Wall-Clock Time Under a Shared Clock.*
The real time an agent waits for a span of simulated time when one compression factor applies to every agent.

$$
t_{\mathrm{w}} = \frac{t_{\mathrm{s}}}{\kappa}
\tag{29}
$$

*Equation 30, Bespoke Freight Propellant From the Rocket Equation.*
The propellant a shipment needs for a given delta-v, the rocket equation rearranged to price freight by delta-v in the blueprint's economy.

$$
m_{\mathrm{p}} = \left( m_{\mathrm{pay}} + m_{\mathrm{s}} \right) \left( e^{\Delta v / \left( I_{\mathrm{sp}}\, g_{0} \right)} - 1 \right)
\tag{30}
$$

### Notation

- $E_{n}$, the energy of hydrogen level $n$ in the Bohr model
- $r_{\mathrm{SOI}}$, the radius of the sphere of influence
- $r_{\mathrm{H}}$, the Hill radius
- $M$, the mass of the larger body, or a ship's mass in Equation 5
- $t_{\mathrm{e}}$, the time two craft spend within range of each other
- $v_{\mathrm{rel}}$, the relative speed of two craft
- $v_{\max}$, a ship's top speed in EVE Online
- $\tau$, the time constant of EVE Online's velocity law
- $I_{\mathrm{sp}}$, the specific impulse of a rocket engine
- $g_{0}$, standard gravity at the surface, 9.80665 metres per second squared
- $t_{\mathrm{H}}$, the Hohmann transfer time
- $a_{\mathrm{t}}$, the semi-major axis of the transfer ellipse
- $\mu_{\odot}$, the Sun's gravitational parameter
- $S$, the synodic period
- $r_{\mathrm{G}}$, the radius of the geostationary orbit
- $\mu$, Earth's gravitational parameter
- $v_{\mathrm{c}}$, the speed of a circular orbit
- $a_{\mathrm{c}}$, the centripetal acceleration at a habitat's rim
- $\omega$, the rate of rotation in radians per second
- $\varepsilon$, the emissivity of a radiator
- $\sigma$, the Stefan-Boltzmann constant
- $t_{\mathrm{L}}$, the one-way light-time delay
- $\mathbf{a}_{\mathrm{T},i}$, the acceleration of craft $i$ from its own thrust
- $\dot{m}$, the rate of change of a craft's mass
- $\Delta t$, the integration step
- $\Phi_{\Delta t}$, the deterministic step function of the shared world
- $U_{n}$, the ordered set of agents' inputs committed for step $n$
- $\mathbf{I}$, a craft's inertia tensor
- $\boldsymbol{\tau}$, the torque of a craft's reaction control thrusters
- $F_{\mathrm{D}}$, the aerodynamic drag force
- $C_{\mathrm{D}}$, the drag coefficient
- $\rho$, the density of the air
- $H$, the scale height of the atmosphere
- $\dot{q}$, the stagnation-point heat flux
- $r_{\mathrm{n}}$, the radius of a vehicle's nose
- $P_{\mathrm{in}}$, the power a craft generates and absorbs
- $\omega_{\mathrm{s}}$, the natural frequency of the first slosh mode
- $C_{\mathrm{job}}$, the cost of installing an industry job in EVE Online
- $V_{\mathrm{EIV}}$, the estimated item value of a job's output
- $I_{\mathrm{SCI}}$, the cost index of a solar system
- $\beta$, the product of a facility's bonuses
- $h_{\mathrm{sys}}$, the job-hours of an activity in one system over 28 days
- $h_{\mathrm{all}}$, the job-hours of that activity in the whole universe over 28 days
- $n_{\mathrm{mat}}$, the quantity of one material a job consumes
- $n_{0}$, a blueprint's base quantity of a material per run
- $\gamma$, a facility's material modifier
- $p_{\mathrm{A}}$, the price paid at the source market
- $p_{\mathrm{B}}$, the price received at the destination market
- $\lambda_{\mathrm{s}}$, the sales tax rate
- $f_{\mathrm{b}}$, the broker's fee rate
- $c_{\mathrm{h}}$, the cost of hauling one unit
- $m_{\mathrm{p}}$, the propellant a shipment needs
- $m_{\mathrm{pay}}$, the payload of a shipment
- $m_{\mathrm{s}}$, the structure and engines that make the trip with the payload
- $t_{\mathrm{w}}$, the wall-clock time an agent waits
- $t_{\mathrm{s}}$, the simulated time that passes
- $\kappa$, the time compression factor shared by every agent

## References

- [Agency, Blevins and Hohmann 1975, Description of the Space Shuttle Reaction Control System][agency_nasa_shuttle_rcs_1975]
- [Agency, ESA 2020, Geostationary Orbit][agency_esa_geo_2020]
- [Agency, Johnson and Holbrow 1977, Space Settlements: A Design Study][agency_nasa_sp413_1977]
- [Agency, Landon et al. 2025, Assessment of the State of Communication Delay Research][agency_nasa_tm_2025_mars_comms]
- [Agency, Launius and Jenkins 2012, Coming Home: Reentry and Recovery from Space][agency_nasa_coming_home]
- [Agency, NASA 2012, What Is Microgravity?][agency_nasa_microgravity]
- [Agency, NASA 2016, Gamers Tackle Virtual Asteroid Sampling Mission][agency_nasa_gamers_osiris_2016]
- [Agency, NASA 2017, Why Do We Really Need Pressure Suits?][agency_nasa_pressure_suits_2017]
- [Agency, NASA 2020, Space Communications: 7 Things You Need to Know][agency_nasa_space_comms_2020]
- [Agency, NASA 2021, NASA Laser Communications Innovations: A Timeline][agency_nasa_laser_comm_timeline_2021]
- [Agency, NASA 2024, 55 Years Ago: Star Trek Final Episode Airs][agency_nasa_star_trek_55_2024]
- [Agency, NASA Anatomy of an Electromagnetic Wave][agency_nasa_em_anatomy]
- [Agency, NASA Black Holes][agency_nasa_black_holes]
- [Agency, NASA Dawn FAQ][agency_nasa_dawn_faq]
- [Agency, NASA Earth Fact Sheet][agency_nasa_earth_fact_sheet]
- [Agency, NASA ISS Active Thermal Control System Overview][agency_nasa_iss_atcs]
- [Agency, NASA Newton's Laws of Motion][agency_nasa_newton]
- [Agency, NASA Rocket Principles][agency_nasa_rocket_principles]
- [Agency, NASA Small Spacecraft Thermal Control][agency_nasa_smallsat_thermal]
- [Agency, NASA Webb Orbit][agency_nasa_webb_orbit]
- [Agency, NASA Whipple Shield Development][agency_nasa_whipple]
- [Agency, Stysley 2011, Laser-Based Optical Trap for Remote Sampling][agency_nasa_niac_stysley_2011]
- [Agency, Westover et al. 2019, Magnet Architectures and Active Radiation Shielding Study][agency_nasa_maarss_2019]
- [Book, Battin 1999, An Introduction to the Mathematics and Methods of Astrodynamics][book_battin_1999]
- [Book, Conway Morris 2003, Life's Solution][book_conway_morris_2003]
- [Book, Curtis 2020a, Interplanetary Trajectories][book_curtis_2020_interplanetary]
- [Book, Glasstone 1964, The Effects of Nuclear Weapons][book_glasstone_1964]
- [Book, Hawking and Hawking 2007, George's Secret Key to the Universe][book_hawking_hawking_2007]
- [Book, Whitfield and Roddenberry 1968, The Making of Star Trek][book_whitfield_roddenberry_1968]
- [Community, EVE University, Acceleration][community_eve_uni_acceleration]
- [Community, EVE University, Capacitor][community_eve_uni_capacitor]
- [Community, EVE University, Industry][community_eve_uni_industry]
- [Community, EVE University, Jump Drives][community_eve_uni_jump_drives]
- [Community, EVE University, Trading][community_eve_uni_trading]
- [Community, EVE University, Warp][community_eve_uni_warp]
- [Community, KSP Wiki, Kerbin][community_ksp_wiki_kerbin]
- [Community, KSP Wiki, Multiplayer][community_ksp_wiki_multiplayer]
- [Community, KSP Wiki, Sphere of Influence][community_ksp_wiki_soi]
- [Community, Star Citizen Wiki, Planet][community_sc_tools_planet]
- [Community, The Star Trek Transcripts, Obsession][community_trek_obsession_transcript]
- [Developer, CCP 2003, Highly Anticipated Massively Multiplayer Online Game][dev_ccp_launch_2003]
- [Developer, CCP 2006, A Deal Is a Deal][dev_ccp_faucets_2006]
- [Developer, CCP 2007, EVE Online Appoints In-World Economist][dev_ccp_economist_2007]
- [Developer, CCP 2007a, Econ Dev Blog No. 3, Some Statistics on Corporations][dev_ccp_corporations_2007]
- [Developer, CCP 2008, I Can Resist Anything but Temptation][dev_ccp_plex_2008]
- [Developer, CCP 2009, The Way of the PLEX][dev_ccp_plex_2009]
- [Developer, CCP 2009a, I Bring Gifts, by Gifts I Mean Taxes][dev_ccp_taxes_2009]
- [Developer, CCP 2012, Price Indices, February 2012][dev_ccp_price_indices_2012]
- [Developer, CCP 2012a, Tech Is Fine, L2P][dev_ccp_technetium_2012]
- [Developer, CCP 2013, EVE Online Surpasses 500,000 Subscribers Worldwide][dev_ccp_subscribers_2013]
- [Developer, CCP 2013a, Warp Drive Active][dev_ccp_warp_2013]
- [Developer, CCP 2013b, Community Spotlight, Red Frog Freight][dev_ccp_red_frog_2013]
- [Developer, CCP 2014, EVE Industry, All You Want to Know][dev_ccp_industry_2014]
- [Developer, CCP 2014a, The Bloodbath of B-R5RB][dev_ccp_b_r5rb_2014]
- [Developer, CCP 2015, EVE Economy Update, EVE Vegas 2015 Report][dev_ccp_economy_vegas_2015]
- [Developer, CCP 2016, Overlays, ISK Buyer Amnesty and Account Security][dev_ccp_rmt_2016]
- [Developer, CCP 2017, PLEX Changes on the Way][dev_ccp_plex_2017]
- [Developer, CCP 2020, Broker Relations][dev_ccp_broker_relations_2020]
- [Developer, CCP 2022, Team Security 2021 in Review][dev_ccp_security_2021]
- [Developer, CCP 2023, Viridian Expansion Notes][dev_ccp_viridian_2023]
- [Developer, CCP 2025, Patch Notes, Version 22.02][dev_ccp_patch_22_02_2025]
- [Developer, CCP 2026, Monthly Economic Report, August 2026][dev_ccp_mer_2026]
- [Developer, CCP, Capsuleers][dev_ccp_capsuleers]
- [Developer, CCP, EVE Swagger Interface Overview][dev_ccp_esi_overview]
- [Developer, CCP, Tritanium Item Record][dev_ccp_esi_tritanium]
- [Developer, Children of a Dead Earth, Steam Store Page][dev_code_steam]
- [Developer, Dark Multiplayer][dev_dark_multiplayer]
- [Developer, Kerbal Space Program, Steam Store Page][dev_ksp_steam]
- [Developer, KerbalEdu 2016][dev_kerbaledu_2016]
- [Developer, Luna Multiplayer][dev_luna_multiplayer]
- [Developer, Principia][dev_principia]
- [Developer, Q-Switched 2016, Burn Rockets Burn][dev_code_rockets_2016]
- [Developer, Q-Switched 2016, Fun with Orbital Mechanics][dev_code_orbital_2016]
- [Developer, Q-Switched 2016, How Realistic Is It Actually?][dev_code_realistic_2016]
- [Developer, Q-Switched 2016, Raw Steel][dev_code_raw_steel_2016]
- [Developer, Q-Switched 2016, Slosh Baffles][dev_code_slosh_2016]
- [Developer, Q-Switched 2016, Space Guns][dev_code_space_guns_2016]
- [Developer, Q-Switched 2016, Stealth in Space][dev_code_stealth_2016]
- [Developer, Q-Switched 2016, The Essence of Space Warfare][dev_code_essence_2016]
- [Developer, Q-Switched 2016, The Photon Lance][dev_code_photon_lance_2016]
- [Developer, Real Solar System][dev_real_solar_system]
- [Developer, Realism Overhaul][dev_realism_overhaul]
- [Developer, Roberts 2018, Letter from the Chairman][dev_rsi_letter_2018]
- [Developer, Roberts 2020, Letter from the Chairman][dev_rsi_letter_2020]
- [Developer, RSI 2014, Lore Builder Twenty][dev_rsi_lore_gravity_2014]
- [Developer, RSI 2017, Star Citizen Alpha 3.0.0][dev_rsi_alpha_300_2017]
- [Developer, RSI 2018, The Shipyard: Fuel Mechanics][dev_rsi_fuel_2018]
- [Developer, RSI 2020, Flight and Fight Upcoming Improvements][dev_rsi_flight_2020]
- [Developer, RSI, Star Citizen Alpha 4.0][dev_rsi_alpha_40]
- [Developer, Squad 2011, First Release Is Up][dev_squad_first_release_2011]
- [Developer, Squad 2014, KSP: Asteroid Redirect Mission Is Officially Released][dev_squad_arm_2014]
- [Developer, Take-Two 2017, Take-Two Acquires Kerbal Space Program][dev_take_two_ksp_2017]
- [Developer, Take-Two 2023, Kerbal Space Program 2 Launches in Early Access][dev_take_two_ksp2_2023]
- [News, Big Think 2015, Michio Kaku][news_big_think_kaku_2015]
- [News, Den of Geek 2020, How EVE Online Players Say the Game Changed Their Lives][news_den_of_geek_2020]
- [News, Engadget 2008, Making Money, the Origin of the Specie][news_engadget_tritanium_2008]
- [News, Engadget 2009, New Perspective on EVE Online's Latest Bank Embezzlement][news_engadget_ebank_2009]
- [News, Engadget 2014, EVE Fanfest 2014 Economy Talk][news_engadget_plex_2014]
- [News, EVE News24 2018, Moments in History, OTEC][news_evenews24_otec_2018]
- [News, Gematsu 2026, CCP Games Rebrands to Fenris Creations][news_gematsu_fenris_2026]
- [News, Gizmodo 2011, The First Draft of the Star Trek Pitch][news_gizmodo_trek_pitch_2011]
- [News, IEEE Spectrum 2009, EVE Online Game Player Embezzles Virtual Money][news_ieee_ebank_2009]
- [News, PC Gamer 2024, Kerbal Space Program 2 Developer Intercept Games May Be Closing][news_pc_gamer_intercept_2024]
- [News, Slashdot 2013, J. Michael Straczynski Answers Your Questions][news_slashdot_straczynski_2013]
- [News, Space.com 2015, The Expanse][news_space_com_expanse_2015]
- [News, The FPS Review 2026, Star Citizen Crosses $1 Billion][news_fps_review_sc_2026]
- [News, The Register 2009, Gamer Embezzles Virtual Cash to Settle Real Debts][news_register_ebank_2009]
- [Reference, Edmund Optics, Can a Laser Beam Be Seen from the Side?][ref_edmund_laser]
- [Reference, FAI 2018, Statement about the Karman Line][ref_fai_karman_2018]
- [Reference, SIGGRAPH History, The Last Starfighter][ref_siggraph_last_starfighter]
- [Related Post, Mass Drivers][related_post_mass_drivers]
- [Related Post, Orbital Manoeuvres in Terms of Delta-v][related_post_orbital_manoeuvres]
- [Related Post, Published Wargames of War with China][related_post_published_wargames]
- [Related Post, Solar Sailing][related_post_solar_sailing]
- [Research, Abramson 1966, The Dynamic Behavior of Liquids in Moving Containers][research_abramson_1966]
- [Research, Allen and Eggers 1958, A Study of the Motion and Aerodynamic Heating of Ballistic Missiles Entering the Earth's Atmosphere][research_allen_eggers_1958]
- [Research, Bohr 1913, On the Constitution of Atoms and Molecules][research_bohr_1913]
- [Research, Levin et al. 2017, Darwin's Aliens][research_levin_et_al_2017]
- [Research, Li et al. 2017, Modeling and Research of a Space-Based Spacecraft Infrared Detection System][research_li_et_al_2017]
- [Research, McKagan et al. 2008, Why We Should Teach the Bohr Model and How to Teach It Effectively][research_mckagan_et_al_2008]
- [Research, Orthia 2019, How Does Science Fiction Television Shape Fans' Relationships to Science? Results from a Survey of 575 Doctor Who Viewers][research_orthia_2019]
- [Research, Sutton and Graves 1971, A General Stagnation-Point Convective Heating Equation for Arbitrary Gas Mixtures][research_sutton_graves_1971]
- [Research, Whipple 1947, Meteorites and Space Travel][research_whipple_1947]
- [Research, Wisdom and Holman 1991, Symplectic Maps for the N-Body Problem][research_wisdom_holman_1991]
- [Research, Yoshida 1990, Construction of Higher Order Symplectic Integrators][research_yoshida_1990]

[agency_esa_geo_2020]: https://www.esa.int/ESA_Multimedia/Images/2020/03/Geostationary_orbit
[agency_nasa_black_holes]: https://science.nasa.gov/universe/black-holes/
[agency_nasa_coming_home]: https://www.nasa.gov/wp-content/uploads/2015/04/695726main_cominghome-ebook.pdf
[agency_nasa_dawn_faq]: https://science.nasa.gov/mission/dawn/faq/
[agency_nasa_earth_fact_sheet]: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
[agency_nasa_em_anatomy]: https://science.nasa.gov/ems/02_anatomy/
[agency_nasa_gamers_osiris_2016]: https://www.nasa.gov/centers-and-facilities/goddard/gamers-tackle-virtual-asteroid-sampling-mission/
[agency_nasa_iss_atcs]: https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf
[agency_nasa_laser_comm_timeline_2021]: https://www.nasa.gov/centers-and-facilities/goddard/nasa-laser-communications-innovations-a-timeline/
[agency_nasa_maarss_2019]: https://ntrs.nasa.gov/citations/20190002579
[agency_nasa_microgravity]: https://www.nasa.gov/learning-resources/for-kids-and-students/what-is-microgravity-grades-5-8/
[agency_nasa_newton]: https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/newtons-laws-of-motion/
[agency_nasa_niac_stysley_2011]: https://www.nasa.gov/wp-content/uploads/2017/07/niac_2011_phasei_stysley_laserbasedopticaltrap_tagged.pdf
[agency_nasa_pressure_suits_2017]: https://www.nasa.gov/wp-content/uploads/2023/05/dressing-for-altitude-nov-2017.pdf
[agency_nasa_rocket_principles]: https://www.grc.nasa.gov/www/k-12/rocket/TRCRocket/rocket_principles.html
[agency_nasa_shuttle_rcs_1975]: https://ntrs.nasa.gov/citations/19750061613
[agency_nasa_smallsat_thermal]: https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/
[agency_nasa_sp413_1977]: https://ntrs.nasa.gov/citations/19770014162
[agency_nasa_space_comms_2020]: https://www.nasa.gov/missions/tech-demonstration/space-communications-7-things-you-need-to-know/
[agency_nasa_star_trek_55_2024]: https://www.nasa.gov/history/55-years-ago-star-trek-final-episode-airs-relationship-with-nasa-endures/
[agency_nasa_tm_2025_mars_comms]: https://ntrs.nasa.gov/api/citations/20250003885/downloads/NASA%20TM20250003885.pdf
[agency_nasa_webb_orbit]: https://science.nasa.gov/mission/webb/orbit/
[agency_nasa_whipple]: https://hvit.jsc.nasa.gov/shield-development/
[book_battin_1999]: https://doi.org/10.2514/4.861543
[book_conway_morris_2003]: https://doi.org/10.1017/CBO9780511535499
[book_curtis_2020_interplanetary]: https://doi.org/10.1016/b978-0-08-102133-0.00008-8
[book_glasstone_1964]: https://archive.org/details/TheEffectsOfNuclearWeapons1957
[book_hawking_hawking_2007]: https://openlibrary.org/books/OL9523149M
[book_whitfield_roddenberry_1968]: https://archive.org/details/makingofstartrek00whit
[community_eve_uni_acceleration]: https://wiki.eveuniversity.org/Acceleration
[community_eve_uni_capacitor]: https://wiki.eveuniversity.org/Capacitor
[community_eve_uni_industry]: https://wiki.eveuniversity.org/Industry
[community_eve_uni_jump_drives]: https://wiki.eveuniversity.org/Jump_drives
[community_eve_uni_trading]: https://wiki.eveuniversity.org/Trading
[community_eve_uni_warp]: https://wiki.eveuniversity.org/Warp
[community_ksp_wiki_kerbin]: https://wiki.kerbalspaceprogram.com/wiki/Kerbin
[community_ksp_wiki_multiplayer]: https://wiki.kerbalspaceprogram.com/wiki/Multiplayer
[community_ksp_wiki_soi]: https://wiki.kerbalspaceprogram.com/wiki/Sphere_of_influence
[community_sc_tools_planet]: https://starcitizen.tools/Planet
[community_trek_obsession_transcript]: http://www.chakoteya.net/StarTrek/47.htm
[dev_ccp_b_r5rb_2014]: https://www.eveonline.com/news/view/the-bloodbath-of-b-r5rb
[dev_ccp_broker_relations_2020]: https://www.eveonline.com/news/view/broker-relations
[dev_ccp_capsuleers]: https://universe.eveonline.com/lore/capsuleers
[dev_ccp_corporations_2007]: https://www.eveonline.com/news/view/econ-dev-blog-no.-3-some-statistics-on-corporations
[dev_ccp_economist_2007]: https://community.eveonline.com/news/news-channels/press-releases/eve-online-appoints-in-world-economist-1
[dev_ccp_economy_vegas_2015]: https://www.eveonline.com/news/view/eve-economy-update-eve-vegas-2015-report
[dev_ccp_esi_overview]: https://developers.eveonline.com/docs/services/esi/overview/
[dev_ccp_esi_tritanium]: https://esi.evetech.net/latest/universe/types/34/?datasource=tranquility&language=en
[dev_ccp_faucets_2006]: https://www.eveonline.com/news/view/a-deal-is-a-deal...
[dev_ccp_industry_2014]: https://www.eveonline.com/news/view/eve-industry-all-you-want-to-know
[dev_ccp_launch_2003]: https://community.eveonline.com/news/news-channels/press-releases/highly-anticipated-massively-multiplayer-online-game-1
[dev_ccp_mer_2026]: https://www.eveonline.com/news/view/monthly-economic-report-august-2026
[dev_ccp_patch_22_02_2025]: https://www.eveonline.com/news/view/patch-notes-version-22-02
[dev_ccp_plex_2008]: https://www.eveonline.com/news/view/i-can-resist-anything-but-temptation
[dev_ccp_plex_2009]: https://www.eveonline.com/news/view/the-way-of-the-plex
[dev_ccp_plex_2017]: https://www.eveonline.com/news/view/plex-changes-on-the-way
[dev_ccp_price_indices_2012]: https://www.eveonline.com/news/view/price-indices-february-2012
[dev_ccp_red_frog_2013]: https://www.eveonline.com/news/view/community-spotlight-red-frog-freight
[dev_ccp_rmt_2016]: https://www.eveonline.com/news/view/overlays-isk-buyer-amnesty-and-account-security
[dev_ccp_security_2021]: https://www.eveonline.com/news/view/team-security-2021-in-review
[dev_ccp_subscribers_2013]: https://community.eveonline.com/news/news-channels/press-releases/eve-online-surpasses-500-000-subscribers-worldwide
[dev_ccp_taxes_2009]: https://www.eveonline.com/news/view/i-bring-gifts-by-gifts-i-mean-taxes-sorry
[dev_ccp_technetium_2012]: https://www.eveonline.com/news/view/tech-is-fine-l2p
[dev_ccp_viridian_2023]: https://www.eveonline.com/news/view/viridian-expansion-notes
[dev_ccp_warp_2013]: https://www.eveonline.com/news/view/warp-drive-active
[dev_code_essence_2016]: https://childrenofadeadearth.wordpress.com/2016/04/20/the-essence-of-space-warfare/
[dev_code_orbital_2016]: https://childrenofadeadearth.wordpress.com/2016/05/17/fun-with-orbital-mechanics/
[dev_code_photon_lance_2016]: https://childrenofadeadearth.wordpress.com/2016/07/02/the-photon-lance/
[dev_code_raw_steel_2016]: https://childrenofadeadearth.wordpress.com/2016/08/04/raw-steel/
[dev_code_realistic_2016]: https://childrenofadeadearth.wordpress.com/2016/04/15/how-realistic-is-it-actually/
[dev_code_rockets_2016]: https://childrenofadeadearth.wordpress.com/2016/05/02/burn-rockets-burn/
[dev_code_slosh_2016]: https://childrenofadeadearth.wordpress.com/2016/05/24/slosh-baffles/
[dev_code_space_guns_2016]: https://childrenofadeadearth.wordpress.com/2016/06/14/space-guns/
[dev_code_stealth_2016]: https://childrenofadeadearth.wordpress.com/2016/07/12/stealth-in-space/
[dev_code_steam]: https://store.steampowered.com/app/476530/
[dev_dark_multiplayer]: https://github.com/godarklight/DarkMultiPlayer
[dev_kerbaledu_2016]: https://web.archive.org/web/20160104215459/http://www.kerbaledu.com/
[dev_ksp_steam]: https://store.steampowered.com/app/220200/
[dev_luna_multiplayer]: https://github.com/LunaMultiplayer/LunaMultiplayer/wiki
[dev_principia]: https://github.com/mockingbirdnest/Principia
[dev_real_solar_system]: https://github.com/KSP-RO/RealSolarSystem
[dev_realism_overhaul]: https://github.com/KSP-RO/RealismOverhaul
[dev_rsi_alpha_300_2017]: https://robertsspaceindustries.com/en/comm-link/transmission/16348-Star-Citizen-Alpha-300
[dev_rsi_alpha_40]: https://robertsspaceindustries.com/en/comm-link/Patch-Notes/20360-Star-Citizen-Alpha-40
[dev_rsi_flight_2020]: https://robertsspaceindustries.com/en/comm-link/transmission/17647-Flight-Fight-Upcoming-Improvements
[dev_rsi_fuel_2018]: https://robertsspaceindustries.com/en/comm-link/engineering/16517-The-Shipyard-Fuel-Mechanics
[dev_rsi_letter_2018]: https://robertsspaceindustries.com/en/comm-link/transmission/16700-Letter-From-The-Chairman
[dev_rsi_letter_2020]: https://robertsspaceindustries.com/en/comm-link/transmission/17805-Letter-From-The-Chairman
[dev_rsi_lore_gravity_2014]: https://robertsspaceindustries.com/en/comm-link/spectrum-dispatch/14262-LORE-BUILDER-TWENTY-Journeys-Generators
[dev_squad_arm_2014]: https://steamcommunity.com/games/220200/announcements/detail/1315356550594321621
[dev_squad_first_release_2011]: https://web.archive.org/web/20111013113946/http://kerbalspace.tumblr.com/post/6872084213/first-release-is-up
[dev_take_two_ksp2_2023]: https://ir.take2games.com/node/29461/pdf
[dev_take_two_ksp_2017]: https://ir.take2games.com/static-files/f86fae80-882c-4c68-b71c-07560c4b1183
[news_big_think_kaku_2015]: https://bigthink.com/videos/universe-in-a-nutshell-the-physics-of-everything-with-michio-kaku/
[news_den_of_geek_2020]: https://www.denofgeek.com/games/eve-online-players-lives-better/
[news_engadget_ebank_2009]: https://www.engadget.com/2009-07-02-new-perspective-on-eve-onlines-latest-bank-embezzlement.html
[news_engadget_plex_2014]: https://www.engadget.com/2014-05-01-eve-fanfest-2014-economy-talk-highlights-plex-prices-and-reveal.html
[news_engadget_tritanium_2008]: https://www.engadget.com/2008-06-29-making-money-the-origin-of-the-specie.html
[news_evenews24_otec_2018]: https://evenews24.com/2018/01/22/moments-in-history-otec/
[news_fps_review_sc_2026]: https://www.thefpsreview.com/2026/05/26/star-citizen-crosses-1-billion-in-crowdfunding-after-14-years-still-has-no-release-date/
[news_gematsu_fenris_2026]: https://www.gematsu.com/2026/05/ccp-games-rebrands-to-fenris-creations-following-split-from-pearl-abyss
[news_gizmodo_trek_pitch_2011]: https://gizmodo.com/read-the-first-draft-of-gene-roddenberrys-star-trek-pit-5746652
[news_ieee_ebank_2009]: https://spectrum.ieee.org/eve-online-game-player-embezzles-virtual-money-creates-real-trouble
[news_pc_gamer_intercept_2024]: https://www.pcgamer.com/games/sim/kerbal-space-program-2-developer-intercept-games-may-be-closing-as-part-of-take-twos-big-layoff-plan
[news_register_ebank_2009]: https://www.theregister.com/security/2009/07/03/gamer-embezzles-virtual-cash-to-settle-real-debts/1491814
[news_slashdot_straczynski_2013]: https://entertainment.slashdot.org/story/13/04/15/1328251/interviews-j-michael-straczynski-answers-your-questions
[news_space_com_expanse_2015]: https://www.space.com/31437-the-expanse-crazy-sci-fi-tech.html
[ref_edmund_laser]: https://www.edmundoptics.com/knowledge-center/frequently-asked-questions/general-questions/lasers/can-a-laser-beam-be-seen-from-the-side
[ref_fai_karman_2018]: https://www-2025.fai.org/news/statement-about-karman-line
[ref_siggraph_last_starfighter]: https://history.siggraph.org/?p=94037
[related_post_mass_drivers]: {% post_url 2026-08-19-mass_drivers %}
[related_post_orbital_manoeuvres]: {% post_url 2026-08-17-orbital_manoeuvres %}
[related_post_published_wargames]: {% post_url 2026-08-11-published_wargames_of_war_with_china %}
[related_post_solar_sailing]: {% post_url 2026-08-18-solar_sailing %}
[research_abramson_1966]: https://ntrs.nasa.gov/citations/19670006555
[research_allen_eggers_1958]: https://ntrs.nasa.gov/citations/19930091020
[research_bohr_1913]: https://doi.org/10.1080/14786441308634955
[research_levin_et_al_2017]: https://doi.org/10.1017/S1473550417000362
[research_li_et_al_2017]: https://doi.org/10.1364/AO.56.002428
[research_mckagan_et_al_2008]: https://doi.org/10.1103/PhysRevSTPER.4.010103
[research_orthia_2019]: https://doi.org/10.22323/2.18040208
[research_sutton_graves_1971]: https://ntrs.nasa.gov/citations/19720003329
[research_whipple_1947]: https://doi.org/10.1086/106009
[research_wisdom_holman_1991]: https://doi.org/10.1086/115978
[research_yoshida_1990]: https://doi.org/10.1016/0375-9601(90)90092-3
