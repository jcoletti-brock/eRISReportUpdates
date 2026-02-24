# Report Conversion Mismatch Summary: Consumption - Index for IUS Kit.rptdesign

**Analysis Date:** February 18, 2026 02:50 PM
**Original File:** `eris\input\reports\Consumption - Index for IUS Kit.rptdesign`
**Status:** X Conversion Not Possible - Missing Lookup Entries

## Tag Analysis Statistics

- Total unique iFIX tags found: 29
- Tags matched in lookup: 28
- Tags NOT matched in lookup: 1
- Match rate: 96.6%

## Tags NOT Found in Lookup

The following iFIX tags were found in the report but do NOT have entries in the lookup table:

| iFIX Tag (without WATH. prefix) | Full Tag Path in Report | Instances Found |
|--------------------------------|------------------------|----------------|
| MTPSVR3.K50VCH01FI03QFL.F_CV | WATH.MTPSVR3.K50VCH01FI03QFL.F_CV | 3 |

## Tags Successfully Matched

The following iFIX tags were found in both the report and the lookup table:

| iFIX Tag Path | Ignition Tag Name (Lookup) | Instances Found |
|---------------|----------------------------|----------------|
| WATH.MTPSVR1.K21W000XFI01QFL.F_CV | Kitchener/Wells/K21_PLC01/W000X_FI01/QFL | 3 |
| WATH.MTPSVR1.K25TWL01FI01QFL.F_CV | Kitchener/Wells/K25_PLC01/TWL01_FI01/QFL | 3 |
| WATH.MTPSVR1.K29TWL01FI01QFL.F_CV | Kitchener/Wells/K29_PLC01/TWL01_FI01/QFL | 3 |
| WATH.MTPSVR1.K91W0091FI01QFL.F_CV | Kitchener/Wells/K91_PLC01/W0091_FI01/QFL | 3 |
| WATH.MTPSVR1.K91W0092FI01QFL.F_CV | Kitchener/Wells/K91_PLC01/W0092_FI01/QFL | 3 |
| WATH.MTPSVR1.K93W0093FI01QFL.F_CV | Kitchener/Wells/K93_PLC01/W0093_FI01/QFL | 3 |
| WATH.MTPSVR1.K93W0094FI01QFL.F_CV | Kitchener/Wells/K93_PLC01/W0094_FI01/QFL | 3 |
| WATH.MTPSVR1.MTPTWL01FI01QFL.F_CV | MTP/MTP_PLCPD/TWL01_FI01/QFL | 3 |
| WATH.MTPSVR3.BLMVCH01FI01QFL.F_CV | Kitchener/BLM_PLC01/VCH01_FI01/QFL | 3 |
| WATH.MTPSVR3.DRVVCH01FI01QFL.F_CV | Kitchener/DRV_PLC01/VCH01_FI01/QFL | 3 |
| WATH.MTPSVR3.FPMVCH01FI01QFL.F_CV | Kitchener/FPM_PLC01/VCH01_FI01/QFL | 3 |
| WATH.MTPSVR3.GBPTWL01FI01QFL.F_CV | Kitchener/Greenbrook/GBP_PLC01/TWL01_FI01/QFL | 3 |
| WATH.MTPSVR3.K23TWL01FI01QFL.F_CV | Kitchener/Wells/K23_PLC01/TWL01_FI01/QFL | 3 |
| WATH.MTPSVR3.K24TWL01FI01QFL.F_CV | Kitchener/Wells/K24_PLC01/TWL01_FI01/QFL | 3 |
| WATH.MTPSVR3.K26W0026FI01QFL.F_CV | Kitchener/Wells/K26_PLC01/W0026_FI01/QFL | 3 |
| WATH.MTPSVR3.K34TWL01FI01QFL.F_CV | Kitchener/Wells/K34_PLC01/TWL01_FI01/QFL | 3 |
| WATH.MTPSVR3.K50VCH01FI0XQFL.F_CV | Kitchener/Wells/K50_PLC01/VCH01_FI0X/QFL | 3 |
| WATH.MTPSVR3.K50W0050FI01QFL.F_CV | Kitchener/Wells/K50_PLC01/W0050_FI01/QFL | 3 |
| WATH.MTPSVR3.K50W0051FI01QFL.F_CV | Kitchener/Wells/K50_PLC01/W0051_FI01/QFL | 3 |
| WATH.MTPSVR3.MGMVCH01FI01QFL.F_CV | Kitchener/MGM_PLC01/VCH01_FI01/QFL | 3 |
| WATH.MTPSVR3.MV2VCH02FI01QFL.F_CV | Waterloo/MV2_PLC01/VCH02_FI01/QFL | 3 |
| WATH.MTPSVR3.MV3VCH03FI01QFL.F_CV | Waterloo/MV3_PLC01/VCH03_FI01/QFL | 3 |
| WATH.MTPSVR3.PKPTWL01FI01QFL.F_CV | Kitchener/PKP_PLC01/TWL01_FI01/QFL | 3 |
| WATH.MTPSVR3.SSPTWL01FI01QFL.F_CV | Kitchener/Strange St/SSP_PLC03/TWL01_FI01/QFL | 3 |
| WATH.MTPSVR3.VIMVCH01FI01QFL.F_CV | Kitchener/VIM_PLC01/VCH01_FI01/QFL | 3 |
| WATH.MTPSVR3.WBVVCH01FI01QFL.F_CV | Waterloo/WBV_PLC01/VCH01_FI01/QFL | 3 |
| WATH.MTPSVR3.WBVVCH01FI02QFL.F_CV | Waterloo/WBV_PLC01/VCH01_FI02/QFL | 3 |
| WATH.MTPSVR3.Z6TETK01FI03QFL.F_CV | Kitchener/Z6T_PLC01/ETK01_FI03/QFL | 3 |


## Required Action

**The lookup table at `src\ifix_to_ign_010152026.csv` must be updated with the missing iFIX tag entries before this report can be converted.**

Add entries to the lookup table for all tags listed in the "Tags NOT Found in Lookup" section above. Each entry should include:
- `hist_tagname`: The iFIX tag name (without WATH. prefix)
- `ign_tagprovider`: The Ignition tag provider
- `ign_tagname`: The corresponding Ignition tag path
- `ign_fullpath`: The full Ignition tag path
- `imaginary`: Whether the tag is imaginary (true/false)

After updating the lookup table, re-run the conversion process for this report.
