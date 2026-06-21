# Project Initiation

Use this reference for cognition calibration, project charter work, technology selection, Git setup, and early project safety.

## Principles

- AI lowers the cost of writing code, not the need for product judgment, technical boundaries, and acceptance responsibility.
- The dangerous shortcut is handing a vague idea directly to AI for implementation.
- The first deliverable is clarity, not a file: target user, core problem, MVP scope, non-goals, workflows, data objects, risks, and acceptance criteria.
- Early project discussion should expand the user's options with concrete reference projects, not only refine the first wording they gave.
- The project purpose must be summarized and confirmed before technical or implementation planning.
- No project document file should be created or updated until the user explicitly agrees to write that specific document.
- Technology choice should follow product shape, team capability, launch pressure, ecosystem maturity, documentation quality, security posture, and licensing.
- Git is the rollback and comparison mechanism for fast AI edits; initialize it before meaningful implementation.
- `PROJECT_CHARTER.md`, `TECH_STACK.md`, and `ENGINEERING_BASELINE.md` alone are not enough to begin a Product MVP scaffold when the project also has frontend, backend, database, tool execution, deployment, or AI workflow concerns.

## Interaction Defaults

### Confirmation Prompt Rule

Any confirmation, consent, approval, or path-choice prompt must include plain-text options in the assistant message. Do not depend on UI buttons, `request_user_input`, AskUserQuestion, or host-specific quick actions.

### User Language Rule

Use the user's current language for questions, confirmations, progress updates, final answers, and milestone messages unless the user asks for another language.

## Stage Flow

1. Calibrate the project idea.
2. Run a Reference Project Scan with direct project links before narrowing the idea.
3. Ask the user to choose, combine, or reject a direction from the scan.
4. Discuss requirements without writing code.
5. Summarize the project purpose and ask the user to confirm or correct it.
6. Ask whether to write `docs/project/PROJECT_CHARTER.md`; wait for explicit consent.
7. Create or update only the approved project charter document.
8. Ask whether to move to technology selection.
9. Run the Capability Library Scan Gate based on confirmed project capabilities.
10. Choose exactly one main technical route plus the included/deferred/rejected third-party library set, then ask whether to write `docs/architecture/TECH_STACK.md`.
11. Define `docs/architecture/ENGINEERING_BASELINE.md` before implementation, again only after consent to write it.
12. Define the remaining implementation-readiness documents before scaffolding: `AGENTS.md`, `docs/architecture/FRONTEND_PLAN.md`, `docs/architecture/DATABASE_DESIGN.md`, `docs/architecture/BACKEND_SPEC.md`, `docs/workflow/AI_WORKFLOW.md`, `docs/ops/TOOL_POLICY.md`, and `docs/ops/DEPLOYMENT.md` as applicable.
13. Initialize Git, create the first documentation checkpoint, and define commit rules.
14. Only after the readiness set is complete should the agent ask whether to scaffold or implement the first approved MVP slice.
15. After implementation starts, keep the first deliverable narrow: one approved MVP slice with verification evidence. For web products this usually includes the first MVP page; for non-web projects it may be the first API, worker flow, CLI flow, automation run, or integration workflow.

## Guided Intake

Ask one question at a time. Do not present a full intake questionnaire at project start.

Start with the smallest question that unlocks the next artifact:

1. What are you trying to build?
2. Which linked reference direction feels closest after the Reference Project Scan?
3. Who is it for?
4. What pain or workflow should the first version solve?
5. What would make the first version useful enough?

Do not ask all five at once. Ask the next question only after the previous answer is reflected back briefly.

Do not stop after one sentence if the product domain is still ambiguous. Before the charter stage, unpack the core nouns in the user's idea:

- Managed objects: what entities, records, resources, jobs, content, tools, assets, users, or workflows does the product manage?
- User operations: what can users create, configure, trigger, inspect, compare, approve, publish, retry, archive, or delete?
- Input/output shape: what information goes in, what result comes out, and what examples define success or failure?
- Lifecycle and state: what statuses, transitions, history, versions, or rollback behavior matter?
- Boundaries: which roles, permissions, external systems, execution environments, data access, and safety limits apply?
- Evidence: what logs, metrics, audit events, screenshots, reports, or other records prove the workflow worked?

Use domain-specific examples only to reduce ambiguity, not as fixed required branches. For example, an AI-tool console may need tool type, invocation, schema, logs, and permission details; an order system may need order states, payment/refund boundaries, fulfillment steps, and audit trails; a dashboard may need the decisions users make from each metric.

## Reference Project Scan

After the user gives a vague product idea and before deep requirement refinement, search for or identify concrete reference projects. The goal is to expand the user's option space with real examples, not to prove that the idea is original.

The scan must include 3-7 specific projects, products, repositories, plugins, templates, or adjacent implementations. Prefer primary sources such as official sites, GitHub repositories, docs, plugin marketplace pages, or product pages.

Required output shape:

| Project | Direct link | Source type | What to borrow | What not to copy blindly | Direction impact |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Rules:

- Include a project name and direct link for every row.
- Include at least one open-source or inspectable implementation when the idea involves software users can reasonably build on.
- Separate direct competitors from adjacent inspiration; both can be useful.
- Explain concrete borrowable pieces such as onboarding, workflow shape, data model, plugin architecture, API surface, local-first design, community distribution, or pricing model.
- Name the risks of copying: overlarge scope, license constraints, closed ecosystem, stale repo, weak security model, expensive infrastructure, or mismatched target user.
- If current community state matters, use live search. If live search is unavailable, state the limitation and ask whether to continue with known examples.

After the table, present 2-4 direction choices grounded in the linked projects. Examples:

1. Keep the original product direction and borrow only workflow patterns.
2. Build a lighter version of one specific open-source project.
3. Shift to a plugin, extension, template, or integration around an existing ecosystem.
4. Choose a differentiated niche that the scan reveals is underserved.

Ask the user to choose, combine, or reject the directions. Do not proceed to Project Purpose Confirmation until the user chooses a direction or explicitly asks to continue with the original idea after reviewing the scan.

## Requirements Depth Gate

Before asking to write `docs/project/PROJECT_CHARTER.md`, ensure the conversation has enough facts for a PRD-quality charter:

- Reference project scan completed, including concrete links, direction choices, and the user's selected direction.
- Target users and concrete usage scenario.
- Problem statement and why the current workflow is painful.
- Product role: what the system does for the user and what it deliberately does not do.
- MVP workflow from entry to successful outcome.
- Must-have features, explicit non-goals, postponed features, and likely version 2 expansion.
- Core pages or surfaces, if user-facing.
- Core domain objects, resources, data, and external systems.
- Business rules, permissions, safety constraints, and failure modes.
- Objective acceptance criteria.
- Open questions that would change scope, architecture, or technical risk.

If these facts are incomplete, ask the next highest-value question instead of writing the document. If the user is unsure, offer 2-3 plausible choices and ask them to choose or edit one.

## Project Purpose Confirmation

After target users and the core pain or workflow are clear, summarize the project purpose in plain language before drafting technical plans.

The summary must cover:

- Who the project serves.
- What problem or workflow it solves.
- What the product's core role is.
- What the MVP should cover first.

Ask the user to confirm or correct the summary. Do not choose a technology stack or plan implementation until the user confirms the project purpose.

Move in this order:

1. Gather the initial idea.
2. Complete the Reference Project Scan and ask the user to choose a direction.
3. Gather enough context for `docs/project/PROJECT_CHARTER.md`.
4. Summarize the project purpose and get user confirmation.
5. Ask whether to write `docs/project/PROJECT_CHARTER.md`; state the target path and scope.
6. After document-write consent, create or update the charter and ask the user to review it.
7. After charter confirmation, ask whether to move to technology selection.
8. Extract required technical capabilities and complete the Capability Library Scan Gate.
9. Recommend exactly one technical route plus included/deferred/rejected third-party libraries, then get user confirmation before writing `docs/architecture/TECH_STACK.md`.
10. After stack confirmation and document-write consent, move to root `AGENTS.md`, `docs/architecture/ENGINEERING_BASELINE.md`, and `docs/ops/TOOL_POLICY.md`.
11. Before implementation, complete the project-specific readiness set: frontend plan for UI work, database design for persisted data, backend spec for API/service/tool execution, AI workflow for agent process, deployment plan for local or hosted runtime, and explicit security acceptance content for high-risk execution or secrets.
12. When multiple readiness documents are missing, identify the current stage and explain which missing documents directly unblock the next stage. Offer plain-text options: a steady path for the single most important next document and an accelerated path for the named missing batch. Do not depend on UI buttons.
13. Only then discuss first implementation planning for the first MVP slice.

If the user says "not sure", offer 2-3 concrete options and ask them to choose one.

## Project Charter Checklist

- Reference Project Scan: linked reference projects, borrowable ideas, cautions, and chosen direction.
- Target users, roles, and their concrete scenario.
- Problem statement in one sentence and current workaround.
- Product role and user value.
- MVP scope: must-have, explicit non-goals, postponed items.
- Core pages, surfaces, or user flows.
- Core domain objects, resources, data, external systems, and integrations.
- Operation model, inputs, outputs, state transitions, logs or evidence, and permission boundaries for configurable, executable, or workflow-driven resources.
- Business rules, safety rules, failure handling, and acceptance criteria.
- Technical constraints, budget, launch target, and known risks.
- Open questions that must be resolved before code.

## Technology Decision Checklist

- Product shape: web, mini program, app, backend service, automation, hybrid.
- Product lifecycle: Product MVP, throwaway prototype, internal tool, or platform.
- Architecture track: Single Web App, Web + API, or Multi-App Platform.
- Frontend framework, backend framework, database, deployment target, UI library, SDKs.
- Capability Library Scan: required technical capabilities, mature open-source candidates, direct links, maintenance evidence, and include/defer/reject decisions.
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

## Implementation Readiness Audit

When the user says "create the project", "start coding", "build the app", "scaffold it", or similar, audit documents before writing implementation files.

Required answer shape:

1. State whether implementation is ready.
2. List present source-of-truth documents.
3. State the current stage and the next stage the user is trying to enter.
4. List only the missing documents that directly unblock the next stage, with one short reason for each.
5. Offer two choices:
   - Steady path: create or update the single most important next document, then ask the user to review it before continuing.
   - Accelerated path: create or update the named missing batch for this stage, then run the implementation readiness audit.

Render the choices as plain-text options, such as `A. Steady path` and `B. Accelerated path`, and name the exact document paths covered by each. Do not depend on UI buttons or host-specific quick actions.

Do not create `apps/`, `packages/`, UI screens, API controllers, database schemas, package manager files, or runnable behavior while the audit has missing required documents. A bootstrap-only exception must be explicitly confirmed and must stay limited to empty folders, root config, Git setup, and documentation plumbing.

## Prompt: Vague Idea to Charter

```text
I want to build a small project with AI, but the idea is still vague. Do not write code yet. Act as a product partner and technical advisor. Guide me step by step. Ask only one question at a time, reflect my answer briefly, and continue until there is enough context to draft docs/project/PROJECT_CHARTER.md.
Before narrowing requirements, scan for 3-7 concrete reference projects with direct project links, explain what to borrow and what not to copy, then ask me to choose or revise a direction.
Before recommending a stack or implementation plan, summarize who the project serves, what problem it solves, what the product does, and what the MVP covers first. Wait for my confirmation. After I confirm the purpose, ask whether you should write docs/project/PROJECT_CHARTER.md and do not create or edit that file until I explicitly agree.
```

## Prompt: Implementation Readiness Audit

```text
Before creating files outside docs or AGENTS.md, audit whether this project is ready for implementation. List the confirmed documents present, identify the current stage and the next stage, then list only the missing source-of-truth documents that directly unblock that next stage. Explain why each missing document matters now. Offer plain-text options: `A. Steady path` for the single most important next document, or `B. Accelerated path` for the named missing batch. Do not depend on UI buttons. Do not scaffold apps, packages, UI, API, database, or runnable behavior until the readiness set is complete.
```

## Prompt: Unique Tech Stack

```text
Based on my project charter and product shape, recommend exactly one Product MVP technical stack. Before confirming the stack, run a capability library scan: extract required technical capabilities, research mature open-source or inspectable third-party libraries with direct links and maintenance evidence, and classify each as Included, Deferred, or Rejected. Explain architecture track, frontend, backend, database, deployment, UI library, key SDKs, production compatibility, migration cost, risks, rejected alternatives, and the rules for re-evaluating the stack later. Write the decision for docs/architecture/TECH_STACK.md only after I confirm the combined stack and library set. Do not start coding.
```

## Prompt: Git Checkpoint

```text
Inspect the current Git status and propose a stage checkpoint. Before committing, list the change scope, risky files, whether secrets or private config are present, and a recommended commit message. Do not commit until I confirm.
```
