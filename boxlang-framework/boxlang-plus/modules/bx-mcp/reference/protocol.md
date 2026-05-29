---
icon: network-wired
description: JSON-RPC 2.0 protocol reference — endpoint, supported methods, request/response envelopes, and authentication.
---

# 🔌 Protocol Reference

The `bx-mcp` server communicates using the **JSON-RPC 2.0** protocol over HTTP POST. This reference covers the endpoint, supported methods, and request/response structures.

---

## 📍 Endpoint

```
POST /~bxmcp/boxlang.bxm
```

| Attribute | Value |
| --- | --- |
| **URL** | `http://localhost:8080/~bxmcp/boxlang.bxm` |
| **Method** | POST |
| **Content-Type** | `application/json` |
| **Auth** | Bearer token via `Authorization` header (optional) |

---

## 🔐 Authentication

If `authToken` is configured, include the token in all requests:

```http
Authorization: Bearer your-auth-token
```

If `authToken` is empty or not configured, omit the header. See [Security & Access Control](../security-and-access-control.md) for authentication configuration options.

---

## 📦 Request Envelope

All requests follow the JSON-RPC 2.0 specification:

```json
{
  "jsonrpc": "2.0",
  "method": "method_name",
  "params": { ... },
  "id": "request-id"
}
```

| Field | Type | Description |
| --- | --- | --- |
| `jsonrpc` | string | Protocol version — must be `"2.0"` |
| `method` | string | The RPC method to call |
| `params` | object | Method-specific parameters |
| `id` | string/number | Request identifier, echoed in response |

---

## 📨 Response Envelope

### Success Response

```json
{
  "jsonrpc": "2.0",
  "result": { ... },
  "id": "request-id"
}
```

### Error Response

```json
{
  "jsonrpc": "2.0",
  "error": {
    "code": -32601,
    "message": "Method not found"
  },
  "id": "request-id"
}
```

---

## 🛠️ Supported Methods

### `tools/list`

List all available MCP tools.

**Request:**
```json
{
  "jsonrpc": "2.0",
  "method": "tools/list",
  "id": "1"
}
```

**Result:**
```json
{
  "result": {
    "tools": [
      {
        "name": "runtime_get_info",
        "description": "BoxLang version, JVM environment, OS details, start time, uptime",
        "inputSchema": { ... }
      }
    ]
  },
  "id": "1"
}
```

**curl example:**
```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":"1"}'
```

---

### `tools/call`

Invoke a specific tool by name with arguments.

**Request:**
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "runtime_get_info",
    "arguments": {}
  },
  "id": "2"
}
```

**Result:**
Tool results are wrapped by the MCP protocol:

```json
{
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{ \"boxlangVersion\": \"1.14.0\", ... }"
      }
    ]
  },
  "id": "2"
}
```

The actual tool output is in `result.content[0].text` as a JSON-encoded string. Use `jq` to extract and pretty-print it:

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"runtime_get_info","arguments":{}},"id":"2"}' | jq '.result.content[0].text | fromjson'
```

---

### `prompts/list`

List all available MCP prompts.

**Request:**
```json
{
  "jsonrpc": "2.0",
  "method": "prompts/list",
  "id": "3"
}
```

**curl example:**
```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"prompts/list","id":"3"}'
```

---

### `prompts/get`

Get a specific prompt by name with optional arguments.

**Request:**
```json
{
  "jsonrpc": "2.0",
  "method": "prompts/get",
  "params": {
    "name": "full_system_audit",
    "arguments": {}
  },
  "id": "4"
}
```

**curl example:**
```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"prompts/get","params":{"name":"full_system_audit","arguments":{}},"id":"4"}' | jq '.result.messages'
```

---

### `resources/list`

List available MCP resources.

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"resources/list","id":"5"}'
```

---

### `resources/read`

Read a specific resource by URI.

```bash
curl -s http://localhost:8080/~bxmcp/boxlang.bxm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-token" \
  -d '{"jsonrpc":"2.0","method":"resources/read","params":{"uri":"resource-uri"},"id":"6"}'
```

---

## 📋 Standard Error Codes

| Code | Message | Description |
| --- | --- | --- |
| `-32700` | Parse error | Invalid JSON was received |
| `-32600` | Invalid Request | The JSON sent is not a valid Request object |
| `-32601` | Method not found | The method does not exist |
| `-32602` | Invalid params | Invalid method parameter(s) |
| `-32603` | Internal error | Internal JSON-RPC error |
| `-32000` | Tool execution error | The tool threw an exception |
| `-32001` | Tool not found | The named tool is not registered |
| `-32002` | Unauthorized | Invalid or missing authentication token |
