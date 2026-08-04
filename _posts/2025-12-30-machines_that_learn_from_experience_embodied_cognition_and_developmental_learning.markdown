---
layout: post
mathjax: true
comments: true
title:  "Machines That Learn From Experience: Embodied Cognition and Developmental Learning"
date:   2025-12-30 00:00:00 +0000
categories: artificial-intelligence machine-learning neuroscience
series: machines_that_learn_from_experience
series_title: Machines That Learn From Experience
series_index: 13
---

<!-- A262 -->
<script>console.log("A262");</script>

Embodied cognition and developmental learning frame intelligence as arising from the coupling between an agent's body, its environment, and its history of interaction across development. The framework departs from the disembodied representation-and-inference view of classical artificial intelligence by treating cognition as fundamentally shaped by the sensorimotor loop, by the physical constraints of the body, and by the progression through developmental stages that scaffold increasingly sophisticated capabilities. The account has proved valuable for robotic control where physical embodiment shapes what can be perceived and produced, for developmental psychology where the trajectory of human learning provides both empirical constraints and computational guidance, and for artificial systems that must acquire competence through interaction rather than through pretrained representations. This article surveys the science and theory of embodied cognition and developmental learning as they stand in the mid 2020s. Coverage includes the philosophical foundations of embodied cognition from Merleau-Ponty through the modern enactive framework, sensorimotor contingency theory, developmental robotics, intrinsic motivation and curiosity as drivers of development, emotion and affect in development, motor development and sensorimotor learning, play and object manipulation development, perceptual development and statistical learning, Piagetian constructivism and stage theory, executive function and cognitive control development, core knowledge and innate priors, symbol grounding and language development, predictive coding and active inference, morphological computation and body schema, curriculum learning and developmental trajectories, social development and joint attention, self-recognition and the development of agency, comparative developmental cognition across species, embodied foundation models and simulation environments, theoretical frameworks including ecological psychology, dynamical systems, and neuroconstructivism, empirical benchmarks, and the neuroscience correspondence to cortical development, critical periods, and sensitive-period plasticity. Article twelve treated evolutionary and open-ended adaptation across generations. The present article treats adaptation across a single lifetime through the developmental mechanisms that scaffold human and artificial cognitive development.

## The Embodied Cognition and Developmental Learning Problem

Embodied cognition posits that intelligent behavior arises from the interactions between a body, a nervous system, and an environment, rather than from the manipulation of abstract symbolic representations divorced from physical instantiation. Formally, the embodied agent is specified by a triple $(\mathcal{B}, \mathcal{N}, \mathcal{E})$ of body, nervous system, and environment, with sensorimotor coupling defined through the observation and action functions

$$o_t = \Omega(\mathcal{B}, \mathcal{E}, s_t^{\mathcal{E}}), \quad a_t = A(\mathcal{N}, o_t, s_t^{\mathcal{N}})$$

where $s_t^{\mathcal{E}}$ is the environmental state, $s_t^{\mathcal{N}}$ is the nervous system state, $\Omega$ maps the state through the body's sensory apparatus, and $A$ produces motor output through the body's actuators. The model emphasizes that both the sensory mapping $\Omega$ and the action mapping $A$ depend considerably on the physical body, and that cognition cannot be studied in abstraction from these embodied constraints.

Developmental learning treats the trajectory of capability acquisition across a single lifetime. Formally, the developmental state at time $t$ depends on the full history of sensorimotor experience,

$$\phi_t = D(\phi_0, o_{1:t-1}, a_{1:t-1}, \theta_{\text{intrinsic}})$$

where $\phi_t$ is the developmental state, $D$ is the developmental transition function, $\phi_0$ is the initial state, and $\theta_{\text{intrinsic}}$ parameterizes the intrinsic drives that shape exploration. This formulation provides a temporal dimension that the standard machine learning framing lacks. A developmental system passes through stages characterized by distinct sensory capabilities, motor repertoires, cognitive strategies, and social competences, with each stage building on and reorganizing the capabilities of prior stages.

The two frameworks are complementary and mutually reinforcing. Embodied cognition provides the theoretical framework for understanding why the structural properties of the body and environment matter for cognition. Developmental learning provides the temporal framework for understanding how sophisticated cognitive capabilities emerge from simpler precursors through structured interaction. Modern developmental robotics combines both perspectives to design artificial systems that progressively acquire capabilities through the exploration of the sensorimotor space.

The treatment contrasts with several assumptions that organize much of the preceding series. The independent-identically-distributed sampling assumption of standard machine learning does not hold for developmental agents whose experience is deeply structured by their current capabilities. The pretrained-and-fine-tuned paradigm of foundation models does not directly address the temporal structure of developmental capability emergence. The reinforcement learning framing of reward maximization does not directly capture the intrinsic-motivation-driven exploration that characterizes early development.

This account also raises methodological questions distinct from other machine learning sub-fields. What is the correct benchmark for developmental progress? How should the intrinsic-versus-extrinsic reward structure be organized to support developmental progress rather than either random exploration or premature exploitation? What is the role of physical embodiment versus simulated embodiment in learning? These questions organize considerable ongoing research and admit distinctive algorithmic responses that connect developmental learning to the intrinsic-motivation treatments of article five and to the curriculum-learning treatments of articles nine and twelve.

## Historical Development

Embodied cognition emerged as a distinct research program in the 1980s and 1990s in reaction to the disembodied symbolic-AI framework that dominated the prior decades. The [Brooks 1991][research_brooks_1991_intelligence] Intelligence without Representation and the earlier [Brooks 1990][research_brooks_1990_elephants] critique of symbolic AI provided the foundational modern statements of the position that intelligent behavior arises from the physical coupling of a body to an environment without the need for centralized symbolic representation.

The [Varela Thompson Rosch 1991][book_varela_thompson_rosch_1991] The Embodied Mind consolidated the philosophical framework by combining phenomenological, cognitive-scientific, and Buddhist-contemplative traditions into a unified account of embodied cognition. The [Clark 1997][book_clark_1997] Being There provided the systematic treatment of embodied cognition for cognitive science and philosophy of mind, and the [Clark and Chalmers 1998][research_clark_chalmers_1998] Extended Mind hypothesis provided the extension to environmentally-scaffolded cognition.

Sensorimotor contingency theory of [O'Regan and Noë 2001][research_oregan_noe_2001] introduced the proposal that perceptual experience is constituted by the patterns of sensorimotor dependencies that characterize an organism's interaction with the environment. The framework provided a concrete alternative to representationalist accounts of perception.

Developmental robotics emerged as a distinct sub-field through the [Weng McClelland Pentland Sporns Stockman Sur Thelen 2001][research_weng_et_al_2001] autonomous mental development framework and the [Lungarella Metta Pfeifer Sandini 2003][research_lungarella_et_al_2003] developmental robotics survey. The [Cangelosi and Schlesinger 2015][book_cangelosi_schlesinger_2015] Developmental Robotics textbook consolidated the field and established the systematic taxonomy that continues to organize the modern literature.

Piagetian constructivism of [Piaget 1952][book_piaget_1952] and the subsequent developmental psychology literature provided the empirical framework for stages of cognitive development in children. Core knowledge accounts of [Spelke 1994][research_spelke_1994] and [Spelke and Kinzler 2007][research_spelke_kinzler_2007] extended the model with proposals about the innate cognitive structures that scaffold early development.

Intrinsic motivation as a driver of development matured through the [Schmidhuber 1991][research_schmidhuber_1991_curiosity] curiosity framework, the [Oudeyer Kaplan Hafner 2007][research_oudeyer_kaplan_hafner_2007] intrinsic motivation systems, and the [Baldassarre and Mirolli 2013][book_baldassarre_mirolli_2013] Intrinsically Motivated Learning in Natural and Artificial Systems edited volume. The model connects developmental robotics to the exploration and intrinsic-motivation treatments of article five.

Predictive coding and active inference emerged as unified theoretical frameworks through the [Rao and Ballard 1999][research_rao_ballard_1999] hierarchical predictive coding proposal and the [Friston 2010][research_friston_2010_fep] free energy principle. The frameworks provide computational-level theories of perception, action, and learning that unify significant portions of the embodied-cognitive-developmental literature.

The 2020s produced substantial diversification including foundation-model-scale embodied learning, large-scale simulation environments, and cross-embodiment learning at deployment scale. The [Oudeyer 2018][research_oudeyer_2018_devrob] developmental robotics survey and the [Cangelosi and Asada 2022][book_cangelosi_asada_2022] Cognitive Robotics consolidated the modern practical and theoretical developments.

## Foundations of Embodied Cognition

The embodied cognition framework rests on several complementary claims that distinguish it from the classical disembodied cognitive science tradition. The first claim is that cognitive processes are constituted by the structural properties of the body. Perception is shaped by the sensory apparatus, action is shaped by the actuator repertoire, and the coupling between the two is shaped by the morphology that determines how sensory and motor systems interact.

The second claim is that cognition is fundamentally situated in an environment that provides both the perceptual affordances and the action possibilities that structure behavior. Environments are not neutral backdrops for cognition but active participants in the cognitive processes that occur within them. The [Gibson 1979][book_gibson_1979] Ecological Approach to Visual Perception introduced the affordance framework in which objects and environments directly present action possibilities to the perceiving organism without the need for intervening symbolic representation. Formally, an affordance is a relation

$$\text{Aff}(o, \mathcal{B}) = \{a \in \mathcal{A} \, : \, p(\text{success}(a, o) \mid \mathcal{B}) > \tau\}$$

between the perceived object or environment $o$ and the body $\mathcal{B}$, specifying the actions $a$ that the body can successfully execute given the object with probability above threshold $\tau$. This formulation has been implemented computationally in the affordance-learning frameworks that estimate action-outcome distributions from embodied interaction data.

The third claim is that cognition is enactive rather than representational. The [Varela Thompson Rosch 1991][book_varela_thompson_rosch_1991] enactive framework proposed that cognition consists in the bringing-forth of a world through the patterns of sensorimotor interaction rather than in the internal representation of an independently-existing external world. The formal instantiation treats agent and environment as coupled dynamical systems

$$\dot{s}_{\mathcal{A}} = f_{\mathcal{A}}(s_{\mathcal{A}}, s_{\mathcal{E}}), \quad \dot{s}_{\mathcal{E}} = f_{\mathcal{E}}(s_{\mathcal{E}}, s_{\mathcal{A}})$$

with the agent's cognitive state $s_{\mathcal{A}}$ and the environmental state $s_{\mathcal{E}}$ evolving under mutually-conditioning dynamics. Cognition consists in the pattern of coupled trajectories rather than in the representation of one system by the other.

The Merleau-Ponty phenomenological framework provided the philosophical grounding for the embodied cognition tradition through the [Merleau-Ponty 1945][book_merleau_ponty_1945] Phenomenology of Perception. The treatment identified the body-subject as the fundamental locus of cognitive activity and provided the conceptual apparatus that subsequent embodied cognitive science elaborated in computational terms.

The extended mind hypothesis of Clark and Chalmers 1998 extended the model to environmentally-scaffolded cognition. Cognitive processes are not confined to the biological brain but extend into the environment through the use of external tools, notation systems, and social interactions that participate in cognitive computation. This account has significantly shaped subsequent theoretical discussions of cognition in artificial systems, particularly with respect to the role of external tools and language in scaffolding capability.

Situated cognition of [Suchman 1987][book_suchman_1987] provided the complementary treatment through the analysis of how situated action differs from planned action, providing empirical grounding for the embodied cognition claims through detailed studies of human interaction with technology. The [Wilson 2002][research_wilson_2002_six_views] Six Views of Embodied Cognition provided the influential taxonomy that distinguishes the claims within the embodied cognition literature and enables systematic empirical evaluation. The [Anderson 2003][research_anderson_2003_field_guide] Embodied Cognition Field Guide consolidated the diverse empirical and theoretical strands into a systematic overview. The [Barsalou 2008][research_barsalou_2008_grounded] Grounded Cognition review consolidated the empirical evidence for the claims of grounded cognitive processing, providing quantitative evidence from behavioral and neuroimaging studies.

Radical embodied cognitive science of [Chemero 2009][book_chemero_2009] provided the systematic philosophical treatment through the argument that cognition can be understood entirely through dynamical-systems and ecological-psychological frameworks without recourse to representational states. The autopoiesis framework of [Maturana and Varela 1980][book_maturana_varela_1980] provided the foundational biological framework in which living systems are characterized by the self-producing organization that supports subsequent cognitive activity, and this formulation has substantially shaped the enactive tradition through the shared emphasis on self-organizing dynamics.

The relationship between embodied cognition and classical symbolic cognitive science remains an active philosophical question. Modern positions include reconciliationist views that treat symbolic and embodied processes as complementary levels of description, replacement views that treat embodied cognition as superseding symbolic accounts, and hybrid views that treat both frameworks as capturing distinct aspects of cognition that must be jointly modeled.

## Sensorimotor Contingency and Enactive Cognition

Sensorimotor contingency theory of O'Regan and Noë 2001 proposed that perceptual experience is constituted by the patterns of sensorimotor dependencies that characterize an organism's interaction with the environment. The model provided a concrete alternative to representationalist accounts of perception.

Formally, the sensorimotor contingency of a modality is the mapping from motor actions to sensory changes conditional on the current sensory state,

$$C_M(a, o_t) = \mathbb{E}[o_{t+1} - o_t \mid a_t = a, o_t]$$

with $C$ describing how the observation changes as a function of the action taken. Different modalities are characterized by distinct sensorimotor contingencies. Vision exhibits a pattern in which eye movements produce systematic changes in the retinal image consistent with the geometry of the three-dimensional world. Audition exhibits a different pattern in which head movements produce interaural time and level differences consistent with the geometry of sound sources.

This formulation predicts that perceptual experience emerges from the mastery of these sensorimotor contingencies rather than from the passive registration of sensory information. The mastery criterion can be formalized as the achievement of low predictive error on the contingency mapping,

$$\text{Mastery}(M) = -\mathbb{E}_{a, o}\!\left[\|C_M(a, o) - \hat{C}_M(a, o; \theta)\|^2\right]$$

with $\hat{C}_M(\cdot; \theta)$ the agent's learned model of the modality-contingencies. Empirical support includes studies of sensory substitution in which subjects trained with a tactile-to-visual sensory substitution device report perceptual experiences consistent with the sensorimotor contingencies of the substituting modality. Sensory substitution of [Bach-y-Rita 1969][research_bach_y_rita_1969] pioneered the empirical framework through the tactile-visual substitution device that enabled congenitally-blind subjects to acquire visual-like perception through tactile stimulation of the back. The [Kohler 1962][research_kohler_1962] inverted-vision experiments provided the complementary empirical framework by documenting the adaptation to systematically-distorted visual input over extended wearing of inverting goggles.

The [Noë 2004][book_noe_2004] Action in Perception provided the systematic philosophical treatment of sensorimotor contingency theory and connected it to the broader phenomenological tradition. The treatment identifies the ways in which perception is constituted by embodied know-how rather than by passive representation.

The enactive framework of Varela Thompson Rosch 1991 generalized this formulation to the proposal that cognition is the emergence of a meaningful world through the patterns of embodied interaction. This account rejects the classical assumption of a pregiven world that is subsequently represented, proposing instead that the cognitive agent and its environment coemerge through the ongoing patterns of structural coupling.

The [Thompson 2007][book_thompson_2007] Mind in Life extended the framework to a systematic treatment of the biological, cognitive, and phenomenological dimensions of enactive cognition. The account connects embodied cognition to the philosophy of biology through the concept of autopoiesis, the self-organizing patterns that constitute living systems.

Modern computational implementations of sensorimotor contingency include the developmental frameworks that treat perceptual learning as the acquisition of sensorimotor prediction models. The [Philipona O'Regan Nadal 2003][research_philipona_oregan_nadal_2003] work on the physical determination of the sensorimotor structure of perceptual modalities provided the mathematical framework for the discovery of the geometric structure of sensory space through motor exploration. The dimensionality of the compensatable subspace matches the number of external spatial degrees of freedom,

$$\dim(\ker(J_M - J_B)) = d_{\text{space}}$$

where $J_M$ is the Jacobian of the sensory response to motor commands and $J_B$ is the Jacobian of the sensory response to body-external motion. The equality supports the discovery of the geometric structure of space through sensorimotor exploration alone.

Enactive cognition connects to modern predictive coding and active inference frameworks through the shared emphasis on the patterns of sensorimotor coupling as the substrate of cognition. This formulation provides the philosophical grounding for computational implementations that treat perception and action as unified processes rather than as separate cognitive faculties.

## Developmental Robotics

Developmental robotics treats the problem of designing artificial systems that progressively acquire capabilities through interaction with their environment, following the general trajectory of biological development. The treatment combines robotics with developmental psychology to produce systems that autonomously develop increasingly sophisticated behaviors.

The Weng et al 2001 autonomous mental development framework introduced the systematic approach through the proposal that intelligent behavior should emerge from the interaction of an autonomous learning system with its environment, without task-programming. This account identified developmental principles including the need for continual learning, self-supervised representation development, and the systematic progression from simpler to more complex tasks.

The Lungarella et al 2003 developmental robotics survey consolidated the early literature and identified the research areas that continue to organize the field. The survey identified sensorimotor development, cognitive development, and social development as the three complementary tracks that developmental robotics must address.

Modern developmental robotics has produced marked empirical and theoretical progress through several research programs. The iCub humanoid platform of [Metta Sandini Vernon Natale Nori 2008][research_metta_et_al_2008_icub] provided the hardware platform that has enabled extensive developmental robotics research. The platform's small child-like form factor and sensorimotor capabilities support the kinds of interactions that mirror early human development.

The Playful of [Baranes and Oudeyer 2013][research_baranes_oudeyer_2013_playful] framework introduced robust intrinsically motivated exploration for developmental robotics, providing an approach that autonomously discovers task structure through the mechanism of learning-progress-based intrinsic motivation. The framework produces developmental trajectories that mirror the patterns of exploration observed in human infants.

Intrinsically Motivated Goal Exploration Processes (IMGEP) of [Forestier Portelas Mollard Oudeyer 2022][research_forestier_et_al_2022_imgep] provided the general computational framework for autonomous goal-generation in developmental agents. The account maintains an archive of previously-encountered goals and generates new goals through mutation and diversification. At each iteration the agent samples a target behavioral outcome $g$ from a goal-generation distribution, executes a policy $\pi_\theta$ conditioned on the goal, and updates both the policy and the archive with the achieved outcome,

$$g \sim p_{\text{goal}}(\cdot \mid \mathcal{A}_t), \quad \tau \sim \pi_\theta(\cdot \mid g), \quad \mathcal{A}_{t+1} = \mathcal{A}_t \cup \{(g, b(\tau))\}$$

where $\mathcal{A}_t$ is the goal-outcome archive and $b(\tau)$ is the behavioral descriptor of the executed trajectory. The model provides an approach that connects developmental robotics to the quality-diversity treatments of article twelve.

The Oudeyer 2018 developmental robotics survey provided the modern consolidation of the field and identified the research directions that connect developmental robotics to modern machine learning practice. This formulation treats developmental robotics as a application of the general principles that unify meta-learning, curriculum learning, intrinsic motivation, and self-supervised learning. The [Asada MacDorman Ishiguro Kuniyoshi 2001][research_asada_et_al_2001_cognitive_dev] cognitive developmental robotics framework provided one of the earlier systematic treatments of the field, and the subsequent [Asada Hosoda Kuniyoshi Ishiguro Inui Yoshikawa Ogino Yoshida 2009][research_asada_et_al_2009] survey consolidated the modern research program.

Autotelic agents of [Colas Karch Sigaud Oudeyer 2022][research_colas_et_al_2022_autotelic] provided the modern systematic framework for developmental agents that autonomously construct their own goals. The treatment consolidates the intrinsic-motivation, goal-generation, and language-conditioned literatures into a unified developmental account that connects to the modern foundation-model-mediated evolutionary methods treated in article twelve.

Contemporary developmental robotics increasingly leverages foundation-model-scale simulation environments and language-model-mediated task specification. This account connects developmental robotics to the modern trends in embodied artificial intelligence and provides a research bridge between the classical developmental cognitive science literature and the modern deep learning practice.

## Intrinsic Motivation and Curiosity in Development

Intrinsic motivation provides the mechanism through which developmental agents autonomously select tasks and explore their capability space. The framework connects developmental robotics to the exploration treatments of article five and provides the driver for the developmental progression from simpler to more complex capabilities. The psychological foundations of intrinsic motivation include the [White 1959][research_white_1959] effectance motivation framework in which mastery motivation is proposed as a distinct drive complementary to biological needs, the [Berlyne 1960][book_berlyne_1960] Conflict Arousal and Curiosity systematic treatment of exploratory behavior, and the [Ryan and Deci 2000][research_ryan_deci_2000] self-determination theory that provided the modern psychological framework for intrinsic and extrinsic motivation. The [Barto 2013][research_barto_2013] intrinsic motivation and reinforcement learning review consolidated the computational reinforcement learning perspective on intrinsic motivation.

The Schmidhuber 1991 curiosity framework introduced the proposal that intrinsic motivation corresponds to the reduction of prediction error in a learned world model. The subsequent [Schmidhuber 2010][research_schmidhuber_2010_formal] formal theory of creativity, fun, and intrinsic motivation extended the account with the computational characterization of the drivers of exploration and creativity.

The Oudeyer Kaplan Hafner 2007 intrinsic motivation systems framework provided the systematic taxonomy of intrinsic motivation mechanisms including novelty, learning progress, and empowerment. The learning-progress signal quantifies the recent improvement in prediction error over a sliding window,

$$\text{LP}(x) = \|\epsilon_{t-w}(x)\| - \|\epsilon_t(x)\|$$

with $\epsilon_t(x)$ the current-model prediction error on task or region $x$ and $\|\cdot\|$ a suitable norm. The learning-progress-based framework has proved particularly influential in developmental robotics through its prediction that developmental agents should preferentially explore states where learning is neither too easy nor too hard.

The Baldassarre and Mirolli 2013 Intrinsically Motivated Learning in Natural and Artificial Systems edited volume consolidated the field and provided the systematic treatment of intrinsic motivation across artificial and biological systems. The model identifies the relationships between intrinsic motivation, developmental progression, and the emergence of sophisticated capabilities.

Modern intrinsic-motivation-based developmental agents produce trajectories that qualitatively mirror the patterns observed in human infants. This formulation predicts developmental progressions including the initial focus on high-learning-progress tasks, the subsequent transition to increasingly-complex tasks as prior tasks are mastered, and the eventual disengagement from mastered tasks in favor of more challenging alternatives.

Empowerment-based intrinsic motivation of [Klyubin Polani Nehaniv 2005][research_klyubin_polani_nehaniv_2005_empowerment] introduced the information-theoretic framework in which agents maximize their potential influence on future observations. Empowerment is formally defined as the channel capacity between action sequences and future states,

$$E(s) = \max_{p(a_{1:n})} \, \mathbb{I}\!\left[A_{1:n} \, ; \, S_{n+1} \mid S_1 = s\right]$$

with the maximization over the distribution of action sequences. The treatment has been applied to developmental robotics as an alternative to learning-progress-based motivation and produces distinctive developmental trajectories characterized by the systematic expansion of behavioral repertoire.

Curiosity-driven exploration in modern deep reinforcement learning connects developmental robotics to the algorithmic frameworks of article five. The Random Network Distillation, ICM, and RND methods of that treatment provide the modern computational instantiations of intrinsic motivation that scale to deep learning function approximation and to foundation-model-scale exploration.

The developmental progression driven by intrinsic motivation admits formal analysis through the framework of automatic curriculum learning. The developmental agent effectively constructs its own curriculum through the selection of tasks based on their current learning progress, and the resulting curriculum exhibits structural properties including the progressive introduction of complexity that mirrors the patterns observed in human development.

## Emotion, Affect, and Motivation in Development

Emotion and affect play roles in developmental learning that extend beyond intrinsic motivation. This account connects developmental cognition to affective neuroscience through the mechanisms by which emotional systems shape learning, memory, decision-making, and social interaction across development.

The [Damasio 1994][book_damasio_1994] Descartes' Error introduced the somatic marker hypothesis, proposing that emotional bodily signals shape decision-making through the mechanism of learned associations between behavioral outcomes and visceral emotional responses. The framework has sizable empirical support from studies of patients with prefrontal-cortex damage and provides the bridge between emotion and rational decision-making that classical accounts had treated as separate faculties.

Affective Neuroscience of [Panksepp 1998][book_panksepp_1998] provided the systematic treatment of the neural substrates of primary emotional systems including seeking, fear, rage, lust, care, panic, and play. The account identified the conserved subcortical circuits that support the primary affective processes and has markedly shaped subsequent comparative and developmental affective neuroscience.

The [Barrett 2017][book_barrett_2017] How Emotions Are Made framework provided the systematic constructionist alternative in which discrete emotional categories emerge through the combination of core affect (valence and arousal) with learned conceptual knowledge. The model connects emotion to categorization and prediction, providing the bridge to predictive-processing accounts of affect.

Emotional development follows a trajectory across infancy and childhood. The [Sroufe 1996][book_sroufe_1996] emotional development framework identified the developmental milestones including the emergence of primary emotions in early infancy, the emergence of self-conscious emotions in the second year, and the elaboration of emotion regulation capacities across childhood. This formulation provides the empirical grounding for the emotional developmental trajectory.

Temperament is the stable individual difference in affective responding that emerges early in development. The [Rothbart Ahadi Hershey 2001][research_rothbart_ahadi_hershey_2001] temperament framework identified the dimensions including surgency, negative affectivity, and effortful control that structure individual differences in emotional style. The treatment has appreciable empirical support and provides testable predictions about the developmental trajectories of different temperamental profiles.

The somatic marker hypothesis of [Damasio Everitt Bishop 1996][research_damasio_everitt_bishop_1996] provided the computational framework for the role of emotion in decision-making. This account proposes that emotional markers accumulated through experience bias decision-making through the mechanism of visceral signals that shape option evaluation. The framework has been extensively studied in patients with prefrontal-cortex lesions who fail on the decision-making tasks that require somatic-marker-based learning.

Affective computing frameworks including the [Picard 1997][book_picard_1997] Affective Computing foundational treatment introduced the engineering framework for artificial systems that recognize, express, and respond to human emotions. The account has been extensively applied to human-computer interaction, educational technology, and social robotics, and provides the engineering bridge between affective neuroscience and artificial intelligence.

Modern developmental robotics increasingly incorporates emotional and affective mechanisms as intrinsic motivational systems. The model connects affective computing to the developmental robotics treatments through the shared emphasis on the roles of affect and motivation in shaping developmental trajectories. Emotional mechanisms provide the evaluative substrate through which developmental agents assess the value of experiences and structure their exploration.

## Motor Development and Sensorimotor Learning

Motor development is the developmental track through which agents acquire sensorimotor capabilities. This formulation connects developmental robotics to the biomechanical and neurophysiological accounts of motor control in biological systems.

The Bernstein problem of [Bernstein 1967][book_bernstein_1967] identified the challenge of motor development as the coordination of the many degrees of freedom of the biological motor system. The problem is captured by the observation that the effective task-relevant dimensionality is typically appreciably smaller than the number of controllable degrees of freedom,

$$d_{\text{task}} = \dim(\mathcal{T}) \ll d_{\text{motor}} = \dim(\mathcal{U})$$

with $\mathcal{T}$ the task-relevant subspace and $\mathcal{U}$ the full motor-command space. The treatment predicts that motor development proceeds through the progressive freeing of degrees of freedom, from initial coactivation patterns to increasingly-refined coordinated control that projects motor commands into the task-relevant subspace.

Motor babbling of [Meltzoff and Moore 1997][research_meltzoff_moore_1997_babbling] provides the mechanism through which infants explore their motor repertoire through the systematic production of motor patterns and observation of their sensory consequences. This account produces the mapping from motor commands to sensory outcomes that supports subsequent goal-directed action.

Dynamic Movement Primitives (DMPs) of [Ijspeert Nakanishi Hoffmann Pastor Schaal 2013][research_ijspeert_et_al_2013_dmp_a262] provide the computational framework for representing motor skills through parameterized dynamical systems. The framework combines a canonical dynamical system that generates the timing structure with a learned forcing function that shapes the trajectory,

$$\ddot{y} = \alpha (\beta (g - y) - \dot{y}) + f(x)$$

where $y$ is the state, $g$ is the goal, $\alpha, \beta$ are dynamic parameters ensuring convergence, $f(x)$ is a learned forcing function, and $x$ is the phase variable that progresses from 1 to 0 over the movement. The account supports the properties of motor learning including generalization across goals, robust adaptation to perturbations, and modular composition of primitive movements.

The motor primitive hypothesis of [Mussa-Ivaldi and Solla 2004][research_mussa_ivaldi_solla_2004] proposed that biological motor behavior is composed of a small number of fundamental primitives that are combined through superposition to produce the full motor repertoire. Formally, complex motor output is generated through the weighted superposition of primitive fields,

$$u(t) = \sum_{i=1}^{K} w_i \, \phi_i(t)$$

with $\phi_i$ the $i$-th motor primitive, $w_i$ the task-weight, and $K$ the number of primitives in the repertoire. The model has considerable empirical support from studies of spinal cord organization and provides testable predictions about the structure of motor control.

Motor development in humans exhibits universal patterns including the cephalocaudal (head-to-tail) progression, the proximodistal (center-to-periphery) progression, and the milestones of head control, sitting, crawling, and walking. This formulation has provided computational inspiration for developmental robotics implementations that follow analogous progressions.

Predictive motor control frameworks including the [Wolpert Ghahramani Jordan 1995][research_wolpert_ghahramani_jordan_1995] forward-model account propose that motor control operates through the combination of a forward model that predicts sensory consequences of motor commands and an inverse model that generates motor commands from desired sensory outcomes. The forward model predicts the next sensory state as

$$\hat{s}_{t+1} = F_{\text{forward}}(s_t, u_t; \theta_F)$$

and the inverse model produces motor commands that achieve a desired sensory outcome,

$$\hat{u}_t = F_{\text{inverse}}(s_t, s_{t+1}^*; \theta_I)$$

with $\theta_F, \theta_I$ the learned parameters. Motor development corresponds to the joint learning of both models through the systematic exploration of the sensorimotor space. The treatment connects motor development to the predictive coding treatments below and to the world model treatments of article seven.

Modern deep learning implementations of motor development include the frameworks that combine differentiable motor primitives with deep reinforcement learning to produce policies that acquire complex motor skills through interaction. This account connects motor development to the modern policy-gradient methods of article three and to the imitation-learning methods of article eleven.

Optimal feedback control of [Todorov and Jordan 2002][research_todorov_jordan_2002_ofc] provided the theoretical framework for motor control in which the motor system minimizes a task-relevant cost function through feedback that operates only on task-relevant deviations. The framework provides quantitative fits to a broad range of human motor behavior and connects motor development to modern control theory. The [Shadmehr and Krakauer 2008][research_shadmehr_krakauer_2008] motor control computational neuroanatomy provided the systematic treatment of the neural substrates of motor learning, and the [Körding and Wolpert 2004][research_kording_wolpert_2004] Bayesian motor learning framework demonstrated that humans integrate prior expectations and sensory information optimally during motor learning.

## Play, Exploration Behavior, and Object Manipulation

Play is the class of behaviors characterized by self-motivated engagement, apparent purposelessness, and the systematic exploration of behavioral possibilities. The account connects developmental learning to a rich tradition in developmental psychology and ethology that identifies play as a central mechanism through which cognitive and behavioral capabilities develop.

The [Piaget 1962][book_piaget_1962_play] Play Dreams and Imitation in Childhood consolidated the developmental theory of play through the identification of three sequential play stages including practice play in the sensorimotor period, symbolic play in the preoperational period, and games-with-rules play in the concrete operational period. The model provides the developmental progression that computational models must reproduce.

The [Bruner 1972][research_bruner_1972_play] Nature and Uses of Immaturity framework identified the role of play in the extended human developmental period. This formulation argues that the human capacity for play is a consequence of the extended immaturity of human children and provides the mechanism through which humans acquire cultural and cognitive capabilities.

The [Pellegrini and Smith 1998][research_pellegrini_smith_1998] play review consolidated the modern developmental psychology framework and identified the functions of play across development. The treatment distinguishes locomotor play, object play, social play, and pretend play, and identifies the developmental trajectory and cognitive contributions of each play type.

Exploratory behavior in infants was systematically studied through the object-manipulation paradigms of [Ruff 1984][research_ruff_1984] and the significant subsequent literature. This account documents the developmental progression from initial mouthing and banging through increasingly-refined object manipulation that reveals the properties of objects through active exploration.

Playful of Baranes and Oudeyer 2013 introduced the computational framework for developmental robotics in which the agent engages in playful exploration of its sensorimotor space. The framework connects the classical play literature to modern developmental robotics through the shared emphasis on self-motivated exploration as a driver of developmental capability emergence.

Symbolic play in children emerges around age two and provides the bridge between sensorimotor and symbolic cognition. The account has been extensively studied both empirically and computationally, and provides developmental milestones that computational models of language and cognitive development must capture. Symbolic play involves the decoupling of action from goal, allowing objects to stand for other objects and actions to represent alternative outcomes.

Modern developmental robotics implementations of play include the frameworks that generate autonomous exploratory behaviors through intrinsic-motivation-driven goal selection. The model connects play to the goal-generation mechanisms treated in the developmental robotics and intrinsic motivation sections.

Object affordance learning through play provides the developmental mechanism through which infants acquire knowledge of object properties. This formulation connects affordance discovery to the sensorimotor exploration treatments and provides the empirical basis for the developmental trajectory of object knowledge that Piagetian and core-knowledge frameworks characterize.

## Perceptual Development and Statistical Learning

Perceptual development treats the track through which agents acquire perceptual capabilities from their sensory experience. The treatment connects developmental robotics to the psychology and neuroscience of perception development in biological systems.

Statistical learning in infants was documented systematically by [Saffran Aslin Newport 1996][research_saffran_aslin_newport_1996] through the demonstration that eight-month-old infants extract statistical regularities from continuous speech streams within just a few minutes of exposure. The statistic learned is the transitional probability between successive syllables,

$$P(y_{t+1} \mid y_t) = \frac{\#(y_t, y_{t+1})}{\#(y_t)}$$

with word boundaries corresponding to the local minima of the transitional probability. This account provides evidence that infants deploy powerful statistical inference mechanisms from the earliest ages and that these mechanisms scaffold subsequent language acquisition.

Visual development follows a trajectory characterized by rapid acuity improvement, the emergence of pattern preferences, the development of face processing, and the emergence of visual object recognition. The [Kellman and Arterberry 2006][book_kellman_arterberry_2006] Cradle of Knowledge consolidated the modern developmental visual perception literature and identified the developmental milestones that computational frameworks must capture. Foundational work by [Fantz 1961][research_fantz_1961] introduced the visual-preference paradigm through which infant visual capabilities have been systematically probed, and the [Kellman and Spelke 1983][research_kellman_spelke_1983] framework documented the infant capacity to perceive partly-occluded objects as unified wholes.

The [Aslin and Newport 2014][research_aslin_newport_2014] statistical learning review consolidated the modern developmental psychology framework and identified the mechanisms through which infant statistical learning supports subsequent language and cognitive development. The foundational neurophysiology of visual development was established by [Hubel and Wiesel 1970][research_hubel_wiesel_1970] through the documentation of critical-period plasticity in the mammalian visual cortex.

Multi-modal statistical learning of [Yu and Smith 2007][research_yu_smith_2007] introduced the cross-situational word-learning framework in which infants acquire word-referent mappings through the statistical regularities in co-occurrence across many labeling instances. The associative co-occurrence update after each labeling instance takes the form

$$\text{assoc}_{t+1}(w, r) = \text{assoc}_t(w, r) + \alpha \, \mathbb{1}[(w, r) \in \text{scene}_t]$$

with $\alpha$ a learning rate and the mapping candidates ranked by their accumulated associative strength. The framework provides evidence that the bootstrapping problem of language acquisition admits distributional solutions that infants deploy in practice.

Bayesian models of infant cognition of [Xu and Tenenbaum 2007][research_xu_tenenbaum_2007] proposed that infant learning is well-modeled by hierarchical Bayesian inference with strong priors over category structure. The account updates a hierarchical posterior over category hypotheses given examples,

$$p(h \mid X) \propto p(X \mid h) \, p(h \mid \Theta) \, p(\Theta)$$

with $h$ a candidate category, $\Theta$ hyperparameters governing category structure, and $X$ observed examples. The model provides quantitative fits to empirical infant behavior across multiple domains and connects developmental psychology to the modern Bayesian machine learning literature.

Face processing development exhibits a trajectory including the very early preference for face-like patterns, the progressive tuning of face processing to the races and genders in the infant's environment, and the emergence of the face-neural circuitry in the fusiform face area. This formulation provides evidence for both innate biases and substantial experience-dependent plasticity in perceptual development.

Perceptual narrowing is the phenomenon by which infant perceptual discrimination is initially broad and progressively narrows to match the distinctions relevant to the ambient environment. The pattern can be characterized by the developmental trajectory of the discrimination sensitivity across categories,

$$d'_{\text{discrim}}(c_i, c_j; t) = f_{\text{narrowing}}(t, \text{exposure}(c_i, c_j))$$

with the sensitivity increasing for category distinctions relevant to the ambient environment and decreasing for irrelevant distinctions. The treatment has been documented for phoneme discrimination, face discrimination, and other perceptual domains, and provides evidence for the patterns of experience-dependent plasticity that shape perceptual capabilities.

Modern deep learning implementations of perceptual development include the frameworks that model infant statistical learning through neural network training on infant-like sensory experience. The [Sullivan Mei Perfors Wojcik Frank 2021][research_sullivan_et_al_2021_saycam] SAYCam framework provides longitudinal head-mounted video recordings from infants and enables the systematic training and evaluation of models on infant-like data.

## Piagetian Constructivism and Stage Theory

Piagetian constructivism of Piaget 1952 provided the foundational modern framework for cognitive development in children. This account identifies stages of cognitive development characterized by qualitatively-distinct cognitive capabilities and provides the mechanisms of assimilation and accommodation through which cognitive development proceeds.

The Piagetian stages include the sensorimotor stage (birth to approximately two years) in which the infant acquires knowledge through sensorimotor interaction with the environment, the preoperational stage (approximately two to seven years) in which the child develops symbolic thought but lacks logical operations, the concrete operational stage (approximately seven to eleven years) in which the child develops logical operations over concrete objects, and the formal operational stage (approximately eleven years onward) in which the adolescent develops abstract logical reasoning.

Assimilation and accommodation provide the mechanisms of cognitive development. Assimilation is the incorporation of new information into existing cognitive schemas, and accommodation is the modification of existing schemas to accommodate information that does not fit. The framework can be formalized as a schema-updating rule

$$S_{t+1} = \begin{cases} S_t \cup \{o_t\} & \text{if } \text{fit}(S_t, o_t) > \tau \quad \text{(assimilation)} \\ \text{modify}(S_t, o_t) & \text{if } \text{fit}(S_t, o_t) \leq \tau \quad \text{(accommodation)} \end{cases}$$

with $S_t$ the current schema, $o_t$ the observed information, $\text{fit}$ a compatibility measure, and $\tau$ a threshold. The account provides a computational account of cognitive change through the balance of these two processes.

Object permanence is a developmental milestone in the sensorimotor stage identified by Piaget through the experiments in which infants search for hidden objects. Modern replications by [Baillargeon 1987][research_baillargeon_1987] documented that object permanence emerges greatly earlier than Piaget originally proposed, through the violation-of-expectation methodology in which infants show surprise at physically impossible events involving hidden objects.

The core knowledge framework of Spelke and Kinzler 2007 extended the Piagetian framework with the proposal that infants possess innate cognitive structures for reasoning about objects, agents, numbers, geometry, and social groups. The model provides a middle ground between pure empiricism and strong nativism through the specification of innate priors that scaffold subsequent learning.

Neo-Piagetian frameworks of [Case 1985][book_case_1985] and [Fischer 1980][research_fischer_1980] refined the stage-theory framework with the proposal that cognitive development involves the progressive expansion of working memory capacity and the reorganization of cognitive structures at stage transitions. This formulation has provided empirical grounding for the developmental milestones observed across cultures.

Rethinking Innateness of [Elman Bates Johnson Karmiloff-Smith Parisi Plunkett 1996][book_elman_et_al_1996] provided the connectionist reformulation of the innateness-versus-learning debate through the proposal that innate architectural biases interact with experience to produce the developmental trajectory. The treatment has considerably shaped subsequent computational developmental psychology.

Modern computational implementations of Piagetian development include the frameworks that model stage transitions through the interaction of learned representations with expanded processing capacity. This account connects developmental psychology to the modern deep learning literature through the shared emphasis on the emergence of complex cognitive capabilities from simpler precursors.

## Executive Function and Cognitive Control Development

Executive function is the set of cognitive control processes that support goal-directed behavior including working memory, inhibitory control, and cognitive flexibility. The framework provides a developmental construct that has been extensively studied both empirically and computationally, and provides testable predictions about the cognitive capabilities that emerge across childhood.

The [Diamond 2013][research_diamond_2013] executive functions review consolidated the modern developmental psychology framework and identified the components of executive function including inhibitory control, working memory, and cognitive flexibility. The account provides quantitative fits to the developmental progression of executive function across childhood and adolescence.

The [Miyake Friedman Emerson Witzki Howerter Wager 2000][research_miyake_et_al_2000] unity and diversity framework identified the factor structure of executive function in adults, and the subsequent [Miyake and Friedman 2012][research_miyake_friedman_2012] developmental extension documented the developmental trajectory of these factors across childhood.

Working memory development follows a progression across childhood characterized by the gradual expansion of the digit span and the improvement of working memory manipulation. The [Baddeley 2003][research_baddeley_2003_wm] working memory model provided the systematic framework for working memory as a cognitive architecture composed of the phonological loop, visuospatial sketchpad, and central executive components. The model has marked empirical support from studies across development and provides testable predictions about the developmental progression of working memory capabilities.

Inhibitory control development is characterized by the developmental progression of the ability to override prepotent responses in favor of goal-directed action. This formulation has been extensively studied through the paradigms including the Stroop task, the day-night task, and the Simon task, and provides evidence for the developmental trajectory of inhibitory control across childhood and adolescence.

Cognitive flexibility development is characterized by the ability to switch between task rules or perspectives. The Dimensional Change Card Sort task of [Zelazo 2006][research_zelazo_2006_dccs] provides the paradigm through which cognitive flexibility development has been systematically probed, and the model documents the developmental progression from perseveration at age three to flexible switching by age five.

The prefrontal cortex is the neural substrate that supports executive function, and its extended developmental trajectory through adolescence and early adulthood provides the neural basis for the developmental progression of executive function capabilities. The [Zelazo 2015][research_zelazo_2015] executive function development framework identified the relationships between neural maturation and cognitive control development.

Modern deep learning implementations of executive function include the frameworks that model working memory through recurrent neural network architectures and the attention mechanisms that support cognitive control. This account connects executive function to the modern machine learning literature through the shared emphasis on the control mechanisms that shape task-directed behavior.

Executive function has proved a particularly strong predictor of academic achievement, social competence, and long-term life outcomes. The framework has extensive applied importance for education, clinical intervention, and public policy, and provides the bridge between developmental psychology and applied practice.

## Core Knowledge and Innate Priors

Core knowledge accounts of Spelke 1994 and Spelke and Kinzler 2007 proposed that infants possess innate cognitive structures for reasoning about objects, agents, numbers, geometry, and social groups. The account provides a alternative to both pure empiricist and strong nativist accounts of cognitive development.

The core knowledge systems include the object system that supports reasoning about the persistence and continuity of physical objects, the agent system that supports reasoning about the goal-directed behavior of animate entities, the number system that supports approximate reasoning about numerical quantities, the geometry system that supports reasoning about the spatial layout of the environment, and the social system that supports reasoning about group membership and social identity.

Empirical evidence for core knowledge systems includes the violation-of-expectation studies that document infant surprise at events that violate core knowledge principles. Baillargeon 1987 provided the foundational demonstrations for object permanence, and subsequent work has extended the account to numerical cognition through [Wynn 1992][research_wynn_1992], to agency through [Woodward 1998][research_woodward_1998_agency], and to social reasoning through [Hamlin Wynn Bloom 2007][research_hamlin_wynn_bloom_2007]. The [Feigenson Dehaene Spelke 2004][research_feigenson_dehaene_spelke_2004] core systems of number review consolidated the numerical cognition literature and identified the dual-system architecture of approximate magnitude representation and precise small-number tracking. The [Carey 2009][book_carey_2009] Origin of Concepts systematic treatment provided the comprehensive framework for conceptual development that combines core-knowledge systems with the mechanisms of conceptual change during development.

Theory of mind development was systematically reviewed by [Wellman Cross Watson 2001][research_wellman_cross_watson_2001] through the meta-analysis of false-belief-task performance across cultures, providing quantitative evidence for the developmental milestone of theory-of-mind acquisition around age four. Descartes' Baby of [Bloom 2004][book_bloom_2004] provided the systematic treatment of the developmental origins of moral, social, and religious cognition.

Physical reasoning in infants was systematically investigated by [Baillargeon Spelke Wasserman 1985][research_baillargeon_spelke_wasserman_1985] and the sizable subsequent literature. This formulation provides evidence that infants deploy principles of physical reasoning including solidity, continuity, and contact from the earliest ages tested.

The [Lake Ullman Tenenbaum Gershman 2017][research_lake_ullman_tenenbaum_gershman_2017] Building Machines That Learn and Think Like People framework argued that human-like machine learning requires the incorporation of core knowledge priors alongside statistical learning capabilities. The treatment has significantly shaped subsequent research on the integration of prior structure with learned representations in machine learning systems.

Bayesian implementations of core knowledge through the [Battaglia Hamrick Tenenbaum 2013][research_battaglia_hamrick_tenenbaum_2013] intuitive physics engine framework provided the computational instantiation of core physical knowledge as a probabilistic simulation engine that infants deploy for physical reasoning. This account predicts physical outcomes through the noisy-simulation-and-marginalization computation

$$p(\text{outcome} \mid \text{scene}) = \int p(\text{outcome} \mid s, \theta_{\text{phys}}) \, p(s \mid \text{scene}) \, p(\theta_{\text{phys}}) \, ds \, d\theta_{\text{phys}}$$

with the scene state $s$ and physical parameters $\theta_{\text{phys}}$ marginalized over their posterior distributions. The framework connects core knowledge to modern probabilistic programming and to the world model treatments of article seven.

Modern debates about core knowledge in artificial systems focus on the question of whether machine learning systems should incorporate core knowledge priors architecturally or should learn them from experience. The advantages of each approach depend on the available compute, the available data, and the inductive biases required for the target application.

Core knowledge frameworks provide a bridge between developmental psychology and modern machine learning. The account identifies the inductive biases that support efficient learning in human infants and provides testable predictions about the structural properties that machine learning systems require to achieve human-like generalization.

## Symbol Grounding and Language Development

The symbol grounding problem of [Harnad 1990][research_harnad_1990_symbol_grounding] identified the challenge of connecting abstract symbols to their referents in the physical world. The model predicts that symbolic reasoning must ultimately be grounded in sensorimotor experience, providing a constraint on the design of intelligent systems.

The Steels 2003 embodied grounding framework of [Steels 2003][research_steels_2003_grounding] provided the computational treatment through the language-game framework in which agents progressively develop shared symbolic representations through their coupled interaction with the environment. This formulation demonstrates that shared symbol systems can emerge from the patterns of embodied interaction without requiring a designer to specify the symbol-referent mappings in advance.

Cross-situational word learning of Yu and Smith 2007 provided the developmental framework in which children acquire word-referent mappings through the statistical regularities across multiple labeling instances. The treatment has been extensively studied both empirically and computationally, and provides the bootstrapping mechanism that supports early lexical acquisition.

The formal cross-situational learning model updates the posterior over word-referent mappings after each observation,

$$p(m \mid w, r) \propto p(w \mid m, r) \, p(r \mid m) \, p(m)$$

with $m$ the word-referent mapping, $w$ the observed word, $r$ the observed referent context, and appropriate factorizations of the likelihood. This account provides quantitative fits to empirical child data and demonstrates that statistical inference resolves the referential ambiguity through cross-situational aggregation.

Fast mapping of [Carey and Bartlett 1978][research_carey_bartlett_1978] documented the ability of young children to acquire word meanings from a single exposure. The mutual-exclusivity inductive bias

$$p(m \mid w, \{m_j\}_{j \neq i}) \propto p(w \mid m) \, \mathbb{1}[m \notin \{m_j\}_{j \neq i}]$$

restricts the candidate word-meaning mappings by excluding meanings already assigned to other words in the vocabulary. The framework has been extensively studied both empirically and computationally, and provides evidence for inductive biases that support rapid one-shot word learning.

Grounded language learning in artificial systems has produced appreciable modern progress through the frameworks that combine language models with physical embodiment. The [Chai Fang Lin Zhang Yang 2018][research_chai_et_al_2018_grounded] grounded language learning survey consolidated the pre-foundation-model literature and identified the challenges of grounded language. Grounding words in perception of [Roy 2005][research_roy_2005] provided the model in which word meanings are learned through the systematic association of language with the perceptual and motor experiences that accompany their use. The [Frank Tenenbaum Fernald 2013][research_frank_tenenbaum_fernald_2013] Bayesian word-learning framework provided the probabilistic computational model of infant word learning that captures both cross-situational statistical learning and the inductive biases of the mutual-exclusivity assumption.

Constructing a Language of [Tomasello 2003][book_tomasello_2003_constructing] provided the systematic usage-based account of language acquisition in which grammatical structure emerges from the patterns of usage rather than through the deployment of an innate universal grammar. The model has substantially shaped subsequent developmental linguistics and provides the bridge to computational language-acquisition models. How Children Learn the Meanings of Words of [Bloom 2000][book_bloom_2000] provided the complementary systematic treatment of the psychological mechanisms of word learning in children.

Modern foundation-model-based approaches to grounded language include the vision-language-action models treated in article ten and eleven, providing an approach that combines the semantic capabilities of language models with the sensorimotor coupling of embodied systems. This formulation has markedly reshaped the engineering practice of grounded language systems.

The [Bisk et al 2020][research_bisk_et_al_2020_experience] Experience Grounds Language argument identified the claim that genuine language understanding requires grounding in embodied experience beyond the text-based training corpora that dominate modern language models. The treatment has appreciably influenced subsequent discussion of the role of embodiment in language understanding.

## Predictive Coding and Active Inference

Predictive coding provides the computational framework in which perception, action, and learning are unified through the systematic minimization of prediction errors. This account has proved influential across cognitive neuroscience, developmental psychology, and machine learning.

The Rao and Ballard 1999 hierarchical predictive coding framework introduced the proposal that the cortex implements a hierarchy of prediction models in which higher levels predict the activity of lower levels, and prediction errors propagate up the hierarchy to update the predictions. The framework has considerable empirical support from neurophysiological studies of the visual and other cortical systems.

The formal predictive coding framework computes prediction errors at each hierarchical level as the difference between the actual activity and the predicted activity,

$$\epsilon_l = x_l - \hat{x}_l, \quad \hat{x}_l = g_l(x_{l+1})$$

where $x_l$ is the activity at level $l$, $g_l$ is the generative model that maps activity from level $l+1$ to predicted activity at level $l$, and $\epsilon_l$ is the prediction error. The account updates both the activities and the generative model parameters to minimize the total weighted prediction error.

The Friston 2010 free energy principle provided the unified theoretical framework through which perception, action, and learning correspond to the minimization of variational free energy,

$$F = \mathbb{E}_{q(s)}[\log q(s) - \log p(o, s)]$$

where $q(s)$ is the internal model's posterior over hidden states, $p(o, s)$ is the joint distribution of observations and hidden states, and the free energy provides an upper bound on the negative log-evidence. Perception updates $q$ to minimize $F$, action selects motor commands that minimize expected $F$, and learning updates the parameters of the generative model to minimize $F$. The free energy admits the decomposition

$$F = D_{\text{KL}}(q(s) \, \| \, p(s \mid o)) - \log p(o)$$

into a divergence between the approximate and true posteriors and the negative log-evidence, providing the formal justification for the variational-inference interpretation of predictive coding.

Active inference of [Friston Rigoli Ognibene Mathys Fitzgerald Pezzulo 2015][research_friston_et_al_2015_active_inference] extended the treatment to action selection through the proposal that agents select actions to minimize expected free energy under alternative policies. The expected free energy of a policy $\pi$ decomposes into pragmatic and epistemic components,

$$G(\pi) = \underbrace{-\mathbb{E}_{q(\tilde{o} \mid \pi)}\!\left[\log p(\tilde{o})\right]}_{\text{pragmatic}} + \underbrace{-\mathbb{E}_{q(\tilde{o} \mid \pi)}\!\left[\mathbb{H}[q(\tilde{s} \mid \tilde{o}, \pi)]\right]}_{\text{epistemic}}$$

with the first term favoring observations aligned with preferred outcomes and the second term favoring observations that reduce hidden-state uncertainty. The decomposition provides a unified account of exploration and exploitation, connecting active inference to the intrinsic motivation treatments of article five.

Precision-weighted prediction errors of [Feldman and Friston 2010][research_feldman_friston_2010] extended the standard predictive coding framework with the weighting of prediction errors by their expected precision,

$$\epsilon_l^{\text{weighted}} = \Pi_l (x_l - \hat{x}_l)$$

with $\Pi_l$ the precision matrix at level $l$ that captures the expected reliability of the sensory evidence. The precision-weighting framework accounts for attentional modulation, perceptual salience, and the patterns of hierarchical inference observed in developmental neuroscience.

The [Clark 2016][book_clark_2016] Surfing Uncertainty consolidated the predictive processing literature and provided the systematic philosophical treatment of predictive coding as a general framework for embodied cognition. The [Hohwy 2013][book_hohwy_2013] Predictive Mind provided the complementary philosophical treatment focused on the implications of predictive processing for the philosophy of mind and cognitive science. The [Millidge Tschantz Buckley 2021][research_millidge_tschantz_buckley_2021] predictive coding review consolidated the modern computational treatments and identified the relationships among the several predictive-coding-inspired frameworks. This formulation identifies the computational and phenomenological implications of the predictive coding view for embodied and enactive cognitive science.

Active inference reinforcement learning of [Tschantz Millidge Seth Buckley 2020][research_tschantz_et_al_2020_ai_rl] provided the bridge between the active inference framework and the modern reinforcement learning literature, demonstrating that the free energy minimization objective produces reinforcement-learning-competitive behavior on standard benchmarks while providing the unified account of perception, action, and learning.

Modern deep learning implementations of predictive coding include the frameworks that instantiate hierarchical predictive models as deep neural networks with error-propagation and update rules. The [Ororbia Kifer 2020][research_ororbia_kifer_2020_neural_generative] neural generative coding framework provided the computational bridge between the classical predictive coding literature and modern deep learning practice.

Predictive coding connects developmental learning to the world model treatments of article seven through the shared emphasis on learned generative models as the substrate of both perception and action. The treatment provides the theoretical unification of developmental robotics, embodied cognition, and modern deep learning through the shared computational principle of prediction-error minimization.

## Morphological Computation and Body Schema

Morphological computation treats the contribution of the physical body to cognitive computation. This account proposes that intelligent behavior emerges not only from neural computation but also from the physical dynamics of the body and its interaction with the environment.

The [Pfeifer and Bongard 2006][book_pfeifer_bongard_2006] How the Body Shapes the Way We Think provided the foundational modern treatment of morphological computation. The framework identifies the ways in which body morphology contributes to cognitive processes and provides testable predictions about the design principles for embodied intelligent systems.

The [Pfeifer and Iida 2005][research_pfeifer_iida_2005] morphological computation framework introduced the computational treatment through the identification of the computational operations that the body performs. Examples include the passive dynamic walking of leg morphologies that produces stable gait without explicit control, the mechanical filtering properties of the ear that support auditory scene analysis, and the properties of the hand that support dexterous manipulation without complex control.

Body schema is the internal representation of the body that supports coordinated action. The [Head and Holmes 1911][research_head_holmes_1911] foundational treatment introduced the body schema concept, and the significant subsequent literature has documented the properties of body schema representations in neurological patients and in healthy individuals.

Self-modeling robots of [Bongard Zykov Lipson 2006][research_bongard_zykov_lipson_2006_a262] demonstrated that robots can autonomously discover their own body schema through active exploration and use the learned model for recovery from unexpected morphological damage. The body schema is formally instantiated as a learned mapping from motor commands to expected sensor readings,

$$\hat{o}_{t+1} = M_\psi(o_t, u_t)$$

with $\psi$ the body-schema parameters that are updated online through the pattern of prediction-error minimization. The account provides the computational instantiation of the body schema in artificial systems and demonstrates that self-modeling supports robust adaptive behavior.

The role of morphology in developmental learning has been documented across many domains. Infant motor development is greatly shaped by the body proportions and biomechanical properties of the infant body. Perceptual development is shaped by the placement and properties of the sensory organs. Social development is shaped by the properties of the body that support communicative gestures and expressions.

The rubber hand illusion of [Botvinick and Cohen 1998][research_botvinick_cohen_1998] provided the experimental paradigm for the study of body ownership. The model documents that the patterns of multisensory integration can produce the phenomenal experience of ownership of external objects, providing empirical evidence for the malleability of body schema.

Modern embodied AI systems increasingly recognize the importance of morphology through the design of physical robots and the choice of embodied simulation environments. This formulation connects embodied AI to the classical morphological computation literature through the shared emphasis on the physical substrate as a computational participant.

Cross-embodiment learning treated in article eleven provides the modern instantiation of the morphological computation framework at foundation-model scale, providing an approach that explicitly addresses the challenges of transferring learned capabilities across different physical bodies.

## Curriculum Learning and Developmental Trajectories

Curriculum learning treats the problem of ordering training examples or tasks to support efficient learning. The treatment connects developmental learning to modern machine learning practice through the shared emphasis on the importance of the ordering of experience for learning outcomes.

Bengio Louradour Collobert Weston 2009 [research_bengio_et_al_2009_curriculum] introduced the modern machine learning curriculum learning framework through the proposal that neural networks train more effectively when the training examples are presented in a difficulty-ordered sequence. The general curriculum objective can be written as an expected loss under a time-dependent training distribution,

$$L_{\text{curriculum}}(\theta) = \mathbb{E}_{t \sim T}\!\left[\mathbb{E}_{x \sim p_t(x)}[L(\theta; x)]\right]$$

with the training distribution $p_t(x)$ progressively shifting from easy to hard examples according to a specified curriculum schedule. This account produces considerably better final performance and faster training convergence on many benchmarks.

Self-paced learning of [Kumar Packer Koller 2010][research_kumar_packer_koller_2010] extended the framework with the proposal that the curriculum should be automatically discovered rather than manually specified. The framework adapts the curriculum based on the current model's capabilities, providing an approach that connects to intrinsic-motivation-based exploration.

Automatic curriculum learning of [Portelas Colas Molinari Oudeyer 2020][research_portelas_et_al_2020_acl_a262] consolidated the automatic curriculum literature and identified the mechanisms including teacher-student frameworks, learning-progress-based selection, and adversarial curriculum generation. The model provides the bridge between developmental robotics and modern deep reinforcement learning.

Teacher-Student Curriculum Learning of [Portelas Colas Hofmann Oudeyer 2019][research_portelas_et_al_2019_ts] introduced the model in which a teacher policy selects tasks to maximize the expected learning progress of a student policy. The teacher's task-selection policy maximizes

$$\pi_{\text{teacher}}(\mathcal{T}) = \arg\max_{\mathcal{T} \in \mathcal{T}_{\text{avail}}} \, \mathbb{E}\!\left[\text{LP}_{\text{student}}(\mathcal{T})\right]$$

where the expected learning progress of the student on task $\mathcal{T}$ is estimated from recent training history. The treatment provides an approach that automatically adapts to the student's current capabilities and mimics the patterns of scaffolded instruction observed in human development.

POET and PAIRED of article twelve provide instantiations of the automatic curriculum framework at foundation-model scale, providing evidence that automatic curriculum construction scales to modern deep reinforcement learning.

The developmental trajectory produced by intrinsic-motivation-driven curriculum construction admits systematic analysis. This account predicts the progression from high-learning-progress tasks to increasingly-complex tasks, with the transitions marking the exhaustion of the learning progress in the current task class. The framework has been documented empirically both in artificial systems and in human developmental data.

Modern language model pretraining increasingly incorporates curriculum-like ordering of training data. The frameworks include difficulty-ordered sampling, domain-progressive training, and instruction-tuning-based curricula that provide the ordered exposure required for capability emergence. The account connects the classical developmental curriculum literature to modern foundation model practice.

Curriculum learning provides the mechanism through which developmental capability emergence can be replicated in artificial systems. The model predicts that the choice of curriculum significantly affects both the final capabilities and the developmental trajectory, providing testable predictions about the relationships between experience ordering and capability emergence.

## Social Development and Joint Attention

Social development is the developmental track through which infants acquire the capacities for social interaction, communication, and cultural learning. This formulation connects developmental robotics to the psychology and neuroscience of social cognition development.

Joint attention is the developmental milestone in which infants coordinate attention with a social partner. The [Bruner 1983][book_bruner_1983] foundational treatment identified joint attention as a critical prerequisite for language acquisition, and the substantial subsequent literature has documented the developmental trajectory through which joint attention emerges. The [Tomasello 1995][research_tomasello_1995_joint] joint attention framework identified the developmental progression from dyadic through referential to symbolic joint attention, and the [Trevarthen 1979][research_trevarthen_1979] primary intersubjectivity framework identified the patterns of caregiver-infant communication that characterize early social development.

Gaze following in infants was systematically documented by [Scaife and Bruner 1975][research_scaife_bruner_1975] through the paradigm in which infants follow the gaze direction of adults. The treatment provides evidence for the developmental progression from purely-reflexive to increasingly-intentional gaze following.

Theory of Mind development treated in article eleven provides the developmental framework through which children acquire the capacity to reason about the mental states of others. This account identifies developmental milestones including the passing of false belief tasks around age four, providing testable developmental predictions.

Social scaffolding of [Vygotsky 1978][book_vygotsky_1978] introduced the developmental framework in which social interactions with more competent partners scaffold the child's capabilities beyond what independent learning would support. The framework has substantially shaped subsequent educational psychology and provides the developmental account of the zone of proximal development.

Natural pedagogy of [Csibra and Gergely 2009][research_csibra_gergely_2009] identified the human-cognitive adaptation through which infants receive generic knowledge from ostensive communication with caregivers. The account provides a mechanistic account of the human capacity for cumulative culture and has been implemented computationally in the pedagogical teaching-and-learning literature.

Imitation development is a track that has been extensively studied. The Meltzoff and Moore 1977 neonatal imitation demonstrations provided the foundational evidence, and the subsequent literature has documented the progression from reflexive imitation through selective imitation to the culturally-shaped imitation that supports cumulative learning.

Modern developmental robotics implementations of social development include the frameworks that model joint attention, imitation, and social scaffolding in humanoid robots. The [Nagai Hosoda Morita Asada 2003][research_nagai_et_al_2003] joint attention developmental framework and the marked subsequent literature have produced humanoid robot systems that exhibit some elements of social developmental capability. The [Kaplan and Hafner 2006][research_kaplan_hafner_2006] joint attention robotics review consolidated the computational literature on artificial systems that exhibit joint-attention-like behavior, and How Infants Know Minds of [Reddy 2008][book_reddy_2008] provided the standard treatment of the developmental origins of social cognition through second-person engagement rather than through third-person theory-of-mind reasoning.

Social development connects developmental robotics to the multi-agent reinforcement learning treatments of article eleven and to the emergent communication treatments through the shared emphasis on the patterns of inter-agent interaction that support cognitive development.

## Self-Recognition and the Development of Agency

Self-recognition and the sense of agency provide the developmental milestones through which the infant acquires the concept of the self as a distinct entity with the capacity for goal-directed action. The model connects developmental psychology to phenomenology, neuroscience, and modern artificial intelligence through the shared question of what constitutes a self-recognizing agent.

The [Gallup 1970][research_gallup_1970_mirror] mirror self-recognition paradigm introduced the empirical test of self-recognition through the surreptitious marking of the face followed by observation of the mark-directed behavior in front of a mirror. This formulation provides the behavioral test that has been applied across species and developmental ages, and self-recognition through the mirror test emerges around age 18 to 24 months in typically-developing children.

The [Amsterdam 1972][research_amsterdam_1972] mirror-self-recognition developmental study documented the developmental progression in children including the initial reflexive response to the mirror image at approximately six months, the exploration of the mirror-image contingency at around 12 months, and the emergence of explicit self-recognition around 18 to 24 months. The treatment has been extensively studied both empirically and computationally.

The [Rochat 2003][research_rochat_2003] five levels of self-awareness framework identified the developmental progression from the initial differentiation of self from environment through the elaborate metacognitive self-awareness that characterizes mature human cognition. This account provides testable predictions about the developmental milestones of self-awareness.

The sense of agency is the experience of causing one's own actions, distinct from the perceptual experience of body ownership. The [Jeannerod 2003][research_jeannerod_2003_agency] framework identified the computational mechanisms that generate the sense of agency through the comparison of predicted and actual sensory consequences of motor commands. The framework provides the bridge between motor control and phenomenal experience.

The [Haggard 2005][research_haggard_2005_agency] framework consolidated the modern experimental treatment of agency through the paradigms including intentional binding, the sense of agency scale, and the neurophysiological correlates of the sense of agency. The account has extensive empirical support and provides testable predictions about the neural substrates of agency.

Gergely and Watson 1999 [research_gergely_watson_1999] introduced the contingency detection framework in which infants distinguish self-produced from other-produced sensory events through the detection of the perfect contingency between motor commands and sensory consequences. The model provides the developmental mechanism through which the self-other distinction emerges from sensorimotor experience.

Modern developmental robotics implementations of self-recognition include the frameworks that model the emergence of a body-schema through active sensorimotor exploration. The Bongard Zykov Lipson 2006 self-modeling framework treated in the morphological computation section provides the computational instantiation. Subsequent work has extended the framework to the developmental trajectory of self-recognition and to the challenges of distinguishing self from environment in artificial systems.

The sense of agency in artificial systems has been studied through the frameworks that model self-monitoring and the mechanisms through which artificial systems attribute outcomes to their own actions versus external causes. The treatment connects to the philosophical questions of machine consciousness and to the practical engineering questions of self-monitoring in autonomous systems.

Self-recognition and agency development provide the developmental substrate for the emergence of self-awareness, meta-cognition, and the theory-of-mind capacities that support social cognition. This account provides the bridge between the developmental psychology of self and the broader questions of cognitive architecture in artificial systems.

## Embodied Foundation Models and Simulation Environments

Modern embodied artificial intelligence increasingly leverages foundation-model-scale simulation environments and cross-embodiment learning. The framework provides the practical substrate for the developmental learning research at deployment scale.

Habitat of [Savva Kadian Maksymets Zhao Wijmans Jain Straub Liu Koltun Malik Parikh Batra 2019][research_savva_et_al_2019_habitat] introduced the fast simulation environment for embodied AI research that supports the training of navigation policies at sizable scale. The account has been widely adopted and has enabled the benchmarking of embodied agents across standard tasks. Habitat 2.0 of [Szot Clegg Undersander Wijmans Zhao Turner Maestre Mukadam Chaplot Maksymets Gokaslan Vondrus Dharur Meier Galuba Chang Kira Koltun Malik Savva Batra 2021][research_szot_et_al_2021_habitat2] extended the framework with interactive physics and long-horizon tasks that support the systematic study of embodied AI beyond pure navigation.

iGibson of [Xia Zamir He Sax Malik Savarese 2020][research_xia_et_al_2020_igibson] provided the complementary simulation environment focused on interactive tasks with realistic physics. This formulation supports the study of embodied tasks that require physical interaction beyond pure navigation.

AI2-THOR of [Kolve Mottaghi Han VanderBilt Weihs Herrasti Deitke Ehsani Gordon Zhu Kembhavi Gupta Farhadi 2017][research_kolve_et_al_2017_ai2thor] provided the photorealistic simulation environment focused on household tasks. The treatment has enabled the study of long-horizon embodied tasks that require the composition of multiple sub-skills.

ThreeDWorld of [Gan Schwartz Alter Schrimpf Traer De Freitas Kubilius Bhandwaldar Haber Sano Kim Wang Mrowca Lingelbach Curtis Feigelis Bear Gutfreund Cox Torralba DiCarlo Tenenbaum McDermott Yamins 2020][research_gan_et_al_2020_tdw] provided the multi-modal simulation environment with realistic physics, audio, and visual rendering. This account supports the study of embodied learning across multiple sensory modalities.

Embodied Question Answering of [Das Datta Gkioxari Lee Parikh Batra 2018][research_das_et_al_2018_eqa] introduced the embodied task in which agents must answer questions about their environment through active exploration. The task requires the joint optimization of navigation and answering,

$$\pi^*(q) = \arg\max_\pi \, \mathbb{E}_{\tau \sim \pi(\cdot \mid q)}\!\left[\log p(a^* \mid q, \tau)\right] - \lambda \, |\tau|$$

with $q$ the question, $\tau$ the exploration trajectory, $a^*$ the correct answer, and $|\tau|$ a length penalty. The framework connects embodied AI to language understanding through the requirement of grounding linguistic queries in embodied experience.

RT-1 and RT-2 of Brohan et al treated in articles nine and eleven provide the modern foundation-model-scale embodied learning systems that transfer capabilities from vision-language pretraining to real-robot control. The account provides the bridge between the modern foundation model literature and embodied artificial intelligence.

Open X-Embodiment of Padalkar et al 2024 treated in prior articles provides the large-scale multi-institution embodied dataset that has enabled the training of cross-embodiment models. The model provides the data infrastructure for embodied foundation model research.

Modern embodied AI increasingly bridges the gap between pure simulation training and real-world deployment through the combination of large-scale simulation, domain randomization, and modest amounts of real-world fine-tuning. This formulation connects embodied learning to the sim-to-real treatments of article eleven and to the meta-learning treatments of article nine.

## Theoretical Frameworks

The theoretical foundations of embodied cognition and developmental learning include several complementary frameworks. Ecological psychology of Gibson 1979 provided the foundational framework through the proposal that perception operates directly on ecological information without intervening symbolic representation. The treatment identifies the structural properties of the ecological environment that support direct perception and has markedly shaped subsequent embodied cognitive science.

Dynamical systems approaches of [Thelen and Smith 1994][book_thelen_smith_1994] provided the complementary framework through the proposal that developmental change is a dynamical process rather than a sequence of discrete stages. The [Beer 1995][research_beer_1995] dynamical systems and adaptive behavior framework provided the computational treatment of dynamical-systems approaches to embodied cognition, and the [van Gelder 1998][research_van_gelder_1998] dynamical hypothesis for cognitive science provided the systematic philosophical argument that cognition is fundamentally a dynamical rather than a computational process. This account identifies the mathematical properties of developmental trajectories including attractors, phase transitions, and the patterns of variability that accompany developmental transitions.

The formal dynamical systems framework represents developmental state through a differential equation

$$\dot{x} = f(x, u, \theta)$$

with $x$ the developmental state, $u$ the environmental input, and $\theta$ the internal parameters. The framework predicts developmental phenomena including the patterns of behavioral variability at transitions, the role of noise in producing developmental change, and the attractor structure that characterizes developmental milestones.

Predictive processing of Clark 2016 provided the theoretical unification of embodied cognition, predictive coding, and active inference. The account identifies the ways in which the predictive coding computational framework unifies appreciable portions of the embodied cognitive literature and provides testable predictions about the patterns of neural and behavioral phenomena.

The relationship between embodied cognition and Bayesian brain frameworks has been extensively studied. The Bayesian brain framework proposes that the brain implements probabilistic inference through neural computation. The general perceptual inference

$$p(s \mid o) \propto p(o \mid s) \, p(s)$$

is instantiated in the hierarchical predictive coding computation described earlier, with the priors $p(s)$ shaped by the developmental history and the likelihoods $p(o \mid s)$ shaped by the sensory apparatus. The extension to embodied Bayesian brains treats the body and environment as participants in the inference computation.

Neural network models of development include the frameworks that model developmental change through the training dynamics of neural networks. The [Elman 1993][research_elman_1993_less] Less is More framework introduced the proposal that developmental constraints on memory or processing can accelerate learning of structural properties, providing evidence for the developmental function of processing limitations.

Free energy accounts of development of [Kirchhoff Parr Palacios Friston Kiverstein 2018][research_kirchhoff_et_al_2018] extended the free energy framework to the developmental context, identifying the ways in which the minimization of free energy across developmental time produces the patterns of biological and cognitive maturation.

Neuroconstructivism of [Mareschal Johnson Sirois Spratling Thomas Westermann 2007][book_mareschal_et_al_2007_neuroconstructivism] provided the systematic modern framework for developmental cognition that integrates neuroscience, computational modeling, and developmental psychology. The model proposes that cognitive development proceeds through the interaction of innate architectural biases with progressive experience-dependent specialization of neural circuits, and provides a alternative to both strong nativist and strong empiricist accounts of development.

The neuroconstructivist framework identifies the principles of developmental change including partial-representation formation, progressive specialization of neural systems, and the role of interaction between developing systems in shaping the eventual cognitive architecture. This formulation has appreciably shaped subsequent computational developmental cognitive science through the integration of biological and computational constraints on developmental trajectories.

The theoretical foundations of developmental learning connect embodied cognition to modern machine learning through several shared frameworks including hierarchical inference, self-supervised representation learning, curriculum learning, and intrinsic motivation. The connections continue to organize considerable ongoing research and provide the theoretical basis for the practical developmental robotics engineering.

## Empirical Landscape and Benchmarks

The empirical landscape of embodied AI and developmental learning has consolidated around several benchmark suites. Habitat of Savva et al 2019 provides the standard navigation benchmark and supports systematic comparison across embodied AI methods. The associated Habitat Challenge competitions have driven significant progress in embodied navigation.

RLBench of [James Ma Arrojo Davison 2020][research_james_et_al_2020_rlbench] provides the standard manipulation benchmark with hundreds of tasks that support the study of manipulation learning at scale. The treatment has enabled the systematic comparison of imitation learning, reinforcement learning, and hybrid methods on standard tasks.

Behavior of [Srivastava Li Xia Nie Wu Nasir Yang Zhao Zhang Wang Fei-Fei 2022][research_srivastava_et_al_2022_behavior] provides the large-scale benchmark for embodied AI focused on complex household tasks. This account has driven progress on the challenges of long-horizon embodied task completion.

The Meta-World benchmark treated in article nine provides the benchmark for meta-learning in robotic manipulation and has been adopted extensively by embodied AI researchers for the study of few-shot task acquisition.

SAYCam of Sullivan et al 2021 provides the longitudinal dataset of infant head-mounted video and enables the direct comparison of computational models to infant experience. The framework provides the empirical grounding for computational developmental models.

Modern embodied AI benchmarks increasingly focus on language-grounded tasks. The benchmarks including CLIPort, VLN, and a range of instruction-following benchmarks support the systematic evaluation of language-grounded embodied agents.

Empirical patterns across the benchmark landscape show several consistent findings. Foundation-model-based embodied learning greatly outperforms task-baselines on many benchmarks. Cross-embodiment training considerably improves policy transfer to held-out embodiments. Curriculum-based training significantly improves both final performance and training efficiency on many tasks. Intrinsic-motivation-based exploration substantially improves sample efficiency on sparse-reward tasks.

The gap between benchmark performance and real-world deployment remains substantial. Simulated benchmark performance often overestimates real-world capability due to the idealizations of simulation environments. The challenges of real-world embodied AI including sensor noise, actuator uncertainty, and long-horizon task composition remain active research areas.

## Applications

Robotic manipulation and locomotion have been the primary application domains for embodied AI. Learning-based approaches have progressively displaced model-based approaches for many manipulation and locomotion tasks, and modern practice combines model-based with learning-based components in hybrid architectures.

Assistive robotics uses embodied AI to develop robots that support elderly, disabled, or ill users. The requirements of assistive robotics including safety, adaptability, and personalization make it a particularly challenging application domain that has driven progress on the technical problems of adaptive embodied AI.

Domestic robotics including robotic vacuum cleaners, lawnmowers, and household assistants have been marked commercial applications of embodied AI. The requirements of consumer domestic robotics including reliability, cost-effectiveness, and ease of use have driven progress on the engineering problems of embodied AI at scale.

Autonomous vehicles use embodied AI for the problem of driving policy learning. The account has been extensively studied both in simulation and on physical vehicles, and modern autonomous driving systems combine embodied AI with model-based planning and safety verification.

Educational technology increasingly uses developmental learning principles to design personalized learning experiences. The application of intrinsic motivation, adaptive difficulty, and social scaffolding to educational software has driven extensive commercial progress.

Rehabilitation robotics uses embodied AI to support the recovery of motor function in patients with neurological injuries. The model connects developmental robotics to the clinical literature on motor rehabilitation and has produced sizable practical impact.

Toys and social robots increasingly incorporate developmental learning principles to produce engaging user experiences. The consumer market for social robots has driven progress on the engineering problems of natural human-robot interaction.

Prosthetics and exoskeletons use embodied AI for the control of assistive devices that interface with the human body. This formulation connects developmental robotics to the biomedical engineering literature on human-machine interfaces.

## Neuroscience Connections

The neuroscience of developmental learning has been extensively documented across many decades of research. Cortical development follows a temporal trajectory characterized by proliferation of neurons and synapses in early development, followed by systematic pruning of connections in response to experience. The [Huttenlocher 1979][research_huttenlocher_1979] documentation of the developmental trajectory of synaptic density in human cortex provided the foundational quantitative framework, characterized by the pattern

$$\rho_{\text{synapse}}(t) = \rho_0 + \rho_1 t \, e^{-\alpha t} - \rho_2 \, \mathbb{1}[t > t_{\text{prune}}] \, (1 - e^{-\beta (t - t_{\text{prune}})})$$

capturing the initial proliferation followed by experience-dependent pruning after the onset time $t_{\text{prune}}$. The appreciable subsequent literature has extended the framework to cortical areas and developmental time windows.

Critical periods are developmental windows during which experience has particularly strong effects on cortical development. The [Hensch 2005][research_hensch_2005_critical_periods] critical periods review consolidated the modern molecular and cellular framework for critical period plasticity, and the considerable subsequent literature has documented the molecular mechanisms that open and close critical periods.

The critical period for language acquisition provides the classical example. Children exposed to language during the critical period achieve native-like proficiency, while individuals first exposed to language after the critical period show significant residual deficits regardless of subsequent training. This account has substantial empirical support from studies of deaf children with variable ages of first language exposure and from studies of second-language acquisition across the lifespan.

Cortical maturation follows a spatial trajectory with sensory and motor cortices maturing first, followed by association cortices, and prefrontal cortex maturing last through adolescence and early adulthood. The [Casey Tottenham Liston Durston 2005][research_casey_et_al_2005] imaging developmental brain framework provided the modern quantitative treatment through structural and functional MRI studies.

Myelination follows a developmental trajectory that continues through adolescence and into early adulthood. The framework has been extensively documented through diffusion tensor imaging studies and provides evidence for the role of myelination in the developmental progression of cognitive capabilities. The [Petanjek Judas Simic Rasin Uylings Rakic Kostovic 2011][research_petanjek_et_al_2011] extended synaptic pruning study documented the prolonged period of prefrontal-cortex pruning that extends into the third decade of life, providing quantitative evidence for the extended developmental window of human prefrontal maturation.

The [Rakic 1988][research_rakic_1988] specification of cerebral cortical areas framework provided the systematic account of cortical development through the radial-unit hypothesis of cortical formation, and this formulation has markedly organized subsequent developmental neuroanatomy research.

Experience-dependent plasticity operates throughout the lifespan but shows patterns of intensity across developmental time. The Hensch 2005 framework identified the molecular brakes that limit plasticity in adult cortex, and subsequent work has identified interventions that reopen critical-period-like plasticity in adults.

The relationship between cortical maturation and cognitive development is characterized by the pattern in which brain regions that mature later support cognitive functions that emerge later in development. Prefrontal cortex maturation through adolescence supports the emergence of executive function, abstract reasoning, and long-horizon planning that characterizes late adolescent cognitive development.

Karmiloff-Smith's [Karmiloff-Smith 1992][book_karmiloff_smith_1992] Beyond Modularity provided the framework for understanding the relationship between cortical modularity and developmental change. The model proposes that cortical modules emerge through development rather than being innately specified, and that the process of representational redescription supports the transition from behavioral competence to explicit metacognitive awareness.

Article fourteen returns to the NeuroAI bridge and treats the correspondence between developmental learning in biological brains and machine learning developmental systems in greater detail.

## Comparative Developmental Cognition

Comparative developmental cognition treats the study of cognitive development across species. This formulation provides both empirical constraints on the evolutionary origins of human cognitive capabilities and the comparative data through which claims about human uniqueness can be systematically evaluated.

The [Tomasello and Call 1997][book_tomasello_call_1997] Primate Cognition consolidated the modern comparative primate cognition literature and identified the cognitive capabilities of great apes across social cognition, tool use, and communication. The treatment provides the empirical grounding for the marked cognitive continuities and human-unique adaptations that characterize human evolution.

Machiavellian intelligence of [Byrne and Whiten 1988][book_byrne_whiten_1988] introduced the hypothesis that primate intelligence evolved through the selective pressure of social interactions in large complex groups. This account has extensive empirical support from cross-species comparisons of brain size, social group size, and cognitive capabilities.

Dog cognition has received sizable attention through the [Miklosi 2007][book_miklosi_2007] Dog Behaviour Evolution and Cognition and the appreciable subsequent literature. The framework documents the cognitive capabilities of domesticated dogs including the human-oriented social cognition that appears specifically adapted to the ecology of human-canine cooperation. The [Hare and Woods 2005][research_hare_woods_2005] dog cognition framework documented the comparative empirical evidence for dog social cognition versus wolves and chimpanzees.

Corvid cognition of [Emery and Clayton 2004][research_emery_clayton_2004] demonstrated the advanced cognitive capabilities of the corvid family including planning, mental time travel, and tool manufacture despite the considerable phylogenetic distance from primates. The account provides evidence for the convergent evolution of intelligence and identifies the structural properties of intelligent nervous systems that transcend the mammalian lineage.

Dolphin cognition has been extensively studied through the [Herman 1980][research_herman_1980_dolphins_a262] and subsequent work identifying the capabilities of dolphins for observational learning, imitation, and symbolic communication. The model provides comparative evidence for the cognitive continuities across marine mammals and terrestrial mammals.

Chimpanzee mirror self-recognition of [Gallup 1970][research_gallup_1970_mirror_a262] provided the empirical evidence for self-recognition in non-human primates. This formulation has been extended to other species including elephants, dolphins, and some corvid species, and provides the comparative test of self-awareness across evolutionary lineages.

The [Thinking Ape framework of Byrne 1995][book_byrne_1995_thinking_ape] provided the systematic account of primate cognition and its evolutionary origins. The treatment identifies the cognitive adaptations that characterize the great apes and provides the evolutionary background against which human cognitive development must be understood.

Comparative developmental cognition provides the empirical framework through which claims about the developmental origins of human cognitive capabilities can be systematically tested. This account has appreciably shaped subsequent developmental psychology, evolutionary psychology, and cognitive science through the comparative data on the developmental origins and evolutionary conservation of cognitive capabilities.

Modern artificial cognitive systems increasingly recognize the value of the comparative cognition literature for understanding the architectural principles that support intelligent behavior. The framework provides an alternative to the exclusively-human-focused developmental psychology through the attention to the diversity of cognitive strategies across species.

## Load-Bearing Open Questions

- What is the correct algorithmic framework for developmental learning that combines intrinsic motivation, curriculum construction, and cross-embodiment transfer at foundation-model scale?
- How closely do the core knowledge systems documented in developmental psychology correspond to the inductive biases that machine learning systems require for human-like generalization?
- What is the correct treatment of the innateness-versus-learning trade-off in artificial developmental systems?
- How should embodied AI systems be evaluated? Current benchmarks focus on tasks rather than on the developmental trajectories that characterize genuine developmental capability emergence.
- Can the patterns of critical-period plasticity be reproduced in artificial systems, and would this be beneficial or detrimental for artificial learning?
- What is the correct account of the role of morphology in cognition, and can this account guide the design of embodied AI systems?
- How closely do the developmental trajectories produced by intrinsic-motivation-based artificial agents correspond to the trajectories observed in human infants and children?
- Can symbol grounding be genuinely solved through the modern foundation model plus embodiment paradigm, or are there residual challenges that require distinct algorithmic responses?
- What is the correct treatment of the role of social scaffolding and joint attention in artificial developmental systems?
- How should developmental learning be integrated with the modern machine learning practice of large-scale pretraining plus fine-tuning?

## References

### Books

- [Baldassarre and Mirolli 2013 Intrinsically Motivated Learning][book_baldassarre_mirolli_2013]
- [Barrett 2017 How Emotions Are Made][book_barrett_2017]
- [Berlyne 1960 Conflict Arousal Curiosity][book_berlyne_1960]
- [Bernstein 1967 Coordination of Movements][book_bernstein_1967]
- [Bloom 2000 How Children Learn Meanings][book_bloom_2000]
- [Bloom 2004 Descartes' Baby][book_bloom_2004]
- [Bruner 1983 Child's Talk][book_bruner_1983]
- [Byrne 1995 Thinking Ape][book_byrne_1995_thinking_ape]
- [Byrne and Whiten 1988 Machiavellian Intelligence][book_byrne_whiten_1988]
- [Cangelosi and Asada 2022 Cognitive Robotics][book_cangelosi_asada_2022]
- [Cangelosi and Schlesinger 2015 Developmental Robotics][book_cangelosi_schlesinger_2015]
- [Carey 2009 Origin of Concepts][book_carey_2009]
- [Case 1985 Intellectual Development][book_case_1985]
- [Chemero 2009 Radical Embodied][book_chemero_2009]
- [Clark 1997 Being There][book_clark_1997]
- [Clark 2016 Surfing Uncertainty][book_clark_2016]
- [Damasio 1994 Descartes' Error][book_damasio_1994]
- [Elman et al 1996 Rethinking Innateness][book_elman_et_al_1996]
- [Gibson 1979 Ecological Approach][book_gibson_1979]
- [Hohwy 2013 Predictive Mind][book_hohwy_2013]
- [Karmiloff-Smith 1992 Beyond Modularity][book_karmiloff_smith_1992]
- [Kellman and Arterberry 2006 Cradle of Knowledge][book_kellman_arterberry_2006]
- [Mareschal et al 2007 Neuroconstructivism][book_mareschal_et_al_2007_neuroconstructivism]
- [Maturana and Varela 1980 Autopoiesis][book_maturana_varela_1980]
- [Merleau-Ponty 1945 Phenomenology of Perception][book_merleau_ponty_1945]
- [Miklosi 2007 Dog Behaviour][book_miklosi_2007]
- [Noë 2004 Action in Perception][book_noe_2004]
- [Panksepp 1998 Affective Neuroscience][book_panksepp_1998]
- [Pfeifer and Bongard 2006 How the Body Shapes][book_pfeifer_bongard_2006]
- [Piaget 1952 Origins of Intelligence][book_piaget_1952]
- [Piaget 1962 Play Dreams Imitation][book_piaget_1962_play]
- [Picard 1997 Affective Computing][book_picard_1997]
- [Reddy 2008 How Infants Know Minds][book_reddy_2008]
- [Sroufe 1996 Emotional Development][book_sroufe_1996]
- [Suchman 1987 Plans and Situated Actions][book_suchman_1987]
- [Sutton and Barto 2018][book_sutton_barto_2018]
- [Thelen and Smith 1994 Dynamic Systems][book_thelen_smith_1994]
- [Thompson 2007 Mind in Life][book_thompson_2007]
- [Tomasello 2003 Constructing a Language][book_tomasello_2003_constructing]
- [Tomasello and Call 1997 Primate Cognition][book_tomasello_call_1997]
- [Varela Thompson Rosch 1991 The Embodied Mind][book_varela_thompson_rosch_1991]
- [Vygotsky 1978 Mind in Society][book_vygotsky_1978]

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
- [A258 Machines That Learn From Experience Meta-Learning and Online Adaptation][related_post_a258_meta_learning]
- [A259 Machines That Learn From Experience Continual and Lifelong Learning][related_post_a259_continual]
- [A260 Machines That Learn From Experience Learning From Demonstration Preference and Other Agents][related_post_a260_demonstration]
- [A261 Machines That Learn From Experience Evolutionary and Open-Ended Adaptation][related_post_a261_evolutionary]

### Research

- [Amsterdam 1972 Mirror][research_amsterdam_1972]
- [Anderson 2003 Field Guide][research_anderson_2003_field_guide]
- [Asada et al 2001 Cognitive Dev Robotics][research_asada_et_al_2001_cognitive_dev]
- [Asada et al 2009][research_asada_et_al_2009]
- [Aslin and Newport 2014 Statistical Learning][research_aslin_newport_2014]
- [Baddeley 2003 Working Memory][research_baddeley_2003_wm]
- [Bach-y-Rita 1969 Sensory Substitution][research_bach_y_rita_1969]
- [Baillargeon 1987][research_baillargeon_1987]
- [Baillargeon Spelke Wasserman 1985][research_baillargeon_spelke_wasserman_1985]
- [Baranes and Oudeyer 2013 Playful][research_baranes_oudeyer_2013_playful]
- [Barsalou 2008 Grounded Cognition][research_barsalou_2008_grounded]
- [Barto 2013 Intrinsic Motivation][research_barto_2013]
- [Battaglia Hamrick Tenenbaum 2013 Physics][research_battaglia_hamrick_tenenbaum_2013]
- [Beer 1995 Dynamical Systems][research_beer_1995]
- [Bengio et al 2009 Curriculum Learning][research_bengio_et_al_2009_curriculum]
- [Bisk et al 2020 Experience Grounds Language][research_bisk_et_al_2020_experience]
- [Bongard Zykov Lipson 2006 Self-Modeling][research_bongard_zykov_lipson_2006_a262]
- [Botvinick and Cohen 1998 Rubber Hand][research_botvinick_cohen_1998]
- [Brooks 1990 Elephants][research_brooks_1990_elephants]
- [Brooks 1991 Intelligence][research_brooks_1991_intelligence]
- [Bruner 1972 Nature of Immaturity][research_bruner_1972_play]
- [Carey and Bartlett 1978 Fast Mapping][research_carey_bartlett_1978]
- [Casey et al 2005 Imaging Developmental Brain][research_casey_et_al_2005]
- [Chai et al 2018 Grounded Language][research_chai_et_al_2018_grounded]
- [Clark and Chalmers 1998 Extended Mind][research_clark_chalmers_1998]
- [Colas et al 2022 Autotelic][research_colas_et_al_2022_autotelic]
- [Csibra and Gergely 2009 Natural Pedagogy][research_csibra_gergely_2009]
- [Damasio Everitt Bishop 1996 Somatic Marker][research_damasio_everitt_bishop_1996]
- [Das et al 2018 EQA][research_das_et_al_2018_eqa]
- [Diamond 2013 Executive Functions][research_diamond_2013]
- [Elman 1993 Less is More][research_elman_1993_less]
- [Emery and Clayton 2004 Corvids][research_emery_clayton_2004]
- [Fantz 1961 Visual Preferences][research_fantz_1961]
- [Feigenson Dehaene Spelke 2004 Number][research_feigenson_dehaene_spelke_2004]
- [Feldman and Friston 2010 Precision][research_feldman_friston_2010]
- [Fischer 1980 Skill Theory][research_fischer_1980]
- [Forestier et al 2022 IMGEP][research_forestier_et_al_2022_imgep]
- [Frank Tenenbaum Fernald 2013 Bayesian Word][research_frank_tenenbaum_fernald_2013]
- [Friston 2010 Free Energy Principle][research_friston_2010_fep]
- [Friston et al 2015 Active Inference][research_friston_et_al_2015_active_inference]
- [Gallup 1970 Mirror Recognition][research_gallup_1970_mirror]
- [Gan et al 2020 ThreeDWorld][research_gan_et_al_2020_tdw]
- [Gergely and Watson 1999 Contingency][research_gergely_watson_1999]
- [Haggard 2005 Agency][research_haggard_2005_agency]
- [Hamlin Wynn Bloom 2007][research_hamlin_wynn_bloom_2007]
- [Hare and Woods 2005 Dog Cognition][research_hare_woods_2005]
- [Harnad 1990 Symbol Grounding][research_harnad_1990_symbol_grounding]
- [Head and Holmes 1911][research_head_holmes_1911]
- [Hensch 2005 Critical Periods][research_hensch_2005_critical_periods]
- [Herman 1980 Dolphins][research_herman_1980_dolphins_a262]
- [Hubel and Wiesel 1970][research_hubel_wiesel_1970]
- [Huttenlocher 1979 Synaptic Density][research_huttenlocher_1979]
- [Ijspeert et al 2013 DMP][research_ijspeert_et_al_2013_dmp_a262]
- [James et al 2020 RLBench][research_james_et_al_2020_rlbench]
- [Jeannerod 2003 Sense of Agency][research_jeannerod_2003_agency]
- [Kaplan and Hafner 2006 Joint Attention][research_kaplan_hafner_2006]
- [Kellman and Spelke 1983 Occluded][research_kellman_spelke_1983]
- [Kirchhoff et al 2018 Markov Blankets][research_kirchhoff_et_al_2018]
- [Klyubin Polani Nehaniv 2005 Empowerment][research_klyubin_polani_nehaniv_2005_empowerment]
- [Kohler 1962 Inverted Vision][research_kohler_1962]
- [Kolve et al 2017 AI2-THOR][research_kolve_et_al_2017_ai2thor]
- [Körding and Wolpert 2004 Bayesian Motor][research_kording_wolpert_2004]
- [Kumar Packer Koller 2010 Self-Paced][research_kumar_packer_koller_2010]
- [Lake Ullman Tenenbaum Gershman 2017][research_lake_ullman_tenenbaum_gershman_2017]
- [Lungarella et al 2003 Developmental Robotics][research_lungarella_et_al_2003]
- [Meltzoff and Moore 1997 Explaining Facial Imitation][research_meltzoff_moore_1997_babbling]
- [Metta et al 2008 iCub][research_metta_et_al_2008_icub]
- [Millidge Tschantz Buckley 2021 PC Review][research_millidge_tschantz_buckley_2021]
- [Miyake and Friedman 2012 Unity EF][research_miyake_friedman_2012]
- [Miyake et al 2000 Unity and Diversity][research_miyake_et_al_2000]
- [Mussa-Ivaldi and Solla 2004 Motor Primitives][research_mussa_ivaldi_solla_2004]
- [Nagai et al 2003 Joint Attention][research_nagai_et_al_2003]
- [Ororbia and Kifer 2020 Neural Generative Coding][research_ororbia_kifer_2020_neural_generative]
- [Oudeyer 2018 Developmental Robotics][research_oudeyer_2018_devrob]
- [Oudeyer Kaplan Hafner 2007 Intrinsic Motivation][research_oudeyer_kaplan_hafner_2007]
- [O'Regan and Noë 2001 Sensorimotor][research_oregan_noe_2001]
- [Pellegrini and Smith 1998 Play][research_pellegrini_smith_1998]
- [Petanjek et al 2011 Extended Pruning][research_petanjek_et_al_2011]
- [Pfeifer and Iida 2005 Morphological Computation][research_pfeifer_iida_2005]
- [Philipona O'Regan Nadal 2003 Sensorimotor Structure][research_philipona_oregan_nadal_2003]
- [Portelas et al 2019 Teacher-Student][research_portelas_et_al_2019_ts]
- [Portelas et al 2020 ACL Survey][research_portelas_et_al_2020_acl_a262]
- [Rakic 1988 Cortical Areas][research_rakic_1988]
- [Rao and Ballard 1999 Predictive Coding][research_rao_ballard_1999]
- [Rochat 2003 Self-Awareness Levels][research_rochat_2003]
- [Rothbart Ahadi Hershey 2001 Temperament][research_rothbart_ahadi_hershey_2001]
- [Roy 2005 Grounding Words][research_roy_2005]
- [Ruff 1984 Object Manipulation][research_ruff_1984]
- [Ryan and Deci 2000 Self-Determination][research_ryan_deci_2000]
- [Saffran Aslin Newport 1996 Statistical Learning][research_saffran_aslin_newport_1996]
- [Savva et al 2019 Habitat][research_savva_et_al_2019_habitat]
- [Scaife and Bruner 1975 Gaze Following][research_scaife_bruner_1975]
- [Schmidhuber 1991 Curiosity][research_schmidhuber_1991_curiosity]
- [Schmidhuber 2010 Formal Theory][research_schmidhuber_2010_formal]
- [Shadmehr and Krakauer 2008 Motor Control][research_shadmehr_krakauer_2008]
- [Spelke 1994 Core Knowledge][research_spelke_1994]
- [Spelke and Kinzler 2007 Core Knowledge][research_spelke_kinzler_2007]
- [Srivastava et al 2022 Behavior][research_srivastava_et_al_2022_behavior]
- [Steels 2003 Grounding][research_steels_2003_grounding]
- [Sullivan et al 2021 SAYCam][research_sullivan_et_al_2021_saycam]
- [Szot et al 2021 Habitat 2.0][research_szot_et_al_2021_habitat2]
- [Todorov and Jordan 2002 OFC][research_todorov_jordan_2002_ofc]
- [Tomasello 1995 Joint Attention][research_tomasello_1995_joint]
- [Trevarthen 1979 Intersubjectivity][research_trevarthen_1979]
- [Tschantz et al 2020 AI RL][research_tschantz_et_al_2020_ai_rl]
- [van Gelder 1998 Dynamical Hypothesis][research_van_gelder_1998]
- [Wellman Cross Watson 2001 ToM Meta-Analysis][research_wellman_cross_watson_2001]
- [Weng et al 2001 Autonomous Mental Development][research_weng_et_al_2001]
- [White 1959 Effectance][research_white_1959]
- [Wilson 2002 Six Views][research_wilson_2002_six_views]
- [Wolpert Ghahramani Jordan 1995 Forward Model][research_wolpert_ghahramani_jordan_1995]
- [Woodward 1998 Agency][research_woodward_1998_agency]
- [Wynn 1992 Numerical][research_wynn_1992]
- [Xia et al 2020 iGibson][research_xia_et_al_2020_igibson]
- [Xu and Tenenbaum 2007 Word Learning][research_xu_tenenbaum_2007]
- [Yu and Smith 2007 Cross-Situational][research_yu_smith_2007]
- [Zelazo 2006 DCCS][research_zelazo_2006_dccs]
- [Zelazo 2015 EF Development][research_zelazo_2015]

[book_baldassarre_mirolli_2013]: https://link.springer.com/book/10.1007/978-3-642-32375-1
[book_barrett_2017]: https://mariner.hmhco.com/9781328915436/how-emotions-are-made/
[book_berlyne_1960]: https://psycnet.apa.org/record/1961-01178-000
[book_bernstein_1967]: https://scholar.google.com/scholar?q=bernstein+1967+coordination+regulation+movements
[book_bloom_2000]: https://mitpress.mit.edu/9780262523295/how-children-learn-the-meanings-of-words/
[book_bloom_2004]: https://basicbooks.com/titles/paul-bloom/descartes-baby/9780465007844/
[book_bruner_1983]: https://global.oup.com/academic/product/childs-talk-9780393301632
[book_byrne_1995_thinking_ape]: https://global.oup.com/academic/product/the-thinking-ape-9780198522652
[book_byrne_whiten_1988]: https://global.oup.com/academic/product/machiavellian-intelligence-9780198521754
[book_cangelosi_asada_2022]: https://mitpress.mit.edu/9780262046831/cognitive-robotics/
[book_cangelosi_schlesinger_2015]: https://mitpress.mit.edu/9780262028011/developmental-robotics/
[book_carey_2009]: https://global.oup.com/academic/product/the-origin-of-concepts-9780199755387
[book_case_1985]: https://www.taylorfrancis.com/books/mono/10.4324/9780203772409/intellectual-development-birth-adulthood-robbie-case
[book_chemero_2009]: https://mitpress.mit.edu/9780262516471/radical-embodied-cognitive-science/
[book_clark_1997]: https://mitpress.mit.edu/9780262531566/being-there/
[book_clark_2016]: https://global.oup.com/academic/product/surfing-uncertainty-9780190933210
[book_damasio_1994]: https://us.macmillan.com/books/9780143036227
[book_elman_et_al_1996]: https://mitpress.mit.edu/9780262550307/rethinking-innateness/
[book_gibson_1979]: https://www.taylorfrancis.com/books/mono/10.4324/9781315740218/ecological-approach-visual-perception-james-gibson
[book_hohwy_2013]: https://global.oup.com/academic/product/the-predictive-mind-9780199686735
[book_karmiloff_smith_1992]: https://mitpress.mit.edu/9780262611145/beyond-modularity/
[book_kellman_arterberry_2006]: https://mitpress.mit.edu/9780262611763/the-cradle-of-knowledge/
[book_mareschal_et_al_2007_neuroconstructivism]: https://global.oup.com/academic/product/neuroconstructivism-vol-i-9780198529910
[book_maturana_varela_1980]: https://link.springer.com/book/10.1007/978-94-009-8947-4
[book_merleau_ponty_1945]: https://www.taylorfrancis.com/books/mono/10.4324/9780203994610/phenomenology-perception-maurice-merleau-ponty
[book_miklosi_2007]: https://global.oup.com/academic/product/dog-behaviour-evolution-and-cognition-9780199545667
[book_noe_2004]: https://mitpress.mit.edu/9780262640633/action-in-perception/
[book_panksepp_1998]: https://global.oup.com/academic/product/affective-neuroscience-9780195178050
[book_pfeifer_bongard_2006]: https://mitpress.mit.edu/9780262162395/how-the-body-shapes-the-way-we-think/
[book_piaget_1952]: https://www.taylorfrancis.com/books/mono/10.4324/9781315006200/origins-intelligence-children-jean-piaget
[book_piaget_1962_play]: https://www.taylorfrancis.com/books/mono/10.4324/9781315006420/play-dreams-imitation-childhood-jean-piaget
[book_picard_1997]: https://mitpress.mit.edu/9780262661157/affective-computing/
[book_reddy_2008]: https://www.hup.harvard.edu/books/9780674032064
[book_sroufe_1996]: https://www.cambridge.org/core/books/emotional-development/8B7CE64EB0DB3EE7FBBD8F09E15DBB4C
[book_suchman_1987]: https://www.cambridge.org/core/books/plans-and-situated-actions/E4A1A5F7E9DBFA76C60D66E5E32C42BF
[book_sutton_barto_2018]: http://incompleteideas.net/book/the-book-2nd.html
[book_thelen_smith_1994]: https://mitpress.mit.edu/9780262700597/a-dynamic-systems-approach-to-the-development-of-cognition-and-action/
[book_thompson_2007]: https://www.hup.harvard.edu/books/9780674025110
[book_tomasello_2003_constructing]: https://www.hup.harvard.edu/books/9780674017641
[book_tomasello_call_1997]: https://global.oup.com/academic/product/primate-cognition-9780195106237
[book_varela_thompson_rosch_1991]: https://mitpress.mit.edu/9780262529365/the-embodied-mind/
[book_vygotsky_1978]: https://www.hup.harvard.edu/books/9780674576292
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
[research_amsterdam_1972]: https://onlinelibrary.wiley.com/doi/10.1002/dev.420050403
[research_anderson_2003_field_guide]: https://www.sciencedirect.com/science/article/abs/pii/S0004370203000546
[research_asada_et_al_2001_cognitive_dev]: https://ieeexplore.ieee.org/document/954823
[research_asada_et_al_2009]: https://ieeexplore.ieee.org/document/4838369
[research_aslin_newport_2014]: https://onlinelibrary.wiley.com/doi/10.1111/cdep.12057
[research_bach_y_rita_1969]: https://www.nature.com/articles/221963a0
[research_baddeley_2003_wm]: https://www.nature.com/articles/nrn1201
[research_baillargeon_1987]: https://psycnet.apa.org/doi/10.1037/0012-1649.23.5.655
[research_baillargeon_spelke_wasserman_1985]: https://www.sciencedirect.com/science/article/abs/pii/0010027785900085
[research_baranes_oudeyer_2013_playful]: https://www.sciencedirect.com/science/article/pii/S0921889012001571
[research_barsalou_2008_grounded]: https://www.annualreviews.org/doi/10.1146/annurev.psych.59.103006.093639
[research_barto_2013]: https://link.springer.com/chapter/10.1007/978-3-642-32375-1_2
[research_battaglia_hamrick_tenenbaum_2013]: https://www.pnas.org/doi/10.1073/pnas.1306572110
[research_beer_1995]: https://www.sciencedirect.com/science/article/abs/pii/000437029400005L
[research_bengio_et_al_2009_curriculum]: https://dl.acm.org/doi/10.1145/1553374.1553380
[research_bisk_et_al_2020_experience]: https://aclanthology.org/2020.emnlp-main.703/
[research_bongard_zykov_lipson_2006_a262]: https://www.science.org/doi/10.1126/science.1133687
[research_botvinick_cohen_1998]: https://www.nature.com/articles/35784
[research_brooks_1990_elephants]: https://people.csail.mit.edu/brooks/papers/elephants.pdf
[research_brooks_1991_intelligence]: https://www.sciencedirect.com/science/article/abs/pii/000437029190053M
[research_bruner_1972_play]: https://psycnet.apa.org/doi/10.1037/h0033144
[research_carey_bartlett_1978]: https://scholar.google.com/scholar?q=carey+bartlett+1978+acquiring+single+new+word
[research_casey_et_al_2005]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(05)00027-1
[research_chai_et_al_2018_grounded]: https://arxiv.org/abs/1802.06025
[research_clark_chalmers_1998]: https://academic.oup.com/analysis/article-abstract/58/1/7/125076
[research_colas_et_al_2022_autotelic]: https://jmlr.org/papers/v24/21-0808.html
[research_csibra_gergely_2009]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(09)00034-4
[research_damasio_everitt_bishop_1996]: https://royalsocietypublishing.org/doi/10.1098/rstb.1996.0125
[research_das_et_al_2018_eqa]: https://openaccess.thecvf.com/content_cvpr_2018/html/Das_Embodied_Question_Answering_CVPR_2018_paper.html
[research_diamond_2013]: https://www.annualreviews.org/doi/10.1146/annurev-psych-113011-143750
[research_elman_1993_less]: https://www.sciencedirect.com/science/article/abs/pii/0010027793900584
[research_emery_clayton_2004]: https://www.science.org/doi/10.1126/science.1098410
[research_fantz_1961]: https://www.science.org/doi/10.1126/science.140.3564.296
[research_feigenson_dehaene_spelke_2004]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(04)00164-6
[research_feldman_friston_2010]: https://www.frontiersin.org/articles/10.3389/fnhum.2010.00215/full
[research_fischer_1980]: https://psycnet.apa.org/doi/10.1037/0033-295X.87.6.477
[research_forestier_et_al_2022_imgep]: https://jmlr.org/papers/v23/21-0808.html
[research_frank_tenenbaum_fernald_2013]: https://www.sciencedirect.com/science/article/pii/S0022249612000958
[research_friston_2010_fep]: https://www.nature.com/articles/nrn2787
[research_friston_et_al_2015_active_inference]: https://link.springer.com/article/10.1007/s10339-015-0710-0
[research_gallup_1970_mirror]: https://www.science.org/doi/10.1126/science.167.3914.86
[research_gallup_1970_mirror_a262]: https://www.science.org/doi/10.1126/science.167.3914.86
[research_gan_et_al_2020_tdw]: https://arxiv.org/abs/2007.04954
[research_gergely_watson_1999]: https://scholar.google.com/scholar?q=gergely+watson+1999+contingency+detection+self
[research_haggard_2005_agency]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(05)00082-9
[research_hamlin_wynn_bloom_2007]: https://www.nature.com/articles/nature06288
[research_hare_woods_2005]: https://www.cell.com/current-biology/fulltext/S0960-9822(05)00958-2
[research_harnad_1990_symbol_grounding]: https://www.sciencedirect.com/science/article/abs/pii/016727899090087A
[research_head_holmes_1911]: https://academic.oup.com/brain/article-abstract/34/2-3/102/278729
[research_hensch_2005_critical_periods]: https://www.nature.com/articles/nrn1787
[research_herman_1980_dolphins_a262]: https://link.springer.com/chapter/10.1007/978-1-4684-3606-5_9
[research_hubel_wiesel_1970]: https://physoc.onlinelibrary.wiley.com/doi/10.1113/jphysiol.1970.sp009022
[research_huttenlocher_1979]: https://www.sciencedirect.com/science/article/abs/pii/0006899379903494
[research_ijspeert_et_al_2013_dmp_a262]: https://www.mitpressjournals.org/doi/10.1162/NECO_a_00393
[research_james_et_al_2020_rlbench]: https://ieeexplore.ieee.org/document/8972362
[research_jeannerod_2003_agency]: https://www.sciencedirect.com/science/article/abs/pii/S1053810003000814
[research_kaplan_hafner_2006]: https://www.worldscientific.com/doi/abs/10.1142/S0219843606000710
[research_kellman_spelke_1983]: https://www.sciencedirect.com/science/article/abs/pii/0010028583900149
[research_kirchhoff_et_al_2018]: https://royalsocietypublishing.org/doi/10.1098/rsif.2017.0792
[research_klyubin_polani_nehaniv_2005_empowerment]: https://ieeexplore.ieee.org/document/1554676
[research_kohler_1962]: https://scholar.google.com/scholar?q=kohler+1962+experiments+world+with+distorting+spectacles
[research_kolve_et_al_2017_ai2thor]: https://arxiv.org/abs/1712.05474
[research_kording_wolpert_2004]: https://www.nature.com/articles/nature02169
[research_kumar_packer_koller_2010]: https://papers.nips.cc/paper/2010/hash/e57c6b956a6521b28495f2886ca0977a-Abstract.html
[research_lake_ullman_tenenbaum_gershman_2017]: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/building-machines-that-learn-and-think-like-people/A9535B1D745A0377E16C590E14B94993
[research_lungarella_et_al_2003]: https://ieeexplore.ieee.org/document/1245676
[research_meltzoff_moore_1997_babbling]: https://www.tandfonline.com/doi/abs/10.1080/095407997116775
[research_metta_et_al_2008_icub]: https://link.springer.com/article/10.1007/s10339-008-0234-y
[research_millidge_tschantz_buckley_2021]: https://arxiv.org/abs/2107.12979
[research_miyake_et_al_2000]: https://www.sciencedirect.com/science/article/abs/pii/S0010028599907343
[research_miyake_friedman_2012]: https://journals.sagepub.com/doi/10.1177/0963721411429458
[research_mussa_ivaldi_solla_2004]: https://link.springer.com/chapter/10.1007/978-3-540-27835-1_17
[research_nagai_et_al_2003]: https://ieeexplore.ieee.org/document/1207344
[research_oregan_noe_2001]: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/sensorimotor-account-of-vision-and-visual-consciousness/E9DBB3DFA36BDCC02C9A2A15D5DDFCED
[research_ororbia_kifer_2020_neural_generative]: https://www.nature.com/articles/s41467-022-29632-7
[research_oudeyer_2018_devrob]: https://link.springer.com/chapter/10.1007/978-3-030-03551-2_18
[research_oudeyer_kaplan_hafner_2007]: https://ieeexplore.ieee.org/document/4141061
[research_pellegrini_smith_1998]: https://srcd.onlinelibrary.wiley.com/doi/10.1111/1467-8624.00047
[research_petanjek_et_al_2011]: https://www.pnas.org/doi/10.1073/pnas.1105108108
[research_pfeifer_iida_2005]: https://ieeexplore.ieee.org/document/1545090
[research_philipona_oregan_nadal_2003]: https://direct.mit.edu/neco/article-abstract/15/9/2029/6771
[research_portelas_et_al_2019_ts]: https://proceedings.mlr.press/v100/portelas20a.html
[research_portelas_et_al_2020_acl_a262]: https://arxiv.org/abs/2003.04664
[research_rakic_1988]: https://www.science.org/doi/10.1126/science.3291116
[research_rao_ballard_1999]: https://www.nature.com/articles/nn0199_79
[research_rochat_2003]: https://www.sciencedirect.com/science/article/abs/pii/S1053810003000817
[research_rothbart_ahadi_hershey_2001]: https://srcd.onlinelibrary.wiley.com/doi/10.1111/1467-8624.00355
[research_roy_2005]: https://www.sciencedirect.com/science/article/abs/pii/S1364661305001737
[research_ruff_1984]: https://srcd.onlinelibrary.wiley.com/doi/10.2307/1130035
[research_ryan_deci_2000]: https://psycnet.apa.org/doi/10.1037/0003-066X.55.1.68
[research_saffran_aslin_newport_1996]: https://www.science.org/doi/10.1126/science.274.5294.1926
[research_savva_et_al_2019_habitat]: https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html
[research_scaife_bruner_1975]: https://www.nature.com/articles/253265a0
[research_schmidhuber_1991_curiosity]: https://ieeexplore.ieee.org/document/170605
[research_schmidhuber_2010_formal]: https://ieeexplore.ieee.org/document/5590297
[research_shadmehr_krakauer_2008]: https://link.springer.com/article/10.1007/s00221-008-1280-5
[research_spelke_1994]: https://www.sciencedirect.com/science/article/abs/pii/0010027794900272
[research_spelke_kinzler_2007]: https://onlinelibrary.wiley.com/doi/10.1111/j.1467-7687.2007.00569.x
[research_srivastava_et_al_2022_behavior]: https://proceedings.mlr.press/v164/srivastava22a.html
[research_steels_2003_grounding]: https://link.springer.com/chapter/10.1007/978-3-540-24616-9_5
[research_sullivan_et_al_2021_saycam]: https://direct.mit.edu/opmi/article/doi/10.1162/opmi_a_00039/97482
[research_szot_et_al_2021_habitat2]: https://papers.nips.cc/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html
[research_todorov_jordan_2002_ofc]: https://www.nature.com/articles/nn963
[research_tomasello_1995_joint]: https://scholar.google.com/scholar?q=tomasello+1995+joint+attention+social+cognition
[research_trevarthen_1979]: https://scholar.google.com/scholar?q=trevarthen+1979+communication+cooperation+infancy
[research_tschantz_et_al_2020_ai_rl]: https://ieeexplore.ieee.org/document/9207382
[research_van_gelder_1998]: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/dynamical-hypothesis-in-cognitive-science/A80AB57E4E1D68C1E9C05E1A87D2E7D8
[research_wellman_cross_watson_2001]: https://onlinelibrary.wiley.com/doi/10.1111/1467-8624.00304
[research_weng_et_al_2001]: https://www.science.org/doi/10.1126/science.291.5504.599
[research_white_1959]: https://psycnet.apa.org/doi/10.1037/h0040934
[research_wilson_2002_six_views]: https://link.springer.com/article/10.3758/BF03196322
[research_wolpert_ghahramani_jordan_1995]: https://www.science.org/doi/10.1126/science.7569931
[research_woodward_1998_agency]: https://www.sciencedirect.com/science/article/abs/pii/S0010027798000584
[research_wynn_1992]: https://www.nature.com/articles/358749a0
[research_xia_et_al_2020_igibson]: https://arxiv.org/abs/2012.02924
[research_xu_tenenbaum_2007]: https://psycnet.apa.org/doi/10.1037/0033-295X.114.2.245
[research_yu_smith_2007]: https://onlinelibrary.wiley.com/doi/10.1111/j.1467-9280.2007.01915.x
[research_zelazo_2006_dccs]: https://www.nature.com/articles/nprot.2006.46
[research_zelazo_2015]: https://onlinelibrary.wiley.com/doi/10.1111/cdep.12118
