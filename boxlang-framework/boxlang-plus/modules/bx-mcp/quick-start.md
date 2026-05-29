---
description: Get up and running with bx-mcp in minutes — install, configure, and connect your first MCP client.
icon: rocket-launch
---

# 🚀 Quick Start

This guide walks you through installing the `bx-mcp` module, configuring it, and connecting your first MCP client.

---

## 📋 Prerequisites

- **BoxLang 1.12+** installed and running
- **bx-plus** and **bx-ai** modules installed
- A **BoxLang+ Subscription** ([purchase here](https://boxlang.io/plans))
- A running BoxLang application or MiniServer instance

---

## 📦 Install the Module

### Via CommandBox

```bash
box install bx-plus,bx-ai,bx-mcp
```

### Via BoxLang OS Binary

```bash
install-bx-module bx-plus bx-ai bx-mcp
```

---

## ⚙️ Minimal Configuration

Add the MCP server configuration to your `boxlang.json` under `modules.bxmcp.settings`:

```json
{
  "modules": {
    "bxmcp": {
      "enabled": true,
      "settings": {
        "enabled": true,
        "authToken": "my-first-mcp-token",
        "allowedIPs": ["127.0.0.1"],
        "includedTools": ["*"],
        "excludedTools": []
      }
    }
  }
}
```

> **⚠️ Security:** Always set `authToken` for any deployment accessible beyond localhost. See [Security & Access Control](security-and-access-control.md) for advanced options including per-token tool filters.

---

## ✅ Verify the Installation

Restart your BoxLang runtime. The MCP server registers automatically during module startup. Verify it's running:

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer my-first-mcp-token" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":"1"}' | jq '.result.tools | length'
```

You should see a response showing the total number of available tools (154).

---

## 🔬 Call Your First Tool

### Get Runtime Information

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer my-first-mcp-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"runtime_get_info","arguments":{}},"id":"2"}' | jq '.result.content[0].text | fromjson'
```

This returns BoxLang version, JVM details, OS information, start time, uptime, and license status.

### Check Cache Health

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer my-first-mcp-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"cache_get_health","arguments":{}},"id":"3"}' | jq '.result.content[0].text | fromjson'
```

### Test a Datasource Connection

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer my-first-mcp-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"datasource_test","arguments":{"dsn":"myDB"}},"id":"4"}' | jq '.result.content[0].text | fromjson'
```

---

## 💻 Configure VS Code

Create a `.vscode/mcp.json` file in your project root:

```json
{
  "mcpServers": {
    "boxlang-mcp": {
      "url": "http://localhost:8080/~bxmcp/boxlang.bxm",
      "headers": {
        "Authorization": "Bearer my-first-mcp-token"
      }
    }
  }
}
```

VS Code will automatically connect to the MCP server when you open the workspace.

---

## 🤖 Configure Claude Desktop

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "boxlang": {
      "url": "http://localhost:8080/~bxmcp/boxlang.bxm",
      "headers": {
        "Authorization": "Bearer my-first-mcp-token"
      }
    }
  }
}
```

---

## 🖥️ Configure Cursor

Create a `.cursor/mcp.json` file in your project root with the same structure as the VS Code example above.

---

## 🎮 Use the Interactive CLI

The module includes a built-in interactive CLI. Launch it from a terminal:

```bash
boxlang bxmcp http://localhost:8080/~bxmcp/boxlang.bxm --token=my-first-mcp-token
```

Once connected, type `tools` to list all tools, `help` for commands, or `run runtime_get_info` to invoke a tool.

---

## 📚 Next Steps

- [Security & Access Control](security-and-access-control.md) — Learn about per-token filtering, IP allowlisting, and CORS
- [Client Configuration](client-configuration.md) — Detailed client setup for all platforms
- [Operations & Monitoring](operations-and-monitoring.md) — Health checks and performance monitoring
- [MCP Tools Reference](reference/tools/README.md) — Complete catalog of all 154 tools
- [MCP Prompts Reference](reference/prompts/README.md) — Pre-built diagnostic and administrative prompts
