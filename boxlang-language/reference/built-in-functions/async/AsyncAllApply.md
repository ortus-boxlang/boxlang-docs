[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `AsyncAllApply`

This function can accept an array of items or a struct of items and apply a function
 to each of the item's in parallel.

The `mapper` argument receives the appropriate item
 and must return a result.
 <p>
 The `errorHandler` is optional and will be called if the mapper function throws an exception.
 The error handler receives the exception and the item that caused it, allowing you to handle errors gracefully.
 <p>
 The result is a future that will return an array of results, or a struct of results if the input was a struct.
 <p>
 The `executor` argument is optional and allows you to specify a custom executor for the
 asynchronous operations. If not provided, the common fork-join pool will be used.
 <p>
 The `timeout` and `timeUnit` arguments allow you to specify a timeout for the operation.
 If the operation does not complete within the specified timeout, it will throw a TimeoutException.
 The allowed time units are: `DAYS`, `HOURS`, `MINUTES`, `SECONDS`, `MILLISECONDS`, `MICROSECONDS`, `NANOSECONDS`.
 <p>
 Example usage:

 <pre>
 // Array
 allApply( items, ( item ) => item.getMemento() )
 // Struct: The result object is a struct of `key` and `value`
 allApply( data, ( item ) => item.key &amp; item.value.toString() )
 </pre>

## Method Signature

```
AsyncAllApply(items=[any], mapper=[function], errorHandler=[function], executor=[any], timeout=[long], timeUnit=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `items` | `any` | `true` | The items to apply the function to. Can be an array or a struct. |  |
| `mapper` | `function` | `true` | The function to apply to each item. It receives the item as an argument and must return a result. |  |
| `errorHandler` | `function` | `false` | Optional function to handle errors. It receives the exception and the item that caused it. |  |
| `executor` | `any` | `false` | Optional executor to use for the asynchronous operations. If not provided, the common fork-join pool will be used. |  |
| `timeout` | `long` | `false` | Optional timeout for the operation. If the operation does not complete within this time, it will throw a TimeoutException. | `0` |
| `timeUnit` | `any` | `false` | Optional time unit for the timeout. Defaults to seconds. Allowed values are: `DAYS`, `HOURS`, `MINUTES`, `SECONDS`, `MILLISECONDS`, `MICROSECONDS`, `NANOSECONDS`. | `SECONDS` |

## Examples



## Related

  * [AsyncAll](./AsyncAll.md)
  * [AsyncAny](./AsyncAny.md)
  * [AsyncRun](./AsyncRun.md)
  * [ExecutorGet](./ExecutorGet.md)
  * [ExecutorHas](./ExecutorHas.md)
  * [ExecutorList](./ExecutorList.md)
  * [ExecutorNew](./ExecutorNew.md)
  * [ExecutorShutdown](./ExecutorShutdown.md)
  * [ExecutorStatus](./ExecutorStatus.md)
  * [FutureNew](./FutureNew.md)
  * [IsInThread](./IsInThread.md)
  * [isThreadAlive](./isThreadAlive.md)
  * [IsThreadInterrupted](./IsThreadInterrupted.md)
  * [RunAsync](./RunAsync.md)
  * [ThreadInterrupt](./ThreadInterrupt.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [ThreadNew](./ThreadNew.md)
  * [ThreadTerminate](./ThreadTerminate.md)
