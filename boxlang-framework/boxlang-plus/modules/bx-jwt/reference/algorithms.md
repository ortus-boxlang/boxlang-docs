---
description: Supported JWS signing and JWE encryption algorithms for the bx-jwt module.
---

# Algorithms

`bx-jwt` follows RFC 7518 (JSON Web Algorithms). The tables below summarize every algorithm registered by the module — including key requirements — so you can pick the right one for your use case.

## Signing (JWS)

| Algorithm | Type     | Min Key Size        | Notes                                                |
| --------- | -------- | ------------------- | ---------------------------------------------------- |
| `HS256`   | HMAC     | 256 bits (32 bytes) | Symmetric — same key signs and verifies.             |
| `HS384`   | HMAC     | 384 bits (48 bytes) | Symmetric.                                           |
| `HS512`   | HMAC     | 512 bits (64 bytes) | Symmetric.                                           |
| `RS256`   | RSA      | 2048-bit            | Asymmetric — private key signs, public key verifies. |
| `RS384`   | RSA      | 2048-bit            | Asymmetric.                                          |
| `RS512`   | RSA      | 4096-bit            | Asymmetric.                                          |
| `ES256`   | EC P-256 | —                   | Asymmetric, smaller keys than RSA.                   |
| `ES384`   | EC P-384 | —                   | Asymmetric.                                          |
| `ES512`   | EC P-521 | —                   | Asymmetric.                                          |

{% hint style="info" %}
HMAC minimum key lengths are enforced at parse time per RFC 7518 §3.2. Use [`jwtGenerateSecret( bits )`](built-in-functions/JWTGenerateSecret.md) to always produce a compliant key.
{% endhint %}

## Encryption (JWE)

| Key Algorithm  | Content Encryption | Key Type                         |
| -------------- | ------------------ | -------------------------------- |
| `RSA-OAEP-256` | `A256GCM`          | RSA public/private key pair.     |
| `dir`          | `A256GCM`          | 256-bit symmetric secret (32 B). |

## `alg:none` is Unconditionally Rejected

The module **always rejects** unsigned tokens (`alg:none`). Passing such a token to `jwtVerify()` or `jwtRefresh()` throws `bxjwt.JWTVerificationException`.

## Restricting Algorithms

Use the `allowedAlgorithms` setting in your `ModuleConfig.bx` to lock down the algorithms your application accepts:

```javascript
allowedAlgorithms = [ "HS256", "RS256", "ES256" ]
```

See [Security Best Practices](../security-best-practices.md) for guidance on choosing an allowlist.

## Related

* [JWTGenerateSecret()](built-in-functions/JWTGenerateSecret.md)
* [JWTGenerateKeyPair()](built-in-functions/JWTGenerateKeyPair.md)
* [Signing (JWS) Guide](../signing-jws.md)
* [Encryption (JWE) Guide](../encryption-jwe.md)
