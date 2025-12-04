# couchbaseGetScope

Get a Couchbase scope instance within a bucket.

## Syntax

```js
couchbaseGetScope(cacheName, [scopeName])
```

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `cacheName` | String | Yes | - | Name of the cache configuration |
| `scopeName` | String | No | `_default` | Name of the scope within the bucket |

## Returns

Returns the Couchbase `Scope` instance with access to:
- Collection management
- Query execution scoped to this scope
- Analytics scoped to this scope

## Examples

### Get Default Scope

```js
// Get default scope (most common)
scope = couchbaseGetScope("default");

// Access default collection
collection = scope.defaultCollection();
```

### Get Custom Scope

```js
// Get specific scope
myAppScope = couchbaseGetScope("default", "myapp");

// Access collections in this scope
usersCollection = myAppScope.collection("users");
ordersCollection = myAppScope.collection("orders");
```

### Execute Scoped Queries

```js
scope = couchbaseGetScope("default", "myapp");

// Query within this scope
result = scope.query(
    "SELECT * FROM users WHERE status = 'active'"
);
```

### Multiple Scopes

```js
// Different scopes for different app modules
authScope = couchbaseGetScope("default", "auth");
ecomScope = couchbaseGetScope("default", "ecommerce");
analyticsScope = couchbaseGetScope("default", "analytics");

// Each scope has its own collections
usersCollection = authScope.collection("users");
productsCollection = ecomScope.collection("products");
eventsCollection = analyticsScope.collection("events");
```

### Scope Organization

```js
// Organize by environment
devScope = couchbaseGetScope("app-cache", "development");
prodScope = couchbaseGetScope("app-cache", "production");

// Same collection names, different scopes
devUsersCollection = devScope.collection("users");
prodUsersCollection = prodScope.collection("users");
```

## Notes

- Default scope is `_default` (Couchbase standard)
- Scopes provide namespace isolation within a bucket
- Useful for multi-tenant applications
- Each scope can have multiple collections
- Scope names are case-sensitive
- Scope must exist in Couchbase or operation will fail

## Scope Benefits

- **Namespace isolation** - Separate data logically within one bucket
- **Access control** - Grant permissions per scope
- **Organization** - Group related collections together
- **Multi-tenancy** - Isolate tenant data within scopes
- **Environment separation** - dev/staging/prod in same bucket

## Related Functions

- [couchbaseGetBucket](CouchbaseGetBucket.md) - Get bucket instance
- [couchbaseGetCollection](CouchbaseGetCollection.md) - Get collection instance
- [couchbaseQuery](CouchbaseQuery.md) - Execute queries

## See Also

- [API Usage Guide](../../api-usage.md)
- [Couchbase Scopes & Collections](https://docs.couchbase.com/server/current/learn/data/scopes-and-collections.html)
