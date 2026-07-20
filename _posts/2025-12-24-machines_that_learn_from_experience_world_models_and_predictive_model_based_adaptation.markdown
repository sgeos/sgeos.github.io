---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: World Models and Predictive, Model-Based Adaptation"
date:   2025-12-24 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 7
---

<!-- A256 -->
<script>console.log("A256");</script>

Model-based reinforcement learning treats the transition and reward structure of the environment as objects that can be learned, represented, and used for planning, rather than relying exclusively on sampled experience for policy improvement. A learned world model provides an internal simulator that supports data augmentation, forward planning, uncertainty quantification, and transfer across tasks in ways that model-free methods do not. This article surveys the science and theory of model-based reinforcement learning and its predictive-coding bridge to neuroscience as they stand in the mid 2020s, covering the Dyna and prioritized-sweeping foundations of the tabular era, the neural network dynamics models and their uncertainty-quantification variants that constitute the modern deep model-based reinforcement learning apparatus, the Dreamer series and MuZero as canonical world-model architectures, model-based policy optimization frameworks, the predictive coding framework of Rao and Ballard and its active-inference and free-energy-principle extensions, and world models in contemporary foundation models. Articles two through six treated the model-free apparatus at length; this article treats the parallel model-based line that has produced sample-efficiency advantages and neuroscience-aligned frameworks that model-free methods do not straightforwardly replicate.

## The Case for Model-Based Reinforcement Learning

Model-based reinforcement learning offers several potential advantages over the model-free apparatus treated in prior articles. Sample efficiency is the most frequently-cited advantage: a learned model amortizes real-environment experience across many simulated rollouts, permitting substantial policy updates with modest real-experience budgets. Transfer across tasks is another advantage: a world model learned in one task can be reused for planning against different reward functions or goal specifications, provided the transition structure remains stable.

Uncertainty quantification is a third advantage. Because a learned model can be probed for its uncertainty at arbitrary states, an agent can use this signal to drive exploration (article five) or to constrain policy updates to states where the model is trustworthy. Interpretability is a fourth: an explicit dynamics model provides more human-interpretable structure than the implicit policy or value function that model-free methods produce.

The disadvantages are also significant. Model bias corrupts policy updates when the learned model differs systematically from the real environment, producing policies that perform well in simulation but poorly in the real environment. Compounding errors over long rollouts amplify model bias exponentially. Model expressiveness and computational cost constrain what environments can be modeled at all, particularly for high-dimensional visual observations where dynamics models must operate in a learned latent space.

The trade-off between model-based and model-free approaches has been an enduring research theme. Empirically, model-based methods dominate on tasks with moderate horizons and structured dynamics; model-free methods dominate on tasks with long horizons, complex dynamics, or high stochasticity. The distinction is not sharp: many contemporary methods hybridize the two approaches through dyna-style architectures that combine model-based rollouts with model-free updates on the aggregated data.

## Historical Development

Model-based reinforcement learning has roots that predate the modern reinforcement learning literature. The idea that intelligent behavior depends on internal models of the world traces to [Craik 1943][book_craik_1943] Nature of Explanation, which proposed that organisms carry small-scale models of external reality within their heads. [Tolman 1948][research_tolman_1948] proposed cognitive maps as spatial internal models that support flexible navigation in rats, providing early empirical evidence for internal-model use in biological learning. Cybernetic control theory in the 1940s and 1950s treated learned or hand-specified dynamics models as central objects, and adaptive control theory of the 1970s formalized the estimation-and-control loop. [Werbos 1987][research_werbos_1987] adaptive critic architectures provided the direct precursor to modern actor-critic methods with learned models. The reinforcement learning literature reintroduced the model-based perspective through the Dyna architecture of [Sutton 1990][research_sutton_1990] and [Sutton 1991][research_sutton_1991], which interleaved real environment interaction with simulated interaction from a learned tabular model. Prioritized sweeping of [Moore and Atkeson 1993][research_moore_atkeson_1993] extended the Dyna framework with priority-queue based simulated updates, focusing computation on the parts of the state space with the largest uncertainty. Real-time dynamic programming of [Barto Bradtke and Singh 1995][research_barto_bradtke_singh_1995] combined asynchronous value iteration with actual environment traversal.

The 2000s produced Gaussian-process-based dynamics models and probabilistic model-based methods that improved sample efficiency by orders of magnitude on continuous control tasks. PILCO of [Deisenroth and Rasmussen 2011][research_deisenroth_rasmussen_2011] used Gaussian process regression on dynamics with analytic policy improvement, achieving state-of-the-art sample complexity on cart-pole and related benchmarks. The framework proved influential but scaled poorly to high-dimensional problems.

The deep learning wave of the 2010s produced neural network dynamics models and permitted model-based reinforcement learning on visual and other high-dimensional observation modalities. World Models of [Ha and Schmidhuber 2018][research_ha_schmidhuber_2018] treated a variational autoencoder for state compression, a mixture density recurrent network for latent dynamics, and a compact controller in the latent space, together forming a modular architecture that has become a template for subsequent work.

The Dreamer series of [Hafner et al 2019][research_hafner_et_al_2019], [Hafner et al 2020][research_hafner_et_al_2020], [Hafner et al 2023][research_hafner_et_al_2023] extended the latent-dynamics-plus-controller architecture with progressively more capable recurrent state-space models and actor-critic learning entirely in imagined trajectories. MuZero of [Schrittwieser et al 2020][research_schrittwieser_et_al_2020] took a distinct approach in which the learned model produces value and policy targets that support MCTS planning without predicting observations directly.

The 2020s have produced transformer-based world models including IRIS of [Micheli et al 2023][research_micheli_et_al_2023], TWM of [Robine et al 2023][research_robine_et_al_2023], and STORM of [Zhang et al 2023][research_zhang_et_al_2023], each demonstrating that autoregressive sequence modeling of tokenized trajectories provides an effective alternative to the recurrent state-space model. Foundation-model-scale world models including [Bruce et al 2024][research_bruce_et_al_2024] Genie for controllable video generation have extended the framework to generative video modeling.

Predictive coding treated later in this article provides the neuroscience-adjacent parallel line of development, with the [Rao and Ballard 1999][research_rao_ballard_1999] hierarchical predictive coding model providing the canonical treatment. The [Friston 2010][research_friston_2010] free-energy principle and active inference framework extends predictive coding to a broader theory of perception, action, and learning that overlaps substantially with model-based reinforcement learning.

## Partial Observability and Belief-Based World Models

Real environments frequently violate the full-observability assumption of the Markov decision process. A partially observable Markov decision process (POMDP) extends the MDP with an observation kernel $O(o \mid s)$ that maps hidden states to observations, and the agent must maintain a belief state over hidden states to act optimally. The POMDP formalism traces to [Kaelbling Littman Cassandra 1998][research_kaelbling_littman_cassandra_1998], which established the theoretical framework and initial algorithms.

The belief-state MDP formulation replaces the hidden state with the belief

$$b_t(s) = \Pr(s_t = s \mid o_{1:t}, a_{1:t-1})$$

updated via Bayes' rule at each step,

$$b_{t+1}(s') = \frac{O(o_{t+1} \mid s') \sum_s P(s' \mid s, a_t) b_t(s)}{\sum_{s''} O(o_{t+1} \mid s'') \sum_s P(s'' \mid s, a_t) b_t(s)}$$

The belief MDP has a fully-observed state space (the space of beliefs) but is generally infinite-dimensional and requires approximation for practical algorithms.

Sample-based belief representations avoid the intractable belief update through particle filtering. POMCP of [Silver and Veness 2010][research_silver_veness_2010] and DESPOT of [Somani Ye Hsu Lee 2013][research_somani_et_al_2013] combined Monte Carlo tree search with particle-based belief updates, achieving state-of-the-art performance on many POMDP benchmarks.

Latent-state world models treated later in this article can be interpreted as belief-based POMDP models with a learned neural belief update replacing the intractable Bayesian one. Deep Variational Reinforcement Learning of [Igl Zintgraf Le Wood Whiteson 2018][research_igl_et_al_2018] provided an explicit variational-inference-based interpretation, training a recurrent model to approximate the belief-state MDP through variational inference on observation likelihood.

The recurrent state-space model architectures of the Dreamer family treated below operationalize the belief-based framework at scale, with the recurrent state $h_t$ serving as an approximate sufficient statistic of history that supports subsequent latent-space planning.

## Model Types and Learning Objectives

Model-based reinforcement learning admits several distinct model formulations and learning objectives. The choice among them substantially affects downstream algorithmic behavior.

Forward dynamics models predict the next state given the current state and action,

$$\hat{P}_\theta(s' \mid s, a) \approx P(s' \mid s, a)$$

with parameters $\theta$ trained by maximum likelihood on collected transitions,

$$L_{\text{ML}}(\theta) = -\mathbb{E}_{(s, a, s') \sim \mathcal{D}}\!\left[\log \hat{P}_\theta(s' \mid s, a)\right]$$

or equivalently by minimizing the KL divergence between empirical and model distributions,

$$L_{\text{KL}}(\theta) = D_{\text{KL}}(P_{\text{data}}(s' \mid s, a) \, \| \, \hat{P}_\theta(s' \mid s, a))$$

For deterministic environments the model may output a point estimate; for stochastic environments the model should output a distribution.

Reward models predict the reward given state and action or state, action, and next state,

$$\hat{R}_\phi(s, a) \approx \mathbb{E}[R(s, a)]$$

trained by regression on observed rewards.

Inverse dynamics models predict the action that connects two consecutive states,

$$\hat{A}_\psi(a \mid s, s') \approx \Pr(a_t = a \mid s_t = s, s_{t+1} = s')$$

Inverse dynamics are useful for representation learning (article four's ICM used them), for planning through backchaining from desired states, and for imitation learning from state-only demonstrations.

Latent dynamics models operate in a learned latent space rather than the raw observation space. An encoder $\phi_\theta : \mathcal{O} \to \mathcal{Z}$ maps observations to latent states, and a latent transition model $\hat{P}_\zeta(z' \mid z, a)$ predicts the next latent given the current. The latent formulation supports learning on high-dimensional observations where direct next-state prediction is infeasible.

Value-equivalent models train the model to produce accurate value predictions rather than accurate observation predictions,

$$L_{\text{VE}}(\theta) = \mathbb{E}\!\left[(V_\pi(s') - V_\pi(\hat{s}'))^2\right]$$

focusing model capacity on the aspects of state relevant for control rather than on visual fidelity. MuZero and related methods pursue this direction.

Task-relevant models make similar restrictions to the state representation by conditioning on task or reward. The choice between prediction-of-observation and prediction-of-value objectives is a load-bearing design choice in modern model-based reinforcement learning.

## Classical Model-Based Methods

The Dyna architecture of [Sutton 1990][research_sutton_1990] provides the archetypal integration of model-free and model-based updates. After each real transition $(s, a, r, s')$, the agent updates its Q-function on the real transition, updates its tabular model of $\hat{P}$ and $\hat{R}$, and performs $n$ simulated Q-updates by sampling states and actions from the model. The mechanism reuses each real transition through the model,

$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[r + \gamma \max_{a'} Q(s', a') - Q(s, a)\right]$$

for real transitions and

$$Q(\tilde{s}, \tilde{a}) \leftarrow Q(\tilde{s}, \tilde{a}) + \alpha \left[\hat{R}(\tilde{s}, \tilde{a}) + \gamma \max_{a'} Q(\tilde{s}', a') - Q(\tilde{s}, \tilde{a})\right]$$

for imagined transitions $(\tilde{s}, \tilde{a}, \hat{R}(\tilde{s}, \tilde{a}), \tilde{s}')$ sampled from the model. Sample efficiency gains scale with the accuracy of the learned model and the ratio of imagined to real updates.

Prioritized sweeping extends Dyna by maintaining a priority queue of state-action pairs to update, ordered by predicted TD error magnitude. Each state-action pair $(s, a)$ is assigned a priority

$$\text{priority}(s, a) = \left| \hat{R}(s, a) + \gamma \max_{a'} Q(\hat{s}', a') - Q(s, a) \right|$$

and the algorithm sweeps the pairs with the highest priorities first. The mechanism focuses computation on the parts of the state space with the largest uncertainty about value, providing substantial acceleration in problems with sparse reward.

Real-time dynamic programming updates value estimates only along trajectories the agent actually visits, providing asymptotic guarantees while restricting computation to the reachable portion of the state space.

PILCO of Deisenroth and Rasmussen 2011 combined Gaussian process regression on the dynamics with analytic policy improvement through moment matching. The PILCO objective computes the expected long-horizon return under the Gaussian process posterior over dynamics,

$$J(\pi) = \mathbb{E}_{p, \pi, \hat{P}}\!\left[\sum_{t=0}^{T} r(s_t)\right]$$

where the expectation is taken over both policy stochasticity and posterior model uncertainty. Analytic gradients through the objective enable policy improvement via gradient ascent. PILCO achieved order-of-magnitude sample-efficiency improvements over model-free methods on cart-pole and other continuous control benchmarks.

Related Gaussian-process-based methods including Bayesian black-box optimization for reinforcement learning and Gaussian process dynamic programming were productive in the 2000s and early 2010s but were largely superseded by neural network dynamics models with the deep learning wave.

## Neural Dynamics Models

The transition to neural network dynamics models enabled deep model-based reinforcement learning on high-dimensional problems that Gaussian processes could not scale to. A deterministic neural dynamics model outputs a point prediction of the next state,

$$\hat{s}' = f_\theta(s, a)$$

trained by mean-squared-error regression on collected transitions. Stochastic neural dynamics models output a distribution, typically parameterized as a Gaussian,

$$\hat{P}_\theta(s' \mid s, a) = \mathcal{N}(s' ; \mu_\theta(s, a), \Sigma_\theta(s, a))$$

with mean and covariance networks jointly trained by maximum likelihood.

Deep neural dynamics models suffer from a compounding-error problem for long rollouts: small per-step prediction errors accumulate across time steps, producing rollout distributions that diverge substantially from the true environment distribution after many steps. The result is that policies trained against long model-based rollouts often overfit to the model's specific error patterns rather than to the true environment.

The Wang and Ba 2020 model ensemble approach reduces this failure through model-averaging across an ensemble of dynamics models trained with different random seeds, permitting per-step epistemic uncertainty quantification that constrains rollout usefulness. The [Chua Calandra McAllister Levine 2018][research_chua_calandra_mcallister_levine_2018] Probabilistic Ensembles with Trajectory Sampling (PETS) framework combined ensembles with trajectory sampling to separate epistemic and aleatoric uncertainty in the dynamics model.

The Model-Based Policy Optimization (MBPO) framework of [Janner Fu Zhang Levine 2019][research_janner_fu_zhang_levine_2019] provides a systematic combination of neural dynamics models with off-policy actor-critic learning. MBPO uses short model-based rollouts from real states rather than long rollouts from initial states, avoiding much of the compounding-error problem while still gaining sample efficiency from the model-based data augmentation.

Feature-space dynamics models operate in a learned representation rather than the raw observation space, providing scalability to high-dimensional observations. Byravan Boots and Fox 2017 SE3-Nets learned rigid-body dynamics for object manipulation. Deep Variational Bayes Filters of [Karl Soelch Bayer van der Smagt 2017][research_karl_et_al_2017] learned probabilistic latent dynamics through variational inference over sequence models.

## Uncertainty in Learned Models

Uncertainty quantification is central to model-based reinforcement learning because it distinguishes states where the model can be trusted from states where model predictions should be discounted. The standard decomposition separates aleatoric uncertainty (irreducible stochasticity in the environment) from epistemic uncertainty (reducible model uncertainty that decreases with more data).

Bayesian methods maintain a posterior over model parameters and characterize epistemic uncertainty through the posterior variance. Full Bayesian inference is generally intractable for neural network dynamics models, but approximations including Bayesian last-layer approximations, deep ensembles, and MC-dropout provide practical proxies. Deep ensembles trained on bootstrap samples of the training data provide a widely-used and often-effective epistemic uncertainty estimate.

The PETS framework of Chua et al 2018 provides the canonical uncertainty-aware model-based method. An ensemble of probabilistic dynamics models are trained, each outputting a Gaussian over next states,

$$\hat{P}_k(s' \mid s, a) = \mathcal{N}(\mu_k(s, a), \Sigma_k(s, a))$$

The ensemble mean and variance across $K$ members provide combined estimates,

$$\bar{\mu}(s, a) = \frac{1}{K} \sum_k \mu_k(s, a), \quad \bar{\Sigma}(s, a) = \underbrace{\frac{1}{K} \sum_k \Sigma_k(s, a)}_{\text{aleatoric}} + \underbrace{\frac{1}{K} \sum_k (\mu_k - \bar{\mu})(\mu_k - \bar{\mu})^\top}_{\text{epistemic}}$$

with the first term capturing aleatoric uncertainty (the average within-ensemble variance) and the second term capturing epistemic uncertainty (the variance of ensemble means). Trajectory sampling propagates uncertainty through rollouts by resampling which ensemble member to use at each step (Trajectory Sampling 1, TS1) or by fixing the ensemble member across the trajectory (Trajectory Sampling infinity, TS-inf).

Uncertainty-aware planning uses the model's uncertainty to constrain trajectory selection. Methods include worst-case optimization (minimize the worst-case return across model realizations), CVaR optimization (minimize the expected value in the worst quantile), and confidence-bound methods (require the return to be achievable with high probability). Each approach reflects different risk preferences and different assumptions about the origin of model uncertainty.

Model-based exploration of article five uses uncertainty to drive exploration, rewarding trajectories that lead to states where the model is uncertain. Plan2Explore, disagreement-based exploration, and related methods build directly on this framework.

## Model Predictive Control and Planning

Model predictive control (MPC) uses the learned model to plan a sequence of actions over a receding horizon, executes the first action, observes the resulting state, and re-plans. The mechanism admits substantial reactivity to real-environment observations while requiring only short-horizon planning that keeps compounding model errors manageable.

The general MPC objective at state $s_t$ is

$$a_t = \arg\max_{a_{t:t+H-1}} \mathbb{E}_{\hat{P}}\!\left[\sum_{k=0}^{H-1} \gamma^k r(s_{t+k}, a_{t+k}) + \gamma^H V(s_{t+H})\right]$$

where the expectation is over model predictions, $H$ is the planning horizon, and $V(s_{t+H})$ is a learned or bootstrapped value function that estimates the return from the horizon.

Sampling-based planners including the cross-entropy method (CEM) of [Rubinstein 1997][research_rubinstein_1997], model predictive path integral (MPPI) of [Williams Aldrich and Theodorou 2017][research_williams_aldrich_theodorou_2017], and their variants sample sequences of actions from a proposal distribution, evaluate them against the model, and refine the proposal distribution based on the top-scoring samples. The CEM update rule for a Gaussian proposal $\mathcal{N}(\mu_i, \sigma_i^2)$ over action sequences is

$$\mu_{i+1} = \frac{1}{|\mathcal{E}|} \sum_{a \in \mathcal{E}} a, \quad \sigma_{i+1}^2 = \frac{1}{|\mathcal{E}|} \sum_{a \in \mathcal{E}} (a - \mu_{i+1})^2$$

where $\mathcal{E}$ is the elite set of top-scoring sampled action sequences at iteration $i$. MPPI uses a soft-max weighting rather than a hard-elite selection,

$$w_j = \frac{\exp(\lambda R_j)}{\sum_{j'} \exp(\lambda R_{j'})}, \quad \mu_{i+1} = \sum_j w_j \, a_j$$

with temperature $\lambda$ controlling the weighting sharpness. The iCEM algorithm of [Pinneri et al 2021][research_pinneri_et_al_2021] provided a widely-used variant with adaptive noise schedules and colored-noise action distributions.

Gradient-based planners exploit differentiability of the model to compute analytical gradients of return with respect to action sequences, permitting efficient trajectory optimization when the model is smooth. Methods including iterative linear quadratic regulator (iLQR) of [Todorov and Li 2005][research_todorov_li_2005] and its variants provide efficient trajectory optimization for smooth dynamics through quadratic approximation of value around a reference trajectory. Deep dynamics MPC of [Nagabandi Kahn Fearing Levine 2018][research_nagabandi_et_al_2018] combined learned neural dynamics models with random-shooting MPC and demonstrated substantial sample-efficiency gains on locomotion tasks.

Tree-search-based planners including Monte Carlo tree search (MCTS) treat planning as tree exploration over action sequences with the model providing state transitions. MuZero treated below combines learned models with MCTS for board games and Atari.

The horizon-versus-error trade-off is fundamental to model-based planning. Long horizons enable planning to distant reward but expose the planner to compounding model error. Short horizons control error but may fail to identify actions with delayed reward. Adaptive horizon selection based on model uncertainty or task structure remains an open research area.

## Planning with Search Over Learned Models

Search-based planning treats the learned model as a simulator over which action-sequence search is performed. The approach dominates on board games and structured domains where the discrete action structure supports efficient tree exploration. Search-based methods complement the sampling and gradient-based planners of the previous section, providing distinct trade-offs on tree-structured problems.

Monte Carlo tree search (MCTS) combined with learned models has produced the most striking results. MuZero of [Schrittwieser et al 2020][research_schrittwieser_et_al_2020] treated later achieved state-of-the-art performance on chess, shogi, Go, and Atari using MCTS over a learned model. Each MCTS iteration proceeds by selection, expansion, simulation, and backup phases,

$$Q(s_t, a) = \frac{1}{N(s_t, a)} \sum_{i=1}^{N(s_t, a)} G_i^{(a)}$$

with the mean-return statistic accumulating across simulations that pass through the state-action pair. Action selection at internal nodes uses the PUCT rule of article four, combining the model's predicted policy prior with the visit-count-weighted exploration bonus.

Sampled MuZero extended the approach to continuous action spaces by sampling a small set of candidate actions at each node from the learned policy prior. Efficient Zero of [Ye Liu Kurutach Abbeel Gao 2021][research_ye_liu_kurutach_abbeel_gao_2021] improved sample efficiency through several algorithmic refinements including self-supervised consistency losses on the internal state representation.

Beyond MCTS, tree-search variants including limited-depth expectimax, alpha-beta with learned evaluators, and various pruning heuristics provide alternative search structures. The choice among search algorithms depends on the structure of the environment (deterministic vs stochastic, discrete vs continuous actions) and the compute budget for planning.

Search combined with sampling-based planners produces hybrid methods that alternate tree expansion with trajectory sampling from the tree leaves. Such hybrids can capture the coverage properties of tree search with the coordinate-descent properties of sampling-based planners.

Learned models can also support one-shot planning through supervised policy distillation. Search over the model produces high-quality action targets that a supervised policy can learn to imitate, permitting the model-based improvements from search to be compressed into a fast reactive controller. This distillation-based approach underlies several practical deployments where inference-time compute budgets preclude online search.

## World Models and Learned Latent Dynamics

World models represent environment dynamics in a compact learned latent space rather than the raw observation space, permitting scalability to visual and other high-dimensional observations. The general structure combines an observation encoder, a latent transition model, and a decoder for reconstruction training.

The [Ha and Schmidhuber 2018][research_ha_schmidhuber_2018] World Models paper provided the canonical modern architecture. A variational autoencoder compresses observations to latent codes,

$$q_\phi(z_t \mid o_t), \quad p_\theta(o_t \mid z_t)$$

with the standard evidence lower bound objective

$$\text{ELBO}(\phi, \theta; o_t) = \mathbb{E}_{q_\phi}\!\left[\log p_\theta(o_t \mid z_t)\right] - D_{\text{KL}}(q_\phi(z_t \mid o_t) \, \| \, p(z_t))$$

trading observation reconstruction quality against KL divergence from the prior. A recurrent mixture density network models the temporal dynamics,

$$p_\psi(z_{t+1} \mid z_t, a_t, h_t)$$

with hidden state $h_t$ providing temporal memory. A compact controller in the latent space provides action selection,

$$a_t = \pi_\vartheta(z_t, h_t)$$

The three-component architecture separates perception (VAE), memory (RNN), and control (policy) into modules that can be trained separately or jointly.

Deep Variational Bayes Filters of Karl et al 2017 provide a related architecture with probabilistic latent state transitions. E2C of [Watter Springenberg Boedecker Riedmiller 2015][research_watter_et_al_2015] jointly learned a latent representation and a locally-linear dynamics model that permitted analytical planning in the latent space.

The Recurrent State-Space Model (RSSM) of [Hafner Lillicrap Fischer Villegas Ha Lee Davidson 2019][research_hafner_et_al_2019] PlaNet combined stochastic and deterministic components in the latent state,

$$h_t = f_\theta(h_{t-1}, z_{t-1}, a_{t-1}), \quad z_t \sim p_\theta(z_t \mid h_t)$$

with the deterministic component providing long-range memory and the stochastic component capturing environment stochasticity. The RSSM training objective combines observation reconstruction, reward prediction, and a KL regularizer between the observation-conditioned posterior and the observation-free prior,

$$L_{\text{RSSM}}(\theta) = -\mathbb{E}\!\left[\sum_t \log p_\theta(o_t \mid h_t, z_t) + \log p_\theta(r_t \mid h_t, z_t)\right] + \beta \sum_t D_{\text{KL}}(q_\phi(z_t \mid h_t, o_t) \, \| \, p_\theta(z_t \mid h_t))$$

with the KL regularizer aligning the belief maintained from observations with the belief that can be projected forward from the recurrent state alone. The RSSM has become the standard architectural pattern for latent-dynamics world models.

## The Dreamer Series

The Dreamer series of Hafner et al 2019, 2020, 2023 extends the world-model framework with actor-critic learning entirely in imagination through the learned world model. The framework has proved among the most successful modern model-based reinforcement learning approaches, achieving competitive or state-of-the-art performance across a wide range of continuous control and discrete action tasks with a single set of hyperparameters.

Dreamer of [Hafner Lillicrap Ba Norouzi 2020][research_hafner_lillicrap_ba_norouzi_2020_dreamer] introduced the imagination-based actor-critic training. The world model produces latent trajectories

$$\{(z_t, a_t, r_t)\}_{t=0}^{H}$$

by rolling out the RSSM forward from a real state $z_0$ with actions sampled from the current policy. The critic is trained to predict the $\lambda$-return over imagined trajectories,

$$V^\lambda_t = (1 - \lambda) \sum_{n=1}^{H-t-1} \lambda^{n-1} V^{(n)}_t + \lambda^{H-t-1} V^{(H-t)}_t$$

with $n$-step return $V^{(n)}_t = \sum_{k=0}^{n-1} \gamma^k \hat{r}_{t+k+1} + \gamma^n V(\hat{z}_{t+n})$, and the actor is trained on these imagined trajectories using analytic gradients through the model,

$$\nabla_\theta J_{\text{actor}}(\theta) = \nabla_\theta \sum_t \gamma^t r_t + \gamma^H V(z_H) + \eta \nabla_\theta H(\pi_\theta)$$

which is possible because the model is differentiable and the gradient flows through the model dynamics as well as the reward function. The entropy regularizer with coefficient $\eta$ prevents premature policy collapse.

DreamerV2 of [Hafner Lillicrap Norouzi Ba 2020][research_hafner_lillicrap_norouzi_ba_2020] extended the framework to Atari with a discrete latent representation and improved training stability. The discrete latent representation

$$z_t = \text{OneHot}(\arg\max_i \pi_\theta^{(i)}(h_t))$$

with straight-through estimator gradients enabled substantially larger effective latent space capacity than continuous latents while maintaining differentiability.

DreamerV3 of [Hafner Pasukonis Ba Lillicrap 2023][research_hafner_et_al_2023] provided the mature version of the framework with domain-general hyperparameter settings, achieving competitive performance across continuous control, discrete action, and video game domains without task-specific tuning. The paper demonstrated that world models had reached practical maturity as a general-purpose reinforcement learning approach.

Distributed variants including DayDreamer of [Wu Escontrela Hafner Abbeel Goldberg 2022][research_wu_et_al_2022] scaled world-model learning to real-robot learning with substantial sample efficiency advantages.

## Model-Based Policy Optimization

Model-based policy optimization frameworks combine learned models with policy optimization algorithms rather than direct planning. The approach provides the sample-efficiency advantages of model-based data augmentation while retaining the flexibility of policy-gradient or actor-critic methods.

MBPO of [Janner Fu Zhang Levine 2019][research_janner_fu_zhang_levine_2019] uses ensemble dynamics models to generate short rollouts of length $k \ll H$ starting from real states, then trains a policy (SAC) on the union of real and imagined data. The short-rollout strategy addresses the compounding-error problem while retaining substantial sample-efficiency gains, with rollout length adjusted based on model accuracy.

Model-Value Expansion (MVE) of [Feinberg Wan Stoica Jordan Gonzalez Levine 2018][research_feinberg_et_al_2018] uses fixed-length model rollouts to extend the TD target with model-based multi-step returns,

$$y_t^{\text{MVE}} = \sum_{k=0}^{H-1} \gamma^k \hat{r}_{t+k+1} + \gamma^H V(\hat{s}_{t+H})$$

providing improved value function targets for actor-critic learning. Stochastic Ensemble Value Expansion (STEVE) of [Buckman Hafner Tucker Brevdo Zoghlun 2018][research_buckman_et_al_2018] extends MVE by computing multi-step targets at multiple horizons and combining them via inverse-variance weighting,

$$y_t^{\text{STEVE}} = \frac{\sum_H (1/\sigma_H^2) \, y_t^{\text{MVE}(H)}}{\sum_H (1/\sigma_H^2)}$$

with $\sigma_H^2$ the estimated variance of the $H$-step target from the model ensemble. The mechanism provides an alternative to short rollouts for combining model-based and model-free data sources.

Model-based value gradient methods including SVG of [Heess Wayne Silver Lillicrap Erez Tassa 2015][research_heess_wayne_silver_lillicrap_erez_tassa_2015] compute analytical gradients of return through the model dynamics,

$$\nabla_\theta J(\theta) = \mathbb{E}\!\left[\sum_t \gamma^t \left(\nabla_a r(s_t, a_t) + \gamma \nabla_a V(s_{t+1}) \nabla_a f_\zeta(s_t, a_t)\right) \nabla_\theta \pi_\theta(s_t)\right]$$

providing an alternative to policy gradient that has proved effective on continuous control.

## Model-Based Meta-Learning and Rapid Adaptation

Model-based reinforcement learning provides distinctive advantages for meta-learning and rapid adaptation to new tasks, since a world model learned across a distribution of tasks can be quickly specialized to a new task using few real environment interactions. Article nine treats meta-reinforcement learning as its principal subject; this section previews the specific model-based line.

Deep online adaptation via meta-learning of [Nagabandi Clavera Liu Fearing Abbeel Levine Finn 2018][research_nagabandi_et_al_2018_meta] trains a meta-learned dynamics model that supports rapid on-line adaptation through few-shot gradient updates. The framework combines MAML-style meta-learning with model-based planning, achieving substantial adaptation efficiency on legged robots facing novel terrain.

Model-based meta-policy optimization of [Clavera Rothfuss Schulman Fujita Asfour Abbeel 2018][research_clavera_et_al_2018] trains an ensemble of dynamics models jointly with a meta-policy that can be quickly specialized to individual ensemble members. The mechanism combines uncertainty-aware planning with policy meta-learning.

Latent-variable model-based meta-learning approaches condition the world model on a latent task embedding

$$\hat{P}_\theta(s' \mid s, a, z_{\text{task}})$$

with the task embedding inferred from a short adaptation trajectory. The framework supports zero-shot generalization to new tasks that share structure with the training distribution through the shared world model.

Foundation-model-scale world models provide an extreme instantiation of the same principle: a very large model trained on many tasks generalizes to new tasks through in-context task specification rather than gradient adaptation. The relationship between meta-learned adaptation and in-context task inference in foundation models is an active research area.

## Model-Based Reinforcement Learning for Offline Data

Model-based methods have proved particularly effective for offline reinforcement learning, in which the agent must learn from a fixed dataset without further environment interaction. Article eight treats offline reinforcement learning as its principal topic; this section covers the specific model-based line.

The core observation is that a learned model can extrapolate beyond the states covered by the offline dataset, producing simulated experience at states the offline data did not visit. This extrapolation is a double-edged sword: it enables policies that improve on the behavior policy that generated the data, but it also amplifies model bias in regions where the model has not been calibrated by data.

Model-Based Offline Policy Optimization (MOPO) of [Yu et al 2020][research_yu_et_al_2020_mopo] and Model-Based Offline Reinforcement Learning (MOReL) of [Kidambi Rajeswaran Netrapalli Joachims 2020][research_kidambi_et_al_2020_morel] address this trade-off by penalizing policies that visit high-uncertainty regions of the learned model. The MOPO reward penalty takes the form

$$\tilde{r}(s, a) = \hat{r}(s, a) - \lambda \, u(s, a)$$

where $u(s, a)$ is an uncertainty estimate from the model ensemble and $\lambda$ controls the trade-off between exploiting the model and staying within its trustworthy region.

COMBO of [Yu Kumar Rafailov Rajeswaran Levine Finn 2021][research_yu_et_al_2021_combo] and RAMBO of [Rigter Lacerda Hawes 2022][research_rigter_lacerda_hawes_2022] extended the framework with conservative Q-learning integration and robust adversarial model training respectively. Each method provides different trade-offs between model exploitation and conservatism.

Empirical results on the D4RL benchmark treated in article eight show that model-based offline methods often outperform model-free offline methods when the offline dataset is small or narrowly-distributed, providing evidence for the sample-efficiency and out-of-distribution generalization advantages of model-based approaches in the offline setting.

## Distinct Model-Based Objectives

The classical objective for model learning is maximum likelihood on observed transitions, but alternative objectives can produce models more useful for control. Value-equivalent models train the model to produce accurate values rather than accurate observations,

$$L_{\text{VE}}(\theta) = \mathbb{E}\!\left[(V(s') - V(\hat{s}'))^2\right] + \eta \, \mathbb{E}\!\left[(r - \hat{r})^2\right]$$

focusing model capacity on aspects of state relevant for value prediction rather than on visual fidelity. The Predictron of [Silver Hasselt Hessel et al 2017][research_silver_hasselt_hessel_2017] and Value Prediction Networks of [Oh Singh Lee 2017][research_oh_singh_lee_2017] provided early demonstrations that a model trained end-to-end for value prediction outperforms models trained for observation prediction on control tasks. The Imagination-Augmented Agent framework of [Racaniere Weber Buchli Buesing et al 2017][research_racaniere_et_al_2017] and the fast generative models of [Buesing Weber Racaniere Rezende Reichert Viola et al 2018][research_buesing_et_al_2018] extended the idea to full generative models optimized for planning rather than reconstruction.

MuZero of [Schrittwieser et al 2020][research_schrittwieser_et_al_2020] pursues this approach. Three neural networks parameterize the learned model: a representation function that encodes past observations into an internal state, a dynamics function that predicts reward and next internal state given an action, and a prediction function that predicts policy and value from the internal state. The internal state is never grounded through observation reconstruction; instead the model is trained to produce accurate reward, value, and policy predictions along MCTS-search trajectories. MuZero achieved state-of-the-art performance across board games and Atari.

Sampled MuZero and Efficient MuZero of [Ye Liu Kurutach Abbeel Gao 2021][research_ye_liu_kurutach_abbeel_gao_2021] extended the framework to continuous action spaces and improved sample efficiency respectively.

Transformer-based world models including IRIS of [Micheli Alonso Fleuret 2023][research_micheli_et_al_2023], TWM of [Robine Hoftmann Uelwer Harmeling 2023][research_robine_et_al_2023], and STORM of [Zhang et al 2023][research_zhang_et_al_2023] tokenize trajectories and use transformer sequence models as world models. The architectural change from recurrent state-space models to transformer models has proved effective on Atari 100k where sample efficiency is the primary metric.

## Sample Complexity of Model-Based Methods

Theoretical sample complexity of model-based reinforcement learning has received substantial attention. For tabular MDPs, model-based methods achieve minimax-optimal sample complexity bounds of order

$$\tilde{\mathcal{O}}\!\left(\frac{|\mathcal{S}| |\mathcal{A}| H^3}{\epsilon^2}\right)$$

for producing an $\epsilon$-optimal policy in finite-horizon MDPs of horizon $H$, matching lower bounds up to logarithmic factors. Model-free methods generally do not achieve minimax rates in the horizon dependence, providing theoretical evidence for the sample-efficiency advantages of model-based methods.

For linear MDPs and low-rank MDPs, model-based methods with appropriate parametric assumptions achieve polynomial sample complexity bounds. Extensions to function-approximation settings continue as an active research area.

The [Kakade Wang Yang 2020][research_kakade_wang_yang_2020] work on sample efficiency of model-based reinforcement learning provided a modern systematic treatment of the theoretical advantages.

Empirical sample-complexity gains from model-based methods depend strongly on the quality of the learned model. When the model is accurate, sample efficiency gains can be one or two orders of magnitude over model-free methods. When the model is inaccurate, model-based methods can produce worse policies than model-free baselines due to model bias.

## Predictive Coding and the Bayesian Brain

Predictive coding provides a neuroscience-adjacent framework for understanding hierarchical predictive processing in biological and artificial neural systems. The [Rao and Ballard 1999][research_rao_ballard_1999] hierarchical predictive coding model of visual cortex proposed that each level of the visual hierarchy attempts to predict activity at the level below through feedback connections, with residual prediction errors propagated upward through feedforward connections. Modern reviews including [Clark 2013][research_clark_2013] Whatever Next survey the accumulated evidence for predictive processing as a general framework for perception, action, and cognition.

The Rao-Ballard equations for a two-level system involve top-down predictions

$$\hat{r}_i^{(l)} = f(W^{(l)} r^{(l+1)})$$

from level $l+1$ to level $l$ and bottom-up prediction errors

$$\epsilon^{(l)} = r^{(l)} - \hat{r}^{(l)}$$

that drive updates at both levels,

$$\dot{r}^{(l)} \propto -\epsilon^{(l)} + W^{(l+1)\top} \epsilon^{(l+1)}$$

$$\dot{W}^{(l)} \propto \epsilon^{(l)} r^{(l+1) \top}$$

for latent activity $r$ and weights $W$. The model was originally proposed as a computational account of receptive field properties in visual cortex but has since been extended to a general framework for hierarchical predictive processing.

The Bayesian brain hypothesis of [Knill and Pouget 2004][research_knill_pouget_2004] proposed that neural computation implements Bayesian inference over environmental causes of sensory observations. Predictive coding provides one algorithmic implementation of the Bayesian brain, treating the top-down predictions as expectations under a generative model and the prediction errors as updates driving posterior belief revision. [Whittington and Bogacz 2017][research_whittington_bogacz_2017] provided a systematic analysis of predictive coding as approximate Bayesian inference, and the [Bogacz 2017][research_bogacz_2017] tutorial on the free energy principle provided an accessible mathematical introduction.

The correspondence to model-based reinforcement learning is direct. The generative model at each level of a predictive coding hierarchy is a learned dynamics model in the corresponding latent space. Model-based reinforcement learning agents can be interpreted as predictive coding agents whose actions are selected to maximize expected reward under the model.

## Active Inference and the Free Energy Principle

The [Friston 2010][research_friston_2010] free energy principle extends predictive coding to a broader theory of perception, action, and learning that provides an alternative formulation of model-based reinforcement learning. The framework treats agents as minimizing a variational free energy

$$F = \mathbb{E}_{q(s)}\!\left[\log q(s) - \log p(s, o \mid m)\right] = D_{\text{KL}}(q(s) \, \| \, p(s \mid o, m)) - \log p(o \mid m)$$

where $q(s)$ is a recognition distribution over hidden states, $p(s, o \mid m)$ is a generative model of hidden states and observations, and $m$ is the model itself. Minimizing free energy through inference (updating $q$) and learning (updating $m$) implements Bayesian belief revision under the generative model.

Active inference extends the framework to action by treating action selection as free-energy minimization over future outcomes. Under the active inference framework, actions are selected to minimize expected free energy

$$G(\pi) = \mathbb{E}_{q(s, o; \pi)}\!\left[\log q(s \mid o; \pi) - \log p(s, o \mid m)\right]$$

which decomposes into an epistemic (information-gain) term and a pragmatic (reward-seeking) term,

$$G(\pi) = \underbrace{-\mathbb{E}_{q(o; \pi)}\!\left[D_{\text{KL}}(q(s \mid o, \pi) \, \| \, q(s \mid \pi))\right]}_{\text{epistemic (negative information gain)}} + \underbrace{-\mathbb{E}_{q(o; \pi)}\!\left[\log p(o \mid m)\right]}_{\text{pragmatic (negative expected utility)}}$$

The epistemic term encourages actions that reduce uncertainty about hidden states; the pragmatic term encourages actions that lead to preferred outcomes. Policies are selected via a softmax posterior over the negative expected free energy,

$$q(\pi) \propto \exp(-G(\pi))$$

providing a probabilistic action selection that trades off exploration and exploitation through a single unified criterion.

The framework provides a unified account of perception, action, and learning that has proved influential in computational neuroscience. Correspondence to model-based reinforcement learning is not exact but close: model-based reinforcement learning minimizes expected negative return under the model, while active inference minimizes expected free energy including an information-gain term. Under specific choices of the generative model and preference structure, the two frameworks coincide.

The [Tschantz Millidge Seth Buckley 2020][research_tschantz_millidge_seth_buckley_2020] and [Millidge Tschantz Buckley 2021][research_millidge_tschantz_buckley_2021] work on active inference for reinforcement learning provides a systematic translation between the frameworks. The [Buckley Kim Ma McGregor 2017][research_buckley_kim_ma_mcgregor_2017] and [Sajid Ball Friston 2021][research_sajid_ball_friston_2021] tutorials provide accessible mathematical introductions to active inference for machine learning audiences.

## World Models in Foundation Models

The rise of large language models and multimodal foundation models has produced a class of world-model-like systems that predict future observations conditional on actions or instructions. These systems blur the boundary between model-based reinforcement learning and generative modeling, and have proved effective for tasks including video prediction, controllable simulation, and embodied planning.

Genie of [Bruce et al 2024][research_bruce_et_al_2024] trained a foundation model for controllable video generation from unlabeled internet video. The model learns a discrete latent action space through inverse dynamics and generates future video conditional on these actions, producing a general-purpose interactive world model for videogame-like environments.

Video diffusion models including UniSim of [Yang Du Ghasemipour Tenenbaum Schuurmans Abbeel 2023][research_yang_du_ghasemipour_2023] treat action-conditioned video generation as a diffusion problem, generating future frames conditional on past frames and control signals. The framework connects world modeling to the diffusion generative modeling framework.

LLM-based world models use language models to predict future states or events in language-described environments. Applications include multi-step reasoning in language tasks, embodied planning with natural-language state descriptions, and simulation of social or agentic scenarios.

The scaling behavior of world models across the foundation model regime is an active area of investigation. Empirical observations suggest that world model capabilities emerge at scale in ways similar to language model capabilities, with the specific relationship between model size, training data, and downstream task performance still being characterized.

## Neuroscience of Internal Models

Internal models in biological neural systems have been extensively studied across multiple systems. Motor learning and control research established that the cerebellum learns forward models of the motor apparatus, predicting sensory consequences of motor commands to enable rapid feedback control. Foundational treatments include [Wolpert Ghahramani and Jordan 1995][research_wolpert_ghahramani_jordan_1995] on internal models for motor learning, [Miall and Wolpert 1996][research_miall_wolpert_1996] on the specific role of forward models, and [Kawato 1999][research_kawato_1999] on internal models as a general principle of motor control. The [Wolpert Miall Kawato 1998][research_wolpert_miall_kawato_1998] framework proposed a hierarchical system of forward and inverse models that supports motor skill learning and adaptation. The forward model predicts the sensory consequences of a motor command,

$$\hat{s}_{t+1} = f_{\text{forward}}(s_t, u_t)$$

and the corresponding sensory prediction error

$$\epsilon_{\text{sensory}} = s_{t+1}^{\text{observed}} - \hat{s}_{t+1}$$

drives adaptation of the forward model and provides the training signal for the inverse controller. The cerebellar prediction-error learning documented at length by [Ito 2008][research_ito_2008] has proved to be one of the clearest neural correspondences to a specific machine learning algorithm. Optimal feedback control frameworks including [Todorov and Jordan 2002][research_todorov_jordan_2002] and [Todorov 2004][research_todorov_2004] connect internal-model-based motor control to normative optimal control theory, providing the theoretical basis for understanding biological motor behavior as approximate optimal control under learned models.

Hippocampal replay treated in article three extends to model-based planning. The hippocampus generates sequences of previously-visited state representations during both awake rest and sleep, and these replayed sequences correlate with subsequent behavior in ways consistent with mental simulation for planning. The [Pfeiffer Foster 2013][research_pfeiffer_foster_2013] finding of forward hippocampal sequences preceding goal-directed navigation provides direct evidence for a model-based planning role.

The prefrontal cortex is implicated in maintaining task-relevant internal models that support planning and decision-making. Correspondence between prefrontal representations and value predictions from model-based reinforcement learning has been established through both electrophysiology and functional imaging.

The dorsolateral prefrontal cortex versus dorsomedial striatum distinction between goal-directed and habitual behavior treated in article fifteen corresponds directly to the model-based versus model-free reinforcement learning distinction. [Daw Niv Dayan 2005][research_daw_niv_dayan_2005] proposed a computational-level account of the two systems as parallel model-based and model-free learners with an arbitration mechanism that selects between them based on uncertainty.

Successor representations of [Dayan 1993][research_dayan_1993] provide an intermediate between fully model-free and fully model-based approaches, encoding expected discounted future state occupancy in a way that supports flexible re-planning when reward changes without requiring full explicit model-based simulation. Article three treated the successor representation and its neural correspondence in the hippocampus; the framework extends to hierarchical successor representations that connect to hierarchical reinforcement learning treated in article six.

## Empirical Landscape

Model-based reinforcement learning benchmarks emphasize sample efficiency, with the Atari 100k regime restricting training to 100000 environment steps as the canonical measure. On this benchmark, model-based methods including DreamerV3, EfficientZero, IRIS, TWM, and STORM substantially outperform model-free baselines, providing empirical evidence for the sample-efficiency advantages of the model-based approach.

Continuous control benchmarks including MuJoCo, DeepMind Control Suite, and MetaWorld provide the standard evaluation for model-based methods in continuous action settings. DreamerV3, MBPO, and PETS-family methods achieve competitive performance, though the relative ranking depends on specific task properties.

Real-world robotics benchmarks including DayDreamer's real-robot learning demonstrations provide the ultimate test of sample efficiency. Model-based methods have achieved substantial sample-efficiency improvements over model-free baselines in real robot learning, though the sim-to-real gap treated in article four remains a concern.

The [Wang and Ba 2020][research_wang_ba_2020] benchmarking study documented the practical performance of various model-based reinforcement learning methods across standard continuous control tasks, providing a systematic empirical comparison. The general finding is that no single model-based method dominates across all tasks, and method selection depends on task-specific properties.

## Sim-to-Real Transfer with Learned Models

Real-robot learning presents distinctive challenges for model-based reinforcement learning. Real-world data is expensive to collect, physical damage risks constrain exploration, and reset mechanisms (returning the environment to a known state) may be unavailable or costly. Model-based methods with their sample-efficiency advantages have shown promise in this regime, and specific techniques have been developed to bridge simulation and reality.

Domain randomization treated in article four extends naturally to the model-based setting. A world model trained across a distribution of simulated environments with randomized dynamics parameters can generalize to real-world dynamics that fall within the training distribution. [Rusu Vecerik Rothorl Heess Pascanu Hadsell 2017][research_rusu_et_al_2017] Sim-to-Real Robotic Reinforcement Learning provided an early demonstration of the framework applied to model-based methods.

Learning agile quadrupedal control of [Hwangbo Lee Dosovitskiy Bellicoso Tsounis Koltun Hutter 2019][research_hwangbo_et_al_2019] combined actuator identification, simulator calibration, and model-based control to achieve robust quadruped locomotion transferred from simulation to physical hardware. The approach demonstrated that careful model calibration substantially reduces the sim-to-real gap.

Domain adaptation via learned dynamics of [Chebotar Handa Makoviichuk Lu Fox Yashchuk Tremblay Birchfield Coste 2019][research_chebotar_et_al_2019] adapted a simulator's parameters to match real-world observations, closing the sim-to-real gap through explicit calibration. The framework combined simulation-based training with real-world adaptation in an iterative closed loop.

DayDreamer of Wu et al 2022 treated earlier demonstrated real-robot learning entirely from real-world experience through a learned world model, achieving substantial sample-efficiency gains without any simulation. The result provided evidence that model-based reinforcement learning has reached the sample efficiency required for practical real-robot deployment on select tasks.

Real-world robotic manipulation benchmarks including RRC of [Byravan et al 2022][research_byravan_et_al_2022] and various real-robot demonstrations have shown that model-based methods can achieve competitive performance with substantially less real-robot interaction than model-free baselines require. The gap between simulation-based demonstration and real-world deployment remains a research frontier.

## Load-Bearing Open Questions

- What is the correct trade-off between model expressiveness and computational cost in world model design? Larger models capture more environment structure but at proportionally larger compute cost.
- How can compounding model errors over long rollouts be reliably controlled? Short rollouts partially address the problem but limit the horizon over which model-based planning provides value.
- What is the correct theoretical framework for characterizing when model-based reinforcement learning provides sample-efficiency advantages? Empirical gains are substantial but theoretical characterization remains incomplete.
- How should the tension between model likelihood and value equivalence be resolved? Value-equivalent models produce compact task-relevant representations but sacrifice the flexibility that observation-predicting models provide.
- What is the correct treatment of aleatoric versus epistemic uncertainty in learned models? Practical methods conflate the two, but theoretical treatment suggests they should be handled distinctly.
- How closely do the internal models of biological brains correspond to the world models of contemporary machine learning? Correspondence at a functional level is well documented, but detailed algorithmic correspondence remains open.
- Can world models be reliably learned at foundation-model scale, and what is the correct theoretical framework for their emergent capabilities?
- How should model-based reinforcement learning be integrated with hierarchical decomposition of article six? Hierarchical world models and multi-timescale planning present distinctive challenges and opportunities.

## References

### Books

- [Craik 1943][book_craik_1943]
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
- [A255 Machines That Learn From Experience Hierarchical Reinforcement Learning][related_post_a255_hierarchical]

### Research

- [Barto Bradtke and Singh 1995][research_barto_bradtke_singh_1995]
- [Bogacz 2017][research_bogacz_2017]
- [Bruce et al 2024][research_bruce_et_al_2024]
- [Buckley Kim Ma McGregor 2017][research_buckley_kim_ma_mcgregor_2017]
- [Buckman Hafner Tucker Brevdo Zoghlun 2018][research_buckman_et_al_2018]
- [Buesing Weber Racaniere et al 2018][research_buesing_et_al_2018]
- [Byravan et al 2022][research_byravan_et_al_2022]
- [Chebotar et al 2019][research_chebotar_et_al_2019]
- [Chua Calandra McAllister Levine 2018][research_chua_calandra_mcallister_levine_2018]
- [Clark 2013][research_clark_2013]
- [Clavera Rothfuss Schulman Fujita Asfour Abbeel 2018][research_clavera_et_al_2018]
- [Daw Niv Dayan 2005][research_daw_niv_dayan_2005]
- [Dayan 1993][research_dayan_1993]
- [Deisenroth and Rasmussen 2011][research_deisenroth_rasmussen_2011]
- [Feinberg Wan Stoica Jordan Gonzalez Levine 2018][research_feinberg_et_al_2018]
- [Friston 2010][research_friston_2010]
- [Ha and Schmidhuber 2018][research_ha_schmidhuber_2018]
- [Hafner et al 2019][research_hafner_et_al_2019]
- [Hafner et al 2020][research_hafner_et_al_2020]
- [Hafner et al 2023][research_hafner_et_al_2023]
- [Hafner Lillicrap Ba Norouzi 2020][research_hafner_lillicrap_ba_norouzi_2020_dreamer]
- [Hafner Lillicrap Norouzi Ba 2020][research_hafner_lillicrap_norouzi_ba_2020]
- [Heess Wayne Silver Lillicrap Erez Tassa 2015][research_heess_wayne_silver_lillicrap_erez_tassa_2015]
- [Hwangbo Lee Dosovitskiy Bellicoso Tsounis Koltun Hutter 2019][research_hwangbo_et_al_2019]
- [Igl Zintgraf Le Wood Whiteson 2018][research_igl_et_al_2018]
- [Ito 2008][research_ito_2008]
- [Janner Fu Zhang Levine 2019][research_janner_fu_zhang_levine_2019]
- [Kaelbling Littman Cassandra 1998][research_kaelbling_littman_cassandra_1998]
- [Kakade Wang Yang 2020][research_kakade_wang_yang_2020]
- [Karl Soelch Bayer van der Smagt 2017][research_karl_et_al_2017]
- [Kawato 1999][research_kawato_1999]
- [Kidambi Rajeswaran Netrapalli Joachims 2020][research_kidambi_et_al_2020_morel]
- [Knill and Pouget 2004][research_knill_pouget_2004]
- [Miall and Wolpert 1996][research_miall_wolpert_1996]
- [Micheli Alonso Fleuret 2023][research_micheli_et_al_2023]
- [Millidge Tschantz Buckley 2021][research_millidge_tschantz_buckley_2021]
- [Moore and Atkeson 1993][research_moore_atkeson_1993]
- [Nagabandi Clavera Liu Fearing Abbeel Levine Finn 2018][research_nagabandi_et_al_2018_meta]
- [Nagabandi Kahn Fearing Levine 2018][research_nagabandi_et_al_2018]
- [Oh Singh Lee 2017][research_oh_singh_lee_2017]
- [Pfeiffer and Foster 2013][research_pfeiffer_foster_2013]
- [Pinneri et al 2021][research_pinneri_et_al_2021]
- [Racaniere et al 2017][research_racaniere_et_al_2017]
- [Rao and Ballard 1999][research_rao_ballard_1999]
- [Rigter Lacerda Hawes 2022][research_rigter_lacerda_hawes_2022]
- [Robine Hoftmann Uelwer Harmeling 2023][research_robine_et_al_2023]
- [Rubinstein 1997][research_rubinstein_1997]
- [Rusu Vecerik Rothorl Heess Pascanu Hadsell 2017][research_rusu_et_al_2017]
- [Sajid Ball Friston 2021][research_sajid_ball_friston_2021]
- [Schrittwieser et al 2020][research_schrittwieser_et_al_2020]
- [Silver Hasselt Hessel et al 2017 Predictron][research_silver_hasselt_hessel_2017]
- [Silver and Veness 2010][research_silver_veness_2010]
- [Somani Ye Hsu Lee 2013][research_somani_et_al_2013]
- [Sutton 1990][research_sutton_1990]
- [Sutton 1991][research_sutton_1991]
- [Todorov 2004][research_todorov_2004]
- [Todorov and Jordan 2002][research_todorov_jordan_2002]
- [Todorov and Li 2005][research_todorov_li_2005]
- [Tolman 1948][research_tolman_1948]
- [Tschantz Millidge Seth Buckley 2020][research_tschantz_millidge_seth_buckley_2020]
- [Wang and Ba 2020][research_wang_ba_2020]
- [Watter Springenberg Boedecker Riedmiller 2015][research_watter_et_al_2015]
- [Werbos 1987][research_werbos_1987]
- [Whittington and Bogacz 2017][research_whittington_bogacz_2017]
- [Williams Aldrich and Theodorou 2017][research_williams_aldrich_theodorou_2017]
- [Wolpert Ghahramani and Jordan 1995][research_wolpert_ghahramani_jordan_1995]
- [Wolpert Miall Kawato 1998][research_wolpert_miall_kawato_1998]
- [Wu Escontrela Hafner Abbeel Goldberg 2022][research_wu_et_al_2022]
- [Yang Du Ghasemipour Tenenbaum Schuurmans Abbeel 2023][research_yang_du_ghasemipour_2023]
- [Ye Liu Kurutach Abbeel Gao 2021][research_ye_liu_kurutach_abbeel_gao_2021]
- [Yu et al 2020 MOPO][research_yu_et_al_2020_mopo]
- [Yu Kumar Rafailov Rajeswaran Levine Finn 2021 COMBO][research_yu_et_al_2021_combo]
- [Zhang et al 2023][research_zhang_et_al_2023]

[book_craik_1943]: https://archive.org/details/thenatureofexplanation
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
[related_post_a255_hierarchical]: {% post_url 2025-12-23-machines_that_learn_from_experience_hierarchical_reinforcement_learning %}
[research_barto_bradtke_singh_1995]: https://www.sciencedirect.com/science/article/pii/000437029400011O
[research_bogacz_2017]: https://www.sciencedirect.com/science/article/pii/S0022249615000759
[research_bruce_et_al_2024]: https://arxiv.org/abs/2402.15391
[research_buckley_kim_ma_mcgregor_2017]: https://www.sciencedirect.com/science/article/pii/S0022249617300962
[research_buckman_et_al_2018]: https://papers.nips.cc/paper/2018/hash/f02208a057804ee16ac72ff4d3cec53b-Abstract.html
[research_buesing_et_al_2018]: https://arxiv.org/abs/1802.03006
[research_byravan_et_al_2022]: https://arxiv.org/abs/2210.15767
[research_chebotar_et_al_2019]: https://ieeexplore.ieee.org/document/8793789
[research_chua_calandra_mcallister_levine_2018]: https://papers.nips.cc/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html
[research_clark_2013]: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/whatever-next-predictive-brains-situated-agents-and-the-future-of-cognitive-science/33542C736E17E3D1D44E8D03BE5F4CD9
[research_clavera_et_al_2018]: https://proceedings.mlr.press/v87/clavera18a.html
[research_daw_niv_dayan_2005]: https://www.nature.com/articles/nn1560
[research_dayan_1993]: https://direct.mit.edu/neco/article/5/4/613/5679
[research_deisenroth_rasmussen_2011]: https://icml.cc/Conferences/2011/papers/323_icmlpaper.pdf
[research_feinberg_et_al_2018]: https://arxiv.org/abs/1803.00101
[research_friston_2010]: https://www.nature.com/articles/nrn2787
[research_ha_schmidhuber_2018]: https://papers.nips.cc/paper/2018/hash/2de5d16682c3c35007e4e92982f1a2ba-Abstract.html
[research_hafner_et_al_2019]: https://proceedings.mlr.press/v97/hafner19a.html
[research_hafner_et_al_2020]: https://openreview.net/forum?id=0oabwyZbOu
[research_hafner_et_al_2023]: https://arxiv.org/abs/2301.04104
[research_hafner_lillicrap_ba_norouzi_2020_dreamer]: https://openreview.net/forum?id=S1lOTC4tDS
[research_hafner_lillicrap_norouzi_ba_2020]: https://openreview.net/forum?id=0oabwyZbOu
[research_heess_wayne_silver_lillicrap_erez_tassa_2015]: https://papers.nips.cc/paper/2015/hash/148510031349642de5ca0c544f31b2ef-Abstract.html
[research_hwangbo_et_al_2019]: https://www.science.org/doi/10.1126/scirobotics.aau5872
[research_igl_et_al_2018]: https://proceedings.mlr.press/v80/igl18a.html
[research_ito_2008]: https://www.nature.com/articles/nrn2332
[research_janner_fu_zhang_levine_2019]: https://papers.nips.cc/paper/2019/hash/5faf461eff3099671ad63c6f3f094f7f-Abstract.html
[research_kaelbling_littman_cassandra_1998]: https://www.sciencedirect.com/science/article/pii/S000437029800023X
[research_kakade_wang_yang_2020]: https://arxiv.org/abs/2010.05673
[research_karl_et_al_2017]: https://openreview.net/forum?id=HyTqHL5xg
[research_kawato_1999]: https://www.sciencedirect.com/science/article/pii/S0959438899000288
[research_kidambi_et_al_2020_morel]: https://papers.nips.cc/paper/2020/hash/f7efa4f864ae9b88d43527f4b14f750f-Abstract.html
[research_knill_pouget_2004]: https://www.sciencedirect.com/science/article/pii/S1364661304002165
[research_miall_wolpert_1996]: https://www.sciencedirect.com/science/article/pii/S0893608096000354
[research_micheli_et_al_2023]: https://openreview.net/forum?id=vhFu1Acb0xb
[research_millidge_tschantz_buckley_2021]: https://direct.mit.edu/neco/article/33/3/674/95642
[research_moore_atkeson_1993]: https://link.springer.com/article/10.1007/BF00993104
[research_nagabandi_et_al_2018]: https://ieeexplore.ieee.org/document/8463189
[research_nagabandi_et_al_2018_meta]: https://openreview.net/forum?id=HyztsoC5Y7
[research_oh_singh_lee_2017]: https://papers.nips.cc/paper/2017/hash/ffbd6cbb019a1413183c8d08f2929307-Abstract.html
[research_pfeiffer_foster_2013]: https://www.nature.com/articles/nature12112
[research_pinneri_et_al_2021]: https://proceedings.mlr.press/v155/pinneri21a.html
[research_racaniere_et_al_2017]: https://papers.nips.cc/paper/2017/hash/9e82757e9a1c12cb710ad680db11f6f1-Abstract.html
[research_rao_ballard_1999]: https://www.nature.com/articles/nn0199_79
[research_rigter_lacerda_hawes_2022]: https://papers.nips.cc/paper/2022/hash/c73df2ba1e3d3adbfbf03c78e2eb5e63-Abstract-Conference.html
[research_robine_et_al_2023]: https://openreview.net/forum?id=TdBaDGCpjly
[research_rubinstein_1997]: https://link.springer.com/article/10.1007/BF01192140
[research_rusu_et_al_2017]: https://proceedings.mlr.press/v78/rusu17a.html
[research_sajid_ball_friston_2021]: https://direct.mit.edu/neco/article/33/3/674/95642
[research_schrittwieser_et_al_2020]: https://www.nature.com/articles/s41586-020-03051-4
[research_silver_hasselt_hessel_2017]: https://proceedings.mlr.press/v70/silver17a.html
[research_silver_veness_2010]: https://papers.nips.cc/paper/2010/hash/edfbe1afcf9246bb0d40eb4d8027d90f-Abstract.html
[research_somani_et_al_2013]: https://papers.nips.cc/paper/2013/hash/e2c0be24560d78c5e599c2a9c9d0bbd2-Abstract.html
[research_sutton_1990]: https://dl.acm.org/doi/10.5555/3091622.3091638
[research_sutton_1991]: https://dl.acm.org/doi/10.1145/122344.122377
[research_todorov_2004]: https://www.nature.com/articles/nn1309
[research_todorov_jordan_2002]: https://www.nature.com/articles/nn963
[research_todorov_li_2005]: https://ieeexplore.ieee.org/document/1470154
[research_tolman_1948]: https://psycnet.apa.org/record/1949-00103-001
[research_tschantz_millidge_seth_buckley_2020]: https://arxiv.org/abs/2002.12636
[research_wang_ba_2020]: https://arxiv.org/abs/1907.02057
[research_watter_et_al_2015]: https://papers.nips.cc/paper/2015/hash/a1afc58c6ca9540d057299ec3016d726-Abstract.html
[research_werbos_1987]: https://ieeexplore.ieee.org/document/6313077
[research_whittington_bogacz_2017]: https://direct.mit.edu/neco/article/29/5/1229/8253
[research_williams_aldrich_theodorou_2017]: https://arc.aiaa.org/doi/10.2514/1.G001921
[research_wolpert_ghahramani_jordan_1995]: https://www.science.org/doi/10.1126/science.7569931
[research_wolpert_miall_kawato_1998]: https://www.sciencedirect.com/science/article/pii/S1364661398012211
[research_wu_et_al_2022]: https://arxiv.org/abs/2206.14176
[research_yang_du_ghasemipour_2023]: https://openreview.net/forum?id=sFyTZEqmUY
[research_ye_liu_kurutach_abbeel_gao_2021]: https://papers.nips.cc/paper/2021/hash/d5eca8dc3820cad9fe56a3bafda65ca1-Abstract.html
[research_yu_et_al_2020_mopo]: https://papers.nips.cc/paper/2020/hash/a322852ce0df73e204b7e67cbbef0d0a-Abstract.html
[research_yu_et_al_2021_combo]: https://papers.nips.cc/paper/2021/hash/f29a179746902e331572c483c45e5086-Abstract.html
[research_zhang_et_al_2023]: https://arxiv.org/abs/2310.09615
