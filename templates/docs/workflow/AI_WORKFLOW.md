# AI_WORKFLOW

## Flow

1. Clarify the request.
2. Read `AGENTS.md` and relevant project documents under `docs/`.
3. Produce or update a plan.
4. If the task changes design, contracts, data shape, permissions, tools, deployment, or operations, update the affected source-of-truth document first.
5. Implement the smallest useful change against the updated documents.
6. Run checks.
7. Report changed-doc summary and evidence.

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

## Session Handoff

- Current goal:
- Completed:
- Remaining:
- Risks:
- Next recommended command:
