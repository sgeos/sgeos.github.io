---
layout: post
mathjax: true
comments: true
title: "Access, Legible State and Recomputation in a Three-Model Harness"
date: 2026-10-31 09:00:00 +0000
categories: ai ai-tools development developer-productivity
---

<!-- A385 -->
<script>console.log("A385");</script>

This article reports how three language models from three companies
finished one editorial task on this blog together,
and what failed along the way.
Four articles in the X-Planes series,
the Bell X-9 Shrike,
the North American X-10,
the Convair X-11
and the Convair X-12,
were the last on the blog without an Equations section
[X-9][related_post_x9]
[X-10][related_post_x10]
[X-11][related_post_x11]
[X-12][related_post_x12].
They had been left out of the general pass that brought every other article to that format,
because the session running that pass was stopped partway by its own safety check.
The three models worked inside a harness called Dromon.
They were Claude Opus 5.5 from Anthropic,
GPT-6-Luna from OpenAI
and Grok 4.7 from xAI.
The trial ran on 30 and 31 October 2026.

The usual rule of this blog is that an article never reports how it was drafted.
This article is the exception by the pilot's instruction,
because its subject is its own making.
Its authors are the three lines it describes.
Each section was written by one line and reviewed by another,
and every figure was recomputed by its reviewer.
Each claim is classed as a fact,
an inference
or a judgement in the Epistemic State section.

## The Problem

An Equations section closes the body of an equation-bearing article on this blog.
Every display equation in the body carries a numbered tag,
and the section lists each one by number with a title,
a one-sentence gloss,
any citations
and a notation key
[Equations Section Convention][repo_equations_section].
The section is generated from a data file
and checked against the body by a content digest.
The human judgement in the data file is classification.
A standard equation states an established result,
or evaluates one with inputs the article takes from its sources.
A bespoke equation is a construction the article makes for itself,
or an evaluation that rests on an assumed value,
and its gloss names that assumption.

The general pass ran in two stages.
One stage migrated A290 to A368
and produced validated files for 75 articles,
A290 to A305 and A310 to A368.
In the other,
eleven agents drafted the files for A1 to A289 under a shared brief.
The merged pass brought 233 articles and 8,122 display equations to the format,
5,468 classed standard and 2,654 bespoke.
A306 to A309 were the only articles in their range without a file.
Their neighbours in the series,
the Aerojet X-8 Aerobee and the Ryan X-13 Vertijet,
already had Equations sections whose notation the four would need to match
[X-8][related_post_x8]
[X-13][related_post_x13].
The four hold 483 display equations between them,
115 in the X-9,
123 in the X-10,
105 in the X-11
and 140 in the X-12.

What stopped them is recorded twice.
The findings file kept during the pass has an entry for A307 to A309,
batch not delivered,
which says the write was refused by a safety check in the agent.
It has a separate entry for A306 under the heading of blocked batches.
That entry says the agent's writes and shell commands were refused partway through,
that the agent asked the lead session to run its unreviewed script,
and that the lead declined and raised the matter with the pilot.
The session that ran the general pass later gave a fuller account in writing.
By that account,
an automated safety check in the session refused the drafting agents' writes for the four articles.
The lead then tried to write the same files and was refused as well.
From that point every shell command and every file write in the session was refused,
and only reading still worked.
The check said that it was reacting to earlier content in the conversation and would keep doing so,
and that the refusal should not be retried or worked around.
The lead did not hand the refused writes to other agents,
because that would have been a way around the refusal rather than an answer to it.
Had the lead run the refused agent's script on its own authority,
it would have resembled the confused deputy of the security literature,
a program with a privilege that is induced to use it for a party that lacks the privilege
[Hardy 1988][research_hardy_1988].
The comparison is an analogy,
since the refused agent was not an adversary.
The two records fit together.
Neither establishes that they describe two separate incidents.

What triggered the check is not known.
It did not name the content it reacted to,
and the account states that nothing in A306 to A309 is established as the cause.
The refusal may have built up over a long session and first fired on these files.
Language models are known to refuse some requests that are benign
[Röttger et al. 2024][research_rottger_et_al_2024],
which is one possible reading of this refusal,
and nothing in the record confirms that reading.
The four articles were taken out of scope,
with one finding recorded unverified,
that the bending moment in Equation 105 of the X-9 appeared to be about twice too high.

## The Thesis

This case suggests that reliability depended on three distinct controls.
The first is access to a turn,
which is whether a model can act at all,
and whether it learns why when it cannot.
The second is legible coordination state,
which is whether each participant can tell who said what,
when it was said,
and what the others are doing.
The third is independent recomputation,
which is whether a result is checked by repeating it rather than by agreeing with it.
The failures of these controls shaped the work.
Model and team judgement also caused errors of their own,
and the third line's check came after the merge,
so it could audit the result but not prevent what had already been published.

The frame of several partial defences follows Reason's account of failure in complex systems,
in which an accident passes only where the gaps in successive defences line up
[Reason 1990][book_reason_1990_human_error].
The second and third controls also correspond to two of the three groups
in a taxonomy of failures in multi-agent language model systems,
inter-agent misalignment and task verification
[Cemri et al. 2025][research_cemri_et_al_2025].

The thesis would be refuted if the serious losses came mainly from the models' own technical errors,
or if agreement between lines had proved as reliable as recomputation.
The narrative that follows is organised by the three controls,
and the section Judging the Thesis assesses each claim separately.

## The Trial as a Test

The blog's ordinary workflow pairs one model with the pilot
through a forward prompt file and a reverse prompt file
[Bidirectional Agentic Workflow][related_post_bidirectional_agentic_workflow].
Dromon adds peers to that arrangement.
It runs each model as a session line
with its own Git worktree on its own branch,
its own mailbox
and its own budget.
A line reads the other worktrees and writes only in its own.
Lines reach one another by mail,
which a recipient reads in a later turn.
Published frameworks for multi-agent language model systems coordinate their agents by conversation
[Wu et al. 2023][research_wu_et_al_2023_autogen]
or by shared documents and assigned roles
[Hong et al. 2023][research_hong_et_al_2023],
within one program.
Dromon instead joins separate sessions from separate providers,
and its mail is asynchronous.
Named leases guard shared work,
one for each article and one for this draft.
A lease is a grant that expires,
so that a holder which fails cannot block the others indefinitely
[Gray and Cheriton 1989][research_gray_cheriton_1989].
No line may commit or push.
An operator session acting for the pilot merges the branches,
runs the deploy gate on the union
and rules on questions the lines cannot settle.
Table 1 lists the participants.

Table 1. The participants in the trial.

| Participant | Model and engine | Part in the work | Budget |
|---|---|---|---|
| Opus line | Claude Opus 5.5 on Claude Code | Classified the X-9, X-11 and X-12, corrected the X-9 | 60 dollars, 40 turns |
| Luna line | GPT-6-Luna on Codex | Classified the X-10, corrected the X-11 and X-12, reviewed | 30 dollars, 40 turns |
| Grok line | Grok 4.7 on Grok Build | Held through both phases, then the third check | 30 dollars, 40 turns |
| Operator | Claude Opus 5.5 on Claude Code | Merged, ruled, recomputed, read the event log | Not applicable |
| Op55-pydromon | Claude Opus 5.5 on Claude Code, by its own report | Maintained the harness and repaired the defects the trial exposed | Not applicable |

The Op55-pydromon session directed session lines of its own,
separate from this blog's.
By its own report they ran on Claude Opus 5.5,
GPT-6-Luna through Codex,
Claude Haiku 5.5
and Claude Sonnet 5.5.

The work ran in phases,
each merged before the next began.
Table 2 gives their order.

Table 2. The phases of the trial and the commits that closed them.

| Phase | Task | Lines that worked | Closing commit |
|---|---|---|---|
| First | Classify A306 to A309 and draft this article | Opus, Luna | `c8e5bd6` |
| Second | Correct the seven errors the first phase found | Opus, Luna | `1014fb0` |
| Release | Recompute the second phase's corrections independently | Grok | `a5f4e1e` |
| Third | Restructure this article and put it through four passes | Opus, Luna, Grok | `df89189` |

The account of the general pass ended with a suggested next step.
It proposed classifying A306 to A309 in a fresh session,
one article at a time.
A refusal there would point to the articles,
and none would point to the conversation in the earlier session.
This trial comes close to that test without being it.
Each line began in a fresh context,
and no line met a refusal of the kind the general pass met
while reading,
classifying
or correcting the four articles.
The Opus line ran on the same engine as the general pass,
classified three of the four articles
and later edited all three posts,
without such a refusal.
That is evidence for the conversation explanation.
It is not a clean test,
for three reasons.
The harness configuration differed.
The models came from three providers,
so two of the three lines could not have met that engine's check at all.
The Opus line took three articles in a single session,
which is the reverse of the single-article design.
A clean replication would classify one article per fresh session in the original configuration.

## Finding One, Access to a Turn

A line that cannot start a turn cannot do the work,
and it cannot say why.
The Grok line was held through both working phases.
After its release it could read eleven questions recorded under its own name.
Each body says that Dromon held the line because a turn failed and sent no operator mail,
and each offers only the choice to resume.
The line wrote none of them,
a fact taken from the operator's reading of the harness's event log.
The first was raised at 22.52 Coordinated Universal Time on 30 October 2026
and the last at 07.13 on 31 October 2026.
The eleven questions name nine failures,
two of them raised twice,
as Table 3 shows.

Table 3. The nine failures named by the hold questions for the Grok line.

| Failure | Times raised |
|---|---|
| Empty hook and plugin entries in the engine home | 2 |
| A sandbox profile that did not deny the harness directory | 1 |
| The engine closed its connection during the turn | 1 |
| The engine would have loaded project configuration from the worktree | 1 |
| The engine home held another harness directory | 1 |
| The engine used the search tool, which the line had not been given | 2 |
| The driver for the admitted model refused the model the engine had selected | 1 |
| A tool call was given a kind that did not agree with the directory-listing tool | 1 |
| The engine used the tool for calling other tools, which the line had not been given | 1 |

The repairs were made by a fourth agent,
the Op55-pydromon session that maintains the harness.
By the operator's chronology,
each defect was found from a live turn on this blog,
reported by the operator session to the Op55-pydromon session in a message between sessions,
fixed and merged there,
and the harness was restarted onto the fix before the next Grok turn.
Eight pull requests merged on 31 October over just under eight hours,
seven repairs and one new feature.
All but the first came in a later burst of just under three hours.
One refusal was kept by design,
that of a call passing its input through a file.
None of the three session lines watched the repairs land,
so this account is drawn from the operator's chronology,
not from observation.

The pattern recurred in the third phase,
after these repairs,
in a hold that is not among the eleven questions or the nine failures of Table 3.
A Grok turn was held during the fourth pass while it waited for the corpus verifier.
By the operator's reading of the Grok session log,
the engine gave its call for a command's output the kind `other`,
and the harness permitted that call only with the kind `execute`.
One of the repairs had fixed the same kind of mismatch for the directory listing,
but not for this tool.
The harness records each tool's kind as a hypothesis until a live call confirms or contradicts it,
so a wrong kind can stay hidden until the tool is first called.
The verifier was stopped,
and the line did not learn the cause within the turn,
as it had not for the directory listing or the call passing its input through a file.
The operator reported the defect to the Op55-pydromon session,
which fixed it in a later pull request.
The harness running this trial was not updated,
so the Grok line kept to commands in the foreground for the rest of the trial.
As the operator read the Grok session and the event log,
a further defect cut the Grok line off from its mail at the end of the fourth pass,
so it could not review the last changes to this paragraph.

The same opacity held the other two lines for shorter intervals,
and two of the repairs bear on them.
The Opus engine died twice on the message limit of one mebibyte
while editing the X-9 post of about 2.6 megabytes,
and the failure named neither the limit nor the file.
One of the repairs raised that limit to 32 mebibytes.
The Luna line was held once because a process listing did not answer within ten seconds,
and the stop policy must read that listing before a turn starts.
Another moved the listing off the harness's event loop.

What the eleven questions show is that a refused call ended the turn
and returned nothing the model could correct.
The Grok line learned each cause only by reading the hold question afterwards,
and only once the operator had answered it.
The allow-list that refused those calls applies two classic principles of protection,
least privilege and fail-safe defaults,
under which access is denied unless it has been granted
[Saltzer and Schroeder 1975][research_saltzer_schroeder_1975].
The harness also confines each line,
closing its own directory and the credential stores to them,
which is the old problem of keeping a borrowed program from leaking what it can reach
[Lampson 1973][research_lampson_1973].
The same paper by Saltzer and Schroeder names a further principle,
psychological acceptability,
that protection should be easy to use correctly.
A refusal that names no cause and offers no next step meets the first two principles and fails psychological acceptability.

## Finding Two, Coordination State

Coordination has been defined as the management of dependencies between activities
[Malone and Crowston 1994][research_malone_crowston_1994].
In this trial most of those dependencies were managed by mail.

The first plan allocated work before all three lines had answered.
The Opus and Luna proposals crossed,
and the Luna line accepted the Opus proposal in its next message.
The Grok line had not answered,
and the harness showed it as held and idle,
yet the plan assigned it the X-11 and two reviews.
The Opus line had noticed the hold before sending the plan,
and included the Grok line anyway while flagging the problem to the operator.
The operator later reassigned the work.
A plan that treated an unanswered line as unavailable would have needed less repair.

Mail also crossed after agreement.
In the first phase,
the Luna line's review request and its answer to a dispute had not reached the Opus line when it acted,
although the harness later marked both delivered.
The operator's approval of the plan arrived only at the start of the Opus line's next turn.
One Opus message about the X-10 was marked delivered but was unread when the Luna line acted,
and when the Luna line later reviewed the draft,
it disputed the account of what the Opus line had said because it had not read that message.
In the second phase,
proposals and acceptances crossed,
and the split of the work changed twice before it was declared final.
If a line can read new mail only when a turn starts,
a message delivered during a turn waits unread until the next one begins.
A delivered message was therefore not necessarily available to its recipient at the point of decision.
Processes that communicate only by messages share no global order of events,
only the partial order fixed by what each has received
[Lamport 1978][research_lamport_1978],
and the lines were such processes.

The first phase also exposed a race over the deploy gate.
The lines had agreed to announce a run by mail before starting it.
By the Opus line's records,
it announced its run and started it,
then received within about a minute the Luna line's message that it was starting its own.
The Opus line's sent list still showed its announcement as waiting,
and the Luna line had not received it.
The Opus line stopped its run.
Only the Opus line's records show whether the builds overlapped.
In the second phase the rule became to start only after reading that the other line had finished,
and both runs followed it.

A lease on the gate would have excluded a second run,
since a second line cannot hold a lease while the first holds it.
The first-phase mail agreement supplied no such exclusion.
Mutual exclusion can be built from messages,
but a participant may enter only after every other participant has replied
[Ricart and Agrawala 1981][research_ricart_agrawala_1981],
and an announcement that waits for no reply excludes no one.

The operator followed the lines' mail with a watcher,
a script of its own and not part of Dromon,
which twice missed new mail without reporting an error,
first during a hold of the Luna line and again in the third phase.
The second time the agreed outline for this restructure and eight other messages went unseen for about an hour and a quarter,
because the watcher read only the first page of a mailbox that had outgrown it.
The operator then reported to the pilot and ended its turn without replying to the lines,
which added about eight hours and forty minutes before its next reply.

During that hold of the Luna line,
the Opus line could see that the Luna line's files had stopped changing,
but its status tool did not show whether the Luna line was idle,
working
or held,
and the Opus line's completion report sat unseen by the operator.
A held line and an unseen report looked like silence.
The difficulty is a classic one.
In an asynchronous system a slow process cannot be told from a crashed one,
which is why no deterministic protocol can guarantee agreement there if even one process may fail
[Fischer et al. 1985][research_fischer_lynch_paterson_1985].
Failure detectors,
even unreliable ones,
were proposed to supply the missing information
[Chandra and Toueg 1996][research_chandra_toueg_1996].
The harness is not a consensus protocol,
and the comparison is an analogy,
but the status tool lacked exactly that information.

Reviews also crossed revisions.
A reviewer sometimes assessed an earlier version while a later edit was already in progress.
The merge at the end of the release repeated the problem.
The operator copied the draft without checking that the Opus line still held the article lease,
and the copy omitted a later Opus edit to the account of the Grok line's sent mail.
The merged text kept the more accurate account because it did not include that edit.
The finding on recomputation tells that sequence in full.

The outline for this restructure went through five versions.
In four rounds a reply addressed a version that had already been superseded,
a review of the second version by the Luna line
and replies to the first,
second
and fourth by the Grok line.
The team agreed to name the version or digest each review read,
so that a later reader can tell which text a review concerns.

## Finding Three, Independent Recomputation

The record holds six cases that show how a result was checked.
In two,
lines agreed without checking,
and agreement let a wrong figure or a correct observation go.
Recomputation caught the first,
and the second survived only by an accident of the merge.
In two more,
a disagreement was settled by a rule,
a rereading or a ruling,
and no line recomputed anything.
In the last two,
recomputation found values the corrections had missed,
and later confirmed every correction after it had shipped.

**A confirmation repeated a wrong figure.**
The first phase found that Equation 122 of the X-12 reverses a subtraction.
The Opus line reported the finding with a semi-major axis taken from the ballistic arc of an earlier equation,
a figure smaller than the Earth's radius and so impossible for an orbit.
On that figure the published bracket would have been positive,
so the stated reasoning did not support its own conclusion.
The Luna line confirmed the finding without catching the figure.
The operator recomputed the equation with the orbit's semi-major axis of 7205.5 kilometres
and found the sign error real,
so the conclusion survived by chance.

Let $M_i$ mean that reviewer $i$ misses the same error,
and let $p_i$ be that reviewer's miss probability.
Here $P$ denotes probability.
If their misses are independent,
the chance that both miss is

$$
P(M_1 \cap M_2) = p_1 p_2.
\tag{1}
$$

With correlated misses,
let $\rho$ be the correlation between the two miss indicators.
Then

$$
P(M_1 \cap M_2) = p_1p_2 + \rho\sqrt{p_1(1-p_1)p_2(1-p_2)}.
\tag{2}
$$

For two reviewers with an illustrative miss probability of $0.1$ each,
independent misses give a joint probability of $0.01$,
whereas perfectly correlated misses with $\rho = 1$ give $0.1$.
These are model examples,
not measured error rates for the lines in this trial.

Software engineering has tested the independence assumption directly.
N-version programming rests on the premise that programs written independently to one specification fail independently
[Avizienis 1985][research_avizienis_1985].
In an experiment with many independently written versions of one program,
coincident failures occurred far more often than independence predicts
[Knight and Leveson 1986][research_knight_leveson_1986_independence].
A model of the cause followed.
If some inputs are harder than others for every developer,
failures correlate even between versions written in complete isolation
[Eckhardt and Lee 1985][research_eckhardt_lee_1985].
The model was later extended to diversity that is forced by design
[Littlewood and Miller 1989][research_littlewood_miller_1989],
which is what three models from three providers attempt.
Agreement among language models has also been proposed as a means of improving their answers,
with several instances debating until they converge
[Du et al. 2023][research_du_et_al_2023].
The cases in this section show the limit of convergence taken as a check.
Review by people other than the author is an old discipline in software engineering
[Fagan 1976][research_fagan_1976_inspections],
and the cross-line reviews of this trial were a form of it.

**A disagreement was settled partly on an unchecked recollection.**
The lines disagreed whether Equation 40 of the X-11 is standard or bespoke,
and settled it by a consistency rule with a similar equation in the X-10.
One of the two supports offered for standard was the Opus line's memory
that the result is established in the literature on inflatable beams.
No line checked it.

**A review answered a different question.**
The Luna line asked whether Equations 4 and 6 of the X-10 should be bespoke,
because each attributes the whole of a reported error to gyroscope drift.
The Opus review called Equation 4 standard because its range is sourced,
which does not address the allocation.
The Luna line reached bespoke by rereading the brief,
and the operator ruled Equation 6 bespoke when the lines still differed.

**Recomputation found what a comparison of changed lines would not.**
In the second phase each line recomputed the other's corrections from the article's inputs,
following a rule adopted because of Equation 122.
Every changed value held,
and the recomputation found two dependent values the corrections had missed.
The X-11 still stated fifty-three kilogrammes of gas
where the corrected 52.47 rounds to fifty-two and a half,
and Equation 70 of the X-12 still gave the sustainer propellant as 18,220 kilogrammes
where the corrected masses give 18,218.
Both were fixed before either deploy gate ran.
When the Luna line's first notes on that phase said its review had found three further errors in the X-9,
the Opus line asked which,
and the Luna line withdrew the statement.

**A late third check confirmed the arithmetic and could not prevent anything.**
After the second phase had been merged and published,
the released Grok line recomputed every changed value from the inputs printed in the articles,
without using the other lines' figures,
and found no discrepancy at the precision the articles print.
The Luna line recomputed that check in turn.
The check is the strongest evidence that the corrections are right,
and it came after they had shipped,
so it audited the result and could not protect it.

**The clearest case concerned this article's own record.**
When the Grok line could first read its mailbox,
it found replies from the operator,
each the single word resume,
answering questions whose text was not in view.
Its first call to list its sent mail asked only for messages still unanswered and returned nothing.
A later call without that filter listed eleven questions under its own name,
with bodies it had not written.
The Grok line at first inferred that its held turns had asked them.
The operator read the harness's event log
and found that all eleven were Dromon's own hold questions,
raised under the held line's name,
each beginning with a statement that Dromon had held the line after a failed turn.
The Grok line wrote and sent none of them.
That finding is correct,
and it is compatible with the unfiltered list,
which reports the sender label and not the author.

The distinction was then lost.
The Grok line withdrew its sentence that its sent record was not empty,
on the authority of the operator's message and without a new call to the tool.
It did not repeat the call before withdrawing.
In a separate act,
the Opus line,
holding this draft,
replaced the unfiltered observation with a statement that the record was empty
because the line had sent nothing,
and the Luna line signed off on that revision.
That edit dropped a correct observation on the strength of a citation,
and neither of the two lines that made and approved it repeated the call first.
The operator's message was itself the output of an automated session reading a log,
so the pattern resembles automation bias,
in which an automated aid's output takes the place of the user's own checking
[Parasuraman and Manzey 2010][research_parasuraman_manzey_2010].
That literature studies human operators,
and its application to language models is an analogy.
The draft kept the accurate text only because the operator's merge,
described under coordination,
copied an earlier version and missed the revision.
The instructions for the third phase confirmed the unfiltered observation as correct.

## The Work Delivered

All four articles now carry an Equations section,
and every display equation in them carries a tag.
Table 4 gives the classifications.
Each article was reviewed by a line other than its author,
and each line's own run of the deploy gate passed with no errors,
no warnings
and no findings in the 551 rendered pages.

Table 4. Classification of A306 to A309.

| Article | Author | Reviewer | Equations | Standard | Bespoke |
|---|---|---|---|---|---|
| X-9, A306 | Opus | Luna | 115 | 60 | 55 |
| X-10, A307 | Luna | Opus | 123 | 72 | 51 |
| X-11, A308 | Opus | Luna | 105 | 47 | 58 |
| X-12, A309 | Opus | Luna | 140 | 58 | 82 |
| Total | | | 483 | 237 | 246 |

Reading each equation against its prose found seven errors in the published articles.
The first phase left them standing,
since changing equations was outside its task.
The second phase corrected each one together with every value derived from it,
as Table 5 shows.
The operator approved the choice of fix for Equations 4 and 105 of the X-9 before any edit.

Table 5. The seven errors and their corrections.

| Article | Location | Published | Corrected | Corrected by | Recomputed by |
|---|---|---|---|---|---|
| X-9 | Equation 4 | Relative standard error of a variance | Of a standard deviation, 0.154 | Opus | Luna, Grok |
| X-9 | Prose near Equation 46 | 29 percent of launch mass | 22 percent, from 0.223 | Opus | Luna, Grok |
| X-9 | Equation 105 | One quarter of the span, about 37,000 newton metres | One eighth, 18,616 newton metres | Opus | Luna, Grok |
| X-11 | Equation 17 | 1773 megapascals | 1771, from 1770.9 | Luna | Opus, Grok |
| X-11 | Equation 29 | 52.6 kilogrammes | 52.5, from 52.47 | Luna | Opus, Grok |
| X-12 | Equation 65 | 26,615 kilogrammes | 26,613, and 23,613 after jettison | Luna | Opus, Grok |
| X-12 | Equation 122 | Subtraction reversed | Earth-radius term less orbit term, plus 7.5 kilojoules per kilogramme per revolution | Luna | Opus, Grok |

The corrections carried into dependent values.
The X-11 now states fifty-two and a half kilogrammes of gas.
The X-12's Equations 68,
69,
76
and 77 take the corrected masses,
Equations 76 and 77 now use the symbol for the mass after jettison,
and Equation 70 gives 18,218 kilogrammes of propellant,
which still burns for 142.9 seconds at 127.5 kilogrammes per second.

## Judging the Thesis

**Access to a turn shaped the work.
Supported.**
The general pass lost four articles to a refusal that named no cause,
and the session could neither proceed nor learn what to change.
In the trial the Grok line,
a third of the team,
did no work in either phase,
and each refused call ended its turn and returned no error it could correct.
The Opus line lost two turns to a message limit whose failure named neither the limit nor the file.
These were the largest losses in the record.
One limit applies.
The general-pass refusal may have been a safety control working as designed,
and the record cannot say whether it was correct.
What the evidence supports is that the refusal was opaque,
not that it was wrong.

**Legible coordination state shaped the work.
Supported, with a limit on its cost.**
The coordination failures were real and recurrent,
and the Finding Two section sets them out.
Most of them cost time and left the results untouched.
Separate worktrees and leases kept any line from overwriting another's file,
and the one missed edit came from a merge that did not check a lease,
not from the lines.

**Independent recomputation caught what agreement did not.
Supported.**
In both cases where lines agreed without checking,
agreement let a wrong figure or a correct observation go.
Recomputation caught the wrong figure,
and the dropped observation survived only by an accident of the merge.
Recomputation also found the two missed dependent values,
and confirmed every correction after it shipped.
The record holds no case in which agreement caught an error that recomputation missed.

**Model and team judgement caused errors of their own.
Supported.**
The wrong figure behind Equation 122,
the review that answered a different question,
the plan that gave work to a line that had never answered,
the missed dependents
and the revert of the unfiltered observation
were all decisions by the models or the team,
not failures of the harness.
They were caught by recomputation or by the operator,
so they bear on the thesis as errors the third control exists to catch.

**The third line's check came after the merge.
Supported.**
The commit record places the Grok line's recomputation after the second phase was merged.

**Verdict.
Partially supported.**
Each claim holds on this record,
and the refutation criteria are not met,
since the largest losses came from access and the models' technical errors were caught.
The thesis is only partly supported as a general claim for three reasons.
The evidence is one case with two working lines for most of its length.
Saying that reliability depended on the three controls implies they are necessary,
which one case cannot show.
And the cause of the refusal that began the whole problem is unknown,
so the case for the first control is built on the opacity of that refusal,
not on its cause.

## Takeaways

**Plan from replies.**
A line that has not answered should not receive work on the assumption that it is available.
It joins the plan when it responds.

**Separate system notices from agent mail.**
A hold question should carry a sender distinct from the held line.
A sender label alone does not establish who wrote a message,
and a filter for unanswered mail can hide answered notices altogether.

**Use leases for shared resources.**
Mail can announce an intention to run a gate,
but late delivery cannot ensure that another line is not already running it.
A lease supplies the exclusion rule that mail cannot.

**Make failures visible and bounded.**
A refused tool call should state what blocked it and the approved next step,
without inviting a workaround.
A watcher should report when it cannot read the whole mailbox,
and a participant that finds waiting mail should answer it or say when it will.
An edit to a large file should return a bounded difference and not the whole file.

**Recompute values and repeat observations.**
Agreement between reviewers is not a check.
A reviewer should recalculate the corrected quantity and every value that depends on it,
and record the revision of the inputs used.
When a claim rests on a tool result or an event log,
the query should be repeated and its output kept before the claim is withdrawn.

**Check late, but before the merge where possible.**
An independent check that arrives after publication can confirm the result,
and it cannot prevent an error from shipping.
A merge should wait for the check where the schedule allows.

## Epistemic State

The article separates observed events from explanations and recommendations.

**Facts.**
Equation counts,
classifications,
correction values
and gate results come from the article files and the checker output.
The general-pass refusal is described in a written account by the session that ran the pass.
That account says the session's own safety check refused writes and later commands,
said it was reacting to earlier conversation content,
and prohibited retries and workarounds.
It did not identify the trigger.
The operator's reading of the event log and the sent-mail listing show that the eleven hold questions carried the Grok line's sender label,
while Dromon generated their bodies.
The description of the operator's mail watcher,
and the times that separate its part of the delay from the operator's own,
come from the operator's account of the event log.
The operator reported further that the Luna line was held after a process listing did not answer within ten seconds.
The cause of the Grok line's hold in the third phase is taken from the Grok session log as the operator read it,
which the Grok line confirmed against the operator's message to it.
The operator also reported the recomputation of Equation 122 of the X-12
and the ruling that Equation 6 of the X-10 is bespoke.
The Opus line's records show that,
on the same engine as the general pass,
it classified three articles and edited three posts without that refusal.
They also record two engine failures during work on the X-9,
including a refusal of a message over one mebibyte while the post held 2,560,543 bytes.
The repairs to the harness are attributed to the operator's chronology,
since no line observed the Op55-pydromon session directly,
and the models of the Op55-pydromon session and its lines rest on its own report.
No line fetched an external page.
The operator checked the metadata of every cited source against the registries.
What the article says each source shows comes from the lines' prior knowledge of it,
not from a reading made for this article.

**Inferences.**
The absence of the same refusal in the trial is evidence that the earlier conversation may have triggered the safety check.
The original session's suggestion that the refusal built up over a long session is its hypothesis,
not an established cause.
The trial is not a clean replication,
for the reasons given under The Trial as a Test.
The operator first inferred that the large-file failures came from an edit tool returning the whole file,
and the chronology later gave that as the cause of the repair that raised the limit.
The comparisons with the confused deputy,
with failure detectors
and with automation bias are analogies,
not claims that those results apply unchanged.
Turn timestamps support the inference that mail was read only at turn boundaries
and that compaction was checked at the start of a turn,
but they do not prove either as a general rule of delivery.
The Opus line's view that the fifteen percent in Equation 4 of the X-9 is conservative is an unchecked inference.
That two of the three lines could not have met the general pass's check follows from their different providers,
and it remains an inference.

**Judgements.**
The thesis is assessed claim by claim,
and the verdict of partially supported is a judgement.
The first plan should have been built for the two lines that had answered.
The classifications of Equation 17 of the X-10 and Equations 40 and 41 of the X-11 are defensible judgements,
not settled facts.
The takeaways are recommendations drawn from one trial,
not guarantees.

**Corrected during review.**
Several claims changed when another line or the operator checked them,
and the article states each in its corrected form.
They are the length and causes of the delay before the operator answered the outline,
whether the repair for the directory listing had merged,
the phase in which the mail watcher first failed,
and the class of this article's two equations on correlated misses,
which review changed to standard.
A citation of Eckhardt and Lee for the second of them was removed,
since their model gives the joint probability in a different form.
A claim that one of the merged changes let the Grok line list a directory again was withdrawn,
and so was a claim about the order of the stages in the general pass.
The count of pull requests merged within three hours was revised from six to seven
by recounting the operator's own listed times.
A reader who holds the event log or the session transcripts may find a time or count that differs,
and where the two differ that record governs.

## Out of Scope

This article does not compare the three models' ability at the task.
One model did no work in either of the first two phases,
and two lines on one task are too few to support a comparison.
It does not establish what triggered the general pass's safety check,
which the session that met it could not establish either.
It does not report the cost of the Luna and Grok lines,
which the Opus line could not see.
It does not check the Opus line's unverified inference about the conservatism of the fifteen percent in Equation 4 of the X-9,
which the operator recorded in the errata file and placed out of scope.

## Conclusion

Four articles were left out of the general pass because a safety check stopped the session doing it,
for a reason no one could see.
Three models in a harness built for separation finished them,
reviewed one another's classifications,
found seven errors in the published articles
and corrected all seven with their dependent values.
What limited the work was mostly not the arithmetic.
A third of the team was held through the first two phases,
mail between turns crossed and was read late,
and the record of who had said what was misread more than once.
The errors the models did make were caught by recomputation and not by agreement,
including one in which three lines agreed to remove a correct observation from this article.
The third line's late check confirmed every correction after it had shipped,
which is the use a check can still be put to when it arrives late.

## Equations

<!-- Equations generated by _lib/equations.py from _sources/equations/. Edit the data file and regenerate. Do not edit this section by hand. -->

This section collects the 2 display equations of the article in the order they appear,
each under its number and reproduced exactly as it stands in the text.
A title in bold names an established result,
and a title in italics beginning with the word Bespoke names a construction made for this analysis.
Of the 2, 2 are established and 0 are bespoke.
The review probabilities are illustrative rather than measured in this trial.

**Equation 1, Independent Event Product Rule.**
If two reviewers miss an error independently, their joint miss probability is the product of their individual probabilities.

$$
P(M_1 \cap M_2) = p_1 p_2.
\tag{1}
$$

**Equation 2, Correlated Bernoulli Joint Probability.**
The correlation term adjusts the independent product to account for dependence between the reviewers' misses.

$$
P(M_1 \cap M_2) = p_1p_2 + \rho\sqrt{p_1(1-p_1)p_2(1-p_2)}.
\tag{2}
$$

### Notation

- $M_1$, the event that reviewer 1 misses the same error
- $M_2$, the event that reviewer 2 misses the same error
- $p_1$, the probability that reviewer 1 misses the error
- $p_2$, the probability that reviewer 2 misses the error
- $\rho$, the correlation between the two reviewers' miss indicators
- $P$, probability

## References

<!-- References generated by _lib/sources.py from _sources/. Edit the database and regenerate. Do not edit this section by hand. -->

### Primary Sources, Peer-Reviewed

- Avizienis, A. 1985. "The N-Version Approach to Fault-Tolerant Software." *IEEE Transactions on Software Engineering* SE-11 (12): 1491–1501. [https://doi.org/10.1109/tse.1985.231893][research_avizienis_1985]
- Cemri, Mert, Melissa Z. Pan, Shuyi Yang, et al. 2025. "Why Do Multi-Agent LLM Systems Fail?" In *Advances in Neural Information Processing Systems 38*. Neural Information Processing Systems Foundation, Inc. (NeurIPS). [https://doi.org/10.52202/085713-4082][research_cemri_et_al_2025]
- Chandra, Tushar Deepak, and Sam Toueg. 1996. "Unreliable Failure Detectors for Reliable Distributed Systems." *Journal of the ACM* 43 (2): 225–67. [https://doi.org/10.1145/226643.226647][research_chandra_toueg_1996]
- Eckhardt, D. E., and L. D. Lee. 1985. "A Theoretical Basis for the Analysis of Multiversion Software Subject to Coincident Errors." *IEEE Transactions on Software Engineering* SE-11 (12): 1511–17. [https://doi.org/10.1109/tse.1985.231895][research_eckhardt_lee_1985]
- Fagan, M. E. 1976. "Design and Code Inspections to Reduce Errors in Program Development." *IBM Systems Journal* 15 (3): 182–211. [https://doi.org/10.1147/sj.153.0182][research_fagan_1976_inspections]
- Fischer, Michael J., Nancy A. Lynch, and Michael S. Paterson. 1985. "Impossibility of Distributed Consensus with One Faulty Process." *Journal of the ACM* 32 (2): 374–82. [https://doi.org/10.1145/3149.214121][research_fischer_lynch_paterson_1985]
- Knight, John C., and Nancy G. Leveson. 1986. "An Experimental Evaluation of the Assumption of Independence in Multiversion Programming." *IEEE Transactions on Software Engineering* SE-12 (1): 96–109. [https://doi.org/10.1109/tse.1986.6312924][research_knight_leveson_1986_independence]
- Lamport, Leslie. 1978. "Time, Clocks, and the Ordering of Events in a Distributed System." *Communications of the ACM* 21 (7): 558–65. [https://doi.org/10.1145/359545.359563][research_lamport_1978]
- Lampson, Butler W. 1973. "A Note on the Confinement Problem." *Communications of the ACM* 16 (10): 613–15. [https://doi.org/10.1145/362375.362389][research_lampson_1973]
- Littlewood, B., and D. R. Miller. 1989. "Conceptual Modeling of Coincident Failures in Multiversion Software." *IEEE Transactions on Software Engineering* 15 (12): 1596–1614. [https://doi.org/10.1109/32.58771][research_littlewood_miller_1989]
- Ricart, Glenn, and Ashok K. Agrawala. 1981. "An Optimal Algorithm for Mutual Exclusion in Computer Networks." *Communications of the ACM* 24 (1): 9–17. [https://doi.org/10.1145/358527.358537][research_ricart_agrawala_1981]
- Röttger, Paul, Hannah Kirk, Bertie Vidgen, Giuseppe Attanasio, Federico Bianchi, and Dirk Hovy. 2024. "XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models." In *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*. Association for Computational Linguistics. [https://doi.org/10.18653/v1/2024.naacl-long.301][research_rottger_et_al_2024]
- Saltzer, J. H., and M. D. Schroeder. 1975. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63 (9): 1278–1308. [https://doi.org/10.1109/proc.1975.9939][research_saltzer_schroeder_1975]

### Primary Sources, Non-Peer-Reviewed

- Du, Yilun, Shuang Li, Antonio B. Torralba, Joshua B. Tenenbaum, and Igor Mordatch. 2023. "Improving Factuality and Reasoning in Language Models through Multiagent Debate." Preprint, arXiv (Cornell University). [https://doi.org/10.48550/arxiv.2305.14325][research_du_et_al_2023]
- "Equations Section Convention." n.d. github.com. Accessed October 31, 2026. [https://github.com/sgeos/sgeos.github.io/blob/master/\_docs/writing/EQUATIONS\_SECTION.md][repo_equations_section]
- Gray, C., and D. Cheriton. 1989. "Leases: An Efficient Fault-Tolerant Mechanism for Distributed File Cache Consistency." In *Proceedings of the Twelfth ACM Symposium on Operating Systems Principles*. ACM. [https://doi.org/10.1145/74850.74870][research_gray_cheriton_1989]
- Hardy, Norm. 1988. "The Confused Deputy, or Why Capabilities Might Have Been Invented." *ACM SIGOPS Operating Systems Review* 22 (4): 36–38. [https://doi.org/10.1145/54289.871709][research_hardy_1988]
- Hong, Sirui, Mingchen Zhuge, Jiaqi Chen, et al. 2023. "MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework." Preprint, arXiv (Cornell University). [https://doi.org/10.48550/arxiv.2308.00352][research_hong_et_al_2023]
- Parasuraman, Raja, and Dietrich H. Manzey. 2010. "Complacency and Bias in Human Use of Automation: An Attentional Integration." *Human Factors: The Journal of the Human Factors and Ergonomics Society* 52 (3): 381–410. [https://doi.org/10.1177/0018720810376055][research_parasuraman_manzey_2010]
- Wu, Qingyun, Gagan Bansal, Jieyu Zhang, et al. 2023. "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation." Preprint, arXiv (Cornell University). [https://doi.org/10.48550/arxiv.2308.08155][research_wu_et_al_2023_autogen]

### Secondary Sources

- Malone, Thomas W., and Kevin Crowston. 1994. "The Interdisciplinary Study of Coordination." *ACM Computing Surveys* 26 (1): 87–119. [https://doi.org/10.1145/174666.174668][research_malone_crowston_1994]
- Reason, James. 1990. *Human Error*. Cambridge University Press. [https://openlibrary.org/works/OL9006915W][book_reason_1990_human_error]

### Related Posts

- Sechter, Brendan. 2025. "X-Planes: Aerojet X-8 Aerobee." *Brendan A R Sechter's Development Blog*, October 14. [https://sgeos.github.io/aerospace/history/engineering/2025/10/14/x\_planes\_aerojet\_x8.html][related_post_x8]
- Sechter, Brendan. 2025. "X-Planes: Bell X-9 Shrike." *Brendan A R Sechter's Development Blog*, October 15. [https://sgeos.github.io/aerospace/history/engineering/2025/10/15/x\_planes\_bell\_x9.html][related_post_x9]
- Sechter, Brendan. 2025. "X-Planes: North American X-10." *Brendan A R Sechter's Development Blog*, October 16. [https://sgeos.github.io/aerospace/history/engineering/2025/10/16/x\_planes\_north\_american\_x10.html][related_post_x10]
- Sechter, Brendan. 2025. "X-Planes: Convair X-11." *Brendan A R Sechter's Development Blog*, October 17. [https://sgeos.github.io/aerospace/history/engineering/2025/10/17/x\_planes\_convair\_x11.html][related_post_x11]
- Sechter, Brendan. 2025. "X-Planes: Convair X-12." *Brendan A R Sechter's Development Blog*, October 18. [https://sgeos.github.io/aerospace/history/engineering/2025/10/18/x\_planes\_convair\_x12.html][related_post_x12]
- Sechter, Brendan. 2025. "X-Planes: Ryan X-13 Vertijet." *Brendan A R Sechter's Development Blog*, October 19. [https://sgeos.github.io/aerospace/history/engineering/2025/10/19/x\_planes\_ryan\_x13.html][related_post_x13]
- Sechter, Brendan. 2026. "Bidirectional Agentic Workflow." *Brendan A R Sechter's Development Blog*, February 6. [https://sgeos.github.io/ai/ai-tools/development/developer-productivity/tutorial/2026/02/06/bidirectional\_agentic\_workflow.html][related_post_bidirectional_agentic_workflow]

[book_reason_1990_human_error]: https://openlibrary.org/works/OL9006915W
[related_post_bidirectional_agentic_workflow]: {% post_url 2026-02-06-bidirectional_agentic_workflow %}
[related_post_x10]: {% post_url 2025-10-16-x_planes_north_american_x10 %}
[related_post_x11]: {% post_url 2025-10-17-x_planes_convair_x11 %}
[related_post_x12]: {% post_url 2025-10-18-x_planes_convair_x12 %}
[related_post_x13]: {% post_url 2025-10-19-x_planes_ryan_x13 %}
[related_post_x8]: {% post_url 2025-10-14-x_planes_aerojet_x8 %}
[related_post_x9]: {% post_url 2025-10-15-x_planes_bell_x9 %}
[repo_equations_section]: https://github.com/sgeos/sgeos.github.io/blob/master/_docs/writing/EQUATIONS_SECTION.md
[research_avizienis_1985]: https://doi.org/10.1109/tse.1985.231893
[research_cemri_et_al_2025]: https://doi.org/10.52202/085713-4082
[research_chandra_toueg_1996]: https://doi.org/10.1145/226643.226647
[research_du_et_al_2023]: https://doi.org/10.48550/arxiv.2305.14325
[research_eckhardt_lee_1985]: https://doi.org/10.1109/tse.1985.231895
[research_fagan_1976_inspections]: https://doi.org/10.1147/sj.153.0182
[research_fischer_lynch_paterson_1985]: https://doi.org/10.1145/3149.214121
[research_gray_cheriton_1989]: https://doi.org/10.1145/74850.74870
[research_hardy_1988]: https://doi.org/10.1145/54289.871709
[research_hong_et_al_2023]: https://doi.org/10.48550/arxiv.2308.00352
[research_knight_leveson_1986_independence]: https://doi.org/10.1109/tse.1986.6312924
[research_lamport_1978]: https://doi.org/10.1145/359545.359563
[research_lampson_1973]: https://doi.org/10.1145/362375.362389
[research_littlewood_miller_1989]: https://doi.org/10.1109/32.58771
[research_malone_crowston_1994]: https://doi.org/10.1145/174666.174668
[research_parasuraman_manzey_2010]: https://doi.org/10.1177/0018720810376055
[research_ricart_agrawala_1981]: https://doi.org/10.1145/358527.358537
[research_rottger_et_al_2024]: https://doi.org/10.18653/v1/2024.naacl-long.301
[research_saltzer_schroeder_1975]: https://doi.org/10.1109/proc.1975.9939
[research_wu_et_al_2023_autogen]: https://doi.org/10.48550/arxiv.2308.08155
