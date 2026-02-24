# Report Conversion Mismatch Summary: Reservoir Levels Percentage.rptdesign

**Analysis Date:** February 18, 2026 03:36 PM
**Original File:** `eris\input\reports\Reservoir Levels Percentage.rptdesign`
**Status:** X Conversion Not Possible - Missing Lookup Entries

## Tag Analysis Statistics

- Total unique iFIX tags found: 14
- Tags matched in lookup: 5
- Tags NOT matched in lookup: 9
- Match rate: 35.7%

## Tags NOT Found in Lookup

The following iFIX tags were found in the report but do NOT have entries in the lookup table:

| iFIX Tag (without WATH. prefix) | Full Tag Path in Report | Instances Found |
|--------------------------------|------------------------|----------------|
| MTPSVR1.MTRTWR1LIQ01.F_CV | WATH.MTPSVR1.MTRTWR1LIQ01.F_CV | 3 |
| MTPSVR1.MTRTWR2LIQ01.F_CV | WATH.MTPSVR1.MTRTWR2LIQ01.F_CV | 3 |
| MTPSVR3.ERRRES1LIQ01.F_CV | WATH.MTPSVR3.ERRRES1LIQ01.F_CV | 3 |
| MTPSVR3.FPTETK1LIQ01.F_CV | WATH.MTPSVR3.FPTETK1LIQ01.F_CV | 3 |
| MTPSVR3.GBPTWR1LIQ01.F_CV | WATH.MTPSVR3.GBPTWR1LIQ01.F_CV | 3 |
| MTPSVR3.GBPTWR2LIQ01.F_CV | WATH.MTPSVR3.GBPTWR2LIQ01.F_CV | 3 |
| MTPSVR3.LATETK1LIQ01.F_CV | WATH.MTPSVR3.LATETK1LIQ01.F_CV | 3 |
| MTPSVR3.PKPRES1LIQ01.F_CV | WATH.MTPSVR3.PKPRES1LIQ01.F_CV | 3 |
| MTPSVR3.Z6TETK1LIQ01.F_CV | WATH.MTPSVR3.Z6TETK1LIQ01.F_CV | 3 |

## Tags Successfully Matched

The following iFIX tags were found in both the report and the lookup table:

| iFIX Tag Path | Ignition Tag Name (Lookup) | Instances Found |
|---------------|----------------------------|----------------|
| WATH.MTPSVR1.M6PRES03LI01QVA.F_CV | Z456/M6P_PLC01/RES03_LI01/QVA | 3 |
| WATH.MTPSVR1.M6PRES04LI01QVA.F_CV | Z456/M6P_PLC01/RES04_LI01/QVA | 3 |
| WATH.MTPSVR1.M6PRES05LI01QVA.F_CV | Z456/M6P_PLC01/RES05_LI01/QVA | 3 |
| WATH.MTPSVR3.K34TWR01LI01QVA.F_CV | Kitchener/Wells/K34_PLC01/TWR01_LI01/QVA | 3 |
| WATH.MTPSVR3.WSPRES1LIQ01.F_CV | Kitchener/WSP_PLC01/WSPRES1LIQ01 | 3 |

## Required Action

**The lookup table at `src\ifix_to_ign_010152026.csv` must be updated with the missing iFIX tag entries before this report can be converted.**

Add entries to the lookup table for all tags listed in the "Tags NOT Found in Lookup" section above. Each entry should include:
- `hist_tagname`: The iFIX tag name (without WATH. prefix)
- `ign_tagprovider`: The Ignition tag provider
- `ign_tagname`: The corresponding Ignition tag path
- `ign_fullpath`: The full Ignition tag path
- `imaginary`: Whether the tag is imaginary (true/false)

After updating the lookup table, re-run the conversion process for this report.
