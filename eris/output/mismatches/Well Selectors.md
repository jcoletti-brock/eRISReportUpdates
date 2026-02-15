# Report Conversion Mismatch Summary: Well Selectors.rptdesign

**Analysis Date:** February 15, 2026 02:19 AM
**Original File:** `eris\input\reports\Well Selectors.rptdesign`
**Status:** ✗ Conversion Not Possible - Missing Lookup Entries

## Tag Analysis Statistics

- Total unique iFIX tags found: 12
- Tags matched in lookup: 11
- Tags NOT matched in lookup: 1
- Match rate: 91.7%

## Tags NOT Found in Lookup

The following iFIX tags were found in the report but do NOT have entries in the lookup table:

| iFIX Tag (without WATH. prefix) | Full Tag Path in Report | Instances Found |
|--------------------------------|------------------------|----------------|
| MTPSVR1.KIWOL03TT.F_CV | WATH.MTPSVR1.KIWOL03TT.F_CV | 3 |

## Tags Successfully Matched

The following iFIX tags were found in both the report and the lookup table:

| iFIX Tag Path | Ignition Tag Name (Lookup) | Instances Found |
|---------------|----------------------------|----------------|
| WATH.MTPSVR2.CBWG04A00SSE.F_CV | Cambridge/Galt Wells/G04_PLC01/CBWG04A00SSE | 6 |
| WATH.MTPSVR2.CBWH05ASWSRS.F_CV | Cambridge/Hespeler Wells/H05_PLC01/CBWH05ASWSRS | 3 |
| WATH.MTPSVR2.G05W00050000QRN.F_CV | Cambridge/Galt Wells/G05_PLC01/W0005_0000/QRN | 3 |
| WATH.MTPSVR2.G05W005A0000SSE.F_CV | Cambridge/Galt Wells/G05_PLC01/W005A_0000_SSE | 3 |
| WATH.MTPSVR2.H03W00030000QRN.F_CV | Cambridge/Hespeler Wells/H03_PLC01/W0003_0000/QRN | 3 |
| WATH.MTPSVR2.H03W003A0000SSE.F_CV | Cambridge/Hespeler Wells/H03_PLC01/W003A_0000_SSE | 6 |
| WATH.MTPSVR2.H05W00050000QRN.F_CV | Cambridge/Hespeler Wells/H05_PLC01/W0005_0000/QRN | 3 |
| WATH.MTPSVR2.H05W005A0000QRN.F_CV | Cambridge/Hespeler Wells/H05_PLC01/W005A_0000/QRN | 3 |
| WATH.MTPSVR3.NHWW00030000QRN.F_CV | NHW_PLC01/W0003_0000/QRN | 3 |
| WATH.MTPSVR3.NHWW00030000SRS.F_CV | NHW_PLC01/W0003_0000/SRS | 3 |
| WATH.MTPSVR3.NHWW00040000QRN.F_CV | NHW_PLC01/W0004_0000/QRN | 3 |

## Required Action

**The lookup table at `src\ifix_to_ign_010152026.csv` must be updated with the missing iFIX tag entries before this report can be converted.**

Add entries to the lookup table for all tags listed in the "Tags NOT Found in Lookup" section above. Each entry should include:
- `hist_tagname`: The iFIX tag name (without WATH. prefix)
- `ign_tagprovider`: The Ignition tag provider
- `ign_tagname`: The corresponding Ignition tag path
- `ign_fullpath`: The full Ignition tag path
- `imaginary`: Whether the tag is imaginary (true/false)

After updating the lookup table, re-run the conversion process for this report.
