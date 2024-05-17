[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryEach`

Iterates over query rows and passes each row per iteration to a callback function

## Method Signature
```
QueryEach(query=[query], callback=[function], parallel=[boolean], maxThreads=[integer])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to iterate over | |
| `callback` | `function` | `true` | The function to invoke for each item. The function will be passed 1 argument: the row. | |
| `parallel` | `boolean` | `false` | Specifies whether the items can be executed in parallel | false|
| `maxThreads` | `integer` | `false` | The maximum number of threads to use when parallel = true | |
|----------|------|----------|-------------|---------|



## Examples

```
QueryEach(query=[query], callback=[function], parallel=[boolean], maxThreads=[integer])
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
  * [QuerySlice](QuerySlice.md)
  * [QuerySome](QuerySome.md)
  * [QuerySort](QuerySort.md)
