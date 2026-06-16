---
name: agent-project-kit
description: Use when planning, building, or reviewing AI-assisted software projects from vague idea to delivery, especially for Vibe Coding, project charters, tech stack decisions, Agent constitution, skill workflows, frontend/backend/database skeletons, security acceptance, tool permissions, or AI-friendly engineering rules.
---

# Agent Project Kit

## Overview

Guide an AI-assisted software project through staged clarification, documented decisions, implementation boundaries, and evidence-based acceptance. Treat AI as a collaborator that needs product context, engineering rules, and verification gates before it writes or changes code.

## Core Rule

Do not jump from a vague idea to implementation. First identify the current project stage, load only the relevant reference, produce or update the stage artifact, then ask for approval before irreversible or high-risk work.

## Guided Interaction

Ask one question at a time when gathering missing project context. Do not present a full intake questionnaire unless the user explicitly asks for one.

For vague project starts, use this loop:

1. State the current stage in one short sentence.
2. Ask the single most important next question.
3. Wait for the answer.
4. Reflect the answer into the current artifact.
5. Continue only to the next necessary question or draft.

If two details are inseparable, ask at most two short questions. Prefer multiple-choice options when they reduce effort.

## Stage Router

| User situation | Load | Primary output |
| --- | --- | --- |
| Vague idea, unsure what AI can do, or first project | `references/project-initiation.md` | clarified problem, MVP boundary, project charter |
| Choosing stack, repository setup, version safety | `references/project-initiation.md` | tech stack decision, Git checkpoint rule |
| Need project-level rules, AGENTS.md, or reusable process | `references/engineering-rules.md` | Agent constitution, candidate skill workflow |
| Planning pages, UX states, components, frontend skeleton | `references/frontend.md` | page map, component map, frontend skeleton plan |
| Designing tables, fields, relations, migrations | `references/database.md` | database design document |
| Defining APIs, backend business boundaries, backend skeleton, architecture acceptance | `references/backend.md` | backend business spec, minimal backend skeleton, acceptance report |
| Checking backend safety, secrets, logs, dependencies, database risk | `references/security.md` | security boundary table, bottom-layer security evidence |
| Deciding which tools or MCPs AI may use | `references/tool-policy.md` | `TOOL_POLICY.md` or tool permission matrix |
| Need whole-project flow, default stack, or reusable prompt pack | `references/workflow-checklists.md` | roadmap, docs checklist, default workflow docs |

## Execution Flow

1. Classify the request into one stage from the router.
2. Read the matching reference file before giving instructions or editing project files.
3. Check whether required upstream artifacts exist. If they are missing, create or request only the next missing artifact, not the entire chain.
4. When information is missing, use Guided Interaction instead of dumping a long checklist of questions.
5. Produce the smallest useful stage artifact: plan, document, checklist, matrix, skeleton, or acceptance report.
6. For implementation work, preserve Git checkpoints and return evidence: commands run, tests, build, browser/API checks, or security proof.
7. For high-risk operations involving production data, secrets, deployment, payments, cloud resources, database writes, or destructive file changes, stop and request explicit confirmation.

## Required Artifacts

When a `templates/` directory is available, copy and adapt its matching template instead of drafting the artifact from scratch.

- `PROJECT_CHARTER.md`: target user, problem, MVP scope, non-goals, risks, acceptance criteria.
- `TECH_STACK.md`: chosen stack, rejected alternatives, re-evaluation rules, forbidden drift.
- `AGENTS.md` or equivalent Agent constitution: project rules, completion definition, tests, Git discipline, conflict handling.
- `TOOL_POLICY.md`: default tools, project tools, high-risk confirmations.
- `DATABASE_DESIGN.md`: objects, tables, fields, relations, indexes, security notes.
- `BACKEND_SPEC.md`: business rules, API boundary, permissions, data flow, error handling.
- `AI_WORKFLOW.md`: clarify, spec, plan, implement, verify, archive.
- `DEPLOYMENT.md`: local, staging, production, environment variables, health checks, rollback.

## Common Mistakes

| Mistake | Correction |
| --- | --- |
| Asking AI to code before scope is clear | Create or update the project charter first. |
| Letting AI choose many possible stacks forever | Discuss alternatives, then commit to one documented main route. |
| Treating Git as an afterthought | Initialize Git early and commit every stable stage. |
| Putting every rule into the Agent constitution | Keep project rules short; move task-specific procedures into skills or references. |
| Accepting "it is secure" as proof | Require file locations, code paths, tests, and role-based evidence. |
| Opening every tool to AI | Separate default-open tools, project-specific tools, and high-risk confirmation gates. |

## Source Notes

This skill is distilled from the local Obsidian handbook `AI 编程项目实战手册` and intentionally excludes image indexes and screenshot assets. Keep the skill procedural, concise, and evidence-oriented.
