# QueryFilter

Filters query rows specified in filter criteria

## Method Signature

```
QueryFilter(query=[query], callback=[function:Predicate], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type                 | Required | Description                                                                                                                                                                                                           | Default |
| ------------ | -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `query`      | `query`              | `true`   | The query to get filtered                                                                                                                                                                                             |         |
| `callback`   | `function:Predicate` | `true`   | The function to invoke for each item. The function will be passed 3 arguments: the query row as a struct, the row number, the query. You can alternatively pass a Java Predicate which will only receive the 1st arg. |         |
| `parallel`   | `boolean`            | `false`  |                                                                                                                                                                                                                       | `false` |
| `maxThreads` | `integer`            | `false`  |                                                                                                                                                                                                                       |         |

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
* [QueryGetCell](querygetcell.md)
* [QueryGetResult](querygetresult.md)
* [QueryInsertAt](queryinsertat.md)
* [QueryKeyExists](querykeyexists.md)
* [QueryMap](querymap.md)
* [QueryNew](querynew.md)
* [QueryPrepend](queryprepend.md)
* [QueryRecordCount](queryrecordcount.md)
* [QueryReduce](queryreduce.md)
* [QueryReverse](queryreverse.md)
* [QueryRowData](queryrowdata.md)
* [QueryRowSwap](queryrowswap.md)
* [QuerySetCell](querysetcell.md)
* [QuerySetRow](querysetrow.md)
* [QuerySlice](queryslice.md)
* [QuerySome](querysome.md)
* [QuerySort](querysort.md)
