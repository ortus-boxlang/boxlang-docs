[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryReduce`

This function reduces the query to a single value.

## Method Signature

```
QueryReduce(query=[query], callback=[function:BiFunction], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to iterate over |  |
| `callback` | `function:BiFunction` | `true` | The function to invoke for each item. The function will be passed 4 arguments: the accumulator, the current item, the current index, and the query. You can alternatively pass a Java Predicate which will only receive the first 2<br>                    args. |  |
| `initialValue` | `any` | `true` | The initial value to use for the reduction |  |

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
  * [QueryFilter](./QueryFilter.md)
  * [QueryGetCell](./QueryGetCell.md)
  * [QueryGetResult](./QueryGetResult.md)
  * [QueryInsertAt](./QueryInsertAt.md)
  * [QueryKeyExists](./QueryKeyExists.md)
  * [QueryMap](./QueryMap.md)
  * [QueryNew](./QueryNew.md)
  * [QueryPrepend](./QueryPrepend.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryReverse](./QueryReverse.md)
  * [QueryRowData](./QueryRowData.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
