# Agents

This folder contains the definitions for specialized AI agents used within the workspace. These agents are designed to bring specific expertise and structured workflows to your development tasks.

## What is an Agent?

An agent is a specialized AI persona configured with a specific role, domain expertise, and operational boundaries. Unlike a generic chat interface, an agent is purpose-built to handle distinct categories of work—such as reviewing SQL code, architecting solutions, or writing technical documentation. By switching between agents, you ensure that the AI adopts the correct mindset, tools, and standards for the task at hand.

## What Agent Files Define

Each `*.agent.md` file in this directory defines the configuration for a single agent. These definitions establish:

- **Identity & Role:** The agent's name and high-level description
- **Core Goal:** The primary objective the agent strives to achieve in every interaction.
- **Responsibilities:** A concrete list of tasks the agent is expected to perform.
- **Boundaries:** Explicit constraints on what the agent should *not* do, ensuring it stays within its scope.
- **Context & Standards:** References to documentation, coding standards, and best practices that the agent must adhere to.

By defining these elements, we create deterministic and reliable AI partners that integrate seamlessly into the development lifecycle.
