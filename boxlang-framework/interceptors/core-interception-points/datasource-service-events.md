# Datasource Service Events

These events occur around the lifecycle of datasources and the datasource service.

* [`onDatasourceServiceStartup`](#onDatasourceServiceStartup)
* [`onDatasourceServiceShutdown`](#onDatasourceServiceShutdown)
* [`onDatasourceStartup`](#onDatasourceStartup)
* [`onDatasourceConfigLoad`](#onDatasourceConfigLoad)
* [`onDatasourceInitialized`](#onDatasourceInitialized)

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

## onDatasourceInitialized

{% hint style="success" %}
New in BoxLang 1.14.0
{% endhint %}

This event is triggered after the datasource configuration has been loaded and processed but **before** the HikariCP connection pool is established. This interception point gives modules and interceptors full access to the raw HikariCP configuration for advanced customization — connection pool sizing, statement caching, timeouts, and any other HikariCP-specific settings.

| Data Key          | Type           | Description                                                                                           |
| ----------------- | -------------- | ----------------------------------------------------------------------------------------------------- |
| `name`            | String         | Datasource name                                                                                       |
| `properties`      | Struct         | Datasource configuration properties                                                                   |
| `hikariConfig`    | Java class     | The raw `com.zaxxer.hikari.HikariConfig` instance, fully configured but not yet used to create a pool |

### Example

```js
class myDatasourceListener {
    function onDatasourceInitialized( struct data ) {
        var hikariConfig = data.hikariConfig

        // Customize connection pool size
        hikariConfig.setMaximumPoolSize( 50 )
        hikariConfig.setMinimumIdle( 10 )

        // Enable statement caching
        hikariConfig.addDataSourceProperty( "cachePrepStmts", true )
        hikariConfig.addDataSourceProperty( "prepStmtCacheSize", 250 )
        hikariConfig.addDataSourceProperty( "prepStmtCacheSqlLimit", 2048 )

        // Adjust timeouts (milliseconds)
        hikariConfig.setConnectionTimeout( 30000 )
        hikariConfig.setIdleTimeout( 600000 )
        hikariConfig.setMaxLifetime( 1800000 )

        println( "Datasource [#data.name#] initialized with custom HikariCP settings" )
    }
}
```
