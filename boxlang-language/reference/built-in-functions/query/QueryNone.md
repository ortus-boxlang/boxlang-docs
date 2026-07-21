[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `QueryNone`

Used to iterate over a Query and test whether <strong>NONE</strong> item meets the test callback.

This is the opposite of {@link QuerySome}.
 <p>
 The function will be passed 3 arguments: the value, the index, and the Query.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large Queries, especially when the test function is computationally expensive or the Query is large.

## Method Signature

```
QueryNone(query=[query], callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query to test against the callback. |  |
| `callback` | `function:Predicate` | `true` |  |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is passed it will be used as the virtual thread argument |  |
| `virtual` | `boolean` | `false` | Whether to use virtual threads when running the filter in parallel. Defaults to false. Ignored if parallel is false. | `false` |

## Examples

### Test that no query rows satisfy a predicate

Returns `true` when the callback returns `false` for every row.

```java
q = queryNew( "name,age", "varchar,integer", [
    [ "Alice", 25 ],
    [ "Bob", 30 ]
] );
writeOutput( q.none( ( row ) => row.age > 100 ) );

```

Result: true

### Returns false when at least one row matches

```java
q = queryNew( "name,score", "varchar,integer", [
    [ "Alice", 85 ],
    [ "Bob", 45 ]
] );
writeOutput( q.none( ( row ) => row.score > 80 ) );

```

Result: false

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
  * [QueryPrepend](./QueryPrepend.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryRecordCount](./QueryRecordCount.md)
  * [QueryReduce](./QueryReduce.md)
  * [QueryRegisterFunction](./QueryRegisterFunction.md)
  * [QueryReverse](./QueryReverse.md)
  * [QueryRowData](./QueryRowData.md)
  * [QueryRowSwap](./QueryRowSwap.md)
  * [QuerySetCell](./QuerySetCell.md)
  * [QuerySetRow](./QuerySetRow.md)
  * [QuerySlice](./QuerySlice.md)
  * [QuerySome](./QuerySome.md)
  * [QuerySort](./QuerySort.md)
