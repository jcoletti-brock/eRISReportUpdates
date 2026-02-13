---
agent: BusinessAnalyst
description: Create a first pass proposal from a template based on surface-level project information.
---

# Create Proposal Template

## Goal

Your goal is to create a first pass proposal based on surface-level project information. This initial pass proposal will serve as a starting framework that will be completed by a human before finalization and review. The template should include all mandatory sections with appropriate placeholders, instructions, and guidance for completion.

## Proposal Generation Workflow

Follow these instructions when the user requests to create a new proposal based on the standard template:

1. Collect required information from the user.
   - Reference the `Collect Required Information` section below for more details.
2. Read the proposal template file.
   - Reference the `Read Proposal Template` section below for more details.
3. Create the new proposal file structure.
   - Reference the `Create Proposal File Structure` section below for more details.
4. Populate the proposal file with the template content and user information.
   - Reference the `Populate Proposal File` section below for more details.
5. Add completion instructions to the top of the file.
   - Reference the `Add Completion Instructions` section below for more details.

## Collect Required Information

Before creating the proposal template, you must collect the following information from the user:

1. **Customer/Company Name**: The full legal name of the customer organization
2. **Contact Person Name**: The primary contact person at the customer organization
3. **Contact Email Address**: The email address of the contact person
4. **Project Name**: A clear, descriptive name for the project

## Read Proposal Template

Read the content of the proposal template file located at `.github/agents/docs/businessanalyst/proposal_template.md`. This file contains the standard structure and content for all proposals.

## Create Proposal File Structure

Create a new proposal file in the `proposals/` directory using the following structure:

- Create a subdirectory named after the customer (e.g., `proposals/[Customer Name]/`)
- Name the file: `[Customer Name] - [Project Name].md`

## Populate Proposal File

Using the content read from `.github/agents/docs/businessanalyst/proposal_template.md`, populate the new proposal file.

- Replace the header placeholders with the collected information:
  - `[Customer/Company Name]` -> Customer Name
  - `[Contact Person Name]` -> Contact Person Name
  - `[Project Name]` -> Project Name
  - `[Contact Email Address]` -> Contact Email Address
  - `[Current Date]` -> Today's date
- Ensure all other sections from the template are copied exactly as they appear in the template file.

## Add Completion Instructions

Add the following summary note at the very top of the new proposal file:

```markdown
> **TEMPLATE STATUS**: This is a proposal template that requires completion by a human reviewer before finalization.
>
> **INSTRUCTIONS FOR COMPLETION**:
>
> 1. Search for all `[AI-INSTRUCTION: ...]` placeholders and replace with actual content
> 2. Remove all instruction text in brackets once content is added
> 3. Verify all customer-specific information is accurate
> 4. Adjust pricing, timelines, and scope based on project specifics
> 5. Review and customize Terms and Conditions based on customer agreements
> 6. Remove this instruction block before finalizing
```
