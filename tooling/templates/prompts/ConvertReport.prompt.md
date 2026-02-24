---
description: "Convert BIRT .rptdesign reports from iFIX tag paths to Ignition tag paths"
---

Your goal is to convert BIRT report files (.rptdesign) from iFIX tag path references to Ignition tag path references using a CSV lookup table. You will validate XML structure, extract tags, match them against a lookup file, and perform the conversion only after user confirmation.

## Report Conversion Workflow

Follow these instructions when converting BIRT reports from iFIX to Ignition:

**IMPORTANT:** Before starting, review the `Required Tools and Approaches` section below to understand which specific tools and methods must be used for each step.

1. Accept one or more .rptdesign file paths from the `eris\input\reports` directory
   - **If the user does not provide a specific report name or there is any uncertainty about which report to convert:**
     - Use `list_dir` tool to list all .rptdesign files in the `eris\input\reports` directory
     - Present the list of available reports to the user
     - Use the `ask_questions` tool to ask the user to select which report(s) to convert
     - Provide the list of report filenames as selectable options
     - Only proceed with the selected report(s)
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
- **CRITICAL:** Check BOTH tag formats - tags may appear in JSON format OR XML queryText URLs:
  - **JSON format pattern:** `r'"tag"\s*:\s*"(WATH\.[A-Z0-9_.]+)"'` (captures WATH tag within JSON property value)
  - **XML queryText URL pattern:** `r'Tag[0-9.]+:(WATH\.[A-Z0-9_.]+):'` (captures WATH tag within URL query parameters)
- Use `re.findall()` on full file content with BOTH patterns
- Combine results from both patterns (use set union to avoid duplicates when counting unique tags)
- **CRITICAL:** Count TOTAL instances (sum of both pattern matches) - this is your baseline for verification
- Store both unique tags and total instance count
- Process results to remove `WATH.` prefix for lookup matching

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
- **Verify iFIX tag removal:** Check BOTH formats using extraction patterns:
  - JSON format: `r'"tag"\s*:\s*"WATH\.[A-Z0-9_.]+"'`
  - XML queryText: `r'Tag[0-9.]+:(WATH\.[A-Z0-9_.]+):'`
  - Sum of both pattern matches must equal 0
- **Verify Ignition tag presence:** Check BOTH formats:
  - JSON format: `r'"tag"\s*:\s*"IGNW\.[^"]+"'`
  - XML queryText: `r'Tag[0-9.]+:(IGNW\.[^:]+):'`
  - Sum of both pattern matches must equal total instances from extraction
- **CRITICAL PATTERN DIFFERENCE:**
  - JSON patterns match within `"tag"` property values
  - XML patterns match within URL query parameters `Tag[number]:[tagpath]:`
  - WATH uses uppercase alphanumeric pattern `[A-Z0-9_.]` to match the actual tag format
  - IGNW uses broad pattern `[^"]` or `[^:]` because transformed paths are lowercase with dashes, etc.
- **CRITICAL VALIDATION:** Total IGNW count MUST EXACTLY EQUAL the total WATH instance count from extraction
  - If 30 unique tags with 90 total instances were found, verify exactly 90 IGNW tags exist after conversion
  - If counts don't match, conversion is incomplete - investigate and report detailed error
- Compare IGNW count against the pre-conversion total instance count (not unique count)

## XML Validation

Before processing any report file:

- Use appropriate tools to verify each .rptdesign file is valid XML
- If any file fails validation, report the error to the user with file name and error details
- **CRITICAL:** Do not proceed with invalid XML files - stop processing and inform the user

## iFIX Tag Path Extraction

Search the entire XML document for iFIX tag paths in ALL possible formats:

- iFIX tag paths are identified by the prefix `WATH.` and appear in TWO possible formats:
  1. **JSON format:** Within JSON `"tag"` properties (e.g., `"tag" : "WATH.MTPSVR1.TAG"`) 
  2. **XML queryText URL format:** Within URL query parameters (e.g., `Tag1.0:WATH.MTPSVR1.TAG:esrMaxGap`)
- **IMPORTANT - Exclude calculated/derived tags:**
  - Calculated tags have prefixes before WATH (e.g., `ET.WATH.`, `MDPH.WATH.`, etc.)
  - These represent system-generated or derived values and should NOT be extracted or converted
  - Only extract pure `WATH.` data tags (those starting with WATH. directly, with no prefix)
  - Use negative lookbehind in patterns to exclude prefixed tags
- **Extraction patterns - MUST use BOTH:**
  - JSON pattern: `r'"tag"\s*:\s*"(WATH\.[A-Z0-9_.]+)"'` (captures WATH tag within JSON property value - will not match if preceded by other text)
  - XML queryText pattern: `r'Tag[0-9.]+:(WATH\.[A-Z0-9_.]+):'` (captures WATH tag within URL query parameters - by design, only matches tags directly after colon, excluding prefixed variants like ET.WATH.)
- **Search the entire XML file** with both patterns - tags may appear in either or both formats
- **CRITICAL COUNTING REQUIREMENTS:**
  - Extract matches from BOTH patterns
  - Count TOTAL instances (sum of all occurrences from both patterns): This is your baseline - if you find 90 total instances, you must convert ALL 90
  - Count UNIQUE tags: Combine results from both patterns, remove duplicates
  - Store both counts separately - they serve different purposes
- For each unique tag, remove the `WATH.` prefix to get the base tag name for lookup
- Present a summary showing:
  - Report file name
  - **Total count of iFIX tag instances found** (e.g., "90 total instances from JSON + queryText")
  - **Count of unique iFIX tags** (e.g., "30 unique tags")
  - List of unique iFIX tags (without WATH. prefix)
  - Per-tag instance counts (e.g., "WATH.TAG1 appears 5 times (3 in JSON, 2 in queryText)")
- **CRITICAL:** If no instances of data iFIX tags (pure WATH. format) are found in a report using EITHER pattern, report this to the user and skip conversion. Create a summary file indicating zero tags found and conversion skipped for that report.
- **Note on calculated tags:** If only prefixed tags like ET.WATH. are found with no matching data tags, this is normal and the report should be skipped (no conversion needed). Inform the user if this is the case.

## Tag Lookup Matching

Use the CSV lookup file located at `src\ifix_to_ign_2026_02_19.csv`:

- The CSV has the following columns: `hist_tagname`, `ign_tagprovider`, `ign_tagname`, `ign_fullpath`, `imaginary`
- For each extracted iFIX tag (with WATH. prefix and trailing colon removed):
  - Search for a match in the `hist_tagname` column
  - The match should be exact (case-sensitive)
  - If found, retrieve the corresponding `ign_tagname` value
- **CRITICAL STOPPING CONDITION:** If any iFIX tag cannot be found in the lookup:
  - Report all unmatched tags to the user
  - List the report file name and the specific tags that have no match
  - Generate a mismatch summary file in the `eris\output\reports\mismatches` directory (see `Mismatch Summary Generation` section)
  - **STOP ALL PROCESSING** - do not proceed with any conversion
  - Inform the user that the lookup table needs to be updated before conversion can proceed

## Mismatch Summary Generation

When iFIX tags cannot be found in the lookup table, create a mismatch summary file:

1. **Create mismatch summary markdown file:**
   - Location: `eris\output\reports\mismatches` directory
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
   | [tag_name] | WATH.[tag_name] | [count] |
   
   ## Tags Successfully Matched
   
   The following iFIX tags were found in both the report and the lookup table:
   
   | iFIX Tag Path | Ignition Tag Name (Lookup) | Instances Found |
   |---------------|----------------------------|----------------|
   | WATH.[tag] | [ign_tagname] | [count] |
   
   ## Required Action
   
   **The lookup table at `src\ifix_to_ign_2026_02_19.csv` must be updated with the missing iFIX tag entries before this report can be converted.**
   
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
   - Create a copy of the original .rptdesign file in the `eris\output\reports\completed` directory
   - Use the same filename as the original
   - If file already exists in output directory, overwrite it

2. **Transform Ignition tag paths:**
   - For each matched tag, take the `ign_tagname` value from the lookup
   - Apply the following transformation:
     - Add prefix `IGNW.`
     - Replace all forward slash characters `/` with dashes `-`
     - Replace all space characters with underscores `_`
     - Convert entire path (except prefix) to lowercase
   - Example: If `ign_tagname` is `Plant/Pumps/P101/Flow Rate`, transform to `IGNW.plant-pumps-p101-flow_rate`

3. **Pre-conversion instance count:**
   - Before making ANY changes, count total instances of each iFIX tag path in the original file
   - Store these counts for post-conversion verification
   - This ensures you know EXACTLY how many replacements should occur

4. **Replace tag paths in XML:**
   - In the output copy, find all instances of the original iFIX tag path in BOTH formats:
     - **JSON format:** Within `"tag"` property values (e.g., `"tag" : "WATH.MTPSVR2.P101_FLOW"`)
     - **XML queryText format:** Within URL query parameters (e.g., `Tag1.0:WATH.MTPSVR2.P101_FLOW:esrMaxGap`)
   - Replace `WATH.[tag_path]` with the transformed Ignition tag path `IGNW.[transformed_path]` in ALL occurrences
   - Examples:
     - JSON: Replace `"tag" : "WATH.MTPSVR2.P101_FLOW"` with `"tag" : "IGNW.plant-pumps-p101-flowrate"`
     - queryText: Replace `Tag1.0:WATH.MTPSVR2.P101_FLOW:esrMaxGap` with `Tag1.0:IGNW.plant-pumps-p101-flowrate:esrMaxGap`
   - Ensure all instances are replaced throughout the entire XML document
   - Use Python's `str.replace()` method which replaces ALL occurrences regardless of context (works for both formats)
   - **Additional string replacements:**
     - Replace all occurrences of `:lab:` with `:esrLab:` throughout the XML document
     - Use Python's `str.replace()` method: `content.replace(':lab:', ':esrLab:')`

5. **Verify replacement:**
   - Reference the `Conversion Verification` subsection in `Required Tools and Approaches` for proper validation methods
   - Count remaining WATH tags using BOTH extraction patterns - sum must equal 0:
     - JSON pattern: `r'"tag"\s*:\s*"WATH\.[A-Z0-9_.]+"'`
     - queryText pattern: `r'Tag[0-9.]+:(WATH\.[A-Z0-9_.]+):'`
   - Count IGNW tags using BOTH corresponding patterns - sum must equal total instances from extraction:
     - JSON pattern: `r'"tag"\s*:\s*"IGNW\.[^"]+"'`
     - queryText pattern: `r'Tag[0-9.]+:(IGNW\.[^:]+):'`
   - **CRITICAL VALIDATION:**
     - If extraction found 30 unique tags with 90 total instances (from both formats combined), post-conversion MUST show:
       - WATH remaining: 0 (sum of both patterns)
       - IGNW found: 90 (sum of both patterns, matching total instances)
     - Any deviation indicates incomplete conversion - FAIL the conversion and report error
   - Report verification results showing: WATH remaining (expected: 0), IGNW found (expected: [total instances])
   - If counts don't match expectations exactly, report detailed error and ask user to investigate

6. **CRITICAL SANITY CHECK - Data Tag Verification:**
   - **THIS CHECK IS MANDATORY AND MUST NOT BE SKIPPED**
   - After all replacements are complete, perform a final sanity check on the converted file
   - **Verify all DATA iFIX tags were converted (excluding calculated/derived tags):**
     - Search for pure `WATH.` data tags using pattern: `r'(?<!T\.)WATH\.[A-Z0-9_.]+'` (negative lookbehind to exclude ET.WATH.)
     - This should return 0 matches if all data tags were converted
   - **Verify calculated tags are preserved (expected behavior):**
     - Calculated tags with prefixes (ET.WATH., MDPH.WATH., etc.) should remain in the file unchanged
     - This is EXPECTED and CORRECT - no action needed
   - **CRITICAL REQUIREMENT:**
     - If pure `WATH.` data tags (without ET. or other prefixes) are found in the converted file, conversion has FAILED
     - Report exact count of unconverted data tags found
     - Report the first few unconverted tags for debugging
     - STOP processing immediately and inform user that manual investigation is required
     - DO NOT generate conversion summary or mark conversion as successful
   - **SUCCESS CRITERIA:**
     - Pure `WATH.` data tags MUST equal 0 (all converted)
     - Calculated tags with prefixes (ET.WATH., etc.) may be present and is expected
     - Only if this check passes can the conversion be considered complete
   - Report result: "Data tag sanity check: PASSED (0 unconverted WATH. data tags)" or "Data tag sanity check: FAILED - [count] unconverted data tags found"

## Summary Generation

After completing conversion for each report file:

1. **Create summary markdown file:**
   - Location: `eris\output\reports\conversion_summary` directory
   - Filename: Same base name as the report file with `.md` extension
   - Example: For `Daily Flow Check - Rural v6G.rptdesign`, create `Daily Flow Check - Rural v6G.md`

2. **Summary content structure:**
   
   The summary file MUST follow this exact format:

   ```markdown
   # Report Conversion Summary: [Report Filename]
   
   **Conversion Date:** [Month Day, Year HH:MM AM/PM]
   **Original File:** `eris\input\reports\[filename]`
   **Converted File:** `eris\output\reports\completed\[filename]`
   
   ## Conversion Statistics
   
   - Total unique iFIX tags found: [count]
   - Total tag instances replaced: [count]
   - All tags successfully matched: ✓
   
   ## Tag Mappings
   
   | iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
   |---------------|----------------------------|----------------------------|-------------------|
   | WATH.[tag] | [ign_tagname] | IGNW.[formatted_lowercase] | [count] |
   
   ## Conversion Details
   
   Successfully converted all [total instances] instances of [unique count] unique iFIX tag paths to their Ignition equivalents.
   
   **Verification:**
   - Data WATH tags remaining in output file: [count, should be 0]
   - IGNW tags in output file: [count, should match total instances]
   - Calculated tags (ET.WATH.*, etc.) preserved: [count] (expected, unchanged)
   - Data tag sanity check: ✓ PASSED (no unconverted WATH. data tags)
   - Conversion status: ✓ Complete
   
   **Tag Format Transformation:**
   - iFIX formats: 
     - JSON: `"tag" : "WATH.[server].[tag_path]"` 
     - XML queryText: `Tag[number]:WATH.[server].[tag_path]:[parameters]`
   - Ignition formats (IGNW prefix uppercase, path lowercase):
     - JSON: `"tag" : "IGNW.[formatted_path]"` (forward slashes replaced with dashes, spaces replaced with underscores, path lowercase)
     - XML queryText: `Tag[number]:IGNW.[formatted_path]:[parameters]` (forward slashes replaced with dashes, spaces replaced with underscores, path lowercase)
   
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
