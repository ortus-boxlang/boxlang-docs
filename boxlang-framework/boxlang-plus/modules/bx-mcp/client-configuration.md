---
description: Configure VS Code, Claude Desktop, Cursor, and other MCP clients to connect to your BoxLang MCP server.
icon: monitor
---

# 💻 Client Configuration

This guide covers how to configure different MCP clients to connect to the BoxLang MCP server.

---

## 🔌 Connection Basics

The BoxLang MCP server is available at:

```
http://localhost:8080/~bxmcp/boxlang.bxm
```

All clients use the same JSON-RPC 2.0 endpoint. The only differences are where and how you store the configuration.

### Common Configuration Shape

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

> Replace `your-auth-token` with the value of `authToken` from your module settings. If `authToken` is empty, omit the `headers` block.

---

## 🆚 VS Code

Create a `.vscode/mcp.json` file in your project root:

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

VS Code automatically detects and connects to MCP servers defined in `.vscode/mcp.json` when you open the workspace. The MCP tools become available to GitHub Copilot and other AI features.

---

## 🤖 Claude Desktop

Add the server configuration to your Claude Desktop configuration file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

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

Restart Claude Desktop after adding the configuration.

---

## 🖥️ Cursor

Create a `.cursor/mcp.json` file in your project root:

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

Cursor will automatically connect to the MCP server and make the tools available for AI-powered development.

---

## 🐚 Generic HTTP Client (curl)

### List All Tools

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-auth-token" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":"1"}' | jq '.result.tools[] | {name, description}'
```

### Call a Tool

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-auth-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"jvm_get_memory_info","arguments":{}},"id":"2"}' | jq '.result.content[0].text | fromjson'
```

### List All Prompts

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-auth-token" \
  -d '{"jsonrpc":"2.0","method":"prompts/list","id":"3"}' | jq '.result.prompts[] | {name, description}'
```

### Get a Specific Prompt

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-auth-token" \
  -d '{"jsonrpc":"2.0","method":"prompts/get","params":{"name":"full_system_audit","arguments":{}},"id":"4"}' | jq '.result.messages'
```

---

## 📝 Tool Filtering at the Client Level

Some MCP clients support restricting which tools are visible. This is a client-side setting and does not replace server-side authorization. For true access control, use the server-side `authToken` array-of-structs approach described in [Security & Access Control](security-and-access-control.md).

---

## 🌐 Remote Connections

To connect to a remote BoxLang server (not localhost):

1. **Update `allowedIPs`** in your module configuration to include your client's IP or CIDR range
2. **Set a strong `authToken`** — never expose a remote endpoint without authentication
3. **Enable HTTPS** on your web server for encrypted transport
4. **Update the URL** in your client configuration to point to the remote host

```json
{
  "mcpServers": {
    "boxlang": {
      "url": "https://my-server.example.com/~bxmcp/boxlang.bxm",
      "headers": {
        "Authorization": "Bearer your-auth-token"
      }
    }
  }
}
```

---

## 🎮 Interactive CLI

The module ships with a built-in interactive CLI client. See the [README](README.md#-interactive-cli) for usage instructions.

---

## 📚 Next Steps

- [Quick Start](quick-start.md) — Basic installation and first tool call
- [Security & Access Control](security-and-access-control.md) — Secure your MCP server
- [Operations & Monitoring](operations-and-monitoring.md) — Health checks and runtime monitoring
