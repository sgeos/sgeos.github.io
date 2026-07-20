---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: Exploration, Intrinsic Motivation, and Curiosity"
date:   2025-12-22 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 5
---

<!-- A254 -->
<script>console.log("A254");</script>

Exploration is the process by which a reinforcement learning agent gathers information about its environment sufficient to identify high-reward behavior. Optimal exploration under uncertainty requires balancing the immediate cost of taking a possibly-suboptimal action against the information gained from that action, and the strategies developed to solve this problem constitute one of the central research programs in the reinforcement learning literature. Article two treated the multi-armed bandit case where exploration analysis is cleanest, article three treated the classical Markov decision process setting where exploration bonuses and PAC-MDP algorithms formalize the extension, article four treated the exploration approaches practical for deep reinforcement learning at scale. This article surveys the intrinsic motivation and curiosity literature that develops structured exploration methods for high-dimensional environments where naive extensions of bandit techniques fail. Topics include count-based exploration and density-based pseudocount methods, prediction-error curiosity and random network distillation, information-theoretic exploration through empowerment and mutual information objectives, Schmidhuber's compression-progress framework, developmental approaches to intrinsic motivation, hard-exploration benchmarks and their algorithmic responses, and neuroscience connections to the curiosity systems in biological brains. Article seven treats model-based reinforcement learning where exploration bonuses can be evaluated more efficiently through simulated rollouts, article twelve treats evolutionary and open-ended approaches to exploration.

## The Exploration-Exploitation Trade-off in Markov Decision Processes

The classical Markov decision process setting inherits the exploration-exploitation trade-off from the bandit setting of article two, but extends its structure in ways that make analysis substantially harder. The value function estimate that a bandit-like algorithm bases exploration decisions on now depends on the transition and reward structure at other states, and the exploration bonus that would guarantee optimality in the bandit setting does not straightforwardly extend to the MDP setting.

Formally, define the sub-optimality gap of a policy $\pi$ at state $s$ as

$$\Delta^\pi(s) = V^*(s) - V^\pi(s)$$

Two related performance measures quantify the effectiveness of an exploration strategy. The cumulative regret over $T$ episodes is

$$R_T = \sum_{k=1}^{T} \left(V^*(s_0) - V^{\pi_k}(s_0)\right)$$

for a sequence of policies $\pi_1, \pi_2, \ldots, \pi_T$ produced by the exploration algorithm. The sample complexity is the number of steps in which the current policy is not $\epsilon$-optimal,

$$\text{SC}(\epsilon, \delta) = \left| \left\{t : V^*(s_t) - V^{\pi_t}(s_t) > \epsilon\right\} \right|$$

which is bounded with probability at least $1 - \delta$ by an algorithm-polynomial in the problem parameters.

An exploration strategy is a rule that governs how the agent selects actions in the presence of uncertainty about $V^*$ and the underlying transition kernel $P$ and reward function $R$. The naive $\epsilon$-greedy strategy of article three suffices for asymptotic convergence to the optimal policy in tabular finite MDPs, but its sample complexity scales poorly with state and action space size and requires long training even in modestly-sized problems.

The three classical categories of exploration strategy are undirected exploration through random action selection (including $\epsilon$-greedy and Boltzmann), optimistic exploration that inflates uncertain value estimates, and posterior sampling that maintains a Bayesian belief over environments and follows the optimal policy for a sampled environment. Article three treated the classical instances, this article treats their extensions to high-dimensional and structured environments where the classical methods fail or scale poorly.

Two structural challenges distinguish MDP exploration from bandit exploration. First, temporal-credit assignment means that exploration bonuses at one state affect the value estimates of predecessor states through the Bellman recursion, so exploration signals propagate through the value function rather than acting only locally. Second, long-horizon exploration may require sequences of actions to reach informative states, and undirected random action selection can produce vanishingly small probability of executing such sequences at any modest state-space size.

## Historical Development

Exploration in reinforcement learning traces to the classical multi-armed bandit theory of article two. [Kaelbling 1993][book_kaelbling_1993] doctoral thesis and the interval estimation heuristic provided early treatments of exploration in the deterministic and stochastic settings for tabular problems. The R-MAX algorithm of [Brafman and Tennenholtz 2002][research_brafman_tennenholtz_2002] and E3 algorithm of [Kearns and Singh 2002][research_kearns_singh_2002] established the PAC-MDP framework for provably-efficient exploration in tabular MDPs treated in article three.

The intrinsic motivation research program has roots in behavioral psychology and developmental science that predate reinforcement learning. [Berlyne 1960][book_berlyne_1960] treatment of curiosity and exploratory behavior established the conceptual framework that later informed computational models. [White 1959][research_white_1959] concept of effectance motivation similarly proposed intrinsic drives beyond hunger, thirst, and other homeostatic motives.

[Schmidhuber 1991][research_schmidhuber_1991] introduced the compression-progress framework in which learning progress on a predictive model serves as an intrinsic reward. The formal theory of curiosity of [Schmidhuber 2010][research_schmidhuber_2010] developed the framework at length and connected it to related work in universal problem solving. In parallel, [Oudeyer and Kaplan 2007][research_oudeyer_kaplan_hafner_2007] intrinsic motivation systems paper developed the developmental robotics perspective on intrinsic motivation, connecting to developmental psychology and to the broader theory of open-ended learning treated in article twelve.

The connection between intrinsic motivation and reinforcement learning was developed by [Barto Singh and Chentanez 2004][research_barto_singh_chentanez_2004], [Chentanez Barto Singh 2005][research_chentanez_barto_singh_2005], and [Singh Barto Chentanez 2005][research_singh_barto_chentanez_2005], which established the intrinsically motivated reinforcement learning framework in which the environment's extrinsic reward is augmented by an intrinsic reward derived from the agent's own predictive model or novelty estimator. [Kaplan and Oudeyer 2004][research_kaplan_oudeyer_2004] developed the maximizing-learning-progress framework that connects intrinsic motivation to developmental psychology. [Storck Hochreiter and Schmidhuber 1995][research_storck_hochreiter_schmidhuber_1995] earlier proposed information-gain-based reinforcement learning that anticipated later work.

The deep reinforcement learning era brought new attention to the exploration problem through the discovery that DQN-style Q-learning failed on Atari games requiring long-horizon exploration, most notoriously Montezuma's Revenge. [Bellemare et al 2016][research_bellemare_et_al_2016_exploration] unified count-based exploration through density models, [Pathak et al 2017][research_pathak_et_al_2017] developed intrinsic curiosity modules using self-supervised prediction error, and [Burda Edwards Storkey Klimov 2018][research_burda_edwards_storkey_klimov_2018] random network distillation provided a simpler alternative. Successive years produced a rich algorithmic literature responding to the discovery that exploration is the binding constraint on many hard reinforcement learning problems.

## Optimism-Based Exploration

Optimism in the face of uncertainty extends from bandits to MDPs by inflating value estimates at uncertain state-action pairs. In tabular finite MDPs the mechanism admits clean analysis. Define an exploration bonus $b(s, a)$ derived from uncertainty and add it to the reward,

$$\tilde{r}(s, a) = r(s, a) + b(s, a)$$

with the bonus decreasing as the state-action pair is visited more. Standard choices include count-based bonuses

$$b(s, a) = \beta / \sqrt{N(s, a)}$$

for visit count $N(s, a)$ and exploration coefficient $\beta$, motivated by the UCB analysis in bandits.

The R-MAX algorithm treats unvisited state-action pairs as maximally rewarding, using

$$\tilde{r}_{\text{R-MAX}}(s, a) = \begin{cases} \hat{r}(s, a) & \text{if } N(s, a) \geq m \\ R_{\max} & \text{otherwise} \end{cases}$$

for a visit threshold $m$ and the maximum possible reward $R_{\max}$, providing exploration through the maximum-reward assumption rather than an additive bonus. Interval-based exploration methods including MBIE-EB of [Strehl and Littman 2008][research_strehl_littman_2008] use bonus terms of the form

$$b_{\text{MBIE-EB}}(s, a) = \frac{\beta}{\sqrt{N(s, a)}}$$

derived from Chernoff-Hoeffding confidence intervals on the estimated Q-value. UCRL2 of [Jaksch Ortner and Auer 2010][research_jaksch_ortner_auer_2010] applies optimism at the level of the entire MDP, maintaining confidence sets over $(P, R)$ constructed as

$$\mathcal{M}_t = \left\{(P', R') : \| P'(\cdot \mid s, a) - \hat{P}_t(\cdot \mid s, a) \|_1 \leq c_1 \sqrt{\log(t)/N_t(s, a)}, \; |R'(s, a) - \hat{R}_t(s, a)| \leq c_2 \sqrt{\log(t)/N_t(s, a)}\right\}$$

and following the policy optimal for the most-optimistic MDP in the confidence set. Both approaches achieve regret bounds of order $\tilde{\mathcal{O}}(D \sqrt{|\mathcal{S}| |\mathcal{A}| T})$ for MDP diameter $D$.

Optimism-based methods extend to function approximation but require additional care. The key challenge is characterizing uncertainty over $V^*$ or $Q^*$ when the value function is parameterized by a neural network rather than tabulated. Bootstrapped DQN of [Osband Blundell Pritzel and Van Roy 2016][research_osband_blundell_pritzel_van_roy_2016_exploration] maintains an ensemble of $K$ Q-networks trained on bootstrap samples of the replay buffer and uses their disagreement as an implicit optimism signal. At each episode, the agent randomly selects one head of the ensemble and follows it greedily, producing an approximate posterior-sampling behavior.

The disagreement measure

$$U(s, a) = \sqrt{\frac{1}{K} \sum_{k=1}^K (Q_k(s, a) - \bar{Q}(s, a))^2}$$

with $\bar{Q}(s, a) = (1/K) \sum_k Q_k(s, a)$ provides a state-action uncertainty estimate that can drive an additive bonus in an alternative use of the ensemble. Ensemble methods provide a practical mechanism to extend optimism-based exploration to deep function approximation without requiring exact posterior computation.

## Exploration Through Policy Optimization

Policy-gradient methods admit distinctive exploration mechanisms grounded in the stochasticity of the policy itself. Entropy regularization adds a policy entropy bonus to the reinforcement learning objective,

$$J_{\text{ent}}(\theta) = J(\theta) + \beta \, \mathbb{E}_{s \sim d^{\pi_\theta}}\!\left[H(\pi_\theta(\cdot \mid s))\right]$$

with weighting coefficient $\beta$, encouraging the policy to maintain stochasticity that supports exploration. Maximum-entropy reinforcement learning of [Ziebart 2010][book_ziebart_2010_thesis] extends the objective to a full information-theoretic formulation in which the policy trades off reward against entropy at every state, and Soft Actor-Critic treated in article four provides the deep-learning implementation. The maximum-entropy objective has close ties to the Boltzmann exploration formulation and to the principle of maximum entropy inference.

Parameter space noise provides an alternative to action-space stochasticity. [Plappert et al 2018][research_plappert_et_al_2018] adds noise directly to policy parameters,

$$\tilde{\theta} = \theta + \sigma \cdot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

for a per-training-step noise sample $\epsilon$ and an adaptive scale $\sigma$. The mechanism produces state-dependent exploration that adapts as the policy learns, and empirically outperforms Gaussian action-space noise on many continuous-control problems. NoisyNets of Fortunato et al 2018 treated in article four provides a related deep-learning variant.

Trust-region and proximal policy optimization treated in article four exhibit their own implicit exploration through the enforced constraint on policy update magnitude. The trust-region bound prevents the policy from collapsing to a narrow behavior distribution early in training, providing a mild exploration bias without explicit exploration bonuses. The empirical robustness of PPO across a wide range of tasks partly stems from this implicit exploration.

The Best-Response Learning framework of [Kakade and Langford 2002][research_kakade_langford_2002_exploration] provides a theoretical basis for conservative policy iteration that connects to exploration guarantees through mixture policies that combine current best-response actions with exploratory actions.

## Posterior Sampling and Epistemic Uncertainty

Posterior sampling for reinforcement learning (PSRL) of [Osband and Van Roy 2013][research_osband_van_roy_2013_psrl] extends Thompson sampling from bandits to MDPs. The agent maintains a posterior distribution over environment parameters $\theta$,

$$p(\theta \mid \mathcal{D}_t) \propto p(\mathcal{D}_t \mid \theta) \, p(\theta)$$

sampled from prior $p(\theta)$ conditioned on trajectory data $\mathcal{D}_t$. At the start of each episode the agent draws $\tilde{\theta} \sim p(\theta \mid \mathcal{D}_t)$, computes the optimal policy $\pi_{\tilde{\theta}}^*$ for the sampled environment, and follows it for the episode. The mechanism trades exploration for exploitation through the posterior variance rather than through explicit optimism.

The Bayesian regret of PSRL for finite-horizon episodic MDPs is

$$R_T^{\text{Bayes}} = \tilde{\mathcal{O}}\!\left(H \sqrt{|\mathcal{S}| |\mathcal{A}| T}\right)$$

for horizon $H$ and total step count $T$, comparable to optimism-based approaches. The posterior-sampling analysis provides an alternative theoretical framework that has proved productive for extending exploration guarantees to structured MDPs.

The distinction between epistemic uncertainty (uncertainty about model parameters that would decrease with more data) and aleatoric uncertainty (irreducible stochasticity in the environment) is fundamental to exploration. Optimism-based and posterior-sampling methods target epistemic uncertainty, since only epistemic uncertainty is reducible through exploration. Aleatoric uncertainty introduces noise that can appear to reward exploration methods but does not correspond to genuine learning progress, and separating the two is a persistent methodological challenge.

Deep ensembles of value functions provide a practical mechanism for estimating epistemic uncertainty in deep reinforcement learning. Randomized prior functions of [Osband Aslanides and Cassirer 2018][research_osband_aslanides_cassirer_2018] add fixed randomly-initialized prior networks to trainable ensemble members, providing a principled Bayesian interpretation and preventing the ensemble from collapsing to zero uncertainty on unfamiliar inputs. Successor Uncertainties of [Janz Hron Mazur Kingma Hernandez-Lobato 2019][research_janz_et_al_2019] provide a principled ensemble-based approach that computes epistemic uncertainty in the value function through the successor representation.

## Reward-Free Exploration and Task-Agnostic Learning

Reward-free exploration is the theoretical framework in which an agent explores the environment without a reward function, then uses the collected experience to solve any downstream reward function that becomes available. The framing separates the exploration problem from the reward-optimization problem, providing analytical clarity and enabling reuse of exploration effort across tasks.

The reward-free framework was formalized by [Jin Krishnamurthy Simchowitz Yu 2020][research_jin_krishnamurthy_simchowitz_yu_2020] for tabular MDPs with a two-stage protocol. An exploration stage lets the agent interact with the environment for a budget of $K$ episodes without observing rewards, followed by a planning stage where the agent is given a reward function and must produce a near-optimal policy. The exploration algorithm receives no reward signal, so it must construct a policy that visits states in a way that supports planning against arbitrary reward functions.

The main result establishes that reward-free exploration requires $\tilde{\mathcal{O}}(H^5 |\mathcal{S}|^2 |\mathcal{A}| / \epsilon^2)$ episodes to achieve $\epsilon$-near-optimality for any reward function with probability at least $1 - \delta$, comparable to reward-informed exploration up to logarithmic factors. The bound demonstrates that the reward signal provides little advantage in the tabular setting.

Extensions to linear MDPs of [Wang Salakhutdinov and Yang 2020][research_wang_salakhutdinov_yang_2020] and to low-rank MDPs of [Modi Chen Krishnamurthy Jiang Agarwal 2021][research_modi_chen_krishnamurthy_2021] extend the framework to function-approximation settings. The reward-free framework has proved productive as a theoretical setting for exploration analysis and connects to the intrinsic-motivation methods surveyed above through the shared emphasis on task-agnostic state coverage.

Practical instantiations of reward-free exploration include the RF-Express and RF-UCRL algorithms, which combine optimistic model estimation with policy computation against imagined "worst-case" reward functions. The empirical performance of reward-free exploration matches or exceeds reward-informed exploration on hard-exploration benchmarks including Montezuma's Revenge in some experiments.

## Count-Based Exploration

The count-based exploration bonus of the form $\beta / \sqrt{N(s, a)}$ works well in tabular MDPs but faces an immediate problem in high-dimensional or continuous state spaces where visit counts are always zero for previously-unseen states. The pseudocount framework of [Bellemare et al 2016][research_bellemare_et_al_2016_exploration] extended count-based methods to arbitrary state spaces by deriving effective visit counts from a density model.

Let $\rho(s)$ be a density estimator over states that assigns a probability $\rho_n(s)$ after $n$ observations and $\rho'_n(s)$ after observing state $s$ once more. The pseudocount

$$\hat{N}(s) = \frac{\rho_n(s)(1 - \rho'_n(s))}{\rho'_n(s) - \rho_n(s)}$$

approximates the number of times $s$ has been observed under the assumption that $\rho$ is a well-calibrated density estimator. The pseudocount provides the input to a count-based bonus,

$$b(s, a) = \beta / \sqrt{\hat{N}(s) + 1}$$

or a variant, and reduces the exploration problem to the density-estimation problem. The choice of density model determines the effective inductive bias for what counts as a novel state.

CTS density models based on context-tree switching provided the original density model in the Bellemare et al pseudocount paper. Subsequent work explored PixelCNN, pixel-based autoregressive models, and other density estimators for the pseudocount role. The pseudocount approach achieved substantial improvements on hard-exploration Atari games including Montezuma's Revenge, where naive $\epsilon$-greedy DQN reaches essentially zero score.

The connection between pseudocounts and information gain provides an alternative theoretical framing. If the density model $\rho$ can be interpreted as a Bayesian predictive distribution, the log-likelihood improvement from observing $s$ provides an information-gain quantity that can serve as an intrinsic reward,

$$r^{\text{IG}}(s) = \log \rho'_n(s) - \log \rho_n(s)$$

The pseudocount can be derived from the information-gain formulation under assumptions on the density model, unifying the count-based and information-theoretic perspectives on exploration.

## Density-Based Pseudocounts

The pseudocount framework generalized to hash-based counts, latent-space counts, and various other density-estimation strategies. [Tang et al 2017][research_tang_et_al_2017] hash-based counts use SimHash or learned hash functions to project high-dimensional states to a small discrete bucket space, then count buckets. The approach provides substantial computational simplification while retaining much of the exploration benefit.

Latent-space pseudocounts of [Machado Bellemare and Bowling 2020][research_machado_bellemare_bowling_2020] count in a learned latent space $\phi(s)$ that captures task-relevant features while discarding task-irrelevant variation. The pseudocount

$$\hat{N}_\phi(s) = \hat{N}(\phi(s))$$

is computed over the latent encoding rather than the raw observation. The approach addresses the noisy-TV problem discussed below by ensuring that the density estimator is invariant to irreducible-noise features of the observation. Hash-based pseudocounts of [Tang et al 2017][research_tang_et_al_2017] use a SimHash or learned hash function $h : \mathcal{S} \to \{0, 1\}^k$ to project observations to a discrete bucket space and count buckets, obtaining an intrinsic reward

$$r^{\text{hash}}(s) = \frac{\beta}{\sqrt{N(h(s)) + 1}}$$

at a computational cost far below the density-model approach.

Deep density models including PixelCNN of [van den Oord Kalchbrenner Kavukcuoglu 2016][research_van_den_oord_et_al_2016] and flow-based models such as RealNVP and Glow provide expressive density estimators that scale to high-dimensional pixel observations. Their use as pseudocount density models produces stronger exploration bonuses at higher computational cost.

The choice of density model shapes the exploration inductive bias substantially. Sensitive density models produce exploration bonuses that reward every novel pixel arrangement, potentially including irrelevant background noise. Insensitive density models miss genuinely novel states embedded in familiar visual contexts. The trade-off is analogous to the one between overfitting and underfitting in supervised learning, and no single choice dominates across problems.

## Prediction-Error Curiosity

The prediction-error curiosity family uses the error of a learned forward or inverse model as an intrinsic reward, motivated by the intuition that surprising outcomes signal opportunities to learn. Earlier work in this direction includes [Stadie Levine and Abbeel 2015][research_stadie_levine_abbeel_2015] surprise-based intrinsic reward for Atari and [Houthooft Chen Duan Schulman De Turck Abbeel 2016][research_houthooft_et_al_2016] Variational Information Maximizing Exploration (VIME) that uses variational information gain on Bayesian neural network models as the intrinsic reward. The Intrinsic Curiosity Module (ICM) of [Pathak Agrawal Efros Darrell 2017][research_pathak_et_al_2017] provides the canonical modern implementation and set the template for subsequent prediction-error methods.

ICM learns an inverse dynamics model $\hat{a}_t = f_{\text{inv}}(\phi(s_t), \phi(s_{t+1}))$ that predicts the action from consecutive state encodings, trained by the inverse-dynamics loss

$$L_{\text{inv}}(\phi, f_{\text{inv}}) = \mathbb{E}\!\left[\ell(f_{\text{inv}}(\phi(s_t), \phi(s_{t+1})), a_t)\right]$$

for classification loss $\ell$, and a forward dynamics model $\hat{\phi}(s_{t+1}) = f_{\text{fwd}}(\phi(s_t), a_t)$ that predicts the next state encoding, trained by the forward loss

$$L_{\text{fwd}}(\phi, f_{\text{fwd}}) = \frac{1}{2} \mathbb{E}\!\left[\| \hat{\phi}(s_{t+1}) - \phi(s_{t+1}) \|^2\right]$$

The combined ICM training objective

$$L_{\text{ICM}} = (1 - \beta) L_{\text{inv}} + \beta L_{\text{fwd}}$$

with $\beta \in [0, 1]$ balances the two losses. The state encoder $\phi$ is trained through the inverse-model objective to capture features relevant to action, filtering out features that the agent cannot influence.

The intrinsic reward is the forward-model prediction error in the learned feature space,

$$r^{\text{ICM}}_t = \frac{\eta}{2} \| \hat{\phi}(s_{t+1}) - \phi(s_{t+1}) \|^2$$

with $\eta$ a scaling coefficient, and the total policy-training reward combines extrinsic and intrinsic terms,

$$r_t^{\text{total}} = r_t^{\text{ext}} + r_t^{\text{ICM}}$$

The mechanism rewards trajectories that lead to forward-model surprise, focusing exploration on parts of the state space where the agent's dynamics model is inaccurate.

The inverse-model feature encoder provides an important refinement. Without the inverse-model objective, the encoder would represent all visual features including irrelevant background noise, and forward-model prediction error would reward exploration of unimportant novelty. By restricting the encoding to action-relevant features, ICM focuses curiosity on parts of the state that the agent can influence through its actions, addressing the noisy-TV problem discussed below.

ICM achieved substantial improvements on VizDoom and Super Mario Bros benchmarks where extrinsic reward is sparse. Subsequent variants including ICM-based Never Give Up of [Badia et al 2020][research_badia_et_al_2020_ngu] added an episodic novelty component to encourage revisiting rewarded regions rather than only novel states.

## Random Network Distillation

Random Network Distillation (RND) of [Burda Edwards Storkey Klimov 2018][research_burda_edwards_storkey_klimov_2018] provides a simpler prediction-error method that trains a predictor network to match the output of a randomly-initialized fixed target network. The intrinsic reward is the prediction error,

$$r^{\text{RND}}_t = \| \hat{f}_\theta(s_t) - f_{\bar{\theta}}(s_t) \|^2$$

where $f_{\bar{\theta}}$ is the fixed random target network and $\hat{f}_\theta$ is the predictor trained by the regression loss

$$L_{\text{RND}}(\theta) = \mathbb{E}_{s \sim \mathcal{D}}\!\left[\| \hat{f}_\theta(s) - f_{\bar{\theta}}(s) \|^2\right]$$

on visited states. RND applies observation and reward normalization

$$\tilde{s}_t = \frac{s_t - \mu_s}{\sigma_s}, \quad \tilde{r}^{\text{RND}}_t = \frac{r^{\text{RND}}_t}{\sigma_r}$$

with running estimates of mean and standard deviation to stabilize training across environments with different observation and reward scales.

The mechanism works because the predictor achieves low error on states it has seen during training and higher error on novel states. Unlike ICM, RND does not require learning inverse or forward dynamics models, the random target provides an implicit density-like signal without any generative modeling. The simplicity has made RND widely adopted for exploration in deep RL applications.

RND on Montezuma's Revenge achieved substantially higher scores than count-based and ICM methods, providing the first Atari agent to reliably solve the game. Combined with distributional RL and other Rainbow components, RND-based agents including Agent57 of [Badia et al 2020][research_badia_et_al_2020_agent57] achieved superhuman performance across all 57 Atari games in the ALE benchmark, closing a long-standing challenge.

The RND intrinsic reward decays as the state space is covered, providing a naturally diminishing exploration bonus. However, RND retains a bias toward novel visual features regardless of task relevance, and the resulting exploration can waste sample budget on task-irrelevant novelty. Combination with task-relevant signals is an active area of research.

## Empowerment and Information-Theoretic Exploration

Empowerment of [Klyubin Polani and Nehaniv 2005][research_klyubin_polani_nehaniv_2005] and its systematic treatment in [Salge Glackin and Polani 2014][research_salge_glackin_polani_2014] provides an information-theoretic objective for exploration that captures the agent's control over its future. The empowerment at state $s$ is the maximum mutual information between an action sequence and the resulting state after $k$ steps,

$$\mathfrak{E}(s) = \max_{p(a_{t:t+k-1})} I(A_{t:t+k-1} ; S_{t+k} \mid S_t = s)$$

where the maximization is over action-sequence distributions. States with high empowerment provide the agent with substantial control over its future outcomes, and empowerment-driven exploration seeks such states.

The computational challenge of empowerment is the mutual-information maximization over action sequences. The definition expands as

$$I(A_{t:t+k-1} ; S_{t+k} \mid S_t) = H(A_{t:t+k-1}) - H(A_{t:t+k-1} \mid S_{t+k}, S_t)$$

where $H$ denotes Shannon entropy. Variational bounds provide tractable approximations. The Barber-Agakov lower bound underlies [Mohamed and Rezende 2015][research_mohamed_rezende_2015] variational empowerment estimator,

$$I(A ; S') \geq \mathbb{E}_{p(a, s')}\!\left[\log q(a \mid s') - \log p(a)\right]$$

where $q(a \mid s')$ is a learned decoder that predicts the action from the resulting state. Maximizing the lower bound over $q$ and the action distribution $p(a)$ provides a tractable empowerment estimator that scales to deep RL settings.

Other information-theoretic exploration objectives include mutual information between latent skills and observations for skill discovery, treated in the multi-goal section below, and information gain about model parameters for model-based exploration. The common thread is the use of information theory to formalize "interesting" states or trajectories in a way that captures the exploration desiderata without appealing to extrinsic reward.

Free-energy based exploration from active inference of [Friston 2010][research_friston_2010_active_inference] provides an alternative information-theoretic framework in which exploration and exploitation both minimize a variational free energy. The framework treats action selection as expected-free-energy minimization,

$$G(\pi) = \mathbb{E}_{q(s, o; \pi)}\!\left[\log q(s \mid o; \pi) - \log p(s, o \mid m)\right]$$

with the expected free energy decomposing into an epistemic (information-gain) term and a pragmatic (reward-seeking) term. Article seven treats predictive coding and active inference at greater length.

## Compression Progress and Schmidhuber's Framework

Schmidhuber's formal theory of creativity, fun, and intrinsic motivation of [Schmidhuber 2010][research_schmidhuber_2010] provides a unified information-theoretic framework in which curiosity, creativity, and aesthetic pleasure all arise from compression progress on the agent's world model. The framework interprets the intrinsic reward as the improvement in world-model compression rate on the observations,

$$r^{\text{CP}}_t = L(o_t \mid M_{t-1}) - L(o_t \mid M_t)$$

where $L(o \mid M)$ is the compression length of observation $o$ under world model $M$, $M_{t-1}$ is the model before observing $o_t$, and $M_t$ is the model after. The compression-progress reward captures the intuition that learning progress itself is intrinsically rewarding.

The framework provides a common analytical vocabulary for intrinsic-motivation methods. Prediction-error curiosity approximates compression progress when the world model is trained to minimize prediction loss. Density-based pseudocounts approximate compression progress when the density model can be interpreted as an implicit compressor. Empowerment relates to compression progress through the mutual-information formulation.

The compression-progress framework connects to broader theories of algorithmic information theory, minimum description length, and probabilistic prediction. It provides a theoretical anchor for intrinsic motivation that predates the deep reinforcement learning era and has continued to inform algorithmic development throughout the deep learning wave.

## Developmental Approaches to Intrinsic Motivation

The developmental robotics community has developed a distinct research program on intrinsic motivation grounded in developmental psychology and open-ended learning. [Oudeyer Kaplan Hafner 2007][research_oudeyer_kaplan_hafner_2007] provides the systematic treatment of intrinsic motivation systems for autonomous mental development, with applications to robotic learning.

The developmental approach emphasizes learning progress as the intrinsic reward signal, similar in spirit to Schmidhuber's compression progress but with emphasis on progress in the ability to reach diverse goals rather than compression of observations. The IAC (Intelligent Adaptive Curiosity) family of algorithms of [Oudeyer Kaplan Hafner 2007][research_oudeyer_kaplan_hafner_2007] partitions the sensorimotor space into regions and estimates learning progress within each region as the derivative of prediction accuracy over time,

$$r^{\text{IAC}}_t = \frac{d}{dt} \text{Accuracy}(f_{\text{region}(s_t)})$$

Exploration focuses on regions where learning progress is highest, capturing the intuition that curiosity is drawn to problems that are neither too easy nor too hard, sometimes called the goldilocks zone.

The developmental approach also emphasizes hierarchical goal generation as an intrinsic-motivation mechanism. Goal-conditioned reinforcement learning treated below extends this intuition into practical algorithms. The connection to embodied cognition treated in article thirteen and to open-ended evolution treated in article twelve makes the developmental approach a bridge between multiple parts of the series.

## Hard Exploration Benchmarks

The Atari benchmarks used throughout deep reinforcement learning research include a small set of games where standard $\epsilon$-greedy DQN fails to achieve nontrivial scores. Montezuma's Revenge is the canonical example. The game requires the agent to navigate through a series of rooms with locked doors, keys, and hazards, receiving reward only upon collecting keys and opening doors. Random exploration produces essentially zero reward, and value-based methods without dedicated exploration make no progress.

Related hard-exploration games include Pitfall, Private Eye, and Solaris. These games share the characteristic that useful behaviors require long sequences of actions to reach any positive reward, making them sensitive to the exploration algorithm rather than to the value-learning algorithm.

Beyond Atari, hard exploration challenges appear in procedurally-generated environments (Procgen, MiniHack, NetHack), sparse-reward robotics tasks (block stacking, insertion tasks), and open-world environments (MineRL, Craftax). Each domain stresses different aspects of the exploration problem. Atari stresses long-horizon exploration with rich visual observations, robotics stresses continuous action spaces and sparse reward, and open-world settings stress open-ended exploration without clear goal specification.

The exploration algorithms treated in this article generally target subsets of these benchmark categories. Pseudocount and RND methods address the visual Atari-style benchmarks. Empowerment and goal-conditioned methods address open-ended and robotic settings. The lack of a unified exploration algorithm that dominates across all these benchmark categories remains one of the field's open challenges.

## Go-Explore and Diverse Solutions

Go-Explore of [Ecoffet Huizinga Lehman Stanley Clune 2019][research_ecoffet_et_al_2019] and its follow-ups took a distinctive approach to hard exploration by explicitly separating the exploration and exploitation phases. The algorithm proceeds in two stages. In the exploration stage, the agent maintains an archive of visited states and repeatedly resets to interesting archive states before continuing exploration through random or heuristic action. In the exploitation stage, the trajectories that reached high-reward states are treated as demonstrations and used to train a policy that reliably reproduces the trajectories.

The mechanism explicitly leverages environment resets (either to a saved state via emulator or to a reachable state via replay) to circumvent the exploration difficulty of forgetting valuable states discovered earlier. On Montezuma's Revenge, Go-Explore achieved scores over 400000, well above what any prior algorithm had achieved, and demonstrated the mechanistic power of state resets.

The reliance on environment resets limits Go-Explore's applicability to environments with such support, either through simulator save-and-restore or through deterministic environment dynamics that permit trajectory replay. Extensions to stochastic environments through the [Ecoffet et al 2021][research_ecoffet_et_al_2021] policy-based Go-Explore variant provide partial solutions but do not fully close the gap.

Diverse solutions arise from a similar concern. In many problems, multiple high-reward behaviors exist, and finding them requires an exploration strategy that resists premature convergence to a single behavior. Quality-diversity algorithms treated in article twelve address diversity as an explicit optimization objective rather than as a side effect of exploration.

## Multi-Goal and Skill-Based Exploration

Goal-conditioned reinforcement learning extends the MDP by conditioning the policy on a goal state or goal specification. The intrinsic-motivation literature adapts this framework to exploration by treating goals as internal targets that the agent generates for itself.

The universal value function of [Schaul Horgan Gregor Silver 2015][research_schaul_horgan_gregor_silver_2015] extends the standard value function with a goal argument,

$$V(s, g) = \mathbb{E}\!\left[\sum_{t=0}^{\infty} \gamma^t r(s_t, g) \mid s_0 = s\right]$$

where the reward is defined relative to a goal $g \in \mathcal{G}$. Automatic goal generation from unsupervised experience produces goals through methods including hindsight experience replay [Andrychowicz et al 2017][research_andrychowicz_et_al_2017_exploration], where failed trajectories $\tau = (s_0, a_0, \ldots, s_T)$ are relabeled with the goals they actually achieved,

$$g'(\tau) = \phi(s_T), \quad r'(s_t, g'(\tau)) = -\| \phi(s_t) - g'(\tau) \|$$

with $\phi$ a state-to-goal mapping. VAE-based goal proposal generates novel goals through a variational autoencoder trained on the state distribution, skew-fit biases goal generation toward rare regions of the state space through density-model reweighting.

Skill discovery through mutual information provides another intrinsic-motivation approach. The Variational Intrinsic Control (VIC) algorithm of [Gregor Rezende and Wierstra 2016][research_gregor_rezende_wierstra_2016] established the mutual-information-based skill discovery framework. The DIAYN (Diversity Is All You Need) algorithm of [Eysenbach Gupta Ibarz Levine 2019][research_eysenbach_gupta_ibarz_levine_2019] learns a set of skills $z$ by maximizing the mutual information between skill and resulting state,

$$I(S ; Z) = H(Z) - H(Z \mid S)$$

The maximization uses a variational discriminator $q(z \mid s)$ to lower-bound the mutual information and rewards the skill policy for producing states from which the skill can be identified,

$$r^{\text{DIAYN}}(s, z) = \log q(z \mid s) - \log p(z)$$

The mechanism produces a diverse collection of behaviors without extrinsic reward, providing a form of unsupervised exploration that generates a repertoire of skills usable for downstream tasks. Extensions include Dynamics-Aware Discovery of Skills (DADS) of [Sharma Gu Levine Kumar Hausman 2020][research_sharma_et_al_2020] which conditions the mutual-information objective on the learned dynamics model, and Variational Option Discovery (VOD) of [Achiam Edwards Amodei 2018][research_achiam_edwards_amodei_2018] which formulates skill discovery within the options framework.

VAE-based goal proposal of [Nair Pong Dalal Bahl Lin Levine 2018][research_nair_pong_dalal_2018] generates novel goals through a variational autoencoder trained on the state distribution, and Skew-Fit of [Pong Dalal Lin Nair Bahl Levine 2020][research_pong_dalal_lin_2020] biases goal generation toward rare regions through density-model reweighting of the training distribution. CURIOUS of [Colas Fournier Sigaud Chetouani Oudeyer 2019][research_colas_fournier_sigaud_2019] combines learning-progress-based intrinsic reward with multi-goal reinforcement learning for autonomous curriculum construction.

Extensions to continuous skills, hierarchical skill structures, and skill composition constitute an active research area. Article six treats hierarchical reinforcement learning and article twelve treats open-ended learning, both of which connect to skill-based exploration.

## Meta-Exploration and Learned Exploration Policies

Meta-exploration frames exploration itself as a learnable skill acquired across a distribution of tasks. Rather than designing exploration bonuses or intrinsic rewards by hand, the meta-exploration approach trains a policy that produces good exploratory behavior on new tasks drawn from a distribution. Article nine treats meta-reinforcement learning as its principal topic, this section previews the role of exploration in that framework.

RL$^2$ of [Duan Schulman Chen Bartlett Sutskever Abbeel 2016][research_duan_schulman_chen_2016_rl2] and the concurrent learning-to-reinforcement-learn work of [Wang Kurth-Nelson Tirumala Soyer Leibo Munos Blundell Kumaran Botvinick 2016][research_wang_et_al_2016_l2rl] formulated meta-reinforcement learning as training a recurrent policy on a distribution of MDPs so that the recurrent state serves as a task-conditional summary of the current task. The recurrent policy learns to explore efficiently at the start of each new task and to exploit once the task is identified,

$$\pi_\theta(a_t \mid o_t, h_t), \quad h_t = f_\theta(o_t, a_{t-1}, r_{t-1}, h_{t-1})$$

with the recurrent state $h_t$ implicitly tracking task uncertainty.

MAESN of [Gupta Mendonca Liu Abbeel Levine 2018][research_gupta_mendonca_liu_2018] introduces a per-task latent variable trained through variational inference alongside the meta-learned policy, providing an explicit uncertainty representation that supports structured exploration in the multi-task setting.

VariBAD of [Zintgraf Shiarlis Igl Schulze Gal Hofmann Whiteson 2020][research_zintgraf_et_al_2020] combines variational Bayesian task inference with policy optimization, producing exploration policies with theoretical connections to Bayes-optimal exploration under uncertainty about the task identity. The framework recovers PSRL-like behavior when the task distribution is broad and behaves closer to a fixed exploration policy when the task distribution is narrow.

Meta-exploration algorithms scale poorly when the task distribution is narrow (little benefit from meta-learning) and when task identification requires extensive exploration (the meta-learned policy struggles to identify tasks quickly). Successful applications typically involve moderately-diverse task distributions where task inference is feasible from a few dozen environment steps.

## Automatic Curriculum Generation

Automatic curriculum generation constructs a sequence of increasingly difficult tasks or goals that support progressive learning, addressing the fact that direct optimization on hard problems often fails while gradual progression through easier variants succeeds. The intersection of curriculum learning with intrinsic motivation and multi-goal reinforcement learning has proved particularly productive.

Goal generation via adversarial training in Goal-GAN of [Florensa Held Wulfmeier Zhang Abbeel 2018][research_florensa_et_al_2018] trains a generator network to propose goals of appropriate difficulty for the current policy. The generator produces goals with intermediate difficulty (achievable but nontrivial) while the discriminator distinguishes these from too-easy or too-hard goals, providing a self-adjusting curriculum.

Teacher-Student Curriculum Learning of [Matiisen Oliver Cohen Schulman 2019][research_matiisen_et_al_2019] treats curriculum construction as a bandit problem where the teacher selects task difficulty and receives reward proportional to student learning progress. The framework connects curriculum learning to the multi-armed bandit theory of article two.

POET of [Wang Lehman Clune Stanley 2019][research_wang_lehman_clune_stanley_2019] and its successor Enhanced POET of [Wang Lehman Rawal Zhi Zhang Clune Stanley 2020][research_wang_lehman_rawal_2020] coevolve environments and agents in an open-ended framework where environments proliferate and diversify alongside agent capabilities. The approach treats the environment distribution as itself an object of optimization, producing an emergent curriculum without hand-specified difficulty gradations.

ALP-GMM of [Portelas Colas Hofmann Oudeyer 2020][research_portelas_colas_hofmann_oudeyer_2020] uses a Gaussian mixture model over the task parameter space and biases sampling toward tasks with high Absolute Learning Progress (ALP), tracking both improvement and regression in performance. The framework connects to the developmental IAC family treated earlier while scaling to continuous task parameterizations.

Curriculum learning provides both a practical mechanism for tackling hard problems and an analytical lens through which to understand the relationship between exploration difficulty and task structure. Article twelve treats open-ended learning at greater length.

## Multi-Agent Exploration

Multi-agent settings introduce distinctive exploration challenges. The joint action space grows exponentially in the number of agents, making brute-force exploration infeasible. The non-stationarity introduced by other agents' learning breaks the assumption that exploration bonuses can be tied to fixed state-action pairs. And coordination among agents is required for exploration strategies that go beyond independent random action.

Independent exploration by each agent treats the multi-agent setting as a collection of parallel single-agent problems, applying single-agent exploration methods without coordination. The approach scales trivially but produces the exponential joint-action complexity as a hard exploration barrier.

Centralized-training decentralized-execution frameworks treated in article four for multi-agent policy learning admit centralized exploration bonuses that condition on the full joint state. Coordinated exploration of [Iqbal and Sha 2019][research_iqbal_sha_2019] introduces per-agent exploration bonuses that reward diverse behavior across the agent team, encouraging behavioral heterogeneity that expands the effective exploration coverage.

Influence-based exploration of [Wang Xu Sanketi Bousmalis 2020][research_wang_xu_sanketi_bousmalis_2020] rewards actions that meaningfully change other agents' behavior, capturing an information-theoretic notion of causal influence in the multi-agent setting. The framework connects to empowerment applied at the level of inter-agent interactions.

Emergent communication provides another form of coordinated exploration, in which agents develop signaling protocols that support joint exploratory behavior. Article eleven treats learning from other agents systematically and returns to these questions.

## Noisy TV and Detachment Problems

The noisy TV problem is a canonical failure mode of prediction-error curiosity. If the environment contains a source of irreducible visual noise (a static-filled television, a random particle system, dice rolls displayed on a screen), the agent's forward model will never predict the noise correctly, and prediction-error curiosity will continually reward observation of the noise source. The agent becomes stuck watching the noise instead of exploring more useful parts of the state space.

The problem was documented for the Intrinsic Curiosity Module by [Burda et al 2019][research_burda_et_al_2019] and provided motivation for several algorithmic variants. RND partially mitigates the problem because the random target network provides a fixed prediction target independent of the noise level, however, RND still fails on truly uncorrelated visual noise. Inverse-model feature encoders in ICM address the problem by ensuring that features are action-conditioned. Latent-space pseudocounts of Machado et al 2020 address it through explicit filtering of noise-only features.

The detachment problem is the failure to return to previously-discovered rewarded regions. Purely-novelty-driven agents may abandon rewarded regions once nearby states have become non-novel, leading to catastrophic forgetting of previously-learned behaviors. Never Give Up of [Badia et al 2020][research_badia_et_al_2020_ngu] addresses this by combining episodic novelty (novelty within the current episode) with lifetime novelty (novelty across all training), encouraging the agent to revisit rewarded regions episodically while still favoring long-term novelty.

Never Give Up combines episodic and lifetime novelty by multiplying the two intrinsic reward terms,

$$r^{\text{NGU}}_t = r^{\text{episodic}}_t \cdot \text{clip}(r^{\text{lifetime}}_t, 1, L)$$

where the episodic term measures novelty within the current episode via a k-nearest-neighbor distance in learned embedding space, the lifetime term measures overall novelty via RND, and the clipping bound $L$ prevents unstable amplification. The multiplicative combination encourages the agent to seek states that are both episode-novel and lifetime-novel.

The related derailment problem is the failure to reproduce successful trajectories reliably. An agent may discover a successful trajectory once but be unable to consistently reproduce it, particularly under stochastic environment dynamics. Go-Explore's exploitation phase directly addresses derailment through supervised policy training on demonstrated trajectories.

These failure modes clarify that exploration is not a single problem but a family of related problems, and successful exploration algorithms typically address multiple failure modes through complementary mechanisms.

## Exploration in Model-Based Reinforcement Learning

Model-based reinforcement learning provides a natural setting for exploration since the learned world model directly measures uncertainty about environment dynamics. Model-based exploration methods use the disagreement or uncertainty of the world model as an exploration signal, rewarding trajectories that lead to states where the model is uncertain.

Plan2Explore of [Sekar et al 2020][research_sekar_et_al_2020] extends the Dreamer world-model architecture with an ensemble of forward dynamics models trained on different data subsamples. The intrinsic reward is the disagreement among ensemble predictions,

$$r^{\text{P2E}}(s, a) = \text{Var}_k\!\left[\hat{f}_k(s, a)\right]$$

which measures epistemic uncertainty in the world model. Plan2Explore trains the exploration policy entirely in imagination through the learned world model, permitting efficient exploration without extensive real-world interaction. Self-supervised exploration via disagreement of [Pathak Gandhi and Gupta 2019][research_pathak_gandhi_gupta_2019] applied the same ensemble-disagreement approach in a model-based framework. Model-based active exploration (MAX) of [Shyam Jaśkowski and Gomez 2019][research_shyam_jaskowski_gomez_2019] uses expected information gain over model parameters as an explicit exploration objective.

Probabilistic Ensembles with Trajectory Sampling (PETS) of [Chua Calandra McAllister Levine 2018][research_chua_calandra_mcallister_levine_2018] pioneered the probabilistic-ensemble approach to model-based reinforcement learning that separates epistemic and aleatoric uncertainty in the dynamics model, providing the foundational technique that later exploration methods build on.

BYOL-Explore of [Guo et al 2022][research_guo_et_al_2022_byol_explore] uses bootstrap-your-own-latent representation learning to derive an intrinsic reward from world-model prediction error in a self-supervised representation space. The mechanism combines the noise-filtering advantages of learned representations with the model-based exploration signal.

Model-based exploration methods offer sample-efficiency advantages over model-free methods when the world model can be learned accurately, since the model amortizes real-world exploration across many simulated exploration steps. Article seven treats model-based reinforcement learning at greater length.

## Neuroscience Connections

The neuroscience of curiosity and exploration provides both empirical grounding for the intrinsic-motivation literature and hypotheses about neural implementation. [Berlyne 1960][book_berlyne_1960] treatment of curiosity connected exploratory behavior to arousal, novelty, and surprise as pre-computational categories that later informed the computational literature. [Loewenstein 1994][research_loewenstein_1994] information-gap theory of curiosity proposed that curiosity arises from awareness of a gap between what one knows and what one wants to know, providing a psychological framing that has influenced computational treatments. Reviews by [Gottlieb Oudeyer Lopes and Baranes 2013][research_gottlieb_et_al_2013] and [Kidd and Hayden 2015][research_kidd_hayden_2015] survey the psychological and neuroscientific literature on curiosity from complementary angles.

Contemporary neuroscience has identified neural systems implicated in curiosity and exploration. The locus coeruleus noradrenergic system regulates exploration through arousal state modulation, with elevated noradrenaline correlating with exploratory behavior. The [Cohen McClure and Yu 2007][research_cohen_mcclure_yu_2007_exploration] framework proposed distinct roles for dopamine and noradrenaline in directed and random exploration respectively. [Wilson Geana White Ludvig and Cohen 2014][research_wilson_geana_white_ludvig_cohen_2014] provided experimental evidence that humans use both directed and random exploration strategies in bandit tasks, with the directed component correlating with prefrontal cortex activity. [Gershman 2018][research_gershman_2018] developed a computational framework linking uncertainty representation to exploration decisions in humans.

Prefrontal cortex activation during exploration decisions has been documented by [Daw O'Doherty Dayan Seymour Dolan 2006][research_daw_odoherty_dayan_seymour_dolan_2006] and successive work using functional magnetic resonance imaging in human bandit tasks. Frontopolar cortex activation correlates with directed exploration bonuses, and the intraparietal sulcus correlates with switching between exploratory and exploitative behavior.

Reward prediction error signals in dopamine neurons, treated in article three, extend to novelty and surprise signals in overlapping systems. The [Bunzeck and Duzel 2006][research_bunzeck_duzel_2006] finding of novelty-elicited dopamine responses connects the classical reward-prediction-error framework to the novelty-driven exploration literature, suggesting a common neural substrate for extrinsic and intrinsic reward signals.

Hippocampal replay treated in article fourteen also participates in exploration by permitting simulated evaluation of possible trajectories through learned associations. The hippocampal contribution to model-based planning and exploration provides another neural substrate for the model-based exploration algorithms treated above.

Article fifteen returns to the psychology of learning literature, including systematic biases in human bandit-task performance that reveal the difference between optimal exploration and human exploration under bounded cognition.

## Empirical Landscape

The empirical landscape of exploration research has consolidated around a few standard benchmark categories. Atari 57 with emphasis on hard-exploration games (Montezuma's Revenge, Pitfall, Private Eye) provides the standard visual discrete-action benchmark. The Atari 100k regime restricts training to 100000 environment steps and emphasizes sample efficiency, making exploration algorithms particularly relevant.

Procgen and MiniHack provide procedurally-generated environments that stress generalization alongside exploration. The MiniGrid family of grid-world environments provides simpler exploration problems useful for algorithmic development and diagnostic experiments.

Continuous-control exploration benchmarks include the DeepMind Control Suite tasks with sparse-reward variants, the Meta-World robotic manipulation suite, and various procedural navigation environments. The MineRL competition of [Guss et al 2019][research_guss_et_al_2019] provided a Minecraft-based benchmark that emphasized exploration in open-world settings with human-provided demonstrations.

The [Bsuite behavior suite][research_osband_et_al_2020_bsuite] of Osband et al 2020 includes several exploration-diagnostic environments including Deep Sea and Cartpole Swingup that isolate exploration performance from other reinforcement learning capabilities.

Empirical practice for exploration research includes reporting results on multiple hard-exploration games rather than average scores across a benchmark, reporting sample efficiency at fixed compute budgets, and reporting the sensitivity of results to intrinsic-reward scaling coefficients. The hyperparameters that control the intrinsic-reward magnitude often affect final performance substantially, and reporting standards have been slower to standardize than for other subareas of deep reinforcement learning.

## Load-Bearing Open Questions

- What is the correct theoretical framework for exploration in the deep reinforcement learning setting where sample-complexity guarantees analogous to PAC-MDP are not available? Practical algorithms proliferate without a unified theoretical account.
- How can the noisy-TV problem be reliably diagnosed and mitigated in a way that generalizes across environments? Ad hoc solutions exist for benchmarks but not a general principle.
- What is the correct relationship between intrinsic and extrinsic reward? Naive addition works empirically but lacks theoretical justification, alternative schemes including two-stage training and adaptive scheduling exist without a clear winner.
- How closely do computational exploration algorithms correspond to the neural mechanisms of curiosity in the brain? Correspondence at a coarse level is well documented, but detailed algorithmic correspondence is not established.
- What is the correct treatment of exploration in multi-agent settings where other agents' behavior provides both an information source and an adversarial signal?
- Can exploration algorithms be designed to be robust to environments with irreducible-noise features without requiring domain-tuning of the intrinsic reward or feature representation?
- How should exploration budgets be allocated across a hierarchy of tasks and time scales, from micro-exploration within a single episode to macro-exploration across a lifetime of learning?
- What is the correct connection between exploration and generalization? Exploration algorithms typically evaluate on tasks with structural similarity to the training distribution, the extent to which learned exploration policies transfer to genuinely novel task distributions is not well understood.

## References

### Books

- [Berlyne 1960][book_berlyne_1960]
- [Kaelbling 1993][book_kaelbling_1993]
- [Sutton and Barto 2018][book_sutton_barto_2018]
- [Ziebart 2010][book_ziebart_2010_thesis]

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

### Research

- [Achiam Edwards Amodei 2018][research_achiam_edwards_amodei_2018]
- [Andrychowicz et al 2017][research_andrychowicz_et_al_2017_exploration]
- [Badia et al 2020 Agent57][research_badia_et_al_2020_agent57]
- [Badia et al 2020 Never Give Up][research_badia_et_al_2020_ngu]
- [Barto Singh Chentanez 2004][research_barto_singh_chentanez_2004]
- [Bellemare et al 2016][research_bellemare_et_al_2016_exploration]
- [Brafman and Tennenholtz 2002][research_brafman_tennenholtz_2002]
- [Bunzeck and Duzel 2006][research_bunzeck_duzel_2006]
- [Burda Edwards Storkey Klimov 2018][research_burda_edwards_storkey_klimov_2018]
- [Burda et al 2019][research_burda_et_al_2019]
- [Chentanez Barto Singh 2005][research_chentanez_barto_singh_2005]
- [Chua Calandra McAllister Levine 2018][research_chua_calandra_mcallister_levine_2018]
- [Cohen McClure and Yu 2007][research_cohen_mcclure_yu_2007_exploration]
- [Colas Fournier Sigaud Chetouani Oudeyer 2019][research_colas_fournier_sigaud_2019]
- [Daw O'Doherty Dayan Seymour Dolan 2006][research_daw_odoherty_dayan_seymour_dolan_2006]
- [Duan Schulman Chen Bartlett Sutskever Abbeel 2016][research_duan_schulman_chen_2016_rl2]
- [Ecoffet Huizinga Lehman Stanley Clune 2019][research_ecoffet_et_al_2019]
- [Ecoffet et al 2021][research_ecoffet_et_al_2021]
- [Eysenbach Gupta Ibarz Levine 2019][research_eysenbach_gupta_ibarz_levine_2019]
- [Florensa Held Wulfmeier Zhang Abbeel 2018][research_florensa_et_al_2018]
- [Friston 2010][research_friston_2010_active_inference]
- [Gershman 2018][research_gershman_2018]
- [Gottlieb Oudeyer Lopes Baranes 2013][research_gottlieb_et_al_2013]
- [Gregor Rezende and Wierstra 2016][research_gregor_rezende_wierstra_2016]
- [Guo et al 2022][research_guo_et_al_2022_byol_explore]
- [Guss et al 2019][research_guss_et_al_2019]
- [Gupta Mendonca Liu Abbeel Levine 2018][research_gupta_mendonca_liu_2018]
- [Houthooft Chen Duan Schulman De Turck Abbeel 2016][research_houthooft_et_al_2016]
- [Iqbal and Sha 2019][research_iqbal_sha_2019]
- [Jaksch Ortner and Auer 2010][research_jaksch_ortner_auer_2010]
- [Janz Hron Mazur Kingma Hernandez-Lobato 2019][research_janz_et_al_2019]
- [Jin Krishnamurthy Simchowitz Yu 2020][research_jin_krishnamurthy_simchowitz_yu_2020]
- [Kakade and Langford 2002][research_kakade_langford_2002_exploration]
- [Kaplan and Oudeyer 2004][research_kaplan_oudeyer_2004]
- [Kearns and Singh 2002][research_kearns_singh_2002]
- [Kidd and Hayden 2015][research_kidd_hayden_2015]
- [Klyubin Polani and Nehaniv 2005][research_klyubin_polani_nehaniv_2005]
- [Loewenstein 1994][research_loewenstein_1994]
- [Machado Bellemare and Bowling 2020][research_machado_bellemare_bowling_2020]
- [Matiisen Oliver Cohen Schulman 2019][research_matiisen_et_al_2019]
- [Modi Chen Krishnamurthy Jiang Agarwal 2021][research_modi_chen_krishnamurthy_2021]
- [Mohamed and Rezende 2015][research_mohamed_rezende_2015]
- [Nair Pong Dalal Bahl Lin Levine 2018][research_nair_pong_dalal_2018]
- [Osband and Van Roy 2013][research_osband_van_roy_2013_psrl]
- [Osband Aslanides Cassirer 2018][research_osband_aslanides_cassirer_2018]
- [Osband Blundell Pritzel and Van Roy 2016][research_osband_blundell_pritzel_van_roy_2016_exploration]
- [Osband et al 2020 Bsuite][research_osband_et_al_2020_bsuite]
- [Oudeyer Kaplan Hafner 2007][research_oudeyer_kaplan_hafner_2007]
- [Pathak Agrawal Efros Darrell 2017][research_pathak_et_al_2017]
- [Pathak Gandhi and Gupta 2019][research_pathak_gandhi_gupta_2019]
- [Plappert et al 2018][research_plappert_et_al_2018]
- [Pong Dalal Lin Nair Bahl Levine 2020][research_pong_dalal_lin_2020]
- [Portelas Colas Hofmann Oudeyer 2020][research_portelas_colas_hofmann_oudeyer_2020]
- [Salge Glackin and Polani 2014][research_salge_glackin_polani_2014]
- [Schaul Horgan Gregor Silver 2015][research_schaul_horgan_gregor_silver_2015]
- [Schmidhuber 1991][research_schmidhuber_1991]
- [Schmidhuber 2010][research_schmidhuber_2010]
- [Sekar et al 2020][research_sekar_et_al_2020]
- [Sharma Gu Levine Kumar Hausman 2020][research_sharma_et_al_2020]
- [Shyam Jaśkowski and Gomez 2019][research_shyam_jaskowski_gomez_2019]
- [Singh Barto Chentanez 2005][research_singh_barto_chentanez_2005]
- [Stadie Levine and Abbeel 2015][research_stadie_levine_abbeel_2015]
- [Storck Hochreiter and Schmidhuber 1995][research_storck_hochreiter_schmidhuber_1995]
- [Strehl and Littman 2008][research_strehl_littman_2008]
- [Tang et al 2017][research_tang_et_al_2017]
- [van den Oord Kalchbrenner Kavukcuoglu 2016][research_van_den_oord_et_al_2016]
- [Wang Kurth-Nelson Tirumala et al 2016 L2RL][research_wang_et_al_2016_l2rl]
- [Wang Lehman Clune Stanley 2019][research_wang_lehman_clune_stanley_2019]
- [Wang Lehman Rawal Zhi Zhang Clune Stanley 2020][research_wang_lehman_rawal_2020]
- [Wang Salakhutdinov Yang 2020][research_wang_salakhutdinov_yang_2020]
- [Wang Xu Sanketi Bousmalis 2020][research_wang_xu_sanketi_bousmalis_2020]
- [White 1959][research_white_1959]
- [Wilson Geana White Ludvig Cohen 2014][research_wilson_geana_white_ludvig_cohen_2014]
- [Zintgraf Shiarlis Igl et al 2020][research_zintgraf_et_al_2020]

[book_berlyne_1960]: https://psycnet.apa.org/record/1961-04263-000
[book_kaelbling_1993]: https://mitpress.mit.edu/9780262111744/learning-in-embedded-systems/
[book_sutton_barto_2018]: http://incompleteideas.net/book/the-book-2nd.html
[book_ziebart_2010_thesis]: https://www.cs.cmu.edu/~bziebart/publications/thesis-bziebart.pdf
[ref_berkeley_cs285]: https://rail.eecs.berkeley.edu/deeprlcourse/
[ref_deepmind_ucl_rl]: https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021
[ref_openai_spinning_up]: https://spinningup.openai.com/
[ref_silver_rl_course]: https://www.davidsilver.uk/teaching/
[ref_stanford_cs234]: https://web.stanford.edu/class/cs234/
[related_post_a250_framing]: {% post_url 2025-12-18-machines_that_learn_from_experience_framing %}
[related_post_a251_bandits]: {% post_url 2025-12-19-machines_that_learn_from_experience_bandits_and_online_learning %}
[related_post_a252_rl_foundations]: {% post_url 2025-12-20-machines_that_learn_from_experience_reinforcement_learning_foundations %}
[related_post_a253_deep_rl]: {% post_url 2025-12-21-machines_that_learn_from_experience_deep_reinforcement_learning %}
[research_achiam_edwards_amodei_2018]: https://arxiv.org/abs/1807.10299
[research_andrychowicz_et_al_2017_exploration]: https://papers.nips.cc/paper/2017/hash/453fadbd8a1a3af50a9df4df899537b5-Abstract.html
[research_badia_et_al_2020_agent57]: https://proceedings.mlr.press/v119/badia20a.html
[research_badia_et_al_2020_ngu]: https://openreview.net/forum?id=Sye57xStvB
[research_barto_singh_chentanez_2004]: https://all.cs.umass.edu/pubs/2004/barto_sc_ICDL04.pdf
[research_bellemare_et_al_2016_exploration]: https://papers.nips.cc/paper/2016/hash/afda332245e2af431fb7b672a68b659d-Abstract.html
[research_brafman_tennenholtz_2002]: https://www.jmlr.org/papers/v3/brafman02a.html
[research_bunzeck_duzel_2006]: https://www.cell.com/neuron/fulltext/S0896-6273(06)00475-6
[research_burda_edwards_storkey_klimov_2018]: https://openreview.net/forum?id=H1lJJnR5Ym
[research_burda_et_al_2019]: https://openreview.net/forum?id=rJNwDjAqYX
[research_chentanez_barto_singh_2005]: https://papers.nips.cc/paper/2004/hash/4be5a36cbaca8ab9d2066debfe4e65c1-Abstract.html
[research_chua_calandra_mcallister_levine_2018]: https://papers.nips.cc/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html
[research_cohen_mcclure_yu_2007_exploration]: https://royalsocietypublishing.org/doi/10.1098/rstb.2007.2098
[research_colas_fournier_sigaud_2019]: https://proceedings.mlr.press/v97/colas19a.html
[research_daw_odoherty_dayan_seymour_dolan_2006]: https://www.nature.com/articles/nature04766
[research_duan_schulman_chen_2016_rl2]: https://arxiv.org/abs/1611.02779
[research_ecoffet_et_al_2019]: https://arxiv.org/abs/1901.10995
[research_ecoffet_et_al_2021]: https://www.nature.com/articles/s41586-020-03157-9
[research_eysenbach_gupta_ibarz_levine_2019]: https://openreview.net/forum?id=SJx63jRqFm
[research_florensa_et_al_2018]: https://proceedings.mlr.press/v80/florensa18a.html
[research_friston_2010_active_inference]: https://www.nature.com/articles/nrn2787
[research_gershman_2018]: https://www.sciencedirect.com/science/article/pii/S0010027718300118
[research_gottlieb_et_al_2013]: https://www.sciencedirect.com/science/article/pii/S1364661313002052
[research_gregor_rezende_wierstra_2016]: https://arxiv.org/abs/1611.07507
[research_guo_et_al_2022_byol_explore]: https://papers.nips.cc/paper/2022/hash/49e28d29dc4b7b5e6c3ea1e4d3c0f2a5-Abstract-Conference.html
[research_guss_et_al_2019]: https://arxiv.org/abs/1907.13440
[research_gupta_mendonca_liu_2018]: https://papers.nips.cc/paper/2018/hash/2c8ebb46c2d97c9dab9a9d40a8e3d1c8-Abstract.html
[research_houthooft_et_al_2016]: https://papers.nips.cc/paper/2016/hash/abd815286ba1007abfbb8415b83ae2cf-Abstract.html
[research_iqbal_sha_2019]: https://proceedings.mlr.press/v97/iqbal19a.html
[research_jaksch_ortner_auer_2010]: https://www.jmlr.org/papers/v11/jaksch10a.html
[research_janz_et_al_2019]: https://papers.nips.cc/paper/2019/hash/4d5b995358e7798bc7e9d9db83c612a5-Abstract.html
[research_jin_krishnamurthy_simchowitz_yu_2020]: https://proceedings.mlr.press/v119/jin20d.html
[research_kakade_langford_2002_exploration]: https://homes.cs.washington.edu/~sham/papers/rl/aoarl.pdf
[research_kaplan_oudeyer_2004]: https://link.springer.com/chapter/10.1007/978-3-540-30301-5_45
[research_kearns_singh_2002]: https://link.springer.com/article/10.1023/A:1017984413808
[research_kidd_hayden_2015]: https://www.cell.com/neuron/fulltext/S0896-6273(15)00949-8
[research_klyubin_polani_nehaniv_2005]: https://ieeexplore.ieee.org/document/1554676
[research_loewenstein_1994]: https://psycnet.apa.org/record/1995-02277-001
[research_machado_bellemare_bowling_2020]: https://ojs.aaai.org/index.php/AAAI/article/view/5877
[research_matiisen_et_al_2019]: https://ieeexplore.ieee.org/document/8827566
[research_modi_chen_krishnamurthy_2021]: https://proceedings.mlr.press/v134/modi21a.html
[research_mohamed_rezende_2015]: https://papers.nips.cc/paper/2015/hash/e00406144c1e7e35240afed70f34166a-Abstract.html
[research_nair_pong_dalal_2018]: https://papers.nips.cc/paper/2018/hash/7ec69dd44416c46745f6edd947b470cd-Abstract.html
[research_osband_aslanides_cassirer_2018]: https://papers.nips.cc/paper/2018/hash/5a7b238ba0f6502e5d6be14424b20ded-Abstract.html
[research_osband_blundell_pritzel_van_roy_2016_exploration]: https://papers.nips.cc/paper/2016/hash/8d8818c8e140c64c743113f563cf750f-Abstract.html
[research_osband_et_al_2020_bsuite]: https://openreview.net/forum?id=rygf-kSYwH
[research_osband_van_roy_2013_psrl]: https://papers.nips.cc/paper/2013/hash/6a5889bb0190d0211a991f47bb19a777-Abstract.html
[research_oudeyer_kaplan_hafner_2007]: https://ieeexplore.ieee.org/document/4141061
[research_pathak_et_al_2017]: https://proceedings.mlr.press/v70/pathak17a.html
[research_pathak_gandhi_gupta_2019]: https://proceedings.mlr.press/v97/pathak19a.html
[research_plappert_et_al_2018]: https://openreview.net/forum?id=ByBAl2eAZ
[research_pong_dalal_lin_2020]: https://proceedings.mlr.press/v119/pong20a.html
[research_portelas_colas_hofmann_oudeyer_2020]: https://proceedings.mlr.press/v100/portelas20a.html
[research_salge_glackin_polani_2014]: https://link.springer.com/chapter/10.1007/978-3-319-03326-2_4
[research_schaul_horgan_gregor_silver_2015]: https://proceedings.mlr.press/v37/schaul15.html
[research_schmidhuber_1991]: https://mediatum.ub.tum.de/doc/814765/file.pdf
[research_schmidhuber_2010]: https://ieeexplore.ieee.org/document/5508364
[research_sekar_et_al_2020]: https://proceedings.mlr.press/v119/sekar20a.html
[research_sharma_et_al_2020]: https://openreview.net/forum?id=HJgLZR4KvH
[research_shyam_jaskowski_gomez_2019]: https://proceedings.mlr.press/v97/shyam19a.html
[research_singh_barto_chentanez_2005]: https://papers.nips.cc/paper/2004/hash/4be5a36cbaca8ab9d2066debfe4e65c1-Abstract.html
[research_stadie_levine_abbeel_2015]: https://arxiv.org/abs/1507.00814
[research_storck_hochreiter_schmidhuber_1995]: https://mediatum.ub.tum.de/doc/814968/file.pdf
[research_strehl_littman_2008]: https://www.sciencedirect.com/science/article/pii/S0022000008000767
[research_tang_et_al_2017]: https://papers.nips.cc/paper/2017/hash/3a20f62a0af1aa152670bab3c602feed-Abstract.html
[research_van_den_oord_et_al_2016]: https://proceedings.mlr.press/v48/oord16.html
[research_wang_et_al_2016_l2rl]: https://arxiv.org/abs/1611.05763
[research_wang_lehman_clune_stanley_2019]: https://arxiv.org/abs/1901.01753
[research_wang_lehman_rawal_2020]: https://proceedings.mlr.press/v119/wang20l.html
[research_wang_salakhutdinov_yang_2020]: https://papers.nips.cc/paper/2020/hash/f24bec27ed49d6ba5cd0e50c3ea2e6f6-Abstract.html
[research_wang_xu_sanketi_bousmalis_2020]: https://arxiv.org/abs/2002.03939
[research_white_1959]: https://psycnet.apa.org/record/1961-04411-001
[research_wilson_geana_white_ludvig_cohen_2014]: https://psycnet.apa.org/record/2014-56348-001
[research_zintgraf_et_al_2020]: https://openreview.net/forum?id=Hkl9JlBYvr
