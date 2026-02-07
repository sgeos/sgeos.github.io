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

- `PROMPT.md` must always be committed to preserve collaboration history.
- The AI agent reads and executes the current prompt, then commits it.

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

## Task Completion Protocol

1. Update `TASKLOG.md` task status.
2. Update `REVERSE_PROMPT.md` with verification and summary.
3. Commit changes.
4. Proceed to next task or stop if blocked.

## Blocking Protocol

If the AI agent cannot proceed due to missing information, ambiguity, or a technical obstacle, it must follow this protocol.

1. Document the blocker in `REVERSE_PROMPT.md` under Questions or Technical Concerns.
2. Update `TASKLOG.md` status to "Blocked."
3. Commit changes.
4. Stop and wait for human direction.
