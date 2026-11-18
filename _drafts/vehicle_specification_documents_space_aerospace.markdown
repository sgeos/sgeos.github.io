---
layout: post
mathjax: true
comments: true
title: "Vehicle Specification Documents in Space Agencies and Aerospace"
date: 2026-11-10 09:00:00 +0000
categories: aerospace engineering space
---

<!-- A392 -->
<script>console.log("A392");</script>

Space agencies and the aerospace industry never describe a launch vehicle or a spacecraft in one document.
They describe it in a family of documents,
each with a fixed form and a fixed owner.
This article surveys that family.
It covers the specification that states what the vehicle must do,
the records that fix its configuration,
the lists that name its parts and materials,
the report that accounts for its mass,
the documents that control its interfaces,
the documents that describe its software as delivered,
and the scales by which an agency states how mature and how proven a design is.
It then examines what operators and agencies publish about real vehicles.

The survey finds four things.
The first is that the vocabularies do not match,
and that several common beliefs about them do not survive a reading of the documents.
The binding systems engineering directive of the National Aeronautics and Space Administration,
NASA,
never names a functional or an allocated baseline.
The European standard on configuration management does not define a configuration item.
The United States defence standard on technical data packages does not define a parts list.
The second is that no document read here defines a bill of materials.
The function exists in every regime,
and several lists share it.
The third is that published descriptions of vehicles leave out as much as they state,
and that one current user's guide gives two values for the same thrust.
The fourth is that the practices share a structure beneath the vocabularies,
which a small programme can adopt.

The article has three parts.
The first describes the documents by type,
from the specification through configuration,
parts lists,
mass,
interfaces,
verification,
software
and readiness.
Each section sets NASA and United States defence practice beside the European standards.
The second describes published vehicle documents as worked examples,
namely launch vehicle user's guides,
a flight manual of the Apollo programme,
a current NASA reference guide,
engine data sheets
and satellite bus data sheets.
The third draws out what the practices share
and consolidates it into a specification sheet for one vehicle.
The description of each document rests on the document itself.
The synthesis and the sheet are the author's,
and the [Epistemic State](#epistemic-state) section separates the two.

The article does not teach systems engineering,
and it is not a source of data on any vehicle.
Every number that it quotes from a published document illustrates a form,
and each carries the revision of the document that prints it.

## Kinds of Document

Seven kinds of document recur.

- **The specification.**
  It states the requirements on a product and the means of verifying each one.
- **The design description.**
  It states what the product is,
  in drawings,
  lists
  and descriptions.
- **The configuration record.**
  It names the items under control,
  the approved documents that define each one,
  and the state of each unit as built.
- **The parts and materials lists.**
  They name the parts and materials that make up the product.
- **The budget or status report.**
  It accounts for a resource such as mass or power against a limit.
- **The interface document.**
  It fixes what two parties must each provide where their products meet.
- **The published description.**
  A user's guide,
  a flight manual,
  a reference guide
  or a data sheet tells an outside reader what the vehicle is and what it can do.

The words for these documents vary by regime,
and the same word can name different things.

| Term | Used by | Sense |
|---|---|---|
| Specification | NASA, defence, European standards | A document that states requirements and the means of verifying them |
| Technical requirements specification | European standards | The customer's specification for a product |
| Specification sheet | Defence standard | The requirements unique to one model within a family covered by a general specification |
| Technical data package | Defence standard, NASA | The authoritative technical description of an item |
| Technical data package | European standard | An archive file of documents and metadata for exchange between information systems |
| Design definition file | European standards | The collected documents that define the design as it stands |
| Configuration item | All three | A product, or part of one, designated for separate control |
| Baseline | All three | An approved description at a point in time, against which change is controlled |
| Parts list | Defence handbook, NASA | A tabulation of the parts and bulk materials of an item |
| Declared list | European standards | A list of the components, materials, mechanical parts or processes of one item, with approval status |
| Bill of materials | NASA directive and a superseded defence handbook, once each | Not defined in any document read |
| Data sheet, specification sheet | Manufacturers | A short document that tabulates the parameters of a product |
| User's guide, user's manual | Launch operators | A planning document for customers of a launch service |

Three rows deserve a remark.
The first is the specification sheet.
A manufacturer uses the phrase for a brochure of parameters,
and the United States defence standard on specifications already gives it a narrower meaning
[DoD 2020a][mil_std_961e].
"A document that specifies requirements and verifications unique to a single style, type, class, grade, or model that falls within a family of products described under a general specification."
A programme that names its own template a specification sheet should say which sense it intends.

The second is the technical data package.
The defence standard on the subject defines it as
"The authoritative technical description of an item."
[DoD 2018][mil_std_31000b].
The European standard on configuration management defines the same phrase as a
"ZIP file containing structured collection of files with their related metadata, to be exchanged between information systems"
[ECSS 2009c][ecss_m_st_40c_rev1].
The first is a body of content and the second is a container.

The third is the bill of materials.
A search of the saved text of every document read for this article finds the phrase in two of them.
The superseded defence handbook on configuration management lists it among its abbreviations
[DoD 2001][mil_hdbk_61a].
NASA's systems engineering directive names it once,
among the entrance criteria of the review that precedes production
[NASA 2023a][agency_nasa_npr_7123_1d].
"The bill of materials is available and critical parts identified."
Neither document defines it.
The search could not cover three European documents whose files forbid the extraction of text,
so the finding for those three rests on the pages the author read.
The section on [the bill of materials](#the-bill-of-materials) shows where the function lives.

## The Specification

NASA's directive defines a specification as
"A document or data that prescribes, in a complete, precise, verifiable manner, the requirements, design, behavior, or characteristics of a system or system component."
The defence standard on specifications defines it as
"A document prepared to support acquisition that describes essential technical requirements for materiel and the criteria for determining whether those requirements are met."
The two agree on the essential pair.
A specification states requirements,
and it states how to tell whether the product meets them.

### Six Fixed Sections

The United States Department of Defense,
DoD,
fixes the form of a specification in MIL-STD-961E,
whose current text carries Change 4 of 16 July 2020
[DoD 2020a][mil_std_961e].
The author read it,
like every military document cited here,
in a copy from a mirror site and not from the official index.
Its central rule is that
"specifications shall contain six numbered sections, titled and numbered as shown below."

| Section | Title | What it holds |
|---|---|---|
| 1 | Scope | The name of the item and an abstract of what the specification covers |
| 2 | Applicable documents | Only the documents that sections 3 and 4 cite |
| 3 | Requirements | Every requirement the item must meet to be acceptable |
| 4 | Verification | Every inspection that shows conformance to section 3 |
| 5 | Packaging | A standard sentence that defers packaging to the contract |
| 6 | Notes | Intended use, acquisition requirements, definitions and supersession data |

A section with nothing to say stays in place,
and the standard supplies its text.
"This section is not applicable to this specification."
The numbering therefore never changes,
and a reader always finds the requirements in section 3 and their verification in section 4.

Three rules govern what may go where.
The first keeps requirements out of the scope.
"The scope shall not contain requirements."
The second ties each requirement to its proof.
"Each requirement shall be stated in such a way that an objective verification can be defined for it."
The standard adds that each requirement should carry a cross-reference to its verification,
and it allows four means.
"Verification may be accomplished by analysis, demonstration, examination, testing, or any combination thereof."
The third keeps requirements out of the notes.
"Section 6 is not contractually binding."

### Kinds of Specification

The same standard sorts specifications on two axes.
The first axis is what a requirement may say.
A performance specification is
"A specification that states requirements in terms of the required results with criteria for verifying compliance, but without stating the methods for achieving the required results."
A detail specification is
"A specification that specifies design requirements, such as materials to be used, how a requirement is to be achieved, or how an item is to be fabricated or constructed."
A document that mixes the two counts as a detail specification.

The second axis is how widely the document applies.
What the standard calls a defense specification serves many programmes.
A specification written for one programme is,
in the standard's own spelling,
program-unique,
and it takes one of five types,
namely system,
item,
software,
material
and process.
Its scope adds a short description of the entity and names its immediately subordinate elements.
It carries two approval blocks,
one for the design activity that submits it
and one for the government official who approves it.
The second block ties the document to configuration control.
"The authorized government approval block shall indicate whether the program-unique specification is authorized for use as a functional, allocated, or product baseline."

### The European Technical Requirements Specification

The European Cooperation for Space Standardization,
ECSS,
calls its counterpart the technical requirements specification
and abbreviates it as TS.
The governing standard is ECSS-E-ST-10-06C of 6 March 2009
[ECSS 2009a][ecss_e_st_10_06c].
It defines the document by its owner,
as the
"document by which the customer establishes the intended purpose of a product, its associated constraints and environment, the operational and performances features"
of that product.
It also states what the document is for.
"The TS is the technical reference for the qualification of the design and for the acceptance of the end product."

A normative annex fixes seven sections.

| Section | Title | What it holds |
|---|---|---|
| 1 | Introductions | Purpose, objective, content and the reason for preparing the document |
| 2 | Applicable and reference documents | Both lists |
| 3 | User's need presentation | The need, the related products and the identified interfaces |
| 4 | Selected concept and product presentation | The concept, the expected architecture and the principles of operation |
| 5 | Life profile description | The situations of the product's life in order of time |
| 6 | Environment and constraints description | The environments and constraints of each situation |
| 7 | Requirements | Every technical requirement |

The European document therefore describes the need,
the concept
and the life of the product before it states a requirement.
The defence document goes from scope and references straight to requirements.
That comparison is the author's inference from the two outlines.

The standard sorts requirements into twelve types,
namely functional,
mission,
interface,
environmental,
operational,
human factor,
logistics support,
physical,
product assurance induced,
configuration,
design
and verification.
Mass is a physical requirement,
and the standard's own example is
"The product shall have a mass of (30 ± 0,1) kg"
with the tolerance stated.
Margins fall under design requirements,
which cover
"the imposed design and construction standards such as design standards, selection list of components or materials, interchangeability, safety or margins."

The standard also sets rules for the document as a whole.
An entity must be responsible for it.
Each cited document carries its revision identifier.
The specification is under configuration management.
It holds technical requirements only.
"Technical requirements specifications shall only include technical requirements and exclude requirements such as cost, methods of payment, quantity required, time or place of delivery."
The standard names no approving signature.
The author infers that approval follows the baselines described in the next section,
since the standard defines the document as the customer's and puts it under configuration control.

### A Well-Formed Requirement

The European standard gives the fullest rules found for a single requirement.
Ten headings carry them,
and the core of each is one sentence.

- **Performance.**
  "Each technical requirement shall be described in quantifiable terms."
- **Justification.**
  "Each technical requirement should be justified."
- **Traceability.**
  Every requirement traces backwards to its source and forwards to what derives from it.
- **Ambiguity.**
  "The technical requirements shall be unambiguous."
- **Uniqueness.**
  "Each technical requirement shall be unique."
- **Identifiability.**
  "A unique identifier shall be assigned to each technical requirement."
- **Singularity.**
  "Each technical requirement shall be separately stated."
- **Completeness.**
  "A technical requirement shall be self-contained."
- **Verification.**
  "A technical requirement shall be verifiable using one or more approved verification methods."
- **Tolerance.**
  "The tolerance shall be specified for each parameter/variable."

The standard then bans 27 terms from any requirement,
among them the words adequate,
sufficient,
typical,
rapid
and suitable,
and the phrases as far as possible and state of the art.
A requirement that the vehicle shall have adequate margin fails twice,
once against the list and once against the rule that a requirement be quantifiable.

Both regimes prefer a requirement that states a result.
The European rule reads as follows.
"Technical requirements should be stated in performance or “what-is-necessary” terms, as opposed to telling a supplier “how to” perform a task, unless the exact steps in performance of the task are essential to ensure the proper functioning of the product."
The defence standard's performance specification rests on the same idea.

### The Specification Tree

A vehicle has many specifications,
and the tree shows how they relate.
The European systems engineering standard,
ECSS-E-ST-10C Rev.1 of 15 February 2017,
requires one and gives it an annex
[ECSS 2017b][ecss_e_st_10c_rev1].
"The objective of the specification tree document is to define the hierarchical relationship of all technical requirements specifications for the different elements of a system or product."
The document lists every specification and draws the hierarchy,
and it obeys one rule of consistency.
"The specification tree shall be coherent with the product tree"

NASA's current documents use the term without defining it.
Neither the directive nor the Systems Engineering Handbook defines a specification tree
[NASA 2017a][agency_nasa_sp_2016_6105_rev2].
The handbook names it once,
in its outline of a management plan,
which asks for
"a description of the relationship of the specification tree and the drawing tree with the products of the system structure"
of the project.
The nearest thing to a drawing of one is the handbook's figure of the technical baselines.
That figure places the system specification and the segment specifications at the top,
the design-to specifications of each prime item and end item beneath them,
and the build-to specification of each end item at the bottom.
NASA's own standard on configuration management,
NASA-STD-0005 of 2008,
did require the tree in a project's plan,
and that standard has been inactive for new design since 2015
[NASA 2008][agency_nasa_std_0005].

## Configuration

Configuration management answers two questions about a vehicle.
Which documents define it,
and does the unit on the stand match them?
The defence handbook on the subject,
MIL-HDBK-61B of 7 April 2020,
names five functions,
namely configuration management planning,
configuration identification,
configuration change control,
configuration audits
and configuration status accounting
[DoD 2020b][mil_hdbk_61b].
The handbook is guidance,
and its cover tells the reader not to cite it as a requirement.
The industry standard behind it is SAE EIA-649C.
Its publisher sells it,
and the author read only the publisher's summary,
which says that the standard defines five functions and does not name them
[SAE 2019][sae_eia_649c].

### Configuration Items

The unit of control is the configuration item,
which the documents abbreviate as CI.
The defence handbook defines it as
"An aggregation of hardware, software, or both that is designated for CM and treated as a single entity in the CM process."
Here CM stands for configuration management.
NASA's directive adds an end use and a test of what designation means
[NASA 2023a][agency_nasa_npr_7123_1d].
"Configuration Item: An aggregation of hardware, software, firmware or any discrete portion thereof that satisfies an end use function, and is designated for separate configuration management (i.e., it has specified requirements, and is an item to which the effectivity of changes is addressed)."

A reader might expect the European definition in the standard on configuration management,
ECSS-M-ST-40C Rev.1 of 6 March 2009.
That standard defines neither the configuration item nor the configuration baseline.
It takes both from the ECSS glossary,
ECSS-S-ST-00-01C Rev.1 of 11 October 2023
[ECSS 2023][ecss_s_st_00_01c_rev1].
The glossary's definition follows the defence wording closely
and widens the aggregation to include processed materials and services.
The standard itself defines two neighbouring terms.
A configured item is
"any level of product whose functional or physical characteristics are recorded in a retrievable, consistent manner"
and a product item is an
"element of the product tree having a unique identifier"
in the same clause
[ECSS 2009c][ecss_m_st_40c_rev1].

The European standard sorts items into two categories.
A developed item is one that someone designs,
in whole or in part,
for the programme.
A non-developed item is a standard or off-the-shelf product,
and the category
"also includes any product that has been developed and qualified for another programme or project with comparable requirements and which is used without modification."
The customer decides what is an item.
"The responsibility for identifying an item as a CI rests with the customer, unless delegated by him to the supplier."
The supplier presents the list of items for the customer's approval at the preliminary design review,
and the list gives six fields for each item,
namely an identification code,
the models and their quantity,
a name,
the category,
the supplier
and the applicable specification.

No United States document read here prints the fields of a record for one item.
NASA's inactive standard comes nearest,
with a list of the identifiers that such a record may hold.
"These numbers may include: a. Specification identification numbers. b. CI numbers. c. Drawing and part numbers. d. Engineering change identification numbers. e. CAGE code numbers. f. Serial numbers. g. Lot numbers."
A CAGE code is a Commercial and Government Entity code,
which identifies a manufacturer.

### Baselines and the Reviews That Set Them

A baseline is an approved description against which a programme measures later changes.
The defence handbook puts it as
"An agreed-to description of the attributes of a product, at a point in time, which serves as a basis for defining change."
Practice commonly speaks of three baselines,
functional,
allocated
and product,
and a reader might expect to find them in NASA's directive.
The documents are less tidy.

NASA's binding text is NASA Procedural Requirements 7123.1D with Change 2,
abbreviated NPR 7123.1D.
It never uses the terms functional baseline or allocated baseline.
It uses product baseline once,
without a definition,
in a success criterion of the Critical Design Review.
What the directive requires is a baseline of named products at named reviews.
The System Requirements Review baselines the requirements.
The Mission Definition Review or System Definition Review baselines the architecture
and the allocation of requirements to the next lower level.
The Critical Design Review baselines the detailed design.
The directive softens the word,
since a baselined product need only be at least a final draft going into its review.

The names live in NASA's handbook,
which is guidance,
and the handbook counts four.
"NASA has four baselines, each of which defines a distinct phase in the evolution of a product design."
The functional baseline holds the performance requirements of the system and their verification.
The allocated baseline holds the requirements allocated to each item.
The product baseline holds the detail of form,
fit
and function and the requirements for acceptance testing.
The fourth is the as-deployed baseline.
The handbook's glossary heads its entries for the first three with the phases B,
C
and D or E.
The Goddard table of margins cited below places the Preliminary Design Review in phase B
and the Critical Design Review in phase C,
so the glossary's labels for the allocated and product baselines run one phase later
than the reviews that the body of the handbook names.
The handbook does not explain the difference.
The author reports both and does not resolve them.

NASA's inactive standard counts differently again.
"There are three basic NASA baselines as indicated below:"
The defence handbook also defines three.
It says that a programme usually establishes an initial product baseline at the critical design review of each item
and finalises and validates the system's product baseline at the physical configuration audit.

The European standard names five baselines and ties each to a review.
It adds a note that other standards call the second and third the requirements baselines.

| Document | Baselines it names | Where each is set |
|---|---|---|
| NPR 7123.1D, binding | The product baseline once, undefined, and neither the functional nor the allocated baseline | Requirements at the System Requirements Review, architecture and allocation at the Mission or System Definition Review, detailed design at the Critical Design Review |
| NASA Systems Engineering Handbook, guidance | Functional, allocated, product, as-deployed | System Definition Review, Preliminary Design Review, Critical Design Review, Operational Readiness Review |
| NASA-STD-0005, inactive | Three, whose documentation it calls functional, allocated and product | Not recorded here |
| MIL-HDBK-61B, guidance | Functional, allocated, product | The product baseline begins at the critical design review and is final at the physical configuration audit |
| ECSS-M-ST-40C Rev.1 | Mission objective, functional configuration, development configuration, design, product configuration | Preliminary requirements review, system requirements review, preliminary design review, critical design review, and configuration verification or the qualification or acceptance review |

In the European scheme the customer and the supplier agree which documents make up each baseline.
The specifications of products and the interface control documents come under control
at the close of the preliminary design review.
The 2009 text still bases the first baseline on a functional specification,
a document that the specification standard of the same date had removed.
The two standards disagree on that word.

### The As-Designed and As-Built Records

A baseline says what the design is.
A separate record says what each unit is.
The defence handbook states the relation between the two in one sentence.
"The physical aspect of configuration verification establishes that the as-built configuration is in conformance with the as-designed configuration."
It expects the status accounting database to hold
"the as-designed, as-built, as-delivered, or as-modified configuration of any serial-numbered unit of the product as well as of any replaceable component within the product."

NASA's inactive standard describes both records.
The as-designed information is
"The complete drawing package including indentured parts list, deviations and waivers, and traceability of requirements and verification package."
The as-built record,
in the standard's table of status accounting products,
"Records exact configuration delivered to NASA. For hardware items, includes deviation or waiver from as-designed configuration; parts make up, including serial/lot number;"
and further detail that the table's layout prevents the author from quoting.
The same standard gives software its own form of the record,
which the section on [software](#software) takes up.

The European standards give each record a named document.
The design definition file,
abbreviated DDF,
is the description of the design
[ECSS 2017b][ecss_e_st_10c_rev1].
"It details the as-designed configuration baseline (as defined in ECSS-M-ST-40) of the system or product and is built up and updated under the responsibility of the team in charge of system engineering."
The file is a logical one,
and its parts usually appear as separate documents.
Its nine sections run from an introduction and the reference documents
through a summary of the requirements,
a functional description,
a physical description,
the technical budgets with their margins and deviations,
the design constraints
and the repository of engineering data
to a conclusion that lists every deviation of the design from its specifications.
For each element of the physical architecture the file gives the nomenclature,
the drawings,
the constituents,
the characteristics
and
"their configuration management identifier (e.g. hardware part number, software version number, drawings number, electrical schematics numbers)."

Two lists then report status.
The configuration item data list reports the design.
"The configuration item data list (CIDL) is a document generated from the central database giving the current design status of a configuration item (CI), at any point of time in sufficient detail, providing its complete definition."
The as-built configuration list reports each unit.
"The objective of the as-built configuration list (ABCL) is to provide a reporting instrument defining the as-built status per each serial number of configuration item subject to formal acceptance."
The first is the source of the second,
and the section on the bill of materials gives the contents of both.

### Status Accounting

Status accounting is the bookkeeping that makes the records retrievable.
NASA's handbook defines it as
"the recording and reporting of configuration data necessary to manage CIs effectively."
The European standard prescribes six index and status lists.
Each row of the first five carries an identifier,
an issue,
a date
and a title.

| List | Further fields |
|---|---|
| Documents | Remarks and the identification of obsolete documents |
| Drawings | Remarks and the models to which the drawing applies |
| Requests for deviation | The document or requirement affected, the item affected and the status of approval |
| Requests for waiver | The document or requirement affected, the originating nonconformance report, the serial number affected and the status of approval |
| Change proposals | The originating change request, the item affected and the status of approval |
| Review item discrepancies | The review, the discrepancy, its title, the affected document and paragraph, the status, the action assigned and the closure date |

NASA's inactive standard lists comparable products,
among them the revision level and revision history of each drawing,
the version level and version history of software,
an indentured listing of the parts of each item that it calls the as-designed version,
the status of each change in process,
and the as-built configuration.

## The Bill of Materials

None of the regimes surveyed issues a document called a bill of materials.
Each issues several lists that together do its work.
One list names every part and material by type.
Another gives the quantity of each part in the next higher assembly.
A third records the serial and lot numbers of what went into one unit.
The care lies in knowing which document defines which list.

### The Technical Data Package and Its Lists

United States defence practice places the parts list inside the technical data package,
abbreviated TDP,
which MIL-STD-31000B of 31 October 2018 governs
[DoD 2018][mil_std_31000b].
The standard describes the package as follows.
"It consists of applicable technical data such as models, engineering design data, associated lists, specifications, standards, performance requirements, quality assurance provisions, software documentation and packaging details."
A package has one of three levels,
conceptual,
developmental
or product,
and the product level sets a demanding test.
"The product shall be defined to the extent necessary for a competent manufacturer to produce an item, which duplicates the physical, interface, and functional characteristics of the original product, without additional design engineering effort or recourse to the original or current design activity."
The standard adds that product data
"shall reflect the approved, tested, and accepted configuration of the defined delivered item."
Every piece of design data carries a minimum of identifying metadata,
namely the nomenclature,
the document or drawing number,
the part number,
the contract number,
the design activity,
the approver,
the approval date
and the revision level with its date.
An index called the technical data package list names every document in the package
with its number,
revision
and date.

The parts list is one of the associated lists,
and here a common belief needs correction.
MIL-STD-31000B does not define a parts list,
an indentured list
or any other associated list.
It refers the reader elsewhere.
"This block is used to define the Government’s requirements for associated lists as defined in ASME Y14.34."
The block in question is a line of the worksheet on which a buyer selects options,
and it offers parts lists,
data lists,
index lists,
wiring lists
and application lists.
The word indentured does not occur in the text of the saved copy,
whose first pages are images and whose text begins part way through the second section.

The governing document is therefore a standard of the American Society of Mechanical Engineers,
ASME,
numbered Y14.34-2013 and reaffirmed in 2024
[ASME 2013][asme_y14_34].
ASME sells it,
and the author did not read it.
Its publisher's summary states its scope.
"This Standard establishes the minimum requirements for the preparation and revision of application lists, data lists, index lists, part lists, and wire lists."

The only free definitions found are a government restatement in the superseded defence handbook,
MIL-HDBK-61A of 7 February 2001,
which its successor dropped
[DoD 2001][mil_hdbk_61a].
The restatement cites the ASME document under a number that the author takes to be a misprint.
It defines the parts list as
"a tabulation of all parts and bulk materials (except those materials which support a process) used in the item to which the list applies."
A parts list may be integral,
which means that it is part of the drawing,
or separate,
which means that it is a document of its own with its own revisions.
The application list is
"a tabulation of parts and the next higher assemblies into which they install."
The handbook notes that practice commonly calls it a where used list.
A data list tabulates the drawings,
lists,
specifications
and standards that pertain to an item,
and an indentured data list is one
"that is structured by successive assembly level"
in the handbook's words.
The handbook also says how a programme may show the structure itself.
"Product structure, derived from the functional analysis and allocation process of system engineering, may be depicted graphically as a tree structure or as an indentured listing."

### NASA's Parts and Materials Lists

NASA adds two lists by standard.
The first covers electrical,
electronic
and electromechanical parts,
which the standard abbreviates as EEE.
NASA-STD-8739.10,
approved on 13 June 2017,
requires an as-designed list and an as-built list
[NASA 2017b][agency_nasa_std_8739_10].
"The As-Designed EEE Parts List shall identify the equipment containing the individual parts, part description, EEE part number and specification, generic part number, EEE part qualification method and status, part approval status, and part manufacturer(s) as applicable and in accordance with program and project requirements."
A preliminary issue is due at the Preliminary Design Review.
The as-built list is a different record with a different purpose.
"The As-Built EEE Parts List shall identify the EEE parts actually used in fabricating each unit."
The manufacturer submits one for each deliverable end item.
It names the end item and its serial number,
the assembly and its serial number,
the part description,
the part number,
the generic part number,
the serial number of the part where it has one,
the circuit location or reference designation,
the manufacturer's CAGE code
and the lot date code,
or their equivalents.

The second list covers materials and processes.
NASA-STD-6016C with Change 1,
approved on 15 November 2023,
requires a project,
with stated exceptions,
to document their usage in a searchable electronic parts list
or in a separate list called the Materials Identification and Usage List
[NASA 2023b][agency_nasa_std_6016c].
The record must describe the hardware as delivered and not as first drawn.
"The documentation of M&P usage shall cover the final design as delivered."
Here M&P stands for materials and processes.
An appendix of recommended content gives the fields.
The first eleven are the detail drawing and dash number,
the next assembly and dash number,
the change letter,
the drawing source,
the material form,
the material manufacturer,
the manufacturer's designation,
the material specification,
the process specification,
the environment
and,
for nonmetallic materials,
the weight.
The appendix recommends a first submission at the Preliminary Design Review,
an as-designed issue at the hardware acceptance review
and as-built updates before the Flight Readiness Review.
It also ties the list to the configuration record.
"The system used shall be an integral part of the engineering configuration control/release system."

### The European Declared Lists

The European standards name four declared lists,
one for components,
one for materials,
one for mechanical parts
and one for processes.
The supplier prepares each for one equipment or one item
and reissues it at the design reviews,
and each records an approval status.

The declared component list comes from ECSS-Q-ST-60C Rev.4 of 30 April 2025
[ECSS 2025b][ecss_q_st_60c_rev4].
The supplier of each equipment issues it in a sortable electronic format
and keeps it under configuration control.
"The DCL shall be issued as a minimum at PDR and CDR (as designed) and before TRR (as built)."
The abbreviations stand for the declared component list,
the preliminary design review,
the critical design review
and the test readiness review.
The as-designed list goes to the customer for approval.
The as-built list goes to the customer for review,
and it reflects
"the actual EEE parts assembled into the flight hardware and their date code"
on each unit.
After three introductory entries the annex asks for sixteen fields.

| Field | Content |
|---|---|
| Component number | The commercial equivalent designation |
| Family | The group code of the European Space Components Coordination |
| Package | The package type |
| Value | The value or range, with tolerance for parts that are not qualified |
| Manufacturer | Name and country |
| Generic procurement specification | The specification for the family |
| Detail procurement specification | With issue and revision for parts that are not qualified |
| Specification amendment | With issue and revision |
| Procurement agent | The agent named as CPPA, the supplier or the distributor |
| Quality level and lot test | The level and the lot acceptance or lot validation test, or the military equivalents |
| Space qualified status | Yes or no |
| Radiation verification testing | Yes or no |
| Approval document | The reference of the part approval document or justification document |
| Approval status | The status of the part |
| Change identification | What changed since the previous issue |
| Date code | For the as-built issue only |

The other three lists come from ECSS-Q-ST-70C Rev.2 of 15 October 2019
[ECSS 2019][ecss_q_st_70c_rev2].
Its statement of purpose for the materials list is typical of the three.
"The purpose of the DML is to have a detailed record of all the materials used to produce the products of a project or programme."
Here DML stands for the declared materials list.
Each list has ten numbered columns under a header
that gives the programme,
the item number,
the document number,
the group
and the issue.

| Column | Declared materials list | Declared mechanical parts list |
|---|---|---|
| 1 | Item number | Item number |
| 2 | Commercial identification or standardised designation | Commercial identification |
| 3 | Chemical nature and product type | Type of part |
| 4 | Procurement information | Procurement information |
| 5 | Processing parameters | Function and main characteristics |
| 6 | Use and location | Use and location |
| 7 | Environmental code | Environmental code |
| 8 | Size code | Criticality |
| 9 | Validation references, with the prime contractor's comments and approval | Supplier reference, with the prime contractor's comments and approval status |
| 10 | Customer's approval status and comments | Customer's approval status and comments |

The declared process list uses the same frame.
Its columns give the item number,
the identification of the process,
its specification,
its description,
its use and location,
the item numbers of the materials or parts that receive it,
its criticality
and the two approval columns.
The item number of every list encodes a group,
so that materials fall into 20 groups,
mechanical parts into 11
and processes into 17.
The environmental code has three parts,
for radiation,
ambience
and temperature.
The size code places the quantity on a scale of decades by area,
volume
or mass.
In the materials list seven approval codes close each row,
from A for approved through W for approved with a concession to R for rejected and D for deleted.
"All materials classified “A” may be used without restriction."

Two rules of these lists bear on the rest of this article.
The first avoids double entry,
since the mechanical parts list should not repeat an item that appears in the component list.
The second limits an appeal to past use.
"If heritage is used as justification for approval it shall cover the current hardware configuration and mission profile."
A control board at each supplier reviews the lists,
and their approval is due by the critical design review.

### The Product Tree and the Part Number Breakdown

The declared lists name types and their approval.
They do not give the structure of the product or the quantity of each part.
Two other European documents do.

The project management standard,
ECSS-M-ST-10C Rev.1 of 6 March 2009,
specifies and requires the product tree,
which the glossary defines
[ECSS 2009b][ecss_m_st_10c_rev1].
The supplier presents it as a diagram or as an indentured structure,
and each entry carries four fields.
"For each item identified in the product tree, the following information shall be provided: 1. identification code; 2. item name; 3. item supplier; 4. applicable specification."
The tree marks which entries are configuration items
and which are recurrent products from earlier projects.
The supplier establishes it at the start of phase B,
finalises it by the preliminary design review
and keeps it under configuration control.
"The product tree shall be subject to customer approval."
The same standard makes the tree the starting point for selecting configuration items
and the basis of both the work breakdown structure and the specification tree.
NASA's counterpart is the product breakdown structure,
which the Expanded Guidance defines as
"A hierarchical breakdown of the hardware and software products of a program/project."
[NASA 2016b][agency_nasa_seh_expanded_vol2].

The quantities are in the configuration item data list,
whose annex in the configuration standard gives five blocks
[ECSS 2009c][ecss_m_st_40c_rev1].
The first holds the cover and scope.
The second holds the documents that the customer controls,
namely the specifications and the interface control documents.
The third holds the engineering documents,
among them the declared lists,
the lower level specifications,
the drawings with their associated lists,
the test specifications and procedures
and the user's manual.
The fourth holds the changes not yet incorporated and the deviations.
The fifth is the breakdown itself.
"indentured breakdown by part numbers starting from the part number associated with the CI down to the lowest level of composition; (b) quantity of each part number used on the next higher assembly; (c) issue status of the drawings and associated lists applicable to each part number."
Every entry in the list points to a document.
"Each entry in the CIDL shall relate to the applicable model(s) of the CI and be defined by its document number, title, issue and release date."

### The As-Built Configuration List

The as-built list starts from the same breakdown and adds what only a built unit has.
The supplier issues one for each serial number of each deliverable item.
"The ABCL configuration item breakdown section, obtained from the equivalent configuration item data list section, shall be completed by adding the following information: 1. serial number identification; 2. lot or batch number identification; 3. reference(s) of applicable nonconformance report(s) or request for waiver(s)."
The list must also state every discrepancy between the design and the unit.
"The as-built configuration list shall list all discrepancies between the as-designed configuration documented in the configuration item data list and the as-built configuration documented by nonconformance reports or waivers."

The author infers that the European bill of materials is these documents taken together.
The product tree gives the structure.
The part number breakdown gives the quantities.
The declared lists give the types,
their sources
and their approval.
The as-built list gives the serial numbers,
the lot numbers
and the departures.
The standards do not use the term,
and no one of the documents holds the whole.
The author reads the same division in the United States documents,
where the indentured parts list belongs to the drawing package,
the parts and materials lists belong to their own standards,
and the as-built record belongs to configuration status accounting.

## Mass Properties and Margins

A mass statement is the part of a vehicle description most often reduced to one number.
The documents treat it as a structured report,
with defined terms,
an allowance for growth that depends on how mature each item is,
and a margin against a limit.

### The Terms

The governing United States document is a standard of the American Institute of Aeronautics and Astronautics,
AIAA,
numbered S-120A-2015
[AIAA 2015][aiaa_s_120a_2015].
AIAA sells it,
and the author did not read it.
The best free statement of its terms is rule 1.06 of the design rules of NASA's Goddard Space Flight Center,
GSFC-STD-1000 Revision I,
approved on 19 August 2025
[NASA 2025a][agency_nasa_gsfc_std_1000i].
The rule belongs to one NASA centre,
and its change log records a revision that aligned the rule with the AIAA standard.
It defines five terms.

- **Basic mass.**
  "Basic mass is the current estimated mass of dry hardware based on an assessment of the most recent design (not including mass growth allowance)"
  and the rule adds that practice once called it the current best estimate.
- **Mass growth allowance.**
  The rule abbreviates it as MGA.
  "Mass Growth Allowance (MGA) is the predicted increase to the basic mass of an item based on an assessment of the hardware category/design maturity/fabrication status in alignment with AIAA S-120A-2015."
- **Predicted mass.**
  "Predicted mass = Basic + MGA"
  in the rule's own notation.
- **Allowable mass.**
  "Allowable mass is the limit against which mass margins are calculated, typically the mass allocation or launch vehicle capacity"
  and the rule adds that practice once called it the maximum permissible value.
- **Mass margin.**
  The margin is the allowable mass less the predicted mass.

Let $M\_{\mathrm{B}}$ be the basic mass,
$G$ the mass growth allowance,
$M\_{\mathrm{P}}$ the predicted mass,
$M\_{\mathrm{A}}$ the allowable mass
and $\mu$ the mass margin in percent.
The predicted mass is the sum of the first two.

$$
M_{\mathrm{P}} = M_{\mathrm{B}} + G
\tag{1}
$$

The rule then fixes the denominator of the percentage.
"Mass margin (%) = (Allowable-Predicted)/Basic X 100."

$$
\mu = \frac{M_{\mathrm{A}} - M_{\mathrm{P}}}{M_{\mathrm{B}}} \times 100
\tag{2}
$$

The denominator matters,
because NASA's own guidance prints three.
The Expanded Guidance for NASA Systems Engineering,
whose mass definitions derive from the 2006 edition of the AIAA standard and not from S-120A,
gives alternative formulas for percent margin
that divide by the basic value,
by the predicted value
or by the required value
[NASA 2016b][agency_nasa_seh_expanded_vol2].
Consider a stage whose items have a basic mass of 400 kilograms
and a growth allowance of 40 kilograms against an allowable mass of 500 kilograms.
Its predicted mass is 440 kilograms and its margin is 60 kilograms.
That margin is 15.0 percent of the basic mass,
13.6 percent of the predicted mass
and 12.0 percent of the allowable mass.
A mass statement that gives a percentage without its denominator has not stated its margin.

The Expanded Guidance expresses the allowance itself as a fraction of the basic value.
With $g$ the fractional growth allowance,

$$
g = \frac{M_{\mathrm{P}} - M_{\mathrm{B}}}{M_{\mathrm{B}}}
\tag{3}
$$

The stage of the example carries an allowance of 10 percent.
The same guidance draws the line between the two quantities.
"Margin accounts for unexpected growth while Mass Growth Allowance (MGA) accounts for expected growth."
The Goddard rule applies both to dry mass only
and handles propellant through margins on velocity change.
It also requires the responsible engineer to assign the allowance from the bottom up,
line by line of the equipment list,
and never from the top down.

The vocabulary varies.
The Goddard rule forbids two words.
"The terms “reserve” and “contingency” are not to be used in relation to mass margins."
The Expanded Guidance gives contingency as another name for the growth allowance,
and the European structural standard asks for
"mass contingency estimates based on the design maturity."
The cancelled defence handbook described below speaks of weight and of a weight growth allowance.
A reader of a mass statement should check which vocabulary its author used.

### Growth Allowance by Design Maturity

The AIAA standard grades the allowance by the maturity of each item and by its kind of hardware.
The author knows its table only at second hand.
A technical memorandum of the NASA Engineering and Safety Center reproduces the table as an image
and says that it used the standard as its framework
[Holladay et al. 2024][agency_nasa_tm_20240014203].
The values below are the author's reading of that image for two of its thirteen hardware columns,
and they are percentages of the basic mass.

| Maturity code and basis | Primary structure | Propulsion and fluid system hardware |
|---|---|---|
| E1, estimated | 18 to 25 | 15 to 25 |
| E2, layout | 10 to 20 | 10 to 20 |
| C3, preliminary design | 4 to 15 | 5 to 15 |
| C4, released design | 2 to 6 | 2 to 7 |
| A5, existing hardware | 1 to 3 | 1 to 3 |
| A6, actual mass | None | None |
| S7, specification value | None | None |

The letters stand for estimated,
calculated,
actual
and specified.
The image defines the grades in a few words each.
An estimated value rests on rough sketches,
parametric analysis
or experience.
A layout value rests on a conceptual design before initial sizing.
A preliminary design value follows initial sizing and precedes the final analyses.
A released design value follows final signoff.
An existing hardware value is a measurement from another programme or a catalogue value.
An actual mass is the measured mass of the flight hardware,
which takes no allowance and carries the uncertainty of the measurement.
A specification value is typically a stated limit,
and it takes no allowance.
The other eleven columns cover electronics in three classes of mass,
thermal control,
batteries,
wire harnesses,
solar arrays,
life support and crew systems,
secondary structure,
mechanisms
and instrumentation.
The highest values in the image are those for an estimated wire harness,
at 50 to 100 percent.

Three cautions attach to the table.
The memorandum's caption says that its copy carries highlights,
so the author cannot say that the copy matches the standard.
The memorandum cites the standard with the year 2019 and the Goddard rule cites it as 2015.
And the table is a transcription by eye,
which a reader who needs the values should replace with the standard itself.

### Margins Required at Each Review

The Goddard rule requires a mass margin at each stage of a project,
and the Expanded Guidance gives a range for margin and allowance together.
The two columns below measure different things and are not directly comparable.
The first is margin alone as a percentage of basic mass.
The second is the sum of margin and growth allowance.

| Review | Goddard rule, mass margin | Expanded Guidance, margin plus allowance |
|---|---|---|
| Before the System Requirements Review | At least 15 percent at all times | 25 to 40 percent at the Mission Concept Review |
| System Requirements Review | At least 15 percent | 25 to 35 percent |
| Preliminary Design Review | At least 10 percent | 20 to 25 percent |
| Critical Design Review | At least 5 percent | 10 to 15 percent |
| System Integration Review | More than 2 percent | Not given |
| Test Readiness Review | Not given | 5 to 10 percent |
| Phase D | Zero | Not given |

The Goddard values come from the rule's table of technical resource margins.
The Expanded Guidance groups the System Requirements Review with the two definition reviews that follow it.
Both columns fall as the design matures,
which is the point of the scheme.
Margin is not a fixed fraction held to the end.
A programme spends it as estimates become measurements.

### The Mass Report

The fullest free account of what a mass report holds is a cancelled one.
MIL-HDBK-1811 of 12 August 1998 covered mass properties control for space vehicles,
and a notice of 27 April 2017 cancelled it without replacement
[DoD 1998][mil_hdbk_1811]
[DoD 2017][mil_hdbk_1811_notice_1].
Its definition of the subject remains useful.
"The mass properties of an item include the item's weight (or mass), center of gravity (or center of mass), mass moments of inertia, and mass products of inertia."
The handbook asks for a status report with eight elements.

1. **A summary.**
   "The predicted mass properties should be tabulated by subsystem and combined for the total predicted mass properties."
   The summary marks the items that the vehicle expends or jettisons
   and gives the totals for the launch condition.
2. **Limit monitoring.**
   The report compares the predicted values with their limits.
3. **Changes.**
   The report lists every change of weight since the previous report.
4. **Potential changes.**
   The report lists the changes that are pending or possible.
5. **Sequential mass properties.**
   The report gives the properties through the mission,
   since they
   "should be determined and documented as a function of time or percent of steady state thrust from mission initiation through mission completion."
6. **Furnished equipment.**
   The report tabulates the equipment that the government supplies and its properties.
7. **Reference axes.**
   A diagram relates the axis system of the report to the vehicle.
8. **Weight growth.**
   The report gives the state of the allowance and of the plan for releasing it.

The handbook also asks that every value state its basis.
"The basis of space vehicle mass properties can be categorized by the methods used for their determination, for example: estimated, calculated, or measured."
It notes that a value taken from released drawings counts as calculated
and that practice had called the measured category actual.
The three words match the letters E,
C
and A of the table above.

An appendix of the handbook gives a sample breakdown for a liquid propulsion stage,
which is the nearest thing in these sources to a standard set of headings for a launch vehicle stage.
It has nine top-level rows,
namely structure,
thermal control,
main propulsion,
orientation control,
secondary power,
instrumentation,
range safety and abort,
weight growth allowance
and fluids.
Structure divides into the fuel tank,
the oxidiser tank,
the intertank structure,
the thrust structure
and the launch supports.
Main propulsion divides into the rocket engine,
the fuel feed,
the oxidiser feed,
pressurisation
and the fill,
drain
and vent system.
Fluids divide into six kinds,
namely impulse propellant,
residual propellant,
reserve propellant,
bias propellant,
outage propellant
and pressurisation gas.
The growth allowance has a row of its own,
and the other rows do not hide it.

One older form needs a correction of scope,
since it is an aircraft form and not a space vehicle form.
MIL-STD-1374A of 30 September 1977 prescribes weight and balance reporting forms for aircraft and rotorcraft,
and a notice of 18 July 2005 cancelled it and pointed to a recommended practice numbered SAWE-RP8
[DoD 1977][mil_std_1374a]
[DoD 2005][mil_std_1374a_notice_3].
Its group weight statement sums the structure,
propulsion
and equipment groups to a weight empty
and adds the useful load to reach a gross weight.
The author read the form from page images of a poor scan,
and the logic stated here is an inference from the order of its rows.

The active lists of the European standards show no document dedicated to mass properties.
The structural standard,
ECSS-E-ST-32C Rev.1 of 15 November 2008,
requires a report
[ECSS 2008][ecss_e_st_32c_rev1].
"The inertia properties shall be monitored and presented in a mass budget report issued on a regular basis agreed with the customer."
"A breakdown of mass to component level shall be given together with mass contingency estimates based on the design maturity."
The international standard on the subject is ISO 22010,
whose second edition the International Organization for Standardization,
ISO,
published in 2022
[ISO 2022][iso_22010_2022].
ISO sells it,
and the author read only its catalogue entry.

A historic report shows the form in use.
The mission report of Apollo 11 carries a table of mass properties in which each row is an event of the mission,
from lift-off to landing
[NASA 1971][agency_nasa_apollo_11_mission_report].
Its columns give the weight,
the centre of gravity on three axes,
the moments of inertia
and the products of inertia.
The text beside it states the basis of the values in one sentence.
"The weights and centers of gravity of the individual command and service modules and of the lunar module ascent and descent stages were measured prior to flight, and the inertial values were calculated."
The table is a sequential mass statement of the kind that the defence handbook later described,
and its sentence of basis separates the measured from the calculated.

### The European Margin Philosophy

The European systems engineering standard sets no numerical margin of mass or resources.
It requires a policy instead.
"The system engineering function shall define and apply the margin policy agreed between customer and supplier in compliance with Annex D.2.1<4.2>b.5."
The annex in question puts the policy in the systems engineering plan
and says that it varies with the project phase,
the product category
and the maturity level.
The same standard requires a technical budget for each engineering parameter that the project selects,
with mass,
power,
communication links
and computer memory as its examples.
For each parameter the budget gives the specified value,
the margin,
a chart of the parameter's history across the stages of design maturity
and the sources of the figures.

One document of the European Space Agency,
ESA,
does set numbers.
It is the margin philosophy for science assessment studies,
issue 1 revision 3 of 15 June 2012
[ESA 2012][esa_margin_philosophy_2012].
It governs early studies and not the later phases of a project,
its cover marks it for official use,
and the author did not look for a successor.
It grades the margin on each equipment by heritage and then adds a margin for the system.

| Quantity | Margin or allowance | Rule |
|---|---|---|
| Equipment mass, off the shelf | At least 5 percent | R-M1-41 |
| Equipment mass, off the shelf with minor modification | At least 10 percent | Printed as R-M2-42 |
| Equipment mass, new or with major modification | At least 20 percent | R-M1-43 |
| System dry mass | 20 percent of the nominal dry mass | R-M1-1 |
| Harness mass | At least 5 percent of the nominal dry mass | R-M1-7 |
| Propellant residuals | 2 percent of the calculated propellant | R-M1-6 |
| Tank volume | At least 10 percent above the total propellant | R-M1-10 |
| Velocity change, accurately calculated manoeuvres | 5 percent | R-DV-11 |
| Velocity change, general orbit maintenance | 100 percent | R-DV-12 |
| Velocity change, attitude control and momentum management | 100 percent | R-DV-13 |
| Equipment power | At least 5, 10 and 20 percent by the same three grades | R-P-11 to R-P-13 |
| System power | At least 20 percent of the nominal requirement | R-P-3 |
| On-board memory | At least 50 percent | R-SW-1 |
| Processor peak usage | At most 50 percent of capability | R-SW-2 |

The second rule number is a slip in the source for R-M1-42.
The document ties its three grades to the European product categories of heritage
that the section on [verification](#verification-qualification-and-acceptance) describes,
with categories A and B at 5 percent,
category C at 10 percent
and category D at 20 percent.

The two layers of mass margin compound.
The nominal dry mass already includes the equipment margins,
and the system margin applies on top of it.
"The total dry mass at launch of the spacecraft shall include an ESA system level mass margin of 20 % of the nominal dry mass at launch (this shall include the equipment level margin as specified in R-M1-4)."
Let $m\_{i}$ be the estimated mass of equipment $i$ before any margin,
$k\_{i}$ its maturity margin as a fraction,
$s$ the system margin as a fraction
and $M\_{\mathrm{D}}$ the total dry mass at launch.
The document prints no formula,
and the author writes its rules as one.

$$
M_{\mathrm{D}} = \left( 1 + s \right) \sum_{i} m_{i} \left( 1 + k_{i} \right)
\tag{4}
$$

Consider three items estimated at 100,
50
and 200 kilograms,
the first off the shelf,
the second off the shelf with a minor modification
and the third new.
Their margined masses are 105,
55
and 240 kilograms,
which give a nominal dry mass of 400 kilograms
and a total dry mass at launch of 480 kilograms.
The total stands 37 percent above the 350 kilograms of the bare estimates.

The other rules follow the same pattern.
The propellant calculation starts from the total dry mass and adds the residuals.
Each margin on velocity change applies to the effective value of its manoeuvre,
and the document requires a study to quantify gravity losses and add them.
A study sizes its solar arrays and batteries to supply the required power,
with all margins,
at the end of life.

The author draws one comparison from the two regimes.
Both grade an allowance on each item by its maturity or heritage,
and both then hold a separate margin for the system.
They differ in the base of the second layer.
The Goddard rule measures its margin between the predicted mass and an allowable mass
and divides by the basic mass.
The European document adds a fixed fraction of a nominal mass that already contains the first layer.
That reading is an inference from the two texts,
and neither text refers to the other.

## Interfaces

An interface is where two products meet,
and two documents govern it.
The first states what the interface must do.
The second states how the design realises it.
Both regimes keep the two apart and both name them the same way,
as the interface requirements document,
IRD,
and the interface control document,
ICD.

### NASA's Interface Documents

NASA's handbook lists the documents and leaves their definitions to its Expanded Guidance
[NASA 2016a][agency_nasa_seh_expanded_vol1].
The requirements document comes first.
"The IRD is a document or model that defines all physical, functional, performance and environmental interface requirements (written in “shall” statements) between two or more end items, elements, or components of a system and ensures project hardware and software compatibility."
The control document answers it.
"An interface control document, model, or drawing details the physical interface between two system elements, including the number and types of connectors, electrical parameters, mechanical properties, and environmental constraints."
The guidance marks the difference by the verb,
since
"An ICD usually does not contain “shall” statements"
and instead records how the design meets the requirements.
A small project may combine the two as one document in two parts.

The guidance also separates a document that two parties agree from one that a single party issues.
The control document is usually an agreement between two or more organisations.
The interface definition document is one-sided.
"An IDD is a unilateral document controlled by the end-item provider, and it basically provides the details of the interface for a design solution that is already established."
The abbreviation IDD needs care,
because NASA's software handbook uses the same letters for the interface design description of software.

Signature follows from agreement.
The guidance's checklist says of the requirements document that
"Each organization needs to approve and sign the IRD."
The handbook sets the rule for the general case.
"For interfaces that require approval from all sides, unanimous approval is required."

The Expanded Guidance outlines the requirements document in an appendix.
The author read the outline as far as its entry on vibroacoustics.

1. **Introduction.**
   Purpose and scope,
   precedence,
   and responsibility with change authority.
2. **Documents.**
   Applicable documents and reference documents.
3. **Interfaces.**
   A general part gives the description of the interface,
   the responsibilities,
   the coordinate systems,
   and the engineering units with their tolerances and conversions.
   The requirements then follow in seven groups,
   namely mass properties,
   structural and mechanical,
   fluid,
   electrical power,
   electronic signal,
   software and data,
   and environments.

The outline asks each side to define its coordinate system,
and its entry on mass properties gives the mass of the element as its example.
A vehicle's mass statement is therefore an interface datum as well as a design datum.

### The European Interface Standard

The European standard is ECSS-E-ST-10-24C Rev.1 of 15 November 2024
[ECSS 2024][ecss_e_st_10_24c_rev1].
Its file forbids the extraction of text,
so the two quotations below are the author's transcriptions from the page.
A reader might expect the standard to define the two documents among its terms.
Its clause of terms defines nine,
and neither document is among them.
The working definitions are the statements of purpose in its annexes.
The first of them places the requirements document inside the family of specifications.
"For a product, the interface requirements document (IRD) is a specific type of technical requirements specification that defines the requirements for an interface or a collection of interfaces."
The second gives the control document the task of defining the design of the interface
so that the two ends are compatible in form,
fit
and function.

The requirements document has five sections,
namely an introduction,
the applicable and reference documents,
the definition of terms,
the interface requirements
and the aspects that each interface must address.
Each requirement carries its verification requirement and says to which end of the interface it applies.
The control document has five sections of its own,
namely an introduction,
responsibility,
the applicable and reference documents,
the definition of terms
and the interface definition.
The responsibility section names the authority that approves the document and its changes.
Each document asks for seven things about each interface,
and six of the seven are common to both.
They are the interface plane,
the behaviour of the interface with its limits of use,
a description by tables,
figures
or drawings,
the units of measure,
the tolerances
and the conversions for any units outside the international system.
The requirements document adds the coordinate system,
and the control document adds the data that affect the definition.
The control document also names the approved change requests that each version incorporates.

The standard is exact about control and signature.
The customer or a delegate is responsible for the interface.
The control document comes under configuration control before the preliminary design review of the suppliers at each end,
and it reaches a frozen state before the critical design review of the first product involved.
"The frozen ICD shall be approved (signed) by all involved parties."
A later change needs a change request that every party and the responsible authority sign before it takes effect.
The standard keeps a one-sided document as well,
which it also calls an interface definition document.

One piece of housekeeping affects anyone who follows the older references.
The interface requirements document was once an annex of the systems engineering standard.
The 2017 revision of that standard deleted the annex and moved it here.
The specification standard of 2009 still points to the deleted annex.

## Verification, Qualification and Acceptance

A description of a vehicle that states what the vehicle can do should also state how anyone knows.
The documents answer with three ideas,
namely the method of verification,
the stage at which it takes place
and the heritage of the product.
This section gives them in outline from the European standard on verification,
ECSS-E-ST-10-02C Rev.1 of 1 February 2018,
which states them most compactly
[ECSS 2018][ecss_e_st_10_02c_rev1].

### Methods and Stages

The European standard names four methods and ranks them.
"The verification is executed by one or more of the following verification methods: test, analysis, review of design and inspection. This list shows the order of precedence that, in general, provides more confidence in the results."
Demonstration counts as a form of test and similarity as a form of analysis.
The defence standard on specifications also names four,
namely analysis,
demonstration,
examination
and test.
The two lists overlap without matching,
since the European review of design has no counterpart by name in the defence list.
That observation is the author's.

The stages are qualification,
acceptance,
pre-launch,
in-orbit
and post-landing,
and the first three must be complete before launch.
Qualification is about the design.
"In the qualification stage the supplier shall demonstrate that the design, including margins, meets the applicable requirements."
Acceptance is about the unit.
"The acceptance article shall be manufactured in agreement with the qualified design."
The acceptance stage shows that the delivered product meets its specified margins,
with any agreed deviations and waivers,
and is free of defects.

The companion standard on testing,
ECSS-E-ST-10-03C Rev.1 of 31 May 2022,
turns the difference into numbers
[ECSS 2022][ecss_e_st_10_03c_rev1].
Qualification testing uses dedicated models and qualification margins,
which demonstrate the margin of the design.
Acceptance testing applies acceptance margins to every flight product in order to find defects of workmanship.
A third approach uses no dedicated model.
"Protoflight testing is the combination of the qualification and acceptance testing objectives on the first flight model."
For the random vibration of equipment the standard's tables give the maximum expected spectrum
plus 3 decibels for 2 minutes on each axis at qualification,
plus 0 decibels for 1 minute at acceptance
and plus 3 decibels for 1 minute at protoflight.
The protoflight unit therefore sees the levels of qualification for the durations of acceptance.
Those figures are the author's summary of three tables and not quotations.

### Product Categories by Heritage

The same verification standard grades every product by its heritage,
and the grade sets how much qualification the product needs.

| Category | Description | Qualification programme |
|---|---|---|
| A | Off the shelf and unmodified, already qualified at least as severely as the project requires, and produced by the same manufacturer with the same tools, processes and procedures | None |
| B | Off the shelf and unmodified, but qualified less severely or differently | Delta qualification, decided case by case |
| C | Off the shelf with modifications | Delta or full qualification including testing, decided case by case |
| D | Newly designed and developed | Full qualification |

The definition of a modification is broad.
"Off-the-shelf product with modifications. Modification includes changes to design, parts, materials, tools, processes, procedures, supplier, or manufacturer."
By that definition a change of supplier alone moves a product from category A to category C.
The standard also limits qualification by similarity,
since the precedent may not itself rest on qualification by similarity.
These four letters recur in the European documents.
The margin philosophy grades its mass and power margins by them,
and the readiness handbook grades the validity of an earlier assessment by them.

### The Verification Control Document

The record of verification is a matrix with one row for each requirement.
The standard lists ten columns.

1. The identifier of the requirement.
2. Its text.
3. Its traceability to other requirements.
4. The levels and stages of verification.
5. The methods.
6. A link to the verification plan.
7. References to the documents that demonstrate compliance.
8. The status of compliance,
   as yes,
   no
   or partial.
9. The close-out status,
   as open
   or closed.
10. The reasons for the close-out status.

The first six columns make up the first issue of the document,
which the standards call the verification matrix.
The matrix is therefore not a separate document.
It is the plan half of a record whose result half fills in as the work proceeds.
A board of customer and supplier representatives judges when verification is complete,
and its conclusions go to the customer for approval.

## Software

Control software is a part of the vehicle,
and both regimes describe a delivered version of it with a document that hardware practice would recognise.
It names the version,
lists what the version consists of,
and states its known problems.
An earlier article on this site treats the discipline that surrounds such software
[Safety-Critical Software][related_post_safety_critical_software].

### NASA's Software Records

NASA's software directive is NPR 7150.2D,
effective from 8 March 2022
[NASA 2022a][agency_nasa_npr_7150_2d].
It requires the record in one sentence.
"The project manager shall provide a software version description for each software release."
The directive does not fix a format.
"Use of NASA Center and contractor formats in document deliverables is acceptable if the required content (as defined by the project) is addressed."
The content comes from the agency's software engineering handbook,
NASA-HDBK-2203,
which NASA maintains as a set of web pages
[NASA 2020][agency_nasa_hdbk_2203].
The handbook calls the record the version description document and abbreviates it as VDD.
"The VDD is the definitive record of all components of a released software work product, whether it is for internal or external release."
The inactive configuration standard states its place among the hardware records.
"The VDD is the equivalent of an as-built version for software."

The handbook recommends ten items of content as a minimum.

1. Full identification of the system and the software,
   with numbers,
   titles,
   abbreviations,
   version numbers
   and release numbers.
2. The executable software,
   including the batch,
   command
   and data files needed to install it on its target computer.
3. The life cycle data that define the software product.
4. The archive and release data.
5. Instructions for building the executable software,
   including the data for compiling and linking and the procedures for recovery and regeneration.
6. Data integrity checks for the executable object code and the source code.
7. The product files needed to install,
   build,
   operate
   and maintain the software.
8. The open change requests and problem reports,
   with any workarounds.
9. The change requests and problem reports implemented since the previous version description.
10. Confirmation of a scan of the software for security defects and for compliance with its coding standard.

The first seven items match a list in the configuration standard of 2008 almost word for word,
and the last three are later additions.

Three other documents describe the software itself.
The design description covers the design decisions,
the architecture
and the detailed design of one software item,
with the traceability of requirements to design and code.
The interface design description gives the type of each interface,
the data elements down to the level of the bit
and the protocols.
The user manual gives a summary of the software,
the means of access,
a reference to its processing
and the information that is particular to each version.
"For NASA flight projects, the Software User Manual is baselined by the Operational Readiness Review (ORR)."

The directive sorts software into six classes,
and a description of control software should state the class.
"Classes A through E cover engineering-related software."

| Class | Heading in the directive |
|---|---|
| A | "Class A: Human Rated Space Software Systems" |
| B | "Class B: Non-Human Space Rated Software Systems or Large Scale Aeronautics Vehicles" |
| C | "Class C: Mission Support Software or Aeronautic Vehicles, or Major Engineering/Research Facility Software" |
| D | "Class D: Basic Science/Engineering Design and Research and Technology Software" |
| E | "Class E: Design Concept, Research, Technology, and General Purpose Software" |
| F | "Class F: General Purpose Computing, Business, and IT Software" |

The current revision has no class G and no class H.
Where more than one class appears to apply,
the directive assigns the higher.
Its examples of class A for launch include guidance,
navigation
and control.

### The European Software Standards

The European software standard is ECSS-E-ST-40C Rev.1 of 30 April 2025,
and its companion on software product assurance,
ECSS-Q-ST-80C Rev.2,
carries the same date
[ECSS 2025a][ecss_e_st_40c_rev1]
[ECSS 2025c][ecss_q_st_80c_rev2].
Anything written before May 2025 cites issues that these two replaced.
The standard groups the documents of a software product into files,
and the delivered software sits in the design definition file as four documents.
They are the software design document,
the software configuration file,
the software release document
and the software user manual.

The release document is the counterpart of NASA's version description.
The standard abbreviates it as SRelD.
"The SRelD is a constituent of the DDF. Its purpose is to describe a given software version including known problems, limitations or restrictions with respect to its approved baseline."
Its annex fixes seven sections.

| Section | Title | What it holds |
|---|---|---|
| 1 | Introduction | Purpose, objective, content and the reason for preparing the document |
| 2 | Applicable and reference documents | Both lists |
| 3 | Terms, definitions and abbreviated terms | Any additional terms |
| 4 | Software release overview | The reference of the configuration file, the version delivered, the status of problem reports, change requests, waivers and deviations, and advice for use |
| 5 | Status of the software configuration item | The evolution since the previous version, and the known problems or limitations |
| 6 | Advice for use of the software configuration item | Advice for this version |
| 7 | On-going changes | The planned evolution of the item |

The release document is a digest of a larger one.
"The software release document is a subset of the software configuration file that describes a new version by comparison with “reference” or the previous one."
The software configuration file is the complete record,
and a reader who looks for it in the software standard will not find its contents there.
Its definition is an annex of the standard on configuration management
[ECSS 2009c][ecss_m_st_40c_rev1].
"The objective of the software configuration file is to provide the configuration status of the software configuration item. It controls its evolution during the programme or project life cycle."
It has twelve sections,
namely an introduction,
the documents,
the terms,
an overview of the item,
an inventory of materials,
the baseline documents,
an inventory of the item,
the means necessary for the item,
installation instructions,
a change list,
auxiliary information
and the possible problems and known errors.
The inventory of the item is exact about what it lists.
"The SCF shall list all files constituting the software configuration item: 1. source codes with name, version, description; 2. binary codes with name, version, description; 3. associated data files necessary to run the software; 4. media labelling references; 5. checksum values; 6. identification and protection method and tool description."
Here SCF stands for the software configuration file.
The section on means names the things outside the item that building and running it require,
such as the compiler with its version.
The change list separates the changes incorporated from those not yet incorporated.

The software design document describes the architecture and the detailed design.
Its overview includes a budget of memory and processor use.
It describes each component under ten headings,
namely identifier,
type,
purpose,
function,
subordinates,
dependencies,
interfaces,
resources,
references
and data.

The European standards grade software by criticality,
in four categories from A to D.
The rule of assignment is in the dependability standard,
ECSS-Q-ST-30C Rev.1 of 15 February 2017
[ECSS 2017c][ecss_q_st_30c_rev1].
"The criticality category of a software product (A, B, C, D) shall be assigned, based on the criticality assigned to the most critical function it implements, and meeting the criteria defined in Table 5-3 and requirements 5.4.2b to 5.4.2g."
Functions fall into four categories of their own,
numbered I to IV,
by whether their failure has catastrophic,
critical,
major
or minor or negligible consequences.
The software product assurance standard,
ECSS-Q-ST-80C Rev.2,
gives the categories of software in its Table D-1,
which the next table summarises
[ECSS 2025c][ecss_q_st_80c_rev2].

| Category | Software, in summary |
|---|---|
| A | Involved in a category I function with no compensating provision, or part of the compensating provision for one |
| B | Involved in a category I function with a compensating provision or a category II function with none, or part of the compensating provision for a category II function |
| C | Involved in a category II function with a compensating provision or a category III function with none, or part of the compensating provision for a category III function |
| D | Involved in a category III function with a compensating provision or a category IV function with none |

A compensating provision may be an inhibit,
a monitor,
a back-up
or an operational procedure.

The two schemes sort on different axes,
which is the author's reading of them.
NASA's classes sort software by the kind of system it belongs to,
from human rated space systems to business software.
The European categories sort it by the worst consequence of the function it implements,
reduced by one step where something else stands behind it.
A description of control software can state either,
and it should say which scheme it uses.

## Technology Readiness and Heritage

Two statements about a design are easy to make and hard to make exactly.
One is how mature it is.
The other is how much of it has flown before.
The agencies give the first a scale of nine levels,
the technology readiness level,
which every source abbreviates as TRL.
They give the second a set of rules that are less complete than the scale.

### The Nine Levels

NASA defines its scale in an appendix of the systems engineering directive
[NASA 2023a][agency_nasa_npr_7123_1d].
The appendix is a table that gives each level a definition,
a description for hardware,
a description for software
and success criteria.
A note at its end settles any dispute within the agency.
"Note: In cases of conflict between NASA directives concerning TRL definitions, NPR 7123.1 will take precedence."

The European scale is that of the international standard ISO 16290 of 2013,
which ECSS adopted by a notice of 1 October 2014,
ECSS-E-AS-11C,
and explains in a handbook of 1 March 2017,
ECSS-E-HB-11A
[ISO 2013][iso_16290_2013]
[ECSS 2014][ecss_e_as_11c]
[ECSS 2017a][ecss_e_hb_11a].
ISO sells its standard,
and its catalogue entry says of the 2013 edition that
"This publication was last reviewed and confirmed in 2024. Therefore this version remains current."
The definitions below reach this article through the handbook,
which presents them as those of the ISO standard.

| Level | NASA directive | European handbook, after ISO 16290 |
|---|---|---|
| 1 | "Basic principles observed and reported." | "Basic principles observed and reported" |
| 2 | "Technology concept and/or application formulated." | "Technology concept and/or application formulated" |
| 3 | "Analytical and experimental proof-of-concept of critical function and/or characteristics." | "Analytical and experimental critical function and/or characteristic proof-of-concept" |
| 4 | "Component and/or breadboard validation in a laboratory environment." | "Component and/or breadboard functional verification in laboratory environment" |
| 5 | "Component and/or brassboard validated in a relevant environment." | "Component and/or breadboard critical function verification in a relevant environment" |
| 6 | "System/sub-system model or prototype demonstration in a relevant environment." | "Model demonstrating the critical functions of the element in a relevant environment" |
| 7 | "System prototype demonstration in an operational environment." | "Model demonstrating the element performance for the operational environment" |
| 8 | "Actual system completed and "flight qualified" through test and demonstration." | "Actual system completed and accepted for flight (“flight qualified”)" |
| 9 | "Actual system flight proven through successful mission operations." | "Actual system “flight proven” through successful mission operations" |

The two columns agree at the ends and part in the middle.
The European handbook explains why,
by comparing the ISO scale with the scale of a NASA white paper of 1995
that it calls the Mankins 95 reference and abbreviates as M95r.
"ISO level 6 is equivalent to M95r level 5."
"ISO level 7 is equivalent to M95r level 6."
The ISO scale inserted a new level 5 for breadboards that are not at full scale,
and it does not recognise the old level 7,
which was the demonstration of a system prototype in the space environment.
The handbook calls the older scale obsolete.

NASA's directive keeps a level 7 that demonstrates a system prototype in an operational environment,
and its level 6 nearly repeats the wording that the handbook gives for the level 6 of 1995.
The handbook heads its comparison as the European interpretation of the white paper,
which the author did not read.
On that interpretation the author infers that a level 6 on NASA's scale corresponds to a level 7 on the ISO scale,
and that the numbers 5,
6
and 7 do not mean the same thing in the two regimes.
Neither document makes that comparison.
A statement of readiness should therefore name its scale.

### The Origin of the Scale

The scale began at NASA,
and the sources agree on little more than that.

- A NASA article of 2010 dates the first scale to 1974
  [Banke 2010][agency_nasa_banke_2010].
  "A NASA researcher, Stan Sadin, conceived the first scale in 1974. It had seven levels which were not formally defined until 1989."
  The article adds that NASA adopted a scale of nine levels in the 1990s.
- A footnote in the Expanded Guidance gives the same year and the same name,
  and credits a later elaboration to a second author in 1995,
  whose surname it misspells
  [NASA 2016b][agency_nasa_seh_expanded_vol2].
- NASA's guide to readiness assessment says instead that the levels were
  "first described at NASA HQ in the 1980s"
  and gives no name
  [Kimmel et al. 2020][agency_nasa_tra_guide].
  Here HQ is the agency's headquarters.
- The European handbook says that the method
  "was originated at NASA in the 1970s"
  and that the scale reached nine levels in 1995.
  Its list of references gives the white paper as the work of John C. Mankins,
  dated 6 April 1995.

The formal definition of 1989 is by citation a paper of Sadin,
Povinelli
and Rosen in the journal Acta Astronautica,
first issued as a conference paper in 1988
[Sadin, Povinelli and Rosen 1989][research_sadin_1989].
The author confirmed the citation from two bibliographic records and did not read the paper,
so this article cannot say how many levels it prints.
The author did not obtain the white paper of 1995 either.
The chain from 1974 through 1989 to 1995 therefore rests here on secondary accounts,
three of them NASA's own and not in full agreement about the decade.

### Evidence and Records

A level is a claim,
and each scale says what evidence supports it.
NASA's success criteria rise from documents to tests to flight.
Level 1 asks for
"Peer reviewed documentation of research underlying the proposed concept/application."
Levels 4 to 7 ask for documented test performance that agrees with analytical predictions.
Level 9 asks for
"Documented mission operational results."

The European handbook names documents and reviews.
Level 6 expects a technical requirements specification,
a design definition file,
a design justification file
and the test reports of a model.
Level 7 adds a qualification review,
level 8 an acceptance review
and level 9 a review of the results of commissioning.
The adoption notice makes those three reviews conditions of the three levels.
It also rules that an element reaches level 8 only when the system that contains it passes its acceptance review,
whatever the place of the element in the product tree.
The handbook states the limits of any assessment in one sentence.
"The measure provided by TRL assessment is valid for a given element, at a given point in time, and a given defined environment."

Each regime has a record of the assessment.
NASA's guide lists six contents for the report that goes to the authority who called for the assessment.

1. A synopsis of the requirements and agreements between the customer and the deliverer of the technology.
2. The identification of the critical technology elements.
3. A scored level for each of them,
   by subject matter experts,
   with the objective evidence for the score.
4. The tests and levels of integration needed to demonstrate readiness,
   as captured in the plans for maturing each element.
5. A risk assessment for each element,
   if requested.
6. Any additional findings of the review team.

The European record is a list,
the technology readiness status list of the systems engineering standard,
which the supplier maintains and gives to the customer at the reviews of the early phases.
It has eight columns,
namely the critical function,
the technology or element,
the level currently declared and verified,
the reference of the assessment report,
the date of the report,
the points that support the declared level,
the forward plan with its target level and date,
and whether the item is a candidate for the list of critical items.

Both regimes commonly expect level 6 before a technology enters the main design work.
NASA's handbook says that,
typically,
"a TRL of 6 (i.e., technology demonstrated in a relevant environment) is required for a technology to be integrated into an SE process."
The European handbook says that
"it is considered normal practice to achieve TRL 6 prior to entering the detailed definition phase (Phase C)."
In the first sentence SE stands for systems engineering.
Given the difference between the scales,
the two thresholds share a number and not necessarily a meaning.

NASA's guide says that it does not address the maturity of software.
The directive's table gives each level a description for software,
and the European handbook has annexes for software and for electronic components.

### Heritage

Heritage is the word for prior use,
and NASA's guidance defines it by the evidence that prior use leaves
[NASA 2016a][agency_nasa_seh_expanded_vol1].
"“Heritage” refers to the original manufacturer’s level of quality and reliability that is built into parts and which has been proven by (1) time in service, (2) number of units in service, (3) mean time between failure performance, and (4) number of use cycles."
The definition is about the maker as much as the design.
A product has high heritage when it comes from the original supplier with its design and manufacture largely unchanged,
and low heritage when another maker built it,
when it has little history of test and use,
or when someone has altered its design or manufacture.
Heritage also depends on where the product serves.
"A product that has high heritage in a ground-based application could have a low heritage when placed in a space environment."

The guidance draws two consequences.
A heritage review confirms that a component suits its new application,
by comparing interfaces,
performance
and the environments of the unit's earlier qualification,
and it records each noncompliance with either a modification or a waiver.
And a change resets the claim.
"This affects the product’s heritage, and therefore, the modified product should be treated as a new design."

The handbook connects heritage to the readiness scale by a chart of questions.
The first question asks whether an identical unit has flown in the same conditions.
"Has an identical unit been successfully operated/launched in identical configuration/environment?"
A yes gives level 9.
If the identical unit flew in a different configuration or architecture,
the level drops to 5 until someone evaluates the differences.
An identical unit that is flight qualified and has not flown gives level 8.
A prototype shown in a relevant environment gives level 6.
The handbook's text warns that further analysis of a reused system may raise the result to level 6 or 7,
and that the system is in any case no longer at level 9.

The European documents do the same work with the four product categories.
For a product in category A the earlier assessment remains valid.
A product in category B takes level 6 for the project that reuses it.
A product in category C needs a new assessment,
and a product in category D needs a first one.

No document read here defines flight heritage in a glossary.
Three passages come near.

- **A Goddard design rule.**
  Rule 1.11 of the Goddard design rules recommends that a project qualify heritage flight hardware fully for its new application,
  calls itself a guideline,
  and in its rationale describes the term without fixing it
  [NASA 2025a][agency_nasa_gsfc_std_1000i].
  "The guideline is written to acknowledge that the definition of flight heritage not only includes having flown on a mission, but also the specific environment (thermal, structural, radiation) and how the item was used."
- **A Goddard assessment rule.**
  The Goddard process reproduced in NASA's guide to readiness assessment asks for proof.
  "Built-to-print flight-proven component, same environment = TRL 9. (Must substantiate with flight history)"
  The same process asks four questions of any claim,
  namely what the heritage is,
  what changes the project contemplates,
  how the old environments compare with the new,
  and whether the changes drive the technology.
- **A European table for electronic components.**
  An annex of the European handbook gives level 9 a duration for components.
  "The component has achieved flight heritage as per qualification envelope or under specific mission approval constraints after a typical duration of two years of nominal performance under nominal mission conditions."

The common content of the three is that flight alone is not heritage.
The claim needs the same design,
the same environment,
the same use
and a record that someone can inspect.
That summary is the author's.
The author did not search the European glossary for the word,
since the author could read only part of that document.

## Published Vehicle Documents

The documents described so far stay inside a programme.
What an outsider sees is a different family,
written for customers,
crews
and the public.
This section reads them as worked examples.
The examples are four current user's guides of launch operators,
one legacy guide,
a flight manual of 1968,
a NASA reference guide of 2025
and seven data sheets.

### User's Guides and Their Chapters

The four current guides are the Falcon User's Guide,
Version 8 of March 2025,
the Ariane 6 User's Manual,
Issue 2 Revision 0 of February 2021,
the Vulcan Launch Systems User's Guide of October 2023
and the Electron Payload User's Guide,
Version 7.0 of 1 November 2022
[SpaceX 2025][spacex_falcon_users_guide_v8]
[Arianespace 2021][arianespace_ariane_6_users_manual]
[ULA 2023][ula_vulcan_users_guide_2023]
[Rocket Lab 2022][rocket_lab_electron_pug_7].
The legacy guide is the Atlas V Launch Services User's Guide,
Revision 11 of March 2010,
which the author uses because it prints things that the current guides omit
[ULA 2010][ula_atlas_v_users_guide_2010].
The author did not confirm that each is the latest revision.

A user's guide is a planning document and says so.
The Falcon guide
"is not intended for detailed design use."
The Electron guide
"is provided for planning purposes only and is superseded by any mission specific documentation provided by Rocket Lab."

All four current guides have the same five blocks,
whatever their chapter titles.
They are a description of the vehicle,
its performance,
the flight environments,
the payload interfaces,
and the launch site with its operations.
Three add a chapter on mission integration.
The Falcon and Ariane 6 guides have chapters on the design and verification requirements that a spacecraft must meet,
and the Vulcan guide has a section.
Safety is a chapter of its own only in the Falcon guide.
The author infers that the five blocks and mission integration are the stable core of the genre.

### The Parameters of a Vehicle Description

The parameters by which a guide describes its vehicle are fewer than a reader might expect.
The table below records what the overview of each guide states in its text.
A value that exists only inside an image would escape it.

| Parameter | Stated by | Not stated by |
|---|---|---|
| Height or length of the vehicle | Falcon, Electron, and Atlas V for each element | Ariane 6 and Vulcan, which give the fairing only |
| Diameter | Falcon, Vulcan, Electron, and Atlas V for each element | Ariane 6, which gives the fairing only |
| Lift-off mass | Electron, and Atlas V as inert and propellant mass for each element | Falcon, Ariane 6, Vulcan |
| Number and type of engines | Falcon, Vulcan, Electron, Atlas V | Ariane 6, which gives names only |
| Thrust at sea level | Falcon, Vulcan, Electron, Atlas V | Ariane 6 |
| Thrust in vacuum | Electron, Atlas V, and Falcon for the upper stage | Ariane 6, Vulcan |
| Specific impulse | Electron, Atlas V | Falcon, Ariane 6, Vulcan |
| Propellants | Falcon, Vulcan, Electron, and Atlas V with masses | Ariane 6, which does not tabulate them |
| Stage burn time | Electron for the upper stage | Falcon, Ariane 6, Vulcan, Atlas V |
| Fairing dimensions | All five | None |

No current guide states everything.
Of the four,
only the Electron guide states a lift-off mass and a specific impulse,
and the Ariane 6 manual gives neither a thrust nor a mass.
The fullest description is in the legacy guide,
whose exploded view gives each element a block of values.
The block for the Atlas V booster reads as follows in Revision 11.
"Propellant: 284,089-kg (626,309 lbs) LO2 & RP-1"
"Inert Mass: 21,054 kg (46,416 lbs)"
"SL 100% Thrust = 3,827 kN (860,309 lbf), ISP = 311.3 s"
In that block LO2 is liquid oxygen,
RP-1 is the kerosene fuel,
SL is sea level
and ISP is specific impulse.
Each thrust carries its condition,
and inert mass and propellant mass stand apart.

The current guides use two forms.
The Falcon guide has a table of characteristics with a column for each stage,
whose rows cover structure,
propulsion,
attitude control
and operations.
Version 7.0 of the Electron guide has a card of labelled values.
"VEHICLE MASS (LIFT-OFF) 13,000 kg"
"5600 LBF Sea Level (Per Engine)"
The card mixes unit systems,
with metric mass and dimensions beside thrust in pounds of force.

### One Guide, Two Values

Version 8 of the Falcon guide gives the total thrust of the first stage twice,
and the two values differ.
The prose gives one figure.
"for a total thrust of 7,605 kN (1,710,000 lbf) at liftoff"
The table gives another against the same figure in pounds,
in a row that goes on to the second stage.
"Thrust (stage total) 7,686 kN (sea level) (1,710,000 lbf) 981 kN (Vacuum) (220,500 lbf)"
The guide gives the thrust of one engine as 845 kilonewtons or 190,000 pounds of force,
and nine times those values is 7,605 kilonewtons and 1,710,000 pounds of force.
The prose is therefore consistent with the engine figure and the table is the odd one.
Which value is correct the author cannot say.

The lesson does not depend on the answer.
A document that states a quantity in two places can come to state two quantities.
A sheet should give each value once,
with its condition and its source,
and should refer to that one place from everywhere else.

### How Performance Is Stated

The guides state performance in three ways.

- **Withheld.**
  The Falcon guide publishes the orbits it serves and no mass.
  "Mass-to-orbit capabilities for the Falcon 9 and Falcon Heavy fairing configuration are available upon request."
- **Point values.**
  The Ariane 6 and Vulcan guides give one value for each reference orbit and each configuration.
  The Vulcan guide of October 2023 lists 16,300 kilograms to the orbit of the space station,
  at an inclination of 51.6 degrees,
  for its configuration with two solid boosters and the standard fairing.
- **Curves.**
  The Electron guide plots payload mass against circular altitude,
  with one curve for each inclination.

A value of performance means little without its assumptions,
and two guides state theirs.
The Ariane 6 manual first defines the mass it quotes,
which includes the separated spacecraft,
any structure for carrying two spacecraft
and the adapter.
It then lists the assumptions.
"Launch at the CSG (French Guiana) taking into account the relevant CSG safety rules."
"Sufficient propellant reserve is assumed to reach the targeted orbit."
"Altitude values are given with respect to an Earth radius of 6,378 km."
Here CSG is the Guiana Space Centre.
The list also limits the aerothermal flux at the jettison of the fairing.
For its standard transfer orbit,
with a perigee altitude of 250 kilometres,
Issue 2 Revision 0 says that
"The Ariane 64 performance for this orbit is up to 11,500 kg."

The Vulcan guide defines its mass in the same inclusive way and then states its margin.
"Propellant reserves are held back to cover estimated 2.33-sigma Vulcan Centaur performance dispersions."
The legacy Atlas V guide explains the figure.
"Historically, commercial Atlas missions have been designed with a 2.33-sigma performance confidence level (99% probability of achieving target orbit elements within guidance injection accuracy)."
The Electron guide states no margin,
no confidence level
and no definition of what its payload mass includes.
The author infers that a statement of performance needs four things beside the number,
namely the orbit,
the launch site,
what the mass includes
and the confidence level.

### Environments and Interfaces

Each guide lists the environments that a payload must survive.
All four give acceleration or quasi-static loads,
acoustics,
shock,
thermal and humidity conditions,
the pressure in the fairing as it vents
and radio-frequency levels.
What matters for a sheet is that each guide also states the statistical basis of its levels
and whether they include a test margin.

- **Falcon.**
  "Provided loads are maximum flight loads (limit level) and do not contain a qualification factor"
  and the acoustic levels are a spatial average at a stated percentile.
- **Ariane 6.**
  The manual gives limit loads.
  "The related probability of these figures not being exceeded is 99 %."
- **Vulcan.**
  "All flight environments defined in this section are maximum expected levels and do not include margins typically associated with qualification tests."
- **Electron.**
  "The loads and environments provided in this section are for reference only"
  and the final values come in the interface control document of the mission.

The descriptions of interfaces share a form.
They give a coordinate system,
the envelope inside the fairing,
a mechanical interface identified by its diameter,
limits on mass and centre of gravity,
the electrical connections
and the means of verification.

### The Saturn V Flight Manual

The historic example is the flight manual for the Saturn V vehicle numbered SA-503,
dated 1 November 1968
[NASA 1968][agency_nasa_saturn_v_flight_manual_sa503].
Its foreword says that its authors prepared it for the astronauts,
and it disclaims authority.
"This manual is for information only and is not a control document."
It describes one vehicle and one mission.
Its ten sections cover a general description,
performance,
emergency detection and procedures,
each of the three stages,
the instrument unit,
the ground support interface,
mission control monitoring,
and mission variables and constraints.

One figure of the general description is a specification sheet in all but name.
It fits on a page,
beside a drawing of the vehicle marked with its height of 363 feet,
and it holds four tables.
The first summarises the solid ullage rockets and retrorockets.
The second gives engine data.
The third gives the dimensions and weights of the stages.
The fourth names the manufacturer of each stage.
Two of the tables follow in part.

| Stage | Engines, with nominal thrust each and in total | Burn time |
|---|---|---|
| S-IC | Five F-1, 1,522,000 and 7,610,000 | 150.7 seconds |
| S-II | Five J-2, 228,000 and 1,140,000 | 367 seconds |

| Stage | Diameter and length | Weight dry and at launch |
|---|---|---|
| S-II | 33.0 feet and 81.5 feet | 88,400 and 1,034,900 pounds |
| S-IVB | 21.7 feet and 59.3 feet | 33,142 and 262,300 pounds |

The figure prints no unit in its thrust cells,
and the author takes the unit to be pounds.
A note at its foot says that the thrust values,
weights
and burn times are all approximations.
The figure therefore separates dry weight from weight at launch,
gives thrust for one engine and for the stage,
and labels its own precision.

The manual states one quantity in three places.
Its figure gives the total thrust of the first stage as 7,610,000,
its section on that stage gives another value,
and its section on performance gives a third,
approximate value in prose.
"nominal sea level thrust of 7,650,000 pounds total, and have a burn time of 150.7 seconds"
The manual does not reconcile them,
and it does not say whether they describe different conditions or differ only by rounding.

Three other forms in the manual are worth copying.
The propellant of each stage has its own table,
and the text explains that the tables
"break down propellant use into such categories as usable, unusable, trapped, buildup and holddown, mainstage, thrust decay, and fuel bias."
The mission appears as a table of events,
each with a time from first motion and a time from a reference event.
And the performance section states a margin as two numbers.
"The nominal payload capability is 95,557 pounds and the required payload is 87,700 pounds."
The difference is 7,857 pounds.
Specific impulse does not appear in the summary figure.
The manual gives it only as a curve against mixture ratio in the section on the second stage.

Two companion documents show how NASA described the same family of vehicles for other readers.
The press kit for the first Saturn V flight gives its figures in prose
[NASA 1967][agency_nasa_apollo_4_press_kit].
"It is 363 feet tall and its first-stage engines produce 7,500,000 pounds of thrust at liftoff. Weight fully fueled is 6,220,025 pounds."
The flight manual,
a year later and for a different vehicle,
gives a gross weight before launch of about 6,094,073 pounds.
The two documents describe different vehicles,
and a reader should not expect their figures to agree.
A technical information summary for the Apollo 11 vehicle is a book of numbered figures
that repeats one sequence for each stage,
namely configuration,
engine system,
propellant system,
thrust vector control,
electrical power
and telemetry
[NASA 1969][agency_nasa_tis_as506].
The author infers that a sheet must name the serial number of the vehicle it describes
as well as its own revision.

### The Space Launch System Reference Guide

NASA's current public description of a launch vehicle is the reference guide to the Space Launch System.
The edition for the Artemis II mission carries the date October 2025
[NASA 2025b][agency_nasa_sls_reference_guide_2025].
It runs from the mission through a section of vehicle data,
the launch flow
and the background of the programme
to the elements one by one,
the facilities
and the industry partners.
Its overview is a list of labels and values in two unit systems.
"Height: 322.4 ft. (98.27 m)"
"Launch thrust: 8.27 million lbs. (36,787 kN)"
"Payload to TLI: > 59,525 lbs. (27 t)"
Here TLI is translunar injection.
A footnote marks the whole block.
"*Data are approximate"
Each element then repeats a fixed set of labels,
namely the contractor,
height,
diameter,
weight fuelled and unfuelled,
propellant,
thrust
and burn time.
Specific impulse is absent,
as it is from most of the user's guides.

The guide also shows how converted values drift.
The edition of 2022 prints the same height with a different conversion
[NASA 2022b][agency_nasa_sls_reference_guide_2022].
"Height: 322.4 ft. (98.3 m)"
The customary value did not change between the editions and the metric value did.
A sheet should state which unit is the source and which is the conversion.

### Engine Data Sheets

Engine makers publish what vehicle guides leave out.
The author read four sheets.
Two are specification sheets of L3Harris dated July 2024,
for the RL10 and the RS-25
[L3Harris 2024a][l3harris_rl10_spec_sheet]
[L3Harris 2024b][l3harris_rs25_spec_sheet].
One is a NASA fact sheet on the RS-25
[NASA 2015][agency_nasa_rs25_fact_sheet].
One is an undated ArianeGroup data sheet for the Vinci engine
[ArianeGroup Vinci][arianegroup_vinci_data_sheet].
The RL10 and Vinci sheets came from an archive,
because their makers no longer serve them.

| Sheet | Fields |
|---|---|
| RL10 | Launch vehicle, model, thrust, weight, fuel, oxidiser, nominal mixture ratio, specific impulse, length, nozzle diameter and a list of milestones |
| RS-25, maker | Thrust at sea level and in vacuum, throttle range, pump and chamber pressures, specific impulse in vacuum, pump power, area ratio, dry weight, mixture ratio, dimensions and propellants |
| RS-25, agency | Thrust, size and weight, operational thrust level, operational time and temperature range |
| Vinci | Cycle, vacuum thrust, specific impulse, combustion pressure, mixing ratio, propellants, flow rates, nozzle diameter, turbopump speeds and height |

The common fields are thrust with its condition,
specific impulse,
mixture ratio,
propellants,
dimensions
and mass.
The better sheets name the operating point.
The heading of the RS-25 sheet names one power level,
and the Vinci sheet gives two columns of values for two operating points.
"Specific impulse (s) 457.2 458.2"
The RL10 sheet gives one row of specific impulse across six models
and does not say whether its thrust and specific impulse are vacuum values.
The two RS-25 sheets,
one from the maker in 2024 and one from NASA in 2015,
differ by one pound in dry weight.
They are two sources that disagree,
and a sheet that cites one should name it.

### Satellite Bus Data Sheets

Three sheets for small satellite buses come from NASA's Rapid IV catalogue of spacecraft.
They are a Blue Canyon Technologies sheet for a bus called Venus-100,
a Lockheed Martin sheet of 2022
and a Ball Aerospace sheet of 2020
[Blue Canyon Technologies Venus-100][bct_venus_100_sheet]
[Lockheed Martin 2022][lockheed_martin_lm4xx]
[Ball Aerospace 2020][ball_bcp_small].
The first uses a table with a column for the specification,
one for its units
and one for the value.
Its rows include payload power,
the maximum payload mass,
the dry mass of the bus without payload,
data rate and storage,
pointing knowledge,
pointing control,
jitter,
slew rate,
design life,
compatible launch vehicles,
orbits
and payload volume.
The author infers from its layout that the catalogue supplies the table,
and could not confirm that from the catalogue itself.

The three sheets state heritage in four forms.

1. **A named mission.**
   The first sheet has a row for the names of heritage missions.
2. **A readiness level and counts.**
   The same sheet says that its bus inherits components
   "from our catalog of TRL-9 flight-proven buses"
   and counts the missions that its maker has supported.
3. **A dated lineage.**
   "The baseline LM4XX bus uses single string avionics flown on our heritage spacecraft, the Gravity Recovery and Interior Laboratory (GRAIL), launched in September 2011."
4. **A comparison.**
   The third sheet sets the flown bus beside the offered one,
   column against column.

The counts in the second form describe the maker and not the bus.
None of the three sheets states a failure,
an anomaly
or the number of units of the offered bus that have flown.
Design life appears with a probability of success,
as in the Ball sheet's
"(Ps >0.9 at 1 year)"
for its bus.

### Flight Record and Reliability

The guides state their records in five ways.

- **A dated count.**
  "As of the end of 2024, SpaceX has completed over 430 Falcon launches, making it the most flown U.S. launch vehicle currently in operation."
- **A family total.**
  The Ariane 6 manual of 2021 cites its predecessors,
  including the
  "74 consecutive successful flights from January 1995 to February 2003"
  of Ariane 4.
  Of Ariane 6 itself the same issue says that
  "The first flight is scheduled in 2022."
- **An inherited record.**
  "The Vulcan Centaur reliability model is directly derived from the Atlas and Delta reliability models and mission histories."
- **A count of payloads.**
  "More than 50 satellites have been deployed to orbit by Electron"
  is a count of satellites and not of launches.
- **Pedigree by serial number.**
  "Engines installed on the Artemis II core stage are serial numbers 2047, 2059, 2061, and 2062."

No current guide defines reliability or gives a count of failures.
The only definitions found are in the legacy guide.
"For the Atlas V program, reliability predictions are defined at two levels: design reliability and mission reliability."
Design reliability covers the failure modes that originate in the design of hardware.
"Mission reliability on the other hand, includes design reliability as well as failure modes introduced by manufacturing processes, assembly, test, and system integration."
For one configuration the table in Revision 11 gives 0.9954 for the first and 0.9867 for the second.
A third figure is a record and not a prediction.
"Atlas/Centaur demonstrated reliability record of 0.9838 (Duane Reliability Growth Method) is based on flight history through the fifteenth flight of the Atlas V LV"
Here LV stands for launch vehicle.
Three numbers thus stand under one word,
namely a prediction from the design,
a prediction updated with flight history
and a record computed from flights.
A sheet that states reliability should say which of the three it means.

### The Interface Control Document and the Questionnaire

In launch services the operator writes the interface control document and the customer supplies the inputs.
"SpaceX generates and controls the ICD, but input is required from the customer."
The Vulcan guide makes the signed document binding.
"The mission ICD is approved by the ULA mission manager and the customer and becomes a contractually binding document when signed."
Here ULA is United Launch Alliance,
the operator of the vehicle.
The Ariane 6 manual gives its equivalent precedence over every other technical document in the case of ambiguity.
The Vulcan practice matches the standards described above,
in which the parties to an interface sign its control document.

The inputs arrive as a questionnaire.
The Falcon guide lists seven deliverables for every payload,
among them safety data,
finite-element and design models,
inputs to the environmental analyses,
inputs to the interface control document
and a statement of environmental tests.
The one complete questionnaire found is in the legacy Atlas V guide,
a blank worksheet of six pages with a column for each of two unit systems.
Its sixteen headings run from trajectory requirements,
the mechanical interface,
the electrical interface
and the thermal and dynamic environments,
through the propulsion system,
tanks,
batteries,
transmitters,
ordnance
and contamination,
to the qualification test programme and the conditions of orbit injection.
The mass,
the centre of gravity
and the inertia of the spacecraft are rows under three of those headings.
The worksheet is the mirror image of a specification sheet.
It is the form on which the other party describes its vehicle.

## What the Practices Share

The regimes differ in vocabulary and agree in structure.
Twelve elements appear in most of them.
The list is the author's synthesis,
and each item names the sources behind it.

1. **State requirements and their verification together.**
   The defence standard puts requirements in section 3 and their verification in section 4 of every specification.
   The European standard makes verification one of its twelve types of requirement
   and demands that every requirement be verifiable by an approved method.
2. **Give every item an identifier that does not change, and every document a revision.**
   The European product tree gives each item an identification that stays fixed for the life of the product,
   unless a modification ends interchangeability.
   NASA's inactive standard lists the numbers that identify an item.
   The defence standard on data packages sets the minimum metadata of a drawing,
   and the European specification standard requires the revision of every document it cites.
3. **Describe the product as a hierarchy.**
   NASA has the product breakdown structure,
   the European standards the product tree
   and the defence handbook the indentured listing.
   The European specification tree must be coherent with the product tree.
4. **Fix the description at reviews and change it only by approval.**
   NASA's handbook,
   the defence handbook
   and the European standard all set baselines at named reviews,
   though they count four,
   three
   and five of them.
5. **Keep the record of the design apart from the record of the unit.**
   The defence handbook verifies the as-built against the as-designed.
   NASA requires as-designed and as-built parts lists.
   The European standards issue a data list for the design and a separate list for each serial number.
6. **List the parts three ways.**
   One list gives types with their source and approval,
   as in the European declared lists and NASA's parts list.
   One gives the structure in an indentured breakdown,
   as in the European data list,
   which adds quantities,
   and the indentured parts list of NASA's drawing package.
   One gives serial numbers,
   lot numbers
   and departures,
   as in the two as-built lists.
7. **State mass as an estimate, an allowance and a margin, each value with its basis.**
   The Goddard rule defines basic mass,
   growth allowance,
   predicted mass,
   allowable mass
   and margin.
   The cancelled defence handbook asks for the basis of each value,
   as an estimate,
   a calculation
   or a measurement.
   The European structural standard asks for contingency by design maturity,
   and the ESA document grades its margins by heritage.
8. **Let the margin fall as the design matures.**
   The Goddard table,
   the Expanded Guidance
   and the European margin policy all tie the required margin to the phase of the project.
9. **Give each interface a requirements document and a control document, and have the parties sign.**
   NASA's guidance and the European standard both do so,
   and the Vulcan guide makes the signed document binding.
10. **Let heritage set the qualification that a product owes.**
    The European categories A to D select no qualification,
    delta qualification
    or full qualification.
    NASA's guidance treats a modified product as a new design,
    and the Goddard rule recommends that a project qualify heritage hardware for its new application.
11. **Give each delivered version of software its own record.**
    NASA's version description and the European release document both identify the version,
    list its contents,
    state what changed
    and state its known problems.
12. **State maturity on a named scale, with evidence and a date.**
    NASA's directive and the ISO standard both have nine levels with evidence for each.
    The European handbook says that an assessment holds for one element,
    one time
    and one environment.

The published documents add a thirteenth element that the standards imply and do not state.
A number given to an outside reader carries its condition.
Thrust comes with sea level or vacuum,
performance with its orbit and its assumptions,
an environment with its statistical basis,
and a reliability with its kind.
The Saturn manual and the reference guide to the Space Launch System both label their figures as approximate.

The regimes differ on points that a designer of a document must decide.

| Point | NASA and United States defence practice | European standards |
|---|---|---|
| Baselines | Three or four, named functional, allocated, product and as-deployed, of which the binding directive names only the product baseline, once | Five, each tied to a review |
| Who designates the items | Not found in the documents read | The customer, unless delegated |
| Parts lists | Associated lists under a sold standard, with NASA lists for electronic parts and for materials | Four declared lists, a part number breakdown and an as-built list |
| Mass margin | Measured against an allowable mass and divided by basic mass in the Goddard rule | A fixed fraction of a nominal mass that already includes equipment margins, in the ESA document for early studies |
| Verification methods | Analysis, demonstration, examination and test | Test, analysis, review of design and inspection |
| Software grade | Classes A to F by the kind of system | Categories A to D by the consequence of failure |
| Readiness scale | The directive's own table | ISO 16290, which differs from it at levels 5 to 7 |
| Standing of the texts | Several are guidance, inactive, cancelled or sold | ECSS standards that are free to download, with three files that forbid the extraction of text, beside the sold ISO 16290 and ISO 22010 |

Four of these are choices that a small programme cannot avoid.
It must pick a denominator for its margin.
It must pick a readiness scale.
It must pick a scheme for grading its software.
And it must decide how many baselines its vehicles need,
which for a design that one team both specifies and builds may be fewer than any regime names.
The last remark is the author's view.

## A Specification Sheet for a Small Programme

A small programme cannot keep a design definition file,
four declared lists
and a verification control document for every vehicle.
It can keep their structure on a few pages,
because each of those documents answers a question that a short table can also answer.
The structure below is the author's consolidation for a programme of that size,
such as a campaign of simulated flights.
Each part names the documents it comes from.

One caution about the name comes first.
The defence standard already defines a specification sheet as the requirements for one model under a general specification.
The sheet proposed here is a description and not a set of requirements.
It is nearer to a manufacturer's data sheet joined to a short design definition file,
and a programme that adopts the name should say so.

### The Sheet

| Part | Content | After |
|---|---|---|
| Identification and configuration | The name of the vehicle, an identifier that never changes, the revision and date of the sheet, the state of the design that it describes, the author, the approver and what the sheet supersedes | The European product tree and design definition file, the defence metadata for design data, the user's guides |
| Description | The purpose of the vehicle, its concept, the phases of its mission and its elements as a product tree with an identifier for each | The European technical requirements specification and product tree, the Saturn manual |
| Mass statement | For each element the basic mass, its basis, the growth allowance and the predicted mass. Dry mass apart from propellant, and propellant by category. The allowable mass, and the margin with its denominator. Mass at each event of the mission | The Goddard rule, the cancelled defence handbook, the Saturn manual, the Apollo 11 mission report |
| Bill of materials | An indentured list of parts with the quantity of each in its next higher assembly, its source, its heritage category and its status | The European data list and declared lists, the defence parts list, the NASA parts lists. The heritage category follows the product categories of the European verification standard |
| Performance | Each value with its orbit, its launch site, what the mass includes and the reserve or confidence level. Engine data with the operating point | The Ariane 6, Vulcan and Atlas V guides, the engine data sheets |
| Interfaces | For each interface the plane, the coordinate system, the units, the limits and who controls it | NASA's outline of the requirements document, the European interface standard |
| Control software | The name and version of each program, its grade with the scheme named, the inventory of its files with checksums, the means needed to build it, the changes since the previous version, the known problems and the advice for use | NASA's version description, the European release document and configuration file |
| Verification status | For each claim the method, the evidence and whether the claim is closed | The European verification control document, section 4 of the defence specification |
| Readiness and heritage | The level of each critical element with the scale named, the date and the evidence. The heritage category, what is reused, what changed and how the environments compare | NASA's directive, ISO 16290 through the European handbook, the European product categories, the Goddard rules |
| Limitations | The known deviations, the open changes, the values that are approximate and the values that are not stated | The conclusion of the design definition file, the release document, the notes on the Saturn figure and the reference guide |
| History | When engineers could first have built a comparable vehicle | The author's addition |

### Rules of Use

Six rules go with the table.

- **State each value once.**
  The Falcon guide shows one quantity with two values,
  and the Saturn manual shows one quantity with three.
  Every other mention on the sheet should point to the one place where the value stands with its source.
- **Give each value its unit, its condition and its basis.**
  A thrust is at sea level or in vacuum.
  A mass is an estimate,
  a calculation
  or a measurement.
  Where the sheet converts a value,
  it says which unit is the original.
- **Name the scale and the scheme.**
  A readiness level names NASA's table or the ISO standard.
  A software grade names NASA's classes or the European categories.
  A margin names its denominator.
- **Keep the design apart from the unit.**
  The sheet describes the design.
  A separate short record describes each unit that departs from it,
  after the as-built lists.
  In a simulated campaign the unit is the vehicle as its operator configured it for one flight.
  That mapping is the author's and comes from no standard read here.
- **Write requirements and descriptions in measurable words.**
  The European list of banned terms applies to a sheet as well as to a specification.
- **Say what the sheet is not.**
  The user's guides call themselves planning documents,
  and the Saturn manual says that it is not a control document.
  A sheet should say which document governs when the two disagree.

### The History Section

The last row of the table has no standard behind it.
No document read for this article contains a section on when engineers could first have built a comparable vehicle.
Two established practices come nearest.

The first is the readiness level.
A level is a dated statement about one element in one environment,
and the European handbook says so in terms.
A history section asks the same question backwards.
It asks for the year by which each critical element of the vehicle could have reached a given level.
That restatement is the author's construction,
and the authors of neither scale wrote it for use on the past.

The second is the assessment of heritage.
The Goddard process asks what the heritage is,
what changes the project contemplates,
how the environments compare
and whether the changes drive the technology.
The published data sheets answer in dated lineages,
such as a named spacecraft and the month of its launch,
and in lists of milestones.
A history section can borrow that form.
For each major element it can name the earliest comparable item that flew,
with a date and a source,
and state what differs between that item and the element on the sheet.

The author suggests three rules for such a section,
none of which any standard states.
It should separate what flew from what engineers could have built,
since the first is a fact with a source and the second is a judgement.
It should name the element that sets the date,
since a vehicle is as early as its latest technology.
And it should carry its own degree of confidence.
The section itself remains an addition to established practice,
and the sheet should label it as one.

## Epistemic State

**Facts and their sources.**
The requirements and contents described above come from the documents themselves.
The author saved a copy of each,
confirmed its number,
issue
and date from its own cover or header,
and matched each quotation against the saved text.
The main exceptions follow.

- **Three European files that forbid the extraction of text.**
  They are the interface standard ECSS-E-ST-10-24C Rev.1,
  the glossary ECSS-S-ST-00-01C Rev.1
  and the adoption notice ECSS-E-AS-11C.
  The author transcribed passages from them by hand.
  Two quotations in this article,
  both from the interface standard,
  rest on that transcription.
  Everything taken from the glossary and the notice is a paraphrase of a transcription.
  The author read only part of the interface standard and 18 of the 61 pages of the glossary.
- **Tables and figures read from images.**
  The author read eight items by eye from page images.
  They are the growth allowance table of the AIAA standard,
  the Goddard table of required margins,
  the baseline figure and the heritage chart of NASA's handbook,
  the summary figure of the Saturn manual,
  the form of MIL-STD-1374A
  and the mass properties table of the Apollo 11 report.
  The sequence of figures for each stage in the Apollo 11 technical information summary also comes from images of its contents pages.
  The growth allowance table is in addition a reproduction in a NASA memorandum and not the standard itself.
- **Military documents.**
  Every military document came from a mirror site,
  and the author judged its currency from the mirror's listings and not from the official index.
  MIL-STD-961E with Change 4,
  MIL-HDBK-61B
  and MIL-STD-31000B appear current.
  MIL-HDBK-61B supersedes MIL-HDBK-61A.
  Notices cancelled MIL-HDBK-1811 in 2017 and MIL-STD-1374A in 2005.
  The saved copy of MIL-STD-31000B has images for its first pages,
  so statements about what its text lacks cover the text layer only.
- **Sold standards.**
  The author did not read AIAA S-120A,
  ASME Y14.34,
  SAE EIA-649C,
  ISO 16290
  or ISO 22010.
  The article knows the first through the Goddard rule and a NASA memorandum,
  the second through its publisher's summary and a superseded handbook,
  the third through its publisher's summary,
  the fourth through the European handbook
  and the fifth through its catalogue entry.
  The United States parts list,
  the mass growth allowance
  and the European readiness levels are therefore each governed by a text that this article reports at second hand.
- **NASA documents of limited standing.**
  The Systems Engineering Handbook and its Expanded Guidance are guidance.
  NASA-STD-0005 has been inactive for new design since 2015,
  and its cover names SAE EIA-649-2 as its successor.
  GSFC-STD-1000 is the standard of one centre.
  The software handbook is a set of web pages that carry no revision date of their own,
  read as they stood in November 2026.
  The cover of the Systems Engineering Handbook carries no date,
  and the year in its citation comes from its catalogue record.
  The cover of the readiness assessment guide also carries no date,
  its catalogue record gives 2020
  and its file gives 2021.
- **The ESA margin document.**
  It dates from 2012,
  governs early studies
  and carries a marking for official use.
  The author quoted one sentence from it and did not look for a successor.
- **Expansions.**
  The expansions of CAGE,
  ESCC,
  LAT,
  LVT
  and RVT are the author's.
  The passages read print the abbreviations without them.
- **The origin of the readiness scale.**
  The author read neither the paper of 1989 nor the white paper of 1995.
- **Published vehicle documents.**
  Each number is what one revision of one document prints,
  and the author checked none against a second source.
  The Electron guide's cover gives 1 November 2022 for its version 7.0,
  while its revision history gives June 2022.
  The author did not confirm that any guide is the latest revision.
  The author read the Falcon cover date from an image.
  The RL10 and Vinci sheets came from an archive,
  and the Vinci sheet carries no date.
  The table of parameters rests on the text of each guide,
  so a value printed only inside an image would be missing from it.
  The author could not obtain the Saturn V manual for a later vehicle,
  the annex of the Ariane 5 manual that holds the customer's questionnaire,
  or the catalogue page that would confirm the origin of the bus table.
- **Tables.**
  The tables of sections,
  fields,
  margins
  and categories condense their sources and are not quotations,
  except where a cell stands in quotation marks.

**Dates.**
The author read the documents in November 2026.
NPR 7150.2D expires on 8 March 2027
and NPR 7123.1D on 5 July 2028.
ECSS revised its two software standards on 30 April 2025.
User's guides change without notice,
and the Ariane 6 manual cited here predates the vehicle's first flight by its own account.
A reader who relies on a clause or a number should check the current issue.

**Inferences.**
The following are inferences,
and the text names each as one where it appears.

- That the European specification describes need,
  concept
  and life before requirements while the defence specification does not.
- That approval of a European specification follows the baselines.
- That the European bill of materials is the product tree,
  the part number breakdown,
  the declared lists
  and the as-built list taken together,
  and that United States practice divides the function in the same way.
- That the three bases of a mass value in the defence handbook match the letters of the AIAA table.
- That the two regimes both layer an item allowance beneath a system margin and differ in the base of the second layer.
- That the formula for total dry mass expresses the ESA rules,
  which the document states in words.
- That the European review of design has no counterpart by name in the defence list of methods,
  and that a change of supplier alone moves a product to category C.
- That level 6 on NASA's scale corresponds to level 7 on the ISO scale.
- That NASA's software classes and the European criticality categories sort on different axes.
- That flight alone is not heritage in any of the three passages that come near a definition.
- That five blocks and mission integration are the stable core of a user's guide,
  that a statement of performance needs four things beside the number,
  and that the bus table is a catalogue template.
- That the thrust in the Saturn figure is in pounds,
  and that the Falcon table and not the Falcon prose holds the odd value.

**The author's view.**
The list of twelve shared elements with its thirteenth,
the table of differences,
the specification sheet,
its six rules,
the mapping of the as-built record onto one simulated flight
and the whole of the history section are the author's.
The author offers them as a reading of the documents,
open to disagreement on the evidence.
None of them is a requirement of any standard.

## Out of Scope

- **Other agencies.**
  The article covers NASA,
  United States defence documents,
  the European standards
  and one ESA document.
  It does not cover the agencies of Japan,
  Russia,
  China
  or India.
- **Aircraft.**
  Type certification and its data sheets belong to a different regime,
  and the article touches aircraft only to correct the scope of one weight form.
- **Engineering method.**
  The article describes documents.
  It does not teach requirements analysis,
  mass estimation,
  trajectory design
  or the calculation of propellant,
  and it prints no equation of propulsion.
- **Structural margins.**
  Factors of safety and margins of safety in the structural sense are a separate subject.
- **Test levels.**
  The article gives one example of qualification and acceptance levels and no more.
- **Safety and reliability analysis.**
  Hazard reports,
  range safety data
  and the methods of reliability prediction receive no treatment.
- **Drawings and models.**
  The standards for engineering drawings and for model-based definition lie beyond the lists that this article describes.
- **Law and contract.**
  The article describes what documents say and gives no advice on contracts or on export control.

## Conclusion

Space agencies and the aerospace industry describe a vehicle in a family of documents.
The specification states requirements and their verification,
in six fixed sections under the defence standard and in seven under the European one.
The configuration record names the items,
fixes baselines at reviews
and keeps the design apart from the unit.
The bill of materials has no document of its own.
A list of types,
an indentured breakdown with quantities
and an as-built list with serial numbers do its work.
The mass statement gives a basic estimate,
an allowance graded by maturity
and a margin against a limit.
Interfaces have a requirements document and a control document that the parties sign.
A delivered version of software has a record of its own.
Maturity has a scale of nine levels,
and heritage has rules that stop short of a definition.

Reading the documents corrects several things that are easy to believe.
NASA's binding directive does not name the classical baselines.
The European standard on configuration management defines neither the configuration item nor the baseline.
The defence standard on data packages does not define a parts list.
The aircraft weight form does not apply to space vehicles,
and a notice has cancelled it.
The readiness scales of NASA and of ISO do not assign the same meaning to every number.
And the texts that govern the United States parts list,
the mass growth allowance
and the European readiness levels are all sold,
so that a reader without them works from restatements.

The published documents teach a plainer lesson.
Operators state what serves a customer and omit the rest,
and a document that states a value twice can state two values.
A small programme can take the structure without the bulk.
A sheet of a few pages can carry an identity,
a description,
a mass statement with its margin,
a list of parts,
performance with its assumptions,
interfaces,
software with its version,
the state of verification,
readiness and heritage,
and limitations.
It needs each value stated once,
with its unit,
its condition,
its basis
and its source.
A section on when engineers could first have built a comparable vehicle is an addition to that practice,
and its writer does best to borrow the discipline of the two practices nearest to it.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 4 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 4, 3 are established and 1 are bespoke.
All four equations take masses in one consistent unit. The first three apply to dry mass only, and the percentage margin of the second is defined with the basic mass in the denominator. The fourth applies to the early study phases that its source governs.

**Equation 1, Predicted Mass.**
The predicted mass of an item is its basic mass plus its mass growth allowance.
[NASA 2025a][agency_nasa_gsfc_std_1000i]

$$
M_{\mathrm{P}} = M_{\mathrm{B}} + G
\tag{1}
$$

**Equation 2, Mass Margin in Percent of Basic Mass.**
The margin between the allowable mass and the predicted mass, expressed as a percentage of the basic mass.
[NASA 2025a][agency_nasa_gsfc_std_1000i]

$$
\mu = \frac{M_{\mathrm{A}} - M_{\mathrm{P}}}{M_{\mathrm{B}}} \times 100
\tag{2}
$$

**Equation 3, Fractional Growth Allowance.**
The growth allowance as a fraction of the basic value, found from the predicted and basic values.
[NASA 2016b][agency_nasa_seh_expanded_vol2]

$$
g = \frac{M_{\mathrm{P}} - M_{\mathrm{B}}}{M_{\mathrm{B}}}
\tag{3}
$$

*Equation 4, Bespoke Total Dry Mass Under Two Layers of Margin.*
The author's expression of the ESA rules, in which a system margin applies to the sum of the equipment masses after each has received its own maturity margin.

$$
M_{\mathrm{D}} = \left( 1 + s \right) \sum_{i} m_{i} \left( 1 + k_{i} \right)
\tag{4}
$$

### Notation

- $M_{\mathrm{B}}$, the basic mass
- $G$, the mass growth allowance
- $M_{\mathrm{P}}$, the predicted mass
- $M_{\mathrm{A}}$, the allowable mass
- $\mu$, the mass margin in percent of the basic mass
- $g$, the growth allowance as a fraction of the basic mass
- $M_{\mathrm{D}}$, the total dry mass at launch
- $s$, the system level mass margin as a fraction
- $m_{i}$, the estimated mass of equipment $i$ before any margin
- $k_{i}$, the design maturity margin of equipment $i$ as a fraction

## References

- [Reference, AIAA 2015, ANSI/AIAA S-120A-2015, Mass Properties Control for Space Systems][aiaa_s_120a_2015]
- [Reference, ArianeGroup Vinci, Vinci Engine Data Sheet, Undated, Archived Copy][arianegroup_vinci_data_sheet]
- [Reference, Arianespace 2021, Ariane 6 User's Manual, Issue 2 Revision 0][arianespace_ariane_6_users_manual]
- [Reference, ASME 2013, ASME Y14.34-2013 (R2024), Associated Lists][asme_y14_34]
- [Reference, Ball Aerospace 2020, BCP-Small Data Sheet, NASA Rapid IV Catalog][ball_bcp_small]
- [Reference, Banke 2010, Technology Readiness Levels Demystified][agency_nasa_banke_2010]
- [Reference, Blue Canyon Technologies Venus-100, Venus-100 Sheet, Version 4, NASA Rapid IV Catalog][bct_venus_100_sheet]
- [Reference, DoD 1977, MIL-STD-1374A, Weight and Balance Data Reporting Forms for Aircraft (Including Rotorcraft), Cancelled][mil_std_1374a]
- [Reference, DoD 1998, MIL-HDBK-1811, Mass Properties Control for Space Vehicles, Cancelled][mil_hdbk_1811]
- [Reference, DoD 2001, MIL-HDBK-61A(SE), Configuration Management Guidance, Superseded][mil_hdbk_61a]
- [Reference, DoD 2005, MIL-STD-1374A Notice 3, Notice of Cancellation][mil_std_1374a_notice_3]
- [Reference, DoD 2017, MIL-HDBK-1811 Notice 1, Notice of Cancellation][mil_hdbk_1811_notice_1]
- [Reference, DoD 2018, MIL-STD-31000B, Technical Data Packages][mil_std_31000b]
- [Reference, DoD 2020a, MIL-STD-961E with Change 4, Defense and Program-Unique Specifications Format and Content][mil_std_961e]
- [Reference, DoD 2020b, MIL-HDBK-61B, Configuration Management Guidance][mil_hdbk_61b]
- [Reference, ECSS 2008, ECSS-E-ST-32C Rev.1, Space Engineering, Structural General Requirements][ecss_e_st_32c_rev1]
- [Reference, ECSS 2009a, ECSS-E-ST-10-06C, Space Engineering, Technical Requirements Specification][ecss_e_st_10_06c]
- [Reference, ECSS 2009b, ECSS-M-ST-10C Rev.1, Space Project Management, Project Planning and Implementation][ecss_m_st_10c_rev1]
- [Reference, ECSS 2009c, ECSS-M-ST-40C Rev.1, Space Project Management, Configuration and Information Management][ecss_m_st_40c_rev1]
- [Reference, ECSS 2014, ECSS-E-AS-11C, Space Engineering, Adoption Notice of ISO 16290][ecss_e_as_11c]
- [Reference, ECSS 2017a, ECSS-E-HB-11A, Space Engineering, Technology Readiness Level (TRL) Guidelines][ecss_e_hb_11a]
- [Reference, ECSS 2017b, ECSS-E-ST-10C Rev.1, Space Engineering, System Engineering General Requirements][ecss_e_st_10c_rev1]
- [Reference, ECSS 2017c, ECSS-Q-ST-30C Rev.1, Space Product Assurance, Dependability][ecss_q_st_30c_rev1]
- [Reference, ECSS 2018, ECSS-E-ST-10-02C Rev.1, Space Engineering, Verification][ecss_e_st_10_02c_rev1]
- [Reference, ECSS 2019, ECSS-Q-ST-70C Rev.2, Space Product Assurance, Materials, Mechanical Parts and Processes][ecss_q_st_70c_rev2]
- [Reference, ECSS 2022, ECSS-E-ST-10-03C Rev.1, Space Engineering, Testing][ecss_e_st_10_03c_rev1]
- [Reference, ECSS 2023, ECSS-S-ST-00-01C Rev.1, ECSS System, Glossary of Terms][ecss_s_st_00_01c_rev1]
- [Reference, ECSS 2024, ECSS-E-ST-10-24C Rev.1, Space Engineering, Interface Management][ecss_e_st_10_24c_rev1]
- [Reference, ECSS 2025a, ECSS-E-ST-40C Rev.1, Space Engineering, Software][ecss_e_st_40c_rev1]
- [Reference, ECSS 2025b, ECSS-Q-ST-60C Rev.4, Space Product Assurance, Electrical, Electronic and Electromechanical (EEE) Components][ecss_q_st_60c_rev4]
- [Reference, ECSS 2025c, ECSS-Q-ST-80C Rev.2, Space Product Assurance, Software Product Assurance][ecss_q_st_80c_rev2]
- [Reference, ESA 2012, Margin Philosophy for Science Assessment Studies, SRE-PA/2011.097/, Issue 1 Revision 3][esa_margin_philosophy_2012]
- [Reference, Holladay et al. 2024, NASA/TM-20240014203, NASA Engineering and Safety Center Lunar Rover Design Concepts Assessments][agency_nasa_tm_20240014203]
- [Reference, ISO 2013, ISO 16290:2013, Space Systems, Definition of the Technology Readiness Levels (TRLs) and Their Criteria of Assessment, Catalogue Entry][iso_16290_2013]
- [Reference, ISO 2022, ISO 22010:2022, Space Systems, Mass Properties Control, Catalogue Entry][iso_22010_2022]
- [Reference, Kimmel et al. 2020, SP-20205003605, Technology Readiness Assessment Best Practices Guide][agency_nasa_tra_guide]
- [Reference, L3Harris 2024a, RL10 Propulsion System Specification Sheet, L26293, Archived Copy][l3harris_rl10_spec_sheet]
- [Reference, L3Harris 2024b, RS-25 Propulsion System Specification Sheet, L26301][l3harris_rs25_spec_sheet]
- [Reference, Lockheed Martin 2022, LM4XX Core Spacecraft Data Sheet, V3b, NASA Rapid IV Catalog][lockheed_martin_lm4xx]
- [Reference, NASA 1967, Apollo 4 Press Kit, News Release 67-275][agency_nasa_apollo_4_press_kit]
- [Reference, NASA 1968, MSFC-MAN-503, Saturn V Flight Manual SA-503][agency_nasa_saturn_v_flight_manual_sa503]
- [Reference, NASA 1969, Technical Information Summary, Apollo-11 (AS-506), Apollo Saturn V Space Vehicle, S&E-ASTR-S-101-69][agency_nasa_tis_as506]
- [Reference, NASA 1971, NASA SP-238, Apollo 11 Mission Report][agency_nasa_apollo_11_mission_report]
- [Reference, NASA 2008, NASA-STD-0005, NASA Configuration Management (CM) Standard, Inactive for New Design][agency_nasa_std_0005]
- [Reference, NASA 2015, NASA Facts, Space Launch System RS-25 Core Stage Engines, FS-2015-07-064-MSFC][agency_nasa_rs25_fact_sheet]
- [Reference, NASA 2016a, NASA/SP-2016-6105-SUPPL, Expanded Guidance for NASA Systems Engineering, Volume 1, Systems Engineering Practices][agency_nasa_seh_expanded_vol1]
- [Reference, NASA 2016b, NASA/SP-2016-6105-SUPPL, Expanded Guidance for NASA Systems Engineering, Volume 2, Crosscutting Topics, Special Topics, and Appendices][agency_nasa_seh_expanded_vol2]
- [Reference, NASA 2017a, NASA SP-2016-6105 Rev2, NASA Systems Engineering Handbook][agency_nasa_sp_2016_6105_rev2]
- [Reference, NASA 2017b, NASA-STD-8739.10, Electrical, Electronic, and Electromechanical (EEE) Parts Assurance Standard][agency_nasa_std_8739_10]
- [Reference, NASA 2020, NASA-HDBK-2203, NASA Software Engineering and Assurance Handbook, Version D, Topic 5.16, Version Description Document][agency_nasa_hdbk_2203]
- [Reference, NASA 2022a, NPR 7150.2D, NASA Software Engineering Requirements][agency_nasa_npr_7150_2d]
- [Reference, NASA 2022b, NASA's Space Launch System Reference Guide, Version 2, NP-2022-08-65-MSFC][agency_nasa_sls_reference_guide_2022]
- [Reference, NASA 2023a, NPR 7123.1D with Change 2, NASA Systems Engineering Processes and Requirements][agency_nasa_npr_7123_1d]
- [Reference, NASA 2023b, NASA-STD-6016C with Change 1, Standard Materials and Processes Requirements for Spacecraft][agency_nasa_std_6016c]
- [Reference, NASA 2025a, GSFC-STD-1000 Revision I, Rules for the Design, Development, Verification, and Operation of Flight Systems][agency_nasa_gsfc_std_1000i]
- [Reference, NASA 2025b, Space Launch System Reference Guide for Artemis II, October 2025][agency_nasa_sls_reference_guide_2025]
- [Reference, Rocket Lab 2022, Electron Payload User's Guide, Version 7.0][rocket_lab_electron_pug_7]
- [Reference, SAE 2019, SAE EIA-649C, Configuration Management Standard, Publisher's Page][sae_eia_649c]
- [Reference, SpaceX 2025, Falcon User's Guide, Version 8][spacex_falcon_users_guide_v8]
- [Reference, ULA 2010, Atlas V Launch Services User's Guide, Revision 11][ula_atlas_v_users_guide_2010]
- [Reference, ULA 2023, Vulcan Launch Systems User's Guide, October 2023][ula_vulcan_users_guide_2023]
- [Related Post, Safety-Critical Software, Aerospace, Programming Languages, and Information Technology Co-Development: Safety-Critical Software][related_post_safety_critical_software]
- [Research, Sadin, Povinelli and Rosen 1989, The NASA Technology Push Towards Future Space Mission Systems][research_sadin_1989]

[agency_nasa_apollo_11_mission_report]: https://ntrs.nasa.gov/api/citations/19710015566/downloads/19710015566.pdf
[agency_nasa_apollo_4_press_kit]: https://ntrs.nasa.gov/api/citations/19670031260/downloads/19670031260.pdf
[agency_nasa_banke_2010]: https://www.nasa.gov/aeronautics/technology-readiness-levels-demystified/
[agency_nasa_gsfc_std_1000i]: https://standards.nasa.gov/system/files/tmp/GSFC-STD-1000RevI_Approved_0.pdf
[agency_nasa_hdbk_2203]: https://swehb.nasa.gov/display/SWEHBVD/5.16+-+VDD+-+Version+Description+Document
[agency_nasa_npr_7123_1d]: https://nodis3.gsfc.nasa.gov/npg_img/N_PR_7123_001D_/N_PR_7123_001D_.pdf
[agency_nasa_npr_7150_2d]: https://nodis3.gsfc.nasa.gov/npg_img/N_PR_7150_002D_/N_PR_7150_002D_.pdf
[agency_nasa_rs25_fact_sheet]: https://www.nasa.gov/wp-content/uploads/2020/09/final_sls_rs25_fact_sheet_508_07312015.pdf
[agency_nasa_saturn_v_flight_manual_sa503]: https://ntrs.nasa.gov/api/citations/19750063889/downloads/19750063889.pdf
[agency_nasa_seh_expanded_vol1]: https://ntrs.nasa.gov/api/citations/20170007238/downloads/20170007238.pdf
[agency_nasa_seh_expanded_vol2]: https://ntrs.nasa.gov/api/citations/20170007239/downloads/20170007239.pdf
[agency_nasa_sls_reference_guide_2022]: https://www.nasa.gov/wp-content/uploads/2022/03/sls-reference-guide-2022-v2-508-0.pdf
[agency_nasa_sls_reference_guide_2025]: https://www.nasa.gov/wp-content/uploads/2026/01/sls-5558-artemis-ii-sls-reference-guide-final-review-508-012026.pdf
[agency_nasa_sp_2016_6105_rev2]: https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf
[agency_nasa_std_0005]: https://standards.nasa.gov/sites/default/files/standards/NASA/Baseline/0/nasa_std_0005_inactive_for_new_design_2015_03_09.pdf
[agency_nasa_std_6016c]: https://standards.nasa.gov/sites/default/files/standards/NASA/C-w/Change-1/1/2023-11-15-NASA-STD-6016C-w-Chg-1-Final_0.pdf
[agency_nasa_std_8739_10]: https://standards.nasa.gov/sites/default/files/standards/NASA/Baseline/0/nasa-std-873910.pdf
[agency_nasa_tis_as506]: https://ntrs.nasa.gov/api/citations/19700011707/downloads/19700011707.pdf
[agency_nasa_tm_20240014203]: https://ntrs.nasa.gov/api/citations/20240014203/downloads/11-15-24%2020240014203.pdf
[agency_nasa_tra_guide]: https://ntrs.nasa.gov/api/citations/20205003605/downloads/%20SP-20205003605%20TRA%20BP%20Guide%20FINAL.pdf
[aiaa_s_120a_2015]: https://doi.org/10.2514/4.103858
[arianegroup_vinci_data_sheet]: https://web.archive.org/web/20200923091648id_/https://www.ariane.group/wp-content/uploads/2020/06/VINCI_2020_04_DS_EN_Eng_Web.pdf
[arianespace_ariane_6_users_manual]: https://ariane.group/app/uploads/sites/4/2024/10/Mua-6_Issue-2_Revision-0_March-2021.pdf
[asme_y14_34]: https://www.asme.org/codes-standards/find-codes-standards/y14-34-associated-lists
[ball_bcp_small]: https://assets.science.nasa.gov/content/dam/science/cds/spacecraft-development/rsdo/rapid-iv-catalog/Ball_BCP_Small_Data%20Sheet.pdf
[bct_venus_100_sheet]: https://assets.science.nasa.gov/content/dam/science/cds/spacecraft-development/rsdo/rapid-iv-catalog/NASA%20RSDO%20Rapid_BCT%20Venus%20Marketing%20Sheet_v4.pdf
[ecss_e_as_11c]: https://ecss.nl/wp-content/uploads/standards/ecss-e/ECSS-E-AS-11C1October2014.pdf
[ecss_e_hb_11a]: https://ecss.nl/wp-content/uploads/2017/03/ECSS-E-HB-11A(1March2017).pdf
[ecss_e_st_10_02c_rev1]: https://ecss.nl/wp-content/uploads/2018/02/ECSS-E-ST-10-02C-Rev.1(1February2018).pdf
[ecss_e_st_10_03c_rev1]: https://ecss.nl/wp-content/uploads/2022/05/ECSS-E-ST-10-03-Rev.1(31May2022).pdf
[ecss_e_st_10_06c]: https://ecss.nl/wp-content/uploads/standards/ecss-e/ECSS-E-ST-10-06C6March2009.pdf
[ecss_e_st_10_24c_rev1]: https://ecss.nl/wp-content/uploads/2024/12/ECSS-E-ST-10-24C-Rev.1(15November2024).pdf
[ecss_e_st_10c_rev1]: https://ecss.nl/wp-content/uploads/2017/02/ECSS-E-ST-10C-Rev.1(15February2017).pdf
[ecss_e_st_32c_rev1]: https://ecss.nl/wp-content/uploads/standards/ecss-e/ECSS-E-ST-32C_Rev.115November2008.pdf
[ecss_e_st_40c_rev1]: https://ecss.nl/wp-content/uploads/2025/05/ECSS-E-ST-40C-Rev.1(30April2025).pdf
[ecss_m_st_10c_rev1]: https://ecss.nl/wp-content/uploads/standards/ecss-m/ECSS-M-ST-10C_Rev.16March2009.pdf
[ecss_m_st_40c_rev1]: https://ecss.nl/wp-content/uploads/standards/ecss-m/ECSS-M-ST-40C_Rev.16March2009.pdf
[ecss_q_st_30c_rev1]: https://ecss.nl/wp-content/uploads/2017/02/ECSS-Q-ST-30C-Rev.1(15February2017).pdf
[ecss_q_st_60c_rev4]: https://ecss.nl/wp-content/uploads/2025/05/ECSS-Q-ST-60C-Rev.4(30April2025).pdf
[ecss_q_st_70c_rev2]: https://ecss.nl/wp-content/uploads/2019/10/ECSS-Q-ST-70C-Rev.2(15October2019).pdf
[ecss_q_st_80c_rev2]: https://ecss.nl/wp-content/uploads/2025/05/ECSS-Q-ST-80C-Rev.2(30April2025).pdf
[ecss_s_st_00_01c_rev1]: https://ecss.nl/wp-content/uploads/2023/10/ECSS-S-ST-00-01C_Rev.1(11October2023).pdf
[esa_margin_philosophy_2012]: https://sci.esa.int/documents/34375/36249/1567260131067-Margin_philosophy_for_science_assessment_studies_1.3.pdf
[iso_16290_2013]: https://www.iso.org/standard/56064.html
[iso_22010_2022]: https://www.iso.org/standard/81693.html
[l3harris_rl10_spec_sheet]: https://web.archive.org/web/20251114072103id_/https://www.l3harris.com/sites/default/files/2024-07/l3harris-ar-rl10-spec-sheet.pdf
[l3harris_rs25_spec_sheet]: https://www.l3harris.com/sites/default/files/2024-07/l3harris-ar-rs-25-spec-sheet.pdf
[lockheed_martin_lm4xx]: https://assets.science.nasa.gov/content/dam/science/cds/spacecraft-development/rsdo/rapid-iv-catalog/LM4XX_Datasheet_V3b.pdf
[mil_hdbk_1811]: https://everyspec.com/MIL-HDBK/MIL-HDBK-1800-1999/download.php?spec=MIL-HDBK-1811.010230.PDF
[mil_hdbk_1811_notice_1]: https://everyspec.com/MIL-HDBK/MIL-HDBK-1800-1999/download.php?spec=MIL-HDBK-1811_NOTICE-1.055728.pdf
[mil_hdbk_61a]: https://everyspec.com/MIL-HDBK/MIL-HDBK-0001-0099/download.php?spec=MIL-HDBK-61A.015177.PDF
[mil_hdbk_61b]: https://everyspec.com/MIL-HDBK/MIL-HDBK-0001-0099/download.php?spec=MIL-HDBK-61B.056174.pdf
[mil_std_1374a]: https://everyspec.com/MIL-STD/MIL-STD-1300-1399/download.php?spec=MIL_STD_1374A.438.pdf
[mil_std_1374a_notice_3]: https://everyspec.com/MIL-STD/MIL-STD-1300-1399/download.php?spec=MIL-STD-1374A_NOTICE-3.029237.pdf
[mil_std_31000b]: https://everyspec.com/MIL-STD/MIL-STD-10000-and-Up/download.php?spec=MIL-STD-31000B.055788.pdf
[mil_std_961e]: https://everyspec.com/MIL-STD/MIL-STD-0900-1099/download.php?spec=MIL-DTD-961E_CHG-4.057000.pdf
[related_post_safety_critical_software]: {% post_url 2026-07-21-safety_critical_software %}
[research_sadin_1989]: https://doi.org/10.1016/0094-5765(89)90054-4
[rocket_lab_electron_pug_7]: https://rocketlabusa.com/assets/Electron-Payload-User-Guide-7.0-v6.pdf
[sae_eia_649c]: https://saemobilus.sae.org/standards/eia649c-configuration-management-standard
[spacex_falcon_users_guide_v8]: https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf
[ula_atlas_v_users_guide_2010]: https://www.ulalaunch.com/docs/default-source/rockets/atlasvusersguide2010.pdf
[ula_vulcan_users_guide_2023]: https://www.ulalaunch.com/docs/default-source/rockets/2023_vulcan_user_guide.pdf
