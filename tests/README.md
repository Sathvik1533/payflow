# Tests

> **Status:** Not yet implemented.

This directory will contain the test suite for Payflow.

## Planned Structure

```
tests/
├── unit/             # Unit tests for individual components
├── integration/      # Integration tests (API + database)
├── e2e/              # End-to-end tests (optional)
└── conftest.py       # Shared test fixtures and configuration
```

## Testing Strategy

Tests will be added alongside implementation during each engineering loop.

For Phase 1 (Payment Ingestion), planned tests include:

- **Unit tests** — Pydantic schema validation, service logic
- **Integration tests** — FastAPI endpoints against a real test database

No tests exist yet.
