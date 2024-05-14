[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QuerySlice`

Returns a subset of rows from an existing query

## Method Signature
```
QuerySlice(query=[query], offset=[integer], length=[integer])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query object to which the rows should be returned. | |
| `offset` | `integer` | `true` | The first row to include in the new query. | |
| `length` | `integer` | `false` | The number of rows to include, defaults to all remaining rows. | 0|
|----------|------|----------|-------------|---------|



## Examples

```
QuerySlice(query=[query], offset=[integer], length=[integer])
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
  * [QueryReduce](QueryReduce.md)
  * [QueryRowData](QueryRowData.md)
  * [QuerySetCell](QuerySetCell.md)
  * [QuerySetRow](QuerySetRow.md)
  * [QuerySome](QuerySome.md)
  * [QuerySort](QuerySort.md)
