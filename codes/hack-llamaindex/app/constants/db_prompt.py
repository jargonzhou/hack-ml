"""
Database prompts.
"""

sql_server_schema_prompt = """
# sql server T-SQL list tables and views
## List Tables & Views Together
```sql
SELECT 
    SCHEMA_NAME(o.schema_id) AS SchemaName,
    o.name AS ObjectName,
    CASE o.type 
        WHEN 'U' THEN 'Table'
        WHEN 'V' THEN 'View'
    END AS ObjectType,
    ep.value AS ObjectComment,
    o.create_date AS CreateDate,
    o.modify_date AS ModifyDate
FROM sys.objects o
LEFT JOIN sys.extended_properties ep 
    ON o.object_id = ep.major_id 
    AND ep.minor_id = 0 
    AND ep.name = 'MS_Description'
WHERE o.type IN ('U', 'V')
ORDER BY ObjectType, SchemaName, ObjectName;
```

# sql server T-SQL list function and stored procedures
## List Procedures & Functions Together
```sql
SELECT 
    SCHEMA_NAME(schema_id) AS SchemaName,
    name AS ObjectName,
    CASE type
        WHEN 'P'  THEN 'Stored Procedure'
        WHEN 'FN' THEN 'Scalar Function'
        WHEN 'IF' THEN 'Inline Table-Valued Function'
        WHEN 'TF' THEN 'Table-Valued Function'
    END AS ObjectType,
    create_date AS CreateDate,
    modify_date AS ModifyDate
FROM sys.objects
WHERE type IN ('P', 'FN', 'IF', 'TF')
ORDER BY ObjectType, SchemaName, ObjectName;
```

## List Only Stored Procedures
```sql
SELECT 
    SCHEMA_NAME(schema_id) AS SchemaName,
    name AS ProcedureName,
    create_date AS CreateDate,
    modify_date AS ModifyDate
FROM sys.objects
WHERE type = 'P'
ORDER BY SchemaName, ProcedureName;
```

## List Only Functions
```sql
SELECT 
    SCHEMA_NAME(schema_id) AS SchemaName,
    name AS FunctionName,
    CASE type
        WHEN 'FN' THEN 'Scalar Function'
        WHEN 'IF' THEN 'Inline Table Function'
        WHEN 'TF' THEN 'Table Function'
    END AS FunctionType,
    create_date AS CreateDate,
    modify_date AS ModifyDate
FROM sys.objects
WHERE type IN ('FN', 'IF', 'TF')
ORDER BY FunctionType, SchemaName, FunctionName;
```

## ANSI-SQL Alternative: INFORMATION_SCHEMA
```sql
SELECT 
    ROUTINE_SCHEMA AS SchemaName,
    ROUTINE_NAME AS RoutineName,
    ROUTINE_TYPE AS RoutineType -- PROCEDURE or FUNCTION
FROM INFORMATION_SCHEMA.ROUTINES
ORDER BY ROUTINE_TYPE, ROUTINE_SCHEMA, ROUTINE_NAME;
```

# table
## Table Definitions
```sql
SELECT 
    SCHEMA_NAME(t.schema_id) AS SchemaName,
    t.name AS TableName,
    ep_table.value AS TableComment, -- Comment on the Table
    c.column_id AS ColumnOrder,
    c.name AS ColumnName,
    TYPE_NAME(c.user_type_id) AS DataType,
    CASE 
        WHEN TYPE_NAME(c.user_type_id) IN ('varchar', 'nvarchar', 'char', 'nchar', 'binary', 'varbinary') 
        THEN CAST(CASE WHEN c.max_length = -1 THEN 'MAX' ELSE CAST(c.max_length AS VARCHAR(10)) END AS VARCHAR(10))
        ELSE NULL 
    END AS MaxLength,
    CASE WHEN c.is_nullable = 1 THEN 'YES' ELSE 'NO' END AS IsNullable,
    ep_col.value AS ColumnComment -- Comment on the Column
FROM sys.tables t
INNER JOIN sys.columns c ON t.object_id = c.object_id
-- Get Table Comments
LEFT JOIN sys.extended_properties ep_table 
    ON t.object_id = ep_table.major_id 
    AND ep_table.minor_id = 0 
    AND ep_table.name = 'MS_Description'
-- Get Column Comments
LEFT JOIN sys.extended_properties ep_col 
    ON c.object_id = ep_col.major_id 
    AND c.column_id = ep_col.minor_id 
    AND ep_col.name = 'MS_Description'
ORDER BY SchemaName, TableName, c.column_id;
```

## ANSI-SQL Alternative: INFORMATION_SCHEMA
```sql
SELECT 
    TABLE_SCHEMA AS SchemaName,
    TABLE_NAME AS ObjectName,
    COLUMN_NAME AS ColumnName,
    ORDINAL_POSITION AS ColumnOrder,
    DATA_TYPE AS DataType,
    CHARACTER_MAXIMUM_LENGTH AS MaxLength,
    IS_NULLABLE AS IsNullable
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME IN (SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES)
ORDER BY TABLE_SCHEMA, TABLE_NAME, ORDINAL_POSITION;
```

# view
## View Definitions
```sql
SELECT 
    SCHEMA_NAME(v.schema_id) AS SchemaName,
    v.name AS ViewName,
    ep_view.value AS ViewComment, -- Comment on the View
    c.name AS ColumnName,
    TYPE_NAME(c.user_type_id) AS DataType,
    CASE WHEN c.is_nullable = 1 THEN 'YES' ELSE 'NO' END AS IsNullable,
    ep_col.value AS ColumnComment, -- Comment on the Column
    OBJECT_DEFINITION(v.object_id) AS ViewDefinitionScript
FROM sys.views v
INNER JOIN sys.columns c ON v.object_id = c.object_id
-- Get View Comments
LEFT JOIN sys.extended_properties ep_view 
    ON v.object_id = ep_view.major_id 
    AND ep_view.minor_id = 0 
    AND ep_view.name = 'MS_Description'
-- Get Column Comments
LEFT JOIN sys.extended_properties ep_col 
    ON c.object_id = ep_col.major_id 
    AND c.column_id = ep_col.minor_id 
    AND ep_col.name = 'MS_Description'
ORDER BY SchemaName, ViewName, c.column_id;
```

# function
## List Function Arguments and Return Types
```sql
SELECT 
    SCHEMA_NAME(o.schema_id) AS SchemaName,
    o.name AS FunctionName,
    CASE o.type 
        WHEN 'FN' THEN 'Scalar Function'
        WHEN 'IF' THEN 'Inline Table Function'
        WHEN 'TF' THEN 'Table-Valued Function'
    END AS FunctionType,
    CASE WHEN p.parameter_id = 0 THEN 'RETURNS' ELSE p.name END AS ParameterOrReturn,
    TYPE_NAME(p.user_type_id) AS DataType,
    p.max_length AS MaxLength,
    p.precision AS Precision,
    p.scale AS Scale
FROM sys.objects o
INNER JOIN sys.parameters p ON o.object_id = p.object_id
WHERE o.type IN ('FN', 'IF', 'TF') -- Filters for all function types
ORDER BY SchemaName, FunctionName, p.parameter_id;

SELECT 
    SPECIFIC_CATALOG AS CatalogName,
    SPECIFIC_SCHEMA AS SchemaName,
    SPECIFIC_NAME AS RoutineName,
    -- ROUTINE_TYPE AS RoutineType, -- PROCEDURE or FUNCTION
    PARAMETER_NAME AS ParameterName,
    DATA_TYPE AS DataType,
    CHARACTER_MAXIMUM_LENGTH AS MaxLength,
    PARAMETER_MODE AS ParameterDirection -- IN, OUT, or NULL (for returns)
FROM INFORMATION_SCHEMA.PARAMETERS
ORDER BY SchemaName, RoutineName, ORDINAL_POSITION;
```

# stored procedure
## List Stored Procedure Arguments
```sql
SELECT 
    SCHEMA_NAME(o.schema_id) AS SchemaName,
    o.name AS ProcedureName,
    p.name AS ParameterName,
    TYPE_NAME(p.user_type_id) AS DataType,
    p.max_length AS MaxLength,
    p.precision AS Precision,
    p.scale AS Scale,
    CASE WHEN p.is_output = 1 THEN 'OUTPUT' ELSE 'INPUT' END AS ParameterDirection
FROM sys.objects o
INNER JOIN sys.parameters p ON o.object_id = p.object_id
WHERE o.type = 'P' -- 'P' filters for Stored Procedures
ORDER BY SchemaName, ProcedureName, p.parameter_id;
```

## sp_describe_first_result_set
```sql
EXEC sp_describe_first_result_set 
    @tsql = N'EXEC dbo.P_Tech_Craft_Fabric';
```

## sys.dm_exec_describe_first_result_set
```sql
SELECT
    column_ordinal AS Position,
    name AS ColumnName,
    system_type_name AS DataType,
    is_nullable AS IsNullable
FROM sys.dm_exec_describe_first_result_set('EXEC dbo.P_Tech_Craft_Fabric', NULL, 0);
```
"""
