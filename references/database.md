# Database

Use this reference when turning business flow into tables, fields, relations, constraints, indexes, and database documentation.

## Principles

- Database design follows product flow and business objects; it should not be guessed from isolated screens.
- A database is not a spreadsheet. It stores, constrains, relates, and protects long-lived business data.
- Bad schema design will distort backend APIs, permissions, queries, and future migrations.
- Every field should have a business reason.

## Design Flow

1. Extract core objects from user journeys and page flows.
2. Identify relationships: one-to-one, one-to-many, many-to-many.
3. Decide data ownership and lifecycle.
4. Define tables, primary keys, foreign keys, required fields, default values, status enums, and timestamps.
5. Add indexes for high-frequency queries, not as decoration.
6. Add security fields and rules: password hash, role, owner/user id, soft delete, audit fields, sensitive data masking.
7. Save the design as `docs/architecture/DATABASE_DESIGN.md` and version it in Git before backend implementation.
8. Do not create schemas, migrations, seeds, or ORM files until the database design document is approved, unless the user explicitly confirms a bootstrap-only exception with no persistent product model.
9. If a later task requires a new or changed table, field, relation, index, enum, seed, schema, migration, ownership rule, retention rule, or rollback plan, update `docs/architecture/DATABASE_DESIGN.md` before writing the database code.

## Table Checklist

- Table purpose.
- Primary key.
- Foreign keys and relationship explanation.
- Required fields and nullable fields.
- State fields and valid transitions.
- Timestamps: created, updated, deleted when needed.
- Indexes and query reason.
- Permission boundary: owner, role, tenant, organization, visibility.
- Sensitive fields and storage rule.
- Migration and rollback note.

## Risk Checks

- Ambiguous object ownership.
- Missing status enum where workflow exists.
- Storing passwords or secrets directly.
- No owner or tenant boundary for user data.
- Many-to-many modeled as comma-separated strings.
- Indexes missing for frequent lookup, or too many indexes without query reason.
- Deleting business data physically when recovery or audit is needed.
- Creating migrations first and leaving `docs/architecture/DATABASE_DESIGN.md` stale.

## Prompt: Initial Database Design

```text
Based on my user flow and business objects, draft the database design. Output core tables, fields, field types, primary keys, foreign keys, indexes, status fields, timestamps, data relationships, design reasons, security notes, and possible risks.
```

## Prompt: Database Design Document

```text
Based on my frontend page flow and backend business rules, generate docs/architecture/DATABASE_DESIGN.md. Include core objects, relationships, table structures, field explanations, types, constraints, indexes, status enums, permission-related fields, security concerns, and migration suggestions.
```
