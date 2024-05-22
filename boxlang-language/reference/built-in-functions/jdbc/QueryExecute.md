[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryExecute`

Execute an SQL query and returns the results.

## Method Signature
```
QueryExecute(sql=[String], params=[any], options=[struct])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `sql` | `String` | `true` | The SQL to execute |  |
| `params` | `any` | `false` | An array of binding parameters or a struct of named binding parameters | `[]` |
| `options` | `struct` | `false` | A struct of query options |  |

## Examples

```
QueryExecute(sql=[String], params=[any], options=[struct])
```

## Related
  * [IsInTransaction](./IsInTransaction.md)
  * [IsWithinTransaction](./IsWithinTransaction.md)
  * [TransactionCommit](./TransactionCommit.md)
  * [TransactionRollback](./TransactionRollback.md)
  * [TransactionSetSavepoint](./TransactionSetSavepoint.md)
