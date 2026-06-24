# MVP Closure Audit

Use this reference when checking whether the implementation satisfies the documented MVP scope, when deciding whether release is safe, or when appending post-implementation next step recommendations.

## Trigger Policy

Run a fresh synchronous audit when:

- The user asks whether the MVP is complete, what remains, what risks exist, whether release is safe, or what to do next after implementation.
- The agent is about to say `Full MVP Scope Complete`, `Release Ready`, or equivalent language.
- The current implementation task may close a documented must-have feature, acceptance criterion, deployment blocker, or security blocker.

Do not run a fresh audit for Local Fix Path, code explanations, single-command tasks, or ordinary bounded work that cannot change MVP completion. Use a recent cached result for a short tail recommendation when useful.

## Required Inputs

Read only the relevant source-of-truth documents for the project shape:

- `docs/project/PROJECT_CHARTER.md` for MVP scope, must-have features, non-goals, risks, and acceptance criteria.
- `docs/architecture/FRONTEND_PLAN.md` when UI, browser states, responsive behavior, or frontend workflow completion matter.
- `docs/architecture/BACKEND_SPEC.md` when APIs, workers, integrations, permissions, or business rules matter.
- `docs/architecture/DATABASE_DESIGN.md` when persistence, migrations, seeds, retention, or rollback matter.
- `docs/architecture/ENGINEERING_BASELINE.md` for required scripts, quality gates, and test expectations.
- `docs/ops/DEPLOYMENT.md` when local run, production host, environment, release, rollback, COOP/COEP, storage, or operational behavior matters.
- `docs/ops/TOOL_POLICY.md` and security notes when secrets, external writes, payments, uploaded executable content, production data, or privileged tools matter.

If source-of-truth documents are missing, report `MVP Scope Incomplete` unless the missing surface is explicitly marked not applicable.

## Audit Steps

1. Extract the documented MVP obligations: must-have scope, first-use workflow, acceptance criteria, quality gates, deployment requirements, and explicitly accepted risks.
2. Inspect current implementation evidence using the lightest reliable method: file locations, tests, build scripts, recent command output, browser/API/CLI/worker logs, deployment previews, or status artifacts.
3. Classify each obligation:
   - `Met`: implemented and supported by current evidence.
   - `Partially met`: implementation exists but evidence, edge states, production behavior, or documented criteria are incomplete.
   - `Missing`: no implementation evidence found.
   - `Deferred or non-goal`: explicitly outside MVP.
   - `Accepted risk`: not solved, but explicitly accepted by the user or source-of-truth document.
4. Classify risks:
   - `blocking`: prevents Full MVP Scope Complete or Release Ready.
   - `non-blocking`: should be tracked but does not block the current milestone.
   - `needs user decision`: requires an explicit acceptance, scope change, or release tradeoff.
5. Determine the lifecycle state:
   - `MVP Scope Incomplete` if any must-have obligation is missing, partially met without accepted risk, or blocked by unresolved risk.
   - `Full MVP Scope Complete` if all documented MVP obligations are met or explicitly deferred/non-goal/accepted, with fresh evidence.
   - `Release Ready` only if Full MVP Scope Complete and deployment, environment, security, regression, rollback, and operational checks pass for the requested release target.

## Common Risk Signals

Treat these as blocking unless the source-of-truth documents or user explicitly accept them:

- `mock-only`: feature works only through mocks, stubs, fixtures, or fake success paths.
- `production-unverified`: local or unit evidence exists but production-like runtime, browser, worker, storage, or hosted environment is unverified.
- `deployment-gap`: missing environment variables, host behavior, COOP/COEP, CDN/static assets, persistence path, health check, rollback, or release command.
- `security-gap`: secrets, permissions, uploaded content, external writes, production data, payment, or privileged tool access is unverified.
- `doc-code-drift`: implementation behavior changed without source-of-truth updates.
- `missing-e2e`: user-critical browser/API/CLI/worker flow lacks end-to-end evidence.
- `ux-unverified`: frontend slice lacks browser evidence for required states, responsive layout, accessibility, or Product MVP UI Quality Gate.

## Output Format

For a full audit, keep the report concise and evidence-oriented:

```text
Conclusion: <MVP Scope Incomplete | Full MVP Scope Complete | Release Ready>

Met:
- <obligation> - evidence: <file/test/log>

Incomplete or blocking:
- <obligation or risk> - why it blocks - recommended fix

Accepted or non-blocking risks:
- <risk> - acceptance source or reason

Next step recommendation:
<one concrete next action, preferably blocking-risk first rather than feature expansion>
```

For ordinary post-task answers, append only a short tail recommendation:

```text
Next step recommendation:
Current MVP closure status is <state>. Prioritize <one or two blocking items> before expanding new functionality.
```

Do not use a milestone celebration message when the state is `MVP Scope Incomplete`.

## Cache And Process Artifacts

When a project allows process artifacts, store durable audit outputs under `docs/agent-project-kit/`, such as `docs/agent-project-kit/mvp-closure-status.md`.

When a script cache is available, use a cache key based on the current git commit, dirty diff, source-of-truth document hashes, package lock hashes, and relevant configuration hashes. If the cache is stale, say so instead of presenting stale results as current evidence.
