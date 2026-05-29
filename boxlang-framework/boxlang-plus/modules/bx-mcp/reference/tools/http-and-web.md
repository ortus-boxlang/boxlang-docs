---
icon: globe
description: HTTP client, slow HTTP/SOAP, request diagnostics, route metrics, and Undertow web server tools.
---

# 🌐 HTTP & Web Tools

This page covers tools for HTTP/SOAP client introspection (`HttpTools`), slow outbound call capture (`SlowHttpTools`), slow request diagnostics (`RequestsTools`), route metrics (`RouteMetricsTools`), and Undertow web server diagnostics (`UndertowTools`).

---

## HTTP & SOAP Clients — `HttpTools`

| Tool | Description |
| --- | --- |
| `http_get_client_count` | Number of active HTTP clients |
| `http_get_client_names` | HTTP client keys |
| `http_get_clients` | Per-client stats: connection counts, request counts, error rates |
| `http_get_soap_clients` | Per-WSDL SOAP client usage details |
| `http_get_executor` | HTTP executor thread pool status and configuration |
| `http_get_service_summary` | Consolidated HTTP service summary |

---

## HTTP/SOAP Diagnostics — `SlowHttpTools`

| Tool | Description |
| --- | --- |
| `slow_http_get_calls` | Recent captured slow outbound HTTP/SOAP call samples with optional limit and since filter |
| `slow_http_get_stats` | Aggregate slow call statistics by destination host (count, avg latency, max latency) |
| `slow_http_clear` | Clear all captured slow-call samples and statistics |
| `slow_http_get_config` | Current slow HTTP collector configuration |
| `slow_http_set_config` | Update slow HTTP collector configuration at runtime |

---

## Request Diagnostics — `RequestsTools`

| Tool | Description |
| --- | --- |
| `requests_get_slow_requests` | Recent captured slow request samples with optional limit and since filter |
| `requests_get_stats` | Aggregate slow-request statistics and collector configuration |
| `requests_get_config` | Current slow request collector configuration |
| `requests_set_config` | Update slow request collector threshold, buffer size, and stack capture setting at runtime |
| `requests_clear` | Clear all captured slow-request samples and counters |

---

## Route Metrics — `RouteMetricsTools`

| Tool | Description |
| --- | --- |
| `routes_get_all` | Per-route request metrics sorted by count, error rate, p99, or last seen time |
| `routes_get_route` | Detailed metrics for a single route by its exact key (e.g. `GET /api/users/{id}`) |
| `routes_get_summary` | Aggregate summary: total requests, error rate, route count, top-5 slowest routes by p99 |
| `routes_get_config` | Current route metrics collector configuration |
| `routes_set_config` | Update route metrics collector config at runtime (maxRoutes, normalizePathParams) |
| `routes_clear` | Clear all accumulated route metrics data |

---

## Web Server (Undertow) — `UndertowTools`

| Tool | Description |
| --- | --- |
| `undertow_get_stats` | Undertow web server statistics: worker pool (core/max/current/busy/queue), IO pool, listener connection/request/error counts, active requests, WebSocket connections |
| `undertow_get_health` | Structured health assessment: status, score, worker saturation, queue depth, listener error rates with issue codes |

These tools auto-detect the deployment mode — BoxLang MiniServer, Runwar/CommandBox, or generic Undertow via JMX — and return rich metrics regardless of which Undertow-based server is running. On non-Undertow deployments, the tools return `{ "available": false }`.
