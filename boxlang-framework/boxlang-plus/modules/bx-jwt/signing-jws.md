---
description: Sign and verify JWTs with HMAC, RSA, and EC keys.
icon: pen
---

# Signing (JWS)

A JSON Web Signature (JWS) is a JWT whose payload has been signed — anyone with the verification key can confirm the token was issued by the holder of the signing key and that the claims have not been tampered with.

This guide walks through the three signing families that `bx-jwt` supports:

* **HMAC** (HS256, HS384, HS512) — symmetric, one key signs and verifies
* **RSA** (RS256, RS384, RS512) — asymmetric, private signs / public verifies
* **EC** (ES256, ES384, ES512) — asymmetric, smaller keys than RSA

## HMAC

HMAC is the simplest option: a single shared secret signs and verifies the token. Use it when both ends of the conversation are services you control.

```javascript
// Generate an RFC 7518–compliant 256-bit secret
secret = jwtGenerateSecret( 256 );

token   = jwtCreate( { sub: "user-123", iss: "my-api" }, secret, "HS256" );
payload = jwtVerify( token, secret, "HS256" );
```

{% hint style="warning" %}
HMAC keys must meet the minimum lengths in RFC 7518 §3.2 (HS256 = 32 bytes, HS384 = 48 bytes, HS512 = 64 bytes). [`jwtGenerateSecret()`](reference/built-in-functions/JWTGenerateSecret.md) always produces a compliant key.
{% endhint %}

## RSA

RSA gives you asymmetric signing: a private key issues tokens, a public key verifies them. Distribute the public key freely — give the private key only to the issuer.

```javascript
keys    = jwtGenerateKeyPair( "RS256" );  // 2048-bit RSA pair
token   = jwtCreate( { sub: "user-123" }, keys.privateKey, "RS256" );
payload = jwtVerify( token, keys.publicKey, "RS256" );
```

For long-lived production keys, persist the PEM strings to disk or to a secret manager and reference them through the [key registry](key-management.md).

## EC (Elliptic Curve)

EC signing produces dramatically smaller signatures and key material than RSA at equivalent security levels.

```javascript
keys    = jwtGenerateKeyPair( "ES256" );  // P-256
token   = jwtCreate( { sub: "user-123" }, keys.privateKey, "ES256" );
payload = jwtVerify( token, keys.publicKey, "ES256" );
```

## Verifying with Claim Assertions

Pass a `claims` struct to `jwtVerify()` to enforce expected values:

```javascript
payload = jwtVerify( token, secret, "HS256", {
    claims: { iss: "my-api", aud: "mobile-app" }
} );
```

A mismatch throws `bxjwt.JWTVerificationException`.

## Verify vs Validate vs Decode

| BIF                                                            | Returns             | Throws on failure | Use when…                                                  |
| -------------------------------------------------------------- | ------------------- | ----------------- | ---------------------------------------------------------- |
| [`jwtVerify()`](reference/built-in-functions/JWTVerify.md)     | claims struct       | Yes               | You need the claims and want exception-driven flow.        |
| [`jwtValidate()`](reference/built-in-functions/JWTValidate.md) | boolean             | No                | Simple yes/no check (e.g. middleware guard).               |
| [`jwtDecode()`](reference/built-in-functions/JWTDecode.md)     | `{header, payload}` | No                | You need to read the header (e.g. `kid`) before verifying. |

## Refreshing Tokens

Use [`jwtRefresh()`](reference/built-in-functions/JWTRefresh.md) to re-issue an existing token with fresh `iat`, `jti`, and an optional new `exp`. All application claims are preserved.

```javascript
newToken = jwtRefresh( oldToken, secret, "HS256", {
    allowExpired : true,
    expireIn     : 3600
} );
```

## Related

* [Encryption (JWE)](encryption-jwe.md)
* [Key Management](key-management.md)
* [Key Rotation](key-rotation.md)
* [Security Best Practices](security-best-practices.md)
* [Algorithms](reference/algorithms.md)
