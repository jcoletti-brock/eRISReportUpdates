# BIRT Report Conversion Summary

**Report:** Reservoir Levels Percentage.rptdesign  
**Conversion Type:** Partial Match  
**Date Generated:** 2026-02-20 14:00:06  

## Conversion Status

- **Total Unique Tags Found:** 14
- **Successfully Converted:** 5
- **Left Unchanged:** 9

## Transformation Rules Applied

| Rule | Transformation |
|------|-----------------|
| Prefix | Add IGNW. |
| Path Case | Lowercase |
| Forward Slash | / -> - |
| Spaces | space -> _ |
| Lab Replacement | :lab: -> :esrLab: |

## Successfully Converted Tags (5)

| iFIX (WATH) Tag | Ignition (IGNW) Tag |
|-----------------|---------------------|
| `WATH.MTPSVR1.M6PRES03LI01QVA.F_CV` | `IGNW.z456-m6p_plc01-res03_li01-qva` |
| `WATH.MTPSVR1.M6PRES04LI01QVA.F_CV` | `IGNW.z456-m6p_plc01-res04_li01-qva` |
| `WATH.MTPSVR1.M6PRES05LI01QVA.F_CV` | `IGNW.z456-m6p_plc01-res05_li01-qva` |
| `WATH.MTPSVR3.K34TWR01LI01QVA.F_CV` | `IGNW.kitchener-wells-k34_plc01-twr01_li01-qva` |
| `WATH.MTPSVR3.WSPRES1LIQ01.F_CV` | `IGNW.kitchener-wsp_plc01-wspres1liq01` |


## Tags Left Unchanged (9)

These tags were not found in the lookup CSV and remain as-is in the converted report:

- `WATH.MTPSVR1.MTRTWR1LIQ01.F_CV`
- `WATH.MTPSVR1.MTRTWR2LIQ01.F_CV`
- `WATH.MTPSVR3.ERRRES1LIQ01.F_CV`
- `WATH.MTPSVR3.FPTETK1LIQ01.F_CV`
- `WATH.MTPSVR3.GBPTWR1LIQ01.F_CV`
- `WATH.MTPSVR3.GBPTWR2LIQ01.F_CV`
- `WATH.MTPSVR3.LATETK1LIQ01.F_CV`
- `WATH.MTPSVR3.PKPRES1LIQ01.F_CV`
- `WATH.MTPSVR3.Z6TETK1LIQ01.F_CV`


## Notes

- This is a **partial conversion** - only matched tags from the CSV lookup were converted
- Unmatched WATH tags remain unchanged in the output file
- All `:lab:` prefixes have been globally replaced with `:esrLab:` regardless of tag match status
- The converted report is ready for deployment with both IGNW and WATH tag references

---

*Conversion performed using BIRT → Ignition Tag Migration Tool*
