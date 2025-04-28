---
icon: database
---

# JDBC Transactions

## Transaction Behavior

### Connections

In BoxLang transactions, _no connection is acquired until the first JDBC query is executed_. Consider this transaction block:

```js
transaction{
    transactionSetSavepoint( 'beginning' );
    transactionRollback( 'beginning' );
    transactionCommit();
}
```

This transaction is a no-op. It begins, tries to set a savepoint, then roll back to the savepoint, then commit... **but never ran any JDBC queries**. Hence, every transactional BIF called above does exactly nothing (besides emit events).

### Datasources

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

## Transaction Events

See [transaction events](/boxlang-framework/interceptors/core-interception-points/transaction-events) for a list of events that are triggered during transaction lifecycles such as begin, commit, rollback, and savepoint operations.

## Nested Transactions

BoxLang fully supports nested or "child" transactions. Nested transactions use the same database connection as the parent transaction, which means queries will run on the same datasource as the parent, using the same connection parameters, and can be rolled back partially or in whole as the parent issues `transactionRollback()` statements.

To achieve all this, BoxLang transactions are savepoint-driven. All savepoints created (and referenced) within child transactions are prefixed within a unique ID to prevent collision. For example, executing `transactionSetSavepoint( 'insert' )` within a child transaction will under the hood create a `CHILD_{UUID}_insert` savepoint. Furthermore, when child transaction begins a `CHILD_{UUID}_BEGIN` savepoint is created which will be used as a rollback point if `transactionRollback()` is called with no savepoint parameter.

Other behavioral notes:

* Rolling back the child transaction will roll back to the `CHILD_{UUID}_BEGIN` savepoint.
* A transaction commit in the child transaction _does not commit the transaction_, but instead creates a `CHILD_{UUID}_COMMIT` savepoint.
* Rolling back the (entire) parent transaction will roll back the child transaction.
* Rolling back the parent transaction to a pre-child savepoint will roll back the entire child transaction.

### Examples

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

## Transactional BIFs

See our list of transactional BIFs:

* [`isInTransaction()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/isInTransaction)
* [`transactionCommit()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/transactionCommit)
* [`transactionRollback()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/transactionRollback)
* [`transactionSetSavepoint()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/transactionSetSavepoint)
