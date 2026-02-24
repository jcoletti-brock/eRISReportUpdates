# Report Conversion Summary: Pump_Volumes.rptdesign

**Conversion Date:** February 20, 2026 01:35 PM
**Original File:** `eris/input/reports/Pump_Volumes.rptdesign`
**Converted File:** `eris/output/reports/completed/Pump_Volumes.rptdesign`

## Conversion Statistics

- Total unique iFIX tags found: 63
- Total tag instances replaced: 189
- All tags successfully matched: OK

## Tag Mappings

| iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
|---------------|----------------------------|----------------------------|-------------------|
| WATH.MTPSVR1.K21W0021FI01QFL.F_CV | Kitchener/Wells/K21_PLC01/W0021_FI01/QFL | IGNW.kitchener-wells-k21_plc01-w0021_fi01-qfl | See above |
| WATH.MTPSVR1.K21W021AFI01QFL.F_CV | Kitchener/Wells/K21_PLC01/W021A_FI01/QFL | IGNW.kitchener-wells-k21_plc01-w021a_fi01-qfl | See above |
| WATH.MTPSVR1.K25TWL01FI01QFL.F_CV | Kitchener/Wells/K25_PLC01/TWL01_FI01/QFL | IGNW.kitchener-wells-k25_plc01-twl01_fi01-qfl | See above |
| WATH.MTPSVR1.K29TWL01FI01QFL.F_CV | Kitchener/Wells/K29_PLC01/TWL01_FI01/QFL | IGNW.kitchener-wells-k29_plc01-twl01_fi01-qfl | See above |
| WATH.MTPSVR1.K91W0091FI01QFL.F_CV | Kitchener/Wells/K91_PLC01/W0091_FI01/QFL | IGNW.kitchener-wells-k91_plc01-w0091_fi01-qfl | See above |
| WATH.MTPSVR1.K91W0092FI01QFL.F_CV | Kitchener/Wells/K91_PLC01/W0092_FI01/QFL | IGNW.kitchener-wells-k91_plc01-w0092_fi01-qfl | See above |
| WATH.MTPSVR1.K93W0093FI01QFL.F_CV | Kitchener/Wells/K93_PLC01/W0093_FI01/QFL | IGNW.kitchener-wells-k93_plc01-w0093_fi01-qfl | See above |
| WATH.MTPSVR1.K93W0094FI01QFL.F_CV | Kitchener/Wells/K93_PLC01/W0094_FI01/QFL | IGNW.kitchener-wells-k93_plc01-w0094_fi01-qfl | See above |
| WATH.MTPSVR2.BMSW0002FI01QYF.F_CV | BMS_PLC01/W0002_FI01/QYF | IGNW.bms_plc01-w0002_fi01-qyf | See above |
| WATH.MTPSVR2.BMSW0003FI01QFL.F_CV | BMS_PLC01/W0003_FI01/QFL | IGNW.bms_plc01-w0003_fi01-qfl | See above |
| ... (53 more rows) | ... | ... | ... |

## Conversion Details

Successfully converted all 189 instances of 63 unique iFIX tag paths to their Ignition equivalents.

**Verification:**
- Data WATH tags remaining in output file: 0
- IGNW tags in output file: 189
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
