---
description: Rapid incident response workflows — triage, error spikes, cascade failures, rollback decisions, and post-mortems.
icon: siren
---

# 🚨 Incident Response

The `bx-mcp` module provides pre-built prompts and tools designed for structured incident response. This guide covers the recommended workflows for common incident scenarios.

---

## 📋 Incident Response Prompts

The module ships with dedicated prompts for incident response. Each prompt instructs an AI agent on which tools to call and in what order:

| Prompt | When to Use |
| --- | --- |
| `incident_triage` | Something is broken — identify what's wrong right now |
| `error_spike_response` | Sudden increase in errors — correlate timing and identify blast radius |
| `cascade_failure_diagnosis` | Multiple subsystems failing — trace the failure chain |
| `rollback_decision` | Deciding whether to rollback — structured go/no-go analysis |
| `post_incident_review` | After resolution — timeline, root cause, and improvement actions |

---

## 🚑 5-Minute Incident Triage

When an incident is reported, follow this rapid triage workflow:

### Step 1: System Health Overview (30 seconds)

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"system_get_health","arguments":{}},"id":"1"}' | jq '.result.content[0].text | fromjson'
```

Look for `critical` or `warning` statuses. The aggregator reports issues across all subsystems.

### Step 2: Check Recent Errors (30 seconds)

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"logging_search_entries","arguments":{"keyword":"error|exception|fatal","limit":20}},"id":"2"}' | jq '.result.content[0].text | fromjson'
```

### Step 3: Check JVM Health (30 seconds)

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_memory_info","arguments":{}},"id":"3"}' | jq '.result.content[0].text | fromjson'

# Check for blocked threads
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_thread_info","arguments":{}},"id":"4"}' | jq '.result.content[0].text | fromjson'
```

### Step 4: Check Web Server (30 seconds)

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"undertow_get_health","arguments":{}},"id":"5"}' | jq '.result.content[0].text | fromjson'
```

### Step 5: Check Data Layer (30 seconds)

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"datasource_get_health","arguments":{}},"id":"6"}' | jq '.result.content[0].text | fromjson'

curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"executor_get_health","arguments":{}},"id":"7"}' | jq '.result.content[0].text | fromjson'
```

**Total: ~3 minutes** to identify the most common failure modes.

---

## 📈 Error Spike Response

When you detect a sudden increase in error rates:

### 1. Correlate Timing

```bash
# Get recent slow requests with timestamps
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"requests_get_slow_requests","arguments":{"limit":50}},"id":"1"}'

# Get recent log errors with timestamps
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"logging_search_entries","arguments":{"keyword":"error","limit":50}},"id":"2"}'
```

### 2. Identify Blast Radius

```bash
# Check which routes are failing
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"routes_get_all","arguments":{"sortBy":"errorRate","limit":10}},"id":"3"}'
```

### 3. Check Downstream Dependencies

```bash
# Look for failing outbound HTTP/SOAP calls
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"slow_http_get_stats","arguments":{}},"id":"4"}'
```

---

## 🔗 Cascade Failure Diagnosis

Cascade failures propagate from one subsystem to others. Common chains:

```
Datasource timeout → thread pool saturation → request queuing → web server overload
```

### Trace the Chain

**1. Check the web server first** — it's usually where the symptom is visible:

```bash
curl -s ... -d '{"method":"tools/call","params":{"name":"undertow_get_stats","arguments":{}}}'
```

Look for high queue depth, worker saturation, or connection backlogs.

**2. Check executor pools** — thread starvation often follows:

```bash
curl -s ... -d '{"method":"tools/call","params":{"name":"executor_get_all","arguments":{}}}'
```

Look for high queue buildup or rejected tasks.

**3. Check datasources** — pool exhaustion can cascade to threads:

```bash
curl -s ... -d '{"method":"tools/call","params":{"name":"datasource_get_pool_metrics","arguments":{}}}'
```

Look for high utilization, waiting threads, or long acquisition times.

**4. Check for deadlocks** — the root cause might be locking:

```bash
curl -s ... -d '{"method":"tools/call","params":{"name":"jvm_get_deadlocks","arguments":{}}}'
```

**5. Get a full thread dump** to confirm the cascade:

```bash
curl -s ... -d '{"method":"tools/call","params":{"name":"jvm_get_thread_dump","arguments":{}}}'
```

---

## 🔄 Rollback Decision Guide

When considering a rollback after a deployment, use this structured approach:

### 1. Current State Assessment

```bash
# What's running now
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"runtime_get_info","arguments":{}},"id":"1"}'

# Which modules are loaded
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"module_get_all","arguments":{}},"id":"2"}'
```

### 2. Health Comparison

Compare current health against known baseline metrics. Key indicators:

| Metric | Healthy Baseline | Warning | Critical |
| --- | --- | --- | --- |
| Heap usage | < 70% | 70-85% | > 85% |
| Active threads | < 50% pool | 50-80% | > 80% |
| Datasource utilization | < 60% | 60-80% | > 80% |
| Error rate | < 1% | 1-5% | > 5% |

### 3. Rollback Decision Matrix

| Condition | Action |
| --- | --- |
| Critical health issues + recent deployment | **Rollback immediately** |
| Warning-level issues + new features deployed | Consider rollback, or hotfix if root cause is known |
| Healthy + minor degradation | Monitor, investigate non-critical path |
| Healthy + all metrics normal | No rollback needed |

---

## 📝 Post-Incident Review

After resolving an incident, collect the following data for a post-mortem:

### Timeline Data

```bash
# Check logging for the incident period
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"logging_get_last_error","arguments":{}},"id":"1"}'

# Review slow requests during the window
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"requests_get_slow_requests","arguments":{"limit":100}},"id":"2"}'
```

### Impact Assessment

```bash
# Route performance to determine which endpoints were affected
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"routes_get_all","arguments":{"sortBy":"errorRate","limit":20}},"id":"3"}'
```

### Generate Improvement Actions

Use the captured data to identify:
- **Monitoring gaps** — Were there warning signs that were missed?
- **Runbook improvements** — What manual steps can be automated?
- **Configuration changes** — Should thresholds be adjusted?
- **Architecture changes** — What subsystem changes would prevent recurrence?

---

## 📚 Next Steps

- [Operations & Monitoring](operations-and-monitoring.md) — Proactive health checks and monitoring
- [Data Layer Diagnostics](data-layer-diagnostics.md) — Cache, datasource, and SQL diagnostics
- [MCP Prompts Reference](reference/prompts/README.md) — Pre-built diagnostic prompts including all incident response prompts
