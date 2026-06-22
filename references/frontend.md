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
- Define frontend engineering structure: source tree, routes, layout boundaries, file responsibilities, import boundaries, and component split rules.
- Establish design tokens: color, typography, spacing, radius, shadow, breakpoints.
- Build the smallest stable skeleton first: app shell, navigation, core layout, shared components, one or two representative pages.
- Expand page by page after the skeleton demonstrates conventions.

## Frontend Engineering Structure

Frontend file organization and component decomposition are engineering decisions, not cosmetic cleanup. A frontend implementation is not ready to start until `docs/architecture/FRONTEND_PLAN.md` defines where route files, page orchestration, reusable UI, business components, state, config, messages, icons, assets, and utilities belong.

Use framework conventions first:

- Next.js: keep `app/` responsible for routing, layouts, loading, and error boundaries. Use `src/` when it helps separate application code from root configuration. Colocate route-specific code when useful, or keep shared code outside `app/`; choose one strategy and stay consistent.
- Vite + React: keep `main.tsx` as the boot entry and `App.tsx` as application composition. Put product code under `src/` with explicit folders for app shell, components, config, state, messages, utilities, assets, and styles.
- Workspaces or monorepos: keep deployable apps in `apps/*` and truly shared packages in `packages/*`. Do not create shared packages until more than one app or package needs the code.

For small single-app React tools, this is an acceptable baseline:

```text
apps/web/src/
  app/
    App.tsx
  components/
    <domain>/
  config/
  i18n/
    messages/
  icons/
  stores/
  utils/
  styles.css
  main.tsx
```

For larger products, multi-page apps, or apps with clear business domains, prefer a domain-oriented structure inspired by feature-sliced architecture:

```text
apps/web/src/
  app/
  pages/ or routes/
  widgets/
  features/
  entities/
  shared/
    ui/
    lib/
    config/
    i18n/
    assets/
```

Use only the layers that add clarity. A small app usually needs `app`, route/page folders, and shared UI/config/lib. Add `features`, `entities`, or `widgets` only when the product has distinct user actions, domain objects, or page sections that change independently.

## File Responsibility Rules

- Route files, `page.tsx`, and `App.tsx` compose layouts and screens. They must not become storage for all UI, messages, config, mock data, icons, browser utilities, export logic, or state machines.
- Shared UI components belong in `components/`, `shared/ui/`, or the selected UI library folder. Business-specific components belong under their domain, feature, page, or widget.
- User-visible text belongs in `i18n/messages` or the documented message system, not scattered through business components unless the project explicitly has no multilingual requirement.
- Product constants, design tokens, media presets, workspace settings, and feature flags belong in `config/` or `shared/config/`.
- Reusable state belongs in `stores/` only when it crosses distant components, routes, tabs, or persistence boundaries. Keep local UI state close to the component first.
- Utilities must be capability-scoped, such as `utils/browser.ts`, `utils/export-image.ts`, or `shared/lib/date`. Do not create a growing catch-all `utils.ts`.
- Icons belong in the selected icon library usage layer or in an `icons/` wrapper when the project needs named product icons.

## Component Split Rules

Start from the user flow and design, then break UI into a component hierarchy. Split a component when it has one of these boundaries:

- A distinct user-facing concept, such as toolbar, preview stage, asset card, export panel, settings dialog, or editor rail.
- A distinct interaction state, such as empty, selected, loading, error, disabled, editing, or exporting.
- A distinct data boundary, such as an entity card, list row, filter panel, preview pane, or job message.
- A repeated UI pattern that appears more than twice or is likely to be reused.
- A complex visual unit whose markup, state, or event handlers obscure its parent component.

Do not split only to create tiny wrappers with no semantic purpose. Do not keep a large component intact only because it is used once if it mixes unrelated responsibilities.

## Import Boundary Rules

- Higher-level composition can import lower-level UI, feature, entity, config, and utility modules.
- Lower-level shared UI and utility modules must not import page, route, or feature-specific code.
- Domain modules should expose a small public entry when other modules need them. Avoid deep imports into another module's private files.
- Cross-module imports on the same conceptual layer should be rare and justified by the documented domain relationship.

## Frontend Structure Acceptance

Before calling frontend implementation complete, verify:

- The source tree matches `docs/architecture/FRONTEND_PLAN.md` or the document was updated first.
- Entry and route files stay small and orchestration-focused.
- UI, config, messages, state, icons, assets, and utilities are separated by responsibility.
- Components are split by user/domain/interaction boundaries, not left as a single generated file.
- No catch-all `components`, `utils`, or `config` dump hides unrelated responsibilities.
- Type/build checks and browser inspection cover the key flow and responsive layout.

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
- Do not implement frontend code before the source tree, file responsibilities, and component split rules are documented in `docs/architecture/FRONTEND_PLAN.md`.
- Do not pack UI, config, messages, state, mock data, icons, and utilities into one page or application file.
- Do not let code become the first record of a frontend design change; update the source-of-truth plan first.
- Preserve framework conventions and existing project components.
- Verification should include build/type checks and browser inspection for key flows.

## Prompt: Page Inventory

```text
Based on my product flow, create a frontend page inventory. For each page, output the page goal, core components, user actions, state changes, required data, corresponding API, empty state, error state, and permission differences. Do not write code yet.
```

## Prompt: Frontend Skeleton Plan

```text
Do not generate every page at once. Based on docs/project/PROJECT_CHARTER.md and docs/architecture/TECH_STACK.md, create docs/architecture/FRONTEND_PLAN.md covering design style, component library, frontend source tree, route structure, shared layout, file responsibility rules, component split rules, design tokens, base components, the first MVP page as the entry for the first MVP slice, and the order for later pages.
```

## Prompt: Frontend Scaffold Readiness

```text
Before creating frontend code, verify that PROJECT_CHARTER.md, TECH_STACK.md, ENGINEERING_BASELINE.md, FRONTEND_PLAN.md, AI_WORKFLOW.md, TOOL_POLICY.md, and AGENTS.md exist. Also verify that FRONTEND_PLAN.md defines the frontend source tree, file responsibilities, component split rules, state/config/i18n/utils ownership, and import boundaries. If any required document or frontend engineering contract is missing, list it and ask to create or update it before scaffolding.
```
