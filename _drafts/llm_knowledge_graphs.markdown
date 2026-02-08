---
layout: post
mathjax: false
comments: true
title: "LLM Knowledge Graphs"
date: 2026-02-08 06:10:36 +0000
categories: ai ai-tools development developer-productivity
---

<!-- Axxx -->

AI coding agents are only as effective as the context they receive.
A model with no knowledge of a project's architecture, conventions, or tooling
will produce generic code that misses the mark.
The emerging solution is not a traditional knowledge graph
built from entity-relationship triples in a graph database.
It is a collection of structured markdown files
that form a navigable, hierarchical knowledge base
optimized for consumption by large language models.

This article examines the practice of building documentation knowledge graphs
for AI coding agents.
It traces the evolution from simple README files
to the multi-layered context hierarchies used by tools like Claude Code,
and argues that the principles of knowledge graph design
apply directly to how developers should organize project documentation
for AI-assisted workflows.
The `_docs/` directory in this blog's repository serves as a worked example.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-08 06:10:36 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64

$ sw_vers
ProductName:		macOS
ProductVersion:		14.6.1
BuildVersion:		23G93

# Hardware Information
$ system_profiler SPHardwareDataType | sed -n '8,10p'
      Chip: Apple M1 Max
      Total Number of Cores: 10 (8 performance and 2 efficiency)
      Memory: 32 GB

# Shell and Version
$ echo "${SHELL}"
/bin/bash

$ "${SHELL}" --version | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin23)

# Claude Code Installation Versions
$ claude --version
2.1.37 (Claude Code)
```

## The Knowledge Problem

Every AI coding agent faces the same fundamental challenge.
The model has been trained on public code and documentation,
but it knows nothing about the specific project it is working on.
The architecture, the naming conventions,
the build commands, the test strategy,
the reasons behind past design decisions,
and the tribal knowledge carried by the team
are all absent from the model's training data.

Without this context, the agent must either ask questions,
make assumptions, or explore the codebase through trial and error.
Each of these strategies consumes tokens.
Anthropic's engineering team defines context engineering as
"the set of strategies for curating and maintaining
the optimal set of tokens during LLM inference."
Every token in the context window competes for the model's attention.
Irrelevant information dilutes the signal.
Missing information forces the agent to guess.

The solution that has emerged across the industry
is to encode project knowledge in structured markdown files
that the agent loads at the start of a session.
These files form what this article calls an LLM knowledge graph.
The term "knowledge graph" is used deliberately.
Although these are not traditional graphs with formal triples and query languages,
they exhibit the structural properties of a graph.
Files are nodes.
Cross-references between files are edges.
The agent traverses the graph by following references
from high-level orientation documents to detailed specification files.

### From READMEs to Agent Configuration

The practice of writing documentation for AI agents
began with simple rule files.
Cursor introduced `.cursorrules` in 2024,
a single file at the project root
containing instructions for the AI assistant.
GitHub Copilot followed with `.github/copilot-instructions.md`.
Windsurf used `.windsurfrules`.
Each tool defined its own format,
and developers who used multiple tools
had to maintain redundant files with the same information.

Claude Code introduced `CLAUDE.md`,
a markdown file at the project root
that the agent reads at session start.
The AGENTS.md specification emerged in mid-2025
as a cross-platform standard,
now supported by over 60,000 open-source repositories
and endorsed by GitHub Copilot, Cursor, Claude Code, and Gemini CLI.
In December 2025, Anthropic, Block, and OpenAI
donated AGENTS.md to the Linux Foundation's Agentic AI Foundation,
alongside the Model Context Protocol and Goose,
signaling a move toward standardization.

ThoughtWorks placed AGENTS.md on their Technology Radar,
describing it as "a common format for providing instructions
to AI coding agents working on a project."
The framing is significant.
These files are not documentation in the traditional sense.
They are configuration artifacts
that directly shape the behavior of autonomous systems.

### The Knowledge Hierarchy

A single configuration file at the project root
is better than nothing, but it does not scale.
A flat file that tries to capture everything about a project
becomes bloated, difficult to maintain, and counterproductive.
Research by HumanLayer suggests that instruction-following quality
decreases as instruction count increases.
Every token in the configuration file
is loaded into every agent request,
creating what Builder.io calls "a hard budget problem."

The solution is a hierarchy.
Claude Code implements a four-level memory architecture
with explicit precedence ordering.

1. **Enterprise Policy**. Organization-level rules enforced by IT administrators. Highest priority.
2. **User Memory**. Global personal preferences stored at `~/.claude/CLAUDE.md`.
3. **Project Memory**. Project-level instructions in `CLAUDE.md` and `.claude/rules/` at the project root.
4. **Directory-Scoped Memory**. `CLAUDE.md` files in subdirectories, loaded on demand when the agent works in that subtree.

More specific rules override more general ones on conflict.
Directory-scoped files load only when needed,
which means the agent does not carry the full weight
of every subdirectory's knowledge in every interaction.

Anthropic's Agent Skills specification
extends this principle further with a three-level progressive disclosure model.
At startup, only the skill name and description are loaded,
consuming roughly 50 tokens per skill.
If the agent determines a skill is relevant to the current task,
it loads the full `SKILL.md` body at roughly 500 tokens.
Supplementary resources like scripts and reference files
load only when specific sub-tasks require them.
This design is analogous to lazy evaluation in graph traversal,
where nodes are fully expanded only when visited.

### A Worked Example

The `_docs/` directory in this blog's repository
illustrates these principles in practice.
The directory was designed from the start
as a knowledge graph for AI agent consumption,
following three structural principles documented in `DOCUMENTATION_STRATEGY.md`.

**Atomic files.** Each file covers one concept.
This keeps the signal-to-noise ratio high
and allows the agent to load only the context it needs.
A file on post structure does not also cover git strategy.
A file on the communication protocol does not also cover prose style.

**Hierarchical organization.** Every section has a `README.md`
that serves as a table of contents.
The root `_docs/README.md` links to four section directories.
Each section `README.md` links to the atomic files within it.
The agent can navigate from the root to any specific document
in at most two hops.

**Breadcrumb navigation.** Every file includes
an upward navigation link to its parent table of contents
and the documentation root.
This allows the agent to reorient itself
if it has navigated deep into the hierarchy.

The resulting structure is a directed acyclic graph
with well-defined traversal semantics.

```
CLAUDE.md (entry point)
└── _docs/README.md (root index)
    ├── writing/README.md
    │   ├── STYLE_GUIDE.md
    │   └── POST_STRUCTURE.md
    ├── architecture/README.md
    │   └── JEKYLL_STRUCTURE.md
    ├── process/README.md
    │   ├── COMMUNICATION.md
    │   ├── GIT_STRATEGY.md
    │   ├── CONTENT_WORKFLOW.md
    │   ├── TASKLOG.md
    │   ├── PROMPT.md
    │   └── REVERSE_PROMPT.md
    └── reference/README.md
        └── GLOSSARY.md
```

The `CLAUDE.md` file at the project root serves as the entry node.
It provides a high-level orientation
and a table linking to each section of `_docs/`.
An agent starting a new session reads `CLAUDE.md`,
then navigates to the relevant section
based on the task at hand.
If the task involves writing a new post,
the agent follows the path to `writing/README.md`
and then to `POST_STRUCTURE.md` and `STYLE_GUIDE.md`.
If the task involves the communication protocol,
it follows the path to `process/README.md`
and then to `COMMUNICATION.md`.

This navigation pattern is precisely how graph traversal works.
The agent starts at a root node,
reads the node's contents to determine which edges to follow,
and loads adjacent nodes on demand.
The graph structure ensures that the agent
never needs to load the entire knowledge base at once.
It loads only the path relevant to the current task.

### Graph Structure in Markdown

The claim that structured markdown documentation
forms a knowledge graph is not merely metaphorical.
The structure satisfies the formal properties of a directed graph.

**Nodes** are individual markdown files.
Each file has a well-defined scope and content.
In graph database terms, each node has properties:
a file path, a topic, a set of instructions or conventions.

**Edges** are the cross-references between files.
A relative markdown link like `[Style Guide](../writing/STYLE_GUIDE.md)`
is a directed edge from the referring document to the target.
Navigation breadcrumbs are upward edges.
Table-of-contents entries are downward edges.
Inline references to other files create lateral edges.

**Traversal** is the agent's process of reading files
and deciding which references to follow.
This is relevance-driven graph traversal.
The agent does not execute a formal query language.
It reads the contents of a node
and uses its understanding of the current task
to decide which adjacent nodes to visit.

The Artem Kulyabin GraphMD project
makes this structural parallel explicit,
treating markdown documents as primary artifacts
where documents and sections are nodes
and links and anchors are edges.
The Jeremy Howard `llms.txt` proposal
applies the same principle to web documentation,
creating site-level index files
optimized for LLM consumption.

The contrast with traditional knowledge graphs is instructive.
A traditional knowledge graph encodes entity-relationship-entity triples
optimized for SPARQL or Cypher queries.
An LLM knowledge graph encodes human-readable instructions
optimized for context windows.
The "query" is not a structured expression
but the model's inference about which references are relevant.
Both structures serve the same fundamental purpose.
They organize knowledge so that a consumer
can find what it needs without loading everything at once.

### Empirical Evidence

The practice of writing documentation for AI agents
has attracted empirical research.
Three peer-reviewed studies have now examined these configuration files at scale.

Chatlatanagulchai and colleagues analyzed 253 `CLAUDE.md` files
from 242 GitHub repositories.
They found that the files typically have shallow hierarchies
with one main heading and several subsections.
Build and run instructions appeared in 77.1% of files.
Implementation details appeared in 71.9%.
Architecture descriptions appeared in 64.8%.
Security appeared in only 8.7% and performance in only 12.7%.
This suggests that developers prioritize operational knowledge
over quality-attribute constraints.

A larger follow-up study by the same group
analyzed 2,303 context files from 1,925 repositories
across Claude Code, OpenAI Codex, and GitHub Copilot.
The key finding is that "these files are not static documentation
but complex, difficult-to-read artifacts
that evolve like configuration code,
maintained through frequent, small additions."
The researchers introduced the concept of "context debt"
as a new form of technical debt.
Just as code accumulates technical debt
that degrades maintainability over time,
agent configuration files accumulate stale or contradictory instructions
that degrade agent performance.

A January 2026 study measured the quantitative impact
of AGENTS.md files on agent efficiency.
The presence of AGENTS.md was associated with
a 28.64% reduction in median runtime
and a 16.58% reduction in output token consumption,
while maintaining comparable task completion behavior.
This is the first controlled evidence
that structured documentation produces measurable efficiency gains for agents.

### Pros and Cons

**Advantages**

- **Immediate feedback loop.** Unlike traditional documentation that may go unread for months, agent documentation produces visible improvements in agent behavior from the first session. This inverts the incentive problem that plagues traditional documentation.
- **Version-controlled knowledge.** Documentation lives in the repository alongside the code it describes, subject to the same review and versioning processes. Changes are auditable through git history.
- **Progressive disclosure.** Hierarchical structures allow agents to load only the knowledge relevant to the current task, keeping context windows lean.
- **Cross-session continuity.** A knowledge graph that persists in the repository provides continuity across AI sessions, reducing the cost of onboarding a new session to the project.
- **Measurable impact.** Empirical evidence shows that structured documentation reduces agent runtime and token consumption.
- **Dual-purpose documentation.** Well-structured agent documentation also serves human developers, reducing the traditional tension between writing for machines and writing for people.

**Limitations**

- **Context debt.** Configuration files accumulate stale instructions over time. Contradictory or outdated instructions actively degrade agent performance.
- **Fragmentation.** Different tools use different file formats. Maintaining consistent knowledge across `.cursorrules`, `copilot-instructions.md`, `CLAUDE.md`, and `AGENTS.md` creates duplication and drift.
- **Shallow knowledge.** Empirical studies show that developers prioritize operational commands over architectural rationale, security constraints, and design trade-offs. The resulting knowledge graphs are biased toward procedural knowledge.
- **Maintenance burden.** These files require active curation. Auto-generating them is tempting but risks producing verbose, low-signal content. Manual curation produces better results but demands ongoing effort.
- **No formal verification.** Unlike traditional knowledge graphs with schema validation, markdown knowledge graphs have no mechanism to detect logical contradictions, missing information, or structural inconsistencies.

### The Maintenance Problem

The most significant challenge facing LLM knowledge graphs is maintenance.
The Agent READMEs study found that 67.4% of Claude Code configuration files
undergo multiple modifications,
confirming that these are living documents rather than write-once artifacts.

The "context debt" concept captures the core risk.
Every instruction added to a configuration file
increases the context budget consumed per request.
Stale instructions do not merely waste tokens.
They actively mislead the agent.
An outdated build command will cause the agent to fail.
An outdated architectural constraint
will cause the agent to produce code
that contradicts the current state of the system.

HumanLayer recommends keeping `CLAUDE.md` files under 60 lines
and using "pointers over copies."
Rather than embedding code snippets or full file contents
in the configuration file,
include references to file paths
so the agent reads the current version on demand.
This is the same principle that database normalization applies.
Store the fact once and reference it,
rather than duplicating it across multiple locations.

The Builder.io guide recommends a reactive approach.
Add a rule "the second time you see the same mistake."
This treats the configuration file as a feedback mechanism
rather than a comprehensive specification.
The agent makes a mistake.
The developer adds a rule to prevent recurrence.
Over time, the file captures the project's most important conventions
through observed failure modes rather than upfront enumeration.

Tools like ai-rules-sync and block/ai-rules
have emerged to address the fragmentation problem,
allowing developers to define rules once
and synchronize them across multiple tool-specific formats.
But the underlying tension between
automation for consistency and manual curation for quality remains unresolved.

## Conclusion

The structured markdown documentation that developers write
for AI coding agents is not merely configuration.
It is a knowledge graph.
The files are nodes.
The cross-references are edges.
The agent's process of reading files and following references
is graph traversal.

This framing matters because it imports decades of knowledge graph design principles
into a problem that the industry is solving by trial and error.
Principles like atomic decomposition,
hierarchical organization,
progressive disclosure,
and normalization through references rather than duplication
are not new ideas.
They are established practices from knowledge engineering
that apply directly to how developers should structure documentation for AI agents.

The empirical evidence supports the value of this approach.
Structured documentation reduces agent runtime.
It reduces token consumption.
It produces measurable improvements in agent effectiveness.
The challenge is maintenance.
Context debt is a real and growing concern,
and the tooling for detecting and remediating it
is still in its early stages.

The recommendation for practitioners is straightforward.
Treat your project's agent documentation
as a knowledge graph with intentional structure.
Keep files atomic and focused.
Organize them hierarchically.
Use references instead of copies.
Add rules reactively based on observed agent mistakes.
Review and prune regularly to prevent context debt.
The payoff is immediate.
The agent that reads your documentation becomes measurably more effective
from the first session.

## Future Reading

- [Effective Context Engineering for AI Agents][anthropic_context_engineering] by Anthropic,
  covering compaction, structured note-taking, and progressive disclosure
  for maintaining context in long-running agent sessions.

- [Agent READMEs: An Empirical Study of Context Files for Agentic Coding][research_agent_readmes]
  by Chatlatanagulchai and colleagues,
  providing the largest empirical study of agent configuration files
  and introducing the concept of context debt.

- [Context Engineering for Coding Agents][industry_fowler_context] by Birgitta Boeckeler
  on Martin Fowler's site,
  surveying the current landscape of context configuration features
  across AI coding tools.

- [Equipping Agents for the Real World with Agent Skills][anthropic_agent_skills] by Anthropic,
  introducing the three-level progressive disclosure model
  for composable agent knowledge.

- [The /llms.txt File][standard_llms_txt] by Jeremy Howard,
  proposing a standard for LLM-optimized documentation
  that has been adopted by hundreds of thousands of websites.

## References

- [Anthropic, Effective Context Engineering for AI Agents][anthropic_context_engineering]
- [Anthropic, Equipping Agents for the Real World with Agent Skills][anthropic_agent_skills]
- [Blog, Bidirectional Agentic Workflow][blog_bidirectional]
- [Blog, Markdown as a Specification Language for Agentic Workflows][blog_markdown_spec]
- [Claude Code, Manage Claude's Memory][cc_memory]
- [Industry, AGENTS.md May Trick Us into Writing Better Docs][industry_kilo_docs]
- [Industry, Context Engineering for Coding Agents][industry_fowler_context]
- [Industry, Fixing Claude Code's Amnesia][industry_episodic_memory]
- [Industry, Mastering Project Context Files for AI Coding Agents][industry_eclipsesource]
- [Industry, Personal AI Infrastructure][industry_miessler_pai]
- [Industry, Spotify Background Coding Agents Part 2: Context Engineering][industry_spotify_context]
- [Industry, Writing a Good CLAUDE.md][industry_humanlayer]
- [Protocol, AGENTS.md][protocol_agents_md]
- [Research, Agent READMEs: An Empirical Study of Context Files][research_agent_readmes]
- [Research, Decoding the Configuration of AI Coding Agents][research_santos_config]
- [Research, On the Impact of AGENTS.md Files on Efficiency][research_agents_md_impact]
- [Research, On the Use of Agentic Coding Manifests][research_agentic_manifests]
- [Standard, The /llms.txt File][standard_llms_txt]
- [Standard, ThoughtWorks Technology Radar: AGENTS.md][standard_thoughtworks_radar]
- [Tool, GraphMD: Turning Markdown into Knowledge Graphs][tool_graphmd]

[anthropic_context_engineering]: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
[anthropic_agent_skills]: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
[blog_bidirectional]: {% post_url 2026-02-06-bidirectional_agentic_workflow %}
[blog_markdown_spec]: {% post_url 2026-02-08-markdown_as_a_specification_language %}
[cc_memory]: https://code.claude.com/docs/en/memory
[industry_kilo_docs]: https://blog.kilo.ai/p/agentsmd-may-trick-us-into-writing
[industry_fowler_context]: https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
[industry_episodic_memory]: https://blog.fsck.com/2025/10/23/episodic-memory/
[industry_eclipsesource]: https://eclipsesource.com/blogs/2025/11/20/mastering-project-context-files-for-ai-coding-agents/
[industry_miessler_pai]: https://danielmiessler.com/blog/personal-ai-infrastructure
[industry_spotify_context]: https://engineering.atspotify.com/2025/11/context-engineering-background-coding-agents-part-2
[industry_humanlayer]: https://www.humanlayer.dev/blog/writing-a-good-claude-md
[protocol_agents_md]: https://agents.md/
[research_agent_readmes]: https://arxiv.org/abs/2511.12884
[research_santos_config]: https://arxiv.org/abs/2511.09268
[research_agents_md_impact]: https://arxiv.org/abs/2601.20404
[research_agentic_manifests]: https://arxiv.org/abs/2509.14744
[standard_llms_txt]: https://llmstxt.org/
[standard_thoughtworks_radar]: https://www.thoughtworks.com/en-us/radar/techniques/agents-md
[tool_graphmd]: https://medium.com/generative-ai-revolution-ai-native-transformation/introducing-graphmd-turning-markdown-documents-into-executable-knowledge-graphs-6925d936423f
