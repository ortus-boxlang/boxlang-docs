[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `AsyncAll`

This BIF accepts an array of futures/closures/lambdas and executes them all in parallel.

It returns a BoxFuture that will contain an array of results once all futures are completed
 successfully.
 <p>
 This means that the futures will be executed in parallel and the results will be returned in the order
 that they were passed in. This also means that this operation is non-blocking and will return immediately
 until you call get() on the future.
 <p>
 Each future can be a BoxFuture or a CompletableFuture or a BoxLang Function that will be treated as a future.

 <pre>
 results = all( [f1, f2, f3] ).get()
 all( [f1, f2, f3] ).then( (values) => logResults( values ) );
 </pre>

## Method Signature

```
AsyncAll(futures=[array], executor=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `futures` | `array` | `true` | An array of BoxFuture objects to process in parallel |  |
| `executor` | `any` | `false` | The executor to use for the BoxFuture object. By default, the BoxFuture object will use the<br>                    default executor (ForkJoinPool.commonPool()). This can be the name of a named executor or a<br>                    custom executor record. |  |

## Examples



## Related

  * [AsyncAllApply](./AsyncAllApply.md)
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
