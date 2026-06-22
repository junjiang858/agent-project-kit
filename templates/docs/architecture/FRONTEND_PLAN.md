# FRONTEND_PLAN

## Product Tone

- Target user:
- Visual density:
- Accessibility expectations:

## Page Map

| Route or screen | Goal | Primary action | Data needed | States |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

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
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Frontend Architecture

- Framework conventions:
- Route structure:
- Shared layout:
- Data fetching pattern:
- Form and validation pattern:
- Error and empty-state pattern:

## Frontend Source Tree

Document the approved frontend file structure before implementation. Mark which folders are framework conventions and which are project conventions.

```text
apps/web/src/
```

## File Boundary Contract

| Concern | Approved location | Notes |
| --- | --- | --- |
| App boot entry |  |  |
| Route/page files |  |  |
| App shell and providers |  |  |
| Shared UI primitives |  |  |
| Business/domain components |  |  |
| Feature or workflow components |  |  |
| Data/API clients or mocks |  |  |
| Local or global stores |  |  |
| Config, constants, tokens |  |  |
| i18n messages |  |  |
| Icons |  |  |
| Assets/media |  |  |
| Utilities and browser adapters |  |  |
| Global styles |  |  |

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
- Icon library:
- Color tokens:
- Typography:
- Spacing:
- Radius:
- Breakpoints:

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
- [ ] Responsive layout check
- [ ] Source tree matches this document
- [ ] Entry and route files are orchestration-focused
- [ ] UI, config, messages, state, icons, assets, and utilities have separate approved locations
- [ ] Components are split by documented user/domain/interaction boundaries
