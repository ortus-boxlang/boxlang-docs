---
description: >-
  Detailed configuration, credential resolution order, caching, and runtime
  behavior for the bx-azure-secrets module.
icon: sliders
---

# Configuration & Usage

This guide covers effective settings, credential source precedence, local development, and operational behavior for `bx-azure-secrets`.

## 🔧 Configuration Sources

Each setting is resolved independently in this order:

1. `this.azure` in `Application.bx` (per-application)
2. Module settings in `boxlang.json` (global)
3. Azure environment variables / `DefaultAzureCredential`

## 🧩 `Application.bx` (Per-App)

Use `this.azure` when each app needs isolated vault or identity behavior.

```js
class {
    this.name = "myApp"

    this.azure = {
        vaultUrl     : "https://my-vault.vault.azure.net/",
        tenantId     : "",
        clientId     : "",
        clientSecret : "",
        cacheTTL     : 300
    }
}
```

When `this.azure` is present, the module creates and reuses a dedicated `SecretClient` for that application.

## 🌍 Global `boxlang.json` Settings

```json
{
  "modules": {
    "bxazure-secrets": {
      "settings": {
        "vaultUrl": "https://my-vault.vault.azure.net/",
        "tenantId": "",
        "clientId": "",
        "clientSecret": "",
        "cacheTTL": 300
      }
    }
  }
}
```

## 🌱 Environment Variable Fallback

Supported environment mappings:

| Setting | Environment Variable(s) |
| --- | --- |
| `vaultUrl` | `AZURE_KEY_VAULT_URL`, fallback `AZURE_KEYVAULT_URL` |
| `tenantId` | `AZURE_TENANT_ID` |
| `clientId` | `AZURE_CLIENT_ID` |
| `clientSecret` | `AZURE_CLIENT_SECRET` |

If explicit credentials are not configured, the module can also rely on Azure credential sources such as managed identity, workload identity, Azure CLI, or environment credentials through `DefaultAzureCredential`.

## 📋 Settings Reference

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `vaultUrl` | string | `""` | Azure Key Vault URL required for secret resolution |
| `tenantId` | string | `""` | Optional Azure tenant id for service principal authentication |
| `clientId` | string | `""` | Optional application client id or managed identity client id |
| `clientSecret` | string | `""` | Optional Azure client secret |
| `cacheTTL` | numeric | `300` | Cache time-to-live in seconds |

## 🔐 Usage Examples

Resolve a secret directly:

```js
dbPassword = getSystemSetting( "azure.DB-PASSWORD" )
```

Resolve with a fallback value:

```js
apiToken = getSystemSetting( "azure.API-TOKEN", "dev-token" )
```

Use in datasource config:

```js
this.datasources = {
    main : {
        className : "org.postgresql.Driver",
        connectionString : "jdbc:postgresql://localhost:5432/app",
        username : "app_user",
        password : getSystemSetting( "azure.DB-PASSWORD" )
    }
}
```

## 🧠 Caching Behavior

- Cache key format is `vaultUrl:secretName`
- Successful secret fetches are cached in-memory
- Expired entries are refreshed on next access
- Set `cacheTTL` to `0` for effectively no cache reuse

## 🏗 Client Lifecycle

- **Per-app client**: Used when `this.azure` exists
- **Global client**: Used when module settings provide vault-based config
- **Default credential client**: Used when relying only on Azure environment variables or credential chain defaults

Per-app clients are released on application shutdown, and all clients are closed or dereferenced on module/runtime shutdown.

## 🧪 Local Development with Azure CLI

Authenticate with Azure CLI and set a test secret:

```bash
az login
az keyvault secret set --vault-name my-vault --name DB-PASSWORD --value "local-password"
```

Minimal module settings:

```json
{
  "modules": {
    "bxazure-secrets": {
      "settings": {
        "vaultUrl": "https://my-vault.vault.azure.net/"
      }
    }
  }
}
```

## 🚨 Troubleshooting

- Secret returns `null`: verify `vaultUrl` is resolved and the secret exists in the target Key Vault
- License errors: confirm `bx-plus` is installed and licensed; for local testing, set `BX_AZURE_DEV=true`
- Permission errors: ensure the runtime identity can perform Key Vault secret reads
- Wrong module settings key: use `bxazure-secrets` under `modules` in `boxlang.json`
