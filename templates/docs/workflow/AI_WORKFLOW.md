# AI_WORKFLOW

## Flow

1. Clarify the request.
2. Read `AGENTS.md` and relevant project documents under `docs/`.
3. Run a Contract Impact Check for feature or fix work.
4. Classify the work as Project Baseline Path, Contract-Changing Feature Path, Bounded Feature Path, or Local Fix Path.
5. Produce or update a plan.
6. If the task changes design, frontend source tree, component boundaries, contracts, data shape, permissions, tools, deployment, or operations, update the affected source-of-truth document first.
7. If the task is a Bounded Feature Path or Local Fix Path, use the Implementation Handoff instead of rerunning the full project baseline.
8. Implement the smallest useful change against the updated documents.
9. Run checks.
10. When the user asks whether the MVP is complete, what remains, whether release is safe, or what to do next after implementation, run an MVP closure audit before claiming completion.
11. Report changed-doc summary and evidence.

## Contract Impact Check

Check whether the task changes:

- Frontend routes, pages, component responsibilities, UI states, interactions, data dependencies, source tree, ownership, or import boundaries.
- API endpoints, request/response contracts, validation, errors, permissions, backend workflows, integrations, workers, or data flow.
- Tables, fields, relations, indexes, enums, seeds, schemas, migrations, ownership, retention, or rollback.
- Frameworks, packages, scripts, repository layout, quality gates, deployment, environment variables, tool permissions, or operations.
- Security, privacy, production data, external writes, payments, secrets, privileged local access, or destructive operations.

If any item changes, use the Contract-Changing Feature Path and update source-of-truth docs before code.

## Implementation Handoff

When the readiness gate has passed and the Contract Impact Check finds no contract changes:

1. Read the relevant docs.
2. State that the work is a Bounded Feature Path or Local Fix Path.
3. Use Superpowers, another approved workflow, or the built-in fallback.
4. Verify with tests, build, browser, API, CLI, worker, security, or run evidence.
5. Report source-of-truth impact and evidence.

## Optional Workflow Tool Fallback

Superpowers, OpenSpec, GitHub Spec Kit, issue trackers, and similar workflow tools are optional accelerators unless the project explicitly declares one as primary.

If available and applicable, use them after protecting source-of-truth gates. If unavailable, do not block. Use the built-in fallback: clarify scope, run the Contract Impact Check, update docs only when contracts change, make a small plan, implement, verify, and report evidence.

## Human Confirmation Required

- Scope changes.
- New major dependency.
- Production or external account actions.
- Destructive operations.
- Security-sensitive changes.
- Source-of-truth document changes when the project requires document consent.

## Evidence by Work Type

| Work type | Evidence |
| --- | --- |
| Docs | changed files and decision summary |
| Frontend | build/check output and browser verification |
| Backend | tests, health check, API sample |
| Database | schema/migration diff and rollback note |
| Security | risk table, code locations, verification |

When implementation changes design or contracts, docs evidence must come before code evidence.
When frontend implementation changes source tree, file responsibilities, component boundaries, state/config/i18n/utils ownership, or import boundaries, `docs/architecture/FRONTEND_PLAN.md` evidence must come before code evidence.

## MVP Closure States

- `MVP Scope Incomplete`: documented must-have scope, acceptance evidence, or blocking risks remain. Do not use a celebration message; report remaining risks and the next recommended action.
- `Full MVP Scope Complete`: the documented MVP scope is implemented and verified with current evidence. Switch to Formal Product Development Mode: release validation, architecture hardening, user feedback, and next-version planning.
- `Release Ready`: Full MVP Scope Complete plus deployment, environment, regression, security, rollback, and operational checks pass for the target release.

## Source-of-Truth Distillation

Core docs describe the current system contract. Do not turn them into change journals.

- Stable feature behavior: `docs/features/`.
- One-change proposal, design, tasks, and acceptance detail: `docs/changes/`.
- Long-term decisions: `docs/decisions/`.
- Agent Project Kit process artifacts: `docs/agent-project-kit/`.
- Durable current contracts: distill back into the relevant core docs.

## Session Handoff

- Current goal:
- Completed:
- Remaining:
- Risks:
- Next recommended command:
