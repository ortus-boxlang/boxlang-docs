---
description: Request interception points are announced by the Application.bx listener
icon: reel
---

# Request Interception Points

The following interception points are announced on every request by the `Application.bx` listeners.  Please note that to listen to these request events, your listener must also be registered for every request.

## Registration

Our advice is to register your listener in either the `onApplicationStart()` or `onRequestStart()` methods of the `Application.bx`.  You will use the `boxRegisterRequestInterceptor()` BIF in order to register them.

```groovy
class{

    function onApplicationStart(){
        boxRegisterRequestInterceptor( classOrLambda )
    }
    
    function onRequestStart( required string targetPage ){
        boxRegisterRequestInterceptor( classOrLambda )
    }

}
```

## Interception Points

These events occur around the life cycle of the request listener `Application.bx`:

* `onAbort`
* `onApplicationEnd`
* `onApplicationStart`
* `onClassRequest`
* `onError`
* `onMissingTemplate`
* `onRequest`
* `onRequestEnd`
* `onRequestStart`
* `onSessionEnd`
* `onSessionStart`



### onAbort

This event is triggered whenever an `abort` component is executed.

| Data Key   | Type   | Description               |
| ---------- | ------ | ------------------------- |
| targetPage | String | The target page executing |

#### Example

```groovy
class myListener{
	function onAbort( struct data ){

	}
}
```

### onApplicationEnd

This event is triggered

| Data Key          | Type       | Description                               |
| ----------------- | ---------- | ----------------------------------------- |
| DatasourceService | Java class | Instance of the BoxLang DatasourceService |

#### Example

```groovy
class myListener{
	function onApplicationEnd( struct data ){

	}
}
```

### onApplicationStart

This event is triggered

| Data Key          | Type       | Description                               |
| ----------------- | ---------- | ----------------------------------------- |
| DatasourceService | Java class | Instance of the BoxLang DatasourceService |

#### Example

```groovy
class myListener{
	function onApplicationStart( struct data ){

	}
}
```

### onClassRequest

This event is triggered

| Data Key          | Type       | Description                               |
| ----------------- | ---------- | ----------------------------------------- |
| DatasourceService | Java class | Instance of the BoxLang DatasourceService |

#### Example

```groovy
class myListener{
	function onClassRequest( struct data ){

	}
}
```

### onError

This event is triggered

| Data Key          | Type       | Description                               |
| ----------------- | ---------- | ----------------------------------------- |
| DatasourceService | Java class | Instance of the BoxLang DatasourceService |

#### Example

```groovy
class myListener{
	function onError( struct data ){

	}
}
```

### onMissingTemplate

This event is triggered

| Data Key          | Type       | Description                               |
| ----------------- | ---------- | ----------------------------------------- |
| DatasourceService | Java class | Instance of the BoxLang DatasourceService |

#### Example

```groovy
class myListener{
	function onMissingTemplate( struct data ){

	}
}
```

### onRequest

This event is triggered

| Data Key          | Type       | Description                               |
| ----------------- | ---------- | ----------------------------------------- |
| DatasourceService | Java class | Instance of the BoxLang DatasourceService |

#### Example

```groovy
class myListener{
	function onRequest( struct data ){

	}
}
```

### onRequestEnd

This event is triggered

| Data Key          | Type       | Description                               |
| ----------------- | ---------- | ----------------------------------------- |
| DatasourceService | Java class | Instance of the BoxLang DatasourceService |

#### Example

```groovy
class myListener{
	function onRequestEnd( struct data ){

	}
}
```

### onRequestStart

This event is triggered

| Data Key          | Type       | Description                               |
| ----------------- | ---------- | ----------------------------------------- |
| DatasourceService | Java class | Instance of the BoxLang DatasourceService |

#### Example

```groovy
class myListener{
	function onRequestStart( struct data ){

	}
}
```

### onSessionEnd

This event is triggered

| Data Key          | Type       | Description                               |
| ----------------- | ---------- | ----------------------------------------- |
| DatasourceService | Java class | Instance of the BoxLang DatasourceService |

#### Example

```groovy
class myListener{
	function onSessionEnd( struct data ){

	}
}
```

### onSessionStart

This event is triggered

| Data Key          | Type       | Description                               |
| ----------------- | ---------- | ----------------------------------------- |
| DatasourceService | Java class | Instance of the BoxLang DatasourceService |

#### Example

```groovy
class myListener{
	function onSessionStart( struct data ){

	}
}
```

