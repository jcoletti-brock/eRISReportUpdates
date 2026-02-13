---
agent: SQLReviewer
description: "Review a T-SQL code file"
---

Your goal is to review the provided T-SQL code for adherence to the established coding standards and best practices. Your goal is to produce a review report that highlights any deviations from the established standards.

## Output Format Template

### Review Summary

The following markdown section will be added at the top of the review document

- Review Date: YYYY-MM-DD
- Filename:
- Section Violations: <csv list of section numbers in descending order>

| Severity | Count | Severity Description                                                  |
| -------- | ----- | --------------------------------------------------------------------- |
| Critical |       | Potential logical/functional error or severe performance anti-pattern |
| Major    |       | Clear standards violation affecting maintainability/performance.      |
| Moderate |       | Style/readability issue; easy fix; cumulative impact.                 |
| Minor    |       | Cosmetic; low impact; mention for completeness.                       |
| Total    |       |                                                                       |

### Review Details

The following markdown table will be provided detailing our line by line findings.
The meanings of each column are as follows:

- Severity: The severity level of the violation (Critical, Major, Moderate, Minor)
- Line: The line number where the violation occured
- Violation Snippet: A brief snippet of the code violation for context
- Standards Reference: A reference to the specific coding standard that was violated, including section number and description.

NOTE: Line Snippets should be wraped in backticks for code formatting.

| Severity | Line # | Line Snippet | Standards Reference |
| -------- | ------ | ------------ | ------------------- |
|          |        |              |                     |

## Review Workflow

- Parse the provided T-SQL Code, **LINE-BY-LINE**, following this process:

- Review each standards section sequentially against the line of code.
- Output the report file in markdown format, adhering to the Output Format Template above.
- Output file should be named `<original_filename>_review.md`
- Items should be ordered by severity (Critical, Major, Moderate, Minor) and then by line number within each severity level.

## NOTES

- Pay specific attention to standards section 3.1 regarding SQL keyword alignment and casing.
- Even though you are instructed elsewhere to do so, **DO NOT** provide a summary to the user in your final response.
