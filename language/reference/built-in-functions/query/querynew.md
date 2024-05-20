# QueryNew

Return new query

## Method Signature

```
QueryNew(columnList=[any], columnTypeList=[string], rowData=[any])
```

### Arguments

| Argument         | Type     | Required | Description                                                                                                                   | Default |
| ---------------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- | ------- |
| `columnList`     | `any`    | `true`   | The column list to be used in the query. Delimited list of column names, or an empty string.                                  |         |
| `columnTypeList` | `string` | `false`  | Comma-delimited list specifying column data types.                                                                            |         |
| `rowData`        | `any`    | `false`  | Data to populate the query. Can be a struct (with keys matching column names), an array of structs, or an array of arrays (in |         |

```
               same order as columnList) | |
```

\|----------|------|----------|-------------|---------|

## Examples

```
QueryNew(columnList=[any], columnTypeList=[string], rowData=[any])
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
* [QueryPrepend](queryprepend.md)
* [QueryRecordCount](queryrecordcount.md)
* [QueryReduce](queryreduce.md)
* [QueryRowData](queryrowdata.md)
* [QuerySetCell](querysetcell.md)
* [QuerySetRow](querysetrow.md)
* [QuerySlice](queryslice.md)
* [QuerySome](querysome.md)
* [QuerySort](querysort.md)
