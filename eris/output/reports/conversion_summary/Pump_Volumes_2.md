# Report Conversion Summary: Pump_Volumes_2.rptdesign

**Conversion Date:** February 20, 2026 01:35 PM
**Original File:** `eris/input/reports/Pump_Volumes_2.rptdesign`
**Converted File:** `eris/output/reports/completed/Pump_Volumes_2.rptdesign`

## Conversion Statistics

- Total unique iFIX tags found: 58
- Total tag instances replaced: 174
- All tags successfully matched: OK

## Tag Mappings

| iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
|---------------|----------------------------|----------------------------|-------------------|
| WATH.MTPSVR1.HVLRWL01FI01QFL.F_CV | Hidden Valley/HVL_PLC01/RWL01_FI01/QFL | IGNW.hidden_valley-hvl_plc01-rwl01_fi01-qfl | See above |
| WATH.MTPSVR1.MTPBLE01FI01QFL.F_CV | MTP/MTP_PLCBL/BLE01_FI01/QFL | IGNW.mtp-mtp_plcbl-ble01_fi01-qfl | See above |
| WATH.MTPSVR1.MTPBLE02FI01QFL.F_CV | MTP/MTP_PLCBL/BLE02_FI01/QFL | IGNW.mtp-mtp_plcbl-ble02_fi01-qfl | See above |
| WATH.MTPSVR1.RW02RCW02FI01QFL.F_CV | ASR Wells/RCW2_PLC01/RCW02_FI01/QFL | IGNW.asr_wells-rcw2_plc01-rcw02_fi01-qfl | See above |
| WATH.MTPSVR1.RW02RCW02FIWAQFL.F_CV | ASR Wells/RCW2_PLC01/RCW02_FIWA/QFL | IGNW.asr_wells-rcw2_plc01-rcw02_fiwa-qfl | See above |
| WATH.MTPSVR1.RW02RCW04FI01QFL.F_CV | ASR Wells/RCW2_PLC01/RCW04_FI01/QFL | IGNW.asr_wells-rcw2_plc01-rcw04_fi01-qfl | See above |
| WATH.MTPSVR1.RW02RCW04FIWAQFL.F_CV | ASR Wells/RCW2_PLC01/RCW04_FIWA/QFL | IGNW.asr_wells-rcw2_plc01-rcw04_fiwa-qfl | See above |
| WATH.MTPSVR1.SR01ASR01FI01QFL.F_CV | ASR Wells/ASR1_PLC01/ASR01_FI01/QFL | IGNW.asr_wells-asr1_plc01-asr01_fi01-qfl | See above |
| WATH.MTPSVR1.SR01ASR01FI02QFL.F_CV | ASR Wells/ASR1_PLC01/ASR01_FI02/QFL | IGNW.asr_wells-asr1_plc01-asr01_fi02-qfl | See above |
| WATH.MTPSVR1.SR01ASR01FIWAQFL.F_CV | ASR Wells/ASR1_PLC01/ASR01_FIWA/QFL | IGNW.asr_wells-asr1_plc01-asr01_fiwa-qfl | See above |
| ... (48 more rows) | ... | ... | ... |

## Conversion Details

Successfully converted all 174 instances of 58 unique iFIX tag paths to their Ignition equivalents.

**Verification:**
- Data WATH tags remaining in output file: 0
- IGNW tags in output file: 174
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
