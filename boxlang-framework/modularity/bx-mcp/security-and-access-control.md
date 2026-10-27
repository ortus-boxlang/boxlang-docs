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
| **Authorization** | Per-token tool filters with glob patterns and named security profiles | Per-request tool access |
| **Network** | IP allowlisting via `allowedIPs` | Connection-level |
| **CORS** | Origin allowlisting via `corsAllowedOrigins` | Browser-based clients |

---

## 🔑 Authentication

Authentication is configured with the `authToken` setting. It supports three shapes.

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

### Shape 2: Array of Structs (Inline Tools)

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

### Shape 3: Array of Structs (Profile Reference) — Recommended

Reference named profiles from `securityProfiles` instead of repeating tool lists:

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "securityProfiles": {
          "admin":    { "includedTools": ["*"], "excludedTools": [] },
          "readonly": { "includedTools": ["*_get*", "*_has*", "*_search*", "*_read*"], "excludedTools": [] }
        },
        "authToken": [
          { "token": "admin-token",   "profile": "admin"    },
          { "token": "monitor-token", "profile": "readonly"  }
        ]
      }
    }
  }
}
```

Each struct accepts:

| Field | Default | Description |
| --- | --- | --- |
| `token` | *(required)* | The Bearer token value the client must send |
| `profile` | *(required)* | Name of a profile defined in `securityProfiles` |

When a token uses `profile`, it inherits all tool rules from the named profile. Inline `includedTools`/`excludedTools` on the same token entry are ignored when `profile` is set. See the [Security Profiles](#-security-profiles) section above for how to define profiles.

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

## 📋 Security Profiles

The `securityProfiles` setting provides a **recommended** way to manage token access — define named profiles once in configuration, then reference them from `authToken` entries via the `profile` field. This eliminates repetitive tool lists and centralizes access policy.

### Built-in Profiles

Two profiles are always available and can be overridden:

| Profile | Included Tools | Description |
| --- | --- | --- |
| `admin` | `["*"]` (all tools) | Unrestricted access to every tool |
| `readonly` | `["*_get*", "*_has*", "*_search*", "*_read*"]` | Read-only observability — all get/has/search/read operations |

### Defining Custom Profiles

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
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
    }
  }
}
```

Each profile accepts:

| Field | Default | Description |
| --- | --- | --- |
| `includedTools` | `["*"]` | Tool whitelist with glob pattern support |
| `excludedTools` | `[]` | Tool blacklist with glob pattern support |

### Using Profiles in Auth Tokens

Once profiles are defined, reference them in `authToken` entries with the `profile` field:

```json
{
  "authToken": [
    { "token": "admin-token",   "profile": "admin"    },
    { "token": "monitor-token", "profile": "readonly"  },
    { "token": "ops-token",     "profile": "operator"  }
  ]
}
```

When a token uses `profile`, it inherits all tool rules from the named profile. Inline `includedTools`/`excludedTools` on the same token entry are ignored when `profile` is set.

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
- ✅ Use `securityProfiles` for centralized, maintainable access policies (recommended over inline tool lists)
- ✅ Restrict `allowedIPs` to trusted networks
- ✅ Add sensitive tools to `excludedTools`
- ✅ Use per-token access control for multi-tenant scenarios
- ✅ Enable TLS/HTTPS on your web server for encrypted transport
- ✅ Review `logging_get_info` and `runtime_get_config` — these expose system details

### Example: Read-Only Monitoring Token (Profile-Based — Recommended)

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "securityProfiles": {
          "admin":    { "includedTools": ["*"], "excludedTools": [] },
          "monitor":  { "includedTools": ["*_get*", "*_has*", "*_search*", "*_read*", "*_health*", "performance_get_*"], "excludedTools": [] }
        },
        "authToken": [
          { "token": "monitor-token", "profile": "monitor" },
          { "token": "admin-token",   "profile": "admin"   }
        ]
      }
    }
  }
}
```

### Example: Read-Only Monitoring Token (Inline)

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

### Example: Ops Token Without Destructive Operations (Profile-Based — Recommended)

```json
{
  "modules": {
    "bxmcp": {
      "settings": {
        "securityProfiles": {
          "operator": {
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
        },
        "authToken": [
          { "token": "ops-token", "profile": "operator" }
        ]
      }
    }
  }
}
```

### Example: Ops Token Without Destructive Operations (Inline)

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
