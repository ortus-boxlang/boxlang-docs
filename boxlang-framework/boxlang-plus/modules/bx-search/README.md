---
description: >-
  Equips BoxLang+ applications with full-text search capabilities — ideal for product catalogs,
  document repositories, knowledge bases, and log search workflows
icon: icon: magnifying-glass
---

# Search +

The BoxLang+ Licensed edition of the **bx-search** module equips your BoxLang+
applications with full-text search capabilities — ideal for product catalogs,
document repositories, knowledge bases, and log search workflows.

This module provides comprehensive full-text search functionality for BoxLang,
including:

- **CFML-compatible components** — `<bx:collection>`, `<bx:index>`, and `<bx:search>` with corresponding `cfcollection` / `cfindex` / `cfsearch` components in CFML files for compatibility
- **Fluent `SearchNew()` BIF** — a chainable `SearchBuilder` API for building and executing searches using a fluent syntax
- **Pluggable provider architecture** — swap between **Elasticsearch 8.x**, **OpenSearch**, and **Apache Solr 9.x** via a single config setting; extend with your own provider by implementing `ISearchProvider`
- **Attachment indexing** — index PDF, Word, and other binary files via the Elasticsearch/OpenSearch ingest-attachment pipeline or Apache Tika (Solr)
- **CFML `QUERY` result format** — `<bx:search>` returns a standard BoxLang `Query` with all expected columns (`KEY`, `TITLE`, `SUMMARY`, `URL`, `SCORE`, `RANK`, `CUSTOM1`–`CUSTOM4`, etc.)

> ⚠️ **This module is for BoxLang+ subscribers.** It can be evaluated with a
> limited trial alongside the [bx-plus module](https://boxlang.io/plans). Learn
> more at [https://boxlang.io/plans](https://boxlang.io/plans).

---

## Installation

The `bx-search` module is installed as part of the **bx-plus** boxlang module bundle.

```bash
# Using CommandBox — install the bx-plus bundle
install-bx-module bx-plus,bx-search
```

Or install directly via CommandBox:

```bash
box install bx-search
```

Or add to your `box.json` dependencies:

```json
"dependencies": {
    "bx-search": "*"
}
```

---

## Requirements

- **BoxLang Runtime** 1.17.0+
- **JDK** 21+
- A running **Elasticsearch 8.x**, **OpenSearch**, or **Apache Solr 9.x** instance (local or remote; Solr 8.x and earlier are not supported)

For file/attachment indexing on Elasticsearch/OpenSearch, the **ingest-attachment** plugin must be installed on your node:

```bash
# Elasticsearch
bin/elasticsearch-plugin install ingest-attachment

# OpenSearch
bin/opensearch-plugin install ingest-attachment
```

---

## Configuration

Configure the module in the `modules` block of your `boxlang.json` or `.cfconfig.json`:

```json
"bx-search": {
    "settings": {
        "engine": "elasticsearch",
        "host": "localhost",
        "port": 9200,
        "protocol": "http",
        "username": "",
        "password": "",
        "indexPrefix": "bxsearch_",
        "defaultLanguage": "en"
    }
}
```

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `engine` | `string` | `"elasticsearch"` | Provider to use: `"elasticsearch"`, `"opensearch"`, or `"solr"` |
| `host` | `string` | `"localhost"` | Hostname of the search cluster |
| `port` | `number` | `9200` | Port of the search cluster |
| `protocol` | `string` | `"http"` | `"http"` or `"https"` |
| `username` | `string` | `""` | Basic-auth username (leave blank if none) |
| `password` | `string` | `""` | Basic-auth password (leave blank if none) |
| `indexPrefix` | `string` | `"bxsearch_"` | Prefix applied to every managed index to avoid collision with non-module indices |
| `defaultLanguage` | `string` | `"en"` | Default language/analyzer when none is specified on a tag |
| `solrBasePath` | `string` | `"/solr"` | Base path of the Solr installation (only used when `engine` is `"solr"`) |

You can also override the engine at the OS/JVM level — useful in CI or Docker environments:

```bash
# Environment variable
export BX_SEARCH_ENGINE=elasticsearch

# JVM system property
-DBX_SEARCH_ENGINE=elasticsearch
```

---

## Components

This module contributes the following components to the BoxLang runtime:

- [collection](#collection-component) — Manages full-text search collections (indices)
- [index](#index-component) — Indexes documents into a search collection
- [search](#search-component) — Executes a full-text search and returns a `Query`

### Collection Component

Manages full-text search collections (indices).

| Attribute | Type | Required | Description |
| --- | --- | --- | --- |
| `action` | `string` | ✅ | `create` \| `delete` \| `list` \| `repair` \| `map` |
| `collection` | `string` | for most actions | Name of the collection |
| `name` | `string` | for `list` | Variable to receive the results (an `Array` of `Struct`) |
| `path` | `string` | no | Optional filesystem path stored as collection metadata (create only) |
| `language` | `string` | no | Analyzer language (create only, defaults to the module setting) |
| `charset` | `string` | no | Ignored — accepted for CFML compatibility |

#### Examples

```html
<--all Create a collection -->
<bx:collection action="create" collection="products" language="english" />

<--all List all collections -->
<bx:collection action="list" name="myCollections" />
<bx:dump var="#myCollections#" />

<--all Force-merge (repair) -->
<bx:collection action="repair" collection="products" />

<--all Delete -->
<bx:collection action="delete" collection="products" />
```

---

### Index Component

Indexes, updates, and removes documents.

| Attribute | Type | Required | Description |
| --- | --- | --- | --- |
| `action` | `string` | ✅ | `update` \| `delete` \| `purge` \| `refresh` |
| `collection` | `string` | ✅ | Target collection name |
| `key` | `string` | for `update`/`delete` | Document identifier; for `type="file\|url"` this is the path/URL |
| `type` | `string` | for `update` | `custom` (default) \| `file` \| `url` |
| `title` | `string` | no | Document title stored and returned in search results |
| `body` | `string` | no | Full-text body (used for `type="custom"`) |
| `urlpath` | `string` | no | URL stored as the document's URL field |
| `language` | `string` | no | Language/analyzer override |
| `custom1`–`custom4` | `string` | no | User-defined metadata fields |
| `extensions` | `string` | no | Ignored — accepted for CFML compatibility |
| `recurse` | `boolean` | no | Ignored — accepted for CFML compatibility |

#### Examples

```html
<--all Index a custom document -->
<bx:index action="update" collection="products" type="custom"
    key="prod-001"
    title="BoxLang Pro License"
    body="Annual subscription for BoxLang Pro with priority support."
    urlpath="/products/boxlang-pro"
    custom1="software"
/>

<--all Index a file attachment -->
<bx:index action="update" collection="docs" type="file"
    key="/path/to/manual.pdf"
    title="User Guide"
    urlpath="/downloads/manual.pdf"
/>

<--all Index a URL -->
<bx:index action="update" collection="docs" type="url"
    key="https://example.com/page"
    urlpath="https://example.com/page"
/>

<--all Delete a specific document -->
<bx:index action="delete" collection="products" key="prod-001" />

<--all Purge all documents from a collection -->
<bx:index action="purge" collection="products" />

<--all Refresh (flush) the index so documents are immediately searchable -->
<bx:index action="refresh" collection="products" />
```

---

### Search Component

Executes a full-text search against a collection and places the results in a CFML-compatible `Query`.

| Attribute | Type | Required | Description |
| --- | --- | --- | --- |
| `collection` | `string` | ✅ | Bare collection name to search |
| `name` | `string` | ✅ | Variable name to receive the result `Query` |
| `criteria` | `string` | no | Search expression / query string (defaults to match-all when omitted) |
| `type` | `string` | no | `simple` (default) \| `explicit` — both map to a multi-match query across all fields |
| `maxrows` | `integer` | no | Maximum number of rows to return (default: `50`) |
| `startrow` | `integer` | no | 1-based offset for pagination (default: `1`) |
| `language` | `string` | no | Language hint (reserved for future analyzer use) |
| `suggestions` | `string` | no | Ignored — accepted for CFML compatibility |

The result `Query` receives the following columns:

| Column | Type | Description |
| --- | --- | --- |
| `RANK` | `integer` | 1-based position in the result set |
| `SCORE` | `double` | Relevance score normalised to 0–100 |
| `KEY` | `varchar` | Document identifier (set via `key` at index time) |
| `TITLE` | `varchar` | Stored title field |
| `SUMMARY` | `varchar` | Stored body excerpt / summary field |
| `URL` | `varchar` | Stored urlpath field |
| `CUSTOM1`–`CUSTOM4` | `varchar` | Stored custom metadata fields |

#### Examples

```html
<--all Basic search -->
<bx:search collection="products" criteria="BoxLang" name="results" maxrows="20" startrow="1" />

<--all Iterate the result Query -->
<bx:output query="results">
    <p><a href="#results.url#">#results.title#</a> — score: #results.score#</p>
</bx:output>
```

---

## Fluent API — `SearchNew()`

`SearchNew()` returns a chainable `SearchBuilder` wired to the active search provider. Build and execute searches entirely in BoxLang code without template tags.

### Signature

```
SearchNew( [collection], [properties] ) → SearchBuilder
```

| Argument | Type | Description |
| --- | --- | --- |
| `collection` | `string` | Optional bare collection name. If omitted, call `.newSearch( collection )` before executing. |
| `properties` | `struct` | Optional raw query DSL struct; becomes the starting DSL for the builder (equivalent to `.setQuery( properties )`) |

### `SearchBuilder` Initialization

| Method | Description |
| --- | --- |
| `newSearch( collection )` / `newSearch( collection, properties )` | Set the target collection (and optionally pre-populate raw DSL). Resets all query state. |
| `reset()` | Clear all query state; retains the collection and provider. |

### `SearchBuilder` Match Methods

| Method | Description |
| --- | --- |
| `match( name, value[, boost[, options[, matchType ] ] ] )` | Add a standard `match` clause. Defaults to `must`; occurrence can be `must`, `should`, or `must_not`. |
| `mustMatch( name, value[, boost ] )` | Add a `must` (AND) match clause. |
| `mustNotMatch( name, value[, boost ] )` | Add a `must_not` match clause. |
| `shouldMatch( name, value[, boost ] )` | Add a `should` (OR) match clause. |
| `multiMatch( names, value[, boost[, type[, matchType ] ] ] )` | Search multiple fields via `multi_match` (e.g. `best_fields`, `cross_fields`). |
| `dateMatch( name, start, end[, boost[, matchType ] ] )` | Add a date range filter. Supports ISO-8601 or ES date math (e.g. `now-7d`); either bound may be `null`. |

### `SearchBuilder` Term & Wildcard

| Method | Description |
| --- | --- |
| `term( name, value[, boost[, matchType ] ] )` | Add an exact-value `term` query on keyword fields. |
| `wildcard( name, value[, boost[, matchType ] ] )` | Add a `wildcard` query; the pattern is wrapped in `*...*` automatically. |

### `SearchBuilder` Output Control

| Method | Description |
| --- | --- |
| `sort( sort[, config ] )` | Append a sort directive. Accepts `"publishDate DESC"`, `( field, "asc" )`, or a full config map. May be called multiple times. |
| `setFrom( from )` | Set the zero-based starting offset for pagination. |
| `setSize( size )` | Set the maximum documents to return per page (default: `10`). |
| `setFields( fields... )` | Restrict returned fields (replaces `_source`). |
| `addField( field )` | Append a single field to the projection list. |
| `addScriptField( name, script )` | Add a script field computed at search time. |
| `addRuntimeMapping( name, mapping )` | Add a runtime field mapping evaluated at search time. |
| `aggregation( name, options )` | Add an aggregation directive, retrievable via `SearchResult#getAggregations()`. |
| `highlight( options )` | Set highlight configuration so matching fragments are returned. |
| `collapseToField( field[, options[, includeOccurrences ] ] )` | Collapse results to the top hit per unique field value. |
| `setQuery( dsl )` | Set the raw query body, overriding all built clauses (accepts a struct or map). |

### `SearchBuilder` Request Parameters & DSL

| Method | Description |
| --- | --- |
| `param( name, value )` | Append a query-string parameter to the request URL (e.g. `version`). |
| `bodyParam( name, value )` | Append a request body parameter merged into the top-level body (e.g. `track_scores`, `min_score`). |
| `getDSL()` | Assemble and return the complete query body without executing. |
| `getDSLAsStruct()` | Return the assembled DSL as a BoxLang struct. |

### `SearchBuilder` Execution

| Method | Description |
| --- | --- |
| `execute()` | Execute the search and return the full result set. |
| `count()` | Return the matched document count (more efficient than `execute()` when only a count is needed). |
| `deleteAll()` | Delete all documents matching the current query; returns the number deleted. |
| `getTermVectors( documentId, fields[, options ] )` | Retrieve term vectors for a document in the target collection. |

### `SearchBuilder` Accessors

| Method | Description |
| --- | --- |
| `getCollection()` | The target collection name (bare, un-prefixed). |
| `getProvider()` | The backing search provider. |

### `SearchResult` Methods

| Method | Return Type | Description |
| --- | --- | --- |
| `getHits()` | `List<SearchDocument>` | The matched documents. |
| `getHitCount()` | `long` | Total number of matching documents. |
| `getAggregations()` | `Map` | Aggregation results (when aggregations were configured). |
| `getCollapsedCount()` | `long` | Count of unique values after field collapse. |
| `getCollapsedOccurrences()` | `Map` | Per-value occurrence counts after field collapse. |

### `SearchDocument` Methods

| Method | Return Type | Description |
| --- | --- | --- |
| `getId()` | `String` | The document identifier. |
| `getScore()` | `double` | The relevance score. |
| `getValue( field )` | `Object` | A stored field value by name. |

### Examples

```java
// Simple full-text search
results = SearchNew( "products" )
    .match( "title", "BoxLang" )
    .setSize( 20 )
    .execute()
    .getHits();

// Boolean search with date range, sort, and pagination
page2 = SearchNew( "articles" )
    .mustMatch( "status", "published" )
    .dateMatch( "publishDate", "now-7d", null )
    .sort( "publishDate DESC" )
    .setFrom( 10 )
    .setSize( 10 )
    .execute();

// Just count hits without fetching documents
totalHits = SearchNew( "products" )
    .mustMatch( "isActive", true )
    .count();

// Aggregations
results = SearchNew( "products" )
    .match( "category", "languages" )
    .aggregation( "byBrand", { "terms": { "field": "brand" } } )
    .execute();
writeDump( results.getAggregations() );

// Raw DSL passthrough
results = SearchNew( "products", {
    "query": {
        "bool": {
            "must": [ { "match": { "body": "BoxLang" } } ],
            "filter": [ { "term": { "custom1": "software" } } ]
        }
    }
} ).setSize( 10 ).execute();
```

---

## Solr Provider

Set `engine: "solr"` to target an **Apache Solr 9.x** instance (standalone mode). Each CFML collection maps to a Solr core created with the schemaless `_default` configset.

```json
"bx-search": {
    "settings": {
        "engine": "solr",
        "host": "localhost",
        "port": 8983,
        "protocol": "http",
        "solrBasePath": "/solr",
        "indexPrefix": "bxsearch_"
    }
}
```

> ℹ️ Solr's default port is `8983` (not `9200`). Set `port` accordingly, or pass `-DBX_SEARCH_PORT=8983`.

**Supported with Solr:**

- `<bx:collection action="create/delete/repair/list">` — core management via the Core Admin API
- `<bx:index action="update" type="custom">` — JSON document indexing
- `<bx:index action="update" type="file|url">` — Apache Tika extraction (text, PDF, Office, and images via EXIF metadata)
- `<bx:index action="delete/purge/refresh">`
- `<bx:search>` with `criteria`, `maxrows`, `startrow`

**Not supported with Solr:**

- `SearchNew()` / `SearchBuilder` — the fluent API emits Elasticsearch query DSL that has no Solr equivalent. Use `<bx:search>` instead.
- `cfcollection action="map"` — directory mapping is an Elasticsearch/Verity concept with no Solr equivalent.
- Solr 8.x and earlier (rejected at startup with a clear error).

---

## Supported Languages / Analyzers

The following language values are accepted on `<bx:collection>` and `<bx:index>`:

| Value | Analyzer |
| --- | --- |
| `en`, `english` | `english` |
| `fr`, `french` | `french` |
| `de`, `german` | `german` |
| `es`, `spanish` | `spanish` |
| `it`, `italian` | `italian` |
| `pt`, `portuguese` | `portuguese` |
| `nl`, `dutch` | `dutch` |
| `sv`, `swedish` | `swedish` |
| _(anything else)_ | `standard` |

---

## CFML Compatibility

This module provides compatibility with CFML search tags:

- ✅ `cfcollection` → `bx:collection`
- ✅ `cfindex` → `bx:index`
- ✅ `cfsearch` → `bx:search`

Migration from ColdFusion requires only prefix changes (`cf` → `bx`).

---

## Technical Requirements

- BoxLang Runtime 1.0.0+
- Java 21+

---

## Support and Documentation

- **Documentation**: [https://boxlang.ortusbooks.com](https://boxlang.ortusbooks.com)
- **Issues**: [https://ortussolutions.atlassian.net/jira/software/c/projects/BLMODULES/issues](https://ortussolutions.atlassian.net/jira/software/c/projects/BLMODULES/issues)
- **Community**: [https://community.ortussolutions.com](https://community.ortussolutions.com)

---

## 📎 Related Modules

{% content-ref url="bx-meilisearch/" %}
[bx-meilisearch](bx-meilisearch/)
{% endcontent-ref %}

{% content-ref url="bx-plus/" %}
[bx-plus](bx-plus/)
{% endcontent-ref %}

***

Return to the [Modules Overview](./).
