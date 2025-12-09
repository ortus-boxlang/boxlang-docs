---
description: Comprehensive guide to database connectivity and operations in BoxLang
icon: database
---

# 🗄️ JDBC Framework

BoxLang provides a comprehensive, enterprise-grade JDBC framework for interacting with relational databases. Built on industry-standard JDBC technology with HikariCP connection pooling, BoxLang makes database operations simple, secure, and performant.

## 🎯 What You Can Do

The BoxLang JDBC framework enables you to:

- **Connect to Databases** - Define and manage datasources for multiple database vendors
- **Execute Queries** - Run SQL queries with parameterized statements for security
- **Manage Transactions** - Ensure data integrity with ACID-compliant transaction support
- **Call Stored Procedures** - Execute database procedures with IN/OUT/INOUT parameters
- **Introspect Databases** - Retrieve metadata about tables, columns, indexes, and more
- **Query of Queries** - Execute SQL against in-memory result sets without database round-trips

## 📚 Framework Components

### [Datasources](datasources.md)

Learn how to define and configure database connections at runtime, application, or query level. Covers connection pooling, environment variables, and portable configurations.

**Key Topics:**
- Supported database vendors (MySQL, PostgreSQL, Oracle, SQL Server, Derby, HyperSQL, MariaDB)
- Configuration options and HikariCP pooling
- Default datasources and inline definitions
- CFConfig integration for portable configs

### [Querying](querying.md)

Master SQL query execution using both `queryExecute()` BIF and `bx:query` component. Learn about parameterized queries, result formatting, caching, and Query of Queries.

**Key Topics:**
- Query execution patterns (BIF vs component)
- Parameterized queries with query params
- Return type options (query, array, struct)
- Query caching strategies
- Query of Queries (QoQ) for in-memory operations

### [Transactions](transactions.md)

Understand database transaction management for ensuring data consistency and integrity across multiple database operations.

**Key Topics:**
- Transaction basics (ACID properties)
- Automatic and manual transaction control
- Isolation levels (read_uncommitted, read_committed, repeatable_read, serializable)
- Savepoints and nested transactions
- Best practices and performance tips

### [Stored Procedures](stored-procedures.md)

Execute database stored procedures with full support for parameters, multiple result sets, and return codes.

**Key Topics:**
- Stored procedure execution with `bx:storedProc`
- IN/OUT/INOUT parameter handling
- Multiple result set capture
- Return code retrieval
- NULL value handling

### [Database Information](db-info.md)

Use the `bx:dbInfo` component to introspect database metadata, discover schema structures, and retrieve connection information.

**Key Topics:**
- Retrieving table and column metadata
- Listing database names and tables
- Foreign key and index information
- Stored procedure discovery
- Database version information

### [Query of Queries (QoQ)](query-of-queries.md)

Execute SQL queries against in-memory query result sets for powerful data manipulation without additional database round trips. BoxLang's QoQ is 5x faster than Lucee and 17x faster than Adobe ColdFusion.

**Key Topics:**
- ANSI JOIN syntax (INNER, LEFT, RIGHT, FULL, CROSS)
- Subqueries in FROM, JOIN, and IN clauses
- CASE statements and custom functions
- Aggregate functions and grouping
- TOP/LIMIT, UNION, bitwise operators
- Performance optimization techniques

### [JDBC Drivers](../../boxlang-framework/modularity/jdbc.md)

Learn about the modular JDBC driver architecture in BoxLang, including how to add support for new database vendors via modules.

## 🔧 BIFs & Components Overview

BoxLang provides both Built-In Functions (BIFs) and Components for JDBC operations, allowing you to choose the syntax that fits your coding style.

### Built-In Functions

| Function | Purpose |
|----------|---------|
| `queryExecute()` | Execute SQL queries |
| `isInTransaction()` | Check if in a transaction |
| `transactionCommit()` | Commit current transaction |
| `transactionRollback()` | Rollback transaction |
| `transactionSetSavepoint()` | Create transaction savepoint |
| `preserveSingleQuotes()` | Preserve SQL string literals |

### Components

| Component | Purpose |
|-----------|---------|
| `bx:query` | Execute SQL queries |
| `bx:queryParam` | Define query parameters |
| `bx:transaction` | Manage transactions |
| `bx:storedProc` | Execute stored procedures |
| `bx:procParam` | Define procedure parameters |
| `bx:procResult` | Capture procedure results |
| `bx:dbInfo` | Retrieve database metadata |

{% hint style="info" %}
BIFs and components offer the same functionality. Script-based code typically uses BIFs, while template-based code uses components.
{% endhint %}

## 🚀 Quick Start

### Define a Datasource

```js
// In Application.bx
class {
    this.name = "myApp";

    this.datasources = {
        "myDB": {
            "driver": "mysql",
            "host": "localhost",
            "port": "3306",
            "database": "myDatabase",
            "username": "root",
            "password": "secret"
        }
    };

    this.datasource = "myDB"; // Set as default
}
```

### Execute a Query

```js
// Using queryExecute() BIF
employees = queryExecute(
    "SELECT * FROM employees WHERE department = ?",
    [ "Sales" ]
);

// Using bx:query component
<bx:query name="employees" datasource="myDB">
    SELECT * FROM employees
    WHERE department = <bx:queryParam value="Sales" sqltype="varchar">
</bx:query>
```

### Use Transactions

```js
transaction {
    queryExecute( "UPDATE accounts SET balance = balance - 100 WHERE id = 1" );
    queryExecute( "UPDATE accounts SET balance = balance + 100 WHERE id = 2" );
    // Both queries commit together, or rollback together on error
}
```

## 🔐 Security Best Practices

1. **Always Use Query Parameters** - Never concatenate user input into SQL strings
2. **Use Environment Variables** - Don't hardcode passwords in source code
3. **Limit Privileges** - Use database accounts with minimum required permissions
4. **Enable SSL/TLS** - Encrypt database connections in production
5. **Validate Input** - Sanitize and validate all user input before querying

## 📖 Related Documentation

- [Query Type Reference](../../boxlang-language/reference/types/query.md) - Query object methods and properties
- [JDBC Built-In Functions](../../boxlang-language/reference/built-in-functions/jdbc/) - Complete BIF reference
- [JDBC Components](../../boxlang-language/reference/components/jdbc/) - Complete component reference
- [Queries Guide](../../boxlang-language/queries.md) - General query documentation

## 💡 Need Help?

- [BoxLang Documentation](https://boxlang.ortusbooks.com) - Complete language documentation
- [Community Forum](https://community.ortussolutions.com) - Get help from the community
- [GitHub Issues](https://github.com/ortus-solutions/boxlang/issues) - Report bugs or request features
