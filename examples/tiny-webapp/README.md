# Tiny Web App Example

This example shows how Agent Project Kit turns a vague idea into staged artifacts before code.

## Idea

Build a tiny web app where a user can save short reading notes and mark them as reviewed.

## Stage Artifacts

1. `PROJECT_CHARTER.md`: define user, MVP boundary, non-goals, and acceptance criteria.
2. `TECH_STACK.md`: pick one route, for example Next.js + TypeScript + SQLite for local prototype.
3. `AGENTS.md`: define AI working rules and completion evidence.
4. `DATABASE_DESIGN.md`: model `notes` with title, body, status, and timestamps.
5. `BACKEND_SPEC.md`: define create/list/update-review APIs or server actions.
6. `TOOL_POLICY.md`: allow local tests and browser checks; require confirmation for deployment.

## Example Prompt

```text
Use $agent-project-kit for this idea: I want a tiny app for saving reading notes and marking them reviewed. Do not write code yet. Start with the project charter and ask only the questions needed to define the MVP.
```
