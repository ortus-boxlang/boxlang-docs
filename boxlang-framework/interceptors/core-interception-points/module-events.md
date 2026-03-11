# Module Events

These events are triggered around the lifecycle of BoxLang modules. They are announced on the **global interceptor pool**.

> **Registration phase:** `onBeforeModuleRegistration` → `onAfterModuleRegistration` (per module) → `onAfterModuleRegistrations`
>
> **Activation phase:** `beforeModuleLoad` → `afterModuleLoad` (per module) → `onAfterModuleActivations`
>
> **Deactivation phase:** `beforeModuleUnload` → `afterModuleUnload` (per module)

| Event Name                    | Cancellable | Description                                        |
| ----------------------------- | :---------: | -------------------------------------------------- |
| `onBeforeModuleRegistration`  |     No      | Before an individual module is registered.         |
| `onAfterModuleRegistration`   |     No      | After an individual module is registered.          |
| `onAfterModuleRegistrations`  |     No      | After all modules have been registered.            |
| `beforeModuleLoad`            |     No      | Before an individual module is activated/loaded.   |
| `afterModuleLoad`             |     No      | After an individual module is activated/loaded.    |
| `onAfterModuleActivations`    |     No      | After all modules have been activated.             |
| `beforeModuleUnload`          |     No      | Before an individual module is deactivated.        |
| `afterModuleUnload`           |     No      | After an individual module is deactivated.         |

* [`onBeforeModuleRegistration`](#onbeforemoduleregistration)
* [`onAfterModuleRegistration`](#onaftermoduleregistration)
* [`onAfterModuleRegistrations`](#onaftermoduleregistrations)
* [`beforeModuleLoad`](#beforemoduleload)
* [`afterModuleLoad`](#aftermoduleload)
* [`onAfterModuleActivations`](#onaftermoduleactivations)
* [`beforeModuleUnload`](#beforemoduleunload)
* [`afterModuleUnload`](#aftermoduleunload)

## onBeforeModuleRegistration

Announced by the Module Service before a module is registered. This event fires for each individual module before its registration begins.

### Data Structure

| Data Key       | Type           | Description                  |
| -------------- | -------------- | ---------------------------- |
| `moduleRecord` | `ModuleRecord` | The module being registered. |
| `moduleName`   | `Key`          | The name/key of the module.  |

### Example

```groovy
class myListener{
	function onBeforeModuleRegistration( struct data ){
		var moduleName   = data.moduleName;
		var moduleRecord = data.moduleRecord;
	}
}
```

## onAfterModuleRegistration

Announced by the Module Service after a module has been successfully registered. At this point, the module's configuration is loaded and its services are registered.

### Data Structure

| Data Key       | Type           | Description                    |
| -------------- | -------------- | ------------------------------ |
| `moduleRecord` | `ModuleRecord` | The module that was registered.|
| `moduleName`   | `Key`          | The name/key of the module.    |

### Example

```groovy
class myListener{
	function onAfterModuleRegistration( struct data ){
		var moduleName   = data.moduleName;
		var moduleRecord = data.moduleRecord;
	}
}
```

## onAfterModuleRegistrations

Announced by the Module Service after all modules have been registered. This event fires once after all individual module registrations are complete.

### Data Structure

| Data Key        | Type                     | Description                       |
| --------------- | ------------------------ | --------------------------------- |
| `moduleRegistry`| `Map<Key, ModuleRecord>` | All registered modules in system. |

### Example

```groovy
class myListener{
	function onAfterModuleRegistrations( struct data ){
		var moduleRegistry = data.moduleRegistry;
	}
}
```

## beforeModuleLoad

Announced by the Module Service before a module is loaded (activated). This event fires for each individual module before it is activated.

### Data Structure

| Data Key       | Type           | Description                 |
| -------------- | -------------- | --------------------------- |
| `moduleRecord` | `ModuleRecord` | The module being loaded.    |
| `moduleName`   | `Key`          | The name/key of the module. |

### Example

```groovy
class myListener{
	function beforeModuleLoad( struct data ){
		var moduleName   = data.moduleName;
		var moduleRecord = data.moduleRecord;
	}
}
```

## afterModuleLoad

Announced by the Module Service after a module has been successfully loaded (activated). The module's `onLoad()` method has been called at this point.

### Data Structure

| Data Key       | Type           | Description                 |
| -------------- | -------------- | --------------------------- |
| `moduleRecord` | `ModuleRecord` | The module that was loaded. |
| `moduleName`   | `Key`          | The name/key of the module. |

### Example

```groovy
class myListener{
	function afterModuleLoad( struct data ){
		var moduleName   = data.moduleName;
		var moduleRecord = data.moduleRecord;
	}
}
```

## onAfterModuleActivations

Announced by the Module Service after all modules have been activated (loaded). This event fires once after all individual module activations are complete.

### Data Structure

| Data Key        | Type                     | Description                      |
| --------------- | ------------------------ | -------------------------------- |
| `moduleRegistry`| `Map<Key, ModuleRecord>` | All activated modules in system. |

### Example

```groovy
class myListener{
	function onAfterModuleActivations( struct data ){
		var moduleRegistry = data.moduleRegistry;
	}
}
```

## beforeModuleUnload

Announced by the Module Service before a module is unloaded (deactivated). This event fires for each individual module before it is deactivated.

### Data Structure

| Data Key       | Type           | Description                   |
| -------------- | -------------- | ----------------------------- |
| `moduleRecord` | `ModuleRecord` | The module being unloaded.    |
| `moduleName`   | `Key`          | The name/key of the module.   |

### Example

```groovy
class myListener{
	function beforeModuleUnload( struct data ){
		var moduleName   = data.moduleName;
		var moduleRecord = data.moduleRecord;
	}
}
```

## afterModuleUnload

Announced by the Module Service after a module has been successfully unloaded (deactivated). All resources have been released at this point.

### Data Structure

| Data Key       | Type           | Description                    |
| -------------- | -------------- | ------------------------------ |
| `moduleRecord` | `ModuleRecord` | The module that was unloaded.  |
| `moduleName`   | `Key`          | The name/key of the module.    |

### Example

```groovy
class myListener{
	function afterModuleUnload( struct data ){
		var moduleName   = data.moduleName;
		var moduleRecord = data.moduleRecord;
	}
}
```
