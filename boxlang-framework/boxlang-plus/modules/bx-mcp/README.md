---
description: >-
  Model Context Protocol server module for BoxLang runtime diagnostics,
  introspection, and operational automation.
icon: robot
---

# MCP +

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://boxlang.io/plans). It requires the `bx-plus` and `bx-ai` modules.
{% endhint %}

The `bx-mcp` module exposes a production-ready **Model Context Protocol (MCP) server** for BoxLang, enabling MCP-capable clients — AI coding assistants, IDE agents, monitoring tools, and automation pipelines — to inspect and operate a live BoxLang runtime over HTTP.

When enabled, the module auto-registers a `boxlang` MCP server and exposes an HTTP endpoint at `/~bxmcp/boxlang.bxm`. Clients communicate via **JSON-RPC 2.0** to list and invoke tools, retrieve prompts, and read resources.

---

## ✨ Features

- **🔍 Runtime Introspection** — Query BoxLang version, configuration, BIFs, components, and global services
- **💻 JVM Diagnostics** — Memory, threads, CPU, GC, hot threads, deadlock detection, heap dumps, disk and file descriptor usage
- **🗄️ Data Layer** — Cache analytics, datasource pool metrics, slow SQL capture, connection pool latency histograms
- **🌐 HTTP & Web** — HTTP/SOAP client stats, slow outbound call capture, slow request analysis, per-route metrics, Undertow server diagnostics
- **⚡ Operations** — Async executor monitoring, scheduler management, module lifecycle, interceptor registry audit, application lifecycle, logging, file watchers
- **🏥 Structured Health Reports** — Unified health snapshots across all subsystems with scoring, issue codes, and actionable recommendations
- **🚨 Incident Response** — Pre-built triage, error spike, cascade failure, rollback decision, and post-incident review workflows
- **🔧 Extensible** — Register custom MCP tools and prompts from your own modules and applications at runtime
- **🎮 Interactive CLI** — Built-in shell client with tab completion, watch mode, and formatted output
- **🔒 Access Control** — Per-token tool filtering with glob patterns, IP allowlisting, CORS support, and tool whitelist/blacklist

---

## 📦 Installation

### Via CommandBox

```bash
box install bx-plus,bx-ai,bx-mcp
```

### Via BoxLang OS Binary

```bash
install-bx-module bx-plus bx-ai bx-mcp
```

---

## 🚀 Quick Start

After installation, the MCP server is available at `http://localhost:8080/~bxmcp/boxlang.bxm`. Here's a 3-step check that everything is working:

**1. List available tools:**

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":"1"}' | jq '.result.tools | length'
```

**2. Get BoxLang runtime information:**

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"runtime_get_info","arguments":{}},"id":"2"}' | jq '.result.content[0].text | fromjson'
```

**3. Check cache health:**

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"cache_get_health","arguments":{}},"id":"3"}' | jq '.result.content[0].text | fromjson'
```

> See the [Quick Start](quick-start.md) guide for detailed setup including VS Code, Claude Desktop, and Cursor client configurations.

---

## 📖 Documentation Sections

### Usage Guides

| Guide | Description |
| --- | --- |
| [Quick Start](quick-start.md) | Install, configure, and connect your first MCP client |
| [Security & Access Control](security-and-access-control.md) | Auth tokens, per-token tool filters, IP allowlisting, CORS |
| [Client Configuration](client-configuration.md) | VS Code, Claude Desktop, Cursor, and generic curl setup |
| [Operations & Monitoring](operations-and-monitoring.md) | Health checks, performance snapshots, JVM monitoring, scheduler oversight |
| [Data Layer Diagnostics](data-layer-diagnostics.md) | Cache analysis, datasource health, slow SQL/HTTP diagnosis |
| [Incident Response](incident-response.md) | Triage workflows, error spikes, cascade failures, post-mortems |
| [Extending with Custom Tools](extending-with-custom-tools.md) | Register custom tools and prompts at runtime |

### Reference

| Section | Description |
| --- | --- |
| [MCP Tools](reference/tools/README.md) | Complete tool catalog organized by domain (154 tools) |
| [MCP Prompts](reference/prompts/README.md) | Pre-built diagnostic and administrative prompts (32 prompts) |
| [Protocol](reference/protocol.md) | JSON-RPC 2.0 endpoint, methods, and request/response envelopes |
| [Health Reports](reference/health-reports.md) | Health report schema, scoring model, and issue code catalog |
| [Configuration](reference/configuration.md) | Complete settings reference and authentication deep-dive |

---

## 🔌 Client Connection

Configure your MCP client to connect to the BoxLang endpoint:

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

See [Client Configuration](client-configuration.md) for platform-specific setup (VS Code, Claude Desktop, Cursor) and [Security & Access Control](security-and-access-control.md) for authentication options.

---

## 🎮 Interactive CLI

The module ships with a built-in interactive CLI client. Launch it from the BoxLang CLI:

```bash
boxlang bxmcp [url] [--timeout=ms] [--token=bearer] [--help]
```

Once connected, use commands like `tools`, `prompts`, `run <tool>`, and `watch <tool>` to interact with any MCP server.

---

## 📋 Requirements

- **BoxLang 1.12+**
- **bx-plus** and **bx-ai** modules
- A BoxLang+ Subscription is required for use

---

## 🔗 Related Documentation

- [BoxLang AI Module](../../../modularity/ai.md)
- [Module Installation Guide](../../../../getting-started/installation/modules.md)
- [Module Configuration](../../../../getting-started/configuration/modules.md)
