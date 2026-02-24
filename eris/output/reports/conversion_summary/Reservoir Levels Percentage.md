# Report Conversion Summary: Reservoir Levels Percentage.rptdesign

**Conversion Date:** February 18, 2026 03:38 PM
**Original File:** `eris\input\reports\Reservoir Levels Percentage.rptdesign`
**Converted File:** `eris\output\reports\Reservoir Levels Percentage.rptdesign`

## Conversion Statistics

- Total unique iFIX tags found: 14
- Total tag instances replaced: 15
- All matched tags successfully converted: Yes (5 out of 5)
- Unmatched tags left unchanged: 9

## Tag Mappings

| iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
|---------------|----------------------------|----------------------------|-------------------|
| WATH.MTPSVR1.M6PRES03LI01QVA.F_CV | Z456/M6P_PLC01/RES03_LI01/QVA | IGNW.z456-m6p_plc01-res03_li01-qva | 3 |
| WATH.MTPSVR1.M6PRES04LI01QVA.F_CV | Z456/M6P_PLC01/RES04_LI01/QVA | IGNW.z456-m6p_plc01-res04_li01-qva | 3 |
| WATH.MTPSVR1.M6PRES05LI01QVA.F_CV | Z456/M6P_PLC01/RES05_LI01/QVA | IGNW.z456-m6p_plc01-res05_li01-qva | 3 |
| WATH.MTPSVR3.K34TWR01LI01QVA.F_CV | Kitchener/Wells/K34_PLC01/TWR01_LI01/QVA | IGNW.kitchener-wells-k34_plc01-twr01_li01-qva | 3 |
| WATH.MTPSVR3.WSPRES1LIQ01.F_CV | Kitchener/WSP_PLC01/WSPRES1LIQ01 | IGNW.kitchener-wsp_plc01-wspres1liq01 | 3 |

## Conversion Details

Successfully converted 15 instances of 5 unique iFIX tag paths to their Ignition equivalents. Nine tags without lookup entries were left unchanged in the output file.

**Verification:**
- Matched IGNW tags in output file: 15 (expected)
- Unmatched WATH tags remaining in output file: 27 (expected - 9 tags x 3 instances each)
- Lab parameters replaced (:lab: to :esrLab:): 14 instances
- Conversion status: Complete (partial - matched tags only)

**Tag Format Transformation:**
- iFIX formats: 
  - JSON: `"tag" : "WATH.[server].[tag_path]"` 
  - XML queryText: `Tag[number]:WATH.[server].[tag_path]:[parameters]`
- Ignition formats (IGNW prefix uppercase, path lowercase):
  - JSON: `"tag" : "IGNW.[formatted_path]"` (forward slashes replaced with dashes, path lowercase)
  - XML queryText: `Tag[number]:IGNW.[formatted_path]:[parameters]` (forward slashes replaced with dashes, path lowercase)

Successfully converted all matching tag paths. Nine unmatched iFIX tags (MTPSVR1.MTRTWR1LIQ01.F_CV, MTPSVR1.MTRTWR2LIQ01.F_CV, MTPSVR3.ERRRES1LIQ01.F_CV, MTPSVR3.FPTETK1LIQ01.F_CV, MTPSVR3.GBPTWR1LIQ01.F_CV, MTPSVR3.GBPTWR2LIQ01.F_CV, MTPSVR3.LATETK1LIQ01.F_CV, MTPSVR3.PKPRES1LIQ01.F_CV, MTPSVR3.Z6TETK1LIQ01.F_CV) remain in the output file and will require lookup table updates before being converted in a future run.
