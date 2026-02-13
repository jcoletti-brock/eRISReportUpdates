# Installation Guide

## Prerequisites

- **Linux/macOS** (or Windows with PowerShell)
- [GitHub Copilot](https://code.visualstudio.com/) in VS Code
- [uv](https://docs.astral.sh/uv/) for package management
- [Python 3.12+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- **GitHub Authentication** (required for private repositories)

## GitHub Authentication

AgentKit downloads templates from GitHub releases. For private/internal repositories, you need to authenticate.

### Option 1: GitHub CLI (Recommended)

Install and authenticate with GitHub CLI:

```bash
# Install gh (if not already installed)
# macOS
brew install gh

# Linux
# See: https://github.com/cli/cli/blob/trunk/docs/install_linux.md

# Authenticate
gh auth login
```

AgentKit will automatically use your `gh` authentication.

### Option 2: Environment Variable

Set a GitHub Personal Access Token:

```bash
# Add to your ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="your_github_token_here"

# Or use GH_TOKEN
export GH_TOKEN="your_github_token_here"
```

**Creating a Personal Access Token:**

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with `repo` scope (for private repos)
3. Copy the token and set it as shown above

**Note:** `GITHUB_TOKEN` is the standard variable name. `GH_TOKEN` is also supported for compatibility.

## Installation

### Install with uv

Install agentkit globally using uv:

```bash
uv tool install 'git+https://github.com/brocksolutions/io-copilot.git@main#subdirectory=tooling/python/bootstrap'
```

Then run it anytime:

```bash
agentkit
```

### Uninstall

To remove agentkit from your system:

```bash
uv tool uninstall agentkit
```

### Try Without Installing

{{ AI-FIXME: Need to test this with regards to output directory }}

Run agentkit directly using uvx without installation:

```bash
uvx --from 'git+https://github.com/brocksolutions/io-copilot.git@main#subdirectory=tooling/python/bootstrap' agentkit
```

### What Happens When You Run It

The CLI launches an interactive prompt that guides you through:

1. Selecting which agent template to create
2. Providing answers to template prompts
3. Generating the final agent file

### Local Development

To work with the source code or contribute:

```bash
# Clone the repository
git clone https://github.com/brocksolutions/io-copilot.git
cd io-copilot/tooling/python/bootstrap

# Run the CLI
uv run agentkit
```
