# Database Schema Documentation

## 1. Tables and Columns
This section describes the tables and their columns, including data types and comments where available.

(The detailed list of tables, columns, data types, and descriptions retrieved from the system tables are included here, sorted by schema and table name.)

## 2. Views
(Listing of views and their definitions if available.)

## 3. Stored Procedures
Stored procedures are categorized by business module:
- **APL (Packing List):** Generating packing lists (e.g., `P_APL_GeneratebyPackingMethod`).
- **QC/QM (Quality Control/Management):** Inspection results and reports (e.g., `P_QC_ClothingInspection_Main`).
- **Plan/Production:** Progress and forecasting (e.g., `P_Plan_ProdProgressQuery`).
- **SD (Sales & Distribution):** Order management and audits (e.g., `P_sd_order_audit`).
- **Tech/Craft:** Technical specifications (e.g., `P_Tech_Craft_Fabric`).

## 4. Functions
### Scalar Functions
- **Language & Dictionary:** `fn_dic_getLangValue`
- **Technical Calculations:** `FN_CalcBasicProcessPrice`, `fn_perf_ratio`
- **Logistics:** `fn_sd_getExchangeRate`

### Inline Table-Valued Functions
- `fnpbConvertStringToTable`
- `fnpbConvertStringToTableWithEmpty`
- `fnpbConvertStringToTwoFieldTable`

### Table-Valued Functions
- **Language Lists:** `fn_dic_getLangValueList`
- **Customer/Permission:** `fn_sd_getCustomerByProductNo`
- **Quality/Material:** `fn_qm_getDefectScoreNewRule`