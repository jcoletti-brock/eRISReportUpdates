# Tag Calculation Conversion Mismatch Summary: CalcsConfigExport.json

**Analysis Date:** February 20, 2026 04:56 PM
**Original File:** `eris\input\tagcalcs\CalcsConfigExport.json`
**Status:** STOP - Conversion Not Possible - Missing Lookup Entries

## Tag Analysis Statistics

- Total unique iFIX tags found: 157
- Tags matched in lookup: 136
- Tags NOT matched in lookup: 21
- Match rate: 86.6%

## Tags NOT Found in Lookup

The following iFIX tags were found in calculations but do NOT have entries in the lookup table:

| iFIX Tag (without WATH. prefix) | Full Tag Path |
|--------------------------------|------------------|
| MTPSVR1.HVLRWL1FIQ01 | WATH.MTPSVR1.HVLRWL1FIQ01.F_CV |
| MTPSVR1.KIWK093FIQ01 | WATH.MTPSVR1.KIWK093FIQ01.F_CV |
| MTPSVR1.KIWK094FIQ01 | WATH.MTPSVR1.KIWK094FIQ01.F_CV |
| MTPSVR1.MTPFL01FIQ01 | WATH.MTPSVR1.MTPFL01FIQ01.F_CV |
| MTPSVR1.MTPFL01NIQ01 | WATH.MTPSVR1.MTPFL01NIQ01.F_CV |
| MTPSVR1.MTPFL02FIQ01 | WATH.MTPSVR1.MTPFL02FIQ01.F_CV |
| MTPSVR1.MTPFL02NIQ01 | WATH.MTPSVR1.MTPFL02NIQ01.F_CV |
| MTPSVR1.MTPFL03FIQ01 | WATH.MTPSVR1.MTPFL03FIQ01.F_CV |
| MTPSVR1.MTPFL03NIQ01 | WATH.MTPSVR1.MTPFL03NIQ01.F_CV |
| MTPSVR1.MTPFL04FIQ01 | WATH.MTPSVR1.MTPFL04FIQ01.F_CV |
| MTPSVR1.MTPFL04NIQ01 | WATH.MTPSVR1.MTPFL04NIQ01.F_CV |
| MTPSVR2.ATPWELLFXQ01 | WATH.MTPSVR2.ATPWELLFXQ01.F_CV |
| MTPSVR2.CBWG016FIQ01 | WATH.MTPSVR2.CBWG016FIQ01.F_CV |
| MTPSVR2.CBWG018FIQ01 | WATH.MTPSVR2.CBWG018FIQ01.F_CV |
| MTPSVR2.MDPWELLFXQ01 | WATH.MTPSVR2.MDPWELLFXQ01.F_CV |
| MTPSVR3.GBPKB00FIQ01 | WATH.MTPSVR3.GBPKB00FIQ01.F_CV |
| MTPSVR3.GBPRES1FIQ01 | WATH.MTPSVR3.GBPRES1FIQ01.F_CV |
| MTPSVR3.KIWK050FXQ01 | WATH.MTPSVR3.KIWK050FXQ01.F_CV |
| MTPSVR3.PKPK031FIQ01 | WATH.MTPSVR3.PKPK031FIQ01.F_CV |
| MTPSVR3.PKPK032FIQ01 | WATH.MTPSVR3.PKPK032FIQ01.F_CV |
| MTPSVR3.PKPK033FIQ01 | WATH.MTPSVR3.PKPK033FIQ01.F_CV |

## Tags Successfully Matched (sample)

The following iFIX tags were found in both the file and the lookup table:

| iFIX Tag Path | Instances |
|---|---|
| WATH.MTPSVR1.M6PRES03LI01QVA.F_CV | 1 |
| WATH.MTPSVR1.M6PRES04LI01QVA.F_CV | 1 |
| WATH.MTPSVR1.M6PRES05LI01QVA.F_CV | 1 |
| WATH.MTPSVR1.MTRTWR1LIQ01.F_CV | 1 |
| WATH.MTPSVR1.MTRTWR2LIQ01.F_CV | 1 |
| WATH.MTPSVR3.ERRRES1LIQ01.F_CV | 1 |
| WATH.MTPSVR3.FPTETK1LIQ01.F_CV | 1 |
| WATH.MTPSVR3.GBPTWR1LIQ01.F_CV | 1 |
| WATH.MTPSVR3.GBPTWR2LIQ01.F_CV | 1 |
| WATH.MTPSVR3.K34TWR01LI01QVA.F_CV | 1 |
| WATH.MTPSVR3.LATETK1LIQ01.F_CV | 1 |
| WATH.MTPSVR3.PKPRES1LIQ01.F_CV | 1 |
| WATH.MTPSVR3.WSPRES1LIQ01.F_CV | 1 |
| WATH.MTPSVR3.Z6TETK1LIQ01.F_CV | 1 |

## Required Action

The lookup table at `src\ifix_to_ign_2026_02_19.csv` must be updated with the missing iFIX tag entries before this file can be converted.

Add entries to the lookup table for all 21 tags listed in the "Tags NOT Found in Lookup" section above. Each entry should include:
- `hist_tagname`: The iFIX tag name (without WATH. prefix)
- `ign_tagprovider`: The Ignition tag provider
- `ign_tagname`: The corresponding Ignition tag path
- `ign_fullpath`: The full Ignition tag path
- `imaginary`: Whether the tag is imaginary (true/false)

After updating the lookup table, re-run the conversion process for this file.
