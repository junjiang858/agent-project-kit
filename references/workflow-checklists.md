# Workflow Checklists

Use this reference for the whole AI programming roadmap, deliverable tracking, default AI-friendly stack, and reusable workflow prompts.

## Contents

- Project Roadmap
- Interaction Defaults
- Task Routing
- Contract Impact Check
- Optional Workflow Tool Fallback
- Implementation Handoff
- Document Consent Gate
- Goal And Completion Signal
- Deliverable Checklist
- Implementation Readiness Gate
- Source-of-Truth Change Gate
- Source-of-Truth Distillation Gate
- Common Mistakes
- Default Product MVP Stack
- Prompts

## Project Roadmap

1. Cognition calibration.
2. Project initiation.
3. Reference project scan with concrete project links.
4. Technology selection with capability library scan.
5. Git version safety.
6. Agent constitution.
7. Skill workflow.
8. Frontend/backend/database technical understanding.
9. Frontend skeleton and database design.
10. Backend business spec and minimal backend skeleton.
11. Backend architecture acceptance.
12. Backend security acceptance.
13. Bottom-layer security acceptance.
14. Tool permission matrix.
15. AI-friendly stack and workflow specification.
16. Implementation readiness audit.
17. Contract Impact Check for feature and fix work.
18. Project scaffold or implementation only after readiness passes.
19. Implementation Handoff for Bounded Feature Path or Local Fix Path.
20. First MVP slice implementation and verification.
21. Product MVP UI quality checked when the slice includes frontend UI.
22. Source-of-truth distillation into current-state docs, `docs/features/`, `docs/changes/`, `docs/decisions/`, or `docs/agent-project-kit/`.
23. First MVP slice completion signal with evidence.
24. MVP closure audit when the user asks whether the full documented MVP scope is complete, what remains, whether release is safe, or what to do next.
25. Formal Product Development Mode after Full MVP Scope Complete.

## Interaction Defaults

### Confirmation Prompt Rule

Any confirmation, consent, approval, or path-choice prompt must include plain-text options in the assistant message. Any task that asks for user confirmation must be answerable in ordinary text. Do not depend on UI buttons, `request_user_input`, AskUserQuestion, or host-specific quick actions.

### User Language Rule

Use the user's current language for questions, confirmations, progress updates, final answers, and milestone messages unless the user asks for another language. Always match the user's current language in all project-stage prompts.

## Task Routing

Use the lightest path that protects the project:

| Path | Use when | Required behavior |
| --- | --- | --- |
| Project Baseline Path | New project, missing core documents, technology stack choice, engineering baseline, security/tool/deployment setup. | Run staged clarification, reference scan, capability scan, document consent, and readiness gates before implementation. |
| Contract-Changing Feature Path | Feature or fix changes product behavior, frontend/API/database contracts, permissions, dependencies, deployment, tools, or operations. | Update affected current-state source-of-truth documents before implementation. |
| Bounded Feature Path | Approved baseline exists and the work stays inside documented contracts. | Read relevant docs, state that no source-of-truth update is needed, then hand off to implementation discipline. |
| Local Fix Path | Small bug fix, copy/style tweak, test fix, code explanation, single command, or other local task. | Skip the project baseline flow and use debugging, TDD, verification, or direct command execution. |

## Contract Impact Check

Before treating work as a Bounded Feature Path, check whether it changes:

- Frontend routes, pages, component responsibilities, UI states, interactions, data dependencies, source tree, ownership, or import boundaries.
- API endpoints, request/response contracts, validation, errors, permissions, backend workflows, integrations, workers, or data flow.
- Tables, fields, relations, indexes, enums, seeds, schemas, migrations, ownership, retention, or rollback.
- Frameworks, packages, scripts, repository layout, quality gates, deployment, environment variables, tool permissions, or operations.
- Security, privacy, production data, external writes, payments, secrets, privileged local access, or destructive operations.

If any item changes, use the Contract-Changing Feature Path.

## Optional Workflow Tool Fallback

Superpowers, OpenSpec, GitHub Spec Kit, issue trackers, and similar workflow tools are optional accelerators, not hard dependencies.

If available and applicable, use Superpowers-style planning, TDD, execution, review, and verification after this skill protects source-of-truth gates. Use OpenSpec, GitHub Spec Kit, issue specs, or chat plans as inputs unless the project explicitly declares one of them to be the primary source of truth.

If unavailable, do not block. Use the built-in fallback: clarify scope, run the Contract Impact Check, update source-of-truth docs only when contracts change, make the smallest useful implementation plan, implement, verify, and report evidence.

## Implementation Handoff

When the readiness gate has passed and the task is a Bounded Feature Path or Local Fix Path, do not rerun the full project baseline. Hand off to Superpowers if installed and applicable, another explicitly selected workflow if the user chose one, or the built-in fallback.

## Document Consent Gate

Do not create, copy, overwrite, move, or edit any project source-of-truth document until the user explicitly agrees to write that specific document or has directly asked for that exact document to be written. This includes `AGENTS.md`, every file under `docs/`, and any root-level planning document.

Before writing a document file:

1. Confirm the current stage artifact in conversation.
2. State the target path and what the document will contain.
3. Ask whether to write or update that file.
4. Wait for an affirmative answer.

Writing one source-of-truth document does not authorize another. Consent applies only to the named document and current stage. Writing `docs/project/PROJECT_CHARTER.md` does not imply permission to write `docs/architecture/TECH_STACK.md`, `AGENTS.md`, or engineering baseline files.

Batch consent is limited to the named document list and current stage. It is not permanent permission, does not cover future documents discovered later, and does not authorize implementation code, scaffolding, package manager files, UI pages, APIs, database schemas, migrations, or runnable behavior.

The agent may discuss, summarize, or propose a short outline in chat before consent, but must not create or modify document files before consent.

## Goal And Completion Signal

At the beginning of a project-level workflow, state the goal in plain language:

- Target outcome: the stage or project state the user wants to reach.
- Completion signal: the artifacts, confirmations, audits, or evidence that prove the goal is reached.
- Next action: the next question, document, audit, or implementation step.

For a new Product MVP, the default goal is: first MVP slice accepted after the project engineering baseline is ready. This has two milestones:

1. Project engineering baseline ready: the agent has clarified the project, created or confirmed the required source-of-truth documents, passed the implementation readiness audit, and received user confirmation to proceed.
2. First MVP slice complete: the agent has implemented one approved, user-verifiable product slice and returned fresh verification evidence.

After the first slice, use explicit lifecycle states: `MVP Scope Incomplete`, `Full MVP Scope Complete`, and `Release Ready`. Do not treat first MVP slice completion, full documented MVP completion, and release readiness as the same status.

Do not say the goal is complete just because a single document exists. Say the goal is complete only when the readiness gate has passed or the narrower user-specified goal has its completion evidence.

When the project engineering baseline is ready, close with a concise readiness message in the user's current language. Preserve the same meaning; do not force Chinese for non-Chinese users.

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

When the first MVP slice is complete, close with the second milestone message in the user's current language. For web products, the first MVP slice usually includes the first MVP page as the entry point, but the standard is the approved product slice, not a static page.

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

## Deliverable Checklist

- [ ] Reference project scan completed with concrete project links and selected direction
- [ ] Capability library scan completed with each required technical capability mapped to included, deferred, or rejected libraries
- [ ] `AGENTS.md`
- [ ] `docs/project/PROJECT_CHARTER.md`
- [ ] `docs/architecture/TECH_STACK.md`
- [ ] `docs/architecture/ENGINEERING_BASELINE.md`
- [ ] Git commit and remote backup rules
- [ ] Common skills or workflow templates
- [ ] `docs/architecture/FRONTEND_PLAN.md`
- [ ] `docs/architecture/DATABASE_DESIGN.md`
- [ ] `docs/architecture/BACKEND_SPEC.md`
- [ ] `docs/features/<feature-name>.md` when stable feature behavior should be findable by feature name
- [ ] `docs/changes/<date-or-id>-<change-name>.md` when one change needs proposal, design, tasks, or acceptance detail
- [ ] `docs/decisions/ADR-<number>-<topic>.md` when a long-term product or architecture decision is made
- [ ] `docs/agent-project-kit/PROCESS_ARTIFACTS.md` or subfolders when saving reference scans, capability scans, readiness audits, or handoffs
- [ ] Backend architecture acceptance report
- [ ] Backend security boundary table
- [ ] Bottom-layer security checklist
- [ ] `docs/ops/TOOL_POLICY.md`
- [ ] `docs/workflow/AI_WORKFLOW.md`
- [ ] `docs/ops/DEPLOYMENT.md`
- [ ] Implementation readiness audit passed
- [ ] Product MVP UI quality checked for frontend work
- [ ] First MVP slice implemented and verified
- [ ] Minimal backend skeleton run evidence
- [ ] Testing and quality check scripts

## Implementation Readiness Gate

Before creating a project scaffold, package manager files, `apps/`, `packages/`, UI screens, API controllers, database schemas, migrations, or runnable behavior, confirm that the relevant source-of-truth documents exist and match the requested product shape.

For a Product MVP that includes web UI, backend, database, local execution, deployment, or AI-assisted workflow, do not start implementation until these are present or explicitly declared not applicable:

- `AGENTS.md`
- `docs/project/PROJECT_CHARTER.md`
- `docs/architecture/TECH_STACK.md`
- `docs/architecture/ENGINEERING_BASELINE.md`
- `docs/architecture/FRONTEND_PLAN.md`
- `docs/architecture/DATABASE_DESIGN.md`
- `docs/architecture/BACKEND_SPEC.md`
- `docs/workflow/AI_WORKFLOW.md`
- `docs/ops/TOOL_POLICY.md`
- `docs/ops/DEPLOYMENT.md`

If documents are missing, output a short stage-aware readiness audit. Name the current stage, identify only the missing documents that directly unblock the next stage, explain why each one matters now, and offer two choices:

1. Steady path: create or update the single most important next document, then review it before continuing.
2. Accelerated path: ask for consent to create or update the named missing batch for this stage, then run the implementation readiness audit.

Use plain-text options, for example `A. Steady path` and `B. Accelerated path`. Do not depend on UI buttons or host-specific quick actions. Each option must name the exact document paths it covers.

Do not proceed to code.

After creating or updating any readiness document, rerun the readiness audit summary before moving to implementation.

For frontend work, also verify that `docs/architecture/FRONTEND_PLAN.md` includes the Product MVP UI Quality Gate: Design Read, Design Dials, design system tokens, UI component strategy, state and interaction contract, responsive and accessibility expectations, anti-slop guardrails, and browser UI quality verification. If these are missing, update the frontend plan before code.

For Bounded Feature Path or Local Fix Path work, do not rerun this full readiness audit if the project baseline has already passed and the Contract Impact Check finds no contract changes. Read the relevant docs, state the bounded classification, and proceed through the Implementation Handoff.

## Reference Project Scan Prompt

```text
Before refining this idea into a project charter, scan for 3-7 concrete reference projects, products, repositories, plugins, templates, or adjacent implementations. Include project name, direct link, source type, what to borrow, what not to copy blindly, and how each reference changes the possible MVP direction. Then offer 2-4 direction choices grounded in those links and ask me to choose, combine, or reject a direction. Do not move to project purpose confirmation, tech stack, or implementation planning until I choose a direction.
```

## Capability Library Scan Prompt

```text
Before confirming the technology stack, extract the required technical capabilities from the confirmed project charter. For each capability, research mature, open-source or inspectable, actively maintained third-party libraries that fit this project. Include capability, library name, direct link, ecosystem, open-source or inspectability status, maintenance evidence, why it fits or does not fit, risk or lock-in note, and decision: Included, Deferred, or Rejected. Then present one combined recommendation: core stack plus project-needed third-party libraries. Do not write docs/architecture/TECH_STACK.md, install packages, or scaffold code until I confirm the combined stack and library set.
```

## UI Quality Gate Prompt

```text
Before frontend implementation, update or audit docs/architecture/FRONTEND_PLAN.md for the Product MVP UI Quality Gate. Include a Design Read, Design Dials, design system tokens, UI component strategy, state and interaction contract, responsive rules, accessibility expectations, anti-slop guardrails, and browser UI quality verification. Do not apply landing-page taste rules blindly to dashboards, admin panels, data tables, or multi-step product UI. For the first MVP page, require loading, empty, error, success, disabled, saving, focus, hover, active, desktop, and mobile behavior where relevant. Do not write UI code until the plan covers these items.
```

When the readiness gate and approved engineering setup are complete, close with a short welcome message in the user's current language. For example, in Chinese: "欢迎进入你的项目工程基线：当前项目工程搭建完毕，文档、技术路线和基础门禁已就位。下一步可以从第一个已批准的产品闭环开始实现。" In English: "Welcome to your project engineering baseline: the core documents, technical route, and readiness gates are in place. Next, start with the first approved product loop."

## Source-of-Truth Change Gate

Before implementing a change that alters design or contracts, update the original project document first:

- Frontend routes, components, states, data dependencies, or interactions: `docs/architecture/FRONTEND_PLAN.md`.
- Frontend source tree, file responsibilities, component split rules, shared UI location, state/config/i18n/utils ownership, or import boundaries: `docs/architecture/FRONTEND_PLAN.md`.
- APIs, validation, response/error contracts, permissions, backend workflows, integrations, or data flow: `docs/architecture/BACKEND_SPEC.md`.
- Tables, fields, relations, indexes, enums, schema, migrations, ownership, retention, or rollback: `docs/architecture/DATABASE_DESIGN.md`.
- Stack, dependencies, scripts, deployment, environment, tools, or operations: the relevant tech stack, engineering baseline, deployment, or tool policy document.

OpenSpec, GitHub Spec Kit, issue specs, and chat plans can guide the change, but they do not replace the repository source-of-truth documents unless the user explicitly changes that rule. If implementation reveals a design change, stop and update the affected document before continuing code.

## Source-of-Truth Distillation Gate

Core source-of-truth documents describe the current system contract, not the full history of how the project got there.

- Distill durable product, architecture, API, database, permission, deployment, and tool contracts into the relevant core document.
- Put stable feature behavior in `docs/features/<feature-name>.md`.
- Put one change's proposal, design notes, tasks, acceptance notes, and temporary context in `docs/changes/<date-or-id>-<change-name>.md`.
- Put long-term product or architecture decisions in `docs/decisions/ADR-<number>-<topic>.md`.
- Put Agent Project Kit process artifacts in `docs/agent-project-kit/`.
- Archive or remove obsolete detail after it is no longer the current contract.

After implementation, distill only durable results back into core current-state docs. Keep process-heavy detail in `docs/changes/`.

## Common Mistakes

| Mistake | Correction |
| --- | --- |
| Asking AI to code before scope is clear | Create or update the project charter first. |
| Listing vague competitor categories during initiation | Run a Reference Project Scan Gate with project name, direct link, lessons, cautions, and direction choices. |
| Planning implementation before confirming project purpose | Summarize the target user, problem, product role, and MVP; wait for user confirmation. |
| Confirming a stack without library research | Run a Capability Library Scan Gate and review project-needed third-party libraries with links, maintenance evidence, and include/defer/reject decisions. |
| Starting a scaffold after only a charter, stack, and engineering baseline | Run the Project Specification Readiness Gate and create frontend, database, backend, workflow, tool policy, deployment, and Agent rule documents as applicable before implementation. |
| Treating frontend directory structure as cleanup after code generation | Define the frontend engineering contract in `docs/architecture/FRONTEND_PLAN.md` before writing UI code, then implement against it. |
| Putting UI, config, messages, state, icons, mock data, and utilities into one route or app file | Split code by route composition, shared UI, business components, config, i18n, state, assets, and capability-scoped utilities. |
| Treating default stack suggestions as mandatory | Use defaults as candidates; document why the project needs a single package, workspace, UI library, icon library, backend, or database before locking it. |
| Letting code, migrations, or APIs become the first record of a design change | Update the original source-of-truth document first, then implement against it. |
| Rerunning the whole baseline for a bounded feature | Run the Contract Impact Check, then use the Implementation Handoff when no contract changes are needed. |
| Turning source-of-truth docs into change journals | Distill current contracts into core docs and keep feature/change/process detail in `docs/features/`, `docs/changes/`, `docs/decisions/`, or `docs/agent-project-kit/`. |
| Treating first MVP slice, full MVP scope, and release readiness as the same status | Use lifecycle states and the MVP Closure Sentinel before claiming Full MVP Scope Complete or Release Ready. |

## Default Product MVP Stack

Use as a default for ordinary individual or small-team web products unless project constraints justify another route. Product MVP means narrow feature scope, not a disposable foundation.

| Layer | Default | Role |
| --- | --- | --- |
| Repository | Single package or workspace, chosen from real boundaries | one deployable frontend app can stay single-package; use `apps/*` and `packages/*` only for real app/shared-package ownership |
| Frontend | Next.js + TypeScript | pages, routing, SSR/full-stack entry |
| Styling | Tailwind CSS | consistent styling constraints |
| UI | shadcn/ui or project-approved design-system strategy | readable, editable defaults; replace when design source or platform conventions justify it |
| Icons | lucide-react or project-approved icon family | consistent icon language; replace when Figma/Stitch/brand/system icons are the real baseline |
| Charts | Recharts or Apache ECharts | business charts and advanced visualization |
| Backend | NestJS for independent APIs; Next.js route handlers/server actions for same-app light backend | modules, APIs, services, permission and validation boundaries |
| Database | PostgreSQL or Supabase/Postgres | relational data, auth/storage acceleration when needed |
| Migrations | Prisma or Drizzle migrations | schema evolution, rollback planning, team visibility |
| Frontend deploy | Vercel | Next.js-friendly deployment |
| Backend deploy | Railway, Render, Fly.io, or Docker | Node service hosting and operations control |
| Quality | ESLint, Prettier, EditorConfig, TypeScript, CI | repeatable code quality |
| Checks | pnpm check, pnpm test, pnpm build, Vitest, React Testing Library, Playwright | quality gate, unit, component, and browser evidence |
| AI discipline | Superpowers or built-in fallback | clarify, plan, implement, verify; Superpowers is optional, not a hard dependency |
| Spec management | OpenSpec, GitHub Spec Kit, or repo docs | durable requirements, design, tasks, acceptance; external spec tools are optional inputs unless explicitly primary |
| AI app SDK | Vercel AI SDK, OpenAI Agents SDK, LangGraph, Dify, n8n | chat, agents, workflows, automation by scenario |

Rule: mature technology reduces AI error rate; workflow discipline constrains execution; tests, browser checks, API checks, builds, and deploy logs form the evidence chain. Defaults are candidates, not mandates: repository shape, UI library, and icon library must be justified by product shape, design-system evidence, implementation boundaries, and migration cost.

SQLite, local JSON files, ad hoc SQL files, and no-migration setups are allowed only for explicit local-first or throwaway prototypes.

## TECH_STACK.md Prompt

```text
Based on the project charter, target users, scope, budget, launch time, and team capability, recommend exactly one Product MVP tech stack for docs/architecture/TECH_STACK.md. Before confirming the stack, run a capability library scan: map required technical capabilities to mature, open-source or inspectable, actively maintained third-party libraries with direct links, maintenance evidence, include/defer/reject decisions, risks, and license notes. Cover architecture track, repository shape, frontend framework, UI library, icon library, chart library, backend framework, database, migrations, deployment platform, AI SDK, and AI workflow discipline. Explain production compatibility, migration cost, choices, rejected alternatives, risks, and re-evaluation triggers.
```

## AI_WORKFLOW.md Prompt

```text
Generate docs/workflow/AI_WORKFLOW.md for this project. Combine Superpowers-style discipline with spec-first work. Define how AI should clarify requirements, write specs, design, split tasks, implement, test, accept, and archive. Mark which steps require human confirmation and which situations forbid direct coding.
Include Optional Workflow Tool Fallback: if Superpowers, OpenSpec, GitHub Spec Kit, or similar tools are unavailable, use the project's built-in clarify, Contract Impact Check, source-of-truth update, plan, implement, verify, and evidence workflow instead of blocking.
```

## DEPLOYMENT.md Prompt

```text
Based on the current stack, generate docs/ops/DEPLOYMENT.md. Cover local run, test environment, production environment, frontend deployment, backend deployment, database, environment variables, logs, rollback, health checks, and pre-launch acceptance checklist.
```

## Implementation Readiness Prompt

```text
Audit implementation readiness before creating code. Check AGENTS.md, PROJECT_CHARTER.md, TECH_STACK.md, ENGINEERING_BASELINE.md, FRONTEND_PLAN.md, DATABASE_DESIGN.md, BACKEND_SPEC.md, AI_WORKFLOW.md, TOOL_POLICY.md, and DEPLOYMENT.md. For frontend work, verify that FRONTEND_PLAN.md includes the frontend source tree, file responsibilities, component split rules, state/config/i18n/utils ownership, import boundaries, Design Read, Design Dials, Product MVP UI Quality Gate, design system tokens, state and interaction contract, responsive/accessibility rules, anti-slop guardrails, and browser UI quality verification. State the current stage, list present documents, and list only the missing documents that directly unblock the next stage. Explain why each missing document matters now. If anything required is missing, offer plain-text options: `A. Steady path` for the single most important next document, or `B. Accelerated path` for the named missing batch. Do not depend on UI buttons. Do not scaffold or implement yet.
```

## Source-of-Truth Change Prompt

```text
Before implementing this change, identify whether it changes frontend design, frontend source tree, component boundaries, state/config/i18n/utils ownership, API/backend contracts, database shape, permissions, stack, deployment, tools, or operations. If it does, update the affected original source-of-truth document first, ask for confirmation when required, then implement code strictly against the updated document. Treat OpenSpec or other spec artifacts as auxiliary inputs unless the project explicitly declares them as source of truth.
If the change is bounded by existing approved contracts, state that it is a Bounded Feature Path and use the Implementation Handoff. If process detail would bloat current-state docs, put it in `docs/changes/`, `docs/features/`, `docs/decisions/`, or `docs/agent-project-kit/` and distill only durable contract changes back into core docs.
```

## Goal Contract Prompt

```text
Before continuing, state the current goal, the completion signal, and the next action. For a new Product MVP, use two milestones by default: project engineering baseline ready, then first MVP slice complete with evidence. When a milestone is satisfied, explicitly say so. If the project engineering baseline is ready, finish with the language-adaptive baseline message. If the first MVP slice is implemented and verified, finish with the language-adaptive first MVP slice message.
```

## MVP Closure Prompt

```text
Audit whether the current implementation satisfies the full documented MVP scope. Read the relevant source-of-truth documents, especially PROJECT_CHARTER.md and any frontend, backend, database, deployment, workflow, tool, or security docs that define MVP obligations. Classify each must-have and acceptance criterion as Met, Partially met, Missing, Deferred/non-goal, or Accepted risk. Classify remaining risks as blocking, non-blocking, or needing a user decision. Return one lifecycle state: MVP Scope Incomplete, Full MVP Scope Complete, or Release Ready. If incomplete, do not use a celebration message; end with remaining risks and one next step recommendation. If Full MVP Scope Complete, say the documented MVP scope is complete and recommend Formal Product Development Mode: release validation, architecture hardening, user feedback, and the next planned version. If Release Ready, include deployment, environment, regression, security, rollback, and operations evidence.
```

## Testing Scripts Prompt

```text
Based on the current stack, generate a testing and quality-check plan for docs/architecture/ENGINEERING_BASELINE.md. Output package.json scripts for typecheck, lint, format:check, test, test:watch, e2e, build, check, check:unit, check:full, and check:e2e when applicable. Define whether pnpm check is the minimal entry or full quality gate, and explain which test layer Vitest, React Testing Library, Playwright, or Jest covers. Finish with rules that can be referenced from AGENTS.md.
```

## Anti-Drift Prompt

```text
Before implementing, read AGENTS.md, docs/project/PROJECT_CHARTER.md, docs/architecture/TECH_STACK.md, docs/architecture/ENGINEERING_BASELINE.md, docs/architecture/FRONTEND_PLAN.md, docs/architecture/DATABASE_DESIGN.md, docs/architecture/BACKEND_SPEC.md, docs/workflow/AI_WORKFLOW.md, docs/ops/TOOL_POLICY.md, and docs/ops/DEPLOYMENT.md. Unless you provide a clear reason and receive confirmation, do not introduce a new frontend framework, UI library, icon library, state library, backend framework, database, deployment platform, package manager, repository shape, or AI workflow tool. If the task changes frontend source tree, component boundaries, state/config/i18n/utils ownership, frontend UI quality gate, frontend/API/database/permission/operation design, update the affected source-of-truth document before code. For frontend work, return browser UI quality evidence for desktop and mobile along with test/build evidence. After finishing, provide changed-doc summary plus test, build, browser, API, or deployment evidence.
If the task is bounded by existing approved contracts, say so and use the Implementation Handoff instead of rerunning the full baseline. Store feature/change/process detail in `docs/features/`, `docs/changes/`, `docs/decisions/`, or `docs/agent-project-kit/` when it would bloat current-state docs.
```
