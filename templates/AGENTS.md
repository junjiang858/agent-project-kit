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

## Source of Truth

1. User instruction
2. `docs/project/PROJECT_CHARTER.md`
3. `docs/architecture/TECH_STACK.md`
4. `docs/architecture/ENGINEERING_BASELINE.md`
5. `docs/ops/TOOL_POLICY.md`
6. Existing code conventions

## Working Rules

- Clarify scope before implementation.
- Preserve the documented tech stack.
- Keep detailed project documents under `docs/`; keep this file short as the root index.
- Update the relevant source-of-truth document before code when design, API, database, permission, deployment, tool, or operational behavior changes.
- Keep changes small and reviewable.
- Use existing patterns before adding abstractions.
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

If multiple readiness documents are missing, do not give only a single next-document suggestion. Offer plain-text options and do not depend on UI buttons:

- `A. Steady path`: create or update the single most important next document, then ask for review.
- `B. Accelerated path`: ask for consent to create or update the named missing batch for this stage, then run the implementation readiness audit.

Batch consent applies only to the named missing batch and does not authorize implementation code, scaffolding, package manager files, UI pages, APIs, schemas, migrations, or runnable behavior.

## Completion Definition

- [ ] Relevant tests or checks pass.
- [ ] Build passes when applicable.
- [ ] Browser/API/security evidence is provided when applicable.
- [ ] Source-of-truth docs are updated before implementation when decisions or contracts change.
- [ ] Git diff is reviewed before commit.

## Forbidden Actions

- Production changes without confirmation.
- Destructive Git or filesystem operations without confirmation.
- Broad rewrites without a plan.
- New major dependencies without documented approval.
