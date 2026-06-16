# Tool Policy

Use this reference when deciding which tools, MCPs, CLIs, browsers, databases, deployment platforms, cloud services, or external systems AI may use.

## Principle

Give AI clear tool boundaries, not unlimited power. Split permissions into:

- Default open: tools required for normal engineering loops.
- Project open: tools needed for this project after context is documented.
- High-risk confirmation: tools or actions that can expose secrets, mutate production, spend money, publish, delete, or affect users.

## Default Open

Usually allow:

- Read and search local code.
- Edit project files.
- Run tests, type checks, lint, builds, and local dev servers.
- Inspect Git status and diff.
- Use browser verification for local apps.
- Search official documentation when current information matters.

## Project Open

Allow after documenting purpose and scope:

- Database development branch or local database.
- Supabase/Vercel/GitHub/Slack/Figma or other project integrations.
- Package manager installs.
- API clients against staging or mock systems.
- Deployment preview environments.

## High-Risk Confirmation

Require explicit approval before:

- Production database writes, migrations, deletes, or bulk exports.
- Handling real secrets, tokens, payment keys, or private user data.
- Production deployment, rollback, DNS, billing, cloud resources, payment settings.
- Destructive filesystem or Git operations.
- Publishing public repositories or packages.
- Sending external messages from user-owned accounts.

## TOOL_POLICY.md Template

```markdown
# TOOL_POLICY

## Default Open

- Read/search/edit project files.
- Run local tests, lint, type checks, builds, and dev servers.
- Inspect Git status and diff.
- Use local browser verification.
- Look up official docs when current facts matter.

## Project Open

- [List project-specific tools, accounts, databases, MCPs, staging services.]
- For each: purpose, allowed operations, forbidden operations, evidence expected.

## Must Confirm First

- Production database writes, migrations, deletes, exports.
- Real secrets, tokens, payment credentials, private user data.
- Production deploy, rollback, DNS, billing, cloud infrastructure changes.
- Destructive Git/filesystem operations.
- Public publishing or external account actions.

## Evidence Required

- State which tools were used.
- Provide tests, diffs, logs, screenshots, API responses, or security scan output as applicable.
```

## Prompt: Generate Tool Policy

```text
Based on this project's tech stack, deployment method, database, and collaboration tools, generate an AI tool permission strategy. Divide it into default open, project open, and high-risk confirmation. For each tool, explain purpose, allowed operations, forbidden operations, verification method, and scenarios requiring human confirmation. Finish with a version that can be saved as TOOL_POLICY.md.
```
