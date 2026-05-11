---
description: Add native support for the Meilisearch search engine in your BoxLang applications with a fluent, BoxLang-native API wrapper.
icon: magnifying-glass
---

# Meilisearch +

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://ww.boxlang.io/plans) but can be installed in conjunction with the [`bx-plus` Module](../bx-plus/) with a limited trial.
{% endhint %}

The BoxLang Meilisearch module adds native access to the fast, lightweight [Meilisearch](https://www.meilisearch.com/) search engine. It provides a fluent, BoxLang-native wrapper around the Meilisearch HTTP API so you can create indexes, manage documents, run searches, and monitor async tasks from your BoxLang code.

## 🔎 What Is Meilisearch?

Meilisearch is a lightning-fast, open-source search engine built for instant, relevant full-text search. It is designed to deliver search-as-you-type experiences with typo tolerance, filtering, faceting, and ranking, while remaining simple to deploy and integrate.

This makes it a strong fit for applications that need responsive search across catalogs, content libraries, knowledge bases, internal tools, or customer-facing discovery workflows.

## ⚡ Key Features

### Fast Search Experiences

Meilisearch is optimized for low-latency, search-as-you-type interactions that feel immediate to end users.

### Typo Tolerance and Ranking

It can return useful results even when queries are misspelled, while also applying relevance-based ranking to improve result quality.

### Filtering and Faceting

You can narrow result sets using filters and build faceted search experiences for categories, tags, status values, or other indexed attributes.

### BoxLang-Native Fluent API

The module exposes a fluent DSL for Meilisearch operations, making chained, readable calls easy to write and maintain.

### Index and Document Management

The wrapper supports common lifecycle operations such as creating indexes, adding or updating documents, deleting content, and retrieving statistics.

### Async Task Tracking

Many write operations return task objects so your application can inspect progress and react to asynchronous indexing work.

## 🚀 Quick Example

```js
// Create an index
meilisearch()
		.index( "books" )
		.create( "id" )

// Add documents
task = meilisearch()
		.index( "books" )
		.documents()
		.add([
				{ id: 1, title: "BoxLang in Action", author: "Ortus" },
				{ id: 2, title: "Search-Driven Apps", author: "Jane Doe" }
		])
		.orReplace()

// Run a search
results = meilisearch()
		.index( "books" )
		.search( "boxlang" )
		.limit( 10 )
		.send()
```

## 💡 Use Cases

### Site Search

Add fast, typo-tolerant search to documentation sites, content portals, blogs, and marketing properties.

### Product Catalog Search

Support filtered product discovery across categories, brands, pricing, and availability.

### Knowledge Bases and Internal Tools

Index internal documentation, tickets, procedures, or support content for quick retrieval.

### Application Search Workflows

Enable search-driven dashboards, admin tools, or user-facing experiences where indexed records need to be queried quickly.

### Search Prototypes and MVPs

Meilisearch is lightweight enough for teams that want a straightforward path to shipping search without adopting a larger search platform.

## 🔧 Requirements

- BoxLang 1.0.0+
- A running Meilisearch instance reachable over HTTP or HTTPS
- A Meilisearch master key or API key for authenticated requests
- Java 21+

## 📦 Installation

Install the module using the standard BoxLang module workflow:

```bash
# For Operating Systems using our Quick Installer.
install-bx-module bx-meilisearch

# Using CommandBox to install for web servers.
box install bx-meilisearch
```

You can configure the module with environment variables:

```bash
export MEILISEARCH_URL=http://localhost:7700
export MEILISEARCH_MASTER_KEY=your-master-key
```

bx-meilisearch will auto-configure using these environment variables, or you can hardcode the values in `boxlang.json`:

```json
{
    "modules": {
        "meilisearch": {
            "enabled": true,
            "settings": {
                "url"      : "http://localhost:7700",
                "masterKey": "your-master-key"
            }
        }
    }
}
```

## 📖 API Documentation

For endpoint coverage and wrapper usage patterns, see the [API Documentation](/boxlang-framework/boxlang-plus/modules/bx-meilisearch/reference/fluent-api/README.md) section.

## 📚 Built-In Function Reference

For generated reference documentation covering the module's built-in functions, see the [Built-In Function Reference](/boxlang-framework/boxlang-plus/modules/bx-meilisearch/reference/built-in-functions/README.md).

