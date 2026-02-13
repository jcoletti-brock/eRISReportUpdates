---
agent: SQLDeveloper
description: "Review a T-SQL code review file and make the necessary corrections as prescribed by the documented coding standards."
---

Your goal is to fix the issues identified in the provided SQL Code Review Report.

## Fixing Instructions

Follow these steps when working through fixing sql code issues:

- Evaluate the Review Details section of the report to identify all issues categorized by severity (Critical, Major, Moderate, Minor).
- For each issue, refer to the Standards Reference provided to understand the specific coding standard that was violated.
- Modify the original T-SQL code to address each violation, ensuring compliance with the referenced coding standards.
- After making all necessary changes, re-evaluate the given review document to ensure that all noted issues have been addressed.

## Issues That Can't Be Resolved

If you encounter any issues that cannot be resolved due to missing context or dependencies (e.g., missing database names, unclear logic), document these challenges clearly.

Create a file named `<original_filename>_unresolved.md` and include:

- summary line from the review report
- specifics as to why you could not resolve the issue.

## NOTES

- **IMPORTANT**: For this task explicitly, it is not your responsibility to evaluate the overall standard compliance of the T-SQL code. Your sole focus should be on addressing and fixing the issues that have already been identified in the review report.
