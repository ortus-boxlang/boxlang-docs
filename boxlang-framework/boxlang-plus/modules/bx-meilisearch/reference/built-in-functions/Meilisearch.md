[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Meilisearch`

Returns the Meilisearch fluent DSL entry point for interacting with a Meilisearch search engine instance.

This function provides access to the complete Meilisearch API through a fluent, chainable interface. It reads connection settings from the module configuration and returns a DSL object that allows you to manage indexes, documents, search operations, settings, API keys, and tasks.

The connection is configured through the module settings in `boxlang.json` or via environment variables. See the [Meilisearch module documentation](/boxlang-framework/boxlang-plus/modules/bx-meilisearch/README.md#-installation) for configuration details.

## Method Signature

```
Meilisearch()
```

### Arguments

This function takes no arguments. All configuration is handled through module settings.

## Examples

### Basic Usage

Get the Meilisearch DSL entry point:

```js
meili = meilisearch()
```

### Creating an Index

Create a new index with a specific primary key:

```js
meilisearch()
    .index( "books" )
    .create( "id" )
```

### Adding Documents

Add or replace documents in an index:

```js
task = meilisearch()
    .index( "books" )
    .documents()
    .add([
        { id: 1, title: "BoxLang in Action", author: "Ortus Solutions" },
        { id: 2, title: "Search-Driven Apps", author: "Jane Doe" }
    ])
    .orReplace()

// Returns a Task object to track the async operation
println( "Task status: #task.getStatus()#" )
```

### Searching Documents

Perform a basic search:

```js
results = meilisearch()
    .index( "books" )
    .search( "boxlang" )
    .send()

println( "Found #results.estimatedTotalHits# results" )
```

### Advanced Search with Filters

Chain multiple search parameters for advanced queries:

```js
results = meilisearch()
    .index( "books" )
    .search( "programming" )
    .filter( "year > 2020" )
    .limit( 10 )
    .offset( 0 )
    .attributesToRetrieve( "title,author,year" )
    .send()

for ( hit in results.hits ) {
    println( "#hit.title# by #hit.author# (#hit.year#)" )
}
```

### Listing All Indexes

Retrieve a list of all indexes:

```js
result = meilisearch()
    .indexes()
    .list()

println( "Found #result.total# indexes" )
for ( index in result.results ) {
    println( "Index: #index.uid#" )
}
```

### Getting Index Statistics

Retrieve statistics for a specific index:

```js
stats = meilisearch()
    .index( "books" )
    .stats()

println( "Documents: #stats.numberOfDocuments#" )
println( "Database size: #stats.databaseSize# bytes" )
```

### Updating Index Settings

Configure searchable attributes and other index settings:

```js
meilisearch()
    .index( "books" )
    .settings()
    .update({
        searchableAttributes: [ "title", "author", "description" ],
        filterableAttributes: [ "year", "genre" ],
        sortableAttributes: [ "year", "title" ]
    })
```

### Deleting Documents

Delete a single document by ID:

```js
task = meilisearch()
    .index( "books" )
    .document( "123" )
    .delete()
```

Delete all documents from an index:

```js
task = meilisearch()
    .index( "books" )
    .documents()
    .deleteAll()
```

### Faceted Search

Search for facet values within a given facet:

```js
result = meilisearch()
    .index( "books" )
    .facetSearch( "genre", {
        facetQuery: "fiction",
        filter: "year > 2020"
    })
    .send()

for ( facet in result.facetHits ) {
    println( "#facet.value#: #facet.count# results" )
}
```

### Managing API Keys

List all API keys:

```js
keys = meilisearch()
    .keys()
    .list()

for ( key in keys.results ) {
    println( "Key: #key.name#" )
}
```

## Related Functions

- [http()](/boxlang-language/reference/built-in-functions/net/HTTP.md) - HTTP client used internally by the Meilisearch module

## Additional Resources

- [Meilisearch Module Documentation](boxlang-framework/boxlang-plus/modules/bx-meilisearch/README.md) - Complete module overview and installation guide
- [Meilisearch API Documentation](boxlang-framework/boxlang-plus/modules/bx-meilisearch/api-usage.md) - Detailed API wrapper usage patterns
- [Official Meilisearch Documentation](https://www.meilisearch.com/docs) - Meilisearch API reference
