---
agent: BusinessAnalyst
description: Conduct a comprehensive review of a proposal to ensure quality, completeness, and risk management.
---

Your goal is to conduct a comprehensive review of an existing proposal to ensure it meets quality standards, eliminates ambiguity, properly manages risk, and sets accurate client expectations. The review should identify gaps, inconsistencies, and areas of improvement while verifying completeness against the mandatory proposal structure.

**Critical Focus Areas:**

- **Misinterpretation & Misleading Content:** Flag any statements that could be misunderstood or interpreted in multiple ways
- **Uncalled Assumptions:** Identify implicit assumptions that are not explicitly documented
- **Mandatory Sections:** Verify all seven required sections are present and complete
- **Clean Reviews:** If the proposal has no issues, simply state that the proposal is ready for submission with no concerns

## Review Process

Follow these instructions to conduct a proposal review:

1. Perform an initial assessment of the proposal structure and mandatory sections.
   - Reference the `Initial Assessment` section below for more details.
   - **IMPORTANT** Always use the `mcp-microsoft-word` tool to read docx files.
2. Systematically review each mandatory section against specific criteria.
   - Reference the `Section-by-Section Review Criteria` section below for more details.
3. Evaluate the proposal for cross-cutting concerns like clarity, ambiguity, and risk.
   - Reference the `Cross-Cutting Review Criteria` section below for more details.
4. Generate a review report if issues are found, or confirm readiness.
   - Reference the `Review Output Format` section below for more details.

## Initial Assessment

Begin by performing a high-level assessment:

- Confirm the proposal is located in the `proposals/` directory
- Verify the file follows naming conventions
- **CRITICAL: Check that all seven mandatory sections are present:**
  1. Introduction
  2. Scope
  3. Schedule and Workplan
  4. Team
  5. Pricing
  6. Assumptions and Clarifications
  7. Terms and Conditions
- Review the overall structure and flow
- If all sections are present and no issues are found, the review can conclude positively

## Section-by-Section Review Criteria

### 1. Introduction Review

**Check for:**

- [ ] Brock Solutions introduction (1-2 sentences) establishes credibility
- [ ] Customer context is clearly described
- [ ] Project introduction clearly states what the proposal addresses
- [ ] Project objective is concise and describes expected outcome
- [ ] Length is appropriate (typically 2-4 paragraphs maximum)
- [ ] Language is clear and professional
- [ ] No vague or ambiguous terms

**Questions to Ask:**

- Is the business value clearly articulated?
- Will the customer understand why this project matters?
- Are there any unsupported claims or assumptions?

### 2. Scope Review

**Check for:**

- [ ] Deliverables are specific and detailed
- [ ] Features and functionalities are clearly described
- [ ] Services to be provided are explicitly listed
- [ ] Documentation deliverables are specified
- [ ] System components and integrations are defined
- [ ] **Out-of-Scope section exists and is comprehensive**
- [ ] Common scope creep areas are explicitly excluded
- [ ] Subsections organize complex scopes (e.g., "Application Functionality", "System Architecture")
- [ ] User stories or requirements are included where applicable
- [ ] Customer responsibilities are clearly stated

**Red Flags:**

- Vague quantifiers: "approximately," "various," "several," "some"
- Undefined technical terms without context
- Missing out-of-scope section
- Ambiguous statements that could be interpreted multiple ways
- Incomplete feature descriptions
- Missing acceptance criteria for deliverables

**Questions to Ask:**

- Can each deliverable be objectively verified?
- Are there any implied deliverables not explicitly stated?
- What could a customer misunderstand or assume is included?
- Are integration boundaries clear?
- Is it clear what's manual vs. automated?

### 3. Schedule and Workplan Review

**Check for:**

- [ ] Total project duration is specified
- [ ] Start date assumption is provided
- [ ] Project phases are clearly defined with durations
- [ ] Key activities for each phase are described
- [ ] Milestones are identified with timeframes
- [ ] Dependencies on customer activities are noted
- [ ] Timeline is realistic based on scope
- [ ] Customer involvement expectations are clear for each phase

**Red Flags:**

- Overly optimistic timelines
- Missing phase durations
- No buffer for reviews or revisions
- Unrealistic assumptions about customer availability
- Dependencies not identified
- No contingency planning

**Questions to Ask:**

- Is this timeline realistic for the scope defined?
- Are there any hidden dependencies?
- Is customer availability properly accounted for?
- What could cause delays?

### 4. Team Review

**Check for:**

- [ ] Brock Solutions team structure is clearly defined
- [ ] Each Brock role has clear responsibilities
- [ ] Table format is used for clarity
- [ ] Customer team requirements are specified
- [ ] Customer time commitments are quantified (hours per week)
- [ ] Customer roles are appropriate for the project
- [ ] Executive sponsorship is included

**Red Flags:**

- Vague role descriptions
- Unrealistic customer time commitments
- Missing key customer roles (e.g., IT resources, SMEs)
- No mention of executive sponsorship
- Unclear who makes decisions
- No project liaison identified

**Questions to Ask:**

- Are customer time expectations realistic?
- Are all necessary customer roles identified?
- Is it clear who has decision-making authority?
- Are responsibilities well-distributed?

### 5. Pricing Review

**Check for:**

- [ ] Total project cost is clearly stated and prominent
- [ ] Cost breakdown is provided (if applicable)
- [ ] What's included in pricing is specified
- [ ] Payment milestones table is present
- [ ] Milestone deliverables are clearly defined
- [ ] Payment percentages/amounts total correctly (100%)
- [ ] Currency is specified
- [ ] Tax treatment is stated
- [ ] Validity period is included (typically 30 days)
- [ ] Purchase order requirements are noted
- [ ] Billing terms are clear (monthly, milestone-based)
- [ ] Late payment interest rates are specified
- [ ] Payment prerequisites are stated

**Red Flags:**

- Missing total cost
- Payment milestones don't add to 100%
- Vague milestone requirements
- No validity period
- Missing pricing notes
- Unclear what's included vs. additional costs
- No mention of expenses or travel costs if applicable

**Questions to Ask:**

- Is the pricing competitive and justified?
- Are milestone requirements objectively measurable?
- Are there hidden costs not addressed?
- Is the payment schedule fair to both parties?

### 6. Assumptions and Clarifications Review

**Check for:**

- [ ] Architecture and infrastructure assumptions are explicit
- [ ] Customer availability expectations are stated
- [ ] Access requirements are specified
- [ ] Customer responsibilities are clearly listed
- [ ] Technical assumptions are documented
- [ ] Scope boundaries are clarified (manual vs. automated, current vs. future)
- [ ] Change management process is referenced (ECP process)
- [ ] Agreement references (MSA, T&C) are included
- [ ] All assumptions from scope are restated explicitly

**Red Flags:**

- Generic or boilerplate assumptions
- Missing critical technical assumptions
- No mention of customer responsibilities
- Vague access or availability requirements
- No clarification on manual vs. automated processes
- Missing change management process

**Questions to Ask:**

- Are there any implicit assumptions not stated?
- Could the customer reasonably assume something different?
- Are all technical dependencies captured?
- What could go wrong if these assumptions are incorrect?
- Are customer obligations enforceable and realistic?

**CRITICAL - Uncalled Assumptions:**

- **Identify and highlight any assumptions made in the proposal that are NOT documented in the Assumptions section**
- Look for implied assumptions in Scope (e.g., "system will integrate" without stating assumed API availability)
- Check Schedule for unstated assumptions (e.g., customer availability, infrastructure readiness)
- Review Team section for implied customer resource assumptions
- Examine technical descriptions for assumed capabilities or conditions
- Flag any "we will" statements that depend on unstated preconditions

### 7. Terms and Conditions Review

**NOTE**: This Terms and Conditions section is only required if there is no mention of an existing Master Services Agreement (MSA) in the proposal. One of the two must be present - either a full Terms and Conditions section OR a reference to an existing MSA with the customer.

**Check for:**

- [ ] Site Access terms are included (or MSA reference exists)
- [ ] Customer Role and Responsibilities are defined (or MSA reference exists)
- [ ] Warranty and Project Performance terms are present (or MSA reference exists)
- [ ] Warranty period is specified (or MSA reference exists)
- [ ] Ownership and Use of Intellectual Property is addressed (or MSA reference exists)
- [ ] Indemnities and Limitation of Liability are included (or MSA reference exists)
- [ ] Liability caps are stated (or MSA reference exists)
- [ ] Confidentiality terms are present (or MSA reference exists)
- [ ] Changes to Scope of Project section with T&M rates is included (or MSA reference exists)
- [ ] T&M rates table is complete and current (or MSA reference exists)
- [ ] Governing Law & Dispute Resolution is specified (or MSA reference exists)
- [ ] Standard rates are valid for one year with inflation clause (or MSA reference exists)
- [ ] If no full T&C section exists, verify that an existing MSA is explicitly referenced

**Red Flags:**

- Missing both T&C section AND MSA reference
- Missing any standard T&C sections (when full T&C is provided)
- Outdated rates
- No liability caps (when full T&C is provided)
- Missing warranty terms (when full T&C is provided)
- Incomplete T&M rates table (when full T&C is provided)
- Vague MSA reference (e.g., "per existing agreement" without specifying which MSA)

**Questions to Ask:**

- Is there either a full T&C section or an explicit MSA reference?
- Are T&Cs consistent with any existing customer agreements?
- Are rates current and competitive?
- Is the warranty period appropriate?
- Are there any customer-specific legal requirements?

## Cross-Cutting Review Criteria

### Clarity and Precision

**Check for:**

- [ ] No vague quantifiers used
- [ ] Specific numbers provided for all estimates
- [ ] Technical terms are defined or commonly understood
- [ ] Consistent terminology throughout
- [ ] Active voice used for actions and deliverables
- [ ] No phrases with multiple interpretations

**Common Vague Terms to Eliminate:**

- "Approximately" → Replace with specific ranges or numbers
- "Various" → List specific items
- "Several" → Specify exact quantity
- "Some" → Define how many
- "About" → Provide exact numbers
- "Should/Could/Might" → Use "will" or clarify conditions

### Completeness

**Check for:**

- [ ] All mandatory sections have substantive content (not just placeholders)
- [ ] No `[AI-INSTRUCTION: ...]` or placeholder text remaining
- [ ] No `[TO BE ASSIGNED]` or `[TBD]` items
- [ ] All tables are complete with actual data
- [ ] Cross-references between sections are accurate
- [ ] Contact information is complete
- [ ] Version number is appropriate

### Ambiguity Elimination

**Check for:**

- [ ] Scope boundaries are explicit (both in-scope AND out-of-scope)
- [ ] No statements that could be interpreted multiple ways
- [ ] Success criteria are measurable and objective
- [ ] Dependencies are clearly identified
- [ ] All edge cases are addressed

**Test Each Statement:**

- Could this be understood differently by different people?
- Is there only one way to interpret this?
- Can this be objectively verified?

**CRITICAL - Flag Misinterpretation Risks:**

- **Highlight any content that could be misinterpreted or misleading**
- Look for statements with implicit meanings that differ from literal meanings
- Identify phrases where customer expectations might differ from intended delivery
- Flag technical jargon that could be misunderstood by non-technical stakeholders
- Note any statements that make promises beyond what's explicitly scoped

### Risk Management

**Check for:**

- [ ] Technical risks are identified
- [ ] Schedule risks are addressed
- [ ] Budget contingencies are appropriate
- [ ] Client dependencies are highlighted
- [ ] Mitigation strategies are actionable
- [ ] Assumptions that could fail are called out

**Common Risks to Consider:**

- Integration complexity
- Customer availability delays
- Technical feasibility
- Third-party dependencies
- Infrastructure readiness
- Scope creep potential

### Professional Quality

**Check for:**

- [ ] Grammar and spelling are correct
- [ ] Formatting is consistent
- [ ] Tables are properly formatted and aligned
- [ ] Bullet points are parallel in structure
- [ ] Numbering is consistent
- [ ] Document flows logically
- [ ] Visual hierarchy is clear
- [ ] No orphaned headings

### Client Perspective

**Check for:**

- [ ] Business value is clearly articulated
- [ ] Technical complexity is appropriate for audience
- [ ] Concerns are proactively addressed
- [ ] Next steps are obvious
- [ ] Tone is professional and confident
- [ ] Customer name is used consistently (not placeholders)
- [ ] Proposal speaks to customer's needs and context

## Review Output Format

**CRITICAL INSTRUCTIONS:**

- **DO NOT edit or modify the proposal file itself**
- **ONLY create a review report if issues are found**
- If issues are found, create a new markdown file named `REVIEW_REPORT.md` in the same folder as the proposal
- If the proposal has no issues and all mandatory sections are complete, simply confirm that the proposal is ready for submission - **DO NOT create a review report file**

Structure your review findings in the `REVIEW_REPORT.md` file using the following format:

```markdown
## Proposal Review Summary

**Proposal:** [Proposal Name]
**Customer:** [Customer Name]
**Review Date:** [Date]
**Overall Status:** [Ready for Submission / Needs Minor Revisions / Needs Major Revisions / Incomplete]
**Mandatory Sections Status:** [All Present ✓ / Missing: [list missing sections]]

### Executive Summary

[2-3 sentences summarizing the overall quality and readiness of the proposal]
[If no issues found: "This proposal is well-structured, complete, and ready for submission. All mandatory sections are present and there are no identified issues or concerns."]

### Mandatory Sections Verification

- [✓/✗] Introduction
- [✓/✗] Scope
- [✓/✗] Schedule and Workplan
- [✓/✗] Team
- [✓/✗] Pricing
- [✓/✗] Assumptions and Clarifications
- [✓/✗] Terms and Conditions

### Critical Issues (Must Fix)

[Numbered list of issues that must be addressed before submission]
[If none: "No critical issues identified."]

1. **[Issue Category]**: [Description]
   - **Location:** [Section name]
   - **Problem:** [What's wrong]
   - **Recommendation:** [Specific fix]

### Misinterpretation & Misleading Content

[Specific instances where content could be misinterpreted or is misleading]
[If none: "No potential misinterpretations identified."]

### Uncalled Assumptions

[List assumptions that appear in the proposal but are not documented in the Assumptions section]
[If none: "All assumptions are properly documented."]

### Recommendations for Improvement (Should Fix)

[Numbered list of improvements that would strengthen the proposal]
[If none: "No significant improvements needed."]

1. **[Issue Category]**: [Description]
   - **Location:** [Section name]
   - **Current State:** [What it says now]
   - **Suggested Improvement:** [How to improve]

### Minor Suggestions (Nice to Have)

[Bullet list of minor polish items]
[If none: "No minor suggestions."]

### Section-by-Section Findings

#### Introduction

- [Specific findings]

#### Scope

- [Specific findings]

#### Schedule and Workplan

- [Specific findings]

#### Team

- [Specific findings]

#### Pricing

- [Specific findings]

#### Assumptions and Clarifications

- [Specific findings]

#### Terms and Conditions

- [Specific findings]

### Checklist Results

**Clarity and Precision:** [✓ Pass / ⚠ Needs Work / ✗ Fail]
**Completeness:** [✓ Pass / ⚠ Needs Work / ✗ Fail]
**Ambiguity Elimination:** [✓ Pass / ⚠ Needs Work / ✗ Fail]
**Risk Management:** [✓ Pass / ⚠ Needs Work / ✗ Fail]
**Professional Quality:** [✓ Pass / ⚠ Needs Work / ✗ Fail]
**Client Perspective:** [✓ Pass / ⚠ Needs Work / ✗ Fail]

### Next Steps

[Clear action items for proposal author]
[If no issues: "No revisions required. Proposal is ready for submission."]
```

## Review Best Practices

### Be Specific and Actionable

- Don't just say "improve clarity" - specify exactly what needs to change
- Provide suggested text when appropriate
- Reference specific lines or sections
- Explain why something is problematic

### Prioritize Issues

- **Critical Issues:** Things that could cause legal/financial problems or major misunderstandings
- **Important Improvements:** Things that significantly impact quality or clarity
- **Minor Suggestions:** Polish and optimization items

### Consider the Audience

- Is technical detail appropriate for the customer's sophistication?
- Does the proposal address their specific concerns?
- Is the tone right for the relationship?

### Validate Against Reality

- Are timelines realistic for the scope?
- Is pricing competitive and justified?
- Are resource allocations feasible?
- Can Brock actually deliver what's promised?

### Check for Consistency

- Same terminology used throughout?
- Numbers add up correctly?
- Cross-references are accurate?
- Dates and timelines align?

### Think Like a Customer

- What questions would you have?
- What could you misunderstand?
- What's missing that you'd want to know?
- What could cause disputes later?

## Common Patterns to Flag

### Scope Creep Risks

- "And related tasks"
- "As needed"
- "Support as required"
- "Reasonable assistance"
- Undefined "coordination" or "collaboration"

### Timeline Red Flags

- No contingency time
- Back-to-back critical path items
- Unrealistic customer turnaround expectations
- Missing key phases (testing, training)

### Pricing Issues

- No breakdown for complex projects
- Unclear what's included
- Missing expense handling
- Payment schedule too aggressive or too lenient

### Assumption Gaps

- "Customer will provide necessary access" (What access? When?)
- "System meets requirements" (What requirements? How verified?)
- "Standard configuration" (What's standard?)

## Success Criteria

A complete proposal review includes:

- All seven mandatory sections evaluated
- Critical issues clearly identified with specific recommendations
- Cross-cutting concerns (clarity, completeness, ambiguity) assessed
- Prioritized findings (critical vs. nice-to-have)
- Specific, actionable recommendations for improvement
- Assessment of overall readiness for submission
- Clear next steps for proposal author
- **A `REVIEW_REPORT.md` file created in the proposal folder ONLY if issues are found**
- **No modifications made to the original proposal file**

## Important Reminders

- **Be thorough but constructive** - the goal is to improve, not criticize
- **Think about risk** - what could go wrong if this proposal is accepted as-is?
- **Consider the customer relationship** - does this proposal strengthen trust?
- **Verify against standards** - use the checklist systematically
- **Look for patterns** - similar issues across sections suggest systematic problems
- **Provide examples** - show what good looks like when recommending changes
