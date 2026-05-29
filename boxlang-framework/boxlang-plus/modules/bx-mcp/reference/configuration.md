---
icon: gear
description: Complete settings reference for the bx-mcp module including authentication access control, slow request tracking, and performance monitoring.
---

# ⚙️ Configuration Reference

All settings are configured in your `boxlang.json` under `modules.bxmcp.settings`.

---

## Complete Settings Table

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
        "enablePoolLatencyTracking": false,
        "heapDumpDir": "",
        "includedTools": ["*"],
        "excludedTools": [],
        "slowSQL": {
          "enabled": true,
          "slowQueryThresholdMs": 1000,
          "slowQueryBufferSize": 200,
          "slowQueryCapture": true
        },
        "slowRequests": {
          "enabled": true,
          "slowRequestThresholdMs": 1000,
          "slowRequestBufferSize": 200,
          "slowRequestCaptureStack": false
        },
        "slowHttp": {
          "enabled": true,
          "slowHttpThresholdMs": 1000,
          "slowHttpBufferSize": 200,
          "slowHttpCaptureBody": false
        }
      }
    }
  }
}
```

### Core Settings

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | `true` | Master switch. When `false`, the MCP server is not registered at runtime. |
| `authToken` | string \| array | `""` | Bearer token(s) controlling access. Supports a simple string or an array of structs with per-token tool filters. Empty = no auth. |
| `allowedIPs` | array | `["127.0.0.1"]` | IP allowlist. Supports individual IPs and CIDR ranges (`192.168.0.0/24`). Empty array = all IPs allowed. |
| `corsAllowedOrigins` | array | `[]` | CORS allowed origins. Supports wildcards (`*.domain.com`). Empty = no CORS headers. |
| `enableStats` | boolean | `true` | Enable MCP server statistics tracking (tool call counts, timing). |
| `maxRequestBodySize` | numeric | `0` | Max HTTP request body size in bytes. `0` = no limit. |
| `includedTools` | array | `["*"]` | Tool whitelist. `["*"]` = all tools. Supports exact names and glob patterns (`jvm*`, `cache_get*`). |
| `excludedTools` | array | `[]` | Tools to hide from the MCP client after the whitelist is applied. Supports exact names and glob patterns. |
| `enablePoolLatencyTracking` | boolean | `false` | Enable HikariCP connection-pool latency histograms for all datasources (acquire/usage/creation percentiles + timeout count). Requires BoxLang 1.14+ with `ON_DATASOURCE_INITIALIZED` event support. |
| `heapDumpDir` | string | `""` | Directory where `.hprof` heap dump files are written by the `jvm_trigger_heap_dump` tool. Empty = system temp directory. The directory is created automatically if it does not exist. |

---

## Slow SQL Configuration

```json
{
  "slowSQL": {
    "enabled": true,
    "slowQueryThresholdMs": 1000,
    "slowQueryBufferSize": 200,
    "slowQueryCapture": true
  }
}
```

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | `true` | Enable slow SQL capture through the `SlowJDBCCollector` interceptor |
| `slowQueryThresholdMs` | number | `1000` | Slow-query cutoff in milliseconds |
| `slowQueryBufferSize` | number | `200` | In-memory sample window size |
| `slowQueryCapture` | boolean | `true` | Controls whether rendered SQL text is stored |

---

## Slow Request Configuration

```json
{
  "slowRequests": {
    "enabled": true,
    "slowRequestThresholdMs": 1000,
    "slowRequestBufferSize": 200,
    "slowRequestCaptureStack": false
  }
}
```

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | `true` | Enable slow inbound request capture through the `SlowRequestCollector` interceptor |
| `slowRequestThresholdMs` | number | `1000` | Slow-request cutoff in milliseconds |
| `slowRequestBufferSize` | number | `200` | In-memory rolling window size |
| `slowRequestCaptureStack` | boolean | `false` | Controls whether a completion-time thread stack snapshot is stored |

---

## Slow HTTP Configuration

```json
{
  "slowHttp": {
    "enabled": true,
    "slowHttpThresholdMs": 1000,
    "slowHttpBufferSize": 200,
    "slowHttpCaptureBody": false
  }
}
```

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | `true` | Enable slow outbound HTTP/SOAP call capture through the `SlowHttpCollector` interceptor |
| `slowHttpThresholdMs` | number | `1000` | Slow-call cutoff in milliseconds |
| `slowHttpBufferSize` | number | `200` | In-memory sample window size |
| `slowHttpCaptureBody` | boolean | `false` | Controls whether a truncated (500-char) response body snippet is stored |

> SOAP calls transit through the same `BoxHttpClient` pipeline, so they are captured automatically by this configuration.

---

## Authentication & Access Control

The `authToken` setting supports two shapes:

### Shape 1: Simple String

```json
{
  "authToken": "my-secret-token"
}
```

One token with full access to every registered tool.

### Shape 2: Array of Structs

```json
{
  "authToken": [
    {
      "token": "admin-token",
      "includedTools": ["*"],
      "excludedTools": []
    },
    {
      "token": "readonly-token",
      "includedTools": ["runtime_get_info", "jvm_get_memory_info", "module_get_all"],
      "excludedTools": []
    }
  ]
}
```

| Field | Default | Description |
| --- | --- | --- |
| `token` | *(required)* | The Bearer token value the client must send |
| `includedTools` | `["*"]` | Tool whitelist. `["*"]` means all tools. Supports glob patterns. |
| `excludedTools` | `[]` | Tools to block even if they match the whitelist. Supports glob patterns. |

### Filtering Rules (Applied in Order)

1. If `includedTools` does **not** contain `"*"` and the tool name does not match any pattern → **denied**
2. If the tool name matches any pattern in `excludedTools` → **denied**
3. Otherwise → **allowed**

### Glob Pattern Reference

| Pattern | Matches |
| --- | --- |
| `"*"` | All tools |
| `"jvm*"` | All tools starting with `jvm_` |
| `"cache_get*"` | `cache_get_all`, `cache_get_stats`, `cache_get_keys`, … |
| `"*_health*"` | Any tool with `_health` in its name |
| `"runtime_get_info"` | Exact match only |

---

## Security Notes

- **`authToken`**: Strongly recommended for any non-localhost deployment. Clients must send `Authorization: Bearer {token}`.
- **`allowedIPs`**: Defaults to `localhost` only. For access from Docker containers or remote machines, add their IPs or CIDR ranges.
- **`excludedTools`**: Use this to hide sensitive operations (e.g., `jvm_trigger_gc`, `cache_clear_all`, `module_reload_all`) from MCP clients. Glob patterns like `cache_clear*` are supported.
- **Disabling authentication**: Leave `authToken` empty (`""`) or omit it entirely to run in open-access mode. Suitable only for localhost-only deployments already protected by `allowedIPs`.
