# Report Conversion Summary: WELL_RUNTIMES - WATH.rptdesign

**Conversion Date:** February 20, 2026 01:35 PM
**Original File:** `eris/input/reports/WELL_RUNTIMES - WATH.rptdesign`
**Converted File:** `eris/output/reports/completed/WELL_RUNTIMES - WATH.rptdesign`

## Conversion Statistics

- Total unique iFIX tags found: 43
- Total tag instances replaced: 129
- All tags successfully matched: OK

## Tag Mappings

| iFIX Tag Path | Ignition Tag Name (Lookup) | Formatted Ignition Tag Path | Instances Replaced |
|---------------|----------------------------|----------------------------|-------------------|
| WATH.MTPSVR1.K21W00210000QRN.F_CV | Kitchener/Wells/K21_PLC01/W0021_0000/QRN | IGNW.kitchener-wells-k21_plc01-w0021_0000-qrn | See above |
| WATH.MTPSVR1.K21W021A0000QRN.F_CV | Kitchener/Wells/K21_PLC01/W021A_0000/QRN | IGNW.kitchener-wells-k21_plc01-w021a_0000-qrn | See above |
| WATH.MTPSVR1.K25W00250000QRN.F_CV | Kitchener/Wells/K25_PLC01/W0025_0000/QRN | IGNW.kitchener-wells-k25_plc01-w0025_0000-qrn | See above |
| WATH.MTPSVR1.K29W00290000QRN.F_CV | Kitchener/Wells/K29_PLC01/W0029_0000/QRN | IGNW.kitchener-wells-k29_plc01-w0029_0000-qrn | See above |
| WATH.MTPSVR1.K91W00910000QRN.F_CV | Kitchener/Wells/K91_PLC01/W0091_0000/QRN | IGNW.kitchener-wells-k91_plc01-w0091_0000-qrn | See above |
| WATH.MTPSVR1.K91W00920000QRN.F_CV | Kitchener/Wells/K91_PLC01/W0092_0000/QRN | IGNW.kitchener-wells-k91_plc01-w0092_0000-qrn | See above |
| WATH.MTPSVR1.K93W00930000QRN.F_CV | Kitchener/Wells/K93_PLC01/W0093_0000/QRN | IGNW.kitchener-wells-k93_plc01-w0093_0000-qrn | See above |
| WATH.MTPSVR1.K93W00940000QRN.F_CV | Kitchener/Wells/K93_PLC01/W0094_0000/QRN | IGNW.kitchener-wells-k93_plc01-w0094_0000-qrn | See above |
| WATH.MTPSVR2.APSW00030000QRN.F_CV | APS_PLC01/W0003_0000/QRN | IGNW.aps_plc01-w0003_0000-qrn | See above |
| WATH.MTPSVR2.ATPW00010000QRN.F_CV | ATP_PLC01/W0001_0000/QRN | IGNW.atp_plc01-w0001_0000-qrn | See above |
| ... (33 more rows) | ... | ... | ... |

## Conversion Details

Successfully converted all 129 instances of 43 unique iFIX tag paths to their Ignition equivalents.

**Verification:**
- Data WATH tags remaining in output file: 0
- IGNW tags in output file: 129
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
