# Agent Project Kit

[English](README.md) | [简体中文](README.zh-CN.md)

Agent Project Kit is a Codex skill for taking AI-assisted software projects from a vague idea to verified delivery.

It turns "just ask the agent to build it" into a staged workflow: clarify the project, choose a stack, set agent rules, plan frontend/backend/database work, define tool permissions, and require evidence before calling work done.

The default posture is Product MVP: small feature scope, but a production-compatible repo shape, stack decision, and engineering baseline.

## Who It Is For

- Solo builders and small teams using Codex, Claude Code, Cursor, Copilot, or similar coding agents.
- People who want AI help but do not want the project to drift into unreviewable code.
- Projects that need lightweight process without adopting a full product-management platform.

## What It Is Not

- Not a CLI that analyzes your codebase.
- Not a project management app.
- Not a generic prompt dump.
- Not a replacement for tests, review, Git discipline, or human product judgment.

## Clone Locally

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

## Install

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

## Use

Invoke the skill explicitly:

```text
Use $agent-project-kit to turn my app idea into a project charter and implementation workflow.
```

By default, the skill guides project startup step by step. It should ask one question at a time, not dump a long intake questionnaire.

For vague ideas, it now uses three startup guardrails before writing files:

- Requirements depth gate: clarify target users, core workflow, domain objects, operations, boundaries, risks, and objective acceptance criteria before drafting a PRD-quality charter.
- Document consent gate: do not create or update `AGENTS.md`, files under `docs/`, or other source-of-truth documents until the user agrees to that specific file.
- Tech stack confirmation gate: do not choose, lock, or write `docs/architecture/TECH_STACK.md` until the project purpose and charter facts are confirmed and the user agrees to enter technology selection.

Usage examples:

```text
Use $agent-project-kit to help me clarify a vague product idea. Ask one question at a time and do not write files until I approve.

Use $agent-project-kit to turn this confirmed product direction into docs/project/PROJECT_CHARTER.md. First summarize the purpose and ask before writing the file.

Use $agent-project-kit to recommend exactly one tech stack after the project charter is confirmed. Ask before writing docs/architecture/TECH_STACK.md.

Use $agent-project-kit to create root AGENTS.md and docs/ops/TOOL_POLICY.md for this repo. Ask before writing each document.

Use $agent-project-kit to plan the backend skeleton and acceptance checklist.

Use $agent-project-kit to review whether this backend is safe enough to deploy.
```

## Workflow

The skill routes work through these stages:

1. Project initiation and MVP boundary
2. Project purpose confirmation and document consent
3. Technology stack decision and Git safety
4. Agent constitution and reusable skill workflow
5. Frontend page map and skeleton plan
6. Database design
7. Backend business spec and minimal skeleton
8. Architecture and security acceptance
9. Tool permission matrix
10. Deployment and AI workflow documents

## Repository Layout

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

## Generated Project Layout

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

## Templates

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

## Validate

Run local validation before publishing changes:

```bash
python3 scripts/validate.py
```

This checks required files, README language links, markdown fences, skill frontmatter, stage reference routing, generated-project document layout, and Product MVP baseline coverage.
It also checks that initiation guardrails remain present: requirements depth, document consent, tech stack confirmation, and a generic domain-object clarification flow instead of a one-domain hardcoded branch.

## Why This Exists

Many AI-assisted projects fail in the same way: the agent starts coding before the project has a stable shape. Agent Project Kit adds a small amount of structure at the exact points where drift usually begins: vague requirements, tech stack churn, missing tool boundaries, backend ambiguity, weak database design, and "trust me" security claims.

The goal is not more process. The goal is fewer expensive surprises.

## License

MIT
