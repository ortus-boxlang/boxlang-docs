---
description: Built-in function reference for the BoxLang Meilisearch module.
icon: function
---

# Built-In Function Reference

This section contains reference documentation for the built-in functions provided by the BoxLang Meilisearch module.

## Available Functions

### Core Functions

| Function | Description |
|----------|-------------|
| [Meilisearch()](Meilisearch.md) | Returns the Meilisearch fluent DSL entry point for interacting with a Meilisearch search engine instance |

## Usage Pattern

All Meilisearch operations begin with the `meilisearch()` function, which returns a fluent DSL object for chaining operations:

```js
// Basic pattern
meilisearch()
    .index( "indexName" )
    .operation()
    
// Example: Search
results = meilisearch()
    .index( "books" )
    .search( "query" )
    .send()
```

See the [Meilisearch() function documentation](Meilisearch.md) for complete examples and usage patterns.