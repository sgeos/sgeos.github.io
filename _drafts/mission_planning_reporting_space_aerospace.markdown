---
layout: post
mathjax: true
comments: true
title: "Mission Planning and Reporting Standards in Space Agencies"
date: 2026-11-09 09:00:00 +0000
categories: aerospace engineering space
---

<!-- A393 -->
<script>console.log("A393");</script>

Space agencies write a mission down three times.
They write it before flight as a plan,
during flight as rules and procedures,
and after flight as a report.
This article surveys the documents that hold those three accounts.
It draws on the directives and handbooks of the National Aeronautics and Space Administration,
NASA,
on the standards of the European Cooperation for Space Standardization,
ECSS,
and on documents of the European Space Agency,
ESA.
It also surveys a fourth account,
which an agency writes when it flies a mission in an analogue,
a simulator
or a model,
and which states how the stand-in differs from the real thing.

The survey finds that the two regimes share a structure.
Each divides a project into phases,
closes each phase with a review,
and gives the decision to proceed to a named authority that is not the review team.
Each asks for the same accounts of a mission under different names.
The survey also finds that several common beliefs about these documents are wrong.
The European standards define no document called a concept of operations,
no mission requirements document
and no mission success criteria.
NASA offers its tables of review criteria as recommended practice and not as mandatory text.
The NASA mission reports examined compare planned and actual values in their consumables and performance tables,
and not in their sequences of events.
On the stand-in the survey finds no single governing standard.
It finds four bodies of practice whose records overlap,
in the author's reading,
on the intended use,
the assumptions
and the limits.
The NASA standard for models and simulations adds the permissible uses
and a warning whenever a result leaves the domain in which someone validated the stand-in.

The article has four parts.
The first describes the documents in the order of a mission,
from the life cycle and its reviews
through the concept of operations,
the requirements and success criteria,
the design reference mission,
the mission analysis,
the flight rules
and the readiness reviews
to the operations documents and the reports after flight.
The second describes how agencies document a stand-in,
and closes with a worked comparison of the planet Venus and its counterpart in a commercial spaceflight game.
The third draws out what the regimes share and where they differ.
The fourth consolidates the survey into three structures that a small programme can use,
namely a mission plan,
a mission report
and a section on differences from the real environment.
The description of each document rests on the document itself.
The synthesis and the three structures are the author's,
and the [Epistemic State](#epistemic-state) section separates the two.

The article does not teach mission design or orbital mechanics,
and it derives no trajectory.
It describes what the documents contain,
and it does not judge whether anyone planned a mission well.

## Kinds of Document

Five kinds of document recur.

- **The plan.**
  It states,
  before flight,
  what the mission is for,
  what counts as success,
  how the mission will proceed
  and on what assumptions and budgets the design rests.
- **The rule and the procedure.**
  A rule records a decision that the operators took in advance.
  A procedure records the steps of one action.
  Both exist before flight and govern it.
- **The review record.**
  It states the criteria of a gate,
  the findings,
  the decision
  and who took the decision.
- **The report.**
  It states,
  after flight,
  what happened against what the plan foresaw,
  which objectives the mission met
  and what went wrong.
- **The statement of limits.**
  It states how a model,
  a simulator
  or an analogue differs from the system it stands for,
  and what a result obtained there may support.

The two regimes name these documents differently.

| Subject | NASA | European standards |
|---|---|---|
| The gate between phases | Key decision point, decided by the Decision Authority | End of phase review, with the decision taken by the customer |
| How the system will be used | Concept of operations, then operations concept | Mission description document, then mission operations concept document |
| The need behind the mission | Stakeholder expectations | Mission statement |
| A reference scenario | Design reference mission | Operations scenario |
| What success means | Mission success criteria and minimum mission success criteria | Mission success, defined once in the operations standard |
| The plan for operations | Mission Operations Plan, a control plan of the Project Plan | Mission operations plan |
| Decisions taken in advance | Flight rules and launch commit criteria | Mission rules, among them launch hold criteria |
| Permission to launch | Certification of flight readiness | Authorisation to proceed for launch |
| The account after flight | Mission report and Final Mission Report | Mission reports, with contents left open |

The pairs in the table are the author's alignment and not a mapping that either regime states.
The sections below give the text behind each row.

## The Life Cycle and Its Reviews

Both regimes divide a project into phases and place a review at the end of each.
They differ in who decides that the project may proceed,
and in how much of a review they fix in advance.

### NASA Phases and Key Decision Points

NASA governs space flight projects with NASA Procedural Requirements 7120.5F,
which stands at Change 4 of 14 November 2024
[NASA 2024a][agency_nasa_npr_7120_5f].
Its status needs a caution.
The page for this directive in the agency's directives library states that an interim directive,
NID 7120.148,
"is the interim directive to NPR 7120.5F and contains the most recent requirements."
NPR stands for NASA Procedural Requirements and NID for NASA Interim Directive.
The interim directive took effect on 9 December 2024
and prints an expiration date of 9 December 2025
[NASA 2024b][agency_nasa_nid_7120_148].
That date had passed when the author read the page in November 2026,
and the page still pointed to the interim text.
The author could not determine whether NASA extended it.
The interim directive reproduces the directive in full,
and its change history ends with the same Change 4.
Every passage that this article quotes from the directive appears in both texts.

The directive divides the life of a project into seven phases.
It groups Phases A and B as Formulation
and Phases C to F as Implementation.
The names below are those of the directive's Figure 2-5,
which the agency's management handbook repeats in its running text
[NASA 2022a][agency_nasa_pm_handbook_2022].

| Phase | Name | Opened by |
|---|---|---|
| Pre-Phase A | Concept Studies | Nothing. The phase precedes Key Decision Point A |
| Phase A | Concept and Technology Development | Key Decision Point A, after the Mission Concept Review |
| Phase B | Preliminary Design and Technology Completion | Key Decision Point B |
| Phase C | Final Design and Fabrication | Key Decision Point C, which approves Implementation |
| Phase D | System Assembly, Integration and Test, and Launch and Checkout | Key Decision Point D |
| Phase E | Operations and Sustainment | Key Decision Point E, which precedes launch |
| Phase F | Closeout | Key Decision Point F, after the Decommissioning Review |

The directive defines the gate by who acts at it.
"A KDP is the event where the Decision Authority determines the readiness of a program or project to progress to the next phase of the life cycle and establishes the content, cost, and schedule commitments for the ensuing phase(s)."
KDP stands for key decision point.
One transition does not follow its decision at once.
"Transition to the following phase occurs immediately following KDP approval except for the transition from Phase D to E, where transition occurs following on-orbit checkout."

The directive names the Decision Authority by the category of the project.
"For programs and Category 1 projects, the Decision Authority is the NASA AA. The NASA AA may delegate this authority to the MDAA. For Category 2 and 3 projects, the Decision Authority is the MDAA."
AA stands for Associate Administrator
and MDAA for Mission Directorate Associate Administrator.
The decision therefore belongs to one named official.
That a review informs the decision and does not take it is the author's reading of the definition.

Two documents carry the mission through these gates.
The first is the Formulation Agreement,
which the project prepares to establish the technical and acquisition work of Formulation.
"The Agreement is approved and signed at KDP A and is updated and resubmitted for signature at KDP B."
The signatures are those of the Mission Directorate Associate Administrator,
the Center Director
and the programme manager.
The directive's template for the agreement has fifteen sections,
and
"Each section of the Formulation Agreement template is required."
The fifth section bears the title Mission Scenario, Architectures, and Interfaces.
It asks the project to
"Document the project's or single-project program's proposed milestones for producing the mission concept, mission scenario (or design reference mission), concept of operations, and mission, spacecraft, payload, and ground systems architectures down to the level of subsystem interfaces."
The section goes on to say what must accompany them.
"Documentation should include ground rules, assumptions, and constraints used for analysis; key architecture drivers, such as redundancy; preliminary key performance parameters; top-level technical parameters and associated margins; and preliminary driving requirements."

The second document is the Project Plan.
"Project Plan. The document that establishes the project's baseline for Implementation, signed by the responsible program manager, Center Director, project manager, and the MDAA, if required."
Here too
"Each section of the Project Plan template is required."
The template has six parts.

| Part | Title | Contents |
|---|---|---|
| 1.0 | Project Overview | Introduction, objectives, mission description and technical approach, authority and governance, stakeholder definition |
| 2.0 | Project Baselines | Requirements, work breakdown structure, schedule, resources, and the joint cost and schedule confidence level |
| 3.0 | Project Control Plans | Twenty-nine plans, among them the Verification and Validation Plan, the Review Plan, the Mission Operations Plan and the Knowledge Management Plan |
| 4.0 | Waivers or Deviations Log | The requirements of the directive for which the project has requested and received a waiver or a deviation |
| 5.0 | Change Log | The log of changes to the plan |
| 6.0 | Appendices | Acronyms, definitions and a compliance matrix for the directive |

The mission itself enters the plan in section 1.3.
"Describe briefly the mission and the mission design. Include mission objectives and goals, mission success criteria, and driving ground rules and assumptions affecting the mission and mission design. Identify key characteristics of the mission, such as launch date(s), flight plans, and the key phases and events on the mission timeline, including end of mission."
The same section asks the project to
"Describe planned mission results, data archiving, and reporting."
One paragraph of a NASA Project Plan therefore names the objectives,
the success criteria,
the assumptions
and the timeline,
and looks ahead to the report.

### NASA Reviews and the Status of Their Criteria

The life-cycle reviews of a project run in a fixed order,
of which the directive's figure gives the principal ones as follows.

1. Mission Concept Review.
2. System Requirements Review.
3. Mission Definition Review for a robotic project,
   or System Definition Review for a crewed one.
4. Preliminary Design Review.
5. Critical Design Review.
6. System Integration Review.
7. Operational Readiness Review.
8. Mission Readiness Review for a robotic project,
   or Flight Readiness Review for a crewed one.
9. Post-Launch Assessment Review.
10. Critical Event Readiness Review.
11. Post-Flight Assessment Review,
    for a crewed project only.
12. Decommissioning Review.
13. Disposal Readiness Review.

The figure also places a Production Readiness Review beside the Critical Design Review,
for a project that builds more than one copy.

The criteria for these reviews sit in a second directive,
NASA Procedural Requirements 7123.1D on systems engineering,
at Change 2 of 20 February 2024
[NASA 2024c][agency_nasa_npr_7123_1d].
A reader who takes its tables of entrance and success criteria for mandatory text misreads it.
The directive makes two things mandatory.
The first is that a project writes criteria at all.
"The technical team shall participate in the development of entrance and success criteria for each of the respective reviews"
is requirement SE-34 of its fifth chapter.
The second is a short list of minimum products at each review.
At the Operational Readiness Review the list holds preliminary verification and validation results
and baselined plans for decommissioning and for disposal.
At the Flight Readiness Review it holds baselined verification and validation results
and the final certification for flight or use.

The tables of criteria are a different kind of text.
They sit in Appendix G,
which says of itself that it
"describes the recommended best practices for entrance and success criteria for the life-cycle and technical reviews required in Chapter 5"
of the directive.
The appendix expects a project to change them.
"Tailoring and customizing are expected for projects and programs."
It asks only that
"The decision not to tailor and customize life-cycle review criteria should be justified to the ETA,"
where ETA stands for Engineering Technical Authority.
Inside the tables,
asterisks mark the products that a directive requires.
The glossary places the binding version of the criteria elsewhere.
"Success criteria are documented in the corresponding technical review plan."
The author infers from these passages that the appendix is guidance
and that the binding text for any one review is the plan the project wrote for it.

### European Phases and Reviews

The European counterpart is ECSS-M-ST-10C Rev. 1 of 6 March 2009,
the standard on project planning and implementation
[ECSS 2009a][ecss_m_st_10c_rev1].
The ECSS list of active standards carried this issue,
and every other ECSS issue cited here,
when the author read it in November 2026
[ECSS Active Standards][ecss_active_standards].
The standard divides a project into seven phases and names thirteen reviews.

| Phase | Name | Reviews |
|---|---|---|
| 0 | Mission analysis and needs identification | Mission definition review, at the end |
| A | Feasibility | Preliminary requirements review, at the end |
| B | Preliminary definition | System requirements review, during the phase. Preliminary design review, at the end |
| C | Detailed definition | Critical design review, at the end |
| D | Qualification and production | Qualification review, during the phase. Acceptance review and operational readiness review, at the end |
| E | Operations and utilisation | Flight readiness review, before launch. Launch readiness review, immediately before launch. Commissioning result review, after on-orbit commissioning. End-of-life review, at the completion of the mission |
| F | Disposal | Mission close-out review, at the end |

The standard is plain about who decides.
"The customer shall take the decision to move from one phase to the next on the basis of the outcome of the associated "end of phase" review."
The objectives of each review stand in the fourth clause of the standard,
which bears the title Principles and is descriptive.
The requirements stand in the fifth.
A European project therefore owes the phases,
the reviews
and the customer's decision as requirements.
It reads the objectives of each review as a description
that the review's own procedure must make exact.
That reading is the author's.

A reader who moves between the regimes should distrust abbreviations.
MCR is the Mission Concept Review at NASA,
the first review of a project,
and the mission close-out review in the European standard,
the last.
PRR is NASA's Production Readiness Review and the European preliminary requirements review.
Both regimes hold a mission definition review.
The European standard places it at the end of phase 0,
and NASA places it after the System Requirements Review.
The European standards also disagree among themselves.
The standard on ground systems and operations uses CRR for a customer requirements review,
where the project planning standard uses it for the commissioning result review
[ECSS 2008a][ecss_e_st_70c].
The operations standard calls the review after commissioning a flight qualification review.
It divides phase E into sub-phases E1 and E2
"in accordance with ECSS-M-ST-10"
although the saved text of that standard holds no such division.
This article writes the names of reviews in full for that reason.

### How a European Review Runs

A companion standard,
ECSS-M-ST-10-01C of 15 November 2008,
fixes the conduct of a review
[ECSS 2008b][ecss_m_st_10_01c].
Three bodies take part.
"The participants in a review shall include the review authority at the level of the consumer, the project teams at the level of the customer and supplier, and the review team."
The review authority is a
"body appointed by the consumer organization, having the mandate to issue recommendations to the customer and issue decisions relating to the review process"
and a note gives review board as its other name.
Its chair comes from outside the project.
"The review authority shall be chaired by an independent representative of the consumer organization and may be co-chaired by a representative of the customer organization."
A table of typical actors makes the roles concrete.
At mission level the consumer is the agency,
the customer is the directorate
and the supplier is the project.

Each review has a written procedure,
and the standard fixes what the procedure must settle.
"The review procedure shall define the: 1. Prerequisites for the go-ahead of the review as planned 2. Review objectives 3. Success criteria."
A European review therefore takes its success criteria from its own procedure
and not from a table in the standard.
The review examines a data package that must comply with the list of documents specified for the review
and must suffice to demonstrate that the project has achieved the review's objectives.
The standard names six meetings,
namely the prerequisite key point,
the kick-off meeting,
the coordination meeting,
the collocation meeting,
the close-out meeting of the review team
and the meeting of the review authority.

The unit of finding is the review item discrepancy,
RID,
an
"issue, identified by a reviewer, that is not compliant with a requirement, a review objective or a design goal"
in the words of the standard.
A discrepancy is major
"if the issue impacts an objective of the review"
and minor
"if considered part of normal work"
and the standard has no other grade.
The record of a discrepancy must hold at least nine things.

1. The issue raised,
   and the reference of the applicable document that the issue violates.
2. The originator's recommendation for resolving the issue.
3. The classification as major or minor.
4. The endorsement of the discrepancy by the review team.
5. The response from the supplier.
6. The concurrence of the review team with that response,
   or its absence.
7. The action items.
8. Confirmation of the status,
   or a reference to the close-out.
9. Any attached document that supports the issue.

Closure needs agreement.
"A RID shall be considered as closed when the disposition and any associated actions have been agreed by all parties."
What the parties cannot close goes upward.
"Open RIDs shall be submitted to the review authority for final disposition."

Two reports end the review.
The report of the review team gives its scope,
its activities
and its meetings,
an assessment of whether the documentation submitted was adequate,
statistics of the discrepancies,
and an assessment of the review.
That assessment covers the status of actions from earlier reviews,
the major findings and recommendations,
the issues brought to the review authority
and the achievement of the review's objectives.
The report closes with conclusions,
with any lessons learned
and with the list of discrepancies and their status.
The report of the review authority gives the major findings,
the recommendations and decisions,
an assessment of the achievement of the review's objectives
and conclusions.

The standard states the outcome in two sentences.
"The review authority shall decide whether the review objectives have been met"
and
"The review authority shall make recommendations to the customer."
It defines no graded outcome such as a pass,
a conditional pass
or a failure.
The author infers that the two standards together split the decision.
The review authority decides whether the review met its objectives,
and the customer decides whether the project enters the next phase.

## The Concept of Operations

The concept of operations is the first account of how anyone will use the system.
NASA defines it and offers an outline for it.
The European standards carry the same content in two documents under other names.

### Two NASA Documents

The systems engineering directive defines two documents whose names differ by word order.
The first comes early.
"Concept of Operations (ConOps): Developed early in Pre-Phase A, describes the overall high-level concept of how the system will be used to meet stakeholder expectations, usually in a time sequenced manner."
The second comes later and goes deeper.
"Operations Concept (OpsCon): Developed later in the life cycle and baselined at PDR, a more detailed description of how the flight system and the ground system are used together to ensure that the concept of operation is reasonable."
ConOps and OpsCon are the directive's abbreviations for the two names,
and PDR stands for Preliminary Design Review.
The directive says what the second should cover.
"The OpsCon should describe how the flight system and ground system work together across mission phases for planning, training, launch, cruise, critical activities, science observations, and end of mission to achieve the mission."
It allows a project to merge the two.
"They may exist as a single product or separate products."

The agency's Systems Engineering Handbook adds who writes each
[NASA 2016][agency_nasa_se_handbook_2016].
The handbook is guidance,
and its preface says that
"it is not intended in any way to be a directive."
It assigns the concept of operations to the technical team,
and says of the operations concept that
"It is typically developed by the operational team."
It also sets the reach of the first document.
"The ConOps should include scenarios for all significant operational situations, including known off-nominal situations."
The concept of operations is not a record for the shelf.
In the handbook's words,
"It serves as the basis for subsequent definition documents such as the operations plan, launch and early orbit plan, and operations handbook,"
and the directive gives it a second duty,
since validation of a product means
"showing proof that the product accomplishes the intended purpose based on stakeholder expectations and the Concept of Operations."

### The Annotated Outline

Appendix S of the handbook holds an annotated outline,
which the handbook presents modestly.
"Appendix S contains one possible outline for developing a ConOps."
The outline opens with a cover page and a table of contents and then runs through eight sections and two appendices.

| Section | Subsections | What the annotations ask for |
|---|---|---|
| 1.0 Introduction | Project Description, with Background and with Assumptions and Constraints. Overview of the Envisioned System, with Overview and System Scope | The conditions that created the need, the high-level goals, the rationale, the basic assumptions and constraints, and what lies inside and outside the project |
| 2.0 Documents | Applicable Documents. Reference Documents | The material that forms part of the requirements, and supplemental material |
| 3.0 Description of Envisioned System | Needs, Goals and Objectives. Overview of System and Key Elements. Interfaces. Modes of Operations. Proposed Capabilities | Expectations for capabilities, behaviour and operations. The elements at a functional level, free of implementation. External interfaces. The modes needed through the life cycle, including testing and training |
| 4.0 Physical Environment | None | The environment through the life cycle, including integration, tests and transportation, with expected and off-nominal conditions |
| 5.0 Support Environment | None | How operators will plan, command, maintain, repair and upgrade the system once it is fielded |
| 6.0 Operational Scenarios, Use Cases and/or Design Reference Missions | Nominal Conditions. Off-Nominal Conditions | What the system provides along a single-thread timeline, under normal conditions and under failures, low performance, unexpected environments or operator errors |
| 7.0 Impact Considerations | Environmental Impacts. Organizational Impacts. Scientific/Technical Impacts | Effects on the environment through the life cycle, on organisations, and on science or technology |
| 8.0 Risks and Potential Issues | None | Risks of development, operations and disposal, and concerns about schedule, staffing or approach |
| Appendices | Acronyms. Glossary of Terms | Every acronym spelled out, and the terms a reader needs |

Three annotations deserve their own words.
The section on assumptions begins
"State the basic assumptions and constraints in the development of the concept."
The section on the physical environment asks for more than a list of conditions.
"A description of whether the system needs to operate, tolerate with degraded performance, or just survive in these conditions should be noted."
The section on scenarios ties the document to the requirements that will follow it.
"A good practice is to label each of these scenarios to facilitate requirements traceability"
and the handbook's example labels take the form DRM-0100 and DRM-0200,
where DRM stands for design reference mission.
The off-nominal scenarios have a stated purpose.
"These scenarios should reveal any additional capabilities or safeguards that are needed in the system."

### The European Equivalents

A common belief holds that the European system engineering standard defines a concept of operations in one of its annexes.
It does not.
ECSS-E-ST-10C Rev.1 of 15 February 2017 defines a mission description document in its Annex B
[ECSS 2017][ecss_e_st_10c_rev1].
The saved text of the standard holds no occurrence of the phrases concept of operations or operations concept.
The content lies in two places.

The first is the mission description document.
The standard requires that in phase 0 the system engineering function
"shall perform an analysis of the Mission Statement document, produce Mission Description document(s) in conformance with Annex B, and maintain this latter document for the final selected concept."
The top-level customer,
typically an agency,
produces one such document for each candidate concept in phases 0 and A.
The document is a deliverable at the mission definition review and at the preliminary requirements review.
Annex B fixes seven sections.

1. Introduction.
2. Applicable and reference documents.
3. Preliminary technical requirements specification summary.
4. Concept description.
5. Assessment of the performance.
6. Identification of risk areas.
7. Conclusion.

The fourth section does the work of a concept of operations.
It must give an overview of the concept,
the mission analysis,
a description of the system element by element,
and a description of how the system works in each mission phase,
with the performance drivers,
the constraints,
the main events
and the operations scenarios.
A note gives example phases for a spacecraft,
namely launch preparation,
the launch and early orbit phase,
in-orbit commissioning,
nominal operations
and disposal.
The fifth section assesses the concept against the preliminary requirements and identifies each non-compliance.
The sixth has a floor.
"The MDD shall provide the list of identified risk related to the concept, including as a minimum technology, contingencies handling, and programmatic aspects."
MDD stands for mission description document in this standard.
The standard on requirements expands the same abbreviation as mission definition document.

The second place is the mission operations concept document,
which Annex C of ECSS-E-ST-70C of 31 July 2008 defines.
"The objective of the mission operations concept document (MOCD) is to define the operations concepts for the various phases of the mission, covering both the space segment and the ground segment."
After an introduction and a list of documents,
its sections are as follows.

- **Mission operations requirements and constraints.**
  The mission description,
  the end-users,
  the programmatic and operational constraints,
  the relationships with other missions
  and the external dependencies.
- **Space segment characteristics.**
- **Mission operations concepts.**
  One concept for each distinct mission phase,
  under five kinds of process,
  namely planning,
  operations execution,
  evaluation,
  mission exploitation
  and support.

The evaluation process is where the plan meets the report.
The document must describe
"the concept for evaluating the success of executed operations and for monitoring the performance of the space segment"
and the section on exploitation gives,
as an example of feedback to planning,
a report of achieved against planned data acquisition.

The author's reading is that the two European documents divide the ground as the two NASA documents do.
The mission description document is early,
belongs to the customer
and describes the mission phase by phase,
as the concept of operations does.
The mission operations concept document is later,
covers the space and ground segments together
and belongs to operations,
as the operations concept does.
Neither regime states that correspondence.

### Outlines Outside the Agencies

Two outlines for a concept of operations circulate outside the agencies,
and the author read neither standard,
since their publishers sell them.
A handbook of the United States Federal Highway Administration prints both outlines side by side in a figure
[FHWA Systems Engineering for ITS][ref_fhwa_conops_template].
The figure is an image,
and the lists below are a transcription of it by hand.
The first outline is that of a guide of the American Institute of Aeronautics and Astronautics,
which the handbook cites in its 1992 edition.

1. Scope.
2. Referenced Documents.
3. User-Oriented Operational Description.
4. Operational Needs.
5. System Overview.
6. Operational Environment.
7. Support Environment.
8. Operational Scenarios.

The second outline is the one that the handbook attributes to the joint standard on requirements engineering,
ISO/IEC/IEEE 29148,
of the International Organization for Standardization,
the International Electrotechnical Commission
and the Institute of Electrical and Electronics Engineers.

1. Scope.
2. Referenced Documents.
3. The Current System or Situation.
4. Justification for and Nature of Changes.
5. Concepts for the Proposed System.
6. Operational Scenarios.
7. Summary of Impacts.
8. Analysis of the Proposed System.

The handbook compares the two.
"As shown, the ANSI outline lends itself to new systems while the IEEE standard is well suited to system upgrades with its initial focus on the current system."
ANSI stands for the American National Standards Institute,
under whose designation the first guide appears,
and IEEE for the third of the bodies named above.
The first outline is the nearer of the two to NASA's Appendix S,
which likewise has sections on the environment,
on the support environment
and on operational scenarios.
That comparison is the author's.
The author also infers that the second outline is that of an older guide of the third body,
IEEE 1362,
carried into the joint standard,
and did not check that lineage against either text.

The status of the three standards is as follows.
The publisher's catalogue shows ISO/IEC/IEEE 29148 at its second edition,
published in November 2018,
with the note
"This publication was last reviewed and confirmed in 2024"
and with a draft revision under development
[ISO 2018][ref_iso_29148_2018].
The publisher of the older guide on concept of operations documents,
IEEE 1362-1998,
lists it as a superseded standard and not as a withdrawn one,
with the line
"Replaced by ISO/IEC/IEEE 29148:2011"
[IEEE 1998][ref_ieee_1362_1998].
The aeronautics institute's guide now bears the designation ANSI/AIAA G-043B-2018
and the title Guide to the Preparation of Operational Concept Documents
[AIAA 2018][ref_aiaa_g_043b_2018].
The author confirmed that designation from a registry record only,
because the publisher's page refused access.

## Objectives, Requirements and Success Criteria

A plan must say what the mission is for and what would count as having done it.
NASA writes the second as criteria tied to a floor.
The European standards write requirements and leave success to follow from them.

### NASA Requirements and the Floor Beneath Them

The project management directive sorts requirements into five levels in its Table 1-1.
They are the agency's strategic goals,
the requirements of the Mission Directorate,
the requirements of the programme,
the requirements of the project
and the requirements of the system.
Each level has a governing document and an approver.
The Program Plan governs the programme's requirements,
and the Mission Directorate Associate Administrator approves them.
The Project Plan governs the project's requirements,
and the programme manager approves them.

The directive defines success as a subset of those requirements.
"Success Criteria. That portion of the top-level requirements that defines what is to be achieved to successfully satisfy NASA Strategic Plan objectives addressed by the program or project."
For a science mission it defines two grades of requirement.
"Baseline Science Requirements. The mission performance requirements necessary to achieve the full science objectives of the mission."
"Threshold Science Requirements. The mission performance requirements necessary to achieve the minimum science acceptable for the investment."
The template of the Program Plan ties the criteria to the lower grade.
"Identify the mission success criteria for each project based on the threshold science requirements. State each requirement in objective, quantifiable, and verifiable terms."
The template of the Project Plan then asks the project to
"document the minimum mission success criteria associated with the program requirements on the project that, if not met, trigger consideration of a Termination Review."
The floor therefore has a consequence.
A project that does not meet it faces consideration of a Termination Review.
The same template asks for the path down from the full mission to the floor.
"Describe the project's descope plans, including key decision dates and savings in cost and schedule, and show how the descopes are related to the project's threshold performance requirements."
The Systems Engineering Handbook adds that success has a degree as well as a list.
"The success criteria also define how well the concept measurements or exploration activities should be accomplished."

Two terms in common use are not terms of the directive.
The string Level 1 does not occur in its saved text.
The management handbook uses Level 1 requirements in two places,
which the author reads as working vocabulary for the programme's requirements on a project.
The phrase full mission success occurs in none of the NASA texts read for this article.
The directive's own vocabulary is baseline and threshold science requirements,
mission success criteria
and minimum mission success criteria.
The author did not obtain a public example of a programme's requirements on a project,
so this article shows no worked set of minimum success criteria.

### Risk Classes

NASA also grades a mission by how much risk the agency will accept in it.
The governing directive is NASA Procedural Requirements 8705.4B,
which took effect on 1 November 2024 and cancelled revision A
[NASA 2024d][agency_nasa_npr_8705_4b].
It defines four classes of risk tolerance for a mission or an instrument.

| Class | Risk tolerance and priority | Lifetime, complexity and cost |
|---|---|---|
| A | Lowest tolerance. Very high priority | Primary mission longer than 5 years. Very high complexity. High life-cycle cost |
| B | Low tolerance. High priority | 3 to 5 years. High complexity. Medium to high cost |
| C | Moderate tolerance. Medium priority | 1 to 3 years. Medium complexity. Medium cost |
| D | High tolerance. Low priority | Less than 1 year. Medium to low complexity. Medium to low cost |

The directive words the classes by what drives them.
"Class A: The lowest risk tolerance that is driven by technical objectives."
"Class D: High risk tolerance that is driven more by programmatic constraints than technical objectives."
The Mission Directorate designates the class,
and it does so early.
"The Mission Directorate designates the mission or instrument risk tolerance class as early in the formulation process as possible but no later than the KDP B Decision Memo."
The table of considerations is an aid and not a formula.
"The considerations provided in the table below are not definitive, nor is any specific mission criterion alone intended to be the ultimate driver to designating a mission or instrument risk tolerance class."

### The European Chain

The European system engineering standard does not use the terms mission objectives or mission requirements at all.
Its chain begins with a mission statement,
which the ECSS glossary defines as a
"document expressing the set of collected needs"
[ECSS 2023][ecss_s_st_00_01c_rev1].
The chain continues through the mission description document to a technical requirements specification,
which ECSS-E-ST-10-06C of 6 March 2009 defines
[ECSS 2009b][ecss_e_st_10_06c].
The specification has seven sections,
namely an introduction,
the applicable and reference documents,
the user's need,
the selected concept,
the life profile,
the environment and constraints,
and the requirements.
The standard lists twelve types of requirement,
one of which is the mission requirement.
"Requirements related to a task, a function, a constraint, or an action induced by the mission scenario."
Three of its rules for writing a requirement match NASA's demand for objective,
quantifiable
and verifiable terms.
"Each technical requirement shall be described in quantifiable terms."
"A technical requirement shall be verifiable using one or more approved verification methods."
"The tolerance shall be specified for each parameter/variable."

Two things that a reader might expect are absent.
None of the ECSS standards read here defines a mission requirements document or a science requirements document.
The review standard lists the abbreviation for the first,
and no standard prescribes its contents.
None of them uses the term success criteria for a mission.
The nearest statement sits in the introduction to the operations standard.
"Mission success is defined here as the achievement of the target mission objectives as expressed in terms of the quantity, quality and availability of delivered mission products and services within a given cost envelope."

### A European Example

ESA nevertheless writes mission requirements documents,
and one is public.
The Mission Requirements Document of the Copernicus CO2 Monitoring mission,
at issue 3.0 of 1 October 2020,
has eight chapters
[ESA 2020][esa_co2m_mrd_2020].

1. Introduction.
2. Background and Justification.
3. Mission Objectives.
4. Mission Requirements.
5. Preliminary System Concepts.
6. Data Products and Usage.
7. Synergies and International Context.
8. References.

Appendices give the terms and conventions of the requirements,
a set of reference scenarios
and a table that traces each mission requirement to a user requirement.
The document states its objectives in prose.
"The primary objective of the CO2 Monitoring mission is to measure images of total column CO2 with the resolution, accuracy, time sampling and spatial coverage required to provide the key space component input of the Operational Anthropogenic CO2 Emissions Monitoring & Verification Support (MVS) Capacity."
It states its requirements as numbered rows,
each with an identifier of the form S7MR-DAT-010 and one sentence.
A firm requirement says shall,
and a softer one says shall target.
The link between the two chapters is itself a requirement.
"The mission requirements shall enable the CO2M mission to fulfil its objectives, as outlined in the previous section."
CO2M is the document's short name for the mission.
The document does not treat its text as final.
"It shall be noted that the document is considered a living document, which will be updated after consultancy with experts and according to new requirement insights."

The saved text of the document holds no occurrence of the term success criteria.
The author infers that in this European example success means compliance with the numbered requirements.
The document does not say so.

## Design Reference Missions

A design reference mission is a scenario that a design must be able to fly.
NASA uses the term in its directives and handbooks and,
so far as the author could find,
defines it in none of them.
The project management directive,
the systems engineering directive,
the directive on human rating
and the glossary of the Systems Engineering Handbook contain no definition.
The documents show the meaning by use.

The handbook treats the reference mission as a kind of scenario.
It speaks of
"use-case scenarios (sometimes referred to as Design Reference Missions (DRMs)) and the ConOps."
It also says how the two relate.
"For exploration missions, multiple DRMs make up a ConOps. The design and performance analysis leading to the requirements should satisfy all of them."
The directive on human rating gives the reference mission a formal weight,
since
"Human-Rating Certifications, per this NPR, are based on reference missions"
[NASA 2017][agency_nasa_npr_8705_2c].
Its rationale explains why a programme writes them down early.
"Defining reference missions establishes the scope of the program to be human-rated and also provides a framework that supports, among other things, identification of crew survival strategies and establishment of scenarios to be used for hazard analysis and risk assessments."

A reference mission is not a requirement.
The reference missions of the Commercial Crew Program say so of themselves.
"This document describes concept DRMs and is not a requirements document"
[NASA 2015][agency_nasa_cct_drm_1110].
They add that
"specific requirements derived from each DRM are provided in separate documents"
which fixes the order of the two.
The scenario comes first and the requirements follow from it.
The same document shows the form of one reference mission.
On the author's reading of its section on a flight to the International Space Station,
the mission states objectives in two ranks,
narrates the nominal flight in order of time from before launch to landing,
and then gives the off-nominal branches.
One branch ends the flight.
"If this final docking attempt is unsuccessful, the mission will be terminated, and the crew will return to Earth."

### A Worked Example

The largest public example is the Human Exploration of Mars Design Reference Architecture 5.0 of July 2009,
with its Addendum of the same date
[Drake 2009a][agency_nasa_dra5_2009]
[Drake 2009b][agency_nasa_dra5_addendum_2009].
The report opens by limiting its own status.
"The strategy and implementation concepts that are described in this report should not be viewed as constituting a formal plan for the human exploration of Mars."
It offers instead
"a common framework for future planning of systems concepts, technology development, and operational testing."

The report has eight chapters.

1. Introduction.
2. Design Reference Architecture 5.0 Summary.
3. Goals and Objectives.
4. Transportation Systems.
5. Surface Systems.
6. Architectural Assessments.
7. Key Challenges.
8. Public Participation.

The order is itself a template.
A summary of the mission comes first,
then the objectives,
then the systems by segment of the mission,
then the trades with their figures of merit,
then what remains unsolved.

The report tells the mission sequence twice.
The second chapter narrates it in prose in the conditional mood,
and one figure draws it as fourteen numbered steps on a single chart.
The narrative ties later steps to the success of earlier ones.
Of the surface infrastructure that the architecture deploys before the crew arrives it says
"the successful completion of these various activities would be part of the decision criteria for launch of the first crew from Earth."
It places a second gate at Mars.
"Before committing the crew to Mars ascent and return to Earth, full systems checkout of the ascent vehicle and the MTV would be required."
MTV stands for Mars transfer vehicle.
A reference mission of this kind therefore carries its own go or no-go points,
long before anyone writes a flight rule.

The numbers sit in tables with their conventions stated.
In the main report the velocity changes appear as a chart.
The Addendum tabulates them,
with one row for each departure opportunity of the crewed missions from 2031 to 2046
and a column of delta-v for each of the three main manoeuvres.
A footnote says what the figures include.
"All delta-Vs include gravity losses but no plane changes."
The text beside the table gives the starting conditions.
"In this analysis, all vehicles depart from a 407-km circular orbit, and a two-burn Earth escape is performed to reduce the gravity-loss penalties."
The report tabulates mass by vehicle element and by launch,
and it shows margin as a row of its own.
The mass table of the transit habitat has a row labelled Margin at 30 percent,
and the text notes that the study doubled the dry weight margin to reach that figure.
For the terminal descent of the lander the Addendum studied margins on the nominal delta-v and states its choice.
"A 30% delta-V margin was selected as the reference baseline."

### Ground Rules and Assumptions

The Addendum separates what the study held fixed from what it was free to vary.
"Items that are Ground Rules are denoted with "GR" and were considered to be held constant for this study. Assumptions, which are denoted with "A," were assumed parameters for initializing the study and may be traded if sufficient time and resources are available during the study."
It says where they came from.
"These were derived based on management guidance, internal and external constraints, design practices, and existing requirements."
Five tables hold them by subject,
namely safety and mission assurance,
operations and general matters,
technical matters,
cost and schedule,
and testing and verification.
Each table has four columns,
which are a number,
the type,
a description
and a rationale.
Item 002,
for example,
is a ground rule that the architecture will provide abort opportunities throughout all mission phases to the maximum extent possible.
Its rationale says that the study will examine the feasibility of aborts as time allows.

The form has three properties worth copying.
Every assumption has a number,
so that a later document can cite it.
Every assumption has a type,
so that a reader knows whether a trade study may move it.
And every assumption has a rationale,
so that a reader can tell when it has stopped being true.
That assessment is the author's.

## Mission Analysis and the Delta-V Budget

Mission analysis turns the scenario into a trajectory and the trajectory into a budget of velocity change,
or delta-v.
The documents differ most in where they put the margin.

### The Mission Analysis Report

The European operations standard requires a mission analysis and lists thirteen things that it must supply.
They are a prediction of the launch window,
the separation sequence of the spacecraft and the launch vehicle,
the launch target orbit,
the positioning or manoeuvring strategy,
the orbit determination concept and navigation analysis,
a schedule of operational events that covers nominal scenarios and planned contingencies,
the ground station coverage,
a detailed analysis of high risk sequences,
the risk of interference with spacecraft already in operation,
the delta-v budget,
the impact of the space environment on operational sequences,
the payload operations strategy
and the data circulation scheme.
The output is a mission analysis report,
whose contents Annex B of the standard fixes.
It is this standard,
and not the system engineering standard,
that defines the report.

1. Introduction.
2. Applicable and reference documents.
3. Mission requirements and constraints.
4. Mission overview.
5. Launch and early orbit phase.
6. Transfer phase,
   for interplanetary missions.
7. Injection into planetary orbit,
   for interplanetary missions.
8. Routine phase,
   meaning operation in the final orbit.
9. Propellant budgets.

The standard gives the report a double purpose.
It serves
"the planning and execution of mission operations"
and it
"also provides input to the spacecraft and mission design."

### A European Example

ESA publishes the mission analysis of its Jupiter mission,
the Jupiter Icy Moons Explorer or JUICE,
as a Consolidated Report on Mission Analysis.
The author read issue 3,
revision 2,
of 25 April 2017
[ESA 2017][esa_juice_crema_2017].
The server that holds it lists later sets of trajectory data and no later report,
so this is the latest report text that the author found and not the latest analysis.
The file carries the marking For Official Use although the agency serves it publicly,
and this article describes its structure and quotes it only briefly.

The report has sixteen chapters.
An introduction and a list of documents come first.
The third chapter gives the requirements,
the definitions
and the assumptions,
and ends with a section on models and assumptions.
Chapters then follow for the phases of the trajectory,
from the interplanetary transfer through the tour of Jupiter's moons to the science phase around Ganymede,
with an overview of the tour.
Chapters on navigation,
planetary protection,
the delta-v budget,
eclipses and occultations,
and communications close the report.

The budget is two tables,
and each has one column for each launch option.
The first table is deterministic.
Its rows follow the trajectory in order of flight.

- Launch window.
- Interplanetary flight.
- Insertion into orbit around Jupiter.
- From that insertion to the end of the Europa phase.
- Jupiter high latitudes.
- Transfer to Ganymede.
- Insertion into orbit around Ganymede.
- Transfer from the elliptic orbit around Ganymede to the circular one.
- Total.

The second table is stochastic.
Its rows are the costs of navigation.

- Launcher dispersions.
- Gravity assists of the interplanetary flight.
- Clean-up after the insertion at Jupiter.
- Gravity assists of the Jupiter tour.
- Approach to the insertion at Ganymede.
- Station keeping.
- Total.

For the baseline launch option the deterministic total is 1,802 metres per second
and the stochastic total is 427 metres per second.
The report's own summary rounds them.
"To summarize the deterministic DeltaV cost is around 1.8 km/s while the stochastic DeltaV cost is around 430 m/s."
The report keeps the two totals apart and adds no percentage of margin to either table.
Where a row holds an allowance,
the text beneath the table says so.
One row includes 5 metres per second for planetary protection,
and another a margin of 20 metres per second for the robustness of the solution.
The report also states what the stochastic table leaves out,
since
"No provision is made for contingencies"
such as a missed fly-by.

The stochastic figures have a stated statistical meaning.
The navigation chapter estimates the cost of each gravity assist at the 99 percent level
and aggregates the individual costs by a linear sum.
The report names the alternative.
A linear sum is pessimistic and assumes that the manoeuvres depend fully on one another.
A root sum square is optimistic and assumes that they are independent.
The author's reading is that this report treats the margin as a property of navigation,
computed and tabulated,
where other documents add it as a percentage.

### A NASA Example

The mission design paper for NASA's Lunar Reconnaissance Orbiter tabulates its budget in one table
[Beckman 2007][agency_nasa_lro_mission_design].
The table has four columns,
which are the manoeuvre or phase,
the delta-v in metres per second,
the fuel in kilograms
and notes.
The table below folds the two numeric columns into one.

| Manoeuvre or phase | Delta-v and fuel | Basis, from the notes column |
|---|---|---|
| Mid-Course Correction | 28 m/s, 26.4 kg | Three sigma launch vehicle errors |
| Lunar capture, the first insertion burn | 567 m/s, 444.9 kg | Deterministic |
| Second insertion burn | 185 m/s, 121.8 kg | Deterministic |
| Third insertion burn | 133 m/s, 81.3 kg | Deterministic |
| Fourth insertion burn | 41 m/s, 24.1 kg | Deterministic |
| Mission Orbit Insertion | 50 m/s, 28.8 kg | Deterministic |
| Mission orbit stationkeeping | 150 m/s, 84.1 kg | Deterministic |
| Extended Mission | 65 m/s, 33.5 kg | Three years, frozen |
| Momentum Unloading | No delta-v, 17.0 kg | Worst case |
| Other, residuals | No delta-v, 15.4 kg | Conservative |
| Unallocated Margin | 39 m/s, 20.9 kg | Conservative |
| Total | 1,258 m/s, 898 kg | None |

The delta-v rows sum to the printed total of 1,258 metres per second,
and the fuel rows sum to 898.2 kilograms against a printed 898.
The unallocated margin is about 3 percent of the total delta-v.
The paper gives the scale of the budget in a sentence.
"LRO launch mass is required to be less than 2000 kg, of which about 900 kg is fuel mass."
LRO stands for Lunar Reconnaissance Orbiter.

The author draws four features of form from this table.
Each row is a manoeuvre or a phase in the order of flight.
Each row carries both the velocity change and the propellant that pays for it.
Most rows state the basis of their number,
whether deterministic,
statistical,
worst case
or conservative.
And the margin is a row of its own,
labelled as unallocated,
so that no other row hides it.
Two uses of propellant that change no velocity,
momentum unloading and residuals,
still appear,
with mass and without delta-v.

### How Margin Is Defined

The most explicit definition of margin in the documents read is a rule of NASA's Goddard Space Flight Center.
Its standard of design rules,
GSFC-STD-1000I of 19 August 2025,
is a standard of that Center and not a mandatory standard of the agency
[NASA 2025b][agency_nasa_gsfc_std_1000i].
Rule 1.06 requires that
"Mission-level resource margins shall be met in accordance with Table 1.06-1."
The notes to that table define the terms.
Let $M\_{\mathrm{B}}$ be the basic mass,
$M\_{\mathrm{G}}$ the mass growth allowance,
$M\_{\mathrm{P}}$ the predicted mass
and $M\_{\mathrm{A}}$ the allowable mass.
The predicted mass is the basic mass with its growth allowance.

$$
M_{\mathrm{P}} = M_{\mathrm{B}} + M_{\mathrm{G}}
\tag{1}
$$

The margin is what remains between the predicted mass and the allowable mass,
and the rule states it as a percentage $m$ of the basic mass.

$$
m = \frac{M_{\mathrm{A}} - M_{\mathrm{P}}}{M_{\mathrm{B}}} \times 100
\tag{2}
$$

In the standard's own notation the second relation reads
"Mass margin (%) = (Allowable-Predicted)/Basic X 100."
As an illustration by the author,
a spacecraft with a basic dry mass of 400 kilograms,
a growth allowance of 60 kilograms
and an allowable mass of 520 kilograms
has a predicted mass of 460 kilograms and a mass margin of 15 percent.
The table sets the margin that a project must hold at each review.
For mass it is more than 15 percent at the System Requirements Review,
more than 10 percent at the Preliminary Design Review,
more than 5 percent at the Critical Design Review,
more than 2 percent at the System Integration Review
and zero in Phase D.

Two notes to the table matter to anyone who writes a budget.
The first fixes the vocabulary.
"The terms "reserve" and "contingency" are not to be used in relation to mass margins."
The second separates dry mass from propellant.
"Margin and MGA apply to dry mass only. Fuel margins are handled through Delta-V margins applied against the predicted mass."
MGA stands for mass growth allowance.
The propellant row of the table accordingly holds no percentage.
It holds a statistical requirement of three standard deviations.
A footnote builds it from worst-case mass properties of the spacecraft,
from three sigma low performance of the launch vehicle and of the propulsion subsystem,
from three sigma errors of flight dynamics,
and from a thruster failure where the system tolerates a single fault.

### Margin as a Percentage

An ESA document for science missions states its margins as percentages by kind of manoeuvre.
This margin philosophy for assessment studies,
at issue 1,
revision 3,
of 15 June 2012,
carries the marking For Official Use
[ESA 2012][esa_margin_philosophy_2012].
It requires a margin of
"5 % for accurately calculated manoeuvres"
and a margin of 100 percent for orbit maintenance manoeuvres that nobody has derived analytically,
and for manoeuvres of attitude control and angular momentum management.
It adds a fixed allocation of 15 metres per second for each planetary gravity assist
and 10 metres per second for each gravity assist at a moon,
for chemical propulsion.
It requires that a budget of impulsive manoeuvres add the gravity losses that the theoretical values omit.
On mass it requires a system margin of 20 percent of the nominal dry mass at launch
and 2 percent of propellant residuals.
The document does not use the words deterministic or stochastic.
That division comes from the mission analysis report above.

A second ESA guideline,
for satellites in low Earth orbit,
takes the opposite line
[ESA 2019][esa_delta_v_guidelines_2019].
It too carries the marking For Official Use.
"No margins shall be applied to the computation of the ΔV, except for the final burn in case of a controlled re-entry, where a margin of 15% shall be applied."
The guideline places its conservatism elsewhere.
It doubles the number of collision avoidance manoeuvres,
and it applies a margin of 100 percent to the propellant for attitude control by thrusters.
It then computes propellant backwards.
"The propellant computation procedure starts with the computation of the propellant required to perform the de-orbiting manoeuvre and then proceeds backward in the mission timeline ending with the propellant needed for the correction of launcher injection errors."
The reason lies in its formula.
Let $P\_{\mathrm{EOL}}$ be the propellant for the manoeuvres at the end of life,
$m\_{\mathrm{dry}}$ the dry mass of the satellite,
$P\_{\mathrm{RES}}$ the propellant residuals,
$P\_{\mathrm{UNC}}$ the allowance for gauging uncertainty,
$\Delta V\_{\mathrm{EOL}}$ the delta-v of those manoeuvres
and $V\_{\mathrm{e}}$ the exhaust velocity.

$$
P_{\mathrm{EOL}} = \left( m_{\mathrm{dry}} + P_{\mathrm{RES}} + P_{\mathrm{UNC}} \right) \left( e^{\Delta V_{\mathrm{EOL}} / V_{\mathrm{e}}} - 1 \right)
\tag{3}
$$

The exhaust velocity is the product of the average specific impulse $I\_{\mathrm{sp}}$,
the thruster efficiency $\eta$
and the standard gravitational acceleration $g\_{0}$,
which the guideline gives as 9.80665 metres per second squared.

$$
V_{\mathrm{e}} = I_{\mathrm{sp}} \, \eta \, g_{0}
\tag{4}
$$

The propellant of each earlier phase uses the same form,
with the propellant of every later phase added to the mass that the burn must move.
The author notes a consequence.
Nobody can read a budget built this way off a table of delta-v alone,
since each row depends on the rows after it.
The guideline sets the residuals at 1 percent
and the gauging allowance at 2 percent of the maximum propellant load of the selected tank,
and a system margin of 15 percent on dry mass where the satellite's requirements are silent.

The documents read therefore place the margin in five different ways.
The lunar orbiter's budget gives it a row.
The Jupiter report computes it as a statistical cost and tabulates it apart.
The Goddard rule holds it as a statistical requirement on propellant and a percentage on dry mass.
The science margin philosophy adds a percentage to each manoeuvre by kind.
The low Earth orbit guideline adds almost none to delta-v
and puts its allowance in counts of manoeuvres,
in propellant
and in dry mass.
The comparison is the author's.
A reader cannot compare one budget with another unless each says which of these conventions it follows.

## Flight Rules and Launch Commit Criteria

A flight rule is a decision that the operators took before the flight,
written down with its reason.
The public example read for this article is Volume A of the Space Shuttle Operational Flight Rules,
NSTS-12820,
in its edition of June 2002 with a page change notice of November 2002
[NASA 2002][agency_nasa_nsts_12820_vol_a].
The copy is an archive capture of a file that NASA released with the material on the Columbia accident.
It is not the last revision of the rules.

### The Form of a Rule

The first rule of the volume states what a flight rule is,
and it is short enough to give whole.
Its number is A1-1 and its title is FLIGHT RULE PURPOSE.
"THE FLIGHT RULES OUTLINE PREPLANNED DECISIONS DESIGNED TO MINIMIZE THE AMOUNT OF REAL-TIME RATIONALIZATION REQUIRED WHEN NON-NOMINAL SITUATIONS OCCUR FROM THE START OF THE TERMINAL COUNTDOWN THROUGH CREW EGRESS OR GROUND SUPPORT EQUIPMENT (GSE) COOLING ACTIVATION, WHICHEVER OCCURS LATER."
Its rationale follows in ordinary type and is one word,
Self-explanatory.
That is a complete rule.
It has a number,
a title,
the rule in capitals
and the rationale in ordinary type.

A rule with a real rationale shows why the two parts stay together.
Rule A1-56 begins
"WHERE DISCREPANCIES EXIST BETWEEN ONBOARD AND GROUND READOUTS, DEDICATED ONBOARD METERS WILL BE CONSIDERED PRIME OVER GROUND READOUTS."
Its rationale opens
"The purpose of this rule is to minimize the possibility of invoking a flight rule as a result of transducer failures, shifts, or errors introduced in the communications path from the vehicle to the MCC."
MCC stands for Mission Control Center.
The rule tells the controller what to do,
and the rationale tells a later reader when the rule would no longer apply.

The saved text shows the other conventions.

- **Number.**
  The volume letter,
  the section number,
  a hyphen
  and a sequence number,
  as in A2-1.
  The volume holds blocks of numbers in reserve.
- **Title.**
  In capitals on the line of the number.
  A tag in brackets marks a rule tied to the critical items list or to a hazard control.
- **Rule text.**
  In capitals,
  with lettered and numbered paragraphs.
- **Rationale.**
  In ordinary type,
  after the rule or after each lettered paragraph.
- **Cross-references.**
  A rule cites another rule by its number in braces.

### The Structure of the Volume and Its Authority

The volume has eighteen sections.
The first two are general,
namely General, Authority, and Definitions,
and Flight Operations.
The other sixteen take one discipline each,
from ground instrumentation and trajectory through propulsion,
data systems,
communications
and life support to the thermal system.
Four appendices hold the acronyms,
the change control,
the waivers
and a cross-reference to hazard reports and critical items.
The volume is the generic layer of two.
Its preface says that a reader should use it together with an annex,
NSTS-18308,
which holds the rules for each flight.
A Flight Rules Control Board,
chaired by the Director of Mission Operations or a designee,
reviews and approves each change request against the generic rules.

The rules also settle who decides when they run out.
During flight the chair of the Mission Management Team is responsible for policy decisions in near real time,
and the rule calls for consulting the chair as soon as possible
whenever a flight needs operations outside the Shuttle operating base.
The flight director keeps a reserve of authority.
"THE FLIGHT DIRECTOR, AFTER ANALYSIS OF THE FLIGHT CONDITION, MAY CHOOSE TO TAKE ANY NECESSARY REAL-TIME ACTION REQUIRED TO ENSURE THE SAFETY OF THE CREW AND SHUTTLE."
And the commander takes over if the link fails.
A further rule gives the commander responsibility for the conduct of the flight,
within the framework of the flight rules,
when the crew cannot communicate with Mission Control.

The volume grades equipment for the decision to launch.
A mandatory element is one that crew safety requires,
or that the rules for launch go or no-go,
launch abort
or early flight termination need.
A highly desirable element is one that enhances the flight.
The count may hold for its repair if that is convenient,
and the definition adds that the team will in no case scrub the launch for it.

### Launch Commit Criteria

The launch commit criteria are a separate document,
which the acronym list of the volume identifies as NSTS 16007
and which the author did not obtain.
The flight rules point to them.
Rule A2-1 opens
"LAUNCH WILL BE NO-GO IF THE FOLLOWING CONDITIONS ARE NOT SATISFIED"
and its first condition is the minimum capability of the vehicle's subsystems,
with a reference to the criteria.
The rationale of that paragraph is the nearest thing to a definition that the Shuttle documents read here supply.
"Launch commit criteria are designed to ensure those systems that are monitorable operate within acceptable limits during the final hours in the launch countdown."
It also says what a deviation costs.
"Any deviation must be accounted for, either by repair, replacement, or a waiver from the MMT."
MMT stands for Mission Management Team.
The author found no definition of launch commit criteria in a NASA directive.

A current definition comes from the Commercial Crew Program,
whose plan for certifying flight readiness has a glossary
[NASA 2022b][agency_nasa_cct_pln_2100].
It defines flight rules as
"Established redline limits for critical flight parameters. Each has pre-planned troubleshooting procedures with pre-approved decisions for expected troubleshooting results."
The entry for launch commit criteria begins in the same words with one substitution.
"Established redline limits for critical launch parameters."
The plan gives real-time changes to a body of the same name as the Shuttle's.
"The MMT will approve all real-time changes, deviations or waivers to Launch Commit Criteria or Flight Rules."

The European operations standard has no document called flight rules.
The content sits in the mission operations plan under the heading of mission rules,
which a later section describes.
The plan must contain launch hold criteria,
the principles for routine and foreseen contingency operations,
criteria for transferring operations between authorities,
mission termination criteria,
and
"rules and criteria for emergencies and anomalies not covered by existing contingency procedures"
which the standard relates to multiple or unforeseen failures for which no pre-defined recovery exists.
The author's reading is that the launch hold criteria answer to the launch commit criteria
and the remaining mission rules to the flight rules.

## Readiness Reviews and the Decision to Fly

The last reviews before launch ask one question in several forms.
Is everything that the mission needs ready,
and who says so?

### Two NASA Reviews

Appendix G of the systems engineering directive describes the Operational Readiness Review by what it must confirm.
"The ORR ensures that all system and support (flight and ground) hardware, software, personnel, procedures, supporting capabilities, and user documentation accurately reflect the deployed state of the system and are operationally ready."
ORR stands for Operational Readiness Review.
Its table recommends twelve entrance criteria.
Among them,
the project has completed its ground testing,
resolved the anomalies from testing,
written,
verified
and approved its operations documentation,
trained its operators
and completed its contingency planning.
It recommends thirteen success criteria,
of which the first three set the tone.
"The system, including all enabling products, is determined to be ready to be placed in an operational status."
"All applicable lessons learned for organizational improvement and systems operations have been captured."
"All waivers and anomalies have been closed."
Two later criteria tie the review to the plan and to a person.
"Operations plans and schedules are consistent with mission objectives."
"Mission risks have been identified, planned mitigations are adequate, and residual risks are accepted by the program/project manager."

The review that follows is the Mission Readiness Review for a robotic project
and the Flight Readiness Review for a crewed one,
and the appendix treats the two in one table.
The review
"also ensures that all flight and ground hardware, software, personnel, and procedures are operationally ready."
Its ten recommended entrance criteria include a system state that supports a decision to launch against established go or no-go criteria,
and the final certification for flight or use,
which the directive itself requires as a product of the review.
Its thirteen recommended success criteria turn on the acceptance of risk.
"Certification that flight operations can safely proceed with acceptable risk has been achieved."
"Open items and waivers have been examined and residual risk from these is deemed to be acceptable."
As the earlier section explained,
the appendix offers these lists as recommended practice.
It expects a project to tailor them.
The directive requires the technical team to take part in developing the entrance and success criteria of each review,
and its glossary places the success criteria in the review plan.

### Who Signs for a Launch Service

For a mission whose launch service NASA acquires or manages,
a policy directive fixes the sequence and the signatures.
It is NASA Policy Directive 8610.24C,
which the agency revalidated on 2 April 2025 with Change 3
[NASA 2025a][agency_nasa_npd_8610_24c].
The directive describes four steps.

1. The Launch Vehicle Readiness Review,
   30 to 60 days before launch,
   certifies readiness to integrate the spacecraft with the launch vehicle.
2. The Flight Readiness Review,
   at the launch site,
   closes the actions of the earlier reviews
   and certifies readiness to begin final launch preparations.
3. The Launch Readiness Review,
   no later than one day before launch,
   closes the actions of the Flight Readiness Review
   and authorises the countdown.
4. The Final Commit-to-Launch Poll,
   about five minutes before launch,
   confirms NASA's readiness to launch.

The spacecraft project holds its own Mission Readiness Review before the second step.
The sources do not agree on the timing of that step.
The directive says in one clause both that the Flight Readiness Review falls between 3 and 12 days before launch
and that it falls about 3 days before,
and the management handbook says about 5 days.

The certificate comes at the third step.
"The Certificate of Flight Readiness (CoFR) is signed at the conclusion of LRR."
LRR stands for Launch Readiness Review.
The authority to sign descends by delegation.
The Associate Administrator of the Space Operations Mission Directorate is responsible for certifying the readiness of the launch vehicle.
That official delegates the authority to the Director for Launch Services,
who delegates the signing to the manager of the Launch Services Program.
The directive then lists who else signs.
"In addition to the LSP Manager, signatories to the CoFR shall include the NASA Spacecraft Mission Director, the NLM, the launch services contractor representative, the LSP ITAs, and a range official."
LSP stands for Launch Services Program,
NLM for NASA Launch Manager
and ITA for Independent Technical Authority.
The programme keeps the record.
"A record of all LSP prelaunch reviews, action items disposition, and the original CoFR will be maintained by the LSP."

The poll at the fourth step has a rule of its own.
"A "Go" statement is required from all parties polled to enter into the terminal count. Mandatory launch constraints cannot be waived after start of the terminal launch countdown."
The NASA Launch Manager conducts it,
receives a statement of go or ready from the Spacecraft Mission Director,
from the technical authorities
and from the other NASA organisations in the countdown,
and gives the final commitment to the launch director of the contractor.

### Who Signs for a Crewed Flight

For human space flight the management handbook describes a longer chain.
It runs through the Operations Readiness Review,
the preliminary Flight Readiness Reviews that the project,
the programme,
the Mission Directorate
and the Center may hold,
and the Safety and Mission Success Review,
to the Agency Flight Readiness Review.
The Mission Directorate Associate Administrator chairs that last review and the Decision Authority attends it.
The handbook places the decision of Key Decision Point E at its end,
and the signature with it.
"The Certification of Flight Readiness (COFR) is signed at the conclusion of the Agency FRR."
FRR stands for Flight Readiness Review.
The handbook describes the role of the safety review as letting senior safety and engineering management
"either concur or nonconcur in program decisions to proceed with a launch or significant flight activity."

The Commercial Crew Program's plan shows the practice in detail.
It states the purpose of the Agency review as a request for approval
"to proceed to launch countdown and/or Return for a mission that transports NASA Crew and cargo and to document the formal acceptance of risk by NASA and the Commercial Provider."
The Associate Administrator of the Space Operations Mission Directorate chairs the board.
Its members are the managers of the Commercial Crew Program,
of the International Space Station Program
and of the commercial provider,
the NASA Chief Engineer,
the Chief Health and Medical Officer,
the Chief Safety and Mission Assurance Officer,
the Director for Commercial Spaceflight Development
and the Directors of three NASA Centers.
The agenda ends with two items.
"5. Chair shall review any open work and action items. 6. Chair shall conduct a poll requesting concurrence and discussion on any formal dissents."

The plan gives the poll a rule and a limit.
"A readiness poll of all Board members shall be conducted at the conclusion of each CoFR Review specified in this plan."
"The Review Chair shall consider the poll results when formulating the final decision."
The members sign,
and
"The CTS CoFR Certificate is considered endorsed when all signatures have been obtained."
CTS stands for Crew Transportation System.
An appendix gives the words of the chair's own statement.
"I have concluded, with the concurrence of the Flight Readiness Review Board that pending satisfactory completion of standard open work, the CTS is ready to execute the mission, as briefed,"
it begins,
and it ends by authorising NASA crew to fly.
The plan provides for an endorsement that an organisation cannot give in full.
"When any of the criteria for a CoFR Endorsement Statement cannot be met due to non-standard open work a CoFR Exception is required, if so determined by the endorsing organization."
The records of the review include the signed statements of readiness of each organisation
and the signed checklist of the poll.

The two polls differ in kind,
and the difference is the author's inference from the two texts.
The launch poll requires a statement of go from every party polled.
The board's poll advises a chair,
who considers its results and decides.

### The European Readiness Reviews

The European project planning standard places three reviews around the launch.
The operational readiness review ends phase D and has three objectives.

- "To verify readiness of the operational procedures and their compatibility with the flight system."
- "To verify readiness of the operations teams."
- "To accept and release the ground segment for operations."

The flight readiness review comes before launch,
and its objective is
"to verify that the flight and ground segments including all supporting systems such as tracking systems, communication systems and safety systems are ready for launch."
The launch readiness review comes just before launch.
Its objective is to declare readiness for launch of the launch vehicle,
of the space and ground segments
and of all supporting systems,
"and to provide the authorization to proceed for launch."

The operations standard gives the first of these reviews its requirements.
The operations customer chairs it.
It ends the operational validation,
and the standard lists five things that it shall do.
It shall ensure that the programme of simulations and rehearsals is complete,
that the ground segment is ready,
that every procedure has passed validation
and that the operations teams are ready.
The fifth is to authorise the use of the ground segment for operations in orbit.
The review does not stand alone.
"The results of the ORR shall be presented at the flight readiness review (FRR)."

The saved text of the project planning standard holds no wording of go or no-go.
The authorisation to proceed for launch is its nearest equivalent.
The passages read name no signatory and no certificate for that authorisation.
On the author's reading of the review standard,
the review authority would decide whether the review met its objectives,
and the customer would decide what follows.

## Operations Documents During Flight

Once the mission flies,
two kinds of document govern it,
the plan and the procedure.
The European operations standard prescribes both in outline.
On the NASA side the directives name the plan and leave its contents to the project.

### The Mission Operations Plan

The standard defines the plan in one sentence.
"The mission operations plan (MOP) contains all the rules, procedures and timelines necessary to implement the in-orbit operations for the mission during all mission phases in accordance with the mission objectives and respecting any constraints imposed by the design of the space and ground segments."
MOP stands for mission operations plan.
The plan also holds the rules and procedures for contingency operations.
After an introduction and a list of documents,
Annex G gives it four sections.

- **Mission management.**
  The mission rules,
  the management of mission operations,
  and configuration management and change control.
- **Mission phase operations.**
  For each phase,
  a description with the major events and their timings,
  the strategy for carrying out the operations,
  and the timelines.
- **Operations procedures.**
  The procedures for nominal and contingency operations of the space and ground segments,
  organised in a hierarchy.
- **Hand-over procedures.**
  The procedures for passing operations from one authority to another.

The section on management must include the means of deciding to go on.
The standard asks for
"mechanisms for confirming the readiness to proceed with operations (briefing) and for reviewing the progress of execution of operations"
which it calls the briefing and the de-briefing.
A timeline has six required parts.

1. A definition of each operational activity.
2. The planned start time,
   absolute or relative.
3. The operational position that executes or monitors the activity.
4. The background activities of each supporting team.
5. A cross-reference to the operations procedures.
6. The breakpoints for briefing and de-briefing.

The section on procedures needs an index of their state.
"A matrix shall be provided indicating for each procedure the mission phase(s) to which it is applicable, and the authorization status of the procedure (validated or not validated)."

The standard names the phases that such a plan must cover.
Critical phases include the launch and early orbit phase,
commissioning,
a planetary flyby or orbit insertion,
and rendezvous and docking.
Routine phases include mission exploitation,
cruise
and hibernation.

### The Operations Procedure

The procedure is the unit beneath the plan.
"An operations procedure is an elementary component of the mission operations plan that defines the actions to achieve a specific operational objective."
Each has a unique number.
The annex on procedures fixes its parts.

1. Preliminary elements,
   namely the title,
   the version control
   and the author.
2. Introduction.
3. Required operational authority.
4. Expected duration.
5. Pre-conditions,
   which refer to the mission phase,
   the configuration of the ground and space segments,
   the orbit position or environmental conditions,
   and the status of other procedures.
6. Procedure body,
   built of steps,
   with a contingency element.
7. Post conditions.

The contingency element says what to do when a step fails,
and it allows three outcomes.
The operator restores the configuration and resumes,
or reaches the goal by another route and stops,
or aborts.
The procedure ends with a verdict and not with its last step.
"Following verification, the status of the procedure shall be one of the following: 1. procedure terminated, success confirmed, or 2. procedure terminated, procedure failed (including reasons)."

### Validation, Execution and Reporting

A plan and its procedures must pass a validation before flight.
The operational validation plan of Annex F covers simulations and rehearsals,
ground segment readiness tests,
and the records and reports of both.
It must identify
"the mechanisms and criteria to be used for measuring and evaluating the success of the operational validation."
The standard describes the rehearsal in terms that bear on any simulated flight.
"Simulations and rehearsals, where operational teams execute nominal and contingency operational scenarios from the MOP using the operational simulator in place of the real spacecraft."

In flight the plan binds.
"All space and ground segment control activities shall be executed in accordance with the plans and procedures as documented in the MOP for those phases."
When events leave the plan,
the standard does not permit improvisation.
"In case of a mission contingency not covered by the MOP, a new plan and procedure(s) shall be produced, validated and approved before being implemented."
The standard also requires a board to review and analyse anomalies of the space segment and to agree on corrective measures.

The standard then lists the reports that operations produce.
Status reports appear at a frequency agreed with the customer,
and a note suggests the rhythm.
"The reporting frequency generally depends on the mission phase e.g. daily for LEOP or critical operations, weekly for routine operations."
LEOP is the launch and early orbit phase in the standard's list of abbreviations,
and the launch and early operations phase in one of its clauses.
An engineering assessment report follows that phase or any critical operation,
and a commissioning report ends the commissioning in orbit.
Performance reports with trend analysis appear at intervals
"to determine success in meeting the mission objectives."
An operations anomaly report records each anomaly.
Of all these reports,
the standard prescribes the contents of the last alone.
The anomaly report has a unique number,
the operational context,
the suspected source,
the date and time,
and a severity graded as no impact,
minor impact
or major impact.
Its sections then give the details of the anomaly,
the actions taken,
the operational impact
and the recommendations.

### Practice at an Operations Centre

The terms flight operations plan and flight control procedure do not occur in the standard.
They are the usage of ESA's operations centre,
and a public report on one mission shows the scale of what they name.
The end-of-mission report for the Gravity Field and Steady-State Ocean Circulation Explorer,
GOCE,
says that at launch the mission's flight operations plan
"contained 970 procedures, all of which had been validated in the pre-launch mission preparation phase"
[ESA 2014][esa_goce_end_of_mission_2014].
After launch the team raised 87 change requests that affected 212 procedures,
added 51 new procedures,
and reissued the plan about twice a year.
The last version held 1,021 procedures.

### The NASA Side

NASA's project management directive makes the Mission Operations Plan one of the control plans of the Project Plan,
and describes it in three sentences.
"Describe the activities required to perform the mission. Describe how the project will implement the associated facilities, hardware, software, and procedures required to complete the mission. Describe mission operations plans, rules, and constraints."
The Systems Engineering Handbook places the detail in the procedures and the rules.
"Additional detail in the form of operational guidelines and constraints should be incorporated in mission operations procedures and flight rules."
The author obtained no NASA flight plan or book of procedures for this article,
so the outline of those documents above rests on the European standard.

## Reports After Flight

The report closes the loop that the plan opened.
The standards say little about its contents,
and the reports themselves say a great deal.

### What NASA Requires

Two NASA reviews look back at a flight.
The Post-Launch Assessment Review follows deployment,
and the first of its recommended success criteria sets the standard for a comparison with prediction.
"The observed spacecraft and science payload performance agrees with prediction, or if not, is adequately understood so that future behavior can be predicted with confidence."
The Post-Flight Assessment Review belongs to human space flight.
"The PFAR evaluates how well mission objectives were met during a mission and identifies all flight and ground system anomalies that occurred during the flight and determines the actions necessary to mitigate or resolve the anomalies for future flights of the same spacecraft design."
PFAR stands for Post-Flight Assessment Review.
The appendix recommends six entrance criteria for it,
which require that the project has dispositioned all anomalies,
made the documentation available,
completed the post-flight activities,
the problem reports
and the evaluation reports,
and planned the retention of its records.
The first of its six recommended success criteria names the report.
"Formal final report documenting flight performance and recommendations for future missions is complete and adequate."
The others ask that the project document the anomalies,
assess their impact on later flights,
keep the records for comparison and trending,
and hold a credible plan for the recommended changes.

At the end of a project the directive defines a Final Mission Report.
"The Final Mission Report is a summary of what the mission accomplished and is prepared at the end of a mission."
It
"generally includes a summary of the mission accomplishments, science data/samples collected, and a summary of the results achieved."
An appendix of the directive lists the report among the products of a project.
The management handbook is candid about its force.
"The Final Mission Report is a best practice as opposed to a requirement."
The directives therefore fix no outline for a mission report,
and the form has to come from the reports.

### Two NASA Mission Reports

The Apollo 11 Mission Report of November 1969 has seventeen chapters
[NASA 1969][agency_nasa_apollo_11_mission_report].

1. Summary.
2. Introduction.
3. Mission Description.
4. Pilots' Report.
5. Lunar Descent and Ascent.
6. Communications.
7. Trajectory.
8. Command and Service Module Performance.
9. Lunar Module Performance.
10. Extravehicular Mobility Unit Performance.
11. The Lunar Surface.
12. Biomedical Evaluation.
13. Mission Support Performance.
14. Assessment of Mission Objectives.
15. Launch Vehicle Summary.
16. Anomaly Summary.
17. Conclusions.

The two performance chapters proceed subsystem by subsystem and each ends with a section on consumables.
Five appendices give the vehicle descriptions,
the spacecraft histories,
the postflight testing,
the availability of data
and a glossary.

The report of a later Space Shuttle flight keeps the same bones.
The STS-81 Space Shuttle Mission Report of March 1997 runs as follows
[NASA 1997][agency_nasa_sts_81_mission_report].
STS stands for Space Transportation System.

1. Introduction.
2. Mission Summary.
3. Payloads and Experiments.
4. Vehicle Performance,
   by element and then by subsystem of the orbiter.
5. Government furnished equipment and flight crew equipment.
6. Cargo Integration.
7. Development Test Objectives and Detailed Supplementary Objectives.
8. Photography and Television Analysis.

Three tables close it,
namely the sequence of events,
the list of in-flight anomalies of the orbiter
and a list for tracking problems with government furnished equipment.
The introduction says why the report exists.
"The requirement is that each organizational element supporting the Program will report the results of their hardware and software evaluation and mission performance plus identify all related in-flight anomalies."
It also fixes the time references,
which a report needs before it can state a single event.
"All times during the flight are given in Greenwich mean time (G.m.t.) and mission elapsed time (MET)."

### Planned Against Actual

A reader might expect the comparison of plan and flight to sit in the timeline.
In neither report does it.
The sequence of events in the Apollo report has two columns,
the event and the time,
and the times are those of the flight.
The Shuttle report's table has a column of actual time and none of planned time.

The comparison sits in the tables of consumables and performance.
The Apollo report's table of reaction control propellant for the service module sets actual usage,
split into fuel,
oxidizer
and total,
beside the usage planned before flight.
Two of its rows follow,
in pounds.

| Condition | Actual usage, total | Preflight planned usage |
|---|---|---|
| Consumed | 560 | 590 |
| Remaining at separation of the command and service modules | 780 | 752 |

The text above the table states the agreement as a tolerance.
"Reaction control system propellant usage predictions and flight data agreed within 5 percent."
The consumed row is consistent with that statement to the nearest percent.
The actual total falls 30 pounds short of the plan,
a difference of about 5 percent of the planned figure.
The same paragraph explains the difference by phase of flight,
with usage above expectation early and below it during the rendezvous.

The Shuttle report pairs the columns instead.
Its table of solid rocket motor performance gives a predicted and an actual value for each motor.
Two of its rows of event times follow,
in seconds.

| Parameter | Left motor, predicted and actual | Right motor, predicted and actual |
|---|---|---|
| 50 psia cue time | 120.3 and 120.7 | 120.4 and 120.5 |
| Separation command | 125.3 and 125.6 | 125.3 and 125.6 |

Where a limit exists,
the prose gives the value and the limit together.
"These values were well within the 3.2 percent allowable limits."
Where no table serves,
both reports compare in a sentence.
The Apollo trajectory chapter records one manoeuvre as
"a velocity change of only 1.2 ft/sec less than planned."

The author draws the form from these examples.
A comparison names the quantity,
gives the planned value and the actual value in the same units,
states the difference or the tolerance,
and explains any difference that matters.

### Whether the Mission Met Its Objectives

The Apollo report gives the assessment a chapter.
It opens with the verdict on the one objective that mattered most.
"The single primary objective was met."
A table then lists the detailed objectives and experiments,
with a description of each and a column that records whether the crew completed it.
The entries in that column are Yes and Partial.
Each objective not fully met receives a subsection that explains the shortfall and says what will happen next.
One such subsection states
"This objective will be repeated for the Apollo 12 mission."
Another gives the cause.
"time constraints on the extravehicular activity precluded collection of these samples with the degree of documentation originally planned."

The Shuttle report grades by degree.
Its section on one payload opens with a count,
"All eleven of the Biorack experiments were completed"
and then gives each experiment a percentage of its planned return,
with a reason for any shortfall.
One line reads
"80 percent - Reduced time due to flight day 4 docking"
and another simply
"100 percent"
without comment.
Each test objective receives a verdict in a paragraph,
including the case in which the flight produced nothing.
"The conditions at landing did not support this DTO; consequently no data were collected for the DTO."
DTO stands for development test objective.

Three practices recur across the two reports.
The assessment restates each objective before judging it.
The verdict has more than two values.
And a shortfall always carries a reason and a disposition.

### Anomalies

The Apollo report gives each anomaly a numbered subsection with a short title,
such as 16.1.1,
Service Propulsion Nitrogen Leak.
On the author's reading of the entries,
each gives the observation with its data,
the analysis of the cause,
the corrective action for later vehicles
and a closing line.
"This anomaly is closed."
The saved text of the report holds that line 24 times.
The Shuttle report uses a table with four columns,
which are a number,
a title,
a reference
and comments.
In the entries that the author read,
each anomaly has an identifier that names the mission,
the element
and a sequence number,
as in STS-81-V-01.
The reference column gives the time of the event in both time systems
and the numbers of the related problem records.
The comments narrate the observation,
the response in flight,
the troubleshooting after flight
and the disposition.

The Apollo report ends with nine numbered conclusions.
They are findings and not recommendations,
as in
"The two-man prelaunch checkout and countdown for ascent from the lunar surface were well planned and executed."

### European Reports and the End of a Mission

The European operations standard names many reports and outlines one.
Besides those of the previous section,
it lists mission reports that cover the experience of mission operations,
a summary of the spacecraft's performance in orbit
and the results of end-of-life tests,
and a report on the disposal operations of the space segment.
It prescribes the contents of none of them.
The reviews are firmer than the reports.
A flight qualification review ends the commissioning,
in-orbit operations reviews recur through the utilisation phase,
and two reviews end the mission.
"Phase E2 shall be concluded by the end-of-life review (ELR), which shall verify that the mission has completed its useful operation or service and that the procedures for disposal are in place."
ELR stands for end-of-life review.
The mission close-out review then ends phase F,
and its purpose is
"to assess the performance of the services provided and to confirm proper disposal of space and ground segments."

Two public documents show what ESA's operators write.
The first is the end-of-mission operations report for GOCE,
which carries the marking For Official Use and which the author read in an archive copy.
Its chapters are an introduction,
an overview of the mission with one section for each phase,
spacecraft operations,
the space segment
and the ground segment.
Its annexes list the spacecraft anomaly reports,
the publications
and a mission calendar.
The report compares plan and flight in narrative and in paired figures,
and it does so by exception.
Of the routine phase it says
"This mission profile for this phase was significantly different than the profile originally planned before launch"
and it sets the planned altitude profile and the actual one in consecutive figures.
Where the flight went better than the plan it says that too.
"the low fuel consumption allowed extending the mission beyond the originally planned 20+10 months."

The second is a status report from the first days of the Venus Express mission
[ESA 2005][esa_venus_express_status_3].
It is a narrative ordered by ground station pass,
followed by a table of coming events with a date and the scheduled event.
It compares flight with plan in three ways.
It states completion,
and what the team gained on the schedule.
"All foreseen activities were completed and it was also possible to bring forward some platform commissioning activities, which were planned for the coming weekend."
It compares behaviour with prediction.
"It is to be noted that both the power and the thermal behaviour of the spacecraft are very close to pre-launch flight predictions."
And it gives the accuracy of a manoeuvre.
"Post manoeuvre assessment based on Doppler data indicated that manoeuvre accuracy was within 0.034%."

The author found in neither European report a table of requirement against achieved value.
That absence is an observation about two documents and not a finding about ESA practice at large.

One European document does come with a fixed outline at the end of a mission.
ECSS adopts the international standard on space debris mitigation,
ISO 24113 in its edition of 2023,
through a notice that reproduces the minimum contents of a space debris mitigation plan
[ECSS 2024][ecss_u_as_10c_rev2].
The plan holds the applicable requirements,
the plans for addressing them,
the means of verification and validation,
a compliance matrix,
justifications for any non-compliance
and,
by an ECSS addition,
"a justification for the selection of the disposal option."
The author did not read ISO 24113,
which its publisher sells.
ESA's own standard,
which carries the marking For Official Use,
adds a report that states how the project implemented and verified its compliance
[ESA 2023a][esa_essb_st_u_007].
The project reissues that report at several points,
among them the design reviews,
any extension of the mission,
the end of the mission
and the approach of re-entry.
ESA's policy requires approval of the plan at the System Requirements Review
and of the report at the Acceptance Review
or at a combined Qualification and Acceptance Review
[ESA 2023b][esa_admin_ipol_2023_1].

### Lessons Learned

Every regime asks for lessons and none prescribes their form.
NASA's directive on programmes and projects defines a lesson as
"Captured knowledge or understanding gained through experience which, if shared, would benefit the work of others"
[NASA 2024a][agency_nasa_npr_7120_5f].
The agency's knowledge policy says that a project prepares its Final Mission Report together with its lessons,
under the agency's knowledge policy
[NASA 2019a][agency_nasa_npd_7120_6a].
The launch service directive requires lessons and corrective actions after each mission,
and the European operations standard requires reports on
"mission operations experience, lessons learned, spacecraft in-orbit performance and end-of-life tests"
as feedback to the engineering of later missions.

## Flying a Stand-In

Many missions never leave the ground.
A crew lives in a habitat in a desert,
a team flies a spacecraft that exists only in software,
or an engineer tests a model one tenth the size of the vehicle.
Each of these is a stand-in for a real mission,
and each yields results that someone will want to apply to the real one.
The documents surveyed in this section answer one question.
What must the record say about the stand-in,
so that a later reader knows how far its results reach?

No single standard governs the answer.
Four bodies of practice bear on it,
namely NASA's analogue missions,
NASA's standard for models and simulations,
the defence practice of accreditation,
and the engineering principle of similitude.
They use different words,
and in the author's reading their records overlap.

### Analogue Missions

NASA defines the analogue by resemblance.
"Analog missions are remote field tests in locations that are identified based on their physical similarities to the extreme space environments of a target mission."
The definition comes from a fact sheet of 2011,
which also says what the missions are for.
They
"provide NASA with data about strengths, limitations and validity of planned human-robotic exploration operations"
[NASA 2011][agency_nasa_analog_fact_sheet_2011].
A NASA conference paper of the following year makes the partial character of the resemblance part of the definition.
The missions,
it says,
frequently occur in remote and extreme environments that are
"representative in one or more ways to that of future spaceflight destinations"
[Reagan et al. 2012][agency_nasa_reagan_2012].
An analogue is therefore like its target in some ways,
by definition,
and the definition claims nothing about the rest.

The list of analogues changes,
and any list needs a date.
The fact sheet of 2011 names six.
The agency's web page,
as the author retrieved it in November 2026,
lists eleven active analogues and one past analogue,
and neither the undersea laboratory nor the desert studies of the 2011 list appears on it
[NASA 2026a][agency_nasa_analog_missions_page].
A reader has to assemble from several sources what each analogue reproduces
and what it does not.

| Analogue | Reproduces | Does not reproduce |
|---|---|---|
| The undersea laboratory of NASA's Extreme Environment Mission Operations | Isolation, real hazard, a small crew, and buoyancy that the divers can adjust from weightlessness to lunar or Martian gravity | Long duration. Its missions last two to three weeks |
| Desert Research and Technology Studies | Rough and dusty terrain, extreme swings of temperature, and realistic communication from a remote place | Not stated in the sources read. For behavioural research the assessment report described below placed it in the third of four tiers |
| The Human Exploration Research Analog | Isolation, confinement and remote conditions, for up to 45 days, with a communication delay of up to 20 minutes each way | Microgravity, which a review of 2025 says that platforms of this class do not reproduce, and perhaps the sense of true separation from Earth, which the same review says many analogues may not fully capture |
| The International Space Station | Microgravity, long duration and real astronauts | Partial gravity and surface operations |

The sources for the table are the fact sheet,
the conference paper,
a facility document for the third analogue
[NASA 2019b][agency_nasa_hera_2019],
and two peer-reviewed reviews.
The first review states the general position.
"Analogs, by definition, will never be perfect, but they are a useful component of an integrated effort to understand the human risks of living and working in space."
It adds that
"A single perfect ground analog that simulates all the characteristics and effects of spaceflight does not exist"
and says of the station that
"factors such as partial gravity and surface operations, for example, cannot be simulated"
[Cromwell et al. 2021][research_cromwell_2021].
The second review reports that the gap changes results.
In its words,
missions in the Human Exploration Research Analog
"have been limited in their ability to induce spaceflight-like behavioral responses"
[Rahill et al. 2025][research_rahill_2025].

An agency page describes its newest analogue only by what it simulates.
The Crew Health and Performance Exploration Analog is a series of missions that
"simulate year-long stays on the surface of Mars"
[NASA 2026b][agency_nasa_chapea_page].
The author found no NASA page that states by name what that analogue does not reproduce.
The pattern holds on the European side.
ESA's page on its cave training course lists the resemblances,
among them
"isolation from the outside world, lack of diurnal cycles, confinement"
and states no limits
[ESA CAVES][esa_what_is_caves].
On this evidence the public pages describe similarity,
and the limits live in the technical literature.

### How NASA Rates an Analogue

One NASA report rates analogues against a flight environment by a stated method.
It is the Analog Assessment Tool Report of May 2011,
written for research on behavioural health
[Keeton et al. 2011][agency_nasa_analog_assessment_tool].
The report begins from a gap.
"However, before the development of our Analog Assessment Tool, an objective and systematic way to determine which platform would be most suitable to conduct research did not exist."

The method has three parts.
The first weights the characteristics of an analogue by their importance,
in two groups,
research and utility.
The second rates each candidate analogue for fidelity on each characteristic.
The third combines the two sets of weights into a ranking.
The edition described in the report used 18 research characteristics and 9 utility characteristics,
and compared twelve analogues against a mission to Mars.

Two features of the method deserve imitation.
The first is that the report writes the target down before it rates anything.
For each characteristic it records how the authors expect that characteristic to appear in the real mission.
"These assumptions are necessary for fidelity comparisons."
Each analogue then receives a description against the same list.
Three rows show the form.

| Characteristic | Assumed for the long-duration mission | Recorded for the undersea laboratory |
|---|---|---|
| Physical isolation | High. The crew is isolated to its own members, and escape is impossible or highly improbable | Under water for approximately 2 to 3 weeks |
| Communication with the outside | Delays with the ground of 4 to 40 minutes for a full communication loop | Communication with topside, by internet and video conferencing |
| Team size | Small, four to six crew members, likely of mixed gender and multicultural | Up to six crew members |

A reader sets the two columns side by side and has the difference for each characteristic.

The second feature is the question that the experts answer.
They
"must determine how well a specific characteristic in an analog matches that same characteristic in the space flight scenario."
The tool has no fixed scale for that judgement.
The experts compare the analogues two at a time,
and a method of pairwise comparison,
the Analytic Hierarchy Process,
turns their judgements into relative weights between 0 and 1.
The report's table of overall weights includes these rows.

| Analogue | Research and utility weights | Average |
|---|---|---|
| International Space Station | 0.199920 and 0.124855 | 0.162387 |
| The undersea laboratory | 0.153658 and 0.161633 | 0.157645 |
| Concordia station, Antarctica | 0.107185 and 0.082588 | 0.094886 |
| Desert Research and Technology Studies | 0.034709 and 0.102042 | 0.068376 |

The author infers a caution from the method.
A weight ranks an analogue against the others in the comparison.
It does not measure the distance between the analogue and the target on any absolute scale.

The report itself warns against reading the ranking too simply.
"Simply considering the fidelity of an analog, however, may not be enough to ensure that the analog serves as the appropriate platform through which to address a research gap."
Its example is Devon Island,
whose terrain resembles that of Mars,
where
"there is constant daylight on Devon Island while Mars has a similar Earth day-night cycle of 24 hours and 39 minutes."
For a study of sleep,
the report says,
the effects of constant daylight may outweigh the resemblance of the terrain.
Fidelity therefore belongs to a characteristic and a question,
and not to an analogue as a whole.
The report draws a constructive use from the same table,
since a small weight on one characteristic shows what an operator must improve
to raise the fidelity of the analogue for the scenario in question.

### European Analogue Sites

A study for ESA takes the same view from the side of geology.
The Catalogue of Planetary Analogues of December 2012 assigns terrestrial sites to features of a planet,
and not to the planet as a whole
[Preston et al. 2012][esa_catalogue_planetary_analogues].
The features of the Moon,
for instance,
"have been assigned terrestrial field sites that mimic one or more of these features."
Each site chapter follows one template,
with sections for location,
context,
environment,
infrastructure
and references,
and with site details under repeated subheadings that end with prior use as an analogue.

The catalogue states limits inside its entries.
One entry concedes that
"current conditions almost certainly preclude such a habitat on contemporary Mars"
before it says what the site may still teach.
Another qualifies one of the uses that it lists,
"surface EVA in terrestrial gravity"
where EVA stands for extravehicular activity.
The author reads the qualification as a statement of a limit.
And where a comparison needs scaling,
the entry says so.
The catalogue calls the Mistastin crater comparable to many of the larger impact craters on the Moon
"when scaled for gravity differences."
A peer-reviewed survey of terrestrial analogues puts the principle in a sentence,
which the author read in the abstract only.
"Their value relies on the similarity of the analogue to its target"
[Preston and Dartnell 2014][research_preston_dartnell_2014].

### The NASA Standard for Models and Simulations

The fullest statement of what to record about a stand-in is NASA-STD-7009B,
the Standard for Models and Simulations,
approved on 5 March 2024
[NASA 2024e][agency_nasa_std_7009b].
It supersedes revision A with its Change 1,
and a reader who cites revision A cites a superseded text.
The agency's catalogue marks the standard
"Not a NASA Mandatory Standard"
which the author takes to mean that its requirements bind a project only where something else invokes the standard.
The numbered sentences with the word shall are its requirements.
The table and the text below mark the clauses that are recommendations.
The standard abbreviates models and simulations as M&S,
the real-world system as RWS,
and verification and validation as V&V.

Its definitions are the vocabulary of the whole subject.
"Model: A description or representation of a system, entity, phenomenon, or process."
"Simulation: The imitation of the behavioral characteristics of a system, entity, phenomenon, or process."
"Validation: The process of determining the degree to which a model or a simulation is an accurate representation of the real world from the perspective of the intended uses of the M&S."
Validation needs something to compare against,
which the standard calls the referent,
and the referent may itself be a stand-in.
"A referent may be the RWS to which the analysis is directed, a similar or analogous system (whereby the closeness of the referent to the RWS becomes pertinent), or a higher-fidelity M&S."
The standard counts scaling among the abstractions that a model may make,
and it attaches a claim to every abstraction.
"Any modeling abstraction carries with it the assumption that it does not significantly affect the intended uses of the M&S."

The standard requires a series of records.

| Record | Clause and force | Content |
|---|---|---|
| Intended use | 4.1.1.1, requirement M&S 40 | The expected purpose and application |
| Assumptions and abstractions | 4.2.1.4, requirement M&S 11 | Each with its rationale and its consequences for the intended uses |
| Limits | 4.2.1.6, requirement M&S 13 | The bounding set of parameters or variables, such as boundary conditions |
| Permissible uses | 4.2.1.7, requirement M&S 14 | The purposes for which the model or simulation is formally allowed |
| Domain of validation | 4.2.5.2, requirement M&S 18 | The region of inputs for which the responses compare favourably with the referent |
| Aspects not validated | 4.2.6, recommendation d | Whatever the validation did not cover |
| Appropriateness for a proposed use | 4.3.1.2, requirement M&S 23 | The proposed use set against the permissible use |

The second row is the one that records differences.
"A record of the assumptions and abstractions underlying the conceptual and implemented model, including their rationales and consequences with respect to the intended uses of the M&S, shall be maintained."
The standard gives the reason,
which is that such a record
"clarifies areas where the M&S differs from the RWS"
and it does not stop at a list of differences.
Each entry carries its rationale and its consequences.
For commercial,
government
and legacy software,
the standard lightens the load.
Some of this information
"may be available in published user guides; a reference to the user guides may suffice for this part of these records."

### Use Outside the Validated Domain

The standard foresees that someone will use a model beyond what anyone validated.
Its requirement M&S 26 offers two courses.
The user either keeps within the permissible uses and the domains of verification and validation,
or does the following.
"Placard the M&S and analysis results with a warning that the M&S were not used in accordance with the permissible uses or were used outside the domains of V&V and include the type of limit exceeded, the extent that the limit was exceeded, and an assessment of the consequences of this action on the M&S results."
The placard has three parts,
which are the kind of limit,
the extent of the excess
and the consequences.
A bare disclaimer does not satisfy the clause.

The same discipline governs the report of results.
The standard lists what a decision maker needs.
"This includes (1) the best estimate of the results, (2) a statement on the uncertainty in the results, (3) objective, credibility supporting, assessments of the M&S capabilities and M&S results (Appendix E), (4) explicit caveats accompanying the results (e.g., the use of the M&S in violation of its assumptions or M&S limits), and (5) the risks associated with accepting the results of the M&S."
Requirement M&S 32 then makes the caveats mandatory.
A report must carry explicit warnings for eight kinds of occurrence,
each
"accompanied by at least a qualitative estimate of the impact of the occurrence"
and two of the eight are the cases at issue here.
"b. Violation of assumptions of the M&S used (as specified in [M&S 11])."
"c. Violation of the M&S limits (as specified in [M&S 13])."
Requirement M&S 33 treats uncertainty in the same spirit.
The report must give a quantitative estimate,
or a qualitative description,
or
"A clear statement that no quantitative estimate or qualitative description of uncertainty is available."
The standard will not accept silence,
and it says why.
"Results without an estimate of uncertainty may differ vastly from those shown."
Two recommendations close the report.
"a. Include concluding remarks stating whether the M&S results are credible enough for the actual use."
"e. Include dissenting technical opinions regarding the credibility of the results or any recommended actions."

### The Assessment Scales

Revision B changed the way the standard grades credibility.
Revision A had one scale of eight factors.
Revision B has two assessments,
one of the capability of the model with five factors
and one of the results with six,
each illustrated as levels from 0 to 4.
The five factors of capability are
"M&S Data Pedigree, M&S Verification, M&S Validation, M&S Development Technical Review, and M&S Development Process/Product Management"
and the six factors of results are
"M&S Use Assessment, M&S Input Pedigree, M&S Uncertainty Characterization, M&S Results Robustness, M&S Use/Analysis Technical Review, and M&S Use Process/Product Management"
in the standard's words.
The standard advises against combining the factors into one score,
and it sets no pass mark.
"This Standard levies no requirements with respect to what levels to achieve (the sufficiency threshold levels), merely that the levels be determined and reported."

Two of the eleven factors bear directly on a stand-in.
The validation factor asks a double question.
"M&S Validation: Did the M&S results compare favorably to the referent data, and how close is the referent to the RWS?"
The use assessment factor asks how far the proposed use lies from what the model has done before.
The table condenses the levels of both.

| Level | Validation factor | Use assessment factor |
|---|---|---|
| 4 | Results compare favourably with measurements on the real system in its operating environment | The proposed use is within the domain of validation and nearly identical to previous uses |
| 3 | Results compare favourably with measurements on the real system in a representative environment | The proposed use is within the domain of verification and differs in minor ways from prior uses |
| 2 | Results compare favourably with measurements from a representative system | The proposed use is within the limits of the model and differs in moderate ways from prior uses |
| 1 | The model is conceptually validated | The type, application domain and purpose match the proposed use, which is the first use or departs widely from prior uses |
| 0 | Insufficient evidence | Insufficient evidence |

At levels 2 to 4 the validation factor also accepts a comparison with a model of higher fidelity that itself meets the level.
The ladder is a ladder of stand-ins.
A comparison with the real system in its real environment ranks highest,
the real system in a representative environment comes next,
and a representative system comes third.

The companion handbook,
NASA-HDBK-7009B,
adds guidance
[NASA 2026c][agency_nasa_hdbk_7009b].
Its cover gives an approval date of 3 February 2026,
its own history log dates the revision 24 September 2025,
and its pages still carry a draft header,
so a reader should cite it with care.
It states the point of this whole section in a clause,
"Understanding and accounting for the differences between the referent and RWS is essential"
and it distinguishes five statements of use,
namely the intended,
the permissible,
the proposed,
the accepted
and the actual use.
When the permissible use does not cover the proposed one,
"a decision must be made to either revise (de-scope) the Proposed Use or to proceed at risk by accepting a Proposed Use that exceeds the M&S capabilities."

### Accreditation in Defence Practice

The United States Department of Defense,
DoD,
documents the same judgement under the name of accreditation.
Its standard practice is MIL-STD-3022 with Change 1 of 5 April 2012
[DoD 2012][mil_std_3022].
The author read it from a mirror and did not check its currency against the department's own database.
The standard defines its terms.
"3.1.1 Accreditation. The official certification that a model, simulation, or federation of models and simulations and its associated data are acceptable for use for a specific purpose."
"3.1.16 Validation. The process of determining the degree to which a model, simulation, or federation of models and simulations, and their associated data are accurate representations of the real world from the perspective of the intended use(s)."
Accreditation is thus always for a purpose,
and validation is always from the perspective of a use.

The standard supplies templates for four documents,
"Accreditation Plan; V&V Plan; V&V Report, and Accreditation Report."
It has no document called a validation report,
and the results of validation go into the third of the four.
The Accreditation Plan has eight sections.

1. Executive summary.
2. Problem statement,
   with the intended use,
   an overview of the model or simulation,
   its application
   and the scope of the accreditation.
3. Requirements and acceptability criteria.
4. Assumptions,
   capabilities,
   limitations,
   and risks and impacts.
5. Accreditation methodology.
6. Accreditation issues.
7. Key participants.
8. Planned accreditation resources.

The problem statement fixes what is at stake before anyone examines the model.
"It documents (1) the question(s) to be answered and the particular aspects of the problem that the M&S will be used to help address; (2) the decisions that will be made based on the M&S results; and (3) the consequences resulting from erroneous M&S outputs."
The fourth section is common to all four documents,
and its heading in the standard is
"M&S ASSUMPTIONS, CAPABILITIES, LIMITATIONS & RISKS/IMPACTS"
with a subsection for each of the four.
The subsection on limitations
"describes the known constraints and limitations associated with the development, testing, and/or use of the M&S."
The subsection on risks carries the implications,
and makes them mandatory.
"The impacts associated with these risk factors shall also be described."
The plan also records the reference against which an assessor measures the model.
"The basis for comparison serves as the reference against which the accuracy of the M&S representations is measured."
The standard admits experiments,
theory,
validated results from other models
and expert knowledge as such a basis.

One rule of the standard protects a template against quiet omission.
"When a section or subsection of a template is not applicable, the section or subsection shall be retained for completeness"
and marked as not applicable.
A reader then knows that the author considered the heading and found nothing to put under it.
NASA's handbook points to this standard,
saying that the outline of its verification and validation report
"could be utilized as a tailorable template to incorporate into M&S activities."

The author infers that the heading of four parts is the nearest published template for a section on how a stand-in differs from the real thing.
Assumptions and limitations say where the stand-in departs.
Capabilities say what it does reproduce.
Risks and impacts say what follows for a user.

### Fidelity and the Three Levels of Use

Two further sources sharpen the vocabulary.
A doctoral thesis at Delft University of Technology reproduces an excerpt of the glossary of a study group on fidelity
of the Simulation Interoperability Standards Organization
[Roza 2005][ref_roza_2005].
The glossary defines fidelity as the degree to which a model or simulation reproduces the state and behaviour of a real world object,
and it adds that a writer should describe fidelity with respect to the measures or standards used in stating it.
The thesis reports a distinction that matters to any reader of a simulated result.
"According to Pace, simulation fidelity is an absolute concept while simulation validity is a relative concept, dependent upon the simulation application."
The author draws the consequence that a stand-in of low fidelity can be valid for a modest use,
and one of high fidelity invalid for an ambitious one.
The file of the thesis forbids copying,
and the author transcribed these passages by hand.

The second source is a NASA site on computational fluid dynamics,
which reproduces definitions from a guide of the American Institute of Aeronautics and Astronautics
[NASA Glenn 2021a][agency_nasa_nparc_glossary].
The author did not read the guide itself.
The site gives a name to the use of a model beyond its validation.
Prediction is the
"Use of a CFD model to foretell the state of a physical system under conditions for which the CFD model has not been validated."
CFD stands for computational fluid dynamics.
The site is frank about what supports a prediction.
"The best one can do is point to the verification results and the most similar validation case."
Its overview sorts the uses of a result into three levels,
which are to
"1) provide qualitative information, 2) provide incremental quantities, and 3) provide absolute quantities"
[NASA Glenn 2021b][agency_nasa_nparc_overview].
The three levels give a compact way to say what a stand-in supports.
A reader may trust a stand-in for the qualitative behaviour,
or for the difference between two cases,
without trusting it for an absolute number.
That application of the three levels to stand-ins in general is the author's.

### Similitude

Engineers who test scale models have the oldest discipline of the four.
A NASA technical paper of August 1979 on model testing of aircraft states it
[Wolowicz et al. 1979][agency_nasa_tp_1435].
"To apply the data to a full-scale aircraft or its components with maximum validity, certain similitude conditions must be met."
The formal statement is that
"the dependence of one physical quantity on others involved in the experiment must be the same for the model and the full-scale airplane."
No test meets every condition.
"Most tests are designed for certain similitude conditions at the expense of other parameters."
The limits of the data follow from the conditions left unmet.
"One of the prime factors necessary to determine the limitations of data obtained from a model is the degree to which the similitude requirements have been met."

The paper's central example concerns gravity.
A dimensionless group,
the Froude number,
must match between model and aircraft for inertial and gravitational effects to be similar.
Let $N\_{\mathrm{Fr}}$ be the Froude number,
$V$ the velocity,
$l$ the characteristic dimension
and $g$ the acceleration of gravity.

$$
N_{\mathrm{Fr}} = \frac{V^{2}}{l g}
\tag{5}
$$

A model smaller than the aircraft has a smaller $l$,
and the tester cannot change $g$ to compensate.
The paper states the consequence for a model that must also match the Mach number.
"Since such scaling is not possible, Froude number similitude can be achieved only under limited geometric-scale conditions, and thus, the model would normally be flown at a different angle of attack than the full-scale airplane."
The thing that no tester can scale is the gravitational field.
The paper then states the limit on its conclusions in plain terms,
finding that conventional Mach scaling
"may be inadequate for simulating the stability, control, and handling qualities characteristics of the actual airplane because of the inability to satisfy Froude number similitude requirements"
in the words of its concluding remarks.

The paper tabulates its scaling.
One table defines the similitude parameters.
Another lists,
for each physical quantity,
the ratio of the model's value to the aircraft's under two schemes,
headed Froude scaling and Mach scaling.
The author draws a pattern from it for any report of a scaled test.
The report has a table with one row for each governing parameter,
the ratio between the stand-in and the real system,
the scaling scheme chosen,
and a statement of which parameters the test sacrificed and what that does to the results.

The same form serves for a stand-in that nobody designed as a scale model.
For any quantity,
let $q\_{\mathrm{S}}$ be its value in the stand-in
and $q\_{\mathrm{R}}$ its value in the real system.
The ratio $k$ of the two is the first thing a reader needs.

$$
k = \frac{q_{\mathrm{S}}}{q_{\mathrm{R}}}
\tag{6}
$$

On the principle of the paper,
a stand-in that preserved every governing dimensionless group would be similar to its target however far each $k$ lay from one.
A stand-in whose ratios differ from quantity to quantity without a scheme is not a scale model,
and its results transfer only where an argument shows that they do.

### A Worked Comparison of Venus and Eve

The following comparison illustrates the form and settles nothing about any real mission.
It supposes that a campaign of simulated flights plans a mission to Venus
and flies it instead in the commercial game Kerbal Space Program,
to the game's planet Eve.
The game's community wiki states the relation between the two bodies.
"Eve is the second planet from Kerbol, the closest planet to Kerbin, and KSP's analogue for the planet Venus."
KSP stands for Kerbal Space Program,
Kerbol is the game's star
and Kerbin is its counterpart of Earth.

The values for Venus and Earth come from the fact sheets of NASA's Space Science Data Coordinated Archive
[Williams 2024a][agency_nasa_venus_fact_sheet]
[Williams 2024b][agency_nasa_earth_fact_sheet].
The values for Eve and Kerbin come from the wiki,
in the revisions that the author retrieved in November 2026
[Kerbal Space Program Wiki 2026a][ref_ksp_wiki_eve]
[Kerbal Space Program Wiki 2026b][ref_ksp_wiki_kerbin].
The wiki is a community source.
Its editors are players and not the game's developer,
the author did not check its numbers against the game,
and the author did not establish which version of the game each number describes.
Every figure for Eve and Kerbin below carries that weakness.

**Intended use.**
The record begins with the use,
after the defence standard's problem statement and NASA's requirement M&S 40.
For this illustration the use is to rehearse the documents and the sequence of a mission to Venus,
and to compare candidate designs with one another.
The use does not include producing any number for a real flight.

**Governing parameters.**
The table gives each quantity as its source states it.

| Quantity | Venus, NASA fact sheet | Eve, community wiki |
|---|---|---|
| Mass | 4.8673 times 10 to the power 24 kg | 1.2243980 times 10 to the power 23 kg |
| Equatorial radius | 6,051.8 km | 700,000 m |
| Surface gravity | 8.87 metres per second squared | 16.7 metres per second squared |
| Escape velocity | 10.36 km/s | 4,831.96 m/s |
| Surface pressure | 92 bars | 506.625 kPa, or 5 atmospheres |
| Temperature | Average 737 K | Maximum 420 K, minimum 160.02 K, no average given |
| Atmosphere | 96.5 percent carbon dioxide and 3.5 percent nitrogen, near the surface, by volume | Composition not stated |
| Scale height | 15.9 km | None in the article's summary box |
| Sidereal rotation period | 5,832.6 hours, retrograde | 80,500 seconds |
| Semi-major axis | 108.210 million km | 9,832,684,544 m |

Three entries need a note.
The fact sheet prints the rotation period of Venus with a negative sign,
which the author reads as the convention for retrograde rotation.
The wiki says of Eve's atmosphere that its composition is unknown,
and suggests from its molecular weight that it may be largely carbon dioxide.
And the wiki's data pages hold a number labelled scale height for each body,
without a unit,
while the article says that scale height varies with altitude in current versions of the game.
The author treats those numbers as doubtful and omits them.

The second table compares each planet with its own home world.
The fact sheet prints the ratio of Venus to Earth for each quantity.
The author computed the ratio of Eve to Kerbin from the wiki's values.

| Quantity | Venus to Earth, as printed | Eve to Kerbin, computed |
|---|---|---|
| Mass | 0.815 | 2.314 |
| Equatorial radius | 0.949 | 1.167 |
| Surface gravity | 0.903 | 1.70 |
| Escape velocity | 0.926 | 1.408 |
| Semi-major axis | 0.723 | 0.723 |
| Sidereal orbit period | 0.615 | 0.615 |

The surface pressure of Venus is about 91 times that of Earth,
on the fact sheets' figures of 92 bars and 1,014 millibars,
and the wiki gives the pressure of Eve as 5 times that of Kerbin.

The third comparison is direct,
the ratio $k$ of Eve to Venus.
The radius of Eve is 0.116 of the radius of Venus,
and its mass is 0.0252 of the mass of Venus.
Its surface gravity is 1.88 times that of Venus.
Its escape velocity is 0.466 of the escape velocity of Venus.
Its orbit is 0.0909 of the size of the orbit of Venus.
The surface pressure of Venus is about 18 times that of Eve.

**Assumptions and abstractions.**
Each entry gives the departure and its consequence,
after NASA's requirement M&S 11.
The consequences are the author's reading of the ratios.

- **The planetary system is far smaller than the real one.**
  The wiki says of the home world that
  "Kerbin has approximately one-tenth the radius of Earth and 1/113th the mass."
  The orbit of Venus is about 11 times the size of Eve's orbit.
  Every distance,
  every time of flight
  and every velocity in a plan for Eve is therefore a number about the game.
- **The layout of the orbits keeps its proportions.**
  Eve's orbit is 0.723 of Kerbin's,
  as the orbit of Venus is 0.723 of Earth's,
  and the periods stand in the same ratio of 0.615 in both systems.
  The shape of the transfer problem,
  an inner planet reached from a home planet whose orbit is larger in the same proportion,
  therefore survives the change of scale.
- **The planet is not a scaled Venus.**
  Venus is smaller,
  lighter
  and weaker in surface gravity than Earth.
  Eve is larger,
  heavier
  and stronger in surface gravity than Kerbin.
  The direction of the difference from home reverses.
  A lesson that rests on surface gravity or escape velocity does not transfer.
  The cost of leaving either surface also depends on its atmosphere,
  and this article records no delta-v for either planet.
- **The atmosphere differs in degree and perhaps in kind.**
  Both planets have a higher surface pressure than their home worlds,
  by a factor of about 91 for Venus and 5 for Eve.
  The fact sheet gives an average temperature of 737 K for Venus,
  and the highest temperature that the wiki records for Eve is 420 K.
  The wiki also says of Eve's atmosphere that
  "The pressure-altitude profile is globally constant and independent of temperature."
  No result about heating,
  aerodynamic loads
  or the survival of hardware at the surface transfers.
- **The simulation is a game.**
  A peer-reviewed study that used the game as a research environment states the position.
  "Although KSP does not offer a perfect simulation of reality, it has been praised for its accurate orbital mechanics"
  [Carrasco et al. 2025][research_carrasco_2025].
  The same study describes its environment as constrained to a two-body problem and to a small number of planets.
  The author read that study as a preprint and not in its journal version.
  Another paper proposes the game as
  "an educational and concept development platform"
  on the evidence of its abstract,
  which is all that the author read
  [Kawthalkar et al. 2022][research_kawthalkar_2022].

**Limits and what nobody validated.**
After NASA's requirement M&S 13 and its recommendation on aspects not validated,
the record must say that this illustration validated nothing.
The author compared no result of the game with any referent.
The tables compare inputs,
which are the properties of two planets,
and not outputs.
On the validation scale of the NASA standard such a stand-in could not rise above level 1,
since nobody has compared a result with measurements even from a representative system.
That placement is the author's.

**What the result supports.**
By the three levels of use,
a flight to Eve can support qualitative statements about a mission to Venus
where they rest on the order of events and on the proportions of the orbits.
It can support a comparison between two designs flown in the same game,
as a statement about the game,
and the transfer of that comparison to Venus is an assumption that the record must name.
It cannot support an absolute quantity.
The research for this article recorded no delta-v for either planet,
and the ratios above are enough to show that a budget for Eve is not a budget for Venus.

**Warnings and uncertainty.**
After NASA's requirements M&S 26, M&S 32 and M&S 33,
any result carried from Eve to Venus needs a placard in three parts.
The kind of limit exceeded is use outside any domain of validation.
The ratios give the extent,
such as an escape velocity 0.466 of the real one and a surface gravity 1.88 times the real one.
The consequence is that no quantity transfers without a separate argument.
On uncertainty the honest entry is the third of the standard's options,
a clear statement that no estimate is available.

**Closing judgement.**
After the standard's recommendation of concluding remarks,
the record ends with a sentence that a reader can act on.
The flight to Eve is credible as a rehearsal of the form and sequence of a mission to Venus.
It is not credible as a source of numbers for one.

### What Such a Comparison Supports

The worked example shows the form at its smallest.
It also shows what the form can and cannot do.

A comparison of this kind can show which results depend on the stand-in.
A reader who sees the ratios knows at once that a mass,
a velocity
or a duration came from a smaller system.
It can separate what a stand-in preserves from what it distorts,
as the proportions of the orbits are separate from the properties of the planet.
And it can make the user state a purpose before stating a result,
which is the step on which the defence standard,
the NASA standard
and the analogue report all insist.

A comparison of this kind cannot validate the stand-in.
A table of ratios compares inputs.
Validation compares results with a referent,
and nothing in the table does that.
It cannot convert a result,
since no single scale factor links the two columns.
And it cannot be complete.
The table lists the quantities that two sources happened to record,
and a real section would begin from the quantities that govern the question,
as the similitude paper begins from the parameters that govern the motion.
A user who needs a number for the real mission has to obtain it from a model validated for that purpose.
The stand-in can tell that user which number to ask for.

## What the Standards Share

The regimes differ in vocabulary and agree in structure.
Fourteen elements recur,
and each appears in at least two of the documents read.
The list is the author's synthesis,
and each item names the sources behind it.

1. **Divide the work into phases and place a gate at the end of each.**
   NASA's project management directive has seven phases opened by lettered key decision points.
   The ECSS project planning standard has seven phases closed by reviews.
2. **Give the decision to a named authority that is not the review team.**
   At NASA the Decision Authority determines readiness to proceed.
   In the ECSS standards the review authority reports and the customer decides.
3. **Write the criteria of a review before holding it.**
   NASA requires the technical team to take part in developing entrance and success criteria,
   and its glossary places the success criteria in the review plan.
   The ECSS review standard requires a procedure that defines prerequisites,
   objectives
   and success criteria.
   The defence standard puts acceptability criteria in the accreditation plan.
4. **Describe the mission as scenarios in order of time, nominal and off-nominal.**
   The outline in NASA's handbook,
   the reference missions of the Commercial Crew Program,
   the ECSS mission description document
   and the ECSS mission analysis all ask for both.
5. **State objectives and success in terms that someone can measure.**
   NASA asks for objective,
   quantifiable
   and verifiable terms.
   The ECSS standard on requirements asks for quantifiable terms,
   a verification method
   and a tolerance.
6. **Write the assumptions down, number them and give each a reason.**
   The Mars reference architecture numbers and types its ground rules and assumptions.
   NASA's templates ask for the driving ground rules and assumptions of the mission design.
   The NASA standard for models and simulations requires a record of assumptions with rationales and consequences.
7. **Tabulate the budget by manoeuvre, with the basis of each number, and keep the margin in view.**
   The lunar orbiter's table,
   the Jupiter report's two tables
   and the Goddard rule all do so,
   by different conventions.
8. **Take the foreseeable decisions in advance and write the reason beside each.**
   The Shuttle flight rules pair every rule with a rationale.
   The ECSS mission operations plan holds mission rules,
   launch hold criteria
   and mission termination criteria.
9. **Validate the procedures before flight and record the status of each.**
   The ECSS operations standard requires a matrix of procedures with their validation status,
   and its operational readiness review confirms the validation of all procedures.
   NASA's recommended criteria for the Operational Readiness Review ask that the project write,
   verify
   and approve its operations documentation.
10. **Certify readiness by signature, and give dissent a place.**
    NASA's launch service directive lists the signatories of the certificate.
    The Commercial Crew plan polls its board,
    records exceptions
    and puts discussion of formal dissents on the agenda.
    The NASA standard for models and simulations recommends that a report include dissenting technical opinions.
11. **Report against the plan.**
    The Apollo and Shuttle reports set planned or predicted values beside actual ones.
    The GOCE end-of-mission report states each departure from the plan with its cause.
    NASA's recommended criterion for the Post-Launch Assessment Review asks that observed performance agree with prediction
    or that the project understand the difference.
12. **Judge each objective and explain each shortfall.**
    The Apollo report marks each objective as met or partly met and gives a subsection to each shortfall.
    The Shuttle report gives each experiment a percentage and a reason.
13. **Record each anomaly through to its closure.**
    The Apollo report closes each anomaly with a status line.
    The Shuttle report tracks each in a numbered table.
    The ECSS operations standard prescribes the contents of an operations anomaly report.
14. **Say what a stand-in is for, how it differs and what follows.**
    The NASA standard requires records of intended use,
    assumptions,
    limits
    and permissible uses,
    and a warning outside them.
    The defence standard requires assumptions,
    capabilities,
    limitations,
    and risks with their impacts.
    The analogue assessment report writes down the target before it rates the analogue.
    The similitude paper derives the limits of test data from the conditions left unmet.

The regimes differ on points that a designer of documents must decide.

| Point | NASA | European standards |
|---|---|---|
| Who decides a phase transition | The Decision Authority, an Associate Administrator chosen by the category of the project | The customer, on the outcome of the review |
| Force of the review criteria | Recommended practice in an appendix, tailored into the review plan | Objectives described in the standard, with criteria set in the procedure of each review |
| Success | Mission success criteria, with a minimum whose loss triggers consideration of a Termination Review | Compliance with requirements. No mission success criteria defined |
| Concept of operations | A defined term, with an annotated outline in guidance | No document of that name. The content lies in two documents with required contents |
| Margin on delta-v | A row of its own in one example, and a statistical requirement on propellant in a Center standard | A percentage by kind of manoeuvre in one document, and almost none in another |
| The decision to launch | A certificate with named signatories, and a poll | An authorisation to proceed for launch, with no signatory named in the passages read |
| The report after flight | No required outline. The Final Mission Report is best practice | Reports required by name, with contents prescribed for the anomaly report alone |

Four of these differences are real choices for a small programme.
The first is whether the programme fixes its review criteria in advance for every mission or writes them for each.
Both regimes,
in the end,
write them for each.
The second is whether success has a floor that differs from the full set of requirements.
NASA's floor has a consequence,
and a floor without one is decoration.
The third is where the margin sits,
since nobody can compare a budget that hides its margin with one that shows it.
The fourth is whether a readiness poll decides or advises.
NASA uses both kinds,
on the author's reading of its documents.

## Structures for a Small Programme

A small programme,
such as a campaign of simulated flights,
has no Decision Authority and no review board.
It can still keep the structure of the documents,
because the structure costs little
and because the standards themselves expect tailoring.
The three structures below are the author's consolidation.
Each part names the document it comes from,
and anything that comes from no document read here says so.

### The Mission Plan

| Part | Content | After |
|---|---|---|
| Identification | A unique number and revision, a title, the date, the author, the status, and the stand-in in which the mission will fly | ECSS operations procedure for the title, version and author. The date, the status and the entry for the stand-in are the author's additions |
| Purpose and objectives | Why the mission exists, and its objectives in ranks | NASA Project Plan, Commercial Crew reference missions |
| Success criteria | For each objective a criterion in quantified and verifiable terms, and the minimum criteria whose failure triggers consideration of ending the mission | NASA Program Plan and Project Plan, ECSS requirements standard |
| Ground rules and assumptions | Each with a number, a type that says whether it is fixed or open to trade, and a rationale | Mars reference architecture, NASA handbook outline |
| Mission description | The system element by element, and the mission phase by phase with its main events and constraints | ECSS mission description document, NASA handbook outline |
| Scenarios | The nominal timeline as labelled scenarios, and the off-nominal branches with the point at which the mission ends early | NASA handbook outline, Commercial Crew reference missions |
| Mission analysis and budget | A table by manoeuvre in order of flight, with delta-v, propellant, the basis of each number, the margin as a row of its own, and a statement of the margin convention | Lunar orbiter paper, ECSS mission analysis report, Goddard rule. The statement of the margin convention is the author's addition |
| Mission rules | Numbered rules, each with its rationale, covering the criteria to commit to launch, the limits in flight, the criteria to end the mission, and who decides beyond the rules | Shuttle flight rules, ECSS mission operations plan |
| Timeline and procedures | The planned start of each activity and the position responsible, and the procedures by reference with the validation status of each | ECSS mission operations plan and operations procedure |
| Readiness | The entrance and success criteria of the readiness review, who answers the poll, whether the poll decides or advises, and who signs | NASA systems engineering directive, launch service directive, Commercial Crew plan |
| Risks | The risks and the open issues | NASA handbook outline, ECSS mission description document |
| Planned reporting | What the mission will measure for its report and where the data will go | NASA Project Plan |
| Differences from the real environment | The section described below, written before flight | NASA standard for models and simulations, defence standard. Its place inside the plan is the author's addition |

Four rules of use go with the table.

- **The plan fixes the criteria before flight.**
  A change to an objective,
  a criterion
  or a rule after approval goes into a change log,
  after the NASA Project Plan.
- **Every rule has a rationale.**
  Nobody can judge a rule without one when circumstances change,
  after the Shuttle flight rules.
- **A waiver is a record.**
  The plan logs each requirement that the mission will knowingly not meet,
  after the NASA Project Plan.
- **An empty part stays in.**
  A part that does not apply keeps its heading and says so,
  after the defence standard.

### The Mission Report

| Part | Content | After |
|---|---|---|
| Identification | A unique number, the mission, the dates, the time references used, the author and the status | Shuttle mission report |
| Summary | What the mission set out to do, what it did, and the verdict on its primary objective | Apollo mission report, NASA Final Mission Report |
| Sequence of events | The events as flown, with actual times | Apollo and Shuttle mission reports |
| Planned against actual | For each budgeted quantity the planned value, the actual value, the difference, the tolerance where one exists, and the explanation of any difference that matters | Apollo and Shuttle mission reports, ESA end-of-mission report |
| Performance | The vehicle and the ground by subsystem, with departures from prediction | Apollo and Shuttle mission reports, NASA Post-Launch Assessment Review |
| Assessment of objectives | Each objective restated, a verdict of met, partly met or not met, the reason for each shortfall and what will happen to it, and the verdict on the minimum success criteria | Apollo and Shuttle mission reports, NASA Post-Flight Assessment Review. The verdict on the minimum success criteria is the author's addition |
| Rules, waivers and decisions | The rules invoked, the rules waived, and each decision taken outside the rules, with who took it | Shuttle flight rules, Commercial Crew plan. The part is the author's addition |
| Anomalies | For each a number, a title, the time, the observation, the cause or its absence, the action and the status | Apollo and Shuttle mission reports, ECSS operations anomaly report |
| Effects of the stand-in | Which results depend on the stand-in, with the warnings that the differences section requires | NASA standard for models and simulations. The part is the author's addition |
| Conclusions and recommendations | Numbered findings, and recommendations for later missions | Apollo mission report, NASA Post-Flight Assessment Review |
| Lessons learned | What a later mission should do differently | NASA directive, ECSS operations standard |
| Records | Where the data and the supporting records are | Apollo mission report, NASA Post-Flight Assessment Review |

Four rules of use go with this table too.

- **The report restates the plan before judging against it.**
  It copies each objective and criterion from the plan,
  so that a reader needs no second document.
- **A comparison has both numbers and the same units.**
  It gives the planned value,
  the actual value
  and the difference,
  after the consumables and performance tables of the two NASA reports.
- **A verdict has more than two values and a shortfall has a reason.**
  The Apollo report used Yes and Partial,
  and the Shuttle report used percentages.
- **An anomaly stays open until someone closes it.**
  The report gives the status of each,
  after the closing line of the Apollo entries.

### The Section on Differences From the Real Environment

This section belongs to every mission that flies in a stand-in.
The plan carries it before the flight
and the report updates it afterwards.

| Part | Content | After |
|---|---|---|
| Intended use | The question that the flight answers, the decisions that rest on the answer, and the consequences of a wrong answer | Defence standard, NASA standard |
| The target | The real environment as assumed, characteristic by characteristic, written before the comparison | Analogue assessment report |
| Governing parameters | One row for each parameter that governs the question, with the real value, the stand-in value, the ratio and the source of each value | Similitude paper, analogue assessment report. The labelling of community sources is the author's addition |
| Assumptions and abstractions | Each departure from the real environment, with its rationale and its consequence for the intended use | NASA standard, defence standard |
| Capabilities | What the stand-in does reproduce | Defence standard |
| Limits and what nobody validated | The bounds of the stand-in, the basis of any comparison with a referent, and the aspects that nobody validated | NASA standard, defence standard |
| What the results support | Each kind of result marked as qualitative, incremental or absolute, with the permissible uses | NASA Glenn overview, NASA standard. The application to stand-ins in general is the author's |
| Warnings and uncertainty | For any result used beyond the above, the kind of limit exceeded, the extent and the consequences, and an estimate of uncertainty or a statement that none exists | NASA standard |
| Risks and impacts | What follows for a reader who uses the mission as a model of a real one | Defence standard |
| Closing judgement | Whether the results are credible enough for the actual use, and any dissent | NASA standard |

Five rules of use go with it.

- **Purpose comes first.**
  The same stand-in can be adequate for one question and useless for another,
  after the analogue assessment report's example of the island with constant daylight.
- **A ratio is not a conversion factor.**
  The table of parameters shows how far the stand-in lies from the target.
  It does not turn a result from one into a result for the other.
  This rule is the author's.
- **No single score.**
  The section describes each difference and does not sum them,
  after the NASA standard's advice against combining its factors.
- **The section may not stay silent on uncertainty.**
  Where no estimate exists the section says so in words,
  after the NASA standard.
- **Every number names its world.**
  A value measured in the stand-in carries the stand-in's name wherever it appears,
  in the report as in the plan.
  This rule is the author's.

The three structures share one habit,
which is the habit of the documents they come from.
Each writes down before the flight the terms on which a reader will judge the flight.

## Epistemic State

**Facts and their sources.**
The requirements and outlines described above come from the documents themselves.
The author saved a copy of each,
confirmed its number,
issue
and date from its own cover or header,
and matched each quotation against the saved text.
The exceptions follow.

- **Documents transcribed by hand.**
  The ECSS glossary forbids copying,
  and the author transcribed its definition of a mission statement from a page image.
  The Delft thesis forbids copying,
  and the sentence quoted from it,
  with the paraphrase of the fidelity definition,
  rests on a transcription by hand.
  Figure 2-5 of the NASA project management directive is an image.
  The author read the order of the reviews and the pairing of phases with key decision points from it by eye,
  and confirmed the phase names against the running text of the management handbook.
  The figure in the highway handbook that holds the two outlines for a concept of operations is an image,
  and the lists are a transcription.
- **Scanned documents.**
  The Apollo 11 report,
  the Lunar Reconnaissance Orbiter paper,
  the STS-81 report
  and the similitude paper are scans with a text layer from optical character recognition.
  The quotations from them match that layer.
  The author read the header and most rows of the lunar orbiter's budget from the page image,
  and four of its rows match the text layer.
  The author read the headers of the two Apollo tables from page images.
- **Documents marked For Official Use.**
  Five ESA files carry that marking on every page although the agency serves them from public addresses.
  They are the margin philosophy,
  the delta-v guideline,
  the Jupiter mission analysis report,
  the GOCE end-of-mission report
  and the debris mitigation standard.
  The article describes their structure and quotes them briefly.
  The GOCE report came from an archive copy of an ESA page.
- **Standards not read.**
  The author did not read ISO 24113,
  ISO/IEC/IEEE 29148,
  IEEE 1362
  or either guide of the American Institute of Aeronautics and Astronautics,
  all of which their publishers sell.
  The statements about them rest on catalogue pages,
  on a registry record,
  on the highway handbook
  and on a NASA page that reproduces definitions.
  The author did not obtain the report of the study group on fidelity,
  and its definition rests on the excerpt in the thesis.
- **Documents not obtained.**
  The author did not obtain the Shuttle launch commit criteria,
  the Shuttle programme's document on certification of flight readiness,
  the flight rules of the International Space Station,
  a public set of programme requirements with minimum success criteria,
  a NASA flight plan or book of procedures,
  the mission analysis guidelines that the Jupiter report cites,
  or a public ESA report on a launch and early orbit phase or a commissioning.
- **Sources read in part.**
  The author read the survey of terrestrial analogues and the paper that proposes the game as a platform in their abstracts only,
  and the study of the game as a research environment as a preprint.
- **A mirror.**
  The author read the defence standard from a mirror site and did not confirm that Change 1 is its current state.
- **A community source.**
  The values for Eve and Kerbin come from a wiki that players edit.
  The author did not check them against the game.
  Several values in the wiki's summary boxes,
  such as mass and escape velocity,
  appear to come from the wiki's own calculations and need not be constants of the game.
  The author did not examine the note that the wiki attaches to Eve's orbital values.
- **Tables.**
  The tables condense their sources and are not quotations.
  The summaries of NASA's table of requirement levels,
  of the Project Plan template,
  of the risk class considerations
  and of the Goddard margin table come from saved text whose column layout defeats a check word by word.
- **Dates on covers.**
  The lunar orbiter paper prints February 2006 beside a paper number of the 2007 series,
  and the article cites it by that number.
  The management handbook prints May 2022 on its cover,
  and the saved file is a later revision that the cover does not announce.
  The saved file of the Systems Engineering Handbook has no dated cover.
- **Editions.**
  The Shuttle flight rules are the edition of 2002 and not the last.
  The Jupiter report is the latest report text found and not the latest analysis.

**Dates.**
The author read the documents in November 2026,
and several are in motion.
NASA's interim directive on project management printed an expiration date of 9 December 2025,
and its status after that date is unknown to the author.
The directive that it restates prints an expiration date of 3 February 2027.
The catalogue shows ISO/IEC/IEEE 29148 under revision.
The NASA handbook for models and simulations carries a draft header under an approved cover.
The agency pages on analogue missions change,
and the list of analogues is that of the page as retrieved.
A reader who relies on a particular clause should check the current issue.

**Inferences.**
The following are inferences,
and the text names each as one where it appears.

- That a NASA review informs the decision at a key decision point and does not take it.
- That Appendix G of the systems engineering directive is guidance,
  and that the binding criteria of a review are those of its review plan.
- That an ECSS review takes its exact criteria from its procedure,
  and that the review authority and the customer divide the decision between them.
- That the two NASA documents on the concept of operations correspond to the two ECSS documents,
  and the other pairings of the vocabulary table.
- That Level 1 requirements is working vocabulary for a programme's requirements on a project.
- That success in the European example means compliance with the numbered requirements.
- That the second outline in the highway handbook descends from IEEE 1362.
- The form of a reference mission,
  of an Apollo anomaly entry
  and of a Shuttle anomaly entry,
  each drawn from the entries read.
- That the Jupiter report treats margin as a computed cost of navigation,
  and the list of five conventions for margin.
- That launch hold criteria answer to launch commit criteria and mission rules to flight rules.
- That the launch poll requires unanimity while the board's poll advises a chair.
- That the weights of the analogue assessment report rank analogues against one another and measure no absolute distance.
- That public agency pages describe the similarities of an analogue and leave its limits to the technical literature.
  The evidence is a handful of pages.
- That the catalogue's mark of a non-mandatory standard means that the models and simulations standard binds only where something invokes it.
- That the defence standard's heading of four parts is the nearest published template for a section on differences.
- That the negative rotation period of Venus denotes retrograde rotation.
- That the four bodies of practice on stand-ins overlap on use,
  assumptions
  and limits.
- Every consequence drawn from the ratios of Venus and Eve,
  and the placement of that stand-in on the validation scale.

**Unresolved.**
The launch service directive gives two timings for its Flight Readiness Review in one clause,
and the management handbook gives a third.
The author did not resolve the difference.

**The author's view.**
The list of fourteen shared elements,
the table of differences,
the three structures for a small programme,
the parts and rules marked as additions,
and the worked comparison of Venus and Eve are the author's.
The comparison illustrates a form and validates nothing.
The author offers all of them as a reading of the documents,
open to disagreement on the evidence.
None of them is a requirement of any standard.

## Out of Scope

- **Other agencies.**
  The article covers NASA,
  the ECSS standards
  and documents of ESA.
  It does not cover the agencies of Russia,
  China,
  India
  or Japan.
- **Cost and schedule.**
  The baselines,
  the confidence levels
  and the earned value of a project receive no treatment.
- **Safety and mission assurance.**
  Hazard analyses,
  range safety,
  human rating
  and planetary protection have their own documents,
  and the article names them only where a plan points to them.
- **Investigation.**
  The article describes how a mission report records an anomaly.
  It does not describe how an agency investigates a mishap.
- **Commercial licensing.**
  The documents that a regulator requires of a commercial launch operator are a separate subject.
- **Orbital mechanics.**
  The article shows how the documents tabulate a budget and derives none.
- **Validation of any simulator.**
  The article compares the recorded properties of two planets.
  It tests no simulator against any referent.

## Conclusion

Agencies write a space mission down before,
during
and after its flight,
and the documents of NASA and of the European standards agree on the shape of each account.
Before flight a plan states the objectives,
the criteria of success,
the assumptions,
the scenarios
and the budget,
and a review with written criteria precedes each commitment.
During flight a plan of operations,
a set of rules with their reasons
and a body of validated procedures govern what the operators do,
and someone named in advance decides whatever the rules do not cover.
After flight a report sets the actual against the planned,
judges each objective,
and follows each anomaly to its closure.

The regimes differ in ways that matter to anyone who models documents on them.
NASA defines a concept of operations and a floor of minimum success,
and it leaves its review criteria as recommended practice.
The European standards prescribe the contents of more documents
and define neither a concept of operations by that name nor mission success criteria.
The examples differ on where a budget keeps its margin,
and the documents on whether a poll decides or advises.

When the mission flies in a stand-in,
a fourth account is due.
The practices read here overlap on its contents,
in the author's reading.
It states the purpose first.
It lists what the stand-in assumes and where it stops.
It says what the results may support,
and it warns in terms when a result leaves that ground.
A table of ratios between the stand-in and the real environment is the beginning of that account and not its end,
since a ratio shows a difference and validates nothing.
A small programme can adopt all four accounts at little cost,
provided it writes each before the flight that will test it.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 6 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 6, 5 are established and 1 are bespoke.
The mass equations take masses in one unit throughout and give the margin in percent. The propellant equation takes delta-v and exhaust velocity in the same unit of velocity. The Froude number and the stand-in ratio are dimensionless, and the ratio requires both values in the same unit.

**Equation 1, Predicted Mass.**
The predicted mass of a flight system is its basic mass plus the mass growth allowance.
[NASA 2025b][agency_nasa_gsfc_std_1000i]

$$
M_{\mathrm{P}} = M_{\mathrm{B}} + M_{\mathrm{G}}
\tag{1}
$$

**Equation 2, Mass Margin as a Percentage of Basic Mass.**
The mass margin is the allowable mass less the predicted mass, stated as a percentage of the basic mass.
[NASA 2025b][agency_nasa_gsfc_std_1000i]

$$
m = \frac{M_{\mathrm{A}} - M_{\mathrm{P}}}{M_{\mathrm{B}}} \times 100
\tag{2}
$$

**Equation 3, Propellant for the End of Life Manoeuvres.**
The propellant that the end of life manoeuvres consume, given the mass that remains after them and the ratio of their delta-v to the exhaust velocity.
[ESA 2019][esa_delta_v_guidelines_2019]

$$
P_{\mathrm{EOL}} = \left( m_{\mathrm{dry}} + P_{\mathrm{RES}} + P_{\mathrm{UNC}} \right) \left( e^{\Delta V_{\mathrm{EOL}} / V_{\mathrm{e}}} - 1 \right)
\tag{3}
$$

**Equation 4, Exhaust Velocity.**
The exhaust velocity as the product of the average specific impulse, the thruster efficiency and the standard gravitational acceleration.
[ESA 2019][esa_delta_v_guidelines_2019]

$$
V_{\mathrm{e}} = I_{\mathrm{sp}} \, \eta \, g_{0}
\tag{4}
$$

**Equation 5, Froude Number.**
The dimensionless group that a model and a full-scale vehicle must share for inertial and gravitational effects to be similar.
[Wolowicz et al. 1979][agency_nasa_tp_1435]

$$
N_{\mathrm{Fr}} = \frac{V^{2}}{l g}
\tag{5}
$$

*Equation 6, Bespoke Ratio of a Stand-In Quantity to the Real Quantity.*
The article states each difference between a stand-in and the real system as the value of a quantity in the stand-in divided by its value in the real system.

$$
k = \frac{q_{\mathrm{S}}}{q_{\mathrm{R}}}
\tag{6}
$$

### Notation

- $M_{\mathrm{P}}$, the predicted mass
- $M_{\mathrm{B}}$, the basic mass
- $M_{\mathrm{G}}$, the mass growth allowance
- $M_{\mathrm{A}}$, the allowable mass
- $m$, the mass margin in percent
- $P_{\mathrm{EOL}}$, the propellant for the end of life manoeuvres
- $m_{\mathrm{dry}}$, the dry mass of the satellite
- $P_{\mathrm{RES}}$, the propellant residuals
- $P_{\mathrm{UNC}}$, the allowance for gauging uncertainty
- $\Delta V_{\mathrm{EOL}}$, the delta-v of the end of life manoeuvres
- $V_{\mathrm{e}}$, the exhaust velocity
- $I_{\mathrm{sp}}$, the average specific impulse
- $\eta$, the thruster efficiency
- $g_{0}$, the standard gravitational acceleration
- $N_{\mathrm{Fr}}$, the Froude number
- $V$, the velocity
- $l$, the characteristic dimension
- $g$, the acceleration of gravity
- $k$, the ratio of a quantity in the stand-in to the same quantity in the real system
- $q_{\mathrm{S}}$, the value of a quantity in the stand-in
- $q_{\mathrm{R}}$, the value of the same quantity in the real system

## References

- [Reference, AIAA 2018, ANSI/AIAA G-043B-2018, Guide to the Preparation of Operational Concept Documents][ref_aiaa_g_043b_2018]
- [Reference, Beckman 2007, Mission Design for the Lunar Reconnaissance Orbiter, AAS 07-057][agency_nasa_lro_mission_design]
- [Reference, DoD 2012, MIL-STD-3022 with Change 1, Documentation of Verification, Validation, and Accreditation (VV&A) for Models and Simulations][mil_std_3022]
- [Reference, Drake 2009a, NASA/SP-2009-566, Human Exploration of Mars Design Reference Architecture 5.0][agency_nasa_dra5_2009]
- [Reference, Drake 2009b, NASA/SP-2009-566-ADD, Human Exploration of Mars Design Reference Architecture 5.0 Addendum][agency_nasa_dra5_addendum_2009]
- [Reference, ECSS 2008a, ECSS-E-ST-70C, Space Engineering, Ground Systems and Operations][ecss_e_st_70c]
- [Reference, ECSS 2008b, ECSS-M-ST-10-01C, Space Management, Organization and Conduct of Reviews][ecss_m_st_10_01c]
- [Reference, ECSS 2009a, ECSS-M-ST-10C Rev. 1, Space Project Management, Project Planning and Implementation][ecss_m_st_10c_rev1]
- [Reference, ECSS 2009b, ECSS-E-ST-10-06C, Space Engineering, Technical Requirements Specification][ecss_e_st_10_06c]
- [Reference, ECSS 2017, ECSS-E-ST-10C Rev.1, Space Engineering, System Engineering General Requirements][ecss_e_st_10c_rev1]
- [Reference, ECSS 2023, ECSS-S-ST-00-01C Rev.1, ECSS System, Glossary of Terms][ecss_s_st_00_01c_rev1]
- [Reference, ECSS 2024, ECSS-U-AS-10C Rev.2, Space Sustainability, Adoption Notice of ISO 24113, Space Systems, Space Debris Mitigation Requirements][ecss_u_as_10c_rev2]
- [Reference, ECSS Active Standards][ecss_active_standards]
- [Reference, ESA 2005, Venus Express Status Report No. 3, End of LEOP Activities][esa_venus_express_status_3]
- [Reference, ESA 2012, SRE-PA/2011.097/ Issue 1 Revision 3, Margin Philosophy for Science Assessment Studies][esa_margin_philosophy_2012]
- [Reference, ESA 2014, GO-RP-ESC-FS-6268 Issue 1, GOCE End-of-Mission Operations Report][esa_goce_end_of_mission_2014]
- [Reference, ESA 2017, JUI-ESOC-MOC-RP-001 Issue 3 Revision 2, JUICE Consolidated Report on Mission Analysis][esa_juice_crema_2017]
- [Reference, ESA 2019, Guidelines for the Computation of Delta-V and Propellant Budget, Issue 1][esa_delta_v_guidelines_2019]
- [Reference, ESA 2020, EOP-SM/3088/YM-ym Issue 3.0, Copernicus CO2 Monitoring Mission Requirements Document][esa_co2m_mrd_2020]
- [Reference, ESA 2023a, ESSB-ST-U-007 Issue 1, ESA Space Debris Mitigation Requirements][esa_essb_st_u_007]
- [Reference, ESA 2023b, ESA/ADMIN/IPOL(2023)1, ESA Space Debris Mitigation Policy][esa_admin_ipol_2023_1]
- [Reference, ESA CAVES, What is CAVES?][esa_what_is_caves]
- [Reference, FHWA Systems Engineering for ITS, Section 6.4, Concept of Operations Template][ref_fhwa_conops_template]
- [Reference, IEEE 1998, IEEE 1362-1998, IEEE Guide for Information Technology, System Definition, Concept of Operations (ConOps) Document, Catalogue Page][ref_ieee_1362_1998]
- [Reference, ISO 2018, ISO/IEC/IEEE 29148:2018, Systems and Software Engineering, Life Cycle Processes, Requirements Engineering, Catalogue Page][ref_iso_29148_2018]
- [Reference, Keeton et al. 2011, NASA/TP-2011-216146, Analog Assessment Tool Report][agency_nasa_analog_assessment_tool]
- [Reference, Kerbal Space Program Wiki 2026a, Eve, Revision 110701][ref_ksp_wiki_eve]
- [Reference, Kerbal Space Program Wiki 2026b, Kerbin, Revision 111119][ref_ksp_wiki_kerbin]
- [Reference, NASA 1969, MSC-00171, Apollo 11 Mission Report][agency_nasa_apollo_11_mission_report]
- [Reference, NASA 1997, NSTS-37412, STS-81 Space Shuttle Mission Report][agency_nasa_sts_81_mission_report]
- [Reference, NASA 2002, NSTS-12820, Space Shuttle Operational Flight Rules, Volume A, All Flights][agency_nasa_nsts_12820_vol_a]
- [Reference, NASA 2011, NF-2011-04-534-HQ, Analog Missions and Field Tests][agency_nasa_analog_fact_sheet_2011]
- [Reference, NASA 2015, CCT-DRM-1110, Crew Transportation System Design Reference Missions][agency_nasa_cct_drm_1110]
- [Reference, NASA 2016, NASA/SP-2016-6105 Rev2, NASA Systems Engineering Handbook][agency_nasa_se_handbook_2016]
- [Reference, NASA 2017, NPR 8705.2C with Change 2, Human-Rating Requirements for Space Systems][agency_nasa_npr_8705_2c]
- [Reference, NASA 2019a, NPD 7120.6A with Change 1, Knowledge Policy for Programs and Projects][agency_nasa_npd_7120_6a]
- [Reference, NASA 2019b, Human Exploration Research Analog (HERA) Facility and Capabilities Information][agency_nasa_hera_2019]
- [Reference, NASA 2022a, NASA/SP-20220009501, NASA Space Flight Program and Project Management Handbook][agency_nasa_pm_handbook_2022]
- [Reference, NASA 2022b, CCT-PLN-2100 Revision B, Crew Transportation System Certification of Flight Readiness Plan][agency_nasa_cct_pln_2100]
- [Reference, NASA 2024a, NPR 7120.5F with Change 4, NASA Space Flight Program and Project Management Requirements][agency_nasa_npr_7120_5f]
- [Reference, NASA 2024b, NID 7120.148, NASA Space Flight Program and Project Management Requirements][agency_nasa_nid_7120_148]
- [Reference, NASA 2024c, NPR 7123.1D with Change 2, NASA Systems Engineering Processes and Requirements][agency_nasa_npr_7123_1d]
- [Reference, NASA 2024d, NPR 8705.4B, Risk Classification for NASA Payloads][agency_nasa_npr_8705_4b]
- [Reference, NASA 2024e, NASA-STD-7009B, Standard for Models and Simulations][agency_nasa_std_7009b]
- [Reference, NASA 2025a, NPD 8610.24C with Change 3, Launch Services Program Pre-Launch Readiness Reviews][agency_nasa_npd_8610_24c]
- [Reference, NASA 2025b, GSFC-STD-1000I, Rules for the Design, Development, Verification, and Operation of Flight Systems][agency_nasa_gsfc_std_1000i]
- [Reference, NASA 2026a, Analog Missions][agency_nasa_analog_missions_page]
- [Reference, NASA 2026b, CHAPEA][agency_nasa_chapea_page]
- [Reference, NASA 2026c, NASA-HDBK-7009B, NASA Handbook for Models and Simulations, An Implementation Guide for NASA-STD-7009B][agency_nasa_hdbk_7009b]
- [Reference, NASA Glenn 2021a, Glossary of Verification and Validation Terms][agency_nasa_nparc_glossary]
- [Reference, NASA Glenn 2021b, Overview of CFD Verification and Validation][agency_nasa_nparc_overview]
- [Reference, Preston et al. 2012, The Catalogue of Planetary Analogues][esa_catalogue_planetary_analogues]
- [Reference, Reagan et al. 2012, NASA's Analog Missions, Driving Exploration Through Innovative Testing, AIAA 2012-5238][agency_nasa_reagan_2012]
- [Reference, Roza 2005, Simulation Fidelity Theory and Practice, Doctoral Thesis, Delft University of Technology][ref_roza_2005]
- [Reference, Williams 2024a, Venus Fact Sheet][agency_nasa_venus_fact_sheet]
- [Reference, Williams 2024b, Earth Fact Sheet][agency_nasa_earth_fact_sheet]
- [Reference, Wolowicz et al. 1979, NASA Technical Paper 1435, Similitude Requirements and Scaling Relationships as Applied to Model Testing][agency_nasa_tp_1435]
- [Research, Carrasco et al. 2025, Large Language Models as Autonomous Spacecraft Operators in Kerbal Space Program, Preprint][research_carrasco_2025]
- [Research, Cromwell et al. 2021, Earth-Based Research Analogs to Investigate Space-Based Health Risks][research_cromwell_2021]
- [Research, Kawthalkar et al. 2022, Modeling and Simulation of a Direct-Ascent Anti-Satellite Missile Using Kerbal Space Program (KSP)][research_kawthalkar_2022]
- [Research, Preston and Dartnell 2014, Planetary Habitability, Lessons Learned from Terrestrial Analogues][research_preston_dartnell_2014]
- [Research, Rahill et al. 2025, Increasing Fidelity in Lunar and Martian Analogs for Behavioral Health and Performance Research][research_rahill_2025]

[agency_nasa_analog_assessment_tool]: https://www.nasa.gov/wp-content/uploads/2016/04/analog_assessment_tools.pdf
[agency_nasa_analog_fact_sheet_2011]: https://www.nasa.gov/wp-content/uploads/2015/06/541196main_analogfactsheet.pdf
[agency_nasa_analog_missions_page]: https://www.nasa.gov/analog-missions/
[agency_nasa_apollo_11_mission_report]: https://ntrs.nasa.gov/citations/19700008096
[agency_nasa_cct_drm_1110]: https://ntrs.nasa.gov/citations/20150018900
[agency_nasa_cct_pln_2100]: https://ntrs.nasa.gov/citations/20220005043
[agency_nasa_chapea_page]: https://www.nasa.gov/humans-in-space/chapea/
[agency_nasa_dra5_2009]: https://www.nasa.gov/wp-content/uploads/2015/09/373665main_nasa-sp-2009-566.pdf
[agency_nasa_dra5_addendum_2009]: https://www.nasa.gov/wp-content/uploads/2015/09/373667main_nasa-sp-2009-566-add.pdf
[agency_nasa_earth_fact_sheet]: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
[agency_nasa_gsfc_std_1000i]: https://standards.nasa.gov/standard/GSFC/GSFC-STD-1000
[agency_nasa_hdbk_7009b]: https://standards.nasa.gov/standard/NASA/NASA-HDBK-7009
[agency_nasa_hera_2019]: https://www.nasa.gov/wp-content/uploads/2016/05/2019_hera_facility_capabilities_information.pdf
[agency_nasa_lro_mission_design]: https://ntrs.nasa.gov/citations/20070021535
[agency_nasa_nid_7120_148]: https://nodis3.gsfc.nasa.gov/OPD_Docs/NID_7120_148_.pdf
[agency_nasa_nparc_glossary]: https://www.grc.nasa.gov/www/wind/valid/tutorial/glossary.html
[agency_nasa_nparc_overview]: https://www.grc.nasa.gov/www/wind/valid/tutorial/overview.html
[agency_nasa_npd_7120_6a]: https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=7120&s=6A
[agency_nasa_npd_8610_24c]: https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=8610&s=24C
[agency_nasa_npr_7120_5f]: https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F
[agency_nasa_npr_7123_1d]: https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1D
[agency_nasa_npr_8705_2c]: https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=2C
[agency_nasa_npr_8705_4b]: https://nodis3.gsfc.nasa.gov/npg_img/N_PR_8705_004B_/N_PR_8705_004B_.pdf
[agency_nasa_nsts_12820_vol_a]: https://web.archive.org/web/20030917144124id_/http://www.jsc.nasa.gov:80/news/columbia/fr_generic.pdf
[agency_nasa_pm_handbook_2022]: https://ntrs.nasa.gov/citations/20220009501
[agency_nasa_reagan_2012]: https://www.nasa.gov/wp-content/uploads/2016/04/nasa_analog_missions_2012.pdf
[agency_nasa_se_handbook_2016]: https://ntrs.nasa.gov/citations/20170001761
[agency_nasa_std_7009b]: https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf
[agency_nasa_sts_81_mission_report]: https://ntrs.nasa.gov/citations/19970016099
[agency_nasa_tp_1435]: https://ntrs.nasa.gov/citations/19790022005
[agency_nasa_venus_fact_sheet]: https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html
[ecss_active_standards]: https://ecss.nl/standards/active-standards/
[ecss_e_st_10_06c]: https://ecss.nl/wp-content/uploads/standards/ecss-e/ECSS-E-ST-10-06C6March2009.pdf
[ecss_e_st_10c_rev1]: https://ecss.nl/wp-content/uploads/2017/02/ECSS-E-ST-10C-Rev.1(15February2017).pdf
[ecss_e_st_70c]: https://ecss.nl/wp-content/uploads/standards/ecss-e/ECSS-E-ST-70C31July2008.pdf
[ecss_m_st_10_01c]: https://ecss.nl/wp-content/uploads/standards/ecss-m/ECSS-M-ST-10-01C15November2008.pdf
[ecss_m_st_10c_rev1]: https://ecss.nl/wp-content/uploads/standards/ecss-m/ECSS-M-ST-10C_Rev.16March2009.pdf
[ecss_s_st_00_01c_rev1]: https://ecss.nl/wp-content/uploads/2023/10/ECSS-S-ST-00-01C_Rev.1(11October2023).pdf
[ecss_u_as_10c_rev2]: https://ecss.nl/wp-content/uploads/2024/02/ECSS-U-AS-10C-Rev.2-(9February2024).pdf
[esa_admin_ipol_2023_1]: https://technology.esa.int/upload/media/ESA-ADMIN-IPOL-2023-1-Space-Debris-Mitigation-Policy-Final.pdf
[esa_catalogue_planetary_analogues]: https://esamultimedia.esa.int/docs/gsp/The_Catalogue_of_Planetary_Analogues.pdf
[esa_co2m_mrd_2020]: https://esamultimedia.esa.int/docs/EarthObservation/CO2M_MRD_v3.0_20201001_Issued.pdf
[esa_delta_v_guidelines_2019]: https://eopro.esa.int/wp-content/uploads/2020/10/Guidelines-for-DeltaV-and-propellant-budget-computation.pdf
[esa_essb_st_u_007]: https://technology.esa.int/upload/media/DGHKMZ_6542582e18e33.pdf
[esa_goce_end_of_mission_2014]: https://web.archive.org/web/20200223230258/https://earth.esa.int/documents/10174/85857/2014-GOCE-Flight-Control-Team.pdf
[esa_juice_crema_2017]: https://spiftp.esac.esa.int/data/ANCDR/JUICE/man/JUICE_CReMA_Issue_3_Revision_2/JUI-ESOC-MOC-RP-001_i3.2_CReMA.pdf
[esa_margin_philosophy_2012]: https://sci.esa.int/documents/34375/36249/1567260131067-Margin_philosophy_for_science_assessment_studies_1.3.pdf
[esa_venus_express_status_3]: https://sci.esa.int/web/venus-express/-/38270-end-of-leop-activities
[esa_what_is_caves]: https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/CAVES_and_Pangaea/What_is_CAVES
[mil_std_3022]: https://everyspec.com/MIL-STD/MIL-STD-3000-9999/MIL-STD-3022_CHG-1_46836/
[ref_aiaa_g_043b_2018]: https://doi.org/10.2514/4.105487
[ref_fhwa_conops_template]: https://ops.fhwa.dot.gov/seits/sections/section6/6_4.html
[ref_ieee_1362_1998]: https://standards.ieee.org/ieee/1362/2047/
[ref_iso_29148_2018]: https://www.iso.org/standard/72089.html
[ref_ksp_wiki_eve]: https://wiki.kerbalspaceprogram.com/wiki/Eve
[ref_ksp_wiki_kerbin]: https://wiki.kerbalspaceprogram.com/wiki/Kerbin
[ref_roza_2005]: https://repository.tudelft.nl/record/uuid:a5afd816-4b04-459d-b54c-da93e3b8a0d7
[research_carrasco_2025]: https://arxiv.org/pdf/2505.19896
[research_cromwell_2021]: https://doi.org/10.1089/space.2020.0048
[research_kawthalkar_2022]: https://doi.org/10.1007/s42401-022-00141-1
[research_preston_dartnell_2014]: https://doi.org/10.1017/S1473550413000396
[research_rahill_2025]: https://doi.org/10.3389/frspt.2025.1505823
