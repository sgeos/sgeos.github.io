---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: NeuroAI, What Neuroscience and Machine Learning Took From Each Other"
date:   2025-12-31 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 14
---

<!-- A263 -->
<script>console.log("A263");</script>

NeuroAI treats the bidirectional exchange between neuroscience and machine learning as a distinct research program in which advances in one field inform and constrain the other. The framework has produced considerable contributions in both directions across seven decades. Neuroscience contributed the architectural and algorithmic ideas that continue to organize modern machine learning including the artificial neuron, hierarchical convolutional processing, reinforcement learning through prediction-error signals, attention as selective processing, and the hippocampal-cortical distinction between episodic and semantic memory. Machine learning contributed the formal frameworks that continue to organize modern computational neuroscience including task-optimized deep networks as normative models of cortical processing, differentiable programming for the characterization of neural computation, and the benchmarking frameworks through which competing accounts of neural representation can be systematically compared. This article surveys the science and theory of NeuroAI as it stands in the mid 2020s. Coverage includes the historical bidirectional exchanges from McCulloch-Pitts through the modern deep learning era, convolutional networks and the visual system, reinforcement learning and the dopamine system, recurrent networks and prefrontal cortex, neural manifolds and population geometry, meta-learning as a model of cortical learning-to-learn, predictive coding and cortical hierarchies, world models and hippocampal function, grid cells and spatial reinforcement learning, successor representations, complementary learning systems for continual learning, attention mechanisms, sparse coding and efficient sensory representation, language models as models of language cortex, foundation models as models of cognition, biologically-plausible alternatives to backpropagation, neuromorphic computing and spiking networks, task-optimized networks as cortical models, cognitive architectures and symbolic higher cognition, whole-brain simulation and digital-twin approaches, machine learning for neural data analysis, the NeuroAI grand challenges, empirical benchmarks and the Brain-Score framework, ethics safety and neurorights considerations, and the open debates about the strengths and limitations of the correspondence. Articles two through thirteen developed the machine learning frameworks whose neural connections this article consolidates. The present article treats NeuroAI as a distinct research program with its own methods, benchmarks, and characteristic questions.

## The NeuroAI Framework

NeuroAI is the research program that treats the relationship between neuroscience and machine learning as a productive mutual constraint rather than as an incidental analogy. The account rests on the observation that intelligent behavior in biological brains and in artificial systems admits significant architectural, algorithmic, and computational-principle overlap despite the substantial differences in substrate, developmental history, and evolutionary origin.

The model admits several formal orientations. Normative NeuroAI seeks the optimization objectives, architectural constraints, and computational principles that would produce brain-like computation from first principles, testing candidate frameworks against the empirical data on neural representations and behavior. Mechanistic NeuroAI seeks the correspondences between artificial network components (units, layers, learned representations) and biological brain components (neurons, cortical areas, receptive-field structures) that permit brain-machine translation of scientific findings across the substrates.

This formulation's productivity depends on the two-way exchange. Neuroscience provides the empirical constraints and existence proofs through which candidate machine learning frameworks can be validated against biological benchmarks. Machine learning provides the formal computational vocabulary through which neuroscience can articulate and test computational hypotheses at scales and complexities that pure biological experimentation cannot easily reach.

Modern NeuroAI has emerged as a distinctive research program with its own conferences, journals, and empirical benchmarks. The institutional consolidation reflects both the marked recent progress in the field and the recognition that the bidirectional exchange requires dedicated methodological and institutional infrastructure that neither pure neuroscience nor pure machine learning provides alone.

The treatment also acknowledges limitations and productive tensions. Deep learning networks and biological brains differ considerably in their learning rules, in their energetic constraints, in their developmental histories, and in their evolutionary origins. The correspondences that NeuroAI identifies are typically at the level of computational principles rather than at the level of implementations, and the mapping from artificial to biological substrate remains an active and often contested area of research.

## Historical Bidirectional Exchanges

The bidirectional exchange between neuroscience and computational modeling of intelligence traces to the earliest days of both fields. Cybernetics of [Wiener 1948][book_wiener_1948] introduced the systematic framework for the study of control and communication in animal and machine, providing the foundational interdisciplinary context in which subsequent neuroscience-machine learning exchange developed. The [Turing 1950][research_turing_1950] Computing Machinery and Intelligence framework introduced the philosophical and technical framework for artificial intelligence that continues to organize the field. The [McCulloch and Pitts 1943][research_mcculloch_pitts_1943] Logical Calculus of the Ideas Immanent in Nervous Activity introduced the formal neuron model that supported both the biological modeling of neural computation and the subsequent engineering of artificial neural networks. The McCulloch-Pitts neuron computes

$$y = \Theta\!\left(\sum_i w_i \, x_i - \theta\right), \quad \Theta(z) = \begin{cases} 1 & z \geq 0 \\ 0 & z < 0 \end{cases}$$

with $\Theta$ the Heaviside step function, $x_i$ binary inputs, $w_i$ integer weights (positive for excitatory, negative for inhibitory), and $\theta$ a firing threshold. This account proposed that neural activity can be understood as the propagation of logical operations through a network of threshold units, providing the shared computational vocabulary that both fields subsequently developed.

The [Hebb 1949][book_hebb_1949] Organization of Behavior introduced the proposal that synaptic strengths change according to the pattern of pre-synaptic and post-synaptic activity, providing the foundational learning rule that continues to organize both computational neuroscience and machine learning through the Hebbian principle that neurons that fire together wire together. Formally, the Hebbian synaptic update is

$$\Delta w_{ij} = \eta \, x_i \, x_j$$

with $w_{ij}$ the synaptic weight from unit $j$ to unit $i$, $x_i, x_j$ the activities of the two units, and $\eta$ a learning rate. The framework provides the biological grounding for the extensive subsequent literature on unsupervised learning and correlational plasticity.

The [Rosenblatt 1958][research_rosenblatt_1958] Perceptron introduced the single-layer neural network trained through the perceptron learning rule that adjusts weights to correct classification errors. The account provided the first modern artificial learning system and demonstrated the correspondence between formal learning rules and biological plasticity that continues to organize both fields.

The [Hubel and Wiesel 1962][research_hubel_wiesel_1962] receptive-field studies of the cat visual cortex identified the hierarchical organization of visual processing through simple, complex, and hypercomplex cells that respond to progressively more complex visual features. The model directly inspired the convolutional architecture of Fukushima 1980 Neocognitron and subsequently of the deep convolutional networks that dominate modern computer vision.

Backpropagation of errors was independently developed several times before its 1986 popularization. The [Werbos 1974][research_werbos_1974] doctoral thesis introduced the algorithm as beyond regression, and the rediscovery through the [Rumelhart et al. 1986][research_rumelhart_hinton_williams_1986] paper subsequently popularized the treatment through the application to hidden-unit learning. The backpropagation framework introduced the algorithm for efficient gradient-based learning in multi-layer neural networks through the chain-rule propagation of error signals from output back through the layers,

$$\frac{\partial L}{\partial w_{ij}^{(l)}} = \frac{\partial L}{\partial a_j^{(l+1)}} \cdot \frac{\partial a_j^{(l+1)}}{\partial w_{ij}^{(l)}}$$

with $w_{ij}^{(l)}$ the weight from unit $i$ to unit $j$ at layer $l$ and $a_j^{(l+1)}$ the activation at the next layer. The treatment provided the engineering foundation for modern deep learning while raising the biological-plausibility questions that continue to motivate research on alternative learning rules.

The 1990s produced sizable deep learning progress through the development of convolutional neural networks by [LeCun et al. 1989][research_lecun_et_al_1989] for digit recognition, providing the empirical validation that hierarchical processing supports the recognition of complex patterns. This account provided the direct architectural bridge from visual neuroscience to modern computer vision. Concurrent work on associative memory through the [Hopfield 1982][research_hopfield_1982] Neural Networks and Physical Systems with Emergent Collective Computational Abilities introduced the spin-glass-based framework for associative memory that continues to organize computational neuroscience research on cortical memory. Boltzmann machines of [Ackley et al. 1985][research_ackley_hinton_sejnowski_1985] extended the model to generative modeling through the stochastic neural network trained by the contrastive-divergence learning rule.

Recurrent neural network research through the [Elman 1990][research_elman_1990_srn] Simple Recurrent Networks provided the framework for temporal processing that continues to organize modern language modeling and cognitive neuroscience research. NETtalk of [Sejnowski and Rosenberg 1987][research_sejnowski_rosenberg_1987] demonstrated the viability of neural networks for the text-to-speech conversion task and provided one of the first cognitive-scientifically-relevant demonstrations of the modern neural network framework.

The renaissance of deep learning through the 2010s produced the modern NeuroAI research program. AlexNet of [Krizhevsky et al. 2012][research_krizhevsky_sutskever_hinton_2012] demonstrated that deep convolutional networks trained on large-scale image classification produce significantly better performance than prior computer vision methods, and the subsequent [Yamins et al. 2014][research_yamins_et_al_2014] work documented that the resulting learned representations closely match those observed in the primate inferior temporal cortex. The account established the empirical foundation for modern NeuroAI through the demonstration that task-optimized deep networks produce brain-like representations.

The [Hassabis et al. 2017][research_hassabis_et_al_2017] Neuroscience-Inspired Artificial Intelligence article consolidated the modern NeuroAI research program and identified the research directions that continue to organize the field. The [Zador et al. 2023][research_zador_et_al_2023] Catalyzing NeuroAI framework provided the modern grand-challenges statement that has substantially shaped subsequent research funding and institutional development.

## The Perceptron, Hebbian Learning, and Early Neural Networks

The perceptron framework of Rosenblatt 1958 introduced the artificial learning system through the multi-layer network of threshold units trained through iterative error-correction. The network computes the mapping

$$y = \sigma\!\left(\sum_i w_i \, x_i - \theta\right)$$

with $x_i$ inputs, $w_i$ weights, $\theta$ a threshold, and $\sigma$ a nonlinear activation function. The perceptron learning rule adjusts weights when the network's output disagrees with the target,

$$\Delta w_i = \eta \, (y^* - y) \, x_i$$

with $y^\*$ the target and $\eta$ a learning rate. The model provided the first empirical demonstration that learning could occur in an artificial network through the interaction of pattern presentation and error-driven weight adjustment.

The [Minsky and Papert 1969][book_minsky_papert_1969] Perceptrons systematic analysis identified the computational limitations of single-layer perceptrons including the inability to represent linearly-inseparable functions such as XOR. This formulation markedly slowed subsequent perceptron research and motivated the eventual development of multi-layer networks that could overcome the limitations. The [Widrow and Hoff 1960][research_widrow_hoff_1960] Adaptive Switching Circuits framework introduced the delta rule (also known as the LMS or Widrow-Hoff rule) for continuous-output linear neurons, providing the direct precursor to the gradient descent methods that dominate modern deep learning.

Hebbian learning of Hebb 1949 provided the biological-inspired unsupervised alternative to error-driven learning. The rule and its variants including Oja's rule of [Oja 1982][research_oja_1982] introduced normalization terms

$$\Delta w_i = \eta \, y \, (x_i - y \, w_i)$$

that maintain bounded weights while extracting the principal component of the input distribution. The treatment provided the computational bridge from correlational plasticity to unsupervised feature learning.

The renaissance of connectionism through the 1980s produced the Parallel Distributed Processing framework of [Rumelhart McClelland PDP Group 1986][book_rumelhart_mcclelland_1986] Explorations in the Microstructure of Cognition. The two-volume treatise consolidated the connectionist framework and identified the advantages of distributed representations over the limitations of symbolic representations for modeling cognitive processes.

The biological correspondence of these early neural network frameworks has been extensively studied. The perceptron admits biological interpretation as a simplified model of cortical neurons whose learning follows the pattern of error-driven synaptic plasticity, and the Hebbian frameworks admit direct biological interpretation through the patterns of long-term potentiation and long-term depression that have been extensively studied in the mammalian hippocampus and cortex.

## Convolutional Networks and the Visual System

Convolutional Neural Networks (CNNs) provide the clearest and most-developed correspondence between artificial neural network architectures and brain areas. This account connects modern computer vision to the structure of the mammalian visual cortex through the shared use of hierarchical local processing.

The Hubel and Wiesel 1962 receptive-field studies of the cat primary visual cortex documented the hierarchical organization from simple cells that respond to oriented edges in retinal positions, through complex cells that respond to oriented edges regardless of position within a limited region, to hypercomplex cells that respond to edge terminations. The framework identified the principles of local receptive fields, hierarchical processing, and translation-invariance that convolutional networks subsequently implemented.

The Fukushima 1980 [research_fukushima_1980_neocognitron] Neocognitron introduced the artificial network architecture that implements the Hubel-Wiesel hierarchy through alternating layers of feature-detecting simple cells and pooling-based complex cells. The convolutional layer computes

$$(K * x)(i, j) = \sum_{m, n} K(m, n) \, x(i - m, j - n)$$

with $K$ the shared convolutional kernel and $x$ the input feature map, and the pooling layer aggregates over local regions through $\text{Pool}(x)(i, j) = \max_{(m, n) \in \mathcal{N}(i, j)} x(m, n)$ or the corresponding averaging operation. The account provided the direct architectural precursor to modern convolutional networks and demonstrated the viability of hierarchical local processing for pattern recognition.

The LeCun et al 1989 CNN framework combined the Neocognitron architecture with gradient-based training through backpropagation, producing the practical system that supported handwritten digit recognition at commercial scale. The model established the engineering viability of CNNs and organized appreciable subsequent development.

The Krizhevsky Sutskever Hinton 2012 AlexNet framework scaled CNNs to the ImageNet dataset through the combination of larger networks, GPU-based training, dropout regularization, and rectified linear activation. This formulation produced considerable improvements over prior computer vision methods and reinvigorated the entire field of computer vision.

The Yamins et al 2014 framework provided the empirical validation that task-optimized deep CNNs produce internal representations that closely match those observed in the primate inferior temporal cortex. The treatment demonstrated that brain regions can be modeled as task-optimized deep networks and provided the empirical foundation for the modern NeuroAI research program. The representational similarity is measured as

$$r(f_{\text{CNN}}, f_{\text{brain}}) = \text{corr}(\text{RDM}(f_{\text{CNN}}), \text{RDM}(f_{\text{brain}}))$$

where $\text{RDM}$ is the Representational Dissimilarity Matrix computed over stimulus pairs, and $r$ measures the correlation between CNN and brain representational geometries.

Subsequent work including [Kriegeskorte 2015][research_kriegeskorte_2015] Deep Neural Networks and Computational Neuroscience consolidated this formulation and identified the research directions for using deep networks as models of cortical processing. [Cadena et al. 2019][research_cadena_et_al_2019] extended the treatment to the primary visual cortex and documented that task-optimized deep networks match V1 responses appreciably better than the Gabor-filter and divisive-normalization models that had previously dominated V1 modeling.

Recurrent extensions of the account through [Nayebi et al. 2018][research_nayebi_et_al_2018] documented that recurrent connections improve the correspondence to biological visual processing, particularly for the delayed responses observed in the ventral visual pathway. The account provides evidence for the functional role of recurrence in cortical computation.

Auditory extensions of this formulation through [Kell et al. 2018][research_kell_et_al_2018] demonstrated that task-optimized deep networks for speech and music recognition produce internal representations that match those observed in the primate auditory cortex. This formulation extended the CNN-cortex correspondence beyond vision and demonstrated the generality of the task-optimization framework.

CORnet of [Kubilius et al. 2018][research_kubilius_et_al_2019_cornet] introduced the brain-inspired recurrent CNN architecture that matches biological visual processing greatly better than pure feedforward CNNs of comparable size. This account demonstrates the advantages of biological-inspired architectural constraints on the correspondence to biological visual processing.

Self-supervised deep networks of [Zhuang et al. 2021][research_zhuang_et_al_2021] demonstrated that self-supervised training on natural images produces internal representations that match biological visual cortex considerably better than the supervised training on categorical labels. The framework has significantly reshaped subsequent understanding of the normative objectives that produce biological-like representations.

Contrastive learning as a cortical model of [Konkle and Alvarez 2022][research_konkle_alvarez_2022] extended the account to the contrastive-learning objectives and demonstrated the correspondences between contrastive-learning representations and biological ventral-stream representations. The Riesenhuber and Poggio 1999 [research_riesenhuber_poggio_1999_hmax] HMAX framework provided the earlier hierarchical model of object recognition inspired by the properties of ventral-stream visual processing. Face processing has been extensively studied through the frameworks including [Chang and Tsao 2017][research_chang_tsao_2017] Code for Facial Identity that identified the axis-based neural code for face identity in primate face patches.

The [Doerig et al. 2023][research_doerig_et_al_2023] Neuroconnectionist Research Programme framework consolidated the modern task-optimization approach to computational neuroscience and identified the research directions for using deep learning as a systematic tool for computational neuroscience.

## Reinforcement Learning and the Dopamine System

The correspondence between reinforcement learning and the dopamine system represents one of the most-developed neuroscience-machine-learning correspondences. The model provides the computational-neuroscientific instantiation of the temporal-difference learning framework treated in article three.

Temporal difference learning of [Sutton 1988][research_sutton_1988_td_a263] introduced the learning-from-difference framework that provides the computational vocabulary through which the dopamine reward-prediction-error signal was subsequently understood. Q-learning of [Watkins 1989][research_watkins_1989_thesis_a263] doctoral thesis and the actor-critic framework of [Barto Sutton Anderson 1983][research_barto_sutton_anderson_1983] established the formal frameworks through which the biological reward system has subsequently been analyzed.

The [Schultz et al. 1997][research_schultz_dayan_montague_1997] Neural Substrate of Prediction and Reward framework identified the correspondence between the reward-prediction-error signal of temporal-difference learning and the phasic firing of midbrain dopamine neurons. This formulation observed that dopamine neurons respond to unexpected rewards, transfer their response to predictive cues over training, and show a decrement below baseline when expected rewards are omitted, exactly as the temporal-difference framework predicts. The reward-prediction-error signal

$$\delta_t = r_t + \gamma \, V(s_{t+1}) - V(s_t)$$

matches the pattern of dopamine neuron responses across a broad range of experimental conditions.

The [Sutton and Barto 1998][book_sutton_barto_1998] Reinforcement Learning An Introduction (with its subsequent revised edition) consolidated the computational framework and identified the correspondence between actor-critic architectures and the division of labor between the basal ganglia and cortex. The treatment predicts functional roles for distinct dopaminergic and cortical circuits that continue to organize computational neuroscience research on reward-based learning.

Distributional reinforcement learning of [Dabney et al. 2018][research_bellemare_et_al_2017_distributional] extended the framework beyond scalar value estimation to distributional value estimation. The distributional Bellman operator

$$\mathcal{T}^\pi Z(s, a) = R(s, a) + \gamma \, Z(s', a'), \quad a' \sim \pi(\cdot \mid s')$$

evolves the full distribution $Z$ of returns rather than only its mean. The subsequent [Dabney et al. 2020][research_dabney_et_al_2020_dopamine] framework documented the empirical evidence that individual dopamine neurons encode different quantiles of the reward distribution through asymmetric learning rates

$$\delta_t^{(\tau)} = \begin{cases} \alpha^+ (r_t + \gamma V(s_{t+1}) - V_\tau(s_t)) & \text{if } r_t + \gamma V(s_{t+1}) > V_\tau(s_t) \\ \alpha^- (r_t + \gamma V(s_{t+1}) - V_\tau(s_t)) & \text{otherwise} \end{cases}$$

with the quantile encoded determined by the ratio $\tau = \alpha^+ / (\alpha^+ + \alpha^-)$. The framework provides the biological validation of the distributional reinforcement learning framework and demonstrates the significant reverse-informational-flow from machine learning to neuroscience.

The Botvinick Ritter Wang Kurth-Nelson Blundell Hassabis 2019 [research_botvinick_et_al_2019_rl_fast_slow] Reinforcement Learning Fast and Slow framework consolidated the modern reinforcement-learning-neuroscience correspondence and identified the dual-system architecture through which the brain implements both slow model-free and fast model-based reinforcement learning.

The [Niv 2009][research_niv_2009] reinforcement learning in the brain review consolidated the pre-2010s literature and identified the correspondences between temporal-difference learning components and neural circuits. The account has been extensively updated through subsequent work but continues to provide the systematic taxonomy of the reinforcement-learning-neuroscience correspondence. The [Doya 2000][research_doya_2000] Computational Neuroscience of Reinforcement Learning framework provided the earlier systematic treatment that identified the correspondences between the algorithmic components of reinforcement learning and neural circuits.

Model-based versus model-free arbitration in the human brain was systematically studied by [Daw et al. 2011][research_daw_et_al_2011] through the two-step decision task that dissociates the two learning strategies. The model provides quantitative evidence for the behavioral and neural correlates of both model-based and model-free reinforcement learning in humans and continues to organize substantial subsequent research.

Causal evidence for the role of dopamine in reward-prediction-error learning was provided by [Steinberg et al. 2013][research_steinberg_et_al_2013] through the optogenetic manipulation experiments that demonstrated the direct causal effect of dopamine activation on associative learning. The [Eshel et al. 2015][research_eshel_et_al_2015] arithmetic-and-local-circuitry framework provided the mechanistic account of dopamine reward-prediction-error computation through the canonical arithmetic operation performed by the VTA circuit.

The actor-critic architecture in which distinct systems compute state values and action policies admits correspondence to the division of labor between ventral striatum (as critic) and dorsolateral striatum (as actor). The policy gradient theorem underlying this framework computes

$$\nabla_\theta J(\pi_\theta) = \mathbb{E}_{s \sim d^\pi, a \sim \pi_\theta}\!\left[\nabla_\theta \log \pi_\theta(a \mid s) \, A^\pi(s, a)\right]$$

with $A^\pi(s, a) = Q^\pi(s, a) - V^\pi(s)$ the advantage function estimated by the critic. Model-based reinforcement learning frameworks connect to the involvement of the prefrontal cortex and hippocampus in goal-directed behavior. The division between habitual and goal-directed behavior treated in article three admits marked neurobiological grounding through the patterns of prefrontal and dorsomedial-striatal activation observed in goal-directed action.

## Recurrent Networks and Prefrontal Cortex

Recurrent Neural Networks (RNNs) provide the computational framework through which the prefrontal cortex has been modeled. This formulation connects modern deep learning to the empirical literature on cognitive control, working memory, and decision-making in prefrontal circuits.

The [Mante et al. 2013][research_mante_et_al_2013] Context-Dependent Computation by Recurrent Dynamics framework introduced the approach of training recurrent networks on the same behavioral tasks used in monkey neurophysiology and comparing the resulting network dynamics to those observed in the biological prefrontal cortex. The treatment demonstrated that trained networks reproduce the patterns of context-dependent computation observed in the biological system through the dynamics of low-dimensional attractor states.

The [Sussillo and Barak 2013][research_sussillo_barak_2013] Opening the Black Box framework introduced the techniques for analyzing trained RNN dynamics through the identification of fixed points, slow points, and dynamical structure. The general RNN dynamics take the form

$$h_{t+1} = f(W_h h_t + W_x x_t + b), \quad y_t = g(W_y h_t)$$

with $h_t$ the hidden state, $x_t$ the input, $y_t$ the output, and fixed points $h^\*$ satisfying $h^\* = f(W_h h^\* + W_x x^\* + b)$. This account has substantially shaped subsequent computational neuroscience research by providing the analytical tools for understanding trained network computation through the classification of fixed points by the eigenvalues of the linearized dynamics at each fixed point.

Task-trained RNNs as models of prefrontal cortex have been extensively developed through [Song et al. 2016][research_song_yang_wang_2016] and the extensive subsequent literature. The [Yang et al. 2019][research_yang_et_al_2019] Task Representations in Neural Networks Trained to Perform Many Cognitive Tasks framework documented that a single RNN trained on many cognitive tasks develops task-representations that correspond to those observed in the biological prefrontal cortex.

Working memory in RNNs has been extensively studied through the mechanisms by which persistent activity supports the maintenance of task-relevant information across delay periods. The framework predicts patterns of persistent activity and decay dynamics that have been extensively documented in biological prefrontal cortex.

The correspondence between RNN dynamics and biological cortical dynamics extends beyond prefrontal cortex to motor cortex, parietal cortex, and other cortical areas. The [Sussillo et al. 2015][research_sussillo_et_al_2015] framework for motor cortex demonstrated that task-trained RNNs produce dynamical signatures that closely match those observed in the biological motor cortex during reaching movements.

The [Vyas et al. 2020][research_vyas_et_al_2020] Computation Through Neural Population Dynamics framework consolidated the modern population-dynamics perspective on cortical computation and identified the ways in which the neural population dynamics framework unifies sizable portions of the modern cortical neurophysiology literature.

Random RNN dynamics of [Rajan and Abbott 2006][research_rajan_abbott_2006] provided the theoretical framework for the analysis of RNN dynamics in the strongly-recurrent regime, identifying the phase transitions between quiescent and chaotic dynamics that characterize random recurrent networks. The account has markedly influenced the theoretical treatment of trained RNN dynamics.

Working memory in cortical circuits was systematically modeled by [Wang 2002][research_wang_2002_working_memory] through the attractor-network framework that identifies persistent activity as arising from the pattern of excitatory-inhibitory balance in cortical microcircuits. The model provides the bridge between the abstract computational treatment of working memory and the biophysical properties of cortical circuits.

Modern transformer-based architectures have received less direct biological grounding than RNNs, though appreciable research on their correspondence to biological attention mechanisms continues. The question of whether transformer attention corresponds to biological attention or represents a distinct computational mechanism remains an active research area.

## Neural Manifolds and Population Geometry

Neural manifolds are the low-dimensional subspaces of the high-dimensional neural activity space in which behaviorally-relevant computations are performed. This formulation provides the geometric characterization of neural population activity that has appreciably reshaped modern computational neuroscience.

The [Cunningham and Yu 2014][research_cunningham_yu_2014] Dimensionality Reduction for Large-Scale Neural Recordings framework consolidated the modern approach to characterizing high-dimensional neural population activity through the low-dimensional latent variables that capture the task-relevant structure. The treatment provides the systematic methodological foundation for the population-geometry perspective on cortical computation.

The [Gallego et al. 2017][research_gallego_et_al_2017] Neural Manifolds for the Control of Movement framework proposed that motor behavior is generated through the traversal of task-relevant neural manifolds rather than through the activity of individual neurons. This account has considerable empirical support from studies of motor cortex during reaching movements and has greatly reshaped subsequent motor neurophysiology research.

The manifold hypothesis states that the effective dimensionality of neural population activity is considerably lower than the neuron count, and that the low-dimensional structure is task-related. Formally, if the neural population activity $\mathbf{r}(t) \in \mathbb{R}^N$ has effective dimensionality $d \ll N$, then

$$\mathbf{r}(t) \approx \mu + \sum_{k=1}^{d} \alpha_k(t) \, \mathbf{v}_k$$

with $\mu$ the mean activity, $\mathbf{v}\_k$ basis vectors defining the manifold, and $\alpha_k(t)$ the time-varying manifold coordinates that capture the task-relevant dynamics.

Manifold capacity of [Chung et al. 2018][research_chung_lee_sompolinsky_2018] extended the treatment to the theoretical characterization of the representational capacity of neural manifolds. The framework provides the theoretical bridge between geometric properties of neural manifolds and the classification and generalization capabilities they support.

The [Chung and Abbott 2021][research_chung_abbott_2021] Neural Population Geometry review consolidated the modern population geometry framework and identified the research directions that continue to organize the field. The model provides the systematic taxonomy of the geometric properties that characterize task-relevant neural population activity.

Deep learning models increasingly incorporate the geometric properties of neural manifolds through the analysis of trained network representations. This formulation provides the bridge between the modern deep learning literature on representation learning and the empirical population-geometry literature.

The bidirectional exchange in neural manifolds has been significant. Machine learning has provided the analytical tools for characterizing high-dimensional neural population activity, and neuroscience has provided the empirical constraints on the geometric properties that support intelligent computation. The correspondence continues to organize substantial modern NeuroAI research.

## Meta-Learning and Cortical Learning-to-Learn

Meta-learning provides the computational framework for the observation that biological brains can rapidly adapt to novel tasks through their prior experience with related task distributions. The treatment connects modern meta-learning treated in article nine to the empirical literature on cognitive flexibility and rapid learning in biological systems.

The Wang Kurth-Nelson Tirumala Soyer Leibo Munos Blundell Kumaran Botvinick 2018 [research_wang_et_al_2018_prefrontal_meta_a263] Prefrontal Cortex as a Meta-Reinforcement Learning System framework proposed that the prefrontal cortex functions as a meta-reinforcement learning system in which recurrent activity supports fast adaptation across tasks while slower dopaminergic updates train the recurrent weights themselves. Formally, this formulation identifies a two-timescale learning system in which the fast inner-loop adaptation operates through recurrent-state dynamics

$$h_t = \text{RNN}_\theta(o_t, a_{t-1}, r_{t-1}, h_{t-1})$$

with recurrent parameters $\theta$ trained slowly through dopaminergic reward-prediction-error signals to produce the policy $\pi_\theta(a_t \mid h_t)$ that supports fast task-adaptation. The framework provides a computational-level explanation for prefrontal cortex behavior across a wide range of experimental paradigms and connects the machine learning meta-learning framework to the biological prefrontal system.

The account predicts patterns of prefrontal cortex behavior including the transitions between exploration and exploitation, the patterns of task-inference behavior, and the developmental trajectory of meta-learning capacity. Empirical support includes studies of prefrontal cortex activity during rapid task acquisition and studies of prefrontal cortex damage that produce deficits in rapid learning.

The [Duan et al. 2016][research_duan_et_al_2016_rl2_a263] RL-squared and [Wang et al. 2016][research_wang_et_al_2016_l2rl_a263] Learning to Reinforcement Learn frameworks provided the machine learning meta-reinforcement learning frameworks that the prefrontal cortex is proposed to implement. The frameworks demonstrate that recurrent policies trained on task distributions display many hallmarks of efficient reinforcement learning at test time, including exploration and adaptation patterns that were not directly trained.

The bidirectional exchange of the meta-learning-prefrontal-cortex correspondence provides a paradigmatic example of NeuroAI. Machine learning provides the formal framework through which prefrontal cortex behavior can be understood, and neuroscience provides the empirical constraints and existence proofs through which candidate meta-learning frameworks can be validated. The correspondence continues to shape both fields through the mutual constraint of computational and empirical considerations.

## Predictive Coding and Cortical Hierarchies

Predictive coding provides the computational framework that unifies perception, action, and learning through the systematic minimization of prediction errors treated in article thirteen. The model has proved influential across cognitive neuroscience, developmental psychology, and machine learning.

The Rao and Ballard 1999 hierarchical predictive coding framework introduced the proposal that the cortex implements a hierarchy of prediction models in which higher levels predict the activity of lower levels, and prediction errors propagate up the hierarchy to update the predictions. This formulation has marked empirical support from neurophysiological studies of the visual and other cortical systems and continues to organize extensive computational neuroscience research.

The Friston 2010 free energy principle provided the unified theoretical framework through which perception, action, and learning correspond to the minimization of variational free energy

$$F = \mathbb{E}_{q(s)}\!\left[\log q(s) - \log p(o, s)\right]$$

with $q(s)$ the approximate posterior over hidden states, $p(o, s)$ the joint model of observations and hidden states, and $F$ an upper bound on the negative log-evidence. Perception updates $q$, action selects motor commands, and learning updates the model, all through the mechanism of free-energy minimization. The bidirectional relationship between predictive coding and machine learning has been significantly developed. The treatment provides the computational vocabulary through which cortical processing can be understood, and modern machine learning provides the engineering frameworks through which predictive coding can be scaled to complex tasks.

The [Whittington and Bogacz 2019][research_whittington_bogacz_2019] Approximate Backpropagation framework demonstrated that predictive coding networks approximately implement backpropagation-of-error through the local error propagation dynamics. This account establishes the equivalence

$$\Delta w_{ij}^{\text{PC}} \approx \Delta w_{ij}^{\text{BP}} \quad \text{as} \quad \tau_{\text{settle}} \to 0$$

with the PC weight update approaching the backpropagation weight update in the limit of small settling time. The framework provides the bridge between the biologically-motivated predictive coding framework and the gradient-based learning that dominates machine learning practice.

The relationship between deep learning and predictive coding continues to organize sizable research. The account provides one candidate for a biologically-plausible learning rule that could explain how the brain implements the credit-assignment computation required for hierarchical learning.

## World Models, Hippocampus, and Successor Representations

World models provide the computational framework through which the hippocampus and related structures have been increasingly modeled. The model connects the world model treatments of article seven to the empirical literature on the hippocampus and its role in memory, navigation, and imagination.

Place cells were discovered by [O'Keefe and Dostrovsky 1971][research_okeefe_dostrovsky_1971] through the electrophysiological studies of the hippocampus during exploration behavior. The [O'Keefe and Nadel 1978][book_okeefe_nadel_1978] Hippocampus as a Cognitive Map framework consolidated the role of the hippocampus in spatial representation and established the research program that continues to organize hippocampal neurophysiology. The [Buzsáki and Moser 2013][research_buzsaki_moser_2013] Memory Navigation and Theta Rhythm framework provided the modern systematic treatment of the bridge between spatial navigation and memory function in the hippocampal system.

The [Behrens et al. 2018][research_behrens_et_al_2018_cognitive_maps] What Is a Cognitive Map framework consolidated the modern computational neuroscience treatment of the hippocampus as a system for representing and using structured knowledge across many domains. This formulation proposes that the spatial cognitive maps identified in classical neurophysiology generalize to abstract relational maps that support the patterns of flexible behavior observed across many species.

Successor representations of [Dayan 1993][research_dayan_1993_sr] introduced the reinforcement learning framework in which states are represented by the expected future occupancy of other states,

$$M(s, s') = \mathbb{E}\!\left[\sum_{t=0}^{\infty} \gamma^t \, \mathbb{1}[s_t = s'] \, \bigg| \, s_0 = s\right]$$

with $M$ the successor representation matrix and $\gamma$ the discount factor. The treatment provides a alternative to both model-free and model-based reinforcement learning that supports rapid value computation while retaining structural information about the transition dynamics.

The [Stachenfeld et al. 2017][research_stachenfeld_botvinick_gershman_2017] Hippocampus as a Predictive Map framework proposed that the hippocampal place cell system implements the successor representation, providing a computational account of the hippocampal function that unifies spatial and non-spatial hippocampal roles. Under the successor representation, the value function factors as

$$V^\pi(s) = \sum_{s'} M^\pi(s, s') \, R(s')$$

with $M^\pi$ the policy-conditioned successor representation and $R$ the state-reward function. This account has appreciable empirical support and provides testable predictions about the patterns of hippocampal activity that should be observed under different task conditions.

The [Momennejad et al. 2017][research_momennejad_et_al_2017] Successor Representation in Human Learning framework provided the empirical evidence for successor-representation-consistent behavior in human learning, providing further support for the computational role of the hippocampus in flexible predictive representation. The [Mattar and Daw 2018][research_mattar_daw_2018_a263] Prioritized Memory Access framework proposed that hippocampal replay implements a prioritized-experience-replay strategy that maximizes the expected value of the resulting learning, providing the computational bridge between hippocampal replay and modern reinforcement learning replay buffers.

The framework connects the classical hippocampus-and-memory literature to modern reinforcement learning through the shared computational vocabulary of predictive representation. The bidirectional exchange has substantially reshaped both computational neuroscience and machine learning through the shared emphasis on the structural properties that support flexible generalization.

## Grid Cells and Spatial Reinforcement Learning

Grid cells provide one of the most striking correspondences between biological neural computation and artificial neural network structure. The account connects the classical spatial neurophysiology to modern deep reinforcement learning through the emergence of grid-cell-like representations in artificial networks trained on navigation tasks.

The [Hafting et al. 2005][research_hafting_et_al_2005_grid] Microstructure of Spatial Map identified the grid cells in the medial entorhinal cortex that fire at the vertices of a triangular grid tiling the environment. The grid-cell response as a function of position takes the form

$$g_k(\mathbf{x}) = \sum_{i=1}^{3} \cos\!\left(\mathbf{k}_i \cdot (\mathbf{x} - \mathbf{x}_0^{(k)})\right)$$

with $\mathbf{k}\_i$ three wavevectors at $60^\circ$ rotational offset that produce the triangular grid pattern, $\mathbf{x}$ the current position, and $\mathbf{x}\_0^{(k)}$ the grid phase offset for cell $k$. The model revolutionized spatial neuroscience by identifying the representational structure that supports mammalian spatial cognition.

The [Banino et al. 2018][research_banino_et_al_2018_grid] Vector-Based Navigation Using Grid-Like Representations framework demonstrated that recurrent networks trained on navigation tasks spontaneously develop grid-cell-like representations that support the patterns of vector-based navigation observed in biological systems. This formulation provided one of the strongest existence proofs for the NeuroAI research program by demonstrating that biological neural representations emerge from task-optimization in artificial systems.

The [Cueva and Wei 2018][research_cueva_wei_2018] Emergence of Grid-Like Representations framework provided the concurrent independent demonstration of grid-cell emergence in trained networks, and the subsequent [Sorscher et al. 2019][research_sorscher_et_al_2019] Unified Theory framework identified the normative principles that predict when grid-cell-like representations should emerge from task-optimization.

The [Whittington et al. 2020][research_whittington_et_al_2020_tem] Tolman-Eichenbaum Machine framework extended the grid-cell framework to a unified computational model of the hippocampal-entorhinal system that supports both spatial and non-spatial relational reasoning. The treatment provides a computational instantiation of the Behrens et al 2018 cognitive maps framework and has considerable empirical support from studies of hippocampal-entorhinal activity across many task domains.

Grid cells and place cells provide the empirical validation of the modern NeuroAI research program. The emergence of biological neural representations from task-optimization in artificial networks demonstrates that the structural properties of neural computation can be predicted from the computational requirements of the tasks the biological brain solves, providing the systematic bridge between neuroscience and machine learning.

## Complementary Learning Systems and Continual Learning

The Complementary Learning Systems (CLS) framework provides the neuroscientific framework for the continual learning treatments of article ten. This account proposes that mammalian memory arises from the interaction of two distinct learning systems, providing the biological grounding for modern continual learning approaches.

The [McClelland et al. 1995][research_mcclelland_mcnaughton_oreilly_1995_a263] Complementary Learning Systems framework proposed the two-system architecture in which the hippocampus provides fast episodic learning of individual experiences while the neocortex provides slow gradual learning of statistical regularities through hippocampal replay during rest and sleep. The framework resolves the stability-plasticity dilemma by dedicating distinct neural substrates to the two demands.

The account has significant empirical support from studies of hippocampal amnesia patients whose pattern of memory impairment matches the treatment's predictions. The temporally-graded retrograde amnesia observed in these patients, in which memories closer to the hippocampal lesion are more affected than memories from long before the lesion, provides direct empirical support for the consolidation dynamics predicted by the framework. Formally, the CLS framework describes a two-timescale update in which fast hippocampal traces $M_{\text{hipp}}$ update rapidly with each experience and slow cortical parameters $\theta_{\text{cortex}}$ update through interleaved replay,

$$M_{\text{hipp}}^{t+1} = M_{\text{hipp}}^t + \alpha_{\text{fast}} \, \epsilon_t, \quad \theta_{\text{cortex}}^{t+1} = \theta_{\text{cortex}}^t + \alpha_{\text{slow}} \, \nabla_\theta \, \mathbb{E}_{(s, a) \sim M_{\text{hipp}}}[L]$$

with $\alpha_{\text{fast}} \gg \alpha_{\text{slow}}$ enforcing the two-timescale structure that resolves the plasticity-stability dilemma.

The [Kumaran et al. 2016][research_kumaran_hassabis_mcclelland_2016_a263] revised CLS framework extended the original framework with the observation that rapid learning of new information consistent with prior structure occurs directly in cortex, while radical departures from prior structure require the hippocampal system. The revision aligns closely with the observation in machine continual learning that within-distribution updates are less prone to forgetting than out-of-distribution updates.

Modern deep learning implementations of the CLS framework provide the machine learning instantiations that connect the biological framework to modern engineering practice. The experience replay methods of article seven and article ten provide the direct machine learning implementations of the hippocampal replay function, and the slow-consolidation methods provide the machine learning implementations of the neocortical consolidation function. The biological replay literature has been extensively developed through [Foster and Wilson 2006][research_foster_wilson_2006_a263] documentation of reverse replay in hippocampus, the [Ji and Wilson 2006][research_ji_wilson_2007] coordinated hippocampal-cortical replay observations, and the [Louie and Wilson 2001][research_louie_wilson_2001] REM-sleep replay documentation. The treatment provides the bridge from cellular-level empirical observations to computational-level engineering applications.

The bidirectional exchange of the CLS framework provides another paradigmatic example of NeuroAI. This account was developed from empirical constraints on biological memory and subsequently provided the theoretical foundation for the engineering solutions in modern continual learning. The engineering successes in turn provide the computational validation of the biological framework.

## Attention Mechanisms and Cortical Attention

Attention mechanisms in deep learning provide a correspondence to biological attention through the shared computational principle of selective processing. The framework connects modern transformer architectures to the empirical literature on selective attention in biological systems.

The [Bahdanau et al. 2014][research_bahdanau_cho_bengio_2015] Neural Machine Translation with Attention framework introduced the attention mechanism that enables neural networks to selectively attend to input elements. The dot-product attention that dominates modern transformer architectures computes

$$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{Q K^\top}{\sqrt{d_k}}\right) V$$

with $Q, K, V$ the query, key, and value matrices and $d_k$ the key dimensionality. The account subsequently developed into the transformer architecture that dominates modern language modeling and other domains.

The correspondence between attention in deep learning and biological attention has been extensively studied. Biological attention is characterized by the selective modulation of neural responses to task-relevant stimuli, and attention in deep learning implements the selective modulation of processing based on relevance to the current computation. The correspondences at the computational-principle level are substantial, though the implementational details differ markedly between the artificial and biological systems. The [Desimone and Duncan 1995][research_desimone_duncan_1995] biased competition framework provided the neuroscientific account of selective attention through the competitive interactions among cortical representations, and the [Reynolds and Chelazzi 2004][research_reynolds_chelazzi_2004] attentional modulation review consolidated the marked empirical literature on attention as gain modulation.

The [Vaswani et al. 2017][research_vaswani_et_al_2017] Attention Is All You Need framework introduced the transformer architecture that has appreciably reshaped modern deep learning and provided the architectural substrate for the modern language models that have been increasingly used as models of biological language processing.

The [Lindsay 2020][research_lindsay_2020_attention] Attention in Psychology Neuroscience and Machine Learning framework provided the systematic review of the relationships between attention in the three fields. The model identifies the computational principles that unify the three treatments and the differences in implementation and terminology that must be reconciled.

Foveation and selective vision provide additional correspondences between attention in deep learning and biological attention. The pattern by which biological visual systems fixate on task-relevant image regions has been modeled through attention-based deep networks, and the resulting fixation patterns often correspond to those observed in human eye-tracking data.

The bidirectional exchange in attention provides an active area of NeuroAI research. Machine learning attention mechanisms have suggested new hypotheses about biological attention computation, and neuroscience findings about biological attention continue to inform the design of attention mechanisms in artificial systems.

## Sparse Coding, Efficient Coding, and Early Sensory Representations

Sparse coding provides the unsupervised learning framework that produces the receptive field structures observed in the primary visual cortex. This formulation connects the classical unsupervised learning literature to the neurophysiology of early sensory processing.

The [Olshausen and Field 1996][research_olshausen_field_1996] Emergence of Simple-Cell Receptive Field Properties framework demonstrated that sparse coding of natural image patches produces the oriented-edge-detecting receptive fields observed in the primary visual cortex simple cells. The treatment provided the existence proof that biological neural representations can emerge from unsupervised learning with the sparsity objective. The sparse coding objective is

$$L(a, W) = \|x - Wa\|^2 + \lambda \|a\|_1$$

with $x$ the input image patch, $W$ the learned dictionary of basis functions, $a$ the sparse codes, and $\lambda$ a sparsity regularization coefficient. The learned basis functions match the Gabor-like receptive fields observed in V1 simple cells.

Independent Component Analysis (ICA) of [Bell and Sejnowski 1997][research_bell_sejnowski_1997] provided the complementary framework that produces similar receptive-field structures through the mechanism of statistical independence. This account maximizes the mutual information between inputs and separated components,

$$W^* = \arg\max_W \, \mathbb{I}(x \, ; \, g(W x))$$

with $g$ a nonlinear function and $W$ the unmixing matrix. The framework provides the alternative normative-principle account of V1 receptive field structure through the maximization of statistical independence rather than sparsity.

Efficient coding of [Barlow 1961][research_barlow_1961_efficient] introduced the proposal that biological sensory systems are optimized to represent natural signals efficiently. The information-maximization framework computes

$$\max_{\theta} \, \mathbb{I}(X \, ; \, R_\theta(X))$$

with $R_\theta$ the neural encoding of the natural signal $X$. The account provides the theoretical foundation for both sparse coding and ICA accounts of V1 and has greatly shaped subsequent computational sensory neuroscience.

Predictive coding provides an alternative normative-principle account of V1 receptive field structure through the proposal that V1 cells encode prediction errors relative to higher-level predictions. The model has extensive empirical support and continues to organize sizable computational neuroscience research alongside the sparse coding and efficient coding frameworks.

Modern deep learning provides the computational bridge between the classical unsupervised learning frameworks and modern representation learning. Self-supervised learning frameworks including contrastive learning and masked autoencoding produce representations that match aspects of biological visual processing, and the correspondence continues to organize appreciable NeuroAI research. Empirical evidence for sparse coding in biological V1 was provided by [Vinje and Gallant 2000][research_vinje_gallant_2000] through the in-vivo electrophysiological measurements showing that V1 responses to natural images exhibit the sparsity that predictive models had proposed. The [Simoncelli and Olshausen 2001][research_simoncelli_olshausen_2001] Natural Image Statistics and Neural Representation review consolidated the relationship between the statistical structure of natural images and the properties of biological sensory representations.

## Language Models and the Language Cortex

Large language models (LLMs) provide the computational framework through which the language cortex has been increasingly modeled. This formulation represents one of the most-active areas of modern NeuroAI research and has considerably reshaped both computational neuroscience and cognitive neuroscience of language.

The [Toneva and Wehbe 2019][research_toneva_wehbe_2019] Interpreting and Improving Natural Language Processing framework provided the initial systematic demonstration that language model representations predict fMRI responses to naturalistic language stimuli. The treatment demonstrated that transformer language models produce internal representations that closely match those observed in the language cortex.

The [Schrimpf et al. 2021][research_schrimpf_et_al_2021_language] The Neural Architecture of Language framework extended the framework to a systematic benchmark that compares many language models to their capacity to predict brain responses to language stimuli. This account provides the empirical validation that language models increasingly match the patterns of language cortex activation.

The [Caucheteux and King 2022][research_caucheteux_king_2022] Brains and Algorithms framework provided the systematic evidence that language model performance on next-word prediction correlates with the patterns of language cortex activation, supporting the hypothesis that predictive processing underlies both artificial and biological language processing. The brain-language-model alignment is measured through the encoding-model framework

$$\hat{y}_{\text{brain}}(t) = \sum_j \beta_j \, f_{\text{LM}}(x_{1:t})_j$$

with $\hat{y}\_{\text{brain}}$ the predicted brain response, $f_{\text{LM}}(x_{1:t})$ the language model's internal representation given input tokens $x_{1:t}$, and $\beta_j$ the encoding-model coefficients fit through ridge regression on paired language-brain data.

The [Goldstein et al. 2022][research_goldstein_et_al_2022] Shared Computational Principles framework provided the empirical evidence for shared computational principles between language models and biological language processing through the analysis of intracranial recordings from patients listening to naturalistic language.

The [Antonello et al. 2024][research_antonello_et_al_2024] Scaling Laws for Language Models framework extended the account to the scaling relationships between language model capabilities and brain prediction accuracy. The scaling law takes the form

$$r_{\text{brain}}(N) \approx r_\infty - c \, N^{-\alpha}$$

with $r_{\text{brain}}$ the brain prediction accuracy, $N$ the language model parameter count, and $r_\infty, c, \alpha$ fit constants. The model provides evidence that the correspondence to biological language processing improves systematically with model scale.

The bidirectional exchange in language modeling continues to organize considerable NeuroAI research. Language models have provided new hypotheses about biological language processing including the role of predictive computation and the pattern of contextual integration across word sequences. Earlier work by [Jain and Huth 2018][research_jain_huth_2018] documented the correspondence between contextual word embeddings and fMRI responses to naturalistic language, providing the empirical foundation for subsequent work at foundation-model scale. The [Millet et al. 2022][research_millet_et_al_2022] framework extended this formulation to the auditory speech-processing pathway through the systematic comparison of self-supervised speech models to biological auditory-cortex responses.

## Foundation Models as Models of Cognition

Foundation models including large language models have increasingly been treated as models of cognitive processes beyond language processing. The treatment provides the bridge between the empirical cognitive psychology literature and the engineering successes of modern foundation models.

The [Binz and Schulz 2023][research_binz_schulz_2023] Using Cognitive Psychology to Understand GPT-3 framework provided the systematic empirical evaluation of the extent to which large language models exhibit the patterns of human cognitive behavior across many classical cognitive psychology paradigms. This account identified both correspondences and systematic divergences between language models and human cognition.

The [Coda-Forno et al. 2023][research_coda_forno_et_al_2023] Meta-in-Context Learning framework demonstrated that large language models exhibit the patterns of meta-learning behavior that had been proposed for biological prefrontal cortex, providing empirical evidence for the correspondence between language model in-context learning and biological meta-reinforcement learning.

Systematic benchmarks for evaluating foundation models as cognitive models have emerged through frameworks including [Ku et al. 2024][research_ku_et_al_2024] and the significant subsequent literature. The frameworks provide the empirical infrastructure for the systematic evaluation of foundation models against cognitive-psychology benchmarks.

The question of whether foundation models exhibit the cognitive capabilities of biological brains remains actively contested. Foundation models exhibit substantial competence on many cognitive tasks but also exhibit systematic errors that suggest the underlying processing mechanisms differ from those of biological cognition. The [Ullman 2023][research_ullman_2023] Large Language Models Fail on Trivial Alterations framework documented failure modes of language models on classical theory-of-mind tasks that highlight the limitations of the language-model-as-cognitive-model framework.

Modern foundation-model-based cognitive modeling includes the frameworks for fine-tuning language models on cognitive psychology data. The approaches include cognitive-behavior-imitation training, cognitive-benchmark-based reinforcement learning, and the fitting of language model predictions to human behavioral data across many cognitive paradigms.

The relationship between foundation model scale and cognitive-modeling accuracy has been extensively studied. The patterns of scaling behavior suggest that some cognitive-modeling accuracy emerges specifically with scale while other aspects require targeted training data. The patterns continue to organize marked modern NeuroAI research on foundation-model-based cognitive modeling.

## Biologically Plausible Learning Rules

Biologically plausible learning rules address the concern that standard backpropagation is unlikely to be the learning rule implemented by biological brains. The framework provides an active NeuroAI research area with extensive recent progress.

The concerns about biological plausibility of backpropagation include the requirement of symmetric feedforward and feedback weights, the requirement of separate forward and backward passes, the requirement of exact gradient computation, and the requirement of non-local information for the credit assignment computation. Standard backpropagation violates each of these constraints in ways that are difficult to reconcile with biological neural systems.

Feedback alignment of [Lillicrap et al. 2016][research_lillicrap_et_al_2016_feedback] introduced the finding that neural networks can learn effectively with random feedback weights rather than symmetric feedback weights. The feedback alignment update replaces the transpose of the forward weights $W^\top$ with a fixed random matrix $B$,

$$\delta^{(l)} = (B^{(l)})^\top \, \delta^{(l+1)} \odot f'(a^{(l)})$$

with $\delta^{(l)}$ the error signal at layer $l$, $a^{(l)}$ the pre-activation, and $\odot$ the Hadamard product. The account provides the existence proof that the weight symmetry requirement of backpropagation is not essential for effective learning, addressing one of the biological plausibility concerns.

Direct feedback alignment of [Nøkland 2016][research_nokland_2016] extended the treatment to networks in which feedback weights connect directly from the output layer to each hidden layer, further relaxing the structural requirements of backpropagation. The model demonstrates that even significantly simpler feedback structures than standard backpropagation support effective learning.

The [Guerguiev et al. 2017][research_guerguiev_lillicrap_richards_2017] Deep Learning with Segregated Dendrites framework introduced the biologically-plausible framework in which dendritic compartments implement the error signaling required for hierarchical learning. The treatment provides the bridge between the abstract backpropagation algorithm and the biophysical properties of cortical pyramidal neurons.

The [Sacramento et al. 2018][research_sacramento_et_al_2018] Dendritic Cortical Microcircuits framework extended the model with the microcircuit model that implements the error propagation required for learning through the interaction of pyramidal and inhibitory neurons. This account provides one candidate implementation of backpropagation-like learning in biological cortical circuits.

The [Whittington and Bogacz 2019][research_whittington_bogacz_2019_a263] framework treated earlier demonstrated that predictive coding networks approximately implement backpropagation, providing another candidate biologically-plausible learning framework.

The [Payeur et al. 2021][research_payeur_et_al_2021] Burst-Dependent Synaptic Plasticity framework introduced the biologically-plausible learning rule that supports hierarchical credit assignment through the mechanism of pyramidal cell burst firing. The account provides one of the strongest recent contenders for a biologically-plausible learning rule that supports deep-learning-competitive performance.

The [Lillicrap et al. 2020][research_lillicrap_et_al_2020] Backpropagation and the Brain review consolidated the modern biologically-plausible learning literature and identified the research directions that continue to organize the field. The model identifies both the progress that has been achieved and the remaining challenges for demonstrating that biological brains implement backpropagation-like learning.

Target propagation of [Bengio et al. 2015a][research_bengio_et_al_2015_targetprop] introduced the alternative to backpropagation in which target activations rather than error gradients are propagated backward through the network, providing another candidate biologically-plausible learning framework. The [Bengio et al. 2015b][research_bengio_fischer_mesnard_2015] biological deep learning treatment provided the systematic account of the correspondences between biological neural computation and deep learning. Equilibrium propagation of [Scellier and Bengio 2017][research_scellier_bengio_2017] introduced the energy-based framework for local learning that supports deep-learning-competitive performance without requiring the separate forward and backward passes of standard backpropagation.

The [Bartunov et al. 2018][research_bartunov_et_al_2018] Assessing the Scalability of Biologically-Motivated Deep Learning framework provided the systematic empirical evaluation of biologically-plausible learning algorithms against the standard deep learning benchmarks. This formulation documented that many biologically-plausible alternatives fail to match standard backpropagation performance at scale, identifying the remaining challenges for biologically-plausible learning.

The [Song et al. 2020][research_song_et_al_2020_pc_backprop] Can the Brain Do Backpropagation framework provided the systematic modern treatment of the predictive-coding-based biologically-plausible learning framework, establishing that predictive coding networks can approximately implement backpropagation across a broader range of architectures than had previously been demonstrated.

## Neuromorphic Computing and Spiking Networks

Neuromorphic computing treats the engineering of computational systems that implement neural-inspired computation through hardware substrates. The treatment provides the alternative computing paradigm to conventional digital computing that has produced sizable recent progress.

Spiking Neural Networks (SNNs) are the class of neural network models that communicate through discrete spikes rather than continuous activations. The leaky integrate-and-fire neuron dynamics take the form

$$\tau_m \frac{dV}{dt} = -(V - V_{\text{rest}}) + R_m I(t), \quad V(t^+) \leftarrow V_{\text{reset}} \text{ if } V(t) \geq V_{\text{th}}$$

with $V$ the membrane voltage, $\tau_m$ the membrane time constant, $R_m$ the membrane resistance, $I$ the input current, and the spike reset when the voltage crosses the threshold $V_{\text{th}}$. The [Maass 1997][research_maass_1997] Networks of Spiking Neurons framework identified the computational advantages of spiking networks including energy efficiency and temporal coding capacity. This account has substantially shaped subsequent spiking neural network research.

The challenge of training spiking networks derives from the non-differentiable nature of the spike-generation function. Surrogate gradient methods of [Neftci Mostafa Zenke 2019][research_neftci_mostafa_zenke_2019] introduced the approach of using smooth surrogate functions for the spike-derivative during backpropagation,

$$\frac{\partial S}{\partial V} \approx \sigma'(V - V_{\text{th}}) = \frac{1}{(1 + |V - V_{\text{th}}|/\beta)^2}$$

with $S$ the spike output, $V$ the membrane voltage, and $\beta$ a smoothness hyperparameter. The framework enables standard gradient-based training of spiking networks and provides the bridge between conventional deep learning and neuromorphic implementation.

Backpropagation through time for spiking networks of [Bellec et al. 2020][research_bellec_et_al_2020] extended the framework to recurrent spiking networks and produced the engineering framework for training appreciable spiking networks on complex tasks. The account has markedly advanced the engineering capabilities of spiking neural networks.

Neuromorphic hardware including the Intel Loihi chip of [Davies 2018][research_davies_et_al_2018_loihi] and the IBM TrueNorth chip of [Merolla et al. 2014][research_merolla_et_al_2014_truenorth] provide the engineering platforms for the efficient execution of spiking neural networks. This formulation provides the bridge between neuroscience-inspired computation and practical energy-efficient computing.

The advantages of neuromorphic computing include considerable energy efficiency, real-time processing capability, and the temporal computation capabilities that spiking networks support. The treatment has been increasingly applied to edge computing, robotics, and other applications where the advantages of neuromorphic hardware provide practical benefits. The [Indiveri Liu Delbruck 2015][research_indiveri_liu_delbruck_2015] neuromorphic silicon neuron circuits overview consolidated the engineering literature and identified the tradeoffs between biological fidelity and engineering practicality that continue to organize neuromorphic hardware design.

## Task-Optimized Networks as Cortical Models

Task-optimized neural networks provide the normative framework through which cortical processing has been increasingly modeled. This account proposes that brain regions can be understood as computational systems optimized to solve tasks, and that task-optimized artificial networks provide quantitative predictions about the resulting neural representations.

The [Yamins and DiCarlo 2016][research_yamins_dicarlo_2016] Using Goal-Driven Deep Learning Models framework consolidated the modern task-optimization approach to cortical modeling and identified the research directions that continue to organize the field. The framework provides the systematic taxonomy of the approaches through which task-optimized networks can be evaluated against biological data.

The [Richards et al. 2019][research_richards_et_al_2019] Deep Learning Framework for Neuroscience framework provided the systematic modern statement of the deep learning approach to computational neuroscience. The account identifies the ways in which deep learning provides the computational vocabulary through which neural circuit function can be understood and predicted.

The Brain-Score benchmark of [Schrimpf 2020][research_schrimpf_et_al_2020_brainscore] provided the evaluation framework through which candidate deep learning models can be systematically compared to biological data. The model combines neural response prediction, behavioral prediction, and other measures into a unified benchmark that enables systematic model comparison. Model performance on Brain-Score is measured as an aggregate score across brain regions and tasks

$$S(M) = \sum_{r} w_r \cdot \text{fit}(M, r)$$

with $\text{fit}(M, r)$ the model-to-brain-region correspondence for region $r$ and $w_r$ the region-weight. This formulation has appreciably accelerated NeuroAI research by providing the quantitative benchmark against which models can be compared.

The [Marblestone et al. 2016][research_marblestone_wayne_kording_2016] Toward an Integration of Deep Learning and Neuroscience framework provided the systematic modern manifesto for the integration of the two fields. The treatment identifies the research directions that continue to organize NeuroAI and provides the bridge between deep learning practice and computational neuroscience.

The correspondence between task-optimized networks and cortical representations has been documented across many brain regions and task domains through the standard encoding-model framework

$$r_{\text{neural}}(t) = \sum_j \beta_j \, \phi_j(x(t)) + \epsilon_t$$

with $r_{\text{neural}}$ the neural response, $\phi_j$ the features from the task-optimized network, and $\beta_j$ the encoding-model coefficients fit through regularized regression on paired stimulus-response data. Visual cortex responses to images match those of task-optimized convolutional networks. Auditory cortex responses to sounds match those of task-optimized recurrent networks. Language cortex responses to language match those of language models. Motor cortex dynamics match those of task-optimized recurrent networks trained on motor tasks. The breadth of the correspondence provides significant evidence for the task-optimization hypothesis of cortical function.

## Cognitive Architectures and Symbolic Higher Cognition

Cognitive architectures provide the complementary framework to the task-optimized-networks approach through the engineering of symbolic and hybrid symbolic-connectionist systems that model integrated cognitive capabilities. This account provides the bridge between the classical symbolic AI tradition and modern NeuroAI research.

The ACT-R framework of [Anderson 1996][research_anderson_1996_act_r] and its extensive subsequent development introduced the cognitive architecture that models human cognition through the interaction of symbolic declarative and procedural memory systems. The framework has substantial empirical grounding through the systematic fitting of ACT-R predictions to human behavioral data across many cognitive tasks.

The SOAR architecture of [Laird 2012][book_laird_2012_soar] provided the alternative cognitive architecture that models integrated intelligent behavior through the chunking mechanism that generates new procedural knowledge from problem-solving experience. The account has been extensively applied to both cognitive modeling and to AI engineering applications.

Spaun (Semantic Pointer Architecture Unified Network) of [Eliasmith et al. 2012][research_eliasmith_et_al_2012_spaun] introduced the integrated brain model that combines cognitive-architectural principles with the biological constraints of spiking neurons. The model demonstrated a single integrated model that performs eight distinct cognitive tasks including working memory, arithmetic, and pattern recognition, providing the existence proof of the integrated-cognitive-architecture framework at biological scale.

The [Eliasmith 2013][book_eliasmith_2013_how_to_build] How to Build a Brain framework consolidated the approach through the Neural Engineering Framework and the Semantic Pointer Architecture. This formulation provides the systematic engineering methodology for the construction of integrated cognitive models that respect biological constraints.

Neural Turing Machines of [Graves et al. 2014][research_graves_wayne_danihelka_2014_ntm] and Differentiable Neural Computers of [Graves et al. 2016][research_graves_et_al_2016_dnc] introduced the neural-network-based memory-augmented architectures that provide the bridge between the symbolic reasoning of classical cognitive architectures and the representation-learning capabilities of deep neural networks. The frameworks have been greatly influential in the engineering of neural systems that support algorithm-like symbolic computation.

The [Marcus 2020][research_marcus_2020_next_decade] Next Decade in AI framework consolidated the modern hybrid-neurosymbolic research program and identified the research directions that continue to organize the field. The treatment proposes that the integration of symbolic and connectionist frameworks is required for the cognitive capabilities that pure deep learning fails to reproduce.

Modern research on the correspondence between cognitive architectures and biological cognition has been considerably reshaped by the emergence of foundation models. The question of whether foundation models implement cognitive-architectural principles through emergent computation or require the explicit incorporation of cognitive-architectural components remains an active research area.

## Whole-Brain Simulation and Digital-Twin Approaches

Whole-brain simulation approaches treat the engineering of computational models that reproduce the biological brain at the level of individual neurons and synapses. This account provides the complementary approach to the task-optimized-networks framework through the bottom-up construction of brain-like computation.

The Blue Brain Project of [Markram 2006][research_markram_2006_blue_brain] introduced the effort to reconstruct the mammalian cortical microcircuit at biophysical detail through the systematic combination of empirical neuroanatomical and neurophysiological data with large-scale computational simulation. The framework has significantly advanced the engineering and empirical understanding of cortical microcircuitry.

The Human Brain Project consolidated the European commitment to whole-brain simulation and provided the marked infrastructure for the research program. The account has produced extensive progress on the engineering of large-scale simulations while raising questions about the appropriate level of biological detail for computational neuroscience.

Cortex simulation of [Izhikevich and Edelman 2008][research_izhikevich_edelman_2008] provided the large-scale simulation that reproduced the patterns of spontaneous cortical activity through a biologically-detailed model of the mammalian thalamocortical system. The model demonstrated the viability of biologically-detailed whole-brain simulation at large scale.

Digital-twin approaches to brain regions have emerged as a distinctive modern framework. The approaches combine machine learning with detailed neurophysiological data to produce per-individual models of biological brain function that support prediction and personalization for applications including brain-computer interfaces and clinical neuroscience.

The tradeoffs between biological detail and computational tractability continue to organize whole-brain simulation research. Detailed biological simulation provides the empirical grounding but often produces limited computational-level understanding. Task-optimized abstraction provides sizable computational-level understanding but at the cost of biological details. Modern practice increasingly combines the two approaches through the integration of empirical constraints with computational modeling.

## Machine Learning for Neural Data Analysis

Machine learning provides the computational toolkit through which modern neuroscience analyzes the increasingly complex and high-dimensional data produced by modern experimental techniques. This formulation provides the bridge from machine learning to practical neuroscience methodology.

Deep learning for neural spike sorting has substantially improved the accuracy and efficiency of extracting single-neuron activity from multi-electrode recordings. The frameworks including Kilosort of [Pachitariu et al. 2016][research_pachitariu_et_al_2016_kilosort] have become the standard tools for the spike-sorting problem and have markedly accelerated modern electrophysiology research.

Deep learning for calcium imaging analysis of [Giovannucci et al. 2019][research_giovannucci_et_al_2019_caiman] and the CaImAn framework provided the tools for extracting neural activity from calcium imaging data at scale. The treatment has appreciably enabled modern large-scale neural recording research.

Neural decoding through machine learning of [King and Dehaene 2014][research_king_dehaene_2014] and the appreciable subsequent literature has provided the tools for inferring cognitive states from neural activity. This account has enabled the brain-computer interface applications and has provided the systematic methodological framework for the inverse problem of mapping neural activity to cognitive content.

Latent dynamical model frameworks including [Pandarinath et al. 2018][research_pandarinath_et_al_2018_lfads] LFADS provided the tools for extracting low-dimensional neural population dynamics from noisy neural recordings. The framework models neural population spike counts $y_t$ as arising from a latent low-dimensional dynamical process,

$$z_{t+1} = f_\theta(z_t) + \epsilon_t, \quad y_t \sim \text{Poisson}(\exp(W z_t + b))$$

with $z_t$ the latent state, $f_\theta$ a learned RNN transition function, and $W, b$ the readout parameters that map latents to per-neuron firing rates. The account has greatly advanced the analysis of neural population activity and provides the bridge between machine learning latent variable models and neural data analysis.

Modern foundation-model-scale neural data analysis is emerging through frameworks that treat neural recordings as sequential data amenable to transformer-based analysis. The frameworks including Neural Latent Transformers provide the systematic tools for analyzing neural population activity at the scales required by modern experimental methods.

## The NeuroAI Grand Challenges

The Zador et al 2023 Catalyzing NeuroAI framework identified the grand challenges for the modern NeuroAI research program. The model consolidates the modern institutional statement of the field and provides the research agenda that has considerably shaped subsequent funding priorities and institutional development.

The grand challenges include the engineering challenge of building AI systems that exhibit the capabilities of biological brains including flexible adaptation, energy efficiency, robustness to distributional shift, and cumulative capability growth across a lifetime. The scientific challenge is the understanding of biological cognition at a level that supports both explanation and engineering application.

The translational challenges include the brain-inspired engineering of energy-efficient computing systems, the development of brain-computer interfaces that enable the systematic reading and writing of neural information, and the development of AI systems that exhibit the cognitive properties that current systems lack.

The institutional challenges include the development of interdisciplinary training programs that provide the systematic combination of neuroscience and machine learning expertise, the development of research infrastructure that supports the bidirectional exchange, and the development of shared benchmarks and standards through which cross-field progress can be systematically evaluated.

This formulation has significantly reshaped the modern NeuroAI research landscape through the consolidation of the field's identity and priorities. The coordinated funding initiatives, dedicated research centers, and specialized publication venues that have emerged since the Zador et al 2023 statement provide evidence for the practical impact of the account.

## Empirical Landscape and Benchmarks

The empirical landscape of modern NeuroAI has consolidated around several benchmark suites. The Brain-Score framework of Schrimpf et al 2020 treated earlier provides the benchmark for evaluating deep learning models against neural and behavioral data across many brain regions and task domains.

The Neural Latent Benchmark of [Pei et al. 2021][research_pei_et_al_2021_nlb] provided the benchmark for evaluating latent dynamical models of neural population activity across many datasets. This account has substantially accelerated the evaluation and comparison of neural dynamics models.

The Sensorium benchmark of [Willeke et al. 2022][research_willeke_et_al_2022_sensorium] provided the benchmark for predicting mouse visual cortex responses to natural images. The framework has enabled the systematic comparison of many candidate models of visual cortex processing.

For language cortex modeling, the [Antonello Turek Vaidya Huth 2024][research_antonello_et_al_2024_a263] scaling laws framework and the brain-language-model benchmarks provide the systematic evaluation of the correspondence between language models and biological language processing.

For behavioral prediction, the Algonauts Project of [Cichy et al. 2019][research_cichy_et_al_2019_algonauts] and subsequent iterations provide the systematic benchmark for predicting human behavioral responses from computational models. The account has markedly advanced the quantitative comparison of computational models of cognition.

Empirical patterns across benchmarks show several consistent findings. Task-optimized deep networks match brain regions appreciably better than the classical models that had previously dominated computational neuroscience. Model scale greatly improves brain prediction across many domains. Architectural innovations that improve engineering performance also often improve biological prediction. Foundation-model-scale training produces the correspondence that pre-foundation-model methods do not reliably achieve.

## Applications

Brain-computer interfaces (BCIs) represent one of the most-developed applications of NeuroAI. The decoding of motor intention from neural activity supports the control of prosthetic limbs, communication systems, and other assistive technologies. Modern BCI systems increasingly incorporate deep learning-based decoding that considerably improves the accuracy and reliability of intention decoding.

Neural prosthetics for vision and audition use NeuroAI approaches to design the patterns of neural stimulation that produce the perceptual experiences the prosthetic is intended to elicit. The frameworks combine neural network models of the target cortical areas with optimization of the stimulation patterns to achieve the desired outcomes.

Neuroscience-inspired energy-efficient computing uses the principles of biological neural computation to design more energy-efficient artificial computing systems. Neuromorphic computing frameworks including Intel Loihi and IBM TrueNorth treated earlier provide the engineering platforms for these applications.

Diagnostic applications of NeuroAI use machine learning to analyze neural data for the detection and characterization of neurological and psychiatric conditions. The frameworks have been applied to Alzheimer's disease, Parkinson's disease, epilepsy, and psychiatric conditions with considerable practical impact.

Educational applications of NeuroAI use the insights from developmental cognitive neuroscience to design more effective educational technology. The frameworks incorporate the developmental learning treatments of article thirteen into practical educational software.

Modern AI development increasingly incorporates NeuroAI insights through the architectural innovations that mirror biological brain structures, the training procedures that mirror biological developmental trajectories, and the evaluation frameworks that assess brain-like properties of artificial systems.

## Open Debates and Limitations

Several open debates continue to organize modern NeuroAI research. The question of whether deep learning provides a good general framework for understanding biological cognition remains actively contested. Proponents point to the significant empirical successes in brain prediction across many domains. Critics point to the implementational differences between artificial and biological systems and to the cognitive capabilities that current deep learning systems fail to reproduce.

The role of backpropagation in biological learning remains actively debated. The biologically-plausible learning frameworks provide candidate implementations that could be biological, but the empirical evidence for any particular candidate remains limited. The question of whether biological cortical circuits actually implement backpropagation-like credit assignment or use fundamentally different learning mechanisms is an active research area.

The developmental origins of biological neural representations remain incompletely understood. Task-optimized deep networks provide existence proofs that biological representations can emerge from task-optimization, but the developmental mechanisms through which biological brains implement task-optimization remain incompletely characterized. The interaction between innate architectural biases and experience-dependent learning in producing biological representations remains an active research area.

The role of embodiment in biological cognition treated in article thirteen provides an important complementary perspective to the standard task-optimization NeuroAI framework. The embodied and enactive traditions argue that cognition cannot be fully understood in abstraction from the bodily and environmental context, and the implications for modern NeuroAI remain actively debated.

The interpretability of deep learning models as models of biological cognition remains limited. Even when a deep network produces representations that match those observed in biological brains, the mechanistic understanding of the network computation remains significantly harder to achieve than the representational similarity. The development of interpretability techniques that support mechanistic understanding of both artificial and biological neural computation remains an active research area.

The role of foundation models in modern NeuroAI represents a distinctive emerging debate. Foundation models provide substantially better brain prediction than smaller specialized models across many domains, but the mechanisms underlying this improvement remain incompletely understood. The question of whether foundation models capture aspects of biological cognition through their scale, their training data, or their architectural properties remains an active research area.

## Ethics, Safety, and Neurorights

The engineering advances of modern NeuroAI raise substantial ethical and safety considerations that require dedicated research alongside the engineering and scientific work. The model identifies the considerations that must be addressed for responsible development and deployment of NeuroAI technology.

Neurorights of [Yuste et al. 2017][research_yuste_et_al_2017_neurorights] proposed the ethical framework for the emerging neurotechnology field through the identification of the mental privacy, personal identity, free will, equitable access, and mental integrity considerations that neurotechnology development must address. This formulation has markedly shaped subsequent international discussion of neurotechnology regulation and provides the starting point for the responsible development of NeuroAI systems.

Brain-computer interface (BCI) ethics addresses the considerations that arise from the technology that reads and writes information to and from biological brains. The treatment identifies the considerations including informed consent, data privacy, potential for coercion, and equitable access to neuroenhancement technologies. The engineering of BCI systems must address these considerations through the technical and institutional mechanisms.

AI safety considerations that arise from the NeuroAI research program include the concerns about AI systems that increasingly approximate biological cognition. The question of whether brain-like AI systems inherit ethically-relevant capabilities including subjective experience, moral status, or the patterns of goal-directed behavior that characterize biological intelligence remains actively contested.

Dual-use considerations for NeuroAI arise from the applicability of NeuroAI advances to both beneficial and harmful purposes. The concerns include the potential misuse of brain-decoding technologies for surveillance, the potential misuse of brain-stimulation technologies for coercion, and the potential misuse of brain-like AI systems for manipulation. The responsible-innovation framework requires the systematic consideration of these dual-use concerns during technology development.

Fairness and bias considerations in NeuroAI include the concerns about the systematic underrepresentation of demographic groups in the datasets used to train models of biological cognition. The engineering of NeuroAI systems must address the patterns of demographic imbalance in the training data and the implications for the resulting models.

The institutional infrastructure for responsible NeuroAI development is emerging through the combination of research-ethics review boards, industry-ethics guidelines, and international regulatory frameworks. The [OECD Principles on Neurotechnology 2019][research_oecd_neurotechnology_2019] and the subsequent international efforts provide the institutional framework for the responsible development of NeuroAI technology.

The research program on beneficial NeuroAI development includes the efforts to align NeuroAI research with human values, to ensure equitable access to NeuroAI benefits, and to prevent the harms that would arise from irresponsible NeuroAI deployment. This account connects NeuroAI to the broader AI alignment and AI safety literatures through the shared concern with responsible development of transformative technology.

## Load-Bearing Open Questions

- What are the biologically-plausible learning rules that support hierarchical credit assignment in biological cortical circuits?
- How closely do the developmental trajectories of biological neural representations correspond to the training trajectories of task-optimized artificial networks?
- What is the correct account of the role of embodiment in biological cognition, and how should this shape the NeuroAI research program?
- Can the successful correspondences between deep learning and biological cortical processing be extended to the cognitive capabilities that current deep learning fails to reproduce?
- What is the correct interpretation of the correspondence between transformer attention and biological attention?
- How should the temporal and dynamical properties of biological neural computation be incorporated into modern NeuroAI models?
- What is the role of individual variability in biological neural computation, and how should this shape the NeuroAI research program?
- Can the engineering advantages of neuromorphic computing be realized at the scale required for modern deep learning applications?
- What is the relationship between the language capabilities of modern language models and the patterns of biological language processing across the lifespan?
- How should the ethical considerations of neurotechnology be integrated into the modern NeuroAI research program?

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Ackley, David H., Geoffrey E. Hinton, and Terrence J. Sejnowski. 1985. "A Learning Algorithm for Boltzmann Machines." *Cognitive Science* 9 (1): 147–69. [https://doi.org/10.1207/s15516709cog0901\_7][research_ackley_hinton_sejnowski_1985]
- Banino, Andrea, Caswell Barry, Benigno Uria, et al. 2018. "Vector-Based Navigation Using Grid-like Representations in Artificial Agents." *Nature* 557 (7705): 429–33. [https://doi.org/10.1038/s41586-018-0102-6][research_banino_et_al_2018_grid]
- Bell, Anthony J., and Terrence J. Sejnowski. 1997. "The “Independent Components” of Natural Scenes Are Edge Filters." *Vision Research* 37 (23): 3327–38. [https://doi.org/10.1016/s0042-6989(97)00121-1][research_bell_sejnowski_1997]
- Bellec, Guillaume, Franz Scherr, Anand Subramoney, et al. 2020. "A Solution to the Learning Dilemma for Recurrent Networks of Spiking Neurons." *Nature Communications* 11 (1): 3625. [https://doi.org/10.1038/s41467-020-17236-y][research_bellec_et_al_2020]
- Botvinick, Matthew, Sam Ritter, Jane X. Wang, Zeb Kurth-Nelson, Charles Blundell, and Demis Hassabis. 2019. "Reinforcement Learning, Fast and Slow." *Trends in Cognitive Sciences* 23 (5): 408–22. [https://doi.org/10.1016/j.tics.2019.02.006][research_botvinick_et_al_2019_rl_fast_slow]
- Buzsáki, György, and Edvard I. Moser. 2013. "Memory, Navigation and Theta Rhythm in the Hippocampal-Entorhinal System." *Nature Neuroscience* 16 (2): 130–38. [https://doi.org/10.1038/nn.3304][research_buzsaki_moser_2013]
- Caucheteux, Charlotte, and Jean-Rémi King. 2022. "Brains and Algorithms Partially Converge in Natural Language Processing." *Communications Biology* 5 (1): 134. [https://doi.org/10.1038/s42003-022-03036-1][research_caucheteux_king_2022]
- Chang, Le, and Doris Y. Tsao. 2017. "The Code for Facial Identity in the Primate Brain." *Cell* 169 (6): 1013-1028.e14. [https://doi.org/10.1016/j.cell.2017.05.011][research_chang_tsao_2017]
- Chung, SueYeon, and L. F. Abbott. 2021. "Neural Population Geometry: An Approach for Understanding Biological and Artificial Neural Networks." *Current Opinion in Neurobiology* 70: 137–44. [https://doi.org/10.1016/j.conb.2021.10.010][research_chung_abbott_2021]
- Cunningham, John P., and Byron M. Yu. 2014. "Dimensionality Reduction for Large-Scale Neural Recordings." *Nature Neuroscience* 17 (11): 1500–1509. [https://doi.org/10.1038/nn.3776][research_cunningham_yu_2014]
- Dabney, Will, Zeb Kurth-Nelson, Naoshige Uchida, et al. 2020. "A Distributional Code for Value in Dopamine-Based Reinforcement Learning." *Nature* 577 (7792): 671–75. [https://doi.org/10.1038/s41586-019-1924-6][research_dabney_et_al_2020_dopamine]
- Daw, Nathaniel D., Samuel J. Gershman, Ben Seymour, Peter Dayan, and Raymond J. Dolan. 2011. "Model-Based Influences on Humans' Choices and Striatal Prediction Errors." *Neuron* 69 (6): 1204–15. [https://doi.org/10.1016/j.neuron.2011.02.027][research_daw_et_al_2011]
- Doerig, Adrien, Rowan P. Sommers, Katja Seeliger, et al. 2023. "The Neuroconnectionist Research Programme." *Nature Reviews Neuroscience* 24 (7): 431–50. [https://doi.org/10.1038/s41583-023-00705-w][research_doerig_et_al_2023]
- Elman, Jeffrey L. 1990. "Finding Structure in Time." *Cognitive Science* 14 (2): 179–211. [https://doi.org/10.1207/s15516709cog1402\_1][research_elman_1990_srn]
- Eshel, Neir, Michael Bukwich, Vinod Rao, Vivian Hemmelder, Ju Tian, and Naoshige Uchida. 2015. "Arithmetic and Local Circuitry Underlying Dopamine Prediction Errors." *Nature* 525 (7568): 243–46. [https://doi.org/10.1038/nature14855][research_eshel_et_al_2015]
- Foster, David J., and Matthew A. Wilson. 2006. "Reverse Replay of Behavioural Sequences in Hippocampal Place Cells during the Awake State." *Nature* 440 (7084): 680–83. [https://doi.org/10.1038/nature04587][research_foster_wilson_2006_a263]
- Fukushima, Kunihiko. 1980. "Neocognitron: A Self-Organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position." *Biological Cybernetics* 36 (4): 193–202. [https://doi.org/10.1007/bf00344251][research_fukushima_1980_neocognitron]
- Gallego, Juan A., Matthew G. Perich, Lee E. Miller, and Sara A. Solla. 2017. "Neural Manifolds for the Control of Movement." *Neuron* 94 (5): 978–84. [https://doi.org/10.1016/j.neuron.2017.05.025][research_gallego_et_al_2017]
- Goldstein, Ariel, Zaid Zada, Eliav Buchnik, et al. 2022. "Shared Computational Principles for Language Processing in Humans and Deep Language Models." *Nature Neuroscience* 25 (3): 369–80. [https://doi.org/10.1038/s41593-022-01026-4][research_goldstein_et_al_2022]
- Graves, Alex, Greg Wayne, Malcolm Reynolds, et al. 2016. "Hybrid Computing Using a Neural Network with Dynamic External Memory." *Nature* 538 (7626): 471–76. [https://doi.org/10.1038/nature20101][research_graves_et_al_2016_dnc]
- Hafting, Torkel, Marianne Fyhn, Sturla Molden, May-Britt Moser, and Edvard I. Moser. 2005. "Microstructure of a Spatial Map in the Entorhinal Cortex." *Nature* 436 (7052): 801–6. [https://doi.org/10.1038/nature03721][research_hafting_et_al_2005_grid]
- Hassabis, Demis, Dharshan Kumaran, Christopher Summerfield, and Matthew Botvinick. 2017. "Neuroscience-Inspired Artificial Intelligence." *Neuron* 95 (2): 245–58. [https://doi.org/10.1016/j.neuron.2017.06.011][research_hassabis_et_al_2017]
- Hubel, D. H., and T. N. Wiesel. 1962. "Receptive Fields, Binocular Interaction and Functional Architecture in the Cat's Visual Cortex." *Journal of Physiology* 160 (1): 106–54. [https://doi.org/10.1113/jphysiol.1962.sp006837][research_hubel_wiesel_1962]
- Ji, Daoyun, and Matthew A. Wilson. 2006. "Coordinated Memory Replay in the Visual Cortex and Hippocampus during Sleep." *Nature Neuroscience* 10 (1): 100–107. [https://doi.org/10.1038/nn1825][research_ji_wilson_2007]
- Kell, Alexander J. E., Daniel L. K. Yamins, Erica N. Shook, Sam V. Norman-Haignere, and Josh H. McDermott. 2018. "A Task-Optimized Neural Network Replicates Human Auditory Behavior, Predicts Brain Responses, and Reveals a Cortical Processing Hierarchy." *Neuron* 98 (3): 630-644.e16. [https://doi.org/10.1016/j.neuron.2018.03.044][research_kell_et_al_2018]
- Konkle, Talia, and George A. Alvarez. 2022. "A Self-Supervised Domain-General Learning Framework for Human Ventral Stream Representation." *Nature Communications* 13 (1): 491. [https://doi.org/10.1038/s41467-022-28091-4][research_konkle_alvarez_2022]
- Kumaran, Dharshan, Demis Hassabis, and James L. McClelland. 2016. "What Learning Systems Do Intelligent Agents Need? Complementary Learning Systems Theory Updated." *Trends in Cognitive Sciences* 20 (7): 512–34. [https://doi.org/10.1016/j.tics.2016.05.004][research_kumaran_hassabis_mcclelland_2016_a263]
- Lillicrap, Timothy P., Daniel Cownden, Douglas B. Tweed, and Colin J. Akerman. 2016. "Random Synaptic Feedback Weights Support Error Backpropagation for Deep Learning." *Nature Communications* 7 (1): 13276. [https://doi.org/10.1038/ncomms13276][research_lillicrap_et_al_2016_feedback]
- Lillicrap, Timothy P., Adam Santoro, Luke Marris, Colin J. Akerman, and Geoffrey Hinton. 2020. "Backpropagation and the Brain." *Nature Reviews Neuroscience* 21 (6): 335–46. [https://doi.org/10.1038/s41583-020-0277-3][research_lillicrap_et_al_2020]
- Lindsay, Grace W. 2020. "Attention in Psychology, Neuroscience, and Machine Learning." *Frontiers in Computational Neuroscience* 14: 29. [https://doi.org/10.3389/fncom.2020.00029][research_lindsay_2020_attention]
- Louie, Kenway, and Matthew A. Wilson. 2001. "Temporally Structured Replay of Awake Hippocampal Ensemble Activity during Rapid Eye Movement Sleep." *Neuron* 29 (1): 145–56. [https://doi.org/10.1016/s0896-6273(01)00186-6][research_louie_wilson_2001]
- Maass, Wolfgang. 1997. "Networks of Spiking Neurons: The Third Generation of Neural Network Models." *Neural Networks* 10 (9): 1659–71. [https://doi.org/10.1016/s0893-6080(97)00011-7][research_maass_1997]
- Mante, Valerio, David Sussillo, Krishna V. Shenoy, and William T. Newsome. 2013. "Context-Dependent Computation by Recurrent Dynamics in Prefrontal Cortex." *Nature* 503 (7474): 78–84. [https://doi.org/10.1038/nature12742][research_mante_et_al_2013]
- Marblestone, Adam H., Greg Wayne, and Konrad P. Kording. 2016. "Toward an Integration of Deep Learning and Neuroscience." *Frontiers in Computational Neuroscience* 10. [https://doi.org/10.3389/fncom.2016.00094][research_marblestone_wayne_kording_2016]
- Markram, Henry. 2006. "The Blue Brain Project." *Nature Reviews Neuroscience* 7 (2): 153–60. [https://doi.org/10.1038/nrn1848][research_markram_2006_blue_brain]
- Mattar, Marcelo G., and Nathaniel D. Daw. 2018. "Prioritized Memory Access Explains Planning and Hippocampal Replay." *Nature Neuroscience* 21 (11): 1609–17. [https://doi.org/10.1038/s41593-018-0232-z][research_mattar_daw_2018_a263]
- McCulloch, Warren S., and Walter Pitts. 1943. "A Logical Calculus of the Ideas Immanent in Nervous Activity." *Bulletin of Mathematical Biophysics* 5 (4): 115–33. [https://doi.org/10.1007/bf02478259][research_mcculloch_pitts_1943]
- Momennejad, I., E. M. Russek, J. H. Cheong, M. M. Botvinick, N. D. Daw, and S. J. Gershman. 2017. "The Successor Representation in Human Reinforcement Learning." *Nature Human Behaviour* 1 (9): 680–92. [https://doi.org/10.1038/s41562-017-0180-8][research_momennejad_et_al_2017]
- Niv, Yael. 2009. "Reinforcement Learning in the Brain." *Journal of Mathematical Psychology* 53 (3): 139–54. [https://doi.org/10.1016/j.jmp.2008.12.005][research_niv_2009]
- O'Keefe, J., and J. Dostrovsky. 1971. "The Hippocampus as a Spatial Map. Preliminary Evidence from Unit Activity in the Freely-Moving Rat." *Brain Research* 34 (1): 171–75. [https://doi.org/10.1016/0006-8993(71)90358-1][research_okeefe_dostrovsky_1971]
- Oja, Erkki. 1982. "Simplified Neuron Model as a Principal Component Analyzer." *Journal of Mathematical Biology* 15 (3): 267–73. [https://doi.org/10.1007/bf00275687][research_oja_1982]
- Olshausen, Bruno A., and David J. Field. 1996. "Emergence of Simple-Cell Receptive Field Properties by Learning a Sparse Code for Natural Images." *Nature* 381 (6583): 607–9. [https://doi.org/10.1038/381607a0][research_olshausen_field_1996]
- Pandarinath, Chethan, Daniel J. O'Shea, Jasmine Collins, et al. 2018. "Inferring Single-Trial Neural Population Dynamics Using Sequential Auto-Encoders." *Nature Methods* 15 (10): 805–15. [https://doi.org/10.1038/s41592-018-0109-9][research_pandarinath_et_al_2018_lfads]
- Payeur, Alexandre, Jordan Guerguiev, Friedemann Zenke, Blake A. Richards, and Richard Naud. 2021. "Burst-Dependent Synaptic Plasticity Can Coordinate Learning in Hierarchical Circuits." *Nature Neuroscience* 24 (7): 1010–19. [https://doi.org/10.1038/s41593-021-00857-x][research_payeur_et_al_2021]
- Richards, Blake A., Timothy P. Lillicrap, Philippe Beaudoin, et al. 2019. "A Deep Learning Framework for Neuroscience." *Nature Neuroscience* 22 (11): 1761–70. [https://doi.org/10.1038/s41593-019-0520-2][research_richards_et_al_2019]
- Riesenhuber, Maximilian, and Tomaso Poggio. 1999. "Hierarchical Models of Object Recognition in Cortex." *Nature Neuroscience* 2 (11): 1019–25. [https://doi.org/10.1038/14819][research_riesenhuber_poggio_1999_hmax]
- Rumelhart, David E., Geoffrey E. Hinton, and Ronald J. Williams. 1986. "Learning Representations by Back-Propagating Errors." *Nature* 323 (6088): 533–36. [https://doi.org/10.1038/323533a0][research_rumelhart_hinton_williams_1986]
- Scellier, Benjamin, and Yoshua Bengio. 2017. "Equilibrium Propagation: Bridging the Gap between Energy-Based Models and Backpropagation." *Frontiers in Computational Neuroscience* 11: 24. [https://doi.org/10.3389/fncom.2017.00024][research_scellier_bengio_2017]
- Stachenfeld, Kimberly L., Matthew M. Botvinick, and Samuel J. Gershman. 2017. "The Hippocampus as a Predictive Map." *Nature Neuroscience* 20 (11): 1643–53. [https://doi.org/10.1038/nn.4650][research_stachenfeld_botvinick_gershman_2017]
- Steinberg, Elizabeth E., Ronald Keiflin, Josiah R. Boivin, Ilana B. Witten, Karl Deisseroth, and Patricia H. Janak. 2013. "A Causal Link between Prediction Errors, Dopamine Neurons and Learning." *Nature Neuroscience* 16 (7): 966–73. [https://doi.org/10.1038/nn.3413][research_steinberg_et_al_2013]
- Sussillo, David, Mark M. Churchland, Matthew T. Kaufman, and Krishna V. Shenoy. 2015. "A Neural Network That Finds a Naturalistic Solution for the Production of Muscle Activity." *Nature Neuroscience* 18 (7): 1025–33. [https://doi.org/10.1038/nn.4042][research_sussillo_et_al_2015]
- Sutton, Richard S. 1988. "Learning to Predict by the Methods of Temporal Differences." *Machine Learning* 3 (1): 9–44. [https://doi.org/10.1007/bf00115009][research_sutton_1988_td_a263]
- Wang, Jane X., Zeb Kurth-Nelson, Dharshan Kumaran, et al. 2018. "Prefrontal Cortex as a Meta-Reinforcement Learning System." *Nature Neuroscience* 21 (6): 860–68. [https://doi.org/10.1038/s41593-018-0147-8][research_wang_et_al_2018_prefrontal_meta_a263]
- Whittington, James C. R., Timothy H. Muller, Shirley Mark, et al. 2020. "The Tolman-Eichenbaum Machine: Unifying Space and Relational Memory through Generalization in the Hippocampal Formation." *Cell* 183 (5): 1249-1263.e23. [https://doi.org/10.1016/j.cell.2020.10.024][research_whittington_et_al_2020_tem]
- Yamins, Daniel L. K., and James J. DiCarlo. 2016. "Using Goal-Driven Deep Learning Models to Understand Sensory Cortex." *Nature Neuroscience* 19 (3): 356–65. [https://doi.org/10.1038/nn.4244][research_yamins_dicarlo_2016]
- Yang, Guangyu Robert, Madhura R. Joglekar, H. Francis Song, William T. Newsome, and Xiao-Jing Wang. 2019. "Task Representations in Neural Networks Trained to Perform Many Cognitive Tasks." *Nature Neuroscience* 22 (2): 297–306. [https://doi.org/10.1038/s41593-018-0310-2][research_yang_et_al_2019]
- Yuste, Rafael, Sara Goering, Blaise Agüera y Arcas, et al. 2017. "Four Ethical Priorities for Neurotechnologies and AI." *Nature* 551 (7679): 159–63. [https://doi.org/10.1038/551159a][research_yuste_et_al_2017_neurorights]
- Zador, Anthony, Sean Escola, Blake Richards, et al. 2023. "Catalyzing Next-Generation Artificial Intelligence through NeuroAI." *Nature Communications* 14 (1): 1597. [https://doi.org/10.1038/s41467-023-37180-x][research_zador_et_al_2023]

### Primary Sources, Non-Peer-Reviewed

- Anderson, John R. 1996. "ACT: A Simple Theory of Complex Cognition." *American Psychologist* 51 (4): 355–65. [https://doi.org/10.1037/0003-066x.51.4.355][research_anderson_1996_act_r]
- Bahdanau, Dzmitry, Kyunghyun Cho, and Yoshua Bengio. 2014. "Neural Machine Translation by Jointly Learning to Align and Translate." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1409.0473][research_bahdanau_cho_bengio_2015]
- Bartunov, Sergey, Adam Santoro, Blake Richards, Luke Marris, Geoffrey E. Hinton, and Timothy Lillicrap. 2018. "Assessing the Scalability of Biologically-Motivated Deep Learning Algorithms and Architectures." *Advances in Neural Information Processing Systems* 31. [https://papers.nips.cc/paper/2018/hash/63c3ddcc7b23daa1e42dc41f9a44a873-Abstract.html][research_bartunov_et_al_2018]
- Bengio, Lee, Bornschein, Mesnard, and Lin. 2015a. *Target Prop*. [https://scholar.google.com/scholar?q=Target+Prop+Bengio+2015][research_bengio_et_al_2015_targetprop]
- Bengio, Yoshua, Dong-Hyun Lee, Jorg Bornschein, Thomas Mesnard, and Zhouhan Lin. 2015b. "Towards Biologically Plausible Deep Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1502.04156][research_bengio_fischer_mesnard_2015]
- Binz, Marcel, and Eric Schulz. 2023. "Using Cognitive Psychology to Understand GPT-3." *Proceedings of the National Academy of Sciences* 120 (6): e2218523120. [https://doi.org/10.1073/pnas.2218523120][research_binz_schulz_2023]
- Cadena, Santiago A., George H. Denfield, Edgar Y. Walker, et al. 2019. "Deep Convolutional Models Improve Predictions of Macaque V1 Responses to Natural Images." *PLOS Computational Biology* 15 (4): e1006897. [https://doi.org/10.1371/journal.pcbi.1006897][research_cadena_et_al_2019]
- Chung, SueYeon, Daniel D. Lee, and Haim Sompolinsky. 2018. "Classification and Geometry of General Perceptual Manifolds." *Physical Review X* 8 (3): 031003. [https://doi.org/10.1103/physrevx.8.031003][research_chung_lee_sompolinsky_2018]
- Cichy, Radoslaw Martin, Gemma Roig, Alex Andonian, et al. 2019. "The Algonauts Project: A Platform for Communication between the Sciences of Biological and Artificial Intelligence." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1905.05675][research_cichy_et_al_2019_algonauts]
- Coda-Forno, Julian, Marcel Binz, Zeynep Akata, Matt Botvinick, Jane Wang, and Eric Schulz. 2023. "Meta-in-Context Learning in Large Language Models." In *Advances in Neural Information Processing Systems 36*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/075280-2844][research_coda_forno_et_al_2023]
- Cueva, Christopher J., and Xue-Xin Wei. 2018. "Emergence of Grid-like Representations by Training Recurrent Neural Networks to Perform Spatial Localization." In *International Conference on Learning Representations*. [https://openreview.net/forum?id=B17JTOe0-][research_cueva_wei_2018]
- Dabney, Will, Mark Rowland, Marc Bellemare, and Rémi Munos. 2018. "Distributional Reinforcement Learning with Quantile Regression." *Proceedings of the AAAI Conference on Artificial Intelligence* 32 (1). [https://doi.org/10.1609/aaai.v32i1.11791][research_bellemare_et_al_2017_distributional]
- Dayan, Peter. 1993. "Improving Generalization for Temporal Difference Learning: The Successor Representation." *Neural Computation* 5 (4): 613–24. [https://doi.org/10.1162/neco.1993.5.4.613][research_dayan_1993_sr]
- Desimone, Robert, and John Duncan. 1995. "Neural Mechanisms of Selective Visual Attention." *Annual Review of Neuroscience* 18 (1): 193–222. [https://doi.org/10.1146/annurev.ne.18.030195.001205][research_desimone_duncan_1995]
- Doya, Kenji. 2000. "Reinforcement Learning in Continuous Time and Space." *Neural Computation* 12 (1): 219–45. [https://doi.org/10.1162/089976600300015961][research_doya_2000]
- Duan, Yan, John Schulman, Xi Chen, Peter L. Bartlett, Ilya Sutskever, and Pieter Abbeel. 2016. "RL^2: Fast Reinforcement Learning via Slow Reinforcement Learning." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1611.02779][research_duan_et_al_2016_rl2_a263]
- Eliasmith, Chris, Terrence C. Stewart, Xuan Choo, et al. 2012. "A Large-Scale Model of the Functioning Brain." *Science* 338 (6111): 1202–5. [https://doi.org/10.1126/science.1225266][research_eliasmith_et_al_2012_spaun]
- Giovannucci, Andrea, Johannes Friedrich, Pat Gunn, et al. 2019. "CaImAn an Open Source Tool for Scalable Calcium Imaging Data Analysis." *eLife* 8: e38173. [https://doi.org/10.7554/elife.38173][research_giovannucci_et_al_2019_caiman]
- Graves, Alex, Greg Wayne, and Ivo Danihelka. 2014. "Neural Turing Machines." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1410.5401][research_graves_wayne_danihelka_2014_ntm]
- Guerguiev, Jordan, Timothy P. Lillicrap, and Blake A. Richards. 2017. "Towards Deep Learning with Segregated Dendrites." *eLife* 6: e22901. [https://doi.org/10.7554/elife.22901][research_guerguiev_lillicrap_richards_2017]
- Hopfield, J. J. 1982. "Neural Networks and Physical Systems with Emergent Collective Computational Abilities." *Proceedings of the National Academy of Sciences* 79 (8): 2554–58. [https://doi.org/10.1073/pnas.79.8.2554][research_hopfield_1982]
- Izhikevich, Eugene M., and Gerald M. Edelman. 2008. "Large-Scale Model of Mammalian Thalamocortical Systems." *Proceedings of the National Academy of Sciences* 105 (9): 3593–98. [https://doi.org/10.1073/pnas.0712231105][research_izhikevich_edelman_2008]
- Jain, Shailee, and Alexander Huth. 2018. "Incorporating Context into Language Encoding Models for fMRI." In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2018/hash/f471223d1a1614b58a7dc45c9d01df19-Abstract.html][research_jain_huth_2018]
- Kriegeskorte, Nikolaus. 2015. "Deep Neural Networks: A New Framework for Modeling Biological Vision and Brain Information Processing." *Annual Review of Vision Science* 1 (1): 417–46. [https://doi.org/10.1146/annurev-vision-082114-035447][research_kriegeskorte_2015]
- Krizhevsky, Alex, Ilya Sutskever, and Geoffrey E. Hinton. 2012. "ImageNet Classification with Deep Convolutional Neural Networks." *Advances in Neural Information Processing Systems* 25. [https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html][research_krizhevsky_sutskever_hinton_2012]
- Ku, Tellex, Wu, and Herrera. 2024. *LLM Cognitive*. [https://scholar.google.com/scholar?q=LLM+Cognitive+Ku+2024][research_ku_et_al_2024]
- Kubilius, Jonas, Martin Schrimpf, Aran Nayebi, Daniel Bear, Daniel L. K. Yamins, and James J. DiCarlo. 2018. "CORnet: Modeling the Neural Mechanisms of Core Object Recognition." Preprint, bioRxiv. [https://doi.org/10.1101/408385][research_kubilius_et_al_2019_cornet]
- LeCun, Y., B. Boser, J. S. Denker, et al. 1989. "Backpropagation Applied to Handwritten Zip Code Recognition." *Neural Computation* 1 (4): 541–51. [https://doi.org/10.1162/neco.1989.1.4.541][research_lecun_et_al_1989]
- Marcus, Gary. 2020. "The Next Decade in AI: Four Steps towards Robust Artificial Intelligence." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2002.06177][research_marcus_2020_next_decade]
- McClelland, James L., Bruce L. McNaughton, and Randall C. O'Reilly. 1995. "Why There Are Complementary Learning Systems in the Hippocampus and Neocortex: Insights from the Successes and Failures of Connectionist Models of Learning and Memory." *Psychological Review* 102 (3): 419–57. [https://doi.org/10.1037/0033-295x.102.3.419][research_mcclelland_mcnaughton_oreilly_1995_a263]
- Merolla, Paul A., John V. Arthur, Rodrigo Alvarez-Icaza, et al. 2014. "A Million Spiking-Neuron Integrated Circuit with a Scalable Communication Network and Interface." *Science* 345 (6197): 668–73. [https://doi.org/10.1126/science.1254642][research_merolla_et_al_2014_truenorth]
- Millet, Juliette, Charlotte Caucheteux, pierre Orhan, et al. 2022. "Toward a Realistic Model of Speech Processing in the Brain with Self-Supervised Learning." In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2022/hash/d81ecfc8fb18e833a3fa0a35d92532b8-Abstract-Conference.html][research_millet_et_al_2022]
- Nayebi, Aran, Daniel Bear, Jonas Kubilius, et al. 2018. "Task-Driven Convolutional Recurrent Models of the Visual System." *Advances in Neural Information Processing Systems* 31. [https://papers.nips.cc/paper/2018/hash/6be93f7a96fed60c477d30ae1de032fd-Abstract.html][research_nayebi_et_al_2018]
- Nøkland, Arild. 2016. "Direct Feedback Alignment Provides Learning in Deep Neural Networks." *Advances in Neural Information Processing Systems* 29. [https://papers.nips.cc/paper/2016/hash/d490d7b4576290fa60eb31b5fc917ad1-Abstract.html][research_nokland_2016]
- Pachitariu, Marius, Nicholas Steinmetz, Shabnam Kadir, Matteo Carandini, and Kenneth D. Harris. 2016. "Kilosort: Realtime Spike-Sorting for Extracellular Electrophysiology with Hundreds of Channels." Preprint, bioRxiv. [https://doi.org/10.1101/061481][research_pachitariu_et_al_2016_kilosort]
- Pei, Felix C., Joel Ye, David M. Zoltowski, et al. 2021. "Neural Latents Benchmark ‘21: Evaluating Latent Variable Models of Neural Population Activity." In *Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)*. [https://openreview.net/forum?id=KVMS3fl4Rsv][research_pei_et_al_2021_nlb]
- Rajan, Kanaka, and L. F. Abbott. 2006. "Eigenvalue Spectra of Random Matrices for Neural Networks." *Physical Review Letters* 97 (18): 188104. [https://doi.org/10.1103/physrevlett.97.188104][research_rajan_abbott_2006]
- Reynolds, John H., and Leonardo Chelazzi. 2004. "Attentional Modulation of Visual Processing." *Annual Review of Neuroscience* 27 (1): 611–47. [https://doi.org/10.1146/annurev.neuro.26.041002.131039][research_reynolds_chelazzi_2004]
- Rosenblatt, F. 1958. "The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain." *Psychological Review* 65 (6): 386–408. [https://doi.org/10.1037/h0042519][research_rosenblatt_1958]
- Sacramento, João, Rui Ponte Costa, Yoshua Bengio, and Walter Senn. 2018. "Dendritic Cortical Microcircuits Approximate the Backpropagation Algorithm." *Advances in Neural Information Processing Systems* 31. [https://papers.nips.cc/paper/2018/hash/1dc3a89d0d440ba31729b0ba74b93a33-Abstract.html][research_sacramento_et_al_2018]
- Schrimpf, Martin, Idan Asher Blank, Greta Tuckute, et al. 2021. "The Neural Architecture of Language: Integrative Modeling Converges on Predictive Processing." *Proceedings of the National Academy of Sciences* 118 (45): e2105646118. [https://doi.org/10.1073/pnas.2105646118][research_schrimpf_et_al_2021_language]
- Schultz, Wolfram, Peter Dayan, and P. Read Montague. 1997. "A Neural Substrate of Prediction and Reward." *Science* 275 (5306): 1593–99. [https://doi.org/10.1126/science.275.5306.1593][research_schultz_dayan_montague_1997]
- Sejnowski and Rosenberg. 1987. *NETtalk*. [https://scholar.google.com/scholar?q=NETtalk+Sejnowski+Rosenberg+1987][research_sejnowski_rosenberg_1987]
- Simoncelli, Eero P., and Bruno A. Olshausen. 2001. "Natural Image Statistics and Neural Representation." *Annual Review of Neuroscience* 24 (1): 1193–1216. [https://doi.org/10.1146/annurev.neuro.24.1.1193][research_simoncelli_olshausen_2001]
- Song, H. Francis, Guangyu R. Yang, and Xiao-Jing Wang. 2016. "Training Excitatory-Inhibitory Recurrent Neural Networks for Cognitive Tasks: A Simple and Flexible Framework." *PLOS Computational Biology* 12 (2): e1004792. [https://doi.org/10.1371/journal.pcbi.1004792][research_song_yang_wang_2016]
- Sorscher, Ben, Gabriel Mel, Surya Ganguli, and Samuel Ocko. 2019. "A Unified Theory for the Origin of Grid Cells through the Lens of Pattern Formation." In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2019/hash/6e7d5d259be7bf56ed79029c4e621f44-Abstract.html][research_sorscher_et_al_2019]
- Sussillo, David, and Omri Barak. 2013. "Opening the Black Box: Low-Dimensional Dynamics in High-Dimensional Recurrent Neural Networks." *Neural Computation* 25 (3): 626–49. [https://doi.org/10.1162/neco\_a\_00409][research_sussillo_barak_2013]
- Toneva, Mariya, and Leila Wehbe. 2019. "Interpreting and Improving Natural-Language Processing (in Machines) with Natural Language-Processing (in the Brain)." In *Advances in Neural Information Processing Systems*. [https://papers.nips.cc/paper\_files/paper/2019/hash/749a8e6c231831ef7756db230b4359c8-Abstract.html][research_toneva_wehbe_2019]
- Turing, A. M. 1950. "i.—Computing Machinery and Intelligence." *Mind* LIX (236): 433–60. [https://doi.org/10.1093/mind/lix.236.433][research_turing_1950]
- Ullman, Tomer. 2023. "Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2302.08399][research_ullman_2023]
- Vaswani, Ashish, Noam Shazeer, Niki Parmar, et al. 2017. "Attention Is All You Need." *Advances in Neural Information Processing Systems* 30. [https://papers.nips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html][research_vaswani_et_al_2017]
- Vinje, William E., and Jack L. Gallant. 2000. "Sparse Coding and Decorrelation in Primary Visual Cortex during Natural Vision." *Science* 287 (5456): 1273–76. [https://doi.org/10.1126/science.287.5456.1273][research_vinje_gallant_2000]
- Vyas, Saurabh, Matthew D. Golub, David Sussillo, and Krishna V. Shenoy. 2020. "Computation through Neural Population Dynamics." *Annual Review of Neuroscience* 43 (1): 249–75. [https://doi.org/10.1146/annurev-neuro-092619-094115][research_vyas_et_al_2020]
- Wang. 2002. *Working Memory*. [https://scholar.google.com/scholar?q=Working+Memory+Wang+2002][research_wang_2002_working_memory]
- Wang, Jane X., Zeb Kurth-Nelson, Dhruva Tirumala, et al. 2016. "Learning to Reinforcement Learn." Preprint, arXiv. [https://doi.org/10.48550/arxiv.1611.05763][research_wang_et_al_2016_l2rl_a263]
- Widrow and Hoff. 1960. "Adaptive." [https://apps.dtic.mil/sti/citations/AD0241531][research_widrow_hoff_1960]
- Willeke, Konstantin F., Paul G. Fahey, Mohammad Bashiri, et al. 2022. "The Sensorium Competition on Predicting Large-Scale Mouse Primary Visual Cortex Activity." Preprint, arXiv. [https://doi.org/10.48550/arxiv.2206.08666][research_willeke_et_al_2022_sensorium]
- Yamins, Daniel L. K., Ha Hong, Charles F. Cadieu, Ethan A. Solomon, Darren Seibert, and James J. DiCarlo. 2014. "Performance-Optimized Hierarchical Models Predict Neural Responses in Higher Visual Cortex." *Proceedings of the National Academy of Sciences* 111 (23): 8619–24. [https://doi.org/10.1073/pnas.1403112111][research_yamins_et_al_2014]
- Zhuang, Chengxu, Siming Yan, Aran Nayebi, et al. 2021. "Unsupervised Neural Network Models of the Ventral Visual Stream." *Proceedings of the National Academy of Sciences* 118 (3): e2014196118. [https://doi.org/10.1073/pnas.2014196118][research_zhuang_et_al_2021]

### Secondary Sources

- Eliasmith, Chris. 2013. *How to Build a Brain: A Neural Architecture for Biological Cognition*. Oxford University Press, Incorporated. [https://global.oup.com/academic/product/how-to-build-a-brain-9780190262129][book_eliasmith_2013_how_to_build]
- Hebb, D. O. 1949. *The Organization of Behavior*. Wiley. [https://www.taylorfrancis.com/books/mono/10.4324/9781410612403/organization-behavior-hebb][book_hebb_1949]
- Laird, John. 2012. *The Soar Cognitive Architecture*. MIT Press. [https://mitpress.mit.edu/9780262122962/the-soar-cognitive-architecture/][book_laird_2012_soar]
- Minsky, Marvin, and Seymour Papert. 1969. *Perceptrons: An Introduction to Computational Geometry*. Brand: MIT Press. [https://mitpress.mit.edu/9780262631112/perceptrons/][book_minsky_papert_1969]
- O'Keefe, John., and Nadel. 1978. *The Hippocampus as a Cognitive Map*. Clarendon Press. [https://academic.oup.com/book/1050][book_okeefe_nadel_1978]
- Rumelhart McClelland PDP Group. 1986. *PDP*. [https://mitpress.mit.edu/9780262680530/parallel-distributed-processing/][book_rumelhart_mcclelland_1986]
- Sutton, Richard S., and Barto. 1998. *Reinforcement Learning: An Introduction*. MIT Press. [https://mitpress.mit.edu/9780262039246/reinforcement-learning/][book_sutton_barto_1998]
- Sutton, Richard S., and Barto. 2018. *Reinforcement Learning: An Introduction*. MIT Press. [http://incompleteideas.net/book/the-book-2nd.html][book_sutton_barto_2018]
- Wiener, Norbert. 1948. *Cybernetics, or Control and Communication in the Animal and the Machine*. The M.i.t. Press. [https://mitpress.mit.edu/9780262537841/cybernetics/][book_wiener_1948]

### Commercial Sources

- "DeepMind x UCL RL Course." n.d. Accessed October 25, 2026. [https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021][ref_deepmind_ucl_rl]
- "OpenAI Spinning Up." n.d. Accessed October 25, 2026. [https://spinningup.openai.com/][ref_openai_spinning_up]

### General Sources

- Antonello, Turek, Vaidya, and Huth. 2024. "\[Title not identified\]." Accessed October 25, 2026. [https://openreview.net/forum?id=xI71dsS3o4][research_antonello_et_al_2024]
- Antonello Turek Vaidya Huth. 2024. "A263." [https://openreview.net/forum?id=xI71dsS3o4][research_antonello_et_al_2024_a263]
- Barlow. 1961. "Efficient Coding." [https://scholar.google.com/scholar?q=barlow+1961+possible+principles+underlying+sensory+messages][research_barlow_1961_efficient]
- Barto Sutton Anderson. 1983. "Actor-Critic." [https://ieeexplore.ieee.org/document/6313077][research_barto_sutton_anderson_1983]
- Behrens, Muller, Whittington, et al. 2018. "Cognitive Maps." [https://www.cell.com/neuron/fulltext/S0896-6273(18)30856-6][research_behrens_et_al_2018_cognitive_maps]
- "Berkeley CS285." n.d. Accessed October 25, 2026. [https://rail.eecs.berkeley.edu/deeprlcourse/][ref_berkeley_cs285]
- Davies. 2018. "Loihi." [https://ieeexplore.ieee.org/document/8259423][research_davies_et_al_2018_loihi]
- Indiveri Liu Delbruck. 2015. "Silicon Neurons." [https://ieeexplore.ieee.org/document/7108440][research_indiveri_liu_delbruck_2015]
- King and Dehaene. 2014. "Decoding." [https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(14)00047-X][research_king_dehaene_2014]
- Neftci Mostafa Zenke. 2019. "Surrogate." [https://ieeexplore.ieee.org/document/8891809][research_neftci_mostafa_zenke_2019]
- OECD. 2019. "Neurotechnology." [https://www.oecd.org/en/topics/sub-issues/emerging-technologies/neurotechnology.html][research_oecd_neurotechnology_2019]
- Schrimpf. 2020. "Brain-Score." [https://www.biorxiv.org/content/10.1101/407007v2][research_schrimpf_et_al_2020_brainscore]
- "Silver RL Course UCL." n.d. Accessed October 25, 2026. [https://www.davidsilver.uk/teaching/][ref_silver_rl_course]
- Song, Millidge, Salvatori, Lukasiewicz, Xu, and Bogacz. 2020. "PC Backprop." [https://papers.nips.cc/paper/2020/hash/fec87a37cdeec1c6ecf8181c0aa2d3bf-Abstract.html][research_song_et_al_2020_pc_backprop]
- "Stanford CS234." n.d. Accessed October 25, 2026. [https://web.stanford.edu/class/cs234/][ref_stanford_cs234]
- Watkins. 1989. "Q-Learning." [https://www.cs.rhul.ac.uk/~chrisw/new\_thesis.pdf][research_watkins_1989_thesis_a263]
- Werbos. 1974. "Backprop Thesis." [https://scholar.google.com/scholar?q=werbos+1974+beyond+regression][research_werbos_1974]
- Whittington and Bogacz. 2019. "A263." [https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(18)30284-X][research_whittington_bogacz_2019]

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
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Evolutionary and Open-Ended Adaptation." *Brendan A R Sechter's Development Blog*, December 29. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/29/machines\_that\_learn\_from\_experience\_evolutionary\_and\_open\_ended\_adaptation.html][related_post_a261_evolutionary]
- Sechter, Brendan. 2025. "Machines That Learn From Experience: Embodied Cognition and Developmental Learning." *Brendan A R Sechter's Development Blog*, December 30. [https://sgeos.github.io/artificial-intelligence/machine-learning/neuroscience/2025/12/30/machines\_that\_learn\_from\_experience\_embodied\_cognition\_and\_developmental\_learning.html][related_post_a262_embodied]

[book_eliasmith_2013_how_to_build]: https://global.oup.com/academic/product/how-to-build-a-brain-9780190262129
[book_hebb_1949]: https://www.taylorfrancis.com/books/mono/10.4324/9781410612403/organization-behavior-hebb
[book_laird_2012_soar]: https://mitpress.mit.edu/9780262122962/the-soar-cognitive-architecture/
[book_minsky_papert_1969]: https://mitpress.mit.edu/9780262631112/perceptrons/
[book_okeefe_nadel_1978]: https://academic.oup.com/book/1050
[book_rumelhart_mcclelland_1986]: https://mitpress.mit.edu/9780262680530/parallel-distributed-processing/
[book_sutton_barto_1998]: https://mitpress.mit.edu/9780262039246/reinforcement-learning/
[book_sutton_barto_2018]: http://incompleteideas.net/book/the-book-2nd.html
[book_wiener_1948]: https://mitpress.mit.edu/9780262537841/cybernetics/
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
[related_post_a261_evolutionary]: {% post_url 2025-12-29-machines_that_learn_from_experience_evolutionary_and_open_ended_adaptation %}
[related_post_a262_embodied]: {% post_url 2025-12-30-machines_that_learn_from_experience_embodied_cognition_and_developmental_learning %}
[research_ackley_hinton_sejnowski_1985]: https://doi.org/10.1207/s15516709cog0901_7
[research_anderson_1996_act_r]: https://doi.org/10.1037/0003-066x.51.4.355
[research_antonello_et_al_2024]: https://openreview.net/forum?id=xI71dsS3o4
[research_antonello_et_al_2024_a263]: https://openreview.net/forum?id=xI71dsS3o4
[research_bahdanau_cho_bengio_2015]: https://doi.org/10.48550/arxiv.1409.0473
[research_banino_et_al_2018_grid]: https://doi.org/10.1038/s41586-018-0102-6
[research_barlow_1961_efficient]: https://scholar.google.com/scholar?q=barlow+1961+possible+principles+underlying+sensory+messages
[research_barto_sutton_anderson_1983]: https://ieeexplore.ieee.org/document/6313077
[research_bartunov_et_al_2018]: https://papers.nips.cc/paper/2018/hash/63c3ddcc7b23daa1e42dc41f9a44a873-Abstract.html
[research_behrens_et_al_2018_cognitive_maps]: https://www.cell.com/neuron/fulltext/S0896-6273(18)30856-6
[research_bell_sejnowski_1997]: https://doi.org/10.1016/s0042-6989(97)00121-1
[research_bellec_et_al_2020]: https://doi.org/10.1038/s41467-020-17236-y
[research_bellemare_et_al_2017_distributional]: https://doi.org/10.1609/aaai.v32i1.11791
[research_bengio_et_al_2015_targetprop]: https://scholar.google.com/scholar?q=Target+Prop+Bengio+2015
[research_bengio_fischer_mesnard_2015]: https://doi.org/10.48550/arxiv.1502.04156
[research_binz_schulz_2023]: https://doi.org/10.1073/pnas.2218523120
[research_botvinick_et_al_2019_rl_fast_slow]: https://doi.org/10.1016/j.tics.2019.02.006
[research_buzsaki_moser_2013]: https://doi.org/10.1038/nn.3304
[research_cadena_et_al_2019]: https://doi.org/10.1371/journal.pcbi.1006897
[research_caucheteux_king_2022]: https://doi.org/10.1038/s42003-022-03036-1
[research_chang_tsao_2017]: https://doi.org/10.1016/j.cell.2017.05.011
[research_chung_abbott_2021]: https://doi.org/10.1016/j.conb.2021.10.010
[research_chung_lee_sompolinsky_2018]: https://doi.org/10.1103/physrevx.8.031003
[research_cichy_et_al_2019_algonauts]: https://doi.org/10.48550/arxiv.1905.05675
[research_coda_forno_et_al_2023]: https://doi.org/10.52202/075280-2844
[research_cueva_wei_2018]: https://openreview.net/forum?id=B17JTOe0-
[research_cunningham_yu_2014]: https://doi.org/10.1038/nn.3776
[research_dabney_et_al_2020_dopamine]: https://doi.org/10.1038/s41586-019-1924-6
[research_davies_et_al_2018_loihi]: https://ieeexplore.ieee.org/document/8259423
[research_daw_et_al_2011]: https://doi.org/10.1016/j.neuron.2011.02.027
[research_dayan_1993_sr]: https://doi.org/10.1162/neco.1993.5.4.613
[research_desimone_duncan_1995]: https://doi.org/10.1146/annurev.ne.18.030195.001205
[research_doerig_et_al_2023]: https://doi.org/10.1038/s41583-023-00705-w
[research_doya_2000]: https://doi.org/10.1162/089976600300015961
[research_duan_et_al_2016_rl2_a263]: https://doi.org/10.48550/arxiv.1611.02779
[research_eliasmith_et_al_2012_spaun]: https://doi.org/10.1126/science.1225266
[research_elman_1990_srn]: https://doi.org/10.1207/s15516709cog1402_1
[research_eshel_et_al_2015]: https://doi.org/10.1038/nature14855
[research_foster_wilson_2006_a263]: https://doi.org/10.1038/nature04587
[research_fukushima_1980_neocognitron]: https://doi.org/10.1007/bf00344251
[research_gallego_et_al_2017]: https://doi.org/10.1016/j.neuron.2017.05.025
[research_giovannucci_et_al_2019_caiman]: https://doi.org/10.7554/elife.38173
[research_goldstein_et_al_2022]: https://doi.org/10.1038/s41593-022-01026-4
[research_graves_et_al_2016_dnc]: https://doi.org/10.1038/nature20101
[research_graves_wayne_danihelka_2014_ntm]: https://doi.org/10.48550/arxiv.1410.5401
[research_guerguiev_lillicrap_richards_2017]: https://doi.org/10.7554/elife.22901
[research_hafting_et_al_2005_grid]: https://doi.org/10.1038/nature03721
[research_hassabis_et_al_2017]: https://doi.org/10.1016/j.neuron.2017.06.011
[research_hopfield_1982]: https://doi.org/10.1073/pnas.79.8.2554
[research_hubel_wiesel_1962]: https://doi.org/10.1113/jphysiol.1962.sp006837
[research_indiveri_liu_delbruck_2015]: https://ieeexplore.ieee.org/document/7108440
[research_izhikevich_edelman_2008]: https://doi.org/10.1073/pnas.0712231105
[research_jain_huth_2018]: https://papers.nips.cc/paper_files/paper/2018/hash/f471223d1a1614b58a7dc45c9d01df19-Abstract.html
[research_ji_wilson_2007]: https://doi.org/10.1038/nn1825
[research_kell_et_al_2018]: https://doi.org/10.1016/j.neuron.2018.03.044
[research_king_dehaene_2014]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(14)00047-X
[research_konkle_alvarez_2022]: https://doi.org/10.1038/s41467-022-28091-4
[research_kriegeskorte_2015]: https://doi.org/10.1146/annurev-vision-082114-035447
[research_krizhevsky_sutskever_hinton_2012]: https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
[research_ku_et_al_2024]: https://scholar.google.com/scholar?q=LLM+Cognitive+Ku+2024
[research_kubilius_et_al_2019_cornet]: https://doi.org/10.1101/408385
[research_kumaran_hassabis_mcclelland_2016_a263]: https://doi.org/10.1016/j.tics.2016.05.004
[research_lecun_et_al_1989]: https://doi.org/10.1162/neco.1989.1.4.541
[research_lillicrap_et_al_2016_feedback]: https://doi.org/10.1038/ncomms13276
[research_lillicrap_et_al_2020]: https://doi.org/10.1038/s41583-020-0277-3
[research_lindsay_2020_attention]: https://doi.org/10.3389/fncom.2020.00029
[research_louie_wilson_2001]: https://doi.org/10.1016/s0896-6273(01)00186-6
[research_maass_1997]: https://doi.org/10.1016/s0893-6080(97)00011-7
[research_mante_et_al_2013]: https://doi.org/10.1038/nature12742
[research_marblestone_wayne_kording_2016]: https://doi.org/10.3389/fncom.2016.00094
[research_marcus_2020_next_decade]: https://doi.org/10.48550/arxiv.2002.06177
[research_markram_2006_blue_brain]: https://doi.org/10.1038/nrn1848
[research_mattar_daw_2018_a263]: https://doi.org/10.1038/s41593-018-0232-z
[research_mcclelland_mcnaughton_oreilly_1995_a263]: https://doi.org/10.1037/0033-295x.102.3.419
[research_mcculloch_pitts_1943]: https://doi.org/10.1007/bf02478259
[research_merolla_et_al_2014_truenorth]: https://doi.org/10.1126/science.1254642
[research_millet_et_al_2022]: https://papers.nips.cc/paper_files/paper/2022/hash/d81ecfc8fb18e833a3fa0a35d92532b8-Abstract-Conference.html
[research_momennejad_et_al_2017]: https://doi.org/10.1038/s41562-017-0180-8
[research_nayebi_et_al_2018]: https://papers.nips.cc/paper/2018/hash/6be93f7a96fed60c477d30ae1de032fd-Abstract.html
[research_neftci_mostafa_zenke_2019]: https://ieeexplore.ieee.org/document/8891809
[research_niv_2009]: https://doi.org/10.1016/j.jmp.2008.12.005
[research_nokland_2016]: https://papers.nips.cc/paper/2016/hash/d490d7b4576290fa60eb31b5fc917ad1-Abstract.html
[research_oecd_neurotechnology_2019]: https://www.oecd.org/en/topics/sub-issues/emerging-technologies/neurotechnology.html
[research_oja_1982]: https://doi.org/10.1007/bf00275687
[research_okeefe_dostrovsky_1971]: https://doi.org/10.1016/0006-8993(71)90358-1
[research_olshausen_field_1996]: https://doi.org/10.1038/381607a0
[research_pachitariu_et_al_2016_kilosort]: https://doi.org/10.1101/061481
[research_pandarinath_et_al_2018_lfads]: https://doi.org/10.1038/s41592-018-0109-9
[research_payeur_et_al_2021]: https://doi.org/10.1038/s41593-021-00857-x
[research_pei_et_al_2021_nlb]: https://openreview.net/forum?id=KVMS3fl4Rsv
[research_rajan_abbott_2006]: https://doi.org/10.1103/physrevlett.97.188104
[research_reynolds_chelazzi_2004]: https://doi.org/10.1146/annurev.neuro.26.041002.131039
[research_richards_et_al_2019]: https://doi.org/10.1038/s41593-019-0520-2
[research_riesenhuber_poggio_1999_hmax]: https://doi.org/10.1038/14819
[research_rosenblatt_1958]: https://doi.org/10.1037/h0042519
[research_rumelhart_hinton_williams_1986]: https://doi.org/10.1038/323533a0
[research_sacramento_et_al_2018]: https://papers.nips.cc/paper/2018/hash/1dc3a89d0d440ba31729b0ba74b93a33-Abstract.html
[research_scellier_bengio_2017]: https://doi.org/10.3389/fncom.2017.00024
[research_schrimpf_et_al_2020_brainscore]: https://www.biorxiv.org/content/10.1101/407007v2
[research_schrimpf_et_al_2021_language]: https://doi.org/10.1073/pnas.2105646118
[research_schultz_dayan_montague_1997]: https://doi.org/10.1126/science.275.5306.1593
[research_sejnowski_rosenberg_1987]: https://scholar.google.com/scholar?q=NETtalk+Sejnowski+Rosenberg+1987
[research_simoncelli_olshausen_2001]: https://doi.org/10.1146/annurev.neuro.24.1.1193
[research_song_et_al_2020_pc_backprop]: https://papers.nips.cc/paper/2020/hash/fec87a37cdeec1c6ecf8181c0aa2d3bf-Abstract.html
[research_song_yang_wang_2016]: https://doi.org/10.1371/journal.pcbi.1004792
[research_sorscher_et_al_2019]: https://papers.nips.cc/paper_files/paper/2019/hash/6e7d5d259be7bf56ed79029c4e621f44-Abstract.html
[research_stachenfeld_botvinick_gershman_2017]: https://doi.org/10.1038/nn.4650
[research_steinberg_et_al_2013]: https://doi.org/10.1038/nn.3413
[research_sussillo_barak_2013]: https://doi.org/10.1162/neco_a_00409
[research_sussillo_et_al_2015]: https://doi.org/10.1038/nn.4042
[research_sutton_1988_td_a263]: https://doi.org/10.1007/bf00115009
[research_toneva_wehbe_2019]: https://papers.nips.cc/paper_files/paper/2019/hash/749a8e6c231831ef7756db230b4359c8-Abstract.html
[research_turing_1950]: https://doi.org/10.1093/mind/lix.236.433
[research_ullman_2023]: https://doi.org/10.48550/arxiv.2302.08399
[research_vaswani_et_al_2017]: https://papers.nips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html
[research_vinje_gallant_2000]: https://doi.org/10.1126/science.287.5456.1273
[research_vyas_et_al_2020]: https://doi.org/10.1146/annurev-neuro-092619-094115
[research_wang_2002_working_memory]: https://scholar.google.com/scholar?q=Working+Memory+Wang+2002
[research_wang_et_al_2016_l2rl_a263]: https://doi.org/10.48550/arxiv.1611.05763
[research_wang_et_al_2018_prefrontal_meta_a263]: https://doi.org/10.1038/s41593-018-0147-8
[research_watkins_1989_thesis_a263]: https://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf
[research_werbos_1974]: https://scholar.google.com/scholar?q=werbos+1974+beyond+regression
[research_whittington_bogacz_2019]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(18)30284-X
[research_whittington_bogacz_2019_a263]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(18)30284-X
[research_whittington_et_al_2020_tem]: https://doi.org/10.1016/j.cell.2020.10.024
[research_widrow_hoff_1960]: https://apps.dtic.mil/sti/citations/AD0241531
[research_willeke_et_al_2022_sensorium]: https://doi.org/10.48550/arxiv.2206.08666
[research_yamins_dicarlo_2016]: https://doi.org/10.1038/nn.4244
[research_yamins_et_al_2014]: https://doi.org/10.1073/pnas.1403112111
[research_yang_et_al_2019]: https://doi.org/10.1038/s41593-018-0310-2
[research_yuste_et_al_2017_neurorights]: https://doi.org/10.1038/551159a
[research_zador_et_al_2023]: https://doi.org/10.1038/s41467-023-37180-x
[research_zhuang_et_al_2021]: https://doi.org/10.1073/pnas.2014196118
