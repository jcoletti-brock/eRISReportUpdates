---
description: "Generate a finalized agent file from a template and user-provided answers."
---

Your goal is to create a production-ready agent definition file by validating and adapting the provided draft content to the target workspace.

<generate_agent_file_from_template>

Follow these instructions to create the finalized agent file:

1. Review the agent creation standards.
   - Reference the `Review Agent Creation Standards` section below for more details.
2. Use the rendered template content as your starting point.
   - Reference the `Rendered Template Content` section below for the draft agent file.
3. Validate and reconcile the content for the target workspace.
   - Reference the `Validate and Reconcile Content` section below for more details.
4. Output the finalized agent file.
   - Reference the `Output the Agent File` section below for more details.

</generate_agent_file_from_template>

<review_agent_creation_standards>

Before modifying the draft content, review the agent file authoring guidelines:

- Read `core/PromptEngineer.agent.md` for your roles and repsonsibilities.
- Read `prompts/create_agent.prompt.md` for the standard agent creation workflow.
- Read `docs/agentwriter/agent_file_template.md` for the required file structure.

**CRITICAL AGENT NOTE**

The first step in your TODO will always be to review the referenced supporting documentation. Do not skip this step, unless the documents have already been reviewed in this session and are not summarized in your memory.

</review_agent_creation_standards>

<rendered_template_content>

The following content was generated from an agent template with user-provided answers. Use this as your starting draft:

---

{{RENDERED_CONTENT}}

---

</rendered_template_content>

<validate_and_reconcile_content>

Perform the following validation tasks on the draft content:

1. **Verify file references** — Check that all referenced documentation paths exist in the workspace.
   - If a path doesn't exist, search for equivalent documentation in the workspace.
   - If no equivalent exists, remove the reference and note it for the user.
   - Update paths to use correct workspace-relative format.

2. **Validate tool references** — Confirm any MCP tools or external tooling mentioned are available.
   - Check `.vscode/mcp.json` or workspace configuration for available tools.
   - Flag references to unavailable tools.

3. **Check standards alignment** — Ensure the agent file follows the patterns from the template guidelines.
   - Verify YAML frontmatter is properly formatted.
   - Confirm all required sections are present.
   - Remove any leftover template placeholders or comments.

4. **Adapt terminology** — Adjust generic terms to match the project's conventions.
   - Align service names, architectural terms, and patterns with workspace usage.

</validate_and_reconcile_content>

<output_the_agent_file>

1. Present the finalized agent file content in full.
2. Save the file to `.github/agents/{{AGENT_NAME}}.agent.md`.
3. Summarize any changes made during validation:
   - File references that were updated or removed.
   - Tools that were flagged as unavailable.
   - Terminology adjustments made.

</output_the_agent_file>
