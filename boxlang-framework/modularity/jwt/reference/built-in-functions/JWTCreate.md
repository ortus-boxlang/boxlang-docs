[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `JWTCreate`

Signs a payload struct and returns a compact JWS (signed JWT) token string.

## Method Signature

```
JWTCreate( payload, [key], [algorithm], [options] )
```

### Arguments

| Argument    | Type     | Required | Description                                                                                                          | Default |
| ----------- | -------- | -------- | -------------------------------------------------------------------------------------------------------------------- | ------- |
| `payload`   | `struct` | Yes      | Claims to encode in the token.                                                                                       |         |
| `key`       | `any`    | No       | Signing key — named key from the registry, HMAC secret, or PEM/JWK string. Optional when `defaultSigningKey` is set. | `null`  |
| `algorithm` | `string` | No       | Signing algorithm (e.g. `HS256`, `RS256`, `ES256`). Resolved from key metadata or `defaultAlgorithm` if omitted.     | `null`  |
| `options`   | `struct` | No       | `headers` (custom JOSE headers struct), `generateIat` (boolean), `generateJti` (boolean).                            | `{}`    |

### Returns

A compact JWS string of the form `<header>.<payload>.<signature>`.

## Examples

```javascript
// HMAC signing
token = jwtCreate( { sub: "u1", iss: "api" }, "my-32-byte-secret-goes-here!!!", "HS256" );

// RSA signing with a custom kid header
token = jwtCreate( { sub: "u1" }, privateKeyPem, "RS256", { headers: { kid: "rsa-v1" } } );

// Use a named key from the registry — algorithm resolved from key metadata
token = jwtCreate( { sub: "u1" }, "myapp-hmac" );

// Disable auto-generated iat for this call
token = jwtCreate( { sub: "u1", iat: specificDate }, secret, "HS256", { generateIat: false } );
```

## Related

* [JWTVerify()](JWTVerify.md) — verify the token signature & claims
* [JWTDecode()](JWTDecode.md) — inspect headers/claims without verifying
* [JWTNew()](JWTNew.md) — fluent builder alternative
* [JWTRefresh()](JWTRefresh.md) — re-issue with fresh time claims
* [Signing (JWS) Guide](../../signing-jws.md)
