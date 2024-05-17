# QueryEach

Iterates over query rows and passes each row per iteration to a callback function

## Method Signature

```
QueryEach(query=[query], callback=[function], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type       | Required   | Description                                                                            | Default   |
| ------------ | ---------- | ---------- | -------------------------------------------------------------------------------------- | --------- |
| `query`      | `query`    | `true`     | The query to iterate over                                                              |           |
| `callback`   | `function` | `true`     | The function to invoke for each item. The function will be passed 1 argument: the row. |           |
| `parallel`   | `boolean`  | `false`    | Specifies whether the items can be executed in parallel                                | false     |
| `maxThreads` | `integer`  | `false`    | The maximum number of threads to use when parallel = true                              |           |
| ----------   | ------     | ---------- | -------------                                                                          | --------- |

## Examples

```
QueryEach(query=[query], callback=[function], parallel=[boolean], maxThreads=[integer])
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
* [QuerySome](querysome.md)
* [QuerySort](querysort.md)
