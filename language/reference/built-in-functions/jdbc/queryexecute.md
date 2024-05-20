# QueryExecute

Executes a query and returns the results.

## Method Signature

```
QueryExecute(sql=[String], params=[any], options=[struct])
```

### Arguments

| Argument   | Type     | Required   | Description                                                            | Default   |
| ---------- | -------- | ---------- | ---------------------------------------------------------------------- | --------- |
| `sql`      | `String` | `true`     | The SQL to execute                                                     |           |
| `params`   | `any`    | `false`    | An array of binding parameters or a struct of named binding parameters | \[]       |
| `options`  | `struct` | `false`    | A struct of queryExecute options                                       |           |
| ---------- | ------   | ---------- | -------------                                                          | --------- |

## Examples

```
QueryExecute(sql=[String], params=[any], options=[struct])
```

## Related

* [IsInTransaction](isintransaction.md)
* [IsWithinTransaction](iswithintransaction.md)
* [TransactionCommit](transactioncommit.md)
* [TransactionRollback](transactionrollback.md)
* [TransactionSetSavepoint](transactionsetsavepoint.md)
