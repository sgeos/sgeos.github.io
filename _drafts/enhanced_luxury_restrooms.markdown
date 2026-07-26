---
layout: post
mathjax: true
comments: true
title:  "Enhanced and Luxury Restrooms: Elevating the Elimination Facility"
date:   2026-01-18 00:00:00 +0000
categories: culture architecture design
series: enhanced_luxury_facilities
series_title: Enhanced and Luxury Facilities
series_index: 1
---

<!-- A293 -->
<script>console.log("A293");</script>

This article is the first in the Enhanced and Luxury Facilities series and treats the elimination facility, the restroom, as an object of design elevation rather than as a fixed utilitarian minimum. The series treats two facility classes that serve universal somatic necessities. The present article treats elimination facilities, and the companion article that follows treats immersion and bathing facilities. The organizing claim of the series is that facilities serving a universal bodily necessity are elevated from a utilitarian minimum toward an enhanced and luxury experience along a common ladder of value dimensions, and that the restroom and the bath are the two poles of a single category of somatic-maintenance architecture rather than two unrelated building types. This article introduces the six-dimension facility-elevation framework that both articles apply, walks the history of the elimination facility from the Roman public latrine through the Victorian public convenience and the contemporary high-technology washroom, and closes with an explicit pattern-extraction section that states the abstract elevation mechanic in a form other readers can recognize in adjacent facility contexts without naming any specific downstream application.

The register of the article is descriptive and analytical rather than promotional. The history supplies the dates, the sites, the fixtures, the standards, and the quantitative apparatus that a comprehensive treatment of the elimination facility requires. The framework supplies the abstract account of what elevation consists of, dimension by dimension. The two registers are complementary. A reader interested only in the history will find a comprehensive reference history of the restroom. A reader interested in the abstract mechanic will find each historical development mapped to the dimension of the framework it advances.

## The Facility-Elevation Mapping Problem

The mapping problem for a treatment of the elimination facility is the question of which specific architectural, mechanical, acoustic, hygienic, logistical, and social arrangements distinguish an elevated elimination facility from a utilitarian one, and whether those arrangements admit a common abstract description across the very different facility instances that the history exhibits. The Roman public latrine, the medieval garderobe, the Victorian public convenience, the mid-century commercial restroom, and the contemporary Japanese high-technology washroom differ so completely in fixture, in material, and in social meaning that a naive account would treat them as unrelated. The mapping problem asks whether a single framework recovers what all elevated instances share.

The problem admits several formalizations depending on the analytical tradition consulted. The public-health tradition treats the elimination facility primarily as an instrument of pathogen containment, and treats elevation as the progressive reduction of disease transmission through sanitation engineering. The architectural tradition treats the facility as a designed room whose elevation is a matter of material, proportion, light, and finish. The service-operations tradition treats the facility as a throughput system whose elevation is a matter of capacity, waiting, and provisioning under stochastic demand. The anthropological tradition treats the facility as a site of ritual and social meaning whose elevation is bound up with privacy norms, status display, and the cultural management of the body. The present article draws on all four traditions and organizes them through a single framework of six dimensions, so that each tradition supplies the operationalization of one or more dimensions rather than competing for the whole account.

## Methodological Commitments

The article adopts several methodological commitments that govern the treatment throughout.

The first commitment is to descriptive history before pattern extraction. The article establishes the dates, sites, fixtures, and standards of the elimination facility as a matter of record before it states the abstract mechanic those facts embody. The pattern-extraction section is confined to the close of the article and is clearly marked.

The second commitment is to primary and institutional sources where they exist. Building codes, plumbing standards, public-health guidance, museum documentation, and manufacturer technical specification are preferred over secondary summary. Where a secondary source is cited, the citation is marked as trade press or as journalism in the reference list category.

The third commitment is to quantitative operationalization where the material supports it. The dimensions of the framework that admit formal models, in particular the throughput dimension and the acoustic and thermal comfort dimensions, are given explicit models with defined variables. The dimensions that resist formal models, in particular the social-signification dimension, are treated descriptively and are not forced into a false precision.

The fourth commitment is to the separation of the biological from the cultural in the treatment of sex-based differences. The article distinguishes the differences in elimination-facility provision and design that follow from anatomical and physiological fact, in particular differences in mean occupancy time and in fixture compatibility, from the differences that follow from cultural convention. The distinction is stated explicitly wherever the two are liable to be conflated.

## The Six-Dimension Facility-Elevation Framework

The framework organizes the elevation of a somatic-maintenance facility into six dimensions. The dimensions are presented here in the abstract and are applied to the elimination facility in the sections that follow. The companion article applies the same six dimensions to the immersion facility.

The first dimension is hygienic sufficiency. Hygienic sufficiency is the health and sanitation floor of the facility. It comprises the containment and removal of waste, the interruption of pathogen transmission, the control of aerosol and surface contamination, and the provision of hand hygiene. Hygienic sufficiency is the non-negotiable base of the framework. Elevation along the other five dimensions is legible as elevation only once hygienic sufficiency is satisfied, because a facility that fails the sanitation floor is not experienced as luxurious regardless of its finish.

The second dimension is discretion and privacy. Discretion and privacy is the management of a private bodily act performed in a shared or serviced space. It comprises acoustic masking of the sounds of elimination, visual sightline control through partition and layout, and olfactory dilution through ventilation. The discretion dimension is the dimension along which the elimination facility differs most sharply from most other building types, because the act the facility serves is one that privacy norms across most cultures require to be concealed.

The third dimension is sensory and aesthetic enrichment. Sensory enrichment comprises the material, the proportion, the illumination, the acoustic character, the scent, and the thermal comfort of the facility considered as a designed environment. Sensory enrichment is the dimension along which luxury is most visibly signaled, because it is the dimension a visitor perceives immediately and consciously.

The fourth dimension is throughput and access equity. Throughput comprises the capacity of the facility to serve its demand without excessive waiting, the provisioning of consumable supply, and the equitable distribution of capacity across the populations the facility serves. The throughput dimension is the dimension most amenable to formal quantitative modeling, because arrivals to a facility and the service they require admit description as a stochastic queueing system.

The fifth dimension is social and ritual signification. Social signification comprises the communal meaning of the facility, the ritual that surrounds its use, the status the facility signals, and the willingness of a user to pay for access. The elimination facility carries less social signification than the immersion facility that the companion article treats, but it carries more than a naive account would suppose, because the provision of an elevated restroom is a status signal on the part of the establishment that provides it.

The sixth dimension is technological augmentation. Technological augmentation comprises the mechanized and automated capability that extends the base function of the facility beyond the manual minimum. In the elimination facility the augmentation dimension includes the washlet and its cleansing and drying functions, the automatic sound-masking device, the touchless fixture, and the vending and dispensing machine.

The six dimensions admit aggregation into a scalar elevation index. Let $x_H, x_P, x_S, x_T, x_R, x_A$ denote the normalized scores of a facility on the six dimensions, each scaled to the unit interval $[0, 1]$. The gating role of hygienic sufficiency is captured by a saturating gate function

$$\Phi(x_H) = \frac{x_H}{x_H + h_0}$$

with $h_0 > 0$ a half-saturation constant that sets the hygienic level at which the gate reaches one half. The elevation index is then the gated weighted aggregate of the remaining five dimensions,

$$E = \Phi(x_H) \cdot \sum_{d \in \{P, S, T, R, A\}} w_d \, x_d$$

with nonnegative weights $w_d$ that sum to one. The gate encodes the framework commitment that hygienic failure suppresses the perceived elevation of a facility regardless of its scores on the enrichment dimensions, because $\Phi(x_H) \to 0$ as $x_H \to 0$ drives $E \to 0$ irrespective of the bracketed sum.

The additive aggregate within the bracket admits a substitution-elastic generalization when the analyst wishes to model complementarity among the enrichment dimensions rather than pure substitutability. The constant-elasticity-of-substitution form

$$E_{\text{CES}} = \Phi(x_H) \cdot \left( \sum_{d \in \{P, S, T, R, A\}} w_d \, x_d^{\rho} \right)^{1/\rho}$$

recovers the additive aggregate as $\rho \to 1$, the geometric aggregate as $\rho \to 0$, and the Leontief minimum as $\rho \to -\infty$. The geometric limit

$$E_{\text{geo}} = \Phi(x_H) \cdot \prod_{d \in \{P, S, T, R, A\}} x_d^{w_d}$$

is the appropriate choice when the analyst holds that a facility scoring near zero on any single enrichment dimension cannot be experienced as elevated, because a single vanishing factor drives the product to zero.

## Throughput and Access Equity as an Economic Property

The throughput dimension of the framework admits the most complete formal treatment, because the arrival of users to an elimination facility and the time each user occupies a fixture together constitute a stochastic service system of the kind that queueing theory describes. The treatment in this section supplies the quantitative apparatus that the potty-parity discussion later in the article applies to the specific question of sex-based provision.

Model the facility as a service system with $c$ interchangeable fixtures. Users arrive according to a Poisson process of rate $\lambda$, so that the number of arrivals in a time interval is Poisson-distributed and the interarrival times are exponential with mean $1/\lambda$. Each user occupies a fixture for a service time with mean $1/\mu$, so that $\mu$ is the per-fixture service rate. The offered load is the dimensionless quantity

$$a = \frac{\lambda}{\mu}$$

measured in erlangs, and the utilization of the facility is

$$\rho = \frac{a}{c} = \frac{\lambda}{c \mu}$$

which must satisfy $\rho < 1$ for the system to be stable, because a utilization at or above one implies an unbounded growth of the waiting line. Under the assumption of exponential service the system is the $M/M/c$ queue, whose stationary behavior is exactly solvable and is treated in the standard references of the field from [Erlang 1917][research_erlang_1917] through [Kleinrock 1975][book_kleinrock_1975_queueing] Queueing Systems and [Shortle and colleagues 2018][book_shortle_2018_queueing] Fundamentals of Queueing Theory.

The stationary distribution of the number in the system begins with the probability that the system is empty,

$$P_0 = \left[ \sum_{k=0}^{c-1} \frac{a^k}{k!} + \frac{a^c}{c! \, (1 - \rho)} \right]^{-1}$$

the normalizing constant of the birth-death process, in terms of which the probability that an arriving user must wait, because all $c$ fixtures are occupied at the moment of arrival, is given by the Erlang-C formula

$$C(c, a) = \frac{a^c}{c! \, (1 - \rho)} \, P_0 = \frac{\dfrac{a^c}{c! \, (1 - \rho)}}{\displaystyle\sum_{k=0}^{c-1} \frac{a^k}{k!} + \frac{a^c}{c! \, (1 - \rho)}}$$

which is the central quantity of the throughput dimension, because it is the probability that a user encounters a queue rather than an available fixture. The waiting time itself is not merely characterized by its mean, because the full distribution of the queueing delay is the exponential tail

$$P(W_q > t) = C(c, a) \, e^{-c \mu (1 - \rho) \, t}$$

which shows that the fraction of users waiting longer than a tolerance $t$ falls exponentially in the tolerance at a rate set by the surplus service capacity $c \mu (1 - \rho)$. The elevated facility may therefore be specified not by a mean-wait target but by a tail target, that no more than a small fraction of users wait longer than a stated tolerance, which is the appropriate service-level criterion when the perceived quality of the facility is set by the worst experience rather than the average one.

The full stationary distribution of the number of users in the system follows from the same birth-death balance. The probability of finding exactly $n$ users present is

$$P_n = \begin{cases} \dfrac{a^n}{n!} \, P_0, & 0 \leq n < c \\[2mm] \dfrac{a^n}{c! \, c^{\,n-c}} \, P_0, & n \geq c \end{cases}$$

so that the occupancy below the fixture count follows a truncated Poisson form and the occupancy above it decays geometrically at ratio $\rho$. The mean number in the system recovers by summation as $L = L_q + a$, the queue content plus the mean number in service, which is Little's law applied to the whole system.

A distinct provisioning regime arises when a user who finds every fixture occupied does not wait but departs, whether to another facility or without service, which is the loss regime rather than the delay regime. Under the loss regime the relevant quantity is the Erlang-B blocking probability

$$B(c, a) = \frac{\dfrac{a^c}{c!}}{\displaystyle\sum_{k=0}^{c} \frac{a^k}{k!}}$$

the probability that all $c$ fixtures are occupied at an arrival, which is the fraction of demand the facility turns away. The loss regime describes the facility whose users will not queue, and the elevated facility that serves an impatient clientele is provisioned against the Erlang-B blocking probability rather than the Erlang-C waiting time, holding the blocking probability below a small target so that the facility rarely turns a user away.

The exponential-service assumption of the Erlang models is an idealization, because measured fixture-occupancy times are closer to a lognormal distribution with a variance the exponential form overstates. The general-service correction of the Kingman approximation adjusts the expected wait of the exponential model by the ratio of the actual service-time variability to the exponential baseline,

$$W_q^{G/G/c} \approx W_q^{M/M/c} \cdot \frac{C_a^2 + C_s^2}{2}$$

with $C_a$ and $C_s$ the coefficients of variation of the interarrival and service times, so that a service process less variable than the exponential, for which $C_s < 1$, yields a shorter wait than the Erlang model predicts. The correction shows that the Erlang results are conservative for the real facility, and that the provisioning derived from them errs toward surplus rather than shortfall, which is the prudent direction of error for a facility whose failure is publicly visible. The expected waiting time in the queue, exclusive of service, follows from the Erlang-C probability as

$$W_q = \frac{C(c, a)}{c \mu - \lambda} = \frac{C(c, a)}{c \mu (1 - \rho)}$$

and the expected number of users waiting in the queue follows from Little's law, the fundamental conservation relation of queueing theory established by [Little 1961][research_little_1961],

$$L_q = \lambda \, W_q$$

which states that the time-average number in the queue equals the arrival rate multiplied by the average time each user spends in the queue and holds for any arrival and service law in steady state, not only for the exponential case. The total expected time in the system, including service, is

$$W = W_q + \frac{1}{\mu}$$

and the total expected number in the system follows both from a second application of Little's law and from the decomposition into the queue content and the number in service,

$$L = \lambda W = L_q + a$$

which expresses the conservation of users across the waiting and service phases of the system.

The sensitivity of the expected wait to the utilization is the property that makes provisioning consequential. As $\rho \to 1$ the factor $1/(1 - \rho)$ in the waiting-time expression diverges, so that the expected wait grows without bound as the facility approaches saturation. A facility provisioned for a utilization of one half exhibits modest waiting, while a facility provisioned for a utilization of nine tenths exhibits waiting an order of magnitude larger under otherwise identical parameters. Elevation along the throughput dimension is, in the first place, the provisioning of a fixture count $c$ sufficient to hold the utilization well below saturation at the peak arrival rate the facility experiences.

The peak arrival rate rather than the mean arrival rate governs the required provisioning, because the demand on many elimination facilities is sharply time-varying. A facility attached to a theater, a stadium, or a transit terminal experiences arrival rates during an intermission or an event egress that exceed the daily mean by a large multiple. Let $\lambda_{\text{peak}} = \beta \lambda_{\text{mean}}$ with a peaking factor $\beta > 1$. The fixture count required to hold the peak utilization below a target $\rho^{\star}$ is

$$c \geq \frac{\beta \lambda_{\text{mean}}}{\mu \, \rho^{\star}}$$

which shows that the required provisioning scales linearly in the peaking factor. A facility designed to the mean rather than to the peak fails precisely at the moments of heaviest demand, which are the moments at which the failure is most visible.

The provisioning problem admits a compact heuristic in the square-root staffing rule, which states that the fixture count required to hold a target probability of delay under offered load $a$ is approximately

$$c \approx a + \beta \sqrt{a}$$

with $\beta$ a service-grade constant that increases with the stringency of the delay target. The rule expresses the economy of scale of shared service, because the safety margin $\beta \sqrt{a}$ grows only as the square root of the load, so that a larger facility serving a larger load requires proportionally fewer surplus fixtures above the offered load than a smaller facility serving a smaller load. The economy of scale is one reason the consolidated restroom of a large establishment can achieve a lower waiting time at a lower fractional over-provisioning than the scattered small restrooms of a fragmented one.

The choice of the fixture count admits formalization as a cost minimization. Let $\kappa$ denote the amortized capital and operating cost per fixture, inclusive of the floor area the fixture occupies, and let $\gamma$ denote the monetized value of a unit of user waiting time. The total cost is the sum of the fixture cost and the aggregate waiting cost,

$$\min_{c} \; \Big[ \, c \, \kappa + \gamma \, \lambda \, W_q(c) \, \Big]$$

which is convex in $c$, because the fixture cost rises linearly while the waiting cost falls convexly as fixtures are added, so that an interior optimum $c^{\star}$ balances the marginal fixture cost against the marginal waiting saving. The elevated facility is characteristically one whose operator assigns a high value to $\gamma$, whether because the facility serves a clientele whose time is valuable or because the operator treats the absence of a queue as a component of the experience it sells, and therefore provisions beyond the point a minimal-cost public facility would choose.

The throughput dimension also admits a spatial efficiency measure in the served demand per unit floor area,

$$\Theta = \frac{c \, \mu \, \rho^{\star}}{A_{\text{floor}}}$$

with $\rho^{\star}$ the utilization at the target service level and $A_{\text{floor}}$ the floor area of the facility. The measure captures the tension between the throughput dimension and the sensory-enrichment dimension, because the generous fixture spacing, the lounge area, and the circulation width that advance sensory enrichment reduce the served demand per unit area, so that an elevated facility trades spatial throughput efficiency for experiential quality.

## Sex-Based Provision and the Potty-Parity Problem

The potty-parity problem is the observation that equal provision of elimination facilities to the sexes, measured by equal floor area or by equal fixture count, produces unequal waiting, and the analysis of what equal provision should mean once the asymmetry is acknowledged. The problem is a direct application of the queueing apparatus of the preceding section, and it is the clearest instance in the elimination-facility context of a sex-based difference that follows in part from physiological fact rather than from convention alone.

The asymmetry has several compounding sources. The mean occupancy time of a fixture differs by sex. The published measurements of restroom occupancy time, including the systematic comparison of [Rawls 1988][research_rawls_1988], report that the mean female occupancy time exceeds the mean male occupancy time by a factor commonly estimated between 1.5 and 2, arising from differences in clothing management, from the higher incidence of accompaniment by children, from the absence of a urinal option that shortens the male mean, and from menstrual-hygiene management. Denote the male service rate $\mu_m$ and the female service rate $\mu_w$, with $\mu_w < \mu_m$ reflecting the longer female mean occupancy time. Denote a common arrival rate $\lambda$ per sex, taken equal here to isolate the service-time asymmetry, and denote the fixture counts $c_m$ and $c_w$.

Equal floor area translated into equal fixture count sets $c_m = c_w = c$. Under equal fixture count the female offered load $a_w = \lambda / \mu_w$ exceeds the male offered load $a_m = \lambda / \mu_m$, so that the female utilization $\rho_w = a_w / c$ exceeds the male utilization $\rho_m = a_m / c$. Because the expected wait is increasing and convex in utilization, the female expected wait exceeds the male expected wait, and the excess grows sharply as the common provision approaches the female saturation point. The ratio of the female to the male expected wait under equal provision is

$$\frac{W_{q,w}}{W_{q,m}} = \frac{C(c, a_w)}{C(c, a_m)} \cdot \frac{1 - \rho_m}{1 - \rho_w}$$

which exceeds the service-time ratio $\mu_m / \mu_w$ by the convex amplification of the utilization factors, so that a service-time asymmetry of a factor near two produces a wait asymmetry far larger as the female utilization approaches one. This convex amplification is the quantitative core of the observed disparity between the female and the male restroom queue. The observed asymmetry of restroom queues, in which the female queue is long while the male queue is short, is the direct consequence.

Parity properly understood is the equalization of an outcome rather than of an input. Two natural parity criteria present themselves. The first is equalization of the expected wait, which requires fixture counts $c_m$ and $c_w$ satisfying

$$W_q(c_m, a_m) = W_q(c_w, a_w)$$

with $W_q$ the Erlang-C waiting time of the preceding section. The second is equalization of the utilization, which requires

$$\frac{\lambda}{c_m \mu_m} = \frac{\lambda}{c_w \mu_w} \quad\Longrightarrow\quad \frac{c_w}{c_m} = \frac{\mu_m}{\mu_w}$$

so that the ratio of required female fixtures to male fixtures equals the ratio of male to female service rate, which is the ratio of female to male mean occupancy time. Under the empirical occupancy-time ratio the utilization-parity criterion requires roughly 1.5 to 2 times as many female fixtures as male fixtures to equalize the utilization, and the wait-parity criterion requires a comparable or larger ratio because the wait is convex in utilization. The building-code response, in the form of the revised fixture-ratio tables of the [International Plumbing Code][ref_ipc_fixture_403] and the [Uniform Plumbing Code][ref_upc_fixtures] and the potty-parity statutes discussed in the historical treatment below, is an institutional approximation to this balancing condition. The formal analysis of the parity problem in the planning and operations literature, from the review of [Anthony and Dufresne 2007][research_anthony_dufresne_2007] through the queueing treatment of [Huh and colleagues 2019][research_huh_2019_potty], confirms that fixture equality does not deliver waiting equality, and the flexibility analysis of [Farajollahzadeh and Hu][research_farajollahzadeh_hu_potty], with its stadium-design case study [Farajollahzadeh and colleagues 2025][research_farajollahzadeh_stadium], shows that pooling capacity through all-gender provision reduces the disparity by the same mechanism that pooling reduces waiting in any shared-server queue. The empirical asymmetry that drives the analysis is documented in the measurement of [whether women spend more time in the restroom than men][research_do_women_spend_more], and the broader gendered-time-cost framing is developed in the recent scholarship [beyond potty parity][research_beyond_potty_parity] and in the [feminist critical analysis of public toilets and gender][research_feminist_critical].

The potty-parity analysis illustrates the general point that access equity, the fourth dimension of the framework, is not achieved by symmetric provision when the populations served differ in their service requirements. Equity in outcome requires asymmetric provision calibrated to the asymmetry in demand. The point recurs in the companion article in the treatment of sex-segregated bathing, where the asymmetry takes a different form.

## Discretion and Privacy as an Acoustic and Olfactory Property

The discretion dimension of the framework admits formal treatment along its acoustic and its olfactory axes. The acoustic axis concerns the concealment of the sounds of elimination, and the olfactory axis concerns the dilution and removal of odor. Both axes reduce to mass-and-energy transport problems that admit standard models.

The acoustic environment of a restroom is governed in the first place by its reverberation. The restroom is characteristically a hard-surfaced room, finished in tile, porcelain, stone, and glass, whose surfaces absorb little sound. The reverberation time, defined as the time for the sound energy density to decay by sixty decibels after a source ceases, is given for a diffuse field by the Sabine relation established in the founding work of architectural acoustics by [Sabine 1922][book_sabine_1922_acoustics] and treated in the modern references such as [Long 2006][book_long_2006_architectural_acoustics] Architectural Acoustics,

$$T_{60} = \frac{0.161 \, V}{A}$$

in metric units, with $V$ the room volume in cubic meters and $A$ the total absorption in metric sabins. The total absorption is the sum over the room surfaces of the surface area multiplied by its absorption coefficient,

$$A = \sum_i S_i \, \alpha_i$$

with $S_i$ the area of surface $i$ and $\alpha_i$ its absorption coefficient, a dimensionless quantity between zero and one. The Sabine relation assumes a nearly uniform and moderate absorption, and where the absorption is high or unevenly distributed the Eyring correction

$$T_{60} = \frac{0.161 \, V}{-S \ln(1 - \bar{\alpha})}$$

with $S$ the total surface area and $\bar{\alpha} = A / S$ the mean absorption coefficient supplies the more accurate estimate, reducing to the Sabine form in the limit of small mean absorption. The hard finishes characteristic of the restroom carry absorption coefficients near a few hundredths, so that the total absorption is small and the reverberation time is long. A long reverberation time sustains and spreads the sounds of elimination, which is precisely the acoustic outcome the discretion dimension seeks to prevent. Elevation along the acoustic axis therefore begins with the introduction of absorption, whether through acoustic ceiling treatment, through sound-absorbing partition material, or through soft furnishing in the serviced restroom.

The concealment of a specific sound against a background is a masking problem. Let $L_s$ denote the sound-pressure level of the elimination sound to be concealed and $L_m$ denote the level of a masking sound introduced deliberately. The detectability of the target against the masker is governed by the signal-to-masker ratio

$$\text{SMR} = L_s - L_m$$

so that a sufficiently loud and spectrally appropriate masker drives the signal-to-masker ratio below the detection threshold and renders the target sound inaudible. The masking is most efficient when the masker occupies the same critical bands as the target, because auditory masking is strongest within a critical band.

The intelligibility of a concealed sound against a background is quantified by the articulation index, standardized as the speech intelligibility index in [ANSI and the Acoustical Society of America S3.5][ref_ansi_asa_s35_sii] and applied to the measurement of speech privacy in [ASTM E1130][ref_astm_e1130]. The index is a band-weighted aggregate of the clipped signal-to-noise ratio,

$$\text{AI} = \sum_k W_k \, \frac{\big[\, \text{SNR}_k + 12 \,\big]_0^{30}}{30}$$

with $W_k$ the importance weight of frequency band $k$, $\text{SNR}_k = L_{s,k} - L_{n,k}$ the signal-to-noise ratio in the band, and the bracket denoting truncation to the interval from zero to thirty decibels. A concealed sound is intelligible as the index approaches one and private as it approaches zero. A masking device raises the effective background in each band, and the combined level of the ambient noise and the added masker is the energy sum

$$L_{n,k}^{\text{tot}} = 10 \log_{10}\!\Big( 10^{L_{n,k}/10} + 10^{L_{m,k}/10} \Big)$$

so that the added masker lowers the signal-to-noise ratio and drives the articulation index toward zero at the neighboring stall. Because the masking and the ambient sounds fluctuate in time, the effective background is characterized by the equivalent continuous level, the logarithmic time average of the fluctuating level,

$$L_{\text{eq}} = 10 \log_{10}\!\left( \frac{1}{T} \int_0^T 10^{L(t)/10} \, dt \right)$$

which is the quantity against which the intelligibility of an intermittent target sound is assessed. The reporting of the masking-sound level is standardized in [ASTM E1573][ref_astm_e1573]. This is the acoustic principle of the automatic sound-masking device, treated in the technological-augmentation history below, which plays a masking sound, characteristically a recorded flush or a synthesized water sound, to conceal the sounds of elimination. The device also serves a resource-conservation function, because it substitutes a recorded sound for the repeated real flushing that users otherwise employ as a masker, and thereby reduces water consumption. Let $n_f$ denote the number of concealment flushes a user would otherwise perform and $v_f$ the volume per flush. The water saved per use by substitution of the device is

$$\Delta v = n_f \, v_f$$

which over the usage volume of a busy public facility integrates to a substantial conserved quantity. The device most closely associated with this function is the [Otohime sound device][ref_npr_otohime] marketed in Japan, whose reported per-use water saving is a manufacturer and journalistic estimate rather than a metrological measurement and is treated here as such.

The olfactory axis reduces to a dilution and removal problem governed by the ventilation of the room. Model the restroom as a well-mixed volume $V$ ventilated at a volumetric flow rate $Q$, with an odorant generated at rate $G$. The steady-state odorant concentration is given by the mass balance

$$C_{\text{ss}} = C_{\text{supply}} + \frac{G}{Q}$$

with $C_{\text{supply}}$ the concentration in the supply air, so that the steady-state odor level is inversely proportional to the ventilation rate. Inverting the relation gives the ventilation flow required to hold the odor concentration at a target level,

$$Q = \frac{G}{C_{\text{ss}} - C_{\text{supply}}}$$

which is the design relation that sizes the exhaust to the generation rate and the acceptable odor concentration. After a generation event ceases, the concentration decays toward the supply level according to the first-order relaxation

$$C(t) = C_{\text{supply}} + \big(C_0 - C_{\text{supply}}\big) \, e^{-Q t / V}$$

with time constant $\tau = V / Q$. The ventilation rate is conventionally expressed as an air-change rate, the number of room volumes exchanged per unit time,

$$\text{ACH} = \frac{Q}{V} = \frac{1}{\tau}$$

so that a higher air-change rate both lowers the steady-state odor level and shortens the decay time constant. The ventilation of the restroom is a matter of code as well as of comfort, and the ventilation standard [ASHRAE 62.1][ref_ashrae_62_1] specifies an exhaust of approximately fifty cubic feet per minute of continuous flow, near twenty-five liters per second, per water closet or urinal, with a higher intermittent rate. Elevation along the olfactory axis is the provision of ventilation sufficient to hold the odor concentration below the perception threshold at the generation rate the facility experiences, supplemented in the elevated facility by active scent introduction that substitutes a pleasant odorant for the neutral target of mere dilution.

## Hygienic Sufficiency as a Sanitation Property

The hygienic-sufficiency dimension, the gating base of the framework, admits treatment as a set of transport and inactivation problems. The dimension comprises the removal of waste, the interruption of pathogen transmission through surface and aerosol pathways, and the provision of hand hygiene.

The disinfection of a surface or a volume of water is governed to first approximation by first-order inactivation kinetics. Let $N$ denote the viable pathogen count and $N_0$ its initial value. Under a constant disinfectant exposure the count decays as

$$\frac{N}{N_0} = e^{-k t}$$

with $k$ an inactivation rate constant that depends on the disinfectant, its concentration, and the organism. The exposure required for a target reduction is characterized by the product of concentration and contact time, the CT value

$$\text{CT} = C \cdot t$$

which for a specified log-reduction target is approximately constant for a given organism and disinfectant, so that a higher concentration permits a shorter contact time and conversely. The CT formulation is the standard basis of water-disinfection and surface-disinfection guidance, and the quantitative-microbial-risk-assessment framework of [Haas and colleagues 2014][book_haas_2014_qmra] supplies the translation from residual pathogen count to infection probability.

The aerosol pathway is the toilet plume, the fine aerosol lofted by the turbulent flow of a flush, documented from the early droplet-production measurements of [Gerba and colleagues 1975][research_gerba_1975_plume] through the literature review of [Johnson and colleagues 2013][research_johnson_2013_plume] and the high-speed visualization of the energetic commercial-toilet plume by [Crimaldi and colleagues 2022][research_crimaldi_2022_plume], with the surface-contamination pathway documented by [Barker and Jones 2005][research_barker_jones_2005] and the role of the closed lid in suppressing the plume established by [Best, Sandoe, and Wilcox 2012][research_best_wilcox_2012]. The residence time of an aerosolized particle governs the opportunity for its inhalation or its deposition on a surface. A particle of diameter $d$ and density $\rho_p$ settling through air of density $\rho_f$ and dynamic viscosity $\eta$ reaches a terminal settling velocity given in the Stokes regime by

$$v_s = \frac{(\rho_p - \rho_f) \, g \, d^2}{18 \, \eta}$$

which scales as the square of the particle diameter, so that the fine particles of the toilet plume settle slowly and persist in the air of the enclosure for an extended interval. For the finest particles, whose diameter approaches the mean free path of the air, the continuum assumption of the Stokes derivation fails and the settling velocity is corrected by the Cunningham slip factor

$$C_c = 1 + \frac{\lambda_{\text{mfp}}}{d} \left[ 2.34 + 1.05 \, e^{-0.39 \, d / \lambda_{\text{mfp}}} \right]$$

with $\lambda_{\text{mfp}}$ the mean free path of the air, so that the corrected settling velocity $v_s C_c$ exceeds the uncorrected Stokes value and the very finest droplet nuclei settle still more slowly, extending their airborne residence. The time for a particle to settle through a height $h$ is

$$t_{\text{settle}} = \frac{h}{v_s C_c}$$

which for the fine particles of the plume reaches minutes to tens of minutes, the interval over which the ventilation of the enclosure must remove them. The persistence is the reason the discretion-dimension ventilation of the preceding section serves a hygienic function as well, because the same air exchange that dilutes odor also removes aerosolized pathogen, and the reason the closed-lid flush is a hygienic measure, because the closed lid interrupts the lofting of the plume.

The translation from an environmental pathogen dose to a probability of infection is the province of dose-response modeling. Under the exponential dose-response model the probability of infection from an ingested or inhaled dose $D$ is

$$P_{\text{inf}} = 1 - e^{-r D}$$

with $r$ a per-organism infectivity parameter, and under the more flexible Beta-Poisson model it is

$$P_{\text{inf}} = 1 - \left(1 + \frac{D}{\beta}\right)^{-\alpha}$$

with $\alpha$ and $\beta$ fitted parameters. The dose itself accumulates along the fomite pathway as the product

$$D = C_s \, A_c \, \tau_{s \to h} \, \tau_{h \to m} \, N_{\text{contacts}}$$

of the surface pathogen concentration $C_s$, the contact area $A_c$, the surface-to-hand and hand-to-mouth transfer efficiencies $\tau_{s \to h}$ and $\tau_{h \to m}$, and the number of contacts $N_{\text{contacts}}$, a chain quantified in the hand-to-face contact studies of [Nicas and Best 2008][research_nicas_best_2008]. The disinfection that reduces the surface concentration $C_s$ follows more generally the Chick-Watson law

$$\ln \frac{N}{N_0} = -k \, C^{\,n} \, t$$

with $n$ the coefficient of dilution that governs the relative importance of disinfectant concentration and contact time, reducing to the simple first-order form when $n$ equals one and the concentration is held constant. The efficacy of a surface-disinfection process is reported as the log reduction

$$\text{LR} = -\log_{10} \frac{N}{N_0}$$

so that the elevated facility that specifies a cleaning protocol to a stated log-reduction target sets a measurable hygienic standard rather than a nominal one. Hand hygiene interrupts the chain at the surface-to-hand and hand-to-mouth links, and the provision of effective hand hygiene, whose evidence base is set out in the [World Health Organization guidelines on hand hygiene][ref_who_hand_hygiene] and the earlier [guideline of Larson for the Association for Professionals in Infection Control][research_larson_1995], is therefore the single most consequential hygienic-dimension feature of the facility. The magnitude of the effect is established by a substantial epidemiological literature, including the systematic review of [Curtis and Cairncross 2003][research_curtis_cairncross_2003] on the reduction of diarrhoeal disease by handwashing with soap, the community meta-analysis of [Aiello and colleagues 2008][research_aiello_2008], and the worldwide review of handwashing practice by [Freeman and colleagues 2014][research_freeman_2014], which together place the provision of hand hygiene among the most consequential public-health functions the facility discharges. The drying of the hands after washing is itself a contested augmentation, because the jet-air dryer disperses residual microorganisms into the air of the facility more than the paper towel does, a finding of the comparative studies of [Best and Redway 2014][research_best_redway_2014], [Kimmitt and Redway 2016][research_kimmitt_redway_2016], and [Huesca-Espitia and colleagues 2018][research_huesca_espitia_2018], so that the choice of drying technology is a further instance of the non-monotone interaction between the augmentation dimension and the hygienic base.

Technological augmentation of hygiene is not unambiguously beneficial, a point that qualifies the augmentation dimension of the framework. The touchless fixture reduces the hand contacts through which the fomite pathway operates, yet the internal complexity of the electronically actuated valve can harbor waterborne pathogen more readily than the simple manual valve. The measurement of [Sydnor and colleagues 2012][research_sydnor_2012_faucet] found a markedly higher incidence of Legionella contamination in electronic-eye faucets than in manual faucets in a hospital setting, and found the electronic fixtures more resistant to disinfection. The augmentation dimension thus interacts with the hygienic-sufficiency base in a manner that is not monotone, and elevation along the augmentation dimension does not guarantee elevation of the hygienic base.

The fluid mechanics of the flush itself is the siphon action of the water closet. The characteristic modern water closet evacuates its bowl by establishing a siphon over the weir of the trap, so that once the rising water fills the trap passage the siphon draws the bowl contents through by the hydrostatic head. The flow through the siphon is governed by the Bernoulli relation along a streamline from the bowl surface to the trap outlet,

$$p_1 + \tfrac{1}{2}\rho v_1^2 + \rho g z_1 = p_2 + \tfrac{1}{2}\rho v_2^2 + \rho g z_2$$

subject to the continuity of the volumetric flow through the varying cross-section,

$$A_1 v_1 = A_2 v_2 = Q_{\text{flush}}$$

so that the discharge velocity at the outlet driven by the head $\Delta h$ from the crest to the outlet is

$$v_{\text{out}} = C_d \sqrt{2 g \, \Delta h}$$

with $C_d$ a discharge coefficient that lumps the viscous and contraction losses of the real trapway. The time to empty a bowl of cross-section $A_b$ through a trap of area $A_t$ as the head falls from $h_0$ to $h_f$ follows by integration of the Torricelli discharge as

$$t_{\text{flush}} = \frac{A_b}{C_d A_t} \sqrt{\frac{2}{g}} \left( \sqrt{h_0} - \sqrt{h_f} \right)$$

which shows that the evacuation time rises with the bowl area and falls with the trap area and the discharge coefficient, the design levers by which the fixture achieves a rapid and complete flush at the reduced water volume treated below. The minimum flush volume consistent with reliable siphon establishment and bowl clearance has fallen across the twentieth and twenty-first centuries under water-conservation pressure. The regulated maximum flush volume in the United States fell to 1.6 gallons, approximately 6.0 liters, under the [Energy Policy Act of 1992][ref_epact_1992], and the high-efficiency threshold under the Environmental Protection Agency [WaterSense specification][ref_epa_watersense_toilets] is 1.28 gallons, approximately 4.8 liters, subject to a solid-clearance performance floor verified by the [Maximum Performance testing protocol][ref_map_testing] against the [ceramic-fixture standard ASME A112.19.2][ref_asme_a112_19_2]. The trap also serves a hygienic function independent of evacuation, because the standing water in the trap forms a seal against the ingress of sewer gas. Let $h_s$ denote the depth of the trap seal. The seal resists a pressure difference up to

$$\Delta p_{\max} = \rho g h_s$$

with $\rho$ the density of water and $g$ the gravitational acceleration, so that a transient pressure excursion in the drainage system exceeding this value breaks the seal and admits sewer gas, which is the failure mode that drainage venting is designed to prevent. The [International Plumbing Code trap provisions][ref_ipc_traps_1002] require a liquid seal depth between two and four inches, approximately fifty to one hundred millimeters, which bounds the pressure excursion the seal can resist.

## Sensory Enrichment and Thermal Comfort

The sensory-enrichment dimension is the dimension along which luxury is most visibly signaled, and it comprises the material, the illumination, the acoustic character treated above, the scent treated above, and the thermal comfort of the facility. The thermal-comfort axis admits the standard formal treatment of the built environment.

The perceived thermal state of an occupant is predicted by the [Fanger comfort model][book_fanger_1970_thermal_comfort], standardized in [ASHRAE Standard 55][ref_ashrae_55] and [ISO 7730][ref_iso_7730], which relates the thermal load on the body to a predicted mean vote on a seven-point thermal-sensation scale. The predicted mean vote is

$$\text{PMV} = \big(0.303 \, e^{-0.036 M} + 0.028\big) \, L$$

with $M$ the metabolic heat production per unit body surface area and $L$ the thermal load, defined as the difference between the internal heat production and the heat loss to the environment at the actual environmental conditions. The dispersion of individual votes about the predicted mean is summarized by the predicted percentage dissatisfied,

$$\text{PPD} = 100 - 95 \, \exp\!\big(-0.03353 \, \text{PMV}^4 - 0.2179 \, \text{PMV}^2\big)$$

which attains its minimum of five percent at a predicted mean vote of zero, so that even under ideally neutral conditions a residual five percent of occupants report dissatisfaction. The comfort model shows that the elimination facility, characteristically a hard and often poorly conditioned room, sits by default away from thermal neutrality, and that elevation along the thermal axis, through the heated seat of the washlet, through radiant floor heating, and through the conditioning of the ventilation air, moves the predicted mean vote toward zero and the predicted percentage dissatisfied toward its floor.

## The Reverberant Field and the Luminous Environment

The sensory dimension of the facility is carried by its sound field and its light in addition to its thermal state, and both admit the standard formal treatment of the built environment, treated in the acoustic references of [Beranek][book_beranek_acoustics] and [Harris][book_harris_acoustical_handbook], that extends the acoustic apparatus of the discretion section.

The sound-pressure level at a point in a room is the sum of a direct field from the source and a reverberant field built up by reflection. The room constant

$$R = \frac{A}{1 - \bar{\alpha}}$$

with $A$ the total absorption and $\bar{\alpha}$ the mean absorption coefficient characterizes the capacity of the room to build a reverberant field, and the steady sound-pressure level at a distance $r$ from a source of sound power $L_w$ and directivity $Q$ is

$$L_p = L_w + 10 \log_{10}\!\left( \frac{Q}{4 \pi r^2} + \frac{4}{R} \right)$$

whose first bracketed term is the direct field falling as the inverse square of the distance and whose second term is the reverberant field, uniform through the room. The two terms are equal at the critical distance

$$r_c = \frac{1}{4}\sqrt{\frac{Q R}{\pi}}$$

beyond which the reverberant field dominates. In the hard-finished restroom the room constant is small, so that the critical distance is short and the reverberant term dominates almost everywhere, and the sounds of the room spread uniformly, which is the acoustic condition the discretion dimension seeks to suppress through absorption that raises $R$ and pushes the critical distance outward.

The luminous environment is governed by the illuminance, the luminous flux per unit area,

$$E = \frac{\Phi}{A_{\text{surface}}}$$

with $\Phi$ the luminous flux, and by the luminance of the surfaces the eye perceives. The perceived quality of the visual environment depends on the luminance contrast between a feature and its background,

$$C = \frac{L_{\text{feature}} - L_{\text{background}}}{L_{\text{background}}}$$

so that the elevated facility manages both the level of illuminance, sufficient for the grooming function the facility often serves, and the contrast and color temperature of the light, which set the character of the space and the appearance of the user in the mirror. The management of the luminous environment is a sensory-dimension elevation with no counterpart in the utilitarian facility, whose lighting serves only visibility.

## Water Consumption and Airborne Transmission

The resource and hygienic dimensions of the facility admit two further quantitative treatments, the water consumption of the facility and the airborne transmission of pathogen within it, which connect the elevation of the individual facility to the resource and public-health context.

The water consumption of a facility is the product of its usage volume and its per-use water demand. For a facility serving $N$ uses per day at a flush volume $v_f$, the annual water consumption is

$$W_{\text{annual}} = N \, v_f \times 365$$

so that the reduction of the per-flush volume from the older seven-gallon fixtures of the early twentieth century to the 1.28-gallon high-efficiency fixture of the WaterSense specification represents a large conserved quantity integrated over the usage volume of a public facility, and the water saved by a fleet of high-efficiency fixtures against a baseline volume $v_0$ is

$$\Delta W = N \, (v_0 - v_f) \times 365$$

which is the resource-dimension elevation the water-conserving fixture represents. The elevation of the facility along the augmentation dimension, through the low-flow fixture and the sound-masking device that reduces concealment flushing, is thus simultaneously a resource-dimension elevation.

The airborne transmission of pathogen within the enclosed facility is described by the Wells-Riley model, which relates the probability of infection to the exposure to airborne infectious quanta. The infection probability is

$$P_{\text{inf}} = 1 - \exp\!\left( -\frac{I \, q \, p \, t}{Q} \right)$$

with $I$ the number of infectious sources present, $q$ the quantum-generation rate per source, $p$ the pulmonary ventilation rate of the exposed user, $t$ the exposure duration, and $Q$ the room ventilation rate. The model shows that the infection probability falls with the ventilation rate $Q$, so that the ventilation that the discretion dimension provides for odor control and the hygienic dimension provides for aerosol removal also reduces airborne transmission, and the short exposure duration $t$ characteristic of the elimination facility limits the risk relative to spaces of longer occupancy. The effectiveness of the ventilation in removing contaminant from the breathing zone, rather than merely from the room, is characterized by a ventilation effectiveness factor that multiplies the nominal ventilation rate, and the elevated facility that places its exhaust to capture contaminant at the source achieves a higher effectiveness than the facility that merely dilutes the room volume.

## Extended Provisioning and Environmental Relations

Several further relations complete the quantitative apparatus of the framework and connect its dimensions to one another. The provisioning treatment extends to the finite-capacity facility, whose waiting area holds at most a bounded number of users, and the environmental treatment extends to the combination of sources and the fuller specification of thermal comfort.

The facility with a finite waiting capacity is the loss-delay system $M/M/c/K$, in which at most $K$ users may be present, those beyond the $c$ in service waiting until the capacity $K$ is reached, after which arrivals are lost. The blocking probability, the fraction of arrivals lost because the system holds $K$ users, is

$$P_K = \frac{a^c \, \rho^{\,K-c}}{c!} \, P_0$$

with $P_0$ the empty-system probability of the finite chain, and the effective arrival rate that enters the system is the offered rate thinned by the blocking, $\lambda_{\text{eff}} = \lambda (1 - P_K)$. The finite-capacity model describes the facility whose queue space is itself limited, so that provisioning must consider the waiting area as well as the fixture count, a consideration the elevated facility addresses through generous circulation space that raises $K$.

The combination of independent sound sources follows the logarithmic addition of their powers. Two sources of equal level $L$ combine to a level

$$L_{\text{total}} = L + 10 \log_{10} 2 \approx L + 3$$

so that doubling the number of equal sources raises the level by approximately three decibels. For $n$ equal sources the combined level is

$$L_n = L + 10 \log_{10} n$$

a relation that governs the accumulation of the sounds of a busy facility and the specification of the masking that must overcome them, because the masking level required rises with the logarithm of the occupancy.

The thermal comfort of the occupant depends not on the air temperature alone but on the operative temperature, the weighted mean of the air temperature and the mean radiant temperature,

$$T_{\text{op}} = \frac{h_c \, T_a + h_r \, T_r}{h_c + h_r}$$

with $h_c$ and $h_r$ the convective and radiative heat-transfer coefficients, so that the cold radiant surfaces characteristic of the hard-finished restroom depress the operative temperature below the air temperature and the heated surfaces of the elevated facility raise it. The thermal response of a heated element such as the washlet seat to a step of applied power follows the first-order relaxation

$$T(t) = T_{\infty} - (T_{\infty} - T_0) \, e^{-t / \tau_h}$$

with time constant $\tau_h = m c / (U A)$ set by the thermal mass and the heat-loss conductance of the element, so that the heated seat reaches its setpoint on a characteristic timescale that the elevated fixture minimizes to deliver immediate comfort. The ventilation effectiveness, the ratio of the contaminant removal achieved at the breathing zone to that of a perfectly mixed room, multiplies the nominal ventilation rate in the mass-balance relations of the discretion section,

$$Q_{\text{eff}} = \varepsilon_v \, Q$$

with $\varepsilon_v$ the effectiveness factor, and the age of air, the mean time since the air at a point entered the room, is its dual measure,

$$\bar{\tau}_{\text{air}} = \frac{V}{Q}$$

for a perfectly mixed room, a low age of air indicating fresh well-distributed supply. The thermal comfort of the occupant depends on the metabolic heat production and the clothing insulation, conventionally measured in the met and clo units, the metabolic rate referenced to the resting value,

$$M = \text{met} \times 58.15 \; \text{W m}^{-2}$$

and the clothing insulation expressed in clo units of $0.155 \; \text{m}^2\,\text{K}\,\text{W}^{-1}$ each, and the heat the occupant must shed is the metabolic rate net of external work,

$$H = M - W$$

which enters the thermal-load term of the Fanger model of the sensory section, so that the lightly clothed and largely sedentary user of the restroom sits at a definite point in the met-clo space that the elevated facility conditions toward comfort. These relations are drawn from the standard references of queueing theory including [Gross and Harris 1998][book_gross_harris_1998_queueing] and of aerosol science including [Hinds 1999][book_hinds_1999_aerosol], and they complete the quantitative operationalization of the framework dimensions.

## Cross-Disciplinary Framings

The elimination facility is studied across several disciplines that each supply a partial account of its elevation, and the framework of this article draws on all of them. The gathering of these framings establishes the intellectual context in which the six-dimension account sits.

The public-health and sanitary-engineering tradition treats the facility as an instrument of disease control. The tradition descends from the nineteenth-century sanitary movement and its demonstration that the containment and removal of human waste interrupts the transmission of enteric disease, and it supplies the hygienic-sufficiency dimension of the framework. The tradition is notable for a cautionary finding that qualifies any triumphalist account of ancient sanitation, because the archaeological-parasitology work of [Mitchell 2017][research_mitchell_parasites] found that the Roman sanitation apparatus of latrines, sewers, and public baths did not reduce the burden of intestinal parasites and may have coincided with its increase, a finding that separates the provision of a facility from the achievement of its hygienic purpose.

The architectural and design tradition treats the facility as a designed room and supplies the sensory-enrichment dimension. The foundational ergonomic study of the domestic bathroom by [Kira 1966][book_kira] established the human-factors analysis of the fixtures and their use, and the design-and-culture scholarship of [Penner 2013][book_penner_bathroom] and the edited volumes of [Molotch and Norén 2010][book_molotch_toilet] and [Gershenson and Penner 2009][book_gershenson_ladies_gents] established the study of the public restroom as a designed and contested social space.

The service-marketing tradition treats the facility as a component of the servicescape, the physical environment in which a service is delivered, formalized by [Bitner 1992][research_bitner], and supplies part of the social-signification dimension through the finding that the condition of the restroom shapes the customer evaluation of the establishment that provides it. The tradition includes the empirical work on restroom cleanliness and patron behavior of [Barber and Scarcelli 2009][research_barber_2009] and [2010][research_barber_2010], the servicescape-cleanliness studies of [Vilnai-Yavetz and Gilboa 2010][research_vilnai_yavetz_2010], [Kim and Bachman 2019][research_kim_bachman_2019], and [Taştan and Soylu 2023][research_tastan_soylu_2023], the review of servicescape cues by [Mari and Poggesi 2013][research_mari_poggesi], and the ambient-scent research of [Spangenberg and colleagues 1996][research_spangenberg], which grounds the scent component of the sensory dimension and establishes the empirical claim that the condition of the restroom measurably shapes patron satisfaction and the intent to return.

The operations-research tradition treats the facility as a queueing system and supplies the throughput dimension through the apparatus of the preceding sections, extended in the potty-parity analyses of [Anthony and Dufresne 2007][research_anthony_dufresne_2007] and the optimization treatments of [Farajollahzadeh and Hu][research_farajollahzadeh_hu_potty].

The gender-studies and legal tradition treats the facility as a site at which the gender order is inscribed in the built environment, developed in the legal history of sex-separated facilities by [Kogan 2007][research_kogan_sex_separation] and the sociological account of [Davis 2020][book_davis_battlegrounds], and supplies the analysis of the sex-based provision that the framework treats under the access-equity dimension.

## The Ancient and Medieval Elimination Facility

The elevated elimination facility has a documented history reaching to antiquity, and the Roman public latrine is its first well-attested instance. The Roman drainage that made the latrine possible began with the [Cloaca Maxima][ref_cloaca_maxima_wiki], the great drain whose construction is attributed to the regal period around 600 before the common era and which was progressively vaulted into a covered sewer draining the Forum to the Tiber. Against this drainage the Romans built the public latrine, the forica, a communal facility of stone benches pierced with keyhole openings set over a channel of running water, with a second channel of clean water at the feet for the rinsing of the shared sponge-on-a-stick, the tersorium, that served the function of cleansing. The archaeology of these facilities is catalogued in the work of [Koloski-Ostrow 2015][book_koloski_ostrow], reviewed in [Isis][research_ostrow_isis], and the edited volume of [Jansen, Koloski-Ostrow, and Moormann 2011][book_jansen_roman_toilets], reviewed in the [Bryn Mawr Classical Review][research_bmcr_roman_toilets], which document the excavated latrines of Rome, Ostia, Pompeii, and Herculaneum and their donor-funded provision, and the practice is surveyed for a general readership by [the Smithsonian][ref_smithsonian_roman] and [History Hit][ref_historyhit_roman]. The primary record of the Roman water infrastructure that the latrine depended on survives in the treatise of [Frontinus][ref_frontinus_aqueducts] on the water administration of Rome, the architectural manual of [Vitruvius][ref_vitruvius_architecture], and the natural-history compilation of [Pliny the Elder][ref_pliny_natural_history], which together supply the contemporaneous documentation that the modern archaeology interprets. The great drain that made the latrines possible is treated in the study of [Hopkins][research_hopkins_cloaca] on the monumental manipulation of water in archaic Rome, the dedicated monograph on Roman toilets of [Hobson 2009][book_hobson_latrinae], and the account of Roman slums, sanitation, and mortality of [Scobie 1986][research_scobie_1986], and the cautionary parasitological finding is documented in full in the [Cambridge repository version][research_mitchell_cam] of the Mitchell study and its [university account][ref_cambridge_roman_parasites].

The Roman latrine already exhibits several dimensions of the framework. It advanced the hygienic base through its running-water removal of waste, though the parasitology cited above shows the advance was incomplete. It advanced the sensory dimension through the marble finish, the decoration, and in some instances the heating of the elevated examples. It was, above all, a communal facility that made no provision for the discretion the modern facility prizes, so that its configuration on the discretion dimension is near the opposite pole from the contemporary elevated restroom, a divergence that illustrates the cultural variability of the dimension weights.

The medieval period saw the elimination facility retreat from the Roman communal model toward the private and the improvised. The castle garderobe, a seat built into the thickness of a wall on a projecting corbel and discharging to the moat or a cesspit below, is the characteristic medieval fixture, documented in the survey of [World History Encyclopedia][ref_worldhistory_medieval] and named, by one etymology, for the belief that the ammoniacal air of the privy protected stored garments from moth and flea. The chamber pot and the collection of night soil by the gong farmer, who emptied cesspits by night and sold the contents as agricultural fertilizer, constituted the urban waste economy of the period. The medieval facility sat near the utilitarian minimum on every dimension of the framework, and the subsequent history is in large part the history of its re-elevation.

## The Flush-Toilet Lineage and the Sanitary Revolution

The modern elimination facility rests on the flush water closet, whose lineage is a sequence of documented inventions across three centuries. The device originates with [Sir John Harington][book_harington_ajax], the Elizabethan courtier who designed a valved flushing closet he named the Ajax, a pun on the jakes, installed one for Queen Elizabeth the First at Richmond Palace in 1592, and described the invention in 1596 in the satire A New Discourse of a Stale Subject Called the Metamorphosis of Ajax, a work preserved in the [Royal Collection][ref_rct_harington] and recognized by [Guinness World Records][ref_guinness_first_flush] as the first flushing toilet. The Harington closet did not propagate, and the decisive advance waited nearly two centuries for the water seal. The lineage is documented in the record of [the Science Museum][ref_science_museum_flushing], the account of [Cumming's advance][ref_historyhit_cumming], the biography of [George Jennings][ref_jennings_wiki], and the American plumbing history of [Ogle 1996][book_ogle_modern_conveniences] and the fixture history of [Eveleigh 2002][book_eveleigh_privies].

The water seal that made the indoor water closet tolerable by preventing the return of sewer gas was patented by [Alexander Cumming][ref_national_archives_toilet] in 1775, whose S-trap held a standing plug of water in a bend below the bowl. The patent number is recorded by the United Kingdom National Archives as number 1105, a figure that some secondary sources give instead as 814, a discrepancy noted here for accuracy. The valve closet of Joseph Bramah, patented in 1778, dominated the following century, and the ceramic washdown closet advanced through the wares of the Staffordshire potteries, including the one-piece all-ceramic Unitas of Thomas Twyford of 1883. The name most attached to the flush toilet in popular memory, Thomas Crapper, belongs to a genuine sanitary engineer and showroom proprietor of the later nineteenth century who did not invent the flush toilet and whose association with it was amplified by a 1969 popular biography of [Reyburn][book_reyburn_flushed], a correction documented by [the Smithsonian][ref_smithsonian_crapper]. The social history of the fixture and its domestic setting is treated in the surveys of [Wright 1960][book_wright_clean_decent], [Eveleigh 2006][book_eveleigh_bogs], [Horan 1996][book_horan_porcelain_god], and [Lambton 1995][book_lambton_temples], and the popular accounts of [Carter 2006][book_carter_flushed], [Hart-Davis 1997][book_hart_davis], and [Bryson 2010][book_bryson_at_home], which together document the century-long domestication of the water closet and its progression from an object of concealment to an object of design.

The flush closet was of limited value until the city could carry its discharge away, and the provision of that capacity was the work of the sanitary revolution. The crisis that forced it in London was the Great Stink of the summer of 1858, when the untreated sewage of the growing city, discharged to the tidal Thames, produced a stench that drove the Parliament from its riverside chambers and compelled the rapid passage of enabling legislation, an episode documented by [the London Museum][ref_london_museum_stink]. The response was the intercepting-sewer network of [Sir Joseph Bazalgette][ref_ice_bazalgette] of the Metropolitan Board of Works, whose main drainage of the 1860s and 1870s, comprising more than a thousand miles of street sewers feeding great interceptors along embankments of the Thames, carried the discharge below the populated city and is credited with ending the metropolitan cholera, a story told in the history of [London's sewer system][ref_heritage_london_sewers]. The Bazalgette drainage recapitulated at the scale of the industrial metropolis the achievement the Roman aqueduct and sewer had reached in antiquity, treated in the engineering history of [Hodge][book_hodge_aqueducts], and the London episode is documented in full in the history of [Halliday 1999][book_halliday_great_stink] and set within the long history of hygiene and purity by [Smith 2007][book_smith_clean]. The comparable American development is the subject of the sanitary-infrastructure history of [Melosi 2000][book_melosi_sanitary_city], the Parisian counterpart is treated by [Reid 1991][book_reid_paris_sewers], and the sensory history of the urban environment the sanitary revolution transformed is treated in the odor history of [Corbin 1986][book_corbin_foul_fragrant]. The sanitary revolution is the historical achievement of the hygienic-sufficiency dimension at the scale of the city, and it is the precondition of every subsequent elevation of the individual facility.

## The Public Convenience and the Gendering of Access

The public elimination facility as a provided amenity dates from the middle of the nineteenth century, and its history is inseparable from the gendering of access to public space. The first public flush toilets to reach a mass public were installed by [George Jennings][ref_great_exhibition_toilets] in the retiring rooms of the Great Exhibition of 1851 in the Crystal Palace, where over the six months of the exhibition more than eight hundred thousand visitors paid one penny for the use of a clean seat, a towel, and a comb, an arrangement that gave the English language the euphemism of spending a penny, a phrase whose history the [Historic England][ref_historic_england_penny] collection documents. The commercial success of the Jennings installation demonstrated that the provision of an elevated public convenience could be a paying enterprise, a demonstration that connects the earliest public facility to the social-signification and access dimensions of the framework.

The public conveniences that followed were provided overwhelmingly for men. The street facilities of the Victorian city were predominantly male urinals, and the absence of provision for women constituted what the historical literature terms the urinary leash, the constraint on the distance and duration of a woman's movement through the city imposed by the absence of a facility she could use, documented in the account of [Historic UK][ref_historic_uk_womens]. The redress of this asymmetry came in part through the commercial provision of the department store, whose ladies' retiring rooms and tea rooms, exemplified by the opening of [Selfridges][ref_selfridges_london_museum] on Oxford Street in 1909, gave women of means a network of facilities that extended their access to the commercial city, a development analyzed in the social history of [Rappaport 2000][book_rappaport_shopping]. The gendering of public-facility access is the historical root of the access-equity dimension and of the potty-parity question the quantitative sections treated, and it establishes that the access dimension has been, from the beginning, a matter of who is enabled to occupy public space.

## The Japanese High-Technology Washroom

The contemporary frontier of the elevated elimination facility is the Japanese high-technology washroom, whose development over the last half century has advanced the sensory, discretion, and technological-augmentation dimensions farther than any other tradition. The central device is the washlet, the integrated cleansing-and-drying seat, whose origin lies in an American medical bidet seat of the 1960s that [TOTO][ref_toto_history] acquired and re-engineered and launched in 1980 as the Washlet G, providing a warm-water cleansing spray, a warm-air dryer, and a heated seat. The device propagated through Japanese households from a penetration near fourteen percent in the early 1990s to above eighty percent in the contemporary period, a diffusion documented by [Nippon.com][ref_nippon_hightech] and analyzed in the material-culture study of [Szczygiel 2016][research_szczygiel_ejcjs], and its cumulative shipments passed seventy million units, as [TOTO][ref_toto_70million] reports.

The discretion dimension received its own Japanese device in the sound-masking machine, introduced by TOTO in 1988 under the name Otohime, the sound princess, which plays a masking water sound to conceal the sounds of elimination and which was motivated, as [Web Japan][ref_webjapan_otohime] records, by the conservation of the water that users otherwise expended on concealment flushing. The device is the physical realization of the acoustic-masking principle the discretion section formalized, and its water-saving figure, treated in that section, is a manufacturer estimate.

The most recent and most visible Japanese advance is the elevation of the public toilet itself into a work of architecture, exemplified by [the Tokyo Toilet][ref_nippon_tokyotoilet] project. Financed through a coordinating role of the Nippon Foundation and begun in 2018, the project commissioned seventeen public toilets in the Shibuya district from sixteen creators including the architects Tadao Ando, Toyo Ito, Kengo Kuma, and Fumihiko Maki, and completed the set in June 2023. The most discussed of the installations are the two transparent toilets of [Shigeru Ban][ref_dezeen_transparent], whose walls of switchable glass turn opaque when the door is locked, resolving the discretion problem through a technological augmentation that makes the state of the facility legible from outside while preserving privacy within. The project became the subject of the Wim Wenders film [Perfect Days][ref_perfectdays_wiki], whose protagonist is a cleaner of the Tokyo toilets and which premiered at Cannes in 2023, and whose treatment of the sanitation labor behind the elevated facility is analyzed in the scholarship of [Hao Wen 2024][research_haowen_mediapolis]. The Tokyo Toilet project is the clearest contemporary demonstration that the elimination facility can be elevated to the status of civic art, advancing the sensory and social-signification dimensions to a degree without precedent in the public facility, and it is documented in the project record of the [completed installations][ref_nippon_17complete], the account of [the Tokyo Toilet][ref_tokyotoilet_wiki], and the monograph of [Okano and Nagare 2023][book_okano_tokyotoilet], while the [Perfect Days][ref_criterion_perfectdays] film and its [reception][ref_nippon_perfectdays] carried the project to a global audience.

The Japanese elevation of the elimination facility rests on a cultural foundation that predates the washlet, because the Japanese aesthetic tradition accorded the toilet a contemplative and aesthetic status that the Western tradition did not, an attitude articulated in the essay of [Tanizaki][book_tanizaki_shadows] In Praise of Shadows, which praised the traditional Japanese toilet as a place of repose and sensory refinement. The material-culture history of the transition from the night-soil economy to the washlet is traced in the study of [Szczygiel][research_szczygiel_nightsoil] on the premodern night-soil collection system, and the technical development and diffusion of the washlet is documented across the record of its [fortieth anniversary][ref_toto_40th], the [facts of its development][ref_toto_10facts], the milestones of its [fifty-millionth][ref_prnewswire_50m] and [sixty-millionth][ref_prnewswire_60m] units, the account of the [sanitary-equipment industry][ref_sanitary_net], and the record of the [TOTO Museum][ref_nippon_toto_museum]. The sound-masking device is further documented in the accounts of [the sound princess][ref_sound_princess_enn] and its [water-conservation function][ref_sound_princess_iol], and the broader Japanese toilet culture in the surveys of [the washlet][ref_washlet_wiki] and [toilets in Japan][ref_toilets_japan_wiki]. The Japanese case demonstrates that the elevation of the elimination facility along the sensory and augmentation dimensions can rest on a deep cultural foundation rather than on technology alone.

## Luxury Fixtures and the Restroom as Status Signal

The private and commercial elevated restroom expresses its elevation through fixture, attendance, and finish, and the contemporary market offers fixtures whose specification approaches the limit of the technological-augmentation dimension. The [Kohler Numi][ref_numi_newatlas], introduced in 2011 and updated in 2019 with an integrated voice assistant, integrates a bidet, a heated seat, a foot warmer, ambient lighting, and audio into a single fixture at a price above six thousand dollars, its [second-generation model][ref_numi2_cnbc] adding an integrated voice assistant, and the [TOTO Neorest][ref_neorest_750h], whose NX variant took a [Red Dot design award][ref_neorest_nx_reddot], and the [Duravit SensoWash][ref_sensowash_duravit] of the designer Philippe Starck, an [award-winning][ref_sensowash_azaward] shower-toilet, occupy the same segment. These fixtures advance the technological-augmentation and sensory dimensions at the scale of the individual fixture, and their price situates the elevated facility as a status good. The frontier of the augmentation dimension extends beyond comfort to health monitoring, in the mountable smart-toilet system of [Park and colleagues 2020][research_park_2020_smart_toilet], which analyzes excreta to provide personalized health data, an augmentation that turns the elimination facility into an instrument of continuous physiological measurement.

The attended restroom advances the social-signification dimension through the provision of human service, a practice roughly two centuries old whose most documented practitioner is the Bristol attendant [Victoria Hughes][ref_attendant_wiki], the first of the profession to receive an entry in the Oxford Dictionary of National Biography, and whose decline is associated with the shift from cash to digital payment that removed the gratuity economy on which the profession rested. The recognition of the elevated restroom is institutionalized in the awards of the [Cintas America's Best Restroom][ref_bestrestroom_hof] contest in the United States and the [Loo of the Year Awards][ref_loty_wiki] in the United Kingdom, and the elevation of the restroom to a designed cultural object is exemplified by the Art Deco lounges of Radio City Music Hall of 1932 and the egg-pod toilets of the London restaurant [Sketch][ref_sketch_wallpaper] of 2002. The advocacy for the provision of sanitation as a matter of dignity and public health is organized globally by the [World Toilet Organization][ref_wto_wiki], founded in 2001, whose [World Toilet Day][ref_un_toilet_day] was adopted by the United Nations in the [General Assembly resolution of 2013][ref_un_res_67_291], a development that situates the elevation of the elimination facility within a global development agenda that treats basic sanitation, rather than luxury, as the unmet need for much of the world. The scale of that unmet need is documented in the primary data of the [World Health Organization and United Nations Children's Fund Joint Monitoring Programme][ref_who_unicef_jmp] and the [World Health Organization sanitation fact sheet][ref_who_sanitation], which record that a large fraction of the world population lacks safely managed sanitation, the baseline against which the elevated facility of the wealthy establishment stands in sharp relief.

## The Manufacturer Landscape and the Fixture Market

The elevation of the elimination facility along the sensory and augmentation dimensions is supplied by a fixture industry whose principal firms have long histories and whose product ranges span the utilitarian to the luxury segment. The industry includes [Kohler][ref_kohler_wiki], founded in the nineteenth century and the maker of the Numi luxury fixture, [TOTO][ref_toto_wiki], the Japanese firm whose washlet defined the augmentation frontier, and the European firms [Villeroy and Boch][ref_vb_wiki], [Roca][ref_roca_wiki], and the successor to the American ceramic industry, [American Standard][ref_amstd_wiki], whose luxury bidet-toilet lines are marketed under the [SpaLet][ref_spalet_americanstandard] name and its [DXV][ref_dxv_at200] premium brand. The industry structure locates the augmentation frontier in the premium product lines of these firms, whose fixtures integrate the cleansing, drying, heating, and self-cleaning functions that advance the augmentation dimension, and whose price situates the elevated fixture as a status good.

The recognition of the elevated facility is institutionalized in awards and in advocacy organizations. The [Cintas America's Best Restroom][ref_cintas_2024] contest recognizes commercial restrooms in the United States, the [Loo of the Year Awards][ref_loty_official] inspect and rate facilities in the United Kingdom against a detailed criterion set, and the [British Toilet Association][ref_bta_about] and the [World Toilet Organization][ref_wto_about] advocate for the provision and the dignity of the facility, the latter through the [United Nations resolution][ref_un_ga11397] that established World Toilet Day. The design science of the commercial restroom is developed in the servicescape research treated above and in the work of [Anthony][book_anthony_defined] on the social dimensions of design, and the ambient-scent component of the sensory dimension is a subject of the scent-marketing industry documented by [ScentAir][ref_scentair]. The commercial history of women's access to elevated facilities through the department store is documented in the account of [the Marshall Field's tea room][ref_marshall_fields_tearoom] and the history of [Marshall Field's][ref_marshall_fields_wiki], and the iconic status of the designed restroom is exemplified by the [Radio City Music Hall][ref_radio_city_wiki] lounges and the Stuart Davis mural [Men Without Women][ref_men_without_women_wiki].

## Vending, Provisioning, and Menstrual Equity

The provisioning dimension of the elimination facility, the supply of the consumable goods its use requires, has its own history bound up with the vending machine and, more recently, with the politics of menstrual equity. The vending of goods within or adjacent to the restroom includes the [condom vending machine][ref_condom_machine_wiki], whose history reaches to the early twentieth century and whose most documented early operator is the Berlin manufacturer [Julius Fromm][ref_fromm_wiki], who placed condom machines in communal facilities from the late 1920s to reduce the embarrassment of over-the-counter purchase, and whose business was expropriated under the Nazi regime, a history recounted by [Aly and Sontheimer][book_aly_fromms] and by [Vice][ref_vice_fromm] and set within the longer social history of the condom by [Collier 2007][book_collier_condom]. The coin-operated sanitary-napkin dispenser followed, and an example is preserved in the collection of [the Smithsonian][ref_smithsonian_modess]. The vending machine itself, of which Japan sustains among the highest densities in the world, is treated in the survey of [the vending machine][ref_vending_machine_wiki]. The provisioning of the workplace facility, and the right to the break its use requires, is treated in the labor history of [Linder and Nygaard 1998][book_linder_void].

The contemporary frontier of restroom provisioning is the free provision of menstrual products as a matter of equity. The [Period Products Free Provision Scotland Act 2021][ref_scotland_period_act] established the first national statutory duty to provide menstrual products without charge, and comparable school-provision schemes have followed in [England][ref_gov_uk_period] and in [more than half of the United States][ref_ecs_period], a legal landscape surveyed across the states in the [scan of the fifty states and the District of Columbia][research_menstrual_legal_landscape]. The provisioning history connects the framework to the access-equity dimension in a form specific to the sexes, because the provisioning a facility requires is not symmetric across the populations it serves, and the equitable provision of menstrual products is an access-dimension elevation with no counterpart in the historically male-default facility.

## Regulatory and Technical Framework

The elevation of the elimination facility is constrained and in part directed by a framework of codes and standards that fix the minimum provision along several dimensions of the framework. The provisioning of fixtures is governed by the plumbing code, which specifies minimum fixture counts by occupancy. The [International Plumbing Code][ref_ipc_fixture_403] and the [Uniform Plumbing Code][ref_upc_fixtures] fix these minima, and the contemporary editions assign a greater female fixture count in assembly occupancies in approximate response to the potty-parity analysis, a code development documented by the [International Code Council][ref_icc_ipc]. The sex-based provision is further directed by the potty-parity statutes, beginning with the California Restroom Equity Act associated with the year 1987, though some sources record 1989, motivated by the queues at large public venues, and continued in the Virginia regulation that took effect in 1989, the advocacy of [Banzhaf][ref_banzhaf_potty], and the New York Women's Restroom Equity Act of 2005 that mandated a fixture ratio near two to one in many assembly venues.

The hygienic and comfort dimensions are governed by the ventilation standard [ASHRAE 62.1][ref_ashrae_62_1], which fixes the exhaust rate per fixture, and by the thermal-comfort standard [ASHRAE Standard 55][ref_ashrae_55] and [ISO 7730][ref_iso_7730]. The water consumption of the fixture is governed by the [Energy Policy Act of 1992][ref_epact_1992], codified in the appliance-efficiency standards of [Title 10 of the Code of Federal Regulations Part 430][ref_ecfr_10_430], and by the voluntary [WaterSense specification][ref_epa_watersense_toilets] and its [product-specification program][ref_epa_watersense_specs] of the Environmental Protection Agency, verified against the performance floor of the [Maximum Performance protocol][ref_map_testing] and the [ceramic-fixture standard][ref_asme_a112_19_2]. The acoustic and privacy dimension is served by the measurement standards [ASTM E1130][ref_astm_e1130] and [ASTM E1573][ref_astm_e1573]. The accessibility of the facility to the full range of bodies is governed by the [2010 ADA Standards for Accessible Design][ref_ada_2010_standards], issued under the authority of the [United States Access Board][ref_access_board_ada], whose provisions for the accessible toilet room fix the access dimension for users with disabilities, and the advocacy for the provision and quality of the public facility is organized in part by the [American Restroom Association][ref_american_restroom_assoc]. The regulatory framework thus fixes a minimum configuration on the hygienic, access, thermal, acoustic, and resource dimensions, above which the elevation of the facility is the discretionary choice of its provider.

## Contemporary Comparative Landscape

The contemporary elimination facility varies markedly across national traditions, and the variation is itself informative about the dimension weights different cultures assign. The Japanese tradition, treated above, advances the sensory, discretion, and augmentation dimensions farthest through the washlet, the sound-masking device, and the architectural public toilet. The North American tradition is distinguished by the partition-and-gap stall, whose door and floor gaps, documented in the comparison of [One Point Partitions][ref_onepoint_stalls], reflect a history of ventilation code, cost, cleaning, and surveillance considerations and which sits low on the discretion dimension relative to the European floor-to-ceiling cubicle. The European tradition, and the German and Swiss traditions in particular, favor the enclosed cubicle that advances the discretion dimension. The variation demonstrates that the elevation of the elimination facility is not a single scale along which nations are ranked, but a multidimensional space in which traditions advance different dimensions to different degrees, which is the central reason the framework retains the full dimension vector rather than collapsing to a scalar.

## Comparative Cross-Sectional Analysis

A cross-sectional comparison of facility types at a single point in time illustrates the framework as a classification device. The airport or transit-terminal restroom faces a high peaking factor and weights the throughput dimension heavily, provisioning a large fixture count and, in the elevated instances, touchless augmentation and wayfinding. The luxury-hotel or fine-restaurant restroom weights the sensory and social-signification dimensions heavily, provisioning finish, attendance, and scent while serving a modest and predictable demand. The stadium or arena restroom faces the highest peaking factor of all and weights throughput above every other dimension, and it is the venue at which the potty-parity failure is most visible and most consequential. The festival or event portable facility sits near the utilitarian minimum on every dimension and illustrates the baseline against which elevation is measured. The domestic bathroom, treated in the design literature from [Kira 1966][book_kira], weights the sensory and augmentation dimensions and is the site at which the luxury fixtures of the augmentation frontier are principally installed. The cross-section shows that the dimension weights are set jointly by the demand profile the facility faces and by the return its provider captures on elevation, which is the structural claim of the framework.

## Data Sources and Reconstruction Methodology

The reconstruction of the history and the quantitative apparatus of this article draws on several classes of source with differing evidential weight, and the methodological commitment to distinguishing them requires that the classes be stated. The archaeological and primary-historical record, including the excavation catalogues of Roman sanitation and the patent record of the flush-closet lineage, supplies the dated events, subject to the discrepancies in the patent-number and statute-year record noted at the relevant points. The standards and code documents supply the regulatory minima with high reliability. The peer-reviewed research supplies the quantitative models and the empirical measurements, including the occupancy-time asymmetry and the servicescape effects. The manufacturer and trade-press sources supply the specification and the market history and are treated as secondary, and the specific manufacturer claims, including the water-saving figure of the sound-masking device, are flagged as manufacturer estimates rather than independent measurements. The framework scores and weights are structural rather than measured, because the systematic measurement of facility populations across the six dimensions has not been assembled, a gap the following section treats.

## Historiographical Gap and Recent Scholarship

The scholarly literature on the elimination facility is fragmented across disciplines that rarely cite one another, and the fragmentation is itself the principal historiographical gap. The public-health and sanitary-engineering literature treats the hygienic dimension in isolation from the social meaning of the facility. The architectural and design literature, including the cultural histories of [Penner 2013][book_penner_bathroom] and the edited volume of [Molotch and Norén 2010][book_molotch_toilet], treats the facility as designed space with limited engagement with the quantitative operations literature. The operations-research literature treats the throughput dimension with mathematical rigor and limited engagement with the cultural and design questions. The gender-studies and legal literature, including [Kogan 2007][research_kogan_sex_separation] and the related treatment of restroom law and transgender identity by [Kogan 2017][research_kogan_transgender], [Cavanagh 2010][book_cavanagh_queering], and [Davis 2020][book_davis_battlegrounds], treats the facility as a site of the gender order with limited engagement with the engineering, and the Victorian roots of the asymmetry are documented in the study of [women's public conveniences in Victorian London][research_unmentionable_suffering]. The service-marketing literature, from [Bitner 1992][research_bitner], treats the facility as a component of commercial experience. The popular and journalistic literature, including [George 2008][book_george_big_necessity] and [Lowe 2018][book_lowe_no_place], synthesizes across the strands for a general audience, and the social and cultural histories of urban filth and its management, from [Jackson 2014][book_jackson_dirty_old_london] on Victorian London and [Cockayne 2007][book_cockayne_hubbub] on early-modern nuisance to the theoretical account of [Laporte 2000][book_laporte_history_shit] and the sociological history of [Inglis 2001][book_inglis_excretory], supply the cultural dimension, while the survey of [Gregory and James 2006][book_gregory_toilets_world] documents the global variety of the facility.

The gap this article addresses is the absence of a common framework that integrates these strands, and the six-dimension framework is offered as such an integration, assigning each disciplinary literature to the dimension or dimensions it illuminates. The recent scholarship has moved toward integration in the inclusive-design tradition of [Greed 2003][book_greed_inclusive] and in the emerging literature on menstrual equity and on all-gender provision, but a unified quantitative-and-cultural account remains to be assembled, and its assembly requires the systematic measurement the preceding section identified as absent.

## Alternative Analytical Frameworks

The six-dimension framework is one organizing lens among several that the literature offers, and the alternatives illuminate features the framework treats only implicitly. The Foucauldian framework treats the facility as an apparatus of discipline and biopolitics, in which the regulation of the eliminating body is an instance of the government of populations, and it illuminates the social-signification and access dimensions as instruments of social control rather than of experience. The purity-and-danger framework of the anthropology of pollution treats the facility as the boundary apparatus that manages the culturally dangerous category of bodily waste, and it illuminates the discretion dimension as the management of symbolic pollution rather than of mere sensory nuisance. The civilizing-process framework of the historical sociology of manners treats the progressive concealment of elimination as an instance of the long-run advance of the threshold of shame and repugnance, and it illuminates the historical trajectory of the discretion dimension.

The feminist and gender-order framework treats the facility as a principal site at which the binary gender order is materialized and enforced, developed in the legal and sociological work cited above, and it illuminates the access-equity dimension and the sex-segregation question as matters of power rather than of throughput alone. The disability and universal-design framework treats the facility through the requirement of access for the full range of bodies, and it illuminates a dimension the six-dimension framework subsumes under access equity but which merits independent treatment. The political-economy framework treats the public facility as a public good subject to under-provision, and it illuminates why the elevated facility clusters in the commercial settings that capture a return on elevation while the public facility tends toward the minimum. The science-and-technology-studies framework treats the fixture as a sociotechnical artifact whose design encodes social assumptions, and it illuminates the technological-augmentation dimension as a carrier of cultural choice rather than of neutral function. Each alternative framework recovers a feature of the elimination facility that the six-dimension framework treats, and the frameworks are complementary rather than competing, because each foregrounds a different dimension of the same object.

## The Elevation Trajectory and the Dynamics of Diffusion

The elevation of the elimination facility is not a static condition but a trajectory through the dimension space of the framework, and the history the preceding sections traced admits reading as such a trajectory. The Roman latrine occupied a position high on the sensory dimension and near the minimum on the discretion dimension. The medieval garderobe fell to the minimum on nearly every dimension. The sanitary revolution raised the hygienic base at the scale of the city and made the subsequent elevation of the individual facility possible. The Victorian public convenience advanced the access dimension unevenly across the sexes. The twentieth century advanced the hygienic and thermal dimensions through the domestic bathroom, and the contemporary Japanese washroom advanced the sensory, discretion, and augmentation dimensions to their present frontier. The trajectory is neither monotone nor uniform, because different cultures and periods advanced different dimensions, and the framework represents this history as a path through a six-dimensional space rather than as movement along a single scale.

The diffusion of an elevation from its point of introduction to general adoption follows the characteristic pattern of the diffusion of an innovation, in which the adopting fraction rises along a sigmoid curve from an early minority through a rapid middle phase to a saturating majority. The washlet in Japan traced such a curve, rising from a penetration near one tenth in the early period to above four fifths in the contemporary period over the course of a generation, and the same curve describes the diffusion of the flush closet, the domestic bathroom, and the low-flow fixture. The diffusion is governed by the interaction of the cost of the elevation, the value the adopter places on it, and the social signal that adoption sends, so that an elevation diffuses rapidly when its cost falls and its social meaning rises, and stalls when either condition fails. The uneven international diffusion of the washlet, rapid in Japan and slow elsewhere, illustrates that the value placed on an elevation is culturally conditioned rather than universal, which is the framework claim that the dimension weights vary across cultures expressed as a claim about the rate of diffusion.

The elevation trajectory is bounded above by the resource and spatial constraints the framework identifies. The augmentation and sensory dimensions consume capital, water, and energy, and the resource dimension the water-consumption section treated sets a limit on the elevation that a resource-constrained context can sustain. The contemporary tension between the augmentation frontier of the high-technology washroom and the resource constraint of a water-stressed world is the point at which the elevation trajectory meets its bound, and the direction of the subsequent trajectory, whether toward further augmentation at higher resource cost or toward a resource-efficient elevation that advances the sensory and discretion dimensions without the resource cost, is among the load-bearing open questions the article closes with.

## Pattern Extraction

The elevation mechanic that the history of the elimination facility illustrates admits abstract characterization in a form other readers can recognize in adjacent facility contexts. This section states the abstract mechanic without naming any specific downstream application. The companion article on bathing states the cross-facility generalization once the second instantiation is in hand.

The abstract elevation mechanic is the property of a facility serving a universal somatic necessity that raises the facility from a utilitarian minimum toward an enhanced and luxury experience by ascending a partially ordered ladder of six value dimensions rooted at a gating hygienic base. The mechanic has several load-bearing features that jointly produce the observed elevation.

First, the elevation is gated at the hygienic base. A facility that fails the sanitation floor is not experienced as elevated regardless of its scores on the enrichment dimensions, which is the content of the gate function $\Phi(x_H)$ in the elevation index. The gating feature distinguishes somatic-maintenance facilities from ornamental spaces, because the somatic facility must discharge its biological function before its enrichment is legible.

Second, the elevation is multidimensional rather than scalar. The five enrichment dimensions of discretion, sensory quality, throughput, social signification, and technological augmentation are distinct axes along which a facility may advance independently, so that a facility may be elevated on one axis while remaining at the minimum on another. The multidimensionality is the reason a single scalar ranking of facilities is inadequate and the reason the framework retains the full dimension vector.

Third, the dimensions stand in partial-order dependency rather than free independence. Advancement on the sensory dimension presupposes a degree of advancement on the throughput dimension, because a facility that cannot serve its demand without a queue cannot present itself as a designed experience. Advancement on the discretion dimension supports advancement on the social-signification dimension, because a facility that fails to conceal the private act cannot signal the status its provider intends. The partial order constrains the feasible elevation trajectories a facility may follow.

Fourth, the elevation trades against spatial and capital efficiency. Advancement on the sensory and throughput dimensions consumes floor area and capital that a utilitarian facility would not spend, so that the elevated facility is characteristically less efficient in served demand per unit area and per unit capital than the minimum facility. The trade is the reason elevation is a choice of the facility provider rather than a free improvement, and the reason elevated facilities cluster where the provider captures a return on the expenditure through the experience it sells or the status it signals.

Fifth, the technological-augmentation dimension interacts non-monotonically with the hygienic base. Augmentation that reduces one transmission pathway may open another, as the touchless-fixture case illustrates, so that advancement on the augmentation dimension does not guarantee advancement of the hygienic base and must be evaluated against the base rather than assumed to support it.

The elevation of a facility class thus requires advancement along the multidimensional ladder subject to the hygienic gate, the partial-order dependencies, the efficiency trade, and the non-monotone augmentation interaction. The specific elimination-facility history closes the ladder in the specific ways the historical treatment documents, and the specific counter-examples of unelevated or failed facilities negate one or more dimensions. The abstract mechanic admits application to any facility serving a universal necessity in which the provider faces the choice whether to spend capital and area on elevation, and the systematic evaluation of any candidate facility requires the evaluation of the six dimensions against the specific technical, hygienic, logistical, and social conditions the facility faces.

The joint-elevation condition admits a compact form. Let $\theta$ denote a threshold on the elevation index above which a facility is recognized as elevated. The facility is elevated when

$$E = \Phi(x_H) \cdot \sum_{d \in \{P, S, T, R, A\}} w_d \, x_d \; \geq \; \theta$$

which requires both that the hygienic gate be substantially open, so that $\Phi(x_H)$ is near one, and that the weighted enrichment aggregate clear the threshold net of the gate. A facility may fail the condition by a closed gate at satisfactory enrichment, which is the unhygienic-but-ornamented failure, or by an open gate at insufficient enrichment, which is the clean-but-utilitarian baseline. The two failure modes are distinguished by which factor of the product is deficient.

## Cross-References to the Companion Article

This article is the first of the two articles in the Enhanced and Luxury Facilities series. It introduces the six-dimension facility-elevation framework and applies the framework to the elimination facility. The companion article that follows applies the same six dimensions to the immersion and bathing facility, where the sensory and social-signification dimensions carry greater weight and where the thermal and hydraulic physics of heated water supplies the quantitative apparatus that the queueing and acoustic physics supplies here. The companion article states the cross-facility generalization of the elevation mechanic once the second instantiation is established, and treats the sex-based differences of the bathing facility, which take the form of segregated bathing rather than of asymmetric provision.

## Terminological Note

The article adopts specific terminology that recurs across both articles of the series. The terms particular to the elimination-facility treatment are defined here.

Somatic-maintenance facility refers to a facility serving a universal bodily necessity, of which the elimination facility and the immersion facility are the two classes the series treats.

Elevation refers to the movement of a facility from a utilitarian minimum toward an enhanced and luxury experience along one or more of the six dimensions of the framework.

Elevation index refers to the scalar aggregate of the six dimension scores under the gated weighted-aggregation form, admitting the additive, geometric, and constant-elasticity-of-substitution variants the framework section defines.

Hygienic gate refers to the saturating function of the hygienic-sufficiency score that multiplies the enrichment aggregate in the elevation index, encoding the suppression of perceived elevation under hygienic failure.

Potty parity refers to the equalization of an outcome, whether expected wait or utilization, across the sexes in the provision of elimination facilities, as distinct from the equalization of the input of floor area or fixture count.

Discretion dimension refers to the acoustic, visual, and olfactory management of the private act of elimination performed in a shared or serviced space.

Technological augmentation refers to the mechanized and automated capability that extends the base function of the facility beyond the manual minimum, including the washlet, the automatic sound-masking device, the touchless fixture, and the vending and dispensing machine.

## Load-Bearing Open Questions

The article identifies several open questions that admit exposition within its scope but do not admit full resolution given the state of the record.

The measurement question asks the specific empirical calibration of the six dimension scores and their weights for a given facility, which the article specifies structurally but does not resolve numerically, because the requisite systematic measurement of facility populations across the dimensions has not been assembled in the literature.

The weighting question asks whether the weights of the enrichment dimensions in the elevation index are stable across cultures or vary with the norms of privacy, display, and the body that differ across cultures. The historical treatment supplies evidence of variation, but the specific weighting functions are not resolved.

The augmentation-interaction question asks the general characterization of the non-monotone interaction between the technological-augmentation dimension and the hygienic base, of which the touchless-fixture case is one instance. The general conditions under which augmentation supports rather than undermines the hygienic base are not resolved.

The parity-criterion question asks which of the several parity criteria, whether equal wait, equal utilization, or equal probability of delay, is the appropriate normative target for the equitable provision of elimination facilities. The article states the criteria and their fixture-ratio consequences but does not adjudicate among them, because the adjudication is a normative rather than a positive question.

The convergence question asks whether the elevation trajectories of elimination facilities across establishments and cultures converge toward a common configuration or sustain persistent divergence. The contemporary evidence of the high-technology washroom suggests partial convergence on the augmentation dimension alongside persistent divergence on the discretion and social-signification dimensions, but the long-run trajectory is not resolved.

## References

### Books

- [Aly and Sontheimer 2007 Fromms How Julius Fromm's Condom Empire Fell to the Nazis][book_aly_fromms]
- [Bryson 2010 At Home A Short History of Private Life][book_bryson_at_home]
- [Carter 2006 Flushed How the Plumber Saved Civilization][book_carter_flushed]
- [Cavanagh 2010 Queering Bathrooms Gender Sexuality and the Hygienic Imagination][book_cavanagh_queering]
- [Collier 2007 The Humble Little Condom A History][book_collier_condom]
- [Davis 2020 Bathroom Battlegrounds How Public Restrooms Shape the Gender Order][book_davis_battlegrounds]
- [Eveleigh 2006 Bogs Baths and Basins The Story of Domestic Sanitation][book_eveleigh_bogs]
- [Fanger 1970 Thermal Comfort][book_fanger_1970_thermal_comfort]
- [George 2008 The Big Necessity][book_george_big_necessity]
- [Gershenson and Penner 2009 Ladies and Gents Public Toilets and Gender][book_gershenson_ladies_gents]
- [Greed 2003 Inclusive Urban Design Public Toilets][book_greed_inclusive]
- [Gross and Harris 1998 Fundamentals of Queueing Theory][book_gross_harris_1998_queueing]
- [Hinds 1999 Aerosol Technology][book_hinds_1999_aerosol]
- [Haas Rose and Gerba 2014 Quantitative Microbial Risk Assessment][book_haas_2014_qmra]
- [Halliday 1999 The Great Stink of London][book_halliday_great_stink]
- [Harington 1596 A New Discourse of a Stale Subject Called the Metamorphosis of Ajax][book_harington_ajax]
- [Hart-Davis 1997 Thunder Flush and Thomas Crapper][book_hart_davis]
- [Hodge Roman Aqueducts and Water Supply][book_hodge_aqueducts]
- [Horan 1996 The Porcelain God A Social History of the Toilet][book_horan_porcelain_god]
- [Jansen Koloski-Ostrow and Moormann 2011 Roman Toilets Their Archaeology and Cultural History][book_jansen_roman_toilets]
- [Kira 1966 The Bathroom][book_kira]
- [Kleinrock 1975 Queueing Systems Volume 1 Theory][book_kleinrock_1975_queueing]
- [Koloski-Ostrow 2015 The Archaeology of Sanitation in Roman Italy][book_koloski_ostrow]
- [Lambton 1995 Temples of Convenience and Chambers of Delight][book_lambton_temples]
- [Linder and Nygaard 1998 Void Where Prohibited][book_linder_void]
- [Long 2006 Architectural Acoustics][book_long_2006_architectural_acoustics]
- [Lowe 2018 No Place to Go How Public Toilets Fail Our Private Needs][book_lowe_no_place]
- [Molotch and Norén 2010 Toilet Public Restrooms and the Politics of Sharing][book_molotch_toilet]
- [Penner 2013 Bathroom][book_penner_bathroom]
- [Rappaport 2000 Shopping for Pleasure Women in the Making of London's West End][book_rappaport_shopping]
- [Reyburn 1969 Flushed with Pride The Story of Thomas Crapper][book_reyburn_flushed]
- [Sabine 1922 Collected Papers on Acoustics][book_sabine_1922_acoustics]
- [Shortle Thompson Gross and Harris 2018 Fundamentals of Queueing Theory][book_shortle_2018_queueing]
- [Smith 2007 Clean A History of Personal Hygiene and Purity][book_smith_clean]
- [Anthony 2017 Defined by Design][book_anthony_defined]
- [Eveleigh 2008 Privies and Water Closets][book_eveleigh_privies]
- [Ogle 1996 All the Modern Conveniences American Household Plumbing][book_ogle_modern_conveniences]
- [Okano and Nagare 2023 The Tokyo Toilet][book_okano_tokyotoilet]
- [Beranek Acoustics][book_beranek_acoustics]
- [Cockayne 2007 Hubbub Filth Noise and Stench in England][book_cockayne_hubbub]
- [Corbin 1986 The Foul and the Fragrant Odor and the French Social Imagination][book_corbin_foul_fragrant]
- [Gregory and James 2006 Toilets of the World][book_gregory_toilets_world]
- [Harris Handbook of Acoustical Measurements and Noise Control][book_harris_acoustical_handbook]
- [Hobson 2009 Latrinae et Foricae Toilets in the Roman World][book_hobson_latrinae]
- [Inglis 2001 A Sociological History of Excretory Experience][book_inglis_excretory]
- [Jackson 2014 Dirty Old London The Victorian Fight Against Filth][book_jackson_dirty_old_london]
- [Laporte 2000 History of Shit][book_laporte_history_shit]
- [Melosi 2000 The Sanitary City][book_melosi_sanitary_city]
- [Reid 1991 Paris Sewers and Sewermen][book_reid_paris_sewers]
- [Tanizaki In Praise of Shadows][book_tanizaki_shadows]
- [Wright 1960 Clean and Decent][book_wright_clean_decent]

### Reference

- [ANSI and Acoustical Society of America S3.5 Speech Intelligibility Index][ref_ansi_asa_s35_sii]
- [ASHRAE Standard 55 Thermal Environmental Conditions for Human Occupancy][ref_ashrae_55]
- [ASHRAE Standard 62.1 Ventilation for Acceptable Indoor Air Quality][ref_ashrae_62_1]
- [ASME A112.19.2 Ceramic Plumbing Fixtures][ref_asme_a112_19_2]
- [ASTM E1130 Objective Measurement of Speech Privacy][ref_astm_e1130]
- [ASTM E1573 Measurement and Reporting of Masking Sound Levels][ref_astm_e1573]
- [Cloaca Maxima][ref_cloaca_maxima_wiki]
- [Cintas America's Best Restroom Hall of Fame][ref_bestrestroom_hof]
- [Dezeen Shigeru Ban Transparent Tokyo Toilets][ref_dezeen_transparent]
- [Duravit SensoWash Starck f][ref_sensowash_duravit]
- [Duravit SensoWash Starck f AZ Award][ref_sensowash_azaward]
- [Education Commission of the States Free Menstrual Products in Schools][ref_ecs_period]
- [Energy Policy Act of 1992][ref_epact_1992]
- [EPA WaterSense Residential Toilets][ref_epa_watersense_toilets]
- [Flush Toilets at the Great Exhibition][ref_great_exhibition_toilets]
- [GOV.UK Free Period Product Scheme for Schools and Colleges][ref_gov_uk_period]
- [Historic UK The History of Women's Public Toilets in Britain][ref_historic_uk_womens]
- [ICC International Plumbing Code Options for Modern Public Restrooms][ref_icc_ipc]
- [Institution of Civil Engineers Sir Joseph Bazalgette][ref_ice_bazalgette]
- [International Plumbing Code Section 403.1 Minimum Plumbing Fixtures][ref_ipc_fixture_403]
- [International Plumbing Code Chapter 10 Traps][ref_ipc_traps_1002]
- [ISO 7730 Analytical Determination of Thermal Comfort PMV and PPD][ref_iso_7730]
- [John Banzhaf Potty Parity][ref_banzhaf_potty]
- [Julius Fromm][ref_fromm_wiki]
- [London Museum The Great Stink of 1858][ref_london_museum_stink]
- [Loo of the Year Awards][ref_loty_wiki]
- [Maximum Performance Toilet Testing][ref_map_testing]
- [New Atlas Kohler Numi][ref_numi_newatlas]
- [CNBC Kohler Numi 2.0 with Amazon Alexa][ref_numi2_cnbc]
- [Nippon.com High-Tech Toilets Become Standard Household Equipment in Japan][ref_nippon_hightech]
- [NPR Otohime Sound Device][ref_npr_otohime]
- [One Point Partitions American versus European Bathroom Stalls][ref_onepoint_stalls]
- [Perfect Days Film][ref_perfectdays_wiki]
- [Period Products Free Provision Scotland Act 2021][ref_scotland_period_act]
- [Red Dot Award Neorest NX][ref_neorest_nx_reddot]
- [Restroom Attendant][ref_attendant_wiki]
- [Smithsonian Three True Things About Thomas Crapper][ref_smithsonian_crapper]
- [Smithsonian National Museum of American History Modess Dispenser][ref_smithsonian_modess]
- [The Nippon Foundation The Tokyo Toilet][ref_nippon_tokyotoilet]
- [TOTO The Little-Known History of Washlet Bidet Seats][ref_toto_history]
- [TOTO Neorest 750H][ref_neorest_750h]
- [TOTO Washlet Shipments Pass 70 Million Units][ref_toto_70million]
- [Uniform Plumbing Code Minimum Plumbing Facilities][ref_upc_fixtures]
- [United Nations World Toilet Day][ref_un_toilet_day]
- [UK National Archives Innovations in Toilet Design][ref_national_archives_toilet]
- [Vice How the Nazis Annihilated Julius Fromm's Condom Empire][ref_vice_fromm]
- [Web Japan TOTO Otohime][ref_webjapan_otohime]
- [World History Encyclopedia Toilets in a Medieval Castle][ref_worldhistory_medieval]
- [World Toilet Organization][ref_wto_wiki]
- [London Museum Selfridges Store That Shook Up London Shopping][ref_selfridges_london_museum]
- [Wallpaper Sketch London Design History][ref_sketch_wallpaper]
- [ADA 2010 Standards for Accessible Design][ref_ada_2010_standards]
- [American Restroom Association][ref_american_restroom_assoc]
- [Code of Federal Regulations Title 10 Part 430 Energy Conservation Program][ref_ecfr_10_430]
- [EPA WaterSense Product Specifications][ref_epa_watersense_specs]
- [Frontinus On the Water Management of the City of Rome][ref_frontinus_aqueducts]
- [Pliny the Elder The Natural History][ref_pliny_natural_history]
- [United Nations General Assembly Resolution 67/291 Sanitation for All][ref_un_res_67_291]
- [United States Access Board ADA Accessibility Standards][ref_access_board_ada]
- [Vitruvius De Architectura][ref_vitruvius_architecture]
- [World Health Organization Sanitation Fact Sheet][ref_who_sanitation]
- [World Health Organization and UNICEF Joint Monitoring Programme for Water Supply Sanitation and Hygiene][ref_who_unicef_jmp]
- [American Standard Companies][ref_amstd_wiki]
- [American Standard SpaLet Bidet Toilets][ref_spalet_americanstandard]
- [World Health Organization Guidelines on Hand Hygiene in Health Care][ref_who_hand_hygiene]
- [British Toilet Association About][ref_bta_about]
- [Cintas Crowns 2024 America's Best Restroom Winner][ref_cintas_2024]
- [Condom Machine][ref_condom_machine_wiki]
- [Criterion Collection Perfect Days][ref_criterion_perfectdays]
- [DXV AT200 SpaLet Bidet Toilet][ref_dxv_at200]
- [Environmental News Network The Sound Princess][ref_sound_princess_enn]
- [George Jennings][ref_jennings_wiki]
- [Guinness World Records First Flushing Toilet][ref_guinness_first_flush]
- [Heritage Calling The Story of London's Sewer System][ref_heritage_london_sewers]
- [Historic England Spending a Penny Collection][ref_historic_england_penny]
- [Vending Machine][ref_vending_machine_wiki]
- [History Hit Alexander Cummings Pioneer of the Flush Toilet][ref_historyhit_cumming]
- [History Hit How the Ancient Romans Went to the Toilet][ref_historyhit_roman]
- [IOL Sound Princess Eliminates Toilet Noises][ref_sound_princess_iol]
- [Japan Sanitary Equipment Industry Association About the Spray Seat][ref_sanitary_net]
- [Kohler Co.][ref_kohler_wiki]
- [Loo of the Year Awards Official][ref_loty_official]
- [Marshall Field's][ref_marshall_fields_wiki]
- [Marshall Field's Tea Room][ref_marshall_fields_tearoom]
- [Men Without Women Mural][ref_men_without_women_wiki]
- [Nippon Foundation All 17 Tokyo Toilets Completed][ref_nippon_17complete]
- [Nippon.com The TOTO Museum and Japan's Toilet Culture][ref_nippon_toto_museum]
- [Nippon.com Wim Wenders and Perfect Days][ref_nippon_perfectdays]
- [PR Newswire Global Sales of TOTO Washlet Exceed 50 Million][ref_prnewswire_50m]
- [PR Newswire TOTO Washlet Line Exceeds 60 Million Units][ref_prnewswire_60m]
- [Radio City Music Hall][ref_radio_city_wiki]
- [Roca Company][ref_roca_wiki]
- [Royal Collection Trust The Metamorphosis of Ajax][ref_rct_harington]
- [ScentAir What Is Scent Marketing][ref_scentair]
- [Science Museum A Flushing Story][ref_science_museum_flushing]
- [Smithsonian How the Ancient Romans Went to the Bathroom][ref_smithsonian_roman]
- [Toilets in Japan][ref_toilets_japan_wiki]
- [Toto Ltd.][ref_toto_wiki]
- [TOTO Washlet 40th Anniversary][ref_toto_40th]
- [TOTO Ten Little-Known Facts About Washlet Bidet Seats][ref_toto_10facts]
- [The Tokyo Toilet][ref_tokyotoilet_wiki]
- [United Nations General Assembly Resolution 67/291 World Toilet Day][ref_un_ga11397]
- [University of Cambridge Roman Toilets Gave No Clear Health Benefit][ref_cambridge_roman_parasites]
- [Villeroy and Boch][ref_vb_wiki]
- [Washlet][ref_washlet_wiki]
- [World Toilet Organization About Us][ref_wto_about]

### Research

- [Aiello and colleagues 2008 Effect of Hand Hygiene on Infectious Disease Risk in the Community Setting][research_aiello_2008]
- [Anthony and Dufresne 2007 Potty Parity in Perspective][research_anthony_dufresne_2007]
- [Barber and Scarcelli 2009 Clean Restrooms How Important Are They][research_barber_2009]
- [Curtis and Cairncross 2003 Effect of Washing Hands with Soap on Diarrhoea Risk][research_curtis_cairncross_2003]
- [Freeman and colleagues 2014 Hygiene and Health Systematic Review of Handwashing Practices Worldwide][research_freeman_2014]
- [Larson 1995 APIC Guideline for Handwashing and Hand Antisepsis][research_larson_1995]
- [Barker and Jones 2005 Aerosol Contamination of Surfaces After Flushing a Domestic Toilet][research_barker_jones_2005]
- [Best and Redway 2014 Comparison of Hand-Drying Methods and Airborne Microbe Dispersal][research_best_redway_2014]
- [Best Sandoe and Wilcox 2012 Aerosolization of Clostridium difficile and the Role of Toilet Lids][research_best_wilcox_2012]
- [Huesca-Espitia and colleagues 2018 Deposition of Bacteria by Bathroom Hot-Air Hand Dryers][research_huesca_espitia_2018]
- [Kimmitt and Redway 2016 Virus Dispersal During Hand Drying][research_kimmitt_redway_2016]
- [Park and colleagues 2020 A Mountable Toilet System for Personalized Health Monitoring][research_park_2020_smart_toilet]
- [Scobie 1986 Slums Sanitation and Mortality in the Roman World][research_scobie_1986]
- [Barber and Scarcelli 2010 Cleanliness Measurement Scale][research_barber_2010]
- [Beyond Potty Parity Public Toilets Gendered Time Costs][research_beyond_potty_parity]
- [Bitner 1992 Servicescapes The Impact of Physical Surroundings][research_bitner]
- [Crimaldi and colleagues 2022 Commercial Toilets Emit Energetic Aerosol Plumes][research_crimaldi_2022_plume]
- [Do Women Spend More Time in the Restroom than Men][research_do_women_spend_more]
- [Erlang 1917 Solution of Some Problems in the Theory of Probabilities][research_erlang_1917]
- [Farajollahzadeh and Hu Potty Parity][research_farajollahzadeh_hu_potty]
- [Farajollahzadeh Hu and Roshanaei 2025 Potty Parity Stadium Restroom Design][research_farajollahzadeh_stadium]
- [Lewkowitz and Gilliland 2025 A Feminist Critical Analysis of Public Toilets and Gender][research_feminist_critical]
- [Gerba Wallis and Melnick 1975 Microbiological Hazards of Household Toilets][research_gerba_1975_plume]
- [Hao Wen 2024 Tokyo Sanitization Wim Wenders Perfect Days][research_haowen_mediapolis]
- [Huh and colleagues 2019 The Potty Parity Problem][research_huh_2019_potty]
- [Johnson and colleagues 2013 Lifting the Lid on Toilet Plume Aerosol][research_johnson_2013_plume]
- [Kim and Bachman 2019 Restaurant Restroom Cleanliness Satisfaction and Intent to Return][research_kim_bachman_2019]
- [Kogan 2007 Sex Separation in Public Restrooms Law Architecture and Gender][research_kogan_sex_separation]
- [Kogan 2017 Public Restrooms and the Distorting of Transgender Identity][research_kogan_transgender]
- [Little 1961 A Proof for the Queuing Formula L Equals Lambda W][research_little_1961]
- [Mari and Poggesi 2013 Servicescape Cues and Customer Behavior][research_mari_poggesi]
- [Mitchell 2017 Human Parasites in the Roman World][research_mitchell_parasites]
- [Nicas and Best 2008 A Study Quantifying the Hand-to-Face Contact Rate][research_nicas_best_2008]
- [Rawls 1988 Restroom Usage in Selected Public Buildings and Facilities][research_rawls_1988]
- [Spangenberg Crowley and Henderson 1996 Improving the Store Environment Olfactory Cues][research_spangenberg]
- [Sydnor and colleagues 2012 Electronic-Eye Faucets Legionella Species Contamination][research_sydnor_2012_faucet]
- [Szczygiel 2016 From Night Soil to Washlet The Material Culture of Japanese Toilets][research_szczygiel_ejcjs]
- [Vilnai-Yavetz and Gilboa 2010 The Effect of Servicescape Cleanliness on Customer Reactions][research_vilnai_yavetz_2010]
- [A World of Unmentionable Suffering Women's Public Conveniences in Victorian London][research_unmentionable_suffering]
- [Bryn Mawr Classical Review of Roman Toilets][research_bmcr_roman_toilets]
- [Hopkins 2007 The Cloaca Maxima and the Monumental Manipulation of Water in Archaic Rome][research_hopkins_cloaca]
- [Menstrual Products in Schools A Scan of Fifty States and the District of Columbia][research_menstrual_legal_landscape]
- [Mitchell 2017 Human Parasites in the Roman World Cambridge Repository][research_mitchell_cam]
- [Review of The Archaeology of Sanitation in Roman Italy in Isis][research_ostrow_isis]
- [Szczygiel Cultural Origins of Japan's Premodern Night Soil Collection System][research_szczygiel_nightsoil]
- [Taştan and Soylu 2023 The Impact of Perceived Cleanliness][research_tastan_soylu_2023]

[book_aly_fromms]: https://openlibrary.org/works/OL756171W
[book_bryson_at_home]: https://archive.org/details/athomeshorthisto0000brys
[book_carter_flushed]: https://www.simonandschuster.com/books/Flushed/W-Hodding-Carter/9780743474092
[book_cavanagh_queering]: https://openlibrary.org/works/OL26466983W
[book_collier_condom]: https://openlibrary.org/works/OL9913348W
[book_davis_battlegrounds]: https://doi.org/10.1525/9780520971660
[book_eveleigh_bogs]: https://archive.org/details/bogsbathsbasinss0000evel
[book_fanger_1970_thermal_comfort]: https://archive.org/details/thermalcomfortan0000fang
[book_george_big_necessity]: https://us.macmillan.com/books/9781250058300/thebignecessity/
[book_gershenson_ladies_gents]: https://tupress.temple.edu/books/ladies-and-gents
[book_greed_inclusive]: https://openlibrary.org/works/OL3953277W
[book_haas_2014_qmra]: https://onlinelibrary.wiley.com/doi/book/10.1002/9781118910030
[book_halliday_great_stink]: https://thehistorypress.co.uk/publication/the-great-stink-of-london/
[book_harington_ajax]: https://www.exclassics.com/ajax/ajaxintr.htm
[book_hart_davis]: https://archive.org/details/thunderflushthom0000hart
[book_hodge_aqueducts]: https://archive.org/details/romanaqueductswa0000hodg
[book_horan_porcelain_god]: https://openlibrary.org/works/OL2982700W
[book_jansen_roman_toilets]: https://shs.hal.science/halshs-02288198
[book_kira]: https://openlibrary.org/works/OL6912148W
[book_kleinrock_1975_queueing]: https://www.wiley.com/en-us/Queueing+Systems%2C+Volume+1%3A+Theory-p-9780471491101
[book_koloski_ostrow]: https://archive.org/details/archaeologyofsan0000kolo
[book_lambton_temples]: https://archive.org/details/templesofconveni0000lamb
[book_linder_void]: https://openlibrary.org/works/OL2003849W
[book_long_2006_architectural_acoustics]: https://books.google.com/books/about/Architectural_Acoustics.html?id=MnYUfErtBGEC
[book_lowe_no_place]: https://chbooks.com/Books/N/No-Place-to-Go
[book_molotch_toilet]: https://nyupress.org/9780814795880/toilet/
[book_penner_bathroom]: https://reaktionbooks.co.uk/work/bathroom
[book_rappaport_shopping]: https://openlibrary.org/works/OL11594739W
[book_reyburn_flushed]: https://archive.org/details/flushedwithpride0000reyb_r5x1
[book_sabine_1922_acoustics]: https://archive.org/details/collectedpaperso00sabi
[book_shortle_2018_queueing]: https://www.wiley.com/en-us/Fundamentals+of+Queueing+Theory,+5th+Edition-p-9781118943526
[book_smith_clean]: https://openlibrary.org/works/OL16070814W
[book_wright_clean_decent]: https://archive.org/details/cleandecentfasci0000wrig
[ref_ansi_asa_s35_sii]: https://webstore.ansi.org/standards/asa/ansiasas31997r2020
[ref_ashrae_55]: https://www.ashrae.org/technical-resources/bookstore/standard-55-thermal-environmental-conditions-for-human-occupancy
[ref_ashrae_62_1]: https://www.ashrae.org/technical-resources/bookstore/standards-62-1-62-2
[ref_asme_a112_19_2]: https://www.asme.org/codes-standards/find-codes-standards/a112-19-2-csa-b45-1-ceramic-plumbing-fixtures
[ref_astm_e1130]: https://www.astm.org/e1130-16r21.html
[ref_astm_e1573]: https://www.astm.org/e1573-22.html
[ref_cloaca_maxima_wiki]: https://en.wikipedia.org/wiki/Cloaca_Maxima
[ref_bestrestroom_hof]: https://www.bestrestroom.com/hall-of-fame/
[ref_dezeen_transparent]: https://www.dezeen.com/2020/08/17/shigeru-ban-transparent-toyko-toilet-shibuya/
[ref_sensowash_duravit]: https://www.duravit.com/en-us/products/all-series/sensowash-r-starck-f/
[ref_sensowash_azaward]: https://www.v2com-newswire.com/en/newsroom/press-kits/5661-01/duravit-sensowash-starck-f-shower-toilet-wins-2021-az-award-for-architectural-product-design
[ref_ecs_period]: https://www.ecs.org/states-address-period-poverty-with-free-menstrual-products-in-schools/
[ref_epact_1992]: https://www.govinfo.gov/app/details/STATUTE-106/STATUTE-106-Pg2776
[ref_epa_watersense_toilets]: https://www.epa.gov/watersense/residential-toilets
[ref_great_exhibition_toilets]: https://en.wikipedia.org/wiki/Flush_toilets_at_the_Great_Exhibition
[ref_gov_uk_period]: https://www.gov.uk/government/news/free-period-product-scheme-for-schools-and-colleges-extended
[ref_historic_uk_womens]: https://www.historic-uk.com/CultureUK/History-of-Womens-Public-Toilets-in-Britain/
[ref_icc_ipc]: https://www.iccsafe.org/building-safety-journal/bsj-technical/international-plumbing-code-providing-options-for-designers-of-modern-public-restrooms/
[ref_ice_bazalgette]: https://www.ice.org.uk/what-is-civil-engineering/meet-the-engineers/sir-joseph-bazalgette
[ref_ipc_fixture_403]: https://codes.iccsafe.org/s/IPC2021P1/chapter-4-fixtures-faucets-and-fixture-fittings/IPC2021P1-Ch04-Sec403.1
[ref_ipc_traps_1002]: https://codes.iccsafe.org/content/IPC2018/chapter-10-traps-interceptors-and-separators
[ref_iso_7730]: https://www.iso.org/standard/39155.html
[ref_banzhaf_potty]: http://banzhaf.net/pottyparity.html
[ref_fromm_wiki]: https://en.wikipedia.org/wiki/Julius_Fromm
[ref_london_museum_stink]: https://www.londonmuseum.org.uk/collections/london-stories/great-stink-of-1858/
[ref_loty_wiki]: https://en.wikipedia.org/wiki/Loo_of_the_Year_Awards
[ref_map_testing]: https://map-testing.com/toilet-types/
[ref_numi_newatlas]: https://newatlas.com/kohler-numi-toilet/27223/
[ref_numi2_cnbc]: https://www.cnbc.com/2019/01/08/kohlers-7000-numi-2point0-toilet-with-amazon-alexa-built-in.html
[ref_nippon_hightech]: https://www.nippon.com/en/features/h00185/high-tech-toilets-become-standard-household-equipment-in-japan.html
[ref_npr_otohime]: https://www.npr.org/transcripts/526005547
[ref_onepoint_stalls]: https://onepointpartitions.com/blog/2022/11/30/american-bathroom-stalls-vs-european/
[ref_perfectdays_wiki]: https://en.wikipedia.org/wiki/Perfect_Days
[ref_scotland_period_act]: https://www.legislation.gov.uk/asp/2021/1
[ref_neorest_nx_reddot]: https://www.red-dot.org/project/neorest-nx-22704-22703
[ref_attendant_wiki]: https://en.wikipedia.org/wiki/Restroom_attendant
[ref_smithsonian_crapper]: https://www.smithsonianmag.com/smart-news/three-true-things-about-sanitary-engineer-thomas-crapper-180965008/
[ref_smithsonian_modess]: https://americanhistory.si.edu/collections/object/nmah_688117
[ref_nippon_tokyotoilet]: https://en.nippon-foundation.or.jp/what/projects/communities/thetokyotoilet
[ref_toto_history]: https://www.totousa.com/blog/toto-s-declaration-of-innovation-br-the-little-known-history-of-washlet-bidet-seats-development
[ref_neorest_750h]: https://www.totousa.com/neorest-750h
[ref_toto_70million]: https://asia.toto.com/company-news/cumulative-washlet-shipments-have-now-passed-70-million-units/
[ref_upc_fixtures]: https://iapmo.org/codes-standards-development/code-development/uniform-plumbing-code
[ref_un_toilet_day]: https://www.un.org/en/observances/toilet-day
[ref_national_archives_toilet]: https://www.nationalarchives.gov.uk/explore-the-collection/explore-by-topic/business-finance-and-innovation/toilet-design/
[ref_vice_fromm]: https://www.vice.com/en/article/inventor-condom-vending-machine-julius-fromm/
[ref_webjapan_otohime]: https://web-japan.org/kidsweb/hitech/toilet/toilet04.html
[ref_worldhistory_medieval]: https://www.worldhistory.org/article/1239/toilets-in-a-medieval-castle/
[ref_wto_wiki]: https://en.wikipedia.org/wiki/World_Toilet_Organization
[ref_selfridges_london_museum]: https://www.londonmuseum.org.uk/collections/london-stories/selfridges-store-shook-up-london-shopping/
[ref_sketch_wallpaper]: https://www.wallpaper.com/design-interiors/sketch-london-design-history
[research_anthony_dufresne_2007]: https://doi.org/10.1177/0885412206295846
[research_barber_2009]: https://doi.org/10.1111/j.1748-0159.2009.00155.x
[research_barber_2010]: https://doi.org/10.1108/09604521011011630
[research_beyond_potty_parity]: https://www.mdpi.com/2075-471X/15/3/55
[research_bitner]: https://doi.org/10.1177/002224299205600205
[research_crimaldi_2022_plume]: https://www.nature.com/articles/s41598-022-24686-5
[research_do_women_spend_more]: https://www.researchgate.net/publication/41137857_Do_Women_Spend_More_Time_in_the_Restroom_than_Men
[research_erlang_1917]: https://mathshistory.st-andrews.ac.uk/Biographies/Erlang/
[research_farajollahzadeh_hu_potty]: https://pubsonline.informs.org/doi/10.1287/mnsc.2021.04075
[research_farajollahzadeh_stadium]: https://doi.org/10.1287/ited.2023.0051ca
[research_feminist_critical]: https://journals.sagepub.com/doi/10.1177/10780874241233529
[research_gerba_1975_plume]: https://journals.asm.org/doi/10.1128/am.30.2.229-237.1975
[research_haowen_mediapolis]: https://www.mediapolisjournal.com/2024/04/tokyo-sanitization/
[research_huh_2019_potty]: https://www.sciencedirect.com/science/article/abs/pii/S0038012118300521
[research_johnson_2013_plume]: https://www.ajicjournal.org/article/S0196-6553(12)00812-7/fulltext
[research_kim_bachman_2019]: https://doi.org/10.1080/15378020.2019.1596002
[research_kogan_sex_separation]: https://www.researchgate.net/publication/303874037_SEX_SEPARATION_IN_PUBLIC_RESTROOMS_LAW_ARCHITECTURE_AND_GENDER
[research_kogan_transgender]: https://dc.law.utah.edu/scholarship/32/
[research_little_1961]: https://doi.org/10.1287/opre.9.3.383
[research_mari_poggesi]: https://doi.org/10.1080/02642069.2011.613934
[research_mitchell_parasites]: https://doi.org/10.1017/S0031182015001651
[research_nicas_best_2008]: https://www.tandfonline.com/doi/full/10.1080/15459620802003896
[research_rawls_1988]: https://vtechworks.lib.vt.edu/items/0ab3b38f-6b97-48f9-b772-3926f8950f9e
[research_spangenberg]: https://doi.org/10.1177/002224299606000205
[research_sydnor_2012_faucet]: https://www.cambridge.org/core/journals/infection-control-and-hospital-epidemiology/article/abs/electroniceye-faucets-legionella-species-contamination-in-healthcare-settings/5E1A7B3DB6C652C4D4985B9B98C963A1
[research_szczygiel_ejcjs]: https://www.japanesestudies.org.uk/ejcjs/vol16/iss3/szczygiel.html
[research_vilnai_yavetz_2010]: https://doi.org/10.1080/15332961003604386
[research_unmentionable_suffering]: https://www.researchgate.net/publication/40804931_A_World_of_Unmentionable_Suffering_Women's_Public_Conveniences_in_Victorian_London
[book_anthony_defined]: https://openlibrary.org/works/OL21139633W
[book_eveleigh_privies]: https://www.waterstones.com/book/privies-and-water-closets/david-eveleigh/9780747807025
[book_ogle_modern_conveniences]: https://books.google.com/books/about/All_the_Modern_Conveniences.html?id=lXrbAAAAMAAJ
[book_okano_tokyotoilet]: https://moom.com.tw/en/item/the-tokyo-toilet
[book_tanizaki_shadows]: https://en.wikipedia.org/wiki/In_Praise_of_Shadows
[ref_amstd_wiki]: https://en.wikipedia.org/wiki/American_Standard_Companies
[ref_spalet_americanstandard]: https://www.americanstandard-us.com/pages/spalet-bidet-toilets-toilet-seats
[ref_bta_about]: http://www.btaloos.co.uk/?page_id=7
[ref_cintas_2024]: https://www.cintas.com/newsroom/details/news/2024/10/15/cintas-crowns-maverik-adventure-s-first-stop-2024-america-s-best-restroom-contest-winner/
[ref_condom_machine_wiki]: https://en.wikipedia.org/wiki/Condom_machine
[ref_criterion_perfectdays]: https://www.criterion.com/films/34274-perfect-days
[ref_dxv_at200]: https://www.dxv.com/electronic-bidet-toilets/at200ls-dual-flush-elongated-spalet-bidet-toilet/canvas-white-d29030cs416415
[ref_guinness_first_flush]: https://www.guinnessworldrecords.com/world-records/449875-first-flushing-toilet
[ref_heritage_london_sewers]: https://heritagecalling.com/2019/03/28/the-story-of-londons-sewer-system/
[ref_historyhit_cumming]: https://www.historyhit.com/alexander-cummings-the-scottish-pioneer-of-the-flush-toilet/
[ref_historyhit_roman]: https://www.historyhit.com/how-the-ancient-romans-went-to-the-toilet/
[ref_jennings_wiki]: https://en.wikipedia.org/wiki/George_Jennings
[ref_kohler_wiki]: https://en.wikipedia.org/wiki/Kohler_Co.
[ref_loty_official]: https://www.loo.co.uk/
[ref_marshall_fields_tearoom]: https://restaurant-ingthroughhistory.com/2008/12/11/department-store-restaurants-marshall-fields/
[ref_marshall_fields_wiki]: https://en.wikipedia.org/wiki/Marshall_Field's
[ref_men_without_women_wiki]: https://en.wikipedia.org/wiki/Men_Without_Women_(mural)
[ref_nippon_17complete]: https://en.nippon-foundation.or.jp/news/articles/2023/20230623-91309.html
[ref_nippon_perfectdays]: https://www.nippon.com/en/japan-topics/c030250/
[ref_nippon_toto_museum]: https://www.nippon.com/en/guide-to-japan/gu900284/
[ref_prnewswire_50m]: https://www.prnewswire.com/news-releases/global-sales-of-totos-popular-washlet-line-exceed-50-million-300942706.html
[ref_prnewswire_60m]: https://www.prnewswire.com/news-releases/totos-popular-washlet-line-exceeds-60-million-units-sold-worldwide-301706757.html
[ref_radio_city_wiki]: https://en.wikipedia.org/wiki/Radio_City_Music_Hall
[ref_rct_harington]: https://www.rct.uk/collection/1121134/a-new-discourse-of-a-stale-subject-called-the-metamorphosis-of-ajax
[ref_roca_wiki]: https://en.wikipedia.org/wiki/Roca_(company)
[ref_sanitary_net]: https://www.sanitary-net.com/global/about/spray-seat.html
[ref_scentair]: https://scentair.com/newscenter/what-scent-marketing-simple-definition/
[ref_science_museum_flushing]: https://blog.sciencemuseum.org.uk/a-flushing-story/
[ref_smithsonian_roman]: https://www.smithsonianmag.com/history/how-the-ancient-romans-went-to-the-bathroom-180979056/
[ref_sound_princess_enn]: https://www.enn.com/articles/150-the-sound-princess--gadget-helps-bathroom-bashful-japanese-women
[ref_sound_princess_iol]: https://iol.co.za/news/eish/2004-10-04-sound-princess-eliminates-toilet-noises/
[ref_toilets_japan_wiki]: https://en.wikipedia.org/wiki/Toilets_in_Japan
[ref_tokyotoilet_wiki]: https://en.wikipedia.org/wiki/The_Tokyo_Toilet
[ref_toto_10facts]: https://www.totousa.com/blog/10-little-known-facts-about-washlet-bidet-seats
[ref_toto_40th]: https://www.totousa.com/press/washlet-40-anniversary
[ref_toto_wiki]: https://en.wikipedia.org/wiki/Toto_Ltd.
[ref_un_ga11397]: https://press.un.org/en/2013/ga11397.doc.htm
[ref_vb_wiki]: https://en.wikipedia.org/wiki/Villeroy_%26_Boch
[ref_washlet_wiki]: https://en.wikipedia.org/wiki/Washlet
[ref_wto_about]: https://worldtoilet.org/web-agency-gb-about-us/
[ref_cambridge_roman_parasites]: https://www.cam.ac.uk/research/news/roman-toilets-gave-no-clear-health-benefit-and-romanisation-actually-spread-parasites
[research_bmcr_roman_toilets]: https://bmcr.brynmawr.edu/2012/2012.03.34/
[research_hopkins_cloaca]: https://www.researchgate.net/publication/265225213_The_Cloaca_Maxima_and_the_monumental_manipulation_of_water_in_archaic_Rome
[research_menstrual_legal_landscape]: https://www.sciencedirect.com/science/article/pii/S1353829225001753
[research_mitchell_cam]: https://www.repository.cam.ac.uk/handle/1810/267257
[research_ostrow_isis]: https://www.journals.uchicago.edu/doi/10.1086/707660
[research_szczygiel_nightsoil]: https://www.whp-journals.co.uk/WW/article/download/1044/592/5447
[research_tastan_soylu_2023]: https://doi.org/10.31822/jomat.2023-8-1-27
[book_gross_harris_1998_queueing]: https://books.google.com/books/about/Fundamentals_of_Queueing_Theory.html?id=K3lQGeCtAJgC
[book_hinds_1999_aerosol]: https://www.wiley.com/en-us/Aerosol+Technology%3A+Properties%2C+Behavior%2C+and+Measurement+of+Airborne+Particles%2C+3rd+Edition-p-9781119494041
[ref_historic_england_penny]: https://historicengland.org.uk/images-books/archive/collections/photographs/spending-a-penny/
[ref_vending_machine_wiki]: https://en.wikipedia.org/wiki/Vending_machine
[book_beranek_acoustics]: https://openlibrary.org/search?q=Beranek+Acoustics
[book_cockayne_hubbub]: https://openlibrary.org/search?q=Hubbub+Filth+Noise+Stench+Cockayne
[book_corbin_foul_fragrant]: https://openlibrary.org/search?q=The+Foul+and+the+Fragrant+Corbin
[book_gregory_toilets_world]: https://openlibrary.org/search?q=Toilets+of+the+World+Gregory
[book_harris_acoustical_handbook]: https://openlibrary.org/search?q=Handbook+of+Acoustical+Measurements+and+Noise+Control+Harris
[book_hobson_latrinae]: https://openlibrary.org/search?q=Latrinae+et+Foricae+Hobson
[book_inglis_excretory]: https://openlibrary.org/search?q=Sociological+History+of+Excretory+Experience+Inglis
[book_jackson_dirty_old_london]: https://openlibrary.org/search?q=Dirty+Old+London+Lee+Jackson
[book_laporte_history_shit]: https://openlibrary.org/search?q=History+of+Shit+Laporte
[book_melosi_sanitary_city]: https://openlibrary.org/search?q=The+Sanitary+City+Melosi
[book_reid_paris_sewers]: https://openlibrary.org/search?q=Paris+Sewers+and+Sewermen+Reid
[ref_ada_2010_standards]: https://www.ada.gov/law-and-regs/design-standards/2010-stds/
[ref_american_restroom_assoc]: https://americanrestroom.org/
[ref_who_hand_hygiene]: https://www.who.int/publications/i/item/9789241597906
[research_barker_jones_2005]: https://doi.org/10.1111/j.1365-2672.2005.02610.x
[research_best_redway_2014]: https://doi.org/10.1016/j.jhin.2014.11.006
[research_best_wilcox_2012]: https://doi.org/10.1016/j.jhin.2011.12.008
[research_huesca_espitia_2018]: https://doi.org/10.1128/AEM.00044-18
[research_kimmitt_redway_2016]: https://doi.org/10.1111/jam.13014
[research_park_2020_smart_toilet]: https://www.nature.com/articles/s41551-020-0534-9
[research_scobie_1986]: https://doi.org/10.1524/klio.1986.68.68.399
[ref_access_board_ada]: https://www.access-board.gov/ada/
[ref_ecfr_10_430]: https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430
[ref_epa_watersense_specs]: https://www.epa.gov/watersense/product-specifications
[ref_frontinus_aqueducts]: https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Frontinus/De_Aquis/home.html
[ref_pliny_natural_history]: https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0137
[ref_un_res_67_291]: https://docs.un.org/en/A/RES/67/291
[ref_vitruvius_architecture]: https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Vitruvius/home.html
[ref_who_sanitation]: https://www.who.int/news-room/fact-sheets/detail/sanitation
[ref_who_unicef_jmp]: https://washdata.org/
[research_aiello_2008]: https://doi.org/10.2105/AJPH.2007.124610
[research_curtis_cairncross_2003]: https://doi.org/10.1016/S1473-3099(03)00606-6
[research_freeman_2014]: https://doi.org/10.1111/tmi.12339
[research_larson_1995]: https://doi.org/10.1016/0196-6553(95)90070-5
