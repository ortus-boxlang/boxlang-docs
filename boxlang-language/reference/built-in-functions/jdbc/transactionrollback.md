[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `TransactionRollback`

Rollback the current transaction and discard all unpersisted queries.

## Method Signature
```
TransactionRollback(savepoint=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `savepoint` | `string` | `false` | String name of the savepoint to rollback to. If not provided, the entire transaction will be rolled back. |  |

## Examples

```
TransactionRollback(savepoint=[string])
```

## Related
  * [IsInTransaction](boxlang-language/reference/built-in-functions/IsInTransaction.md)
  * [IsWithinTransaction](boxlang-language/reference/built-in-functions/IsWithinTransaction.md)
  * [QueryExecute](boxlang-language/reference/built-in-functions/QueryExecute.md)
  * [TransactionCommit](boxlang-language/reference/built-in-functions/TransactionCommit.md)
  * [TransactionSetSavepoint](boxlang-language/reference/built-in-functions/TransactionSetSavepoint.md)
