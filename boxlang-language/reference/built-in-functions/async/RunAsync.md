[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `RunAsync`

Executes the given code asynchronously and returns to you a BoxFuture object which inherits from CompletableFuture.

This way you can create fluent asynchronous code that can be chained and composed.

## Method Signature

```
RunAsync(callback=[function], executor=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function` | `true` | The code to execute asynchronously, this can be a closure<br>                    or lambda. |  |
| `executor` | `any` | `false` | The executor to use for the asynchronous execution. This<br>                    can be an instance of an Executor class, or the name of a<br>                    registered executor in the AsyncService. |  |

## Examples

### Run a function asynchronously and get the result



<a href="https://try.boxlang.io/?code=eJxLKy0pLUpVsFUoKs1zLK7MS9ZQ0NBUsLVTqObiLEoFyuUpKHmk5uTkK4TnF%2BWkKCpZc9UqaFpzlRdllqT6l5YUlJZoKKSBDdFLTy0B6gVKAgCTuhrL" target="_blank">Run Example</a>

```java
future = runAsync( () => {
	return "Hello World!";
} );
writeOutput( future.get() );

```

Result: Hello World!

### Run a function after the asynchronous function and use a five milliseconds timeout when calling get()



<a href="https://try.boxlang.io/?code=eJxdjUEKwkAMRdfOKf5yBqEFxVWp0BN4iJJqwEbJJEgR795QXbkK%2FPf%2Fy%2BTmSuihLkNdZMzIBf0Z77RTCiY4demD0tiNJCAGWcDydMNf7xvucdj6XVKqfrdQT9uP5kqWcQyCto3LFcYzPdwyC%2BZa0kvZ6OIWmozfOjwr13wyHQ%3D%3D" target="_blank">Run Example</a>

```java
future = runAsync( () => {
	return 5;
} ).then( ( Any input ) => {
	return input + 2;
} );
result = future.get( 3 ); // 3 is timeout(in ms)
writeOutput( result );

```

Result: 5

### Run a function asynchronously with then() and error()




```java
future = runAsync( () => {
	return 5;
} ).then( ( Any input ) => {
	return input + 2;
} ).error( () => {
	return "Error occurred.";
} );
writeOutput( future.get() );

```

Result: 7

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxdjU0OgkAMhdfOKd5yiAmgLgkmnMBDaNFJpJCZNoQY727HceWufT%2FfG1U0EnpE5SFtfPXwFfozXm4XyTzGoe3cG1UtD2JzMfCGwIsK%2FoJF3ONYCp276bR4jGXC%2FkhJn2JjRarvJN7wZqFp8hESJEw0q%2FjAmFLl1hiELipG9vj1jZTz81fNnVPrPrwgPNQ%3D" target="_blank">Run Example</a>

```java
future = runAsync( () => {
	return 10;
} ).then( ( Any input ) => {
	return input + 20;
} );
dump( future );
result = future.get( 10 ); // 10 is timeout(in ms)
writeOutput( result );
 // output is 30

```



## Related

  * [AsyncAll](./AsyncAll.md)
  * [AsyncAllApply](./AsyncAllApply.md)
  * [AsyncAny](./AsyncAny.md)
  * [AsyncRun](./AsyncRun.md)
  * [ExecutorDelete](./ExecutorDelete.md)
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
  * [ThreadInterrupt](./ThreadInterrupt.md)
  * [ThreadJoin](./ThreadJoin.md)
  * [ThreadNew](./ThreadNew.md)
  * [ThreadTerminate](./ThreadTerminate.md)
