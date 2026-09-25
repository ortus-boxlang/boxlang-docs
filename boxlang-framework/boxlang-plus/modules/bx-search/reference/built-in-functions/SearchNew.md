[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SearchNew`

Creates and returns a new {@link SearchBuilder} wired to the active search
 provider.

The builder returned is the entry point for the bx-search fluent query API.
 When an {@code index} is supplied, {@code newSearch( ... )} is invoked
 automatically; otherwise the caller must call {@code builder.newSearch( collection )}
 before executing. When a {@code properties} struct is provided, it becomes the
 starting query DSL for the builder (equivalent to calling {@code setQuery( properties )}).

## Method Signature

```
SearchNew(index=[string], properties=[struct])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `index` | `string` | `false` | Optional bare collection name. If omitted the caller must invoke<br>                 {@code builder.newSearch(collection)} before executing. |  |
| `properties` | `struct` | `false` | Optional struct containing a raw query body. When provided,<br>                      this becomes the starting DSL for the builder (equivalent to<br>                      calling {@code setQuery(properties)}). |  |

## Examples

# SearchNew / SearchBuilder

`SearchNew()` returns a fluent `SearchBuilder` that is pre-wired to the active search
provider. The sections below document every builder method with a description and a
usage example.

---

## Initialization

### `newSearch( collection )` / `newSearch( collection, properties )`

Sets the target collection and, optionally, pre-populates the query from a raw DSL
struct. Any previously configured query state is reset first.

```boxlang
// New search on the "products" collection
SearchNew().newSearch( "products" );

// New search populated from a raw DSL struct
SearchNew().newSearch( "products", {
    "query": { "match_all": {} }
} );
```

### `reset()`

Clears all query state, returning the builder to a blank slate. The collection and
provider are retained.

```boxlang
var builder = SearchNew( "products" ).match( "title", "BoxLang" );
// Later, start over but keep the same collection
builder.reset().match( "description", "search engine" );
```

---

## Match methods

### `match( name, value )`

Adds a standard `match` query clause against a single field (analyzed text). By default
it is added to the `must` (AND) list. Supports optional boost, options, and occurrence.

```boxlang
SearchNew( "products" ).match( "title", "BoxLang" );
```

Match with a relevance boost and additional options against any given occurrence:

```boxlang
var results = SearchNew( "products" )
    .match(
        "description",
        "fast JVM language",
        1.5,                                // boost
        { "operator": "and", "fuzziness": "AUTO" },  // match options
        "must"                              // occurrence: must | should | must_not
    )
    .execute();
```

### `mustMatch( name, value )`

Adds a `must` match clause — documents **must** match to be returned.

```boxlang
SearchNew( "products" )
    .mustMatch( "isActive", true )
    .mustMatch( "category", "languages", 2.0 );  // optional boost
```

### `mustNotMatch( name, value )`

Adds a `must_not` match clause — documents must **not** match.

```boxlang
SearchNew( "products" )
    .mustNotMatch( "status", "archived" )
    .mustNotMatch( "sku", "LEGACY-*", 1.2 );   // optional boost
```

### `shouldMatch( name, value )`

Adds a `should` match clause — documents **may** match (boosts their relevance score).

```boxlang
SearchNew( "products" )
    .mustMatch( "category", "languages" )
    .shouldMatch( "tags", "boxlang" )
    .shouldMatch( "tags", "cfml", 1.5 );      // optional boost
```

### `multiMatch( names, value )`

Searches multiple fields at once using Elasticsearch's `multi_match` query. Supports
optional boost, `type` (e.g. `best_fields`, `cross_fields`), and occurrence.

```boxlang
SearchNew( "products" ).multiMatch( [ "title", "description", "tags" ], "boxlang" );
```

Full signature with boost, match type, and occurrence:

```boxlang
SearchNew( "products" ).multiMatch(
    [ "title", "body" ],
    "database",
    1.8,               // boost
    "cross_fields",    // multi_match type
    "should"           // occurrence
);
```

### `dateMatch( name, start, end )`

Adds a date range filter clause on a date-mapped field. Supports ISO-8601 strings and
Elasticsearch date math (e.g. `now-7d`). Only one bound is required.

```boxlang
// Publish dates within the last 7 days
var results = SearchNew( "articles" )
    .mustMatch( "status", "published" )
    .dateMatch( "publishDate", "now-7d", null )
    .sort( "publishDate DESC" )
    .execute();

// An explicit range between two dates
SearchNew( "articles" ).dateMatch( "publishDate", "2026-01-01", "2026-12-31" );
```

---

## Term / Wildcard

### `term( name, value )`

Adds an exact-value `term` query — ideal for keyword fields that are not analyzed.
Supports optional boost and occurrence.

```boxlang
SearchNew( "products" ).term( "sku", "BL-001" );

// With boost, as a should
SearchNew( "products" ).term( "sellerId", 42, 3.0 );
```

### `wildcard( name, value )`

Adds a `wildcard` query for partial matches on keyword-mapped fields. Note that
wildcards are slower than `term`/`match`. The pattern is wrapped in `*...*`
automatically.

```boxlang
SearchNew( "products" ).wildcard( "sku", "BL" );       // matches BL* name contains
SearchNew( "products" ).wildcard( "brand", "Acme", 1.5, "must_not" );
```

---

## Sorting

### `sort( field )` / `sort( field, config )`

Appends a sort directive. May be called multiple times for compound sorting.

```boxlang
// Space-separated field + direction string
SearchNew( "products" ).sort( "publishDate DESC" );

// Separate field and direction
SearchNew( "products" ).sort( "price", "asc" );

// Full config map
SearchNew( "products" ).sort( "post_date", {
    "order": "desc",
    "format": "strict_date_optional_time_nanos"
} );

// Compound sort
SearchNew( "products" ).sort( "publishDate DESC" ).sort( "price ASC" );
```

---

## Pagination

### `setFrom( from )`

Sets the zero-based starting offset for pagination.

```boxlang
SearchNew( "products" ).setFrom( 20 ).setSize( 10 );
```

### `setSize( size )`

Sets the maximum number of documents to return per page (default is 10).

```boxlang
SearchNew( "products" ).setSize( 100 ).execute();
```

---

## Field projection

### `setFields( fields... )`

Sets the list of fields to return in each hit, replacing the full `_source` with the
projected fields. Accepts indexed and runtime field names.

```boxlang
var results = SearchNew( "products" )
    .setFields( "title", "price", "sku" )
    .execute();
```

### `addField( field )`

Appends a single field to the projection list.

```boxlang
SearchNew( "products" ).setFields( "title" ).addField( "description" );
```

### `addScriptField( name, script )`

Defines a script field, computed at search time for each hit. The script is an
Elasticsearch script definition map.

```boxlang
var results = SearchNew( "products" )
    .addScriptField( "discountedPrice", {
        "source": "doc['price'].value * 0.9"
    } )
    .execute();
```

### `addRuntimeMapping( name, mapping )`

Defines a runtime field mapping evaluated at search time (type plus optional script).

```boxlang
var results = SearchNew( "products" )
    .addRuntimeMapping( "searchScore", {
        "type": "long",
        "script": { "source": "(doc['price'].value > 100 ? 5 : 1)" }
    } )
    .execute();
```

---

## Aggregations & Highlight

### `aggregation( name, options )`

Adds an aggregation directive, retrievable afterwards from
`SearchResult#getAggregations()`.

```boxlang
var results = SearchNew( "products" )
    .match( "category", "languages" )
    .aggregation( "maxPrice", { "max": { "field": "price" } } )
    .aggregation( "byBrand", { "terms": { "field": "brand" } } )
    .execute();
```

### `highlight( options )`

Sets the highlight configuration so matching fragments are returned with each hit.

```boxlang
var results = SearchNew( "products" )
    .match( "description", "search engine" )
    .highlight( {
        "fields": { "description": { "fragment_size": 100 } }
    } )
    .execute();
```

---

## Field collapse

### `collapseToField( field )` / `collapseToField( field, options, includeOccurrences )`

Collapses results to the single most-relevant document per unique value of the given
field. When `includeOccurrences` is `true`, cardinality/terms aggregations are added so
the collapsed counts are populated.

```boxlang
// Collapse to one result per seller
var results = SearchNew( "products" )
    .match( "category", "languages" )
    .collapseToField( "sellerId" )
    .execute();

// Collapse including occurrence counts
SearchNew( "products" )
    .collapseToField( "brand", { "inner_hits": { "size": 3 } }, true );
```

---

## Raw DSL override

### `setQuery( dsl )`

Sets the raw query body, overriding every built clause. Useful for passing a pre-built
DSL struct directly (accepts a struct or a plain Java map).

```boxlang
var results = SearchNew( "products" )
    .setQuery( { "query": { "match_all": {} } } )
    .setSize( 5 )
    .execute();
```

---

## Request parameters

### `param( name, value )`

Appends a query-string parameter to the request URL (e.g. `version`).

```boxlang
SearchNew( "products" ).param( "version", true ).execute();
```

### `bodyParam( name, value )`

Appends a request body parameter merged into the top-level body (e.g. `track_scores`,
`min_score`).

```boxlang
SearchNew( "products" )
    .match( "title", "BoxLang" )
    .bodyParam( "min_score", 1.5 )
    .execute();
```

---

## DSL assembly

### `getDSL()` / `getDSLAsStruct()`

Assembles and returns the complete query body **without** executing it. Useful for
debugging or passing the DSL elsewhere.

```boxlang
var builder = SearchNew( "products" ).match( "title", "BoxLang" ).setSize( 20 );

var dsl      = builder.getDSL();          // plain struct
var dslAsStr = builder.getDSLAsStruct();  // explicit IStruct

writeDump( builder.getDSL() );
```

---

## Execution

### `execute()`

Executes the search and returns the full result set as a `SearchResult`.

```boxlang
var results = SearchNew( "products" )
    .match( "title", "BoxLang" )
    .setSize( 20 )
    .execute();
```

### `count()`

Executes the query and returns only the matched document count — more efficient than
`execute()` when only a count is needed.

```boxlang
var total = SearchNew( "products" )
    .mustMatch( "isActive", true )
    .count();
writeOutput( "Total active products: #total#" );
```

### `deleteAll()`

Deletes all documents in the collection that match the current query.

```boxlang
var deleted = SearchNew( "auditLogs" )
    .dateMatch( "loggedAt", null, "now-90d" )
    .deleteAll();
writeOutput( "Deleted #deleted# log entries." );
```

### `getTermVectors( documentId, fields )`

Retrieves term vectors (term frequency, etc.) for a document in the target collection.
Optional options map is supported (e.g. `min_word_length`).

```boxlang
var vectors = SearchNew( "products" )
    .getTermVectors( "prod-123", [ "title", "description" ] );
```

---

## Accessors

### `getCollection()` / `getProvider()`

Access the target collection name (bare, un-prefixed) and the backing provider.

```boxlang
var builder = SearchNew( "products" );
writeOutput( "Collection: #builder.getCollection()#" );
```

## Related


