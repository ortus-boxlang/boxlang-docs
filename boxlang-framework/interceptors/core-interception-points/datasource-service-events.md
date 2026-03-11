# Datasource Service Events

These events occur around the lifecycle of datasources and the datasource service. They are announced on the **global interceptor pool**.

| Event Name                    | Cancellable | Description                                          |
| ----------------------------- | :---------: | ---------------------------------------------------- |
| `onDatasourceServiceStartup`  |     No      | After the datasource service has started up.         |
| `onDatasourceServiceShutdown` |     No      | Before the datasource service shuts down.            |
| `onDatasourceConfigLoad`      |     No      | Before a datasource configuration is loaded.         |
| `onDatasourceStartup`         |     No      | Before an individual datasource is started.          |

* [`onDatasourceServiceStartup`](#ondatasourceservicestartup)
* [`onDatasourceServiceShutdown`](#ondatasourceserviceshutdown)
* [`onDatasourceConfigLoad`](#ondatasourceconfigload)
* [`onDatasourceStartup`](#ondatasourcestartup)

## onDatasourceServiceStartup

Fired immediately after the datasource service has started up and is ready to manage datasources. This is a good place to register custom datasources or initialize datasource-related resources.

### Data Structure

| Data Key            | Type                | Description                               |
| ------------------- | ------------------- | ----------------------------------------- |
| `datasourceService` | `DatasourceService` | Instance of the BoxLang DatasourceService.|

### Example

```groovy
class myListener{
	function onDatasourceServiceStartup( struct data ){
		var datasourceService = data.datasourceService;
	}
}
```

## onDatasourceServiceShutdown

Fired immediately before the datasource service shuts down. This is a good place to perform cleanup on custom datasources, close connections, or release resources.

### Data Structure

| Data Key            | Type                | Description                               |
| ------------------- | ------------------- | ----------------------------------------- |
| `datasourceService` | `DatasourceService` | Instance of the BoxLang DatasourceService.|

### Example

```groovy
class myListener{
	function onDatasourceServiceShutdown( struct data ){
		var datasourceService = data.datasourceService;
	}
}
```

## onDatasourceConfigLoad

Fired immediately before a datasource configuration is loaded and processed. This is a good place to modify datasource configuration properties or apply environment-specific settings before the datasource initializes.

### Data Structure

| Data Key     | Type     | Description                                      |
| ------------ | -------- | ------------------------------------------------ |
| `name`       | `String` | The datasource name.                             |
| `properties` | `Struct` | Datasource configuration properties to be loaded.|

### Example

```groovy
class myListener{
	function onDatasourceConfigLoad( struct data ){
		var name       = data.name;
		var properties = data.properties;
	}
}
```

## onDatasourceStartup

Fired immediately before an individual datasource is started. This is a good place to perform last-minute configuration tweaks or validate settings before the datasource becomes available for queries.

### Data Structure

| Data Key     | Type               | Description                                                           |
| ------------ | ------------------ | --------------------------------------------------------------------- |
| `name`       | `String`           | The datasource name.                                                  |
| `properties` | `Struct`           | Datasource configuration properties.                                  |
| `config`     | `DatasourceConfig` | Instance of the DatasourceConfig class storing all datasource config. |

### Example

```groovy
class myListener{
	function onDatasourceStartup( struct data ){
		var name       = data.name;
		var properties = data.properties;
		var config     = data.config;
	}
}
```
