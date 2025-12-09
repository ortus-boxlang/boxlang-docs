---
description: Execute SQL queries against in-memory query result sets for powerful data manipulation
icon: database
---

# 🔄 Query of Queries (QoQ)

Query of Queries (QoQ) allows you to execute SQL queries against in-memory query result sets, eliminating the need for additional database round trips. BoxLang's QoQ implementation is built from scratch using a high-performance ANTLR grammar based on SQLite, delivering exceptional speed and a comprehensive feature set that surpasses traditional CFML implementations.

## 📋 Overview

BoxLang's Query of Queries provides:

- **Fast Performance**, optimized for large datasets
- **ANSI JOIN syntax** - INNER, LEFT, RIGHT, FULL, and CROSS joins
- **Unlimited table joins** - No restrictions on number of tables
- **Subqueries** - Nested SELECT statements in FROM, JOIN, and IN clauses
- **CASE statements** - Standard and input-based CASE expressions
- **Custom functions** - Register your own scalar and aggregate functions
- **Complete SQL syntax** - TOP/LIMIT, UNION, DISTINCT, GROUP BY, ORDER BY
- **Bitwise operators** - XOR, AND, OR, NOT operations
- **Type safety** - Preserves column types and NULL handling

## 🚀 Basic Usage

To execute a query of queries, set the `dbtype` option to `"query"`:

```js
// Create source data
employees = queryNew(
    "name,department,salary,hireDate",
    "varchar,varchar,integer,date",
    [
        [ "John Doe", "Engineering", 75000, createDate( 2020, 1, 15 ) ],
        [ "Jane Smith", "Marketing", 68000, createDate( 2019, 3, 22 ) ],
        [ "Bob Johnson", "Engineering", 82000, createDate( 2018, 7, 10 ) ],
        [ "Alice Williams", "Sales", 71000, createDate( 2021, 5, 5 ) ]
    ]
);

// Query the query
result = queryExecute(
    "SELECT name, salary FROM employees WHERE department = ?",
    [ "Engineering" ],
    { dbtype: "query" }
);

// Result contains 2 rows: John Doe and Bob Johnson
writeOutput( "Found #result.recordCount# engineers" );
```

## 🔗 ANSI JOIN Syntax

BoxLang supports modern ANSI JOIN syntax with unlimited table joins and full alias support.

### INNER JOIN

Returns only matching rows from both tables:

```js
users = queryNew(
    "userID,name,departmentID",
    "integer,varchar,integer",
    [
        [ 1, "John Doe", 10 ],
        [ 2, "Jane Smith", 20 ],
        [ 3, "Bob Johnson", 10 ]
    ]
);

departments = queryNew(
    "departmentID,name",
    "integer,varchar",
    [
        [ 10, "Engineering" ],
        [ 20, "Marketing" ]
    ]
);

result = queryExecute(
    "SELECT u.name, d.name as departmentName
     FROM users u
     INNER JOIN departments d ON u.departmentID = d.departmentID",
    [],
    { dbtype: "query" }
);

// Returns: John Doe (Engineering), Jane Smith (Marketing), Bob Johnson (Engineering)
```

### LEFT (OUTER) JOIN

Returns all rows from the left table, with NULLs for non-matching right table rows:

```js
result = queryExecute(
    "SELECT u.name, d.name as departmentName
     FROM users u
     LEFT JOIN departments d ON u.departmentID = d.departmentID",
    [],
    { dbtype: "query" }
);

// Includes users even if department doesn't exist
```

### RIGHT (OUTER) JOIN

Returns all rows from the right table, with NULLs for non-matching left table rows:

```js
result = queryExecute(
    "SELECT u.name, d.name as departmentName
     FROM users u
     RIGHT JOIN departments d ON u.departmentID = d.departmentID",
    [],
    { dbtype: "query" }
);

// Includes departments even if no users exist
```

### FULL (OUTER) JOIN

Returns all rows from both tables, with NULLs where matches don't exist:

```js
result = queryExecute(
    "SELECT u.name, d.name as departmentName
     FROM users u
     FULL OUTER JOIN departments d ON u.departmentID = d.departmentID",
    [],
    { dbtype: "query" }
);

// Includes all users and all departments
```

### CROSS JOIN

Returns the Cartesian product of both tables (every combination):

```js
colors = queryNew( "color", "varchar", [ [ "Red" ], [ "Blue" ] ] );
sizes = queryNew( "size", "varchar", [ [ "Small" ], [ "Large" ] ] );

result = queryExecute(
    "SELECT c.color, s.size
     FROM colors c
     CROSS JOIN sizes s",
    [],
    { dbtype: "query" }
);

// Returns: Red/Small, Red/Large, Blue/Small, Blue/Large
```

### Multiple Table Joins

Join as many tables as needed:

```js
result = queryExecute(
    "SELECT e.name, d.name as dept, m.name as manager, p.title as project
     FROM employees e
     INNER JOIN departments d ON e.departmentID = d.id
     LEFT JOIN employees m ON e.managerID = m.id
     LEFT JOIN projects p ON e.projectID = p.id
     WHERE e.active = true
     ORDER BY d.name, e.name",
    [],
    { dbtype: "query" }
);
```

## 🧩 Subqueries

BoxLang supports non-correlated subqueries in multiple contexts.

### FROM/JOIN Subqueries

Use a subquery as a table source:

```js
// Find employees earning more than the average in their department
result = queryExecute(
    "SELECT e.name, e.salary, e.department
     FROM employees e
     INNER JOIN (
         SELECT department, AVG( salary ) as avgSalary
         FROM employees
         GROUP BY department
     ) d ON e.department = d.department
     WHERE e.salary > d.avgSalary",
    [],
    { dbtype: "query" }
);
```

### IN/NOT IN Subqueries

Filter using a subquery result set:

```js
// Find users in executive departments
result = queryExecute(
    "SELECT name, department
     FROM users
     WHERE departmentID IN (
         SELECT departmentID
         FROM departments
         WHERE type = 'Executive'
     )",
    [],
    { dbtype: "query" }
);

// Find products not in any order
outOfStock = queryExecute(
    "SELECT productName
     FROM products
     WHERE productID NOT IN (
         SELECT DISTINCT productID
         FROM orderItems
     )",
    [],
    { dbtype: "query" }
);
```

## 🎯 CASE Statements

CASE expressions provide conditional logic within SQL queries.

### Standard CASE

Each WHEN contains a boolean expression:

```js
result = queryExecute(
    "SELECT name,
            salary,
            CASE
                WHEN salary < 50000 THEN 'Junior'
                WHEN salary < 80000 THEN 'Mid-Level'
                WHEN salary < 120000 THEN 'Senior'
                ELSE 'Executive'
            END as level
     FROM employees",
    [],
    { dbtype: "query" }
);
```

### Input CASE

Compare against a single input expression:

```js
result = queryExecute(
    "SELECT name,
            department,
            CASE department
                WHEN 'Engineering' THEN 'Tech'
                WHEN 'Marketing' THEN 'Business'
                WHEN 'Sales' THEN 'Business'
                ELSE 'Other'
            END as division
     FROM employees",
    [],
    { dbtype: "query" }
);
```

### CASE in ORDER BY

```js
// Custom sort order
result = queryExecute(
    "SELECT name, status
     FROM tasks
     ORDER BY CASE status
         WHEN 'Critical' THEN 1
         WHEN 'High' THEN 2
         WHEN 'Normal' THEN 3
         ELSE 4
     END",
    [],
    { dbtype: "query" }
);
```

## 📊 Aggregate Functions

BoxLang supports all standard aggregate functions plus powerful additions.

### Standard Aggregates

```js
result = queryExecute(
    "SELECT department,
            COUNT(*) as employeeCount,
            AVG( salary ) as avgSalary,
            MIN( salary ) as minSalary,
            MAX( salary ) as maxSalary,
            SUM( salary ) as totalSalary
     FROM employees
     GROUP BY department",
    [],
    { dbtype: "query" }
);
```

### String Aggregation

Concatenate values with delimiters:

```js
// Using STRING_AGG (standard SQL)
result = queryExecute(
    "SELECT department,
            STRING_AGG( name, ', ' ) as employeeList
     FROM employees
     GROUP BY department",
    [],
    { dbtype: "query" }
);

// Using GROUP_CONCAT (MySQL-style)
result = queryExecute(
    "SELECT department,
            GROUP_CONCAT( name, '; ' ) as employeeList
     FROM employees
     GROUP BY department",
    [],
    { dbtype: "query" }
);
```

## 🔧 Built-In Functions

BoxLang provides a comprehensive set of SQL functions.

### Math Functions

```js
result = queryExecute(
    "SELECT productName,
            price,
            ABS( discount ) as absDiscount,
            CEILING( price * 1.15 ) as priceWithTax,
            FLOOR( price * 0.9 ) as salePrice,
            SQRT( quantity ) as sqrtQty
     FROM products",
    [],
    { dbtype: "query" }
);
```

**Available:** `abs()`, `acos()`, `asin()`, `atan()`, `cos()`, `sin()`, `tan()`, `exp()`, `sqrt()`, `ceiling()`, `floor()`

### String Functions

```js
result = queryExecute(
    "SELECT UPPER( firstName ) as firstName,
            LOWER( email ) as email,
            CONCAT( firstName, ' ', lastName ) as fullName,
            LEFT( phone, 3 ) as areaCode,
            RIGHT( ssn, 4 ) as last4SSN,
            LENGTH( bio ) as bioLength,
            LTRIM( RTRIM( description ) ) as cleanDesc
     FROM users",
    [],
    { dbtype: "query" }
);
```

**Available:** `upper()`, `lower()`, `ucase()`, `lcase()`, `concat()`, `left()`, `right()`, `length()`, `ltrim()`, `rtrim()`

### NULL Handling

```js
result = queryExecute(
    "SELECT name,
            COALESCE( middleName, '(none)' ) as middle,
            ISNULL( suffix, 'N/A' ) as suffix
     FROM people",
    [],
    { dbtype: "query" }
);
```

**Available:** `coalesce()`, `isNull()`

### Type Conversion

```js
result = queryExecute(
    "SELECT CAST( price AS INTEGER ) as priceInt,
            CAST( quantity AS VARCHAR ) as quantityStr,
            CONVERT( total, 'DECIMAL' ) as totalDecimal
     FROM orders",
    [],
    { dbtype: "query" }
);
```

**Available:** `cast()`, `convert()`

## 🛠️ Custom Function Registration

Register your own functions for use in QoQ queries.

### Scalar Functions

Process a single value and return a single result:

```js
// Register a BIF using functional wrapper syntax
queryRegisterFunction( "reverse", ::reverse );

result = queryExecute(
    "SELECT name, REVERSE( name ) as reversedName
     FROM employees",
    [],
    { dbtype: "query" }
);

// Register a custom closure
queryRegisterFunction( "maskEmail", ( email ) => {
    parts = email.split( "@" );
    return parts[ 1 ] ? "***@#parts[ 2 ]#" : email;
} );

result = queryExecute(
    "SELECT name, maskEmail( email ) as maskedEmail
     FROM users",
    [],
    { dbtype: "query" }
);
```

### Aggregate Functions

Process multiple values and return a single result:

```js
// Register an aggregate function
queryRegisterFunction(
    "arrayToList",
    ::arrayToList,
    "varchar",
    "aggregate"
);

result = queryExecute(
    "SELECT department,
            arrayToList( name ) as employeeList
     FROM employees
     GROUP BY department",
    [],
    { dbtype: "query" }
);

// Custom aggregate with closure
queryRegisterFunction(
    "countDistinct",
    ( arr ) => arr.reduce( ( acc, val ) => {
        acc[ val ] = true;
        return acc;
    }, {} ).count(),
    "integer",
    "aggregate"
);

result = queryExecute(
    "SELECT department,
            countDistinct( title ) as uniqueTitles
     FROM employees
     GROUP BY department",
    [],
    { dbtype: "query" }
);
```

## 📐 Operators

BoxLang QoQ supports all standard SQL operators plus bitwise operations.

### Comparison Operators

```js
result = queryExecute(
    "SELECT * FROM employees
     WHERE salary >= 50000
       AND department = 'Engineering'
       AND hireDate < '2020-01-01'",
    [],
    { dbtype: "query" }
);
```

**Available:** `=`, `!=`, `<>`, `<`, `>`, `<=`, `>=`, `IS`, `IS NOT`, `LIKE`, `NOT LIKE`, `IN`, `NOT IN`, `BETWEEN`, `NOT BETWEEN`

### Mathematical Operators

```js
result = queryExecute(
    "SELECT name,
            salary,
            salary * 1.05 as raisedSalary,
            salary / 12 as monthlySalary,
            salary + bonus as totalComp,
            salary - deductions as netPay,
            salary % 1000 as remainder
     FROM employees",
    [],
    { dbtype: "query" }
);
```

**Available:** `+`, `-`, `*`, `/`, `%` (modulo)

### Bitwise Operators

```js
flags = queryNew(
    "name,permissions",
    "varchar,integer",
    [
        [ "Admin", 7 ],    // 0111
        [ "User", 3 ],     // 0011
        [ "Guest", 1 ]     // 0001
    ]
);

result = queryExecute(
    "SELECT name,
            permissions & 4 as canDelete,
            permissions & 2 as canWrite,
            permissions & 1 as canRead,
            permissions | 8 as withExtraFlag,
            permissions ^ 15 as inverted
     FROM flags",
    [],
    { dbtype: "query" }
);
```

**Available:** `&` (AND), `|` (OR), `^` (XOR), `!` (NOT)

### String Concatenation

```js
result = queryExecute(
    "SELECT firstName || ' ' || lastName as fullName
     FROM users",
    [],
    { dbtype: "query" }
);
```

**Available:** `||` (concatenation)

## 🎚️ Query Clauses

### DISTINCT

Remove duplicate rows:

```js
result = queryExecute(
    "SELECT DISTINCT department FROM employees",
    [],
    { dbtype: "query" }
);
```

### WHERE

Filter rows:

```js
result = queryExecute(
    "SELECT * FROM employees
     WHERE salary > 50000
       AND department IN ( 'Engineering', 'Sales' )
       AND hireDate BETWEEN '2020-01-01' AND '2023-12-31'",
    [],
    { dbtype: "query" }
);
```

### GROUP BY

Aggregate data:

```js
result = queryExecute(
    "SELECT department, COUNT(*) as count, AVG( salary ) as avgSalary
     FROM employees
     GROUP BY department
     HAVING COUNT(*) > 5",
    [],
    { dbtype: "query" }
);
```

### ORDER BY

Sort results:

```js
result = queryExecute(
    "SELECT name, salary, department
     FROM employees
     ORDER BY department ASC, salary DESC, name",
    [],
    { dbtype: "query" }
);
```

### TOP and LIMIT

Limit result count:

```js
// Using TOP (SQL Server style)
result = queryExecute(
    "SELECT TOP 10 name, salary
     FROM employees
     ORDER BY salary DESC",
    [],
    { dbtype: "query" }
);

// Using LIMIT (MySQL/PostgreSQL style)
result = queryExecute(
    "SELECT name, salary
     FROM employees
     ORDER BY salary DESC
     LIMIT 10",
    [],
    { dbtype: "query" }
);
```

### UNION

Combine multiple queries:

```js
// UNION (removes duplicates)
result = queryExecute(
    "SELECT name, 'Employee' as type FROM employees
     UNION
     SELECT name, 'Contractor' as type FROM contractors",
    [],
    { dbtype: "query" }
);

// UNION ALL (keeps duplicates)
result = queryExecute(
    "SELECT product FROM sales2023
     UNION ALL
     SELECT product FROM sales2024",
    [],
    { dbtype: "query" }
);

// UNION DISTINCT (explicit duplicate removal)
result = queryExecute(
    "SELECT email FROM customers
     UNION DISTINCT
     SELECT email FROM leads",
    [],
    { dbtype: "query" }
);
```

## 🎯 Advanced Examples

### Data Transformation Pipeline

```js
// Multi-step data processing
salesData = queryExecute(
    "SELECT * FROM rawSales WHERE year = 2024",
    [],
    { datasource: "myDB" }
);

// Calculate metrics
metrics = queryExecute(
    "SELECT region,
            product,
            SUM( amount ) as totalSales,
            AVG( amount ) as avgSale,
            COUNT(*) as transactionCount
     FROM salesData
     GROUP BY region, product",
    [],
    { dbtype: "query" }
);

// Identify top performers
topPerformers = queryExecute(
    "SELECT region, product, totalSales
     FROM metrics
     WHERE totalSales > (
         SELECT AVG( totalSales )
         FROM metrics
     )
     ORDER BY totalSales DESC
     LIMIT 10",
    [],
    { dbtype: "query" }
);
```

### Complex Filtering

```js
// Find employees with specific criteria
result = queryExecute(
    "SELECT e.name,
            e.department,
            e.salary,
            CASE
                WHEN e.salary > d.avgSalary * 1.5 THEN 'Above Average'
                WHEN e.salary > d.avgSalary THEN 'Average'
                ELSE 'Below Average'
            END as performance
     FROM employees e
     INNER JOIN (
         SELECT department, AVG( salary ) as avgSalary
         FROM employees
         GROUP BY department
     ) d ON e.department = d.department
     WHERE e.isActive = true
       AND e.hireDate < '2020-01-01'
       AND e.salary NOT IN (
           SELECT salary
           FROM employees
           WHERE department = 'Executive'
       )",
    [],
    { dbtype: "query" }
);
```

### Pivot-like Operations

```js
// Transform rows to columns
sales = queryNew(
    "month,region,amount",
    "varchar,varchar,integer",
    [
        [ "Jan", "North", 1000 ],
        [ "Jan", "South", 1500 ],
        [ "Feb", "North", 1200 ],
        [ "Feb", "South", 1800 ]
    ]
);

pivot = queryExecute(
    "SELECT month,
            SUM( CASE WHEN region = 'North' THEN amount ELSE 0 END ) as North,
            SUM( CASE WHEN region = 'South' THEN amount ELSE 0 END ) as South,
            SUM( amount ) as Total
     FROM sales
     GROUP BY month
     ORDER BY month",
    [],
    { dbtype: "query" }
);
```

### Data Deduplication

```js
// Find and remove duplicates
duplicates = queryExecute(
    "SELECT email, COUNT(*) as count
     FROM users
     GROUP BY email
     HAVING COUNT(*) > 1",
    [],
    { dbtype: "query" }
);

// Keep only first occurrence
unique = queryExecute(
    "SELECT DISTINCT email, name, signupDate
     FROM users u1
     WHERE signupDate = (
         SELECT MIN( signupDate )
         FROM users u2
         WHERE u1.email = u2.email
     )",
    [],
    { dbtype: "query" }
);
```

## 💡 Best Practices

### Performance
- ✅ **Use JOINs over subqueries** when possible for better performance
- ✅ **Filter early** - Apply WHERE clauses to reduce row count before JOINs
- ✅ **Limit columns** - SELECT only needed columns, not SELECT *
- ✅ **Use indexes** - Original database query results maintain index information
- ✅ **Minimize DISTINCT** - Use only when necessary as it requires deduplication

### Memory Management
- ✅ **Limit result sets** - Use TOP/LIMIT to prevent memory issues
- ✅ **Process in batches** - For large datasets, break into smaller QoQ operations
- ✅ **Clean up queries** - Remove references to large query objects when done
- ✅ **Monitor query size** - Be aware of result set row counts and column widths

### Code Quality
- ✅ **Use parameterized queries** - Prevent SQL injection even in QoQ
- ✅ **Alias tables** - Always use table aliases for clarity and readability
- ✅ **Format SQL** - Use proper indentation and line breaks
- ✅ **Document complex logic** - Comment non-obvious CASE statements and subqueries
- ✅ **Test edge cases** - Verify NULL handling, empty results, and data type conversions

### Data Integrity
- ✅ **Preserve types** - QoQ maintains original column data types
- ✅ **Handle NULLs** - Use COALESCE or ISNULL for NULL-safe operations
- ✅ **Validate joins** - Ensure JOIN conditions match appropriate data types
- ✅ **Check for duplicates** - Use DISTINCT when necessary

## 🚫 Common Pitfalls

❌ **Forgetting dbtype option**
```js
// BAD - executes against database instead of query
result = queryExecute( "SELECT * FROM employees" );

// GOOD - executes against query object
result = queryExecute(
    "SELECT * FROM employees",
    [],
    { dbtype: "query" }
);
```

❌ **Ambiguous column references with multiple tables**
```js
// BAD - name exists in both tables
result = queryExecute(
    "SELECT name FROM employees e
     INNER JOIN departments d ON e.deptID = d.id",
    [],
    { dbtype: "query" }
);

// GOOD - specify table alias
result = queryExecute(
    "SELECT e.name, d.name as deptName FROM employees e
     INNER JOIN departments d ON e.deptID = d.id",
    [],
    { dbtype: "query" }
);
```

❌ **Not handling NULL values**
```js
// BAD - math operations with NULL return NULL
result = queryExecute(
    "SELECT salary * bonus as total FROM employees",
    [],
    { dbtype: "query" }
);

// GOOD - use COALESCE to handle NULLs
result = queryExecute(
    "SELECT salary * COALESCE( bonus, 0 ) as total FROM employees",
    [],
    { dbtype: "query" }
);
```

❌ **Using correlated subqueries**
```js
// BAD - BoxLang doesn't support correlated subqueries
result = queryExecute(
    "SELECT name FROM employees e1
     WHERE salary > (
         SELECT AVG( salary )
         FROM employees e2
         WHERE e2.department = e1.department
     )",
    [],
    { dbtype: "query" }
);

// GOOD - use JOIN with aggregate subquery
result = queryExecute(
    "SELECT e.name FROM employees e
     INNER JOIN (
         SELECT department, AVG( salary ) as avgSalary
         FROM employees
         GROUP BY department
     ) d ON e.department = d.department
     WHERE e.salary > d.avgSalary",
    [],
    { dbtype: "query" }
);
```

## 🔍 Limitations

Query of Queries has some limitations to be aware of:

- **No correlated subqueries** - Subqueries cannot reference outer query tables
- **No window functions** - OVER(), PARTITION BY not supported
- **No CTEs** - Common Table Expressions (WITH clause) not available
- **Read-only** - Cannot INSERT, UPDATE, or DELETE rows
- **No transactions** - All operations are immediate
- **In-memory only** - Large result sets may impact memory usage

## 🔗 Related Documentation

- [Querying](querying.md) - Execute database queries
- [Datasources](datasources.md) - Configure database connections
- [Query Type Reference](../../boxlang-language/reference/types/query.md) - Query object methods and properties
- [queryExecute() BIF](../../boxlang-language/reference/built-in-functions/jdbc/QueryExecute.md) - Complete BIF reference

## 📚 Additional Resources

- [BoxLang QoQ Performance Blog Post](https://www.codersrevolution.com/blog/boxlangs-qoq-is-here-and-its-5x-faster-than-lucee-17x-faster-than-adobe)
- [BoxLang QoQ Features Blog Post](https://www.codersrevolution.com/blog/boxlang-query-of-query-improvements-and-additions)
- [SQLite SQL Syntax](https://www.sqlite.org/lang.html) - BoxLang QoQ grammar is based on SQLite
