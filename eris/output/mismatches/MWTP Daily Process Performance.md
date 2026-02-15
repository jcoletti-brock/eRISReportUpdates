# Report Conversion Mismatch Summary: MWTP Daily Process Performance.rptdesign

**Analysis Date:** February 15, 2026 12:32 AM
**Original File:** `eris\input\reports\MWTP Daily Process Performance.rptdesign`
**Status:** X Conversion Not Possible - Missing Lookup Entries

## Tag Analysis Statistics

- Total unique iFIX tags found: 109
- Tags matched in lookup: 104
- Tags NOT matched in lookup: 5
- Match rate: 95.4%

## Tags NOT Found in Lookup

The following iFIX tags were found in the report but do NOT have entries in the lookup table:

| iFIX Tag (without WATH. prefix) | Full Tag Path in Report | Instances Found |
|--------------------------------|------------------------|----------------|
| MTPSVR1.MTPBLE1TT.F_CV | WATH.MTPSVR1.MTPBLE1TT.F_CV | 3 |
| MTPSVR1.MTPBLE2TT.F_CV | WATH.MTPSVR1.MTPBLE2TT.F_CV | 3 |
| MTPSVR1.SR00ASR00FI01QFL.F_CV | WATH.MTPSVR1.SR00ASR00FI01QFL.F_CV | 3 |
| MTPSVR1.SR00ASR00FI02QFL.F_CV | WATH.MTPSVR1.SR00ASR00FI02QFL.F_CV | 3 |
| MTPSVR1.SR00ASR00FIWAQFL.F_CV | WATH.MTPSVR1.SR00ASR00FIWAQFL.F_CV | 3 |

## Tags Successfully Matched

The following iFIX tags were found in both the report and the lookup table:

| iFIX Tag Path | Ignition Tag Name (Lookup) | Instances Found |
|---------------|----------------------------|----------------|
| WATH.MTPSVR1.HVLRWB00CE01QVA.F_CV | Hidden Valley/HVL_PLC01/RWB00_CE01/QVA | 3 |
| WATH.MTPSVR1.HVLRWB00DO01QVA.F_CV | Hidden Valley/HVL_PLC01/RWB00_DO01/QVA | 3 |
| WATH.MTPSVR1.HVLRWB00NI01QVA.F_CV | Hidden Valley/HVL_PLC01/RWB00_NI01/QVA | 3 |
| WATH.MTPSVR1.HVLRWB00PH01QVA.F_CV | Hidden Valley/HVL_PLC01/RWB00_PH01/QVA | 3 |
| WATH.MTPSVR1.HVLRWB00TI01QVA.F_CV | Hidden Valley/HVL_PLC01/RWB00_TI01/QVA | 3 |
| WATH.MTPSVR1.HVLRWL01FI01QFL.F_CV | Hidden Valley/HVL_PLC01/RWL01_FI01/QFL | 3 |
| WATH.MTPSVR1.MHRRES01LI01QVA.F_CV | MHR_PLC01/RES01_LI01/QVA | 3 |
| WATH.MTPSVR1.MHRRES02LI01QVA.F_CV | MHR_PLC01/RES02_LI01/QVA | 3 |
| WATH.MTPSVR1.MOZOCT01ON01QVA.F_CV | MOZ_PLC01/OCT01_ON01/QVA | 3 |
| WATH.MTPSVR1.MOZOCT01ON02QVA.F_CV | MOZ_PLC01/OCT01_ON02/QVA | 3 |
| WATH.MTPSVR1.MOZOCT02ON01QVA.F_CV | MOZ_PLC01/OCT02_ON01/QVA | 3 |
| WATH.MTPSVR1.MOZOCT02ON02QVA.F_CV | MOZ_PLC01/OCT02_ON02/QVA | 3 |
| WATH.MTPSVR1.MOZOZG00FV12VSO.F_CV | MOZ_PLC01/OZG00_FV12_VSO | 3 |
| WATH.MTPSVR1.MOZOZG00FV34VSO.F_CV | MOZ_PLC01/OZG00_FV34_VSO | 3 |
| WATH.MTPSVR1.MTPASB0XFI01QVA.F_CV | MTP/MTP_PLCFL/ASB0X_FI01/QVA | 3 |
| WATH.MTPSVR1.MTPBLE01FI01QFL.F_CV | MTP/MTP_PLCBL/BLE01_FI01/QFL | 3 |
| WATH.MTPSVR1.MTPBLE02FI01QFL.F_CV | MTP/MTP_PLCBL/BLE02_FI01/QFL | 3 |
| WATH.MTPSVR1.MTPBWP0XFI01QFL.F_CV | MTP/MTP_PLCFL/BWP0X_FI01/QFL | 3 |
| WATH.MTPSVR1.MTPCLC0X0000QVA.F_CV | MTP/MTP_PLCCL/CLC0X_0000/QVA | 3 |
| WATH.MTPSVR1.MTPCMT01LI01QVA.F_CV | MTP/MTP_PLCBL/CMT01_LI01/QVA | 3 |
| ... (84 more matched tags) | ... | ... |

## Required Action

**The lookup table at `src\ifix_to_ign_010152026.csv` must be updated with the missing iFIX tag entries before this report can be converted.**

Add entries to the lookup table for all tags listed in the "Tags NOT Found in Lookup" section above. Each entry should include:
- `hist_tagname`: The iFIX tag name (without WATH. prefix)
- `ign_tagprovider`: The Ignition tag provider
- `ign_tagname`: The corresponding Ignition tag path
- `ign_fullpath`: The full Ignition tag path
- `imaginary`: Whether the tag is imaginary (true/false)

After updating the lookup table, re-run the conversion process for this report.
