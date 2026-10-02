---
description: Interception points announced when a BoxLang class instance is created and initialized
icon: cube
---

# Class Instance Events

These events fire when a BoxLang class is instantiated through `new`, `createObject()`, deserialization, or any other path that bootstraps a BoxLang class. They are announced on the **global interceptor pool** and are available starting in BoxLang **1.18.0**.

Use them for dependency injection, auditing, observability, and AOP-style decoration of class instances.

| Event Name              | Cancellable | Description                                                                                                  |
| ----------------------- | :---------: | ------------------------------------------------------------------------------------------------------------ |
| `afterBoxClassCreation` |     No      | The instance is fully defined (pseudo-constructor ran, interfaces and abstract methods validated) but `init()` has **not** run. |
| `afterBoxClassInit`     |     No      | `init()` (or the implicit constructor) has completed.                                                        |

* [`afterBoxClassCreation`](class-instance-events.md#afterboxclasscreation)
* [`afterBoxClassInit`](class-instance-events.md#afterboxclassinit)

{% hint style="info" %}
The data for these events is only built when at least one interceptor is listening, so they add no cost to class creation when unused.
{% endhint %}

## afterBoxClassCreation

Fired after the class instance is fully defined but **before** `init()` is called. The pseudo-constructor has run, and interfaces and abstract methods have been validated.

* It **also fires for `noInit` creations** such as `createObject()` and deserialization, where `init()` is never called. Check the `noInit` key to tell them apart.
* It **never fires for super classes** in an `extends` chain, only for the concrete instance being created.

### Data Structure

| Data Key    | Type            | Description                                                       |
| ----------- | --------------- | ----------------------------------------------------------------- |
| `instance`  | `IClassRunnable` | The BoxLang class instance.                                       |
| `className` | `String`        | The name of the class.                                            |
| `noInit`    | `Boolean`       | `true` when `init()` will be skipped for this instance.           |
| `context`   | `IBoxContext`   | The context the class is being created in.                        |

### Example

```js
class {

    function afterBoxClassCreation( data ) {
        // Inject a dependency before init() runs
        if ( data.className contains "Service" ) {
            data.instance.getVariablesScope().logger = getLogger()
        }
    }

}
```

## afterBoxClassInit

Fired after `init()` (or the implicit constructor) completes.

* It **does not fire** for `noInit` creations, since `init()` never runs.
* It **does not fire** when `init()` throws an exception.

### Data Structure

| Data Key    | Type            | Description                                                                                         |
| ----------- | --------------- | --------------------------------------------------------------------------------------------------- |
| `instance`  | `IClassRunnable` | The BoxLang class instance.                                                                         |
| `result`    | `Object`        | What construction returned: the instance, or whatever a non-null `init()` returned.                 |
| `className` | `String`        | The name of the class.                                                                              |
| `context`   | `IBoxContext`   | The context the class is being created in.                                                          |

### Example

```js
class {

    function afterBoxClassInit( data ) {
        writeLog( text="Created #data.className#", type="information" )
    }

}
```

{% hint style="warning" %}
These are announced on the global interceptor pool in the hot path of class instantiation. Keep handlers fast, and return early for classes you do not care about.
{% endhint %}
