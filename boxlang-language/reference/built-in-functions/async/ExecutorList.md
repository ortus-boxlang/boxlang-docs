[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ExecutorList`

Get's an array of all the executors registered in the system

## Method Signature

```
ExecutorList()
```

### Arguments

This function does not accept any arguments

## Examples

### List all registered executors

```java
executorNew( "pool1", "fixed", 2 );
executorNew( "pool2", "cached" );
execs = executorList();
writeOutput( execs.len() gte 2 );

```

Result: true

### Executor list contains executor names

```java
executorNew( "myExecutor", "single" );
execs = executorList();
writeOutput( execs.some( ( e ) => e.name() == "myExecutor" ) );

```

Result: true

## Related

  * [AsyncAll](./AsyncAll.md)
  * [AsyncAllApply](./AsyncAllApply.md)
  * [AsyncAny](./AsyncAny.md)
  * [AsyncRun](./AsyncRun.md)
  * [ExecutorDelete](./ExecutorDelete.md)
  * [ExecutorGet](./ExecutorGet.md)
  * [ExecutorHas](./ExecutorHas.md)
  * [ExecutorNew](./ExecutorNew.md)
  * [ExecutorShutdown](./ExecutorShutdown.md)
  * [ExecutorStatus](./ExecutorStatus.md)
  * [FutureNew](./FutureNew.md)
  * [IsInThread](./IsInThread.md)
  * [isThreadAlive](./isThreadAlive.md)
  * [IsThreadInterrupted](./IsThreadInterrupted.md)
  * [RunAsync](./RunAsync.md)
  * [ThreadCurrent](./ThreadCurrent.md)
  * [ThreadInterrupt](./ThreadInterrupt.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [ThreadNew](./ThreadNew.md)
  * [ThreadTerminate](./ThreadTerminate.md)
