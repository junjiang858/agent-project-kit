# Architecture Baseline

Use this reference when choosing the project architecture track, repository shape, backend boundary, and production-compatible MVP stack.

## Contents

- Core Principle
- Community Anchors
- Capability Library Scan Gate
- Architecture Tracks
- Default Product MVP Stack
- Repository Shape Decision
- Stack Decision Rules
- Anti-Patterns

## Core Principle

Build a Product MVP by default: keep the feature scope small, but choose a repository shape and core stack that can grow without replacing the foundation. Use a throwaway stack only when the user explicitly says the work is a disposable prototype.

Do not choose, write, or lock a technology stack from a vague project idea. Technology selection starts only after the project purpose and charter facts are confirmed, the Capability Library Scan Gate has been completed, and writing `docs/architecture/TECH_STACK.md` requires explicit consent for that document.

A confirmed technology stack is not permission to scaffold or implement. Before creating package manager files, apps, packages, UI/API code, database schema, migrations, or runnable behavior, run the Project Specification Readiness Gate from `SKILL.md` and confirm that all product-shape documents are present.

## Community Anchors

Use mature ecosystem conventions as defaults, then narrow them to the project's actual shape:

- Turborepo and pnpm workspace conventions: `apps/*` for applications or services, `packages/*` for shared libraries and tooling, root package manager config, and lockfile. Use these only when the project has real application/package boundaries.
- Nx workspace conventions: keep applications and libraries separated so boundaries stay clear as the repo grows.
- Next.js conventions: preserve framework-owned routing and file conventions instead of inventing a custom application layout.
- NestJS conventions: use modules, providers, controllers, services, validation, and dependency injection for APIs with real business rules.

Reference URLs:

- https://turborepo.dev/docs/crafting-your-repository/structuring-a-repository
- https://pnpm.io/workspaces
- https://pnpm.io/catalogs
- https://nx.dev/docs/concepts/decisions/folder-structure
- https://nextjs.org/docs/app/getting-started/project-structure
- https://docs.nestjs.com/modules
- https://docs.nestjs.com/providers

## Capability Library Scan Gate

Before recommending or confirming a technology stack, extract the project's required technical capabilities from the confirmed charter facts. Examples include authentication, forms, validation, tables, charts, rich text, file upload, search, background jobs, payments, email, realtime, AI SDKs, workflow orchestration, observability, testing, and deployment.

Then research project-needed third-party libraries only for those capabilities. Do not produce a generic "popular libraries" list.

Required output shape:

| Capability | Library name | Direct link | Ecosystem | Open-source or inspectable | Maintenance evidence | Why include/defer/reject | Risk or lock-in note | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | Included / Deferred / Rejected |

Rules:

- Each recommended or rejected candidate must include capability, library name, direct link, ecosystem, open-source or inspectability status, license or commercial constraint when relevant, maintenance evidence, why it fits or does not fit this project, migration or lock-in risk, and whether it is included now, deferred, or rejected.
- Include a capability, library name, direct link, and decision for every row.
- Prefer mature, open-source, actively maintained, well-documented libraries when they fit the project.
- Use official docs, GitHub repositories, package registries, release notes, or security advisories for maintenance evidence.
- Mention license or commercial-use constraints when relevant.
- Include rejected or deferred candidates when they explain why the chosen stack stays smaller.
- Avoid adding dependencies for framework-native capabilities unless the project has a concrete need.

Do not confirm a technology stack, write `docs/architecture/TECH_STACK.md`, install dependencies, or scaffold implementation until the user confirms the combined core stack and third-party library set.
- If current maintenance status matters, use live research. If live research is unavailable, say maintenance evidence is incomplete.

After the table, present one combined recommendation for user review:

1. Core stack: product form, architecture track, framework, runtime, database, deployment, package manager, testing.
2. Included libraries: only libraries needed by the MVP.
3. Deferred libraries: useful later, not needed for the first slice.
4. Rejected libraries: considered but not a fit.
5. Re-evaluation triggers: when a deferred or rejected library should be reconsidered.

Do not confirm the stack, write `docs/architecture/TECH_STACK.md`, install packages, or scaffold files until the user confirms the combined stack and library set.

## Architecture Tracks

Choose one track and record it in `docs/architecture/TECH_STACK.md`.

| Track | Use when | Default shape |
| --- | --- | --- |
| Single Web App | One deployable web product, backend needs are light or handled by framework/server actions | Single package when no shared boundary exists; otherwise `apps/web` plus only real `packages/*` libraries |
| Web + API | Web app plus independent backend API, real business rules, permissions, integrations, or mobile/API clients | `apps/web`, `apps/api`, `packages/shared`, `packages/config`, `packages/db` |
| Multi-App Platform | Admin app, worker, multiple clients, or platform-style growth expected | `apps/web`, `apps/admin`, `apps/api`, `apps/worker`, `packages/shared`, `packages/config`, `packages/db`, optional `packages/auth` |

## Default Product MVP Stack

For ordinary long-lived web products:

- Package manager and repository shape: use a single package for one deployable frontend app with one ownership boundary and no shared library boundary; use a workspace with `apps/*` and `packages/*` only when local packages have real ownership.
- Web: Next.js + TypeScript when SSR, routing, API adjacency, or Vercel deployment matters; otherwise React + Vite is acceptable for frontend-only tools.
- API: NestJS for independent product backends with modules, validation, auth, and business boundaries. Fastify is acceptable for narrow services when the architecture document explains how modules, validation, errors, and observability are handled.
- Database: PostgreSQL or Supabase/Postgres for long-lived relational products. SQLite is acceptable for explicit local-first, embedded, or throwaway prototypes.
- Data access: Prisma or Drizzle with migrations. Do not rely on hand-written schema files as the only migration story.
- Shared packages: put cross-app types, schemas, clients, config, database access, reusable media/core logic, worker contracts, or SDK-like APIs in `packages/` only when they are actually shared or meaningfully isolated from UI.
- Build orchestration: plain pnpm scripts are enough for small repos; add Turborepo or Nx when multiple packages need coordinated caching, affected builds, or task pipelines.
- AI workflow discipline: Superpowers, OpenSpec, GitHub Spec Kit, and similar tools are optional accelerators. If they are unavailable, document the built-in fallback in `docs/workflow/AI_WORKFLOW.md`: clarify scope, run the Contract Impact Check, update source-of-truth docs only when contracts change, plan, implement, verify, and report evidence.

## Repository Shape Decision

Before recommending a workspace, classify the repository boundary:

| Shape | Use when | Avoid when |
| --- | --- | --- |
| Single package frontend app | One deployable frontend app, all code has one ownership boundary, no shared schemas/core logic, no worker package, no near-term second app | The app already has reusable domain logic, worker contracts, or package-level tests that would be clearer outside UI |
| pnpm workspace | There are two or more real packages, such as `apps/web` plus shared schemas, media/core logic, workers, SDKs, generated clients, or future deployable apps | The `packages/*` folders would be empty placeholders or only speculative "future-proofing" |
| Turborepo/Nx workspace | Multiple packages need task caching, affected builds, generators, dependency graph visibility, or CI optimization | Plain pnpm scripts are still easy to understand and fast enough |

Do not create empty shared packages just because the default Product MVP stack mentions workspaces. If the project starts as a single package and later gains a real boundary, update `TECH_STACK.md`, `ENGINEERING_BASELINE.md`, `FRONTEND_PLAN.md`, and root agent rules before moving files.

## Stack Decision Rules

Before recommending the stack, confirm:

- `docs/project/PROJECT_CHARTER.md` exists or the equivalent charter facts have been confirmed in conversation.
- The user has agreed to enter technology selection.
- The Capability Library Scan Gate has mapped required technical capabilities to included, deferred, and rejected libraries.
- Product form is known: web, mini program, mobile app, backend service, automation, hybrid, or something else.
- Product lifecycle is known: Product MVP, throwaway prototype, internal tool, or platform.
- Team capability, launch pressure, budget or hosting constraints, and expected users are known enough to guide tradeoffs.

Before writing `docs/architecture/TECH_STACK.md`, ask for consent and state the target path. Consent to write the project charter does not imply consent to write the tech stack document.

Before implementation, document:

- Architecture Track.
- Product Lifecycle: Product MVP, throwaway prototype, internal tool, or platform.
- Capability Library Scan: which project-needed third-party libraries are included, deferred, or rejected, with maintenance evidence.
- Production Compatibility: what can remain unchanged after launch.
- Migration Cost: which choices would be expensive to replace later.
- Explicit Non-Replacement: core framework, database family, package manager, deployment model, auth approach.
- Optional Workflow Tool Fallback: whether the project uses Superpowers, OpenSpec, GitHub Spec Kit, another workflow, or the built-in fallback.
- Re-Evaluation Triggers: product shape, team capability, compliance, performance, cost, or ecosystem risk changes.

Before scaffolding, also document the frontend plan, database design, backend spec, AI workflow, tool policy, deployment plan, and Agent rules when those surfaces exist. If any are missing, ask to create the next source-of-truth document instead of writing code.

For frontend applications, the frontend plan must document the engineering structure before UI code is generated: framework-owned directories, project-owned directories, route/page responsibilities, shared UI location, business component boundaries, state ownership, config and i18n ownership, utility boundaries, and import rules. Directory structure and component decomposition are architecture decisions, not cleanup tasks after scaffolding.

## Anti-Patterns

- Choosing SQLite, in-memory stores, ad hoc files, or no migrations for a product expected to launch with real users.
- Starting with a single `App.tsx` and no route/component/data boundaries for an app expected to grow.
- Creating `apps/*` and `packages/*` before a real app/package boundary exists.
- Treating `App.tsx`, `page.tsx`, or a route file as the container for all UI, config, messages, state, icons, mock data, and utilities.
- Creating a flat `components/` or `utils.ts` dump without documented ownership, domain boundaries, or import rules.
- Creating custom backend patterns while ignoring framework conventions.
- Confirming a stack before researching third-party libraries needed by the project's actual capabilities.
- Adding a popular library without a project capability, direct source link, maintenance evidence, and include/defer/reject decision.
- Adding monorepo complexity for a one-file script or disposable experiment.
- Introducing a second framework or database before documenting why the current stack cannot handle the need.
