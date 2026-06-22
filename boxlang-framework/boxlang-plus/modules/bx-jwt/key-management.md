---
description: The bx-jwt named key registry — define keys once, reference them everywhere.
icon: key
---

# Key Management

The key registry lets you declare keys once in module configuration and reference them by name throughout your application. Keeping secrets in configuration (or environment variables) makes [key rotation](key-rotation.md), auditing, and secret-manager integration far easier than embedding keys in code.

## Defining Keys

Keys live in the `keys` setting of your `ModuleConfig.bx`:

```javascript
settings = {
    keys : {

        // HMAC secret — supports ${env.VAR} placeholder substitution
        "api-signing" : {
            algorithm : "HS256",
            secret    : "${env.JWT_HMAC_SECRET}"
        },

        // RSA key pair (PEM file paths or inline PEM strings)
        "api-rsa" : {
            algorithm  : "RS256",
            privateKey : "/etc/keys/api-private.pem",
            publicKey  : "/etc/keys/api-public.pem"
        },

        // Public-only key for verifying third-party tokens
        "partner-public" : {
            algorithm : "RS256",
            publicKey : "/etc/keys/partner-public.pem"
        },

        // JWK (JSON Web Key) defined inline
        "oidc-verify" : {
            algorithm : "RS256",
            jwk       : { kty: "RSA", n: "...", e: "AQAB" }
        }
    }
}
```

The registry is parsed once at module startup. Every entry can supply any combination of `secret`, `privateKey`, `publicKey`, and `jwk` — the module picks whichever the operation requires.

## Using Named Keys

Pass the key's name in place of raw key material. The algorithm is resolved from the key metadata, so you can omit it too:

```javascript
token   = jwtCreate( { sub: "u1" }, "api-signing" );
payload = jwtVerify( token, "api-signing" );
```

## Module-Wide Defaults

Set `defaultSigningKey` / `defaultVerifyKey` (and the encryption equivalents) to drop the key argument entirely:

```javascript
settings = {
    keys              : { "app" : { algorithm: "HS256", secret: "${env.JWT_SECRET}" } },
    defaultSigningKey : "app",
    defaultVerifyKey  : "app"
}
```

```javascript
token   = jwtCreate( { sub: "u1" } );
payload = jwtVerify( token );
```

See [Configuration](configuration.md) for the full list of default settings.

## Runtime Key Management

For dynamic key sources (KMS, Vault, rotating service accounts) you can manipulate the registry at runtime through `JWTService`:

```javascript
jwtService = getBoxContext().getRuntime().getGlobalService( "JWTService" );

// Register
jwtService.registerKey( "session-key", {
    algorithm : "HS256",
    secret    : generateSecureKey()
} );

// Inspect
names  = jwtService.getKeyNames();
hasKey = jwtService.hasKey( "session-key" );

// Remove
jwtService.removeKey( "session-key" );
```

## Picking the Right Key Type

| Use case                                        | Recommended                                                  |
| ----------------------------------------------- | ------------------------------------------------------------ |
| Two services you own                            | HMAC (`HS256`) — shortest setup, fastest                     |
| Public consumers verifying your tokens          | RSA or EC (`RS256` / `ES256`) — distribute public key only   |
| Verifying third-party / OIDC tokens             | Public-only RSA/EC entry, or a JWK fetched from the issuer   |
| Confidential payloads at rest in client storage | RSA-OAEP for JWE — see [Encryption (JWE)](encryption-jwe.md) |

## Related

* [Configuration](configuration.md) — all settings reference
* [Key Rotation](key-rotation.md)
* [Security Best Practices](security-best-practices.md)
* [JWTGenerateSecret()](reference/built-in-functions/JWTGenerateSecret.md)
* [JWTGenerateKeyPair()](reference/built-in-functions/JWTGenerateKeyPair.md)
