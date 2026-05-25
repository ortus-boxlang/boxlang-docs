---
icon: lock
description: Encrypt and decrypt JWTs using RSA-OAEP key wrap or direct symmetric encryption.
---

# Encryption (JWE)

A JSON Web Encryption (JWE) token has its payload encrypted — even the issuer cannot read it without the decryption key. Use JWE when the claims contain sensitive data (PII, PHI, secrets) that must remain confidential in transit *and* at rest in client storage.

`bx-jwt` supports two encryption modes:

* **RSA-OAEP-256 + A256GCM** — asymmetric key wrapping. Anyone with the RSA public key can encrypt; only the private-key holder can decrypt.
* **`dir` + A256GCM** — direct symmetric encryption with a 256-bit (32-byte) shared key.

## RSA Key Wrapping (Asymmetric)

```javascript
keys = jwtGenerateKeyPair( "RS256" );  // 2048-bit RSA pair

// Encrypt with the public key (anyone can do this)
token = jwtEncrypt( { sub: "u1", ssn: "123-45-6789" }, keys.publicKey, {
    keyAlgorithm: "RSA-OAEP-256",
    encAlgorithm: "A256GCM"
} );

// Decrypt with the private key (only the holder can do this)
payload = jwtDecrypt( token, keys.privateKey, {
    keyAlgorithm: "RSA-OAEP-256",
    encAlgorithm: "A256GCM"
} );
```

This pattern is ideal when many producers must encrypt for a single consumer (e.g. a central service that receives sensitive payloads from many clients).

## Direct Symmetric Encryption

When both ends of the conversation can hold the same secret, `dir` is faster and produces smaller tokens.

```javascript
secret = jwtGenerateSecret( 256 );  // 32 bytes for A256GCM

token   = jwtEncrypt( { sub: "u1" }, secret, {
    keyAlgorithm: "dir",
    encAlgorithm: "A256GCM"
} );

payload = jwtDecrypt( token, secret, {
    keyAlgorithm: "dir",
    encAlgorithm: "A256GCM"
} );
```

{% hint style="warning" %}
The `dir` mode requires the encryption key to be exactly the right size for the content encryption algorithm. A256GCM = 32 bytes (256 bits).
{% endhint %}

## Nested JWT (Sign → Encrypt)

When you need both **integrity** (proof of issuer) and **confidentiality** (encrypted payload), sign the token first and then encrypt the result. The standard `cty: "JWT"` header tells consumers the JWE wraps a JWS.

```javascript
// 1. Sign the inner JWS
signed = jwtCreate( { sub: "u1", role: "admin" }, innerPrivKey, "RS256", {
    headers: { cty: "JWT" }
} );

// 2. Encrypt the signed token as the outer JWE
encrypted = jwtEncrypt( signed, outerPubKey, {
    keyAlgorithm : "RSA-OAEP-256",
    encAlgorithm : "A256GCM",
    headers      : { cty: "JWT" }
} );

// On the consumer side:
decrypted = jwtDecrypt( encrypted, outerPrivKey, {
    keyAlgorithm : "RSA-OAEP-256",
    encAlgorithm : "A256GCM"
} );
payload = jwtVerify( decrypted, innerPubKey, "RS256" );
```

## Fluent Builder for JWE

The same fluent builder used for signing also produces JWEs — just call `.encrypt()` to terminate the chain:

```javascript
token = jwtNew()
    .subject( "patient-456" )
    .claim( "phi", { dob: "1990-01-15", ssn: "xxx-xx-1234" } )
    .expireIn( 900 )
    .encrypt( secret, "dir", "A256GCM" );
```

## Related

* [Signing (JWS)](signing-jws.md)
* [Key Management](key-management.md)
* [Security Best Practices](security-best-practices.md)
* [JWTEncrypt()](reference/built-in-functions/JWTEncrypt.md)
* [JWTDecrypt()](reference/built-in-functions/JWTDecrypt.md)
