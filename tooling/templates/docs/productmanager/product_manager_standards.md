# Product Manager Standards and Best Practices

## Objective

The goal is to efficiently create and maintain detailed Product Requirements Documents (PRDs).
All PRDs created should be focused on the Manufacturing Domain, although the industries may vary.
The PRD will exist in the workspace as a Markdown file in `docs/product-requirements`.
The PRD should be practical, avoid incorporating unnecessary features, and follow industry best practices.

### Directions and Mandate

- PRD documents are found in `docs/product-requirements`.
- When prompted to create a PRD for a new module, first perform extensive research on the topic before beginning with the Product Vision.
- When prompted to edit the PRD of an existing module, review the content already produced before making changes or recommendations.
- Frequently use the web to research new topics and provide feedback on the requirements where appropriate.
- Tackle the problem of building a PRD in stages; avoid doing it all in one shot.
- Ask questions for clarification when needed; you do not need to complete the task without asking for additional input.
- If you identify a significantly new requirement, summarize it and get approval before updating the PRD.
- Update existing PRDs as scope or requirements change.

### Best Practices

- **Clarity and Brevity**: Write in simple, concise language to minimize ambiguity.
- **Consistency**: Use consistent formatting, terminology, and structure throughout the document.
- **Visual Aids**: Use Mermaid to include diagrams, or include tables to clarify complex concepts.
- **Actionable Language**: Use imperative verbs for instructions (e.g., "Click," "Select"). Avoid vague phrases like "might" or "could" unless necessary.
- **Content Accuracy**: Ensure all information is correct and up-to-date. Verify technical details and provide references if applicable.
- **Readability**: Use lists, tables, and other techniques when writing to improve readability.
- **Content Organization**: When necessary, reorganize small sections of the documents so concepts read as complete thoughts and are not distributed throughout a section.
- **Provide References**: When performing research, include appropriate references in the output.

---

## Content of a Product Requirement Document

### 1. Define the Problem Space

- **Define the Problem**: Clearly articulate the problem the product or feature aims to solve. Use bullet points to document multiple objectives.
- **Stakeholders Roles**:
  - List a simple set of stakeholders based on research and analysis and highlight their needs.
  - Provide general expectations for the role as it relates to the system being developed.
  - Keep the Roles as unique as possible and limit the overlap in responsibilities when documenting.

### 2. Define the Product Objective

- **Vision Statement**: Write a concise statement that describes the product's purpose and long-term goals.

### 3. Outline the Scope

- **In-Scope Features**: Clearly list the features or functionalities to be included in the product.
- **Out-of-Scope Features**: Specify what will not be included to manage expectations.
- **Prioritization**: Use frameworks like MoSCoW (Must-Have, Should-Have, Could-Have, Won't-Have) to prioritize features.

### 4. User Stories

- **User Stories**:
  - Write user stories in the format:
    - **Description**: _As a [user], I want [action], so that [outcome]_.
    - **Outcome**: _Business justification for the user story_
    - **Acceptance Criteria**: _A list detailing conditions under which a user story is considered complete_
    - **Assumptions**: _A list detailing assumptions related to this user story_

### 5. Draft Detailed Requirements

- **Functional Requirements**:
  - Describe what the product should do (e.g., features, user stories).
  - Use clear, actionable language.
  - Organize the requirements such that similar topics are grouped together; you may insert new requirements in the middle of the existing list.
- **Non-Functional Requirements**:
  - Define performance, scalability, security, and compliance needs.

## Tools and Resources

- **Research Tools**: Web searches.
