---
applyTo: '**'
---
## Code Quality and Design

The following rules help define how we should think about code quality and design in our code:

- Low Cyclomatic Complexity – Keep logic simple; avoid nested conditionals and complex branching.
- Minimized Cognitive Complexity – Code should be easy to read and understand.
- No Code Duplication – Abstract and reuse logic in clean, testable functions or hooks.
- High Cohesion & Loose Coupling – Each component should do one thing and depend minimally on others.
- Clear Naming Conventions – Descriptive, consistent, and self-explanatory identifiers.
- Single Responsibility Principle (SRP) – Each component/module should focus on a single purpose.

## Anchor comments

Add specially formatted comments throughout the codebase, where appropriate, for yourself as inline knowledge that can be easily `grep`ped for.

### Guidelines:

- Use `AIDEV-NOTE:`, `AIDEV-TODO:`, or `AIDEV-QUESTION:` (all-caps prefix) for comments aimed at AI and developers.
- Keep them concise (≤ 120 chars).
- **Important:** Before scanning files, always first try to **locate existing anchors** `AIDEV-*` in relevant subdirectories.
- **Update relevant anchors** when modifying associated code.
- **Do not remove `AIDEV-NOTE`s** without explicit human instruction.
