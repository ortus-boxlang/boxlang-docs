## Transactional Events

BoxLang emits events during the lifecycle of a JDBC transaction which can be used to react to various transaction points in your app:

* onTransactionBegin
* onTransactionEnd
* onTransactionCommit
* onTransactionRollback
* onTransactionSetSavepoint
* onTransactionAcquire\*
* onTransactionRelease\*

Note that all these events (with the exception of `onTransactionAcquire` and `onTransactionRelease`) have the potential to be acting upon a no-op transaction, with a null `connection` parameter since no connection was ever obtained. ( Read more in [Transaction Behavior](/boxlang-framework/transactions.md#transaction-behavior) for a description of how transactions work. )

With this in mind, you'll want to do null checks against the `connection` parameter in case no connection has yet been acquired:

```js
function onTransactionSetSavepoint( struct data ){
    if( data.keyExists( "connection" ) && data.connection != null ){
        // we can be sure this transaction is "doing work".
    }
}
```

The two exceptions, as mentioned above, are `onTransactionAcquire` and `onTransactionRelease`, which _only_ emit once a connection has been acquired, and is being released, respectively. Most of the time you'll want to listen for these events instead of their `onTransactionBegin`/`onTransactionEnd` counterparts.

## `onTransactionBegin`

This event fires when the transaction block is first opened and before the body begins processing.

Note that in BoxLang transactions, _no connection is acquired until the first JDBC query is executed_. This means that the `onTransactionBegin` will not have any connection to operate on. Most of the time, you will want to use [`ontransactionacquire`](#onTransactionAcquire) in place of `onTransactionBegin`.

| Parameter   | Parameter type | Description                        |
| ----------- | -------------- | ---------------------------------- |
| transaction | Java class     | Instance of the Transaction object |

Example:

```js
function onTransactionBegin( struct data ){}
```

## `onTransactionEnd`

This event fires when the transaction block is closed after the body has finished processing.

Consider using [`ontransactionrelease`](#onTransactionRelease) as an alternative to `onTransactionEnd` if you only want to listen for transactions that have done work.

| Parameter   | Parameter type | Description                                                                                                                                            |
| ----------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| transaction | Java class     | Instance of the Transaction object                                                                                                                     |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon. May be `null` if no JDBC queries have executed inside this transaction. |

Example:

```js
function onTransactionEnd( struct data ){}
```

## `onTransactionAcquire`

This event fires when the transaction first acquires a connection due to a JDBC query being executed within the body. You should prefer this over `onTransactionBegin`.

| Parameter   | Parameter type | Description                                                                   |
| ----------- | -------------- | ----------------------------------------------------------------------------- |
| transaction | Java class     | Instance of the Transaction object                                            |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon |

Example:

```js
function onTransactionAcquire( struct data ){}
```

## `onTransactionRelease`

This event fires when the transaction releases its connection. You should prefer this over `onTransactionEnd`.

| Parameter   | Parameter type | Description                                                                   |
| ----------- | -------------- | ----------------------------------------------------------------------------- |
| transaction | Java class     | Instance of the Transaction object                                            |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon |

Example:

```js
function onTransactionRelease( struct data ){}
```

## `onTransactionCommit`

This event fires when a transaction commit action occurs. Can occur multiple times (or never) within a single transaction.

| Parameter   | Parameter type | Description                                                                   |
| ----------- | -------------- | ----------------------------------------------------------------------------- |
| transaction | Java class     | Instance of the Transaction object                                            |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon |

Example:

```js
function onTransactionCommit( struct data ){}
```

## `onTransactionRollback`

This event fires when a transaction rollback action occurs. Can occur multiple times (or never) within a single transaction.

| Parameter   | Parameter type | Description                                                                   |
| ----------- | -------------- | ----------------------------------------------------------------------------- |
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
| ----------- | -------------- | ----------------------------------------------------------------------------- |
| transaction | Java class     | Instance of the Transaction object                                            |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon |
| savepoint   | String         | Savepoint name to set.                                                        |

Example:

```js
function onTransactionSetSavepoint( struct data ){}
```