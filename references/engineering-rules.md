# Engineering Rules

Use this reference for project-level Agent rules, AGENTS.md, reusable skill design, and long-running AI collaboration discipline.

## Agent Constitution

The Agent constitution governs stable project-level behavior. Keep it short, actionable, and easy for AI to re-read before work.

Include:

- Project goal and current product boundary.
- Chosen technical route from `docs/architecture/TECH_STACK.md` and forbidden drift.
- Code quality rules and completion definition.
- Test, build, and verification requirements.
- Git checkpoint and commit policy.
- Tool permission principles, with details delegated to `docs/ops/TOOL_POLICY.md`.
- Forbidden actions: secrets in code, destructive commands, production mutation without confirmation, broad rewrites without approval.
- Conflict order: user instruction, project docs, Agent constitution, skill/reference instructions, local code conventions.
- Source-of-truth change gate: when design or contracts change, update the original project document before implementation.
- Source-of-truth distillation: keep current-state docs compact; place stable feature behavior in `docs/features/`, one-change detail in `docs/changes/`, long-term decisions in `docs/decisions/`, and Agent Project Kit process artifacts in `docs/agent-project-kit/`.
- Optional workflow tool fallback: Superpowers, OpenSpec, GitHub Spec Kit, and similar tools are accelerators; when unavailable, use the repository's documented clarify, plan, implement, verify, and evidence workflow instead of blocking.

Avoid:

- Long tutorials.
- Every possible style preference.
- Tool permission matrices that belong in `docs/ops/TOOL_POLICY.md`.
- Task-specific workflows that belong in separate skills.
- Full change journals, task logs, or acceptance transcripts that belong in `docs/changes/`.

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

When a task changes frontend design, API/backend contracts, database shape, permissions, deployment, tools, or operations, the first evidence must be the updated source-of-truth document path and summary. Code evidence comes after that.

## Prompt: Agent Constitution

```text
Based on the project charter, technical route, and collaboration rules, draft a concise root AGENTS.md. Include project goal, development boundaries, quality standards, testing requirements, commit policy, tool permission principles, forbidden actions, completion definition, conflict handling, optional workflow tool fallback, and source-of-truth distillation. Index docs/project/PROJECT_CHARTER.md, docs/architecture/TECH_STACK.md, docs/architecture/ENGINEERING_BASELINE.md, docs/workflow/AI_WORKFLOW.md, docs/ops/TOOL_POLICY.md, docs/features/, docs/changes/, docs/decisions/, and docs/agent-project-kit/. Reference docs/ops/TOOL_POLICY.md for detailed tool permissions instead of embedding the full matrix.
```

## Prompt: Skill Draft

```text
Turn this repeated project task into a reusable skill draft. Include use cases, triggers, required inputs, execution steps, output format, verification checklist, common failure modes, and iteration notes.
```
