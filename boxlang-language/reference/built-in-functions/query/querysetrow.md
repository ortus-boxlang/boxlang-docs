[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QuerySetRow`

Adds or updates a row in a query based on the provided row data and position.

## Method Signature
```
QuerySetRow(query=[query], rowNumber=[integer], rowData=[any])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query object to which the row should be added or updated. |  |
| `rowNumber` | `integer` | `false` | Optional position of the row to update; if omitted or zero, a new row will be added. | `0` |
| `rowData` | `any` | `true` | A struct or array containing data for the row. |  |

## Examples

```
QuerySetRow(query=[query], rowNumber=[integer], rowData=[any])
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
  * [QueryNew](boxlang-language/reference/built-in-functions/QueryNew.md)
  * [QueryPrepend](boxlang-language/reference/built-in-functions/QueryPrepend.md)
  * [QueryRecordCount](boxlang-language/reference/built-in-functions/QueryRecordCount.md)
  * [QueryReduce](boxlang-language/reference/built-in-functions/QueryReduce.md)
  * [QueryRowData](boxlang-language/reference/built-in-functions/QueryRowData.md)
  * [QuerySetCell](boxlang-language/reference/built-in-functions/QuerySetCell.md)
  * [QuerySlice](boxlang-language/reference/built-in-functions/QuerySlice.md)
  * [QuerySome](boxlang-language/reference/built-in-functions/QuerySome.md)
  * [QuerySort](boxlang-language/reference/built-in-functions/QuerySort.md)
