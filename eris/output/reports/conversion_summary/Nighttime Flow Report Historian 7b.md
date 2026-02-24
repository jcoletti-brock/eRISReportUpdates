# Report Conversion Summary: Nighttime Flow Report Historian 7b.rptdesign

**Conversion Date:** February 20, 2026 01:35 PM
**Original File:** `eris/input/reports/Nighttime Flow Report Historian 7b.rptdesign`
**Converted File:** `eris/output/reports/completed/Nighttime Flow Report Historian 7b.rptdesign`

## Conversion Statistics

- Total unique iFIX tags found: 4
- Total tag instances replaced: 4
- All tags successfully matched: OK

## Tag Mappings

| iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
|---------------|----------------------------|----------------------------|-------------------|
| WATH.MTPSVR2.BMSTWL01FI01QYF.F_CV | BMS_PLC01/TWL01_FI01/QYF | IGNW.bms_plc01-twl01_fi01-qyf | See above |
| WATH.MTPSVR2.LBMIL001FI01QFL.F_CV | Rural/North Dumfries/LBM_PLC01/IL001_FI01/QFL | IGNW.rural-north_dumfries-lbm_plc01-il001_fi01-qfl | See above |
| WATH.MTPSVR2.LINTWL01FI01QFL.F_CV | LIN_PLC01/TWL01_FI01/QFL | IGNW.lin_plc01-twl01_fi01-qfl | See above |
| WATH.MTPSVR2.WMHTWL01FI01QFL.F_CV | Rural/Woolwich/WMH_PLC01/TWL01_FI01/QFL | IGNW.rural-woolwich-wmh_plc01-twl01_fi01-qfl | See above |

## Conversion Details

Successfully converted all 4 instances of 4 unique iFIX tag paths to their Ignition equivalents.

**Verification:**
- Data WATH tags remaining in output file: 0
- IGNW tags in output file: 4
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
