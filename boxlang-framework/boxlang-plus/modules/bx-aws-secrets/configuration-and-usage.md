---
description: >-
  Detailed configuration, credential resolution order, caching, and runtime
  behavior for the bx-aws-secrets module.
icon: sliders
---

# Configuration & Usage

This guide covers effective settings, credential source precedence, LocalStack support, and operational behavior for `bx-aws-secrets`.

## 🔧 Configuration Sources

Each setting is resolved independently in this order:

1. `this.aws` in `Application.bx` (per-application)
2. Module settings in `boxlang.json` (global)
3. AWS environment variables (where supported)

## 🧩 `Application.bx` (Per-App)

Use `this.aws` when each app needs isolated credentials or region-specific behavior.

```js
class {
    this.name = "myApp"

    this.aws = {
        region          : "us-east-2",
        accessKeyId     : "${AWS_ACCESS_KEY_ID}",
        secretAccessKey : "${AWS_SECRET_ACCESS_KEY}",
        sessionToken    : "",
        cacheTTL        : 300,
        endpointOverride : ""
    }
}
```

When `this.aws` is present, the module creates and reuses a dedicated `SecretsManagerClient` for that application.

## 🌍 Global `boxlang.json` Settings

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

## 🌱 Environment Variable Fallback

Supported environment mappings:

| Setting | Environment Variable(s) |
| --- | --- |
| `region` | `AWS_REGION`, fallback `AWS_DEFAULT_REGION` |
| `accessKeyId` | `AWS_ACCESS_KEY_ID` |
| `secretAccessKey` | `AWS_SECRET_ACCESS_KEY` |
| `sessionToken` | `AWS_SESSION_TOKEN` |

`cacheTTL` and `endpointOverride` are not sourced from environment variables by the module.

## 📋 Settings Reference

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `region` | string | `""` | AWS region (required for secret resolution) |
| `accessKeyId` | string | `""` | AWS access key id |
| `secretAccessKey` | string | `""` | AWS secret access key |
| `sessionToken` | string | `""` | Optional temporary credentials token |
| `cacheTTL` | numeric | `300` | Cache time-to-live in seconds |
| `endpointOverride` | string | `""` | Custom endpoint (for example LocalStack) |

## 🔐 Usage Examples

Resolve a secret directly:

```js
dbPassword = getSystemSetting( "aws.DB_PASSWORD" )
```

Resolve with a fallback value:

```js
apiToken = getSystemSetting( "aws.API_TOKEN", "dev-token" )
```

Use in datasource config:

```js
this.datasources = {
    main : {
        className : "org.postgresql.Driver",
        connectionString : "jdbc:postgresql://localhost:5432/app",
        username : "app_user",
        password : getSystemSetting( "aws.DB_PASSWORD" )
    }
}
```

## 🧠 Caching Behavior

- Cache key format is `region:secretName`
- Successful secret fetches are cached in-memory
- Expired entries are refreshed on next access
- Set `cacheTTL` to `0` for effectively no cache reuse

## 🏗 Client Lifecycle

- **Per-app client**: Used when `this.aws` exists
- **Global client**: Used when module settings provide region-based config
- **Env client**: Used when relying only on AWS environment variables

Per-app clients are closed on application shutdown, and all clients are closed on module/runtime shutdown.

## 🧪 Local Development with LocalStack

```json
{
  "modules": {
    "bxaws-secrets": {
      "settings": {
        "region": "us-east-1",
        "accessKeyId": "test",
        "secretAccessKey": "test",
        "endpointOverride": "http://localhost:4566"
      }
    }
  }
}
```

Create a test secret:

```bash
aws --endpoint-url=http://localhost:4566 secretsmanager create-secret \
  --name DB_PASSWORD \
  --secret-string "local-password"
```

## 🚨 Troubleshooting

- Secret returns `null`: verify region is resolved and secret name exists in AWS Secrets Manager
- License errors: confirm `bx-plus` is installed and licensed; for local testing, set `BX_AWS_DEV=true`
- Permission errors: ensure IAM policy includes `secretsmanager:GetSecretValue`
- Wrong module settings key: use `bxaws-secrets` under `modules` in `boxlang.json`
