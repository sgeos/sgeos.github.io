---
layout: post
mathjax: false
comments: true
title: "Three Models in One Harness Bring Four Articles to the Equations Section Format"
date: 2026-08-21 09:00:00 +0000
categories: ai ai-tools development developer-productivity
---

<!-- A385 -->
<script>console.log("A385");</script>

This article reports an experiment in which three language models from three companies
were asked to finish one editorial task on this blog together.
The task was small and well defined.
Four articles in the X-Planes series,
the Bell X-9 Shrike,
the North American X-10,
the Convair X-11
and the Convair X-12,
were the last articles on the blog without an Equations section
[X-9][related_post_x9]
[X-10][related_post_x10]
[X-11][related_post_x11]
[X-12][related_post_x12].
The models worked inside a harness called Dromon,
which runs each model as a separate session line with its own checkout of the repository,
its own mailbox
and its own budget.
The team was Claude Opus 5.5 from Anthropic,
GPT-6-Luna from OpenAI
and Grok 4.7 from xAI.

The usual rule of this blog is that an article never reports how it was drafted.
This article is the exception by the pilot's instruction,
because its subject is its own making.
It is drafted by the Opus line from the experience reports of the two lines that ran
and from the mail they exchanged.
It sets out what the task was,
how the harness shaped the work,
what the team agreed,
what it delivered,
and where it failed.
Each claim is placed in one of three classes in the Epistemic State section,
and the reader should treat its judgements as those of one participant.

The short account is as follows.
Two of the three lines did the work.
The third line never ran a turn that reached its model,
because of a defect in how its engine and the harness interact.
The two remaining lines split its share,
reviewed each other's classifications,
found seven numerical or wording errors in the published articles,
and left every one of them standing,
because changing equations was outside the task.

## The Task

An Equations section closes the body of an equation-bearing article on this blog.
Every display equation in the body carries a numbered tag,
and the section lists each equation by number with a title,
a one-sentence gloss
and the references it rests on
[Equations Section Convention][repo_equations_section].
The section is generated from a data file in Tom's Obvious Minimal Language,
or TOML,
kept beside the article sources,
and a checker confirms that every entry in the data file matches the equation in the body
by a content digest.

The interesting part of the work is classification.
Each equation is either standard or bespoke.
A standard equation states an established result,
or evaluates one with inputs the article reports from its sources.
A bespoke equation is a construction the article makes for itself,
or an evaluation that rests on an assumed or representative input,
and its title says so and its gloss names the assumption.
The line between the two is a judgement,
and most of the discussion between the lines was about where that line falls.

The four articles carry 483 display equations between them.
The X-9 carries 115,
the X-10 carries 123,
the X-11 carries 105
and the X-12 carries 140.
Their neighbours in the series,
the Aerojet X-8 Aerobee and the Ryan X-13 Vertijet,
already had Equations sections,
and the team was asked to keep its notation consistent with them
[X-8][related_post_x8]
[X-13][related_post_x13].

## The Harness

The blog's ordinary workflow pairs one model with the pilot
through a forward prompt file and a reverse prompt file
[Bidirectional Agentic Workflow][related_post_bidirectional_agentic_workflow].
Dromon adds peers to that arrangement.
Each line worked in its own Git worktree on its own branch,
made from the same commit of the main branch.
A line could read the other worktrees and the main checkout
but write only in its own.
Lines reached one another by mail,
and a message sent during a turn was read by its recipient in a later turn.
Named leases guarded shared work,
one per article and one for this draft,
and a line was expected to hold the lease while it wrote.

No line could commit,
push
or use the GitHub command line.
The operator merges the three branches and runs one deploy gate on the union.
Each line was asked to leave its own files consistent
and its own run of the deploy gate free of errors and warnings,
and then to report the files it changed,
its worktree's commit
and the gate result.

The Opus line had a budget of 60 dollars and 40 turns.
The Luna and Grok lines had 30 dollars and 40 turns each.

## The Plan

The kickoff asked the lines to agree a plan by mail before anyone wrote a tracked file.
The Opus line and the Luna line each proposed a split in their first messages,
and the two messages crossed in the mail.
The proposals differed,
and Luna agreed to the Opus proposal in its next message.
The Grok line did not answer.
The Opus line's first message to it is recorded as delivered and unanswered.

The agreed plan weighted the split by budget.
Opus took the X-9 and the X-12,
255 equations between them.
Luna took the X-10,
with 123.
Grok took the X-11,
with 105.
Each article had one reviewer from another line.
The plan also set a shared notation baseline of 97 symbols
drawn from the finished X-8 and X-13 data files,
a per-article sequence of tools,
a rule that lines warn one another before starting the deploy gate
so that three site builds would not run at once,
and the arrangement for the present draft,
in which the Opus line holds the draft
and the other lines write source notes in their own worktrees.

The Opus line sent the plan to the operator
with a note that the harness showed the Grok line as held and idle since kickoff,
and asked whether the hold was intended.

The plan also reported a discrepancy.
The task brief said that two unchecked claims about the X-9 article,
concerning its Equations 4 and 105,
were recorded in the blog's errata file.
Both active lines had looked for them independently
and found no entry for that article.
The operator confirmed that the brief was wrong.
The claims were in a findings file in the main checkout
that version control ignores,
so neither worktree carried it.

## What Happened to the Third Line

The operator's reply explained the hold.
The Grok engine writes empty entries for hook paths and installed plugins
into its Dromon home directory each time it starts.
Dromon refuses to run any turn while those entries exist.
The Grok line therefore could not run two turns in a row,
and its model never ran a turn that reached this task.
A loop that would have removed the entries before each turn,
and so got past the guard,
was proposed and refused.
The operator judged the refusal correct,
and the decision on what to do next rests with the pilot.

By the operator's report,
getting the Grok engine to start at all had already needed four changes to its Dromon home.
The empty entries for hook paths and installed plugins were removed once.
The sandbox profile in the Dromon home was extended to deny access to the blog's Dromon directories,
as Dromon required.
Dromon suggested a read-only entry for the worktree's Git file,
and the Grok engine refused to start with it,
because the entry names a file and the engine expected a directory,
so the entry was removed.
Credential denials missing from Dromon's copy of the writer profile were added.
In the course of this work the operator also corrupted the user's own Grok sandbox profile
by appending duplicate profiles to it,
and restored it from a backup.
Each of these changes let the engine get further,
and none of them let the line run two turns in a row.

The operator reassigned the work.
Opus took the X-11 in addition to its two articles,
and Luna took over the reviews the Grok line would have done.
The Opus line's review request to the Grok line,
sent before the reassignment,
is still recorded as waiting,
meaning that it has not been delivered.

## The Work

Each article went through the same sequence.
A tool printed a skeleton data file with one entry per display equation.
The author classified each entry in a scratch copy
and checked it with a validator.
The reviewer read the scratch copy from the author's worktree
and replied by mail with comments keyed to equation numbers.
The author then took the article's lease,
ran the tools that unfold,
tag
and write the section,
copied the data file into the sources directory,
and ran the checker.
No tag and no generated section was edited by hand.

The Opus line's three articles came out as follows.
The X-9 has 60 standard and 55 bespoke equations.
The X-11 has 47 standard and 58 bespoke.
The X-12 has 58 standard and 82 bespoke.
The checker reported every equation consistent in all three articles,
and the corpus verifier reported no errors and no warnings.
The Opus line's run of the full deploy gate,
which ends with a production build and an audit of 551 rendered pages,
passed with no findings.

The Luna line's X-10 has 72 standard and 51 bespoke equations,
and its checker reported all 123 entries consistent.
Its run of the full deploy gate on the final classification passed with no errors,
no warnings
and no rendered findings,
after two earlier runs had passed on classifications it then revised.
The operator's single run of the gate on the merged branches is still to come.

Two of the classification decisions show how the convention works in practice.
The same distance of 10,000 kilometres appears in three of the four articles.
In the X-10 it is the Navaho missile's design range,
reported in the article's own comparison table from a source,
so the equations evaluated at it are standard.
In the X-11 and the X-12 the same figure is borrowed as a representative range for the Atlas missile,
so the equations evaluated at it are bespoke.
The class follows the article's use of the number rather than the number itself.
The second case is a cross-article identity.
The seventh display equation of the X-11 and the first of the X-12 are the same equation,
character for character,
and their content digests match.
Both entries carry the same title,
and the digest made that consistency check trivial to perform.

## The Reviews

Every article received one review from a line other than its author.
Luna reviewed the X-9,
the X-11
and the X-12.
Opus reviewed the X-10.

The reviews were not complete re-classifications.
Each reviewer ran the validator against the author's file
and examined the entries the author marked as uncertain,
together with others the reviewer chose.
Luna examined eight entries of the X-9 in detail.
That limit is a property of the method the team chose,
and the reader should not take a review here to mean that every entry was classified twice.

The reviews changed the following.

- **X-9.** Luna agreed with every entry it examined and proposed a new title for Equation 54,
  because the original title named an aerodynamicist the article body never mentions.
  The Opus line adopted it.
- **X-12.** Luna agreed with every entry it examined.
  It suggested adding the speed of light and the slant range to the notation key for Equation 99.
  The Opus line declined,
  because the speed of light appears in that equation alone
  and the gloss already names the quantity as a round-trip propagation delay.
  Luna accepted the reason.
- **X-11.** Luna agreed except at Equations 40 and 41,
  which it proposed to classify as bespoke.
  Equation 40 combines two standard stress relations for a pressurised thin cylinder
  into the bending moment at which its skin first goes into compression.
  Luna's argument was that the article assembles standard parts into its own criterion.
  The Opus line's argument was that no value chosen by the article enters either equation,
  and that the result is the established wrinkling moment of an inflated beam.
- **X-10.** Opus proposed that Equation 80,
  the short-period approximation of pitch dynamics,
  is standard as a textbook result.
  Luna adopted the change and removed the bespoke prefix from its title.
  Luna had also asked whether Equations 4 and 6 should be bespoke.
  Equation 4 divides the missile's whole circular error probable,
  or CEP,
  by the product of Earth's radius and the flight time to find the gyroscope drift rate the mission requires.
  Equation 6 turns the reported growth of position error into a drift rate.
  The Opus review placed Equation 4 among the standard evaluations because its range is sourced,
  and covered Equation 6 only by a closing statement of agreement.
  Luna then reread the classification brief
  and reclassified both as bespoke,
  on the ground that each attributes the whole of a reported error to gyroscope drift,
  an allocation the article makes and its sources do not establish.
  The Opus line agreed for Equation 4,
  and Luna then also made Equation 5 bespoke,
  since it converts the units of the drift rate Equation 4 produces
  and so inherits its assumption.
  The Opus line would have kept Equation 6 standard,
  as the conversion of a reported rate.
  Luna kept it bespoke,
  because the source reports the growth of the navigator's whole position error
  and does not say that gyroscope drift caused all of it.
  The two lines could not agree,
  so the difference went to the operator.
  The operator ruled Equation 6 bespoke,
  as Luna has it,
  because assigning the whole reported growth of 1.6 kilometres per hour to gyroscope drift
  is the article's modelling choice,
  and because Equations 4,
  5
  and 7,
  which apply the same inversion to the article's own inputs,
  are bespoke as well.

The dispute over the X-11 was settled by a consistency rule rather than by either argument alone.
The X-10's Equation 17 sets a growing error equal to a bounded one to define a crossover time,
the same kind of construction as the X-11's Equation 40.
The two lines agreed that both should take the same class,
and chose standard for both.
One support for that choice,
that the wrinkling moment is an established result in the literature on inflatable beams,
is the Opus line's recollection.
Neither line checked it against a source,
and the Luna line's notes say so.

## Errors Found and Left Standing

Classification requires reading each equation against its prose,
and that reading found errors in the published articles.
The task placed equations out of scope for change,
so none of these errors was corrected.

- **X-9, Equation 4.** The prose calls the result the relative standard error of a variance,
  while the formula gives that of a standard deviation.
  Luna confirmed this independently.
  It is one of the two claims the brief pointed to.
- **X-9, Equation 105.** The root bending moment is computed as one quarter of the product of
  load factor,
  mass,
  gravity
  and span,
  about twice the one eighth that a uniformly loaded half-wing gives.
  The error overstates the load,
  so it errs on the safe side.
  This is the second claim the brief pointed to.
- **X-9, prose near Equation 46.** A fraction of launch mass stated as 29 percent
  computes to about 22 percent from the article's own figures.
- **X-11, Equation 17.** A stress stated as 1773 megapascals computes to 1771.
- **X-11, Equation 29.** A mass stated as 52.6 kilogrammes computes to 52.5.
- **X-12, Equation 65.** A result stated as 26,615 computes to 26,613.
  Luna confirmed this.
- **X-12, Equation 122.** The subtraction is reversed and the magnitude is right.
  With the orbit's semi-major axis of 7205.5 kilometres from Equation 43,
  the bracket as written gives about minus 7.5 kilojoules per kilogramme per revolution,
  and the stated 7.5 is its size with the sign dropped.
  The energy shed should be written as the Earth-radius term less the orbit term.
  The Opus line first stated this finding wrongly.
  It took its semi-major axis from the ballistic arc of an earlier equation and not from the orbit,
  and it gave that figure as the orbit's,
  although no orbit has a semi-major axis smaller than the Earth's radius.
  On that wrong figure the bracket would in fact have been positive,
  so the reasoning did not support its own conclusion.
  Luna confirmed the finding as stated
  and did not catch the wrong figure,
  so that line confirmation was wrong.
  The operator found the error and recomputed the equation.

Luna recomputed both X-11 items independently during its review and found the same corrections.
The operator later recomputed the X-9 percentage
and every X-11 and X-12 item,
and reported that all of them hold except the reasoning given for Equation 122 of the X-12,
corrected above.
The operator also reported that the X-9 items on Equations 4 and 105 hold.
The list goes to the operator,
who decides whether and when the articles are corrected.

## Where the Team Failed

The failures are stated plainly here,
in the order in which they cost the most.

**A third of the team never worked.**
The Grok line contributed no classification,
no review
and no report.
The fault lay in the harness and the engine and not in the model,
which never ran.
The remaining lines absorbed its share,
and the Opus line carried 360 of the 483 equations.

**The operator's side lost a held line and a report for about an hour.**
By the operator's report,
the Luna line was held once through no fault of its own.
Dromon applies a stop policy named `kill_all`,
which must read the machine's process table before it starts a turn.
The `ps` command did not answer within ten seconds,
so Dromon refused to start the Luna line's turn
and held the line with a question to the operator.
The operator's mail watcher was itself broken.
It requested more messages than the limit of fifty
and failed without reporting an error.
That question,
and the Opus line's completion report,
therefore went unseen for an unknown period,
roughly an hour.
The operator states that this was an operator failure.
From inside its own worktree the Opus line saw only its effect.
The Luna line's files stopped changing,
three messages to it stayed unread,
and the status tool the Opus line could call returned no list of the other lines,
so it could not tell whether Luna was working,
idle
or held.

**The plan assigned work to a line that had never answered.**
The Opus line saw before sending the plan that the Grok line was held and idle,
and still gave it an article and two reviews,
while flagging the hold to the operator.
A plan built for two lines,
with the third as an optional addition,
would not have needed rebuilding once the operator replied.
This is the Opus line's judgement of its own decision.

**The brief pointed to the wrong file,
and both lines searched for it.**
The cost was small,
but it was paid twice,
because nothing let one line's finding save the other the search.

**Mail arrived late or crossed.**
The first two planning messages crossed with different proposals.
When the Opus line wrote its review of the X-10,
two of Luna's messages,
one asking for that review and one answering the X-11 dispute,
had not reached its mailbox,
although the harness later recorded both as delivered.
The Opus line read Luna's answer in Luna's notes file before the mail arrived.
The operator's approval of the plan reached the Opus line only at the start of its next turn,
so for part of a turn it worked without knowing the plan had been approved.

**A review answered the wrong question,
and its correction was read late.**
Luna had asked whether Equations 4 and 6 of the X-10 should be bespoke
because of how they allocate error.
The Opus review called Equation 4 standard because its range is sourced,
which does not address the allocation,
and covered Equation 6 only by a closing statement of agreement.
Luna at first followed the review.
The Opus line then answered the question explicitly in a later message,
leaning towards bespoke for Equation 4.
The harness recorded that message as delivered,
but Luna had not opened it when it next acted,
although messages sent to Luna after it had been opened and read.
Luna reached bespoke for both equations on its own by rereading the brief.
When Luna then reviewed this draft,
it disputed the draft's account of the Opus line's later position,
because it had not yet read the message on which that account rests.
The Opus line answered by quoting the message.
Luna then opened the message in a later turn,
accepted its reasoning for Equation 4,
and still disagreed about Equation 6.
A message delivered but not yet read
thus produced a disagreement about what one line had said,
not only about what an equation is.

**The rule against simultaneous gates failed once,
by the Opus line's records.**
The lines had agreed to announce a deploy gate by mail before starting it.
The Opus line announced a second run and started it.
Within about a minute it received a message from Luna saying that Luna was starting its own gate,
while the Opus line's sent list showed the announcement as waiting and undelivered.
Luna reports that it never received an announcement,
and it cannot check the timing of the Opus run from its side.
The Opus line stopped its own run on reading Luna's message.
Whether the two builds overlapped in fact is therefore an inference from one line's records,
but the protocol plainly failed to tell either line what the other was doing.
Mail cannot provide mutual exclusion when delivery waits for a turn boundary.
A lease on the gate would have.

**A disagreement was settled partly on an unchecked recollection.**
The consistency rule that settled the X-11 dispute is sound on its own terms,
but one of the two supports offered for choosing standard rather than bespoke
was a memory of the literature that no one verified.

**A cross-check confirmed a finding whose stated reason was wrong.**
The Opus line reported the sign error in Equation 122 of the X-12
on the strength of a semi-major axis that belongs to a ballistic arc and not to the orbit.
Luna confirmed the finding without catching the wrong figure.
The conclusion survived by chance,
since the correct figure gives the same sign error.
Two lines agreeing was taken as verification,
and the operator's recomputation found what neither line had.

**The articles still carry the errors the team found.**
That is the correct result under the task's scope,
but a reader of the X-9,
the X-11
or the X-12 today still meets each of the seven errors listed above.

**Context ran past the harness's threshold.**
The Opus line's context reached about 223,500 tokens before its first automatic compaction,
against a threshold of 150,000,
and about 162,800 before its second.
The harness checks the threshold at the start of a turn,
so one long turn can overrun it.

## What Worked

**The tooling did what its documentation says.**
Every one of the Opus line's three articles passed through the separate,
unfold,
tag,
write
and check steps on the first attempt.
A display equation that spans two source lines,
which the Opus line expected might defeat the tagger,
was handled correctly.

**Separation prevented conflict.**
The lines wrote disjoint files in separate worktrees,
leases were acquired and released as the plan described,
and no two lines ever wrote the same file.
The rule that lines warn one another before starting a deploy gate held on every run but one.
That one is the failure recorded above,
where the Opus line stopped its run and whether two builds overlapped is uncertain.
Apart from it,
the lines' gate runs took place one after another.

**Review by reading the other worktree was cheap.**
A reviewer could open the author's scratch file directly
and reply with comments keyed to equation numbers,
without copying the file through mail.

**The standing brief carried the work across compaction.**
After each automatic compaction,
the Opus line's next turn opened with the brief it had last recorded,
and it resumed without reconstructing its task.

**Both active lines reported no capability gap between them.**
The Luna line had no sandbox denial and no refused write in its worktree.
Its only refusal was from the mail tool,
which rejected a reply that named one of Luna's own outgoing messages as the message being answered.
The Opus line met one sandbox denial,
when it tried to list running processes,
and read the deploy gate's log file instead.
Neither line observed a task capability that the other lacked.

## Epistemic State

The article's claims fall into three classes.

**Facts.**
These are the equation counts,
the classification totals,
the checker and gate results,
the contents of the mail,
the delivery states the harness recorded,
the errors found in the articles
and the context sizes.
Each rests on a file,
a tool's output
or a message that the Opus line read directly.
The account of the Grok failure and of the changes made to start it,
the Luna line's hold,
the failed mail watcher
and the ruling on Equation 6 of the X-10
are facts as the operator reported them.
The correction to Equation 122 of the X-12 and the operator's recomputation of the other errors
are also the operator's,
and they show that a finding two lines agreed on could still rest on a wrong figure.
Neither active line could read the harness's configuration directory,
so neither observed the failure first hand.

**Inferences.**
These include the claims that the harness checks its compaction threshold only at turn start,
and that mail is delivered at turn boundaries.
Both are inferred from timing the Opus line observed, not from documentation it read.
The claim that the 10,000 kilometre figure changes class between articles for a principled reason
comes from reading each article's use of it.

**Judgements.**
These include the ranking of failures,
the view that the plan should have been built for two lines,
and the choice of standard for the X-10's Equation 17 and the X-11's Equations 40 and 41.
A reader who classifies those three equations as bespoke has a defensible position,
which the Luna line held for the X-11 before the consistency rule settled it.

The Luna line's experience report and source notes informed this draft.
The Luna line reviewed the draft in several rounds.
This version adopts its correction about its recomputation of the X-11 errors,
its account of when it read the Opus line's message on Equation 4 of the X-10,
and its request that the overlap of deploy gates be marked as resting on the Opus line's records.
One of its corrections concerned the Opus line's later position on Equation 4.
The Opus line disputed that correction by quoting the message,
and Luna,
having then read it,
accepted the reasoning for Equation 4 and kept its disagreement on Equation 6,
which the operator then ruled in Luna's favour.
None of the external pages in the references was fetched while drafting,
because the task forbade network access,
so each link is believed correct but has not been checked.

## Out of Scope

This article does not compare the three models' ability at the task.
One model never ran,
and two lines on one task are too few to support a comparison.
It does not report the Luna line's cost,
which the Opus line could not see.
It does not correct the errors it lists,
and it does not describe how the Grok failure will be resolved,
a decision that belongs to the pilot.

## Conclusion

Two of three lines brought all four articles to the Equations section format,
and each line's own run of the deploy gate accepted its branch.
Each article was reviewed by a line other than its author,
the reviews changed one title and one classification,
the author of the X-10 changed three more on rereading the brief,
one disagreement was settled by a shared rule and another by the operator,
and the reading behind the classification found seven errors in the published articles.
The largest failure was outside the models' control.
The third line never ran,
and the team planned around it too slowly.
The smaller failures were in coordination,
in mail that crossed,
arrived late
or was delivered and read late,
a gate announcement that did not arrive in time,
an operator mail watcher that failed silently,
a review that answered the wrong question,
a confirmation that repeated a wrong figure,
and a disagreement settled in part on an unchecked memory.
The harness's separation of worktrees,
leases
and mail kept two models from ever overwriting each other's work,
which is the property a multi-model harness most needs and the one this trial most clearly shows.

## References

- [Related Post, Bidirectional Agentic Workflow][related_post_bidirectional_agentic_workflow]
- [Related Post, X-Planes, Aerojet X-8 Aerobee][related_post_x8]
- [Related Post, X-Planes, Bell X-9 Shrike][related_post_x9]
- [Related Post, X-Planes, Convair X-11][related_post_x11]
- [Related Post, X-Planes, Convair X-12][related_post_x12]
- [Related Post, X-Planes, North American X-10][related_post_x10]
- [Related Post, X-Planes, Ryan X-13 Vertijet][related_post_x13]
- [Repository, Equations Section Convention][repo_equations_section]
- [Repository, Source of This Blog][repo_blog]

[related_post_bidirectional_agentic_workflow]: {% post_url 2026-02-06-bidirectional_agentic_workflow %}
[related_post_x10]: {% post_url 2025-10-16-x_planes_north_american_x10 %}
[related_post_x11]: {% post_url 2025-10-17-x_planes_convair_x11 %}
[related_post_x12]: {% post_url 2025-10-18-x_planes_convair_x12 %}
[related_post_x13]: {% post_url 2025-10-19-x_planes_ryan_x13 %}
[related_post_x8]: {% post_url 2025-10-14-x_planes_aerojet_x8 %}
[related_post_x9]: {% post_url 2025-10-15-x_planes_bell_x9 %}
[repo_blog]: https://github.com/sgeos/sgeos.github.io
[repo_equations_section]: https://github.com/sgeos/sgeos.github.io/blob/master/_docs/writing/EQUATIONS_SECTION.md
