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
  * [QueryAddColumn](boxlang-language/reference/built-in-functions/QueryAddColumn.md)
  * [QueryAddRow](boxlang-language/reference/built-in-functions/QueryAddRow.md)
  * [QueryAppend](boxlang-language/reference/built-in-functions/QueryAppend.md)
  * [QueryClear](boxlang-language/reference/built-in-functions/QueryClear.md)
  * [QueryColumnArray](boxlang-language/reference/built-in-functions/QueryColumnArray.md)
  * [QueryColumnCount](boxlang-language/reference/built-in-functions/QueryColumnCount.md)
  * [QueryColumnData](boxlang-language/reference/built-in-functions/QueryColumnData.md)
  * [QueryColumnExists](boxlang-language/reference/built-in-functions/QueryColumnExists.md)
  * [QueryCurrentRow](boxlang-language/reference/built-in-functions/QueryCurrentRow.md)
  * [QueryDeleteColumn](boxlang-language/reference/built-in-functions/QueryDeleteColumn.md)
  * [QueryDeleteRow](boxlang-language/reference/built-in-functions/QueryDeleteRow.md)
  * [QueryEach](boxlang-language/reference/built-in-functions/QueryEach.md)
  * [QueryEvery](boxlang-language/reference/built-in-functions/QueryEvery.md)
  * [QueryFilter](boxlang-language/reference/built-in-functions/QueryFilter.md)
  * [QueryGetCell](boxlang-language/reference/built-in-functions/QueryGetCell.md)
  * [QueryGetResult](boxlang-language/reference/built-in-functions/QueryGetResult.md)
  * [QueryKeyExists](boxlang-language/reference/built-in-functions/QueryKeyExists.md)
  * [QueryMap](boxlang-language/reference/built-in-functions/QueryMap.md)
  * [QueryPrepend](boxlang-language/reference/built-in-functions/QueryPrepend.md)
  * [QueryRecordCount](boxlang-language/reference/built-in-functions/QueryRecordCount.md)
  * [QueryReduce](boxlang-language/reference/built-in-functions/QueryReduce.md)
  * [QueryRowData](boxlang-language/reference/built-in-functions/QueryRowData.md)
  * [QuerySetCell](boxlang-language/reference/built-in-functions/QuerySetCell.md)
  * [QuerySetRow](boxlang-language/reference/built-in-functions/QuerySetRow.md)
  * [QuerySlice](boxlang-language/reference/built-in-functions/QuerySlice.md)
  * [QuerySome](boxlang-language/reference/built-in-functions/QuerySome.md)
  * [QuerySort](boxlang-language/reference/built-in-functions/QuerySort.md)
