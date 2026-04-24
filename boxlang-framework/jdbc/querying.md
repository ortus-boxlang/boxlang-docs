---
description: Execute SQL queries against databases using queryExecute() or bx:query component
icon: magnifying-glass
---

# 🔍 Querying Databases

BoxLang provides powerful and flexible ways to execute SQL queries against your databases. You can use either the `queryExecute()` Built-In Function (BIF) or the `bx:query` component, both offering the same capabilities with different syntax styles.

## 📋 Overview

Database querying in BoxLang supports:

- **Parameterized Queries** - Prevent SQL injection with bound parameters
- **Multiple Return Types** - Get results as query objects, arrays, or structs
- **Query Caching** - Cache frequently-used queries for performance
- **Query of Queries (QoQ)** - Execute SQL against in-memory result sets
- **Flexible Syntax** - Choose between BIF and component styles
- **Connection Pooling** - Automatic connection management via HikariCP

## 🔧 Query Execution Methods

### Using queryExecute() BIF

The `queryExecute()` function is the preferred method for script-based code:

```js
// Basic query
employees = queryExecute( "SELECT * FROM employees" );

// With positional parameters
employee = queryExecute(
    "SELECT * FROM employees WHERE id = ?",
    [ 42 ]
);

// With named parameters
salesTeam = queryExecute(
    "SELECT * FROM employees WHERE department = :dept AND salary > :minSalary",
    {
        dept: "Sales",
        minSalary: 50000
    }
);

// With options
result = queryExecute(
    "SELECT * FROM products WHERE category = ?",
    [ "Electronics" ],
    {
        datasource: "myDB",
        returntype: "array",
        maxrows: 100
    }
);
```

### Using bx:query Component

The `bx:query` component is ideal for template-based code islands, or when you prefer XML-style syntax.  Please also note that you can also use the `bx:query` component inside script code as well.

```js
bx:query name="employees" datasource="myDB"{
    SELECT * FROM employees
    WHERE department = bx:queryParam value="#dept#" sqltype="varchar"{}
    ORDER BY lastName
}
```

```xml
<bx:query name="employees" datasource="myDB">
    SELECT * FROM employees
    WHERE department = <bx:queryParam value="#dept#" sqltype="varchar">
    ORDER BY lastName
</bx:query>

<!-- With result capture -->
<bx:query name="products" datasource="myDB" result="queryInfo">
    SELECT * FROM products
    WHERE price > <bx:queryParam value="#minPrice#" sqltype="decimal">
</bx:query>

<p>Query executed in #queryInfo.executionTime# ms</p>
<p>Returned #queryInfo.recordCount# rows</p>
```

## 🛡️ Parameterized Queries

**Always** use query parameters for user input to prevent SQL injection attacks.

### Positional Parameters

Use `?` placeholders and provide values in an array:

```js
queryExecute(
    "SELECT * FROM users WHERE username = ? AND active = ?",
    [ username, true ]
);
```

### Named Parameters

Use `:paramName` placeholders and provide values in a struct:

```js
queryExecute(
    "SELECT * FROM orders WHERE customerId = :id AND orderDate > :date",
    {
        id: customerId,
        date: createDate( 2024, 1, 1 )
    }
);
```

### bx:queryParam Component

For template syntax, use `bx:queryParam` for type-safe parameter binding:

```xml
<bx:query name="results">
    SELECT * FROM products
    WHERE category = <bx:queryParam value="#category#" sqltype="varchar">
    AND price BETWEEN <bx:queryParam value="#minPrice#" sqltype="decimal">
                  AND <bx:queryParam value="#maxPrice#" sqltype="decimal">
    AND inStock = <bx:queryParam value="#true#" sqltype="bit">
</bx:query>
```

### Advanced Parameter Options

Parameters can include additional options for fine-grained control:

```js
queryExecute(
    "SELECT * FROM products WHERE id IN (:ids) AND name LIKE :pattern",
    {
        ids: {
            value: [ 1, 2, 3, 4, 5 ],
            type: "integer",
            list: true,
            separator: ","
        },
        pattern: {
            value: "Widget%",
            type: "varchar",
            maxLength: 50
        }
    }
);
```

**Parameter Options:**
- `value` - The parameter value
- `type` - SQL type (varchar, integer, decimal, date, timestamp, bit, etc.)
- `null` - Set to true for NULL values
- `list` - Set to true for IN clause lists
- `separator` - List separator (default: ",")
- `maxLength` - Maximum length for string types
- `scale` - Decimal scale for numeric types

## 📊 Return Types

Control how query results are returned using the `returntype` option.

### Query Object (Default)

Returns a BoxLang [Query object](../../boxlang-language/queries.md) with rows accessible via array notation:

```js
employees = queryExecute( "SELECT * FROM employees" );

for ( row in employees ) {
    echo( row.firstName & " " & row.lastName );
}

// Access specific row
firstEmployee = employees[ 1 ];

// Get column as array
names = employees[ "firstName" ];
```

### Array of Structs

Returns an array where each element is a struct representing a row:

```js
employees = queryExecute(
    "SELECT * FROM employees",
    [],
    { returntype: "array" }
);

for ( employee in employees ) {
    echo( employee.firstName & " " & employee.lastName );
}
```

### Struct (Keyed by Column)

Returns a struct keyed by a specific column, with each value being a struct of the row data:

```js
employees = queryExecute(
    "SELECT * FROM employees",
    [],
    {
        returntype: "struct",
        columnKey: "id"
    }
);

// Access by employee ID
employee42 = employees[ 42 ];
echo( employee42.firstName );
```

## ⚡ Query Caching

Cache frequently-executed queries to improve performance:

```js
// Cache for 1 hour
products = queryExecute(
    "SELECT * FROM products WHERE active = ?",
    [ true ],
    {
        cache: true,
        cacheTimeout: createTimeSpan( 0, 1, 0, 0 )
    }
);

// Custom cache key
categories = queryExecute(
    "SELECT * FROM categories ORDER BY name",
    [],
    {
        cache: true,
        cacheKey: "all_categories",
        cacheTimeout: createTimeSpan( 1, 0, 0, 0 ), // 1 day
        cacheProvider: "default"
    }
);
```

**Cache Options:**
- `cache` - Enable caching (boolean)
- `cacheKey` - Custom cache key (defaults to SQL hash)
- `cacheTimeout` - Time-to-live duration
- `cacheLastAccessTimeout` - Idle timeout
- `cacheProvider` - Named cache provider to use

{% hint style="warning" %}
Be cautious caching queries with user-specific data. Cache keys should include relevant user identifiers when needed.
{% endhint %}

### Cache Timeouts

Note cache timeout behavior varies based on duration values:
- **Positive duration** - Cache for specified duration - `createTimeSpan( 0, 1, 0, 0 )`
- **Zero** - Cache indefinitely - `createTimeSpan( 0, 0, 0, 0 )`
- **Negative duration** - Never cache - `createTimeSpan( 0, 0, 0, -1 )`

## 🔄 Query of Queries (QoQ)

Execute SQL queries against in-memory query objects without hitting the database:

```js
// Get all employees from database
allEmployees = queryExecute( "SELECT * FROM employees" );

// Filter in-memory using SQL
salesTeam = queryExecute(
    "SELECT firstName, lastName, salary
     FROM allEmployees
     WHERE department = ?
     ORDER BY salary DESC",
    [ "Sales" ],
    { dbtype: "query" }
);

// Join multiple queries in memory
employeeOrders = queryExecute(
    "SELECT e.firstName, e.lastName, o.orderDate, o.total
     FROM employees e
     INNER JOIN orders o ON e.id = o.employeeId
     WHERE o.orderDate > ?
     ORDER BY o.orderDate DESC",
    [ createDate( 2024, 1, 1 ) ],
    { dbtype: "query" }
);
```

**QoQ Features:**
- Standard SQL syntax (SELECT, WHERE, ORDER BY, GROUP BY, JOIN)
- Aggregation functions (COUNT, SUM, AVG, MIN, MAX)
- No database round-trips
- Ideal for filtering, sorting, and transforming result sets

**QoQ Limitations:**
- Limited SQL function support compared to full databases
- No transaction support
- Performance depends on result set size

## 📈 Query Result Information

Capture metadata about query execution using the `result` option:

```js
queryExecute(
    "SELECT * FROM employees",
    [],
    { result: "queryInfo" }
);

// Access execution metadata
echo( "Execution time: " & queryInfo.executionTime & " ms" );
echo( "Record count: " & queryInfo.recordCount );
echo( "Cached: " & queryInfo.cached );
echo( "SQL: " & queryInfo.sql );
```

**Result Struct Properties:**
- `recordCount` - Number of rows returned
- `columnList` - Comma-delimited list of columns
- `executionTime` - Query execution time in milliseconds
- `cached` - Boolean indicating if result was cached
- `sql` - The SQL statement executed
- `sqlParameters` - Array of bound parameter values

## 🎛️ Query Options

Complete list of options available for `queryExecute()` and `bx:query`:

| Option | Type | Description |
|--------|------|-------------|
| `datasource` | string | Datasource name or inline struct |
| `dbtype` | string | "query" for QoQ, "hql" for Hibernate |
| `returntype` | string | "query", "array", or "struct" |
| `columnKey` | string | Column to use as struct key (when returntype="struct") |
| `maxrows` | integer | Maximum rows to return |
| `timeout` | integer | Query timeout in seconds |
| `cache` | boolean | Enable query caching |
| `cacheKey` | string | Custom cache key |
| `cacheTimeout` | duration | Cache time-to-live |
| `cacheLastAccessTimeout` | duration | Cache idle timeout |
| `cacheProvider` | string | Named cache provider |
| `result` | string | Variable name to store execution metadata |
| `username` | string | Override datasource username |
| `password` | string | Override datasource password |
| `fetchsize` | integer | Number of rows to fetch at once |

## 📊 Query Metadata

Every query result has metadata that provides information about the query execution, columns, and result set. You can access this metadata using the `getMetadata()` function or the query's `$bx.meta` property.

### Accessing Query Metadata

```js
// Execute a query
employees = queryExecute( "SELECT * FROM employees WHERE active = ?", [ true ] );

// Get metadata using getMetadata() BIF
meta = getMetadata( employees );

// Or access directly via the query object
meta = employees.getMetadata();

// Access via $bx.meta property
meta = employees.$bx.meta;
```

### Metadata Structure

Query metadata includes the following keys:

| Key | Type | Description |
|-----|------|-------------|
| `type` | string | Always "Query" |
| `recordCount` | integer | Number of rows in the result set |
| `columnList` | string | Comma-delimited list of column names |
| `columnMetadata` | struct | Detailed information about each column |
| `executionTime` | integer | Query execution time in milliseconds |
| `cached` | boolean | Whether the result was retrieved from cache |
| `cacheKey` | string | Cache key if query was cached |
| `cacheProvider` | string | Cache provider name if cached |
| `cacheTimeout` | duration | Cache time-to-live duration |
| `cacheLastAccessTimeout` | duration | Cache idle timeout duration |
| `sql` | string | The executed SQL statement (when available) |
| `sqlParameters` | array | Bound parameter values (when available) |
| `_HASHCODE` | integer | Java hashcode of the query object |

### Column Metadata

The `columnMetadata` key contains detailed information about each column:

```js
employees = queryExecute( "SELECT id, firstName, lastName, salary FROM employees" );
meta = getMetadata( employees );

// Access column metadata
for ( column in meta.columnMetadata ) {
    writeOutput( "Column: #column.name#<br>" );
    writeOutput( "Type: #column.type#<br>" );
    writeOutput( "SQL Type: #column.sqltype#<br>" );
    writeOutput( "Index: #column.index#<br><br>" );
}
```

Each column has the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Column name |
| `type` | string | BoxLang type (String, Integer, Double, DateTime, etc.) |
| `sqltype` | string | JDBC SQL type (VARCHAR, INTEGER, DECIMAL, TIMESTAMP, etc.) |
| `index` | integer | Zero-based column index in the result set |

### Practical Examples

#### Display Query Information

```js
result = queryExecute(
    "SELECT * FROM products WHERE category = ?",
    [ "Electronics" ],
    { cache: true, cacheTimeout: createTimeSpan( 0, 1, 0, 0 ) }
);

meta = getMetadata( result );

writeOutput( "Records returned: #meta.recordCount#<br>" );
writeOutput( "Execution time: #meta.executionTime# ms<br>" );
writeOutput( "Cached: #meta.cached#<br>" );
writeOutput( "Columns: #meta.columnList#<br>" );
```

#### Debug Query Columns

```xml
<bx:query name="employees">
    SELECT id, firstName, lastName, department, salary, hireDate
    FROM employees
</bx:query>

<bx:set meta = getMetadata( employees )>

<table>
    <thead>
        <tr>
            <th>Column Name</th>
            <th>BoxLang Type</th>
            <th>SQL Type</th>
            <th>Position</th>
        </tr>
    </thead>
    <tbody>
        <bx:loop collection="#meta.columnMetadata#" item="colName" index="colMeta">
            <tr>
                <td>#colMeta.name#</td>
                <td>#colMeta.type#</td>
                <td>#colMeta.sqltype#</td>
                <td>#colMeta.index + 1#</td>
            </tr>
        </bx:loop>
    </tbody>
</table>
```

#### Cache Performance Monitoring

```js
function getCachedData() {
    result = queryExecute(
        "SELECT * FROM statistics",
        [],
        {
            cache: true,
            cacheKey: "daily_stats",
            cacheTimeout: createTimeSpan( 1, 0, 0, 0 )
        }
    );

    meta = getMetadata( result );

    if ( meta.cached ) {
        writeLog( "Cache HIT for daily_stats - saved #meta.executionTime#ms" );
    } else {
        writeLog( "Cache MISS for daily_stats - executed in #meta.executionTime#ms" );
    }

    return result;
}
```

#### Dynamic Column Mapping

```js
// Query from unknown source
data = queryExecute( "SELECT * FROM dynamic_table" );
meta = getMetadata( data );

// Build column mapping based on metadata
columnMapping = {};
for ( column in meta.columnMetadata ) {
    columnMapping[ column.name ] = {
        type: column.type,
        sqltype: column.sqltype,
        position: column.index
    };
}

// Use mapping for data transformation
transformed = data.map( ( row ) => {
    result = {};
    for ( col in columnMapping ) {
        // Transform based on type
        if ( columnMapping[ col ].type == "DateTime" ) {
            result[ col ] = dateFormat( row[ col ], "yyyy-mm-dd" );
        } else {
            result[ col ] = row[ col ];
        }
    }
    return result;
} );
```

#### Query Comparison Tool

```js
// Compare two query structures
function compareQueryStructures( query1, query2 ) {
    meta1 = getMetadata( query1 );
    meta2 = getMetadata( query2 );

    differences = [];

    // Compare column counts
    if ( meta1.recordCount != meta2.recordCount ) {
        differences.append( "Record count mismatch: #meta1.recordCount# vs #meta2.recordCount#" );
    }

    // Compare column lists
    if ( meta1.columnList != meta2.columnList ) {
        differences.append( "Column list mismatch" );
    }

    // Compare column types
    for ( colName in meta1.columnMetadata ) {
        if ( structKeyExists( meta2.columnMetadata, colName ) ) {
            col1 = meta1.columnMetadata[ colName ];
            col2 = meta2.columnMetadata[ colName ];

            if ( col1.type != col2.type ) {
                differences.append(
                    "Column #colName# type mismatch: #col1.type# vs #col2.type#"
                );
            }
        } else {
            differences.append( "Column #colName# missing in second query" );
        }
    }

    return differences;
}
```

### Metadata in Result Variable

When using the `result` parameter, execution metadata is automatically captured:

```js
queryExecute(
    "UPDATE employees SET salary = ? WHERE id = ?",
    [ newSalary, employeeId ],
    { result: "updateResult" }
);

// Result variable contains:
writeOutput( "Rows updated: #updateResult.recordCount#<br>" );
writeOutput( "Execution time: #updateResult.executionTime# ms<br>" );
writeOutput( "SQL: #updateResult.sql#<br>" );

// For INSERT with generated keys
queryExecute(
    "INSERT INTO employees (firstName, lastName) VALUES (?, ?)",
    [ "John", "Doe" ],
    { result: "insertResult" }
);

writeOutput( "Generated ID: #insertResult.generatedKey#<br>" );
```

### Best Practices for Metadata

- ✅ **Use metadata for debugging** - Check execution times and column information during development
- ✅ **Monitor cache performance** - Log cache hits/misses in production
- ✅ **Validate data structures** - Compare expected vs actual column types
- ✅ **Dynamic data handling** - Use column metadata for generic data processors
- ❌ **Don't access metadata unnecessarily** - Small performance cost for metadata generation
- ❌ **Don't store metadata long-term** - Query structure may change over time

## 💡 Best Practices

### Security
- ✅ **Always use query parameters** for user input
- ✅ **Never concatenate** user input into SQL strings
- ✅ **Validate input** before querying
- ✅ **Use environment variables** for credentials

### Performance
- ✅ **Use connection pooling** (automatic with datasources)
- ✅ **Cache static queries** (categories, lookups, etc.)
- ✅ **Limit result sets** with `maxrows` when appropriate
- ✅ **Use QoQ** for in-memory filtering instead of multiple DB queries
- ✅ **Index database columns** used in WHERE clauses

### Code Quality
- ✅ **Use consistent syntax** (BIF or component, not mixed)
- ✅ **Name result variables** descriptively
- ✅ **Capture execution metadata** for debugging
- ✅ **Handle empty result sets** gracefully

### Anti-Patterns
- ❌ **Don't use string concatenation** for SQL building
- ❌ **Don't cache user-specific data** without proper keying
- ❌ **Don't fetch all rows** when you only need a few
- ❌ **Don't ignore errors** - wrap in try/catch for critical operations

## 🔗 Related Documentation

- [Datasources](datasources.md) - Configure database connections
- [Transactions](transactions.md) - Manage database transactions
- [Query Type Reference](../../boxlang-language/reference/types/query.md) - Query object methods
- [queryExecute() BIF](../../boxlang-language/reference/built-in-functions/jdbc/QueryExecute.md) - Complete BIF reference
- [bx:query Component](../../boxlang-language/reference/components/jdbc/Query.md) - Complete component reference

## 📚 Examples

### Pagination

```js
page = 1;
pageSize = 20;
offset = ( page - 1 ) * pageSize;

results = queryExecute(
    "SELECT * FROM products
     WHERE active = ?
     ORDER BY name
     LIMIT ? OFFSET ?",
    [ true, pageSize, offset ]
);
```

### Dynamic WHERE Clauses

```js
sql = "SELECT * FROM products WHERE 1=1";
params = [];

if ( structKeyExists( form, "category" ) ) {
    sql &= " AND category = ?";
    params.append( form.category );
}

if ( structKeyExists( form, "minPrice" ) ) {
    sql &= " AND price >= ?";
    params.append( form.minPrice );
}

results = queryExecute( sql, params );
```

### Batch Processing

```js
batchSize = 1000;
offset = 0;

do {
    batch = queryExecute(
        "SELECT * FROM orders WHERE processed = ? LIMIT ? OFFSET ?",
        [ false, batchSize, offset ],
        { returntype: "array" }
    );

    for ( order in batch ) {
        processOrder( order );
    }

    offset += batchSize;
} while ( !batch.isEmpty() );
```
