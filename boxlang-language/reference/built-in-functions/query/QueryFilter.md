[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryFilter`

Filters query rows specified in filter criteria

## Method Signature

```
QueryFilter(query=[query], callback=[function], parallel=[boolean], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to get filtered |  |
| `callback` | `function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. |  |
| `parallel` | `boolean` | `false` |  | `false` |
| `maxThreads` | `integer` | `false` |  |  |

## Examples



## Related

  * [QueryAddColumn](./QueryAddColumn.md)
  * [QueryAddRow](./QueryAddRow.md)
  * [QueryAppend](./QueryAppend.md)
  * [QueryClear](./QueryClear.md)
  * [QueryColumnArray](./QueryColumnArray.md)
  * [QueryColumnCount](./QueryColumnCount.md)
  * [QueryColumnData](./QueryColumnData.md)
  * [QueryColumnExists](./QueryColumnExists.md)
  * [QueryCurrentRow](./QueryCurrentRow.md)
  * [QueryDeleteColumn](./QueryDeleteColumn.md)
  * [QueryDeleteRow](./QueryDeleteRow.md)
  * [QueryEach](./QueryEach.md)
  * [QueryEvery](./QueryEvery.md)
  * [QueryGetCell](./QueryGetCell.md)
  * [QueryGetResult](./QueryGetResult.md)
  * [QueryKeyExists](./QueryKeyExists.md)
  * [QueryMap](./QueryMap.md)
  * [QueryNew](./QueryNew.md)
  * [QueryPrepend](./QueryPrepend.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryReduce](./QueryReduce.md)
  * [QueryRowData](./QueryRowData.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
