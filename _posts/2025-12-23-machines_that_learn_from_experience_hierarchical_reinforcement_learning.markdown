---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: Hierarchical Reinforcement Learning"
date:   2025-12-23 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 6
---

<!-- A255 -->
<script>console.log("A255");</script>

Hierarchical reinforcement learning treats the problem of learning at multiple timescales through structured temporal abstraction. A hierarchical agent decomposes long-horizon control into a policy over subroutines that themselves execute across many primitive time steps, addressing the credit-assignment difficulty and sample-complexity scaling of flat reinforcement learning on problems with long horizons or structured task decompositions. This article surveys the science and theory of hierarchical reinforcement learning as it stands in the mid 2020s, covering the semi-Markov decision process formalism that underlies temporally-extended actions, the options framework of Sutton Precup and Singh that constitutes the canonical modern treatment, the MAXQ hierarchical value function decomposition of Dietterich, the feudal reinforcement learning framework of Dayan and Hinton, the deep-learning extensions including FeUdal Networks and the Option-Critic architecture, goal-conditioned and sub-goal-based hierarchies, algorithmic option discovery, and the neuroscience connections to the prefrontal-striatal circuits implicated in hierarchical control in biological brains. Articles two through five treated the pre-Markov and single-timescale foundations, articles seven treats model-based planning that connects to hierarchical planning, article nine treats meta-learning as an alternative approach to fast adaptation at long horizons.

## Temporal Abstraction and Its Motivations

Long-horizon reinforcement learning presents structural difficulties that motivate temporal abstraction. The effective discount factor for credit assignment across $k$ steps is $\gamma^k$, which becomes vanishingly small for $k$ on the order of tens or hundreds of primitive steps. Value function estimates for states many steps distant from the primary reward source are consequently noisy and difficult to learn. Exploration through primitive-action random walks concentrates the visitation distribution near the starting state, requiring exponentially-many samples to reach distant states.

Hierarchical control addresses these difficulties by introducing temporally-extended actions that operate at longer timescales. A high-level policy selects among these temporally-extended actions, each of which executes for many primitive steps before returning control to the high-level policy. The effective time-step for the high-level policy is many primitive steps, and credit assignment at the high level involves shorter effective horizons.

Formally, consider a task requiring $H$ primitive-action steps to complete. A flat agent must propagate value signal through $H$ Bellman updates, with effective discount factor

$$\gamma^H_{\text{flat}} = \gamma^H$$

A two-level hierarchical agent with sub-policies each of length $k$ propagates value at the high level through only $H/k$ steps, with effective discount factor per high-level step

$$\gamma_{\text{high}} = \gamma^k$$

and total high-level effective discount

$$\gamma^{H/k}_{\text{high}} = (\gamma^k)^{H/k} = \gamma^H$$

Although the total discount at task-completion horizon is unchanged, the number of Bellman updates required to propagate value across that horizon reduces by the temporal compression ratio $k$, and each high-level Bellman update carries less variance in the value target because it aggregates reward over $k$ primitive-action steps.

Hierarchical decomposition also supports skill transfer across tasks that share sub-structure. A locomotion sub-policy learned to navigate one maze may transfer to any maze of similar geometry, a manipulation primitive learned for one grasping task may transfer to related manipulation tasks. The transferability of hierarchical components has proved a substantial motivation for the field.

Finally, hierarchical control aligns with the observed structure of biological motor control and cognitive planning, in which behavioral sequences are organized into nested phrases with clear onsets, terminations, and hierarchical composition. The neuroscience connections treated later in this article provide the empirical grounding for this alignment.

## Historical Development

The hierarchical reinforcement learning research program has multiple parallel origins. The behavior-based robotics community treated hierarchical behavior organization through subsumption architectures [Brooks 1986][research_brooks_1986] that composed reactive control modules into layered behavior systems. The cognitive-science community developed hierarchical task-network planning frameworks that formalized the decomposition of complex actions into subtask sequences.

Within reinforcement learning proper, [Dayan and Hinton 1993][research_dayan_hinton_1993] feudal reinforcement learning provided the first systematic treatment of hierarchical reinforcement learning as a distinct algorithmic framework. The manager-worker structure with information hiding between levels became a template for later work.

[Parr and Russell 1998][research_parr_russell_1998] hierarchical abstract machines (HAMs) formalized hierarchical reinforcement learning through the machine-hierarchy formalism, providing convergence guarantees analogous to the classical Q-learning results but for the induced semi-Markov decision process.

The options framework of [Sutton Precup and Singh 1999][research_sutton_precup_singh_1999] became the canonical modern formalization. The paper unified the previous frameworks under the shared semi-Markov decision process foundation and established the intra-option learning algorithms that permit efficient policy evaluation and control at both levels of the hierarchy. [Precup and Sutton 1998][research_precup_sutton_1998] earlier introduced multi-time models for temporally abstract planning, providing the precursor formalization of option-level dynamics. [Precup 2000][book_precup_thesis_2000] doctoral thesis provided the systematic development, and [Barto and Mahadevan 2003][research_barto_mahadevan_2003] survey consolidated the field's state at the turn of the millennium.

[Dietterich 2000][research_dietterich_2000] MAXQ decomposition provided a distinct hierarchical value function factorization that admits separate optimality analyses at each level of the hierarchy. MAXQ trades some of the flexibility of the options framework for stronger structural constraints that enable cleaner theoretical treatment.

The deep reinforcement learning wave of the 2010s brought new algorithmic developments. [Kulkarni et al 2016][research_kulkarni_et_al_2016] hierarchical DQN combined deep Q-learning with sub-goal-based hierarchy. [Bacon Harb and Precup 2017][research_bacon_harb_precup_2017] Option-Critic Architecture extended the actor-critic framework to the options setting. [Vezhnevets et al 2017][research_vezhnevets_et_al_2017] FeUdal Networks provided a deep-learning implementation of the feudal reinforcement learning framework. [Nachum Gu Lee Levine 2018][research_nachum_gu_lee_levine_2018] HIRO extended the framework to off-policy hierarchical reinforcement learning.

## Semi-Markov Decision Processes

The semi-Markov decision process (SMDP) formalism generalizes the Markov decision process to accommodate actions whose duration is variable. An SMDP is specified by a tuple

$$\mathcal{M}_{\text{SMDP}} = (\mathcal{S}, \mathcal{A}, P, R, F)$$

where $\mathcal{S}, \mathcal{A}$ are state and action spaces, $P(s' \mid s, a)$ is a transition kernel, $R(s, a)$ is a reward function, and $F(\tau \mid s, a)$ is a duration distribution specifying the number of time steps that action $a$ occupies starting from state $s$.

The SMDP Bellman equation replaces the single-step reward and discount with cumulative reward and discount over the action duration,

$$V^{\pi}(s) = \sum_a \pi(a \mid s) \left[R(s, a) + \sum_{s', \tau} F(\tau \mid s, a) P(s' \mid s, a, \tau) \gamma^\tau V^\pi(s')\right]$$

where $R(s, a)$ now denotes the expected discounted cumulative reward accumulated during action $a$ and $F(\tau \mid s, a)$ is the probability that action $a$ takes duration $\tau$. Concretely, if action $a$ initiated at state $s$ generates a sequence of primitive-action rewards $r_1, r_2, \ldots, r_\tau$, the cumulative reward is

$$R(s, a) = \mathbb{E}\!\left[\sum_{i=0}^{\tau-1} \gamma^i r_{i+1} \mid s, a\right]$$

The discount factor $\gamma^\tau$ reflects that reward received after $\tau$ primitive steps is discounted by $\gamma$ raised to $\tau$. The SMDP Bellman optimality equation for the action-value function is

$$Q^*(s, a) = R(s, a) + \sum_{s', \tau} F(\tau \mid s, a) P(s' \mid s, a, \tau) \gamma^\tau \max_{a'} Q^*(s', a')$$

Q-learning extends to the SMDP setting through an SMDP Q-learning update,

$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[r + \gamma^\tau \max_{a'} Q(s', a') - Q(s, a)\right]$$

where $r$ is the cumulative discounted reward and $\tau$ the duration of the action selected at $s$. The update reduces to standard Q-learning when $\tau = 1$ and provides the algorithmic foundation for the options and MAXQ frameworks treated below.

## The Options Framework

The options framework of Sutton Precup and Singh formalizes temporally-extended actions in the reinforcement learning setting. An option is a triple

$$o = (I_o, \pi_o, \beta_o)$$

where $I_o \subseteq \mathcal{S}$ is the initiation set specifying states from which the option can be invoked, $\pi_o : \mathcal{S} \to \Delta(\mathcal{A})$ is the intra-option policy specifying action selection while the option is executing, and $\beta_o : \mathcal{S} \to [0, 1]$ is the termination condition specifying the probability of terminating the option at each state.

Primitive actions can be modeled as one-step options with $I_o = \mathcal{S}$, $\pi_o$ deterministic, and $\beta_o = 1$ everywhere. This unification allows the options framework to treat primitive and temporally-extended actions uniformly under the same SMDP formalism.

A policy over options $\mu : \mathcal{S} \to \Delta(\mathcal{O})$ selects an option at each option-initiation state. The induced dynamics are semi-Markov. Option execution proceeds through primitive-action steps until the termination condition triggers, at which point the high-level policy selects a new option. Formally, upon selecting option $o$ at state $s_t$, primitive actions are drawn according to $a_i \sim \pi_o(\cdot \mid s_{t+i})$ for $i = 0, 1, \ldots$, and termination occurs at step $\tau$ with probability

$$P(\tau_o = k) = \prod_{i=0}^{k-1} (1 - \beta_o(s_{t+i})) \, \beta_o(s_{t+k})$$

corresponding to the option continuing through $k$ steps of non-termination followed by termination at step $k$.

The option value function

$$V^\mu(s) = \mathbb{E}\!\left[\sum_{k=0}^{\infty} \gamma^k r_{k+1} \mid s_0 = s, \mu\right]$$

satisfies the SMDP Bellman equation for the induced semi-Markov process. The option-Q function

$$Q^\mu(s, o) = \mathbb{E}\!\left[r(s, o) + \gamma^{\tau(s, o)} V^\mu(s') \mid s_0 = s, o_0 = o\right]$$

decomposes the option value as expected cumulative discounted reward $r(s, o)$ accumulated during option execution plus the discounted next-state value.

The options framework subsumes MAXQ, HAMs, and feudal reinforcement learning as special cases through appropriate specialization of initiation sets, intra-option policies, and termination conditions. This unifying property has made the options framework the standard formalism for modern hierarchical reinforcement learning theory.

## Options Bellman Equations and Intra-Option Learning

The intra-option learning framework permits updates to the option value function based on individual primitive-step transitions rather than requiring the option to terminate before update. The intra-option Q-update is

$$Q(s, o) \leftarrow Q(s, o) + \alpha \left[r + \gamma U(s', o) - Q(s, o)\right]$$

where

$$U(s', o) = (1 - \beta_o(s')) Q(s', o) + \beta_o(s') \max_{o'} Q(s', o')$$

is the option-conditional value that continues the option with probability $1 - \beta_o(s')$ and terminates and selects the greedy next option with probability $\beta_o(s')$. The mechanism enables efficient credit assignment within options while preserving the semi-Markov structure at the high level.

Intra-option policy improvement uses the standard policy-improvement operations within each option, treating the option's intra-policy as an independent policy over primitive actions with augmented reward signal that includes option-conditional continuation value.

The Bellman optimality equation for options is

$$Q^*(s, o) = \sum_a \pi_o(a \mid s) \left[R(s, a) + \gamma \sum_{s'} P(s' \mid s, a) U^*(s', o)\right]$$

with

$$U^*(s', o) = (1 - \beta_o(s')) Q^*(s', o) + \beta_o(s') V^*(s'), \quad V^*(s') = \max_{o'} Q^*(s', o')$$

The recursive structure enables value iteration and other dynamic programming methods to compute $Q^*$ and thereby the optimal policy over options.

The option advantage function

$$A^\mu_\Omega(s, o) = Q^\mu(s, o) - V^\mu(s)$$

quantifies the value of committing to option $o$ over the current policy-average option choice. The termination advantage

$$A^\mu_\beta(s, o) = Q^\mu(s, o) - V^\mu(s)$$

quantifies the value of continuing option $o$ over terminating and selecting a fresh option, and enters directly into the termination-gradient theorem treated later. The sign of the termination advantage determines whether the current option should extend or end at each state.

## MAXQ Decomposition

The MAXQ hierarchical value function decomposition of Dietterich takes a distinctive approach to hierarchical reinforcement learning. Rather than allowing arbitrary temporally-extended actions, MAXQ decomposes the value function itself into contributions from a task hierarchy.

A MAXQ task hierarchy consists of subtasks organized in a directed acyclic graph. Each subtask $M_i$ is defined by three components. These are the set of primitive or composite actions available within the subtask, a termination predicate specifying when the subtask is complete, and a pseudo-reward function specifying the local reward within the subtask.

The MAXQ value function decomposition writes the value of a state under a subtask as

$$V^\pi(i, s) = V^{\pi_i}(a_i(s), s) + C^\pi(i, s, a_i(s))$$

where $\pi_i$ is the current policy at subtask $i$, $a_i(s)$ is the action or child subtask selected at state $s$, $V^{\pi_i}(a_i(s), s)$ is the value of the selected child, and $C^\pi(i, s, a_i(s))$ is the completion function

$$C^\pi(i, s, a) = \mathbb{E}\!\left[\gamma^{\tau_a} V^\pi(i, s') \mid \text{child } a \text{ terminates at } s'\right]$$

representing the expected discounted reward from completing subtask $i$ after the child terminates. The recursive Bellman equation for the MAXQ hierarchy is

$$V^\pi(i, s) = \sum_a \pi_i(a \mid s) \left[V^{\pi_i}(a, s) + C^\pi(i, s, a)\right]$$

The decomposition provides several advantages. Subtask values can be learned locally within each subtask, permitting sample efficiency gains through reuse of subtask policies across contexts. The completion function factors out the parent-task-portion of value from the child-task-portion.

The MAXQ-Q learning algorithm updates each completion function through a TD update

$$C(i, s, a) \leftarrow C(i, s, a) + \alpha \left[\gamma^{\tau_a} V(i, s') - C(i, s, a)\right]$$

where $s'$ is the state at child termination and $\tau_a$ is the duration of the child. The mechanism learns completion functions locally within each subtask context while composing them hierarchically for evaluation.

MAXQ optimality is characterized by two notions. Recursive optimality corresponds to each subtask being optimal under the assumption that its child subtasks are optimal. Hierarchical optimality corresponds to global optimality of the induced policy. The two coincide only under restrictive conditions, and MAXQ typically achieves recursive but not hierarchical optimality without additional constraints.

MAXQ-Q of Dietterich provides the sample-based algorithm that learns the completion functions online through TD-style updates. Convergence guarantees hold under standard conditions on step size and infinite visitation of subtask contexts.

## Feudal Reinforcement Learning and Hierarchical Abstract Machines

Feudal reinforcement learning of [Dayan and Hinton 1993][research_dayan_hinton_1993] structures the hierarchy as a sequence of manager-worker relationships. Each level receives rewards only from its immediate supervisor, and each level sends actions only to its immediate subordinate. Information is hidden across levels. Workers do not see the top-level reward and managers do not see primitive actions.

The feudal architecture provides several conceptual advantages. Reward-hiding at intermediate levels avoids reward-signal dilution across long horizons. Action-hiding at intermediate levels supports abstract policy formulation independent of implementation-level details. The manager-worker delegation naturally supports skill transfer and modular composition.

Hierarchical Abstract Machines of [Parr and Russell 1998][research_parr_russell_1998] formalize hierarchical reinforcement learning through finite-state machines that constrain the action space at each state. A HAM consists of a hierarchy of machines with state types for choice states (where reinforcement learning selects an action), call states (where control transfers to a called machine), action states (where a primitive action is executed), and stop states (where control returns to the calling machine).

The HAM-induced MDP has a state space consisting of pairs $(s, m)$ where $s$ is the environment state and $m$ is the current machine state,

$$\mathcal{S}_{\text{HAM}} = \mathcal{S} \times \mathcal{M}$$

with transitions among machine states determined by the HAM structure and transitions among environment states determined by the underlying MDP. Q-learning within the induced MDP updates state-machine-conditioned Q-values

$$Q((s, m), a) \leftarrow Q((s, m), a) + \alpha \left[r + \gamma^\tau \max_{a'} Q((s', m'), a') - Q((s, m), a)\right]$$

for choice-state actions $a$ over the accumulated reward $r$ and duration $\tau$ until the next choice state. HAMQ, the HAM Q-learning algorithm, converges to the HAM-optimal policy under standard conditions on step size and infinite visitation of choice-state contexts.

The choice-versus-constraint formulation of HAMs contrasts with the free-form option framework. HAMs restrict the class of policies to those consistent with the hierarchy but provide clean theoretical guarantees within that class.

## Deep Hierarchical Reinforcement Learning

The deep reinforcement learning wave of the 2010s produced neural implementations of the classical hierarchical frameworks. Hierarchical DQN of [Kulkarni Narasimhan Saeedi Tenenbaum 2016][research_kulkarni_et_al_2016] combined deep Q-learning with a two-level hierarchy in which a high-level meta-controller selects sub-goals from a discrete set and a low-level controller learns to reach the selected sub-goal. The meta-controller Q-network is updated on transitions between sub-goal completions,

$$Q_{\text{meta}}(s, g) \leftarrow Q_{\text{meta}}(s, g) + \alpha \left[R_g + \gamma \max_{g'} Q_{\text{meta}}(s', g') - Q_{\text{meta}}(s, g)\right]$$

where $R_g$ is the cumulative extrinsic reward received while pursuing sub-goal $g$ and $s'$ is the state at sub-goal termination. The low-level controller uses an intrinsic reward signal for reaching the sub-goal,

$$r^{\text{intrinsic}}_t = \mathbb{1}\!\left\{\phi(s_t) = g\right\}$$

for a goal-check function $\phi$. The mechanism achieved substantial improvements on Montezuma's Revenge where flat DQN made essentially no progress.

FeUdal Networks of [Vezhnevets et al 2017][research_vezhnevets_et_al_2017] extended the feudal framework to deep neural networks with a manager operating at a coarser timescale than the worker. The manager produces a directional sub-goal in a latent state space,

$$g_t = f_{\text{manager}}(s_t; \theta_M) \in \mathbb{R}^d$$

updated every $c$ primitive steps and pooled across neighboring updates. The worker receives an intrinsic reward for producing state changes aligned with the manager's directional sub-goal,

$$r_t^{\text{FuN}} = \frac{1}{c} \sum_{i=1}^{c} \cos\!\left(s_{t+i} - s_t, g_{t-i}\right)$$

which is the cosine similarity between the actual state-change direction and the manager-specified target direction. The mechanism decouples the manager's goal specification from the worker's action selection through the shared latent space, addressing the credit-assignment difficulty at scale.

FeUdal Networks achieved substantial gains on Atari games including Montezuma's Revenge, Frostbite, Ms. Pac-Man, and Enduro, demonstrating that hierarchical decomposition combined with deep function approximation could handle the long-horizon exploration difficulties that had blocked flat deep RL agents.

## The Option-Critic Architecture

The Option-Critic Architecture of [Bacon Harb and Precup 2017][research_bacon_harb_precup_2017] extends the actor-critic framework to the options setting, providing an end-to-end differentiable learning algorithm for options. The framework learns the intra-option policies, termination conditions, and policy over options jointly through gradient descent on the expected return.

The option-policy gradient theorem gives the gradient of the expected return with respect to the intra-option policy parameters $\theta$,

$$\nabla_\theta J = \mathbb{E}_{s, o}\!\left[Q_U(s, o, a) \nabla_\theta \log \pi_{o, \theta}(a \mid s)\right]$$

where $Q_U(s, o, a) = \mathbb{E}[r + \gamma U(s', o) \mid s, o, a]$ is the option-conditioned action-value at the primitive-action level.

The termination gradient theorem gives the gradient with respect to the termination condition parameters $\vartheta$,

$$\nabla_\vartheta J = -\mathbb{E}\!\left[\nabla_\vartheta \beta_{o, \vartheta}(s') \left(Q^\mu(s', o) - V^\mu(s')\right)\right]$$

which is proportional to the advantage of continuing the option over terminating and switching to the best next option. Options that provide substantial advantage over termination are encouraged to persist, options that provide little advantage over termination are encouraged to end.

The Option-Critic framework enables option discovery in the sense that options emerge from the joint optimization of the actor-critic objective. However, the emergent options often exhibit trivial behavior in which each option effectively terminates after every primitive step, degenerating to flat policy optimization. Additional regularization terms or termination-cost penalties are required to encourage non-trivial temporal abstraction.

Extensions of Option-Critic include Interest-Option-Critic that adds learned interest functions to complement the termination conditions, and Attention Option-Critic that uses attention mechanisms to condition option selection on relevant state features.

## HIRO and Off-Policy Hierarchical Learning

HIRO of [Nachum Gu Lee Levine 2018][research_nachum_gu_lee_levine_2018] provides an off-policy hierarchical reinforcement learning algorithm for continuous control settings. A high-level policy $\mu_{\text{high}}(g \mid s)$ produces state-conditioned sub-goals in the observation space at fixed intervals of $c$ primitive-action steps, and a low-level policy $\pi_{\text{low}}(a \mid s, g)$ learns to reach the sub-goals through goal-conditioned reinforcement learning with intrinsic reward

$$r^{\text{low}}_t = -\| s_{t+1} - (s_t + g_t) \|_2$$

for goal-directed displacement $g_t$, encouraging state changes aligned with the specified sub-goal.

The critical technical challenge in off-policy hierarchical learning is that the low-level policy changes during training, invalidating past trajectories collected under earlier low-level policies. HIRO addresses this through goal relabeling. At training time, high-level transitions are relabeled with the sub-goals that would have been optimal under the current low-level policy,

$$\tilde{g}_t = \arg\max_g P(a_{t:t+c-1} \mid s_{t:t+c-1}, g, \pi_{\text{low}})$$

which is approximated by searching over a small set of candidate goals around the actually-executed goal and the state transitions that occurred.

HIRO demonstrated state-of-the-art performance on hierarchical continuous control benchmarks including ant maze navigation and simulated manipulation tasks, providing evidence that sample-efficient hierarchical learning is feasible with off-policy methods.

Related methods include HAC (Hierarchical Actor-Critic) of [Levy et al 2018][research_levy_et_al_2018] which uses subgoal testing to handle the moving-target problem in hierarchical off-policy learning, and Data-Efficient Hierarchical RL of [Nachum et al 2019][research_nachum_et_al_2019] which further refines the sub-goal representation using learned representations.

## Goal-Conditioned Hierarchies

Goal-conditioned reinforcement learning treated in article five naturally extends to hierarchical settings. A high-level policy proposes goals from a goal space $\mathcal{G}$ and a low-level goal-conditioned policy attempts to reach those goals. The universal value function of [Schaul Horgan Gregor Silver 2015][research_schaul_horgan_gregor_silver_2015_hrl] provides the foundational value function representation

$$V(s, g) = \mathbb{E}\!\left[\sum_t \gamma^t r(s_t, g) \mid s_0 = s, \pi(\cdot \mid \cdot, g)\right]$$

that generalizes across goals in a shared parameter space.

Hierarchical goal-conditioned methods differ in how they define the goal space and the high-level policy. Options-of-Interest of [Barreto et al 2019][research_barreto_et_al_2019] connects options to successor features, treating options as being defined by successor-feature-based termination criteria. HRL with Latent Sub-Goals of [Nachum et al 2019][research_nachum_et_al_2019] learns a latent goal representation that compresses the high-dimensional state space to a lower-dimensional goal manifold.

Sub-goal generation approaches use various methods to propose useful sub-goals. Landmark-based methods identify frequently-visited states as candidate sub-goals. Learned goal generators produce sub-goals through generative models trained on visited states. Adversarial goal generation trains a generator to produce goals of appropriate difficulty for the current policy, connecting to the curriculum generation methods of article five.

## Skills as Latent Codes and Continuous Skill Spaces

The latent-code formulation of skills treats a hierarchical policy as a two-level composition in which a high-level policy selects a skill embedding $z \in \mathcal{Z}$ from a continuous skill space and a low-level latent-conditioned policy

$$\pi_\theta(a \mid s, z)$$

produces different behaviors for different values of the code. Continuous latent spaces support interpolation between skills, distance-based skill similarity, and gradient-based composition, providing a natural interface for skill manipulation that discrete option sets do not.

Encoder-decoder skill representations learn to compress action sequences into latent codes and to decode from latent codes back to action sequences. The framework provides an inference mechanism to identify the skill executing during a demonstration and a generation mechanism to produce skill-consistent actions during control. Neural Probabilistic Motor Primitives of [Merel Hasenclever Galashov Ahuja Tassa Wayne Tirumala Wulfmeier Heess 2019][research_merel_et_al_2019] applied the framework to complex humanoid motion, showing that a substantial repertoire of motor skills can be compressed into a low-dimensional latent code with high fidelity and then reproduced by a latent-conditioned decoder.

OPAL of Ajay et al 2021 treated earlier extended the framework to offline reinforcement learning by learning skill embeddings from offline datasets. The offline-learned skill space then serves as the action space for an online high-level policy, decoupling the skill-learning phase from the task-solving phase.

Diffusion-based skill representations of [Chi Feng Du Xu Cousineau Burchfiel Song 2023][research_chi_et_al_2023] (Diffusion Policy) use diffusion models as the low-level policy conditional on skill or goal representations. The mechanism provides substantial expressiveness for complex multi-modal action distributions that plain Gaussian policies struggle to capture, and has proved particularly effective for robot manipulation with high-frequency continuous action.

The choice between discrete and continuous skill representations represents a fundamental design axis in hierarchical reinforcement learning. Discrete options admit clean theoretical treatment through the options framework but require prior specification or discovery of the option set. Continuous skill embeddings admit end-to-end training and support smooth composition but sacrifice the analytical clarity of the options formalism.

## Language-Conditioned Hierarchical Control

The rise of large language models treated in article four has produced a class of language-conditioned hierarchical control systems in which the high-level policy is either a language model directly emitting subgoal commands or a policy conditioned on natural-language instructions from a language model. The framework treats language as a substrate for high-level plan specification and grounds language-level plans in low-level executable actions.

SayCan of [Ahn et al 2022][research_ahn_et_al_2022_saycan] combines an LLM that proposes candidate subgoal actions with a value function that scores each candidate for reachability under the current low-level policy. The combined score selects the next skill to execute,

$$p(\text{skill}_i \mid \text{context}) \propto p_{\text{LLM}}(\text{skill}_i \mid \text{context}) \cdot V(\text{skill}_i \mid s)$$

providing a hierarchical policy in which the language model handles high-level reasoning through natural language and the value function handles low-level executability grounding. The mechanism connects deployed language models to robotic control in a way that requires no additional training of the language model itself.

Inner Monologue of [Huang et al 2022][research_huang_et_al_2022] extends the SayCan framework with feedback loops in which execution outcomes, environment observations, and human feedback are fed back to the language model as additional context for revised planning. The framework produces language models that iteratively refine their plans in response to execution feedback.

PaLM-E of [Driess et al 2023][research_driess_et_al_2023] integrates vision, language, and control into a unified multimodal foundation model that can serve as either the planner or the low-level policy across a range of tasks. The model tokenizes images and continuous action signals alongside language tokens, producing a single autoregressive model over the joint sequence.

Voyager of [Wang et al 2023][research_wang_et_al_2023_voyager] uses an LLM as an open-ended lifelong agent in Minecraft, autonomously proposing curriculum items, executing them via code-generation into a game API, and accumulating a library of learned skills across many hours of gameplay. The framework connects hierarchical reinforcement learning to open-ended learning treated in article twelve.

The rapid pace of development in language-conditioned control has outpaced systematic theoretical treatment, but the empirical demonstrations across robotics, game-playing, and instruction-following tasks establish language-conditioned hierarchies as a substantial contemporary research direction.

## Option Discovery

The option discovery problem is the algorithmic construction of useful options without hand-specification. The problem has proved substantially harder than the algorithmic components of options learning, and no dominant solution has emerged as of the mid 2020s.

Bottleneck-state-based methods identify states through which many trajectories pass and define options that reach these bottleneck states. The intuition is that bottlenecks correspond to gateway states that must be traversed to reach many downstream regions, so options that reach bottlenecks provide broad utility. Approaches include the diverse-density method of [McGovern and Barto 2001][research_mcgovern_barto_2001] which identifies subgoal candidates as states appearing on many successful trajectories but few unsuccessful ones, the Q-Cut algorithm of [Menache Mannor and Shimkin 2002][research_menache_mannor_shimkin_2002] which uses graph min-cut to find bottleneck states, and the relative-novelty framework of [Simsek and Barto 2004][research_simsek_barto_2004] that identifies states whose visitation strongly precedes visitation of otherwise-rare states. [Wolfe and Barto 2005][research_wolfe_barto_2005] local graph partitioning provided an alternative graph-based subgoal-discovery method.

Successor-feature-based methods use the successor representation of [Dayan 1993][research_dayan_1993_hrl] to identify options that reach diverse regions of the state space. Options-of-Interest of Barreto et al 2019 provides one systematic instantiation. Eigenoption discovery of [Machado Bellemare Bowling 2018][research_machado_bellemare_bowling_2018_eigenoptions] uses the eigenfunctions of the successor representation to define options. The graph-Laplacian formulation constructs the state-transition matrix

$$L = D - W$$

where $W$ is the state-transition adjacency matrix under a uniform random policy and $D$ is the corresponding diagonal degree matrix. Eigenoption termination conditions are derived from the eigenvectors corresponding to small eigenvalues, capturing broad directional structure in the state space that promotes efficient exploration.

Skill discovery through mutual information treated in article five provides another algorithmic option-discovery approach. DIAYN, DADS, and their extensions produce diverse options through unsupervised objectives on the state distribution induced by each option.

Learning progress and empowerment-based option discovery provide additional signals for identifying useful options. Options that produce large empowerment gains or large learning progress on the current policy are candidates for skill retention.

The Option-Critic framework treated above provides an end-to-end approach to option discovery through gradient descent on the return, but suffers from the degeneracy problem in which learned options collapse to trivial behavior. Deliberation cost or termination-cost regularization addresses this partially,

$$L_{\text{OC}}(\theta, \vartheta) = -\mathbb{E}[G] + \eta \, \mathbb{E}\!\left[\sum_t \beta_{o_t, \vartheta}(s_t)\right]$$

where $\eta$ penalizes frequent option termination. The Termination Critic of [Harutyunyan Dabney Borsa Heess Munos Precup 2019][research_harutyunyan_et_al_2019] provides a principled information-theoretic objective that specifically targets the termination-degeneracy problem. Flexible option learning of [Klissarov and Precup 2021][research_klissarov_precup_2021] introduces adaptive regularization schedules that improve option-critic convergence.

Deep skill chaining of [Bagaria and Konidaris 2020][research_bagaria_konidaris_2020] combines options with sequential-chaining that constructs a chain of options ending at a task goal by iteratively learning options whose termination sets serve as initiation sets for the previous option in the chain. The [Konidaris and Barto 2007][research_konidaris_barto_2007] work on portable options established the earlier framework for transferable skills across contexts.

Options from Symbols of [Konidaris Kaelbling and Lozano-Perez 2018][research_konidaris_kaelbling_lozano_perez_2018] connects options to abstract symbolic planning, showing how options with well-defined effects support hierarchical task-network planning. Offline primitive discovery of [Ajay Kumar Agrawal Levine Nachum 2021][research_ajay_et_al_2021] (OPAL) learns skill primitives from offline datasets that can then be composed by an online meta-policy, connecting hierarchical reinforcement learning to the offline RL setting treated in article eight.

## Sample Complexity of Hierarchical Reinforcement Learning

The theoretical sample-complexity advantages of hierarchical decomposition have received substantial attention but remain incompletely characterized. The intuition is clear. If a task decomposes into $K$ subtasks each of horizon $H$, then flat learning must propagate value across the full $KH$-horizon while hierarchical learning could potentially learn subtasks in parallel and compose them into a policy of horizon $K$ at the high level and $H$ at each low level, potentially reducing sample complexity substantially.

Regret analysis for options under UCRL2-style optimism was given by [Fruit and Lazaric 2017][research_fruit_lazaric_2017], proving that options can substantially reduce regret when the option structure aligns with the task structure. The bound has the form

$$R_T = \tilde{\mathcal{O}}\!\left(D_O \sqrt{|\mathcal{S}| |\mathcal{O}| T}\right)$$

where $D_O$ is the diameter of the option-induced SMDP and $|\mathcal{O}|$ is the number of options. When $|\mathcal{O}| \ll |\mathcal{A}|$ and $D_O$ is comparable to the primitive-action diameter $D$, hierarchical exploration achieves substantially better regret than flat exploration.

[Wen Precup Ibarz Barreto Silver Van Roy 2020][research_wen_precup_ibarz_2020] provided efficient reinforcement learning via hierarchy analysis with sub-linear regret bounds under favorable option structures. The theoretical understanding of when hierarchical decomposition provably reduces sample complexity remains a productive research area with contributions continuing through the 2020s. Extensions include analysis of hierarchical policy iteration, sample-complexity bounds for MAXQ-style decompositions, and hierarchical PAC-MDP frameworks.

The gap between theoretical sample-complexity advantages of well-designed hierarchies and the practical difficulty of automatically discovering such hierarchies constitutes a substantial current tension in the field. Theoretical results assume that useful options exist and are used, while practical algorithms struggle to discover them without extensive supervision or hand-tuned regularization.

Empirical sample-complexity gains from hierarchical decomposition depend strongly on the alignment between the learned options and the underlying task structure. Well-aligned options can reduce sample complexity by orders of magnitude, misaligned options can produce worse performance than flat baselines. This sensitivity makes empirical evaluation of hierarchical methods particularly challenging.

## Hierarchical Imitation Learning

Hierarchical imitation learning combines the expert-demonstration setting of imitation learning treated in article eleven with hierarchical decomposition. The framework enables learning hierarchies from demonstration data rather than through the difficult online option-discovery problem, leveraging structural information implicit in expert behavior.

The [Fox Krishnan Stoica Goldberg 2017][research_fox_krishnan_stoica_goldberg_2017] Directed-Info GAIL framework infers latent option assignments in demonstration trajectories through variational expectation-maximization, identifying which segments of the demonstration correspond to which option. The identified segments provide supervised training data for option policies, converting the difficult online option-discovery problem into a supervised inference problem.

The [Le Yue Wang Kang Yue 2018][research_le_et_al_2018] hierarchical imitation and reinforcement learning framework combines expert-demonstrated high-level policy with learned low-level skills. The framework leverages hierarchical demonstration structure while adapting low-level execution to environment-details through reinforcement learning fine-tuning.

Behavioral cloning at each level of the hierarchy provides the simplest instantiation but requires demonstration data at each level. When high-level demonstrations are unavailable, weakly-supervised or unsupervised approaches attempt to infer high-level structure from primitive-action demonstrations, using change-point detection, mutual-information objectives, or clustering of trajectory segments to identify option boundaries.

Compile of [Kipf Li Bloem-Reddy Gonzales Battaglia Zoran 2019][research_kipf_et_al_2019] extended the option-inference framework to end-to-end differentiable inference through soft change-point detection. The Play-LMP framework of [Lynch Khansari Duong Nair Havaldar Hausman Levine Bellemare 2020][research_lynch_et_al_2020] used unsupervised play data as demonstration for a latent-plan-conditioned policy, connecting to the latent-code skill representations discussed above.

## Hierarchical Planning

Hierarchical planning combines hierarchical control with model-based reinforcement learning. When a world model is available or learnable, hierarchical planning can search across high-level action sequences while grounding the plan in low-level executable actions.

Hierarchical MCTS extends the Monte Carlo tree search of article four to the hierarchical setting. Trees are built over sequences of options rather than primitive actions, with each option leaf evaluated through low-level rollouts. AlphaGo-style self-play systems have used option-like abstractions in various forms.

Semi-parametric hierarchical planning combines learned models with structured planning. Methods including hierarchical variants of Dreamer treated in article four build world models over multiple timescales and plan across them jointly.

Option models describe the expected outcome of executing an option from a state, capturing both the expected duration and the expected next state distribution. Formally, the option model consists of a duration-and-outcome distribution

$$P^o(s', \tau \mid s) = P(s_{\tau} = s', \tau_o = \tau \mid s_0 = s, o)$$

and a cumulative reward function

$$R^o(s) = \mathbb{E}\!\left[\sum_{i=0}^{\tau_o - 1} \gamma^i r_{i+1} \mid s_0 = s, o\right]$$

Option models enable multi-step planning at the option timescale, providing a natural bridge between hierarchical control and model-based planning treated in article seven.

## Multi-Task and Multi-Agent Hierarchical RL

Hierarchical decomposition supports multi-task learning through shared low-level policies. When multiple tasks share the same primitive-action environment but differ in reward structure, the same low-level skills may be reusable across tasks with only the high-level policy adapting. Methods including Meta-Learning Shared Hierarchies of [Frans Ho Chen Abbeel Schulman 2018][research_frans_et_al_2018] explicitly train the low-level policy across a distribution of tasks to induce transferable skills.

Modular multitask reinforcement learning of [Andreas Klein Levine 2017][research_andreas_klein_levine_2017] uses natural-language descriptions of tasks to select among modular sub-policies, providing an alternative to purely-emergent modularity. Stochastic Neural Networks for Hierarchical RL of [Florensa Duan and Abbeel 2017][research_florensa_duan_abbeel_2017] learns a repertoire of skills via stochastic latent variables, applied to locomotion transfer. Learning modulated locomotor controllers of [Heess Wayne Silver Lillicrap Erez Tassa 2016][research_heess_wayne_silver_2016] demonstrated hierarchical decomposition on complex simulated locomotion tasks. The MCP framework of [Peng Chang Zhang Abbeel Levine 2019][research_peng_chang_zhang_2019] learns composable multiplicative-composition primitives for continuous control transfer.

Multi-agent hierarchical reinforcement learning combines the hierarchical decomposition of within-agent behavior with the multi-agent coordination challenges of article four. Hierarchical policies can decouple agent-level decisions (which agents to coordinate with, what team-level goal to pursue) from primitive-action decisions (movements to execute), providing computational and conceptual advantages.

## Practical Considerations and Design Choices

The design of hierarchical reinforcement learning systems involves several interacting decisions that shape empirical behavior substantially. Hierarchy depth (typically two levels but sometimes three or more), branching factor at each level (few options per state versus many), state representation at each level (raw observation versus learned abstraction), reward signal at each level (extrinsic only versus intrinsic subgoal-completion rewards), and the temporal grain of high-level decisions (fixed period versus terminate-when-appropriate) each affect learning dynamics substantially.

When hierarchy helps in practice has received systematic empirical analysis. [Nachum Tang Lee Gu Levine 2019][research_nachum_tang_lee_2019] documented conditions under which hierarchies provide substantial advantages, namely tasks with long horizons and clear sub-task structure, tasks where intrinsic reward or subgoal signal aligns with useful behavior, and tasks where the low-level policy can be pretrained on related tasks. Absent these conditions, flat methods often match or exceed hierarchical methods on standard benchmarks.

The choice between hand-designed and learned hierarchies represents a major design axis. Hand-designed hierarchies encode domain knowledge and often achieve strong initial performance at the cost of manual engineering effort and reduced generality. Learned hierarchies require less domain-design but often produce inferior or trivially-degenerate options without careful regularization.

Regularization strategies for learned options include termination-cost penalties, mutual-information objectives, diversity penalties, duration constraints, and information bottlenecks between levels. No single regularization strategy dominates across benchmarks, and empirical practice typically combines several. The [Vezhnevets et al 2020][research_vezhnevets_et_al_2020] Options-as-Responses framework provides one influential systematic proposal that uses response functions to shape option boundaries.

Empirical debugging of hierarchical agents presents distinctive challenges. Standard reinforcement learning diagnostics (value function estimates, TD error magnitudes, policy entropy) apply at each level of the hierarchy, but the interaction between levels can produce non-obvious failure modes. Manifestations include high-level policy oscillation between options (which prevents any option from executing to useful completion), low-level policy specialization to high-level commands (which prevents transfer across high-level policies), and complete option degeneracy (which reduces the hierarchy to a flat policy). Diagnostic tools that inspect option usage histograms, option duration distributions, and per-option value estimates support debugging of these failure modes.

The interaction of hierarchy with modern deep reinforcement learning techniques (PPO, SAC, world models) requires careful consideration. Off-policy hierarchical methods must handle the changing-low-level-policy problem addressed by HIRO's goal relabeling. On-policy hierarchical methods must handle the credit assignment across option boundaries. Actor-critic hierarchical methods must handle the interaction between multiple simultaneous policy gradients.

## Neuroscience Connections

Hierarchical control in biological brains has been extensively documented across multiple systems. The prefrontal cortex is widely implicated in the maintenance and hierarchical composition of task-level goals, with dorsolateral prefrontal cortex maintaining task-set representations that guide lower-level behavior. The cascade model of [Koechlin Ody Kouneiher 2003][research_koechlin_ody_kouneiher_2003] proposed a hierarchical organization of frontal cortex with progressively-more-abstract representations along a caudal-to-rostral axis.

The basal ganglia have been proposed to implement hierarchical action selection through parallel loops through cortex, striatum, pallidum, and thalamus. Each loop can be interpreted as selecting among actions at a particular level of abstraction, from motor to cognitive planning. The [Botvinick 2008][research_botvinick_2008] proposal for hierarchically-organized frontal-striatal loops provides a framework linking hierarchical reinforcement learning to neural circuitry, and [Botvinick Niv and Barto 2009][research_botvinick_niv_barto_2009] extended the treatment to include the developmental and evolutionary considerations of hierarchically organized behavior. [Solway Diuk Cordova Yee Barto Niv Botvinick 2014][research_solway_et_al_2014] proposed a normative account of behavioral hierarchy that predicts optimal decomposition of behavior in task settings. [Balaguer Spiers Hassabis and Summerfield 2016][research_balaguer_spiers_hassabis_summerfield_2016] identified neural signatures of hierarchical planning in human functional magnetic resonance imaging.

Dopamine-based reinforcement signals treated in article three extend naturally to the hierarchical setting through pseudo-reward at option termination. The correspondence between temporal-difference errors in dopamine responses and reinforcement signals at option boundaries has been proposed by [Ribas-Fernandes Solway Diuk McGuire Barto Niv Botvinick 2011][research_ribas_fernandes_et_al_2011] and successors, providing empirical evidence for the hierarchical reinforcement learning framework at a neural level.

The habit-versus-goal-directed distinction treated in article fifteen connects to hierarchical control through the mapping of habits to low-level cached options and goal-directed behavior to high-level model-based planning. The hierarchical framework provides a natural bridge between the two systems.

Article fourteen treats NeuroAI more systematically and returns to the correspondence between hierarchical reinforcement learning algorithms and neural mechanisms.

## Empirical Landscape

Hierarchical reinforcement learning benchmarks have been slower to standardize than flat RL benchmarks. The MuJoCo Ant Maze and Ant Push tasks used in HIRO have become de facto standards for continuous-control hierarchical RL evaluation. Craft/Minecraft-like environments including MineRL, Craftax, and NetHack provide challenging discrete-action hierarchical benchmarks with substantial task structure.

Atari hard-exploration games including Montezuma's Revenge remain common benchmarks that demonstrate hierarchical decomposition's value. Grid worlds with room structure, key-and-door tasks, and other structured environments provide simpler settings for diagnostic experiments.

Empirical performance of hierarchical methods has been mixed. On carefully-constructed hierarchical benchmarks, hierarchical methods often outperform flat methods substantially. On less-structured environments, the advantage is smaller or absent, and flat methods with sufficient compute often match hierarchical methods. The frequent observation that emergent options learned by end-to-end methods often collapse to trivial behavior suggests that current methods do not reliably discover useful temporal abstractions without additional inductive biases or supervision.

Reproducibility challenges in hierarchical reinforcement learning are similar to those documented for flat deep RL in article four. Hyperparameter sensitivity is often severe, and reported gains on benchmarks sometimes fail to reproduce with careful implementation. The [Wolczyk Zajac Pascanu Kucinski Milos 2021][research_wolczyk_et_al_2021] Continual World benchmark provides a systematic setting for evaluating hierarchical and continual reinforcement learning methods.

## Load-Bearing Open Questions

- What are the correct inductive biases for reliably learning useful options in end-to-end trained hierarchical agents? Current methods produce trivial or over-specialized options without additional regularization, and no single regularization strategy dominates.
- How should the hierarchy depth and branching factor be determined? Two-level hierarchies dominate the literature, but there is no principled account of when deeper hierarchies would provide additional benefit.
- What is the correct theoretical framework for sample complexity in hierarchical reinforcement learning? Bounds analogous to PAC-MDP exist for restricted settings but do not straightforwardly generalize.
- How can hierarchical decomposition be reliably combined with model-based reinforcement learning? Option models exist in principle but have not produced the empirical gains that flat model-based methods have achieved.
- To what extent do the algorithmic hierarchies studied in machine learning correspond to the hierarchical control mechanisms in biological brains? Correspondence at coarse levels is well documented, but detailed algorithmic correspondence remains open.
- How should hierarchical decomposition interact with meta-learning and continual learning? Learned low-level skills should support fast adaptation to new tasks, but current methods do not consistently deliver this promise.
- What is the correct handling of the exploration problem in hierarchical settings? Options can dramatically improve exploration when the option boundaries align with task structure but can hinder exploration when they do not.
- How should the trade-off between recursive optimality and hierarchical optimality be resolved in practice? Recursive optimality is often much easier to achieve but is not guaranteed to produce globally-optimal behavior.

## References

### Books

- [Precup 2000 Thesis][book_precup_thesis_2000]
- [Sutton and Barto 2018][book_sutton_barto_2018]

### Reference

- [Berkeley CS285][ref_berkeley_cs285]
- [DeepMind x UCL RL Course][ref_deepmind_ucl_rl]
- [OpenAI Spinning Up][ref_openai_spinning_up]
- [Silver RL Course UCL][ref_silver_rl_course]
- [Stanford CS234][ref_stanford_cs234]

### Related Posts

- [A250 Machines That Learn From Experience Framing][related_post_a250_framing]
- [A251 Machines That Learn From Experience Bandits and Online Learning][related_post_a251_bandits]
- [A252 Machines That Learn From Experience Reinforcement Learning Foundations][related_post_a252_rl_foundations]
- [A253 Machines That Learn From Experience Deep Reinforcement Learning][related_post_a253_deep_rl]
- [A254 Machines That Learn From Experience Exploration Intrinsic Motivation and Curiosity][related_post_a254_exploration]

### Research

- [Ahn et al 2022 SayCan][research_ahn_et_al_2022_saycan]
- [Ajay Kumar Agrawal Levine Nachum 2021][research_ajay_et_al_2021]
- [Andreas Klein and Levine 2017][research_andreas_klein_levine_2017]
- [Bacon Harb and Precup 2017][research_bacon_harb_precup_2017]
- [Bagaria and Konidaris 2020][research_bagaria_konidaris_2020]
- [Balaguer Spiers Hassabis Summerfield 2016][research_balaguer_spiers_hassabis_summerfield_2016]
- [Barreto et al 2019][research_barreto_et_al_2019]
- [Barto and Mahadevan 2003][research_barto_mahadevan_2003]
- [Botvinick 2008][research_botvinick_2008]
- [Botvinick Niv Barto 2009][research_botvinick_niv_barto_2009]
- [Brooks 1986][research_brooks_1986]
- [Chi Feng Du Xu Cousineau Burchfiel Song 2023][research_chi_et_al_2023]
- [Dayan 1993][research_dayan_1993_hrl]
- [Dayan and Hinton 1993][research_dayan_hinton_1993]
- [Dietterich 2000][research_dietterich_2000]
- [Driess et al 2023 PaLM-E][research_driess_et_al_2023]
- [Florensa Duan and Abbeel 2017][research_florensa_duan_abbeel_2017]
- [Fox Krishnan Stoica Goldberg 2017][research_fox_krishnan_stoica_goldberg_2017]
- [Frans Ho Chen Abbeel Schulman 2018][research_frans_et_al_2018]
- [Fruit and Lazaric 2017][research_fruit_lazaric_2017]
- [Harutyunyan Dabney Borsa Heess Munos Precup 2019][research_harutyunyan_et_al_2019]
- [Heess Wayne Silver Lillicrap Erez Tassa 2016][research_heess_wayne_silver_2016]
- [Huang et al 2022 Inner Monologue][research_huang_et_al_2022]
- [Kipf Li Bloem-Reddy Gonzales Battaglia Zoran 2019][research_kipf_et_al_2019]
- [Klissarov and Precup 2021][research_klissarov_precup_2021]
- [Koechlin Ody Kouneiher 2003][research_koechlin_ody_kouneiher_2003]
- [Konidaris and Barto 2007][research_konidaris_barto_2007]
- [Konidaris Kaelbling Lozano-Perez 2018][research_konidaris_kaelbling_lozano_perez_2018]
- [Kulkarni Narasimhan Saeedi Tenenbaum 2016][research_kulkarni_et_al_2016]
- [Le Yue Wang Kang Yue 2018][research_le_et_al_2018]
- [Levy et al 2018][research_levy_et_al_2018]
- [Lynch et al 2020][research_lynch_et_al_2020]
- [Machado Bellemare Bowling 2018][research_machado_bellemare_bowling_2018_eigenoptions]
- [McGovern and Barto 2001][research_mcgovern_barto_2001]
- [Menache Mannor and Shimkin 2002][research_menache_mannor_shimkin_2002]
- [Merel Hasenclever Galashov Ahuja Tassa Wayne Tirumala Wulfmeier Heess 2019][research_merel_et_al_2019]
- [Nachum Gu Lee Levine 2018][research_nachum_gu_lee_levine_2018]
- [Nachum et al 2019][research_nachum_et_al_2019]
- [Nachum Tang Lee Gu Levine 2019][research_nachum_tang_lee_2019]
- [Parr and Russell 1998][research_parr_russell_1998]
- [Peng Chang Zhang Abbeel Levine 2019][research_peng_chang_zhang_2019]
- [Precup and Sutton 1998][research_precup_sutton_1998]
- [Ribas-Fernandes Solway Diuk McGuire Barto Niv Botvinick 2011][research_ribas_fernandes_et_al_2011]
- [Schaul Horgan Gregor Silver 2015][research_schaul_horgan_gregor_silver_2015_hrl]
- [Simsek and Barto 2004][research_simsek_barto_2004]
- [Solway Diuk Cordova Yee Barto Niv Botvinick 2014][research_solway_et_al_2014]
- [Sutton Precup and Singh 1999][research_sutton_precup_singh_1999]
- [Vezhnevets et al 2017][research_vezhnevets_et_al_2017]
- [Vezhnevets et al 2020][research_vezhnevets_et_al_2020]
- [Wang et al 2023 Voyager][research_wang_et_al_2023_voyager]
- [Wen Precup Ibarz Barreto Silver Van Roy 2020][research_wen_precup_ibarz_2020]
- [Wolczyk Zajac Pascanu Kucinski Milos 2021][research_wolczyk_et_al_2021]
- [Wolfe and Barto 2005][research_wolfe_barto_2005]

[book_precup_thesis_2000]: https://scholarworks.umass.edu/dissertations/AAI9978540/
[book_sutton_barto_2018]: http://incompleteideas.net/book/the-book-2nd.html
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
[research_ahn_et_al_2022_saycan]: https://arxiv.org/abs/2204.01691
[research_ajay_et_al_2021]: https://openreview.net/forum?id=V69LGwJ0lIN
[research_andreas_klein_levine_2017]: https://proceedings.mlr.press/v70/andreas17a.html
[research_bacon_harb_precup_2017]: https://ojs.aaai.org/index.php/AAAI/article/view/10916
[research_bagaria_konidaris_2020]: https://openreview.net/forum?id=B1gqipNYwH
[research_balaguer_spiers_hassabis_summerfield_2016]: https://www.cell.com/neuron/fulltext/S0896-6273(16)00104-1
[research_barreto_et_al_2019]: https://arxiv.org/abs/1901.05075
[research_barto_mahadevan_2003]: https://link.springer.com/article/10.1023/A:1025696116075
[research_botvinick_2008]: https://www.sciencedirect.com/science/article/pii/S1364661308002052
[research_botvinick_niv_barto_2009]: https://www.sciencedirect.com/science/article/pii/S0010027708001960
[research_brooks_1986]: https://ieeexplore.ieee.org/document/1087032
[research_chi_et_al_2023]: https://arxiv.org/abs/2303.04137
[research_dayan_1993_hrl]: https://direct.mit.edu/neco/article/5/4/613/5679
[research_dayan_hinton_1993]: https://papers.nips.cc/paper/1992/hash/d14220ee66aeec73c49038385428ec4c-Abstract.html
[research_dietterich_2000]: https://www.jair.org/index.php/jair/article/view/10266
[research_driess_et_al_2023]: https://arxiv.org/abs/2303.03378
[research_florensa_duan_abbeel_2017]: https://openreview.net/forum?id=B1oK8aoxe
[research_fox_krishnan_stoica_goldberg_2017]: https://arxiv.org/abs/1703.08294
[research_frans_et_al_2018]: https://openreview.net/forum?id=SyX0IeWAW
[research_fruit_lazaric_2017]: https://papers.nips.cc/paper/2017/hash/d3b1fb02964aa64e257f9f26a31f72cf-Abstract.html
[research_harutyunyan_et_al_2019]: https://ojs.aaai.org/index.php/AAAI/article/view/4342
[research_heess_wayne_silver_2016]: https://papers.nips.cc/paper/2016/hash/74563ba21a90da13dacf2a73e3ddefa7-Abstract.html
[research_huang_et_al_2022]: https://arxiv.org/abs/2207.05608
[research_kipf_et_al_2019]: https://proceedings.mlr.press/v97/kipf19a.html
[research_klissarov_precup_2021]: https://papers.nips.cc/paper/2021/hash/2ab3e4b0e69cf49c26f0c98d7f5ef8ba-Abstract.html
[research_koechlin_ody_kouneiher_2003]: https://www.science.org/doi/10.1126/science.1088545
[research_konidaris_barto_2007]: https://link.springer.com/article/10.1007/s10514-007-9034-y
[research_konidaris_kaelbling_lozano_perez_2018]: https://www.jair.org/index.php/jair/article/view/11175
[research_kulkarni_et_al_2016]: https://papers.nips.cc/paper/2016/hash/f442d33fa06832082290ad8544a8da27-Abstract.html
[research_le_et_al_2018]: https://proceedings.mlr.press/v80/le18a.html
[research_levy_et_al_2018]: https://openreview.net/forum?id=ryzECoAcY7
[research_lynch_et_al_2020]: https://proceedings.mlr.press/v100/lynch20a.html
[research_machado_bellemare_bowling_2018_eigenoptions]: https://ojs.aaai.org/index.php/AAAI/article/view/11824
[research_mcgovern_barto_2001]: https://scholarworks.umass.edu/cs_faculty_pubs/8/
[research_menache_mannor_shimkin_2002]: https://link.springer.com/chapter/10.1007/3-540-36755-1_25
[research_merel_et_al_2019]: https://openreview.net/forum?id=BJl6TjRcY7
[research_nachum_gu_lee_levine_2018]: https://papers.nips.cc/paper/2018/hash/e6384711491713d29bc63fc5eeb5ba4f-Abstract.html
[research_nachum_et_al_2019]: https://openreview.net/forum?id=H1emus0qF7
[research_nachum_tang_lee_2019]: https://openreview.net/forum?id=SkljlBEtvS
[research_parr_russell_1998]: https://papers.nips.cc/paper/1997/hash/5487315b1286f907165907aa8fc96619-Abstract.html
[research_peng_chang_zhang_2019]: https://papers.nips.cc/paper/2019/hash/95192c98732387165bf8e396c0f2dad2-Abstract.html
[research_precup_sutton_1998]: https://papers.nips.cc/paper/1997/hash/44e2be2a5b9e6f4e421c58af1c8e5fef-Abstract.html
[research_ribas_fernandes_et_al_2011]: https://www.cell.com/neuron/fulltext/S0896-6273(11)00559-X
[research_schaul_horgan_gregor_silver_2015_hrl]: https://proceedings.mlr.press/v37/schaul15.html
[research_simsek_barto_2004]: https://dl.acm.org/doi/10.1145/1015330.1015353
[research_solway_et_al_2014]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003779
[research_sutton_precup_singh_1999]: https://www.sciencedirect.com/science/article/pii/S0004370299000521
[research_vezhnevets_et_al_2017]: https://proceedings.mlr.press/v70/vezhnevets17a.html
[research_vezhnevets_et_al_2020]: https://openreview.net/forum?id=BJgUX6VtDB
[research_wang_et_al_2023_voyager]: https://arxiv.org/abs/2305.16291
[research_wen_precup_ibarz_2020]: https://arxiv.org/abs/2002.05095
[research_wolczyk_et_al_2021]: https://papers.nips.cc/paper/2021/hash/ae3b6d6a89a3b56ca5c8b6c65e26326d-Abstract.html
[research_wolfe_barto_2005]: https://dl.acm.org/doi/10.1145/1102351.1102481
