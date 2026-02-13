# Secure React Architecture Guidelines (v19+)

This document defines the principles for implementing **secure, idiomatic, and maintainable** React applications using React v19.0.0+. Designed for use by human developers and co-pilot agents alike.

## 1. Component Design Principles

### Single Responsibility Principle (SRP)

- Components should do one thing and do it well.
- Split large components into focused subcomponents or hooks.

### High Cohesion, Loose Coupling

- Group related logic in modules and avoid tight interdependencies.
- Prefer collocating styles, types, and tests with components.

### Low Complexity

- Minimize **cyclomatic** and **cognitive** complexity.
- Prefer small, declarative functions and hooks.

### Clear Naming

- Use explicit and descriptive names for variables, components, and hooks.

### Accessibility (a11y)

- Comply with WCAG 2.1+:
  - Use semantic HTML.
  - Provide alt text, ARIA roles, keyboard navigation.
  - Validate contrast ratios.

## 2. Data Handling and Output Safety

### Never Trust User Input

- Treat **all API data, form inputs, and props** as untrusted.

### Avoid `dangerouslySetInnerHTML`

- If unavoidable, sanitize content using a trusted library like `DOMPurify`.

### JSX Auto-Escaping

- Always output user content via JSX curly braces:

```jsx
<p>{userInput}</p> // Safe
```

### URL Sanitization

Use this allowlist validator for all external links:

```jsp
const validateAndSanitizeUrl = (url: string): string => {
  try {
    const { protocol, href } = new URL(url);
    const allowed = ["https:", "mailto:"];
    return;
    allowed.includes(protocol) ? href : "#";
  } catch {
    return "#";
  }
};
```

Usage:

```jsp
<a
  href="{validateAndSanitizeUrl(userUrl)}"
  target="_blank"
  rel="noopener noreferrer"
>
  Visit
</a>
```

### Prop Safety

- Avoid injecting unvalidated props into executable attributes (onClick, style, etc.).

- Validate with PropTypes or TypeScript.

## 3. DOM and Styling Safety

### Avoid Direct DOM Access

- Never mutate DOM manually (innerHTML, setAttribute, etc.).

- Use React refs only for non-render operations (e.g., focus, measurements).

### Escape Dynamic Styles

Use CSS.escape() for all untrusted style values:

```jsx
const safeClass = CSS.escape(userInputClassName);
```

## 4. Authentication and State Security

### Enforce Authorization Server-Side

UI can hide components based on roles, but true access control must happen on the server.

### Don’t Store Secrets Client-Side

Never expose API keys, tokens, or secrets in frontend code or environment variables.

### Secure State Management

Do not store sensitive data (e.g., tokens, passwords, PII) in:

- Redux
- React context
- localStorage or sessionStorage

## 5. Error Handling and Resilience

### Use Error Boundaries

Catch runtime errors gracefully:

```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false };

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  render() {
    return this.state.hasError ? <ErrorUI /> : this.props.children;
  }
}
```

### Avoid Leaking Internal Errors

- Do not render raw error messages or stack traces in production.
- Log to a trusted observability platform (e.g., Sentry).

## 6. Safe Third-Party and Dependency Practices

### Use Only Safe, Maintained Libraries

Avoid libraries that:

- Inject HTML
- Perform unsafe DOM manipulation
- Are unmaintained or have known vulnerabilities

### Load External Resources Safely

- Use trusted CDNs
- Apply Subresource Integrity (SRI) for `<script>` or `<link>` tags.

## 7. Application Hardening

### React Strict Mode

Wrap your app in `<React.StrictMode>` to detect unsafe lifecycle patterns.

### Content Security Policy (CSP)

Set a secure CSP header:

```csharp
Content-Security-Policy:
  default-src 'self';
  frame-ancestors 'none';
  script-src 'self' https://trusted.cdn.com;
```

Also use:

```yaml
X-Frame-Options: DENY
```

### CSRF Protection

- Use CSRF tokens for all mutating operations (POST, PUT, DELETE).

## Summary Checklist

- Validate and sanitize all user inputs and links
- Never use dangerouslySetInnerHTML without DOMPurify
- Escape all dynamic styles
- Avoid secrets and sensitive data in frontend code/state
- Use error boundaries for resilience
- Enforce server-side access control
- Keep dependencies updated and minimal
- Use React StrictMode and CSP in all environments
- Comply with accessibility standards
