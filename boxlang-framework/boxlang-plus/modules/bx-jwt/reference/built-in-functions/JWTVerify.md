[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `JWTVerify`

Verifies a JWS signature and validates standard claims. Returns the decoded claims struct on success. Throws on any failure.

## Method Signature

```
JWTVerify( token, [key], [algorithm], [options] )
```

### Arguments

| Argument    | Type     | Required | Description                                                                                                 | Default |
| ----------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------- | ------- |
| `token`     | `string` | Yes      | Compact JWS token string to verify.                                                                          |         |
| `key`       | `any`    | No       | Verification key. Optional when `defaultVerifyKey` (or `defaultSigningKey` for HMAC) is configured.         | `null`  |
| `algorithm` | `string` | No       | Expected algorithm. Resolved from key metadata or token header if omitted.                                   | `null`  |
| `options`   | `struct` | No       | `claims` (struct of expected claim values), `clockSkew` (seconds tolerance for `exp`/`nbf`).                | `{}`    |

### Returns

The verified claims as a `struct`.

### Throws

* `bxjwt.JWTVerificationException` — bad signature or claim mismatch
* `bxjwt.JWTExpiredException` — token is expired
* `bxjwt.JWTNotYetValidException` — token not yet valid (`nbf`)
* `bxjwt.JWTParseException` — malformed token

## Examples

```javascript
// Basic verify
payload = jwtVerify( token, secret, "HS256" );

// With claim assertions
payload = jwtVerify( token, secret, "HS256", {
    claims: { iss: "my-api", aud: "mobile-app" }
} );

// With explicit clock skew
payload = jwtVerify( token, secret, "HS256", { clockSkew: 30 } );

// RSA verify with public key
payload = jwtVerify( token, publicKeyPem, "RS256" );
```

## Related

* [JWTValidate()](JWTValidate.md) — boolean version (no throw)
* [JWTCreate()](JWTCreate.md) — signed-token issuer
* [JWTDecode()](JWTDecode.md) — read header to choose key before verifying
* [Security Best Practices](../../security-best-practices.md)
