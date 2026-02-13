# Development Standards: SQL

## Revision History

| Version | Date       | Author          | Summary                                                   |
| ------- | ---------- | --------------- | --------------------------------------------------------- |
| 1.0     | 2024-08-13 | Brock Solutions | Initial draft based on Development_Standards_SQL_v1.1.pdf |

---

## Table of Contents

1. [General Information](#1-general-information)
2. [Commenting](#2-commenting)
3. [Readability and Formatting](#3-readability-and-formatting)
4. [Naming Conventions and Data Types](#4-naming-conventions-and-data-types)
5. [Coding Practices](#5-coding-practices)
6. [Performance Considerations](#6-performance-considerations)
7. [Debugging Techniques](#7-debugging-techniques)
8. [Standards Checklist](#8-standards-checklist)

---

## 1. General Information

### 1.1 Purpose

Provide a common, opinionated set of guidelines to:
• Increase readability of queries
• Improve onboarding speed
• Reduce ambiguity in SQL development style
• Promote performant design choices

### 1.2 Document Breakdown

Sections: Commenting; Readability & Formatting; Naming & Data Types; Coding Practices; Performance Considerations; Debugging; Checklist.
Planned future additions: Security Guidelines, Source Control (expanded), Logging Methods, Design Considerations, Glossary, Internal Training Links, External Reference Links.

---

## 2. Commenting

### 2.1 Headers

Standard header for stored procedures, functions, triggers, views, etc.

```sql
-- =============================================
-- Author: John Smith
-- Create date: yyyy-mm-dd
-- Description: Brief description of usage
-- Created by Brock Solutions. Copyright 2024
-- =============================================
-- Used In
-- =============================================
-- Application .. Method/Rule
-- _____________________________________________
-- PM ........... RuleManager.RuleName
-- NET .......... Class.Method or Dataset
-- Business Obj . Report Name
-- Report Serv .. Report Name
-- SQL .......... Stored Procedure Name
-- =============================================
-- Change Log
-- =============================================
-- Date ......... Initials ........ Description
-- _____________________________________________
-- yyyy-mm-dd ... JS .............. MG____/US-____ - Description of change.
-- =============================================
```

Notes: Keep 'Used In' updated. Change Log should reference job number (e.g. MG9229) or ADO item (e.g. US-1234).

### 2.2 Body Comments

Comment non-trivial logic. Prefer concise, purposeful comments. Update comments after refactors to avoid drift.

---

## 3. Readability and Formatting

Consistency accelerates comprehension. Principles below reinforce scanning for structure.

### 3.1 Indentation

Major SQL keywords **must** be left-aligned and placed on their own line. Subordinate elements must be indented one level.

**Major SQL keywords include:** SELECT, FROM, WHERE, ORDER BY, GROUP BY, HAVING, INSERT, UPDATE, DELETE, INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN, CROSS JOIN, etc.

**Subordinate elements include:** column lists, table references following FROM, ON conditions, AND/OR conditions within WHERE clauses, embedded SELECT statements, etc.

```sql
SELECT
	 [BPM_EQUIPMENT_PROPERTY].equip_prpty_value AS Value
	,[BPM_EQUIPMENT].equip_name AS EquipmentName
	,(
        SELECT
            [POM_ENTRY].pom_entry_id
        FROM
            [SITMES].[dbo].[POM_ENTRY] WITH (NOLOCK)
        WHERE
            [POM_ENTRY].equip_pk = [BPM_EQUIPMENT].equip_pk
	) AS EntryID
FROM
    [SITMES].[dbo].[BPM_EQUIPMENT] WITH (NOLOCK)
INNER JOIN
    [SITMES].[dbo].[BPM_EQUIPMENT_PROPERTY] WITH (NOLOCK)
    ON [BPM_EQUIPMENT_PROPERTY].equip_pk = [BPM_EQUIPMENT].equip_pk
WHERE
    [BPM_EQUIPMENT_PROPERTY].equip_prpty_id = @chvPropertyName
    AND [BPM_EQUIPMENT].equip_name = @chvEquipmentName
ORDER BY
     [BPM_EQUIPMENT].RowUpdated DESC
    ,[BPM_EQUIPMENT].equip_name ASC;
```

### 3.2 Capitalization

SQL reserved keywords uppercase; identifiers PascalCase or consistent project style.

### 3.3 Explicit Column Selection

> NEVER `SELECT *` in deployed code.

### 3.4 Explicit Database Declaration

- Tables names fully scoped in FROM clause `[DB].[Schema].[Table]`.
- All other selectors must qualify the table `[TableName].[ColumnName]`.

Often the scope of work expands multiple databases which result in queries becoming much more
complex to read. Explicit database declaration must always be used to ensure that the correct database
is utilized, preventing future potential data access errors. Also, by using this suggested declaration
structure, the code readability is improved as the code will not make lines of code run on for many
characters.

In general, the database name should always be referenced within the FROM clause once and only
once. There should be no need to use the name anywhere else within the query. If a SELECT statement
is embedded, the explicit database declaration should be used again.

### 3.4.1 Table Aliases

> IMPORTANT! No table aliases or table renaming.

```sql
-- Sample Query: Explicit Database Declaration
SELECT
	 [BPM_EQUIPMENT_PROPERTY].equip_prpty_value AS Value
	,[BPM_EQUIPMENT].equip_name AS EquipmentName
	,(
        SELECT
            [POM_ENTRY].pom_entry_id
        FROM
            [SITMES].[dbo].[POM_ENTRY] WITH (NOLOCK)
        WHERE
            [POM_ENTRY].equip_pk = [BPM_EQUIPMENT].equip_pk
		) AS EntryID
FROM
    [SITMES].[dbo].[BPM_EQUIPMENT] WITH (NOLOCK)
    INNER JOIN [SITMES].[dbo].[BPM_EQUIPMENT_PROPERTY] WITH (NOLOCK)
	    ON [BPM_EQUIPMENT_PROPERTY].equip_pk = [BPM_EQUIPMENT].equip_pk
WHERE
    [BPM_EQUIPMENT_PROPERTY].equip_prpty_id = @chvPropertyName
	AND [BPM_EQUIPMENT].equip_name = @chvEquipmentName
ORDER BY
     [BPM_EQUIPMENT].RowUpdated DESC
	,[BPM_EQUIPMENT].equip_name ASC;
```

### 3.5 Table References

Qualify columns with table/alias for clarity. Use aliases when repeating a table or long names.

### 3.6 Column Selection, Comma Placement

- Always, one column per line

In any case where multiple columns are used (SELECT/ORDER BY), a comma should be placed in the left
most part of the new line. This allows the programmer to rapidly comment out columns or order by
conditions when debugging the query.

```sql
SELECT E.equip_pk
      ,E.equip_name
      ,E.equip_id
      ,E.equip_superior
      --,E.equip_parent_pk
FROM [SITMES].[dbo].[BPM_EQUIPMENT] E WITH (NOLOCK);
```

### 3.7 Column Declaration / Aliasing

When altering the name of a column which is returned by the query or if you are simply declaring a
column name because of a group by function or some custom CASE statement, the name of the new
column should be encased in single quotes (').

It should be noted that not all columns need to be renamed and if using just the default column name,
then no declaration needs to be made.

```sql
-- Sample Query: Column Name Declaration
SELECT
     [BPM_EQUIPMENT].equip_name
    ,[BPM_EQUIPMENT_PROPERTY].equip_prpty_value AS 'PropertyValue'
    ,[BPM_EQUIPMENT_PROPERTY].equip_prpty_name AS 'PropertyName'
FROM
    [SITMES].[dbo].[BPM_EQUIPMENT] WITH(NOLOCK)
    INNER JOIN [SITMES].[dbo].[BPM_EQUIPMENT_PROPERTY]
        ON [BPM_EQUIPMENT_PROPERTY].equip_pk = [BPM_EQUIPMENT].equip_pk
WHERE
    [BPM_EQUIPMENT_PROPERTY].equip_prpty_name = @chvnPropertyName
```

### 3.8 Embedded SELECTs

There are various methods of using embedded `SELECT` statements. These methods are listed in the
bullets below:

- Returning a single cell from a complex table location linking a particular column back to the
  main tables.

  > NOTE:
  >
  > It is important to remember that these queries may only return one result but also, if this is a
  > derived table, these columns should not be filtered on through `WHERE` clauses or sorted by
  > `ORDER` BY clauses because the performance of the query will degrade substantially.
  >
  > When attempting to do something such as this, it may make sense to insert the data into a
  > temp table and then query from that against the columns that were originally considered to
  > be embedded.

```sql
-- Sample Query: Embedded SELECT Example 1

--  Returning an entire table which is then joined upon within the FROM statement (often called
-- derived tables).

SELECT
	 [BPM_EQUIPMENT_PROPERTY].equip_prpty_value AS Value
	,[BPM_EQUIPMENT].equip_name AS EquipmentName
	,(
        SELECT
            [POM_ENTRY].pom_entry_id
        FROM
            [SITMES].[dbo].[POM_ENTRY] WITH (NOLOCK)
        WHERE
            [POM_ENTRY].equip_pk = [BPM_EQUIPMENT].equip_pk
		) AS EntryID
FROM
    [SITMES].[dbo].[BPM_EQUIPMENT] WITH (NOLOCK)
    INNER JOIN [SITMES].[dbo].[BPM_EQUIPMENT_PROPERTY] WITH (NOLOCK)
	    ON [BPM_EQUIPMENT_PROPERTY].equip_pk = [BPM_EQUIPMENT].equip_pk
WHERE
    [BPM_EQUIPMENT_PROPERTY].equip_prpty_id = @chvPropertyName
	AND [BPM_EQUIPMENT].equip_name = @chvEquipmentName
ORDER BY
     [BPM_EQUIPMENT].RowUpdated DESC
	,[BPM_EQUIPMENT].equip_name ASC;
```

Derived table example:

```sql
-- Sample Query: Embedded SELECT Example 2
-- Return an integer to supply part of the WHERE clause such that a string is only queried once on
-- the table and then cached for the remaining portion of the query. Performance is substantially
-- increased due to the utilization of integers versus strings.
SELECT
    [TEMP].MaterialID
  , [TEMP].MaterialDescription
  , [TEMP].Equipment
FROM (
    SELECT DISTINCT
        [POM_MAT_LIST].def_id     AS 'MaterialID'
      , [MMDefinitions].descript AS 'MaterialDescription'
      , [BPM_EQUIPMENT].equip_name AS 'Equipment'
      , [POM_MAT_LIST].class     AS 'Class'
    FROM [SITMES].[dbo].[POM_ORDER]
    INNER JOIN [SITMES].[dbo].[POM_ENTRY]
        ON [POM_ENTRY].pom_order_pk = [POM_ORDER].pom_order_pk
    INNER JOIN [SITMES].[dbo].[POM_MAT_SPEC]
        ON [POM_MAT_SPEC].pom_entry_pk = [POM_ENTRY].pom_entry_pk
    INNER JOIN [SITMES].[dbo].[POM_MAT_LIST]
        ON [POM_MAT_LIST].pom_mat_spec_pk = [POM_MAT_SPEC].pom_mat_spec_pk
    INNER JOIN [SITMES].[dbo].[MMDefinitions]
        ON [MMDefinitions].DefID = [POM_MAT_LIST].def_id
    INNER JOIN [SITMES].[dbo].[BPM_EQUIPMENT]
        ON [BPM_EQUIPMENT].equip_pk = [POM_ENTRY].equip_pk
    WHERE [POM_ORDER].pom_order_id = @chvorderID
      AND [BPM_EQUIPMENT].equip_name LIKE '%' + @chvEquipment + '%'
      AND [POM_MAT_LIST].usage = 1
) AS [TEMP]
ORDER BY
    [TEMP].Class;
```

```sql
-- Sample Query: Embedded SELECT Example 3 (Integer Lookup for Performance)
SELECT
    [MMLots].LotID
  , [MMLotPrpVals].PropValDec
FROM
    [SITMES].[dbo].[MMLots] WITH (NOLOCK)
INNER JOIN
    [SITMES].[dbo].[MMLotPrpVals] WITH (NOLOCK)
        ON [MMLotPrpVals].LotPK = [MMLots].LotPK
WHERE [MMLotPrpVals].PropertyPK =
    (
        SELECT [MMProperties].PropertyPK
            FROM [SITMES].[dbo].[MMProperties] WITH (NOLOCK)
        WHERE
            [MMProperties].PropertyID = 'LOTdtCreationDate'
    )
  AND [MMLotPrpVals].PropValDec IS NOT NULL;
```

**Additional notes to consider:**

- Always try to avoid embedding SELECT statements when possible. Use INNER JOINs in the main
  SELECT to avoid unnecessary complexity and improve readability.
- When embedding a SELECT statement within a SELECT statement, the structure should remain
  the same, but all lines should be indented appropriately.

### 3.9 JOIN and ON Placement

When using INNER or OUTER type JOIN's, they should always be placed at the left most portion of the
line so that programmers can quickly determine how the data is being linked to the newly defined
table. It also makes for quick and easy removal of the code when debugging.
ON's should always be placed on the next line, with each separate conditional statement placed on its
own line.

```sql
-- Sample Query: Correct Placement of JOIN
SELECT
     [POM_MAT_LIST].def_id AS 'MaterialID'
    ,[MMDefinitions].descript AS 'MaterialDescription'
    ,[BPM_EQUIPMENT].equip_name AS 'Equipment'
    ,[POM_MAT_LIST].class AS 'Class'
FROM
    [SITMES].[dbo].[POM_ORDER]
    INNER JOIN [SITMES].[dbo].[POM_ENTRY]
        ON [POM_ENTRY].pom_order_pk = [POM_ORDER].pom_order_pk
        AND [POM_ENTRY].pom_entry_id <> [POM_ORDER].pom_order_id
    INNER JOIN [SITMES].[dbo].[POM_MAT_SPEC]
        ON [POM_MAT_SPEC].pom_entry_pk = [POM_ENTRY].pom_entry_pk
    INNER JOIN [SITMES].[dbo].[POM_MAT_LIST]
        ON [POM_MAT_LIST].pom_mat_spec_pk = [POM_MAT_SPEC].pom_mat_spec_pk
    INNER JOIN [SITMES].[dbo].[MMDefinitions]
        ON [MMDefinitions].DefID = [POM_MAT_LIST].def_id
    INNER JOIN [SITMES].[dbo].[BPM_EQUIPMENT]
        ON [BPM_EQUIPMENT].equip_pk = [POM_ENTRY].equip_pk
WHERE
    [POM_ORDER].pom_order_id = @chvorderID
    AND [BPM_EQUIPMENT].equip_name LIKE '%' + @chvEquipment + '%'
    AND [POM_MAT_LIST].usage = 1
```

### 3.10 Transaction Isolation / WITH (NOLOCK)

When reading uncommitted is acceptable, it should be set at the start of the procedure. If you are unsure when this condition is acceptable please consult your software or discipline lead.

Prefer `SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED` at procedure start (be aware of dirty reads risk). `WITH (NOLOCK)` for functions where isolation cannot be set.

```sql
-- Transaction Isolation
CREATE PROCEDURE dbo.EQU_GetOrderExecutionEquipment
(
	  @OrderID     VARCHAR(101)
	, @PlantID     VARCHAR(50)
	, @JobID       VARCHAR(50) = NULL
	, @VuseArea    VARCHAR(50) = NULL
)
AS
BEGIN
	SET NOCOUNT ON;
	SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
	-- Body ...
END;
```

```sql

-- Sample Query: WITH(NOLOCK) Example
SELECT
     [MMLots].LotID
    ,[MMLotPrpVals].PropValDev
FROM
    [SITMES].[dbo].[MMLots] WITH(NOLOCK)
    INNER JOIN [SITMES].[dbo].[MMLotPrpVals] WITH(NOLOCK)
        ON [MMLotPrpVals].LotPK = [MMLots].LotPK
```

### 3.11 ORDER BY Column Names

Avoid positional ordering. Use explicit column/alias names.

## 4. Naming Conventions and Data Types

### 4.1 Variable Naming & Type Hints

> Reference
>
> https://www.cms.gov/Research-Statistics-Data-and-Systems/CMS-Information-Technology/DBAdmin/downloads/SQLServerStandardsandGuildelines.pdf

Prefix variables to surface type quickly (legacy convention retained for clarity). Examples:
| Data Type | Prefix | Example |
|-----------|--------|---------|
| char | chr | @chrFirstName |
| varchar | chv | @chvActivity |
| nchar | chrn | @chrnLastName |
| nvarchar | chvn | @chvnLastName |
| text | txt | @txtNote |
| ntext | txtn | @txtnComment |
| datetime | dtm | @dtmTargetDate |
| smalldatetime | dts | @dtsCompletedDate |
| tinyint | iny | @inyActivityID |
| smallint | ins | @insEquipmentTypeID |
| int | int | @intAsset |
| bigint | inb | @inbGTIN |
| decimal/numeric | dec | @decProfit |
| real | rea | @reaVelocity |
| float | flt | @fltLength |
| smallmoney | mns | @mnsCost |
| money | mny | @mnyPrice |
| binary | bin | @binPath |
| varbinary | biv | @bivContract |
| image | img | @imgLogo |
| bit | bit | @bitOperational |
| timestamp | tsp | @tspOrderID |
| uniqueidentifier | guid | @guidPrice |
| sql_variant | var | @varInventory |
| cursor | cur | @curInventory |
| table (variable) | tbl | @tblLease |

#### 4.1.1 Data Type Considerations

Choose the most constrained, semantically appropriate type. Be mindful of NVARCHAR (double storage). Prefer `VARCHAR(MAX)` / `NVARCHAR(MAX)` over deprecated `TEXT`/`NTEXT`.

Hints: Use `CHAR` only for fixed, non-nullable, uniform length data; prefer `VARCHAR` when optional or variable length; consider memory impact of unused fixed-length NULLable columns.

---

## 5. Coding Practices

### 5.1 Reduce Main Table Result Set Early

Filter high-cardinality root table before broad joins.

```sql
-- Sample Query: Unrestricted Result Set
-- If you were to take this query and add a simple condition in the WHERE clause to reduce the number of
-- rows in the [MMLots] table, the join would be considerably faster.
-- As it stand the entire [MMLots] table is being joined to the [MMLotPrpVals] table and then filtered

SELECT
    [MMLots].LotID
FROM
    [SITMES].[dbo].[MMLots] WITH(NOLOCK)
    INNER JOIN [SITMES].[dbo].[MMLotPrpVals] WITH(NOLOCK)
        ON [MMLotPrpVals].LotPK = [MMLots].LotPK
        AND [MMLotPrpVals].PropertyPK =
        (
            SELECT
                [MMProperties].PropertyPK
            FROM
                [SITMES].[dbo].[MMProperties] WITH(NOLOCK)
            WHERE
                [MMProperties].PropertyID = 'LOTdtCreationDate'
        )
WHERE
    [MMLotPrpVals].PropValDate BETWEEN '2010-01-01' AND '2010-02-01'
```

### 5.2 OR / LIKE Pitfalls

Situations have been seen where a combination of OR's with LIKE statements will be used to
enable/disable where clause conditions.

The danger in doing this is that when SQL creates the
execution plans on the first run of a stored procedure, the query is optimized for those first inputs.

If the inputs combinations change so that various LIKE conditions must run that did not previously, the
original result of that plan could have a negative impact on the execution of the stored procedure.

When evaluating stored procedures and the conditional statements within the WHERE clause, it is
important to try and eliminate the need for LIKE clauses. This may require some addition work prior to
executing the main SELECT statements in the stored procedure, but it will ensure that the execution
plan that is generated works for all input variations.

The examples below show implementations of what not to do:

```sql
SELECT
     [MMLots].LotID
    ,[MMLotOperations].OperationDate
FROM
    [SITMES].[dbo].[MMLots]
    INNER JOIN [SITMES].[dbo].[MMHuts]
        ON [MMLots]. Hut PK [MMHuts].Hut PK
    INNER JOIN [SITMES].[dbo].[MMDefVers]
        ON [MMLots]. DefVer PK [MMDefVers].DefVerPK
    INNER JOIN [SITMES].[dbo].[MMDefinitions]
        ON [MMDefVers].DefPK = [MMDefinitions].DefPK
    INNER JOIN [SITMES].[dbo].[MMLotOperations]
        ON [MMLots].LotPK [MMLotOperations].LotPK
WHERE
    (@chvLotID IS NULL OR [MMLots].LotID = @chvLotID)
    -- NOTE THE TWO LIKE CLAUSES BELOW: LET'S AVOID THESE IF POSSIBLE
    AND (@chvMaterialID IS NULL OR [MMDefinitions].DefID LIKE + @chvMaterialID + '%')
    AND (@chvHutID IS NULL OR [MHuts].HutID LIKE + @chvHutID + '%')
    AND ([MMLotOperations].OperationDate BETWEEN @dtmUTCStartDate AND @dtmUTCEndDate)
```

An approach to overcome the use of LIKE clauses is to create Declared tables prior to the main query
execution. The declared table should contain as little rows as possible and be in the simplest data types
as possible.

For example, for the case above, it may make sense to create a declared table called materials. In this
table, all the materials are inserted into it that meet the requirements of the input @chvMaterialID

```sql
IF @chvMaterialID IS NULL
    SET @chvMaterialID = '%'

INSERT INTO @Materials
SELECT
    [MMDefinitions].DefPK
FROM
    [SITMES].[dbo].[MMDefinitions]
WHERE
    [MMDefinitions].DefID LIKE '%' + @chvMaterialID + '%'
```

The main condition can the now become:

```sql
WHERE
    ...
    AND [MMDefinitions].DefPK IN (SELECT DefPK FROM @Materials)
    ...

```

### 5.3 Wildcards & Index Usage

A wild card is a '%' or '\_' in SQL where it represents an array of strings or a single character that are all
unknown. The wildcard is typically used in a LIKE statement to return multiple rows of data where the
conditions are somewhat vague.

- Index Scan: An Index Scan touches every row in a table regardless of whether it qualifies. As a
  result, the cost of performance is directly proportional to the rows in the table.
- Index Seek: An Index Seek touches only those rows that qualify and pages that contain these
  qualifying rows. As a result, the cost of performance is only proportional to the number of
  qualifying rows instead of all the rows in the table.

When building the WHERE condition of a query, be very careful where the decision of a wildcard is
placed. The reason for this is that when building a query, one wants to try and eliminate as many "table
scans" as possible.

```sql
-- Scan
WHERE L.LotID LIKE '%222';
-- Seek since the engine can key off of records starting with D in an index
WHERE L.LotID LIKE 'D%';
```

### 5.4 Cursors

Avoid the use of cursors as much as possible. If a cursor is unavoidable, first discuss this with the
technical lead in your group. Based on the outcome of the conversation, the suggested approach may
be to use a WHILE loop.

To effectively replace a WHILE loop, a column must be specified to uniquely identify each column. This
may mean that a row count may need to be added to a result set.

It is important to test the performances of a WHILE loop against a cursor to verify performances. This
goes back to the practice of trying different approaches to verify the decisions made to create the
query with the optimal performance.

## 6. Standards Checklist

Use this self-audit before committing changes. Tick items as you verify them.

### Commenting

- [ ] Header block present (see 2.1)
- [ ] Sufficient inline comments (see 2.2)

### Readability & Formatting

- [ ] Indentation consistent (see 3.1)
- [ ] Capitalization consistent (see 3.2)
- [ ] Explicit database declarations used appropriately (see 3.4)
- [ ] Table/alias prefixes on all columns (see 3.5)
- [ ] Leading commas / one column per line (see 3.6)
- [ ] Aliased derived columns (see 3.7)
- [ ] Embedded SELECTs justified & formatted (see 3.8)
- [ ] JOIN + ON placement (see 3.9)
- [ ] Isolation level / NOLOCK usage considered (see 3.10)
- [ ] ORDER BY uses names not ordinals (see 3.11)

### Naming & Data Types

- [ ] Variable naming & type prefixes correct (see 4.1 and 4.1.1)

### Coding Practices

- [ ] Reduce main table result set early / root set considered (see 5.1)
- [ ] OR / LIKE pitfalls considered (see 5.2)
- [ ] Wildcards & index usage considered (see 5.3)
- [ ] Cursors avoided or justified (see 5.4)
