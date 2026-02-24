```prompt
---
description: "Convert tag calculations from iFIX tag paths to Ignition tag paths in CalcsConfigExport.json"
---

Your goal is to convert tag calculation configurations (CalcsConfigExport.json) from iFIX tag path references to Ignition tag path references using a CSV lookup table. You will validate JSON structure, extract tags from embedded MVEL code, match them against a lookup file, and perform the conversion only after user confirmation.

## Tag Calculation Conversion Workflow

Follow these instructions when converting calculation configurations from iFIX to Ignition:

**IMPORTANT:** Before starting, review the `Required Tools and Approaches` section below to understand which specific tools and methods must be used for each step.

1. Accept the CalcsConfigExport.json file path from the `eris\input\tagcalcs` directory
   - If the file is not explicitly provided, assume `eris\input\tagcalcs\CalcsConfigExport.json`
   - Verify the file exists before proceeding
   
2. Validate the file as valid JSON
   - Reference the `Required Tools and Approaches` section for specific validation tools
   - Reference the `JSON Validation` section below for more details

3. Extract all iFIX tag paths from embedded MVEL code
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
   - Reference the `Tag Calculation Conversion` section below for more details

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

### JSON Validation
- Use Python's `json.load()` method
- Execute using preferred Python tool (Pylance MCP or terminal)
- Report any parsing exceptions as validation failures

### iFIX Tag Extraction from MVEL Code
- Use Python's `re` module with careful pattern matching
- **CRITICAL:** Tags are embedded in MVEL code strings with JSON escaping (`\\r\\n`, `\\"`, etc.)
- **CRITICAL:** Must unescape JSON strings first before extracting tags
- **Extraction patterns - MUST use both:**
  - Pattern 1: `r'(?<![\w.])WATH\.((?:[A-Z0-9]+\.)*[A-Z0-9_]+(?:QVA|QFL|QRN)?(?:\.F_CV)?)'` (unescaped code)
  - This pattern captures WATH tags in code context but NOT in comments or strings within code
- **Search strategy:**
  - Iterate through each calculation item in the JSON array
  - Extract `code.value` field (contains MVEL code)
  - Unescape JSON escape sequences: `\\r\\n` → `\r\n`, `\\"` → `"`, etc.
  - Apply regex pattern to unescaped code
  - Collect all matches
- **CRITICAL COUNTING REQUIREMENTS:**
  - Count TOTAL instances: Sum of all occurrences in all calculations
  - Count UNIQUE tags: Combine results across all calculations, remove duplicates
  - Store both counts separately - they serve different purposes
- For each unique tag, remove the `WATH.` prefix to get the base tag name for lookup
- Present a summary showing:
  - Total count of iFIX tag instances found across all calculations
  - Count of unique iFIX tags
  - Per-calculation instance counts (e.g., "Calculation Name: 5 instances of 2 unique tags")
- **CRITICAL:** If no instances of iFIX tags are found, report this to the user and skip conversion.

### CSV Lookup Processing
- Use Python's `csv.DictReader`
- Encoding: `utf-8-sig` (handles UTF-8 with or without BOM)
- Build lookup dictionary keyed by `hist_tagname` column
- Perform exact case-sensitive matching

### File Conversion
- **PREFERRED:** Use Python with JSON library for parsing and manipulation
- Parse JSON, modify code strings, re-serialize to JSON
- Preserve JSON formatting and structure
- Handle JSON escaping properly when writing back

### Conversion Verification
- **Verify iFIX tag removal:** Search unescaped code with extraction pattern
  - Pattern: `r'(?<![\w.])WATH\.((?:[A-Z0-9]+\.)*[A-Z0-9_]+(?:QVA|QFL|QRN)?(?:\.F_CV)?)'`
  - Sum of matches across all calculations must equal 0
- **Verify Ignition tag presence:** Search for replaced tags
  - Pattern: `r'IGNW\.[a-z0-9_-]+(?:[.-]?[a-z0-9_-]+)*'`
  - Sum of matches must equal total instances from extraction
- **CRITICAL VALIDATION:**
  - If extraction found 45 total instances across calculations, post-conversion MUST show:
    - WATH remaining: 0 (sum across all calculations)
    - IGNW found: 45 (sum across all calculations)
  - Any deviation indicates incomplete conversion - FAIL the conversion and report error
- Report verification results showing: WATH remaining (expected: 0), IGNW found (expected: [total instances])

## JSON Validation

Before processing the calculation file:

- Use appropriate tools to verify the CalcsConfigExport.json file is valid JSON
- If validation fails, report the error to the user with file name and error details
- **CRITICAL:** Do not proceed with invalid JSON files - stop processing and inform the user

## iFIX Tag Path Extraction

Search the entire JSON document for iFIX tag paths in MVEL code:

- iFIX tag paths are identified by the prefix `WATH.` and appear within MVEL code strings
- Tags appear in calculation input descriptors and code blocks
- **IMPORTANT - Handle JSON escaping:**
  - Raw JSON contains: `"value" : "...WATH.TAG...\\r\\n..."`
  - Must unescape to: `...WATH.TAG...\r\n...` before regex matching
  - Unescape sequences: `\\` → `\`, `\"` → `"`, `\\r` → `\r`, `\\n` → `\n`, `\\t` → `\t`
- **Extraction pattern:**
  - `r'(?<![\w.])WATH\.((?:[A-Z0-9]+\.)*[A-Z0-9_]+(?:QVA|QFL|QRN)?(?:\.F_CV)?)'` (on unescaped code)
  - Captures pure WATH tags (not prefixed with other text like ET.WATH.)
  - Matches tag names with possible suffixes like QVA, QFL, QRN, F_CV
- **Search the entire JSON file** - tags may appear in:
  - Input descriptors (`input[].value` and `input[].metadata`)
  - MVEL code blocks (`code[].value`)
  - Output references (rarely, but possible)
- **CRITICAL COUNTING REQUIREMENTS:**
  - Extract matches from all locations
  - Count TOTAL instances (sum of all occurrences): This is your baseline
  - Count UNIQUE tags: Combine results across all fields, remove duplicates
  - Store both counts separately
- For each unique tag, remove the `WATH.` prefix to get the base tag name for lookup
- Present a summary showing:
  - File name
  - **Total count of iFIX tag instances found** (e.g., "45 total instances across all calculations")
  - **Count of unique iFIX tags** (e.g., "28 unique tags")
  - List of unique iFIX tags (without WATH. prefix)
  - Per-calculation breakdown (e.g., "Calculation 'X': 5 instances of 3 unique tags")
- **CRITICAL:** If no instances of iFIX tags are found, report this to the user and skip conversion. Create a summary file indicating zero tags found and conversion skipped.

## Tag Lookup Matching

Use the CSV lookup file located at `src\ifix_to_ign_2026_02_19.csv`:

- The CSV has the following columns: `hist_tagname`, `ign_tagprovider`, `ign_tagname`, `ign_fullpath`, `imaginary`
- For each extracted iFIX tag (with WATH. prefix removed):
  - Search for a match in the `hist_tagname` column
  - The match should be exact (case-sensitive)
  - If found, retrieve the corresponding `ign_tagname` value
- **CRITICAL STOPPING CONDITION:** If any iFIX tag cannot be found in the lookup:
  - Report all unmatched tags to the user
  - List which calculations contain the missing tags
  - Generate a mismatch summary file in the `eris\output\tagcalcs\mismatches` directory (see `Mismatch Summary Generation` section)
  - **STOP ALL PROCESSING** - do not proceed with any conversion
  - Inform the user that the lookup table needs to be updated before conversion can proceed

## Mismatch Summary Generation

When iFIX tags cannot be found in the lookup table, create a mismatch summary file:

1. **Create mismatch summary markdown file:**
   - Location: `eris\output\tagcalcs\mismatches` directory
   - Filename: `CalcsConfigExport_mismatches.md`

2. **Mismatch summary content structure:**
   
   ```markdown
   # Tag Calculation Conversion Mismatch Summary: CalcsConfigExport.json
   
   **Analysis Date:** [Month Day, Year HH:MM AM/PM]
   **Original File:** `eris\input\tagcalcs\CalcsConfigExport.json`
   **Status:** ✗ Conversion Not Possible - Missing Lookup Entries
   
   ## Tag Analysis Statistics
   
   - Total unique iFIX tags found: [count]
   - Tags matched in lookup: [count]
   - Tags NOT matched in lookup: [count]
   - Match rate: [percentage]%
   
   ## Tags NOT Found in Lookup
   
   The following iFIX tags were found in calculations but do NOT have entries in the lookup table:
   
   | iFIX Tag (without WATH. prefix) | Calculations Using Tag | Instances |
   |--------------------------------|------------------------|-----------|
   | [tag_name] | [Calc1, Calc2, ...] | [count] |
   
   ## Tags Successfully Matched
   
   The following iFIX tags were found in both the file and the lookup table:
   
   | iFIX Tag Path | Ignition Tag Name (Lookup) | Instances Found |
   |---------------|----------------------------|-----------------|
   | WATH.[tag] | [ign_tagname] | [count] |
   
   ## Required Action
   
   The lookup table at `src\ifix_to_ign_2026_02_19.csv` must be updated with the missing iFIX tag entries before this file can be converted.
   
   Add entries to the lookup table for all tags listed in the "Tags NOT Found in Lookup" section above. Each entry should include:
   - `hist_tagname`: The iFIX tag name (without WATH. prefix)
   - `ign_tagprovider`: The Ignition tag provider
   - `ign_tagname`: The corresponding Ignition tag path
   - `ign_fullpath`: The full Ignition tag path
   - `imaginary`: Whether the tag is imaginary (true/false)
   
   After updating the lookup table, re-run the conversion process for this file.
   ```

   **Formatting Requirements:**
   - Date format: Use full month name, day, year, and 12-hour time with AM/PM (e.g., "February 13, 2026 09:07 AM")
   - Tables: Include all tag information with instance counts and calculation references
   - Use ✗ symbol for failure indicators
   - Clearly separate unmatched tags from matched tags
   - Include match rate percentage calculation

3. **User notification:**
   - Inform the user that a mismatch summary file has been created
   - Provide the path to the mismatch summary file
   - Remind user that the lookup table must be updated before conversion can proceed

## User Confirmation

If all iFIX tags are successfully matched in the lookup:

- Inform the user: "All [X] unique iFIX tag(s) found in [Y] calculation(s) have matching Ignition equivalents in the lookup table."
- Display a summary table showing:
  - Original iFIX tag path (with WATH. prefix)
  - Corresponding Ignition tag name from lookup (raw from ign_tagname column)
  - Formatted Ignition tag path that will be used (with IGNW. prefix and / replaced with -)
  - Total instances to be replaced
- Ask the user: "Do you want to proceed with converting the calculation configuration file?"
- Use the `ask_questions` tool to get user confirmation
- Only proceed if user explicitly confirms
- If user declines, stop processing and acknowledge their decision

## Tag Calculation Conversion

When user confirms conversion, process the calculation file:

1. **Create output copy:**
   - Create a copy of the original CalcsConfigExport.json file in the `eris\output\tagcalcs` directory
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
   - Before making ANY changes, count total instances of each iFIX tag in the original file
   - Store these counts for post-conversion verification
   - This ensures you know EXACTLY how many replacements should occur

4. **Replace tag paths in JSON:**
   - Parse the JSON file into memory
   - Iterate through each calculation in the JSON array
   - For each code block and any tag references:
     - Unescape JSON escape sequences to get readable code
     - Find all instances of `WATH.[tag_path]`
     - Replace with transformed Ignition tag path `IGNW.[transformed_path]`
     - Re-escape for JSON storage
   - Also replace in input descriptors and metadata where tags appear
   - Ensure all instances are replaced throughout the entire JSON document
   - Use Python's `str.replace()` method on unescaped strings, then re-escape

5. **Verify replacement:**
   - Reference the `Required Tools and Approaches` section for proper validation methods
   - Count remaining WATH tags in unescaped code - sum must equal 0:
     - Pattern: `r'(?<![\w.])WATH\.((?:[A-Z0-9]+\.)*[A-Z0-9_]+(?:QVA|QFL|QRN)?(?:\.F_CV)?)'`
     - Apply to all unescaped code blocks
   - Count IGNW tags - sum must equal total instances from extraction:
     - Pattern: `r'IGNW\.[a-z0-9_-]+(?:[.-]?[a-z0-9_-]+)*'`
     - Apply to all code blocks
   - **CRITICAL VALIDATION:**
     - If extraction found 45 total instances, post-conversion MUST show:
       - WATH remaining: 0 (sum across all calculations)
       - IGNW found: 45 (sum across all calculations)
     - Any deviation indicates incomplete conversion - FAIL the conversion and report error
   - Report verification results showing: WATH remaining (expected: 0), IGNW found (expected: [total instances])
   - If counts don't match expectations exactly, report detailed error and ask user to investigate

6. **Validate output JSON:**
   - Ensure the converted JSON is still valid JSON
   - Parse and re-serialize to verify correctness
   - Report any JSON structural errors

## Summary Generation

After completing conversion:

1. **Create summary markdown file:**
   - Location: `eris\output\tagcalcs\conversion_summary` directory
   - Filename: `CalcsConfigExport_conversion_summary.md`

2. **Summary content structure:**
   
   ```markdown
   # Tag Calculation Conversion Summary: CalcsConfigExport.json
   
   **Conversion Date:** [Month Day, Year HH:MM AM/PM]
   **Original File:** `eris\input\tagcalcs\CalcsConfigExport.json`
   **Converted File:** `eris\output\tagcalcs\CalcsConfigExport.json`
   
   ## Conversion Statistics
   
   - Total unique iFIX tags found: [count]
   - Total tag instances replaced: [count]
   - Total calculations processed: [count]
   - Calculations with replacements: [count]
   - All tags successfully matched: ✓
   
   ## Tag Mappings
   
   | iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
   |---------------|----------------------------|----------------------------|-------------------|
   | WATH.[tag] | [ign_tagname] | IGNW.[formatted_lowercase] | [count] |
   
   ## Conversion Details
   
   Successfully converted all [total instances] instances of [unique count] unique iFIX tag paths to their Ignition equivalents across [num calculations] calculations.
   
   **Verification:**
   - WATH tags remaining in output file: [count, should be 0]
   - IGNW tags in output file: [count, should match total instances]
   - JSON validation: ✓ Valid
   - Conversion status: ✓ Complete
   
   **Tag Format Transformation:**
   - iFIX format (in MVEL code): `WATH.[server].[tag_path]` 
   - Ignition format (IGNW prefix, path lowercase):
     - MVEL code usage: `IGNW.[formatted_path]` (forward slashes replaced with dashes, spaces replaced with underscores, path lowercase)
   
   **Calculations Affected:**
   - [Calculation Name 1]: [X] tag instances replaced
   - [Calculation Name 2]: [Y] tag instances replaced
   
   All tag paths were successfully validated against the lookup table and converted according to the specified transformation rules. The JSON structure has been preserved and validated.
   ```

   **Formatting Requirements:**
   - Date format: Use full month name, day, year, and 12-hour time with AM/PM (e.g., "February 13, 2026 09:07 AM")
   - Table: Include all tag mappings with instance counts
   - Conversion Details: Must include the opening summary, Verification subsection, and Tag Format Transformation subsection followed by Calculations Affected list and closing statement
   - Use checkmark symbol: ✓ for completion indicators

3. **Final user notification:**
   - Inform the user that conversion is complete
   - Provide the paths to the converted file and summary file
   - Confirm total number of tags replaced and calculations processed

```
