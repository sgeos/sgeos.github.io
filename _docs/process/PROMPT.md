# Prompt Staging Area

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is a staging area for complex human-to-AI instructions. The human pilot drafts and refines prompts here before execution.

---

# Current Prompt

## Comments

Read, but unverified:

- Android Development on FreeBSD
- Android Unit Testing
- Authenticating a Phoenix JSON API with Guardian and Ueberauth
- Claude Code on FreeBSD
- Claude Code on OpenBSD
- Claude Code Over SSH
- Getting Started with Solana Using Rust and Pinocchio
- Solana sBPF Assembly Example

Evidently, the 

### Publication of A87

Evidently, the `date` command output was the following.

```sh
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-18 15:58:18 +0000
```

I want to have software versions date and the header date synced.
I manually made this change.

## Objectives

### Document Date Sync

If appropriate, document that the software versions and header dates should be synced.

### Draft New Article

Please draft an article on the difference between what I call
Fast Move Consumer Goods (FMCG) engineering,
and mission-critical engineering.
I highly suspect that there is an industry standard,
or conventional term for "FMCG Engineering."
I will use FMCG for the spec, but please use the conventional term in the article.
Research this topic and fold reference links into the body.
Include "Future Reading" section, and a comprehensive list of references.
Title the article appropriately, and assign a filename that reflects the title.

#### Background

In my experience, there are two kinds of engineering:

- Fast Move Consumer Goods (FMCG)
- Mission-Critical

The most succinct way I have found to differentiate the two
is whether or not a poor quality MVP has positive or negative value.
The idea is that some engineer projects value speed more than correctness.
If your poor quality MVP has:

- Positive value because you can iterate on user feedback
  and make things better, you are in FMCG land.
  Examples: Video Streaming, Video Games
- Negative because you will probably go out of business for killing someone or
  losing a lot money, you are in mission-critical land.
  Examples: Aerospace, FinTech, AdTech

Most projects tend towards FMCG, where shipping yesterday would have been ideal.
A number of projects have a mission-critical core that needs to be correct,
and a FMCG shell that can be acceptably iterated upon to iron out quality issues
with live users.

The FMCG and mission-critical mindsets are very different.

- FMCG: Ship when possible, fix later.
- Mission-Critical: Fix now, ship when ready.

A FMCG mindset on a mission-critical project may get people killed.
A mission-critical mindset on a FMCG project will likely be too slow to be competitive.
It is possible for the same person to adapt their mindset to the project,
and it is also important to know what kind of project you are working on.
If the project has a mission-critical core with a FMCG shell,
defining that boundary is important.

#### Publication

Assign article number and prospective publication date, but do not publish.

## Context

I want to get a couple of articles published while I still remember what they are.

## Constraints

(none)

## Success Criteria

- New article drafted and in release candidate status.
- Date sync documented in knowledge graph.

## Notes

(none)
