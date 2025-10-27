---
description: >-
  Premium Couchbase integration module offering distributed caching and NoSQL
  document access for BoxLang+ applications.
icon: couch
---

# Couchbase +

### \*\*_Coming Soon!\*\*_

The `bx-couchbase` module integrates Couchbase Server with BoxLang, enabling distributed caching, key/value storage, and document access patterns for horizontally scaled applications.

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://ww.boxlang.io/plans) but can be installed in conjunction with the [`bx-plus` Module](bx-plus.md) with a limited trial.
{% endhint %}

## 🚀 Features

* High-performance distributed cache provider
* Key/value operations with TTL support
* JSON document storage & retrieval
* Bucket, scope, and collection targeting
* Basic N1QL query execution (conceptual)
* Connection pooling & health pings

## 📦 Installation

### Via CommandBox

```bash
box install bx-couchbase
```

### Via BoxLang

```bash
install-bx-module bx-couchbase
```

## ⚙ Configuration

```jsonc
{
  "couchbase": {
    "connectionString": "couchbase://localhost",
    "username": "Administrator",
    "password": "password",
    "bucket": "default",
    "scope": "_default",
    "collection": "_default",
    "defaultTTLSeconds": 900
  }
}
```

Environment overrides:

```bash
export COUCHBASE_CONNECTION_STRING=couchbase://db.internal
export COUCHBASE_USERNAME=Administrator
export COUCHBASE_PASSWORD=secret
```

## 🧪 Basic Usage

```js
cb = moduleService.get( "bx-couchbase" );

// Store document
cb.upsert( key = "user:42", value = { id: 42, name: "Alice", active: true }, ttl = 600 );

// Retrieve
user = cb.get( "user:42" );
writeDump( var = user );
```

## 🔍 Query (Conceptual)

```js
results = cb.query( "SELECT name FROM default WHERE active = TRUE LIMIT 10" );
for ( r in results ) {
    writeOutput( r.name & "<br>" );
}
```

## 🧰 Cache Provider Integration

Configure Couchbase as a BoxCache provider for distributed caching:

```js
cache = cacheService.getCache( "default" );
cache.put( id = "landing", value = generateLandingHTML(), timeout = 120 );
html = cache.get( "landing" );
```

## 🛡 Error Handling

```js
try {
    doc = cb.get( "user:100" );
} catch ( e ) {
    writeLog( text = "Couchbase access failed: " & e.message, type = "error" );
}
```

## 🔐 Entitlement

Requires valid BoxLang+ subscription (`bx-plus`). Entitlement failures provide actionable messaging.

## 📏 Performance Tips

* Prefer upsert over separate exists + insert flows
* Use TTL for ephemeral data to control memory
* Batch queries where possible

## 📎 Related Modules

{% content-ref url="bx-redis/" %}
[bx-redis](bx-redis/)
{% endcontent-ref %}

{% content-ref url="bx-plus.md" %}
[bx-plus.md](bx-plus.md)
{% endcontent-ref %}

***

Return to the [Modules Overview](./).
