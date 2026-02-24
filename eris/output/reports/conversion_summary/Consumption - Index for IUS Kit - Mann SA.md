# Report Conversion Summary: Consumption - Index for IUS Kit - Mann SA.rptdesign

**Conversion Date:** February 20, 2026 01:25 PM
**Original File:** `eris/input/reports/Consumption - Index for IUS Kit - Mann SA.rptdesign`
**Converted File:** `eris/output/reports/completed/Consumption - Index for IUS Kit - Mann SA.rptdesign`

## Conversion Statistics

- Total unique iFIX tags found: 27
- Total tag instances replaced: 81
- All tags successfully matched: OK

## Tag Mappings

| iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
|---------------|----------------------------|----------------------------|-------------------|
| WATH.MTPSVR1.K21W000XFI01QFL.F_CV | Kitchener/Wells/K21_PLC01/W000X_FI01/QFL | IGNW.kitchener-wells-k21_plc01-w000x_fi01-qfl | See above |
| WATH.MTPSVR1.K25TWL01FI01QFL.F_CV | Kitchener/Wells/K25_PLC01/TWL01_FI01/QFL | IGNW.kitchener-wells-k25_plc01-twl01_fi01-qfl | See above |
| WATH.MTPSVR1.K29TWL01FI01QFL.F_CV | Kitchener/Wells/K29_PLC01/TWL01_FI01/QFL | IGNW.kitchener-wells-k29_plc01-twl01_fi01-qfl | See above |
| WATH.MTPSVR1.K91W0091FI01QFL.F_CV | Kitchener/Wells/K91_PLC01/W0091_FI01/QFL | IGNW.kitchener-wells-k91_plc01-w0091_fi01-qfl | See above |
| WATH.MTPSVR1.K91W0092FI01QFL.F_CV | Kitchener/Wells/K91_PLC01/W0092_FI01/QFL | IGNW.kitchener-wells-k91_plc01-w0092_fi01-qfl | See above |
| WATH.MTPSVR1.K93W0093FI01QFL.F_CV | Kitchener/Wells/K93_PLC01/W0093_FI01/QFL | IGNW.kitchener-wells-k93_plc01-w0093_fi01-qfl | See above |
| WATH.MTPSVR1.K93W0094FI01QFL.F_CV | Kitchener/Wells/K93_PLC01/W0094_FI01/QFL | IGNW.kitchener-wells-k93_plc01-w0094_fi01-qfl | See above |
| WATH.MTPSVR1.MTPTWL01FI01QFL.F_CV | MTP/MTP_PLCPD/TWL01_FI01/QFL | IGNW.mtp-mtp_plcpd-twl01_fi01-qfl | See above |
| WATH.MTPSVR2.KHVDSH01FI01QFL.F_CV | Cambridge/KHV_PLC01/DSH01_FI01/QFL | IGNW.cambridge-khv_plc01-dsh01_fi01-qfl | See above |
| WATH.MTPSVR3.BLMVCH01FI01QFL.F_CV | Kitchener/BLM_PLC01/VCH01_FI01/QFL | IGNW.kitchener-blm_plc01-vch01_fi01-qfl | See above |
| ... (17 more rows) | ... | ... | ... |

## Conversion Details

Successfully converted all 81 instances of 27 unique iFIX tag paths to their Ignition equivalents.

**Verification:**
- Data WATH tags remaining in output file: 0
- IGNW tags in output file: 81
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
