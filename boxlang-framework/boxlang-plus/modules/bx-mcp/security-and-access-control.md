---
description: Secure your MCP server with auth tokens, per-token tool filters, IP allowlisting, and CORS configuration.
icon: lock
---

# 🔒 Security & Access Control

The `bx-mcp` module provides multiple layers of security to control access to your runtime diagnostics and management tools. These layers can be combined for defense in depth.

---

## 📋 Security Layers

| Layer | Mechanism | Scope |
| --- | --- | --- |
| **Authentication** | Bearer token via `authToken` | Every request |
| **Authorization** | Per-token tool filters with glob patterns | Per-request tool access |
| **Network** | IP allowlisting via `allowedIPs` | Connection-level |
| **CORS** | Origin allowlisting via `corsAllowedOrigins` | Browser-based clients |

---

## 🔑 Authentication

Authentication is configured with the `authToken` setting. It supports two shapes.

### Shape 1: Simple String

One token with full access to every registered tool:

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "authToken": "my-secret-token"
      }
    }
  }
}
```

Clients send:

```http
Authorization: Bearer my-secret-token
```

### Shape 2: Array of Structs

Multiple tokens, each with independent tool-level access control:

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
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
          },
          {
            "token": "ops-token",
            "includedTools": ["*"],
            "excludedTools": ["jvm_trigger_gc", "cache_clear_all", "module_reload_all"]
          }
        ]
      }
    }
  }
}
```

Each struct accepts the following fields:

| Field | Default | Description |
| --- | --- | --- |
| `token` | *(required)* | The Bearer token value the client must send |
| `includedTools` | `["*"]` | Tool whitelist — exact names or glob patterns |
| `excludedTools` | `[]` | Tools to block even if they match the whitelist |

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

### Disabling Authentication

Leave `authToken` empty (`""`) or omit it entirely to run in open-access mode. Suitable only for localhost-only deployments already protected by `allowedIPs`.

---

## 🌐 IP Allowlisting

Control access at the network level with `allowedIPs`. Supports individual IP addresses and CIDR notation.

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "allowedIPs": ["127.0.0.1", "192.168.1.0/24", "10.0.0.5"]
      }
    }
  }
}
```

| Value | Behavior |
| --- | --- |
| `["127.0.0.1"]` | **Default** — localhost only |
| `["192.168.0.0/16"]` | Allow entire private subnet |
| `["10.0.0.1", "10.0.0.2"]` | Allow specific IPs |
| `[]` | Allow all IPs (use with caution) |

---

## 🌍 CORS Configuration

Configure cross-origin requests for browser-based MCP clients:

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "corsAllowedOrigins": ["http://localhost:3000", "https://myapp.example.com", "*.domain.com"]
      }
    }
  }
}
```

| Value | Behavior |
| --- | --- |
| `[]` | **Default** — no CORS headers sent |
| `["*"]` | Allow all origins |
| `["*.domain.com"]` | Allow subdomains via wildcard |

---

## 🛡️ Tool Blacklisting

Use `excludedTools` at the global level to hide sensitive operations from all clients:

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "includedTools": ["*"],
        "excludedTools": [
          "jvm_trigger_gc",
          "jvm_trigger_heap_dump",
          "cache_clear_all",
          "module_reload_all",
          "runtime_clear_system_cache",
          "app_stop"
        ]
      }
    }
  }
}
```

---

## 🔐 Security Best Practices

### Production Deployment Checklist

- ✅ Set a strong `authToken` — never leave it empty
- ✅ Restrict `allowedIPs` to trusted networks
- ✅ Add sensitive tools to `excludedTools`
- ✅ Use per-token access control for multi-tenant scenarios
- ✅ Enable TLS/HTTPS on your web server for encrypted transport
- ✅ Review `logging_get_info` and `runtime_get_config` — these expose system details

### Example: Read-Only Monitoring Token

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "authToken": [
          {
            "token": "monitor-token",
            "includedTools": [
              "runtime_get_info",
              "jvm_get_*",
              "cache_get_*",
              "datasource_get_*",
              "sql_get_*",
              "system_get_health",
              "performance_get_snapshot"
            ],
            "excludedTools": []
          },
          {
            "token": "admin-token",
            "includedTools": ["*"],
            "excludedTools": []
          }
        ]
      }
    }
  }
}
```

### Example: Ops Token Without Destructive Operations

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "authToken": [
          {
            "token": "ops-token",
            "includedTools": ["*"],
            "excludedTools": [
              "jvm_trigger_gc",
              "jvm_trigger_heap_dump",
              "cache_clear_all",
              "cache_clear_item",
              "module_reload_all",
              "module_reload",
              "app_stop",
              "app_restart",
              "app_sessions_clear",
              "runtime_clear_system_cache",
              "runtime_clear_page_pool",
              "runtime_toggle_debug_mode"
            ]
          }
        ]
      }
    }
  }
}
```

---

## 📚 Next Steps

- [Client Configuration](client-configuration.md) — Set up VS Code, Claude Desktop, Cursor, and other clients
- [Operations & Monitoring](operations-and-monitoring.md) — Health checks and runtime monitoring
- [Configuration Reference](reference/configuration.md) — Complete settings reference
