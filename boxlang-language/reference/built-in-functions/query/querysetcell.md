# QuerySetCell

Sets a cell to a value.

## Method Signature

```
QuerySetCell(query=[query], column=[string], value=[any], row=[integer])
```

### Arguments

| Argument | Type      | Required | Description                                                                                        | Default |
| -------- | --------- | -------- | -------------------------------------------------------------------------------------------------- | ------- |
| `query`  | `query`   | `true`   | The query to set the cell in                                                                       |         |
| `column` | `string`  | `true`   | The column name to set the cell in                                                                 |         |
| `value`  | `any`     | `true`   | The value to set the cell to                                                                       |         |
| `row`    | `integer` | `false`  | The row number to set the cell in. If no row number is specified, the cell on the last row is set. |         |

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
* [QueryReduce](queryreduce.md)
* [QueryReverse](queryreverse.md)
* [QueryRowData](queryrowdata.md)
* [QueryRowSwap](queryrowswap.md)
* [QuerySetRow](querysetrow.md)
* [QuerySlice](queryslice.md)
* [QuerySome](querysome.md)
* [QuerySort](querysort.md)
