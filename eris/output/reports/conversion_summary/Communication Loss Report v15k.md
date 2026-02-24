# Report Conversion Summary: Communication Loss Report v15k.rptdesign

**Conversion Date:** February 20, 2026 01:25 PM
**Original File:** `eris/input/reports/Communication Loss Report v15k.rptdesign`
**Converted File:** `eris/output/reports/completed/Communication Loss Report v15k.rptdesign`

## Conversion Statistics

- Total unique iFIX tags found: 173
- Total tag instances replaced: 352
- All tags successfully matched: OK

## Tag Mappings

| iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
|---------------|----------------------------|----------------------------|-------------------|
| WATH.MTPSVR1.K21TWL01RF01QVA.F_CV | Kitchener/Wells/K21_PLC01/TWL01_RF01/QVA | IGNW.kitchener-wells-k21_plc01-twl01_rf01-qva | See above |
| WATH.MTPSVR1.K21W0021FI01QVA.F_CV | Kitchener/Wells/K21_PLC01/W0021_FI01/QVA | IGNW.kitchener-wells-k21_plc01-w0021_fi01-qva | See above |
| WATH.MTPSVR1.K25TWL01FI01QVA.F_CV | Kitchener/Wells/K25_PLC01/TWL01_FI01/QVA | IGNW.kitchener-wells-k25_plc01-twl01_fi01-qva | See above |
| WATH.MTPSVR1.K25TWL01RF01QVA.F_CV | Kitchener/Wells/K25_PLC01/TWL01_RF01/QVA | IGNW.kitchener-wells-k25_plc01-twl01_rf01-qva | See above |
| WATH.MTPSVR1.K29TWL01FI01QVA.F_CV | Kitchener/Wells/K29_PLC01/TWL01_FI01/QVA | IGNW.kitchener-wells-k29_plc01-twl01_fi01-qva | See above |
| WATH.MTPSVR1.K29TWL01RF01QVA.F_CV | Kitchener/Wells/K29_PLC01/TWL01_RF01/QVA | IGNW.kitchener-wells-k29_plc01-twl01_rf01-qva | See above |
| WATH.MTPSVR1.K91TWL01RF01QVA.F_CV | Kitchener/Wells/K91_PLC01/TWL01_RF01/QVA | IGNW.kitchener-wells-k91_plc01-twl01_rf01-qva | See above |
| WATH.MTPSVR1.K91TWL02RF01QVA.F_CV | Kitchener/Wells/K91_PLC01/TWL02_RF01/QVA | IGNW.kitchener-wells-k91_plc01-twl02_rf01-qva | See above |
| WATH.MTPSVR1.K91W0091FI01QVA.F_CV | Kitchener/Wells/K91_PLC01/W0091_FI01/QVA | IGNW.kitchener-wells-k91_plc01-w0091_fi01-qva | See above |
| WATH.MTPSVR1.K91W0092FI01QVA.F_CV | Kitchener/Wells/K91_PLC01/W0092_FI01/QVA | IGNW.kitchener-wells-k91_plc01-w0092_fi01-qva | See above |
| ... (163 more rows) | ... | ... | ... |

## Conversion Details

Successfully converted all 352 instances of 173 unique iFIX tag paths to their Ignition equivalents.

**Verification:**
- Data WATH tags remaining in output file: 0
- IGNW tags in output file: 352
- Calculated tags (ET.WATH.*, etc.) preserved: 0 (expected, unchanged)
- Data tag sanity check: OK PASSED (no unconverted WATH. data tags)
- Conversion status: OK Complete

**Tag Format Transformation:**
- iFIX formats:
  - JSON: `"tag" : "WATH.[server].[tag_path]"`
  - XML queryText: `Tag[number]:WATH.[server].[tag_path]:[parameters]`
- Ignition formats (IGNW prefix uppercase, path lowercase):
  - JSON: `"tag" : "IGNW.[lowercase-path-with-dashes]"`
  - XML queryText: `Tag[number]:IGNW.[lowercase-path-with-dashes]:[parameters]`

All tag paths were successfully validated against the lookup table and converted according to the specified transformation rules.
