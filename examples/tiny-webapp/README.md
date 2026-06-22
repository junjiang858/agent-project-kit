# Tiny Web App Example

This example shows how Agent Project Kit turns a vague idea into staged artifacts before code.
The default completion target is not only "documents are ready"; it is the first MVP slice accepted after the engineering baseline is ready.

## Idea

Build a tiny web app where a user can save short reading notes and mark them as reviewed.

## Reference project scan

Before narrowing the MVP, scan a few concrete note-taking or reading-list products with direct project links. Use the scan to decide what to borrow, what to avoid, and which first workflow should become the first MVP slice.

## Capability library scan

Before confirming the tech stack, map the tiny notes workflow to project-needed third-party libraries. For this small MVP, validation and forms may be included if they reduce code risk, while rich text editing, full-text search, AI embeddings, sync engines, and analytics should usually be deferred unless the selected direction requires them. Each candidate should include a direct link, maintenance evidence, risk note, and Included / Deferred / Rejected decision.

## Stage Artifacts

1. Reference project scan: include direct project links such as Omnivore (https://github.com/omnivore-app/omnivore), Logseq (https://github.com/logseq/logseq), and Reor (https://github.com/reorproject/reor), then choose whether the app is a read-it-later tool, knowledge base companion, or local AI notes app.
2. Capability library scan: list project-needed third-party libraries with direct links, maintenance evidence, and Included / Deferred / Rejected decisions before confirming the tech stack.
3. `AGENTS.md`: define AI working rules and index the project documents.
4. `docs/project/PROJECT_CHARTER.md`: define user, MVP boundary, non-goals, and acceptance criteria.
5. `docs/architecture/TECH_STACK.md`: pick one Product MVP route, for example Next.js + TypeScript + Supabase/Postgres, plus the confirmed third-party library set.
6. `docs/architecture/ENGINEERING_BASELINE.md`: define scripts, lint/type/test/build checks, CI, env, and migration expectations.
7. `docs/architecture/FRONTEND_PLAN.md`: map pages, components, states, frontend source tree, file boundaries, and skeleton order.
8. `docs/architecture/DATABASE_DESIGN.md`: model `notes` with title, body, status, owner, and timestamps.
9. `docs/architecture/BACKEND_SPEC.md`: define create/list/update-review APIs or server actions.
10. `docs/ops/TOOL_POLICY.md`: allow local tests and browser checks; require confirmation for deployment.
11. `docs/workflow/AI_WORKFLOW.md`: define clarify, spec, implement, verify, and archive rules.
12. `docs/ops/DEPLOYMENT.md`: define local run, environment variables, deployment, health checks, and rollback.

## First MVP Slice

After the engineering baseline passes, the first MVP slice should be one narrow product loop:

1. User opens the notes page.
2. User creates a short reading note.
3. User sees the note in the list.
4. User marks the note as reviewed.
5. The agent returns build, browser, or API verification evidence for that flow.

## Example Prompt

```text
Use $agent-project-kit for this idea: I want a tiny app for saving reading notes and marking them reviewed. Do not write code yet. Guide me step by step and ask only one question at a time until docs/project/PROJECT_CHARTER.md is ready to draft.
Before deep requirement questions, scan concrete reference projects with direct project links and ask me to choose the direction.
Before confirming the tech stack, run a capability library scan and list Included / Deferred / Rejected third-party libraries.
```
