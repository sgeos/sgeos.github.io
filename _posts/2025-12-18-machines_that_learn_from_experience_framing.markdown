---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: Framing"
date:   2025-12-18 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 1
---

<!-- A250 -->
<script>console.log("A250");</script>

Adaptive learning from experience constitutes a family of computational problems distinct from the batch learning that dominates supervised machine learning. In experiential learning, a learner interacts with an environment over time, its actions shape the data it subsequently receives, and its objective is not to fit a fixed dataset but to maximize a cumulative long-run signal against a partially known and possibly non-stationary world. This article opens a sixteen-article series that surveys the science and theory of adaptive, reinforcement, and experiential-learning artificial intelligence together with the neuroscience and psychology of learning from which the field has borrowed extensively and to which it now contributes reciprocally. The framing here establishes the agent-environment loop as the field's central formal object, distinguishes the problems that arise from those of batch supervised learning, introduces a six-axis analytical framework that subsequent articles apply, previews the mind-sciences boundary at which the hardest open problems sit, and lays down the roadmap for the sixteen articles that follow.

## The Agent-Environment Loop

The agent-environment loop is the fundamental object of study. A learning agent occupies an environment that persists in some state over time. At each discrete time step $t$, the agent observes some function of the environment state, selects an action from an admissible action set, receives a scalar reward signal, and the environment transitions to a new state. The interaction proceeds indefinitely or until an episodic terminal condition is reached.

Formally, a Markov decision process is a tuple

$$
\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, R, \gamma, \mu_0)
\tag{1}
$$

where $\mathcal{S}$ is the state space, $\mathcal{A}$ is the action space, $P$ is the transition kernel, $R$ is the reward function, $\gamma \in [0, 1)$ is the discount factor, and $\mu_0$ is the initial state distribution. The transition kernel

$$
P(s_{t+1} \mid s_t, a_t)
\tag{2}
$$

satisfies the Markov property, meaning that the distribution of $s_{t+1}$ conditional on the full history $(s_0, a_0, \ldots, s_t, a_t)$ depends only on the most recent state and action,

$$
P(s_{t+1} \mid s_t, a_t, s_{t-1}, a_{t-1}, \ldots, s_0, a_0) = P(s_{t+1} \mid s_t, a_t)
\tag{3}
$$

The reward at step $t+1$ is drawn from a distribution $R(r_{t+1} \mid s_t, a_t, s_{t+1})$ or in deterministic settings from a function $r(s_t, a_t)$.

The agent selects actions according to a policy $\pi$, which is either a deterministic function $\pi : \mathcal{S} \to \mathcal{A}$ or a stochastic function $\pi(a \mid s)$ giving a probability distribution over actions with

$$
\sum_a \pi(a \mid s) = 1, \quad \pi(a \mid s) \geq 0
\tag{4}
$$

The agent's objective is to select a policy that maximizes the expected discounted return

$$
G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k+1}
\tag{5}
$$

where $\gamma \in [0, 1)$ is a discount factor that trades off immediate against delayed reward. For episodic tasks the sum is finite and the discount factor may be one. An alternative objective is the average reward per step,

$$
J_{\text{avg}}(\pi) = \lim_{T \to \infty} \frac{1}{T} \mathbb{E}_{\pi} \left[ \sum_{t=0}^{T-1} r_{t+1} \right]
\tag{6}
$$

which is appropriate for continuing tasks where discounting is inappropriate.

The policy $\pi$ induces a joint distribution over trajectories $\tau = (s_0, a_0, r_1, s_1, a_1, r_2, \ldots)$ given by

$$
p_{\pi}(\tau) = \mu_0(s_0) \prod_{t=0}^{\infty} \pi(a_t \mid s_t) P(s_{t+1} \mid s_t, a_t)
\tag{7}
$$

and induces a marginal state distribution $d^{\pi}(s)$ obtained by summing this joint over histories.

Two additional formalizations are worth naming at the outset. The partially observable Markov decision process replaces direct state observation by an observation $o_t$ drawn from an observation kernel

$$
O(o_t \mid s_t)
\tag{8}
$$

with the agent obliged to maintain a belief state $b_t(s) = P(s_t = s \mid o_1, a_1, \ldots, o_t)$ or a sufficient statistic of history to act well. The contextual bandit reduces the problem to a single decision at each step under a contextual signal, with no dynamics linking successive states. Both objects appear in later articles.

The agent-environment loop unifies problems that appear disparate at first inspection. Robot manipulation, board game play, dialogue policy learning, adaptive experimental design, animal foraging, and organizational strategy all instantiate the same abstract structure, differing only in the identities of $\mathcal{S}$, $\mathcal{A}$, $R$, and $P$. This unification is at once the field's greatest theoretical strength and its most seductive trap. Later articles will treat the settings in which the loop's assumptions are load-bearing and those in which they are approximations. [Sutton and Barto 2018][book_sutton_barto_2018] provides the canonical modern treatment of the loop as the organizing formalism of reinforcement learning.

## Historical Roots

The agent-environment loop as a research object descends from several parallel developments. Behaviorist psychology under [Pavlov 1927][book_pavlov_1927] work on conditional reflex, [Thorndike 1911][book_thorndike_1911] law of effect, and [Skinner 1938][book_skinner_1938] operant conditioning identified reinforcement as the mechanism by which animal behavior adapts to consequences, laying the empirical foundation for what came to be called instrumental or operant conditioning. The [Rescorla and Wagner 1972][research_rescorla_wagner_1972] model formalized classical conditioning as prediction-error-driven associative learning and would later be shown to correspond mathematically to temporal-difference learning. Cybernetics under [Wiener 1948][book_wiener_1948] and [Ashby 1952][book_ashby_1952] framed adaptation as feedback control across biological, mechanical, and social systems.

The neural side of the story runs in parallel. [McCulloch and Pitts 1943][research_mcculloch_pitts_1943] introduced the threshold neuron model that set the direction for computational neuroscience and neural-network machine learning alike. [Hebb 1949][book_hebb_1949] proposed the associative learning rule that neurons which fire together wire together, providing the foundational learning principle for Hebbian and later contrastive learning approaches. [Minsky 1961][research_minsky_1961] surveyed the problem structure of artificial intelligence and identified reinforcement learning as one of its central pillars. [Klopf 1972][research_klopf_1972] hedonistic neuron proposal explicitly connected reinforcement learning ideas to single-neuron computation and directly influenced the Barto-Sutton program.

Dynamic programming under [Bellman 1957][book_bellman_1957] gave the recursive mathematical structure that would later underpin reinforcement learning's core algorithms, and Howard's [Howard 1960][book_howard_1960] policy iteration extended dynamic programming to Markov decision processes with an explicit policy object. In the same period, [Samuel 1959][research_samuel_1959] implemented an early self-play learning system for checkers that anticipated modern reinforcement learning by decades, and [Widrow and Hoff 1960][research_widrow_hoff_1960] introduced the least-mean-squares adaptive filter that provided one of the earliest online learning rules.

The synthesis emerged in the 1980s. Sutton's [Sutton 1988][research_sutton_1988] temporal-difference learning connected animal learning experiments to computable algorithms via the Rescorla-Wagner model, whose associative strength update

$$
\Delta V_i = \alpha_i \beta \left( \lambda - \sum_j V_j \right)
\tag{9}
$$

expresses conditioning as a prediction-error-driven adjustment of associative strengths $V_j$ toward the reinforcement magnitude $\lambda$. Watkins's [Watkins 1989][research_watkins_1989] Q-learning provided the first convergence-guaranteed reinforcement learning algorithm for tabular control. Williams's [Williams 1992][research_williams_1992] REINFORCE established the policy gradient theorem's practical form. Barto, Sutton, and Anderson's [Barto et al. 1983][research_barto_sutton_anderson_1983] actor-critic architecture drew on neuroscience for its inspiration. By the mid 1990s the [Kaelbling et al. 1996][research_kaelbling_littman_moore_1996] survey codified reinforcement learning as a distinct field, and [Bertsekas and Tsitsiklis 1996][book_bertsekas_tsitsiklis_1996] provided its mathematical foundations under the label neuro-dynamic programming.

The 2010s produced deep reinforcement learning through the marriage of the classical algorithms with neural function approximation. [Mnih et al. 2015][research_mnih_et_al_2015] deep Q-networks demonstrated human-level Atari game play from pixels. [Silver et al. 2016][research_silver_et_al_2016] AlphaGo defeated Lee Sedol in Go. [Silver et al. 2017][research_silver_et_al_2017] AlphaZero achieved superhuman performance in chess, shogi, and Go from self-play alone. Article three in this series treats the deep reinforcement learning wave in detail.

Alongside these algorithmic developments, the neuroscience of reward learning uncovered striking parallels. [Schultz et al. 1997][research_schultz_dayan_montague_1997] identified midbrain dopamine neurons as encoding a reward prediction error mathematically identical to the temporal-difference error, launching the modern era of computational neuroscience-machine learning cross-fertilization. Article fourteen surveys this bridge under the emerging label NeuroAI.

## Learning From Experience Versus Batch Learning

Supervised batch learning, which dominates contemporary machine learning practice, poses a fundamentally different problem. In batch supervised learning, a training set $\{(x_i, y_i)\}\_{i=1}^n$ is drawn independently and identically distributed from a fixed distribution $\mathcal{D}$,

$$
(x_i, y_i) \stackrel{\text{iid}}{\sim} \mathcal{D}, \quad i = 1, \ldots, n
\tag{10}
$$

and the objective is to fit a function $f : \mathcal{X} \to \mathcal{Y}$ that minimizes an empirical risk

$$
\hat{R}(f) = \frac{1}{n} \sum_{i=1}^n L(f(x_i), y_i)
\tag{11}
$$

as a proxy for the true risk $R(f) = \mathbb{E}\_{(x,y) \sim \mathcal{D}}[L(f(x), y)]$. The learner does not choose which $x_i$ to observe, the data distribution does not change over training, the objective decomposes into per-sample losses, and the assumptions of statistical learning theory permit generalization bounds under standard capacity control.

Experiential learning violates each of these conditions.

First, the data distribution depends on the agent's own behavior. If the agent's policy changes, the state distribution over which it collects data changes as well,

$$
d^{\pi}(s) \neq d^{\pi'}(s) \quad \text{in general when} \quad \pi \neq \pi'
\tag{12}
$$

This coupling breaks the independence assumption underlying most concentration bounds in statistical learning theory and forces reasoning about the joint distribution of policy and data.

Second, the objective is not a per-sample loss but a return that depends on a temporally extended trajectory. Credit assignment across a sequence of actions requires attributing reward to actions taken possibly many steps earlier. The temporal-difference and policy-gradient algorithms of the next articles are the field's principal tools for this attribution problem.

Third, the agent must choose what data to collect. The exploration-exploitation trade-off, formalized in the multi-armed bandit setting treated in article two, forces the agent to balance obtaining reward under the current best policy against gathering information that may reveal a better policy. There is no batch supervised analog to this trade-off because the batch already exists.

Fourth, the environment may be non-stationary. State transitions, reward distributions, or task specifications may change over the agent's lifetime. The continual and lifelong learning literature treated in article ten develops the algorithmic responses to non-stationarity, and the meta-learning literature in article nine develops learning-to-learn approaches that seek to adapt fast to distributional shift.

Fifth, the interaction may be adversarial or multi-agent. Other learning agents adapt in response to the learner's own adaptations, producing the game-theoretic dynamics treated in article eleven. Even single-agent problems can become effectively adversarial when the reward function is misspecified and the agent optimizes against the specification rather than the intent.

These five departures make experiential learning theoretically distinct from batch supervised learning rather than merely a special case. Statistical learning theory in the supervised setting provides probably approximately correct (PAC) generalization bounds of the form

$$
P\left( R(f) - \hat{R}(f) > \epsilon \right) \leq \delta
\tag{13}
$$

for hypothesis class complexity control, sample size $n$, and confidence $\delta$. The corresponding sample-complexity theory for reinforcement learning replaces $\epsilon$ with suboptimality of the learned policy and $n$ with the number of environment interactions. Foundational results include the PAC-MDP framework and its subsequent refinements. Article three treats the sample-complexity landscape for tabular and function-approximation reinforcement learning. The rest of this series treats each departure in depth.

## The Six-Axis Analytical Framework

Subsequent articles in the series treat the field along six analytical axes that recur throughout. Naming them here provides a shared vocabulary for cross-article comparison.

The first axis is signal. The learner may receive a full reward function at every step (dense reward), a reward only at episode termination (sparse reward), a preference between trajectories rather than a scalar reward (preference learning), a demonstration of desired behavior (imitation), or an intrinsic motivation signal computed from its own predictions (curiosity). Different signals require different algorithms and impose different sample-efficiency constraints.

The second axis is objective. The learner may optimize expected discounted return (the classical MDP objective), long-run average reward, distributional characteristics of return such as variance or conditional value at risk

$$
\text{CVaR}_\alpha[G] = \mathbb{E}[G \mid G \leq q_\alpha(G)]
\tag{14}
$$

where $q_\alpha$ denotes the $\alpha$-quantile of the return distribution (risk-sensitive objectives treated in article four's extensions), regret against a reference policy

$$
R_T = \sum_{t=1}^T \left( r^*_t - r_t \right)
\tag{15}
$$

or an information-theoretic objective such as empowerment, the maximum mutual information between an action sequence and the resulting state,

$$
\mathfrak{E}(s) = \max_{\pi} I(A_{t:t+k} ; S_{t+k} \mid S_t = s)
\tag{16}
$$

The choice of objective changes the algorithmic surface substantially.

The third axis is structure. The learner may face a flat Markov decision process, a partially observable Markov decision process, a hierarchical Markov decision process with options or sub-policies, a factored state space, a multi-agent stochastic game, or a partially observable stochastic game. Article six treats hierarchical structure directly, and article twelve treats multi-agent structure.

The fourth axis is model. The learner may be model-free, using only samples from the environment to update a policy or value function, model-based, learning an internal model of the environment to plan with, or model-implicit, using a learned representation that supports planning without an explicit generative model. Article seven treats model-based reinforcement learning and world models in detail.

The fifth axis is interaction. The learner may be online, collecting data from the environment as it learns, offline, learning from a fixed dataset of prior experience without further interaction, on-policy, using data collected under the current policy, or off-policy, using data collected under other policies. Article eight treats offline reinforcement learning and its distributional shift problem.

The sixth axis is adaptation. The learner may face a stationary task, a non-stationary task with drifting distribution, a task family with rapid adaptation required for each new task, or an open-ended stream of tasks with no clear end. Articles nine and ten treat meta-learning and continual learning respectively, and article twelve treats open-ended and evolutionary approaches.

Each subsequent article in the series positions its subject along these six axes explicitly, and the synthesis article at the end of the series maps the whole field onto this framework.

## Foundational Formal Objects

Before proceeding to the topics of subsequent articles, the framing article names the formal objects that recur throughout.

The state value function under a policy $\pi$ is the expected return from state $s$ under $\pi$,

$$
V^{\pi}(s) = \mathbb{E}_{\pi} \left[ G_t \mid s_t = s \right]
\tag{17}
$$

The action value function or Q function under $\pi$ is the expected return from state $s$ taking action $a$ and thereafter following $\pi$,

$$
Q^{\pi}(s, a) = \mathbb{E}_{\pi} \left[ G_t \mid s_t = s, a_t = a \right]
\tag{18}
$$

The Bellman expectation equation gives the recursive relationship

$$
V^{\pi}(s) = \sum_a \pi(a \mid s) \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V^{\pi}(s') \right]
\tag{19}
$$

and the Bellman optimality equation gives

$$
V^*(s) = \max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V^*(s') \right]
\tag{20}
$$

An optimal policy $\pi^\*$ is any policy achieving $V^{\pi^\*} = V^\*$ at every state. Existence of optimal deterministic policies is guaranteed for finite MDPs under standard conditions [Puterman 1994][book_puterman_1994]. The corresponding Bellman optimality equation for the action value function is

$$
Q^*(s, a) = \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma \max_{a'} Q^*(s', a') \right]
\tag{21}
$$

and an optimal policy is recovered by the greedy rule

$$
\pi^*(s) = \arg\max_a Q^*(s, a)
\tag{22}
$$

The advantage function measures how much better action $a$ is than the average action under $\pi$,

$$
A^{\pi}(s, a) = Q^{\pi}(s, a) - V^{\pi}(s)
\tag{23}
$$

and appears as a variance-reduction baseline in policy-gradient methods. The Bellman expectation operator $T^{\pi}$ acting on value functions is a $\gamma$-contraction under the sup norm,

$$
\| T^{\pi} V - T^{\pi} V' \|_{\infty} \leq \gamma \| V - V' \|_{\infty}
\tag{24}
$$

which by the Banach fixed-point theorem guarantees a unique fixed point $V^{\pi}$ and convergence of value iteration.

Temporal-difference learning updates a value estimate $V(s_t)$ using the sampled TD error

$$
\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)
\tag{25}
$$

toward its target $r_{t+1} + \gamma V(s_{t+1})$ with step size $\alpha$,

$$
V(s_t) \leftarrow V(s_t) + \alpha \delta_t
\tag{26}
$$

The corresponding action-value update rules are SARSA,

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t) \right]
\tag{27}
$$

and Q-learning,

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t) \right]
\tag{28}
$$

which differ in whether the target uses the actual next action (SARSA, on-policy) or the maximizing next action (Q-learning, off-policy).

The policy gradient theorem gives the gradient of the expected return $J(\theta) = \mathbb{E}\_{\pi_\theta}[G_0]$ under a parameterized policy $\pi_\theta$,

$$
\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \sum_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, Q^{\pi_\theta}(s_t, a_t) \right]
\tag{29}
$$

which underlies the REINFORCE algorithm and its many descendants including actor-critic, trust-region policy optimization, and proximal policy optimization treated in articles three and four. Variance reduction by subtracting a state-dependent baseline $b(s_t)$ gives the advantage form

$$
\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \sum_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, A^{\pi_\theta}(s_t, a_t) \right]
\tag{30}
$$

which uses the advantage function defined above.

The classical planning algorithms proceed by iterating the Bellman operator. Value iteration applies the optimality operator directly,

$$
V_{k+1}(s) = \max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V_k(s') \right]
\tag{31}
$$

converging to $V^\*$ from any initial $V_0$ at a geometric rate governed by $\gamma$. Policy iteration alternates policy evaluation, which solves the Bellman expectation equation for the current policy, and policy improvement, which sets

$$
\pi_{k+1}(s) = \arg\max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V^{\pi_k}(s') \right]
\tag{32}
$$

and converges to $\pi^\*$ in a finite number of iterations for finite MDPs. When the environment model is unavailable, Monte Carlo estimation replaces the expectation with sample averages from full episodes,

$$
V(s) \leftarrow V(s) + \alpha \left[ G_t - V(s) \right]
\tag{33}
$$

where $G_t$ is the actual return observed from state $s$ at time $t$. Temporal-difference learning bootstraps a partial estimate rather than waiting for episode completion.

For off-policy learning, importance sampling corrects for the mismatch between the behavior policy $\mu$ that generated the data and the target policy $\pi$ being evaluated. The per-step ratio is

$$
\rho_t = \frac{\pi(a_t \mid s_t)}{\mu(a_t \mid s_t)}
\tag{34}
$$

and the trajectory-level ratio $\rho_{t:T} = \prod_{k=t}^{T} \rho_k$ appears in the importance-sampling estimator of the value function. Article eight develops the practical consequences of importance-sampling variance for offline learning.

These objects recur throughout the series. Articles two through five build the classical and deep reinforcement learning apparatus around them.

## The Mind Sciences Boundary

The hardest open problems in adaptive learning cluster at the boundary with neuroscience and psychology of learning. The bridge runs in both directions.

From machine learning to the mind sciences, temporal-difference learning provided the computational hypothesis that unified [Schultz et al. 1997][research_schultz_dayan_montague_1997] a wealth of behavioral and electrophysiological data on midbrain dopamine as a reward prediction error. Actor-critic architectures aligned with the anatomy of basal ganglia loops. Hippocampal experience replay [McClelland et al. 1995][research_mcclelland_mcnaughton_oreilly_1995] parallels the experience-replay buffers that stabilize deep reinforcement learning.

From the mind sciences to machine learning, the developmental robotics literature draws on [Piaget 1936][book_piaget_1936] constructivism and on developmental psychology to argue for staged, embodied learning. Predictive processing and active inference [Friston 2010][research_friston_2010] frame the brain as a hierarchical prediction machine that minimizes a variational free energy,

$$
F = \mathbb{E}_{q(s)} \left[ \log q(s) - \log p(o, s) \right] = D_{\text{KL}}(q(s) \, \| \, p(s \mid o)) - \log p(o)
\tag{35}
$$

where $q(s)$ is a recognition distribution over hidden states and $p(o, s)$ is a generative model of observations and hidden states. Active inference extends the framing to action by treating action selection as minimization of expected free energy over future outcomes. The framing has produced influential models of perception, action selection, and interoception, and overlaps with model-based reinforcement learning in ways treated in articles seven and fourteen. Cognitive architectures such as SOAR [Newell 1990][book_newell_1990], ACT-R [Anderson 2007][book_anderson_2007], and CLARION carry decades of cognitive-psychology insight into computational form. [Simon 1969][book_simon_1969] treatment of bounded rationality provides an early framing of intelligence as constrained optimization under limited computational resources that has since informed both artificial intelligence and behavioral economics.

The reciprocal traffic between these fields is neither purely metaphorical nor a straightforward mapping. Machine learning models often abstract away neural implementation constraints that are load-bearing for the brain, and mind-sciences models often invoke functional decompositions whose computational realization is contested. Articles thirteen and fourteen treat these frictions directly, and article fifteen surveys the psychology of learning literature that has shaped the field's algorithmic vocabulary.

## The Hard Problems

The characteristic difficulty of experiential learning can be located in five recurring problem classes.

Credit assignment. When an agent receives a reward after a temporally extended sequence of actions, the question of which actions were responsible for the reward is the temporal credit assignment problem. Backward-in-time algorithms such as temporal-difference learning and eligibility traces distribute credit through bootstrapping, forward-in-time algorithms such as Monte Carlo methods wait for episode completion. Neither is uniformly better, and the choice interacts with function approximation, discount factor, and reward density.

Exploration. The agent must sometimes take actions whose expected immediate return under the current policy is suboptimal in order to gather information that may reveal a better policy. The multi-armed bandit setting of article two provides the cleanest analysis of the exploration-exploitation trade-off, with regret bounds of the form

$$
R_T = \mathcal{O}(\sqrt{K T \log T})
\tag{36}
$$

for $K$-armed problems over horizon $T$ under optimistic algorithms such as upper confidence bound, which selects at time $t$ the arm

$$
a_t = \arg\max_a \left[ \hat{Q}_t(a) + c \sqrt{\frac{\ln t}{N_t(a)}} \right]
\tag{37}
$$

where $\hat{Q}\_t(a)$ is the empirical mean reward for arm $a$ and $N_t(a)$ is the count of prior pulls of arm $a$. Thompson sampling instead maintains a posterior over parameters $\theta$ and samples

$$
\tilde{\theta}_t \sim p(\theta \mid \mathcal{D}_t), \quad a_t = \arg\max_a Q(a; \tilde{\theta}_t)
\tag{38}
$$

trading exploration for exploitation through posterior uncertainty rather than optimism. Curiosity-driven exploration methods extend the analysis to structured environments by adding an intrinsic reward such as

$$
r^{\text{int}}_t = \| \hat{f}(s_t, a_t) - \phi(s_{t+1}) \|^2
\tag{39}
$$

where $\hat{f}$ is a learned forward model in a representation $\phi$ and the intrinsic reward is the prediction error. Article five treats these methods in detail.

Generalization. Function approximation is necessary in high-dimensional state or action spaces, but it introduces theoretical hazards. Off-policy learning combined with function approximation and bootstrapping produces the deadly triad that can destabilize convergence [Sutton and Barto 2018][book_sutton_barto_2018]. The original divergence-under-linear-function-approximation analysis by [Tsitsiklis and Van Roy 1997][research_tsitsiklis_van_roy_1997] gave the first formal characterization of the failure mode. Deep reinforcement learning has produced practical algorithms that manage but do not fully resolve the triad.

Non-stationarity. Real environments change over time, and the agent's own learning changes the distribution of data it collects. Continual learning aims to accumulate knowledge across tasks without catastrophic forgetting, meta-learning aims to adapt fast to new tasks by exploiting shared structure, open-ended learning aims to keep learning indefinitely as tasks arise. Articles nine, ten, and twelve treat these responses.

Reward specification. The reward function encodes the designer's intent, and the mismatch between specification and intent produces reward hacking, specification gaming, and misalignment. Preference learning, inverse reinforcement learning, and learning from demonstration in article eleven partially address the problem by inferring reward from human data rather than requiring exact specification.

Sample efficiency. Deep reinforcement learning algorithms often require millions to billions of environment interactions to reach competitive performance, a cost that dominates practical application. Model-based methods, off-policy corrections, and pretraining schemes each attempt to reduce sample complexity, treated in articles seven and eight.

Safety and robustness. Learning agents may take catastrophic exploratory actions during training, may fail to generalize to environments outside their training distribution, and may exploit adversarial vulnerabilities in learned representations. Safe exploration and robust reinforcement learning constitute active research areas at the field's applied edge.

These seven problem classes recur throughout the series. Each article treats one or more of them as its principal analytical target.

## Empirical Landscape and Benchmarks

The theoretical framework acquires its practical character through the benchmarks on which algorithms are developed and compared. Article coverage of algorithmic contributions in the series references these benchmarks throughout, and the framing here names the principal environments and the community practice around them.

Board games. Chess, Go, shogi, and poker have served as reinforcement learning testbeds since [Samuel 1959][research_samuel_1959] checkers work. [Tesauro 1995][research_tesauro_1995] TD-Gammon demonstrated that self-play temporal-difference learning could reach world-class backgammon play with a neural network policy. AlphaGo, AlphaZero, and MuZero extended the paradigm to Go, chess, shogi, and video games with progressively more general algorithmic apparatus.

Arcade games. The Arcade Learning Environment [Bellemare et al. 2013][research_bellemare_et_al_2013] provided approximately fifty-seven Atari 2600 games as a benchmark that requires learning from raw pixel input under a shared reward signal. The Deep Q-Network results of [Mnih et al. 2015][research_mnih_et_al_2015] on this suite catalyzed the deep reinforcement learning wave.

Continuous control. The MuJoCo physics engine [MuJoCo Physics Engine][ref_mujoco] and the DeepMind Control Suite provide continuous-state continuous-action robotic control benchmarks including locomotion, manipulation, and dexterous hand control. The Gymnasium framework, successor to OpenAI Gym, has become the standard interface [Farama Foundation Gymnasium][ref_farama_gymnasium].

Procedurally generated environments. Procgen [Cobbe et al. 2019][research_cobbe_et_al_2019] and its successors provide procedurally generated benchmarks that stress generalization rather than memorization. The MinAtar suite provides simplified Atari-like environments for controlled experimentation.

Simulated robotics and dexterous manipulation. Isaac Gym, Meta-World, and RoboSuite provide manipulation and dexterous control benchmarks with GPU-accelerated physics that support the throughput required for modern algorithms.

Real-world robotics. Physical robot benchmarks including real-robot manipulation, quadruped locomotion, and drone control provide the ultimate empirical test but are constrained by cost, safety, and time. Sim-to-real transfer techniques and domain randomization partially bridge simulation and reality.

Language and dialogue. Reinforcement learning from human feedback has produced a class of large language model post-training methods that use preference data rather than reward signals directly. These methods sit at the boundary of the applications scope this series excludes and the theoretical apparatus articles eleven and fifteen treat.

Community practice includes standardized benchmarks with defined evaluation protocols, open-source implementations such as those in Stable Baselines and CleanRL, and reproducibility guidelines that address the observation of [Henderson et al. 2018][research_henderson_et_al_2018] that reinforcement learning results are often more variable across random seeds and implementations than reported summary statistics suggest.

## Series Roadmap

The sixteen articles proceed as follows. Each is a comprehensive science-and-theory survey rather than an application or tutorial. The full analytical framework recurs across the articles, and cross-references between them use series metadata rather than forward-in-time references so that each article stands alone.

Article one, this article, is the framing.

Article two treats bandits and online learning, the pre-Markov-decision-process foundation of experiential learning. Multi-armed bandits, contextual bandits, regret theory, upper confidence bound algorithms, and Thompson sampling. Anchors include Robbins 1952, Lai and Robbins 1985, Auer Cesa-Bianchi and Fischer 2002, and Thompson 1933.

Article three treats reinforcement learning foundations. Markov decision processes, dynamic programming, Monte Carlo methods, temporal-difference learning, Q-learning, SARSA, policy gradients, and actor-critic. The canonical algorithmic and mathematical apparatus. Anchors include Sutton and Barto 2018, Watkins 1989, and Williams 1992.

Article four treats deep reinforcement learning. Function approximation with neural networks, deep Q-networks, policy-gradient methods at scale including trust-region and proximal policy optimization, and self-play in AlphaGo and AlphaZero. Anchors include Mnih et al 2015, Silver et al 2016 and 2017, Schulman et al 2015 and 2017.

Article five treats exploration, intrinsic motivation, and curiosity. Count-based and pseudocount methods, prediction-error curiosity, empowerment, and information-gain objectives. Anchors include Schmidhuber's decades-long program, Oudeyer and Kaplan, Bellemare et al 2016, and Pathak et al 2017.

Article six treats hierarchical reinforcement learning. The options framework, MAXQ, feudal networks, planning at multiple timescales, and semi-Markov decision processes. Anchors include Sutton Precup Singh 1999, Dietterich 2000, and Dayan and Hinton 1993.

Article seven treats world models and predictive, model-based adaptation. Model-based reinforcement learning, learned latent dynamics, planning with learned models, and the connection to predictive coding in neuroscience. Anchors include Sutton 1991, Ha and Schmidhuber 2018, and Rao and Ballard 1999.

Article eight treats offline and batch reinforcement learning. Learning from a fixed dataset without further interaction, distributional shift, importance sampling, conservative Q-learning, and behavior regularization. Anchors include Precup Sutton Singh 2000, Levine et al 2020, and Kumar et al 2020.

Article nine treats meta-learning and online adaptation. Learning to learn, few-shot adaptation, context-conditioned policies, and fast online adaptation. Anchors include Schmidhuber's program, Hochreiter et al 2001, and Finn et al 2017.

Article ten treats continual and lifelong learning. Catastrophic forgetting, the stability-plasticity dilemma, elastic weight consolidation, generative replay, and progressive networks. Anchors include McCloskey and Cohen 1989, French 1999, Ring 1994, Thrun 1998, Kirkpatrick et al 2017, and Rusu et al 2016.

Article eleven treats learning from demonstration, preference, and other agents. Imitation learning, inverse reinforcement learning, preference and human-feedback learning, and multi-agent adaptation. Anchors include Ng and Russell 2000, Abbeel and Ng 2004, and Christiano et al 2017.

Article twelve treats evolutionary and open-ended adaptation. Evolutionary strategies, neuroevolution, quality-diversity, and developmental and open-ended learning. Anchors include Holland, Stanley and Miikkulainen 2002, Lehman and Stanley, and Salimans et al 2017.

Article thirteen treats embodied cognition and developmental learning. Sensorimotor contingencies, developmental robotics, morphological computation, and the tight coupling of body and cognition. Anchors include Pfeifer and Bongard 2007, Smith and Gasser 2005, Weng et al 2001, and O'Regan and Noë 2001.

Article fourteen treats NeuroAI. Dopamine and temporal-difference reward-prediction error, hippocampal replay and experience replay, complementary learning systems, predictive coding, the free-energy principle and active inference, and neuromodulation. Anchors include Schultz Dayan Montague 1997, McClelland McNaughton and O'Reilly 1995, Rao and Ballard 1999, Friston, and Zador et al 2023.

Article fifteen treats the psychology of learning. Law of effect, operant and classical conditioning, the Rescorla-Wagner model and its correspondence to temporal-difference learning, model-free and model-based control as habitual and goal-directed behavior, and bounded rationality. Anchors include Thorndike 1911, Skinner 1938, Rescorla and Wagner 1972, Daw Niv and Dayan 2005, and Simon.

Article sixteen synthesizes the series and separates the established public interdisciplinary knowledge from the genuinely open problems, delineating what is settled public domain versus active research at the closing of the series's editorial window.

## Load-Bearing Open Questions

- What is the correct formal object for experiential learning under partial observability at scales beyond the tractable POMDP? History-conditioned policies, recurrent state representations, and world models each capture aspects of the problem, but no single formalism dominates.
- Under what conditions does the deadly triad of off-policy learning, function approximation, and bootstrapping fail to destabilize? Empirical practice has assembled workarounds, but the theoretical characterization remains incomplete.
- What is the right treatment of the exploration-exploitation trade-off in high-dimensional structured environments where bandit regret bounds do not tighten usefully? Intrinsic motivation methods provide practical mechanisms without matching theoretical guarantees.
- How closely do neural implementations of reinforcement learning in animal brains correspond to machine learning algorithms, and where do the correspondences break?
- What formal apparatus captures open-ended learning in the sense that human cultures and evolutionary systems exhibit? Neither reinforcement learning nor evolutionary algorithms fully model open-endedness.
- To what extent can reward specification failures be repaired by preference learning and inverse reinforcement learning as opposed to by improving the reward specification directly?

These questions recur throughout the series and are revisited in the closing synthesis.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 39 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 39, 39 are established and 0 are bespoke.
Returns, values and regret carry the units of the reward signal, while discount factors, step sizes and probabilities are dimensionless, and time is counted in discrete decision steps rather than in seconds.

**Equation 1, Markov Decision Process as a Tuple.**
A Markov decision process is specified by its state space, action space, transition kernel, reward function, discount factor and initial state distribution.
[Sutton and Barto 2018][book_sutton_barto_2018]

$$
\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, R, \gamma, \mu_0)
\tag{1}
$$

**Equation 2, Transition Kernel.**
The transition kernel gives the distribution of the next state conditional on the current state and action.

$$
P(s_{t+1} \mid s_t, a_t)
\tag{2}
$$

**Equation 3, Markov Property.**
Conditioning the next state on the full history gives the same distribution as conditioning on the most recent state and action alone.

$$
P(s_{t+1} \mid s_t, a_t, s_{t-1}, a_{t-1}, \ldots, s_0, a_0) = P(s_{t+1} \mid s_t, a_t)
\tag{3}
$$

**Equation 4, Stochastic Policy as a Distribution over Actions.**
A stochastic policy assigns each action a non-negative probability, and these probabilities sum to one in every state.

$$
\sum_a \pi(a \mid s) = 1, \quad \pi(a \mid s) \geq 0
\tag{4}
$$

**Equation 5, Discounted Return.**
The return from a step is the sum of all later rewards, each weighted by the discount factor raised to its delay.

$$
G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k+1}
\tag{5}
$$

**Equation 6, Average Reward Objective.**
For a continuing task the policy is judged by the long-run expected reward per step rather than by a discounted sum.

$$
J_{\text{avg}}(\pi) = \lim_{T \to \infty} \frac{1}{T} \mathbb{E}_{\pi} \left[ \sum_{t=0}^{T-1} r_{t+1} \right]
\tag{6}
$$

**Equation 7, Trajectory Distribution Induced by a Policy.**
The probability of a trajectory factorises into the initial state probability and the product of policy and transition probabilities along it.

$$
p_{\pi}(\tau) = \mu_0(s_0) \prod_{t=0}^{\infty} \pi(a_t \mid s_t) P(s_{t+1} \mid s_t, a_t)
\tag{7}
$$

**Equation 8, Observation Kernel of a Partially Observable Process.**
In a partially observable Markov decision process the agent receives an observation drawn from a distribution conditioned on the hidden state.

$$
O(o_t \mid s_t)
\tag{8}
$$

**Equation 9, Rescorla-Wagner Update.**
The associative strength of each conditioned stimulus moves in proportion to the difference between the reinforcement magnitude and the summed strengths of all stimuli present.
[Rescorla and Wagner 1972][research_rescorla_wagner_1972]

$$
\Delta V_i = \alpha_i \beta \left( \lambda - \sum_j V_j \right)
\tag{9}
$$

**Equation 10, Independent and Identically Distributed Training Sample.**
In batch supervised learning each labelled example is drawn independently from one fixed distribution.

$$
(x_i, y_i) \stackrel{\text{iid}}{\sim} \mathcal{D}, \quad i = 1, \ldots, n
\tag{10}
$$

**Equation 11, Empirical Risk.**
The empirical risk of a predictor is its loss averaged over the training sample.

$$
\hat{R}(f) = \frac{1}{n} \sum_{i=1}^n L(f(x_i), y_i)
\tag{11}
$$

**Equation 12, Policy Dependence of the State Distribution.**
Two different policies generally visit states with different frequencies, so the data an agent collects depends on its own behaviour.

$$
d^{\pi}(s) \neq d^{\pi'}(s) \quad \text{in general when} \quad \pi \neq \pi'
\tag{12}
$$

**Equation 13, Probably Approximately Correct Generalisation Bound.**
A probably approximately correct bound states that the true risk exceeds the empirical risk by more than a tolerance with probability at most a stated confidence level.

$$
P\left( R(f) - \hat{R}(f) > \epsilon \right) \leq \delta
\tag{13}
$$

**Equation 14, Conditional Value at Risk of the Return.**
The conditional value at risk is the expected return over the lower tail of outcomes at or below the chosen quantile.

$$
\text{CVaR}_\alpha[G] = \mathbb{E}[G \mid G \leq q_\alpha(G)]
\tag{14}
$$

**Equation 15, Cumulative Regret.**
Regret sums over the horizon the shortfall of the reward received against the reward a reference policy would have obtained.

$$
R_T = \sum_{t=1}^T \left( r^*_t - r_t \right)
\tag{15}
$$

**Equation 16, Empowerment.**
Empowerment is the largest mutual information that any policy can achieve between a sequence of actions and the state it leads to from a given state.

$$
\mathfrak{E}(s) = \max_{\pi} I(A_{t:t+k} ; S_{t+k} \mid S_t = s)
\tag{16}
$$

**Equation 17, State Value Function.**
The value of a state under a policy is the expected return from that state when the policy is followed.

$$
V^{\pi}(s) = \mathbb{E}_{\pi} \left[ G_t \mid s_t = s \right]
\tag{17}
$$

**Equation 18, Action Value Function.**
The action value is the expected return from taking a given action in a given state and following the policy thereafter.

$$
Q^{\pi}(s, a) = \mathbb{E}_{\pi} \left[ G_t \mid s_t = s, a_t = a \right]
\tag{18}
$$

**Equation 19, Bellman Expectation Equation.**
The value of a state equals the policy-weighted expectation of the immediate reward plus the discounted value of the successor state.

$$
V^{\pi}(s) = \sum_a \pi(a \mid s) \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V^{\pi}(s') \right]
\tag{19}
$$

**Equation 20, Bellman Optimality Equation for State Values.**
The optimal value of a state is the best expected immediate reward plus discounted optimal value of the successor over all actions.
[Puterman 1994][book_puterman_1994]

$$
V^*(s) = \max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V^*(s') \right]
\tag{20}
$$

**Equation 21, Bellman Optimality Equation for Action Values.**
The optimal action value is the expected immediate reward plus the discounted best action value available in the successor state.
[Puterman 1994][book_puterman_1994]

$$
Q^*(s, a) = \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma \max_{a'} Q^*(s', a') \right]
\tag{21}
$$

**Equation 22, Greedy Policy from Optimal Action Values.**
An optimal policy selects in each state an action that maximises the optimal action value.

$$
\pi^*(s) = \arg\max_a Q^*(s, a)
\tag{22}
$$

**Equation 23, Advantage Function.**
The advantage of an action is its action value less the value of the state under the policy.

$$
A^{\pi}(s, a) = Q^{\pi}(s, a) - V^{\pi}(s)
\tag{23}
$$

**Equation 24, Contraction of the Bellman Expectation Operator.**
Applying the Bellman expectation operator shrinks the largest difference between two value functions by at least the discount factor.

$$
\| T^{\pi} V - T^{\pi} V' \|_{\infty} \leq \gamma \| V - V' \|_{\infty}
\tag{24}
$$

**Equation 25, Temporal-Difference Error.**
The temporal-difference error is the reward plus the discounted estimate of the next state less the estimate of the current state.

$$
\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)
\tag{25}
$$

**Equation 26, Tabular One-Step Temporal-Difference Update.**
The value estimate of the visited state moves by a step size times the temporal-difference error.
[Sutton 1988][research_sutton_1988]

$$
V(s_t) \leftarrow V(s_t) + \alpha \delta_t
\tag{26}
$$

**Equation 27, SARSA Update.**
SARSA moves the action value toward a target built from the action the agent actually takes next, which makes it an on-policy method.

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t) \right]
\tag{27}
$$

**Equation 28, Q-Learning Update.**
Q-learning moves the action value toward a target built from the best action value in the next state, which makes it an off-policy method.
[Watkins 1989][research_watkins_1989]

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t) \right]
\tag{28}
$$

**Equation 29, Policy Gradient Theorem.**
The gradient of expected return is the expectation of the score function of the policy weighted by the action value.
[Williams 1992][research_williams_1992]

$$
\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \sum_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, Q^{\pi_\theta}(s_t, a_t) \right]
\tag{29}
$$

**Equation 30, Advantage Form of the Policy Gradient.**
Subtracting the state value as a baseline replaces the action value by the advantage without biasing the gradient and reduces its variance.

$$
\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \sum_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, A^{\pi_\theta}(s_t, a_t) \right]
\tag{30}
$$

**Equation 31, Value Iteration.**
Value iteration applies the Bellman optimality operator to the current estimate and converges geometrically to the optimal value.
[Bellman 1957][book_bellman_1957]

$$
V_{k+1}(s) = \max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V_k(s') \right]
\tag{31}
$$

**Equation 32, Policy Improvement Step.**
Policy iteration replaces the current policy by the policy that is greedy with respect to its evaluated value function.
[Howard 1960][book_howard_1960]

$$
\pi_{k+1}(s) = \arg\max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V^{\pi_k}(s') \right]
\tag{32}
$$

**Equation 33, Constant Step Monte Carlo Update.**
Monte Carlo estimation moves the value of a state toward the full return observed after visiting it.

$$
V(s) \leftarrow V(s) + \alpha \left[ G_t - V(s) \right]
\tag{33}
$$

**Equation 34, Per-Step Importance Sampling Ratio.**
The ratio of target to behaviour policy probabilities for the action taken reweights off-policy data toward the target policy.

$$
\rho_t = \frac{\pi(a_t \mid s_t)}{\mu(a_t \mid s_t)}
\tag{34}
$$

**Equation 35, Variational Free Energy.**
The variational free energy equals the Kullback-Leibler divergence from the recognition distribution to the true posterior minus the log evidence, so minimising it both improves inference and bounds surprise.
[Friston 2010][research_friston_2010]

$$
F = \mathbb{E}_{q(s)} \left[ \log q(s) - \log p(o, s) \right] = D_{\text{KL}}(q(s) \, \| \, p(s \mid o)) - \log p(o)
\tag{35}
$$

**Equation 36, Gap-Free Regret of Optimistic Bandit Algorithms.**
Optimistic algorithms on a $K$-armed bandit incur regret growing no faster than the square root of $K T \log T$ over horizon $T$.

$$
R_T = \mathcal{O}(\sqrt{K T \log T})
\tag{36}
$$

**Equation 37, Upper Confidence Bound Action Selection.**
The upper confidence bound rule picks the arm whose empirical mean plus an exploration bonus that shrinks with its pull count is largest.

$$
a_t = \arg\max_a \left[ \hat{Q}_t(a) + c \sqrt{\frac{\ln t}{N_t(a)}} \right]
\tag{37}
$$

**Equation 38, Thompson Sampling.**
Thompson sampling draws parameters from the posterior and acts greedily with respect to the draw.

$$
\tilde{\theta}_t \sim p(\theta \mid \mathcal{D}_t), \quad a_t = \arg\max_a Q(a; \tilde{\theta}_t)
\tag{38}
$$

**Equation 39, Forward-Model Prediction Error Curiosity Reward.**
The intrinsic reward is the squared error of a learned forward model in predicting the embedding of the next state.

$$
r^{\text{int}}_t = \| \hat{f}(s_t, a_t) - \phi(s_{t+1}) \|^2
\tag{39}
$$

### Notation

- $\mathcal{S}$, the state space
- $\mathcal{A}$, the action space
- $\gamma$, the discount factor, between zero and one
- $\mu_0$, the initial state distribution
- $\pi(a \mid s)$, the probability that the policy selects action $a$ in state $s$
- $\mu(a_t \mid s_t)$, the behaviour policy that generated off-policy data
- $G_t$, the discounted return from step $t$
- $d^{\pi}(s)$, the marginal state distribution induced by policy $\pi$
- $V^{\pi}(s)$, the state value function under policy $\pi$
- $Q^{\pi}(s, a)$, the action value function under policy $\pi$
- $A^{\pi}(s, a)$, the advantage function under policy $\pi$
- $T^{\pi}$, the Bellman expectation operator for policy $\pi$
- $\delta_t$, the temporal-difference error at step $t$
- $\alpha$, the step size in an update rule, the conditioned stimulus salience in the Rescorla-Wagner model and the tail level in the conditional value at risk
- $\rho_t$, the per-step importance sampling ratio
- $V_j$, the associative strength of conditioned stimulus $j$
- $\lambda$, the maximum associative strength the reinforcer supports
- $q_\alpha(G)$, the lower $\alpha$-quantile of the return distribution
- $R_T$, the cumulative regret over horizon $T$
- $N_t(a)$, the number of prior pulls of arm $a$
- $\mathfrak{E}(s)$, the empowerment of state $s$
- $q(s)$, the approximate posterior, or recognition distribution, over hidden states
- $p(o, s)$, the generative model of observations and hidden states
- $\phi$, the learned state representation in which curiosity is measured

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Friston, Karl. 2010. "The Free-Energy Principle: A Unified Brain Theory?" *Nature Reviews Neuroscience* 11 (2): 127–38. [https://doi.org/10.1038/nrn2787][research_friston_2010]
- McCulloch, Warren S., and Walter Pitts. 1943. "A Logical Calculus of the Ideas Immanent in Nervous Activity." *Bulletin of Mathematical Biophysics* 5 (4): 115–33. [https://doi.org/10.1007/bf02478259][research_mcculloch_pitts_1943]
- Mnih, Volodymyr, Koray Kavukcuoglu, David Silver, et al. 2015. "Human-Level Control through Deep Reinforcement Learning." *Nature* 518 (7540): 529–33. [https://doi.org/10.1038/nature14236][research_mnih_et_al_2015]
- Silver, David, Aja Huang, Chris J. Maddison, et al. 2016. "Mastering the Game of Go with Deep Neural Networks and Tree Search." *Nature* 529 (7587): 484–89. [https://doi.org/10.1038/nature16961][research_silver_et_al_2016]
- Silver, David, Julian Schrittwieser, Karen Simonyan, et al. 2017. "Mastering the Game of Go without Human Knowledge." *Nature* 550 (7676): 354–59. [https://doi.org/10.1038/nature24270][research_silver_et_al_2017]
- Sutton, Richard S. 1988. "Learning to Predict by the Methods of Temporal Differences." *Machine Learning* 3 (1): 9–44. [https://doi.org/10.1007/bf00115009][research_sutton_1988]
- Williams, Ronald J. 1992. "Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning." *Machine Learning* 8 (3–4): 229–56. [https://doi.org/10.1007/bf00992696][research_williams_1992]

### Primary Sources, Non-Peer-Reviewed

- Bellemare, M. G., Y. Naddaf, J. Veness, and M. Bowling. 2013. "The Arcade Learning Environment: An Evaluation Platform for General Agents." *Journal of Artificial Intelligence Research* 47: 253–79. [https://doi.org/10.1613/jair.3912][research_bellemare_et_al_2013]
- Cobbe, Karl, Christopher Hesse, Jacob Hilton, and John Schulman. 2019. "Leveraging Procedural Generation to Benchmark Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1912.01588][research_cobbe_et_al_2019]
- "DeepMind Control Suite." n.d. github.com. Accessed October 25, 2026. [https://github.com/deepmind/dm\_control][ref_dm_control_suite]
- Henderson, Peter, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup, and David Meger. 2018. "Deep Reinforcement Learning That Matters." *Proceedings of the AAAI Conference on Artificial Intelligence* 32 (1). [https://doi.org/10.1609/aaai.v32i1.11694][research_henderson_et_al_2018]
- Kaelbling, L. P., M. L. Littman, and A. W. Moore. 1996. "Reinforcement Learning: A Survey." *Journal of Artificial Intelligence Research* 4: 237–85. [https://doi.org/10.1613/jair.301][research_kaelbling_littman_moore_1996]
- Klopf, A. H. 1972. "Brain Function and Adaptive Systems: A Heterostatic Theory." DTIC, March 3. [https://apps.dtic.mil/sti/citations/AD0742259][research_klopf_1972]
- McClelland, James L., Bruce L. McNaughton, and Randall C. O'Reilly. 1995. "Why There Are Complementary Learning Systems in the Hippocampus and Neocortex: Insights from the Successes and Failures of Connectionist Models of Learning and Memory." *Psychological Review* 102 (3): 419–57. [https://doi.org/10.1037/0033-295x.102.3.419][research_mcclelland_mcnaughton_oreilly_1995]
- Schultz, Wolfram, Peter Dayan, and P. Read Montague. 1997. "A Neural Substrate of Prediction and Reward." *Science* 275 (5306): 1593–99. [https://doi.org/10.1126/science.275.5306.1593][research_schultz_dayan_montague_1997]
- Tesauro, Gerald. 1995. "Temporal Difference Learning and TD-Gammon." *Communications of the ACM* 38 (3): 58–68. [https://doi.org/10.1145/203330.203343][research_tesauro_1995]

### Secondary Sources

- Anderson, John Robert. 2007. *How Can the Human Mind Occur in the Physical Universe?*. Oxford University Press, Incorporated. [https://global.oup.com/academic/product/how-can-the-human-mind-occur-in-the-physical-universe-9780195398953][book_anderson_2007]
- Ashby. 1952. *\[Title not identified\]*. [https://archive.org/details/designforbrain00ashb][book_ashby_1952]
- Bellman. 1957. *Dynamic Programming Princeton Landmarks in Mathematics*. Princeton University Press. [https://press.princeton.edu/books/paperback/9780691146683/dynamic-programming][book_bellman_1957]
- Bertsekas. 2019. *\[Title not identified\]*. [http://www.athenasc.com/rlbook.html][book_bertsekas_2019]
- Bertsekas, Dimitri P., and Tsitsiklis. 1996. *Neuro-Dynamic Programming*. Athena Scientific. [http://www.athenasc.com/ndpbook.html][book_bertsekas_tsitsiklis_1996]
- Dayan, Peter, and L. F. Abbott. 2001. *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems*. Massachusetts Institute of Technology Press. [https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/][book_dayan_abbott_2001]
- Hebb, D. O. 1949. *The Organization of Behavior; a Neuropsychological Theory*. Wiley. [https://psycnet.apa.org/record/1950-02200-000][book_hebb_1949]
- Howard, Ronald Arthur. 1960. *Dynamic Programming and Markov Processes*. MIT Press. [https://mitpress.mit.edu/9780262080095/dynamic-programming-and-markov-processes/][book_howard_1960]
- Newell, Allen. 1990. *Unified Theories of Cognition (the William James Lectures)*. Harvard University Press. [https://www.hup.harvard.edu/books/9780674921016][book_newell_1990]
- Pavlov. 1927. *\[Title not identified\]*. [https://openlibrary.org/search?q=Pavlov+1927][book_pavlov_1927]
- Piaget. 1936. *\[Title not identified\]*. [https://www.routledge.com/The-Origin-of-Intelligence-in-the-Child/Piaget/p/book/9780415846394][book_piaget_1936]
- Puterman, Martin L. 1994. *Markov Decision Processes: Discrete Stochastic Dynamic Programming*. Wiley. [https://doi.org/10.1002/9780470316887][book_puterman_1994]
- Simon, Herbert Alexander. 1969. *The Sciences of the Artificial*. M.I.T. Press. [https://mitpress.mit.edu/9780262691918/the-sciences-of-the-artificial/][book_simon_1969]
- Skinner. 1938. *Behavior of Organisms (1991 Edition)*. [https://www.bfskinner.org/product/the-behavior-of-organisms/][book_skinner_1938]
- Sutton, Richard S., and Barto. 2018. *Reinforcement Learning: An Introduction*. MIT Press. [http://incompleteideas.net/book/the-book-2nd.html][book_sutton_barto_2018]
- Szepesvari. 2010. *Algorithms of Reinforcement Learning*. [https://sites.ualberta.ca/~szepesva/rlbook.html][book_szepesvari_2010]
- Thorndike, Edward L. , 1874-1949. 1911. *Animal Intelligence; Experimental Studies*. New York, The Macmillan company. [https://archive.org/details/animalintelligen00thor][book_thorndike_1911]
- Wiener, Norbert. 1948. *Cybernetics, or Control and Communication in the Animal and the Machine*. The M.i.t. Press. [https://mitpress.mit.edu/9780262730099/cybernetics/][book_wiener_1948]

### Commercial Sources

- "DeepMind x UCL RL Course." n.d. Accessed October 25, 2026. [https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021][ref_deepmind_ucl_rl]
- "Welcome to Spinning up in Deep RL! — Spinning up Documentation." n.d. Accessed October 25, 2026. [https://spinningup.openai.com/][ref_openai_spinning_up]

### General Sources

- Barto, Sutton, and Anderson. 1983. "\[Title not identified\]." Accessed October 25, 2026. [https://ieeexplore.ieee.org/document/6313077][research_barto_sutton_anderson_1983]
- "Berkeley CS285." n.d. Accessed October 25, 2026. [https://rail.eecs.berkeley.edu/deeprlcourse/][ref_berkeley_cs285]
- "CleanRL." n.d. Accessed October 25, 2026. [https://docs.cleanrl.dev/][ref_cleanrl]
- "Farama Foundation Gymnasium." n.d. Accessed October 25, 2026. [https://gymnasium.farama.org/][ref_farama_gymnasium]
- Minsky. 1961. "\[Title not identified\]." Accessed October 25, 2026. [https://ieeexplore.ieee.org/document/4066245][research_minsky_1961]
- "MuJoCo Physics Engine." n.d. Accessed October 25, 2026. [https://mujoco.org/][ref_mujoco]
- Rescorla and Wagner. 1972. "\[Title not identified\]." Accessed October 25, 2026. [https://sites.ualberta.ca/~egray/teaching/Rescorla%20&%20Wagner%201972.pdf][research_rescorla_wagner_1972]
- Samuel. 1959. "\[Title not identified\]." Accessed October 25, 2026. [https://ieeexplore.ieee.org/document/5392560][research_samuel_1959]
- "Silver RL Course UCL." n.d. Accessed October 25, 2026. [https://www.davidsilver.uk/teaching/][ref_silver_rl_course]
- "Stable-Baselines3 Docs: Reliable Reinforcement Learning Implementations — Stable Baselines3 2.8.0a1 Documentation." n.d. Accessed October 25, 2026. [https://stable-baselines3.readthedocs.io/][ref_stable_baselines]
- "Stanford CS234." n.d. Accessed October 25, 2026. [https://web.stanford.edu/class/cs234/][ref_stanford_cs234]
- "Sutton and Barto Second Edition PDF." n.d. Accessed October 25, 2026. [http://incompleteideas.net/book/RLbook2020.pdf][ref_sutton_barto_pdf]
- Tsitsiklis and Van Roy. 1997. "\[Title not identified\]." Accessed October 25, 2026. [https://ieeexplore.ieee.org/document/580874][research_tsitsiklis_van_roy_1997]
- Watkins. 1989. "Q-Learning." [https://www.cs.rhul.ac.uk/~chrisw/new\_thesis.pdf][research_watkins_1989]
- Widrow and Hoff. 1960. "\[Title not identified\]." Accessed October 25, 2026. [https://www-isl.stanford.edu/~widrow/papers/c1960adaptiveswitching.pdf][research_widrow_hoff_1960]

[book_anderson_2007]: https://global.oup.com/academic/product/how-can-the-human-mind-occur-in-the-physical-universe-9780195398953
[book_ashby_1952]: https://archive.org/details/designforbrain00ashb
[book_bellman_1957]: https://press.princeton.edu/books/paperback/9780691146683/dynamic-programming
[book_bertsekas_2019]: http://www.athenasc.com/rlbook.html
[book_bertsekas_tsitsiklis_1996]: http://www.athenasc.com/ndpbook.html
[book_dayan_abbott_2001]: https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/
[book_hebb_1949]: https://psycnet.apa.org/record/1950-02200-000
[book_howard_1960]: https://mitpress.mit.edu/9780262080095/dynamic-programming-and-markov-processes/
[book_newell_1990]: https://www.hup.harvard.edu/books/9780674921016
[book_pavlov_1927]: https://openlibrary.org/search?q=Pavlov+1927
[book_piaget_1936]: https://www.routledge.com/The-Origin-of-Intelligence-in-the-Child/Piaget/p/book/9780415846394
[book_puterman_1994]: https://doi.org/10.1002/9780470316887
[book_simon_1969]: https://mitpress.mit.edu/9780262691918/the-sciences-of-the-artificial/
[book_skinner_1938]: https://www.bfskinner.org/product/the-behavior-of-organisms/
[book_sutton_barto_2018]: http://incompleteideas.net/book/the-book-2nd.html
[book_szepesvari_2010]: https://sites.ualberta.ca/~szepesva/rlbook.html
[book_thorndike_1911]: https://archive.org/details/animalintelligen00thor
[book_wiener_1948]: https://mitpress.mit.edu/9780262730099/cybernetics/
[ref_berkeley_cs285]: https://rail.eecs.berkeley.edu/deeprlcourse/
[ref_cleanrl]: https://docs.cleanrl.dev/
[ref_deepmind_ucl_rl]: https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021
[ref_dm_control_suite]: https://github.com/deepmind/dm_control
[ref_farama_gymnasium]: https://gymnasium.farama.org/
[ref_mujoco]: https://mujoco.org/
[ref_openai_spinning_up]: https://spinningup.openai.com/
[ref_silver_rl_course]: https://www.davidsilver.uk/teaching/
[ref_stable_baselines]: https://stable-baselines3.readthedocs.io/
[ref_stanford_cs234]: https://web.stanford.edu/class/cs234/
[ref_sutton_barto_pdf]: http://incompleteideas.net/book/RLbook2020.pdf
[research_barto_sutton_anderson_1983]: https://ieeexplore.ieee.org/document/6313077
[research_bellemare_et_al_2013]: https://doi.org/10.1613/jair.3912
[research_cobbe_et_al_2019]: https://doi.org/10.48550/arxiv.1912.01588
[research_friston_2010]: https://doi.org/10.1038/nrn2787
[research_henderson_et_al_2018]: https://doi.org/10.1609/aaai.v32i1.11694
[research_kaelbling_littman_moore_1996]: https://doi.org/10.1613/jair.301
[research_klopf_1972]: https://apps.dtic.mil/sti/citations/AD0742259
[research_mcclelland_mcnaughton_oreilly_1995]: https://doi.org/10.1037/0033-295x.102.3.419
[research_mcculloch_pitts_1943]: https://doi.org/10.1007/bf02478259
[research_minsky_1961]: https://ieeexplore.ieee.org/document/4066245
[research_mnih_et_al_2015]: https://doi.org/10.1038/nature14236
[research_rescorla_wagner_1972]: https://sites.ualberta.ca/~egray/teaching/Rescorla%20&%20Wagner%201972.pdf
[research_samuel_1959]: https://ieeexplore.ieee.org/document/5392560
[research_schultz_dayan_montague_1997]: https://doi.org/10.1126/science.275.5306.1593
[research_silver_et_al_2016]: https://doi.org/10.1038/nature16961
[research_silver_et_al_2017]: https://doi.org/10.1038/nature24270
[research_sutton_1988]: https://doi.org/10.1007/bf00115009
[research_tesauro_1995]: https://doi.org/10.1145/203330.203343
[research_tsitsiklis_van_roy_1997]: https://ieeexplore.ieee.org/document/580874
[research_watkins_1989]: https://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf
[research_widrow_hoff_1960]: https://www-isl.stanford.edu/~widrow/papers/c1960adaptiveswitching.pdf
[research_williams_1992]: https://doi.org/10.1007/bf00992696
