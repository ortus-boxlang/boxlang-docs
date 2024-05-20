# QuerySetRow

Adds or updates a row in a query based on the provided row data and position.

## Method Signature

```
QuerySetRow(query=[query], rowNumber=[integer], rowData=[any])
```

### Arguments

| Argument    | Type      | Required   | Description                                                                          | Default   |
| ----------- | --------- | ---------- | ------------------------------------------------------------------------------------ | --------- |
| `query`     | `query`   | `true`     | The query object to which the row should be added or updated.                        |           |
| `rowNumber` | `integer` | `false`    | Optional position of the row to update; if omitted or zero, a new row will be added. | 0         |
| `rowData`   | `any`     | `true`     | A struct or array containing data for the row.                                       |           |
| ----------  | ------    | ---------- | -------------                                                                        | --------- |

## Examples

```
QuerySetRow(query=[query], rowNumber=[integer], rowData=[any])
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
* [QuerySlice](queryslice.md)
* [QuerySome](querysome.md)
* [QuerySort](querysort.md)
