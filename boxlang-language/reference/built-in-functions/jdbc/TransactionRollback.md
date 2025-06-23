[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `TransactionRollback`

Rollback the current transaction and discard all unpersisted queries.

<p>
 Only the changes made since the last <code>transactionSetSavepoint()</code> or <code>transactionCommit()</code> call will be discarded.
 <p>
 If no transaction is found in the current context, this method will throw an exception.

## Method Signature

```
TransactionRollback(savepoint=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `savepoint` | `string` | `false` | String name of the savepoint to rollback to. If not provided, the entire transaction will be rolled back. |  |

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

### Script Syntax

In this code, any error triggered will cause transactionRollback() to run and roll back the pending transaction

<a href="https://try.boxlang.io/?code=eJxLqrAqKUrMK05MLsnMz1Oo5uIsKaoEUZz6%2BgrJ%2BSmpCiX5CkWleUABJHXO%2Bbm5mSUamtZcnLUKyYklyRkKGol5lQqpmmCtSCqD8nNykhKTsyFquWq5AC39I%2Bw%3D" target="_blank">Run Example</a>

```java
bx:transaction {
	try {
		// code to run
		transactionCommit();
	} catch (any e) {
		transactionRollback();
	}
}

```



## Related

  * [IsInTransaction](./IsInTransaction.md)
  * [IsWithinTransaction](./IsWithinTransaction.md)
  * [PreserveSingleQuotes](./PreserveSingleQuotes.md)
  * [QueryExecute](./QueryExecute.md)
  * [TransactionCommit](./TransactionCommit.md)
  * [TransactionSetSavepoint](./TransactionSetSavepoint.md)
