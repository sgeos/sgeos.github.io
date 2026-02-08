---
layout: post
mathjax: false
comments: true
title: "Markdown as a Specification Language for Agentic Workflows"
date: 2026-02-07 00:00:00 +0000
categories: ai, ai-tools, development, developer-productivity
---

<!-- Axxx -->

"The hottest new programming language is English."
This claim, popularized by Andrej Karpathy in January 2023
and echoed by Jensen Huang and others,
captures a real shift in how software gets built.
AI coding agents can now accept natural language instructions
and produce working code.
But the conclusion that unstructured English is sufficient
as a specification language does not follow from this observation.

This article argues that markdown,
not freeform natural language,
is the practical specification language for AI-assisted development.
Markdown provides just enough structure to reduce ambiguity
while remaining readable by both humans and machines.
It is also language-agnostic,
meaning developers can write specifications in their native language
within a consistent structural framework.

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-07 00:00:00 +0000

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

## Instructions

### The Claim

The idea that natural language will replace programming languages
has a longer history than the current AI boom suggests.
Computer scientist Alan Perlis observed decades ago
that when someone says "I want a programming language in which I need only say what I wish done,"
the appropriate response is to "give him a lollipop."
COBOL was marketed on a similar promise in the 1960s.

The modern version of this claim gained traction in January 2023
when Andrej Karpathy tweeted that "the hottest new programming language is English."
The tweet was viewed nearly four million times.
Jensen Huang reinforced the message at the World Government Summit in February 2024,
stating that "the programming language is human"
and that it was "no longer necessary" to learn to code.
He repeated the theme at London Tech Week in June 2025.
Matt Welsh argued in Communications of the ACM
that "the conventional idea of 'writing a program' is headed for extinction"
and that most software would be "replaced by AI systems that are trained rather than programmed."

These statements contain a kernel of truth.
AI agents have made it possible for people without programming experience
to produce working software by describing what they want in plain language.
But the leap from "AI understands English" to "English is a good specification language"
conflates capability with suitability.

### The Problem with Unstructured English

A LessWrong analysis titled "English is a Terrible Programming Language"
identifies six properties that a good specification language should have.
It should be objective, explicit, unambiguous, relatively static, internally consistent, and robust.
English fails on every count.
It is subjective, implicit, ambiguous, constantly evolving, contradictory, and structurally inconsistent.

Consider a practical example.
A developer tells an AI agent in plain English to
"add a delete button to the user profile that asks for confirmation."
This instruction is ambiguous on several axes.
Where on the profile should the button appear?
What does "confirmation" mean?
A browser dialog, a modal, a separate page?
What happens after deletion?
What about error handling?
Authorization?

The developer might know the answers to all of these questions,
but by leaving them implicit,
they shift the burden of interpretation to the AI agent.
The agent will fill in the gaps with its own assumptions,
which may or may not match the developer's intent.
This is the same problem that requirements engineers
have faced with natural language specifications for decades.
AI does not solve the ambiguity problem.
It hides it.

Practitioners who use unstructured English prompts in agentic workflows
often describe a pattern of correction loops.
The agent produces something close to what was intended,
the developer adjusts with another English prompt,
the agent revises,
and the cycle continues.
This is sometimes called "vibe coding,"
a term coined by Andrej Karpathy in February 2025
to describe a workflow where the developer
"fully gives in to the vibes"
and lets the AI produce code based on informal descriptions.
Vibe coding works well for prototypes and disposable scripts.
It becomes unreliable for production systems
where correctness, reproducibility, and auditability matter.

### Markdown as the Middle Ground

Markdown occupies a useful position between unstructured prose
and formal specification languages.
It provides structural primitives that reduce ambiguity
without requiring the developer to learn a new language.

- **Headers** create hierarchy, organizing specifications into sections and subsections.
- **Lists** create enumeration, forcing the developer to break requirements into discrete items.
- **Code blocks** separate natural language from technical artifacts like commands, file paths, and configuration.
- **Tables** structure data into rows and columns, useful for parameter definitions and comparison matrices.
- **Bold and italic** markers draw attention to constraints and key terms.
- **Reference links** create traceability between claims and their sources.

These features are modest compared to a formal language,
but they impose just enough structure
to address the most common sources of ambiguity in natural language specifications.
The developer must organize their thoughts into sections.
Requirements must be itemized.
Technical details must be separated from prose descriptions.

Markdown is also the de facto standard for AI agent configuration files.
`CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `SKILL.md`,
and specification files used by GitHub Spec Kit, Amazon Kiro, and JetBrains Junie
are all markdown or markdown-adjacent formats.
This is not a coincidence.
Language model training data is heavily weighted toward markdown content from GitHub repositories,
documentation sites, and technical blogs.
Models have strong priors for interpreting markdown structure.

### Spec-Driven Development

The emergence of spec-driven development
formalizes the use of markdown as a specification language.
GitHub's Spec Kit, introduced in 2025,
places a markdown specification document at the center of the engineering process.
The spec drives implementation through four phases.

1. **Specify** the requirements in a markdown document.
2. **Plan** the implementation by generating a design document from the spec.
3. **Tasks** break the plan into discrete, verifiable work items.
4. **Implement** the code, guided by the spec and task list.

Thoughtworks identified spec-driven development as one of the key new engineering practices of 2025.
Red Hat and JetBrains published guides on integrating spec-driven workflows
with their respective AI coding tools.
Addy Osmani documented practical guidelines for writing specifications
that AI agents can reliably execute.

The key insight of spec-driven development
is that the specification is a living document.
It is updated as the developer and agent make decisions,
discover constraints, or change direction.
This is fundamentally different from the "write English, get code" model.
The specification is not a one-shot prompt.
It is an evolving contract between the human and the AI.

### The Native Language Advantage

A significant advantage of markdown over both unstructured English
and formal specification languages
is that markdown structure is language-agnostic.
The structural primitives of headers, lists, tables, and code blocks
work identically regardless of whether the prose is written in English, Japanese, German, or Portuguese.

This matters because the claim that "English is the new programming language"
implicitly marginalizes developers who are not native English speakers.
A developer in Tokyo or Sao Paulo can write markdown specifications
in their native language with the same structural benefits.
Modern language models understand dozens of languages.
The structure constrains ambiguity regardless of which human language fills the sections.

Consider a bilingual specification where the section headers and structural elements
are in the developer's working language,
while code blocks and technical identifiers remain in English
because the underlying programming ecosystem requires it.
Markdown accommodates this naturally.
Unstructured English does not.

### Format Comparison

Research on prompt formatting provides empirical support
for the value of structure.
A 2024 study found that GPT-3.5-turbo performance varied by up to 40%
depending on the prompt template used for a code translation task.
Markdown-style formatting outperformed both JSON and XML by 18% for creative tasks.
Larger models like GPT-4 were more robust to format variation,
but still performed measurably better with structured inputs.

The research also found that format preference is model-specific.
Claude performs better with structured formats like XML and markdown.
GPT models are more flexible but still benefit from consistent formatting.
The practical takeaway is that any consistent structure
outperforms unstructured prose for specification tasks.

| Format | Strengths | Weaknesses |
|--------|-----------|------------|
| Plain English | Maximum flexibility, no learning curve | Ambiguous, not version-controllable as structured data, no hierarchy |
| Markdown | Readable, structured, version-controllable, language-agnostic | Not formally verifiable, still allows ambiguity within sections |
| YAML/JSON | Machine-parseable, schema-validatable | Less human-readable, verbose for prose, poor for mixed content |
| Domain-Specific Languages | Maximum precision, formally verifiable | High barrier to entry, not readable by non-specialists |

### Pros and Cons

The case for markdown as a specification language is strong
but not without limitations.

**Advantages**

- **Structured enough to reduce ambiguity.** Headers, lists, and tables force the developer to organize their intent.
- **Readable by both humans and machines.** Markdown renders cleanly in editors, web browsers, and terminals. Language models parse it reliably.
- **Version-controllable.** Markdown files produce clean diffs in git, making specification changes auditable.
- **Language-agnostic.** Developers can write in their native language within a consistent structural framework.
- **Lightweight.** No tooling required beyond a text editor. No build step, no compilation, no runtime.
- **Ecosystem adoption.** `CLAUDE.md`, `AGENTS.md`, `SKILL.md`, and spec-driven development tools all use markdown.
- **Living document friendly.** Markdown files are easy to update incrementally as requirements evolve.

**Limitations**

- **Not formally verifiable.** Markdown provides structure but not a type system or grammar. It cannot catch logical contradictions in specifications.
- **Still subject to natural language ambiguity.** Within any given section, the prose remains natural language. Markdown reduces ambiguity at the structural level but does not eliminate it at the semantic level.
- **No enforcement mechanism.** Nothing prevents a developer from writing a poorly structured markdown file. The discipline must come from conventions and templates, not the format itself.
- **Learning curve for non-technical stakeholders.** While markdown is simpler than YAML or JSON, it is not universally known outside of technical communities.

### Context Engineering

Anthropic's research on context engineering
provides additional justification for structured markdown specifications.
As context windows grow, a phenomenon called "context rot" emerges.
Every token added to the context window competes for the model's attention.
Stuffing a hundred thousand tokens of unstructured history into the window
causes the model's ability to reason about what actually matters to degrade.

Structured markdown addresses context rot
by organizing information into scannable sections.
An AI agent processing a markdown specification
can navigate to the relevant section using headers
rather than scanning the entire document linearly.
The `CLAUDE.md` approach used by Claude Code
employs this principle explicitly.
Project-level instructions are structured in markdown
and dropped into context at session start,
while more detailed information is retrieved just-in-time
through file system navigation.

Anthropic's Agent Skills specification,
published as an open standard in December 2025,
extends this principle further.
Each skill is a folder with a `SKILL.md` file
containing YAML frontmatter and markdown instructions.
When a request matches a skill's domain,
the agent loads only the relevant skill.
Anthropic calls this "progressive disclosure,"
and it is fundamentally a strategy
for managing context through structured markdown documents.

## Conclusion

The claim that "English is the new programming language" is a useful provocation
but a poor specification strategy.
Unstructured natural language is ambiguous, implicit, and difficult to version control.
It works for casual interactions with AI assistants
but breaks down for multi-session projects
where correctness, reproducibility, and traceability matter.

Markdown is not a formal specification language.
It does not replace programming languages
any more than blueprints replace construction.
But it provides just enough structure
to bridge the gap between human intent and machine execution.
It is readable, version-controllable, language-agnostic, and already the de facto standard
for AI agent configuration and specification files.

The more precise claim is this.
The specification language for agentic workflows is structured markdown
in the developer's native language.
The structure reduces ambiguity.
The native language maximizes expressiveness.
The combination is more effective
than either unstructured English or a formal language alone.

## Future Reading

- [Spec-Driven Development with AI][github_spec_kit] by GitHub,
  which introduces specification-first development using markdown
  and documents the four-phase Specify, Plan, Tasks, Implement workflow.

- [How to Write a Good Spec for AI Agents][ai_good_spec] by Addy Osmani,
  with practical guidelines for writing specifications
  that AI coding agents can reliably execute.

- [Does Prompt Formatting Have Any Impact on LLM Performance?][research_prompt_formatting]
  by researchers at arxiv,
  providing empirical evidence on how structured formatting
  affects language model output quality.

- [English is a Terrible Programming Language][ai_english_terrible]
  on LessWrong,
  which analyzes the properties that a good specification language should have
  and explains why natural language falls short.

- [Effective Context Engineering for AI Agents][ai_context_engineering] by Anthropic,
  covering compaction, structured note-taking, and progressive disclosure
  for maintaining context in long-running agent sessions.

## References

- [AI, Agentic AI Course][ai_agentic_course]
- [AI, Effective Context Engineering for AI Agents][ai_context_engineering]
- [AI, English is a Terrible Programming Language][ai_english_terrible]
- [AI, How to Write a Good Spec for AI Agents][ai_good_spec]
- [AI, My LLM Coding Workflow Going into 2026][ai_llm_workflow]
- [AI, The End of Programming][ai_end_of_programming]
- [AI, The Hottest New Programming Language Is English][ai_karpathy_tweet]
- [Claude Code, Agent Skills Specification][cc_agent_skills]
- [Claude Code, Best Practices for Claude Code][cc_best_practices]
- [GitHub, Spec-Driven Development with AI: GitHub Spec Kit][github_spec_kit]
- [GitHub, Spec-Driven Development: Using Markdown as a Programming Language][github_sdd_markdown]
- [Industry, Jensen Huang: The New Programming Language Is Human][industry_huang_human]
- [Industry, Spec-Driven Development: Unpacking 2025's Key New Practices][industry_sdd_thoughtworks]
- [Protocol, AGENTS.md][protocol_agents_md]
- [Research, Does Prompt Formatting Have Any Impact on LLM Performance?][research_prompt_formatting]
- [Research, Quote Origin: The Hottest New Programming Language Is English][research_quote_investigator]

[ai_agentic_course]: https://www.deeplearning.ai/courses/agentic-ai/
[ai_context_engineering]: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
[ai_english_terrible]: https://www.lesswrong.com/posts/GidPzba7Qj8B5Guiw/english-is-a-terrible-programming-language-and-other-reasons
[ai_good_spec]: https://addyosmani.com/blog/good-spec/
[ai_llm_workflow]: https://addyosmani.com/blog/ai-coding-workflow/
[ai_end_of_programming]: https://m-cacm.acm.org/magazines/2023/1/267976-the-end-of-programming/fulltext
[ai_karpathy_tweet]: https://x.com/karpathy/status/1617979122625712128
[cc_agent_skills]: https://agentskills.io
[cc_best_practices]: https://code.claude.com/docs/en/best-practices
[github_spec_kit]: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
[github_sdd_markdown]: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-using-markdown-as-a-programming-language-when-building-with-ai/
[industry_huang_human]: https://dig.watch/updates/nvidias-huang-the-new-programming-language-is-human
[industry_sdd_thoughtworks]: https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices
[protocol_agents_md]: https://agents.md/
[research_prompt_formatting]: https://arxiv.org/html/2411.10541v1
[research_quote_investigator]: https://quoteinvestigator.com/2024/10/20/hottest-program/
