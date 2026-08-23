# Function Invocations

These events occur when a user-defined function is about to be executed or has finished executing. They are announced on the **global interceptor pool**.

> **Performance guard:** `preFunctionInvoke`, `postFunctionInvoke`, and `onFunctionException` are only announced when at least one listener is registered for any of the three events. If no listeners exist, this code path is skipped entirely. Keep function interceptors lightweight as they fire on every user-defined function call.

| Event Name            | Cancellable | Description                                                                                      |
| --------------------- | :---------: | ------------------------------------------------------------------------------------------------ |
| `preFunctionInvoke`   |     No      | Fired before a user-defined function executes.                                                   |
| `postFunctionInvoke`  |   **Yes**   | Fired after a function returns successfully. Interceptors can override the return value.         |
| `onFunctionException` |     No      | Fired when a function throws an exception. The exception is re-thrown after the event completes. |

* [`preFunctionInvoke`](function-invocations.md#prefunctioninvoke) - This event is triggered before a function is invoked.
* [`postFunctionInvoke`](function-invocations.md#postfunctioninvoke) - This event is triggered after a function has been invoked.
* [`onFunctionException`](function-invocations.md#onfunctionexception) - This event is triggered when an exception occurs during the function invocation.

## preFunctionInvoke

This event is triggered before a function is invoked. It allows you to perform actions or modifications before the function execution begins. The arguments scope has already been created and populated at this point, so arguments can be inspected or mutated before the function body runs.

### Data Structure

| Data Key    | Type                 | Description                             |
| ----------- | -------------------- | --------------------------------------- |
| `arguments` | `ArgumentsScope`     | The arguments scope                     |
| `context`   | `FunctionBoxContext` | The function-specific context           |
| `function`  | `Function`           | The UDF/Function/Closure/Lambda invoked |
| `name`      | `String`             | The name of the function invoked        |

### Example

```groovy
class myListener{

	function preFunctionInvoke( struct data ){
		// Access the function name
		var functionName = data.name;

		// Log the function invocation
		log.info("Function invoked: " & functionName);

		// You can modify arguments if needed
		data.arguments.set("newArg", "value");
	}
}
```

## postFunctionInvoke

This event is triggered after a function has returned **successfully**. Does not fire if the function threw an exception — use `onFunctionException` for that. The same event data struct from `preFunctionInvoke` is reused with `result` added.

The `result` key is **mutable** — setting it in the event data overrides the value returned to the caller.

### Data Structure

| Data Key    | Type                 | Description                                                                              |
| ----------- | -------------------- | ---------------------------------------------------------------------------------------- |
| `arguments` | `ArgumentsScope`     | The arguments scope                                                                      |
| `context`   | `FunctionBoxContext` | The function-specific context                                                            |
| `function`  | `Function`           | The UDF/Function/Closure/Lambda invoked                                                  |
| `name`      | `String`             | The name of the function invoked                                                         |
| `result`    | `Any`                | The return value of the function (absent if the function returned `null`). **Set this key to override the return value.** |

### Example

```groovy
class myListener{
	function postFunctionInvoke( struct data ){
		// Access the function name
		var functionName = data.name;

		// Log the function invocation result
		log.info("Function invoked: " & functionName & ", Result: " & data.result);

		// You can modify the result if needed
		data.result = "Modified Result";
	}
}
```

## onFunctionException

This event is triggered when an exception occurs during the function invocation. The exception is **not suppressed** — it is re-thrown after the event completes. The same event data struct from `preFunctionInvoke` is reused with `exception` added.

### Data Structure

| Data Key    | Type                 | Description                                                |
| ----------- | -------------------- | ---------------------------------------------------------- |
| `arguments` | `ArgumentsScope`     | The arguments scope                                        |
| `context`   | `FunctionBoxContext` | The function-specific context                              |
| `function`  | `Function`           | The UDF/Function/Closure/Lambda invoked                    |
| `name`      | `String`             | The name of the function invoked                           |
| `exception` | `Throwable`          | The exception that occurred during the function invocation |

### Example

```groovy
class myListener{
	function onFunctionException( struct data ){
		// Access the function name
		var functionName = data.name;

		// Log the exception
		log.error("Exception in function: " & functionName & ", Message: " & data.exception.message);

		// Note: the exception will still be thrown after this event completes.
	}
}
```
