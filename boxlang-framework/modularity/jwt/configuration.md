---
icon: gear
description: Complete reference for every bx-jwt configuration setting.
---

# Configuration

Configure defaults and the key registry in your application's `ModuleConfig.bx`, or in the module-level configuration. All settings are optional; sensible defaults ship with the module.

```javascript
settings = {

    // ----------------------------------------------------------------
    // Key Registry
    // ----------------------------------------------------------------
    keys : {
        // "myapp-hmac" : { algorithm : "HS256", secret : "${env.JWT_SECRET}" },
        // "myapp-rsa"  : { algorithm : "RS256", privateKey : "/path/to/private.pem", publicKey : "/path/to/public.pem" }
    },

    // ----------------------------------------------------------------
    // Signature Defaults
    // ----------------------------------------------------------------
    defaultSigningKey    : "",
    defaultVerifyKey     : "",
    defaultAlgorithm     : "HS256",

    // ----------------------------------------------------------------
    // Encryption Defaults
    // ----------------------------------------------------------------
    defaultEncryptionKey : "",
    defaultDecryptionKey : "",
    defaultKeyAlgorithm  : "RSA-OAEP-256",
    defaultEncAlgorithm  : "A256GCM",

    // ----------------------------------------------------------------
    // Token Behavior
    // ----------------------------------------------------------------
    generateIat          : true,
    generateJti          : true,
    clockSkew            : 60,

    // ----------------------------------------------------------------
    // Default Claims (auto-injected when missing from the payload)
    // ----------------------------------------------------------------
    defaultIssuer        : "",
    defaultAudience      : "",
    defaultExpiration    : 0,

    // ----------------------------------------------------------------
    // Security
    // ----------------------------------------------------------------
    allowedAlgorithms    : []
}
```

## Settings Reference

| Setting                | Type      | Default          | Purpose                                                                                                       |
| ---------------------- | --------- | ---------------- | ------------------------------------------------------------------------------------------------------------- |
| `keys`                 | `struct`  | `{}`             | Named key registry. Each entry can declare an `algorithm`, `secret`, `privateKey`, `publicKey`, and/or `jwk`. |
| `defaultSigningKey`    | `string`  | `""`             | Named key used by `jwtCreate()` / `jwtRefresh()` when no key argument is provided.                            |
| `defaultVerifyKey`     | `string`  | `""`             | Named key used by `jwtVerify()` / `jwtValidate()` when no key argument is provided.                           |
| `defaultAlgorithm`     | `string`  | `HS256`          | Algorithm used when the BIF call omits one and the key has none declared.                                     |
| `defaultEncryptionKey` | `string`  | `""`             | Named key used by `jwtEncrypt()` when no key is provided.                                                     |
| `defaultDecryptionKey` | `string`  | `""`             | Named key used by `jwtDecrypt()` when no key is provided.                                                     |
| `defaultKeyAlgorithm`  | `string`  | `RSA-OAEP-256`   | Default JWE key management algorithm.                                                                          |
| `defaultEncAlgorithm`  | `string`  | `A256GCM`        | Default JWE content encryption algorithm.                                                                      |
| `generateIat`          | `boolean` | `true`           | Auto-inject the `iat` claim when missing from the payload.                                                     |
| `generateJti`          | `boolean` | `true`           | Auto-inject the `jti` claim when missing from the payload.                                                     |
| `clockSkew`            | `numeric` | `60`             | Seconds of tolerance applied to `exp` / `nbf` validation.                                                      |
| `defaultIssuer`        | `string`  | `""`             | Auto-inject `iss` claim when missing. Leave empty to disable.                                                  |
| `defaultAudience`      | `string`  | `""`             | Auto-inject `aud` claim when missing.                                                                          |
| `defaultExpiration`    | `numeric` | `0`              | Seconds from now to auto-inject `exp`. `0` disables auto-expiry.                                               |
| `allowedAlgorithms`    | `array`   | `[]`             | Algorithm allowlist. Empty = allow all supported algorithms.                                                   |

## Key Registry Entry Shape

| Property     | Type     | Description                                                                            |
| ------------ | -------- | -------------------------------------------------------------------------------------- |
| `algorithm`  | `string` | The JWS or JWE algorithm this key is intended for (e.g. `HS256`, `RS256`).             |
| `secret`     | `string` | HMAC secret. Supports `${env.VAR}` placeholder substitution.                           |
| `privateKey` | `string` | PEM-encoded private key, or a filesystem path to a PEM file.                           |
| `publicKey`  | `string` | PEM-encoded public key, or a filesystem path to a PEM file.                            |
| `jwk`        | `struct` | Inline JSON Web Key.                                                                   |

See the [Key Management Guide](key-management.md) for examples of every key type.

## Zero-Argument BIFs

When defaults are fully configured, the `key` and `algorithm` arguments become optional:

```javascript
settings = {
    keys              : { "app" : { algorithm: "HS256", secret: "${env.JWT_SECRET}" } },
    defaultSigningKey : "app",
    defaultVerifyKey  : "app",
    defaultAlgorithm  : "HS256",
    defaultIssuer     : "my-api",
    defaultAudience   : "web",
    defaultExpiration : 3600
}
```

```javascript
token   = jwtCreate( { sub: "user-123" } );  // no key/algorithm needed
payload = jwtVerify( token );
```

## Related

* [Key Management](key-management.md)
* [Security Best Practices](security-best-practices.md)
* [Algorithms](reference/algorithms.md)
