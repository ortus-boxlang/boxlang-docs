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
  * [QueryKeyExists](./QueryKeyExists.md)
  * [QueryMap](./QueryMap.md)
  * [QueryNew](./QueryNew.md)
  * [QueryPrepend](./QueryPrepend.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryReduce](./QueryReduce.md)
  * [QueryRowData](./QueryRowData.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
