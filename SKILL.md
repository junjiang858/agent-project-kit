---
name: agent-project-kit
description: Use when starting or governing AI-assisted software projects, especially project baseline setup, source-of-truth documents, architecture or contract changes, implementation readiness, tool permissions, security or deployment boundaries, or routing bounded feature work.
---

# Agent Project Kit

## Overview

Guide an AI-assisted software project through staged clarification, documented decisions, implementation boundaries, and evidence-based acceptance. Treat AI as a collaborator that needs product context, engineering rules, and verification gates before it writes or changes code.

## Core Rule

Do not jump from a vague idea to documents, technology choices, project scaffolding, or implementation. First identify the current project stage, load only the relevant reference, clarify the minimum facts for that stage, and ask for explicit consent before creating or updating any project document file or before irreversible or high-risk work.

For vague product ideas, do not narrow only inside the user's first wording. Before project purpose confirmation or project charter drafting, run the Reference Project Scan Gate so the user sees concrete existing projects, products, open-source repos, or adjacent implementations with direct links and can choose the direction with better context.

Before confirming a technology stack for a Product MVP, run the Capability Library Scan Gate. The agent must derive the needed technical capabilities from the confirmed project purpose and charter facts, research mature open-source or inspectable third-party libraries for those capabilities, and present the chosen stack together with the project-needed library set for user review.

Never create application scaffolding, UI pages, API skeletons, database schemas, package manager files, or implementation directories until the Project Specification Readiness Gate is satisfied or the user explicitly confirms a narrow bootstrap-only exception.

## Global Interaction Rules

### Confirmation Prompt Rule

Any task that asks for user confirmation, consent, approval, or a path choice must include a plain-text fallback in the assistant message. Do not depend on UI buttons, `request_user_input`, AskUserQuestion, or any host-specific quick action. Interactive tools may be used when available, but the visible message must still contain enough text for the user to reply directly.

When options are useful, label them clearly, such as `A. Continue` and `B. Revise`, and state what each option authorizes. For one-way or high-risk confirmations, state the exact action that will happen and wait for an explicit affirmative reply before acting.

### User Language Rule

Always match the user's current language for questions, confirmations, progress updates, final answers, and milestone messages unless the user requests another language. If the conversation contains multiple languages, use the language of the user's latest instruction. Preserve the same operational meaning across languages; do not force Chinese examples on non-Chinese users or English examples on Chinese users.

## Goal Contract

At the start of every project-level run, state the current goal in one sentence. The goal must include:

- Target outcome: what stage outcome the user is trying to reach.
- Completion signal: what concrete artifacts, confirmations, or evidence prove that outcome is reached.
- Next action: the single next question, document, audit, or implementation step.

Do not declare the goal achieved merely because a document was written. Declare success only when the goal's completion signal is satisfied and the user has confirmed the relevant source-of-truth artifact or readiness result.

For the common "create/start this project" flow, the default target outcome is: the project reaches an approved first MVP slice after the engineering baseline is ready. This default has two milestones:

1. Project engineering baseline ready.
2. First MVP slice accepted with evidence.

Beyond the first slice, use explicit lifecycle states instead of treating every positive audit as the same kind of "done":

| State | Meaning | Output behavior |
| --- | --- | --- |
| Engineering Baseline Ready | The project purpose, technical route, core source-of-truth documents, readiness gate, and required security/tool/deployment boundaries are ready for implementation. | Use the project engineering baseline readiness message. |
| First MVP Slice Complete | One approved, user-verifiable product loop has been implemented and checked with fresh evidence. | Use the first MVP slice completion message. |
| MVP Scope Incomplete | A closure audit found missing must-have scope, acceptance evidence, or blocking risk against the source-of-truth documents. | Do not celebrate; append remaining risks and a next step recommendation. |
| Full MVP Scope Complete | The documented MVP scope is implemented, current evidence covers the required acceptance criteria, and no blocking risk remains unless the user explicitly accepts it. | Use the MVP scope completion message and switch to Formal Product Development Mode. |
| Release Ready | Full MVP Scope Complete plus deployment, environment, security, regression, rollback, and operational checks are validated for the requested release target. | Use the release validation message and recommend release, monitoring, and post-release follow-up. |

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
- For frontend slices, a UI/UX/design system result that satisfies the Product MVP UI Quality Gate.
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

The Full MVP Scope Complete milestone is achieved only after the agent checks the current implementation against the MVP scope, must-have features, non-goals, acceptance criteria, and risks in the source-of-truth documents. It is broader than the first MVP slice and narrower than Release Ready.

A Full MVP Scope Complete result must include:

- Coverage of the documented MVP must-have scope and objective acceptance criteria.
- Fresh implementation evidence such as build, test, browser, API, CLI, worker, deployment preview, or run logs.
- Explicit separation of blocking risks from accepted non-blocking risks.
- No unresolved mock-only, production-unverified, deployment, security, or document-code drift blocker unless the user accepts it as outside the MVP release decision.

Chinese example:

```text
🎉 文档定义的 MVP 范围已完成！

✅ 当前实现已经覆盖真源文档定义的 MVP 范围，并提供了新的验证证据。
🚀 下一步进入正式项目发展：发布验证、架构加固、用户反馈和下一版本规划。
```

English example:

```text
🎉 MVP scope is complete!

✅ The documented MVP scope has been implemented and verified with current evidence.
🚀 Next, move into formal product development: release validation, architecture hardening, user feedback, and the next planned version.
```

Release Ready is achieved only after Full MVP Scope Complete and a release validation pass for the target environment.

Chinese example:

```text
🎉 发布验证已通过！

✅ MVP 范围、部署环境、回归检查、安全边界和运营准备已经通过当前证据验证。
🚀 下一步可以发布、监控真实使用情况，并规划发布后的修复和下一版本。
```

English example:

```text
🎉 Release validation passed!

✅ The MVP scope, deployment environment, regression checks, security boundaries, and operational readiness are verified with current evidence.
🚀 Next, release, monitor real usage, and plan post-release fixes and the next version.
```

When Full MVP Scope Complete is reached, do not close this skill. Stop treating the project as an MVP construction task and switch to Formal Product Development Mode: preserve and evolve the approved architecture, route new work through Contract Impact Check, update source-of-truth documents only when product, architecture, API, data, permissions, deployment, or operations change, run release validation for production requests, and plan post-MVP work through roadmap, features, ADRs, quality hardening, operations, and user feedback.

### MVP Closure Sentinel

Use `references/mvp-closure.md` for detailed MVP closure audit rules when the user asks whether the MVP is complete, asks what remains, asks whether the project can be released, asks for current risks or next steps after implementation, or when the agent is about to claim Full MVP Scope Complete or Release Ready.

To avoid slowing ordinary replies:

- Skip the closure audit for Local Fix Path, code explanation, single-command requests, and non-project-level questions.
- Use only the cached or recent closure result for ordinary project-level final suggestions unless the user asks for a fresh audit or the current task may close a documented must-have item.
- Run a synchronous closure audit before saying Full MVP Scope Complete or Release Ready.
- After implementation work, append a short next step recommendation when the closure result is incomplete, stale, or newly complete; do not interrupt the main answer with a long audit unless the user asked for it.
- Store MVP closure audits and cache snapshots under `docs/agent-project-kit/` or `.agent-project-kit/cache/` when the project allows process artifacts.

## Default Workflow Priority

When this skill is loaded or the user request matches AI-assisted project initiation, project baseline setup, source-of-truth documents, architecture or contract changes, implementation readiness, tool permissions, security boundaries, deployment boundaries, or bounded-feature routing, Agent Project Kit is the default primary workflow.

Use overlapping skills, including `superpowers` planning, TDD, execution, or review skills, only as auxiliary method libraries. Do not let overlapping skills replace this skill's stage router, confirmation gates, or required artifacts.

Skip this priority only when the user explicitly names another skill or process as the primary workflow, or when the task is a local code fix, code explanation, single command, or other non-project-level task.

Use the lightest path that protects the project:

| Path | Use when | Agent Project Kit responsibility |
| --- | --- | --- |
| Project Baseline Path | New project, project reorganization, missing core documents, technology stack choice, engineering baseline, security/tool/deployment boundary setup. | Run the staged clarification, reference scan, capability scan, document consent, and readiness gates before implementation. |
| Contract-Changing Feature Path | A feature or fix changes product behavior, routes, UI states, component responsibilities, API contracts, data shape, permissions, dependencies, deployment, tool permissions, or operations. | Read affected source-of-truth documents, propose the documentation delta, get required consent, update current-state docs first, then hand off to implementation. |
| Bounded Feature Path | The baseline exists and the work is inside approved source-of-truth contracts without changing architecture, data, permissions, dependencies, deployment, or tool boundaries. | Read the relevant docs, state that no source-of-truth update is needed, then use implementation discipline without rerunning the full baseline. |
| Local Fix Path | Small bug fix, copy/style tweak, test fix, code explanation, single command, or other local task that does not change product or engineering contracts. | Do not run the project baseline flow. Use debugging, TDD, verification, or direct command execution as appropriate. |

Before classifying a feature as bounded, run a Contract Impact Check. Treat the work as contract-changing if it changes any of:

- Frontend route, page, component responsibility, UI state, interaction, data dependency, source tree, shared UI location, state/config/i18n/icon/asset/utility ownership, or import boundary.
- API endpoint, request/response contract, validation, error shape, permission rule, backend workflow, integration, worker, or data flow.
- Table, field, relation, index, enum, seed, schema, migration, data ownership, retention, or rollback plan.
- Framework, package, script, repository layout, quality gate, deployment path, environment variable, tool permission, or operational behavior.
- Security, privacy, production data, external write, payment, secrets, privileged local access, or destructive operation boundary.

### Optional Workflow Tool Fallback

Superpowers, OpenSpec, GitHub Spec Kit, issue trackers, and similar workflow tools are optional accelerators, not hard dependencies.

If an overlapping workflow tool is available and applicable, use it as an auxiliary method library after this skill has classified the task and protected the source-of-truth gates. For example, use Superpowers-style planning, TDD, execution, review, and verification during implementation, or use OpenSpec/GitHub Spec Kit artifacts as change-spec inputs.

If an optional workflow tool is unavailable, do not block the workflow and do not ask the user to install it unless the user explicitly requested that specific tool as the primary workflow. Use this built-in fallback:

1. Clarify the requested scope.
2. Run the Contract Impact Check.
3. Read and update affected source-of-truth documents only when contracts change.
4. Produce the smallest useful implementation plan.
5. Implement the smallest useful change.
6. Verify with tests, build, browser, API, CLI, worker, security, or run evidence as applicable.
7. Report source-of-truth deltas and verification evidence.

### Implementation Handoff

When the Project Specification Readiness Gate has passed and the current task is a Bounded Feature Path or Local Fix Path, do not restart the full project baseline flow. Hand off to the project's approved implementation discipline: Superpowers if installed and applicable, another explicitly selected workflow if the user chose one, or the built-in fallback above.

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

Treat default stack recommendations as context-aware candidates, not hard requirements. Confirm repository shape, UI library, icon library, framework, build tool, package manager, and backend/database boundaries from the product shape, design system, implementation needs, and migration cost. A single deployable frontend app can stay a single package when all code has one ownership boundary and no shared package boundary exists; a workspace is appropriate only when local packages such as shared schemas, reusable media/core logic, workers, SDKs, or multiple apps have real ownership. For design-heavy frontend work, linked designs, screenshots, existing design systems, and brand assets may justify replacing default UI or icon libraries after documenting the reason and receiving approval.

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

Render these as plain-text options even when no interactive choice tool is available. Do not depend on UI buttons, `request_user_input`, or any host-specific quick action. Label the choices clearly, such as `A. Steady path` and `B. Accelerated path`, and include the exact document paths covered by each choice.

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

For frontend work, `docs/architecture/FRONTEND_PLAN.md` must include a frontend engineering contract before implementation: source tree, route and app-shell responsibilities, component split rules, state/config/i18n/icon/asset/utility ownership, and import boundaries. A page map or visual style note alone is not enough to start frontend code.

For frontend work, `docs/architecture/FRONTEND_PLAN.md` must also satisfy the Product MVP UI Quality Gate before implementation. It must include the Design Read, design system tokens, UI component strategy, state and interaction contract, responsive and accessibility expectations, anti-slop guardrails, and browser UI quality verification plan. A first MVP page may be narrow, but it must not be a throwaway or visually generic surface.

If any required artifact is missing, do not dump a raw checklist. State the current stage, identify only the documents that directly unblock the next stage, explain why each one matters now, and offer the steady path or accelerated path from the Document Consent Gate. Use plain-text options and do not depend on UI buttons. Do not create code or scaffolding while the gate is incomplete.

Bootstrap-only exception: if the user explicitly asks to create a bare repository skeleton before the readiness set is complete, confirm that the exception is limited to empty folders, root config, Git setup, and documentation plumbing. Do not add UI/API/business logic, database schema, migrations, or runnable product behavior under this exception.

## Source-of-Truth Change Gate

Before implementing any change that alters project design, product behavior, contracts, data shape, permissions, or operations, update the original source-of-truth document first and get the required confirmation. Treat OpenSpec, GitHub Spec Kit, issue specs, design notes, and chat plans as auxiliary inputs unless the user explicitly declares one of them to be the new source of truth.

Design or contract changes include:

- New or changed page, route, component responsibility, UI state, data dependency, or frontend interaction: update `docs/architecture/FRONTEND_PLAN.md`.
- New or changed frontend source tree, folder responsibility, component split rule, import boundary, shared UI location, i18n/config/state/utils ownership, or file colocation rule: update `docs/architecture/FRONTEND_PLAN.md`.
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

### Source-of-Truth Distillation Gate

Core source-of-truth documents describe the current system contract, not the full history of how the project got there. Do not append every feature discussion, task list, rejected option, or verification log to `PROJECT_CHARTER.md`, `TECH_STACK.md`, `FRONTEND_PLAN.md`, `BACKEND_SPEC.md`, `DATABASE_DESIGN.md`, `AI_WORKFLOW.md`, `TOOL_POLICY.md`, or `DEPLOYMENT.md`.

Route detail by lifespan:

- Current product, architecture, API, data, permission, deployment, or tool contract: distill into the relevant core source-of-truth document.
- Stable feature behavior that users or agents will reference repeatedly: place in `docs/features/<feature-name>.md` and link from the relevant core document when useful.
- One change's proposal, design notes, task breakdown, acceptance notes, or temporary implementation context: place in `docs/changes/<date-or-id>-<change-name>.md`.
- Long-term architecture or product tradeoff: place in `docs/decisions/ADR-<number>-<topic>.md`.
- Agent Project Kit process artifacts such as reference scans, capability scans, readiness audits, or handoffs: place under `docs/agent-project-kit/`.
- Obsolete detail: archive, replace with a short historical note, or remove after confirming it is no longer the current contract.

After completing a change, distill only the durable result back into the core source-of-truth documents. Keep process-heavy detail in `docs/changes/`, not in the current-state docs.

## Product MVP UI Quality Gate

MVP scope may be small, but UI/UX/design system quality is not optional. A Product MVP should cut features, not ship a careless interface. For web products, the first MVP page is the user's entry into the first product loop, so it must feel like a coherent product surface rather than a temporary demo.

Before creating or updating `docs/architecture/FRONTEND_PLAN.md`, run a Design Read:

- Identify the surface type: marketing site, product workspace, SaaS app, admin panel, dashboard, data table, multi-step flow, internal tool, content surface, mobile app, mini program, or hardware UI.
- Identify audience, product tone, visual density, interaction complexity, accessibility constraints, existing brand assets, and reference signals.
- State one concise design direction for the plan. If two directions would materially change the product, ask one clarifying question.
- Use taste-skill and anti-slop rules contextually; do not apply landing-page taste rules blindly to dashboards, admin panels, data tables, or multi-step product UI. For operational product UI, prefer scannable density, efficient controls, clear state, restrained motion, and mature design-system or data-grid patterns.

`docs/architecture/FRONTEND_PLAN.md` must define:

- Design system foundation: selected UI library, icon library, typography, semantic color tokens, spacing, radius, shadow, border, breakpoints, z-index, motion, and theme strategy.
- Layout contract: app shell, navigation, toolbar, content regions, sidebars, detail panels, tables/lists/cards, dialogs, and mobile collapse rules.
- State and interaction contract: loading, empty, error, success, disabled, selected, validating, saving, optimistic, permission-denied, focus, hover, active, keyboard, toast, dialog, destructive-action, and undo patterns when relevant.
- Component strategy: use the approved UI library for common controls, avoid hand-written duplicate base components, customize tokens rather than scattering one-off styles, and split business components by user concept, interaction state, and data boundary.
- Design-system dependency rule: selected UI and icon libraries are approved project decisions, not fixed skill defaults. When a Figma/Stitch/design-system source or existing codebase uses a different component or icon language, propose the replacement, update `TECH_STACK.md` and `FRONTEND_PLAN.md`, get approval, then implement through a local adapter or component layer.
- Anti-slop guardrails: no generic AI-purple gradient default, no fake product previews made from decorative divs, no gratuitous glassmorphism or motion, no repeated equal-card layouts unless the product data truly calls for them, no ungrounded metrics, no placeholder-as-label forms, no text overflow, and no incoherent overlaps.
- Browser UI quality verification: build/type check plus browser inspection of the key flow on desktop and mobile, including visual hierarchy, readable contrast, text fit, stable dimensions, responsive layout, keyboard/focus behavior, and required states.

Before declaring a first frontend MVP slice complete, verify that the page proves the approved product loop, follows the documented design system, exposes the expected states, and has fresh browser evidence. If the UI looks generic, fragmented, inaccessible, or structurally inconsistent with `FRONTEND_PLAN.md`, the slice is not complete even if the happy path works.

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
| Existing baseline and bounded feature or local fix | `references/workflow-checklists.md`, then affected source-of-truth docs | Contract Impact Check, implementation handoff, verification evidence |
| User asks whether MVP is complete, what remains, whether release is safe, or asks for post-implementation next steps | `references/mvp-closure.md`, then relevant source-of-truth docs | MVP closure audit, lifecycle state, remaining risks, and next step recommendation |
| Feature/change detail would bloat current-state docs | `references/document-layout.md`, affected stage references | `docs/features/`, `docs/changes/`, `docs/decisions/`, or `docs/agent-project-kit/` placement |

## Execution Flow

1. Classify the request into one stage from the router.
2. State the Goal Contract for the current run: target outcome, completion signal, and next action.
3. For feature or fix work, run the Contract Impact Check before choosing Project Baseline, Contract-Changing Feature, Bounded Feature, or Local Fix.
4. Read the matching reference file before giving instructions or editing project files.
5. When creating project documents, use `references/document-layout.md` unless the user explicitly requests a different layout.
6. Check whether required upstream artifacts exist. If only one artifact or fact is missing, request only that item. If multiple readiness documents are missing, run the stage-aware readiness audit and offer both steady and accelerated paths.
7. When information is missing, use Guided Interaction instead of dumping a long checklist of questions.
8. For project initiation, satisfy Reference Project Scan Gate, Requirements Depth Gate, and Project Purpose Confirmation before asking to write the project charter.
9. For every document file, satisfy Document Consent Gate before creating or updating it.
10. Before technology stack confirmation, satisfy the Capability Library Scan Gate and get user confirmation for the combined core stack and library set.
11. Before scaffolding or implementation, satisfy the Project Specification Readiness Gate. If documents are missing, stop implementation and offer the steady path and accelerated path as plain-text options.
12. Before any implementation that changes design or contracts, satisfy the Source-of-Truth Change Gate and update the original project documents first.
13. When change details would bloat a current-state document, satisfy the Source-of-Truth Distillation Gate and route process detail to `docs/features/`, `docs/changes/`, `docs/decisions/`, or `docs/agent-project-kit/`.
14. For Bounded Feature Path or Local Fix Path after readiness has passed, use the Implementation Handoff instead of rerunning the full project baseline.
15. Produce the smallest useful approved stage artifact: plan, document, checklist, matrix, skeleton, or acceptance report. After creating or updating any readiness document, rerun the readiness audit summary in the final response; when multiple readiness documents remain, end with the two plain-text options rather than a single "next document" suggestion.
16. For implementation work, preserve Git checkpoints and return evidence: updated source-of-truth documents when design changed, commands run, tests, build, browser/API checks, or security proof.
17. Use the MVP Closure Sentinel only when triggered. Do not make ordinary questions slower by rereading the whole project when a cached closure result or no closure result is sufficient.
18. For high-risk operations involving production data, secrets, deployment, payments, cloud resources, database writes, or destructive file changes, stop and request explicit confirmation.
19. When a Goal Contract milestone is genuinely satisfied, say so explicitly. Provide the project engineering baseline congratulatory message at the baseline milestone, the first MVP slice congratulatory message after the approved slice is implemented and verified, the MVP scope completion message only after the closure audit passes, and the release validation message only after release checks pass.

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
| Treating frontend directory structure as cleanup after code generation | Define the frontend engineering contract in `docs/architecture/FRONTEND_PLAN.md` before writing UI code, then implement against it. |
| Putting UI, config, messages, state, icons, mock data, and utilities into one route or app file | Split code by route composition, shared UI, business components, config, i18n, state, assets, and capability-scoped utilities. |
| Treating Git as an afterthought | Initialize Git early and commit every stable stage. |
| Putting every rule into the Agent constitution | Keep project rules short; move task-specific procedures into skills or references. |
| Dumping every project document in the repository root | Keep only `AGENTS.md` as the root index; put detailed documents under `docs/`. |
| Choosing a throwaway MVP stack for a product MVP | Keep scope small, but choose a stack and repo shape that can grow without a core rewrite. |
| Treating default stack suggestions as mandatory | Use defaults as candidates; document why the project needs a single package, workspace, UI library, icon library, backend, or database before locking it. |
| Accepting "it is secure" as proof | Require file locations, code paths, tests, and role-based evidence. |
| Opening every tool to AI | Separate default-open tools, project-specific tools, and high-risk confirmation gates. |
| Letting code, migrations, or APIs become the first record of a design change | Update the original source-of-truth document first, then implement against it. |
| Rerunning the whole baseline for a bounded feature | Run the Contract Impact Check, then use the Implementation Handoff when no contract changes are needed. |
| Requiring Superpowers or OpenSpec when they are unavailable | Use Optional Workflow Tool Fallback unless the user explicitly made that tool the primary workflow. |
| Turning source-of-truth docs into change journals | Distill current contracts into core docs and keep feature/change/process detail in `docs/features/`, `docs/changes/`, `docs/decisions/`, or `docs/agent-project-kit/`. |
| Treating first MVP slice, full MVP scope, and release readiness as the same status | Use the lifecycle states and the MVP Closure Sentinel before claiming Full MVP Scope Complete or Release Ready. |

## Source Notes

This skill is distilled from the local Obsidian handbook `AI 编程项目实战手册` and intentionally excludes image indexes and screenshot assets. Keep the skill procedural, concise, and evidence-oriented.
