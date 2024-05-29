[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `TransactionCommit`

Commit the current transaction and persist all stored queries.

You can continue to use the transaction after a ,<code>,transactionCommit(),</code>, call, but you will not be able to roll back past (before) this
 point since the changes are fully persisted to the database.

## Method Signature

```
TransactionCommit()
```

### Arguments

This function does not accept any arguments

## Examples

```
TransactionCommit()
```

## Related

  * [IsInTransaction](./IsInTransaction.md)
  * [IsWithinTransaction](./IsWithinTransaction.md)
  * [QueryExecute](./QueryExecute.md)
  * [TransactionRollback](./TransactionRollback.md)
  * [TransactionSetSavepoint](./TransactionSetSavepoint.md)
