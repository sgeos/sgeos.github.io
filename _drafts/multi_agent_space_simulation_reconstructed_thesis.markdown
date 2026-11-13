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
and a hardware failure took the notes and the paper together,
with no backup of either.
What follows is therefore a reconstruction from memory.
It does not quote the paper,
give its title
or reproduce its figures,
because none of those survive for anyone to check.

The loss may be no great misfortune.
In the author's view,
an undergraduate class is a poor format for writing a good paper,
because undergraduate classes prioritise grading,
the display of knowledge
and the verification of academic honesty
above the quality of the written material,
and they grade writing against somewhat arbitrary criteria.
This reconstruction is free of those requirements.
Its aim is simply to be a good paper.

The argument in brief is this.
Simulations in which one agent flies under honest physics exist,
and so do simulations in which many agents share one world.
No known product does both.
The reason is not incompetence.
Each product serves its own purpose well,
and honest travel times are hard to share among many people.
A simulation that did both is possible.
It would teach true physics to the people who used it,
and how those people behaved in it would be evidence
of how people might behave in near-term space.
Whether it would pay is the open question.

The article has four parts.
The first sets out the thesis and what a model is.
The second reviews four products as space exploration and space exploitation simulations for the general public,
namely Kerbal Space Program,
Children of a Dead Earth,
EVE Online
and Star Citizen,
and explains why they look as they do.
The third catalogues the soft science fiction conventions
that these products and the wider media present as if they were physics,
and gives the correct physics and a remedy for each.
The fourth turns the reviews and the remedies into a blueprint
for a high-fidelity multi-agent predictive simulation
that is approachable enough to educate the public
and deliberately refrains from miseducating it.

This article uses two terms in a fixed sense throughout.
It calls the people and programs that act inside a simulation agents,
whether a human or an automaton stands behind them.
It calls the products simulations,
because the question it asks of each is how faithfully it simulates.
The whole article is the author's position.
A claim that carries a citation is a sourced fact,
a claim named as an inference is one,
and every other judgement is the author's.
The [Epistemic State](#epistemic-state) section sorts them.

This is the first article in a short series.
An earlier article on this site treats the background mechanics of delta-v,
which recur below
[Orbital Manoeuvres][related_post_orbital_manoeuvres].
Two others treat propulsion that needs no propellant
[Solar Sailing][related_post_solar_sailing]
and propulsion that leaves the reaction mass behind
[Mass Drivers][related_post_mass_drivers].

## The Thesis

The thesis has six parts.

1. **Strong single-agent models exist.**
   A single agent can already fly a spacecraft through a faithful model of orbital mechanics.
2. **Multi-agent models have poor physical models.**
   The reviewed simulations in which many people act together in one world
   simplify or replace the physics of space travel.
3. **A multi-agent simulation with a physical model that does not cheat is possible**,
   and none is known.
   A model that does not cheat may omit physics and may rescale it,
   but it never contradicts it,
   in the sense the next section defines.
   A multi-agent simulation here means many independent agents
   in one persistent world on one clock,
   in a product built for the general public.
   None of the products the paper reviewed is such a simulation,
   and the author knows of none since.
   The paper's list held other simulations that it never reviewed for lack of time,
   so the claim is that none is known,
   not that none exists.
   No obstacle in physics or computation is known,
   and the [Possibility](#possibility) section gives the argument.
   The open problems are problems of design,
   and the hardest of them is time.
4. **The existing products have not failed.**
   Their developers are generally competent,
   and each one's model successfully expresses its own product thesis,
   given its product-market fit and its development constraints,
   including staffing.
   The gap lies between the products,
   not in any one of them.
5. **People adapt their behaviour to conditions.**
   A sufficiently high-fidelity multi-agent simulation should therefore have significant predictive value
   about how people would behave under the conditions it models,
   because its agents are subject to the same incentives and constraints that reality imposes.
   That hinges on a scenario whose incentives and constraints
   are close enough to those of real prospective problems.
   Predictive value is therefore largely a function of being able to formulate realistic scenarios
   that agents are willing to take part in exploring.
   The competence of the agents matters less.
   Most people are of average ability for their station,
   in a simulation as in the world,
   and circumstance and station drive a great many of their decisions.
   Three things bound the value,
   the fidelity of the model,
   how approachable it is
   and the incentives its agents feel.
6. **There is market demand for such a simulation**,
   and meeting it would educate the public.
   A simulation the public will not use teaches nobody.
   This is the least supported of the six,
   and the [Market Demand](#market-demand) section says why.

The paper drew on several purchased texts on modelling and simulation,
which covered subjects such as n-body simulation
and the simulation of fluids and fuel tanks.
The author no longer has those books to hand and no longer recalls their titles,
so this article does not cite them.
The author has also forgotten some of the detailed articles that the paper cited.
The sources below are public ones,
and the argument is a broad synthesis
that leans on space agency sources wherever one exists.
A later article in this series
dates the work that has appeared since the paper
and tests the third claim against it.
Whether such a simulation is commercially viable
is a separate question from whether it is possible,
and the [Time](#time) and [Market Demand](#market-demand) sections below treat it honestly.

Two near misses deserve naming at the outset,
because a reader who knows the field will think of them.
Community modifications let a few agents share Kerbal Space Program,
and its sequel announced the same for the general public,
and the studio closed without delivering it.
The first is a proof of concept at small scale,
and the second is an attempt that failed.
The reviews below say why neither is the simulation the third part describes.

## What Is a Model?

A model is an intentional simplification.
Its purpose is to help a person reason about something.
The test of a model is whether it supports the reasoning a problem needs,
not whether it is true in every detail.

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
and teachers still give it to students meeting atomic structure for the first time.
Physics education researchers have debated whether it should be,
and one study of the debate found that
"Although the evidence for this claim is weak, many have accepted it,"
of the claim that it should not
[McKagan et al. 2008][research_mckagan_et_al_2008].
The Bohr model survives because it fits the problem
of a student who needs energy levels and not orbitals.

**Fidelity should fit the problem.**
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
This article does not fault a product for simplifying,
and it judges each product twice.
It judges first against the product's own purpose,
where the only fault is a simplification that defeats that purpose.
It judges again against its own purpose,
which is a simulation that educates the public and predicts behaviour in space.
For that purpose a stricter rule follows from the same principle,
and it turns on the distinction between **omission** and **contradiction**.
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
A model that does not cheat,
in the words of the thesis,
omits and rescales
but never contradicts.

The Bohr model does contradict.
It is wrong about the electron,
and it is still right-sized for its classroom.
The sizing principle allows that,
because the teacher tells the student that the model is provisional,
and the student replaces it within a few years.
A simulation for the public carries no such warning,
and no later course replaces it.
Its agents learn what it shows them,
and anyone who reads their behaviour as evidence about real space
inherits every contradiction in the model.
For a simulation that teaches and predicts,
the right size therefore excludes contradiction.
The rule is not a law of modelling.
It is the sizing principle applied to those two purposes.

## Review Criteria

The reviews ask the same seven questions of each product.

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
by the studio Squad,
and its store page carries the label
"Single-player"
and none for more than one agent
[Kerbal Space Program][dev_ksp_steam].
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
The community edits that wiki,
but the developer said the same in 2012.
Posting as TheHarvesteR,
Felipe Falanghe wrote that
"The planetarium only simulates two-body gravity,
and switches gravity sources for spacecraft based on the SOI they are in"
[Falanghe 2012][dev_harvester_patched_conics_2012].
SOI is the sphere of influence.

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
and it fails where neither body's pull can be neglected.
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
This is an **omission** and not a **contradiction**,
since the program leaves the third body out
and puts nothing false in its place.
For an agent learning the Hohmann transfer,
the omission is sound.
For an agent who goes looking for that orbit,
it defeats the purpose,
which is the second ground for fault named above.

**Scale and approachability.**
The program's home planet,
Kerbin,
has an equatorial radius of 600 kilometres
[Kerbin][community_ksp_wiki_kerbin],
against Earth's mean radius of 6,371 kilometres
[NASA Earth Fact Sheet][agency_nasa_earth_fact_sheet].
The community wiki puts Kerbin at
"approximately one-tenth the radius of Earth."
A smaller planet with the same surface gravity needs a lower orbital speed,
so a beginner reaches orbit with a small rocket.
This is an approachability choice,
and a good one,
because it changes a parameter and keeps every law.
The change has a price.
The same wiki gives Kerbin
"1/113th the mass"
of Earth,
which at a radius of 600 kilometres against 6,371
implies a density more than ten times Earth's,
and no ordinary matter is so dense.
The planet is impossible as matter and correct as mechanics,
and the mechanics are what the program teaches.
The program still teaches that orbit is a matter of speed and not of height.

**Travel and propellant.**
Every manoeuvre spends propellant,
and a transfer takes the time its orbit takes.
The wiki puts the cost of reaching low orbit about Kerbin at
"approximately 3400 m/s"
of delta-v
[Kerbin][community_ksp_wiki_kerbin].
A single agent passes the waiting by accelerating time,
a device that the multi-agent modifications below must work around.

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
The product thus lets an agent choose fidelity,
and so puts the sizing principle of the previous section into practice.

**The agents.**
The stock program has no multi-agent mode
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
namely that a time warp chosen by one agent cannot be shared,
and a later article in this series treats it in depth.

These modifications are the nearest thing known to a counterexample
to the third part of the thesis,
so the reason they are not one needs stating.
Their physics does not cheat,
since it is the program's own.
Under subspaces the world is shared and its present is not.
The community wiki lists Dark Multiplayer under an approach that,
by its account,
introduces
"paradox-inducing abnormalities"
unless the agents share the same time frame.
Under the alternative,
in which all agents advance time together,
the clock is shared,
and the wiki calls that arrangement
"great for small network games"
[Multiplayer][community_ksp_wiki_multiplayer].
That second mode is the blueprint's shared clock in miniature.
What the modifications lack is the rest of the third part's definition,
namely many agents,
a persistent world
and a product built for the general public.
They are a proof of concept at small scale.
The thesis concerns what happens at large scale,
where one agent's wish to skip ahead meets thousands of others.

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
Its publisher described a school edition,
KerbalEdu,
as
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
It is a great textbook sandbox for a single agent,
and its fidelity is right-sized for what it teaches.

**Takes.**
The blueprint takes the textbook core,
the planning tools that let an agent see a future orbit before committing to it,
and the principle that an agent may choose how much fidelity to handle.

**Refuses.**
It refuses the single-agent world,
and it refuses a fixed patched-conic model where the agents' purposes need more.

## Children of a Dead Earth

Children of a Dead Earth is a single-agent space warfare simulation
by Q-Switched Productions,
released on 23 September 2016
and labelled
"Single-player"
only
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
are each derived from engineering equations in the developer's posts,
so travel costs propellant and takes the time its trajectory takes
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
That post does not establish
whether the simulation integrates the motion of the liquid itself.

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
each move at about 7.66 kilometres per second,
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
Its users joke that using it needs several science degrees.
The author's experience is milder.
Anyone with a proper science degree can work out the parts
that their own programme did not cover.
But a simulation that needs a degree to begin with
is not a simulation for the general public.
It is simply too complex for most people.

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
The developer calls its human agents capsuleers
[Capsuleers][dev_ccp_capsuleers].

**A measured economy.**
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
The simulation's physical models are
so far from the physics they depict that they are wrong.
Ships fly as submarines move through water.
The developer's own account of warp gives every ship a
"maximum speed"
under its own engines
[CCP 2013a][dev_ccp_warp_2013].
A top speed under continuous thrust is already a departure from mechanics.
In vacuum the acceleration from a given thrust does not fall as speed rises,
and a ship gains speed for as long as it has propellant to burn.
A search found no velocity law published by the developer.
The community's own guide gives one.
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
That is the law of a body pushed through a viscous fluid,
in which drag grows with speed until it balances the thrust.
The developer's statements agree with the guide's law on two points,
the top speed above and the alignment time below.
The same guide says that when propulsion stops,
the ship decelerates to a standstill,
because the model
"assumes that space has some substance to it and thus some friction."
The author has watched ships in the simulation slow to rest in just that way.
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
about $1.39\,\tau$,
which agrees with the alignment time given in the developer-hosted documentation for third-party developers
[Useful Formulae][dev_ccp_useful_formulae].
Warp speeds run from about 1.5 to 8 astronomical units per second
by the community's figures
[Warp][community_eve_uni_warp],
so a crossing that would take a real spacecraft months takes seconds.
Stargates link systems.
A ship spends no propellant,
and the simulation tracks no delta-v.
Ships draw on a capacitor that recharges from an onboard generator,
which powers modules and starts each warp,
and only capital jump drives burn fuel
[Capacitor][community_eve_uni_capacitor]
[Jump Drives][community_eve_uni_jump_drives].

**The agents.**
Every agent that matters is a person.
The interactions between them therefore have full fidelity,
because the simulation does not simulate them at all.
It only sets the rules of a sandbox around them,
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

**Approachability.**
An agent needs no physics to act,
since the simulation contains none to know.
What an agent must learn is the economy,
the politics
and the other agents,
and that difficulty is of the kind the simulation exists to offer.

**The product thesis.**
A search found no statement of aim by the developer beyond the descriptions quoted above,
a single universe in which agents compete,
run as a sandbox.
This article infers the thesis it attributes to the product from them
and from the product itself.
It is one world whose content is the dealings of its agents with one another.

### The Economy

EVE Online's mechanics change from one release to the next,
so each figure below carries the date of its source.
A figure that is out of date still describes how agents acted at the time,
and the conclusions drawn from it do not depend on its being current.

EVE Online is fascinatingly odd here.
Its individual models are terrible,
yet they interlock so comprehensively that the whole has real predictive value.
The commodity market is the one place where the model is strong and accurate,
because nothing simulates it.
Real agents set every price,
so the market behaves as markets do.

This subsection is long,
because the economy is the best evidence this article has
that agents in a simulation behave as people do.
It describes the supply chain and its rules,
with the developer's formulas for readers who want them,
then the money,
and then the real economic behaviour that appeared with nobody designing it.
A reader in a hurry can pass over the formulas
without losing the argument.

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
A supply chain that exists and works
matters more to that problem than one that is accurate.
Being able to navigate at all,
and to operate from and in different places,
matters more than navigating realistically.
EVE Online therefore passes the fidelity test for its own purpose
and fails it for education.
The blueprint below must pass both.
The author's conjecture is that more realistic simplified models could have worked in EVE Online,
and that the developer lacked the specialists to distil them for the product.
No source consulted confirms or refutes it.
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
A search found no statement by the developer on the name's origin,
so the borrowing is the author's reading,
of technobabble pulled into the base of a supply chain.

**Industry costs.**
The developer publishes its formulas.
This article quotes them to show what kind of model the parts are.
Each is a rule of bookkeeping with no physics in it,
and one of them is a sound piece of economic design.
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
When the developer introduced the index in 2014,
it defined it from
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
Nothing in that rule is manufacture.
It is an entry in a ledger,
and agents have built a real industry on it.

**The market.**
Agents set prices in regional markets,
and the developer's own economist has noted
"the unrelenting dominance of Jita as a central hub"
[CCP 2015][dev_ccp_economy_vegas_2015].
Every sale pays a sales tax,
raised in 2025
"from 4% to 7.5%"
[CCP 2025][dev_ccp_patch_22_02_2025],
and every order pays a broker's fee.
Structures owned by agents set their own fees,
and the developer observes that
"It is not uncommon for structure owners to give themselves and their friends a 0% fee"
[CCP 2020][dev_ccp_broker_relations_2020].
A haul between two hubs is worth making only when the margin survives the fees.
With $p\_{\mathrm{A}}$ the price paid at the source,
$p\_{\mathrm{B}}$ the price received at the destination,
$\lambda\_{\mathrm{s}}$ the sales tax rate,
$f\_{\mathrm{b}}$ the broker's fee rate
and $c\_{\mathrm{h}}$ the cost of hauling one unit,
a trade placed as an order at each end pays when

$$
p_{\mathrm{B}} \left( 1 - \lambda_{\mathrm{s}} - f_{\mathrm{b}} \right) - p_{\mathrm{A}} \left( 1 + f_{\mathrm{b}} \right) - c_{\mathrm{h}} > 0
\tag{9}
$$

The developer set the Accounting skill in 2019 to reduce the sales tax by 11 percent per level
and Broker Relations to reduce the broker's fee by 0.3 percentage points per level
[CCP 2019][dev_ccp_taxes_2019],
and the community guide gives the base broker's fee at a station of the simulation's own as 3 percent
[Trading][community_eve_uni_trading].
Taking the sales tax of 2025 with the skill effects of 2019,
which assumes that those effects did not change in between,
the rates at the fifth level of each are about 3.4 and 1.5 percent.
Buying at 100 and selling at 110 then leaves about 3.1 per unit
before the cost of hauling,
so a gross spread of 10 percent shrinks to a net margin near 3.

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
In 2008 the developer let subscribers convert paid subscription time into an item,
the
"30 Day Pilot's License Extension (PLEX),"
which a subscriber could put
"directly on to the market"
[CCP 2008][dev_ccp_plex_2008].
A PLEX
"can be bought via the in-game market for ISK and then applied to add 30 days of game time"
[CCP 2009][dev_ccp_plex_2009],
and in 2017 the developer converted each
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
which resembles a central bank's intervention to steady a price.
The developer forbids trade outside that channel.
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
real economic behaviour appeared that nobody designed.
- **Tax havens.**
  The simulation's starter corporations once offered
  "war declaration immunity and 0% tax,"
  which the developer said gave them
  "an inherent advantage over player corporations which was never intended"
  [CCP 2009a][dev_ccp_taxes_2009].
  The developer responded in 2009 by taxing the starter corporations at 11 percent,
  a rate it chose after researching the average taxes of corporations run by agents.
  Its economist had already measured corporate taxation,
  finding that
  "The average tax rate is 8.6% but the median is tax rate is 5%"
  [CCP 2007a][dev_ccp_corporations_2007].
- **Embezzlement at a bank.**
  In 2009 an agent who ran a bank owned by agents,
  EBank,
  embezzled
  "roughly 200 billion ISK, or 8.6% of EBANK's 2.3 trillion ISK in deposits"
  [Engadget 2009][news_engadget_ebank_2009],
  and,
  as Reuters reported,
  exchanged it for cash through the black market
  [Reuters 2009][news_reuters_ebank_2009],
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
  and one of the cartel's own organisers described it in the trade press as
  "a price-fixing cartel which controls the Technetium supply"
  [The Mittani 2012][news_ten_ton_hammer_otec_2012].

The developer answers in kind.
Faucets,
sinks,
inflation indices
and sales of PLEX from reserve
are monetary policy under other names,
practised by the developer and not by the agents.

**Skills that transfer.**
High-commitment simulations can hold their agents to very high expectations,
and the transfer runs both ways.
A survey reported in an article presented by the developer
found that
"56% of players said that skills they learned through playing EVE had proven to be valuable in their lives outside of the game and in their careers"
[Den of Geek 2020][news_den_of_geek_2020].
The developer sponsored the source,
and a search did not find the underlying study,
so this article reports the figure as the developer's claim.
Peer-reviewed work is more cautious but points the same way.
One study examined leadership in online environments shared by many participants,
EVE Online among them
[Lisk et al. 2011][research_lisk_et_al_2011],
and another found evidence that leadership practised online spills over into work
[Xanthopoulou and Papagiannidis 2012][research_xanthopoulou_papagiannidis_2012].

### The Verdict on EVE Online

**Education.**
EVE Online largely simulates the science fiction of film and television,
and its soft science fiction sandbox borders on miseducating the public,
because it shows its agents,
year after year,
that ships coast to a stop
and that a solar system is a few seconds wide.

**Takes.**
The blueprint takes the market,
the single shared world,
real people as agents,
loss that lasts,
and the lesson that systemic interaction can matter more to agents
than the realism of any one component.

**Refuses.**
It refuses drag in vacuum,
free travel,
and the absence of propellant.

## Star Citizen

Star Citizen is a multi-agent space simulation by Cloud Imperium Games.
It remains in alpha testing as of this writing.
The developer's own crowdfunding counter reported funds of 106,210,587,748
and a head count of 6,757,438 on 13 November 2026
[RSI Crowdfund Statistics][dev_rsi_crowdfund_stats].
The counter's data labels the head count as fans,
who need not all be paying backers,
and it does not state the units of the funds.
Read as cents,
the funds come to about 1.06 billion United States dollars.
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
The product thesis is that agents can act out adventures
as if they were the stars of their own films.
Its roles are rich and asymmetric,
including
"exploration, hauling, trading, mercenary, outlaw, bounty hunting and mining,"
with more planned
[Roberts 2020][dev_rsi_letter_2020].

Star Citizen appears to be broadly aspiring to a higher-fidelity version of EVE Online's soft science fiction thesis,
with its own spin.
Where EVE Online's agents command ships from a capsule,
Star Citizen's agents act at the tactical level of a human avatar,
on ships,
on stations
and on the surfaces of planets and moons.
That makes the two very different in practice.
A large ship has several stations that do very different things,
flown together by a crew,
and a ship can carry smaller craft and ground vehicles in its hold.
The developer's own description of the Carrack promises
"Muiltiple seats with their own dedicated actions"
and
"a Pisces-class launch (design redacted) and an Ursa-class rover for ground exploration"
[RSI 2014][dev_rsi_carrack_2014].

Its activities split broadly in two.
**Ship-based** loops include bounty hunting and cargo,
present by Alpha 3.0.0 in December 2017
[Star Citizen Alpha 3.0.0 Patch Notes][dev_rsi_patch_300_2017],
mining by ship,
added in Alpha 3.2.0 in June 2018 to
"the moons of Crusader (Daymar, Yela, and Cellin)"
[Alpha 3.2.0 Patch Notes][dev_rsi_patch_320_2018],
and salvage,
whose
"first implementation"
arrived in Alpha 3.18 in March 2023
[RSI Roadmap][dev_rsi_roadmap].
**Personnel-based** loops include first-person combat in bunkers,
added as
"Hurston underground bunker FPS AI missions"
in Alpha 3.4.0 in December 2018
[Alpha 3.4.0 Patch Notes][dev_rsi_patch_340_2018],
hacking at terminals,
exploring on foot,
and driving ground vehicles.
Many ships have several seats,
so a pilot may fly with no gunners or several,
depending on the ship's configuration and the people available.
Engineering arrived as a station of its own in Alpha 4.5.0 in December 2025,
when
"Ships now feature an engineering terminal providing comprehensive oversight of all ship systems"
[Star Citizen Alpha 4.5.0][dev_rsi_patch_450_2025].
Medicine became a loop in Alpha 3.15 in 2021,
in which
"ambulances (such as the Cutlass Red) can treat minor wounds and stabilize patients in transit to hospital"
[Deadly Consequences][dev_rsi_alpha_315_2021],
so search and rescue is a nominal experience in the simulation.
The release notes consulted list no dedicated search-and-rescue missions.
Other loops remain planned.
Crafting arrived in a first tier for personal equipment in 2026,
while base building,
farming
and data running remain announcements.
Its characteristic scale of interaction is the crew and the landing party,
where EVE Online's is the fleet and the market.
The product has been a buggy mess in perpetual alpha,
and it has been getting better.
Its management and its controversies aside,
the product as delivered is interesting enough to care about,
perpetual alpha and all.
It is directionally promising.
EVE Online receives more attention in this article only because it is the more mature product,
with two decades of a running economy to study.

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
and it would be surprising if the simulation modelled propellant slosh at all.
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
The developer designed for orbits.
In 2016 Chris Roberts said that day and night would come from a planet rotating on its axis,
and that the system
"will also be able to rotate the planet around the sun"
[GamersNexus 2016][news_gamersnexus_roberts_2016].
A search found no developer statement on whether that capability is in use.
The community wiki states that the planets
"spin, have a day and night cycle, and are planned to eventually orbit"
[Planet][community_sc_tools_planet].
On that evidence,
which on the present state is the community's and not the developer's,
the bodies rotate in place at fixed positions,
and the simulation,
though designed for orbits,
does not simulate them.
That matches the author's experience.
The author recalls noting,
while using the simulation,
that its celestial bodies were not subject to celestial mechanics,
and that a body sits at fixed coordinates to which a ship travels.

**Gravity.**
Ships and stations carry artificial gravity.
The developer's design brief for it says that it
"must be able to be turned on and off,"
and that
"'handwavium' is completely acceptable if it makes sense"
[Lore Builder Twenty][dev_rsi_lore_gravity_2014].
Gravity of that kind is the gravity of film and television,
and the catalogue below treats it.

**Launch and reentry.**
Since 2020 the simulation has modelled lift and drag in atmosphere.
The developer states that
"Ships with wings are now able to stall"
and that
"In atmosphere, thrusters now lose efficiency and become much weaker"
[Flight and Fight Improvements][dev_rsi_flight_2020].
A search found no source for reentry heating as a hazard
or for any requirement to reach orbital speed in order to reach orbit.
Agents fly through launch and reentry,
but the simulation does not model them as the challenges they are.

**Approachability.**
An agent needs no physics to act here either.
An agent enters the simulation as a person in a body,
who walks,
flies
and shoots by the conventions of film,
and that is as approachable as an interface can be.

**Education.**
Star Citizen is a multi-agent soft science fiction reenactment,
and its model expresses that thesis well.
Like EVE Online,
it is a soft science fiction sandbox that borders on miseducating the public.

**Takes.**
The blueprint takes asymmetric roles,
the crew as the unit that flies a ship,
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
The four are prominent,
so the finding is about products that succeeded
and not about every attempt.
Kerbal Space Program wanted approachable rocketry and got it.
Children of a Dead Earth wanted to discover space warfare and did.
EVE Online wanted a single universe of real people with a real economy,
and Star Citizen wants agents to live their own films.

The table sets the four reviews side by side.

| | Kerbal Space Program | Children of a Dead Earth | EVE Online | Star Citizen |
|---|---|---|---|---|
| Orbits | Patched conics | N-body | None, ships fly under a drag law | None found, bodies rotate in place |
| Travel | True time, skipped by accelerating time | True time | Warp, seconds per system | Quantum travel |
| Propellant | Tracked | Tracked | None, except jump fuel | Tracked at low fidelity |
| Agents in one world | One | One | Many, in a single world | Many, up to 500 per shard |
| Physics needed to begin | Little | A great deal | None | None |
| What it shows | True physics, with sound omissions | True physics, to few | Contradicted physics | Contradicted physics |

The two columns on the left hold the honest physics,
and the two on the right hold the agents.
No column holds both.

The developers are generally competent.
Each product reflects a combination of product-market fit and its product thesis.
Where one of the four falls short of the standard this article sets for high-fidelity space simulation,
it is because it had a different product thesis
and the developer achieved it.
Many other titles succeed on their own terms
as multi-agent soft science fiction simulations.
Falling short of that standard in that way is not a failure of craft.
It is a choice of target.
The other way to fall short is to aim at the standard and miss,
as Kerbal Space Program 2 did.

Staffing is part of the explanation.
A model of high fidelity costs specialists to build and to maintain.
A small studio can afford it only in a narrow product,
as Children of a Dead Earth shows,
and a large studio can afford it only if its market rewards it.
The two multi-agent products drew their audiences with the simplest physics,
and the product that drew a large audience with honest physics,
Kerbal Space Program,
drew it one agent at a time.
That is the gap the thesis names.
No known product has yet paid for physics that does not cheat
in a product built for many agents and the general public at once.

Management is the other part,
and two products show it.
Kerbal Space Program 2,
a sequel by a new studio,
Intercept Games,
entered early access in February 2023.
Its publisher's announcement listed a multi-agent mode among the features to come,
saying that
"Players will be able to both cooperate and compete with friends to explore space together"
[Take-Two 2023][dev_take_two_ksp2_2023].
That made it the one known attempt at a multi-agent simulation on the textbook core
in a product for the general public,
and it is a development since the paper.
The press recorded that the sequel,
first due in 2020,
"limped into early access"
on Steam,
that
"Bugs and performance issues were major problems,"
and that it
"launched without features included in the original"
[PC Gamer 2024][news_pcgamer_intercept_2024].
The mode never arrived.
In November 2026 the product's store page still lists
"colonies, interstellar travel, and multiplayer"
as planned,
under a notice from the store that the developers last updated the product more than two years ago
[Kerbal Space Program 2][dev_ksp2_steam].
In 2024 Take-Two filed a notice with Washington's Employment Security Department
of a permanent closure in Seattle affecting seventy workers,
which did not name the studio
[Washington WARN Notices][ref_wa_esd_warn],
and the press reported,
citing Bloomberg,
that Take-Two was shutting Intercept Games down
[GeekWire 2024][news_geekwire_intercept_2024].
The author's judgement is that mismanagement sank the project,
and the studio with it.
What the record shows is narrower.
The attempt failed in execution
before it could test whether the public wanted the result.
Star Citizen is the harder case.
It has stayed in alpha for well over a decade,
yet it has found an odd market equilibrium
in which a nominally unfinished product earns large recurring revenue.

The developer collects its revenue as pledges,
not purchases.
The developer's terms state that
"You do not purchase anything, you make a pledge towards the development of the Game"
and that pledge funds
"are a deposit to be used for the development and production cost of the Game"
[RSI Terms of Service 2026][dev_rsi_tos_2026].
A pledge is nonetheless contractually binding.
The same terms make any unearned portion non-refundable
"until and unless RSI has ceased development and failed to deliver,"
with an arbitration clause
and a withdrawal period of thirty days added in 2023.
The refund condition has tightened over time.
The original terms of 2012 allowed a refund twelve months after the estimated delivery date,
and the press reported the change in 2016 to the condition of ceased development at the time
[Massively Overpowered 2016][news_massively_refund_2016].
The sales model is grey,
in the author's view,
and the project is controversial.
Most of that controversy is the sentiment of customers and spectators,
which primary sources do not record,
and the developer has no incentive to acknowledge unhappiness publicly.
The press records some of it.
A backer who sued for a refund and lost said of the developer that
"They figured out how to sell scope creep itself"
[Kotaku 2018][news_kotaku_refund_2018],
the developer told another that
"Refunds are always discretionary and are considered on a case-by-case basis"
[Polygon 2017][news_polygon_refund_2017],
and the developer added a disclaimer to its ship sales
after the United Kingdom's advertising regulator called them misleading
[PC Gamer 2021][news_pcgamer_asa_2021].

Cloud Imperium publishes its annual financials,
which make the equilibrium measurable.
The reports for 2020 to 2024 state income
and costs including capital expenditure,
in millions of United States dollars,
for the whole company,
Star Citizen and Squadron 42 together
[Cloud Imperium 2020][dev_cig_financials_2020]
[Cloud Imperium 2021][dev_cig_financials_2021]
[Cloud Imperium 2022][dev_cig_financials_2022]
[Cloud Imperium 2023][dev_cig_financials_2023]
[Cloud Imperium 2024][dev_cig_financials_2024].
For 2020 to 2022 the income is the sum of the stated pledges or sales,
subscriptions
and other income,
and the cost is the sum of the stated costs and capital expenditure.
With $\rho\_{y}$ the ratio of spending to income in year $y$,
$C\_{y}$ the costs including capital expenditure
and $R\_{y}$ the income,

$$
\rho_{y} = \frac{C_{y}}{R_{y}}
\tag{10}
$$

| Year | Income | Costs with capital expenditure | Ratio |
|---|---|---|---|
| 2020 | 88.2 | 80.9 | 0.92 |
| 2021 | 100.4 | 100.5 | 1.00 |
| 2022 | 130.7 | 129.4 | 0.99 |
| 2023 | 143 | 163 | 1.14 |
| 2024 | 146.6 | 161 | 1.10 |

Over the five years the company took in about 609 million dollars and spent about 635 million,
a ratio of 1.04.
It spends what it raises,
and in the last two years more.

That supports two readings,
and the article owes the reader both.
On the first,
the perpetual alpha is the business model working as intended.
The alpha label lowers expectations,
selling ships ahead of what agents can do with them depends on nothing being final,
and the terms keep pledges non-refundable for as long as development continues.
That reading fits this article's own principle
that developers are generally competent and achieve their product thesis.
Star Citizen has achieved product-market fit while still in alpha,
which is highly irregular.
Under those circumstances the author might stay in perpetual alpha too,
since a release would trade a working market for a set of expectations the product would then have to meet.
On the second,
the project is mismanaged.
The author is not unhappy with Star Citizen,
but understands why some people are,
and leans to the second reading from professional experience in the game industry.
The figures sharpen rather than settle the question.
A ratio near one is consistent with what the terms promise,
since a pledge is a deposit towards development,
and the figures show the company banking no profit.
This article did not establish what covered the excess of spending over income
in the last two years.
Income that recurs without a release imposes no deadline,
which is how a project can grow for fourteen years without one.
What the figures cannot show is what the spending bought.
The author's judgement is that spending of about 635 million dollars in five years,
on top of the eight years before them,
would have produced a version 1.0 release under ordinary control of scope.
That judgement rests on the combination of cumulative expenditure and a perpetual alpha,
and a reader who weighs the scale of the ambition differently
may reach the first reading.
When the author was following it,
the developer was largely selling dreams,
ships and features either not yet built or only partially implemented,
and delivering at a pace sufficient to keep its backers engaged.
Setting the ethics of that model aside,
Star Citizen is plainly doing something right
even as it does a number of other things wrong.
Neither case is evidence against the competence of developers in general.
Both show that an ambitious space simulation is expensive and risky.
The fourth claim names exactly that constraint.

## Soft Science Fiction and Its Remedies

The two multi-agent products share their physics with film and television.
Star Citizen says as much of its aim,
and EVE Online's borrowed mineral shows the lineage in one case.
That the developers inherited the conventions and did not arrive at them independently
is otherwise an inference from the resemblance.
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
"similar" to Earth
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
A search found no primary source saying that the production chose warp drive for the same reason.
That it served the same purpose,
literally a wave of the hand that delivers the cast to the next adventure,
is the author's inference from the format.

EVE Online and Star Citizen use that model of travel.
They can justify it for the same reasons the series did.
Both put agents into adventures in a shared world,
and the adventures need the agents to be in the same place at the same time.
The justification is real,
but it is a justification for the format,
not a description of space.

Three causes kept these conventions alive.
The first is the format,
as the western shows.
The second is that effects budgets limited what a production could show faithfully,
as the transporter shows.
The third,
in the author's view,
is that writers often lacked training in the physics they depicted
and audiences seldom knew the difference.
The second cause weakens with every year since the arrival of computer-generated imagery.
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
A simulation is a participatory medium.
It does not only show a convention,
it trains its agents to act on it.
Education research gives two reasons to take that seriously.
Fiction does teach false science.
A study of middle school students who watched the film The Core found that
"a single viewing of a science fiction film can negatively impact student ideas regarding scientific phenomena"
[Barnett et al. 2006][research_barnett_et_al_2006].
The study was small,
the 82 students of one teacher,
and its authors say that its findings may not hold for the population at large.
And errors about motion are among the hardest to give up.
Clement reported in physics students a mistaken view of force and acceleration that
"is highly resistant to change"
and traced it to
"a deep-seated preconception that makes a full understanding of Newton's first and second laws very difficult"
[Clement 1982][research_clement_1982].
A later review of the field summarised the finding.
In its words,
"many students believe that motion implies a force, both before and after the study of introductory mechanics"
[McDermott and Redish 1999][research_mcdermott_redish_1999].
That belief is the flight model of EVE Online,
in which a ship moves only while its engine pushes.
It is an inference that an agent who flies under that model for years
is practising the preconception a physics course must then undo.
A search found no study of what a simulation's flight model does to its agents' physics,
so the miseducation this article warns of is a hypothesis with indirect support.
If it holds,
solving the problem described here
is of direct relevance to educating the public
for the future benefit of humanity.

### The Catalogue

Each entry gives the convention,
the correct physics
and the remedy,
and says where the convention appears
when a reviewed product or a source shows it.

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
The error,
wherever it occurs,
is to carry the behaviour into vacuum.

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
\tag{11}
$$

An engine with a specific impulse of 450 seconds and a mass ratio of four
gives a delta-v of about 6.1 kilometres per second.

Time is the other cost.
The cheapest two-burn transfer between two circular orbits in the same plane is the Hohmann transfer,
half an ellipse that touches both
[Curtis 2020a][book_curtis_2020_interplanetary].
With $t\_{\mathrm{H}}$ the transfer time,
$a\_{\mathrm{t}}$ the semi-major axis of the transfer ellipse,
the mean of the two orbital radii,
and $\mu\_{\odot}$ the Sun's gravitational parameter at $1.327 \times 10^{11}$ cubic kilometres per second squared,

$$
t_{\mathrm{H}} = \pi \sqrt{\frac{a_{\mathrm{t}}^{3}}{\mu_{\odot}}}
\tag{12}
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
\tag{13}
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
\tag{14}
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
\tag{15}
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
\tag{16}
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
\tag{17}
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
Researchers have studied active magnetic shielding against radiation
[Westover et al. 2019][agency_nasa_maarss_2019],
but it remains a concept.

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
\tag{18}
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
Model heat as a resource that a craft must reject,
give every craft a thermal signature,
and do not let a ship vanish.

**Space is cold.**
Space has almost nothing in it to be cold.
Vacuum is an insulator,
as the thermal guidance above implies.
A body in vacuum loses heat only by radiation,
which is slow at ordinary temperatures,
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
and let fragments and radiation carry the damage,
since there is no air to carry a blast.

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
\tag{19}
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
and warfare,
and Children of a Dead Earth's developer notes that
"seconds or even minutes of lag in command would prove fatal in combat"
[How Realistic Is It Actually?][dev_code_realistic_2016].

**Reentry by friction, and launch without cost.**
Popular accounts describe reentry heating as friction.
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
Leaving slosh out is an omission and not a contradiction,
and it appears here because the remedy is a matter of sizing.

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
A search found no source of any kind for inertial dampeners.
By Newton's second law a crew feels every acceleration of its ship,
and that limit on a crewed craft's manoeuvres is part of the physics worth teaching.

**Remedy.**
Do not include either.

**Black holes that suck.**
NASA states that black holes do not suck in other matter,
and that
"From far enough away, their gravitational effects are just like those of other objects of the same mass"
[NASA Black Holes][agency_nasa_black_holes].

**Remedy.**
Use the gravity of the mass,
which an n-body model does unprompted.

## A Blueprint

The reviews and the remedies converge on one design.
It describes a high-fidelity multi-agent predictive simulation for the general public
that is approachable enough to educate
and refrains from miseducating.

Its nearest concrete form is a real-time,
multi-agent simulation built on the method of Children of a Dead Earth.
Real-time here means continuous and persistent.
The world runs around the clock whether or not a given agent is present,
and it does not proceed in turns.
It does not mean that the clock runs at the rate of a wall clock,
which the [Time](#time) section treats.
Near-term space means the solar system under known physics
and engineering that can be specified from it,
which is the standard Children of a Dead Earth set itself.
That simulation already has the physics,
derived from engineering equations with no vision imposed on the result.
What it lacks is the shared world.
The design below keeps the method and the physical core,
runs them in real time on a shared clock,
puts many human agents into one persistent world with a market and asymmetric roles,
and makes the whole approachable by tools rather than by fiction.
It takes a method,
not a product,
and its builders would derive every system afresh from first principles.

### Possibility

The third part of the thesis says that such a simulation is possible.
The claim rests on three observations.

The first is that each half already exists.
Children of a Dead Earth runs n-body gravity and systems derived from engineering equations
on a personal computer,
and EVE Online holds a large population in one persistent world.
That second proof has a caveat.
EVE Online's record is 65,303 agents connected at once,
which the press reported in 2013
[Engadget 2013][news_engadget_pcu_2013],
and those agents occupied a world divided into systems joined by gates.
The developer balances its load by moving whole systems between server processes,
and it has written of an overloaded system that
"We cannot split the solar system up into more units and spread them out"
[CCP 2010][dev_ccp_character_nodes_2010].
When a battle outgrows its process,
the developer slows that process's clock,
down to what it calls
"the artificial 10% cap on the time dilation factor"
[CCP 2014b][dev_ccp_hed_gp_2014].
Star Citizen's shards hold 500 agents each.
Neither product shows that one continuous solar system can hold as many agents,
and a world whose orbits all run on one clock
cannot slow one region without breaking the timing of the rest.
The [Physical Core](#the-physical-core) section proposes a division that the physics itself supplies.

The second is that the halves do not obstruct each other.
A craft's pull on other craft and on the planets is negligible,
so each craft is a separate problem,
a small body moving among massive ones whose positions are already known.
Trajectory software for real missions works the same way.
One account of the standard method says that it ignores the forces of the spacecraft on the celestial bodies,
so that
"the motion of the celestial bodies can be determined independently from the motion of the spacecraft"
[Berry and Coppola 2007][research_berry_coppola_2007].
The cost of the gravity model therefore grows in proportion to the number of craft
and not to its square.
With $t\_{\mathrm{step}}$ the time one processor core needs to advance every craft by one step,
$N\_{\mathrm{c}}$ the number of craft,
$\bar{n}$ the mean number of bodies each craft feels
and $t\_{\mathrm{f}}$ the time of one evaluation of the inverse-square law,

$$
t_{\mathrm{step}} = N_{\mathrm{c}}\, \bar{n}\, t_{\mathrm{f}}
\tag{20}
$$

A published benchmark of gravitational force loops measured two billion evaluations a second
on one processor core with vector instructions,
twenty times the rate of plain code
[Tanikawa et al. 2013][research_tanikawa_et_al_2013].
Plain code therefore needs about 10 nanoseconds for each evaluation.
The benchmark used single precision and a solar system needs double,
so this article allows 20.
One hundred thousand craft,
each feeling thirty bodies,
then need three million evaluations and about 0.06 seconds for each step.
Binding each craft to a parent body,
as the [Physical Core](#the-physical-core) section describes,
cuts the bodies a craft feels from thirty to about three
and the step to about 6 milliseconds.
The work divides cleanly among cores,
because no craft waits on another.
A craft in interplanetary cruise also needs far fewer steps than one in low orbit.
That estimate is the author's and shows an order of magnitude only.
It covers the propagation of the live world and nothing else.
The number of steps in each second of real time grows with the compression of the clock.
The planning tools may cost more than the world does,
since each plan propagates a craft across months and each edit repeats the work.
And the estimate leaves out collisions,
sensors
and everything else that happens when craft meet,
which is where a real implementation would spend its effort.

The third is that the hardest problem is not computation.
It is time,
and the [Time](#time) section treats it.
The claim of possibility is therefore conditional.
No obstacle in physics or computation is known.
Whether a design can make the result palatable to the general public
depends on the problem of time,
which this article names and does not solve.

### Principles

1. **Omit, never contradict.**
   The simulation may leave a phenomenon out when the agents' purposes do not need it,
   and it says so.
   It never replaces a phenomenon with its opposite.
   It may change parameters,
   such as scale and the rate of time,
   but never laws.
   This is the sizing principle of the earlier section
   applied to a simulation that teaches and predicts,
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
   Tools that explain and compute supply approachability.
   Fiction that removes the physics never does.
4. **Make loss last.**
   Other agents can destroy what an agent builds,
   and what they destroy stays destroyed,
   as in EVE Online.
   Agents who risk nothing they value give no evidence
   of how people behave when something is at stake.
5. **Be open to checking.**
   The simulation publishes its model,
   its economy
   and the record of what happened,
   because evidence nobody can check is not evidence.

### The Physical Core

- **Scale.**
  The world is the real solar system at its true scale.
  Kerbal Space Program's small planets are a sound change of parameter
  for a single agent learning to reach orbit.
  A simulation meant to predict behaviour in near-term space
  needs the distances and the delta-v budgets of near-term space.
  Rescaling and time compression both shorten a voyage.
  Rescaling also lowers every delta-v budget and shortens every light time,
  so it changes the prices and the delays the simulation exists to study.
  Compression changes only how long those delays feel.
  The design therefore prefers compression,
  and the rate of time is the one parameter it changes.
  A reduced system at a lower compression is an alternative it has not weighed further.
- **Gravity.**
  The planets and moons follow ephemerides,
  precomputed positions from a real solar system model,
  such as the planetary and lunar ephemerides
  that the Jet Propulsion Laboratory fits to observations
  [Park et al. 2021][research_park_et_al_2021]
  and publishes for download
  [JPL 2020][agency_jpl_ephemerides_2020].
  That is an **omission** of their response to the agents' craft,
  which is negligible,
  and not a **contradiction**.
  Of a planet that gives a spacecraft a gravity assist,
  NASA writes that
  "The massive planet's loss is too small to be measured"
  [NASA Basics of Spaceflight][agency_nasa_bsf_trajectories].
  The simulation integrates craft numerically under n-body gravity,
  so Lagrange points,
  the perturbations of third bodies
  and gravity assists emerge unscripted.
  The equation given below treats each body as a point mass.
  The oblateness of a planet,
  the decay of a low orbit in thin air
  and the pressure of sunlight are further terms of the same equation,
  and one account of the standard method lists solar radiation pressure,
  atmospheric drag
  and corrections for general relativity among the forces on a spacecraft
  [Berry and Coppola 2007][research_berry_coppola_2007].
  By this article's own test agents need those terms wherever they work in low orbit.
  An orbit that keeps pace with the Sun exists because
  "The Earth's equatorial bulge imparts an out-of-plane force on the orbit which causes a gyroscopic precession of the line of nodes"
  [Mesarch 2018][agency_nasa_orbit_primer_2018],
  and NASA notes that
  "Satellites in a low Earth orbit are also pulled out of their orbit by drag from the atmosphere"
  [Riebeek 2009][agency_nasa_orbit_catalog_2009].
  The design adds those terms there.
  An integrator whose energy error stays bounded over long runs,
  such as a symplectic method,
  keeps orbits stable through months of simulated time.
  Yoshida constructed symplectic methods of higher order
  [Yoshida 1990][research_yoshida_1990],
  and Wisdom and Holman built symplectic maps for n-body problems with a dominant central mass
  and followed the outer planets with them for a billion years
  [Wisdom and Holman 1991][research_wisdom_holman_1991].
- **Gravity at scale.**
  Honest gravity need not be expensive gravity.
  Three practical techniques keep it affordable without contradicting it.
  The first is the ephemeris itself.
  Bodies that follow precomputed positions cannot perturb one another into disorder,
  and bodies integrated live can.
  The makers of the Principia modification found that under n-body gravity
  "the Jool system breaks down within 19 days,"
  and they altered the stock system to keep its moons
  [Principia Jool Stability][dev_principia_jool].
  Kerbal Space Program avoids the problem as the blueprint does,
  and its wiki notes that
  "the orbits of the celestial bodies can't be changed"
  [Sphere of Influence][community_ksp_wiki_soi].
  The second is to bind each craft,
  and each small natural object,
  to a parent body.
  The simulation integrates the craft in the parent's frame,
  where it feels the parent in full
  and every other body as a perturbation,
  and it drops a perturbation that falls below a declared threshold.
  The implementation subsection below gives the equation and the sizes.
  A craft in low orbit about Earth needs Earth,
  the Moon
  and the Sun,
  and Jupiter at its nearest adds about one part in a trillion.
  The third is to divide the world along the same lines.
  The neighbourhood of each body is a natural shard,
  a craft passes from one shard to the next at the sphere of influence,
  and the cruise between planets is a shard of its own.
  Light time helps here.
  Events in two shards cannot affect each other faster than light crosses the gap,
  which takes 1.3 seconds from Earth to the Moon and minutes between planets,
  so the machines that run the shards have that long,
  divided by the compression of the clock,
  to agree.
  Each technique is an omission of stated size.
  The design leaves out the momentum a craft exchanges with the body it flies past,
  the slight effect of a flyby on that body's rotation
  and the pull of one craft on another,
  and it says so.
  It keeps the behaviour that matters at the scale of a mission,
  namely transfers,
  captures,
  gravity assists,
  Lagrange points
  and the slow work of perturbations on an orbit.
- **Clocks.**
  Each craft keeps its own clock,
  which runs at the rate that relativity gives it.
  The difference is slight within the solar system
  and becomes decisive only in interstellar travel.
- **Propellant and delta-v.**
  Every manoeuvre costs propellant by the rocket equation,
  and the interface shows each agent the delta-v remaining.
- **Heat.**
  A craft must reject its waste heat,
  and the radiators that reject it are a signature that others can see.
- **Light time.**
  Every message,
  order
  and sensor reading arrives late by its light time.
  The rule binds craft and instruments.
  It cannot bind the people behind them,
  who talk to one another outside the simulation
  and may act through several characters at once.
  The design therefore enforces light time on what it controls,
  namely what a craft senses,
  when an order reaches it
  and when a trade settles,
  so that knowing a thing early does not allow acting on it early.
  What agents learn outside the simulation remains a leak,
  and it is a declared limit on what their behaviour shows.
- **Slosh and structure.**
  Modelled where docking,
  landing
  or pointing need them,
  and sized out elsewhere.

### Equations for an Implementation

This subsection is a reference for implementers,
and a reader interested only in the argument can skip it.
The core above needs a small set of equations,
and an implementer needs them in one place.
An earlier article on this site works the manoeuvres an agent plans with numbers,
among them the Hohmann transfer,
plane changes
and the Oberth effect
[Orbital Manoeuvres][related_post_orbital_manoeuvres].
The equations below are the ones the simulation itself must integrate.

**Gravity and thrust.**
Each craft moves under the gravity of every massive body and its own thrust.
In an inertial frame,
with $\ddot{\mathbf{r}}\_{i}$ the acceleration of craft $i$,
$G$ the gravitational constant,
$m\_{j}$ and $\mathbf{r}\_{j}$ the mass and position of massive body $j$,
and $\mathbf{a}\_{\mathrm{T},i}$ the acceleration of its own thrust,

$$
\ddot{\mathbf{r}}_{i} = -G \sum_{j} m_{j} \frac{\mathbf{r}_{i} - \mathbf{r}_{j}}{\lvert \mathbf{r}_{i} - \mathbf{r}_{j} \rvert^{3}} + \mathbf{a}_{\mathrm{T},i}
\tag{21}
$$

[Battin 1999][book_battin_1999]
[Hughes 2007][agency_nasa_gmat_2007].
The sum runs over the planets and moons on their ephemerides,
so a craft feels every body at once,
and Lagrange points and perturbations appear unscripted.
Thrust consumes propellant.
With $\dot{m}$ the rate of change of the craft's mass
and $F$ the thrust,

$$
\dot{m} = -\frac{F}{I_{\mathrm{sp}}\, g_{0}}
\tag{22}
$$

An engine of 100 kilonewtons at a specific impulse of 450 seconds
burns about 22.7 kilograms of propellant each second.
Integrated over a burn,
this equation is the rocket equation above.

**Binding to a parent body.**
The same motion has a second form,
relative to one body,
the craft's parent.
With $\mathbf{r}$ the position of the craft relative to the parent,
$\mu\_{\mathrm{p}}$ the parent's gravitational parameter,
$\mu\_{k}$ and $\mathbf{r}\_{k}$ the gravitational parameter of another body $k$ and its position relative to the parent,
and $\mathbf{a}\_{\mathrm{T}}$ the acceleration of thrust,

$$
\ddot{\mathbf{r}} = -\frac{\mu_{\mathrm{p}}}{\lvert \mathbf{r} \rvert^{3}}\, \mathbf{r} + \sum_{k} \mu_{k} \left( \frac{\mathbf{r}_{k} - \mathbf{r}}{\lvert \mathbf{r}_{k} - \mathbf{r} \rvert^{3}} - \frac{\mathbf{r}_{k}}{\lvert \mathbf{r}_{k} \rvert^{3}} \right) + \mathbf{a}_{\mathrm{T}}
\tag{23}
$$

[Hughes 2007][agency_nasa_gmat_2007].
The first term in the bracket is the pull of body $k$ on the craft.
The second is its pull on the parent,
which the equation needs because,
as one account puts it,
"the integration frame, which has its origin at the center of mass of the primary body, is not inertial"
[Berry and Coppola 2007][research_berry_coppola_2007].
The two terms nearly cancel,
and what remains is a tide.
For a craft at distance $r$ from its parent
and a third body at the much greater distance $d$,
the bracket is at most about $2 \mu\_{k} r / d^{3}$.
A craft at the height of the space station feels 8.64 metres per second squared from Earth.
With NASA's values for the other bodies
[NASA Moon Fact Sheet][agency_nasa_moon_fact_sheet]
[NASA Sun Fact Sheet][agency_nasa_sun_fact_sheet]
[NASA Jupiter Fact Sheet][agency_nasa_jupiter_fact_sheet],
the Moon adds at most about $1.2 \times 10^{-6}$ metres per second squared,
the Sun about $5.4 \times 10^{-7}$,
and Jupiter at its nearest about $8 \times 10^{-12}$.
Those are about 1.4 parts in ten million of Earth's pull,
0.6 parts in ten million
and one part in a trillion.
A simulation that keeps every perturbation above one part in a billion
gives that craft three bodies to feel and not thirty,
and the threshold is a declared omission of known size.
The tidal bound is this article's approximation,
good to first order in the ratio of the two distances.

**The step.**
A symplectic method can advance the equations of motion of a coasting craft in fixed steps.
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
\tag{24}
$$

This second-order method is the base from which Yoshida built higher orders
[Yoshida 1990][research_yoshida_1990].
For a craft coasting about one dominant body,
its energy error stays bounded instead of drifting,
so the orbit does not slowly spiral in or out over a long simulation.
Hairer,
Lubich
and Wanner show the behaviour on the two-body problem,
where
"there are only small errors in the Hamiltonian along the numerical solution, but no drift"
[Hairer et al. 2003][research_hairer_et_al_2003].
The property has conditions.
It holds for a constant step,
and it bounds the error in energy,
not the error in position along the orbit.
Among moving planets a craft's energy is not constant even in exact physics,
which is what a gravity assist exploits,
so the result does not carry over unchanged.
A close flyby needs a shorter step than a cruise,
and a burn or a pass through air is not a conservative force.
Changing the step is itself a hazard,
since
"Adaptive step size control is difficult to combine with geometric numerical integration"
[Hairer and Söderlind 2005][research_hairer_soderlind_2005],
though the same authors give a reversible rule that keeps the long-term behaviour.
The choice of integrator is therefore open.
Whatever the choice,
every machine must apply the same rule for choosing steps,
and a later article in this series treats it.

**Determinism.**
A shared world does not strictly need a reproducible step.
One authoritative server can compute the world and tell every client the answer,
which is the simplest arrangement.
The blueprint asks for reproducibility anyway,
for two reasons.
A predictive simulation should be open to checking,
and a world that anyone can replay from its recorded inputs is.
And a planning tool that runs the same step as the world
forecasts exactly what the world will do,
for as long as no other agent intervenes.
The idea is old in networked simulation.
The developers of Age of Empires wrote in 2001 that
"the expectation was to run the exact same simulation on each machine,"
and that a recording of the commands could then replay a whole session
[Bettner and Terrano 2001][dev_bettner_terrano_2001].
With $\mathbf{x}\_{n}$ the full state of the world at step $n$,
$U\_{n}$ the set of agents' inputs committed for that step in an agreed order,
and $\Phi\_{\Delta t}$ the step function,

$$
\mathbf{x}_{n+1} = \Phi_{\Delta t}\!\left( \mathbf{x}_{n}, U_{n} \right)
\tag{25}
$$

Every machine that starts from the same state
and applies the same ordered inputs
reaches the same state,
provided the step function is exactly reproducible.
That proviso is the difficult one.
Floating-point arithmetic that a compiler may reorder or fuse
can make two machines disagree in the last bit,
and an n-body system amplifies the difference.
Monniaux's survey of the problem warns that
"The result of computations can actually depend on compilation options or compiler versions,"
and that
"one should not expect consistent behaviour of transcendental functions across libraries, processor manufacturers or models"
[Monniaux 2008][research_monniaux_2008].
The Age of Empires developers met the same thing in practice,
where
"very subtle differences would multiply over time"
An implementation therefore fixes the order of every operation,
including those inside library functions and across processor cores,
or uses fixed-point arithmetic for the state.
The requirement applies to the machines that compute the world.
It does not extend to the agents' own machines,
which must not hold what their sensors cannot see.
This equation is the article's statement of that requirement,
and a later article in this series treats it in detail.

**Attitude.**
Pointing is a separate problem from moving.
With $\mathbf{I}$ the craft's inertia tensor,
$\boldsymbol{\omega}$ its angular velocity
and $\boldsymbol{\tau}$ the torque of its reaction control thrusters,
Euler's equations of rigid-body rotation give

$$
\mathbf{I}\, \dot{\boldsymbol{\omega}} + \boldsymbol{\omega} \times \left( \mathbf{I}\, \boldsymbol{\omega} \right) = \boldsymbol{\tau}
\tag{26}
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
\tag{27}
$$

and a simple model of the density,
with $\rho\_{0}$ its value at sea level,
about 1.225 kilograms per cubic metre,
and $H$ the scale height,
about 8.5 kilometres,
is

$$
\rho(h) = \rho_{0}\, e^{-h/H}
\tag{28}
$$

Heating at the nose follows the stagnation-point correlation of Sutton and Graves
[Sutton and Graves 1971][research_sutton_graves_1971].
With $\dot{q}$ the heat flux,
$r\_{\mathrm{n}}$ the radius of the nose
and $k$ a constant for the atmosphere,
about $1.74 \times 10^{-4}$ in units that give watts per square metre for Earth's air,

$$
\dot{q} = k \sqrt{\frac{\rho}{r_{\mathrm{n}}}}\, v^{3}
\tag{29}
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
\tag{30}
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
\tag{31}
$$

Under a thrust of a tenth of standard gravity,
a one-metre pendulum swings at about one radian per second,
a period of about six seconds,
slow enough to couple into a docking manoeuvre.
In a coasting craft the acceleration is nearly zero,
the restoring force vanishes,
and the liquid wanders.
Hence a small ullage thrust settles it before an engine starts.

**Clocks.**
A clock on a moving craft does not keep the time of a clock at home.
With $t\_{\mathrm{c}}$ the time a craft's own clock shows,
$t$ the time of a clock at rest far from every mass,
$\Phi$ the Newtonian gravitational potential at the craft,
which is negative,
$v$ the craft's speed
and $c$ the speed of light,
the weak-field result that satellite navigation relies on is

$$
\frac{d t_{\mathrm{c}}}{d t} = 1 + \frac{\Phi}{c^{2}} - \frac{v^{2}}{2 c^{2}}
\tag{32}
$$

[Ashby 2003][research_ashby_2003].
Ashby writes it with the reference clock on Earth's surface,
and observes of the Global Positioning System,
GPS,
that without such corrections
"the system would not work."
NASA puts numbers on it.
Uncorrected,
"GPS satellite clocks would gain ~38 microseconds per day relative to clocks on the ground (~11 km range error)"
[Winternitz 2017][agency_nasa_winternitz_2017].
The speed term alone,
at an interplanetary 30 kilometres per second,
is five parts in a billion,
about a sixth of a second in a year.
A crew would never notice that,
and a navigator cannot ignore it.
The simulation therefore keeps a clock for each craft.
The cost is one line in the step,
and the alternative,
clocks that all agree whatever their speed,
is a small contradiction of the kind the first principle forbids.

### Time

Travel takes its true time,
and the simulation gives that time a job.
A time warp chosen by one agent cannot be shared,
since one agent's acceleration of time would move every other agent's world.
A shared clock may still run fast,
provided it runs fast for everyone.
With $t\_{\mathrm{w}}$ the wall-clock time an agent waits,
$t\_{\mathrm{s}}$ the simulated time that passes
and $\kappa$ the compression factor shared by every agent,

$$
t_{\mathrm{w}} = \frac{t_{\mathrm{s}}}{\kappa}
\tag{33}
$$

The same factor shortens everything.
The table applies it to four durations worked earlier in this article
and to one more,
a single orbit at the height of the space station,
which at 7.66 kilometres per second around a circle of radius 6,791 kilometres
takes about 93 minutes.

| Duration | True | Compressed by 10 | Compressed by 100 |
|---|---|---|---|
| The exchange of a straight pass in low orbit | 13 seconds | 1.3 seconds | 0.13 seconds |
| The longest one-way light time to Mars | 22 minutes | 2.2 minutes | 13 seconds |
| One orbit at the height of the space station | 93 minutes | 9.3 minutes | 56 seconds |
| The Hohmann transfer to Mars | 259 days | 26 days | 2.6 days |
| The synodic period of Earth and Mars | 780 days | 78 days | 7.8 days |

No single compression suits both the voyage and the engagement.
At one hundred the voyage becomes bearable,
and the exchange becomes too short for any person to act in.

Compression also has a cost that is easy to miss.
It keeps every ratio between physical durations,
so the physics stays true,
but it does not compress the agents.
A person needs the same seconds to read a display and decide,
whatever the clock does.
At a compression of one hundred,
the light time to Mars shrinks from a wait that reshapes command
to a pause shorter than a sentence,
and the delay that the catalogue's remedy imposes
all but disappears from the agents' experience.
Compression is therefore a change of parameter that leaves the physics intact
and still moves the simulation away from the conditions it means to predict.
The less of it a design needs,
the more its agents' behaviour is worth as evidence.
The blueprint does not fix the factor.
It states a preference,
the lowest compression its agents will tolerate,
and leaves the value to trial.
The rest of this section addresses that tension.
The inference drawn here is that a shared world needs a shared clock,
compressed by the same factor for everyone,
and agents who plan and commit manoeuvres in advance
and then do something else while the plan executes.
That is how real spaceflight operates,
and it is the tempo Children of a Dead Earth discovered,
long waits followed by short decisive exchanges.
A private timeline of the kind the Kerbal Space Program multi-agent modifications use
is a workable compromise when agents must act alone,
and a later article in this series compares the two.

Travel that takes its true time in the lives of the participants is not a new idea.
In the tabletop role-playing game Traveller,
a starship that jumps between stars
"always stays in Jump Space for roughly one week"
[Traveller System Reference Document][ref_traveller_srd],
and the author recalls overhearing the notion of running that game in real time,
so that a journey from one world to the next takes a week of the participants' lives.

Long journeys change what an agent is.
Under any compression a design can afford,
a transfer to Mars still takes days or weeks of an agent's real time.
Relativistic time dilation is nominally relevant as well,
though it is chiefly a concern of interstellar travel.
At the speeds of near-term spaceflight it amounts to a fraction of a second in a year,
as the clock equation above shows.
At a tenth of the speed of light a traveller's clock would lose about 1.8 days in every year,
and at higher speeds a character in transit would live through less time than the world it left.
Conclusions about colonisation,
exploration
and exploitation that reach to the stars must reckon with it.

An agent has two ways to live with a long journey.
One is to act through several characters,
one in transit while another works at the destination.
A character can leave earlier
and arrive shortly before the role it is to fill begins,
much as a real programme sends a crew ahead of a mission.
The other is simply to attend to real life while the journey runs.
Balancing life against a high-commitment simulation is a problem its dedicated agents already face,
and some welcome an escape valve built into the design.
An agent who expects to be away has good reason to begin a long voyage first,
so that the absence costs nothing.
That is a matter of the agent's own management of time,
outside the simulation.
Inside it,
the effect is a population of individuals who set out for distant places
for reasons the simulation never sees.
That is a fair model of people who travel far out of restlessness
or for causes of their own.

A world that runs around the clock also imposes a schedule.
EVE Online's agents,
as a class,
already work to taxing schedules across time zones
when an event matters,
even though no individual can attend every pivotal development.
Any high-fidelity simulation that runs continuously
may subject its agents to the same realities,
inconvenient as they are.
The brief exchange of a pass between two fleets
happens when the orbits say it happens,
which may be the middle of the night on a Tuesday
or the middle of an important meeting.
Agents must then balance their real lives against their obligations in the simulation,
and that balance is itself a kind of stake.
Two answers follow.
Agents may need to find other stakeholders who can cover the inconvenient shifts,
as an organisation with members in several time zones does.
Run around the clock,
a single simulated spaceship may need three shifts of real people,
as a real ship at sea or a mission control room does.
That sounds absurd to anyone who would never touch such a simulation,
and it is exactly what its most committed agents would organise.
Or the simulation may need a mechanism to resolve events from orders committed in advance.
The mechanism has two forms,
and each has a cost.
In the first,
the event still happens when the orbits say,
and the craft acts on standing orders with nobody at the controls.
That keeps the shared present
and takes the person out of the moment,
so it yields evidence of how people plan
and none of how they act under fire.
In the second,
the simulation computes the outcome early for craft whose agents have all committed,
which locks those craft from that moment
and is a private timeline of the kind the Kerbal Space Program modifications use.
Neither form moves an event.
What an agent can choose,
at the time of planning,
is a trajectory whose decisive moment falls within waking hours.
Committed orders suit the physics,
since a transfer planned in advance is how real spaceflight already works.

True scale brings one more difficulty that this article only names.
Under honest delta-v budgets,
two craft come within reach of each other
only when one of them pays to cross the other's path at the right moment,
so encounters are rare.
The western's problem returns.
Adventures need agents in the same place at the same time,
and honest physics makes that expensive.
Meetings would concentrate where traffic must pass,
in low orbits,
at stations
and in the weeks around a transfer window.
Whether that is enough to sustain a shared world is open,
and a later article in this series takes it up.

This is where the thesis is most at risk,
and the article should say so plainly.
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
  so the simulation bounds their interactions and does not simulate them.
  As in Star Citizen,
  a crew may fly a ship,
  and the roles are asymmetric,
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

EVE Online shows that agents will build and run a supply chain that spans a world.
The blueprint keeps that and puts physics under it.
Delta-v prices freight.
With $m\_{\mathrm{p}}$ the propellant needed,
$m\_{\mathrm{pay}}$ the payload,
$m\_{\mathrm{s}}$ the structure and engines that make the trip with it,
and the other symbols as in the rocket equation,

$$
m_{\mathrm{p}} = \left( m_{\mathrm{pay}} + m_{\mathrm{s}} \right) \left( e^{\Delta v / \left( I_{\mathrm{sp}}\, g_{0} \right)} - 1 \right)
\tag{34}
$$

At a specific impulse of 450 seconds,
a delta-v of 4 kilometres per second
needs about 1.5 kilograms of propellant for every kilogram that makes the trip.
Geography becomes orbital mechanics.
A cheap route is a low delta-v route,
and the synodic period above opens the cheapest route to Mars once every 26 months,
so an honest economy would have trading seasons,
with prices rising and falling as windows open and close.
Prices inside the simulation would also travel at the speed of light.
A quote from another planet is minutes old when it arrives,
so a trader there acts on the past.
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
because evidence nobody can check is not evidence.
Openness and light time pull against each other,
since a public feed of every market would let agents see prices before the light arrives.
The simulation must therefore publish its record late,
by at least the longest light time in the world,
or after the fact.

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
In one shared world,
agents cannot each choose their own physics,
as Kerbal Space Program's modifications allow a single agent to do.
What each agent chooses is how much of the one model to handle by hand.
The planning tool may think in patched conics,
which are accurate enough for a first plan,
as the review above noted,
provided it then shows the correction that the full model makes.
The tool can be simple while the world stays true.

Layered disclosure has a cost in a shared world that it does not have in a sandbox.
A beginner who relies on the planning tool
competes with experts who edit every burn,
and by the fourth principle what the beginner loses stays lost.
The account of the meta above predicts who wins.
The blueprint does not solve this.
It records it as an open problem of design,
in which approachability and lasting loss pull against each other.
Kerbal Space Program's sales and its use in schools suggest
that the public will take up planning tools of this kind,
though a search found no measurement of what its users learn.
An autopilot that obeys physics is an approachability tool.
A warp drive that disobeys it is miseducation.

### Predictive Value

People adapt their behaviour to conditions.
If the conditions of a simulation are those of real near-term space,
the agents' adaptation to them is evidence about how people would behave there,
in markets,
in logistics
and in conflict.

The idea is not new,
and research on virtual worlds supports it with conditions.
Castronova and colleagues tested whether aggregate economic behaviour maps from the real world to a virtual one,
using the transaction records of a large commercial virtual world,
and reported that
"virtual economic behavior follows real-world patterns"
[Castronova et al. 2009][research_castronova_et_al_2009].
They also found the virtual economy less stable than a real one,
and wrote that
"virtual economies are not perfect analogs of real economies at the aggregate level."
Two epidemiologists made a similar argument after
"the accidental inclusion of a disease-like phenomenon"
in an online virtual world,
proposing that such worlds could help to validate epidemic models
and supply what they lack,
namely
"important human behaviours"
[Lofgren and Fefferman 2007][research_lofgren_fefferman_2007].
Williams named the condition on which all such work depends,
a
"mapping principle,"
defined as
"the extent to which behaviors in one space are consistent with behaviors in another"
[Williams 2010][research_williams_2010].
Williams is also the sharpest critic of the idea.
The same paper counts the epidemic study among those that
"took the mapping principle on faith"
and warns that
"the risks and rewards of virtual worlds do not always map to those offline. The most obvious example is pain and death."
None of that work concerns spaceflight.
It supports the general claim that behaviour in a simulated world can map to behaviour in the real one,
and it insists that researchers show the mapping and not assume it.
The three bounds that follow are this article's account of what the mapping depends on.

The mechanism deserves stating outright.
A sufficiently high-fidelity multi-agent simulation should have significant predictive value
because its agents are subject to the same incentives and constraints that reality imposes.
People who face the same costs,
the same delays
and the same scarcities tend toward the same choices,
whoever they are.
The history of wargaming offers an example.
Between the world wars the United States Naval War College gamed a war against Japan,
with its own students taking the Japanese side.
A historian of those games observes that
"The fact that the Japanese players used tactics in games resembling those they actually used during the Pacific War demonstrates that circumstances rather than some form of perceived Japanese military culture determined much of what they did"
[Friedman 2017][book_friedman_2017].
The students behaved as the Japanese later did
because they stood where the Japanese later stood.
The claim hinges on the scenario.
The incentives and constraints of the simulation must be close enough to those of real prospective problems.
Where they are not,
the agents adapt just as faithfully to the wrong conditions.
Predictive value is therefore largely a function of two abilities,
to formulate a realistic scenario
and to find agents willing to take part in exploring it.
The first is the work of fidelity and the second of approachability,
which is why the bounds below begin with those two.
The same demands hold outside the armed forces.
Herman,
Frost
and Kurz describe wargames designed and staged for the United States Army,
for global corporations
and for nonprofit groups
[Herman et al. 2009][book_herman_et_al_2009],
and the author's reading of such accounts is that a wargame is only as good as its scenario
and the people who come to it.

The competence of the agents matters less than it might seem.
Most people are of average ability for their station.
That holds for the participants in a wargame,
and it holds for the people who occupy the real stations that the wargame simulates.
People of clearly less than average ability take part in simulations too,
and such people also hold real stations.
Brilliant people are few,
in a simulation as in the world,
and their scarcity matters little,
because circumstance and station drive a great many decisions whoever makes them.
An agent needs only enough competence to do something reasonable,
and a competent person of less than average ability asks for advice.
The games at Newport bear this out.
Their participants were the officers who went on to hold the commands they had gamed.
The same historian records that
"Of the flag officers commanding combat formations in the 1941 fleet, only one had not attended the War College"
[Friedman 2017][book_friedman_2017].
They were average for their station in the plainest sense,
since they were the people who filled it.
Fleet Admiral Nimitz told the college in 1960 that
"the war with Japan had been re-enacted in the game rooms here"
"in so many different ways that nothing that happened during the war was a surprise"
except the kamikaze
[Hattendorf 2014][ref_hattendorf_2014].
Research on forecasting points the same way.
Green and Armstrong compared forecasts of the decisions made in real conflicts and found that
"The forecasts of experts who used their unaided judgment were little better than those of novices."
A form of role playing did far better.
It reduced error by 47 percent against the forecasts of game-theory experts,
and its participants
"were mostly undergraduate students"
[Green and Armstrong 2007][research_green_armstrong_2007].
Armstrong's review of role playing drew the same lesson about who takes each role,
that
"the little evidence available suggests that casting is not critical"
[Armstrong 2001][research_armstrong_2001].
That research concerns small groups acting out a single decision,
not a wargame,
and the profession of wargaming itself warns against the word predict.
An article in the college's own review holds that
"a war game can never be truly predictive"
and that what a game teaches,
"being merely indicative in itself, must be combined with judgment in order to have useful predictive value"
[Rubel 2006][research_rubel_2006].
A history of the method from the college's own press concludes that
"the large majority of games do not correlate to later events"
[Caffrey 2019][book_caffrey_2019].
The author's claim is the narrower one that this record supports.
Participants of average ability for their station,
placed under realistic incentives and constraints,
have produced conclusions with surprising predictive potential,
and the result depends on the scenario far more than on the talent in the room.

Wargaming also names the two practical problems that such a simulation would face.
The first is getting the stakeholders who would most benefit to take part.
Perla and McGrady hold that a game's effect on
"key decision makers"
is an essential source of an organisation's adaptation
[Perla and McGrady 2011][research_perla_mcgrady_2011],
yet
"Blue players are typically junior to the individuals who will make the actual decisions"
[Caffrey 2019][book_caffrey_2019].
The second is the reflex to wave away a result that nobody expected.
Rubel calls such results whispers,
"tempting to dismiss"
though they are,
and holds that
"these whispers are frequently the most important outcomes of war gaming."
The Japanese games before Midway are the standard case.
The part usually told is an umpire's reversal of a lucky hit,
and Rubel judges that ruling justified.
The failure lay elsewhere.
Someone asked what would happen if an American carrier force ambushed the Japanese carriers,
and
"that uncomfortable question seems to have been ignored"
[Rubel 2006][research_rubel_2006].
Sixty years later the United States did much the same in its Millennium Challenge exercise.
The official report records that the free play of the opposing force
"was eventually constrained to the point where the end state was scripted"
[Joint Forces Command][ref_jfcom_mc02],
and the general who led that force recalled that
"A phrase I heard over and over was: 'That would never have happened,'"
[The Guardian 2002][news_guardian_mc02_2002].

A simulation of the kind proposed here inherits both problems.
Those with the most to learn from it,
the agencies,
firms
and investors who will make the real decisions,
are the least likely to spend their evenings in it.
And its most valuable results will be the ones that look wrong.
A blockade that fails,
a market that seizes
or a colony that its own agents abandon
will invite the verdict that the simulation is unrealistic,
when the purpose of building it was to find out.

The first of the three bounds is fidelity,
because agents adapt to the model and not to reality,
which is what Children of a Dead Earth's meta shows.
Castronova and colleagues reached the same caution from the other side,
suggesting that
"macroeconomic outcomes in a virtual world may be explained largely by design structure."
Fidelity includes the scenario.
A simulation must posit technologies,
prices
and starting conditions that the real future will not copy,
and whatever it yields is conditional on them.
Time compression belongs under this bound too,
for the reason the [Time](#time) section gave.
The second is approachability,
because a model only an expert can use
yields the behaviour of a small and unrepresentative population of experts.
The time design above pulls against this bound,
since agents who organise three shifts for one ship
are a small and unrepresentative population of another kind.
The third is incentives.
An agent who risks nothing it values has no reason to behave as it would where the stakes are real.
Wargamers know the effect,
and Rubel notes that
"players tend to be more aggressive than they would be in the real world with real lives at stake"

EVE Online shows that a simulation can meet this bound.
Some of its agents take it more seriously than their real jobs,
and a saying among them holds that internet spaceships are more fun than work.
People who defend a ledger of fantasy wealth that fiercely
are displaying the incentive feedback that a predictive simulation needs,
even if the enthusiasm is questionably placed.
The mechanism is on record above.
A destroyed ship is gone,
and the exchange rate puts a price in real money on what its owner lost.
The author has placed significant effort in the EVE Online sandbox,
questionably,
despite being a fairly tempered participant.

The same case shows what high commitment brings with it.
A multi-agent simulation that people take seriously
can hold its agents to wildly high expectations,
and skills pass between it and real life in both directions,
as the review above recorded.
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
which is how terrible parts produce tax havens and embezzlement.
It is an inference that predictive value has two sources,
the fidelity of the parts and the completeness of their interlock.
Interlock is not a fourth bound.
It is the first bound seen at the level of the system,
since the couplings between the parts are themselves part of the model.
EVE Online is strong in the second source and weak in the first,
and Children of a Dead Earth the reverse.

One caution applies to the whole case.
What EVE Online has demonstrated is reproduction.
Behaviour known from real economies reappeared in it,
and nobody designed it.
A model that reproduces known behaviour unprompted
has passed the first test of a predictive model.
It has not yet made a prediction that was later confirmed,
and neither has anything proposed here.

That raises an obvious question.
If EVE Online reproduces real behaviour without honest physics,
why does physics matter at all?
The answer is that predictive value extends only to the conditions a simulation models.
EVE Online models an economy,
a polity
and a society of real people,
so its evidence concerns economic,
political
and social behaviour,
and there its fidelity is high,
because the market and the people are real.
It models no delta-v,
no light-time
and no launch windows,
so it gives no evidence of how people would behave under them.
A blockade that physics makes impossible,
a market that the synodic period opens and closes,
an order that arrives twenty minutes late,
and a war decided by who can afford the propellant to reach the battle
lie outside its scope,
however good its economy.
A simulation for near-term space needs EVE Online's interlock
and honest physics together,
because the questions it exists to answer are the ones the physics shapes.

One limit lies outside the design altogether.
The agents of any such simulation are volunteers with leisure.
The actors of real near-term space are states,
firms
and crews,
who act under law and at mortal risk.
The simulation could show how people adapt to physical and economic conditions.
It could not show what institutions would permit.

A simulation that maximises one bound at the expense of the others
predicts poorly outside the conditions it happens to model well.
The blueprint's principles exist to raise all three together.
The same tension appears in the published wargames reviewed elsewhere on this site,
whose value depends on how faithfully their rules capture the conditions they model
[Published Wargames][related_post_published_wargames].

### Market Demand

The thesis holds that there is market demand for such a simulation,
and the reviewed products support the claim only indirectly.
Kerbal Space Program sold more than five million units
[Take-Two 2023][dev_take_two_ksp2_2023].
EVE Online passed half a million subscribers in one shared world in 2013
[CCP 2013][dev_ccp_subscribers_2013].
Star Citizen's counter shows about a billion dollars raised before release
[RSI Crowdfund Statistics][dev_rsi_crowdfund_stats].
The public pays for spaceflight,
for shared worlds
and for both together.
It is an inference that it would pay for both with honest physics.
The inference is the weakest link in the thesis,
and two objections need stating.
The audiences of EVE Online and Star Citizen may be paying for exactly the conveniences that honest physics removes,
so nobody can simply add their numbers to Kerbal Space Program's.
And the one known attempt to put many agents on the textbook core in a product for the public,
Kerbal Space Program 2,
lost its studio before it delivered its multi-agent mode.
That closure shows a failure of execution.
It cannot show an absence of demand,
since the product that would have tested the demand never shipped,
and it cannot show its presence either.
The claim therefore stands as an inference that no product has yet tested.
It is the market half of the thesis,
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
The main ones are Kerbal Space Program's scale
and the account of how its multi-agent modifications handle time,
EVE Online's velocity law,
its warp speeds and its capacitor,
the base broker's fee in EVE Online,
the reception of Kerbal Space Program 2,
the 2009 bank embezzlement and the technetium cartel,
which rest on press reports and a participant's account,
and the controversy around Star Citizen,
which rests on press reports of sentiment.
Two facts rest on a community wiki and on the author's own observation together.
The author has watched EVE Online's ships slow to rest,
and recalls noting that Star Citizen's celestial bodies were not subject to celestial mechanics.
Star Citizen's crowdfunding total comes from the developer's own counter,
whose units this article infers to be cents.
The Cloud Imperium incomes for 2020 to 2022 and all five spending ratios are sums and quotients of stated figures.
The survey on transferable skills appeared in an article sponsored by the developer.
The Star Trek line about tritanium is from the episode as aired,
located through a fan transcript.
Of the studies of fiction,
misconception
and virtual worlds,
this article cites two from their abstracts alone,
Clement 1982 and Lofgren and Fefferman 2007.
The summary of Clement's finding,
that motion implies a force,
comes from a later review.
The equation of motion relative to a parent body comes from a NASA specification
whose scanned text the research for this article read from page images.
That participants in wargames are of average ability for their station is the author's argument.
Its support here is the record that the Newport participants went on to hold the commands they had gamed,
and research on role playing by students,
which is not wargaming.
The account of Herman,
Frost
and Kurz rests on the catalogue record of their book and on the author's memory of reading it,
since neither the author nor the research for this article had its text to hand.
That people have run Traveller in real time rests on a remark the author overheard in person
and recalls imperfectly,
which no source here supports.
The physics of each remedy comes from NASA,
ESA,
the Fédération Aéronautique Internationale,
textbooks
or peer-reviewed work,
with three exceptions named in the text
and a few statements that follow from first principles and carry no citation.
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
the judgement that Kerbal Space Program 2 was mismanaged,
the training of writers as a cause of the soft science fiction conventions,
the judgement that Star Citizen aspires to a higher-fidelity version of EVE Online's thesis and is directionally promising,
the judgement that its sales model is grey and that its project is mismanaged,
the judgement that EVE Online's economy is the best multi-agent supply chain known,
that its wrong models have the right fidelity for interaction,
and the conjecture that the developer lacked the people to distil more realistic models,
the characterisation of EVE Online's most committed agents,
their scheduling across time zones,
the transfer of skills
and burnout,
the estimate of what the gravity model costs to compute,
the tidal bound on a third body's perturbation,
the claim that ability average for a station suffices for agents,
the view that predictive value is largely a matter of realistic scenarios and willing agents,
and the blueprint.
The author offers these as judgements,
open to disagreement on the evidence.
The author discloses an interest in one of the products,
having participated in the EVE Online sandbox.

**Inferences.**
This article infers from the format
that warp drive served Star Trek's production as the transporter did,
since no primary source says it.
It infers that the two multi-agent products took their conventions from film and television
from the resemblance,
from Star Citizen's stated aim
and from one borrowed name.
It infers the product thesis it attributes to EVE Online from the developer's descriptions.
That an agent who flies for years under a model that contradicts inertia
is practising a misconception,
that time compression moves a simulation away from the conditions it means to predict,
that a shared world needs a shared clock,
that layered disclosure resolves the conflict between fidelity and approachability,
that several characters per agent would make long journeys workable,
that resolution of events from committed orders would ease scheduling across time zones,
that predictive value has two sources, the fidelity of the parts and the completeness of their interlock,
that predictive value extends only to the conditions a simulation models,
that an honest economy would have trading seasons
and prices that travel at the speed of light,
and that the public would pay for honest physics
are inferences.
The last is the weakest,
and no product has tested it.
That research on role playing by small groups carries over to a simulation of thousands
is an inference,
and so is the reading of voyages begun before an absence
as a model of individuals who travel for private reasons.
This reconstruction names incentives as a third bound on predictive value.
The author regards the reasoning behind it,
that agents under the same incentives and constraints behave as real stakeholders would,
as part of the thesis.
The eleven equations that the Equations section marks as bespoke are constructions of this article,
and the engagement-time,
radiator
and gravity-cost equations among them show orders of magnitude only.
What EVE Online has demonstrated is reproduction of known behaviour,
not a prediction later confirmed,
and the miseducation this article warns of is a hypothesis with indirect support.

**The reconstruction.**
The author reconstructed the thesis from memory.
Where this article's wording differs from the paper's,
nobody can consult the paper to settle it.
The books the paper drew on stand on a shelf the author cannot reach,
and the notes went with the paper,
so most of its original sources go uncited here.
This article reviews the products as they stand in November 2026,
not as they stood when the author wrote the paper,
which,
as far as the author recalls,
leaves the conclusions unchanged.

## Out of Scope

- **Developments since the paper.**
  Research harnesses that put many automated agents into Kerbal Space Program and into high-fidelity satellite simulators,
  and language models tested as spacecraft operators,
  are the subject of the next article in this series.
- **The hard problems in detail.**
  This article names shared time,
  the rarity of encounters under honest delta-v budgets,
  and deterministic networked physics,
  and a later article works them.
- **Other products.**
  The paper's list held other simulations that it never reviewed for lack of time.
  This article does not review Orbiter,
  Elite Dangerous,
  Space Engineers
  or the others either,
  so it states the third claim as none known.
- **Hands-on testing.**
  The reviews rest on the developers' public statements,
  on first principles
  and,
  where the text says so,
  on the author's earlier experience of the products,
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
have poor physical models shared with film and television,
in which,
between them,
ships coast to a stop,
travel takes almost no time,
gravity has no mechanism
and planets,
on the evidence found,
do not orbit.
None of these products has failed.
Each expresses its own thesis under its own constraints,
and EVE Online in particular shows that a real economy of real agents
can make the sum greater than the parts.

What no known product offers is the combination,
a single shared world of many agents
under physics that does not cheat,
made approachable by tools rather than by fiction.
No obstacle in physics or computation is known.
The open problems are of design,
and true travel times are the hardest of them.
Whether it would pay is another question.
People adapt to the conditions they are given,
and agents in such a simulation would face the incentives and constraints of real space,
so it should yield evidence
of how people would behave under the conditions it models,
more a source of tested hypotheses than a forecast,
bounded by its fidelity,
by how many people can use it,
and by how much its agents care.
How much it yields depends chiefly on whether its builders can formulate realistic scenarios
and whether agents are willing to explore them.
The public has shown that it will pay for spaceflight and for shared worlds.
A simulation that gave it both,
truthfully,
would also teach it,
and through the loop between science fiction and science,
the children it taught might help to build the future it depicted.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 34 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 34, 23 are established and 11 are bespoke.
Each equation takes the units its section states. Distances are in kilometres unless the section says otherwise, the worked numbers are rounded to the precision of their inputs, and several letters are reused, each defined where it appears. The letter a is a semi-major axis in Equations 2 and 3 and an acceleration in Equation 31, T is a sidereal day in Equation 14 and a temperature in Equations 18 and 30, R is a weapon range in Equation 4 and the radius of Earth in Equation 16, the Greek letter tau is a time constant in Equation 5 and a torque in Equation 26, the Greek letter rho is a ratio of spending to income in Equation 10 and the density of air in Equations 27 to 29, and the capital Greek letter phi is a step function in Equation 25 and a gravitational potential in Equation 32.

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

*Equation 10, Bespoke Ratio of Spending to Income.*
The ratio of a company's costs including capital expenditure to its income in one year, used to test whether Cloud Imperium spends what it raises.
[Cloud Imperium 2023][dev_cig_financials_2023]

$$
\rho_{y} = \frac{C_{y}}{R_{y}}
\tag{10}
$$

**Equation 11, Tsiolkovsky Rocket Equation.**
The delta-v a rocket gains as its mass falls from the initial to the final mass.

$$
\Delta v = I_{\mathrm{sp}}\, g_{0} \ln \frac{m_{0}}{m_{\mathrm{f}}}
\tag{11}
$$

**Equation 12, Hohmann Transfer Time.**
Half the period of the transfer ellipse, the time the cheapest two-burn transfer between two coplanar circular orbits takes.
[Curtis 2020a][book_curtis_2020_interplanetary]

$$
t_{\mathrm{H}} = \pi \sqrt{\frac{a_{\mathrm{t}}^{3}}{\mu_{\odot}}}
\tag{12}
$$

**Equation 13, Synodic Period.**
The interval between repetitions of two planets' relative position, which spaces the windows for a transfer.
[Curtis 2020a][book_curtis_2020_interplanetary]

$$
\frac{1}{S} = \frac{1}{T_{1}} - \frac{1}{T_{2}}
\tag{13}
$$

**Equation 14, Geostationary Orbit Radius.**
The radius at which a circular orbit's period equals one sidereal day, the only place a satellite holds position over the ground.
[ESA 2020][agency_esa_geo_2020]

$$
r_{\mathrm{G}} = \left( \frac{\mu T^{2}}{4 \pi^{2}} \right)^{1/3}
\tag{14}
$$

**Equation 15, Circular Orbital Speed.**
The speed of a circular orbit at a given radius, which is what makes reaching orbit hard.

$$
v_{\mathrm{c}} = \sqrt{\frac{\mu}{r}}
\tag{15}
$$

**Equation 16, Gravity at Altitude.**
The inverse-square fall of gravity with height, which leaves about nine-tenths of surface gravity at the space station.
[NASA 2012][agency_nasa_microgravity]

$$
g(h) = g_{0} \left( \frac{R}{R + h} \right)^{2}
\tag{16}
$$

**Equation 17, Centripetal Acceleration.**
The acceleration felt at the rim of a rotating habitat, the physical basis of spin gravity.
[Johnson and Holbrow 1977][agency_nasa_sp413_1977]

$$
a_{\mathrm{c}} = \omega^{2} r
\tag{17}
$$

*Equation 18, Bespoke Radiator Power Without Absorbed Sunlight.*
The Stefan-Boltzmann law applied to a radiator facing cold space with absorbed sunlight neglected, an assumption of the article's that lowers the area needed.

$$
P = \varepsilon \sigma A T^{4}
\tag{18}
$$

**Equation 19, Light-Time Delay.**
The one-way delay of any signal over a distance, which no message or sensor reading can beat.
[Landon et al. 2025][agency_nasa_tm_2025_mars_comms]

$$
t_{\mathrm{L}} = \frac{d}{c}
\tag{19}
$$

*Equation 20, Bespoke Cost of One Gravity Step.*
The time one processor core needs to advance every craft by one step, linear in the number of craft because craft do not attract one another, an order-of-magnitude estimate of the article's.
[Tanikawa et al. 2013][research_tanikawa_et_al_2013]

$$
t_{\mathrm{step}} = N_{\mathrm{c}}\, \bar{n}\, t_{\mathrm{f}}
\tag{20}
$$

**Equation 21, N-Body Equation of Motion With Thrust.**
The acceleration of a craft in an inertial frame under the gravity of every massive body plus its own thrust, the equation the core integrates.
[Battin 1999][book_battin_1999]
[Hughes 2007][agency_nasa_gmat_2007]

$$
\ddot{\mathbf{r}}_{i} = -G \sum_{j} m_{j} \frac{\mathbf{r}_{i} - \mathbf{r}_{j}}{\lvert \mathbf{r}_{i} - \mathbf{r}_{j} \rvert^{3}} + \mathbf{a}_{\mathrm{T},i}
\tag{21}
$$

**Equation 22, Propellant Mass Flow.**
The rate at which an engine of given thrust and specific impulse consumes propellant, which integrates to the rocket equation.

$$
\dot{m} = -\frac{F}{I_{\mathrm{sp}}\, g_{0}}
\tag{22}
$$

**Equation 23, Motion Relative to a Parent Body With Third-Body Terms.**
The acceleration of a craft in the frame of its parent body, where each other body enters as the difference between its pull on the craft and its pull on the parent.
[Hughes 2007][agency_nasa_gmat_2007]
[Berry and Coppola 2007][research_berry_coppola_2007]

$$
\ddot{\mathbf{r}} = -\frac{\mu_{\mathrm{p}}}{\lvert \mathbf{r} \rvert^{3}}\, \mathbf{r} + \sum_{k} \mu_{k} \left( \frac{\mathbf{r}_{k} - \mathbf{r}}{\lvert \mathbf{r}_{k} - \mathbf{r} \rvert^{3}} - \frac{\mathbf{r}_{k}}{\lvert \mathbf{r}_{k} \rvert^{3}} \right) + \mathbf{a}_{\mathrm{T}}
\tag{23}
$$

**Equation 24, Kick-Drift-Kick Leapfrog Step.**
The second-order symplectic step whose energy error stays bounded for a coasting craft at a constant step, the base of higher-order symplectic integrators.
[Yoshida 1990][research_yoshida_1990]
[Hairer et al. 2003][research_hairer_et_al_2003]

$$
\begin{aligned}
\mathbf{v}_{n+1/2} &= \mathbf{v}_{n} + \tfrac{\Delta t}{2}\, \mathbf{a}(\mathbf{r}_{n}) \\
\mathbf{r}_{n+1} &= \mathbf{r}_{n} + \Delta t\, \mathbf{v}_{n+1/2} \\
\mathbf{v}_{n+1} &= \mathbf{v}_{n+1/2} + \tfrac{\Delta t}{2}\, \mathbf{a}(\mathbf{r}_{n+1})
\end{aligned}
\tag{24}
$$

*Equation 25, Bespoke Reproducible State Transition.*
The shared world's state advanced by one deterministic step from the agents' ordered inputs, the article's statement of the requirement that the step be reproducible.

$$
\mathbf{x}_{n+1} = \Phi_{\Delta t}\!\left( \mathbf{x}_{n}, U_{n} \right)
\tag{25}
$$

**Equation 26, Euler's Equations of Rigid-Body Rotation.**
The change in a craft's angular velocity under the torque of its thrusters, which turns the craft without changing its path.

$$
\mathbf{I}\, \dot{\boldsymbol{\omega}} + \boldsymbol{\omega} \times \left( \mathbf{I}\, \boldsymbol{\omega} \right) = \boldsymbol{\tau}
\tag{26}
$$

**Equation 27, Aerodynamic Drag.**
The drag force on a body moving through air, which governs launch and reentry.

$$
F_{\mathrm{D}} = \tfrac{1}{2}\, \rho v^{2} C_{\mathrm{D}} A
\tag{27}
$$

**Equation 28, Isothermal Exponential Atmosphere.**
The simple model of air density falling exponentially with height above sea level.

$$
\rho(h) = \rho_{0}\, e^{-h/H}
\tag{28}
$$

**Equation 29, Sutton-Graves Stagnation-Point Heating.**
The convective heat flux at the nose of a vehicle entering an atmosphere, which falls as the nose grows blunter.
[Sutton and Graves 1971][research_sutton_graves_1971]

$$
\dot{q} = k \sqrt{\frac{\rho}{r_{\mathrm{n}}}}\, v^{3}
\tag{29}
$$

*Equation 30, Bespoke Lumped Thermal Balance.*
A single-node energy balance in which a craft heats when the power it gains exceeds what its radiators reject, an assumption of uniform temperature.

$$
m c\, \frac{dT}{dt} = P_{\mathrm{in}} - \varepsilon \sigma A T^{4}
\tag{30}
$$

**Equation 31, Pendulum Model of First-Mode Slosh.**
The natural frequency of the equivalent pendulum that represents a tank's first slosh mode under axial acceleration.
[Abramson 1966][research_abramson_1966]

$$
\omega_{\mathrm{s}} = \sqrt{\frac{a}{L}}
\tag{31}
$$

**Equation 32, Weak-Field Rate of a Moving Clock.**
The rate of a craft's clock against a distant clock at rest, slowed by the gravitational potential and by speed, to first order.
[Ashby 2003][research_ashby_2003]

$$
\frac{d t_{\mathrm{c}}}{d t} = 1 + \frac{\Phi}{c^{2}} - \frac{v^{2}}{2 c^{2}}
\tag{32}
$$

*Equation 33, Bespoke Wall-Clock Time Under a Shared Clock.*
The real time an agent waits for a span of simulated time when one compression factor applies to every agent.

$$
t_{\mathrm{w}} = \frac{t_{\mathrm{s}}}{\kappa}
\tag{33}
$$

*Equation 34, Bespoke Freight Propellant From the Rocket Equation.*
The propellant a shipment needs for a given delta-v, the rocket equation rearranged to price freight by delta-v in the blueprint's economy.

$$
m_{\mathrm{p}} = \left( m_{\mathrm{pay}} + m_{\mathrm{s}} \right) \left( e^{\Delta v / \left( I_{\mathrm{sp}}\, g_{0} \right)} - 1 \right)
\tag{34}
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
- $t_{\mathrm{step}}$, the time one processor core needs to advance every craft by one step
- $N_{\mathrm{c}}$, the number of craft
- $\bar{n}$, the mean number of bodies each craft feels
- $t_{\mathrm{f}}$, the time of one evaluation of the inverse-square law
- $\mu_{\mathrm{p}}$, the gravitational parameter of a craft's parent body
- $\mu_{k}$, the gravitational parameter of another body $k$
- $t_{\mathrm{c}}$, the time a craft's own clock shows
- $\Phi$, the Newtonian gravitational potential at a craft
- $c$, the speed of light
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
- $\rho_{y}$, the ratio of spending to income in year $y$
- $C_{y}$, the costs including capital expenditure in year $y$
- $R_{y}$, the income in year $y$
- $m_{\mathrm{p}}$, the propellant a shipment needs
- $m_{\mathrm{pay}}$, the payload of a shipment
- $m_{\mathrm{s}}$, the structure and engines that make the trip with the payload
- $t_{\mathrm{w}}$, the wall-clock time an agent waits
- $t_{\mathrm{s}}$, the simulated time that passes
- $\kappa$, the time compression factor shared by every agent

## References

- [Agency, Blevins and Hohmann 1975, Description of the Space Shuttle Reaction Control System][agency_nasa_shuttle_rcs_1975]
- [Agency, ESA 2020, Geostationary Orbit][agency_esa_geo_2020]
- [Agency, Hughes 2007, General Mission Analysis Tool Mathematical Specifications][agency_nasa_gmat_2007]
- [Agency, Johnson and Holbrow 1977, Space Settlements: A Design Study][agency_nasa_sp413_1977]
- [Agency, JPL 2020, JPL Planetary and Lunar Ephemerides][agency_jpl_ephemerides_2020]
- [Agency, Landon et al. 2025, Assessment of the State of Communication Delay Research][agency_nasa_tm_2025_mars_comms]
- [Agency, Launius and Jenkins 2012, Coming Home: Reentry and Recovery from Space][agency_nasa_coming_home]
- [Agency, Mesarch 2018, GDC Orbit Primer][agency_nasa_orbit_primer_2018]
- [Agency, NASA 2012, What Is Microgravity?][agency_nasa_microgravity]
- [Agency, NASA 2016, Gamers Tackle Virtual Asteroid Sampling Mission][agency_nasa_gamers_osiris_2016]
- [Agency, NASA 2017, Why Do We Really Need Pressure Suits?][agency_nasa_pressure_suits_2017]
- [Agency, NASA 2020, Space Communications: 7 Things You Need to Know][agency_nasa_space_comms_2020]
- [Agency, NASA 2021, NASA Laser Communications Innovations: A Timeline][agency_nasa_laser_comm_timeline_2021]
- [Agency, NASA 2024, 55 Years Ago: Star Trek Final Episode Airs][agency_nasa_star_trek_55_2024]
- [Agency, NASA Anatomy of an Electromagnetic Wave][agency_nasa_em_anatomy]
- [Agency, NASA Basics of Spaceflight, Trajectories][agency_nasa_bsf_trajectories]
- [Agency, NASA Black Holes][agency_nasa_black_holes]
- [Agency, NASA Dawn FAQ][agency_nasa_dawn_faq]
- [Agency, NASA Earth Fact Sheet][agency_nasa_earth_fact_sheet]
- [Agency, NASA ISS Active Thermal Control System Overview][agency_nasa_iss_atcs]
- [Agency, NASA Jupiter Fact Sheet][agency_nasa_jupiter_fact_sheet]
- [Agency, NASA Moon Fact Sheet][agency_nasa_moon_fact_sheet]
- [Agency, NASA Newton's Laws of Motion][agency_nasa_newton]
- [Agency, NASA Rocket Principles][agency_nasa_rocket_principles]
- [Agency, NASA Small Spacecraft Thermal Control][agency_nasa_smallsat_thermal]
- [Agency, NASA Sun Fact Sheet][agency_nasa_sun_fact_sheet]
- [Agency, NASA Webb Orbit][agency_nasa_webb_orbit]
- [Agency, NASA Whipple Shield Development][agency_nasa_whipple]
- [Agency, Riebeek 2009, Catalog of Earth Satellite Orbits][agency_nasa_orbit_catalog_2009]
- [Agency, Stysley 2011, Laser-Based Optical Trap for Remote Sampling][agency_nasa_niac_stysley_2011]
- [Agency, Westover et al. 2019, Magnet Architectures and Active Radiation Shielding Study][agency_nasa_maarss_2019]
- [Agency, Winternitz 2017, Introduction to GPS and Other Global Navigation Satellite Systems][agency_nasa_winternitz_2017]
- [Book, Battin 1999, An Introduction to the Mathematics and Methods of Astrodynamics][book_battin_1999]
- [Book, Caffrey 2019, On Wargaming][book_caffrey_2019]
- [Book, Conway Morris 2003, Life's Solution][book_conway_morris_2003]
- [Book, Curtis 2020a, Interplanetary Trajectories][book_curtis_2020_interplanetary]
- [Book, Friedman 2017, Winning a Future War: War Gaming and Victory in the Pacific War][book_friedman_2017]
- [Book, Glasstone 1964, The Effects of Nuclear Weapons, Revised Edition Reprinted February 1964][book_glasstone_1964]
- [Book, Hawking and Hawking 2007, George's Secret Key to the Universe][book_hawking_hawking_2007]
- [Book, Herman et al. 2009, Wargaming for Leaders: Strategic Decision Making from the Battlefield to the Boardroom][book_herman_et_al_2009]
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
- [Developer, Bettner and Terrano 2001, 1500 Archers on a 28.8: Network Programming in Age of Empires and Beyond][dev_bettner_terrano_2001]
- [Developer, CCP 2003, Highly Anticipated Massively Multiplayer Online Game][dev_ccp_launch_2003]
- [Developer, CCP 2006, A Deal Is a Deal][dev_ccp_faucets_2006]
- [Developer, CCP 2007, EVE Online Appoints In-World Economist][dev_ccp_economist_2007]
- [Developer, CCP 2007a, Econ Dev Blog No. 3, Some Statistics on Corporations][dev_ccp_corporations_2007]
- [Developer, CCP 2008, I Can Resist Anything but Temptation][dev_ccp_plex_2008]
- [Developer, CCP 2009, The Way of the PLEX][dev_ccp_plex_2009]
- [Developer, CCP 2009a, I Bring Gifts, by Gifts I Mean Taxes][dev_ccp_taxes_2009]
- [Developer, CCP 2010, Fixing Lag: Character Nodes][dev_ccp_character_nodes_2010]
- [Developer, CCP 2012, Price Indices, February 2012][dev_ccp_price_indices_2012]
- [Developer, CCP 2012a, Tech Is Fine, L2P][dev_ccp_technetium_2012]
- [Developer, CCP 2013, EVE Online Surpasses 500,000 Subscribers Worldwide][dev_ccp_subscribers_2013]
- [Developer, CCP 2013a, Warp Drive Active][dev_ccp_warp_2013]
- [Developer, CCP 2013b, Community Spotlight, Red Frog Freight][dev_ccp_red_frog_2013]
- [Developer, CCP 2014, EVE Industry, All You Want to Know][dev_ccp_industry_2014]
- [Developer, CCP 2014a, The Bloodbath of B-R5RB][dev_ccp_b_r5rb_2014]
- [Developer, CCP 2014b, HED-GP Technical Retrospective][dev_ccp_hed_gp_2014]
- [Developer, CCP 2015, EVE Economy Update, EVE Vegas 2015 Report][dev_ccp_economy_vegas_2015]
- [Developer, CCP 2016, Overlays, ISK Buyer Amnesty and Account Security][dev_ccp_rmt_2016]
- [Developer, CCP 2017, PLEX Changes on the Way][dev_ccp_plex_2017]
- [Developer, CCP 2019, Updates to Sales Taxes and Brokers Fees][dev_ccp_taxes_2019]
- [Developer, CCP 2020, Broker Relations][dev_ccp_broker_relations_2020]
- [Developer, CCP 2022, Team Security 2021 in Review][dev_ccp_security_2021]
- [Developer, CCP 2023, Viridian Expansion Notes][dev_ccp_viridian_2023]
- [Developer, CCP 2025, Patch Notes, Version 22.02][dev_ccp_patch_22_02_2025]
- [Developer, CCP 2026, Monthly Economic Report, August 2026][dev_ccp_mer_2026]
- [Developer, CCP, Capsuleers][dev_ccp_capsuleers]
- [Developer, CCP, EVE Swagger Interface Overview][dev_ccp_esi_overview]
- [Developer, CCP, Tritanium Item Record][dev_ccp_esi_tritanium]
- [Developer, CCP, Useful Formulae][dev_ccp_useful_formulae]
- [Developer, Children of a Dead Earth, Steam Store Page][dev_code_steam]
- [Developer, Cloud Imperium 2020, Cloud Imperium Financials for 2020][dev_cig_financials_2020]
- [Developer, Cloud Imperium 2021, Cloud Imperium Financials for 2021][dev_cig_financials_2021]
- [Developer, Cloud Imperium 2022, Cloud Imperium Financials for 2022][dev_cig_financials_2022]
- [Developer, Cloud Imperium 2023, Cloud Imperium Financials for 2023][dev_cig_financials_2023]
- [Developer, Cloud Imperium 2024, CFO Comment on the 2024 Accounting][dev_cig_financials_2024]
- [Developer, Dark Multiplayer][dev_dark_multiplayer]
- [Developer, Falanghe 2012, Patched Conics Trajectory from Initial Orbit State][dev_harvester_patched_conics_2012]
- [Developer, Kerbal Space Program 2, Steam Store Page][dev_ksp2_steam]
- [Developer, Kerbal Space Program, Steam Store Page][dev_ksp_steam]
- [Developer, KerbalEdu 2016][dev_kerbaledu_2016]
- [Developer, Luna Multiplayer][dev_luna_multiplayer]
- [Developer, Principia][dev_principia]
- [Developer, Principia, On the Dynamical Stability of Principia's Modified Jool System][dev_principia_jool]
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
- [Developer, RSI 2014, Into the Unknown, a Carrack and Her Crew][dev_rsi_carrack_2014]
- [Developer, RSI 2014, Lore Builder Twenty][dev_rsi_lore_gravity_2014]
- [Developer, RSI 2017, Star Citizen Alpha 3.0.0][dev_rsi_alpha_300_2017]
- [Developer, RSI 2017a, Star Citizen Alpha 3.0.0 Patch Notes][dev_rsi_patch_300_2017]
- [Developer, RSI 2018, The Shipyard: Fuel Mechanics][dev_rsi_fuel_2018]
- [Developer, RSI 2018a, Star Citizen Alpha 3.2.0 Patch Notes][dev_rsi_patch_320_2018]
- [Developer, RSI 2018b, Star Citizen Alpha 3.4.0 Patch Notes][dev_rsi_patch_340_2018]
- [Developer, RSI 2020, Flight and Fight Upcoming Improvements][dev_rsi_flight_2020]
- [Developer, RSI 2021, Deadly Consequences, Alpha 3.15][dev_rsi_alpha_315_2021]
- [Developer, RSI 2025, Star Citizen Alpha 4.5.0][dev_rsi_patch_450_2025]
- [Developer, RSI 2026, Terms of Service][dev_rsi_tos_2026]
- [Developer, RSI, Crowdfund Statistics][dev_rsi_crowdfund_stats]
- [Developer, RSI, Roadmap][dev_rsi_roadmap]
- [Developer, RSI, Star Citizen Alpha 4.0][dev_rsi_alpha_40]
- [Developer, Squad 2011, First Release Is Up][dev_squad_first_release_2011]
- [Developer, Squad 2014, KSP: Asteroid Redirect Mission Is Officially Released][dev_squad_arm_2014]
- [Developer, Take-Two 2017, Take-Two Acquires Kerbal Space Program][dev_take_two_ksp_2017]
- [Developer, Take-Two 2023, Kerbal Space Program 2 Launches in Early Access][dev_take_two_ksp2_2023]
- [News, Big Think 2015, Michio Kaku][news_big_think_kaku_2015]
- [News, Den of Geek 2020, How EVE Online Players Say the Game Changed Their Lives][news_den_of_geek_2020]
- [News, Engadget 2008, Making Money, the Origin of the Specie][news_engadget_tritanium_2008]
- [News, Engadget 2009, New Perspective on EVE Online's Latest Bank Embezzlement][news_engadget_ebank_2009]
- [News, Engadget 2013, EVE Online Smashes PCU Record During Anniversary Celebrations][news_engadget_pcu_2013]
- [News, Engadget 2014, EVE Fanfest 2014 Economy Talk][news_engadget_plex_2014]
- [News, GamersNexus 2016, Chris Roberts on Character Technology and Engine Architecture][news_gamersnexus_roberts_2016]
- [News, GeekWire 2024, Take-Two Interactive Layoffs Hit Seattle Area][news_geekwire_intercept_2024]
- [News, Gematsu 2026, CCP Games Rebrands to Fenris Creations][news_gematsu_fenris_2026]
- [News, Gizmodo 2011, The First Draft of the Star Trek Pitch][news_gizmodo_trek_pitch_2011]
- [News, IEEE Spectrum 2009, EVE Online Game Player Embezzles Virtual Money][news_ieee_ebank_2009]
- [News, Kotaku 2018, Star Citizen Backer Sues to Get $4,500 Back, Loses][news_kotaku_refund_2018]
- [News, Massively Overpowered 2016, Star Citizen Changes Refund Clause for New Backers][news_massively_refund_2016]
- [News, PC Gamer 2021, Star Citizen Adds Disclaimer to Spaceship Preorders][news_pcgamer_asa_2021]
- [News, PC Gamer 2024, Kerbal Space Program 2 Developer Intercept Games and Rollerdrome Studio Roll7 Are Reportedly Closing][news_pcgamer_intercept_2024]
- [News, Polygon 2017, Star Citizen Backer's $25,000 Refund Has Taken Months][news_polygon_refund_2017]
- [News, Reuters 2009, Gamer Steals Online Loot to Pay Real-World Debts][news_reuters_ebank_2009]
- [News, Slashdot 2013, J. Michael Straczynski Answers Your Questions][news_slashdot_straczynski_2013]
- [News, Space.com 2015, The Expanse][news_space_com_expanse_2015]
- [News, The Guardian 2002, Wake-up Call][news_guardian_mc02_2002]
- [News, The Mittani 2012, Sins of a Solar Spymaster 78, The Extortion of Empire][news_ten_ton_hammer_otec_2012]
- [News, The Register 2009, Gamer Embezzles Virtual Cash to Settle Real Debts][news_register_ebank_2009]
- [Reference, Edmund Optics, Can a Laser Beam Be Seen from the Side?][ref_edmund_laser]
- [Reference, FAI 2018, Statement about the Karman Line][ref_fai_karman_2018]
- [Reference, Hattendorf 2014, Saving Nimitz's Graybook][ref_hattendorf_2014]
- [Reference, SIGGRAPH History, The Last Starfighter][ref_siggraph_last_starfighter]
- [Reference, Traveller System Reference Document, Spacecraft Operations][ref_traveller_srd]
- [Reference, U.S. Joint Forces Command, Millennium Challenge 2002 Experiment Report][ref_jfcom_mc02]
- [Reference, Washington Employment Security Department, WARN Notices][ref_wa_esd_warn]
- [Related Post, Mass Drivers][related_post_mass_drivers]
- [Related Post, Orbital Manoeuvres in Terms of Delta-v][related_post_orbital_manoeuvres]
- [Related Post, Published Wargames of War with China][related_post_published_wargames]
- [Related Post, Solar Sailing][related_post_solar_sailing]
- [Research, Abramson 1966, The Dynamic Behavior of Liquids in Moving Containers][research_abramson_1966]
- [Research, Allen and Eggers 1958, A Study of the Motion and Aerodynamic Heating of Ballistic Missiles Entering the Earth's Atmosphere][research_allen_eggers_1958]
- [Research, Armstrong 2001, Role Playing: A Method to Forecast Decisions][research_armstrong_2001]
- [Research, Ashby 2003, Relativity in the Global Positioning System][research_ashby_2003]
- [Research, Barnett et al. 2006, The Impact of Science Fiction Film on Student Understanding of Science][research_barnett_et_al_2006]
- [Research, Berry and Coppola 2007, Correct Modeling of the Indirect Term for Third-Body Perturbations][research_berry_coppola_2007]
- [Research, Bohr 1913, On the Constitution of Atoms and Molecules][research_bohr_1913]
- [Research, Castronova et al. 2009, As Real as Real? Macroeconomic Behavior in a Large-Scale Virtual World][research_castronova_et_al_2009]
- [Research, Clement 1982, Students' Preconceptions in Introductory Mechanics][research_clement_1982]
- [Research, Green and Armstrong 2007, The Ombudsman: Value of Expertise for Forecasting Decisions in Conflicts][research_green_armstrong_2007]
- [Research, Hairer and Söderlind 2005, Explicit, Time Reversible, Adaptive Step Size Control][research_hairer_soderlind_2005]
- [Research, Hairer et al. 2003, Geometric Numerical Integration Illustrated by the Störmer-Verlet Method][research_hairer_et_al_2003]
- [Research, Levin et al. 2017, Darwin's Aliens][research_levin_et_al_2017]
- [Research, Li et al. 2017, Modeling and Research of a Space-Based Spacecraft Infrared Detection System][research_li_et_al_2017]
- [Research, Lisk et al. 2011, Leadership in Multiplayer Online Gaming Environments][research_lisk_et_al_2011]
- [Research, Lofgren and Fefferman 2007, The Untapped Potential of Virtual Game Worlds to Shed Light on Real World Epidemics][research_lofgren_fefferman_2007]
- [Research, McDermott and Redish 1999, Resource Letter PER-1: Physics Education Research][research_mcdermott_redish_1999]
- [Research, McKagan et al. 2008, Why We Should Teach the Bohr Model and How to Teach It Effectively][research_mckagan_et_al_2008]
- [Research, Monniaux 2008, The Pitfalls of Verifying Floating-Point Computations][research_monniaux_2008]
- [Research, Orthia 2019, How Does Science Fiction Television Shape Fans' Relationships to Science? Results from a Survey of 575 Doctor Who Viewers][research_orthia_2019]
- [Research, Park et al. 2021, The JPL Planetary and Lunar Ephemerides DE440 and DE441][research_park_et_al_2021]
- [Research, Perla and McGrady 2011, Why Wargaming Works][research_perla_mcgrady_2011]
- [Research, Rubel 2006, The Epistemology of War Gaming][research_rubel_2006]
- [Research, Sutton and Graves 1971, A General Stagnation-Point Convective Heating Equation for Arbitrary Gas Mixtures][research_sutton_graves_1971]
- [Research, Tanikawa et al. 2013, Phantom-GRAPE: Numerical Software Library to Accelerate Collisionless N-Body Simulation][research_tanikawa_et_al_2013]
- [Research, Whipple 1947, Meteorites and Space Travel][research_whipple_1947]
- [Research, Williams 2010, The Mapping Principle, and a Research Framework for Virtual Worlds][research_williams_2010]
- [Research, Wisdom and Holman 1991, Symplectic Maps for the N-Body Problem][research_wisdom_holman_1991]
- [Research, Xanthopoulou and Papagiannidis 2012, Play Online, Work Better?][research_xanthopoulou_papagiannidis_2012]
- [Research, Yoshida 1990, Construction of Higher Order Symplectic Integrators][research_yoshida_1990]

[agency_esa_geo_2020]: https://www.esa.int/ESA_Multimedia/Images/2020/03/Geostationary_orbit
[agency_jpl_ephemerides_2020]: https://ssd.jpl.nasa.gov/planets/eph_export.html
[agency_nasa_black_holes]: https://science.nasa.gov/universe/black-holes/
[agency_nasa_bsf_trajectories]: https://science.nasa.gov/learn/basics-of-space-flight/chapter4-1/
[agency_nasa_coming_home]: https://www.nasa.gov/wp-content/uploads/2015/04/695726main_cominghome-ebook.pdf
[agency_nasa_dawn_faq]: https://science.nasa.gov/mission/dawn/faq/
[agency_nasa_earth_fact_sheet]: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
[agency_nasa_em_anatomy]: https://science.nasa.gov/ems/02_anatomy/
[agency_nasa_gamers_osiris_2016]: https://www.nasa.gov/centers-and-facilities/goddard/gamers-tackle-virtual-asteroid-sampling-mission/
[agency_nasa_gmat_2007]: https://ntrs.nasa.gov/citations/20080031744
[agency_nasa_iss_atcs]: https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf
[agency_nasa_jupiter_fact_sheet]: https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html
[agency_nasa_laser_comm_timeline_2021]: https://www.nasa.gov/centers-and-facilities/goddard/nasa-laser-communications-innovations-a-timeline/
[agency_nasa_maarss_2019]: https://ntrs.nasa.gov/citations/20190002579
[agency_nasa_microgravity]: https://www.nasa.gov/learning-resources/for-kids-and-students/what-is-microgravity-grades-5-8/
[agency_nasa_moon_fact_sheet]: https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html
[agency_nasa_newton]: https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/newtons-laws-of-motion/
[agency_nasa_niac_stysley_2011]: https://www.nasa.gov/wp-content/uploads/2017/07/niac_2011_phasei_stysley_laserbasedopticaltrap_tagged.pdf
[agency_nasa_orbit_catalog_2009]: https://science.nasa.gov/earth/earth-observatory/catalog-of-earth-satellite-orbits/
[agency_nasa_orbit_primer_2018]: https://science.nasa.gov/wp-content/uploads/2023/05/GDC_OrbitPrimer.pdf
[agency_nasa_pressure_suits_2017]: https://www.nasa.gov/wp-content/uploads/2023/05/dressing-for-altitude-nov-2017.pdf
[agency_nasa_rocket_principles]: https://www.grc.nasa.gov/www/k-12/rocket/TRCRocket/rocket_principles.html
[agency_nasa_shuttle_rcs_1975]: https://ntrs.nasa.gov/citations/19750061613
[agency_nasa_smallsat_thermal]: https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/
[agency_nasa_sp413_1977]: https://ntrs.nasa.gov/citations/19770014162
[agency_nasa_space_comms_2020]: https://www.nasa.gov/missions/tech-demonstration/space-communications-7-things-you-need-to-know/
[agency_nasa_star_trek_55_2024]: https://www.nasa.gov/history/55-years-ago-star-trek-final-episode-airs-relationship-with-nasa-endures/
[agency_nasa_sun_fact_sheet]: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
[agency_nasa_tm_2025_mars_comms]: https://ntrs.nasa.gov/api/citations/20250003885/downloads/NASA%20TM20250003885.pdf
[agency_nasa_webb_orbit]: https://science.nasa.gov/mission/webb/orbit/
[agency_nasa_whipple]: https://hvit.jsc.nasa.gov/shield-development/
[agency_nasa_winternitz_2017]: https://ntrs.nasa.gov/citations/20170004590
[book_battin_1999]: https://doi.org/10.2514/4.861543
[book_caffrey_2019]: https://digital-commons.usnwc.edu/newport-papers/43/
[book_conway_morris_2003]: https://doi.org/10.1017/CBO9780511535499
[book_curtis_2020_interplanetary]: https://doi.org/10.1016/b978-0-08-102133-0.00008-8
[book_friedman_2017]: https://www.history.navy.mil/research/publications/publications-by-subject/winning-a-future-war.html
[book_glasstone_1964]: https://doi.org/10.2172/972902
[book_hawking_hawking_2007]: https://openlibrary.org/books/OL9523149M
[book_herman_et_al_2009]: https://openlibrary.org/isbn/9780071596886
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
[dev_bettner_terrano_2001]: https://www.gamedeveloper.com/programming/1500-archers-on-a-28-8-network-programming-in-age-of-empires-and-beyond
[dev_ccp_b_r5rb_2014]: https://www.eveonline.com/news/view/the-bloodbath-of-b-r5rb
[dev_ccp_broker_relations_2020]: https://www.eveonline.com/news/view/broker-relations
[dev_ccp_capsuleers]: https://universe.eveonline.com/lore/capsuleers
[dev_ccp_character_nodes_2010]: https://www.eveonline.com/news/view/fixing-lag-character-nodes
[dev_ccp_corporations_2007]: https://www.eveonline.com/news/view/econ-dev-blog-no.-3-some-statistics-on-corporations
[dev_ccp_economist_2007]: https://community.eveonline.com/news/news-channels/press-releases/eve-online-appoints-in-world-economist-1
[dev_ccp_economy_vegas_2015]: https://www.eveonline.com/news/view/eve-economy-update-eve-vegas-2015-report
[dev_ccp_esi_overview]: https://developers.eveonline.com/docs/services/esi/overview/
[dev_ccp_esi_tritanium]: https://esi.evetech.net/latest/universe/types/34/?datasource=tranquility&language=en
[dev_ccp_faucets_2006]: https://www.eveonline.com/news/view/a-deal-is-a-deal...
[dev_ccp_hed_gp_2014]: https://www.eveonline.com/news/view/what-a-hed-ache
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
[dev_ccp_taxes_2019]: https://www.eveonline.com/news/view/updates-to-sales-taxes-and-brokers-fees
[dev_ccp_technetium_2012]: https://www.eveonline.com/news/view/tech-is-fine-l2p
[dev_ccp_useful_formulae]: https://developers.eveonline.com/docs/guides/useful-formulae/
[dev_ccp_viridian_2023]: https://www.eveonline.com/news/view/viridian-expansion-notes
[dev_ccp_warp_2013]: https://www.eveonline.com/news/view/warp-drive-active
[dev_cig_financials_2020]: https://cloudimperiumgames.com/blog/corporate/cloud-imperium-financials-for-2020
[dev_cig_financials_2021]: https://cloudimperiumgames.com/blog/corporate/cloud-imperium-financials-for-2021
[dev_cig_financials_2022]: https://cloudimperiumgames.com/blog/corporate/cloud-imperium-financials-for-2022
[dev_cig_financials_2023]: https://cloudimperiumgames.com/blog/corporate/cloud-imperium-financials-for-2023
[dev_cig_financials_2024]: https://cloudimperiumgames.com/blog/corporate/cfo-comment-on-the-2024-accounting
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
[dev_harvester_patched_conics_2012]: https://www.physicsforums.com/threads/patched-conics-trajectory-from-initial-orbit-state.590896/
[dev_kerbaledu_2016]: https://web.archive.org/web/20160104215459/http://www.kerbaledu.com/
[dev_ksp2_steam]: https://store.steampowered.com/app/954850/
[dev_ksp_steam]: https://store.steampowered.com/app/220200/
[dev_luna_multiplayer]: https://github.com/LunaMultiplayer/LunaMultiplayer/wiki
[dev_principia]: https://github.com/mockingbirdnest/Principia
[dev_principia_jool]: https://github.com/mockingbirdnest/Principia/wiki/On-the-dynamical-stability-of-Principia's-modified-Jool-system
[dev_real_solar_system]: https://github.com/KSP-RO/RealSolarSystem
[dev_realism_overhaul]: https://github.com/KSP-RO/RealismOverhaul
[dev_rsi_alpha_300_2017]: https://robertsspaceindustries.com/en/comm-link/transmission/16348-Star-Citizen-Alpha-300
[dev_rsi_alpha_315_2021]: https://robertsspaceindustries.com/en/comm-link/transmission/18338-Deadly-Consequences-Alpha-315
[dev_rsi_alpha_40]: https://robertsspaceindustries.com/en/comm-link/Patch-Notes/20360-Star-Citizen-Alpha-40
[dev_rsi_carrack_2014]: https://robertsspaceindustries.com/en/comm-link/transmission/14323-Into-The-Unknown-A-Carrack-Her-Crew
[dev_rsi_crowdfund_stats]: https://robertsspaceindustries.com/en/funding-goals
[dev_rsi_flight_2020]: https://robertsspaceindustries.com/en/comm-link/transmission/17647-Flight-Fight-Upcoming-Improvements
[dev_rsi_fuel_2018]: https://robertsspaceindustries.com/en/comm-link/engineering/16517-The-Shipyard-Fuel-Mechanics
[dev_rsi_letter_2018]: https://robertsspaceindustries.com/en/comm-link/transmission/16700-Letter-From-The-Chairman
[dev_rsi_letter_2020]: https://robertsspaceindustries.com/en/comm-link/transmission/17805-Letter-From-The-Chairman
[dev_rsi_lore_gravity_2014]: https://robertsspaceindustries.com/en/comm-link/spectrum-dispatch/14262-LORE-BUILDER-TWENTY-Journeys-Generators
[dev_rsi_patch_300_2017]: https://robertsspaceindustries.com/en/comm-link/transmission/16349-Star-Citizen-Alpha-300
[dev_rsi_patch_320_2018]: https://robertsspaceindustries.com/spectrum/community/SC/forum/190048/thread/star-citizen-alpha-3-2-0-live-796019-patch-notes
[dev_rsi_patch_340_2018]: https://robertsspaceindustries.com/spectrum/community/SC/forum/190048/thread/star-citizen-alpha-3-4-0-live-1028053-patch-notes
[dev_rsi_patch_450_2025]: https://robertsspaceindustries.com/en/comm-link/Patch-Notes/20934-Star-Citizen-Alpha-450
[dev_rsi_roadmap]: https://robertsspaceindustries.com/roadmap/release-view
[dev_rsi_tos_2026]: https://robertsspaceindustries.com/tos
[dev_squad_arm_2014]: https://steamcommunity.com/games/220200/announcements/detail/1315356550594321621
[dev_squad_first_release_2011]: https://web.archive.org/web/20111013113946/http://kerbalspace.tumblr.com/post/6872084213/first-release-is-up
[dev_take_two_ksp2_2023]: https://ir.take2games.com/node/29461/pdf
[dev_take_two_ksp_2017]: https://ir.take2games.com/static-files/f86fae80-882c-4c68-b71c-07560c4b1183
[news_big_think_kaku_2015]: https://bigthink.com/videos/universe-in-a-nutshell-the-physics-of-everything-with-michio-kaku/
[news_den_of_geek_2020]: https://www.denofgeek.com/games/eve-online-players-lives-better/
[news_engadget_ebank_2009]: https://www.engadget.com/2009-07-02-new-perspective-on-eve-onlines-latest-bank-embezzlement.html
[news_engadget_pcu_2013]: https://www.engadget.com/2013-05-06-eve-online-smashes-pcu-record-during-anniversary-celebrations.html
[news_engadget_plex_2014]: https://www.engadget.com/2014-05-01-eve-fanfest-2014-economy-talk-highlights-plex-prices-and-reveal.html
[news_engadget_tritanium_2008]: https://www.engadget.com/2008-06-29-making-money-the-origin-of-the-specie.html
[news_gamersnexus_roberts_2016]: https://gamersnexus.net/gg/2617-chris-roberts-character-technology-weather-system-engine-arch
[news_geekwire_intercept_2024]: https://www.geekwire.com/2024/take-two-layoffs-hit-seattle-area-70-workers-affected/
[news_gematsu_fenris_2026]: https://www.gematsu.com/2026/05/ccp-games-rebrands-to-fenris-creations-following-split-from-pearl-abyss
[news_gizmodo_trek_pitch_2011]: https://gizmodo.com/read-the-first-draft-of-gene-roddenberrys-star-trek-pit-5746652
[news_guardian_mc02_2002]: https://www.theguardian.com/world/2002/sep/06/usa.iraq
[news_ieee_ebank_2009]: https://spectrum.ieee.org/eve-online-game-player-embezzles-virtual-money-creates-real-trouble
[news_kotaku_refund_2018]: https://kotaku.com/star-citizen-backer-sues-to-get-4-500-back-loses-1827666550
[news_massively_refund_2016]: https://massivelyop.com/2016/06/21/star-citizen-changes-refund-clause-for-new-backers-plans-procedurally-generated-planets-for-2-7/
[news_pcgamer_asa_2021]: https://www.pcgamer.com/star-citizen-adds-disclaimer-to-spaceship-preorders-after-regulator-says-theyre-misleading/
[news_pcgamer_intercept_2024]: https://www.pcgamer.com/games/sim/kerbal-space-program-2-developer-intercept-games-may-be-closing-as-part-of-take-twos-big-layoff-plan/
[news_polygon_refund_2017]: https://www.polygon.com/2017/12/13/16767590/star-citizen-refund/
[news_register_ebank_2009]: https://www.theregister.com/security/2009/07/03/gamer-embezzles-virtual-cash-to-settle-real-debts/1491814
[news_reuters_ebank_2009]: https://www.eeworldonline.com/gamer-steals-online-loot-to-pay-real-world-debts/
[news_slashdot_straczynski_2013]: https://entertainment.slashdot.org/story/13/04/15/1328251/interviews-j-michael-straczynski-answers-your-questions
[news_space_com_expanse_2015]: https://www.space.com/31437-the-expanse-crazy-sci-fi-tech.html
[news_ten_ton_hammer_otec_2012]: https://www.tentonhammer.com/columns/sins-of-a-solar-spymaster-78-the-extortion-of-empire
[ref_edmund_laser]: https://www.edmundoptics.com/knowledge-center/frequently-asked-questions/general-questions/lasers/can-a-laser-beam-be-seen-from-the-side
[ref_fai_karman_2018]: https://www-2025.fai.org/news/statement-about-karman-line
[ref_hattendorf_2014]: https://www.usni.org/magazines/naval-history-magazine/2014/june/saving-nimitzs-graybook
[ref_jfcom_mc02]: https://www.esd.whs.mil/Portals/54/Documents/FOID/Reading%20Room/Joint_Staff/12-F-0344-Millennium-Challenge-2002-Experiment-Report.pdf
[ref_siggraph_last_starfighter]: https://history.siggraph.org/?p=94037
[ref_traveller_srd]: https://www.traveller-srd.com/core-rules/spacecraft-operations/
[ref_wa_esd_warn]: https://fortress.wa.gov/esd/file/WARN/Public/SearchWARN.aspx
[related_post_mass_drivers]: {% post_url 2026-08-19-mass_drivers %}
[related_post_orbital_manoeuvres]: {% post_url 2026-08-17-orbital_manoeuvres %}
[related_post_published_wargames]: {% post_url 2026-08-11-published_wargames_of_war_with_china %}
[related_post_solar_sailing]: {% post_url 2026-08-18-solar_sailing %}
[research_abramson_1966]: https://ntrs.nasa.gov/citations/19670006555
[research_allen_eggers_1958]: https://ntrs.nasa.gov/citations/19930091020
[research_armstrong_2001]: https://doi.org/10.1007/978-0-306-47630-3_2
[research_ashby_2003]: https://doi.org/10.12942/lrr-2003-1
[research_barnett_et_al_2006]: https://doi.org/10.1007/s10956-006-9001-y
[research_berry_coppola_2007]: https://www.agi.com/getmedia/eff08466-52ad-4483-958a-2e3ceb922eab/Correct-Modeling-of-the-Indirect-Term-for-Third-Body-Perturbations.pdf
[research_bohr_1913]: https://doi.org/10.1080/14786441308634955
[research_castronova_et_al_2009]: https://doi.org/10.1177/1461444809105346
[research_clement_1982]: https://doi.org/10.1119/1.12989
[research_green_armstrong_2007]: https://doi.org/10.1287/inte.1060.0262
[research_hairer_et_al_2003]: https://doi.org/10.1017/S0962492902000144
[research_hairer_soderlind_2005]: https://doi.org/10.1137/040606995
[research_levin_et_al_2017]: https://doi.org/10.1017/S1473550417000362
[research_li_et_al_2017]: https://doi.org/10.1364/AO.56.002428
[research_lisk_et_al_2011]: https://doi.org/10.1177/1046878110391975
[research_lofgren_fefferman_2007]: https://doi.org/10.1016/S1473-3099(07)70212-8
[research_mcdermott_redish_1999]: https://doi.org/10.1119/1.19122
[research_mckagan_et_al_2008]: https://doi.org/10.1103/PhysRevSTPER.4.010103
[research_monniaux_2008]: https://doi.org/10.1145/1353445.1353446
[research_orthia_2019]: https://doi.org/10.22323/2.18040208
[research_park_et_al_2021]: https://doi.org/10.3847/1538-3881/abd414
[research_perla_mcgrady_2011]: https://digital-commons.usnwc.edu/nwc-review/vol64/iss3/8/
[research_rubel_2006]: https://digital-commons.usnwc.edu/nwc-review/vol59/iss2/8
[research_sutton_graves_1971]: https://ntrs.nasa.gov/citations/19720003329
[research_tanikawa_et_al_2013]: https://doi.org/10.1016/j.newast.2012.08.009
[research_whipple_1947]: https://doi.org/10.1086/106009
[research_williams_2010]: https://doi.org/10.1111/j.1468-2885.2010.01371.x
[research_wisdom_holman_1991]: https://doi.org/10.1086/115978
[research_xanthopoulou_papagiannidis_2012]: https://doi.org/10.1016/j.techfore.2012.03.006
[research_yoshida_1990]: https://doi.org/10.1016/0375-9601(90)90092-3
