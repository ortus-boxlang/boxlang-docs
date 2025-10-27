---
description: >-
  Premium BoxLang+ modules providing extended integration, data handling, and
  operational capabilities.
icon: puzzle
---

# Modules Overview

BoxLang+ includes a curated set of modules that extend the platform with integration points, productivity accelerators, and enterprise-grade features. Each module is versioned independently and installed on demand.

## 🔍 Module Index

| Module | Purpose | Quick Install |
|--------|---------|---------------|
| `bx-csv` | Streaming CSV parsing & generation for large datasets | `box install bx-csv` |
| `bx-couchbase` | **In Development**<br>Distributed caching & NoSQL document storage via Couchbase | `box install bx-couchbase` |
| `bx-ldap` | A comprehensive LDAP module for BoxLang that brings full-featured LDAP directory access to your applications! | `box install bx-ldap` |
| `bx-plus` | Subscription bootstrap, entitlement validation, shared utilities | `box install bx-plus` |
| `bx-plus-pdf` | **In Development**<br>PDF generation and manipulation for documents, reports, and forms | `box install bx-plus-pdf` |
| `bx-redis` | High-performance Redis-backed caching, data structures, pub/sub | `box install bx-redis` |
| `bx-spreadsheet` | Read, write, style spreadsheet documents (XLSX) | `box install bx-spreadsheet` |

## 🚀 Installation Pattern

All premium modules follow a consistent installation workflow using either CommandBox or BoxLang CLI:

### Via CommandBox

```bash
box install <module-name>
```

### Via BoxLang

```bash
install-bx-module <module-name>
```

After installation, modules register themselves automatically or provide a simple activation step described in their documentation.

## 🧪 Common Usage Flow

1. Install module with CommandBox.
2. Configure via `boxlang.json`, environment variables, or runtime API.
3. Inject or call provided services/components.
4. Handle errors using standard exception management patterns.

## 📁 Module Docs

{% content-ref url="bx-csv.md" %}
[bx-csv.md](bx-csv.md)
{% endcontent-ref %}

{% content-ref url="bx-couchbase.md" %}
[bx-couchbase.md](bx-couchbase.md)
{% endcontent-ref %}

{% content-ref url="bx-ldap.md" %}
[bx-ldap.md](bx-ldap.md)
{% endcontent-ref %}

{% content-ref url="bx-plus.md" %}
[bx-plus.md](bx-plus.md)
{% endcontent-ref %}

{% content-ref url="bx-plus-pdf.md" %}
[bx-plus-pdf.md](bx-plus-pdf.md)
{% endcontent-ref %}

{% content-ref url="bx-redis.md" %}
[bx-redis.md](bx-redis.md)
{% endcontent-ref %}

{% content-ref url="bx-spreadsheet.md" %}
[bx-spreadsheet.md](bx-spreadsheet.md)
{% endcontent-ref %}

## 🛡 Reliability & Performance

Modules are tested against real-world workloads and evolve with feedback from production adopters. Performance-sensitive modules (Redis, CSV, Spreadsheet) emphasize streaming, connection pooling, and memory-efficient data structures.

## 🔄 Versioning & Compatibility

* Semantic versioning (MAJOR.MINOR.PATCH)
* Changelogs published per release
* Compatibility matrix maintained for BoxLang runtime versions

## 📣 Feedback Loop

Need a new integration or capability? Reach out through official support channels or community discussions. Prioritized enhancements are often driven by real use cases.
