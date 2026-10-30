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

_New in 1.17.0._ Any string value prefixed with `bxsecret:` is automatically decrypted at runtime, wherever it appears — plaintext values elsewhere continue to work completely unchanged, so this is opt-in per value, not an all-or-nothing switch. Supported locations include:

* `boxlang.json` settings, anywhere in the tree
* `Application.bx` datasource definitions and other `this.*` settings
* Environment variable overrides and JSON environment variable placeholders
* Application component attributes (e.g. `<bx:application>`)
* Nested application settings, such as caches and mappings

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

It isn't limited to datasources — any config value can be encrypted, for example a third-party API key:

```json
{
	"api": {
		"key": "bxsecret:wfYldsN1NOxSAC6k6H4RKg=="
	}
}
```

A `bxsecret:` value can also live inside a `${...}` [placeholder](../configuration.md#environment-variable-substitution), so you can combine encryption with environment-driven overrides in the same config tree:

```json
"password": "${env.DB_PASSWORD:bxsecret:AbCdEf123...==}"
```

### The Secret Seed

Decryption uses a symmetric key (the "seed"). BoxLang automatically generates a unique seed per install and persists it at:

```
{boxlang-home}/config/.seed
```

{% hint style="danger" %}
This file must be retained and protected. Losing it makes every `bxsecret:` value in your config permanently undecryptable; anyone who obtains it can decrypt them. Treat it with the same care as the secrets it protects — keep it out of source control and back it up the same way you'd manage any other production credential.
{% endhint %}

Because the seed is generated per install, the same plaintext encrypted on two different runtimes produces two different `bxsecret:` values, and a value encrypted with one seed cannot be decrypted with another. For a cluster of servers — or any deployment where you need the same encrypted values to work across multiple runtimes — share one seed across them using one of:

* Copying the same `.seed` file to each runtime
* The `BOXLANG_SECURITY_SECRETSEED` environment variable
* The `security.secretSeed` setting in `boxlang.json` (**discouraged** — this setting itself is stored in plain text, which undermines the point of encrypting the rest of your config)

```bash
export BOXLANG_SECURITY_SECRETSEED=my-shared-seed-value
```

```bash
-Dboxlang.security.secretSeed=my-shared-seed-value
```

The algorithm used for encryption/decryption is controlled by `security.secretAlgorithm` (default `AES`, shown above) — note that this setting itself is always read as plain text.

## Software Bill of Materials (SBOM)

Every BoxLang release build publishes a [CycloneDX](https://cyclonedx.org/) Software Bill of Materials (SBOM) next to its binaries. An SBOM lists the third-party libraries an artifact depends on, with their names and versions, so you can check them against vulnerability databases and answer supply-chain and compliance questions without unpacking the jars.

The SBOM is generated from the resolved dependency graph of each project, not from the shaded jar. Shading removes the `META-INF/maven` metadata that scanners rely on, so scanning a shaded jar directly misses the libraries bundled inside it.

### Where to Find Them

Each project publishes its own SBOM and a SHA-256 checksum in the same download folder as its other artifacts. Replace `<version>` with the release version.

| Project | Download folder |
| --- | --- |
| BoxLang | `https://downloads.ortussolutions.com/ortussolutions/boxlang/<version>/` |
| MiniServer | `https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-miniserver/<version>/` |
| Servlet | `https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-servlet/<version>/` |
| Web Support | `https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-web-support/<version>/` |
| AWS Lambda | `https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-aws-lambda/<version>/` |
| Azure Functions | `https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-azure-functions/<version>/` |
| Google Cloud Functions | `https://downloads.ortussolutions.com/ortussolutions/boxlang-runtimes/boxlang-google-functions/<version>/` |

In each folder the files are named after the project:

* `<artifact>-<version>.cdx.json` is the SBOM
* `<artifact>-<version>.cdx.json.sha256` is its checksum

For example, the BoxLang SBOM for version `1.19.0` is `boxlang-1.19.0.cdx.json`. Both files are also attached to the matching GitHub release.

{% hint style="info" %}
SBOMs are published for releases built after this feature was added. Older versions do not have one.
{% endhint %}

### Verify the Checksum

Download the SBOM and its checksum into the same folder, then verify:

```bash
sha256sum -c boxlang-<version>.cdx.json.sha256
```

On macOS you can use `shasum -a 256 -c` instead of `sha256sum -c`.

### Scan an SBOM

Any tool that reads CycloneDX can consume the file. For example, with [Grype](https://github.com/anchore/grype):

```bash
grype sbom:boxlang-<version>.cdx.json
```

### What an SBOM Covers

* **Runtime dependencies only.** Test dependencies are excluded.
* **One SBOM per project.** BoxLang and each runtime publish their own.
* **Runtimes do not list BoxLang itself.** The runtimes (MiniServer, Servlet, AWS Lambda, Azure Functions and Google Cloud Functions) bundle the BoxLang jar, but it is not listed in their SBOM. To audit a runtime, also use the BoxLang SBOM for the matching release.
* **Snapshot builds** produce files named `<artifact>-<version>-snapshot.cdx.json`.
