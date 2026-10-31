# A385 notes from Luna

## Facts

The operator approved the plan with Grok removed from active work because Dromon held the line before the model ran. The operator said Grok's engine wrote empty hooks-paths and installed-plugins entries into its Dromon home on each start. A removal loop was refused, which the operator judged correct.

The operator reassigned A308 to Opus and assigned Luna to cross-review A308 and A309. The operator also said that if Grok resumed, it could review and write its own experience report and A385 notes.

The kickoff instructions pointed to ARTICLE_ERRATA.md for two unchecked A306 claims, but the file in both my worktree and the main checkout had no A306 entry. The operator corrected the source path to the gitignored tmp/eq2/FINDINGS.md and said not to change either equation.

I read Opus's A306 classification and returned tag-specific feedback by mail. I generated the A307 skeleton with the exact X-10 post path, classified and validated all 123 equations in tmp, and sent Opus a message pointing to the file. He later reported that the message had not reached him by his review, although sent tracking now lists it as delivered. He reviewed the file directly from my worktree and agreed with all classifications except tag 80.

My first skeleton invocation passed A307 instead of a post path and failed. The command help showed a generic POST placeholder. I then found the post by article marker and reran the command with its filename.

I reviewed Opus's A309 classification with the X-12 article path. The validator passed all 140 equations. I confirmed two body issues Opus had found, the arithmetic in tag 65 and the sign in tag 122. I did not alter the body.

I suggested that A309's notation key define $c$ and $d$ in its round-trip propagation delay equation. Opus argued that the adjacent prose and conventional notation make them clear, and I agreed. This differs from A305 and A310, where the same letters have less conventional or overloaded meanings.

I cross-reviewed Opus's A308 classification from his worktree. The validator reported all 105 equations consistent. I first recommended tags 40 and 41 as bespoke because the article assembles standard stress relations into its pressure-stabilised bending threshold. Opus noted that this differs from A307's general crossover time in tag 17, and argued that both are standard because they express generic relations without article-chosen inputs. I agreed and withdrew my recommendation. His claim that the A308 onset moment is established in the inflatable-beam literature remains an unverified recollection. In the same review I independently recalculated A308 tag 17 as 1,770.9436517 megapascals, rounding to 1,771, and tag 29 as 52.46879357 kilogrammes, rounding to 52.5. I reported both differences without changing the body.

Opus argued for a consistent classification across A307 Equation 17 and A308 Equations 40 and 41. We agreed to classify all three as standard because they state generic crossover or onset relations without article-chosen inputs. He identified A307 Equation 80 as a textbook short-period approximation, and I reclassified it as standard. His recollection that the A308 onset moment is established in the inflatable-beam literature has not been independently checked, so I will not present that attribution as verified.

I initially accepted Opus's view that A307 Equations 4 and 6 were standard because the inputs were sourced. After rereading the classification brief, I changed Equation 4 to bespoke because it assigns the whole weapon circular error probable to gyroscope drift. Equation 5 is the unit conversion of that assumption-based value, so I also changed it to bespoke. Equation 6 assigns the whole reported position error growth to gyroscope drift. The sources report the value but do not state that all growth came from that component, so I kept it bespoke. Opus now agrees that Equation 4 is bespoke but considers Equation 6 standard because the numerical input is reported. This disagreement is unresolved and must go to the operator. Equation 17 remains standard because it states a generic crossover relation without an article-chosen value.

The same 10,000 kilometre range receives different classifications across the articles. A307 uses it as the Navaho's sourced design range, while A308 and A309 use it as a representative Atlas range. That supports standard classifications for direct evaluations of established relations in A307 and bespoke classifications for representative Atlas evaluations in A308 and A309. The sourced range does not make A307 Equations 4 and 5 standard, because their error-budget allocation is an assumption. Equation 6 does not use that range directly, and its classification instead turns on whether the reported total navigator error growth can be assigned to gyroscope drift.

After Opus reviewed A307, I changed tag 80 to standard, then reclassified tags 4 and 5 as bespoke and applied the article. I left tag 6 bespoke despite Opus's disagreement. `equations.py check` reports all 123 equations consistent, with 72 standard and 51 bespoke. The final `./_check.sh` passed with 384 posts checked, zero errors and warnings, 178/178 and 94/94 library tests, 14 Ruby tests, production build successful and rendered audit of 551 pages with no findings. No sandbox denial or write refusal has occurred in my worktree. I have no evidence of permanently lost mail. Opus reported that two review messages from me had not reached his inbox by the time of his A307 review, although sent tracking later listed them as delivered. The timing is unavailable.

The mail tool refused one outgoing message because I supplied my own outgoing message identifier as `reply_to`. I retried without that field, and the message was delivered.

The process-list tool returned no list and stated that the daemon cannot identify or stop another process because it cannot read that process's environment. I could not independently inspect Opus's gate process. Opus's draft reports that an announced gate message was waiting and undelivered while the two lines' runs overlapped. I did not receive that announcement; I cannot independently confirm the overlap timing from my side.

The A385 draft's first account of the Eq 4 and 6 review was written before I read Opus's later clarification, message m-80ec3c937468. That message arrived unread in a later turn. I opened it and replied in m-cb8f30558427. It confirms Opus now considers Eq 4 bespoke and Eq 6 standard. I agree on Eq 4 but retain bespoke for Eq 6 and have asked the operator to settle that remaining disagreement. The claim that I never opened the clarification is no longer accurate.

## Inferences

The team could preserve independent authorship and cross-review by keeping each line's edits in its own worktree and exchanging paths and tag-specific comments by mail.

The stale path in the kickoff and Grok's hold were the two coordination defects that required operator intervention. The operator corrected the source path and reallocated the work without allowing one line to bypass the hold.

## Judgements

The hold was a substantive failure of the three-line plan, even though the two active lines could continue after reassignment. The article should describe this as a team failure and include the refused workaround, rather than imply that Grok completed work.

The command placeholder should be replaced with an example post filename because I initially read A307 as the argument to skeleton. This was a documentation ambiguity and my command error, not a tool malfunction.

I changed A307 Equations 4 and 6 after rereading the classification brief, even though Opus's review treated them as standard. I judge the source values insufficient to support the unstated assumption that the entire reported error comes from gyroscope drift.

I have not observed a technical capability available to Opus that is unavailable to Luna. Differences so far are assignment and access rules, not model capability.
