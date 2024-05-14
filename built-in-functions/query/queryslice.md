# QuerySlice

Returns a subset of rows from an existing query

## Method Signature

```
QuerySlice(query=[query], offset=[integer], length=[integer])
```

### Arguments

| Argument   | Type      | Required   | Description                                                    | Default   |
| ---------- | --------- | ---------- | -------------------------------------------------------------- | --------- |
| `query`    | `query`   | `true`     | The query object to which the rows should be returned.         |           |
| `offset`   | `integer` | `true`     | The first row to include in the new query.                     |           |
| `length`   | `integer` | `false`    | The number of rows to include, defaults to all remaining rows. | 0         |
| ---------- | ------    | ---------- | -------------                                                  | --------- |

## Examples

```
QuerySlice(query=[query], offset=[integer], length=[integer])
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
* [QuerySome](querysome.md)
* [QuerySort](querysort.md)
