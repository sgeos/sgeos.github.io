---
layout: post
mathjax: false
comments: true
title: "Bidirectional Agentic Workflow"
date: 2026-02-07 17:00:18 +0000
categories: ai, ai-tools, development, developer-productivity, tutorial
---

<!-- A75 -->

The rise of agentic AI systems has introduced a new challenge for software development teams.
These systems can plan, execute, and iterate on code autonomously,
but the question of how to structure collaboration between a human developer and an AI agent remains largely unsolved.
Most workflows today are either fully autonomous, where the agent works without checkpoints,
or fully interactive, where the developer guides every step in real time.

This post documents a bidirectional communication protocol
that sits between those two extremes.
It was developed through practical use on a mission-critical application,
and ported to this Jekyll blog.
This protocol is designed to maintain shared context across sessions,
enforce verification at task boundaries,
and preserve a complete audit trail in version control.
This article itself was drafted using the protocol it describes.

## Software Versions

```sh
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-02-07 17:00:18 +0000

$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64

$ sw_vers
ProductName:		macOS
ProductVersion:		14.6.1
BuildVersion:		23G93

$ git --version
git version 2.52.0

$ jekyll --version
jekyll 4.2.2
```

## Instructions

### The Problem

AI coding agents are powerful but stateless.
Each new session starts with a blank context window.
The agent does not remember what it did yesterday,
what decisions were made, or what questions remain unanswered.
Developers compensate by re-explaining context,
re-stating constraints, and re-describing the project state at the start of every session.

This problem compounds in multi-session projects.
Without a protocol, critical decisions live only in chat transcripts that are difficult to search,
impossible to version control, and invisible to future sessions.
The developer becomes the sole keeper of project state,
which defeats the purpose of delegating work to an agent.

### The Bidirectional Protocol

The protocol uses three markdown files committed to the project repository.
Together, they form a structured communication channel
that persists across sessions and is visible to both the human developer and the AI agent.

| Document | Direction | Purpose |
|----------|-----------|---------|
| `PROMPT.md` | Human to AI | Staging area for complex instructions |
| `REVERSE_PROMPT.md` | AI to Human | Status reports, questions, and concerns |
| `TASKLOG.md` | Shared | Current task state and verification log |

These files live in a `docs/process/` directory within the repository.
The complete protocol documentation, including templates and conventions,
is available in the [reference implementation][github_blog_repo] used for this blog.
Note that the fine structure of the documentation may evolve,
but the top-level files including `docs/README.md` should remain present.

### Forward Prompt: Human to AI

`PROMPT.md` is a staging area where the human developer drafts complex, multi-step instructions
before executing them.
The file has a consistent structure.

- **Comments**: Status notes and context for the AI agent.
- **Objectives**: Numbered, hierarchical task descriptions.
- **Context**: Background information relevant to the objectives.
- **Constraints**: Boundaries on what the AI agent should and should not do.
- **Success Criteria**: Verifiable conditions that define task completion.
- **Notes**: Supplementary information.

The developer writes the prompt, commits it, and then instructs the agent to execute it.
This approach has two advantages over inline chat prompts.
First, the prompt is version controlled, creating a complete history of human-to-AI instructions.
Second, the structured format reduces ambiguity by forcing the developer to specify constraints and success criteria before execution begins.

The AI agent treats `PROMPT.md` as read-only.
It never modifies the file.
It does, however, commit the file alongside its own changes
so that the human prompt and AI response remain in sync in version control history.

### Reverse Prompt: AI to Human

`REVERSE_PROMPT.md` is the AI-to-human communication channel.
The AI agent overwrites this file after completing each prompted task.
The file has a fixed structure.

- **Last Updated**: Date and task identifier.
- **Verification**: Commands run and their results.
- **Implementation Summary**: What was done and why.
- **Questions for Human Pilot**: Numbered questions requiring decisions.
- **Technical Concerns / Risks**: Flagged issues or risks.
- **Intended Next Step**: What the agent would do next, pending human direction.
- **Session Context**: Orientation notes for a new AI session reading the file.

The "Session Context" section is particularly important.
It provides a new AI session with enough context to continue work
without the human developer needing to re-explain the project state.
A new session reads `TASKLOG.md` and `REVERSE_PROMPT.md` before proceeding.

### Task Log: Shared State

`TASKLOG.md` is the shared source of truth for the current unit of work.
It tracks task status, success criteria, and a verification log.
Every task marked "Complete" must have a corresponding verification entry
documenting the command run and its result.

### The Blocking Protocol

A critical rule in the protocol is the blocking protocol.
If the AI agent encounters ambiguity, missing information,
or a technical obstacle, it must not proceed with assumptions.
Instead, it documents the blocker in `REVERSE_PROMPT.md`,
updates `TASKLOG.md` to "Blocked," commits the current state, and stops.
This prevents the agent from making incorrect assumptions
and propagating errors through subsequent tasks.

### Session Startup

Every AI session follows the same startup sequence.

1. Read `TASKLOG.md` for current task state.
2. Read `REVERSE_PROMPT.md` for last AI communication.
3. Wait for human prompt before proceeding.

This ensures the agent has context before acting
and that the human developer retains control of task initiation.

### Work Item Traceability

The protocol includes a coding system for work items.
Each task is identified using an `Ax-Py-Tz` code,
where `A` is the article number, `P` is the prompt number within that article,
and `T` is the task number within that prompt.
These codes appear in `TASKLOG.md` entries and in git commit messages,
creating a traceable link between prompts, tasks, and code changes.

### Supporting Infrastructure

The protocol is supported by two additional conventions.

**Scoped conventional commits** use the format `<scope>: <imperative summary>`
with a co-author attribution for AI-assisted work.
The AI agent commits once after all tasks in a prompt are complete,
including the `REVERSE_PROMPT.md` update.

**A documentation knowledge graph** in `docs/` provides
persistent reference material that the AI agent can consult.
This includes style guides, architecture documentation, and the protocol specification itself.
The knowledge graph uses atomic files (one concept per file)
with breadcrumb navigation to allow AI agents to load only the context they need.

### Workflow Diagram

The following diagram illustrates the complete workflow cycle.

```
Human                              AI Agent
  │                                   │
  ├─ Draft PROMPT.md ──────────────>  │
  │                                   │
  ├─ "Execute PROMPT.md" ──────────>  │
  │                                   ├─ Read TASKLOG.md
  │                                   ├─ Read REVERSE_PROMPT.md
  │                                   ├─ Read PROMPT.md
  │                                   ├─ Execute tasks
  │                                   ├─ Update TASKLOG.md
  │                                   ├─ Update REVERSE_PROMPT.md
  │                                   ├─ Commit all changes
  │                                   │
  │  <──────── REVERSE_PROMPT.md ─────┤
  │                                   │
  ├─ Review questions/concerns        │
  ├─ Draft next PROMPT.md ─────────>  │
  │                                   │
  └─ (repeat) ────────────────────>   │
```

### COMMUNICATION.md

The `COMMUNICATION.md` file for this project is listed below.
You may need to tweak some of the details for your exact workflow.
For example, the mission critical application that this bidirectional
workflow was developed for used `Vw-Mx-Py-Tz` coding,
where V is the version, and M is the milestone.

**`docs/process/COMMUNICATION.md` complete listing**
````
# Bidirectional Communication Protocol

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Protocol for structured communication between the human pilot and AI agent across sessions.

## Overview

Three working documents maintain state across AI sessions and enable asynchronous collaboration.

| Document | Direction | Persistence |
|----------|-----------|-------------|
| [PROMPT.md](./PROMPT.md) | Human to AI | Committed to preserve prompt history |
| [REVERSE_PROMPT.md](./REVERSE_PROMPT.md) | AI to Human | Overwritten after each completed task |
| [TASKLOG.md](./TASKLOG.md) | Shared | Updated incrementally as tasks complete |

## Forward Prompt (Human to AI)

`PROMPT.md` is a staging area for complex, multi-step instructions. The human pilot drafts and refines prompts here before execution.

### Structure

- **Comments**: Status notes and context for the AI agent.
- **Objectives**: Numbered, hierarchical task descriptions.
- **Context**: Background information relevant to the objectives.
- **Constraints**: Boundaries on what the AI agent should and should not do.
- **Success Criteria**: Verifiable conditions that define task completion.
- **Notes**: Supplementary information.

### Rules

- `PROMPT.md` is **read-only for the AI agent**. The AI agent must never modify this file. Only the human pilot writes to `PROMPT.md`.
- The AI agent must commit `PROMPT.md` along with other changes if it has been modified by the human pilot. This keeps the human prompt and AI reverse prompt in sync with committed work.

## Reverse Prompt (AI to Human)

`REVERSE_PROMPT.md` is the AI-to-human communication channel. The AI agent overwrites this file after completing each task.

### Structure

- **Last Updated**: Date, task identifier, and parent milestone.
- **Verification**: Commands run and their results, one per completed task.
- **Summary**: Implementation summary and status.
- **Questions for Human Pilot**: Numbered questions requiring human decisions.
- **Technical Concerns / Risks**: Flagged issues or risks.
- **Intended Next Step**: What the AI agent would do next, pending human direction.
- **Session Context**: Orientation notes for a new AI session reading the file.

### Rules

- If blocked or uncertain, document the blocker in `REVERSE_PROMPT.md` and stop. Do not proceed with assumptions.
- Every completed task must have a verification command and result documented.

## Task Log

`TASKLOG.md` is the shared source of truth for the current unit of work.

### Structure

- **Task Name and Status**: Descriptive name with status indicator (In-Progress, Blocked, Complete).
- **Success Criteria**: Checkbox list of verifiable completion conditions.
- **Task Breakdown**: Table with task ID, description, status, and verification method.
- **Notes**: Additional context or decisions.
- **History**: Date-based change log.

### Rules

- Update task status as work progresses.
- Every task marked "Complete" must have a corresponding verification entry.
- If blocked, update status to "Blocked" and document the blocker.

## Session Startup Protocol

1. Read `TASKLOG.md` for current task state.
2. Read `REVERSE_PROMPT.md` for last AI communication.
3. Wait for human prompt before proceeding.

## Work Item Coding System

All work items use the **Ax-Py-Tz** coding system for traceability across articles, prompts, and tasks.

### Format

`Ax-Py-Tz`

| Component | Meaning | Example |
|-----------|---------|---------|
| Ax | Article number | A0 = non-article work, A1 = first published article |
| Py | Prompt within article | P3 = third prompt |
| Tz | Task within prompt | T2 = second task |

The article number is a monotonically increasing identifier. It does not reset. Each article corresponds to a blog post. A0 is reserved for non-article work such as documentation, process, and infrastructure changes.

### Usage

- **TASKLOG.md**: Tasks use Ax-Py-Tz codes in the ID column.
- **Git commits**: Reference task codes in the commit body using `[Task: Ax-Py-Tz]`.
- **Blog posts**: Every future post should include an invisible HTML comment with its article number immediately after the front matter closing `---`. Example: `<!-- A5 -->`.

### Examples

- `A3-P1-T2` = Article 3, Prompt 1, Task 2
- `A7-P2` = Article 7, Prompt 2 (no specific task)
- `A0-P2-T1` = Article 0 (documentation), Prompt 2, Task 1

## Task Completion Protocol

1. Complete all implementation tasks.
2. Update `TASKLOG.md` task status.
3. Update `REVERSE_PROMPT.md` with verification and summary.
4. Commit all changes in a single commit. The commit happens after all tasks including the `REVERSE_PROMPT.md` update are complete.
5. Proceed to next prompt or stop if blocked.

## Blocking Protocol

If the AI agent cannot proceed due to missing information, ambiguity, or a technical obstacle, it must follow this protocol.

1. Document the blocker in `REVERSE_PROMPT.md` under Questions or Technical Concerns.
2. Update `TASKLOG.md` status to "Blocked."
3. Commit changes.
4. Stop and wait for human direction.
````

## Comparison with Other Approaches

The landscape of human-AI development workflows has diversified rapidly.
The following comparison situates the bidirectional protocol
relative to other established approaches.

### Fully Autonomous Agents

Tools like Devin and OpenAI Codex (background mode) operate with minimal human intervention.
The agent receives a task, works autonomously through a code-run-test-fix loop,
and delivers a pull request when finished.
This approach maximizes throughput
but introduces risks around silent failures, technical debt accumulation,
and a gap between what the agent produced and what the developer expected.
Cognition (the company behind Devin) reports that roughly 10-20% of autonomous sessions
are abandoned because the result diverges from intent.

The bidirectional protocol addresses this by introducing structured checkpoints
at prompt boundaries.
The agent works autonomously within a single prompt
but must report back before proceeding to the next unit of work.

### Inline Pair Programming

Tools like GitHub Copilot (inline suggestions) and Cursor (chat-based editing)
operate in a tight interactive loop.
The developer guides each step in real time, reviewing suggestions line by line.
This approach maintains high control
but limits the agent's ability to work on larger tasks independently.
It also produces no persistent record of the collaboration beyond the code diff itself.

The bidirectional protocol operates at a coarser granularity than inline pair programming.
The human developer defines objectives and constraints in `PROMPT.md`,
then steps back while the agent executes.
This frees the developer from moment-to-moment supervision
while retaining oversight through the reverse prompt.

### Spec-Driven Development

GitHub's Spec Kit places a specification document at the center of the engineering process.
The spec drives implementation, checklists, and task breakdowns
through four phases: Specify, Plan, Tasks, and Implement.
This is structurally similar to the bidirectional protocol
in that both use versioned documents as shared contracts between human and AI.

The key difference is scope.
Spec-Driven Development targets the full software development lifecycle,
while the bidirectional protocol focuses specifically on session-to-session communication
and task verification.
The two approaches could be combined,
using specs for high-level planning and the bidirectional protocol for execution.

### The Breadcrumb Protocol

The Breadcrumb Protocol, documented by Dasith Wijesiriwardena,
uses "breadcrumb files" as collaborative scratch pads
stored in `.github/.copilot/breadcrumbs/`.
Each breadcrumb includes sections for requirements, plans, decisions, and implementation details.
The protocol includes explicit approval gates before implementation begins.

The Breadcrumb Protocol and the bidirectional protocol share the insight
that structured files committed to version control
are more durable than chat transcripts.
The Breadcrumb Protocol focuses on maintaining context within a single task,
while the bidirectional protocol emphasizes continuity across multiple sessions
through the `REVERSE_PROMPT.md` session context section and the task log.

### CLAUDE.md and AGENTS.md

Project-level instruction files like `CLAUDE.md`, `.cursorrules`, and the emerging `AGENTS.md` standard
provide persistent context to AI agents about project conventions, build commands, and architectural patterns.
Over 20,000 GitHub repositories have adopted `AGENTS.md` since its introduction in July 2025.

These files serve a complementary function to the bidirectional protocol.
`CLAUDE.md` provides static project knowledge.
The bidirectional protocol provides dynamic session state.
The two are most effective when used together.
In the reference implementation, `CLAUDE.md` references the knowledge graph
and includes a session startup protocol
that directs the agent to read `TASKLOG.md` and `REVERSE_PROMPT.md`.

### Bounded Autonomy

The emerging consensus across the industry is what some practitioners call "bounded autonomy"
or risk-based autonomy.
Rather than choosing between full autonomy and full human control,
successful deployments implement tiered approaches.
Low-risk, repeatable tasks receive full automation.
High-impact decisions require human checkpoints.

The bidirectional protocol implements bounded autonomy at the prompt level.
Within a single prompt, the agent operates autonomously.
Between prompts, the human developer reviews, decides, and redirects.
The blocking protocol ensures that the agent escalates uncertainty
rather than proceeding with assumptions.

## Summary

The bidirectional agentic workflow addresses a gap
between fully autonomous agents and interactive pair programming.
By committing structured communication files to version control,
the protocol preserves context across sessions,
enforces verification at task boundaries,
and maintains an audit trail of human-AI collaboration.

The core components are `PROMPT.md` (human to AI), `REVERSE_PROMPT.md` (AI to human),
and `TASKLOG.md` (shared state).
These files are lightweight to maintain
and compatible with any AI coding agent that can read and write files.
The protocol does not depend on any specific tool or platform.

The approach is most valuable for multi-session projects
where continuity and traceability matter more than raw speed.
For quick, single-session tasks, inline pair programming remains more efficient.
For large-scale automated pipelines, fully autonomous agents may be more appropriate.
The bidirectional protocol occupies the middle ground:
structured enough to prevent drift, lightweight enough to avoid ceremony.

## Future Reading

- [Effective Context Engineering for AI Agents][ai_context_engineering] by Anthropic,
  which covers compaction, structured note-taking, and multi-agent architectures
  for maintaining context in long-running agent sessions.

- [Spec-Driven Development with AI][github_spec_kit] by GitHub,
  introducing a specification-first approach
  that complements the bidirectional protocol at the planning level.

- [Coding Agents 101][devin_agents_101] by Cognition (Devin),
  which covers practical patterns for working with autonomous coding agents
  including the inner loop/outer loop distinction.

- [Andrew Ng's Agentic AI Course][ai_agentic_course] on DeepLearning.AI,
  covering the four foundational agentic design patterns:
  reflection, tool use, planning, and multi-agent collaboration.

- [AGENTS.md][protocol_agents_md],
  an emerging open standard for portable AI coding agent instructions
  adopted by over 20,000 repositories.

## References

- [AI, Agentic AI Course][ai_agentic_course]
- [AI, Effective Context Engineering for AI Agents][ai_context_engineering]
- [AI, Human-in-the-Loop vs Autonomous Development for Enterprise Software][ai_hitl_vs_auto]
- [AI, My LLM Coding Workflow Going into 2026][ai_llm_workflow]
- [Aider, AI Pair Programming in Your Terminal][aider_pair_programming]
- [Claude Code, Best Practices for Claude Code][cc_best_practices]
- [Claude Code, Common Workflows: Claude Code Documentation][cc_common_workflows]
- [Claude Code, Eight Trends Defining How Software Gets Built in 2026][cc_eight_trends]
- [Claude Code, Inside the Development Workflow of Claude Code's Creator][cc_creator_workflow]
- [Claude Code, Understanding Claude Code Plan Mode and the Architecture of Intent][cc_plan_mode]
- [Devin, Coding Agents 101: The Art of Actually Getting Things Done][devin_agents_101]
- [GitHub, Bidirectional Agentic Workflow Reference Implementation][github_blog_repo]
- [GitHub, Spec-Driven Development with AI: GitHub Spec Kit][github_spec_kit]
- [Protocol, AGENTS.md][protocol_agents_md]
- [Protocol, AGENTS.md: A New Standard for Unified Coding Agent Instructions][protocol_agents_md_article]
- [Protocol, Agent Client Protocol][protocol_acp]
- [Protocol, From Prompts to AGENTS.md: What Survives Across Thousands of Runs][protocol_agents_md_tessl]
- [Protocol, Structured Workflows for Coding with AI Agents Using the Breadcrumb Protocol][protocol_breadcrumb]
- [Research, ICLR 2025 Workshop on Bidirectional Human-AI Alignment][research_iclr_bidirectional]
- [Research, SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering][research_swe_agent]

[ai_agentic_course]: https://www.deeplearning.ai/courses/agentic-ai/
[ai_context_engineering]: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
[ai_hitl_vs_auto]: https://securityboulevard.com/2026/01/human-in-the-loop-vs-autonomous-development-for-enterprise-software/
[ai_llm_workflow]: https://addyosmani.com/blog/ai-coding-workflow/
[aider_pair_programming]: https://aider.chat/
[cc_best_practices]: https://code.claude.com/docs/en/best-practices
[cc_common_workflows]: https://code.claude.com/docs/en/common-workflows
[cc_eight_trends]: https://claude.com/blog/eight-trends-defining-how-software-gets-built-in-2026
[cc_creator_workflow]: https://www.infoq.com/news/2026/01/claude-code-creator-workflow/
[cc_plan_mode]: https://lord.technology/2025/07/03/understanding-claude-code-plan-mode-and-the-architecture-of-intent.html
[devin_agents_101]: https://devin.ai/agents101
[github_blog_repo]: https://github.com/sgeos/sgeos.github.io
[github_spec_kit]: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
[protocol_agents_md]: https://agents.md/
[protocol_agents_md_article]: https://addozhang.medium.com/agents-md-a-new-standard-for-unified-coding-agent-instructions-0635fc5cb759
[protocol_acp]: https://zed.dev/acp
[protocol_agents_md_tessl]: https://tessl.io/blog/from-prompts-to-agents-md-what-survives-across-thousands-of-runs/
[protocol_breadcrumb]: https://dasith.me/2025/04/02/vibe-coding-breadcrumbs/
[research_iclr_bidirectional]: https://arxiv.org/pdf/2409.08622
[research_swe_agent]: https://arxiv.org/abs/2405.15793
