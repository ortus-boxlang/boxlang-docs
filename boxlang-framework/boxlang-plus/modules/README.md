---
description: >-
  Premium BoxLang+ modules providing extended integration, data handling, and
  operational capabilities.
icon: puzzle
---

# Modules Overview

BoxLang+ includes a curated set of modules that extend the platform with integration points, productivity accelerators, and enterprise-grade features. Each module is versioned independently and installed on demand.

## 🔍 Module Index

| Module                              | Purpose                                                                                                                                                                     | Quick Install                |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| [`bx-csv`](bx-csv/)               | Streaming CSV parsing & generation for large datasets                                                                                                                       | `box install bx-csv`         |
| [`bx-couchbase`](bx-couchbase/)     | <p><strong>In Development</strong><br>Distributed caching &#x26; NoSQL document storage via Couchbase</p>                                                                   | `box install bx-couchbase`   |
| [`bx-ldap`](bx-ldap/)               | A comprehensive LDAP module for BoxLang that brings full-featured LDAP directory access to your applications!                                                               | `box install bx-ldap`        |
| [`bx-plus`](bx-plus/)               | Subscription bootstrap, entitlement validation, shared utilities                                                                                                            | `box install bx-plus`        |
| [`bx-pdf`](bx-plus-pdf/)          | <p><br>PDF generation and manipulation for documents, reports, and forms. This module provides free-tier as well as <a href="bx-plus-pdf.md">licensed functionality</a></p> | `box install bx-pdf`         |
| [`bx-redis`](bx-redis/)             | High-performance Redis-backed caching, data structures, pub/sub                                                                                                             | `box install bx-redis`       |
| [`bx-spreadsheet`](bx-spreadsheet/) | Read, write, style spreadsheet documents (XLSX)                                                                                                                             | `box install bx-spreadsheet` |
| [`bx-soap-compat`](soap-compat-+.md) | SOAP compatibility layer for generating, parsing, and communicating with web services.                                                                                                | `box install bx-soap-compat` |
| [`bx-rest-compat`](rest-compat-+/) | REST component compatibility and routing translation layer for running legacy framework-less REST architectures.                                                              | `box install bx-rest-compat` |
| [`bx-meilisearch`](bx-meilisearch/) | [Meilisearch](https://www.meilisearch.com/) integration for fast, full-text search capabilities within BoxLang applications.                                                              | `box install bx-meilisearch` |

## 🚀 Installation Pattern

All premium modules follow a consistent installation workflow using either CommandBox or BoxLang CLI:

### Via CommandBox CLI

```bash
box install <module-name>
```

### Via BoxLang OS Binary

```bash
install-bx-module <module-name>
```

After installation, modules register themselves automatically or provide a simple activation step described in their documentation.

## 🧪 Common Usage Flow

1. Install module.
2. Configure via `boxlang.json`, environment variables, or runtime API. Each module can have different configuration needs; refer to individual module docs for specifics.
3. Inject or call provided services/components.
4. Handle errors using standard exception management patterns.

## 📁 Module Docs

{% content-ref url="bx-csv.md" %}
[bx-csv.md](bx-csv.md)
{% endcontent-ref %}

{% content-ref url="bx-couchbase/" %}
[bx-couchbase](bx-couchbase/)
{% endcontent-ref %}

{% content-ref url="bx-ldap/" %}
[bx-ldap](bx-ldap/)
{% endcontent-ref %}

{% content-ref url="bx-plus/" %}
[bx-plus](bx-plus/)
{% endcontent-ref %}

{% content-ref url="bx-plus-pdf.md" %}
[bx-plus-pdf.md](bx-plus-pdf.md)
{% endcontent-ref %}

{% content-ref url="bx-redis/" %}
[bx-redis](bx-redis/)
{% endcontent-ref %}

{% content-ref url="bx-spreadsheet/" %}
[bx-spreadsheet](bx-spreadsheet/)
{% endcontent-ref %}

{% content-ref url="soap-compat-+.md" %}
[soap-compat-+.md](soap-compat-+.md)
{% endcontent-ref %}

{% content-ref url="rest-compat-+/" %}
[rest-compat-+](rest-compat-+/)
{% endcontent-ref %}

## 🛡 Reliability & Performance

Modules are tested against real-world workloads and evolve with feedback from production adopters. Performance-sensitive modules (Redis, CSV, Spreadsheet) emphasize streaming, connection pooling, and memory-efficient data structures.

## 🔄 Versioning & Compatibility

* Semantic versioning (MAJOR.MINOR.PATCH)
* Changelogs published per release
* Compatibility matrix maintained for BoxLang runtime versions

## 📣 Feedback Loop

Need a new integration or capability? Reach out through official support channels or community discussions. Prioritized enhancements are often driven by real use cases.
