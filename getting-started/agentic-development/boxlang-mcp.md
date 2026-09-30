---
description: >-
  Let AI agents inspect and operate a live BoxLang runtime over MCP with the
  BoxLang+ bx-mcp module.
icon: plug
---

# BoxLang MCP

{% hint style="success" %}
`bx-mcp` is a BoxLang+ module. **Try every BoxLang+ module free for 60 days.** The trial starts automatically the first time you start a BoxLang server or CLI with a BoxLang+ module installed. No sign-up and no key. See [BoxLang+](../../boxlang-framework/boxlang-plus/README.md).
{% endhint %}

Documentation MCP servers tell an agent what BoxLang **should** do. The `bx-mcp` module lets an agent see what your BoxLang server is **actually** doing. It exposes a Model Context Protocol server from a running runtime, so an agent can inspect and diagnose it directly.

## ✨ What an Agent Can Do

The module ships 154 tools across 17 runtime domains. Examples:

* **Runtime and JVM:** version, configuration, memory, threads, GC, deadlock detection
* **Data layer:** cache health, datasource pool metrics, slow SQL
* **HTTP and web:** slow requests, outbound call stats, per-route metrics
* **Operations:** executors, schedulers, modules, interceptors, applications, logging, file watchers
* **Health reports and incident workflows:** structured snapshots and triage prompts

## 📦 Install

```bash
install-bx-module bx-plus bx-ai bx-mcp
```

With CommandBox:

```bash
box install bx-plus,bx-ai,bx-mcp
```

Once installed, the server is available at `/~bxmcp/boxlang.bxm`, for example `http://localhost:8080/~bxmcp/boxlang.bxm`.

## 🔌 Connect an Agent

VS Code, in `.vscode/mcp.json`:

```json
{
  "mcpServers": {
    "boxlang-mcp": {
      "url": "http://localhost:8080/~bxmcp/boxlang.bxm",
      "headers": {
        "Authorization": "Bearer your-auth-token"
      }
    }
  }
}
```

See [Client Configuration](../../boxlang-framework/boxlang-plus/modules/bx-mcp/client-configuration.md) for Claude Desktop, Cursor, and curl examples.

## 🔐 Governance and Access Control

An agent with runtime access needs boundaries. `bx-mcp` provides:

* **Bearer tokens** for authentication
* **Security profiles** with tool allow and deny lists, including glob patterns
* **IP allowlists** and CORS controls

Some tools change state, for example clearing caches, triggering GC, or reloading modules. Give agents a read-only profile unless they need more:

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "securityProfiles": {
          "readonly": { "includedTools": [ "*_get*", "*_has*", "*_search*", "*_read*" ], "excludedTools": [] }
        },
        "authToken": [
          { "token": "monitor-token", "profile": "readonly" }
        ]
      }
    }
  }
}
```

{% hint style="warning" %}
Always set an `authToken` for any deployment reachable beyond localhost.
{% endhint %}

## 📚 Learn More

{% content-ref url="../../boxlang-framework/boxlang-plus/modules/bx-mcp/README.md" %}
[README.md](../../boxlang-framework/boxlang-plus/modules/bx-mcp/README.md)
{% endcontent-ref %}

{% content-ref url="../../boxlang-framework/boxlang-plus/modules/bx-mcp/security-and-access-control.md" %}
[security-and-access-control.md](../../boxlang-framework/boxlang-plus/modules/bx-mcp/security-and-access-control.md)
{% endcontent-ref %}

## 🧱 ColdBox Applications

For a ColdBox application, the `cbMCP` module gives agents live application introspection such as routes, handlers, modules, and WireBox mappings. It is BoxLang only. See the [ColdBox cbMCP documentation](https://coldbox.ortusbooks.com/getting-started/agentic-development/cbmcp).
