# Agent Project Kit

[English](README.md) | [简体中文](README.zh-CN.md)

> Stop letting coding agents turn vague ideas into messy repos.
>
> Agent Project Kit makes the agent clarify, confirm, document, choose a stack, and verify before it writes code.

## ✨ What This Is

Agent Project Kit is a Codex skill that gives AI-assisted software projects a lightweight product and engineering operating system.

It is built for the moment when a user says "help me build a project" but the product, users, scope, stack, data model, safety boundaries, and acceptance criteria are not clear enough yet.

Instead of letting the agent rush into files or code, Agent Project Kit routes the work through staged clarification, explicit document consent, technology decisions, project rules, implementation plans, and evidence-based acceptance.

The default posture is Product MVP:

- Keep the first version small.
- Avoid disposable foundations.
- Make the repo shape, technical route, engineering baseline, tool permissions, and verification habits strong enough to survive real iteration.

## 🚦 Before / After

Without this skill:

```text
"Build me an admin system."
→ The agent creates files, picks a stack, invents requirements, and leaves shallow docs.
```

With Agent Project Kit:

```text
clarify users
→ define MVP scope
→ confirm project purpose
→ ask before writing docs
→ choose one technical route
→ create project rules
→ verify with evidence
```

## 📦 What You Get

Agent Project Kit helps the agent create and maintain project source-of-truth files such as:

- `docs/project/PROJECT_CHARTER.md` — users, problem, MVP scope, workflows, domain objects, risks, and acceptance criteria.
- `docs/architecture/TECH_STACK.md` — one chosen stack, rejected alternatives, migration cost, production compatibility, and re-evaluation rules.
- `AGENTS.md` — project-level agent rules and document index.
- `docs/architecture/ENGINEERING_BASELINE.md` — scripts, quality gates, testing, migrations, environment rules, and commit discipline.
- `docs/ops/TOOL_POLICY.md` — default tools, project-specific tools, and high-risk confirmation gates.
- `docs/workflow/AI_WORKFLOW.md` — clarify, spec, plan, implement, verify, and archive workflow.

## 🧩 What It Helps You Do

- Turn vague ideas into PRD-quality project charters.
- Scan concrete reference projects with direct project links before narrowing a vague idea.
- Prevent premature document creation, technology choices, and implementation.
- Choose one main technical route based on product shape, lifecycle, team capability, launch pressure, migration cost, and production compatibility.
- Review project-needed third-party libraries with direct links, maintenance evidence, and include/defer/reject decisions before confirming the stack.
- Create durable project source-of-truth documents under `docs/` instead of scattering planning notes across chat history.
- Update source-of-truth documents before code when a later task changes frontend design, API contracts, database shape, permissions, deployment, tools, or operations.
- Establish AI working rules through `AGENTS.md`, engineering baselines, tool permission policies, and workflow documents.
- Plan frontend, backend, database, security, deployment, and acceptance work with verification evidence instead of "trust me" completion claims.

## 🧠 Why It Helps

- Reduces AI drift by making the agent return to confirmed project facts before it writes or changes code.
- Protects user control by asking before creating source-of-truth documents or locking major technical decisions.
- Makes small projects easier to grow by separating product clarity, architecture, engineering rules, and implementation tasks.
- Gives non-expert builders a practical path through product definition, stack selection, project rules, and acceptance without adopting a heavy project-management system.

## 🧭 Who It Is For

- Solo builders and small teams using Codex, Claude Code, Cursor, Copilot, or similar coding agents.
- Product-minded builders who want AI speed without losing control of scope, stack, documents, and acceptance standards.
- Non-expert or early-stage developers who need the agent to act like a product partner and architecture advisor before acting like a code generator.
- Teams that want lightweight project structure, not a full product-management platform.
- AI-assisted projects that are expected to become real products, internal tools, dashboards, automation systems, services, or prototypes with a clear path to iteration.

## 🎯 Best-Fit Scenarios

- You have a vague idea and need the agent to ask the right next question instead of writing code immediately.
- You need a `PROJECT_CHARTER.md`, `TECH_STACK.md`, `AGENTS.md`, or `TOOL_POLICY.md`, but want the agent to confirm the facts and ask before writing files.
- You are choosing between prototype speed and Product MVP durability, and need a single technical route with tradeoffs and re-evaluation rules.
- You want a repeatable AI workflow for frontend, backend, database, security, deployment, and acceptance planning.
- You are preparing a new repo so future agent sessions can understand the project facts, boundaries, tools, and verification expectations.

## 💬 Mini Demo

```text
User: Help me create a project.
Agent: Current stage: project initiation. What are you trying to build?

User: A tiny app for saving reading notes.
Agent: Before narrowing requirements, I should scan concrete references:
Omnivore (https://github.com/omnivore-app/omnivore), Logseq (https://github.com/logseq/logseq),
and Reor (https://github.com/reorproject/reor). I will compare what to borrow, what not to copy,
and how each changes the MVP direction.

User: I like the lightweight read-it-later angle from Omnivore.
Agent: Got it. I will use that direction, then clarify who uses it and which first workflow must succeed.
```

## 🔍 Why This Is Different

Agent Project Kit is not just a prompt collection.

It combines:

- Stage routing: the agent loads only the reference needed for the current phase.
- Reference project scan gate: the agent checks concrete examples with direct project links before narrowing a vague idea.
- Capability library scan gate: before stack confirmation, the agent maps required technical capabilities to mature, open-source, maintained third-party libraries and asks the user to confirm the combined stack and library set.
- Confirmation gates: requirements depth, project purpose, document consent, tech stack consent, and high-risk operation confirmation.
- Text fallback for confirmation prompts: every approval or path choice must be answerable from plain text, not only UI buttons.
- Language adaptation: questions, confirmations, progress updates, and completion messages should match the user's current language.
- Templates: reusable source-of-truth documents for project, architecture, workflow, and operations.
- References: detailed stage guidance for frontend, backend, database, security, tools, and engineering baselines.
- Validation: a local script checks that the skill keeps its required files, routes, guardrails, and document layout intact.

## 🧭 Similar Project Comparison

Mature skill packs such as [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) and Superpowers focus on the full engineering lifecycle: spec, plan, build, test, review, security, performance, and shipping. Agent Project Kit focuses one layer earlier: turning a vague project idea into confirmed product and engineering source-of-truth before implementation starts.

| Compared with | Agent Project Kit emphasizes |
| --- | --- |
| Full-lifecycle skill packs | Reference scans, project initiation, source-of-truth documents, and implementation readiness before code. |
| Autonomous execution frameworks | User-confirmed decisions, one-question-at-a-time clarification, and explicit write or high-risk consent. |
| Generic prompt collections | Reusable templates, stage routing, source-of-truth change gates, and local validation. |

Use it as the primary router while the product shape is still forming. Pair it with mature lifecycle skills later for TDD, code review, security, performance, and launch.

## 🚫 What It Is Not

- Not a CLI that analyzes your codebase.
- Not a project management app.
- Not a generic prompt dump.
- Not a replacement for tests, review, Git discipline, or human product judgment.

## ⬇️ Clone Locally

Clone this repository to a local workspace:

```bash
git clone https://github.com/junjiang858/agent-project-kit.git
cd agent-project-kit
```

If you prefer a specific local path:

```bash
git clone https://github.com/junjiang858/agent-project-kit.git ~/skills/agent-project-kit
cd ~/skills/agent-project-kit
```

## 🛠 Install

Install the runtime skill files into your Codex skills directory:

```bash
./scripts/install.sh
```

The default install target is:

```text
${CODEX_HOME:-$HOME/.codex}/skills/agent-project-kit
```

Install into a project-local skills directory when you want the skill bundled with a specific project:

```bash
./scripts/install.sh /path/to/project/.codex/skills/agent-project-kit
```

Example:

```bash
./scripts/install.sh ~/projects/my-app/.codex/skills/agent-project-kit
```

Run the same command again to refresh an existing installation after pulling updates:

```bash
git pull
./scripts/install.sh
```

## 💬 Use

Invoke the skill explicitly:

```text
Use $agent-project-kit to turn my app idea into a project charter and implementation workflow.
```

By default, the skill guides project startup step by step. It should ask one question at a time, not dump a long intake questionnaire.

For vague ideas, it now uses four startup guardrails before writing files:

- Reference project scan gate: before deep refinement, provide 3-7 concrete projects, products, repos, plugins, templates, or adjacent implementations with direct project links, borrowable lessons, cautions, and direction choices.
- Requirements depth gate: clarify target users, core workflow, domain objects, operations, boundaries, risks, and objective acceptance criteria before drafting a PRD-quality charter.
- Document consent gate: do not create or update `AGENTS.md`, files under `docs/`, or other source-of-truth documents until the user agrees to that specific file.
- Tech stack confirmation gate: do not choose, lock, or write `docs/architecture/TECH_STACK.md` until the project purpose and charter facts are confirmed and the user agrees to enter technology selection.

During technology selection, it also uses a capability library scan gate: derive technical capabilities from the confirmed charter, research project-needed third-party libraries with direct links and maintenance evidence, then present the core stack plus included/deferred/rejected libraries for user confirmation.

Usage examples:

```text
Use $agent-project-kit to help me clarify a vague product idea. Ask one question at a time and do not write files until I approve.

Use $agent-project-kit to scan concrete reference projects for my vague app idea. Include direct project links, what to borrow, what not to copy, and direction choices before asking deeper requirements questions.

Use $agent-project-kit to turn this confirmed product direction into docs/project/PROJECT_CHARTER.md. First summarize the purpose and ask before writing the file.

Use $agent-project-kit to recommend exactly one tech stack after the project charter is confirmed. Ask before writing docs/architecture/TECH_STACK.md.

Use $agent-project-kit to run a capability library scan before confirming the tech stack. List project-needed third-party libraries with direct links, maintenance evidence, risks, and include/defer/reject decisions.

Use $agent-project-kit to create root AGENTS.md and docs/ops/TOOL_POLICY.md for this repo. Ask before writing each document.

Use $agent-project-kit to plan the backend skeleton and acceptance checklist.

Use $agent-project-kit to review whether this backend is safe enough to deploy.
```

## 🧯 Implementation Readiness Gate

Before the agent creates app scaffolding, package manager files, UI routes, API skeletons, database schemas, migrations, or runnable behavior, it audits whether the project source-of-truth documents are ready.

For Product MVP work, this usually means checking:

- `AGENTS.md`
- `docs/project/PROJECT_CHARTER.md`
- `docs/architecture/TECH_STACK.md`
- `docs/architecture/ENGINEERING_BASELINE.md`
- `docs/architecture/FRONTEND_PLAN.md`
- `docs/architecture/DATABASE_DESIGN.md`
- `docs/architecture/BACKEND_SPEC.md`
- `docs/workflow/AI_WORKFLOW.md`
- `docs/ops/TOOL_POLICY.md`
- `docs/ops/DEPLOYMENT.md`

If required documents are missing, the agent should list the stage-aware gaps instead of writing code. When multiple documents are missing, it should offer plain-text options rather than relying on UI buttons:

- Steady path: create or update the single most important next document, then review it.
- Accelerated path: authorize the named missing batch for this stage, create or update only those documents, then run the readiness audit again.

The accelerated path is still limited to the named documents; it is not permission to scaffold, install dependencies, or implement product behavior.

## 🧭 Source-of-Truth Change Gate

When a later task changes design or contracts, the agent should update the original project document before implementation:

- Frontend routes, components, states, data dependencies, or interactions: `docs/architecture/FRONTEND_PLAN.md`.
- APIs, validation, responses, errors, permissions, backend workflows, integrations, or data flow: `docs/architecture/BACKEND_SPEC.md`.
- Tables, fields, relations, indexes, enums, schemas, migrations, ownership, retention, or rollback: `docs/architecture/DATABASE_DESIGN.md`.

OpenSpec, GitHub Spec Kit, issue specs, and chat plans can guide a change, but they do not replace the repo's source-of-truth docs unless the project explicitly says so.

## 🎉 Goal And Completion Signal

Agent Project Kit makes each project-level run name its goal before it continues:

- Target outcome: what stage or project state the user wants to reach.
- Completion signal: what artifacts, confirmations, audits, or evidence prove the target has been reached.
- Next action: the next question, document, readiness audit, or implementation step.

For a new Product MVP, the default goal is usually: first MVP slice accepted after the project engineering baseline is ready.

This has two milestones. The project engineering baseline is reached when the project purpose is confirmed, the required source-of-truth documents are present or marked not applicable, the implementation readiness gate has passed, and the user has confirmed the readiness result or approved the next implementation step. The first MVP slice is reached when one approved product loop has been implemented and verified with fresh build, test, browser, API, CLI, worker, or run evidence.

When the baseline milestone is reached, the agent closes with a concise readiness message in the user's current language. For English users:

```text
🎉 Project engineering baseline is ready!

✅ The project goal, technical route, core documents, and implementation readiness gate are in place.
🚀 Next, you can start implementing the first approved product loop.
```

When the first MVP slice is complete, the second milestone message is:

```text
🎉 First MVP slice is complete!

✅ The first approved product loop has been implemented with run, build, browser, API, or task verification evidence.
🚀 Next, you can expand the remaining pages, data flows, APIs, jobs, or deployment path.
```

## 🧱 Workflow

The skill routes work through these stages:

1. Project initiation and MVP boundary
2. Reference project scan and direction choice
3. Project purpose confirmation and document consent
4. Technology stack decision with capability library scan and Git safety
5. Agent constitution and reusable skill workflow
6. Frontend page map and skeleton plan
7. Database design
8. Backend business spec and minimal skeleton
9. Architecture and security acceptance
10. Tool permission matrix
11. Deployment and AI workflow documents
12. Implementation readiness audit before scaffolding or code
13. First MVP slice implementation and verification
14. Goal milestone signals and language-adaptive completion messages

## 📁 Repository Layout

```text
.
├── SKILL.md                  # Runtime skill entry point
├── agents/openai.yaml        # Codex UI metadata
├── references/               # Stage-specific guidance loaded on demand
├── templates/                # Copyable project documents
├── examples/tiny-webapp/     # Small end-to-end example
├── scripts/install.sh        # Local installer
└── scripts/validate.py       # Repository validation
```

## 🗂 Generated Project Layout

By default, generated project documents should not be dumped into the repository root. Keep `AGENTS.md` as the root agent index and place detailed source-of-truth documents under `docs/`:

```text
.
├── AGENTS.md
└── docs/
    ├── project/PROJECT_CHARTER.md
    ├── architecture/TECH_STACK.md
    ├── architecture/ENGINEERING_BASELINE.md
    ├── architecture/FRONTEND_PLAN.md
    ├── architecture/DATABASE_DESIGN.md
    ├── architecture/BACKEND_SPEC.md
    ├── workflow/AI_WORKFLOW.md
    ├── ops/TOOL_POLICY.md
    └── ops/DEPLOYMENT.md
```

## 🧾 Templates

Copy templates into your project when the skill asks for stage artifacts:

- `templates/AGENTS.md`
- `templates/docs/project/PROJECT_CHARTER.md`
- `templates/docs/architecture/TECH_STACK.md`
- `templates/docs/architecture/ENGINEERING_BASELINE.md`
- `templates/docs/architecture/FRONTEND_PLAN.md`
- `templates/docs/architecture/DATABASE_DESIGN.md`
- `templates/docs/architecture/BACKEND_SPEC.md`
- `templates/docs/workflow/AI_WORKFLOW.md`
- `templates/docs/ops/TOOL_POLICY.md`
- `templates/docs/ops/DEPLOYMENT.md`

## ✅ Validate

Run local validation before publishing changes:

```bash
python3 scripts/validate.py
```

This checks required files, README language links, markdown fences, skill frontmatter, stage reference routing, generated-project document layout, and Product MVP baseline coverage.
It also checks that initiation guardrails remain present: reference project scan, requirements depth, document consent, tech stack confirmation, and a generic domain-object clarification flow instead of a one-domain hardcoded branch.

## 💡 Why This Exists

Many AI-assisted projects fail in the same way: the agent starts coding before the project has a stable shape. Agent Project Kit adds a small amount of structure at the exact points where drift usually begins: vague requirements, tech stack churn, missing tool boundaries, backend ambiguity, weak database design, and "trust me" security claims.

The goal is not more process. The goal is fewer expensive surprises.

## 📄 License

MIT
