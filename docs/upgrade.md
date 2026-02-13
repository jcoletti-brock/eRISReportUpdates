# Upgrade Guide

Keep AgentKit up to date to get the latest agent templates, bug fixes, and new features.

---

## Quick Reference

| What to Upgrade  | Command                                                                                                                     | When to Use                  |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **CLI Tool**     | `uv tool install --force 'git+https://github.com/brocksolutions/io-copilot.git@main#subdirectory=tooling/python/bootstrap'` | Get latest CLI and templates |
| **One-time Use** | Just run `uvx` as normal                                                                                                    | Always uses latest version   |

---

## Upgrading the CLI Tool

### If you installed with `uv tool install`

```bash
uv tool install --force 'git+https://github.com/brocksolutions/io-copilot.git@main#subdirectory=tooling/python/bootstrap'
```

This reinstalls AgentKit with the latest version, including updated templates.

### If you use `uvx` (one-shot execution)

No upgrade needed—`uvx` always fetches the latest version:

```bash
uvx --from 'git+https://github.com/brocksolutions/io-copilot.git@main#subdirectory=tooling/python/bootstrap' agentkit
```

### Verify the upgrade

```bash
agentkit --version
```

### Uninstalling AgentKit

To remove AgentKit from your system:

```bash
uv tool uninstall agentkit
```

---

## Updating Generated Agent Files

When AgentKit templates are updated (new best practices, improved prompts, etc.), you may want to get the latest changes for your agent files.

### Checking for differences

The simplest way to find differences would be to run AgentKit, select an agent template, and choose `2. Show template content` to view the current template without generating files.

Copy the output text from the template and ask your agent to compare the new template to your existing (tailored) agent file for the same expertise.

The agent should be able to highlight differences and suggest updates if you deem them appropriate.

## Next Steps

After upgrading:

- **Test new templates:** Run `agentkit` to see if new templates are available
- **Review release notes:** Check [GitHub Releases](https://github.com/brocksolutions/io-copilot/releases) for changes
- **Update documentation:** Review the [installation guide](installation.md) for new features
