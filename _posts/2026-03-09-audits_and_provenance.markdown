---
layout: post
mathjax: true
comments: true
title: "Audits and Provenance"
date:   2026-03-09 09:00:00 +0000
categories: philosophy management engineering
---

<!-- A223 -->
<script>console.log("A223");</script>

An audit is a structured verification pass that produces reviewable evidence about a property of a system, a record, or a process. The property is one that the auditee cannot credibly self-attest without third-party review. The pass is bounded by a scope, follows a defined procedure, and terminates in findings that identify what conforms, what does not conform, and what requires remediation. Engineering audits verify system correctness, security, and quality. Documentation audits verify that written artifacts are complete, current, and accurate. Compliance audits verify conformance with regulatory, contractual, or internal policy requirements. Provenance and audit trails are not a fourth audit category. They are the substrate that makes the first three possible.

This article treats audits at the class level, identifies the properties shared across categories, walks the three principal audit categories with worked examples, and treats provenance as the load-bearing infrastructure that determines whether any of the three categories can be conducted at all. The framing matters because organizations frequently treat audits as adversarial interruption or bureaucratic overhead. Both framings are category mistakes. Audits are productive verification with the same cognitive shape as peer review in science, code review in software, or referee reports in mathematics. Provenance is the record-keeping discipline that all such verification depends upon.

## What All Audits Share

Every audit exhibits four properties. The properties hold across engineering, documentation, and compliance instances and do not depend on the domain.

**Scope and procedure.** The audit begins with a written scope naming what is under review and what is not. The procedure defines what evidence will be examined, in what order, and against what criteria. An audit without a written scope is not an audit. It is a conversation. An audit without a defined procedure produces findings that cannot be reproduced by another auditor with the same evidence, which defeats the reason for auditing in the first place.

**Independent review.** The auditor is separate from the auditee. Full independence means the auditor has no reporting relationship, financial interest, or personal stake in the auditee's outcome. Practical independence often falls short of the full standard but must preserve enough separation that the auditor can produce adverse findings without adverse consequence. An audit conducted by the auditee's manager is not an audit. It is an evaluation. The distinction is not pedantic. The evaluator has authority over the evaluee's future employment. The auditor does not. The theoretical treatment of audit quality by [DeAngelo][research_deangelo_audit_quality] establishes that quality is jointly determined by the probability of finding a breach and the probability of reporting it. Both depend on independence, and both degrade when independence is compromised.

**Evidence artifacts.** The audit produces reviewable artifacts. Working papers document what was examined and what was concluded. Findings identify instances of conformance and non-conformance with citations to the evidence. A summary report communicates the findings to the auditee and to the audit's client. All three artifacts survive after the audit closes. A second auditor should be able to review the artifacts and reach substantially similar findings from the same evidence.

**Findings, remediation, and re-verification.** Findings are actionable. Each non-conformance names a fact, a criterion it fails against, and a remediation path. The audit closes when remediation is agreed and, in the case of high-severity findings, when re-verification confirms the remediation was applied. Audits that produce findings without remediation are theater. Audits whose remediation is never verified are half-completed workflows.

Any activity omitting one of the four properties is something other than an audit. Peer conversations, informal reviews, project retrospectives, and casual testing all have value but should not be labeled audits. The naming discipline matters because organizations that conflate the categories end up with neither the benefits of formal audit nor the benefits of informal review.

## Engineering Audits

Engineering audits verify properties of technical systems that cannot be established by casual inspection. Three sub-categories dominate practice.

**Correctness audits.** Formal code review, design review, mathematical proof review, and formal verification of software or hardware. The scope names a system component and the property to verify. Evidence is the source code, the specification, the design documents, and the reasoning trace. Independent reviewers examine the artifacts against the criteria and produce findings. Correctness audits are the modern instantiation of the peer review process that mathematics and the natural sciences have run for centuries. Empirical work by [Bacchelli and Bird][research_bacchelli_code_review] on modern code review at industrial scale documents that the practice produces value beyond defect discovery, including knowledge transfer, alternative solutions, and shared understanding of the codebase. The multiple-value observation matters because it explains why code review persists as an engineering discipline even where defect-discovery rates are modest.

**Security audits.** Threat modeling review, penetration testing, static-analysis output review, incident post-mortems, and access-control audits. Scope names a system boundary and a threat model. Evidence includes system configuration, code, network topology, access logs, and prior incident records. Findings identify vulnerabilities, misconfigurations, and control gaps. Security audits produce their most valuable output when adversarial in orientation. The auditor is trying to find vulnerabilities that the auditee missed, and the auditee's cooperation is necessary but not sufficient.

**Quality audits.** Test-coverage review, defect-rate review, performance-envelope verification, reliability metric review, and change-management-process audits. Scope names a quality attribute and a target level. Evidence includes test results, defect databases, performance measurements, and process records. Findings identify gaps between measured quality and target quality, and gaps between claimed process and actual practice.

The three sub-categories compose. A system that passes correctness review may still fail security review if the correctness criterion did not address adversarial inputs. A system that passes both may fail quality review if performance in production degrades under load. Engineering audits at the full level of assurance combine all three, staggered across the development lifecycle rather than concentrated at release time.

## Documentation Audits

Documentation audits verify that written artifacts are complete, current, and accurate. They apply to specifications, design documents, user manuals, operational runbooks, decision records, meeting notes, and architecture design records.

**Completeness.** Does the documentation cover every load-bearing decision and every non-obvious design choice? Are gaps identified as gaps rather than left silent?

**Currency.** Do the documented behaviors match the current state of the system? When the system changed, was the documentation updated in the same change set, or does it describe a version that no longer exists?

**Accuracy.** Where documentation makes factual claims, are those claims correct against the system as it currently operates? A documented interface that does not match the implementation is worse than no documentation, because it produces false confidence.

Documentation audits interact with the other categories. A correctness audit is easier when the specification is complete. A security audit is easier when threat models are documented and current. A compliance audit becomes possible only when the compliance-relevant documentation is accurate.

Prior corpus articles on [documentation-oriented workflow][related_post_bidirectional_agentic] and [Markdown as a specification language][related_post_markdown_spec] describe the documentation practices that make documentation audits tractable when they arrive.

## Compliance Audits

Compliance audits verify that an organization conforms with an external requirement. The requirement can be regulatory, contractual, or internal-policy in origin.

**Regulatory compliance.** Financial reporting under Sarbanes-Oxley for United States public companies, data-protection compliance under the General Data Protection Regulation for European Union data subjects, protected-health-information compliance under the Health Insurance Portability and Accountability Act for United States medical records, payment-card processing compliance under the Payment Card Industry Data Security Standard for organizations that handle payment cards. Regulatory audits have legal force. Non-conformance can result in penalties, sanctions, or loss of the license to operate.

**Contractual compliance.** Service Organization Controls audit under the Trust Services Criteria maintained by the American public-accountancy standard-setting body, information-security-management audit under ISO 27001, and other framework-based audits that customers require of their suppliers. Contractual audits result in a report that the auditee shares with customers. Non-conformance can result in loss of the contract, but not typically in legal penalty.

**Internal policy compliance.** Verification that an organization's actual practice matches its own documented policies for change management, access control, incident response, procurement, or ethics. Internal audits are conducted by an internal audit function that reports to an audit committee rather than to line management. The independence is imperfect but structured to preserve the audit's integrity within the organization.

Compliance audits examine controls, the procedures the organization has adopted to satisfy the requirement. The audit does not directly examine the underlying property. It examines whether the controls that produce the property are designed, implemented, operating, and monitored. A compliance-passed system is not necessarily a secure or correct system. It is a system whose controls appear designed and operating to satisfy the framework. The distinction between compliance-passing and property-holding is a common source of organizational confusion. The economic mechanism behind the gap is worked out in [Anderson's foundational analysis of security economics][research_anderson_security_economics], which documents that market failures and misaligned incentives produce systems that pass compliance requirements while failing on the underlying properties the compliance framework was designed to protect.

## Provenance and Audit Trails

Provenance is the recorded history of how an artifact came to be. An audit trail is a form of provenance record that documents actions taken by identifiable actors against identifiable resources at identifiable times, sequenced in a way that can be reconstructed after the fact.

Provenance is the substrate that makes all three audit categories possible. An engineering audit that cannot trace a bug back to the commit that introduced it, the review that missed it, and the specification that permitted it produces findings the auditee cannot act upon. A documentation audit that cannot trace a documented claim back to the decision record that established it cannot determine whether the claim is current. A compliance audit that cannot show the operating log for a control cannot demonstrate that the control was actually operating.

Let $N_R$ denote the count of state transitions that produced audit-ready records during the audit scope's time window, and let $N_T$ denote the total number of state transitions in the same window. The provenance completeness $p$ is the ratio.

$$
p = \frac{N_R}{N_T}
$$

Audit feasibility requires $p$ close to unity. A system with $p = 1$ produces perfect audit evidence. A system with $p = 0$ produces none. Practical systems fall between, and where $p$ falls determines what audits are possible.

The formal treatment of provenance originated with [Buneman, Khanna, and Tan][research_buneman_provenance], who distinguished "why" provenance, meaning which inputs contributed to a value, from "where" provenance, meaning which source location produced it. Subsequent survey work by [Simmhan, Plale, and Gannon][research_simmhan_provenance_survey] extended the taxonomy across scientific computing practice and cataloged provenance systems by the properties they preserve. The four properties treated below map onto the accepted taxonomy.

**Chain of custody.** Every provenance-producing record identifies who did what, to which resource, at what time, and why. The chain of custody is complete when every state transition from the resource's creation to the current moment is documented by an entry made contemporaneously with the action.

**Immutability.** Once written, provenance records cannot be altered without leaving evidence of the alteration. Cryptographic signatures, append-only logs, git commit chains, and blockchain-style hash-chained records all achieve immutability by different means. The choice among them depends on the threat model. A system whose provenance can be silently rewritten produces no audit evidence.

**Reconstructibility.** Given the provenance records, an auditor should be able to reconstruct the state of the resource at any past moment. Reconstructibility distinguishes provenance from mere logging. A log that captures events but does not permit state reconstruction fails the primary provenance test.

**Retention.** Provenance records must survive as long as the resource's audit scope extends. Financial records under Sarbanes-Oxley must survive seven years. Data-protection records under General Data Protection Regulation must survive as long as the underlying data. Software design records should survive as long as the software runs. Retention rules that permit destruction of provenance records before the audit scope ends convert every future audit into an impossible task.

Where provenance fails, all three audit categories fail together. Where provenance is maintained, all three become tractable. Investments in provenance infrastructure produce audit-readiness as a byproduct rather than as a scramble at audit time.

## Common Failure Modes

Audits fail in characteristic ways. The failure modes recur across categories.

**Cargo-cult checklists.** The audit becomes a checklist exercise divorced from the underlying property being verified. Checkboxes are ticked, nothing is examined. The failure mode is often introduced when an audit expands to a scope the auditor cannot examine substantively within the time budget.

**Adversarial auditee posture.** The auditee treats the audit as a threat and minimizes cooperation. Requested evidence is delayed or provided in unusable form. Findings are contested procedurally rather than substantively. The auditor's productivity collapses to the rate at which the auditee cooperates, which may be arbitrarily slow.

**Scope creep.** The audit expands beyond its original scope during execution, either at the client's direction or at the auditor's initiative. Scope creep produces audits that never end, findings that never remediate, and audit fatigue at the auditee.

**Retroactive documentation.** The auditee writes documentation immediately before the audit rather than during the work that the documentation supposedly describes. The documentation matches the audit criteria but not the actual practice. Retroactive documentation is a symptom of missing provenance infrastructure and a cause of misleading audit outcomes.

**Findings without remediation.** The audit produces findings, closes out, and no remediation is undertaken. The next audit produces the same findings again. The audit is theater.

**Single-auditor bias.** A single auditor's blind spots become the audit's blind spots. Formal audit standards require independent quality review of the auditor's work precisely because single-auditor bias is universal.

**Audit fatigue.** Frequent audits without corresponding investment in audit-ready infrastructure produce cynicism at the auditee and burnout at the auditor. Both parties eventually treat the audit as ceremony rather than substance.

## Implications for Organizations

Organizations that treat audits as productive verification rather than adversarial interruption make different structural choices.

They invest in provenance infrastructure so that every load-bearing action produces an audit-ready record contemporaneously with the action. Let $c$ denote the marginal cost per action of producing an audit-ready record at the time of the action, and let $C_R$ denote the retrofit cost of reconstructing an equivalent record after the fact. For a system with $N$ accumulated actions, contemporaneous investment scales linearly as $c N$. Retrofit is a fixed one-time cost paid at audit time. The observed inequality across mature audit engagements is

$$
c N \ll C_R
$$

by wide margins, and $c$ is small per action. The total cost of ordinary work is dominated by the retrofit cost imposed on organizations that lack the infrastructure, not by the cumulative marginal cost of maintaining it.

They organize documentation so that the record-keeping practices needed for audits are the same as the record-keeping practices needed for the work itself. When documentation exists as a byproduct of work, audits examine the same records the workers already produce. When documentation exists as an audit-specific artifact, workers produce two overlapping records and one is always stale.

They separate the internal audit function from line management so that independent review can produce adverse findings without adverse consequence. Internal audit functions that report to the audit committee of the board rather than to the executive team are the structural mechanism.

They calibrate audit frequency to the rate of change of the underlying system. Let $\lambda$ denote the system's change rate in changes per unit time, and let $T$ denote the interval between audits. The number of changes accumulated between audits is $\lambda T$. Effective audit coverage requires the accumulated changes to remain bounded by the auditor's per-audit review capacity $K$.

$$
\lambda T \leq K
$$

A stable system with small $\lambda$ can accommodate long $T$ and remain well-covered. A system under rapid change with large $\lambda$ requires either shorter $T$ or an audit style that examines change management as the object of audit rather than the underlying state itself. Prior corpus discussion of [engineering pace and mission-criticality tradeoffs][related_post_fast_vs_critical] establishes the frequency-versus-scrutiny tradeoff in a related setting.

They treat audit findings as work rather than as noise. A finding that identifies a real issue creates work. The work should be planned, resourced, and tracked to completion. Findings that are dismissed produce the theater failure mode described above.

## Prior Art

The audit practice has multiple mature traditions.

Financial audit under Sarbanes-Oxley in the United States is codified in the Public Company Accounting Oversight Board's audit standards. The Institute of Internal Auditors publishes International Standards for the Professional Practice of Internal Auditing. Both traditions concentrate on control-based audit reasoning.

Security audit frameworks include the National Institute of Standards and Technology's SP 800-series risk management framework, the Trust Services Criteria for SOC 2 reports, and the ISO 27001 information security management standard. Each specifies control frameworks and audit procedures for particular threat surfaces.

Software correctness audit draws on the formal-methods tradition and on the peer-review discipline of code review. The [Common Weakness Enumeration][ref_cwe] and [Common Vulnerabilities and Exposures][ref_cve] catalogs provide standardized taxonomies that engineering security audits reference.

Provenance research in scientific computing produced the [W3C PROV specification][ref_w3c_prov], which formalizes the entity-activity-agent model of provenance records. The specification underlies modern reproducibility infrastructure in computational science.

## Conclusion

Audits are structured verification passes that produce reviewable evidence artifacts. Four properties define the class. Those properties are written scope and procedure, independent review, evidence artifacts, and findings with remediation. Three principal categories instantiate the class. The categories are engineering audits over technical systems, documentation audits over written artifacts, and compliance audits over conformance with external requirements. Provenance is the substrate that all three categories depend upon, and organizations that invest in provenance produce audit-readiness as a byproduct of ordinary work.

The organizational framing that treats audits as adversarial interruption is a category mistake. The audit's cognitive shape is that of peer review, code review, or referee report in mathematics, all of which are productive verification within their domains. Organizations that internalize the framing structure their record-keeping and management so that audit-readiness follows from doing the work rather than from separately preparing for the audit.

## References

- [Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy][ref_aicpa_tsc]
- [MITRE, Common Vulnerabilities and Exposures][ref_cve]
- [MITRE, Common Weakness Enumeration][ref_cwe]
- [GDPR, General Data Protection Regulation, official portal][ref_gdpr]
- [The Institute of Internal Auditors, International Standards for the Professional Practice of Internal Auditing][ref_iia_standards]
- [ISO 27001, Information Security Management Systems, Requirements][ref_iso_27001]
- [NIST SP 800-53, Security and Privacy Controls for Information Systems and Organizations][ref_nist_800_53]
- [PCAOB, Public Company Accounting Oversight Board, standards library][ref_pcaob_standards]
- [W3C, PROV Overview, An Overview of the PROV Family of Documents][ref_w3c_prov]
- [Related Post, Bidirectional Agentic Workflow][related_post_bidirectional_agentic]
- [Related Post, Fast-Moving Versus Mission-Critical Engineering][related_post_fast_vs_critical]
- [Related Post, Markdown as a Specification Language for Agentic Workflows][related_post_markdown_spec]
- [Anderson, Ross, Why Information Security is Hard, An Economic Perspective, Annual Computer Security Applications Conference 17, 2001][research_anderson_security_economics]
- [Bacchelli, Alberto and Bird, Christian, Expectations, Outcomes, and Challenges of Modern Code Review, International Conference on Software Engineering 35, 2013][research_bacchelli_code_review]
- [Buneman, Peter, Khanna, Sanjeev, and Tan, Wang-Chiew, Why and Where, A Characterization of Data Provenance, International Conference on Database Theory 8, 2001][research_buneman_provenance]
- [DeAngelo, Linda Elizabeth, Auditor size and audit quality, Journal of Accounting and Economics 3, 1981][research_deangelo_audit_quality]
- [Simmhan, Yogesh L., Plale, Beth, and Gannon, Dennis, A survey of data provenance in e-Science, SIGMOD Record 34, 2005][research_simmhan_provenance_survey]

[ref_aicpa_tsc]: https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022
[ref_cve]: https://www.cve.org/
[ref_cwe]: https://cwe.mitre.org/
[ref_gdpr]: https://gdpr-info.eu/
[ref_iia_standards]: https://www.theiia.org/en/standards/2024-standards/global-internal-audit-standards/
[ref_iso_27001]: https://www.iso.org/standard/27001
[ref_nist_800_53]: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
[ref_pcaob_standards]: https://pcaobus.org/oversight/standards
[ref_w3c_prov]: https://www.w3.org/TR/prov-overview/
[related_post_bidirectional_agentic]: {% post_url 2026-02-06-bidirectional_agentic_workflow %}
[related_post_fast_vs_critical]: {% post_url 2026-02-24-fast_moving_versus_mission_critical_engineering %}
[related_post_markdown_spec]: {% post_url 2026-02-08-markdown_as_a_specification_language %}
[research_anderson_security_economics]: https://doi.org/10.1109/ACSAC.2001.991552
[research_bacchelli_code_review]: https://doi.org/10.1109/ICSE.2013.6606617
[research_buneman_provenance]: https://doi.org/10.1007/3-540-44503-X_20
[research_deangelo_audit_quality]: https://doi.org/10.1016/0165-4101(81)90002-1
[research_simmhan_provenance_survey]: https://doi.org/10.1145/1084805.1084812
