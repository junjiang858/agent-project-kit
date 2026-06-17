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
- Confirm product tone, target user, and visual density.
- Choose framework, UI component library, icon library, and chart library.
- Define directory structure, routes, layout boundaries, and component split rules.
- Establish design tokens: color, typography, spacing, radius, shadow, breakpoints.
- Build the smallest stable skeleton first: app shell, navigation, core layout, shared components, one or two representative pages.
- Expand page by page after the skeleton demonstrates conventions.

## Guardrails

- Do not generate all pages horizontally before shared rules exist.
- Do not let each page invent its own layout, CSS scale, data-loading pattern, or error style.
- Preserve framework conventions and existing project components.
- Verification should include build/type checks and browser inspection for key flows.

## Prompt: Page Inventory

```text
Based on my product flow, create a frontend page inventory. For each page, output the page goal, core components, user actions, state changes, required data, corresponding API, empty state, error state, and permission differences. Do not write code yet.
```

## Prompt: Frontend Skeleton Plan

```text
Do not generate every page at once. Based on docs/project/PROJECT_CHARTER.md and docs/architecture/TECH_STACK.md, create docs/architecture/FRONTEND_PLAN.md covering design style, component library, directory structure, routes, shared layout, design tokens, base components, and the order for the first pages.
```
