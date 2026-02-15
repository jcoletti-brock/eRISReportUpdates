# Report Conversion Mismatch Summary: Daily Flow Check - Rural v6G.rptdesign

**Analysis Date:** February 14, 2026 11:25 PM
**Original File:** `eris\input\reports\Daily Flow Check - Rural v6G.rptdesign`
**Status:** X Conversion Not Possible - Missing Lookup Entries

## Tag Analysis Statistics

- Total unique iFIX tags found: 47
- Tags matched in lookup: 27
- Tags NOT matched in lookup: 20
- Match rate: 57.4%

## Tags NOT Found in Lookup

The following iFIX tags were found in the report but do NOT have entries in the lookup table:

| iFIX Tag (without WATH. prefix) | Full Tag Path in Report | Instances Found |
|--------------------------------|------------------------|----------------|
| MTPSVR2.ATPA001TT.F_CV | WATH.MTPSVR2.ATPA001TT.F_CV | 1 |
| MTPSVR2.ATPA002TT.F_CV | WATH.MTPSVR2.ATPA002TT.F_CV | 1 |
| MTPSVR2.ATPA003TT.F_CV | WATH.MTPSVR2.ATPA003TT.F_CV | 1 |
| MTPSVR2.ATPTWL1TT.F_CV | WATH.MTPSVR2.ATPTWL1TT.F_CV | 1 |
| MTPSVR2.CPSIL001FIQYF.F_CV | WATH.MTPSVR2.CPSIL001FIQYF.F_CV | 1 |
| MTPSVR2.LBMIL01TT.F_CV | WATH.MTPSVR2.LBMIL01TT.F_CV | 1 |
| MTPSVR2.LINW0001FI01QFL.F_CV | WATH.MTPSVR2.LINW0001FI01QFL.F_CV | 1 |
| MTPSVR2.SJPIL01TT.F_CV | WATH.MTPSVR2.SJPIL01TT.F_CV | 1 |
| MTPSVR2.SJPOL02TT.F_CV | WATH.MTPSVR2.SJPOL02TT.F_CV | 1 |
| MTPSVR2.SJPSJB0T2.F_CV | WATH.MTPSVR2.SJPSJB0T2.F_CV | 1 |
| MTPSVR2.SJPSJB0TT.F_CV | WATH.MTPSVR2.SJPSJB0TT.F_CV | 1 |
| MTPSVR2.STCSC02TT.F_CV | WATH.MTPSVR2.STCSC02TT.F_CV | 1 |
| MTPSVR2.STCSC03TT.F_CV | WATH.MTPSVR2.STCSC03TT.F_CV | 1 |
| MTPSVR2.STCSC04TT.F_CV | WATH.MTPSVR2.STCSC04TT.F_CV | 1 |
| MTPSVR2.STCSCB0TT.F_CV | WATH.MTPSVR2.STCSCB0TT.F_CV | 1 |
| MTPSVR3.BLMVCH1TTV01.F_CV | WATH.MTPSVR3.BLMVCH1TTV01.F_CV | 1 |
| MTPSVR3.FGSFG01TT.F_CV | WATH.MTPSVR3.FGSFG01TT.F_CV | 1 |
| MTPSVR3.FGSFGB0TT.F_CV | WATH.MTPSVR3.FGSFGB0TT.F_CV | 1 |
| MTPSVR3.NHPTWL0FI01QYF.F_CV | WATH.MTPSVR3.NHPTWL0FI01QYF.F_CV | 1 |
| MTPSVR3.NHWNH03TT.F_CV | WATH.MTPSVR3.NHWNH03TT.F_CV | 1 |

## Tags Successfully Matched

The following iFIX tags were found in both the report and the lookup table:

| iFIX Tag Path | Ignition Tag Name (Lookup) | Instances Found |
|---------------|----------------------------|----------------|
| WATH.MTPSVR2.BMSTWL01FI01QYF.F_CV | BMS_PLC01/TWL01_FI01/QYF | 1 |
| WATH.MTPSVR2.BMSW0002FI01QYF.F_CV | BMS_PLC01/W0002_FI01/QYF | 1 |
| WATH.MTPSVR2.BMSW0003FI01QYF.F_CV | BMS_PLC01/W0003_FI01/QYF | 1 |
| WATH.MTPSVR2.CBVVCH01FI01QFL.F_CV | Rural/Woolwich/CBV_PLC01/VCH01_FI01/QFL | 1 |
| WATH.MTPSVR2.CGSC005TT.F_CV | Rural/Woolwich/CGS_PLC01/CGSC005TT | 1 |
| WATH.MTPSVR2.CGSC006TT.F_CV | Rural/Woolwich/CGS_PLC01/CGSC006TT | 1 |
| WATH.MTPSVR2.CGSCNB0TT.F_CV | Rural/Woolwich/CGS_PLC01/CGSCNB0TT | 2 |
| WATH.MTPSVR2.HEMVCH01FI01QFL.F_CV | Rural/Wellesley/HEM_PLC01/VCH01_FI01/QFL | 1 |
| WATH.MTPSVR2.HEPTWL1TT.F_CV | Rural/Wellesley/HEP_PLC01/HEPTWL1TT | 1 |
| WATH.MTPSVR2.LINTWL01FI01QFL.F_CV | LIN_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR2.LINW0002FI01QFL.F_CV | LIN_PLC01/W0002_FI01/QFL | 1 |
| WATH.MTPSVR2.MVPTWL01FI01QFL.F_CV | MVP_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR2.MVPW0005FI01QFL.F_CV | MVP_PLC01/W0005_FI01/QFL | 1 |
| WATH.MTPSVR2.MVPW004AFI01QFL.F_CV | MVP_PLC01/W004A_FI01/QFL | 1 |
| WATH.MTPSVR2.MYPTWL01FI01QFL.F_CV | Rural/Woolwich/MYP_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR2.MYPW0001FI01QFL.F_CV | Rural/Woolwich/MYP_PLC01/W0001_FI01/QFL | 1 |
| WATH.MTPSVR2.MYPW0002FI01QFL.F_CV | Rural/Woolwich/MYP_PLC01/W0002_FI01/QFL | 1 |
| WATH.MTPSVR2.WHPTWL01FI01QFL.F_CV | WHP_PLC01/TWL01_FI01/QFL | 2 |
| WATH.MTPSVR2.WHPW0005FI01QFL.F_CV | WHP_PLC01/W0005_FI01/QFL | 1 |
| WATH.MTPSVR2.WHPW0006FI01QFL.F_CV | WHP_PLC01/W0006_FI01/QFL | 1 |
| WATH.MTPSVR2.WMHTWL1FIQ02.F_CV | Rural/Woolwich/WMH_PLC01/WMHTWL1FIQ02 | 1 |
| WATH.MTPSVR2.WMHWM00FIQ02.F_CV | Rural/Woolwich/WMH_PLC01/WMHWM00FIQ02 | 1 |
| WATH.MTPSVR3.NDPTWL01FI01QFL.F_CV | NDP_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR3.NDPW0004FI01QFL.F_CV | NDP_PLC01/W0004_FI01/QFL | 1 |
| WATH.MTPSVR3.NDPW0005FI01QFL.F_CV | NDP_PLC01/W0005_FI01/QFL | 1 |
| WATH.MTPSVR3.STAVCH01FI01QFL.F_CV | Rural/Wilmot/STA_PLC01/VCH01_FI01/QFL | 1 |
| WATH.MTPSVR3.VIMVCH01FI01QYF.F_CV | Kitchener/VIM_PLC01/VCH01_FI01/QYF | 1 |

## Required Action

**The lookup table at `src\ifix_to_ign_010152026.csv` must be updated with the missing iFIX tag entries before this report can be converted.**

Add entries to the lookup table for all tags listed in the "Tags NOT Found in Lookup" section above. Each entry should include:
- `hist_tagname`: The iFIX tag name (without WATH. prefix)
- `ign_tagprovider`: The Ignition tag provider
- `ign_tagname`: The corresponding Ignition tag path
- `ign_fullpath`: The full Ignition tag path
- `Imaginary`: Whether the tag is imaginary (true/false)

After updating the lookup table, re-run the conversion process for this report.
