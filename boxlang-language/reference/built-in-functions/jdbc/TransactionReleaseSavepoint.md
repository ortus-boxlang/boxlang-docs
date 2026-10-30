---
description: Release a named transaction savepoint without committing or rolling back changes.
icon: database
---

# Function: `TransactionReleaseSavepoint`

Releases a savepoint in the current transaction. This is optional cleanup: it discards a recovery boundary without committing or rolling back database changes.

{% hint style="info" %}
Added in BoxLang 1.19.0 (currently unreleased). See the [1.19.x release notes](../../../../readme/release-history/1.19.0.md).
{% endhint %}

## Method Signature

```js
transactionReleaseSavepoint( savepoint )
```

### Arguments

| Argument | Type | Required | Description | Default |
| --- | --- | --- | --- | --- |
| `savepoint` | `string` | `true` | Name of an existing savepoint in the current transaction. Names are case-insensitive and cannot be blank. | |

### Returns

`null`.

## Behavior

* Release invalidates the named savepoint and every savepoint created after it. Earlier savepoints remain available.
* A released name can be used again with `transactionSetSavepoint()`.
* Rolling back to a named savepoint keeps that target available, so it can then be released. Committing, fully rolling back, or ending the outer transaction clears all savepoints.
* Savepoints created before the first query are pending. Releasing a pending savepoint updates the registry without acquiring a database connection or choosing a datasource.
* Once a connection exists, release calls JDBC `Connection.releaseSavepoint()`. The JDBC driver must support this operation.
* When nested transactions are enabled, a child can release its own savepoints; it cannot use this function to release a parent's savepoint.

### Errors

An active transaction is required. A blank, missing, released, or otherwise invalidated savepoint name raises an error. Unsupported JDBC release and other JDBC failures raise a `DatabaseException`; a failed JDBC release leaves the savepoint handles available for recovery.

Unlike this function, the `transaction action="releasesavepoint"` component action is silently ignored outside an active transaction, matching the component's other non-begin actions.

## Examples

### Release after successful work

This example assumes a configured default datasource and an existing `products` table. The update is committed when the outer transaction completes successfully. Releasing the savepoint does not commit it early.

```js
transaction {
	transactionSetSavepoint( "beforeUpdate" )
	queryExecute( "UPDATE products SET price = ? WHERE id = ?", [ { value: 19.99, sqltype: "decimal", scale: 2 }, 42 ] )
	transactionReleaseSavepoint( "beforeUpdate" )
}
```

### Roll back, release, and reuse a name

The first update is rolled back. The second update is retained if the outer transaction completes successfully.

```js
transaction {
	transactionSetSavepoint( "item" )
	queryExecute( "UPDATE products SET price = ? WHERE id = ?", [ { value: 19.99, sqltype: "decimal", scale: 2 }, 42 ] )
	transactionRollback( "item" )
	transactionReleaseSavepoint( "item" )

	transactionSetSavepoint( "item" )
	queryExecute( "UPDATE products SET price = ? WHERE id = ?", [ { value: 24.99, sqltype: "decimal", scale: 2 }, 42 ] )
	transactionReleaseSavepoint( "item" )
}
```

## Related

* [TransactionSetSavepoint](TransactionSetSavepoint.md)
* [TransactionRollback](TransactionRollback.md)
* [TransactionCommit](TransactionCommit.md)
* [Transaction component](../../components/jdbc/Transaction.md)
* [Transaction guide](../../../../boxlang-framework/jdbc/transactions.md)
* [Transaction events](../../../../boxlang-framework/interceptors/core-interception-points/transaction-events.md#ontransactionreleasesavepoint)
