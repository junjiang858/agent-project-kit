# Engineering Rules

Use this reference for project-level Agent rules, AGENTS.md, reusable skill design, and long-running AI collaboration discipline.

## Agent Constitution

The Agent constitution governs stable project-level behavior. Keep it short, actionable, and easy for AI to re-read before work.

Include:

- Project goal and current product boundary.
- Chosen technical route and forbidden drift.
- Code quality rules and completion definition.
- Test, build, and verification requirements.
- Git checkpoint and commit policy.
- Tool permission principles, with details delegated to `TOOL_POLICY.md`.
- Forbidden actions: secrets in code, destructive commands, production mutation without confirmation, broad rewrites without approval.
- Conflict order: user instruction, project docs, Agent constitution, skill/reference instructions, local code conventions.

Avoid:

- Long tutorials.
- Every possible style preference.
- Tool permission matrices that belong in `TOOL_POLICY.md`.
- Task-specific workflows that belong in separate skills.

## Skill Workflow

Use skills for repeated, fragile, or expert workflows. A good skill has:

- Trigger conditions.
- Required inputs and upstream artifacts.
- Procedure.
- Output format.
- Verification method.
- Common failure modes.
- Optional scripts, templates, or references.

Start small. Convert repeated project pain into one concise skill, then revise it after real use.

## Completion Definition

A task is not complete until the agent can show evidence appropriate to the work:

- Docs: updated file path and summary of changed decisions.
- Frontend: build, type/lint checks, browser screenshot or interaction check when applicable.
- Backend: test command, health check, API sample, logs free of sensitive data.
- Database: migration or schema diff, relationship explanation, rollback note.
- Security: risk table, affected files, verification method, normal and forbidden path evidence.

## Prompt: Agent Constitution

```text
Based on the project charter, technical route, and collaboration rules, draft a concise Agent constitution. Include project goal, development boundaries, quality standards, testing requirements, commit policy, tool permission principles, forbidden actions, completion definition, and conflict handling. Reference TOOL_POLICY.md for detailed tool permissions instead of embedding the full matrix.
```

## Prompt: Skill Draft

```text
Turn this repeated project task into a reusable skill draft. Include use cases, triggers, required inputs, execution steps, output format, verification checklist, common failure modes, and iteration notes.
```
