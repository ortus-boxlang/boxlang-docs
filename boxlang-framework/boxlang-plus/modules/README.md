---
description: >-
  Premium BoxLang+ modules providing extended integration, data handling, and
  operational capabilities.
icon: puzzle
---

# Modules Overview

BoxLang+/Starter includes a curated set of modules that extend the platform with integration points, productivity accelerators, and enterprise-grade features. Each module is versioned independently and installed on demand.

## 🔍 Module Index

| Module | Purpose |
| --- | --- |
| [`bx-aws-secrets`](bx-aws-secrets/) | AWS Secrets Manager provider for `getSystemSetting()` with the `aws.` namespace. |
| [`bx-couchbase`](bx-couchbase/) | Distributed caching and NoSQL document storage via Couchbase. |
| [`bx-csv`](bx-csv/) | Streaming CSV parsing and generation for large datasets. |
| [`bx-ldap`](bx-ldap/) | Full-featured LDAP directory access for BoxLang applications. |
| [`bx-mcp`](bx-mcp/) | Model Context Protocol server for runtime diagnostics, introspection, and operational automation. |
| [`bx-meilisearch`](bx-meilisearch/) | [Meilisearch](https://www.meilisearch.com/) integration for fast full-text search in BoxLang applications. |
| [`bx-pdf`](bx-plus-pdf/) | PDF generation and manipulation for documents, reports, and forms, including [licensed functionality](bx-plus-pdf/). |
| [`bx-plus`](bx-plus/) | Subscription bootstrap, entitlement validation, and shared utilities. |
| [`bx-redis`](bx-redis/) | Redis-backed caching, data structures, and pub/sub messaging. |
| [`bx-rest-compat`](rest-compat-+/) | REST component compatibility and routing translation for legacy framework-less REST architectures. |
| [`bx-soap-compat`](soap-compat-+.md) | SOAP compatibility layer for generating, parsing, and communicating with web services. |
| [`bx-spreadsheet`](bx-spreadsheet/) | Read, write, and style spreadsheet documents (XLSX). |

## 🚀 Installation Pattern

All premium modules follow a consistent installation workflow using either CommandBox / BoxLang CLI. Our recommended approach is CommandBox as it takes care of all dependencies.

### Via CommandBox CLI

```bash
# Install bx-plus as a dependency for license management and the target module.
box install <module-name>
```

### Via BoxLang OS Binary

```bash
# Install bx-plus module first to enable license management
install-bx-module bx-plus
# Then install other modules
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

{% content-ref url="bx-aws-secrets/" %}
[bx-aws-secrets](bx-aws-secrets/)
{% endcontent-ref %}

{% content-ref url="bx-couchbase/" %}
[bx-couchbase](bx-couchbase/)
{% endcontent-ref %}

{% content-ref url="bx-ldap/" %}
[bx-ldap](bx-ldap/)
{% endcontent-ref %}

{% content-ref url="bx-mcp/" %}
[bx-mcp](bx-mcp/)
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

{% content-ref url="bx-meilisearch/" %}
[bx-meilisearch](bx-meilisearch/)
{% endcontent-ref %}

## 🛡 Reliability & Performance

Modules are tested against real-world workloads and evolve with feedback from production adopters. Performance-sensitive modules (Redis, CSV, Spreadsheet) emphasize streaming, connection pooling, and memory-efficient data structures.

## 🔄 Versioning & Compatibility

* Semantic versioning (MAJOR.MINOR.PATCH)
* Changelogs published per release
* Compatibility matrix maintained for BoxLang runtime versions

## 📣 Feedback Loop

Need a new integration or capability? Reach out through official support channels or community discussions. Prioritized enhancements are often driven by real use cases.
