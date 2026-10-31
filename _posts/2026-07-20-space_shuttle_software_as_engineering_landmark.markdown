---
layout: post
mathjax: true
comments: true
title: "Aerospace, Programming Languages, and Information Technology Co-Development: Space Shuttle Software as Engineering Landmark"
date: 2026-07-20 09:00:00 +0000
categories: history technology aerospace
series: co_development_aerospace_computing
series_title: Aerospace, Programming Languages, and Information Technology Co-Development
series_index: 8
---

<!-- A244 -->
<script>console.log("A244");</script>

This eighth article of the twelve-part series covers the Space Shuttle primary avionics software system hereafter PASS as the first large-scale demonstration that safety-critical software could be built to airline-comparable reliability targets. The Shuttle software, developed at International Business Machines Corporation hereafter IBM Federal Systems Division under contract to National Aeronautics and Space Administration hereafter NASA between 1974 and the early 1980s and maintained through the program's operational life to 2011, established the engineering practices that the subsequent aerospace software tradition adopted as standard. HAL/S, the purpose-built aerospace programming language in which PASS was written, and the IBM Federal Systems Division software process, later formalized as the origin of what became the Capability Maturity Model, together supplied the engineering vocabulary that the discipline used for the following four decades.

The Space Shuttle software effort followed and drew on the Apollo Guidance Computer software effort treated in [A242][related_post_a242_apollo_guidance_computer]. Where the AGC software was written in assembly for a purpose-built 16-bit machine at approximately 36,000 lines of Colossus and 32,000 lines of Luminary, the Shuttle software was written in a high-level language for a general-purpose avionics computer at approximately 400,000 lines of HAL/S. The order-of-magnitude increase in software size crossed the threshold at which the Apollo assembly-language approach became infeasible and required the engineering discipline that the Shuttle program developed. The reliability record that the Shuttle software achieved, with no software-caused loss of vehicle across 135 missions between STS-1 in April 1981 and STS-135 in July 2011, established the empirical proposition that safety-critical software at this scale can be built to reliability targets comparable with commercial aviation.

## Shuttle Avionics Architecture

The Space Shuttle used a fault-tolerant avionics architecture with five general-purpose computers per orbiter, described comprehensively in the primary treatment by [Hanaway and Moorehead 1989][book_hanaway_moorehead_shuttle_avionics] as NASA Special Publication 504. Four of the five computers ran identical copies of PASS and voted on their outputs at each computational cycle. The fifth ran the Backup Flight System hereafter BFS, a separately developed program running dissimilar software developed by Rockwell International, the airframe contractor, on independently written code intended to protect against common-mode software errors in PASS. The redundancy-management technique used by the Shuttle computers is documented in the primary IBM Systems Journal paper by [Sklaroff 1976][research_sklaroff_1976]. The five-computer redundant architecture, treated at the reliability-analysis level in the framing article [A237][related_post_a237_framing_co_development], gave the Shuttle avionics fault tolerance against single computer hardware failures and against certain classes of common-mode software failures. The reliability of the four-computer PASS voting group under majority rule and independent-failure assumption is

$$
R_{\text{PASS vote}} = \sum_{i=3}^{4} \binom{4}{i} R^i (1 - R)^{4-i} = 4R^3 - 3R^4
\tag{1}
$$

which for per-machine hardware reliability $R = 0.99$ per mission gives group reliability of approximately 0.9994, or roughly one additional nine beyond a single machine. The value of the BFS as a fifth dissimilar-software element was to defend against the residual common-mode software failure fraction that voting cannot detect.

The computers were IBM AP-101 general-purpose machines, initially the AP-101B variant with 32-bit words, approximately 424,000 words of magnetic-core memory, and instruction rates of approximately 420,000 instructions per second, later upgraded through the AP-101S variant with substantially larger memory and faster execution as the Shuttle program's software requirements grew. The AP-101 was originally developed for military avionics applications and represented substantially more computing capability than the Apollo Guidance Computer described in [A242][related_post_a242_apollo_guidance_computer]. Comparing the two directly

$$
\frac{r_{\text{AP-101}}}{r_{\text{AGC}}} \approx \frac{420{,}000}{85{,}000} \approx 5
\tag{2}
$$

understates the practical capability difference because the AP-101 also had substantially larger word width, larger memory, floating-point hardware, and a mature software development toolchain, while the AGC required assembly programming with a specialized interpretive layer for vector and matrix operations.

The five computers communicated with each other and with the Shuttle's sensors and actuators through a serial data bus called the Multiplexer-Demultiplexer Data Bus. The bus operated at approximately one megabit per second with time-division multiple access among the connected units. Sensor data flowed from the vehicle instruments to the computers, computed commands flowed from the computers to the actuators, and inter-computer synchronization messages coordinated the four-way vote among the PASS computers. The engineering discipline of bus scheduling, bus fault detection, and bus recovery formed a substantial part of the Shuttle avionics engineering practice.

## The Primary Avionics Software System

PASS was developed by IBM Federal Systems Division at Owego, New York, under contract to NASA and to Rockwell International as the prime Shuttle contractor. The initial development period was approximately 1974 through 1980, culminating in the software delivery for the first orbital test flight STS-1 in April 1981. Peak development team size was approximately 250 engineers, and total development effort through the initial delivery was approximately 22,000 person-months, per the account in [Madden and Rone 1984][research_madden_rone_1984] previously cited in [A237][related_post_a237_framing_co_development]. Effective per-engineer productivity across the multi-year development satisfied approximately

$$
\bar{p}_{\text{PASS}} \approx \frac{L_{\text{initial}}}{E_{\text{total}}} \approx \frac{4 \times 10^{5} \text{ lines}}{2.2 \times 10^{4} \text{ person-months}} \approx 18 \text{ lines per person-month}
\tag{3}
$$

or roughly 220 lines per person-year, one to two orders of magnitude below the informal productivity of small commercial programs of the same era but consistent with the productivity figures for SAGE cited in [A240][related_post_a240_early_cold_war_sage] and reflective of the coordination-cost scaling from the Brooks law introduced in [A237][related_post_a237_framing_co_development]. Subsequent development through the operational life of the program added functionality for successive Shuttle missions and adapted to hardware upgrades and mission profile changes.

PASS occupied the four voting computers on each orbiter and provided the primary functional software for essentially all mission phases including launch, ascent guidance, on-orbit operations, deorbit, atmospheric entry, and landing. The mission-phase software modules called Operational Programs each contained approximately 100,000 to 200,000 lines of HAL/S, with only one Operational Program active at a time and the others loaded from mass storage as the mission progressed. This overlay approach was necessary because the AP-101 memory could not hold the complete mission software simultaneously, and the memory-management engineering to load and initialize an Operational Program without disrupting the flight-critical computation was itself a substantial engineering artifact.

The total PASS software base grew from approximately 400,000 source lines of HAL/S at STS-1 to approximately 500,000 to 600,000 source lines by the end of the operational program. This growth over approximately three decades of active development is consistent with the Lehman software-size growth law introduced in the [framing article][related_post_a237_framing_co_development], at approximately

$$
L(t) = L_0 \cdot 2^{(t - t_0) / T_L}
\tag{4}
$$

with doubling time $T_L$ of order 50 to 90 years for the PASS software specifically, substantially slower than the 6 to 8 year doubling time typical of major aerospace programs, reflecting the engineering discipline that Shuttle software adopted against uncontrolled growth.

## The Backup Flight System

The BFS was developed by Rockwell International separately from PASS with the requirement of protecting against common-mode software failures in PASS. The Rockwell team was organizationally isolated from the IBM PASS team, and the two teams were prohibited from sharing detailed design information. Both teams received the same NASA-supplied requirements specifications but implemented them independently. The BFS was substantially smaller than PASS, at approximately 90,000 lines of HAL/S, providing only the functionality required to complete an atmospheric entry and landing in the event of PASS failure. The BFS was silent during normal operation, monitoring the PASS output through the data bus without producing commands. If the crew engaged the BFS manually through a cockpit switch, the BFS took control and the PASS computers were disabled.

The STS-1 first launch experienced a notable software incident involving the BFS synchronization with the PASS computers. During the pre-launch sequence, the BFS was unable to synchronize its data-bus timing with the four PASS computers due to a timing race condition that occurred once per 67 initialization attempts, corresponding to a per-attempt failure probability of

$$
P_{\text{sync fail}} \approx \frac{1}{67} \approx 1.5 \text{ percent}
\tag{5}
$$

which is at the level where ground testing runs of order 10 to 30 attempts would more likely than not miss the failure by chance, and the 20 to 30 initialization tests that had been performed during pre-launch verification indeed had not encountered it. The launch was scrubbed on 10 April 1981 when the synchronization failure occurred, and the timing race was diagnosed and patched over the following two days. STS-1 launched successfully on 12 April 1981. The first-hand account of the incident from the NASA guidance officer involved is [Garman 1981][research_garman_1981] "The Bug Heard 'Round the World," a widely cited primary source in the aerospace software literature on race conditions and testing coverage.

The BFS design remained controversial within the aerospace software community throughout the Shuttle program. The argument for dissimilar redundant software was that common-mode failures in PASS would be caught by the differently implemented BFS. The counterargument, drawing on the Knight and Leveson 1986 empirical result cited in the [framing article][related_post_a237_framing_co_development], was that independently developed software versions exhibit statistically correlated failures at rates substantially higher than the independence assumption predicts, undermining the theoretical protection that dissimilar redundancy is supposed to provide. The Shuttle experience did not conclusively resolve this argument in either direction, but the decision by NASA and Rockwell to retain the BFS throughout the program indicated their operational judgment that the incremental protection justified the incremental cost.

## The HAL/S Programming Language

HAL/S was developed by Intermetrics under contract to NASA specifically for the Shuttle software program. The language design began in 1972 and the compiler was operational by 1974 in time for PASS development. The primary design paper is [Newkirk 1971][research_newkirk_1971] presenting HAL/S as a higher-order programming language for real-time aerospace applications. HAL/S was based on PL/I in its general syntax but added several features for aerospace applications including compile-time verification of array bounds, single-precision and double-precision floating-point primitives with explicit conversion, vector and matrix primitives as first-class types, real-time constructs for periodic tasks and interrupts, and a range of restrictions on constructs that the language designers considered dangerous for safety-critical use including recursion, dynamic memory allocation, and unstructured control flow. The design intent was to make the compiler enforce the coding standards that the Apollo team had enforced by manual review, reducing the reviewer burden and providing statically checked correctness properties.

HAL/S source was compiled to AP-101 machine code by a compiler that ran on IBM 360 mainframes at the IBM Federal Systems Division facility and later at NASA Johnson Space Center. Compilation cycle times of hours were typical for complete rebuilds of PASS, and the software configuration management practices for HAL/S source, compiled objects, and load-image files became a substantial engineering discipline in their own right. The HAL/S language was not adopted outside the Shuttle program. Subsequent aerospace software programs generally used Ada, C, or C++ rather than HAL/S because the NASA-Intermetrics implementation was not commercially available and because the Ada language treated in a later article of this series absorbed many of the safety features that had motivated HAL/S.

The load-bearing engineering property of HAL/S was that the compiler enforced the coding standards. Coding standards enforcement at compile time is substantially more reliable than coding standards enforcement by human review because the compiler applies the check to every line of every source file at every compilation, without fatigue and without variability. The class of errors that HAL/S made impossible at compile time included several categories that had caused problems in the Apollo assembly-language software, and the reduction in this class of errors was one of the factors that permitted the Shuttle software to scale to ten times the Apollo software size at comparable defect density.

## The IBM Federal Systems Division Software Process

The IBM Federal Systems Division software process for PASS became one of the most-studied examples of large-scale safety-critical software engineering. The process is described technically in the [Sperling and Weinstock 1985][research_sperling_weinstock_1985] paper, in the primary IBM Owego account by [Kolkhorst and Macina 1988][research_kolkhorst_macina_1988], and in the retrospective in [Fishman 1996][research_fishman_1996] published in Fast Company magazine, which supplied the defect-density figures that the aerospace software community subsequently cited for two decades.

The PASS defect density in delivered software was reported at approximately 0.11 defects per thousand lines of code for the initial STS-1 delivery and improved to approximately 0.004 defects per thousand lines of code for later releases, per the [Fishman 1996][research_fishman_1996] figures. Compared with commercial software of the same period at typical defect densities of 1 to 10 defects per thousand lines, the PASS software achieved defect densities two to four orders of magnitude lower. The improvement over time from 0.11 to 0.004 defects per thousand lines followed approximately

$$
D(t) = D_0 \cdot e^{-t / T_D}
\tag{6}
$$

with time constant $T_D$ of order 3 to 5 years, reflecting the process improvements that the IBM team introduced iteratively over the operational life of the program.

The process elements that produced these defect-density results included several practices later formalized as the origin of what became the Capability Maturity Model, whose intellectual foundation is documented in [Humphrey 1988][research_humphrey_1988] in IEEE Software as the characterizing paper on software process maturity. Formal design and code inspection following the procedure documented in [Fagan 1976][research_fagan_1976] at IBM Systems Journal caught approximately 60 percent of defects before they reached testing. If $D_{\text{introduced}}$ defects are introduced during design and coding, the residual defect count reaching testing under inspection efficiency $f_{\text{inspection}}$ is

$$
D_{\text{to test}} = D_{\text{introduced}} \cdot (1 - f_{\text{inspection}})
\tag{7}
$$

which for $f_{\text{inspection}} = 0.6$ reduces the testing load by 60 percent and, combined with the escalating cost of defect fix at successively later development phases per the approximate exponential

$$
C_{\text{fix}}(\text{phase}) \approx C_0 \cdot r^{n}
\tag{8}
$$

with cost multiplier $r$ of approximately 3 to 10 per phase and $n$ the phase-count offset from design, produces the engineering-economics argument for inspection that IBM used to justify the inspection cost. Configuration management tracked every change at the level of individual instructions. Formal specification of requirements and detailed design preceded implementation, with formal signoff between phases. Post-release defect analysis fed back into process improvement, with each defect traced to the process step that permitted its introduction and the process step revised to prevent recurrence.

## Reliability Record and Verification Cost

The operational Shuttle software achieved a reliability record across 135 missions between STS-1 in April 1981 and STS-135 in July 2011. Zero software-caused loss of vehicle occurred during the operational program. Zero software-caused loss of crew occurred. Aggregated across the average mission duration of approximately 200 hours, the operational record supplies an empirical Shuttle-software mean-time-between-catastrophic-failure lower bound of

$$
T_{\text{PASS, MTBF}} \gtrsim N_{\text{missions}} \cdot T_{\text{per mission}} \approx 135 \cdot 200 \approx 27{,}000 \text{ mission-hours}
\tag{9}
$$

with the true value bounded below only by the observed zero catastrophic failures rather than characterized by them, analogous to the AGC empirical MTBF treatment in [A242][related_post_a242_apollo_guidance_computer]. The two Shuttle losses that did occur, Challenger on 28 January 1986 during STS-51-L and Columbia on 1 February 2003 during STS-107, were caused by non-software factors including cold-weather effects on the solid rocket booster O-rings for Challenger and impact damage to the reinforced carbon-carbon leading edge for Columbia. Both losses were extensively investigated and neither implicated the Shuttle software. The operational reliability record for Shuttle software is one of the load-bearing empirical anchors in the aerospace software literature for the proposition that safety-critical software at this scale can be built to reliability targets comparable with commercial aviation.

The verification cost that produced this reliability was substantial. Total software development cost for the Shuttle program is variously estimated at approximately 500 million to 1 billion United States dollars in 1980s currency, or approximately 1 to 2 billion in current dollars. Divided across the approximately 400,000 lines of initial delivery, the per-line cost approaches

$$
C_{\text{per-line, PASS}} \approx \frac{5 \times 10^{8}}{4 \times 10^{5}} \approx 1{,}250 \text{ United States dollars per line}
\tag{10}
$$

on the low end of the cost estimate and approximately 2,500 dollars per line on the high end. The Boehm 1981 verification-effort scaling law introduced in the [framing article][related_post_a237_framing_co_development] with exponent $\gamma$ approximately 1.2 for safety-critical software gives verification cost as a fraction of total cost that consumed approximately 40 to 60 percent of the total development effort. These figures established the cost proposition that safety-critical software at this scale is expensive to produce but is nonetheless commercially viable given adequate mission value.

## Framework Application to Space Shuttle Software

The six-axis framework introduced in [A237][related_post_a237_framing_co_development] applies to Shuttle software with axis weightings reflecting the character of the largest aerospace safety-critical software program of the 1980s and the reference point against which subsequent programs including the Boeing 777 flight-control system and the F-35 Lightning II mission systems were later benchmarked.

The first axis is numerical computation demand. Shuttle software computed guidance solutions, control laws, sensor fusion, and displays at rates matching the flight-dynamics timescale. Total operation counts per mission were of order $10^{13}$ operations, roughly three orders of magnitude larger than the AGC's per-mission count treated in [A242][related_post_a242_apollo_guidance_computer], reflecting both the AP-101's higher instruction rate and the longer mission durations of the Shuttle era.

The second axis is real-time control. Shuttle software closed guidance and control loops at rates matching the flight-dynamics requirements of each mission phase, with control-loop rates typically 25 Hertz and guidance-loop rates typically 5 Hertz. The synchronous four-computer voting architecture imposed additional real-time constraints on inter-computer synchronization that were substantially tighter than the individual loop rates.

The third axis is reliability and verification. Shuttle software established the reliability standards that the subsequent safety-critical software tradition treated as the benchmark. The 0.004 defects per thousand lines figure for late-program releases remains a widely cited empirical anchor in the software engineering literature, though achieving it required verification investment substantially higher than commercial software programs sustain.

The fourth axis is networking and distribution. The Shuttle data bus at one megabit per second was a substantial distributed real-time system, though small by comparison with the ground-based networks treated in [A243][related_post_a243_arpanet_networking]. The engineering discipline of avionics data bus design, including deterministic scheduling and cross-computer synchronization, drew on and contributed to the broader real-time computing tradition treated in [A241][related_post_a241_aerospace_simulation].

The fifth axis is software engineering as a discipline. The IBM Federal Systems Division software process became one of the most-studied examples of industrial software engineering discipline. The practices formalized later as the Capability Maturity Model, and the measurement of defect density, verification cost, and process-improvement effectiveness that IBM tracked across the Shuttle program, supplied the empirical basis on which the subsequent large-scale software engineering discipline developed.

The sixth axis is semiconductor economics and dual-use. The AP-101 series was a general-purpose military avionics computer whose Shuttle use extended and refined the manufacturing base without originating it. The dual-use pattern that characterized the earlier Apollo program was less pronounced in the Shuttle era because the underlying computing capability had already been established for other applications.

## Conclusion

The Space Shuttle software was the first large-scale demonstration that safety-critical software could be built to airline-comparable reliability targets. The 400,000-line PASS software written in HAL/S at the IBM Federal Systems Division achieved defect densities two to four orders of magnitude below commercial software of the same period, and the operational program of 135 missions produced no software-caused loss of vehicle or crew across three decades of operation. The engineering practices that produced this record established the vocabulary that the subsequent safety-critical software tradition adopted as standard, including formal design and code inspection, phase-based development with formal signoff, systematic configuration management, and post-release defect analysis feeding back into process improvement. HAL/S as the purpose-built aerospace programming language for the Shuttle program illustrated the value of compiler-enforced coding standards, though HAL/S itself was not adopted beyond the Shuttle program because subsequent aerospace software adopted Ada and later C and C++ for the ecosystem-support and portability reasons that dictated commercial language selection.

The next article in the series treats safety-critical software as an engineering discipline in its own right, including industry consensus standards, formal verification adoption, model-based development, and the ongoing tension between waterfall and iterative processes in aerospace contexts.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 10 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 10, 5 are established and 5 are bespoke.
Reliabilities are probabilities per mission, defect densities are per thousand lines of source code, costs are in United States dollars of the 1980s unless the text states otherwise, and $T_L$ is a doubling time while $T_D$ is an e-folding time.

**Equation 1, Three of Four Majority Voting Reliability.**
Under independent failures the voting group survives when at least three of its four computers survive, and the binomial sum reduces to $4R^3 - 3R^4$.

$$
R_{\text{PASS vote}} = \sum_{i=3}^{4} \binom{4}{i} R^i (1 - R)^{4-i} = 4R^3 - 3R^4
\tag{1}
$$

**Equation 2, Instruction Rate Ratio of the AP-101 to the Apollo Guidance Computer.**
Dividing the instruction rate of the AP-101 by that of the Apollo Guidance Computer gives a raw speed advantage of about five.

$$
\frac{r_{\text{AP-101}}}{r_{\text{AGC}}} \approx \frac{420{,}000}{85{,}000} \approx 5
\tag{2}
$$

**Equation 3, Average Productivity of the Initial PASS Development.**
The delivered size of the Primary Avionics Software System divided by the reported development effort gives about eighteen lines per person-month.
[Madden and Rone 1984][research_madden_rone_1984]

$$
\bar{p}_{\text{PASS}} \approx \frac{L_{\text{initial}}}{E_{\text{total}}} \approx \frac{4 \times 10^{5} \text{ lines}}{2.2 \times 10^{4} \text{ person-months}} \approx 18 \text{ lines per person-month}
\tag{3}
$$

*Equation 4, Bespoke Exponential Growth of the PASS Code Base.*
The size of the code base is modelled as doubling at a constant rate, with a doubling time of fifty to ninety years that the article assigns to this program.

$$
L(t) = L_0 \cdot 2^{(t - t_0) / T_L}
\tag{4}
$$

**Equation 5, Per-Attempt Probability of the STS-1 Synchronisation Failure.**
A timing race that occurred once in sixty-seven initialisation attempts corresponds to a failure probability of about one and a half percent per attempt.
[Garman 1981][research_garman_1981]

$$
P_{\text{sync fail}} \approx \frac{1}{67} \approx 1.5 \text{ percent}
\tag{5}
$$

*Equation 6, Bespoke Exponential Decline of Defect Density.*
The fall in delivered defect density is modelled as an exponential decay with a time constant of three to five years that the article assumes.

$$
D(t) = D_0 \cdot e^{-t / T_D}
\tag{6}
$$

**Equation 7, Defects Escaping Inspection.**
Inspection that removes a fraction of the introduced defects leaves the complementary fraction to reach testing.
[Fagan 1976][research_fagan_1976]

$$
D_{\text{to test}} = D_{\text{introduced}} \cdot (1 - f_{\text{inspection}})
\tag{7}
$$

*Equation 8, Bespoke Geometric Escalation of Defect Repair Cost.*
The cost of repairing a defect is assumed to rise by a constant multiplier of three to ten for each development phase it survives.

$$
C_{\text{fix}}(\text{phase}) \approx C_0 \cdot r^{n}
\tag{8}
$$

*Equation 9, Bespoke Lower Bound on Time between Catastrophic Software Failures.*
The bound multiplies the one hundred and thirty-five missions flown without a catastrophic software failure by a representative mission duration of two hundred hours that the article assumes.

$$
T_{\text{PASS, MTBF}} \gtrsim N_{\text{missions}} \cdot T_{\text{per mission}} \approx 135 \cdot 200 \approx 27{,}000 \text{ mission-hours}
\tag{9}
$$

*Equation 10, Bespoke Development Cost per Line.*
The cost per line divides the low end of an unsourced range of program cost estimates, five hundred million dollars, by the four hundred thousand lines of the initial delivery.

$$
C_{\text{per-line, PASS}} \approx \frac{5 \times 10^{8}}{4 \times 10^{5}} \approx 1{,}250 \text{ United States dollars per line}
\tag{10}
$$

### Notation

- $R_{\text{PASS vote}}$, the reliability of the four-computer Primary Avionics Software System voting group
- $R$, the hardware reliability of one computer per mission
- $r_{\text{AP-101}}$, the instruction rate of the AP-101, in instructions per second
- $r_{\text{AGC}}$, the instruction rate of the Apollo Guidance Computer, in instructions per second
- $\bar{p}_{\text{PASS}}$, the mean productivity per engineer
- $L_{\text{initial}}$, the source lines of the initial delivery
- $E_{\text{total}}$, the total development effort in person-months
- $L(t)$, the source lines at time $t$
- $L_0$, the source lines at the reference time $t_0$
- $T_L$, the doubling time of the code base
- $P_{\text{sync fail}}$, the probability that one initialisation attempt fails to synchronise
- $D(t)$, the delivered defect density at time $t$
- $D_0$, the initial defect density
- $T_D$, the e-folding time of the decline
- $D_{\text{to test}}$, the defects that reach testing
- $D_{\text{introduced}}$, the defects introduced during design and coding
- $f_{\text{inspection}}$, the fraction of defects that inspection removes
- $C_0$, the cost of a repair in the design phase
- $r$, the cost multiplier per phase
- $n$, the number of phases after design
- $T_{\text{PASS, MTBF}}$, the mean time between catastrophic failures of the Shuttle software
- $N_{\text{missions}}$, the number of missions flown
- $T_{\text{per mission}}$, the mean mission duration in hours
- $C_{\text{per-line, PASS}}$, the development cost per source line

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Kolkhorst, B. G., and A. J. Macina. 1988. "Developing Error-Free Software." *IEEE Aerospace and Electronic Systems Magazine* 3 (11): 25–31. [https://doi.org/10.1109/62.17928][research_kolkhorst_macina_1988]

### Primary Sources, Non-Peer-Reviewed

- Fagan, M. E. 1976. "Design and Code Inspections to Reduce Errors in Program Development." *IBM Systems Journal* 15 (3): 182–211. [https://doi.org/10.1147/sj.153.0182][research_fagan_1976]
- *HAL/S Language Specification*. n.d. [https://ntrs.nasa.gov/citations/19790018664][ref_hals_spec]
- Hanaway, John F., and Robert W. Moorehead. 1989. *Space Shuttle Avionics System*. NASA-SP-504. NASA. [https://ntrs.nasa.gov/citations/19900015844][book_hanaway_moorehead_shuttle_avionics]
- Madden, William A., and Kyle Y. Rone. 1984. "Design, Development, Integration: Space Shuttle Primary Flight Software System." *Communications of the ACM* 27 (9): 914–25. [https://doi.org/10.1145/358234.358254][research_madden_rone_1984]
- *NASA Shuttle Avionics*. n.d. [https://ntrs.nasa.gov/citations/19910023576][ref_nasa_shuttle_avionics]
- Newkirk. 1971. *\[Title not identified\]*. [https://ntrs.nasa.gov/citations/19730015690][research_newkirk_1971]
- Tomayko, James E. 1987. *Computers in Spaceflight: The NASA Experience*. NASA-CR-182505. NASA. [https://ntrs.nasa.gov/citations/19880069935][book_tomayko_shuttle_software]

### General Sources

- Fishman. 1996. "\[Title not identified\]." Accessed October 25, 2026. [https://www.fastcompany.com/28121/they-write-right-stuff][research_fishman_1996]
- Garman. 1981. "\[Title not identified\]." Accessed October 25, 2026. [https://dl.acm.org/doi/10.1145/1005944.1005948][research_garman_1981]
- Humphrey. 1988. "\[Title not identified\]." Accessed October 25, 2026. [https://ieeexplore.ieee.org/document/2014][research_humphrey_1988]
- Sklaroff. 1976. "Authors." Accessed October 25, 2026. [https://ieeexplore.ieee.org/document/5388349][research_sklaroff_1976]
- Sperling and Weinstock. 1985. "Wages through the Ages: The Influence of Technology on the Standard of Living." Accessed October 25, 2026. [https://ieeexplore.ieee.org/document/5010028][research_sperling_weinstock_1985]

### Tertiary Sources

- "Lockheed Martin Systems Integration – Owego." 2026. Wikipedia. Last modified June 30, at 07:27 (UTC). [https://en.wikipedia.org/w/index.php?title=Lockheed\_Martin\_Systems\_Integration\_%E2%80%93\_Owego&oldid=1361815407][ref_ibm_fsd]

### Related Posts

- Sechter, Brendan. 2026. "Aerospace, Programming Languages, and Information Technology Co-Development: Framing and the Co-Development Mechanism." *Brendan A R Sechter's Development Blog*, July 13. [https://sgeos.github.io/history/technology/aerospace/2026/07/13/framing\_and\_the\_co\_development\_mechanism.html][related_post_a237_framing_co_development]
- Sechter, Brendan. 2026. "Aerospace, Programming Languages, and Information Technology Co-Development: Early Cold War Air Defense and SAGE." *Brendan A R Sechter's Development Blog*, July 16. [https://sgeos.github.io/history/technology/aerospace/2026/07/16/early\_cold\_war\_air\_defense\_and\_sage.html][related_post_a240_early_cold_war_sage]
- Sechter, Brendan. 2026. "Aerospace, Programming Languages, and Information Technology Co-Development: Aerospace Simulation and Real-Time Systems." *Brendan A R Sechter's Development Blog*, July 17. [https://sgeos.github.io/history/technology/aerospace/2026/07/17/aerospace\_simulation\_and\_real\_time\_systems.html][related_post_a241_aerospace_simulation]
- Sechter, Brendan. 2026. "Aerospace, Programming Languages, and Information Technology Co-Development: The Apollo Guidance Computer." *Brendan A R Sechter's Development Blog*, July 18. [https://sgeos.github.io/history/technology/aerospace/2026/07/18/apollo\_guidance\_computer.html][related_post_a242_apollo_guidance_computer]
- Sechter, Brendan. 2026. "Aerospace, Programming Languages, and Information Technology Co-Development: ARPANET and Networking Origins." *Brendan A R Sechter's Development Blog*, July 19. [https://sgeos.github.io/history/technology/aerospace/2026/07/19/arpanet\_and\_networking\_origins.html][related_post_a243_arpanet_networking]

[book_hanaway_moorehead_shuttle_avionics]: https://ntrs.nasa.gov/citations/19900015844
[book_tomayko_shuttle_software]: https://ntrs.nasa.gov/citations/19880069935
[ref_hals_spec]: https://ntrs.nasa.gov/citations/19790018664
[ref_ibm_fsd]: https://en.wikipedia.org/w/index.php?title=Lockheed_Martin_Systems_Integration_%E2%80%93_Owego&oldid=1361815407
[ref_nasa_shuttle_avionics]: https://ntrs.nasa.gov/citations/19910023576
[related_post_a237_framing_co_development]: {% post_url 2026-07-13-framing_and_the_co_development_mechanism %}
[related_post_a240_early_cold_war_sage]: {% post_url 2026-07-16-early_cold_war_air_defense_and_sage %}
[related_post_a241_aerospace_simulation]: {% post_url 2026-07-17-aerospace_simulation_and_real_time_systems %}
[related_post_a242_apollo_guidance_computer]: {% post_url 2026-07-18-apollo_guidance_computer %}
[related_post_a243_arpanet_networking]: {% post_url 2026-07-19-arpanet_and_networking_origins %}
[research_fagan_1976]: https://doi.org/10.1147/sj.153.0182
[research_fishman_1996]: https://www.fastcompany.com/28121/they-write-right-stuff
[research_garman_1981]: https://dl.acm.org/doi/10.1145/1005944.1005948
[research_humphrey_1988]: https://ieeexplore.ieee.org/document/2014
[research_kolkhorst_macina_1988]: https://doi.org/10.1109/62.17928
[research_madden_rone_1984]: https://doi.org/10.1145/358234.358254
[research_newkirk_1971]: https://ntrs.nasa.gov/citations/19730015690
[research_sklaroff_1976]: https://ieeexplore.ieee.org/document/5388349
[research_sperling_weinstock_1985]: https://ieeexplore.ieee.org/document/5010028
