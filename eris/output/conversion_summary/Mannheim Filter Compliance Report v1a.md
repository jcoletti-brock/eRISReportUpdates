# Report Conversion Summary: Mannheim Filter Compliance Report v1a.rptdesign

**Conversion Date:** February 15, 2026 12:04 AM
**Original File:** `eris\input\reports\Mannheim Filter Compliance Report v1a.rptdesign`
**Converted File:** `eris\output\reports\Mannheim Filter Compliance Report v1a.rptdesign`

## Conversion Statistics

- Total unique iFIX tags found: 8
- Total tag instances replaced: 16
- All tags successfully matched: ✓

## Tag Mappings

| iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
|---------------|----------------------------|----------------------------|-------------------|
| WATH.MTPSVR1.MTPFL001NI01QVA.F_CV | MTP/MTP_PLCFL/FL001_NI01/QVA | IGNW.MTP-MTP_PLCFL-FL001_NI01-QVA | 2 |
| WATH.MTPSVR1.MTPFL001OV01QZI.F_CV | MTP/MTP_PLCFL/FL001_OV01/QZI | IGNW.MTP-MTP_PLCFL-FL001_OV01-QZI | 2 |
| WATH.MTPSVR1.MTPFL002NI01QVA.F_CV | MTP/MTP_PLCFL/FL002_NI01/QVA | IGNW.MTP-MTP_PLCFL-FL002_NI01-QVA | 2 |
| WATH.MTPSVR1.MTPFL002OV01QZI.F_CV | MTP/MTP_PLCFL/FL002_OV01/QZI | IGNW.MTP-MTP_PLCFL-FL002_OV01-QZI | 2 |
| WATH.MTPSVR1.MTPFL003NI01QVA.F_CV | MTP/MTP_PLCFL/FL003_NI01/QVA | IGNW.MTP-MTP_PLCFL-FL003_NI01-QVA | 2 |
| WATH.MTPSVR1.MTPFL003OV01QZI.F_CV | MTP/MTP_PLCFL/FL003_OV01/QZI | IGNW.MTP-MTP_PLCFL-FL003_OV01-QZI | 2 |
| WATH.MTPSVR1.MTPFL004NI01QVA.F_CV | MTP/MTP_PLCFL/FL004_NI01/QVA | IGNW.MTP-MTP_PLCFL-FL004_NI01-QVA | 2 |
| WATH.MTPSVR1.MTPFL004OV01QZI.F_CV | MTP/MTP_PLCFL/FL004_OV01/QZI | IGNW.MTP-MTP_PLCFL-FL004_OV01-QZI | 2 |

## Conversion Details

Successfully converted all 16 instances of 8 unique iFIX tag paths to their Ignition equivalents.

**Verification:**
- WATH tags remaining in output file: 0
- IGNW tags in output file: 16
- WATH. sanity check: ✓ PASSED (no occurrences found)
- Conversion status: ✓ Complete

**Tag Format Transformation:**
- iFIX formats: 
  - JSON: `"tag" : "WATH.[server].[tag_path]"` 
  - XML queryText: `Tag[number]:WATH.[server].[tag_path]:[parameters]`
- Ignition formats:
  - JSON: `"tag" : "IGNW.[formatted_path]"` (forward slashes replaced with dashes)
  - XML queryText: `Tag[number]:IGNW.[formatted_path]:[parameters]` (forward slashes replaced with dashes)

All tag paths were successfully validated against the lookup table and converted according to the specified transformation rules.
