---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: Meta-Learning and Online Adaptation"
date:   2025-12-26 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 9
---

<!-- A258 -->
<script>console.log("A258");</script>

Meta-learning is the study of algorithms that improve their own learning process by acquiring, across a distribution of related tasks, the ability to adapt rapidly to a new task with few environment interactions. In the reinforcement learning setting, meta-learning provides a route to sample efficiency that complements the model-based and hierarchical approaches of prior articles. Rather than learning each task from scratch, a meta-learned agent brings prior structure that specializes to the new task through a fast inner-loop adaptation. This article surveys the science and theory of meta-learning and online adaptation as they stand in the mid 2020s. Coverage includes the recurrent-network approach of RL-squared and learning-to-reinforcement-learn, the gradient-based Model-Agnostic Meta-Learning family and its second-order and implicit variants, metric-based meta-learning through matching and prototypical networks, context-conditioned policies with Bayesian task inference including VariBAD and PEARL, hypernetworks and amortized adaptation, meta-gradient methods that optimize hyperparameters and auxiliary signals online, meta-learning of optimizers and reward functions, task distribution design and automatic curriculum construction, meta-overfitting and the memorization failure mode, in-context reinforcement learning through algorithm distillation, model-based meta-learning and rapid dynamics adaptation, meta-learning theory including PAC-Bayes and generalization bounds, cross-embodiment and foundation-scale meta-reinforcement learning, sim-to-real adaptation and its relationship to domain randomization, software frameworks and reproducibility considerations, and the neuroscience correspondence to prefrontal cortex meta-learning. Article five treated exploration in isolated single-task settings. The present article treats how meta-learning shapes the exploration policies acquired across an experience distribution.

## The Meta-Learning Problem: Learning to Learn

Meta-learning treats the learning algorithm itself as an object to be improved through experience. In the standard supervised or reinforcement learning setting, an algorithm maps a training dataset $\mathcal{D}$ to a hypothesis $h$,

$$h = \mathcal{A}(\mathcal{D})$$

with the algorithm $\mathcal{A}$ fixed by human design. Meta-learning parameterizes the algorithm $\mathcal{A}$ by meta-parameters $\phi$ and optimizes those parameters across a distribution of tasks,

$$\phi^* = \arg\max_\phi \mathbb{E}_{\mathcal{T} \sim p(\mathcal{T})}\!\left[\mathcal{L}_{\mathcal{T}}(\mathcal{A}_\phi(\mathcal{D}_{\mathcal{T}}))\right]$$

where $\mathcal{L}_{\mathcal{T}}$ is a task-loss and $\mathcal{D}_{\mathcal{T}}$ is the training data for task $\mathcal{T}$. The optimized meta-algorithm $\mathcal{A}_{\phi^*}$ produces hypotheses that adapt rapidly to new tasks drawn from $p(\mathcal{T})$.

The reinforcement learning specialization treats each task as a Markov decision process $\mathcal{M} = (\mathcal{S}, \mathcal{A}, P_{\mathcal{T}}, R_{\mathcal{T}}, \gamma)$ with task-transition and reward. The learning algorithm produces a policy from experience,

$$\pi = \mathcal{A}_\phi(\tau_{1:H})$$

where $\tau_{1:H}$ is a sequence of transitions collected during the inner-loop adaptation. Meta-reinforcement learning optimizes $\phi$ to produce policies that achieve high return on tasks drawn from $p(\mathcal{T})$ after only $H$ steps of adaptation. The meta-testing procedure for a new task $\mathcal{T} \sim p(\mathcal{T})$ then proceeds by executing

$$\tau_{1:H} \sim \pi_{\mathcal{A}_\phi(\emptyset)}, \pi_{\mathcal{A}_\phi(\tau_{1:1})}, \ldots, \pi_{\mathcal{A}_\phi(\tau_{1:H-1})}$$

with progressive re-adaptation as data accumulates, followed by evaluation of the final adapted policy $\pi_{\mathcal{A}_\phi(\tau_{1:H})}$ over an evaluation horizon under task $\mathcal{T}$.

Two distinct settings shape the meta-learning literature. The multi-task setting provides simultaneous access to many tasks during meta-training, with the objective of producing an algorithm that generalizes to unseen tasks from the same distribution. The continual setting provides sequential exposure to tasks, with the objective of producing an algorithm that improves over the sequence without forgetting earlier tasks. Both settings admit algorithmic and theoretical treatments.

The distinction between meta-learning and multi-task learning is subtle. A pure multi-task algorithm produces a single policy that performs well across a fixed set of tasks. A meta-learning algorithm produces a fast adapter that specializes to any task in the distribution. The two coincide when the task distribution is finite and observable during training, but diverge when the meta-learned adapter is expected to generalize to unseen tasks.

## Historical Development

The idea of learning to learn has a long history. [Schmidhuber 1987][research_schmidhuber_1987_metalearning] doctoral thesis proposed evolutionary meta-learning in which the learning algorithm itself is evolved across generations of tasks. [Naik and Mammone 1992][research_naik_mammone_1992] independently introduced meta-neural-networks in the connectionist learning literature. [Bengio Bengio and Cloutier 1990][research_bengio_bengio_cloutier_1990] proposed learning a synaptic update rule as an alternative to backpropagation. [Schmidhuber Zhao and Wiering 1996][research_schmidhuber_zhao_wiering_1996] developed the meta-learning framework further with bias learning. The [Thrun and Pratt 1998][book_thrun_pratt_1998] Learning to Learn edited volume consolidated the field at the turn of the century, and the [Vilalta and Drazdil 2002][research_vilalta_drazdil_2002] survey provided a systematic taxonomy of meta-learning approaches. The [Hospedales Antoniou Micaelli Storkey 2022][research_hospedales_et_al_2022] modern survey reviews the field circa the early 2020s.

The neural network meta-learning of [Hochreiter Younger and Conwell 2001][research_hochreiter_younger_conwell_2001] used LSTMs as universal learning algorithms, training a recurrent network to solve a sequence of related regression tasks by taking the training data as input and producing predictions. The framework provided the direct precursor to the modern recurrent meta-reinforcement learning approaches. The Bayes-adaptive MDP framework treated later has roots in the [Duff 2002][book_duff_2002] doctoral thesis on optimal exploration under uncertainty, and the [Poupart Vlassis Hoey Regan 2006][research_poupart_et_al_2006] analytical treatment of Bayes-adaptive MDPs provided the algorithmic foundation for tractable Bayes-optimal reinforcement learning.

Meta-reinforcement learning emerged as a distinct research area in the mid 2010s. [Duan Schulman Chen Bartlett Sutskever Abbeel 2016][research_duan_et_al_2016_rl2] RL-squared and [Wang Kurth-Nelson Tirumala Soyer Leibo Munos Blundell Kumaran Botvinick 2016][research_wang_et_al_2016_l2rl] Learning to Reinforcement Learn independently proposed training recurrent policies on distributions of MDPs so that the recurrent state implicitly encodes the task identity.

[Finn Abbeel and Levine 2017][research_finn_abbeel_levine_2017] Model-Agnostic Meta-Learning (MAML) provided a gradient-based alternative that has become the canonical modern meta-learning framework. MAML optimizes initial parameters that are one gradient step away from good task-parameters, providing a general-purpose adaptation mechanism applicable to any differentiable model.

The 2018-2020 period produced considerable algorithmic diversification. Reptile of [Nichol Achiam Schulman 2018][research_nichol_achiam_schulman_2018] provided a simpler first-order approximation to MAML. Probabilistic Meta-Reinforcement Learning (PEARL) of [Rakelly Zhou Quillen Finn Levine 2019][research_rakelly_et_al_2019_pearl] combined off-policy meta-learning with variational task inference. Variational Bayes-Adaptive Deep RL (VariBAD) of [Zintgraf Shiarlis Igl Schulze Gal Hofmann Whiteson 2020][research_zintgraf_et_al_2020_varibad] introduced Bayes-optimal meta-reinforcement learning through variational task inference.

Meta-gradient methods matured in parallel through [Xu van Hasselt Silver 2018][research_xu_van_hasselt_silver_2018] meta-gradient RL and subsequent work on learning hyperparameters, auxiliary rewards, and discount factors through outer-loop gradients.

In-context reinforcement learning emerged in the 2020s. Algorithm Distillation of [Laskin Wang Oh Parisotto Spencer et al 2023][research_laskin_et_al_2023] demonstrated that transformer sequence models trained on learning-algorithm outputs could produce in-context learning behavior at test time. Adaptive Agent of [Bauer et al 2023][research_bauer_et_al_2023_ada] combined meta-learning with foundation-model-scale training to achieve rapid adaptation across a vast distribution of tasks.

## The Meta-Reinforcement Learning Framework

The meta-reinforcement learning framework specifies a distribution $p(\mathcal{T})$ over MDPs from which tasks are sampled. Each task $\mathcal{T} \sim p(\mathcal{T})$ specifies transition dynamics $P_{\mathcal{T}}(s' \mid s, a)$ and reward $R_{\mathcal{T}}(s, a)$ that may vary across tasks, while the state and action spaces are typically shared.

The meta-training procedure alternates between task sampling and inner-loop adaptation. For each meta-training batch, tasks are sampled from $p(\mathcal{T})$. For each task, the meta-algorithm collects trajectories under the current adaptation policy and updates the task-policy. The meta-parameters are then updated based on the resulting task-policy's performance.

The meta-training objective is

$$J_{\text{meta}}(\phi) = \mathbb{E}_{\mathcal{T} \sim p(\mathcal{T})}\!\left[J_{\mathcal{T}}(\pi_{\mathcal{A}_\phi(\tau_{1:H})})\right]$$

where $\pi_{\mathcal{A}_\phi(\tau_{1:H})}$ is the policy produced by the meta-algorithm after $H$ steps of adaptation, and $J_{\mathcal{T}}$ is the expected return under task $\mathcal{T}$,

$$J_{\mathcal{T}}(\pi) = \mathbb{E}_\pi\!\left[\sum_{t=0}^{T-1} \gamma^t R_{\mathcal{T}}(s_t, a_t) \mid s_0 \sim \mu_0\right]$$

Optimizing this objective produces a meta-algorithm that adapts efficiently to new tasks.

The Bayes-adaptive MDP formalism provides a normative framing. Treating the task identity as a latent variable, the joint state-plus-task becomes fully observable via the belief $b_t(\mathcal{T})$, and the optimal Bayes-adaptive policy solves

$$\pi^*_{\text{BAMDP}} = \arg\max_\pi \mathbb{E}_{\mathcal{T} \sim p(\mathcal{T})}\!\left[\sum_{t=0}^{T-1} \gamma^t R_{\mathcal{T}}(s_t, a_t) \mid s_0 \sim \mu_0, \pi\right]$$

with actions conditioned on both the current state and the current belief. Bayes-optimal exploration automatically emerges from this framing because information-gathering actions that reduce belief uncertainty about $\mathcal{T}$ are valuable through their effect on future expected reward.

Two critical quantities characterize meta-reinforcement learning problems. The adaptation budget $H$ specifies how many steps of task-data collection are available. The task distribution $p(\mathcal{T})$ specifies the range of variation the meta-algorithm is expected to handle. Different meta-learning methods target different regimes of these two variables.

For small adaptation budgets $H \ll |\mathcal{S}||\mathcal{A}|$, the meta-algorithm must exploit strong prior structure and cannot recover the task from data alone. For large budgets, meta-learning provides diminishing returns over separate training on each task. The intermediate regime, where $H$ is large enough to identify the task but small enough that generic reinforcement learning would fail, is the target of most contemporary meta-reinforcement learning research.

## Recurrent Meta-Reinforcement Learning

The recurrent meta-reinforcement learning framework treats meta-learning as training a recurrent policy on a distribution of MDPs. The recurrent hidden state implicitly encodes task-identifying information from past experience, and the policy conditions action selection on this hidden state.

RL-squared of Duan et al 2016 formulates the meta-policy as

$$\pi_\theta(a_t \mid o_t, h_t), \quad h_t = f_\theta(o_t, a_{t-1}, r_{t-1}, h_{t-1})$$

with the recurrent state $h_t$ updated by a neural network based on the current observation, previous action, previous reward, and previous hidden state. The recurrent policy is trained end-to-end by standard policy gradient methods on the outer meta-objective, treating the entire adaptation trajectory as a single episode from the meta-learning perspective.

The mechanism is remarkably simple in principle. The recurrent policy sees a sequence of task-experience during meta-testing and produces actions consistent with efficient adaptation to whatever task is being solved. The task identity is never explicitly represented. Instead, it is implicitly encoded in the recurrent state.

Learning to Reinforcement Learn of Wang et al 2016 provided the concurrent formulation with an explicit connection to prefrontal cortex meta-learning. The paper documented that recurrent policies trained on task distributions display many hallmarks of efficient reinforcement learning at test time, including exploration and adaptation patterns that were not directly trained.

The recurrent framework's principal advantage is generality. It requires no assumptions about the task structure or the adaptation mechanism, and the recurrent network can in principle learn arbitrarily-complex adaptation strategies. Its principal disadvantage is data-hungry meta-training. The recurrent policy must experience many tasks to learn the meta-strategy, and the amount of meta-training data required scales with the complexity of the task distribution.

Modern variants extend the account with transformer sequence models in place of recurrent networks, treating the adaptation trajectory as a sequence to be autoregressively modeled. [Ni Eysenbach and Levine 2022][research_ni_eysenbach_levine_2022] documented that transformer-based sequence models considerably outperform recurrent baselines on POMDP-based meta-reinforcement learning benchmarks when trained at sufficient scale. The transformer-based approach connects meta-reinforcement learning to the sequence modeling framework treated in articles four and eight.

## Model-Agnostic Meta-Learning

Model-Agnostic Meta-Learning (MAML) of Finn Abbeel and Levine 2017 provides a gradient-based approach to meta-learning that has become the canonical modern framework. MAML learns initial parameters that are near a good solution for any task in the distribution, so that a small number of gradient updates on task-data produces a task-policy that performs well.

Formally, MAML optimizes meta-parameters $\theta$ that satisfy

$$\theta^* = \arg\min_\theta \mathbb{E}_{\mathcal{T} \sim p(\mathcal{T})}\!\left[\mathcal{L}_{\mathcal{T}}(\theta - \alpha \nabla_\theta \mathcal{L}_{\mathcal{T}}(\theta))\right]$$

where $\alpha$ is the inner-loop step size and $\mathcal{L}_{\mathcal{T}}$ is the task-loss. The inner-loop adaptation from meta-parameters to task-parameters is

$$\theta'_{\mathcal{T}} = \theta - \alpha \nabla_\theta \mathcal{L}_{\mathcal{T}}^{\text{train}}(\theta)$$

and the multi-step extension performs $k$ successive gradient updates

$$\theta_i = \theta_{i-1} - \alpha \nabla_\theta \mathcal{L}_{\mathcal{T}}^{\text{train}}(\theta_{i-1}), \quad i = 1, \ldots, k$$

starting from $\theta_0 = \theta$. The mechanism requires that a small number of gradient steps from $\theta^*$ on the task-loss produces near-optimal task-parameters.

Computing the meta-gradient requires differentiating through the inner-loop gradient update, which produces second-order gradients. The meta-gradient at $\theta$ is

$$\nabla_\theta J_{\text{MAML}} = \mathbb{E}_{\mathcal{T}}\!\left[(I - \alpha \nabla_\theta^2 \mathcal{L}_{\mathcal{T}}(\theta)) \nabla_{\theta'} \mathcal{L}_{\mathcal{T}}(\theta')|_{\theta' = \theta - \alpha \nabla_\theta \mathcal{L}_{\mathcal{T}}(\theta)}\right]$$

where the second-order term $\nabla_\theta^2 \mathcal{L}_{\mathcal{T}}(\theta)$ is the Hessian of the inner-loop loss. Full second-order MAML is computationally expensive but provides the theoretical basis for the approach.

First-order MAML approximations drop the second-order terms in exchange for computational efficiency, using

$$\nabla_\theta J_{\text{FOMAML}} \approx \mathbb{E}_{\mathcal{T}}\!\left[\nabla_{\theta'} \mathcal{L}_{\mathcal{T}}(\theta')|_{\theta' = \theta - \alpha \nabla_\theta \mathcal{L}_{\mathcal{T}}(\theta)}\right]$$

producing a gradient approximation that has empirically proved to be sufficient on many tasks. The [Nichol Achiam Schulman 2018][research_nichol_achiam_schulman_2018] Reptile algorithm provides an even simpler first-order alternative,

$$\theta \leftarrow \theta + \beta (\text{SGD}_k^{\mathcal{T}}(\theta) - \theta)$$

where $\text{SGD}_k^{\mathcal{T}}(\theta)$ is the parameters obtained after $k$ steps of stochastic gradient descent on task $\mathcal{T}$. Reptile achieves comparable performance to MAML with significantly simpler implementation.

The policy-gradient specialization of MAML for reinforcement learning uses the REINFORCE gradient in the inner loop,

$$\nabla_\theta \mathcal{L}_{\mathcal{T}}(\theta) = -\mathbb{E}_{\tau \sim \pi_\theta}\!\left[\sum_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) G_t\right]$$

with the outer-loop meta-gradient computed through the inner-loop trajectory sampling and gradient update.

MAML has been applied to reinforcement learning through several variants. Proximal Meta-Policy Search (ProMP) of [Rothfuss Lee Clavera Asfour Abbeel 2019][research_rothfuss_et_al_2019] combined MAML with the trust-region and clipped policy gradient methods of article four, producing meta-policies with stable inner-loop adaptation. Implicit MAML of [Rajeswaran Finn Kakade Levine 2019][research_rajeswaran_et_al_2019_imaml] used implicit differentiation to avoid the second-order gradients, providing computational efficiency without the accuracy loss of first-order approximations.

MAML++ of [Antoniou Edwards Storkey 2019][research_antoniou_edwards_storkey_2019] documented that many practical improvements to MAML including per-layer learning rates, multi-step BN statistics, and cosine-annealed learning rates substantially improve performance across benchmark tasks. The Bayesian interpretation of MAML by [Grant Finn Levine Darrell Griffiths 2018][research_grant_finn_levine_darrell_griffiths_2018] framed MAML as hierarchical Bayesian inference and provided a principled probabilistic account of gradient-based meta-learning. Online meta-learning of [Finn Rajeswaran Kakade Levine 2019][research_finn_rajeswaran_kakade_levine_2019] extended MAML to sequential settings in which tasks arrive one at a time and the meta-learner must handle non-stationary task distributions. The [Ravi and Larochelle 2017][research_ravi_larochelle_2017] framing of the meta-learner as an LSTM optimizer provided one of the foundational architectural alternatives to MAML.

The empirical analysis of [Raghu Raghu Bengio Vinyals 2020][research_raghu_raghu_bengio_vinyals_2020] documented that most of the adaptation benefit in MAML on few-shot supervised tasks derives from feature reuse rather than rapid weight change, motivating simplified variants such as ANIL that adapt only the classification head. The observation partially transfers to reinforcement learning, where fixed shared representations combined with task-value or policy heads often match full-parameter MAML on benchmark tasks. The [Rusu Rao Sygnowski Vinyals Pascanu Osindero Hadsell 2019][research_rusu_et_al_2019_leo] LEO framework proposed latent embedding optimization as an intermediate between MAML and metric-based methods, performing gradient-based adaptation in a low-dimensional latent space of task representations.

## Metric-Based Meta-Learning

Metric-based meta-learning approaches parameterize the learning algorithm as a distance function in a learned embedding space. Given a small support set of examples from a novel task, the meta-learned algorithm classifies or acts by comparing new inputs to the support set through the learned metric. The model originated in few-shot supervised classification but has direct analogues in reinforcement learning through embedding-based task representations and value function approximation.

Siamese networks of [Koch Zemel Salakhutdinov 2015][research_koch_zemel_salakhutdinov_2015] provided the initial architecture, training paired networks to produce embeddings such that same-class pairs are close and different-class pairs are far in the embedding space. This formulation is trained with a contrastive or triplet loss

$$L_{\text{contrastive}}(x_i, x_j, y_{ij}) = y_{ij} \, \|f_\theta(x_i) - f_\theta(x_j)\|^2 + (1 - y_{ij}) \, \max(0, m - \|f_\theta(x_i) - f_\theta(x_j)\|)^2$$

with $y_{ij} = 1$ if the pair is same-class and $y_{ij} = 0$ otherwise, and $m$ a margin hyperparameter.

Matching Networks of [Vinyals Blundell Lillicrap Kavukcuoglu Wierstra 2016][research_vinyals_et_al_2016_matching] extended the treatment to few-shot classification. Given a support set $\mathcal{S} = \{(x_i, y_i)\}_{i=1}^N$ and a query $x^*$, the predicted label is

$$\hat{y}^* = \sum_{i=1}^{N} a(x^*, x_i) \, y_i, \quad a(x^*, x_i) = \frac{\exp(\text{cosine}(f(x^*), g(x_i)))}{\sum_j \exp(\text{cosine}(f(x^*), g(x_j)))}$$

where the attention weights implement a soft nearest-neighbor lookup in the learned embedding space. The full context embedding variant conditions $f$ and $g$ on the entire support set through a bidirectional LSTM, enabling context-dependent metric adaptation.

Prototypical Networks of [Snell Swersky Zemel 2017][research_snell_swersky_zemel_2017] provided a simpler and often more effective framework in which each class is represented by the mean embedding of its support examples

$$c_k = \frac{1}{|\mathcal{S}_k|} \sum_{(x_i, y_i) \in \mathcal{S}_k} f_\theta(x_i)$$

and query classification proceeds by softmax over squared distances to prototypes

$$p_\theta(y = k \mid x^*) = \frac{\exp(-\|f_\theta(x^*) - c_k\|^2)}{\sum_{k'} \exp(-\|f_\theta(x^*) - c_{k'}\|^2)}$$

This account provides a Bayes-optimal classifier under an assumed spherical Gaussian likelihood in embedding space and generalizes to zero-shot settings when class embeddings are computed from side information rather than support examples.

Relation Networks of [Sung Yang Zhang Xiang Torr Hospedales 2018][research_sung_et_al_2018] replaced the fixed metric with a learned neural comparison function that operates on concatenated support-query embedding pairs, producing a similarity score directly rather than through a distance calculation. The framework subsumes matching and prototypical networks and often achieves stronger performance when the underlying similarity is highly non-Euclidean.

In reinforcement learning settings, metric-based meta-learning appears through several routes. Successor feature approaches of [Barreto Dabney Munos Hunt Schaul van Hasselt Silver 2017][research_barreto_et_al_2017] decompose value functions into task-independent features and task-reward weights, enabling policy transfer through inner products in the successor feature space. Contrastive task inference through embedding-space clustering has been used in extensions of PEARL for improved sample efficiency. The relation between metric-based supervised meta-learning and Bayesian task inference in reinforcement learning is close, with both frameworks producing task representations that support downstream adaptation through comparison operations.

## Context-Conditioned Policies and Task Inference

Context-conditioned policy approaches separate the task representation from the policy itself. A task inference network $q_\phi(z \mid \tau_{1:H})$ maps a short trajectory of experience to a latent task representation $z$, and a task-conditioned policy $\pi_\theta(a \mid s, z)$ uses this representation for action selection.

The account provides several conceptual advantages over the recurrent and gradient-based approaches. The task inference network is trained specifically for the inference task, which can leverage supervised learning objectives such as reconstruction, contrastive learning, or variational inference. The task-conditioned policy can be trained by standard reinforcement learning methods with $z$ as an additional input, avoiding the specialized meta-training procedures of MAML.

PEARL of Rakelly Zhou Quillen Finn Levine 2019 provides the canonical modern instantiation. The task inference network uses variational inference on a set of context transitions,

$$q_\phi(z \mid \mathcal{C}) = \mathcal{N}(z ; \mu_\phi(\mathcal{C}), \Sigma_\phi(\mathcal{C}))$$

where $\mathcal{C} = \{(s_i, a_i, r_i, s'_i)\}_{i=1}^N$ is a set of transitions from the target task. The context is aggregated in a permutation-invariant manner via a product-of-Gaussians factorization over per-transition encodings,

$$\mu_\phi(\mathcal{C}) = \frac{\sum_i \mu_\phi(c_i) / \sigma^2_\phi(c_i)}{\sum_i 1 / \sigma^2_\phi(c_i)}, \quad \sigma^{-2}_\phi(\mathcal{C}) = \sum_i \sigma^{-2}_\phi(c_i)$$

so that the inferred task representation does not depend on the ordering of the context transitions.

The task-conditioned policy is trained by off-policy actor-critic methods (SAC) with the inferred task representation as an additional input,

$$\pi_\theta(a \mid s, z), \quad Q_\psi(s, a, z)$$

The end-to-end meta-training objective combines the reinforcement learning objective with a variational inference term,

$$J_{\text{PEARL}}(\theta, \psi, \phi) = J_{\text{SAC}}(\theta, \psi, \phi) - \beta \, D_{\text{KL}}(q_\phi(z \mid \mathcal{C}) \, \| \, p(z))$$

where the KL term regularizes the task representation toward a prior distribution.

PEARL has proved to be one of the most sample-efficient meta-reinforcement learning methods on standard benchmarks, largely due to its off-policy training that leverages replay-buffer data across tasks. Extensions include MQL of [Fakoor Chaudhari Soatto Smola 2020][research_fakoor_et_al_2020_mql] which simplified the task inference through a meta-Q-learning framework. Task-conditional VAE approaches of [Sæmundsson Hofmann Deisenroth 2018][research_saemundsson_hofmann_deisenroth_2018] applied similar variational task inference to Gaussian process dynamics models, providing a principled framework for model-based meta-learning with structured priors. The task inference framework of [Humplik Igl Duan et al 2019][research_humplik_et_al_2019] combined explicit task supervision with policy learning, producing more sample-efficient task inference than purely-variational alternatives.

## Bayesian Meta-Reinforcement Learning

Bayesian meta-reinforcement learning provides a principled framework that treats task identity as a latent variable and derives Bayes-optimal exploration policies. The model produces exploration behavior that trades off task inference against reward exploitation in a normatively-optimal way.

The Bayes-adaptive MDP formalism casts meta-reinforcement learning as a POMDP over the joint state-plus-task-identity space. The optimal Bayes-adaptive policy conditions on the belief over task identity,

$$b_t(\mathcal{T}) = \Pr(\mathcal{T} \mid o_{1:t}, a_{1:t-1})$$

updated by Bayes rule at each step. Solving the Bayes-adaptive POMDP exactly is intractable for realistic problems, but approximate methods provide practical algorithms. The BAMCP algorithm of [Guez Silver Dayan 2013][research_guez_silver_dayan_2013] extended Monte Carlo tree search to the Bayes-adaptive setting, providing sample-efficient planning under task uncertainty. The [Ortega Wang Rowland Genewein Hutter et al 2019][research_ortega_et_al_2019] Bayesian meta-reinforcement learning treatment provided a systematic modern framework connecting the classical Bayes-adaptive theory to deep function approximation.

VariBAD of Zintgraf Shiarlis Igl Schulze Gal Hofmann Whiteson 2020 provides a variational Bayesian meta-reinforcement learning framework. A variational encoder produces a distribution over latent tasks

$$q_\phi(z_t \mid \tau_{1:t}) = \mathcal{N}(z_t ; \mu_\phi(\tau_{1:t}), \Sigma_\phi(\tau_{1:t}))$$

trained through a variational objective that combines observation prediction with a KL regularizer,

$$L_{\text{VariBAD}}(\phi) = -\mathbb{E}_{q_\phi}\!\left[\sum_t \log p_\theta(o_t, r_t \mid s_t, a_t, z_t)\right] + \beta \sum_t D_{\text{KL}}(q_\phi(z_t \mid \tau_{1:t}) \, \| \, p(z_t))$$

The policy conditions on the current variational task belief

$$\pi_\theta(a_t \mid s_t, q_\phi(z_t \mid \tau_{1:t}))$$

producing behavior that trades off task-identifying exploration against reward-seeking exploitation.

VariBAD produces near-Bayes-optimal behavior on tabular meta-reinforcement learning problems and scales to deep function approximation on standard benchmarks. Its principal advantage over MAML and PEARL is the explicit uncertainty representation, which supports normatively-optimal exploration in a way that gradient-based and point-estimate methods do not directly provide.

Extensions include HyperX of [Zintgraf Feng Igl Whiteson 2021][research_zintgraf_et_al_2021_hyperx] that incorporates hypernetwork-based task adaptation and reward-based exploration bonuses tuned for Bayes-adaptive exploration, and BOReL of [Dorfman Shenfeld Tamar 2021][research_dorfman_shenfeld_tamar_2021] that extends the treatment to offline meta-reinforcement learning.

## Hypernetworks and Amortized Adaptation

Hypernetworks provide a distinct route to meta-learning in which a meta-network directly outputs the parameters of a task-policy or value function. The treatment was introduced by [Ha Dai Le 2016][research_ha_dai_le_2016] in the general context of dynamic neural network generation and has been applied to meta-reinforcement learning through several routes.

The hypernetwork meta-learner formalizes as

$$\theta_{\text{policy}} = H_\phi(z_{\text{task}}), \quad z_{\text{task}} = q_\psi(\tau_{1:H})$$

where $H_\phi$ is the hypernetwork with meta-parameters $\phi$, $z_{\text{task}}$ is a task embedding produced by a task inference network $q_\psi$ from adaptation trajectory $\tau_{1:H}$, and $\theta_{\text{policy}}$ are the parameters of the task-policy $\pi_{\theta_{\text{policy}}}$. This account combines the task-inference approach of PEARL with the direct policy-parameter generation of hypernetworks, avoiding both the second-order gradients of MAML and the recurrent state maintenance of RL-squared.

The primary appeal of the hypernetwork framework is expressive task-dependent structure. A policy with parameters generated by a hypernetwork can implement arbitrarily different task-behaviors without requiring the shared-representation constraint of context-conditioned policies. The primary challenge is training stability, since the meta-parameter space of $\phi$ is typically much larger than the task-policy parameters, and hypernetwork training exhibits characteristic sensitivity to weight initialization and normalization.

Amortized Bayesian inference provides a complementary perspective. Rather than solving the Bayes-adaptive planning problem directly, amortized methods train a neural network to output an approximation of the Bayes-adaptive policy directly from a small adaptation trajectory. The [Mishra Rohaninejad Chen Abbeel 2018][research_mishra_et_al_2018_snail] SNAIL architecture combined temporal convolutions with attention to produce fully-amortized meta-learners that generalize across a wide range of few-shot tasks. Amortization avoids the recurrent-state bottleneck of RL-squared while retaining the sequence-modeling advantages of attention-based architectures.

Recent work by [Kirsch Sohl-Dickstein Metz 2019][research_kirsch_sohl_dickstein_metz_2019] on MetaGenRL demonstrated that hypernetwork-generated objective functions can be meta-learned across environments to produce reinforcement learning updates that transfer to entirely novel Markov decision processes not seen during meta-training, extending the amortized meta-learning paradigm to the algorithm-space directly.

## Meta-Gradient Methods

Meta-gradient methods use outer-loop gradients to optimize aspects of the inner learning process that are typically treated as hyperparameters. The framework provides a principled alternative to grid search over hyperparameters and enables online adaptation of the learning process itself.

The core observation is that if the inner learning process is differentiable, then gradients with respect to its hyperparameters can be computed and used to optimize a meta-objective. Xu van Hasselt and Silver 2018 introduced this formulation by optimizing the discount factor and $\lambda$-return parameter online,

$$\gamma \leftarrow \gamma - \eta \nabla_\gamma J_{\text{outer}}(\theta_\gamma)$$

where $J_{\text{outer}}$ is a meta-objective (typically the return over a validation trajectory) and $\theta_\gamma$ are the policy parameters produced by the inner learning process with the current $\gamma$. The chain rule expansion of the meta-gradient exposes its computational structure,

$$\nabla_\gamma J_{\text{outer}} = \frac{\partial J_{\text{outer}}}{\partial \theta_\gamma} \cdot \frac{\partial \theta_\gamma}{\partial \gamma}$$

with the second factor requiring backpropagation through the inner-loop training dynamics.

Meta-Gradient Reinforcement Learning of Xu van Hasselt Silver 2018 documented that meta-gradient adaptation of $\gamma$ and $\lambda$ produces significant improvements on Atari benchmarks. Subsequent work extended the treatment to auxiliary reward functions [Zheng Oh Singh 2018][research_zheng_oh_singh_2018_lirpg], auxiliary tasks, exploration bonuses, and learning rates.

Learned Intrinsic Reward Policy Gradient (LIRPG) of Zheng Oh Singh 2018 optimizes an intrinsic reward function online through meta-gradients. The intrinsic reward augments the extrinsic reward during policy optimization,

$$\tilde{r}_t = r_t + \eta_{\text{intrinsic}}(s_t, a_t; \phi)$$

with $\phi$ optimized to maximize the outer-loop objective (extrinsic return only). The mechanism produces intrinsic rewards that shape policy learning without affecting the true objective.

Meta-Gradient learned rewards of [Oh Guo Warde-Farley Wayne Ostrovski Silver 2020][research_oh_et_al_2020] extended the framework to learn broader reward-shaping structures, and Never Give Up + Meta-Gradient of subsequent work combined the approach with the exploration methods of article five.

Self-tuning actor-critic architectures of [Zahavy Xu Veeriah Hessel Oh van Hasselt Silver Singh 2020][research_zahavy_et_al_2020_stac] STAC and STACX combined meta-gradient adaptation of multiple hyperparameters (return coefficients, auxiliary loss weights, entropy regularization) across parallel actor-critic training. The treatment demonstrated that meta-gradient adaptation of even a modest number of hyperparameters yields substantial improvements over hand-tuned baselines on Atari and DeepMind Control Suite benchmarks, and provided evidence that meta-gradient methods scale to production-scale reinforcement learning training.

The [Xu Van Hasselt Hessel Modayil et al 2020][research_xu_et_al_2020_meta_a2c] Meta-Gradient A2C extension demonstrated that meta-gradient adaptation of the discount factor and bootstrap parameter under an on-policy actor-critic training regime markedly improves benchmark performance without requiring hyperparameter search.

Meta-gradient methods provide a general framework for online adaptation of the learning process. Their principal challenge is the compute cost of meta-training, which requires inner-loop training to convergence for each outer-loop gradient, and the potential instability of nested optimization. Practical implementations use truncated inner loops and several stabilization techniques. Bootstrapped meta-learning of [Flennerhag et al 2022][research_flennerhag_et_al_2022] addressed the truncation-bias problem through target-network-based meta-gradient estimation, enabling stable long-horizon meta-training. The [Zheng Oh Wang Ha Weber Hafner Wu Levine et al 2020][research_zheng_et_al_2020_learning_reward] Learning to Reward framework extended meta-gradient reward learning to arbitrary parametric reward functions with theoretical guarantees on convergence to reward-shaping equivalence.

## Meta-Learning of Optimizers and Auxiliary Losses

The meta-learning of optimization procedures themselves represents a distinct branch of the meta-learning literature. Rather than learning initial parameters or task representations, this branch learns the update rule that transforms gradients into parameter updates.

Learning to Learn by Gradient Descent by Gradient Descent of [Andrychowicz Denil Gomez Hoffman Pfau Schaul Shillingford de Freitas 2016][research_andrychowicz_et_al_2016] parameterized the optimizer update rule as a recurrent network,

$$\Delta \theta_t = m_\phi(\nabla_\theta L, h_t), \quad h_{t+1} = f_\phi(\nabla_\theta L, h_t)$$

trained to minimize the loss achieved by iteratively applying the update rule. This account produced learned optimizers that outperformed standard first-order methods on the training task distribution but generalized poorly to novel tasks.

Subsequent work by [Metz Maheswaranathan Cheung Sohl-Dickstein 2019][research_metz_et_al_2019] documented the challenges of training generalizable learned optimizers and proposed training procedures that produce optimizers robust to task shift. The [Li and Malik 2017][research_li_malik_2017] Learning to Optimize framework provided a reinforcement-learning-based approach to optimizer meta-learning that treats optimization as a sequential decision process.

Meta-learning of auxiliary losses provides a related direction. The framework parameterizes an auxiliary loss function that is added to the primary learning objective,

$$L_{\text{aux}}(\theta) = L_{\text{primary}}(\theta) + \lambda \, L_{\phi}(\theta)$$

with $\phi$ optimized through outer-loop gradients to maximize the primary objective. The learned auxiliary loss can encode auxiliary tasks, regularizers, or representation-learning objectives that support the primary objective without being explicitly designed. [Wichrowska Maheswaranathan Hoffman Colmenarejo Denil de Freitas Sohl-Dickstein 2017][research_wichrowska_et_al_2017] provided scaled-up learned optimizers with cross-task generalization, and [Chen Hoffman Colmenarejo Denil Lillicrap de Freitas 2017][research_chen_et_al_2017_learned_optimizer] demonstrated that learned optimizers can generalize appreciably beyond the training distribution when trained on diverse task ensembles.

## Multi-Task Reinforcement Learning

Multi-task reinforcement learning treats the setting in which the agent learns a shared policy or value function across many related tasks simultaneously. The account overlaps greatly with meta-learning but has distinctive algorithmic considerations.

Shared representation multi-task learning trains a single network with task-heads,

$$Q(s, a; \phi_{\text{shared}}, \phi_{\text{task}}) = h_{\phi_{\text{task}}}(f_{\phi_{\text{shared}}}(s, a))$$

with shared parameters $\phi_{\text{shared}}$ trained on all tasks and task-parameters $\phi_{\text{task}}$ trained only on the corresponding task. The mechanism supports positive transfer through shared representations while allowing task-specialization. Progressive Networks of [Rusu Rabinowitz Desjardins Soyer Kirkpatrick Kavukcuoglu Pascanu Hadsell 2016][research_rusu_et_al_2016_progressive] provided an alternative that avoids negative transfer by adding new columns for each task while freezing prior columns. Actor-Mimic of [Parisotto Ba Salakhutdinov 2016][research_parisotto_ba_salakhutdinov_2016] used policy distillation from single-task expert policies to a multi-task student policy, providing an alternative multi-task learning framework grounded in imitation learning. The [Sener and Koltun 2018][research_sener_koltun_2018] treatment of multi-task learning as multi-objective optimization provided a principled framework based on Pareto-optimality of the multi-task loss.

Multi-task actor-critic frameworks including [Teh Bapst Czarnecki Quan Kirkpatrick Hadsell de Freitas Heess 2017][research_teh_et_al_2017] Distral use distillation between task-and shared policies to encourage transferable behavior. Distral's task-policies are trained with a KL regularizer toward the shared distilled policy,

$$L_{\text{Distral}}(\pi_{\mathcal{T}}, \pi_0) = -J_{\mathcal{T}}(\pi_{\mathcal{T}}) + \alpha \, D_{\text{KL}}(\pi_{\mathcal{T}} \, \| \, \pi_0) - \beta \, H(\pi_{\mathcal{T}})$$

with $\pi_0$ trained to distill the ensemble of task-policies, encouraging shared structure to propagate through the distillation channel.

Negative interference between tasks is a persistent challenge. Learning gradient projection methods of [Yu Kumar Gupta Hausman Levine Finn 2020][research_yu_et_al_2020_pcgrad] PCGrad address negative interference by projecting each task's gradient onto the space orthogonal to interfering directions from other tasks. For each task pair with gradients $g_i, g_j$ where $g_i \cdot g_j < 0$, PCGrad replaces $g_i$ with its projection

$$g_i^{\text{PC}} = g_i - \frac{g_i \cdot g_j}{\|g_j\|^2} g_j$$

removing the conflicting component before averaging across the multi-task ensemble.

## Task Distribution Design and Automatic Curriculum

The design of the meta-training task distribution has marked effect on the resulting meta-learner. A distribution that is too narrow produces meta-learners that specialize to the training tasks without providing useful transfer to novel tasks. A distribution that is too broad produces meta-learners that adapt slowly because the meta-prior cannot support strong fast-adaptation structure. Task distribution design has thus emerged as an active research area distinct from the meta-learning algorithm design itself.

Manually-curated task distributions such as Meta-World and Alchemy provide the empirical benchmarks against which meta-learning methods are compared. The choice of task distribution however has strong effects on the ranking of meta-learning algorithms, and results that hold on one distribution often fail to generalize to others. Modern practice emphasizes evaluating across multiple task distributions to assess robustness of meta-learning methods to distributional choice.

Automatic curriculum construction provides an alternative to manual task-distribution design. Rather than specifying the training distribution directly, the meta-training procedure searches over tasks to construct a curriculum that maximizes some notion of learning progress. The model connects to the developmental robotics tradition treated in article twelve and to the intrinsic motivation methods treated in article five.

Teacher-Student Curriculum Learning of [Portelas Colas Hofmann Oudeyer 2019][research_portelas_et_al_2019] provided one systematic framework. A teacher policy $\pi_{\text{teacher}}(\mathcal{T})$ proposes tasks that maximize expected learning progress of the student, quantified as the change in expected return per unit training compute. The teacher is trained by reinforcement learning with learning progress as the reward, producing task distributions that automatically adapt to the current capability of the student.

POET of [Wang Lehman Clune Stanley 2019][research_wang_et_al_2019_poet] extended the model to open-ended coevolution of environments and agents. New environments are proposed by mutating existing environments, and environments that are neither too easy nor too hard for the current agent population are preserved. This formulation produces continually-expanding sets of environments and agents that co-adapt over evolutionary time.

Unsupervised Environment Design of [Dennis Jaques Hughes Gleave Wang Peng Turner Foerster Torr Stone 2020][research_dennis_et_al_2020_paired] PAIRED introduced a game-theoretic formulation in which an adversarial environment generator proposes environments that maximize the regret of the current agent against an antagonist policy. The regret objective automatically balances difficulty and learnability, producing environments that are challenging but solvable at the agent's current capability level.

Reverse curriculum of [Florensa Held Geng Abbeel 2018][research_florensa_et_al_2018_reverse_curriculum] provided a related framework for goal-conditioned reinforcement learning in which the curriculum is generated by starting near the goal state and progressively expanding outward. This account is particularly effective for sparse-reward manipulation tasks where random exploration would fail to encounter reward. Prioritized Level Replay of [Jiang Grefenstette Rocktäschel 2020][research_jiang_grefenstette_rocktaschel_2020] adapted prioritized-replay ideas to procedurally-generated environments, sampling levels that maximize learning progress.

Automatic Curriculum Learning of [Portelas Romac Hofmann Oudeyer 2020][research_portelas_et_al_2020_acl_survey] provided a systematic survey of the automatic curriculum literature circa the early 2020s. The framework connects meta-learning to the broader intelligent-tutoring-system and self-paced-learning traditions.

## Meta-Overfitting and Meta-Generalization

Meta-learning methods are prone to a distinctive failure mode of meta-overfitting, in which the meta-learner memorizes task-information from the meta-training tasks rather than acquiring genuine fast-adaptation capability. Meta-overfitting manifests as strong performance on meta-training tasks but poor performance on held-out tasks from the same distribution, even when the adaptation trajectory would in principle suffice to identify the task.

The [Yin Tucker Zhou Levine Finn 2020][research_yin_et_al_2020_memorization] Meta-Learning without Memorization framework provided the systematic diagnosis. The account identified that when the task distribution admits a shortcut solution, in which the task-conditional policy can be constructed without inspecting the adaptation data, gradient-based meta-learning methods often converge to the shortcut solution rather than the intended fast-adaptation solution. The proposed remedy is a mutual-information regularizer that forces the adapted parameters to depend on the adaptation data.

Meta-overfitting is closely related to the meta-generalization gap, defined as the difference between meta-training and meta-test performance. The gap widens with the effective complexity of the meta-learner and narrows with the number of meta-training tasks. Empirical scaling analyses of [Al-Shedivat Diaz-Rodriguez Guo Hospedales 2021][research_al_shedivat_et_al_2021_meta_generalization] documented that many meta-learning methods on standard benchmarks require considerably more tasks than the typical evaluation protocol provides for reliable meta-generalization.

The related failure mode of meta-underfitting occurs when the meta-learner fails to acquire task-adaptation and instead produces a task-agnostic policy that achieves mediocre performance across the distribution. Meta-underfitting is often caused by insufficient meta-training data, inadequate meta-learner capacity, or overly-constrained inner-loop update rules.

Robust meta-learning approaches address distribution shift between meta-training and meta-testing task distributions. Task augmentation via mixup, task interpolation, and adversarial task construction have all been proposed as regularizers that improve out-of-distribution meta-generalization. The [Yao Wei Huang Wang Li 2021][research_yao_et_al_2021_task_augmentation] task augmentation framework provided a systematic treatment of the meta-learning analogue of data augmentation.

## Continual and Online Adaptation

Continual adaptation extends the meta-learning framework to settings in which the agent faces a sequence of related tasks and must adapt to each without forgetting the previous ones. The model connects meta-learning to the continual learning of article ten.

Online adaptation via meta-learning of [Nagabandi Clavera Liu Fearing Abbeel Levine Finn 2018][research_nagabandi_et_al_2018_meta_online] provides the direct link between meta-learning and continual online adaptation. This formulation trains a meta-learned initialization such that few-shot gradient updates produce task-parameters that generalize to unseen environmental conditions. At each online step, the current parameters are updated from the meta-initialization based on a sliding window of recent transitions,

$$\theta_t = \theta_{\text{meta}} - \alpha \sum_{s=1}^{k} \nabla_{\theta_{\text{meta}}} \ell(\theta_{\text{meta}}; \tau_{t-s})$$

where $\ell$ is the per-transition prediction loss. Applied to legged robot control, this formulation enables rapid adaptation to novel terrain, actuator faults, and payload variations through a small number of online gradient steps.

Continuous Adaptation via Meta-Learning (CAML) of [Al-Shedivat Bansal Burda Sutskever Mordatch Abbeel 2018][research_al_shedivat_et_al_2018] extended MAML to continuously-changing environments in multi-agent settings where the changing behavior of other agents produces non-stationarity.

MOLe of [Nagabandi Finn Levine 2019][research_nagabandi_finn_levine_2019_mole] developed a mixture-of-experts framework for continual adaptation that identifies task boundaries and switches among meta-learned expert policies, providing a middle ground between pure meta-learning and pure continual learning. Reconciling meta-learning and continual learning through Bayesian nonparametrics, [Jerfel Grant Griffiths Heller 2019][research_jerfel_et_al_2019] proposed a Dirichlet-process mixture over meta-learned initializations that automatically identifies task clusters and enables backward transfer across the sequence of tasks. [Caccia Rodríguez Ostapenko Normandin Lin et al 2020][research_caccia_et_al_2020] provided the OSAKA benchmark and framework for online fast adaptation in continual meta-learning, exposing the tension between meta-adaptation speed and long-run non-forgetting.

## In-Context Reinforcement Learning

In-context reinforcement learning extends the in-context learning of large language models to the reinforcement learning setting. This account treats meta-learning as sequence modeling. A transformer trained on a distribution of learning-algorithm traces produces reinforcement learning behavior at test time by autoregressively predicting the algorithm's next action.

Algorithm Distillation of Laskin Wang Oh Parisotto Spencer et al 2023 provided the systematic treatment. A transformer is trained on trajectories

$$\tau = (o_1, a_1, r_1, o_2, a_2, r_2, \ldots)$$

where the trajectory represents the entire learning-algorithm trace over the lifetime of an agent solving a task. The transformer is trained by autoregressive cross-entropy on trajectory-conditional action prediction,

$$L_{\text{AD}}(\theta) = -\mathbb{E}_{\tau \sim \mathcal{D}_{\text{learn}}}\!\left[\sum_t \log \pi_\theta(a_t \mid \tau_{1:t-1})\right]$$

where $\mathcal{D}_{\text{learn}}$ is a dataset of learning-algorithm traces across a distribution of tasks. At test time the transformer predicts $a_t$ conditional on $\tau_{1:t-1}$ and produces increasingly-competent actions as more trajectory context is provided. The mechanism is remarkably general. Any learning algorithm can be distilled into an in-context transformer by generating training traces from the algorithm.

Adaptive Agent of Bauer et al 2023 combined meta-reinforcement learning with foundation-model-scale training on the XLand environment, achieving rapid adaptation across a vast distribution of tasks. The agent demonstrates task-inference-like behavior at test time without explicit task representation, using its transformer sequence model to condition on trajectory context.

In-context reinforcement learning connects meta-learning to the sequence modeling framework of articles four and eight and to the foundation model treatments throughout the series. The relationship between in-context learning as a compression of learning algorithms and traditional meta-learning as a parameterization of learning algorithms remains an active research area.

Related work by [Kirsch Harrison Sohl-Dickstein Metz 2022][research_kirsch_et_al_2022] on general-purpose in-context meta-learning provided a systematic framework connecting in-context learning to classical meta-learning theory. Supervised pretraining approaches of [Lee et al 2023][research_lee_et_al_2023_supervised_pretraining] demonstrated that supervised learning on cross-task trajectory data can produce in-context reinforcement learning behavior comparable to specialized meta-reinforcement learning algorithms.

## Meta-Learning Theory and Sample Complexity

The theoretical foundations of meta-learning provide sample complexity bounds that quantify when meta-learning provides advantages over independent per-task learning. The framework of [Baxter 2000][research_baxter_2000] provided the early Bayesian analysis of learning across task distributions, establishing that shared task structure enables sample-complexity gains proportional to the effective task-representation dimension.

The generalization bound for meta-learning takes the form

$$\mathbb{E}_{\mathcal{T} \sim p(\mathcal{T})}[R(\mathcal{A}_\phi, \mathcal{T})] \leq \hat{R}_{\text{meta}}(\mathcal{A}_\phi) + \mathcal{O}\!\left(\sqrt{\frac{\text{Comp}(\mathcal{A})}{n_{\text{tasks}} m_{\text{per-task}}}}\right)$$

where $\text{Comp}(\mathcal{A})$ is a complexity measure of the meta-algorithm class, $n_{\text{tasks}}$ is the number of meta-training tasks, and $m_{\text{per-task}}$ is the number of samples per task. When the effective algorithm-class complexity is smaller than the model-class complexity for per-task learning, meta-learning provides sample-complexity advantages.

Modern analyses including [Denevi Ciliberto Grazzi Pontil 2019][research_denevi_et_al_2019] and [Khodak Balcan Talwalkar 2019][research_khodak_balcan_talwalkar_2019] provide refined bounds for gradient-based meta-learning under favorable geometric assumptions on the task loss landscape. The [Balcan Blum Sharma 2018][research_balcan_blum_sharma_2018] work on algorithm design principles for meta-learning extended the framework to structured hypothesis classes.

The theory of PAC-Bayesian meta-learning provides bounds that are often practical to compute and use for meta-algorithm selection. The [Amit and Meir 2018][research_amit_meir_2018] PAC-Bayes bounds for meta-learning and the [Rothfuss Fortuin Josifoski Krause 2021][research_rothfuss_et_al_2021_pacoh] PACOH framework for principled Bayesian meta-learning provided the modern development. The account connects meta-learning to broader statistical learning theory and clarifies when meta-learning theoretical guarantees hold.

Convergence analyses of MAML including [Fallah Mokhtari Ozdaglar 2020][research_fallah_mokhtari_ozdaglar_2020] established sample-complexity bounds for gradient-based meta-learning under standard smoothness conditions, providing theoretical justification for the empirical success of first-order MAML variants.

Sample-complexity analyses to meta-reinforcement learning remain limited by the difficulty of the underlying reinforcement learning setting. Bounds tend to require restrictive assumptions on the MDP class and adaptation procedure, and empirical performance often exceeds theoretical predictions.

## Model-Based Meta-Reinforcement Learning

Model-based meta-reinforcement learning combines the sample-efficiency advantages of the model-based methods treated in article seven with the fast adaptation of meta-learning. The model meta-learns a world model that adapts rapidly to new tasks, then uses the adapted model for planning or model-based policy optimization.

The Nagabandi et al 2018 deep online adaptation via meta-learning framework treated earlier provides the direct instantiation. A meta-learned dynamics model rapidly adapts to novel environmental conditions through few-shot gradient updates, and the adapted model is used for model-based control via MPC. This formulation achieves significantly better real-robot adaptation efficiency than model-free alternatives.

Model-based meta-policy optimization of [Clavera Rothfuss Schulman Fujita Asfour Abbeel 2018][research_clavera_et_al_2018] combined MAML with model-based reinforcement learning through ensemble dynamics models. The mechanism supports uncertainty-aware planning during meta-testing when the task is not fully identified. Learning-to-adapt for legged robotics of [Nagabandi Finn Levine 2018][research_nagabandi_finn_levine_2018_learn_to_adapt] applied a similar framework to real-robot control and provided evidence that model-based meta-learning generalizes to physical hardware with acceptable data budgets.

Latent-variable model-based meta-learning approaches condition the world model on a latent task embedding

$$\hat{P}_\theta(s' \mid s, a, z_{\text{task}}), \quad q_\phi(z_{\text{task}} \mid \tau_{1:H})$$

with the task embedding inferred from a short adaptation trajectory. The joint training objective combines observation reconstruction under the task-conditioned model with a variational regularizer,

$$L_{\text{TCWM}}(\theta, \phi) = -\mathbb{E}_{q_\phi(z \mid \tau)}\!\left[\sum_t \log \hat{P}_\theta(s_{t+1} \mid s_t, a_t, z)\right] + \beta \, D_{\text{KL}}(q_\phi(z \mid \tau) \, \| \, p(z))$$

The treatment supports zero-shot generalization to new tasks that share structure with the training distribution through the shared world model.

Recent developments including task-conditioned world models in the Dreamer family provide model-based meta-learning at foundation-model scale. The relationship between meta-learning and generalist agents is bidirectional. Meta-learning provides principled adaptation mechanisms for generalist agents, and generalist agents provide the task-scaled infrastructure for meta-learning to reach practical relevance.

## Cross-Embodiment and Foundation-Scale Meta-Reinforcement Learning

The foundation-model paradigm has substantially reshaped the practice of meta-reinforcement learning in the mid 2020s. Rather than training specialized meta-learners on hand-curated task distributions, foundation-scale meta-reinforcement learning trains large sequence models on vast collections of experience data spanning many embodiments, tasks, and modalities.

Gato of [Reed Zolna Parisotto Colmenarejo Novikov Barth-Maron Giménez et al 2022][research_reed_et_al_2022_gato] demonstrated that a single 1.2-billion-parameter transformer trained on tokenized experience data from 604 distinct tasks including robotics, Atari, image captioning, and dialogue can perform all tasks competitively at test time by conditioning on task identity. This account does not perform meta-adaptation in the traditional sense, but exhibits in-context task inference through the shared sequence model.

RT-1 of [Brohan Brown Carbajal Chebotar Dabis et al 2022][research_brohan_et_al_2022_rt1] and RT-2 of [Brohan Brown Carbajal Chebotar Chen et al 2023][research_brohan_et_al_2023_rt2] extended the account to real-robot manipulation across diverse tasks and objects. RT-2's contribution was the integration of pretrained vision-language models with reinforcement learning trajectory data, enabling zero-shot generalization to novel objects and instructions through the shared representational structure of the underlying foundation model.

Cross-embodiment meta-learning of [Open X-Embodiment Collaboration et al 2023][research_open_x_embodiment_2023] demonstrated that policies trained jointly on data from 22 different robotic embodiments outperform embodiment-baselines on held-out embodiments, providing evidence for positive transfer across markedly different action and observation spaces. The account connects meta-reinforcement learning to the broader multimodal foundation model literature and establishes an emerging pattern of scaled cross-domain training.

The relationship between foundation-scale meta-learning and traditional specialized meta-learning remains an open research question. Traditional meta-learners achieve strong adaptation from small task distributions with modest compute budgets, while foundation-scale meta-learners achieve broad generalization with extensive compute and data investment. The two approaches likely complement rather than substitute for one another in the mature engineering practice.

Instruction-following meta-learning provides a related direction connecting meta-reinforcement learning to language-conditioned control. Language-instructed manipulation, navigation, and dialogue policies exhibit in-context adaptation to novel task specifications provided through natural language, effectively performing task inference through language rather than through trajectory observations. The model connects to the reinforcement learning from human feedback approaches of the language model literature.

## Sim-to-Real Adaptation and Domain Randomization

Sim-to-real transfer is a longstanding problem in robotics that has a close but distinct relationship to meta-reinforcement learning. Sim-to-real methods train policies in simulation and deploy them on physical hardware, which requires the trained policy to generalize to the sim-to-real gap of unmodeled physical effects.

Domain randomization of [Tobin Fong Ray Schneider Zaremba Abbeel 2017][research_tobin_et_al_2017_dr] provides the canonical alternative to meta-learning for sim-to-real transfer. Rather than meta-training on a distribution of tasks with the intent of enabling test-time adaptation, domain randomization trains a single robust policy on a distribution of simulated environments with randomized physical parameters, resulting in a policy that performs adequately across the randomization distribution without further adaptation.

Formally, domain randomization solves

$$\pi^*_{\text{DR}} = \arg\max_\pi \mathbb{E}_{\mathcal{T} \sim p(\mathcal{T})}\!\left[J_{\mathcal{T}}(\pi)\right]$$

which is the multi-task objective without task-adaptation. This formulation produces zero-shot generalization to any task in the randomization support at the cost of task-optimality.

Dynamics randomization of [Peng Andrychowicz Zaremba Abbeel 2018][research_peng_et_al_2018_dynamics_rand] extended domain randomization to dynamical properties including mass, friction, and actuator characteristics. The treatment combined with LSTM policies produced appreciably better sim-to-real transfer for legged robotics than either component alone.

Adaptive domain randomization approaches combine the two paradigms. The [Akkaya Andrychowicz Chociej Litwin McGrew Petron Paino Plappert et al 2019][research_openai_et_al_2019_rubiks] Rubik's Cube framework used automatic domain randomization to progressively expand the randomization distribution during training, producing policies that transferred to physical hand manipulation. The policy retained sufficient adaptation capability through the LSTM recurrence to specialize to the physical hand at deployment time.

The tradeoff between domain randomization and meta-learning is subtle. Domain randomization requires no test-time compute for adaptation but requires the randomization distribution to encompass the deployment conditions. Meta-learning tolerates deployment conditions outside the training distribution when the adaptation trajectory reveals the discrepancy, at the cost of test-time adaptation compute. In practice modern robotics systems often combine both approaches, using domain randomization to establish a robust prior policy and meta-adaptation to specialize to the deployment environment.

The related framework of system identification meta-learning of [Yu Tan Bai Xu Liu 2017][research_yu_et_al_2017_sysid] used a small adaptation trajectory to identify physical parameters of the deployment environment, then used the identified parameters to select or specialize a policy. This account provides a middle ground between pure meta-learning and pure domain randomization by making the task representation explicit and physically-interpretable.

## Empirical Landscape

The empirical landscape of meta-reinforcement learning has consolidated around several standard benchmarks. Meta-World of [Yu Quillen He Julian Hausman Finn Levine 2020][research_yu_et_al_2020_metaworld] provides a suite of fifty robotic manipulation tasks that share the same robot embodiment but require distinct manipulation skills. The benchmark supports both meta-training on a subset and evaluation on held-out tasks and multi-task training on the full set.

Procgen and the Procgen-based generalization benchmarks provide procedurally-generated video games that test generalization across the procedural distribution rather than adaptation to fixed tasks. The distinction between generalization and meta-learning is subtle. Pure generalization requires no test-time adaptation, while meta-learning explicitly optimizes for it.

Alchemy of [Wang et al 2021][research_wang_et_al_2021_alchemy] provides a specifically-designed meta-reinforcement learning benchmark with hidden structural rules that must be inferred through experimentation. The benchmark exposes the exploration-versus-exploitation trade-off that Bayes-optimal meta-learning should navigate.

XLand of [Team et al 2021][research_team_et_al_2021_xland] provides a vast procedurally-generated 3D environment that has served as a test-bed for foundation-model-scale meta-reinforcement learning. Adaptive Agent's performance on XLand provides evidence for the scalability of transformer-based in-context meta-reinforcement learning.

Empirical performance across these benchmarks shows several patterns. Recurrent meta-learning through RL-squared and L2RL provides strong performance when meta-training data is abundant. Gradient-based methods including MAML and ProMP provide better sample efficiency at meta-test time but require more careful meta-training. Bayesian methods including PEARL and VariBAD provide the strongest exploration behavior at higher implementation complexity. In-context methods including Algorithm Distillation and Adaptive Agent provide the most flexible framework but require foundation-model-scale training.

MiniHack of [Samvelyan Kirk Kurin et al 2021][research_samvelyan_et_al_2021_minihack] provides a diverse and configurable NetHack-based environment specifically designed for meta-reinforcement learning research. NLE of [Küttler Nardelli et al 2020][research_kuttler_et_al_2020_nle] provides the underlying NetHack Learning Environment that has served as one of the most challenging open benchmarks for reinforcement learning generalization.

Crafter of [Hafner 2022][research_hafner_2022_crafter] provides a Minecraft-inspired procedurally-generated benchmark that supports both meta-learning and long-horizon reinforcement learning research with greatly lower computational requirements than 3D game engines.

Empirical comparison across meta-reinforcement learning benchmarks is complicated by the sensitivity of results to hyperparameter choices, task distribution details, and evaluation protocols. Standardized evaluation practices are an active area of methodological development.

## Applications

Fast robotic adaptation is the most-developed application of meta-reinforcement learning. Legged robots that adapt to novel terrain in real time, manipulators that adapt to novel objects, and grippers that adapt to novel grasping conditions all benefit from meta-learned initialization or task inference. The Nagabandi et al 2018 real-robot demonstrations provided early evidence, and subsequent work has extended to broader classes of robotic tasks.

Personalized medicine treats meta-reinforcement learning as a framework for adapting general treatment policies to individual patient characteristics. The task distribution corresponds to the distribution of patients, and adaptation to a patient occurs through their treatment response history. The framework has been applied to individualized dosing, chronic disease management, and behavior change interventions.

Educational and tutoring systems use meta-reinforcement learning to adapt tutoring policies to individual learners. The task distribution corresponds to learners with varying prior knowledge and learning speeds, and adaptation occurs through the learner's response to instruction.

Recommender systems apply meta-learning to cold-start problems in which new users or new items have limited interaction history. Meta-learned initialization or task inference produces reasonable initial recommendations that improve rapidly with interaction data.

Autonomous driving uses meta-learning for driving-context adaptation. Different weather conditions, road types, and traffic scenarios present distinct control challenges that benefit from a meta-learned adaptive controller.

Financial and trading applications treat meta-reinforcement learning as a framework for adapting trading policies to individual market regimes, with the task distribution corresponding to the distribution of market conditions across historical periods.

Wireless network resource allocation uses meta-reinforcement learning to adapt scheduling and beamforming policies to varying network topologies and user distributions, connecting meta-learning to online-learning approaches in the communications engineering literature.

## Software Frameworks and Reproducibility

The practical realization of meta-reinforcement learning depends on software tooling for differentiating through inner-loop training procedures, managing task distributions, and reproducing benchmark results. Several open-source frameworks have emerged to support the practical work.

Higher of [Grefenstette Amos Yarats Htut Riedel Chintala 2019][research_grefenstette_et_al_2019_higher] provides a PyTorch extension for computing higher-order gradients through arbitrary training loops. The account is the standard tool for implementing MAML and related gradient-based meta-learning methods, supporting both first-order and full second-order gradients through a functional module rewrite.

Learn2learn of [Arnold Mahajan Datta Bunner Zarkias 2020][research_arnold_et_al_2020_learn2learn] provides a broader library of meta-learning algorithms and benchmarks. The library implements MAML, ANIL, Reptile, PEARL, matching networks, prototypical networks, and other standard methods on both few-shot supervised and meta-reinforcement learning benchmarks.

Torchmeta of [Deleu Warde-Farley Sygnowski Bengio 2019][research_deleu_et_al_2019_torchmeta] provides an alternative library focused on few-shot supervised meta-learning with support for standard benchmarks including Omniglot and miniImageNet. The library provides task-generator utilities that abstract away the boilerplate of episode construction.

Garage of [Duan Chen Houthooft Schulman Abbeel 2016 et al][research_duan_et_al_garage] and its successor libraries provide reinforcement-learning-implementations of PEARL, MAML, RL-squared, and related methods. The model enables direct benchmark comparison across meta-reinforcement learning algorithms with consistent evaluation protocols.

Reproducibility of meta-reinforcement learning results has been a persistent challenge. The [Henderson Islam Bachman Pineau Precup Meger 2018][research_henderson_et_al_2018_reproducibility] analysis of reinforcement learning reproducibility documented sizable variation in reported results across random seeds and implementation details, and subsequent analyses have documented similar patterns to meta-reinforcement learning. The [Beck Vuorio Liu Xiong Zintgraf Finn Whiteson 2023][research_beck_et_al_2023_metarl_survey] survey of meta-reinforcement learning provided consolidated reproducibility guidelines that are increasingly adopted in the modern practice.

Standardization of benchmark protocols including consistent task distributions, evaluation horizons, and adaptation budgets has become a research priority. Meta-World v2 in particular introduced standardized benchmarking that has improved cross-paper comparability. Ongoing work on Meta-RL reproducibility infrastructure continues to strengthen the empirical foundation of the field.

## Neuroscience Connections

The prefrontal cortex has been proposed as implementing meta-reinforcement learning in biological brains. The [Wang Kurth-Nelson Tirumala Soyer Leibo Munos Blundell Kumaran Botvinick 2018][research_wang_et_al_2018_prefrontal] framework proposed that the prefrontal cortex functions as a meta-reinforcement learning system in which recurrent activity supports fast adaptation across tasks while slower dopaminergic updates train the recurrent weights themselves. The proposal provides a computational-level explanation for prefrontal cortex behavior across a wide range of experimental paradigms.

This formulation predicts that lesions to prefrontal cortex should impair fast adaptation but leave slow reinforcement learning intact. The prediction is broadly consistent with the neuropsychological literature on prefrontal damage, though the specificity of the mapping remains under investigation.

[Botvinick et al 2019][research_botvinick_et_al_2019_meta] provided a broader review of the neuroscience-machine-learning connection, treating meta-reinforcement learning as a instance of the broader principle that the brain implements algorithms shaped by evolutionary and developmental meta-learning across distributions of environmental challenges.

Dopamine-based reinforcement signals continue to play their role in the meta-learning framework. Dopamine provides the outer-loop training signal for the meta-learned recurrent computation, while the recurrent computation implements the inner-loop task-policy. The two-timescale structure aligns with dual-system models of prefrontal cortex function.

Human meta-learning behavior in laboratory tasks has been documented at length. Humans exhibit rapid adaptation to novel task structure that is difficult to explain without prior meta-learned knowledge. Behavioral signatures including few-shot generalization, task-inference-driven exploration, and rapid re-adaptation to previously-solved tasks all show correspondence with computational meta-reinforcement learning predictions. [Dasgupta Schulz Chater Gershman 2020][research_dasgupta_schulz_chater_gershman_2020] proposed that human meta-learning behavior in structured environments is well-modeled by resource-rational Bayesian meta-learning, providing a normative framework that connects behavioral signatures to computational-level accounts. Computational-cognitive accounts of task-general learning by [Lake Ullman Tenenbaum Gershman 2017][research_lake_et_al_2017] argued that human-level meta-learning requires structured causal models of the task-generating process rather than purely-statistical adaptation.

Article fourteen returns to the NeuroAI bridge and treats the meta-reinforcement learning correspondence in greater detail.

## Load-Bearing Open Questions

- What is the correct theoretical framework for meta-reinforcement learning under weak task-distribution structure? Current bounds assume favorable geometric or Bayesian conditions that may not hold in practice.
- How can meta-learning generalize beyond the meta-training task distribution? Current methods generalize well within the distribution but often poorly to out-of-distribution tasks.
- What is the correct relationship between meta-learning and in-context learning in foundation models? Empirical results suggest close correspondence but the theoretical basis remains unclear.
- How should meta-learning handle non-stationary task distributions? Current methods assume the task distribution is fixed during meta-training but this assumption often fails in practice.
- Can meta-learning be scaled to the foundation model regime while retaining the sample-efficiency advantages? Current large-scale approaches lose the fast-adaptation properties of specialized meta-learners.
- What is the correct treatment of the exploration-exploitation trade-off during meta-testing? Bayesian meta-learning provides one answer but is computationally expensive, while simpler methods trade optimality for tractability.
- How closely do the meta-learning mechanisms of biological brains correspond to machine learning meta-learning algorithms?
- Can meta-learning be reliably combined with hierarchical decomposition and model-based planning?

## References

### Books

- [Duff 2002][book_duff_2002]
- [Sutton and Barto 2018][book_sutton_barto_2018]
- [Thrun and Pratt 1998][book_thrun_pratt_1998]

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
- [A256 Machines That Learn From Experience World Models and Predictive Model-Based Adaptation][related_post_a256_world_models]
- [A257 Machines That Learn From Experience Offline and Batch Reinforcement Learning][related_post_a257_offline]

### Research

- [Akkaya et al 2019 Rubik's Cube][research_openai_et_al_2019_rubiks]
- [Al-Shedivat Bansal Burda Sutskever Mordatch Abbeel 2018][research_al_shedivat_et_al_2018]
- [Al-Shedivat Diaz-Rodriguez Guo Hospedales 2021][research_al_shedivat_et_al_2021_meta_generalization]
- [Amit and Meir 2018][research_amit_meir_2018]
- [Andrychowicz et al 2016][research_andrychowicz_et_al_2016]
- [Antoniou Edwards Storkey 2019][research_antoniou_edwards_storkey_2019]
- [Arnold et al 2020 learn2learn][research_arnold_et_al_2020_learn2learn]
- [Balcan Blum Sharma 2018][research_balcan_blum_sharma_2018]
- [Barreto et al 2017 Successor Features][research_barreto_et_al_2017]
- [Bauer et al 2023 Adaptive Agent][research_bauer_et_al_2023_ada]
- [Baxter 2000][research_baxter_2000]
- [Beck Vuorio Liu Xiong Zintgraf Finn Whiteson 2023 Meta-RL Survey][research_beck_et_al_2023_metarl_survey]
- [Bengio Bengio Cloutier 1990][research_bengio_bengio_cloutier_1990]
- [Botvinick et al 2019][research_botvinick_et_al_2019_meta]
- [Brohan et al 2022 RT-1][research_brohan_et_al_2022_rt1]
- [Brohan et al 2023 RT-2][research_brohan_et_al_2023_rt2]
- [Caccia et al 2020 OSAKA][research_caccia_et_al_2020]
- [Chen Hoffman Colmenarejo Denil Lillicrap de Freitas 2017][research_chen_et_al_2017_learned_optimizer]
- [Clavera Rothfuss Schulman Fujita Asfour Abbeel 2018][research_clavera_et_al_2018]
- [Dasgupta Schulz Chater Gershman 2020][research_dasgupta_schulz_chater_gershman_2020]
- [Deleu et al 2019 Torchmeta][research_deleu_et_al_2019_torchmeta]
- [Denevi Ciliberto Grazzi Pontil 2019][research_denevi_et_al_2019]
- [Dennis et al 2020 PAIRED][research_dennis_et_al_2020_paired]
- [Dorfman Shenfeld Tamar 2021][research_dorfman_shenfeld_tamar_2021]
- [Duan Schulman Chen Bartlett Sutskever Abbeel 2016 RL2][research_duan_et_al_2016_rl2]
- [Duan et al Garage][research_duan_et_al_garage]
- [Fakoor Chaudhari Soatto Smola 2020][research_fakoor_et_al_2020_mql]
- [Fallah Mokhtari Ozdaglar 2020][research_fallah_mokhtari_ozdaglar_2020]
- [Finn Abbeel Levine 2017 MAML][research_finn_abbeel_levine_2017]
- [Finn Rajeswaran Kakade Levine 2019 Online Meta-Learning][research_finn_rajeswaran_kakade_levine_2019]
- [Flennerhag et al 2022 Bootstrapped Meta-Learning][research_flennerhag_et_al_2022]
- [Florensa et al 2018 Reverse Curriculum][research_florensa_et_al_2018_reverse_curriculum]
- [Grant Finn Levine Darrell Griffiths 2018 Bayesian MAML][research_grant_finn_levine_darrell_griffiths_2018]
- [Grefenstette et al 2019 higher][research_grefenstette_et_al_2019_higher]
- [Guez Silver Dayan 2013 BAMCP][research_guez_silver_dayan_2013]
- [Ha Dai Le 2016 HyperNetworks][research_ha_dai_le_2016]
- [Hafner 2022 Crafter][research_hafner_2022_crafter]
- [Henderson et al 2018 Reproducibility][research_henderson_et_al_2018_reproducibility]
- [Hochreiter Younger Conwell 2001][research_hochreiter_younger_conwell_2001]
- [Hospedales Antoniou Micaelli Storkey 2022][research_hospedales_et_al_2022]
- [Humplik Igl Duan et al 2019][research_humplik_et_al_2019]
- [Jerfel Grant Griffiths Heller 2019][research_jerfel_et_al_2019]
- [Jiang Grefenstette Rocktäschel 2020 PLR][research_jiang_grefenstette_rocktaschel_2020]
- [Khodak Balcan Talwalkar 2019][research_khodak_balcan_talwalkar_2019]
- [Kirsch Harrison Sohl-Dickstein Metz 2022][research_kirsch_et_al_2022]
- [Kirsch Sohl-Dickstein Metz 2019 MetaGenRL][research_kirsch_sohl_dickstein_metz_2019]
- [Koch Zemel Salakhutdinov 2015 Siamese][research_koch_zemel_salakhutdinov_2015]
- [Küttler et al 2020 NLE][research_kuttler_et_al_2020_nle]
- [Lake Ullman Tenenbaum Gershman 2017][research_lake_et_al_2017]
- [Laskin et al 2023 Algorithm Distillation][research_laskin_et_al_2023]
- [Lee et al 2023 Supervised Pretraining][research_lee_et_al_2023_supervised_pretraining]
- [Li and Malik 2017][research_li_malik_2017]
- [Metz Maheswaranathan Cheung Sohl-Dickstein 2019][research_metz_et_al_2019]
- [Mishra et al 2018 SNAIL][research_mishra_et_al_2018_snail]
- [Nagabandi Clavera Liu Fearing Abbeel Levine Finn 2018][research_nagabandi_et_al_2018_meta_online]
- [Nagabandi Finn Levine 2018 Learn to Adapt][research_nagabandi_finn_levine_2018_learn_to_adapt]
- [Nagabandi Finn Levine 2019 MOLe][research_nagabandi_finn_levine_2019_mole]
- [Naik and Mammone 1992][research_naik_mammone_1992]
- [Ni Eysenbach Levine 2022][research_ni_eysenbach_levine_2022]
- [Nichol Achiam Schulman 2018 Reptile][research_nichol_achiam_schulman_2018]
- [Oh Guo Warde-Farley Wayne Ostrovski Silver 2020][research_oh_et_al_2020]
- [Open X-Embodiment Collaboration 2023][research_open_x_embodiment_2023]
- [Ortega Wang Rowland Genewein Hutter et al 2019][research_ortega_et_al_2019]
- [Parisotto Ba Salakhutdinov 2016 Actor-Mimic][research_parisotto_ba_salakhutdinov_2016]
- [Peng Andrychowicz Zaremba Abbeel 2018 Dynamics Randomization][research_peng_et_al_2018_dynamics_rand]
- [Portelas Colas Hofmann Oudeyer 2019 Teacher-Student][research_portelas_et_al_2019]
- [Portelas Romac Hofmann Oudeyer 2020 ACL Survey][research_portelas_et_al_2020_acl_survey]
- [Poupart Vlassis Hoey Regan 2006][research_poupart_et_al_2006]
- [Raghu Raghu Bengio Vinyals 2020 ANIL][research_raghu_raghu_bengio_vinyals_2020]
- [Rajeswaran Finn Kakade Levine 2019 iMAML][research_rajeswaran_et_al_2019_imaml]
- [Rakelly Zhou Quillen Finn Levine 2019 PEARL][research_rakelly_et_al_2019_pearl]
- [Ravi and Larochelle 2017][research_ravi_larochelle_2017]
- [Reed et al 2022 Gato][research_reed_et_al_2022_gato]
- [Rothfuss Fortuin Josifoski Krause 2021 PACOH][research_rothfuss_et_al_2021_pacoh]
- [Rothfuss Lee Clavera Asfour Abbeel 2019 ProMP][research_rothfuss_et_al_2019]
- [Rusu Rabinowitz Desjardins Soyer Kirkpatrick Kavukcuoglu Pascanu Hadsell 2016 Progressive Networks][research_rusu_et_al_2016_progressive]
- [Rusu Rao Sygnowski Vinyals Pascanu Osindero Hadsell 2019 LEO][research_rusu_et_al_2019_leo]
- [Sæmundsson Hofmann Deisenroth 2018][research_saemundsson_hofmann_deisenroth_2018]
- [Samvelyan et al 2021 MiniHack][research_samvelyan_et_al_2021_minihack]
- [Schmidhuber 1987][research_schmidhuber_1987_metalearning]
- [Schmidhuber Zhao Wiering 1996][research_schmidhuber_zhao_wiering_1996]
- [Sener and Koltun 2018][research_sener_koltun_2018]
- [Snell Swersky Zemel 2017 Prototypical Networks][research_snell_swersky_zemel_2017]
- [Sung Yang Zhang Xiang Torr Hospedales 2018 Relation Networks][research_sung_et_al_2018]
- [Team et al 2021 XLand][research_team_et_al_2021_xland]
- [Teh Bapst Czarnecki Quan Kirkpatrick Hadsell de Freitas Heess 2017 Distral][research_teh_et_al_2017]
- [Tobin et al 2017 Domain Randomization][research_tobin_et_al_2017_dr]
- [Vilalta and Drazdil 2002][research_vilalta_drazdil_2002]
- [Vinyals et al 2016 Matching Networks][research_vinyals_et_al_2016_matching]
- [Wang et al 2016 Learning to Reinforcement Learn][research_wang_et_al_2016_l2rl]
- [Wang et al 2018 Prefrontal Meta-RL][research_wang_et_al_2018_prefrontal]
- [Wang et al 2019 POET][research_wang_et_al_2019_poet]
- [Wang et al 2021 Alchemy][research_wang_et_al_2021_alchemy]
- [Wichrowska et al 2017 Learned Optimizers][research_wichrowska_et_al_2017]
- [Xu et al 2020 Meta-A2C][research_xu_et_al_2020_meta_a2c]
- [Xu van Hasselt Silver 2018 Meta-Gradient RL][research_xu_van_hasselt_silver_2018]
- [Yao et al 2021 Task Augmentation][research_yao_et_al_2021_task_augmentation]
- [Yin Tucker Zhou Levine Finn 2020 Memorization][research_yin_et_al_2020_memorization]
- [Yu Kumar Gupta Hausman Levine Finn 2020 PCGrad][research_yu_et_al_2020_pcgrad]
- [Yu Quillen He Julian Hausman Finn Levine 2020 Meta-World][research_yu_et_al_2020_metaworld]
- [Yu Tan Bai Xu Liu 2017 SysID][research_yu_et_al_2017_sysid]
- [Zahavy et al 2020 STAC][research_zahavy_et_al_2020_stac]
- [Zheng et al 2020 Learning Reward][research_zheng_et_al_2020_learning_reward]
- [Zheng Oh Singh 2018 LIRPG][research_zheng_oh_singh_2018_lirpg]
- [Zintgraf Feng Igl Whiteson 2021 HyperX][research_zintgraf_et_al_2021_hyperx]
- [Zintgraf Shiarlis Igl Schulze Gal Hofmann Whiteson 2020 VariBAD][research_zintgraf_et_al_2020_varibad]

[book_duff_2002]: https://www.cs.umass.edu/~mduff/duff_diss.pdf
[book_sutton_barto_2018]: http://incompleteideas.net/book/the-book-2nd.html
[book_thrun_pratt_1998]: https://link.springer.com/book/10.1007/978-1-4615-5529-2
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
[research_al_shedivat_et_al_2018]: https://openreview.net/forum?id=Sk2u1g-0-
[research_al_shedivat_et_al_2021_meta_generalization]: https://arxiv.org/abs/2106.15884
[research_amit_meir_2018]: https://proceedings.mlr.press/v80/amit18a.html
[research_arnold_et_al_2020_learn2learn]: https://arxiv.org/abs/2008.12284
[research_barreto_et_al_2017]: https://papers.nips.cc/paper/2017/hash/350db081a661525235354dd3e19b8c05-Abstract.html
[research_beck_et_al_2023_metarl_survey]: https://arxiv.org/abs/2301.08028
[research_brohan_et_al_2022_rt1]: https://arxiv.org/abs/2212.06817
[research_brohan_et_al_2023_rt2]: https://arxiv.org/abs/2307.15818
[research_deleu_et_al_2019_torchmeta]: https://arxiv.org/abs/1909.06576
[research_dennis_et_al_2020_paired]: https://papers.nips.cc/paper/2020/hash/985e9a46e10005356bbaf194249f6856-Abstract.html
[research_duan_et_al_garage]: https://github.com/rlworkgroup/garage
[research_florensa_et_al_2018_reverse_curriculum]: https://proceedings.mlr.press/v78/florensa17a.html
[research_grefenstette_et_al_2019_higher]: https://arxiv.org/abs/1910.01727
[research_ha_dai_le_2016]: https://openreview.net/forum?id=rkpACe1lx
[research_hafner_2022_crafter]: https://arxiv.org/abs/2109.06780
[research_henderson_et_al_2018_reproducibility]: https://ojs.aaai.org/index.php/AAAI/article/view/11694
[research_jiang_grefenstette_rocktaschel_2020]: https://arxiv.org/abs/2010.03934
[research_kirsch_sohl_dickstein_metz_2019]: https://arxiv.org/abs/1910.04098
[research_koch_zemel_salakhutdinov_2015]: https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf
[research_kuttler_et_al_2020_nle]: https://papers.nips.cc/paper/2020/hash/569ff987c643b4bedf504efda8f786c2-Abstract.html
[research_mishra_et_al_2018_snail]: https://openreview.net/forum?id=B1DmUzWAW
[research_open_x_embodiment_2023]: https://arxiv.org/abs/2310.08864
[research_openai_et_al_2019_rubiks]: https://arxiv.org/abs/1910.07113
[research_peng_et_al_2018_dynamics_rand]: https://arxiv.org/abs/1710.06537
[research_portelas_et_al_2019]: https://proceedings.mlr.press/v100/portelas20a.html
[research_portelas_et_al_2020_acl_survey]: https://arxiv.org/abs/2003.04664
[research_raghu_raghu_bengio_vinyals_2020]: https://openreview.net/forum?id=rkgMkCEtPB
[research_reed_et_al_2022_gato]: https://arxiv.org/abs/2205.06175
[research_rusu_et_al_2019_leo]: https://openreview.net/forum?id=BJgklhAcK7
[research_samvelyan_et_al_2021_minihack]: https://arxiv.org/abs/2109.13202
[research_snell_swersky_zemel_2017]: https://papers.nips.cc/paper/2017/hash/cb8da6767461f2812ae4290eac7cbc42-Abstract.html
[research_sung_et_al_2018]: https://openaccess.thecvf.com/content_cvpr_2018/html/Sung_Learning_to_Compare_CVPR_2018_paper.html
[research_tobin_et_al_2017_dr]: https://arxiv.org/abs/1703.06907
[research_vinyals_et_al_2016_matching]: https://papers.nips.cc/paper/2016/hash/90e1357833654983612fb05e3ec9148c-Abstract.html
[research_wang_et_al_2019_poet]: https://arxiv.org/abs/1901.01753
[research_xu_et_al_2020_meta_a2c]: https://arxiv.org/abs/2007.08794
[research_yao_et_al_2021_task_augmentation]: https://proceedings.mlr.press/v139/yao21b.html
[research_yin_et_al_2020_memorization]: https://openreview.net/forum?id=BklEFpEYwS
[research_yu_et_al_2017_sysid]: https://arxiv.org/abs/1710.06537
[research_zahavy_et_al_2020_stac]: https://papers.nips.cc/paper/2020/hash/5cf21ce30208cfffaa832c6e44bb567d-Abstract.html
[research_zheng_et_al_2020_learning_reward]: https://papers.nips.cc/paper/2020/hash/e8fd4a8a5bab2b3785d794ab51fef55c-Abstract.html
[research_zintgraf_et_al_2021_hyperx]: https://proceedings.mlr.press/v139/zintgraf21a.html
[research_andrychowicz_et_al_2016]: https://papers.nips.cc/paper/2016/hash/fb87582825f9d28a8d42c5e5e5e8b23d-Abstract.html
[research_antoniou_edwards_storkey_2019]: https://openreview.net/forum?id=HJGven05Y7
[research_balcan_blum_sharma_2018]: https://arxiv.org/abs/1802.02219
[research_bauer_et_al_2023_ada]: https://arxiv.org/abs/2301.07608
[research_baxter_2000]: https://www.jair.org/index.php/jair/article/view/10248
[research_bengio_bengio_cloutier_1990]: https://scholar.google.com/scholar?q=bengio+bengio+cloutier+1990+synaptic+update
[research_botvinick_et_al_2019_meta]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30061-0
[research_caccia_et_al_2020]: https://papers.nips.cc/paper/2020/hash/c0a271bc0ecb776a094786474322cb82-Abstract.html
[research_chen_et_al_2017_learned_optimizer]: https://arxiv.org/abs/1611.03824
[research_clavera_et_al_2018]: https://proceedings.mlr.press/v87/clavera18a.html
[research_dasgupta_schulz_chater_gershman_2020]: https://www.sciencedirect.com/science/article/pii/S0010027720301980
[research_denevi_et_al_2019]: https://proceedings.mlr.press/v97/denevi19a.html
[research_dorfman_shenfeld_tamar_2021]: https://papers.nips.cc/paper/2021/hash/9c2b23e70f47f1eecf20ac2b9a97b8f8-Abstract.html
[research_duan_et_al_2016_rl2]: https://arxiv.org/abs/1611.02779
[research_fakoor_et_al_2020_mql]: https://openreview.net/forum?id=SJeD3CEFPH
[research_fallah_mokhtari_ozdaglar_2020]: https://proceedings.mlr.press/v108/fallah20a.html
[research_finn_abbeel_levine_2017]: https://proceedings.mlr.press/v70/finn17a.html
[research_finn_rajeswaran_kakade_levine_2019]: https://proceedings.mlr.press/v97/finn19a.html
[research_flennerhag_et_al_2022]: https://openreview.net/forum?id=b-ny3x071E5
[research_grant_finn_levine_darrell_griffiths_2018]: https://openreview.net/forum?id=BJ_UL-k0b
[research_guez_silver_dayan_2013]: https://jmlr.org/papers/v15/guez14a.html
[research_hochreiter_younger_conwell_2001]: https://link.springer.com/chapter/10.1007/3-540-44668-0_13
[research_hospedales_et_al_2022]: https://ieeexplore.ieee.org/document/9428530
[research_humplik_et_al_2019]: https://arxiv.org/abs/1905.06424
[research_jerfel_et_al_2019]: https://papers.nips.cc/paper/2019/hash/e4da3b7fbbce2345d7772b0674a318d5-Abstract.html
[research_khodak_balcan_talwalkar_2019]: https://papers.nips.cc/paper/2019/hash/f4aa0dd960521e045ae2f20621fb4ee9-Abstract.html
[research_kirsch_et_al_2022]: https://arxiv.org/abs/2212.04475
[research_lake_et_al_2017]: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/building-machines-that-learn-and-think-like-people/A9535B1D745A0377E16C590E14B94993
[research_laskin_et_al_2023]: https://openreview.net/forum?id=hy0a5MMPUv
[research_lee_et_al_2023_supervised_pretraining]: https://openreview.net/forum?id=vsSp4Ts_KRi
[research_li_malik_2017]: https://openreview.net/forum?id=ry4Vrt5gl
[research_metz_et_al_2019]: https://openreview.net/forum?id=SylO2yStDr
[research_nagabandi_et_al_2018_meta_online]: https://openreview.net/forum?id=HyztsoC5Y7
[research_nagabandi_finn_levine_2018_learn_to_adapt]: https://openreview.net/forum?id=HyztsoC5Y7v2
[research_nagabandi_finn_levine_2019_mole]: https://openreview.net/forum?id=HyxAfnA5tm
[research_naik_mammone_1992]: https://ieeexplore.ieee.org/document/287172
[research_ni_eysenbach_levine_2022]: https://proceedings.mlr.press/v162/ni22a.html
[research_nichol_achiam_schulman_2018]: https://arxiv.org/abs/1803.02999
[research_oh_et_al_2020]: https://papers.nips.cc/paper/2020/hash/0abdc563a06105aee3c6136871c9f4d1-Abstract.html
[research_ortega_et_al_2019]: https://arxiv.org/abs/1905.03030
[research_parisotto_ba_salakhutdinov_2016]: https://arxiv.org/abs/1511.06342
[research_poupart_et_al_2006]: https://dl.acm.org/doi/10.1145/1143844.1143932
[research_rajeswaran_et_al_2019_imaml]: https://papers.nips.cc/paper/2019/hash/072b030ba126b2f4b2374f342be9ed44-Abstract.html
[research_rakelly_et_al_2019_pearl]: https://proceedings.mlr.press/v97/rakelly19a.html
[research_ravi_larochelle_2017]: https://openreview.net/forum?id=rJY0-Kcll
[research_rothfuss_et_al_2019]: https://openreview.net/forum?id=SkxXCi0qFX
[research_rothfuss_et_al_2021_pacoh]: https://proceedings.mlr.press/v139/rothfuss21a.html
[research_rusu_et_al_2016_progressive]: https://arxiv.org/abs/1606.04671
[research_saemundsson_hofmann_deisenroth_2018]: https://arxiv.org/abs/1803.07551
[research_schmidhuber_1987_metalearning]: https://people.idsia.ch/~juergen/diploma.html
[research_schmidhuber_zhao_wiering_1996]: https://link.springer.com/article/10.1023/A:1018909723456
[research_sener_koltun_2018]: https://papers.nips.cc/paper/2018/hash/432aca3a1e345e339f35a30c8f65edce-Abstract.html
[research_team_et_al_2021_xland]: https://arxiv.org/abs/2107.12808
[research_teh_et_al_2017]: https://papers.nips.cc/paper/2017/hash/0abdc563a06105aee3c6136871c9f4d1-Abstract.html
[research_vilalta_drazdil_2002]: https://link.springer.com/article/10.1023/A:1019956318069
[research_wang_et_al_2016_l2rl]: https://arxiv.org/abs/1611.05763
[research_wang_et_al_2018_prefrontal]: https://www.nature.com/articles/s41593-018-0147-8
[research_wang_et_al_2021_alchemy]: https://arxiv.org/abs/2102.02926
[research_wichrowska_et_al_2017]: https://proceedings.mlr.press/v70/wichrowska17a.html
[research_xu_van_hasselt_silver_2018]: https://papers.nips.cc/paper/2018/hash/2715518c875999308842e3455eda2fe3-Abstract.html
[research_yu_et_al_2020_pcgrad]: https://papers.nips.cc/paper/2020/hash/3fe78a8acf5fda99de95303940a2420c-Abstract.html
[research_yu_et_al_2020_metaworld]: https://proceedings.mlr.press/v100/yu20a.html
[research_zheng_oh_singh_2018_lirpg]: https://papers.nips.cc/paper/2018/hash/51de85ddd068f0bc787691d356176df9-Abstract.html
[research_zintgraf_et_al_2020_varibad]: https://openreview.net/forum?id=Hkl9JlBYvr
