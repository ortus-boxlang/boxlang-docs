[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryNew`

Return new query

## Method Signature
```
QueryNew(columnList=[any], columnTypeList=[string], rowData=[any])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `columnList` | `any` | `true` | The column list to be used in the query. Delimited list of column names, or an empty string. |  |
| `columnTypeList` | `string` | `false` | Comma-delimited list specifying column data types. |  |
| `rowData` | `any` | `false` | Data to populate the query. Can be a struct (with keys matching column names), an array of structs, or an array of arrays (in<br>                   same order as columnList) |  |

## Examples

```
QueryNew(columnList=[any], columnTypeList=[string], rowData=[any])
```

## Related
  * [QueryAddColumn](QueryAddColumn.md)
  * [QueryAddRow](QueryAddRow.md)
  * [QueryAppend](QueryAppend.md)
  * [QueryClear](QueryClear.md)
  * [QueryColumnArray](QueryColumnArray.md)
  * [QueryColumnCount](QueryColumnCount.md)
  * [QueryColumnData](QueryColumnData.md)
  * [QueryColumnExists](QueryColumnExists.md)
  * [QueryCurrentRow](QueryCurrentRow.md)
  * [QueryDeleteColumn](QueryDeleteColumn.md)
  * [QueryDeleteRow](QueryDeleteRow.md)
  * [QueryEach](QueryEach.md)
  * [QueryEvery](QueryEvery.md)
  * [QueryFilter](QueryFilter.md)
  * [QueryGetCell](QueryGetCell.md)
  * [QueryGetResult](QueryGetResult.md)
  * [QueryKeyExists](QueryKeyExists.md)
  * [QueryMap](QueryMap.md)
  * [QueryPrepend](QueryPrepend.md)
  * [QueryRecordCount](QueryRecordCount.md)
  * [QueryReduce](QueryReduce.md)
  * [QueryRowData](QueryRowData.md)
  * [QuerySetCell](QuerySetCell.md)
  * [QuerySetRow](QuerySetRow.md)
  * [QuerySlice](QuerySlice.md)
  * [QuerySome](QuerySome.md)
  * [QuerySort](QuerySort.md)
