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
        },
        "routeMetrics": {
          "enabled": true,
          "maxRoutes": 200,
          "normalizePathParams": true
        },
        "securityProfiles": {
          "admin": { "includedTools": ["*"], "excludedTools": [] },
          "readonly": { "includedTools": ["*_get*", "*_has*", "*_search*", "*_read*"], "excludedTools": [] }
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
| `authToken` | string \| array | `""` | Bearer token(s) controlling access. Supports three shapes: simple string (one token, full access), array of structs with inline tool lists, or array of structs with `profile` references to `securityProfiles`. Empty = no auth. |
| `allowedIPs` | array | `["127.0.0.1"]` | IP allowlist. Supports individual IPs and CIDR ranges (`192.168.0.0/24`). Empty array = all IPs allowed. |
| `corsAllowedOrigins` | array | `[]` | CORS allowed origins. Supports wildcards (`*.domain.com`). Empty = no CORS headers. |
| `enableStats` | boolean | `true` | Enable MCP server statistics tracking (tool call counts, timing). |
| `maxRequestBodySize` | numeric | `0` | Max HTTP request body size in bytes. `0` = no limit. |
| `includedTools` | array | `["*"]` | Tool whitelist. `["*"]` = all tools. Supports exact names and glob patterns (`jvm*`, `cache_get*`). |
| `excludedTools` | array | `[]` | Tools to hide from the MCP client after the whitelist is applied. Supports exact names and glob patterns. |
| `securityProfiles` | object | `{}` | Named security profiles referenced by `authToken` entries via the `profile` field. Each profile defines `includedTools` and `excludedTools` arrays with glob support. Two built-in profiles (`admin` and `readonly`) can be overridden here. |
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

## Route Metrics Configuration

```json
{
  "routeMetrics": {
    "enabled": true,
    "maxRoutes": 200,
    "normalizePathParams": true
  }
}
```

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | boolean | `true` | Enable per-route inbound request metrics through the `RouteMetricsCollector` interceptor |
| `maxRoutes` | number | `200` | Maximum number of unique routes tracked; least-recently-seen evicted when exceeded |
| `normalizePathParams` | boolean | `true` | Replace digit-only and UUID path segments with `{id}` to prevent metric table explosion (e.g., `/users/123` → `/users/{id}`) |

> Route metrics capture count, error rate, and latency histograms (p50/p95/p99) per `METHOD /normalized-path` for every completed request.

---

## Security Profiles

The `securityProfiles` setting defines named profiles referenced from `authToken` entries via the `profile` field. This is the **recommended** approach — define profiles once, assign tokens to profiles instead of repeating tool lists.

### Built-in Profiles

Two profiles are always available and can be overridden here:

| Profile | Included Tools | Description |
| --- | --- | --- |
| `admin` | `["*"]` (all tools) | Unrestricted access to every tool |
| `readonly` | `["*_get*", "*_has*", "*_search*", "*_read*"]` | Read-only observability — all get/has/search/read operations |

### Custom Profile Configuration

```json
{
  "securityProfiles": {
    "admin": { "includedTools": ["*"], "excludedTools": [] },
    "readonly": { "includedTools": ["*_get*", "*_has*", "*_search*", "*_read*"], "excludedTools": [] },
    "operator": {
      "includedTools": ["*_get*", "*_has*", "module_reload*", "scheduler_*"],
      "excludedTools": ["app_stop", "runtime_toggle_debug_mode"]
    },
    "monitor": {
      "includedTools": ["*_get*", "*_health*", "performance_get_*"],
      "excludedTools": []
    }
  }
}
```

Each profile accepts:

| Field | Default | Description |
| --- | --- | --- |
| `includedTools` | `["*"]` | Tool whitelist with glob pattern support |
| `excludedTools` | `[]` | Tool blacklist with glob pattern support |

---

## Authentication & Access Control

The `authToken` setting supports three shapes:

### Shape 1: Simple String

```json
{
  "authToken": "my-secret-token"
}
```

One token with full access to every registered tool.

### Shape 2: Array of Structs (Inline Tools)

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

### Shape 3: Array of Structs (Profile Reference) — Recommended

Instead of repeating tool lists, reference a named profile from `securityProfiles`:

```json
{
  "authToken": [
    { "token": "admin-token",   "profile": "admin"    },
    { "token": "monitor-token", "profile": "readonly"  },
    { "token": "ops-token",     "profile": "operator"  }
  ]
}
```

| Field | Default | Description |
| --- | --- | --- |
| `token` | *(required)* | The Bearer token value the client must send |
| `profile` | *(required)* | Name of a profile defined in `securityProfiles` above |

When a token has a `profile` field, it inherits all tool rules from the named profile. Inline `includedTools`/`excludedTools` on the same token entry are ignored when `profile` is set.

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
