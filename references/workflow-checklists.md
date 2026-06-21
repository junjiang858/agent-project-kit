# Workflow Checklists

Use this reference for the whole AI programming roadmap, deliverable tracking, default AI-friendly stack, and reusable workflow prompts.

## Project Roadmap

1. Cognition calibration.
2. Project initiation.
3. Technology selection.
4. Git version safety.
5. Agent constitution.
6. Skill workflow.
7. Frontend/backend/database technical understanding.
8. Frontend skeleton and database design.
9. Backend business spec and minimal backend skeleton.
10. Backend architecture acceptance.
11. Backend security acceptance.
12. Bottom-layer security acceptance.
13. Tool permission matrix.
14. AI-friendly stack and workflow specification.
15. Implementation readiness audit.
16. Project scaffold or implementation only after readiness passes.

## Goal And Completion Signal

At the beginning of a project-level workflow, state the goal in plain language:

- Target outcome: the stage or project state the user wants to reach.
- Completion signal: the artifacts, confirmations, audits, or evidence that prove the goal is reached.
- Next action: the next question, document, audit, or implementation step.

For a new Product MVP, the default goal is: project engineering baseline ready. This means the agent has clarified the project, created or confirmed the required source-of-truth documents, passed the implementation readiness audit, and received user confirmation to proceed.

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

## Deliverable Checklist

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

If documents are missing, output a short readiness audit and ask whether to create the next missing document or the named missing batch. Do not proceed to code.

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
Based on the project charter, target users, scope, budget, launch time, and team capability, recommend exactly one Product MVP tech stack for docs/architecture/TECH_STACK.md. Cover architecture track, repository shape, frontend framework, UI library, icon library, chart library, backend framework, database, migrations, deployment platform, AI SDK, and AI workflow discipline. Explain production compatibility, migration cost, choices, rejected alternatives, risks, and re-evaluation triggers.
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
Audit implementation readiness before creating code. Check AGENTS.md, PROJECT_CHARTER.md, TECH_STACK.md, ENGINEERING_BASELINE.md, FRONTEND_PLAN.md, DATABASE_DESIGN.md, BACKEND_SPEC.md, AI_WORKFLOW.md, TOOL_POLICY.md, and DEPLOYMENT.md. List present and missing documents. If anything required is missing, ask whether to create the next missing document and do not scaffold or implement yet.
```

## Source-of-Truth Change Prompt

```text
Before implementing this change, identify whether it changes frontend design, API/backend contracts, database shape, permissions, stack, deployment, tools, or operations. If it does, update the affected original source-of-truth document first, ask for confirmation when required, then implement code strictly against the updated document. Treat OpenSpec or other spec artifacts as auxiliary inputs unless the project explicitly declares them as source of truth.
```

## Goal Contract Prompt

```text
Before continuing, state the current goal, the completion signal, and the next action. When the completion signal is satisfied, explicitly say the goal is achieved. If the project engineering baseline is ready, finish with the language-adaptive readiness message.
```

## Testing Scripts Prompt

```text
Based on the current stack, generate a testing and quality-check plan for docs/architecture/ENGINEERING_BASELINE.md. Output package.json scripts for typecheck, lint, format:check, test, test:watch, e2e, build, check, check:unit, check:full, and check:e2e when applicable. Define whether pnpm check is the minimal entry or full quality gate, and explain which test layer Vitest, React Testing Library, Playwright, or Jest covers. Finish with rules that can be referenced from AGENTS.md.
```

## Anti-Drift Prompt

```text
Before implementing, read AGENTS.md, docs/project/PROJECT_CHARTER.md, docs/architecture/TECH_STACK.md, docs/architecture/ENGINEERING_BASELINE.md, docs/architecture/FRONTEND_PLAN.md, docs/architecture/DATABASE_DESIGN.md, docs/architecture/BACKEND_SPEC.md, docs/workflow/AI_WORKFLOW.md, docs/ops/TOOL_POLICY.md, and docs/ops/DEPLOYMENT.md. Unless you provide a clear reason and receive confirmation, do not introduce a new frontend framework, UI library, state library, backend framework, database, deployment platform, or AI workflow tool. If the task changes frontend/API/database/permission/operation design, update the affected source-of-truth document before code. After finishing, provide changed-doc summary plus test, build, browser, API, or deployment evidence.
```
