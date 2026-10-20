---
description: Store your own global named settings in boxlang.json and override them per application
icon: sliders
---

# Runtime Settings

The `runtimeSettings` struct in `boxlang.json` is yours. Store any named values your applications need: API URLs, feature flags, limits, lists, nested structures. BoxLang does not interpret them, it only loads, resolves and serves them.

{% hint style="info" %}
**New in BoxLang 1.19.0**: the `runtimeSettings` configuration, the `this.runtimeSettings` Application.bx override and the `getRuntimeSetting()` BIF.
{% endhint %}

## 📝 Defining Settings

{% code title="boxlang.json" %}
```json
{
    "runtimeSettings": {
        "apiUrl": "${env.API_URL:http://localhost:8080}",
        "stripeKey": "bxsecret:AbC123...",
        "maxUploads": 10,
        "features": {
            "beta": true,
            "regions": [ "us", "eu" ]
        }
    }
}
```
{% endcode %}

* Keys are unique, as in any JSON object.
* Values can be **any type**: strings, numbers, booleans, structs, arrays.
* An empty struct is the default.

## 🔌 Environment Variables and Secrets

Every value, at any depth and inside arrays, supports the same interpolation as the rest of `boxlang.json`.

| Syntax | Resolves to |
| ------ | ----------- |
| `${env.VAR}` | The environment variable `VAR` |
| `${env.VAR:default}` | `VAR`, or `default` when it is not set |
| `${user-dir}`, `${user-home}`, `${boxlang-home}`, `${java-temp}` | The built-in path variables |
| `bxsecret:...` | A value encrypted with the runtime secret seed, decrypted when loaded |

Placeholders can resolve to `bxsecret:` values and are decrypted at that point, so `"${env.STRIPE_KEY}"` can hold an encrypted value.

{% hint style="warning" %}
An unresolved placeholder with no default stays as the literal text `${NAME}`. Always provide a default when a value is optional.
{% endhint %}

{% hint style="info" %}
Interpolated values are strings. `"${env.MAX_ITEMS:10}"` yields `"10"`, not the number `10`. Cast it when you read it, for example `val( getRuntimeSetting( "maxItems" ) )`.
{% endhint %}

## 🔍 Reading Settings

Use the [GetRuntimeSetting](../../boxlang-language/reference/built-in-functions/system/GetRuntimeSetting.md) BIF.

```js
getRuntimeSetting( "apiUrl" )
getRuntimeSetting( "features.beta" )          // dotted path into nested structs
getRuntimeSetting( "features.regions.1" )     // 1-based array index
getRuntimeSetting( "timeout", 30 )            // default when missing
getRuntimeSetting()                           // the whole merged struct
```

A missing key with no default throws an exception.

## 🏗️ Application Overrides

Runtime settings are hierarchical, like the rest of the configuration. An `Application.bx` can declare `this.runtimeSettings` and it is **deep merged** over the global values. The application wins by key.

```js
// Application.bx
class {

    this.name = "myApp"

    this.runtimeSettings = {
        apiUrl : "${env.MYAPP_API_URL:https://api.myapp.com}",
        features : { regions : [ "ap" ] }
    }

}
```

With the global settings above, inside this application:

| Setting | Value | Why |
| ------- | ----- | --- |
| `apiUrl` | `https://api.myapp.com` (or the env var) | App overrides the global value |
| `maxUploads` | `10` | Inherited from global |
| `features.beta` | `true` | Nested structs merge by key |
| `features.regions` | `[ "ap" ]` | Arrays and scalars are **replaced**, not merged |

The same works with the application component:

```js
bx:application name="myApp" runtimeSettings={ features : { beta : false } };
```

### When values are resolved

| Layer | Resolved |
| ----- | -------- |
| Global `boxlang.json` | Once, when the runtime configuration loads |
| `Application.bx` | At the start of **every request**, when the descriptor is re-read, then cached for the rest of that request |

Only `runtimeSettings` gets `${...}` interpolation in `Application.bx`. Other application settings are not interpolated. Secrets (`bxsecret:`) are decrypted for all application settings.

## 🔒 Read Only

The returned structs and arrays are deeply unmodifiable. Attempting to change them throws an exception. If you need mutable state, copy the value, or use the cache or application scope.

## ✅ Best Practices

* Keep secrets encrypted with `bxsecret:` or in environment variables, never plain text in the file.
* Always give optional values a default, either in `${env.X:default}` or in `getRuntimeSetting( key, default )`.
* Group related values in a struct, for example `features` or `payments`, and read them with a dotted path.
* Use `boxlang.json` for environment-wide policy and `Application.bx` for app-specific overrides.
