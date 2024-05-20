# QueryFilter

Filters query rows specified in filter criteria

## Method Signature

```
QueryFilter(query=[query], callback=[function], parallel=[boolean], maxThreads=[integer])
```

### Arguments

| Argument     | Type       | Required   | Description                                                                                                     | Default   |
| ------------ | ---------- | ---------- | --------------------------------------------------------------------------------------------------------------- | --------- |
| `query`      | `query`    | `true`     | The query to get filtered                                                                                       |           |
| `callback`   | `function` | `true`     | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. |           |
| `parallel`   | `boolean`  | `false`    |                                                                                                                 | false     |
| `maxThreads` | `integer`  | `false`    |                                                                                                                 |           |
| ----------   | ------     | ---------- | -------------                                                                                                   | --------- |

## Examples

```
QueryFilter(query=[query], callback=[function], parallel=[boolean], maxThreads=[integer])
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
