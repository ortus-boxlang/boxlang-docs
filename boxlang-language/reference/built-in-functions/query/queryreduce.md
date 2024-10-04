# QueryReduce

This function reduces the query to a single value.

## Method Signature

```
QueryReduce(query=[query], callback=[function:BiFunction], initialValue=[any])
```

### Arguments

| Argument       | Type                  | Required | Description                                                                                                                                                                                                                                         | Default |
| -------------- | --------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `query`        | `query`               | `true`   | The query to iterate over                                                                                                                                                                                                                           |         |
| `callback`     | `function:BiFunction` | `true`   | <p>The function to invoke for each item. The function will be passed 4 arguments: the accumulator, the current item, the current index, and the query. You can alternatively pass a Java Predicate which will only receive the first 2<br>args.</p> |         |
| `initialValue` | `any`                 | `true`   | The initial value to use for the reduction                                                                                                                                                                                                          |         |

## Examples

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
* [QueryInsertAt](queryinsertat.md)
* [QueryKeyExists](querykeyexists.md)
* [QueryMap](querymap.md)
* [QueryNew](querynew.md)
* [QueryPrepend](queryprepend.md)
* [QueryRecordCount](queryrecordcount.md)
* [QueryReverse](queryreverse.md)
* [QueryRowData](queryrowdata.md)
* [QueryRowSwap](queryrowswap.md)
* [QuerySetCell](querysetcell.md)
* [QuerySetRow](querysetrow.md)
* [QuerySlice](queryslice.md)
* [QuerySome](querysome.md)
* [QuerySort](querysort.md)
