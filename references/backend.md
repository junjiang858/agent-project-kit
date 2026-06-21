# Backend

Use this reference for backend understanding, API boundaries, business rules, minimal backend skeletons, and backend architecture acceptance.

## Backend Understanding

Backend owns business rules, data processing, permission checks, system interfaces, and protection of data. Frontend expresses and interacts; backend decides, stores, computes, and guards.

Before coding, distinguish:

- Small script: solves one narrow task quickly.
- Project backend: needs stable architecture, API contracts, validation, permissions, data access, observability, and maintainability.

## Backend Business Spec

Produce `docs/architecture/BACKEND_SPEC.md` before implementation. Include:

- Business objects and actions.
- Rules that must be enforced on the backend.
- Data flow: input, validation, processing, storage, response.
- API list and contract: method, path, input, output, errors.
- Which API reads or writes which database tables.
- Authentication, roles, ownership, and admin-only operations.
- Parameter validation, error handling, and logging rules.
- Recommended language/framework and why alternatives are not chosen.

If a later task changes an API, request/response contract, validation rule, error shape, permission boundary, backend workflow, integration, worker, or data flow, update `docs/architecture/BACKEND_SPEC.md` before editing backend code.

## Minimal Backend Skeleton

The goal is the smallest runnable structure, not full feature coverage.

Do not build even a minimal backend skeleton until `docs/architecture/BACKEND_SPEC.md` exists and the Project Specification Readiness Gate has passed for the requested product shape.

Run four lines:

- Startup line: app starts with documented command and environment variables.
- Interface line: health check and one representative API route.
- Business line: one minimal module goes through route, service, data access, validation, and error handling.
- Operations line: config, env, logging, basic tests, and run evidence.

Deliver:

- Architecture design and directory responsibility.
- Startup command.
- Health check result.
- Minimal module test or API sample.
- Environment variable list.
- Known gaps and next implementation order.

## Architecture Acceptance

Backend "can start" is not enough. Accept it by checking:

- Alignment with project charter, tech stack, Agent constitution, and database design.
- Directory responsibilities and module boundaries.
- Full call chain for one minimal module.
- Unified response shape and error handling.
- Authentication/permission entry points.
- Framework reuse boundaries: use framework conventions instead of custom scattered patterns.
- Evidence: command output, test result, health check, API sample.
- Source-of-truth sync: changed backend contracts are reflected in `docs/architecture/BACKEND_SPEC.md` before implementation evidence is accepted.

## Prompt: Backend Business Boundary

```text
Do not write code yet. Based on the project charter, frontend flow, database design, and business needs, analyze the backend plan. Output backend responsibilities, required APIs, business validation for each API, database tables each API reads/writes, login/admin requirements, parameter validation, exception handling, recommended language/framework, built-in framework capabilities, required external libraries, and decisions that must go into docs/architecture/BACKEND_SPEC.md.
```

## Prompt: Minimal Backend Skeleton

```text
Based on docs/architecture/BACKEND_SPEC.md and docs/architecture/TECH_STACK.md, first verify the Project Specification Readiness Gate. If ready, build a minimal runnable backend skeleton. First output the implementation plan and directory responsibilities, then implement startup line, interface line, business line, and operations line. Finish with startup command, test method, health check, and run evidence.
```

## Prompt: Architecture Acceptance

```text
Perform backend architecture acceptance on the current skeleton. Check rule alignment, directory responsibility, minimal module call chain, interface response standard, framework reuse boundary, permission entry points, and startup evidence. Output issues, remediation suggestions, and the implementation source-of-truth update.
```
