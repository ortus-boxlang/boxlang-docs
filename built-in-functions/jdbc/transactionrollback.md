# TransactionRollback

Rollback the current transaction and discard all unpersisted queries.

## Method Signature

```
TransactionRollback(savepoint=[string])
```

### Arguments

| Argument    | Type     | Required   | Description   | Default   |
| ----------- | -------- | ---------- | ------------- | --------- |
| `savepoint` | `string` | `false`    |               |           |
| ----------  | ------   | ---------- | ------------- | --------- |

## Examples

```
TransactionRollback(savepoint=[string])
```

## Related

* [IsInTransaction](isintransaction.md)
* [IsWithinTransaction](iswithintransaction.md)
* [QueryExecute](queryexecute.md)
* [TransactionCommit](transactioncommit.md)
* [TransactionSetSavepoint](transactionsetsavepoint.md)
