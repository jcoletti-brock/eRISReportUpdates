---
description: "Convert BIRT .rptdesign reports from iFIX tag paths to Ignition tag paths"
---

Your goal is to convert BIRT report files (.rptdesign) from iFIX tag path references to Ignition tag path references using a CSV lookup table. You will validate XML structure, extract tags, match them against a lookup file, and perform the conversion only after user confirmation.

## Report Conversion Workflow

Follow these instructions when converting BIRT reports from iFIX to Ignition:

**IMPORTANT:** Before starting, review the `Required Tools and Approaches` section below to understand which specific tools and methods must be used for each step.

1. Accept one or more .rptdesign file paths from the `eris\input\reports` directory
2. Validate each file as valid XML
   - Reference the `Required Tools and Approaches` section for specific validation tools
   - Reference the `XML Validation` section below for more details
3. Extract all iFIX tag paths from the XML
   - Reference the `Required Tools and Approaches` section for extraction tools
   - Reference the `iFIX Tag Path Extraction` section below for more details
4. Match extracted tags against the CSV lookup file
   - Reference the `Required Tools and Approaches` section for CSV processing tools
   - Reference the `Tag Lookup Matching` section below for more details
5. If mismatches are found, generate a mismatch summary document
   - Reference the `Mismatch Summary Generation` section below for more details
6. Report findings and request user confirmation (only if all tags matched)
   - Reference the `User Confirmation` section below for more details
7. If user confirms, perform the conversion
   - Reference the `Required Tools and Approaches` section for file conversion tools
   - Reference the `Report Conversion` section below for more details
8. Generate a conversion summary document
   - Reference the `Summary Generation` section below for more details

## Required Tools and Approaches

To ensure consistent execution across conversion runs:

### Python Code Execution
**PREFERRED:** Use `mcp_pylance_mcp_s_pylanceRunCodeSnippet` tool for all Python operations
- Eliminates shell quoting/escaping issues (especially critical on Windows)
- Handles file paths automatically (forward slashes work seamlessly)
- Supports clean multi-line Python code execution
- Provides proper exit codes and formatted output

**FALLBACK:** If Pylance MCP tool unavailable, use terminal: `python -c` one-liners
- Requires careful path escaping on Windows (use forward slashes: `c:/path/to/file`)
- May encounter issues with complex string quoting

### XML Validation
- Use Python's `xml.etree.ElementTree.parse()` method
- Execute using preferred Python tool (Pylance MCP or terminal)
- Report any parsing exceptions as validation failures

### iFIX Tag Extraction
- Use Python's `re` module
- Pattern: `r'WATH\.[\w\.]+:'` (matches WATH. prefix, word/dot characters, trailing colon)
- Use `re.findall()` on full file content
- Process results to remove `WATH.` prefix and trailing `:` for lookup matching

### CSV Lookup Processing
- Use Python's `csv.DictReader`
- Encoding: `utf-8-sig` (handles UTF-8 with or without BOM)
- Build lookup dictionary keyed by `hist_tagname` column
- Perform exact case-sensitive matching

### File Conversion
- **PREFERRED:** Use Python string replacement with file I/O (simpler, more reliable)
- **ALTERNATIVE:** Use VS Code's `multi_replace_string_in_file` tool for batch replacements
  - Include sufficient context (3-5 lines) in oldString for unambiguous matching
  - Verify replacement counts match expected instances

### Conversion Verification
- **Verify iFIX tag removal:** Use pattern `r'WATH\.[^:]+:'` to count remaining WATH tags (should be 0)
- **Verify Ignition tag presence:** Use pattern `r'IGNW\.[^:]+:'` to count IGNW tags (should equal total instances)
- **CRITICAL:** Use `[^:]+` (match any character except colon) instead of `[\w\-\.]+` to avoid undercounting
- The broad pattern ensures all valid tag characters are captured, including underscores, dots, and dashes
- Compare IGNW count against expected total instances from extraction phase

## XML Validation

Before processing any report file:

- Use appropriate tools to verify each .rptdesign file is valid XML
- If any file fails validation, report the error to the user with file name and error details
- **CRITICAL:** Do not proceed with invalid XML files - stop processing and inform the user

## iFIX Tag Path Extraction

Search the entire XML document for iFIX tag paths:

- iFIX tag paths are identified by the prefix `WATH.` and end with a colon `:`
- Pattern to search: `WATH.*:`
- These tags are typically found within `<queryText>` XML elements, but **search the entire XML file**
- Extract all unique iFIX tag paths found in each report
- For each tag, remove the `WATH.` prefix to get the base tag name for lookup
- Remove the trailing colon `:` as well
- Present a summary showing:
  - Report file name
  - Total count of iFIX tag instances found
  - List of unique iFIX tags (without WATH. prefix and trailing colon)
- **CRITICAL:** If no instances of iFIX tags are found in a report, report this to the user and skip conversion. Create a summary file indicating zero tags found and conversion skipped for that report.

## Tag Lookup Matching

Use the CSV lookup file located at `src\ifix_to_ign_010152026.csv`:

- The CSV has the following columns: `hist_tagname`, `ign_tagprovider`, `ign_tagname`, `ign_fullpath`, `imaginary`
- For each extracted iFIX tag (with WATH. prefix and trailing colon removed):
  - Search for a match in the `hist_tagname` column
  - The match should be exact (case-sensitive)
  - If found, retrieve the corresponding `ign_tagname` value
- **CRITICAL STOPPING CONDITION:** If any iFIX tag cannot be found in the lookup:
  - Report all unmatched tags to the user
  - List the report file name and the specific tags that have no match
  - Generate a mismatch summary file in the `eris\output\mismatches` directory (see `Mismatch Summary Generation` section)
  - **STOP ALL PROCESSING** - do not proceed with any conversion
  - Inform the user that the lookup table needs to be updated before conversion can proceed

## Mismatch Summary Generation

When iFIX tags cannot be found in the lookup table, create a mismatch summary file:

1. **Create mismatch summary markdown file:**
   - Location: `eris\output\mismatches` directory
   - Filename: Same base name as the report file with `.md` extension
   - Example: For `Daily Flow Check - Rural v6G.rptdesign`, create `Daily Flow Check - Rural v6G.md`

2. **Mismatch summary content structure:**
   
   The mismatch summary file MUST follow this exact format:

   ```markdown
   # Report Conversion Mismatch Summary: [Report Filename]
   
   **Analysis Date:** [Month Day, Year HH:MM AM/PM]
   **Original File:** `eris\input\reports\[filename]`
   **Status:** ✗ Conversion Not Possible - Missing Lookup Entries
   
   ## Tag Analysis Statistics
   
   - Total unique iFIX tags found: [count]
   - Tags matched in lookup: [count]
   - Tags NOT matched in lookup: [count]
   - Match rate: [percentage]%
   
   ## Tags NOT Found in Lookup
   
   The following iFIX tags were found in the report but do NOT have entries in the lookup table:
   
   | iFIX Tag (without WATH. prefix) | Full Tag Path in Report | Instances Found |
   |--------------------------------|------------------------|----------------|
   | [tag_name] | WATH.[tag_name]: | [count] |
   
   ## Tags Successfully Matched
   
   The following iFIX tags were found in both the report and the lookup table:
   
   | iFIX Tag Path | Ignition Tag Name (Lookup) | Instances Found |
   |---------------|----------------------------|----------------|
   | WATH.[tag]: | [ign_tagname] | [count] |
   
   ## Required Action
   
   **The lookup table at `src\ifix_to_ign_010152026.csv` must be updated with the missing iFIX tag entries before this report can be converted.**
   
   Add entries to the lookup table for all tags listed in the "Tags NOT Found in Lookup" section above. Each entry should include:
   - `hist_tagname`: The iFIX tag name (without WATH. prefix)
   - `ign_tagprovider`: The Ignition tag provider
   - `ign_tagname`: The corresponding Ignition tag path
   - `ign_fullpath`: The full Ignition tag path
   - `imaginary`: Whether the tag is imaginary (true/false)
   
   After updating the lookup table, re-run the conversion process for this report.
   ```

   **Formatting Requirements:**
   - Date format: Use full month name, day, year, and 12-hour time with AM/PM (e.g., "February 13, 2026 09:07 AM")
   - Tables: Include all tag information with instance counts
   - Use ✗ symbol for failure indicators
   - Clearly separate unmatched tags from matched tags
   - Include match rate percentage calculation

3. **User notification:**
   - Inform the user that a mismatch summary file has been created
   - Provide the path to the mismatch summary file
   - Remind user that the lookup table must be updated before conversion can proceed

## User Confirmation

If all iFIX tags are successfully matched in the lookup:

- Inform the user: "All [X] unique iFIX tag(s) found across [Y] report file(s) have matching Ignition equivalents in the lookup table."
- Display a summary table showing:
  - Original iFIX tag path (with WATH. prefix)
  - Corresponding Ignition tag name from lookup (raw from ign_tagname column)
  - Formatted Ignition tag path that will be used (with IGNW. prefix and / replaced with -)
- Ask the user: "Do you want to proceed with converting the report file(s)?"
- Use the `ask_questions` tool to get user confirmation
- Only proceed if user explicitly confirms
- If user declines, stop processing and acknowledge their decision

## Report Conversion

When user confirms conversion, process each report file:

1. **Create output copy:**
   - Create a copy of the original .rptdesign file in the `eris\output\reports` directory
   - Use the same filename as the original
   - If file already exists in output directory, overwrite it

2. **Transform Ignition tag paths:**
   - For each matched tag, take the `ign_tagname` value from the lookup
   - Apply the following transformation:
     - Add prefix `IGNW.`
     - Replace all forward slash characters `/` with dashes `-`
   - Example: If `ign_tagname` is `Plant/Pumps/P101/FlowRate`, transform to `IGNW.Plant-Pumps-P101-FlowRate`

3. **Replace tag paths in XML:**
   - In the output copy, find all instances of the original iFIX tag path (including WATH. prefix and trailing colon)
   - Replace with the transformed Ignition tag path (including IGNW. prefix and trailing colon)
   - Example: Replace `WATH.P101_FLOW:` with `IGNW.Plant-Pumps-P101-FlowRate:`
   - Ensure all instances are replaced throughout the entire XML document

4. **Verify replacement:**
   - Reference the `Conversion Verification` subsection in `Required Tools and Approaches` for proper validation methods
   - Count remaining WATH tags using pattern `r'WATH\.[^:]+:'` - must equal 0
   - Count IGNW tags using pattern `r'IGNW\.[^:]+:'` - must equal total instances from extraction
   - **CRITICAL:** Do not use restrictive patterns like `[\w\-]` that may miss valid characters
   - Report verification results showing: WATH remaining (expected: 0), IGNW found (expected: total instances)
   - If counts don't match expectations, investigate and report detailed warning to user

## Summary Generation

After completing conversion for each report file:

1. **Create summary markdown file:**
   - Location: `eris\output\conversion_summary` directory
   - Filename: Same base name as the report file with `.md` extension
   - Example: For `Daily Flow Check - Rural v6G.rptdesign`, create `Daily Flow Check - Rural v6G.md`

2. **Summary content structure:**
   
   The summary file MUST follow this exact format:

   ```markdown
   # Report Conversion Summary: [Report Filename]
   
   **Conversion Date:** [Month Day, Year HH:MM AM/PM]
   **Original File:** `eris\input\reports\[filename]`
   **Converted File:** `eris\output\reports\[filename]`
   
   ## Conversion Statistics
   
   - Total unique iFIX tags found: [count]
   - Total tag instances replaced: [count]
   - All tags successfully matched: ✓
   
   ## Tag Mappings
   
   | iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
   |---------------|----------------------------|----------------------------|-------------------|
   | WATH.[tag]: | [ign_tagname] | IGNW.[formatted]: | [count] |
   
   ## Conversion Details
   
   Successfully converted all [total instances] instances of [unique count] unique iFIX tag paths to their Ignition equivalents.
   
   **Verification:**
   - WATH tags remaining in output file: [count, should be 0]
   - IGNW tags in output file: [count, should match total instances]
   - Conversion status: ✓ Complete
   
   **Tag Format Transformation:**
   - iFIX format: `WATH.[server].[tag_path]:` 
   - Ignition format: `IGNW.[formatted_path]:` (forward slashes replaced with dashes)
   
   All tag paths were successfully validated against the lookup table and converted according to the specified transformation rules.
   ```

   **Formatting Requirements:**
   - Date format: Use full month name, day, year, and 12-hour time with AM/PM (e.g., "February 13, 2026 09:07 AM")
   - Table: Include all tag mappings with instance counts
   - Conversion Details: Must include the three subsections (opening summary, Verification, Tag Format Transformation) followed by closing statement
   - Use checkmark symbol: ✓ for completion indicators

3. **Final user notification:**
   - Inform the user that conversion is complete
   - Provide the paths to the converted report file(s) and summary file(s)
   - Confirm total number of files processed successfully
