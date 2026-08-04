---
layout: post
mathjax: false
comments: true
title: "The State of Context Engineering in Early 2026"
date: 2026-02-09 01:14:33 +0000
categories: ai ai-tools development developer-productivity
series: agentic_workflows
series_title: Agentic Workflows
series_index: 4
---
<!-- A78 -->
<script>console.log("A78");</script>

Context engineering has emerged as a distinct discipline
in the eighteen months since AI coding agents
moved from experimental tools to production infrastructure.
The term was popularized by Anthropic in September 2025,
but the underlying practices had been developing for over a year prior.
By early 2026, context engineering has its own standards body,
its own empirical research literature,
and its own failure modes that practitioners have documented through hard experience.

This article surveys the state of context engineering as of February 2026.
It traces how the field emerged from prompt engineering,
examines the tools and standards that define the current landscape,
reviews the empirical evidence for what works,
and identifies the challenges that remain unsolved.
The three preceding articles in this series cover related ground.
[Bidirectional Agentic Workflow][blog_bidirectional] documents
a communication protocol for human-agent collaboration.
[Markdown as a Specification Language][blog_markdown_spec] argues
that structured markdown is the practical specification format for agent instructions.
[LLM Knowledge Graphs][blog_knowledge_graphs] examines
how documentation repositories function as navigable knowledge structures for agents.
This article steps back to survey the broader field
that these practices exist within.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-08 01:14:33 +0000

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

## From Prompt Engineering to Context Engineering

Prompt engineering, the practice of crafting individual queries
to elicit desired behavior from a language model,
was the dominant paradigm for working with LLMs through 2023 and most of 2024.
A developer would refine a single prompt,
adjusting phrasing and structure until the model produced useful output.
This approach works for one-shot interactions
but breaks down when agents operate over multiple turns,
read and write files, execute commands,
and maintain state across long sessions.

The term "context engineering" has a traceable lineage.
Prompt engineer Riley Goodside used the phrase as early as 2023,
but it remained niche until mid-2025.
The inflection point came in June 2025
when Shopify CEO Tobi Lutke posted that he preferred
"context engineering" over "prompt engineering"
because it "describes the core skill better:
the art of providing all the context for the task
to be plausibly solvable by the LLM."
Andrej Karpathy endorsed the shift shortly after,
describing context engineering as
"the delicate art and science of filling the context window
with just the right information for the next step."

Simon Willison argued that the term would stick
because its "inferred definition" is much closer to the intended meaning
than "prompt engineering,"
which many people dismiss as
"a laughably pretentious term for typing things into a chatbot."
Willison observed that "context engineering" captures the fact
that previous model responses, tool outputs, and retrieved documents
are all critical parts of the process, not just user prompts.

Anthropic formalized the distinction
in their September 2025 blog post on context engineering.
They defined context engineering as
"the set of strategies for curating and maintaining
the optimal set of tokens during LLM inference."
Where prompt engineering asks
"how do I phrase this question to get a good answer,"
context engineering asks
"what total configuration of information
is most likely to produce the desired behavior
over the full lifecycle of this agent session."

Karpathy's 2025 year-in-review
reinforced this framing by conceptualizing LLMs
as "a new kind of operating system"
where the LLM is like the CPU
and the context window is like RAM,
the model's working memory.
This analogy makes the resource management aspect explicit.
Just as an operating system must manage limited RAM
across competing processes,
an agent must manage a limited context window
across competing information needs.

The shift is significant because it reframes the problem.
Prompt engineering treats the model as a function.
Context engineering treats the model as a system
with memory, state, and resource constraints.
The context window is a finite budget.
Every token of system instruction, tool output, file content,
and conversation history competes for attention.
Irrelevant information dilutes the signal.
Missing information forces the agent to guess or explore.
Context engineering is the discipline of managing this budget
to maximize agent effectiveness.

Andrej Karpathy popularized the observation
that "the hottest new programming language is English" in January 2023.
As argued in [Markdown as a Specification Language][blog_markdown_spec],
the reality is more nuanced.
Unstructured natural language is insufficient for reliable agent behavior.
The specifications that agents consume need structure,
and the dominant format for that structure is markdown.
Context engineering is, in practice, the engineering of markdown documents
that agents load, parse, and act upon.

## The Current Tool Landscape

By early 2026, every major AI coding tool
has implemented some form of context engineering infrastructure.
The convergence is notable even as fragmentation persists.

### Configuration Files

The simplest layer of context engineering
is the static configuration file at the project root.

Claude Code reads `CLAUDE.md` files
from a four-level hierarchy with explicit precedence ordering.
Enterprise policies override project-level rules,
which override user-level preferences,
which override directory-scoped instructions.
Files in subdirectories load on demand
when the agent works in that subtree,
implementing a form of progressive disclosure.

GitHub Copilot reads `.github/copilot-instructions.md`
and supports `.instructions.md` files
with `applyTo` fields for path-specific instructions.
VS Code now provides an official context engineering guide
that includes custom agent files
for plan-and-implement workflows.
Cursor reads files from the `.cursor/rules/` directory
and supports glob-pattern scoping
that activates rules only for matching file paths.
Cursor rules have evolved from the original single `.cursorrules` file
through a `.cursor/` folder with `index.mdc`
to the current multi-file architecture
with context-aware dynamic rules.
Gemini CLI reads `GEMINI.md` files following a similar pattern.

Each tool uses its own file format and conventions.
A project that uses multiple tools
must maintain redundant configuration files.
The AGENTS.md specification emerged as a response to this fragmentation.

### AGENTS.md and Standardization

AGENTS.md is a plain markdown file
designed to provide project-specific instructions
to any AI coding agent.
Released in August 2025 and donated to the Linux Foundation's
Agentic AI Foundation in December 2025,
it represents the first cross-platform standard
for agent configuration.

Over 60,000 open-source repositories have adopted AGENTS.md.
ThoughtWorks placed it on their Technology Radar,
describing it as "a common format for providing instructions
to AI coding agents working on a project."
The standard is intentionally minimal.
It requires no special fields or formatting
and relies on the ability of LLM-based agents
to interpret human-readable guidance.

The standardization effort addresses fragmentation
but does not fully solve it.
Tool-specific features like Cursor's glob-pattern scoping
or Claude Code's hierarchical memory
have no equivalent in the AGENTS.md format.
Developers who need these features
must still maintain tool-specific files alongside AGENTS.md.

### Model Context Protocol

The Model Context Protocol (MCP) provides a complementary standard
for dynamic context.
Announced by Anthropic in November 2024,
MCP enables agents to access external data sources
through a standardized interface.
MCP servers can expose database schemas, API documentation,
issue trackers, and other live information
that agents need during a session.

The pace of MCP adoption has been remarkable.
OpenAI adopted MCP across the Agents SDK, Responses API,
and ChatGPT desktop in March 2025.
Google DeepMind confirmed MCP support in Gemini models in April 2025.
GitHub and Microsoft joined MCP's steering committee at Build 2025 in May.
Major specification updates followed in November 2025,
including asynchronous operations, statelessness, server identity,
and an official registry.
In December 2025, MCP was donated to the Agentic AI Foundation
alongside AGENTS.md.
Where AGENTS.md and configuration files provide static project knowledge,
MCP provides the plumbing for runtime context retrieval.

Anthropic's Agent Skills specification builds on this foundation
with a three-level progressive disclosure model.
At startup, only the skill name and description load,
consuming roughly 50 tokens per skill.
If the agent determines a skill is relevant,
it loads the full SKILL.md body at roughly 500 tokens.
Supplementary resources load only when sub-tasks require them.
This design treats context as a scarce resource
and allocates it incrementally based on demonstrated need.

### The llms.txt Standard

Jeremy Howard's llms.txt proposal
extends the context engineering pattern to web documentation.
A website places a markdown index file at `/llms.txt`
that provides LLM-friendly content
optimized for consumption within context windows.
Over 844,000 websites have implemented it,
including Anthropic, Cloudflare, Docker, and HubSpot.
The complementary `llms-full.txt` variant
includes all detailed content in a single file,
eliminating the need for link traversal.

The llms.txt standard shares the same design principles
as project-level context engineering.
Both filter and structure information for machine consumption.
Both prioritize signal density over completeness.
Both acknowledge that context windows are finite
and that not everything can fit.

## Empirical Evidence

The practice of context engineering
has attracted a small but growing body of empirical research.
Six studies published between August 2025 and January 2026
provide quantitative data on how context files are written,
how they evolve, and what impact they have.

### The Content of Context Files

Chatlatanagulchai and colleagues analyzed 253 CLAUDE.md files
from 242 GitHub repositories in September 2025.
They found that the files typically have shallow hierarchies
with one main heading and several subsections.
Build and run instructions appeared in 77.1% of files.
Implementation details appeared in 71.9%.
Architecture descriptions appeared in 64.8%.
Security appeared in only 8.7% and performance in only 12.7%.
This distribution suggests that developers prioritize
operational knowledge over quality-attribute constraints.

### Evolution Patterns

A larger follow-up study by the same group
analyzed 2,303 context files from 1,925 repositories
across Claude Code, OpenAI Codex, and GitHub Copilot.
The central finding is that "these files are not static documentation
but complex, difficult-to-read artifacts
that evolve like configuration code,
maintained through frequent, small additions."
The researchers found that 67.4% of Claude Code configuration files
undergo multiple modifications,
confirming that these are living documents
that require active maintenance.

This study also introduced the concept of "context debt"
as a new form of technical debt.
Just as code accumulates technical debt
that degrades maintainability over time,
agent configuration files accumulate stale or contradictory instructions
that degrade agent performance.

### Configuration Patterns

Santos and colleagues analyzed 328 configuration files
from public Claude Code projects in November 2025.
They identified co-occurrence patterns
in how software engineering concerns
are grouped within individual configuration files.
Architecture specification emerged as particularly important.
Projects that provided architectural context to agents
saw more consistent adherence to design patterns.

### Adoption in Open Source

Mohsenimofidi and colleagues investigated
the adoption of AI configuration files
in 466 open-source projects in October 2025.
They found no established structure yet,
with significant variation in how context is provided.
Instructions fall into five categories:
descriptive, prescriptive, prohibitive, explanatory, and conditional.
This taxonomy suggests that context files
serve multiple communicative functions simultaneously,
which may contribute to the maintenance burden
that other studies have documented.

### Multi-Agent Context

A study on context engineering
for multi-agent LLM code assistants in August 2025
described structured layering of context
where agents work with role-specific prompts,
CLAUDE.md context, task-specific instructions,
and relevant code or knowledge snippets.
The multi-agent setting introduces
a context multiplication problem.
If a root agent passes its full history to a sub-agent,
and that sub-agent does the same,
the token count explodes
and sub-agents become confused by irrelevant conversational history.

### Efficiency Impact

A January 2026 study measured the quantitative impact
of AGENTS.md files on agent efficiency.
Analyzing 10 repositories and 124 pull requests,
the researchers found that the presence of AGENTS.md
was associated with a 28.64% reduction in median runtime
and a 16.58% reduction in output token consumption,
while maintaining comparable task completion behavior.
This is the first controlled evidence
that structured context engineering
produces measurable efficiency gains.

## Enterprise Adoption

Anthropic's 2026 Agentic Coding Trends Report,
released in January 2026,
provides a window into enterprise adoption.
The report identifies eight trends organized into three categories.
Foundation trends change how development happens.
Capability trends expand what agents accomplish.
Impact trends affect business outcomes.

The headline finding is that engineers
are moving from writing code themselves
to coordinating AI agents that handle implementation.
However, developers report being able to "fully delegate"
only 0-20% of tasks,
with the rest requiring active supervision,
validation, and human judgment.

Case studies from the report illustrate the scale.
Rakuten engineers tested Claude Code
on implementing an activation vector extraction method
in a 12.5-million-line codebase.
The agent finished the job in seven hours
and achieved 99.9% numerical accuracy.
TELUS teams created over 13,000 custom AI solutions
while shipping engineering code 30% faster,
saving over 500,000 hours total.

Spotify's engineering team published a three-part series
on their experience with background coding agents.
They deployed agents at scale for code migrations,
merging over 1,500 AI-generated pull requests into production.
Their key observation about context engineering
is that "prompts evolve by trial and error
without yet having structured ways to evaluate
which prompts or models perform best."
This points to a maturity gap.
Enterprise teams are investing heavily in context engineering
but lack systematic methods for measuring and improving it.

## Practitioner Strategies

While the empirical research documents what developers are doing,
a growing body of practitioner writing
documents what developers should be doing.
Several frameworks have emerged
for thinking systematically about context management.

### The LangChain Taxonomy

LangChain's context engineering series
proposes four strategic categories for managing context.
**Write** creates new context through system prompts
and structured instructions.
**Select** retrieves relevant context
from larger knowledge bases using search and filtering.
**Compress** reduces context volume
through summarization and compaction.
**Isolate** separates concerns
by routing different types of context to different agents or tools.
This taxonomy provides a useful vocabulary
for discussing context engineering decisions
and maps cleanly to the technical mechanisms
that tools like Claude Code implement.

### Frequent Intentional Compaction

Dex Horthy of HumanLayer introduced
the concept of Frequent Intentional Compaction,
a workflow design pattern that targets
40-60% context window utilization.
Rather than allowing the context to fill organically
and relying on automatic compaction at the limit,
Horthy's approach designs the entire development workflow
around context management.
A research-plan-implement pattern
provides each step with only the exact context
needed to be successful.
This is the most explicit articulation
of context budgeting as a first-class engineering concern.

### Context as Screenplay

Addy Osmani's series on context engineering,
published on O'Reilly Media,
frames the practice as writing
"the full screenplay for the AI"
rather than crafting "a magical sentence."
Osmani covers tool use and environmental context,
guardrails and safety,
and the architectural decisions
around providing the right information at the right time.
The screenplay metaphor is instructive.
A screenplay specifies setting, character knowledge,
available props, and constraints on behavior.
Context engineering does the same
for an AI agent's operating environment.

### Production Lessons from Manus

Yichao "Peak" Ji shared production insights
from building the Manus agent.
Several lessons stand out.
The KV-cache hit rate is the single most important metric
for production agents.
Cached tokens cost ten times less with Claude Sonnet,
making cache-friendly context design
an economic imperative at scale.
The file system serves as unlimited external memory,
and task recitation through constantly rewriting a todo file
combats goal drift in long sessions.
Perhaps most counterintuitively,
leaving failed actions in context helps the agent learn.
Removing errors deprives the model of negative examples.
Ji calls the iterative process of rebuilding
the agent framework "Stochastic Graduate Descent,"
a deliberate play on words
that captures the trial-and-error nature
of context engineering in practice.

## Unsolved Challenges

Despite the progress in tooling and standardization,
several fundamental challenges remain.

### Context Rot

Chroma's research on context rot measured 18 LLMs and found that
"models do not use their context uniformly.
Instead, their performance grows increasingly unreliable
as input length grows."
This means that simply adding more context
does not linearly improve agent behavior.
There is a point of diminishing returns
beyond which additional information
actively degrades performance.

The practical implication is that context engineering
is not just about what to include.
It is equally about what to exclude.
Anthropic's guidance recommends that system prompts
"present ideas at the right altitude for the agent."
Too much detail overwhelms.
Too little leaves gaps.
Finding the right level of abstraction
is the core skill of context engineering.

### The Scalability Gap

Factory.ai documented "the context window problem"
for enterprise-scale codebases.
Large language models have context windows
of approximately one million tokens.
A typical enterprise monorepo can span thousands of files
and several million tokens.
This gap between what the model can hold
and what the project contains
is a fundamental bottleneck.

Factory's response is to build layers of scaffolding.
Structured repository overviews provide architectural context.
Semantic search retrieves relevant files.
Targeted file operations stay within the context budget.
The philosophy is to treat context
as a scarce, high-value resource,
"carefully allocating and curating it
with the same rigor one might apply
to managing CPU time or memory."

### Configuration Fragmentation

Each tool's proprietary configuration format
creates duplication and potential inconsistency.
A project using Claude Code, Copilot, and Cursor
must maintain CLAUDE.md, copilot-instructions.md,
and Cursor rules files.
AGENTS.md provides a cross-platform baseline
but does not replace tool-specific features.

Tools like ai-rules-sync and block/ai-rules
have emerged to synchronize rules across formats,
but the underlying tension remains.
The more tool-specific features a developer uses,
the more configuration diverges.

### Production Readiness

VentureBeat reported on the gap between
AI coding agent demos and production deployment.
The failure modes include brittle context windows
where agents "start strong,
make sensible changes to the first few files,
then progressively lose track of what they were doing."
Operational awareness gaps manifest
when agents attempt to execute commands
incompatible with the target environment.
Repeated hallucinations within a single session
force developers to restart and re-provide all context.

These failure modes are fundamentally context problems.
The agent loses track because context degrades over long sessions.
The agent misunderstands the environment
because environmental context is missing or stale.
The agent hallucinates because
irrelevant context drowns out relevant information.
Better context engineering mitigates each of these failures,
but does not eliminate them.

## Where the Field is Heading

Several trends suggest the direction of context engineering
over the next year.

**Larger context windows.**
Claude Opus 4.6 introduced a one-million-token context window in February 2026.
Larger windows ease the budget constraint
but do not eliminate the need for curation.
Context rot research shows that more tokens
do not automatically mean better performance.

**Standards convergence.**
The Agentic AI Foundation's governance of AGENTS.md
and MCP signals industry movement toward shared standards.
The question is whether convergence will be deep enough
to eliminate the need for tool-specific configuration.

**Automated context management.**
Tools are beginning to automate context curation.
Claude Code's auto-compaction summarizes earlier conversation
when approaching context limits.
Agent Skills load resources incrementally based on task relevance.
The trend is toward systems that manage their own context budgets
rather than relying entirely on developer-authored static files.

**Empirical evaluation.**
Spotify's observation that teams lack
"structured ways to evaluate which prompts or models perform best"
identifies a clear gap.
The January 2026 AGENTS.md efficiency study
is a step toward systematic evaluation,
but the field needs broader benchmarks
and evaluation frameworks
for context engineering practices.

**Context as architecture.**
The most significant shift may be conceptual.
As [LLM Knowledge Graphs][blog_knowledge_graphs] argues,
documentation repositories for AI agents
exhibit the structural properties of directed graphs.
Treating context engineering as a form of information architecture,
rather than an ad hoc collection of configuration files,
imports established design principles from knowledge engineering.
Atomic decomposition, hierarchical organization,
progressive disclosure, and normalization through references
are not new ideas.
They are proven techniques being rediscovered
in the context of AI-assisted development.

## Conclusion

Context engineering in early 2026
has moved beyond the experimental phase
but has not yet reached maturity.
The field has standards, empirical research,
enterprise adoption, and documented best practices.
It also has fragmentation, scalability challenges,
context rot, and a lack of systematic evaluation methods.

The central insight of context engineering
is that the quality of the context
determines the quality of the agent's output.
A model's training data provides general capability.
Context provides capability.
The most capable model in the world
will produce generic, off-target results
without project-specific context.
A less capable model with well-engineered context
will often outperform it.

The recommendation for practitioners
is the same as it was for traditional software engineering.
Treat your agent's context with the same rigor
you apply to your code.
Version it. Review it. Test it.
Prune it when it becomes stale.
Structure it for the consumer, not for the author.
Context engineering is not a passing trend.
It is the interface layer between human intent and machine execution,
and getting it right is the difference between
an AI agent that helps and one that hinders.

## Future Reading

- [Effective Context Engineering for AI Agents][anthropic_context_engineering] by Anthropic,
  the foundational reference that defines context engineering
  and provides strategies for managing context in agent systems.

- [2026 Agentic Coding Trends Report][anthropic_trends_report] by Anthropic,
  surveying enterprise adoption of AI coding agents
  with case studies from Rakuten and TELUS.

- [Context Engineering for AI Agents: Lessons from Building Manus][industry_manus]
  by Yichao "Peak" Ji,
  sharing production lessons on KV-cache optimization,
  file system memory, and task recitation.

- [Agent READMEs: An Empirical Study of Context Files][research_agent_readmes]
  by Chatlatanagulchai and colleagues,
  the largest empirical study of agent configuration files
  introducing the concept of context debt.

- [Context Engineering: Bringing Engineering Discipline to Prompts][industry_osmani]
  by Addy Osmani on O'Reilly,
  framing context as "the full screenplay for the AI"
  with coverage of tool use, guardrails, and architectural decisions.

- [The Context Window Problem][industry_factory_context] by Factory.ai,
  examining the scalability gap between context windows
  and enterprise codebases.

- [Context Engineering for Coding Agents][industry_fowler_context]
  by Birgitta Boeckeler on Martin Fowler's site,
  a practitioner survey of context configuration features
  across AI coding tools.

## References

- [Anthropic, 2026 Agentic Coding Trends Report][anthropic_trends_report]
- [Anthropic, Effective Context Engineering for AI Agents][anthropic_context_engineering]
- [Anthropic, Equipping Agents for the Real World with Agent Skills][anthropic_agent_skills]
- [Anthropic, Introducing the Model Context Protocol][anthropic_mcp]
- [Blog, Bidirectional Agentic Workflow][blog_bidirectional]
- [Blog, Context Engineering][blog_willison]
- [Blog, LLM Knowledge Graphs][blog_knowledge_graphs]
- [Blog, Markdown as a Specification Language for Agentic Workflows][blog_markdown_spec]
- [Blog, Year in Review 2025][blog_karpathy]
- [Claude Code, Manage Claude's Memory][cc_memory]
- [Industry, Advanced Context Engineering for Coding Agents][industry_humanlayer]
- [Industry, Context Engineering for AI Agents: Lessons from Building Manus][industry_manus]
- [Industry, Context Engineering for Coding Agents][industry_fowler_context]
- [Industry, Context Engineering: Bringing Engineering Discipline to Prompts][industry_osmani]
- [Industry, Fixing Claude Code's Amnesia][industry_episodic_memory]
- [Industry, LangChain Context Engineering for Agents][industry_langchain]
- [Industry, Personal AI Infrastructure][industry_miessler_pai]
- [Industry, Spotify Background Coding Agents Part 2: Context Engineering][industry_spotify_context]
- [Industry, The Context Window Problem][industry_factory_context]
- [Industry, Why AI Coding Agents Aren't Production-Ready][industry_venturebeat]
- [Protocol, AGENTS.md][protocol_agents_md]
- [Research, Agent READMEs: An Empirical Study of Context Files][research_agent_readmes]
- [Research, Context Engineering for AI Agents in Open-Source Software][research_oss_context]
- [Research, Context Engineering for Multi-Agent LLM Code Assistants][research_multi_agent]
- [Research, Decoding the Configuration of AI Coding Agents][research_santos_config]
- [Research, On the Impact of AGENTS.md Files on Efficiency][research_agents_md_impact]
- [Research, On the Use of Agentic Coding Manifests][research_agentic_manifests]
- [Standard, The /llms.txt File][standard_llms_txt]
- [Standard, ThoughtWorks Technology Radar: AGENTS.md][standard_thoughtworks_radar]
- [Tool, Set Up a Context Engineering Flow in VS Code][tool_vscode]

[anthropic_agent_skills]: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
[anthropic_context_engineering]: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
[anthropic_mcp]: https://www.anthropic.com/news/model-context-protocol
[anthropic_trends_report]: https://claude.com/blog/eight-trends-defining-how-software-gets-built-in-2026
[blog_bidirectional]: {% post_url 2026-02-06-bidirectional_agentic_workflow %}
[blog_karpathy]: https://karpathy.bearblog.dev/year-in-review-2025/
[blog_knowledge_graphs]: {% post_url 2026-02-07-llm_knowledge_graphs %}
[blog_markdown_spec]: {% post_url 2026-02-08-markdown_as_a_specification_language %}
[blog_willison]: https://simonwillison.net/2025/jun/27/context-engineering/
[cc_memory]: https://code.claude.com/docs/en/memory
[industry_episodic_memory]: https://blog.fsck.com/2025/10/23/episodic-memory/
[industry_factory_context]: https://factory.ai/news/context-window-problem
[industry_fowler_context]: https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
[industry_humanlayer]: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md
[industry_langchain]: https://blog.langchain.com/context-engineering-for-agents/
[industry_manus]: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
[industry_miessler_pai]: https://danielmiessler.com/blog/personal-ai-infrastructure
[industry_osmani]: https://addyo.substack.com/p/context-engineering-bringing-engineering
[industry_spotify_context]: https://engineering.atspotify.com/2025/11/context-engineering-background-coding-agents-part-2
[industry_venturebeat]: https://venturebeat.com/ai/why-ai-coding-agents-arent-production-ready-brittle-context-windows-broken
[protocol_agents_md]: https://agents.md/
[research_agent_readmes]: https://arxiv.org/abs/2511.12884
[research_agentic_manifests]: https://arxiv.org/abs/2509.14744
[research_agents_md_impact]: https://arxiv.org/abs/2601.20404
[research_multi_agent]: https://arxiv.org/abs/2508.08322
[research_oss_context]: https://arxiv.org/abs/2510.21413
[research_santos_config]: https://arxiv.org/abs/2511.09268
[standard_llms_txt]: https://llmstxt.org/
[standard_thoughtworks_radar]: https://www.thoughtworks.com/en-us/radar/techniques/agents-md
[tool_vscode]: https://code.visualstudio.com/docs/copilot/guides/context-engineering-guide
