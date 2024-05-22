[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `TransactionSetSavepoint`

Sets a savepoint in the current transaction.

## Method Signature
```
TransactionSetSavepoint(savepoint=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `savepoint` | `string` | `true` | Specify a savepoint name. |  |

## Examples

```
TransactionSetSavepoint(savepoint=[string])
```

## Related
  * [IsInTransaction](./IsInTransaction.md)
  * [IsWithinTransaction](./IsWithinTransaction.md)
  * [QueryExecute](./QueryExecute.md)
  * [TransactionCommit](./TransactionCommit.md)
  * [TransactionRollback](./TransactionRollback.md)
