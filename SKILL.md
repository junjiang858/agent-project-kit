---
name: agent-project-kit
description: Use when planning, building, or reviewing AI-assisted software projects from vague idea to delivery, especially for Vibe Coding, project charters, tech stack decisions, Agent constitution, skill workflows, frontend/backend/database skeletons, security acceptance, tool permissions, or AI-friendly engineering rules.
---

# Agent Project Kit

## Overview

Guide an AI-assisted software project through staged clarification, documented decisions, implementation boundaries, and evidence-based acceptance. Treat AI as a collaborator that needs product context, engineering rules, and verification gates before it writes or changes code.

## Core Rule

Do not jump from a vague idea to documents, technology choices, or implementation. First identify the current project stage, load only the relevant reference, clarify the minimum facts for that stage, and ask for explicit consent before creating or updating any project document file or before irreversible or high-risk work.

## Default Workflow Priority

When this skill is loaded or the user request matches AI-assisted project initiation, planning, architecture, frontend, backend, database, security, tool permissions, acceptance, or delivery workflow, Agent Project Kit is the default primary workflow.

Use overlapping skills, including `superpowers` planning, TDD, execution, or review skills, only as auxiliary method libraries. Do not let overlapping skills replace this skill's stage router, confirmation gates, or required artifacts.

Skip this priority only when the user explicitly names another skill or process as the primary workflow, or when the task is a local code fix, code explanation, single command, or other non-project-level task.

## Guided Interaction

Ask one question at a time when gathering missing project context. Do not present a full intake questionnaire unless the user explicitly asks for one.

For vague project starts, use this loop:

1. State the current stage in one short sentence.
2. Ask the single most important next question.
3. Wait for the answer.
4. Reflect the answer into the current artifact.
5. Continue only to the next necessary question or draft.

If two details are inseparable, ask at most two short questions. Prefer multiple-choice options when they reduce effort.

Do not treat a one-sentence project idea as enough context for a project charter. When the user's wording contains ambiguous domain nouns or product-shape terms, clarify what they mean in this project before drafting a PRD-quality artifact. Identify the core objects the product manages, the main operations users perform on them, and the boundaries around roles, data, external systems, execution, observability, and safety.

## Project Purpose Confirmation

Before moving beyond project initiation, summarize the project purpose for the user: who it serves, what problem it solves, what the product does, and what the MVP should cover first. Ask the user to confirm or correct that summary.

Do not move into technology stack, frontend, backend, database, or implementation planning until the user confirms the project purpose summary.

## Document Consent Gate

Do not create, copy, overwrite, move, or edit any project source-of-truth document until the user explicitly agrees to write that specific document or has directly asked for that exact document to be written. This includes `AGENTS.md`, every file under `docs/`, and any root-level planning document.

Before writing a document file:

1. Confirm the current stage artifact in conversation.
2. State the target path and what the document will contain.
3. Ask whether to write or update that file.
4. Wait for an affirmative answer.

Consent applies only to the named document and current stage. Writing `docs/project/PROJECT_CHARTER.md` does not imply permission to write `docs/architecture/TECH_STACK.md`, `AGENTS.md`, or engineering baseline files.

The agent may discuss, summarize, or propose a short outline in chat before consent, but must not create or modify document files before consent.

## Requirements Depth Gate

Before asking to write `docs/project/PROJECT_CHARTER.md`, gather enough context for a PRD-quality charter. At minimum, the conversation must cover:

- Target user or user role.
- Core scenario and pain point.
- MVP outcome and first-use workflow.
- Must-have features, explicit non-goals, and postponed items.
- Core domain objects and important data, resources, or external systems.
- Key business rules, permissions, and safety constraints.
- Acceptance criteria that can be checked objectively.
- Open questions that would affect architecture or implementation.

If these are not known yet, keep asking one focused question at a time. If the user is unsure, offer 2-3 concrete options and ask them to choose or revise one.

## Stage Router

| User situation | Load | Primary output |
| --- | --- | --- |
| Creating or reorganizing project source-of-truth documents | `references/document-layout.md` | root `AGENTS.md` index plus docs under `docs/` |
| Vague idea, unsure what AI can do, or first project | `references/project-initiation.md` | clarified problem, MVP boundary, project charter |
| Choosing stack, repository setup, version safety | `references/project-initiation.md`, `references/architecture-baseline.md` | tech stack decision, architecture track, Git checkpoint rule |
| Defining quality gates, scripts, CI, migrations, env, or repo hygiene | `references/engineering-baseline.md` | engineering baseline and acceptance checklist |
| Need project-level rules, AGENTS.md, or reusable process | `references/engineering-rules.md` | Agent constitution, candidate skill workflow |
| Planning pages, UX states, components, frontend skeleton | `references/frontend.md` | page map, component map, frontend skeleton plan |
| Designing tables, fields, relations, migrations | `references/database.md` | database design document |
| Defining APIs, backend business boundaries, backend skeleton, architecture acceptance | `references/backend.md` | backend business spec, minimal backend skeleton, acceptance report |
| Checking backend safety, secrets, logs, dependencies, database risk | `references/security.md` | security boundary table, bottom-layer security evidence |
| Deciding which tools or MCPs AI may use | `references/tool-policy.md` | `docs/ops/TOOL_POLICY.md` or tool permission matrix |
| Need whole-project flow, default stack, or reusable prompt pack | `references/workflow-checklists.md` | roadmap, docs checklist, default workflow docs |

## Execution Flow

1. Classify the request into one stage from the router.
2. Read the matching reference file before giving instructions or editing project files.
3. When creating project documents, use `references/document-layout.md` unless the user explicitly requests a different layout.
4. Check whether required upstream artifacts exist. If they are missing, request only the next missing artifact or fact, not the entire chain.
5. When information is missing, use Guided Interaction instead of dumping a long checklist of questions.
6. For project initiation, satisfy Requirements Depth Gate and Project Purpose Confirmation before asking to write the project charter.
7. For every document file, satisfy Document Consent Gate before creating or updating it.
8. Produce the smallest useful approved stage artifact: plan, document, checklist, matrix, skeleton, or acceptance report.
9. For implementation work, preserve Git checkpoints and return evidence: commands run, tests, build, browser/API checks, or security proof.
10. For high-risk operations involving production data, secrets, deployment, payments, cloud resources, database writes, or destructive file changes, stop and request explicit confirmation.

## Required Artifacts

When a `templates/` directory is available, copy and adapt its matching template instead of drafting the artifact from scratch.

- `AGENTS.md`: root-level Agent constitution and index into project documents.
- `docs/project/PROJECT_CHARTER.md`: target user, problem, MVP scope, non-goals, risks, acceptance criteria.
- `docs/architecture/TECH_STACK.md`: chosen stack, architecture track, rejected alternatives, re-evaluation rules, forbidden drift.
- `docs/architecture/ENGINEERING_BASELINE.md`: scripts, code quality, CI, migrations, env, testing, commit discipline.
- `docs/architecture/FRONTEND_PLAN.md`: pages, routes, components, states, design system, frontend skeleton plan.
- `docs/architecture/DATABASE_DESIGN.md`: objects, tables, fields, relations, indexes, security notes.
- `docs/architecture/BACKEND_SPEC.md`: business rules, API boundary, permissions, data flow, error handling.
- `docs/workflow/AI_WORKFLOW.md`: clarify, spec, plan, implement, verify, archive.
- `docs/ops/TOOL_POLICY.md`: default tools, project tools, high-risk confirmations.
- `docs/ops/DEPLOYMENT.md`: local, staging, production, environment variables, health checks, rollback.

## Common Mistakes

| Mistake | Correction |
| --- | --- |
| Asking AI to code before scope is clear | Create or update the project charter first. |
| Planning implementation before confirming project purpose | Summarize the target user, problem, product role, and MVP; wait for user confirmation. |
| Letting AI choose many possible stacks forever | Discuss alternatives, then commit to one documented main route. |
| Treating Git as an afterthought | Initialize Git early and commit every stable stage. |
| Putting every rule into the Agent constitution | Keep project rules short; move task-specific procedures into skills or references. |
| Dumping every project document in the repository root | Keep only `AGENTS.md` as the root index; put detailed documents under `docs/`. |
| Choosing a throwaway MVP stack for a product MVP | Keep scope small, but choose a stack and repo shape that can grow without a core rewrite. |
| Accepting "it is secure" as proof | Require file locations, code paths, tests, and role-based evidence. |
| Opening every tool to AI | Separate default-open tools, project-specific tools, and high-risk confirmation gates. |

## Source Notes

This skill is distilled from the local Obsidian handbook `AI 编程项目实战手册` and intentionally excludes image indexes and screenshot assets. Keep the skill procedural, concise, and evidence-oriented.
