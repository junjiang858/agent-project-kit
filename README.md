<h1 align="center">Agent Project Kit</h1>

<p align="center">
  <strong>Make coding agents clarify, document, and verify before they code.</strong>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License MIT" src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <a href="SKILL.md"><img alt="Agent Skill" src="https://img.shields.io/badge/Agent%20Skill-SKILL.md-555.svg"></a>
  <img alt="Codex" src="https://img.shields.io/badge/Codex-ready-111827.svg">
  <img alt="Project Governance" src="https://img.shields.io/badge/Project-Governance-7c3aed.svg">
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> ·
  <a href="#-what-it-does">What It Does</a> ·
  <a href="#-when-to-use-it">When To Use It</a> ·
  <a href="#-what-you-get">What You Get</a> ·
  <a href="#-how-it-works">How It Works</a> ·
  <a href="#-compared-with-similar-projects">Comparison</a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a>
</p>

---

> Stop letting coding agents turn vague ideas into messy repos.
>
> Agent Project Kit makes the agent clarify, confirm, document, choose a stack, and verify with evidence before it writes code.

Agent Project Kit is a Codex skill for governing AI-assisted software projects. It gives the agent a lightweight product and engineering operating system for the moment when the idea, users, scope, stack, data model, tool permissions, and acceptance criteria are not clear enough yet.

It is best used as the project router before implementation discipline takes over.

## 🚀 Quick Start

Clone the repository:

```bash
git clone https://github.com/junjiang858/agent-project-kit.git
cd agent-project-kit
```

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

Invoke the skill explicitly:

```text
Use $agent-project-kit to turn my app idea into a project charter and implementation workflow.
```

Refresh an existing installation after pulling updates:

```bash
git pull
./scripts/install.sh
```

Validate the repository before publishing changes:

```bash
python3 scripts/validate.py
```

## 🧩 What It Does

Agent Project Kit helps an agent:

- Turn vague ideas into PRD-quality project charters.
- Scan concrete reference projects with direct links before narrowing a vague idea.
- Ask for explicit consent before writing source-of-truth documents or locking major technical decisions.
- Choose one main technical route based on product shape, lifecycle, team capability, migration cost, and production compatibility.
- Review project-needed third-party libraries with links, maintenance evidence, and include/defer/reject decisions before confirming the stack.
- Treat default stack choices as candidates, not mandates: repository shape, UI library, and icon library must be justified by product shape, design-system evidence, and real package boundaries.
- Keep durable project facts under `docs/` instead of scattering them across chat history.
- Route later work as Project Baseline, Contract-Changing Feature, Bounded Feature, or Local Fix so small changes do not rerun the full baseline.
- Distinguish Engineering Baseline Ready, First MVP Slice Complete, MVP Scope Incomplete, Full MVP Scope Complete, and Release Ready so milestone messages do not blur together.
- Require verification evidence instead of "trust me" completion claims.

## 🎯 When To Use It

| Situation | Use Agent Project Kit to |
| --- | --- |
| Vague product idea | Ask one question at a time, scan references, choose an MVP direction, and confirm the project purpose. |
| New repo or missing baseline | Create source-of-truth docs, tool rules, stack decisions, and readiness checks before implementation. |
| Stack or library choice | Compare one main route, rejected alternatives, capability libraries, maintenance evidence, and migration risks. |
| Contract-Changing Feature Path | Update affected source-of-truth docs before code changes. |
| Bounded Feature Path | Confirm the work stays inside approved contracts, then hand off to normal implementation discipline. |
| Local Fix Path | Avoid the full baseline flow and use the lightest direct path. |

## 📦 What You Get

The skill helps the agent create and maintain project source-of-truth files such as:

| Artifact | Purpose |
| --- | --- |
| `AGENTS.md` | Project-level agent constitution and index into source-of-truth docs. |
| `docs/project/PROJECT_CHARTER.md` | Users, problem, MVP scope, workflows, domain objects, risks, and acceptance criteria. |
| `docs/architecture/TECH_STACK.md` | One chosen stack, rejected alternatives, migration cost, production compatibility, and re-evaluation rules. |
| `docs/architecture/ENGINEERING_BASELINE.md` | Scripts, quality gates, tests, migrations, environment rules, and commit discipline. |
| `docs/architecture/FRONTEND_PLAN.md` | Page map, Design Read, Product MVP UI Quality Gate, design system, component boundaries, and browser UI verification. |
| `docs/architecture/DATABASE_DESIGN.md` | Domain objects, tables, fields, relations, indexes, migrations, ownership, and rollback notes. |
| `docs/architecture/BACKEND_SPEC.md` | API contracts, permissions, backend workflows, integrations, data flow, and error handling. |
| `docs/workflow/AI_WORKFLOW.md` | Clarify, spec, plan, implement, verify, and archive workflow. |
| `docs/ops/TOOL_POLICY.md` | Default tools, project-specific tools, and high-risk confirmation gates. |
| `docs/ops/DEPLOYMENT.md` | Local, staging, production, environment variables, health checks, and rollback. |
| `docs/features/`, `docs/changes/`, `docs/decisions/`, `docs/agent-project-kit/` | Stable feature notes, one-change detail, long-term decisions, and process artifacts that should not bloat current-state docs. |

## ⚙️ How It Works

For project-level work, the skill routes the agent through this flow:

```text
clarify the stage
→ scan concrete references
→ confirm project purpose
→ ask before writing source-of-truth docs
→ choose one stack plus capability libraries
→ audit implementation readiness
→ classify later work by contract impact
→ implement only after the right gate is satisfied
→ report verification evidence
```

The key gates are:

- **Reference Project Scan Gate**: show 3-7 concrete projects, products, repos, plugins, templates, or adjacent implementations with direct links before narrowing a vague idea.
- **Requirements Depth Gate**: clarify users, core workflow, domain objects, operations, boundaries, risks, and objective acceptance criteria before drafting a PRD-quality charter.
- **Document Consent Gate**: do not create or update `AGENTS.md`, files under `docs/`, or other source-of-truth documents until the user agrees to that specific file.
- **Tech Stack Confirmation Gate**: do not lock `docs/architecture/TECH_STACK.md` until the project purpose and charter facts are confirmed.
- **Capability Library Scan Gate**: map project-needed capabilities to mature, maintained libraries before confirming the stack.
- **Project Specification Readiness Gate**: do not scaffold app code, package files, UI routes, APIs, schemas, migrations, or runnable behavior until required source-of-truth docs are ready.
- **Source-of-Truth Change Gate**: when a later task changes design, APIs, data, permissions, tools, deployment, or operations, update the original source-of-truth document before implementation.
- **Source-of-Truth Distillation**: keep durable current contracts in core docs, and move feature, change, decision, or process detail to `docs/features/`, `docs/changes/`, `docs/decisions/`, or `docs/agent-project-kit/`.

The Reference project scan gate requires direct project links. The Capability library scan gate reviews project-needed third-party libraries with direct links and maintenance evidence.

When multiple readiness documents are missing, the skill offers plain-text options: a steady path for the single next document or an accelerated path for a named batch. All confirmation prompts must be answerable in text, even when a UI choice tool is available, and they should match the user's current language.

Optional accelerators such as Superpowers, OpenSpec, GitHub Spec Kit, issue trackers, and similar tools can strengthen the workflow. If they are unavailable, Agent Project Kit falls back to its built-in clarify, Contract Impact Check, plan, implement, verify, and evidence workflow.

## ✅ Goal And Completion Signal

Each project-level run starts by naming the target outcome, completion signal, and next action. For a new Product MVP, the default target is usually first MVP slice accepted after the project engineering baseline is ready.

Baseline completion means the project purpose is confirmed, required source-of-truth documents are present or marked not applicable, readiness has passed, and the user has approved the result or next implementation step. First MVP slice completion means one approved product loop has been implemented and verified with fresh build, test, browser, API, CLI, worker, or run evidence.

After the first slice, the skill uses MVP closure states: `MVP Scope Incomplete`, `Full MVP Scope Complete`, and `Release Ready`. The MVP Closure Sentinel runs only when triggered by completion, release, remaining-risk, or next-step questions, or before the agent claims full MVP or release readiness. Ordinary local fixes and code explanations do not run a fresh full-project closure audit.

Completion messages are language-adaptive completion messages; they should match the user's current language.

```text
🎉 Project engineering baseline is ready!

✅ The project goal, technical route, core documents, and implementation readiness gate are in place.
🚀 Next, you can start implementing the first approved product loop.
```

```text
🎉 First MVP slice is complete!

✅ The first approved product loop has been implemented with run, build, browser, API, or task verification evidence.
🚀 Next, you can expand the remaining pages, data flows, APIs, jobs, or deployment path.
```

```text
🎉 MVP scope is complete!

✅ The documented MVP scope has been implemented and verified with current evidence.
🚀 Next, move into formal product development: release validation, architecture hardening, user feedback, and the next planned version.
```

```text
🎉 Release validation passed!

✅ The MVP scope, deployment environment, regression checks, security boundaries, and operational readiness are verified with current evidence.
🚀 Next, release, monitor real usage, and plan post-release fixes and the next version.
```

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

## 🔍 Why It Is Different

Agent Project Kit is not a generic prompt collection. It focuses on the governing layer around AI implementation:

| Capability | What this skill adds |
| --- | --- |
| Stage routing | The agent loads only the reference needed for the current phase. |
| Reference grounding | Vague ideas are compared against concrete projects with direct links before requirements are narrowed. |
| Stack discipline | Technology choices include one main route, rejected alternatives, capability libraries, maintenance evidence, and re-evaluation rules. |
| User control | Source-of-truth docs, stack decisions, and high-risk operations require explicit confirmation. |
| Frontend quality | Product MVP work requires a Design Read, design system tokens, state contracts, anti-slop guardrails, and browser verification. |
| Source-of-truth maintenance | Durable current contracts stay in core docs; feature, change, decision, and process detail is routed to dedicated directories. |
| Language adaptation | Questions, confirmations, progress updates, and completion messages match the user's current language. |
| Local validation | `scripts/validate.py` checks required files, reference routing, guardrails, templates, README links, and markdown fences. |

## 🧭 Compared With Similar Projects

| Compared with | Common emphasis | Agent Project Kit emphasis |
| --- | --- | --- |
| OpenAI/Codex skills model | Reusable workflows packaged as `SKILL.md` plus optional scripts, references, assets, and progressive disclosure. | A specific project-governance workflow built on that model. |
| `anthropics/skills` | Reference implementations that demonstrate many skill patterns and file-processing workflows. | A focused operating system for AI-assisted software project baselines. |
| `addyosmani/agent-skills` and other lifecycle packs | Spec, plan, build, test, review, security, performance, and ship discipline. | Upstream project clarity, source-of-truth docs, implementation readiness, contract-change routing, and bounded handoff. |
| OpenSpec, GitHub Spec Kit, issue specs | Change proposals, specs, tasks, archival, and implementation tracking. | Repo-level current-state source-of-truth priority and fallback when external spec tools are unavailable. |
| Autonomous execution frameworks | More continuous agent execution after approval. | User-confirmed decisions, one-question-at-a-time clarification, and explicit write or high-risk consent. |
| Generic prompt collections | Reusable prompts and role instructions. | Templates, references, stage routing, document gates, and repository validation. |

Use Agent Project Kit as the primary router while the product shape or contracts are still forming. Pair it with mature lifecycle skills later for TDD, code review, security, performance, and launch.

## 🛡️ Safety And Trust

The install script copies runtime skill files and helper scripts into the target directory:

- `SKILL.md`
- `agents/`
- `references/`
- `templates/`
- `scripts/`

It does not install dependencies, scaffold an application, modify package manager files, run remote code, or change your project documents. Project documents and implementation files are created only when the user asks for them or approves the specific document/action through the skill workflow.

Run validation with:

```bash
python3 scripts/validate.py
```

The validator checks required files, README language links, markdown fences, skill frontmatter, stage reference routing, generated-project document layout, Product MVP baseline coverage, Product MVP UI Quality Gate coverage, MVP closure semantics, implementation handoff, source-of-truth distillation, and template paths.

As with any skill or plugin, review the files before installing and test the workflow in your own environment before relying on it for critical work.

## 📁 Repository Layout

```text
.
├── SKILL.md                  # Runtime skill entry point
├── agents/openai.yaml        # Codex UI metadata
├── references/               # Stage-specific guidance loaded on demand
├── templates/                # Copyable project documents
├── examples/tiny-webapp/     # Small end-to-end example
├── scripts/mvp_closure_snapshot.py # Cacheable MVP closure evidence snapshot
├── scripts/install.sh        # Local installer
└── scripts/validate.py       # Repository validation
```

## 🗂️ Generated Project Layout

Generated project documents should not be dumped into the repository root. Keep `AGENTS.md` as the root agent index and place detailed source-of-truth documents under `docs/`:

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
    ├── features/<feature-name>.md
    ├── changes/<date-or-id>-<change-name>.md
    ├── decisions/ADR-<number>-<topic>.md
    ├── agent-project-kit/PROCESS_ARTIFACTS.md
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
- `templates/docs/features/FEATURE.md`
- `templates/docs/changes/CHANGE.md`
- `templates/docs/decisions/ADR.md`
- `templates/docs/agent-project-kit/PROCESS_ARTIFACTS.md`
- `templates/docs/workflow/AI_WORKFLOW.md`
- `templates/docs/ops/TOOL_POLICY.md`
- `templates/docs/ops/DEPLOYMENT.md`

## 🚫 What It Is Not

- Not a full autonomous codebase analyzer; the optional snapshot script only caches evidence for agent review.
- Not a project management app.
- Not a generic prompt dump.
- Not a replacement for tests, review, Git discipline, or human product judgment.
- Not a reason to skip implementation skills once the baseline is ready.

## 📄 License

MIT
