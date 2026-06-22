---
description: All Built-In Functions registered by the bx-jwt module.
---

# Built-In Functions

| Function                                      | Description                                                        |
| --------------------------------------------- | ------------------------------------------------------------------ |
| [JWTCreate()](JWTCreate.md)                   | Signs a payload and returns a compact JWS token string.            |
| [JWTVerify()](JWTVerify.md)                   | Verifies a JWS signature and claims; throws on failure.            |
| [JWTValidate()](JWTValidate.md)               | Boolean verification — returns true/false instead of throwing.     |
| [JWTDecode()](JWTDecode.md)                   | Decodes a JWS without verifying the signature.                     |
| [JWTRefresh()](JWTRefresh.md)                 | Re-issues a token with fresh `iat`, `jti`, and optional new `exp`. |
| [JWTEncrypt()](JWTEncrypt.md)                 | Encrypts a payload as a compact JWE token.                         |
| [JWTDecrypt()](JWTDecrypt.md)                 | Decrypts a JWE token and returns the claims struct.                |
| [JWTNew()](JWTNew.md)                         | Returns a fluent `JwtBuilder` for chainable token construction.    |
| [JWTGenerateSecret()](JWTGenerateSecret.md)   | Generates a cryptographically random Base64 HMAC secret.           |
| [JWTGenerateKeyPair()](JWTGenerateKeyPair.md) | Generates an RSA or EC key pair as PEM strings.                    |
