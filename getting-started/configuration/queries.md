---
description: Configure global query defaults for the BoxLang runtime
icon: database
---

# Queries

{% hint style="info" %}
**Since BoxLang 1.14.0**. The `queries` configuration section lets you set global defaults for all `queryExecute()` and `bx:query` operations in the runtime.
{% endhint %}

BoxLang allows you to define global query option defaults that apply to every query execution in the runtime. These defaults can be overridden per-query by passing explicit options to `queryExecute()` or via `bx:query` attributes.

## Configuration Structure

The queries configuration is located in the `queries` section of your `boxlang.json` file:

{% code title="boxlang.json" %}
```json
// Query Default Options
"queries": {
    // The default timeout for queries in seconds. 0 means no timeout.
    // This can be overridden per query.
    "timeout": 0,
    // The default return type for queries.
    // Valid values: "query", "array", "struct". Overridable per query.
    "returnType": "query",
    // Number of rows to fetch from the database at once.
    // Defaults to all rows (0). Overridable per query.
    "fetchSize": 0,
    // Maximum number of rows to return. Defaults to all rows (0).
    // Overridable per query.
    "maxRows": 0,
    // The default named cache to use for query caching.
    // This cache must be defined in the "caches" section of this config file.
    "cacheProvider": "default"
}
```
{% endcode %}

## Configuration Properties

### `timeout`

| Property | Value |
|----------|-------|
| **Type** | `numeric` |
| **Default** | `0` |
| **Description** | The default query timeout in seconds. A value of `0` means no timeout. This can be overridden per query via the `timeout` option in `queryExecute()` or the `timeout` attribute on `bx:query`. |

### `returnType`

| Property | Value |
|----------|-------|
| **Type** | `string` |
| **Default** | `"query"` |
| **Description** | The default return type for query results. Valid values are `"query"`, `"array"`, and `"struct"`. When `"struct"` is used, a `columnKey` must be provided per query. This can be overridden per query via the `returnType` option in `queryExecute()`. |

### `fetchSize`

| Property | Value |
|----------|-------|
| **Type** | `numeric` |
| **Default** | `0` |
| **Description** | The number of rows to fetch from the database at once. A value of `0` fetches all rows. Useful for controlling JDBC driver fetch behavior and memory usage on large result sets. Overridable per query via the `fetchSize` option in `queryExecute()`. |

### `maxRows`

| Property | Value |
|----------|-------|
| **Type** | `numeric` |
| **Default** | `0` |
| **Description** | The maximum number of rows to return from a query. A value of `0` returns all rows. Use this to limit result set size globally. Overridable per query via the `maxRows` option in `queryExecute()`. |

### `cacheProvider`

| Property | Value |
|----------|-------|
| **Type** | `string` |
| **Default** | `"default"` |
| **Description** | The named cache provider to use for query caching. This cache must be defined in the `caches` section of the `boxlang.json` configuration file. When set, query results can be cached automatically if caching is enabled per query. Overridable per query via the `cacheProvider` option in `queryExecute()`. |

## Per-Query Overrides

All global defaults can be overridden on individual queries by passing the corresponding option to `queryExecute()`:

```js
// Override global defaults for a specific query
var result = queryExecute(
    "SELECT * FROM users",
    {},
    {
        timeout: 30,           // override global timeout
        returnType: "array",   // override global returnType
        maxRows: 100,          // override global maxRows
        fetchSize: 50,         // override global fetchSize
        cacheProvider: "redis" // override global cacheProvider
    }
)
```

The `bx:query` component also supports these options as attributes:

```html
<bx:query name="result" datasource="app"
    timeout="30"
    returnType="array"
    maxRows="100"
    fetchSize="50"
    cacheProvider="redis">
    SELECT * FROM users
</bx:query>
```

## Application-Level Defaults

In addition to the global `boxlang.json` configuration, you can set query option defaults at the application level using `this.queryOptions` in your `Application.bx`:

```js
// Application.bx
class Application {
    // Query Default Options for this application
    this.queryOptions = {
        // The default timeout for queries in seconds. 0 means no timeout.
        "timeout": 0,
        // The default return type: "query", "array", or "struct"
        "returnType": "query",
        // Number of rows to fetch from database at once
        "fetchSize": 0,
        // Maximum number of rows to return, defaults to all rows (0)
        "maxRows": 0,
        // The default named cache to use for query caching
        "cacheProvider": "default"
    }

    function onRequest( event, interceptData ) {
        // All queries in this application use these defaults
        // unless overridden per query
    }
}
```

{% hint style="info" %}
**Precedence**: Per-query options take the highest priority, followed by `this.queryOptions` in `Application.bx`, with `boxlang.json` global defaults as the fallback.
{% endhint %}

## Query Transformers

Since BoxLang 1.14.0, you can also register **query transformers** at the application level via `this.queryTransformers` in `Application.bx`. See [Queries](../../boxlang-language/queries.md#-query-transformers--custom-result-formatting) for complete documentation.

## See Also

{% content-ref url="../../boxlang-language/queries.md" %}
[Queries](queries.md)
{% endcontent-ref %}

{% content-ref url="datasources.md" %}
[Datasources](datasources.md)
{% endcontent-ref %}

{% content-ref url="caches.md" %}
[Caches](caches.md)
{% endcontent-ref %}
