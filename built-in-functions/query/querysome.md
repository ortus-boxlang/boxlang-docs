# QuerySome

This function calls a given closure/function with every element in a given query and returns true, if one of the closure calls returns true

## Method Signature

```
QuerySome(query=[query], callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])
```

### Arguments

| Argument       | Type       | Required   | Description                                                                                                        | Default   |
| -------------- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------ | --------- |
| `query`        | `query`    | `true`     | The query to iterate over                                                                                          |           |
| `callback`     | `function` | `true`     | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query. |           |
| `parallel`     | `boolean`  | `false`    | Specifies whether the items can be executed in parallel                                                            | false     |
| `maxThreads`   | `integer`  | `false`    | The maximum number of threads to use when parallel = true                                                          |           |
| `initialValue` | `any`      | `false`    |                                                                                                                    |           |
| ----------     | ------     | ---------- | -------------                                                                                                      | --------- |

## Examples

```
QuerySome(query=[query], callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])
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
* [QueryReduce](queryreduce.md)
* [QueryRowData](queryrowdata.md)
* [QuerySetCell](querysetcell.md)
* [QuerySetRow](querysetrow.md)
* [QuerySlice](queryslice.md)
* [QuerySort](querysort.md)
