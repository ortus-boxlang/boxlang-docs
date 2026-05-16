---
description: >-
  Model Context Protocol server module for BoxLang runtime diagnostics,
  introspection, and operational automation.
icon: bot
---

# MCP +

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://boxlang.io/plans). It requires the `bx-plus` and `bx-ai` modules.
{% endhint %}

The `bx-mcp` module exposes a production-ready MCP server for BoxLang so MCP-capable clients (AI agents, IDE assistants, automation tools) can inspect and operate a live runtime safely.

When enabled, the module auto-registers a `boxlang` MCP server and exposes an HTTP endpoint at `/~bxmcp/boxlang.bxm`.

## 🚀 Installation

### Via CommandBox

```bash
box install bx-plus,bx-ai,bx-mcp
```

### Via BoxLang OS Binary

```bash
install-bx-module bx-plus bx-ai bx-mcp
```

## ⚙️ Configuration

Configure `bx-mcp` in your `boxlang.json` under `modules.bxmcp.settings`:

```json
{
  "modules": {
    "bxmcp": {
      "enabled": true,
      "settings": {
        "enabled": true,
        "authToken": "FILL_THIS_OUT_ALWAYS",
        "allowedIPs": ["127.0.0.1"],
        "corsAllowedOrigins": [],
        "enableStats": true,
        "maxRequestBodySize": 0,
        "includedTools": ["*"],
        "excludedTools": []
      }
    }
  }
}
```

### Settings Reference

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | `true` | Master switch for MCP server registration. |
| `authToken` | string | `""` | Bearer token required by clients. |
| `allowedIPs` | array | `["127.0.0.1"]` | IP allowlist with IP/CIDR support. |
| `corsAllowedOrigins` | array | `[]` | CORS allowlist with wildcard support. |
| `enableStats` | boolean | `true` | Enables server and tool usage statistics. |
| `maxRequestBodySize` | numeric | `0` | Request body limit in bytes, `0` means unlimited. |
| `includedTools` | array | `["*"]` | Tool whitelist. |
| `excludedTools` | array | `[]` | Tool blacklist applied after whitelist. |

{% hint style="warning" %}
For any non-local deployment, set `authToken` and tighten `allowedIPs` and `excludedTools`.
{% endhint %}

## 🧰 Runtime Tool Domains

`bx-mcp` ships with over 100 tools grouped by runtime domain:

| Domain | Purpose |
| --- | --- |
| Runtime & Configuration | Runtime version, config inspection, BIF/component discovery, debug toggles |
| JVM Diagnostics | Memory, threads, GC, CPU, class loading, environment data |
| Cache Management | Cache stats, key metadata, health checks, clear/reap operations |
| Datasource Management | Datasource inventory, pool metrics, connectivity tests |
| Async Executors | Executor status, pool stats, saturation and health reporting |
| Schedulers | Scheduler/task inventory, stats, pause/resume, force-run operations |
| Modules | Module listing, settings, path inspection, reload operations |
| Interceptors | Interception points, listener states, registry summaries |
| Applications | Active app inventory, summaries, lifecycle stop operations |
| Logging | Logger/appender inspection, log reads, search, test writes |
| HTTP/SOAP Clients | Outbound client inventory, usage metrics, executor status |
| File Watchers | Watcher lifecycle operations, stats, health summaries |

## 🧠 Built-In MCP Prompts

The module also registers curated prompt workflows for common operations such as:

- Runtime health checks
- Memory pressure diagnosis
- Cache and datasource analysis
- Thread dump and error investigations
- Module, scheduler, and interceptor audits

These prompts help MCP clients call tools in the right sequence with operational context.

## 🔌 Client Connection Example

Point your MCP client at the BoxLang endpoint:

```json
{
  "mcpServers": {
    "boxlang": {
      "url": "http://localhost:8080/~bxmcp/boxlang.bxm",
      "headers": {
        "Authorization": "Bearer your-auth-token"
      }
    }
  }
}
```

If `authToken` is empty, omit the `headers` block.

## 🔗 Related Docs

- [BoxLang AI](../../../modularity/ai.md)
- [Module Installation](../../../../getting-started/installation/modules.md)
- [Module Configuration](../../../../getting-started/configuration/modules.md)
