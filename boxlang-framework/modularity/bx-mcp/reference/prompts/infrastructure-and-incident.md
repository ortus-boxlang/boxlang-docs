---
icon: siren
description: Pre-built prompts for web server diagnostics, route performance analysis, incident triage, error spike response, and post-incident review.
---

# 🏗️ Infrastructure & Incident Prompts

## Web Server & Routing

| Prompt | Description | Arguments |
| --- | --- | --- |
| `web_server_diagnostics` | Deep-dive Undertow diagnostics: worker thread pool saturation, IO pool, active/queued requests, listener stats, WebSocket connections | — |
| `slow_request_analysis` | Identify slow inbound HTTP requests: correlates captured samples with per-route metrics to surface worst-performing endpoints | `limit` *(optional, default: 50)* |
| `route_performance_analysis` | Per-route HTTP performance: identify slowest and highest-traffic endpoints, error rates, prioritized optimization backlog | `sortBy` *(optional, default: avgLatency)*, `limit` *(optional, default: 20)* |

## Incident Response

| Prompt | Description | Arguments |
| --- | --- | --- |
| `incident_triage` | Rapid incident triage: scan errors, threads, memory, web server, datasources, and executors to identify what's broken right now | — |
| `error_spike_response` | Error spike response: correlate timing, identify blast radius, and recommend containment actions | `keyword` *(optional)* |
| `cascade_failure_diagnosis` | Cascade failure diagnosis: trace failure chains across subsystems (datasource timeout → thread saturation → request queuing) | — |
| `rollback_decision` | Rollback decision: structured go/no-go comparison of current state vs. deployment baseline | `expectedModules` *(optional)* |
| `post_incident_review` | Post-incident review: collect timeline, identify impact, determine root cause, and generate improvement actions | `keyword` *(optional)* |
