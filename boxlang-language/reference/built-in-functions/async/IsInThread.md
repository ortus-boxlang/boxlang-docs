[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsInThread`

Verifies if the calling execution code is running in a thread or not.

## Method Signature

```
IsInThread()
```

### Arguments

This function does not accept any arguments

## Examples

### isinthread Example

Check if the code is running inside a bx:thread.

<a href="https://try.boxlang.io/?code=eJwrSi0sTS0u0fP0C%2FEIcnV0UbBVSEvMKU615iovyixJ9S8tKSgt0VDILPbMC8koSk1M0dBU0LTmSqqwKgFzFRKTSzLz82yVikrzlBTyEnNTbZUyoUqVFKq5OIswLUA2zJqrlqs4JzW1QEPB0MDAAGQ2isUY2oEKACLTOhQ%3D" target="_blank">Run Example</a>

```java
request.INTHREAD = false;
writeOutput( isInThread() );
bx:thread action="run" name="inThread" {
	request.INTHREAD = isInThread();
}
sleep( 1000 );
writeOutput( request.INTHREAD );

```

Result: falsetrue

### Additional Examples


## Related

  * [RunAsync](./RunAsync.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [IsThreadInterrupted](./IsThreadInterrupted.md)
  * [ExecutorGet](./ExecutorGet.md)
  * [ExecutorNew](./ExecutorNew.md)
  * [FutureNew](./FutureNew.md)
  * [ExecutorStatus](./ExecutorStatus.md)
  * [ExecutorList](./ExecutorList.md)
  * [ThreadTerminate](./ThreadTerminate.md)
  * [ThreadNew](./ThreadNew.md)
  * [ExecutorHas](./ExecutorHas.md)
  * [ThreadInterrupt](./ThreadInterrupt.md)
  * [ExecutorShutdown](./ExecutorShutdown.md)
  * [isThreadAlive](./isThreadAlive.md)
