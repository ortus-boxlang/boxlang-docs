[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryReduce`

This function reduces the query to a single value.

## Method Signature
```
QueryReduce(query=[query], callback=[function], initialValue=[any])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to iterate over | |
| `callback` | `function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query. | |
| `initialValue` | `any` | `true` | The initial value to use for the reduction | |
|----------|------|----------|-------------|---------|



## Examples

```
QueryReduce(query=[query], callback=[function], initialValue=[any])
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
  * [QueryNew](QueryNew.md)
  * [QueryPrepend](QueryPrepend.md)
  * [QueryRecordCount](QueryRecordCount.md)
  * [QueryRowData](QueryRowData.md)
  * [QuerySetCell](QuerySetCell.md)
  * [QuerySetRow](QuerySetRow.md)
  * [QuerySlice](QuerySlice.md)
  * [QuerySome](QuerySome.md)
  * [QuerySort](QuerySort.md)
