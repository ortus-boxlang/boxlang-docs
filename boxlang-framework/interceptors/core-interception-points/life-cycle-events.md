# BIF & Component Lifecycle Events

These events fire during the instantiation and invocation of Built-In Functions (BIFs) and Components (`bx:*` tags). They are announced on the **global interceptor pool**.

> **Note:** `postBIFInvocation` is registered as a known event and its presence is checked before invocation, but the post-invocation code currently announces `onBIFInvocation` a second time instead. Until this is resolved, listen on `onBIFInvocation` and check whether `result` is present in the data to distinguish pre from post.

> **Note:** `onComponentInvocation` is defined in `BoxEvent` but is not currently announced anywhere in the runtime.

| Event Name                   | Cancellable | Description                                                                                          |
| ---------------------------- | :---------: | ---------------------------------------------------------------------------------------------------- |
| `onBIFInstance`              |     No      | Fired once when a BIF is instantiated for the first time (lazy, singleton per BIF).                 |
| `onBIFInvocation`            |   **Yes**   | Fired before a BIF executes. Also fired after execution with `result` added — interceptors can override the return value. |
| `postBIFInvocation`          |     —       | Defined but not currently announced. See note above.                                                 |
| `onComponentInstance`        |     No      | Fired once when a Component is instantiated for the first time (lazy, singleton per Component).      |
| `onCacheComponentAction`     |   **Yes**   | Fired when a `bx:cache` action is not natively handled. Interceptors can supply the result.          |
| `onFileComponentAction`      |   **Yes**   | Fired when a `bx:file` action is not natively handled. Interceptors can supply the response.         |
| `onCreateObjectRequest`      |   **Yes**   | Fired when `createObject()` is called with an unknown type. Interceptors can supply the object.      |
| `afterDynamicObjectCreation` |     No      | Fired after a Java object is instantiated via the dynamic interop service.                           |

* [`onBIFInstance`](life-cycle-events.md#onbifinstance)
* [`onBIFInvocation`](life-cycle-events.md#onbifinvocation)
* [`onComponentInstance`](life-cycle-events.md#oncomponentinstance)
* [`onCacheComponentAction`](life-cycle-events.md#oncachecomponentaction)
* [`onFileComponentAction`](life-cycle-events.md#onfilecomponentaction)
* [`onCreateObjectRequest`](life-cycle-events.md#oncreateobjectrequest)
* [`afterDynamicObjectCreation`](life-cycle-events.md#afterdynamicobjectcreation)

## onBIFInstance

Fired once — the first time a BIF is used and its singleton instance is created. BIF instances are created lazily and cached, so this fires at most once per BIF per runtime lifetime. Use this to decorate, wrap, or inspect BIF instances at startup.

### Data Structure

| Data Key     | Type            | Description                                        |
| ------------ | --------------- | -------------------------------------------------- |
| `instance`   | `BIF`           | The newly created BIF instance.                    |
| `name`       | `Key`           | The name of the BIF.                               |
| `descriptor` | `BIFDescriptor` | The descriptor that manages this BIF registration. |

### Example

```groovy
class myListener{
	function onBIFInstance( struct data ){
		var instance   = data.instance;
		var name       = data.name;
		var descriptor = data.descriptor;
	}
}
```

## onBIFInvocation

Fired **twice** per BIF call — once before execution (no `result` key) and once after (with `result` added if non-null). The same event data struct is reused for both calls.

- **Pre-invocation:** `result` is absent. Arguments can be inspected or mutated.
- **Post-invocation:** `result` is present (if the BIF returned a non-null value). Setting `result` in the data struct overrides the actual return value.

This event is only announced when at least one listener is registered for `onBIFInvocation` or `postBIFInvocation`, making it safe for high-throughput scenarios.

### Data Structure (pre-invocation)

| Data Key    | Type             | Description                                |
| ----------- | ---------------- | ------------------------------------------ |
| `context`   | `IBoxContext`    | The context in which the BIF is executing. |
| `arguments` | `ArgumentsScope` | The arguments passed to the BIF.           |
| `bif`       | `BIF`            | The BIF instance being invoked.            |
| `name`      | `Key`            | The name used to call the BIF.             |

### Data Structure (post-invocation, additional key)

| Data Key | Type     | Description                                                                      |
| -------- | -------- | -------------------------------------------------------------------------------- |
| `result` | `Object` | The return value of the BIF. Set this key to override the result returned to the caller. |

### Example

```groovy
class myListener{
	function onBIFInvocation( struct data ){
		var name   = data.name;
		var result = data.result ?: null; // null on pre-invocation

		if ( !isNull( result ) ) {
			// post-invocation — optionally override the result
			// data.result = myOverriddenValue;
		}
	}
}
```

## onComponentInstance

Fired once — the first time a Component (`bx:*` tag) is used and its singleton instance is created. Component instances are created lazily and cached. Use this to inspect or wrap Component instances at startup.

### Data Structure

| Data Key     | Type                  | Description                                              |
| ------------ | --------------------- | -------------------------------------------------------- |
| `instance`   | `Component`           | The newly created Component instance.                    |
| `name`       | `Key`                 | The name of the Component.                               |
| `descriptor` | `ComponentDescriptor` | The descriptor that manages this Component registration. |

### Example

```groovy
class myListener{
	function onComponentInstance( struct data ){
		var instance   = data.instance;
		var name       = data.name;
		var descriptor = data.descriptor;
	}
}
```

## onCacheComponentAction

Fired when a `bx:cache` component action is encountered that is not in the set of natively handled operations. This allows modules to extend the `bx:cache` component with custom actions. If no interceptor sets `result`, a `BoxRuntimeException` is thrown.

### Data Structure

| Data Key         | Type                      | Description                                                                       |
| ---------------- | ------------------------- | --------------------------------------------------------------------------------- |
| `component`      | `Cache`                   | The `bx:cache` component instance.                                                |
| `context`        | `IBoxContext`             | The context in which the component is executing.                                  |
| `attributes`     | `IStruct`                 | The attributes passed to the component tag.                                       |
| `body`           | `Component.ComponentBody` | The body of the component tag (if any).                                           |
| `executionState` | `IStruct`                 | The current execution state.                                                      |
| `result`         | `Object`                  | Initially `null`. Set this to provide a result and prevent the runtime exception. |

### Example

```groovy
class myListener{
	function onCacheComponentAction( struct data ){
		var action = data.attributes[ "action" ];

		if ( action == "myCustomAction" ) {
			data.result = "handled";
		}
	}
}
```

## onFileComponentAction

Fired when a `bx:file` component action is not natively supported by the runtime. Modules can intercept this event to handle custom or extended file actions. If no interceptor sets `response`, a `BoxRuntimeException` is thrown.

### Data Structure

| Data Key         | Type          | Description                                                                                       |
| ---------------- | ------------- | ------------------------------------------------------------------------------------------------- |
| `response`       | `Object`      | Initially `null`. Set this to provide the result. If a `variable` attribute is present on the tag, the response is assigned to that variable. |
| `context`        | `IBoxContext` | The context in which the component is executing.                                                  |
| `attributes`     | `IStruct`     | The attributes passed to the component tag.                                                       |
| `executionState` | `IStruct`     | The current execution state.                                                                      |

### Example

```groovy
class myListener{
	function onFileComponentAction( struct data ){
		var action = data.attributes[ "action" ];

		if ( action == "stream" ) {
			data.response = myStreamResult;
		}
	}
}
```

## onCreateObjectRequest

Fired when `createObject()` is called with a `type` that is not natively handled (`class`, `java`, or `webservice`). This is the extension point for modules to support new object creation types. If no interceptor sets `response` and no native handler matches, a `BoxRuntimeException` is thrown.

### Data Structure

| Data Key    | Type             | Description                                                                        |
| ----------- | ---------------- | ---------------------------------------------------------------------------------- |
| `response`  | `Object`         | Initially `null`. Set this to return the created object to the caller.             |
| `context`   | `IBoxContext`    | The context in which `createObject()` was called.                                  |
| `arguments` | `ArgumentsScope` | The full arguments passed to `createObject()`, including `type`, `className`, etc. |

### Example

```groovy
class myListener{
	function onCreateObjectRequest( struct data ){
		var type = data.arguments[ "type" ];

		if ( type == "myType" ) {
			data.response = new MyCustomObject();
		}
	}
}
```

## afterDynamicObjectCreation

Fired after a Java object is successfully instantiated via the BoxLang dynamic interop service (e.g., via `createObject("java", ...)` or any Java constructor call through the interop layer). Use this to post-process, wrap, or audit newly created Java objects.

### Data Structure

| Data Key | Type     | Description                             |
| -------- | -------- | --------------------------------------- |
| `object` | `Object` | The newly created Java object instance. |
| `clazz`  | `Class`  | The Java class that was instantiated.   |

### Example

```groovy
class myListener{
	function afterDynamicObjectCreation( struct data ){
		var object = data.object;
		var clazz  = data.clazz;
		// Wrap, proxy, or audit the new instance
	}
}
```
