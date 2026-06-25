# FRONTEND_PLAN

## Product Tone

- Target user:
- Visual density:
- Accessibility expectations:

## Design Read

- Surface type:
- Audience:
- Product tone:
- Reference signals:
- Existing brand assets:
- Quiet constraints:
- One-sentence direction:

## Design Dials

| Dial             | Value | Rationale |
| ---------------- | ----- | --------- |
| Design variance  |       |           |
| Motion intensity |       |           |
| Visual density   |       |           |

Rules:

- Do not apply landing-page taste rules blindly to dashboards, admin panels, data tables, or multi-step product UI.
- For operational UI, prioritize scannable density, efficient controls, clear state, restrained motion, and mature design-system patterns.
- For marketing or brand surfaces, document the visual asset strategy and anti-slop checks.

## Product MVP UI Quality Gate

- MVP UI quality standard:
- First user loop:
- Design system foundation:
- Layout contract:
- Interaction completeness:
- Responsive requirement:
- Accessibility requirement:
- Anti-slop constraints:
- Browser UI quality verification:

## Page Map

| Route or screen | Goal | Primary action | Data needed | States |
| --------------- | ---- | -------------- | ----------- | ------ |
|                 |      |                |             |        |

## First MVP Page

- Related first MVP slice:
- Route or screen:
- Target user:
- Primary action:
- Success outcome:
- Required states:
- Data/API/mock behavior:
- Browser verification evidence:

## Component Map

| Component | Purpose | Owner layer or folder | Reuse scope | State owned |
| --------- | ------- | --------------------- | ----------- | ----------- |
|           |         |                       |             |             |

## Frontend Architecture

- Framework conventions:
- Route structure:
- Shared layout:
- Data fetching pattern:
- Form and validation pattern:
- Error and empty-state pattern:
- Responsive layout pattern:
- Accessibility pattern:

## Frontend Source Tree

Document the approved frontend file structure before implementation. Mark which folders are framework conventions and which are project conventions.

```text
<approved frontend root, such as src/ or apps/web/src/>
```

## File Boundary Contract

| Concern                        | Approved location | Notes |
| ------------------------------ | ----------------- | ----- |
| App boot entry                 |                   |       |
| Route/page files               |                   |       |
| App shell and providers        |                   |       |
| Shared UI primitives           |                   |       |
| Business/domain components     |                   |       |
| Feature or workflow components |                   |       |
| Data/API clients or mocks      |                   |       |
| Local or global stores         |                   |       |
| Config, constants, tokens      |                   |       |
| i18n messages                  |                   |       |
| Icons                          |                   |       |
| Assets/media                   |                   |       |
| Utilities and browser adapters |                   |       |
| Global styles                  |                   |       |

Rules:

- `App.tsx`, `page.tsx`, and route files compose screens; they must not hold unrelated UI, config, messages, state stores, icons, mock data, and utilities.
- A catch-all `utils.ts`, `config.ts`, or flat `components/` dump is not allowed once responsibilities are distinct.
- Any new top-level frontend folder must be added here before implementation.

## Component Split Rules

- Split by user-facing concept:
- Split by interaction state:
- Split by data or domain boundary:
- Split repeated patterns after:
- Keep local-only pieces inline when:
- Extract custom hooks when:
- Promote state to a store when:

## Import Boundaries

- Route/page/app composition may import:
- Shared UI may import:
- Feature/domain modules may import:
- Forbidden imports:
- Public entry files required for:

## Design System

- UI library:
- UI library rationale:
- Icon library:
- Icon library rationale:
- Design-source alignment:
- Replacement rule:
- Theme strategy:
- Semantic color tokens:
- Typography scale:
- Spacing scale:
- Radius scale:
- Border and shadow:
- Breakpoints:
- Z-index scale:
- Motion tokens:
- Component baseline:
- Customization rule:

## State And Interaction Contract

| State or interaction | Pattern | Components affected | Notes |
| -------------------- | ------- | ------------------- | ----- |
| Loading              |         |                     |       |
| Empty                |         |                     |       |
| Error                |         |                     |       |
| Success              |         |                     |       |
| Disabled             |         |                     |       |
| Validating or saving |         |                     |       |
| Selected or editing  |         |                     |       |
| Destructive action   |         |                     |       |
| Focus and keyboard   |         |                     |       |
| Hover, active, touch |         |                     |       |

Rules:

- Forms use visible labels, optional helper text, error text below fields, and accessible focus rings.
- Loading states use skeletons or layout-matched placeholders rather than generic spinners when possible.
- Empty states identify the next useful action.
- Error states are inline or contextual; toasts are only for transient feedback.

## Anti-Slop Preflight

- [ ] No generic AI-purple gradient default, random glow, or decorative effect replacing information architecture
- [ ] No fake product previews made from decorative div rectangles
- [ ] No gratuitous glassmorphism, bento, marquee, or motion in dense operational UI
- [ ] No ungrounded metrics, fake-precise numbers, or generic placeholder names
- [ ] No placeholder-as-label forms
- [ ] No low-contrast ghost buttons or invisible focus states
- [ ] No text overflow, clipped labels, button wrapping on desktop, or incoherent overlap
- [ ] No card-in-card layout unless the nested frame represents a real tool, modal, or repeated item
- [ ] UI library components are customized through tokens or documented component variants, not scattered one-off styles
- [ ] UI and icon libraries match the approved design source or have a documented, approved reason to differ

## Implementation Order

1. First MVP page for the first MVP slice:
2. 
3. 

## Change Rule

- Update this document before implementing changes to routes, components, UI states, data dependencies, permissions, or interaction behavior.
- Update the Frontend Source Tree, File Boundary Contract, Component Split Rules, and Import Boundaries before moving frontend code across directories or adding new frontend layers.

## Verification

- [ ] Type/build check
- [ ] Browser verification for key flow
- [ ] Desktop responsive layout check
- [ ] Mobile responsive layout check
- [ ] Source tree matches this document
- [ ] Entry and route files are orchestration-focused
- [ ] UI, config, messages, state, icons, assets, and utilities have separate approved locations
- [ ] Components are split by documented user/domain/interaction boundaries
- [ ] Design Read, Design Dials, and Product MVP UI Quality Gate are followed
- [ ] Required loading, empty, error, success, disabled, and saving states render
- [ ] Text fits controls, cards, table cells, badges, and empty/error states
- [ ] Contrast, focus rings, keyboard navigation, and touch targets are usable
