---
layout: post
mathjax: true
comments: true
title: "Incident Reporting Standards in Space Agencies and Aerospace"
date: 2026-11-11 09:00:00 +0000
categories: aerospace engineering safety
---

<!-- A391 -->
<script>console.log("A391");</script>

Space agencies and the aerospace industry have written down,
in considerable detail,
how to report that something went wrong.
This article surveys those standards.
It covers how each one decides that an event needs a report,
how it grades the event,
who investigates,
what the report contains,
how it names causes,
and what must happen before anyone may close the matter.

The survey finds that the standards share a structure beneath vocabularies that do not match.
It also finds three points on which they differ and on which anyone designing a report must choose.
The first is what triggers a report.
The second is whether a severity class carries any consequence.
The third is what closing requires,
since some standards close a report once someone has taken the corrective action
and others only once someone has shown that it works.

The article has three parts.
The first describes the regimes one at a time,
namely the National Aeronautics and Space Administration,
NASA,
then civil aviation,
commercial launch,
defence practice,
the European and Japanese space standards
and industry practice.
The second describes the methods of cause analysis that the regimes call on
and the confidential channels that run beside them.
The third draws out what the regimes share
and consolidates it into a report structure that a small programme can use.
The description of each standard rests on the document itself.
The synthesis and the report structure are the author's,
and the [Epistemic State](#epistemic-state) section separates the two.

The article does not teach investigation,
and it gives no legal advice.
An earlier article on this site treats safety-critical software,
whose discipline grew out of investigations of the kind described here
[Safety-Critical Software][related_post_safety_critical_software].

## Kinds of Record

Four kinds of record recur,
and most organizations keep more than one.

- **The mishap or accident report.**
  An event caused harm or loss,
  and a formal investigation follows.
- **The close call, near miss or occurrence report.**
  An event caused little or no harm and could have caused more.
- **The nonconformance, problem or anomaly report.**
  A product or a system did not meet a requirement or did not behave as expected.
- **The failure report.**
  An item stopped performing its function,
  usually in test,
  and the report feeds a reliability programme.

The words for the events vary by regime.

| Term | Used by | Sense |
|---|---|---|
| Mishap | NASA, defence, commercial launch | An unplanned event with harm or loss |
| Accident, serious incident, incident | Civil aviation | Three classes graded by result and by potential |
| Close call, near miss | NASA, defence | An event that could have been a mishap |
| Occurrence | European Union aviation | Any safety-related event that endangers or could endanger |
| Anomaly | Commercial launch, European operations, NASA | A deviation from what was expected |
| Nonconformance | European standards, NASA, Japan | A requirement that was not met |
| Failure | Reliability practice | An item no longer able to perform its function |

The European glossary settles one pair by decree.
"Accident and mishap are synonymous."
The others do not map so neatly,
and the Japanese and European standards disagree about one of them.
In the Japanese reliability standard a nonconformance
"includes anomalies, failures, discrepancies, defects, shortages and malfunctions."
In the European standards an anomaly is an observation that may or may not turn out to be a nonconformance.
A reader moving between regimes should check each term against its own glossary.

## NASA Mishaps and Close Calls

NASA governs mishaps with one directive,
NASA Procedural Requirements 8621.1.
Revision D took effect on 6 July 2020
[NASA 2020][agency_nasa_npr_8621_1d].
An interim directive of 28 July 2026 restates and amends it,
and the agency's directives library tells readers to use the interim text
[NASA 2026][agency_nasa_nid_8621_157].
The interim directive expires on 28 July 2027,
so a reader after that date should look for its successor.
Paragraph numbers below are those of the interim directive.

### What Counts

The directive opens with the event and not with the report.
A mishap is
"an unplanned event resulting in at least one of the following"
and the list that follows names occupational injury or illness,
damage to property,
and
"NASA mission failure before the scheduled completion of the planned primary mission."
The interim directive adds a fifth outcome,
a failure to achieve the minimum mission success criteria
that the project had not declared as a contingency and accepted as a risk beforehand.
A close call is
"an event requiring first aid treatment or less, or property damage or mission failure with a direct cost of less than \\$20,000, based on a worst case estimate by the responsible organization, but has NASA mishap potential."
The interim directive also rules that in human spaceflight
any anomaly or activation of a safety-critical system that affects the safety of the crew or the spacecraft
is a mishap or a close call whether or not anyone was hurt.

The same directive says what does not count.
Damage in a test is not a mishap when it
"is limited to test articles or test facilities, and the risk of damage was formally documented and accepted by signature before the test."
The exemption rewards a programme for stating in advance what it expects to break.
Where it applies,
the directive still expects
"a proper failure review"
to find the causes and the corrective actions.

### Classification

Two measures set the class of a mishap,
and the worse of the two governs.
In the directive's words,
"The severity of the personnel injury and the direct cost of the mishap or close call (property damage or mission failure) determine the classification level of the mishap or close call (Table A)."

| Class | Direct cost of damage and mission failure | Injury or illness |
|---|---|---|
| Type A | 2 million dollars or more, or loss of a crewed aircraft or spacecraft | Fatality or permanent total disability |
| Type B | 500,000 dollars to 2 million | Permanent partial disability, or three or more people in hospital |
| Type C | 50,000 to 500,000 dollars | Days away from work or restricted duty, or one or two people in hospital |
| Type D | 20,000 to 50,000 dollars | Any other recordable injury or illness |
| Close call | Less than 20,000 dollars, with the potential for a mishap | First aid or less, with the potential for a mishap |

A third route bypasses both measures.
An official may declare a mishap or close call to be of high visibility,
whatever its cost,
when it carries
"a high degree of safety risk, programmatic impact or public, media, or political interest."
The definition names events
"affecting flight hardware or software"
among its examples.
A high-visibility event receives the treatment of a Type A or Type B mishap.

The class matters because it selects the effort.
The classification is first made within 24 hours on an estimate,
and the directive accepts that
"The final mishap classification level could change based on the final estimate of the direct cost."

### Clocks

The directive sets a deadline for each step.

| Deadline | Step |
|---|---|
| 1 hour | Telephone notice to headquarters of a Type A, Type B or high-visibility event |
| 24 hours | Declaration of the mishap or close call, its classification, and the first record in the NASA Mishap Information System |
| 7 workdays | Appointment of the investigating authority |
| Every 30 workdays | A status report that can be released to the public |
| 75 workdays | The signed investigation report |
| 15 workdays from tasking | The corrective action plan |
| Every 30 workdays | Status of corrective actions until the plan is closed |
| 10 workdays from tasking | Lessons learned |

The first record is an entry in a database and not a document.
An appendix fixes its fields under five questions,
who,
what,
when,
where
and why.
The fields due within 24 hours are the submitting organization and author,
a brief description that gives the source,
the mechanism
and the outcome of the event,
the classification,
the date and time
and the location.
The why field arrives last,
within two workdays of the signing of the report,
and holds the findings,
each supported by facts,
with the recommendations that answer them.

### Who Investigates

The directive calls the investigator the investigating authority.
It is a board of at least five members for a Type A mishap,
a board or a team of at least three for a Type B mishap,
and a team or a single investigator for anything less.
An appointing official outside the investigation appoints it and receives its report.
The members need not all be strangers to the work.
The rule is that
"The majority of IA members are to be independent from or have no responsibility for the operation or activity associated with the mishap or close call,"
where IA stands for investigating authority.
The chairperson must ensure that
"the investigation process is impartial, independent, and non-punitive."
The preface gives the reason for the last word.
"The investigation and resulting products outlined in this NPR will not be used to direct or justify disciplinary action."
NPR stands for NASA Procedural Requirements.

### The Report

The directive fixes the order of the report.

1. Signature pages,
   the list of consultants
   and the executive summary.
2. "Narrative description and facts (what, when, where, how)."
3. "Type of data gathered and data analysis."
4. Findings.
5. Recommendations.
6. A minority report,
   where a member dissents.

The title page and the executive summary carry the class,
the record number,
the date of the event
and the date of the report.
The report describes the damage or the mission failure,
the severity of any injury
and the direct cost.
It names no witnesses,
since
"Witness statements, witness names, and names of those involved in the mishap or related activities are not to be included in the mishap investigation report."

The depth of the report scales with the class.
A table in the directive lists fourteen products and marks which class needs which.
Every level down to a close call requires five of them.
They are the signatures of the investigators,
the narrative of facts,
the findings and recommendations,
any minority report,
and an explanation of why the event occurred.
That explanation must give every finding,
whether a proximate cause,
a root cause,
a contributing factor,
a failed barrier
or an observation,
with the evidence on which it rests.
Type A,
Type B
and high-visibility events add a timeline,
a description of the data gathered,
a description of each structured analysis technique used,
and an event and causal factor tree or a similar diagram of the mishap.

Two rules govern what the report may conclude.
The investigators must
"Use a structured analysis (such as Fault Tree Analysis or Human Factors Analysis) technique"
to establish what happened and why.
And they must
"Confirm the recommendations are clear, verifiable, achievable, measurable, and traceable to at least one significant finding."

### The Vocabulary of Cause

The directive defines its causal terms as a ladder,
and each definition carries a test.

- **Proximate cause.**
  "The event that occurred, including any conditions existing immediately before the undesired outcome, directly resulted in its occurrence, and if eliminated or modified, would have prevented it. Also, known as direct cause."
- **Intermediate cause.**
  "An event or condition that existed before the proximate cause, directly resulted in its occurrence, and if eliminated or modified, would have prevented the proximate cause from occurring."
- **Root cause.**
  "An event or condition, primarily associated with organizational factors, which existed before the intermediate cause and directly resulted in its occurrence"
  and which,
  had it been eliminated,
  would have prevented the outcome.
  The definition allows that
  "In the absence of a prevalent organizational factor, the root cause may be identified as undetermined."
- **Contributing factor.**
  "An event or condition that may have contributed to the occurrence of an undesired outcome, but if eliminated or modified, would not on its own have prevented the occurrence."
- **Observation.**
  "A factor, event, or circumstance identified during an investigation that did not contribute to the mishap or close call, but if left uncorrected, has the potential to cause a mishap or increase the severity of a mishap; or a positive factor, event, or circumstance that should be noted."
- **Finding.**
  "A conclusion, positive or negative, based on facts established by the investigating authority during the investigation (i.e., cause, contributing factor, and observation)."

The test is counterfactual in each case.
A cause is something whose removal would have prevented the next step up the ladder.
A contributing factor fails that test and still mattered.
An observation lies outside the chain altogether.
The appendix on data entry shows the difference between a fact and a finding with an example.
The fact is that the coefficient of friction was 0.3.
The finding is that the floor was too slippery for the employee to walk upon safely.

The label root cause has not held one meaning.
The board that investigated the loss of the Mars Climate Orbiter in 1999 worked to a draft definition,
"the first causal action or failure to act that could have been controlled systematically either by policy/practice/procedure or individual adherence to policy/practice/procedure,"
and named as the root cause
"the failure to use metric units in the coding of a ground software file"
[Mars Climate Orbiter Mishap Investigation Board 1999][agency_nasa_mco_1999].
Under the present definition,
which ties a root cause chiefly to organizational factors,
a coding error would sit nearer the proximate end of the ladder.
That reading is an inference from the two texts.
Its practical consequence is that the root causes of two NASA reports are comparable
only when both boards worked under the same revision of the directive.

### After the Report

The report does not close the matter.
Endorsing officials review it and record concurrence or nonconcurrence,
and the appointing official accepts or rejects it.
The public file of one mishap,
the fall of the N-Prime weather satellite of the National Oceanic and Atmospheric Administration,
NOAA,
from its handling fixture in 2003,
includes the endorsement form of the agency's safety office
[NOAA N-Prime Mishap Investigation Board 2004][agency_nasa_nprime_2004].
The responsible organization then writes a corrective action plan,
which must hold three things.

- "Corrective actions description and the estimated completion dates for each corrective action."
- "The lowest-level NASA organization responsible for completing the corrective actions."
- "A matrix or other means of matching corrective actions to all findings and recommendations."

Three different parties then close the loop.
The responsible manager implements the actions and reports their status.
The safety office must
"Verify corrective actions activities were implemented, completed, and closed."
The appointing official issues the closure statement,
defined as
"A final statement made by the appointing official documenting all corrective actions have been completed and the Corrective Action Plan is closed."
Before anyone adopts the actions,
the appointing official must
"Assess recommendations according to their effectiveness in reducing likelihood and consequence of causal factor reoccurrence."
Afterwards the directive asks for proof that the responsible manager implemented each action.
It does not ask for proof that the action worked,
a point on which the Japanese and the industry standards below go further.

Lessons learned are the last product.
They comprise
"at a minimum, the mishap investigation report's executive summary, findings, and recommendations authorized for public release,"
and they go to the agency's Lessons Learned Information System.
The policy that governs that system prescribes no format for a lesson
[NASA 2019][agency_nasa_npd_7120_6a].

### Three Reports in Practice

Three public reports show the form at work.
The Genesis report follows the vocabulary section by section.
Its numbered sections run from a summary of the project
through
the mishap description with sequence of events and timeline,
the method of investigation,
the proximate cause,
the root causes and contributing factors,
and the recommendations,
to other observations
[Genesis Mishap Investigation Board][agency_nasa_genesis_mib].
A fault tree closes out the physical failure scenarios in an appendix,
and an event and causal factor tree shows the path from the proximate cause to the root causes.
The board stated the proximate cause in one sentence.
"The Board determined the Genesis mishap proximate cause to be that the G-switch sensors did not activate the EST due to the improper orientation on the relay cards of SRC-AU boxes."
EST stands for the event sequence timer,
SRC for the sample return capsule
and AU for its avionics unit.

The N-Prime report organises its root causes by the four levels of a human factors taxonomy
that a later section describes,
and each of its recommendations names the findings it answers.
The report of the Columbia Accident Investigation Board is the contrast.
An external board wrote it,
outside the agency's ordinary procedure.
It speaks of a physical cause and of organizational causes,
numbers its findings,
observations
and recommendations by chapter,
and compiles every recommendation in a final chapter
[Columbia Accident Investigation Board 2003][agency_caib_2003].

### Problems Below the Threshold

Most things that go wrong in a programme are not mishaps.
NASA's handbook on problems,
nonconformances
and anomalies supplies the vocabulary for them,
and it is guidance without mandatory force
[NASA 2008][agency_nasa_hdbk_8739_18].
An anomaly is
"An unexpected event, hardware or software damage, a departure from established procedures or performance, or a deviation of system, subsystem, or hardware or software performance outside certified or approved design and performance specification limits."
A nonconformance is
"A condition of any article, material, process, or service in which one or more characteristics do not conform to requirements specified in the contract, drawings, specifications, or other approved documents."
The handbook's life cycle for a problem has seven steps,
"problem identification, problem assessment and investigation analysis, root cause determination, problem report, corrective action and problem resolution, problem recurrence control and lessons learned, and problem disposition and closure."

The handbook separates three kinds of response.
Remedial action deals with the item in hand.
Corrective action removes the cause.
Recurrence control is
"preventative action, beyond remedial action, taken to preclude or minimize the recurrence of a problem in existing and future hardware or software."
It also gives an honest name to the case in which nobody finds the cause.
"If the root cause cannot be identified with high confidence, the problem report should clearly document that the problem is an "Unexplained Anomaly" (UA), with the problem report also documenting which of the possible causes, if any, are considered the most likely cause of the problem."

The mandatory text for hardware nonconformances is the agency's quality assurance directive.
It sends serious cases to a review board that must
"investigate the cause(s) for the quality nonconformances, set the direction for their resolution, assign a disposition (e.g., scrap item, rework, repair, return, downgrade, use as is), and track and report the progress of the investigations and dispositions until closure"
[NASA 2021][agency_nasa_npr_8735_2c].
Its appendix recommends sixteen elements for the record.
Among them are the initiator,
the dates of initiation and closure,
the item's identifiers,
a detailed description,
the affected specification or drawing,
the proximate causes,
the root causes when determined,
the supporting evidence,
the disposition with its rationale,
and the people who made the decision.
The same two causal terms therefore run from the largest mishap report down to the smallest record.

## Civil Aviation

Civil aviation supplies the oldest model and the one most widely adopted.
The International Civil Aviation Organization,
ICAO,
publishes it as Annex 13 to the Convention on International Civil Aviation.
The edition in force is the thirteenth,
of July 2024
[ICAO 2024a][icao_annex_13].
The ICAO Council adopted a further amendment in March 2026,
which does not become applicable until November 2028
[ICAO 2026][icao_c_dec_237_4].
ICAO sells the Annex.
Its manual on reporting,
which restates much of the Annex and adds guidance,
is free to read
[ICAO 2024b][icao_doc_9756_part_iv].

### Purpose

The Annex states the purpose of an investigation in two sentences.
"The sole objective of the investigation of an accident or incident shall be the prevention of accidents and incidents. It is not the purpose of this activity to apportion blame or liability."
Two requirements protect that purpose.
The investigation is separate from any judicial or administrative proceeding that apportions blame,
and the authority that conducts it is independent of the aviation authorities
and of anyone else who could interfere with its objectivity.
The European Union writes the purpose into every report.
Its regulation on investigation provides that
"The report shall state that the sole objective of the safety investigation is the prevention of future accidents and incidents without apportioning blame or liability"
[European Union 2010][eu_reg_996_2010].

### Three Classes

The Annex sorts occurrences into three classes.
An accident involves death,
serious injury,
major damage to the aircraft
or its loss.
An incident is
"an occurrence, other than an accident, associated with the operation of an aircraft which affects or could affect the safety of operation."
A serious incident lies between them.
It is
"an incident involving circumstances indicating that there was a high probability of an accident."
A note to the definition adds that
"The difference between an accident and a serious incident lies only in the result."

That note carries the main idea that aviation contributes to the classification of near misses.
The Annex grades an event by what it nearly was,
not only by what it turned out to be.
An attachment to the Annex reduces the judgement to two questions.
Is there a credible scenario by which the event could have become an accident?
Were the defences that remained effective or limited?
A credible scenario with limited defences makes a serious incident.
The European Risk Classification Scheme,
ERCS,
states the same principle for all reported occurrences.
"The ERCS shall address the safety risk of an occurrence and not its actual outcome. The assessment of each occurrence shall determine the worst likely accident outcome that the occurrence might have led to, and how close to that accident outcome the occurrence was"
[European Commission 2020][eu_reg_2020_2034].

### Clocks

| Period | Step |
|---|---|
| With a minimum of delay | Notification to the states concerned |
| Immediately | Start of the investigation |
| 30 days | Preliminary report to the states concerned and to ICAO, for an accident |
| 30 days, extended to 60 on request | Consultation on the draft final report |
| As soon as possible and, if possible, within 12 months | Public final report |
| Each anniversary | An interim statement while the final report is outstanding |
| 90 days | Reply of the addressee to a safety recommendation |

The twelve months are a hope more than a rule.
ICAO's manual reports a review of fatal accidents to large aircraft between 1990 and 2016.
Of those with a public final report,
a quarter were public within one year
and about two thirds within two.
The anniversary statement exists because investigations often miss the target,
and it must detail
"the progress of the investigation and any safety issues raised."

### The Final Report

The Annex recommends a format and allows a state to adapt it.
The report opens with a title and a synopsis,
and its body has four parts,
namely factual information,
analysis,
conclusions
and safety recommendations.
The first part has nineteen subheadings in a fixed order.

1. History of the flight.
2. Injuries to persons.
3. Damage to aircraft.
4. Other damage.
5. Personnel information.
6. Aircraft information.
7. Meteorological information.
8. Aids to navigation.
9. Communications.
10. Aerodrome information.
11. Flight recorders.
12. Wreckage and impact information.
13. Medical and pathological information.
14. Fire.
15. Survival aspects.
16. Tests and research.
17. Organizational and management information.
18. Additional information.
19. Useful or effective investigation techniques.

The fixed order makes any report comparable with any other.
A reader who wants the weather turns to the seventh subheading of every report ever written to the format.
The injuries go into a table,
and the damage to the aircraft is one of four words,
destroyed,
substantially damaged,
slightly damaged
or no damage.

The discipline of the format lies in the wall between its parts.
The analysis may draw only on what the factual part records,
and the manual adds that
"no new facts should be introduced in the analysis part."
The conclusions list the findings and then the causes or contributing factors,
and the Annex asks that the list
"include both the immediate and the deeper systemic causes and/or contributing factors."
The manual gives several rules for writing them.

- "Significant events and factors that were investigated in detail, but eliminated in the analysis, should also be stated in the findings."
- "When certain of a cause, a definite statement should be used; if reasonably sure of a cause, a qualifying word such as "probable" or "likely" should be used."
- "When there is insufficient evidence to establish why an accident or an incident occurred, there should be no hesitation in stating that the causes remain undetermined."
- "In order to ensure that appropriate action is taken, each safety recommendation should be issued to a specific addressee."

The manual also shows the same causes written twice,
once naming the people who failed
and once naming the function that nobody performed,
and it prefers the second.
And it notes a practice that suits a small organization.
"For reporting on small investigations, many States have created abbreviated report formats that contain only the history of flight, information on the deficiencies discovered by the investigation, analysis of the factors contributing to the occurrence, and findings related to the deficiencies."

### Causes and Contributing Factors

The Annex defines its two causal terms differently from NASA.
"Causes are defined as actions, omissions, events, conditions, or a combination thereof, which led to the accident or incident."
"Contributing factors are actions, omissions, events, conditions, or a combination thereof, which, if eliminated, avoided or absent, would have reduced the probability of the accident or incident occurring, or mitigated the severity of the consequences of the accident or incident."
The Annex lets a state use either term or both.
Its contributing factor is a matter of probability and of severity.
NASA's contributing factor is one whose removal
"would not on its own have prevented the occurrence."
The two definitions overlap without coinciding,
and a factor that mitigated nothing but made the event more likely
is a contributing factor in the Annex's sense alone.
That comparison is an inference from the two texts.

Both definitions in the Annex end with the same sentence,
that identifying a cause or a contributing factor
"does not imply the assignment of fault or the determination of administrative, civil or criminal liability."

### The United States

The United States applies the Annex through the National Transportation Safety Board,
the NTSB.
Its regulation on notification,
part 830 of title 49 of the Code of Federal Regulations,
CFR,
defines an aircraft accident,
serious injury
and substantial damage,
and lists the serious incidents that an operator must report at once,
among them a failure of the flight control system,
a fire in flight
and a collision in flight
[NTSB 2026a][reg_49cfr830].
The operator files a written report within ten days of an accident.

The regulation on procedure states the character of the investigation.
"NTSB investigations are fact-finding proceedings with no adverse parties"
and
"are not conducted for the purpose of determining the rights, liabilities, or blame of any person or entity"
[NTSB 2026b][reg_49cfr831].
The board brings the organizations involved into the investigation as parties.
"Party status is limited to those persons, Federal, state, or local government agencies and organizations whose employees, functions, activities, or products were involved in the accident and that can provide suitable qualified technical personnel to actively assist in an investigation."
The parties supply expertise and may submit proposed findings.
They do not decide the outcome,
since
"determining the probable cause of an accident is exclusively the right and duty of the NTSB."

The board's report on the loss of a door plug from an airliner in January 2024 shows the form
[NTSB 2025][ntsb_air_25_04].
It keeps the four parts of the Annex,
uses twelve of the nineteen subheadings,
and opens with an executive summary under three questions,
what happened,
what the board found
and what it recommended.
Its conclusions hold 35 numbered findings and then a statement of probable cause,
which begins
"The National Transportation Safety Board determines that the probable cause of this accident was"
and is followed by a sentence that begins
"Contributing to the accident was."
It issues nineteen new recommendations,
each to a named addressee
and each with its own number.

The board then tracks every recommendation by status.
"The status of a recommendation is "open" until the sufficient action has been achieved to mark it "closed""
[NTSB Status Explanation][ntsb_status_explanation].
The statuses grade the response as well as record it.
One open status reads
"Open--Acceptable Response: Response by recipient indicates a planned action that would comply with the safety recommendation when completed."
One closed status reads
"Closed--Acceptable Action: Response by recipient indicates action on the safety recommendation has been completed. The action complies with the safety recommendation."
A recommendation can also close unacceptably,
when the recipient disagrees and the board concludes that further correspondence would change nothing.
The vocabulary admits that a closed item is not always a solved one.

### Occurrence Reporting in the European Union

Investigation deals with the few events that are accidents or serious incidents.
A second European regulation deals with the many that are not
[European Union 2014][eu_reg_376_2014].
It defines an occurrence as
"any safety-related event which endangers or which, if not corrected or addressed, could endanger an aircraft, its occupants or any other person."
Named classes of people,
from the pilot in command to ground staff,
must report an occurrence
"within 72 hours of becoming aware of the occurrence, unless exceptional circumstances prevent this,"
and their organization has a further 72 hours to pass the report to the authority.
Each organization must also keep a voluntary system for
"other safety-related information which is perceived by the reporter as an actual or potential hazard to aviation safety."

The regulation fixes the minimum content of a report in an annex.
The common fields are a headline,
the responsible entity and file number,
the status of the occurrence,
the date,
the place,
the class and category of the occurrence,
a narrative,
the type of event
and a risk classification.
The organization must then analyse what it collects.
Where it finds a risk,
it sends preliminary results to the authority within 30 days
and final results,
in principle,
within three months.
Where it decides on corrective or preventive action,
it must
"establish a process to monitor the implementation and effectiveness of the action."

The regulation also protects the reporter,
under the name of just culture.
"'just culture' means a culture in which front-line operators or other persons are not punished for actions, omissions or decisions taken by them that are commensurate with their experience and training, but in which gross negligence, wilful violations and destructive acts are not tolerated."
An employee who reports,
or who is named in a report,
"shall not be subject to any prejudice by their employer."

## Commercial Launch and Reentry

The Federal Aviation Administration,
the FAA,
licenses commercial launch and reentry in the United States,
and its rule takes a different shape from NASA's.
It has one definition of a mishap and no classes
[FAA 2026a][reg_14cfr_401_7].

"Mishap means any event, or series of events associated with a licensed or permitted activity resulting in any of the following: (1) A fatality or serious injury (as defined in 49 CFR 830.2); (2) A malfunction of a safety-critical system; (3) A failure of the licensee's or permittee's safety organization, safety operations, safety procedures; (4) High risk, as determined by the FAA, of causing a serious or fatal injury to any space flight participant, crew, government astronaut, or member of the public; (5) Substantial damage, as determined by the FAA, to property not associated with licensed or permitted activity; (6) Unplanned substantial damage, as determined by the FAA, to property associated with licensed or permitted activity; (7) Unplanned permanent loss of a launch or reentry vehicle during licensed activity or permitted activity; (8) The impact of hazardous debris outside the planned landing site or designated hazard area; or (9) Failure to complete a launch or reentry as planned as reported in § 450.213(b)."

The agency did propose classes.
Its proposal of 2019 set out four,
numbered from Class 1 to Class 4
and modelled on NASA and Air Force practice
[FAA 2019][reg_faa_nprm_2019].
The final rule of 2020 dropped them,
and the reason is instructive.
"The FAA reviewed the regulatory requirements associated with each of the proposed mishap classes and agrees there were no significant differences among the regulatory requirements for each class. The requirements to report, respond to, and investigate mishaps are incumbent upon an operator regardless of a mishap's severity"
[FAA 2020][reg_faa_final_rule_2020].
A severity class earns its place only when something depends on it.
The same preamble says that the fourth outcome,
high risk,
is meant
"to cover events akin to a near miss or close-call."

The regulation also defines the tier below a mishap.
"Anomaly means any condition during licensed or permitted activity that deviates from what is standard, normal, or expected, during the verification or operation of a system, subsystem, process, facility, or support equipment."
And it has its own version of the exemption for expected damage.
Test-induced damage is not a mishap when the operator agreed its scope with the agency beforehand
and the damage harmed nobody outside the activity
[FAA 2026c][reg_14cfr_450_175].

### What the Operator Owes

The operator must work to a written mishap plan
[FAA 2026b][reg_14cfr_450_173].
Notice is immediate for a fatality or a serious injury
and within 24 hours otherwise.
A written preliminary report follows within five days,
and the rule lists its contents.

- Date and time of the mishap.
- "Description of the mishap and sequence of events leading to the mishap, to the extent known."
- Intended and actual location of the launch,
  reentry
  or landing.
- Impact points of hazardous debris.
- Identification of the vehicle and of any payload.
- "Number and general description of any fatalities or injuries."
- "Description and estimated costs of any property damage."
- Hazardous materials involved.
- "Action taken by any person to contain the consequences of the event."
- Weather at the time.
- "Potential consequences for other similar vehicles, systems, or operations."

The last item deserves notice.
Within five days the operator must say what the event may mean for other vehicles,
which is the question that the European alert system,
described below,
also asks.

On the investigation itself the rule is brief.
An operator must
"Investigate the root causes of the mishap"
and
"Report investigation results to the FAA."
It must also
"identify and implement preventative measures for avoiding recurrence of the mishap prior to the next flight, unless otherwise approved by the Administrator."
The rule prescribes no format for the final report.
The agency's advisory circular,
which does not bind,
recommends NASA's.
"The FAA recommends use of the NASA mishap report format, as documented in NASA Procedural Requirements (NPR 8621.1, as revised)"
[FAA 2021][reg_faa_ac_450_173_1].
The circular lists the same six sections,
asks that the plan provide for
"the recording of any dissenting opinions,"
and adds that
"Corrective actions should not only address technical root causes, but also any organizational root causes."
It also asks for a step that NASA's directive leaves out,
saying that
"an operator's plan should include a process for following up to verify the implementation and effectiveness of preventative measures."

### Closure and Return to Flight

The operator usually leads the investigation and the agency oversees it.
The agency's page on the process describes two ways back to flight
[FAA 2026d][reg_faa_mishap_page].
In the first,
the agency accepts the final report,
and
"if accepted, the mishap investigation is closed. The corrective actions then must be implemented, and all relevant licensing requirements met before a return to flight operations."
In the second,
the operator asks to fly before the investigation ends,
and the agency may
"authorize a return to flight operations while the mishap investigation remains open."
Closure therefore means that the agency has accepted the report.
The implementation of the corrective actions is a separate condition,
checked afterwards.

The agency's public statements show the form of a closed case
[FAA 2026e][reg_faa_statements].
Of the seventh flight test of the Starship vehicle it wrote in March 2025 that
"The final mishap report cites the probable root cause for the loss of the Starship vehicle was stronger than anticipated vibrations during flight led to increased stress on, and failure of, the hardware in the propulsion system. SpaceX identified 11 corrective actions to prevent a reoccurrence of the event. The FAA verified that SpaceX implemented corrective actions prior to Flight 8."
Of the first flight of the New Glenn vehicle it wrote that
"The final mishap report identified the proximate cause of the mishap as an inability of New Glenn's first stage to restart the engines, preventing a reentry burn from occurring, and resulting in the loss of the stage. Blue Origin identified seven corrective actions to prevent reoccurrence of the event."
Each statement carries the same items,
namely the event,
who led and who accepted the investigation,
one sentence of cause,
a count of corrective actions,
how the agency verifies their implementation,
and the determination on flight.
The label on the cause varies from one statement to the next,
from probable root cause to proximate cause to direct cause,
and the statements do not explain the choice.

Where a mishap kills or seriously injures someone,
or throws dangerous debris onto property unconnected with the launch,
the National Transportation Safety Board leads the investigation
under an agreement that the two agencies signed in September 2022
[NTSB and FAA 2022][reg_ntsb_faa_moa_2022].
The board proposed a rule of its own for commercial space investigations in 2021
and later withdrew it
[NTSB 2021][reg_ntsb_nprm_2021]
[OIRA 2024][reg_oira_3147_aa19].

## Defence Practice

The United States Department of Defense contributes three things to the subject.
They are a set of classes that NASA's table closely resembles,
a separation of two investigations,
and the standard matrix of severity against probability.

### Classes

The department's instruction,
in which DoD stands for the Department of Defense,
defines a mishap as
"An unplanned event or series of events that results in damage to DoD property; occupational illness to DoD personnel; injury to on- or off-duty DoD military personnel; injury to on-duty DoD civilian personnel; or damage to public or private property, or injury or illness to non-DoD personnel, caused by DoD activities"
[DoD 2019][mil_dodi_6055_07].
It defines four classes.
The issue read here,
change 2 of June 2019,
prints thresholds of 2 million dollars for Class A,
500,000 dollars for Class B,
50,000 dollars for Class C
and 20,000 dollars for Class D,
with injury criteria that step down from fatality or permanent total disability
to any recordable injury.
Later thresholds may apply,
and the author could confirm none from a primary text.
The instruction also defines the event that was not a mishap.
A near miss is
"An undesired event that, under slightly different circumstances, would have resulted in personal harm, property damage, or an undesired loss of resources."

The instruction asks two questions before it assigns any class.
Did an event occur that resulted in death,
injury,
illness
or property damage?
Was the outcome intended?
Harm that nobody intended is a mishap,
and the instruction notes that
"Mishaps may be reassigned to a different class as more data becomes available."

### Two Investigations

The department runs two investigations of a serious mishap and keeps them apart.
The instruction states the purpose of the safety investigation in two words,
"Prevent mishaps."
The legal investigation exists to
"Inquire into all the facts and circumstances surrounding mishaps as well as to obtain and preserve all available evidence for use in litigation, claims, disciplinary action, adverse administrative action, and for public disclosure."
The instruction requires the department to
"Conduct the legal investigation independently from the safety investigation,"
and it bars the safety investigators from serving on the legal one.

The separation protects candour.
The instruction explains that
"Safety privilege is based on a national defense need for rapid and accurate assessment of the causes of mishaps to prevent a recurrence and maintain mission readiness."
The privilege covers statements given under a promise of confidentiality
and the deliberations of the investigators,
including their findings,
causes
and recommendations.
Facts are not privileged and pass to the legal investigation.
A public report of an Air Force accident investigation board shows the result.
Its Summary of Facts and its Statement of Opinion are separate parts
[USAF Accident Investigation Board][mil_usaf_aib_uh1n_2023],
and the statute forbids the use of the opinion as evidence in a civil or criminal proceeding
[United States Code 2023][mil_10usc2254].

A civil programme has no such privilege to offer.
It can still borrow the lesser form of the idea,
which is to keep the facts and the opinions in separate parts of one report.

### Severity, Probability and Risk

The department's system safety standard looks forward where the instruction looks back
[DoD 2023][mil_std_882e].
It defines a hazard as
"A real or potential condition that could lead to an unplanned event or series of events (i.e. mishap) resulting in death, injury, occupational illness, damage to or loss of equipment or property, or damage to the environment,"
and risk as
"A combination of the severity of the mishap and the probability that the mishap will occur."
It grades severity in four categories.

| Category | Name | Injury criterion | Monetary loss |
|---|---|---|---|
| 1 | Catastrophic | Death or permanent total disability | 10 million dollars or more |
| 2 | Critical | Permanent partial disability, or three or more people in hospital | 1 million to 10 million dollars |
| 3 | Marginal | One or more lost work days | 100,000 dollars to 1 million |
| 4 | Negligible | No lost work day | Less than 100,000 dollars |

It grades probability in six levels,
from A,
Frequent,
through Probable,
Occasional,
Remote
and Improbable
to F,
Eliminated.
The standard reserves the last level for a hazard that no longer exists,
and it warns that
"No amount of doctrine, training, warning, caution, or Personal Protective Equipment (PPE) can move a mishap probability to level F."
A matrix then assigns one of four risk levels to each pair.
The standard writes a pair as a code of one digit and one letter.
"For example, a RAC of 1A is the combination of a Catastrophic severity category and a Frequent probability level,"
where RAC stands for risk assessment code.

| Risk level | Codes |
|---|---|
| High | 1A, 1B, 1C, 2A, 2B |
| Serious | 1D, 2C, 3A, 3B |
| Medium | 1E, 2D, 2E, 3C, 3D, 3E, 4A, 4B |
| Low | 4C, 4D, 4E |

The two scales are easy to confuse and should not be.
A severity category describes a mishap that could happen and tops out at 10 million dollars.
A mishap class describes one that did happen and,
in the issue read here,
tops out at 2 million.
Catastrophic is not another word for Class A.

Two further passages of the standard bear on a report.
It ranks the measures that reduce a risk,
from eliminating the hazard by design,
through engineered features and warning devices,
down to procedures and training,
and it advises that for the two worst severity categories
"the use of signage, procedures, training, and PPE as the only risk reduction method should be avoided."
The ranking is a ready test of a corrective action.
An action that only tells people to be more careful sits at the bottom of it.
The standard also lists the minimum contents of a hazard record,
"identified hazards, associated mishaps, risk assessments (initial, target, event(s)), identified risk mitigation measures, selected mitigation measures, hazard status, verification of risk reductions, and risk acceptances."

## European Space Standards

The European Cooperation for Space Standardization,
ECSS,
publishes the standards under which the European Space Agency and its contractors work.
Its unit of record is the nonconformance and not the mishap.
The current standard on the subject is the first revision of issue C,
dated 1 March 2018
[ECSS 2018][ecss_q_st_10_09c_rev1].

### Nonconformance

The ECSS glossary defines a nonconformance in four words,
"non-fulfilment of a requirement"
[ECSS 2023][ecss_s_st_00_01c_rev1].
The definition ties every report to a requirement that the product failed to meet,
which is why the report form has a place for the affected document.
The standard sorts nonconformances into two classes.
A major nonconformance is one that can affect the customer's requirements in a listed set of areas,
among them
"safety of people or equipment,"
"operational, functional or any technical requirements imposed by the business agreement,"
"reliability, maintainability, availability"
and
"lifetime."
A minor nonconformance is any that
"by definition cannot be classified as major."
Two rules of classification stand out.
The class follows consequence,
and a note adds that
"Classification of nonconformances is not based on their consequences on cost and schedule."
And doubt resolves upward.
"In case of doubt, the internal NRB shall classify nonconformances as major."
The abbreviation is for the nonconformance review board.

### The Board and Its Dispositions

The review board decides everything about a nonconformance.
"The NRB shall be the sole technical authority for the treatment of nonconformances occurring in the frame of a business agreement."
It has two tiers.
An internal board at the supplier,
chaired by product assurance with engineering as its other core member,
handles every case,
and a customer board joins for a major one.
The supplier must tell the customer of a major nonconformance
"within five working days of their detection."

Three actions come before any board meets.
The supplier must protect people and equipment,
mark and segregate the item to prevent its unauthorized use,
and prevent a recurrence on similar items then in process or under test.
The description written at that point must be
"sufficiently detailed that it can be understood by personnel not involved"
in the detection.

The board then chooses among five dispositions for the item.

- **Return to supplier.**
  "This disposition only applies to nonconforming procured items."
- **Use as is.**
  "The item is found to be usable without eliminating the nonconformance."
- **Rework.**
  "The item is recoverable to conform completely to all specified requirements."
- **Repair.**
  The work makes the item fit for its intended use
  although it still does not conform to the original requirement.
- **Scrap.**
  "The item is not recoverable by rework or repair, for technical or economic reasons."

A disposition settles the item in hand.
It does not settle the cause,
and the standard treats the two separately.
The board
"shall investigate the cause(s) of the nonconformance,"
and in particular
"shall analyse whether human error or poor workmanship are the primary or secondary cause for the nonconformance."
It
"shall determine corrective actions to eliminate the cause(s) of the nonconformance and prevent any recurrence,"
and it
"shall determine also preventive actions to avoid the occurrence of the nonconformance on similar items."
The standard names no method of cause analysis.
A major nonconformance with a disposition of use as is,
or of repair,
needs a request for waiver that the customer approves.

### The Report and Its Closure

A normative annex specifies the nonconformance report in 39 elements,
and the supplier may use any form that carries the mandatory ones.
They fall into six groups.

- **Identification.**
  The company,
  the project,
  a unique report number and revision,
  and whether the item is on the list of critical items.
- **The item.**
  Its name and number,
  the drawing or part number that defines it,
  and the procedure in execution when the nonconformance occurred.
- **The observation.**
  The date and place,
  the activity under way,
  a description with the means of detection and the conditions,
  and the name,
  date
  and signature of the person who raised the report.
- **The first decision.**
  The class,
  the dispositions of the internal board,
  the cause,
  defined as the
  "basic fact or circumstance which causes the"
  nonconformance,
  and the corrective or preventive actions.
- **The second decision, for a major report.**
  The dispositions of the customer board,
  the cause as finally determined,
  the corrective actions it agreed,
  and any request for waiver.
- **Closure.**
  A statement by product assurance for every action the board determined,
  and the date,
  signature
  and stamp of the person who closes the report.

The form thus records the cause twice,
once as first found and once as finally determined.
It allows the first account to be wrong.

The standard states when a report may close.

1. "All related actions have been performed and their results successfully verified."
2. "All defined inspections and tests have been performed, and their results verified and reported on or traceable from the NCR."
3. "Related RFWs are approved."

NCR stands for nonconformance report and RFW for request for waiver.
The supplier's product assurance representative closes the report,
and a major report closes
"only after customer PA endorsement,"
where PA stands for product assurance.
The supplier must also keep a status list of every report
and review the whole population for trends
"not less than quarterly,"
counting the reports by cause.

### Anomalies in Operation

A nonconformance is a confirmed failure to meet a requirement.
An anomaly is an observation that something was not as expected,
and it comes first.
The earlier issue of the glossary defined an anomaly as
"any deviation from the expected situation"
and noted that
"An anomaly justifies an investigation that might lead to the discovery of a nonconformance or a defect"
[ECSS 2012][ecss_s_st_00_01c_2012].
The current glossary no longer defines the word,
though current standards still use it.

In flight operations the anomaly has its own report and its own board
[ECSS 2008][ecss_e_st_70c].
"An anomaly review board shall be established to review and analyse space segment anomalies and to agree on corrective measures."
"Space segment and ground segment anomalies shall be formally reported and documented in the form of an operations anomaly report."
The reports
"shall be maintained for the entire life of the mission and tracked until closure."
The nonconformance rules apply
"in the case that the anomaly is shown to be a nonconformance."

The operations anomaly report has six sections after its identification.

1. Preliminary elements.
   The operational context,
   the suspected source,
   a title,
   the date and time of occurrence,
   the severity,
   the originator,
   the authorising manager
   and the status.
2. Introduction.
   The operational impact in summary,
   the recovery actions taken,
   and whether this is the first occurrence.
3. Details of the anomaly.
   References to earlier occurrences,
   the actions under way that may have contributed,
   the configuration before,
   during
   and after,
   and supporting material such as telemetry and logs.
4. Actions taken.
   A chronicle of the response.
5. Operational impact.
   Outages,
   replanning
   and the effect on redundancy.
6. Recommendations.
   A proposed course of further investigation and resolution,
   with a schedule.

Its severity scale has three steps and grades an anomaly by its effect on the mission.

- "No impact: The anomaly has no impact on the primary mission objectives"
- "Minor impact: The anomaly has no significant operational impact on the mission."
- "Major impact: The anomaly has a substantial impact on the mission objectives, or compromises the future safety of the mission or the available redundancies."

### The Alert

One output of the European system has no close counterpart in NASA's mishap directive.
An alert is a
"formal notification to users, informing them of failures or problems that can affect more than one user, or can recur in other projects or circumstances, if no preventive actions are taken."
The board that handles a major nonconformance must
"Assess the need for raising an alert to other users of similar nonconforming items."
The alert carries the question of read-across,
namely who else has this problem,
out of the single report and into a channel of its own
[ECSS 2016][ecss_q_st_10c_rev1].

### Inquiries

For the loss of a flight the European Space Agency convenes an inquiry board,
and its public reports show a stable form.
The report on the first flight of Ariane 5 runs from the failure,
through the analysis with its chain of technical events,
to conclusions and fourteen numbered recommendations
[Lions 1996][esa_ariane_501_1996].
The agency's summary describes the method.
"A chain of events, their inter-relations and causes have been established, starting with the destruction of the launcher and tracing back in time towards the primary cause"
[ESA 1996][esa_pr_33_1996].
The board's statement of cause has two parts.
The first is the mechanism,
that the loss of guidance information
"was due to specification and design errors in the software of the inertial reference system."
The second is the defence that failed,
that the reviews and tests of the development programme did not include the analysis and testing
"which could have detected the potential failure."

The agency charged the inquiry into the loss of the Schiaparelli lander in 2016
"To establish the root cause of the anomaly and the reasons for this root cause."
It organised its work around an anomaly tree,
named four root causes of equal standing,
and added a counterfactual about one of them,
that had a single timing value been correct
"the landing would probably have been successful, in which case the other root causes would probably never have been identified"
[Tolker-Nielsen 2017][esa_schiaparelli_2017].
The sentence is a caution about every investigation that stops at the first sufficient cause.

## Japan

The Japan Aerospace Exploration Agency publishes English translations of its standards,
with the Japanese text taking precedence.
Its quality standard requires at least ten items in the record of a noncompliance,
among them the date and process of detection,
the description against the requirement or the acceptance criteria,
the causes,
the dispositions,
the confirmed results of the dispositions
and the corrective actions
[JAXA 2008][jaxa_jmr_005a].
For serious cases it requires an analysis of background factors by a named method,
and
"The reason for noncompliance shall be investigated until the"
root causes that lead to corrective action are identified.

Its reliability standard sets the strictest closing rule read for this article
[JAXA 2012][jaxa_jmr_004c].
"Close-out of each anomaly or failure shall require at least all of the following"
and six conditions follow.

- "Corrective actions have been accomplished."
- "Necessary preventive changes have been devised and accomplished, and the pertinent engineering change notices have been referenced on the close-out documentation."
- "Appropriateness of necessary design or software changes is proven by test."
- "The effectiveness of preventive actions has been proven."
- "The preventive action has been appropriately made in existing similar items."
- "The close-out document has been signed off by the appropriate management authority to ensure completion of a technical review and by the reliability or quality organization to confirm completion of all actions."

Three of the six go beyond confirming that someone took an action.
A test must prove the change,
the contractor must show that the preventive action works,
and that action must reach the similar items that already exist.

## Industry Practice

### Failure Reporting, Analysis and Corrective Action

The United States defence handbook on failure reporting gives the closed loop its classic definition
[DoD 1995][mil_hdbk_2155].
"Closed loop failure reporting system. A controlled system assuring that all failures and faults are reported, analyzed (engineering or laboratory analysis), positive corrective actions are identified to prevent recurrence, and that the adequacy of implemented corrective actions is verified by test."
Its steps are failure reporting,
failure analysis,
failure verification,
corrective action
and close-out.
Verification means confirming that the reported failure was real,
since
"All reported failures shall be verified as actual or an explanation provided for lack of verification."

The handbook prescribes no form.
It requires that a failure report identify the failed item,
the symptoms,
the test conditions
and the operating time at failure,
and its appendix puts the content as five questions.
"The failure documentation must provide information on who discovered the failure, what failed, where it failed, when it failed, and how future failures will be prevented."
A failure review board oversees the system.
"A Failure Review Board (FRB) shall be established to review failure trends, corrective action status, and to assure adequate corrective actions are taken."

Its closing rule has two branches.
"A failure report shall be considered closed-out upon completion of corrective action implementation and verification or rationale in those instances where corrective action was not implemented. The rationale to support no corrective action shall be documented and approved by responsible authority."
A report may therefore close without a fix,
provided someone with authority signs the reason.

### Reliability Growth

Failure reporting has a quantitative side.
If a programme finds its failures,
analyses them
and corrects the design,
the reliability of the system should grow,
and the programme can measure the growth.
Duane observed that when a programme incorporates fixes during development,
a plot of cumulative failure rate against cumulative test time is a straight line on logarithmic axes
[DoD 2011][mil_hdbk_189c].
Let $\lambda\_{\Sigma}$ be the cumulative failure rate,
$F$ the number of failures in $H$ total test hours,
$K$ a constant
and $\alpha$ the growth rate.

$$
\lambda_{\Sigma} = \frac{F}{H} = K H^{-\alpha}
\tag{1}
$$

[DoD 1998][mil_hdbk_338b].
The failure rate that the system shows now is lower than its cumulative average,
because the average still counts the failures of the early design.
Differentiating the number of failures with respect to time gives the instantaneous rate.

$$
\lambda_{\mathrm{I}} = \frac{dF}{dH} = \left( 1 - \alpha \right) K H^{-\alpha}
\tag{2}
$$

The mean time between failures is the reciprocal of each rate.
With $M\_{\mathrm{C}}$ the cumulative value
and $M\_{\mathrm{I}}$ the instantaneous one,

$$
M_{\mathrm{I}} = \frac{M_{\mathrm{C}}}{1 - \alpha}
\tag{3}
$$

The handbook explains the instantaneous value as
"The MTBF that the equipment currently on test would exhibit if we stopped the reliability growth and continued testing,"
where MTBF stands for the mean time between failures.
A programme that has logged 12 failures in 1,000 hours has a cumulative value of about 83 hours.
At a growth rate of 0.4 its instantaneous value is about 139 hours.

The growth rate is the link to the reporting system.
The handbook says that it
"can vary between 0.1 and 0.6,"
that the low figure
"can be expected in those programs where no specific consideration is given to reliability,"
and that the high figure needs
"an aggressive, hard-hitting reliability program with management support."
The rate
"is governed by the amount of control, rigor, and efficiency by which failures are discovered, analyzed, and corrected through design and quality action."
The growth rate is,
in that sense,
a measure of how well the closed loop is working.
The later handbook on reliability growth warns against treating the model as exact.
It notes that Duane's plots impute zero reliability at the start of test,
and that the method
"makes no allowance for variation."

### Quality Systems and Structured Problem Solving

The quality management standards of the industry put nonconformity and corrective action in one clause.
The International Organization for Standardization,
ISO,
and SAE International sell ISO 9001 and its aerospace derivative AS9100,
and the author did not read their text.
The free guidance of their owners shows what the clause demands as records,
namely
"Evidence of the nature of the nonconformities and any subsequent actions taken"
and
"Results of any corrective action"
[ISO Documented Information][iso_documented_information].
The aerospace version adds a requirement
"to include the human factors considerations in the root causes analysis of nonconformities"
[IAQG 2020][iaqg_9100_2016_overview].

The vocabulary of these standards separates three actions that plain speech runs together.
The European aerospace standard on problem solving defines them
[CEN 2018][en_9136_2018].
A correction is
"action taken to eliminate a detected nonconformity."
A corrective action is
"action taken to eliminate the cause of a detected nonconformity or other undesirable situation to prevent recurrence."
A preventive action is
"action to eliminate the cause of a potential nonconformity or other undesirable potential situation."
The ECSS glossary states the contrast in one line.
"Corrective action is taken to prevent recurrence whereas preventive action is taken to prevent occurrence."

The same standard sets out a method in nine steps,
numbered from zero.

- Step 0. Start immediate containment actions.
- Step 1. Build the team.
- Step 2. Define the problem.
- Step 3. Complete and optimise the containment actions.
- Step 4. Identify the root causes.
- Step 5. Define and select permanent corrective actions.
- Step 6. Implement the permanent corrective action and check its effectiveness.
- Step 7. Standardise and transfer the knowledge across the business.
- Step 8. Recognise and close the team.

Its definitions add two distinctions that a report can use directly.
The first is among kinds of cause.
An apparent cause is the
"event or action that immediately results in or precedes the nonconformity,"
with the note that
"This is generally NOT the root cause."
Contributing causes are
"causes that by themselves would not cause the problem, but can increase the risk of the issue to occur."
A root cause is the
"original event(s), action(s), and/or condition(s) generating (directly or in cascade) an actual or potential undesirable condition, situation, nonconformity, or failure."
The second distinction is between two verifications.
Implementation verification is
"action taken to verify that the planned actions were taken as scheduled."
Effectiveness verification is
"action taken to verify that the planned corrective action(s) have prevented recurrence."
The first asks whether someone did the work.
The second asks whether it worked.

## Methods of Cause Analysis

The standards above require a structured analysis and mostly decline to name one.
Five methods recur in them and in the reports written under them.

### The Timeline

Every regime starts from the order of events.
NASA defines a timeline as
"Events and conditions preceding and following a mishap supported by facts and arranged in chronological order,"
and its vocabulary separates the two things a timeline holds.
An event is
"A real-time occurrence describing one discrete action, typically an error, failure, or malfunction,"
and a condition is
"A single as-found state."
The Annex 13 format puts the same material under the history of the flight,
and ICAO's manual asks the report to state the time reference it uses
and its offset from Coordinated Universal Time.

### The Event and Causal Factor Tree

NASA's own method builds a tree downward from the outcome.
The directive defines the event and causal factor tree as
"A graphic representation of the mishap or close call that shows the event (accident) at the top of the tree; depicts the logical sequence of events; illustrates all causal factors (including conditions and failed barriers) necessary and sufficient for the mishap or close call occurrence; and depicts the root causes at the bottom of the tree."
The agency's overview of root cause analysis gives the procedure in six steps
[NASA 2003][agency_nasa_rca_overview_2003].

- "Clearly define the undesired outcome."
- "Gather data, including a list of all potential causes."
- "Create an event and causal factor tree."
- "Continue asking "why" to identify root causes."
- "Check your logic and eliminate items that are not causes."
- "Generate solutions that address both proximate causes and root causes."

The same overview supplies the test for each item on the tree.
"If the action, deficiency, or decision in question were corrected, eliminated or avoided, would the undesired outcome be prevented or avoided?"
An item that passes stays on the tree as a cause,
and an item that fails comes off.
It also supplies three reasons to stop asking why.
The analysis has reached the organizational factors,
or a problem that the organization cannot correct,
or the end of the data.
Where the evidence is incomplete,
"the analyst can use the term "probable" to describe the proximate, intermediate, or root cause."

### The Fault Tree

A fault tree runs the other way in purpose.
It starts from an undesired state and asks what combinations of faults could produce it.
NASA's handbook defines the method as one
"whereby an undesired state of the system is specified (usually a state that is critical from a safety or reliability standpoint), and the system is then analyzed in the context of its environment and operation to find all realistic ways in which the undesired event (top event) can occur"
[Stamatelatos et al. 2002][agency_nasa_fault_tree_handbook_2002].
An investigation uses it to close out possibilities.
Each branch is a candidate scenario,
and the evidence either supports the branch or eliminates it,
which is how the Genesis board used its tree.

The tree is a logical model,
and an analyst can evaluate it in numbers.
Two gates do most of the work.
An OR gate passes a fault when either input occurs.
With $P(A)$ and $P(B)$ the probabilities of two independent input events
and $P(Q)$ the probability of the output,

$$
P(Q) = P(A) + P(B) - P(A)\,P(B)
\tag{4}
$$

An AND gate passes a fault only when both inputs occur.
For independent inputs,

$$
P(Q) = P(A)\,P(B)
\tag{5}
$$

Two independent faults with probabilities of 0.01 and 0.02
give 0.0298 through an OR gate
and 0.0002 through an AND gate.
The handbook warns about the assumption.
"If A and B are not independent events, then P(Q) may be significantly greater than P(A)P(B)."
A common cause,
such as one bad procedure applied to two redundant units,
defeats the product rule.

A minimal cut set is
"the smallest combination of basic events that result in the top event."
A cut set with a single member is a single point of failure.
Let $P(T)$ be the probability of the top event,
$C\_{i}$ the minimal cut sets
and $P(b\_{j})$ the probability of basic event $j$.
When the basic events are improbable,
the probability of the top event is close to the sum over the cut sets.

$$
P(T) \approx \sum_{i} \prod_{j \in C_{i}} P(b_{j})
\tag{6}
$$

The handbook calls that sum the rare event approximation
and gives it as accurate for basic event probabilities below 0.1.
It also states the limit of the method.
The faults in a tree
"are not exhaustive"
and
"cover only the faults that are assessed to be realistic by the analyst."
A fault tree cannot find the scenario that nobody thought to draw.

### The Five Whys and the Fishbone Diagram

The simplest method is to ask why until the answer stops being a symptom.
One guide from the United States government describes the five whys as
"a simple problem-solving technique that helps to get to the root of a problem quickly"
and adds that
"It often takes three to five whys, but it can take more than five!"
[CMS 2014a][ref_cms_five_whys].
The Japanese quality standard requires the method by name for serious cases.
The same guide states its limit.
"Note that the Five Whys technique may not always help you to identify the root cause."
A single chain of whys follows one path,
and most failures have several.

The cause and effect diagram,
often called a fishbone diagram,
widens the search before it narrows.
It is
"a visual way to look at cause and effect"
in which
"The problem or effect is displayed at the head or mouth of the fish"
and the team sorts candidate causes along the bones by category
[CMS 2014b][ref_cms_fishbone].
The diagram collects candidates.
It does not test them,
so each still needs the counterfactual test above.
That caution is the author's inference,
since the guide read for this article describes the diagram's purpose and states no limit.

### Human Factors Classification

Most mishaps involve a person,
and a report that stops at operator error has explained nothing.
The Human Factors Analysis and Classification System,
HFACS,
gives the investigator four levels to work through.
Its authors described it as follows.
"Drawing upon Reason's (1990) concept of latent and active failures, HFACS describes four levels of failure: 1) Unsafe Acts, 2) Preconditions for Unsafe Acts, 3) Unsafe Supervision, and 4) Organizational Influences"
[Shappell and Wiegmann 2000][research_shappell_wiegmann_2000].
The Department of Defense maintains its own version,
which names the levels acts,
preconditions,
supervision or leadership,
and organizational influences
[DoD 2022][mil_dod_hfacs_8_0].
NASA requires the analysis for its most serious classes,
and the N-Prime board organised its root causes along the four levels.

The defence guide makes two rules that keep the method honest.
The first forces the analysis below the surface.
"Every unsafe act will include at least one individual precondition."
The second ties every code to evidence.
The investigator must write a supporting statement for each code selected,
and
"If you have difficulty writing a supporting statement, then the code is likely not applicable or worthy of inclusion, or you need to revisit the evidence for that area of your investigation."
The four levels correspond closely to NASA's ladder.
The unsafe act is usually the proximate cause,
the precondition and the supervision are intermediate,
and the organizational influence is the root.
That correspondence is an inference,
and neither document states it.

## Voluntary and Confidential Reporting

The reports described so far are compulsory.
A second channel exists for what people would otherwise keep to themselves,
and it works only if reporting is safe.

The Aviation Safety Reporting System,
ASRS,
which NASA operates for the Federal Aviation Administration,
is the model.
It
"collects, analyzes, and responds to voluntarily submitted aviation safety incident reports in order to lessen the likelihood of aviation accidents"
[NASA ASRS Program Briefing][agency_nasa_asrs_summary].
Its protection is confidentiality.
"ASRS de-identifies reports before entering them into the incident database. All personal and organizational names are removed. Dates, times, and related information, which could be used to infer an identity, are either generalized or eliminated"
[NASA ASRS Confidentiality][agency_nasa_asrs_confidentiality].
A regulation backs the promise.
"The Administrator of the FAA will not use reports submitted to the National Aeronautics and Space Administration under the Aviation Safety Reporting Program (or information derived therefrom) in any enforcement action except information concerning accidents or criminal offenses which are wholly excluded from the Program"
[FAA 2026f][reg_14cfr_91_25].

NASA's internal channel uses a different protection.
"The NASA Safety Reporting System (NSRS) is an anonymous, voluntary and responsive reporting channel to notify NASA's upper management of your concerns about hazards"
[NASA Safety Reporting System][agency_nasa_nsrs].
A contractor stands between the reporter and the agency,
so that the agency never learns the name.
The two designs answer the same problem.
A confidential system knows the reporter and removes the identity.
An anonymous system never holds it.
The first can ask the reporter a follow-up question,
and the second cannot.

The European regulation on occurrence reporting takes a third course and makes the protection a legal duty of the employer,
as the section on civil aviation described.
All three rest on the reasoning behind the defence privilege.
People tell the truth about an event when nobody can use the telling against them.

## What the Standards Share

The regimes differ in vocabulary and agree in structure.
Eleven elements appear in most of them.
The list is the author's synthesis,
and each item names the sources behind it.

1. **Decide first whether the event is reportable.**
   The defence instruction asks whether harm occurred and whether anyone intended it.
   The FAA asks whether the event lay within the scope of the licence and meets the definition.
   NASA and the FAA both exempt damage that a programme declared in advance as a risk of the test.
2. **Classify by consequence, and count what nearly happened.**
   NASA's close call,
   the defence near miss,
   the serious incident of Annex 13
   and the FAA's high risk outcome all grade an event by its potential.
   ECSS resolves doubt upward.
   NASA and the defence instruction both allow the class to change as the facts arrive.
3. **Give the class a consequence.**
   NASA's class selects the investigator and the products of the report.
   The FAA dropped its proposed classes because nothing depended on them.
4. **Contain first and keep the evidence.**
   ECSS requires three immediate actions before any board meets.
   The FAA requires the operator to preserve data and physical evidence.
   The industry method begins with containment at step zero.
5. **Make a short first record quickly.**
   NASA allows 24 hours,
   the FAA five days for its written preliminary report,
   the European Union 72 hours,
   and Annex 13 thirty days for its preliminary report.
   Each first record answers who,
   what,
   when
   and where,
   and leaves why for later.
6. **Investigate to prevent, not to blame, and keep the investigator independent.**
   Annex 13,
   the two European regulations,
   NASA's directive
   and the safety board's regulation all say so in terms.
   The defence system separates the investigations to protect the candour of one of them.
7. **Write the report in a fixed order, with facts before analysis.**
   Annex 13 and NASA both run from facts through analysis and findings to recommendations.
   ICAO's manual forbids new facts in the analysis,
   and the Air Force report separates its facts from its opinion.
8. **State causes in layers, test each one, and say how sure the finding is.**
   NASA's ladder,
   the apparent and root causes of the industry standard
   and the four levels of the human factors system all layer the cause.
   NASA's overview and the five whys guide both test a cause by asking whether its removal would have prevented the outcome.
   ICAO's manual,
   NASA's overview
   and NASA's handbook all provide for a probable cause
   and for a cause that remains undetermined or unexplained.
9. **Trace every recommendation to a finding and every action to a recommendation.**
   NASA requires both,
   the second by a matrix.
   ICAO's manual asks that each recommendation name its addressee.
10. **Separate what is done to the item from what is done about the cause.**
    ECSS distinguishes the disposition from the corrective and the preventive action.
    NASA's handbook distinguishes remedial action,
    corrective action
    and recurrence control.
    The industry standard distinguishes correction,
    corrective action
    and preventive action.
    The ECSS alert and the last field of the FAA's preliminary report both ask who else is exposed.
11. **Close on stated conditions, by someone other than the person who did the work.**
    NASA uses three parties.
    ECSS closes on verified actions,
    completed tests
    and approved waivers,
    with the customer's endorsement for a major report.
    The defence handbook and NASA's handbook both allow a report to close without a fix or without a cause,
    on a documented and approved reason.

The regimes differ on three points that a designer of a report must decide.

| Regime and its unit of record | Severity scale | What closing requires |
|---|---|---|
| NASA mishap directive, the mishap or close call | Types A to D and close call | Actions implemented, verified by the safety office, closed by the appointing official |
| FAA commercial launch, the mishap | None | Final report accepted, then actions implemented before flight |
| Annex 13 and the safety board, the accident or incident | Three classes | Each recommendation answered within 90 days and tracked by status |
| ECSS, the nonconformance or anomaly | Major and minor | Actions verified, tests done, waivers approved |
| Japanese reliability standard, the anomaly or failure | Not examined | Change proven by test and preventive action proven effective |
| Defence failure reporting, the failure | None | Corrective action verified, or an approved reason for none |

The deepest difference is in the last column.
Some regimes close when the record shows that someone took the action.
Others close only when the record shows that the action worked.
The industry standard gives the two their names,
implementation verification and effectiveness verification.
The second is harder,
because the proof that a rare failure will not recur is the absence of an event.
The Japanese standard asks for proof by test,
and the reliability handbooks offer a statistical answer in the growth of the mean time between failures.

## A Report Structure for a Small Programme

A small programme cannot convene a board of five.
It can still keep the structure,
because the structure costs little and the standards themselves scale it down.
NASA requires five products of every report down to a close call,
and ICAO's manual describes abbreviated formats for small investigations.
The structure below is the author's consolidation for a programme of that size,
such as a campaign of simulated flights.
Each element names the standard it comes from.

### Before Any Report

- **State the triggers.**
  A written list says which events require a report.
  The FAA's definition is the model,
  a numbered list of outcomes that needs no judgement of severity.
  A loss of the vehicle,
  a loss of crew,
  a failure to complete the flight as planned
  and a malfunction of a safety-critical system are natural entries.
- **Declare expected losses in advance.**
  A test that the programme expects to destroy its article is not an incident
  when the programme wrote the risk down and accepted it before the test,
  after NASA's exemption and the FAA's.
- **Fix the classes and what each one costs.**
  Two or three classes suffice.
  Each should select something,
  such as the depth of the report or who must review it.
  The programme grades a near miss by the worst credible outcome,
  after the European risk classification scheme.

### The Report

| Part | Content | After |
|---|---|---|
| Identification | A unique number and revision, a title, the class, the date and time of the event with the time reference, the date of the report, the author and the status | ECSS, NASA |
| Summary | What happened, what was found and what was done, in a few sentences | NASA, the safety board |
| Sequence of events | A timeline from recorded data, separating events from conditions | NASA, Annex 13 |
| Configuration | The vehicle, the software version and the procedure in execution | ECSS |
| Outcome | What was lost or damaged, and what the event could credibly have become | Annex 13, NASA |
| Immediate actions | What was done to contain the event, and what evidence was preserved | ECSS, FAA |
| Analysis | The method used, and the candidates examined and eliminated | NASA, ICAO |
| Findings | The proximate cause, the deeper causes, the contributing factors and the observations, each with its evidence and its degree of certainty | NASA |
| Requirements affected | Each requirement, criterion or rule that was not met | ECSS, NASA |
| Actions | The correction, the corrective action and the preventive action, each with an owner, a date and the finding it answers | NASA, the industry standard |
| Read-across | Other vehicles, missions or procedures exposed to the same cause | ECSS, FAA |
| Closure | Who verified that each action was taken, how its effect was shown, who closed the report and when, or the approved reason for taking no action | ECSS, the Japanese standard, the defence handbook |
| Dissent | Any disagreement with the findings | NASA |

Four rules of writing go with the table.

- **Facts and analysis stay in separate parts.**
  The analysis introduces no new fact.
- **A finding is a sentence that concludes something from facts.**
  The fact is a measurement or an observation.
  The finding says what it means.
- **A cause names the function that failed, not only the person.**
  Operator error is where the analysis starts.
- **The report records an unknown cause as unknown.**
  The report names the most likely candidate and says that it is unproven.

### Classifying the Origin

A report in a simulated programme needs one field that the flight standards do not supply.
The fault may lie in the vehicle design,
in the control software,
in the procedure,
in the operator
or in the simulator itself.
The last is the analogue of a failure of test equipment.
It matters because a defect of the simulator calls for a different corrective action,
and because a programme that blames its tools too readily learns nothing.
The counterfactual test applies to this field as to any cause.
Would the outcome have been prevented had the simulator behaved as documented?
This field is the author's addition and comes from no standard read here.

### Strength of the Action

The system safety standard ranks risk reduction measures,
and the ranking serves as a check on a corrective action.
An action that removes the hazard by design ranks highest.
One that adds an engineered safeguard comes next,
then one that adds a warning,
and last one that adds a procedure or training.
For the gravest outcomes the standard advises against relying on the last kind alone.
A report whose only action is a reminder to take more care has probably stopped at the proximate cause.

## Epistemic State

**Facts and their sources.**
The requirements described above come from the documents themselves.
The author saved a copy of each,
confirmed its edition from its own cover or header,
and matched each quotation against the saved text.
The main exceptions follow.

- **Annex 13.**
  ICAO sells the Annex.
  The author transcribed the quotations from it by hand from a view-only copy
  that the Swiss Federal Office of Civil Aviation publishes.
  Several of them have an exact counterpart in ICAO's free manual
  or in the European regulation.
- **Scanned documents.**
  The defence handbook on failure reporting and the Ariane 5 inquiry report are scans.
  The author read their quotations from the page images
  and also matched the Ariane quotations against an unofficial transcription.
- **Sold standards.**
  The author did not read ISO 9001,
  AS9100
  or the industry standards on problem solving in full.
  The article relies on their owners' free guidance
  and on the free preview of the European standard on problem solving,
  which holds the definitions and the titles of the nine steps and not the text of the steps.
- **Defence documents.**
  The author read the defence instruction on mishaps as change 2 of June 2019,
  from a copy filed in a public docket.
  Later thresholds may have superseded its dollar figures.
  The author could not obtain the Air Force instructions on safety investigations and on accident investigation boards,
  and the account of the two investigations rests on the instruction,
  the statute
  and one public board report.
- **Tables.**
  The tables of classes and deadlines condense the source tables and are not quotations.
- **Public statements.**
  The corrective action counts for the two launch vehicles come from the FAA's page of dated statements,
  which the agency edits and from which old entries drop.

**Dates.**
The author read the documents in November 2026,
and several are in motion.
NASA's interim directive expires in July 2027.
Amendment 20 to Annex 13 becomes applicable in November 2028,
and the author did not read its text.
New editions of ISO 9000 and ISO 9001 appeared in 2026,
and the author did not read them.
A reader who relies on a particular clause should check the current issue.

**Inferences.**
The following are inferences,
and the text names each as one where it appears.

- That a coding error named as a root cause in 1999 would sit nearer the proximate end of NASA's present ladder.
- That NASA's contributing factor and the contributing factor of Annex 13 overlap without coinciding.
- That the four levels of the human factors system correspond to NASA's ladder.
- That NASA's directive requires proof of implementation and not of effectiveness.
  A search of its text for the word effective finds a duty to assess recommendations before their adoption
  and none to verify an action afterwards.
- That a fishbone diagram collects candidate causes without testing them.

**The author's view.**
The list of eleven shared elements,
the comparison table,
the report structure for a small programme,
the field for the origin of a fault
and the use of the system safety ranking as a test of corrective actions are the author's.
The author offers them as a reading of the standards,
open to disagreement on the evidence.
None of them is a requirement of any standard.

## Out of Scope

- **Other fields.**
  Nuclear,
  medical,
  rail
  and maritime investigation have their own standards,
  and the article draws on none of them
  beyond two guides on method from a health agency.
- **Other agencies.**
  The article covers NASA,
  the European standards
  and two Japanese standards.
  It does not cover the agencies of Russia,
  China
  or India.
- **Occupational safety law.**
  NASA's classes rest on the recordable injury of United States occupational safety regulation,
  which the article does not describe.
- **Software problem reporting.**
  Software assurance standards have their own rules for defect reports,
  and the article does not treat them.
- **Other methods of analysis.**
  Barrier analysis,
  change analysis
  and the systems-theoretic methods receive no treatment.
- **Law.**
  The article describes what regulations say and gives no legal advice.

## Conclusion

Space agencies and the aerospace industry write several kinds of report about things that go wrong,
under vocabularies that do not match.
NASA writes mishap and close call reports under one directive with five classes.
Civil aviation writes accident and incident reports to the format of Annex 13.
The FAA requires a commercial launch operator to report,
investigate
and prevent,
and prescribes no classes.
The European standards record nonconformances and anomalies and bring each before a board.
The reliability tradition records failures in a closed loop.

Beneath the vocabularies the regimes share a structure.
Each regime decides whether an event is reportable,
grades it by consequence,
makes a first record quickly,
investigates in order to prevent,
writes its facts before its analysis,
layers its causes,
ties its actions to its findings
and closes on stated conditions.
The differences that remain are real choices.
A severity class is worth having only where something depends on it.
A cause is worth naming only with its evidence and its degree of certainty.
And a regime can close a report when someone has taken the action
or when someone has shown that it worked,
which are different standards.
A small programme can adopt the whole structure at little cost,
provided it writes down its triggers,
its classes
and its closing rule before the first event that tests them.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 6 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 6, 6 are established and 0 are bespoke.
The reliability equations take test time in hours and failure rates in failures per hour. The fault tree equations take dimensionless probabilities, and the two gate equations hold only for independent input events.

**Equation 1, Duane Cumulative Failure Rate.**
The cumulative failure rate of a system under development falls as a power of total test time when fixes are incorporated.
[DoD 1998][mil_hdbk_338b]

$$
\lambda_{\Sigma} = \frac{F}{H} = K H^{-\alpha}
\tag{1}
$$

**Equation 2, Instantaneous Failure Rate Under the Duane Model.**
The failure rate the system shows now, found by differentiating the number of failures with respect to test time.
[DoD 1998][mil_hdbk_338b]

$$
\lambda_{\mathrm{I}} = \frac{dF}{dH} = \left( 1 - \alpha \right) K H^{-\alpha}
\tag{2}
$$

**Equation 3, Instantaneous Mean Time Between Failures.**
The current mean time between failures exceeds the cumulative value by a factor set by the growth rate.
[DoD 1998][mil_hdbk_338b]

$$
M_{\mathrm{I}} = \frac{M_{\mathrm{C}}}{1 - \alpha}
\tag{3}
$$

**Equation 4, Probability of an OR Gate With Independent Inputs.**
The probability that at least one of two independent input events occurs.
[Stamatelatos et al. 2002][agency_nasa_fault_tree_handbook_2002]

$$
P(Q) = P(A) + P(B) - P(A)\,P(B)
\tag{4}
$$

**Equation 5, Probability of an AND Gate With Independent Inputs.**
The probability that two independent input events both occur.
[Stamatelatos et al. 2002][agency_nasa_fault_tree_handbook_2002]

$$
P(Q) = P(A)\,P(B)
\tag{5}
$$

**Equation 6, Rare Event Approximation for the Top Event.**
The probability of the top event as the sum over minimal cut sets of the product of their basic event probabilities, accurate when those probabilities are small.
[Stamatelatos et al. 2002][agency_nasa_fault_tree_handbook_2002]

$$
P(T) \approx \sum_{i} \prod_{j \in C_{i}} P(b_{j})
\tag{6}
$$

### Notation

- $\lambda_{\Sigma}$, the cumulative failure rate
- $F$, the number of failures during the test time
- $H$, the total test hours
- $K$, a constant determined by circumstances
- $\alpha$, the growth rate
- $\lambda_{\mathrm{I}}$, the instantaneous failure rate
- $M_{\mathrm{C}}$, the cumulative mean time between failures
- $M_{\mathrm{I}}$, the instantaneous mean time between failures
- $P(A)$, the probability of input event $A$
- $P(B)$, the probability of input event $B$
- $P(Q)$, the probability of the output event of a gate
- $P(T)$, the probability of the top event
- $C_{i}$, minimal cut set $i$
- $P(b_{j})$, the probability of basic event $j$

## References

- [Reference, CEN 2018, EN 9136:2018, Aerospace Series, Root Cause Analysis and Problem Solving (9S Methodology), Preview][en_9136_2018]
- [Reference, CMS 2014a, Five Whys Tool for Root Cause Analysis][ref_cms_five_whys]
- [Reference, CMS 2014b, How to Use the Fishbone Tool for Root Cause Analysis][ref_cms_fishbone]
- [Reference, Columbia Accident Investigation Board 2003, Report Volume I][agency_caib_2003]
- [Reference, DoD 1995, MIL-HDBK-2155, Failure Reporting, Analysis and Corrective Action Taken][mil_hdbk_2155]
- [Reference, DoD 1998, MIL-HDBK-338B, Electronic Reliability Design Handbook][mil_hdbk_338b]
- [Reference, DoD 2011, MIL-HDBK-189C, Reliability Growth Management][mil_hdbk_189c]
- [Reference, DoD 2019, DoD Instruction 6055.07, Mishap Notification, Investigation, Reporting, and Record Keeping, Change 2][mil_dodi_6055_07]
- [Reference, DoD 2022, Human Factors Analysis and Classification System (DoD HFACS) Version 8.0][mil_dod_hfacs_8_0]
- [Reference, DoD 2023, MIL-STD-882E with Change 1, System Safety][mil_std_882e]
- [Reference, ECSS 2008, ECSS-E-ST-70C, Space Engineering, Ground Systems and Operations][ecss_e_st_70c]
- [Reference, ECSS 2012, ECSS-S-ST-00-01C, ECSS System, Glossary of Terms][ecss_s_st_00_01c_2012]
- [Reference, ECSS 2016, ECSS-Q-ST-10C Rev.1, Space Product Assurance, Product Assurance Management][ecss_q_st_10c_rev1]
- [Reference, ECSS 2018, ECSS-Q-ST-10-09C Rev.1, Space Product Assurance, Nonconformance Control System][ecss_q_st_10_09c_rev1]
- [Reference, ECSS 2023, ECSS-S-ST-00-01C Rev.1, ECSS System, Glossary of Terms][ecss_s_st_00_01c_rev1]
- [Reference, ESA 1996, Ariane 501, Presentation of Inquiry Board Report][esa_pr_33_1996]
- [Reference, European Commission 2020, Commission Delegated Regulation (EU) 2020/2034 on the Common European Risk Classification Scheme][eu_reg_2020_2034]
- [Reference, European Union 2010, Regulation (EU) No 996/2010 on the Investigation and Prevention of Accidents and Incidents in Civil Aviation][eu_reg_996_2010]
- [Reference, European Union 2014, Regulation (EU) No 376/2014 on the Reporting, Analysis and Follow-up of Occurrences in Civil Aviation][eu_reg_376_2014]
- [Reference, FAA 2019, Streamlined Launch and Reentry Licensing Requirements, Notice of Proposed Rulemaking, 84 FR 15296][reg_faa_nprm_2019]
- [Reference, FAA 2020, Streamlined Launch and Reentry License Requirements, Final Rule, 85 FR 79566][reg_faa_final_rule_2020]
- [Reference, FAA 2021, Advisory Circular 450.173-1, Part 450 Mishap Plan, Reporting, Response, and Investigation Requirements][reg_faa_ac_450_173_1]
- [Reference, FAA 2026a, 14 CFR 401.7, Definitions][reg_14cfr_401_7]
- [Reference, FAA 2026b, 14 CFR 450.173, Mishap Plan, Reporting, Response, and Investigation Requirements][reg_14cfr_450_173]
- [Reference, FAA 2026c, 14 CFR 450.175, Test-Induced Damage][reg_14cfr_450_175]
- [Reference, FAA 2026d, Compliance, Enforcement and Mishap][reg_faa_mishap_page]
- [Reference, FAA 2026e, General Statements][reg_faa_statements]
- [Reference, FAA 2026f, 14 CFR 91.25, Aviation Safety Reporting Program, Prohibition Against Use of Reports for Enforcement Purposes][reg_14cfr_91_25]
- [Reference, Genesis Mishap Investigation Board, Genesis Mishap Investigation Board Report, Volume I][agency_nasa_genesis_mib]
- [Reference, IAQG 2020, 9100:2016 Overview][iaqg_9100_2016_overview]
- [Reference, ICAO 2024a, Annex 13 to the Convention on International Civil Aviation, Aircraft Accident and Incident Investigation, Thirteenth Edition][icao_annex_13]
- [Reference, ICAO 2024b, Doc 9756, Manual of Aircraft Accident and Incident Investigation, Part IV, Reporting, Third Edition with Amendment 1][icao_doc_9756_part_iv]
- [Reference, ICAO 2026, Council, 237th Session, Fourth Meeting, Summary of Decisions, C-DEC 237/4][icao_c_dec_237_4]
- [Reference, ISO Documented Information, Guidance on the Requirements for Documented Information of ISO 9001:2015][iso_documented_information]
- [Reference, JAXA 2008, JMR-005A, Quality Assurance Program Standard][jaxa_jmr_005a]
- [Reference, JAXA 2012, JMR-004C, Reliability Program Standard][jaxa_jmr_004c]
- [Reference, Lions 1996, Ariane 5 Flight 501 Failure, Report by the Inquiry Board][esa_ariane_501_1996]
- [Reference, Mars Climate Orbiter Mishap Investigation Board 1999, Phase I Report][agency_nasa_mco_1999]
- [Reference, NASA 2003, Root Cause Analysis Overview][agency_nasa_rca_overview_2003]
- [Reference, NASA 2008, NASA-HDBK-8739.18, Procedural Handbook for NASA Program and Project Management of Problems, Nonconformances, and Anomalies][agency_nasa_hdbk_8739_18]
- [Reference, NASA 2019, NPD 7120.6A, Knowledge Policy for Programs and Projects][agency_nasa_npd_7120_6a]
- [Reference, NASA 2020, NPR 8621.1D, NASA Procedural Requirements for Mishap and Close Call Reporting, Investigating, and Recordkeeping][agency_nasa_npr_8621_1d]
- [Reference, NASA 2021, NPR 8735.2C, Hardware Quality Assurance Program Requirements for Programs and Projects][agency_nasa_npr_8735_2c]
- [Reference, NASA 2026, NID 8621.157, Requirements for Mishap and Close Call Reporting, Investigating, and Recordkeeping][agency_nasa_nid_8621_157]
- [Reference, NASA ASRS Confidentiality, Aviation Safety Reporting System, Confidentiality and Incentives to Report][agency_nasa_asrs_confidentiality]
- [Reference, NASA ASRS Program Briefing, Aviation Safety Reporting System, Program Briefing][agency_nasa_asrs_summary]
- [Reference, NASA Safety Reporting System][agency_nasa_nsrs]
- [Reference, NOAA N-Prime Mishap Investigation Board 2004, NOAA N-PRIME Mishap Investigation Final Report][agency_nasa_nprime_2004]
- [Reference, NTSB 2021, Commercial Space Investigations, Notice of Proposed Rulemaking, 86 FR 63324][reg_ntsb_nprm_2021]
- [Reference, NTSB 2025, Aviation Investigation Report AIR-25-04, In-Flight Separation of Left Mid Exit Door Plug, Alaska Airlines Flight 1282][ntsb_air_25_04]
- [Reference, NTSB 2026a, 49 CFR Part 830, Notification and Reporting of Aircraft Accidents or Incidents and Overdue Aircraft][reg_49cfr830]
- [Reference, NTSB 2026b, 49 CFR Part 831, Investigation Procedures][reg_49cfr831]
- [Reference, NTSB and FAA 2022, Memorandum of Agreement Concerning Commercial Space Mishap Investigations][reg_ntsb_faa_moa_2022]
- [Reference, NTSB Status Explanation, Safety Recommendations Database, Status Assignment Definitions][ntsb_status_explanation]
- [Reference, OIRA 2024, Unified Agenda, Spring 2024, RIN 3147-AA19, Commercial Space Investigations][reg_oira_3147_aa19]
- [Reference, Stamatelatos et al. 2002, Fault Tree Handbook with Aerospace Applications, Version 1.1][agency_nasa_fault_tree_handbook_2002]
- [Reference, Tolker-Nielsen 2017, ExoMars 2016, Schiaparelli Anomaly Inquiry][esa_schiaparelli_2017]
- [Reference, United States Code 2023, 10 U.S.C. 2254, Treatment of Reports of Aircraft Accident Investigations][mil_10usc2254]
- [Reference, USAF Accident Investigation Board, Aircraft Accident Investigation Board Report, UH-1N, F.E. Warren Air Force Base, 30 August 2023][mil_usaf_aib_uh1n_2023]
- [Related Post, Safety-Critical Software, Aerospace, Programming Languages, and Information Technology Co-Development: Safety-Critical Software][related_post_safety_critical_software]
- [Research, Shappell and Wiegmann 2000, The Human Factors Analysis and Classification System (HFACS), DOT/FAA/AM-00/7][research_shappell_wiegmann_2000]

[agency_caib_2003]: https://www.nasa.gov/wp-content/uploads/static/history/columbia/reports/CAIBreportv1.pdf
[agency_nasa_asrs_confidentiality]: https://asrs.arc.nasa.gov/overview/confidentiality.html
[agency_nasa_asrs_summary]: https://asrs.arc.nasa.gov/overview/summary.html
[agency_nasa_fault_tree_handbook_2002]: https://extapps.ksc.nasa.gov/reliability/Documents/Fault_Tree_Handbook_with_Aerospace_Applications_August_2002.pdf
[agency_nasa_genesis_mib]: https://www.nasa.gov/wp-content/uploads/2015/01/149414main_Genesis_MIB.pdf
[agency_nasa_hdbk_8739_18]: https://standards.nasa.gov/standard/NASA/NASA-HDBK-873918
[agency_nasa_mco_1999]: https://llis.nasa.gov/llis_lib/pdf/1009464main1_0641-mr.pdf
[agency_nasa_nid_8621_157]: https://nodis3.gsfc.nasa.gov/OPD_Docs/NID_8621_157_.pdf
[agency_nasa_npd_7120_6a]: https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=7120&s=6A
[agency_nasa_npr_8621_1d]: https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8621&s=1D
[agency_nasa_npr_8735_2c]: https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8735&s=2C
[agency_nasa_nprime_2004]: https://www.nasa.gov/wp-content/uploads/2015/01/65776main_noaa_np_mishap.pdf
[agency_nasa_nsrs]: https://sma.nasa.gov/sma-disciplines/nsrs
[agency_nasa_rca_overview_2003]: https://web.archive.org/web/20090116102710id_/http://www.hq.nasa.gov/office/codeq/rca/rootcauseppt.pdf
[ecss_e_st_70c]: https://ecss.nl/wp-content/uploads/standards/ecss-e/ECSS-E-ST-70C31July2008.pdf
[ecss_q_st_10_09c_rev1]: https://ecss.nl/standard/24183/
[ecss_q_st_10c_rev1]: https://ecss.nl/wp-content/uploads/2021/01/ECSS-Q-ST-10C-Rev.1(15March2016).pdf
[ecss_s_st_00_01c_2012]: https://ecss.nl/wp-content/uploads/standards/ecss-s/ECSS-S-ST-00-01C1October2012.pdf
[ecss_s_st_00_01c_rev1]: https://ecss.nl/wp-content/uploads/2023/10/ECSS-S-ST-00-01C_Rev.1(11October2023).pdf
[en_9136_2018]: https://cdn.standards.iteh.ai/samples/63973/5a1d65037fb243d09c36667064dc24c7/SIST-EN-9136-2018.pdf
[esa_ariane_501_1996]: https://esamultimedia.esa.int/docs/esa-x-1819eng.pdf
[esa_pr_33_1996]: https://www.esa.int/Newsroom/Press_Releases/Ariane_501_-_Presentation_of_Inquiry_Board_report
[esa_schiaparelli_2017]: https://sci.esa.int/documents/33431/35950/1567260317467-ESA_ExoMars_2016_Schiaparelli_Anomaly_Inquiry.pdf
[eu_reg_2020_2034]: https://eur-lex.europa.eu/eli/reg_del/2020/2034/oj
[eu_reg_376_2014]: https://eur-lex.europa.eu/eli/reg/2014/376/oj
[eu_reg_996_2010]: https://eur-lex.europa.eu/eli/reg/2010/996/oj
[iaqg_9100_2016_overview]: https://iaqg.org/wp-content/uploads/2020/01/9100-2016-Overview-5-13-2020.pdf
[icao_annex_13]: https://store.icao.int/en/annex-13-aircraft-accident-and-incident-investigation
[icao_c_dec_237_4]: https://www.icao.int/sites/default/files/about-icao/Council/Council%20Documentation/237/C-DECs/C.237.DEC.04.EN.pdf
[icao_doc_9756_part_iv]: https://www.icao.int/sites/default/files/airnavigation/AIG/9756_P4_cons_en.pdf
[iso_documented_information]: https://www.iso.org/files/live/sites/isoorg/files/archive/pdf/en/documented_information.pdf
[jaxa_jmr_004c]: https://sma.jaxa.jp/TechDoc/Docs/E_JAXA-JMR-004C_N1.pdf
[jaxa_jmr_005a]: https://sma.jaxa.jp/TechDoc/Docs/E_JAXA-JMR-005A_N4.pdf
[mil_10usc2254]: https://www.govinfo.gov/content/pkg/USCODE-2023-title10/html/USCODE-2023-title10-subtitleA-partIV-chap134-subchapII-sec2254.htm
[mil_dod_hfacs_8_0]: https://skybrary.aero/sites/default/files/bookshelf/34475.pdf
[mil_dodi_6055_07]: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/605507p.pdf
[mil_hdbk_189c]: https://everyspec.com/MIL-HDBK/MIL-HDBK-0099-0199/download.php?spec=MIL-HDBK-189C.034842.pdf
[mil_hdbk_2155]: https://everyspec.com/MIL-HDBK/MIL-HDBK-2000-2999/MIL-HDBK-2155_21714/
[mil_hdbk_338b]: https://everyspec.com/MIL-HDBK/MIL-HDBK-0300-0499/download.php?spec=MIL-HDBK-338B.015041.pdf
[mil_std_882e]: https://www.cto.mil/wp-content/uploads/2025/07/MIL-STD-882E-w_CHANGE-1.pdf
[mil_usaf_aib_uh1n_2023]: https://airandspaceforces.com/app/uploads/2024/11/30AUG23-AFGSC-FEW-AFB-AIB-Report_pdf.pdf
[ntsb_air_25_04]: https://www.ntsb.gov/investigations/AccidentReports/Reports/AIR2504.pdf
[ntsb_status_explanation]: https://www.ntsb.gov/safety/safety-recs/Pages/Status-Explanation.aspx
[ref_cms_fishbone]: https://www.cms.gov/medicare/provider-enrollment-and-certification/qapi/downloads/fishbonerevised.pdf
[ref_cms_five_whys]: https://www.cms.gov/medicare/provider-enrollment-and-certification/qapi/downloads/fivewhys.pdf
[reg_14cfr_401_7]: https://www.ecfr.gov/current/title-14/section-401.7
[reg_14cfr_450_173]: https://www.ecfr.gov/current/title-14/section-450.173
[reg_14cfr_450_175]: https://www.ecfr.gov/current/title-14/section-450.175
[reg_14cfr_91_25]: https://www.ecfr.gov/current/title-14/section-91.25
[reg_49cfr830]: https://www.ecfr.gov/current/title-49/part-830
[reg_49cfr831]: https://www.ecfr.gov/current/title-49/part-831
[reg_faa_ac_450_173_1]: https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_450.173-1.pdf
[reg_faa_final_rule_2020]: https://www.federalregister.gov/documents/2020/12/10/2020-22042/streamlined-launch-and-reentry-license-requirements
[reg_faa_mishap_page]: https://www.faa.gov/space/compliance_enforcement_mishap
[reg_faa_nprm_2019]: https://www.federalregister.gov/documents/2019/04/15/2019-05972/streamlined-launch-and-reentry-licensing-requirements
[reg_faa_statements]: https://www.faa.gov/newsroom/statements/general-statements
[reg_ntsb_faa_moa_2022]: https://www.faa.gov/sites/faa.gov/files/2022-09/NTSB-FAA-Commercial-Space-MOA.pdf
[reg_ntsb_nprm_2021]: https://www.federalregister.gov/documents/2021/11/16/2021-24766/commercial-space-investigations
[reg_oira_3147_aa19]: https://www.reginfo.gov/public/do/eAgendaViewRule?pubId=202404&RIN=3147-AA19
[related_post_safety_critical_software]: {% post_url 2026-07-21-safety_critical_software %}
[research_shappell_wiegmann_2000]: https://rosap.ntl.bts.gov/view/dot/15397/dot_15397_DS1.pdf
