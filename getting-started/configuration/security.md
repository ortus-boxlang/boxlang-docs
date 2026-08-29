---
description: Configure the security settings in BoxLang
icon: shield-cross
---

# Security

This segment is where you can configure the security elements of BoxLang under the `security`block in the `boxlang.json`

{% code title="boxlang.json" %}
```json5
// These are the security settings for the runtime
"security": {
	// All regex patterns are case-insensitive
	// A list of regex patterns that will match class paths, and if matched, execution will be disallowed
	// This applies to import statements, createObject, new, and class creation
	// Ex: "disallowedImports": ["java\\.lang\\.(ProcessBuilder|Reflect", "java\\.io\\.(File|FileWriter)"]
	"disallowedImports": [],
	// A list of BIF names that will be disallowed from execution
	// Ex: "disallowedBifs": ["createObject", "systemExecute"]
	"disallowedBifs": [],
	// A list of Component names that will be disallowed from execution
	// Ex: "disallowedComponents": [ "execute", "http" ]
	"disallowedComponents": [],
	// This is a boolean flag that determines if the server.system scope will be populated with the
	// Java system properties and environment variables. By default this is set to true.
	"populateServerSystemScope": true,
	// An explicit whitelist of file extensions that are allowed to be uploaded - overrides any values in the disallowedWriteExtensions
	"allowedFileOperationExtensions": [],
	// The list of file extensions that are not allowed to be uploaded. Also enforced by file relocation operations ( e.g. copy/move )
	"disallowedFileOperationExtensions": [],
	// The algorithm used to decrypt "bxsecret:" encrypted configuration values
	"secretAlgorithm": "AES"
},
```
{% endcode %}

## Allowed File Operation Extensions

An explicit whitelist of file extensions that are allowed to be uploaded - overrides any values in the `disallowedWriteExtensions`

```json
"allowedFileOperationExtensions": [],
```

Individual file extensions may be whitelisted in your Application context like so:

```
this.allowedFileOperationExtensions = [ "bxm", "bx" ];
```

Anything placed in the allowed extensions overrides the disallowed extensions array

## Disallowed Imports

An array of regex patterns (case-sensitive) that will try to be matched to imports or to creation of classes. If they match the patterns a security exception wil be thrown.

```json
// Ex: "disallowedImports": ["java\\.lang\\.(ProcessBuilder|Reflect", "java\\.io\\.(File|FileWriter)"]
"disallowedImports": [],
```

## Disallowed BIFS

An array of BIF names that will be disallowed from execution.

```json
// Ex: "disallowedBifs": ["createObject", "systemExecute"]
"disallowedBifs": [],
```

## Disallowed Components

An array of Component names that will be disallowed from execution.

```json
// Ex: "disallowedComponents": ["execute", "http"]
"disallowedComponents": [],
```

## Disallowed File Operation Extensions

The list of file extensions that are not allowed to be uploaded. Also enforced by file relocation operations ( e.g. copy/move ).  By default, in the CLI and Lambda runtimes,  we don't restrict, but you can :)

In Web runtimes, the following extensions are disallowed by default.   Unlike other engines this list does not apply to just uploads but applies to File move and copy operations.  This is enforced to prevent a bad actor from uploading a file with one extension and being able to copy it to another that is executable.

```json
"disallowedFileOperationExtensions": [
		"bat",
		"exe",
		"cmd",
		"cfm",
		"cfc",
		"cfs",
		"bx",
		"bxm",
		"bxs",
		"sh",
		"php",
		"pl",
		"cgi",
		"386",
		"dll",
		"com",
		"torrent",
		"js",
		"app",
		"jar",
		"pif",
		"vb",
		"vbscript",
		"wsf",
		"asp",
		"cer",
		"csr",
		"jsp",
		"drv",
		"sys",
		"ade",
		"adp",
		"bas",
		"chm",
		"cpl",
		"crt",
		"csh",
		"fxp",
		"hlp",
		"hta",
		"inf",
		"ins",
		"isp",
		"jse",
		"htaccess",
		"htpasswd",
		"ksh",
		"lnk",
		"mdb",
		"mde",
		"mdt",
		"mdw",
		"msc",
		"msi",
		"msp",
		"mst",
		"ops",
		"pcd",
		"prg",
		"reg",
		"scr",
		"sct",
		"shb",
		"shs",
		"url",
		"vbe",
		"vbs",
		"wsc",
		"wsf",
		"wsh"
	],
```

**Note:** If you wish to override a single extension you may do so by placing the extension in the `allowedFileOperationExtensions` setting in the application:

```
this.allowedFileOperationExtensions = [ "bxm", "bx" ];
```

## populateServerSystemScope

This is a boolean flag that, if enabled, will populate the `server.system` scope with the Java environment and properties.  If disabled, it will not populate them and users will only be able to get environment and properties via the `getSystemSetting()` BIF. &#x20;

```json
"populateServerSystemScope" : false
```

## Encrypted Configuration Secrets — `bxsecret:`

_New in 1.17.0._ Any string value anywhere in your config tree — `boxlang.json` or `Application.bx` settings — can be encrypted instead of stored as plain text. BoxLang decrypts it automatically, in place, the moment the config is loaded.

Generate an encrypted value with the `generatesecret` CLI action, using the runtime's active secret seed:

```bash
boxlang generatesecret "s3cr3tPassw0rd"
# => bxsecret:AbCdEf123...==
```

Then use the resulting `bxsecret:...` value anywhere a config value is read — most commonly a datasource password:

```json
{
	"datasources": {
		"myDS": {
			"driver": "mysql",
			"properties": { "host": "localhost", "database": "myapp" },
			"username": "app_user",
			"password": "bxsecret:AbCdEf123...=="
		}
	}
}
```

A `bxsecret:` value can also live inside a `${...}` [placeholder](../configuration.md#environment-variable-substitution), so you can combine encryption with environment-driven overrides in the same config tree:

```json
"password": "${env.DB_PASSWORD:bxsecret:AbCdEf123...==}"
```

### The Secret Seed

Decryption uses a symmetric key (the "seed") that is auto-generated and persisted per-install the first time it's needed. For reproducible deployments — or to share the same seed across a cluster of servers — pin it explicitly via an environment variable or JVM system property:

```bash
export BOXLANG_SECURITY_SECRETSEED=my-shared-seed-value
```

```bash
-Dboxlang.security.secretSeed=my-shared-seed-value
```

{% hint style="danger" %}
Anyone who has the seed can decrypt every `bxsecret:` value in your config. Treat it with the same care as the secrets it protects — keep it out of source control and manage it the same way you'd manage any other production credential.
{% endhint %}

The algorithm used for encryption/decryption is controlled by `security.secretAlgorithm` (default `AES`, shown above).
