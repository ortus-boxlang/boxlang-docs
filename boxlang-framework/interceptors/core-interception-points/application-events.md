# Application Events

These events occur around the life cycle of the request listener `Application.bx`:

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

Announced by the Application service before the application listener gets defined.  This is a good place to do any type of processing that needs to be done before the application listener is loaded.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |
| `template`    | `URI` | The URI of the template matching the Application.bx       |

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

Announced by the Application service after the application listener gets defined.  This is a good place to do any type of processing that needs to be done after the application listener is loaded. This could include
any custom frameworks or modules that need to be loaded after the application listener is loaded.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |
| `template`    | `URI` | The URI of the template matching the Application.bx       |

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

This event is triggered whenever an `abort` component is executed.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `args`        | `struct`                  | The arguments relating the event |
| `application` | `Application`             | The BoxLang Application class    |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |

### `Args` Structure

| Args Key     | Type     | Description                      |
| ------------ | -------- | -------------------------------- |
| `targetPage` | `string` | The target page that was aborted |

### Example

```groovy
class myListener{
	function onAbort( struct data ){

	}
}
```

## onApplicationDefined

This happens when the application is defined and the following has been set:

* Aplication scope
* Class loaders
* Caches
* Schedulers
* Session Management

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |

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

This event is triggered when the application has timed out or is being shut down. It could also happen if the application is being reloaded or the server is being restarted or shut down.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `args`        | `struct`                  | The arguments relating the event |
| `application` | `Application`             | The BoxLang Application class    |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |

### `Args` Structure

| Args Key           | Type     | Description           |
| ------------------ | -------- | --------------------- |
| `applicationScope` | `struct` | The application scope |

### Example

```groovy
class myListener{
	function onApplicationEnd( struct data ){
		// This is where you would do any cleanup
		// or save the application scope to a file
	}
}
```

## onApplicationRestart

This event is triggered when the application is restarted via the `ApplicationRestart()` BIF.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `application` | `Application`             | The BoxLang Application class    |
| `context`     | `IBoxContext`             | The BoxLang Request context      |

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

This event is triggered when the application is started and it's guaranteed to be synchronized. This could be when the server is started or when the application is reloaded as well. Every time an application times out, this event will be triggered again upon startup. This is a great place to initialize your application.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `args`        | `struct`                  | The arguments relating the event |
| `application` | `Application`             | The BoxLang Application class    |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |

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

This event is triggered whenever a class is being executed remotely via HTTP or any type of remote request. If you implement this event, you can intercept the request and do any type of processing before the class is executed. This is a great place to implement security checks or any type of processing that needs to be done before the class is executed.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `args`        | `struct`                  | The arguments relating the event |
| `application` | `Application`             | The BoxLang Application class    |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |

### `Args` Structure

| Args Key        | Type     | Description                                                   |
| --------------- | -------- | ------------------------------------------------------------- |
| `className`     | `string` | The name of the executing class                               |
| `methodName`    | `string` | The name of the requested method                              |
| `params`        | `struct` | The parameters being passed to the requested executing method |
| `classInstance` | `object` | The instance of the class being executed                      |

### Example

```groovy
class myListener{
	function onClassRequest( struct data ){
		// This is where you would do any security checks
		// or any type of processing that needs to be done
		// before the class is executed.
		
		// You can also call the class method here if you want
		// to execute it yourself.
		
		var result = data.classInstance.invoke( data.methodName, data.params );
		
		return result;	
	}
}
```

## onError

This event is triggered whenever an uncaught exception occurs anywhere in your application. This is a great place to log the error or send an email to the administrator. You can also use this event to display a custom error page or redirect the user to a different page.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `args`        | `struct`                  | The arguments relating the event |
| `application` | `Application`             | The BoxLang Application class    |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |

### `Args` Structure

| Args Key    | Type        | Description          |
| ----------- | ----------- | -------------------- |
| `exception` | `Throwable` | The caugth exception |

### Example

```groovy
class myListener{
	function onError( struct data ){
		// This is where you would log the error
		// or send an email to the administrator.
		
		// You can also use this event to display a custom error page
		// or redirect the user to a different page.
		var exception = data.args.exception;
		
	}
}
```

## onMissingTemplate

This event is triggered whenever a template that's being requested for execution is not found. This is a great place to log the error or send an email to the administrator or handle it dynamically.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `args`        | `struct`                  | The arguments relating the event |
| `application` | `Application`             | The BoxLang Application class    |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |

### `Args` Structure

| Args Key     | Type     | Description                        |
| ------------ | -------- | ---------------------------------- |
| `targetPage` | `string` | The target page that was not found |

### Example

```groovy
class myListener{
	function onMissingTemplate( struct data ){
		// This is where you would log the error
		// or send an email to the administrator.
		
		// You can also use this event to display a custom error page
		// or redirect the user to a different page.
		var targetPage = data.args.targetPage;
	}
}
```

## onRequest

This event is triggered whenever a request is being executed, right after the `onRequestStart, onClassRequest` events. This is a great place to do any type of processing that needs to be done before the request is executed.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `args`        | `struct`                  | The arguments relating the event |
| `application` | `Application`             | The BoxLang Application class    |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |

### `Args` Structure

| Args Key     | Type     | Description                        |
| ------------ | -------- | ---------------------------------- |
| `targetPage` | `string` | The target page that was requested |

### Example

```groovy
class myListener{
	function onRequest( struct data ){
		// This is where you would do any type of processing
		// that needs to be done before the request is executed.
		var targetPage = data.args.targetPage;
	}
}
```

## onRequestFlushBuffer

Whenever a context flushes the output buffer, this event is triggered. This is a great place to do any type of processing that needs to be done before the request is executed or transform the output buffer.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `output`    | `String` | The output to be flushed       |

### Example

```groovy
class myListener{
	function onRequestFlushBuffer( struct data ){
		// This is where you would do any type of processing
		// that needs to be done before the request is executed.
		var output = data.output;
	}
}
```

## onRequestEnd

This event is triggered once the request has been executed and the response is being sent back to the client. This is a great place to do any type of processing that needs to be done after the request is executed.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `args`        | `struct`                  | The arguments relating the event |
| `application` | `Application`             | The BoxLang Application class    |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |

### `Args` Structure

_None_

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

This event is triggered at the beginning of the request, right before the `onClassRequest` event. This is a great place to do any type of processing that needs to be done before the request is executed.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `args`        | `struct`                  | The arguments relating the event |
| `application` | `Application`             | The BoxLang Application class    |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |

### `Args` Structure

| Args Key     | Type     | Description                        |
| ------------ | -------- | ---------------------------------- |
| `targetPage` | `string` | The target page that was requested |

### Example

```groovy
class myListener{
	function onRequestStart( struct data ){
		// This is where you would do any type of processing
		// that needs to be done before the request is executed.
		
		var targetPage = data.args.targetPage;
		
		// You can also use this event to display a custom error page
		// or redirect the user to a different page.
	}
}
```

## onSessionEnd

This event is triggered when the session has timed out or is being shut down.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `args`        | `struct`                  | The arguments relating the event |
| `application` | `Application`             | The BoxLang Application class    |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |

### `Args` Structure

| Args Key           | Type     | Description                                 |
| ------------------ | -------- | ------------------------------------------- |
| `sessionScope`     | `struct` | The session scope being shutdown            |
| `applicationScope` | `struct` | The application scope linked to the session |

### Example

```groovy
class myListener{
	function onSessionEnd( struct data ){
		// This is where you would do any cleanup
		// or save the session scope to a file
		// or do any type of processing that needs to be done
		// before the session is shutdown.
		var sessionScope = data.args.sessionScope;
		var applicationScope = data.args.applicationScope;
	}
}
```

## onSessionStart

This event is triggered when the session is started. This is a great place to initialize your session or do any type of processing that needs to be done before the session is started.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `args`        | `struct`                  | The arguments relating the event |
| `application` | `Application`             | The BoxLang Application class    |
| `context`     | `IBoxContext`             | The BoxLang Request context      |
| `listener`    | `BaseApplicationListener` | The BoxLang listener class       |

### `Args` Structure

| Args Key    | Type     | Description            |
| ----------- | -------- | ---------------------- |
| `sessionID` | `string` | The session identifier |

### Example

```groovy
class myListener{
	function onSessionStart( struct data ){
		// This is where you would do any type of processing
		// that needs to be done before the session is started.
		
		var sessionID = data.args.sessionID;
		
		// You can also use this event to display a custom error page
		// or redirect the user to a different page.
	}
}
```

## onSessionDestroyed

This is when a session get's destroyed. This could be when the session times out or when the session is being destroyed manually. This is a great place to do any type of processing that needs to be done before the session is destroyed.

### Data Structure

| Data Key      | Type                      | Description                      |
| ------------- | ------------------------- | -------------------------------- |
| `application` | `Application`             | The BoxLang Application class    |
| `listner`     | `Listener`             | The BoxLang Listener class      |
| `session`     | `Session`             | The BoxLang Session class      |

### Example

```groovy
class myListener{
	function onSessionDestroyed( struct data ){
		// This is where you would do any type of processing
		// that needs to be done before the session is started.
		
		var sessionID = data.args.sessionID;
		
		// You can also use this event to display a custom error page
		// or redirect the user to a different page.
	}
}
```
