# AGENTS

## Project Goal

- 

## Project Documents

Read these before implementation:

1. `docs/project/PROJECT_CHARTER.md`
2. `docs/architecture/TECH_STACK.md`
3. `docs/architecture/ENGINEERING_BASELINE.md`
4. `docs/workflow/AI_WORKFLOW.md`
5. `docs/ops/TOOL_POLICY.md`

Read task-specific docs when relevant:

- Frontend: `docs/architecture/FRONTEND_PLAN.md`
- Backend/API: `docs/architecture/BACKEND_SPEC.md`
- Database: `docs/architecture/DATABASE_DESIGN.md`
- Deployment: `docs/ops/DEPLOYMENT.md`
- Stable feature behavior: `docs/features/`
- One-change proposal, design, tasks, and acceptance detail: `docs/changes/`
- Long-term product or architecture decisions: `docs/decisions/`
- Agent Project Kit process artifacts: `docs/agent-project-kit/`

## Source of Truth

1. User instruction
2. `docs/project/PROJECT_CHARTER.md`
3. `docs/architecture/TECH_STACK.md`
4. `docs/architecture/ENGINEERING_BASELINE.md`
5. `docs/ops/TOOL_POLICY.md`
6. Current-state feature, backend, frontend, database, deployment, and tool docs under `docs/`
7. Existing code conventions

## Working Rules

- Clarify scope before implementation.
- Run a Contract Impact Check before feature or fix work. If the change affects product behavior, frontend/API/database contracts, permissions, dependencies, deployment, tools, or operations, update the relevant source-of-truth document before code.
- For Bounded Feature Path or Local Fix Path work that stays inside approved contracts, state that no source-of-truth update is needed and proceed through the approved implementation discipline.
- Preserve the documented tech stack.
- Keep detailed project documents under `docs/`; keep this file short as the root index.
- Update the relevant source-of-truth document before code when design, API, database, permission, deployment, tool, or operational behavior changes.
- Keep current-state source-of-truth docs compact. Put stable feature behavior in `docs/features/`, one-change process detail in `docs/changes/`, long-term decisions in `docs/decisions/`, and Agent Project Kit process artifacts in `docs/agent-project-kit/`.
- Superpowers, OpenSpec, GitHub Spec Kit, and similar workflow tools are optional accelerators unless this project explicitly declares one as primary. If unavailable, use the built-in clarify, Contract Impact Check, plan, implement, verify, and evidence workflow instead of blocking.
- For frontend work, follow `docs/architecture/FRONTEND_PLAN.md` for source tree, file responsibilities, component split rules, state/config/i18n/utils ownership, and import boundaries before editing UI code.
- For frontend work, also follow the Product MVP UI Quality Gate in `docs/architecture/FRONTEND_PLAN.md`: Design Read, design system tokens, state and interaction contract, responsive/accessibility expectations, anti-slop guardrails, and browser UI quality verification.
- Keep changes small and reviewable.
- Use existing patterns before adding abstractions.
- Preserve the approved repository shape, UI library, and icon library unless the source-of-truth documents are updated and the user approves the change.
- Never put secrets in code or Git history.

## Interaction Defaults

### Confirmation Prompt Rule

Any request for confirmation, consent, approval, or a path choice must include plain-text options in the assistant message. Do not rely only on UI buttons, `request_user_input`, AskUserQuestion, or host-specific quick actions. State what each option authorizes before waiting for the user's reply.

### User Language Rule

Use the user's current language for questions, confirmations, progress updates, final answers, and milestone messages unless the user asks for another language.

## Implementation Readiness

Do not create runnable product code, package manager files, app scaffolding, API skeletons, database schemas, migrations, or dev-server behavior until the readiness gate is satisfied.

Required before implementation:

- `AGENTS.md`
- `docs/project/PROJECT_CHARTER.md`
- `docs/architecture/TECH_STACK.md`
- `docs/architecture/ENGINEERING_BASELINE.md`
- `docs/architecture/FRONTEND_PLAN.md` when frontend UI is in scope
- `docs/architecture/DATABASE_DESIGN.md` or an explicit no-database decision when persistence is in scope
- `docs/architecture/BACKEND_SPEC.md` or an explicit no-backend decision when API, worker, or service boundaries are in scope
- `docs/workflow/AI_WORKFLOW.md`
- `docs/ops/TOOL_POLICY.md`
- `docs/ops/DEPLOYMENT.md` when local run, environment variables, or hosting are in scope

When frontend UI is in scope, `docs/architecture/FRONTEND_PLAN.md` must define the frontend engineering contract, not only the visual style or page list. It must cover source tree, route/page responsibilities, shared UI and business component locations, state ownership, config/messages/icons/assets/utilities ownership, and import boundaries.

It must also define the Product MVP UI Quality Gate before UI code starts. The plan must include Design Read, Design Dials, design system tokens, UI component strategy, state and interaction contract, responsive and accessibility expectations, anti-slop guardrails, and browser UI quality verification. Do not use the accelerated path to skip this gate; after creating or updating the named missing batch, rerun the implementation readiness audit and block frontend code if the UI quality gate is incomplete.

If multiple readiness documents are missing, do not give only a single next-document suggestion. Offer plain-text options and do not depend on UI buttons:

- `A. Steady path`: create or update the single most important next document, then ask for review.
- `B. Accelerated path`: ask for consent to create or update the named missing batch for this stage, then run the implementation readiness audit.

Batch consent applies only to the named missing batch and does not authorize implementation code, scaffolding, package manager files, UI pages, APIs, schemas, migrations, or runnable behavior.

## Implementation Handoff

When the implementation readiness gate has passed and the task is a Bounded Feature Path or Local Fix Path, do not rerun the full project baseline. Use the approved implementation workflow:

1. Read the affected source-of-truth docs.
2. State whether the Contract Impact Check found any source-of-truth changes.
3. If no contract changes are needed, implement the smallest useful change.
4. Verify with tests, build, browser, API, CLI, worker, security, or run evidence as applicable.
5. Report changed files, source-of-truth impact, and verification evidence.

## Completion Definition

- [ ] Relevant tests or checks pass.
- [ ] Build passes when applicable.
- [ ] Browser/API/security evidence is provided when applicable.
- [ ] Frontend browser UI quality evidence is provided for desktop and mobile when UI is changed.
- [ ] Source-of-truth docs are updated before implementation when decisions or contracts change.
- [ ] Frontend files follow the documented source tree and component boundaries when UI is changed.
- [ ] Git diff is reviewed before commit.

## Forbidden Actions

- Production changes without confirmation.
- Destructive Git or filesystem operations without confirmation.
- Broad rewrites without a plan.
- New major dependencies without documented approval.
- Changing repository shape, UI library, or icon library without documented approval.
- Packing unrelated frontend UI, config, messages, state, mock data, icons, and utilities into a single app, page, or route file.
