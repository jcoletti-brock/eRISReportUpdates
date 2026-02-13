# Release Process

This document describes the process for creating and deploying AgentKit release packages.

## Overview

AgentKit uses an automated release workflow that:

- Automatically increments version numbers
- Packages templates into a distribution archive
- Creates GitHub releases with release notes
- Makes packages available for download

## Release Components

### 1. Template Package

The release package (`agentkit-templates-<version>.zip`) contains:

- All agent templates from `tooling/templates/`
- Agent file templates (`.agent.md` files)
- Prompt templates
- Documentation templates
- Supporting configuration files

### 2. Version Management

Versions follow semantic versioning (`vMAJOR.MINOR.PATCH`):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes and minor updates

## Automated Release Workflow

### Trigger Conditions

The release workflow automatically runs when:

- Changes are pushed to `main` branch
- Changes affect `tooling/templates/**` or `tooling/python/bootstrap/**`
- Manual workflow dispatch is triggered

## Preparing a release

The repo contains a dev/release branch that is used to stage changes for the next release. Follow these steps to prepare a release:

- IF the release is adjusting the major or minor version, tag the latest dev/release branch commit with the new version (e.g., `v1.2.0`).
- Merge the dev/release branch into main.
  - The release workflow will automatically run on main, create the packages and a GitHub release.

NOTE: The release line will always autoincrement the patch version. IE: 1.2.0 will become 1.2.1.
