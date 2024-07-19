[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ExecutorNew`

Creates and registers a new executor by name and type.

The return value is an ExecutorRecord object that can be used to interact with the executor.

 Available types are:
 - "cached" - Creates a cached thread pool executor.
 - "fixed" - Creates a fixed thread pool executor.
 - "fork_join" - Creates a fork-join pool executor.
 - "scheduled" - Creates a scheduled thread pool executor.
 - "single" - Creates a single thread executor.
 - "virtual" - Creates a virtual thread executor.
 - "work_stealing" - Creates a work-stealing thread pool executor.

## Method Signature

```
ExecutorNew(name=[string], type=[string], maxThreads=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The name of the executor to create if not already created |  |
| `type` | `string` | `true` | The type of executor to create |  |
| `maxThreads` | `integer` | `false` |  | `20` |

## Examples



## Related

  * [ExecutorGet](./ExecutorGet.md)
  * [ExecutorHas](./ExecutorHas.md)
  * [ExecutorList](./ExecutorList.md)
  * [ExecutorShutdown](./ExecutorShutdown.md)
  * [ExecutorStatus](./ExecutorStatus.md)
  * [FutureNew](./FutureNew.md)
  * [IsInThread](./IsInThread.md)
  * [RunAsync](./RunAsync.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [ThreadTerminate](./ThreadTerminate.md)
