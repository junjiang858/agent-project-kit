# Engineering Baseline

Use this reference when defining repo hygiene, scripts, CI, code quality, migrations, environment configuration, and testing expectations.

## Baseline Principle

MVP means fewer product features, not weaker engineering foundations. A Product MVP should have enough structure to extend safely without replacing the core stack.

## Required Scripts

For JavaScript/TypeScript projects, prefer these root scripts:

| Script | Purpose |
| --- | --- |
| `dev` | start local development |
| `build` | produce production build |
| `typecheck` | verify TypeScript types |
| `lint` | run ESLint |
| `format` or `format:check` | run or check Prettier formatting |
| `test` | run unit or integration tests |
| `check` | minimal local quality gate, usually typecheck + lint + test + build |
| `clean` | remove generated build artifacts when useful |

## Code Quality

Prefer:

- `.editorconfig`
- ESLint flat config or framework-approved ESLint setup
- Prettier config
- TypeScript strictness appropriate to the framework
- Shared config package when multiple apps/packages need the same rules

Husky, lint-staged, and commitlint are recommended for teams and public projects, but CI remains the required source of enforcement.

References:

- https://eslint.org/docs/latest/use/configure/configuration-files
- https://typicode.github.io/husky/

## CI

For public or collaborative repositories, add CI early:

1. Install with the committed lockfile.
2. Run `typecheck`.
3. Run `lint`.
4. Run `test`.
5. Run `build`.

CI can skip expensive browser checks until the first UI workflow exists, but it should not skip install, typecheck, lint, tests, and build once those scripts are defined.

## Database Migrations

If the project has a database, define before backend implementation:

- migration tool and config file
- migration directory
- local development database command
- schema generation or introspection command
- rollback or recovery note

Do not treat an example SQL file as the full migration strategy for a product MVP.

## Environment Configuration

Provide `.env.example` with names only, not secrets. Document required variables in `docs/ops/DEPLOYMENT.md` or `docs/architecture/ENGINEERING_BASELINE.md`.

Validate env at runtime for backend services and production builds. Fail fast when required variables are missing.

## Backend Baseline

For an API service, define:

- unified error handler
- request id or correlation id
- structured logging boundary
- validation layer, usually schema or DTO validation
- auth and permission entry point
- path traversal and file upload safety if files are involved
- health check

## Testing Layers

Use the smallest meaningful test layer for each risk:

- Unit tests for pure logic, validation, utility functions, and services.
- Integration tests for API routes, database access, auth boundaries, and migrations.
- Browser or e2e tests for critical user flows after the UI exists.
- Security regression tests for forbidden paths, access control, unsafe uploads, or sensitive data exposure.

## Commit Discipline

Recommended public-project baseline:

- Commit stable stage boundaries.
- Inspect `git status` and `git diff` before commits.
- Keep generated secrets, private config, local databases, and personal notes out of Git.
- Use conventional commit messages or document the project commit style.
