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

## Deliverable Checklist

- [ ] `PROJECT_CHARTER.md`
- [ ] `TECH_STACK.md`
- [ ] Git commit and remote backup rules
- [ ] `AGENTS.md` or Agent constitution
- [ ] Common skills or workflow templates
- [ ] Frontend page and component inventory
- [ ] `DATABASE_DESIGN.md`
- [ ] `BACKEND_SPEC.md`
- [ ] Minimal backend skeleton run evidence
- [ ] Backend architecture acceptance report
- [ ] Backend security boundary table
- [ ] Bottom-layer security checklist
- [ ] `TOOL_POLICY.md`
- [ ] `AI_WORKFLOW.md`
- [ ] `DEPLOYMENT.md`
- [ ] Testing and quality check scripts

## Default AI-Friendly Stack

Use as a default for ordinary individual or small-team web projects unless project constraints justify another route.

| Layer | Default | Role |
| --- | --- | --- |
| Frontend | Next.js + TypeScript | pages, routing, SSR/full-stack entry |
| Styling | Tailwind CSS | consistent styling constraints |
| UI | shadcn/ui | readable, editable, AI-friendly component source |
| Icons | lucide-react | consistent icon language |
| Charts | Recharts or Apache ECharts | business charts and advanced visualization |
| Backend | NestJS | modules, APIs, services, permission and validation boundaries |
| Database | PostgreSQL or Supabase | relational data, auth/storage acceleration when needed |
| Frontend deploy | Vercel | Next.js-friendly deployment |
| Backend deploy | Railway, Render, Fly.io, or Docker | Node service hosting and operations control |
| Checks | pnpm check, pnpm test, pnpm build, Vitest, React Testing Library, Playwright | quality gate, unit, component, and browser evidence |
| AI discipline | Superpowers | clarify, plan, implement, verify |
| Spec management | OpenSpec or GitHub Spec Kit | durable requirements, design, tasks, acceptance |
| AI app SDK | Vercel AI SDK, OpenAI Agents SDK, LangGraph, Dify, n8n | chat, agents, workflows, automation by scenario |

Rule: mature technology reduces AI error rate; workflow discipline constrains execution; tests, browser checks, API checks, builds, and deploy logs form the evidence chain.

## TECH_STACK.md Prompt

```text
Based on the project charter, target users, scope, budget, launch time, and team capability, recommend exactly one AI-friendly tech stack. Cover frontend framework, UI library, icon library, chart library, backend framework, database, deployment platform, AI SDK, and AI workflow discipline. Explain choices, rejected alternatives, risks, and which project documents must record these decisions.
```

## AI_WORKFLOW.md Prompt

```text
Generate AI_WORKFLOW.md for this project. Combine Superpowers-style discipline with spec-first work. Define how AI should clarify requirements, write specs, design, split tasks, implement, test, accept, and archive. Mark which steps require human confirmation and which situations forbid direct coding.
```

## DEPLOYMENT.md Prompt

```text
Based on the current stack, generate DEPLOYMENT.md. Cover local run, test environment, production environment, frontend deployment, backend deployment, database, environment variables, logs, rollback, health checks, and pre-launch acceptance checklist.
```

## Testing Scripts Prompt

```text
Based on the current stack, generate a testing and quality-check plan. Output package.json scripts for typecheck, lint, test, test:watch, e2e, build, check, check:unit, check:full, and check:e2e when applicable. Define whether pnpm check is the minimal entry or full quality gate, and explain which test layer Vitest, React Testing Library, Playwright, or Jest covers. Finish with rules that can be written into TESTING.md and AGENTS.md.
```

## Anti-Drift Prompt

```text
Before implementing, read TECH_STACK.md, AI_WORKFLOW.md, TOOL_POLICY.md, and AGENTS.md. Unless you provide a clear reason and receive confirmation, do not introduce a new frontend framework, UI library, state library, backend framework, database, deployment platform, or AI workflow tool. After finishing, provide test, build, browser, API, or deployment evidence.
```
