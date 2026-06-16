# AGENTS

## Project Goal

- 

## Source of Truth

1. User instruction
2. `PROJECT_CHARTER.md`
3. `TECH_STACK.md`
4. `TOOL_POLICY.md`
5. Existing code conventions

## Working Rules

- Clarify scope before implementation.
- Preserve the documented tech stack.
- Keep changes small and reviewable.
- Use existing patterns before adding abstractions.
- Never put secrets in code or Git history.

## Completion Definition

- [ ] Relevant tests or checks pass.
- [ ] Build passes when applicable.
- [ ] Browser/API/security evidence is provided when applicable.
- [ ] Docs are updated when decisions change.
- [ ] Git diff is reviewed before commit.

## Forbidden Actions

- Production changes without confirmation.
- Destructive Git or filesystem operations without confirmation.
- Broad rewrites without a plan.
- New major dependencies without documented approval.
