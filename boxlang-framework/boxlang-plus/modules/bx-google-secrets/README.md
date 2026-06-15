---
description: >-
  Google Secret Manager integration for BoxLang system settings via the google.
  namespace in getSystemSetting().
icon: key
---

# Google Secrets +

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://boxlang.io/plans), and requires a valid `bx-plus` license.
{% endhint %}

The `bx-google-secrets` module registers a `google` system setting provider so BoxLang can resolve secrets directly from Google Secret Manager using `getSystemSetting()`.

## ✨ Features

- Resolve secrets with `getSystemSetting( "google.SECRET_NAME" )`
- 3-tier configuration resolution per setting: `this.google` in `Application.bx`, module settings, then Google environment variables/Application Default Credentials
- In-memory TTL caching to reduce Secret Manager API calls
- Per-application `SecretManagerServiceClient` isolation when `this.google` is defined
- Automatic client cleanup on application shutdown
- Graceful fallback behavior: returns `null` on provider errors so normal `getSystemSetting()` fallback continues

## 📦 Requirements

- BoxLang 1.14+
- `bx-plus` module
- Google Cloud project with Secret Manager enabled
- Google identity with `secretmanager.versions.access` permission

## 🚀 Installation

### Via CommandBox

```bash
box install bx-plus,bx-google-secrets
```

### Via BoxLang OS Binary

```bash
install-bx-module bx-plus bx-google-secrets
```

## ⚡ Quick Start

1. Install and activate `bx-plus` and `bx-google-secrets`
2. Configure credentials through `this.google`, module settings, or Google Application Default Credentials
3. Resolve secrets with `google.` namespaced keys

```js
dbPassword = getSystemSetting( "google.DB_PASSWORD" )
apiKey = getSystemSetting( "google.API_KEY", "fallback-key" )
```

## ⚙️ Basic Configuration

Use module settings in `boxlang.json` when you want global defaults:

```json
{
  "modules": {
    "bxgoogle-secrets": {
      "settings": {
        "projectId": "my-gcp-project",
        "credentialsPath": "${GOOGLE_APPLICATION_CREDENTIALS}",
        "credentialsJson": "",
        "cacheTTL": 300
      }
    }
  }
}
```

{% hint style="info" %}
The module id for installation is `bx-google-secrets`, while module settings are keyed under `bxgoogle-secrets`.
{% endhint %}

For per-app overrides and local development examples, see [Configuration & Usage](configuration-and-usage.md).

## 🔍 How Secret Resolution Works

For `getSystemSetting( "google.MY_SECRET" )`, the provider:

1. Resolves effective Google settings (3-tier lookup)
2. Checks in-memory cache using `projectId:secretName`
3. Calls Google Secret Manager when cache is stale/missing
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
