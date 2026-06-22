# JWTEncrypt

Encrypts a payload as a compact JWE (JSON Web Encryption) token. The payload can be a struct, a string (for nested JWT-in-JWE), or any value the module can serialize.

## Method Signature

```
JWTEncrypt( payload, [key], [options] )
```

### Arguments

| Argument  | Type     | Required | Description                                                          | Default |
| --------- | -------- | -------- | -------------------------------------------------------------------- | ------- |
| `payload` | `any`    | Yes      | Claims struct or value to encrypt.                                   |         |
| `key`     | `any`    | No       | Encryption key — named key, RSA public-key PEM, or symmetric secret. | `null`  |
| `options` | `struct` | No       | See options table below.                                             | `{}`    |

#### Options

| Option         | Type     | Description                                                           | Default        |
| -------------- | -------- | --------------------------------------------------------------------- | -------------- |
| `keyAlgorithm` | `string` | Key management algorithm: `RSA-OAEP-256` or `dir` (direct symmetric). | `RSA-OAEP-256` |
| `encAlgorithm` | `string` | Content encryption algorithm: `A256GCM`.                              | `A256GCM`      |
| `headers`      | `struct` | Custom JOSE headers (e.g. `kid`, `cty` for nested JWTs).              | `{}`           |

### Returns

A compact JWE string of the form `<header>.<encrypted-key>.<iv>.<ciphertext>.<tag>`.

## Examples

```javascript
// RSA key wrapping (asymmetric encryption)
token = jwtEncrypt( { sub: "u1", ssn: "123-45-6789" }, rsaPublicKeyPem, {
    keyAlgorithm: "RSA-OAEP-256",
    encAlgorithm: "A256GCM"
} );

// Direct symmetric encryption (32-byte key for A256GCM)
token = jwtEncrypt( { sub: "u1" }, secret32bytes, {
    keyAlgorithm: "dir",
    encAlgorithm: "A256GCM"
} );

// Nested JWT — sign first, then encrypt with cty: "JWT"
signed    = jwtCreate( { sub: "u1" }, signingKey, "RS256" );
encrypted = jwtEncrypt( signed, encryptionPubKey, {
    keyAlgorithm: "RSA-OAEP-256",
    encAlgorithm: "A256GCM",
    headers: { cty: "JWT" }
} );
```

## Related

* [JWTDecrypt()](JWTDecrypt.md) — counterpart for decryption
* [Encryption (JWE) Guide](../../encryption-jwe.md)
* [Algorithms](../algorithms.md)
