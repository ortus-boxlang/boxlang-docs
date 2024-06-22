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



## Related

  * [IsInTransaction](./IsInTransaction.md)
  * [IsWithinTransaction](./IsWithinTransaction.md)
  * [QueryExecute](./QueryExecute.md)
  * [TransactionCommit](./TransactionCommit.md)
  * [TransactionRollback](./TransactionRollback.md)
