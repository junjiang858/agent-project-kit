# Project Initiation

Use this reference for cognition calibration, project charter work, technology selection, Git setup, and early project safety.

## Principles

- AI lowers the cost of writing code, not the need for product judgment, technical boundaries, and acceptance responsibility.
- The dangerous shortcut is handing a vague idea directly to AI for implementation.
- The first deliverable is clarity: target user, core problem, MVP scope, non-goals, risks, and acceptance criteria.
- Technology choice should follow product shape, team capability, launch pressure, ecosystem maturity, documentation quality, security posture, and licensing.
- Git is the rollback and comparison mechanism for fast AI edits; initialize it before meaningful implementation.

## Stage Flow

1. Calibrate the project idea.
2. Create an isolated project folder with a clear English name.
3. Discuss requirements without writing code.
4. Produce `PROJECT_CHARTER.md`.
5. Choose exactly one main technical route and write `TECH_STACK.md`.
6. Initialize Git, create the first checkpoint, and define commit rules.

## Project Charter Checklist

- Target users and their concrete scenario.
- Problem statement in one sentence.
- MVP scope: must-have, explicit non-goals, postponed items.
- Core pages or user flows.
- Core data objects.
- Business rules and acceptance criteria.
- Technical constraints, budget, launch target, and known risks.
- Open questions that must be resolved before code.

## Technology Decision Checklist

- Product shape: web, mini program, app, backend service, automation, hybrid.
- Frontend framework, backend framework, database, deployment target, UI library, SDKs.
- Reasons for the chosen route.
- Rejected alternatives and why they are not the default route.
- Risk notes: maintenance, security, license, ecosystem, hosting, migration cost.
- Rule: future new frameworks or major libraries require explicit re-evaluation.

## Git Discipline

- Initialize Git immediately after project creation.
- Commit at stable stage boundaries, not only after large changes.
- Before commit, inspect status, diff, tests, and risk files.
- Before remote push or public release, scan for secrets, private configs, accounts, test data, and private assets.
- Put commit rhythm and forbidden files in the Agent constitution.

## Prompt: Vague Idea to Charter

```text
I want to build a small project with AI, but the idea is still vague. Do not write code yet. Act as a product partner and technical advisor. Ask about target users, core problem, MVP boundary, technical risks, data objects, business flow, and acceptance criteria until the project is clear enough to turn into PROJECT_CHARTER.md.
```

## Prompt: Unique Tech Stack

```text
Based on my project charter and product shape, recommend exactly one technical stack. Explain frontend, backend, database, deployment, UI library, key SDKs, reasons, risks, rejected alternatives, and the rules for re-evaluating the stack later. Do not start coding.
```

## Prompt: Git Checkpoint

```text
Inspect the current Git status and propose a stage checkpoint. Before committing, list the change scope, risky files, whether secrets or private config are present, and a recommended commit message. Do not commit until I confirm.
```
