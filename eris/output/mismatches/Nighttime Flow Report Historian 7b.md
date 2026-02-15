# Report Conversion Mismatch Summary: Nighttime Flow Report Historian 7b.rptdesign

**Analysis Date:** February 15, 2026 12:43 AM
**Original File:** `eris\input\reports\Nighttime Flow Report Historian 7b.rptdesign`
**Status:** X Conversion Not Possible - Missing Lookup Entries

## Tag Analysis Statistics

- Total unique iFIX tags found: 6
- Tags matched in lookup: 4
- Tags NOT matched in lookup: 2
- Match rate: 66.7%

## Tags NOT Found in Lookup

The following iFIX tags were found in the report but do NOT have entries in the lookup table:

| iFIX Tag (without WATH. prefix) | Full Tag Path in Report | Instances Found |
|--------------------------------|------------------------|----------------|
| MTPSVR2.LINTWL1FIQ01_00_04 | ET.WATH.MTPSVR2.LINTWL1FIQ01_00_04 | 1 |
| MTPSVR2.LINTWL1FIQ01_06_10 | ET.WATH.MTPSVR2.LINTWL1FIQ01_06_10 | 1 |

## Tags Successfully Matched

The following iFIX tags were found in both the report and the lookup table:

| iFIX Tag Path | Ignition Tag Name (Lookup) | Instances Found |
|---------------|----------------------------|----------------|
| WATH.MTPSVR2.BMSTWL01FI01QYF.F_CV | BMS_PLC01/TWL01_FI01/QYF | 1 |
| WATH.MTPSVR2.LBMIL001FI01QFL.F_CV | Rural/North Dumfries/LBM_PLC01/IL001_FI01/QFL | 1 |
| WATH.MTPSVR2.LINTWL01FI01QFL.F_CV | LIN_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR2.WMHTWL01FI01QFL.F_CV | Rural/Woolwich/WMH_PLC01/TWL01_FI01/QFL | 1 |

## Required Action

**The lookup table at `src\ifix_to_ign_010152026.csv` must be updated with the missing iFIX tag entries before this report can be converted.**

Add entries to the lookup table for all tags listed in the "Tags NOT Found in Lookup" section above. Each entry should include:
- `hist_tagname`: The iFIX tag name (without WATH. prefix)
- `ign_tagprovider`: The Ignition tag provider
- `ign_tagname`: The corresponding Ignition tag path
- `ign_fullpath`: The full Ignition tag path
- `imaginary`: Whether the tag is imaginary (true/false)

After updating the lookup table, re-run the conversion process for this report.

## Notes

The ET.WATH tags are pre-computed/engineered tags that were not found in the lookup table. These need to be added before conversion can proceed.
