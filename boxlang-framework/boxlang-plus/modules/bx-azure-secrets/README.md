---
description: >-
  Azure Key Vault integration for BoxLang system settings via the azure.
  namespace in getSystemSetting().
icon: key
---

# Azure Secrets +

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://boxlang.io/plans), and requires a valid `bx-plus` license.
{% endhint %}

The `bx-azure-secrets` module registers an `azure` system setting provider so BoxLang can resolve secrets directly from Azure Key Vault using `getSystemSetting()`.

## ✨ Features

- Resolve secrets with `getSystemSetting( "azure.SECRET-NAME" )`
- 3-tier configuration resolution per setting: `this.azure` in `Application.bx`, module settings, then Azure environment variables/default credentials
- In-memory TTL caching to reduce Key Vault API calls
- Per-application `SecretClient` isolation when `this.azure` is defined
- Automatic client cleanup on application shutdown
- Graceful fallback behavior: returns `null` on provider errors so normal `getSystemSetting()` fallback continues

## 📦 Requirements

- BoxLang 1.14+
- `bx-plus` module
- Azure identity with Key Vault `secrets/get` permission

## 🚀 Installation

### Via CommandBox

```bash
box install bx-plus,bx-azure-secrets
```

### Via BoxLang OS Binary

```bash
install-bx-module bx-plus bx-azure-secrets
```

## ⚡ Quick Start

1. Install and activate `bx-plus` and `bx-azure-secrets`
2. Configure credentials through `this.azure`, module settings, or Azure `DefaultAzureCredential`
3. Resolve secrets with `azure.` namespaced keys

```js
dbPassword = getSystemSetting( "azure.DB-PASSWORD" )
apiKey = getSystemSetting( "azure.API-KEY", "fallback-key" )
```

## ⚙️ Basic Configuration

Use module settings in `boxlang.json` when you want global defaults:

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

{% hint style="info" %}
The module id for installation is `bx-azure-secrets`, while module settings are keyed under `bxazure-secrets`.
{% endhint %}

For per-app overrides and Azure CLI examples, see [Configuration & Usage](configuration-and-usage.md).

## 🔍 How Secret Resolution Works

For `getSystemSetting( "azure.MY-SECRET" )`, the provider:

1. Resolves effective Azure settings (3-tier lookup)
2. Checks in-memory cache using `vaultUrl:secretName`
3. Calls Azure Key Vault when cache is stale/missing
4. Caches and returns the secret value
5. Returns `null` on lookup failure, allowing standard BoxLang fallback behavior

## 🔗 Related Documentation

{% content-ref url="configuration-and-usage.md" %}
[configuration-and-usage.md](configuration-and-usage.md)
{% endcontent-ref %}

{% content-ref url="../../../../getting-started/configuration/modules.md" %}
[modules.md](../../../../getting-started/configuration/modules.md)
{% endcontent-ref %}

{% content-ref url="../bx-plus/" %}
[bx-plus](../bx-plus/)
{% endcontent-ref %}
