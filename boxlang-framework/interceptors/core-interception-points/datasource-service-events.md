# Datasource Service Events

These events occur around the lifecycle of datasources and the datasource service.

* [`onDatasourceServiceStartup`](#onDatasourceServiceStartup)
* [`onDatasourceServiceShutdown`](#onDatasourceServiceShutdown)
* [`onDatasourceStartup`](#onDatasourceStartup)

## onDatasourceServiceStartup

This event is triggered immediately after the datasource service has started. You could use this event to register custom datasources after the service has started, for example. 

### Data Elements

- `DatasourceService`: Instance - The BoxLang datasource service.

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

### Data Elements

- `DatasourceService`: The BoxLang datasource service.

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

### Data Elements

- `name` - String - Name
- `properties` - Struct - Datasource configuration properties
- `config` - Instance - Datasource configuration object

### Example

```js
class myDatasourceListener {
    function onDatasourceStartup( struct data ) {
        println("Datasource [#data.name#] is starting up!");
        println( data.properties );
    }
}
```