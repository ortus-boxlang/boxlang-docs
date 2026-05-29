---
icon: tools
description: Complete catalog of all 154 MCP tools organized by domain for BoxLang runtime diagnostics and management.
---

# 🧰 MCP Tools

The `bx-mcp` module exposes **154 MCP tools** across **17 runtime domains**. Each tool is an `@mcpTool` annotated method discovered automatically via classpath scanning.

Tools are organized into the following domain pages:

| Domain | Page | Tools |
| --- | --- | --- |
| Runtime & JVM | [Runtime & Platform](runtime-and-platform.md) | 30 |
| Caches, Datasources, SQL | [Data Layer](data-layer.md) | 29 |
| HTTP Clients, Slow HTTP, Requests, Routes, Web Server | [HTTP & Web](http-and-web.md) | 24 |
| Executors, Schedulers, Modules, Interceptors, Applications, Logging, Watchers | [Operations](operations.md) | 69 |
| Performance, System Health | [Performance & Health](performance-and-health.md) | 2 |

---

## Calling a Tool

All tools are called via JSON-RPC 2.0 over HTTP POST:

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"tool_name","arguments":{}},"id":"1"}'
```

See the [Protocol Reference](../protocol.md) for complete details.

---

## Tool Naming Convention

All tools follow the `domain_action_description` naming convention:

- `runtime_get_info` — Get BoxLang runtime information
- `cache_get_health` — Get cache health assessment
- `jvm_get_memory_info` — Get JVM memory information

This makes it easy to discover tools by domain and understand their purpose at a glance.
