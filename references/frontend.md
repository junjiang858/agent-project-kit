# Frontend

Use this reference when planning pages, components, UI states, frontend architecture, design tokens, or a first frontend skeleton.

## Frontend Understanding

Frontend is the user entry, interaction flow, visual state, and data presentation layer. It is not only "making things look good."

Describe frontend needs with:

- Pages and the user goal for each page.
- Components: forms, lists, detail views, dialogs, navigation, upload, filters.
- States: loading, empty, error, success, disabled, optimistic updates.
- Data source for each view and the backend API that provides it.
- Design style, component library, icon library, responsive rules, and accessibility expectations.

## Page Map Checklist

- Core route or screen.
- Target user and job to be done.
- Primary action.
- Required components.
- Input/output data.
- API dependency.
- State matrix.
- Empty and error behavior.
- Permission or role differences.

## Frontend Skeleton Checklist

- Save the frontend plan as `docs/architecture/FRONTEND_PLAN.md`.
- Confirm that the Project Specification Readiness Gate is satisfied before creating frontend files or routes.
- If the implementation changes routes, components, UI states, data dependencies, permissions, or interaction behavior, update `docs/architecture/FRONTEND_PLAN.md` before editing frontend code.
- Confirm product tone, target user, and visual density.
- Choose framework, UI component library, icon library, and chart library.
- Define directory structure, routes, layout boundaries, and component split rules.
- Establish design tokens: color, typography, spacing, radius, shadow, breakpoints.
- Build the smallest stable skeleton first: app shell, navigation, core layout, shared components, one or two representative pages.
- Expand page by page after the skeleton demonstrates conventions.

## First MVP Page Acceptance

For web products, the first MVP page is usually the user entry for the first MVP slice. Do not treat a static page as complete unless it proves the approved product slice from entry to useful outcome.

The first MVP page should define:

- The approved first MVP slice it belongs to.
- Route or screen name and target user.
- Primary user action and success outcome.
- Required components, states, and data/API/mock behavior.
- Empty, loading, error, success, and disabled states when relevant.
- Verification evidence: build/type check plus browser inspection for the key flow and responsive layout.

## Guardrails

- Do not generate all pages horizontally before shared rules exist.
- Do not let each page invent its own layout, CSS scale, data-loading pattern, or error style.
- Do not let code become the first record of a frontend design change; update the source-of-truth plan first.
- Preserve framework conventions and existing project components.
- Verification should include build/type checks and browser inspection for key flows.

## Prompt: Page Inventory

```text
Based on my product flow, create a frontend page inventory. For each page, output the page goal, core components, user actions, state changes, required data, corresponding API, empty state, error state, and permission differences. Do not write code yet.
```

## Prompt: Frontend Skeleton Plan

```text
Do not generate every page at once. Based on docs/project/PROJECT_CHARTER.md and docs/architecture/TECH_STACK.md, create docs/architecture/FRONTEND_PLAN.md covering design style, component library, directory structure, routes, shared layout, design tokens, base components, the first MVP page as the entry for the first MVP slice, and the order for later pages.
```

## Prompt: Frontend Scaffold Readiness

```text
Before creating frontend code, verify that PROJECT_CHARTER.md, TECH_STACK.md, ENGINEERING_BASELINE.md, FRONTEND_PLAN.md, AI_WORKFLOW.md, TOOL_POLICY.md, and AGENTS.md exist. If any required document is missing, list it and ask to create it before scaffolding.
```
