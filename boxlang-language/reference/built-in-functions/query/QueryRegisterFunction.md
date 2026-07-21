[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryRegisterFunction`

Register a new scalar or aggregate function for use with Query of Query.

Functions only need to be registered once per runtime and they will be cached in memory until
 the runtime restarts.

## Method Signature

```
QueryRegisterFunction(name=[string], function=[function], returnType=[string], type=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The name of the function to register without parenthesis. You will reference it in your SQL with this name. |  |
| `function` | `function` | `true` | The function to register. This can be a closure or a function reference. For scalar functions, the function will receive a value for each incoming argument and must return a single value.<br>                    For aggregate functions, the function will receive a value for each incoming argument in the form of an array of values representing each row being aggregated and must return a single value.<br>                    Null values are not passed into aggregates. Aggregate functions should return a scalar value<br>                    so the size of the array won't necessarily match the number of rows in the query, and may be different across columns. |  |
| `returnType` | `string` | `true` | The return type of the function as a query column type. Default is "Object". This can be any valid query column type. This can be used to enforce<br>                      how the return values of this function are handled. For example, customFunc() + customFunc2() will behave differently based on whether the custom functions return strings or numbers. | `Object` |
| `type` | `string` | `true` | The type of function to register. This can be "scalar" or "aggregate". Default is "scalar". | `scalar` |

## Examples

### Register a function available within query operations

```java
queryRegisterFunction( "doubleIt", ( value ) => value * 2 );
q = queryNew( "n", "integer", [ [ 5 ], [ 10 ] ] );
result = q.map( ( row ) => doubleIt( row.n ) );
writeOutput( result[ 1 ] );

```

Result: 10

## Related

  * [QueryAddColumn](./QueryAddColumn.md)
  * [QueryAddRow](./QueryAddRow.md)
  * [QueryAppend](./QueryAppend.md)
  * [QueryClear](./QueryClear.md)
  * [QueryColumnArray](./QueryColumnArray.md)
  * [QueryColumnCount](./QueryColumnCount.md)
  * [QueryColumnData](./QueryColumnData.md)
  * [QueryColumnExists](./QueryColumnExists.md)
  * [QueryColumnList](./QueryColumnList.md)
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
  * [QueryNone](./QueryNone.md)
  * [QueryPrepend](./QueryPrepend.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryReduce](./QueryReduce.md)
  * [QueryReverse](./QueryReverse.md)
  * [QueryRowData](./QueryRowData.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
