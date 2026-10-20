[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetRuntimeSetting`

**New in BoxLang 1.19.0**

Retrieve a user-defined runtime setting. Settings are defined in the `runtimeSettings` struct of `boxlang.json` and can be overridden (deep merged) by `this.runtimeSettings` in the Application descriptor. Values support `${env.X}` placeholders and `bxsecret:` values. The returned values are read-only.

<p>
 Use a dotted path to reach nested values, e.g. `features.beta`. Array elements can be reached with a 1-based index, e.g. `limits.1`. If no key is passed, the whole merged settings struct is returned.
 <p>
 If the key is not found and no default is provided, an exception is thrown.

## Method Signature

```
GetRuntimeSetting(key=[String], defaultValue=[Any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `key` | `String` | `false` | The name or dotted path of the setting to retrieve. Omit to retrieve all settings. |  |
| `defaultValue` | `Any` | `false` | The default value to return if the setting is not found |  |

## Examples

### Get a setting

```java
// boxlang.json: "runtimeSettings": { "apiUrl": "${env.API_URL:http://localhost}" }
apiUrl = getRuntimeSetting( "apiUrl" )
```

### Nested values and array indexes

```java
// "runtimeSettings": { "features": { "beta": true, "regions": [ "us", "eu" ] } }
isBeta = getRuntimeSetting( "features.beta" )
firstRegion = getRuntimeSetting( "features.regions.1" )
```

### With a default value

```java
timeout = getRuntimeSetting( "timeout", 30 )
```

### All settings

```java
all = getRuntimeSetting()
```

## Related

  * [Runtime Settings](../../../../getting-started/configuration/runtime-settings.md)
  * [GetSystemSetting](./GetSystemSetting.md)
  * [GetApplicationMetadata](./GetApplicationMetadata.md)
