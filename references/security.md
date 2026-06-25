# Security

Use this reference for backend security acceptance, configuration safety, logging safety, dependency safety, database safety, and evidence-based verification.

## Contents

- Backend Security Boundary
- Bottom-Layer Security Matrix
- Security Checklist
- Risk Table Format
- Prompts

## Backend Security Boundary

Feature success only proves the normal path works. Security acceptance proves abnormal requests are rejected.

Check:

- Inputs from frontend are validated again on the backend.
- Login state, role permissions, and data ownership are enforced server-side.
- Password policy, hash storage, and failed-login limits exist where relevant.
- Queries and commands use parameterized mechanisms; no string concatenation execution.
- AI identifies risk, rule, code location, verification method, and remediation.

## Bottom-Layer Security Matrix

| Dimension | Common risk | Required evidence |
| --- | --- | --- |
| Config | Secrets, tokens, admin passwords hard-coded | config source list, environment variable read locations, secret scan result |
| Logs | Passwords, phone numbers, tokens, raw request bodies in logs | log field allowlist, masking rule, sample log |
| Dependencies | Known vulnerabilities in framework or libraries | dependency version list, vulnerability scan result, upgrade plan |
| Database | Unbounded read/update/delete, missing transaction, accidental delete | permission boundary, transaction strategy, delete and rollback policy |
| Acceptance | Verbal "handled" without proof | role-switched normal and abnormal request evidence |

## Security Checklist

- List all critical inputs from frontend and confirm backend validation.
- Check authentication, authorization, role gates, and data ownership.
- Confirm secrets only come from environment variables or deployment secret management.
- Ensure real secrets never enter Git.
- Inspect logs for passwords, tokens, phone numbers, emails, IDs, and full request bodies.
- Review dependency versions and security advisories for framework, ORM, auth, upload, and parser libraries.
- Check database permission limits, transaction use, soft delete or recovery strategy.
- Test the same critical APIs as unauthenticated user, normal user, and admin.
- Require risk table, affected files, fix notes, and verification evidence.

## Risk Table Format

| Risk | File or config location | Current behavior | Impact | Fix | Verification | Priority |
| --- | --- | --- | --- | --- | --- | --- |

## Prompt: Backend Security Acceptance

```text
Perform basic backend security acceptance. Output a backend security boundary table covering interface input, login state, permission design, password rules, data ownership, injection risk, and dead-code risk. For each item, include risk, rule, code location, verification method, and remediation suggestion.
```

## Prompt: Bottom-Layer Security Acceptance

```text
Perform bottom-layer security acceptance for the current backend project. Focus on configuration files, logs, dependencies, and database operations. Output a table with risk item, file or config location, current implementation, leakage/vulnerability/privilege/delete risk, recommended fix, verification method, and fix priority. Do not answer "handled" without evidence.
```
