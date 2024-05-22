[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryAddColumn`

Adds a column to a query and populates its rows with the contents of a one-dimensional array.

## Method Signature
```
QueryAddColumn(query=[query], columnName=[string], datatype=[any], array=[array])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query object to which the column should be added. |  |
| `columnName` | `string` | `true` | The name of the column to add. |  |
| `datatype` | `any` | `false` | The column data type of the new column or the array to populate the column with as a shortcut for "varchar". | `Varchar` |
| `array` | `array` | `false` |  | `[]` |

## Examples

```
QueryAddColumn(query=[query], columnName=[string], datatype=[any], array=[array])
```

## Related
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
  * [QuerySetRow](boxlang-language/reference/built-in-functions/QuerySetRow.md)
  * [QuerySlice](boxlang-language/reference/built-in-functions/QuerySlice.md)
  * [QuerySome](boxlang-language/reference/built-in-functions/QuerySome.md)
  * [QuerySort](boxlang-language/reference/built-in-functions/QuerySort.md)
