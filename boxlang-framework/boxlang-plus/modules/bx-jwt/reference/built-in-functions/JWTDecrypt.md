# JWTDecrypt

Decrypts a JWE token and returns the decrypted claims as a struct (or the inner payload for nested JWTs).

## Method Signature

```
JWTDecrypt( token, [key], [options] )
```

### Arguments

| Argument  | Type     | Required | Description                                                           | Default |
| --------- | -------- | -------- | --------------------------------------------------------------------- | ------- |
| `token`   | `string` | Yes      | Compact JWE token string.                                             |         |
| `key`     | `any`    | No       | Decryption key — named key, RSA private-key PEM, or symmetric secret. | `null`  |
| `options` | `struct` | No       | See options table below.                                              | `{}`    |

#### Options

| Option         | Type     | Description                            | Default        |
| -------------- | -------- | -------------------------------------- | -------------- |
| `keyAlgorithm` | `string` | Expected key management algorithm.     | `RSA-OAEP-256` |
| `encAlgorithm` | `string` | Expected content encryption algorithm. | `A256GCM`      |

### Returns

The decrypted claims as a `struct` (or the raw inner payload for nested JWTs — typically a string you then pass into `jwtVerify()`).

## Throws

* `bxjwt.JWTEncryptionException` — decryption or authentication-tag failure
* `bxjwt.JWTParseException` — malformed token

## Examples

```javascript
// RSA-OAEP decryption
payload = jwtDecrypt( token, rsaPrivateKeyPem, {
    keyAlgorithm: "RSA-OAEP-256",
    encAlgorithm: "A256GCM"
} );

// Direct symmetric decryption
payload = jwtDecrypt( token, secret32bytes, {
    keyAlgorithm: "dir",
    encAlgorithm: "A256GCM"
} );
```

## Related

* [JWTEncrypt()](JWTEncrypt.md)
* [Encryption (JWE) Guide](../../encryption-jwe.md)
