# Workflow Checklists

Use this reference for the whole AI programming roadmap, deliverable tracking, default AI-friendly stack, and reusable workflow prompts.

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
17. Project scaffold or implementation only after readiness passes.
18. First MVP slice implementation and verification.
19. First MVP slice completion signal with evidence.

## Interaction Defaults

### Confirmation Prompt Rule

Any confirmation, consent, approval, or path-choice prompt must include plain-text options in the assistant message. Do not depend on UI buttons, `request_user_input`, AskUserQuestion, or host-specific quick actions.

### User Language Rule

Use the user's current language for questions, confirmations, progress updates, final answers, and milestone messages unless the user asks for another language.

## Goal And Completion Signal

At the beginning of a project-level workflow, state the goal in plain language:

- Target outcome: the stage or project state the user wants to reach.
- Completion signal: the artifacts, confirmations, audits, or evidence that prove the goal is reached.
- Next action: the next question, document, audit, or implementation step.

For a new Product MVP, the default goal is: first MVP slice accepted after the project engineering baseline is ready. This has two milestones:

1. Project engineering baseline ready: the agent has clarified the project, created or confirmed the required source-of-truth documents, passed the implementation readiness audit, and received user confirmation to proceed.
2. First MVP slice complete: the agent has implemented one approved, user-verifiable product slice and returned fresh verification evidence.

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
- [ ] Backend architecture acceptance report
- [ ] Backend security boundary table
- [ ] Bottom-layer security checklist
- [ ] `docs/ops/TOOL_POLICY.md`
- [ ] `docs/workflow/AI_WORKFLOW.md`
- [ ] `docs/ops/DEPLOYMENT.md`
- [ ] Implementation readiness audit passed
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

## Reference Project Scan Prompt

```text
Before refining this idea into a project charter, scan for 3-7 concrete reference projects, products, repositories, plugins, templates, or adjacent implementations. Include project name, direct link, source type, what to borrow, what not to copy blindly, and how each reference changes the possible MVP direction. Then offer 2-4 direction choices grounded in those links and ask me to choose, combine, or reject a direction. Do not move to project purpose confirmation, tech stack, or implementation planning until I choose a direction.
```

## Capability Library Scan Prompt

```text
Before confirming the technology stack, extract the required technical capabilities from the confirmed project charter. For each capability, research mature, open-source or inspectable, actively maintained third-party libraries that fit this project. Include capability, library name, direct link, ecosystem, open-source or inspectability status, maintenance evidence, why it fits or does not fit, risk or lock-in note, and decision: Included, Deferred, or Rejected. Then present one combined recommendation: core stack plus project-needed third-party libraries. Do not write docs/architecture/TECH_STACK.md, install packages, or scaffold code until I confirm the combined stack and library set.
```

When the readiness gate and approved engineering setup are complete, close with a short welcome message in the user's current language. For example, in Chinese: "欢迎进入你的项目工程基线：当前项目工程搭建完毕，文档、技术路线和基础门禁已就位。下一步可以从第一个已批准的产品闭环开始实现。" In English: "Welcome to your project engineering baseline: the core documents, technical route, and readiness gates are in place. Next, start with the first approved product loop."

## Source-of-Truth Change Gate

Before implementing a change that alters design or contracts, update the original project document first:

- Frontend routes, components, states, data dependencies, or interactions: `docs/architecture/FRONTEND_PLAN.md`.
- APIs, validation, response/error contracts, permissions, backend workflows, integrations, or data flow: `docs/architecture/BACKEND_SPEC.md`.
- Tables, fields, relations, indexes, enums, schema, migrations, ownership, retention, or rollback: `docs/architecture/DATABASE_DESIGN.md`.
- Stack, dependencies, scripts, deployment, environment, tools, or operations: the relevant tech stack, engineering baseline, deployment, or tool policy document.

OpenSpec, GitHub Spec Kit, issue specs, and chat plans can guide the change, but they do not replace the repository source-of-truth documents unless the user explicitly changes that rule. If implementation reveals a design change, stop and update the affected document before continuing code.

## Default Product MVP Stack

Use as a default for ordinary individual or small-team web products unless project constraints justify another route. Product MVP means narrow feature scope, not a disposable foundation.

| Layer | Default | Role |
| --- | --- | --- |
| Repository | pnpm workspace with `apps/*`, `packages/*`, `docs/*` | mature monorepo shape without forcing heavy tooling |
| Frontend | Next.js + TypeScript | pages, routing, SSR/full-stack entry |
| Styling | Tailwind CSS | consistent styling constraints |
| UI | shadcn/ui | readable, editable, AI-friendly component source |
| Icons | lucide-react | consistent icon language |
| Charts | Recharts or Apache ECharts | business charts and advanced visualization |
| Backend | NestJS for independent APIs; Next.js route handlers/server actions for same-app light backend | modules, APIs, services, permission and validation boundaries |
| Database | PostgreSQL or Supabase/Postgres | relational data, auth/storage acceleration when needed |
| Migrations | Prisma or Drizzle migrations | schema evolution, rollback planning, team visibility |
| Frontend deploy | Vercel | Next.js-friendly deployment |
| Backend deploy | Railway, Render, Fly.io, or Docker | Node service hosting and operations control |
| Quality | ESLint, Prettier, EditorConfig, TypeScript, CI | repeatable code quality |
| Checks | pnpm check, pnpm test, pnpm build, Vitest, React Testing Library, Playwright | quality gate, unit, component, and browser evidence |
| AI discipline | Superpowers | clarify, plan, implement, verify |
| Spec management | OpenSpec or GitHub Spec Kit | durable requirements, design, tasks, acceptance |
| AI app SDK | Vercel AI SDK, OpenAI Agents SDK, LangGraph, Dify, n8n | chat, agents, workflows, automation by scenario |

Rule: mature technology reduces AI error rate; workflow discipline constrains execution; tests, browser checks, API checks, builds, and deploy logs form the evidence chain.

SQLite, local JSON files, ad hoc SQL files, and no-migration setups are allowed only for explicit local-first or throwaway prototypes.

## TECH_STACK.md Prompt

```text
Based on the project charter, target users, scope, budget, launch time, and team capability, recommend exactly one Product MVP tech stack for docs/architecture/TECH_STACK.md. Before confirming the stack, run a capability library scan: map required technical capabilities to mature, open-source or inspectable, actively maintained third-party libraries with direct links, maintenance evidence, include/defer/reject decisions, risks, and license notes. Cover architecture track, repository shape, frontend framework, UI library, icon library, chart library, backend framework, database, migrations, deployment platform, AI SDK, and AI workflow discipline. Explain production compatibility, migration cost, choices, rejected alternatives, risks, and re-evaluation triggers.
```

## AI_WORKFLOW.md Prompt

```text
Generate docs/workflow/AI_WORKFLOW.md for this project. Combine Superpowers-style discipline with spec-first work. Define how AI should clarify requirements, write specs, design, split tasks, implement, test, accept, and archive. Mark which steps require human confirmation and which situations forbid direct coding.
```

## DEPLOYMENT.md Prompt

```text
Based on the current stack, generate docs/ops/DEPLOYMENT.md. Cover local run, test environment, production environment, frontend deployment, backend deployment, database, environment variables, logs, rollback, health checks, and pre-launch acceptance checklist.
```

## Implementation Readiness Prompt

```text
Audit implementation readiness before creating code. Check AGENTS.md, PROJECT_CHARTER.md, TECH_STACK.md, ENGINEERING_BASELINE.md, FRONTEND_PLAN.md, DATABASE_DESIGN.md, BACKEND_SPEC.md, AI_WORKFLOW.md, TOOL_POLICY.md, and DEPLOYMENT.md. State the current stage, list present documents, and list only the missing documents that directly unblock the next stage. Explain why each missing document matters now. If anything required is missing, offer plain-text options: `A. Steady path` for the single most important next document, or `B. Accelerated path` for the named missing batch. Do not depend on UI buttons. Do not scaffold or implement yet.
```

## Source-of-Truth Change Prompt

```text
Before implementing this change, identify whether it changes frontend design, API/backend contracts, database shape, permissions, stack, deployment, tools, or operations. If it does, update the affected original source-of-truth document first, ask for confirmation when required, then implement code strictly against the updated document. Treat OpenSpec or other spec artifacts as auxiliary inputs unless the project explicitly declares them as source of truth.
```

## Goal Contract Prompt

```text
Before continuing, state the current goal, the completion signal, and the next action. For a new Product MVP, use two milestones by default: project engineering baseline ready, then first MVP slice complete with evidence. When a milestone is satisfied, explicitly say so. If the project engineering baseline is ready, finish with the language-adaptive baseline message. If the first MVP slice is implemented and verified, finish with the language-adaptive first MVP slice message.
```

## Testing Scripts Prompt

```text
Based on the current stack, generate a testing and quality-check plan for docs/architecture/ENGINEERING_BASELINE.md. Output package.json scripts for typecheck, lint, format:check, test, test:watch, e2e, build, check, check:unit, check:full, and check:e2e when applicable. Define whether pnpm check is the minimal entry or full quality gate, and explain which test layer Vitest, React Testing Library, Playwright, or Jest covers. Finish with rules that can be referenced from AGENTS.md.
```

## Anti-Drift Prompt

```text
Before implementing, read AGENTS.md, docs/project/PROJECT_CHARTER.md, docs/architecture/TECH_STACK.md, docs/architecture/ENGINEERING_BASELINE.md, docs/architecture/FRONTEND_PLAN.md, docs/architecture/DATABASE_DESIGN.md, docs/architecture/BACKEND_SPEC.md, docs/workflow/AI_WORKFLOW.md, docs/ops/TOOL_POLICY.md, and docs/ops/DEPLOYMENT.md. Unless you provide a clear reason and receive confirmation, do not introduce a new frontend framework, UI library, state library, backend framework, database, deployment platform, or AI workflow tool. If the task changes frontend/API/database/permission/operation design, update the affected source-of-truth document before code. After finishing, provide changed-doc summary plus test, build, browser, API, or deployment evidence.
```
