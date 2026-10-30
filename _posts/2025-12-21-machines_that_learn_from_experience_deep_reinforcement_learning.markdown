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

The neural function-approximation universe adopted by deep reinforcement learning consists of the standard architectural families of deep learning, including convolutional neural networks for pixel input, multi-layer perceptrons for low-dimensional continuous state, recurrent networks for partial observability and long-range temporal dependencies, and increasingly transformers for both state processing and sequence modeling of trajectories. The [Goodfellow et al. 2016][book_goodfellow_bengio_courville_2016] textbook and the [LeCun et al. 2015][research_lecun_bengio_hinton_2015] review together provide the standard references for the deep learning background that deep reinforcement learning presumes.

In deep Q-learning, the action-value function is represented as $Q_\theta(s, a) = f_\theta(s)\_a$ for discrete actions, with the network $f_\theta : \mathcal{S} \to \mathbb{R}^{\lvert \mathcal{A} \rvert}$ mapping states to a vector of one $Q$-value per action. For continuous action spaces the parameterization becomes $Q_\theta(s, a) = g_\theta(s, a)$ where both state and action are network inputs. Policy networks parameterize $\pi_\theta(a \mid s) = h_\theta(s, a)$ for discrete actions via softmax outputs or, for continuous actions, as a Gaussian $\pi_\theta(a \mid s) = \mathcal{N}(\mu_\theta(s), \Sigma_\theta(s))$ with state-conditional mean and covariance.

## Deep Q-Networks

The Deep Q-Network algorithm was introduced in the [Mnih et al. 2013][research_mnih_et_al_2013] NIPS Deep Learning workshop paper and extended into the [Mnih et al. 2015][research_mnih_et_al_2015] Nature paper that provided the canonical demonstration that Q-learning with neural function approximation could reach human-level performance on Atari games from raw pixel input. The DQN loss function is the mean squared error between the network's Q-value estimate and the bootstrapped target,

$$
L(\theta) = \mathbb{E}_{(s, a, r, s') \sim \mathcal{D}}\!\left[\left(r + \gamma \max_{a'} Q_{\theta^{-}}(s', a') - Q_\theta(s, a)\right)^2\right]
\tag{1}
$$

where $\mathcal{D}$ is the experience replay buffer, $\theta$ are the online network parameters, and $\theta^{-}$ are the target network parameters that are held fixed and periodically copied from $\theta$.

The convolutional architecture takes as input a stack of four grayscale $84 \times 84$ frames representing recent history and produces one Q-value output per admissible action. Three convolutional layers are followed by a fully-connected layer and an output layer of size $\lvert \mathcal{A} \rvert$. The frame stacking provides limited temporal context, more sophisticated approaches use recurrent networks.

Training details established the practical template for deep Q-learning that persists to the present. Experience replay uses a first-in-first-out buffer of $10^6$ transitions, from which random minibatches of size 32 are drawn for gradient updates. The target network is copied from the online network every $C = 10^4$ optimizer steps. Exploration uses $\epsilon$-greedy with $\epsilon$ linearly decayed from 1.0 to 0.1 over the first million environment steps. Reward clipping to $\{-1, 0, +1\}$ standardizes scale across games. The RMSprop optimizer with learning rate $2.5 \times 10^{-4}$ and momentum 0.95 provides the parameter updates.

Empirical results on the fifty-seven-game Arcade Learning Environment of [Bellemare et al. 2013][research_bellemare_naddaf_veness_bowling_2013] demonstrated human-level or superhuman play from raw pixels on approximately half the games, sub-human but nontrivial performance on others, and near-total failure on a small subset requiring long-horizon exploration or memory (notably Montezuma's Revenge). The results launched the deep reinforcement learning field as a distinct research area.

## DQN Extensions and Rainbow

Successive papers refined DQN along several dimensions. Double DQN of [van Hasselt et al. 2016][research_van_hasselt_guez_silver_2016] extends the tabular double Q-learning idea to the neural setting. The bootstrapped target uses the online network for action selection but the target network for value evaluation,

$$
y_t = r_{t+1} + \gamma Q_{\theta^{-}}(s_{t+1}, \arg\max_{a'} Q_\theta(s_{t+1}, a'))
\tag{2}
$$

reducing the overestimation bias that plagues single-network Q-learning under function approximation.

Dueling DQN of [Wang et al. 2016][research_wang_et_al_2016] factors the network into two streams that separately estimate the state value and the action advantage,

$$
Q_\theta(s, a) = V_\theta(s) + \left(A_\theta(s, a) - \frac{1}{|\mathcal{A}|} \sum_{a'} A_\theta(s, a')\right)
\tag{3}
$$

where the advantage stream subtracts its mean to identify $V$ and $A$ up to a constant. The factorization improves learning efficiency in states where action choice matters little.

Prioritized experience replay of [Schaul et al. 2015][research_schaul_et_al_2016] samples transitions from the buffer with sampling probability

$$
P(i) = \frac{p_i^\alpha}{\sum_j p_j^\alpha}
\tag{4}
$$

where $p_i = \lvert \delta_i \rvert + \epsilon$ is the priority derived from the transition's absolute TD error and $\alpha \in [0, 1]$ controls the degree of prioritization. To correct for the sampling bias introduced by prioritization, gradient updates are weighted by importance-sampling weights

$$
w_i = \left(\frac{1}{N \cdot P(i)}\right)^\beta
\tag{5}
$$

with $\beta$ annealed from an initial value to 1 over training. Prioritization focuses learning on the transitions where the current value estimate is most wrong and yields substantial sample efficiency improvements.

Noisy networks of [Fortunato et al. 2018][research_fortunato_et_al_2018] replace $\epsilon$-greedy exploration with parametric noise added to network weights. A noisy linear layer with weight $W$ and bias $b$ is replaced by

$$
y = (W_\mu + W_\sigma \odot \epsilon_W) x + (b_\mu + b_\sigma \odot \epsilon_b)
\tag{6}
$$

where $\epsilon_W, \epsilon_b$ are noise samples drawn independently or according to a factorized scheme, and $W_\sigma, b_\sigma$ are learned noise-magnitude parameters. The mechanism provides state-dependent exploration that adapts as the network learns.

Multi-step returns and distributional Q-learning treated in article three round out the standard extensions. Bootstrapped DQN of [Osband et al. 2016][research_osband_blundell_pritzel_van_roy_2016] takes a different exploration approach, maintaining an ensemble of Q-networks whose disagreement drives exploration in a posterior-sampling analogue of Thompson sampling. Data augmentation approaches including DrQ of [Kostrikov et al. 2020][research_kostrikov_yarats_fergus_2020] apply image transformations to observations to improve sample efficiency on pixel-based tasks.

Rainbow of [Hessel et al. 2018][research_hessel_et_al_2018] combined double, dueling, prioritized replay, noisy networks, multi-step, and distributional Q-learning into a single agent that substantially outperforms any component alone on the Atari benchmark. Rainbow ablations identify multi-step returns, distributional Q-learning, and prioritized replay as the most impactful contributions in the combined system, with dueling and double DQN contributing smaller but non-negligible gains.

## Distributional Deep Q-Networks

Distributional reinforcement learning treated in article three admits a natural deep-network implementation. The C51 algorithm of [Bellemare et al. 2017][research_bellemare_dabney_munos_2017] represents the return distribution $Z_\theta(s, a)$ as a categorical distribution over 51 atoms uniformly spaced in a fixed reward range, and the network outputs a probability vector over these atoms for each action. The distributional Bellman target is computed by projecting the shifted-and-scaled distribution back onto the fixed support, and the loss is the KL divergence between predicted and target distributions,

$$
L(\theta) = \mathbb{E}_{(s, a, r, s')}\!\left[D_{\text{KL}}\!\left(\Phi \mathcal{T} Z_{\theta^{-}}(s', a^*) \,\|\, Z_\theta(s, a)\right)\right]
\tag{7}
$$

where $\Phi$ is the projection operator, $\mathcal{T}$ the distributional Bellman operator, and $a^\* = \arg\max_{a'} \mathbb{E}[Z_\theta(s', a')]$.

Quantile Regression DQN of [Dabney et al. 2018a][research_dabney_rowland_bellemare_munos_2018] represents the return distribution by its quantiles rather than a fixed categorical support. For $N$ quantiles at fixed levels $\tau_i = (2i - 1) / 2N$, the network outputs quantile values $\{Z^i_\theta(s, a)\}$ and the quantile regression loss is

$$
L^{\text{QR}}(\theta) = \sum_i \sum_j \mathbb{E}\!\left[\rho_{\tau_i}(y_j - Z^i_\theta(s, a))\right]
\tag{8}
$$

where $y_j$ are the target quantile values and $\rho_\tau(u) = u(\tau - \mathbb{1}\{u < 0\})$ is the quantile Huber loss.

Implicit Quantile Networks of [Dabney et al. 2018b][research_dabney_ostrovski_silver_munos_2018] generalize QR-DQN to arbitrary continuous quantile levels sampled at each update. The IQN network parameterizes a quantile function

$$
Z_\tau(s, a) = f_\theta(\psi(s), \phi(\tau))_a
\tag{9}
$$

where $\psi(s)$ is a state encoding, $\phi(\tau)$ is a Fourier or trigonometric embedding of the quantile level $\tau \in [0, 1]$, and the combined output produces the corresponding quantile value. The formulation provides a flexible representation of the return distribution and enables risk-sensitive objectives that require quantile queries at levels other than the fixed set of QR-DQN.

Beyond immediate algorithmic gains on Atari, the distributional framework provides the natural setting for risk-sensitive objectives, uncertainty quantification, and connections to other probabilistic modeling frameworks. Article three developed the distributional theory, the deep neural implementation delivers its empirical benefits.

## Recurrent Networks and Partial Observability

Partial observability requires state representation that captures relevant history. Recurrent networks provide the standard tool for this purpose. Deep Recurrent Q-Network (DRQN) of [Hausknecht and Stone 2015][research_hausknecht_stone_2015] added an LSTM layer to the DQN architecture, processing observations sequentially rather than through frame stacking, and demonstrated improved performance on partially-observed Atari variants. R2D2 of [Kapturowski et al. 2019][research_kapturowski_et_al_2019] combined LSTM with distributed prioritized replay for state-of-the-art Atari performance and introduced careful state initialization strategies to reduce sensitivity of learning to recurrent state.

Belief-state maintenance provides the theoretical interpretation. If the agent maintains a sufficient statistic of history equivalent to the belief state

$$
b_t(s) = P(s_t = s \mid o_{1:t}, a_{1:t-1})
\tag{10}
$$

then the resulting sufficient-statistic-conditioned policy is equivalent to a POMDP-optimal policy. Learned recurrent representations approximate this ideal without the intractable Bayesian filtering that exact belief-state computation would require.

Transformer-based sequence models provide an alternative to recurrent networks for long-range dependencies. Adaptive Agent of [Adaptive Agent Team et al. 2023][research_bauer_et_al_2023] and other transformer-in-RL approaches achieve competitive performance on memory-demanding benchmarks including DMLab-30 and XLand, though the compute cost is often higher than LSTM-based alternatives. The choice between recurrent and transformer backbones remains an active empirical question in the field.

## Auxiliary Tasks and Representation Learning

Auxiliary loss functions provide additional training signal beyond the main reinforcement learning objective, often improving representation quality and sample efficiency. UNREAL of [Jaderberg et al. 2017][research_jaderberg_et_al_2017] added auxiliary tasks including pixel control, reward prediction, and value function replay to A3C, achieving substantial gains on the DMLab benchmark.

Self-predictive representations of [Schwarzer et al. 2021][research_schwarzer_et_al_2021] and its successors use a self-supervised objective that predicts future latent states from current representation and actions,

$$
L_{\text{SPR}}(\theta) = \sum_k \left\| f_{\text{proj}}(g_\theta(\phi_\theta(s_t), a_{t:t+k-1})) - \text{sg}\!\left(f_{\text{proj}}(\phi_\theta(s_{t+k}))\right) \right\|^2
\tag{11}
$$

where sg denotes stop-gradient, $\phi_\theta$ is the state encoder, $g_\theta$ is a latent transition model, and $f_{\text{proj}}$ is a projection network. The self-supervised loss substantially improves sample efficiency on Atari 100k and other data-limited benchmarks. The similar CURL algorithm of [Laskin et al. 2020][research_laskin_srinivas_abbeel_2020] uses contrastive learning between augmented views of the same observation as the auxiliary signal.

The auxiliary-task framework connects to broader trends in self-supervised learning and to model-based approaches through the shared reliance on prediction. World-model methods including Dreamer treated later can be understood as auxiliary tasks that provide additional representation-learning signal alongside the primary value learning.

## Policy Gradient at Scale

The policy gradient methods of article three extend directly to deep neural policies but require modifications to remain stable at scale. The naive REINFORCE update on a deep policy exhibits catastrophic variance and step-size sensitivity, and the practical algorithms of the deep reinforcement learning era all involve mechanisms to control the effective policy update magnitude.

Trust-region policy optimization of [Schulman et al. 2015][research_schulman_levine_moritz_jordan_abbeel_2015] enforces a Kullback-Leibler constraint on the policy update. The optimization problem is

$$
\max_\theta \; \mathbb{E}_{s, a \sim \pi_{\theta_{\text{old}}}}\!\left[\frac{\pi_\theta(a \mid s)}{\pi_{\theta_{\text{old}}}(a \mid s)} A^{\pi_{\theta_{\text{old}}}}(s, a)\right] \quad \text{subject to} \quad \mathbb{E}_{s}\!\left[D_{\text{KL}}(\pi_{\theta_{\text{old}}}(\cdot \mid s) \,\|\, \pi_\theta(\cdot \mid s))\right] \leq \delta
\tag{12}
$$

The importance-sampling ratio $r_t(\theta) = \pi_\theta(a_t \mid s_t) / \pi_{\theta_{\text{old}}}(a_t \mid s_t)$ enables off-policy correction from the batch of trajectories collected under the old policy. TRPO solves the constrained optimization via conjugate gradient on the Fisher information matrix and line search along the natural gradient direction.

TRPO provided the first scalable trust-region method for deep policy optimization, achieving competitive performance on MuJoCo continuous control tasks. The algorithmic complexity of the conjugate-gradient solution motivated subsequent simpler alternatives.

Proximal Policy Optimization of [Schulman et al. 2017][research_schulman_wolski_dhariwal_radford_klimov_2017] replaces the trust-region constraint with a clipped surrogate objective,

$$
L^{\text{CLIP}}(\theta) = \mathbb{E}_t\!\left[\min\!\left(r_t(\theta) \hat{A}_t, \; \text{clip}(r_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A}_t\right)\right]
\tag{13}
$$

where $\hat{A}\_t$ is a generalized advantage estimate from article three. The clipping operator caps the effective step size in the direction of the advantage without requiring an explicit KL constraint or expensive second-order optimization. PPO uses first-order optimization (Adam) with multiple epochs of minibatch updates over the collected trajectory batch and has become the default policy-gradient algorithm across the field.

The complete PPO objective adds a value-function regression term and an entropy bonus,

$$
L^{\text{PPO}}(\theta) = L^{\text{CLIP}}(\theta) - c_1 \mathbb{E}_t\!\left[(V_\theta(s_t) - V_t^{\text{target}})^2\right] + c_2 \mathbb{E}_t\!\left[H(\pi_\theta(\cdot \mid s_t))\right]
\tag{14}
$$

with coefficients $c_1$ and $c_2$ balancing the three terms. The simplicity of PPO's implementation and its robustness across a wide range of tasks account for its adoption. [Engstrom et al. 2020][research_engstrom_et_al_2020] documented that many of PPO's empirical advantages come from implementation details (learning-rate annealing, orthogonal initialization, observation normalization, value function clipping, generalized advantage estimation with $\lambda$) rather than the clipping mechanism per se.

## Asynchronous and Distributed Actor-Critic

The Asynchronous Advantage Actor-Critic (A3C) algorithm of [Mnih et al. 2016][research_mnih_et_al_2016] introduced distributed training for deep reinforcement learning. Multiple parallel workers each interact with independent copies of the environment, compute policy and value updates from local rollouts, and asynchronously apply the updates to a shared parameter server. The asynchronous parallelism produces effective batching of gradient updates and provides a diverse experience distribution that stabilizes learning.

The synchronous variant A2C waits for all workers to complete their rollouts before applying updates, sacrificing some asynchrony for reduced variance and easier reproducibility. Both variants demonstrated that policy-gradient methods could compete with DQN on Atari while extending naturally to continuous action spaces.

IMPALA of [Espeholt et al. 2018][research_espeholt_et_al_2018] separates actor and learner processes and uses a V-trace off-policy correction to account for the lag between actor policies and the learner policy at update time. The V-trace target is a truncated importance-sampled n-step return,

$$
v_t = V(s_t) + \sum_{k=t}^{t+n-1} \gamma^{k-t} \left(\prod_{j=t}^{k-1} c_j\right) \rho_k (r_{k+1} + \gamma V(s_{k+1}) - V(s_k))
\tag{15}
$$

where $c_j = \min(\bar{c}, \pi(a_j \mid s_j) / \mu(a_j \mid s_j))$ and $\rho_k = \min(\bar{\rho}, \pi(a_k \mid s_k) / \mu(a_k \mid s_k))$ are truncated importance-sampling ratios with clip constants $\bar{c}, \bar{\rho}$. V-trace enables high-throughput distributed training by tolerating policy lag that would break naive on-policy methods.

Ape-X of [Horgan 2018][research_horgan_et_al_2018] and R2D2 of [Kapturowski et al. 2019][research_kapturowski_et_al_2019] extended the distributed actor-learner paradigm with prioritized experience replay and recurrent architectures respectively, producing systems that trained on Atari to superhuman performance in a matter of hours on multi-node clusters.

## Deterministic Policy Gradient and Continuous Control

Continuous action spaces require different algorithmic treatment than discrete actions. The Deep Deterministic Policy Gradient (DDPG) of [Lillicrap et al. 2015][research_lillicrap_et_al_2016] extends the deterministic policy gradient of article three to deep networks. The actor $\mu_\theta : \mathcal{S} \to \mathcal{A}$ outputs a deterministic action, and the critic $Q_w(s, a)$ estimates the action-value. The critic is trained by the standard DQN-style TD loss, and the actor is trained by the deterministic policy gradient

$$
\nabla_\theta J(\theta) = \mathbb{E}_{s \sim d^\mu}\!\left[\nabla_\theta \mu_\theta(s) \nabla_a Q_w(s, a)|_{a = \mu_\theta(s)}\right]
\tag{16}
$$

Exploration is added by injecting noise into the deterministic action at training time, either Ornstein-Uhlenbeck noise as in the original paper or independent Gaussian noise as in later work.

Twin Delayed DDPG (TD3) of [Fujimoto et al. 2018][research_fujimoto_hoof_meger_2018] addresses three DDPG failure modes. Twin critics take the minimum of two independently-trained Q-networks in the target computation,

$$
y = r + \gamma \min_{i \in \{1, 2\}} Q_{w_i^{-}}(s', \tilde{a}), \quad \tilde{a} = \mu_{\theta^{-}}(s') + \epsilon
\tag{17}
$$

where $\epsilon \sim \text{clip}(\mathcal{N}(0, \sigma^2), -c, c)$ is clipped Gaussian target policy smoothing noise. The min operator reduces overestimation bias analogously to double Q-learning, the target policy smoothing regularizes the value function against sharp local overestimates, and delayed policy updates apply the actor gradient only every $d$ critic updates to prevent policy exploitation of critic errors.

Soft Actor-Critic (SAC) of [Haarnoja et al. 2018][research_haarnoja_zhou_abbeel_levine_2018] replaces the standard reinforcement learning objective with a maximum-entropy objective

$$
J_{\text{SAC}}(\pi) = \mathbb{E}\!\left[\sum_{t=0}^{\infty} \gamma^t \left(r_{t+1} + \alpha H(\pi(\cdot \mid s_t))\right)\right]
\tag{18}
$$

where the entropy bonus with temperature $\alpha$ encourages stochastic policies. The corresponding soft Bellman equation for the state value function is

$$
V^\pi(s) = \mathbb{E}_{a \sim \pi}\!\left[Q^\pi(s, a) - \alpha \log \pi(a \mid s)\right]
\tag{19}
$$

and for the action value function,

$$
Q^\pi(s, a) = \mathbb{E}_{s'}\!\left[r + \gamma V^\pi(s')\right]
\tag{20}
$$

SAC learns a stochastic Gaussian policy and uses the reparameterization trick

$$
a = \mu_\theta(s) + \sigma_\theta(s) \odot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)
\tag{21}
$$

to obtain low-variance policy gradient estimates by backpropagating through the sampled action. Automatic temperature tuning targets a desired minimum entropy $\bar{H}$ by adjusting $\alpha$ according to the loss

$$
L(\alpha) = -\alpha \mathbb{E}\!\left[\log \pi_\theta(a \mid s) + \bar{H}\right]
\tag{22}
$$

rather than fixing $\alpha$ as a hyperparameter. SAC is generally the most robust off-policy continuous-control algorithm as of the mid 2020s, with reliable performance across the MuJoCo continuous control benchmarks.

Both DDPG-family and SAC algorithms use Polyak-averaged target networks

$$
\theta^{-} \leftarrow \tau \theta + (1 - \tau) \theta^{-}
\tag{23}
$$

with small $\tau$ (typically 0.005) to stabilize bootstrapping targets.

The MuJoCo continuous control benchmarks including HalfCheetah, Hopper, Walker2d, Ant, and Humanoid provide the standardized evaluation setting. The DeepMind Control Suite of [Tassa et al. 2018][research_tassa_et_al_2018] extends the benchmarks with additional tasks and richer observation modalities. GPU-parallelized physics simulators including Isaac Gym have enabled millions of environment steps per second, further reducing the wall-clock cost of continuous-control experiments.

## Transformer Architectures and Decision Sequences

Transformer architectures introduced to reinforcement learning in the late 2010s and early 2020s reframed the problem as sequence modeling of trajectories. Rather than iterating value or policy updates through temporal-difference or policy gradient learning, the transformer approach directly models the distribution of successful trajectories and generates actions conditioned on prior history and target outcomes.

Decision Transformer of [Chen et al. 2021][research_chen_et_al_2021] treats reinforcement learning as sequence modeling by autoregressively predicting actions conditioned on states, previous actions, and target returns-to-go. The model factorizes the trajectory as

$$
P(\tau) = \prod_t P(a_t \mid s_{t-K:t}, a_{t-K:t-1}, \hat{R}_{t-K:t})
\tag{24}
$$

where $\hat{R}\_t = \sum_{k=t}^{T} r_k$ is the return-to-go from time $t$. Training uses standard supervised learning loss on trajectory data without value bootstrapping or off-policy corrections. The target return-to-go conditioning provides a form of policy specification at inference time. The agent generates actions consistent with achieving the specified return. Decision Transformer performs competitively with model-free offline RL methods and simplifies the algorithmic apparatus considerably.

Trajectory Transformer of [Janner et al. 2021][research_janner_li_levine_2021] similarly models the full trajectory distribution over discretized state-action-reward tokens and uses beam search over token sequences for planning. The formulation unifies model-based planning and model-free policy learning through the shared transformer sequence model.

Gato of [Reed et al. 2022][research_reed_et_al_2022] extended the transformer approach to a multi-task generalist agent trained on hundreds of tasks including Atari games, robotic manipulation, image captioning, and dialogue, demonstrating that a single 1.2-billion-parameter transformer can handle a diverse task portfolio via appropriate tokenization of heterogeneous inputs and outputs.

Video PreTraining of [Baker et al. 2022][research_baker_et_al_2022] used behavioral cloning on unlabeled Internet videos of Minecraft gameplay to train a foundation model that could then be fine-tuned with reinforcement learning, achieving substantial sample-efficiency improvements. The approach connects deep reinforcement learning to the pretraining-then-fine-tuning paradigm familiar from large language models.

The transformer-based approaches trade the sample-inefficient online exploration of classical deep RL for the scaling advantages of offline sequence modeling. Whether this trade-off dominates depends on the availability of large trajectory datasets, the availability of expressive value functions or reward signals, and the compute budget. Article eight treats offline RL directly and returns to these questions.

## AlphaGo, AlphaZero, and MuZero

The self-play line of DeepMind's Go and general-game programs constitutes the most striking achievement of deep reinforcement learning to date. AlphaGo of [Silver et al. 2016][research_silver_et_al_2016] combined supervised learning from human games with reinforcement learning via self-play and Monte Carlo tree search (MCTS) to defeat world champion Lee Sedol in March 2016.

The architecture used two neural networks. A policy network trained by supervised learning on human moves predicted human move distributions and was fine-tuned by policy gradient on self-play games. A value network trained on self-play games predicted the outcome from a given position. During gameplay, MCTS explored a search tree with the value network scoring leaf positions and the policy network providing prior probabilities for tree expansion.

AlphaGo Zero of [Silver et al. 2017][research_silver_et_al_2017] simplified the approach by eliminating human game data entirely and combining policy and value networks into a single dual-head network $f_\theta(s) = (p, v)$ that outputs a policy distribution and a value estimate. MCTS uses the PUCT selection rule

$$
a_t = \arg\max_a \left[Q(s_t, a) + c_{\text{puct}} \, p(a \mid s_t) \frac{\sqrt{\sum_b N(s_t, b)}}{1 + N(s_t, a)}\right]
\tag{25}
$$

with $Q(s, a)$ the mean action value from tree statistics, $p(a \mid s)$ the neural network policy prior, $N(s, a)$ the visit count, and $c_{\text{puct}}$ an exploration constant. The training loop alternates self-play games under the current network with MCTS, and network updates minimize the combined loss

$$
L(\theta) = (z - v_\theta(s))^2 - \boldsymbol{\pi}^\top \log \boldsymbol{p}_\theta(s) + c \|\theta\|^2
\tag{26}
$$

where $z \in \{-1, 0, +1\}$ is the game outcome, $\boldsymbol{\pi}$ is the MCTS-improved policy from search visit counts, and the final term is L2 regularization. The resulting agent exceeded the strength of AlphaGo Master and the earlier AlphaGo Lee Sedol version within 40 days of training on 4 TPUs.

AlphaZero of [Silver et al. 2018][research_silver_et_al_2018] extended the AlphaGo Zero algorithm to chess, shogi, and Go with a single training pipeline, achieving superhuman performance in all three games from scratch using only the game rules and the reward signal at terminal positions. AlphaZero demonstrated that the same algorithm suffices for a broad class of two-player zero-sum perfect-information games.

MuZero of [Schrittwieser et al. 2020][research_schrittwieser_et_al_2020] removed the assumption that the environment model is known. Three neural networks parameterize a learned model. A representation function $h_\theta(o_1, \ldots, o_t) = s^0$ encodes past observations into an internal state, a dynamics function $g_\theta(s^{k-1}, a^k) = (r^k, s^k)$ predicts the reward and next internal state given an action, and a prediction function $f_\theta(s^k) = (p^k, v^k)$ predicts policy and value from internal state. MCTS operates over the learned internal state space rather than the true environment. The MuZero training loss combines terms for observed reward, value, and policy at each unrolled step,

$$
L_t(\theta) = \sum_{k=0}^{K} \left[(r_{t+k} - r_\theta^k)^2 + (z_{t+k} - v_\theta^k)^2 - \boldsymbol{\pi}_{t+k}^\top \log \boldsymbol{p}_\theta^k\right] + c \|\theta\|^2
\tag{27}
$$

where $K$ is the number of unrolled steps and $z_{t+k}$ is the $n$-step or full-return target. MuZero achieved superhuman play in chess, shogi, and Go while also matching state-of-the-art on Atari, unifying the previously-distinct settings of board games and video games under a single algorithm.

The self-play line demonstrates the power of combining deep reinforcement learning, tree search, and self-generated training data. The success in board games has proved harder to replicate in domains without perfect information or with substantial stochasticity, though [Perolat et al. 2022][research_perolat_et_al_2022] Player of Games extended the paradigm to imperfect-information games including no-limit poker, and EfficientZero and Sampled MuZero variants extended to continuous control settings.

## Model-Based Deep Reinforcement Learning

Model-based deep reinforcement learning learns an internal model of environment dynamics and uses it for planning or value estimation. Article seven treats the topic at length, a brief survey positions the field's contemporary state.

World Models of [Ha and Schmidhuber 2018][research_ha_schmidhuber_2018] proposed learning a compressed latent-state representation via variational autoencoder, forward dynamics via mixture density recurrent networks in the latent space, and a compact policy in the latent space via policy gradient or evolution strategies. The framework demonstrated substantial sample efficiency gains on visual reinforcement learning benchmarks.

The Dreamer series extends latent-state world models with the Recurrent State Space Model and actor-critic learning entirely in imagination, progressively improving performance across visual control benchmarks. [Hafner et al. 2019][research_hafner_et_al_2019] Dreamer established the base algorithm, [Hafner et al. 2020][research_hafner_et_al_2020] DreamerV2 achieved competitive performance on Atari, and [Hafner et al. 2023][research_hafner_et_al_2023] DreamerV3 achieved competitive performance across a wide range of continuous control, discrete action, and video game domains with a single set of hyperparameters, providing evidence that model-based deep reinforcement learning has reached practical maturity.

MuZero and its extensions blur the distinction between model-based and model-free by learning implicit models that support MCTS planning without requiring the model to predict raw observations. EfficientZero of [Ye et al. 2021][research_ye_liu_kurutach_abbeel_gao_2021] extended MuZero with several modifications including self-supervised consistency losses and value prefix prediction, achieving comparable performance to MuZero with 100000 environment steps rather than millions. SimPLe of [Kaiser et al. 2019][research_kaiser_et_al_2019] provided an earlier demonstration that model-based Atari play with reasonable sample efficiency is feasible using deep video-prediction models.

The distinction between explicit generative models and implicit planning models has become substantially less sharp in the deep reinforcement learning era than the corresponding distinction in classical reinforcement learning.

## Multi-Agent Deep Reinforcement Learning

Multi-agent settings introduce non-stationarity from each agent's perspective, since other agents adapt in response to observed behavior. Classical algorithms based on single-agent MDP assumptions do not directly apply, and deep multi-agent reinforcement learning has developed specialized techniques.

Centralized training with decentralized execution provides a widely-used framework. During training, agents access global information for value estimation or actor updates, during execution, each agent conditions only on its local observations. MADDPG of [Lowe et al. 2017][research_lowe_et_al_2017] extends DDPG to multi-agent settings by training each agent's critic on the full joint action space while restricting the actor to local observations.

QMIX of [Rashid et al. 2018][research_rashid_et_al_2018] factors the joint value function as a monotonic mixture of per-agent utility functions,

$$
Q_{\text{tot}}(\boldsymbol{s}, \boldsymbol{a}) = f_{\text{mix}}(Q_1(s_1, a_1), \ldots, Q_n(s_n, a_n) ; \boldsymbol{s})
\tag{28}
$$

where the mixing network $f_{\text{mix}}$ has monotonically non-negative weights conditioning on the global state. The monotonicity constraint preserves individual-global maximum consistency,

$$
\arg\max_{\boldsymbol{a}} Q_{\text{tot}}(\boldsymbol{s}, \boldsymbol{a}) = (\arg\max_{a_1} Q_1(s_1, a_1), \ldots, \arg\max_{a_n} Q_n(s_n, a_n))
\tag{29}
$$

enabling decentralized greedy execution while maintaining a coherent joint value function during training. QTRAN of [Son et al. 2019][research_son_et_al_2019] and other successor methods relax the monotonicity constraint for greater expressiveness at the cost of more complex training.

Independent Q-learning treats each agent as facing an MDP with fixed other agents but suffers from the non-stationarity introduced by other agents' learning. QMIX, MADDPG, and their descendants attempt to mitigate this through joint-value factorization or centralized critics.

Self-play in zero-sum games has produced the strongest deep multi-agent RL results. AlphaStar of [Vinyals et al. 2019][research_vinyals_et_al_2019] combined a large population of self-play agents with a league training approach in StarCraft II, defeating professional players. OpenAI Five of [OpenAI et al. 2019a][research_openai_five_2019] used self-play combined with team play for Dota 2. Player of Games treated earlier extends self-play to imperfect-information settings.

Emergent communication and social dilemmas provide other important research directions in multi-agent RL, connecting to game theory, mechanism design, and cognitive science. Article eleven treats learning from other agents at greater length.

## Reinforcement Learning from Human Feedback

Reinforcement learning from human feedback has become the standard post-training mechanism for large language models. The approach originates in [Christiano et al. 2017][research_christiano_et_al_2017] preference-based reinforcement learning. Rather than requiring an engineered reward function, the algorithm learns a reward model from human comparisons of trajectory segments and optimizes policy against the learned reward via standard reinforcement learning (typically PPO).

[Stiennon et al. 2020][research_stiennon_et_al_2020] applied preference-based reinforcement learning to text summarization, demonstrating that RLHF-trained models produce summaries preferred to supervised-learning baselines by human evaluators. [Ouyang et al. 2022][research_ouyang_et_al_2022] InstructGPT extended the approach to general instruction-following, producing the modern RLHF template that underlies contemporary conversational assistants.

The standard RLHF pipeline proceeds in three stages. First, supervised fine-tuning on human demonstrations aligns the model with instruction-following behavior. Second, a reward model $R_\phi(x, y)$ is trained on human preference comparisons using the Bradley-Terry model,

$$
P(y_w \succ y_l \mid x) = \sigma(R_\phi(x, y_w) - R_\phi(x, y_l))
\tag{30}
$$

with the reward-model loss

$$
L^{\text{RM}}(\phi) = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}}\!\left[\log \sigma(R_\phi(x, y_w) - R_\phi(x, y_l))\right]
\tag{31}
$$

for preferred completion $y_w$ and dispreferred completion $y_l$. Third, PPO optimizes the policy against the learned reward model with a KL penalty against the supervised-fine-tuned model,

$$
L^{\text{RLHF}}(\theta) = \mathbb{E}_{x, y \sim \pi_\theta}\!\left[R(x, y)\right] - \beta \mathbb{E}_{x, y \sim \pi_\theta}\!\left[D_{\text{KL}}\!\left(\pi_\theta(y \mid x) \,\|\, \pi_{\text{SFT}}(y \mid x)\right)\right]
\tag{32}
$$

where $\pi_{\text{SFT}}$ is the supervised-fine-tuned reference model and $\beta$ is a KL penalty coefficient that prevents the policy from drifting too far from the reference.

Direct Preference Optimization of [Rafailov et al. 2023][research_rafailov_et_al_2023] eliminates the explicit reward model by deriving a closed-form loss that directly optimizes the policy against preference data. The DPO loss

$$
L^{\text{DPO}}(\theta) = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}}\!\left[\log \sigma\!\left(\beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{SFT}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{SFT}}(y_l \mid x)}\right)\right]
\tag{33}
$$

for preferred completion $y_w$ and dispreferred completion $y_l$ trades the standard reinforcement learning apparatus for a simpler supervised-learning-style optimization. DPO and its variants have become widely adopted for open-source language model post-training.

Constitutional AI of [Bai et al. 2022a][research_bai_et_al_2022a] Constitutional AI and reinforcement learning from AI feedback replace human preference labels with model-generated preferences guided by a set of natural-language principles, reducing the human-annotation cost while raising questions about circular training dynamics that article eleven treats in the broader preference-learning context. The [Bai et al. 2022b][research_bai_et_al_2022b] Anthropic helpful-and-harmless training-a-helpful-and-harmless-assistant paper provided detailed methodology for the RLHF pipeline that has become the standard reference. [Casper et al. 2023][research_casper_et_al_2023] surveys open problems and fundamental limitations of RLHF including reward hacking, mode collapse, and misgeneralization of learned reward models. The scope of this article limits treatment of the alignment aspects to the algorithmic apparatus, broader concerns are treated elsewhere in the series.

## Scaling and Compute

Deep reinforcement learning systems have scaled substantially in compute cost over the past decade. AlphaGo Zero trained on 4 TPUs for approximately 40 days. AlphaStar of [Vinyals et al. 2019][research_vinyals_et_al_2019] on StarCraft II used a large distributed training system involving thousands of concurrent games. OpenAI Five on Dota 2 used approximately 128000 CPU cores for training. The RLHF post-training of contemporary large language models involves clusters comparable to the pretraining setup.

Scaling laws for reinforcement learning have received recent attention. [Andrychowicz et al. 2021][research_andrychowicz_et_al_2021] characterized what matters in policy-gradient RL through a large-scale empirical study, identifying algorithmic details, network architecture, hyperparameter choices, and problem-factors that individually or collectively determine performance. [Hilton et al. 2023][research_hilton_et_al_2023] studied scaling laws for compute in single-agent reinforcement learning, finding that reinforcement learning shows compute-efficiency improvements comparable to supervised learning under appropriate parameterization. Their compute-efficiency law takes the approximate form

$$
\text{Score}(C) - \text{Score}_{\max} = -\alpha C^{-\beta}
\tag{34}
$$

for compute budget $C$ and constants $\alpha, \beta$ that depend on the domain, mirroring the power-law form observed in supervised learning scaling.

Practical scaling considerations include the choice of on-policy versus off-policy algorithms (off-policy generally scales better because it decouples data collection from optimization), the choice of synchronous versus asynchronous distributed training, the tradeoff between environment throughput and gradient throughput, and hyperparameter sensitivity at scale. The engineering complexity of contemporary deep reinforcement learning systems approaches that of large-scale supervised learning training pipelines.

Hyperparameter sensitivity remains a notorious feature of deep reinforcement learning. Learning rates, batch sizes, network architectures, replay buffer sizes, target network update frequencies, and exploration schedules all substantially affect final performance, and the sensitivity often extends to seemingly minor implementation details.

## Sim-to-Real Transfer

Deep reinforcement learning policies trained in simulation frequently fail to transfer to physical systems without additional engineering. The sim-to-real gap encompasses several distinct phenomena, including differences in dynamics between simulator and reality, differences in observation modalities and noise characteristics, differences in reward signal fidelity, and unmodeled environmental factors.

Domain randomization of [Tobin et al. 2017][research_tobin_et_al_2017] trains policies on randomized simulator parameters (visual textures, physical properties, sensor noise, actuator delays) so that reality falls within the training distribution. The policy learns to be robust to the randomized variations and transfers to reality without additional adaptation. The subsequent [Peng et al. 2018][research_peng_andrychowicz_zaremba_abbeel_2018] paper extended the approach to dynamics randomization for physical robot manipulation.

System identification uses real-world data to estimate simulator parameters, adapting the simulator to reality rather than the policy. Combined approaches interleave simulation training with real-world calibration and progressively narrow the sim-to-real gap.

Learning from demonstration provides an alternative to pure reinforcement learning. Real-world demonstrations, either from humans or from teleoperated systems, initialize policies that reinforcement learning then refines. Article eleven treats learning from demonstration systematically.

The dexterous manipulation results of [OpenAI et al 2019 Dactyl][research_openai_dactyl_2019] achieved sim-to-real transfer for in-hand manipulation of a Rubik's cube using extensive domain randomization combined with automatic domain randomization that adaptively expands the randomization ranges as the policy improves. RGB-based robotic manipulation benchmarks including RoboSuite and Meta-World provide standardized settings for sim-to-real research.

The extent to which sim-to-real transfer succeeds remains a matter of considerable practical engineering effort. Article thirteen on embodied cognition and developmental robotics returns to related themes from a different angle.

## Reproducibility and Empirical Challenges

The reproducibility challenges of deep reinforcement learning have been documented at length. [Henderson et al. 2018][research_henderson_et_al_2018] showed that deep RL results are frequently more variable across random seeds and implementations than reported summary statistics suggest, with substantially different conclusions possible from different seed subsets of the same algorithm on the same benchmark.

[Andrychowicz et al. 2021][research_andrychowicz_et_al_2021] provided the largest empirical study of what matters in policy-gradient RL to date, systematically varying 22 factors across 5 different algorithms on standard benchmarks. Their conclusions include that many algorithmic choices interact strongly with hyperparameters, that reported algorithmic advantages are often smaller than or comparable to hyperparameter-choice effects, and that reproducibility requires careful controls over implementation details.

[Engstrom et al. 2020][research_engstrom_et_al_2020] performed a detailed ablation of PPO implementations and identified that a substantial fraction of PPO's advantage over TRPO comes from implementation-level details (Adam optimizer, learning-rate annealing, orthogonal initialization, observation normalization, value function clipping, generalized advantage estimation) rather than the clipping mechanism per se.

Contemporary best-practice guidelines include running experiments with at least 10 random seeds per configuration, reporting median performance and interquartile range or bootstrap confidence intervals rather than only mean and standard error, providing full hyperparameter specifications and code, and evaluating on multiple benchmark suites to check generalization of algorithmic improvements. Open-source reference implementations including Stable Baselines3, CleanRL, and RLlib support reproducibility efforts by providing standardized algorithm implementations.

The [Agarwal et al. 2021][research_agarwal_et_al_2021] deep reinforcement learning statistical practice paper proposed the interquartile mean and stratified bootstrap confidence intervals as more informative summary statistics than the standard mean-and-median reporting. The [Colas et al. 2018][research_colas_sigaud_oudeyer_2018] and [Colas et al. 2019][research_colas_sigaud_oudeyer_2019] papers argued for statistically-grounded seed budget planning in deep reinforcement learning. The rlberry and rliable Python packages support these statistical practices.

## Empirical Benchmark Landscape

The empirical landscape of deep reinforcement learning has evolved substantially. The original Atari 57 benchmark of [Bellemare et al. 2013][research_bellemare_naddaf_veness_bowling_2013] remains a canonical discrete-action visual benchmark, extended by the Atari 100k benchmark that emphasizes sample efficiency by restricting learning to 100000 environment steps.

Continuous control benchmarks include the MuJoCo suite of [Todorov et al. 2012][research_todorov_erez_tassa_2012], the DeepMind Control Suite of [Tassa et al. 2018][research_tassa_et_al_2018], and their GPU-parallelized successors including Isaac Gym. Robotic manipulation benchmarks include Meta-World, RoboSuite, and RLBench.

Generalization benchmarks including Procgen of [Cobbe et al. 2019][research_cobbe_et_al_2019] and NetHack of [Küttler et al. 2020][research_kuttler_et_al_2020] emphasize procedural generation to prevent memorization and test out-of-distribution generalization.

Behavior suite for reinforcement learning of [Osband et al. 2020][research_osband_et_al_2020] provides a diagnostic set of simple tasks that isolate reinforcement learning capabilities (exploration, generalization, memory, credit assignment) for controlled algorithmic comparison.

Complex-multi-agent strategy game benchmarks including StarCraft II and Dota 2 have provided challenge problems that stressed the field's capabilities. AlphaStar and OpenAI Five demonstrated deep reinforcement learning agents competitive with top human players in these games, though the systems required substantial engineering effort and compute investment beyond what typical deep RL benchmarks admit.

## Neuroscience Connections

The neuroscience connections of deep reinforcement learning are more complex than those of the classical apparatus treated in article three. Deep neural networks provide potentially closer models of biological neural systems than tabular or linear function approximation, and the learned representations of deep RL agents show some alignment with neural representations in the primate visual cortex.

[Cadieu et al. 2014][research_cadieu_et_al_2014] and [Yamins and DiCarlo 2016][research_yamins_dicarlo_2016] documented that supervised-trained convolutional networks produce internal representations that predict responses of neurons in inferior temporal cortex on unseen images better than any hand-designed feature representation. The finding suggests that convolutional architectures capture something important about the visual system's computation. Whether similar alignment holds for the value and policy representations learned by deep RL agents remains an active research area.

Deep predictive coding models of [Rao and Ballard 1999][research_rao_ballard_1999] and their successors provide neuroscience-inspired architectures that learn latent-state representations by predicting sensory inputs. These models connect to model-based deep reinforcement learning through their shared reliance on prediction as a training signal. Article seven treats predictive coding at length.

The prefrontal cortex has been interpreted as implementing meta-reinforcement learning by [Wang et al. 2018][research_wang_et_al_2018], with recurrent activity supporting fast adaptation across tasks while slower dopaminergic updates train the recurrent weights themselves. [Botvinick 2020][research_botvinick_et_al_2020] surveyed the broader implications of deep reinforcement learning insights for neuroscience. The Tolman-Eichenbaum machine of [Whittington et al. 2020][research_whittington_et_al_2020] proposes a unified computational model that links spatial navigation, memory, and reinforcement learning through generalization mechanisms in the hippocampal formation. Article fourteen treats the NeuroAI bridge at length.

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

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 34 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 34, 33 are established and 1 are bespoke.
Losses and objectives are expectations over sampled transitions or trajectories, returns and values carry the units of the reward signal, and coefficients such as the discount factor, the clipping range and the entropy temperature are dimensionless hyperparameters whose values differ between the papers cited.

**Equation 1, Deep Q-Network Loss.**
The deep Q-network minimises the squared difference between its action value and a bootstrapped target computed with a slowly updated target network over transitions drawn from a replay buffer.
[Mnih et al. 2015][research_mnih_et_al_2015]

$$
L(\theta) = \mathbb{E}_{(s, a, r, s') \sim \mathcal{D}}\!\left[\left(r + \gamma \max_{a'} Q_{\theta^{-}}(s', a') - Q_\theta(s, a)\right)^2\right]
\tag{1}
$$

**Equation 2, Double Deep Q-Network Target.**
The online network selects the next action and the target network evaluates it, which reduces overestimation bias.
[van Hasselt et al. 2016][research_van_hasselt_guez_silver_2016]

$$
y_t = r_{t+1} + \gamma Q_{\theta^{-}}(s_{t+1}, \arg\max_{a'} Q_\theta(s_{t+1}, a'))
\tag{2}
$$

**Equation 3, Dueling Network Aggregation.**
The action value is assembled from a state value stream and an advantage stream whose mean is subtracted so that the two are identifiable.
[Wang et al. 2016][research_wang_et_al_2016]

$$
Q_\theta(s, a) = V_\theta(s) + \left(A_\theta(s, a) - \frac{1}{|\mathcal{A}|} \sum_{a'} A_\theta(s, a')\right)
\tag{3}
$$

**Equation 4, Prioritised Replay Sampling Probability.**
A transition is sampled with probability proportional to its priority raised to an exponent that sets the strength of prioritisation.
[Schaul et al. 2015][research_schaul_et_al_2016]

$$
P(i) = \frac{p_i^\alpha}{\sum_j p_j^\alpha}
\tag{4}
$$

**Equation 5, Prioritised Replay Importance Weights.**
Each sampled transition's gradient is weighted by the inverse of its sampling probability relative to uniform, raised to an annealed exponent.
[Schaul et al. 2015][research_schaul_et_al_2016]

$$
w_i = \left(\frac{1}{N \cdot P(i)}\right)^\beta
\tag{5}
$$

**Equation 6, Noisy Linear Layer.**
Each weight and bias is a learned mean plus a learned scale times sampled noise, which gives state-dependent exploration.
[Fortunato et al. 2018][research_fortunato_et_al_2018]

$$
y = (W_\mu + W_\sigma \odot \epsilon_W) x + (b_\mu + b_\sigma \odot \epsilon_b)
\tag{6}
$$

**Equation 7, Categorical Distributional Loss.**
The categorical algorithm minimises the Kullback-Leibler divergence from the projected distributional Bellman target to the predicted return distribution.
[Bellemare et al. 2017][research_bellemare_dabney_munos_2017]

$$
L(\theta) = \mathbb{E}_{(s, a, r, s')}\!\left[D_{\text{KL}}\!\left(\Phi \mathcal{T} Z_{\theta^{-}}(s', a^*) \,\|\, Z_\theta(s, a)\right)\right]
\tag{7}
$$

**Equation 8, Quantile Regression Loss.**
Quantile regression fits each output to its quantile level by an asymmetric loss summed over pairs of predicted and target quantiles.
[Dabney et al. 2018a][research_dabney_rowland_bellemare_munos_2018]

$$
L^{\text{QR}}(\theta) = \sum_i \sum_j \mathbb{E}\!\left[\rho_{\tau_i}(y_j - Z^i_\theta(s, a))\right]
\tag{8}
$$

**Equation 9, Implicit Quantile Function.**
Implicit quantile networks output the return quantile at any sampled level from a state encoding combined with an embedding of that level.
[Dabney et al. 2018b][research_dabney_ostrovski_silver_munos_2018]

$$
Z_\tau(s, a) = f_\theta(\psi(s), \phi(\tau))_a
\tag{9}
$$

**Equation 10, Belief State.**
The belief state is the posterior probability of each hidden state given the history of observations and actions.

$$
b_t(s) = P(s_t = s \mid o_{1:t}, a_{1:t-1})
\tag{10}
$$

**Equation 11, Self-Predictive Representation Loss.**
The encoder and a latent transition model are trained to predict projected future latent states, with gradients stopped through the target.
[Schwarzer et al. 2021][research_schwarzer_et_al_2021]

$$
L_{\text{SPR}}(\theta) = \sum_k \left\| f_{\text{proj}}(g_\theta(\phi_\theta(s_t), a_{t:t+k-1})) - \text{sg}\!\left(f_{\text{proj}}(\phi_\theta(s_{t+k}))\right) \right\|^2
\tag{11}
$$

**Equation 12, Trust-Region Policy Optimisation Problem.**
Trust-region policy optimisation maximises an importance-weighted advantage surrogate subject to a bound on the mean Kullback-Leibler divergence from the old policy.
[Schulman et al. 2015][research_schulman_levine_moritz_jordan_abbeel_2015]

$$
\max_\theta \; \mathbb{E}_{s, a \sim \pi_{\theta_{\text{old}}}}\!\left[\frac{\pi_\theta(a \mid s)}{\pi_{\theta_{\text{old}}}(a \mid s)} A^{\pi_{\theta_{\text{old}}}}(s, a)\right] \quad \text{subject to} \quad \mathbb{E}_{s}\!\left[D_{\text{KL}}(\pi_{\theta_{\text{old}}}(\cdot \mid s) \,\|\, \pi_\theta(\cdot \mid s))\right] \leq \delta
\tag{12}
$$

**Equation 13, Clipped Surrogate Objective.**
Proximal policy optimisation takes the smaller of the ratio-weighted advantage and its clipped counterpart, which removes the incentive to move the ratio outside a band around one.
[Schulman et al. 2017][research_schulman_wolski_dhariwal_radford_klimov_2017]

$$
L^{\text{CLIP}}(\theta) = \mathbb{E}_t\!\left[\min\!\left(r_t(\theta) \hat{A}_t, \; \text{clip}(r_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A}_t\right)\right]
\tag{13}
$$

**Equation 14, Combined Proximal Policy Optimisation Objective.**
The full objective adds a value regression penalty and an entropy bonus to the clipped surrogate.
[Schulman et al. 2017][research_schulman_wolski_dhariwal_radford_klimov_2017]

$$
L^{\text{PPO}}(\theta) = L^{\text{CLIP}}(\theta) - c_1 \mathbb{E}_t\!\left[(V_\theta(s_t) - V_t^{\text{target}})^2\right] + c_2 \mathbb{E}_t\!\left[H(\pi_\theta(\cdot \mid s_t))\right]
\tag{14}
$$

**Equation 15, V-Trace Target.**
V-trace corrects the value estimate by temporal-difference errors weighted with truncated importance ratios, which tolerates lag between actor and learner policies.
[Espeholt et al. 2018][research_espeholt_et_al_2018]

$$
v_t = V(s_t) + \sum_{k=t}^{t+n-1} \gamma^{k-t} \left(\prod_{j=t}^{k-1} c_j\right) \rho_k (r_{k+1} + \gamma V(s_{k+1}) - V(s_k))
\tag{15}
$$

**Equation 16, Deep Deterministic Policy Gradient.**
The actor is updated by chaining its Jacobian with the action gradient of the learned critic at the action it outputs.
[Lillicrap et al. 2015][research_lillicrap_et_al_2016]

$$
\nabla_\theta J(\theta) = \mathbb{E}_{s \sim d^\mu}\!\left[\nabla_\theta \mu_\theta(s) \nabla_a Q_w(s, a)|_{a = \mu_\theta(s)}\right]
\tag{16}
$$

**Equation 17, Twin Delayed Target with Policy Smoothing.**
The target takes the minimum of two target critics evaluated at a target action perturbed by clipped Gaussian noise.
[Fujimoto et al. 2018][research_fujimoto_hoof_meger_2018]

$$
y = r + \gamma \min_{i \in \{1, 2\}} Q_{w_i^{-}}(s', \tilde{a}), \quad \tilde{a} = \mu_{\theta^{-}}(s') + \epsilon
\tag{17}
$$

**Equation 18, Maximum-Entropy Objective.**
Soft actor-critic maximises the discounted sum of reward plus a temperature times the entropy of the policy at each state.
[Haarnoja et al. 2018][research_haarnoja_zhou_abbeel_levine_2018]

$$
J_{\text{SAC}}(\pi) = \mathbb{E}\!\left[\sum_{t=0}^{\infty} \gamma^t \left(r_{t+1} + \alpha H(\pi(\cdot \mid s_t))\right)\right]
\tag{18}
$$

**Equation 19, Soft State Value.**
The soft state value is the expected action value less the temperature times the log probability of the action.
[Haarnoja et al. 2018][research_haarnoja_zhou_abbeel_levine_2018]

$$
V^\pi(s) = \mathbb{E}_{a \sim \pi}\!\left[Q^\pi(s, a) - \alpha \log \pi(a \mid s)\right]
\tag{19}
$$

**Equation 20, Soft Bellman Equation for Action Values.**
The soft action value is the expected reward plus the discounted soft value of the successor state.
[Haarnoja et al. 2018][research_haarnoja_zhou_abbeel_levine_2018]

$$
Q^\pi(s, a) = \mathbb{E}_{s'}\!\left[r + \gamma V^\pi(s')\right]
\tag{20}
$$

**Equation 21, Reparameterised Gaussian Action.**
The action is a deterministic function of the state and independent standard normal noise, so gradients can pass through the sample.

$$
a = \mu_\theta(s) + \sigma_\theta(s) \odot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)
\tag{21}
$$

**Equation 22, Automatic Entropy Temperature Loss.**
The temperature is adjusted by gradient descent so that the policy entropy is driven toward a target value.

$$
L(\alpha) = -\alpha \mathbb{E}\!\left[\log \pi_\theta(a \mid s) + \bar{H}\right]
\tag{22}
$$

**Equation 23, Soft Polyak Target Network Update.**
The target network parameters move a small fraction $\tau$ of the way toward the online parameters at each step.

$$
\theta^{-} \leftarrow \tau \theta + (1 - \tau) \theta^{-}
\tag{23}
$$

**Equation 24, Decision Transformer Factorisation.**
Decision Transformer models each action autoregressively given a recent window of states, actions and returns-to-go.
[Chen et al. 2021][research_chen_et_al_2021]

$$
P(\tau) = \prod_t P(a_t \mid s_{t-K:t}, a_{t-K:t-1}, \hat{R}_{t-K:t})
\tag{24}
$$

**Equation 25, Predictor Upper Confidence Tree Selection Rule.**
Tree search selects the action maximising the mean value plus a bonus proportional to the network prior and to the square root of the parent visit count over one plus the action visit count.
[Silver et al. 2017][research_silver_et_al_2017]

$$
a_t = \arg\max_a \left[Q(s_t, a) + c_{\text{puct}} \, p(a \mid s_t) \frac{\sqrt{\sum_b N(s_t, b)}}{1 + N(s_t, a)}\right]
\tag{25}
$$

**Equation 26, AlphaGo Zero Training Loss.**
The dual-head network minimises the squared error of its value against the game outcome, the cross-entropy of its policy against the search policy and a weight penalty.
[Silver et al. 2017][research_silver_et_al_2017]

$$
L(\theta) = (z - v_\theta(s))^2 - \boldsymbol{\pi}^\top \log \boldsymbol{p}_\theta(s) + c \|\theta\|^2
\tag{26}
$$

**Equation 27, MuZero Training Loss.**
MuZero sums over unrolled model steps the reward, value and policy errors of its learned model, plus a weight penalty.
[Schrittwieser et al. 2020][research_schrittwieser_et_al_2020]

$$
L_t(\theta) = \sum_{k=0}^{K} \left[(r_{t+k} - r_\theta^k)^2 + (z_{t+k} - v_\theta^k)^2 - \boldsymbol{\pi}_{t+k}^\top \log \boldsymbol{p}_\theta^k\right] + c \|\theta\|^2
\tag{27}
$$

**Equation 28, Monotonic Value Mixing.**
QMIX writes the joint action value as a state-conditioned mixing of the per-agent utilities with non-negative weights.
[Rashid et al. 2018][research_rashid_et_al_2018]

$$
Q_{\text{tot}}(\boldsymbol{s}, \boldsymbol{a}) = f_{\text{mix}}(Q_1(s_1, a_1), \ldots, Q_n(s_n, a_n) ; \boldsymbol{s})
\tag{28}
$$

**Equation 29, Individual-Global Maximum Consistency.**
Monotonic mixing guarantees that the joint greedy action is the tuple of each agent's individually greedy action.
[Rashid et al. 2018][research_rashid_et_al_2018]

$$
\arg\max_{\boldsymbol{a}} Q_{\text{tot}}(\boldsymbol{s}, \boldsymbol{a}) = (\arg\max_{a_1} Q_1(s_1, a_1), \ldots, \arg\max_{a_n} Q_n(s_n, a_n))
\tag{29}
$$

**Equation 30, Bradley-Terry Preference Model.**
The probability that one completion is preferred to another is the logistic function of the difference in their learned rewards.

$$
P(y_w \succ y_l \mid x) = \sigma(R_\phi(x, y_w) - R_\phi(x, y_l))
\tag{30}
$$

**Equation 31, Reward Model Loss.**
The reward model minimises the negative log likelihood of the observed preferences under the Bradley-Terry model.

$$
L^{\text{RM}}(\phi) = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}}\!\left[\log \sigma(R_\phi(x, y_w) - R_\phi(x, y_l))\right]
\tag{31}
$$

**Equation 32, Kullback-Leibler Regularised Fine-Tuning Objective.**
Reinforcement learning from human feedback, abbreviated RLHF, maximises the learned reward less a multiple of the divergence from the supervised reference model.

$$
L^{\text{RLHF}}(\theta) = \mathbb{E}_{x, y \sim \pi_\theta}\!\left[R(x, y)\right] - \beta \mathbb{E}_{x, y \sim \pi_\theta}\!\left[D_{\text{KL}}\!\left(\pi_\theta(y \mid x) \,\|\, \pi_{\text{SFT}}(y \mid x)\right)\right]
\tag{32}
$$

**Equation 33, Direct Preference Optimisation Loss.**
Direct preference optimisation fits the Bradley-Terry model with the reward replaced by the scaled log ratio of policy to reference probabilities.
[Rafailov et al. 2023][research_rafailov_et_al_2023]

$$
L^{\text{DPO}}(\theta) = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}}\!\left[\log \sigma\!\left(\beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{SFT}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{SFT}}(y_l \mid x)}\right)\right]
\tag{33}
$$

*Equation 34, Bespoke Saturating Power Law of Score Against Compute.*
The article summarises reinforcement learning compute scaling as a score approaching a ceiling with a power-law deficit in compute, a form it states as approximate and whose constants depend on the domain.
[Hilton et al. 2023][research_hilton_et_al_2023]

$$
\text{Score}(C) - \text{Score}_{\max} = -\alpha C^{-\beta}
\tag{34}
$$

### Notation

- $\theta^{-}$, the target network parameters
- $\mathcal{D}$, the experience replay buffer or preference dataset
- $Q_\theta(s, a)$, the action value estimated by the online network
- $p_i$, the replay priority of transition $i$, its absolute temporal-difference error plus a small constant
- $\beta$, the importance-weight annealing exponent in equation 5, the divergence penalty coefficient in equations 32 and 33 and a fitted exponent in equation 34
- $\alpha$, the prioritisation exponent in equation 4, the entropy temperature in equations 18 to 22 and a fitted constant in equation 34
- $\rho_{\tau_i}$, the quantile regression loss at level $\tau_i$
- $b_t(s)$, the belief state, a probability distribution over hidden states at step $t$
- $r_t(\theta)$, the ratio of new to old policy probability for the action taken
- $\hat{A}_t$, the advantage estimate at step $t$
- $c_j$, a truncated importance ratio in V-trace, with $\rho_k$ the other
- $\mu_\theta(s)$, the deterministic actor or the mean of the Gaussian policy
- $\bar{H}$, the target entropy
- $\hat{R}_{t-K:t}$, the returns-to-go over the context window
- $c_{\text{puct}}$, the exploration constant of tree search
- $\boldsymbol{\pi}$, the search policy derived from visit counts
- $Q_{\text{tot}}$, the joint action value of all agents
- $R_\phi(x, y_w)$, the learned reward of the preferred completion to a prompt
- $\pi_{\text{SFT}}$, the supervised fine-tuned reference model
- $C$, the compute budget in equation 34

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- LeCun, Yann, Yoshua Bengio, and Geoffrey Hinton. 2015. "Deep Learning." *Nature* 521 (7553): 436–44. [https://doi.org/10.1038/nature14539][research_lecun_bengio_hinton_2015]
- Mnih, Volodymyr, Koray Kavukcuoglu, David Silver, et al. 2015. "Human-Level Control through Deep Reinforcement Learning." *Nature* 518 (7540): 529–33. [https://doi.org/10.1038/nature14236][research_mnih_et_al_2015]
- Peng, Xue Bin, Marcin Andrychowicz, Wojciech Zaremba, and Pieter Abbeel. 2018. "Sim-to-Real Transfer of Robotic Control with Dynamics Randomization." In *2018 IEEE International Conference on Robotics and Automation (ICRA)*. IEEE. [https://doi.org/10.1109/icra.2018.8460528][research_peng_andrychowicz_zaremba_abbeel_2018]
- Schrittwieser, Julian, Ioannis Antonoglou, Thomas Hubert, et al. 2020. "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model." *Nature* 588 (7839): 604–9. [https://doi.org/10.1038/s41586-020-03051-4][research_schrittwieser_et_al_2020]
- Silver, David, Aja Huang, Chris J. Maddison, et al. 2016. "Mastering the Game of Go with Deep Neural Networks and Tree Search." *Nature* 529 (7587): 484–89. [https://doi.org/10.1038/nature16961][research_silver_et_al_2016]
- Silver, David, Julian Schrittwieser, Karen Simonyan, et al. 2017. "Mastering the Game of Go without Human Knowledge." *Nature* 550 (7676): 354–59. [https://doi.org/10.1038/nature24270][research_silver_et_al_2017]
- Vinyals, Oriol, Igor Babuschkin, Wojciech M. Czarnecki, et al. 2019. "Grandmaster Level in StarCraft II Using Multi-Agent Reinforcement Learning." *Nature* 575 (7782): 350–54. [https://doi.org/10.1038/s41586-019-1724-z][research_vinyals_et_al_2019]
- Wang, Jane X., Zeb Kurth-Nelson, Dharshan Kumaran, et al. 2018. "Prefrontal Cortex as a Meta-Reinforcement Learning System." *Nature Neuroscience* 21 (6): 860–68. [https://doi.org/10.1038/s41593-018-0147-8][research_wang_et_al_2018]
- Whittington, James C. R., Timothy H. Muller, Shirley Mark, et al. 2020. "The Tolman-Eichenbaum Machine: Unifying Space and Relational Memory through Generalization in the Hippocampal Formation." *Cell* 183 (5): 1249-1263.e23. [https://doi.org/10.1016/j.cell.2020.10.024][research_whittington_et_al_2020]
- Yamins, Daniel L. K., and James J. DiCarlo. 2016. "Using Goal-Driven Deep Learning Models to Understand Sensory Cortex." *Nature Neuroscience* 19 (3): 356–65. [https://doi.org/10.1038/nn.4244][research_yamins_dicarlo_2016]

### Primary Sources, Non-Peer-Reviewed

- Adaptive Agent Team, Jakob Bauer, Kate Baumli, et al. 2023. "Human-Timescale Adaptation in an Open-Ended Task Space." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2301.07608][research_bauer_et_al_2023]
- Agarwal, Rishabh, Max Schwarzer, Pablo Samuel Castro, Aaron Courville, and Marc Bellemare. 2021. "Deep Reinforcement Learning at the Edge of the Statistical Precipice." *Advances in Neural Information Processing Systems* 34: 29304–20. [https://papers.nips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html][research_agarwal_et_al_2021]
- Andrychowicz, Marcin, Anton Raichuk, Piotr Stańczyk, et al. 2021. "What Matters for on-Policy Deep Actor-Critic Methods? A Large-Scale Study." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=nIAxjsniDzg][research_andrychowicz_et_al_2021]
- Bai, Yuntao, Andy Jones, Kamal Ndousse, et al. 2022b. "Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2204.05862][research_bai_et_al_2022b]
- Bai, Yuntao, Saurav Kadavath, Sandipan Kundu, et al. 2022a. "Constitutional AI: Harmlessness from AI Feedback." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2212.08073][research_bai_et_al_2022a]
- Baker, Bowen, Ilge Akkaya, Peter Zhokov, et al. 2022. "Video PreTraining (VPT): Learning to Act by Watching Unlabeled Online Videos." In *Advances in Neural Information Processing Systems 35*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/068431-1789][research_baker_et_al_2022]
- Bellemare, Marc G., Will Dabney, and Rémi Munos. 2017. "A Distributional Perspective on Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v70/bellemare17a.html][research_bellemare_dabney_munos_2017]
- Bellemare, M. G., Y. Naddaf, J. Veness, and M. Bowling. 2013. "The Arcade Learning Environment: An Evaluation Platform for General Agents." *Journal of Artificial Intelligence Research* 47: 253–79. [https://doi.org/10.1613/jair.3912][research_bellemare_naddaf_veness_bowling_2013]
- Cadieu, Charles F., Ha Hong, Daniel L. K. Yamins, et al. 2014. "Deep Neural Networks Rival the Representation of Primate IT Cortex for Core Visual Object Recognition." *PLoS Computational Biology* 10 (12): e1003963. [https://doi.org/10.1371/journal.pcbi.1003963][research_cadieu_et_al_2014]
- Casper, Stephen, Xander Davies, Claudia Shi, et al. 2023. "Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2307.15217][research_casper_et_al_2023]
- Chen, Lili, Kevin Lu, Aravind Rajeswaran, et al. 2021. "Decision Transformer: Reinforcement Learning via Sequence Modeling." *Advances in Neural Information Processing Systems* 34: 15084–97. [https://papers.nips.cc/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html][research_chen_et_al_2021]
- Christiano, Paul F., Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. 2017. "Deep Reinforcement Learning from Human Preferences." *Advances in Neural Information Processing Systems* 30. [https://papers.nips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html][research_christiano_et_al_2017]
- Cobbe, Karl, Christopher Hesse, Jacob Hilton, and John Schulman. 2019. "Leveraging Procedural Generation to Benchmark Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1912.01588][research_cobbe_et_al_2019]
- Colas, Cédric, Olivier Sigaud, and Pierre-Yves Oudeyer. 2018. "How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1806.08295][research_colas_sigaud_oudeyer_2018]
- Colas, Cédric, Olivier Sigaud, and Pierre-Yves Oudeyer. 2019. "A Hitchhiker's Guide to Statistical Comparisons of Reinforcement Learning Algorithms." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1904.06979][research_colas_sigaud_oudeyer_2019]
- Dabney, Will, Georg Ostrovski, David Silver, and Remi Munos. 2018b. "Implicit Quantile Networks for Distributional Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v80/dabney18a.html][research_dabney_ostrovski_silver_munos_2018]
- Dabney, Will, Mark Rowland, Marc Bellemare, and Rémi Munos. 2018a. "Distributional Reinforcement Learning with Quantile Regression." *Proceedings of the AAAI Conference on Artificial Intelligence* 32 (1). [https://doi.org/10.1609/aaai.v32i1.11791][research_dabney_rowland_bellemare_munos_2018]
- Engstrom, Logan, Andrew Ilyas, Shibani Santurkar, et al. 2020. "Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2005.12729][research_engstrom_et_al_2020]
- Espeholt, Lasse, Hubert Soyer, Remi Munos, et al. 2018. "IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v80/espeholt18a.html][research_espeholt_et_al_2018]
- Fortunato, Meire, Mohammad Gheshlaghi Azar, Bilal Piot, et al. 2018. "Noisy Networks for Exploration." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=rywHCPkAW][research_fortunato_et_al_2018]
- Fujimoto, Scott, Herke Hoof, and David Meger. 2018. "Addressing Function Approximation Error in Actor-Critic Methods." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v80/fujimoto18a.html][research_fujimoto_hoof_meger_2018]
- Ha, David, and Jürgen Schmidhuber. 2018. "Recurrent World Models Facilitate Policy Evolution." *Advances in Neural Information Processing Systems* 31. [https://papers.nips.cc/paper/2018/hash/2de5d16682c3c35007e4e92982f1a2ba-Abstract.html][research_ha_schmidhuber_2018]
- Haarnoja, Tuomas, Aurick Zhou, Pieter Abbeel, and Sergey Levine. 2018. "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v80/haarnoja18b.html][research_haarnoja_zhou_abbeel_levine_2018]
- Hafner, Danijar, Timothy Lillicrap, Ian Fischer, et al. 2019. "Learning Latent Dynamics for Planning from Pixels." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v97/hafner19a.html][research_hafner_et_al_2019]
- Hafner, Danijar, Timothy P. Lillicrap, Mohammad Norouzi, and Jimmy Ba. 2020. "Mastering Atari with Discrete World Models." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=0oabwyZbOu][research_hafner_et_al_2020]
- Hafner, Danijar, Jurgis Pasukonis, Jimmy Ba, and Timothy Lillicrap. 2023. "Mastering Diverse Domains through World Models." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2301.04104][research_hafner_et_al_2023]
- Hausknecht, Matthew, and Peter Stone. 2015. "Deep Recurrent Q-Learning for Partially Observable MDPs." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1507.06527][research_hausknecht_stone_2015]
- Henderson, Peter, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup, and David Meger. 2018. "Deep Reinforcement Learning That Matters." *Proceedings of the AAAI Conference on Artificial Intelligence* 32 (1). [https://doi.org/10.1609/aaai.v32i1.11694][research_henderson_et_al_2018]
- Hessel, Matteo, Joseph Modayil, Hado Van Hasselt, et al. 2018. "Rainbow: Combining Improvements in Deep Reinforcement Learning." *Proceedings of the AAAI Conference on Artificial Intelligence* 32 (1). [https://doi.org/10.1609/aaai.v32i1.11796][research_hessel_et_al_2018]
- Hilton, Jacob, Jie Tang, and John Schulman. 2023. "Scaling Laws for Single-Agent Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2301.13442][research_hilton_et_al_2023]
- Jaderberg, Max, Volodymyr Mnih, Wojciech Marian Czarnecki, et al. 2017. "Reinforcement Learning with Unsupervised Auxiliary Tasks." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=SJ6yPD5xg][research_jaderberg_et_al_2017]
- Janner, Michael, Qiyang Li, and Sergey Levine. 2021. "Offline Reinforcement Learning as One Big Sequence Modeling Problem." In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2021/hash/099fe6b0b444c23836c4a5d07346082b-Abstract.html][research_janner_li_levine_2021]
- Kaiser, Lukasz, Mohammad Babaeizadeh, Piotr Milos, et al. 2019. "Model-Based Reinforcement Learning for Atari." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1903.00374][research_kaiser_et_al_2019]
- Kapturowski, Steven, Georg Ostrovski, John Quan, Remi Munos, and Will Dabney. 2019. "Recurrent Experience Replay in Distributed Reinforcement Learning." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=r1lyTjAqYX][research_kapturowski_et_al_2019]
- Kostrikov, Ilya, Denis Yarats, and Rob Fergus. 2020. "Image Augmentation Is All You Need: Regularizing Deep Reinforcement Learning from Pixels." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2004.13649][research_kostrikov_yarats_fergus_2020]
- Küttler, Heinrich, Nantas Nardelli, Alexander Miller, et al. 2020. "The NetHack Learning Environment." *Advances in Neural Information Processing Systems* 33: 7671–84. [https://papers.nips.cc/paper/2020/hash/569ff987c643b4bedf504efda8f786c2-Abstract.html][research_kuttler_et_al_2020]
- Laskin, Michael, Aravind Srinivas, and Pieter Abbeel. 2020. "CURL: Contrastive Unsupervised Representations for Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v119/laskin20a.html][research_laskin_srinivas_abbeel_2020]
- Lillicrap, Timothy P., Jonathan J. Hunt, Alexander Pritzel, et al. 2015. "Continuous Control with Deep Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1509.02971][research_lillicrap_et_al_2016]
- Lowe, Ryan, Yi Wu, Aviv Tamar, Jean Harb, OpenAI Pieter Abbeel, and Igor Mordatch. 2017. "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments." *Advances in Neural Information Processing Systems* 30. [https://papers.nips.cc/paper/2017/hash/68a9750337a418a86fe06c1991a1d64c-Abstract.html][research_lowe_et_al_2017]
- Mnih, Volodymyr, Adria Puigdomenech Badia, Mehdi Mirza, et al. 2016. "Asynchronous Methods for Deep Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v48/mniha16.html][research_mnih_et_al_2016]
- Mnih, Volodymyr, Koray Kavukcuoglu, David Silver, et al. 2013. "Playing Atari with Deep Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1312.5602][research_mnih_et_al_2013]
- OpenAI, Ilge Akkaya, Marcin Andrychowicz, et al. 2019b. "Solving Rubik's Cube with a Robot Hand." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1910.07113][research_openai_dactyl_2019]
- OpenAI, Christopher Berner, Greg Brockman, et al. 2019a. "Dota 2 with Large Scale Deep Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1912.06680][research_openai_five_2019]
- Osband, Ian, Charles Blundell, Alexander Pritzel, and Benjamin Van Roy. 2016. "Deep Exploration via Bootstrapped DQN." *Advances in Neural Information Processing Systems* 29. [https://papers.nips.cc/paper/2016/hash/8d8818c8e140c64c743113f563cf750f-Abstract.html][research_osband_blundell_pritzel_van_roy_2016]
- Osband, Ian, Yotam Doron, Matteo Hessel, et al. 2020. "Behaviour Suite for Reinforcement Learning." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=rygf-kSYwH][research_osband_et_al_2020]
- Ouyang, Long, Jeffrey Wu, Xu Jiang, et al. 2022. "Training Language Models to Follow Instructions with Human Feedback." In *Advances in Neural Information Processing Systems 35*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/068431-2011][research_ouyang_et_al_2022]
- Perolat, Julien, Bart De Vylder, Daniel Hennes, et al. 2022. "Mastering the Game of Stratego with Model-Free Multiagent Reinforcement Learning." *Science* 378 (6623): 990–96. [https://doi.org/10.1126/science.add4679][research_perolat_et_al_2022]
- Rafailov, Rafael, Archit Sharma, Eric Mitchell, Christopher D. Manning, Stefano Ermon, and Chelsea Finn. 2023. "Direct Preference Optimization: Your Language Model Is Secretly a Reward Model." In *Advances in Neural Information Processing Systems 36*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/075280-2338][research_rafailov_et_al_2023]
- Rashid, Tabish, Mikayel Samvelyan, Christian Schroeder, Gregory Farquhar, Jakob Foerster, and Shimon Whiteson. 2018. "QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v80/rashid18a.html][research_rashid_et_al_2018]
- Reed, Scott, Konrad Zolna, Emilio Parisotto, et al. 2022. "A Generalist Agent." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2205.06175][research_reed_et_al_2022]
- Schaul, Tom, John Quan, Ioannis Antonoglou, and David Silver. 2015. "Prioritized Experience Replay." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1511.05952][research_schaul_et_al_2016]
- Schulman, John, Sergey Levine, Pieter Abbeel, Michael Jordan, and Philipp Moritz. 2015. "Trust Region Policy Optimization." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v37/schulman15.html][research_schulman_levine_moritz_jordan_abbeel_2015]
- Schulman, John, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. 2017. "Proximal Policy Optimization Algorithms." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1707.06347][research_schulman_wolski_dhariwal_radford_klimov_2017]
- Schwarzer, Max, Ankesh Anand, Rishab Goel, R. Devon Hjelm, Aaron Courville, and Philip Bachman. 2021. "Data-Efficient Reinforcement Learning with Self-Predictive Representations." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=uCQfPZwRaUu][research_schwarzer_et_al_2021]
- Silver, David, Thomas Hubert, Julian Schrittwieser, et al. 2018. "A General Reinforcement Learning Algorithm That Masters Chess, Shogi, and Go through Self-Play." *Science* 362 (6419): 1140–44. [https://doi.org/10.1126/science.aar6404][research_silver_et_al_2018]
- Son, Kyunghwan, Daewoo Kim, Wan Ju Kang, David Earl Hostallero, and Yung Yi. 2019. "QTRAN: Learning to Factorize with Transformation for Cooperative Multi-Agent Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v97/son19a.html][research_son_et_al_2019]
- Stiennon, Nisan, Long Ouyang, Jeffrey Wu, et al. 2020. "Learning to Summarize with Human Feedback." *Advances in Neural Information Processing Systems* 33: 3008–21. [https://papers.nips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html][research_stiennon_et_al_2020]
- Tassa, Yuval, Yotam Doron, Alistair Muldal, et al. 2018. "DeepMind Control Suite." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1801.00690][research_tassa_et_al_2018]
- Tobin, Josh, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, and Pieter Abbeel. 2017. "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1703.06907][research_tobin_et_al_2017]
- van Hasselt, Hado, Arthur Guez, and David Silver. 2016. "Deep Reinforcement Learning with Double Q-Learning." *Proceedings of the AAAI Conference on Artificial Intelligence* 30. [https://ojs.aaai.org/index.php/AAAI/article/view/10295][research_van_hasselt_guez_silver_2016]
- Wang, Ziyu, Tom Schaul, Matteo Hessel, Hado Hasselt, Marc Lanctot, and Nando Freitas. 2016. "Dueling Network Architectures for Deep Reinforcement Learning." In *International Conference on Machine Learning*. [https://proceedings.mlr.press/v48/wangf16.html][research_wang_et_al_2016]
- Ye, Weirui, Shaohuai Liu, Thanard Kurutach, Pieter Abbeel, and Yang Gao. 2021. "Mastering Atari Games with Limited Data." *Advances in Neural Information Processing Systems* 34: 25476–88. [https://papers.nips.cc/paper/2021/hash/d5eca8dc3820cad9fe56a3bafda65ca1-Abstract.html][research_ye_liu_kurutach_abbeel_gao_2021]

### Secondary Sources

- Goodfellow, Bengio, and Courville. 2016. *Deep Learning*. [https://www.deeplearningbook.org/][book_goodfellow_bengio_courville_2016]
- Sutton, Richard S., and Barto. 2018. *Reinforcement Learning: An Introduction*. MIT Press. [http://incompleteideas.net/book/the-book-2nd.html][book_sutton_barto_2018]

### Commercial Sources

- "Welcome to Spinning up in Deep RL! — Spinning up Documentation." n.d. Accessed October 25, 2026. [https://spinningup.openai.com/][ref_openai_spinning_up]

### General Sources

- "Berkeley CS285." n.d. Accessed October 25, 2026. [https://rail.eecs.berkeley.edu/deeprlcourse/][ref_berkeley_cs285]
- Botvinick. 2020. "\[Title not identified\]." Accessed October 25, 2026. [https://www.cell.com/neuron/fulltext/S0896-6273(20)30437-5][research_botvinick_et_al_2020]
- "CleanRL." n.d. Accessed October 25, 2026. [https://docs.cleanrl.dev/][ref_cleanrl]
- "Farama Foundation Gymnasium." n.d. Accessed October 25, 2026. [https://gymnasium.farama.org/][ref_farama_gymnasium]
- Horgan. 2018. "\[Title not identified\]." Accessed October 25, 2026. [https://openreview.net/forum?id=H1Dy---0Z][research_horgan_et_al_2018]
- Rao and Ballard. 1999. "\[Title not identified\]." Accessed October 25, 2026. [https://www.nature.com/articles/nn0199\_79][research_rao_ballard_1999]
- "Stable-Baselines3 Docs: Reliable Reinforcement Learning Implementations — Stable Baselines3 2.8.0a1 Documentation." n.d. Accessed October 25, 2026. [https://stable-baselines3.readthedocs.io/][ref_stable_baselines]
- "Sutton and Barto Second Edition PDF." n.d. Accessed October 25, 2026. [http://incompleteideas.net/book/RLbook2020.pdf][ref_sutton_barto_pdf]
- Todorov, Erez, and Tassa. 2012. "\[Title not identified\]." Accessed October 25, 2026. [https://ieeexplore.ieee.org/document/6386109][research_todorov_erez_tassa_2012]

### Related Posts

- Sechter, Brendan. 2025. "Machines That Learn From Experience: Framing." *Brendan A R Sechter's Development Blog*, December 18. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/18/machines\_that\_learn\_from\_experience\_framing.html][related_post_a250_framing]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Bandits and Online Learning." *Brendan A R Sechter's Development Blog*, December 19. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/19/machines\_that\_learn\_from\_experience\_bandits\_and\_online\_learning.html][related_post_a251_bandits]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Reinforcement Learning Foundations." *Brendan A R Sechter's Development Blog*, December 20. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/20/machines\_that\_learn\_from\_experience\_reinforcement\_learning\_foundations.html][related_post_a252_rl_foundations]

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
[research_bai_et_al_2022a]: https://doi.org/10.48550/arxiv.2212.08073
[research_bai_et_al_2022b]: https://doi.org/10.48550/arxiv.2204.05862
[research_baker_et_al_2022]: https://doi.org/10.52202/068431-1789
[research_bauer_et_al_2023]: https://doi.org/10.48550/arxiv.2301.07608
[research_bellemare_dabney_munos_2017]: https://proceedings.mlr.press/v70/bellemare17a.html
[research_bellemare_naddaf_veness_bowling_2013]: https://doi.org/10.1613/jair.3912
[research_botvinick_et_al_2020]: https://www.cell.com/neuron/fulltext/S0896-6273(20)30437-5
[research_cadieu_et_al_2014]: https://doi.org/10.1371/journal.pcbi.1003963
[research_casper_et_al_2023]: https://doi.org/10.48550/arxiv.2307.15217
[research_chen_et_al_2021]: https://papers.nips.cc/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html
[research_christiano_et_al_2017]: https://papers.nips.cc/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html
[research_cobbe_et_al_2019]: https://doi.org/10.48550/arxiv.1912.01588
[research_colas_sigaud_oudeyer_2018]: https://doi.org/10.48550/arxiv.1806.08295
[research_colas_sigaud_oudeyer_2019]: https://doi.org/10.48550/arxiv.1904.06979
[research_dabney_ostrovski_silver_munos_2018]: https://proceedings.mlr.press/v80/dabney18a.html
[research_dabney_rowland_bellemare_munos_2018]: https://doi.org/10.1609/aaai.v32i1.11791
[research_engstrom_et_al_2020]: https://doi.org/10.48550/arxiv.2005.12729
[research_espeholt_et_al_2018]: https://proceedings.mlr.press/v80/espeholt18a.html
[research_fortunato_et_al_2018]: https://openreview.net/forum?id=rywHCPkAW
[research_fujimoto_hoof_meger_2018]: https://proceedings.mlr.press/v80/fujimoto18a.html
[research_ha_schmidhuber_2018]: https://papers.nips.cc/paper/2018/hash/2de5d16682c3c35007e4e92982f1a2ba-Abstract.html
[research_haarnoja_zhou_abbeel_levine_2018]: https://proceedings.mlr.press/v80/haarnoja18b.html
[research_hafner_et_al_2019]: https://proceedings.mlr.press/v97/hafner19a.html
[research_hafner_et_al_2020]: https://openreview.net/forum?id=0oabwyZbOu
[research_hafner_et_al_2023]: https://doi.org/10.48550/arxiv.2301.04104
[research_hausknecht_stone_2015]: https://doi.org/10.48550/arxiv.1507.06527
[research_henderson_et_al_2018]: https://doi.org/10.1609/aaai.v32i1.11694
[research_hessel_et_al_2018]: https://doi.org/10.1609/aaai.v32i1.11796
[research_hilton_et_al_2023]: https://doi.org/10.48550/arxiv.2301.13442
[research_horgan_et_al_2018]: https://openreview.net/forum?id=H1Dy---0Z
[research_jaderberg_et_al_2017]: https://openreview.net/forum?id=SJ6yPD5xg
[research_janner_li_levine_2021]: https://papers.nips.cc/paper_files/paper/2021/hash/099fe6b0b444c23836c4a5d07346082b-Abstract.html
[research_kaiser_et_al_2019]: https://doi.org/10.48550/arxiv.1903.00374
[research_kapturowski_et_al_2019]: https://openreview.net/forum?id=r1lyTjAqYX
[research_kostrikov_yarats_fergus_2020]: https://doi.org/10.48550/arxiv.2004.13649
[research_kuttler_et_al_2020]: https://papers.nips.cc/paper/2020/hash/569ff987c643b4bedf504efda8f786c2-Abstract.html
[research_laskin_srinivas_abbeel_2020]: https://proceedings.mlr.press/v119/laskin20a.html
[research_lecun_bengio_hinton_2015]: https://doi.org/10.1038/nature14539
[research_lillicrap_et_al_2016]: https://doi.org/10.48550/arxiv.1509.02971
[research_lowe_et_al_2017]: https://papers.nips.cc/paper/2017/hash/68a9750337a418a86fe06c1991a1d64c-Abstract.html
[research_mnih_et_al_2013]: https://doi.org/10.48550/arxiv.1312.5602
[research_mnih_et_al_2015]: https://doi.org/10.1038/nature14236
[research_mnih_et_al_2016]: https://proceedings.mlr.press/v48/mniha16.html
[research_openai_dactyl_2019]: https://doi.org/10.48550/arxiv.1910.07113
[research_openai_five_2019]: https://doi.org/10.48550/arxiv.1912.06680
[research_osband_blundell_pritzel_van_roy_2016]: https://papers.nips.cc/paper/2016/hash/8d8818c8e140c64c743113f563cf750f-Abstract.html
[research_osband_et_al_2020]: https://openreview.net/forum?id=rygf-kSYwH
[research_ouyang_et_al_2022]: https://doi.org/10.52202/068431-2011
[research_peng_andrychowicz_zaremba_abbeel_2018]: https://doi.org/10.1109/icra.2018.8460528
[research_perolat_et_al_2022]: https://doi.org/10.1126/science.add4679
[research_rafailov_et_al_2023]: https://doi.org/10.52202/075280-2338
[research_rao_ballard_1999]: https://www.nature.com/articles/nn0199_79
[research_rashid_et_al_2018]: https://proceedings.mlr.press/v80/rashid18a.html
[research_reed_et_al_2022]: https://doi.org/10.48550/arxiv.2205.06175
[research_schaul_et_al_2016]: https://doi.org/10.48550/arxiv.1511.05952
[research_schrittwieser_et_al_2020]: https://doi.org/10.1038/s41586-020-03051-4
[research_schulman_levine_moritz_jordan_abbeel_2015]: https://proceedings.mlr.press/v37/schulman15.html
[research_schulman_wolski_dhariwal_radford_klimov_2017]: https://doi.org/10.48550/arxiv.1707.06347
[research_schwarzer_et_al_2021]: https://openreview.net/forum?id=uCQfPZwRaUu
[research_silver_et_al_2016]: https://doi.org/10.1038/nature16961
[research_silver_et_al_2017]: https://doi.org/10.1038/nature24270
[research_silver_et_al_2018]: https://doi.org/10.1126/science.aar6404
[research_son_et_al_2019]: https://proceedings.mlr.press/v97/son19a.html
[research_stiennon_et_al_2020]: https://papers.nips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html
[research_tassa_et_al_2018]: https://doi.org/10.48550/arxiv.1801.00690
[research_tobin_et_al_2017]: https://doi.org/10.48550/arxiv.1703.06907
[research_todorov_erez_tassa_2012]: https://ieeexplore.ieee.org/document/6386109
[research_van_hasselt_guez_silver_2016]: https://ojs.aaai.org/index.php/AAAI/article/view/10295
[research_vinyals_et_al_2019]: https://doi.org/10.1038/s41586-019-1724-z
[research_wang_et_al_2016]: https://proceedings.mlr.press/v48/wangf16.html
[research_wang_et_al_2018]: https://doi.org/10.1038/s41593-018-0147-8
[research_whittington_et_al_2020]: https://doi.org/10.1016/j.cell.2020.10.024
[research_yamins_dicarlo_2016]: https://doi.org/10.1038/nn.4244
[research_ye_liu_kurutach_abbeel_gao_2021]: https://papers.nips.cc/paper/2021/hash/d5eca8dc3820cad9fe56a3bafda65ca1-Abstract.html
