---
description: Introspect database metadata to discover tables, columns, indexes, procedures, and more
icon: magnifying-glass-chart
---

# 🔍 Database Information

The `bx:dbInfo` component allows you to introspect database metadata, providing detailed information about database structures, schemas, tables, columns, indexes, foreign keys, stored procedures, and version information. This is essential for dynamic database operations, schema discovery, and database management tools.

## 📋 Overview

Database introspection in BoxLang enables you to:

- **Discover Schemas** - List all databases and schemas in a connection
- **List Tables** - Retrieve all tables, views, and system tables
- **Inspect Columns** - Get detailed column metadata including types, constraints, and keys
- **Analyze Indexes** - View index information for performance optimization
- **Map Foreign Keys** - Discover relationships between tables
- **Find Procedures** - List available stored procedures
- **Check Versions** - Retrieve database and JDBC driver version information

## 🔧 Basic Usage

The `bx:dbInfo` component requires two attributes:

1. `type` - The type of metadata to retrieve
2. `name` - The variable name to store results

```js
bx:dbInfo
    type="tables"
    name="tableList"
    datasource="myDB";

writeDump( tableList );
```

## 📊 Metadata Types

### Database Names (DBNAMES)

List all databases and schemas accessible through the connection:

```js
bx:dbInfo
    type="dbnames"
    name="databases"
    datasource="myDB";

// Results contain DBNAME and TYPE columns
for ( row in databases ) {
    writeOutput( "<p>#row.DBNAME# (#row.type#)</p>" );
}
```

**Result Columns:**
- `DBNAME` - Database or schema name
- `TYPE` - Either "CATALOG" or "SCHEMA"

### Tables

Retrieve information about tables in the database:

```js
// All tables in default database
bx:dbInfo
    type="tables"
    name="allTables"
    datasource="myDB";

// Filter by pattern
bx:dbInfo
    type="tables"
    name="userTables"
    pattern="user_%"
    datasource="myDB";

// Specific schema
bx:dbInfo
    type="tables"
    name="schemaTables"
    pattern="public.%"
    datasource="myDB";

// Filter by table type
bx:dbInfo
    type="tables"
    name="views"
    filter="VIEW"
    datasource="myDB";
```

**Result Columns:**
- `TABLE_CAT` - Table catalog (may be null)
- `TABLE_SCHEM` - Table schema (may be null)
- `TABLE_NAME` - Table name
- `TABLE_TYPE` - Table type (TABLE, VIEW, SYSTEM TABLE, etc.)
- `REMARKS` - Explanatory comment on the table
- Plus additional database-specific columns

**Common Filter Values:**
- `TABLE` - Regular tables (default)
- `VIEW` - Database views
- `SYSTEM TABLE` - System tables
- `GLOBAL TEMPORARY` - Global temporary tables
- `LOCAL TEMPORARY` - Local temporary tables
- `ALIAS` - Table aliases
- `SYNONYM` - Table synonyms

### Columns

Get detailed information about columns in a table:

```js
bx:dbInfo
    type="columns"
    name="employeeColumns"
    table="employees"
    datasource="myDB";

for ( col in employeeColumns ) {
    output = "<p>#col.COLUMN_NAME# - #col.TYPE_NAME#";
    if ( col.IS_PRIMARYKEY ) {
        output &= " (PK)";
    }
    if ( col.IS_FOREIGNKEY ) {
        output &= " (FK -> #col.REFERENCED_PRIMARYKEY_TABLE#.#col.REFERENCED_PRIMARYKEY#)";
    }
    output &= "</p>";
    writeOutput( output );
}
```

**Result Columns:**
- `TABLE_CAT` - Table catalog
- `TABLE_SCHEM` - Table schema
- `TABLE_NAME` - Table name
- `COLUMN_NAME` - Column name
- `DATA_TYPE` - SQL data type from java.sql.Types
- `TYPE_NAME` - Data source dependent type name
- `COLUMN_SIZE` - Column size
- `DECIMAL_DIGITS` - Decimal digits (for numeric types)
- `IS_NULLABLE` - "YES", "NO", or ""
- `COLUMN_DEF` - Default value
- `IS_PRIMARYKEY` - Boolean, true if primary key
- `IS_FOREIGNKEY` - Boolean, true if foreign key
- `REFERENCED_PRIMARYKEY` - Referenced column name (if foreign key)
- `REFERENCED_PRIMARYKEY_TABLE` - Referenced table name (if foreign key)
- Plus additional database-specific columns

### Foreign Keys

Discover foreign key relationships for a table:

```js
bx:dbInfo
    type="foreignkeys"
    name="employeeForeignKeys"
    table="employees"
    datasource="myDB";

for ( fk in employeeForeignKeys ) {
    writeOutput(
        "<p>#fk.FKCOLUMN_NAME# references #fk.PKTABLE_NAME#.#fk.PKCOLUMN_NAME#</p>"
    );
}
```

**Result Columns:**
- `PKTABLE_CAT` - Primary key table catalog
- `PKTABLE_SCHEM` - Primary key table schema
- `PKTABLE_NAME` - Primary key table name
- `PKCOLUMN_NAME` - Primary key column name
- `FKTABLE_CAT` - Foreign key table catalog
- `FKTABLE_SCHEM` - Foreign key table schema
- `FKTABLE_NAME` - Foreign key table name
- `FKCOLUMN_NAME` - Foreign key column name
- `KEY_SEQ` - Sequence number within foreign key
- `UPDATE_RULE` - What happens on UPDATE
- `DELETE_RULE` - What happens on DELETE
- `FK_NAME` - Foreign key name
- `PK_NAME` - Primary key name
- `DEFERRABILITY` - Can evaluation be deferred until commit

### Indexes

Retrieve index information for a table:

```js
bx:dbInfo
    type="index"
    name="employeeIndexes"
    table="employees"
    datasource="myDB";

for ( idx in employeeIndexes ) {
    output = "<p>Index: #idx.INDEX_NAME# on #idx.COLUMN_NAME#";
    if ( !idx.NON_UNIQUE ) {
        output &= " (Unique)";
    }
    output &= "</p>";
    writeOutput( output );
}
```

**Result Columns:**
- `TABLE_CAT` - Table catalog
- `TABLE_SCHEM` - Table schema
- `TABLE_NAME` - Table name
- `NON_UNIQUE` - Boolean, false if index values must be unique
- `INDEX_QUALIFIER` - Index catalog
- `INDEX_NAME` - Index name
- `TYPE` - Index type (tableIndexStatistic, tableIndexClustered, etc.)
- `ORDINAL_POSITION` - Column sequence within index
- `COLUMN_NAME` - Column name
- `ASC_OR_DESC` - "A" for ascending, "D" for descending
- `CARDINALITY` - Number of unique values in index
- `PAGES` - Number of pages used for index
- `FILTER_CONDITION` - Filter condition, if any

### Stored Procedures

List stored procedures available in the database:

```js
bx:dbInfo
    type="procedures"
    name="allProcedures"
    datasource="myDB";

// Filter by pattern
bx:dbInfo
    type="procedures"
    name="userProcedures"
    pattern="sp_user_%"
    datasource="myDB";

for ( proc in userProcedures ) {
    writeOutput( "<p>#proc.PROCEDURE_NAME# - #proc.REMARKS#</p>" );
}
```

**Result Columns:**
- `PROCEDURE_CAT` - Procedure catalog
- `PROCEDURE_SCHEM` - Procedure schema
- `PROCEDURE_NAME` - Procedure name
- `REMARKS` - Explanatory comment
- `PROCEDURE_TYPE` - Procedure type (procedureResultUnknown, procedureNoResult, procedureReturnsResult)

### Database Version

Get version information about the database and JDBC driver:

```js
bx:dbInfo
    type="version"
    name="versionInfo"
    datasource="myDB";

writeOutput( "<p>Database: #versionInfo.DATABASE_PRODUCTNAME# #versionInfo.DATABASE_VERSION#</p>" );
writeOutput( "<p>JDBC Driver: #versionInfo.DRIVER_NAME# #versionInfo.DRIVER_VERSION#</p>" );
writeOutput( "<p>JDBC Version: #versionInfo.JDBC_MAJOR_VERSION#.#versionInfo.JDBC_MINOR_VERSION#</p>" );
```

**Result Columns:**
- `DATABASE_PRODUCTNAME` - Database product name (e.g., "MySQL", "PostgreSQL")
- `DATABASE_VERSION` - Database version string
- `DRIVER_NAME` - JDBC driver name
- `DRIVER_VERSION` - JDBC driver version
- `JDBC_MAJOR_VERSION` - JDBC major version number
- `JDBC_MINOR_VERSION` - JDBC minor version number

## 🎯 Complete Examples

### Dynamic Table Browser

```js
// List all tables
bx:dbInfo type="tables" name="tables" datasource="myDB";

writeOutput( "<h2>Database Tables</h2>" );

for ( table in tables ) {
    writeOutput( "<h3>#table.TABLE_NAME# (#table.TABLE_TYPE#)</h3>" );

    // Get columns for this table
    bx:dbInfo
        type="columns"
        name="columns"
        table=table.TABLE_NAME
        datasource="myDB";

    writeOutput( "<table><thead><tr>" );
    writeOutput( "<th>Column</th><th>Type</th><th>Size</th><th>Nullable</th><th>Default</th><th>Keys</th>" );
    writeOutput( "</tr></thead><tbody>" );

    for ( col in columns ) {
        keys = "";
        if ( col.IS_PRIMARYKEY ) keys &= "PK ";
        if ( col.IS_FOREIGNKEY ) keys &= "FK";

        writeOutput( "<tr>" );
        writeOutput( "<td>#col.COLUMN_NAME#</td>" );
        writeOutput( "<td>#col.TYPE_NAME#</td>" );
        writeOutput( "<td>#col.COLUMN_SIZE#</td>" );
        writeOutput( "<td>#col.IS_NULLABLE#</td>" );
        writeOutput( "<td>#col.COLUMN_DEF#</td>" );
        writeOutput( "<td>#keys#</td>" );
        writeOutput( "</tr>" );
    }

    writeOutput( "</tbody></table>" );
}
```

### Schema Documentation Generator

```js
bx:dbInfo type="tables" name="tables" datasource="myDB";

writeOutput( "<h1>Database Schema Documentation</h1>" );

// Group tables by type
tablesByType = {};
for ( table in tables ) {
    if ( !structKeyExists( tablesByType, table.TABLE_TYPE ) ) {
        tablesByType[ table.TABLE_TYPE ] = [];
    }
    tablesByType[ table.TABLE_TYPE ].append( table );
}

for ( tableType in tablesByType ) {
    writeOutput( "<h2>#tableType#</h2>" );

    for ( table in tablesByType[ tableType ] ) {
        writeOutput( "<h3>#table.TABLE_NAME#</h3>" );
        writeOutput( "<p><em>#table.REMARKS#</em></p>" );

        // Column details
        bx:dbInfo
            type="columns"
            name="cols"
            table=table.TABLE_NAME
            datasource="myDB";

        writeOutput( "<h4>Columns</h4><ul>" );
        for ( col in cols ) {
            colDef = "<strong>#col.COLUMN_NAME#</strong> (#col.TYPE_NAME#";
            if ( col.COLUMN_SIZE > 0 ) colDef &= "(#col.COLUMN_SIZE#)";
            colDef &= ")";
            if ( col.IS_NULLABLE == "NO" ) colDef &= " NOT NULL";
            if ( len( col.COLUMN_DEF ) ) colDef &= " DEFAULT #col.COLUMN_DEF#";
            writeOutput( "<li>#colDef#</li>" );
        }
        writeOutput( "</ul>" );

        // Foreign keys
        bx:dbInfo
            type="foreignkeys"
            name="fks"
            table=table.TABLE_NAME
            datasource="myDB";

        if ( fks.recordCount > 0 ) {
            writeOutput( "<h4>Foreign Keys</h4><ul>" );
            for ( fk in fks ) {
                writeOutput( "<li>#fk.FKCOLUMN_NAME# → #fk.PKTABLE_NAME#.#fk.PKCOLUMN_NAME#</li>" );
            }
            writeOutput( "</ul>" );
        }

        // Indexes
        bx:dbInfo
            type="index"
            name="idxs"
            table=table.TABLE_NAME
            datasource="myDB";

        if ( idxs.recordCount > 0 ) {
            writeOutput( "<h4>Indexes</h4><ul>" );
            // Group by index name
            indexGroups = {};
            for ( idx in idxs ) {
                if ( !structKeyExists( indexGroups, idx.INDEX_NAME ) ) {
                    indexGroups[ idx.INDEX_NAME ] = {
                        unique: !idx.NON_UNIQUE,
                        columns: []
                    };
                }
                indexGroups[ idx.INDEX_NAME ].columns.append( idx.COLUMN_NAME );
            }
            for ( indexName in indexGroups ) {
                indexInfo = indexGroups[ indexName ];
                output = "<li>#indexName#";
                if ( indexInfo.unique ) output &= " (Unique)";
                output &= " on (#indexInfo.columns.toList()#)</li>";
                writeOutput( output );
            }
            writeOutput( "</ul>" );
        }

        writeOutput( "<hr>" );
    }
}
```

### Table Relationship Mapper

```js
bx:dbInfo type="tables" name="tables" datasource="myDB";

writeOutput( "<h2>Database Relationships</h2>" );

for ( table in tables ) {
    bx:dbInfo
        type="foreignkeys"
        name="fks"
        table=table.TABLE_NAME
        datasource="myDB";

    if ( fks.recordCount > 0 ) {
        writeOutput( "<h3>#table.TABLE_NAME#</h3><ul>" );
        for ( fk in fks ) {
            writeOutput( "<li>" );
            writeOutput( "<code>#fk.FKCOLUMN_NAME#</code> references " );
            writeOutput( "<strong>#fk.PKTABLE_NAME#</strong>.<code>#fk.PKCOLUMN_NAME#</code>" );
            writeOutput( "<br><small>On Update: #fk.UPDATE_RULE# | On Delete: #fk.DELETE_RULE#</small>" );
            writeOutput( "</li>" );
        }
        writeOutput( "</ul>" );
    }
}
```

### Database Comparison Tool

```js
// Compare two databases
dbInfo1 = [];
dbInfo2 = [];

// Get table lists
dbInfo type="tables" name="local:dbInfo1" datasource="prodDB";
dbInfo type="tables" name="local:dbInfo2" datasource="devDB";

// Find differences
prodTables = queryColumnData( dbInfo1, "TABLE_NAME" );
devTables = queryColumnData( dbInfo2, "TABLE_NAME" );

// Tables in prod but not dev
missingInDev = [];
for ( tableName in prodTables ) {
    if ( !arrayContains( devTables, tableName ) ) {
        missingInDev.append( tableName );
    }
}

// Tables in dev but not prod
extraInDev = [];
for ( tableName in devTables ) {
    if ( !arrayContains( prodTables, tableName ) ) {
        extraInDev.append( tableName );
    }
}

writeOutput( "Tables missing in dev: " & missingInDev.toList() );
writeOutput( "Extra tables in dev: " & extraInDev.toList() );
```

## 🛠️ Component Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `type` | string | Yes | Type of metadata: "dbnames", "tables", "columns", "foreignkeys", "index", "procedures", or "version" |
| `name` | string | Yes | Variable name to store the result query |
| `datasource` | string | No | Datasource name (uses default if not specified) |
| `table` | string | Conditional | Table name (required for "columns", "foreignkeys", "index") |
| `pattern` | string | No | Table name pattern using wildcards (%, _) or schema.table syntax |
| `dbname` | string | No | Database name (defaults to connection database) |
| `filter` | string | No | Table type filter (TABLE, VIEW, etc.) - only for type="tables" |

## 💡 Best Practices

### Pattern Matching
- ✅ **Use wildcards** for flexible table matching: `user_%` matches all tables starting with "user_"
- ✅ **Specify schema** when needed: `public.%` for all tables in public schema
- ✅ **Cache metadata** for static schemas to avoid repeated queries

### Performance
- ✅ **Filter by pattern** instead of retrieving all tables
- ✅ **Use specific queries** (columns for one table vs all tables)
- ✅ **Cache results** for metadata that doesn't change often
- ✅ **Limit scope** with database and schema names

### Error Handling
- ✅ **Check table existence** before querying columns
- ✅ **Handle empty results** gracefully
- ✅ **Validate user input** before using in patterns
- ✅ **Test with different databases** - metadata structure varies

### Security
- ✅ **Limit permissions** - don't grant metadata access unnecessarily
- ✅ **Sanitize patterns** - prevent injection via pattern strings
- ✅ **Audit usage** - log metadata queries in production
- ✅ **Filter sensitive tables** from user-facing tools

## 🚫 Common Pitfalls

❌ **Not handling NULL values in metadata**
```js
// BAD - may cause errors
writeOutput( "<p>Remarks: #table.REMARKS#</p>" );

// GOOD - handle NULLs
writeOutput( "<p>Remarks: #table.REMARKS ?: 'No description'#</p>" );
```

❌ **Forgetting required attributes**
```js
// BAD - missing table attribute
bx:dbInfo type="columns" name="cols";

// GOOD
bx:dbInfo type="columns" name="cols" table="employees";
```

❌ **Not checking for empty results**
```js
// BAD - may cause errors on empty query
writeOutput( "<p>First table: #tables[ 1 ].TABLE_NAME#</p>" );

// GOOD - check first
if ( tables.recordCount > 0 ) {
    writeOutput( "<p>First table: #tables[ 1 ].TABLE_NAME#</p>" );
} else {
    writeOutput( "<p>No tables found</p>" );
}
```

## 🔗 Related Documentation

- [Datasources](datasources.md) - Configure database connections
- [Querying](querying.md) - Execute SQL queries
- [bx:dbInfo Component](../../boxlang-language/reference/components/jdbc/DBInfo.md) - Complete component reference
- [Query Type Reference](../../boxlang-language/reference/types/query.md) - Working with query results
