---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: Evolutionary and Open-Ended Adaptation"
date:   2025-12-29 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 12
---

<!-- A261 -->
<script>console.log("A261");</script>

Evolutionary and open-ended adaptation frames learning as a population-level search process in which candidate solutions are progressively refined through selection, variation, and recombination. The framework departs from the gradient-based optimization that organizes most of the preceding articles by treating the fitness landscape as a black-box function evaluated through interaction rather than differentiated through backpropagation. The absence of gradient information admits distinctive algorithmic responses including population-based search, novelty-seeking exploration, coevolution among interacting populations, and open-ended systems that continually invent their own objectives. The account has proved valuable for optimization problems where gradients are unavailable or unreliable, for the discovery of qualitatively-diverse solutions rather than single optima, and for the design of environments that provide continual challenge to their inhabitants. This article surveys the science and theory of evolutionary and open-ended adaptation as they stand in the mid 2020s. Coverage includes the classical genetic algorithm, evolution strategy, and genetic programming frameworks, modern deep neuroevolution and evolution strategies at scale, swarm intelligence and estimation-of-distribution algorithms, developmental encoding and artificial morphogenesis, novelty search and quality-diversity methods, multi-objective evolutionary algorithms, symbolic regression and program synthesis, open-endedness and the POET framework, artificial life and digital evolution, coevolution and multi-agent evolutionary dynamics, neural architecture search, hybrid evolutionary reinforcement learning, cultural evolution and language-model-mediated adaptation, meta-evolution of learning rules, theoretical frameworks including the schema theorem and no-free-lunch results, empirical benchmarks, and the biological correspondence to evolutionary theory, the Baldwin effect, and evo-devo. Article eleven treated learning from other agents. The present article treats learning through evolutionary population dynamics that may operate across single lifetimes or across generations.

## The Evolutionary Adaptation Problem

The evolutionary adaptation problem is specified by a population of candidate solutions and a fitness function that evaluates each candidate. At each generation, selection favors high-fitness candidates, variation operators produce new candidates through mutation or recombination, and the resulting population replaces the prior one. Formally, given a fitness function $F : \mathcal{X} \to \mathbb{R}$ over a solution space $\mathcal{X}$, an evolutionary algorithm maintains a population

$$\mathcal{P}_t = \{x_1^{(t)}, x_2^{(t)}, \ldots, x_N^{(t)}\}, \quad x_i^{(t)} \in \mathcal{X}$$

and iteratively updates the population through a triple of operations. Selection maps the current population to a distribution $s(\mathcal{P}\_t)$ that favors high-fitness individuals. Variation operators apply mutation $m : \mathcal{X} \to \mathcal{X}$ and recombination $r : \mathcal{X} \times \mathcal{X} \to \mathcal{X}$ to selected parents to produce offspring. Replacement combines offspring and prior population into the next generation $\mathcal{P}\_{t+1}$. The general evolutionary update rule takes the form

$$\mathcal{P}_{t+1} = \text{replace}\!\left(\mathcal{P}_t, \, \{m(r(s(\mathcal{P}_t), s(\mathcal{P}_t))) \, : \, i = 1, \ldots, \lambda\}\right)$$

with $\lambda$ offspring generated per generation. evolutionary algorithms differ in the concrete instantiation of the selection, variation, and replacement operators.

The fitness function itself admits several formalizations. In the simplest case, fitness is a deterministic function of the candidate, and the problem reduces to black-box optimization. In more complex cases, fitness depends on the interaction of the candidate with the environment or with other agents, producing stochastic or non-stationary fitness landscapes. In the most general case, fitness is not specified in advance but emerges from the interaction of candidates with an open-ended environment that itself evolves in response to the population.

The evolutionary framework differs from gradient-based learning in several distinctive ways. Fitness need not be differentiable, permitting optimization over discrete structures, sparse rewards, and other settings where gradient methods struggle. The population maintains diversity that supports the discovery of qualitatively-distinct solutions rather than convergence to a single optimum. Multiple candidates are evaluated in parallel, providing natural distribution across compute resources. The model connects naturally to biological evolution, providing both algorithmic inspiration and computational tests of evolutionary hypotheses.

This formulation also faces distinctive challenges. Sample efficiency is generally lower than for gradient-based methods when gradients are available, since black-box optimization cannot exploit the local geometry of the fitness landscape. Selection pressure must be carefully balanced with variation to avoid premature convergence to local optima. The formulation of fitness landscapes can produce deceptive landscapes on which greedy improvement fails, and algorithmic frameworks including novelty search have been developed to address the deception problem.

The scope of evolutionary adaptation extends beyond direct optimization to encompass questions of open-endedness, novelty, and the conditions under which continual complexity growth emerges. These questions connect the algorithmic literature to biological evolution, to the philosophy of complexity, and to the design of open-ended computational environments.

## Historical Development

Evolutionary computation emerged concurrently in several research groups during the 1960s and 1970s. Evolutionary programming of [Fogel et al. 1966][research_fogel_owens_walsh_1966] introduced the treatment in the context of finite state machine evolution. Evolution strategies of [Rechenberg 1973][research_rechenberg_1973] and [Schwefel 1977][research_schwefel_1977] developed the framework independently for continuous parameter optimization in engineering design. The [Holland 1975][book_holland_1975] Adaptation in Natural and Artificial Systems introduced the genetic algorithm framework and the schema theorem that provided the initial theoretical foundation. Genetic programming of [Koza 1992][book_koza_1992] extended the account to the evolution of computer programs represented as syntax trees. The De Jong 1975 [research_dejong_1975] doctoral dissertation provided the first systematic empirical study of genetic algorithm performance across a suite of test functions.

The [Goldberg 1989][book_goldberg_1989] textbook consolidated the genetic algorithm literature and established the model as a broadly-applicable optimization method. The [Back Fogel Michalewicz 1997][book_back_fogel_michalewicz_1997] Handbook of Evolutionary Computation unified the previously-disparate genetic-algorithm, evolution-strategy, and evolutionary-programming traditions under a common formal framework. The [Beyer and Schwefel 2002][research_beyer_schwefel_2002] evolution strategies comprehensive introduction consolidated the modern evolution-strategy literature. The [Whitley 1994][research_whitley_1994] genetic algorithm tutorial provided the accompanying accessible introduction to the genetic-algorithm framework. Simulated Annealing of [Kirkpatrick et al. 1983][research_kirkpatrick_gelatt_vecchi_1983] provided the complementary single-solution population-of-one approach that shared the black-box optimization framing with population-based methods.

Neuroevolution emerged as a distinct sub-field through the 1990s and early 2000s. The [Stanley and Miikkulainen 2002][research_stanley_miikkulainen_2002_neat] NeuroEvolution of Augmenting Topologies (NEAT) framework introduced complexification-through-innovation-numbers as a mechanism for the co-evolution of neural network topology and weights, providing the foundational modern neuroevolutionary algorithm. HyperNEAT of [Stanley D'Ambrosio Gauci 2009][research_stanley_dambrosio_gauci_2009_hyperneat] extended this formulation with indirect encoding through Compositional Pattern-Producing Networks (CPPNs) that supports the evolution of considerably larger neural networks than direct-encoding methods can practically address.

The no-free-lunch theorems of [Wolpert and Macready 1997][research_wolpert_macready_1997_nfl] established that no optimization algorithm outperforms all others averaged across all possible objective functions, providing formal grounds for the diversity of algorithmic approaches and clarifying the role of problem-structural assumptions in algorithm design.

The 2010s produced the modern deep neuroevolution literature. Salimans Ho Chen Sidor Sutskever 2017 [research_salimans_et_al_2017_es] Evolution Strategies as a Scalable Alternative to Reinforcement Learning demonstrated that natural evolution strategies distributed across many workers achieve competitive performance with policy-gradient reinforcement learning on Atari and MuJoCo benchmarks, providing evidence that evolutionary methods scale to the deep learning regime.

Novelty search of [Lehman and Stanley 2011][research_lehman_stanley_2011_novelty] and Quality-Diversity of [Pugh et al. 2016][research_pugh_soros_stanley_2016_qd] introduced distinctive algorithmic frameworks that select for behavioral novelty and phenotypic diversity rather than direct fitness improvement. MAP-Elites of [Mouret and Clune 2015][research_mouret_clune_2015_mapelites] provided the algorithmic instantiation that has become the standard quality-diversity method.

Open-endedness reached prominence through POET of [Wang et al. 2019][research_wang_et_al_2019_poet_a261] which introduced the co-evolution of environments and agents that provides continually-expanding challenges. Enhanced POET of [Wang et al. 2020][research_wang_et_al_2020_epoet] extended the treatment with additional mechanisms for maintaining open-ended growth.

The 2020s produced further diversification including foundation-model-mediated evolutionary methods, quality-diversity at scale, and neural architecture search at deployment scale. The [Faldor Cully 2024][research_faldor_cully_2024_qd_survey] survey and the [Chalumeau et al. 2024][research_chalumeau_et_al_2024_qd_rl] treatment consolidated the modern quality-diversity and evolutionary reinforcement learning literatures.

## Genetic Algorithms and Evolution Strategies

Genetic algorithms and evolution strategies constitute the two foundational modern evolutionary frameworks. The frameworks differ in the encoding of solutions, in the selection and variation operators, and in the theoretical foundations.

Genetic algorithms of Holland 1975 encode solutions as binary strings and apply crossover and bit-flip mutation as variation operators. Selection is typically proportional to fitness through fitness-proportionate selection

$$p(x_i^{(t)}) = \frac{F(x_i^{(t)})}{\sum_{j=1}^{N} F(x_j^{(t)})}$$

or tournament selection in which random subsets of size $k$ compete for reproduction. The classical convergence analysis proceeds through the schema theorem which characterizes the expected number of instances of a schema $H$ in the next generation as

$$\mathbb{E}[m(H, t+1)] \geq m(H, t) \cdot \frac{f(H)}{\bar{f}} \cdot \left(1 - p_c \frac{\delta(H)}{L-1} - p_m \, o(H)\right)$$

where $f(H)$ is the average fitness of instances of $H$, $\bar{f}$ is the population average fitness, $L$ is the string length, $\delta(H)$ is the defining length of the schema, $o(H)$ is the schema order, and $p_c, p_m$ are the crossover and mutation rates. The schema theorem provides an explanation for the exponential accumulation of high-fitness low-order schemata under fitness-proportionate selection.

Evolution strategies of Rechenberg 1973 and Schwefel 1977 encode solutions as real-valued vectors and apply Gaussian mutation as the primary variation operator. The classical (1+1)-ES maintains a single parent $x_t$ and generates one offspring per generation through Gaussian perturbation

$$x_{t+1} = \begin{cases} x_t + \sigma \, \epsilon & \text{if } F(x_t + \sigma \epsilon) > F(x_t) \\ x_t & \text{otherwise} \end{cases}, \quad \epsilon \sim \mathcal{N}(0, I)$$

replacing the parent when the offspring has higher fitness. The step size $\sigma$ adapts through the Rechenberg 1/5-success rule

$$\sigma_{t+1} = \begin{cases} \sigma_t / c & \text{if } p_s > 1/5 \\ \sigma_t \cdot c & \text{if } p_s < 1/5 \\ \sigma_t & \text{otherwise} \end{cases}$$

with $p_s$ the recent success rate of proposed offspring and $c \in (0, 1)$ a fixed adjustment factor. The $(\mu, \lambda)$-ES generalizes to $\mu$ parents and $\lambda$ offspring with selection restricted to offspring, and the $(\mu + \lambda)$-ES selects from the union of parents and offspring.

The Covariance Matrix Adaptation Evolution Strategy (CMA-ES) of [Hansen and Ostermeier 2001][research_hansen_ostermeier_2001_cmaes] introduced the modern high-performance evolution strategy through the adaptation of a full covariance matrix that captures the local structure of the fitness landscape. The CMA-ES update generates offspring as

$$x_k = m + \sigma \, \mathcal{N}(0, C)$$

with mean $m$, step size $\sigma$, and covariance $C$. The rank-$\mu$ covariance update at each generation applies

$$C_{t+1} = (1 - c_\mu) C_t + c_\mu \sum_{i=1}^{\mu} w_i \, y_{i:\lambda} \, y_{i:\lambda}^\top$$

where $y_{i:\lambda} = (x_{i:\lambda} - m_t) / \sigma_t$ are normalized ranked-by-fitness search directions, $w_i$ are weights that emphasize higher-ranked offspring, and $c_\mu$ is a learning rate. The covariance update aligns the search distribution with successful search directions. The treatment has become the standard black-box optimization baseline and continues to organize the modern evolution strategy literature. The [Hansen 2016][research_hansen_2016_cmaes_tutorial] tutorial provides the canonical reference.

Natural Evolution Strategies of [Wierstra et al. 2014][research_wierstra_et_al_2014_nes] introduced the account as a stochastic gradient method on the parameter distribution rather than on individual solutions. The gradient of the expected fitness under a search distribution $\pi_\theta$ is

$$\nabla_\theta \, \mathbb{E}_{x \sim \pi_\theta}[F(x)] = \mathbb{E}_{x \sim \pi_\theta}[F(x) \, \nabla_\theta \log \pi_\theta(x)]$$

which admits Monte Carlo estimation through samples from $\pi_\theta$. Natural gradient corrections improve the update stability by scaling the gradient with the inverse Fisher information matrix of the search distribution,

$$\tilde{\nabla}_\theta \, \mathbb{E}[F] = F(\theta)^{-1} \nabla_\theta \, \mathbb{E}[F], \quad F(\theta) = \mathbb{E}_{x \sim \pi_\theta}\!\left[\nabla_\theta \log \pi_\theta(x) \, \nabla_\theta \log \pi_\theta(x)^\top\right]$$

where $F(\theta)$ is the Fisher information matrix of the parameter distribution.

The [Salimans et al. 2017][research_salimans_et_al_2017_es] Evolution Strategies as a Scalable Alternative to Reinforcement Learning framework demonstrated that a simplified version of NES scales to deep neural network policies through massive parallelization. The update rule perturbs the parameters with isotropic Gaussian noise and updates the parameters through the fitness-weighted sum,

$$\nabla_\theta \, \mathbb{E}_{\epsilon \sim \mathcal{N}(0, I)}[F(\theta + \sigma \epsilon)] \approx \frac{1}{N \sigma} \sum_{i=1}^{N} F(\theta + \sigma \epsilon_i) \, \epsilon_i$$

The framework achieved competitive performance with policy-gradient methods on standard benchmarks while providing significantly better parallelization efficiency, motivating considerable subsequent work on evolutionary approaches to deep reinforcement learning.

## Swarm Intelligence and Estimation of Distribution Algorithms

Population-based optimization extends beyond the classical evolutionary framework to include swarm intelligence methods and estimation of distribution algorithms. These frameworks share the population-of-candidates structure with evolutionary algorithms but replace crossover-and-mutation variation with alternative population-update rules.

Particle Swarm Optimization (PSO) of [Kennedy and Eberhart 1995][research_kennedy_eberhart_1995_pso] maintains a swarm of candidate solutions whose positions and velocities evolve through interactions with the personal-best and global-best positions. The velocity update

$$v_i^{t+1} = \omega \, v_i^t + \phi_p \, r_p \, (p_i^{\text{best}} - x_i^t) + \phi_g \, r_g \, (g^{\text{best}} - x_i^t)$$

combines inertia $\omega$, personal-best attraction with coefficient $\phi_p$, and global-best attraction with coefficient $\phi_g$, with $r_p, r_g$ uniform random weights and $p_i^{\text{best}}$, $g^{\text{best}}$ the personal and global best positions respectively. The account has been widely applied to engineering optimization problems and admits distinctive theoretical treatments through dynamical-systems analysis of the swarm trajectories.

Ant Colony Optimization (ACO) of [Dorigo et al. 1996][research_dorigo_maniezzo_colorni_1996] introduced a distinct population-based framework inspired by ant foraging behavior. The model maintains a pheromone distribution over solution components that guides subsequent candidate construction through stochastic sampling. The pheromone update rule reinforces components used by high-quality solutions and evaporates pheromone over time to prevent premature convergence. ACO has proved particularly effective for combinatorial optimization problems including the traveling salesman problem and network routing.

Differential Evolution (DE) of [Storn and Price 1997][research_storn_price_1997_de] introduced a mutation operator that generates offspring through difference-of-parents perturbations rather than Gaussian noise,

$$v_i = x_{r_1} + F \cdot (x_{r_2} - x_{r_3})$$

with $r_1, r_2, r_3$ distinct random indices and $F$ a scale factor. This formulation adapts to the local geometry of the fitness landscape through the population-derived difference vectors, providing self-scaling behavior that Gaussian mutation does not directly admit. DE has become the standard baseline for continuous black-box optimization alongside CMA-ES.

Estimation of Distribution Algorithms (EDAs) of [Mühlenbein 1997][research_muhlenbein_1997_eda] replace explicit variation operators with the fitting of a probabilistic model to selected high-fitness individuals and the sampling of the model to produce the next generation. The Bayesian Optimization Algorithm (BOA) of [Pelikan Goldberg Cantú-Paz 2000][research_pelikan_goldberg_cantupaz_2000_boa] used learned Bayesian networks as the probabilistic model, providing an approach that captures inter-variable dependencies in the fitness landscape. The [Larrañaga and Lozano 2002][book_larranaga_lozano_2002] Estimation of Distribution Algorithms consolidated the account and established the systematic taxonomy that continues to organize the field.

Swarm intelligence and EDA methods provide alternative frameworks that complement the classical evolutionary methods on problem classes with structural properties. Combinatorial problems often admit efficient ACO treatment. Continuous problems with strong inter-variable dependencies often benefit from EDA modeling. Continuous problems with mild inter-variable dependencies often admit efficient DE or CMA-ES treatment. Modern practice combines the frameworks through hybrid methods that leverage the strengths of each approach.

## Neuroevolution

Neuroevolution treats the evolutionary search of neural network parameters and architectures. This account combines the general evolutionary methodology with the structural properties of neural networks, providing distinctive algorithmic considerations that distinguish it from generic parameter optimization.

Neuroevolution has three principal encoding approaches. Direct encoding represents each network parameter and connection as a distinct gene, providing straightforward mutation and crossover but limited scalability due to the linear growth of the genome with network size. Indirect encoding represents networks through generative processes that produce full networks from compact descriptions, supporting the evolution of substantially larger networks through hierarchical or generative genotype-to-phenotype mappings. Developmental encoding represents networks through the evolution of a developmental process that unfolds into a network through iterative construction.

NEAT of Stanley and Miikkulainen 2002 introduced complexification through innovation numbers. The framework starts with minimal networks and adds nodes and connections through mutation across generations, tracking the historical origin of each innovation through unique innovation numbers that enable meaningful crossover between structurally-distinct networks. The innovation-number framework resolves the competing conventions problem that had blocked earlier crossover-based neuroevolution.

The NEAT speciation mechanism partitions the population into species based on genome similarity, protecting innovative variants from immediate competitive pressure while they mature. The compatibility distance between two genomes is

$$\delta = \frac{c_1 E + c_2 D}{N} + c_3 \bar{W}$$

where $E$ and $D$ are excess and disjoint gene counts, $\bar{W}$ is the average weight difference of matching genes, $N$ is a normalization factor, and $c_1, c_2, c_3$ are weight coefficients. Individuals with $\delta$ below a threshold belong to the same species. Species-adjusted fitness sharing distributes each individual's fitness across its species,

$$f_i' = \frac{f_i}{|\{j : \delta(x_i, x_j) < \delta_{\text{th}}\}|}$$

with $\delta_{\text{th}}$ the compatibility threshold. The mechanism produces balanced species populations by penalizing overrepresented species and protects novel structural innovations from immediate extinction.

HyperNEAT of Stanley D'Ambrosio Gauci 2009 introduced Compositional Pattern-Producing Networks (CPPNs) as an indirect encoding that generates network weights from a compact CPPN that maps coordinate inputs to connection weights. Given the source coordinates $(x_1, y_1)$ and target coordinates $(x_2, y_2)$ of a hypothetical connection in the substrate network, the CPPN produces the weight

$$w_{ij} = \text{CPPN}_\theta(x_1, y_1, x_2, y_2)$$

with the CPPN parameters $\theta$ subject to evolutionary search. The account supports the evolution of markedly larger networks than NEAT can practically address, exploiting geometric regularities in the network structure to compress the effective genome size.

ES-HyperNEAT of [Risi and Stanley 2012][research_risi_stanley_2012_eshyperneat] extended the framework with evolvable substrate configurations that permit the evolution to determine both the network structure and the coordinate placement, providing improved capacity for the discovery of task-network topologies.

Deep Neuroevolution of [Such et al. 2017][research_such_et_al_2017_deep_neuroevolution] documented that simple genetic algorithms applied to deep neural network policies achieve competitive performance with policy-gradient methods on Atari benchmarks, providing evidence that neuroevolution scales to the deep learning regime with proper parallelization.

Novelty search evolution strategies (NS-ES) of [Conti et al. 2018][research_conti_et_al_2018_nses] combined novelty search with evolution strategies, providing improved exploration in deceptive fitness landscapes than pure fitness-based selection admits.

Evolving Deep Neural Networks of [Miikkulainen et al. 2019][research_miikkulainen_et_al_2019] applied evolutionary methods to the joint optimization of architecture and hyperparameters for deep neural networks, achieving competitive performance with gradient-based training on multiple benchmarks. The [Yao 1999][research_yao_1999] evolving artificial neural networks survey consolidated the pre-deep-learning neuroevolution literature and established the taxonomy of encoding schemes and evolutionary operators that subsequent surveys have refined. The [Floreano et al. 2008][research_floreano_durr_mattiussi_2008] neuroevolution review provided the complementary treatment focused on evolutionary robotics applications.

Designing Neural Networks through Neuroevolution of [Stanley et al. 2019][research_stanley_et_al_2019_neuroevolution] provided the systematic modern review that consolidated the deep neuroevolution literature and identified the settings in which neuroevolutionary methods provide advantages over gradient-based training. AutoML-Zero of [Real et al. 2020][research_real_et_al_2020_automlzero] extended the account to the evolutionary discovery of complete machine learning algorithms including both architecture and training procedure, demonstrating that evolutionary search can rediscover key algorithmic innovations of deep learning from primitive operations.

## Developmental Encoding and Artificial Morphogenesis

Developmental encoding treats the evolutionary search of generative processes that produce artifacts through iterative construction rather than direct specification. The treatment connects evolutionary computation to developmental biology through the shared observation that biological form emerges through developmental unfolding from compact genetic information.

The [Stanley 2007][research_stanley_2007_cppn] Compositional Pattern-Producing Networks framework introduced the indirect encoding through function composition that has become the standard modern developmental encoding for neuroevolution. This account produces phenotypes through the recursive composition of primitive functions including sinusoids, Gaussians, and linear combinations, providing an approach that generates complex regular patterns from compact genotypes.

Hornby and Pollack 2001 [research_hornby_pollack_2001] introduced generative representation for the evolution of virtual creatures through L-system-based body encodings. The framework produced appreciably more complex morphologies than direct encoding admits, providing evidence for the advantages of generative encodings on morphological evolution tasks.

The [Miller 2004][research_miller_2004_embryology] evolvable model of embryology introduced a developmental model in which cellular processes including division, differentiation, and death are governed by evolved gene-regulatory networks. The account provides a computational instantiation of morphogen-based development that supports the study of the structural properties that produce evolvable morphological systems.

Compositional Pattern-Producing Networks were applied to soft robot design by [Cheney et al. 2013][research_cheney_et_al_2013_a261] Unshackling Evolution to produce soft-robot morphologies with continuous material distributions, providing evidence that developmental encoding scales to physical robotic design.

Soft Robots That Grow of [Kriegman et al. 2020][research_kriegman_et_al_2020] introduced xenobots, biological soft robots assembled from frog cells whose morphology is designed through evolutionary search. The model provides evidence that developmental encoding can bridge computational and biological substrates, producing physical designs that self-assemble according to evolved developmental rules.

Bentley and Kumar 1999 [research_bentley_kumar_1999] introduced the systematic comparison of direct, developmental, and implicit encoding schemes for morphological evolution, providing empirical evidence that developmental encoding produces qualitatively-different design distributions than direct encoding.

Developmental encoding provides distinctive properties for evolutionary search. Compact genotypes admit efficient search of very large phenotype spaces. Generative encodings often exhibit inductive biases that support the discovery of regular patterns. Development-based encodings connect naturally to biological accounts of evolvability through modularity, weak linkage, and canalization. This formulation continues to organize significant research on the developmental mechanisms that support evolvable systems.

## Novelty Search and Quality-Diversity

Novelty search and quality-diversity methods depart from the direct fitness-optimization framing of classical evolutionary algorithms. The frameworks explicitly seek behavioral diversity or the coverage of a behavioral space, rather than the convergence to a single high-fitness solution.

Novelty Search of Lehman and Stanley 2011 introduced this formulation through a selection criterion based on behavioral novelty rather than fitness. The behavioral novelty of a candidate is measured as the distance to its $k$-nearest neighbors in a behavioral archive,

$$\rho(x) = \frac{1}{k} \sum_{i=1}^{k} \|b(x) - b(x_i^{\text{NN}})\|$$

where $b(x)$ is the behavioral descriptor of candidate $x$ and $x_i^{\text{NN}}$ are its $k$ nearest neighbors in the archive. Selection favors candidates with high novelty regardless of their fitness, producing populations that systematically explore the behavioral space. Combined novelty-plus-fitness selection weights the two objectives through

$$s(x) = (1 - w) \, \rho(x) + w \, F(x)$$

with $w \in [0, 1]$ trading off exploration against exploitation, and archive updates typically retain the candidate when $\rho(x) > \rho_{\text{th}}$ for a threshold $\rho_{\text{th}}$.

This account provides a response to the deception problem in evolutionary optimization. On deceptive fitness landscapes where the local fitness gradient leads away from the global optimum, direct fitness-based selection converges to local optima. Novelty search bypasses the gradient information entirely and instead maintains coverage of the behavioral space, often discovering the global optimum as a side effect of the systematic exploration.

Quality-Diversity of Pugh Soros Stanley 2016 combined the novelty framework with quality selection to produce populations that are both diverse and high-performing. The framework maintains a set of candidates that populate a behavioral map, with each cell of the map containing the highest-fitness candidate discovered with the corresponding behavioral characteristics.

MAP-Elites of Mouret and Clune 2015 provided the algorithmic instantiation. The account discretizes the behavioral space into a grid, and maintains a single elite per cell,

$$\mathcal{E}(b) = \arg\max_{x : b(x) = b} F(x)$$

with $\mathcal{E}$ producing the current best individual with behavioral descriptor $b$. Selection samples from the elite archive with variation applied to produce new candidates that may either fill empty cells or replace the elite of an existing cell. The model provides simultaneously a high-quality solution repertoire and a systematic exploration of the behavioral space. The QD score aggregates this formulation's dual objective through

$$\text{QD}(\mathcal{E}) = \sum_{b \in \mathcal{B}_{\text{filled}}} F(\mathcal{E}(b))$$

capturing both coverage of the behavioral space and quality of the retained solutions.

Robots that Adapt through Injury of [Cully et al. 2015][research_cully_et_al_2015_robots] demonstrated that a MAP-Elites-generated repertoire of behaviors supports rapid post-injury adaptation in physical robots. After the robot suffers damage that prevents standard walking gaits, the pre-computed behavioral map provides a diverse set of alternatives that can be searched for a functional gait through Bayesian optimization, achieving greatly faster recovery than reinforcement learning from scratch.

Covariance Matrix Adaptation MAP-Elites (CMA-ME) of [Fontaine Nikolaidis 2021a][research_fontaine_nikolaidis_2021_cmame] combined MAP-Elites with CMA-ES-style covariance adaptation, providing considerably improved sample efficiency over the vanilla MAP-Elites variation operator.

Differentiable Quality-Diversity (DQD) of [Fontaine Nikolaidis 2021b][research_fontaine_nikolaidis_2021_dqd] introduced the framework for settings where fitness and behavioral descriptor gradients are available, providing significantly improved sample efficiency by exploiting differentiable structure while retaining the diverse-solution guarantees of MAP-Elites.

QD-RL of Chalumeau Cully Grillotti Bonnet Miret Flajolet 2024 [research_chalumeau_et_al_2024_qd_rl] combined quality-diversity with reinforcement learning through the mechanism of policy-gradient variation operators, providing an approach that combines the sample efficiency of reinforcement learning with the diversity guarantees of MAP-Elites.

The [Cully and Demiris 2018][research_cully_demiris_2018_qd_review] Quality and Diversity Optimization framework consolidated the algorithmic and application literature, providing the systematic taxonomy that continues to organize the field. The complementary [Chatzilygeroudis et al. 2021][research_chatzilygeroudis_et_al_2021_qd_overview] Quality-Diversity Optimization survey provided the algorithmic taxonomy focused on the structural properties of behavioral space representation. CVT-MAP-Elites of [Vassiliades et al. 2018][research_vassiliades_et_al_2018_cvt] extended MAP-Elites to high-dimensional behavioral spaces through Centroidal Voronoi Tessellation, providing an approach that scales to substantially higher-dimensional behavioral descriptors than uniform-grid MAP-Elites can practically address.

Abandoning Objectives of [Lehman and Stanley 2011][research_lehman_stanley_2011_abandoning] provided the earlier extension of the novelty-search framework to a philosophical argument for the systematic advantages of behavioral diversity over direct objective optimization. Fontaine et al 2020 [research_fontaine_et_al_2020_cma_me_orig] provided the original CMA-ME framework at introduction alongside the systematic empirical evaluation across diverse benchmarks. Grillotti and Cully 2022 [research_grillotti_cully_2022] introduced Modular QD frameworks that decouple archive management, variation operator, and selection procedure, supporting systematic empirical comparison across the design choices.

## Multi-Objective Evolutionary Algorithms

Multi-objective evolutionary algorithms treat the setting in which several objectives must be simultaneously optimized without a-priori aggregation into a single scalar fitness. The treatment produces a Pareto front of non-dominated solutions that trade off among the objectives, providing decision-makers with the full range of achievable trade-offs.

The general multi-objective problem seeks the Pareto set

$$\mathcal{P}^* = \{x \in \mathcal{X} \, : \, \nexists y \in \mathcal{X} \text{ such that } y \succ_{\text{Pareto}} x\}$$

with $\succ_{\text{Pareto}}$ the Pareto-dominance relation. The image of $\mathcal{P}^\*$ in objective space forms the Pareto front, and multi-objective evolutionary algorithms approximate this front through population-based search.

NSGA-II of [Deb Pratap Agarwal Meyarivan 2002][research_deb_et_al_2002_nsga2] introduced the modern non-dominated sorting genetic algorithm through fast non-dominated sorting combined with crowding-distance-based diversity preservation. This account partitions the population into non-domination levels

$$\mathcal{F}_1 = \{x \in \mathcal{P} \, : \, \nexists y \in \mathcal{P}, y \succ_{\text{Pareto}} x\}, \quad \mathcal{F}_k = \{x \in \mathcal{P} \setminus \cup_{j<k} \mathcal{F}_j : \, \nexists y \in \mathcal{P} \setminus \cup_{j<k} \mathcal{F}_j, y \succ_{\text{Pareto}} x\}$$

with selection favoring lower-index fronts and, within a front, favoring individuals with higher crowding distance. NSGA-II has become the standard baseline for multi-objective evolutionary optimization and continues to organize the modern literature.

NSGA-III of [Deb and Jain 2013][research_deb_jain_2013_nsga3] extended the account to many-objective problems with more than three objectives through reference-point-based selection, addressing the pathology of NSGA-II's crowding-distance metric on high-dimensional Pareto fronts.

MOEA/D of [Zhang and Li 2007][research_zhang_li_2007_moead] introduced a decomposition-based framework in which the multi-objective problem is decomposed into a set of scalar sub-problems that are simultaneously optimized through a shared population. The account provides markedly better scalability to many-objective settings than dominance-based methods and admits distinctive theoretical treatments through the weight-vector decomposition.

SPEA2 of [Zitzler Laumanns Thiele 2001][research_zitzler_laumanns_thiele_2001_spea2] introduced strength Pareto evolutionary algorithm version 2 through fine-grained fitness assignment based on both dominated-by and dominating counts, providing an alternative to NSGA-II's front-based ranking with distinctive empirical properties on problem classes.

Multi-objective evolution strategies of [Igel Hansen Roth 2007][research_igel_hansen_roth_2007_moes] extended CMA-ES to the multi-objective setting through the mechanism of covariance-matrix adaptation applied to each Pareto-front-approximating sub-population.

Multi-objective evolutionary algorithms have proved particularly valuable in engineering design where trade-offs among cost, performance, and reliability must be systematically explored. Modern applications include neural architecture search with joint accuracy-and-latency objectives, hyperparameter optimization with joint performance-and-compute objectives, and antenna design with joint gain-and-directivity objectives. The model connects evolutionary computation to the broader multi-criteria decision-making literature and to the Pareto-based analysis of trade-offs in engineering practice.

## Open-Endedness

Open-endedness treats systems that continually invent new challenges and produce new solutions without external specification of objectives. This formulation connects evolutionary computation to the broader philosophy of complexity and to biological accounts of the conditions under which sustained complexity growth emerges.

The [Bedau 1998][research_bedau_1998_four_questions] four questions for open-endedness identified the philosophical criteria that a computational system must satisfy to exhibit genuinely open-ended behavior. The treatment distinguished bounded from unbounded evolutionary systems and provided testable predictions about the structural conditions that support open-endedness. The [Standish 2003][research_standish_2003_open_ended] treatment provided a complementary characterization through the information-theoretic requirement of the continual generation of surprising outcomes. The [Taylor 2016][research_taylor_et_al_2016_oee] open-ended evolution research roadmap consolidated the philosophical, biological, and computational treatments of open-endedness and identified the technical challenges that continue to organize the field.

The Minimal Criterion Coevolution of [Soros and Stanley 2014][research_soros_stanley_2014_mcc] introduced a minimal-criterion framework for open-endedness in which reproduction requires meeting a threshold criterion rather than optimizing a fitness function, providing an approach that supports continual diversification without direct fitness selection.

POET of Wang Lehman Clune Stanley 2019 introduced the paired open-ended trailblazer framework in which environments and agents coevolve. New environments are proposed by mutating existing environments, and environments that are neither too easy nor too hard for the current agent population are preserved. This account produces continually-expanding sets of environments and agents that co-adapt over evolutionary time.

Enhanced POET of Wang Lehman Clune Stanley 2020 extended the model with additional mechanisms including behavior characterization for environments and improved transfer between agent-environment pairs. The extended framework produced appreciably more diverse environments than the original POET and demonstrated sustained open-ended growth over longer timescales.

Unsupervised Environment Design of [Dennis et al. 2020][research_dennis_et_al_2020_paired_a261] PAIRED introduced a game-theoretic formulation for open-ended environment generation. An adversarial environment generator proposes environments that maximize the regret of the current agent $\pi_A$ against an antagonist policy $\pi_B$,

$$\theta^*_{\text{env}} = \arg\max_{\theta_{\text{env}}} \left(J_{\theta_{\text{env}}}(\pi_B) - J_{\theta_{\text{env}}}(\pi_A)\right)$$

providing an automatic curriculum of environments that are challenging but solvable at the agent's current capability level. The regret objective ensures that generated environments are neither too easy where both agents succeed nor too hard where both agents fail.

Open-Ended Learning of [Open-Ended et al. 2021][research_openendedlearningteam_2021] combined POET-style environment generation with foundation-model-scale training in the XLand environment, achieving substantial capability transfer across a vast distribution of procedurally-generated tasks. The account provides evidence that open-endedness scales to the foundation-model regime.

Automatic Curriculum Learning of [Portelas et al. 2020][research_portelas_et_al_2020_acl_a261] consolidated the automatic curriculum literature and identified the mechanisms that connect open-endedness to reinforcement learning practice. The model treated in article nine's meta-learning discussion provides the algorithmic bridge between open-ended environment generation and reinforcement learning training.

Recent work extends the open-endedness framework to language-model-mediated environments. OMNI-EPIC of [Faldor et al. 2024][research_faldor_et_al_2024_omni_epic] introduced language-model-based environment proposal that continually generates novel task descriptions consistent with the current agent's capability, providing a bridge between the classical evolutionary open-endedness framework and the language-model-based task generation of the modern foundation-model literature. AI-Generating Algorithms (AI-GAs) of [Clune 2019][research_clune_2019_aigas] identified the research agenda of designing algorithms that generate AI systems automatically through open-ended self-improvement, providing a philosophical framing for much of the subsequent language-model-mediated evolutionary work.

Sustained open-endedness has proved greatly more difficult to achieve than initial open-ended-like behavior. Most systems that appear open-ended in early generations converge to bounded solution distributions over longer timescales, and the conditions under which genuinely unbounded evolution occurs remain an active research area.

## Artificial Life and Digital Evolution

Artificial life treats the computational study of evolutionary and adaptive processes in synthetic substrates. This formulation provides both a philosophical approach to life-as-it-could-be and a set of computational systems that support empirical study of evolutionary phenomena at compute-tractable timescales.

The [Von Neumann 1966][book_von_neumann_1966] Theory of Self-Reproducing Automata provided the foundational treatment of self-replication and universal construction, establishing the theoretical framework that subsequent artificial life systems have implemented. The [Langton 1986][research_langton_1986_alife] Studying Artificial Life with Cellular Automata framework consolidated the approach through cellular automata and established artificial life as a distinct research discipline.

Tierra of [Ray 1991][research_ray_1991_tierra] provided the foundational modern digital evolution system through a virtual assembly-language environment in which self-replicating programs compete for CPU time and memory. The treatment demonstrated the emergence of parasites, hyperparasites, and immune responses through pure evolutionary dynamics without designer intervention, providing evidence for the structural conditions under which complex ecological interactions emerge.

Avida of [Ofria and Wilke 2004][research_ofria_wilke_2004_avida] extended the Tierra framework with a more controllable experimental substrate that has enabled marked subsequent research on evolutionary dynamics. The Lenski Ofria Pennock Adami 2003 [research_lenski_et_al_2003] evolutionary origin of complex features study documented the pathway by which a complex logic operation emerges through the sequential accumulation of simpler operations in Avida, providing quantitative evidence for the incremental-evolution hypothesis of complexity origins.

The [Adami 1998][book_adami_1998] Introduction to Artificial Life consolidated the field and provided the systematic treatment of the computational and biological connections. Subsequent work has extended the model to evolutionary questions including the evolution of altruism, the origin of multicellularity, and the structural properties that support open-ended complexity growth.

Evolvable Hardware of [Thompson 1997][research_thompson_1997_evolvable_hardware] extended the digital evolution framework to physical FPGA substrates through the direct evolution of circuit configurations. The framework demonstrated that evolutionary search discovers circuits that exploit physical properties of the substrate that human designers had not anticipated, providing evidence for the advantages of evolution when applied to physical systems.

Major Transitions in Individuality of [Maynard et al. 1995][book_maynard_smith_szathmary_1995] provided the biological framework for the transitions in evolutionary complexity including the origin of cells, multicellularity, and eusocial societies. Computational instantiations of the treatment have been developed to study the structural conditions under which higher-level individuality emerges from lower-level components. Waser and Adami 2018 [research_waser_adami_2018] provided the information-theoretic treatment of major evolutionary transitions in artificial life systems.

The Sayama 2009 [research_sayama_2009] open-ended evolution in artificial life systems framework provided a systematic taxonomy of the structural properties that support sustained evolution in synthetic substrates, connecting the artificial life literature to the modern open-endedness treatments.

Artificial life and digital evolution provide the experimental framework through which evolutionary hypotheses can be tested at compute-tractable timescales. The model connects evolutionary computation to the empirical questions of comparative biology and to the philosophical questions of the general conditions under which life-like processes emerge from computational substrates.

## Coevolution

Coevolution treats the setting in which multiple populations coevolve with fitness functions defined by the interactions among the populations. This formulation provides both a natural biological correspondence and a computational mechanism for generating challenges automatically.

Competitive coevolution treats populations with fitness functions defined by pairwise contests. Given populations $\mathcal{P}^A$ and $\mathcal{P}^B$, the fitness of $x \in \mathcal{P}^A$ against the opposing population is

$$F^A(x) = \mathbb{E}_{y \sim \mathcal{P}^B}[U(x, y)]$$

with $U$ the payoff of $x$ against $y$. The treatment has been applied to the evolution of game-playing strategies, adversarial defense mechanisms, and predator-prey dynamics. The Rosin and Belew 1997 [research_rosin_belew_1997] Hall of Fame framework preserved historical strategies to prevent the loss of adaptations against previously-defeated opponents, providing a mechanism to address the coevolutionary instability problem.

Cooperative coevolution treats populations with shared fitness functions that decompose across the populations. The [Potter and De Jong 2000][research_potter_dejong_2000] cooperative coevolutionary framework introduced the decomposition of complex problems into sub-populations that coevolve toward joint solutions,

$$F(x^1, x^2, \ldots, x^K) = F_{\text{joint}}(x^1 \oplus x^2 \oplus \cdots \oplus x^K)$$

with each sub-population evolving one component $x^k$ and the joint solution assembled through concatenation or composition. This account supports the evolution of considerably larger solutions than monolithic populations can practically address.

Pareto coevolution of [Ficici and Pollack 2001][research_ficici_pollack_2001_pareto] introduced multi-objective coevolutionary dynamics through Pareto optimality across the interacting populations, providing formal grounds for the discovery of qualitatively-distinct trade-off solutions. Solution $x$ Pareto-dominates $y$ under objectives $F_1, \ldots, F_M$ if

$$\forall m : \, F_m(x) \geq F_m(y) \quad \text{and} \quad \exists m : \, F_m(x) > F_m(y)$$

with the Pareto front comprising all non-dominated solutions. The framework provides the multi-objective extension of the scalar-fitness evolutionary framework.

Modern deep coevolution has proved particularly effective for adversarial settings including robust reinforcement learning and adversarial defense. Adversarial coevolution frameworks including PSRO of Lanctot Zambaldi Gruslys et al 2017 and the AlphaStar league of Vinyals et al 2019 (both treated in article eleven) combine coevolutionary population dynamics with modern deep reinforcement learning to produce robust policies against adversarial opponents.

The dynamics of coevolutionary systems including cycling among strategies, mutual escalation, and disengagement have been extensively studied. The [Popovici et al. 2012][research_popovici_et_al_2012_coevolution] handbook treatment consolidated the theoretical and empirical literature on coevolutionary dynamics. Cliff and Miller 1996 [research_cliff_miller_1996] provided the foundational study of coevolutionary dynamics in simulated predator-prey systems and identified the arms-race patterns that continue to organize the field. Watson and Pollack 2001 [research_watson_pollack_2001] introduced symbiotic coevolution frameworks in which cooperation among sub-populations produces solutions beyond what independent sub-populations could achieve. Coevolutionary robotics of [Bongard 2004][research_bongard_2004_coevolutionary] demonstrated that morphology-controller coevolution produces qualitatively-different robotic designs than fixed-morphology controller optimization.

## Neural Architecture Search

Neural architecture search (NAS) treats the automatic discovery of neural network architectures. The account combines evolutionary and gradient-based search over architectural design spaces, and has produced state-of-the-art architectures for image classification, object detection, and language modeling.

Reinforcement-learning-based NAS of [Zoph and Le 2017][research_zoph_le_2017_nas] introduced the model through a recurrent controller that samples architectures and receives their downstream accuracy as reward. The model achieved state-of-the-art performance on CIFAR-10 image classification at extensive compute cost.

Large-Scale Evolution of Image Classifiers of [Real et al. 2017][research_real_et_al_2017_large_scale] introduced evolutionary NAS through mutation of existing architectures, providing an approach with significantly lower compute cost than reinforcement-learning-based NAS. AmoebaNet of [Real et al. 2019][research_real_et_al_2019_amoebanet] extended this formulation with regularized evolution that maintains a fixed-size population and applies age-based selection, achieving state-of-the-art performance on ImageNet classification.

Differentiable Architecture Search (DARTS) of [Liu et al. 2019][research_liu_simonyan_yang_2019_darts] introduced a gradient-based approach to NAS through a continuous relaxation of the discrete architecture space. Each candidate operation $o \in \mathcal{O}$ at each connection receives a mixing weight $\alpha_o$ and the output at each node combines all candidate operations as

$$\bar{o}(x) = \sum_{o \in \mathcal{O}} \frac{\exp(\alpha_o)}{\sum_{o' \in \mathcal{O}} \exp(\alpha_{o'})} \, o(x)$$

with the architecture parameters $\alpha$ and network weights $w$ jointly optimized through bilevel optimization

$$\min_\alpha L_{\text{val}}(w^*(\alpha), \alpha), \quad w^*(\alpha) = \arg\min_w L_{\text{train}}(w, \alpha)$$

This account substantially reduces the search compute cost through gradient-based bilevel optimization but requires the differentiable structure that pure evolutionary methods do not.

Weight-sharing NAS through Efficient Neural Architecture Search (ENAS) of [Pham et al. 2018][research_pham_et_al_2018_enas] introduced parameter sharing across candidate architectures, providing a sizable compute-cost reduction that enabled NAS at practical scale. Stochastic Neural Architecture Search (SNAS) of [Xie et al. 2019][research_xie_et_al_2019_snas] introduced a differentiable framework with reduced bias compared to DARTS through the reparameterization of the discrete architecture selection. ProxylessNAS of [Cai et al. 2019][research_cai_zhu_han_2019_proxyless] eliminated the proxy-task requirement of prior differentiable NAS methods by directly searching on the target task with binarized architecture gates. FBNet of [Wu et al. 2019][research_wu_et_al_2019_fbnet] applied differentiable NAS to hardware-aware architecture search with explicit latency constraints, providing an approach that scales to mobile-deployment optimization.

The [Elsken et al. 2019][research_elsken_metzen_hutter_2019_nas_survey] neural architecture search survey consolidated the algorithmic and empirical literature and identified the trade-offs among evolutionary, reinforcement-learning-based, and gradient-based NAS approaches.

EfficientNet of [Tan and Le 2019][research_tan_le_2019_efficientnet] introduced compound scaling of architecture width, depth, and resolution through a systematic search. The compound-scaling rule assigns

$$d = \alpha^\phi, \quad w = \beta^\phi, \quad r = \gamma^\phi, \quad \text{subject to} \quad \alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$$

where $d, w, r$ are depth, width, and resolution scaling factors, $\phi$ is a global scaling coefficient, and $\alpha, \beta, \gamma$ are per-dimension constants determined through the small-grid search. The framework produces architectures that dominate the Pareto frontier of accuracy versus compute and has markedly shaped subsequent architectural design practice.

## Symbolic Regression and Program Synthesis

Symbolic regression and program synthesis apply evolutionary search to the discovery of mathematical expressions and programs from empirical data or specification. The account connects evolutionary computation to the broader automated-scientific-discovery and program-synthesis literatures.

Symbolic regression through genetic programming of Koza 1992 provided the foundational approach. The model represents candidate expressions as syntax trees over primitive functions and evolves the trees through subtree crossover and point mutation. The fitness function scores expressions against target data through goodness-of-fit metrics that trade off accuracy against expression complexity through the parsimony pressure.

Distilling Free-Form Natural Laws of [Schmidt and Lipson 2009][research_schmidt_lipson_2009_a261] applied symbolic regression to the discovery of conservation laws from empirical measurements, providing evidence that evolutionary search discovers physically-meaningful mathematical expressions when appropriate structural constraints are imposed. This formulation has been applied to a broad range of physical, biological, and engineering systems with appreciable practical impact.

Deep Symbolic Regression (DSR) of [Petersen 2021][research_petersen_et_al_2021_dsr] combined recurrent neural network policies with reinforcement learning to sample symbolic expressions, providing a modern approach that leverages gradient-based training alongside evolutionary structural search. The treatment generalizes across problem classes through the learned prior over expression structure.

The [La Cava et al. 2021][research_lacava_et_al_2021] SRBench framework provided the systematic benchmark for symbolic regression methods, enabling reproducible comparison across the appreciably-diverse algorithmic approaches. The benchmark documented that no single method dominates across all problem classes, motivating the problem-structure-matching approach to method selection.

End-to-End Symbolic Regression with Transformers of [Kamienny et al. 2022][research_kamienny_et_al_2022] introduced a transformer-based approach that predicts symbolic expressions directly from numerical data through supervised pretraining on synthetic examples. This account provides greatly faster inference than evolutionary search while retaining competitive discovery quality on standard benchmarks.

Symbolic Regression via Graph Neural Networks of [Cranmer et al. 2020][research_cranmer_et_al_2020] combined symbolic regression with graph neural network priors to discover interpretable expressions from complex-system simulation data. The framework provides evidence that evolutionary symbolic regression complements the modern deep-learning-based scientific discovery literature.

Program synthesis through genetic programming has been applied to problem classes including string manipulation, list processing, and program-repair tasks. The connection to modern language-model-mediated code generation through the evolutionary methods of section eleven provides an emerging framework that combines evolutionary structural search with the semantic capabilities of foundation models.

## Evolutionary Reinforcement Learning

Evolutionary reinforcement learning combines evolutionary population dynamics with reinforcement-learning-style value estimation and policy improvement. The account leverages the exploration capacity of evolutionary methods while retaining the sample-efficiency benefits of gradient-based reinforcement learning.

Evolutionary Reinforcement Learning (ERL) of [Khadka and Tumer 2018][research_khadka_tumer_2018_erl] introduced a hybrid framework in which an evolutionary population coexists with a reinforcement learning agent that samples from the population's replay buffer. The shared replay buffer accumulates transitions from all population members,

$$\mathcal{B} = \bigcup_{\pi \in \mathcal{P}_t} \{(s, a, r, s') \, : \, (s, a, r, s') \sim \pi\}$$

and the reinforcement learning agent optimizes a policy through standard off-policy gradient updates on $\mathcal{B}$. The evolutionary population provides exploration diversity while the reinforcement learning agent provides gradient-based refinement, and this formulation periodically injects the refined policy back into the evolutionary population as an elite candidate.

CEM-RL of [Pourchot and Sigaud 2019][research_pourchot_sigaud_2019_cemrl] combined the Cross-Entropy Method with off-policy deep reinforcement learning, providing an approach that inherits the exploration benefits of CEM while retaining sample-efficient off-policy gradients. The CEM update samples a population from a Gaussian distribution over parameters and updates the distribution by fitting to the top $k$ performers,

$$\mu_{t+1} = \frac{1}{k} \sum_{i \in \text{top-}k} \theta_i, \quad \Sigma_{t+1} = \frac{1}{k} \sum_{i \in \text{top-}k} (\theta_i - \mu_{t+1})(\theta_i - \mu_{t+1})^\top$$

providing an evolutionary-strategies-like update alongside the standard off-policy gradient improvement on the population's shared replay buffer.

Genetic Soft Actor-Critic of [Kelly Bowling 2020][research_kelly_bowling_2020_gsac] extended the ERL framework with soft-actor-critic-based improvement, providing state-of-the-art performance on continuous control benchmarks. This formulation combines the entropy-based exploration of SAC with the population-based exploration of evolutionary search.

GEP-PG of [Colas et al. 2018][research_colas_sigaud_oudeyer_2018_geppg] combined goal-exploration processes with policy gradients, using evolutionary population-based novelty-guided exploration to initialize policy-gradient training. The treatment achieves considerable improvements over pure policy-gradient methods on sparse-reward continuous control tasks. NEAT-RL of [Igel 2003][research_igel_2003] provided the earlier framework combining NEAT-style neuroevolution with reinforcement learning, establishing the settings in which neuroevolutionary methods complement gradient-based methods.

The [Sigaud 2023][research_sigaud_2023_erl_survey] evolutionary reinforcement learning survey consolidated the algorithmic and empirical literature and identified the settings in which evolutionary reinforcement learning provides advantages over pure gradient-based or pure evolutionary methods.

Modern practice increasingly combines the frameworks in the pattern where evolutionary methods provide the exploration and diversity, gradient methods provide the sample-efficient local improvement, and the combined framework achieves both broad coverage and efficient convergence.

## Foundation Models and Language-Model-Mediated Evolution

The rise of large-scale foundation models has produced new frameworks for evolutionary adaptation in which the language model serves as both the variation operator and the fitness evaluator. This account combines the systematic search capabilities of evolutionary methods with the semantic capabilities of foundation models.

Evolution through Large Models of [Lehman et al. 2022][research_lehman_et_al_2023_elm] introduced ELM, the systematic use of language models as variation operators for evolutionary search over code, natural language, and other symbolic domains. Formally, the language-model variation operator applies

$$x' \sim p_{\text{LM}}(\cdot \mid \text{prompt}(x_1, x_2, \ldots))$$

where the prompt encodes selected parents and instructions for semantic mutation or recombination. The framework demonstrated considerably better performance than random mutation for tasks in which the fitness landscape rewards semantic properties.

PromptBreeder of [Fernando et al. 2023][research_fernando_et_al_2023_promptbreeder] introduced the application of language-model-based evolution to the prompt-engineering domain, producing self-improving prompts that outperform hand-designed prompts across diverse tasks. The account mutates prompts through language-model paraphrasing and selects prompts based on downstream task performance.

LMX of [Meyerson et al. 2023][research_meyerson_et_al_2023_lmx] extended the treatment to the language-model-based crossover of natural language descriptions, providing an evolutionary mechanism for the discovery of task specifications and problem statements.

OpenELM of [Bradley et al. 2024][research_bradley_et_al_2024_openelm] provided an open-source framework for language-model-based evolution across diverse task types, and OMNI-EPIC of Faldor Zhang Cully Clune 2024 combined language-model-based environment generation with open-ended agent training, providing evidence that foundation-model-scale evolution retains the open-endedness properties of the classical evolutionary literature.

EvoPrompt of [Guo et al. 2023][research_chen_et_al_2024_evoprompt] introduced systematic evolutionary search over prompts with genetic-algorithm-style crossover and mutation, providing an alternative to gradient-based prompt tuning that operates directly in the natural-language prompt space. Eureka of [Ma et al. 2023][research_ma_et_al_2023_eureka] applied language-model-mediated evolution to the reward-function design problem for reinforcement learning, producing reward functions that outperform hand-designed alternatives on many benchmark tasks through evolutionary search over language-model-generated candidates.

FunSearch of [Romera-Paredes et al. 2023][research_romera_paredes_et_al_2024_funsearch] combined language-model-mediated evolution with formal fitness evaluation to discover novel mathematical constructions including improved cap-set constructions and new bin-packing heuristics, providing evidence that language-model-mediated evolutionary search produces genuinely novel mathematical results rather than paraphrases of prior work.

Language-model-mediated evolution provides a distinctive framework that combines the systematic search capabilities of evolutionary methods with the semantic capabilities of foundation models. This formulation connects evolutionary computation to the broader trend toward foundation-model-mediated optimization and to the application of foundation models as universal function approximators for structured search problems.

## Cultural Evolution and Memetic Systems

Cultural evolution treats the transmission of behavioral patterns across individuals through observational learning, teaching, and communication. The treatment provides both a biological account of human cognitive evolution and a computational framework for multi-agent systems that adapt through inter-agent transmission rather than pure genetic inheritance.

The [Boyd and Richerson 1985][book_boyd_richerson_1985] Culture and the Evolutionary Process framework established the dual-inheritance theory of human cognitive evolution, in which genetic and cultural transmission systems coevolve to produce specifically-human cognitive capabilities. This account has significantly shaped subsequent evolutionary anthropology and provides testable predictions about the conditions under which cumulative cultural evolution emerges.

Memetics of [Dawkins 1976][book_dawkins_1976] provided the alternative framework in which cultural units are treated as evolutionary replicators analogous to genes, providing a computational metaphor that has substantially influenced artificial life and computational cultural evolution. Cavalli-Sforza and Feldman 1981 [book_cavalli_sforza_feldman_1981] provided the formal mathematical framework for cultural transmission in structured populations, extending population genetics to the cultural inheritance channel. Henrich 2016 [book_henrich_2016] consolidated the modern cumulative-cultural-evolution literature and identified the cognitive adaptations that support the human capacity for cumulative culture.

Computational cultural evolution studies including [Kirby et al. 2015][research_kirby_cornish_smith_2015_a261] iterated learning documented that transmission through learning agents produces patterns of linguistic and behavioral simplification that mirror observed patterns in natural language evolution, providing experimental evidence for the computational mechanisms of cultural evolution.

Multi-agent artificial systems including the Nowak Tarnita Antal 2010 [research_nowak_tarnita_antal_2010] evolutionary dynamics framework provided formal treatments of cultural transmission in structured populations, connecting evolutionary computation to the broader mathematical biology of population dynamics. The replicator dynamics equation

$$\dot{x}_i = x_i \left(f_i(x) - \bar{f}(x)\right), \quad \bar{f}(x) = \sum_j x_j f_j(x)$$

with $x_i$ the frequency of strategy $i$ and $f_i(x)$ the fitness of strategy $i$ in the population state $x$, provides the foundational mathematical framework for the analysis of selection under frequency-dependent fitness. The framework unifies genetic and cultural transmission through the shared underlying selection mechanism.

Modern cultural-evolution-inspired methods in machine learning include population-based training of Jaderberg et al 2017 treated in article eleven, which exploits inter-agent transmission of hyperparameters as a form of cultural evolution. The account connects evolutionary computation to the automated hyperparameter optimization literature.

Cultural evolution provides a bridge between the classical evolutionary computation literature and the modern multi-agent learning literature, connecting the population-level adaptation of evolutionary algorithms to the inter-agent learning dynamics of multi-agent reinforcement learning.

## Theoretical Frameworks

The theoretical foundations of evolutionary computation include several complementary frameworks. The schema theorem of Holland 1975 provides an initial account of the dynamics of building-block selection under fitness-proportionate selection. The Building Block Hypothesis extends the framework to the conjecture that genetic algorithms succeed by combining short low-order high-fitness schemata into longer higher-fitness solutions.

The [Wolpert and Macready 1997][research_wolpert_macready_1997_nfl] No-Free-Lunch theorems established that no optimization algorithm outperforms all others averaged across all possible objective functions. The formal statement is

$$\sum_f P(y \mid f, m, a_1) = \sum_f P(y \mid f, m, a_2)$$

for any two algorithms $a_1, a_2$ and any performance metric $y$ evaluated after $m$ steps on objective function $f$, averaged uniformly across all possible $f$. The theorem provides formal grounds for the diversity of algorithmic approaches and clarifies that algorithm performance depends specifically on the structural assumptions matching the actual problem distribution.

Runtime analysis of evolutionary algorithms of [Droste et al. 2002][research_droste_jansen_wegener_2002] and subsequent work established rigorous bounds on the expected runtime of evolutionary algorithms on problem classes. This formulation provides formal complexity-theoretic grounding that complements the empirical evaluation methodology of the field. Convergence analysis of evolution strategies by [Rudolph 1997][research_rudolph_1997] established rigorous convergence results for canonical evolution strategies on standard problem classes, and the [Beyer 2001][book_beyer_2001_es_theory] theory of evolution strategies book consolidated the modern theoretical treatment. The [Doerr Doerr Kötzing Neumann 2013][research_doerr_et_al_2013_runtime] runtime-analysis framework provided more refined bounds under structural assumptions on the problem class.

Neutral theory of molecular evolution of [Kimura 1968][research_kimura_1968_neutral] established that the majority of observed genetic variation is selectively neutral, providing an important complement to the selection-driven account of evolutionary dynamics. The treatment has been adopted in computational evolutionary methods through the mechanism of neutral drift that supports the exploration of connected fitness plateaus.

Fitness landscape geometry as characterized by [Kauffman 1993][book_kauffman_1993] NK-landscape framework provides a systematic account of the structural properties that determine the difficulty of evolutionary search. This account parameterizes fitness landscapes by two integers with $N$ the number of loci and $K$ the number of epistatic interactions per locus, generating fitness values

$$F(x) = \frac{1}{N} \sum_{i=1}^{N} f_i(x_i, x_{i_1}, \ldots, x_{i_K})$$

where $f_i$ are randomly-generated per-locus fitness contributions dependent on locus $i$ and its $K$ interacting neighbors. Low-$K$ landscapes admit efficient search while high-$K$ landscapes exhibit rugged fitness landscapes with many local optima that trap greedy improvement.

The Price equation of [Price 1970][research_price_1970] provides the foundational mathematical framework for the analysis of selection dynamics, decomposing the change in a trait mean into a covariance-with-fitness component and a within-generation-change component,

$$\bar{w} \, \Delta \bar{z} = \text{Cov}(w_i, z_i) + \mathbb{E}[w_i \, \Delta z_i]$$

where $\bar{z}$ is the population mean of trait $z$, $w_i$ is the fitness of individual $i$, $\bar{w}$ is the population mean fitness, and $\Delta z_i$ is the within-generation change in trait $z$ for individual $i$'s offspring. The framework provides a common formal language for the analysis of biological and artificial selection.

Evolutionary game theory of [Nowak 2006][book_nowak_2006] provides the mathematical framework for the analysis of selection in populations with frequency-dependent fitness, connecting evolutionary computation to the multi-agent reinforcement learning treatments of article eleven through the shared replicator dynamics.

The theoretical foundations of quality-diversity and novelty search have been markedly developed in recent years. The [Doncieux et al. 2019][research_doncieux_et_al_2019_qd_theory] analysis of the quality-diversity framework provided formal grounds for the conditions under which behavioral diversity supports fitness improvement.

## Empirical Landscape and Benchmarks

The empirical landscape of evolutionary computation has consolidated around several benchmark suites. The BBOB (Black-Box Optimization Benchmark) of [Hansen et al. 2009][research_hansen_et_al_2009_bbob] provides continuous optimization test functions with known ground-truth structure, supporting systematic comparison across evolutionary and non-evolutionary black-box optimization methods.

For neural architecture search, the NAS-Bench series including NAS-Bench-101 of [Ying et al. 2019][research_ying_et_al_2019_nasbench] and NAS-Bench-201 of [Dong and Yang 2020][research_dong_yang_2020_nasbench201] provide precomputed tables of architecture performances that enable rapid evaluation and reproducibility of NAS methods.

For open-ended learning, the XLand benchmark supports the evaluation of both meta-learning and open-ended adaptation frameworks at foundation-model scale. The [Adaptive Agent Team et al. 2023][research_bauer_et_al_2023_ada_a261] Adaptive Agent extensions treated in article nine provide the foundation-model-scale open-ended learning benchmark.

For quality-diversity, standard benchmarks include continuous control tasks with behavioral descriptors defined by observed features. The QDgym benchmark of [Nilsson and Cully 2021][research_nilsson_cully_2021_qdgym] provides continuous-control quality-diversity tasks with standardized behavioral descriptors.

For coevolution, standard benchmarks include board games, adversarial reinforcement learning tasks, and predator-prey environments. The AlphaStar league benchmark of Vinyals et al 2019 has become an informal reference for coevolutionary training at foundation-model scale.

Empirical patterns across benchmarks show several consistent findings. Evolution strategies match or exceed policy-gradient methods on continuous control at appreciably better parallelization efficiency. Quality-diversity methods produce systematically more diverse solution repertoires than direct fitness optimization. Neural architecture search methods discover architectures that match or exceed hand-designed baselines on standard image classification and language modeling benchmarks. Open-ended frameworks produce continually-expanding solution distributions in short timescales but often converge to bounded distributions over longer timescales.

## Applications

Robotic design optimization has been one of the most-developed applications of evolutionary methods. The [Sims 1994][research_sims_1994_blocks] Evolving Virtual Creatures framework provided the foundational demonstration that evolutionary methods produce qualitatively-diverse morphological designs. Subsequent work has extended the framework to soft robots, legged robots, and manipulator arms. Self-modeling robots of [Bongard et al. 2006][research_bongard_zykov_lipson_2006] demonstrated that evolutionary self-modeling supports rapid recovery from unexpected morphological damage through the online discovery of alternative body configurations. Unshackling Evolution of [Cheney et al. 2013][research_cheney_et_al_2013] introduced the compositional pattern-producing network encoding for soft-robot design, producing qualitatively-different robotic morphologies than direct-encoding approaches admit.

Distilling Free-Form Natural Laws of [Schmidt and Lipson 2009][research_schmidt_lipson_2009] applied genetic programming to the discovery of physical laws from empirical data, providing evidence that evolutionary methods produce physically-meaningful mathematical expressions when appropriate structural constraints are imposed.

Neural architecture search has produced state-of-the-art architectures for image classification, object detection, and language modeling. The EfficientNet family of Tan and Le 2019 has greatly shaped subsequent architectural design practice, and NAS-derived architectures underlie significant portions of the deployed computer vision systems.

Drug discovery and molecular design use evolutionary methods for the search over chemical structure space. The [Nigam et al. 2021][research_nigam_et_al_2021] STONED framework provided a foundational modern method for evolutionary molecular design, and subsequent work has extended the account to therapeutic targets.

Materials science applications use evolutionary methods for the search over material composition and processing parameters. This formulation has been applied to alloy design, catalysis, and photovoltaic materials with substantial industrial impact.

Financial trading strategy evolution uses genetic programming to discover trading strategies from historical data. The treatment connects evolutionary computation to the broader quantitative finance literature and has been deployed at scale by systematic trading firms.

Antenna design and other engineering optimization problems use evolutionary methods for the search over design parameters. The [Lohn et al. 2006][research_lohn_hornby_linden_2006] NASA ST5 antenna provided the first flight-proven evolutionary-designed hardware component, demonstrating that evolutionary methods produce practical engineering solutions.

Game design and procedural content generation use evolutionary methods for the search over game rules, level layouts, and character designs. This account connects evolutionary computation to the broader procedural generation literature and has been deployed in commercial games.

## Neuroscience and Biological Correspondence

Biological evolution provides the foundational natural precedent for computational evolutionary methods. The [Darwin 1859][book_darwin_1859] origin of species established the framework of descent with modification under natural selection that continues to organize evolutionary biology. The Modern Synthesis of [Fisher 1930][book_fisher_1930], [Wright 1932][research_wright_1932_landscape], and [Haldane 1932][book_haldane_1932] combined Darwinian selection with Mendelian genetics through population genetics, providing the quantitative framework that computational evolutionary methods extended to artificial systems. Fisher's fundamental theorem of natural selection

$$\Delta \bar{w} = \sigma^2_A(w) / \bar{w}$$

establishes that the rate of fitness increase equals the additive genetic variance in fitness divided by the mean fitness, providing the foundational quantitative statement of adaptive evolution and its analogue in artificial evolutionary systems.

The Baldwin Effect of [Baldwin 1896][research_baldwin_1896] proposed the mechanism through which learning within a lifetime influences evolutionary trajectories across generations. The Hinton and Nowlan 1987 [research_hinton_nowlan_1987] computational demonstration of the Baldwin effect provided the first artificial-life instantiation, showing that lifetime learning smooths the fitness landscape and accelerates evolutionary discovery of adaptive traits. Formally, the Baldwin-smoothed fitness of a genotype $g$ under a lifetime learning budget $T$ is

$$F_{\text{Baldwin}}(g) = \mathbb{E}_{\pi \sim \text{Learn}_T(g)}\!\left[F(\pi)\right]$$

with $\text{Learn}\_T(g)$ the distribution of phenotypes reachable from $g$ through $T$ steps of lifetime learning. When lifetime learning can reach the fitness optimum from many nearby genotypes, the effective evolutionary fitness landscape is smoother than the direct genotype-to-fitness map.

Evolutionary developmental biology (evo-devo) of [Carroll 2005][book_carroll_2005] identified the molecular mechanisms through which conserved developmental genes produce diverse morphological outcomes, providing empirical evidence for the compositional and modular structure of biological evolution. The framework provides testable predictions about the structural conditions that support cumulative evolution.

Waddington's epigenetic landscape of [Waddington 1957][book_waddington_1957] provided the visualization framework for the canalization of developmental trajectories that produces robust phenotypes despite environmental and genetic perturbation. The formal expression through canalization functions

$$\phi_c(g) = \phi(g) + \sum_{i} h_i(g) \, \mathbb{1}[\phi(g) \in \text{basin}_i]$$

captures the attractor structure in which developmental trajectories are drawn toward canalized phenotypes despite genotypic variation. The account has been adopted in the computational literature as a metaphor for the structural properties of evolvable systems.

The Baldwin Effect and Baldwinian evolution in artificial systems has been studied extensively. The [Ackley and Littman 1991][research_ackley_littman_1991] interaction between learning and evolution framework provided one of the earliest artificial-life studies of the interactions between within-lifetime learning and across-lifetime evolutionary adaptation.

Cognitive evolution has been proposed as involving selection pressures for observational learning, cultural transmission, and theory of mind. The [Tomasello 1999][book_tomasello_1999] Cultural Origins of Human Cognition framework provided the systematic account of the cognitive adaptations that support cumulative cultural evolution in humans, and the model has organized marked subsequent developmental psychology and comparative cognition research.

Evolvability itself as an evolvable trait has been studied by [Kirschner and Gerhart 1998][research_kirschner_gerhart_1998] which identified the molecular and organizational mechanisms that support the evolution of evolvability. This formulation predicts that structural properties including modularity, weak linkage, and exploratory processes support the accumulation of adaptive complexity across evolutionary time. Robustness and evolvability of [Wagner 2005][book_wagner_2005] provided the systematic treatment of the relationship between phenotypic robustness and the capacity for evolutionary innovation, providing testable predictions about the structural properties of evolvable systems.

Evolution of cooperation of [Axelrod 1984][book_axelrod_1984] and the evolutionary game-theoretic analyses of [Nowak and May 1992][research_nowak_may_1992] established the formal frameworks for the analysis of cooperative behavior evolution in structured populations, connecting evolutionary computation to the broader mathematical biology of social interaction.

Neuroevolution as biological hypothesis-testing has been proposed by [Miconi 2017][research_miconi_2016_biologically_plausible] and subsequent work as a framework for testing hypotheses about the evolutionary origins of neural learning mechanisms. The treatment connects computational evolutionary methods to the empirical questions of comparative neurobiology.

Article fourteen returns to the NeuroAI bridge and treats the evolutionary correspondence in greater detail alongside the broader mapping between machine learning and neuroscience.

## Load-Bearing Open Questions

- What are the structural conditions under which sustained open-ended evolution occurs, and can these conditions be systematically engineered in artificial systems?
- How should evolutionary methods be combined with gradient-based reinforcement learning to leverage the strengths of both frameworks?
- What is the correct theoretical framework for quality-diversity that characterizes when behavioral diversity supports fitness improvement versus when it produces distributional drift?
- Can neural architecture search be reliably combined with continual and lifelong learning to produce architectures that evolve alongside the tasks they solve?
- How closely do the biological mechanisms of the Baldwin effect and evo-devo correspond to computational evolutionary methods, and where do the correspondences fail?
- What is the correct treatment of coevolutionary instability and cycling in adversarial multi-population settings?
- Can language-model-mediated evolution be reliably scaled to open-ended settings that produce genuinely novel task specifications rather than paraphrased variations of existing tasks?
- How should evolutionary methods handle the fitness-evaluation cost trade-off in settings where full fitness evaluation requires extensive compute per candidate?
- What is the correct account of cultural evolution in artificial multi-agent systems, and can specifically-human patterns of cumulative culture be reproduced through appropriate transmission mechanisms?
- Can evolutionary methods be reliably combined with the foundation-model paradigm to produce systems that improve through both gradient-based and population-based mechanisms simultaneously?

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Beyer, Hans-Georg, and Hans-Paul Schwefel. 2002. "Evolution Strategies – a Comprehensive Introduction." *Natural Computing* 1 (1): 3–52. [https://doi.org/10.1023/a:1015059928466][research_beyer_schwefel_2002]
- Cully, Antoine, Jeff Clune, Danesh Tarapore, and Jean-Baptiste Mouret. 2015. "Robots That Can Adapt like Animals." *Nature* 521 (7553): 503–7. [https://doi.org/10.1038/nature14422][research_cully_et_al_2015_robots]
- Dorigo, M., V. Maniezzo, and A. Colorni. 1996. "Ant System: Optimization by a Colony of Cooperating Agents." *IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics)* 26 (1): 29–41. [https://doi.org/10.1109/3477.484436][research_dorigo_maniezzo_colorni_1996]
- Floreano, Dario, Peter Dürr, and Claudio Mattiussi. 2008. "Neuroevolution: From Architectures to Learning." *Evolutionary Intelligence* 1 (1): 47–62. [https://doi.org/10.1007/s12065-007-0002-4][research_floreano_durr_mattiussi_2008]
- Lenski, Richard E., Charles Ofria, Robert T. Pennock, and Christoph Adami. 2003. "The Evolutionary Origin of Complex Features." *Nature* 423 (6936): 139–44. [https://doi.org/10.1038/nature01568][research_lenski_et_al_2003]
- Nowak, Martin A., and Robert M. May. 1992. "Evolutionary Games and Spatial Chaos." *Nature* 359 (6398): 826–29. [https://doi.org/10.1038/359826a0][research_nowak_may_1992]
- Pugh, Justin K., Lisa B. Soros, and Kenneth O. Stanley. 2016. "Quality Diversity: A New Frontier for Evolutionary Computation." *Frontiers in Robotics and AI* 3. [https://doi.org/10.3389/frobt.2016.00040][research_pugh_soros_stanley_2016_qd]
- Romera-Paredes, Bernardino, Mohammadamin Barekatain, Alexander Novikov, et al. 2023. "Mathematical Discoveries from Program Search with Large Language Models." *Nature* 625 (7995): 468–75. [https://doi.org/10.1038/s41586-023-06924-6][research_romera_paredes_et_al_2024_funsearch]
- Stanley, Kenneth O. 2007. "Compositional Pattern Producing Networks: A Novel Abstraction of Development." *Genetic Programming and Evolvable Machines* 8 (2): 131–62. [https://doi.org/10.1007/s10710-007-9028-8][research_stanley_2007_cppn]
- Stanley, Kenneth O., Jeff Clune, Joel Lehman, and Risto Miikkulainen. 2019. "Designing Neural Networks through Neuroevolution." *Nature Machine Intelligence* 1 (1): 24–35. [https://doi.org/10.1038/s42256-018-0006-z][research_stanley_et_al_2019_neuroevolution]
- Storn, Rainer, and Kenneth Price. 1997. "Differential Evolution – a Simple and Efficient Heuristic for Global Optimization over Continuous Spaces." *Journal of Global Optimization* 11 (4): 341–59. [https://doi.org/10.1023/a:1008202821328][research_storn_price_1997_de]
- Whitley, Darrell. 1994. "A Genetic Algorithm Tutorial." *Statistics and Computing* 4 (2). [https://doi.org/10.1007/bf00175354][research_whitley_1994]
- Wu, Bichen, Kurt Keutzer, Xiaoliang Dai, et al. 2019. "FBNet: Hardware-Aware Efficient ConvNet Design via Differentiable Neural Architecture Search." In *2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. IEEE. [https://doi.org/10.1109/cvpr.2019.01099][research_wu_et_al_2019_fbnet]

### Primary Sources, Non-Peer-Reviewed

- Adaptive Agent Team, Jakob Bauer, Kate Baumli, et al. 2023. "Human-Timescale Adaptation in an Open-Ended Task Space." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2301.07608][research_bauer_et_al_2023_ada_a261]
- Baldwin, J. Mark. 1896. "A New Factor in Evolution." *American Naturalist* 30 (354): 441–51. [https://doi.org/10.1086/276408][research_baldwin_1896]
- Bongard, Josh, Victor Zykov, and Hod Lipson. 2006. "Resilient Machines through Continuous Self-Modeling." *Science* 314 (5802): 1118–21. [https://doi.org/10.1126/science.1133687][research_bongard_zykov_lipson_2006]
- Bradley, Nordmoen, Stanley, and Lehman. 2024. *OpenELM*. [https://scholar.google.com/scholar?q=OpenELM+Bradley+2024][research_bradley_et_al_2024_openelm]
- Cai, Han, Ligeng Zhu, and Song Han. 2019. "ProxylessNAS: Direct Neural Architecture Search on Target Task and Hardware." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=HylVB3AqYm][research_cai_zhu_han_2019_proxyless]
- Chalumeau, Cully, Grillotti, Bonnet, Miret, and Flajolet. 2024. *QD-RL*. [https://scholar.google.com/scholar?q=QD-RL+Chalumeau+2024][research_chalumeau_et_al_2024_qd_rl]
- Chatzilygeroudis, Cully, Vassiliades, and Mouret. 2021. *QD Overview*. [https://scholar.google.com/scholar?q=QD+Overview+Chatzilygeroudis+2021][research_chatzilygeroudis_et_al_2021_qd_overview]
- Cheney, Nick, Robert MacCurdy, Jeff Clune, and Hod Lipson. 2013. "Unshackling Evolution: Evolving Soft Robots with Multiple Materials and a Powerful Generative Encoding." In *Proceedings of the 15th annual conference on Genetic and evolutionary computation*. ACM. [https://doi.org/10.1145/2463372.2463404][research_cheney_et_al_2013]
- Clune, Jeff. 2019. "AI-GAs: AI-Generating Algorithms, an Alternate Paradigm for Producing General Artificial Intelligence." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1905.10985][research_clune_2019_aigas]
- Colas, Cédric, Olivier Sigaud, and Pierre-Yves Oudeyer. 2018. "GEP-PG: Decoupling Exploration and Exploitation in Deep Reinforcement Learning Algorithms." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v80/colas18a.html][research_colas_sigaud_oudeyer_2018_geppg]
- Cranmer, Miles, Alvaro Sanchez Gonzalez, Peter Battaglia, et al. 2020. "Discovering Symbolic Models from Deep Learning with Inductive Biases." *Advances in Neural Information Processing Systems* 33: 17429–42. [https://papers.nips.cc/paper/2020/hash/c9f2f917078bd2db12f23c3b413d9cba-Abstract.html][research_cranmer_et_al_2020]
- Dong, Xuanyi, and Yi Yang. 2020. "NAS-Bench-201: Extending the Scope of Reproducible Neural Architecture Search." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=HJxyZkBKDr][research_dong_yang_2020_nasbench201]
- Elsken, Thomas, Jan Hendrik Metzen, and Frank Hutter. 2019. "Neural Architecture Search: A Survey." *Journal of Machine Learning Research* 20: 1–21. [https://jmlr.org/papers/v20/18-598.html][research_elsken_metzen_hutter_2019_nas_survey]
- Faldor, Maxence, Jenny Zhang, Antoine Cully, and Jeff Clune. 2024. "OMNI-EPIC: Open-Endedness via Models of Human Notions of Interestingness with Environments Programmed in Code." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2405.15568][research_faldor_et_al_2024_omni_epic]
- Faldor Cully. 2024. *QD Survey*. [https://scholar.google.com/scholar?q=QD+Survey+Faldor+Cully+2024][research_faldor_cully_2024_qd_survey]
- Fernando, Chrisantha, Dylan Banarse, Henryk Michalewski, Simon Osindero, and Tim Rocktäschel. 2023. "Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2309.16797][research_fernando_et_al_2023_promptbreeder]
- Fontaine, Matthew C., Julian Togelius, Stefanos Nikolaidis, and Amy K. Hoover. 2020. "Covariance Matrix Adaptation for the Rapid Illumination of Behavior Space." In *Proceedings of the 2020 Genetic and Evolutionary Computation Conference*. ACM. [https://doi.org/10.1145/3377930.3390232][research_fontaine_et_al_2020_cma_me_orig]
- Fontaine Nikolaidis. 2021a. *CMA-ME*. [https://scholar.google.com/scholar?q=CMA-ME+Fontaine+Nikolaidis+2021][research_fontaine_nikolaidis_2021_cmame]
- Grillotti and Cully. 2022. *Modular QD*. [https://scholar.google.com/scholar?q=Modular+QD+Grillotti+Cully+2022][research_grillotti_cully_2022]
- Guo, Qingyan, Rui Wang, Junliang Guo, et al. 2023. "EvoPrompt: Connecting LLMs with Evolutionary Algorithms Yields Powerful Prompt Optimizers." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2309.08532][research_chen_et_al_2024_evoprompt]
- Hansen, Nikolaus. 2016. "The CMA Evolution Strategy: A Tutorial." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1604.00772][research_hansen_2016_cmaes_tutorial]
- Hornby and Pollack. 2001. *L-System*. [https://scholar.google.com/scholar?q=L-System+Hornby+Pollack+2001][research_hornby_pollack_2001]
- Kamienny, Pierre-Alexandre, Stéphane D'Ascoli, Guillaume Lample, and Francois Charton. 2022. "End-To-End Symbolic Regression with Transformers." In *Advances in Neural Information Processing Systems 35*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/068431-0746][research_kamienny_et_al_2022]
- Kelly Bowling. 2020. *GSAC*. [https://scholar.google.com/scholar?q=GSAC+Kelly+Bowling+2020][research_kelly_bowling_2020_gsac]
- Kimura, Motoo. 1968. "Evolutionary Rate at the Molecular Level." *Nature* 217 (5129): 624–26. [https://doi.org/10.1038/217624a0][research_kimura_1968_neutral]
- Kirby, Cornish, and Smith. 2015. *Iterated*. [https://scholar.google.com/scholar?q=Iterated+Kirby+Cornish+Smith+2015][research_kirby_cornish_smith_2015_a261]
- Kirkpatrick, S., C. D. Gelatt, and M. P. Vecchi. 1983. "Optimization by Simulated Annealing." *Science* 220 (4598): 671–80. [https://doi.org/10.1126/science.220.4598.671][research_kirkpatrick_gelatt_vecchi_1983]
- Kirschner, Marc, and John Gerhart. 1998. "Evolvability." *Proceedings of the National Academy of Sciences* 95 (15): 8420–27. [https://doi.org/10.1073/pnas.95.15.8420][research_kirschner_gerhart_1998]
- Kriegman, Sam, Douglas Blackiston, Michael Levin, and Josh Bongard. 2020. "A Scalable Pipeline for Designing Reconfigurable Organisms." *Proceedings of the National Academy of Sciences* 117 (4): 1853–59. [https://doi.org/10.1073/pnas.1910837117][research_kriegman_et_al_2020]
- La Cava, William, Patryk Orzechowski, Bogdan Burlacu, et al. 2021. "Contemporary Symbolic Regression Methods and Their Relative Performance." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2107.14351][research_lacava_et_al_2021]
- Lehman, Joel, Jonathan Gordon, Shawn Jain, Kamal Ndousse, Cathy Yeh, and Kenneth O. Stanley. 2022. "Evolution through Large Models." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2206.08896][research_lehman_et_al_2023_elm]
- Liu, Hanxiao, Karen Simonyan, and Yiming Yang. 2019. "DARTS: Differentiable Architecture Search." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=S1eYHoC5FX][research_liu_simonyan_yang_2019_darts]
- Lohn, Hornby, and Linden. 2006. *\[Title not identified\]*. [https://ntrs.nasa.gov/citations/20060005022][research_lohn_hornby_linden_2006]
- Ma, Yecheng Jason, William Liang, Guanzhi Wang, et al. 2023. "Eureka: Human-Level Reward Design via Coding Large Language Models." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2310.12931][research_ma_et_al_2023_eureka]
- Meyerson, Elliot, Mark J. Nelson, Herbie Bradley, et al. 2023. "Language Model Crossover: Variation through Few-Shot Prompting." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2302.12170][research_meyerson_et_al_2023_lmx]
- Miconi, Thomas. 2017. "Biologically Plausible Learning in Recurrent Neural Networks Reproduces Neural Dynamics Observed during Cognitive Tasks." *eLife* 6: e20899. [https://doi.org/10.7554/elife.20899][research_miconi_2016_biologically_plausible]
- Miller. 2004. *Embryology*. [https://scholar.google.com/scholar?q=Embryology+Miller+2004][research_miller_2004_embryology]
- Mouret, Jean-Baptiste, and Jeff Clune. 2015. "Illuminating Search Spaces by Mapping Elites." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1504.04909][research_mouret_clune_2015_mapelites]
- Nilsson and Cully. 2021. *QDgym*. [https://scholar.google.com/scholar?q=QDgym+Nilsson+Cully+2021][research_nilsson_cully_2021_qdgym]
- Nowak, Martin A., Corina E. Tarnita, and Tibor Antal. 2010. "Evolutionary Dynamics in Structured Populations." *Philosophical Transactions of the Royal Society B: Biological Sciences* 365 (1537): 19–30. [https://doi.org/10.1098/rstb.2009.0215][research_nowak_tarnita_antal_2010]
- Ofria, Charles, and Claus O. Wilke. 2004. "Avida: A Software Platform for Research in Computational Evolutionary Biology." *Artificial Life* 10 (2): 191–229. [https://doi.org/10.1162/106454604773563612][research_ofria_wilke_2004_avida]
- Open-Ended, Learning, and Team. 2021. *\[Title not identified\]*. [https://scholar.google.com/scholar?q=Open-Ended+Learning+Team+2021][research_openendedlearningteam_2021]
- Popovici, Elena, Anthony Bucci, R. Paul Wiegand, and Edwin D. De Jong. 2012. "Coevolutionary Principles." In *Handbook of Natural Computing*. Springer Berlin Heidelberg. [https://doi.org/10.1007/978-3-540-92910-9\_31][research_popovici_et_al_2012_coevolution]
- Portelas, Rémy, Cédric Colas, Lilian Weng, Katja Hofmann, and Pierre-Yves Oudeyer. 2020. "Automatic Curriculum Learning for Deep RL: A Short Survey." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2003.04664][research_portelas_et_al_2020_acl_a261]
- Pourchot and Sigaud. 2019. "CEM-RL: Combining Evolutionary and Gradient-Based Methods for Policy Search." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=BkeU5j0ctQ][research_pourchot_sigaud_2019_cemrl]
- Real, Esteban, Alok Aggarwal, Yanping Huang, and Quoc V. Le. 2019. "Regularized Evolution for Image Classifier Architecture Search." *Proceedings of the AAAI Conference on Artificial Intelligence* 33 (01): 4780–89. [https://doi.org/10.1609/aaai.v33i01.33014780][research_real_et_al_2019_amoebanet]
- Real, Esteban, Chen Liang, David So, and Quoc Le. 2020. "AutoML-Zero: Evolving Machine Learning Algorithms from Scratch." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v119/real20a.html][research_real_et_al_2020_automlzero]
- Real, Esteban, Sherry Moore, Andrew Selle, et al. 2017. "Large-Scale Evolution of Image Classifiers." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v70/real17a.html][research_real_et_al_2017_large_scale]
- Salimans, Tim, Jonathan Ho, Xi Chen, Szymon Sidor, and Ilya Sutskever. 2017. "Evolution Strategies as a Scalable Alternative to Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1703.03864][research_salimans_et_al_2017_es]
- Schmidt, Michael, and Hod Lipson. 2009. "Distilling Free-Form Natural Laws from Experimental Data." *Science* 324 (5923): 81–85. [https://doi.org/10.1126/science.1165893][research_schmidt_lipson_2009]
- Sigaud. 2023. *ERL Survey*. [https://scholar.google.com/scholar?q=ERL+Survey+Sigaud+2023][research_sigaud_2023_erl_survey]
- Sims, Karl. 1994. "Evolving Virtual Creatures." In *Proceedings of the 21st annual conference on Computer graphics and interactive techniques - SIGGRAPH '94*. ACM Press. [https://doi.org/10.1145/192161.192167][research_sims_1994_blocks]
- Standish, Russell K. 2003. "Open-Ended Artificial Evolution." *International Journal of Computational Intelligence and Applications* 03 (02): 167–75. [https://doi.org/10.1142/s1469026803000914][research_standish_2003_open_ended]
- Such, Felipe Petroski, Vashisht Madhavan, Edoardo Conti, Joel Lehman, Kenneth O. Stanley, and Jeff Clune. 2017. "Deep Neuroevolution: Genetic Algorithms Are a Competitive Alternative for Training Deep Neural Networks for Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1712.06567][research_such_et_al_2017_deep_neuroevolution]
- Tan, Mingxing, and Quoc Le. 2019. "EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v97/tan19a.html][research_tan_le_2019_efficientnet]
- Wang, Rui, Joel Lehman, Jeff Clune, and Kenneth O. Stanley. 2019. "Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1901.01753][research_wang_et_al_2019_poet_a261]
- Wang, Rui, Joel Lehman, Aditya Rawal, et al. 2020. "Enhanced POET: Open-Ended Reinforcement Learning through Unbounded Invention of Learning Challenges and Their Solutions." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v119/wang20l.html][research_wang_et_al_2020_epoet]
- Waser and Adami. 2018. *Transitions*. [https://scholar.google.com/scholar?q=Transitions+Waser+Adami+2018][research_waser_adami_2018]
- Ying, Chris, Aaron Klein, Eric Christiansen, Esteban Real, Kevin Murphy, and Frank Hutter. 2019. "NAS-Bench-101: Towards Reproducible Neural Architecture Search." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v97/ying19a.html][research_ying_et_al_2019_nasbench]

### Secondary Sources

- Adami, Christoph. 1998. *Introduction to Artificial Life*. Springer New York. [https://doi.org/10.1007/978-1-4612-1650-6][book_adami_1998]
- Axelrod, Robert M. 1984. *The Evolution of Cooperation*. Basic Books. [https://basicbooks.com/titles/robert-axelrod/the-evolution-of-cooperation/9780465005642/][book_axelrod_1984]
- Back Fogel Michalewicz. 1997. *Handbook*. [https://www.taylorfrancis.com/books/edit/10.1201/9781420050387/handbook-evolutionary-computation-thomas-back-david-fogel-zbigniew-michalewicz][book_back_fogel_michalewicz_1997]
- Beyer, Hans-Georg. 2001. *The Theory of Evolution Strategies*. Springer Berlin Heidelberg. [https://doi.org/10.1007/978-3-662-04378-3][book_beyer_2001_es_theory]
- Boyd, Robert Ph. D., and Richerson. 1985. *Culture and the Evolutionary Process*. University of Chicago Press. [https://press.uchicago.edu/ucp/books/book/chicago/C/bo5972728.html][book_boyd_richerson_1985]
- Carroll, Sean B. 2005. *Endless Forms Most Beautiful: The New Science of Evo Devo and the Making of the Animal Kingdom*. W.W. Norton & Co. [https://wwnorton.com/books/9780393327793][book_carroll_2005]
- Cavalli-Sforza, Luigi Luca, and Marcus W. Feldman. 1981. *Cultural Transmission and Evolution: A Quantitative Approach*. Princeton University Press. [https://press.princeton.edu/books/paperback/9780691082837/cultural-transmission-and-evolution][book_cavalli_sforza_feldman_1981]
- Darwin. 1859. *Origin of Species*. [https://darwin-online.org.uk/content/frameset?itemID=F373&viewtype=text&pageseq=1][book_darwin_1859]
- Dawkins, Richard. 1976. *The Selfish Gene*. BBC. [https://global.oup.com/academic/product/the-selfish-gene-9780198788607][book_dawkins_1976]
- Fisher, Ronald Aylmer. 1930. *The Genetical Theory of Natural Selection*. The Clarendon Press. [https://global.oup.com/academic/product/the-genetical-theory-of-natural-selection-9780198504405][book_fisher_1930]
- Goldberg, David E. 1989. *Genetic Algorithms in Search, Optimization, and Machine Learning*. Addison-Wesley Pub. Co. [https://dl.acm.org/doi/book/10.5555/534133][book_goldberg_1989]
- Haldane, J. B. S. 1932. *The Causes of Evolution*. Longmans, Green and co. [https://press.princeton.edu/books/paperback/9780691024424/the-causes-of-evolution][book_haldane_1932]
- Henrich, Joseph Patrick. 2016. *The Secret of Our Success: How Culture Is Driving Human Evolution, Domesticating Our Species, and Making Us Smarter*. Princeton University Press. [https://press.princeton.edu/books/paperback/9780691178431/the-secret-of-our-success][book_henrich_2016]
- Holland, John H. 1975. *Adaptation in Natural and Artificial Systems: An Introductory Analysis with Applications to Biology, Control, and Artificial Intelligence*. University of Michigan Press. [https://mitpress.mit.edu/9780262581110/adaptation-in-natural-and-artificial-systems/][book_holland_1975]
- Kauffman, Stuart A. 1993. *The Origins of Order: Self-Organization and Selection in Evolution*. Oxford University Press. [https://global.oup.com/academic/product/the-origins-of-order-9780195079517][book_kauffman_1993]
- Koza, John R. 1992. *Genetic Programming: On the Programming of Computers by Means of Natural Selection*. MIT Press. [https://mitpress.mit.edu/9780262111706/genetic-programming/][book_koza_1992]
- Larrañaga, Pedro, and Jose A. Lozano, eds. 2002. *Estimation of Distribution Algorithms*. Springer US. [https://doi.org/10.1007/978-1-4615-1539-5][book_larranaga_lozano_2002]
- Maynard, John Maynard Smith, and Szathmáry. 1995. *The Major Transitions in Evolution*. W.H. Freeman Spektrum. [https://global.oup.com/academic/product/the-major-transitions-in-evolution-9780198502944][book_maynard_smith_szathmary_1995]
- Nowak, Martin A. 2006. *Evolutionary Dynamics: Exploring the Equations of Life*. Harvard University Press. [https://www.hup.harvard.edu/books/9780674023383][book_nowak_2006]
- Sutton, Richard S., and Barto. 2018. *Reinforcement Learning: An Introduction*. MIT Press. [http://incompleteideas.net/book/the-book-2nd.html][book_sutton_barto_2018]
- Tomasello, Michael. 1999. *Cultural Origins of Human Cognition*. Harvard University Press. [https://www.hup.harvard.edu/books/9780674005822][book_tomasello_1999]
- Von Neumann, John. 1966. *Theory of Self-Reproducing Automata*. University of Illinois Press. [https://cba.mit.edu/events/03.11.ASE/docs/VonNeumann.pdf][book_von_neumann_1966]
- Waddington, Conrad H. 1957. *The Strategy of the Genes: A Discussion of Some Aspects of Theoretical Biology*. Allen & Unwin. [https://www.taylorfrancis.com/books/mono/10.4324/9781315766744/strategy-genes-waddington][book_waddington_1957]
- Wagner, Andreas. 2005. *Robustness and Evolvability in Living Systems*. Princeton University Press. [https://press.princeton.edu/books/paperback/9780691134079/robustness-and-evolvability-in-living-systems][book_wagner_2005]

### Commercial Sources

- "DeepMind x UCL RL Course." n.d. Accessed October 25, 2026. [https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021][ref_deepmind_ucl_rl]
- "OpenAI Spinning Up." n.d. Accessed October 25, 2026. [https://spinningup.openai.com/][ref_openai_spinning_up]

### General Sources

- Ackley and Littman. 1991. "\[Title not identified\]." Accessed October 25, 2026. [https://direct.mit.edu/isal/proceedings-abstract/alife/487/99257][research_ackley_littman_1991]
- Bedau. 1998. "Four Questions." [https://direct.mit.edu/artl/article-abstract/4/1/125/2321][research_bedau_1998_four_questions]
- Bentley and Kumar. 1999. "Encoding." [https://dl.acm.org/doi/10.5555/2933923.2933989][research_bentley_kumar_1999]
- "Berkeley CS285." n.d. Accessed October 25, 2026. [https://rail.eecs.berkeley.edu/deeprlcourse/][ref_berkeley_cs285]
- Bongard. 2004. "Coevolutionary." [https://www.pnas.org/doi/10.1073/pnas.0405301102][research_bongard_2004_coevolutionary]
- Cliff and Miller. 1996. "\[Title not identified\]." Accessed October 25, 2026. [https://link.springer.com/chapter/10.1007/3-540-61314-3\_10][research_cliff_miller_1996]
- Conti, Madhavan, Such, et al. 2018. "NS-ES." [https://papers.nips.cc/paper/2018/hash/b1301141feffabac455e1f90a7de2054-Abstract.html][research_conti_et_al_2018_nses]
- Cully and Demiris. 2018. "QD Review." [https://ieeexplore.ieee.org/document/8237407][research_cully_demiris_2018_qd_review]
- De Jong. 1975. "\[Title not identified\]." Accessed October 25, 2026. [https://deepblue.lib.umich.edu/handle/2027.42/4507][research_dejong_1975]
- Deb and Jain. 2013. "NSGA-III." [https://ieeexplore.ieee.org/document/6600851][research_deb_jain_2013_nsga3]
- Deb Pratap Agarwal Meyarivan. 2002. "NSGA-II." [https://ieeexplore.ieee.org/document/996017][research_deb_et_al_2002_nsga2]
- Dennis, Jaques, Hughes, et al. 2020. "PAIRED." [https://papers.nips.cc/paper/2020/hash/985e9a46e10005356bbaf194249f6856-Abstract.html][research_dennis_et_al_2020_paired_a261]
- Doerr Doerr Kötzing Neumann. 2013. "Runtime." [https://link.springer.com/article/10.1007/s00453-011-9585-3][research_doerr_et_al_2013_runtime]
- Doncieux, Laflaquière, and Coninx. 2019. "QD Theory." [https://link.springer.com/article/10.1007/s10710-019-09343-3][research_doncieux_et_al_2019_qd_theory]
- Droste, Jansen, and Wegener. 2002. "\[Title not identified\]." Accessed October 25, 2026. [https://link.springer.com/article/10.1023/A:1013951316365][research_droste_jansen_wegener_2002]
- Ficici and Pollack. 2001. "Pareto." [https://direct.mit.edu/evco/article-abstract/9/2/183/1099][research_ficici_pollack_2001_pareto]
- Fogel, Owens, and Walsh. 1966. "\[Title not identified\]." Accessed October 25, 2026. [https://dl.acm.org/doi/book/10.5555/1096080][research_fogel_owens_walsh_1966]
- Fontaine Nikolaidis. 2021b. "DQD." [https://papers.nips.cc/paper/2021/hash/532b7cbe070a3579f424988a040752f2-Abstract.html][research_fontaine_nikolaidis_2021_dqd]
- Hansen, Finck, Ros, and Auger. 2009. "BBOB." [https://coco.gforge.inria.fr/doku.php?id=bbob-2009][research_hansen_et_al_2009_bbob]
- Hansen and Ostermeier. 2001. "CMA-ES." [https://direct.mit.edu/evco/article-abstract/9/2/159/1090][research_hansen_ostermeier_2001_cmaes]
- Hinton and Nowlan. 1987. "\[Title not identified\]." Accessed October 25, 2026. [https://www.cs.toronto.edu/~hinton/absps/baldwin.pdf][research_hinton_nowlan_1987]
- Igel. 2003. "NEAT-RL." [https://ieeexplore.ieee.org/document/1299617][research_igel_2003]
- Igel Hansen Roth. 2007. "MO-CMA-ES." [https://direct.mit.edu/evco/article-abstract/15/1/1/1230][research_igel_hansen_roth_2007_moes]
- Kennedy and Eberhart. 1995. "PSO." [https://ieeexplore.ieee.org/document/488968][research_kennedy_eberhart_1995_pso]
- Khadka and Tumer. 2018. "ERL." [https://papers.nips.cc/paper/2018/hash/85fc37b18c57097425b52fc7afbb6969-Abstract.html][research_khadka_tumer_2018_erl]
- Langton. 1986. "ALife." [https://www.sciencedirect.com/science/article/abs/pii/0167278986902374][research_langton_1986_alife]
- Lehman and Stanley. 2011. "Novelty." [https://direct.mit.edu/evco/article-abstract/19/2/189/1365][research_lehman_stanley_2011_abandoning]
- Miikkulainen, Liang, Meyerson, et al. 2019. "\[Title not identified\]." Accessed October 25, 2026. [https://www.sciencedirect.com/science/article/pii/B9780128159804000151][research_miikkulainen_et_al_2019]
- Mühlenbein. 1997. "EDA." [https://direct.mit.edu/evco/article-abstract/5/3/303/1176][research_muhlenbein_1997_eda]
- Nigam, Friederich, Krenn, and Aspuru-Guzik. 2021. "STONED." [https://pubs.rsc.org/en/content/articlehtml/2021/sc/d1sc00231g][research_nigam_et_al_2021]
- Pelikan Goldberg Cantú-Paz. 2000. "BOA." [https://direct.mit.edu/evco/article-abstract/8/3/311/1113][research_pelikan_goldberg_cantupaz_2000_boa]
- Petersen. 2021. "DSR." [https://openreview.net/forum?id=m5Qsh0kBQG][research_petersen_et_al_2021_dsr]
- Pham, Guan, Zoph, Le, and Dean. 2018. "ENAS." [https://proceedings.mlr.press/v80/pham18a.html][research_pham_et_al_2018_enas]
- Potter and De Jong. 2000. "Cooperative." [https://direct.mit.edu/evco/article-abstract/8/1/1/819][research_potter_dejong_2000]
- Price. 1970. "Price Equation." [https://www.nature.com/articles/227520a0][research_price_1970]
- Ray. 1991. "Tierra." [https://direct.mit.edu/isal/proceedings-abstract/alife/470/99202][research_ray_1991_tierra]
- Rechenberg. 1973. "Evolutionsstrategie." [https://scholar.google.com/scholar?q=rechenberg+1973+evolutionsstrategie][research_rechenberg_1973]
- Risi and Stanley. 2012. "ES-HyperNEAT." [https://direct.mit.edu/artl/article-abstract/18/4/331/2769][research_risi_stanley_2012_eshyperneat]
- Rosin and Belew. 1997. "Hall of Fame." [https://direct.mit.edu/evco/article-abstract/5/1/1/847][research_rosin_belew_1997]
- Rudolph. 1997. "Convergence." [https://link.springer.com/article/10.1023/A:1018503430137][research_rudolph_1997]
- Sayama. 2009. "ALife OEE." [https://direct.mit.edu/artl/article-abstract/16/1/71/2492][research_sayama_2009]
- Schwefel. 1977. "\[Title not identified\]." Accessed October 25, 2026. [https://scholar.google.com/scholar?q=schwefel+1977+numerische+optimierung][research_schwefel_1977]
- "Silver RL Course UCL." n.d. Accessed October 25, 2026. [https://www.davidsilver.uk/teaching/][ref_silver_rl_course]
- Soros and Stanley. 2014. "MCC." [https://direct.mit.edu/isal/proceedings-abstract/alife2014/26/638][research_soros_stanley_2014_mcc]
- "Stanford CS234." n.d. Accessed October 25, 2026. [https://web.stanford.edu/class/cs234/][ref_stanford_cs234]
- Stanley and Miikkulainen. 2002. "NEAT." [https://direct.mit.edu/evco/article-abstract/10/2/99/1123][research_stanley_miikkulainen_2002_neat]
- Stanley D'Ambrosio Gauci. 2009. "HyperNEAT." [https://direct.mit.edu/artl/article-abstract/15/2/185/2578][research_stanley_dambrosio_gauci_2009_hyperneat]
- Taylor. 2016. "OEE Roadmap." [https://direct.mit.edu/artl/article-abstract/22/3/408/2717][research_taylor_et_al_2016_oee]
- Thompson. 1997. "Evolvable Hardware." [https://link.springer.com/chapter/10.1007/BFb0041008][research_thompson_1997_evolvable_hardware]
- Vassiliades, Chatzilygeroudis, and Mouret. 2018. "CVT-MAP-Elites." [https://ieeexplore.ieee.org/document/8000704][research_vassiliades_et_al_2018_cvt]
- Watson and Pollack. 2001. "Symbiotic." [https://direct.mit.edu/evco/article-abstract/9/2/213/1097][research_watson_pollack_2001]
- Wierstra, Schaul, Peters, and Schmidhuber. 2014. "NES." [https://jmlr.org/papers/v15/wierstra14a.html][research_wierstra_et_al_2014_nes]
- Wolpert and Macready. 1997. "NFL." [https://ieeexplore.ieee.org/document/585893][research_wolpert_macready_1997_nfl]
- Wright. 1932. "Landscape." [https://www.esp.org/foundations/genetics/classical/holdings/w/wright-1932.pdf][research_wright_1932_landscape]
- Xie, Zheng, Liu, and Lin. 2019. "SNAS." [https://openreview.net/forum?id=rylqooRqK7][research_xie_et_al_2019_snas]
- Yao. 1999. "Evolving ANN." [https://ieeexplore.ieee.org/document/784219][research_yao_1999]
- Zhang and Li. 2007. "MOEA/D." [https://ieeexplore.ieee.org/document/4358754][research_zhang_li_2007_moead]
- Zitzler Laumanns Thiele. 2001. "SPEA2." [https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=10.1.1.28.7571][research_zitzler_laumanns_thiele_2001_spea2]
- Zoph and Le. 2017. "NAS." [https://openreview.net/forum?id=r1Ue8Hcxg][research_zoph_le_2017_nas]

### Related Posts

- Sechter, Brendan. 2025. "Machines That Learn From Experience: Framing." *Brendan A R Sechter's Development Blog*, December 18. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/18/machines\_that\_learn\_from\_experience\_framing.html][related_post_a250_framing]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Bandits and Online Learning." *Brendan A R Sechter's Development Blog*, December 19. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/19/machines\_that\_learn\_from\_experience\_bandits\_and\_online\_learning.html][related_post_a251_bandits]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Reinforcement Learning Foundations." *Brendan A R Sechter's Development Blog*, December 20. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/20/machines\_that\_learn\_from\_experience\_reinforcement\_learning\_foundations.html][related_post_a252_rl_foundations]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Deep Reinforcement Learning." *Brendan A R Sechter's Development Blog*, December 21. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/21/machines\_that\_learn\_from\_experience\_deep\_reinforcement\_learning.html][related_post_a253_deep_rl]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Exploration, Intrinsic Motivation, and Curiosity." *Brendan A R Sechter's Development Blog*, December 22. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/22/machines\_that\_learn\_from\_experience\_exploration\_intrinsic\_motivation\_and\_curiosity.html][related_post_a254_exploration]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Hierarchical Reinforcement Learning." *Brendan A R Sechter's Development Blog*, December 23. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/23/machines\_that\_learn\_from\_experience\_hierarchical\_reinforcement\_learning.html][related_post_a255_hierarchical]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: World Models and Predictive, Model-Based Adaptation." *Brendan A R Sechter's Development Blog*, December 24. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/24/machines\_that\_learn\_from\_experience\_world\_models\_and\_predictive\_model\_based\_adaptation.html][related_post_a256_world_models]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Offline and Batch Reinforcement Learning." *Brendan A R Sechter's Development Blog*, December 25. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/25/machines\_that\_learn\_from\_experience\_offline\_and\_batch\_reinforcement\_learning.html][related_post_a257_offline]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Meta-Learning and Online Adaptation." *Brendan A R Sechter's Development Blog*, December 26. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/26/machines\_that\_learn\_from\_experience\_meta\_learning\_and\_online\_adaptation.html][related_post_a258_meta_learning]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Continual and Lifelong Learning." *Brendan A R Sechter's Development Blog*, December 27. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/27/machines\_that\_learn\_from\_experience\_continual\_and\_lifelong\_learning.html][related_post_a259_continual]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Learning From Demonstration, Preference, and Other Agents." *Brendan A R Sechter's Development Blog*, December 28. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/28/machines\_that\_learn\_from\_experience\_learning\_from\_demonstration\_preference\_and\_other\_agents.html][related_post_a260_demonstration]

[book_adami_1998]: https://doi.org/10.1007/978-1-4612-1650-6
[book_axelrod_1984]: https://basicbooks.com/titles/robert-axelrod/the-evolution-of-cooperation/9780465005642/
[book_back_fogel_michalewicz_1997]: https://www.taylorfrancis.com/books/edit/10.1201/9781420050387/handbook-evolutionary-computation-thomas-back-david-fogel-zbigniew-michalewicz
[book_beyer_2001_es_theory]: https://doi.org/10.1007/978-3-662-04378-3
[book_boyd_richerson_1985]: https://press.uchicago.edu/ucp/books/book/chicago/C/bo5972728.html
[book_carroll_2005]: https://wwnorton.com/books/9780393327793
[book_cavalli_sforza_feldman_1981]: https://press.princeton.edu/books/paperback/9780691082837/cultural-transmission-and-evolution
[book_darwin_1859]: https://darwin-online.org.uk/content/frameset?itemID=F373&viewtype=text&pageseq=1
[book_dawkins_1976]: https://global.oup.com/academic/product/the-selfish-gene-9780198788607
[book_fisher_1930]: https://global.oup.com/academic/product/the-genetical-theory-of-natural-selection-9780198504405
[book_goldberg_1989]: https://dl.acm.org/doi/book/10.5555/534133
[book_haldane_1932]: https://press.princeton.edu/books/paperback/9780691024424/the-causes-of-evolution
[book_henrich_2016]: https://press.princeton.edu/books/paperback/9780691178431/the-secret-of-our-success
[book_holland_1975]: https://mitpress.mit.edu/9780262581110/adaptation-in-natural-and-artificial-systems/
[book_kauffman_1993]: https://global.oup.com/academic/product/the-origins-of-order-9780195079517
[book_koza_1992]: https://mitpress.mit.edu/9780262111706/genetic-programming/
[book_larranaga_lozano_2002]: https://doi.org/10.1007/978-1-4615-1539-5
[book_maynard_smith_szathmary_1995]: https://global.oup.com/academic/product/the-major-transitions-in-evolution-9780198502944
[book_nowak_2006]: https://www.hup.harvard.edu/books/9780674023383
[book_sutton_barto_2018]: http://incompleteideas.net/book/the-book-2nd.html
[book_tomasello_1999]: https://www.hup.harvard.edu/books/9780674005822
[book_von_neumann_1966]: https://cba.mit.edu/events/03.11.ASE/docs/VonNeumann.pdf
[book_waddington_1957]: https://www.taylorfrancis.com/books/mono/10.4324/9781315766744/strategy-genes-waddington
[book_wagner_2005]: https://press.princeton.edu/books/paperback/9780691134079/robustness-and-evolvability-in-living-systems
[ref_berkeley_cs285]: https://rail.eecs.berkeley.edu/deeprlcourse/
[ref_deepmind_ucl_rl]: https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021
[ref_openai_spinning_up]: https://spinningup.openai.com/
[ref_silver_rl_course]: https://www.davidsilver.uk/teaching/
[ref_stanford_cs234]: https://web.stanford.edu/class/cs234/
[related_post_a250_framing]: {% post_url 2025-12-18-machines_that_learn_from_experience_framing %}
[related_post_a251_bandits]: {% post_url 2025-12-19-machines_that_learn_from_experience_bandits_and_online_learning %}
[related_post_a252_rl_foundations]: {% post_url 2025-12-20-machines_that_learn_from_experience_reinforcement_learning_foundations %}
[related_post_a253_deep_rl]: {% post_url 2025-12-21-machines_that_learn_from_experience_deep_reinforcement_learning %}
[related_post_a254_exploration]: {% post_url 2025-12-22-machines_that_learn_from_experience_exploration_intrinsic_motivation_and_curiosity %}
[related_post_a255_hierarchical]: {% post_url 2025-12-23-machines_that_learn_from_experience_hierarchical_reinforcement_learning %}
[related_post_a256_world_models]: {% post_url 2025-12-24-machines_that_learn_from_experience_world_models_and_predictive_model_based_adaptation %}
[related_post_a257_offline]: {% post_url 2025-12-25-machines_that_learn_from_experience_offline_and_batch_reinforcement_learning %}
[related_post_a258_meta_learning]: {% post_url 2025-12-26-machines_that_learn_from_experience_meta_learning_and_online_adaptation %}
[related_post_a259_continual]: {% post_url 2025-12-27-machines_that_learn_from_experience_continual_and_lifelong_learning %}
[related_post_a260_demonstration]: {% post_url 2025-12-28-machines_that_learn_from_experience_learning_from_demonstration_preference_and_other_agents %}
[research_ackley_littman_1991]: https://direct.mit.edu/isal/proceedings-abstract/alife/487/99257
[research_baldwin_1896]: https://doi.org/10.1086/276408
[research_bauer_et_al_2023_ada_a261]: https://doi.org/10.48550/arxiv.2301.07608
[research_bedau_1998_four_questions]: https://direct.mit.edu/artl/article-abstract/4/1/125/2321
[research_bentley_kumar_1999]: https://dl.acm.org/doi/10.5555/2933923.2933989
[research_beyer_schwefel_2002]: https://doi.org/10.1023/a:1015059928466
[research_bongard_2004_coevolutionary]: https://www.pnas.org/doi/10.1073/pnas.0405301102
[research_bongard_zykov_lipson_2006]: https://doi.org/10.1126/science.1133687
[research_bradley_et_al_2024_openelm]: https://scholar.google.com/scholar?q=OpenELM+Bradley+2024
[research_cai_zhu_han_2019_proxyless]: https://openreview.net/forum?id=HylVB3AqYm
[research_chalumeau_et_al_2024_qd_rl]: https://scholar.google.com/scholar?q=QD-RL+Chalumeau+2024
[research_chatzilygeroudis_et_al_2021_qd_overview]: https://scholar.google.com/scholar?q=QD+Overview+Chatzilygeroudis+2021
[research_chen_et_al_2024_evoprompt]: https://doi.org/10.48550/arxiv.2309.08532
[research_cheney_et_al_2013]: https://doi.org/10.1145/2463372.2463404
[research_cheney_et_al_2013_a261]: https://doi.org/10.1145/2463372.2463404
[research_cliff_miller_1996]: https://link.springer.com/chapter/10.1007/3-540-61314-3_10
[research_clune_2019_aigas]: https://doi.org/10.48550/arxiv.1905.10985
[research_colas_sigaud_oudeyer_2018_geppg]: https://proceedings.mlr.press/v80/colas18a.html
[research_conti_et_al_2018_nses]: https://papers.nips.cc/paper/2018/hash/b1301141feffabac455e1f90a7de2054-Abstract.html
[research_cranmer_et_al_2020]: https://papers.nips.cc/paper/2020/hash/c9f2f917078bd2db12f23c3b413d9cba-Abstract.html
[research_cully_demiris_2018_qd_review]: https://ieeexplore.ieee.org/document/8237407
[research_cully_et_al_2015_robots]: https://doi.org/10.1038/nature14422
[research_deb_et_al_2002_nsga2]: https://ieeexplore.ieee.org/document/996017
[research_deb_jain_2013_nsga3]: https://ieeexplore.ieee.org/document/6600851
[research_dejong_1975]: https://deepblue.lib.umich.edu/handle/2027.42/4507
[research_dennis_et_al_2020_paired_a261]: https://papers.nips.cc/paper/2020/hash/985e9a46e10005356bbaf194249f6856-Abstract.html
[research_doerr_et_al_2013_runtime]: https://link.springer.com/article/10.1007/s00453-011-9585-3
[research_doncieux_et_al_2019_qd_theory]: https://link.springer.com/article/10.1007/s10710-019-09343-3
[research_dong_yang_2020_nasbench201]: https://openreview.net/forum?id=HJxyZkBKDr
[research_dorigo_maniezzo_colorni_1996]: https://doi.org/10.1109/3477.484436
[research_droste_jansen_wegener_2002]: https://link.springer.com/article/10.1023/A:1013951316365
[research_elsken_metzen_hutter_2019_nas_survey]: https://jmlr.org/papers/v20/18-598.html
[research_faldor_cully_2024_qd_survey]: https://scholar.google.com/scholar?q=QD+Survey+Faldor+Cully+2024
[research_faldor_et_al_2024_omni_epic]: https://doi.org/10.48550/arxiv.2405.15568
[research_fernando_et_al_2023_promptbreeder]: https://doi.org/10.48550/arxiv.2309.16797
[research_ficici_pollack_2001_pareto]: https://direct.mit.edu/evco/article-abstract/9/2/183/1099
[research_floreano_durr_mattiussi_2008]: https://doi.org/10.1007/s12065-007-0002-4
[research_fogel_owens_walsh_1966]: https://dl.acm.org/doi/book/10.5555/1096080
[research_fontaine_et_al_2020_cma_me_orig]: https://doi.org/10.1145/3377930.3390232
[research_fontaine_nikolaidis_2021_cmame]: https://scholar.google.com/scholar?q=CMA-ME+Fontaine+Nikolaidis+2021
[research_fontaine_nikolaidis_2021_dqd]: https://papers.nips.cc/paper/2021/hash/532b7cbe070a3579f424988a040752f2-Abstract.html
[research_grillotti_cully_2022]: https://scholar.google.com/scholar?q=Modular+QD+Grillotti+Cully+2022
[research_hansen_2016_cmaes_tutorial]: https://doi.org/10.48550/arxiv.1604.00772
[research_hansen_et_al_2009_bbob]: https://coco.gforge.inria.fr/doku.php?id=bbob-2009
[research_hansen_ostermeier_2001_cmaes]: https://direct.mit.edu/evco/article-abstract/9/2/159/1090
[research_hinton_nowlan_1987]: https://www.cs.toronto.edu/~hinton/absps/baldwin.pdf
[research_hornby_pollack_2001]: https://scholar.google.com/scholar?q=L-System+Hornby+Pollack+2001
[research_igel_2003]: https://ieeexplore.ieee.org/document/1299617
[research_igel_hansen_roth_2007_moes]: https://direct.mit.edu/evco/article-abstract/15/1/1/1230
[research_kamienny_et_al_2022]: https://doi.org/10.52202/068431-0746
[research_kelly_bowling_2020_gsac]: https://scholar.google.com/scholar?q=GSAC+Kelly+Bowling+2020
[research_kennedy_eberhart_1995_pso]: https://ieeexplore.ieee.org/document/488968
[research_khadka_tumer_2018_erl]: https://papers.nips.cc/paper/2018/hash/85fc37b18c57097425b52fc7afbb6969-Abstract.html
[research_kimura_1968_neutral]: https://doi.org/10.1038/217624a0
[research_kirby_cornish_smith_2015_a261]: https://scholar.google.com/scholar?q=Iterated+Kirby+Cornish+Smith+2015
[research_kirkpatrick_gelatt_vecchi_1983]: https://doi.org/10.1126/science.220.4598.671
[research_kirschner_gerhart_1998]: https://doi.org/10.1073/pnas.95.15.8420
[research_kriegman_et_al_2020]: https://doi.org/10.1073/pnas.1910837117
[research_lacava_et_al_2021]: https://doi.org/10.48550/arxiv.2107.14351
[research_langton_1986_alife]: https://www.sciencedirect.com/science/article/abs/pii/0167278986902374
[research_lehman_et_al_2023_elm]: https://doi.org/10.48550/arxiv.2206.08896
[research_lehman_stanley_2011_abandoning]: https://direct.mit.edu/evco/article-abstract/19/2/189/1365
[research_lehman_stanley_2011_novelty]: https://direct.mit.edu/evco/article-abstract/19/2/189/1365
[research_lenski_et_al_2003]: https://doi.org/10.1038/nature01568
[research_liu_simonyan_yang_2019_darts]: https://openreview.net/forum?id=S1eYHoC5FX
[research_lohn_hornby_linden_2006]: https://ntrs.nasa.gov/citations/20060005022
[research_ma_et_al_2023_eureka]: https://doi.org/10.48550/arxiv.2310.12931
[research_meyerson_et_al_2023_lmx]: https://doi.org/10.48550/arxiv.2302.12170
[research_miconi_2016_biologically_plausible]: https://doi.org/10.7554/elife.20899
[research_miikkulainen_et_al_2019]: https://www.sciencedirect.com/science/article/pii/B9780128159804000151
[research_miller_2004_embryology]: https://scholar.google.com/scholar?q=Embryology+Miller+2004
[research_mouret_clune_2015_mapelites]: https://doi.org/10.48550/arxiv.1504.04909
[research_muhlenbein_1997_eda]: https://direct.mit.edu/evco/article-abstract/5/3/303/1176
[research_nigam_et_al_2021]: https://pubs.rsc.org/en/content/articlehtml/2021/sc/d1sc00231g
[research_nilsson_cully_2021_qdgym]: https://scholar.google.com/scholar?q=QDgym+Nilsson+Cully+2021
[research_nowak_may_1992]: https://doi.org/10.1038/359826a0
[research_nowak_tarnita_antal_2010]: https://doi.org/10.1098/rstb.2009.0215
[research_ofria_wilke_2004_avida]: https://doi.org/10.1162/106454604773563612
[research_openendedlearningteam_2021]: https://scholar.google.com/scholar?q=Open-Ended+Learning+Team+2021
[research_pelikan_goldberg_cantupaz_2000_boa]: https://direct.mit.edu/evco/article-abstract/8/3/311/1113
[research_petersen_et_al_2021_dsr]: https://openreview.net/forum?id=m5Qsh0kBQG
[research_pham_et_al_2018_enas]: https://proceedings.mlr.press/v80/pham18a.html
[research_popovici_et_al_2012_coevolution]: https://doi.org/10.1007/978-3-540-92910-9_31
[research_portelas_et_al_2020_acl_a261]: https://doi.org/10.48550/arxiv.2003.04664
[research_potter_dejong_2000]: https://direct.mit.edu/evco/article-abstract/8/1/1/819
[research_pourchot_sigaud_2019_cemrl]: https://openreview.net/forum?id=BkeU5j0ctQ
[research_price_1970]: https://www.nature.com/articles/227520a0
[research_pugh_soros_stanley_2016_qd]: https://doi.org/10.3389/frobt.2016.00040
[research_ray_1991_tierra]: https://direct.mit.edu/isal/proceedings-abstract/alife/470/99202
[research_real_et_al_2017_large_scale]: https://proceedings.mlr.press/v70/real17a.html
[research_real_et_al_2019_amoebanet]: https://doi.org/10.1609/aaai.v33i01.33014780
[research_real_et_al_2020_automlzero]: https://proceedings.mlr.press/v119/real20a.html
[research_rechenberg_1973]: https://scholar.google.com/scholar?q=rechenberg+1973+evolutionsstrategie
[research_risi_stanley_2012_eshyperneat]: https://direct.mit.edu/artl/article-abstract/18/4/331/2769
[research_romera_paredes_et_al_2024_funsearch]: https://doi.org/10.1038/s41586-023-06924-6
[research_rosin_belew_1997]: https://direct.mit.edu/evco/article-abstract/5/1/1/847
[research_rudolph_1997]: https://link.springer.com/article/10.1023/A:1018503430137
[research_salimans_et_al_2017_es]: https://doi.org/10.48550/arxiv.1703.03864
[research_sayama_2009]: https://direct.mit.edu/artl/article-abstract/16/1/71/2492
[research_schmidt_lipson_2009]: https://doi.org/10.1126/science.1165893
[research_schmidt_lipson_2009_a261]: https://doi.org/10.1126/science.1165893
[research_schwefel_1977]: https://scholar.google.com/scholar?q=schwefel+1977+numerische+optimierung
[research_sigaud_2023_erl_survey]: https://scholar.google.com/scholar?q=ERL+Survey+Sigaud+2023
[research_sims_1994_blocks]: https://doi.org/10.1145/192161.192167
[research_soros_stanley_2014_mcc]: https://direct.mit.edu/isal/proceedings-abstract/alife2014/26/638
[research_standish_2003_open_ended]: https://doi.org/10.1142/s1469026803000914
[research_stanley_2007_cppn]: https://doi.org/10.1007/s10710-007-9028-8
[research_stanley_dambrosio_gauci_2009_hyperneat]: https://direct.mit.edu/artl/article-abstract/15/2/185/2578
[research_stanley_et_al_2019_neuroevolution]: https://doi.org/10.1038/s42256-018-0006-z
[research_stanley_miikkulainen_2002_neat]: https://direct.mit.edu/evco/article-abstract/10/2/99/1123
[research_storn_price_1997_de]: https://doi.org/10.1023/a:1008202821328
[research_such_et_al_2017_deep_neuroevolution]: https://doi.org/10.48550/arxiv.1712.06567
[research_tan_le_2019_efficientnet]: https://proceedings.mlr.press/v97/tan19a.html
[research_taylor_et_al_2016_oee]: https://direct.mit.edu/artl/article-abstract/22/3/408/2717
[research_thompson_1997_evolvable_hardware]: https://link.springer.com/chapter/10.1007/BFb0041008
[research_vassiliades_et_al_2018_cvt]: https://ieeexplore.ieee.org/document/8000704
[research_wang_et_al_2019_poet_a261]: https://doi.org/10.48550/arxiv.1901.01753
[research_wang_et_al_2020_epoet]: https://proceedings.mlr.press/v119/wang20l.html
[research_waser_adami_2018]: https://scholar.google.com/scholar?q=Transitions+Waser+Adami+2018
[research_watson_pollack_2001]: https://direct.mit.edu/evco/article-abstract/9/2/213/1097
[research_whitley_1994]: https://doi.org/10.1007/bf00175354
[research_wierstra_et_al_2014_nes]: https://jmlr.org/papers/v15/wierstra14a.html
[research_wolpert_macready_1997_nfl]: https://ieeexplore.ieee.org/document/585893
[research_wright_1932_landscape]: https://www.esp.org/foundations/genetics/classical/holdings/w/wright-1932.pdf
[research_wu_et_al_2019_fbnet]: https://doi.org/10.1109/cvpr.2019.01099
[research_xie_et_al_2019_snas]: https://openreview.net/forum?id=rylqooRqK7
[research_yao_1999]: https://ieeexplore.ieee.org/document/784219
[research_ying_et_al_2019_nasbench]: https://proceedings.mlr.press/v97/ying19a.html
[research_zhang_li_2007_moead]: https://ieeexplore.ieee.org/document/4358754
[research_zitzler_laumanns_thiele_2001_spea2]: https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=10.1.1.28.7571
[research_zoph_le_2017_nas]: https://openreview.net/forum?id=r1Ue8Hcxg
