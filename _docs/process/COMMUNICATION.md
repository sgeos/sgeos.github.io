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
- `PROMPT.md` must always be committed to preserve collaboration history. The human pilot is responsible for committing prompt changes.

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
| Ax | Article number | A1 = first article using this system |
| Py | Prompt within article | P3 = third prompt |
| Tz | Task within prompt | T2 = second task |

The article number is a monotonically increasing identifier. It does not reset. Each article corresponds to a blog post or a documentation effort.

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
