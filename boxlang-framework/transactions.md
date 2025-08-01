---
icon: database
---

# 🔄 JDBC Transactions

Database transactions are one of the most critical features for ensuring **data integrity** and **consistency** in your applications. BoxLang provides comprehensive transaction support through both a modern `transaction{}` block syntax and the underlying `bx:transaction` component.

## 🚀 Why Transactions Matter

Transactions ensure the **ACID properties** of database operations:

- **⚛️ Atomicity**: All operations succeed together or fail together - no partial updates
- **🔒 Consistency**: Database remains in a valid state before and after the transaction
- **🏝️ Isolation**: Concurrent transactions don't interfere with each other
- **💾 Durability**: Committed changes persist even after system failures

### 💡 Real-World Examples

```js
// ❌ Without transactions - DANGEROUS!
queryExecute( "UPDATE accounts SET balance = balance - 100 WHERE id = 1" );
// 💥 What if the application crashes here?
queryExecute( "UPDATE accounts SET balance = balance + 100 WHERE id = 2" );

// ✅ With transactions - SAFE!
transaction {
    queryExecute( "UPDATE accounts SET balance = balance - 100 WHERE id = 1" );
    queryExecute( "UPDATE accounts SET balance = balance + 100 WHERE id = 2" );
    // Both updates succeed together or both are rolled back
}
```

## 📝 Transaction Syntax

BoxLang offers multiple ways to work with transactions:

### 🎯 Block Syntax (Recommended)

The modern `transaction{}` block syntax provides automatic transaction management:

```js
// Basic transaction block
transaction {
    queryExecute( "INSERT INTO orders (customer_id, total) VALUES (?, ?)", [ 123, 99.99 ] );
    queryExecute( "INSERT INTO order_items (order_id, product_id) VALUES (?, ?)", [ orderId, 456 ] );
}

// Transaction with specific datasource
transaction datasource="shopDB" {
    queryExecute( "UPDATE inventory SET quantity = quantity - 1 WHERE product_id = ?", [ 456 ] );
    queryExecute( "INSERT INTO sales_log (product_id, sold_at) VALUES (?, NOW())", [ 456 ] );
}

// Transaction with isolation level
transaction isolation="repeatable_read" {
    var currentBalance = queryExecute( "SELECT balance FROM accounts WHERE id = ?", [ accountId ] );
    queryExecute( "UPDATE accounts SET balance = ? WHERE id = ?", [ currentBalance.balance + 100, accountId ] );
}
```

### ⚙️ Manual Transaction Control

For complex scenarios, use transaction BIFs directly:

```js
if ( !isInTransaction() ) {
    transactionBegin();
}

try {
    transactionSetSavepoint( "beforeCriticalOperation" );

    // Critical database operations
    queryExecute( "UPDATE critical_data SET value = ?", [ newValue ] );

    if ( someCondition ) {
        transactionRollback( "beforeCriticalOperation" );
    } else {
        transactionCommit();
    }
} catch ( any e ) {
    transactionRollback();
    rethrow;
}
```

## 🔧 Transaction Attributes & Options

### 📋 Available Attributes

| Attribute | Values | Description |
|-----------|--------|-------------|
| `action` | `begin`, `commit`, `rollback`, `setsavepoint` | Action to perform on the transaction |
| `isolation` | `read_uncommitted`, `read_committed`, `repeatable_read`, `serializable` | Transaction isolation level |
| `savepoint` | String | Name of the savepoint to create or rollback to |
| `nested` | Boolean | Whether this is a nested transaction (default: `false`) |
| `datasource` | String | Specific datasource name for the transaction |

### 🔒 Isolation Levels Explained

Choose the right isolation level based on your concurrency and consistency needs:

```js
// 🚨 READ_UNCOMMITTED - Lowest isolation, highest performance
transaction isolation="read_uncommitted" {
    // Can read uncommitted data from other transactions
    // Risk: Dirty reads, non-repeatable reads, phantom reads
}

// 📖 READ_COMMITTED - Default for most databases
transaction isolation="read_committed" {
    // Only reads committed data
    // Risk: Non-repeatable reads, phantom reads
}

// 🔄 REPEATABLE_READ - Consistent reads within transaction
transaction isolation="repeatable_read" {
    // Same data read multiple times returns identical results
    // Risk: Phantom reads (new rows may appear)
}

// 🛡️ SERIALIZABLE - Highest isolation, lowest performance
transaction isolation="serializable" {
    // Complete isolation from other transactions
    // Risk: Potential deadlocks, reduced concurrency
}
```

## 🎯 Transaction Behavior

### Connections

In BoxLang transactions, _no connection is acquired until the first JDBC query is executed_. Consider this transaction block:

```js
transaction{
    transactionSetSavepoint( 'beginning' );
    transactionRollback( 'beginning' );
    transactionCommit();
}
```

This transaction is a no-op. It begins, tries to set a savepoint, then roll back to the savepoint, then commit... **but never ran any JDBC queries**. Hence, every transactional BIF called above does exactly nothing (besides [emit events](interceptors/core-interception-points/transaction-events.md)).

### 🗄️ Datasources

In BoxLang, transactions are inherently single-connection concepts. You can't have a transaction that spans multiple connections or datasources.

Hence, despite containing TWO queries this transaction has only a single query that executes within a transaction context:

```js
transaction{
    // As the first query within the transaction, the datasource obtained for this query will be set as the transaction datasource.
    queryExecute( "INSERT INTO vehicles ( make, model ) VALUES ( 'Ford', 'Fusion' )", {} );
    // This query will execute outside of any transactional context and cannot be rolled back.
    queryExecute( "UPDATE users SET datedModifies=GETDATE() )", {}, { datasource : "adminDB" } );
}
```

In Adobe and Lucee, the first query executed within the datasource determines the transactional datasource; that is, the first query to run sets the datasource to use for that transaction. Any queries which specify a different datasource will execute outside the context of the transaction.

To improve expectations around this behavior, BoxLang supports a `datasource` attribute on the transaction block:

```js
transaction datasource="carDB" {
    // this query will run inside the transaction because its datasource matches the transaction 'datasource' attribute
    queryExecute( "INSERT INTO vehicles ( make, model ) VALUES ( 'Ford', 'Fusion' )", { datasource : "carDB" } );
    // this query will NOT run inside the transaction because its datasource does NOT match the transaction 'datasource' attribute
    queryExecute( "UPDATE users SET datedModifies=GETDATE() )", {}, { datasource : "adminDB" } );
}
```

Setting the datasource at the transaction block makes it much more obvious which datasource the transaction will operate upon.

## 💾 Savepoints

Savepoints allow you to create checkpoints within a transaction for partial rollbacks:

```js
transaction {
    queryExecute( "INSERT INTO orders (id, customer_id) VALUES (1, 123)" );

    transactionSetSavepoint( "afterOrder" );

    try {
        queryExecute( "INSERT INTO order_items (order_id, product_id) VALUES (1, 456)" );
        queryExecute( "UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 456" );

        // If inventory goes negative, rollback just the items/inventory changes
        var inventory = queryExecute( "SELECT quantity FROM inventory WHERE product_id = 456" );
        if ( inventory.quantity < 0 ) {
            transactionRollback( "afterOrder" );
            throw "Insufficient inventory";
        }

    } catch ( any e ) {
        transactionRollback( "afterOrder" );
        rethrow;
    }

    // Order remains even if items failed
}
```

## 🚨 Exception Handling

Transactions automatically roll back when exceptions occur:

```js
transaction {
    try {
        queryExecute( "INSERT INTO users (name) VALUES (?)", [ "John" ] );

        // This will cause the entire transaction to roll back
        queryExecute( "INSERT INTO invalid_table (data) VALUES (?)", [ "test" ] );

    } catch ( database e ) {
        // Transaction is already rolled back automatically
        writeLog( "Database error: " & e.message );

        // Could start a new transaction for error logging
        transaction {
            queryExecute( "INSERT INTO error_log (error, occurred_at) VALUES (?, NOW())", [ e.message ] );
        }
    }
}
```

## 📊 Performance Considerations

### ⚡ Best Practices

```js
// ✅ Good: Keep transactions short
transaction {
    queryExecute( "UPDATE account SET balance = balance - 100 WHERE id = ?", [ fromAccount ] );
    queryExecute( "UPDATE account SET balance = balance + 100 WHERE id = ?", [ toAccount ] );
} // Transaction ends quickly

// ❌ Bad: Long-running transaction
transaction {
    queryExecute( "SELECT * FROM large_table" ); // Could take minutes

    // Process thousands of records...
    for ( record in largeDataset ) {
        queryExecute( "INSERT INTO processed_data VALUES (?)", [ record ] );
        sleep( 100 ); // Never sleep in transactions!
    }
} // Holds locks for too long

// ✅ Better: Batch processing with smaller transactions
for ( batch in batches ) {
    transaction {
        for ( record in batch ) {
            queryExecute( "INSERT INTO processed_data VALUES (?)", [ record ] );
        }
    }
}
```

### 🔄 Deadlock Prevention

```js
// ✅ Good: Consistent order prevents deadlocks
transaction {
    // Always update accounts in ID order
    var accounts = [ fromAccountId, toAccountId ].sort( "numeric" );

    queryExecute( "UPDATE accounts SET balance = balance - 100 WHERE id = ?", [ accounts[1] ] );
    queryExecute( "UPDATE accounts SET balance = balance + 100 WHERE id = ?", [ accounts[2] ] );
}

// ❌ Bad: Inconsistent order can cause deadlocks
transaction {
    queryExecute( "UPDATE accounts SET balance = balance - 100 WHERE id = ?", [ fromAccountId ] );
    queryExecute( "UPDATE accounts SET balance = balance + 100 WHERE id = ?", [ toAccountId ] );
}
```

## 🔄 Transaction Events

See [transaction events](interceptors/core-interception-points/transaction-events.md) for a list of events that are triggered during transaction lifecycles such as begin, commit, rollback, and savepoint operations.

## 🏗️ Nested Transactions

BoxLang fully supports nested or "child" transactions. Nested transactions use the same database connection as the parent transaction, which means queries will run on the same datasource as the parent, using the same connection parameters, and can be rolled back partially or in whole as the parent issues `transactionRollback()` statements.

To achieve all this, BoxLang transactions are savepoint-driven. All savepoints created (and referenced) within child transactions are prefixed within a unique ID to prevent collision. For example, executing `transactionSetSavepoint( 'insert' )` within a child transaction will under the hood create a `CHILD_{UUID}_insert` savepoint. Furthermore, when child transaction begins a `CHILD_{UUID}_BEGIN` savepoint is created which will be used as a rollback point if `transactionRollback()` is called with no savepoint parameter.

### 📋 Nested Transaction Behaviors

- Rolling back the child transaction will roll back to the `CHILD_{UUID}_BEGIN` savepoint.
- A transaction commit in the child transaction _does not commit the transaction_, but instead creates a `CHILD_{UUID}_COMMIT` savepoint.
- Rolling back the (entire) parent transaction will roll back the child transaction.
- Rolling back the parent transaction to a pre-child savepoint will roll back the entire child transaction.

### 📚 Examples

Check out a few examples to hammer home the behaviors of a nested transaction:

```js
transaction{
    queryExecute( "INSERT INTO vehicles ( make, model ) VALUES ( 'Ford', 'Fusion' )", {} );
    transaction{
        queryExecute( "INSERT INTO vehicles ( make, model ) VALUES ( 'BMW', 'X3' )", {} );
        transactionRollback();
    }
}
```

In this example, the 'BMW X3' insert is rolled back by the unqualified `transactionRollback()` call, but the 'Ford Fusion' insert in the parent transaction is still committed to the database when the parent transaction completes:

| Make | Model  |
| ---- | ------ |
| Ford | Fusion |

Note that we would get the same result if the child transaction threw an exception instead of rolling back:

```js
transaction{
    queryExecute( "INSERT INTO vehicles ( make, model ) VALUES ( 'Ford', 'Fusion' )", {} );
    transaction{
        queryExecute( "INSERT INTO vehicles ( make, model ) VALUES ( 'BMW', 'X3' )", {} );
        doSomethingThatThrows();
    }
}
```

| Make | Model  |
| ---- | ------ |
| Ford | Fusion |

Let's run this same one again, but replace the child rollback with a commit, and add a rollback to the parent transaction:

```js
transaction{
    queryExecute( "INSERT INTO vehicles ( make, model ) VALUES ( 'Ford', 'Fusion' )", {} );
    transaction{
        queryExecute( "INSERT INTO vehicles ( make, model ) VALUES ( 'BMW', 'X3' )", {} );
        transactionCommit();
    }
    transactionRollback();
}
```

You can see that regardless of the `transactionCommit()` in the child transaction, **both** inserts are rolled back:

## 🧰 Transactional BIFs

See our list of transactional BIFs:

- [`isInTransaction()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/isInTransaction) - Check if currently inside a transaction
- [`transactionBegin()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/transactionBegin) - Start a new transaction manually
- [`transactionCommit()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/transactionCommit) - Commit the current transaction
- [`transactionRollback()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/transactionRollback) - Roll back the current transaction
- [`transactionSetSavepoint()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/transactionSetSavepoint) - Create a savepoint for partial rollbacks

## 🎨 Common Patterns

### 💰 Financial Transfers

```js
function transferMoney( fromAccount, toAccount, amount ) {
    transaction isolation="serializable" {
        // Verify sufficient funds
        var fromBalance = queryExecute(
            "SELECT balance FROM accounts WHERE id = ? FOR UPDATE",
            [ fromAccount ]
        );

        if ( fromBalance.balance < amount ) {
            throw "Insufficient funds";
        }

        // Perform transfer
        queryExecute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            [ amount, fromAccount ]
        );

        queryExecute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            [ amount, toAccount ]
        );

        // Log the transaction
        queryExecute(
            "INSERT INTO transfer_log (from_account, to_account, amount, transferred_at) VALUES (?, ?, ?, NOW())",
            [ fromAccount, toAccount, amount ]
        );
    }
}
```

### 🛒 E-commerce Order Processing

```js
function processOrder( customerId, items ) {
    transaction {
        // Create order
        var orderResult = queryExecute(
            "INSERT INTO orders (customer_id, status, created_at) VALUES (?, 'pending', NOW())",
            [ customerId ],
            { result: "order" }
        );

        var orderId = order.generatedKey;
        var totalAmount = 0;

        transactionSetSavepoint( "beforeItems" );

        try {
            // Process each item
            for ( item in items ) {
                // Check inventory
                var inventory = queryExecute(
                    "SELECT quantity FROM inventory WHERE product_id = ? FOR UPDATE",
                    [ item.productId ]
                );

                if ( inventory.quantity < item.quantity ) {
                    throw "Insufficient inventory for product " & item.productId;
                }

                // Reserve inventory
                queryExecute(
                    "UPDATE inventory SET quantity = quantity - ? WHERE product_id = ?",
                    [ item.quantity, item.productId ]
                );

                // Add order item
                queryExecute(
                    "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)",
                    [ orderId, item.productId, item.quantity, item.price ]
                );

                totalAmount += item.price * item.quantity;
            }

            // Update order total and mark as confirmed
            queryExecute(
                "UPDATE orders SET total_amount = ?, status = 'confirmed' WHERE id = ?",
                [ totalAmount, orderId ]
            );

        } catch ( any e ) {
            transactionRollback( "beforeItems" );

            // Mark order as failed but keep the order record
            queryExecute(
                "UPDATE orders SET status = 'failed', error_message = ? WHERE id = ?",
                [ e.message, orderId ]
            );

            rethrow;
        }

        return orderId;
    }
}
```

### 🔄 Batch Data Processing

```js
function processBatchUpdates( updates ) {
    var batchSize = 100;
    var processed = 0;

    for ( var i = 1; i <= arrayLen( updates ); i += batchSize ) {
        transaction {
            var batch = arraySlice( updates, i, min( batchSize, arrayLen( updates ) - i + 1 ) );

            for ( update in batch ) {
                queryExecute(
                    "UPDATE products SET price = ? WHERE id = ?",
                    [ update.price, update.id ]
                );
                processed++;
            }

            // Log progress
            queryExecute(
                "UPDATE batch_jobs SET processed_count = ? WHERE id = ?",
                [ processed, batchJobId ]
            );
        }
    }
}
```

{% hint style="success" %}
**💡 Pro Tip:** The `transaction{}` block syntax automatically handles transaction lifecycle management, making it the preferred approach for most use cases. It maps directly to the `bx:transaction` component but provides cleaner, more readable code.
{% endhint %}

{% hint style="warning" %}
**⚠️ Warning:** Always keep transactions as short as possible to avoid blocking other operations. Long-running transactions can cause performance issues and deadlocks in high-concurrency applications.
{% endhint %}

{% hint style="info" %}
**🔗 Related:** For optimal performance, consider using [connection pooling](datasources.md) and properly configured [query caching](query-caching.md) alongside your transaction management strategy.
{% endhint %}
