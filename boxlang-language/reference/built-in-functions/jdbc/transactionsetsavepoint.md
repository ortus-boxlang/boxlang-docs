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
  * [IsInTransaction](boxlang-language/reference/built-in-functions/IsInTransaction.md)
  * [IsWithinTransaction](boxlang-language/reference/built-in-functions/IsWithinTransaction.md)
  * [QueryExecute](boxlang-language/reference/built-in-functions/QueryExecute.md)
  * [TransactionCommit](boxlang-language/reference/built-in-functions/TransactionCommit.md)
  * [TransactionRollback](boxlang-language/reference/built-in-functions/TransactionRollback.md)
