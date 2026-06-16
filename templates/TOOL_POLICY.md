# TOOL_POLICY

## Default Open

- Read/search/edit project files.
- Run local tests, lint, type checks, builds, and dev servers.
- Inspect Git status and diff.
- Use local browser verification.
- Look up official docs when current facts matter.

## Project Open

| Tool | Purpose | Allowed | Forbidden | Evidence |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Must Confirm First

- Production database writes, migrations, deletes, or exports.
- Real secrets, tokens, payment credentials, private user data.
- Production deploy, rollback, DNS, billing, cloud infrastructure changes.
- Destructive Git or filesystem operations.
- Public publishing or external account actions.

## Evidence Required

- State which tools were used.
- Provide tests, diffs, logs, screenshots, API responses, or security scan output as applicable.
