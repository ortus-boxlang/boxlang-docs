[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryEvery`

Executes a callback/closure against every row in a query and returns true if the callback/closure returned true for every row.

## Method Signature
```
QueryEvery(query=[query], closure=[function], parallel=[boolean], maxThreads=[integer])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to iterate over |  |
| `closure` | `function` | `true` | The function to invoke for each item. The function will be passed 1 argument: the row. |  |
| `parallel` | `boolean` | `false` | Specifies whether the items can be executed in parallel | `false` |
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when parallel = true |  |

## Examples

```
QueryEvery(query=[query], closure=[function], parallel=[boolean], maxThreads=[integer])
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
