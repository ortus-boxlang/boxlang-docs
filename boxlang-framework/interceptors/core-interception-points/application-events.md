# Application Events

These events cover the full lifecycle of applications and requests in BoxLang. Most events are announced on **both** the application's local interceptor pool and the global interceptor pool. Exceptions are noted per event.

> **Dual-pool announcement:** Events marked "Local + Global" are announced first on the application's own interceptor pool (visible only to that application's registered interceptors), then on the global interceptor pool. Register on the global pool for cross-application listeners; register on the application pool for application-scoped listeners.

| Event Name                      | Cancellable | Pool           | Description                                                                        |
| ------------------------------- | :---------: | -------------- | ---------------------------------------------------------------------------------- |
| `beforeApplicationListenerLoad` |     No      | Global only    | Fired before the application listener is loaded and the application is defined.    |
| `afterApplicationListenerLoad`  |     No      | Global only    | Fired after the application listener is loaded and the application is defined.     |
| `onAbort`                       |     No      | Local + Global | Fired when a `bx:abort` tag or `abort()` call terminates the request.             |
| `onApplicationDefined`          |     No      | Global only    | Fired after the application settings have been processed for a request.            |
| `onApplicationEnd`              |     No      | Local only     | Fired when an application shuts down.                                              |
| `onApplicationRestart`          |     No      | Global only    | Fired when an application is explicitly restarted.                                 |
| `onApplicationStart`            |     No      | Local only     | Fired when an application starts for the first time.                               |
| `onClassRequest`                |     No      | Local + Global | Fired when a BoxLang class is requested directly (remote method invocation).       |
| `onError`                       |     No      | Local + Global | Fired when an unhandled exception occurs during a request.                         |
| `onMissingTemplate`             |     No      | Local + Global | Fired when a requested template file cannot be found.                              |
| `onRequest`                     |     No      | Local + Global | Fired for every incoming request, after `onRequestStart`.                          |
| `onRequestFlushBuffer`          |   **Yes**   | Global only    | Fired when the output buffer is flushed. Interceptors can modify the output.       |
| `onRequestEnd`                  |     No      | Local + Global | Fired at the end of every request.                                                 |
| `onRequestStart`                |     No      | Local + Global | Fired at the beginning of every request.                                           |
| `onSessionCreated`              |     No      | Local + Global | Fired when a new session is created.                                               |
| `onSessionDestroyed`            |     No      | Local + Global | Fired when a session is destroyed.                                                 |
| `onSessionEnd`                  |     No      | Local + Global | Fired when a session times out or is shut down.                                    |
| `onSessionStart`                |     No      | Local + Global | Fired when a session is started.                                                   |

* [`beforeApplicationListenerLoad`](application-events.md#beforeapplicationlistenerload)
* [`afterApplicationListenerLoad`](application-events.md#afterapplicationlistenerload)
* [`onAbort`](application-events.md#onabort)
* [`onApplicationDefined`](application-events.md#onapplicationdefined)
* [`onApplicationEnd`](application-events.md#onapplicationend)
* [`onApplicationRestart`](application-events.md#onapplicationrestart)
* [`onApplicationStart`](application-events.md#onapplicationstart)
* [`onClassRequest`](application-events.md#onclassrequest)
* [`onError`](application-events.md#onerror)
* [`onMissingTemplate`](application-events.md#onmissingtemplate)
* [`onRequest`](application-events.md#onrequest)
* [`onRequestFlushBuffer`](application-events.md#onrequestflushbuffer)
* [`onRequestEnd`](application-events.md#onrequestend)
* [`onRequestStart`](application-events.md#onrequeststart)
* [`onSessionCreated`](application-events.md#onsessioncreated)
* [`onSessionDestroyed`](application-events.md#onsessiondestroyed)
* [`onSessionEnd`](application-events.md#onsessionend)
* [`onSessionStart`](application-events.md#onsessionstart)

## beforeApplicationListenerLoad

Announced by the Application service before the application listener gets defined. This is a good place to do any type of processing that needs to be done before the application listener is loaded. Announced on the **global interceptor pool** only.

### Data Structure

| Data Key   | Type                      | Description                                              |
| ---------- | ------------------------- | -------------------------------------------------------- |
| `context`  | `IBoxContext`             | The BoxLang Request context                              |
| `listener` | `BaseApplicationListener` | The BoxLang listener class                               |
| `template` | `String`                  | The path to the `Application.bx` template, if found.    |

### Example

```groovy
class myListener{
	function beforeApplicationListenerLoad( struct data ){
		// This is where you can create  your own scopes or load your own caches
		// or more.
	}
}
```

## afterApplicationListenerLoad

Announced by the Application service after the application listener gets defined. This is a good place to do any type of processing that needs to be done after the application listener is loaded. This could include any custom frameworks or modules that need to be loaded after the application listener is loaded. The application scope, session management, datasources, and mappings are all in place at this point. Announced on the **global interceptor pool** only.

### Data Structure

| Data Key   | Type                      | Description                                              |
| ---------- | ------------------------- | -------------------------------------------------------- |
| `context`  | `IBoxContext`             | The BoxLang Request context                              |
| `listener` | `BaseApplicationListener` | The BoxLang listener class                               |
| `template` | `String`                  | The path to the `Application.bx` template, if any.      |

### Example

```groovy
class myListener{
	function afterApplicationListenerLoad( struct data ){
		// This is where you can create  your own scopes or load your own caches
		// or more.
	}
}
```

## onAbort

This event is triggered whenever an `abort` component is executed. Mirrors the `onAbort()` lifecycle method in `Application.bx`. Announced on both local and global pools.

### Data Structure

| Data Key      | Type                      | Description                                           |
| ------------- | ------------------------- | ----------------------------------------------------- |
| `args`        | `Object[]`                | Indexed arguments: `args[0]` is the aborted template. |
| `application` | `Application`             | The BoxLang Application class                         |
| `context`     | `IBoxContext`             | The BoxLang Request context                           |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class                            |

### `Args` Structure

| Index    | Type     | Description                      |
| -------- | -------- | -------------------------------- |
| `args[0]`| `String` | The target page that was aborted |

### Example

```groovy
class myListener{
	function onAbort( struct data ){
		var targetPage = data.args[ 1 ]; // 1-based index in BoxLang
	}
}
```

## onApplicationDefined

Fired once per request after the application's settings have been fully processed and applied to the context. This fires on every request but represents the point where the application is "known" for that request — application scope, class loaders, caches, schedulers, and session management are all set. Announced on the **global interceptor pool** only.

### Data Structure

| Data Key   | Type                      | Description                                         |
| ---------- | ------------------------- | --------------------------------------------------- |
| `context`  | `IBoxContext`             | The BoxLang Request context                         |
| `listener` | `BaseApplicationListener` | The BoxLang listener class                          |

### Example

```groovy
class myListener{
	function onApplicationDefined( struct data ){
		// This is where you can create  your own scopes or load your own caches
		// or more.
	}
}
```

## onApplicationEnd

This event is triggered when the application has timed out or is being shut down. It could also happen if the application is being reloaded or the server is being restarted or shut down. Announced on the **application's local interceptor pool** only.

### Data Structure

| Data Key      | Type                      | Description                                           |
| ------------- | ------------------------- | ----------------------------------------------------- |
| `args`        | `Object[]`                | Indexed arguments: `args[0]` is the application scope.|
| `application` | `Application`             | The BoxLang Application class                         |
| `context`     | `IBoxContext`             | The BoxLang Request context                           |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class                            |

### `Args` Structure

| Index    | Type               | Description           |
| -------- | ------------------ | --------------------- |
| `args[0]`| `ApplicationScope` | The application scope |

### Example

```groovy
class myListener{
	function onApplicationEnd( struct data ){
		// This is where you would do any cleanup
		// or save the application scope to a file
		var appScope = data.args[ 1 ]; // 1-based index in BoxLang
	}
}
```

## onApplicationRestart

This event is triggered when the application is restarted via the `ApplicationRestart()` BIF. Announced on the **global interceptor pool** only, before the restart sequence begins.

### Data Structure

| Data Key      | Type          | Description                                      |
| ------------- | ------------- | ------------------------------------------------ |
| `application` | `Application` | The BoxLang Application class                    |
| `context`     | `IBoxContext` | The BoxLang Request context                      |

### Example

```groovy
class myListener{
	function onApplicationRestart( struct data ){
		// This is where you would do any cleanup
		// or log restarts
	}
}
```

## onApplicationStart

This event is triggered when the application is started and it's guaranteed to be synchronized. This could be when the server is started or when the application is reloaded as well. Every time an application times out, this event will be triggered again upon startup. This is a great place to initialize your application. Announced on the **application's local interceptor pool** only.

### Data Structure

| Data Key      | Type                      | Description                                  |
| ------------- | ------------------------- | -------------------------------------------- |
| `args`        | `Object[]`                | Empty array — no arguments are passed.       |
| `application` | `Application`             | The BoxLang Application class                |
| `context`     | `IBoxContext`             | The BoxLang Request context                  |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class                   |

### `Args` Structure

_None_

### Example

```groovy
class myListener{
	function onApplicationStart( struct data ){

	}
}
```

## onClassRequest

This event is triggered whenever a class is being executed remotely via HTTP or any type of remote request. If you implement this event, you can intercept the request and do any type of processing before the class is executed. This is a great place to implement security checks or any type of processing that needs to be done before the class is executed. Announced on both local and global pools.

### Data Structure

| Data Key      | Type                      | Description                                                          |
| ------------- | ------------------------- | -------------------------------------------------------------------- |
| `args`        | `Object[]`                | Indexed arguments — see Args Structure below.                        |
| `application` | `Application`             | The BoxLang Application class                                        |
| `context`     | `IBoxContext`             | The BoxLang Request context                                          |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class                                           |

### `Args` Structure

| Index    | Type              | Description                                                   |
| -------- | ----------------- | ------------------------------------------------------------- |
| `args[0]`| `String`          | The name of the executing class                               |
| `args[1]`| `String`          | The name of the requested method                              |
| `args[2]`| `Struct`          | The parameters being passed to the requested executing method |
| `args[3]`| `IClassRunnable`  | The instance of the class being executed                      |

### Example

```groovy
class myListener{
	function onClassRequest( struct data ){
		// This is where you would do any security checks
		// or any type of processing that needs to be done
		// before the class is executed.

		// You can also call the class method here if you want
		// to execute it yourself.

		var result = data.args[ 4 ].invoke( data.args[ 2 ], data.args[ 3 ] ); // 1-based index in BoxLang

		return result;
	}
}
```

## onError

This event is triggered whenever an uncaught exception occurs anywhere in your application. This is a great place to log the error or send an email to the administrator. You can also use this event to display a custom error page or redirect the user to a different page. Announced on both local and global pools.

### Data Structure

| Data Key      | Type                      | Description                                           |
| ------------- | ------------------------- | ----------------------------------------------------- |
| `args`        | `Object[]`                | Indexed arguments — see Args Structure below.         |
| `application` | `Application`             | The BoxLang Application class                         |
| `context`     | `IBoxContext`             | The BoxLang Request context                           |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class                            |

### `Args` Structure

| Index    | Type        | Description                           |
| -------- | ----------- | ------------------------------------- |
| `args[0]`| `Throwable` | The caught exception                  |
| `args[1]`| `String`    | Additional info string (may be empty) |

### Example

```groovy
class myListener{
	function onError( struct data ){
		// This is where you would log the error
		// or send an email to the administrator.

		// You can also use this event to display a custom error page
		// or redirect the user to a different page.
		var exception = data.args[ 1 ]; // 1-based index in BoxLang

	}
}
```

## onMissingTemplate

This event is triggered whenever a template that's being requested for execution is not found. This is a great place to log the error or send an email to the administrator or handle it dynamically. Announced on both local and global pools.

### Data Structure

| Data Key      | Type                      | Description                                           |
| ------------- | ------------------------- | ----------------------------------------------------- |
| `args`        | `Object[]`                | Indexed arguments: `args[0]` is the missing template. |
| `application` | `Application`             | The BoxLang Application class                         |
| `context`     | `IBoxContext`             | The BoxLang Request context                           |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class                            |

### `Args` Structure

| Index    | Type     | Description                        |
| -------- | -------- | ---------------------------------- |
| `args[0]`| `String` | The target page that was not found |

### Example

```groovy
class myListener{
	function onMissingTemplate( struct data ){
		// This is where you would log the error
		// or send an email to the administrator.

		// You can also use this event to display a custom error page
		// or redirect the user to a different page.
		var targetPage = data.args[ 1 ]; // 1-based index in BoxLang
	}
}
```

## onRequest

This event is triggered whenever a request is being executed, right after the `onRequestStart` event. This is a great place to do any type of processing that needs to be done before the request is executed. Announced on both local and global pools.

### Data Structure

| Data Key      | Type                      | Description                                            |
| ------------- | ------------------------- | ------------------------------------------------------ |
| `args`        | `Object[]`                | Indexed arguments: `args[0]` is the requested template.|
| `application` | `Application`             | The BoxLang Application class                          |
| `context`     | `IBoxContext`             | The BoxLang Request context                            |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class                             |

### `Args` Structure

| Index    | Type     | Description                        |
| -------- | -------- | ---------------------------------- |
| `args[0]`| `String` | The target page that was requested |

### Example

```groovy
class myListener{
	function onRequest( struct data ){
		// This is where you would do any type of processing
		// that needs to be done before the request is executed.
		var targetPage = data.args[ 1 ]; // 1-based index in BoxLang
	}
}
```

## onRequestFlushBuffer

Whenever a context flushes the output buffer, this event is triggered. The `output` key is **mutable** — interceptors can modify the string before it is written out. This event is only announced when at least one listener is registered for it. Announced on the **global interceptor pool** only.

### Data Structure

| Data Key  | Type          | Description                                                                            |
| --------- | ------------- | -------------------------------------------------------------------------------------- |
| `context` | `IBoxContext` | The BoxLang Request context                                                            |
| `output`  | `String`      | The buffered output string about to be written. **Set this key to modify the output.** |

### Example

```groovy
class myListener{
	function onRequestFlushBuffer( struct data ){
		// This is where you would do any type of processing
		// that needs to be done before the request is executed.
		var output = data.output;
		// Transform, compress, or filter the output
		data.output = output.replace( "foo", "bar" );
	}
}
```

## onRequestEnd

This event is triggered once the request has been executed and the response is being sent back to the client. This is a great place to do any type of processing that needs to be done after the request is executed. Announced on both local and global pools.

### Data Structure

| Data Key      | Type                      | Description                                            |
| ------------- | ------------------------- | ------------------------------------------------------ |
| `args`        | `Object[]`                | Indexed arguments: `args[0]` is the requested template.|
| `application` | `Application`             | The BoxLang Application class                          |
| `context`     | `IBoxContext`             | The BoxLang Request context                            |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class                             |

### `Args` Structure

| Index    | Type     | Description                        |
| -------- | -------- | ---------------------------------- |
| `args[0]`| `String` | The target page that was requested |

### Example

```groovy
class myListener{
	function onRequestEnd( struct data ){
		// This is where you would do any type of processing
		// that needs to be done after the request is executed.

		// You can also use this event to display a custom error page
		// or redirect the user to a different page.
	}
}
```

## onRequestStart

This event is triggered at the beginning of the request, right before the `onClassRequest` event. This is a great place to do any type of processing that needs to be done before the request is executed. Announced on both local and global pools.

### Data Structure

| Data Key      | Type                      | Description                                            |
| ------------- | ------------------------- | ------------------------------------------------------ |
| `args`        | `Object[]`                | Indexed arguments: `args[0]` is the requested template.|
| `application` | `Application`             | The BoxLang Application class                          |
| `context`     | `IBoxContext`             | The BoxLang Request context                            |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class                             |

### `Args` Structure

| Index    | Type     | Description                        |
| -------- | -------- | ---------------------------------- |
| `args[0]`| `String` | The target page that was requested |

### Example

```groovy
class myListener{
	function onRequestStart( struct data ){
		// This is where you would do any type of processing
		// that needs to be done before the request is executed.

		var targetPage = data.args[ 1 ]; // 1-based index in BoxLang

		// You can also use this event to display a custom error page
		// or redirect the user to a different page.
	}
}
```

> **Execution order on session creation:** `onSessionCreated` → `onSessionStart`
>
> **Execution order on session expiry/removal:** `onSessionDestroyed` → `onSessionEnd`

## onSessionCreated

Fired immediately when a new `Session` object is constructed — before the `onSessionStart` lifecycle method runs. Announced on the **global interceptor pool** only. Use this for low-level session tracking, auditing, or pre-initialization.

### Data Structure

| Data Key      | Type          | Description                                              |
| ------------- | ------------- | -------------------------------------------------------- |
| `session`     | `Session`     | The newly created session object.                        |
| `application` | `Application` | The application instance this session belongs to.        |

### Example

```groovy
class myListener{
	function onSessionCreated( struct data ){
		// Track session creation, pre-seed session data, etc.
		var session = data.session;
		var application = data.application;
	}
}
```

## onSessionStart

This event is triggered when a new session is being started for the first time in a request. This mirrors the `onSessionStart()` method in `Application.bx`. The session is guaranteed to only start once — concurrent requests share a lock to ensure this fires exactly once per session, even under high concurrency. Announced on both local and global pools.

### Data Structure

| Data Key      | Type                      | Description                                                   |
| ------------- | ------------------------- | ------------------------------------------------------------- |
| `args`        | `Object[]`                | Indexed arguments: `args[0]` is the session ID.               |
| `application` | `Application`             | The BoxLang Application class                                 |
| `context`     | `IBoxContext`             | The BoxLang Request context                                   |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class                                    |

### `Args` Structure

| Index    | Type  | Description    |
| -------- | ----- | -------------- |
| `args[0]`| `Key` | The session ID |

### Example

```groovy
class myListener{
	function onSessionStart( struct data ){
		// This is where you would do any type of processing
		// that needs to be done before the session is started.

		var sessionId = data.args[ 1 ]; // 1-based index in BoxLang
	}
}
```

## onSessionEnd

This event is triggered when a session is ending — when it times out or is being shut down. This mirrors the `onSessionEnd()` method in `Application.bx`. The session scope is still accessible via `args` at this point. Announced on both local and global pools.

### Data Structure

| Data Key      | Type                      | Description                                                  |
| ------------- | ------------------------- | ------------------------------------------------------------ |
| `args`        | `Object[]`                | Indexed arguments — see Args Structure below.                |
| `application` | `Application`             | The BoxLang Application class                                |
| `context`     | `IBoxContext`             | A temporary request context created for the session shutdown |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class                                   |

### `Args` Structure

| Index    | Type               | Description                                 |
| -------- | ------------------ | ------------------------------------------- |
| `args[0]`| `SessionScope`     | The session scope being shut down           |
| `args[1]`| `ApplicationScope` | The application scope linked to the session |

### Example

```groovy
class myListener{
	function onSessionEnd( struct data ){
		// This is where you would do any cleanup
		// or save the session scope to a file
		// or do any type of processing that needs to be done
		// before the session is shutdown.
		var sessionScope = data.args[ 1 ];      // 1-based index in BoxLang
		var applicationScope = data.args[ 2 ];  // 1-based index in BoxLang
	}
}
```

## onSessionDestroyed

Fired just before a session is fully removed, after `onSessionEnd` has completed. Announced on the **global interceptor pool** only. Use this for final cleanup, metrics, or logging after the session lifecycle is fully complete.

### Data Structure

| Data Key      | Type                      | Description                                                            |
| ------------- | ------------------------- | ---------------------------------------------------------------------- |
| `session`     | `Session`                 | The session object being destroyed.                                    |
| `application` | `ApplicationScope`        | The application scope associated with the session being destroyed.     |
| `listener`    | `BaseApplicationListener` | The application listener associated with the session's application.    |

### Example

```groovy
class myListener{
	function onSessionDestroyed( struct data ){
		// Final cleanup, audit logging, metrics, etc.
		var session = data.session;
		var appScope = data.application;
	}
}
```
