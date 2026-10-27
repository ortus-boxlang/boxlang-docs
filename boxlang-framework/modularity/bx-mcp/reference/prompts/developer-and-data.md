---
icon: code
description: Pre-built prompts for BIF/component discovery, application debugging, cache analysis, datasource health, and slow SQL/HTTP diagnosis.
---

# 💻 Developer & Data Layer Prompts

## Developer

| Prompt | Description | Arguments |
| --- | --- | --- |
| `bif_component_discovery` | Explore available BIFs and components; search by keyword | `keyword` *(optional)* |
| `application_debug_assistant` | Targeted debug assistant for a specific application: lifecycle state, log errors, datasource health, cache stats, thread context | `appName` *(required)* |

## Data Layer

| Prompt | Description | Arguments |
| --- | --- | --- |
| `analyze_cache_performance` | Cache hit rates, eviction patterns, sizing; optionally focus on a named cache | `cacheName` *(optional)* |
| `datasource_health_report` | Datasource connectivity, connection pool utilization, configuration audit | — |
| `slow_sql_diagnosis` | Identify and diagnose slow SQL queries: patterns, datasource hotspots, and tuning recommendations | `limit` *(optional, default: 50)* |
| `slow_http_diagnosis` | Identify and diagnose slow outbound HTTP/SOAP calls: destination host hotspots, error-prone integrations, timeout and connection pool tuning recommendations | `limit` *(optional, default: 50)* |
