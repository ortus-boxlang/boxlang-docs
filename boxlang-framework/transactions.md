# JDBC Transactions

## Transaction Behavior

### Connections

In BoxLang transactions, *no connection is acquired until the first JDBC query is executed*. Consider this transaction block:

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

## Transactional Events

BoxLang emits events during the lifecycle of a JDBC transaction which can be used to react to various transaction points in your app:

* onTransactionBegin
* onTransactionEnd
* onTransactionCommit
* onTransactionRollback
* onTransactionSetSavepoint
* onTransactionAcquire*
* onTransactionRelease*

Note that all these events (with the exception of `onTransactionAcquire` and `onTransactionRelease`) have the potential to be acting upon a no-op transaction, with a null `connection` parameter since no connection was ever obtained. ( Read more in [Transaction Behavior](#transaction-behavior) for a description of how transactions work. )

With this in mind, you'll want to do null checks against the `connection` parameter in case no connection has yet been acquired:

```js
function onTransactionSetSavepoint( struct data ){
    if( data.keyExists( "connection" ) && data.connection != null ){
        // we can be sure this transaction is "doing work".
    }
}
```

The two exceptions, as mentioned above, are `onTransactionAcquire` and `onTransactionRelease`, which *only* emit once a connection has been acquired, and is being released, respectively. Most of the time you'll want to listen for these events instead of their `onTransactionBegin`/`onTransactionEnd` counterparts.

## `onTransactionBegin`

This event fires when the transaction block is first opened and before the body begins processing. 

Note that in BoxLang transactions, *no connection is acquired until the first JDBC query is executed*. This means that the `onTransactionBegin` will not have any connection to operate on. Most of the time, you will want to use [`onTransactionAcquire`](#onTransactionAcquire) in place of `onTransactionBegin`.


| Parameter   | Parameter type | Description                                                                   |
|-------------|----------------|-------------------------------------------------------------------------------|
| transaction | Java class     | Instance of the Transaction object                                            |

Example:

```js
function onTransactionBegin( struct data ){}
```

## `onTransactionEnd`

This event fires when the transaction block is closed after the body has finished processing.

Consider using [`onTransactionRelease`](#onTransactionRelease) as an alternative to `onTransactionEnd` if you only want to listen for transactions that have done work.

| Parameter   | Parameter type | Description                                                                   |
|-------------|----------------|-------------------------------------------------------------------------------|
| transaction | Java class     | Instance of the Transaction object                                            |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon. May be `null` if no JDBC queries have executed inside this transaction. |

Example:

```js
function onTransactionEnd( struct data ){}
```

## `onTransactionAcquire`

This event fires when the transaction first acquires a connection due to a JDBC query being executed within the body. You should prefer this over `onTransactionBegin`.

| Parameter   | Parameter type | Description                                                                   |
|-------------|----------------|-------------------------------------------------------------------------------|
| transaction | Java class     | Instance of the Transaction object                                            |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon |

Example:

```js
function onTransactionAcquire( struct data ){}
```

## `onTransactionRelease`

This event fires when the transaction releases its connection. You should prefer this over `onTransactionEnd`.

| Parameter   | Parameter type | Description                                                                   |
|-------------|----------------|-------------------------------------------------------------------------------|
| transaction | Java class     | Instance of the Transaction object                                            |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon |

Example:

```js
function onTransactionRelease( struct data ){}
```

## `onTransactionCommit`

This event fires when a transaction commit action occurs. Can occur multiple times (or never) within a single transaction.

| Parameter   | Parameter type | Description                                                                   |
|-------------|----------------|-------------------------------------------------------------------------------|
| transaction | Java class     | Instance of the Transaction object                                            |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon |

Example:

```js
function onTransactionCommit( struct data ){}
```

## `onTransactionRollback`

This event fires when a transaction rollback action occurs. Can occur multiple times (or never) within a single transaction.

| Parameter   | Parameter type | Description                                                                   |
|-------------|----------------|-------------------------------------------------------------------------------|
| transaction | Java class     | Instance of the Transaction object                                            |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon |
| savepoint   | String         | Savepoint name to roll back to. May be `null`.                                |

Example:

```js
function onTransactionRollback( struct data ){}
```

## `onTransactionSetSavepoint`

This event fires when a transaction savepoint is set.

| Parameter   | Parameter type | Description                                                                   |
|-------------|----------------|-------------------------------------------------------------------------------|
| transaction | Java class     | Instance of the Transaction object                                            |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon |
| savepoint   | String         | Savepoint name to set.                                                        |

Example:

```js
function onTransactionSetSavepoint( struct data ){}
```

## Nested Transactions

BoxLang fully supports nested or "child" transactions. Nested transactions use the same database connection as the parent transaction, which means queries will run on the same datasource as the parent, using the same connection parameters, and can be rolled back partially or in whole as the parent issues `transactionRollback()` statements.

To achieve all this, BoxLang transactions are savepoint-driven. All savepoints created (and referenced) within child transactions are prefixed within a unique ID to prevent collision. For example, executing `transactionSetSavepoint( 'insert' )` within a child transaction will under the hood create a `CHILD_{UUID}_insert` savepoint. Furthermore, when child transaction begins a `CHILD_{UUID}_BEGIN` savepoint is created which will be used as a rollback point if `transactionRollback()` is called with no savepoint parameter.

Other behavioral notes:

* Rolling back the child transaction will roll back to the `CHILD_{UUID}_BEGIN` savepoint.
* A transaction commit in the child transaction *does not commit the transaction*, but instead creates a `CHILD_{UUID}_COMMIT` savepoint.
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
|------|--------|
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
|------|--------|
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

| Make | Model  |
|------|--------|

## Transactional BIFs

See our list of transactional BIFs:

* [`isInTransaction()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/isInTransaction)
* [`transactionCommit()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/transactionCommit)
* [`transactionRollback()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/transactionRollback)
* [`transactionSetSavepoint()`](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/jdbc/transactionSetSavepoint)