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

$$\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, R, \gamma, \mu_0)$$

where $\mathcal{S}$ is the state space, $\mathcal{A}$ is the action space, $P$ is the transition kernel, $R$ is the reward function, $\gamma \in [0, 1)$ is the discount factor, and $\mu_0$ is the initial state distribution. The transition kernel

$$P(s_{t+1} \mid s_t, a_t)$$

satisfies the Markov property, meaning that the distribution of $s_{t+1}$ conditional on the full history $(s_0, a_0, \ldots, s_t, a_t)$ depends only on the most recent state and action,

$$P(s_{t+1} \mid s_t, a_t, s_{t-1}, a_{t-1}, \ldots, s_0, a_0) = P(s_{t+1} \mid s_t, a_t)$$

The reward at step $t+1$ is drawn from a distribution $R(r_{t+1} \mid s_t, a_t, s_{t+1})$ or in deterministic settings from a function $r(s_t, a_t)$.

The agent selects actions according to a policy $\pi$, which is either a deterministic function $\pi : \mathcal{S} \to \mathcal{A}$ or a stochastic function $\pi(a \mid s)$ giving a probability distribution over actions with

$$\sum_a \pi(a \mid s) = 1, \quad \pi(a \mid s) \geq 0$$

The agent's objective is to select a policy that maximizes the expected discounted return

$$G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k+1}$$

where $\gamma \in [0, 1)$ is a discount factor that trades off immediate against delayed reward. For episodic tasks the sum is finite and the discount factor may be one. An alternative objective is the average reward per step,

$$J_{\text{avg}}(\pi) = \lim_{T \to \infty} \frac{1}{T} \mathbb{E}_{\pi} \left[ \sum_{t=0}^{T-1} r_{t+1} \right]$$

which is appropriate for continuing tasks where discounting is inappropriate.

The policy $\pi$ induces a joint distribution over trajectories $\tau = (s_0, a_0, r_1, s_1, a_1, r_2, \ldots)$ given by

$$p_{\pi}(\tau) = \mu_0(s_0) \prod_{t=0}^{\infty} \pi(a_t \mid s_t) P(s_{t+1} \mid s_t, a_t)$$

and induces a marginal state distribution $d^{\pi}(s)$ obtained by summing this joint over histories.

Two additional formalizations are worth naming at the outset. The partially observable Markov decision process replaces direct state observation by an observation $o_t$ drawn from an observation kernel

$$O(o_t \mid s_t)$$

with the agent obliged to maintain a belief state $b_t(s) = P(s_t = s \mid o_1, a_1, \ldots, o_t)$ or a sufficient statistic of history to act well. The contextual bandit reduces the problem to a single decision at each step under a contextual signal, with no dynamics linking successive states. Both objects appear in later articles.

The agent-environment loop unifies problems that appear disparate at first inspection. Robot manipulation, board game play, dialogue policy learning, adaptive experimental design, animal foraging, and organizational strategy all instantiate the same abstract structure, differing only in the identities of $\mathcal{S}$, $\mathcal{A}$, $R$, and $P$. This unification is at once the field's greatest theoretical strength and its most seductive trap. Later articles will treat the settings in which the loop's assumptions are load-bearing and those in which they are approximations. [Sutton and Barto 2018][book_sutton_barto_2018] provides the canonical modern treatment of the loop as the organizing formalism of reinforcement learning.

## Historical Roots

The agent-environment loop as a research object descends from several parallel developments. Behaviorist psychology under [Pavlov 1927][book_pavlov_1927] work on conditional reflex, [Thorndike 1911][book_thorndike_1911] law of effect, and [Skinner 1938][book_skinner_1938] operant conditioning identified reinforcement as the mechanism by which animal behavior adapts to consequences, laying the empirical foundation for what came to be called instrumental or operant conditioning. The [Rescorla and Wagner 1972][research_rescorla_wagner_1972] model formalized classical conditioning as prediction-error-driven associative learning and would later be shown to correspond mathematically to temporal-difference learning. Cybernetics under [Wiener 1948][book_wiener_1948] and [Ashby 1952][book_ashby_1952] framed adaptation as feedback control across biological, mechanical, and social systems.

The neural side of the story runs in parallel. [McCulloch and Pitts 1943][research_mcculloch_pitts_1943] introduced the threshold neuron model that set the direction for computational neuroscience and neural-network machine learning alike. [Hebb 1949][book_hebb_1949] proposed the associative learning rule that neurons which fire together wire together, providing the foundational learning principle for Hebbian and later contrastive learning approaches. [Minsky 1961][research_minsky_1961] surveyed the problem structure of artificial intelligence and identified reinforcement learning as one of its central pillars. [Klopf 1972][research_klopf_1972] hedonistic neuron proposal explicitly connected reinforcement learning ideas to single-neuron computation and directly influenced the Barto-Sutton program.

Dynamic programming under [Bellman 1957][book_bellman_1957] gave the recursive mathematical structure that would later underpin reinforcement learning's core algorithms, and Howard's [Howard 1960][book_howard_1960] policy iteration extended dynamic programming to Markov decision processes with an explicit policy object. In the same period, [Samuel 1959][research_samuel_1959] implemented an early self-play learning system for checkers that anticipated modern reinforcement learning by decades, and [Widrow and Hoff 1960][research_widrow_hoff_1960] introduced the least-mean-squares adaptive filter that provided one of the earliest online learning rules.

The synthesis emerged in the 1980s. Sutton's [Sutton 1988][research_sutton_1988] temporal-difference learning connected animal learning experiments to computable algorithms via the Rescorla-Wagner model, whose associative strength update

$$\Delta V_i = \alpha_i \beta \left( \lambda - \sum_j V_j \right)$$

expresses conditioning as a prediction-error-driven adjustment of associative strengths $V_j$ toward the reinforcement magnitude $\lambda$. Watkins's [Watkins 1989][research_watkins_1989] Q-learning provided the first convergence-guaranteed reinforcement learning algorithm for tabular control. Williams's [Williams 1992][research_williams_1992] REINFORCE established the policy gradient theorem's practical form. Barto, Sutton, and Anderson's [Barto Sutton Anderson 1983][research_barto_sutton_anderson_1983] actor-critic architecture drew on neuroscience for its inspiration. By the mid 1990s the [Kaelbling Littman Moore 1996][research_kaelbling_littman_moore_1996] survey codified reinforcement learning as a distinct field, and [Bertsekas and Tsitsiklis 1996][book_bertsekas_tsitsiklis_1996] provided its mathematical foundations under the label neuro-dynamic programming.

The 2010s produced deep reinforcement learning through the marriage of the classical algorithms with neural function approximation. [Mnih et al 2015][research_mnih_et_al_2015] deep Q-networks demonstrated human-level Atari game play from pixels. [Silver et al 2016][research_silver_et_al_2016] AlphaGo defeated Lee Sedol in Go. [Silver et al 2017][research_silver_et_al_2017] AlphaZero achieved superhuman performance in chess, shogi, and Go from self-play alone. Article three in this series treats the deep reinforcement learning wave in detail.

Alongside these algorithmic developments, the neuroscience of reward learning uncovered striking parallels. [Schultz Dayan Montague 1997][research_schultz_dayan_montague_1997] identified midbrain dopamine neurons as encoding a reward prediction error mathematically identical to the temporal-difference error, launching the modern era of computational neuroscience-machine learning cross-fertilization. Article fourteen surveys this bridge under the emerging label NeuroAI.

## Learning From Experience Versus Batch Learning

Supervised batch learning, which dominates contemporary machine learning practice, poses a fundamentally different problem. In batch supervised learning, a training set $\{(x_i, y_i)\}_{i=1}^n$ is drawn independently and identically distributed from a fixed distribution $\mathcal{D}$,

$$(x_i, y_i) \stackrel{\text{iid}}{\sim} \mathcal{D}, \quad i = 1, \ldots, n$$

and the objective is to fit a function $f : \mathcal{X} \to \mathcal{Y}$ that minimizes an empirical risk

$$\hat{R}(f) = \frac{1}{n} \sum_{i=1}^n L(f(x_i), y_i)$$

as a proxy for the true risk $R(f) = \mathbb{E}_{(x,y) \sim \mathcal{D}}[L(f(x), y)]$. The learner does not choose which $x_i$ to observe, the data distribution does not change over training, the objective decomposes into per-sample losses, and the assumptions of statistical learning theory permit generalization bounds under standard capacity control.

Experiential learning violates each of these conditions.

First, the data distribution depends on the agent's own behavior. If the agent's policy changes, the state distribution over which it collects data changes as well,

$$d^{\pi}(s) \neq d^{\pi'}(s) \quad \text{in general when} \quad \pi \neq \pi'$$

This coupling breaks the independence assumption underlying most concentration bounds in statistical learning theory and forces reasoning about the joint distribution of policy and data.

Second, the objective is not a per-sample loss but a return that depends on a temporally extended trajectory. Credit assignment across a sequence of actions requires attributing reward to actions taken possibly many steps earlier. The temporal-difference and policy-gradient algorithms of the next articles are the field's principal tools for this attribution problem.

Third, the agent must choose what data to collect. The exploration-exploitation trade-off, formalized in the multi-armed bandit setting treated in article two, forces the agent to balance obtaining reward under the current best policy against gathering information that may reveal a better policy. There is no batch supervised analog to this trade-off because the batch already exists.

Fourth, the environment may be non-stationary. State transitions, reward distributions, or task specifications may change over the agent's lifetime. The continual and lifelong learning literature treated in article ten develops the algorithmic responses to non-stationarity, and the meta-learning literature in article nine develops learning-to-learn approaches that seek to adapt fast to distributional shift.

Fifth, the interaction may be adversarial or multi-agent. Other learning agents adapt in response to the learner's own adaptations, producing the game-theoretic dynamics treated in article eleven. Even single-agent problems can become effectively adversarial when the reward function is misspecified and the agent optimizes against the specification rather than the intent.

These five departures make experiential learning theoretically distinct from batch supervised learning rather than merely a special case. Statistical learning theory in the supervised setting provides probably approximately correct (PAC) generalization bounds of the form

$$P\left( R(f) - \hat{R}(f) > \epsilon \right) \leq \delta$$

for hypothesis class complexity control, sample size $n$, and confidence $\delta$. The corresponding sample-complexity theory for reinforcement learning replaces $\epsilon$ with suboptimality of the learned policy and $n$ with the number of environment interactions. Foundational results include the PAC-MDP framework and its subsequent refinements. Article three treats the sample-complexity landscape for tabular and function-approximation reinforcement learning. The rest of this series treats each departure in depth.

## The Six-Axis Analytical Framework

Subsequent articles in the series treat the field along six analytical axes that recur throughout. Naming them here provides a shared vocabulary for cross-article comparison.

The first axis is signal. The learner may receive a full reward function at every step (dense reward), a reward only at episode termination (sparse reward), a preference between trajectories rather than a scalar reward (preference learning), a demonstration of desired behavior (imitation), or an intrinsic motivation signal computed from its own predictions (curiosity). Different signals require different algorithms and impose different sample-efficiency constraints.

The second axis is objective. The learner may optimize expected discounted return (the classical MDP objective), long-run average reward, distributional characteristics of return such as variance or conditional value at risk

$$\text{CVaR}_\alpha[G] = \mathbb{E}[G \mid G \leq q_\alpha(G)]$$

where $q_\alpha$ denotes the $\alpha$-quantile of the return distribution (risk-sensitive objectives treated in article four's extensions), regret against a reference policy

$$R_T = \sum_{t=1}^T \left( r^*_t - r_t \right)$$

or an information-theoretic objective such as empowerment, the maximum mutual information between an action sequence and the resulting state,

$$\mathfrak{E}(s) = \max_{\pi} I(A_{t:t+k} ; S_{t+k} \mid S_t = s)$$

The choice of objective changes the algorithmic surface substantially.

The third axis is structure. The learner may face a flat Markov decision process, a partially observable Markov decision process, a hierarchical Markov decision process with options or sub-policies, a factored state space, a multi-agent stochastic game, or a partially observable stochastic game. Article six treats hierarchical structure directly, and article twelve treats multi-agent structure.

The fourth axis is model. The learner may be model-free, using only samples from the environment to update a policy or value function, model-based, learning an internal model of the environment to plan with, or model-implicit, using a learned representation that supports planning without an explicit generative model. Article seven treats model-based reinforcement learning and world models in detail.

The fifth axis is interaction. The learner may be online, collecting data from the environment as it learns, offline, learning from a fixed dataset of prior experience without further interaction, on-policy, using data collected under the current policy, or off-policy, using data collected under other policies. Article eight treats offline reinforcement learning and its distributional shift problem.

The sixth axis is adaptation. The learner may face a stationary task, a non-stationary task with drifting distribution, a task family with rapid adaptation required for each new task, or an open-ended stream of tasks with no clear end. Articles nine and ten treat meta-learning and continual learning respectively, and article twelve treats open-ended and evolutionary approaches.

Each subsequent article in the series positions its subject along these six axes explicitly, and the synthesis article at the end of the series maps the whole field onto this framework.

## Foundational Formal Objects

Before proceeding to the topics of subsequent articles, the framing article names the formal objects that recur throughout.

The state value function under a policy $\pi$ is the expected return from state $s$ under $\pi$,

$$V^{\pi}(s) = \mathbb{E}_{\pi} \left[ G_t \mid s_t = s \right]$$

The action value function or Q function under $\pi$ is the expected return from state $s$ taking action $a$ and thereafter following $\pi$,

$$Q^{\pi}(s, a) = \mathbb{E}_{\pi} \left[ G_t \mid s_t = s, a_t = a \right]$$

The Bellman expectation equation gives the recursive relationship

$$V^{\pi}(s) = \sum_a \pi(a \mid s) \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V^{\pi}(s') \right]$$

and the Bellman optimality equation gives

$$V^*(s) = \max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V^*(s') \right]$$

An optimal policy $\pi^*$ is any policy achieving $V^{\pi^*} = V^*$ at every state. Existence of optimal deterministic policies is guaranteed for finite MDPs under standard conditions [Puterman 1994][book_puterman_1994]. The corresponding Bellman optimality equation for the action value function is

$$Q^*(s, a) = \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma \max_{a'} Q^*(s', a') \right]$$

and an optimal policy is recovered by the greedy rule

$$\pi^*(s) = \arg\max_a Q^*(s, a)$$

The advantage function measures how much better action $a$ is than the average action under $\pi$,

$$A^{\pi}(s, a) = Q^{\pi}(s, a) - V^{\pi}(s)$$

and appears as a variance-reduction baseline in policy-gradient methods. The Bellman expectation operator $T^{\pi}$ acting on value functions is a $\gamma$-contraction under the sup norm,

$$\| T^{\pi} V - T^{\pi} V' \|_{\infty} \leq \gamma \| V - V' \|_{\infty}$$

which by the Banach fixed-point theorem guarantees a unique fixed point $V^{\pi}$ and convergence of value iteration.

Temporal-difference learning updates a value estimate $V(s_t)$ using the sampled TD error

$$\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$$

toward its target $r_{t+1} + \gamma V(s_{t+1})$ with step size $\alpha$,

$$V(s_t) \leftarrow V(s_t) + \alpha \delta_t$$

The corresponding action-value update rules are SARSA,

$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t) \right]$$

and Q-learning,

$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t) \right]$$

which differ in whether the target uses the actual next action (SARSA, on-policy) or the maximizing next action (Q-learning, off-policy).

The policy gradient theorem gives the gradient of the expected return $J(\theta) = \mathbb{E}_{\pi_\theta}[G_0]$ under a parameterized policy $\pi_\theta$,

$$\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \sum_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, Q^{\pi_\theta}(s_t, a_t) \right]$$

which underlies the REINFORCE algorithm and its many descendants including actor-critic, trust-region policy optimization, and proximal policy optimization treated in articles three and four. Variance reduction by subtracting a state-dependent baseline $b(s_t)$ gives the advantage form

$$\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \sum_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, A^{\pi_\theta}(s_t, a_t) \right]$$

which uses the advantage function defined above.

The classical planning algorithms proceed by iterating the Bellman operator. Value iteration applies the optimality operator directly,

$$V_{k+1}(s) = \max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V_k(s') \right]$$

converging to $V^*$ from any initial $V_0$ at a geometric rate governed by $\gamma$. Policy iteration alternates policy evaluation, which solves the Bellman expectation equation for the current policy, and policy improvement, which sets

$$\pi_{k+1}(s) = \arg\max_a \sum_{s', r} P(s', r \mid s, a) \left[ r + \gamma V^{\pi_k}(s') \right]$$

and converges to $\pi^*$ in a finite number of iterations for finite MDPs. When the environment model is unavailable, Monte Carlo estimation replaces the expectation with sample averages from full episodes,

$$V(s) \leftarrow V(s) + \alpha \left[ G_t - V(s) \right]$$

where $G_t$ is the actual return observed from state $s$ at time $t$. Temporal-difference learning bootstraps a partial estimate rather than waiting for episode completion.

For off-policy learning, importance sampling corrects for the mismatch between the behavior policy $\mu$ that generated the data and the target policy $\pi$ being evaluated. The per-step ratio is

$$\rho_t = \frac{\pi(a_t \mid s_t)}{\mu(a_t \mid s_t)}$$

and the trajectory-level ratio $\rho_{t:T} = \prod_{k=t}^{T} \rho_k$ appears in the importance-sampling estimator of the value function. Article eight develops the practical consequences of importance-sampling variance for offline learning.

These objects recur throughout the series. Articles two through five build the classical and deep reinforcement learning apparatus around them.

## The Mind Sciences Boundary

The hardest open problems in adaptive learning cluster at the boundary with neuroscience and psychology of learning. The bridge runs in both directions.

From machine learning to the mind sciences, temporal-difference learning provided the computational hypothesis that unified [Schultz Dayan Montague 1997][research_schultz_dayan_montague_1997] a wealth of behavioral and electrophysiological data on midbrain dopamine as a reward prediction error. Actor-critic architectures aligned with the anatomy of basal ganglia loops. Hippocampal experience replay [McClelland McNaughton O'Reilly 1995][research_mcclelland_mcnaughton_oreilly_1995] parallels the experience-replay buffers that stabilize deep reinforcement learning.

From the mind sciences to machine learning, the developmental robotics literature draws on [Piaget 1936][book_piaget_1936] constructivism and on developmental psychology to argue for staged, embodied learning. Predictive processing and active inference [Friston 2010][research_friston_2010] frame the brain as a hierarchical prediction machine that minimizes a variational free energy,

$$F = \mathbb{E}_{q(s)} \left[ \log q(s) - \log p(o, s) \right] = D_{\text{KL}}(q(s) \, \| \, p(s \mid o)) - \log p(o)$$

where $q(s)$ is a recognition distribution over hidden states and $p(o, s)$ is a generative model of observations and hidden states. Active inference extends the framing to action by treating action selection as minimization of expected free energy over future outcomes. The framing has produced influential models of perception, action selection, and interoception, and overlaps with model-based reinforcement learning in ways treated in articles seven and fourteen. Cognitive architectures such as SOAR [Newell 1990][book_newell_1990], ACT-R [Anderson 2007][book_anderson_2007], and CLARION carry decades of cognitive-psychology insight into computational form. [Simon 1969][book_simon_1969] treatment of bounded rationality provides an early framing of intelligence as constrained optimization under limited computational resources that has since informed both artificial intelligence and behavioral economics.

The reciprocal traffic between these fields is neither purely metaphorical nor a straightforward mapping. Machine learning models often abstract away neural implementation constraints that are load-bearing for the brain, and mind-sciences models often invoke functional decompositions whose computational realization is contested. Articles thirteen and fourteen treat these frictions directly, and article fifteen surveys the psychology of learning literature that has shaped the field's algorithmic vocabulary.

## The Hard Problems

The characteristic difficulty of experiential learning can be located in five recurring problem classes.

Credit assignment. When an agent receives a reward after a temporally extended sequence of actions, the question of which actions were responsible for the reward is the temporal credit assignment problem. Backward-in-time algorithms such as temporal-difference learning and eligibility traces distribute credit through bootstrapping, forward-in-time algorithms such as Monte Carlo methods wait for episode completion. Neither is uniformly better, and the choice interacts with function approximation, discount factor, and reward density.

Exploration. The agent must sometimes take actions whose expected immediate return under the current policy is suboptimal in order to gather information that may reveal a better policy. The multi-armed bandit setting of article two provides the cleanest analysis of the exploration-exploitation trade-off, with regret bounds of the form

$$R_T = \mathcal{O}(\sqrt{K T \log T})$$

for $K$-armed problems over horizon $T$ under optimistic algorithms such as upper confidence bound, which selects at time $t$ the arm

$$a_t = \arg\max_a \left[ \hat{Q}_t(a) + c \sqrt{\frac{\ln t}{N_t(a)}} \right]$$

where $\hat{Q}_t(a)$ is the empirical mean reward for arm $a$ and $N_t(a)$ is the count of prior pulls of arm $a$. Thompson sampling instead maintains a posterior over parameters $\theta$ and samples

$$\tilde{\theta}_t \sim p(\theta \mid \mathcal{D}_t), \quad a_t = \arg\max_a Q(a; \tilde{\theta}_t)$$

trading exploration for exploitation through posterior uncertainty rather than optimism. Curiosity-driven exploration methods extend the analysis to structured environments by adding an intrinsic reward such as

$$r^{\text{int}}_t = \| \hat{f}(s_t, a_t) - \phi(s_{t+1}) \|^2$$

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

Arcade games. The Arcade Learning Environment [Bellemare et al 2013][research_bellemare_et_al_2013] provided approximately fifty-seven Atari 2600 games as a benchmark that requires learning from raw pixel input under a shared reward signal. The Deep Q-Network results of [Mnih et al 2015][research_mnih_et_al_2015] on this suite catalyzed the deep reinforcement learning wave.

Continuous control. The MuJoCo physics engine [MuJoCo Physics Engine][ref_mujoco] and the DeepMind Control Suite provide continuous-state continuous-action robotic control benchmarks including locomotion, manipulation, and dexterous hand control. The Gymnasium framework, successor to OpenAI Gym, has become the standard interface [Farama Foundation Gymnasium][ref_farama_gymnasium].

Procedurally generated environments. Procgen [Cobbe et al 2019][research_cobbe_et_al_2019] and its successors provide procedurally generated benchmarks that stress generalization rather than memorization. The MinAtar suite provides simplified Atari-like environments for controlled experimentation.

Simulated robotics and dexterous manipulation. Isaac Gym, Meta-World, and RoboSuite provide manipulation and dexterous control benchmarks with GPU-accelerated physics that support the throughput required for modern algorithms.

Real-world robotics. Physical robot benchmarks including real-robot manipulation, quadruped locomotion, and drone control provide the ultimate empirical test but are constrained by cost, safety, and time. Sim-to-real transfer techniques and domain randomization partially bridge simulation and reality.

Language and dialogue. Reinforcement learning from human feedback has produced a class of large language model post-training methods that use preference data rather than reward signals directly. These methods sit at the boundary of the applications scope this series excludes and the theoretical apparatus articles eleven and fifteen treat.

Community practice includes standardized benchmarks with defined evaluation protocols, open-source implementations such as those in Stable Baselines and CleanRL, and reproducibility guidelines that address the observation of [Henderson et al 2018][research_henderson_et_al_2018] that reinforcement learning results are often more variable across random seeds and implementations than reported summary statistics suggest.

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

## References

### Books

- [Anderson 2007][book_anderson_2007]
- [Ashby 1952][book_ashby_1952]
- [Bellman 1957][book_bellman_1957]
- [Bertsekas 2019][book_bertsekas_2019]
- [Bertsekas and Tsitsiklis 1996][book_bertsekas_tsitsiklis_1996]
- [Dayan and Abbott 2001][book_dayan_abbott_2001]
- [Hebb 1949][book_hebb_1949]
- [Howard 1960][book_howard_1960]
- [Newell 1990][book_newell_1990]
- [Pavlov 1927][book_pavlov_1927]
- [Piaget 1936][book_piaget_1936]
- [Puterman 1994][book_puterman_1994]
- [Simon 1969][book_simon_1969]
- [Skinner 1938][book_skinner_1938]
- [Sutton and Barto 2018][book_sutton_barto_2018]
- [Szepesvari 2010][book_szepesvari_2010]
- [Thorndike 1911][book_thorndike_1911]
- [Wiener 1948][book_wiener_1948]

### Reference

- [Berkeley CS285][ref_berkeley_cs285]
- [CleanRL][ref_cleanrl]
- [DeepMind Control Suite][ref_dm_control_suite]
- [DeepMind x UCL RL Course][ref_deepmind_ucl_rl]
- [Farama Foundation Gymnasium][ref_farama_gymnasium]
- [MuJoCo Physics Engine][ref_mujoco]
- [OpenAI Spinning Up][ref_openai_spinning_up]
- [Silver RL Course UCL][ref_silver_rl_course]
- [Stable Baselines3][ref_stable_baselines]
- [Stanford CS234][ref_stanford_cs234]
- [Sutton and Barto Second Edition PDF][ref_sutton_barto_pdf]

### Research

- [Barto Sutton Anderson 1983][research_barto_sutton_anderson_1983]
- [Bellemare et al 2013][research_bellemare_et_al_2013]
- [Cobbe et al 2019][research_cobbe_et_al_2019]
- [Friston 2010][research_friston_2010]
- [Henderson et al 2018][research_henderson_et_al_2018]
- [Kaelbling Littman Moore 1996][research_kaelbling_littman_moore_1996]
- [Klopf 1972][research_klopf_1972]
- [McClelland McNaughton O'Reilly 1995][research_mcclelland_mcnaughton_oreilly_1995]
- [McCulloch and Pitts 1943][research_mcculloch_pitts_1943]
- [Minsky 1961][research_minsky_1961]
- [Mnih et al 2015][research_mnih_et_al_2015]
- [Rescorla and Wagner 1972][research_rescorla_wagner_1972]
- [Samuel 1959][research_samuel_1959]
- [Schultz Dayan Montague 1997][research_schultz_dayan_montague_1997]
- [Silver et al 2016][research_silver_et_al_2016]
- [Silver et al 2017][research_silver_et_al_2017]
- [Sutton 1988][research_sutton_1988]
- [Tesauro 1995][research_tesauro_1995]
- [Tsitsiklis and Van Roy 1997][research_tsitsiklis_van_roy_1997]
- [Watkins 1989][research_watkins_1989]
- [Widrow and Hoff 1960][research_widrow_hoff_1960]
- [Williams 1992][research_williams_1992]

[book_anderson_2007]: https://global.oup.com/academic/product/how-can-the-human-mind-occur-in-the-physical-universe-9780195398953
[book_ashby_1952]: https://archive.org/details/designforbrain00ashb
[book_bellman_1957]: https://press.princeton.edu/books/paperback/9780691146683/dynamic-programming
[book_bertsekas_2019]: http://www.athenasc.com/rlbook.html
[book_bertsekas_tsitsiklis_1996]: http://www.athenasc.com/ndpbook.html
[book_dayan_abbott_2001]: https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/
[book_hebb_1949]: https://psycnet.apa.org/record/1950-02200-000
[book_howard_1960]: https://mitpress.mit.edu/9780262080095/dynamic-programming-and-markov-processes/
[book_newell_1990]: https://www.hup.harvard.edu/books/9780674921016
[book_pavlov_1927]: https://archive.org/details/conditionedrefle00pavl
[book_piaget_1936]: https://www.routledge.com/The-Origin-of-Intelligence-in-the-Child/Piaget/p/book/9780415846394
[book_puterman_1994]: https://onlinelibrary.wiley.com/doi/book/10.1002/9780470316887
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
[research_bellemare_et_al_2013]: https://www.jair.org/index.php/jair/article/view/10819
[research_cobbe_et_al_2019]: https://arxiv.org/abs/1912.01588
[research_friston_2010]: https://www.nature.com/articles/nrn2787
[research_henderson_et_al_2018]: https://ojs.aaai.org/index.php/AAAI/article/view/11694
[research_kaelbling_littman_moore_1996]: https://www.jair.org/index.php/jair/article/view/10166
[research_klopf_1972]: https://apps.dtic.mil/sti/citations/AD0742259
[research_mcclelland_mcnaughton_oreilly_1995]: https://psycnet.apa.org/record/1995-42327-001
[research_mcculloch_pitts_1943]: https://link.springer.com/article/10.1007/BF02478259
[research_minsky_1961]: https://ieeexplore.ieee.org/document/4066245
[research_mnih_et_al_2015]: https://www.nature.com/articles/nature14236
[research_rescorla_wagner_1972]: https://sites.ualberta.ca/~egray/teaching/Rescorla%20&%20Wagner%201972.pdf
[research_samuel_1959]: https://ieeexplore.ieee.org/document/5392560
[research_schultz_dayan_montague_1997]: https://www.science.org/doi/10.1126/science.275.5306.1593
[research_silver_et_al_2016]: https://www.nature.com/articles/nature16961
[research_silver_et_al_2017]: https://www.nature.com/articles/nature24270
[research_sutton_1988]: https://link.springer.com/article/10.1007/BF00115009
[research_tesauro_1995]: https://dl.acm.org/doi/10.1145/203330.203343
[research_tsitsiklis_van_roy_1997]: https://ieeexplore.ieee.org/document/580874
[research_watkins_1989]: https://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf
[research_widrow_hoff_1960]: https://www-isl.stanford.edu/~widrow/papers/c1960adaptiveswitching.pdf
[research_williams_1992]: https://link.springer.com/article/10.1007/BF00992696
