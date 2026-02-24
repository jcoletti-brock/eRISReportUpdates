---
description: "Convert JSON config files from iFIX tag paths to Ignition tag paths using batch processing"
---

Your goal is to convert JSON config files in bulk from iFIX tag path references to Ignition tag path references using a CSV lookup table. You will validate JSON structure, extract tags, match them against a lookup file, and perform batch conversion after user confirmation.

## Config File Conversion Workflow

Follow these instructions when converting JSON config files from iFIX to Ignition in batch:

**IMPORTANT:** Before starting, review the `Required Tools and Approaches` section below to understand which specific tools and methods must be used for each step.

1. Scan the `eris\input\tagspecs` directory for all .json files (494 total expected)
   - Build a list of all config files to process
   - Report the total count to the user

2. Validate each file as valid JSON
   - Reference the `Required Tools and Approaches` section for specific validation tools
   - Reference the `JSON Validation` section below for more details
   - Continue processing even if individual files fail validation - collect and report all failures

3. Extract all iFIX tag paths from ALL files
   - Reference the `Required Tools and Approaches` section for extraction tools
   - Reference the `iFIX Tag Path Extraction` section below for more details
   - Aggregate results across ALL files (not per-file)
   - Build a unified tracking datastructure showing which files contain which tags

4. Match aggregated extracted tags against the CSV lookup file
   - Reference the `Required Tools and Approaches` section for CSV processing tools
   - Reference the `Tag Lookup Matching` section below for more details
   - Perform matching ONCE for all unique tags, not per-file

5. If any mismatches are found globally, generate a batch mismatch summary document
   - Reference the `Batch Mismatch Summary Generation` section below for more details
   - Stop processing completely - do not proceed with conversions

6. If all tags matched successfully, report findings and request user confirmation
   - Reference the `User Confirmation` section below for more details
   - Display summary of config files to be converted and total tag replacements

7. If user confirms, perform batch conversion on all config files
   - Reference the `Required Tools and Approaches` section for file conversion tools
   - Reference the `Batch Conversion` section below for more details

8. Generate batch conversion summary documents
   - Reference the `Batch Summary Generation` section below for more details

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
- Use Python's `json.load()` method in a try/except block
- Execute using preferred Python tool (Pylance MCP or terminal)
- Report any parsing exceptions as validation failures
- Continue processing other files even if some fail validation

### iFIX Tag Extraction
- Use Python's `re` module
- **CRITICAL:** Check ALL possible tag formats - tags may appear in ANY context within JSON:
  - Direct string values: `"value": "WATH.TAG.PATH"`
  - Within object keys: `"WATH.TAG.PATH": {...}`
  - Nested in arrays: `["WATH.TAG.PATH", ...]`
  - Within complex strings or templates
- **Extraction pattern:** `r'(?<![A-Z0-9_.-])WATH\.[A-Z0-9_.]+(?![A-Z0-9_.-])'` 
  - Captures pure `WATH.` data tags (those starting with WATH. directly)
  - Negative lookbehind/lookahead prevents matching prefixed variants
- Use `re.findall()` on full file content as string
- **CRITICAL:** Count TOTAL instances across ALL files (this is your baseline)
- Record unique tags and their instances per file for detailed tracking
- Store total instance count - this MUST match post-conversion count
- Process results to remove `WATH.` prefix for lookup matching

### CSV Lookup Processing
- Use Python's `csv.DictReader`
- Encoding: `utf-8-sig` (handles UTF-8 with or without BOM)
- Build lookup dictionary keyed by `hist_tagname` column
- Perform exact case-sensitive matching
- Load CSV ONCE into memory for efficient repeated lookups

### Batch File Conversion
- **PREFERRED:** Use Python string replacement with file I/O in a loop
  - Load all file paths first
  - Process each file with the same replacement logic
  - Write to output directory
- Track success/failure per file
- Handle file write errors gracefully
- Maintain detailed logs of which files were converted successfully

### Batch Conversion Verification
- **Verify iFIX tag removal:** After ALL conversions, spot-check representative files
  - Check pattern: `r'(?<![A-Z0-9_.-])WATH\.[A-Z0-9_.]+(?![A-Z0-9_.-])'`
  - Sum of remaining WATH matches across sampled files should be 0
- **Verify Ignition tag presence:** Check representative output files
  - Check pattern: `r'IGNW\.[^\s",}:\]]+'`
  - Verify counts match expected replacements for sampled files
- **Aggregate verification:** Track total replacements made across ALL files
  - Must EXACTLY EQUAL total instances found during extraction phase
  - If counts don't match, conversion is incomplete - report detailed error

## JSON Validation

Before processing any config file:

- Use appropriate tools to verify each .json file is valid JSON
- If any file fails validation, report the error with file name and error details
- **IMPORTANT:** Do not skip invalid files - collect all validation failures and report them
- Continue processing valid files while noting which files had validation issues
- Invalid files should not be processed or output

## iFIX Tag Path Extraction

Search the entire JSON content for iFIX tag paths in ALL possible formats:

- iFIX tag paths are identified by the prefix `WATH.` and can appear ANYWHERE in JSON:
  - String values: `"field": "WATH.TAG"`
  - Object keys: `{"WATH.TAG": value}`
  - Within arrays, nested objects, or embedded in other strings
- **IMPORTANT - Exclude calculated/derived tags:**
  - Calculated tags have prefixes before WATH (e.g., `ET.WATH.`, `MDPH.WATH.`, etc.)
  - These represent system-generated or derived values and should NOT be extracted or converted
  - Only extract pure `WATH.` data tags (those starting with WATH. directly, with no prefix)
  - Use negative lookbehind: `(?<![A-Z0-9_.-])` to exclude prefixed tags
- **Extraction pattern - MUST use this pattern:**
  - Pattern: `r'(?<![A-Z0-9_.-])WATH\.[A-Z0-9_.]+(?![A-Z0-9_.-])'`
  - Captures WATH tags surrounded by word boundaries, excluding prefixed variants
- **Search ENTIRE content of ALL files** with this pattern
- **CRITICAL COUNTING REQUIREMENTS:**
  - Count TOTAL instances across ALL files (sum of all occurrences): This is your baseline
  - Count UNIQUE tags across all files: Combine results, remove duplicates
  - Track PER-FILE instance counts: Record which files contain which tags and how many instances
  - Store all counts separately - they serve different purposes
- For each unique tag, remove the `WATH.` prefix to get the base tag name for lookup
- Present a summary showing:
  - Total config files scanned
  - Count of config files containing iFIX tags
  - **Total count of iFIX tag instances across ALL files** (e.g., "250 total instances")
  - **Count of unique iFIX tags** (e.g., "45 unique tags")
  - List of unique iFIX tags (without WATH. prefix)
  - Per-tag statistics: total instances across all files, which config files contain each tag
- **CRITICAL:** If no instances of data iFIX tags (pure WATH. format) are found across ANY file using the pattern, report this to the user and skip conversion. Create a summary file indicating zero tags found and conversion skipped.

## Tag Lookup Matching

Use the CSV lookup file located at `src\ifix_to_ign_010152026.csv`:

- The CSV has the following columns: `hist_tagname`, `ign_tagprovider`, `ign_tagname`, `ign_fullpath`, `imaginary`
- For each extracted unique iFIX tag (with WATH. prefix removed):
  - Search for a match in the `hist_tagname` column
  - The match should be exact (case-sensitive)
  - If found, retrieve the corresponding `ign_tagname` value
- **CRITICAL STOPPING CONDITION:** If ANY iFIX tag cannot be found in the lookup:
  - Report all unmatched tags to the user
  - List the unmatched tags and which config files contain them
  - Generate a batch mismatch summary file in the `eris\output\tagspecs\mismatches` directory (see `Batch Mismatch Summary Generation` section)
  - **STOP ALL PROCESSING** - do not proceed with any conversions
  - Inform the user that the lookup table needs to be updated before conversion can proceed

## Batch Mismatch Summary Generation

When iFIX tags cannot be found in the lookup table, create a comprehensive batch mismatch summary:

1. **Create batch mismatch summary markdown file:**
   - Location: `eris\output\tagspecs\mismatches` directory
   - Filename: `BATCH_MISMATCH_SUMMARY_[TIMESTAMP].md`
   - Example: `BATCH_MISMATCH_SUMMARY_2026-02-19_143052.md`

2. **Batch mismatch summary content structure:**

   ```markdown
   # Config File Batch Conversion Mismatch Summary
   
   **Analysis Date:** [Month Day, Year HH:MM AM/PM]
   **Files Scanned:** [count]
   **Config Files with iFIX Tags:** [count]
   **Status:** ✗ Conversion Not Possible - Missing Lookup Entries
   
   ## Overall Statistics
   
   - Total unique iFIX tags found: [count]
   - Tags matched in lookup: [count]
   - Tags NOT matched in lookup: [count]
   - Match rate: [percentage]%
   
   ## Tags NOT Found in Lookup
   
   The following iFIX tags were found in config files but do NOT have entries in the lookup table:
   
   | iFIX Tag (without WATH. prefix) | Total Instances | Config Files Containing Tag | Instances Per File |
   |--------------------------------|-----------------|---------------------------|-------------------|
   | [tag_name] | [total_count] | file1.json (5), file2.json (3), ... | See details below |
   
   ### Detailed Instance Breakdown by Config File
   
   #### [tag_name]
   - `config_file_1.json`: [count] instances
   - `config_file_2.json`: [count] instances
   - ...
   
   ## Tags Successfully Matched
   
   The following iFIX tags were found in config files and DO have matching entries:
   
   | iFIX Tag Path | Ignition Tag Name (Lookup) | Total Instances | Config Files Containing Tag |
   |---------------|----------------------------|-----------------|---------------------------|
   | WATH.[tag] | [ign_tagname] | [count] | file1.json (3), file3.json (7), ... |
   
   ## Required Action
   
   **The lookup table at `src\ifix_to_ign_010152026.csv` must be updated with the missing iFIX tag entries before batch conversion can proceed.**
   
   Add entries to the lookup table for all tags listed in the "Tags NOT Found in Lookup" section above. Each entry should include:
   - `hist_tagname`: The iFIX tag name (without WATH. prefix)
   - `ign_tagprovider`: The Ignition tag provider
   - `ign_tagname`: The corresponding Ignition tag path
   - `ign_fullpath`: The full Ignition tag path
   - `imaginary`: Whether the tag is imaginary (true/false)
   
   After updating the lookup table, re-run the batch conversion process for all config files.
   ```

   **Formatting Requirements:**
   - Date format: Use full month name, day, year, and 12-hour time with AM/PM (e.g., "February 19, 2026 09:07 AM")
   - Include detailed instance breakdown
   - Tables for both unmatched and matched tags
   - Use ✗ symbol for failure indicators
   - Clearly separate unmatched tags from matched tags
   - Include match rate percentage calculation
   - List affected config files with instance counts

3. **User notification:**
   - Inform the user that a batch mismatch summary file has been created
   - Provide the path to the mismatch summary file
   - Remind user that the lookup table must be updated before batch conversion can proceed

## User Confirmation

If all iFIX tags are successfully matched in the lookup:

- Inform the user: "All [X] unique iFIX tag(s) have matching Ignition equivalents in the lookup table. Ready to process [Y] config file(s)."
- Display a summary table showing:
  - Original iFIX tag path (with WATH. prefix)
  - Corresponding Ignition tag name from lookup (raw from ign_tagname column)
  - Formatted Ignition tag path that will be used (with IGNW. prefix and / replaced with -)
  - Total instances to be replaced across ALL config files
- Ask the user: "Do you want to proceed with converting all config file(s)?"
- Use the `ask_questions` tool to get user confirmation
- Only proceed if user explicitly confirms
- If user declines, stop processing and acknowledge their decision

## Batch Conversion

When user confirms conversion, process all config files in batch:

1. **Create output directory structure:**
   - Ensure `eris\output\tagspecs\completed` directory exists
   - Create it if it doesn't exist

2. **Transform Ignition tag paths:**
   - For each matched tag, take the `ign_tagname` value from the lookup
   - Apply the following transformation:
     - Take the full tag path (e.g., `Cambridge/Galt Wells/G04_PLC01/CBW_G004_AI01/QVA`)
     - Replace all forward slashes `/` with hyphens `-`
     - Convert entire path (except prefix) to lowercase
   - Example: If `ign_tagname` is `Cambridge/Galt Wells/G04_PLC01/CBW_G004_AI01/QVA`, transform to `IGNW.cambridge-galt wells-g04-plc01-cbw-g004-ai01-qva`
   - **IMPORTANT:** Preserve spaces as-is in the transformed path (do NOT remove or replace spaces)

3. **Pre-conversion instance count:**
   - Before making ANY changes, count total instances of each iFIX tag path across ALL files
   - Store these counts for post-conversion verification
   - This ensures you know EXACTLY how many replacements should occur

4. **Replace tag paths in JSON:**
   - For each config file in input directory:
     - Load file as JSON or raw text
     - For each matched tag pair (iFIX → Ignition):
       - Find all instances of `WATH.[tag_path]`
       - Replace with transformed Ignition tag path `IGNW.[transformed_path]`
       - Ensure ALL occurrences are replaced
     - Write converted file to `eris\output\tagspecs\completed` directory with same filename
     - Validate output JSON is valid after conversion
   - Use Python's `str.replace()` method which replaces ALL occurrences
   - Preserve original formatting and structure as much as possible

5. **Track conversion results:**
   - Record which files were successfully converted
   - Record which files had errors or JSON validation failures
   - Count actual replacements made per file
   - Aggregate statistics across all files

6. **Verify replacement:**
   - Reference the `Batch Conversion Verification` subsection in `Required Tools and Approaches` for proper validation methods
   - For representative sample of converted files (at least 10% or 50 files, whichever is larger):
     - Count remaining WATH tags using extraction pattern - should equal 0
     - Count IGNW tags - should match expected replacement counts
   - Aggregate total IGNW count across sampled files
   - Verify it proportionally matches the pre-conversion baseline
   - **CRITICAL SANITY CHECK - Data Tag Verification:**
     - Total replacements made across ALL files must EXACTLY EQUAL total instances found during extraction
     - If extraction found 250 total instances, you must make exactly 250 replacements across all files
     - If counts don't match, conversion is incomplete - investigate and report detailed error
     - Report which files were successfully converted vs. which had issues

## Batch Summary Generation

After completing batch conversion:

1. **Create batch conversion summary markdown file:**
   - Location: `eris\output\tagspecs\conversion_summary` directory
   - Filename: `BATCH_CONVERSION_SUMMARY_[TIMESTAMP].md`
   - Example: `BATCH_CONVERSION_SUMMARY_2026-02-19_143052.md`

2. **Batch summary content structure:**

   ```markdown
   # Config File Batch Conversion Summary
   
   **Conversion Date:** [Month Day, Year HH:MM AM/PM]
   **Files Scanned:** [count]
   **Files Successfully Converted:** [count]
   **Files Skipped/Failed:** [count]
   **Status:** ✓ Batch Conversion Complete
   
   ## Conversion Statistics
   
   - Total unique iFIX tags converted: [count]
   - Total tag instances replaced: [count]
   - Total tag instances expected: [count]
   - Replacement verification: ✓ PASSED / ✗ FAILED
   
   ## Tag Conversion Summary
   
   | iFIX Tag Path | Ignition Tag Name (Lookup) | Transformed Ignition Path | Total Replacements |
   |---------------|----------------------------|--------------------------|------------------|
   | WATH.[tag] | [ign_tagname] | IGNW.[transformed] | [count] |
   
   ## Per-File Conversion Details
   
   ### Successfully Converted Files ([count])
   
   | Config File | Tags Replaced | Instances Replaced |
   |-------------|---------------|------------------|
   | file1.json | tag1, tag2, tag3 | 12 |
   | file2.json | tag2, tag4 | 8 |
   | ... | ... | ... |
   
   ### Files Skipped/Failed ([count])
   
   | Config File | Reason |
   |-------------|--------|
   | file_X.json | [reason - e.g., invalid JSON, no iFIX tags found] |
   
   ## Verification Results
   
   - Pre-conversion baseline: [count] total instances
   - Actual replacements made: [count] total instances
   - Post-conversion iFIX tags remaining (sample check): 0
   - Post-conversion IGNW tags present (sample check): ✓ Verified
   - **Overall verification:** ✓ PASSED
   
   ## Output Location
   
   All successfully converted config files have been saved to:
   ```
   eris\output\tagspecs\completed\
   ```
   
   Files are organized with the same names as the originals for easy reference.
   
   ## Next Steps
   
   The converted config files are ready for deployment or further processing. Original files remain unchanged in `eris\input\tagspecs\`.
   ```

   **Formatting Requirements:**
   - Date format: Use full month name, day, year, and 12-hour time with AM/PM
   - Include detailed per-file statistics
   - Use ✓ for success indicators, ✗ for failures
   - Show both aggregate and per-file metrics
   - Clear separation of successful vs. failed/skipped files
   - Include verification status explicitly

3. **Additional per-file summary (optional but recommended):**
   - Create individual summary files for EACH converted config file
   - Location: `eris\output\tagspecs\conversion_summary\[original_filename_without_ext].md`
   - Content: Original file name, tags replaced, instances replaced, output location

4. **Final user notification:**
   - Present the batch conversion summary results to the user
   - Confirm number of files successfully converted
   - Highlight any files that had issues
   - Provide location of output files and summary documentation
