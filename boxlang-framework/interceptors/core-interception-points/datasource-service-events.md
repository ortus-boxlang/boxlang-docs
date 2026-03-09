# Datasource Service Events

These events occur around the lifecycle of datasources and the datasource service.

* [`onDatasourceServiceStartup`](#onDatasourceServiceStartup)
* [`onDatasourceServiceShutdown`](#onDatasourceServiceShutdown)
* [`onDatasourceStartup`](#onDatasourceStartup)
* [`onDatasourceConfigLoad`](#onDatasourceConfigLoad)

## onDatasourceServiceStartup

This event is triggered immediately after the datasource service has started. You could use this event to register custom datasources after the service has started, for example. 

| Data Key          | Type           | Description                               |
| ----------------- | -------------- | ----------------------------------------- |
| DatasourceService | Java class     | Instance of the BoxLang DatasourceService |

### Example

```js
class myDatasourceListener {
    function onDatasourceServiceStartup( struct data ) {
        println("Datasource service is starting up");
        println( data.datasourceService.getNames() );
    }
}
```

## onDatasourceServiceShutdown

This event is triggered immediately prior to datasource service shutdown. You could use this event to perform any cleanup on custom datasources, for example.

| Data Key          | Type           | Description                               |
| ----------------- | -------------- | ----------------------------------------- |
| DatasourceService | Java class     | Instance of the BoxLang DatasourceService |

### Example

```js
class myDatasourceListener {
    function onDatasourceServiceShutdown( struct data ) {
        println("Datasource service is shutting down");
        println( data.datasourceService.getNames() );
    }
}
```


## onDatasourceStartup

This event is triggered immediately prior to datasource startup. You can listen to this event to perform any last-minute configuration tweaks on the datasource before it is started.

| Data Key          | Type           | Description                                                                                           |
| ----------------- | -------------- | ----------------------------------------------------------------------------------------------------- |
| `name`            | String         | Datasource name                                                                                       |
| `properties`      | Struct         | Datasource configuration properties                                                                   |
| `config`          | Java class     | Instance of the DatasourceConfig class, which stores all configuration for this datasource.           |

### Example

```js
class myDatasourceListener {
    function onDatasourceStartup( struct data ) {
        println("Datasource [#data.name#] is starting up!");
        println( data.properties );
    }
}
```

## onDatasourceConfigLoad

This event is triggered immediately prior to datasource configuration load. You can use this event to modify the datasource configuration prior to processing

| Data Key          | Type           | Description                                                                                           |
| ----------------- | -------------- | ----------------------------------------------------------------------------------------------------- |
| `name`            | String         | Datasource name                                                                                       |
| `properties`      | Struct         | Datasource configuration properties                                                                   |

### Example

```js
class myDatasourceListener {
    function onDatasourceConfigLoad( struct data ) {
        println("Datasource [#data.name#] is configuring!");
        println( data.properties );
    }
}
```
# Datasource Service Events

These events occur around the lifecycle of datasources and the datasource service.

* [`onDatasourceServiceStartup`](#ondatasourceservicestartup)
* [`onDatasourceServiceShutdown`](#ondatasourceserviceshutdown)
* [`onDatasourceStartup`](#ondatasourcestartup)
* [`onDatasourceConfigLoad`](#ondatasourceconfigload)

---

## onDatasourceServiceStartup

This event is triggered immediately after the datasource service has started up and is ready to manage datasources. This is a good place to register custom datasources, configure datasource defaults, or initialize datasource-related resources.

### Data Structure

| Data Key              | Type                    | Description                               |
| -------------------- | ----------------------- | ----------------------------------------- |
| `datasourceService`   | `DatasourceService`     | Instance of the BoxLang DatasourceService |

### Example

```boxlang
class myDatasourceListener {
	function onDatasourceServiceStartup( struct data ) {
		var datasourceService = data.datasourceService;
		
		logger.info( "Datasource service is starting up" );
		logger.debug( "Available datasources: #datasourceService.getNames().toString()#" );
		
		// You could register custom datasources here
		// or perform initialization tasks
	}
}
```

---

## onDatasourceServiceShutdown

This event is triggered immediately prior to datasource service shutdown. This is a good place to perform cleanup on custom datasources, save state, close connections, or release any resources that were allocated during service operation.

### Data Structure

| Data Key              | Type                    | Description                               |
| -------------------- | ----------------------- | ----------------------------------------- |
| `datasourceService`   | `DatasourceService`     | Instance of the BoxLang DatasourceService |

### Example

```boxlang
class myDatasourceListener {
	function onDatasourceServiceShutdown( struct data ) {
		var datasourceService = data.datasourceService;
		var datasources = datasourceService.getNames();
		
		logger.info( "Datasource service is shutting down" );
		logger.debug( "Closing #datasources.size()# datasources" );
		
		// Perform cleanup on custom datasources
		for ( var dsName in datasources ) {
			logger.debug( "Shutting down datasource: #dsName#" );
		}
	}
}
```

---

## onDatasourceStartup

This event is triggered immediately before an individual datasource is started. This is a good place to perform last-minute configuration tweaks on the datasource, validate settings, or initialize datasource-specific resources before it becomes available for queries.

### Data Structure

| Data Key     | Type           | Description                                                                           |
| ------------ | -------------- | ------------------------------------------------------------------------------------- |
| `name`       | `String`       | The datasource name                                                                   |
| `properties` | `Struct`       | Datasource configuration properties                                                   |
| `config`     | `DatasourceConfig` | Instance of the DatasourceConfig class storing all datasource configuration           |

### `properties` Structure

| Property Key       | Type      | Description                                          |
| ------------------ | --------- | ---------------------------------------------------- |
| `driver`           | `String`  | The JDBC driver class name                           |
| `url`              | `String`  | The database connection URL                          |
| `username`         | `String`  | The database username                                |
| `password`         | `String`  | The database password                                |
| `maxConnections`   | `Integer` | Maximum number of pooled connections                 |
| `connectionTimeout` | `Integer` | Connection timeout in milliseconds                    |

### Example

```boxlang
class myDatasourceListener {
	function onDatasourceStartup( struct data ) {
		var name = data.name;
		var properties = data.properties;
		var config = data.config;
		
		logger.info( "Datasource [#name#] is starting up" );
		logger.debug( "Driver: #properties.driver#" );
		logger.debug( "URL: #properties.url#" );
		
		// Perform last-minute configuration adjustments
		if ( !properties.keyExists( "maxConnections" ) ) {
			properties.maxConnections = 10;
			logger.debug( "Set default max connections to 10" );
		}
		
		// You could also validate the datasource configuration here
		if ( !properties.keyExists( "url" ) || !properties.keyExists( "driver" ) ) {
			logger.error( "Invalid datasource configuration for [#name#]" );
		}
	}
}
```

---

## onDatasourceConfigLoad

This event is triggered immediately before a datasource configuration is loaded and processed. This is a good place to modify datasource configuration properties, apply environment-specific settings, or validate configuration before the datasource initializes.

### Data Structure

| Data Key     | Type           | Description                                           |
| ------------ | -------------- | ----------------------------------------------------- |
| `name`       | `String`       | The datasource name                                   |
| `properties` | `Struct`       | Datasource configuration properties to be loaded      |

### Example

```boxlang
class myDatasourceListener {
	function onDatasourceConfigLoad( struct data ) {
		var name = data.name;
		var properties = data.properties;
		
		logger.info( "Datasource [#name#] configuration is loading" );
		
		// Apply environment-specific overrides
		var environment = systemDot.getProperty( "environment", "development" );
		
		if ( environment == "production" ) {
			// Increase pool size in production
			properties.maxConnections = 50;
			logger.debug( "Production mode: set max connections to 50" );
		} else if ( environment == "development" ) {
			// Use smaller pool in development
			properties.maxConnections = 5;
			logger.debug( "Development mode: set max connections to 5" );
		}
		
		// You could also load properties from external sources
		logger.debug( "Loading configuration for datasource: #name#" );
		logger.debug( "Properties: #properties.toString()#" );
	}
}
```

---

## DatasourceConfig Class Properties

The `DatasourceConfig` object available in datasource events provides configuration information:

| Property | Type | Description |
|----------|------|-------------|
| `getName()` | `String` | Get the datasource name |
| `getProperties()` | `Struct` | Get all configuration properties |
| `getProperty(key)` | `Object` | Get a specific property value |
| `setProperty(key, value)` | `void` | Set a property value |

---

## Context Variables Available in All Events

When implementing any datasource event listener, the following variables are automatically available in your function scope:

| Variable | Type | Description |
|----------|------|-------------|
| `logger` | `Logger` | Logger instance for this interceptor |
| `boxRuntime` | `BoxRuntime` | The BoxRuntime instance |
| `interceptorService` | `InterceptorService` | The InterceptorService instance |
| `properties` | `Struct` | Interceptor configuration properties |

---

## Event Execution Order

```
DATASOURCE SERVICE LIFECYCLE
│
├─ onDatasourceServiceStartup
│  [DatasourceService starts]
│
├─ onDatasourceConfigLoad (per datasource)
│  [Datasource configuration loads]
│
├─ onDatasourceStartup (per datasource)
│  [Individual datasource starts]
│
├─ [Datasources available for use]
│
└─ onDatasourceServiceShutdown
   [DatasourceService shuts down]
```

---

## How to Register a Datasource Event Listener

Create an interceptor class and register it through BoxLang's interceptor service:

### Option 1: Via Application Listener

```boxlang
component {
	function onApplicationStart() {
		var interceptorService = application.boxRuntime.getInterceptorService();
		var listener = new MyDatasourceListener();
		interceptorService.register( listener );
	}
}
```

### Option 2: Via Module Configuration

```boxlang
component {
	function configure() {
		settings = {
			name = "DatasourceModule",
			version = "1.0.0"
		};
		
		// Register your event listener
		interceptors = [
			{ class="path.to.MyDatasourceListener", properties={} }
		];
	}
}
```

### Option 3: Implement in Listener Class

```boxlang
component displayname="MyDatasourceListener" {
	
	function onDatasourceServiceStartup( struct data ) {
		// Handle event
	}
	
	function onDatasourceConfigLoad( struct data ) {
		// Handle event
	}
	
	function onDatasourceStartup( struct data ) {
		// Handle event
	}
	
	function onDatasourceServiceShutdown( struct data ) {
		// Handle event
	}
}
```

---

## Common Use Cases

| Use Case | Event to Implement | What You Can Do |
|---|---|---|
| Monitor datasource startup | `onDatasourceStartup` | Log datasource details, validate configuration |
| Register custom datasources | `onDatasourceServiceStartup` | Add datasources programmatically |
| Apply environment settings | `onDatasourceConfigLoad` | Override connection pooling, credentials based on environment |
| Cleanup before shutdown | `onDatasourceServiceShutdown` | Close custom connections, save state |
| Modify connection pooling | `onDatasourceStartup` or `onDatasourceConfigLoad` | Adjust maxConnections, timeouts dynamically |
| Validate datasource setup | `onDatasourceConfigLoad` | Check required properties exist |
| Performance monitoring | `onDatasourceStartup` | Track startup times, log configuration |
| Dynamic configuration | `onDatasourceConfigLoad` | Load config from files, environment variables, remote sources |

---

## Example: Complete Datasource Listener

```boxlang
component displayname="CompleteDatasourceListener" {

	function onDatasourceServiceStartup( struct data ) {
		var datasourceService = data.datasourceService;
		logger.info( "==== DATASOURCE SERVICE STARTUP ====" );
		logger.info( "Available datasources: #datasourceService.getNames().toString()#" );
	}

	function onDatasourceConfigLoad( struct data ) {
		var name = data.name;
		var properties = data.properties;
		var env = systemDot.getProperty( "environment", "dev" );
		
		logger.info( "Configuring datasource: #name# (Environment: #env#)" );
		
		// Environment-specific configuration
		switch( env ) {
			case "production":
				properties.maxConnections = 100;
				properties.connectionTimeout = 30000;
				break;
			case "staging":
				properties.maxConnections = 50;
				properties.connectionTimeout = 20000;
				break;
			default:
				properties.maxConnections = 10;
				properties.connectionTimeout = 10000;
		}
		
		logger.debug( "Max connections set to: #properties.maxConnections#" );
	}

	function onDatasourceStartup( struct data ) {
		var name = data.name;
		var startTime = now();
		
		logger.info( "Starting datasource: #name#" );
		
		// You could perform validation here
		var properties = data.properties;
		if ( !properties.keyExists( "url" ) || properties.url.isEmpty() ) {
			logger.error( "Datasource [#name#] missing required URL property" );
		}
	}

	function onDatasourceServiceShutdown( struct data ) {
		var datasourceService = data.datasourceService;
		logger.info( "==== DATASOURCE SERVICE SHUTDOWN ====" );
		logger.info( "Datasources being shut down: #datasourceService.getNames().toString()#" );
	}
}
```

---

## Best Practices

1. **Log strategically** - Use appropriate log levels (info for important events, debug for details)
2. **Validate early** - Check configuration in `onDatasourceConfigLoad` before startup
3. **Handle errors gracefully** - Don't throw exceptions in listeners; log errors instead
4. **Keep listeners fast** - Long-running operations can slow service startup/shutdown
5. **Use environment detection** - Apply different settings based on environment in event listeners
6. **Document custom properties** - If adding custom properties, document them clearly
7. **Clean up resources** - Ensure cleanup happens in `onDatasourceServiceShutdown`
8. **Test thoroughly** - Test listeners with various datasource configurations
