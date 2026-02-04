# Function Invocations

These events occur when a function is about to be executed or has finished executing.

* [`preFunctionInvoke`](function-invocations.md#prefunctioninvoke) - This event is triggered before a function is invoked.
* [`postFunctionInvoke`](function-invocations.md#postfunctioninvoke) - This event is triggered after a function has been invoked.
* [`onFunctionException`](function-invocations.md#onfunctionexception) - This event is triggered when an exception occurs during the function invocation.

## preFunctionInvoke

This event is triggered before a function is invoked. It allows you to perform actions or modifications before the function execution begins.

### Data Structure

| Data Key    | Type             | Description                             |
| ----------- | ---------------- | --------------------------------------- |
| `arguments` | `ArgumentsScope` | The arguments scope                     |
| `context`   | `IBoxContext`    | The BoxLang Request context             |
| `function`  | `Function`       | The UDF/Function/Closure/Lambda invoked |
| `name`      | `String`         | The name of the function invoked        |

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

This event is triggered after a function has been invoked. It allows you to perform actions or modifications after the function execution has completed.

### Data Structure

| Data Key    | Type             | Description                             |
| ----------- | ---------------- | --------------------------------------- |
| `arguments` | `ArgumentsScope` | The arguments scope                     |
| `context`   | `IBoxContext`    | The BoxLang Request context             |
| `function`  | `Function`       | The UDF/Function/Closure/Lambda invoked |
| `name`      | `String`         | The name of the function invoked        |
| `result`    | `Any`            | The result of the function call         |

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

This event is triggered when an exception occurs during the function invocation. It allows you to handle exceptions gracefully.

### Data Structure

| Data Key    | Type             | Description                                                |
| ----------- | ---------------- | ---------------------------------------------------------- |
| `arguments` | `ArgumentsScope` | The arguments scope                                        |
| `context`   | `IBoxContext`    | The BoxLang Request context                                |
| `function`  | `Function`       | The UDF/Function/Closure/Lambda invoked                    |
| `name`      | `String`         | The name of the function invoked                           |
| `exception` | `Exception`      | The exception that occurred during the function invocation |

### Example

```groovy
class myListener{
	function onFunctionException( struct data ){
		// Access the function name
		var functionName = data.name;
		
		// Log the exception
		log.error("Exception in function: " & functionName & ", Message: " & data.exception.message);
		
		// You can handle the exception or modify the response if needed
		data.exception.message = "Custom error message";
	}
}
```
