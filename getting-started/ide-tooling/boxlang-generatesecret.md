---
description: Encrypt configuration values with the BoxLang generatesecret CLI action.
icon: key
---

# 🔐 BoxLang Generate Secret

The BoxLang Generate Secret tool (`generatesecret`) encrypts a plaintext value using the runtime's active security secret seed. It returns a `bxsecret:` value that BoxLang can decrypt automatically when it reads configuration.

This is useful for protecting datasource passwords, API keys, and other sensitive configuration values without storing them as plaintext in `boxlang.json` or `Application.bx`.

## Usage

Make sure you have installed the OS version of [BoxLang](../installation/) so the `boxlang` binary and its CLI actions are available.

```bash
boxlang generatesecret "s3cr3tPassw0rd"
```

The command prints an encrypted value prefixed with `bxsecret:`:

```text
bxsecret:AbCdEf123...==
```

Copy the complete value, including the `bxsecret:` prefix, into the configuration setting that contains the secret.

## Configuration Example

Use the generated value anywhere BoxLang reads a configuration value. For example, a datasource password can be stored as:

```json
{
  "datasources": {
    "myDS": {
      "driver": "mysql",
      "properties": {
        "host": "localhost",
        "database": "myapp"
      },
      "username": "app_user",
      "password": "bxsecret:AbCdEf123...=="
    }
  }
}
```

BoxLang decrypts `bxsecret:` values automatically at runtime. See [Encrypted Configuration Secrets](../configuration/security.md#encrypted-configuration-secrets--bxsecret) for supported configuration locations, including environment variable placeholders and application settings.

## Secret Seed

Encryption and decryption use the runtime's active secret seed. BoxLang generates a unique seed per installation and stores it at:

```text
{boxlang-home}/config/.seed
```

Protect and retain this file. Values encrypted with one seed cannot be decrypted with another, so losing the seed makes the corresponding configuration values permanently undecryptable.

For a cluster or another deployment that needs to decrypt the same values across multiple runtimes, share the same seed through one of these options:

* Copy the same `.seed` file to each runtime.
* Set the `BOXLANG_SECURITY_SECRETSEED` environment variable.
* Set `security.secretSeed` in `boxlang.json` (not recommended because the seed is then stored in plaintext).

```bash
export BOXLANG_SECURITY_SECRETSEED=my-shared-seed-value
boxlang generatesecret "s3cr3tPassw0rd"
```

{% hint style="danger" %}
Never commit the `.seed` file or plaintext secrets to source control. Anyone who obtains the seed can decrypt values generated with it.
{% endhint %}

## Related Documentation

* [Encrypted Configuration Secrets](../configuration/security.md#encrypted-configuration-secrets--bxsecret)
* [BoxLang CLI Scripting](../running-boxlang/cli-scripting.md)
