---
description: >-
  Premium BoxLang+ modules providing extended integration, data handling, and
  operational capabilities.
icon: puzzle
---

# Modules Overview

BoxLang+ includes a curated set of modules that extend the platform with integration points, productivity accelerators, and enterprise-grade features. Each module is versioned independently and installed on demand.

## 🔍 Module Index

<table><thead><tr><th width="155">Module</th><th>Purpose</th><th>Quick Install</th></tr></thead><tbody><tr><td><code>bx-csv</code></td><td>Streaming CSV parsing &#x26; generation for large datasets</td><td><code>box install bx-csv</code></td></tr><tr><td><code>bx-couchbase</code><br><br></td><td><strong>In Development</strong><br>Distributed caching &#x26; NoSQL document storage via Couchbase</td><td><code>box install bx-couchbase</code></td></tr><tr><td><code>bx-ldap</code></td><td>A comprehensive LDAP module for BoxLang that brings full-featured LDAP directory access to your applications!</td><td><code>box install bx-ldap</code></td></tr><tr><td><code>bx-plus</code></td><td>Subscription bootstrap, entitlement validation, shared utilities</td><td><code>box install bx-plus</code></td></tr><tr><td><code>bx-plus-pdf</code></td><td><strong>In Development</strong><br>PDF generation and manipulation for documents, reports, and forms</td><td><code>box install bx-plus-pdf</code></td></tr><tr><td><code>bx-redis</code></td><td>High-performance Redis-backed caching, data structures, pub/sub</td><td><code>box install bx-redis</code></td></tr><tr><td><code>bx-spreadsheet</code></td><td>Read, write, style spreadsheet documents (XLSX)</td><td><code>box install bx-spreadsheet</code></td></tr></tbody></table>

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

{% content-ref url="bx-plus.md" %}
[bx-plus.md](bx-plus.md)
{% endcontent-ref %}

{% content-ref url="broken-reference" %}
[Broken link](broken-reference)
{% endcontent-ref %}

{% content-ref url="broken-reference" %}
[Broken link](broken-reference)
{% endcontent-ref %}

{% content-ref url="bx-csv.md" %}
[bx-csv.md](bx-csv.md)
{% endcontent-ref %}

{% content-ref url="bx-couchbase.md" %}
[bx-couchbase.md](bx-couchbase.md)
{% endcontent-ref %}

{% content-ref url="bx-plus-pdf.md" %}
[bx-plus-pdf.md](bx-plus-pdf.md)
{% endcontent-ref %}

## 🛡 Reliability & Performance

Modules are tested against real-world workloads and evolve with feedback from production adopters. Performance-sensitive modules (Redis, CSV, Spreadsheet) emphasize streaming, connection pooling, and memory-efficient data structures.

## 🔄 Versioning & Compatibility

* Semantic versioning (MAJOR.MINOR.PATCH)
* Changelogs published per release
* Compatibility matrix maintained for BoxLang runtime versions

## 📣 Feedback Loop

Need a new integration or capability? Reach out through official support channels or community discussions. Prioritized enhancements are often driven by real use cases.

***

Select a module above to dive deeper.
