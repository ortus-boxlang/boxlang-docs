# QueryReduce

This function reduces the query to a single value.

## Method Signature

```
QueryReduce(query=[query], callback=[function], initialValue=[any])
```

### Arguments

| Argument       | Type       | Required   | Description                                                                                                        | Default   |
| -------------- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------ | --------- |
| `query`        | `query`    | `true`     | The query to iterate over                                                                                          |           |
| `callback`     | `function` | `true`     | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query. |           |
| `initialValue` | `any`      | `true`     | The initial value to use for the reduction                                                                         |           |
| ----------     | ------     | ---------- | -------------                                                                                                      | --------- |

## Examples

```
QueryReduce(query=[query], callback=[function], initialValue=[any])
```

## Related

* [QueryAddColumn](queryaddcolumn.md)
* [QueryAddRow](queryaddrow.md)
* [QueryAppend](queryappend.md)
* [QueryClear](queryclear.md)
* [QueryColumnArray](querycolumnarray.md)
* [QueryColumnCount](querycolumncount.md)
* [QueryColumnData](querycolumndata.md)
* [QueryColumnExists](querycolumnexists.md)
* [QueryCurrentRow](querycurrentrow.md)
* [QueryDeleteColumn](querydeletecolumn.md)
* [QueryDeleteRow](querydeleterow.md)
* [QueryEach](queryeach.md)
* [QueryEvery](queryevery.md)
* [QueryFilter](queryfilter.md)
* [QueryGetCell](querygetcell.md)
* [QueryGetResult](querygetresult.md)
* [QueryKeyExists](querykeyexists.md)
* [QueryMap](querymap.md)
* [QueryNew](querynew.md)
* [QueryPrepend](queryprepend.md)
* [QueryRecordCount](queryrecordcount.md)
* [QueryRowData](queryrowdata.md)
* [QuerySetCell](querysetcell.md)
* [QuerySetRow](querysetrow.md)
* [QuerySlice](queryslice.md)
* [QuerySome](querysome.md)
* [QuerySort](querysort.md)
