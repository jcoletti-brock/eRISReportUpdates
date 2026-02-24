# Report Conversion Summary: Mannheim Filter Compliance Report v1a.rptdesign

**Conversion Date:** February 20, 2026 01:35 PM
**Original File:** `eris/input/reports/Mannheim Filter Compliance Report v1a.rptdesign`
**Converted File:** `eris/output/reports/completed/Mannheim Filter Compliance Report v1a.rptdesign`

## Conversion Statistics

- Total unique iFIX tags found: 8
- Total tag instances replaced: 16
- All tags successfully matched: OK

## Tag Mappings

| iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
|---------------|----------------------------|----------------------------|-------------------|
| WATH.MTPSVR1.MTPFL001NI01QVA.F_CV | MTP/MTP_PLCFL/FL001_NI01/QVA | IGNW.mtp-mtp_plcfl-fl001_ni01-qva | See above |
| WATH.MTPSVR1.MTPFL001OV01QZI.F_CV | MTP/MTP_PLCFL/FL001_OV01/QZI | IGNW.mtp-mtp_plcfl-fl001_ov01-qzi | See above |
| WATH.MTPSVR1.MTPFL002NI01QVA.F_CV | MTP/MTP_PLCFL/FL002_NI01/QVA | IGNW.mtp-mtp_plcfl-fl002_ni01-qva | See above |
| WATH.MTPSVR1.MTPFL002OV01QZI.F_CV | MTP/MTP_PLCFL/FL002_OV01/QZI | IGNW.mtp-mtp_plcfl-fl002_ov01-qzi | See above |
| WATH.MTPSVR1.MTPFL003NI01QVA.F_CV | MTP/MTP_PLCFL/FL003_NI01/QVA | IGNW.mtp-mtp_plcfl-fl003_ni01-qva | See above |
| WATH.MTPSVR1.MTPFL003OV01QZI.F_CV | MTP/MTP_PLCFL/FL003_OV01/QZI | IGNW.mtp-mtp_plcfl-fl003_ov01-qzi | See above |
| WATH.MTPSVR1.MTPFL004NI01QVA.F_CV | MTP/MTP_PLCFL/FL004_NI01/QVA | IGNW.mtp-mtp_plcfl-fl004_ni01-qva | See above |
| WATH.MTPSVR1.MTPFL004OV01QZI.F_CV | MTP/MTP_PLCFL/FL004_OV01/QZI | IGNW.mtp-mtp_plcfl-fl004_ov01-qzi | See above |

## Conversion Details

Successfully converted all 16 instances of 8 unique iFIX tag paths to their Ignition equivalents.

**Verification:**
- Data WATH tags remaining in output file: 0
- IGNW tags in output file: 16
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
