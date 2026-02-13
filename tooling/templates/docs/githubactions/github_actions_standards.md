# GitHub Actions Standards and Best Practices

This document provides comprehensive guidance on workflow syntax, security best practices, performance optimization, testing strategies, and common integration patterns for GitHub Actions.

## Core Resources

- [GitHub Actions Workflow Syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Context Variables](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts)
- [Actions Toolkit Documentation](https://github.com/actions/toolkit)
- [Marketplace Actions](https://github.com/marketplace?type=actions)

## Workflow Development Guidelines

**ALWAYS** before making any changes to a workflow review the workflow to ensure actions are not being duplicated or redundant.
**ALWAYS** ensure that steps are using outputs or caches from previous steps where possible.
**ALWAYS** Review the context documentation to understand if we have access to information that could make the flow more efficient or secure.

### Basic Workflow Structure

```yaml
name: CI/CD Pipeline
on:
  push:
    branches:
      - main
      - "dev/**"
    paths:
      - "services/backend/**"
      - "services/common/**"
  pull_request:
    branches:
      - main
      - "dev/**"
    paths:
      - "services/backend/**"
      - "services/common/**"
  workflow_dispatch: # Allow manual triggering

# Environment variables here, example only, depends on your project and action
env:
  NODE_VERSION: "18"
  PYTHON_VERSION: "3.11"

# Jobs define the steps to be executed, example only, depends on your project and action
jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16, 18, 20]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: "npm"
      - run: npm ci
      - run: npm run lint
      - run: npm test
```

### Security Best Practices

#### Secrets Management

- Never hardcode secrets in workflows
- Use `${{ secrets.SECRET_NAME }}` for sensitive data
- Limit secret scope to specific environments when possible
- Use OIDC for cloud provider authentication instead of long-lived tokens

#### Permissions

```yaml
permissions:
  contents: read # Default minimal permissions
  pull-requests: write # Only add what's needed
  issues: write
  id-token: write # For OIDC authentication
```

#### Third-Party Actions

- Use trusted, well-maintained actions from verified publishers
- Review action source code before use in production

### Performance Optimization

#### Caching Strategies

```yaml
- uses: actions/cache@v3
  with:
    path: |
      ~/.npm
      ~/.cache/pip
      node_modules
      .venv
    key: ${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json', '**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-deps-
```

#### Job Parallelization

```yaml
jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        include:
          - os: ubuntu-latest
            artifact-name: linux-build
          - os: windows-latest
            artifact-name: windows-build
          - os: macos-latest
            artifact-name: macos-build
```

#### Conditional Execution

```yaml
- name: Deploy to staging
  if: github.ref == 'refs/heads/develop'
  run: echo "Deploying to staging"

- name: Deploy to production
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
  run: echo "Deploying to production"
```

### Advanced Patterns

#### Reusable Workflows

```yaml
# .github/workflows/reusable-build.yml
on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
    secrets:
      api-key:
        required: true

jobs:
  build:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - uses: actions/checkout@v4
      - name: Build
        run: echo "Building for ${{ inputs.environment }}"
```

#### Custom Actions Development

```yaml
# action.yml
name: "Custom Build Action"
description: "Builds and tests the application"
inputs:
  node-version:
    description: "Node.js version to use"
    required: false
    default: "18"
outputs:
  build-status:
    description: "Build status result"
runs:
  using: "node20"
  main: "dist/index.js"
```

#### Environment-Specific Deployments

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://example.com
    steps:
      - name: Deploy
        run: echo "Deploying to production"
```

### Error Handling and Debugging

#### Fail-Fast vs Continue-on-Error

```yaml
- name: Critical step
  run: exit 1  # This will fail the job

- name: Optional step
  run: exit 1
  continue-on-error: true  # Job continues even if this fails

strategy:
  fail-fast: false  # Don't cancel other matrix jobs on failure
```

#### Debug Logging

```yaml
- name: Debug workflow
  run: |
    echo "Runner OS: ${{ runner.os }}"
    echo "GitHub ref: ${{ github.ref }}"
    echo "Event name: ${{ github.event_name }}"
    echo "Actor: ${{ github.actor }}"
  env:
    ACTIONS_RUNNER_DEBUG: true
    ACTIONS_STEP_DEBUG: true
```

#### Artifact Management

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: build-artifacts
    path: |
      dist/
      build/
    retention-days: 30

- uses: actions/download-artifact@v4
  with:
    name: build-artifacts
    path: ./artifacts
```

### Common Action Patterns

#### Multi-Stage Build Pipeline

```yaml
jobs:
  build:
    outputs:
      version: ${{ steps.version.outputs.version }}
    steps:
      - id: version
        run: echo "version=$(date +%Y%m%d-%H%M%S)" >> $GITHUB_OUTPUT

  test:
    needs: build
    steps:
      - run: echo "Testing version ${{ needs.build.outputs.version }}"

  deploy:
    needs: [build, test]
    if: github.ref == 'refs/heads/main'
    steps:
      - run: echo "Deploying version ${{ needs.build.outputs.version }}"
```

#### Docker Build and Push

```yaml
- name: Build and push Docker image
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: |
      myregistry/myapp:latest
      myregistry/myapp:${{ github.sha }}
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

### Monitoring and Notifications

#### Microsoft Teams Integration

Use an Incoming Webhook on the Teams channel you want to post to and store the webhook URL in a repository secret (for example: `TEAMS_WEBHOOK_URL`). A simple and reliable pattern is to build a MessageCard (Connector) payload and post it with `curl` so you don't depend on third-party actions.

```yaml
- name: Notify Microsoft Teams on failure
  if: failure()
  env:
    TEAMS_WEBHOOK_URL: ${{ secrets.TEAMS_WEBHOOK_URL }}
  run: |
    cat > payload.json <<EOF
    {
      "@type": "MessageCard",
      "@context": "http://schema.org/extensions",
      "summary": "Build failed for ${{ github.repository }}",
      "themeColor": "FF0000",
      "title": "Build failed for ${{ github.repository }}",
      "sections": [
        {
          "activityTitle": "Branch: ${{ github.ref_name }}",
          "facts": [
            { "name": "Commit", "value": "${{ github.sha }}" }
          ]
        }
      ]
    }
    EOF
    curl -H "Content-Type: application/json" -d @payload.json "$TEAMS_WEBHOOK_URL"
```

Notes:

- Keep the webhook secret-scoped and rotate it if access changes.
- For richer notifications consider using Adaptive Cards or a small action that formats run summaries before posting.

### Custom Action Development (TypeScript)

#### Package Structure

```
action/
├── action.yml
├── src/
│   ├── main.ts
│   └── types.ts
├── dist/
│   └── index.js
├── package.json
└── tsconfig.json
```

#### Core Action Template

```typescript
import * as core from "@actions/core";
import * as github from "@actions/github";

async function run(): Promise<void> {
  try {
    // Get inputs
    const myInput = core.getInput("my-input", { required: true });
    const myOptionalInput = core.getBooleanInput("optional-flag");

    // Use GitHub context
    const { context } = github;
    core.info(`Processing ${context.repo.owner}/${context.repo.repo}`);

    // Your action logic here
    const result = await performAction(myInput);

    // Set outputs
    core.setOutput("result", result);
    core.summary.addHeading("Action Results");
    core.summary.addCodeBlock(JSON.stringify(result, null, 2), "json");
    await core.summary.write();
  } catch (error) {
    core.setFailed(error instanceof Error ? error.message : String(error));
  }
}

async function performAction(input: string): Promise<any> {
  // Implementation here
  return { success: true, input };
}

run();
```

### Testing Strategies

#### Local Testing with act

```bash
# Install act
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Test specific workflow
act -j test

# Test with secrets
act -j deploy --secret-file .secrets
```

#### Unit Testing Actions

```typescript
// __tests__/main.test.ts
import { run } from "../src/main";
import * as core from "@actions/core";

jest.mock("@actions/core");

describe("action", () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it("should process input correctly", async () => {
    (core.getInput as jest.Mock).mockReturnValue("test-input");

    await run();

    expect(core.setOutput).toHaveBeenCalledWith("result", expect.any(Object));
  });
});
```

### Common Issues and Solutions

#### PATH Issues

```yaml
- name: Add to PATH
  run: echo "$HOME/.local/bin" >> $GITHUB_PATH

- name: Verify PATH
  run: echo $PATH
```

#### Environment Variables

```yaml
- name: Set environment variable
  run: |
    echo "MY_VAR=value" >> $GITHUB_ENV
    echo "MULTILINE_VAR<<EOF" >> $GITHUB_ENV
    echo "line 1" >> $GITHUB_ENV
    echo "line 2" >> $GITHUB_ENV
    echo "EOF" >> $GITHUB_ENV
```

#### Matrix Build Failures

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
  fail-fast: false # Continue other versions on failure
```

## Best Practices Summary

1. **Security First**: Use minimal permissions, pin action versions, manage secrets properly
2. **Performance**: Leverage caching, parallel jobs, and conditional execution
3. **Maintainability**: Use reusable workflows, clear naming, and comprehensive documentation
4. **Monitoring**: Implement proper logging, notifications, and artifact management
5. **Testing**: Test locally with act, write unit tests for custom actions
6. **Error Handling**: Use appropriate continue-on-error and fail-fast strategies

## Common Workflow Templates

### Node.js Project

```yaml
name: Node.js CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16, 18, 20]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: "npm"
      - run: npm ci
      - run: npm run build --if-present
      - run: npm test
```

### Python Project

```yaml
name: Python CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10, 3.11]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

### Docker Build

```yaml
name: Docker Build
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ghcr.io/${{ github.repository }}:latest
```
