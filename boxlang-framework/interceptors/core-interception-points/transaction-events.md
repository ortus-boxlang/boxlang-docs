---
description: Observe JDBC transaction lifecycle events and savepoint operations.
icon: database
---

# Transaction Events

BoxLang emits events during the lifecycle of a JDBC transaction which can be used to react to various transaction points in your app:

* [`onTransactionBegin`](#ontransactionbegin)
* [`onTransactionEnd`](#ontransactionend)
* [`onTransactionCommit`](#ontransactioncommit)
* [`onTransactionRollback`](#ontransactionrollback)
* [`onTransactionSetSavepoint`](#ontransactionsetsavepoint)
* [`onTransactionReleaseSavepoint`](#ontransactionreleasesavepoint)
* [`onTransactionAcquire`](#ontransactionacquire)
* [`onTransactionRelease`](#ontransactionrelease)

Transaction events are announced first to the application listener's interceptor pool when a request context exists, then to the runtime interceptor pool. Both pools receive the transaction's originating execution context explicitly. For BoxLang class interceptors, that context is available as the second handler argument and as `data.context`; it may be more specific than the request or runtime context. Payload structs are produced on demand for listening pools.

`onTransactionAcquire` has a connection because acquisition has succeeded. `onTransactionBegin` has no `connection` key. Every other event may have a null `connection` if no query has acquired one yet, including `onTransactionRelease`, which is announced during transaction cleanup even for a transaction that never queried the database. See [Transaction Behavior](../../jdbc/transactions.md#transaction-behavior).

With this in mind, you'll want to do null checks against the `connection` parameter in case no connection has yet been acquired:

```js
function onTransactionSetSavepoint( struct data, context ) {
	if ( data.keyExists( "connection" ) && data.connection != null ) {
		// The transaction has acquired a connection.
	}
}
```

`onTransactionAcquire` is useful for work that requires an acquired connection. In cleanup handlers, including `onTransactionRelease`, check for a null connection before accessing it.

## onTransactionBegin

This event fires when the transaction block is first opened and before the body begins processing.

Note that in BoxLang transactions, _no connection is acquired until the first JDBC query is executed_. This means that the `onTransactionBegin` will not have any connection to operate on. Most of the time, you will want to use [`onTransactionAcquire`](#ontransactionacquire) in place of `onTransactionBegin`.

| Data Key    | Type           | Description                        |
| ----------- | -------------- | ---------------------------------- |
| transaction | Java class     | Instance of the Transaction object |
| context | IBoxContext | Originating transaction execution context, also passed as the second argument to BoxLang class handlers. |

### Example

```js
function onTransactionBegin( struct data, context ){}
```

## onTransactionEnd

This event fires when the transaction block is closed after the body has finished processing.

`onTransactionEnd` and [`onTransactionRelease`](#ontransactionrelease) are both announced during cleanup. Neither guarantees that the transaction acquired a connection.

| Data Key    | Type           | Description                                                                                                                                            |
| ----------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| transaction | Java class     | Instance of the Transaction object                                                                                                                     |
| context | IBoxContext | Originating transaction execution context, also passed as the second argument to BoxLang class handlers. |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon. May be `null` if no JDBC queries have executed inside this transaction. |

### Example

```js
function onTransactionEnd( struct data, context ){}
```

## onTransactionAcquire

This event fires when the transaction first acquires a connection due to a JDBC query being executed within the body. You should prefer this over `onTransactionBegin`.

| Data Key    | Type           | Description                                                                   |
| ----------- | -------------- | ----------------------------------------------------------------------------- |
| transaction | Java class     | Instance of the Transaction object                                            |
| context | IBoxContext | Originating transaction execution context, also passed as the second argument to BoxLang class handlers. |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon |

### Example

```js
function onTransactionAcquire( struct data, context ){}
```

## onTransactionRelease

This event fires during transaction cleanup, before connection properties are reset and the connection is closed. The `connection` may be `null` when the transaction executed no queries.

| Data Key    | Type           | Description                                                                   |
| ----------- | -------------- | ----------------------------------------------------------------------------- |
| transaction | Java class     | Instance of the Transaction object                                            |
| context | IBoxContext | Originating transaction execution context, also passed as the second argument to BoxLang class handlers. |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon. May be `null` before a connection is acquired. |

### Example

```js
function onTransactionRelease( struct data, context ){}
```

## onTransactionCommit

This event fires when a transaction commit action occurs. Can occur multiple times (or never) within a single transaction.

| Data Key    | Type           | Description                                                                   |
| ----------- | -------------- | ----------------------------------------------------------------------------- |
| transaction | Java class     | Instance of the Transaction object                                            |
| context | IBoxContext | Originating transaction execution context, also passed as the second argument to BoxLang class handlers. |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon. May be `null` before a connection is acquired. |

### Example

```js
function onTransactionCommit( struct data, context ){}
```

## onTransactionRollback

This event fires when a transaction rollback action occurs. Can occur multiple times (or never) within a single transaction.

| Data Key    | Type           | Description                                                                   |
| ----------- | -------------- | ----------------------------------------------------------------------------- |
| transaction | Java class     | Instance of the Transaction object                                            |
| context | IBoxContext | Originating transaction execution context, also passed as the second argument to BoxLang class handlers. |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon. May be `null` before a connection is acquired. |
| savepoint   | String         | Savepoint name to roll back to. May be `null`.                                |

### Example

```js
function onTransactionRollback( struct data, context ){}
```

## onTransactionSetSavepoint

This event fires when a transaction savepoint is set.

| Data Key    | Type           | Description                                                                   |
| ----------- | -------------- | ----------------------------------------------------------------------------- |
| transaction | Java class     | Instance of the Transaction object                                            |
| context | IBoxContext | Originating transaction execution context, also passed as the second argument to BoxLang class handlers. |
| connection  | Java class     | Instance of the java.sql.Connection object this transaction is operating upon. May be `null` before a connection is acquired. |
| savepoint   | String         | Savepoint name to set.                                                        |

### Example

```js
function onTransactionSetSavepoint( struct data, context ){}
```

## onTransactionReleaseSavepoint

{% hint style="info" %}
Added in BoxLang 1.19.0 (currently unreleased).
{% endhint %}

This event fires for an explicit savepoint-release attempt after the name has been validated and found in the transaction registry, but before JDBC release and registry invalidation. It does not confirm successful release: the driver can still reject the operation. Invalid or missing names fail before this event is announced.

Release is optional cleanup; it does not commit or roll back changes. Pending savepoints can be released before the first query, so `connection` may be `null`. This event is distinct from `onTransactionRelease`, which concerns transaction connection cleanup.

| Data Key | Type | Description |
| --- | --- | --- |
| transaction | Java class | Instance of the transaction object announcing the operation. |
| context | IBoxContext | Originating transaction execution context, also passed as the second argument to BoxLang class handlers. |
| connection | Java class | Transaction's JDBC connection, or `null` if none has been acquired. |
| savepoint | String | Name of the savepoint to release. Nested transaction names include the child's internal prefix. |

### Example

```js
function onTransactionReleaseSavepoint( struct data, context ) {
	writeLog( text = "Releasing transaction savepoint: " & data.savepoint )
}
```

See [`transactionReleaseSavepoint()`](../../../boxlang-language/reference/built-in-functions/jdbc/TransactionReleaseSavepoint.md) for the API, failure behavior, and savepoint lifetime rules.
