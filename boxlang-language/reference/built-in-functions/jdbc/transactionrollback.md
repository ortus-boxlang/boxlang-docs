# TransactionRollback

Rollback the current transaction and discard all unpersisted queries.

, Only the changes made since the last ,`,transactionSetSavepoint(),`, or ,`,transactionCommit(),`, call will be discarded. ,

, If no transaction is found in the current context, this method will throw an exception.

## Method Signature

```
TransactionRollback(savepoint=[string])
```

### Arguments

| Argument    | Type     | Required | Description                                                                                               | Default |
| ----------- | -------- | -------- | --------------------------------------------------------------------------------------------------------- | ------- |
| `savepoint` | `string` | `false`  | String name of the savepoint to rollback to. If not provided, the entire transaction will be rolled back. |         |

## Examples

### Using TransactionRollback with TransactionCommit

This simple example shows two JDBC queries executed inside a transaction. The first query, an INSERT, is committed to the database while the second is rolled back.

```java
transaction {
    queryExecute( "INSERT INTO vehicles (id,make) VALUES (8, 'Ford' )", {}, { datasource : "carDB" } );
    transactionCommit();

    queryExecute( "UPDATE developers SET name = 'Chevrolet' WHERE id=8", {}, { datasource : "carDB" } );
    transactionRollback();
}
```

Note that the rollback cannot affect the INSERT statement, since it has already been committed ("persisted") to the database.

#### Using TransactionRollback with TransactionSetSavepoint

Many times, you may wish to roll back only a portion of a transaction. This is possible by setting a "savepoint" upon the transaction:

```java
transaction {
    queryExecute( "INSERT INTO vehicles (id,make) VALUES (8, 'Ford' )", {}, { datasource : "carDB" } );
    transactionSetSavepoint( 'insert' );

    queryExecute( "UPDATE developers SET name = 'Chevrolet' WHERE id=8", {}, { datasource : "carDB" } );
    transactionRollback( 'insert' );
}
```

Multiple savepoints can be set or referenced.

## Related

* [IsInTransaction](isintransaction.md)
* [IsWithinTransaction](iswithintransaction.md)
* [PreserveSingleQuotes](preservesinglequotes.md)
* [QueryExecute](queryexecute.md)
* [TransactionCommit](transactioncommit.md)
* [TransactionSetSavepoint](transactionsetsavepoint.md)
