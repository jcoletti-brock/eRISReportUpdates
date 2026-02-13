---
applyTo: '**'
---
# Security Design Patterns

The following rules help define how we should think about security in our code:

## Secrets

- Never hardcode secrets – Fetch them from environment variables or a secure configuration service.

## Use TLS

- Use HTTPS only for all API calls.
- Implement proper CORS policies.
