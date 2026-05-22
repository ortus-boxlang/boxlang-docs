---
description: JwtBuilder fluent API reference — chainable methods returned by jwtNew().
---

# Fluent API (JwtBuilder)

`jwtNew()` returns a `JwtBuilder` object that lets you compose a JWT one method at a time. Every claim/header method returns `this` so calls can be chained. Terminate the chain with `.sign()` (JWS) or `.encrypt()` (JWE) to produce the compact token string.

## Claim Methods

| Method                 | Signature                  | Description                                                         |
| ---------------------- | -------------------------- | ------------------------------------------------------------------- |
| `subject( val )`       | `(any) → this`             | Sets the `sub` claim.                                               |
| `issuer( val )`        | `(any) → this`             | Sets the `iss` claim.                                               |
| `audience( val )`      | `(string\|array) → this`   | Sets the `aud` claim. Accepts a string or an array of audiences.    |
| `claim( key, val )`    | `(string, any) → this`     | Sets an arbitrary custom claim.                                     |
| `withPayload( val )`   | `(struct) → this`          | Replaces the entire payload with the given struct.                  |
| `expireIn( seconds )`  | `(numeric) → this`         | Sets `exp` as `now() + seconds`.                                    |
| `expireAt( date )`     | `(date) → this`            | Sets `exp` to an explicit DateTime.                                 |
| `issuedNow()`          | `() → this`                | Sets `iat` to `now()`.                                              |
| `issuedAt( date )`     | `(date) → this`            | Sets `iat` to an explicit DateTime.                                 |
| `notBefore( date )`    | `(date) → this`            | Sets the `nbf` claim.                                               |
| `jti( val )`           | `(any) → this`             | Sets the `jti` (JWT ID) claim.                                      |

## Header Methods

| Method               | Signature              | Description                                                            |
| -------------------- | ---------------------- | ---------------------------------------------------------------------- |
| `header( key, val )` | `(string, any) → this` | Sets a JOSE header field (e.g. `kid`, `typ`, `cty`).                   |

## Terminal Methods

| Method                                                | Signature                                       | Returns  | Description                                          |
| ----------------------------------------------------- | ----------------------------------------------- | -------- | ---------------------------------------------------- |
| `sign( [key], [algorithm] )`                          | `(any?, string?) → string`                      | `string` | Signs and returns the compact JWS string.            |
| `encrypt( [key], [keyAlgorithm], [encAlgorithm] )`    | `(any?, string?, string?) → string`             | `string` | Encrypts and returns the compact JWE string.         |

When the terminal arguments are omitted, the builder falls back to the module's `defaultSigningKey` / `defaultAlgorithm` (or `defaultEncryptionKey` / `defaultKeyAlgorithm` / `defaultEncAlgorithm` for `.encrypt()`).

## Examples

```javascript
// HMAC with custom headers
token = jwtNew()
    .subject( "alice" )
    .claim( "tenant", "acme-corp" )
    .expireIn( 900 )
    .header( "kid", "signing-key-v2" )
    .sign( secret, "HS256" );

// RSA with all standard claims
token = jwtNew()
    .subject( "svc-account" )
    .issuer( "auth-service" )
    .audience( [ "api", "analytics" ] )
    .issuedNow()
    .expireIn( 3600 )
    .jti( createUUID() )
    .sign( privateKeyPem, "RS256" );

// JWE encryption
token = jwtNew()
    .subject( "patient-456" )
    .claim( "phi", { dob: "1990-01-15", ssn: "xxx-xx-1234" } )
    .encrypt( secret, "dir", "A256GCM" );

// Re-use an existing payload struct
payload = { sub: "user-1", iss: "my-api", roles: [ "admin" ] };
token   = jwtNew().withPayload( payload ).expireIn( 3600 ).sign( secret, "HS256" );
```

## Related

* [JWTNew()](../built-in-functions/JWTNew.md) — the BIF that returns the builder
* [Fluent Builder Guide](../../fluent-builder.md)
* [JWTCreate()](../built-in-functions/JWTCreate.md) — functional equivalent
* [JWTEncrypt()](../built-in-functions/JWTEncrypt.md) — functional equivalent for JWE
