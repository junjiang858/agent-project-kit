---
name: agent-project-kit
description: Use when starting or governing AI-assisted software projects, especially project baseline setup, source-of-truth documents, architecture or contract changes, implementation readiness, tool permissions, security or deployment boundaries, or routing bounded feature work.
---

# Agent Project Kit

## Overview

Guide AI-assisted software projects through staged clarification, source-of-truth documents, implementation boundaries, and evidence-based acceptance. Use this skill as the project router before implementation discipline takes over.

## Core Rule

Do not jump from a vague idea to documents, technology choices, scaffolding, or implementation. First classify the current stage, read only the matching reference, clarify the minimum missing facts, and ask for explicit consent before creating or updating project source-of-truth documents or doing irreversible or high-risk work.

Never create application scaffolding, UI pages, API skeletons, database schemas, package manager files, implementation directories, or runnable product behavior until the Project Specification Readiness Gate passes or the user explicitly confirms a narrow bootstrap-only exception.

## Default Workflow Priority

When this skill is loaded or the user request matches AI-assisted project initiation, project baseline setup, source-of-truth documents, architecture or contract changes, implementation readiness, tool permissions, security boundaries, deployment boundaries, or bounded-feature routing, Agent Project Kit is the default primary workflow.

Use overlapping skills, including Superpowers, OpenSpec, GitHub Spec Kit, issue trackers, review skills, TDD skills, security skills, and deployment skills, only as auxiliary method libraries after this skill classifies the project path and protects the source-of-truth gates.

If an overlapping workflow tool is unavailable, use the Optional Workflow Tool Fallback in `references/workflow-checklists.md` instead of blocking or asking the user to install tools they did not request.

Skip this priority only when the user explicitly names another workflow as primary, or when the task is a Local Fix Path such as a small code explanation, copy tweak, single command, or isolated test fix that does not change product or engineering contracts.

## Global Interaction Rules

### Confirmation Prompt Rule

Any request for confirmation, consent, approval, or a path choice must include plain-text options in the assistant message. Do not depend on UI buttons, host quick actions, or tool-only prompts.

### User Language Rule

Use the user's current language for questions, confirmations, progress updates, final answers, and milestone messages unless the user requests another language. Preserve the same operational meaning in the user's current language.

## Goal Contract

At the start of every project-level run, state the Goal Contract in one sentence:

- Target outcome: the stage outcome or project state the user is trying to reach.
- Completion signal: the artifacts, confirmations, audits, or evidence that prove the outcome is reached.
- Next action: the single next question, document, audit, or implementation step.

For a new Product MVP, the default target is first MVP slice accepted after the project engineering baseline is ready. The two early milestones are project engineering baseline ready and First MVP slice accepted with evidence.

After the first slice, use explicit lifecycle states from `references/mvp-closure.md`: `MVP Scope Incomplete`, `Full MVP Scope Complete`, and `Release Ready`. When `Full MVP Scope Complete` is reached, switch to Formal Product Development Mode.

Do not declare a milestone complete just because a document was written. Completion requires the relevant gate, confirmation, implementation evidence, or closure audit described in `references/workflow-checklists.md` and `references/mvp-closure.md`.

## Path Router

Use the lightest path that protects the project:

| Path                           | Use when                                                                                                                                                                                     | Minimum behavior                                                                                                        |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Project Baseline Path          | New project, project reorganization, missing core documents, technology stack choice, engineering baseline, security, tool, or deployment boundary setup.                                    | Run staged clarification, reference scan, capability scan, document consent, and readiness gates before implementation. |
| Contract-Changing Feature Path | A feature or fix changes product behavior, routes, UI states, component responsibilities, API contracts, data shape, permissions, dependencies, deployment, tool permissions, or operations. | Run the Contract Impact Check, update affected source-of-truth documents first, then implement.                         |
| Bounded Feature Path           | Baseline exists and the work stays inside approved source-of-truth contracts.                                                                                                                | Read relevant docs, state no source-of-truth update is needed, then use the Implementation Handoff.                     |
| Local Fix Path                 | Small bug fix, copy/style tweak, test fix, code explanation, single command, or local task that does not change product or engineering contracts.                                            | Skip the project baseline flow and use the lightest direct engineering method.                                          |

Before treating work as bounded, run the Contract Impact Check from `references/workflow-checklists.md`.

## Core Gates

Keep the gate names in working memory, then read the routed reference for details:

- Reference Project Scan Gate: for vague or early product ideas before requirements, Project Purpose Confirmation, stack choice, or charter drafting. See `references/project-initiation.md`.
- Requirements Depth Gate: before asking to write `docs/project/PROJECT_CHARTER.md`. See `references/project-initiation.md`.
- Project Purpose Confirmation: before technology stack, frontend, backend, database, or implementation planning. See `references/project-initiation.md`.
- Capability Library Scan Gate: before technology stack confirmation, dependency installation, package manager edits, scaffolding, or implementation. Treat default stack recommendations as context-aware candidates. See `references/architecture-baseline.md`.
- Document Consent Gate: before creating, copying, overwriting, moving, or editing `AGENTS.md`, files under `docs/`, or other source-of-truth documents. See `references/workflow-checklists.md`.
- Project Specification Readiness Gate: before any scaffold, package manager file, UI/API/database code, migration, local dev server, or runnable behavior. See `references/workflow-checklists.md`.
- Source-of-Truth Change Gate: before implementation that changes product design, contracts, data shape, permissions, dependencies, tools, deployment, or operations. See `references/workflow-checklists.md`.
- Source-of-Truth Distillation Gate: when detail would bloat current-state docs; route stable feature behavior to `docs/features/`, one-change detail to `docs/changes/`, long-term decisions to `docs/decisions/`, and process artifacts to `docs/agent-project-kit/`. See `references/document-layout.md` and `references/workflow-checklists.md`.
- Product MVP UI Quality Gate: before frontend implementation or first frontend MVP slice completion. See `references/frontend.md`.
- MVP Closure Sentinel: before claiming `Full MVP Scope Complete` or `Release Ready`, or when the user asks what remains, whether the MVP is complete, whether release is safe, or what to do next after implementation. See `references/mvp-closure.md`.

When multiple readiness documents are missing, offer exactly two plain-text options:

1. Steady path: create or update the single most important next document, then ask for review.
2. Accelerated path: ask the user to authorize the named missing batch for this stage, create or update only those named documents, then run the readiness audit.

## Stage Router

Read the matching reference before giving stage instructions or editing project files:

| User situation                                                                                                       | Load                                                                      | Primary output                                                                                  |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Creating or reorganizing project source-of-truth documents                                                           | `references/document-layout.md`                                           | root `AGENTS.md` index plus docs under `docs/`                                                  |
| Vague idea, unsure what AI can do, or first project                                                                  | `references/project-initiation.md`                                        | clarified problem, reference scan, MVP boundary, project charter                                |
| Choosing stack, repository setup, version safety                                                                     | `references/project-initiation.md`, `references/architecture-baseline.md` | tech stack decision, architecture track, Git checkpoint rule                                    |
| Defining quality gates, scripts, CI, migrations, env, or repo hygiene                                                | `references/engineering-baseline.md`                                      | engineering baseline and acceptance checklist                                                   |
| Need project-level rules, AGENTS.md, or reusable process                                                             | `references/engineering-rules.md`                                         | Agent constitution and candidate skill workflow                                                 |
| Planning pages, UX states, components, frontend skeleton                                                             | `references/frontend.md`                                                  | page map, component map, frontend skeleton plan                                                 |
| Designing tables, fields, relations, migrations                                                                      | `references/database.md`                                                  | database design document                                                                        |
| Defining APIs, backend business boundaries, backend skeleton, architecture acceptance                                | `references/backend.md`                                                   | backend business spec, minimal backend skeleton, acceptance report                              |
| Checking backend safety, secrets, logs, dependencies, database risk                                                  | `references/security.md`                                                  | security boundary table and bottom-layer security evidence                                      |
| Deciding which tools or MCPs AI may use                                                                              | `references/tool-policy.md`                                               | `docs/ops/TOOL_POLICY.md` or tool permission matrix                                             |
| Need whole-project flow, default stack, or reusable prompt pack                                                      | `references/workflow-checklists.md`                                       | roadmap, docs checklist, default workflow docs                                                  |
| User asks to create the project, scaffold the app, or start implementation                                           | `references/workflow-checklists.md`, then missing stage references        | implementation readiness audit before any code                                                  |
| Existing baseline and bounded feature or local fix                                                                   | `references/workflow-checklists.md`, then affected source-of-truth docs   | Contract Impact Check, Implementation Handoff, verification evidence                            |
| User asks whether MVP is complete, what remains, whether release is safe, or asks for post-implementation next steps | `references/mvp-closure.md`, then relevant source-of-truth docs           | MVP closure audit, lifecycle state, remaining risks, next step recommendation                   |
| Feature/change detail would bloat current-state docs                                                                 | `references/document-layout.md`, affected stage references                | placement in `docs/features/`, `docs/changes/`, `docs/decisions/`, or `docs/agent-project-kit/` |

## Execution Flow

1. Classify the request into Project Baseline Path, Contract-Changing Feature Path, Bounded Feature Path, or Local Fix Path.
2. State the Goal Contract for project-level work.
3. Read the matching reference file before giving instructions or editing project files.
4. For vague project starts, satisfy Reference Project Scan Gate, Requirements Depth Gate, and Project Purpose Confirmation before asking to write the project charter.
5. For every source-of-truth document file, satisfy Document Consent Gate before creating or updating it.
6. Before technology stack confirmation, satisfy the Capability Library Scan Gate and get user confirmation for the combined core stack and third-party library set.
7. Before scaffolding or implementation, satisfy the Project Specification Readiness Gate. If documents are missing, stop implementation and offer the Steady path and Accelerated path with named missing batch and plain-text options.
8. Before implementation that changes design or contracts, satisfy the Source-of-Truth Change Gate and update the original project documents first.
9. When change details would bloat current-state docs, satisfy the Source-of-Truth Distillation Gate.
10. For Bounded Feature Path or Local Fix Path after readiness has passed, use the Implementation Handoff instead of rerunning the full baseline.
11. For implementation work, return evidence: changed source-of-truth documents when design changed, commands run, tests, build, browser/API checks, deployment checks, or security proof.
12. For high-risk operations involving production data, secrets, deployment, payments, cloud resources, database writes, or destructive file changes, stop and request explicit confirmation.
13. Use the MVP Closure Sentinel only when triggered.
14. When a Goal Contract milestone is genuinely satisfied, say so explicitly in the user's current language.

## Required Artifacts

When a `templates/` directory is available, copy and adapt its matching template instead of drafting the artifact from scratch.

- `AGENTS.md`: root-level Agent constitution and index into project documents.
- `docs/project/PROJECT_CHARTER.md`: reference project scan, target user, problem, MVP scope, non-goals, risks, acceptance criteria.
- `docs/architecture/TECH_STACK.md`: chosen stack, architecture track, capability library scan, rejected alternatives, re-evaluation rules, forbidden drift.
- `docs/architecture/ENGINEERING_BASELINE.md`: scripts, code quality, CI, migrations, env, testing, commit discipline.
- `docs/architecture/FRONTEND_PLAN.md`: pages, routes, components, states, design system, frontend source tree, file boundary contract, component split rules, import boundaries, frontend skeleton plan.
- `docs/architecture/DATABASE_DESIGN.md`: objects, tables, fields, relations, indexes, security notes.
- `docs/architecture/BACKEND_SPEC.md`: business rules, API boundary, permissions, data flow, error handling.
- `docs/workflow/AI_WORKFLOW.md`: clarify, spec, plan, implement, verify, archive.
- `docs/ops/TOOL_POLICY.md`: default tools, project tools, high-risk confirmations.
- `docs/ops/DEPLOYMENT.md`: local, staging, production, environment variables, health checks, rollback.
- `docs/features/<feature-name>.md`: stable feature behavior that should be easy to find without bloating current-state architecture docs.
- `docs/changes/<date-or-id>-<change-name>.md`: one change's proposal, design notes, tasks, acceptance notes, and temporary implementation context.
- `docs/decisions/ADR-<number>-<topic>.md`: long-term product or architecture decisions and rejected alternatives.
- `docs/agent-project-kit/`: Agent Project Kit process artifacts such as reference scans, capability scans, readiness audits, MVP closure audits, and handoffs.

These artifacts are not all required for every tiny task, but they are required before implementation when the project contains the corresponding surface.

## Source Notes

This skill is intentionally a lean router. Keep detailed procedures in `references/`, reusable project documents in `templates/`, and deterministic helpers in `scripts/`.
