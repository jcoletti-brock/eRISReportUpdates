# Report Conversion Mismatch Summary: Daily Flow Check - IUS 5-9 v01E.rptdesign

**Analysis Date:** February 18, 2026 03:05 PM
**Original File:** `eris\input\reports\Daily Flow Check - IUS 5-9 v01E.rptdesign`
**Status:** Conversion Not Possible - Missing Lookup Entries

## Tag Analysis Statistics

- Total unique iFIX tags found: 39
- Tags matched in lookup: 18
- Tags NOT matched in lookup: 21
- Match rate: 46.2%

## Tags NOT Found in Lookup

The following iFIX tags were found in the report but do NOT have entries in the lookup table:

| iFIX Tag (without WATH. prefix) | Full Tag Path in Report | Instances Found |
|--------------------------------|------------------------|----------------|
| MTPSVR1.KIWK021TT.F_CV | WATH.MTPSVR1.KIWK021TT.F_CV | 1 |
| MTPSVR1.KIWK025TT.F_CV | WATH.MTPSVR1.KIWK025TT.F_CV | 1 |
| MTPSVR1.KIWK029TT.F_CV | WATH.MTPSVR1.KIWK029TT.F_CV | 1 |
| MTPSVR1.KIWK091TT.F_CV | WATH.MTPSVR1.KIWK091TT.F_CV | 1 |
| MTPSVR1.KIWK092TT.F_CV | WATH.MTPSVR1.KIWK092TT.F_CV | 1 |
| MTPSVR1.KIWK093TT.F_CV | WATH.MTPSVR1.KIWK093TT.F_CV | 1 |
| MTPSVR1.KIWK094TT.F_CV | WATH.MTPSVR1.KIWK094TT.F_CV | 1 |
| MTPSVR1.MTRTWL1TT.F_CV | WATH.MTPSVR1.MTRTWL1TT.F_CV | 1 |
| MTPSVR2.CBWG009FIQ01.F_CV | WATH.MTPSVR2.CBWG009FIQ01.F_CV | 1 |
| MTPSVR2.MDPCB00TTV01.F_CV | WATH.MTPSVR2.MDPCB00TTV01.F_CV | 1 |
| MTPSVR2.TTPTWL1TT.F_CV | WATH.MTPSVR2.TTPTWL1TT.F_CV | 1 |
| MTPSVR3.GBPK008TT.F_CV | WATH.MTPSVR3.GBPK008TT.F_CV | 1 |
| MTPSVR3.GBPK01ATTV01.F_CV | WATH.MTPSVR3.GBPK01ATTV01.F_CV | 1 |
| MTPSVR3.GBPK02ATTV01.F_CV | WATH.MTPSVR3.GBPK02ATTV01.F_CV | 1 |
| MTPSVR3.GBPK05ATT.F_CV | WATH.MTPSVR3.GBPK05ATT.F_CV | 1 |
| MTPSVR3.GBPKB00TT.F_CV | WATH.MTPSVR3.GBPKB00TT.F_CV | 1 |
| MTPSVR3.GBPRWT1TT.F_CV | WATH.MTPSVR3.GBPRWT1TT.F_CV | 1 |
| MTPSVR3.HRMMV02TT.F_CV | WATH.MTPSVR3.HRMMV02TT.F_CV | 1 |
| MTPSVR3.KIWK023TT.F_CV | WATH.MTPSVR3.KIWK023TT.F_CV | 1 |
| MTPSVR3.KIWK050TT.F_CV | WATH.MTPSVR3.KIWK050TT.F_CV | 1 |
| MTPSVR3.KIWK051TT.F_CV | WATH.MTPSVR3.KIWK051TT.F_CV | 1 |

## Tags Successfully Matched

The following iFIX tags were found in both the report and the lookup table:

| iFIX Tag Path | Ignition Tag Name (Lookup) | Instances Found |
|---------------|----------------------------|----------------|
| WATH.MTPSVR2.CBWG004FIQ01.F_CV | Cambridge/Galt Wells/G04_PLC01/CBW_G004_FI01/QVA | 1 |
| WATH.MTPSVR2.G05TWL01FI01QFL.F_CV | Cambridge/Galt Wells/G05_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR2.H03TWL01FI01QFL.F_CV | Cambridge/Hespeler Wells/H03_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR2.H04TWL01FI01QFL.F_CV | Cambridge/Hespeler Wells/H04_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR2.H05TWL01FI01QVA.F_CV | Cambridge/Hespeler Wells/H05_PLC01/TWL01_FI01/QVA | 1 |
| WATH.MTPSVR2.MDPRES0TTV01.F_CV | MDP_PLC01/MDPRES0TTV01 | 1 |
| WATH.MTPSVR2.PTPTWL01FI01QFL.F_CV | Cambridge/PTP_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR2.RAPTWL01FI01QFL.F_CV | Cambridge/RAP_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR2.STPTWL01FI01QFL.F_CV | Cambridge/STP_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR3.K24TWL01FI01QFL.F_CV | Kitchener/Wells/K24_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR3.K26W0026FI01QFL.F_CV | Kitchener/Wells/K26_PLC01/W0026_FI01/QFL | 1 |
| WATH.MTPSVR3.K34TWL01FI01QFL.F_CV | Kitchener/Wells/K34_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR3.K34W000XFI01QFL.F_CV | Kitchener/Wells/K34_PLC01/W000X_FI01/QFL | 1 |
| WATH.MTPSVR3.KIWOL02TT.F_CV | Kitchener/Wells/K50_PLC01/KIWOL02TT | 1 |
| WATH.MTPSVR3.MV3VCH03FI01QFL.F_CV | Waterloo/MV3_PLC01/VCH03_FI01/QFL | 1 |
| WATH.MTPSVR3.PKPTWL01FI01QFL.F_CV | Kitchener/PKP_PLC01/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR3.SSPTWL01FI01QFL.F_CV | Kitchener/Strange St/SSP_PLC03/TWL01_FI01/QFL | 1 |
| WATH.MTPSVR3.Z6TETK01FI03QFL.F_CV | Kitchener/Z6T_PLC01/ETK01_FI03/QFL | 1 |

## Required Action

**The lookup table at `src\ifix_to_ign_010152026.csv` must be updated with the missing iFIX tag entries before this report can be converted.**

Add entries to the lookup table for all tags listed in the "Tags NOT Found in Lookup" section above. Each entry should include:
- `hist_tagname`: The iFIX tag name (without WATH. prefix)
- `ign_tagprovider`: The Ignition tag provider
- `ign_tagname`: The corresponding Ignition tag path
- `ign_fullpath`: The full Ignition tag path
- `imaginary`: Whether the tag is imaginary (true/false)

After updating the lookup table, re-run the conversion process for this report.
