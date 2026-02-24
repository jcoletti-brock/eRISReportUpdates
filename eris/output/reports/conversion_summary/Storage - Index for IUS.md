# Report Conversion Summary: Storage - Index for IUS.rptdesign

**Conversion Date:** February 20, 2026 01:35 PM
**Original File:** `eris/input/reports/Storage - Index for IUS.rptdesign`
**Converted File:** `eris/output/reports/completed/Storage - Index for IUS.rptdesign`

## Conversion Statistics

- Total unique iFIX tags found: 25
- Total tag instances replaced: 75
- All tags successfully matched: OK

## Tag Mappings

| iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
|---------------|----------------------------|----------------------------|-------------------|
| WATH.MTPSVR1.M6PRES03LI01QVA.F_CV | Z456/M6P_PLC01/RES03_LI01/QVA | IGNW.z456-m6p_plc01-res03_li01-qva | See above |
| WATH.MTPSVR1.M6PRES04LI01QVA.F_CV | Z456/M6P_PLC01/RES04_LI01/QVA | IGNW.z456-m6p_plc01-res04_li01-qva | See above |
| WATH.MTPSVR1.M6PRES05LI01QVA.F_CV | Z456/M6P_PLC01/RES05_LI01/QVA | IGNW.z456-m6p_plc01-res05_li01-qva | See above |
| WATH.MTPSVR1.MHROL010FI01QFL.F_CV | MHR_PLC01/OL010_FI01/QFL | IGNW.mhr_plc01-ol010_fi01-qfl | See above |
| WATH.MTPSVR1.MHRRES01LI01QVA.F_CV | MHR_PLC01/RES01_LI01/QVA | IGNW.mhr_plc01-res01_li01-qva | See above |
| WATH.MTPSVR1.MHRRES02LI01QVA.F_CV | MHR_PLC01/RES02_LI01/QVA | IGNW.mhr_plc01-res02_li01-qva | See above |
| WATH.MTPSVR2.EWTETK01LI01QVA.F_CV | Rural/Woolwich/EWT_PLC01/ETK01_LI01/QVA | IGNW.rural-woolwich-ewt_plc01-etk01_li01-qva | See above |
| WATH.MTPSVR2.HWSETK01LI01QVA.F_CV | Rural/Woolwich/HWS_PLC01/ETK01_LI01/QVA | IGNW.rural-woolwich-hws_plc01-etk01_li01-qva | See above |
| WATH.MTPSVR2.INTETK01LI01QVA.F_CV | Cambridge/INT_PLC01/ETK01_LI01/QVA | IGNW.cambridge-int_plc01-etk01_li01-qva | See above |
| WATH.MTPSVR2.MDPTWR01LI01QVA.F_CV | MDP_PLC01/TWR01_LI01/QVA | IGNW.mdp_plc01-twr01_li01-qva | See above |
| ... (15 more rows) | ... | ... | ... |

## Conversion Details

Successfully converted all 75 instances of 25 unique iFIX tag paths to their Ignition equivalents.

**Verification:**
- Data WATH tags remaining in output file: 0
- IGNW tags in output file: 75
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
