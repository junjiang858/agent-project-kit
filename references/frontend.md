# Frontend

Use this reference when planning pages, components, UI states, frontend architecture, design tokens, or a first frontend skeleton.

## Contents

- Frontend Understanding
- Page Map Checklist
- Frontend Skeleton Checklist
- Product MVP UI Quality Gate
- Frontend Engineering Structure
- File Responsibility Rules
- Component Split Rules
- Import Boundary Rules
- Frontend Structure Acceptance
- First MVP Page Acceptance
- Guardrails
- Prompts

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
- Run the Product MVP UI Quality Gate before implementation.
- Confirm product tone, target user, and visual density.
- Choose framework, UI component library, icon library, and chart library.
- Define frontend engineering structure: source tree, routes, layout boundaries, file responsibilities, import boundaries, and component split rules.
- Establish design tokens: color, typography, spacing, radius, shadow, breakpoints.
- Build the smallest stable skeleton first: app shell, navigation, core layout, shared components, one or two representative pages.
- Expand page by page after the skeleton demonstrates conventions.

## Product MVP UI Quality Gate

MVP scope may be small, but UI/UX/design system quality is not optional. A first MVP page should prove a useful product loop with a coherent visual system, clear interaction feedback, and responsive usability.

### Design Read

Before writing the frontend plan or frontend code, infer the design direction from the product facts:

- Surface type: marketing page, SaaS app, product workspace, admin panel, dashboard, data table, multi-step flow, internal tool, content surface, mobile app, mini program, or hardware UI.
- Audience: buyer, operator, admin, creator, reader, developer, field worker, or consumer.
- Product tone: utilitarian, calm B2B, trust-first, playful, premium, technical, editorial, content-heavy, or operational.
- Reference signals: linked products, screenshots, existing brand assets, design systems, or explicit style words.
- Quiet constraints: accessibility, regulated data, public-sector trust, high-frequency workflows, mobile-first use, or low bandwidth.

State the design read in one sentence. If two directions would change layout, density, or component choice materially, ask one clarifying question. Otherwise proceed.

### Design Dials

Document three dials in `FRONTEND_PLAN.md`; use them to make layout decisions explicit:

| Dial             | Meaning                                             | Product UI default                                                    |
| ---------------- | --------------------------------------------------- | --------------------------------------------------------------------- |
| Design variance  | How conventional or expressive the layout is        | 3-6 for tools and dashboards, 6-8 for brand or marketing surfaces     |
| Motion intensity | How much movement supports feedback or storytelling | 1-3 for operational UI, 3-5 for SaaS pages, higher only with a reason |
| Visual density   | How much information appears per viewport           | 6-9 for dashboards/admin, 4-7 for SaaS apps, 2-4 for marketing        |

For dashboards, admin panels, data tables, and multi-step product UI, do not apply landing-page taste rules blindly. Prefer scannable density, predictable navigation, efficient controls, clear tables/lists, and restrained motion. In short: do not apply landing-page taste rules blindly to dashboards, admin panels, data tables, or multi-step product UI. For marketing or portfolio surfaces, apply stronger anti-slop and visual asset rules.

### Design System Contract

`FRONTEND_PLAN.md` must define the system before code:

- UI library and how it will be customized, not left in default visual state.
- Icon library, one icon family, and consistent stroke/weight rules.
- Semantic color tokens for background, surface, border, muted text, primary text, accent, success, warning, danger, info, focus, and disabled.
- Typography scale for app shell, page title, section heading, body, metadata, labels, table text, and numeric text.
- Spacing, radius, border, shadow, z-index, breakpoint, and motion tokens.
- Theme strategy: light, dark, or system; include contrast expectations and when dual-mode is required.
- Component baseline: buttons, inputs, selects, tabs, toolbar, filters, list/table/card, dialog, toast, empty state, error state, loading skeleton, and pagination when relevant.

### Design-system dependency rule

The selected UI and icon libraries are approved project decisions, not fixed skill defaults. When a Figma, Stitch, screenshot, brand system, existing codebase, platform convention, or anti-slop requirement points to a different component or icon language, evaluate the replacement before implementation. Document why the chosen UI library and icon library fit the design, whether the library is open-source or inspectable, how it affects bundle size and maintenance, and what local wrapper or adapter will keep future replacement cheap.

Use the approved UI library for common controls. Do not hand-write repeated base buttons, inputs, dialogs, cards, or tabs inside business pages. If a component appears more than twice or has a shared interaction rule, extract it into the documented shared or domain component location.

Treat common choices such as shadcn/ui and lucide as candidates, not mandatory defaults.

Do not replace UI or icon libraries silently during implementation. Use this sequence:

1. Identify the design-system mismatch or implementation constraint.
2. Propose the replacement with maintenance, license, accessibility, tree-shaking, and migration notes.
3. Update `docs/architecture/TECH_STACK.md` and this `FRONTEND_PLAN.md`.
4. Get user approval.
5. Install dependencies and implement through documented component or icon adapters.

### State And Interaction Contract

Every key screen or component should document relevant states:

- Loading: skeletons should match the final layout shape.
- Empty: explain the next useful action.
- Error: inline for forms, contextual for panels, toast only for transient failures.
- Success: confirm the completed action without blocking the workflow.
- Disabled and validating: controls show why action is unavailable when useful.
- Selected, editing, saving, optimistic, permission-denied, and destructive-action states when relevant.
- Hover, focus, active, keyboard navigation, and touch target behavior.
- Undo, confirmation dialog, or clear irreversible-action copy for destructive flows.

Forms must use visible labels above inputs, helper text when useful, error text below inputs, readable placeholders, and accessible focus rings. Placeholder-as-label is not acceptable.

### Anti-Slop Guardrails

Avoid common AI-generated UI tells unless the product brief explicitly calls for them:

- No generic AI-purple gradient default, random glow, or decorative visual effect as a substitute for information architecture.
- No fake product preview built from decorative div rectangles. Use a real screenshot, real component preview, generated asset, or skip the preview.
- No repeated three-equal-card layout as the default page structure.
- No gratuitous glassmorphism, bento, marquee, or motion in dense operational UI.
- No ungrounded metrics, fake-precise numbers, generic names, or startup-slop brand labels.
- No placeholder-only forms, no invisible focus states, no low-contrast ghost buttons.
- No text overflow, clipped labels, button text wrapping on desktop, or incoherent overlap.
- No card-in-card layouts unless the nested frame represents a real tool, modal, or repeated item.

For marketing or brand pages, use real visual assets or clearly documented placeholders. For tools and dashboards, prioritize real working controls, dense but organized information, and reusable product components over decorative sections.

### Browser UI Quality Verification

Before marking frontend work complete, verify:

- Type/build check passes.
- Browser inspection covers the approved key flow.
- Desktop and mobile viewports have no overlap, overflow, clipped text, unstable layout jumps, or inaccessible controls.
- Navigation and toolbar controls remain usable at expected breakpoints.
- Text fits buttons, cards, table cells, badges, and empty/error states.
- Contrast, focus rings, keyboard navigation, and touch targets are usable.
- Loading, empty, error, success, disabled, and saving states render.
- The implementation matches the documented design system, component strategy, and responsive rules.

## Frontend Engineering Structure

Frontend file organization and component decomposition are engineering decisions, not cosmetic cleanup. A frontend implementation is not ready to start until `docs/architecture/FRONTEND_PLAN.md` defines where route files, page orchestration, reusable UI, business components, state, config, messages, icons, assets, and utilities belong.

Use framework conventions first:

- Next.js: keep `app/` responsible for routing, layouts, loading, and error boundaries. Use `src/` when it helps separate application code from root configuration. Colocate route-specific code when useful, or keep shared code outside `app/`; choose one strategy and stay consistent.
- Client-rendered SPA frameworks: keep the framework boot entry and root composition file clear, such as React `main.tsx`/`App.tsx`, Vue `main.ts`/`App.vue`, or Svelte `main.ts`/`App.svelte`. Put product code under `src/` with explicit folders for app shell, components, config, state, messages, utilities, assets, and styles.
- Workspaces or monorepos: keep deployable apps in `apps/*` and truly shared packages in `packages/*`. Do not create shared packages until more than one app or a real non-UI package boundary needs the code.

For small single-package frontend apps, this is an acceptable baseline:

```text
src/
  app/
    App.<framework-extension>
  components/
    <domain>/
  config/
  i18n/
    messages/
  icons/
  stores/
  utils/
  styles.css
  main.<framework-extension>
```

For larger products, multi-page apps, or apps with clear business domains, prefer a domain-oriented structure inspired by feature-sliced architecture:

```text
src/ or apps/web/src/
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
- Icons belong in the selected icon library usage layer or in an `icons/` wrapper when the project needs named product icons, design-system state variants, or a replacement-safe adapter.

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
- UI follows the documented Design Read, Design Dials, design system tokens, and interaction contract.
- Type/build checks and browser inspection cover the key flow and responsive layout.

## First MVP Page Acceptance

For web products, the first MVP page is usually the user entry for the first MVP slice. Do not treat a static page as complete unless it proves the approved product slice from entry to useful outcome.

The first MVP page should define:

- The approved first MVP slice it belongs to.
- Route or screen name and target user.
- Primary user action and success outcome.
- Required components, states, and data/API/mock behavior.
- Empty, loading, error, success, and disabled states when relevant.
- Design system, interaction, responsive, accessibility, and anti-slop acceptance notes.
- Verification evidence: build/type check plus browser inspection for the key flow and responsive layout.

## Guardrails

- Do not generate all pages horizontally before shared rules exist.
- Do not let each page invent its own layout, CSS scale, data-loading pattern, or error style.
- Do not implement frontend code before the source tree, file responsibilities, and component split rules are documented in `docs/architecture/FRONTEND_PLAN.md`.
- Do not implement frontend code before the Product MVP UI Quality Gate is documented in `docs/architecture/FRONTEND_PLAN.md`.
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
Do not generate every page at once. Based on docs/project/PROJECT_CHARTER.md and docs/architecture/TECH_STACK.md, create docs/architecture/FRONTEND_PLAN.md covering the Design Read, Design Dials, Product MVP UI Quality Gate, design system, component library, frontend source tree, route structure, shared layout, file responsibility rules, component split rules, state and interaction contract, responsive rules, accessibility expectations, anti-slop guardrails, base components, the first MVP page as the entry for the first MVP slice, and the order for later pages.
```

## Prompt: Frontend Scaffold Readiness

```text
Before creating frontend code, verify that PROJECT_CHARTER.md, TECH_STACK.md, ENGINEERING_BASELINE.md, FRONTEND_PLAN.md, AI_WORKFLOW.md, TOOL_POLICY.md, and AGENTS.md exist. Also verify that FRONTEND_PLAN.md defines the frontend source tree, file responsibilities, component split rules, state/config/i18n/utils ownership, import boundaries, Design Read, Design Dials, Product MVP UI Quality Gate, design system tokens, state and interaction contract, responsive/accessibility rules, anti-slop guardrails, and browser UI quality verification. If any required document, frontend engineering contract, or UI quality gate is missing, list it and ask to create or update it before scaffolding.
```
