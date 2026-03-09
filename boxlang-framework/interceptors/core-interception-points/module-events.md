# Module Events

These events are triggered around the lifecycle of BoxLang modules.

| Event Name                 | Data | Description                     |
| -------------------------- | :--: | ------------------------------- |
| `afterModuleRegistrations` |      | After all module registrations. |
| `preModuleRegistration`    |      | Before a module registration.   |
| `postModuleRegistration`   |      | After a module registration.    |
| `afterModuleActivations`   |      | After all module activations.   |
| `preModuleLoad`            |      | Before a module is loaded.      |
| `postModuleLoad`           |      | After a module is loaded.       |
| `preModuleUnload`          |      | Before a module is unloaded.    |
| `postModuleUnload`         |      | After a module is unloaded.     |

* [`beforeModuleLoad`](#beforemoduleload)
* [`afterModuleLoad`](#aftermoduleload)
* [`beforeModuleUnload`](#beforemoduleunload)
* [`afterModuleUnload`](#aftermoduleunload)
* [`onBeforeModuleRegistration`](#onbeforemoduleregistration)
* [`onAfterModuleRegistration`](#onaftermoduleregistration)
* [`onAfterModuleRegistrations`](#onaftermoduleregistrations)
* [`onAfterModuleActivations`](#onaftermoduleactivations)

---

## beforeModuleLoad

Announced by the Module Service before a module is loaded (activated). This event fires for each individual module before it is activated. This is a good place to do any type of processing that needs to be done before the module is loaded, such as dependency validation or resource preparation.

### Data Structure

| Data Key      | Type            | Description                      |
| ------------- | --------------- | -------------------------------- |
| `moduleRecord` | `ModuleRecord`  | The module being loaded          |
| `moduleName`   | `Key`           | The name/key of the module       |

### Example

```boxlang
class myListener {
	function beforeModuleLoad( struct data ) {
		var moduleName = data.moduleName.getName();
		var moduleRecord = data.moduleRecord;
		// Check dependencies or validate configuration before load
		if ( !moduleRecord.dependencies.isEmpty() ) {
			logger.info( "Module #moduleName# has dependencies: #moduleRecord.dependencies.toString()#" );
		}
	}
}
```

---

## afterModuleLoad

Announced by the Module Service after a module has been successfully loaded (activated). This event fires for each individual module after it has completed initialization and its `onLoad()` method has been called.

### Data Structure

| Data Key      | Type            | Description                      |
| ------------- | --------------- | -------------------------------- |
| `moduleRecord` | `ModuleRecord`  | The module that was loaded       |
| `moduleName`   | `Key`           | The name/key of the module       |

### `moduleRecord` Properties Available

| Property           | Type      | Description                      |
| ------------------ | --------- | -------------------------------- |
| `activationTime`   | `Long`    | Milliseconds to activate module  |
| `activatedOn`      | `Instant` | Timestamp of activation          |

### Example

```boxlang
class myListener {
	function afterModuleLoad( struct data ) {
		var moduleName = data.moduleName.getName();
		var timing = data.moduleRecord.activationTime;
		
		logger.info( "Module #moduleName# loaded in #timing# ms" );
		
		if ( timing > 5000 ) {
			logger.warn( "Slow module load detected: #timing# ms" );
		}
	}
}
```

---

## beforeModuleUnload

Announced by the Module Service before a module is unloaded (deactivated). This event fires for each individual module before it is deactivated. This is a good place to prepare for cleanup or save any module state before it is shut down.

### Data Structure

| Data Key      | Type            | Description                      |
| ------------- | --------------- | -------------------------------- |
| `moduleRecord` | `ModuleRecord`  | The module being unloaded        |
| `moduleName`   | `Key`           | The name/key of the module       |

### Example

```boxlang
class myListener {
	function beforeModuleUnload( struct data ) {
		var moduleName = data.moduleName.getName();
		logger.info( "Preparing to unload module: #moduleName#" );
		// Save state, close resources, etc.
	}
}
```

---

## afterModuleUnload

Announced by the Module Service after a module has been successfully unloaded (deactivated). This event fires for each individual module after it has completed shutdown and all resources have been released.

### Data Structure

| Data Key      | Type            | Description                      |
| ------------- | --------------- | -------------------------------- |
| `moduleRecord` | `ModuleRecord`  | The module that was unloaded     |
| `moduleName`   | `Key`           | The name/key of the module       |

### Example

```boxlang
class myListener {
	function afterModuleUnload( struct data ) {
		var moduleName = data.moduleName.getName();
		logger.info( "Module #moduleName# has been unloaded" );
		// Verify cleanup, reset caches, etc.
	}
}
```

---

## onBeforeModuleRegistration

Announced by the Module Service before a module is registered. This event fires for each individual module before its registration begins. This is a good place to validate module configuration or prevent registration if needed.

### Data Structure

| Data Key      | Type            | Description                      |
| ------------- | --------------- | -------------------------------- |
| `moduleRecord` | `ModuleRecord`  | The module being registered      |
| `moduleName`   | `Key`           | The name/key of the module       |

### Example

```boxlang
class myListener {
	function onBeforeModuleRegistration( struct data ) {
		var moduleName = data.moduleName.getName();
		var moduleRecord = data.moduleRecord;
		
		logger.info( "Pre-registering module: #moduleName#" );
		
		// Validate module is enabled
		if ( !moduleRecord.isEnabled() ) {
			logger.warn( "Module #moduleName# is disabled" );
		}
	}
}
```

---

## onAfterModuleRegistration

Announced by the Module Service after a module has been successfully registered. This event fires for each individual module after its registration is complete. At this point, the module's configuration is loaded and its services are registered.

### Data Structure

| Data Key      | Type            | Description                      |
| ------------- | --------------- | -------------------------------- |
| `moduleRecord` | `ModuleRecord`  | The module that was registered   |
| `moduleName`   | `Key`           | The name/key of the module       |

### `moduleRecord` Properties Available

| Property           | Type      | Description                      |
| ------------------ | --------- | -------------------------------- |
| `registrationTime` | `Long`    | Milliseconds to register module  |
| `registeredOn`     | `Instant` | Timestamp of registration        |

### Example

```boxlang
class myListener {
	function onAfterModuleRegistration( struct data ) {
		var moduleName = data.moduleName.getName();
		var timing = data.moduleRecord.registrationTime;
		
		logger.info( "Registered module: #moduleName# in #timing# ms" );
		logger.info( "Version: #data.moduleRecord.getVersion()#" );
		logger.info( "Author: #data.moduleRecord.getAuthor()#" );
	}
}
```

---

## onAfterModuleRegistrations

Announced by the Module Service after all modules have been registered. This event fires once after all individual module registrations are complete. This is a great place to perform module discovery or initialize cross-module dependencies.

### Data Structure

| Data Key        | Type                           | Description                      |
| --------------- | ------------------------------ | -------------------------------- |
| `moduleRegistry` | `Map<Key, ModuleRecord>`       | All registered modules in system |

### Example

```boxlang
class myListener {
	function onAfterModuleRegistrations( struct data ) {
		var modules = data.moduleRegistry;
		var moduleCount = modules.size();
		
		logger.info( "All modules registered: #moduleCount# modules" );
		
		// Log details of each module
		for ( var moduleName in modules ) {
			var module = modules[ moduleName ];
			logger.debug( "  - #module.getName()# @ #module.getVersion()#" );
		}
	}
}
```

---

## onAfterModuleActivations

Announced by the Module Service after all modules have been activated (loaded). This event fires once after all individual module activations are complete. This is a great place to perform cross-module initialization or startup tasks that depend on all modules being active.

### Data Structure

| Data Key        | Type                           | Description                      |
| --------------- | ------------------------------ | -------------------------------- |
| `moduleRegistry` | `Map<Key, ModuleRecord>`       | All activated modules in system  |

### Example

```boxlang
class myListener {
	function onAfterModuleActivations( struct data ) {
		var modules = data.moduleRegistry;
		var activeCount = 0;
		
		// Count active modules
		for ( var moduleName in modules ) {
			if ( modules[ moduleName ].isActivated() ) {
				activeCount++;
			}
		}
		
		logger.info( "Module activation complete: #activeCount# modules active" );
		
		// Perform cross-module initialization here
	}
}
```

---

## ModuleRecord Properties Reference

The `ModuleRecord` object available in all module events provides the following properties and methods:

### Identification

| Property | Type | Description |
|----------|------|-------------|
| `getName()` | `String` | Module name |
| `getVersion()` | `String` | Module version |
| `getAuthor()` | `String` | Module author |

### Status

| Property | Type | Description |
|----------|------|-------------|
| `isActivated()` | `Boolean` | Whether module is currently active |
| `isEnabled()` | `Boolean` | Whether module is enabled |

### Location

| Property | Type | Description |
|----------|------|-------------|
| `getPhysicalPath()` | `String` | Full file system path to module |

### Timing

| Property | Type | Description |
|----------|------|-------------|
| `registrationTime` | `Long` | Milliseconds to register (set in `onAfterModuleRegistration`) |
| `activationTime` | `Long` | Milliseconds to activate (set in `afterModuleLoad`) |
| `registeredOn` | `Instant` | Timestamp when registered |
| `activatedOn` | `Instant` | Timestamp when activated |

### Configuration

| Property | Type | Description |
|----------|------|-------------|
| `settings` | `Struct` | Module configuration settings |
| `dependencies` | `Array` | Array of dependent module names |
| `interceptors` | `Array` | Array of registered interceptors |
| `customInterceptionPoints` | `Array` | Array of custom event names |

---

## Context Variables Available in All Events

When implementing any module event listener, the following variables are automatically available in your function scope:

| Variable | Type | Description |
|----------|------|-------------|
| `logger` | `Logger` | Logger instance for this interceptor |
| `boxRuntime` | `BoxRuntime` | The BoxRuntime instance |
| `interceptorService` | `InterceptorService` | The InterceptorService instance |
| `properties` | `Struct` | Interceptor configuration properties |

---

## Event Execution Order

```
REGISTRATION PHASE
├── onBeforeModuleRegistration (Module 1)
├── [Module registers and loads configuration]
├── onAfterModuleRegistration (Module 1)
├── onBeforeModuleRegistration (Module 2)
├── [Module registers and loads configuration]
├── onAfterModuleRegistration (Module 2)
└── onAfterModuleRegistrations [ALL COMPLETE]

ACTIVATION PHASE
├── beforeModuleLoad (Module 1)
├── [Module initializes, onLoad() called]
├── afterModuleLoad (Module 1)
├── beforeModuleLoad (Module 2)
├── [Module initializes, onLoad() called]
├── afterModuleLoad (Module 2)
└── onAfterModuleActivations [ALL COMPLETE]

DEACTIVATION PHASE
├── beforeModuleUnload (Module 1)
├── [Module cleanup, onUnload() called]
├── afterModuleUnload (Module 1)
├── beforeModuleUnload (Module 2)
├── [Module cleanup, onUnload() called]
└── afterModuleUnload (Module 2)
```

---

## How to Register a Module Event Listener

Create an interceptor class and register it in your module's `ModuleConfig.bx`:

```boxlang
component {
	function configure() {
		settings = {
			name = "MyModule",
			version = "1.0.0"
		};
		
		// Register your event listener
		interceptors = [
			{ class="path.to.MyModuleListener", properties={} }
		];
	}
}
```

Then implement the events you need:

```boxlang
component displayname="MyModuleListener" {
	