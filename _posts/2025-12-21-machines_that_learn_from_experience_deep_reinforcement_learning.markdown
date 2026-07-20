---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: Deep Reinforcement Learning"
date:   2025-12-21 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 4
---

<!-- A253 -->
<script>console.log("A253");</script>

Deep reinforcement learning combines the algorithmic apparatus of reinforcement learning treated in article three with deep neural networks as function approximators, extending classical tabular and linear-function-approximation methods to problems with high-dimensional state and action spaces that would otherwise be intractable. The 2013 to 2025 wave of deep reinforcement learning has produced systems that master Atari games from raw pixels, achieve superhuman performance in Go and other board games via self-play, control robotic systems in continuous action spaces, and provide the post-training mechanism for large language models. This article surveys the science and theory of deep reinforcement learning as it stands in the mid 2020s, covering the extensions of tabular Q-learning to deep Q-networks and their many refinements, the extensions of policy gradient methods to trust-region and proximal policy optimization, the actor-critic family including DDPG, TD3, and SAC, the self-play line of AlphaGo through MuZero, the scaling and reproducibility considerations that shape the field's empirical practice, and the use of reinforcement learning for language-model post-training. Articles two and three of this series established the pre-Markov bandit foundation and the classical Markov decision process apparatus respectively, articles seven and eight treat model-based and offline reinforcement learning at length, this article treats the online model-free deep reinforcement learning core.

## Neural Function Approximation in Reinforcement Learning

The transition from linear to nonlinear function approximation in reinforcement learning is a qualitative change. Linear temporal-difference methods enjoy convergence guarantees under standard on-policy conditions treated in article three. Neural function approximation combined with bootstrapping and off-policy learning falls squarely within the deadly triad, and convergence guarantees are generally absent.

Empirical practice manages the instability through architectural and training-procedure interventions that are the subject of much of this article. The mechanisms include experience replay to break temporal correlation in the training data, target networks to stabilize bootstrapping targets, reward clipping or normalization to control target scale, frame stacking or recurrent state to address partial observability, careful initialization and normalization to control gradient magnitudes, and gradient clipping to prevent optimizer divergence. Each mechanism accepts the deadly triad and manages its instability rather than avoiding it.

The deep reinforcement learning field has largely accepted this arrangement. Empirical success has substantially outpaced theoretical understanding, and the theoretical framework of the field lags its practical accomplishments. Article three's treatment of the deadly triad and its classical resolutions through gradient-TD methods provides the theoretical background against which deep reinforcement learning practice should be understood.

The neural function-approximation universe adopted by deep reinforcement learning consists of the standard architectural families of deep learning, including convolutional neural networks for pixel input, multi-layer perceptrons for low-dimensional continuous state, recurrent networks for partial observability and long-range temporal dependencies, and increasingly transformers for both state processing and sequence modeling of trajectories. The [Goodfellow Bengio and Courville 2016][book_goodfellow_bengio_courville_2016] textbook and the [LeCun Bengio and Hinton 2015][research_lecun_bengio_hinton_2015] review together provide the standard references for the deep learning background that deep reinforcement learning presumes.

In deep Q-learning, the action-value function is represented as $Q_\theta(s, a) = f_\theta(s)_a$ for discrete actions, with the network $f_\theta : \mathcal{S} \to \mathbb{R}^{|\mathcal{A}|}$ mapping states to a vector of one $Q$-value per action. For continuous action spaces the parameterization becomes $Q_\theta(s, a) = g_\theta(s, a)$ where both state and action are network inputs. Policy networks parameterize $\pi_\theta(a \mid s) = h_\theta(s, a)$ for discrete actions via softmax outputs or, for continuous actions, as a Gaussian $\pi_\theta(a \mid s) = \mathcal{N}(\mu_\theta(s), \Sigma_\theta(s))$ with state-conditional mean and covariance.

## Deep Q-Networks

The Deep Q-Network algorithm was introduced in the [Mnih et al 2013][research_mnih_et_al_2013] NIPS Deep Learning workshop paper and extended into the [Mnih et al 2015][research_mnih_et_al_2015] Nature paper that provided the canonical demonstration that Q-learning with neural function approximation could reach human-level performance on Atari games from raw pixel input. The DQN loss function is the mean squared error between the network's Q-value estimate and the bootstrapped target,

$$L(\theta) = \mathbb{E}_{(s, a, r, s') \sim \mathcal{D}}\!\left[\left(r + \gamma \max_{a'} Q_{\theta^{-}}(s', a') - Q_\theta(s, a)\right)^2\right]$$

where $\mathcal{D}$ is the experience replay buffer, $\theta$ are the online network parameters, and $\theta^{-}$ are the target network parameters that are held fixed and periodically copied from $\theta$.

The convolutional architecture takes as input a stack of four grayscale $84 \times 84$ frames representing recent history and produces one Q-value output per admissible action. Three convolutional layers are followed by a fully-connected layer and an output layer of size $|\mathcal{A}|$. The frame stacking provides limited temporal context, more sophisticated approaches use recurrent networks.

Training details established the practical template for deep Q-learning that persists to the present. Experience replay uses a first-in-first-out buffer of $10^6$ transitions, from which random minibatches of size 32 are drawn for gradient updates. The target network is copied from the online network every $C = 10^4$ optimizer steps. Exploration uses $\epsilon$-greedy with $\epsilon$ linearly decayed from 1.0 to 0.1 over the first million environment steps. Reward clipping to $\{-1, 0, +1\}$ standardizes scale across games. The RMSprop optimizer with learning rate $2.5 \times 10^{-4}$ and momentum 0.95 provides the parameter updates.

Empirical results on the fifty-seven-game Arcade Learning Environment of [Bellemare Naddaf Veness and Bowling 2013][research_bellemare_naddaf_veness_bowling_2013] demonstrated human-level or superhuman play from raw pixels on approximately half the games, sub-human but nontrivial performance on others, and near-total failure on a small subset requiring long-horizon exploration or memory (notably Montezuma's Revenge). The results launched the deep reinforcement learning field as a distinct research area.

## DQN Extensions and Rainbow

Successive papers refined DQN along several dimensions. Double DQN of [van Hasselt Guez and Silver 2016][research_van_hasselt_guez_silver_2016] extends the tabular double Q-learning idea to the neural setting. The bootstrapped target uses the online network for action selection but the target network for value evaluation,

$$y_t = r_{t+1} + \gamma Q_{\theta^{-}}(s_{t+1}, \arg\max_{a'} Q_\theta(s_{t+1}, a'))$$

reducing the overestimation bias that plagues single-network Q-learning under function approximation.

Dueling DQN of [Wang et al 2016][research_wang_et_al_2016] factors the network into two streams that separately estimate the state value and the action advantage,

$$Q_\theta(s, a) = V_\theta(s) + \left(A_\theta(s, a) - \frac{1}{|\mathcal{A}|} \sum_{a'} A_\theta(s, a')\right)$$

where the advantage stream subtracts its mean to identify $V$ and $A$ up to a constant. The factorization improves learning efficiency in states where action choice matters little.

Prioritized experience replay of [Schaul Quan Antonoglou Silver 2016][research_schaul_et_al_2016] samples transitions from the buffer with sampling probability

$$P(i) = \frac{p_i^\alpha}{\sum_j p_j^\alpha}$$

where $p_i = |\delta_i| + \epsilon$ is the priority derived from the transition's absolute TD error and $\alpha \in [0, 1]$ controls the degree of prioritization. To correct for the sampling bias introduced by prioritization, gradient updates are weighted by importance-sampling weights

$$w_i = \left(\frac{1}{N \cdot P(i)}\right)^\beta$$

with $\beta$ annealed from an initial value to 1 over training. Prioritization focuses learning on the transitions where the current value estimate is most wrong and yields substantial sample efficiency improvements.

Noisy networks of [Fortunato et al 2018][research_fortunato_et_al_2018] replace $\epsilon$-greedy exploration with parametric noise added to network weights. A noisy linear layer with weight $W$ and bias $b$ is replaced by

$$y = (W_\mu + W_\sigma \odot \epsilon_W) x + (b_\mu + b_\sigma \odot \epsilon_b)$$

where $\epsilon_W, \epsilon_b$ are noise samples drawn independently or according to a factorized scheme, and $W_\sigma, b_\sigma$ are learned noise-magnitude parameters. The mechanism provides state-dependent exploration that adapts as the network learns.

Multi-step returns and distributional Q-learning treated in article three round out the standard extensions. Bootstrapped DQN of [Osband Blundell Pritzel and Van Roy 2016][research_osband_blundell_pritzel_van_roy_2016] takes a different exploration approach, maintaining an ensemble of Q-networks whose disagreement drives exploration in a posterior-sampling analogue of Thompson sampling. Data augmentation approaches including DrQ of [Kostrikov Yarats and Fergus 2020][research_kostrikov_yarats_fergus_2020] apply image transformations to observations to improve sample efficiency on pixel-based tasks.

Rainbow of [Hessel et al 2018][research_hessel_et_al_2018] combined double, dueling, prioritized replay, noisy networks, multi-step, and distributional Q-learning into a single agent that substantially outperforms any component alone on the Atari benchmark. Rainbow ablations identify multi-step returns, distributional Q-learning, and prioritized replay as the most impactful contributions in the combined system, with dueling and double DQN contributing smaller but non-negligible gains.

## Distributional Deep Q-Networks

Distributional reinforcement learning treated in article three admits a natural deep-network implementation. The C51 algorithm of [Bellemare Dabney and Munos 2017][research_bellemare_dabney_munos_2017] represents the return distribution $Z_\theta(s, a)$ as a categorical distribution over 51 atoms uniformly spaced in a fixed reward range, and the network outputs a probability vector over these atoms for each action. The distributional Bellman target is computed by projecting the shifted-and-scaled distribution back onto the fixed support, and the loss is the KL divergence between predicted and target distributions,

$$L(\theta) = \mathbb{E}_{(s, a, r, s')}\!\left[D_{\text{KL}}\!\left(\Phi \mathcal{T} Z_{\theta^{-}}(s', a^*) \,\|\, Z_\theta(s, a)\right)\right]$$

where $\Phi$ is the projection operator, $\mathcal{T}$ the distributional Bellman operator, and $a^* = \arg\max_{a'} \mathbb{E}[Z_\theta(s', a')]$.

Quantile Regression DQN of [Dabney Rowland Bellemare and Munos 2018][research_dabney_rowland_bellemare_munos_2018] represents the return distribution by its quantiles rather than a fixed categorical support. For $N$ quantiles at fixed levels $\tau_i = (2i - 1) / 2N$, the network outputs quantile values $\{Z^i_\theta(s, a)\}$ and the quantile regression loss is

$$L^{\text{QR}}(\theta) = \sum_i \sum_j \mathbb{E}\!\left[\rho_{\tau_i}(y_j - Z^i_\theta(s, a))\right]$$

where $y_j$ are the target quantile values and $\rho_\tau(u) = u(\tau - \mathbb{1}\{u < 0\})$ is the quantile Huber loss.

Implicit Quantile Networks of [Dabney Ostrovski Silver and Munos 2018][research_dabney_ostrovski_silver_munos_2018] generalize QR-DQN to arbitrary continuous quantile levels sampled at each update. The IQN network parameterizes a quantile function

$$Z_\tau(s, a) = f_\theta(\psi(s), \phi(\tau))_a$$

where $\psi(s)$ is a state encoding, $\phi(\tau)$ is a Fourier or trigonometric embedding of the quantile level $\tau \in [0, 1]$, and the combined output produces the corresponding quantile value. The formulation provides a flexible representation of the return distribution and enables risk-sensitive objectives that require quantile queries at levels other than the fixed set of QR-DQN.

Beyond immediate algorithmic gains on Atari, the distributional framework provides the natural setting for risk-sensitive objectives, uncertainty quantification, and connections to other probabilistic modeling frameworks. Article three developed the distributional theory, the deep neural implementation delivers its empirical benefits.

## Recurrent Networks and Partial Observability

Partial observability requires state representation that captures relevant history. Recurrent networks provide the standard tool for this purpose. Deep Recurrent Q-Network (DRQN) of [Hausknecht and Stone 2015][research_hausknecht_stone_2015] added an LSTM layer to the DQN architecture, processing observations sequentially rather than through frame stacking, and demonstrated improved performance on partially-observed Atari variants. R2D2 of [Kapturowski et al 2019][research_kapturowski_et_al_2019] combined LSTM with distributed prioritized replay for state-of-the-art Atari performance and introduced careful state initialization strategies to reduce sensitivity of learning to recurrent state.

Belief-state maintenance provides the theoretical interpretation. If the agent maintains a sufficient statistic of history equivalent to the belief state

$$b_t(s) = P(s_t = s \mid o_{1:t}, a_{1:t-1})$$

then the resulting sufficient-statistic-conditioned policy is equivalent to a POMDP-optimal policy. Learned recurrent representations approximate this ideal without the intractable Bayesian filtering that exact belief-state computation would require.

Transformer-based sequence models provide an alternative to recurrent networks for long-range dependencies. Adaptive Agent of [Bauer et al 2023][research_bauer_et_al_2023] and other transformer-in-RL approaches achieve competitive performance on memory-demanding benchmarks including DMLab-30 and XLand, though the compute cost is often higher than LSTM-based alternatives. The choice between recurrent and transformer backbones remains an active empirical question in the field.

## Auxiliary Tasks and Representation Learning

Auxiliary loss functions provide additional training signal beyond the main reinforcement learning objective, often improving representation quality and sample efficiency. UNREAL of [Jaderberg et al 2017][research_jaderberg_et_al_2017] added auxiliary tasks including pixel control, reward prediction, and value function replay to A3C, achieving substantial gains on the DMLab benchmark.

Self-predictive representations of [Schwarzer et al 2021][research_schwarzer_et_al_2021] and its successors use a self-supervised objective that predicts future latent states from current representation and actions,

$$L_{\text{SPR}}(\theta) = \sum_k \left\| f_{\text{proj}}(g_\theta(\phi_\theta(s_t), a_{t:t+k-1})) - \text{sg}\!\left(f_{\text{proj}}(\phi_\theta(s_{t+k}))\right) \right\|^2$$

where sg denotes stop-gradient, $\phi_\theta$ is the state encoder, $g_\theta$ is a latent transition model, and $f_{\text{proj}}$ is a projection network. The self-supervised loss substantially improves sample efficiency on Atari 100k and other data-limited benchmarks. The similar CURL algorithm of [Laskin Srinivas and Abbeel 2020][research_laskin_srinivas_abbeel_2020] uses contrastive learning between augmented views of the same observation as the auxiliary signal.

The auxiliary-task framework connects to broader trends in self-supervised learning and to model-based approaches through the shared reliance on prediction. World-model methods including Dreamer treated later can be understood as auxiliary tasks that provide additional representation-learning signal alongside the primary value learning.

## Policy Gradient at Scale

The policy gradient methods of article three extend directly to deep neural policies but require modifications to remain stable at scale. The naive REINFORCE update on a deep policy exhibits catastrophic variance and step-size sensitivity, and the practical algorithms of the deep reinforcement learning era all involve mechanisms to control the effective policy update magnitude.

Trust-region policy optimization of [Schulman Levine Moritz Jordan and Abbeel 2015][research_schulman_levine_moritz_jordan_abbeel_2015] enforces a Kullback-Leibler constraint on the policy update. The optimization problem is

$$\max_\theta \; \mathbb{E}_{s, a \sim \pi_{\theta_{\text{old}}}}\!\left[\frac{\pi_\theta(a \mid s)}{\pi_{\theta_{\text{old}}}(a \mid s)} A^{\pi_{\theta_{\text{old}}}}(s, a)\right] \quad \text{subject to} \quad \mathbb{E}_{s}\!\left[D_{\text{KL}}(\pi_{\theta_{\text{old}}}(\cdot \mid s) \,\|\, \pi_\theta(\cdot \mid s))\right] \leq \delta$$

The importance-sampling ratio $r_t(\theta) = \pi_\theta(a_t \mid s_t) / \pi_{\theta_{\text{old}}}(a_t \mid s_t)$ enables off-policy correction from the batch of trajectories collected under the old policy. TRPO solves the constrained optimization via conjugate gradient on the Fisher information matrix and line search along the natural gradient direction.

TRPO provided the first scalable trust-region method for deep policy optimization, achieving competitive performance on MuJoCo continuous control tasks. The algorithmic complexity of the conjugate-gradient solution motivated subsequent simpler alternatives.

Proximal Policy Optimization of [Schulman Wolski Dhariwal Radford Klimov 2017][research_schulman_wolski_dhariwal_radford_klimov_2017] replaces the trust-region constraint with a clipped surrogate objective,

$$L^{\text{CLIP}}(\theta) = \mathbb{E}_t\!\left[\min\!\left(r_t(\theta) \hat{A}_t, \; \text{clip}(r_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A}_t\right)\right]$$

where $\hat{A}_t$ is a generalized advantage estimate from article three. The clipping operator caps the effective step size in the direction of the advantage without requiring an explicit KL constraint or expensive second-order optimization. PPO uses first-order optimization (Adam) with multiple epochs of minibatch updates over the collected trajectory batch and has become the default policy-gradient algorithm across the field.

The complete PPO objective adds a value-function regression term and an entropy bonus,

$$L^{\text{PPO}}(\theta) = L^{\text{CLIP}}(\theta) - c_1 \mathbb{E}_t\!\left[(V_\theta(s_t) - V_t^{\text{target}})^2\right] + c_2 \mathbb{E}_t\!\left[H(\pi_\theta(\cdot \mid s_t))\right]$$

with coefficients $c_1$ and $c_2$ balancing the three terms. The simplicity of PPO's implementation and its robustness across a wide range of tasks account for its adoption. [Engstrom Ilyas Santurkar Tsipras Janoos Rudolph and Madry 2020][research_engstrom_et_al_2020] documented that many of PPO's empirical advantages come from implementation details (learning-rate annealing, orthogonal initialization, observation normalization, value function clipping, generalized advantage estimation with $\lambda$) rather than the clipping mechanism per se.

## Asynchronous and Distributed Actor-Critic

The Asynchronous Advantage Actor-Critic (A3C) algorithm of [Mnih et al 2016][research_mnih_et_al_2016] introduced distributed training for deep reinforcement learning. Multiple parallel workers each interact with independent copies of the environment, compute policy and value updates from local rollouts, and asynchronously apply the updates to a shared parameter server. The asynchronous parallelism produces effective batching of gradient updates and provides a diverse experience distribution that stabilizes learning.

The synchronous variant A2C waits for all workers to complete their rollouts before applying updates, sacrificing some asynchrony for reduced variance and easier reproducibility. Both variants demonstrated that policy-gradient methods could compete with DQN on Atari while extending naturally to continuous action spaces.

IMPALA of [Espeholt et al 2018][research_espeholt_et_al_2018] separates actor and learner processes and uses a V-trace off-policy correction to account for the lag between actor policies and the learner policy at update time. The V-trace target is a truncated importance-sampled n-step return,

$$v_t = V(s_t) + \sum_{k=t}^{t+n-1} \gamma^{k-t} \left(\prod_{j=t}^{k-1} c_j\right) \rho_k (r_{k+1} + \gamma V(s_{k+1}) - V(s_k))$$

where $c_j = \min(\bar{c}, \pi(a_j \mid s_j) / \mu(a_j \mid s_j))$ and $\rho_k = \min(\bar{\rho}, \pi(a_k \mid s_k) / \mu(a_k \mid s_k))$ are truncated importance-sampling ratios with clip constants $\bar{c}, \bar{\rho}$. V-trace enables high-throughput distributed training by tolerating policy lag that would break naive on-policy methods.

Ape-X of [Horgan et al 2018][research_horgan_et_al_2018] and R2D2 of [Kapturowski et al 2019][research_kapturowski_et_al_2019] extended the distributed actor-learner paradigm with prioritized experience replay and recurrent architectures respectively, producing systems that trained on Atari to superhuman performance in a matter of hours on multi-node clusters.

## Deterministic Policy Gradient and Continuous Control

Continuous action spaces require different algorithmic treatment than discrete actions. The Deep Deterministic Policy Gradient (DDPG) of [Lillicrap et al 2016][research_lillicrap_et_al_2016] extends the deterministic policy gradient of article three to deep networks. The actor $\mu_\theta : \mathcal{S} \to \mathcal{A}$ outputs a deterministic action, and the critic $Q_w(s, a)$ estimates the action-value. The critic is trained by the standard DQN-style TD loss, and the actor is trained by the deterministic policy gradient

$$\nabla_\theta J(\theta) = \mathbb{E}_{s \sim d^\mu}\!\left[\nabla_\theta \mu_\theta(s) \nabla_a Q_w(s, a)|_{a = \mu_\theta(s)}\right]$$

Exploration is added by injecting noise into the deterministic action at training time, either Ornstein-Uhlenbeck noise as in the original paper or independent Gaussian noise as in later work.

Twin Delayed DDPG (TD3) of [Fujimoto Hoof and Meger 2018][research_fujimoto_hoof_meger_2018] addresses three DDPG failure modes. Twin critics take the minimum of two independently-trained Q-networks in the target computation,

$$y = r + \gamma \min_{i \in \{1, 2\}} Q_{w_i^{-}}(s', \tilde{a}), \quad \tilde{a} = \mu_{\theta^{-}}(s') + \epsilon$$

where $\epsilon \sim \text{clip}(\mathcal{N}(0, \sigma^2), -c, c)$ is clipped Gaussian target policy smoothing noise. The min operator reduces overestimation bias analogously to double Q-learning, the target policy smoothing regularizes the value function against sharp local overestimates, and delayed policy updates apply the actor gradient only every $d$ critic updates to prevent policy exploitation of critic errors.

Soft Actor-Critic (SAC) of [Haarnoja Zhou Abbeel and Levine 2018][research_haarnoja_zhou_abbeel_levine_2018] replaces the standard reinforcement learning objective with a maximum-entropy objective

$$J_{\text{SAC}}(\pi) = \mathbb{E}\!\left[\sum_{t=0}^{\infty} \gamma^t \left(r_{t+1} + \alpha H(\pi(\cdot \mid s_t))\right)\right]$$

where the entropy bonus with temperature $\alpha$ encourages stochastic policies. The corresponding soft Bellman equation for the state value function is

$$V^\pi(s) = \mathbb{E}_{a \sim \pi}\!\left[Q^\pi(s, a) - \alpha \log \pi(a \mid s)\right]$$

and for the action value function,

$$Q^\pi(s, a) = \mathbb{E}_{s'}\!\left[r + \gamma V^\pi(s')\right]$$

SAC learns a stochastic Gaussian policy and uses the reparameterization trick

$$a = \mu_\theta(s) + \sigma_\theta(s) \odot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

to obtain low-variance policy gradient estimates by backpropagating through the sampled action. Automatic temperature tuning targets a desired minimum entropy $\bar{H}$ by adjusting $\alpha$ according to the loss

$$L(\alpha) = -\alpha \mathbb{E}\!\left[\log \pi_\theta(a \mid s) + \bar{H}\right]$$

rather than fixing $\alpha$ as a hyperparameter. SAC is generally the most robust off-policy continuous-control algorithm as of the mid 2020s, with reliable performance across the MuJoCo continuous control benchmarks.

Both DDPG-family and SAC algorithms use Polyak-averaged target networks

$$\theta^{-} \leftarrow \tau \theta + (1 - \tau) \theta^{-}$$

with small $\tau$ (typically 0.005) to stabilize bootstrapping targets.

The MuJoCo continuous control benchmarks including HalfCheetah, Hopper, Walker2d, Ant, and Humanoid provide the standardized evaluation setting. The DeepMind Control Suite of [Tassa et al 2018][research_tassa_et_al_2018] extends the benchmarks with additional tasks and richer observation modalities. GPU-parallelized physics simulators including Isaac Gym have enabled millions of environment steps per second, further reducing the wall-clock cost of continuous-control experiments.

## Transformer Architectures and Decision Sequences

Transformer architectures introduced to reinforcement learning in the late 2010s and early 2020s reframed the problem as sequence modeling of trajectories. Rather than iterating value or policy updates through temporal-difference or policy gradient learning, the transformer approach directly models the distribution of successful trajectories and generates actions conditioned on prior history and target outcomes.

Decision Transformer of [Chen et al 2021][research_chen_et_al_2021] treats reinforcement learning as sequence modeling by autoregressively predicting actions conditioned on states, previous actions, and target returns-to-go. The model factorizes the trajectory as

$$P(\tau) = \prod_t P(a_t \mid s_{t-K:t}, a_{t-K:t-1}, \hat{R}_{t-K:t})$$

where $\hat{R}_t = \sum_{k=t}^{T} r_k$ is the return-to-go from time $t$. Training uses standard supervised learning loss on trajectory data without value bootstrapping or off-policy corrections. The target return-to-go conditioning provides a form of policy specification at inference time. The agent generates actions consistent with achieving the specified return. Decision Transformer performs competitively with model-free offline RL methods and simplifies the algorithmic apparatus considerably.

Trajectory Transformer of [Janner Li and Levine 2021][research_janner_li_levine_2021] similarly models the full trajectory distribution over discretized state-action-reward tokens and uses beam search over token sequences for planning. The formulation unifies model-based planning and model-free policy learning through the shared transformer sequence model.

Gato of [Reed et al 2022][research_reed_et_al_2022] extended the transformer approach to a multi-task generalist agent trained on hundreds of tasks including Atari games, robotic manipulation, image captioning, and dialogue, demonstrating that a single 1.2-billion-parameter transformer can handle a diverse task portfolio via appropriate tokenization of heterogeneous inputs and outputs.

Video PreTraining of [Baker et al 2022][research_baker_et_al_2022] used behavioral cloning on unlabeled Internet videos of Minecraft gameplay to train a foundation model that could then be fine-tuned with reinforcement learning, achieving substantial sample-efficiency improvements. The approach connects deep reinforcement learning to the pretraining-then-fine-tuning paradigm familiar from large language models.

The transformer-based approaches trade the sample-inefficient online exploration of classical deep RL for the scaling advantages of offline sequence modeling. Whether this trade-off dominates depends on the availability of large trajectory datasets, the availability of expressive value functions or reward signals, and the compute budget. Article eight treats offline RL directly and returns to these questions.

## AlphaGo, AlphaZero, and MuZero

The self-play line of DeepMind's Go and general-game programs constitutes the most striking achievement of deep reinforcement learning to date. AlphaGo of [Silver et al 2016][research_silver_et_al_2016] combined supervised learning from human games with reinforcement learning via self-play and Monte Carlo tree search (MCTS) to defeat world champion Lee Sedol in March 2016.

The architecture used two neural networks. A policy network trained by supervised learning on human moves predicted human move distributions and was fine-tuned by policy gradient on self-play games. A value network trained on self-play games predicted the outcome from a given position. During gameplay, MCTS explored a search tree with the value network scoring leaf positions and the policy network providing prior probabilities for tree expansion.

AlphaGo Zero of [Silver et al 2017][research_silver_et_al_2017] simplified the approach by eliminating human game data entirely and combining policy and value networks into a single dual-head network $f_\theta(s) = (p, v)$ that outputs a policy distribution and a value estimate. MCTS uses the PUCT selection rule

$$a_t = \arg\max_a \left[Q(s_t, a) + c_{\text{puct}} \, p(a \mid s_t) \frac{\sqrt{\sum_b N(s_t, b)}}{1 + N(s_t, a)}\right]$$

with $Q(s, a)$ the mean action value from tree statistics, $p(a \mid s)$ the neural network policy prior, $N(s, a)$ the visit count, and $c_{\text{puct}}$ an exploration constant. The training loop alternates self-play games under the current network with MCTS, and network updates minimize the combined loss

$$L(\theta) = (z - v_\theta(s))^2 - \boldsymbol{\pi}^\top \log \boldsymbol{p}_\theta(s) + c \|\theta\|^2$$

where $z \in \{-1, 0, +1\}$ is the game outcome, $\boldsymbol{\pi}$ is the MCTS-improved policy from search visit counts, and the final term is L2 regularization. The resulting agent exceeded the strength of AlphaGo Master and the earlier AlphaGo Lee Sedol version within 40 days of training on 4 TPUs.

AlphaZero of [Silver et al 2018][research_silver_et_al_2018] extended the AlphaGo Zero algorithm to chess, shogi, and Go with a single training pipeline, achieving superhuman performance in all three games from scratch using only the game rules and the reward signal at terminal positions. AlphaZero demonstrated that the same algorithm suffices for a broad class of two-player zero-sum perfect-information games.

MuZero of [Schrittwieser et al 2020][research_schrittwieser_et_al_2020] removed the assumption that the environment model is known. Three neural networks parameterize a learned model. A representation function $h_\theta(o_1, \ldots, o_t) = s^0$ encodes past observations into an internal state, a dynamics function $g_\theta(s^{k-1}, a^k) = (r^k, s^k)$ predicts the reward and next internal state given an action, and a prediction function $f_\theta(s^k) = (p^k, v^k)$ predicts policy and value from internal state. MCTS operates over the learned internal state space rather than the true environment. The MuZero training loss combines terms for observed reward, value, and policy at each unrolled step,

$$L_t(\theta) = \sum_{k=0}^{K} \left[(r_{t+k} - r_\theta^k)^2 + (z_{t+k} - v_\theta^k)^2 - \boldsymbol{\pi}_{t+k}^\top \log \boldsymbol{p}_\theta^k\right] + c \|\theta\|^2$$

where $K$ is the number of unrolled steps and $z_{t+k}$ is the $n$-step or full-return target. MuZero achieved superhuman play in chess, shogi, and Go while also matching state-of-the-art on Atari, unifying the previously-distinct settings of board games and video games under a single algorithm.

The self-play line demonstrates the power of combining deep reinforcement learning, tree search, and self-generated training data. The success in board games has proved harder to replicate in domains without perfect information or with substantial stochasticity, though [Perolat et al 2022][research_perolat_et_al_2022] Player of Games extended the paradigm to imperfect-information games including no-limit poker, and EfficientZero and Sampled MuZero variants extended to continuous control settings.

## Model-Based Deep Reinforcement Learning

Model-based deep reinforcement learning learns an internal model of environment dynamics and uses it for planning or value estimation. Article seven treats the topic at length, a brief survey positions the field's contemporary state.

World Models of [Ha and Schmidhuber 2018][research_ha_schmidhuber_2018] proposed learning a compressed latent-state representation via variational autoencoder, forward dynamics via mixture density recurrent networks in the latent space, and a compact policy in the latent space via policy gradient or evolution strategies. The framework demonstrated substantial sample efficiency gains on visual reinforcement learning benchmarks.

The Dreamer series extends latent-state world models with the Recurrent State Space Model and actor-critic learning entirely in imagination, progressively improving performance across visual control benchmarks. [Hafner Lillicrap Fischer Villegas Ha Lee Davidson 2019][research_hafner_et_al_2019] Dreamer established the base algorithm, [Hafner Lillicrap Norouzi and Ba 2020][research_hafner_et_al_2020] DreamerV2 achieved competitive performance on Atari, and [Hafner Pasukonis Ba and Lillicrap 2023][research_hafner_et_al_2023] DreamerV3 achieved competitive performance across a wide range of continuous control, discrete action, and video game domains with a single set of hyperparameters, providing evidence that model-based deep reinforcement learning has reached practical maturity.

MuZero and its extensions blur the distinction between model-based and model-free by learning implicit models that support MCTS planning without requiring the model to predict raw observations. EfficientZero of [Ye Liu Kurutach Abbeel and Gao 2021][research_ye_liu_kurutach_abbeel_gao_2021] extended MuZero with several modifications including self-supervised consistency losses and value prefix prediction, achieving comparable performance to MuZero with 100000 environment steps rather than millions. SimPLe of [Kaiser et al 2019][research_kaiser_et_al_2019] provided an earlier demonstration that model-based Atari play with reasonable sample efficiency is feasible using deep video-prediction models.

The distinction between explicit generative models and implicit planning models has become substantially less sharp in the deep reinforcement learning era than the corresponding distinction in classical reinforcement learning.

## Multi-Agent Deep Reinforcement Learning

Multi-agent settings introduce non-stationarity from each agent's perspective, since other agents adapt in response to observed behavior. Classical algorithms based on single-agent MDP assumptions do not directly apply, and deep multi-agent reinforcement learning has developed specialized techniques.

Centralized training with decentralized execution provides a widely-used framework. During training, agents access global information for value estimation or actor updates, during execution, each agent conditions only on its local observations. MADDPG of [Lowe et al 2017][research_lowe_et_al_2017] extends DDPG to multi-agent settings by training each agent's critic on the full joint action space while restricting the actor to local observations.

QMIX of [Rashid et al 2018][research_rashid_et_al_2018] factors the joint value function as a monotonic mixture of per-agent utility functions,

$$Q_{\text{tot}}(\boldsymbol{s}, \boldsymbol{a}) = f_{\text{mix}}(Q_1(s_1, a_1), \ldots, Q_n(s_n, a_n) ; \boldsymbol{s})$$

where the mixing network $f_{\text{mix}}$ has monotonically non-negative weights conditioning on the global state. The monotonicity constraint preserves individual-global maximum consistency,

$$\arg\max_{\boldsymbol{a}} Q_{\text{tot}}(\boldsymbol{s}, \boldsymbol{a}) = (\arg\max_{a_1} Q_1(s_1, a_1), \ldots, \arg\max_{a_n} Q_n(s_n, a_n))$$

enabling decentralized greedy execution while maintaining a coherent joint value function during training. QTRAN of [Son et al 2019][research_son_et_al_2019] and other successor methods relax the monotonicity constraint for greater expressiveness at the cost of more complex training.

Independent Q-learning treats each agent as facing an MDP with fixed other agents but suffers from the non-stationarity introduced by other agents' learning. QMIX, MADDPG, and their descendants attempt to mitigate this through joint-value factorization or centralized critics.

Self-play in zero-sum games has produced the strongest deep multi-agent RL results. AlphaStar of [Vinyals et al 2019][research_vinyals_et_al_2019] combined a large population of self-play agents with a league training approach in StarCraft II, defeating professional players. OpenAI Five of [OpenAI et al 2019][research_openai_five_2019] used self-play combined with team play for Dota 2. Player of Games treated earlier extends self-play to imperfect-information settings.

Emergent communication and social dilemmas provide other important research directions in multi-agent RL, connecting to game theory, mechanism design, and cognitive science. Article eleven treats learning from other agents at greater length.

## Reinforcement Learning from Human Feedback

Reinforcement learning from human feedback has become the standard post-training mechanism for large language models. The approach originates in [Christiano Leike Brown Martic Legg and Amodei 2017][research_christiano_et_al_2017] preference-based reinforcement learning. Rather than requiring an engineered reward function, the algorithm learns a reward model from human comparisons of trajectory segments and optimizes policy against the learned reward via standard reinforcement learning (typically PPO).

[Stiennon et al 2020][research_stiennon_et_al_2020] applied preference-based reinforcement learning to text summarization, demonstrating that RLHF-trained models produce summaries preferred to supervised-learning baselines by human evaluators. [Ouyang et al 2022][research_ouyang_et_al_2022] InstructGPT extended the approach to general instruction-following, producing the modern RLHF template that underlies contemporary conversational assistants.

The standard RLHF pipeline proceeds in three stages. First, supervised fine-tuning on human demonstrations aligns the model with instruction-following behavior. Second, a reward model $R_\phi(x, y)$ is trained on human preference comparisons using the Bradley-Terry model,

$$P(y_w \succ y_l \mid x) = \sigma(R_\phi(x, y_w) - R_\phi(x, y_l))$$

with the reward-model loss

$$L^{\text{RM}}(\phi) = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}}\!\left[\log \sigma(R_\phi(x, y_w) - R_\phi(x, y_l))\right]$$

for preferred completion $y_w$ and dispreferred completion $y_l$. Third, PPO optimizes the policy against the learned reward model with a KL penalty against the supervised-fine-tuned model,

$$L^{\text{RLHF}}(\theta) = \mathbb{E}_{x, y \sim \pi_\theta}\!\left[R(x, y)\right] - \beta \mathbb{E}_{x, y \sim \pi_\theta}\!\left[D_{\text{KL}}\!\left(\pi_\theta(y \mid x) \,\|\, \pi_{\text{SFT}}(y \mid x)\right)\right]$$

where $\pi_{\text{SFT}}$ is the supervised-fine-tuned reference model and $\beta$ is a KL penalty coefficient that prevents the policy from drifting too far from the reference.

Direct Preference Optimization of [Rafailov Sharma Mitchell Manning Ermon Finn 2023][research_rafailov_et_al_2023] eliminates the explicit reward model by deriving a closed-form loss that directly optimizes the policy against preference data. The DPO loss

$$L^{\text{DPO}}(\theta) = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}}\!\left[\log \sigma\!\left(\beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{SFT}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{SFT}}(y_l \mid x)}\right)\right]$$

for preferred completion $y_w$ and dispreferred completion $y_l$ trades the standard reinforcement learning apparatus for a simpler supervised-learning-style optimization. DPO and its variants have become widely adopted for open-source language model post-training.

Constitutional AI of [Bai et al 2022a][research_bai_et_al_2022a] Constitutional AI and reinforcement learning from AI feedback replace human preference labels with model-generated preferences guided by a set of natural-language principles, reducing the human-annotation cost while raising questions about circular training dynamics that article eleven treats in the broader preference-learning context. The [Bai et al 2022b][research_bai_et_al_2022b] Anthropic helpful-and-harmless training-a-helpful-and-harmless-assistant paper provided detailed methodology for the RLHF pipeline that has become the standard reference. [Casper et al 2023][research_casper_et_al_2023] surveys open problems and fundamental limitations of RLHF including reward hacking, mode collapse, and misgeneralization of learned reward models. The scope of this article limits treatment of the alignment aspects to the algorithmic apparatus, broader concerns are treated elsewhere in the series.

## Scaling and Compute

Deep reinforcement learning systems have scaled substantially in compute cost over the past decade. AlphaGo Zero trained on 4 TPUs for approximately 40 days. AlphaStar of [Vinyals et al 2019][research_vinyals_et_al_2019] on StarCraft II used a large distributed training system involving thousands of concurrent games. OpenAI Five on Dota 2 used approximately 128000 CPU cores for training. The RLHF post-training of contemporary large language models involves clusters comparable to the pretraining setup.

Scaling laws for reinforcement learning have received recent attention. [Andrychowicz et al 2021][research_andrychowicz_et_al_2021] characterized what matters in policy-gradient RL through a large-scale empirical study, identifying algorithmic details, network architecture, hyperparameter choices, and problem-factors that individually or collectively determine performance. [Hilton et al 2023][research_hilton_et_al_2023] studied scaling laws for compute in single-agent reinforcement learning, finding that reinforcement learning shows compute-efficiency improvements comparable to supervised learning under appropriate parameterization. Their compute-efficiency law takes the approximate form

$$\text{Score}(C) - \text{Score}_{\max} = -\alpha C^{-\beta}$$

for compute budget $C$ and constants $\alpha, \beta$ that depend on the domain, mirroring the power-law form observed in supervised learning scaling.

Practical scaling considerations include the choice of on-policy versus off-policy algorithms (off-policy generally scales better because it decouples data collection from optimization), the choice of synchronous versus asynchronous distributed training, the tradeoff between environment throughput and gradient throughput, and hyperparameter sensitivity at scale. The engineering complexity of contemporary deep reinforcement learning systems approaches that of large-scale supervised learning training pipelines.

Hyperparameter sensitivity remains a notorious feature of deep reinforcement learning. Learning rates, batch sizes, network architectures, replay buffer sizes, target network update frequencies, and exploration schedules all substantially affect final performance, and the sensitivity often extends to seemingly minor implementation details.

## Sim-to-Real Transfer

Deep reinforcement learning policies trained in simulation frequently fail to transfer to physical systems without additional engineering. The sim-to-real gap encompasses several distinct phenomena, including differences in dynamics between simulator and reality, differences in observation modalities and noise characteristics, differences in reward signal fidelity, and unmodeled environmental factors.

Domain randomization of [Tobin Fong Ray Schneider Zaremba Abbeel 2017][research_tobin_et_al_2017] trains policies on randomized simulator parameters (visual textures, physical properties, sensor noise, actuator delays) so that reality falls within the training distribution. The policy learns to be robust to the randomized variations and transfers to reality without additional adaptation. The subsequent [Peng Andrychowicz Zaremba Abbeel 2018][research_peng_andrychowicz_zaremba_abbeel_2018] paper extended the approach to dynamics randomization for physical robot manipulation.

System identification uses real-world data to estimate simulator parameters, adapting the simulator to reality rather than the policy. Combined approaches interleave simulation training with real-world calibration and progressively narrow the sim-to-real gap.

Learning from demonstration provides an alternative to pure reinforcement learning. Real-world demonstrations, either from humans or from teleoperated systems, initialize policies that reinforcement learning then refines. Article eleven treats learning from demonstration systematically.

The dexterous manipulation results of [OpenAI et al 2019 Dactyl][research_openai_dactyl_2019] achieved sim-to-real transfer for in-hand manipulation of a Rubik's cube using extensive domain randomization combined with automatic domain randomization that adaptively expands the randomization ranges as the policy improves. RGB-based robotic manipulation benchmarks including RoboSuite and Meta-World provide standardized settings for sim-to-real research.

The extent to which sim-to-real transfer succeeds remains a matter of considerable practical engineering effort. Article thirteen on embodied cognition and developmental robotics returns to related themes from a different angle.

## Reproducibility and Empirical Challenges

The reproducibility challenges of deep reinforcement learning have been documented at length. [Henderson et al 2018][research_henderson_et_al_2018] showed that deep RL results are frequently more variable across random seeds and implementations than reported summary statistics suggest, with substantially different conclusions possible from different seed subsets of the same algorithm on the same benchmark.

[Andrychowicz et al 2021][research_andrychowicz_et_al_2021] provided the largest empirical study of what matters in policy-gradient RL to date, systematically varying 22 factors across 5 different algorithms on standard benchmarks. Their conclusions include that many algorithmic choices interact strongly with hyperparameters, that reported algorithmic advantages are often smaller than or comparable to hyperparameter-choice effects, and that reproducibility requires careful controls over implementation details.

[Engstrom et al 2020][research_engstrom_et_al_2020] performed a detailed ablation of PPO implementations and identified that a substantial fraction of PPO's advantage over TRPO comes from implementation-level details (Adam optimizer, learning-rate annealing, orthogonal initialization, observation normalization, value function clipping, generalized advantage estimation) rather than the clipping mechanism per se.

Contemporary best-practice guidelines include running experiments with at least 10 random seeds per configuration, reporting median performance and interquartile range or bootstrap confidence intervals rather than only mean and standard error, providing full hyperparameter specifications and code, and evaluating on multiple benchmark suites to check generalization of algorithmic improvements. Open-source reference implementations including Stable Baselines3, CleanRL, and RLlib support reproducibility efforts by providing standardized algorithm implementations.

The [Agarwal Schwarzer Castro Courville Bellemare 2021][research_agarwal_et_al_2021] deep reinforcement learning statistical practice paper proposed the interquartile mean and stratified bootstrap confidence intervals as more informative summary statistics than the standard mean-and-median reporting. The [Colas Sigaud and Oudeyer 2018][research_colas_sigaud_oudeyer_2018] and [Colas Sigaud Oudeyer 2019][research_colas_sigaud_oudeyer_2019] papers argued for statistically-grounded seed budget planning in deep reinforcement learning. The rlberry and rliable Python packages support these statistical practices.

## Empirical Benchmark Landscape

The empirical landscape of deep reinforcement learning has evolved substantially. The original Atari 57 benchmark of [Bellemare Naddaf Veness and Bowling 2013][research_bellemare_naddaf_veness_bowling_2013] remains a canonical discrete-action visual benchmark, extended by the Atari 100k benchmark that emphasizes sample efficiency by restricting learning to 100000 environment steps.

Continuous control benchmarks include the MuJoCo suite of [Todorov Erez and Tassa 2012][research_todorov_erez_tassa_2012], the DeepMind Control Suite of [Tassa et al 2018][research_tassa_et_al_2018], and their GPU-parallelized successors including Isaac Gym. Robotic manipulation benchmarks include Meta-World, RoboSuite, and RLBench.

Generalization benchmarks including Procgen of [Cobbe et al 2019][research_cobbe_et_al_2019] and NetHack of [Küttler et al 2020][research_kuttler_et_al_2020] emphasize procedural generation to prevent memorization and test out-of-distribution generalization.

Behavior suite for reinforcement learning of [Osband et al 2020][research_osband_et_al_2020] provides a diagnostic set of simple tasks that isolate reinforcement learning capabilities (exploration, generalization, memory, credit assignment) for controlled algorithmic comparison.

Complex-multi-agent strategy game benchmarks including StarCraft II and Dota 2 have provided challenge problems that stressed the field's capabilities. AlphaStar and OpenAI Five demonstrated deep reinforcement learning agents competitive with top human players in these games, though the systems required substantial engineering effort and compute investment beyond what typical deep RL benchmarks admit.

## Neuroscience Connections

The neuroscience connections of deep reinforcement learning are more complex than those of the classical apparatus treated in article three. Deep neural networks provide potentially closer models of biological neural systems than tabular or linear function approximation, and the learned representations of deep RL agents show some alignment with neural representations in the primate visual cortex.

[Cadieu et al 2014][research_cadieu_et_al_2014] and [Yamins and DiCarlo 2016][research_yamins_dicarlo_2016] documented that supervised-trained convolutional networks produce internal representations that predict responses of neurons in inferior temporal cortex on unseen images better than any hand-designed feature representation. The finding suggests that convolutional architectures capture something important about the visual system's computation. Whether similar alignment holds for the value and policy representations learned by deep RL agents remains an active research area.

Deep predictive coding models of [Rao and Ballard 1999][research_rao_ballard_1999] and their successors provide neuroscience-inspired architectures that learn latent-state representations by predicting sensory inputs. These models connect to model-based deep reinforcement learning through their shared reliance on prediction as a training signal. Article seven treats predictive coding at length.

The prefrontal cortex has been interpreted as implementing meta-reinforcement learning by [Wang Kurth-Nelson Tirumala Soyer Leibo Munos Blundell Kumaran Botvinick 2018][research_wang_et_al_2018], with recurrent activity supporting fast adaptation across tasks while slower dopaminergic updates train the recurrent weights themselves. [Botvinick et al 2020][research_botvinick_et_al_2020] surveyed the broader implications of deep reinforcement learning insights for neuroscience. The Tolman-Eichenbaum machine of [Whittington Muller Mark Chen Barry Burgess Behrens 2020][research_whittington_et_al_2020] proposes a unified computational model that links spatial navigation, memory, and reinforcement learning through generalization mechanisms in the hippocampal formation. Article fourteen treats the NeuroAI bridge at length.

Despite these correspondences, deep RL agents differ from biological learners in ways that constrain the analogy. Sample complexity in deep RL is typically many orders of magnitude worse than animal learning on comparable tasks. Learning dynamics differ substantially, with deep RL requiring millions or billions of samples where animals learn in tens or hundreds. Robustness to distribution shift and adversarial perturbation is a substantial gap. Article fourteen treats the NeuroAI bridge at length, the survey here notes the connections without pretending they resolve the deeper mysteries.

## Load-Bearing Open Questions

- Why does deep reinforcement learning work at all given the deadly triad of off-policy learning, function approximation, and bootstrapping that classical theory predicts should destabilize convergence?
- What is the correct theoretical framework for the deep reinforcement learning success? Sample-complexity theory, regret analysis, and convergence guarantees have largely lagged behind the empirical practice.
- How can the sample efficiency of deep reinforcement learning be brought closer to that of biological learning? Current systems require sample complexity many orders of magnitude greater than animals achieve on comparable tasks.
- What is the correct way to characterize and mitigate the reproducibility challenges of deep reinforcement learning? Standardized benchmarks and statistical practices help but do not fully resolve the problem.
- How should sim-to-real transfer be understood theoretically and improved practically? Deep RL policies trained in simulation frequently fail to transfer to physical systems without substantial additional engineering.
- What is the theoretical basis for the empirical success of RLHF in language-model post-training? The KL-constrained reward maximization framework is well-understood in principle, but its empirical effectiveness on high-dimensional language-model policies is not fully theoretically explained.
- How should deep reinforcement learning agents be evaluated for generalization beyond training distribution? Procedural generation benchmarks address the problem partially, but full out-of-distribution generalization remains an open challenge.
- What is the correct architectural inductive bias for deep reinforcement learning? Convolutional networks, recurrent networks, transformers, and mixture models each capture aspects, and no unified architectural framework has emerged.

## References

### Books

- [Goodfellow Bengio and Courville 2016][book_goodfellow_bengio_courville_2016]
- [Sutton and Barto 2018][book_sutton_barto_2018]

### Reference

- [Berkeley CS285][ref_berkeley_cs285]
- [CleanRL][ref_cleanrl]
- [Farama Foundation Gymnasium][ref_farama_gymnasium]
- [OpenAI Spinning Up][ref_openai_spinning_up]
- [Stable Baselines3][ref_stable_baselines]
- [Sutton and Barto Second Edition PDF][ref_sutton_barto_pdf]

### Related Posts

- [A250 Machines That Learn From Experience Framing][related_post_a250_framing]
- [A251 Machines That Learn From Experience Bandits and Online Learning][related_post_a251_bandits]
- [A252 Machines That Learn From Experience Reinforcement Learning Foundations][related_post_a252_rl_foundations]

### Research

- [Agarwal Schwarzer Castro Courville Bellemare 2021][research_agarwal_et_al_2021]
- [Andrychowicz et al 2021][research_andrychowicz_et_al_2021]
- [Bai et al 2022a][research_bai_et_al_2022a]
- [Bai et al 2022b][research_bai_et_al_2022b]
- [Baker et al 2022][research_baker_et_al_2022]
- [Bauer et al 2023][research_bauer_et_al_2023]
- [Bellemare Dabney and Munos 2017][research_bellemare_dabney_munos_2017]
- [Bellemare Naddaf Veness Bowling 2013][research_bellemare_naddaf_veness_bowling_2013]
- [Botvinick et al 2020][research_botvinick_et_al_2020]
- [Cadieu et al 2014][research_cadieu_et_al_2014]
- [Casper et al 2023][research_casper_et_al_2023]
- [Chen et al 2021][research_chen_et_al_2021]
- [Christiano Leike Brown Martic Legg Amodei 2017][research_christiano_et_al_2017]
- [Cobbe et al 2019][research_cobbe_et_al_2019]
- [Colas Sigaud Oudeyer 2018][research_colas_sigaud_oudeyer_2018]
- [Colas Sigaud Oudeyer 2019][research_colas_sigaud_oudeyer_2019]
- [Dabney Ostrovski Silver Munos 2018][research_dabney_ostrovski_silver_munos_2018]
- [Dabney Rowland Bellemare Munos 2018][research_dabney_rowland_bellemare_munos_2018]
- [Engstrom et al 2020][research_engstrom_et_al_2020]
- [Espeholt et al 2018][research_espeholt_et_al_2018]
- [Fortunato et al 2018][research_fortunato_et_al_2018]
- [Fujimoto Hoof and Meger 2018][research_fujimoto_hoof_meger_2018]
- [Ha and Schmidhuber 2018][research_ha_schmidhuber_2018]
- [Haarnoja Zhou Abbeel Levine 2018][research_haarnoja_zhou_abbeel_levine_2018]
- [Hafner et al 2019][research_hafner_et_al_2019]
- [Hafner et al 2020][research_hafner_et_al_2020]
- [Hafner et al 2023][research_hafner_et_al_2023]
- [Hausknecht and Stone 2015][research_hausknecht_stone_2015]
- [Henderson et al 2018][research_henderson_et_al_2018]
- [Hessel et al 2018][research_hessel_et_al_2018]
- [Hilton et al 2023][research_hilton_et_al_2023]
- [Horgan et al 2018][research_horgan_et_al_2018]
- [Jaderberg et al 2017][research_jaderberg_et_al_2017]
- [Janner Li and Levine 2021][research_janner_li_levine_2021]
- [Kaiser et al 2019][research_kaiser_et_al_2019]
- [Kapturowski et al 2019][research_kapturowski_et_al_2019]
- [Kostrikov Yarats and Fergus 2020][research_kostrikov_yarats_fergus_2020]
- [Küttler et al 2020][research_kuttler_et_al_2020]
- [Laskin Srinivas Abbeel 2020][research_laskin_srinivas_abbeel_2020]
- [LeCun Bengio and Hinton 2015][research_lecun_bengio_hinton_2015]
- [Lillicrap et al 2016][research_lillicrap_et_al_2016]
- [Lowe et al 2017][research_lowe_et_al_2017]
- [Mnih et al 2013][research_mnih_et_al_2013]
- [Mnih et al 2015][research_mnih_et_al_2015]
- [Mnih et al 2016][research_mnih_et_al_2016]
- [OpenAI Dactyl 2019][research_openai_dactyl_2019]
- [OpenAI Five 2019][research_openai_five_2019]
- [Osband Blundell Pritzel and Van Roy 2016][research_osband_blundell_pritzel_van_roy_2016]
- [Osband et al 2020][research_osband_et_al_2020]
- [Ouyang et al 2022][research_ouyang_et_al_2022]
- [Peng Andrychowicz Zaremba Abbeel 2018][research_peng_andrychowicz_zaremba_abbeel_2018]
- [Perolat et al 2022][research_perolat_et_al_2022]
- [Rafailov Sharma Mitchell Manning Ermon Finn 2023][research_rafailov_et_al_2023]
- [Rao and Ballard 1999][research_rao_ballard_1999]
- [Rashid et al 2018][research_rashid_et_al_2018]
- [Reed et al 2022][research_reed_et_al_2022]
- [Schaul Quan Antonoglou Silver 2016][research_schaul_et_al_2016]
- [Schrittwieser et al 2020][research_schrittwieser_et_al_2020]
- [Schulman Levine Moritz Jordan Abbeel 2015][research_schulman_levine_moritz_jordan_abbeel_2015]
- [Schulman Wolski Dhariwal Radford Klimov 2017][research_schulman_wolski_dhariwal_radford_klimov_2017]
- [Schwarzer et al 2021][research_schwarzer_et_al_2021]
- [Silver et al 2016][research_silver_et_al_2016]
- [Silver et al 2017][research_silver_et_al_2017]
- [Silver et al 2018][research_silver_et_al_2018]
- [Son et al 2019][research_son_et_al_2019]
- [Stiennon et al 2020][research_stiennon_et_al_2020]
- [Tassa et al 2018][research_tassa_et_al_2018]
- [Tobin et al 2017][research_tobin_et_al_2017]
- [Todorov Erez and Tassa 2012][research_todorov_erez_tassa_2012]
- [van Hasselt Guez Silver 2016][research_van_hasselt_guez_silver_2016]
- [Vinyals et al 2019][research_vinyals_et_al_2019]
- [Wang et al 2016][research_wang_et_al_2016]
- [Wang et al 2018][research_wang_et_al_2018]
- [Whittington et al 2020][research_whittington_et_al_2020]
- [Yamins and DiCarlo 2016][research_yamins_dicarlo_2016]
- [Ye Liu Kurutach Abbeel Gao 2021][research_ye_liu_kurutach_abbeel_gao_2021]

[book_goodfellow_bengio_courville_2016]: https://www.deeplearningbook.org/
[book_sutton_barto_2018]: http://incompleteideas.net/book/the-book-2nd.html
[ref_berkeley_cs285]: https://rail.eecs.berkeley.edu/deeprlcourse/
[ref_cleanrl]: https://docs.cleanrl.dev/
[ref_farama_gymnasium]: https://gymnasium.farama.org/
[ref_openai_spinning_up]: https://spinningup.openai.com/
[ref_stable_baselines]: https://stable-baselines3.readthedocs.io/
[ref_sutton_barto_pdf]: http://incompleteideas.net/book/RLbook2020.pdf
[related_post_a250_framing]: {% post_url 2025-12-18-machines_that_learn_from_experience_framing %}
[related_post_a251_bandits]: {% post_url 2025-12-19-machines_that_learn_from_experience_bandits_and_online_learning %}
[related_post_a252_rl_foundations]: {% post_url 2025-12-20-machines_that_learn_from_experience_reinforcement_learning_foundations %}
[research_agarwal_et_al_2021]: https://papers.nips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html
[research_andrychowicz_et_al_2021]: https://openreview.net/forum?id=nIAxjsniDzg
[research_bai_et_al_2022a]: https://arxiv.org/abs/2212.08073
[research_bai_et_al_2022b]: https://arxiv.org/abs/2204.05862
[research_baker_et_al_2022]: https://papers.nips.cc/paper/2022/hash/9c7008aff45b5d8f0973b23e1a22ada0-Abstract-Conference.html
[research_bauer_et_al_2023]: https://arxiv.org/abs/2301.07608
[research_bellemare_dabney_munos_2017]: https://proceedings.mlr.press/v70/bellemare17a.html
[research_bellemare_naddaf_veness_bowling_2013]: https://www.jair.org/index.php/jair/article/view/10819
[research_botvinick_et_al_2020]: https://www.cell.com/neuron/fulltext/S0896-6273(20)30437-5
[research_cadieu_et_al_2014]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003963
[research_casper_et_al_2023]: https://arxiv.org/abs/2307.15217
[research_chen_et_al_2021]: https://papers.nips.cc/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html
[research_christiano_et_al_2017]: https://papers.nips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html
[research_cobbe_et_al_2019]: https://arxiv.org/abs/1912.01588
[research_colas_sigaud_oudeyer_2018]: https://arxiv.org/abs/1806.08295
[research_colas_sigaud_oudeyer_2019]: https://arxiv.org/abs/1904.06979
[research_dabney_ostrovski_silver_munos_2018]: https://proceedings.mlr.press/v80/dabney18a.html
[research_dabney_rowland_bellemare_munos_2018]: https://ojs.aaai.org/index.php/AAAI/article/view/11791
[research_engstrom_et_al_2020]: https://openreview.net/forum?id=r1etN1rtPB
[research_espeholt_et_al_2018]: https://proceedings.mlr.press/v80/espeholt18a.html
[research_fortunato_et_al_2018]: https://openreview.net/forum?id=rywHCPkAW
[research_fujimoto_hoof_meger_2018]: https://proceedings.mlr.press/v80/fujimoto18a.html
[research_ha_schmidhuber_2018]: https://papers.nips.cc/paper/2018/hash/2de5d16682c3c35007e4e92982f1a2ba-Abstract.html
[research_haarnoja_zhou_abbeel_levine_2018]: https://proceedings.mlr.press/v80/haarnoja18b.html
[research_hafner_et_al_2019]: https://proceedings.mlr.press/v97/hafner19a.html
[research_hafner_et_al_2020]: https://openreview.net/forum?id=0oabwyZbOu
[research_hafner_et_al_2023]: https://arxiv.org/abs/2301.04104
[research_hausknecht_stone_2015]: https://arxiv.org/abs/1507.06527
[research_henderson_et_al_2018]: https://ojs.aaai.org/index.php/AAAI/article/view/11694
[research_hessel_et_al_2018]: https://ojs.aaai.org/index.php/AAAI/article/view/11796
[research_hilton_et_al_2023]: https://arxiv.org/abs/2301.13442
[research_horgan_et_al_2018]: https://openreview.net/forum?id=H1Dy---0Z
[research_jaderberg_et_al_2017]: https://openreview.net/forum?id=SJ6yPD5xg
[research_janner_li_levine_2021]: https://papers.nips.cc/paper/2021/hash/099fe6b0b444c23836c4a5d07346082b-Abstract.html
[research_kaiser_et_al_2019]: https://arxiv.org/abs/1903.00374
[research_kapturowski_et_al_2019]: https://openreview.net/forum?id=r1lyTjAqYX
[research_kostrikov_yarats_fergus_2020]: https://arxiv.org/abs/2004.13649
[research_kuttler_et_al_2020]: https://papers.nips.cc/paper/2020/hash/569ff987c643b4bedf504efda8f786c2-Abstract.html
[research_laskin_srinivas_abbeel_2020]: https://proceedings.mlr.press/v119/laskin20a.html
[research_lecun_bengio_hinton_2015]: https://www.nature.com/articles/nature14539
[research_lillicrap_et_al_2016]: https://arxiv.org/abs/1509.02971
[research_lowe_et_al_2017]: https://papers.nips.cc/paper/2017/hash/68a9750337a418a86fe06c1991a1d64c-Abstract.html
[research_mnih_et_al_2013]: https://arxiv.org/abs/1312.5602
[research_mnih_et_al_2015]: https://www.nature.com/articles/nature14236
[research_mnih_et_al_2016]: https://proceedings.mlr.press/v48/mniha16.html
[research_openai_dactyl_2019]: https://arxiv.org/abs/1910.07113
[research_openai_five_2019]: https://arxiv.org/abs/1912.06680
[research_osband_blundell_pritzel_van_roy_2016]: https://papers.nips.cc/paper/2016/hash/8d8818c8e140c64c743113f563cf750f-Abstract.html
[research_osband_et_al_2020]: https://openreview.net/forum?id=rygf-kSYwH
[research_ouyang_et_al_2022]: https://papers.nips.cc/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html
[research_peng_andrychowicz_zaremba_abbeel_2018]: https://ieeexplore.ieee.org/document/8460528
[research_perolat_et_al_2022]: https://www.science.org/doi/10.1126/science.add4679
[research_rafailov_et_al_2023]: https://papers.nips.cc/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html
[research_rao_ballard_1999]: https://www.nature.com/articles/nn0199_79
[research_rashid_et_al_2018]: https://proceedings.mlr.press/v80/rashid18a.html
[research_reed_et_al_2022]: https://arxiv.org/abs/2205.06175
[research_schaul_et_al_2016]: https://arxiv.org/abs/1511.05952
[research_schrittwieser_et_al_2020]: https://www.nature.com/articles/s41586-020-03051-4
[research_schulman_levine_moritz_jordan_abbeel_2015]: https://proceedings.mlr.press/v37/schulman15.html
[research_schulman_wolski_dhariwal_radford_klimov_2017]: https://arxiv.org/abs/1707.06347
[research_schwarzer_et_al_2021]: https://openreview.net/forum?id=uCQfPZwRaUu
[research_silver_et_al_2016]: https://www.nature.com/articles/nature16961
[research_silver_et_al_2017]: https://www.nature.com/articles/nature24270
[research_silver_et_al_2018]: https://www.science.org/doi/10.1126/science.aar6404
[research_son_et_al_2019]: https://proceedings.mlr.press/v97/son19a.html
[research_stiennon_et_al_2020]: https://papers.nips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html
[research_tassa_et_al_2018]: https://arxiv.org/abs/1801.00690
[research_tobin_et_al_2017]: https://ieeexplore.ieee.org/document/8202133
[research_todorov_erez_tassa_2012]: https://ieeexplore.ieee.org/document/6386109
[research_van_hasselt_guez_silver_2016]: https://ojs.aaai.org/index.php/AAAI/article/view/10295
[research_vinyals_et_al_2019]: https://www.nature.com/articles/s41586-019-1724-z
[research_wang_et_al_2016]: https://proceedings.mlr.press/v48/wangf16.html
[research_wang_et_al_2018]: https://www.nature.com/articles/s41593-018-0147-8
[research_whittington_et_al_2020]: https://www.cell.com/cell/fulltext/S0092-8674(20)31388-X
[research_yamins_dicarlo_2016]: https://www.nature.com/articles/nn.4244
[research_ye_liu_kurutach_abbeel_gao_2021]: https://papers.nips.cc/paper/2021/hash/d5eca8dc3820cad9fe56a3bafda65ca1-Abstract.html
