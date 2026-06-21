---
name: agent-project-kit
description: Use when planning, building, or reviewing AI-assisted software projects from vague idea to delivery, especially for Vibe Coding, project charters, tech stack decisions, Agent constitution, skill workflows, frontend/backend/database skeletons, security acceptance, tool permissions, or AI-friendly engineering rules.
---

# Agent Project Kit

## Overview

Guide an AI-assisted software project through staged clarification, documented decisions, implementation boundaries, and evidence-based acceptance. Treat AI as a collaborator that needs product context, engineering rules, and verification gates before it writes or changes code.

## Core Rule

Do not jump from a vague idea to documents, technology choices, project scaffolding, or implementation. First identify the current project stage, load only the relevant reference, clarify the minimum facts for that stage, and ask for explicit consent before creating or updating any project document file or before irreversible or high-risk work.

For vague product ideas, do not narrow only inside the user's first wording. Before project purpose confirmation or project charter drafting, run the Reference Project Scan Gate so the user sees concrete existing projects, products, open-source repos, or adjacent implementations with direct links and can choose the direction with better context.

Before confirming a technology stack for a Product MVP, run the Capability Library Scan Gate. The agent must derive the needed technical capabilities from the confirmed project purpose and charter facts, research mature open-source or inspectable third-party libraries for those capabilities, and present the chosen stack together with the project-needed library set for user review.

Never create application scaffolding, UI pages, API skeletons, database schemas, package manager files, or implementation directories until the Project Specification Readiness Gate is satisfied or the user explicitly confirms a narrow bootstrap-only exception.

## Goal Contract

At the start of every project-level run, state the current goal in one sentence. The goal must include:

- Target outcome: what stage outcome the user is trying to reach.
- Completion signal: what concrete artifacts, confirmations, or evidence prove that outcome is reached.
- Next action: the single next question, document, audit, or implementation step.

Do not declare the goal achieved merely because a document was written. Declare success only when the goal's completion signal is satisfied and the user has confirmed the relevant source-of-truth artifact or readiness result.

For the common "create/start this project" flow, the default target outcome is: the project reaches an approved first MVP slice after the engineering baseline is ready. This default has two milestones:

1. Project engineering baseline ready.
2. First MVP slice accepted with evidence.

The project engineering baseline milestone is achieved when:

- Project purpose is confirmed.
- Required source-of-truth documents for the product shape are present or explicitly marked not applicable.
- The Project Specification Readiness Gate has passed.
- High-risk security/tool/deployment boundaries are documented when relevant.
- The user has confirmed the readiness result or approved the next implementation step.

When this milestone is achieved, end with a concise readiness message in the user's current language. Preserve the same meaning; do not force Chinese for non-Chinese users.

Chinese example:

```text
🎉 恭喜，项目工程基线已就绪！

✅ 项目目标、技术路线、核心文档和实现前门禁已经到位。
🚀 下一步可以从第一个已批准的产品闭环开始实现。
```

English example:

```text
🎉 Project engineering baseline is ready!

✅ The project goal, technical route, core documents, and implementation readiness gate are in place.
🚀 Next, you can start implementing the first approved product loop.
```

The first MVP slice milestone is achieved only after the baseline is ready and one approved, user-verifiable product slice has been implemented and checked. For web products, this usually includes the first MVP page as the user entry, but the completion standard is the slice, not a static page. For non-web projects, the slice can be the first API, worker flow, CLI flow, automation run, or other product workflow.

A first MVP slice must include:

- One approved core user scenario from entry to useful outcome.
- The necessary UI page, API, worker, CLI, automation, or integration surface for that scenario.
- Required states, data/API/mock behavior, and acceptance criteria from the source-of-truth documents.
- Fresh verification evidence such as build, test, browser, API, CLI, worker, or run logs.

Chinese example:

```text
🎉 恭喜，首个 MVP 切片已完成！

✅ 第一个已批准的产品闭环已经实现，并提供了运行、构建、浏览器、API 或任务验收证据。
🚀 下一步可以继续扩展后续页面、数据流、接口、任务或部署发布。
```

English example:

```text
🎉 First MVP slice is complete!

✅ The first approved product loop has been implemented with run, build, browser, API, or task verification evidence.
🚀 Next, you can expand the remaining pages, data flows, APIs, jobs, or deployment path.
```

## Default Workflow Priority

When this skill is loaded or the user request matches AI-assisted project initiation, planning, architecture, frontend, backend, database, security, tool permissions, acceptance, or delivery workflow, Agent Project Kit is the default primary workflow.

Use overlapping skills, including `superpowers` planning, TDD, execution, or review skills, only as auxiliary method libraries. Do not let overlapping skills replace this skill's stage router, confirmation gates, or required artifacts.

Skip this priority only when the user explicitly names another skill or process as the primary workflow, or when the task is a local code fix, code explanation, single command, or other non-project-level task.

## Guided Interaction

Ask one question at a time when gathering missing project context. Do not present a full intake questionnaire unless the user explicitly asks for one.

For vague project starts, use this loop:

1. State the current stage in one short sentence.
2. Ask the single most important next question.
3. Wait for the answer.
4. When the initial idea is clear enough to search and the scan is not done yet, complete the Reference Project Scan Gate and ask the user to choose a direction.
5. Wait for the user's direction choice.
6. Reflect the answer into the current artifact.
7. Continue only to the next necessary question or draft.

If two details are inseparable, ask at most two short questions. Prefer multiple-choice options when they reduce effort.

Do not treat a one-sentence project idea as enough context for a project charter. When the user's wording contains ambiguous domain nouns or product-shape terms, clarify what they mean in this project before drafting a PRD-quality artifact. Identify the core objects the product manages, the main operations users perform on them, and the boundaries around roles, data, external systems, execution, observability, and safety.

## Reference Project Scan Gate

Before Requirements Depth Gate, Project Purpose Confirmation, technology selection, or project charter drafting for a vague or early product idea, scan for concrete reference projects.

The scan must include 3-7 specific projects, products, open-source repositories, plugins, templates, or adjacent implementations. Each item must include project name, direct link, and decision impact:

- Project name.
- A direct link to the product page, repository, documentation, marketplace page, or other primary source.
- Source type: open-source repo, commercial product, plugin, framework example, template, or adjacent implementation.
- What this project can teach or contribute to the user's idea.
- What not to copy blindly.
- How it changes the user's possible MVP direction.

Do not satisfy this gate with abstract categories like "similar SaaS products", "open-source tools", or "competitors" without concrete links. If the community landscape may have changed, use web search or another live source. If live search is unavailable, say that the scan is incomplete and ask whether to continue with known examples or wait for research.

After the scan, offer 2-4 direction choices grounded in those references. Ask the user to pick, combine, or reject a direction. Do not continue to project purpose confirmation, `docs/project/PROJECT_CHARTER.md`, technology selection, or implementation planning until the user chooses or confirms a direction after seeing the linked references.

## Project Purpose Confirmation

Before moving beyond project initiation, summarize the project purpose for the user: who it serves, what problem it solves, what the product does, and what the MVP should cover first. Ask the user to confirm or correct that summary.

Do not move into technology stack, frontend, backend, database, or implementation planning until the user confirms the project purpose summary.

## Capability Library Scan Gate

Before technology stack confirmation, `docs/architecture/TECH_STACK.md`, dependency installation, package manager edits, scaffolding, or implementation, scan for third-party libraries that match the project's required technical capabilities.

The scan starts from confirmed project facts, not generic popularity. First extract the required technical capabilities, such as authentication, forms, validation, tables, charts, rich text, file upload, search, background jobs, payments, email, realtime, AI SDKs, workflow orchestration, observability, testing, or deployment. Then research only libraries that serve those capabilities.

Each recommended or rejected candidate must include capability, library name, direct link, ecosystem, open-source or inspectability status, license or commercial constraint when relevant, maintenance evidence, why it fits or does not fit this project, migration or lock-in risk, and whether it is included now, deferred, or rejected.

Prefer mature, well-documented, actively maintained, open-source libraries when they fit the project. Do not add a library just because it is popular; if the MVP can use framework-native functionality without losing clarity, mark the library as deferred or unnecessary.

If the library landscape may have changed, use live search, official docs, package registries, GitHub repositories, release notes, or security advisories. If live research is unavailable, say that maintenance confidence is incomplete and ask whether to continue with known candidates or wait for research.

Present the final review as one combined stack decision:

- Core stack: framework, runtime, database, deployment, package manager, testing.
- Capability library table: included, deferred, and rejected libraries.
- Reasons why the included libraries are necessary for this project.
- Risks, licensing notes, and replacement triggers.

Do not confirm a technology stack, write `docs/architecture/TECH_STACK.md`, install dependencies, or scaffold implementation until the user confirms the combined core stack and third-party library set.

## Document Consent Gate

Do not create, copy, overwrite, move, or edit any project source-of-truth document until the user explicitly agrees to write that specific document or has directly asked for that exact document to be written. This includes `AGENTS.md`, every file under `docs/`, and any root-level planning document.

Before writing a document file:

1. Confirm the current stage artifact in conversation.
2. State the target path and what the document will contain.
3. Ask whether to write or update that file.
4. Wait for an affirmative answer.

Consent applies only to the named document and current stage. Writing `docs/project/PROJECT_CHARTER.md` does not imply permission to write `docs/architecture/TECH_STACK.md`, `AGENTS.md`, or engineering baseline files.

When multiple documents are missing for the next stage, first interpret the current stage, then explain which missing documents directly unblock that next stage and why they are needed now. Offer exactly two paths:

1. Steady path: create or update only the single most important next document, then ask for review before continuing.
2. Accelerated path: ask the user to authorize the named missing batch for this stage, create or update only those listed documents, then run the implementation readiness audit.

Batch consent is limited to the named document list and current stage. It is not permanent permission, does not cover future documents discovered later, and does not authorize implementation code, scaffolding, package manager files, UI pages, APIs, database schemas, migrations, or runnable behavior.

The agent may discuss, summarize, or propose a short outline in chat before consent, but must not create or modify document files before consent.

## Requirements Depth Gate

Before asking to write `docs/project/PROJECT_CHARTER.md`, gather enough context for a PRD-quality charter. At minimum, the conversation must cover:

- The selected direction from the Reference Project Scan Gate and any reference projects the user wants to borrow from or avoid.
- Target user or user role.
- Core scenario and pain point.
- MVP outcome and first-use workflow.
- Must-have features, explicit non-goals, and postponed items.
- Core domain objects and important data, resources, or external systems.
- Key business rules, permissions, and safety constraints.
- Acceptance criteria that can be checked objectively.
- Open questions that would affect architecture or implementation.

If these are not known yet, keep asking one focused question at a time. If the user is unsure, offer 2-3 concrete options and ask them to choose or revise one.

## Project Specification Readiness Gate

Before creating or modifying implementation files, scaffolding a repo, adding package manager files, creating `apps/` or `packages/`, writing UI/API/database code, or starting a dev server, verify that the relevant source-of-truth documents exist and are confirmed by the user.

For a Product MVP with web, backend, database, tool execution, deployment, or AI workflow concerns, the implementation readiness set is:

- `AGENTS.md`
- `docs/project/PROJECT_CHARTER.md`
- `docs/architecture/TECH_STACK.md`
- `docs/architecture/ENGINEERING_BASELINE.md`
- `docs/architecture/FRONTEND_PLAN.md` when any frontend UI will be created.
- `docs/architecture/DATABASE_DESIGN.md` when any database, schema, migration, or persistent data model will be created.
- `docs/architecture/BACKEND_SPEC.md` when any API, backend service, worker, tool execution, or integration boundary will be created.
- `docs/workflow/AI_WORKFLOW.md`
- `docs/ops/TOOL_POLICY.md`
- `docs/ops/DEPLOYMENT.md` when local run, environment variables, deployment, or operational setup is needed.

For high-risk projects involving uploaded executable content, tool execution, secrets, payments, production data, external writes, or privileged local access, also require explicit security acceptance content before implementation. This can live in `docs/architecture/BACKEND_SPEC.md`, `docs/ops/TOOL_POLICY.md`, or a separately approved security document if the user requests one.

If any required artifact is missing, do not dump a raw checklist. State the current stage, identify only the documents that directly unblock the next stage, explain why each one matters now, and offer the steady path or accelerated path from the Document Consent Gate. Do not create code or scaffolding while the gate is incomplete.

Bootstrap-only exception: if the user explicitly asks to create a bare repository skeleton before the readiness set is complete, confirm that the exception is limited to empty folders, root config, Git setup, and documentation plumbing. Do not add UI/API/business logic, database schema, migrations, or runnable product behavior under this exception.

## Source-of-Truth Change Gate

Before implementing any change that alters project design, product behavior, contracts, data shape, permissions, or operations, update the original source-of-truth document first and get the required confirmation. Treat OpenSpec, GitHub Spec Kit, issue specs, design notes, and chat plans as auxiliary inputs unless the user explicitly declares one of them to be the new source of truth.

Design or contract changes include:

- New or changed page, route, component responsibility, UI state, data dependency, or frontend interaction: update `docs/architecture/FRONTEND_PLAN.md`.
- New or changed API, request/response contract, validation rule, error shape, permission rule, backend workflow, integration, worker, or data flow: update `docs/architecture/BACKEND_SPEC.md`.
- New or changed table, field, relation, index, enum, seed, schema, migration, ownership rule, retention rule, or rollback plan: update `docs/architecture/DATABASE_DESIGN.md`.
- New or changed framework, dependency, script, repository layout, quality gate, deployment path, environment variable, tool permission, or operational behavior: update the relevant tech stack, engineering baseline, tool policy, or deployment document.

Use this sequence:

1. Read the current source-of-truth documents and identify which ones the requested change affects.
2. Propose the documentation delta before code, schema, migration, API, or UI edits.
3. Satisfy the Document Consent Gate and update the existing document files, not only a chat summary or temporary spec.
4. Confirm the updated documents still satisfy the Project Specification Readiness Gate.
5. Implement the smallest code change that follows the updated documents.
6. If implementation reveals an unavoidable design change, pause implementation, update the source-of-truth document first, then continue.

## Stage Router

| User situation | Load | Primary output |
| --- | --- | --- |
| Creating or reorganizing project source-of-truth documents | `references/document-layout.md` | root `AGENTS.md` index plus docs under `docs/` |
| Vague idea, unsure what AI can do, or first project | `references/project-initiation.md` | clarified problem, MVP boundary, project charter |
| Choosing stack, repository setup, version safety | `references/project-initiation.md`, `references/architecture-baseline.md` | tech stack decision, architecture track, Git checkpoint rule |
| Defining quality gates, scripts, CI, migrations, env, or repo hygiene | `references/engineering-baseline.md` | engineering baseline and acceptance checklist |
| Need project-level rules, AGENTS.md, or reusable process | `references/engineering-rules.md` | Agent constitution, candidate skill workflow |
| Planning pages, UX states, components, frontend skeleton | `references/frontend.md` | page map, component map, frontend skeleton plan |
| Designing tables, fields, relations, migrations | `references/database.md` | database design document |
| Defining APIs, backend business boundaries, backend skeleton, architecture acceptance | `references/backend.md` | backend business spec, minimal backend skeleton, acceptance report |
| Checking backend safety, secrets, logs, dependencies, database risk | `references/security.md` | security boundary table, bottom-layer security evidence |
| Deciding which tools or MCPs AI may use | `references/tool-policy.md` | `docs/ops/TOOL_POLICY.md` or tool permission matrix |
| Need whole-project flow, default stack, or reusable prompt pack | `references/workflow-checklists.md` | roadmap, docs checklist, default workflow docs |
| User asks to create the project, scaffold the app, or start implementation | `references/workflow-checklists.md`, then the missing stage references | implementation readiness audit before any code |

## Execution Flow

1. Classify the request into one stage from the router.
2. State the Goal Contract for the current run: target outcome, completion signal, and next action.
3. Read the matching reference file before giving instructions or editing project files.
4. When creating project documents, use `references/document-layout.md` unless the user explicitly requests a different layout.
5. Check whether required upstream artifacts exist. If they are missing, request only the next missing artifact or fact, not the entire chain.
6. When information is missing, use Guided Interaction instead of dumping a long checklist of questions.
7. For project initiation, satisfy Reference Project Scan Gate, Requirements Depth Gate, and Project Purpose Confirmation before asking to write the project charter.
8. For every document file, satisfy Document Consent Gate before creating or updating it.
9. Before technology stack confirmation, satisfy the Capability Library Scan Gate and get user confirmation for the combined core stack and library set.
10. Before scaffolding or implementation, satisfy the Project Specification Readiness Gate. If documents are missing, stop implementation and continue with the next approved source-of-truth document.
11. Before any implementation that changes design or contracts, satisfy the Source-of-Truth Change Gate and update the original project documents first.
12. Produce the smallest useful approved stage artifact: plan, document, checklist, matrix, skeleton, or acceptance report.
13. For implementation work, preserve Git checkpoints and return evidence: updated source-of-truth documents when design changed, commands run, tests, build, browser/API checks, or security proof.
14. For high-risk operations involving production data, secrets, deployment, payments, cloud resources, database writes, or destructive file changes, stop and request explicit confirmation.
15. When a Goal Contract milestone is genuinely satisfied, say so explicitly. Provide the project engineering baseline congratulatory message at the baseline milestone, and provide the first MVP slice congratulatory message only after the approved slice is implemented and verified with fresh evidence.

## Required Artifacts

When a `templates/` directory is available, copy and adapt its matching template instead of drafting the artifact from scratch.

- `AGENTS.md`: root-level Agent constitution and index into project documents.
- `docs/project/PROJECT_CHARTER.md`: reference project scan, target user, problem, MVP scope, non-goals, risks, acceptance criteria.
- `docs/architecture/TECH_STACK.md`: chosen stack, architecture track, capability library scan, rejected alternatives, re-evaluation rules, forbidden drift.
- `docs/architecture/ENGINEERING_BASELINE.md`: scripts, code quality, CI, migrations, env, testing, commit discipline.
- `docs/architecture/FRONTEND_PLAN.md`: pages, routes, components, states, design system, frontend skeleton plan.
- `docs/architecture/DATABASE_DESIGN.md`: objects, tables, fields, relations, indexes, security notes.
- `docs/architecture/BACKEND_SPEC.md`: business rules, API boundary, permissions, data flow, error handling.
- `docs/workflow/AI_WORKFLOW.md`: clarify, spec, plan, implement, verify, archive.
- `docs/ops/TOOL_POLICY.md`: default tools, project tools, high-risk confirmations.
- `docs/ops/DEPLOYMENT.md`: local, staging, production, environment variables, health checks, rollback.

These artifacts are not all required for every tiny task, but they are required before implementation when the project contains the corresponding surface. Do not treat `PROJECT_CHARTER.md`, `TECH_STACK.md`, and `ENGINEERING_BASELINE.md` alone as enough to start a Product MVP scaffold with frontend, backend, database, tool execution, or deployment concerns.

## Common Mistakes

| Mistake | Correction |
| --- | --- |
| Asking AI to code before scope is clear | Create or update the project charter first. |
| Listing vague competitor categories during initiation | Run a Reference Project Scan Gate with project name, direct link, lessons, cautions, and direction choices. |
| Planning implementation before confirming project purpose | Summarize the target user, problem, product role, and MVP; wait for user confirmation. |
| Confirming a stack without library research | Run a Capability Library Scan Gate and review project-needed third-party libraries with links, maintenance evidence, and include/defer/reject decisions. |
| Letting AI choose many possible stacks forever | Discuss alternatives, then commit to one documented main route. |
| Starting a scaffold after only a charter, stack, and engineering baseline | Run the Project Specification Readiness Gate and create frontend, database, backend, workflow, tool policy, deployment, and Agent rule documents as applicable before implementation. |
| Treating Git as an afterthought | Initialize Git early and commit every stable stage. |
| Putting every rule into the Agent constitution | Keep project rules short; move task-specific procedures into skills or references. |
| Dumping every project document in the repository root | Keep only `AGENTS.md` as the root index; put detailed documents under `docs/`. |
| Choosing a throwaway MVP stack for a product MVP | Keep scope small, but choose a stack and repo shape that can grow without a core rewrite. |
| Accepting "it is secure" as proof | Require file locations, code paths, tests, and role-based evidence. |
| Opening every tool to AI | Separate default-open tools, project-specific tools, and high-risk confirmation gates. |
| Letting code, migrations, or APIs become the first record of a design change | Update the original source-of-truth document first, then implement against it. |

## Source Notes

This skill is distilled from the local Obsidian handbook `AI 编程项目实战手册` and intentionally excludes image indexes and screenshot assets. Keep the skill procedural, concise, and evidence-oriented.
