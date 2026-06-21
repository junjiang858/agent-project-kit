# Project Initiation

Use this reference for cognition calibration, project charter work, technology selection, Git setup, and early project safety.

## Principles

- AI lowers the cost of writing code, not the need for product judgment, technical boundaries, and acceptance responsibility.
- The dangerous shortcut is handing a vague idea directly to AI for implementation.
- The first deliverable is clarity: target user, core problem, MVP scope, non-goals, risks, and acceptance criteria.
- The project purpose must be summarized and confirmed before technical or implementation planning.
- Technology choice should follow product shape, team capability, launch pressure, ecosystem maturity, documentation quality, security posture, and licensing.
- Git is the rollback and comparison mechanism for fast AI edits; initialize it before meaningful implementation.

## Stage Flow

1. Calibrate the project idea.
2. Discuss requirements without writing code.
3. Summarize the project purpose and ask the user to confirm or correct it.
4. Create an isolated project folder with a clear English name.
5. Produce `docs/project/PROJECT_CHARTER.md`.
6. Choose exactly one main technical route and write `docs/architecture/TECH_STACK.md`.
7. Define `docs/architecture/ENGINEERING_BASELINE.md` before implementation.
8. Initialize Git, create the first checkpoint, and define commit rules.

## Guided Intake

Ask one question at a time. Do not present a full intake questionnaire at project start.

Start with the smallest question that unlocks the next artifact:

1. What are you trying to build?
2. Who is it for?
3. What pain or workflow should the first version solve?
4. What would make the first version useful enough?

Do not ask all four at once. Ask the next question only after the previous answer is reflected back briefly.

## Project Purpose Confirmation

After target users and the core pain or workflow are clear, summarize the project purpose in plain language before drafting technical plans.

The summary must cover:

- Who the project serves.
- What problem or workflow it solves.
- What the product's core role is.
- What the MVP should cover first.

Ask the user to confirm or correct the summary. Do not choose a technology stack or plan implementation until the user confirms the project purpose.

Move in this order:

1. Gather enough context for `docs/project/PROJECT_CHARTER.md`.
2. Summarize the project purpose and get user confirmation.
3. Draft `docs/project/PROJECT_CHARTER.md` and ask for confirmation.
4. After confirmation, move to `docs/architecture/TECH_STACK.md`.
5. After stack confirmation, move to root `AGENTS.md`, `docs/architecture/ENGINEERING_BASELINE.md`, and `docs/ops/TOOL_POLICY.md`.
6. Only then discuss first implementation planning.

If the user says "not sure", offer 2-3 concrete options and ask them to choose one.

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
- Product lifecycle: Product MVP, throwaway prototype, internal tool, or platform.
- Architecture track: Single Web App, Web + API, or Multi-App Platform.
- Frontend framework, backend framework, database, deployment target, UI library, SDKs.
- Production compatibility: which choices can remain after launch.
- Migration cost: which choices would be expensive to replace later.
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
I want to build a small project with AI, but the idea is still vague. Do not write code yet. Act as a product partner and technical advisor. Guide me step by step. Ask only one question at a time, reflect my answer briefly, and continue until there is enough context to draft docs/project/PROJECT_CHARTER.md.
Before recommending a stack or implementation plan, summarize who the project serves, what problem it solves, what the product does, and what the MVP covers first. Wait for my confirmation.
```

## Prompt: Unique Tech Stack

```text
Based on my project charter and product shape, recommend exactly one Product MVP technical stack. Explain architecture track, frontend, backend, database, deployment, UI library, key SDKs, production compatibility, migration cost, risks, rejected alternatives, and the rules for re-evaluating the stack later. Write the decision for docs/architecture/TECH_STACK.md. Do not start coding.
```

## Prompt: Git Checkpoint

```text
Inspect the current Git status and propose a stage checkpoint. Before committing, list the change scope, risky files, whether secrets or private config are present, and a recommended commit message. Do not commit until I confirm.
```
