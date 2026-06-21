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
