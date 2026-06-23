# Document Layout

Use this reference whenever the skill creates, reorganizes, or indexes project source-of-truth documents.

## Default Layout

Keep the repository root scannable. `AGENTS.md` stays at the root because agents naturally look there first. Detailed project documents live under `docs/`.

```text
.
├── AGENTS.md
├── README.md
├── apps/
├── packages/
└── docs/
    ├── project/
    │   └── PROJECT_CHARTER.md
    ├── architecture/
    │   ├── TECH_STACK.md
    │   ├── ENGINEERING_BASELINE.md
    │   ├── FRONTEND_PLAN.md
    │   ├── DATABASE_DESIGN.md
    │   └── BACKEND_SPEC.md
    ├── features/
    │   └── <feature-name>.md
    ├── changes/
    │   └── <date-or-id>-<change-name>.md
    ├── decisions/
    │   └── ADR-<number>-<topic>.md
    ├── agent-project-kit/
    │   └── PROCESS_ARTIFACTS.md
    ├── workflow/
    │   └── AI_WORKFLOW.md
    └── ops/
        ├── TOOL_POLICY.md
        └── DEPLOYMENT.md
```

## Root Rules

Root may contain entry points and tooling only: `AGENTS.md`, `README.md`, package manager files, lockfiles, repo config, `.env.example`, `.gitignore`, `apps/`, `packages/`, `docs/`, `.codex/`, and `.github/`.

Do not put detailed planning documents in the root unless the user explicitly requests a flat layout.

## AGENTS.md Role

Use root `AGENTS.md` as a short index and operating contract:

- Link to the project source-of-truth documents under `docs/`.
- State source-of-truth priority and completion definition.
- Keep stable rules only.
- Do not duplicate the full contents of `docs/architecture/TECH_STACK.md`, `docs/ops/TOOL_POLICY.md`, or specs.

## Document Lifespan

Keep current-state source-of-truth documents compact. They should describe the contract the project follows now, not the full history of every change.

- Core source-of-truth documents under `docs/project/`, `docs/architecture/`, `docs/workflow/`, and `docs/ops/` hold current product, architecture, workflow, deployment, and tool contracts.
- `docs/features/` holds stable feature behavior that is useful to find by feature name without bloating architecture documents.
- `docs/changes/` holds one change's proposal, design notes, tasks, acceptance notes, and temporary implementation context.
- `docs/decisions/` holds ADR-style long-term product or architecture decisions and rejected alternatives.
- `docs/agent-project-kit/` holds Agent Project Kit process artifacts such as reference scans, capability scans, readiness audits, and handoffs.

When a change finishes, distill only durable contract changes back into the core documents. Keep process-heavy detail in `docs/changes/` or archive it.

## Path Mapping

| Artifact | Default path |
| --- | --- |
| Agent constitution | `AGENTS.md` |
| Project charter | `docs/project/PROJECT_CHARTER.md` |
| Tech stack | `docs/architecture/TECH_STACK.md` |
| Engineering baseline | `docs/architecture/ENGINEERING_BASELINE.md` |
| Frontend plan | `docs/architecture/FRONTEND_PLAN.md` |
| Database design | `docs/architecture/DATABASE_DESIGN.md` |
| Backend spec | `docs/architecture/BACKEND_SPEC.md` |
| Feature note | `docs/features/<feature-name>.md` |
| Change note | `docs/changes/<date-or-id>-<change-name>.md` |
| Architecture decision | `docs/decisions/ADR-<number>-<topic>.md` |
| Agent Project Kit process artifacts | `docs/agent-project-kit/PROCESS_ARTIFACTS.md` or subfolders under `docs/agent-project-kit/` |
| AI workflow | `docs/workflow/AI_WORKFLOW.md` |
| Tool policy | `docs/ops/TOOL_POLICY.md` |
| Deployment plan | `docs/ops/DEPLOYMENT.md` |

## Migration Rule

If old root documents already exist, do not move them silently. Propose a migration plan, list old and new paths, and ask for confirmation before moving files.
