# Agent Project Kit

[English](README.md) | [简体中文](README.zh-CN.md)

Agent Project Kit is a Codex skill for taking AI-assisted software projects from a vague idea to verified delivery.

It turns "just ask the agent to build it" into a staged workflow: clarify the project, choose a stack, set agent rules, plan frontend/backend/database work, define tool permissions, and require evidence before calling work done.

## Who It Is For

- Solo builders and small teams using Codex, Claude Code, Cursor, Copilot, or similar coding agents.
- People who want AI help but do not want the project to drift into unreviewable code.
- Projects that need lightweight process without adopting a full product-management platform.

## What It Is Not

- Not a CLI that analyzes your codebase.
- Not a project management app.
- Not a generic prompt dump.
- Not a replacement for tests, review, Git discipline, or human product judgment.

## Install

Clone this repository, then install the runtime skill files into your Codex skills directory:

```bash
git clone https://github.com/junjiang858/agent-project-kit.git
cd agent-project-kit
./scripts/install.sh
```

The default target is:

```text
${CODEX_HOME:-$HOME/.codex}/skills/agent-project-kit
```

You can install to another directory:

```bash
./scripts/install.sh /path/to/skills/agent-project-kit
```

## Use

Invoke the skill explicitly:

```text
Use $agent-project-kit to turn my app idea into a project charter and implementation workflow.
```

Typical requests:

```text
Use $agent-project-kit to help me choose a tech stack for this product idea.
Use $agent-project-kit to draft AGENTS.md and TOOL_POLICY.md for this repo.
Use $agent-project-kit to plan the backend skeleton and acceptance checklist.
Use $agent-project-kit to review whether this backend is safe enough to deploy.
```

## Workflow

The skill routes work through these stages:

1. Project initiation and MVP boundary
2. Technology stack and Git safety
3. Agent constitution and reusable skill workflow
4. Frontend page map and skeleton plan
5. Database design
6. Backend business spec and minimal skeleton
7. Architecture and security acceptance
8. Tool permission matrix
9. Deployment and AI workflow documents

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

## Templates

Copy templates into your project when the skill asks for stage artifacts:

- `templates/PROJECT_CHARTER.md`
- `templates/TECH_STACK.md`
- `templates/AGENTS.md`
- `templates/TOOL_POLICY.md`
- `templates/DATABASE_DESIGN.md`
- `templates/BACKEND_SPEC.md`
- `templates/AI_WORKFLOW.md`
- `templates/DEPLOYMENT.md`

## Validate

Run local validation before publishing changes:

```bash
python3 scripts/validate.py
```

This checks required files, README language links, markdown fences, skill frontmatter, and stage reference routing.

## Why This Exists

Many AI-assisted projects fail in the same way: the agent starts coding before the project has a stable shape. Agent Project Kit adds a small amount of structure at the exact points where drift usually begins: vague requirements, tech stack churn, missing tool boundaries, backend ambiguity, weak database design, and "trust me" security claims.

The goal is not more process. The goal is fewer expensive surprises.

## License

MIT
