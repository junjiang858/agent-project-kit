# TECH_STACK

## Decision Status

- Project charter or equivalent facts confirmed:
- User agreed to enter technology selection:
- Capability library scan reviewed by user:
- User confirmed this stack:
- User approved writing this document:
- Last reviewed:

## Selection Context

- Product form:
- Product lifecycle:
- Target users or expected scale:
- Team capability:
- Launch pressure:
- Budget, hosting, compliance, or operational constraints:

## Architecture Track

- Track: Single Web App / Web + API / Multi-App Platform
- Repository shape:
- Repository shape rationale:
- Product lifecycle:

## Default Route

| Layer | Choice | Reason |
| --- | --- | --- |
| Package manager |  |  |
| Frontend |  |  |
| Backend |  |  |
| Database |  |  |
| Migrations |  |  |
| UI |  |  |
| Icons |  |  |
| Deployment |  |  |
| Testing |  |  |

## Capability Library Scan

### Required Technical Capabilities

| Capability | Requirement source | Needed in MVP? |
| --- | --- | --- |
|  |  | Yes / Later / No |

### Third-Party Library Decisions

| Capability | Library name | Direct link | Ecosystem | Open-source or inspectable | Maintenance evidence | Why include/defer/reject | Risk or lock-in note | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | Included / Deferred / Rejected |

## Production Compatibility

- Choices intended to survive launch:
- Choices that are acceptable only for prototype or local development:
- What must not be replaced later without explicit approval:
- UI/icon/repository choices that may be replaced with approval:

## Migration Cost

| Choice | Replacement cost | Notes |
| --- | --- | --- |
|  |  |  |

## Rejected Alternatives

| Alternative | Why rejected |
| --- | --- |
|  |  |

## Forbidden Drift

- Do not introduce a new framework, database, UI kit, icon library, deployment platform, package manager, repository shape, or state library without documenting the reason and receiving approval.
- Do not create `apps/*` or `packages/*` unless the repository shape above names a real app/package boundary.
- Do not change UI or icon libraries only because a default stack suggests them; design-system evidence and user approval are required.

## Re-Evaluation Rules

Revisit this file when:

- Product shape changes.
- Team capability changes.
- Hosting, cost, compliance, or performance constraints change.
- A selected dependency becomes unsafe or unmaintained.
- A design source, brand system, accessibility need, or implementation boundary shows that the approved UI/icon library or repository shape no longer fits.
