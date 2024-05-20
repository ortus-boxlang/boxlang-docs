# TransactionSetSavepoint

Sets a savepoint in the current transaction.

## Method Signature

```
TransactionSetSavepoint(savepoint=[string])
```

### Arguments

| Argument    | Type     | Required   | Description   | Default   |
| ----------- | -------- | ---------- | ------------- | --------- |
| `savepoint` | `string` | `true`     |               |           |
| ----------  | ------   | ---------- | ------------- | --------- |

## Examples

```
TransactionSetSavepoint(savepoint=[string])
```

## Related

* [IsInTransaction](isintransaction.md)
* [IsWithinTransaction](iswithintransaction.md)
* [QueryExecute](queryexecute.md)
* [TransactionCommit](transactioncommit.md)
* [TransactionRollback](transactionrollback.md)
