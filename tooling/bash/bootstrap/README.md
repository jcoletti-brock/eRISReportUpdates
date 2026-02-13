# Agent Template Engine

Customize AI agent personalities and workflows by answering a series of guided questions. The Agent Template Engine transforms your responses into a ready-to-use agent prompt.

## The Output: Your Personalized Agent Prompt

- The tool helps you generate an **answer sheet** by guiding you through a series of questions about your specific needs, preferences, and environment. Based on your responses,
- The tool generates a **customized agent prompt**.
- You are expected to then use this prompt with an agent of your choice.
  - We suggest a thinking model such as GPT-5.2, Claude 4.5, or Gemini Pro.

### Why use an agent, we're just filling out a template anyway?

The advantage of using and agent is that we can give it instructions to do this tasks which requires reasoning and context from your current workspace. If we used a static template with user answers, the user would be fully responsibly for making sure all inputs were absolutely accurate, up to date, and matched the expected input format given the prompt engineering template.

Examples include:

- Reconciling file paths to reference documentation
- Evaluating your codebase to provide suggestions on tweaks or improvements to the prompt engineering.

## What You Can Do

- **Choose from multiple agent templates** — Select pre-built agent types tailored to different roles and tasks
- **Answer guided questions** — Provide information about your specific needs, preferences, and environment through an interactive prompt
- **Preview template content** — Review what the agent template contains before customizing it
- **Customize your answers** — Review what you've provided and make any necessary adjustments
- **Generate personalized agent prompts** — Create customized agent configuration files tailored to your exact requirements

## How It Works

1. **Start the engine** — Run the application to open the interactive menu
2. **Select an agent template** — Browse available templates and pick the one that fits your role
3. **Answer customization questions** — Respond to guided questions about your environment, coding standards, tools, and preferences
4. **Review and tweak your answers** — Review what you've provided and make any necessary adjustments in the answer file
5. **Generate your agent prompt** — Generate a custom agent prompt to be used to configure your AI agent

## Getting Started

### Running the Application

From the command line, launch the interactive menu:

```bash
# Navigate to the bootstrap directory
cd tooling/bash/bootstrap

# Run the application
./agentkit.sh
```
