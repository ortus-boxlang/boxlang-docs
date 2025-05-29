[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `TransactionSetSavepoint`

Sets a savepoint in the current transaction.

This savepoint can then be a rollback point when executing a rollback via `transactionRollback(
 "mySavepointName" )`.

## Method Signature

```
TransactionSetSavepoint(savepoint=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `savepoint` | `string` | `true` | Specify a savepoint name. |  |

## Examples

#### Using TransactionSetSavepoint with TransactionRollback

Here's a simple example of using multiple savepoints within a transaction:

```java
transaction {
    queryExecute( "INSERT INTO vehicles (id,make) VALUES (8, 'Ford' )", {}, { datasource : "carDB" } );
    transactionSetSavepoint( 'insert' );

    queryExecute( "UPDATE developers SET name = 'Chevrolet' WHERE id=8", {}, { datasource : "carDB" } );
    transactionSetSavepoint( 'update' );

    // more stuff ...
    transactionRollback( 'insert' );
}
```

In this example, the UPDATE will be rolled back while the INSERT statement will remain. Remember that in `transactionRollback()`, the savepoint is not the name of a single savepoint to roll back, but the name of the savepoint to rollback TO.

### Roll back to a specified savepoint

This example runs multiple queries with a savepoint for each, and rolls back to the 'useradded' savepoint if the last query fails.

<a href="https://try.boxlang.io/?code=eJxNjDEOgzAMRef4FBZTmNjbW5QTmMQSUZHTBoOIUO5O3YnlL%2B%2F9Nx0PLSQrBU1Z8AQ3DJhk5aK4%2FRbcDY%2BsI%2B38yUnUY2ecYuTYYf80sdq%2F%2FRMkWWcu%2BN24VHAYSMOMnqQi96bdu6%2B8LBOFt7dMgwYX92Ew1w%3D%3D" target="_blank">Run Example</a>

```java
bx:transaction {
	// insert user
	transactionSetSavepoint( "useradded" );
	try {
	}
	// another query
	 catch (any e) {
		transactionRollback();
	}
}

```



## Related

  * [TransactionRollback](./TransactionRollback.md)
  * [PreserveSingleQuotes](./PreserveSingleQuotes.md)
  * [TransactionCommit](./TransactionCommit.md)
  * [QueryExecute](./QueryExecute.md)
  * [IsInTransaction](./IsInTransaction.md)
  * [IsWithinTransaction](./IsWithinTransaction.md)
