# Prompt Staging Area

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is a staging area for complex human-to-AI instructions. The human pilot drafts and refines prompts here before execution.

---

# Current Prompt

## Comments

A78 is ready for publication later today.
We will be doing some housekeeping while figuring out backlog drafts.
Ideally, I want to post one article per day with a backlog of complete articles.

## Objectives

### Release Announcement

Articles need a release announcement.
After an article is published, a release announcement should be suggested in the reverse prompt.
The template follows.

```
New Blog Post: <title>

<hook> <brief summary>

Key takeaways:
- <Key takeaway A>
- <Key takeaway B>
- <Key takeaway C>

You can read the full article here:
<URL>

Let me know your thoughts. I would love to hear about <your topical application of material>!

<#hashtags>
```

To give a concrete example, here is the actual announcement for A77 that was posted on LinkedIn.

```
New Blog Post: LLM Knowledge Graphs

AI coding agents are only as effective as the context they receive.
Many teams treat agent instructions as flat config files, but in practice the most effective setups behave like knowledge graphs optimized for how LLMs actually load and traverse context.

In this article, I break down how structured markdown documentation functions as a navigable knowledge graph for AI coding agents, why this approach measurably improves agent performance, and how teams can design documentation that scales without bloating context windows.

Key takeaways:
- Structured markdown files form a graph, not just documentation. Files are nodes, links are edges, and agent context loading is traversal.
- Hierarchical, atomic documentation enables progressive disclosure, reducing token usage and improving agent reliability.
- Empirical research shows agent configuration files improve efficiency, but also introduce a new "context debt" risk that must be actively managed.

You can read the full article here:
https://sgeos.github.io/ai/ai-tools/development/developer-productivity/2026/02/07/llm_knowledge_graphs.html

Let me know your thoughts. I would love to hear how you are structuring project context or agent documentation in your own workflows!

hashtag#AI hashtag#LLM hashtag#DeveloperProductivity hashtag#ContextEngineering hashtag#KnowledgeGraphs hashtag#AgenticAI hashtag#Documentation
```

Please document this protocol in the knowledge graph.

### Draft Mathmatical Proofs Post

Please take the tier 4 proofs stub, research the topic, and draft a full post.
It should cover the following.

- What a mathematical proof is
- How they are written
- Why proofs are important
- Why proofs are important to software engineers
- Why proofs are important in the age of agentic workflows

If the old draft does not have an article number, give it the next available number and make sure to add/update the the article number comment!

### Blog Branding Assessment and Candidate Future Post Topics

Review topics to date, including those in draft limbo.
Comment on the emergent blog brand in your reverse prompt.
Add a table of topical on-brand post ideas in a table at the end of `old_drafts.md`.

## Context

A78 is ready, but it is too soon to publish.

## Constraints

(no comment)

## Success Criteria

- Knowledge graph updated.
- Mathematical proofs post drafted with research fully folded into the document.
- Blog branding assessment reported.
- Candidate future post topics added to table at end of `old_drafts.md`.

## Notes

(no comment)
