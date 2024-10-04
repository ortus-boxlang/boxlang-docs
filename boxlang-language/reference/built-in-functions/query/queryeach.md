# QueryEach

Iterates over query rows and passes each row per iteration to a callback function

## Method Signature

```
QueryEach(query=[query], callback=[function:Consumer], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type                | Required | Description                                                                                                                                                                                        | Default |
| ------------ | ------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `query`      | `query`             | `true`   | The query to iterate over                                                                                                                                                                          |         |
| `callback`   | `function:Consumer` | `true`   | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query. You can alternatively pass a Java Consumer which will only receive the 1st arg. |         |
| `parallel`   | `boolean`           | `false`  | Specifies whether the items can be executed in parallel                                                                                                                                            | `false` |
| `maxThreads` | `integer`           | `false`  | The maximum number of threads to use when parallel = true                                                                                                                                          |         |

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
* [QueryReduce](queryreduce.md)
* [QueryReverse](queryreverse.md)
* [QueryRowData](queryrowdata.md)
* [QueryRowSwap](queryrowswap.md)
* [QuerySetCell](querysetcell.md)
* [QuerySetRow](querysetrow.md)
* [QuerySlice](queryslice.md)
* [QuerySome](querysome.md)
* [QuerySort](querysort.md)
