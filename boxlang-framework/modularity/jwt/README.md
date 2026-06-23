---
icon: key
description: >-
  JWT module for BoxLang providing complete JWS signing, JWE
  encryption, and a fluent token builder with RFC 7518 / RFC 7519 compliance.
---

# JWT - Json Web Tokens

The `bx-jwt` module is a production-ready BoxLang library for creating, signing, verifying, encrypting, and decrypting JSON Web Tokens (JWT/JWE). It implements:

* **JWS** (JSON Web Signature) — signed tokens using HMAC, RSA, or EC keys
* **JWE** (JSON Web Encryption) — encrypted tokens using RSA or symmetric keys
* **RFC 7518** — JSON Web Algorithms
* **RFC 7519** — JSON Web Token

## 🚀 Key Features

* 🔑 **HMAC Signing** — HS256, HS384, HS512 with RFC 7518 minimum key length enforcement
* 🔐 **RSA Signing** — RS256, RS384, RS512
* 📐 **EC Signing** — ES256 (P-256), ES384 (P-384), ES512 (P-521)
* 🔒 **JWE Encryption** — RSA-OAEP-256, direct symmetric (`dir`) with A256GCM
* 🗝️ **Named Key Registry** — register keys by name in module config; reference by name in BIFs
* 🏗️ **Fluent Builder** — `jwtNew()` returns a chainable builder for elegant token creation
* ♻️ **Token Refresh** — `jwtRefresh()` re-issues tokens with fresh time claims
* 🔓 **Decode Without Verify** — `jwtDecode()` to inspect headers/claims before choosing a key
* ✅ **Boolean Validation** — `jwtValidate()` returns true/false without throwing
* 🔧 **Key Generation** — `jwtGenerateSecret()` and `jwtGenerateKeyPair()` helpers
* ⏱️ **Clock Skew** — configurable tolerance for `exp` / `nbf` validation
* 📋 **Default Claims** — auto-inject `iss`, `aud`, `exp`, `iat`, `jti` from module settings
* 🚫 **`alg:none` Protection** — unconditionally rejects unsigned tokens
* 📋 **Algorithm Allowlist** — restrict permitted algorithms via module settings

## 📦 Installation

```bash
# Operating Systems using the Quick Installer
install-bx-module bx-jwt

# Using CommandBox for web servers
box install bx-jwt
```

## 🎯 Registered BIFs

This module registers the following Built-In Functions (BIFs):

| Function              | Purpose                                                                | Documentation                                                                                  |
| --------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `jwtNew()`            | Returns a fluent `JwtBuilder` for chainable token construction         | [Fluent Builder](fluent-builder.md)                                                            |
| `jwtCreate()`         | Signs a payload and returns a compact JWS token string                 | [JWTCreate](reference/built-in-functions/JWTCreate.md)                                         |
| `jwtVerify()`         | Verifies a JWS signature & claims; throws on failure                   | [JWTVerify](reference/built-in-functions/JWTVerify.md)                                         |
| `jwtValidate()`       | Like `jwtVerify()` but returns true/false instead of throwing          | [JWTValidate](reference/built-in-functions/JWTValidate.md)                                     |
| `jwtDecode()`         | Decodes a JWS token **without** verifying the signature                | [JWTDecode](reference/built-in-functions/JWTDecode.md)                                         |
| `jwtRefresh()`        | Re-issues a token with fresh `iat`, `jti`, optional new `exp`          | [JWTRefresh](reference/built-in-functions/JWTRefresh.md)                                       |
| `jwtEncrypt()`        | Encrypts a payload as a compact JWE token                              | [JWTEncrypt](reference/built-in-functions/JWTEncrypt.md)                                       |
| `jwtDecrypt()`        | Decrypts a JWE token and returns the claims struct                     | [JWTDecrypt](reference/built-in-functions/JWTDecrypt.md)                                       |
| `jwtGenerateSecret()` | Generates a cryptographically random Base64 HMAC secret (default: 256) | [JWTGenerateSecret](reference/built-in-functions/JWTGenerateSecret.md)                         |
| `jwtGenerateKeyPair()`| Generates an RSA or EC key pair as PEM strings                         | [JWTGenerateKeyPair](reference/built-in-functions/JWTGenerateKeyPair.md)                       |

## ⚡ Quick Start

### Sign & Verify (HMAC)

```javascript
secret  = jwtGenerateSecret( 256 );
token   = jwtCreate( { sub: "user-123", iss: "my-api", roles: [ "admin" ] }, secret, "HS256" );
payload = jwtVerify( token, secret, "HS256" );
writeOutput( payload.sub ); // user-123
```

### Sign & Verify (RSA)

```javascript
keys    = jwtGenerateKeyPair( "RS256" );
token   = jwtCreate( { sub: "user-123" }, keys.privateKey, "RS256" );
payload = jwtVerify( token, keys.publicKey, "RS256" );
```

### Fluent Builder

```javascript
token = jwtNew()
    .subject( "user-123" )
    .issuer( "my-api" )
    .audience( "mobile-client" )
    .claim( "roles", [ "admin", "user" ] )
    .expireIn( 3600 )
    .header( "kid", "v1" )
    .sign( secret, "HS256" );
```

### Encrypt & Decrypt (JWE)

```javascript
token   = jwtEncrypt( { sub: "user-123", ssn: "123-45-6789" }, secret, { keyAlgorithm: "dir", encAlgorithm: "A256GCM" } );
payload = jwtDecrypt( token, secret, { keyAlgorithm: "dir", encAlgorithm: "A256GCM" } );
```

## 📚 Usage Guides

* [Signing (JWS)](signing-jws.md) — HMAC, RSA, and EC signing patterns
* [Encryption (JWE)](encryption-jwe.md) — RSA-OAEP and symmetric encryption
* [Key Management](key-management.md) — the named key registry and runtime keys
* [Fluent Builder](fluent-builder.md) — `jwtNew()` chainable API walkthrough
* [Key Rotation](key-rotation.md) — `kid`-based rotation patterns
* [Security Best Practices](security-best-practices.md) — allowlists, key sizes, clock skew
* [Configuration](configuration.md) — full ModuleConfig settings reference

## 🔌 Reference

* [Built-In Functions](reference/built-in-functions/README.md) — one page per BIF
* [Fluent API (JwtBuilder)](reference/fluent-api/README.md) — chainable methods reference
* [Algorithms](reference/algorithms.md) — supported JWS/JWE algorithm tables

## ✅ Requirements

* **BoxLang Runtime** 1.0.0+

## 📄 License

Licensed under the [BoxLang Plus Subscription License](https://www.boxlang.io/license).
