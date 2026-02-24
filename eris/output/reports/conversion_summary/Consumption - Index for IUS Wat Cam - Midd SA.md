# Report Conversion Summary: Consumption - Index for IUS Wat Cam - Midd SA.rptdesign

**Conversion Date:** February 20, 2026 01:25 PM
**Original File:** `eris/input/reports/Consumption - Index for IUS Wat Cam - Midd SA.rptdesign`
**Converted File:** `eris/output/reports/completed/Consumption - Index for IUS Wat Cam - Midd SA.rptdesign`

## Conversion Statistics

- Total unique iFIX tags found: 28
- Total tag instances replaced: 84
- All tags successfully matched: OK

## Tag Mappings

| iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
|---------------|----------------------------|----------------------------|-------------------|
| WATH.MTPSVR2.CBVVCH01FI01QFL.F_CV | Rural/Woolwich/CBV_PLC01/VCH01_FI01/QFL | IGNW.rural-woolwich-cbv_plc01-vch01_fi01-qfl | See above |
| WATH.MTPSVR2.CBWG004TT.F_CV | Cambridge/Galt Wells/G04_PLC01/CBWG004TT | IGNW.cambridge-galt_wells-g04_plc01-cbwg004tt | See above |
| WATH.MTPSVR2.DUNVCH01FI01QFL.F_CV | Cambridge/DUN_PLC01/VCH01_FI01/QFL | IGNW.cambridge-dun_plc01-vch01_fi01-qfl | See above |
| WATH.MTPSVR2.G05TWL01FI01QFL.F_CV | Cambridge/Galt Wells/G05_PLC01/TWL01_FI01/QFL | IGNW.cambridge-galt_wells-g05_plc01-twl01_fi01-qfl | See above |
| WATH.MTPSVR2.G09TWL01FI01QFL.F_CV | Cambridge/Galt Wells/G09_PLC01/TWL01_FI01/QFL | IGNW.cambridge-galt_wells-g09_plc01-twl01_fi01-qfl | See above |
| WATH.MTPSVR2.H03TWL01FI01QFL.F_CV | Cambridge/Hespeler Wells/H03_PLC01/TWL01_FI01/QFL | IGNW.cambridge-hespeler_wells-h03_plc01-twl01_fi01-qfl | See above |
| WATH.MTPSVR2.H04TWL01FI01QFL.F_CV | Cambridge/Hespeler Wells/H04_PLC01/TWL01_FI01/QFL | IGNW.cambridge-hespeler_wells-h04_plc01-twl01_fi01-qfl | See above |
| WATH.MTPSVR2.H05TWL01FI01QFL.F_CV | Cambridge/Hespeler Wells/H05_PLC01/TWL01_FI01/QFL | IGNW.cambridge-hespeler_wells-h05_plc01-twl01_fi01-qfl | See above |
| WATH.MTPSVR2.KHVDSH01FI01QFL.F_CV | Cambridge/KHV_PLC01/DSH01_FI01/QFL | IGNW.cambridge-khv_plc01-dsh01_fi01-qfl | See above |
| WATH.MTPSVR2.LBMIL001FI01QFL.F_CV | Rural/North Dumfries/LBM_PLC01/IL001_FI01/QFL | IGNW.rural-north_dumfries-lbm_plc01-il001_fi01-qfl | See above |
| ... (18 more rows) | ... | ... | ... |

## Conversion Details

Successfully converted all 84 instances of 28 unique iFIX tag paths to their Ignition equivalents.

**Verification:**
- Data WATH tags remaining in output file: 0
- IGNW tags in output file: 84
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
