# Proposal Standards

## Best Practices for Proposal Writing

- **Eliminate Ambiguity**: Use precise, definitive language. Avoid vague terms like "approximately," "might," "could," "various," or "several"
- **Quantify Everything**: Provide specific numbers for deliverables, timelines, costs, and resources
- **Clear Scope Boundaries**: Explicitly state what is included AND what is excluded
- **Consistent Terminology**: Use the same terms throughout the document; create a glossary if needed
- **Structured Format**: Follow a logical, consistent structure for all proposals
- **Visual Clarity**: Use tables, diagrams (mermaid), and lists to present complex information
- **Active Voice**: Use imperative language for deliverables and requirements
- **Risk Mitigation**: Identify potential risks and provide mitigation strategies
- **Assumption Documentation**: Clearly list all assumptions and their implications
- **Verification Criteria**: Define measurable acceptance criteria for all deliverables

## Required Proposal Structure

**CRITICAL**: All Brock Solutions proposals MUST include the following sections in this exact order. These sections are mandatory and define the standard proposal format.

### 1. **Introduction** (REQUIRED)

Provide a brief introduction that covers:

- **Brock Solutions**: 1-2 sentence company introduction establishing credibility
- **Customer Context**: Brief description of the customer and their organization
- **Project Introduction**: Clear statement of what the proposal addresses
- **Project Objective**: Concise overview of the project goal and expected outcome

Keep this section focused and concise (typically 2-4 paragraphs maximum).

### 2. **Scope** (REQUIRED)

Detailed outline of what is included and NOT included in the project proposal.

- **In-Scope Items**:

  - Detailed list of deliverables with specific descriptions
  - Features and functionalities to be implemented
  - Services to be provided (design, development, testing, training, etc.)
  - Documentation to be delivered
  - System components and integrations

- **Out-of-Scope Items**:
  - Explicitly list what is NOT included
  - Identify common misunderstandings or scope creep areas
  - Reference future phases or capabilities (e.g., "automated data capture is not part of this scope")
  - Clarify boundaries for integrations or features

**Important**: The Scope section should be comprehensive and detailed. Break down functionality by user stories, system components, or technical requirements as appropriate. Use subsections like "Application Functionality", "System Architecture", "Licensing", etc. to organize complex scopes.

### 3. **Schedule and Workplan** (REQUIRED)

Describes how long the project will run with timeline details:

- **Duration**: Total estimated project duration (e.g., "8 weeks", "3 months")
- **Start Date Assumption**: Provide approximate dates assuming a specific start date
  - Example: "The project will commence in [Month Year] and is estimated to complete by [Month Year]"
- **Project Phases**: Break down the timeline into clear phases with durations:
  - **Design Phase**: Duration and key activities
  - **Development/Configure Phase**: Duration and key activities
  - **Testing Phase**: Duration and key activities
  - **Deploy/Commissioning Phase**: Duration and key activities
- **Milestones**: Key checkpoints and deliverable dates
- **Dependencies**: Note any schedule dependencies on customer activities

### 4. **Team** (REQUIRED)

Clear distinction of roles from both Brock Solutions and Customer perspectives:

- **Brock Solutions Team**:

  - List each role (Project Manager, Technical Lead, Developers, etc.)
  - Provide brief description of responsibilities for each role
  - Use a table format for clarity
  - Example roles: Project Manager, Software Technical Lead, Controls Lead, Developers/Software Configuration

- **Customer Team Requirements**:
  - List required customer roles and their involvement
  - Specify approximate weekly time allocations per role
  - Example: "BCAD IT Specialist: 2-4 hours per week for server setup and network configuration"
  - Example: "Maintenance Manager: 1-2 hours per week for design reviews and feedback"
  - Include roles like: Technical Stakeholders, IT Resources, Executive Sponsorship, Subject Matter Experts

**Important**: Be specific about customer time commitments to set realistic expectations.

### 5. **Pricing** (REQUIRED)

Tabular breakdown of project costs:

- **Total Project Cost**: Clearly stated total amount (e.g., "$77,300.00")
- **Cost Breakdown** (if applicable):
  - Use table format to break down costs by category
  - Categories may include: Development, Testing, Hardware, Licenses, Site Visits, etc.
- **Included Items**: What the pricing includes (e.g., "includes 2 site visits")
- **Payment Milestones**: Table showing payment schedule
  - Milestone name
  - Milestone requirements/deliverables
  - Payment percentage or amount
- **Pricing Notes**:
  - Currency (USD, CAD, etc.)
  - Tax exclusions
  - Validity period (e.g., "valid for 30 days")
  - Purchase order requirements
  - Billing terms (monthly, milestone-based)
  - Late payment interest rates
  - Payment prerequisites

### 6. **Assumptions and Clarifications** (REQUIRED)

Bulleted list that makes the Scope section more concrete and explicit:

- **Architecture Assumptions**: Server specs, network requirements, existing infrastructure
- **Customer Availability**: Expected responsiveness, review timelines, decision-making
- **Access Requirements**: Site access, system access, credentials, environments
- **Customer Responsibilities**: What the customer must provide or perform
- **Technical Assumptions**: Integration endpoints, data availability, system capabilities
- **Scope Boundaries**: Clarifications on what's manual vs. automated, current vs. future phases
- **Change Management**: Process for handling scope changes (reference ECP process)
- **Agreements**: Reference to Terms and Conditions or Master Services Agreement (MSA)

**Important**: This section eliminates ambiguity by making implicit assumptions explicit. Include items like:

- "BCAD IT will perform server provisioning..."
- "For the initial implementation, status conditions are expected to be manually toggled..."
- "Any additional requests for functionality will need to be addressed in an Engineering Change Proposal (ECP)"

### 7. **Terms and Conditions** (REQUIRED - with conditions)

Standard set of items, usually defined and copy/pasted based on customer agreement:

- **Site Access**: Assumptions about uninterrupted access, assistance, standby time billing
- **Customer Role and Responsibilities**: Information provision, document accuracy, timely reviews
- **Warranty and Project Performance**: Warranty period, coverage, limitations, support terms
- **Ownership and Use of Intellectual Property (IP)**: License grants, ownership rights, restrictions
- **Indemnities and Limitation of Liability**: Mutual indemnification, liability caps, exclusions
- **Confidentiality**: Handling of confidential information by both parties
- **Changes to Scope of Project**: Time and material rates for scope changes
- **Governing Law & Dispute Resolution**: Jurisdiction, arbitration terms

**Important**: These terms are typically standardized. Reference existing customer agreements (MSA) when applicable. Ensure time and material rates table is included for potential scope changes.

**NOTE**: This Terms and Conditions section is only required if there is no mention of an existing Master Services Agreement (MSA) in the proposal. One of the two must be present - either a full Terms and Conditions section OR a reference to an existing MSA with the customer.

## Output Standards

### Document Format

- All proposals are in Markdown format
- Stored in `proposals/` directory in a project-specific subdirectory using the format: `proposals/CustomerName-ProjectName/`
- Named using convention: `CustomerName-ProjectName.md`
- Example: A proposal for Fort Lauderdale Airport's Gate Monitoring project would be stored as `proposals/FLL-GateMonitoring/FLL-GateMonitoring.md`

### Document Structure and Formatting

**Header Information (Top of Document)**

Every proposal must begin with a header table containing key project information:

```markdown
---

**Company [Customer/Company Name]
Name:**

---

**Attention:** [Contact Person Name]

**Subject:** [Project Name]

**Date:** [Current Date]

**E-Mail:** [Contact Email Address]

**Quote #:** [Quote Number or TBD]

**Version #:** [Version Number, e.g., 1.0]

---
```

**Section Headers**

Use Markdown headers to clearly delineate each mandatory section:

- Use `##` (level 2) headers for main sections: `## Introduction`, `## Scope`, `## Schedule and Workplan`, etc.
- Use `###` (level 3) headers for subsections: `### Application Functionality`, `### Brock Solutions Team`, `### Pricing Notes`, etc.
- Use `####` (level 4) headers for nested subsections when needed

**Example Structure:**

```markdown
## Introduction

[Introduction content...]

## Scope

[Scope overview...]

### Application Functionality

[Details on features...]

### System Architecture

[Architecture details...]

### Out of Scope

[Exclusions...]

## Schedule and Workplan

[Timeline overview...]

### Design Phase

[Design phase details...]

### Development/Configure Phase

[Development details...]
```

**Formatting Guidelines**

- **Bold text** for emphasis on key terms, section labels, or important statements (e.g., `**Total Project Cost**`, `**Duration**`)
- Use tables for structured data (Team roles, Pricing breakdown, Payment milestones, T&M rates)
- Use bullet points (`-`) for lists of items, features, or assumptions
- Use numbered lists for sequential steps or prioritized items
- Use blockquotes (`>`) for important notes or callouts if needed
- Maintain consistent spacing between sections (typically one blank line after headers, two blank lines between major sections)

### Version Control

- Track significant changes in a revision history section
- Use semantic versioning (major.minor.patch)
- Document what changed and why
- Maintain previous versions for reference

### Quality Standards

- Zero tolerance for ambiguity in scope and deliverables
- All estimates must have supporting rationale
- Every assumption must be explicitly stated
- Technical accuracy is paramount
- Client perspective and business value are prioritized
