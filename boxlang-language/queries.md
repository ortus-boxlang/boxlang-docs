---
description: BoxLang provides the easiest way to query databases with powerful SQL execution and manipulation capabilities
icon: database
---

# 🗄️ Queries

A **query** is a BoxLang data type that represents tabular data from database operations or programmatic construction. It stores rows and columns of data along with metadata about the query execution and structure.

CFML became famous in its infancy because it was easy to query databases with a simple `cfquery` tag and no verbose ceremonious coding. BoxLang continues this tradition while adding modern features like functional programming operations, query metadata access, and flexible datasource configuration.

{% hint style="info" %}
**Java Interoperability**: BoxLang queries implement Java's `Collection<IStruct>` interface, making them compatible with Java collection operations and frameworks. Each row can be treated as a `Map<Key, Object>` in Java code.
{% endhint %}

{% hint style="success" %}
All BoxLang queries are passed to functions as memory references, not values. Keep that in mind when working with queries. There is also the `passby=reference|value` attribute to function arguments where you can decide whether to pass by reference or value.
{% endhint %}

## 📋 Table of Contents

- [Queries in Code](#queries-in-code)
- [Creating Queries](#creating-queries)
- [Query Execution](#query-execution)
- [Query Properties & Metadata](#query-properties--metadata)
- [Accessing Query Data](#accessing-query-data)
- [Functional Programming](#functional-programming)
- [Query Manipulation](#query-manipulation)
- [Best Practices](#best-practices)

## 💻 Queries in Code

Let's explore query creation and manipulation:

```js
// Create a query programmatically
users = queryNew(
    "id,name,email,age",
    "integer,varchar,varchar,integer",
    [
        { id: 1, name: "Alice", email: "alice@example.com", age: 30 },
        { id: 2, name: "Bob", email: "bob@example.com", age: 25 },
        { id: 3, name: "Charlie", email: "charlie@example.com", age: 35 }
    ]
);

// Access query properties
println( "Records: " & users.recordCount );
println( "Columns: " & users.columnList );
println( "First user: " & users.name[ 1 ] );

// Functional programming with queries
println( "--- Functional Operations ---" );

// Filter - get rows matching condition (returns new query)
adults = users.filter( ( row ) -> row.age >= 30 );
println( "Adults: " & adults.recordCount );

// Map - transform each row (returns array of transformed values)
emails = users.map( ( row ) -> row.email.ucase() );
println( "Emails: " & emails.toString() );

// Reduce - combine all rows into single value
totalAge = users.reduce( ( sum, row ) -> sum + row.age, 0 );
println( "Total age: " & totalAge );

// Each - perform action on each row
users.each( ( row, index ) => {
    println( "#index#: #row.name# (#row.age#)" );
} );

// Sort - order by column(s)
sortedUsers = users.sort( "age DESC, name ASC" );
println( "Sorted: " & sortedUsers.name.toList() );
```

Please note that all member functions can also be used as traditional [query functions](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/query). However, [member functions](https://boxlang.ortusbooks.com/getting-started/overview/syntax-style-guide#member-functions) look much better for readability.

## 📚 Query Built-In Functions (BIFs)

BoxLang provides a comprehensive set of query BIFs organized by functionality. All query BIFs can be called as member methods on Query objects.

### 🔨 Creation & Conversion Functions

| Function | Purpose | Example |
|----------|---------|----------|
| `queryNew()` | Create new query | `queryNew("id,name", "integer,varchar")` |
| `queryExecute()` | Execute SQL query | `queryExecute("SELECT * FROM users")` |
| `queryAddRow()` | Add row(s) | `queryAddRow(qry, {id:1, name:"John"})` |
| `queryAddColumn()` | Add column | `queryAddColumn(qry, "age", "integer")` |

### 🔍 Access & Retrieval Functions

| Function | Purpose | Example |
|----------|---------|----------|
| `queryGetCell()` | Get single cell value | `queryGetCell(qry, "name", 1)` → `"John"` |
| `querySetCell()` | Set single cell value | `querySetCell(qry, "name", "Jane", 1)` |
| `queryGetRow()` | Get row as struct | `queryGetRow(qry, 1)` → `{id:1, name:"John"}` |
| `querySetRow()` | Set entire row values | `querySetRow(qry, 1, {name:"Jane"})` |
| `queryRowData()` | Get row data (alias) | `queryRowData(qry, 1)` |
| `queryColumnData()` | Get column as array | `queryColumnData(qry, "name")` → `["John", "Jane"]` |
| `queryColumnArray()` | Get column as array | `queryColumnArray(qry, "name")` |

### 📊 Metadata Functions

| Function | Purpose | Example |
|----------|---------|----------|
| `queryRecordCount()` | Get row count | `queryRecordCount(qry)` → `10` |
| `queryColumnCount()` | Get column count | `queryColumnCount(qry)` → `5` |
| `queryColumnList()` | Get column names | `queryColumnList(qry)` → `"id,name,email"` |
| `queryColumnExists()` | Check if column exists | `queryColumnExists(qry, "age")` → `true` |
| `queryKeyExists()` | Check if key exists | `queryKeyExists(qry, "name")` → `true` |
| `queryCurrentRow()` | Get current row number | `queryCurrentRow(qry)` → `3` |
| `queryGetResult()` | Get execution metadata | `queryGetResult(qry)` → `{sql, executionTime, ...}` |

### ➕ Modification Functions

| Function | Purpose | Example |
|----------|---------|----------|
| `queryAddRow()` | Add row(s) | `queryAddRow(qry, 3)` adds 3 empty rows |
| `queryDeleteRow()` | Delete row | `queryDeleteRow(qry, 2)` |
| `queryInsertAt()` | Insert row at position | `queryInsertAt(qry, 2, {id:5})` |
| `queryRowSwap()` | Swap two rows | `queryRowSwap(qry, 1, 3)` |
| `queryAddColumn()` | Add column | `queryAddColumn(qry, "age", "integer")` |
| `queryDeleteColumn()` | Delete column | `queryDeleteColumn(qry, "age")` |
| `queryClear()` | Remove all rows | `queryClear(qry)` |
| `queryAppend()` | Append another query | `queryAppend(qry1, qry2)` |
| `queryPrepend()` | Prepend another query | `queryPrepend(qry1, qry2)` |

### 🔄 Functional Programming Functions

| Function | Purpose | Example |
|----------|---------|----------|
| `queryEach()` | Execute callback for each row | `queryEach(qry, (row) -> println(row.name))` |
| `queryMap()` | Transform each row | `queryMap(qry, (row) -> row.name.ucase())` |
| `queryFilter()` | Filter rows by condition | `queryFilter(qry, (row) -> row.age > 18)` |
| `queryReduce()` | Reduce to single value | `queryReduce(qry, (sum, row) -> sum + row.age, 0)` |
| `queryEvery()` | Test if all match | `queryEvery(qry, (row) -> row.age >= 18)` |
| `querySome()` | Test if any match | `querySome(qry, (row) -> row.age > 50)` |
| `queryNone()` | Test if none match | `queryNone(qry, (row) -> row.age < 0)` |

### 📐 Manipulation Functions

| Function | Purpose | Example |
|----------|---------|----------|
| `querySort()` | Sort by column(s) | `querySort(qry, "age DESC, name")` |
| `queryReverse()` | Reverse row order | `queryReverse(qry)` |
| `querySlice()` | Extract portion of rows | `querySlice(qry, 1, 10)` → first 10 rows |

### 🔧 Utility Functions

| Function | Purpose | Example |
|----------|---------|----------|
| `valueList()` | Column values as list | `valueList(qry, "name")` → `"John,Jane,Bob"` |
| `quotedValueList()` | Quoted column values | `quotedValueList(qry, "name")` → `"'John','Jane'"` |
| `queryRegisterFunction()` | Register function for QoQ | `queryRegisterFunction("myFunc", myUDF)` |

## 🎯 Core Java Methods

The `Query.java` class provides essential methods for direct query manipulation:

### Collection Interface Methods

| Method | Purpose | Returns |
|--------|---------|---------|
| `size()` | Get number of rows | `int` |
| `isEmpty()` | Check if query is empty | `boolean` |
| `contains(Object)` | Check if contains row data | `boolean` |
| `iterator()` | Get row iterator | `Iterator<IStruct>` |
| `toArray()` | Convert to array of row data | `Object[]` |
| `toArrayOfStructs()` | Convert to array of structs | `Array` |
| `add(IStruct)` | Add row as struct | `boolean` |
| `remove(Object)` | Remove row by object | `boolean` |
| `clear()` | Remove all rows | `void` |

### Query-Specific Methods

| Method | Purpose | Returns |
|--------|---------|---------|
| `addRow(Object[])` | Add row from array | `int` (row number) |
| `addRow(Array)` | Add row from Array | `int` |
| `addRow(IStruct)` | Add row from struct | `int` |
| `addRows(int)` | Add N empty rows | `int` (last row) |
| `addEmptyRow()` | Add one empty row | `int` |
| `deleteRow(int)` | Delete row at index | `Query` |
| `swapRow(int, int)` | Swap two rows | `Query` |
| `getRow(int)` | Get row as array | `Object[]` |
| `getRowAsStruct(int)` | Get row as struct | `IStruct` |
| `getCell(Key, int)` | Get cell value | `Object` |
| `setCell(Key, int, Object)` | Set cell value | `Query` |

### Column Methods

| Method | Purpose | Returns |
|--------|---------|---------|
| `addColumn(Key, QueryColumnType)` | Add column | `Query` |
| `addColumn(Key, QueryColumnType, Object[])` | Add column with data | `Query` |
| `deleteColumn(Key)` | Delete column | `void` |
| `getColumn(Key)` | Get QueryColumn object | `QueryColumn` |
| `getColumnMeta(Key)` | Get column metadata | `IStruct` |
| `getColumnMeta()` | Get all column metadata | `IStruct` |
| `getColumnData(Key)` | Get column data as array | `Object[]` |
| `getColumnDataAsArray(Key)` | Get column as BoxLang Array | `Array` |
| `getColumnIndex(Key)` | Get column position | `int` |
| `getColumnList()` | Get column names as string | `String` |
| `getColumnArray()` | Get column names as Array | `Array` |
| `getColumnNames()` | Get column names as Array | `Array` |
| `hasColumn(Key)` | Check if column exists | `boolean` |
| `hasColumns()` | Check if query has columns | `boolean` |

### Metadata & Duplication

| Method | Purpose | Returns |
|--------|---------|---------|
| `getMetaData()` | Get query metadata | `IStruct` |
| `setMetadata(IStruct)` | Set query metadata | `Query` |
| `duplicate()` | Shallow copy of query | `Query` |
| `duplicate(boolean)` | Shallow/deep copy | `Query` |
| `duplicate(IBoxContext)` | Context-aware copy | `Query` |
| `toUnmodifiable()` | Create immutable copy | `UnmodifiableQuery` |

### Advanced Methods

| Method | Purpose | Returns |
|--------|---------|---------|
| `sort(Comparator<IStruct>)` | Sort with comparator | `void` |
| `sortData(Comparator<Object[]>)` | Sort row arrays directly | `void` |
| `truncate(long)` | Keep only N rows | `Query` |
| `insertQueryAt(int, Query)` | Insert query at position | `Query` |
| `fromResultSet(BoxStatement, ResultSet)` | Create from JDBC ResultSet | `Query` (static) |
| `fromArray(Array, Array, Object)` | Create from arrays | `Query` (static) |

## 📖 What is a Query?

A query is a request to a database representing the results' rows and columns. It returns a BoxLang `query` object containing a **record set** and other metadata information about the query. The query can ask for information from the database, write new data to the database, update existing information in the database, or delete records from the database. This can be done in several ways:

* Using the `bx:query` component in script: `bx:query name="qItems" { SELECT * FROM table }`
* Using the `queryExecute()` function: `queryExecute("SELECT * FROM table")`

Here's an example of using the [default datasource](datasources.md#default-datasource) in script syntax:

```js
qItems = queryExecute(
    "SELECT QUANTITY, ITEM FROM CUPBOARD ORDER BY ITEM"
);
```

## 🔌 Datasource Configuration

BoxLang provides flexible datasource configuration options at multiple levels:

### Configuration Locations

1. **Global** - `boxlang.json` (runtime-wide)
2. **Application** - `Application.bx` (per-application)
3. **Inline** - Query-level (ad-hoc connections)

### Basic Datasource Structure

```js
this.datasources[ "myDB" ] = {
    driver   : "mysql",
    host     : "localhost",
    port     : "3306",
    database : "myapp",
    username : "dbuser",
    password : "dbpass"
};

// OR with JDBC URL
this.datasources[ "myDB" ] = {
    url      : "jdbc:mysql://localhost:3306/myapp?useSSL=false",
    username : "dbuser",
    password : "dbpass"
};
```

### Supported Database Drivers

| Driver | Example URL |
|--------|-------------|
| **MySQL** | `jdbc:mysql://localhost:3306/mydb` |
| **PostgreSQL** | `jdbc:postgresql://localhost:5432/mydb` |
| **Microsoft SQL Server** | `jdbc:sqlserver://localhost:1433;databaseName=mydb` |
| **Oracle** | `jdbc:oracle:thin:@localhost:1521:XE` |
| **Derby** | `jdbc:derby:memory:mydb;create=true` |
| **H2** | `jdbc:h2:mem:mydb` |
| **HyperSQL** | `jdbc:hsqldb:mem:mydb` |

### Connection Pool Options (HikariCP)

```js
this.datasources[ "myDB" ] = {
    driver              : "mysql",
    host                : "localhost",
    port                : "3306",
    database            : "myapp",
    username            : "dbuser",
    password            : "dbpass",
    // Connection pool settings
    maximumPoolSize     : 10,
    minimumIdle         : 2,
    connectionTimeout   : 30000,
    idleTimeout         : 600000,
    maxLifetime         : 1800000,
    validationTimeout   : 5000
};
```

### Default Datasource

```js
// Set default datasource
this.defaultDatasource = "myDB";

// Queries use default if not specified
users = queryExecute( "SELECT * FROM users" );
```

### Inline Datasource

```js
// Ad-hoc datasource in query
users = queryExecute(
    "SELECT * FROM users",
    {},
    {
        datasource: {
            driver   : "mysql",
            host     : "localhost",
            database : "tempdb",
            username : "user",
            password : "pass"
        }
    }
);
```

{% content-ref url="datasources.md" %}
[datasources.md](datasources.md)
{% endcontent-ref %}

{% content-ref url="../boxlang-framework/jdbc/" %}
[jdbc](../boxlang-framework/jdbc/)
{% endcontent-ref %}

## 🔄 Iterating Over Queries

The query object can be iterated on like a normal collection through various looping constructs:

### For-In Loop (Recommended)

```js
for ( row in qItems ) {
    println( "There are #row.quantity# #row.item# in the pantry" );
}
```

### Each with Closure

```js
qItems.each( ( row, index ) => {
    println( "#index#: There are #row.quantity# #row.item# in the pantry" );
} );
```

### Traditional Index Loop

```js
for ( i = 1; i <= qItems.recordCount; i++ ) {
    println( "There are #qItems.quantity[ i ]# #qItems.item[ i ]# in the pantry" );
}
```

### Array Notation Access

```js
// Access specific row and column
firstItem = qItems[ "item" ][ 1 ];
secondQuantity = qItems[ "quantity" ][ 2 ];

// Loop with array notation
for ( i = 1; i <= qItems.recordCount; i++ ) {
    item = qItems[ "item" ][ i ];
    quantity = qItems[ "quantity" ][ i ];
    println( "Item: #item#, Quantity: #quantity#" );
}
```

{% hint style="success" %}
**Best Practice**: Use for-in loops or `each()` for cleaner, more readable code. Reserve index-based loops for when you need precise position control.
### 🚀 Multi-Threaded Looping

BoxLang allows you to leverage the `each()` operations in a multi-threaded fashion. The `queryEach()` or `each()` functions allow for `parallel` and `maxThreads` arguments so the iteration can happen concurrently:

```js
queryEach( qry, callback, parallel:boolean, maxThreads:numeric );
qry.each( callback, parallel:boolean, maxThreads:numeric );
```

**Example:**

```js
users.each( ( row ) => {
    userService.process( row );
}, true, 20 );
```

{% hint style="warning" %}
**Thread Safety Warning**: When using parallel execution, ensure proper var scoping and implement appropriate locking strategies. Thread concurrency requires careful attention to shared state and race conditions.
{% endhint %}

{% hint style="info" %}
**Limitation**: This approach uses a single thread executor per execution and does not provide exception handling across threads. For production-grade parallel processing, consider BoxLang's async programming features instead.
{% endhint %}

### ⚡ BoxLang Async Programming (Recommended for Parallel Operations)

For a functional and much more flexible approach to multi-threaded or parallel programming, use BoxLang's built-in async programming constructs, which leverage the Java Concurrency and CompletableFutures frameworks.

{% content-ref url="../boxlang-framework/asynchronous-programming/" %}
[asynchronous-programming](../boxlang-framework/asynchronous-programming/)
{% endcontent-ref %}

**Key async methods for parallel query processing:**
## 🔒 Using Query Parameters (Preventing SQL Injection)

When using user input in queries, you must prevent [SQL injection attacks](https://owasp.org/www-community/attacks/SQL_Injection). BoxLang provides query parameters for safe SQL execution.

{% hint style="danger" %}
**Security Critical**: Never concatenate user input directly into SQL strings! Always use query parameters.
{% endhint %}

### Named Parameters (Recommended)

```js
// Named parameter with automatic type binding
result = queryExecute(
    "SELECT quantity, item FROM cupboard WHERE item_id = :itemID",
    { itemID: { value: arguments.itemID, sqltype: "integer" } }
);

// Multiple named parameters
users = queryExecute(
    "SELECT * FROM users WHERE age >= :minAge AND status = :status",
    {
        minAge: { value: 18, sqltype: "integer" },
        status: { value: "active", sqltype: "varchar" }
    }
);
```

### Positional Parameters

```js
// Positional placeholders with ?
result = queryExecute(
    "SELECT quantity, item FROM cupboard WHERE item_id = ?",
    [ { value: arguments.itemID, sqltype: "integer" } ]
);

// Multiple positional parameters
users = queryExecute(
    "SELECT * FROM users WHERE age >= ? AND status = ?",
    [
        { value: 18, sqltype: "integer" },
        { value: "active", sqltype: "varchar" }
    ]
);
```

### Using bx:queryParam Component

```js
bx:query name="result" {
    writeOutput("
        SELECT * FROM users
        WHERE age >= ");
    bx:queryParam value=18 sqltype="integer";
    writeOutput(" AND email LIKE ");
    bx:queryParam value="%@example.com" sqltype="varchar";
}
``` .get();
```em and must return a result. Consider this a parallel `map()` operation.
* `anyOf( a1, a2, ... ):Future` : This method accepts an infinite amount of future objects, closures, or an array of closures/futures and will execute them in parallel. However, instead of returning all of the results in an array like `all()`, this method will return the future that executes the fastest! Race Baby!
* `withTimeout( timeout, timeUnit )` : Apply a timeout to `all()` or `allApply()` operations. The `timeUnit` can be days, hours, microseconds, milliseconds, minutes, nanoseconds, and seconds. The default is milliseconds.

## Using Input

We usually won't have the luxury of simple queries; we will need user input to construct our queries. Here is where you need to be extra careful not to allow for [SQL injection.](https://owasp.org/www-community/attacks/SQL_Injection) BoxLang has several ways to help you prevent SQL Injection, whether using tags or script calls. Leverage the `bx:queryparam` construct/tag ([https://boxlang.ortusbooks.com/boxlang-language/reference/types/queryparam](https://boxlang.ortusbooks.com/boxlang-language/reference/types/queryparam)) and always sanitize your input via the `encode` functions in BoxLang.

```java
// Named variable holder
// automatic parameterization via inline struct definitions
queryExecute(
 "select quantity, item from cupboard where item_id = :itemID"
 { itemID = { value=arguments.itemID, sqltype="numeric" } }
);

// Positional placeholder
queryExecute(
 "select quantity, item from cupboard where item_id = ?"
 [ { value=arguments.itemID, sqltype="varchar" } ]
);
```

### 📋 Available SQL Types

The `sqltype` parameter binds values to specific database types for security and query plan optimization:

| Type | Description | Example |
|------|-------------|---------|
| `bigint` | 64-bit integer | `-9223372036854775808` to `9223372036854775807` |
| `bit` | Boolean/bit value | `true` / `false` |
| `char` | Fixed-length string | `"ABC  "` (padded) |
| `varchar` | Variable-length string | `"Hello World"` |
| `nchar` | Fixed-length Unicode string | `"ABC  "` |
| `nvarchar` | Variable-length Unicode string | `"Hello 世界"` |
| `longvarchar` | Long text | Long text content |
| `longnvarchar` | Long Unicode text | Long Unicode content |
| `integer` | 32-bit integer | `-2147483648` to `2147483647` |
| `smallint` | 16-bit integer | `-32768` to `32767` |
| `tinyint` | 8-bit integer | `-128` to `127` |
| `numeric` | Fixed precision decimal | `123.45` |
| `decimal` | Fixed precision decimal | `123.45` |
| `float` | Floating point | `123.456789` |
| `double` | Double precision float | `123.456789012345` |
| `real` | Single precision float | `123.456` |
| `money` | Currency value | `1234.56` |
| `money4` | Small currency value | `214748.3647` |
| `date` | Date only | `2025-12-09` |
| `time` | Time only | `14:30:00` |
| `timestamp` | Date and time | `2025-12-09 14:30:00` |
| `blob` | Binary large object | Binary data |
| `clob` | Character large object | Large text |
| `nclob` | Unicode large object | Large Unicode text |
| `sqlxml` | XML data | `<root><item /></root>` |
| `refcursor` | Result set reference | Oracle REF CURSOR |
| `idstamp` | Unique identifier | UUID/GUID |

{% hint style="warning" %}
The `cf_sql_{type}` syntax (e.g., `cf_sql_varchar`) is only supported when [bx-compat-cfml](https://forgebox.io/view/bx-compat-cfml) is installed. Use the native type names (e.g., `varchar`) in all new code.
{% endhint %}

## 🏗️ Building Queries Programmatically

You can create and manipulate queries without database connections using BoxLang's query construction functions:

### Creating Empty Queries

```js
// Create query with columns only
news = queryNew( "id,title", "integer,varchar" );

// Add rows one at a time
queryAddRow( news );
querySetCell( news, "id", 1 );
querySetCell( news, "title", "Dewey defeats Truman" );

queryAddRow( news );
querySetCell( news, "id", 2 );
querySetCell( news, "title", "Man walks on Moon" );

writeDump( news );
```

### Creating Queries with Data

```js
// Array of structs approach (recommended)
news = queryNew(
    "id,title",
    "integer,varchar",
    [
        { id: 1, title: "Dewey defeats Truman" },
        { id: 2, title: "Man walks on Moon" },
        { id: 3, title: "Apollo 11 Moon Landing" }
    ]
);

// Single struct approach
singleNews = queryNew(
    "id,title",
    "integer,varchar",
    { id: 1, title: "Dewey defeats Truman" }
);

// Array of arrays approach (positional)
newsArray = queryNew(
    "id,title",
    "integer,varchar",
    [
        [ 1, "Dewey defeats Truman" ],
        [ 2, "Man walks on Moon" ]
    ]
);
```

### Manipulating Query Data

```js
// Add multiple empty rows
queryAddRow( news, 5 ); // Adds 5 empty rows

// Add row from struct
queryAddRow( news, { id: 4, title: "New Event" } );

// Add column with data
queryAddColumn( news, "author", "varchar", [ "John", "Jane", "Bob", "Alice" ] );

// Delete rows and columns
queryDeleteRow( news, 2 ); // Delete row 2
queryDeleteColumn( news, "author" ); // Delete column

// Swap rows
queryRowSwap( news, 1, 3 ); // Swap positions

// Get and set specific cells
title = queryGetCell( news, "title", 1 );
querySetCell( news, "title", "Updated Title", 1 );

// Get row as struct
row = queryGetRow( news, 1 );
writeDump( row ); // { id: 1, title: "Updated Title" }

// Get column as array
titles = queryColumnData( news, "title" );
writeDump( titles ); // [ "Updated Title", "Man walks on Moon", ... ]
```

### Method Chaining

```js
// Build query fluently
users = queryNew( "id,name,age", "integer,varchar,integer" )
    .addRow( { id: 1, name: "Alice", age: 30 } )
    .addRow( { id: 2, name: "Bob", age: 25 } )
    .addRow( { id: 3, name: "Charlie", age: 35 } )
    .filter( ( row ) -> row.age >= 30 )
    .sort( "name ASC" );
```

## 🔍 Query of Queries (QoQ)

Query existing query objects using SQL without hitting the database. BoxLang's QoQ implementation is extremely fast - **5x faster than Lucee** and **17x faster than Adobe ColdFusion**.

```js
// Create a query
users = queryNew(
    "id,firstname,lastname,age",
    "integer,varchar,varchar,integer",
    [
        { id: 1, firstname: "Han", lastname: "Solo", age: 35 },
        { id: 2, firstname: "Luke", lastname: "Skywalker", age: 28 },
        { id: 3, firstname: "Leia", lastname: "Organa", age: 28 }
    ]
);

// Query the query
youngUsers = queryExecute(
    "SELECT * FROM users WHERE age < :maxAge ORDER BY firstname",
    { maxAge: { value: 30, sqltype: "integer" } },
    { dbtype: "query" }
);

writeDump( youngUsers );
```

### Advanced QoQ Features

BoxLang QoQ supports modern SQL features:

```js
// ANSI JOINs
orders = queryNew( "orderID,userID,total", "integer,integer,decimal", [ ... ] );
users = queryNew( "userID,name", "integer,varchar", [ ... ] );

result = queryExecute( "
    SELECT u.name, o.total
    FROM users u
    INNER JOIN orders o ON u.userID = o.userID
    WHERE o.total > 100
", {}, { dbtype: "query" } );

// Subqueries
highValueCustomers = queryExecute( "
    SELECT * FROM users
    WHERE userID IN (
        SELECT userID FROM orders WHERE total > 1000
    )
", {}, { dbtype: "query" } );

// Aggregates with GROUP BY
summary = queryExecute( "
    SELECT age, COUNT(*) as count, AVG(age) as avgAge
    FROM users
    GROUP BY age
    HAVING count > 1
", {}, { dbtype: "query" } );

// CASE statements
categorized = queryExecute( "
    SELECT name, age,
        CASE
            WHEN age < 18 THEN 'Minor'
            WHEN age < 65 THEN 'Adult'
            ELSE 'Senior'
        END as category
    FROM users
", {}, { dbtype: "query" } );
```

{% hint style="info" %}
For complete QoQ documentation including custom functions, bitwise operators, and performance tips, see [Query of Queries](../boxlang-framework/jdbc/query-of-queries.md).
{% endhint %}

{% hint style="success" %}
**Performance Tip**: For simple filtering and sorting, use functional methods like `queryFilter()` and `querySort()` instead of QoQ - they're even faster and more type-safe!
{% endhint %}

## 📦 Alternative Return Types

You can return query results as arrays or structs instead of query objects - perfect for JSON APIs and modern frameworks.

### Return as Array of Structs

```js
// Each row becomes a struct in an array
users = queryExecute(
    "SELECT id, name, email FROM users",
    {},
    { returntype: "array" }
);

// Result: [
//     { id: 1, name: "Alice", email: "alice@example.com" },
//     { id: 2, name: "Bob", email: "bob@example.com" }
// ]

// Perfect for JSON APIs
return users.toJSON();
```

### Return as Struct of Structs

```js
// Use a column as the key for a struct of structs
usersById = queryExecute(
    "SELECT id, name, email FROM users",
    {},
    { returntype: "struct", columnkey: "id" }
);

// Result: {
//     "1": { id: 1, name: "Alice", email: "alice@example.com" },
//     "2": { id: 2, name: "Bob", email: "bob@example.com" }
// }

// Fast lookups by ID
alice = usersById[ 1 ];
```

### Convert Existing Query

```js
// Convert query object to array
qry = queryExecute( "SELECT * FROM users" );
arrayData = qry.toArrayOfStructs();

// Manual conversion with map
arrayData = qry.map( ( row ) -> {
    return { id: row.id, name: row.name };
} );
```

{% hint style="success" %}
**Best Practice**: Use `returntype="array"` for REST APIs and JSON responses. It's cleaner and more compatible with JavaScript frameworks like React, Vue, and Angular.
{% endhint %}

## 🏗️ QB - Query Builder Module

**QB** (Query Builder) is a powerful module for building database queries with a fluent, chainable API. It abstracts database differences and makes complex queries readable and maintainable.

### Installation

```bash
box install qb
```

### Features

* ✅ Fluent, chainable query building
* ✅ Database-agnostic (MySQL, PostgreSQL, MSSQL, Oracle, etc.)
* ✅ Complex joins, subqueries, and CTEs
* ✅ Query caching and pagination
* ✅ Raw expressions when needed
* ✅ Schema builder for migrations

### Basic Usage

```js
// Inject QB instance
property name="query" inject="Builder@qb";

// Build and execute queries
posts = query.from( "posts" )
    .whereNotNull( "published_at" )
    .whereIn( "author_id", [ 5, 10, 27 ] )
    .orderBy( "published_at", "DESC" )
    .limit( 10 )
    .get();

// Complex queries with joins
users = query.from( "users as u" )
    .join( "orders as o", "u.id", "=", "o.user_id" )
    .select( [ "u.name", "COUNT(o.id) as order_count" ] )
    .groupBy( "u.id" )
    .having( "order_count", ">", 5 )
    .get();

// Subqueries
topAuthors = query.from( "posts" )
    .whereIn( "author_id", function( q ) {
        q.select( "id" )
            .from( "users" )
            .where( "reputation", ">", 1000 );
    } )
    .get();
```

### Insert, Update, Delete

```js
// Insert
query.table( "users" )
    .insert( { name: "Alice", email: "alice@example.com" } );

// Update
query.table( "users" )
    .where( "id", 1 )
    .update( { email: "newemail@example.com" } );

// Delete
query.table( "users" )
    .where( "status", "inactive" )
    .delete();
```

📖 **Full Documentation**: [https://qb.ortusbooks.com/](https://qb.ortusbooks.com/)

{% hint style="success" %}
**Recommended**: Use QB for complex queries and database migrations. It provides better testability and database portability than raw SQL.
{% endhint %}

## ⚙️ Query Options

BoxLang supports comprehensive query options for controlling execution behavior:

### Core Options

| Option | Type | Description | Example |
|--------|------|-------------|---------|
| `result` | String | Variable name to store query metadata | `result: "queryResult"` |
| `maxRows` | Integer | Limit number of rows returned | `maxRows: 100` |
| `queryTimeout` | Integer | Max execution time (seconds) | `queryTimeout: 30` |
| `returnType` | String | Return format: `query`, `array`, `struct` | `returnType: "array"` |
| `columnKey` | String | Key column for struct return type | `columnKey: "id"` |
| `fetchSize` | Integer | JDBC batch size for large results | `fetchSize: 500` |
| `dbtype` | String | Database type (`"query"` for QoQ) | `dbtype: "query"` |

### Caching Options

| Option | Type | Description | Example |
|--------|------|-------------|---------|
| `cache` | Boolean | Enable query caching | `cache: true` |
| `cacheKey` | String | Unique cache identifier | `cacheKey: "userList"` |
| `cacheProvider` | String | Cache provider name | `cacheProvider: "default"` |
| `cacheTimeout` | Duration | Cache expiration time | `cacheTimeout: "1h"` |

### Example Usage

```js
// Basic query with options
users = queryExecute(
    "SELECT * FROM users WHERE status = :status",
    { status: { value: "active", sqltype: "varchar" } },
    {
        maxRows: 50,
        queryTimeout: 10,
        returnType: "array",
        cache: true,
        cacheKey: "activeUsers",
        cacheTimeout: "30m"
    }
);

// Store metadata in result variable
queryExecute(
    "SELECT * FROM large_table",
    {},
    {
        result: "metadata",
        fetchSize: 1000,
        maxRows: 10000
    }
);

// Access metadata
writeDump( metadata.sql );
writeDump( metadata.executionTime );
writeDump( metadata.cached );
```

### CFML Compatibility Options

When [bx-compat-cfml](https://forgebox.io/view/bx-compat-cfml) is installed, these aliases are available:

| CFML Option | BoxLang Equivalent |
|-------------|-------------------|
| `blockfactor` | `fetchSize` |
| `cacheID` | `cacheKey` |
| `cacheRegion` | `cacheProvider` |
| `cachedAfter` | Converted to `cacheTimeout` |
| `cachedWithin` | `cacheTimeout` |

{% hint style="info" %}
**Future Options**: Support planned for `cachedWithin="request"`, `timezone`, `psq`, and `lazy` loading.
{% endhint %}

{% hint style="warning" %}
**Unsupported**: The following CFML options are not supported: `username`, `password`, `debug`, `clientInfo`, `fetchClientInfo`, `ormoptions`.
{% endhint %}
