---
layout: post
mathjax: true
comments: true
title: "Aerospace, Programming Languages, and Information Technology Co-Development: Pre-War Computing Origins and Ballistics"
date: 2026-07-13 09:00:00 +0000
categories: history technology aerospace
series: co_development_aerospace_computing
series_title: Aerospace, Programming Languages, and Information Technology Co-Development
series_index: 2
---

<!-- A238 -->
<script>console.log("A238");</script>

This second article of the twelve-part series covers the computing landscape as it stood between roughly 1900 and 1945, with focus on the specific aerospace and defense applications that produced the demand for the machines that followed. The framing established in [A237][related_post_a237_framing_co_development] treats the pre-war period as the preindustrial baseline of the aerospace-computing co-development pair. This article walks that baseline in detail. Ballistic table computation supplies the organizing thread. Mechanical fire-control computers, analog differential analyzers, electromechanical relay computers, and the origins of the first general-purpose electronic digital computer at the Moore School of Electrical Engineering each address the ballistics-table problem or its variants, and each contributes specific engineering artifacts that later programs inherited.

The article treats the four principal computing modalities of the period in the order they matured. Human computer bureaus organized under mathematicians produced the ballistic tables of the First World War and the interwar period. Mechanical fire-control computers translated the ballistics problem into physical linkages that field artillery, naval gunnery, and anti-aircraft crews could operate in real time. Analog differential analyzers solved the differential equations underlying ballistics numerically at accuracy sufficient for many practical calculations. Electronic digital computers, arriving at the very end of the period with the Electronic Numerical Integrator and Computer hereafter ENIAC, replaced the human computers at the specific task of ballistic-table production at speeds that made previously infeasible calculations routine.

## The Ballistic Table Problem

Exterior ballistics is the study of projectile motion after it leaves the muzzle of a gun and before it strikes the target. The governing equations are the equations of motion of a point mass subject to gravity and aerodynamic drag, treated as a standard problem in [McCoy 1999][book_mccoy_modern_exterior_ballistics] and in the earlier work by Moulton at Aberdeen. For a projectile with mass $m$, velocity $\mathbf{v}$, and position $\mathbf{x}$, the equations are

$$m \frac{d^2 \mathbf{x}}{dt^2} = m \mathbf{g} - \frac{1}{2} \rho v^2 C_d(M) A \hat{\mathbf{v}}$$

where $\mathbf{g}$ is gravitational acceleration, $\rho$ is atmospheric density which itself varies with altitude, $v$ is the speed, $C_d(M)$ is the drag coefficient as a function of Mach number $M$, $A$ is the projectile cross-sectional area, and $\hat{\mathbf{v}}$ is the unit velocity vector. The problem admits no closed-form solution for realistic projectiles because the drag coefficient depends non-linearly on the Mach number, especially in the transonic regime around $M = 1$, and because the atmospheric density varies with the trajectory itself. Numerical integration is the only practical approach.

A firing table for a specific gun and shell combination must give the elevation angle and time of flight for every target range across the operational envelope, corrected for atmospheric density, wind, and target altitude. A single table requires roughly 1,500 trajectories, per the account in [Grier 2005][book_grier_when_computers_were_human], and each trajectory requires between roughly 500 and 1,000 multiplications along with comparable additions. The total operation count per table is

$$N_{\text{ops}} = N_{\text{trajectories}} \cdot N_{\text{ops per trajectory}} \approx 1.5 \times 10^3 \cdot 7.5 \times 10^2 \approx 10^6$$

roughly one million floating-point-equivalent operations. A trained human computer performing manual arithmetic with mechanical desk calculators produced between 3,000 and 5,000 multiplications per working day. A single firing table therefore required roughly one computer-year of continuous labor. During the First World War the United States Army Ordnance Department established a computing bureau at the Aberdeen Proving Ground under [Moulton][research_moulton_1926] and expanded it through subsequent decades to keep pace with new artillery pieces and new shell designs.

The scale of the bureau expanded dramatically during the Second World War. By 1945 the Aberdeen bureau employed several hundred human computers, most of them women, working in shifts, per the accounts in [Grier 2005][book_grier_when_computers_were_human] and in the collected NASA and Ordnance Department histories. The Ballistic Research Laboratory hereafter BRL at Aberdeen was the single largest institutional consumer of scalar arithmetic in the United States during the war. The backlog of unfinished tables grew throughout the war as new weapons entered service faster than the bureau could produce firing tables, which set the specific demand that the ENIAC was built to meet.

## Mechanical Fire-Control Computers

Firing tables answer the question of where to aim a gun for a target at a known range. Fire-control computers answer the different but related question of how to aim a gun at a moving target given range and bearing measurements from optical or radar tracking. The fire-control problem is a real-time computation. The gun must fire ahead of the target by the projectile time-of-flight along a solution that accounts for target motion, own-ship motion, gun offset from the ship or aircraft reference frame, and ballistic corrections. In its simplest form, the intercept problem requires the aim point to satisfy

$$\mathbf{x}_{\text{aim}} = \mathbf{x}_{\text{target}}(t_0) + \mathbf{v}_{\text{target}} \cdot T_{\text{flight}}$$

where $T_{\text{flight}}$ is the projectile time-of-flight to the aim point, which itself depends on $\mathbf{x}_{\text{aim}}$ through the ballistic equations. The coupling makes the intercept problem implicit and requires iterative or approximate solution methods. Solving this problem in real time before the digital computer required physical linkages that implemented the arithmetic mechanically.

The [Ford Instrument Company][ref_ford_instrument_mk1] Mark 1 fire-control computer, in production from 1932 and installed on United States Navy capital ships from 1934, was the most sophisticated of the pre-war mechanical fire-control computers. The Mark 1 solved the naval gunnery problem using disk-and-ball integrators originally described in [Thomson 1876][research_thomson_1876] and elaborated by Thomson's brother William Thomson, later Lord Kelvin, in the same period, per the treatment in [Mindell 2002][book_mindell_between_human_and_machine]. A disk-and-ball integrator computes the integral $\int y \, dx$ mechanically by placing a ball on a rotating disk at radius $y$ from the disk center and driving the rotation by shaft speed proportional to $\dot{x}$. The output shaft rotation rate is

$$\dot{\theta}_{\text{output}} = \frac{y(t)}{R} \cdot \dot{\theta}_{\text{disk}}$$

where $R$ is the ball wheel radius, so the accumulated output rotation

$$\theta_{\text{output}}(t) = \frac{1}{R} \int_0^t y(\tau) \, d\theta_{\text{disk}}(\tau) = \frac{1}{R} \int y \, dx$$

directly implements the mathematical integral. The Mark 1 chained many such integrators together to solve the coupled differential equations of the fire-control problem, including target-motion prediction, ballistic trajectory correction, and stabilization against ship roll and pitch.

The [Kerrison Predictor][ref_kerrison_predictor], developed at the British Anti-Aircraft Research Committee in the late 1930s and produced in quantity by Sperry Gyroscope during the Second World War, applied similar mechanical-analog principles to anti-aircraft fire control. The Predictor accepted target range, bearing, and elevation from a rangefinder crew and computed the corrected aim point for a 40-millimeter Bofors gun to hit the target after the shell time-of-flight. The Predictor and its successors were used through the Battle of Britain and beyond, and their operational effectiveness was one of the specific factors that made low-altitude bombing runs increasingly costly for the Luftwaffe.

The Norden Mark XV bombsight, developed by Carl Norden and Theodore Barth from the mid-1920s and fielded in United States Army Air Forces bombers from 1937, computed the bomb-release point for level-flight bombing. Ignoring air resistance for a first approximation, a bomb released from altitude $H$ at ground speed $v_g$ falls for time

$$T_{\text{fall}} = \sqrt{\frac{2H}{g}}$$

and travels a horizontal trail distance

$$L_{\text{trail}} = v_g \cdot T_{\text{fall}} = v_g \sqrt{\frac{2H}{g}}$$

before impact, which gives the release-point offset from the target that the bombsight must compute. The Norden combined a gyroscopically stabilized telescopic sight with a mechanical computer that solved the full bombing equation including air resistance, ground speed measurement, altitude, wind, and target position. It also computed the release signal for the bomb and, in some variants, controlled the aircraft heading through the C-1 autopilot during the bombing run. The Norden was treated as a state secret through the Second World War and was widely regarded, then and later, as one of the most technically sophisticated mechanical computers ever built. Its precision claims turned out to be overstated in operational use, particularly under the anti-aircraft fire and weather conditions of European bombing, but the underlying mechanical computing was genuine and its influence on later fire-control and guidance systems substantial.

## Analog Differential Analyzers

The ballistic-table problem is fundamentally a problem of numerically integrating a system of ordinary differential equations. A differential analyzer solves such systems continuously in analog form rather than digitally step by step. The differential analyzer at MIT built by [Bush 1931][research_bush_1931] and [Bush and Caldwell 1945][research_bush_caldwell_1945] chained mechanical integrators, adders, multipliers, and function generators using rotating shafts as the primary data-carrying elements. A physical variable was represented as the angular position of a shaft. Integration was performed by disk-and-ball integrators of the same class used in the Ford Mark 1 fire-control computer. Multiplication was performed by servomechanisms coupling one shaft rotation rate to another according to a table of pre-cut cams.

The Bush analyzer was used for a wide variety of scientific and engineering problems including power system stability analysis, atomic structure calculation, and ballistic trajectory computation. A copy was built at the University of Manchester in the United Kingdom under Douglas Hartree in 1934, described by [Hartree 1935][research_hartree_1935] in Nature as one of the earliest widely available published accounts of an operating differential analyzer in Britain. Another copy was built at the BRL at Aberdeen in 1935 specifically for ballistic table production, and it operated in that role continuously through the Second World War, per [Bromley 1990][research_bromley_1990] and the account in [Owens 1986][book_owens_bush_analyzer]. A single trajectory that took a human computer roughly 20 hours to produce required roughly 15 minutes on the differential analyzer.

Analog analyzers had two fundamental limitations. First, accuracy was bounded by the physical precision of the mechanical elements. The Bush analyzer achieved approximately 0.1 percent accuracy per integrator, with error accumulating over a chained calculation. For a chain of $n$ serial integrators with individual error $\epsilon$, the total error scales approximately as

$$\epsilon_{\text{total}} \approx \epsilon \sqrt{n}$$

if errors are uncorrelated, giving 0.3 percent total error for a chain of 10 integrators. For ballistic trajectories with 5 to 10 chained integrations this was acceptable. For longer computations or higher-precision requirements it was not. Second, changing the problem required physically reconfiguring the analyzer, which took hours to days depending on complexity. Analog analyzers therefore excelled at repeated computation of a single problem class and struggled with problem diversity. Both limitations became increasingly binding as the Second World War generated demand for more calculations at higher precision than the analog analyzers could economically supply. The Rockefeller Differential Analyzer built by Bush at MIT between 1935 and 1942 used electromechanical rather than purely mechanical components and reached approximately 10 to 100 times the throughput of the original Bush analyzer, but the fundamental limits of analog computing remained.

## Electromechanical Predecessors

Between the analog differential analyzer and the electronic digital computer sits a class of electromechanical relay computers. These machines used telephone-style electromechanical relays as binary switching elements, with number representation and arithmetic implemented digitally rather than by continuous physical quantities. Relay switching was slower than vacuum-tube switching by three orders of magnitude, but relay reliability was substantially better than vacuum tubes could achieve in early implementations, and relays were manufactured by the telephone industry in enormous quantities at low unit cost. The relay switching time $t_{\text{switch}}$ of order 5 to 20 milliseconds set the maximum sequential operation rate to

$$r_{\text{max}} = \frac{1}{t_{\text{switch}}} \approx 50 \text{ to } 200 \text{ operations per second}$$

which was several orders of magnitude below vacuum-tube capability but adequate for many scientific calculations that did not require real-time response.

The Bell Telephone Laboratories Complex Number Calculator built by [Stibitz 1940][research_stibitz_1940] and demonstrated remotely from Dartmouth College over telegraph lines in September 1940 was the first electromechanical relay computer to demonstrate remote operation. Its problem domain was complex-number arithmetic for filter design and network analysis, where the product of complex numbers $a + bi$ and $c + di$ requires four real multiplications and two real additions per the standard formula

$$(a + bi)(c + di) = (ac - bd) + (ad + bc)i$$

which was tedious enough by hand that Bell Labs engineers welcomed the calculator's twenty-second execution time as a substantial productivity improvement. The successor Bell Labs Model V, delivered to the National Advisory Committee for Aeronautics hereafter NACA Langley in 1946 and to Aberdeen Proving Ground in 1947, was a general-purpose relay computer that could execute stored programs read from punched tape. The Model V used approximately 9,000 relays and computed at roughly 5 to 10 multiplications per second, thousands of times slower than the ENIAC but with substantially better reliability.

The German engineer Konrad Zuse independently developed a parallel line of electromechanical computers in Berlin between 1936 and 1945. The Zuse [Z3][ref_zuse_z3], completed in May 1941, was the first working programmable binary computer and computed floating-point arithmetic using approximately 2,600 relays, per the primary technical reconstruction in [Rojas 1997][research_rojas_1997]. Zuse's work was largely unknown outside Germany until after the war and had little direct influence on Allied computing development, but it established the feasibility of the relay-based digital computing approach and contributed to the postwar recognition that relay computers occupied a specific technological niche that neither the analog analyzer nor the vacuum-tube computer reached.

The IBM Automatic Sequence Controlled Calculator, more commonly known as the Harvard Mark I, was built at International Business Machines and delivered to Harvard University under Howard Aiken in 1944, and described technically in [Aiken and Hopper 1946][research_aiken_hopper_1946] in a three-part paper in Electrical Engineering. The Mark I combined electromechanical relays with rotating cam-driven mechanical elements and computed at approximately 3 to 5 multiplications per second. It was substantially slower than the ENIAC that followed it, but its 1944 delivery date made it one of the first operational large-scale automatic computers in the United States, and it was used through the war for a variety of ordnance and aerodynamics calculations under Aiken and Commander Grace Hopper of the United States Navy Reserve.

## The Electronic Numerical Integrator and Computer

The ENIAC was designed and built at the Moore School of Electrical Engineering at the University of Pennsylvania between 1943 and 1945 under a contract from the Ballistic Research Laboratory at Aberdeen. The project was proposed by physicist John Mauchly in a 1942 memorandum, per [Mauchly 1942][research_mauchly_1942], describing "The Use of High Speed Vacuum Tube Devices for Calculating," and was implemented by Mauchly with electrical engineer J. Presper Eckert as the lead design engineer. The BRL contract was signed 5 June 1943 for what the contract described as an "electronic difference analyzer" for ballistic table computation.

The ENIAC used 17,468 vacuum tubes, weighed approximately 30 tons, occupied a room 30 feet by 50 feet, and consumed approximately 150 kilowatts of electrical power, per the primary description in [Goldstine and Goldstine 1946][research_goldstine_goldstine_1946] published in Mathematical Tables and Other Aids to Computation. It performed roughly 5,000 additions per second or 385 multiplications per second, three orders of magnitude faster than the electromechanical Harvard Mark I and approximately five orders of magnitude faster than a human computer with a mechanical desk calculator. A trajectory that required 20 hours from a human computer or 15 minutes from the differential analyzer required approximately 30 seconds on the ENIAC. This speed comparison

$$T_{\text{ENIAC}} : T_{\text{DA}} : T_{\text{human}} \approx 1 : 30 : 2400$$

understates the practical significance because the ENIAC could work continuously through shifts on multiple problems as long as its vacuum tubes did not fail, while human computers and differential analyzers required extensive setup per problem.

Vacuum tube reliability was the ENIAC's principal engineering challenge. If each tube had mean time between failures $T_{\text{tube}}$ and the machine required all $N_{\text{tubes}}$ tubes to function, the machine mean time between failures satisfied approximately

$$T_{\text{ENIAC}} \approx \frac{T_{\text{tube}}}{N_{\text{tubes}}}$$

for uncorrelated failures. With $N_{\text{tubes}} = 17{,}468$ and $T_{\text{tube}}$ approximately 2,500 hours, the naive prediction gave a machine MTBF of roughly 8 minutes, which would have made the ENIAC useless. The engineering team, led by Eckert, adopted several countermeasures including running tubes at substantially reduced heater voltage to extend individual tube life, systematic overnight tube testing to identify tubes about to fail, and physical arrangement that made tube replacement fast when failure did occur. The actual operational MTBF reached several days once the machine stabilized, per [McCartney 1999][book_mccartney_eniac] and the account in [Ceruzzi 2003][book_ceruzzi_history_modern_computing].

Energy consumption per operation for the ENIAC was extraordinary by modern standards. Dividing electrical power by operation rate,

$$E_{\text{op}} = \frac{P}{r_{\text{ops}}} = \frac{150 \text{ kW}}{5{,}000 \text{ additions per second}} = 30 \text{ joules per addition}$$

which is approximately twelve orders of magnitude larger than the picojoule-per-operation energy budget of contemporary integrated circuits. The energy-per-operation trajectory across the digital era is one of the fundamental co-development quantities the series treats, and the ENIAC anchors the historical starting point.

The ENIAC was operational at the Moore School in late 1945, though it was not publicly announced until 15 February 1946, several months after the war ended. Its first substantive calculation was not a ballistic table but a mathematical simulation of the thermonuclear reaction rates for the hydrogen bomb feasibility study, requested by Edward Teller and John von Neumann for the Manhattan Project, per the retrospective account in [Metropolis and Nelson 1982][research_metropolis_nelson_1982] documenting the early computing work at Los Alamos National Laboratory. The BRL took delivery of the machine in 1947 and used it for ballistic-table production for approximately seven years, during which it was reprogrammed multiple times and eventually converted to stored-program operation using ideas from the [von Neumann 1945][related_post_a237_framing_co_development] First Draft of a Report on the EDVAC. The direct predecessor role of the ENIAC in producing the subsequent digital computer industry is treated in [Goldstine 1972][book_goldstine_computer_from_pascal_to_von_neumann], and the collection of primary sources spanning the entire pre-ENIAC and early-ENIAC period is compiled and annotated in [Randell 1975][book_randell_origins_of_digital_computers], which remains the standard scholarly anthology.

## Framework Application to the Pre-War Era

The six-axis framework introduced in the preceding article applies to the pre-war era with the axis weightings that characterize this specific historical moment.

The first axis is numerical computation demand. The demand was overwhelmingly ballistic table production, with secondary demand from other artillery-related calculations including bomb ballistics, torpedo fire control, and rocket trajectory analysis. Aerodynamic calculation for aircraft design was a distant third. The total operation count required for the wartime demand exceeded human capacity by orders of magnitude, and this excess was the specific pressure that produced the ENIAC and its contemporaries. The wall-clock time to produce a single firing table scales as

$$T_{\text{table}} = N_{\text{trajectories}} \cdot t_{\text{trajectory}}$$

which for $N_{\text{trajectories}} \approx 1{,}500$ gives 30,000 person-hours or roughly 15 person-years of continuous labor by human computer for $t_{\text{trajectory}} \approx 20$ hours, roughly 375 machine-hours or two machine-months for the differential analyzer at $t_{\text{trajectory}} \approx 15$ minutes, and roughly 12.5 machine-hours or half a machine-day for the ENIAC at $t_{\text{trajectory}} \approx 30$ seconds. The five-orders-of-magnitude compression from human bureau to ENIAC is what made the wartime table backlog tractable in principle even though the machine arrived too late to affect operations directly.

The second axis is real-time control. Fire-control computers occupied this axis exclusively during the pre-war and wartime period. The Ford Mark 1, the Kerrison Predictor, the Norden bombsight, and their contemporaries all operated in real time under strict latency bounds set by projectile time-of-flight and target motion. The mechanical-analog approach was the only feasible implementation given the technology of the period, and the disk-and-ball integrator was the load-bearing computing element.

The third axis is reliability and verification. The reliability of mechanical fire-control computers was addressed through overengineering, redundancy of critical components, and extensive shipboard maintenance procedures. The reliability of the ENIAC was addressed through the tube-derating and testing procedures previously described. Verification, in the modern sense of establishing that the computation performed matched the intended computation, was addressed by comparison of computed results against hand-calculated reference cases, since the correctness of the underlying mathematics was not in doubt but the correctness of the machine implementation could always be questioned.

The fourth axis is networking and distribution. The pre-war period had no computer networks in the modern sense, but distributed sensor-to-actuator systems existed. The Chain Home radar network in Britain distributed radar returns from coastal stations to a central filter room where plotters combined the returns into a single track picture, which was then distributed to fighter command sectors for interception. The bandwidth-delay product of the plotter-to-fighter-controller path was measured in minutes and kilometers, and the plotters served as the human implementation of the sensor-fusion function that later automated systems would perform in software.

The fifth axis is software engineering as a discipline. The pre-war era predated software engineering as a discipline, but analog analyzer programming, plugboard configuration for the ENIAC, and the systematic notations that human computer bureaus used to record and check calculations all constitute proto-software-engineering practices. Mauchly, Eckert, and the mathematicians associated with the BRL including [Adele Goldstine][ref_adele_goldstine], who wrote the first ENIAC operating manual, contributed to the initial vocabulary and practice.

The sixth axis is semiconductor economics and dual-use. The vacuum tube was the pre-transistor equivalent of the modern semiconductor, and the vacuum-tube industry was substantially expanded by wartime demand for radar, radio, and computing applications. The learning-curve mechanism formalized in the preceding article applied to vacuum tubes as it later applied to transistors, and the postwar transition from vacuum tubes to transistors inherited a manufacturing base that wartime demand had built out.

## Conclusion

The pre-war era established the aerospace-computing coupling in its earliest recognizable form. Ballistic table demand exceeded human capacity, mechanical fire-control demand exceeded human capacity, and both created sustained pressure for computational machinery that produced the analog differential analyzer, the electromechanical relay computer, and eventually the electronic digital computer. Each modality contributed specific engineering artifacts. The disk-and-ball integrator moved from the fire-control computer to the differential analyzer and eventually to the digital-analog hybrid computers of the postwar period. The plugboard programming of the ENIAC anticipated later programming abstractions. The vacuum-tube reliability engineering developed for the ENIAC influenced early commercial computers and continued to matter until the transistor supplanted the vacuum tube in the late 1950s.

The next article in the series treats the wartime computing efforts that ran in parallel with the ENIAC development, including the Colossus code-breaking computers at Bletchley Park, the Manhattan Project computing infrastructure, and the specific role of the Second World War in accelerating the transition from mechanical and analog computing to electronic digital computing.

## References

### Books

- [Ceruzzi 2003][book_ceruzzi_history_modern_computing]
- [Goldstine 1972][book_goldstine_computer_from_pascal_to_von_neumann]
- [Grier 2005][book_grier_when_computers_were_human]
- [McCartney 1999][book_mccartney_eniac]
- [McCoy 1999][book_mccoy_modern_exterior_ballistics]
- [Mindell 2002][book_mindell_between_human_and_machine]
- [Owens 1986][book_owens_bush_analyzer]
- [Randell 1975][book_randell_origins_of_digital_computers]

### Reference

- [Adele Goldstine ENIAC Manual][ref_adele_goldstine]
- [Ford Instrument Mark 1][ref_ford_instrument_mk1]
- [Kerrison Predictor][ref_kerrison_predictor]
- [Zuse Z3][ref_zuse_z3]

### Related Posts

- [A237 Framing and the Co-Development Mechanism][related_post_a237_framing_co_development]

### Research

- [Aiken and Hopper 1946][research_aiken_hopper_1946]
- [Bromley 1990][research_bromley_1990]
- [Bush 1931][research_bush_1931]
- [Bush and Caldwell 1945][research_bush_caldwell_1945]
- [Goldstine and Goldstine 1946][research_goldstine_goldstine_1946]
- [Hartree 1935][research_hartree_1935]
- [Mauchly 1942][research_mauchly_1942]
- [Metropolis and Nelson 1982][research_metropolis_nelson_1982]
- [Moulton 1926][research_moulton_1926]
- [Rojas 1997][research_rojas_1997]
- [Stibitz 1940][research_stibitz_1940]
- [Thomson 1876][research_thomson_1876]

[book_ceruzzi_history_modern_computing]: https://mitpress.mit.edu/9780262532037/a-history-of-modern-computing/
[book_goldstine_computer_from_pascal_to_von_neumann]: https://press.princeton.edu/books/paperback/9780691023670/the-computer-from-pascal-to-von-neumann
[book_grier_when_computers_were_human]: https://press.princeton.edu/books/paperback/9780691133829/when-computers-were-human
[book_mccartney_eniac]: https://openlibrary.org/works/OL2724030W/ENIAC
[book_mccoy_modern_exterior_ballistics]: https://openlibrary.org/works/OL10298553W/Modern_exterior_ballistics
[book_mindell_between_human_and_machine]: https://www.press.jhu.edu/books/title/2129/between-human-and-machine
[book_owens_bush_analyzer]: https://www.jstor.org/stable/25690567
[book_randell_origins_of_digital_computers]: https://link.springer.com/book/9781475705669

[ref_adele_goldstine]: https://www.seas.upenn.edu/about/history-heritage/eniac/
[ref_ford_instrument_mk1]: https://maritime.org/doc/computermk1/
[ref_kerrison_predictor]: https://collection.sciencemuseumgroup.org.uk/objects/co51067/predictor-no-3-mk-i-kerrison-anti-aircraft-fire-control-predictor
[ref_zuse_z3]: https://en.wikipedia.org/wiki/Z3_(computer)

[related_post_a237_framing_co_development]: {% post_url 2026-07-12-framing_and_the_co_development_mechanism %}

[research_aiken_hopper_1946]: https://ieeexplore.ieee.org/document/5222878
[research_bromley_1990]: https://ieeexplore.ieee.org/document/4638384
[research_bush_1931]: https://www.jstor.org/stable/24537568
[research_bush_caldwell_1945]: https://www.jstor.org/stable/24540537
[research_goldstine_goldstine_1946]: https://www.jstor.org/stable/2002620
[research_hartree_1935]: https://www.nature.com/articles/135940a0
[research_mauchly_1942]: https://en.wikipedia.org/wiki/John_Mauchly
[research_metropolis_nelson_1982]: https://ieeexplore.ieee.org/document/4640726
[research_moulton_1926]: https://openlibrary.org/works/OL15194913W/New_methods_in_exterior_ballistics
[research_rojas_1997]: https://ieeexplore.ieee.org/document/586074
[research_stibitz_1940]: https://ieeexplore.ieee.org/document/5222693
[research_thomson_1876]: https://royalsocietypublishing.org/doi/10.1098/rspl.1876.0038
