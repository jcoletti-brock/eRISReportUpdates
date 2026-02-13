# React Development Best Practices

You are an expert in Javascript, Node.js, Vite, React, React Router, Redux, HTML, CSS, and MUI.
The following are best practices and guidelines for react 19+ development.

## Development Philosophy

- Use React 19+
- Write clean, maintainable, and scalable code
- Prefer functional and declarative programming patterns over imperative
- Emphasize type safety and static analysis
- Practice component-driven development

## Code Implementation Guidelines

- Begin by asking questions to clarify the requirements if the request is unclear or implementation options are varied.

## Code Style

- ESlint and Prettier are use to enforce code style and formatting.
- Verify that these rules are applied when new code is added or existing code is modified.
- We want to remove any unused imports so that we always pass ESlint checks.

## Naming Conventions

### General Rules

- Use PascalCase for:
  - Components
  - Type definitions
  - Interfaces
- Use camelCase for:
  - Variables
  - Functions
  - Methods
  - Hooks
  - Properties
  - Props
- Use UPPERCASE for:
  - Environment variables
  - Constants
  - Global configurations

### Specific Naming Patterns

- Prefix event handlers with 'handle': handleClick, handleSubmit
- Prefix boolean variables with verbs: isLoading, hasError, canSubmit
- Prefix custom hooks with 'use': useAuth, useForm
- Use complete words over abbreviations except for:
  - err (error)
  - req (request)
  - res (response)
  - props (properties)
  - ref (reference)

## React Best Practices

### Component Architecture

- Define components using the function keyword
- Extract reusable logic into custom hooks
- Implement proper component composition
- Use React.memo() strategically for performance
- Implement proper cleanup in useEffect hooks

### React Performance Optimization

- Use useCallback for memoizing callback functions
- Implement useMemo for expensive computations
- Avoid inline function definitions in JSX
- Implement code splitting using dynamic imports
- Implement proper key props in lists (avoid using index as key)

### UI and Styling

Component Libraries

- Use MUI for consistent, accessible component design https://mui.com/material-ui/all-components/.
- Apply composition patterns to create modular, reusable components.

### Styling Guidelines

- Design with responsive principles for flexibility across devices.
- Ensure color contrast ratios meet accessibility standards for readability.
- User MUIs native token system for consistent theming and styling.

  - Typography: https://mui.com/material-ui/customization/typography/
  - Spacing: https://mui.com/material-ui/customization/spacing/
  - Breakpoints: https://mui.com/material-ui/customization/breakpoints/

## State Management

### Local State

- Use useState for component-level state
- Implement proper state initialization

### Global State

- Use Redux Toolkit for global state
- Use createSlice to define state, reducers, and actions together.
- Avoid using createReducer and createAction unless necessary.
- Normalize state structure to avoid deeply nested data.
- Use selectors to encapsulate state access.
- Avoid large, all-encompassing slices; separate concerns by feature.

## Error Handling and Validation

### Error Boundaries

- Use error boundaries to catch and handle errors in React component trees gracefully.
- Log caught errors to an external service (e.g., Sentry) for tracking and debugging.
- Design user-friendly fallback UIs to display when errors occur, keeping users informed without breaking the app.

## Internationalization (i18n)

- Use next-i18next for translations
- Implement proper locale detection
- Use proper number and date formatting
- Implement proper RTL support
- Use proper currency formatting

## Documentation

- Use JSDoc for documentation
- Document all public functions, classes, methods, and interfaces
- Add examples when appropriate (in documentation, not implementation)
- Use complete sentences with proper punctuation
- Keep descriptions clear and concise
- Use proper markdown formatting
- Use proper code blocks
- Use proper links
- Use proper headings
- Use proper lists
