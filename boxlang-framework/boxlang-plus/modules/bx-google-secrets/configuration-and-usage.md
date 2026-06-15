---
description: >-
  Detailed configuration, credential resolution order, caching, and runtime
  behavior for the bx-google-secrets module.
icon: sliders
---

# Configuration & Usage

This guide covers effective settings, credential source precedence, local development, and operational behavior for `bx-google-secrets`.

## 🔧 Configuration Sources

Each setting is resolved independently in this order:

1. `this.google` in `Application.bx` (per-application)
2. Module settings in `boxlang.json` (global)
3. Google environment variables / Application Default Credentials

## 🧩 `Application.bx` (Per-App)

Use `this.google` when each app needs isolated project or credential behavior.

```js
class {
    this.name = "myApp"

    this.google = {
        projectId       : "my-gcp-project",
        credentialsPath : "${GOOGLE_APPLICATION_CREDENTIALS}",
        credentialsJson : "",
        cacheTTL        : 300
    }
}
```

When `this.google` is present, the module creates and reuses a dedicated `SecretManagerServiceClient` for that application.

## 🌍 Global `boxlang.json` Settings

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

## 🌱 Environment Variable Fallback

Supported environment mappings:

| Setting | Environment Variable(s) |
| --- | --- |
| `projectId` | `GOOGLE_CLOUD_PROJECT`, fallback `GCLOUD_PROJECT` |
| `credentialsPath` | `GOOGLE_APPLICATION_CREDENTIALS` |
| `credentialsJson` | `GOOGLE_CREDENTIALS_JSON` |

If explicit credentials are not configured, the module can also rely on Google Application Default Credentials from environments such as Cloud Run, GKE, Compute Engine, App Engine, or a locally authenticated `gcloud` session.

## 📋 Settings Reference

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `projectId` | string | `""` | Google Cloud project ID required for secret resolution |
| `credentialsPath` | string | `""` | Optional service account JSON file path |
| `credentialsJson` | string | `""` | Optional raw service account JSON content |
| `cacheTTL` | numeric | `300` | Cache time-to-live in seconds |

## 🔐 Usage Examples

Resolve a secret directly:

```js
dbPassword = getSystemSetting( "google.DB_PASSWORD" )
```

Resolve with a fallback value:

```js
apiToken = getSystemSetting( "google.API_TOKEN", "dev-token" )
```

Use in datasource config:

```js
this.datasources = {
    main : {
        className : "org.postgresql.Driver",
        connectionString : "jdbc:postgresql://localhost:5432/app",
        username : "app_user",
        password : getSystemSetting( "google.DB_PASSWORD" )
    }
}
```

## 🧠 Caching Behavior

- Cache key format is `projectId:secretName`
- Successful secret fetches are cached in-memory
- Expired entries are refreshed on next access
- Set `cacheTTL` to `0` for effectively no cache reuse

## 🏗 Client Lifecycle

- **Per-app client**: Used when `this.google` exists
- **Global client**: Used when module settings provide project-based config
- **ADC/env client**: Used when relying only on environment credentials or Google Application Default Credentials

Per-app clients are closed on application shutdown, and all clients are closed on module/runtime shutdown.

## 🧪 Local Development with gcloud

Authenticate with Google Cloud CLI and set a project:

```bash
gcloud auth application-default login
export GOOGLE_CLOUD_PROJECT="my-gcp-project"
gcloud secrets create DB_PASSWORD --replication-policy="automatic"
gcloud secrets versions add DB_PASSWORD --data-file=- <<< "local-password"
```

Minimal module settings:

```json
{
  "modules": {
    "bxgoogle-secrets": {
      "settings": {
        "projectId": "my-gcp-project"
      }
    }
  }
}
```

## 🚨 Troubleshooting

- Secret returns `null`: verify `projectId` is resolved and the secret exists in Google Secret Manager
- License errors: confirm `bx-plus` is installed and licensed; for local testing, set `BX_GOOGLE_DEV=true`
- Permission errors: ensure the runtime identity can access secret versions
- Wrong module settings key: use `bxgoogle-secrets` under `modules` in `boxlang.json`
