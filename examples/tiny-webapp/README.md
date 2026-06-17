# Tiny Web App Example

This example shows how Agent Project Kit turns a vague idea into staged artifacts before code.

## Idea

Build a tiny web app where a user can save short reading notes and mark them as reviewed.

## Stage Artifacts

1. `AGENTS.md`: define AI working rules and index the project documents.
2. `docs/project/PROJECT_CHARTER.md`: define user, MVP boundary, non-goals, and acceptance criteria.
3. `docs/architecture/TECH_STACK.md`: pick one Product MVP route, for example Next.js + TypeScript + Supabase/Postgres.
4. `docs/architecture/ENGINEERING_BASELINE.md`: define scripts, lint/type/test/build checks, CI, env, and migration expectations.
5. `docs/architecture/FRONTEND_PLAN.md`: map pages, components, states, and skeleton order.
6. `docs/architecture/DATABASE_DESIGN.md`: model `notes` with title, body, status, owner, and timestamps.
7. `docs/architecture/BACKEND_SPEC.md`: define create/list/update-review APIs or server actions.
8. `docs/ops/TOOL_POLICY.md`: allow local tests and browser checks; require confirmation for deployment.

## Example Prompt

```text
Use $agent-project-kit for this idea: I want a tiny app for saving reading notes and marking them reviewed. Do not write code yet. Guide me step by step and ask only one question at a time until docs/project/PROJECT_CHARTER.md is ready to draft.
```
