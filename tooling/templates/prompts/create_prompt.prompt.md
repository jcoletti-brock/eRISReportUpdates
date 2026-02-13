---
agent: "PromptEngineer"
description: "Create a new prompt definition file from requirements and context."
model: Gemini 3 Pro (Preview) (copilot)
---

Your goal is to design and codify a structured task execution protocol, transforming high-level requirements into a deterministic set of instructions that guides an agent to a successful outcome.

## Create New Prompt Definition

Follow these instructions when a user asks you to create or significantly revise a prompt definition file:

1. Clarify the prompt's purpose and scope.
   - Reference the `Clarify Prompt Purpose and Boundaries` section below for more details.
2. Design the prompt's goal and execution steps.
   - Reference the `Define Goal and Execution Steps` section below for more details.
3. Map the above into a concrete `*.prompt.md` file using the standard template.
   - Reference the `Draft the Prompt File Using the Template` section below for more details.
4. Validate the final prompt file for clarity, determinism, and consistency.
   - Reference the `Validate the Prompt Definition` section below for more details.

## Clarify Prompt Purpose and Boundaries

- Ask (or infer from the request) what specific task this prompt is designed to execute.
- Identify which agent mode is best suited to execute this prompt (e.g., "Engineer", "TechnicalWriter", "SqlDeveloper").
- Distill the purpose into a one–two sentence description suitable for the `description` field in the prompt header.
- Identify explicit boundaries: what the prompt should not cover, and any prerequisites.

## Define Goal and Execution Steps

- Define the "Goal" of the prompt clearly. This is the core objective the agent must achieve.
- Break down the execution into a high-level summary section with a relevant title.
- Create detailed sections for each high-level step.
- Ensure instructions are deterministic and actionable.

## Draft the Prompt File Using the Template

- Use `.github/agents/docs/agentwriter/prompt_file_template.md` as the structural reference.
- Populate the YAML header `agent` with the selected agent mode.
- Populate the YAML header `description` with the distilled task description.
- Replace `<core task objective description ...>` with the defined goal.
- Replace `< High level TODO Summary >` with the high-level steps, ensuring each step includes a sub-bullet referencing its corresponding detailed section.
- Create detailed sections for each step, replacing `<Details Section Title X>` with appropriate titles and content.
- Remove any `AI-NOTE` style guidance before finalizing.
- Save the completed prompt definition as a new file under `.github/prompts/` in the current workspace.

## Validate the Prompt Definition

- Read the final prompt file end-to-end to ensure it is self-contained, clear, and deterministic.
- Check that:
  - The agent mode is appropriate for the task.
  - The goal is clear and achievable.
  - The steps are logical and cover the entire scope of the task.
  - There are no leftover placeholders or notes.
- When returning the result to the user, provide the full `*.prompt.md` content and a brief summary of the prompt's purpose.
