---
description: >-
  AWS Secrets Manager integration for BoxLang system settings via the aws.
  namespace in getSystemSetting().
icon: key
---

# AWS Secrets +

{% hint style="danger" %}
This module is only available to [+/++ subscribers only](https://boxlang.io/plans), and requires a valid `bx-plus` license.
{% endhint %}

The `bx-aws-secrets` module registers an `aws` system setting provider so BoxLang can resolve secrets directly from AWS Secrets Manager using `getSystemSetting()`.

## ✨ Features

- Resolve secrets with `getSystemSetting( "aws.SECRET_NAME" )`
- 3-tier configuration resolution per setting: `this.aws` in `Application.bx`, module settings, then AWS environment variables
- In-memory TTL caching to reduce Secrets Manager API calls
- Per-application `SecretsManagerClient` isolation when `this.aws` is defined
- Automatic client cleanup on application shutdown
- Graceful fallback behavior: returns `null` on provider errors so normal `getSystemSetting()` fallback continues

## 📦 Requirements

- BoxLang 1.14+
- `bx-plus` module
- AWS IAM permissions to read secrets (`secretsmanager:GetSecretValue`)

## 🚀 Installation

### Via CommandBox

```bash
box install bx-plus,bx-aws-secrets
```

### Via BoxLang OS Binary

```bash
install-bx-module bx-plus bx-aws-secrets
```

## ⚡ Quick Start

1. Install and activate `bx-plus` and `bx-aws-secrets`
2. Configure credentials through `this.aws`, module settings, or AWS environment variables
3. Resolve secrets with `aws.` namespaced keys

```js
dbPassword = getSystemSetting( "aws.DB_PASSWORD" )
apiKey = getSystemSetting( "aws.API_KEY", "fallback-key" )
```

## ⚙️ Basic Configuration

Use module settings in `boxlang.json` when you want global defaults:

```json
{
  "modules": {
    "bxaws-secrets": {
      "settings": {
        "region": "us-east-2",
        "accessKeyId": "${AWS_ACCESS_KEY_ID}",
        "secretAccessKey": "${AWS_SECRET_ACCESS_KEY}",
        "sessionToken": "",
        "cacheTTL": 300,
        "endpointOverride": ""
      }
    }
  }
}
```

{% hint style="info" %}
The module id for installation is `bx-aws-secrets`, while module settings are keyed under `bxaws-secrets`.
{% endhint %}

For per-app overrides and LocalStack examples, see [Configuration & Usage](configuration-and-usage.md).

## 🔍 How Secret Resolution Works

For `getSystemSetting( "aws.MY_SECRET" )`, the provider:

1. Resolves effective AWS settings (3-tier lookup)
2. Checks in-memory cache using `region:secretName`
3. Calls AWS Secrets Manager when cache is stale/missing
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
